#!/usr/bin/env python3
"""
Pulse-mode + spec enrichment for the FDA 510(k) IPL dataset.

WHY: the openFDA API only returns metadata (who/when/what code). The thing you
actually care about — single vs double vs triple pulse, and the real per-pulse
fluence — lives in each filing's PDF summary. Multi-pulse devices advertise the
SUMMED energy of a pulse train as one big "joule" number; the true single-pulse
output is a fraction of that. This script finds the PDFs, reads them, and flags
exactly which clearances use multi-pulse so you know when the headline number is
inflated.

WHAT IT DOES, per clearance:
  1. Resolves the FDA PDF summary URL (cdrh_docs/pdf{YY}/{K}.pdf) and downloads
     it (cached locally so re-runs are fast).
  2. Extracts text with `pdftotext`.
  3. Detects pulse modes: single / double-dual / triple-three / multi / SHR,
     and captures the exact sentence ("snippet") so you can read it yourself.
  4. Pulls candidate spec values: fluence (J/cm2), energy (J), wavelength (nm),
     pulse duration (ms).
  5. Sets multi_pulse_flag = True when dual/triple/multi pulse is present ->
     "advertised single-pulse joules are likely a summed pulse train."
  6. Records pdf_status so coverage gaps are EXPLICIT, never silent
     (ok / no_text_layer_needs_ocr / download_failed / not_found).

Honest scope: this AUTOMATES detection + candidate extraction + the exact
snippet. For a device flagged multi_pulse, the authoritative single-pulse value
still warrants a human glance at the linked filing — but you'll know which ~handful
of the 162 to actually open, instead of all of them.

Usage:
    python3 enrich_pulse_specs.py                  # OHT, decided 2020+ (default)
    python3 enrich_pulse_specs.py --codes OHT OHS
    python3 enrich_pulse_specs.py --since 2015     # earlier years (more scanned PDFs)
    python3 enrich_pulse_specs.py --all            # every record in latest.json
"""

import argparse
import json
import os
import re
import subprocess
import urllib.request

HERE = os.path.dirname(os.path.abspath(__file__))
DATA = os.path.join(HERE, "data")
CACHE = os.path.join(DATA, "pdf_cache")
TXT = os.path.join(DATA, "pdf_text")

PULSE_PATTERNS = {
    "triple": r"(triple[\s-]?pulse|three[\s-]?pulse|3[\s-]?pulse|tri[\s-]?pulse)",
    "double": r"(dual[\s-]?pulse|double[\s-]?pulse|two[\s-]?pulse|2[\s-]?pulse|bi[\s-]?pulse)",
    "single": r"single[\s-]?pulse",
    "multi":  r"(multi[\s-]?pulse|sub[\s-]?pulse|pulse[\s-]?train|pulse[\s-]?stack|stacked[\s-]?pulse|burst)",
    "shr":    r"\bshr\b|super[\s-]?hair[\s-]?removal",
}


def pdf_url_candidates(k):
    """FDA CDRH PDF dir convention varies by K-number year prefix:
       2002-2009 -> pdfN (no leading zero, e.g. K08xxxx -> pdf8)
       2010+     -> pdfNN (e.g. K25xxxx -> pdf25)
       2000/2001 -> pdf / pdf1
    Return ordered candidates; download_pdf tries each until one resolves."""
    yy = k[1:3]
    base = "https://www.accessdata.fda.gov/cdrh_docs"
    n = int(yy)
    cands = []
    if n >= 2:
        cands.append(f"{base}/pdf{n}/{k}.pdf")   # pdf2..pdf25 (primary)
    cands.append(f"{base}/pdf{yy}/{k}.pdf")        # pdf08 form (older convention)
    cands.append(f"{base}/pdf/{k}.pdf")            # 2000-era flat dir
    cands.append(f"{base}/pdf1/{k}.pdf")
    # de-dup preserving order
    seen, out = set(), []
    for u in cands:
        if u not in seen:
            seen.add(u); out.append(u)
    return out


def pdf_summary_url(k):
    """Primary direct-PDF URL (best guess) for display/linking."""
    return pdf_url_candidates(k)[0]


def download_pdf(k):
    os.makedirs(CACHE, exist_ok=True)
    path = os.path.join(CACHE, f"{k}.pdf")
    if os.path.exists(path) and os.path.getsize(path) > 1000:
        return path, "ok"
    last = "not_found"
    for url in pdf_url_candidates(k):
        try:
            req = urllib.request.Request(url, headers={"User-Agent": "ipl-fda-pipeline/1.0"})
            with urllib.request.urlopen(req, timeout=90) as r:
                data = r.read()
            if len(data) < 1000:
                last = "not_found"
                continue
            with open(path, "wb") as f:
                f.write(data)
            return path, "ok"
        except urllib.error.HTTPError as e:
            last = "not_found" if e.code == 404 else f"download_failed_{e.code}"
        except Exception:
            last = "download_failed"
    return None, last


def ocr_pdf(pdf_path, k):
    """Rasterize the PDF to images (pdftoppm) and OCR them (tesseract).
    Used only when the PDF has no embedded text layer (scanned filings)."""
    import tempfile, glob
    with tempfile.TemporaryDirectory() as td:
        prefix = os.path.join(td, "pg")
        try:
            subprocess.run(["pdftoppm", "-r", "300", "-png", pdf_path, prefix],
                           capture_output=True, timeout=300, check=True)
        except Exception:
            return ""
        chunks = []
        for img in sorted(glob.glob(prefix + "*.png")):
            try:
                r = subprocess.run(["tesseract", img, "-", "--psm", "6"],
                                   capture_output=True, timeout=180)
                chunks.append(r.stdout.decode("utf-8", "ignore"))
            except Exception:
                continue
    return "\n".join(chunks)


def extract_text(pdf_path, k):
    os.makedirs(TXT, exist_ok=True)
    try:
        out = subprocess.run(
            ["pdftotext", "-q", pdf_path, "-"],
            capture_output=True, timeout=120,
        )
        text = out.stdout.decode("utf-8", "ignore")
    except Exception:
        text = ""
    status = "ok"
    if len(text.strip()) < 200:  # scanned image PDF -> OCR it
        ocr_text = ocr_pdf(pdf_path, k)
        if len(ocr_text.strip()) >= 200:
            text, status = ocr_text, "ok_ocr"
        else:
            return "", "no_text_layer_needs_ocr"
    with open(os.path.join(TXT, f"{k}.txt"), "w") as f:
        f.write(text)
    return text, status


def snippet(text_lower, pattern, width=90):
    m = re.search(pattern, text_lower)
    if not m:
        return ""
    s = max(0, m.start() - width)
    e = min(len(text_lower), m.end() + width)
    return re.sub(r"\s+", " ", text_lower[s:e]).strip()


def best_values(text_lower):
    flu = re.findall(r"(\d+\.?\d*)\s*j\s*/?\s*cm", text_lower)
    eng = re.findall(r"(\d+\.?\d*)\s*j\b", text_lower)
    wl  = re.findall(r"(\d{3,4})\s*[-–]\s*(\d{3,4})\s*nm", text_lower)
    ms  = re.findall(r"(\d+\.?\d*)\s*ms", text_lower)
    def fnums(xs, lo, hi):
        v = sorted({float(x) for x in xs if lo <= float(x) <= hi})
        return v
    flu_v = fnums(flu, 0.5, 50)
    eng_v = fnums(eng, 1, 200)
    ms_v = fnums(ms, 0.1, 100)
    wl_r = sorted({f"{a}-{b}" for a, b in wl})
    return {
        "fluence_jcm2_candidates": ", ".join(str(x) for x in flu_v),
        "fluence_jcm2_max": max(flu_v) if flu_v else "",
        "energy_j_candidates": ", ".join(str(x) for x in eng_v),
        "energy_j_max": max(eng_v) if eng_v else "",
        "wavelength_nm": "; ".join(wl_r),
        "pulse_ms_range": f"{min(ms_v)}-{max(ms_v)}" if ms_v else "",
    }


def analyze(text):
    t = text.lower()
    modes = []
    snips = {}
    for name, pat in PULSE_PATTERNS.items():
        if re.search(pat, t):
            modes.append(name)
            sn = snippet(t, pat)
            if sn:
                snips[name] = sn
    multi = any(m in modes for m in ("double", "triple", "multi"))
    # most informative snippet: prefer the highest-order pulse-mode sentence
    for pref in ("triple", "double", "multi", "single", "shr"):
        if pref in snips:
            key_snip = snips[pref]
            break
    else:
        key_snip = ""
    out = {
        "pulse_modes": "+".join(modes) if modes else "(none detected)",
        "multi_pulse_flag": "YES" if multi else ("no" if modes else "unknown"),
        "pulse_snippet": key_snip,
    }
    out.update(best_values(t))
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--codes", nargs="*", default=["OHT"])
    ap.add_argument("--since", default="2020", help="min decision year (YYYY)")
    ap.add_argument("--all", action="store_true", help="ignore code/year filters")
    args = ap.parse_args()

    with open(os.path.join(DATA, "fda_510k_ipl_latest.json")) as f:
        records = json.load(f)

    if not args.all:
        records = [
            r for r in records
            if r.get("product_code") in args.codes
            and r.get("decision_date", "0")[:4] >= args.since
        ]
    print(f"Enriching {len(records)} clearances "
          f"({'ALL' if args.all else '+'.join(args.codes)+', '+args.since+'+'})\n")

    rows = []
    counts = {"ok": 0, "ok_ocr": 0, "no_text_layer_needs_ocr": 0,
              "not_found": 0, "download_failed": 0}
    for i, r in enumerate(records, 1):
        k = r["k_number"]
        pdf_path, dstat = download_pdf(k)
        if dstat == "ok":
            text, tstat = extract_text(pdf_path, k)
        else:
            text, tstat = "", dstat
        status = tstat
        counts[status] = counts.get(status, 0) + 1
        info = analyze(text) if text else {
            "pulse_modes": "", "multi_pulse_flag": "unknown", "pulse_snippet": "",
            "fluence_jcm2_candidates": "", "fluence_jcm2_max": "",
            "energy_j_candidates": "", "energy_j_max": "",
            "wavelength_nm": "", "pulse_ms_range": "",
        }
        row = {
            "k_number": k,
            "decision_date": r.get("decision_date", ""),
            "product_code": r.get("product_code", ""),
            "applicant": r.get("applicant", ""),
            "device_name": r.get("device_name", ""),
            "pdf_status": status,
            **info,
            "pdf_url": pdf_summary_url(k),
        }
        rows.append(row)
        flag = "  *** MULTI-PULSE ***" if info["multi_pulse_flag"] == "YES" else ""
        print(f"[{i}/{len(records)}] {k} {r.get('decision_date','')} "
              f"{status:24} {info['pulse_modes']}{flag}")

    import csv
    cols = list(rows[0].keys()) if rows else []
    out_csv = os.path.join(DATA, "pulse_specs_enriched.csv")
    with open(out_csv, "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=cols)
        w.writeheader()
        w.writerows(rows)

    multi = [r for r in rows if r["multi_pulse_flag"] == "YES"]
    print(f"\n=== SUMMARY ===")
    print(f"Parsed OK: {counts['ok']}   OCR'd: {counts['ok_ocr']}   "
          f"Still scanned/failed-OCR: {counts['no_text_layer_needs_ocr']}   "
          f"Missing PDF: {counts['not_found']}   "
          f"Failed: {counts['download_failed']}")
    print(f"MULTI-PULSE devices (advertised joules likely summed): {len(multi)}")
    for r in multi:
        print(f"  {r['k_number']} {r['applicant'][:35]:35} "
              f"modes={r['pulse_modes']}  maxFluence={r['fluence_jcm2_max']}")
    print(f"\nWrote: data/pulse_specs_enriched.csv")
    print(f"Full text of each filing cached in: data/pdf_text/<K>.txt")


if __name__ == "__main__":
    main()
