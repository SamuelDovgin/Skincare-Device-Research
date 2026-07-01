# YDUNVIE / 欧莱美 Full Product Catalog Analysis

Source: indexed catalog pages from ydunvie.com.cn (the live .cn site was unstable during research). **~31 product names** confirmed across catalog pages.

> ⚠️ **Critical caveat:** product/category *names* are confirmed from indexed catalog pages; most detailed *specs* below are **inferred from category + naming + a few retail listings**, not verified spec sheets. Treat every spec as "demand the datasheet." See screening questions in [04_suppliers_and_companies §5](04_suppliers_and_companies.md).

**Company:** Wuxi/Jiangsu Olemy (欧莱美) Laser Technology → brand YDUNVIE / 易科美. Per 36Kr: skincare, skin detection, hair, gum, body/pain; wavelengths ~650nm–1927nm; "40+" products. FDA: K182498 (microbeam/fractional). Most credible technical strength = **home fractional laser skincare** (1450nm Iris + 1927nm Dora/Velar lines).

**Company facts (✅ verified this pass):**
- Brand 易科美/YDUNVIE launched in China **April 2014**; **first domestic (China) home-use 1450nm fractional laser** beauty device.
- Parent **合铼科技 (Helai)** raised a **tens-of-millions-RMB (≈ low-millions USD) Pre-A round** (36Kr, May 2024) — a funded, growing company, not a fly-by-night.

> 💱 *All ¥/RMB figures below include an approximate USD conversion at **~¥7.2 / $1** (mid-2026). Rates move — treat as ballpark.*
- **Three core (patented) technologies:** 纳米点阵 (nano-matrix microbeam) · 磁悬浮摆臂扫描 (magnetic-levitation scanning arm / frame-type **DynamicScan**) · 智能冷却 + 360° 环形冷凝冰晶 (intelligent cooling + 360° ring ice-crystal cooling).
- Marketing tagline: "院线同源" (*same-origin as clinic devices*) / "移动的私家美容院" (a mobile private salon).

---

## 0. Model-code map (the A-series) — read this first ⭐

The retail SKUs use **A-series codes** that don't appear on the English brand pages. This is the Rosetta stone for matching listings (JD/Tmall/Lazada/MimiSilk/myernk) to actual products:

| Code | Product name | Wavelength | What it is | China price | Best for |
|------|-------------|-----------|------------|-------------|----------|
| **A7** | **Iris** (纳米点阵嫩肤仪) | 1450nm ✅ | the **original** home fractional rejuvenation device; 360° semiconductor ice cooling, deep-dermal | ~¥3,998 (≈$555; JD ¥3,988 ≈ $554) | pores, eye wrinkles, acne scars, rough/sensitive skin, collagen |
| **A9** | **Iris Ice / Ice Crystal** (冰晶点阵) | 1450nm ⚠️ | the **flagship/premium upgrade** — denser/higher-coverage nano-array, full 360° ice-crystal cooling + DynamicScan; aimed at **stubborn acne pits + severe pores** | ~¥2,788–4,588 (≈$387–$637; promo ~¥3,000–3,400 ≈ $417–$472) | the "do it properly" 1450nm collagen/texture device |
| **A8** | **Dora / "大白"** (纳米点阵焕肤仪) | **1927nm** ⚠️ | the **pigment/brightening** device — point-matrix for melanin metabolism, freckles, dullness, even tone | ~¥2,300 (≈$319) China / ~$719 reseller | **pigment / PIH / brightening (your pigment goal)** |
| **MINI** | **Iris Mini** | 1450nm 🔍 | smaller/portable fractional | ~¥2,300 (≈$319) | budget/portable texture |
| **P5** | **Nova Plus** (三重光电祛痘) | multi-light 🔍 | triple-photoelectric acne device | ~¥1,580 (≈$219) | active acne |

> ⚠️ **Naming caution:** the English "Iris Ice **Plus**" (seen on OYAY/MimiSilk-adjacent listings) and the Chinese **A9 Iris Ice** may or may not be the exact same SKU — "Plus"/"Pro" suffixes on export listings often denote a region/bundle/firmware variant, not a hardware step-up (per [03](03_device_landscape.md), Iris and Iris Ice both cap ~12 mJ/pulse). **Confirm the A-code + spec sheet before assuming a "Plus" is stronger.**

**The short version for your decision:** the device you most likely want for **collagen/texture** is the **A9 Iris Ice (1450nm)**; for **pigment** it's the **A8 Dora (1927nm)**. MimiSilk sells the **1450nm Iris** (see §G) — *not*, as far as I can tell, a 1927nm Dora.

---

## A. Tender Skin / 嫩肤 — the 1450nm fractional collagen/texture line ⭐ most relevant

| Model | Likely role | Confidence | Notes |
|-------|-------------|-----------|-------|
| **Iris** *(A7)* | original 1450nm nano-fractional | ⚠️ | 360° semiconductor ice cooling, deep-dermal; ~¥3,998 (≈$555). The base model MimiSilk appears to resell (§G). |
| **Iris Ice** *(A9)* | **flagship** 1450nm nano-matrix fractional w/ cooling | ⚠️ best-documented | 180 J full-face, DynamicScan, ~1.1 µm dot spacing, 133 ms pulses, 3 modes, "Smart Cool" ~6 s, depth ~300/350/400 µm, ~10 min full-face, 3 treatments/charge. **The flagship to care about.** |
| **Iris FR** | fractional-rejuvenation variant | 🔍 name only | "FR" likely fractional resurfacing; ask wavelength/cooling/energy/depth |
| **Iris Ice Plus** | export "upgrade" of Iris Ice | ⚠️ | 3–12 mJ/pulse; **probably not stronger** — upgrades look like cooling/sensors/app/zones/cert, not raw output (both cap ~12 mJ). May just be a region/bundle label for A9. |
| **Iris Mini** *(MINI)* | smaller/portable | 🔍 | ~¥2,300 (≈$319); likely lower energy / slower full-face |
| **R10** | skin-rejuv device | 🔍 generic name | confirm modality (1450/1927/LED/RF?) before assuming |
| **R10 RS** | revised R10 | 🔍 | "unknown but newer"; get datasheet |
| **Muse** | 纳米点阵嫩肤 (nano-fractional) | ⚠️ | if truly 1450nm nano-fractional, overlaps Iris; differentiator = energy/cooling/scan/time |

**Targets for this line:** pores, texture, oiliness, acne marks, early fine lines, shallow pitted marks, collagen. **Best fit for the collagen/texture goal.**

---

## B. Skin Renewal / 焕肤 — the 1927nm pigment/brightening line ⭐ most relevant for *pigment*

| Model | Likely role | Confidence | Notes |
|-------|-------------|-----------|-------|
| **Dora** *(A8 / "大白")* | base 1927nm renewal/brightening | ⚠️ | **1927nm point-matrix laser**, melanin metabolism, freckles, dullness, even tone; 3 gears, 2–3×/week, 20–25 min/session, inductive charging, vibration, "cherry-blossom pink"; ~¥2,300 (≈$319) China / **~$719 reseller**, 1-yr warranty. **Home Perméa/Moxi analog.** |
| **Dora Plus** | upgraded Dora | 🔍 | more modes / energy / cooling? |
| **Dora Pro** | top-end Dora | 🔍 | most interesting for **pigment/brightness** if 1927nm confirmed |

> ⚠️ **The recurring Dora wavelength inconsistency:** retail copy headlines "1927nm" but some body text says "1450nm." Likely sloppy copy reuse from the Iris template — but **this is the single most important spec to confirm for your pigment goal.** A real 1927nm = correct pigment physics; if it's actually 1450nm it's just another collagen device. Demand the rating label / spec sheet before buying.

**Targets:** pigment, PIH, dullness, uneven tone, brightening — **best wavelength match for the user's pigment goal.** Caution: 1927nm can worsen PIH if poorly dosed.

---

## C. Wrinkle Reduction
| Model | Likely role | Confidence |
|-------|-------------|-----------|
| **Zen** | dedicated fine-line device | 🔍 modality unknown (laser? IR? RF? LED?) — ask wavelength/fluence/depth |

---

## D. Whitening / Brightening (7 products)
| Model | Likely role | Notes |
|-------|-------------|-------|
| **Velar Precision** | targeted spot/brightening | small window for spots/freckles — verify source (1927? LED? VCSEL?) |
| **Velar Max** | wider/stronger brightening | "Max" ≠ proven higher fluence — ask energy + area |
| **Velar Light** | entry-level brightening | gentler, maintenance |
| **Velar Smooth** | brightening + texture-smoothing | may overlap 1927nm renewal |
| **VCSEL Light** | VCSEL-based light | more "laser-like" than LED, gentler than fractional; ask wavelength/coherence/target |
| **Velar Mask** | wearable brightening mask | lower-risk, lower-power |
| **LED Mask** | LED mask | least aggressive; good for redness/inflammation/acne support, **weak for true pigment removal** |

---

## E. Acne (4 products)
| Model | Likely role | Notes |
|-------|-------------|-------|
| **Nova** | base acne device (iF Design: "Advance Acne Clearing Device") | ask wavelength: ~415nm blue (C. acnes), ~630–660nm red (inflammation), NIR (healing) |
| **Nova Plus** | "三重光电祛痘" (triple photoelectric) | more serious than single-LED wand; ask the 3 modalities |
| **Nova Pro** | higher-end | verify acne type targeted |
| **Nova Max** | highest-power/largest-area | safety docs matter if heat/laser-based |

---

## F. Other categories (lower priority for skin-quality goal)
| Category | Models | What they likely are |
|----------|--------|----------------------|
| **Penetration** | Iontop H | iontophoresis / active-ingredient delivery (companion, not resurfacing) |
| **Pain Relief** | Relax Light, Relax Smooth | likely 830nm IR / photobiomodulation; ask mW/cm² + J/cm² |
| **Hair Removal** | Remo Max / Light / Smooth / Precision | likely IPL; judge by J/cm², filter, pulse width, cooling, skin-tone sensor |
| **Hair Regrowth** | Reju Max / Precision / Light | red-light/laser scalp therapy; ask wavelength, diode count, output, format |
| **Gum Protection** | Rete Precision | oral/gum photobiomodulation — needs dental regulatory docs |
| **Desktop / Pro** | Premium A | multifunction platform — confirm home vs salon vs medical |
| **Oral platform** | Smile Clear | multifunction oral/teeth/gum laser platform |
| **Skin analysis** | AI Derma Mirror | AI skin-analysis camera (diagnostic, **not treatment**) — for salon/retail demos |

---

## G. Is MimiSilk just a rebranded YDUNVIE? — and how to buy

**MimiSilk Iris (✅ specs pulled this pass):** 1450nm, **12 mJ single-beam max** ("~¼ of clinical-equipment energy"), **100 µm × 30 µm microbeam**, targets dermis ~300–600 µm (acne marks ≤200 µm), **5–10 min full-face**, **$599** (reg $699), **2-yr warranty + 90-day money-back**, ships to US/CA/AU/EU + selected Asia. Claims "FDA-Cleared" (**no K-number given**), self-describes as **"MimiSilk (Danish beauty science)."** (MimiSilk holds no patents of its own — [14](14_mimisilk_iris_tria_patent_analysis.md) has a claim-by-claim, ⚠️ not-legal-advice read of whether it might read on Tria's still-active patents instead.)

**The verdict on the rebrand question:**
- The **spec fingerprint is essentially identical to the YDUNVIE Iris (A7)**: same 1450nm, same ~12 mJ ceiling, same 100 µm microbeam, same fractional acne-mark/pore/fine-line indications. That's a strong match — consistent with the Reddit/myernk trail that MimiSilk = a relabeled YDUNVIE/Jiangsu Unimed device.
- **BUT** MimiSilk's own page shows **zero** YDUNVIE / Jiangsu Unimed / China references and markets itself as **"Danish."** So the link is *inferred from spec-matching*, not disclosed. 🔍
- **What MimiSilk corresponds to:** the **1450nm Iris (A7)** — *not* clearly the premium **A9 Iris Ice**, and **not** a **1927nm Dora**. MimiSilk lists only a 1450nm device (alone or bundled with PDRN masks). **If you want the 1927nm pigment device, MimiSilk likely can't supply it.**

**Two purchase paths (per your plan):**

| Path | Pros | Cons | Best when |
|------|------|------|-----------|
| **Direct from manufacturer** (Jiangsu Unimed / YDUNVIE / 易科美) | full model range incl. **A9 Iris Ice** *and* **A8 Dora 1927nm**; lowest unit price (~¥3,000–3,400 ≈ $417–$472); can request real spec sheet + K-number | MOQ/import/language friction; warranty/returns harder; must verify authorization | you want the **1927nm Dora**, the true **A9**, or multiple units / OEM |
| **MimiSilk** (Western storefront) | English support, **2-yr warranty + 90-day money-back**, ships to US/EU/etc., turnkey | **~$599** (premium over China); only the **1450nm Iris**; "Danish" claim obscures origin; **no K-number disclosed** | you want the **1450nm collagen/texture device** with hassle-free returns and don't need 1927nm |

**Before buying either, get in writing:** (1) the **A-code** of the exact unit, (2) **wavelength on the rating label** (critical for Dora — confirm 1927nm), (3) the **FDA K-number** it ships under (likely K182498) and whether it covers *that* model, (4) mJ/pulse vs full-face-J clarified, (5) cooling spec, (6) Fitzpatrick/skin-tone limits. See [06 RFQ](06_sourcing_rfq_templates.md).

> **For your stated goals:** if pigment is the priority → you need the **A8 Dora (1927nm)**, which means **manufacturer-direct** (MimiSilk doesn't sell it). If collagen/texture is the priority → **MimiSilk Iris** (≈ A7) is the low-friction buy, or **A9 Iris Ice** direct if you want the denser flagship.

---

## Channel & price summary (1450nm Iris family)

| Channel | Product | Price | Notes |
|---------|---------|-------|-------|
| China retail (JD/Tmall/SMZDM) | A9 Iris Ice / A7 Iris | ¥2,788–4,588 (≈$387–$637; promo ~¥3,000–3,400 ≈ $417–$472) | cheapest; domestic |
| Dealmoon (cross-border) | A7-Iris | ¥5,982 (≈$831) / CA$3,988 | indexed export |
| myernk (HK, "authorized agent") | YDUNVIE Ice Crystal | ~$580 | + also lists Iluminage (see [03](03_device_landscape.md)) |
| MimiSilk | Iris (1450nm) | $599 (reg $699) | 2-yr warranty, 90-day refund, Western support |
| OYAY | Iris Ice Plus | $999 | dropship; avoid unless authorization proven |
| jofioubeauty | A8 Dora "大白" (1927nm) | ~$719 | a reseller path for the **pigment** device |

---

## Priorities for the user's goals
1. **Dora / Dora Plus / Dora Pro (1927nm) = A8** — best wavelength for **pigment/PIH/brightening** (manufacturer-direct or jofiou; **not** MimiSilk)
2. **Iris Ice = A9 (1450nm)** (or base **Iris = A7** via MimiSilk; also Muse / Iris FR) — best for **pores/texture/acne marks/fine lines/collagen**
3. **Nova Plus / Pro / Max** — if active acne/post-acne inflammation is a concern
4. *Deprioritize:* LED/VCSEL masks (maintenance only), and all Remo/Reju/Relax/Rete/Smile/Premium/AI-Mirror lines for this goal

**Before buying anything from this catalog, get a spec sheet with:** exact wavelength ±tol, laser/LED type, mJ/pulse and/or J/cm² (and whether single-pulse or total), spot size, fractional density, pulse width, cooling temp, treatment depth, eye-safety design, Fitzpatrick limits, certifications (K-number/CE/IEC 60825-1/60601/ISO 13485), clinical data, contraindications.

---

### Sources
- [36Kr/QQ: 「易科美」first domestic home 1450nm fractional laser; Pre-A funding (May 2024)](https://news.qq.com/rain/a/20240527A02UCJ00) · [易科美 Baidu Baike](https://baike.baidu.com/item/%E6%98%93%E7%A7%91%E7%BE%8E/22948298)
- [美容仪之家 YDUNVIE Iris spec page (A7, ¥3,998 ≈ $555; lists MINI, A8, P5)](https://www.imeirongyi.com/product/information/ydunvie-iris.html) · [Zhihu "院线同源易科美冰晶" review](https://zhuanlan.zhihu.com/p/663240311)
- [Lazada: Ydunvie **A9** Ice Crystal Dot Matrix Laser](https://www.lazada.sg/products/ydunvie-a9-ice-crystal-dot-matrix-laser-beauty-meter-ipl-device-shrink-pores-flat-pox-pits-light-acne-marks-ydunvie-i3209669909.html) · [Dealmoon A7-Iris (¥5,982 ≈ $831)](https://www.dealmoon.com/product/-ydunvie-a7-iris/3541987)
- [jofioubeauty: Ydunvie **A8** 大白/Dora 1927nm ($719)](https://www.jofioubeauty.com/zh-usa/products/ydunvie-%E6%98%93%E7%A7%91%E7%BE%8E%E5%A4%A7%E7%99%BD%E7%B4%8D%E7%B1%B3%E9%9B%B7%E5%B0%84%E6%BF%80%E5%85%89%E7%85%A5%E8%86%9A%E5%84%80-%E5%8E%BB%E9%9B%80%E6%96%91-%E7%BE%8E%E7%99%BD%E6%8F%90%E4%BA%AE%E5%AE%B6%E7%94%A8%E7%BE%8E%E5%AE%B9%E5%84%80-1) · [MimiSilk Iris ($599)](https://www.mimisilk.com/products/mimisilk-iris-1450nm-advanced-skin-renewing-device)
- iF Design Award (YDUNVIE devices); SMZDM/Tmall/JD listings (retail specs ⚠️ unverified)
