# 04 — Handheld Red Light Therapy (RLT) Devices

Research into handheld red light therapy devices for **hands, back pain, and carpal tunnel** — targeting ~5W LEDs with classic red (660nm) + near-infrared (850nm) wavelengths.

## Contents
- **[01_handheld_rlt_spec_comparison.md](01_handheld_rlt_spec_comparison.md)** — the main deliverable: full spec table for all 12 Alibaba listings, irradiance ranking, the "5W LED reality check," per-device cards, a head-to-head on the added contenders, and a ranked recommendation.
- **[02_raw_extracted_specs.md](02_raw_extracted_specs.md)** — raw per-listing spec dumps (text attributes + everything OCR'd from listing images), kept for traceability.
- **[03_independent_research_and_decision.md](03_independent_research_and_decision.md)** — independent literature/dosing context, fresh listing audit notes, supplier questions, and my final buy/skip decision.
- **[04_pl300_measured_specs_and_dose_model.md](04_pl300_measured_specs_and_dose_model.md)** — the user's PL300 half-body panel: complete claimed/measured/inferred spec sheet, meter readings, dose math, model limits, and verification gaps.
- **[05_whole_body_pbm_dosing_evidence.md](05_whole_body_pbm_dosing_evidence.md)** — human whole-body protocol matrix: 13.8–33.6 J/cm² study doses, calculated weekly exposure, outcomes, and PL300 translation.
- **[PL300 dose visualizer](pl300_dose_visualizer.html)** — interactive session-time calculator with the supplied seller curve, 60°/60° and 60°/30° lens-array scenarios, Lambertian/inverse-square comparisons, coverage geometry, conservative goal presets, and filterable PBM evidence map.
- **[`pl300_source_docs/`](pl300_source_docs/)** — preserved meter photos, seller-listing screenshots, transcriptions, hashes, manufacturer-family sources, and source manifest.
- **[`whole_body_source_docs/`](whole_body_source_docs/)** — preserved systematic-review PDF, randomized-study PDF, and Europe PMC full texts used for the whole-body protocol matrix.
- **`listing_images/`** — 92 archived listing photos (`L1_img1.jpg` … `L11_img10.jpg`). L12 is text-only from a supplied Alibaba page capture; no listing images are archived yet.

## The 12 listings (ranked)
| Rank | ID | Device | Price (1 pc) | Note |
|------|----|--------|--------------|------|
| 1 | L1 | AZURETHERAPY AL60 | $30 | 🥇 best documented; 190 mW/cm², full certs |
| 2 | L2 | Ideatherapy RTL12-C | ~$36–71 | 🥈 most honest irradiance data; aluminum |
| 3 | L7 | MINI60PRO desktop | $69–89 | 🥉 4 wavelengths, CE/FCC/RoHS, goggles |
| 4 | L10 | **Redfy RT60** ⭐NEW | $15.22 | best value; credible maker; "5W" match — but no irradiance |
| 5 | L11 | **SunPlus** ⭐NEW | $45.28 | broadest cert wall (ISO 13485) — but no irradiance, borrowed spec table |
| 6 | L6 | Mini 660/850 | $22.80 | likely same chassis as L1, thin docs |
| 7 | L5 | Traveler Mini Panel | $17.83 | 3W, magnetic back + kickstand, 301 g |
| 8 | L3 | 12pcs "8W" Panel | $16.90 | best controls, 10000mAh; "8W" unverified |
| 9 | L4 | 60W 3-wavelength | $8.30 | cheapest; 5W/1060nm claims but no spec images |
| 10 | L8 | Face Panel w/ goggles | $13.60+ | big brick, not truly handheld |
| 11 | L12 | **Ideatherapy RL-series** ⭐NEW | $44-109 | red/NIR LED lamp, not IPL; no irradiance, MOQ 3 |
| ❌ 12 | L9 | MINI60PRO standing | $62 | ❌ wholesale only (MOQ 51–101) |

## Key takeaway
"5W" is mostly a marketing label here (most units are ~2.5W/chip dual-emitter, or 3W SMD). **Irradiance (mW/cm²) at a stated distance** is the spec that actually matters for dose and penetration depth — rank by that and by honest documentation. After independently checking the archived listing images plus current indexed manufacturer/listing pages, my top pick remains **L1 AZURETHERAPY AL60**. **L2 Ideatherapy RTL12-C** is the only serious challenger, but current RTL12-C traces show variant/spec drift, so I would only buy it after seller confirmation and fresh meter readings. The added devices don't unseat L1: **L10 Redfy RT60** is the best *value* and truest "5W red+NIR" match (credible manufacturer, but no irradiance disclosed), **L11 SunPlus** has the strongest certification wall yet also hides irradiance and uses a spec table from a different model, and **L12 Ideatherapy RL-series** is a red/NIR LED lamp listing, not IPL, with no dose-relevant output specs.

_Data collected 2026-06-29 from alibaba.com product listings (text + image OCR)._

## PL300 panel update

Added 2026-07-12 as a panel-specific extension of this RLT lane and expanded 2026-07-13 with the owner's seller screenshots. The measured anchor is **161.145 mW/cm² mean at approximately 6 inches in combined red+NIR mode**. The seller claims 145/136/113/105 mW/cm² at 6/12/18/24 inches; the visualizer shows that curve separately from 60° lens-array and Lambertian models. The 60° angle is user-recalled and remains unverified. Seller claims, company-family documents, direct meter readings, inferred channel output, and model estimates are labeled separately.
