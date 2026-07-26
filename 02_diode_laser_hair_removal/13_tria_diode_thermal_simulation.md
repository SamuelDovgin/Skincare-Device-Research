# Tria 810 nm Diode Laser — Chromophore Absorption & Thermal Simulation

**The question:** Tria is the only FDA-cleared *laser* for home hair removal — a real **810 nm diode** instead of a broadband IPL flashlamp. What does that one wavelength actually buy you, why is 810 nm a hair-removal sweet spot, and how should Tria’s verified efficacy constrain a thermal model? (Spoiler, corrected after digging into the patents: **both fire a long ~300–400 ms pulse** — the “20 ms spike” repeated online is a myth.) The shared simulator lets you switch between verified IPL and Tria presets while keeping the model scale fixed.

> 🔦 **[▶ Open the shared IPL & diode thermal simulator](../01_ipl_hair_removal/hair_removal_thermal_simulator.html?mode=diode)** — both technologies now use one time–temperature engine, one Arrhenius endpoint, and a clinical-evidence panel. The Tria 20 J/cm² calibration is disclosed rather than hidden in a separate bar scale.

> ⚠️ Not medical advice. Absorption values are representative literature figures (Jacques 2013 for melanin; omlc/Prahl compilations for hemoglobin & water); the thermal model is an illustrative teaching integrator, not a validated simulation. This is the *physics-of-one-pulse* companion to the device/value analysis in [11_810nm_diode_laser_alternatives_vs_ipl.md](11_810nm_diode_laser_alternatives_vs_ipl.md). Never aim a laser at anyone's eyes.

---

## ⭐ The honest bottom line (read this first)

1. **810 nm is a genuine sweet spot, and the chromophore numbers show why.** At 810 nm, melanin's absorption coefficient (~136 cm⁻¹) out-absorbs blood by ~30× and water by ~6800×, while the light still penetrates ~1.5–2 mm to reach the follicle bulb. Shorter wavelengths (532–600 nm) heat blood and the epidermis more and don't reach the follicle; longer ones (1064 nm) penetrate deeper and spare the epidermis but barely heat the hair. 700–950 nm is the "near-infrared optical window," and every hair laser lives in it.[[9]](https://en.wikipedia.org/wiki/Near-infrared_window_in_biological_tissue)

2. **Tria's published incident-fluence ceiling is higher, but that is not the same as absorbed follicle dose.** Tria reaches **20 J/cm²** versus roughly 5–6 J/cm² for many home IPL devices in this archive. Melanin absorbs 810 nm less strongly than shorter IPL wavelengths, while 810 nm also penetrates deeper and avoids some competing superficial absorption. The shared model therefore exposes a small **1.105× diode delivery calibration** instead of pretending the unknown absorbed dose can be derived from incident J/cm² alone. Separate human outcome data are decisive: 20 J/cm² produced more durable reduction than 7 or 12 J/cm² within the same 810 nm device.[[5]](https://pubmed.ncbi.nlm.nih.gov/22886431/)

3. **Both Tria models fire a LONG ~300–400 ms pulse — not a "20 ms spike" (a widely-repeated myth I had to correct mid-project).** Tria's own patent US 7,250,045 states the pulse is *"nominally 300–350 ms,"* with the worked example *"20 J/cm² in 350 ms… requires an optical peak power of only 46 watts,"* and the **Precision IFU independently confirms *"MAX PULSE DURATION 400 ms, MAX OUTPUT 40 W."*** The "20 ms" from reviews is physically impossible at ~40 W (it would need ~1000 W). Because peak power is fixed, **pulse length rises with the level you pick** (~140 ms at 7 J/cm² → ~400 ms at 20). Consequence: the follicle never *spikes* — over a long pulse it sheds heat as fast as it absorbs it, settling at a sustained warmth that works via thermal-damage-time diffusion.[[4]](https://pubmed.ncbi.nlm.nih.gov/12030874/) The 4X and Precision are thermally **twins**; what differs is spot size, level count (5 vs 3), and battery/workflow — not pulse timing.

4. **A single-wavelength home diode is explicitly wrong for the deepest skin.** At 810 nm, epidermal melanin can intercept a larger fraction of incident light before it reaches the follicle. The shared simulator treats Fitzpatrick tone only as a sensitivity proxy, not a personal safety classifier. Tria’s own skin-tone restrictions—not a model temperature—are the binding home-use rule; clinics often use **1064 nm Nd:YAG** when deeper skin requires a more epidermis-sparing wavelength.

---

## 1. The chromophores — what actually absorbs the light

Only a handful of molecules in skin absorb visible/near-IR light. Hair removal is a game of dumping energy into **hair melanin** while sparing the rest.

| Chromophore | Where | μₐ at 810 nm (cm⁻¹) | Role in hair removal |
|---|---|---:|---|
| **Melanin** (eumelanin) | Hair shaft/bulb **and** epidermis | **~136** | The target (in hair) — and the hazard (in epidermis) |
| **Oxy-hemoglobin** | Blood vessels | ~4.4 | Competitor; dominant only at 500–600 nm |
| **Deoxy-hemoglobin** | Blood vessels | ~3.6 | Competitor; small bump ~758 nm |
| **Water** | All tissue (~65%) | ~0.02 | Negligible until >950 nm |

Melanin absorption falls off smoothly with wavelength (Jacques 2013: μₐ ≈ 6.6×10¹¹ · λ⁻³·³³).[[1]](https://pubmed.ncbi.nlm.nih.gov/23666068/) At 500 nm it is ~680 cm⁻¹; at 810 nm ~136; at 1064 nm ~55. That decline is the central trade-off: **shorter = more melanin absorption but shallower + more epidermal/blood competition; longer = deeper + more epidermis-sparing but weaker on the hair.** The shared simulator does not claim to reconstruct a device’s depth-dependent spectrum; it keeps that missing optical transfer inside a labeled calibration term.

---

## 2. Why 810 nm — the wavelength trade-off

| Wavelength | Melanin absorption | Depth / epidermal safety | Clinical role |
|---|---|---|---|
| 532 nm (KTP) | Very high | Shallow; blood competes hard | Surface pigment/vessels — **not hair** |
| 694 nm (ruby) | High | Moderate; risky on darker skin | Old hair laser, light skin |
| 755 nm (alexandrite) | High | Good | Fast, light–medium skin, fine hair |
| **810 nm (diode / Tria)** | **Balanced** | **Deep + reasonable safety** | **The all-round workhorse** |
| 1064 nm (Nd:YAG) | Low | Deepest; safest on dark skin | Fitzpatrick V–VI (needs high fluence) |

The qualitative wavelength ranking comes from the optical literature, not from a fitted consumer-device thermometer: shorter visible wavelengths face more superficial melanin/blood competition, 755–810 nm balances melanin absorption with depth, and 1064 nm is more epidermis-sparing but usually needs higher fluence. The shared tool therefore focuses on the auditable comparison it can support—fluence, pulse width, timing, melanin competition, and one disclosed IPL/diode calibration boundary.

---

## 3. Tria 4X vs. Precision — same long pulse, the "20 ms" myth debunked

| | Tria 4X | Tria Precision (HRLp) |
|---|---|---|
| Wavelength | 810 nm | 810 nm |
| Max fluence | 20 J/cm² (levels 7/12/20) | 20 J/cm² |
| **Pulse duration** | **~300–350 ms** ◐ *(patent; 4X IFU omits it)* | **400 ms max** ✅ *(Precision IFU)* |
| Peak power | ~46 W ◐ *(patent example)* | **40 W** ✅ *(Precision IFU)* |
| Spot | ~1.0 cm² | ~0.8 cm² (9×9 mm) |
| FDA | K090820 / K120737 | K120737 |
| Mechanism | **Long soak → sustained / TDT** | **Long soak → sustained / TDT** |

> **Provenance check (I chased this to the primary sources after being challenged on it — good thing).** The widely-quoted **"20 ms" for the 4X is wrong.** Tria's own patent **US 7,250,045** states the pulse is *"nominally 300 to 350 milliseconds"* (range 10 ms–1 s; preferred 200–600 ms) and gives the worked example *"to produce 20 J/cm² in 350 ms with a 9 mm by 9 mm output area requires an optical peak power of only 46 watts."* The **Precision IFU** independently confirms *"MAX PULSE DURATION: 400 ms"* and *"MAX OUTPUT LASER RADIATION: 40 W."* The 4X IFU omits pulse duration, but the shared platform + identical ~40 W-class delivery means it's the same long pulse. A 20 ms pulse at 20 J/cm² would need ~1000 W — no battery handheld does that. **Both Tria models are long-pulse.**

Because a diode's peak power is fixed (~40–46 W), **pulse length rises with the level you select** — roughly ~140 ms at 7 J/cm² up to ~350–400 ms at 20 J/cm². Over a pulse that long the follicle **can't spike**: it sheds heat as fast as it absorbs it (its thermal-relaxation time is only ~10–100 ms) and settles at a **sustained warmth**. That sustained heat then has time to diffuse outward to the bulge stem cells — the "thermal damage time" window, ~170–1000 ms.[[4]](https://pubmed.ncbi.nlm.nih.gov/12030874/) So Tria works by *soaking*, not spiking.

**What the recalibrated model shows at Tria’s verified settings:** with the disclosed 1.105× diode delivery calibration, the 20 J/cm² / 350 ms preset lands just above the selected deep-target Ω=1 criterion (about Ω=1.09), while the illustrative 12 and 7 J/cm² cases remain below it. That is a deliberately modest benchmark fit to the *direction* of Wheeland’s dose response—not a claim that Ω predicts 65%, 49%, or 44% hair reduction. Clinical reduction over an eight-session course also reflects hair-cycle targeting; thermal dose does not accumulate unchanged between monthly sessions.

**Two things people always ask about Tria — the pain, and the lack of chilled contact cooling.** Tria’s fan manages device heat, but the Precision IFU does not describe a chilled treatment window. Dark, coarse follicles can create a localized deep hot-pinprick sensation; epidermal melanin, treatment site, pulse structure, and individual sensitivity also contribute. The shared simulator now keeps pain outside the thermal bar and instead shows the randomized pain findings beside the efficacy anchors.

---

## 3A. July 2026 pain update — yes, other people often report the same gap

The user's report—**Tria Precision was dramatically more painful than their IPL device**—is plausible and well aligned with two stronger sources:

1. The **Precision IFU itself** says almost all users in its clinical study reported mild-to-moderate pain or discomfort during the first treatment. It lists warmth, burning, tingling, and itching, compares the sensation to a rubber-band snap, and says sensitivity generally declined in later treatments.[[7]](Tria_Precision_IFU_HRLp.pdf)
2. A **2026 randomized split-body trial** treated opposite axillae with IPL and an 810 nm diode at the same professional fluence/pulse duration (25 J/cm², 10 ms; both cooled). First-session median pain was **6/10 for diode versus 1/10 for IPL**; by session four it was **5 versus 0**. The diode also caused more transient perifollicular edema and hair carbonization, consistent with a stronger immediate follicular thermal effect.[[11]](https://pmc.ncbi.nlm.nih.gov/articles/PMC13242373/)

That trial is unusually relevant because the diode spot was **0.81 cm²**, essentially the same small geometry used in Tria's patent example. It is **not** a direct Tria-vs-home-IPL trial: the clinic devices used 25 J/cm² / 10 ms, while Precision uses a much longer pulse and home IPL usually uses lower fluence. The pain numbers therefore anchor the direction of the difference, not your expected score.

### Why your IPL probably felt gentler

| Driver | Tria Precision | Typical home IPL | Pain implication |
|---|---|---|---|
| Published fluence | 7–20 J/cm² | commonly about 5–6 J/cm² in this archive | Tria can deliver much more energy density per spot |
| Spectrum | concentrated 810 nm diode | broadband filtered flash | Different depth and follicular heat distribution |
| Treatment window | small, about 0.8 cm² | often several cm² | Tria feels like repeated localized pinpricks |
| Contact cooling | no chilled skin-contact system disclosed | many newer devices use sapphire/contact cooling | cooled IPL can suppress surface heat sensation |
| Hair density | each dark coarse follicle is a strong absorber | same principle, usually lower per-pulse dose | underarms/bikini/coarse patches often hurt most |
| Pulse protocol | up to 400 ms, 40 W max | device-specific; may use split/sub-pulses | sensation can be deeper/longer even without a clinic-style spike |

The honest qualifier is that **device class alone does not determine pain**. A 2010 randomized hirsutism trial found its IPL protocol more painful than its long-pulsed diode protocol (median 6 vs 3), while 2014 and 2026 comparisons found diode more painful. Fluence, pulse width, cooling, spot, body site, hair density, and individual sensitivity can reverse the ranking.[[12]](https://pubmed.ncbi.nlm.nih.gov/20731651/)

### What other Tria users describe (anecdotal, not prevalence data)

Recent user reports span a wide range:

- one user described level 5 as only “maybe a pinch,” but said Tria produced a deeper heat/pain than prior IPL;
- another returned the device because it took too long and “hurts a LOT”;
- a dedicated “too painful” thread includes users unable to tolerate level 3, users staying at level 2, and one person who sold an older unit because they could not use it without numbing cream;
- another comparison described professional laser as a rubber-band snap but Tria as a “harsh bite.”

These reports establish **range and adherence problems**, not a percentage of users affected. People with extreme experiences are more likely to post.[[13]](https://www.reddit.com/r/HairRemoval/comments/1cghosy/tria_4x_too_painful/)

### Practical ways to improve tolerability

1. **Patch-test and use the highest level you can comfortably tolerate.** The Precision manual explicitly directs Low → Medium → High testing on separate spots, a 24-hour wait, then the highest comfortable level. “High at all costs” is not the instruction.
2. **Cleanse, shave closely, and dry completely.** The IFU says surface-hair removal improves comfort and lets light reach the follicle. Do not wax or pluck because the follicular target must remain.
3. **Treat small zones.** The Precision is a spot tool. A completed Medium session can be more useful than repeatedly abandoning High.
4. **Do not stack pulses.** Move by about half a window after each pulse for coverage, but never repeatedly fire the same spot; the IFU warns that this can cause discomfort, heating, and injury.
5. **Consider brief external cooling.** A 2023 randomized 810 nm diode study found ice packs and lidocaine-prilocaine provided broadly similar pain control, with 60.2% of treatment preferences favoring ice. For home use, use a wrapped cool pack, never direct ice, and dry the skin completely before firing.[[14]](https://pubmed.ncbi.nlm.nih.gov/36410628/)
6. **Avoid high-strength internet numbing creams.** FDA warned in 2024 that high-concentration lidocaine products marketed for laser hair removal can cause irregular heartbeat, seizures, and breathing difficulty. Ask a clinician before using anesthetic, especially on large areas.[[15]](https://www.fda.gov/news-events/press-announcements/fda-warns-consumers-avoid-certain-topical-pain-relief-products-due-potential-dangerous-health)

> **Stop instead of pushing through** if pain is intense or persists after treatment, or if blistering, a burn, or a skin-color change appears. That is the Precision manual's safety boundary, not a normal “effective treatment” signal.

---

## 4. Dark skin — why a single-wavelength diode isn't enough

Diode 810 nm is **safer on medium-dark skin than IPL** (epidermal melanin absorbs less at 810 than at IPL's shorter wavelengths), but it still has a hard ceiling. Drag skin tone to **Fitzpatrick VI** in the simulator at 810 nm:

- **Epidermis ~71 °C** (burn / pigment-change zone, HIGH risk) — epidermal melanin absorbs the beam before it gets deep.
- **Follicle ~42 °C** (sub-lethal) — starved of the light the epidermis stole (melanin competition).

Now change only the wavelength to **1064 nm (Nd:YAG)**: epidermis drops to ~58 °C *and* the follicle rises to ~47 °C — safer **and** more effective. Nd:YAG's weak melanin absorption is a feature here: it lets the beam skip past the epidermal melanin and reach the follicle. This is exactly why clinics reach for Nd:YAG on the deepest skin tones, and why Tria (810 nm only) is contraindicated for Fitzpatrick VI.

---

## 5. What the Tria clinical data shows

The cleanest home-device dose-response ever published was run **on the Tria**, testing its own three fluence levels in the same people over 8 monthly sessions:[[5]](https://pubmed.ncbi.nlm.nih.gov/22886431/)

| Tria fluence | Reduction @ 1 month | @ 12 months |
|---|---|---|
| 7 J/cm² | 60% | 44% |
| 12 J/cm² | — | 49% |
| **20 J/cm²** | **73%** | **65%** |

Higher single-pulse fluence bought more **durable** reduction — the strongest argument for running Tria at level 5 (20 J/cm²) on tolerant areas. Tria's own 88-subject clearance study tested 7/12/20 J/cm² and reported up to ~100% reduction in high-fluence areas after a full regimen.[[6]](https://www.trialaser.com/products/hair-removal-laser-4x)

---

## 6. The raw data — verified source extracts (recorded so we don't lose it)

Everything above is distilled from the primary extracts below. They're written out verbatim here because the interactive simulator's embedded data could be regenerated, but *this markdown is the durable record.*

### 6a. Tria specs — every category, hardest source

| Spec | Tria 4X | Tria Precision (HRLp) | Source |
|---|---|---|---|
| Wavelength | 810 nm | 810 nm | ✅ both IFUs (PDFs in this folder) |
| Max fluence | 7–20 J/cm² (levels 7/12/20) | 7–20 J/cm² | ✅ both IFUs |
| Energy levels | 5 | 3 (Low / Medium / High) | ✅ both IFUs |
| **Pulse duration** | **~300–350 ms** (nominal) | **400 ms** (max) | ◐ patent US 7,250,045 (4X) · ✅ Precision IFU |
| **Peak optical power** | ~46 W (worked example) | **40 W** (max) | ◐ patent (4X) · ✅ Precision IFU |
| Spot / window | ~1 cm² | ~0.8 cm² (9×9 mm) | ◐ patent example = 0.8 cm² |
| Laser class | 1 | 1 | ✅ both IFUs |
| FDA 510(k) | K090820, K120737 | K120737 | ✅ FDA |
| Rep rate (between pulses) | varies — slower at high level / warm room | same | ◐ both IFUs (qualitative) |
| Active skin cooling | **none** (sapphire window protects the device, doesn't pre-chill skin → it stings) | none | ◐ patent (window/heat-sink only) + pain reports |
| ❌ "20 ms pulse" claim | **debunked** — third-party only; needs ~1000 W but Tria is ~40 W | — | — |

### 6b. Verbatim extracts

**Tria Precision IFU (HRLp) — Technical Specifications page** (`Tria_Precision_IFU_HRLp.pdf`, in this folder):
> LASER TYPE: Diode laser · LASER CLASS: 1 · OUTPUT WAVELENGTH: 810 nm · MAX OUTPUT LASER RADIATION: **40 W** · **MAX PULSE DURATION: 400 ms** · OUTPUT FLUENCE: 7–20 J/cm² · MODEL: HRLp · EXPECTED SERVICE LIFE: 3 Years

**Tria 4X IFU — Technical Specifications** (`Tria_4X_IFU_2ndGen_current.pdf`, in this folder):
> Laser type: Diode laser · Laser class: 1 (IEC 60825-1:2014) · Output wavelength: 810 nm · Output fluence: 7–20 J/cm² · clinical study fluences 7/12/20 J/cm² · **[no pulse duration or peak power listed anywhere in the spec page]**

**Patent US 7,250,045 B2** (Tria/SpectraGenics) — the hard source for pulse timing:
> Pulse duration **nominally 300–350 ms** (claimed range 10 ms – 1 s; preferred 200–600 ms). Peak optical power **30–60 W** (average ~8 W). Worked example: *"to produce 20 J/cm² in 350 ms with a 9 mm by 9 mm output area requires an optical peak power of only 46 watts."* Spot 0.25–5 cm² (preferred 0.8 cm² = 9×9 mm). Fluence 4–100 J/cm² (preferred ~20). ~800 nm (700–1100 nm), AlGaAs diode bars, sapphire cooling. → Also recorded in the patents section of [11_810nm_diode_laser_alternatives_vs_ipl.md](11_810nm_diode_laser_alternatives_vs_ipl.md).

### 6c. Other 810 nm diode devices (FDA context)

| Device | Max fluence | Spot | Pulse | Source |
|---|---|---|---|---|
| DermRays / CurrentBody V8S | 9 J/cm² | 3.0 cm² (30×10 mm) | not published (modeled long) | FDA K230090 |
| DermRays V4S | 7 J/cm² | 3.0 cm² | not published | FDA K230090 |
| SilkPro | 25 J/cm² (5/10/15/20/25) | 0.81 cm² (9×9 mm) | not published | FDA K142845 |
| Foundational — US 5,735,844 (Anderson/MGH) | 10–200 J/cm² (pref 30–50) | ≥8 mm, 0.75–1 cm² | — | patent |

### 6d. Chromophore absorption coefficients (μₐ, cm⁻¹) — the simulator's dataset

Melanin: Jacques 2013 melanosome formula **μₐ = 6.6×10¹¹ · λ⁻³·³³**. Hemoglobin & water: representative whole-blood / pure-water values from omlc/Prahl compilations. (Illustrative teaching figures, not a spectrophotometer trace.)

| λ (nm) | Melanin | Oxy-Hb | Deoxy-Hb | Water |
|---|---:|---:|---:|---:|
| 532 (KTP) | 552 | 240 | 158 | 0.0004 |
| 577 | 423 | 296 | 132 | 0.002 |
| 694 (ruby) | 228 | 1.6 | 12 | 0.006 |
| 755 (alexandrite) | 171 | 2.6 | 7.2 | 0.026 |
| **810 (diode / Tria)** | **136** | **4.4** | **3.6** | **0.02** |
| 940 | 83 | 6.6 | 3.4 | 0.27 |
| 1064 (Nd:YAG) | 55 | 4.0 | 2.0 | 0.12 |
| 1200 | 37 | 3.4 | 1.6 | 1.0 |

At **810 nm** melanin out-absorbs oxy-hemoglobin by ~**31×** and water by ~**6800×** — the selectivity that makes 810 nm *the* hair-removal wavelength.

---

## ⚠️ Evidence gaps

- **The model is illustrative.** It reproduces qualitative physics (chromophore selectivity, fluence, pulse-duration trade-offs) from published μₐ and TRT/TDT values; absolute temperatures and thresholds are conservative stand-ins.
- **Chromophore μₐ are representative figures, not a spectrophotometer trace.** Melanin uses the Jacques melanosome formula; hemoglobin/water use standard omlc/Prahl compilations. Real skin values vary with concentration, oxygenation, and hydration.
- **Tria's exact per-level pulse behavior isn't fully public.** The 4X IFU omits pulse duration entirely; the ~300–350 ms figure comes from Tria's patent (US 7,250,045) plus its ~40 W-class power. The Precision IFU gives "MAX 400 ms / 40 W" — a *ceiling*, not the value at each level. Since pulse length scales with fluence at fixed power, lower levels fire shorter pulses. (The "20 ms" in many reviews is simply wrong — see §3.)
- **Penetration is modeled as a smooth wavelength factor, not a Monte-Carlo photon simulation** — the depth trend is right, the exact millimeters are approximate.
- **The pain explorer is a directional teaching index, not a fitted pain scale.** It exposes contributors that plausibly move discomfort up or down; it does not predict a personal 0–10 score, safety, or efficacy.

---

## 📚 Sources

1. Jacques SL. Optical properties of biological tissues: a review. *Phys Med Biol* 2013;58(11):R37 — melanosome μₐ = 6.6×10¹¹·λ⁻³·³³. https://pubmed.ncbi.nlm.nih.gov/23666068/
2. Prahl S / Optical Media Lab — compiled oxy/deoxy-hemoglobin & water absorption spectra. https://omlc.org/spectra/
3. Anderson RR, Parrish JA. Selective photothermolysis. *Science* 1983;220:524-527. https://pubmed.ncbi.nlm.nih.gov/6836297/
4. Rogachefsky AS, et al. Super-long-pulsed 810 nm diode laser & the concept of thermal damage time. *Dermatol Surg* 2002;28(5):410-414 — TDT 170–1000 ms, optimal ≈400 ms at 46 J/cm² (the Precision's basis). https://pubmed.ncbi.nlm.nih.gov/12030874/
5. Wheeland RG. Simple, effective home 810 nm laser (Tria) dose-response, 2012 — 7/12/20 J/cm² → 44/49/65% at 12 months. https://pubmed.ncbi.nlm.nih.gov/22886431/
6. Tria Beauty Hair Removal Laser 4X — product page, IFU (in this folder) & FDA K090820 / K120737. The IFU's technical specs confirm **810 nm** and **7–20 J/cm²** only — it does **not** publish a pulse duration; the "~20 ms / ~3 pulses/s" figures are from third-party reviews. https://www.trialaser.com/products/hair-removal-laser-4x
7. Tria Hair Removal Laser Precision (HRLp) IFU (in this folder) — **verified** technical specs: 810 nm · **MAX PULSE DURATION 400 ms** · **MAX OUTPUT LASER RADIATION 40 W** · 7–20 J/cm². https://www.manualslib.com/manual/1292786/Tria-Hair-Removal-Laser-Precision.html
8. **US 7,250,045 (Tria/SpectraGenics)** — the hard source for Tria's pulse: *"nominally 300 to 350 milliseconds"* (range 10 ms–1 s; pref 200–600 ms), peak power 30–60 W, worked example *"20 J/cm² in 350 ms… requires an optical peak power of only 46 watts."* Also spot 0.25–5 cm² (pref 0.8 = 9×9 mm), fluence 4–100 (pref ~20). https://patents.google.com/patent/US7250045B2/en · (plus US 5,735,844, Anderson/MGH: 680–1200 nm, sapphire cooling — see [11_810nm_diode_laser_alternatives_vs_ipl.md](11_810nm_diode_laser_alternatives_vs_ipl.md)).
9. Near-infrared optical window in biological tissue — 700–950 nm penetrates deepest with least competing absorption. https://en.wikipedia.org/wiki/Near-infrared_window_in_biological_tissue
10. Byalakere Shivanna C, et al. *Methods to overcome poor responses and challenges of laser hair removal in dark skin.* 2022 — follicular TRT/coagulation context used by the thermal teaching model. https://pmc.ncbi.nlm.nih.gov/articles/PMC9541334/
11. Barros RTB, et al. *Efficacy and safety of intense pulsed light compared to diode Laser for hair removal: a randomized controlled trial.* *Lasers Med Sci* 2026;41:108. Median session-1 pain: diode 6/10 vs IPL 1/10; at session 4: 5 vs 0. Local CC BY full-text XML: [source_docs/PMC13242373_2026_IPL_vs_diode_randomized_fulltext.xml](source_docs/PMC13242373_2026_IPL_vs_diode_randomized_fulltext.xml). https://pmc.ncbi.nlm.nih.gov/articles/PMC13242373/
12. Ismail SA. *Hair removal in hirsute women with normal testosterone levels: a randomized controlled trial of long-pulsed diode laser vs. intense pulsed light.* *Br J Dermatol* 2010;163(4):859-864. This protocol found IPL more painful (median 6 vs 3), demonstrating that device parameters can reverse the category-level pattern. https://pubmed.ncbi.nlm.nih.gov/20731651/
13. r/HairRemoval, “Tria 4x too painful” and linked user-experience threads, accessed 2026-07-12. Anecdotal/self-selected evidence for the range from tolerable to treatment-limiting pain; not prevalence data. https://www.reddit.com/r/HairRemoval/comments/1cghosy/tria_4x_too_painful/
14. Roongpisuthipong W, et al. *Comparative effectiveness of ice packs versus topical lidocaine-prilocaine mixture for pain control in laser hair removal of the axilla.* *J Am Acad Dermatol* 2023;88(3):617-622. Randomized 810 nm diode comparison; no serious adverse events and 60.2% of treatment preferences favored ice. https://pubmed.ncbi.nlm.nih.gov/36410628/
15. U.S. FDA. *FDA Warns Consumers to Avoid Certain Topical Pain Relief Products Due to Potential for Dangerous Health Effects.* 2024-03-26 — warning includes products marketed for laser hair removal and risks from excessive lidocaine absorption. https://www.fda.gov/news-events/press-announcements/fda-warns-consumers-avoid-certain-topical-pain-relief-products-due-potential-dangerous-health

*Compiled 2026-07-01; pain/tolerability update 2026-07-12; shared-model update 2026-07-25. Pairs with the [shared IPL & diode simulator](../01_ipl_hair_removal/hair_removal_thermal_simulator.html?mode=diode) and the device/value analysis in [11_810nm_diode_laser_alternatives_vs_ipl.md](11_810nm_diode_laser_alternatives_vs_ipl.md).*
