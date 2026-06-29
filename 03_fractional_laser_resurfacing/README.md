# Home Laser Resurfacing Research

Research thread: finding an **at-home device that improves skin quality — pigmentation/PIH, tone/brightness, and long-term collagen/fine lines** — ideally approaching what an in-office **Clear + Brilliant** delivers.

> **Distinct from the parent repo.** The top-level `IPL Device Research` project is about **broadband IPL for hair removal + redness**. This subfolder is a *different device class*: **non-ablative fractional infrared lasers** (Clear + Brilliant, Fraxel, Tria, NIRA, YDUNVIE). Different chromophore (water, not melanin/hemoglobin), different goal (resurfacing/collagen, not hair).

## TL;DR

1. **The category you want is *non-ablative fractional infrared laser*.** Clear + Brilliant is the in-office benchmark. Home members: **Tria FRX, PaloVia, Philips RéAura, MimiSilk Iris, YDUNVIE Iris Ice/Dora.** NIRA, LYMA, JOVS and LED masks are a *gentler adjacent category* — not true resurfacers. See [01](01_laser_resurfacing_science.md).
2. **Match wavelength to the problem:** **1927nm = pigment/brightness** (superficial — Perméa/Moxi/LaseMD; home = YDUNVIE **Dora**). **1450nm = collagen/texture** (deeper — C+B Original/Fraxel; home = **Tria FRX**, YDUNVIE **Iris Ice**). See [01](01_laser_resurfacing_science.md) §2. **For a 25-yo whose priority is pigment → 1927nm is the evidence-based pick** (1450nm is better-studied but for *acne/collagen*, not pigment); full head-to-head + recommendation in [09](09_1927nm_vs_1450nm_headtohead.md).
3. **A home device cannot equal Clear + Brilliant — and the quantified reason is NOT energy, depth, or beam diameter.** Per-microbeam energy is genuinely similar (home 5–12 mJ vs C+B 4–9 mJ ✅), **depth is set by wavelength** (all 1440/1450nm devices ≈ equal, ~300–450 µm), and **per-column fluence even favors home** (small ~100 µm spot at 12 mJ ≈ 150 J/cm² > C+B 140 µm/9 mJ ≈ 58 J/cm²). **The gap is coverage density per session + supervised dose control.** C+B treats ~10% coverage / ~650–1,270 MTZ/cm² per session; back-calculating from "180 J full-face," a home Iris/MimiSilk/Tria device delivers only **~30–180 MTZ/cm² (~0.3–1.5% coverage) — roughly 10–30× less density per session.** Full math + cross-checks in [08 §3b](08_clear_brilliant_quantified_gap.md); expectations in [02](02_in_office_vs_at_home.md).
4. **Most trustworthy home buy = Tria FRX** (✅ FDA K130459, 1450±50nm fractional, real company). **Best pigment-wavelength home option = YDUNVIE Dora (1927nm)** ⚠️ but unverified. **For pigment specifically, topicals + SPF still beat any home laser** (parent [07](../01_ipl_hair_removal/07_alternatives_and_strategy.md)).
5. **The likely China factory behind the "Iris" devices = Jiangsu Unimed / YDUNVIE / 易科美 / Olemy** (✅ FDA K182498; funded company, China's first home 1450nm fractional laser). **Model-code map:** **A9 = Iris Ice** (1450nm flagship, collagen/texture), **A8 = Dora** (1927nm, pigment/brightening), A7 = base Iris. **MimiSilk Iris (~$599) ≈ the 1450nm Iris (A7) by spec-fingerprint** but markets itself as "Danish" and sells *no* 1927nm version — so **for the pigment (Dora/1927nm) device you'd need manufacturer-direct.** Full breakdown + purchase paths in [05](05_ydunvie_catalog.md). See also [04](04_suppliers_and_companies.md).

## Documents

| # | File | What it covers |
|---|------|----------------|
| 01 | [Laser resurfacing science](01_laser_resurfacing_science.md) | Device taxonomy (ablative/fractional/setting), water-as-chromophore physics, 1450 vs 1927nm, fractional vs warming, efficacy specs, the unit traps, PIH safety |
| 02 | [In-office vs at-home](02_in_office_vs_at_home.md) | **Clear + Brilliant (✅ verified specs) vs home devices — what's different, what to realistically expect** for pigment + collagen |
| 03 | [Device landscape](03_device_landscape.md) | **Every comparable home/discontinued device ranked** (Tria, PaloVia, RéAura, MimiSilk, YDUNVIE Iris/Dora, OYAY, NIRA, Iluminage, LYMA, JOVS, DermRays) + clinical relatives |
| 04 | [Suppliers & companies](04_suppliers_and_companies.md) | **Jiangsu Unimed/YDUNVIE deep profile + China supply chain + FDA 510(k) supplier map** + where they sell, China pricing, Alibaba matching, screening + red flags |
| 05 | [YDUNVIE catalog](05_ydunvie_catalog.md) | **All ~31 YDUNVIE products** analyzed line-by-line (Iris, Dora, Velar, Nova, etc.) |
| 06 | [Sourcing & RFQ templates](06_sourcing_rfq_templates.md) | Copy-paste RFQs (1450nm / 1927nm / 1064nm / VCSEL), universal spec sheet, screening, standards |
| 07 | [Future research plan](07_future_research_plan.md) | **Phased plan** to verify specs, map the market, review clinical efficacy, source & decide |
| 08 | [The quantified gap](08_clear_brilliant_quantified_gap.md) | **Dermatology evidence: exactly how Clear + Brilliant differs from home devices.** Energy ≈ similar, depth ≈ wavelength-set, beam diameter/fluence ≈ matched (even favors home) — **the gap is density/coverage + dose control**, quantified with numbers |
| 09 | [1927nm vs 1450nm head-to-head](09_1927nm_vs_1450nm_headtohead.md) | **Wavelength decision for a 25-yo, pigment-focused user.** The evidence comparison + recommendation: 1450nm is better-studied *for acne/collagen*, but **1927nm is the evidence-based pigment wavelength** |
| 10 | [Where to buy — storefronts](10_where_to_buy_storefronts.md) | **Every storefront selling each device**, with all YDUNVIE models (A7/A9/Dora) by channel + price, dropship tells, and how to buy without getting burned |
| 11 | [Subscriber Q&A — low-density rejuvenation](11_subscriber_qa_lowdensity_rejuvenation.md) | A reader's "month-of-home ≈ one C+B?" question + **how a laser-specialty derm would answer and why** (coverage ≠ remodeling); includes a short drafted reply |
| 12 | [Alibaba supplier scan (live)](12_alibaba_supplier_scan.md) | **Live Alibaba browse:** no consumer handheld exists there; YDUNVIE/Focuslight absent; 6 md04 clinic-machine suppliers confirmed + OEM laser-module sources (incl. a 1440nm diode chip) |
| 13 | [Tria SmoothBeauty owner's guide](13_tria_smoothbeauty_owners_guide.md) | **The device in hand, ID'd + spec'd from its primary-source manuals** (PDFs mirrored in `tria_smoothbeauty/`). SmoothBeauty = Age-Defying = FRX (model SRL, ✅ FDA 2013). ✅ verified specs (1440nm, 5–12 mJ, Class 1), coverage/density estimate, indication-vs-marketing reality, and a full **quick-start + 12-week protocol** |

## Confidence legend
✅ **Verified** (FDA 510(k) / peer-reviewed / official spec) · ⚠️ **Marketing claim** (seller/brand, unconfirmed) · 🔍 **Inferred** (from wavelength/category)

> **Provenance & honesty note.** This folder organizes a prior research conversation (much of it from brand/marketing pages, which are error-prone). The **anchor facts were re-verified** against FDA filings and clinical sources during this pass (Clear+Brilliant, NIRA, Tria, PaloVia, RéAura, Jiangsu Unimed K182498). Everything still marked ⚠️/🔍 needs primary-source confirmation — that's exactly what [07](07_future_research_plan.md) is for. Treat ⚠️ specs (esp. YDUNVIE/OYAY/MimiSilk numbers) as *claims to verify*, not facts.

## Status / open items
- **Verified this pass:** Clear+Brilliant Touch (1440/1927nm specs), NIRA (K163137/K222685), Tria FAN (K130459), PaloVia (K090525), RéAura (1435nm+Solta), Jiangsu Unimed (K182498 valid).
- **Tria specs upgraded ⚠️→✅ from primary-source IFU** ([13](13_tria_smoothbeauty_owners_guide.md)): SmoothBeauty/Age-Defying/FRX are one device (model SRL) — 1440nm diode, **5–12 mJ/pulse**, Class 1, indication = periorbital wrinkles only (IFU explicitly **not** for pigment/dyschromia/freckles/veins). Manuals mirrored at `tria_smoothbeauty/source_docs/`.
- **Partially resolved:** MimiSilk Iris ≈ YDUNVIE Iris (A7) by spec-fingerprint (1450nm, 12 mJ, 100 µm microbeam), but MimiSilk doesn't disclose the YDUNVIE/Jiangsu Unimed link (claims "Danish") and sells only the 1450nm model. Model codes mapped: A9=Iris Ice, A8=Dora(1927nm), A7=Iris. See [05](05_ydunvie_catalog.md).
- **Open (high-value):** Confirm **Dora is truly 1927nm** (retail copy conflicts with 1450nm) — *the* spec for the pigment goal. Does Iris Ice **Plus**/A9 out-perform base Iris or just add UX/cert? Real clinical efficacy of home NAF vs Clear+Brilliant? Buyable 1927nm home device with credible PIH-safety data? → [07](07_future_research_plan.md).
- **Not yet done:** primary 510(k) PDFs not yet mirrored into the repo (planned in Phase 1).
