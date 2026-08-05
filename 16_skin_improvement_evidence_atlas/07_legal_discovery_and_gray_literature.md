# Legal discovery layer and gray literature

*Updated 2026-08-02. This page records sources found outside the archive’s usual PubMed-only workflow. It does not use Sci-Hub or unauthorized full text.*

## 0. Bottom line

The web contains valuable evidence that is easy to miss if a search stops at a familiar journal list: PMC full text, Europe PMC records, clinical-trial protocols and statistical-analysis plans, institutional theses, conference abstracts, preprints, robotics papers, regulatory safety communications, and formulation/product studies. These sources broaden discovery, but they must be labeled by evidence type before they influence the atlas score.

## 1. What was added

- **300 Europe PMC discovery records** across photoaging, acne devices, pigment, peptides, photoprotection, RF, microneedling, HIFU/ultrasound, PBM, and fractional-laser searches. The ledger includes PMID/DOI/PMCID, year, title, journal, open-access/full-text flags, source query, and Europe PMC URL.
- **18 nontraditional/gray sources** including PMC full-text studies, ClinicalTrials.gov protocols, Korean and Spanish institutional theses, an EADV conference abstract, UCL/KAIST repositories, arXiv engineering papers, and current FDA safety/regulatory pages.
- **A strict evidence boundary:** discovery records are not counted as efficacy proof until screened for human design, endpoint fit, product identity, sample size, follow-up, skin-type representation, adverse events, and conflicts.

## 2. How to use the discovery ledger

1. Filter first for `pmcid` or `open_access=Y` when you want legal full text.
2. Deduplicate against the local 200-PMID archive spine and the 100-record 2025–2026 ledger.
3. Promote only records with a defined human endpoint or a clearly useful regulatory/technical constraint into the scored evidence map.
4. Keep animal, in-vitro, thesis, protocol, abstract, and engineering records in their own evidence class; they are valuable for mechanisms and gap-finding but do not become clinical efficacy claims by proximity.

## 3. High-value discoveries

| Source type | What it adds | How to interpret it |
|---|---|---|
| PMC RF microneedling review | Full methods, conflicts, geography, and study-level synthesis | Useful synthesis; industry conflicts and heterogeneous protocols remain relevant |
| PMC peptide meta-analysis | 19 RCTs / 1,341 participants and topical-versus-oral subgroup framing | Helps keep oral pooled effects separate from topical finished-formula claims |
| ClinicalTrials.gov protocols | Prespecified outcomes and comparator/device plans before results | Design evidence, not a treatment result |
| Institutional theses | Local-language, device-specific, or small applied studies not always visible in journal searches | Discovery and hypothesis generation; verify degree, methods, and peer-review status |
| arXiv robotics papers | Sensor, aiming, imaging, and automation concepts | Engineering feasibility, not clinical efficacy or safety clearance |
| PMC formulation studies | Finished-formula details and large observational datasets | Product-linked evidence; inspect comparator, dropout, and sponsorship |
| FDA safety communication | Current post-market risk signal and a home-use boundary for RF microneedling | Safety/regulatory evidence, not a comparative efficacy result |

## 4. Evidence rules for “corners of the web”

- Legal availability is not evidence quality.
- A thesis is not automatically weaker than a journal paper, but its methods, supervision, sample, and review status must be checked.
- A preprint or conference abstract may be the earliest signal, not the final result.
- A protocol can reveal a strong design even when results are not yet public; it cannot establish efficacy.
- Patents and engineering papers can explain what a device might do; they do not show what a marketed unit actually delivers to human skin.
- Search-engine snippets, social posts, scraped PDFs, and file-sharing mirrors are leads only; they are not promoted into the corpus without a lawful, stable source.
- FDA clearance is device- and indication-specific; it is not a blanket endorsement of every use, setting, combination, or home device.

## Sources

1. [Europe PMC REST search API](https://www.ebi.ac.uk/europepmc/webservices/rest/search) — legal bibliographic discovery endpoint used for the 300-record ledger.
2. [Radiofrequency microneedling for facial rejuvenation](https://pmc.ncbi.nlm.nih.gov/articles/PMC13058395/) — open full-text systematic review with study geography and conflict disclosure.
3. [Oral and topical peptides for skin aging](https://pmc.ncbi.nlm.nih.gov/articles/PMC13037056/) — open full-text systematic review/meta-analysis.
4. [Mechanically induced skin renewal](https://pmc.ncbi.nlm.nih.gov/articles/PMC13184425/) — recent overview that explicitly describes evidence and mechanism limits.
5. [Peptide-pro complex serum](https://pmc.ncbi.nlm.nih.gov/articles/PMC10084013/) — open full-text product-linked formulation study.
6. [Topical hydroxypinacolone retinoate-peptide product versus fractional CO2 laser](https://pmc.ncbi.nlm.nih.gov/articles/PMC11743323/) — open full-text comparative topical/device study.
7. [NCT03767972 Energy Devices for Rejuvenation protocol/SAP](https://clinicaltrials.gov/study/NCT03767972) — protocol-level device-comparison source.
8. [Robotics meets cosmetic dermatology](https://arxiv.org/abs/2005.10462) — engineering paper on vision-guided photo-rejuvenation delivery.
9. [FDA RF-microneedling safety communication](https://www.fda.gov/medical-devices/safety-communications/potential-risks-certain-uses-radiofrequency-rf-microneedling-fda-safety-communication) — October 15, 2025 post-market safety communication.
10. [FDA microneedling devices overview](https://www.fda.gov/medical-devices/aesthetic-cosmetic-devices/microneedling-devices) — device-specific authorization, benefits, risks, and combination-use context.
