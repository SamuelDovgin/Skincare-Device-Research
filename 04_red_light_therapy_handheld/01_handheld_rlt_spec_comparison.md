# Handheld Red Light Therapy (RLT) Devices — Spec Comparison & Ranking

**Buyer profile:** Handheld RLT device for **hands, back pain, and carpal tunnel pain**. Wants **~5W LEDs**, **classic red + near-infrared (NIR)** wavelengths.
**Compiled:** 2026-06-29 · updated 2026-06-30 · Source: 12 Alibaba listings (text specs + specs OCR'd from listing images where available). L1-L11 listing images are archived in `listing_images/`; L12 is text-only from a supplied Alibaba page capture. *(L10 Redfy + L11 SunPlus added 2026-06-29; L12 Ideatherapy RL-series added 2026-06-30.)*

> **How to read this:** Alibaba listings hide most real specs inside the product *images* (infographics), not the text fields. Every number below was pulled either from the listing's key-attributes text or read directly off the listing photos. Where a spec only appears in the title/marketing and is **not** backed by a spec table, it's flagged as *(claim only)*. "not stated" means it appears nowhere — which, for irradiance and certifications, is itself a red flag.

> **Independent check added:** I re-checked the archived listing images directly and compared the top candidates against current indexed Alibaba/manufacturer pages where available. The deeper audit, evidence review, dose math, and my final call are in **[03_independent_research_and_decision.md](03_independent_research_and_decision.md)**.

---

## My final decision

If I were buying for the stated use case today, I would buy **L1 — AZURETHERAPY AL60**.

Why: it has the cleanest combination of true handheld form factor, 660/850nm wavelengths, a documented **190 mW/cm² at contact**, USB-C cordless use, the strongest certificate trail, and a matching manufacturer presence outside the original Alibaba page. It is not a true "12 individual 5W LEDs" device — its own spec says 24 chips / 60W — but its documented irradiance matters more than the wattage label.

**L2 — Ideatherapy RTL12-C** is the only listing I would seriously cross-shop. Its archived distance measurements are excellent, but current indexed RTL12-C pages do not all describe the exact same wattage/battery/charging package. Ask the supplier to confirm exactly which RTL12-C version ships and send fresh meter photos before choosing it over L1.

**The added contenders don't change this.** **L10 (Redfy RT60, $15.22)** is the strongest *value* play — a credible manufacturer, the same dual-chip 660/850 architecture as L1, cordless with pulse control, and the truest "5W red+NIR" match to the original brief — but it publishes **no irradiance**, so it can't displace L1 on proof. **L11 (SunPlus, $45.28)** has the **best certification wall of the image-archived set** (incl. ISO 13485) yet also discloses no irradiance and leans on a spec table that belongs to a different model. **L12 (Ideatherapy RL-series, $44-109, MOQ 3)** is not IPL and not a clean handheld candidate: it is a red/NIR LED lamp/listing family with no model-specific irradiance, power, battery, size, or certification data in the supplied page text. All three are "ask for a meter reading first" buys. See the head-to-head section for the full reasoning.

---

## ⚡ TL;DR ranking for your use case (hands / back / carpal tunnel)

| Rank | Device | Why | Price (1 pc) |
|------|--------|-----|--------------|
| 🥇 1 | **L1 — AZURETHERAPY AL60** | Highest *documented* irradiance (190 mW/cm²), complete spec sheet, best certifications, cordless 5000mAh USB-C, real established supplier, 2-yr warranty | **$30** |
| 🥈 2 | **L2 — Ideatherapy RTL12-C** | Most *honest* data (irradiance given at 3 distances), quality aluminum build, genuine handheld, named brand | ~$36–71 (MOQ 3) |
| 🥉 3 | **L7 — MINI60PRO (desktop)** | Best wavelength coverage (4 WL incl. 830+850 for depth), **only one with CE/FCC/RoHS on the label**, includes goggles | $69–89 |
| 4 | **L10 — Redfy RT60** ⭐NEW | Same dual-chip architecture as L1 from a *credible* large RLT maker, cordless 4000mAh, **frequency-adjustable**, cheapest credible option — **but irradiance undisclosed** | **$15.22** |
| 5 | **L11 — SunPlus** ⭐NEW | **Broadest certification wall of the image-archived set** (incl. ISO 13485 medical QMS), solid build + 4000mAh — but priciest mini, no irradiance, and its spec table is for a *different model* | $45.28 |
| 6 | **L6 — Mini Panel 660/850** | Looks like the same hardware as L1 (130×85, 5000mAh, USB-C) but cheaper — a budget gamble with thin documentation | $22.80 |
| 7 | **L5 — Traveler Mini Panel** | Feature-rich & lightweight (magnetic back, kickstand, pulse, 301 g), explicit 3W 3030 LEDs, but no irradiance/certs | $17.83 |
| 8 | **L3 — 12pcs "8W" Panel** | Best controls (pulse Hz, dimming, lock, biggest 10000mAh battery) but 8W is title-only and no irradiance; handle costs extra | $16.90 |
| 9 | **L4 — 60W 3-wavelength** | Cheapest, only genuine 5W-per-LED *claim* + unique 1060nm, but **zero spec images** and implausible attributes — buying blind | $8.30 |
| 10 | **L8 — Face Panel w/ goggles** | Marketed "handheld" but a 220×210×80mm brick on a stand; inconsistent stock photos; no performance specs | $13.60+ |
| 11 | **L12 — Ideatherapy RL-series** ⭐NEW | Credible 12-year supplier; 660/850nm, 30° beam, remote/standing lamp listing — but text-only, multi-variant, **no irradiance**, and MOQ 3 | $44-109 |
| ❌ 12 | **L9 — MINI60PRO (standing)** | Same family as L7 but **wholesale only (MOQ 51–101 pcs)** — not buyable as a single unit | $62 (51+ pcs) |

---

## 🔬 The "5W LED" reality check (read this first)

You asked for **5W lights**. Here's the honest situation across these listings:

- **Genuine high-power LEDs come in two physical forms:** large single emitters with a **secondary domed/collimating lens** (the "5W look" — big clear bubbles over each diode) vs. flat **SMD chips** (e.g., "3030", "5050") sitting flush on a board. The domed-lens devices here are **L1, L4, L6** (and L2 uses focusing reflectors).
- **Per-diode wattage is rarely what's advertised.** Most of these pack **two chips (660nm + 850nm) into one lens**, so "12 LEDs / 60W" is really **24 chips ≈ 2.5W each**, not 5W. That's the case for **L1** (24 chips/60W) and **L6**.
- **Only L4 actually implies ~5W/diode** (60W ÷ 12 single lenses) — but L4 has *no spec images at all* and lists an implausible "iron / 1 kg" body, so that 5W is an unverified marketing number.
- **L10 (Redfy) explicitly markets "12pcs × 5W Medical LED"** — the literal 5W label you wanted — but those 12 are **dual-chip lenses** (660+850 under one optic), so it's the *same* ~2.5W/chip reality as L1, and there's **no spec table or irradiance** to back the 60W figure.
- **L5 is explicit: 3W "3030" LEDs.** A 3030 package physically can't sustain 5W, so this is a believable 3W — just not what you asked for.
- **L3 claims "8W"** in the title only, over small SMD packages — almost certainly a peak/marketing figure.
- **L11 (SunPlus) states no per-LED wattage at all** for the handheld (its spec table belongs to a different 48W panel).
- **L12 (Ideatherapy RL-series)** lists LED-count options (**12/24/27/35 pcs**) and wavelengths (**660/850nm**) but does not tie those options to model names, power draw, battery status, irradiance, or dimensions. It is a listing family, not a verified single device spec.

**Bottom line:** Don't chase the "5W" label — it's mostly marketing and inconsistently defined. **Irradiance (mW/cm²) at a stated distance is the spec that actually determines your dose and how deep the light reaches** (which is what matters for carpal tunnel and back pain). Rank by irradiance + honest documentation, not by the wattage sticker. By that logic the domed-lens, high-irradiance units (**L1**, and **L2**'s focused design) are your best "high-power" bets even though they're ~2.5W/chip.

---

## 📊 Master spec comparison

| Spec | L1 AZURETHERAPY AL60 | L2 Ideatherapy RTL12-C | L3 "8W" Panel | L4 60W 3-WL | L5 Traveler Mini | L6 Mini 660/850 | L7 MINI60PRO desk | L8 Face Panel | L9 MINI60PRO stand | L10 Redfy RT60 | L11 SunPlus | L12 Ideatherapy RL-series |
|------|------|------|------|------|------|------|------|------|------|------|------|------|
| **Type** | Handheld | Handheld | Handheld | Handheld | Handheld + kickstand | Handheld | Desktop/portable | Panel on stand | Standing | Handheld + stand | Handheld + kickstand | Standing/portable lamp listing |
| **Wavelengths** | 660 / 850 | 660 / 850 | 660 / 850 | 660 / 850 / **1060** | 660 / 850 | 660 / 850 | **630/660/830/850** | 660 / 850 | **630/660/830/850** | 660 / 850 (1:1) | 660 / 850 | 660 / 850 |
| **LEDs** | 12 lenses / **24 chips** | 12 modules | 12 (multi-die) | 12 lenses | **40 pcs** (~35 visible) | 12 dual-chip | 12 dual-chip | 13 lenses | 12 lenses | 12 dual-chip lenses | 12 domed lenses | **12 / 24 / 27 / 35 pcs** options |
| **Power/LED** | ~2.5W/chip | not stated | 8W *(claim only)* | ~5W *(claim only)* | **3W** (3030) | not stated | not stated | not stated | not stated | **5W** *(claim only)* | not stated | not stated |
| **Total power** | **60W** | not stated | not stated | 60W *(claim)* | nominal 120W / ~18W real | not stated | **15W rated** | not stated | "60W" *(name only)* | 60W *(claim)* | not stated *(table = wrong model)* | not stated |
| **Irradiance** | **190 mW/cm² @ contact** | **110@3in / 94@5in / 64@6in** | not stated | not stated | not stated | 110 mW/cm² *(text only)* | >130 mW/cm² *(no distance)* | not stated | not stated | **not stated** | **not stated** | **not stated** |
| **Beam angle** | 30° | focusing optics | not stated | not stated | not stated | collimator | not stated | not stated | not stated | domed optics | domed optics | 30° |
| **Battery** | 5000mAh, USB-C | built-in, micro-USB | **10000mAh**, USB-C | ambiguous | 5000mAh, DC9V/2A | 5000mAh, USB-C | rechargeable, micro-USB | rechargeable, USB-C | rechargeable | 4000mAh, cordless | 4000mAh, cordless | not stated; AC input listed |
| **Input** | 5V | not stated | not stated | AC110–240V | DC 9V 2A | not stated | 9V | not stated | not stated | not stated | not stated | **100–240V AC** |
| **Size (mm)** | 130×85×30 | ~76×150×30 | not stated | not stated | 142×101×30 | 130×85×40 | 150×95×38 | **220×210×80** | 150×95×38 | not stated | not stated | not stated |
| **Weight** | not stated | not stated | not stated | "1KG" *(suspect)* | **301 g** | not stated | not stated | not stated | not stated | not stated | not stated | not stated |
| **Timer / modes** | brightness + countdown | countdown + R/NIR | **timer 1–20m, 4 dim, pulse 0–9999Hz, R/NIR/Both, lock** | timer, Red/NIR/Mode | timer, pulse, modes | 2 buttons | timer + pulse, 3 modules | **timer 5–30m, 5 levels, 3 modes+pulse** | timer, 2 buttons | dimmable + **frequency-adjustable** | adjustable brightness + timer | remote control *(title claim)* |
| **EMF / flicker** | 0µT@3in / no flicker | "EMF 0.0" photo | not stated | not stated | not stated | not stated | not stated | not stated | not stated | not stated | not stated | not stated |
| **Lifespan** | 100,000 hrs | not stated | not stated | not stated | not stated | not stated | not stated | not stated | not stated | not stated | not stated | not stated |
| **Certifications** | **FCC, ETL, CE, UKCA, RoHS, TGA, Global-Mark** | none listed (2yr warr.) | none | none | none | none | **CE, FCC, RoHS** | none | none | factory-level: MDSAP/TGA/ISO/FCC/CE/RoHS *(not unit-specific)* | **ISO 9001, ISO 13485, MDSAP, TGA, ETL, TÜV, CE, FCC, RoHS, PSE, SGS** | not listed in supplied text |
| **In the box** | device, USB cable, zip case, manual | device, USB cable | device, cable, pouch, manual | not stated | device, gift box, manual | not stated | device, adapter, **goggles**, manual | device, **goggles** | device, cable+US plug, **goggles** | device, EVA carry case | not stated | not stated |
| **Price (1 pc)** | $30 ($27 @1k+) | ~$36–71 | $16.90 | $8.30 | $17.83 | $22.80 | $69–89 | $13.60+ | $62 (51+ pcs) | **$15.22** ($30–55 tiers) | $45.28 (20% off $56.60) | $44-109 |
| **MOQ** | 1 | **3** | 1 | 1 | 1 | 1 | 1 | 1 box | **51–101** | 1 | 1 | **3** |
| **Warranty** | **2 years** | 2 years | not stated | not stated | not stated | not stated | not stated | not stated | not stated | not stated | not stated | not stated |

---

## 🏆 Irradiance ranking (the spec that matters most)

Irradiance drives both **dose** (how long a session takes) and **penetration depth** (how much reaches a wrist nerve or back muscle). Higher = better, *but compare at the same distance*:

1. **L1 — 190 mW/cm² @ contact** — highest disclosed, but measured at 0 in (skin contact), so it flatters vs. others.
2. **L7 — >130 mW/cm²** — no distance given, so not directly comparable (and only 15W total makes a high number doubtful).
3. **L2 — 110 @ 3in, 94 @ 5in, 64 @ 6in** — **the most trustworthy figure** because it's reported at multiple real distances. At contact it would likely exceed L1.
4. **L6 — 110 mW/cm²** — text only, not shown on any image.
5. **L3, L4, L5, L8, L9, L10 (Redfy), L11 (SunPlus), L12 (Ideatherapy RL-series) — not stated** — unknown dose; you can't plan treatment time, and it suggests the vendor either didn't measure or doesn't want to. (Notably, the added entries — despite L11's big cert wall, L10's credible factory, and L12's 12-year supplier — disclose **zero irradiance**.)

For pain/deep tissue, you want strong **850nm** output and irradiance in roughly the **100+ mW/cm²** range at the distance you'll actually use it (which, for hands/wrist, is **contact** — favoring L1/L2/L6).

---

## 🆚 The added contenders — does any one win? (head-to-head reasoning)

You asked for the reason each one is best, or what beats it and why. Here it is, measured against the same yardstick used for everything else: **documented irradiance > honest documentation > correct red+NIR wavelengths > handheld ergonomics > certs/value.**

### L10 — Redfy RT60 → lands at #4. Beaten by L1, L2, L7.
**What it has going for it (and why it could have been #1):**
- It's the **closest match to what you actually asked for**: explicitly sold as **"12pcs × 5W Medical LED"**, 660+850nm, cordless. On paper it's the "5W red+NIR handheld" you described.
- **Redfy is a real, large contract manufacturer** (17+ yrs, claims Fortune-500 clients, 8,230 m² factory) — more credible than the anonymous white-label sellers (L6, L8, L9).
- Same **dual-chip domed-lens architecture as L1**, plus a feature L1 lacks: **frequency (pulse) adjustability**, which is useful for some pain protocols. Cordless 4000mAh, carry case included, and it's the **cheapest credible option at $15.22**.

**Why L1 still beats it (the decisive gap):** L1 **publishes a measured 190 mW/cm² at contact**; Redfy discloses **no irradiance at all** for the RT60 — and irradiance is the #1 spec for dosing your wrist/back. L1 also has **unit-specific certifications** (FCC/ETL/CE/UKCA/RoHS/TGA), whereas Redfy's cert logos are **factory-level**, not tied to this device. The "5W/LED" is the *same dual-chip marketing math* as L1 (so realistically ~2.5W/chip, **not** 12 discrete 5W diodes). So L10 is essentially **"L1's hardware without L1's proof."**
- **Why it beats L2:** lower price, in-stock single-unit MOQ (L2 needs MOQ 3), USB-era cordless, more credible manufacturer scale. But **L2 beats it back** by publishing real irradiance at 3 distances — proof wins.
- **Why it beats L7:** far cheaper and a more serious manufacturer. **L7 beats it back** with 4 wavelengths (830+850 depth) and *on-label* CE/FCC/RoHS.
- **Why it beats L6:** same architecture but Redfy is a known maker, adds frequency control + carry case, and is cheaper. (L6 only edges it on having *a* — unverified — irradiance number in text.)

**Verdict:** the best of the *"ask the seller for a meter reading"* tier. Buy-worthy **only after** Redfy sends a contact/1-inch irradiance photo and confirms the RT60's own certs. Until then, it can't displace L1.

### L11 — SunPlus → lands at #5. Beaten by L1, L2, L7, L10.
**What it has going for it (and why it's tempting):**
- The **single strongest compliance story of the image-archived set**: ISO 9001 + **ISO 13485 (medical-device quality system)**, MDSAP, TGA, ETL, TÜV Rheinland, CE, FCC, RoHS, PSE, SGS. That's a broader, more medical-grade cert wall than even L1.
- Solid, well-finished build, **4000mAh cordless**, domed lenses (better collimation than flat SMD), fold-out kickstand, adjustable brightness + timer, 660+850nm.

**Why it doesn't win:** for *this* use case, certifications don't substitute for **delivered light**, and SunPlus discloses **no irradiance, no per-LED or total power, no dimensions/weight** for the actual handheld. Worse, its only detailed **spec table is borrowed from a different model** (the LF48 — a 120-LED, 48W, 24V mains-powered desktop panel), so the headline numbers don't even describe the unit you'd receive. That's a real honesty red flag. And at **$45.28 it's the most expensive mini here** — you'd be paying a premium for the cert wall + battery, not for measurably stronger output.
- **Why it beats L6/L5/L3:** much stronger compliance, better-documented brand, good battery/build. **Why L10 beats it:** L10 is ⅓ the price from an equally/more credible maker with the same battery class and an extra pulse feature — neither discloses irradiance, so price + maker credibility break the tie for L10.
- **Why L1/L2/L7 all beat it:** all three give you *something measured or on-label* (L1/L2 irradiance, L7 on-label certs + 4 WL); L11 gives a cert wall but no performance proof for the real device.

**Verdict:** the pick **if regulatory paperwork is your top priority** (e.g., reselling, or you want ISO 13485 provenance). For raw pain-relief value it's outclassed — get the supplier to confirm the *handheld's* real wavelengths, power, and irradiance, because the listing's spec table is for another product.

### One-line summary
> The added devices don't unseat **L1**. **L10 (Redfy)** is the better *value/credibility* play and the truest "5W red+NIR" match — but only L1 proves its output. **L11 (SunPlus)** wins on certifications alone, yet hides behind a borrowed spec sheet and a premium price. **L12 (Ideatherapy RL-series)** belongs in red/NIR LED tracking, not IPL, and is still missing the dose data that matters. All three share the field-wide flaw: **no disclosed irradiance.**

### L12 — Ideatherapy RL-series portable lamp → lands at #11. Not an IPL device.
**Why it belongs in this project rather than the IPL project:**
- The supplied Alibaba page describes **red + near-infrared LED therapy**: wavelengths **660nm and 850nm**, not xenon-flash IPL.
- It is marketed as a portable **red light lamp / LED therapy device** for home, clinic, commercial, and beauty-center use.
- It lists a **30° beam angle**, **100-240V AC** input, and multiple LED-count options (**12/24/27/35 pcs**).

**What it has going for it:**
- The supplier, **Shenzhen Idea Light Limited**, is a 12-year Alibaba manufacturer with strong marketplace signals in the supplied page text (4.7/5 store rating, <=2h response time, >=96% on-time delivery, main markets including the US).
- It uses the right basic wavelength pair for red/NIR PBM (**660/850nm**).

**Why it does not move the ranking:**
- The page is a **multi-variant listing family**, not a clean model-specific spec sheet.
- No irradiance, optical power, total electrical draw, dimensions, weight, battery/runtime, included accessories, or unit-specific certificates appear in the supplied text.
- It is listed as **type: Standing**, with **MOQ 3** and a $44-109 price range, so it is not as clean a single-unit handheld buy as L1/L2/L10.

**Verdict:** track it as an **Ideatherapy red/NIR LED candidate**, not IPL. It could be worth asking about if you like the supplier, but the first question is the same as always: send a contact/1-inch irradiance meter photo for the exact RL-series model that ships.

---

## 📋 Per-device detail cards

### 🥇 L1 — AZURETHERAPY AL60  ·  $30 (MOQ 1)
[Listing](https://www.alibaba.com/product-detail/Factory-Direct-Handheld-Rechargeable-LED-Infrared_1601548480919.html) · Supplier: **Shenzhen Azure Technology Co., Ltd.** (3 yrs, 4.9★, US$300k+ online revenue, 53 staff)
- **12 lenses / 24 chips, 60W**, 660/850nm, **30° beam**, **190 mW/cm² @ contact**
- 5000mAh battery, USB-C, 5V; 130×85×30mm; **no flicker, 0µT EMF @3in**; 100,000 hr life
- Controls: brightness dial, **digital countdown display**, battery + charging indicators
- **Certs: FCC, ETL, CE, UKCA, RoHS, TGA, Global-Mark** · **2-yr warranty** · zip case included
- ✅ Best-documented unit here, real irradiance figure, strongest compliance, established seller.
- ⚠️ It's ~2.5W/chip, not 5W. Small 130×85 face = spot treatment (fine for hands/wrist; multiple placements for a back).
- 📸 Spec table: `listing_images/L1_img2.jpg`

### 🥈 L2 — Ideatherapy RTL12-C  ·  ~$36–71 (MOQ 3)
[Listing](https://www.alibaba.com/product-detail/Ideatherapy-Model-RTL12-Portable-Handheld-850nm_1600081086457.html) · Brand: **Ideatherapy**
- 12 lensed modules, 660/850nm with **R/NIR mode button**, aluminum shell (red/black/silver)
- **Irradiance 110/94/64 mW/cm² at 3/5/6 in** — best-disclosed of the group; "EMF 0.0" marketing photo
- ~76×150×30mm, built-in battery, **micro-USB** charging, countdown timer, plug options AU/UK/EU/US/CN/JP
- ✅ Most honest spec sheet, premium build, genuinely handheld, named brand. 2-yr warranty.
- ⚠️ No wattage, no mAh, **no certs listed**, micro-USB (dated), MOQ 3, no irradiance *table image* (numbers are in callouts).
- 📸 Irradiance/EMF: `L2_img4.jpg`; dimensions: `L2_img2.jpg`

### 🥉 L7 — MINI60PRO (desktop/portable)  ·  $69–89 (MOQ 1)
[Listing](https://www.alibaba.com/product-detail/Desktop-630Nm-660Nm-830Nm-850Nm-Red_1601422382660.html)
- 12 **dual-chip dual-color** lenses, **4 wavelengths 630/660/830/850nm**, **15W rated**, >130 mW/cm² *(no distance)*
- Rechargeable (micro-USB, 9V), 150×95×38mm, **timer + pulse, 3 modules**, digital display, flip-out silicone stand/handle
- **Certs: CE, FCC, RoHS (printed on the spec label)** · includes **goggles**
- ✅ Widest wavelength coverage (830+850 both good for depth), only single-unit option with on-label certs, goggles included.
- ⚠️ Only 15W total for 12 LEDs makes the >130 mW/cm² claim doubtful; small area; priciest single unit; no mAh/EMF/lifespan.
- 📸 Spec label: `L7_img2.jpg`

### 4 — L10 — Redfy RT60  ·  $15.22 (MOQ 1)  ⭐NEW
[Listing](https://www.alibaba.com/product-detail/Redfy-Cordless-HandHeld-Device-660Nm-850Nm_1600719440073.html) · Brand: **Redfy** (large red-light contract manufacturer: 17+ yrs, claims Fortune-500 clients, 8,230 m² factory)
- **12 dual-chip domed lenses** (660+850nm, 1:1), marketed **"12pcs × 5W Medical LED" / 60W** *(claim only — no spec table)*
- **4000mAh** cordless, **dimmable + frequency-adjustable (pulse)**, front display, fold-out stand, EVA carry case included
- Certs shown are **factory/company-level** (MDSAP, TGA, ISO, FCC, CE, RoHS) — **not tied to this unit**
- ✅ Closest listing to your "5W red+NIR handheld" spec, from a *credible* manufacturer; same architecture as L1 plus pulse control; cheapest credible option.
- ⚠️ **No irradiance disclosed, no dimensions/weight/input/lifespan.** "5W/LED" is the same dual-chip math as L1 (~2.5W/chip in reality). Listing padded with 12 unrelated panels whose specs (>210 mW/cm²) do **not** apply to the RT60.
- 📸 Closest thing to a spec sheet: `L10_img5.jpg`

### 5 — L11 — SunPlus Mini  ·  $45.28 (MOQ 1)  ⭐NEW
[Listing](https://www.alibaba.com/product-detail/SunPlus-Portable-Mini-Red-Light-Therapy_11000030593664.html) · Brand: **SunPlus**
- **12 domed lenses**, 660/850nm, **4000mAh** cordless, adjustable brightness + timer, fold-out kickstand, vented, well-finished
- **Strongest cert wall of the image-archived set:** ISO 9001, **ISO 13485 (medical QMS)**, MDSAP, TGA, ETL, TÜV Rheinland, CE, FCC, RoHS, PSE, SGS
- ✅ Best compliance/provenance story in the set; solid build + real battery; domed-lens optics.
- ⚠️ **Priciest mini here** and discloses **no irradiance / no real power / no dimensions** for the handheld. Its only spec table is **for a different model** (LF48: 120 LEDs, 48W, 24V mains) — headline specs don't describe the unit you'd receive.
- 📸 Certs: `L11_img10.jpg`; (mismatched) spec table: `L11_img9.jpg`

### 6 — L6 — Mini Panel 660/850  ·  $22.80 (MOQ 1)
[Listing](https://www.alibaba.com/product-detail/660Nm-850Nm-Red-Near-Infrared-Portable_1601481874824.html)
- 12 dual-chip LEDs (660+850 fire together), **5000mAh Li-ion, USB-C**, 130×85×40mm, collimator lenses
- Irradiance **110 mW/cm² (text only, not on any image)**
- ✅ Same chassis/size/battery as L1 at a lower price — possibly the same factory hardware.
- ⚠️ Thin documentation: no total/per-LED power, no certs, no EMF/lifespan/weight, wide price spread ($11.97–224) = many hidden configs.
- 📸 Dimensions: `L6_img4.jpg`; battery/LED: `L6_img2.jpg`

### 7 — L5 — Traveler Mini Panel  ·  $17.83 (MOQ 1)
[Listing](https://www.alibaba.com/product-detail/Handheld-Red-Light-Therapy-Device-for_1601492525001.html)
- **40 pcs 3W 3030 LEDs** (~35 visible), 660/850nm, **5000mAh**, DC 9V/2A, **142×101×30mm, 301 g**
- **Magnetic back + fold-out kickstand** (hands-free), pulse mode + intelligent modes, digital countdown
- ✅ Lightest, most ergonomic for hands-free use on a wrist/forearm; explicit LED spec; cheap.
- ⚠️ Only **3W** LEDs; **no irradiance**, no certs, no EMF/lifespan; LED count likely overstated (40 claimed vs ~35 shown); nominal 120W vs ~18W real input.
- 📸 Spec table: `L5_img5.jpg`

### 8 — L3 — 12pcs "8W" Panel  ·  $16.90 (MOQ 1)
[Listing](https://www.alibaba.com/product-detail/Red-Therapy-Light-Small-Panel-for_1600838083905.html) · Brand: IDEARED/IDEATHERAPY
- 12 multi-die LEDs, 660/850nm, **biggest battery 10000mAh, USB-C**, aluminum, white/black
- **Best controls:** timer 1–20 min, **4 brightness levels**, **pulse 0–9999 Hz**, R/NIR/Both mode select, **mis-touch lock**, digital display
- ✅ Most adjustable device + largest battery (longest runtime).
- ⚠️ **"8W" is title-only** (implausible for SMD), **no irradiance**, **handle sold separately**, this page is the "no-lock" version (contradicts marketing); no certs.
- 📸 Controls: `L3_img3.jpg`; in-box: `L3_img5.jpg`

### 9 — L4 — 60W 3-Wavelength  ·  $8.30 (MOQ 1)
[Listing](https://www.alibaba.com/product-detail/60W-Red-Near-Infrared-660nm-850nm_1601359600648.html)
- Claims 12 lenses, **660/850/1060nm**, **60W (~5W/LED)**, AC110–240V, "iron, 1KG"
- ✅ Cheapest; only listing implying genuine **5W/diode** and the only one with **1060nm** (deeper penetration wavelength); 4-digit timer, Red/NIR modes.
- ❌ **Zero spec images** — every number is unverified text. "Iron / 1 kg" is implausible (looks like ABS plastic). Power delivery (battery vs corded) ambiguous. No irradiance, no certs. **Highest-risk buy.**
- 📸 No spec table exists; control detail: `L4_img5.jpg`

### 10 — L8 — Face Panel w/ Goggles  ·  $13.60+ (MOQ 1 box)
[Listing](https://www.alibaba.com/product-detail/Red-Light-Therapy-for-Face-Portable_1601696740019.html)
- 13 lenses, 660/850nm, USB-C, **timer 5–30 min, 5 brightness levels, 3 modes + pulse**, includes goggles + 360° swivel stand
- ⚠️ **220×210×80mm = a brick**, shown used two-handed / on a stand — **not a true handheld** for a wrist. **Inconsistent stock photos** (one image shows a different color/LED count unit — confirm what actually ships). **No performance specs at all.**
- 📸 Controls: `L8_img6.jpg`

### 11 — L12 — Ideatherapy RL-series portable lamp  ·  $44-109 (MOQ 3)  ⭐NEW
[Listing](https://www.alibaba.com/product-detail/IDEATHERAPY-New-Design-Portable-RL-series_1601723705554.html) · Supplier: **Shenzhen Idea Light Limited** (12 yrs, 4.7★ store rating in supplied page text)
- **660/850nm**, LED quantity options **12/24/27/35 pcs**, **30° beam angle**, **100-240V AC** input
- Marketed as "portable RL series remote control red light lamp / LED therapy device" for travel and home use; application fields include home, clinic, commercial, and beauty center
- Price **$44-109**, **MOQ 3**, estimated shipping shown as $15.55 for 3 pcs in the supplied page text
- ✅ Credible known Ideatherapy/Idea Light supplier; correct red/NIR wavelength pair; global AC input.
- ⚠️ **Not IPL.** Text-only entry with **no irradiance, no model-specific power, no dimensions/weight, no battery/runtime, no certs, and no archived listing images**. It is a listing family, so confirm exactly which LED-count version ships.
- 📸 No archived images yet; source is supplied Alibaba page text.

### ❌ 12 — L9 — MINI60PRO (standing)  ·  $62 (MOQ 51–101 pcs)
[Listing](https://www.alibaba.com/product-detail/New-Arrival-Red-Light-Therapy-Led_1601406290243.html)
- 4 WL 630/660/830/850nm, 12 lenses, "60W" (model name only — sibling L7 is 15W rated), goggles included, also marketed for **equine/animal** use
- ❌ **Wholesale only — MOQ 51–101 pieces.** Not purchasable as a single unit, so it's out for an individual buyer regardless of specs. No spec table in images.

---

## 🎯 Recommendation for hands / back / carpal tunnel

- **Best overall: L1 (AZURETHERAPY AL60, $30).** It's the only one combining a *measured* high irradiance (190 mW/cm²), a full spec sheet, broad certifications, cordless USB-C convenience, and a real supplier with a warranty. The high irradiance + contact use is exactly what you want for pressing on a wrist (carpal tunnel) or hand joints, and you place it on several spots for the back. ~2.5W/chip, but its real-world output beats the "5W" labels elsewhere.
- **If you value honesty/build over a cert sticker: L2 (Ideatherapy RTL12-C).** Irradiance quoted at three distances and an aluminum body — the kind of vendor that measured its product. Current indexed RTL12-C pages show inconsistent wattage/battery/charging details versus the archived listing, so confirm the exact current version before buying.
- **If you want maximum wavelength depth + compliance: L7 (MINI60PRO).** 830+850nm both present and the only single-unit option with CE/FCC/RoHS on the label, goggles included — but verify that >130 mW/cm² claim, since 15W total is low.
- **Best value / closest "5W red+NIR" match: L10 (Redfy RT60, $15.22).** From a credible large manufacturer, same dual-chip architecture as L1, cordless with pulse control — but it discloses no irradiance, so treat it as "L1's hardware without L1's proof." Buy only after the seller sends a contact-distance meter reading and the unit's own certs.
- **If regulatory paperwork is your priority: L11 (SunPlus, $45.28).** The broadest cert wall here (incl. ISO 13485) — but you're paying a premium for compliance, not measured output, and its spec table is for a different model.
- **New Ideatherapy RL-series listing (L12, $44-109):** add it to the vendor-watch list, not the buy list. It is red/NIR LED, **not IPL**, and the supplied page text lacks the output specs needed to dose it.
- **For hands-free wrist/forearm use specifically: L5** (magnetic back + kickstand, 301 g) is the most ergonomic, if you can accept 3W LEDs and undisclosed irradiance.
- **Avoid for this purpose:** **L9** (wholesale-only), **L8** (not really handheld), and **L4** (no verifiable specs at all, despite the tempting 5W/1060nm claims and $8.30 price).

### Practical dose starting point
Use the formula: **dose (J/cm²) = irradiance (W/cm²) × time (seconds)**. If L1's 190 mW/cm² contact number is accurate, 10 J/cm² is roughly 53 seconds. Because supplier numbers can be optimistic and red/NIR power is split across channels, I would start more conservatively in real life: **1–3 minutes per wrist/hand point** and **3–5 minutes per focal back point**, 3–5x/week, then adjust based on response. More is not automatically better; PBM has a biphasic dose-response pattern.

### Questions to send any supplier before buying
1. **Irradiance in mW/cm² at skin contact AND at 1 inch** (ask for a meter photo). This is the #1 number.
2. **Exact wavelengths and the 660:850 power split** (and whether modes fire them separately).
3. **Real per-diode wattage and total electrical draw** (not the "LED rated" sum).
4. **Battery mAh + runtime at full power**, and charging standard (USB-C preferred over micro-USB).
5. **Certifications** — request the actual CE/FCC/RoHS certificate PDFs, not just logos.
6. **For L8:** confirm exactly which unit ships (the photos disagree). **For L3:** confirm the handle and lock are included.

> ⚠️ **Note on claims:** None of these are FDA-cleared medical devices; they're general-wellness products. Irradiance, wattage, and EMF numbers on Alibaba are frequently overstated — treat every unverified figure as a starting point for supplier questions, not a guarantee.
