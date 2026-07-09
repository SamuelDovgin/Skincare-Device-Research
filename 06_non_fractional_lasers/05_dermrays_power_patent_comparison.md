# DermRays Revive Power, Patent, and Device Comparison

*Compiled 2026-07-09. This is technical research orientation, not medical advice, purchase advice, or a legal opinion. Confidence legend: verified = primary source or direct math from primary source; limited = official marketing or small/undisclosed study claim; inference = physics/regulatory extrapolation.*

## 0. Bottom line

DermRays Revive should stay in the **non-fractional laser** category. It does not need a new archive folder because the existing lane already captures the key distinction: Revive is real 1064nm laser hardware, but it is not a fractional resurfacing device.

The highest-signal update is power geometry:

| Metric | DermRays Revive | What it means |
|---|---:|---|
| FDA-listed fluence | 5-10 J/cm2 | Higher than NIRA's public 2.1-3.8 J/cm2 range, but lower than many professional 1064nm hair-removal workflows |
| FDA-listed spot area | 1.766 cm2 | Large 15mm non-fractional spot, not microthermal zones |
| Calculated energy per pulse | 8.83-17.66 J | Fluence x area; supports that this is high-energy for a home-size device |
| FDA-listed pulse width | 400 ms | Long-pulse/bulk-heating exposure, not fractional injury |
| Calculated average optical power during pulse | 22.1-44.2 W | Energy divided by 0.4 seconds; an inference, not a separately published optical-output test |
| Public Revive human outcome evidence | Marketing study claims only | Official page claims SGS/8-week results, but K231910 does not publish a controlled wrinkle or pigment endpoint |
| Patent signal | Stronger than a generic reseller | 2025 CN patent claims a home 10 J/cm2 anti-aging/freckle laser architecture with contact sensing, waveguide shaping, TEC/fan cooling, and temperature sensors |

So the honest ranking is: **real hardware, plausible controlled dermal heating, strong marketing, incomplete clinical transparency.** It is more technically serious than LED/LLLT beauty lasers, but it is still not a Clear + Brilliant, Moxi, Fraxel, LaseMD, Tria FRX, or home 1927nm fractional resurfacer substitute.

## 1. Why this page exists

The previous DermRays pages answered "where does it belong?" This page answers the more detailed buyer/research question: **how powerful is it, what does it have, what do the patents suggest, and how does that compare to NIRA, Tria FRX, and professional 1064nm devices?**

What it does not do:

- it does not estimate tissue temperature;
- it does not create a safe treatment protocol;
- it does not treat patents as proof of shipping features;
- it does not treat FDA substantial equivalence as proof of professional-equivalent outcomes.

For the visual version, open [`dose_geometry_simulator.html`](dose_geometry_simulator.html).

## 2. Verified Revive spec sheet

FDA K231910 identifies DermRays Revive as model **LHR-S5-1064**, applicant **Wuhan Lotuxs Technology Co., Ltd.**, product code **GEX**, regulation **21 CFR 878.4810**, Class II powered laser surgical instrument, with **prescription use** labeling. The listed indication is hair removal, permanent hair reduction, and treatment of wrinkles, for Fitzpatrick I-VI including tanned skin. [[1]](source_docs/FDA_510k_K231910_DermRays_Revive.pdf)

| Field | DermRays Revive |
|---|---|
| FDA 510(k) | K231910 |
| Decision date | 2024-01-30 |
| Applicant | Wuhan Lotuxs Technology Co., Ltd. |
| Model | LHR-S5-1064 |
| Device type | Powered laser surgical instrument |
| Product code | GEX, with subsequent product codes OHS and OHT in the FDA database entry |
| Use type | Prescription |
| Wavelength | 1064nm +/- 10nm |
| Pulse width | 400 ms |
| Single-pulse max energy density | 5.0-10.0 J/cm2 |
| Handpiece spot size | 15mm |
| Working area | 1.766 cm2 |
| Input | AC100-240V, 50/60Hz, 1.6A max |
| Activation | Finger switch in the FDA comparison table |
| Predicates | Primary: Cynosure Elite+ Laser K141425; secondary: Lotuxs Diode Laser Hair Removal K232117 |
| Testing summarized | Biocompatibility, electrical/EMC, IEC 60601-2-22, IEC 60825-1, software V&V, shelf-life, cleaning/disinfection |

The FDA summary says Revive uses a 1064nm diode laser acting through the epidermis into the dermis, with absorption by melanin, hemoglobin, and water. That description supports the category placement, but it is still a manufacturer summary inside a substantial-equivalence file. [[1]](source_docs/FDA_510k_K231910_DermRays_Revive.pdf)

## 3. Power math: what "10 J/cm2" really becomes

DermRays markets **10 J/cm2** as the headline power number. The FDA file gives the inputs needed for a simple geometric calculation: [[1]](source_docs/FDA_510k_K231910_DermRays_Revive.pdf)

```text
Energy per pulse = fluence x spot area
At 5 J/cm2:  5 x 1.766 = 8.83 J
At 10 J/cm2: 10 x 1.766 = 17.66 J

Average optical pulse power = energy / pulse duration
At 5 J/cm2:  8.83 J / 0.400 s = 22.1 W
At 10 J/cm2: 17.66 J / 0.400 s = 44.2 W
```

That is meaningful for a handheld/home-size device. It is also the reason DermRays' "2.78x NIRA" marketing is directionally understandable: FDA K222685 lists NIRA Model 2 at **2.1, 2.4, 2.7, 3.2, and 3.8 J/cm2**, so 10 / 3.6 or 10 / 3.8 is roughly 2.6-2.8x by fluence. [[2]](source_docs/dermrays-revive-product-page-2026-07-09.html)[[5]](source_docs/FDA_510k_K222685_NIRA_Model_2.pdf)

But that comparison is incomplete in three ways:

1. **Wavelength differs.** DermRays is 1064nm; NIRA is 1450nm. Different absorption profile, different target logic.
2. **Pulse structure differs.** DermRays is a 400 ms pulse; NIRA Model 2 is a 2.0-3.1 second pulse train with 2 W max laser power. [[5]](source_docs/FDA_510k_K222685_NIRA_Model_2.pdf)
3. **Geometry differs from fractional lasers.** Tria and Clear + Brilliant use microbeams/MTZs. A big whole-spot Joule number is not the same variable as per-microbeam energy plus MTZ density.

## 4. Device comparison table

| Device/class | Wavelength | Energy geometry | Public power/dose anchor | Regulatory/evidence anchor | Best read |
|---|---:|---|---|---|---|
| **DermRays Revive** | 1064nm | Non-fractional 15mm spot | 5-10 J/cm2; 1.766 cm2; 400 ms; 8.83-17.66 J/pulse derived | FDA K231910 Rx wrinkles + hair removal; no public controlled endpoint in summary [[1]](source_docs/FDA_510k_K231910_DermRays_Revive.pdf) | Highest-interest experimental 1064nm home/Rx wrinkle laser |
| **NIRA Model 2 / Pro-class** | 1450nm | Non-fractional 12.5 x 13.8mm spot | 2.1-3.8 J/cm2; 2 W max; 2.0-3.1 sec pulse train [[5]](source_docs/FDA_510k_K222685_NIRA_Model_2.pdf) | K222685 uses K163137 predicate; original NIRA has 76-subject periorbital wrinkle endpoint [[4]](source_docs/FDA_510k_K163137_NIRA_Beauty_Skin_Laser.pdf)[[5]](source_docs/FDA_510k_K222685_NIRA_Model_2.pdf) | Lower-power, more transparent clinical wrinkle evidence |
| **NIRA original / Precision-class** | 1450nm | Non-fractional 4 x 4mm spot | 2.16-2.97 J/cm2; 0.8 sec pulse train [[5]](source_docs/FDA_510k_K222685_NIRA_Model_2.pdf) | K163137: 76-subject open-label periorbital wrinkle study [[4]](source_docs/FDA_510k_K163137_NIRA_Beauty_Skin_Laser.pdf) | Fine-line maintenance, especially periorbital |
| **Tria SmoothBeauty / FRX** | 1440/1450nm family | Fractional microbeam | Local IFU gives 5-12 mJ/pulse; FDA K130459 confirms 1450 +/- 50nm fractional wrinkle device [[6]](source_docs/FDA_510k_K130459_Tria_FAN_System.pdf) | Home fractional mechanism; periorbital wrinkle indication | Best home analog to low-density fractional NAFL logic |
| **Clear + Brilliant / Moxi / Fraxel-type** | 1440/1927/other | Fractional microthermal zones | Per-microbeam energy and MTZ density, not whole-spot fluence | Professional use, trained endpoint control | True resurfacing lane |
| **Cynosure Elite+ 1064nm context** | 1064nm | Professional long-pulse platform | K231910 predicate table lists 12 J/cm2 at 15mm and 4.7 J/cm2 at 24mm for the predicate comparison; platform input is 208/240VAC 30A [[1]](source_docs/FDA_510k_K231910_DermRays_Revive.pdf)[[3]](source_docs/FDA_510k_K141425_Cynosure_Elite_Plus.pdf) | K141425 includes vascular, benign pigmented lesions, wrinkles, PFB, and hair reduction language [[3]](source_docs/FDA_510k_K141425_Cynosure_Elite_Plus.pdf) | Predicate context only, not outcome equivalence |
| **Lotuxs V6S 1064nm hair device** | 1064nm | Wide non-fractional window | K232117 lists 4-7 J/cm2 variants and 30mm x 10mm working area; 5Hz repetition rate [[7]](source_docs/FDA_510k_K232117_Lotuxs_1064nm_Diode_Hair_Removal.pdf) | Hair removal/persistent hair reduction only | Helps explain Lotuxs 1064nm family lineage |

## 5. Claims vs evidence

| Claim | Source | Confidence | Read |
|---|---|---:|---|
| Revive is a 1064nm, 400 ms, 5-10 J/cm2, 15mm, Rx laser | FDA K231910 | Verified | This is the anchor fact. [[1]](source_docs/FDA_510k_K231910_DermRays_Revive.pdf) |
| Revive is intended for wrinkles and hair removal | FDA K231910 | Verified | Wrinkle indication is real; effect magnitude is not shown in the public summary. [[1]](source_docs/FDA_510k_K231910_DermRays_Revive.pdf) |
| Revive treats pigment/dark spots/chloasma | DermRays product page plus predicate spillover | Limited | The product page claims dark-spot results, but Revive's own FDA indication is not a clean pigment clearance. [[2]](source_docs/dermrays-revive-product-page-2026-07-09.html)[[3]](source_docs/FDA_510k_K141425_Cynosure_Elite_Plus.pdf) |
| "96% smoother skin" and "90% faded dark spots" | DermRays product page | Limited | The page references SGS/8-week/participant data, but it gives conflicting counts (56 participants in one place, 28 subjects in another) and not a full protocol/report. [[2]](source_docs/dermrays-revive-product-page-2026-07-09.html) |
| 10-minute treatments, 2-3x/week, 3 levels, contact sensor | DermRays product page | Limited | Useful current marketing/usage claim; still needs full IFU/manual and label verification. [[2]](source_docs/dermrays-revive-product-page-2026-07-09.html) |
| 10 J/cm2 is about 2.78x NIRA by fluence | DermRays product page plus FDA K222685 | Verified math from mixed sources | True by fluence arithmetic, but incomplete because wavelength, pulse train, spot geometry, and endpoints differ. [[2]](source_docs/dermrays-revive-product-page-2026-07-09.html)[[5]](source_docs/FDA_510k_K222685_NIRA_Model_2.pdf) |
| Revive can replace Clear + Brilliant | None found | No | Wrong geometry. It is non-fractional 1064nm, not NAFL MTZ resurfacing. |

## 6. Patent map

### CN120132236A/B: home laser freckle-removal and anti-aging beauty instrument

Google Patents lists **CN120132236A** as a 2025 Chinese application titled in English as **"A home-use laser freckle removal and anti-aging beauty instrument."** The current assignee is listed as **Wuhan Lotus Technology Co Ltd** (likely the same Lotuxs/Lotus translation family), inventor **Yang Lin**, priority and filing date **2025-05-14**, publication **2025-06-13**, grant publication **CN120132236B** on **2025-08-19**, status active, anticipated expiration **2045-05-14**. [[8]](patents_source_docs/google-patents-CN120132236A-home-laser-freckle-anti-aging-2026-07-09.html)

What it claims or describes:

- housing, treatment head, lens, laser, and circuit board;
- contact/conductive columns around the treatment head;
- annular circuit board controlling emission only when contact pins touch skin;
- optical waveguide that reshapes laser output toward a circular spot;
- heat sink, fan, heat pipes, TEC cooling, and temperature sensors;
- laser wavelength range 500-2000nm;
- peak power range 1-200 W;
- pulse-width range 1-900 ms;
- energy density of 10 J/cm2. [[8]](patents_source_docs/google-patents-CN120132236A-home-laser-freckle-anti-aging-2026-07-09.html)

**Interpretation:** this is the strongest Revive-adjacent patent signal. It matches the product story: home laser, anti-aging/freckle language, 10 J/cm2, contact sensing, waveguide shaping, and active cooling. It still does **not** prove that the shipping DermRays Revive unit contains every claimed element, and it does not prove clinical outcomes.

### WO2023077653A1 / US20240033000A1 / EP4424261B1: Lotuxs handheld home laser hair-removal system

Google Patents also shows a related Lotuxs/Lotus family for a handheld home laser hair-removal system, priority **2021-11-02**, PCT filing **2021-12-30**, publication **2023-05-11**. The Google page lists the PCT status as ceased but also lists US and EP family members, including **US20240033000A1** and **EP4424261B1**. [[9]](patents_source_docs/google-patents-WO2023077653A1-handheld-home-laser-hair-removal-2026-07-09.html)

This family is mainly hair-removal architecture, not the Revive skin-care device. It still matters because it shows Lotuxs engineering around:

- VCSEL / laser chip arrays;
- sapphire or optical waveguide treatment windows;
- cooling and thermal management;
- skin sensors;
- optional 755/810/1064nm laser-chip combinations. [[9]](patents_source_docs/google-patents-WO2023077653A1-handheld-home-laser-hair-removal-2026-07-09.html)

**Interpretation:** the hair-removal patent family supports Lotuxs as an active laser-device engineering company, but the Revive-specific evidence weight should rest on K231910 and CN120132236A/B.

## 7. What DermRays appears to have

Based on FDA, official product copy, and patents, the feature stack looks like this:

| Feature | Evidence | Confidence |
|---|---|---:|
| 1064nm diode laser | FDA K231910 | Verified |
| 15mm non-fractional treatment spot | FDA K231910 | Verified |
| 5-10 J/cm2 exposure range | FDA K231910 | Verified |
| 3 energy levels | Official product page | Limited |
| 400 ms pulse | FDA K231910 | Verified |
| Prescription-use status | FDA K231910 and FDA database | Verified |
| Skin-contact safeguard | Product page says contact sensor; CN patent describes contact columns; FDA comparison table says finger switch | Limited/mixed |
| Cooling/thermal management | CN patent describes TEC, fan, heat pipes, sensors; product page says painless/no downtime | Limited until IFU/teardown |
| Eye-protection requirements | Not found in public product page or K231910 summary | Unknown |
| Full user protocol, overlap rules, pulse-count limits | Not found publicly | Unknown |
| Independent bench output | Not found | Unknown |

The biggest practical missing item is still the **full IFU/manual**. For a 1064nm laser, the IFU matters more than the product page because it should define eye protection, contraindications, overlap, cleaning, stop rules, and exact protocol.

## 8. Purchase and research decision

**Do not make a new top-level category.** DermRays Revive belongs in `06_non_fractional_lasers/`.

For the user's actual skin-quality/pigment/collagen decision:

1. Choose true fractional NAFL when the goal is Clear + Brilliant-like texture/resurfacing logic.
2. Choose NIRA if the goal is lower-risk, transparent, daily fine-line maintenance with a public FDA clinical endpoint.
3. Treat DermRays Revive as the more interesting, higher-energy, non-fractional 1064nm experiment: stronger power geometry than NIRA, less public clinical transparency than NIRA, and not fractional.
4. Do not treat pigment/dark-spot marketing as proven until the full SGS report, IFU, or controlled pigment endpoint appears.

## Evidence gaps

- Full DermRays Revive IFU/manual.
- Retail label photos confirming LHR-S5-1064, K231910, Rx/OTC handling, warnings, and eye-protection language.
- Independent optical output or thermal bench testing.
- Full SGS clinical report, inclusion/exclusion criteria, endpoints, adverse events, treatment protocol, and whether participant count was 56 or 28.
- Published human outcomes for Revive wrinkles, pigment, or redness.
- Confirmation of which CN120132236B elements are actually present in shipping hardware.

## Sources

1. [Local FDA K231910 DermRays Revive 510(k) summary](source_docs/FDA_510k_K231910_DermRays_Revive.pdf) - primary source for Revive model, indication, Rx status, wavelength, pulse width, fluence, spot size, working area, predicates, and non-clinical tests.
2. [Local DermRays Revive product-page snapshot, captured 2026-07-09](source_docs/dermrays-revive-product-page-2026-07-09.html) - official marketing source for price/availability, 10 J/cm2 headline, 2-3x/week claim, 3 energy levels, SGS/8-week result claims, and NIRA/LYMA comparisons.
3. [Local FDA K141425 Cynosure Elite+ 510(k) summary](source_docs/FDA_510k_K141425_Cynosure_Elite_Plus.pdf) - primary source for professional 1064nm predicate indication language: vascular lesions, benign pigmented lesions, wrinkles, PFB, and hair reduction.
4. [Local FDA K163137 NIRA Beauty Skin Laser 510(k) summary](source_docs/FDA_510k_K163137_NIRA_Beauty_Skin_Laser.pdf) - primary source for NIRA original OTC periorbital wrinkle indication and 76-subject clinical endpoint.
5. [Local FDA K222685 NIRA Model 2 510(k) summary](source_docs/FDA_510k_K222685_NIRA_Model_2.pdf) - primary source for NIRA Model 2 spot size, 2 W max power, 2.1-3.8 J/cm2 fluence, pulse train, cooling, and treatment schedule.
6. [Local FDA K130459 Tria FAN System 510(k) summary](source_docs/FDA_510k_K130459_Tria_FAN_System.pdf) - primary source for Tria FAN/SmoothBeauty fractional 1450nm wrinkle device status; PDF is locally mirrored but renders oddly in some tools.
7. [Local FDA K232117 Lotuxs 1064nm Diode Hair Removal 510(k) summary](source_docs/FDA_510k_K232117_Lotuxs_1064nm_Diode_Hair_Removal.pdf) - primary source for Lotuxs 1064nm hair-removal predicate family and V6S/V6S-B specs.
8. [Local Google Patents CN120132236A snapshot](patents_source_docs/google-patents-CN120132236A-home-laser-freckle-anti-aging-2026-07-09.html) - patent source for home laser anti-aging/freckle instrument, 10 J/cm2 language, contact columns, optical waveguide, TEC/fan/heat-pipe cooling, and sensor architecture.
9. [Local Google Patents WO2023077653A1 snapshot](patents_source_docs/google-patents-WO2023077653A1-handheld-home-laser-hair-removal-2026-07-09.html) - patent source for Lotuxs handheld home laser hair-removal architecture, VCSEL/chip arrays, sapphire/window optics, cooling, sensors, and optional 755/810/1064nm family.
