# Annotated bibliography and evidence ledger

*Compiled 2026-07-14. The companion CSV is the full structured ledger for this update. PubMed IDs are used as stable keys because DOI metadata can be corrected or displayed differently across online-first and issue records.*

## 0. How to use this page

The [paper index CSV](data/paper_index.csv) contains 100 selected 2025–2026 records. The [high-prestige paper index](data/high_prestige_paper_index.csv) isolates 35 papers from leading dermatology and procedure journals. Filter by `category`, `year`, `design`, `evidence_tier`, `conflict_flag`, or `existing_archive_route` to answer questions such as:

- Which recent studies are randomized human trials?
- Which findings specifically include skin of color or Fitzpatrick III–V?
- Which studies are reviews rather than new clinical data?
- Which claims are manufacturer-linked or product-specific?
- Which existing topic should receive a follow-up page?

## 1. Highest-priority reads

| Priority | Read | Why |
|---|---|---|
| 1 | [PIH prevention in skin of colour](https://pubmed.ncbi.nlm.nih.gov/39953770/) | Directly relevant to IPL/laser/peel safety; sunscreen was the only consistently successful prevention measure |
| 2 | [Visible-light photoprotection consensus](https://pubmed.ncbi.nlm.nih.gov/42101389/) | Establishes the measurement problem behind tinted sunscreen claims |
| 3 | [Tinted vs untinted sunscreen in melasma](https://pubmed.ncbi.nlm.nih.gov/41014037/) | Recent randomized intervention aligned with the archive’s pigment goal |
| 4 | [Adapalene for female skin aging](https://pubmed.ncbi.nlm.nih.gov/40990960/) | Recent human retinoid/photoaging trial with tolerability data |
| 5 | [Prebiotic gel cream in acne](https://pubmed.ncbi.nlm.nih.gov/41098119/) | Illustrates both the microbiome signal and the open-label/product-linked limitation |
| 6 | [Hydrogel acne meta-analysis](https://pubmed.ncbi.nlm.nih.gov/41528187/) | Shows why formulation evidence must be read with heterogeneity statistics |
| 7 | [PBM frequency trial](https://pubmed.ncbi.nlm.nih.gov/40167796/) | Gives a reproducible LED wavelength/irradiance/fluence tuple |
| 8 | [MFU-V meta-analysis](https://pubmed.ncbi.nlm.nih.gov/39540440/) | Best recent high-level HIFU/MFU evidence in the archive |
| 9 | [RF microneedling facial rejuvenation review](https://pubmed.ncbi.nlm.nih.gov/41947517/) | Useful efficacy synthesis, but conflict and home-translation caveats are explicit |
| 10 | [IPL vs diode hair-removal RCT](https://pubmed.ncbi.nlm.nih.gov/42249955/) | Directly updates the existing hair-removal decision lane |

## 2. Interpretation rules

- A systematic review inherits the weaknesses of its included studies; it is not automatically high certainty.
- A randomized trial with a branded product is still randomized evidence, but the result belongs to that formula and dose.
- A consensus statement is a practice framework, not a treatment effect estimate.
- An in-vitro result is a mechanistic or formulation signal only.
- A clinic device result does not establish the safety or efficacy of a home device without matching output, geometry, treatment schedule, and outcome.
- A study that reports a percentage improvement but omits comparator, variance, or follow-up should not be used in a precise value calculation.

## 3. What to add in a future update

1. Search Embase, Scopus, Web of Science, and ClinicalTrials.gov for records not indexed in PubMed.
2. Capture full-text parameter tables for the major device comparisons.
3. Add a dedicated acne topic if the user’s priority shifts from device research to disease management.
4. Recheck 2026 online-first records for corrections, retractions, and final issue metadata.
5. Add independent replication and real-world adherence studies for tinted sunscreen, microbiome products, topical peptides, and home energy devices.

## Sources

1. [PubMed](https://pubmed.ncbi.nlm.nih.gov/) — primary index used for the ledger and stable record links.
2. [NCBI E-utilities documentation](https://www.ncbi.nlm.nih.gov/books/NBK25501/) — API metadata and retrieval method.
3. [PRISMA 2020 statement](https://www.bmj.com/content/372/bmj.n71) — reporting framework used as a search-logging reference; this update is not itself a registered systematic review.
