# Evidence framework and search method

*Compiled 2026-08-02. This is a transparent scoping atlas, not a registered systematic review or meta-analysis.*

## 0. Bottom line

The original atlas compilation reported a snapshot of 200 unique PubMed identifiers across the archive and combined it with the structured 100-record 2025–2026 index. The repository has since grown, and no frozen identifier manifest reproduces that historical count. The result remains broad and useful for navigation, but it should not be described as “all papers in the industry” or as a current bibliometric census.

## 1. Search boundary

- **Date window:** 2006-01-01 through 2026-08-02 for the atlas; older foundational papers remain visible when they define a mechanism or device lineage.
- **Databases and source types:** PubMed/MEDLINE records, PMC full text where legitimately available, FDA clearances/labels and safety communications, official IFUs/manuals, ClinicalTrials.gov records, patents, and the existing archive’s preserved source files.
- **Concept families:** photoaging, wrinkles, laxity, acne, acne scars, melasma, PIH, rosacea/redness, barrier repair, photoprotection, hair removal, peptides, vitamins/actives, LED/PBM, IPL, laser resurfacing, RF, RF microneedling, HIFU/MFU, microneedling, injectables, and periprocedural care.
- **Included evidence:** human RCTs, controlled trials, prospective cohorts, systematic reviews/meta-analyses, consensus statements, regulatory primary documents, and mechanistic studies when they explain a constraint.
- **Excluded from efficacy scoring:** influencer testimonials, retailer star ratings, patents as proof of performance, market-size estimates, unverified seller specifications, and animal/in-vitro work standing alone.

## 2. Evidence hierarchy

| Tier | Meaning | Example use |
|---|---|---|
| A | Human RCT, systematic review/meta-analysis, or regulatory primary evidence tied to the stated endpoint | Establishes a category–endpoint signal |
| B | Human prospective/controlled study, consensus, or well-described product-linked trial | Supports a plausible but narrower claim |
| C | Mechanistic, in-vitro, small uncontrolled, or indirect evidence | Explains plausibility; does not prove consumer outcome |
| M | Marketing, patent, seller, or product claim | Describes the market; never counted as efficacy proof |

## 3. Atlas score

The interactive map uses a transparent 0–100 score, rounded for display:

`score = 0.35 × human-volume + 0.30 × design-strength + 0.20 × endpoint-fit + 0.15 × transparency`

Human volume uses the mapped number of category-relevant human studies/reviews, capped so a prolific but repetitive product literature does not dominate. Design strength rewards RCTs and high-level synthesis. Endpoint fit asks whether the evidence measures the user’s target rather than a surrogate. Transparency rewards reproducible parameters, product identity, follow-up, and safety reporting.

**Current auditability limit:** the stored CSV contains the final score, directional human/review/RCT counts, endpoint fit, and transparency, but it does not contain the normalized `human-volume` and `design-strength` fields, their exact transforms/caps, or a frozen PMID-to-category manifest. The formula describes the editorial model but the current rows cannot be independently recomputed. Until those fields are restored, treat scores and counts as manually curated orientation estimates—not effect sizes or precise bibliometric totals.

This is a navigation score, not a validated clinical prediction model, cost-effectiveness analysis, or personalized treatment ranking. The map uses node size based on `score`, while the interface separately shows evidence tier and home-translation confidence. Categories are nonexclusive: for example, retinoids and azelaic acid also contribute to the broad acne-active lane, so scores must not be added together as independent benefit.

## 4. What is counted

- The recent handoff includes the [100-record 2025–2026 ledger](../14_latest_skincare_research_2025_2026/data/paper_index.csv), with year, design, population, key result, evidence tier, conflict flag, and existing archive route.
- The local anchor ledger contains selected 2006–2026 human studies, reviews, and consensus papers that define the major categories and the archive’s older evidence spine.
- Existing topic pages remain the source of exact device-level counts, measured outputs, regulatory identifiers, product labels, and preserved PDFs.
- The [focused current-routine ledger](data/high_value_current_regimen_evidence.csv) provides a smaller paper-level join for the highest-ranked/currently used categories. It is auditable but is not an attempt to validate every directional atlas count.

## 5. Main limitations

The search is PubMed-centered; it is not exhaustive across Embase, Scopus, Web of Science, Chinese/Korean databases, or commercial formulation dossiers. Publication bias, industry sponsorship, inconsistent endpoints, under-representation of darker skin types, short follow-up, device-specific parameter reporting, overlapping categories, and the missing reproducibility fields all limit cross-category comparison. A large node may reflect a mature research field with mixed effect sizes; a small node may reflect an emerging field that is not yet disproven.

## Sources

1. [PRISMA 2020 statement](https://www.bmj.com/content/372/bmj.n71) — reporting framework and transparency reference.
2. [PubMed](https://pubmed.ncbi.nlm.nih.gov/) — primary bibliographic index used by the archive.
3. [2025–2026 archive search method](../14_latest_skincare_research_2025_2026/index.html#doc0) — the recent search record and eligibility framing.
4. [PubMed E-utilities documentation](https://www.ncbi.nlm.nih.gov/books/NBK25501/) — stable API metadata reference.
