# Comparative study census and category rankings

*Compiled 2026-09-04. This is a reproducible evidence census and comparison map, not a prescription. It covers directly relevant human trials and systematic/regulatory records identifiable in PubMed, PMC, and official regulator sources through the cutoff, plus representative mechanism papers. “Every publicly available study” cannot literally be guaranteed: paywalls, indexing delays, language databases, unpublished negative studies, and changing product formulas create a hard boundary. A complete machine-readable row set is in [`data/ingredient_study_census_2026-09-04.csv`](data/ingredient_study_census_2026-09-04.csv).

## Bottom line

There is no single clinical leaderboard for body hyperpigmentation. The most defensible ranking separates **magnitude**, **confidence**, **body-site translation**, and **safety horizon**:

1. **Reference/finite medical lane:** hydroquinone (HQ), usually as a clinician-supervised triple combination (TCC) for a defined course. It has the deepest melasma evidence, but relapse, irritation, and exogenous ochronosis make it a finite tool rather than a lifetime body lotion. [[1]](https://pubmed.ncbi.nlm.nih.gov/36566490/)
2. **Best practical maintenance evidence:** topical tranexamic acid (TXA), azelaic acid 15–20%, niacinamide 4–5%, and Thiamidol/ITR. TXA and azelaic have independent comparative trials; niacinamide has the clearest direct axillary trial; Thiamidol has the strongest newer inhibitor program, including a 200-person vehicle-controlled trial. [[2]](https://pubmed.ncbi.nlm.nih.gov/37213446/)[[3]](https://pubmed.ncbi.nlm.nih.gov/23355788/)[[4]](https://pubmed.ncbi.nlm.nih.gov/41566113/)
3. **Credible alternatives:** cysteamine 5%, kojic acid, 4-n-butylresorcinol (4-BR/rucinol), and Melasyl/2-MNG. Their signal is real, but trials are generally smaller, shorter, facial, formulation-specific, or industry-linked. [[5]](https://pubmed.ncbi.nlm.nih.gov/39673630/)[[6]](https://pubmed.ncbi.nlm.nih.gov/40586974/)
4. **Adjunct/uncertain lane:** alpha-arbutin, N-acetyl glucosamine (NAG), vitamin C derivatives, phenylethyl resorcinol (SymWhite 377), hexylresorcinol, glutathione, resveratrol, licorice, and new peptides. They can be reasonable substitutions or formula components, but their isolated long-term body effect is less certain.
5. **Historical/toxic lane:** mercury salts and monobenzone can reduce pigment by enzyme inhibition plus tissue injury or melanocyte destruction. That explains their historical visual effect; it does not make them acceptable lighteners. They are excluded from every practical tier and routine.

## How the census was built

**Search frame.** PubMed/PMC and Europe PMC were queried for each ingredient and its synonyms (for example, `tranexamic acid AND melasma topical`, `isobutylamido thiazolyl resorcinol`, `2-MNG/Melasyl`, `rucinol/4-n-butylresorcinol`, `hexylresorcinol`, `phenylethyl resorcinol/SymWhite 377`, `cysteamine`, `alpha-arbutin`, `niacinamide`, `N-acetyl glucosamine`, `glutathione`, `kojic`, `ascorbic`, `retinoid`, `glycolic`, and `mercury skin lightening`). Systematic reviews were used to find older RCTs; primary records were retained whenever the abstract supplied design, sample, concentration, duration, and outcome. FDA, WHO, and EU SCCS records were used for regulatory and safety boundaries.

**Included.** Human randomized/controlled trials, split-face or evaluator-blinded comparisons, prospective formula studies, systematic reviews/meta-analyses, human enzyme/melanocyte assays, representative animal/in-vitro mechanism papers, and historical/regulatory toxicology records. **Excluded from efficacy ranking.** Pure marketing claims without a traceable design, oral/injectable “whitening” as if it were topical, and cosmetic products whose current INCI or concentration could not be verified.

**Evidence classes.**

| Code | Meaning | What it can support |
|---|---|---|
| **A** | Randomized/controlled human trial or systematic review with a relevant endpoint | A short-term efficacy estimate for the studied site/formula |
| **B** | Open-label, split-face, small or combination-formula human study | A plausible signal; not isolated-ingredient superiority |
| **C** | Human enzyme/cell assay, animal model, or mechanistic review | Where the molecule acts and whether the biology is plausible |
| **R/H** | Regulatory, toxicology, or historical record | Permitted/prohibited use and hazard; not a benefit claim |

The **confidence tier** below is therefore not the same as a predicted “lightening power” tier. An ingredient can have a dramatic assay result but only C/B clinical confidence.

## Category taxonomy: where each strategy acts

| Category | Biological job | Ingredients/strategies in the census | Typical evidence |
|---|---|---|---|
| **A. Stimulus and prevention** | Reduce UV/visible-light and repeated inflammation before pigment is made | Broad-spectrum sunscreen, clothing/shade, trigger control, hair/ingrown management | High-level prevention logic; body outcome is driver-dependent |
| **B. Upstream inflammatory/plasmin signaling** | Reduce keratinocyte–melanocyte signals that raise melanogenesis | TXA; azelaic acid; niacinamide; anti-inflammatory care | TXA/azelaic RCTs; mechanistic reviews |
| **C. Transcriptional melanocyte control** | Reduce MITF/TYR/TYRP1/DCT expression or melanocyte activation | Retinoids (indirect), phenylethyl resorcinol (p44/42–MITF), some botanicals | Mostly facial/combination or mechanism studies |
| **D. Direct melanogenic enzyme inhibition** | Inhibit tyrosinase or related TRP enzymes | HQ, Thiamidol/ITR, 4-BR/rucinol, kojic acid, arbutin, resorcinols, azelaic | Human assays plus small-to-moderate clinical programs |
| **E. Precursor chemistry / redox** | Intercept dopaquinone or reactive intermediates | Melasyl/2-MNG, cysteamine, vitamin C, glutathione, resveratrol | New 2-MNG non-inferiority data; mixed adjunct evidence |
| **F. Melanosome transfer** | Keep formed melanosomes from reaching keratinocytes | Niacinamide, NAG/niacinamide, retinoid/turnover support | Direct transfer assay and clinical formulas |
| **G. Turnover and optical removal** | Move pigmented keratinocytes out; smooth retained scale | Tretinoin/adapalene, glycolic/lactic acid, professional peels | PIH/AN reviews and procedure trials; irritation-limited |
| **H. Barrier and repair** | Reduce new inflammation and improve tolerability/adherence | Ceramides, urea, bland moisturizers, controlled routines | Supportive, not direct depigmentation |
| **I. Destructive/toxic historical** | Irreversibly injure melanocytes or enzymes | Mercury salts, monobenzone, chronic steroid mixtures | Historical/regulatory/toxicology; never a cosmetic recommendation |

## Comparative ranking: effect signal versus confidence

| Tier | Ingredient/strategy | Best human signal in the census | Mechanism category | Confidence for acquired body marks | Long-term interpretation |
|---|---|---|---|---|---|
| **Reference / finite S+** | HQ 2–4%; TCC (HQ+tretinoin+fluocinolone) | HQ monotherapy and combinations rank among the largest pooled effects; TCC had more “none/mild” ratings than HQ alone and about 53% relapse-free at six-month maintenance in one trial | D + G + C | **High for facial melasma; moderate for body extrapolation** | Course-limited, clinician guided; ochronosis/irritation and relapse prevent lifetime use |
| **S** | Topical TXA 2–5% | Meta-analysis pooled TXA SMD about −1.5; 5% TXA and 3% TXA were broadly comparable with HQ in small trials; combination TXA+NIA beat vehicle | B/E | **Moderate–high facial; moderate body extrapolation** | A useful maintenance signal lane; topical is not oral TXA |
| **S** | Azelaic acid 15–20% | Meta-analysis pooled SMD about −1.3; 20% azelaic improved phototypes IV–VI and was comparable with 5% TXA for acne PIH | B/D | **Moderate facial; moderate body extrapolation** | Strong anti-inflammatory/tyrosinase option if tolerated |
| **S− / A+** | Thiamidol/ITR 0.1–0.2% | 0.2% vehicle RCT: mMASI −36.1% vs −16.1% at 12 weeks; comparable with HQ4 in a 50-person evaluator-blinded study | D | **Moderate, newer and manufacturer-heavy** | Promising single inhibitor; no multi-year/large-area proof |
| **A** | Cysteamine 5% | Meta-analysis SMD −0.84 vs placebo; not significantly different from HQ4; 16-week cysteamine versus kojic showed small, nonsignificant separation | E/D | **Moderate facial; low body** | Short-contact or defined treatment phase; odor/irritation and adherence matter |
| **A** | 4-BR/rucinol 0.1–0.3% | Small split-face RCT and 0.3% open study improved melanin/MASI; 4-BR mechanistic advantage in human-tyrosinase and model assays | D | **Moderate mechanism, low–moderate clinical** | Choose as one direct inhibitor, not an extra layer |
| **A− / emerging** | Melasyl/2-MNG 0.5–1% | 0.5% serum was non-inferior to HQ4 over 84 days in 109 women when both used tinted SPF; newer skin-of-color and UV/HEV studies support signal | E | **Moderate but formula/company-specific** | Different precursor-trap lane; body evidence remains thin |
| **A−** | Niacinamide 4–5% | 4% axillary RCT improved colorimetry; only about 24% were good/excellent responders; 2% NIA + 2% TXA beat vehicle facially | F/B/H | **Moderate; best direct axillary anchor** | High-value maintenance/transfer lane; higher % is not proven better |
| **B+** | Kojic acid ≤1–2% | Meta-analysis pooled SMD about −0.9; 1% kojic and combinations improved facial pigmentation, but allergy risk exists | D/E | **Moderate facial, low body** | Substitution option; do not treat SCCS ceiling as an efficacy target |
| **B+** | Alpha-arbutin 0.5–2% | Small open or combination studies; 2025 alpha-arbutin+kojic pilot did not clearly beat TCC; SCCS body-lotion opinion is safety-focused | D | **Low–moderate** | Conservative adjunct; trace HQ/degradation and concentration matter |
| **B** | NAG 2% + niacinamide 4% | 202-person, 10-week formula beat vehicle; ingredient contribution is inseparable | F/H | **Low isolated; moderate formula** | Reasonable signal/transfer substitution |
| **B** | Hexylresorcinol 1% | 32-person randomized split-body study found no difference versus HQ2%, with good tolerance; NIA combination appeared synergistic in a formula study | D | **Low–moderate** | Interesting alternative; limited independent replication |
| **B−** | Phenylethyl resorcinol / SymWhite 377 | Small 12-week combination studies (retinaldehyde + 377 or multi-ingredient complex) improved mottled pigment; not isolated | C/D | **Low isolated** | Formula-dependent; no reason to stack with 4-BR/ITR |
| **B−** | Vitamin C (ascorbic/derivatives) | 5% ascorbic acid was less often subjectively successful than HQ4 but had fewer adverse effects; derivatives and peels vary | E/H | **Low–moderate** | Antioxidant/exposed-area adjunct, not the strongest stand-alone body inhibitor |
| **B−** | Glutathione (topical) | 2025 systematic review found topical 0.5% better than 0.1%/placebo in small studies; older review called evidence inconclusive | E/H | **Low** | Formula/short-term signal; no IV/injectable use |
| **C+** | Resveratrol, glabridin/liquiritin, botanicals | Mechanism/animal and small open or formula studies; human monotherapy evidence sparse | C/E | **Low** | Substitutions when better-defined lanes are unavailable |
| **C+ watchlist** | KT-939, PTPD-12, malassezin, oxyresveratrol | Strong assay or small early human signals; no mature independent comparative/long-term body trials | C/D/E | **Very low for routine decisions** | Watch, do not infer retail or lifetime safety |
| **X: prohibited/unsafe** | Mercury salts, monobenzone, unlabelled steroids/bleaches | Pigment reduction is confounded by irreversible enzyme inhibition, melanocyte loss, barrier injury, or systemic toxicity | I | **No acceptable efficacy tier** | Historical/regulatory warning only |

### What the pooled numbers actually mean

The 2023 systematic review/meta-analysis found 45 efficacy studies involving 2,359 participants. Pooled standardized mean differences were roughly HQ monotherapy −1.3, HQ combinations −1.4, cysteamine −1.6, TXA −1.5, azelaic acid −1.3, and kojic acid −0.9. Irritation incidence was approximately 50.9% for HQ combinations, 42.2% cysteamine, 18.7% azelaic acid, 5.3% kojic acid, and 0.8% TXA. These estimates mix sites, formulas, comparators, and durations and are not a product-to-product league table. [[1]](https://pubmed.ncbi.nlm.nih.gov/36566490/)

The wider 2019 topical-RCT review located 35 randomized studies across azelaic acid, cysteamine, HQ, niacinamide, TXA, 4-BR, glycolic acid, kojic acid, ascorbic acid, ellagic acid, and arbutin. A 2023 review screened 174 controlled trials and gave the strongest grades to HQ/TCC, sunscreen, kojic acid, and azelaic acid, while noting that evidence for vitamin C, resorcinols, and topical TXA needed strengthening. [[7]](https://pubmed.ncbi.nlm.nih.gov/31741361/)[[8]](https://pubmed.ncbi.nlm.nih.gov/38099013/)

## Study census: representative human and mechanistic records

The table is intentionally explicit about design, site, and what cannot be inferred. The companion CSV contains the same fields for filtering and future updates.

| Ingredient/strategy | Study (year) | Design / sample | Protocol and site | Main result | Evidence class and translation |
|---|---|---|---|---|---|
| Topical depigmenters overall | Chang et al. 2023 [[1]](https://pubmed.ncbi.nlm.nih.gov/36566490/) | Systematic review/meta-analysis; 45 studies, 2,359 participants | Mostly facial melasma/PIH; mixed durations | Pooled SMDs and irritation estimates above | **A**; useful class signal, not product ranking |
| Topical RCT landscape | Austin et al. 2019 [[7]](https://pubmed.ncbi.nlm.nih.gov/31741361/) | Systematic review; 35 RCTs | Azelaic, HQ, cysteamine, NIA, TXA, 4-BR, acids, kojic, ascorbic, arbutin | Heterogeneous RCT base | **A**; identifies evidence gaps |
| Comprehensive topical/systemic review | 2023 review [[8]](https://pubmed.ncbi.nlm.nih.gov/38099013/) | 174 controlled trials screened | Melasma/PIH | HQ/TCC, sunscreen, kojic, azelaic graded strongest | **A**; treatment hierarchy, not body efficacy |
| TXA, all routes | 2024 meta-analysis [[9]](https://pubmed.ncbi.nlm.nih.gov/38843906/) | 22 studies, 1,280 participants | Oral/topical/injection, 8 weeks–2 years | Significant MASI/MI improvements; high heterogeneity | **A**; route-specific safety must remain separate |
| TXA, route comparison | 2024 network/meta-analysis [[10]](https://pubmed.ncbi.nlm.nih.gov/38283017/) | 28 RCTs | Injection/microneedling, oral, topical | Invasive routes generally larger effects than topical | **A**; cannot convert injection/oral to home topical dosing |
| TXA 5% vs HQ 3% | 2019 RCT [[11]](https://pubmed.ncbi.nlm.nih.gov/31057273/) | 100 analyzed; 12 weeks | Facial melasma | MASI reduction 27% TXA vs 26.7% HQ; nonsignificant; TXA satisfaction higher | **A**; facial, short-term |
| TXA 3% vs HQ 4% | 2024 double-blind split-face [[12]](https://pubmed.ncbi.nlm.nih.gov/38918942/) | 20; 8 weeks | Facial melasma | Both improved; no significant difference | **A**; small/facial |
| TXA 5% vs azelaic 20% | 2023 RCT [[13]](https://pubmed.ncbi.nlm.nih.gov/37213446/) | 60 completers; 12 weeks | Acne PIH | Both improved; more early AEs with azelaic | **A**; strongest direct comparator for these two topical lanes |
| TXA 2% + NIA 2% | 2013 vehicle RCT [[14]](https://pubmed.ncbi.nlm.nih.gov/24033822/) | Facial randomized vehicle-controlled | 8 weeks | Combination outperformed vehicle | **A**; cannot isolate ingredients |
| TXA + NIA + arbutin formula vs HQ | 2019 split-face [[15]](https://pubmed.ncbi.nlm.nih.gov/31664751/) | 44 healthy subjects | 3% or 2% TXA combinations vs HQ4; 4 weeks | All improved; no differences | **A/B**; healthy-site short study |
| NIA 4% axilla | Castanedo-Cazares et al. 2013 [[3]](https://pubmed.ncbi.nlm.nih.gov/23355788/) | 24 women, phototypes III–V | 4% NIA vs 0.05% desonide/placebo; axilla; 9 weeks | Colorimetry improved; good/excellent response ~24% | **A**; best direct body topical anchor, modest responder rate |
| NIA 5% vs HQ 4% | 2011 randomized study [[16]](https://pubmed.ncbi.nlm.nih.gov/21822427/) | 27; 8 weeks | Facial melasma | Good/excellent 44% NIA vs 55% HQ; AEs 18% vs 29% | **A**; facial, small |
| NIA transfer mechanism | 2002 clinical/mechanism study [[17]](https://pubmed.ncbi.nlm.nih.gov/12100180/) | Coculture + human studies | 2% NIA + sunscreen / 5% moisturizer | 35–68% inhibition of melanosome transfer in coculture; four-week lightening | **A/C**; mechanism plus short clinical signal |
| NAG 2% + NIA 4% | Kimball et al. 2009 [[18]](https://pubmed.ncbi.nlm.nih.gov/19845667/) | 202; 10 weeks | Facial hyperpigmentation | Significant reduction vs vehicle | **A**; combination attribution limit |
| Azelaic acid 20% | Lowe et al. [[19]](https://pubmed.ncbi.nlm.nih.gov/9829446/) | Randomized vehicle-controlled; 24 weeks | Facial hyperpigmentation, phototypes IV–VI | Significant improvement | **A**; body extrapolation |
| HQ + tretinoin + fluocinolone (TCC) | 2008 Asian trial [[20]](https://pubmed.ncbi.nlm.nih.gov/18616780/) | About 249; 8 weeks | Facial melasma | TCC had 64.2% none/mild vs 39.4% HQ; AEs 48.8% vs 13.7% | **A**; finite Rx, not long-term body use |
| TCC maintenance | 2011 RCT [[21]](https://pubmed.ncbi.nlm.nih.gov/21623930/) | 242 entering six-month maintenance | Daily induction then reduced schedule | About 53% relapse-free at six months; twice-weekly tended better | **A**; relapse remains common |
| TCC open-label | 2010 study [[22]](https://pubmed.ncbi.nlm.nih.gov/20398959/) | 70; 24 weeks | 12 weeks daily then reduced/continued | Relapse common; AEs ~53% | **B**; maintenance ceiling |
| HQ community study | 2006 open-label [[23]](https://pubmed.ncbi.nlm.nih.gov/16610738/) | 1,290; 8 weeks | Facial melasma | 75% moderate/marked/almost clear/clear | **B**; uncontrolled |
| Cysteamine 5% | 2014 double-blind placebo RCT [[24]](https://pubmed.ncbi.nlm.nih.gov/25251767/) | 50; four months | Facial melasma | Better than placebo | **A**; odor/irritation and facial-only |
| Cysteamine meta-analysis | 2024 [[5]](https://pubmed.ncbi.nlm.nih.gov/39673630/) | 7 RCTs | Melasma | SMD −0.84 vs placebo; vs HQ4 nonsignificant | **A**; clarifies moderate signal |
| Cysteamine vs HQ + ascorbic | 2022 RCT [[25]](https://pubmed.ncbi.nlm.nih.gov/35510765/) | 65/80 completed; four months | Facial melasma | mMASI decrease similar; melanin index favored HQ combo | **A**; short, facial |
| Cysteamine vs TXA mesotherapy | 2020 RCT [[26]](https://pubmed.ncbi.nlm.nih.gov/32879998/) | 54; four months | Facial melasma | No significant difference; fewer complications with topical cysteamine | **A**; comparator includes invasive route |
| Cysteamine + ectoine vs HQ + ectoine | 2024 trial [[27]](https://pubmed.ncbi.nlm.nih.gov/40127492/) | Controlled clinical trial | Facial melasma | Both improved; cysteamine slightly greater, nonsignificant | **A/B**; small and formula-specific |
| Kojic 1% | 2013 single-blind RCT [[28]](https://pubmed.ncbi.nlm.nih.gov/23918998/) | 80; 12 weeks | Facial melasma | Kojic legitimate; KA+HQ best | **A**; combination attribution |
| Cysteamine 5% vs kojic 2% | 2025 trial [[29]](https://pubmed.ncbi.nlm.nih.gov/40296942/) | 72 Indian women; 16 weeks | Facial melasma | mMASI −12.25% vs −10%; no significant difference; no AEs reported | **A**; small and short |
| Alpha-arbutin 5% + kojic 2% vs TCC | 2025 split-face pilot [[30]](https://pubmed.ncbi.nlm.nih.gov/39555866/) | 30; 12 weeks + four-week follow-up | Facial melasma | mMASI/MI differences nonsignificant; TCC PGA better, more recurrence/erythema | **A/B**; concentrations not a body-lotion target |
| Alpha-arbutin/herbal formula | 2019 RCT [[31]](https://pubmed.ncbi.nlm.nih.gov/30980618/) | 90; 12 weeks | Facial melasma | Herbal > arbutin > placebo; attribution/formula limits | **A/B** |
| Thiamidol human-tyrosinase screen | Mann et al. 2018 [[32]](https://pubmed.ncbi.nlm.nih.gov/29427586/) | Screen ~50,000 compounds; cell model | Enzyme/cultured melanocytes | ITR hTYR IC50 ~1.1 μM; suppression reversible after withdrawal | **C**; potency and reversibility, not body efficacy |
| Thiamidol vs HQ4 | 2021 evaluator-blinded RCT [[33]](https://pubmed.ncbi.nlm.nih.gov/33988887/) | 50; 90 days | Facial melasma | Comparable improvement; two ITR contact dermatitis cases | **A**; small |
| Thiamidol 0.2% vehicle RCT | 2026 double-blind RCT [[4]](https://pubmed.ncbi.nlm.nih.gov/41566113/) | 200/196; 12 weeks | Facial melasma | mMASI −36.1% vs −16.1% at week 12; mixed secondary endpoints | **A**; newest controlled signal, facial |
| Thiamidol UVB prevention | 2020 controlled study [[34]](https://pubmed.ncbi.nlm.nih.gov/32757247/) | 30; three-week pre-treatment + UVB | Human UV-induced pigmentation | Earlier return toward baseline; no significant AEs | **A/C**; prevention, not treatment |
| Thiamidol systematic review | 2024 [[35]](https://pubmed.ncbi.nlm.nih.gov/39496126/) | 14 clinical studies | Mostly 0.1–0.2% twice daily, 12–24 weeks | Limited but consistent short-term improvement | **A**; manufacturer-heavy |
| Thiamidol skin-of-color case series | 2025 [[36]](https://pubmed.ncbi.nlm.nih.gov/40847672/) | 10 Indian women, FST III–V | 0.2% twice daily, 12 weeks | mMASI −34.4%; no control | **B** |
| 4-BR 0.1% | 2010 split-face RCT [[37]](https://pubmed.ncbi.nlm.nih.gov/20548876/) | 20; 8 weeks | Facial melasma | Significant vs vehicle at weeks 4/8; mild transient AEs | **A**; small |
| 4-BR 0.3% | 2016 open study [[38]](https://pubmed.ncbi.nlm.nih.gov/26855596/) | 52 Indian participants; 8 weeks BID | Facial melasma | MASI 14.73 → 6.48; no AEs reported | **B**; no control |
| Rucinol 0.3% | 2007 split-face RCT [[39]](https://pubmed.ncbi.nlm.nih.gov/17388924/) | 32; 12 weeks + optional follow-up | Facial melasma | Significant vs vehicle, good tolerance | **A**; small |
| 4-BR/resveratrol liposomal | 2019 formula study [[40]](https://pubmed.ncbi.nlm.nih.gov/31347777/) | 21; four weeks | Facial hyperpigmentation | MI improved; 52.3% moderate/significant at week 4 | **B**; formula-specific |
| Hexylresorcinol 1% vs HQ2% | 2023 randomized split-body [[41]](https://pubmed.ncbi.nlm.nih.gov/36502500/) | 32 healthy women; 12 weeks | Face/hands | No difference; HR well tolerated | **A**; healthy/short |
| Hexylresorcinol + NIA | 2022 split-face/formula study [[42]](https://pubmed.ncbi.nlm.nih.gov/34958693/) | Chinese split-face; 12 weeks + in-vitro | Facial pigmentation | Combination appeared synergistic vs NIA alone | **B/C**; exact n/formula attribution |
| Phenylethyl resorcinol | 2015 combination study [[43]](https://pubmed.ncbi.nlm.nih.gov/25871836/) | 20; 12 weeks + follow-up | Solar lentigines face/hands | Retinaldehyde + 377 + antioxidant improved lesions | **B**; not isolated |
| Phenylethyl resorcinol complex | 2013 study [[44]](https://pubmed.ncbi.nlm.nih.gov/23438137/) | 80; 12 weeks | Facial mottled hyperpigmentation | About 32% reduction; 57% moderate response | **B**; multi-ingredient |
| Melasyl/2-MNG vs HQ4 | 2025 randomized non-inferiority [[45]](https://pubmed.ncbi.nlm.nih.gov/40586974/) | 109 women; 84 days | Facial melasma; tinted SPF in both arms | 0.5% 2-MNG met non-inferiority margin; local reactions 6% vs 21.4% at day 28 | **A**; product/formula and company limits |
| Melasyl skin-of-color serum | 2025 open study [[46]](https://pmc.ncbi.nlm.nih.gov/articles/PMC12710987/) | 60 women FST IV–VI; 12 weeks | Facial dyschromia; serum + SPF | Brightness/radiance improved week 2; dyschromia week 4 | **B**; uncontrolled |
| Melasyl HEV prevention | 2025 controlled trials [[47]](https://pubmed.ncbi.nlm.nih.gov/41142247/) | 58 total FST III–IV | 0.5/1% 2-MNG vs vehicle; HEV | Reduced HEV-induced pigmentation; 7% ascorbic acid did not | **A/C**; prevention model |
| KT-939 | 2025 research paper [[48]](https://pubmed.ncbi.nlm.nih.gov/41159291/) | hTYR/cell studies + 0.2% lotion, 28-day single-center study | Human enzyme, melanocytes, healthy sensitive skin | hTYR IC50 0.07 μM; melanocyte IC50 0.36 μM; reversible washout; early clinical signal | **B/C**; no mature independent RCT or long-term |
| PTPD-12 peptide | 2025 split-face [[49]](https://pubmed.ncbi.nlm.nih.gov/41044809/) | 21; 8 weeks | Facial pigmentation | MI decrease 22.23, p<0.0001; autophagy claim | **B/C**; novel, short |
| Malassezin 0.75% vs HQ4 | 2026 split-face [[50]](https://pubmed.ncbi.nlm.nih.gov/41493251/) | 20; 12 weeks | Facial melasma | Both improved; no between-side difference; mild AEs | **A/B**; tiny study |
| Vitamin C 5% vs HQ4 | 2004 split-face [[51]](https://pubmed.ncbi.nlm.nih.gov/15304189/) | 16; 16 weeks | Facial melasma | HQ subjectively 93% vs ascorbic 62.5%; colorimetry no difference; AEs 68.7% vs 6.2% | **A**; old/small |
| Topical glutathione | 2025 systematic review [[52]](https://pubmed.ncbi.nlm.nih.gov/39444151/) | 5 topical RCTs + one open oral | Mostly facial/body exposed areas | 0.5% topical > 0.1%/placebo in small studies; bias mixed | **A/B**; not IV/injectable |
| Liquiritin | 2000 split-face [[53]](https://pubmed.ncbi.nlm.nih.gov/10809983/) | 20; four weeks BID | Facial melasma | Topical liquiritin improved versus vehicle | **B**; small/old |
| Glabridin/andrographolide/apolactoferrin | 2019 open-label [[54]](https://pubmed.ncbi.nlm.nih.gov/31541594/) | 40; six months | Facial melasma | Endpoints improved; three mild xerosis cases | **B**; uncontrolled formula |
| Mercury chloride mechanism | 2020 laboratory study [[55]](https://pubmed.ncbi.nlm.nih.gov/32210794/) | Enzyme study | Human tyrosinase | HgCl2 IC50 29.97 μM monophenolase/77.93 μM diphenolase; irreversible noncompetitive inhibition at histidines | **C/R**; explains effect, not acceptability |
| Mercury toxicology | 2012 review [[56]](https://pubmed.ncbi.nlm.nih.gov/22070559/) | 118 citations; 31 relevant reports | Mercury salts in lighteners | Dermal absorption, kidney/CNS/GI toxicity, household contamination | **R/H**; safety exclusion |

## Enzyme potency is not a clinical ranking

The 2025 KT-939 comparison reported the following **within one human-tyrosinase assay**:

| Test compound | Reported IC50 |
|---|---:|
| KT-939 | **0.07 μM** |
| Thiamidol | **0.33 μM** |
| Resveratrol | **6.04 μM** |
| 4-n-butylresorcinol | **7.09 μM** |
| Phenylethyl resorcinol | **21.28 μM** |

That is an approximately 4–5-fold KT-939 advantage over Thiamidol **in that assay**, not proof of 4–5-fold better skin results. The earlier ITR screen reported about 1.1 μM for Thiamidol and different values for 4-BR, because assay substrate, enzyme preparation, exposure time, and calculation can differ. A molecule must also reach the relevant melanocyte, remain stable in a vehicle, avoid rapid metabolism, and improve a patient-visible endpoint. The practical order therefore weights controlled human trials above isolated IC50 values. [[32]](https://pubmed.ncbi.nlm.nih.gov/29427586/)[[48]](https://pubmed.ncbi.nlm.nih.gov/41159291/)

## Dated product/value crosswalk

These are products surfaced by the pasted research and the 2026-09-02/04 U.S. snapshot. They are **shopping examples, not clinical trial arms**. A product earns a value tier for transparent ingredients, site fit, price, and evidence translation—not for a brand's marketing claim.

| Value tier | Product examples | Category/job | Why it ranks here | Limits |
|---|---|---|---|---|
| **S value** | Good Molecules Discoloration Correcting Body Treatment; The Ordinary Niacinamide 5% Face & Body | NIA/TXA signal-transfer lane | Body positioning or transparent 5% NIA; inexpensive, easy to use as one signal lane | GM uses LHA and a proprietary TXA derivative; no head-to-head body RCT |
| **S value** | Eucerin Radiant Tone Dark Spot Corrector Body Lotion | Thiamidol direct inhibitor | Body-specific lotion with Thiamidol/HA/Licochalcone-A; strongest value among domestic body inhibitor examples | Exact active percentage is not exposed; short facial/body marketing evidence; do not equate with 0.2% RCT concentration |
| **A site-fit** | Bioderma Pigmentbio Sensitive Areas; Eucerin Anti-Pigment Sensitive Areas Body Serum (international) | Fold/axilla external skin | Designed for sensitive/friction-prone external areas | Percentages and independent RCT evidence are limited; import/seller issues for Eucerin |
| **A site-fit** | La Roche-Posay Mela B3 Dual Body Discoloration Treatment | Melasyl + NIA + LHA body lane | Body-specific 2-MNG/Melasyl positioning and accessible U.S. listing | Alcohol/fragrance/LHA and short consumer study; no proof of superiority over Eucerin |
| **A face-to-body extrapolation** | Anua Azelaic Acid 10%; The Ordinary Azelaic Acid 10% | Azelaic anti-inflammatory/direct lane | Widely available and transparent 10% category options | Face formulas; 15–20% has stronger drug evidence; use body extrapolation only |
| **A formula** | COSRX Alpha-Arbutin 2; Minimalist Alpha-Arbutin 2 (also lists 4-BR) | Arbutin ± 4-BR direct lane | Exact active disclosure and easy comparison; Minimalist gives a resorcinol variant | Face serums, small bottles, no proof the blend beats a single direct inhibitor |
| **B formula** | Numbuzin No.5 Glutathione/TXA; Naturium TXA 5% | TXA + adjuncts | Coherent combination formulas with transparent TXA positioning | Small/face-oriented; avoid duplicating another TXA/NIA product initially |
| **B formula** | Admire My Skin Ultra Potent Brightening Serum (Synovea HR); SKINTIFIC 377 | Hexylresorcinol or 377 | Gives access to lower-priority resorcinol categories | Face formulas and combination acids; lower independent evidence |
| **A barrier/SPF** | Eucerin Advanced Repair/Smoothing Repair; Eucerin Daily Hydration SPF 30 or SPF 50 | H/ A prevention | Barrier and photoprotection prevent new pigment and improve adherence | Not direct inhibitors; sunscreen must be applied generously/reapplied |
| **B turnover** | AmLactin 12% lactic acid; The Ordinary Glycolic 7%; adapalene 0.1% | G turnover | Useful when roughness, KP, acne, or ingrowns are drivers | Off-label body extrapolation or acne label; do not stack turnover families |

Official examples and prices are preserved in the [buy-now product/value tier list](index.html#doc7), while the pathway visualizer shows which biological lane each example represents. Product stock, formula, seller, and price can change; re-check the official or authorized retailer page before purchase.

### Products explicitly surfaced by the pasted finale

The pasted Chemist Confessions reconstruction names six “radar” products and then expands the shopping list with lower-cost and regional examples. The table below keeps that provenance separate from the clinical census. **A product page, consumer-use test, or an ingredient appearing high in an INCI list is not the same as an independent randomized trial of the finished product.** Prices are the page/attachment snapshots available on 2026-09-04 and should be rechecked before buying.

| Product (official/current page where available) | Snapshot and declared actives | Pathway category | How to use the evidence | Value/status |
|---|---|---|---|---|
| [Eucerin Radiant Tone Dual Serum](https://www.eucerinus.com/products/radiant-tone/dual-serum) | 1 fl oz; Thiamidol + hyaluronic acid; official page reports a 98% “improved complexion” home-use claim; price is retailer-dependent | **D. Direct TYR inhibitor** | Thiamidol itself has controlled clinical evidence, but this page does not disclose the percentage and is labeled for face/neck. Do not assume it matches the 0.2% trial concentration or that it is a body product. | **A evidence-to-price when available; current** |
| [Anua Niacinamide 10 TXA 4 Serum](https://anua.com/products/niacinamide-10-txa-4-serum-2?_pos=2&_psq=Serum&_ss=e&_v=1.0) | 30 ml; $24 page price; 10% niacinamide + 4% TXA + 2% arbutin; official directions mention elbows/knees/hands | **B/F/D. Upstream + transfer + direct** | The concentrations are transparent and sit in clinically interesting ranges, but the finished formula is not the same as a controlled TXA/NIA trial. Face formula; body use is extrapolation. | **A value; current** |
| [COSRX The Alpha-Arbutin 2 Discoloration Care Serum](https://www.cosrx.com/products/the-alpha-arbutin-2-discoloration-care-serum?_pos=6&_sid=56988b0d8&_ss=r&externalId=2L5lB) | 50 ml; $25; alpha-arbutin 2% with TXA, niacinamide, NAG, ferulic acid and glutathione; manufacturer page reports 4-week reductions of 22.31% in dark-spot appearance and 20.47% in melanin | **B/F/D/E. Multi-target formula** | The result is a company-sponsored P&K product test, not an independent body RCT; it is useful as a formula snapshot, not proof that every ingredient contributes equally. | **A value; current** |
| [Anua Azelaic Acid 10 Hyaluron Serum](https://anua.com/products/azelaic-acid-10-hyaluron-redness-soothing-serum?shpxid=69b2282e-5b36-4a83-ab0f-41bba1a3572a) | 30 ml; $23 sale/$24 regular; 10% azelaic acid with cica/HA; directions start at 1–2 times weekly and increase gradually | **B/D. Inflammation + TYR** | Azelaic acid’s better melasma evidence is at 15–20%; this 10% cosmetic serum is a reasonable lower-dose trial and a redness/blemish option, not an equivalent to prescription 20%. | **A− value; current** |
| [Minimalist Alpha Arbutin 2% Face Serum](https://beminimalist.co/collections/face-serum/products/alpha-arbutin-2) | 30 ml; ₹495 page price; 2% alpha-arbutin + ferulic acid + 4-butylresorcinol (percentage not disclosed) | **D/E. Direct TYR + antioxidant** | The brand’s 3-D skin-model and consumer claims are not a peer-reviewed human RCT; the undisclosed 4-BR dose prevents comparison with 0.1–0.3% studies. | **A value for experimentation; current** |
| [The Ordinary Alpha Arbutin 2% + HA](https://theordinary.com/en-us/alpha-arbutin-2-ha-serum-100401.html) | Water-based 2% alpha-arbutin + HA; attachment snapshot ≈$11.50; face serum | **D. Direct TYR** | Transparent arbutin concentration, but the clinical body evidence is thin and this is not a body-lotion study. | **S/A value; current** |
| [Numbuzin No.5 Glutathione TXA Advanced Dark Spot Ampoule](https://us.numbuzin.com/products/no-5-glutathione-txa-advanced-dark-spot-ampoule-concentrate) | 10 g; $24.70 sale/$26 regular; glutathione + TXA + niacinamide; no percentages; sulfur-like odor noted on page | **B/E. Upstream + redox** | A coherent adjunct formula, but unknown concentrations and small topical glutathione literature make it weaker than a transparent 3–5% TXA product. | **B value; current** |
| [La Roche-Posay Mela B3 Dark Spot Serum](https://www.laroche-posay.us/our-products/face/face-serum/mela-b3-dark-spot-serum-with-melasyl-niacinamide-3337875890021.html) | 30 ml $44.99 / 50 ml $60.99; Melasyl + 10% niacinamide; face serum | **E/F. Precursor trap + transfer** | Melasyl/2-MNG now has a small non-inferiority study and prevention data, but the product’s marketing/consumer studies do not isolate its dose or prove body superiority. | **A formula interest; current** |
| [Admire My Skin Ultra Potent Brightening Serum](https://www.admiremyskin.com/products/melasma-treatment-cream) | $17.99 sale/$25; 1% Synovea HR (hexylresorcinol) plus kojic, azelaic, lactic, salicylic and vitamin C | **B/D/G. Direct + turnover-heavy formula** | This is a multi-acid formula, not a clean hexylresorcinol experiment; the acid load can create the inflammation it is meant to reduce. | **B+/A− formula value; current** |
| [SKINTIFIC 377 Dark Spot Serum](https://us.skintific.com/products/377-dark-spot-serum) | US page lists 20/30 ml variants (20 ml shown at $9.90); brand describes 377 as phenylethyl resorcinol; concentration is not disclosed | **C/D. Resorcinol/MITF-adjacent** | Treat “377” as a brand/active name, not a known dose. The page’s variant/INCI presentation should be checked against the package before relying on it. | **B value; current, dose uncertain** |
| [Paula’s Choice 25% Vitamin C + Glutathione Clinical Serum](https://www.paulaschoice.com/25pct-vitamin-c-and-glutathione-clinical-serum/1490-1490.html) | 25% vitamin C + glutathione; one of the finale’s six radar products | **E. Redox** | Paula’s Choice help-center material marks the product as discontinued; the legacy page may remain indexed, so it is **not a buy-now recommendation**. | **Historical/discontinued** |

The pasted research also compares regional quasi-drug or mass-market examples—**HAKU Melanofocus IV (TXA + 4MSK), ONE BY KOSÉ Melanoshot P (kojic acid), POLA White Shot SXS (4-n-butylresorcinol/Rucinol), SK-II GenOptics, DermaFactory 3% TXA, and NIVEA Luminous630/Thiamidol-range products**. Their Japanese/Indian/Korean price and ranking snapshots are market context, not equivalent evidence: formulas, legal categories, seller authenticity, and availability differ by country. They are retained here so the source research is not silently narrowed to U.S. products; the clinical comparisons remain the peer-reviewed rows above.

**Shopping rule from the evidence map:** for a current OTC purchase, choose **one transparent upstream/transfer formula (for example Anua TXA/NIA), one direct inhibitor with a defined or brand-verified active (for example Eucerin Thiamidol or a 4-BR product), and one prevention/barrier step**. A second product containing the same TXA, niacinamide, arbutin, or acids adds label count more reliably than it adds proven pigment reduction. The [pathway visualizer](melanin_pathway_visualizer.html) is the fastest way to see those overlaps.

## Maximal mechanistic thought experiment (not a treatment protocol)

The user's “maximal maximal” idea is useful as a **coverage model**: if each product acted at a different node, would the map cover more of the pathway? It is not proof that simultaneous use is better, and no study has tested this full stack. The only defensible practical routine remains the phased plan in [Maximal routine and site-specific protocols](index.html#doc4) and the [routine composer](maximal_routine_composer.html).

| Lane | Theoretical ingredient/product examples | Target node | What is genuinely supported | Why adding more is not automatically better |
|---|---|---|---|---|
| 1. Prevent stimulus | Broad-spectrum SPF, shade/clothing, trigger and shaving control | UV/visible light; repeated inflammation | Prevention and driver control are foundational | No lightener can outcompete a continuing trigger |
| 2. Upstream signal | Topical TXA (or a transparent TXA product) | Plasminogen/plasmin → PGE2/ET-1/SCF signaling | Facial RCTs and meta-analyses | Oral/injected TXA is a different risk category; duplicate TXA blends add complexity |
| 3. Transfer | NIA 4–5% or NAG+NIA | PAR-2/melanosome transfer to keratinocytes | Direct transfer mechanism; axillary NIA trial | More NIA is not proven to improve body results; same lane can be redundant |
| 4. Inflammation/direct | Azelaic 10–20% | Inflammation plus mitochondrial/TYR effects | RCT/meta-analysis support | It can be the direct/anti-inflammatory anchor; stacking acids raises trigger risk |
| 5. Direct human-TYR | **Choose one**: Thiamidol, 4-BR, or another defined resorcinol | TYR (and TRP-1 for some resorcinols) | Human assays and short clinical programs | No head-to-head body trial; multiple inhibitors do not equal additive effect |
| 6. Precursor trap | Melasyl/2-MNG | Dopaquinone/reactive melanin precursors | Non-inferiority facial study and prevention models | Different node is interesting, but combining with a direct inhibitor is untested |
| 7. Thiol/redox | Cysteamine or vitamin C/glutathione | Quinones/redox balance | Cysteamine RCTs; vitamin C/glutathione smaller evidence | Cysteamine odor/irritation and redox interactions limit practical use |
| 8. Turnover | Tretinoin/adapalene **or** glycolic/lactic acid | Keratinocyte turnover/retention | PIH/AN and peel evidence | Turnover is not a second inhibitor; irritation can create more pigment |
| 9. Repair | Ceramide/urea/petrolatum moisturizer | Barrier and recovery | Supports adherence and reduces trigger load | Supportive, not a “lightening” ingredient |

### Safe interpretation of the thought experiment

- The map can contain **all nine categories**, but a real week should choose one product per necessary lane and add only one change at a time. The route that covers the most molecular labels can still produce less net improvement if it causes dermatitis.
- Mercury, monobenzone, chronic steroid mixtures, unlabeled bleaches, and injectable/oral glutathione remain outside the map's practical branch. “Ignore irritation and long-term safety for now” cannot override permanent depigmentation, systemic toxicity, or an unapproved indication.
- The visualizer intentionally shows a red historical mercury node only after the reader requests it; it never places mercury in the selectable practical stack.

## Evidence gaps that keep the ranking provisional

1. There is no independent, multi-year, head-to-head body trial comparing TXA, azelaic acid, niacinamide, Thiamidol, Melasyl, 4-BR, cysteamine, or arbutin on axillae, inner thighs, elbows, or large body areas.
2. Many proprietary-active studies are facial, short, single-arm, manufacturer-linked, or combination formulas. A positive product study cannot isolate the named ingredient.
3. Body skin varies in thickness, occlusion, shaving trauma, microbiome, and surface area. Facial percentages and vehicles cannot be copied without a body-site safety assumption.
4. Long-term daily data beyond six to twelve months are sparse; relapse after reducing frequency is rarely measured.
5. IC50 values from different assays are not commensurate, and in-vitro “no cytotoxicity” does not establish long-term human safety.
6. Retail active percentages and vehicles are frequently undisclosed. The product tier is therefore a dated value snapshot, not a claim of equivalent dose.

## Source-log trail

The [verbose source/resource recovery log](source_docs/research_resource_log_2026-09-04.txt) is the recovery notebook for this census: **S01–S68** cover the representative studies, mechanism/regulatory records, and product pages; **S86** preserves the machine-readable CSV index; and **S87–S90** preserve the user-supplied context that prompted the update. What this section found: rank magnitude, confidence, body translation, and safety horizon separately; retain the nine-lane model only as a mechanistic thought experiment; and do not double-count the duplicate Melasyl/HQ and TXA/azelaic bibliography entries. Each census row can be traced back to its stable ID, URL status, local archive path, and limitation in the log.

## Sources

1. [Chang et al. 2023 topical depigmenting meta-analysis](https://pubmed.ncbi.nlm.nih.gov/36566490/)
2. [Alirezaei et al. topical TXA vs azelaic acid](https://pubmed.ncbi.nlm.nih.gov/37213446/)
3. [Castanedo-Cazares et al. axillary niacinamide RCT](https://pubmed.ncbi.nlm.nih.gov/23355788/)
4. [2026 Thiamidol vehicle-controlled RCT](https://pubmed.ncbi.nlm.nih.gov/41566113/)
5. [Cysteamine meta-analysis](https://pubmed.ncbi.nlm.nih.gov/39673630/)
6. [Melasyl/2-MNG vs hydroquinone non-inferiority study](https://pubmed.ncbi.nlm.nih.gov/40586974/)
7. [Austin et al. topical melasma RCT systematic review](https://pubmed.ncbi.nlm.nih.gov/31741361/)
8. [2023 systematic review of topical/systemic melasma treatments](https://pubmed.ncbi.nlm.nih.gov/38099013/)
9. [2024 TXA efficacy meta-analysis](https://pubmed.ncbi.nlm.nih.gov/38843906/)
10. [2024 TXA route comparison meta-analysis](https://pubmed.ncbi.nlm.nih.gov/38283017/)
11. [5% TXA vs 3% hydroquinone](https://pubmed.ncbi.nlm.nih.gov/31057273/)
12. [3% TXA vs 4% hydroquinone split-face trial](https://pubmed.ncbi.nlm.nih.gov/38918942/)
13. [5% TXA vs 20% azelaic acid](https://pubmed.ncbi.nlm.nih.gov/37213446/)
14. [2% TXA + 2% niacinamide vehicle RCT](https://pubmed.ncbi.nlm.nih.gov/24033822/)
15. [TXA/niacinamide/arbutin combinations vs HQ](https://pubmed.ncbi.nlm.nih.gov/31664751/)
16. [4% niacinamide vs 4% hydroquinone](https://pubmed.ncbi.nlm.nih.gov/21822427/)
17. [Niacinamide melanosome-transfer study](https://pubmed.ncbi.nlm.nih.gov/12100180/)
18. [NAG + niacinamide randomized study](https://pubmed.ncbi.nlm.nih.gov/19845667/)
19. [20% azelaic-acid vehicle-controlled trial](https://pubmed.ncbi.nlm.nih.gov/9829446/)
20. [Triple combination vs hydroquinone in Asian participants](https://pubmed.ncbi.nlm.nih.gov/18616780/)
21. [Triple-combination maintenance RCT](https://pubmed.ncbi.nlm.nih.gov/21623930/)
22. [Triple-combination 24-week study](https://pubmed.ncbi.nlm.nih.gov/20398959/)
23. [Large community hydroquinone study](https://pubmed.ncbi.nlm.nih.gov/16610738/)
24. [Cysteamine 5% placebo RCT](https://pubmed.ncbi.nlm.nih.gov/25251767/)
25. [Cysteamine vs hydroquinone + ascorbic acid](https://pubmed.ncbi.nlm.nih.gov/35510765/)
26. [Cysteamine vs tranexamic-acid mesotherapy](https://pubmed.ncbi.nlm.nih.gov/32879998/)
27. [Cysteamine + ectoine vs HQ + ectoine](https://pubmed.ncbi.nlm.nih.gov/40127492/)
28. [Kojic-acid clinical comparison](https://pubmed.ncbi.nlm.nih.gov/23918998/)
29. [Cysteamine vs kojic acid 2025 trial](https://pubmed.ncbi.nlm.nih.gov/40296942/)
30. [Alpha-arbutin + kojic acid vs triple combination](https://pubmed.ncbi.nlm.nih.gov/39555866/)
31. [Arbutin/herbal formula RCT](https://pubmed.ncbi.nlm.nih.gov/30980618/)
32. [Thiamidol human-tyrosinase screen](https://pubmed.ncbi.nlm.nih.gov/29427586/)
33. [Thiamidol vs HQ evaluator-blinded RCT](https://pubmed.ncbi.nlm.nih.gov/33988887/)
34. [Thiamidol UVB-prevention study](https://pubmed.ncbi.nlm.nih.gov/32757247/)
35. [Thiamidol systematic review](https://pubmed.ncbi.nlm.nih.gov/39496126/)
36. [Thiamidol skin-of-color case series](https://pubmed.ncbi.nlm.nih.gov/40847672/)
37. [0.1% 4-n-butylresorcinol split-face RCT](https://pubmed.ncbi.nlm.nih.gov/20548876/)
38. [0.3% 4-n-butylresorcinol open study](https://pubmed.ncbi.nlm.nih.gov/26855596/)
39. [Rucinol split-face RCT](https://pubmed.ncbi.nlm.nih.gov/17388924/)
40. [4-BR/resveratrol liposomal study](https://pubmed.ncbi.nlm.nih.gov/31347777/)
41. [Hexylresorcinol vs HQ randomized study](https://pubmed.ncbi.nlm.nih.gov/36502500/)
42. [Hexylresorcinol + niacinamide study](https://pubmed.ncbi.nlm.nih.gov/34958693/)
43. [Phenylethyl resorcinol + retinaldehyde study](https://pubmed.ncbi.nlm.nih.gov/25871836/)
44. [Phenylethyl-resorcinol complex study](https://pubmed.ncbi.nlm.nih.gov/23438137/)
45. [Melasyl/2-MNG facial melasma study](https://pubmed.ncbi.nlm.nih.gov/40586974/)
46. [Melasyl skin-of-color open study](https://pmc.ncbi.nlm.nih.gov/articles/PMC12710987/)
47. [Melasyl HEV prevention trials](https://pubmed.ncbi.nlm.nih.gov/41142247/)
48. [KT-939 2025 study](https://pubmed.ncbi.nlm.nih.gov/41159291/)
49. [PTPD-12 peptide study](https://pubmed.ncbi.nlm.nih.gov/41044809/)
50. [Malassezin vs hydroquinone study](https://pubmed.ncbi.nlm.nih.gov/41493251/)
51. [Ascorbic acid vs hydroquinone](https://pubmed.ncbi.nlm.nih.gov/15304189/)
52. [Topical glutathione systematic review](https://pubmed.ncbi.nlm.nih.gov/39444151/)
53. [Liquiritin split-face study](https://pubmed.ncbi.nlm.nih.gov/10809983/)
54. [Glabridin/andrographolide/apolactoferrin study](https://pubmed.ncbi.nlm.nih.gov/31541594/)
55. [Mercury chloride human-tyrosinase mechanism](https://pubmed.ncbi.nlm.nih.gov/32210794/)
56. [Mercury skin-lightener toxicology review](https://pubmed.ncbi.nlm.nih.gov/22070559/)
57. [Eucerin Radiant Tone Dual Serum — official product page](https://www.eucerinus.com/products/radiant-tone/dual-serum)
58. [Anua Niacinamide 10 TXA 4 Serum — official product page](https://anua.com/products/niacinamide-10-txa-4-serum-2?_pos=2&_psq=Serum&_ss=e&_v=1.0)
59. [COSRX Alpha-Arbutin 2 Discoloration Care — official product page](https://www.cosrx.com/products/the-alpha-arbutin-2-discoloration-care-serum?_pos=6&_sid=56988b0d8&_ss=r&externalId=2L5lB)
60. [Anua Azelaic Acid 10 Hyaluron — official product page](https://anua.com/products/azelaic-acid-10-hyaluron-redness-soothing-serum?shpxid=69b2282e-5b36-4a83-ab0f-41bba1a3572a)
61. [Minimalist Alpha Arbutin 2% — official product page](https://beminimalist.co/collections/face-serum/products/alpha-arbutin-2)
62. [The Ordinary Alpha Arbutin 2% + HA — official product page](https://theordinary.com/en-us/alpha-arbutin-2-ha-serum-100401.html)
63. [Numbuzin No.5 Glutathione TXA Ampoule — official product page](https://us.numbuzin.com/products/no-5-glutathione-txa-advanced-dark-spot-ampoule-concentrate)
64. [La Roche-Posay Mela B3 — official U.S. product page](https://www.laroche-posay.us/our-products/face/face-serum/mela-b3-dark-spot-serum-with-melasyl-niacinamide-3337875890021.html)
65. [Admire My Skin Ultra Potent Brightening Serum — official product page](https://www.admiremyskin.com/products/melasma-treatment-cream)
66. [SKINTIFIC 377 Dark Spot Serum — official U.S. product page](https://us.skintific.com/products/377-dark-spot-serum)
67. [Paula’s Choice discontinued-product notice](https://helpcenter.paulaschoice.com/en_us/discontinued-product-H1CluQLoex)
68. [User-supplied Chemist Confessions #170 Hyperpigmentation Finale](https://youtu.be/r95YJoxZQ-I) — source of the tier framework and named radar products; placements are cross-checked against the independent evidence census above.
