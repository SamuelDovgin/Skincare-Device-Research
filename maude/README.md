# FDA MAUDE / Reported-Event Layer

*Compiled 2026-08-12. This is a post-market reporting layer, not a medical-safety calculator or medical advice.*

## Bottom line

MAUDE adds a useful real-world signal to the device categories in this archive: what users, health professionals, facilities, importers, and manufacturers reported to FDA about injuries, malfunctions, patient problems, device problems, and narratives. It does **not** tell us the true event rate, prove that a device caused an event, or support a safe/unsafe ranking by brand. FDA explicitly warns against using MDR data to calculate incidence, compare devices, or establish causality from a report alone. [[1]](https://www.fda.gov/medical-devices/mandatory-reporting-requirements-manufacturers-importers-and-user-facilities/about-manufacturer-and-user-facility-device-experience-maude-database)

## What was added

Each device topic with a focused MAUDE product-code lane now has an **FDA-reported events** panel. The panel is loaded from the local JSON snapshots in [`data/`](data/), so it works when the archive is opened from disk as well as from a web server.

| Topic | FDA code | What the panel represents |
|---|---:|---|
| IPL and diode hair removal | `OHT` | Home light-based hair-removal reports. The FDA code includes both IPL and diode/laser-style consumer hair-removal devices, so brand and narrative review still matter. |
| Red-light / LED devices | `OHS` | OTC light-based wrinkle-reduction reports, including LED masks and handheld light systems. |
| RF skin tightening | `PAY` | OTC radiofrequency wrinkle-reduction reports. The count is currently small, so this is mainly a device-level signal. |
| Microneedling | `QAI` | Powered microneedling reports, including patient outcomes and procedure/device problems. |
| HIFU / MFU | `OHV` | Focused-ultrasound aesthetic reports, including clinic systems and body-contouring devices in the same FDA code. |

The same `OHT` dataset is linked from both the IPL and diode-laser pages because FDA's product code is not a clean technology classifier. This avoids implying that every OHT report belongs to every device family.

## How the data was built

1. The refresh script queries the official openFDA Device Adverse Event endpoint by FDA product code.
2. It preserves the FDA MDR report key, dates, event type, reporter/source fields, device identity, model, manufacturer, 510(k)/PMA field, patient-problem terms, device-problem terms, outcomes, follow-up flags, and narrative text.
3. It deduplicates repeated terms within one report while retaining multiple reports and multiple device/patient entries.
4. It sorts reports newest first and creates a direct FDA detail link for every record.
5. The shared viewer reads the local snapshots, provides search/filter/sort, summarizes coded terms, and lets the reader expand the posted narrative.

The refresh date and FDA API metadata date are shown in each topic panel. The current snapshot was captured on 2026-08-12; the API metadata reported an FDA dataset update date of 2026-08-05.

## Interpretation rules

- A report is a report, not a confirmed causal finding.
- Counts are counts of indexed MDR records, not unique people, treatments, products sold, or event incidence.
- One report can contain multiple devices, patients, patient-problem terms, device-problem terms, and follow-up information.
- `Injury`, `Malfunction`, and other FDA event-type labels are shown exactly as coded; they are not converted into a severity score.
- Missing brand/model/manufacturer data is preserved as missing rather than guessed from marketplace names.
- Summary reports and manufacturer follow-ups are not silently converted into individual events.
- FDA's public data can contain incomplete, inaccurate, delayed, unverified, biased, redacted, or duplicated information. [[1]](https://www.fda.gov/medical-devices/mandatory-reporting-requirements-manufacturers-importers-and-user-facilities/about-manufacturer-and-user-facility-device-experience-maude-database)[[2]](https://www.fda.gov/medical-devices/medical-device-reporting-mdr-how-report-medical-device-problems/mdr-data-files)

## Why this enriches the category pages

The existing pages explain mechanism, clearance, clinical evidence, product claims, and home-versus-professional gaps. MAUDE adds a separate post-market question:

> What kinds of problems have actually been reported to FDA for devices in this regulatory lane, and what does the narrative say about the device, user, treatment, and follow-up?

That makes it possible to surface recurring safety themes such as burns, erythema, pigment change, scarring, infection, eye symptoms, nerve symptoms, overheating, labeling gaps, output problems, incompatibility, and technique-related issues—without presenting those themes as rates or proof that a specific device caused them.

## Data files

- [`maude_oht.json`](data/maude_oht.json) — OHT home light hair-removal reports.
- [`maude_ohs.json`](data/maude_ohs.json) — OHS OTC light/wrinkle-reduction reports.
- [`maude_pay.json`](data/maude_pay.json) — PAY OTC RF reports.
- [`maude_qai.json`](data/maude_qai.json) — QAI powered-microneedling reports.
- [`maude_ohv.json`](data/maude_ohv.json) — OHV focused-ultrasound reports.
- [`fetch_maude.py`](fetch_maude.py) — reproducible refresh script.

### Sources

1. FDA. [About the MAUDE database](https://www.fda.gov/medical-devices/mandatory-reporting-requirements-manufacturers-importers-and-user-facilities/about-manufacturer-and-user-facility-device-experience-maude-database) — database scope, limitations, fields, follow-ups, and causality warning.
2. FDA. [MDR Data Files](https://www.fda.gov/medical-devices/medical-device-reporting-mdr-how-report-medical-device-problems/mdr-data-files) — downloadable master, device, patient, narrative, and problem-code files; monthly updates; report-key joins.
3. openFDA. [Device Adverse Event API](https://open.fda.gov/apis/device/event/how-to-use-the-endpoint/) — endpoint syntax, searchable fields, and API limits.
4. FDA. [MDR Adverse Event Codes](https://www.fda.gov/medical-devices/mandatory-reporting-requirements-manufacturers-importers-and-user-facilities/mdr-adverse-event-codes) — device-problem, health-effect, investigation, and harmonized terminology structure.
