# HIFU / Microfocused Ultrasound Skin Tightening

Focused ultrasound is its own tightening lane, separate from fractional lasers, RF, and microneedling. This folder covers aesthetic HIFU/MFU systems for lifting, laxity, wrinkle, and body-contouring claims, with the main practical question framed the way the fractional-laser folder does it: what is the real gap between clinic devices and home devices?

## Bottom line

1. **Clinic HIFU/MFU is real, but the strongest anchor is a professional, prescription-device ecosystem.** Ulthera/Ultherapy was classified by FDA as a Class II focused ultrasound stimulator, product code `OHV`, regulation `21 CFR 878.4590`, originally as a prescription device for non-invasive eyebrow lift [[1]](source_docs/fda-k072505-ulthera-de-novo-classification.pdf). Newer Ulthera clearances include eyebrow lift, submental/neck lift, decollete lines/wrinkles, and appearance of skin laxity on abdomen, anterior arms, posterior arms, and knees [[2]](source_docs/fda-k260618-ulthera-prime-2026.pdf).
2. **Ulthera is not just a hot wand.** The IFU describes trained-user requirements, DeepSEE imaging to 8 mm, confirmation of coupling and depth, transducers at 1.5/3.0/4.5 mm, line spacing, and discrete thermal coagulation points [[3]](source_docs/ulthera-us-instructions-for-use-2021.pdf).
3. **Sofwave is also an FDA-cleared professional ultrasound lane, but it is not the same geometry as Ultherapy.** The FDA summaries describe high-frequency ultrasound with epidermal cooling, treatment depth around 1-2 mm, and clinical studies for facial lines/wrinkles plus eyebrow/submental/neck lifting indications [[4]](source_docs/fda-k191421-sofacia-sofwave.pdf)[[5]](source_docs/fda-k211483-sofwave-lifting-indications.pdf).
4. **Home HIFU/MFU is not to Ultherapy what Tria FRX is to Clear + Brilliant.** For fractional lasers, the home version can plausibly be read as lower-density fractional photothermolysis. For HIFU, the gap is not just density. It is focal geometry, layer verification, acoustic coupling, target mapping, line spacing, operator training, and complication management.
5. **No FDA-cleared OTC home facial HIFU/MFU device was found in the OHV openFDA snapshot captured on 2026-07-07.** The OHV dataset contains clinic/professional systems such as Ulthera, Sofwave, LipoSonix, UltraShape, SCIZER, and BeShape; it did not show a consumer OTC facial-lifting HIFU category in this pass [[6]](data/openfda-ohv-510k-2026-07-07.csv).
6. **Official home-device pages still show safety signals.** Medicube's High Focus Shot page recommends 600-1200 shots and warns against repeated/overlapping shots because skin depression or burns can occur; it also names prohibited areas including around the eyes, jawbone, Adam's apple, and thyroid area [[7]](https://medicube.us/pages/high-focus-shot).
7. **The home evidence base is thin.** A PubMed-indexed paper on a home-used HIFU device tested 4 MHz / 1.5 mm focal-depth treatment on mouse backs and measured dermal/collagen markers. That is useful mechanism signal, not human facial-lift evidence [[8]](https://pubmed.ncbi.nlm.nih.gov/36704876/).
8. **Risk is not imaginary.** Ulthera labeling and a 2024 MFU-V adverse-event review point to burns/scarring, nerve effects, fat/volume loss/lipoatrophy, numbness, dysesthesia, ptosis, and other complications as the serious boundary to respect [[3]](source_docs/ulthera-us-instructions-for-use-2021.pdf)[[9]](https://pubmed.ncbi.nlm.nih.gov/39625163/).

## Recommended reading order

| # | File | What it covers |
|---|------|----------------|
| 01 | [HIFU science brief](01_hifu_science_brief.md) | Focused ultrasound physics, target depths, TCPs, collagen remodeling, and why HIFU does not map cleanly to fractional-laser density math |
| 02 | [Clinic device evidence map](02_clinic_device_evidence_map.md) | Ulthera/Ultherapy, Sofwave, SCIZER/body contouring, and "Doublo" naming pitfalls, separated by FDA status and clinical evidence |
| 03 | [Home device landscape](03_home_device_landscape.md) | Medicube High Focus Shot, Ussera Deep Shot, generic mini/prosumer HIFU claims, home-device evidence, and regulatory caveats |
| 04 | [Home vs clinic results gap](04_home_vs_clinic_results_gap.md) | Direct comparison to fractional lasers, RF, and microneedling; why home HIFU is not simply a lower-power Ultherapy treatment |
| 05 | [Selection and safety protocol](05_selection_and_safety_protocol.md) | Goal-based choice guide, provider questions, home-use stop rules, and risk boundaries |
| 06 | [Clinical outcomes and realistic expectations](index.html#doc6) | Filing-level denominators, endpoints, responder proportions, patient-reported outcomes, pain, adverse events, and the translation limits behind Ulthera and Sofwave claims |

## Interactive tool

- [Depth planner](depth_planner.html) - visual explainer for ultrasound depth, clinic/home/device buckets, target layers, and risk boundaries. It is educational only, not treatment planning.

## Supporting material

- [Focused-ultrasound clinical outcomes CSV](data/focused_ultrasound_clinical_outcomes.csv) — structured filing extraction behind document 06.

- [Source-doc manifest](source_docs/README.md)
- FDA PDFs and IFU mirrors in [`source_docs/`](source_docs/)
- openFDA OHV, Ulthera, and Sofwave snapshots in [`data/`](data/)
- Official Medicube product-page captures in [`source_docs/`](source_docs/)
- PubMed captures for home-used HIFU mouse evidence and MFU-V adverse-event review in [`source_docs/`](source_docs/)
- The topic viewer's [FDA-reported events panel](index.html#maude) adds a searchable OHV MAUDE snapshot for focused-ultrasound reports, with an explicit professional-device/home-device scope warning.

## Relationship to neighboring folders

- [`03_fractional_laser_resurfacing/`](../03_fractional_laser_resurfacing/) is the best analogy to study for a home-vs-clinic framework, but **not** the right mechanism analogy for HIFU. Fractional lasers compare by wavelength, microbeam size, energy, density, coverage, and downtime.
- [`07_radio_frequency_skin_tightening/`](../07_radio_frequency_skin_tightening/) is the nearest tightening neighbor. RF home devices can be clinically real without being Thermage/RF-microneedling equivalents. HIFU adds a harder depth/focus/coupling problem.
- [`10_microneedling_collagen_induction/`](../10_microneedling_collagen_induction/) is the procedural-control analog: home tools may touch the broad mechanism, but professional outcomes depend on sterile, depth-controlled, indication-specific treatment stacks.

## Status / open items

- Captured a first-pass source corpus on 2026-07-07: FDA PDFs, Ulthera IFU, openFDA data, Medicube product pages, and PubMed pages.
- **Added 2026-08-12:** OHV MAUDE extraction and rendered report viewer. Still open: independent teardown/output data for home HIFU devices, official manuals/IFUs for Medicube High Focus Shot and Ussera if available, and direct clinic protocol/cost quotes by market.

## Sources

1. FDA K072505 / De Novo classification order for Ulthera. [Local PDF](source_docs/fda-k072505-ulthera-de-novo-classification.pdf) - Class II, product code OHV, prescription eyebrow-lift indication.
2. FDA K260618, Ulthera expanded knee indication. [Local PDF](source_docs/fda-k260618-ulthera-prime-2026.pdf) - Current captured Ulthera indications include eyebrow, submental/neck, decollete, abdomen, arms, and knees.
3. Ulthera System Instructions for Use, 2021. [Local PDF](source_docs/ulthera-us-instructions-for-use-2021.pdf) - Trained-user requirement, DeepSEE imaging, 1.5/3.0/4.5 mm transducers, TCPs, adverse events, and treatment precautions.
4. FDA K191421, Sofacia/Sofwave facial lines and wrinkles. [Local PDF](source_docs/fda-k191421-sofacia-sofwave.pdf) - 1-2 mm treatment depth, cooling, and 12-week facial wrinkle study.
5. FDA K211483, Sofwave lifting indications. [Local PDF](source_docs/fda-k211483-sofwave-lifting-indications.pdf) - Facial wrinkles, eyebrow lift, and submental/neck tissue indication with clinical performance data.
6. openFDA OHV 510(k) snapshot captured 2026-07-07. [CSV](data/openfda-ohv-510k-2026-07-07.csv) - 30 OHV records in the captured dataset, no OTC home facial HIFU category found in this pass.
7. Medicube High Focus Shot official page captured 2026-07-07. https://medicube.us/pages/high-focus-shot - Product-page FAQ and notes include 600-1200 shots, overlap warnings, and prohibited areas; local capture in `source_docs/medicube-high-focus-shot-page-2026-07-07.html`.
8. PubMed 36704876, "Efficacy of a home-used high-intensity focused ultrasound device on wrinkle reduction." https://pubmed.ncbi.nlm.nih.gov/36704876/ - Mouse-back study using a home-used HIFU probe at 4 MHz and 1.5 mm focal depth.
9. PubMed 39625163, "Microfocused Ultrasound With Visualization: A Systematic Review of Adverse Events and Risk of Subsequent Facelift Compromise." https://pubmed.ncbi.nlm.nih.gov/39625163/ - Review found common transient effects in literature and MAUDE reports including lipoatrophy, neurologic sequelae, and scarring.
