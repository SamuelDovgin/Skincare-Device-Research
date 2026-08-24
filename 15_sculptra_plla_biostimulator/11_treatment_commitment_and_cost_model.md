# Sculptra Treatment-Commitment and Cost Model

*Compiled 2026-08-23. Research orientation and budgeting support, not medical or financial advice. All prices, vial counts, visit counts, and time values in the tool are user-entered scenarios—not treatment recommendations or market-price claims.*

## 0. Bottom line

The useful cost question is not “what is one vial?” It is **what would the entire initial series require if the quote, reassessments, travel, and time burden are all counted before treatment begins?** The [treatment-commitment planner](treatment_commitment_planner.html) makes that arithmetic visible without predicting how many vials or sessions a person needs.

## 1. Why this addition exists

The provider checklist already explains which quote components to ask about. This model closes the next gap: it converts the answers into a comparable total and a dated visit sequence. That is especially important for a gradual treatment because a low per-vial headline can omit session fees, follow-up policy, travel, and the time needed for staged reassessment.

## 2. Model specification

The planner uses only user-entered values:

| Output | Calculation |
|---|---|
| Product charge | sessions × vials per session × price per vial |
| Session charges | sessions × injector/facility fee |
| Separate follow-up charges | follow-up visits × follow-up fee |
| Travel | (sessions + separate follow-ups) × round-trip travel cost |
| Time burden | total visit hours × optional value per hour |
| Contingency | selected percentage × direct treatment subtotal |
| Scenario total | product + session + follow-up + travel + time + contingency |

The visit calendar starts on the date selected by the reader and spaces injection-session scenarios by the selected interval. The FDA cheek-wrinkle clinical program evaluated treatment to optimal correction at roughly four-week intervals, with no more than four sessions in that regimen; the current U.S. IFU also describes a single cheek regimen of up to four sequential sessions spaced three to four weeks apart. [[1]](source_docs/FDA_P030050_S039_Sculptra_IFU_2023.pdf)

That evidence is a **regimen boundary**, not a personal need estimate. The tool warns when a scenario exceeds four initial sessions; it does not block custom arithmetic for a quote that needs clarification.

## 3. How to use it

1. Enter the exact quote, including whether the price is per vial or already bundled.
2. Put zero in any genuinely included fee; do not silently assume “follow-up included.”
3. Run at least a low and high scenario when the clinic gives a range.
4. Save or print the result alongside the product name, treatment area, on/off-label status, lot-verification plan, complication contact, and refund/touch-up terms.
5. Compare totals only after confirming that competing quotes describe the same material, anatomy, provider follow-up, and emergency support.

## 4. What the result does not mean

- A lower total is not evidence of safer technique, authentic product, or better results.
- A higher vial count is not evidence of a better “lift.” There is no validated vials-by-age rule.
- The contingency is a budgeting reserve, not an estimate of complication probability or treatment failure.
- The time-value field is optional personal planning arithmetic, not a wage-loss or cost-effectiveness estimate.
- The model does not price management of nodules, vascular injury, or other complications.
- A two-year extension signal does not establish a universal maintenance interval or allow the planner to annualize benefit. [[2]](source_docs/FDA_P030050_S039_SSED_cheek_wrinkles_2023.pdf)

## Practical takeaways

Ask the clinic to resolve any blank field before paying a deposit. The most important non-price questions remain exact product identity, the reason for the proposed anatomy and amount, staged reassessment, delayed-complication coverage, and an emergency plan. Read the [treatment journey and provider checklist](index.html#doc6) before interpreting the cheapest scenario as the best offer.

## Evidence gaps

- There is no public, representative national dataset for current Sculptra price per vial, bundled course price, or provider complication-management cost.
- Regional pricing, taxes, anesthesia, imaging, and follow-up policies change quickly.
- No randomized evidence defines an optimal maintenance interval or validates a cost-per-responder calculation.
- The model has not been validated as a healthcare cost-effectiveness instrument.

## Sources

1. FDA. *Sculptra U.S. Instructions for Use, P030050/S039.* [Local PDF](source_docs/FDA_P030050_S039_Sculptra_IFU_2023.pdf) — evaluated cheek regimen, session spacing, maximum initial sessions, provider-use boundary, and safety information.
2. FDA. *Sculptra P030050/S039 Summary of Safety and Effectiveness Data.* [Local PDF](source_docs/FDA_P030050_S039_SSED_cheek_wrinkles_2023.pdf) — pivotal trial treatment course and follow-up through 24 months; not a maintenance-cost study.
3. [Treatment journey and provider checklist](index.html#doc6) — quote components, staged reassessment, combination planning, and maintenance evidence gaps already established in this topic.
