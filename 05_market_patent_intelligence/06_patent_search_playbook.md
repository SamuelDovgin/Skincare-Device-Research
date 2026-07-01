# 06 — The Playbook: How to Aggregate This Yourself

This category is a **dated snapshot** (assembled 2026-06-30), not a live feed. This site is a static
archive with no backend, so it can't scrape patent databases on every visit. What it *can* do — and
what this document is — is hand you the exact **repeatable process** used to build the other docs here,
so you can refresh the picture yourself in an afternoon whenever you want.

Everything below uses **free, public** sources. Patents are public by design; FDA clearances are public;
even most market-size headline figures leak out of paywalled reports through press releases. The trick is
knowing which query goes to which database.

---

## 1. The five databases that matter

| Tool | Best for | Cost | URL |
|------|----------|------|-----|
| **Google Patents** | Fast full-text search, "Cited by" / citation graph, family view, PDF | Free | patents.google.com [[1]](https://patents.google.com) |
| **USPTO Patent Public Search** | Authoritative US filings, legal status, examiner data | Free | ppubs.uspto.gov [[2]](https://ppubs.uspto.gov/pubwebapp/) |
| **Espacenet (EPO)** | Global coverage (100+ offices), classification search, family/legal status | Free | worldwide.espacenet.com [[3]](https://worldwide.espacenet.com) |
| **The Lens** | Bulk export, analytics dashboards, links patents ↔ scholarship | Free (login) | lens.org [[4]](https://www.lens.org) |
| **FDA 510(k) / De Novo database** | Whether a device is *cleared*, and cleared for *what* | Free | accessdata.fda.gov [[5]](https://www.accessdata.fda.gov/scripts/cdrh/cfdocs/cfpmn/pmn.cfm) |

Rule of thumb: **start in Google Patents** (fastest), **confirm legal status in Espacenet or USPTO**
(Google's status field lags), and **cross-check the marketing claim in FDA's database** (a device can
have ten patents and still not be cleared for what the ad implies).

---

## 2. Patent search — the actual queries

### 2a. Find the foundational patents of a modality
Search the modality + mechanism, not the brand. Brands change; the physics doesn't.

- IPL hair removal → `intense pulsed light hair removal` and the class code **A61B18/203** (dermatologic
  laser/IPL). In Google Patents, run the term, then switch to the **classification** the top results share
  and browse siblings. [[1]](https://patents.google.com)
- RF skin tightening → `radiofrequency skin tightening` + **A61B18/14** (RF electrosurgery) / **A61N1/40**.
- Fractional laser → `fractional photothermolysis` (this is the Manstein/Anderson coinage — chase its
  citations). [[1]](https://patents.google.com)
- Microneedle RF → `radiofrequency microneedle` + **A61B18/1477**.

Then click **"Cited by"** on a seminal result to walk *forward* in time to everyone who built on it, and
the reference list to walk *backward* to the prior art. The citation graph is the landscape.

### 2b. Find who is filing *now* (the trend signal)
- Add a date filter: `after:priority:20230101`.
- Add `assignee:` to follow a company: `assignee:"Home Skinovations"`, `assignee:"Tria Beauty"`,
  `assignee:"L'Oreal"`, `assignee:"Solta"`, `assignee:"Cynosure"`.
- Sort by date, not relevance, to see the leading edge.

### 2c. Read the legal status (the part that decides market impact)
A patent only blocks competitors while it's **alive**. Utility patents run **20 years from the earliest
non-provisional filing date**, subject to maintenance-fee payment. [[2]](https://ppubs.uspto.gov/pubwebapp/)[[6]](https://www.uspto.gov/patents/laws/patent-fees) So a foundational IPL patent
filed in 2001 is, absent extensions, **expired around 2021** — which is exactly why the OEM flood of cheap
IPL happened when it did. Check status in Espacenet's **"Legal events"** tab or USPTO, because Google's
"Status: Expired" flag is often stale or based on fee lapse rather than term end. [[3]](https://worldwide.espacenet.com)

### 2d. Map an assignee's portfolio fast
In **The Lens**, search `assignee:(company)`, then open the **Analysis** tab for auto-generated charts:
filings per year, jurisdictions, top classifications, and citation counts — a one-click portfolio map you'd
otherwise build by hand. Export to CSV for your own tables. [[4]](https://www.lens.org)

---

## 3. The clearance cross-check (do not skip this)

A patent says *"someone invented a thing."* It says **nothing** about whether a device is legal to sell for
a given claim. That's the FDA's job, and it's the single most useful reality filter for this whole market.

Search the **510(k) database** by device or applicant. [[5]](https://www.accessdata.fda.gov/scripts/cdrh/cfdocs/cfpmn/pmn.cfm) For home light/energy devices you will almost
always find the product regulated under a hair-removal product code (e.g. **OHT / GEX**-type lamp codes) —
meaning it is cleared **for hair removal only**, even when the same box is marketed for "skin rejuvenation,"
"anti-aging," or "spot correction." If a device claims a dermatologic benefit its 510(k) doesn't list, that
claim is marketing, not clearance. This is the throughline of the entire archive: *no at-home IPL/laser
device is FDA-cleared for anything but hair removal.* [[5]](https://www.accessdata.fda.gov/scripts/cdrh/cfdocs/cfpmn/pmn.cfm)[[7]](https://www.fda.gov/medical-devices/home-use-devices/aesthetic-cosmetic-devices)

Also check the **De Novo** and **product-classification** databases for genuinely new categories (LED masks,
some RF devices are cleared under different codes for "temporary improvement in the appearance of…"). The
wording of the clearance is the honest version of the claim.

---

## 4. Market sizing — reading vendor numbers without getting fooled

Home-device market-size figures come from research firms (Grand View, Fortune Business Insights,
MarketsandMarkets, Precedence, Statista). They are **models, not audited accounts**, and they routinely
disagree by 2–5× because each defines "the market" differently (devices only? incl. topicals? incl.
professional?). [[8]](https://www.grandviewresearch.com/industry-analysis/beauty-devices-market) How to use them honestly:

1. **Never cite one number.** Pull 3–4 and show the *range* — that's what the "estimates by source" table
   in doc 04 does.
2. **Read the scope line.** "At-home beauty devices" ≠ "beauty devices" ≠ "aesthetic devices (incl. clinic)."
   A huge headline number is usually the widest scope.
3. **Discount the CAGR.** Forecast CAGRs are the most speculative field in the whole report; treat them as
   direction, not precision.
4. **Prefer disclosed anchors.** A public company's segment revenue (e.g. a SharkNinja or L'Oréal earnings
   deck) or a real funding round is worth more than a modeled TAM. [[8]](https://www.grandviewresearch.com/industry-analysis/beauty-devices-market)

The free **press release** for a paywalled report almost always contains the headline size + CAGR + the
segment/region breakdown — enough to build the table without buying the PDF.

---

## 5. A repeatable 60-minute refresh recipe

1. **Trend pulse (15 min).** Google Patents, each modality term + `after:priority:20250101`, sort by date.
   Note new assignees and any new mechanism words (that's where the frontier is).
2. **Portfolio deltas (15 min).** The Lens, re-run your saved assignee searches; screenshot the filings-
   per-year chart; note who accelerated.
3. **Clearance sweep (10 min).** FDA 510(k) database, search the quarter's new home-device applicants; note
   what code they cleared under (tells you the *real* allowed claim).
4. **Market check (10 min).** Search `"at-home beauty device market" 2026 report` for any fresh press
   release; update the size range.
5. **Product scan (10 min).** Skim CES / brand-launch coverage and 2–3 retail best-seller lists; add any
   new device to the teardown table with its claimed spec + whatever clearance you can verify.

Log the date you did it. A dated snapshot you can trust beats a "live" number you can't.

---

## 6. Caveats & honesty notes

- **Patents ≠ products.** Most filings never ship. Treat a patent as evidence of *intent and direction*,
  not of a real device.
- **Assignee ≠ inventor ≠ manufacturer.** A Shenzhen OEM may make the hardware while the patent sits with a
  Western brand, or vice-versa. Don't infer who *makes* a device from who *owns* a patent.
- **Google's legal-status field lags.** Always confirm expiry in Espacenet/USPTO before claiming a patent is
  dead.
- **Market numbers are models.** Cite the firm and the year, show the spread, never launder one estimate
  into a fact.
- **This snapshot decays.** Filing trends and clearances move quarterly. Re-run §5 before relying on it.

---

## Sources

1. Google Patents — https://patents.google.com — free full-text patent search with "Cited by" citation graph, family view, and classification browsing; primary tool for finding foundational and recent filings.
2. USPTO Patent Public Search — https://ppubs.uspto.gov/pubwebapp/ — authoritative US patent search with legal status and examiner data; used to confirm grant/status.
3. Espacenet (European Patent Office) — https://worldwide.espacenet.com — global patent coverage across 100+ offices with a "Legal events" tab for authoritative expiry/status, which Google's status field often lags.
4. The Lens — https://www.lens.org — free patent + scholarship database with bulk CSV export and auto-generated assignee analytics (filings-per-year, jurisdictions, classifications).
5. FDA 510(k) Premarket Notification Database — https://www.accessdata.fda.gov/scripts/cdrh/cfdocs/cfpmn/pmn.cfm — searchable record of what a device is actually cleared to be marketed for; the reality filter against marketing claims.
6. USPTO — Patent term and maintenance fees — https://www.uspto.gov/patents/laws/patent-fees — utility patents run 20 years from earliest non-provisional filing, contingent on maintenance-fee payment, explaining when foundational patents expire.
7. FDA — Aesthetic (Cosmetic) Devices / hair-removal laser & IPL guidance — https://www.fda.gov/medical-devices/home-use-devices/aesthetic-cosmetic-devices — home IPL/laser devices are regulated and generally cleared for hair removal, not skin rejuvenation.
8. Grand View Research — Beauty Devices Market report (press summary) — https://www.grandviewresearch.com/industry-analysis/beauty-devices-market — example of a vendor market-size model; illustrates why scope/CAGR must be read carefully and triangulated across firms.
