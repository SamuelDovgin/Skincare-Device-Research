# Strategy: Automated FDA 510(k) IPL Data Acquisition

**Goal:** Continuously and automatically capture every FDA 510(k) clearance for
IPL (Intense Pulsed Light) devices that companies file — no manual K-number
lookup — so the dataset is always current and ready for analysis.

---

## The key insight

Every 510(k) clearance in your research (K221569, K223928, K251173, K253881,
K260518, …) lives in **one queryable public database**: the **openFDA device
510(k) API** (`https://api.fda.gov/device/510k.json`).

- **No API key required**, no scraping, no PDFs to hunt down.
- Returns structured JSON: K-number, applicant, device name, decision date,
  product code, decision type, advisory committee, and more.
- Updated by the FDA on a regular cadence as new clearances post.
- Each record links straight to the FDA AccessData clearance page (and its PDF
  summary) — so you can drill into specs whenever a device looks relevant.

This turns "go look up FDA numbers" into a one-command pull. **You never have to
find K-numbers manually** — the pipeline discovers them for you.

---

## What "IPL data" means in FDA terms

The FDA classifies devices by **product code**. The codes that matter here:

| Code | What it is | Relevance |
|------|-----------|-----------|
| **OHT** | **OTC IPL hair removal** | ⭐ THE home/consumer IPL category. Fansizhe, Semlamp, Ulike, Braun, Nood, Philips, Mlay — all here. This is the spine of your project. (162 clearances all-time.) |
| OHS | OTC LED light, wrinkle reduction | Adjacent home light devices (not IPL, same buyers/market) |
| OLP | OTC acne light devices | Adjacent home light category |
| GEX | Professional/clinic IPL & laser | The pro landscape (2,800+ records — broad; opt in only if needed) |

Plus a **device-name keyword sweep** for `"intense pulsed light"` that catches
any IPL device filed under a *different* product code (professional/aesthetic
systems, combo devices, etc.). Deduplicated against the code-based pull.

**Default config = `OHT` + the keyword sweep.** That gives you:
- a **clean home-IPL core** (filter `product_code == OHT`, ~162 records), and
- a **wide IPL net** (272 records) for completeness.

---

## The process (4 steps, fully automated)

```
┌─ 1. PULL ────────────────────────────────────────────────┐
│  pull_fda_510k.py queries openFDA for each product code   │
│  in config.json + each keyword sweep. Pages through all   │
│  results (1000/request). No manual input.                 │
└───────────────────────────────────────────────────────────┘
                          │
┌─ 2. DEDUPE + SORT ───────▼────────────────────────────────┐
│  Merge by K-number (a device can match a code AND a       │
│  keyword). Sort newest-decision-date first.               │
└───────────────────────────────────────────────────────────┘
                          │
┌─ 3. WRITE ───────────────▼────────────────────────────────┐
│  data/fda_510k_ipl_latest.csv   (spreadsheet-ready)       │
│  data/fda_510k_ipl_latest.json  (full records)            │
│  data/fda_510k_ipl_<date>.csv   (dated history snapshot)  │
└───────────────────────────────────────────────────────────┘
                          │
┌─ 4. DIFF ────────────────▼────────────────────────────────┐
│  Compare against the previous snapshot →                  │
│  data/NEW_since_last_run.csv lists only clearances that    │
│  appeared since you last ran it. This is your "what did    │
│  companies file recently" feed.                           │
└───────────────────────────────────────────────────────────┘
```

Every run appends a line to `data/run_log.txt` (date, total, # new).

---

## How to run

```bash
cd fda_data_pipeline

# Default pull (OHT + "intense pulsed light" sweep, all-time):
python3 pull_fda_510k.py

# Just the clean home-IPL category:
python3 pull_fda_510k.py --codes OHT --keywords

# Widen to the whole home light-device market:
python3 pull_fda_510k.py --codes OHT OHS OLP

# Only recent clearances:
python3 pull_fda_510k.py --since 2024-01-01

# Add the professional IPL/laser landscape:
python3 pull_fda_510k.py --codes OHT GEX
```

No dependencies beyond Python 3 standard library. No API key.

---

## Keeping it current (optional automation)

The pipeline is built to be re-run on a schedule — each run refreshes
`latest.*` and regenerates `NEW_since_last_run.csv`. Options:

- **Manual:** run it whenever you want a refresh.
- **Cron / launchd:** schedule a weekly or monthly pull on this machine.
- **Claude `/schedule`:** a recurring cloud agent that runs the pull and
  surfaces new clearances. (Ask and I'll set it up.)

Because openFDA lags real-world FDA postings by a short interval, a **weekly or
biweekly** cadence is plenty — new home-IPL clearances post on the order of a
handful per month.

---

## What this dataset is good for (next: analysis)

The captured fields support analysis like:
- **Clearance velocity** — filings per year/quarter, who's accelerating.
- **Manufacturer landscape** — which OEMs (Fansizhe, Semlamp, Ulike, Mlay,
  Xiazhifeng…) dominate, and the private-label / cross-license web.
- **Recency** — newest clearances first; what's been filed in the last N months.
- **Predicate chains** — pair this list with the PDF summaries (links included)
  to trace substantial-equivalence lineage.
- **Geographic concentration** — Shenzhen OEM cluster vs Western brands.

> Note: the API gives **metadata** (who/when/what code). Device **specs**
> (wavelength, fluence, pulse) live in the PDF summaries — each record includes
> the `pdf_url` to that filing. The enrichment step below pulls those specs.

---

## Pulse-mode extraction — finding the REAL single-pulse power

**The problem you flagged:** a device advertised as "27.5 J" may be summing a
*pulse train* — three sub-pulses fired in one shot. The true single-pulse output
is a fraction of the headline number. To know which devices do this, you have to
read the filing, because **pulse mode is not in the API** — it's in the PDF.

`enrich_pulse_specs.py` automates that read:

```bash
python3 enrich_pulse_specs.py                 # OHT, 2020+ (where this matters most)
python3 enrich_pulse_specs.py --codes OHT GEX # include professional systems
python3 enrich_pulse_specs.py --all           # every clearance in the dataset
```

For each clearance it downloads the FDA PDF summary, extracts the text, and:

- **Detects pulse modes** — `single` / `double`-dual / `triple`-three / `multi`
  / `shr` — and sets **`multi_pulse_flag = YES`** when a pulse train is present.
  That flag is your "the advertised joules are summed, treat with suspicion" marker.
- **Captures the exact sentence** (`pulse_snippet`) so you read it yourself —
  e.g. K253881: *"all models have single pulse, dual pulse and three pulse
  functions"*; Ulike K261325: *"a lamp that can emit continuously double or
  triple pulses per shot."*
- **Pulls candidate spec values** — fluence (J/cm²), energy (J), wavelength
  (nm), pulse duration (ms) — into `pulse_specs_enriched.csv`.
- **Records `pdf_status`** so gaps are explicit: `ok` /
  `no_text_layer_needs_ocr` (scanned PDF) / `not_found` / `download_failed`.

**First enrichment run (OHT, 2020+, 127 devices): 21 flagged multi-pulse**,
including every Fansizhe/Semlamp/Ulike/Mlay high-output device. These are exactly
the clearances where the catalog joule number ≠ the single-pulse reality.

> Honest scope: this tells you *which* of the 162 to scrutinize and gives you the
> relevant sentence + candidate numbers. For a flagged device, confirming the
> precise per-pulse fluence still warrants a glance at the linked filing — but you
> open ~21, not 162. The per-filing text is cached in `data/pdf_text/<K>.txt`.

---

## How do we KNOW this is extensive? (provable, not a vibe)

`validate_completeness.py` proves coverage four independent ways and prints any
gap explicitly — a gap is a finding, never a silent omission:

```bash
python3 validate_completeness.py
```

1. **API-total reconciliation.** openFDA reports the total match count for every
   query; the pipeline pages until it has exactly that many. **162/162 OHT** =
   provably zero missed.
2. **Definitional completeness (the strongest guarantee).** The FDA assigns
   *every* OTC IPL hair-removal device the code **OHT**. "All OHT" is therefore
   the **census** of the home-IPL category — not a sample, the whole population.
3. **Known-item recall.** The 10 K-numbers already verified in this project
   (K212881, K221569, K223928, K251173, K253881, K260518, Ulike K241998, IONKA
   K230739, Semlamp K221246/K240969) **must all appear**. Current recall: **100%.**
4. **Cross-code leakage check.** It asks openFDA which product codes contain
   IPL-named devices. Result: IPL devices also live under **GEX** (professional
   IPL/laser) and **ONF** (other light-based) — and **all of them are captured**
   by the keyword sweep. Nothing IPL-named falls outside what we pull.

**Verdict from the last run:** *EXTENSIVE — full census of OHT + keyword sweep
across every other code that contains an IPL device.*
