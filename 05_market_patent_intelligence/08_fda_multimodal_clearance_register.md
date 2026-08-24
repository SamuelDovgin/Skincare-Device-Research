# FDA multimodal clearance register

*Register compiled 2026-08-23 from five locally preserved FDA 510(k) decision files. This is regulatory intelligence, not a clinical recommendation. Verify the current FDA record and exact marketed model before relying on it.*

## Bottom line

The market topic already maps patents, brands, OEMs, and emerging technology. Its most actionable missing asset was a **model-level regulatory register** for the recent wave of microcurrent + LED + heat/vibration devices.

The five clearances contain nine materially different model/indication groups. Treating each 510(k) as one generic “multifunction beauty device” would hide the central finding:

> **The same submission can contain acne-capable, wrinkle-only, face-only, and face/body-stimulation models. Brand family and shell similarity are not enough; model-level indications are the unit of truth.**

Download the machine-readable [FDA multimodal clearance register](data/fda_multimodal_clearance_register.csv).

## 1. Register at a glance

| 510(k) / decision | Applicant / device | Model split that matters | LED indication(s) | New clinical study? |
|---|---|---|---|---|
| **K241718** · 2024-10-28 | Shenzhen Aozemei · AM-810/812 family | Four models share the filing | Facial wrinkles; mild-to-moderate inflammatory acne | No new clinical study described; conclusion rests on nonclinical testing/equivalence [[1]](https://www.accessdata.fda.gov/cdrh_docs/pdf24/K241718.pdf) |
| **K252142** · 2025-12-05 | Shenzhen Siken 3D · SKB family | SKB-1909 red+blue; SKB-1703 blue only; six models red only | Model-specific facial wrinkles and/or acne | No new clinical study described [[2]](https://www.accessdata.fda.gov/cdrh_docs/pdf25/K252142.pdf) |
| **K252187** · 2025-12-23 | Aura Medical · Aura Glide FC40 | One model | Red: periorbital wrinkles; blue: mild-to-moderate inflammatory acne; microcurrent: facial stimulation | FDA summary says clinical testing was not needed for substantial equivalence [[3]](https://www.accessdata.fda.gov/cdrh_docs/pdf25/K252187.pdf) |
| **K252642** · 2025-11-19 | Shenzhen Dachi · CEC101 / EEI101 | CEC face stimulation; EEI face/neck/body stimulation; both have red/blue, EEI also mixed acne mode | Facial wrinkles; inflammatory acne | No new clinical study described [[4]](https://www.accessdata.fda.gov/cdrh_docs/pdf25/K252642.pdf) |
| **K253833** · 2026-01-30 | Shenzhen Jianchao · INIA/F-series | Ten models red+blue; four models red only | Red: periorbital wrinkles; blue on ten-model subset: inflammatory acne | “Not applicable”; nonclinical/equivalence basis [[5]](https://www.accessdata.fda.gov/cdrh_docs/pdf25/K253833.pdf) |

## 2. What the filings actually establish

### Regulatory claim lanes

- **OHS** is the light-based OTC wrinkle-reduction lane.
- **OLP** is the OTC light-based acne lane.
- **NFO** is the OTC aesthetic transcutaneous electrical-stimulation lane.

Those codes and indications establish what FDA found substantially equivalent for the named models. They do not establish that every mode works better than sham, that combined modes are synergistic, or that a reseller’s renamed shell is the cleared device.

### Optical specifications vary enough to matter

| Filing | Red | Blue | Public irradiance in summary |
|---|---:|---:|---:|
| K241718 | 630 ± 10 nm | 415 ± 10 nm | red 2.5; blue 1.4 mW/cm²; amber 605 ± 10 nm at 15 mW/cm² |
| K252142 | 630 ± 10 nm | 460 ± 10 nm | red 2.3; blue 1.33 mW/cm² |
| K252187 | 633 ± 10 nm | 415 ± 10 nm | LED power listed; comparable irradiance not clearly reported in public summary |
| K252642 | 622 ± 10 nm | 415 ± 10 nm | CEC: red 0.77 / blue 0.75; EEI: red 1.43 / blue 1.12 / mixed 1.81 mW/cm² |
| K253833 | 630 ± 10 nm | 470 ± 10 nm | red 2.3; blue 4.48 mW/cm² |

This range makes wavelength-color marketing and “same factory” reasoning insufficient. The cleared optical output, treatment area, timer, microcurrent circuit, and model suffix all need matching.

## 3. How to use the CSV as a decision aid

### Verify a marketed product

1. Capture the exact model string from the device label—not only the listing title.
2. Filter `models` for an exact match.
3. Check whether the intended use is wrinkle, acne, facial stimulation, body stimulation, or a subset.
4. Match wavelength and mode behavior to the FDA summary and IFU.
5. Confirm legal manufacturer/applicant and current FDA database record.
6. Treat renamed/private-label equivalence as **unverified** until the label, 510(k) owner authorization, or device listing connects them.

### Audit a claim

| Marketplace claim | Register check |
|---|---|
| “FDA approved anti-aging and acne device” | Correct the term to **510(k)-cleared** where applicable; match exact model and separate red wrinkle from blue acne indication |
| “Microcurrent lifts face and body” | Check whether NFO stimulation includes body for that model; stimulation is not the same as a proven lifting endpoint |
| “Seven-color clinical LED” | Identify which colors have cleared indications; decorative or wellness modes may have none |
| “Same as K241718” | Compare model, applicant, product codes, wavelengths, irradiance, treatment area, timer, and predicate chain |

## 4. Market and patent implications

The register shows a repeatable clearance strategy: pair low-irradiance red/blue LEDs with aesthetic microcurrent and inherit parts of the claim structure through predicate devices, often without a new clinical trial. That creates three useful intelligence signals:

1. **Predicate convergence:** K241718 and K171821 recur, so changes in those reference platforms deserve monitoring.
2. **Model proliferation:** one hardware family can segment indications by LED population/software, which can support private-label SKU expansion.
3. **Evidence whitespace:** independent trials that isolate microcurrent, red LED, blue LED, heat, vibration, and combinations remain commercially differentiating because clearance files often rely on bench testing and equivalence.

Read this alongside the [blind-spots and opportunity map](index.html#doc6) and [frontier radar](frontier_radar.html).

## Data notes and discrepancies

- One CSV row represents one materially distinct model/indication group, not necessarily one physical SKU.
- Wavelength and irradiance fields transcribe public 510(k) summaries; `NR` means not clearly reported, not zero.
- K252642’s decision-letter cover lists OHS, while the summary comparison table describes OHS/OLP and the indications include acne. The CSV preserves that discrepancy rather than silently choosing one representation.
- “No new clinical study” means the public summary did not describe a new subject-device clinical trial; it does not mean no predicate evidence exists.
- Decision dates are the dates on the FDA letters, not product-launch dates.

## Evidence gaps

- The register covers the five preserved recent files, not every OHS/OLP/NFO submission.
- It does not yet resolve current device listings, private-label authorizations, UDI records, recalls, or adverse-event counts for every model.
- Public summaries may omit proprietary output/control details.
- 510(k) substantial equivalence is not an independent comparative efficacy result.
- Exact commercial product names, firmware, accessories, and geographic variants can drift after clearance.

### Sources

1. [FDA K241718 decision file](https://www.accessdata.fda.gov/cdrh_docs/pdf24/K241718.pdf) — Aozemei models, indications, modes, wavelength/irradiance, predicates, and nonclinical basis.
2. [FDA K252142 decision file](https://www.accessdata.fda.gov/cdrh_docs/pdf25/K252142.pdf) — Siken model-specific indication split and optical specifications.
3. [FDA K252187 decision file](https://www.accessdata.fda.gov/cdrh_docs/pdf25/K252187.pdf) — Aura Glide microcurrent/red/blue indications, treatment times, predicates, and no-new-clinical-testing statement.
4. [FDA K252642 decision file](https://www.accessdata.fda.gov/cdrh_docs/pdf25/K252642.pdf) — CEC/EEI stimulation areas, red/blue/mixed modes, optical output, predicates, and cover/summary code discrepancy.
5. [FDA K253833 decision file](https://www.accessdata.fda.gov/cdrh_docs/pdf25/K253833.pdf) — model groups, face/body stimulation, periorbital/acne indications, wavelength/irradiance, and nonclinical basis.
