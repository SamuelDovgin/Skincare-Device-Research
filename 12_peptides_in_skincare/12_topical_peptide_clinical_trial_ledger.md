# Topical peptide clinical-trial ledger

*Compiled 2026-08-23 from the topic's preserved full text and PubMed records. Research orientation, not medical advice. This is a trial-design audit—not an ingredient-price score, concentration estimate, or product recommendation.*

## 0. Bottom line

The topical-peptide evidence base is much smaller than the product and ingredient universe:

- Only **pal-KTTKS** and **Argireline** have directly auditable, peptide-isolating randomized topical trials in this core set, and each still relies heavily on one older study. [[1]](source_docs/pal-kttks-2005-rct-pubmed.xml)[[2]](source_docs/argireline-2013-rct-pubmed.xml)
- The only controlled GHK-Cu study preserved here found **no objective advantage** for erythema, wrinkles, or overall skin quality after CO2 laser; satisfaction favored the copper regimen. [[3]](source_docs/ghk-cu-post-laser-2006-trial-pubmed.xml)
- CHP-9, OS-01, and PTPD-12 are interesting but each is currently a **single early program** with important comparator, formula, size, or independence limits. [[4]](source_docs/chang-2025-cyclized-hexapeptide-9-trial.xml)[[5]](source_docs/os01-peptide14-2025-rct-pubmed.xml)[[6]](source_docs/ptpd12-pigment-2025-rct-pubmed.xml)
- The 2026 meta-analysis included 19 RCTs/1,341 participants, but reported only two high-quality topical studies and found that the pooled wrinkle signal was largely driven by oral formulations. [[7]](source_docs/nukaly-2026-oral-topical-peptides-systematic-review.pdf)

The [machine-readable ledger](data/topical_peptide_clinical_trial_ledger.csv) keeps comparator, duration, endpoint, independence, and limitation fields separate from the price and formula models.

## 1. Why this addition matters

This topic already answers “what peptides cost?” and “how much might be in the bottle?” Those are commercial/formulation questions. They do not answer:

> **Was the peptide itself isolated against a meaningful control, in enough people, for long enough, with an endpoint that matches my goal?**

The ledger therefore treats trial design as a sequence of gates:

1. peptide identity and final concentration disclosed;
2. matched vehicle or credible active comparator;
3. randomization/blinding;
4. objective endpoint plus participant-centered outcome;
5. duration long enough for the claimed endpoint;
6. independent replication and diverse population;
7. durability after stopping.

No peptide in this core set clears all seven.

## 2. Study-by-study audit

| Ingredient/program | Best preserved study | What it adds | Why confidence stops where it does |
|---|---|---|---|
| Pal-KTTKS | 93 women; 12-week randomized, double-blind, split-face matched-moisturizer trial; 3 ppm [[1]](source_docs/pal-kttks-2005-rct-pubmed.xml) | Cleanest classic signal that a named topical peptide can improve fine lines beyond vehicle | One manufacturer-authored landmark trial; limited demographic breadth; little independent replication |
| Argireline | 60 participants; randomized 3:1; placebo; twice daily for four weeks [[2]](source_docs/argireline-2013-rct-pubmed.xml) | Direct peri-orbital wrinkle/replica signal | Short, uneven allocation, one main trial; delivery remains a formulation constraint |
| GHK-Cu | Randomized post-CO2-laser regimen study; 13 completers; 12 weeks [[3]](source_docs/ghk-cu-post-laser-2006-trial-pubmed.xml) | Important negative/mixed anchor: objective outcomes did not beat control | Very small, procedural combination context; not a pure facial anti-aging monotherapy test |
| CHP-9 | 96 randomized/91 completed; vehicle and 0.002% retinol; 56 days [[4]](source_docs/chang-2025-cyclized-hexapeptide-9-trial.xml) | Unusually complete active- and vehicle-controlled modern study | The active comparator used 0.002% retinol—50× below the 0.1% formula used in the topic's comparator trial—and authors were manufacturer-affiliated |
| OS-01 | 60 women aged 60–90; finished formula versus commercial moisturizer; 12 weeks [[5]](source_docs/os01-peptide14-2025-rct-pubmed.xml) | Barrier/hydration signal in an older population | Not matched vehicle, proprietary formula, OneSkin-affiliated program; systemic-aging interpretation exploratory |
| PTPD-12 | 21-person randomized split-face control; eight weeks [[6]](source_docs/ptpd12-pigment-2025-rct-pubmed.xml) | Early direct pigment signal with melanin index and histology | Very small, single study, no comparison with established pigment care |
| 2026 SRMA | 19 RCTs/1,341 participants [[7]](source_docs/nukaly-2026-oral-topical-peptides-systematic-review.pdf) | Best field-level warning against extrapolating oral results to topical serums | Heterogeneous formulas/routes; only two high-quality topical studies |

## 3. Comparator quality changes the claim

| Comparator | Claim it can support | Claim it cannot support |
|---|---|---|
| Matched vehicle | Incremental effect of the test peptide/formula over its base | Superiority to sunscreen, retinoids, injectables, or devices |
| Commercial moisturizer | Finished formula versus another finished product | Peptide-specific causation; bases and supportive ingredients differ |
| Very-low-dose retinol | Performance versus that exact retinol formula | “Better than retinol” as a class or better than common 0.1–0.3% products |
| Post-procedure routine without peptide | Added value in that recovery stack | Standalone anti-aging efficacy |
| No control / before-after | Feasibility and signal detection | Causal efficacy |

## 4. Decision implications

| Goal | Evidence-led first peptide | How to frame the experiment |
|---|---|---|
| Fine lines / general low-irritation adjunct | Pal-KTTKS/Matrixyl-family formula | 12-week trial; keep sunscreen/retinoid schedule stable; expect modest change |
| Expression/periorbital lines | Argireline formula | Four-to-eight-week low-stakes adjunct; do not call it topical Botox |
| Barrier/hydration in older skin | OS-01 only if the finished formula and price fit | Treat as product-specific; compare with a good moisturizer, not “no care” |
| Pigment | PTPD-12 is watchlist, not first-line | Photoprotection and established pigment care lead |
| Copper/repair | GHK-Cu is optional and mechanistically interesting | Do not pay a large premium based on collagen/wound claims alone |
| New anti-aging technology | CHP-9 watchlist | Wait for independent replication against standard-strength retinol |

Use the [evidence-rating model](index.html#doc9) for ingredient-level prioritization and the [formula audit](index.html#doc11) for likely amount. This ledger is the separate **clinical-design check** those models were missing.

## 5. What would upgrade a peptide

A high-value future study would be:

- preregistered and independently run;
- at least 150–300 participants across multiple centers and phototypes;
- matched vehicle plus a meaningful standard comparator;
- assay-confirmed peptide identity, concentration, and end-of-study stability;
- 6–12 months with standardized objective wrinkle/pigment/barrier endpoints;
- adverse-event, adherence, and quality-of-life reporting;
- follow-up after stopping to test durability.

## Evidence gaps

- Independent replication is missing for nearly every named topical peptide.
- Many retail formulas use trademarked premixes, multiple peptides, retinoids, antioxidants, or humectants, preventing peptide-specific attribution.
- Most studies do not assay skin exposure, formula stability, or active concentration during use.
- Diverse phototypes, men, acne-prone skin, rosacea/eczema, and concomitant retinoid users are underrepresented.
- The ledger is intentionally selective: it captures the topic's decision-critical preserved sources, not every supplier study ever published.

## Sources

1. Robinson LR et al. Pal-KTTKS randomized split-face trial. [Local PubMed XML](source_docs/pal-kttks-2005-rct-pubmed.xml) - 93 participants, 3 ppm, 12 weeks, matched moisturizer.
2. Wang Y et al. Argireline randomized placebo trial. [Local PubMed XML](source_docs/argireline-2013-rct-pubmed.xml) - 60 participants, four weeks, clinical and replica endpoints.
3. Miller TR et al. GHK-Cu after CO2 laser randomized study. [Local PubMed XML](source_docs/ghk-cu-post-laser-2006-trial-pubmed.xml) - no objective wrinkle/erythema/skin-quality advantage in 13 completers.
4. Chang H et al. CHP-9 active- and vehicle-controlled trial. [Local full-text XML](source_docs/chang-2025-cyclized-hexapeptide-9-trial.xml) - 96 randomized, 0.002% CHP-9 versus 0.002% retinol and vehicle, 56 days.
5. OS-01/Peptide 14 randomized pilot. [Local PubMed XML](source_docs/os01-peptide14-2025-rct-pubmed.xml) - 60 older women, finished formula versus commercial moisturizer, 12 weeks.
6. PTPD-12 pigment trial. [Local PubMed XML](source_docs/ptpd12-pigment-2025-rct-pubmed.xml) - 21-person randomized split-face study, eight weeks.
7. Nukaly HY et al. *Oral and topical peptides for skin aging.* [Local PDF](source_docs/nukaly-2026-oral-topical-peptides-systematic-review.pdf) - 19 RCTs/1,341 participants; pooled benefit driven mainly by oral studies and few high-quality topical studies.
8. Kikuchi K et al. 0.1% stabilized retinol trial. [Local PubMed XML](source_docs/retinol-0.1-percent-2015-rct-pubmed.xml) - standard-strength comparator context for the CHP-9 interpretation.
