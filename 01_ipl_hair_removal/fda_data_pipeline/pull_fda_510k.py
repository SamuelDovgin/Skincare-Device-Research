#!/usr/bin/env python3
"""
FDA 510(k) IPL pipeline — automated pull from the openFDA device API.

No manual K-number lookup, no API key required. This queries the public
openFDA 510(k) endpoint by product code (and optional device-name keywords),
deduplicates, sorts newest-first, writes a flat CSV + full JSON, and diffs
against the previous run so you can see exactly what's NEW since last time.

Usage:
    python3 pull_fda_510k.py                 # use config.json defaults
    python3 pull_fda_510k.py --codes OHT     # override product codes
    python3 pull_fda_510k.py --since 2025-01-01
    python3 pull_fda_510k.py --keywords "intense pulsed light"

Outputs (in ./data/):
    fda_510k_ipl_latest.csv     # human/spreadsheet-friendly, newest first
    fda_510k_ipl_latest.json    # full records (everything the API returns)
    fda_510k_ipl_<date>.csv     # dated snapshot for history
    NEW_since_last_run.csv      # records not present in the prior snapshot
    run_log.txt                 # append-only log of every run
"""

import argparse
import csv
import datetime as dt
import json
import os
import sys
import time
import urllib.parse
import urllib.request

API = "https://api.fda.gov/device/510k.json"
HERE = os.path.dirname(os.path.abspath(__file__))
DATA = os.path.join(HERE, "data")

# Columns pulled into the flat CSV (the JSON keeps everything).
CSV_FIELDS = [
    "k_number", "decision_date", "date_received", "product_code",
    "applicant", "device_name", "decision_description", "clearance_type",
    "advisory_committee_description", "country_code", "state",
    "expedited_review_flag", "third_party_flag", "statement_or_summary",
    "pdf_url",
]


def load_config():
    cfg_path = os.path.join(HERE, "config.json")
    with open(cfg_path) as f:
        return json.load(f)


def fetch_page(search, limit, skip):
    """One openFDA request. Returns (results_list, total_count)."""
    qs = urllib.parse.urlencode({"search": search, "limit": limit, "skip": skip})
    url = f"{API}?{qs}"
    req = urllib.request.Request(url, headers={"User-Agent": "ipl-fda-pipeline/1.0"})
    with urllib.request.urlopen(req, timeout=60) as resp:
        payload = json.load(resp)
    return payload.get("results", []), payload["meta"]["results"]["total"]


def fetch_all(search, label):
    """Page through every record for a search string (openFDA skip cap = 25000)."""
    limit = 1000
    skip = 0
    out = []
    while True:
        try:
            results, total = fetch_page(search, limit, skip)
        except urllib.error.HTTPError as e:
            if e.code == 404:  # openFDA returns 404 for zero matches
                print(f"  [{label}] 0 records")
                return out
            raise
        out.extend(results)
        print(f"  [{label}] {len(out)}/{total}")
        skip += limit
        if skip >= total or skip >= 25000:
            break
        time.sleep(0.3)  # be polite to the public API
    return out


def pdf_url(k_number):
    """The FDA AccessData clearance page (human-readable, links to the PDF summary)."""
    return (
        "https://www.accessdata.fda.gov/scripts/cdrh/cfdocs/cfpmn/"
        f"pmn.cfm?ID={k_number}"
    )


def collect(codes, keywords, since):
    """Pull all records for the given product codes + keyword sweeps, deduped.

    Search strings use literal spaces (Lucene operators) and double-quotes for
    phrases; fetch_page() runs them through urlencode exactly ONCE. Do not
    pre-encode here — double-encoding silently corrupts the phrase match.
    """
    date_clause = f" AND decision_date:[{since} TO 2100-01-01]" if since else ""
    by_k = {}

    for code in codes:
        search = f"product_code:{code}{date_clause}"
        print(f"Product code {code}:")
        for r in fetch_all(search, code):
            by_k[r["k_number"]] = r

    for kw in keywords:
        # Quoted = exact phrase. Unquoted multi-word terms OR-explode in openFDA
        # (e.g. bare 'intense pulsed light' matches 4000+ via intense OR light).
        phrase = f'"{kw}"' if " " in kw else kw
        search = f"device_name:{phrase}{date_clause}"
        print(f"Keyword '{kw}':")
        for r in fetch_all(search, kw):
            by_k.setdefault(r["k_number"], r)  # don't overwrite a code-matched record

    records = list(by_k.values())
    records.sort(key=lambda r: r.get("decision_date", ""), reverse=True)
    return records


def flatten(r):
    row = {f: r.get(f, "") for f in CSV_FIELDS if f != "pdf_url"}
    row["pdf_url"] = pdf_url(r.get("k_number", ""))
    return row


def previous_k_numbers():
    """K-numbers from the last 'latest' snapshot, for diffing."""
    path = os.path.join(DATA, "fda_510k_ipl_latest.json")
    if not os.path.exists(path):
        return set()
    with open(path) as f:
        return {r["k_number"] for r in json.load(f)}


def write_outputs(records, today):
    os.makedirs(DATA, exist_ok=True)
    prev = previous_k_numbers()

    # Full JSON (everything)
    with open(os.path.join(DATA, "fda_510k_ipl_latest.json"), "w") as f:
        json.dump(records, f, indent=2)

    # Flat CSV (latest + dated snapshot)
    rows = [flatten(r) for r in records]
    for name in ("fda_510k_ipl_latest.csv", f"fda_510k_ipl_{today}.csv"):
        with open(os.path.join(DATA, name), "w", newline="") as f:
            w = csv.DictWriter(f, fieldnames=CSV_FIELDS)
            w.writeheader()
            w.writerows(rows)

    # Diff: what's new vs the prior run
    new = [r for r in records if r["k_number"] not in prev] if prev else []
    if prev:
        with open(os.path.join(DATA, "NEW_since_last_run.csv"), "w", newline="") as f:
            w = csv.DictWriter(f, fieldnames=CSV_FIELDS)
            w.writeheader()
            w.writerows(flatten(r) for r in new)
    return rows, new, prev


def log(today, n_total, n_new, prev_exists, codes, keywords):
    line = (
        f"{today}  total={n_total}  new={n_new if prev_exists else 'n/a (first run)'}  "
        f"codes={'+'.join(codes)}  keywords={keywords or '-'}\n"
    )
    with open(os.path.join(DATA, "run_log.txt"), "a") as f:
        f.write(line)


def main():
    cfg = load_config()
    ap = argparse.ArgumentParser()
    ap.add_argument("--codes", nargs="*", help="product codes, e.g. OHT OHS")
    ap.add_argument("--keywords", nargs="*", help="device_name phrases to sweep")
    ap.add_argument("--since", help="earliest decision_date YYYY-MM-DD")
    args = ap.parse_args()

    codes = args.codes or cfg["product_codes"]
    keywords = args.keywords if args.keywords is not None else cfg.get("keywords", [])
    since = args.since or cfg.get("since")
    today = dt.date.today().isoformat()

    print(f"=== FDA 510(k) IPL pull — {today} ===")
    print(f"Codes: {codes}  Keywords: {keywords}  Since: {since or 'all time'}\n")

    records = collect(codes, keywords, since)
    rows, new, prev = write_outputs(records, today)

    print(f"\nTotal unique clearances: {len(records)}")
    if prev:
        print(f"NEW since last run: {len(new)}")
        for r in new[:25]:
            print(f"  + {r['k_number']}  {r.get('decision_date')}  "
                  f"{r.get('applicant','')[:45]}")
    else:
        print("First run — no prior snapshot to diff against.")
        print("Most recent 10 clearances:")
        for r in records[:10]:
            print(f"  {r['k_number']}  {r.get('decision_date')}  "
                  f"{r.get('applicant','')[:45]}")

    log(today, len(records), len(new), bool(prev), codes, keywords)
    print(f"\nWrote: data/fda_510k_ipl_latest.csv  +  .json  +  dated snapshot")


if __name__ == "__main__":
    main()
