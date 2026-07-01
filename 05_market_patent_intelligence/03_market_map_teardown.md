# 03 — Market Map & Product Teardown: What the Popular Devices Actually Are

*Research archive — compiled 2026-06-30. Every FDA clearance, price, and maker-of-record below was verified against a primary source (FDA 510(k)/MAUDE, the brand's own page, or a corporate filing) during this research pass. Where a spec is marketing-only or unverifiable, it is flagged as such. Specs marked "FDA" come from the device's 510(k) file and are the honest numbers; brands' headline "J per flash" figures are single-pulse energy, not fluence (J/cm²), and are noted where they differ.*

This is the map of the buzzy consumer devices people actually search for — sorted by what they *really are* under the hood, not by how they're marketed. The single most important throughline: **almost every at-home light/energy device is FDA-cleared for hair removal only** (product code **OHT** — "light-based over-the-counter hair removal"). "Skin rejuvenation," "photofacial," "anti-aging," and "spot correction" language is overwhelmingly *marketing*, not a cleared indication. [[35]](https://fda.report/Product-Code/OHT)

---

## 1. Master comparison table

| Device | Brand origin | Modality | Key specs (verified) | FDA clearance | Price (US) | Maker of record |
|---|---|---|---|---|---|---|
| **Ulike Sapphire Air 10** | 🇨🇳 own-brand | IPL, dual-lamp, sapphire cooling | 550–1200 nm; **2.79–6.41 J/cm²** (FDA); 3.9 cm² | **K242039** — OHT, hair removal only [[2]](https://www.accessdata.fda.gov/cdrh_docs/pdf24/K242039.pdf) | ~$349 (MSRP $399) | Shenzhen Ulike Smart Electronics [[2]](https://www.accessdata.fda.gov/cdrh_docs/pdf24/K242039.pdf) |
| **Ulike Sapphire Air 3** | 🇨🇳 own-brand | IPL, sapphire cooling | 550–1200 nm; **2.42–7.27 J/cm²** (FDA); 3.3 cm² | **K251984** — OHT, hair removal only [[1]](https://www.accessdata.fda.gov/cdrh_docs/pdf25/K251984.pdf) | ~$279 (MSRP $329) | Shenzhen Ulike Smart Electronics [[1]](https://www.accessdata.fda.gov/cdrh_docs/pdf25/K251984.pdf) |
| **Braun Silk-expert Pro 5** | 🇩🇪 brand / 🇬🇧 maker | IPL, SensoAdapt tone sensor | ~510–1200 nm; ~3–6 J/cm²; ~3 cm²; 400k flashes; 10 levels | **K190354** — OHT, hair removal only [[5]](https://fda.innolitics.com/submissions/SU/subpart-e%E2%80%94surgical-devices/OHT/K190354) | ~$420 | **CyDen Ltd** (Swansea, UK) [[9]](https://fda.report/PMN/K190354) |
| **Braun Silk-expert Pro 3** | 🇩🇪 brand / 🇬🇧 maker | IPL, SensoAdapt tone sensor | ~510–1200 nm; ~3–6 J/cm²; 300k flashes; 3 levels | **K190366** — OHT, hair removal only [[6]](https://fda.innolitics.com/submissions/SU/subpart-e%E2%80%94surgical-devices/OHT/K190366) | ~$250–300 | **CyDen Ltd** [[9]](https://fda.report/PMN/K190354) |
| **Philips Lumea 9000** | 🇳🇱 brand | IPL, SmartSkin auto-tone | 565–1400 nm; **2.5–6.5 J/cm²**; 450k flashes; 5 levels | **K243453** — OHT/GEX, hair removal only [[13]](https://www.accessdata.fda.gov/cdrh_docs/pdf24/K243453.pdf) | $400–580 (Amazon-excl.) | Koninklijke Philips NV [[12]](https://www.usa.philips.com/a-w/about/news/archive/standard/news/press/2025/its-not-me-its-you-an-official-breakup-letter-to-my-old-hair-removal-routine.html) |
| **Nood The Flasher 2.0** | 🇺🇸 brand / 🇨🇳 maker | IPL ("PrecisionPulse"), corded | 510–1200 nm; 4.5 J/cm²; 10 ms; finite ~500k flashes | Rides OEM's OHT 510(k)s; **no clearance under "Nood"** [[16]](https://www.accessdata.fda.gov/scripts/cdrh/cfdocs/cfmaude/detail.cfm?mdrfoi__id=16707096&pc=OHT) | ~$169–199 | **Shenzhen Beauty Every Moment** (via FDA MAUDE) [[16]](https://www.accessdata.fda.gov/scripts/cdrh/cfdocs/cfmaude/detail.cfm?mdrfoi__id=16707096&pc=OHT) |
| **JOVS Venus Pro II** | 🇨🇳 own-brand | IPL/"OPT," sapphire cooling | ~590–1200 nm (reviewer); ~6 J/cm²; 6 levels | OHT hair-removal clearances at maker level (K214113/K231800) [[20]](https://fda.innolitics.com/submissions/SU/subpart-e%E2%80%94surgical-devices/OHT/K231800) | ~$299 | Shenzhen Qianyu Technology [[20]](https://fda.innolitics.com/submissions/SU/subpart-e%E2%80%94surgical-devices/OHT/K231800) |
| **JOVS Blacken (DPL)** | 🇨🇳 own-brand | DPL "photofacial" (narrow-spectrum IPL) | 500–650 nm (Pro); Blacken X 532+755 nm | **No verified FDA clearance** — *not* a hair-removal product [[20]](https://fda.innolitics.com/submissions/SU/subpart-e%E2%80%94surgical-devices/OHT/K231800) | $369–449 | Shenzhen Qianyu Technology |
| **Tria Hair Removal Laser 4X** | 🇺🇸 brand | **Diode laser** (not IPL) | 810 nm; up to ~22 J/cm²; 5 levels; cordless | Cleared OTC for hair removal (the only at-home *laser*) [[21]](https://triabeauty.com/products/hair-removal-laser-4x) | ~$449 | Tria Beauty (now Beauty Tech Group) [[21]](https://triabeauty.com/products/hair-removal-laser-4x)[[36]](https://cosmeticsbusiness.com/currentbody-owner-the-beauty-tech-group-name-ex) |
| **MiMi Silk "Iris"** | 🇭🇰 dropship | Claimed 1450 nm fractional laser | Claims only; **no verified output** | **None found** — 0 matches in FDA DB [[24]](https://api.fda.gov/device/510k.json?search=applicant:mimisilk) | ~$699 | "Label Skincare Ltd," HK shell [[23]](https://www.mimisilk.com/policies/terms-of-service) |
| **Shark CryoGlow** | 🇺🇸 brand | LED mask + IR + under-eye cooling | Red/blue/IR LED + Peltier cooling | **Cleared Class II, Nov 27 2024** [[30]](https://ir.sharkninja.com/news/news-details/2025/Shark-Beauty-Skyrockets-to-1-Skincare-Facial-Devices-Brand-in-the-U-S-1/default.aspx) | ~$350 | SharkNinja / Shark Beauty [[30]](https://ir.sharkninja.com/news/news-details/2025/Shark-Beauty-Skyrockets-to-1-Skincare-Facial-Devices-Brand-in-the-U-S-1/default.aspx) |
| **Omnilux Contour Face** | 🇺🇸/🇬🇧 clinical | LED mask (flexible silicone) | 633 nm red + 830 nm NIR; 132 LEDs | LED cleared for wrinkles/appearance | ~$395 | Omnilux (GlobalMed Tech), self-made [[31]](https://omniluxled.com/pages/about-us) |
| **CurrentBody Series 2** | 🇬🇧 brand | LED mask (flexible silicone) | 3 wavelengths; 236 LEDs | LED cleared for appearance | ~$470 | The Beauty Tech Group [[32]](https://us.currentbody.com/blogs/editorial/currentbody-vs-omnilux)[[36]](https://cosmeticsbusiness.com/currentbody-owner-the-beauty-tech-group-name-ex) |
| **Clear + Brilliant** | 🇺🇸 clinical | **In-office** fractional laser | 1440 nm + 1927 nm (Touch) | **K-cleared professional device** (2011) [[26]](https://www.prnewswire.com/news-releases/solta-medical-announces-fda-510k-clearance-for-new-clear--brilliant-technology-121377129.html) | in-office (~$300–500/session) | Solta Medical / Bausch Health [[25]](https://www.prnewswire.com/news-releases/bausch-healths-aesthetics-business-solta-medical-announces-the-launch-of-clear--brilliant-touch-laser-in-canada-302694162.html) |
| **Dyson "skincare device"** | 🇬🇧 brand | Spectral sensor + phototherapy | *Patent only* — no product | N/A (not shipping) [[28]](https://patents.google.com/patent/US20240245300A1/en) | — | Dyson Technology Ltd [[28]](https://patents.google.com/patent/US20240245300A1/en) |

---

## 2. Teardown by modality

### 2.1 IPL hair removal — the crowded mainstream

This is the mature core of the market. Four "tiers" are visible once you look past the marketing:

**Tier 1 — Western brands, verifiable clearances.**
- **Philips Lumea** made the big 2025 move: after decades of *not* being sold in the US, Philips launched the **Lumea 9000 Series** in the US on **Aug 20, 2025**, Amazon-exclusive at **$400–580**, cleared under **K243453** (hair removal only). [[11]](https://www.usa.philips.com/c-p/BRI984_03/bri984-lumea-ipl-9000-series-ipl-hair-removal-device-with-se)[[12]](https://www.usa.philips.com/a-w/about/news/archive/standard/news/press/2025/its-not-me-its-you-an-official-breakup-letter-to-my-old-hair-removal-routine.html) Its older "Prestige"/8000 family (BRI949/954/956) is *still not* FDA-cleared and only reaches the US via grey-market import. [[11]](https://www.usa.philips.com/c-p/BRI984_03/bri984-lumea-ipl-9000-series-ipl-hair-removal-device-with-se) Honest specs (9000): **565–1400 nm, 2.5–6.5 J/cm², 450,000 flashes**. [[14]](https://www.wearebodybeautiful.com/philips-lumea-9000-series-review/)
- **Braun Silk-expert Pro 5 / Pro 3** carry the strongest "safety sensor" story (SensoAdapt reads skin tone ~80×/sec and auto-limits power). The twist: **Braun doesn't make them.** The FDA applicant and maker of record on both (**K190354**, **K190366**) is **CyDen Limited** of Swansea, UK — and the common "De'Longhi makes Braun" belief is wrong, because De'Longhi's Braun license covers only *household small appliances*, not grooming IPL. [[5]](https://fda.innolitics.com/submissions/SU/subpart-e%E2%80%94surgical-devices/OHT/K190354)[[6]](https://fda.innolitics.com/submissions/SU/subpart-e%E2%80%94surgical-devices/OHT/K190366)[[9]](https://fda.report/PMN/K190354)[[10]](https://www.prnewswire.com/news-releases/delonghi-and-procter--gamble-have-reached-an-agreement-for-the-perpetual-licensing-of-the-braun-brand-for-use-in-household-small-appliances-147896105.html)

**Tier 2 — Chinese own-brand vertical players (the ones eating the mainstream).**
- **Ulike** is the standout. It is *not* a Western brand hiding a Chinese OEM — it **is** a Shenzhen manufacturer (Shenzhen Ulike Smart Electronics) that files its own FDA 510(k)s and built a real global brand. The **Air 10** (dual-lamp, **K242039**) and **Air 3** (**K251984**) are cleared for hair removal only. Note the honesty gap: Ulike markets "26 J" / "21 J" per flash, but the **FDA-disclosed fluence is 2.79–6.41 and 2.42–7.27 J/cm²** respectively — the headline "J" is single-flash energy, not the dose that matters. [[1]](https://www.accessdata.fda.gov/cdrh_docs/pdf25/K251984.pdf)[[2]](https://www.accessdata.fda.gov/cdrh_docs/pdf24/K242039.pdf)[[3]](https://www.ulike.com/products/sapphire-air-3-ipl-hair-removal)[[4]](https://www.ulike.com/products/sapphire-air-10-ipl-hair-removal)
- **JOVS** (Shenzhen Qianyu Technology) splits its line: the **Venus Pro II** is a genuine IPL hair-removal device (maker-level OHT clearances), while the **Blacken "DPL" line** is a *skin-rejuvenation photofacial* device with **no verified FDA clearance** and "3× stronger than IPL" marketing that isn't substantiated. [[20]](https://fda.innolitics.com/submissions/SU/subpart-e%E2%80%94surgical-devices/OHT/K231800)

**Tier 3 — US marketing brands on Shenzhen hardware (true white-label).**
- **Nood The Flasher 2.0** is the textbook case. There is **no 510(k) under the name "Nood"** — its "FDA-cleared" claim rides on its Chinese OEM's clearances, and FDA's **MAUDE** adverse-event database explicitly names the manufacturer as **Shenzhen Beauty Every Moment Intelligent Electric Co., Ltd.** [[16]](https://www.accessdata.fda.gov/scripts/cdrh/cfdocs/cfmaude/detail.cfm?mdrfoi__id=16707096&pc=OHT) It's corded, 510–1200 nm, 4.5 J/cm², with a *finite* (~500k) flash count — not the "unlimited" some assume — backed by a free-handset-replacement policy. [[15]](https://trynood.com/products/the-flasher-2)[[17]](https://www.innerbody.com/nood-reviews)

**Tier 4 — thin dropship / unverifiable.**
- **MiMi Silk** is a Shopify storefront run by **"Label Skincare Limited," a Hong Kong shell (reg. 77505362)** at a known mass-registration address, domain registered **Dec 2024**, WHOIS hidden. It sells IPL ("Peach Fuzz"/"Cactus") *and* a **$699 "Iris" claimed to be a 1450 nm fractional laser** — a category that normally *requires* FDA clearance. A direct openFDA query returns **zero** clearances under either the brand or the legal entity, yet the site markets "FDA-cleared." The same "Iris" appears on a separate reseller site (awegene.com) — a dropship signal. Treat all medical/efficacy claims, especially the laser, with strong skepticism. [[22]](https://www.mimisilk.com/)[[23]](https://www.mimisilk.com/policies/terms-of-service)[[24]](https://api.fda.gov/device/510k.json?search=applicant:mimisilk)

### 2.2 Diode laser — the Tria exception

**Tria** is the only at-home **laser** (not IPL) with a real pedigree: an **810 nm diode laser**, cordless, up to ~22 J/cm², cleared OTC for hair removal — built on the foundational SpectraGenics/Tria patent (US7118563, which **expired in 2025**, see [doc 02](02_patent_landscape.md)). It concentrates more energy in a tiny spot than IPL, which is why it's slower but favored for stubborn/coarse hair. Tria now sits inside **The Beauty Tech Group** (with CurrentBody and Ziip), which pursued a ~£300M London IPO in 2025. [[21]](https://triabeauty.com/products/hair-removal-laser-4x)[[36]](https://cosmeticsbusiness.com/currentbody-owner-the-beauty-tech-group-name-ex) *(This archive covers Tria in depth in the `02_diode_laser_hair_removal/` folder.)*

### 2.3 LED masks — the fastest-growing, lowest-barrier category

LED has **no dominant foundational patent** (see [doc 02](02_patent_landscape.md)), which is exactly why it's the most crowded and fastest-growing type. Three honest tiers:
- **Clinically pedigreed & self-made: Omnilux** — originated from UK cancer-research phototherapy, now owned by GlobalMed Technologies, in 5,000+ derm offices, 40+ studies; its home masks (633 nm + 830 nm) use the same LED tech as its clinical units. [[31]](https://omniluxled.com/pages/about-us)
- **Consumer leaders: CurrentBody** (Series 2, 236 LEDs, 3 wavelengths) and **Shark CryoGlow** — the latter is the entrant story of the category: SharkNinja got a real **FDA Class II clearance (Nov 27, 2024)** and vaulted to **#1 US skincare facial-device brand** within a year by adding IR + under-eye Peltier cooling. [[30]](https://ir.sharkninja.com/news/news-details/2025/Shark-Beauty-Skyrockets-to-1-Skincare-Facial-Devices-Brand-in-the-U-S-1/default.aspx)[[32]](https://us.currentbody.com/blogs/editorial/currentbody-vs-omnilux)
- **The myth to retire:** the popular claim that "Omnilux secretly OEMs CurrentBody / Dr. Dennis Gross / HigherDOSE" is **not documented** — comparison teardowns show different LED counts and constructions, and the brands present as independent competitors. Silicone masks *look* alike, but "one shared OEM" is speculation without a filing or teardown to prove it. [[32]](https://us.currentbody.com/blogs/editorial/currentbody-vs-omnilux)

### 2.4 RF & microcurrent — the newest home shift

Energy that used to be clinic-only is migrating home: **microcurrent** (NuFACE, ZIIP, FOREO) and increasingly **RF / RF-microneedling** and Korean **multi-modal** wands (Medicube Age-R stacks microcurrent + EMS + RF). This is the direction of travel — covered in [doc 04](04_market_size_trends.md) (market) and [doc 05](05_frontier_emerging_tech.md) (frontier).

### 2.5 The in-office device people mis-search: Clear + Brilliant

**Clear + Brilliant is NOT an at-home device.** It's a **physician-administered, in-office fractional non-ablative laser** (1440 nm, plus 1927 nm on the "Touch" and "Perméa" variants), owned by **Solta Medical (Bausch Health)** and FDA-cleared as a professional device since 2011. [[25]](https://www.prnewswire.com/news-releases/bausch-healths-aesthetics-business-solta-medical-announces-the-launch-of-clear--brilliant-touch-laser-in-canada-302694162.html)[[26]](https://www.prnewswire.com/news-releases/solta-medical-announces-fda-510k-clearance-for-new-clear--brilliant-technology-121377129.html) People search it next to home gadgets because it's marketed as a *gentle "laser facial" with minimal downtime* ("Baby Fraxel"). The honest answer to "what's the at-home version?": **there isn't one.** No current consumer device does true fractional laser resurfacing. The one that ever did — **PaloVia** (Palomar, FDA-cleared 2009) — was discontinued around 2012. [[27]](https://wwd.com/beauty-industry-news/products/feature/palovia-the-wrinkle-fighting-laser-3428719-1207053/) The closest *legal* at-home categories are LED and mild RF — different, far weaker mechanisms.

### 2.6 The rumor to kill: "Dyson skincare device"

There is **no Dyson skin device** shipping or announced. Dyson's entire beauty line is hair/scalp. The only skin signal is a **pending patent application (US20240245300A1, published 2024)** for a spectral-sensor + phototherapy "skincare device" — R&D IP, not a product. The viral "Dyson Airwrap for your face" is actually Therabody's TheraFace. [[28]](https://patents.google.com/patent/US20240245300A1/en)[[29]](https://www.dyson.com/hair-care)

---

## 3. Branded vs OEM reality

The casual claim "it's all the same Shenzhen factory" is half-right. There are really **three** structures, and conflating them is the common error:

1. **Genuine white-label** — a Western marketing brand on Shenzhen ODM hardware. **Nood → Shenzhen Beauty Every Moment** is the clearest FDA-documented case. [[16]](https://www.accessdata.fda.gov/scripts/cdrh/cfdocs/cfmaude/detail.cfm?mdrfoi__id=16707096&pc=OHT)
2. **Chinese own-brand vertical players** — **Ulike** and **JOVS** are Shenzhen manufacturers that file their *own* clearances and sell under their *own* name. Not rebadged Western brands; Chinese OEMs that built brands. [[2]](https://www.accessdata.fda.gov/cdrh_docs/pdf24/K242039.pdf)[[20]](https://fda.innolitics.com/submissions/SU/subpart-e%E2%80%94surgical-devices/OHT/K231800)
3. **Premium self-manufacturers** — **Omnilux** (clinical LED), **CyDen** (the real maker behind Braun's IPL). [[9]](https://fda.report/PMN/K190354)[[31]](https://omniluxled.com/pages/about-us)

A large, openly-advertised OEM/ODM layer supplies rebrandable hardware to everyone else: **Shenzhen Semlamp** (states it does ODM for "domestic and international brand merchants," products in Walmart/Costco), **Fansizhe/MOOLWEEL** (FZ-series, filed via Shenzhen Ionka as **K230739**), **Mismon/Mlay**, **Sincoheren**, and dozens more offering "free logo, low MOQ, change it to your brand." [[33]](https://www.semlamp.com/en/Profile/)[[34]](https://fda.innolitics.com/device/K230739) The honest limit: NDAs mean these factories rarely name their Western customers, so "Factory X makes Brand Y" is only provable where an FDA filing or MAUDE record links them — which is why **Nood is the one confirmable smoking gun.**

---

## 4. Hype vs evidence — the red-flag checklist

| Claim you'll see | Reality |
|---|---|
| "FDA-cleared" (implying skin/anti-aging benefit) | Almost always cleared for **hair removal only** (OHT). Skin-tone/rejuvenation is not the cleared indication. [[35]](https://fda.report/Product-Code/OHT) |
| "FDA-cleared" (no K-number shown) | Verify it. Nood's is real but sits on its OEM's clearance; **MiMi Silk's has zero database matches.** [[16]](https://www.accessdata.fda.gov/scripts/cdrh/cfdocs/cfmaude/detail.cfm?mdrfoi__id=16707096&pc=OHT)[[24]](https://api.fda.gov/device/510k.json?search=applicant:mimisilk) |
| "Unlimited flashes / lifetime" | Usually a *finite* lamp (~250k–500k) plus a replacement policy (Nood, Philips, Braun disclose real counts). [[15]](https://trynood.com/products/the-flasher-2)[[14]](https://www.wearebodybeautiful.com/philips-lumea-9000-series-review/)[[5]](https://fda.innolitics.com/submissions/SU/subpart-e%E2%80%94surgical-devices/OHT/K190354) |
| "26 J!" / "21 J!" per flash | Single-flash energy, not fluence. The dose that matters (J/cm²) is only in the FDA file and is far lower (~2.4–6.5 J/cm²). [[1]](https://www.accessdata.fda.gov/cdrh_docs/pdf25/K251984.pdf)[[2]](https://www.accessdata.fda.gov/cdrh_docs/pdf24/K242039.pdf) |
| "3× stronger than IPL" / "clinic-grade" (DPL, dropship lasers) | Unsubstantiated marketing; often no clearance at all (JOVS Blacken, MiMi Silk Iris). [[20]](https://fda.innolitics.com/submissions/SU/subpart-e%E2%80%94surgical-devices/OHT/K231800)[[24]](https://api.fda.gov/device/510k.json?search=applicant:mimisilk) |
| "At-home Clear + Brilliant / fractional laser" | Doesn't exist for consumers. Clear + Brilliant is in-office; the one home fractional laser (PaloVia) is discontinued. [[25]](https://www.prnewswire.com/news-releases/bausch-healths-aesthetics-business-solta-medical-announces-the-launch-of-clear--brilliant-touch-laser-in-canada-302694162.html)[[27]](https://wwd.com/beauty-industry-news/products/feature/palovia-the-wrinkle-fighting-laser-3428719-1207053/) |
| "Dyson skincare device" | Not a product — a pending patent only. [[28]](https://patents.google.com/patent/US20240245300A1/en) |

**Bottom line:** the credible, verifiable IPL picks are the ones that publish real FDA files and honest specs — **Ulike, Braun (CyDen), Philips**. The mainstream is commoditizing on shared OEM hardware; differentiation is now cooling, tone-sensing, and industrial design, not the underlying light physics (which is off-patent — see [doc 02](02_patent_landscape.md)). Skepticism scales with the claim: hair-removal claims are usually honest; "skin rejuvenation," "laser facial at home," and no-K-number "FDA-cleared" claims are where the market gets loose.

---

## Sources

1. FDA 510(k) K251984 — Ulike Sapphire Air 3 (Shenzhen Ulike Smart Electronics) — https://www.accessdata.fda.gov/cdrh_docs/pdf25/K251984.pdf — Air 3: OHT, decision 2025-06-27, 550–1200 nm, 2.42–7.27 J/cm², 3.3 cm², hair removal only.
2. FDA 510(k) K242039 — Ulike Sapphire Air 10 (Shenzhen Ulike) — https://www.accessdata.fda.gov/cdrh_docs/pdf24/K242039.pdf — Air 10: OHT, decision 2024-11-06, dual-lamp, 550–1200 nm, 2.79–6.41 J/cm², 3.9 cm², Beurer predicate, hair removal only.
3. Ulike Sapphire Air 3 product page — https://www.ulike.com/products/sapphire-air-3-ipl-hair-removal — marketing specs, modes, cooling, pricing.
4. Ulike Sapphire Air 10 product page — https://www.ulike.com/products/sapphire-air-10-ipl-hair-removal — dual-lamp, SkinSensor, "26 J" per-flash marketing figure, pricing.
5. FDA 510(k) K190354 — Braun Silk-expert Pro 5 (applicant CyDen Ltd) — https://fda.innolitics.com/submissions/SU/subpart-e%E2%80%94surgical-devices/OHT/K190354 — Model 6031, OHT, hair-removal indication; maker CyDen.
6. FDA 510(k) K190366 — Braun Silk-expert Pro 3 (applicant CyDen Ltd) — https://fda.innolitics.com/submissions/SU/subpart-e%E2%80%94surgical-devices/OHT/K190366 — Model 6032, OHT, hair-removal indication; maker CyDen.
7. Braun US — Silk-expert Pro 5 PL5157 — https://us.braun.com/en-us/female-hair-removal/ipls/silk-expert-pro-5-pl5157 — 400k flashes, 10 levels + 3 modes, SkinPro 2.0/SensoAdapt.
8. Braun US — Silk-expert Pro 3 PL3020 — https://us.braun.com/en-us/female-hair-removal/ipls/silk-expert-pro-3-pl3020 — 300k flashes, 100 flashes/min, 3 levels, sensor + interlock.
9. fda.report — CyDen K190354 PMN — https://fda.report/PMN/K190354 — confirms CyDen Limited (Swansea, UK) as applicant/maker of record for Braun Silk-expert.
10. PR Newswire — De'Longhi / P&G Braun brand license — https://www.prnewswire.com/news-releases/delonghi-and-procter--gamble-have-reached-an-agreement-for-the-perpetual-licensing-of-the-braun-brand-for-use-in-household-small-appliances-147896105.html — De'Longhi license limited to household small appliances (not grooming IPL).
11. Philips US — Lumea 9000 Series BRI984/03 — https://www.usa.philips.com/c-p/BRI984_03/bri984-lumea-ipl-9000-series-ipl-hair-removal-device-with-se — US model, 5 settings, window sizes, SmartSkin.
12. Philips US press release (US launch, Aug 2025) — https://www.usa.philips.com/a-w/about/news/archive/standard/news/press/2025/its-not-me-its-you-an-official-breakup-letter-to-my-old-hair-removal-routine.html — Lumea US launch Aug 20 2025, Amazon-exclusive, $399.99–$579.99.
13. FDA 510(k) K243453 — Philips Lumea 9000 — https://www.accessdata.fda.gov/cdrh_docs/pdf24/K243453.pdf — OHT/GEX product code, hair-removal + permanent-reduction indication (accessed via FDA PDF).
14. We Are Body Beautiful — Philips Lumea 9000 review — https://www.wearebodybeautiful.com/philips-lumea-9000-series-review/ — 565–1400 nm, 2.5–6.5 J/cm², 450,000 flashes, window sizes.
15. Nood — The Flasher 2.0 product page — https://trynood.com/products/the-flasher-2 — IPL, 510–1200 nm, 4.5 J/cm², 10 ms, corded, "FDA-cleared" claim, ~$179–199.
16. FDA MAUDE report (mdrfoi 16707096) — Nood Flasher 2.0 manufacturer — https://www.accessdata.fda.gov/scripts/cdrh/cfdocs/cfmaude/detail.cfm?mdrfoi__id=16707096&pc=OHT — links "NOOD- THE FLASHER 2.0" to maker Shenzhen Beauty Every Moment Intelligent Electric Co., Ltd.
17. Innerbody — Nood Flasher 2.0 review — https://www.innerbody.com/nood-reviews — ~5 J/cm², corded, finite flash count, street price ~$169.
18. JOVS Venus Pro II product page — https://jovs.com/products/jovs-venus-pro-2-hair-removal-device — IPL/OPT, sapphire cooling, 6 modes/levels, ~$299.
19. JOVS Blacken DPL photofacial page — https://jovs.com/products/jovs-blacken-dpl-photofacial-skincare-device — DPL 500–650 nm, skin-rejuvenation marketing, $369.
20. FDA Innolitics K231800 — JOVS (Shenzhen Qianyu Technology) — https://fda.innolitics.com/submissions/SU/subpart-e%E2%80%94surgical-devices/OHT/K231800 — applicant Shenzhen Qianyu; "IPL Hair Removal Device"; OHT; hair-removal only (Blacken line has no verified clearance).
21. Tria Beauty — Hair Removal Laser 4X — https://triabeauty.com/products/hair-removal-laser-4x — 810 nm diode laser, cordless, OTC hair-removal clearance (the only at-home laser).
22. MiMi Silk homepage — https://www.mimisilk.com/ — product line (IPL/laser/LED), "FDA-cleared" marketing claims.
23. MiMi Silk Terms of Service — https://www.mimisilk.com/policies/terms-of-service — legal entity "Label Skincare Limited," HK reg. 77505362, New Mandarin Plaza Kowloon address.
24. openFDA 510(k) API, applicant:mimisilk / "label skincare" — https://api.fda.gov/device/510k.json?search=applicant:mimisilk — zero matches; no FDA clearance under brand or legal entity.
25. PR Newswire — Bausch Health/Solta launches Clear + Brilliant Touch (2026) — https://www.prnewswire.com/news-releases/bausch-healths-aesthetics-business-solta-medical-announces-the-launch-of-clear--brilliant-touch-laser-in-canada-302694162.html — confirms Clear + Brilliant is a physician-administered Solta/Bausch device (1440+1927 nm).
26. PR Newswire — Solta FDA 510(k) clearance for Clear + Brilliant (2011) — https://www.prnewswire.com/news-releases/solta-medical-announces-fda-510k-clearance-for-new-clear--brilliant-technology-121377129.html — professional-setting non-ablative fractional clearance, May 2011.
27. WWD — PaloVia: the wrinkle-fighting at-home laser — https://wwd.com/beauty-industry-news/products/feature/palovia-the-wrinkle-fighting-laser-3428719-1207053/ — first (and now discontinued) FDA-cleared at-home fractional laser.
28. Google Patents — US20240245300A1 "Skincare device" (Dyson Technology Ltd) — https://patents.google.com/patent/US20240245300A1/en — spectral-sensor + phototherapy patent application (pending), not a product.
29. Dyson Hair Care (official) — https://www.dyson.com/hair-care — Dyson's entire beauty lineup is hair/scalp; no skin device.
30. SharkNinja IR — Shark Beauty CryoGlow #1 facial device — https://ir.sharkninja.com/news/news-details/2025/Shark-Beauty-Skyrockets-to-1-Skincare-Facial-Devices-Brand-in-the-U-S-1/default.aspx — CryoGlow FDA clearance Nov 27 2024; #1 US skincare facial-device brand within a year.
31. Omnilux — About Us — https://omniluxled.com/pages/about-us — self-manufactured clinical LED brand (Paterson Institute origin, GlobalMed Technologies, 5,000+ derm offices).
32. CurrentBody vs Omnilux — https://us.currentbody.com/blogs/editorial/currentbody-vs-omnilux — treats them as independent competitors (236 vs 132 LEDs); refutes the "Omnilux inside" white-label assumption.
33. Shenzhen Semlamp company profile — https://www.semlamp.com/en/Profile/ — self-describes as ODM for "domestic and international brand merchants," products in Walmart/Costco.
34. FDA 510(k) K230739 (Shenzhen Ionka Medical) — https://fda.innolitics.com/device/K230739 — FZ-608/100/200 (Fansizhe/MOOLWEEL) family — the open OEM/ODM white-label layer.
35. FDA Product Code OHT reference — https://fda.report/Product-Code/OHT — OHT = "light-based over-the-counter hair removal"; the cleared indication for nearly all these devices is hair removal only.
36. Cosmetics Business — The Beauty Tech Group (CurrentBody/Ziip/Tria) IPO — https://cosmeticsbusiness.com/currentbody-owner-the-beauty-tech-group-name-ex — ~£300M London IPO; Tria and CurrentBody under one owner.
