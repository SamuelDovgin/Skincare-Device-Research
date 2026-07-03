# DermRays Revive Deep Dive

*Compiled 2026-07-03. This is technical research, not medical advice or a legal/regulatory opinion.*

## 1. Why it belongs here

DermRays Revive is a real FDA-cleared laser device, but it is **not** a fractional resurfacing laser.

The fractional folder ranks devices by closeness to Clear + Brilliant / Fraxel-style microscopic treatment zones. DermRays Revive uses a **15mm non-fractional 1064nm spot**. That makes it a separate class: more like a low-fluence, long-pulse, handheld 1064nm laser than a home Fraxel/C+B analog.

## 2. Verified FDA specs

| Field | DermRays Revive |
|---|---|
| FDA 510(k) | **K231910** |
| Applicant | **Wuhan Lotuxs Technology Co., Ltd.** |
| Device name | DermRays Revive |
| Model | LHR-S5-1064 |
| Product code | **GEX** |
| Regulation | 21 CFR 878.4810 |
| Device type | Powered laser surgical instrument |
| Use type | **Prescription use** |
| Wavelength | **1064nm +/- 10nm** |
| Pulse width | **400 ms** |
| Fluence | **5.0-10.0 J/cm2** |
| Spot size | **15mm** |
| Working area | **1.766 cm2** |
| Input | AC100-240V, 50/60Hz, 1.6A max |
| Indications | Hair removal, permanent hair reduction, treatment of wrinkles |
| Skin types | Fitzpatrick I-VI, including tanned skin |

The primary predicate is **Cynosure Elite+ Laser (K141425)**, and the secondary predicate is another Wuhan Lotuxs 1064nm diode hair-removal device **K232117**.

## 3. Claims vs clearance

| Claim area | What the FDA file supports | What needs caution |
|---|---|---|
| Hair removal | Explicitly intended for hair removal and permanent hair reduction | 5-10 J/cm2 at 1064nm may be modest vs in-office Nd:YAG hair-removal protocols |
| Wrinkles | Explicitly intended for treatment of wrinkles | Clinical effect size for this exact home/Rx device is not public in the summary |
| All skin types | FDA file says Fitzpatrick I-VI, including tanned skin | "Can be used" does not mean "use high settings aggressively" |
| Pigment/melasma/glow | Professional 1064nm predicate language includes pigmented lesions; DermRays marketing claims spot/glow benefits | The Revive indication itself is not a clean home melasma/PIH clearance; pigment-prone users should be conservative |
| Redness/rosacea | Marketing and testimonials claim redness benefits | 1064nm can be vascular-adjacent, but this home device's clinical data are not visible in the public 510(k) summary |

## 4. Patent signal

A Google Patents search surfaces **CN120132236A**, titled in translation as a home laser spot-removal / anti-aging beauty instrument. It describes a home laser device with:

- housing, treatment head, laser, circuit board;
- lens in the treatment head;
- contact/conductive columns around the treatment head;
- optical waveguide shaping;
- heat sink, fan, heat pipes;
- TEC cooling and temperature sensors.

**Read:** this looks directionally relevant to the DermRays/Lotuxs product family, but it is a **Chinese patent application**, not a proof that the shipping Revive unit uses every claimed feature. The key value is that it supports Lotuxs having its own home-laser engineering activity rather than merely reselling a generic laser.

## 5. How to think about the 1064nm mechanism

1064nm is valuable because it penetrates relatively deeply and is less epidermal-melanin-selective than shorter wavelengths. That makes it a workhorse in professional dermatology for darker-skin hair removal and some vascular/pigment contexts.

But the DermRays device has a specific home/Rx-scale exposure:

- **5-10 J/cm2** fluence;
- **400 ms** long pulse;
- **15mm** non-fractional spot;
- **no public MTZ density**, because there are no MTZs;
- **no public full protocol** in the FDA summary.

So the right expectation is controlled bulk heating and possible hair/wrinkle benefit, not fractional resurfacing.

## 6. Practical comparison to the repo's existing options

| Compared with | DermRays Revive is... |
|---|---|
| Clear + Brilliant / Moxi / LaseMD | Wrong geometry and wavelength for the same role; not a fractional resurfacer |
| Tria FRX / SmoothBeauty | Non-fractional, 1064nm, Rx; Tria FRX is fractional 1440/1450nm OTC for periorbital wrinkles |
| YDUNVIE Dora 1927nm | Much less directly pigment-resurfacing oriented; Dora claims superficial 1927nm fractional |
| NIRA | Higher-energy/deeper 1064nm laser concept, but still non-fractional; NIRA is lower-intensity 1450nm wrinkle warming |
| Tria 4X / DermRays V8S | Different wavelength/use: 1064nm wrinkle + hair claims vs 810nm hair-removal-only lane |
| Home RF | Both are controlled heating concepts; RF has a stronger dedicated skin-tightening home-device literature |

## 7. Purchase / verification checklist

Before treating this as purchase-grade:

1. Get the **full IFU/manual** for the exact shipped model.
2. Confirm whether the retail unit label says **LHR-S5-1064** and references **K231910**.
3. Ask whether the device is sold/used under **prescription supervision** in the U.S.; the FDA summary marks Rx, not OTC.
4. Ask for treatment cadence by area, pulse count limits, overlap instructions, and contraindications.
5. Ask what eye protection is required for 1064nm.
6. Ask whether the device has skin-contact, temperature, and motion/overlap safeguards.
7. Treat influencer before/afters as marketing until there is a controlled trial or at least a full IFU with protocol.

## 8. Bottom line

**DermRays Revive is the most interesting non-fractional home/Rx laser in this project so far.** It deserves a real file because it is not a fake IPL "laser" listing. But its role is not Clear + Brilliant at home. It is a 1064nm non-fractional laser with wrinkles + hair-removal clearance, broad marketing claims, and meaningful open questions around home protocol, Rx status, and real-world effect size.

### Sources

- [FDA 510(k) K231910 summary PDF — DermRays Revive](https://www.accessdata.fda.gov/cdrh_docs/pdf23/K231910.pdf)
- [FDA 510(k) database entry — K231910](https://www.accessdata.fda.gov/scripts/cdrh/cfdocs/cfpmn/pmn.cfm?id=K231910)
- [DermRays Revive product page](https://www.dermrays.com/products/dermrays-revive)
- [DermRays skin-care technology page](https://www.dermrays.com/en-us/pages/skin-care-technology)
- [DermRays certifications page](https://www.dermrays.com/en-us/pages/certifications)
- [Google Patents CN120132236A](https://patents.google.com/patent/CN120132236A/zh)

