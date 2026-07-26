# Outcome Scales and Responder Definitions: What “≥1 Grade” Means

*Compiled 2026-07-26. Research orientation, not medical advice. These are study endpoint definitions, not a personal outcome prediction or a universal definition of a noticeable cosmetic change.*

## 0. Bottom line

In the pivotal Sculptra cheek trial, **“≥1-grade improvement” means moving down by at least one category on the five-level Galderma Cheek Wrinkles Scale (GCWS), from baseline to follow-up, on the left and right cheeks at the same visit**. Lower scores mean less severe wrinkles. The primary month-12 endpoint required both cheeks to qualify; improvement on only one cheek did not count as a responder. [[1]](source_docs/FDA_P030050_S039_SSED_cheek_wrinkles_2023.pdf)

This is an **ordinal category change**, not a one-percentage-point change, one wrinkle disappearing, a one-millimeter lift, or proof that the change was obvious in photographs. The randomized trial publication is available at [PubMed PMID 38206151](https://pubmed.ncbi.nlm.nih.gov/38206151/), and the complete scale wording is preserved in the [ClinicalTrials.gov trial record](data/NCT04124692_cheek_wrinkle_trial.json). [[2]](data/NCT04124692_cheek_wrinkle_trial.json)

## 1. The exact GCWS point system

| GCWS grade | Study label | Trial-record description |
|---:|---|---|
| **0** | None | No lines or wrinkles |
| **1** | Mild | Only a few superficial lines |
| **2** | Moderate | Many superficial lines or a few shallow wrinkles |
| **3** | Severe | Many shallow wrinkles or a few moderate-depth wrinkles |
| **4** | Very severe | Many moderate wrinkles or at least one deep wrinkle, with or without redundant folds |

The trial used the scale in two conditions: [[2]](data/NCT04124692_cheek_wrinkle_trial.json)

- **GCWS at rest:** the participant's face was relaxed. This produced the primary month-12 endpoint.
- **GCWS dynamic:** the participant made a closed maximum smile. This was a secondary endpoint.

The primary trial population entered with **grade 2 or 3 on each cheek**. A movement from 3 to 2, 2 to 1, or 3 to 1 therefore met the per-cheek threshold. A score cannot improve below 0. [[1]](source_docs/FDA_P030050_S039_SSED_cheek_wrinkles_2023.pdf)

## 2. Worked responder examples

| Baseline left / right | Month 12 left / right | Grade change | Primary responder? | Why |
|---|---|---|---|---|
| 3 / 3 | 2 / 2 | −1 / −1 | **Yes** | Both cheeks improved by at least one grade. |
| 3 / 2 | 2 / 1 | −1 / −1 | **Yes** | Different starting grades are acceptable; both sides crossed the threshold. |
| 3 / 3 | 1 / 2 | −2 / −1 | **Yes** | “At least one” includes a two-grade improvement. |
| 3 / 2 | 2 / 2 | −1 / 0 | **No** | Only the left cheek improved. The bilateral concurrent rule was not met. |
| 2 / 2 | 2 / 2 | 0 / 0 | **No** | Stable severity is not a responder. |
| 2 / 2 | 3 / 1 | +1 / −1 | **No** | One cheek worsened even though the other improved. |

These are arithmetic examples of the prespecified rule, not individual trial participants.

## 3. How the 70.7% result was calculated

The FDA's primary month-12 analysis reported: [[1]](source_docs/FDA_P030050_S039_SSED_cheek_wrinkles_2023.pdf)

| Analysis | Sculptra | No treatment | Interpretation |
|---|---:|---:|---|
| **Prespecified multiple-imputation estimate** | **70.7%** (95% CI 61.1–80.4) | **25.9%** (13.4–38.3) | FDA headline estimate accounting for missing month-12 values under the specified imputation model |
| **Observed cases** | **63/88 (71.6%)** | **12/46 (26.1%)** | Raw qualifying participants among those with observed month-12 assessments |

Fourteen month-12 scores were imputed: nine in the treatment group and five in the control group. That is why the FDA estimate is 70.7%, while the journal abstract and observed-case table report 71.6%. They describe the same trial using different missing-data presentations—not conflicting studies. [[1]](source_docs/FDA_P030050_S039_SSED_cheek_wrinkles_2023.pdf) [[3]](https://pubmed.ncbi.nlm.nih.gov/38206151/)

## 4. What a one-grade response does and does not prove

### It does show

- a blinded live evaluator judged both cheeks to be in a lower severity category than at baseline;
- the prespecified regulatory threshold was met at that visit; and
- the treatment and control groups can be compared using the same rule.

### It does not show

- the number or percentage of wrinkles removed;
- a measured change in facial volume, collagen mass, millimeters of projection, or “lift”;
- that the participant, injector, and an independent photo reviewer all agreed;
- that the change exceeded a separately established minimal clinically important difference; or
- that every responder improved by the same amount—a one-grade and a two-grade improvement both count once.

The scale is identified as validated in the registry and trial publication, but the pivotal responder threshold should not be re-labeled as a universal minimal clinically important difference without a separate anchor-based analysis. The study's much lower independent-photo identification rate—37% for Sculptra versus 16% control—illustrates that live ordinal grading and visible photo discrimination answer different questions. [[1]](source_docs/FDA_P030050_S039_SSED_cheek_wrinkles_2023.pdf)

## 5. The six-point NLF Wrinkle Assessment Scale used by the visualizer

The visualizer's nasolabial-fold endpoint—**“≥1-grade improvement in wrinkle severity”**—uses the separate six-point photographic Wrinkle Assessment Scale (WAS), not the cheek GCWS. Figure 5 of the FDA IFU supplies these anchors: [[4]](source_docs/FDA_P030050_S039_Sculptra_IFU_2023.pdf)

| WAS grade | FDA Figure 5 label |
|---:|---|
| **0** | No wrinkles |
| **1** | Just perceptible wrinkle |
| **2** | Shallow wrinkles |
| **3** | Moderately deep wrinkle |
| **4** | Deep wrinkle, well-defined edges |
| **5** | Very deep wrinkle, redundant fold |

Here, a lower number is also better. A change from 4→3, 3→2, or 2→1 is a one-grade improvement; 4→2 is a two-grade improvement. The immediate-use study's Week-48 responder rate counted participants with at least a one-grade reduction from baseline on the WAS. The FDA IFU reports **74.1% (43/58)** for the 8 mL-plus-lidocaine group and **66.7% (14/21)** for the 5 mL group. Both groups received Sculptra, so this is an active preparation comparison—not proof of efficacy versus no treatment. [[4]](source_docs/FDA_P030050_S039_Sculptra_IFU_2023.pdf)

## 6. Do not mix these other “point systems”

| Measure | Scale / threshold | What it asks | Why it is not interchangeable with GCWS |
|---|---|---|---|
| **NLF Wrinkle Assessment Scale (WAS)** | Six-point photo-numeric severity scale (0–5); the exact anchors are shown above | How severe is the nasolabial fold? | Different anatomy, scale, photographs, and trials. See Figure 5 and the clinical tables in the FDA IFU. [[4]](source_docs/FDA_P030050_S039_Sculptra_IFU_2023.pdf) |
| **GAIS** | Seven ordered categories from very much improved to very much worse in the cheek trial | How does the overall appearance compare with baseline? | Global change rating; “improved” is broader and was unblinded for investigator/participant assessments. |
| **Independent 2D-photo identification** | Binary correct/incorrect identification of the month-12 image | Can a reviewer distinguish the post-treatment photograph? | Not a wrinkle-severity grade and sensitive to the photographic view. |
| **FACE-Q cheeks score** | Item responses converted to a 0–100 Rasch-transformed score | How satisfied is the participant with cheek appearance? | Patient-reported satisfaction, not evaluator-rated wrinkle severity. |
| **WSRS in comparator studies** | Usually a five-category nasolabial-fold severity scale; exact anchors follow the paper/protocol | How severe is the NLF in that specific study? | A WSRS change in a PDLLA/PLLA trial cannot be substituted for the Sculptra GCWS cheek endpoint. |
| **Bellafill acne-scar ASRS responder** | At least a two-point improvement for at least 50% of treated scars | Did enough individual acne scars cross a stricter scar threshold? | Different product, indication, unit of analysis, scale, and responder rule. |

## 7. How references should be written in this archive

Preferred shorthand:

> **70.7% month-12 FDA-estimated bilateral GCWS responder rate:** at least a one-grade reduction from baseline on the 0–4 GCWS at rest, on both cheeks concurrently, as judged live by a blinded evaluator.

Avoid:

- “70.7% wrinkle reduction”;
- “70.7% of wrinkles disappeared”;
- “70.7% had a dramatic result”;
- “one point of improvement” without naming the scale and direction; or
- combining GCWS, GAIS, photo identification, and satisfaction into one success rate.

## Evidence gaps

- A readily identifiable standalone peer-reviewed GCWS development/validation paper with the full validation sample and reliability coefficients was not located in this pass; the trial registry and pivotal paper identify the scale as validated and provide the anchors.
- No anchor-based analysis located here establishes that a one-grade GCWS change is the minimal clinically important difference for every patient.
- Ordinal categories do not reveal the physical distance between grades; 3→2 and 2→1 should not be assumed to represent equal biological change.
- Inter-rater performance in routine clinical photography may differ from a trained, standardized trial setting.

## Sources

1. FDA. P030050/S039 Summary of Safety and Effectiveness Data. [Local PDF](source_docs/FDA_P030050_S039_SSED_cheek_wrinkles_2023.pdf) - trial population, bilateral responder definition, observed and imputed month-12 analyses, and endpoint comparisons.
2. ClinicalTrials.gov NCT04124692 results record. [Local JSON](data/NCT04124692_cheek_wrinkle_trial.json) - exact 0–4 GCWS anchors, at-rest/dynamic conditions, bilateral responder definition, and registered outcomes.
3. Fabi SG et al. Effectiveness and Safety of Sculptra PLLA in the Correction of Cheek Wrinkles. https://pubmed.ncbi.nlm.nih.gov/38206151/ - randomized pivotal-trial publication and observed-case responder result.
4. FDA. Sculptra U.S. IFU P030050/S039. [Local PDF](source_docs/FDA_P030050_S039_Sculptra_IFU_2023.pdf) - GCWS endpoint, six-point NLF WAS, Figure 5 photographic scale, and clinical tables.
