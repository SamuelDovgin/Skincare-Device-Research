# Non-Fractional Laser Devices

Research thread: lasers that are **real lasers but not fractional resurfacing devices**. This is where devices like **DermRays Revive** belong: coherent/narrowband optical energy, but delivered as a larger non-fractional spot rather than microscopic treatment zones (MTZs).

> **Why this folder exists:** the fractional-laser section is about Clear + Brilliant / Fraxel / Tria FRX / YDUNVIE Iris-style MTZ resurfacing. DermRays Revive is FDA-cleared and technically interesting, but it is **1064nm, non-fractional, prescription-use, 15mm spot** hardware. It should not be ranked as an at-home Clear + Brilliant analog.

## TL;DR

1. **Non-fractional laser != fractional resurfacing.** A non-fractional laser treats a continuous spot/field. A fractional laser splits energy into many microcolumns, intentionally leaving untreated skin between columns for faster healing and remodeling density control.
2. **DermRays Revive is the anchor device here.** FDA K231910 lists it as **1064nm +/- 10nm**, **400 ms**, **5-10 J/cm2**, **15mm spot / 1.766 cm2 working area**, intended for **hair removal, permanent hair reduction, and wrinkles**, for Fitzpatrick I-VI including tanned skin, with **prescription use** labeling.
3. **1064nm is useful but not magic.** It penetrates more deeply and is less melanin-absorbed than shorter wavelengths, which is why long-pulsed Nd:YAG/1064nm is common for darker-skin hair removal and vascular work. But at home, a 5-10 J/cm2 long-pulse consumer-size unit is a very different exposure than an in-office Nd:YAG platform.
4. **For pigment/PIH:** 1064nm is not the same evidence lane as **1927nm fractional**. DermRays marketing leans hard into pigment/glow claims; the FDA file supports wrinkles + hair removal, while pigment-lesion language mainly enters through the professional Cynosure Elite+ predicate, not as proof of home-equivalent pigment outcomes.
5. **Power headline:** DermRays' FDA 5-10 J/cm2 over a 1.766 cm2 spot implies **8.83-17.66 J per pulse** and about **22.1-44.2 W average optical pulse power** over 400 ms. That is high-energy for a home/Rx-size device, but it is still non-fractional spot heating, not MTZ resurfacing.
6. **Clinical-grade reality check:** NIRA has a real FDA periorbital wrinkle endpoint, but public fluence is far below professional 1450nm workflows; DermRays has real 1064nm clearance, but no public human wrinkle/pigment outcome in the 510(k) summary. Neither maps to Clear + Brilliant the way Tria FRX does.
7. **Buying posture:** treat DermRays Revive as a separate Rx-class/non-fractional laser experiment, not as a substitute for Clear + Brilliant, Moxi, LaseMD, Tria FRX, or YDUNVIE Dora/Iris.

## Documents

| # | File | What it covers |
|---|------|----------------|
| 01 | [Non-fractional laser science](01_non_fractional_laser_science.md) | Device taxonomy, why non-fractional spot heating behaves differently from MTZ resurfacing, and what 1064nm is actually good for |
| 02 | [Device landscape](02_device_landscape.md) | DermRays Revive, 810nm wide-window hair lasers, NIRA/non-fractional 1450nm warmers, LYMA/LLLT, and pro 1064nm context |
| 03 | [DermRays Revive deep dive](03_dermrays_revive_deep_dive.md) | FDA K231910 specs, claims vs clearance, patent signal, buy/use implications, and open verification questions |
| 04 | [NIRA / DermRays professional-results gap](04_nira_dermrays_professional_results_gap.md) | Whether NIRA or DermRays can reach clinic-grade results; Tria/C+B comparison frame; dose, evidence, and practical ceiling |
| 05 | [DermRays power, patent, and device comparison](05_dermrays_power_patent_comparison.md) | Fluence-to-Joule math, NIRA/Tria/pro-1064 comparison, current product claims, patent map, and feature-verification checklist |

## Supporting material

- [`dose_geometry_simulator.html`](dose_geometry_simulator.html) visualizes non-fractional spot geometry, pulse energy, pulse power, area tiling, and fractional-vs-non-fractional assumptions.
- [`data/dermrays_power_comparison.json`](data/dermrays_power_comparison.json) stores the comparison assumptions used for the DermRays/NIRA/Tria/pro-context math.
- [`source_docs/`](source_docs/) now mirrors FDA K231910, K232117, K141425, K222685, K163137, K130459, plus current DermRays page snapshots captured 2026-07-09.
- [`patents_source_docs/`](patents_source_docs/) preserves Google Patents snapshots for the Revive-adjacent CN120132236A/B family and the Lotuxs handheld home-laser hair-removal family.

## Relationship to the other folders

- Hair-removal diode lasers at **810nm** still live mostly in [`02_diode_laser_hair_removal/`](../02_diode_laser_hair_removal/) because the goal is hair.
- True fractional resurfacing stays in [`03_fractional_laser_resurfacing/`](../03_fractional_laser_resurfacing/).
- LED/LLLT stays in [`04_red_light_therapy_handheld/`](../04_red_light_therapy_handheld/) unless a device is being compared mainly as "laser" marketing.
- Market/patent-wide context stays in [`05_market_patent_intelligence/`](../05_market_patent_intelligence/).

## Status / open items

- **Verified:** DermRays Revive FDA K231910 specs, Rx labeling, derived energy-per-pulse math, NIRA FDA comparison anchors, and Lotuxs patent-family snapshots.
- **Open:** independent bench output, IFU/manual, real treatment cadence, contraindications, eye-protection requirements, whether retail sale/use instructions match the prescription-use clearance, whether the SGS/marketing study details can be inspected, and which 2025 Chinese patent claims map to the shipping DermRays Revive unit.

### Sources

- [FDA 510(k) K231910 summary PDF — DermRays Revive](https://www.accessdata.fda.gov/cdrh_docs/pdf23/K231910.pdf)
- [FDA 510(k) database entry — K231910](https://www.accessdata.fda.gov/scripts/cdrh/cfdocs/cfpmn/pmn.cfm?id=K231910)
- [DermRays Revive official product page](https://www.dermrays.com/products/dermrays-revive)
- [DermRays skin-care technology page](https://www.dermrays.com/en-us/pages/skin-care-technology)
- [Google Patents CN120132236A — home laser spot-removal / anti-aging beauty instrument](https://patents.google.com/patent/CN120132236A/zh)
