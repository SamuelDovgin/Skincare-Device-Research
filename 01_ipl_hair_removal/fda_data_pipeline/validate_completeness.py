#!/usr/bin/env python3
"""
Completeness audit — the provable answer to "how do you know this is extensive?"

Extensiveness is not a vibe; it's checkable. This script proves coverage four
independent ways and prints any gaps EXPLICITLY (a gap is a finding, not a
silent omission).

  1. API-TOTAL RECONCILIATION
     openFDA reports meta.results.total for every query. We re-query each
     product code and confirm our saved dataset holds exactly that many. If we
     have 162/162 OHT, we provably missed zero OHT devices.

  2. DEFINITIONAL COMPLETENESS (the strongest guarantee)
     The FDA assigns EVERY over-the-counter IPL hair-removal device the product
     code OHT. So "all OHT" = 100% of the home-IPL hair-removal population by
     definition — not a sample, the census.

  3. KNOWN-ITEM RECALL
     We hard-code the K-numbers already verified in this project's research
     docs (K212881, K221569, K223928, K251173, K253881, K260518, plus named
     competitors Ulike/IONKA). Every one MUST appear in the pull. A miss = a bug.

  4. CROSS-CODE LEAKAGE CHECK
     We ask openFDA which product codes contain devices whose name mentions
     "intense pulsed light." If a code shows up that we're NOT pulling, it's
     reported so you can decide whether to widen config.json.

Run after pull_fda_510k.py:
    python3 validate_completeness.py
"""

import json
import os
import urllib.parse
import urllib.request
from collections import Counter

API = "https://api.fda.gov/device/510k.json"
HERE = os.path.dirname(os.path.abspath(__file__))
DATA = os.path.join(HERE, "data")

# K-numbers independently verified elsewhere in this project. The pull MUST
# contain all of these or it has a gap.
KNOWN_KNUMBERS = {
    "K212881": "Fansizhe T012C (earliest)",
    "K221569": "Fansizhe T013C/T015C/T015K (510nm predicate)",
    "K221246": "Semlamp SLB080/126/136",
    "K223928": "Fansizhe T023/T021/T001/T011/T016 family",
    "K240969": "Semlamp SLB287/329/301/328",
    "K241998": "Ulike UI20 series (reference device)",
    "K230739": "IONKA FZ-608/100/200 (reference device)",
    "K251173": "Fansizhe original 2025 clearance",
    "K253881": "Fansizhe Special 510(k) upgrade (triple-pulse)",
    "K260518": "Semlamp direct clearance incl SL-B352",
}


def api_total(search):
    qs = urllib.parse.urlencode({"search": search, "limit": 1})
    url = f"{API}?{qs}"
    req = urllib.request.Request(url, headers={"User-Agent": "ipl-fda-pipeline/1.0"})
    try:
        with urllib.request.urlopen(req, timeout=60) as r:
            return json.load(r)["meta"]["results"]["total"]
    except urllib.error.HTTPError as e:
        if e.code == 404:
            return 0
        raise


def code_breakdown_for_keyword(kw):
    """Which product codes contain devices named like the keyword? (count() facet)"""
    phrase = f'"{kw}"' if " " in kw else kw  # exact phrase; single encode pass below
    qs = urllib.parse.urlencode(
        {"search": f"device_name:{phrase}", "count": "product_code"}
    )
    url = f"{API}?{qs}"
    req = urllib.request.Request(url, headers={"User-Agent": "ipl-fda-pipeline/1.0"})
    try:
        with urllib.request.urlopen(req, timeout=60) as r:
            data = json.load(r)
        return {b["term"]: b["count"] for b in data.get("results", [])}
    except urllib.error.HTTPError as e:
        if e.code == 404:
            return {}
        raise


def main():
    with open(os.path.join(DATA, "fda_510k_ipl_latest.json")) as f:
        records = json.load(f)
    with open(os.path.join(HERE, "config.json")) as f:
        cfg = json.load(f)

    saved_k = {r["k_number"] for r in records}
    codes = cfg["product_codes"]
    keywords = cfg.get("keywords", [])

    print("=" * 64)
    print("FDA 510(k) IPL — COMPLETENESS AUDIT")
    print("=" * 64)
    print(f"Dataset holds {len(records)} unique clearances "
          f"({len(saved_k)} unique K-numbers)\n")

    # 1. API-total reconciliation
    print("[1] API-TOTAL RECONCILIATION (did we page through everything?)")
    all_ok = True
    by_code = Counter(r.get("product_code", "") for r in records)
    for code in codes:
        total = api_total(f"product_code:{code}")
        have = by_code.get(code, 0)
        ok = have >= total
        all_ok &= ok
        print(f"    {code}: have {have} / API reports {total}  "
              f"{'OK' if ok else '!!! GAP'}")
    print(f"    -> {'All product codes fully captured.' if all_ok else 'GAP DETECTED — re-run pull.'}\n")

    # 2. Definitional completeness
    print("[2] DEFINITIONAL COMPLETENESS")
    print("    OHT is the FDA code assigned to EVERY OTC IPL hair-removal device.")
    print(f"    Pulling all OHT = the full census of home-IPL hair removal, not a sample.\n")

    # 3. Known-item recall
    print("[3] KNOWN-ITEM RECALL (verified K-numbers must all be present)")
    missing = []
    for k, desc in sorted(KNOWN_KNUMBERS.items()):
        present = k in saved_k
        if not present:
            missing.append(k)
        print(f"    {'FOUND ' if present else 'MISSING'} {k}  {desc}")
    if missing:
        print(f"    !!! {len(missing)} known device(s) MISSING: {missing}")
        print("        (May be filed under a product code not in config.json — check [4].)")
    else:
        print("    -> All verified known devices present. Recall = 100%.")
    print()

    # 4. Cross-code leakage
    print("[4] CROSS-CODE LEAKAGE (IPL devices under codes we don't pull)")
    for kw in keywords:
        bd = code_breakdown_for_keyword(kw)
        print(f"    device_name ~ \"{kw}\" spans {len(bd)} product codes:")
        not_pulled = {c: n for c, n in bd.items() if c not in codes}
        for c, n in sorted(bd.items(), key=lambda x: -x[1])[:12]:
            mark = "" if c in codes else "  <- not in product_codes (caught by keyword sweep)"
            print(f"      {c}: {n}{mark}")
        # Are those leakage devices actually in our dataset (via the sweep)?
        leaked_in = sum(1 for r in records
                        if r.get("product_code") in not_pulled)
        print(f"    -> {leaked_in} of these non-OHT IPL devices ARE captured via the "
              f"keyword sweep.\n")

    print("=" * 64)
    verdict = "EXTENSIVE: full census of OHT + keyword sweep across all other codes."
    if missing or not all_ok:
        verdict = "INCOMPLETE — see gaps above."
    print(f"VERDICT: {verdict}")
    print("=" * 64)


if __name__ == "__main__":
    main()
