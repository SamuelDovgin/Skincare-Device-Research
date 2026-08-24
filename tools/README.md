# tools

## `apply_citation_features.py`

Adds two citation features to the research archive, idempotently:

1. **Clickable inline citations** — numbered markers `[n]` in the markdown become
   `[[n]](source-url)`, linking to the source listed in that doc's *Sources* section.
2. **Evidence popover** — in each folder `index.html`, hovering (desktop) or tapping
   (mobile) a `[n]` shows the source name + the supporting quote pulled from that doc's
   Sources list, with an *Open full source* link. (CSS/JS injected into the viewer.)
3. **Embed sync** — re-syncs each `index.html`'s embedded `DOCS[].md` from disk.

### ⚠️ Re-run after regenerating the viewer
The folder `index.html` files are regenerated **externally** from the `.md` files. That
regeneration **wipes the popover** (it lives in the HTML, not the markdown). The `[[n]](url)`
links survive (they're in the markdown), but the hover/tap popover does not. After any
viewer regeneration, re-apply with:

```bash
python3 tools/apply_citation_features.py
```

Safe to run anytime — it only changes what's missing. Check status without writing:

```bash
python3 tools/apply_citation_features.py --check   # exit 1 if anything is pending
```

## `build_pairwise_evidence_ledger.js`

Extracts the Stack Lab's ingredient-only rule engine and writes
`13_combined_skincare_regimen/data/ingredient_pair_research_ledger.csv`. The ledger
contains one row per unordered pair, its same-session category and spacing rule, the
evidence boundary, source IDs, and direct proof links.

```bash
node tools/build_pairwise_evidence_ledger.js
```
