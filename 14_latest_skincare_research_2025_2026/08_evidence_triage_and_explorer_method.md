# Evidence Triage and Paper Explorer Method

*Compiled 2026-08-23. Research-navigation method, not a systematic review, clinical quality appraisal, diagnosis, or treatment recommendation.*

## Bottom line

The archive already had a strong 100-record evidence ledger and a 35-paper high-prestige supplement. What it lacked was a way to ask a practical question across both datasets without scanning long tables. The [paper evidence explorer](paper_evidence_explorer.html) adds combined search, category, design-family, evidence-tier, conflict-signal, year, archive-route, and high-prestige filters.

The explorer does **not** rank treatments. It helps a reader locate records, see what kind of evidence they are looking at, and route the paper to the archive topic that can interpret it.

## 1. Corpus accounting

| Layer | Records | Interpretation |
|---|---:|---|
| Main ledger | 100 | Frozen inclusion set through the archive's 2026-07-14 cutoff |
| High-prestige supplement | 35 | An overlapping subset of the 100, enriched with journal and selection-rationale fields |
| Total unique records in explorer | **100** | Never display 135 as though the supplement were additional evidence |
| Post-cutoff watchlist | 5 | Live-screened candidates kept separate pending full inclusion review |

The embedded JavaScript mirror is generated from the two CSVs so the explorer can work when the archive is opened from disk. The CSVs remain the auditable source tables; the tool's deterministic self-test verifies the expected 100/35 counts.

## 2. What each filter means

| Filter | What it does | What it does not mean |
|---|---|---|
| Free-text search | Matches PMID, title, population/scope, result, category, and recorded design | Semantic search or relevance scoring |
| Category | Uses the original ledger's 20 category labels | A mutually exclusive disease taxonomy |
| Design family | Normalizes 67 free-text design descriptions into seven navigation buckets | A validated risk-of-bias judgment |
| Evidence tier | Preserves the ledger's A/B/C/review field | A universal GRADE rating or treatment recommendation |
| Conflict signal | Filters “none disclosed,” “industry-linked,” and uncertain labels | Proof that a finding is true or false |
| Archive destination | Shows which numbered folder should own the deeper interpretation | Proof that the folder already incorporated the paper |
| High-prestige only | Intersects results with the 35-record journal subset | Automatic high quality or clinical importance |

## 3. Design-family normalization

The explorer applies a transparent deterministic text rule:

1. descriptions containing randomized, within-person, or intraparticipant language → **randomized / within-person**;
2. systematic review, meta-analysis, review, or synthesis → **review / meta-analysis**;
3. consensus, Delphi, recommendations, or algorithm → **consensus / Delphi**;
4. prospective, open-label, cohort, clinical study, or clinical trial → **prospective nonrandomized** unless captured above;
5. retrospective → **retrospective**;
6. in-vitro, ex-vivo, translational, formulation, histology, or similar language → **preclinical / translational**; and
7. everything else → **other clinical / unclear**.

This is a browsing convenience. A “randomized” tag says nothing by itself about allocation concealment, blinding, missing data, selective reporting, multiplicity, measurement validity, or applicability.

## 4. A defensible reading workflow

1. Start with the clinical question, population, and endpoint—not the product name.
2. Filter to a category, then compare randomized records with reviews/consensus.
3. Read population and scope before treating a result as transferable.
4. Open PubMed and, where possible, the full paper; verify comparator, sample size, duration, absolute effect, adverse events, attrition, and funding.
5. Use the archive-destination link for device parameters, regulatory status, formulation context, and safety boundaries.
6. Treat the conflict field as a prompt for closer methods review, not a veto.
7. Re-run PubMed before a current purchasing or treatment decision.

## 5. Live post-cutoff recheck: what changed

On 2026-08-23, a PubMed entry-date recheck from 2026-07-15 through 2026-08-23 surfaced five especially relevant candidates. They are recorded in the direct-download [post-cutoff watchlist CSV](data/post_cutoff_watchlist_2026-08-23.csv) but intentionally excluded from the frozen 100-record explorer until the original inclusion and extraction method is rerun.

| PMID | Why it deserves full screening | Immediate limitation |
|---|---|---|
| [42545315](https://pubmed.ncbi.nlm.nih.gov/42545315/) | Scoping review uses a GRADE framework to compare home acne/rejuvenation device lanes; reports strongest support for home fractional nonablative laser and moderate support for some LED/RF uses | Scoping review; modality-level conclusions still require paper/device matching |
| [42587095](https://pubmed.ncbi.nlm.nih.gov/42587095/) | Randomized split-face study compares MFU alone with MFU + 1550-nm NAFL in Fitzpatrick III–IV participants | 22 completers; combination study does not isolate the effect of MFU versus no treatment |
| [42572367](https://pubmed.ncbi.nlm.nih.gov/42572367/) | Vehicle-controlled split-face trial of one defined 0.1% retinal + 10% azelaic-acid concentrate | 23 completers, eight weeks, one formulation; not proof that arbitrary product stacking is equivalent |
| [42574285](https://pubmed.ncbi.nlm.nih.gov/42574285/) | One-year randomized vehicle-controlled photoprotection study uses in-vivo 3D multiphoton microscopy across seasons | 59 women, European descent, Fitzpatrick II–III, one city and one specific formula |
| [42627471](https://pubmed.ncbi.nlm.nih.gov/42627471/) | Narrative review specifically addresses aging, pigment, visible light, and procedural risk in skin of color | Narrative—not systematic—review; multiple relationships are disclosed by some authors |

This watchlist is an **update signal**, not a conclusion that every record should enter the final ledger. Full screening still needs duplicate checks, original eligibility rules, full-text methods/limitations, consistent tier assignment, and archive routing.

## 6. What the explorer adds—and what remains missing

### Added

- one query surface across every main-ledger record;
- explicit 100-versus-35 overlap accounting;
- transparent design normalization;
- combined conflict, tier, category, route, year, and journal-subset filtering;
- direct PubMed and destination-topic routing;
- filtered CSV export; and
- a deterministic `?test=1` mode that checks counts, normalization, combined filtering, empty states, and CSV escaping.

### Still missing

- formal duplicate screening and PRISMA flow for future updates;
- full-text risk-of-bias judgments per study;
- normalized sample-size, comparator, duration, absolute-effect, and adverse-event fields across all 100 records;
- trial-registry matching and correction/retraction monitoring;
- systematic Embase, Scopus, Web of Science, clinical-trial-registry, and non-English searches;
- independent verification of every conflict/funding entry; and
- a formally rerun corpus after 2026-07-14.

## Sources

1. [PubMed](https://pubmed.ncbi.nlm.nih.gov/) / MEDLINE. Official NCBI search and record source used for the live post-cutoff check.
2. [Search method and executive map](index.html#doc0). Original scope, inclusion rules, and archive routing.
3. [Annotated bibliography and evidence ledger](index.html#doc5). Study-level narrative context behind the structured records.
4. [High-prestige dermatology papers](index.html#doc6). Selection rationale for the overlapping 35-paper subset.
5. PubMed records [42545315](https://pubmed.ncbi.nlm.nih.gov/42545315/), [42587095](https://pubmed.ncbi.nlm.nih.gov/42587095/), [42572367](https://pubmed.ncbi.nlm.nih.gov/42572367/), [42574285](https://pubmed.ncbi.nlm.nih.gov/42574285/), and [42627471](https://pubmed.ncbi.nlm.nih.gov/42627471/). Live post-cutoff candidates screened 2026-08-23.
