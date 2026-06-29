# Future Research Plan

What to investigate next to confidently pick (or commission) an at-home device that gets closest to an efficacious in-office laser treatment for **pigment + long-term collagen**.

**Guiding question:** *Of devices actually buyable today, which delivers the most of Clear + Brilliant's mechanism at home — and is it worth it vs a short in-office course + topicals?*

---

## Phase 0 — Decide the real strategy first (1 day, no spend)
Before any device research, settle the framing, because it changes everything downstream:
- **Pigment is mostly a topicals + photoprotection problem**, not a device problem (parent repo [07](../01_ipl_hair_removal/07_alternatives_and_strategy.md)). Confirm you accept a home laser as an *adjunct/collagen tool*, not a pigment cure.
- **Pick the primary goal:** if it's **pigment** → 1927nm path (Dora/Perméa class). If it's **collagen/texture** → 1450nm path (Tria/Iris class). If both → plan for *two* devices or an in-office Perméa course + home 1450nm maintenance.
- **Set budget + risk tolerance:** trustworthy-FDA ($650 Tria) vs cheaper-China-verify-yourself ($420–600 YDUNVIE/MimiSilk) vs in-office course ($1,500–3,000).

**Output:** one-paragraph decision recorded at top of the README.

---

## Phase 1 — Verify the top candidates against primary sources (1–2 weeks)
Turn the ⚠️ marketing claims in [03](03_device_landscape.md) into ✅ or ❌. Priority order:

| Candidate | What to verify | How |
|-----------|----------------|-----|
| **Tria FRX** | exact mJ/pulse, density, depth, real clinical data beyond periorbital | Read K130459 + K141868 PDFs fully; find independent reviews/studies |
| **YDUNVIE Iris Ice / Plus** | true wavelength, mJ/pulse vs full-face J, density, cooling temp, K182498 coverage | Request datasheet from Jiangsu Unimed; pull K182498 PDF; compare Iris vs Iris Ice Plus in **same units** |
| **YDUNVIE Dora (1927nm)** | confirm 1927nm, energy, depth, Fitzpatrick limits, PIH data | Datasheet + any clinical evidence; this is the pigment workhorse |
| **MimiSilk Iris** | is it literally the YDUNVIE/Jiangsu Unimed device? what's its real K-number/UDI? | Ask MimiSilk for K-number + label; compare to K182498; check myernk "authorized agent" claim |

**Key deliverable:** a one-page verified spec comparison (Tria vs Iris Ice Plus vs Dora vs Clear+Brilliant), all in identical units, single-pulse vs total clearly flagged.

**Download for the repo:** the actual 510(k) PDFs (K130459, K141868, K163137, K222685, K090525, K133473, K182498, K231910, K244020) — mirror the parent repo's "PDFs in repo" practice.

---

## Phase 2 — Map the buyable market completely (1 week)
Fill gaps in [03](03_device_landscape.md). Devices/brands to chase down that the current pass only touched lightly:

- **Discontinued-but-instructive:** PaloVia and Philips RéAura — find teardown reviews, manuals, real specs (they define "home Fraxel done right").
- **Current China-market siblings:** OYAY (Iris/Dora), MimiSilk, myernk YDUNVIE, plus any other "1450nm/1927nm at-home fractional" brands (Iris Ice clones proliferate). Determine which are the **same Jiangsu Unimed hardware** vs distinct.
- **Korean/other OEM:** the "1450nm Accu Smart"-type systems and any Korean home fractional devices.
- **Newer in-office tech to benchmark against:** Sciton Moxi, LaseMD Ultra, Fraxel Dual — confirm their parameters as the "efficacious ceiling."
- **Adjacent (rule in/out):** confirm NIRA, LYMA, JOVS, DermRays are correctly categorized as *not* fractional resurfacers.

**Deliverable:** expanded master table with a "same-hardware-as?" column and a verified ✅/⚠️ on every spec.

---

## Phase 3 — Clinical efficacy evidence review (1–2 weeks)
The current folder is strong on *specs* and weak on *outcomes*. Before buying, answer: **does the home version actually work, and how much?**

- Find peer-reviewed trials for **home NAF lasers** (PaloVia multicenter trial is the anchor; search for Tria, RéAura studies).
- Compare effect sizes: home NAF vs in-office Clear+Brilliant/Fraxel for (a) pigment/tone, (b) wrinkles/collagen.
- Pull **realistic expectation numbers** (e.g., % improvement, sessions-to-result) to set expectations honestly.
- Specifically search **1927nm at-home pigment** evidence and **PIH risk in Fitzpatrick III–VI** for these devices.

**Deliverable:** a short evidence brief — "what % of in-office results can a home fractional device realistically deliver, and over what timeframe."

---

## Phase 4 — Sourcing & verification execution (2–4 weeks)
Operationalize [04](04_suppliers_and_companies.md) + [06](06_sourcing_rfq_templates.md):

1. Send **RFQ #1 (1450nm)** and **RFQ #2 (1927nm)** to: Jiangsu Unimed/YDUNVIE (direct), Focuslight (OEM module), and 2–3 clinic suppliers (Gigaalaser, Liton) for context.
2. Demand: K-number coverage, authorization letter, label/IFU/UDI, **calibrated output-measurement video**, single-vs-total energy clarification.
3. Cross-check any "FDA cleared" claim against the actual K-number applicant.
4. If buying a finished consumer unit: prefer an **authorized agent** with returns/warranty over a dropship store (OYAY-type).
5. Negotiate China benchmark (~¥3,000–3,400 ≈ $417–$472 at ~¥7.2/$1 for YDUNVIE A9) vs Western relabel premiums.

**Deliverable:** supplier scorecard (manufacturer-vs-trader, docs provided, real specs, price, MOQ, authorization) → a buy/no-buy recommendation.

---

## Phase 5 — Decision & protocol (a few days)
- **Final pick** (or "buy none — do in-office Perméa course + topicals" if evidence says home isn't worth it).
- **Usage/safety protocol** mirroring parent repo [06](../01_ipl_hair_removal/06_final_recommendation.md): cadence, ramp, cooling, SPF, contraindications, what to stop on.
- If commissioning OEM: a spec contract derived from RFQ answers.

---

## Open questions to resolve (carried forward)
1. Is **MimiSilk Iris == YDUNVIE Iris == Jiangsu Unimed K182498** the *same device*? (high-value: collapses 3 leads into 1)
2. Does **Iris Ice Plus** have any real output advantage over Iris Ice, or only UX/cert? (current evidence: probably not)
3. Is there a **buyable home 1927nm** device with credible PIH-safety data, or is in-office Perméa/Moxi the only safe pigment route?
4. What is the **real per-session and cumulative efficacy** of home NAF vs Clear+Brilliant? (Phase 3)
5. **Discontinued PaloVia/RéAura** — any new-old-stock or refurbished units worth acquiring to study/use?
6. **Eye safety** of cheap China home lasers near the periorbital area — independently verified or just claimed?

---

## How to run this efficiently
- This whole plan is a good fit for the repo's **deep-research** approach (multi-source, adversarially verified, cited) — e.g. invoke `/deep-research` per phase with the phase's guiding question.
- Mirror parent-repo discipline: **download primary PDFs into the repo**, label every claim ✅/⚠️/🔍, and force all specs into identical units before comparing.
- Keep the README TL;DR updated as each phase resolves ⚠️ → ✅/❌.
