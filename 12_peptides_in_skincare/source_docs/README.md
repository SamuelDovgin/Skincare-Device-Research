# Peptide Research Source Manifest

Captured 2026-07-12 and expanded 2026-07-13. Files are preserved to keep the peptide evidence ranking and supplier-industry map auditable. Open-access full text is stored as publisher PDF or Europe PMC JATS XML. Paywalled primary studies are represented by PubMed XML records containing bibliographic metadata and abstracts, not unauthorized full text.

The ingredient-cost model added 2026-08-13 uses live supplier/product URLs and a local calculation ledger rather than pretending that private supplier quotes are public. See [`../07_peptide_ingredient_cost_model.md`](../07_peptide_ingredient_cost_model.md) and [`../data/peptide_cost_model.csv`](../data/peptide_cost_model.csv) for the assumptions, ranges, and source links.

| File | Source | Type | What it supports |
|---|---|---|---|
| `nukaly-2026-oral-topical-peptides-systematic-review.pdf` | Frontiers in Medicine / PMC13037056, CC BY | Open-access systematic review PDF | 19 RCT/1,341-participant synthesis; only two high-quality topical studies; oral formulations drive much pooled benefit |
| `chang-2025-cyclized-hexapeptide-9-trial.xml` | Europe PMC / PMC12207714, CC BY | Open-access full-text JATS XML | 96-person CHP-9 vs 0.002% retinol vs vehicle randomized trial; methods, outcomes, funding/conflict statements |
| `acetyl-hexapeptide-8-permeability-efficacy-review-2025.xml` | Europe PMC / PMC12193160, CC BY | Open-access full-text JATS XML | Argireline mechanism, permeability limits, and clinical-evidence review |
| `ghk-topical-antiwrinkle-review-2024.xml` | Europe PMC / PMC11830136, CC BY-NC | Open-access full-text JATS XML | GHK/Pal-GHK permeability, formulation, and delivery constraints |
| `ghk-cu-skin-regeneration-review-2015.xml` | Europe PMC / PMC4508379, CC BY | Open-access full-text JATS XML | GHK-Cu mechanistic and historical clinical context |
| `pal-kttks-2005-rct-pubmed.xml` | PubMed PMID 18492182 | Primary-study abstract record | 93-person randomized double-blind split-face pal-KTTKS trial |
| `argireline-2013-rct-pubmed.xml` | PubMed PMID 23417317 | Primary-study abstract record | 60-person randomized placebo-controlled Argireline trial |
| `ghk-cu-post-laser-2006-trial-pubmed.xml` | PubMed PMID 16847171 | Primary-study abstract record | Randomized post-CO2-laser GHK-Cu trial with no objective advantage |
| `niacinamide-2005-rct-pubmed.xml` | PubMed PMID 18492135 | Comparator primary-study abstract | 5% niacinamide split-face vehicle-controlled evidence |
| `sunscreen-photoaging-2013-rct-pubmed.xml` | PubMed PMID 23732711 | Comparator primary-study abstract | 903-person randomized 4.5-year photoaging-prevention evidence |
| `tretinoin-and-botulinum-comparator-trials-pubmed.xml` | PubMed PMIDs 3336176 and 19549186 | Comparator primary-study abstracts | Tretinoin photoaging and botulinum-toxin dynamic-line evidence |
| `retinol-0.1-percent-2015-rct-pubmed.xml` | PubMed PMID 25738849 | Comparator primary-study abstract | One-year double-blind vehicle-controlled 0.1% stabilized-retinol photoaging evidence; concentration context for CHP-9 comparator |
| `os01-peptide14-2025-rct-pubmed.xml` | PubMed PMID 40193112 | Primary-study abstract record | OS-01 barrier/hydration pilot randomized trial |
| `ptpd12-pigment-2025-rct-pubmed.xml` | PubMed PMID 41044809 | Primary-study abstract record | PTPD-12 randomized split-face hyperpigmentation trial |
| `croda-matrixyl3000-development-formulation-2025.pdf` | Croda Beauty, development formulation SG0063 | Official supplier formulation PDF | Shows 3.00% Matrixyl 3000 commercial material, its two peptide INCIs, and Croda as supplier; demonstrates that use level refers to the premix rather than pure peptide |
| `basf-caregen-exclusive-peptide-supply-agreement-2021.pdf` | BASF/Caregen joint release | Official company announcement PDF | Verifies a global exclusive BASF supply agreement for four Caregen cosmetic peptides and the platform-to-ingredient-supplier business model |

## Original URLs

- https://pmc.ncbi.nlm.nih.gov/articles/PMC13037056/
- https://pmc.ncbi.nlm.nih.gov/articles/PMC12207714/
- https://pmc.ncbi.nlm.nih.gov/articles/PMC12193160/
- https://pmc.ncbi.nlm.nih.gov/articles/PMC11830136/
- https://pmc.ncbi.nlm.nih.gov/articles/PMC4508379/
- https://pubmed.ncbi.nlm.nih.gov/18492182/
- https://pubmed.ncbi.nlm.nih.gov/23417317/
- https://pubmed.ncbi.nlm.nih.gov/16847171/
- https://pubmed.ncbi.nlm.nih.gov/18492135/
- https://pubmed.ncbi.nlm.nih.gov/23732711/
- https://pubmed.ncbi.nlm.nih.gov/3336176/
- https://pubmed.ncbi.nlm.nih.gov/19549186/
- https://pubmed.ncbi.nlm.nih.gov/25738849/
- https://pubmed.ncbi.nlm.nih.gov/40193112/
- https://pubmed.ncbi.nlm.nih.gov/41044809/
- https://www.crodabeauty.com/mediaassets/files/beauty/ungated-files/ch0203--rebalancing-and-vitalising-scalp-mask--190924pcedf0194v1en.pdf
- https://www.basf.com/my/en/media/news-releases/asia-pacific/2021/01/basf_caregen_supply_agreement

## Cost-model source set (web snapshots checked 2026-08-13)

| Source | Type | What it supports |
|---|---|---|
| https://trulux.com/products/matrixyl-3000/ | Supplier storefront | Public 50 g–1 kg Matrixyl 3000 commercial-premix pricing |
| https://trulux.com/products/matrixyl-synthe-6/ | Supplier storefront | Public 50 g–1 kg Matrixyl Synthe’6 commercial-premix pricing |
| https://trulux.com/products/syn-coll/ | Supplier storefront | Public Palmitoyl Tripeptide-5/SYN-COLL pricing |
| https://www.made-in-china.com/price/prodetail_Organic-Intermediate_KwtGPkbvbeAm.html | Marketplace supplier listing | Bulk GHK-Cu price tiers; treated as lower-confidence marketplace evidence |
| https://albochem.com/product/ghk-cu-raw-powder-copperii-glycyl-l-histidyl-l-lysinate-%E2%89%A599-purity-10-grams/ | Cosmetic raw-material storefront | Small-lot ≥99% GHK-Cu price anchor |
| https://www.alibaba.com/supplier/polynucleotides-supplier-supplier-for-wholesale.html | Marketplace supplier index | Bulk Sodium DNA/PDRN price range |
| https://www.js-akx.com/PNO%E9%98%BF%E6%8B%89%E4%B8%81-I1506387.html | Cosmetic raw-material catalog | Small-lot Sodium DNA/PDRN price anchor |
| https://geekandgorgeous.com/products/power-peptides | Official product page | 3% Matrixyl 3000, 2% Synthe’6, 4% TEGO PEP 4-17, 0.001% X50, price and size |
| https://nichebeautylab.com/collections/bestseller-north-america/products/copper-peptide | Official product page | Theramid Copper 3% and 13% peptide-complex claims |
| https://nichebeautylab.com/en-gb/collections/eu-bestseller/products/derma-peptides | Official product page | Theramid Derma-Peptides 35% and size/price |
| https://us.allies.shop/products/copper-tripeptide-ectoin-advanced-repair-serum | Official product page | Allies 1% Copper Tripeptide Complex, 2% Acetyl Hexapeptide-8 Complex, 2% Copper Lysinate Complex |
