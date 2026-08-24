# FDA indication matrix and provider verification checklist

*Compiled 2026-08-23 from the topic's mirrored FDA decision summaries. Research orientation, not medical advice. A 510(k) substantial-equivalence decision is not a head-to-head clinical-efficacy ranking.*

## 0. Bottom line

“FDA-cleared microneedling pen” is incomplete. The useful verification unit is:

> **exact model + K-number/De Novo + prescription status + cleared body area + indication + age/phototype scope + sterile cartridge + current IFU**

The seven-source [machine-readable indication matrix](data/fda_microneedling_indication_matrix.csv) shows why:

- SkinPen's foundational De Novo is for **facial acne scars in adults 22+**, with safety/effectiveness not evaluated above 1.5 mm even though the device can adjust higher. [[1]](source_docs/fda-den160029-skinpen-precision-system-de-novo-summary.pdf)
- Exceed's captured clearance is for specific **facial wrinkles in Fitzpatrick I-III**, not acne scars or every skin type. [[2]](source_docs/fda-k180778-exceed-facial-wrinkles.pdf)
- SkinPen's later neck-wrinkle clearance includes **Fitzpatrick II-IV for neck wrinkles** and all Fitzpatrick types for facial acne scars. [[3]](source_docs/fda-k202243-skinpen-neck-wrinkles.pdf)
- SkinStylus K253002 is narrowly useful because it explicitly covers **periorbital wrinkles in Fitzpatrick I-VI, age 34+**. [[4]](source_docs/fda-k253002-skinstylus-sterilock-periorbital-wrinkles.pdf)
- Every device in this matrix is prescription-use. It does not create an FDA-authorized OTC medical-microneedling lane.

## 1. What the FDA files actually authorize

| Filing | Device | Captured indication | Population boundary | Depth fact to keep separate |
|---|---|---|---|---|
| DEN160029 | SkinPen Precision | Facial acne-scar appearance | Adults 22+ | Adjusts to 2.5 mm; safety/effectiveness above 1.5 mm not evaluated and not recommended in the De Novo labeling [[1]](source_docs/fda-den160029-skinpen-precision-system-de-novo-summary.pdf) |
| K180778 | Exceed | Glabellar, periorbital, and cheek-fold wrinkles | Adults 22+; Fitzpatrick I-III | 0.0–1.5 mm adjustment; maximum is not a universal setting [[2]](source_docs/fda-k180778-exceed-facial-wrinkles.pdf) |
| K202243 | SkinPen Precision | Neck wrinkles plus facial acne scars | Adults 22+; neck II-IV, acne scars all types | Area-specific evidence; do not transplant neck depth to every facial zone [[3]](source_docs/fda-k202243-skinpen-neck-wrinkles.pdf) |
| K230420 | Dr.pen system | Facial acne-scar appearance | Adults 22+ | Hardware adjusts to 2.0 mm; clearance does not make consumer A-series pens equivalent [[5]](source_docs/fda-k230420-dr-pen-microneedling-system.pdf) |
| K243800 | Dermalogica PRO Pen | Facial acne-scar appearance | Adults 22+ | 0.2 mm increments to 1.5 mm; sterile single-use 14-pin cartridge disclosed [[6]](source_docs/fda-k243800-dermalogica-pro-pen.pdf) |
| K253002 | SkinStylus SteriLock | Periorbital-wrinkle appearance | Adults 34+; Fitzpatrick I-VI | Exact periorbital treatment depth remains provider/IFU-specific [[4]](source_docs/fda-k253002-skinstylus-sterilock-periorbital-wrinkles.pdf) |
| K252591 | CODE-X | Facial acne-scar appearance | Adults 22+ | 2.0 mm maximum disclosed; no universal protocol inferred [[7]](source_docs/fda-k252591-code-x-microneedling-system.pdf) |

## 2. Why K-number matching changes the consultation

A clinic can truthfully say it owns a cleared microneedling device while still proposing a use outside the captured indication. Off-label practice can be legal and reasonable, but it should be **named**, not hidden behind the word “cleared.”

Ask the provider to fill in this sentence:

> “We are using **[exact device/model]**, cleared in **[K-number/De Novo]** for **[indication/body area/population]**. Your proposed treatment is **on-label / off-label because ___**. The planned cartridge, depth range, passes, interval, and aftercare are **___**.”

That separates four questions that marketing often collapses:

1. Is the exact handpiece legally marketed?
2. Is the proposed indication/body area in the summary?
3. Is the patient population represented?
4. Is the proposed depth/protocol supported by the current IFU and provider training?

## 3. Provider verification checklist

### Device identity

- Exact trade name and model—not “SkinPen-style,” “FDA registered,” or a generic Dr. Pen family name.
- K-number or De Novo number, with applicant/manufacturer matching the device label.
- Current prescription IFU and patient labeling available before consent.
- Cartridge model, needle count, lot/expiry, sterile barrier, and single-use status shown before opening.

### Indication fit

- Target is named precisely: acne-scar appearance, facial wrinkles, neck wrinkles, periorbital wrinkles, or something off-label.
- Body area and minimum age match the filing or the off-label rationale is explained.
- Fitzpatrick restrictions/representation are stated rather than assumed.
- Active acne, melasma/PIH tendency, keloid history, infection, medications, and recent procedures are screened.

### Protocol transparency

- Planned depth is mapped by facial/neck region; it is not “the maximum everywhere.”
- Number of passes and endpoint are explained without using pinpoint bleeding as the only proof of adequate treatment.
- Cleaning, handpiece barrier/fluid-ingress protection, and room infection-control steps are visible.
- No claim that FDA clearance authorizes transdermal delivery of vitamin C, PRP, exosomes, drugs, or cosmetics. FDA's device definition specifically separates that use. [[1]](source_docs/fda-den160029-skinpen-precision-system-de-novo-summary.pdf)[[8]](source_docs/fda-guidance-regulatory-considerations-microneedling-products-2020.pdf)

### Outcome and adverse-event plan

- Standardized photos and a scar/wrinkle scale are chosen before treatment.
- Expected number of sessions, follow-up, downtime, and maintenance are stated.
- The clinic has a plan for infection, herpes reactivation, prolonged erythema, PIH/hypopigmentation, scarring, and unexpected pain/neurologic symptoms.
- RF microneedling is identified as a separate energy-based procedure, not an upgrade setting on the same evidence. FDA's 2025 communication lists burns, scarring, fat loss, disfigurement, and nerve injury. [[9]](source_docs/fda-rf-microneedling-safety-communication-2025-10-15.html)

## 4. Three common misreads corrected

| Misread | Correction |
|---|---|
| “The pen reaches 2.5 mm, so 2.5 mm is cleared and better.” | Hardware range, clinically evaluated range, anatomical thickness, and selected protocol are different facts. |
| “Dr. Pen is FDA-cleared.” | K230420 applies to an exact prescription system/applicant and indication; it does not clear every marketplace pen bearing a similar brand. |
| “FDA-cleared microneedling means approved serum infusion.” | The QAI classification excludes intended transdermal delivery of cosmetics, drugs, biologics, vitamin solutions, or PRP. |

## 5. Practical takeaways

- For acne scars, prioritize exact prescription-device identity, sterile single-use cartridges, scar subtype, and provider experience over brand popularity.
- For wrinkles, verify the precise area and phototype scope; an acne-scar clearance is not automatically a wrinkle clearance.
- Treat maximum depth as a device specification, never as a self-selected treatment target.
- Use the [skin-depth explainer](skin_depth_demo.html) for anatomy intuition, then return to this matrix for regulatory reality.
- Search the existing [QAI clearance panel](index.html#qai) by K-number to see the broader device-family timeline.

## Evidence gaps

- Current IFUs and patient labels are still missing for several devices; FDA summaries do not replace them.
- The matrix does not rank providers, costs, motor performance, cartridge accuracy, or clinical outcomes.
- Later 510(k) submissions may change a device's indications; recheck FDA AccessData before a procedure.
- Fitzpatrick inclusion in a clearance is not proof of equal efficacy or equal PIH risk across all phototypes.
- Predicate equivalence does not mean every cleared pen has independently demonstrated the same clinical effect size.

## Sources

1. FDA DEN160029, SkinPen Precision System De Novo summary. [Local PDF](source_docs/fda-den160029-skinpen-precision-system-de-novo-summary.pdf) - foundational indication, Rx status, depth boundary, topical-delivery exclusion, and special controls.
2. FDA K180778, Exceed Microneedling Device. [Local PDF](source_docs/fda-k180778-exceed-facial-wrinkles.pdf) - facial-wrinkle areas, Fitzpatrick I-III, age 22+, prescription use, and device depth range.
3. FDA K202243, SkinPen neck wrinkles. [Local PDF](source_docs/fda-k202243-skinpen-neck-wrinkles.pdf) - neck II-IV and facial acne-scar all-phototype indication wording.
4. FDA K253002, SkinStylus SteriLock. [Local PDF](source_docs/fda-k253002-skinstylus-sterilock-periorbital-wrinkles.pdf) - periorbital wrinkles, Fitzpatrick I-VI, age 34+.
5. FDA K230420, Dr.pen Microneedling System. [Local PDF](source_docs/fda-k230420-dr-pen-microneedling-system.pdf) - exact applicant/device, facial acne-scar indication, and depth range.
6. FDA K243800, Dermalogica PRO Pen. [Local PDF](source_docs/fda-k243800-dermalogica-pro-pen.pdf) - facial acne-scar indication, 1.5 mm maximum, and sterile single-use cartridge description.
7. FDA K252591, CODE-X. [Local PDF](source_docs/fda-k252591-code-x-microneedling-system.pdf) - facial acne-scar indication and 2.0 mm device maximum.
8. FDA Guidance, *Regulatory Considerations for Microneedling Products*. [Local PDF](source_docs/fda-guidance-regulatory-considerations-microneedling-products-2020.pdf) - medical-device and transdermal-delivery boundaries.
9. FDA RF Microneedling Safety Communication, 2025-10-15. [Local HTML](source_docs/fda-rf-microneedling-safety-communication-2025-10-15.html) - serious RF-microneedling complication and no-home-use warning.
