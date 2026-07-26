# Potential-Results Visualizer: Method and Evidence Limits

*Compiled 2026-07-26. This is an evidence explorer, not a diagnostic model, photo simulator, dosing calculator, or prediction of an individual's result.*

## 0. Bottom line

The visualizer plots **published cohort endpoints exactly as reported**. It lets a reader change the concern (cheek wrinkles or nasolabial folds), assessor/endpoint, and follow-up time, then see treatment, comparator, sample size, confidence interval, and design caveat. It deliberately does not ask for age, sex, vial count, selfies, or provider technique because no validated model converts those inputs into a personal probability or facial image. [[1]](source_docs/FDA_P030050_S039_SSED_cheek_wrinkles_2023.pdf)

## 1. Why a results “simulator” would be misleading

A true outcome model would require reliable relationships among:

- baseline anatomy and wrinkle/volume severity;
- injection area, plane, particle distribution, and total PLLA mass;
- provider technique and session stopping rules;
- age, sex, skin type, immune status, smoking, weight change, sun exposure, and prior procedures;
- objective 3D volume/skin measures and patient priorities;
- adverse events and loss to follow-up.

The trials do not publish a validated multivariable dose-response model with those inputs. Any slider that says “three vials + age 48 = 82% improvement” would invent precision. The tool therefore uses the safer name **potential-results evidence visualizer** and confines outputs to observed study groups.

## 2. Data provenance

The visualizer's data are stored in [`data/sculptra_clinical_endpoints.csv`](data/sculptra_clinical_endpoints.csv). Rows come from:

1. FDA P030050/S039 SSED/IFU tables for the 149-person cheek trial and extension. [[1]](source_docs/FDA_P030050_S039_SSED_cheek_wrinkles_2023.pdf)
2. The randomized 5 mL-versus-8 mL Sculptra NLF study in the U.S. IFU. [[2]](source_docs/FDA_P030050_S039_Sculptra_IFU_2023.pdf)
3. PubMed reports from the 233-person Sculptra-versus-human-collagen NLF trial and extension. [[3]](https://pubmed.ncbi.nlm.nih.gov/21460676/)

No value is scraped from clinic marketing, social media, a before/after image gallery, or a non-Sculptra product.

## 3. Endpoint dictionary

| Endpoint | Definition | Strength | Limitation |
|---|---|---|---|
| GCWS at rest responder | ≥1-grade improvement from baseline in both cheeks | Blinded live evaluator; FDA primary endpoint | Ordinal one-grade threshold; scale/product sponsor involvement |
| GCWS dynamic responder | ≥1-grade improvement in both cheeks during expression | Blinded live evaluator | Secondary endpoint |
| Treating-investigator GAIS | Improved/much improved/very much improved globally | Clinically intuitive and longitudinal | Injector knows treatment; broad “any improvement” threshold |
| Subject GAIS | Participant reports global improvement | Captures patient-perceived value | Unblinded and expectation-sensitive |
| Independent 2D photo identification | Reviewer correctly identifies month-12 image | Blinded, visually stringent | 2D photos can miss live/3D change; denominator not given in SSED summary |
| NLF WAS responder | ≥1-grade improvement on wrinkle scale | Blinded evaluator | Different anatomy, study, preparation, and comparator |
| Subject global evaluation | Subject-perceived overall NLF improvement | Long follow-up available | Secondary endpoint; extension attrition |

These endpoints are not interchangeable. The visualizer never averages them into a single “Sculptra score.”

## 4. Study-population boundary

The cheek trial enrolled adults aged 41–89 with moderate/severe cheek wrinkles; 96.6% were women and 90.6% White. Only 14 participants were Fitzpatrick V–VI. The output should not be presented as a calibrated probability for a man, a wrinkle-free 25-year-old, a person on immunosuppression, or an off-label body site. [[1]](source_docs/FDA_P030050_S039_SSED_cheek_wrinkles_2023.pdf)

## 5. Time handling

- Month values are plotted only when the source reports them.
- Week 48 is displayed as week 48 / approximately 11 months, never interpolated to month 12.
- No curve is fitted between visits.
- Extension results at months 19–24 are visually separated from the randomized base study and labeled as selected follow-up cohorts.
- Immediate injection-day swelling is not plotted as efficacy.

## 6. Uncertainty and attrition

Where the source provides a 95% confidence interval, the chart displays it. When the source reports only a rounded rate, the tool says “CI not reported” rather than manufacturing one. Numerator/denominator are shown when available.

The month-12 primary cheek endpoint uses the FDA's multiple-imputation estimate (70.7%; CI 61.1–80.4) and also notes the observed-case count (63/88, 71.6%). Extension results show the smaller denominators so persistence is not mistaken for full-cohort retention.

## 7. Evidence classes shown in the tool

- **Randomized + blinded primary/secondary endpoint** — strongest.
- **Randomized + unblinded assessor/patient report** — useful but expectation/assessor bias possible.
- **Prospective extension** — durability signal with attrition/selection.
- **Active-comparison NLF study** — informative but not placebo/no-treatment controlled.
- **Single-arm or class-level context** — not used for a headline personal estimate.

## 8. Deterministic validation rules

The visualizer contains a callable `window.runSculptraVisualizerTests()` self-test that verifies:

1. all rates are finite and between 0% and 100%;
2. all confidence intervals are ordered and bound the point estimate when available;
3. numerator never exceeds denominator;
4. the month-12 primary treatment rate exceeds the concurrent control;
5. the independent-photo rate remains distinct from investigator/subject GAIS;
6. extension rows retain smaller denominators and an extension warning;
7. no unsupported interpolation, personal-prediction, or vial-dose function exists;
8. every study source and local data link resolves in the topic audit.

## 9. How to use the result responsibly

- Read the endpoint label before the percentage.
- Prefer the blinded primary endpoint for efficacy orientation.
- Use GAIS to understand perceived improvement, not to replace the primary endpoint.
- Use photo discrimination as a realism check, not proof the live result is invisible.
- Use 24–25 month rows as durability evidence among returners, not a guarantee.
- Treat any clinic promise that exceeds the study population, area, or endpoint as an extrapolation.

## Evidence gaps

- Individual-level trial data needed for subgroup modeling.
- Standardized 3D photography and validated minimal clinically important differences.
- Modern Sculptra-specific HA/CaHA head-to-head data.
- Denominator-based real-world complication rates integrated with benefits.
- Independent replication with diverse sex, race, and skin-type enrollment.

## Sources

1. FDA. P030050/S039 SSED. [Local PDF](source_docs/FDA_P030050_S039_SSED_cheek_wrinkles_2023.pdf) - primary data source for cheek visualizer rows.
2. FDA. Sculptra U.S. IFU. [Local PDF](source_docs/FDA_P030050_S039_Sculptra_IFU_2023.pdf) - NLF reconstitution-study rows and endpoint definitions.
3. Brown SA et al. Subject global evaluation and satisfaction using PLLA versus human collagen. https://pubmed.ncbi.nlm.nih.gov/21460676/ - NLF durability rows through month 25.
4. ClinicalTrials.gov NCT04124692. [Local JSON](data/NCT04124692_cheek_wrinkle_trial.json) - registered protocol/results record captured through the API.
