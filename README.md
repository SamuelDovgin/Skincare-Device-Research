# Skincare Device Research

Research into at-home, light- and energy-based skincare devices for **facial redness/erythema, hyperpigmentation, post-inflammatory hyperpigmentation (PIH), and evening skin tone**, plus **hair removal**, **skin-quality (collagen) rejuvenation**, **tightening/laxity**, and topical support as parallel goals. Budget-conscious; covers branded, retail, Chinese OEM/Alibaba sourcing, patent/regulatory context, and practical product buying.

The repo is organized by **product type** into eleven projects:

| Folder | Product class | Goal |
|--------|---------------|------|
| [`01_ipl_hair_removal/`](01_ipl_hair_removal/) | Broadband IPL (intense pulsed light) | Hair removal; pigment/redness strategy |
| [`02_diode_laser_hair_removal/`](02_diode_laser_hair_removal/) | Diode lasers (Tria 810nm & alternatives) | Targeted hair removal |
| [`03_fractional_laser_resurfacing/`](03_fractional_laser_resurfacing/) | Non-ablative fractional lasers | Skin quality — pigment + collagen |
| [`04_red_light_therapy_handheld/`](04_red_light_therapy_handheld/) | Handheld red/NIR LED therapy | Local pain/recovery adjuncts |
| [`05_market_patent_intelligence/`](05_market_patent_intelligence/) | Market + patent intelligence | Cross-category ownership, IP, and product teardown |
| [`06_non_fractional_lasers/`](06_non_fractional_lasers/) | Non-fractional lasers | 1064nm / 1450nm / LLLT laser claims that are not fractional resurfacing |
| [`07_radio_frequency_skin_tightening/`](07_radio_frequency_skin_tightening/) | Radiofrequency (RF) skin tightening | Collagen/laxity devices, home RF, RF microneedling risk |
| [`08_vitamin_c_serums/`](08_vitamin_c_serums/) | Vitamin C serums | SkinCeuticals C E Ferulic, patents, dupes, DIY L-ascorbic acid, derivatives |
| [`09_zinc_oxide_barrier_cream/`](09_zinc_oxide_barrier_cream/) | Zinc oxide barrier cream | Science-first barrier lane: mechanism, dermatitis/wound evidence, safety protocol, and product notes |
| [`10_microneedling_collagen_induction/`](10_microneedling_collagen_induction/) | Microneedling / collagen induction | Acne scars, wrinkles/scars, FDA QAI devices, home-vs-professional boundary, RF microneedling risk |
| [`11_hifu_skin_tightening/`](11_hifu_skin_tightening/) | HIFU / microfocused ultrasound | Clinic HIFU/MFU, home-device claims, focal-depth physics, and home-vs-clinic boundary |

## TL;DR

1. **For the PRIMARY goal (pigment/PIH/redness), a home IPL device is the wrong primary tool.** Broadband IPL can *worsen* pigmentation in pigment-prone skin (~2.96% IPL-induced hyperpigmentation in Fitzpatrick III–IV). Lead instead with **iron-oxide tinted sunscreen + topicals (azelaic acid, tranexamic acid, niacinamide) + non-thermal LED (red 630–660nm / amber ~590nm)**. See **[01 / doc 07](01_ipl_hair_removal/07_alternatives_and_strategy.md)**. For the narrow-band alternative, **DPL is filtered IPL, not a laser**; the new [JOVS Blacken/OEM comparison](01_ipl_hair_removal/17_jovs_blacken_dpl_and_oem_comparison.md) separates three JOVS models from their lookalike Alibaba shells.
2. **No home IPL device — branded or Chinese OEM — is FDA-cleared for anything but hair removal** (all are product code OHT). Verified from the actual filings. See **[01 / doc 03](01_ipl_hair_removal/03_fda_510k_analysis.md)**.
3. **If buying a device for the hair goal:** best OEM target = **Fansizhe T023A** (510nm filter, sapphire cooling; FDA K223928 baseline 5.5 J/cm², and a **seller video on 2026-06-14 measured a real 18.23J / 6.08 J/cm² single flash** — the highest verified single-pulse fluence in the dataset). Budget single-pulse fallback = **Fansizhe T001M/T001A**. Lowest-risk branded option = **Nood Flasher 2.0** ($169, FDA-cleared, 510nm, warranty). See **[01 / doc 06](01_ipl_hair_removal/06_final_recommendation.md)**.
4. **For skin quality (collagen/pigment), the device class is non-ablative fractional resurfacing**, not IPL or hair lasers — a different thread entirely. See **[`03_fractional_laser_resurfacing/`](03_fractional_laser_resurfacing/)**.
5. **For localized pain/recovery, handheld red-light devices are a separate, adjunctive project.** Evidence is mixed for carpal tunnel/back/hand pain, so output documentation and conservative dosing matter more than "5W" marketing. See **[`04_red_light_therapy_handheld/`](04_red_light_therapy_handheld/)**.
6. **DermRays Revive belongs in the non-fractional laser lane, not the Clear + Brilliant lane.** FDA K231910 confirms a 1064nm, 400 ms, 5-10 J/cm², 15mm, prescription-use laser for hair removal + wrinkles. Its FDA geometry implies **8.83-17.66 J per pulse** and **22.1-44.2 W average pulse power**, but that still means non-fractional spot heating, not MTZ resurfacing. NIRA has stronger public wrinkle-outcome evidence than DermRays, while DermRays has the more interesting 1064nm power story. See **[`06_non_fractional_lasers/`](06_non_fractional_lasers/)**, the [`power_comparison_visualizer.html`](06_non_fractional_lasers/power_comparison_visualizer.html), and the [`dose_geometry_simulator.html`](06_non_fractional_lasers/dose_geometry_simulator.html).
7. **Radiofrequency is now its own collagen/tightening project.** Home RF has a real FDA pathway for mild-to-moderate wrinkle reduction, while RF microneedling is a higher-risk medical procedure flagged by FDA in 2025. Home RF can be clinically real without being Thermage/RF-microneedling equivalent. See **[`07_radio_frequency_skin_tightening/`](07_radio_frequency_skin_tightening/)**.
8. **Vitamin C serums are now separated from device research as the topical antioxidant lane.** SkinCeuticals C E Ferulic is the best-studied benchmark; its key US7179841B2 patent expired on 2025-03-24, making Trader Joe's-style CEF dupes more plausible but not automatically equivalent. Use vitamin C in the morning and Differin at night. See **[`08_vitamin_c_serums/`](08_vitamin_c_serums/)**.
9. **Zinc oxide diaper rash cream is now a science-first barrier lane, not just a product tip.** The strongest evidence is for OTC skin-protectant use, irritant/moisture dermatitis, TEWL/barrier support, and wound/periwound adjuncts; adult facial overnight use remains an extrapolation. If experimenting, start around **10-15% zinc oxide** and reserve 40% pastes for spot rescue. See **[`09_zinc_oxide_barrier_cream/`](09_zinc_oxide_barrier_cream/)**.
10. **Microneedling now has its own collagen-induction lane.** The strongest evidence is professional treatment of atrophic acne scars; FDA has not authorized OTC medical microneedling devices; and RF microneedling is a professional procedure, not a home-device shortcut. See **[`10_microneedling_collagen_induction/`](10_microneedling_collagen_induction/)**.
11. **HIFU / microfocused ultrasound is now separated as a tightening lane.** Clinic Ulthera/Sofwave evidence is real but procedure-specific; home HIFU/MFU is not a clean "lower-density Ultherapy" analog because focal depth, coupling, line spacing, visualization, and anatomy control matter more than shot count. See **[`11_hifu_skin_tightening/`](11_hifu_skin_tightening/)**.

---

## 01 — IPL hair removal · [`01_ipl_hair_removal/`](01_ipl_hair_removal/)

Broadband intense pulsed light devices (Fansizhe / Semlamp OEM, Nood / Ulike branded), the underlying photothermolysis science, FDA clearance landscape, and the pigment-strategy reframe.

| # | File | What it covers |
|---|------|----------------|
| 01 | [Science brief](01_ipl_hair_removal/01_science_brief.md) | Selective photothermolysis, TRT, wavelength/chromophore physics, clinical fluence, PIH risk, home-device limits |
| 02 | [Ideal device specs](01_ipl_hair_removal/02_ideal_device_specs.md) | Target spec sheet, scoring matrix, Alibaba red flags |
| 03 | [FDA 510(k) analysis](01_ipl_hair_removal/03_fda_510k_analysis.md) | Verified specs, predicate/reference devices (Ulike, IONKA), why OHT ≠ rejuvenation |
| 04 | [Fansizhe catalog](01_ipl_hair_removal/04_fansizhe_catalog_transcription.md) | Every Fansizhe model, specs, fluence, FDA status |
| 05 | [Semlamp catalog](01_ipl_hair_removal/05_semlamp_catalog_transcription.md) | Every Semlamp model, "age spot" filter heads, certs |
| 06 | [Final device recommendation](01_ipl_hair_removal/06_final_recommendation.md) | Ranked IPL picks for the hair goal + usage/safety protocol |
| 07 | [Alternatives & strategy](01_ipl_hair_removal/07_alternatives_and_strategy.md) | **The reframe**: DPL vs IPL, LED, topicals-first, branded vs OEM, evidence-based plan |
| 08 | [FDA IPL device dataset](01_ipl_hair_removal/08_fda_ipl_device_dataset.md) | **Every FDA-cleared home IPL device ranked by J/cm²** — auto-generated + hand-verified |
| 11 | [510nm IPL vs Tria head-to-head](01_ipl_hair_removal/11_510nm_ipl_vs_tria_research_headtohead.md) | 510nm IPL vs the Tria diode option for the hair goal |
| 12 | [Treatment cadence guide](01_ipl_hair_removal/12_treatment_cadence_guide.md) | Per-body-area treatment cadence, maintenance timing, and how to ramp use |
| 13 | [Skin rejuvenation guide](01_ipl_hair_removal/13_skin_rejuvenation_guide.md) | Reality check and conservative cadence for off-label body-only IPL rejuvenation attempts |
| 14 | [IPL research evidence map](01_ipl_hair_removal/14_ipl_research_evidence_map.md) | Best-cited IPL papers grouped by what they prove: mechanism, hair, cadence, rejuvenation, and safety |
| 15 | [Multi-flash thermal accumulation](01_ipl_hair_removal/15_multi_flash_thermal_accumulation.md) | Fixed-spot pulse stacking, clinical SHR distinction, and the missing pulse-timing data |
| 16 | [SHR / Ulike thermal simulation](01_ipl_hair_removal/16_shr_ulike_thermal_simulation.md) | Revised time–temperature/Arrhenius model: why 65 °C is not an instant switch and 45–50 °C is not a proven kill line |
| 17 | [JOVS Blacken DPL and OEM comparison](01_ipl_hair_removal/17_jovs_blacken_dpl_and_oem_comparison.md) | **Three JOVS models, DPL vs IPL, the two supplied Alibaba links, manufacturer trail, and best comparable AY101** |

**Supporting material:** [`cadence_planner.html`](01_ipl_hair_removal/cadence_planner.html) interactive treatment schedule planner · [`shr_thermal_simulator.html`](01_ipl_hair_removal/shr_thermal_simulator.html) revised Arrhenius time–temperature and pulse-stacking simulator · [thermal-model source manifest](01_ipl_hair_removal/thermal_model_source_docs/README.md) with primary/full-text kinetics, measured hair-temperature, and histology sources · [`jovs-dpl-comparator.html`](01_ipl_hair_removal/jovs-dpl-comparator.html) interactive JOVS/Alibaba wavelength, fluence, and sourcing comparison · [JOVS DPL source manifest](01_ipl_hair_removal/jovs_dpl_source_docs/README.md) with mirrored product pages, FDA K231800, peer-reviewed full text, and Alibaba listing images · [Natalie/Fansizhe conversation notes](01_ipl_hair_removal/fansizhe_natalie_conversation_notes.md) · Fansizhe & Semlamp FDA 510(k) PDFs · product catalogs · `Weiss_IPL.pdf` (clinical IPL photoaging parameters) · [`fda_data_pipeline/`](01_ipl_hair_removal/fda_data_pipeline/) — pulls all FDA 510(k) IPL clearances from openFDA, OCRs every filing, extracts pulse modes/fluence, and generates doc 08 (re-runnable; see its [STRATEGY.md](01_ipl_hair_removal/fda_data_pipeline/STRATEGY.md)).

## 02 — Diode laser hair removal · [`02_diode_laser_hair_removal/`](02_diode_laser_hair_removal/)

True diode lasers (Tria 810nm and alternatives) and the used-market analysis around a $50 Tria Precision offer.

| # | File | What it covers |
|---|------|----------------|
| 09 | [Tria Precision marketplace assessment](02_diode_laser_hair_removal/09_tria_precision_marketplace_assessment.md) | $50 used Tria Precision vs 4X and the IPL shortlist; worth it only as a small-area dark-hair tool |
| 10 | [Used Tria value & wear pricing](02_diode_laser_hair_removal/10_used_tria_value_and_wear_pricing.md) | Used-market comps, cosmetic/battery wear model, $40/$45/$50 negotiation thresholds |
| 11 | [810nm diode alternatives vs IPL](02_diode_laser_hair_removal/11_810nm_diode_laser_alternatives_vs_ipl.md) | DermRays/CurrentBody, Epilaser, SilkPro, ViQure/prosumer, and when IPL still wins |
| 12 | [Marketplace seller activity analysis](02_diode_laser_hair_removal/12_marketplace_seller_activity_analysis.md) | Seller/listing behavior for the $50 offer: listing age, batch-posting, sold-history caveats |

**Supporting material:** Tria 4X & Tria Precision IFUs (810nm, 7–20 J/cm² spec confirmation) · [marketplace_seller_activity_sanitized.json](02_diode_laser_hair_removal/marketplace_seller_activity_sanitized.json) (sanitized data snapshot for doc 12).

## 03 — Fractional laser resurfacing · [`03_fractional_laser_resurfacing/`](03_fractional_laser_resurfacing/)

A **separate device class for the *skin-quality* goal (pigment + collagen), not hair.** Non-ablative fractional lasers (Clear + Brilliant, Tria FRX, NIRA, YDUNVIE Iris/Dora) and the user's owned Tria SmoothBeauty: science, in-office-vs-home expectations, full device landscape, the Jiangsu Unimed/YDUNVIE supplier map, RFQ templates, and a future research plan. The [`beam_coverage_simulator.html`](03_fractional_laser_resurfacing/beam_coverage_simulator.html) interactive tool visualizes beam depth, beam width, MTZ coverage, and total energy by device. See its [README](03_fractional_laser_resurfacing/README.md).

## 04 — Handheld red light therapy · [`04_red_light_therapy_handheld/`](04_red_light_therapy_handheld/)

Handheld red/NIR LED devices for **hands, wrist/carpal-tunnel symptoms, and localized back pain**, with Alibaba listing-image OCR plus a text-only added Ideatherapy RL-series listing, device-output ranking, and a final buy/skip decision.

| # | File | What it covers |
|---|------|----------------|
| 01 | [Handheld RLT spec comparison](04_red_light_therapy_handheld/01_handheld_rlt_spec_comparison.md) | Full side-by-side of 12 Alibaba listings: wavelengths, irradiance, cert claims, controls, and ranking |
| 02 | [Raw extracted specs](04_red_light_therapy_handheld/02_raw_extracted_specs.md) | Traceability dump of listing text and OCR'd image specs |
| 03 | [Independent research & decision](04_red_light_therapy_handheld/03_independent_research_and_decision.md) | Literature context, dose math, current listing audit, supplier questions, and final recommendation |

**Supporting material:** 92 archived listing images in [`listing_images/`](04_red_light_therapy_handheld/listing_images/) for L1-L11, a text-only supplied Alibaba capture for L12, plus the project [README](04_red_light_therapy_handheld/README.md).

## 05 — Market & patent intelligence · [`05_market_patent_intelligence/`](05_market_patent_intelligence/)

Cross-category research on who owns the technology, what the buzzy devices really are, where the market is heading, and what has moved off-patent.

| # | File | What it covers |
|---|------|----------------|
| 01 | [Overview](05_market_patent_intelligence/01_overview.md) | Executive summary of product, patent, and market findings |
| 02 | [Patent landscape](05_market_patent_intelligence/02_patent_landscape.md) | Foundational IPL/laser/RF/LED patents, expiry map, and active filing themes |
| 03 | [Market map teardown](05_market_patent_intelligence/03_market_map_teardown.md) | What popular devices actually are under the hood |
| 04 | [Market size trends](05_market_patent_intelligence/04_market_size_trends.md) | Category sizing, growth rates, and consumer-device trend lines |
| 05 | [Frontier & emerging tech](05_market_patent_intelligence/05_frontier_emerging_tech.md) | AI dosing, sensors, home RF, 1064nm, and what is real vs hype |
| 06 | [Patent search playbook](05_market_patent_intelligence/06_patent_search_playbook.md) | How to keep researching patents without inventing numbers |

## 06 — Non-fractional lasers · [`06_non_fractional_lasers/`](06_non_fractional_lasers/)

Real lasers that are **not** fractional resurfacing devices: DermRays Revive, 1064nm home/Rx laser claims, 810nm wide-window hair lasers, NIRA-like non-fractional warmers, and LYMA/LLLT boundary cases.

| # | File | What it covers |
|---|------|----------------|
| 01 | [Non-fractional laser science](06_non_fractional_lasers/01_non_fractional_laser_science.md) | Fractional vs non-fractional geometry, 1064nm physics, and why DermRays is not a Clear + Brilliant analog |
| 02 | [Device landscape](06_non_fractional_lasers/02_device_landscape.md) | DermRays Revive, 810nm wide-window devices, NIRA, LYMA, and pro 1064nm context |
| 03 | [DermRays Revive deep dive](06_non_fractional_lasers/03_dermrays_revive_deep_dive.md) | FDA K231910 specs, claims vs clearance, patent signal, and verification checklist |
| 04 | [NIRA / DermRays professional-results gap](06_non_fractional_lasers/04_nira_dermrays_professional_results_gap.md) | Can NIRA or DermRays reach clinic-grade results? Evidence, dose, and why Tria's C+B analogy does not transfer |
| 05 | [DermRays power, patent, and device comparison](06_non_fractional_lasers/05_dermrays_power_patent_comparison.md) | Fluence-to-Joule math, NIRA/Tria/pro-1064 comparison, current claims, patent map, and feature-verification checklist |

**Supporting material:** [`power_comparison_visualizer.html`](06_non_fractional_lasers/power_comparison_visualizer.html) quick DermRays/NIRA/Tria/pro-context visualizer · [`dose_geometry_simulator.html`](06_non_fractional_lasers/dose_geometry_simulator.html) interactive non-fractional laser dose-geometry simulator · local FDA/product snapshots in [`source_docs/`](06_non_fractional_lasers/source_docs/) · Google Patents captures in [`patents_source_docs/`](06_non_fractional_lasers/patents_source_docs/) · [`data/dermrays_power_comparison.json`](06_non_fractional_lasers/data/dermrays_power_comparison.json).

## 07 — Radiofrequency skin tightening · [`07_radio_frequency_skin_tightening/`](07_radio_frequency_skin_tightening/)

RF devices for collagen remodeling, mild wrinkles, laxity, and skin tightening — separated from lasers/IPL/LED because RF heats by electrical impedance, not optical absorption.

| # | File | What it covers |
|---|------|----------------|
| 01 | [RF science brief](07_radio_frequency_skin_tightening/01_rf_science_brief.md) | Mechanism, tissue heating, device geometries, home vs pro RF, and evidence expectations |
| 02 | [Initial device landscape](07_radio_frequency_skin_tightening/02_initial_device_landscape.md) | NEWA, TriPollar, CurrentBody, Silk'n, Medicube, Thermage, and RF microneedling buckets |
| 03 | [Patent & regulatory notes](07_radio_frequency_skin_tightening/03_patent_regulatory_notes.md) | Thermage patent anchor, FDA PAY category, CurrentBody K232424, and FDA RF microneedling warning |
| 04 | [Home RF vs professional results gap](07_radio_frequency_skin_tightening/04_home_rf_vs_professional_results_gap.md) | Can at-home RF reach clinical-grade results? NEWA/CurrentBody vs Thermage/RF microneedling |

## 08 — Vitamin C serums · [`08_vitamin_c_serums/`](08_vitamin_c_serums/)

Topical antioxidant and pigment-support lane: SkinCeuticals C E Ferulic, the Duke Parameters, patent expiry, Trader Joe's and budget dupes, DIY L-ascorbic acid recipes, and newer derivative systems from L'Oreal/Kiehl's and others.

| # | File | What it covers |
|---|------|----------------|
| 01 | [C E Ferulic science & patents](08_vitamin_c_serums/01_ce_ferulic_science_and_patents.md) | Why the formula is well studied, Duke Parameters, US5140043 and US7179841, patent expiry, and what the claims cover |
| 02 | [Product comparison](08_vitamin_c_serums/02_product_comparison.md) | SkinCeuticals vs Trader Joe's vs DIY vs budget dupes vs Kiehl's/L'Oreal derivative strategies |
| 03 | [DIY vitamin C protocol](08_vitamin_c_serums/03_diy_vitamin_c_protocol.md) | Exact 10/15/20% recipes, pH logic, no-strip risk management, storage, oxidation, and how to use with Differin |
| 04 | [Derivatives & next-gen formulas](08_vitamin_c_serums/04_derivatives_and_next_gen_formulas.md) | Vitamin Cg, THD/ATIP, ethyl ascorbic acid, SAP/MAP, Melasyl combinations, and current SkinCeuticals direction |

## 09 — Zinc oxide barrier cream · [`09_zinc_oxide_barrier_cream/`](09_zinc_oxide_barrier_cream/)

Topical barrier-support lane for the online "diaper rash cream as a face night treatment" trend. The section now starts with mechanism and evidence, then moves to safety and product selection: zinc oxide as an OTC skin protectant, petrolatum/dimethicone vehicle effects, TEWL/barrier data, diaper-dermatitis studies, wound-healing literature, Differin/device routine fit, and label-checked Amazon notes.

| # | File | What it covers |
|---|------|----------------|
| 01 | [Zinc oxide and skin-barrier science](09_zinc_oxide_barrier_cream/01_zinc_oxide_skin_barrier_science.md) | Skin-protectant mechanism, zinc biology, petrolatum/dimethicone vehicle effects, TEWL, particle penetration, and what diaper cream is not |
| 02 | [Evidence map: dermatitis, barrier, wound healing](09_zinc_oxide_barrier_cream/02_evidence_map_dermatitis_wound_healing.md) | FDA monograph, DailyMed labels, diaper dermatitis studies, infant barrier-function RCT, pilonidal wound RCT, human wound-model trial, and limitations |
| 03 | [Safety, routine fit, and protocol](09_zinc_oxide_barrier_cream/03_safety_protocol_and_routine_fit.md) | Patch testing, Differin/adapalene scheduling, device-aftercare cautions, acne/rosacea/perioral dermatitis caveats, and stop rules |
| 04 | [Product selection notes](09_zinc_oxide_barrier_cream/04_product_selection_notes.md) | Current Amazon/DailyMed label-based product picks, 10-15% vs 40% logic, and what to avoid for facial use |
| 05 | [Sudocrem product comparison](09_zinc_oxide_barrier_cream/05_sudocrem_product_comparison.md) | Sudocrem 15.29% zinc oxide comparison against Triple Paste, Pipette, and Desitin, with label-based caveats |
| 06 | [Reddit anecdote scan](09_zinc_oxide_barrier_cream/06_reddit_anecdote_scan.md) | Reddit consensus read: Triple Paste as crowd default, Aquaphor Baby 40% as rescue, Sudocrem as comparator, and caution threads |
| 07 | [Full product comparison chart](09_zinc_oxide_barrier_cream/07_full_product_comparison_chart.md) | Reddit-mentioned products plus label-checked alternatives in one chart: Triple Paste, Honest, Pipette, Sudocrem, Aquaphor, Desitin, Boudreaux's, Burt's, cica creams, and more |

## 10 — Microneedling and collagen induction · [`10_microneedling_collagen_induction/`](10_microneedling_collagen_induction/)

Mechanical microneedling lane for acne scars, wrinkles/scars, device regulation, home-vs-professional boundary, and RF microneedling risk. This is separated from fractional lasers and non-invasive RF because the injury source is needles: mechanical puncture for standard microneedling, needle-delivered heat for RF microneedling.

| # | File | What it covers |
|---|------|----------------|
| 01 | [Microneedling science brief](10_microneedling_collagen_induction/01_microneedling_science_brief.md) | Mechanical fractional injury, wound-healing cascade, needle depth logic, geometry, and what "collagen induction" can and cannot imply |
| 02 | [Clinical evidence map](10_microneedling_collagen_induction/02_clinical_evidence_map.md) | Acne-scar, wrinkle, scar, pigment/melasma, topical-delivery, home-device, and RF-microneedling evidence separated by confidence |
| 03 | [Regulatory and device landscape](10_microneedling_collagen_induction/03_regulatory_and_device_landscape.md) | FDA QAI category, SkinPen/Exceed/Dr. Pen/Dermalogica examples, openFDA 26-record snapshot, and RF microneedling warning line |
| 04 | [Home vs professional results gap](10_microneedling_collagen_induction/04_home_vs_professional_results_gap.md) | Why a 0.2-0.5 mm home roller is not a SkinPen/Exceed treatment, what home tools can plausibly do, and marketing red flags |
| 05 | [Selection and safety protocol](10_microneedling_collagen_induction/05_selection_and_safety_protocol.md) | Goal picker, provider questions, contraindication prompts, stop rules, and a conservative home-use boundary |

**Supporting material:** [`skin_depth_demo.html`](10_microneedling_collagen_induction/skin_depth_demo.html) interactive depth/benefit explainer, mirrored FDA microneedling guidance, SkinPen De Novo files, selected QAI 510(k) summaries, FDA patient page, FDA RF microneedling safety communication, and an openFDA `QAI` snapshot captured 2026-07-06 in [`source_docs/`](10_microneedling_collagen_induction/source_docs/) and [`data/`](10_microneedling_collagen_induction/data/).

## 11 — HIFU / microfocused ultrasound skin tightening · [`11_hifu_skin_tightening/`](11_hifu_skin_tightening/)

Focused ultrasound lane for clinic HIFU/MFU, home-device claims, focal-depth physics, and the home-vs-clinic boundary. This is separated from RF and fractional lasers because ultrasound depends on acoustic focal geometry, coupling, target depth, and anatomy rather than optical absorption or electrical impedance.

| # | File | What it covers |
|---|------|----------------|
| 01 | [HIFU science brief](11_hifu_skin_tightening/01_hifu_science_brief.md) | Focused ultrasound physics, target depths, thermal coagulation points, and why HIFU does not map cleanly to fractional-laser density math |
| 02 | [Clinic device evidence map](11_hifu_skin_tightening/02_clinic_device_evidence_map.md) | Ulthera/Ultherapy, Sofwave, SCIZER/body contouring, and naming pitfalls separated by FDA status and geometry |
| 03 | [Home device landscape](11_hifu_skin_tightening/03_home_device_landscape.md) | Medicube High Focus Shot, Ussera, generic mini/prosumer HIFU claims, home evidence, and regulatory caveats |
| 04 | [Home vs clinic results gap](11_hifu_skin_tightening/04_home_vs_clinic_results_gap.md) | The fractional-laser-style comparison: why home HIFU is not simply a lower-power/lower-density Ultherapy treatment |
| 05 | [Selection and safety protocol](11_hifu_skin_tightening/05_selection_and_safety_protocol.md) | Goal picker, provider questions, home stop rules, and risk boundaries |

**Supporting material:** [`depth_planner.html`](11_hifu_skin_tightening/depth_planner.html) interactive focal-depth explainer, mirrored FDA HIFU/MFU PDFs, Ulthera IFU, Sofwave files, Medicube product-page captures, PubMed pages, and an openFDA `OHV` snapshot captured 2026-07-07 in [`source_docs/`](11_hifu_skin_tightening/source_docs/) and [`data/`](11_hifu_skin_tightening/data/).

---

## Status / open items
- Verified against primary sources where available: FDA filings, IFUs/manuals, catalog transcriptions, current FDA AccessData/openFDA data, mirrored PDFs, and archived listing images.
- **Open — IPL/DPL:** real Alibaba per-unit pricing, MOQ, and single/sample-unit availability for several OEM IPL models remain partly unconfirmed; for JOVS/AY101, exact wavelength transmission, fluence, pulse duration, and the manufacturer relationship remain unverified despite the shared-shell evidence in doc 17.
- **Open — fractional lasers:** verify whether YDUNVIE Dora is truly 1927nm, whether Iris Ice Plus materially improves on A9/base Iris, and whether a buyable 1927nm home device has credible PIH-safety data.
- **Open — red light therapy:** seller-supplied irradiance meter photos and exact current variant confirmation are still needed before treating Alibaba RLT specs as purchase-grade.
- **Open — non-fractional lasers:** obtain DermRays Revive IFU/manual, label photos, eye-protection requirements, and independent output/thermal testing.
- **Open — RF:** build a device-by-device comparison, verify K-numbers for Silk'n/TriPollar/Medicube variants, and run an Alibaba RF supplier scan.
- **Open — vitamin C:** independently verify Trader Joe's full INCI/pH/stability, monitor post-2025 CEF clone launches, and confirm any SkinCeuticals 2026 patent-pending antioxidant launch from primary materials.
- **Open — zinc oxide:** look for direct adult facial barrier trials separating zinc oxide from petrolatum/dimethicone vehicle effects, and monitor Amazon/DailyMed label changes for the product notes.
- **Open — microneedling:** extract MAUDE adverse events for mechanical and RF microneedling, obtain direct IFUs for each cleared pen, add provider-cost quotes by metro, and capture official consumer roller/stamp product pages.
- **Open — HIFU:** extract MAUDE adverse events for Ulthera/Sofwave/body HIFU, find independent output/focal-depth tests for home HIFU/MFU devices, and capture official manuals/IFUs for Medicube High Focus Shot and Ussera if available.
