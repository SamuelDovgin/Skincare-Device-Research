# 2025–2026 literature source manifest

*Accessed 2026-07-14. No unauthorized full texts were copied into this repository. The durable primary route for each paper is its PubMed record, which links to a legitimate full text when available.*

## Search sources

- [PubMed](https://pubmed.ncbi.nlm.nih.gov/) was the primary index. Queries were run against title/abstract and publication-date fields for 2025–2026 across acne, skin barrier/atopic dermatitis, microbiome, melasma/PIH, sunscreen/visible light, photoaging, peptide/cosmetic, LED/photobiomodulation, laser/IPL, RF/RF microneedling, HIFU/MFU, and hair-removal terms.
- [NCBI E-utilities](https://www.ncbi.nlm.nih.gov/books/NBK25501/) was used to inspect PubMed IDs, publication type, date, journal, DOI fields, and abstracts for the structured ledger.
- The paper ledger links every record to `https://pubmed.ncbi.nlm.nih.gov/<PMID>/`; the PubMed page is the source of truth for the article metadata.
- A second journal-curated pass prioritized JAMA Dermatology, JAAD, British Journal of Dermatology, JEADV, Dermatologic Surgery, and Lasers in Surgery and Medicine. It added 34 new records to the main ledger and preserves 35 selected records in `data/high_prestige_paper_index.csv`.

## Evidence labels

- **primary-clinical:** randomized trial, controlled clinical study, prospective cohort, or clinical trial.
- **review/meta-analysis:** systematic review, network meta-analysis, or meta-analysis of clinical studies.
- **consensus/guideline:** Delphi or expert algorithm; useful for practice framing, not equivalent to a randomized efficacy result.
- **emerging:** in-vitro, delivery, or mechanistic work included to show where the field is moving; not a clinical outcome.

## Funding and conflict flags

The ledger uses `industry-linked`, `mixed/unclear`, or `none disclosed` when the PubMed record identifies a manufacturer, brand, inventor, consultant relationship, or no declared conflict. “Industry-linked” does not make a study false; it lowers independence and increases the need for replication.

## Recheck protocol

Before a future update, rerun the same term families with the new date range, deduplicate by PMID/DOI, check retractions and corrections, and add an `accessed` date. Treat e-publication dates as the inclusion date when an issue date falls later.
