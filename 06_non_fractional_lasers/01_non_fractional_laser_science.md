# Non-Fractional Laser Science: What This Category Is

*Compiled 2026-07-03. Confidence legend: ✅ verified from FDA/primary source · ⚠️ marketing/spec claim · 🔍 inference from physics or device class.*

## 1. The taxonomy correction

The project now has three separate "laser" buckets:

| Bucket | Examples | Energy pattern | Main goal |
|---|---|---|---|
| **Hair-removal diode lasers** | Tria 4X/Precision, DermRays V8S/V4S | Single-wavelength laser, usually 808/810nm, spot or window delivery | Follicle heating |
| **Fractional resurfacing lasers** | Clear + Brilliant, Tria FRX, PaloVia, YDUNVIE Iris/Dora | Microbeams / microscopic treatment zones with untreated skin between columns | Texture, pigment, collagen, resurfacing |
| **Non-fractional skin lasers** | **DermRays Revive**, NIRA-like warmers, long-pulsed 1064nm context | Continuous spot/field heating, not MTZ resurfacing | Wrinkles, bulk dermal heating, hair/vascular/pigment-adjacent claims |

The mistake this folder prevents: seeing "laser" and mentally upgrading the device into a **fractional resurfacer**. Those are different dose geometries.

## 2. Fractional vs non-fractional is about geometry, not wavelength

A fractional device creates many tiny thermal injuries per square centimeter and leaves intervening skin intact. That lets it push high local microbeam fluence while controlling coverage density and healing burden.

A non-fractional device treats a whole spot. The energy is spread across the entire treatment window, so the relevant variables are:

- **wavelength**: what absorbs the light and how deeply it travels
- **fluence**: J/cm2 over the whole spot
- **pulse duration**: how long tissue has to diffuse heat
- **spot size**: larger spots can penetrate more efficiently but spread energy over a larger area
- **cooling/contact sensing**: the safety margin for epidermis
- **cadence and overlap**: how much total heating accumulates across passes

This is why DermRays Revive at 1064nm / 5-10 J/cm2 / 400 ms is not comparable to Clear + Brilliant at 1440/1927nm fractional microbeams. Both are lasers; they do different tissue engineering.

## 3. What 1064nm means

1064nm sits in the near-infrared. Compared with shorter pigment/vascular wavelengths, it is generally:

- **less strongly absorbed by epidermal melanin**, which is why long-pulsed 1064nm Nd:YAG is a standard option for darker skin hair removal and vascular work;
- **deeper penetrating**, especially with larger spot sizes;
- **less directly "surface pigment" oriented** than 1927nm fractional thulium/diode resurfacing, which is designed around superficial water absorption and epidermal renewal.

Practical read for this project:

- **Hair removal:** 1064nm can be useful, especially for darker skin, but home fluence/power may be far below clinic Nd:YAG.
- **Wrinkles / collagen:** plausible via controlled dermal heating, but the dose geometry is bulk heating, not fractional remodeling.
- **Pigment / PIH:** be cautious. DermRays marketing says pigment; the strongest pigment-specific home-laser rationale in this repo remains **1927nm fractional**, not non-fractional 1064nm.

## 4. Where DermRays Revive fits

FDA K231910 describes DermRays Revive as:

| Spec | DermRays Revive |
|---|---|
| Applicant | Wuhan Lotuxs Technology Co., Ltd. |
| Device class | Powered laser surgical instrument |
| Product code | GEX |
| Wavelength | **1064nm +/- 10nm** |
| Pulse width | **400 ms** |
| Fluence | **5.0-10.0 J/cm2** |
| Spot size | **15 mm** |
| Working area | **1.766 cm2** |
| Use type | **Prescription use** |
| Indications | Hair removal, permanent hair reduction, wrinkles |
| Skin types | Fitzpatrick I-VI, including tanned skin |

That spec sheet is the fingerprint of a **long-pulse, non-fractional 1064nm diode laser**. It belongs next to other non-fractional lasers and bulk-heating devices, not next to Tria FRX or Clear + Brilliant.

## 5. Safety posture

Non-fractional lasers can still burn, pigment, or scar. The risk levers are less glamorous than the wavelength:

- do not overlap passes aggressively unless the IFU explicitly says to;
- do not treat recently tanned, inflamed, irritated, tattooed, or photosensitized skin without medical guidance;
- verify eye protection and contact-sensor behavior;
- treat "all skin types" as a clearance statement, not as permission to run high levels on pigment-prone facial skin;
- prescription-use labeling matters: retail availability does not erase the device's FDA use status.

## 6. Initial ranking logic

For **collagen/tightening**, non-fractional 1064nm and RF both sit in the broad "controlled dermal heating" family. RF has a much larger dedicated tightening literature; 1064nm has the benefit of optical selectivity and deeper penetration, but home 1064nm devices have much less public clinical evidence.

For **pigment**, this folder is not the lead lane. The project still ranks:

1. SPF/topicals base layer
2. In-office 1927nm / vascular/pigment lasers as appropriate
3. Verified home fractional 1927nm only if specs and safety are credible
4. Non-fractional 1064nm as experimental/adjacent, not primary

### Sources

- [FDA K231910 — DermRays Revive 510(k) summary](https://www.accessdata.fda.gov/cdrh_docs/pdf23/K231910.pdf)
- [DermRays skin-care technology page](https://www.dermrays.com/en-us/pages/skin-care-technology)
- [DermRays Revive product page](https://www.dermrays.com/products/dermrays-revive)
- [FDA K231910 database entry](https://www.accessdata.fda.gov/scripts/cdrh/cfdocs/cfpmn/pmn.cfm?id=K231910)

