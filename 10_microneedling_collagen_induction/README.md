# Microneedling and Collagen Induction

Compiled 2026-07-06. This is research orientation, not medical advice. Microneedling can be a medical procedure when the device penetrates living skin or is intended to change skin structure/function. Use a qualified clinician for medical microneedling decisions.

This topic covers **mechanical microneedling**: dermarollers, dermastamps, powered microneedling pens, prescription FDA-cleared systems, superficial home rollers/patches, and the adjacent but higher-risk **RF microneedling** branch. It is separated from fractional lasers and non-invasive RF because the injury source is needles, not optical absorption or bulk electrical heating.

> **Key distinction:** professional microneedling is a controlled mechanical wound-healing procedure. Superficial home "microneedling" rollers are usually exfoliation/product-absorption tools. RF microneedling adds heat at depth and is a medical procedure the FDA says should not be used at home.

## TL;DR

1. **Best-evidence use case: atrophic acne scars.** Systematic reviews of randomized trials consistently find improvement with microneedling, and FDA's SkinPen De Novo created a Class II, prescription-only microneedling category for facial acne scars in adults 22+.
2. **Wrinkle/scar indications exist, but they are narrower.** FDA has authorized microneedling devices for facial acne scars, facial wrinkles, neck wrinkles, and abdominal scars in specified adult populations and body areas. Do not generalize those clearances to every scar, pigment issue, or "collagen" claim.
3. **No FDA-authorized over-the-counter medical microneedling exists.** FDA says it has not authorized any microneedling medical devices for OTC sale. Superficial home rollers may avoid device status only when they do not penetrate living skin and make appearance/exfoliation claims.
4. **The major home-use gap is control and sterility, not just depth.** Prescription systems use sterile single-use cartridges, validated cleaning/disinfection, penetration-depth accuracy testing, fluid-ingress controls, and clinician training. Cheap rollers/stamps rarely provide that safety stack.
5. **Do not use microneedling as a serum/PRP/drug-infusion hack.** FDA's microneedling classification excludes devices intended for transdermal delivery of cosmetics, drugs, biologics, vitamin solutions, or PRP; the risks of combination/off-label use are not established.
6. **RF microneedling belongs in the professional procedure lane.** FDA's 2025 safety communication reports burns, scarring, fat loss, disfigurement, nerve damage, and injuries requiring medical/surgical intervention, and states RF microneedling devices should not be used at home.

## Documents

| # | File | What it covers |
|---|------|----------------|
| 01 | [Microneedling science brief](01_microneedling_science_brief.md) | Mechanical fractional injury, wound-healing cascade, needle depth logic, what "collagen induction" can and cannot imply |
| 02 | [Clinical evidence map](02_clinical_evidence_map.md) | Acne-scar, wrinkle, scar, pigment/melasma, topical-delivery, and RF-microneedling evidence separated by confidence |
| 03 | [Regulatory and device landscape](03_regulatory_and_device_landscape.md) | FDA QAI category, SkinPen/Exceed/Dr. Pen/Dermalogica examples, openFDA 26-record snapshot, RF microneedling warning line |
| 04 | [Home vs professional results gap](04_home_vs_professional_results_gap.md) | Why a 0.2-0.5 mm home roller is not a SkinPen/Exceed treatment, what home tools can plausibly do, and marketing red flags |
| 05 | [Selection and safety protocol](05_selection_and_safety_protocol.md) | Goal-based picker, when to seek a provider, what to ask, stop rules, contraindications, and a conservative home-use boundary |

## Relationship to other folders

- Closest outcome overlap: [`03_fractional_laser_resurfacing/`](../03_fractional_laser_resurfacing/) for texture, acne marks, pigment, and collagen remodeling. Fractional laser creates thermal microthermal zones; microneedling creates mechanical punctures.
- Closest risk/adjacency overlap: [`07_radio_frequency_skin_tightening/`](../07_radio_frequency_skin_tightening/) for non-invasive RF and RF microneedling. RF microneedling is not an at-home substitute for home RF.
- Pigment strategy still depends on [`01_ipl_hair_removal/07_alternatives_and_strategy.md`](../01_ipl_hair_removal/07_alternatives_and_strategy.md): photoprotection and topicals lead; microneedling is not the first-line pigment device.
- Barrier aftercare connects to [`09_zinc_oxide_barrier_cream/03_safety_protocol_and_routine_fit.md`](../09_zinc_oxide_barrier_cream/03_safety_protocol_and_routine_fit.md), but heavy occlusion after fresh needling should follow clinician aftercare, not internet slugging logic.

## Supporting material

- [`skin_depth_demo.html`](skin_depth_demo.html) is an interactive skin-depth explainer that maps needle depth to target layer, plausible benefit, evidence boundary, and main risk.
- [`source_docs/`](source_docs/) contains FDA guidance, FDA device summaries, FDA microneedling pages, and the 2025 RF microneedling safety communication.
- [`data/openfda-qai-510k-2026-07-06.json`](data/openfda-qai-510k-2026-07-06.json) is a live openFDA product-code `QAI` snapshot captured 2026-07-06. API metadata says last updated 2026-06-22 and total results = 26.
- [`data/openfda-qai-510k-2026-07-06.csv`](data/openfda-qai-510k-2026-07-06.csv) is a reader-friendly extract of K-number, decision date, device, applicant, country, clearance type, and decision description.

## Status / open items

- **Done:** FDA microneedling guidance mirrored; SkinPen De Novo/order and decision summary mirrored; SkinPen K202243, Exceed K180778, Dr. Pen K230420, Dermalogica K243800, SkinStylus K253002, and CODE-X K252591 summaries mirrored; openFDA QAI snapshot captured.
- **Still needed:** a full MAUDE adverse-event extraction for microneedling/RF microneedling; direct IFUs for each cleared pen; provider-cost quotes by metro; better official product-source captures for home rollers/stamps.
- **Evidence gap:** direct, high-quality evidence for home consumer rollers/stamps treating acne scars or wrinkles remains weak. Most credible data are from clinician-performed powered devices or professional RF microneedling studies.

### Sources

1. FDA Microneedling Devices page. https://www.fda.gov/medical-devices/aesthetic-cosmetic-devices/microneedling-devices - primary source for legally authorized indications, no OTC authorization, risk list, contraindication prompts, cartridge reuse warning, and topical/PRP delivery boundary.
2. FDA De Novo Summary DEN160029, SkinPen Precision System. [Local PDF](source_docs/fda-den160029-skinpen-precision-system-de-novo-summary.pdf) - primary source for QAI, 21 CFR 878.4430, Rx status, acne-scar indication, 1.5 mm evaluated-depth caveat, clinical outcomes, and adverse events.
3. FDA Guidance, Regulatory Considerations for Microneedling Products. [Local PDF](source_docs/fda-guidance-regulatory-considerations-microneedling-products-2020.pdf) - primary source for device vs non-device boundary, stratum-corneum/living-skin distinction, and claims that trigger device regulation.
4. openFDA device 510(k) API query, product code QAI, captured 2026-07-06. [JSON](data/openfda-qai-510k-2026-07-06.json) / [CSV](data/openfda-qai-510k-2026-07-06.csv) - primary dataset for 26 QAI records through FDA API metadata last updated 2026-06-22.
5. FDA RF Microneedling Safety Communication, issued 2025-10-15. [Local HTML](source_docs/fda-rf-microneedling-safety-communication-2025-10-15.html) - primary source for serious RF microneedling complications and the home-use warning.
