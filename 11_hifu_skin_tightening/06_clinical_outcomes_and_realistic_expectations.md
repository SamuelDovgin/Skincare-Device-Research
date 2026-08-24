# Clinical outcomes and realistic expectations: Ulthera and Sofwave

*Compiled 2026-08-23 from topic-local FDA decision summaries. Research orientation, not medical advice. The table preserves each filing's endpoint and denominator; it is not a cross-device efficacy ranking.*

## 0. Bottom line

Clinic focused ultrasound can produce measurable and photographically detectable changes, but the FDA summaries describe **subtle aesthetic endpoints**, not facelift-sized transformations:

- Sofwave's eyebrow study reported a mean **0.78 mm maximal** and **0.69 mm average** eyebrow-height lift at three months. [[1]](source_docs/fda-k211483-sofwave-lifting-indications.pdf)
- Its submental/neck study reported a mean **38 mm² area-based lift**; that unit is not 38 linear millimeters and should not be read that way. [[1]](source_docs/fda-k211483-sofwave-lifting-indications.pdf)
- Sofwave's facial-wrinkle filing reported 45/58 (78%) correctly identified pre/post photo sequences with at least a one-unit elastosis-scale reduction, while 34/58 (59%) said they were satisfied. [[2]](source_docs/fda-k191421-sofacia-sofwave.pdf)
- Ulthera's décolleté filing is cautionary: 54 of 108 per-protocol day-180 photo sets were excluded for inconsistent photography, and the final 36/54 improvement result used a post-hoc masked endpoint without a prespecified success criterion. [[3]](source_docs/fda-k134032-ulthera-decollete-lines-wrinkles.pdf)

The [machine-readable outcome ledger](data/focused_ultrasound_clinical_outcomes.csv) keeps objective/masked, clinician-rated, patient-reported, pain, and safety fields separate.

## 1. Why this page exists

The existing clinic map answers **which systems and indications are credible**. The missing question was **how large and how certain were the outcomes in the FDA summaries?**

This page avoids three common errors:

1. turning “correctly identified pre/post photos” into percent wrinkle reduction;
2. comparing 0.78 mm eyebrow height with 38 mm² submental area as if they were the same unit;
3. treating an uncontrolled filing study as proof that one device beats another.

## 2. Outcome ledger

| Filing / indication | Objective or masked endpoint | Patient/clinician endpoint | Pain/safety signal | Best interpretation |
|---|---|---|---|---|
| Ulthera K121700 · submental/neck lift | 51/70 had at least 20 mm² lift; 84.3% of that subgroup was identified as improved by masked evaluators [[4]](source_docs/fda-k121700-ulthera-submental-neck.pdf) | Satisfaction questionnaires were used, but the extracted summary does not give the rate | Events described as mild/short-lived; no related serious or unanticipated events | A measurable lift signal in an open-label study; conditional wording and no control limit magnitude claims |
| Ulthera K134032 · décolleté lines/wrinkles | 36/54 evaluable photo sets judged improved at day 180 [[3]](source_docs/fda-k134032-ulthera-decollete-lines-wrinkles.pdf) | CGAIS and satisfaction collected | See filing | 67% applies only to the quality-filtered subset; primary-scale and photography problems materially weaken confidence |
| Sofwave K191421 · facial lines/wrinkles | 45/58 (78%) correctly ordered photo pairs and ≥1 elastosis-scale unit reduction at week 12 [[2]](source_docs/fda-k191421-sofacia-sofwave.pdf) | 42/58 (72%) noticed improvement; 34/58 (59%) satisfied | Mean pain 7.49/10; no device-related events reported | Detectable wrinkle change for many, but satisfaction was lower and follow-up short |
| Sofwave K211483 · eyebrow lift | 53/67 (79%) photo sequences correct; mean maximal lift 0.78 mm, average lift 0.69 mm [[1]](source_docs/fda-k211483-sofwave-lifting-indications.pdf) | 51/64 (80%) improved by PGAIS; 55% reported improvement and satisfaction | Mean zone pain 6.4/10 | The clearest realistic scale anchor: measurable, generally subtle lift |
| Sofwave K211483 · submental/neck lift | 60/75 (80%) photo sequences correct; mean lift 38 mm² [[1]](source_docs/fda-k211483-sofwave-lifting-indications.pdf) | 61/72 (85%) improved by PGAIS; 55% reported improvement; 50% satisfied | Mean zone pain 5.3/10 | Area-based change can be real while patient satisfaction remains about half |

## 3. How to read the endpoints

| Endpoint | What it measures | What it does not measure |
|---|---|---|
| Correct pre/post sequence | Whether blinded reviewers can detect direction of change | Percent lift, clinical importance, or satisfaction |
| Millimeters of eyebrow height | Linear position change on standardized 2D images | A surgical brow lift or whole-face laxity correction |
| Square millimeters of lift | Change in an outlined area metric | Linear movement, fat loss, or a universal contour score |
| PGAIS/CGAIS | Clinician's global change category | Blinded objective magnitude unless the assessment itself is masked |
| Patient improvement/satisfaction | Whether the result felt worthwhile | Objective tissue change or freedom from expectation bias |
| Pain score | Procedural burden | Efficacy; more pain is not proof of more lift |

## 4. Consultation worksheet

Ask a clinic to translate its proposed procedure into the same evidence fields:

| Field | Provider answer |
|---|---|
| Exact device/model and FDA filing |  |
| Exact indication and target zone |  |
| Imaging/visualization and transducer/applicator |  |
| Expected objective scale (mm, mm², wrinkle grade, photo ordering) |  |
| Expected patient-satisfaction range |  |
| Follow-up when the result should peak |  |
| Typical pain-control plan and downtime |  |
| Plan for burns, numbness, weakness, asymmetry, fat loss, or prolonged pain |  |
| What anatomy would make the result too small or the risk too high |  |

If the provider can offer only “X shots,” “collagen stimulation,” or dramatic unstandardized before/after photos, the decision is not yet evidence-ready.

## 5. Practical takeaways

- Treat **subtle, delayed improvement** as the default expectation.
- Use standardized baseline, three-month, and six-month photos with unchanged lighting, focal length, position, expression, and weight context.
- Do not compare filing percentages unless the endpoint, denominator, follow-up, body zone, and photo-quality rules match.
- Patient satisfaction can be materially lower than physician/imaging response; ask which outcome matters to you.
- The clinic results do not validate home HIFU. The [depth planner](depth_planner.html) explains why focal geometry, coupling, imaging, and anatomy remain separate requirements.

## Evidence gaps

- None of these rows is a randomized head-to-head Ulthera-versus-Sofwave trial.
- Filing summaries provide selective performance reporting and do not replace full protocols, statistical analysis plans, or publications.
- Durability beyond the reported follow-up and outcomes after repeat treatments are incompletely described.
- Darker phototypes, very lean faces, prior fillers, previous energy procedures, and baseline volume loss need better stratified outcome and adverse-event reporting.
- MAUDE is useful for signal detection but cannot supply complication incidence because use counts and reporting completeness are unknown.

## Sources

1. FDA K211483, Sofwave lifting indications. [Local PDF](source_docs/fda-k211483-sofwave-lifting-indications.pdf) - eyebrow and submental/neck study denominators, objective measurements, PGAIS, satisfaction, pain, and safety.
2. FDA K191421, Sofacia/Sofwave facial lines and wrinkles. [Local PDF](source_docs/fda-k191421-sofacia-sofwave.pdf) - 12-week masked/photo, elastosis, satisfaction, pain, and safety endpoints.
3. FDA K134032, Ulthera décolleté lines/wrinkles. [Local PDF](source_docs/fda-k134032-ulthera-decollete-lines-wrinkles.pdf) - photo-quality exclusions, post-hoc endpoint change, and 180-day evaluable-subset result.
4. FDA K121700, Ulthera submental/neck lift. [Local PDF](source_docs/fda-k121700-ulthera-submental-neck.pdf) - 70-person open-label performance summary and adverse-event statement.
5. Ulthera System IFU. [Local PDF](source_docs/ulthera-us-instructions-for-use-2021.pdf) - device geometry, training, contraindications, expected responses, and adverse-event warnings.
6. PubMed 39625163, MFU-V adverse-event review. https://pubmed.ncbi.nlm.nih.gov/39625163/ - external context for transient effects, lipoatrophy, neurologic sequelae, and scarring reports.
