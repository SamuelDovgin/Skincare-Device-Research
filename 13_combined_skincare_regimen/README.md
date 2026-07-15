# Combined Skincare Regimen

This is the archive's cross-category routine lane: it combines daily skincare, the owned Tria SmoothBeauty/Age-Defying fractional laser, full-body red-light therapy, exercise-day cleansing, sun protection, optional actives, and the other researched device classes into one decision surface. It does **not** replace the mechanism-specific folders or personalized dermatology care.

*Compiled 2026-07-12. Research orientation, not medical advice. Product names and percentages should be checked against the bottle in hand.*

## Bottom line

1. **Your foundation is already strong:** moisturizer, vitamin C, adapalene, azelaic acid, and SPF all have plausible roles. The issue is scheduling, not a lack of products.
2. **The highest-value change is daily sunscreen, not only “if outside.”** Use broad-spectrum SPF 30+ on face, neck, ears, and other exposed skin every morning; reapply after sweating and about every two hours while outdoors. A randomized trial found 24% less measured skin aging with daily versus discretionary sunscreen use over 4.5 years. [[1]](https://pubmed.ncbi.nlm.nih.gov/23732711/)
3. **Do not make Tria + azelaic acid + adapalene a single aggressive evening.** The Tria IFU requires clean, dry, product-free skin and says not to treat skin still red/swollen; adapalene labeling warns that irritation rises with multiple topical acne medications/irritants. An exact evidence-based washout interval is not published, so separating Tria and adapalene/acid nights is a conservative inference, not a manufacturer rule. [[2]](../03_fractional_laser_resurfacing/tria_smoothbeauty/source_docs/tria-smoothbeauty-instructions-for-use.pdf)[[3]](https://dailymed.nlm.nih.gov/dailymed/drugInfo.cfm?setid=5d5340d6-e1da-46e4-973c-40cf8e907aa3)
4. **Three full face washes may be too much if skin feels tight, hot, flaky, or stings.** Keep the post-gym cleanse when sweat/sunscreen need removal, but merge it with the bedtime cleanse when timing allows; use a mild cleanser and avoid scrubbing.
5. **Do not add another retinoid, exfoliating acid, or energy device merely to maximize anti-aging.** Consistency with sunscreen + one retinoid + moisturizer has a better evidence-to-irritation ratio than stacking.
6. **Your full-body RLT panel is a dose question, not a minutes question.** Ten minutes is only meaningful with wavelength, irradiance, distance, frequency, and the panel manual. Facial rejuvenation trials have used specific measured doses and commonly 2-3 sessions/week; that does not validate every panel's daily ten-minute protocol. [[4]](https://pubmed.ncbi.nlm.nih.gov/40167796/)

## Recommended baseline

| Time | Default routine | Tria-course adjustment |
|---|---|---|
| Morning | Optional gentle cleanse/rinse → Trader Joe's vitamin C if tolerated → CeraVe moisturizer as needed → Round Lab broad-spectrum SPF 50 every day | Same; sunscreen is especially important |
| RLT | Follow panel manual; clean bare skin is easiest for reproducible dosing; use eye protection if the manual requires it | Do not assume RLT cancels irritation or permits more laser/actives |
| After gym | Gentle cleanse or thorough rinse depending on sweat/sunscreen → Good Molecules 10% azelaic acid only if calm → moisturizer | On Tria days, keep this bland and skip azelaic acid near the laser session |
| Night, non-Tria | Gentle cleanse if needed → pea-size 0.1% adapalene to dry face → CeraVe moisturizer; buffer with moisturizer if irritation-prone | Use on selected non-laser nights only if skin is fully calm |
| Night, Tria | Clean, completely dry, product-free face → Tria exactly per IFU → bland moisturizer | Skip adapalene, exfoliating acids, and azelaic acid that session; resume based on recovery/tolerance |
| Recovery | Gentle cleanse/rinse → moisturizer → sunscreen | No laser or actives until baseline comfort returns |

## Documents and tool

| # | File | What it covers |
|---|---|---|
| 01 | [Current regimen audit](01_current_regimen_audit.md) | What to keep, change, avoid, and verify in the routine exactly as supplied |
| 02 | [Combination rules and evidence map](02_combination_rules_and_evidence_map.md) | Evidence hierarchy, device/active conflict rules, overload logic, and uncertainty |
| Tool | [Drag-and-drop routine builder](routine_builder.html) | Mobile touch drag/drop plus tap placement, all researched device lanes, per-concern scores, an explainable “path toward 100” routine finder, goal/context controls, five-part overall score, ranked improvements, warnings, strengths, local save, and copyable export |

## Relationship to neighboring folders

- [`03_fractional_laser_resurfacing/`](../03_fractional_laser_resurfacing/) owns the Tria SmoothBeauty/FRX evidence and IFU.
- [`04_red_light_therapy_handheld/`](../04_red_light_therapy_handheld/) owns RLT output/dose reasoning.
- [`08_vitamin_c_serums/`](../08_vitamin_c_serums/) owns vitamin C formulation and Differin-fit analysis.
- [`09_zinc_oxide_barrier_cream/`](../09_zinc_oxide_barrier_cream/) owns barrier-rescue options.
- [`12_peptides_in_skincare/`](../12_peptides_in_skincare/) is an adjacent active lane under development; peptides remain optional in this planner.
- IPL, diode laser, non-fractional laser, RF, microneedling, and HIFU remain mechanism-specific topics; the builder classifies them by routine fit and professional/home boundary rather than repeating their research.

## Status / open items

- The builder now shows anti-aging, pigment/redness, acne/pores, barrier/tolerance, and whole-health coverage separately instead of hiding them inside one average. “Find my path toward 100” constructs and explains a lower-conflict, higher-fit single-day plan, shows the projected score and exact card changes, and leaves safety/habit context toggles unchanged. It explicitly treats 100 as a theoretical model ceiling—not a clinical-result promise or a reason to stack incompatible treatments.
- Mobile interaction verification completed at a 390 × 844 viewport: no horizontal overflow; touch drag to the fixed slot dock and tap-to-place both passed automated browser checks. The embedded deterministic self-test also checks scoring bounds, preset ordering, sunscreen sensitivity, duplicate-retinoid penalties, Tria/adapalene warnings, path-finder improvement/separation, per-concern bounds, and catalog validity.
- Confirm the exact Trader Joe's vitamin C product and the exact “Cretaceous” moisturizer name; the planner preserves them as user-entered items rather than inventing formulas.
- Confirm the RLT panel model, wavelengths, irradiance at the actual distance, and manufacturer eye-protection/cadence instructions before judging daily ten-minute dosing.
- A dermatologist should individualize adapalene/laser spacing for persistent irritation, melasma/PIH tendency, eczema/rosacea, pregnancy planning, or prescription therapy.

## Sources

1. Hughes MCB et al. *Sunscreen and prevention of skin aging: a randomized trial.* Ann Intern Med. 2013. https://pubmed.ncbi.nlm.nih.gov/23732711/ - daily sunscreen group had 24% less measured aging than discretionary use over 4.5 years.
2. Tria SmoothBeauty Instructions for Use. [Local PDF](../03_fractional_laser_resurfacing/tria_smoothbeauty/source_docs/tria-smoothbeauty-instructions-for-use.pdf) - clean/dry/product-free treatment, labeled cadence, reactions, and stop rules.
3. DailyMed. Adapalene gel 0.1% Drug Facts. https://dailymed.nlm.nih.gov/dailymed/drugInfo.cfm?setid=5d5340d6-e1da-46e4-973c-40cf8e907aa3 - once-daily use, sunscreen/moisturizer guidance, irritation cautions, and severe-irritation stop rule.
4. Bragato EF et al. *Role of photobiomodulation application frequency in facial rejuvenation.* Lasers Med Sci. 2025. https://pubmed.ncbi.nlm.nih.gov/40167796/ - parameter-specific 660 nm facial LED trial at 8.05 J/cm², 2-3 sessions weekly.
5. King S et al. *A systematic review to evaluate the efficacy of azelaic acid in acne, rosacea, melasma and skin aging.* J Cosmet Dermatol. 2023. https://pubmed.ncbi.nlm.nih.gov/37550898/ - 43 RCTs; support for acne, rosacea, and melasma, but no eligible skin-aging RCTs.
6. Tran QT et al. *Effectiveness and tolerability of adapalene cream 0.1% in female skin ageing.* Indian J Dermatol Venereol Leprol. 2025. https://pubmed.ncbi.nlm.nih.gov/40990960/ - small six-month RCT with wrinkle/pigment improvement and frequent early stinging/xerosis.
7. American Academy of Dermatology. Practice Safe Sun. https://www.aad.org/public/everyday-care/sun-protection/shade-clothing-sunscreen/practice-safe-sun - broad-spectrum, water-resistant SPF 30+, protective clothing, and outdoor reapplication guidance.
