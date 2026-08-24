# Localized PBM evidence and N-of-1 protocol

*Rapid evidence synthesis updated 2026-08-23. Photobiomodulation (PBM) is not a substitute for diagnosis or urgent care. Follow the exact device instructions and clinician guidance.*

## Bottom line

The topic’s panel model now estimates dose and whole-body exposure well. The largest remaining gap was the original use case—**localized hand, carpal-tunnel, and pain treatment**—where protocols and outcomes are much less consistent than the phrase “red light therapy” implies.

- For **carpal tunnel syndrome (CTS)**, recent syntheses do not show a dependable clinically important pain or grip-strength advantage over splinting/sham, although some analyses report a function or pain signal.
- For **hand osteoarthritis and chronic low-back pain**, sham-controlled results include important nulls.
- A 2026 randomized home-use trial is especially relevant: active multiwavelength low-level light and sham both improved, but there was no meaningful between-group advantage.
- Therefore the most useful role for the PL300 is a **measurement-led personal trial with a prespecified stop rule**, not borrowing a favorable paper’s wavelength or joule number and assuming equivalence.

## 1. Evidence map by condition

| Condition / source | Evidence | Result | Translation to this PL300 |
|---|---|---|---|
| CTS, 2025 systematic review/meta-analysis | 13 randomized trials | No advantage for pain or grip strength; function improved, with major dosimetry heterogeneity | Directly relevant condition, but protocols/devices vary and do not validate a panel exposure [[1]](https://pubmed.ncbi.nlm.nih.gov/39776290/) |
| CTS, 2020 network meta-analysis | 6 RCTs, 418 participants | LLLT + splint reduced pain by 0.53 cm vs splint alone—judged not clinically significant—and was not superior for symptoms/function | Strong caution against expecting a large additive effect [[2]](https://pubmed.ncbi.nlm.nih.gov/32026843/) |
| Peripheral neuropathic pain review | Condition-stratified meta-analysis | Reported a CTS pain signal, illustrating that synthesis choices change the conclusion | A contrasting signal, not a settled dose prescription [[3]](https://pubmed.ncbi.nlm.nih.gov/36535605/) |
| Hand osteoarthritis | Randomized sham-controlled trial; 42 active, 46 sham | No significant pain, stiffness, or function advantage after 6 weeks | Direct hand-region null; laser applicator geometry differs from a panel [[4]](https://pubmed.ncbi.nlm.nih.gov/15704096/) |
| Chronic nonspecific low-back pain, 2020 | Systematic review, 12 RCTs, pooled n=1,046 | Effect versus sham was clinically unimportant; review did not support use | High-value null; not hand-specific [[5]](https://pubmed.ncbi.nlm.nih.gov/32680739/) |
| Chronic low-back pain, 2016 | Meta-analysis, 15 studies, n=1,039 | Reported a larger pain signal in higher-dose/shorter-duration subgroups | Conflicting synthesis; subgroup/dose findings are hypothesis-generating [[6]](https://pubmed.ncbi.nlm.nih.gov/27207675/) |
| Home-based multiwavelength LLLT, 2026 | Randomized double-blind sham-controlled trial, n=30; 20 min/day, 5 days/week, 3 weeks | Active and sham improved; no between-group differences, pain effect size about 0.08; no adverse events reported | Best home-use design here, but 670/780/830/910 nm, 3.83 mW/cm², 4.59 J/cm², and 92.7 cm² applicator do not match PL300 [[7]](https://pmc.ncbi.nlm.nih.gov/articles/PMC12987803/) |

The disagreement is informative: condition definition, co-intervention, sham, wavelength, irradiance, spot/area, dose calculation, treatment schedule, and follow-up all change the estimate. “Same joules” does not mean same exposure.

## 2. Why a paper cannot set the PL300 timer

The PL300 archive currently treats its purchased 630/660/810/830/850 nm allocation and output curve as partially measured, partially claimed, and partially modeled. The best-estimate six-inch irradiance is about 70 mW/cm², with a 60–90 mW/cm² working interval and a separate 161.241 mW/cm² hotspot stress observation. Those values are far above the 3.83 mW/cm² active irradiance in the 2026 home trial. See the [measured-spec audit](index.html#doc4) before setting a timer.

Four non-equivalences matter:

1. **Beam geometry:** a contact laser/probe, 92.7 cm² applicator, and large panel illuminate different tissue volumes.
2. **Spectral mix:** an allocation ratio is not measured radiant power per wavelength.
3. **Incident vs absorbed dose:** skin angle, distance, pigmentation, reflection, and depth change what tissue receives.
4. **Thermal confounding:** a high-output panel may feel warm; heat, expectation, rest time, and light cannot be cleanly separated without a credible sham.

The [PL300 dose visualizer](pl300_dose_visualizer.html) is appropriate for exposure bookkeeping, not for converting a meta-analysis into a therapeutic prescription.

## 3. A conservative personal measurement protocol

This is an **N-of-1 outcome audit**, not proof of efficacy.

### Before starting

- Obtain a diagnosis for persistent numbness, weakness, progressive symptoms, traumatic pain, or symptoms that could need timely treatment. Do not delay indicated care.
- Freeze the background regimen for the audit: splint use, exercises, medications, workstation changes, sleep plan, and other devices.
- Choose **one primary outcome** before looking at results: daily average pain 0–10, Boston Carpal Tunnel Questionnaire score, grip task, or a specific timed activity.
- Define a personally meaningful success threshold in advance (for example, “I would continue only if typing tolerance rises by X minutes without worse night symptoms”).
- Fix device mode, distance, body position, target area, timer, and time of day. Do not increase dose during the trial.

### Schedule

| Phase | Duration | Action |
|---|---:|---|
| Baseline A | 7 days | No PBM change; record the primary outcome, sleep, workload, co-interventions, and symptoms daily |
| Treatment B | 21 days | Use one fixed conservative exposure only if permitted by the device/clinical plan; record outcome before treatment and at the same next-day time |
| Observation | 7 days | Stop PBM, keep other variables stable, continue logging to look for persistence or regression |

Download the [localized PBM log](data/localized_pbm_n_of_1_log.csv). Photograph the setup once with a ruler so distance and angle can be reproduced.

### Decision rule

- **Continue only** if the prespecified primary outcome crosses the personal threshold, the change is sustained rather than one favorable day, co-interventions stayed stable, and no safety endpoint failed.
- **Call it inconclusive** if workload, medication, splinting, sleep, or setup changed materially; do not rescue the result by switching endpoints.
- **Stop** for burn-like heat, persistent redness, swelling, worsening pain/numbness/weakness, headache/eye symptoms, or any device/IFU stop condition.
- A baseline-to-treatment improvement cannot separate treatment from placebo, regression to the mean, rest, or natural fluctuation. Report it as a personal signal, not proof.

## 4. What would materially improve confidence

A useful direct study would randomize a PL300-like panel against a credible heat/light-matched sham, stratify a diagnosed condition, map irradiance across the actual hand/wrist plane, report per-band output, fix co-interventions, use validated function plus pain outcomes, and follow participants after stopping treatment.

## Evidence gaps

- No product-specific clinical trial was located for the PL300.
- CTS studies are heterogeneous and often small; pooled conclusions conflict.
- Panel-to-probe dose translation is unvalidated.
- Blinding visible/thermal high-output panels is difficult.
- Longer-term function, nerve-conduction outcomes, and harms are sparsely reported for home panels.
- A personal A–B observation cannot establish causality or population benefit.

### Sources

1. [2025 CTS PBM systematic review and meta-analysis](https://pubmed.ncbi.nlm.nih.gov/39776290/) — 13 randomized trials; pain/grip null, function signal, and dosimetry heterogeneity.
2. [2020 CTS network meta-analysis](https://pubmed.ncbi.nlm.nih.gov/32026843/) — six RCTs/418 participants and clinically small add-on pain estimate.
3. [PBM for peripheral neuropathic pain meta-analysis](https://pubmed.ncbi.nlm.nih.gov/36535605/) — contrasting CTS subgroup pain signal.
4. [Sham-controlled low-level laser trial in hand osteoarthritis](https://pubmed.ncbi.nlm.nih.gov/15704096/) — direct hand-region randomized null.
5. [2020 chronic nonspecific low-back-pain systematic review](https://pubmed.ncbi.nlm.nih.gov/32680739/) — 12 RCTs and clinically unimportant sham-controlled effect.
6. [2016 low-back-pain meta-analysis](https://pubmed.ncbi.nlm.nih.gov/27207675/) — contrasting pooled/subgroup signal.
7. [2026 randomized home-based multiwavelength LLLT trial](https://pmc.ncbi.nlm.nih.gov/articles/PMC12987803/) — direct home-use sham-controlled protocol, exposure details, null between-group result, and adverse-event reporting.
