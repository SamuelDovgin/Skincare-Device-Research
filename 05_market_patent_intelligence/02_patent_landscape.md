# 02 — Patent Landscape: Who Owns the Home-Device Frontier

*Research archive note — compiled 2026-06-30. Every patent number below was opened on Google Patents (or, where noted, confirmed via Justia / USPTO / company sources) and reflects the assignee, dates, and scope shown on the fetched page. Where a specific number could not be verified, the claim is stated qualitatively rather than invented.*

This document maps the patent terrain underneath the at-home skincare / light-therapy / hair-removal boom across five modalities: **IPL hair removal, diode-laser hair removal, RF skin tightening / RF microneedling, fractional laser resurfacing, and red/NIR LED therapy** — plus the adjacent cryolipolysis franchise, which shares the same academic origin. The through-line: nearly every foundational patent traces back to a small cluster of inventors (R. Rox Anderson and Dieter Manstein at Massachusetts General Hospital's Wellman Center; Shimon Eckhouse at ESC/Lumenis), those foundational patents have now **all expired** (2015–2025), and the resulting freedom-to-operate has unleashed a flood of OEM and design-patent filings, increasingly from Shenzhen.

---

## 1. Executive summary of the ownership map

| Modality | Foundational IP holder(s) | Key expired anchor | Who is filing now (2022–2026) |
|---|---|---|---|
| IPL hair removal | Shimon Eckhouse / ESC → Lumenis; MGH (Anderson) licensed to Palomar | US5405368 (1995), US5595568 (1997) — both expired 2015 | Home Skinovations/Silk'n, Philips, Shenzhen OEMs (Ulike, BSX) |
| Diode-laser hair removal (home) | SpectraGenics → TRIA Beauty | US7118563 (2006), expired 2025 | Few; category is small, TRIA-dominated |
| RF skin tightening / microneedling | Thermage → Solta (Knowlton) | US5919219 (1999), expired 2015 | Solta/Bausch, BTL, Lutronic/Cynosure, home-RF entrants |
| Fractional laser resurfacing | Reliant → Solta; MGH (Manstein/Anderson) | US7282060 (2007), expired 2023 | Solta, Lutronic, Chinese fractional-laser OEMs |
| Red/NIR LED therapy | Highly fragmented; no single foundational holder | (broad prior art) | L'Oréal, Shanghai Edge (CurrentBody-style masks), Dyson |
| *(adjacent)* Cryolipolysis | MGH (Anderson/Manstein) → licensed to ZELTIQ/Allergan | US7367341 (2008), expired 2023 | Allergan/AbbVie + numerous copycats |

The single most important structural fact: **the two hair-removal cornerstones (Eckhouse's flashlamp patent and Anderson's optical-pulse hair-removal patent) both expired on/around Feb 2015**, and TRIA's home diode-laser cornerstone expired **March 2025** [[1]](https://patents.google.com/patent/US5405368A/en)[[2]](https://patents.google.com/patent/US7118563B2/en)[[7]](https://en.wikipedia.org/wiki/Intense_pulsed_light). That is the legal precondition for today's sub-$300 IPL market.

---

## 2. Foundational / most-cited patents by modality

### 2.1 IPL (intense pulsed light) hair removal

The IPL field has two roots. The **device root** is Shimon Eckhouse's flashlamp patent; the **hair-removal method root** is R. Rox Anderson's MGH optical-pulse patent, which Palomar in-licensed and famously enforced.

- **US5405368A — "Method and apparatus for therapeutic electromagnetic treatment"** — inventor **Shimon Eckhouse**, assignee **ESC Inc** (the predecessor lineage to ESC Medical / Lumenis). Priority **Oct 20, 1992**, granted **Apr 11, 1995**, **expired**. This is the seminal non-laser *pulsed flashlamp* patent — variable pulse widths (10⁻⁵–10⁻¹ s), broad filterable spectrum, iris control — and its child applications explicitly extended into hair depilation [[1]](https://patents.google.com/patent/US5405368A/en). Eckhouse is widely credited as the inventor of clinical IPL, and this is the patent usually cited as the origin.

- **US5595568A — "Permanent hair removal using optical pulses"** — inventors **R. Rox Anderson, Melanie Grossman, William Farinelli**, assignee **General Hospital Corp (Massachusetts General Hospital)**. Filed **Feb 1, 1995**, granted **Jan 21, 1997**, **expired Feb 1, 2015**. Covers large-area optical hair removal at 680–1200 nm, 10–30 ms pulses, 30–50 J/cm² fluence, using a transparent contact device (with optional 4–15 °C cooling) to spare the epidermis while heating follicular melanin [[8]](https://patents.google.com/patent/US5595568A/en). **Palomar Medical Technologies in-licensed this MGH family and licensed it out to ~10 competitors**, litigating aggressively — it is the "hair-removal patent" behind the mid-2000s licensing wars [[9]](https://www.biospace.com/palomar-medical-technologies-successful-in-u-s-patent-office-re-examination-of-hair-removal-patent).

**Market consequence:** because both the Eckhouse device root (2015) and the Anderson MGH method root (2015) expired a decade ago, the *core* of IPL hair removal is firmly in the public domain. New IPL patents today are almost all **incremental** — cooling, skin-tone sensing, safety interlocks, form factor — or **design (D-series)** patents, which is exactly the Shenzhen-OEM pattern (see §4).

Home-IPL incumbents build on this base:
- **Home Skinovations Ltd. (the Silk'n brand)** holds a substantial home-IPL/skin-treatment portfolio (Justia lists the assignee "Home Skinovations Ltd.," with related assets later moving to "Silk'n Beauty Ltd." in 2023) [[5]](https://patents.justia.com/assignee/home-skinovations-ltd). I could not verify a single canonical Silk'n patent *number* to the level of a fetched claims page, so I describe it qualitatively rather than cite a specific number. *(One number I probed, US8579952, turned out to be a Wuhan Miracle Laser apparatus — unrelated — a good reminder not to guess.)*
- **Philips (Koninklijke Philips NV)** is a heavy home-light-treatment filer — e.g. **US11471054B2 — "Light-based skin treatment device"** (priority Apr 12, 2017; granted Oct 18, 2022) adds an in-waveguide **image sensor** that images skin during treatment while a privacy interlock **prevents it from imaging the environment off-skin** [[12]](https://patents.google.com/patent/US11471054B2/en); and **US10932541B2 — "Skin treatment device"** (Philips, granted Mar 2, 2021) on friction control for photo-epilators and shavers [[11]](https://patents.google.com/patent/US10932541B2/en).

### 2.2 Diode-laser hair removal (home)

This category is essentially defined by one company: **TRIA Beauty** (formerly **SpectraGenics**).

- **US7118563B2 — "Self-contained, diode-laser-based dermatologic treatment apparatus"** — original assignee **SpectraGenics Inc** (renamed **TRIA Beauty, Inc.**; the patent later moved to Aesthete Holding Corporation). Priority **Feb 25, 2003**, granted **Oct 10, 2006**, **expired ~March 2025**. Covers a cordless, <1 kg handheld with one or more **diode-laser bars** + battery circuit, delivering 4–100 J/cm² for hair-regrowth inhibition [[2]](https://patents.google.com/patent/US7118563B2/en). This is the cornerstone of the *only* FDA-cleared at-home **laser** (as opposed to IPL) hair-reduction device.
- Continuations in the family include **US8551104B2** (same title, 2013) and **US9414888B2** ("Devices and methods for radiation-based dermatological treatments," a hand-held scanned-beam device) [[2]](https://patents.google.com/patent/US7118563B2/en).

**Market consequence:** with US7118563 expiring in 2025, expect diode-laser home devices to broaden — this is likely why Shenzhen entrants (Ulike, JOVS) increasingly market "laser" rather than IPL and are filing around cooling/optics (see §4).

### 2.3 RF (radiofrequency) skin tightening / RF microneedling

- **US5919219A — "Method for controlled contraction of collagen tissue using RF energy"** — inventor **Edward W. Knowlton**, original assignee **Thermage Inc**, now **Solta Medical Inc**. Priority **May 5, 1995**, granted **Jul 6, 1999**, **expired ~May 2015**. This is the **Thermage foundational patent** — monopolar RF with a *reverse thermal gradient* (cooled surface, heated deep collagen) driving partial collagen denaturation and tightening [[3]](https://patents.google.com/patent/US5919219A/en). Solta (now under Bausch Health) built the Thermage/Thermage FLX franchise on this base.
- **RF microneedling** is the *hot* sub-field. The clinical devices (Lutronic **Genius**, Cynosure, **Morpheus8/InMode**, **Vivace**) each hold device-level IP — e.g., Genius markets a patented AI/real-time-tissue-feedback energy delivery — though I could not verify a single canonical Genius/Vivace *number* to a fetched claims page, so I flag it qualitatively. Notably, in **October 2025 the FDA issued a safety communication** about RF-microneedling burns/nerve-damage risks (Vivace, Morpheus8, Genius), and a **home-RF clinical trial (NCT06565884)** ran in 2023 — signaling active convergence toward *home* RF [[17]](https://www.aslms.org/about-aslms/media-center/news/2025/12/08/fda-safety-communication-on-rf-microneedling)[[18]](https://clinicaltrials.gov/study/NCT06565884).

**Filing trend:** RF microneedling and **home-RF** are among the most active 2022–2026 areas. Home-RF entrants (including Chinese cosmetic-instrument makers running trials like NCT06565884) are filing around dosing/safety, and Solta/BTL/InMode continue clinic-device filings. (Solta and BTL Industries have also litigated/settled RF patent disputes.)

### 2.4 Fractional laser resurfacing

Fractional photothermolysis was invented by **Dieter Manstein & R. Rox Anderson** at MGH's Wellman Center (the 2004 *Lasers Surg Med* paper), and commercialized by **Reliant Technologies** (Fraxel), now part of **Solta Medical** [[4]](https://pubmed.ncbi.nlm.nih.gov/15216537/)[[6]](https://patents.google.com/patent/US7282060B2/en).

- **US7282060B2 — "Method and apparatus for monitoring and controlling laser-induced tissue treatment"** — inventors DeBenedictis, Myers, Chan, Frangineas; assignee **Reliant Technologies → Solta Medical Inc** (page also shows a Hitachi lineage). Priority **Dec 23, 2003**, granted **Oct 16, 2007**, **expired Dec 23, 2023**. Covers the **closed-loop control** that made fractional practical: handpiece-motion detection with automatic adjustment of power/pulse-rate/wavelength to keep dose uniform regardless of hand speed, producing uniform microscopic treatment zones [[6]](https://patents.google.com/patent/US7282060B2/en).

**Market consequence:** with the Reliant control-loop patent expiring **end-2023**, fractional-resurfacing freedom-to-operate has opened up — fueling Chinese fractional-laser OEMs and cheaper clinic/home hybrids.

### 2.5 Red / NIR LED therapy (masks)

Unlike the laser/IPL/RF fields, LED phototherapy has **no single dominant foundational patent** — the space is fragmented with lots of prior art, so IP here is largely **form-factor, light-guide, and control** patents, plus a wave of **design patents** on mask shapes. This low IP barrier is exactly why LED masks are the most crowded consumer category.

- **US11642546B2 — "LED Facial Mask"** — inventor **Wenhui Dai**, assignee **Shanghai Edge Light Industry Co Ltd**. Granted **May 9, 2023** (term to ~2034). Covers a wearable mask with a thin (0.3–0.7 mm) **transparent light guide** with a dot/dash extraction pattern distributing red (630 nm), yellow (590 nm), or blue (470 nm) light, USB-powered, with a vision cut-out [[10]](https://patents.google.com/patent/US11642546B2/en). (This is a representative mask patent; it is *not* a CurrentBody-owned patent despite the similar product category.)
- **L'Oréal** is publicly pushing into the space — announcing (early 2026) a flexible silicone **LED Face Mask** co-developed with iSmart using 630 nm red + 830 nm NIR, plus infrared beauty devices — signaling a major incumbent staking LED/IR IP [[19]](https://wwd.com/beauty-industry-news/beauty-features/loreal-infrared-led-eye-masks-straightener-skin-hair-1238436469/).

---

## 3. Notable expired / expiring foundational patents (and why they mattered)

| Patent | Assignee | Modality | Expired | Why it opened the floodgates |
|---|---|---|---|---|
| US5405368 | ESC (→ Lumenis) | IPL device (flashlamp) | ~2015 | Core *pulsed-light device* concept became public — any OEM can build an IPL flashlamp [[1]](https://patents.google.com/patent/US5405368A/en) |
| US5595568 | General Hospital Corp (MGH; Palomar-licensed) | IPL/light hair removal | Feb 2015 | The heavily-licensed/litigated "hair-removal method" — its expiry ended the licensing chokehold Palomar had over ~10 competitors [[8]](https://patents.google.com/patent/US5595568A/en)[[9]](https://www.biospace.com/palomar-medical-technologies-successful-in-u-s-patent-office-re-examination-of-hair-removal-patent) |
| US5919219 | Thermage → Solta | Monopolar RF tightening | ~2015 | Reverse-thermal-gradient RF tightening entered public domain, enabling RF copycats [[3]](https://patents.google.com/patent/US5919219A/en) |
| US7282060 | Reliant → Solta | Fractional laser control | Dec 2023 | Closed-loop fractional dosing opened up; cheaper fractional devices followed [[6]](https://patents.google.com/patent/US7282060B2/en) |
| US7118563 | SpectraGenics/TRIA | Home diode-laser hair removal | ~Mar 2025 | The at-home *laser* cornerstone expired — expect diode-laser home entrants [[2]](https://patents.google.com/patent/US7118563B2/en) |
| US7367341 | General Hospital Corp (MGH → ZELTIQ) | Cryolipolysis (adjacent) | ~Oct 2023 | CoolSculpting's core "selective fat cooling" method opened; cheap cryo units proliferate [[13]](https://patents.google.com/patent/US7367341B2/en) |

**The pattern:** the entire *first generation* of energy-based aesthetic IP — assembled 1995–2007 by a handful of MGH inventors plus Eckhouse and Knowlton — has now lapsed. This is the structural reason a Shenzhen OEM can ship an FDA-notified IPL device for a fraction of a clinic's cost: the physics is unpatented; only the *implementation details* (cooling, sensing, safety, industrial design) remain patentable.

---

## 4. Who is filing 2022–2026, and in what modality

The active-filing frontier splits cleanly into **(a) incremental improvements by incumbents** and **(b) a surge of Shenzhen OEM design + utility patents**.

**Shenzhen / Chinese OEM surge (IPL & laser hair removal):**
- **Shenzhen Ulike Smart Electronics Co Ltd** — **EP4331430A4 "Hair Removal Device"** (priority Nov 15, 2021; filed Aug 19, 2022; published Sep 11, 2024; granted Mar 2026). Covers laser/light follicle treatment with **Peltier (sapphire ice) cooling** and thermally-stabilized mirrors/prisms; the family spans **US/EP/JP/KR/AU/CA/IL/MX/TW** — i.e., Ulike is building a real multi-jurisdiction fence around its "Sapphire Air" cooling story [[16]](https://patents.google.com/patent/EP4331430A4/en). Ulike (marketing "1,000+ global patents") epitomizes the OEM-turned-IP-filer trend.
- **Shenzhen BSX Technology Electronics Co Ltd** — **USD1031162S "IPL hair removal device"** (design patent, filed Dec 22, 2022; granted **Jun 11, 2024**) — representative of the **design-patent land-grab** on device housings [[14]](https://patents.justia.com/patent/D1031162).
- Numerous additional Shenzhen hair-removal design patents (e.g., **USD1013269**, granted Jan 30, 2024) confirm the volume.

**Incumbent incremental filings (sensing / safety / imaging):**
- **Philips** — US11471054 (2022, in-waveguide skin imaging + off-skin privacy interlock) [[12]](https://patents.google.com/patent/US11471054B2/en); ongoing home-light-treatment filings.
- **Dyson (Dyson Technology Ltd)** — **US20240245300A1 "Skincare device"** (priority Jun 4, 2021; published Jul 25, 2024) — a **spectral-sensor + machine-learning** device that reads skin reflectance (haemoglobin, collagen, elastin, melanin), classifies wrinkles/pores/roughness with an ML model, and **autonomously tunes multi-source light therapy per facial region** [[15]](https://patents.google.com/patent/US20240245300A1/en). A major consumer-electronics entrant staking AI-dosed phototherapy IP.
- **L'Oréal** — publicly filing/announcing red+NIR LED masks and infrared devices (2026) [[19]](https://wwd.com/beauty-industry-news/beauty-features/loreal-infrared-led-eye-masks-straightener-skin-hair-1238436469/).
- **Solta/Bausch, InMode, Lutronic/Cynosure, BTL** — continued RF-microneedling clinic-device filings; home-RF entrants filing around dosing/safety.

**Hottest sub-fields, verified:** **RF microneedling** (clinical, now migrating toward home — FDA safety communication Oct 2025; home-RF trial NCT06565884 in 2023) and **LED masks** (lowest IP barrier, most entrants, now attracting L'Oréal/Dyson-class players).

---

## 5. Representative recent (2023–2026) applications — where invention is heading

These verified filings show the direction of travel: **skin-sensing + AI dosing, imaging with privacy interlocks, and cooling/safety.**

| Publication # | Applicant | Modality | Filed / Published | What it covers |
|---|---|---|---|---|
| **US20240245300A1** | Dyson Technology Ltd | LED/light therapy | Priority 2021-06-04 / Pub 2024-07-25 | Spectral sensor + ML classifier reads skin constituents & wrinkles, then **autonomously tunes multi-region light therapy**; tracks color-change indicators to know when to stop [[15]](https://patents.google.com/patent/US20240245300A1/en) |
| **US11471054B2** | Koninklijke Philips NV | IPL / light treatment | Priority 2017-04-12 / Granted 2022-10-18 | In-waveguide **image sensor** images skin during treatment; **safety/privacy interlock** blocks imaging when off-skin; images used to locate device & adjust parameters [[12]](https://patents.google.com/patent/US11471054B2/en) |
| **EP4331430A4** | Shenzhen Ulike Smart Electronics | Laser/light hair removal | Filed 2022-08-19 / Pub 2024-09-11 | **Peltier ice-cooling** + thermally-stabilized optics for follicle treatment; broad multi-country family [[16]](https://patents.google.com/patent/EP4331430A4/en) |
| **US11642546B2** | Shanghai Edge Light Industry | Red/NIR LED mask | Granted 2023-05-09 | Thin **transparent light-guide** mask, multi-wavelength (630/590/470 nm), USB-powered [[10]](https://patents.google.com/patent/US11642546B2/en) |
| **USD1031162S** | Shenzhen BSX Technology | IPL hair removal (design) | Filed 2022-12-22 / Granted 2024-06-11 | Ornamental design of an IPL housing — representative of the OEM **design-patent** wave [[14]](https://patents.justia.com/patent/D1031162) |

**Direction of invention (verified themes):** (1) **skin-sensing / AI dosing** — spectral + ML classifiers that pick wavelength/fluence per skin region (Dyson) and imaging-based feedback (Philips); (2) **cooling** as the primary differentiator now that the underlying physics is off-patent (Ulike sapphire/Peltier); (3) **safety interlocks** (Philips off-skin privacy lockout; RF-microneedling safety scrutiny post-2025 FDA communication); (4) **hybrid/multi-modal + connectivity** — devices bundling light + galvanic/RF and Bluetooth app-controlled dosing (seen across recent hair-removal filings).

---

## 6. Honest uncertainty / caveats

- **Silk'n / Home Skinovations** and **Lutronic Genius / Vivace RF-microneedling**: I confirmed the *assignees* and portfolios exist (Justia lists Home Skinovations Ltd. and its 2023 move to Silk'n Beauty Ltd. [[5]](https://patents.justia.com/assignee/home-skinovations-ltd); Genius markets patented AI feedback), but I did **not** verify a single canonical *patent number* to a fetched claims page for either, so I have deliberately **not** cited a number for them.
- Some early Palomar/MGH hair-removal continuations (beyond US5595568) exist; I anchored on the one number whose claims page I actually opened.
- Expiration dates shown are the "anticipated/lifetime" dates on the Google Patents pages; small differences (terminal disclaimers, PTA) can shift them by months.
- L'Oréal's 2026 LED-mask and Dyson's device are at the *application/product-announcement* stage — grants may still be pending.

---

## Sources

1. Google Patents — US5405368A "Method and apparatus for therapeutic electromagnetic treatment" (Shimon Eckhouse / ESC Inc) — https://patents.google.com/patent/US5405368A/en — foundational IPL flashlamp patent, priority 1992, granted 1995, expired; child apps extend to hair depilation.
2. Google Patents — US7118563B2 "Self-contained, diode-laser-based dermatologic treatment apparatus" (SpectraGenics → TRIA Beauty) — https://patents.google.com/patent/US7118563B2/en — home diode-laser cornerstone; <1 kg, diode-laser bars, 4–100 J/cm²; priority 2003, granted 2006, expired ~Mar 2025.
3. Google Patents — US5919219A "Method for controlled contraction of collagen tissue using RF energy" (Thermage → Solta Medical; inventor Knowlton) — https://patents.google.com/patent/US5919219A/en — Thermage foundational monopolar-RF reverse-thermal-gradient patent; priority 1995, granted 1999, expired ~2015.
4. PubMed — Manstein D, Herron GS, Sink RK, Tanner H, Anderson RR (2004), "Fractional photothermolysis: a new concept for cutaneous remodeling…" — https://pubmed.ncbi.nlm.nih.gov/15216537/ — establishes MGH (Manstein/Anderson) as inventors of fractional photothermolysis, commercialized by Reliant.
5. Justia Patents — "Patents Assigned to Home Skinovations Ltd." — https://patents.justia.com/assignee/home-skinovations-ltd — confirms Home Skinovations (Silk'n) home-IPL/skin-treatment portfolio and later reassignment to Silk'n Beauty Ltd. (2023).
6. Google Patents — US7282060B2 "Method and apparatus for monitoring and controlling laser-induced tissue treatment" (Reliant Technologies → Solta Medical) — https://patents.google.com/patent/US7282060B2/en — closed-loop fractional dosing control; priority 2003, granted 2007, expired Dec 2023.
7. Wikipedia — "Intense pulsed light" — https://en.wikipedia.org/wiki/Intense_pulsed_light — corroborates Eckhouse (US5405368, filed 1992/granted 1995) as first detailed IPL patent and IPL market history.
8. Google Patents — US5595568A "Permanent hair removal using optical pulses" (Anderson/Grossman/Farinelli; General Hospital Corp/MGH) — https://patents.google.com/patent/US5595568A/en — foundational light hair-removal method (680–1200 nm, 10–30 ms, 30–50 J/cm², contact cooling); filed 1995, granted 1997, expired Feb 2015.
9. BioSpace — "Palomar Medical Technologies Successful in U.S. Patent Office Re-Examination of Hair Removal Patent" — https://www.biospace.com/palomar-medical-technologies-successful-in-u-s-patent-office-re-examination-of-hair-removal-patent — Palomar in-licensed the MGH hair-removal family (US5595568 / US5735844) and licensed/litigated it against ~10 competitors.
10. Google Patents — US11642546B2 "LED Facial Mask" (Wenhui Dai / Shanghai Edge Light Industry Co Ltd) — https://patents.google.com/patent/US11642546B2/en — transparent light-guide mask, 630/590/470 nm, USB-powered; granted May 2023 (representative LED-mask patent, not CurrentBody-owned).
11. Google Patents — US10932541B2 "Skin treatment device" (Koninklijke Philips NV) — https://patents.google.com/patent/US10932541B2/en — friction-control for photo-epilators/shavers; Philips home-device filing, granted Mar 2021.
12. Google Patents — US11471054B2 "Light-based skin treatment device" (Koninklijke Philips NV) — https://patents.google.com/patent/US11471054B2/en — in-waveguide skin imaging with off-skin privacy/safety interlock; priority 2017, granted Oct 2022.
13. Google Patents — US7367341B2 "Methods and devices for selective disruption of fatty tissue by controlled cooling" (Anderson/Manstein; General Hospital Corp → ZELTIQ) — https://patents.google.com/patent/US7367341B2/en — cryolipolysis foundational patent; priority 2002, granted 2008, expired ~Oct 2023.
14. Justia Patents — USD1031162 "IPL hair removal device" (Shenzhen BSX Technology Electronics Co., Ltd.) — https://patents.justia.com/patent/D1031162 — Shenzhen OEM IPL design patent, filed Dec 2022, granted Jun 11 2024 (illustrates the design-patent land-grab).
15. Google Patents — US20240245300A1 "Skincare device" (Dyson Technology Ltd) — https://patents.google.com/patent/US20240245300A1/en — spectral-sensor + ML classifier reading skin constituents/wrinkles, autonomously tuning multi-region light therapy; priority 2021, published Jul 25 2024 (AI-dosing frontier).
16. Google Patents — EP4331430A4 "Hair Removal Device" (Shenzhen Ulike Smart Electronics Co Ltd) — https://patents.google.com/patent/EP4331430A4/en — laser/light follicle treatment with Peltier ice-cooling + thermally-stabilized optics; filed Aug 2022, published Sep 2024, multi-country family (US/EP/JP/KR/AU/CA/IL/MX/TW).
17. ASLMS — "FDA Safety Communication on RF Microneedling" (Dec 2025 summary of Oct 2025 FDA communication) — https://www.aslms.org/about-aslms/media-center/news/2025/12/08/fda-safety-communication-on-rf-microneedling — FDA warned of burns/nerve damage from Vivace/Morpheus8/Genius; signals safety-focused RF filing pressure.
18. ClinicalTrials.gov — NCT06565884 "Safety, Efficacy of Home RF Cosmetic Instrument…" — https://clinicaltrials.gov/study/NCT06565884 — evidence of home-RF migration; trial ran Mar–Sep 2023.
19. WWD — "L'Oréal Unveils LED Eye Masks, Infrared Hair Straightener" — https://wwd.com/beauty-industry-news/beauty-features/loreal-infrared-led-eye-masks-straightener-skin-hair-1238436469/ — L'Oréal red (630 nm) + NIR (830 nm) LED mask (with iSmart) and infrared devices; incumbent staking LED/IR IP (2026).
