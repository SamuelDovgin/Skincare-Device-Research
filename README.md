# Skincare Device Research

Research into at-home, light-based skincare devices for **facial redness/erythema, hyperpigmentation, post-inflammatory hyperpigmentation (PIH), and evening skin tone**, plus **hair removal** and **skin-quality (collagen) rejuvenation** as parallel goals. Budget-conscious; covers branded, retail, and Chinese OEM/Alibaba sourcing.

The repo is organized by **product type** into four projects:

| Folder | Product class | Goal |
|--------|---------------|------|
| [`01_ipl_hair_removal/`](01_ipl_hair_removal/) | Broadband IPL (intense pulsed light) | Hair removal; pigment/redness strategy |
| [`02_diode_laser_hair_removal/`](02_diode_laser_hair_removal/) | Diode lasers (Tria 810nm & alternatives) | Targeted hair removal |
| [`03_fractional_laser_resurfacing/`](03_fractional_laser_resurfacing/) | Non-ablative fractional lasers | Skin quality — pigment + collagen |
| [`04_red_light_therapy_handheld/`](04_red_light_therapy_handheld/) | Handheld red/NIR LED therapy | Local pain/recovery adjuncts |

## TL;DR

1. **For the PRIMARY goal (pigment/PIH/redness), a home IPL device is the wrong primary tool.** Broadband IPL can *worsen* pigmentation in pigment-prone skin (~2.96% IPL-induced hyperpigmentation in Fitzpatrick III–IV). Lead instead with **iron-oxide tinted sunscreen + topicals (azelaic acid, tranexamic acid, niacinamide) + non-thermal LED (red 630–660nm / amber ~590nm)**. See **[01 / doc 07](01_ipl_hair_removal/07_alternatives_and_strategy.md)**.
2. **No home IPL device — branded or Chinese OEM — is FDA-cleared for anything but hair removal** (all are product code OHT). Verified from the actual filings. See **[01 / doc 03](01_ipl_hair_removal/03_fda_510k_analysis.md)**.
3. **If buying a device for the hair goal:** best OEM target = **Fansizhe T023A** (510nm filter, sapphire cooling; FDA K223928 baseline 5.5 J/cm², and a **seller video on 2026-06-14 measured a real 18.23J / 6.08 J/cm² single flash** — the highest verified single-pulse fluence in the dataset). Budget single-pulse fallback = **Fansizhe T001M/T001A**. Lowest-risk branded option = **Nood Flasher 2.0** ($169, FDA-cleared, 510nm, warranty). See **[01 / doc 06](01_ipl_hair_removal/06_final_recommendation.md)**.
4. **For skin quality (collagen/pigment), the device class is non-ablative fractional resurfacing**, not IPL or hair lasers — a different thread entirely. See **[`03_fractional_laser_resurfacing/`](03_fractional_laser_resurfacing/)**.
5. **For localized pain/recovery, handheld red-light devices are a separate, adjunctive project.** Evidence is mixed for carpal tunnel/back/hand pain, so output documentation and conservative dosing matter more than "5W" marketing. See **[`04_red_light_therapy_handheld/`](04_red_light_therapy_handheld/)**.

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

**Supporting material:** [Natalie/Fansizhe conversation notes](01_ipl_hair_removal/fansizhe_natalie_conversation_notes.md) · Fansizhe & Semlamp FDA 510(k) PDFs · product catalogs · `Weiss_IPL.pdf` (clinical IPL photoaging parameters) · [`fda_data_pipeline/`](01_ipl_hair_removal/fda_data_pipeline/) — pulls all FDA 510(k) IPL clearances from openFDA, OCRs every filing, extracts pulse modes/fluence, and generates doc 08 (re-runnable; see its [STRATEGY.md](01_ipl_hair_removal/fda_data_pipeline/STRATEGY.md)).

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

A **separate device class for the *skin-quality* goal (pigment + collagen), not hair.** Non-ablative fractional lasers (Clear + Brilliant, Tria FRX, NIRA, YDUNVIE Iris/Dora) and the user's owned Tria SmoothBeauty: science, in-office-vs-home expectations, full device landscape, the Jiangsu Unimed/YDUNVIE supplier map, RFQ templates, and a future research plan. See its [README](03_fractional_laser_resurfacing/README.md).

## 04 — Handheld red light therapy · [`04_red_light_therapy_handheld/`](04_red_light_therapy_handheld/)

Handheld red/NIR LED devices for **hands, wrist/carpal-tunnel symptoms, and localized back pain**, with Alibaba listing-image OCR plus a text-only added Ideatherapy RL-series listing, device-output ranking, and a final buy/skip decision.

| # | File | What it covers |
|---|------|----------------|
| 01 | [Handheld RLT spec comparison](04_red_light_therapy_handheld/01_handheld_rlt_spec_comparison.md) | Full side-by-side of 12 Alibaba listings: wavelengths, irradiance, cert claims, controls, and ranking |
| 02 | [Raw extracted specs](04_red_light_therapy_handheld/02_raw_extracted_specs.md) | Traceability dump of listing text and OCR'd image specs |
| 03 | [Independent research & decision](04_red_light_therapy_handheld/03_independent_research_and_decision.md) | Literature context, dose math, current listing audit, supplier questions, and final recommendation |

**Supporting material:** 92 archived listing images in [`listing_images/`](04_red_light_therapy_handheld/listing_images/) for L1-L11, a text-only supplied Alibaba capture for L12, plus the project [README](04_red_light_therapy_handheld/README.md).

---

## Status / open items
- Verified against primary sources where available: FDA filings, IFUs/manuals, catalog transcriptions, current FDA AccessData/openFDA data, mirrored PDFs, and archived listing images.
- **Open — IPL:** real Alibaba per-unit pricing, MOQ, and single/sample-unit availability for the OEM IPL models remain partly unconfirmed; prices in docs 02/06 are estimates.
- **Open — fractional lasers:** verify whether YDUNVIE Dora is truly 1927nm, whether Iris Ice Plus materially improves on A9/base Iris, and whether a buyable 1927nm home device has credible PIH-safety data.
- **Open — red light therapy:** seller-supplied irradiance meter photos and exact current variant confirmation are still needed before treating Alibaba RLT specs as purchase-grade.
