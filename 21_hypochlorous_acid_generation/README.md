# Hypochlorous Acid: pH-Controlled Generation and Compatibility

*Created 2026-08-24; updated 2026-08-25. This is a measurement-led recipe and calibration topic, not a medical, cosmetic, disinfection, or product-certification guide. It does not approve a homemade liquid for skin, eyes, inhalation, face-contact bedding, or a regulatory disinfectant claim.*

## Why this is now a separate topic

The archive's DIY-powder topic remains about cosmetic ingredients. This topic owns a different decision: whether a specific electrolysis generator can support a **manual-compatible, acidified-brine reference run** and whether the measured output is in the project’s pH/FAC calibration band.

The supplied PWPAM manual is deliberately kept separate. It calls its output sodium hypochlorite, specifies salt plus water, and gives cleaning-oriented concentration rows. It does **not** authorize vinegar, a pH target, or an HOCl facial-product workflow. Its manual record is preserved in the [PWPAM boundary note](index.html#doc3); it is not a recipe to modify. [[7]](../19_diy_topical_formulation/source_docs/pwpam_manual_2026-08-24_recipe-and-use.jpg)

## Short answer

1. **Only use the acidified-brine reference with a generator whose own manual expressly permits that chemistry.** A salt-only, proprietary-capsule, unknown, or PWPAM-type manual is a hard stop. Do not add vinegar before or after a salt-only run. Mixing hypochlorites with acid can release toxic chlorine gas. [[1]](https://www.cdc.gov/infection-control/hcp/disinfection-sterilization/chemical-disinfectants.html)
2. **The source ratios stay fixed while batch size can scale:** 2.00 g pure non-iodized NaCl per liter and no more than the manual's 5.0 mL/L of 5% distilled white vinegar. The developer offers 200–1,000 mL water (approximately 200–1,000 g); only the 1,000 mL points are manufacturer-published, so smaller-volume times are labeled proportional sensitivity estimates and require confirmed electrode immersion. [[2]](source_docs/eco-one-user-manual.pdf) [[3]](source_docs/farah-al-haj-ali-2021-electrolyzed-water.pdf)
3. **The skincare developer spans 40–500 ppm:** the 1 L presets are 3/5/8/16/40 minutes for 40/60/100/200/500 ppm, with 100 ppm at 8 minutes as the default concentration reference. Intermediate FAC and smaller-volume time values are model outputs, not official programs. Published Eco One batches varied materially, so final pH and FAC still have to be measured. [[2]](source_docs/eco-one-user-manual.pdf) [[4]](source_docs/stony-brook-eco-one-hocl-study-2021.pdf) [[8]](source_docs/FDA_510k_K180305_Hychloderm_0.01pct_HOCl.pdf) [[9]](source_docs/Zhang_2023_0.01pct_HOCl_blepharitis_RCT.pdf) [[11]](https://store.hocl.com/ecoone/)
4. **pH is selectable for planning but measured for calibration.** The pH control changes an illustrative, source-anchored pre-batch vinegar estimate capped at 5 mL/L; the dashed pH graph is not measured kinetics. A completed chlorine-containing batch is never counter-adjusted. [[2]](source_docs/eco-one-user-manual.pdf) [[4]](source_docs/stony-brook-eco-one-hocl-study-2021.pdf) [[5]](source_docs/hypo-7-5-product-manual.pdf)
5. **Use the two tools in order:** first the [generator & product-compatibility checker](product_compatibility_checker.html), then the [HOCl recipe & output guide](hypochlorous_acid_calibration_planner.html). Neither tool authorizes altering a completed chlorine-containing solution.

## Documents

| # | Rendered research page | What it answers |
|---|---|---|
| 01 | [Scaled recipe, time curve, and QC](index.html#doc1) | How the source ratios scale, which time/FAC points are official, how the pH sensitivity works, and what real batches measured. |
| 02 | [Generator and product compatibility](index.html#doc2) | How manual chemistry, reservoir materials, test range, pH method, and intended use determine whether the generic reference workflow applies. |
| 03 | [PWPAM manual boundary](index.html#doc3) | Why the supplied PWPAM salt-only cleaning unit is recorded separately and cannot enter the vinegar-based workflow. |

## Interactive tools

- [Skincare HOCl recipe developer](hypochlorous_acid_calibration_planner.html) — continuous sliders for 200–1,000 mL water (approximately 200–1,000 g; 1 mL increments), 40–500 ppm FAC (1 ppm increments), final pH 4.5–6.5, and starting-water pH (0.01 increments), plus convenience buttons for the five published FAC references and common pH scenarios; scaled salt/time/vinegar recipe; FAC and pH-over-time planning graphs; paired measurement classification; and a chat-ready next-batch report.
- [Generator & product-compatibility checker](product_compatibility_checker.html) — exposes the manual, material, measurement, and intended-use gates before the planner is offered.
- [Rendered source manifest](../markdown-viewer.html?file=21_hypochlorous_acid_generation/source_docs/README.md) — primary manual images, official safety guidance, and the peer-reviewed source record.

## Calibration bands used here

| Result | Interpretation in this project | Next action |
|---|---|---|
| pH ≤ 3.0 or pH > 7.0 | Outside the user’s requested record envelope | Stop. Do not counter-adjust a completed batch. Review the manual and make no unapproved chemistry change. |
| pH > 3.0 and < 4.0 | Inside the broad envelope but below the cited working band | Stop/investigate. It is not a normal target or a skin/product approval. |
| pH 4.0–4.9 | Inside the exact manual's recipe expectation | Pair it with FAC and method quality; repeat a separate fresh batch before describing the process as repeatable. |
| pH 5.0–6.0 | Preferred overlap across the two archived vinegar-compatible manuals | Log the paired pH/FAC measurements. This remains a process observation, not an efficacy or safety certificate. |
| pH 6.1–6.5 | Plausible but outside the exact manual's 4–6 expectation | Recheck the method and repeat only through a fresh manual-compatible batch. |
| pH 6.6–7.0 | Outside the cited working bands | Investigate; do not add acid to the completed batch. |

## Scope boundaries

- Do not mix acid with an existing sodium-hypochlorite/bleach solution, PWPAM output, household cleaners, chlorine tablets, or ammonia-containing products. [[1]](https://www.cdc.gov/infection-control/hcp/disinfection-sterilization/chemical-disinfectants.html)
- Do not infer that pH or an FAC strip establishes exact HOCl concentration, purity, stability, face safety, eye safety, skin compatibility, shelf life, or a disinfectant claim.
- Device materials matter: chlorine solutions can corrode metals, and the generator maker—not this tool—owns compatibility and warranty guidance. [[1]](https://www.cdc.gov/infection-control/hcp/disinfection-sterilization/chemical-disinfectants.html)
- For skin or face-contact use, choose a finished, appropriately labeled product rather than treating this calibration lane as a substitute.

## Sources

1. [CDC, Chemical Disinfectants](https://www.cdc.gov/infection-control/hcp/disinfection-sterilization/chemical-disinfectants.html) — chlorine chemistry, pH/speciation context, material cautions, and acid/ammonia mixing hazard.
2. [Eco One user manual](source_docs/eco-one-user-manual.pdf) — exact one-liter recipe and nominal FAC/time rows.
3. [Farah & Al-Haj Ali, 2021](source_docs/farah-al-haj-ali-2021-electrolyzed-water.pdf) — peer-reviewed 2 g/L salt + 5 mL/L vinegar preparation.
4. [Stony Brook Eco One study](source_docs/stony-brook-eco-one-hocl-study-2021.pdf) — measured batch pH/FAC values showing variability around the manual curve.
5. [HYPO 7.5 product manual](source_docs/hypo-7-5-product-manual.pdf) — separate larger-scale vinegar-compatible system and required final tests.
6. [CDC, Chlorine chemical-emergency fact sheet](https://www.cdc.gov/chemical-emergencies/chemical-fact-sheets/chlorine.html) — exposure and emergency context.
7. User-supplied PWPAM manual photographs — exact device identity, salt-only rows, coarse strip chart, and warning language; archived in the adjacent DIY topic as direct image records.
8. [FDA 510(k) K180305 Hychloderm summary](source_docs/FDA_510k_K180305_Hychloderm_0.01pct_HOCl.pdf) — primary regulatory record for a finished buffered 0.01% HOCl skin/wound solution; not evidence of home-batch equivalence.
9. [Zhang et al., 2023](source_docs/Zhang_2023_0.01pct_HOCl_blepharitis_RCT.pdf) — randomized trial using 0.01% topical HOCl in a specific adjunctive eyelid-hygiene protocol.
10. [Tran et al., 2021](https://pubmed.ncbi.nlm.nih.gov/33247899/) — facial-skin antisepsis comparison in which 0.01% HOCl did not outperform chlorhexidine; counterweight against treating the concentration reference as a universal efficacy claim.
11. [Official Eco One product page](https://store.hocl.com/ecoone/) — current one-liter production table through 500 ppm and manufacturer capacity/recipe context; accessed 2026-08-25.
