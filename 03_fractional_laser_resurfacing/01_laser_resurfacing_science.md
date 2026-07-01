# Science Brief: Non-Ablative Fractional Laser Resurfacing (Pigment + Collagen)

**Goal of this thread:** find an *at-home* device that meaningfully improves **skin quality** — pigmentation/PIH, tone/brightness, and long-term collagen/fine lines — ideally approaching what an in-office **Clear + Brilliant** does.

> **How this differs from the parent repo.** The main `IPL Device Research` project is about **broadband IPL for hair removal + redness**. This subfolder is a *different device class*: **fractional / non-ablative infrared lasers** (Clear + Brilliant, Fraxel, Tria, NIRA, etc.). Different physics, different chromophore, different goal. Read the parent repo's [07_alternatives_and_strategy](../01_ipl_hair_removal/07_alternatives_and_strategy.md) first — its core finding (for pigment-prone skin, lead with topicals + photoprotection, not energy devices) still governs everything here.

**Confidence legend used throughout this folder:**
- ✅ **Verified** — FDA 510(k) filing, peer-reviewed clinical paper, or official manufacturer spec sheet
- ⚠️ **Marketing claim** — from a seller/brand/retail page, not independently confirmed
- 🔍 **Inferred** — reasoned from wavelength/category physics; needs primary-source confirmation

---

## 1. The device taxonomy — where each thing sits

There are three axes that matter. Almost every confusion in the marketing comes from collapsing them.

| Axis | Option A | Option B | Why it matters |
|------|----------|----------|----------------|
| **Ablation** | **Ablative** (CO₂ 10,600nm, Er:YAG 2940nm) — vaporizes tissue | **Non-ablative** (1410–1927nm) — heats but leaves surface intact | Ablative = dramatic results + real downtime + high PIH risk. **All home pigment/collagen devices are non-ablative.** |
| **Fractionation** | **Fractional** — treats microscopic columns, leaves bridges of intact skin between | **Non-fractional / bulk** — heats a whole zone uniformly | Fractional = faster healing, controlled injury, the basis of Fraxel/Clear+Brilliant/Tria. Non-fractional (NIRA) = gentler dermal warming, no true resurfacing. |
| **Setting/power** | **In-office** (Clear+Brilliant, Fraxel, Moxi) — provider-controlled, high energy | **At-home / OTC** (Tria, NIRA, YDUNVIE) — capped energy for safety | The energy gap is the whole story (see [02_in_office_vs_at_home](02_in_office_vs_at_home.md)). |

**The category you actually want for skin quality:** *non-ablative **fractional** infrared laser*. Clear + Brilliant is the in-office reference. Tria FRX, PaloVia, Philips RéAura, MimiSilk Iris, and YDUNVIE Iris Ice are the home members. NIRA is the odd one out — it is non-ablative but **non-fractional**, so it is a "dermal warmer," not a resurfacer.

---

## 2. The governing physics: water as the chromophore

IPL targets **melanin and hemoglobin** (pigment, hair, vessels). These resurfacing lasers target **water**, which is everywhere in skin. By heating water in tiny columns, you create **microthermal zones (MTZs)** — controlled micro-injuries that trigger a wound-healing/remodeling cascade: epidermal turnover (pushes out pigment) + dermal collagen stimulation (fine lines, texture).

**Water absorption rises with wavelength in this band**, and that single fact determines depth and target:

| Wavelength | Water absorption | Penetration depth (approx) | Best target | ✅/source |
|-----------|------------------|---------------------------|-------------|-----------|
| **1410–1450nm** | moderate | **deeper (~280–400 µm)** | dermal collagen, texture, pores, fine lines, shallow acne marks | ✅ depths from a 1440/1927 NAF diode study: 1440nm reaches ~280/340/390 µm by energy level |
| **1470nm** | moderate | deep | collagen/texture (OEM/clinic) | 🔍 |
| **1550nm** | higher | deep (Fraxel re:store class) | dermal remodeling, scars, deeper wrinkles | ✅ Fraxel re:store |
| **1927nm** | **high** | **shallow (~170 µm)** | **superficial pigment, dullness, melasma/PIH-prone discoloration, brightening** | ✅ 1927nm handpiece reaches ~170 µm at 5 mJ |

**The single most important takeaway for pigment vs collagen:**
- **Pigmentation / PIH / brown spots / dullness / brightening → 1927nm** (superficial, where epidermal pigment lives). This is Clear + Brilliant **Perméa**, Sciton **Moxi**, **LaseMD**, and the home YDUNVIE **Dora**.
- **Collagen / texture / pores / fine lines → 1440–1550nm** (deeper, into the dermis). This is Clear + Brilliant **Original**, **Fraxel**, **Tria FRX**, **NIRA**, and the home YDUNVIE **Iris Ice**.

> "Deeper" ≠ "better." For pigment, the *superficial* 1927nm is the right tool because the target is in the epidermis. Pushing a deeper 1450nm beam past the pigment just adds dermal heat — which in pigment-prone skin can *worsen* PIH. Match the wavelength to the depth of the problem.

---

## 3. Mechanism difference: fractional injury vs bulk warming

This is why NIRA is not a Clear + Brilliant substitute even though the wavelengths are close.

- **Fractional (Clear+Brilliant, Tria FRX, YDUNVIE Iris/Dora):** create discrete columns of controlled thermal injury, leaving untreated skin between them. The injury drives epidermal turnover (pigment) and dermal remodeling (collagen). This is what produces *resurfacing*-type results — texture, pores, tone, mild pigment.
- **Non-fractional warming (NIRA):** ✅ NIRA's own framing is heating the dermis above ~39°C to activate heat-shock-protein / collagen pathways while staying below the pain threshold. No micro-injury columns, so no true resurfacing. It is a **daily/low-downtime collagen-maintenance** tool, not a pigment or resurfacing device.

So the mechanistic ranking for *visible remodeling*:
**In-office fractional (Clear+Brilliant/Fraxel) > home fractional (Tria/YDUNVIE) > home non-fractional warming (NIRA).**
But the *downtime/convenience* ranking is the exact inverse.

---

## 4. What makes a treatment "efficacious" — the spec ceiling

Marketing loves to quote one big number. For fractional lasers, **no single number tells you efficacy** — you need the whole set:

| Spec | What it controls | Why a single number misleads |
|------|------------------|------------------------------|
| **Energy per microbeam (mJ/pulse)** | depth + intensity of each column | "12 mJ" sounds strong but is meaningless without spot size |
| **Microbeam/spot diameter (µm)** | fluence (energy ÷ area) | a wide low-mJ beam ≠ a tight high-mJ beam |
| **Density (MTZs/cm² or % coverage)** | how much skin is treated per pass | low density = gentle but slow/weak results |
| **Total delivered energy (J, full-face)** | cumulative dose | a "180 J full-face" headline mixes units with per-pulse mJ |
| **Treatment depth (µm)** | which target you reach | epidermal (pigment) vs dermal (collagen) |
| **Number of sessions** | cumulative remodeling | one session of anything does little |
| **Wavelength + tolerance (nm ± nm)** | the target itself | 1450 vs 1927 is the whole pigment-vs-collagen split |

**Unit trap to watch (appears constantly in YDUNVIE/OYAY listings):** *"180 J full-face"* (total accumulated energy over a whole treatment) is **not** comparable to *"12 mJ/pulse"* (energy in one microbeam). A device can have identical 12 mJ/pulse but very different full-face totals depending on density, time, and area. **Always force sellers onto the same units before comparing** (see [06_sourcing_rfq_templates](06_sourcing_rfq_templates.md)).

---

## 5. The home-vs-clinical energy gap (the honest reality)

✅ Verified spec anchors (full detail and citations in [02_in_office_vs_at_home](02_in_office_vs_at_home.md) and [03_device_landscape](03_device_landscape.md)):

| Device | Class | Wavelength | Per-pulse / fluence ceiling |
|--------|-------|-----------|------------------------------|
| Clear + Brilliant Original | in-office fractional | 1440nm | **9 mJ** max, 2.5 W avg |
| Clear + Brilliant Perméa | in-office fractional | 1927nm | **5 mJ** max, 0.9 W avg |
| Tria FRX (FAN) | home fractional | 1450±50nm | ~5–12 mJ/pulse ⚠️ (marketing) |
| PaloVia | home fractional | 1410nm | ~10–15 mJ ⚠️ |
| NIRA Model 2 | home **non-fractional** | 1450nm | 2.1–3.8 J/cm² (fluence), 2 W |
| YDUNVIE Iris Ice / Plus | home fractional | 1450nm | 3–12 mJ/pulse ⚠️ (OEM/seller) |

Interestingly, the **per-microbeam energy of home fractional devices (5–12 mJ) overlaps Clear + Brilliant's own 5–9 mJ** — and at a matched wavelength so does the **depth** (depth is set by wavelength, not by the device). The clinical gap is **not** mainly energy or depth — it's **density/coverage, scan precision, dual-wavelength capability, number of passes, and a provider tuning aggression to a clinical endpoint**. A home device fires **fewer, less-dense, more conservative** columns (at the same depth) and caps aggression for safety. That's why it takes far more home sessions for a fraction of the result — but it is not *nothing*, especially cumulatively. (Quantified in [08](08_clear_brilliant_quantified_gap.md).)

---

## 6. PIH / safety — the constraint that dominates pigment-prone skin

The reason this whole thread needs caution: **any thermal/injury device can trigger post-inflammatory hyperpigmentation (PIH) in melanin-rich or pigment-prone skin.** A device sold "for brightening" can *worsen* brown discoloration if energy, density, cooling, or instructions are poor.

Protective factors to demand in any device:
- **Cooling** (contact/sapphire/"ice") to protect the epidermis
- **Lower density / conservative energy** options
- **Skin-tone guidance / sensor** and explicit Fitzpatrick limits
- **Eye-safety design** (mandatory for any home laser near the periorbital area)
- A protocol that spaces sessions and ramps slowly

**Contraindications that recur across these devices:** pregnancy, active acne/infection, melasma (relative — can flare), isotretinoin use, photosensitizing meds, recent sun exposure/tan. Always pair with strict daily SPF — without photoprotection, any pigment gains reverse.

---

## 7. One-paragraph synthesis

For **pigment/PIH/brightness**, the right physics is **1927nm fractional** (Perméa / Moxi / LaseMD in-office; YDUNVIE **Dora** at home). For **collagen/texture/pores/fine lines**, it's **1440–1550nm fractional** (Clear+Brilliant Original / Fraxel in-office; **Tria FRX**, **YDUNVIE Iris Ice** at home). **NIRA** is a gentle non-fractional dermal warmer — good low-downtime collagen maintenance, weak for pigment. No home device closes the clinical gap, but home **fractional** devices (Tria / YDUNVIE / PaloVia) are genuinely the *same category* as Clear + Brilliant, whereas non-fractional and LED/VCSEL devices are a softer adjacent category. Whatever the device, **cooling + conservative settings + daily SPF** are non-negotiable for pigment-prone skin.

---

## 8. The patent behind "fractional" itself

Every device on this page — Clear + Brilliant, Fraxel, Tria, PaloVia, YDUNVIE — implements the same underlying concept: fractional photothermolysis, treating only a fraction of the skin surface in a grid of microscopic injury columns. That concept has a real, specific, foundational patent, not just Manstein's well-known 2004 paper: **US 6,997,923 B2** ("Method and apparatus for EMR treatment," MGH + Palomar Medical Technologies, filed Dec. 2001, granted Feb. 2006) claims concentrating radiation into discrete 3-D "treatment portions" with a treatment-to-total-volume "fill factor" of 0.1–90% — the patent-claim expression of the "microscopic treatment zone" concept, with **Dieter Manstein himself as a named co-inventor**. Notably assigned to MGH + Palomar, not Reliant Technologies (maker of the original Fraxel) — a competing Reliant application on the same concept went abandoned, and the IP was later cross-licensed industry-wide via a "Fractional Technology Open Patent Program." Solta Medical's own next-generation consumer-fractional patent, **US 8,475,507 B2** (filed 2011, matches the PaloVia/home-NAFL concept), extends the same lineage. **Full patent block, links, and mirrored PDF for both are in [08 §9](08_clear_brilliant_quantified_gap.md)** — not repeated here to avoid the two docs' structured citations colliding on the folder's aggregated Patents page.

**Not found:** any patent held by Jiangsu Unimed or under the "YDUNVIE" name — direct Google Patents queries (assignee-scoped and unscoped) for both names returned zero results. Only a USPTO *trademark* registration (Serial 88541477, for the YDUNVIE mark itself) exists. **Separately checked "MimiSilk" as its own assignee name** (not just the presumed Jiangsu Unimed/YDUNVIE OEM link) — same result: no patent found under that name either, via direct Google Patents queries and a site-restricted web search. MimiSilk's own "About Us" page describes its tech only in marketing terms ("proprietary dual-band technology — 415nm blue light and 830nm infrared laser with advanced electro-pulse energy," which describes a different SKU than the Iris fractional device this repo tracks) and names no patent number or manufacturing partner. Consistent with this repo's broader pattern of Chinese OEM manufacturers skipping formal patent filings. (Tria's and Clear+Brilliant's own patents are cited in [08](08_clear_brilliant_quantified_gap.md) rather than repeated here.)

---

### Sources (this brief)
- [Clear + Brilliant Touch clinical protocol (NCT05027282)](https://clinicaltrials.gov/study/NCT05027282) — 1440/1927nm combination
- [The 1440nm and 1927nm Nonablative Fractional Diode Laser — JDD review](https://jddonline.com/articles/article-the-1440-nm-and-1927-nm-nonablative-fractional-diode-laser-current-trends-and-future-directi-S1545961620S00s3X/) — depths, targets
- [NIRA Model 2 510(k) K222685](https://www.accessdata.fda.gov/cdrh_docs/pdf22/K222685.pdf) — 1450nm non-fractional, fluence, 39°C/HSP mechanism framing
- [Tria FAN System 510(k) K130459](https://www.accessdata.fda.gov/cdrh_docs/pdf13/k130459.pdf) — 1450±50nm fractional, periorbital
- [PaloVia home NAF laser multicenter trial (ScienceDirect)](https://www.sciencedirect.com/science/article/abs/pii/S0190962212001430) — 1410nm, internal scanner
