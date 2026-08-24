# Combination Rules and Evidence Map

*Compiled 2026-07-12. This framework is educational, not diagnostic or prescriptive. “Avoid together” means the planner's conservative routine-fit rule, not a proven universal contraindication unless the source explicitly says so.*

## 0. Bottom line

The planner rewards **coverage of essentials and tolerability**, not the number of products. Sunscreen for meaningful UV exposure, moisturizer, one retinoid strategy, and sustainable adherence outrank optional actives and devices. The planner's sunscreen toggle is an adherence heuristic, not a room-specific UV calculation; the photographed desk is modeled separately in the rendered [current regimen audit](../markdown-viewer.html?file=13_combined_skincare_regimen/01_current_regimen_audit.md#2-sunscreen-at-this-desk-room-specific-uva-model).

This page documents the single-routine scoring model. For weekly AM/PM placement, formulation-specific ingredient pairs, and state-based device recovery, use the [Skincare Stack Lab](skincare_stack_lab.html) and its rendered [independent interaction evidence](../markdown-viewer.html?file=13_combined_skincare_regimen/05_ingredient_compatibility_and_weekly_planner.md).

## 1. Evidence ladder used by the meter

| Class | Meaning | Examples |
|---|---|---|
| A — foundation | Strong benefit-to-risk or official guidance for the stated role | Broad-spectrum sunscreen when meaningful UV exposure is expected, moisturizer, gentle cleansing |
| B — targeted | Good evidence for a defined concern, with irritation/selection caveats | Adapalene for acne; azelaic acid for acne/rosacea/melasma; professional indication-specific devices |
| C — adjunct | Plausible/limited evidence or parameter-dependent benefit | Vitamin C, peptides, consumer RLT, niacinamide, tranexamic acid |
| D — specialist/episodic | Not a daily routine card; anatomy, sterility, settings, or clinician judgment dominate | HIFU, professional fractional laser, RF microneedling, peels, hydroquinone courses |
| E — duplicate/overload | Adds little unique benefit to an existing slot or increases irritation | Multiple retinoids, Tria + exfoliating acid + adapalene in one evening |

## 2. Conflict rules

| Combination | Planner output | Basis and boundary |
|---|---|---|
| Tria + adapalene same day | Strong caution; separate by day and recover first | Tria creates expected erythema/stinging; adapalene is irritating and its label cautions multiple irritants. Exact washout is unknown. [[1]](../03_fractional_laser_resurfacing/tria_smoothbeauty/source_docs/tria-smoothbeauty-instructions-for-use.pdf)[[2]](https://dailymed.nlm.nih.gov/dailymed/drugInfo.cfm?setid=5d5340d6-e1da-46e4-973c-40cf8e907aa3) |
| Tria + azelaic acid same session | Caution; bland aftercare preferred | Conservative irritation control; not an explicit IFU contraindication |
| Tria + AHA/BHA/peel | Avoid in same session/course when reactive | Tria IFU excludes recently peeled/resurfaced skin; adapalene label also cautions AHA/glycolic products. [[1]](../03_fractional_laser_resurfacing/tria_smoothbeauty/source_docs/tria-smoothbeauty-instructions-for-use.pdf)[[2]](https://dailymed.nlm.nih.gov/dailymed/drugInfo.cfm?setid=5d5340d6-e1da-46e4-973c-40cf8e907aa3) |
| Adapalene + tretinoin/retinol/retinal | Duplicate retinoid warning | More irritation without a clear reason to stack |
| Adapalene + azelaic acid | May coexist, but separate initially if stinging | Both can irritate; azelaic evidence is indication-specific [[3]](https://pubmed.ncbi.nlm.nih.gov/37550898/) |
| Vitamin C AM + adapalene PM | Generally sensible if tolerated | Time separation reduces crowding; vitamin C remains an adjunct, sunscreen remains the anchor |
| RLT + topicals | Dose/product dependent | Apply on bare skin unless the device/manual validates a topical; photosensitizing drugs require clinician/manual review |
| Two energy devices same day | Strong caution | No general evidence validates consumer multimodal stacking; mechanism-specific risks differ |
| Home microneedling/HIFU/RF microneedling | Specialist boundary | Sterility, anatomy, depth, coupling, and adverse-event management dominate |

## 3. Meter design

The score is an educational fit score, not a biological outcome prediction. The builder exposes five 0–100 dimensions:

| Dimension | What raises it | What does not |
|---|---|---|
| Protection — 27% | Morning broad-spectrum sunscreen, daily use, outdoor reapplication, exposed-body protection, shade/UPF | Owning sunscreen but using it only occasionally |
| Selected-goal fit — 25% | Capped coverage for the goals the user selects: anti-aging, pigment/redness, acne/pores, barrier/tolerance, and whole-health habits | Adding every optional serum; credit within each goal plateaus |
| Recovery — 18% | Moisturizer, limited cleansing load, sleep, and bland Tria aftercare | Occluding an already-irritating stack and calling it recovery |
| Health habits — 15% | Sleep opportunity, exercise, no tobacco/smoke, a varied diet, and appropriate dermatology review | Beauty supplements or devices as substitutes for general health behaviors |
| Tolerability — 15% | Low irritation and no major conflicts | Tria + adapalene, duplicate retinoids, multiple energy devices, excessive cleansing, or aggressive treatment on already-irritated skin |

The implementation is:

`overall = 0.27(protection) + 0.25(goal fit) + 0.18(recovery) + 0.15(health) + 0.15(tolerability) − complexity penalty`

The complexity penalty is capped at 12 points and begins only after the routine passes a reasonable number of unique skincare/device steps. Strong interactions add to an illustrative irritation-risk budget; they are not estimates of adverse-event probability. Every optional lane has capped credit, while duplication and conflicts continue to subtract.

The suggestions are ordered by likely leverage: first protection and active device/retinoid conflicts, then barrier load and goal gaps, then parameter verification and whole-health habits. Selecting “skin irritated now,” “Tria treatment day,” “outdoor/sweaty day,” “RLT dose verified,” or a pregnancy/nursing context changes both the score and the recommendations.

The builder also exposes each selected concern as its own 0–100 coverage score. This prevents a strong acne score from hiding weak pigment, barrier, or health-habit coverage inside the average. The **“Find my path toward 100”** action uses the current catalog, selected concerns, and safety context to construct a higher-fit single-day routine; it then reports:

- current versus projected overall fit;
- each concern's current versus projected coverage;
- the weighted dimensions responsible for the current shortfall;
- the exact cards it would add, pause, or move;
- why a conservative Tria or recovery day may remain below 100.

The routine finder does not silently mark sunscreen as a daily habit, claim an RLT dose has been verified, clear irritated skin, or change pregnancy/nursing context. It leaves those toggles as entered. A 100 is therefore a **theoretical routine-fit ceiling**, not the expected score for every day type and not a treatment target. On Tria days, separating adapalene, acids, and other devices can improve safety while deliberately lowering same-day concern coverage; those concerns belong across separate day types rather than in one maximal stack.

It does not estimate collagen gain, acne clearance, cancer prevention, or “biological age.” The score deliberately plateaus: adding more items can reduce it.

### Mobile interaction model

- Desktop uses the visible ↕ handle for pointer drag-and-drop directly into the Morning / Body-Daytime / After Gym / Night slots; clicking a card remains the no-drag alternative.
- Mobile uses a dedicated `touch-action: none` drag handle. Touching the ↕ handle opens a fixed four-slot drop dock; moving the finger and releasing over a slot performs the drop without relying on mobile Safari's inconsistent HTML5 drag API.
- Tapping any catalog or placed card opens a large bottom placement sheet as an accessible fallback.
- Placed cards can be moved with the same touch drag handle or removed directly.
- The overall score remains visible in the sticky mobile header, and no scoring control depends on hover.

## 4. What has the best anti-aging leverage

1. Daily UV protection and avoiding tanning/sunburn.
2. Sustainable retinoid use if appropriate and tolerated.
3. Moisture/barrier support that keeps the first two usable.
4. No tobacco, adequate sleep, exercise, and a generally nutritious diet—health priorities that no serum substitutes for.
5. Targeted adjuncts/devices chosen for one defined concern, not “everything.”

## Evidence gaps

- There is no validated universal scoring system for combining consumer skincare actives and devices; weights are transparent heuristics.
- The five component weights and interaction penalties are illustrative decision-support assumptions, not measured effect sizes or adverse-event probabilities.
- The path finder is a deterministic optimization over the planner's own catalog and rules, not a validated regimen generator; its projected score inherits every limitation of the scoring model.
- Product formulas, sunscreen labels, and device outputs change; bottle/manual data override catalog defaults.
- The sunscreen score does not know window geometry, glass type, direct-sun status, local UVA, or time outdoors. It must not be interpreted as evidence that sunscreen is necessary in every indoor room.
- Skin type, disease history, medication use, pregnancy, and clinician procedures can materially change routine fit.

## Sources

1. Tria SmoothBeauty IFU. [Local PDF](../03_fractional_laser_resurfacing/tria_smoothbeauty/source_docs/tria-smoothbeauty-instructions-for-use.pdf) - treatment preparation, cadence, exclusions, reactions, and stop rules.
2. DailyMed adapalene gel 0.1%. https://dailymed.nlm.nih.gov/dailymed/drugInfo.cfm?setid=5d5340d6-e1da-46e4-973c-40cf8e907aa3 - once-daily directions, irritation cautions, sunscreen, moisturizer, and severe-irritation stop rule.
3. King S et al. Azelaic acid systematic review. https://pubmed.ncbi.nlm.nih.gov/37550898/ - 43 RCTs support acne/rosacea/melasma; no eligible aging RCTs.
4. Hughes MCB et al. Sunscreen randomized trial. https://pubmed.ncbi.nlm.nih.gov/23732711/ - 24% less measured aging with daily versus discretionary sunscreen.
5. Tran QT et al. Adapalene 0.1% aging RCT. https://pubmed.ncbi.nlm.nih.gov/40990960/ - small RCT with improvement and frequent early stinging/xerosis.
6. Bragato EF et al. Facial PBM frequency RCT. https://pubmed.ncbi.nlm.nih.gov/40167796/ - parameter-specific evidence; 2 versus 3 weekly sessions, not a universal daily-panel rule.
