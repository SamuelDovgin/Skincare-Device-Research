# Sourcing: RFQ Templates & Spec Sheet

Copy-paste RFQs for contacting suppliers. **Do not post "high intensity face laser"** — bad suppliers will pitch unsafe or fake-power devices. Use the precise wording below.

> **Regulatory note:** in the US, aesthetic/medical laser devices fall under both FDA radiation-emitting-product rules *and* medical-device rules depending on intended use. Ask for the actual **510(k) number**, not "FDA registered."

**Post two RFQs** for what the user wants: one for **1450nm fractional** (Tria/MimiSilk/PaloVia-like, the collagen/texture target) and one for **1927nm fractional** (Dora/Perméa-like, the pigment target).

---

## The universal spec sheet (require this from every supplier, same units)

```
Exact wavelength and tolerance: ___ nm ± ___ nm
Laser type: Diode / VCSEL / fiber / other
Fractional or non-fractional: ___
Fluence if non-fractional: ___ J/cm² at each level
Pulse energy if fractional: ___ mJ/pulse at each level
Pulse width / pulse train: ___ ms or ___ sec
Spot size / beam size: ___ mm² or ___ cm²
Beam profile: Gaussian / top-hat / other
Fractional microbeam diameter: ___ µm
Fractional density / coverage: ___ % or ___ beams/cm²
Repetition rate: ___ Hz
Cooling method: fan / contact cooling / sapphire / none
Contact sensor: yes/no
Skin contact lockout: yes/no
Skin tone sensor: yes/no
Eye safety design: describe
Treatment area: face / periorbital / full face / body
Battery / power: USB-C / adapter / rechargeable
Cartridge or lifetime: ___ pulses / hours
Warranty: ___ months
```

**Unit trap to police:** make them state whether each J/cm² or mJ figure is **single-pulse, pulse-train total, or full-treatment dose.** (Same multi-pulse inflation issue as the parent IPL repo's T055/T023 finding.)

---

## RFQ #1 — 1450nm fractional (collagen/texture; Tria/MimiSilk/PaloVia-like)

**Title:** OEM/ODM handheld 1450nm non-ablative diode laser skin rejuvenation device with FDA 510(k), IEC 60825-1, IEC 60601 reports

> We are sourcing a qualified OEM/ODM manufacturer of a **handheld non-ablative diode laser** skin-rejuvenation device for wrinkle reduction / texture improvement.
>
> **Target:** wavelength **1410–1450nm** (esp. 1450nm ±20–50nm); handheld diode; **home-use/OTC preferred** (or clearly-labeled professional). Both technology options welcome: **(a) fractional 1410–1450nm** (Tria/PaloVia/advanced-skin-renewing class) or **(b) non-fractional 1450nm** (NIRA/Iluminage class).
>
> Please complete the **universal spec sheet** above for every model, and provide:
> - FDA **510(k) number** + applicant name + **authorization letter** to private-label/export
> - FDA device listing + establishment registration (if applicable)
> - **IEC 60825-1** (laser safety), **IEC 60601-1** (electrical), **IEC 60601-1-2** (EMC), **IEC 60601-1-11** (home healthcare, if home-use), **IEC 60601-2-22** (laser equipment, if applicable)
> - **ISO 10993** biocompatibility (skin-contact parts), **ISO 13485**, **ISO 14971** risk file, **IEC 62366** usability, software validation (if applicable), CE/MDR, UKCA, RoHS, REACH, FCC
> - Device **label photo, IFU/manual**, and a **video of output measured on a calibrated meter**
>
> **Do not send generic "FDA registered" certificates.** Quote: sample price, MOQ, OEM/private-label cost, mold/shell cost, lead time, packaging, warranty.

**Reasonable benchmarks (✅):** NIRA Model 2 (K222685) is the cleanest *non-fractional* model: 1450±20nm, spot 12.5×13.8mm², 2W, fluence 2.1–3.8 J/cm². Tria FAN (K130459) is the *fractional* benchmark: 1450±50nm, periorbital.

---

## RFQ #2 — 1927nm fractional (pigment/brightening; Dora/Perméa-like)

**Title:** OEM/ODM handheld 1927nm non-ablative fractional laser for pigment/brightening with FDA/IEC files

> We are sourcing a **handheld 1927nm non-ablative fractional laser** for superficial pigment, dullness, and tone (home-use/OTC preferred).
>
> **Target:** 1927nm ±20nm, fractional microbeam output, contact/"ice" cooling, consumer handheld form factor (similar category to Clear+Brilliant Perméa / Sciton Moxi at a home dose).
>
> Complete the **universal spec sheet**, with special attention to: mJ/pulse per level, microbeam diameter, density, **treatment depth**, cooling temperature, and **Fitzpatrick/skin-tone restrictions** (pigment devices can worsen PIH). Provide the same regulatory package as RFQ #1.

---

## RFQ #3 — separate category: 1064nm higher-fluence (NOT a C+B analog — only if exploring)

**Title:** OEM/ODM 1064nm handheld diode laser (wrinkle/hair) with verified J/cm², pulse width, FDA/IEC files

> 1064nm handheld laser for wrinkle treatment and/or hair removal. Provide wavelength±, J/cm² per level, pulse width, spot size, cooling, **Rx vs OTC status**, Fitzpatrick support, eye-safety class, interlocks, FDA 510(k), IEC 60825-1 / 60601-2-22 reports.

**Benchmark (✅):** DermRays Revive (K231910): 1064±10nm, 400ms, 5–10 J/cm², 15mm spot — **prescription**, not OTC. So explicitly confirm Rx-vs-OTC.

---

## RFQ #4 — separate category: VCSEL/LLLT (JOVS/LYMA-like, gentle PBM)

**Title:** OEM/ODM VCSEL / low-level laser photobiomodulation facial device with mW/cm² report + FDA/IEC files

> PBM facial device (VCSEL/laser-diode/LED). Provide wavelengths (660/808/850nm…), irradiance mW/cm², treatment time, area, calculated J/cm² dose, emitter count, eye-safety class, FDA 510(k), IEC 60825-1, IEC 60601-1/EMC, biocompatibility.

**Benchmarks (✅):** JOVS/Qianyu mask (K244020): 660/850nm VCSEL, 40–100 mW/cm². LYMA (K210823): 808+620nm, 62.5 mW/cm², 8 cm².

---

## Supplier screening questions (send after first reply)
See [04_suppliers_and_companies §5](04_suppliers_and_companies.md) — manufacturer vs trader, legal name on FDA/CE docs, K-number coverage, label/IFU/UDI, OTC vs Rx, exact per-level output, single-vs-total energy, measuring lab, authorization letter.

## Red flags
See [04_suppliers_and_companies §6](04_suppliers_and_companies.md) — "FDA approved" with no K-number; "1450nm" with no J/cm² or mJ/pulse; "high energy" with no pulse width/spot/profile; no contact sensor / no IEC 60825-1; home-use claims for melasma/mole/tattoo removal; "fractional" that's actually CO₂/IPL/RF/808nm hair removal.

## Standards (why they're not random paperwork)
- **IEC 60825-1** — laser product safety classification (180nm–1mm). Mandatory for any laser.
- **IEC 60601-2-22** — medical/cosmetic laser equipment safety + performance.
- **IEC 60601-1-11** — home-healthcare-environment requirements (relevant for OTC home devices).
