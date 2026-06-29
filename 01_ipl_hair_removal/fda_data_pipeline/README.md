# fda_data_pipeline

Automated puller for FDA 510(k) IPL clearances, straight from the **openFDA**
device API. No manual K-number lookup, no API key, no dependencies.

## Quick start
```bash
cd fda_data_pipeline
python3 pull_fda_510k.py
```
Outputs land in `data/`. See **[STRATEGY.md](STRATEGY.md)** for the full plan,
product-code reference, and scheduling options.

## Full pipeline (run in order)
```bash
python3 pull_fda_510k.py           # 1. pull dataset from openFDA
python3 enrich_pulse_specs.py --all # 2. download+OCR every filing PDF -> pulse modes + text
python3 validate_completeness.py   # 3. prove coverage is extensive
python3 build_dataset.py           # 4. merge API + verified + auto specs -> dataset_full.json
python3 make_markdown.py           # 5. render ../08_fda_ipl_device_dataset.md (ranked by J/cm²)
```

## Files
| File | Purpose |
|------|---------|
| `STRATEGY.md` | The acquisition strategy + process diagram + how-to |
| `pull_fda_510k.py` | Pull (pull → dedupe → write → diff) |
| `enrich_pulse_specs.py` | Download + **OCR** each PDF → pulse modes + cached text |
| `validate_completeness.py` | Provable extensiveness audit (4 independent checks) |
| `build_dataset.py` | Merge API + hand-verified + auto specs; classify IPL vs diode |
| `make_markdown.py` | Render the ranked `08_fda_ipl_device_dataset.md` deliverable |
| `verified_specs.json` | **Hand-read subject-device specs** (the ✅ rows); add to here to verify more |
| `config.json` | What to pull: product codes, keyword sweeps, date range |
| `data/fda_510k_ipl_latest.csv/.json` | Raw API records (spreadsheet + full) |
| `data/pulse_specs_enriched.csv` | **Pulse modes + multi_pulse_flag + fluence per device** |
| `data/dataset_full.json` | Final merged dataset (feeds the markdown) |
| `data/pdf_cache/<K>.pdf`, `data/pdf_text/<K>.txt` | Cached filing PDFs + extracted/OCR'd text |
| `data/fda_510k_ipl_<date>.csv`, `NEW_since_last_run.csv`, `run_log.txt` | History/diff/log |

## Why a hand-verified layer (`verified_specs.json`)
The 510(k) comparison tables interleave the **subject** device with its
**predicate + reference** devices, and `pdftotext` linearizes them — so no regex
reliably isolates the subject's fluence (tested: max/first/mode each fail on
different filings; auto often grabs a reference's higher value). Fluence for the
decision-relevant devices is therefore **hand-read from each spec table** and
stored in `verified_specs.json` (the ✅ rows). Auto rows are kept but flagged `~`.

## The multi-pulse flag (what you asked about)
`pulse_specs_enriched.csv` sets `multi_pulse_flag = YES` whenever a filing
describes double/triple/multi-pulse firing — meaning the advertised single big
"joule" number is a **summed pulse train**, not true single-pulse output. It also
captures the exact sentence from the filing (`pulse_snippet`) and candidate
fluence/energy/wavelength/pulse-duration values. First run flagged **21 of 127**
OHT devices (2020+) as multi-pulse.

## The clean home-IPL slice
Filter `product_code == OHT` for the consumer hair-removal IPL category
(Fansizhe, Semlamp, Ulike, Braun, Nood, Philips, Mlay…) — the spine of this
research project. Everything else in the file comes from the broader
`"intense pulsed light"` keyword sweep.

## Current snapshot (2026-06-12)
- **241** unique IPL clearances across 3 codes: **OHT 162** (home IPL census),
  **GEX 46** (professional IPL/laser), **ONF 33** (other light-based).
- Newest: K261325 (Ulike, 2026-05-21), K260594 (Xiazhifeng), K260742 (Ulike),
  K260518 (Semlamp) — several **newer than the devices analyzed in doc 03**.
- Completeness audit: 162/162 OHT reconciled, 100% known-item recall.
