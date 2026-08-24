#!/usr/bin/env python3
"""Fetch and normalize FDA openFDA Device Adverse Event records for this archive.

The output is intentionally a compact, reader-facing evidence layer. It keeps
the original report narrative and identifiers, but does not turn MAUDE into a
rate or causal-risk calculator. Re-run this script when refreshing the data.
"""

from __future__ import annotations

import json
from collections import Counter
from datetime import date
from pathlib import Path
from urllib.parse import urlencode
from urllib.request import Request, urlopen


ROOT = Path(__file__).resolve().parents[1]
DATA_DIR = ROOT / "maude" / "data"
API = "https://api.fda.gov/device/event.json"
CAPTURED_AT = date.today().isoformat()

SOURCES = {
    "OHT": {
        "label": "Home light-based hair removal (IPL/diode)",
        "definition": "Over-the-counter device uses thermal energy to kill hair follicles for hair removal.",
        "regulation": "21 CFR 878.4810",
        "topics": ["01_ipl_hair_removal", "02_diode_laser_hair_removal"],
    },
    "OHS": {
        "label": "OTC light-based wrinkle reduction (LED/light therapy)",
        "definition": "Light-based over-the-counter wrinkle-reduction devices, including LED and related optical systems.",
        "regulation": "21 CFR 878.4810",
        "topics": ["04_red_light_therapy_handheld"],
    },
    "PAY": {
        "label": "OTC radiofrequency wrinkle reduction",
        "definition": "Over-the-counter radiofrequency device using localized heating for non-invasive aesthetic use.",
        "regulation": "21 CFR 878.4420",
        "topics": ["07_radio_frequency_skin_tightening"],
    },
    "QAI": {
        "label": "Powered microneedling",
        "definition": "Powered microneedle device using one or more needles to mechanically puncture and injure skin tissue for aesthetic use.",
        "regulation": "21 CFR 878.4430",
        "topics": ["10_microneedling_collagen_induction"],
    },
    "OHV": {
        "label": "Focused ultrasound for aesthetic tissue heating or disruption (HIFU/MFU)",
        "definition": "Focused ultrasound used to produce localized heating for tissue coagulation or mechanical cellular disruption for non-invasive aesthetic use.",
        "regulation": "21 CFR 878.4590",
        "topics": ["11_hifu_skin_tightening"],
    },
}


def fetch(code: str) -> dict:
    search = f"device.device_report_product_code:{code}"
    records = []
    first_payload = None
    # openFDA permits larger limits with an API key; the public endpoint is
    # reliable here at 100 records per request, so page explicitly.
    for skip in range(0, 100000, 100):
        query = urlencode({"search": search, "limit": 100, "skip": skip})
        request = Request(f"{API}?{query}", headers={"User-Agent": "Skincare-Device-Research/1.0", "Accept": "application/json"})
        try:
            with urlopen(request, timeout=90) as response:
                payload = json.load(response)
        except Exception:
            if first_payload is not None:
                break
            raise
        if first_payload is None:
            first_payload = payload
        page = payload.get("results", [])
        records.extend(page)
        total = payload.get("meta", {}).get("results", {}).get("total", len(records))
        if len(records) >= total or len(page) < 100:
            break
    if first_payload is None:
        raise RuntimeError(f"No MAUDE response for {code}")
    first_payload["results"] = records
    return first_payload


def as_list(value):
    if isinstance(value, list):
        return value
    return []


def unique(values):
    out = []
    seen = set()
    for value in values:
        if not isinstance(value, str):
            continue
        value = " ".join(value.split()).strip()
        if not value or value in seen:
            continue
        seen.add(value)
        out.append(value)
    return out


def normalize_record(raw: dict, code: str) -> dict:
    devices = as_list(raw.get("device"))
    patients = as_list(raw.get("patient"))
    texts = as_list(raw.get("mdr_text"))
    device_names = unique([d.get("brand_name", "") for d in devices])
    models = unique([d.get("model_number", "") for d in devices])
    manufacturers = unique([
        d.get("manufacturer_d_name", "") or d.get("manufacturer_name", "")
        for d in devices
    ])
    patient_problems = unique([
        problem
        for patient in patients
        for problem in as_list(patient.get("patient_problems"))
    ])
    outcomes = unique([
        outcome
        for patient in patients
        for outcome in as_list(patient.get("sequence_number_outcome"))
    ])
    narratives = unique([text.get("text", "") for text in texts])
    device_problems = unique(as_list(raw.get("product_problems")))
    report_key = str(raw.get("mdr_report_key", "")).strip()
    detail_url = (
        "https://www.accessdata.fda.gov/scripts/cdrh/cfdocs/cfmaude/"
        f"detail.cfm?mdrfoi__id={report_key}&pc={code}"
    )
    return {
        "mdr_report_key": report_key,
        "date_received": raw.get("date_received", ""),
        "date_of_event": raw.get("date_of_event", ""),
        "event_type": raw.get("event_type", ""),
        "report_source": raw.get("report_source_code", ""),
        "source_type": unique(as_list(raw.get("source_type"))),
        "reporter_occupation": raw.get("reporter_occupation_code", ""),
        "health_professional": raw.get("health_professional", ""),
        "brand_names": device_names,
        "model_numbers": models,
        "manufacturers": manufacturers,
        "device_names": unique([d.get("generic_name", "") for d in devices]),
        "product_code": code,
        "pma_510k": raw.get("pma_pmn_number", ""),
        "patient_problems": patient_problems,
        "device_problems": device_problems,
        "outcomes": outcomes,
        "remedial_action": unique(as_list(raw.get("remedial_action"))),
        "device_available": unique([d.get("device_availability", "") for d in devices]),
        "device_evaluated": unique([d.get("device_evaluated_by_manufacturer", "") for d in devices]),
        "report_type": unique(as_list(raw.get("type_of_report"))),
        "summary_report": raw.get("summary_report_flag", ""),
        "number_devices": raw.get("number_devices_in_event", ""),
        "number_patients": raw.get("number_patients_in_event", ""),
        "narratives": narratives,
        "detail_url": detail_url,
    }


def main() -> None:
    DATA_DIR.mkdir(parents=True, exist_ok=True)
    for code, config in SOURCES.items():
        payload = fetch(code)
        records = [normalize_record(raw, code) for raw in payload.get("results", [])]
        records.sort(key=lambda row: (row["date_received"], row["mdr_report_key"]), reverse=True)
        event_counts = Counter(row["event_type"] or "Not provided" for row in records)
        patient_counts = Counter(
            problem for row in records for problem in row["patient_problems"]
        )
        device_counts = Counter(
            problem for row in records for problem in row["device_problems"]
        )
        output = {
            "metadata": {
                "product_code": code,
                "label": config["label"],
                "definition": config["definition"],
                "regulation": config["regulation"],
                "topics": config["topics"],
                "captured_at": CAPTURED_AT,
                "api_last_updated": payload.get("meta", {}).get("last_updated", ""),
                "api_total": payload.get("meta", {}).get("results", {}).get("total", len(records)),
                "record_count": len(records),
                "source_url": f"{API}?{urlencode({'search': f'device.device_report_product_code:{code}'})}",
                "classification_url": f"https://www.accessdata.fda.gov/scripts/cdrh/cfdocs/cfPCD/classification.cfm?id={code}",
                "event_counts": dict(event_counts),
                "patient_problem_counts": dict(patient_counts),
                "device_problem_counts": dict(device_counts),
            },
            "records": records,
        }
        path = DATA_DIR / f"maude_{code.lower()}.json"
        path.write_text(json.dumps(output, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        print(f"WROTE {path} ({len(records)} records; API total {output['metadata']['api_total']})")


if __name__ == "__main__":
    main()
