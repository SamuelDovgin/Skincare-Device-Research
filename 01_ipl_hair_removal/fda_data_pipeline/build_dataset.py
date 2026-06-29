#!/usr/bin/env python3
"""
Assemble the analysis dataset from the enriched data.

Reliable fields (from API + text): brand/applicant, models (device_name),
decision date, product code, pulse modes, multi_pulse_flag, FDA PDF link, and
candidate spec values (fluence/energy/spot/wavelength/pulse) extracted by regex.

IMPORTANT — fluence/energy candidates are NOT authoritative. The 510(k)
comparison tables interleave the subject device with predicate + reference
devices, and pdftotext linearizes them so no regex reliably isolates the
subject's value (validated: max/first/mode each fail on different filings). So:
  - VERIFIED rows (hand-read from the filing, listed in verified_specs.json)
    carry exact subject-device values.
  - AUTO rows carry the regex candidate (max J/cm2 found anywhere in the filing)
    flagged confidence='auto' — treat as approximate, verify via the PDF link.

Outputs data/dataset_full.json consumed by make_markdown.py.
"""
import csv, json, os, re

HERE = os.path.dirname(os.path.abspath(__file__))
DATA = os.path.join(HERE, "data")


def pdf_summary_url(k):
    yy = k[1:3]; n = int(yy)
    d = f"pdf{n}" if n >= 2 else "pdf"
    return f"https://www.accessdata.fda.gov/cdrh_docs/{d}/{k}.pdf"


def fda_page_url(k):
    return ("https://www.accessdata.fda.gov/scripts/cdrh/cfdocs/cfpmn/"
            f"pmn.cfm?ID={k}")


def light_source(text, device_name=""):
    """Classify the device's emitter. OHT (OTC hair removal) contains both true
    IPL (Xenon broadband flashlamp) AND diode-laser/LED devices that are NOT IPL
    but get swept in. Decide by the language in the filing + the device name."""
    t = (device_name + " " + text).lower()
    ipl = (t.count("xenon") + t.count("intense pulsed light") + t.count("flashlamp")
           + len(re.findall(r"\bipl\b", t)))          # short summaries just say "IPL"
    diode = (t.count("diode laser") + t.count("laser diode")
             + t.count("diode led") + t.count("semiconductor laser"))
    # a single narrow IR wavelength (808/810/780-850) with no broadband range = diode
    narrow = bool(re.search(r"\b8[01]0\s*nm\b", t)) and "xenon" not in t
    if diode >= 1 or (narrow and ipl == 0):
        return "diode"
    if ipl >= 1:
        return "ipl"
    return "unknown"


def candidates(text):
    t = text.lower()
    flu = sorted({float(x) for x in re.findall(r"(\d+\.?\d*)\s*j\s*/?\s*cm", t)
                  if 0.3 <= float(x) <= 60})
    eng = sorted({float(x) for x in re.findall(r"(\d+\.?\d*)\s*j\b", t)
                  if 1 <= float(x) <= 200})
    spot = sorted({float(x) for x in re.findall(r"(\d+\.?\d*)\s*cm\s*[²2]", t)
                   if 0.2 <= float(x) <= 60})
    wl = sorted({f"{a}-{b}" for a, b in
                 re.findall(r"(\d{3,4})\s*[-–~]\s*(\d{3,4})\s*nm", t)})
    ms = sorted({float(x) for x in re.findall(r"(\d+\.?\d*)\s*ms", t)
                 if 0.05 <= float(x) <= 120})
    return {
        "fluence_max": max(flu) if flu else None,
        "fluence_all": flu,
        "energy_max": max(eng) if eng else None,
        "spot_sizes": spot,
        "wavelengths": wl,
        "pulse_ms": f"{min(ms)}-{max(ms)}" if ms else "",
    }


def main():
    enr = {r["k_number"]: r
           for r in csv.DictReader(open(os.path.join(DATA, "pulse_specs_enriched.csv")))}
    recs = json.load(open(os.path.join(DATA, "fda_510k_ipl_latest.json")))

    vpath = os.path.join(HERE, "verified_specs.json")
    verified = json.load(open(vpath)) if os.path.exists(vpath) else {}

    out = []
    for r in recs:
        k = r["k_number"]
        e = enr.get(k, {})
        txtp = os.path.join(DATA, "pdf_text", f"{k}.txt")
        text = open(txtp).read() if os.path.exists(txtp) else ""
        cand = candidates(text)
        lsrc = light_source(text, r.get("device_name", "")) if text else "unknown"
        row = {
            "k_number": k,
            "brand": r.get("applicant", ""),
            "device_name": r.get("device_name", ""),
            "decision_date": r.get("decision_date", ""),
            "product_code": r.get("product_code", ""),
            "pulse_modes": e.get("pulse_modes", ""),
            "multi_pulse": e.get("multi_pulse_flag", ""),
            "pdf_status": e.get("pdf_status", ""),
            "pdf_summary_url": pdf_summary_url(k),
            "fda_page_url": fda_page_url(k),
            **{f"auto_{kk}": vv for kk, vv in cand.items()},
        }
        if k in verified:
            v = verified[k]
            row.update({
                "confidence": "verified",
                "light_source": v.get("light_source", lsrc),
                "fluence_jcm2": v.get("fluence_jcm2"),
                "energy_j": v.get("energy_j"),
                "spot_cm2": v.get("spot_cm2"),
                "wavelength_nm": v.get("wavelength_nm"),
                "pulse_ms": v.get("pulse_ms"),
                "models": v.get("models", r.get("device_name", "")),
                "note": v.get("note", ""),
            })
        else:
            row.update({
                "confidence": "auto",
                "light_source": lsrc,
                "fluence_jcm2": cand["fluence_max"],
                "energy_j": cand["energy_max"],
                "spot_cm2": max(cand["spot_sizes"]) if cand["spot_sizes"] else None,
                "wavelength_nm": "; ".join(cand["wavelengths"]),
                "pulse_ms": cand["pulse_ms"],
                "models": r.get("device_name", ""),
                "note": "",
            })
        out.append(row)

    with open(os.path.join(DATA, "dataset_full.json"), "w") as f:
        json.dump(out, f, indent=2)
    nver = sum(1 for r in out if r["confidence"] == "verified")
    print(f"Built dataset_full.json: {len(out)} devices ({nver} verified, "
          f"{len(out)-nver} auto)")


if __name__ == "__main__":
    main()
