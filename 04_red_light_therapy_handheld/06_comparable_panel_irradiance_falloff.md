# Comparable Red-Light Panel Irradiance Falloff

*Online measurement scan completed 2026-07-13; closest-comparator search and default curve re-audited 2026-08-11. This is a measurement-method comparison and PL300 model check, not medical advice or a product endorsement.*

## Bottom line

The PL300 seller's **falloff shape is possible for a large LED array**, but its absolute output is substantially higher than the closest accredited comparators. The strongest newly expanded evidence is a seven-panel 2025 PlatinumLED/LightLab family hosted on device.report. All seven reports used the same two spectral meters, combined red+NIR mode, stabilization standard, 49-point grid, and 6/12/18/24-inch protocol. The user-supplied BIOMAX 900 report is one member rather than an isolated example.

The four closest members by package count or measured input are BIOMAX 600, BIOMAX 900, PRO GRANDE, and PRO MIDI. Their raw six-inch grid averages are **84.30, 83.13, 84.15, and 90.27 mW/cm²**, but they drive each package harder than the claimed PL300 configuration. Normalizing measured watts per package to `360 W / 300 packages` produces **58.54, 61.78, 58.43, and 61.44 mW/cm²**. That tight convergence is more informative than averaging unrelated seller curves. [[18]](pl300_source_docs/device_report_lightlab_family_2026-08-11.csv)

The purchased configuration adds an important constraint: it is claimed at **360 W**, not approximately 500 W. That draw is physically plausible for 300 dual-chip package positions, but it has not been wall-meter verified. Power-normalizing the same-method lab family shifts the likely grid-average region substantially below the unscaled 300-LED median. A PL300 center spot could still be higher because its lens layout may concentrate light more tightly than a 49-point average.

This supports two different numbers for two different jobs:

- **70 mW/cm² at six inches** is the rounded most-likely treatment-position point estimate. It sits above the 58–62 mW/cm² drive-normalized close-family cluster to allow for optics and center-versus-grid differences.
- **90 mW/cm² at six inches** is the conservative timer anchor. It sits at the upper edge of the raw close-family grid averages, so it should shorten rather than lengthen exposure if the family analogy is directionally correct. It is not a worst-case ceiling because the exact-unit screen is higher.

The one unique supplied PL300 screen at **161.241 mW/cm²** is not discarded. It remains the upper exact-unit observation because it used a spectrometer and was reportedly below the seller's headline specification. It receives limited weight because its meter range option, calibration, exact distance, point location, and repeatability are unknown. The seller catalog remains a claim rather than a measurement.

That finding changes the model interpretation:

- The old Lambertian curve falls substantially faster than every included large-array centerline curve at both 12 and 24 inches. It is useful as a steep-falloff sensitivity bound, not as the most evidence-aligned default.
- The idealized **60° red / 60° NIR** curve also falls somewhat faster than the observed comparison range.
- The unverified **60° red / 30° NIR** split remains inside the observed range, but the current SAIDI-family RLP300 catalog specifies a 30° lens while an anecdotal seller conversation described mixed 60° red / 30° NIR optics. The exact PL300 optics remain unresolved.
- Beam-angle labels alone do not predict a panel's distance curve. Array dimensions, emitter spacing, focal overlap, channel optics, drive level, and measurement location all matter.

Most importantly, normalized falloff cannot validate an absolute dose. The supplied PL300 originals contain **one unique readable 161.241 mW/cm² screen photographed twice**, not two independent readings. That value exceeds the standard published range of the identified meter family unless it is a customized high-range unit. A body-plane grid at the actual treatment position is still the deciding evidence.

## Audited PL300 gradient used by the planner

The graph shows the rounded most-likely estimate, while the timer defaults to the device.report-weighted conservative curve:

| Distance | Most-likely point estimate | Conservative timer anchor | Workable interval | Outer hotspot stress case |
|---:|---:|---:|---:|---:|
| 6 in | **70 mW/cm²** | **90 mW/cm²** | **60–90** | 161.241 |
| 12 in | **60 mW/cm²** | **77 mW/cm²** | **51–77** | 138 |
| 18 in | **50 mW/cm²** | **66 mW/cm²** | **44–66** | 118 |
| 24 in | **43 mW/cm²** | **57 mW/cm²** | **38–57** | 105 |

Both curves use an approximately 0.86 / 0.73 / 0.63 retained-output shape at 12 / 18 / 24 inches. That follows the closest mapped BIOMAX grid and the broader comparison median without accepting the seller's unusually slow 0.94 retention at 12 inches. The narrower band is an auditable working interval, **not a statistical confidence interval**. The 161.241 photo and its modeled falloff remain a separately displayed stress case because combining them into the routine band made every timer too imprecise to use. Every curve estimates a point or small-grid value, not the body's average irradiance.

## 1. How the comparison was built

The search prioritized sources that reported at least two explicit distances on the same panel and mode. Evidence is separated into four tiers:

| Tier | Source type | What it can establish |
|---|---|---|
| A | Accredited laboratory report using spectral irradiance equipment | Strongest available irradiance/method evidence for that tested unit |
| B | Independent reviewer measurement using a spectrometer | Useful direct comparison; less controlled and potentially commercially conflicted |
| C | Owner measurement with a named broadband meter and correction method | Anecdotal shape check; absolute values remain meter- and correction-dependent |
| D | Manufacturer manual or seller graphic without a disclosed meter/protocol | Company claim; useful for claimed curve shape only |

The comparison uses **center-point or source-designated readings**, because that is what most sources provide. Center output is not the same as the illuminated-area average. The broad row-level dataset is preserved in [`comparable_panel_falloff_2026-07-13.csv`](pl300_source_docs/comparable_panel_falloff_2026-07-13.csv); the internally consistent seven-report family and power normalization are preserved separately in [`device_report_lightlab_family_2026-08-11.csv`](pl300_source_docs/device_report_lightlab_family_2026-08-11.csv).

### 1.1 Complete same-method device.report family

| Report | Packages | Measured input | 6 / 12 / 18 / 24 in grid averages | PL300-drive-scaled 6 in | Similarity role |
|---|---:|---:|---:|---:|---|
| [BIOMAX 300 LLIA002684-001](https://device.report/m/c1072ea1abfbeaac9ffb660ea87223874e564664f10ca36b0eabe2da47d85f58.pdf) | 100 | 174.8 W | 71.79 / 56.25 / 43.89 / 35.30 | 49.28 | Same method; much smaller |
| [BIOMAX 450 LLIA002684-002](https://device.report/m/f1c6b008415d2f4a98696a7b7f09617d269281f18504314801cdaac7787e4505) | 150 | 248.8 W | 79.79 / 67.67 / 54.60 / 44.73 | 57.73 | Same method; half the packages |
| [BIOMAX 600 LLIA002684-003](https://device.report/m/869e5e0f9161fa349510ff891910f7c7fcd2645df62e19f0bb0ba69a22949f9d) | 200 | **345.6 W** | 84.30 / 66.00 / 53.77 / 45.18 | **58.54** | Closest measured input |
| [BIOMAX 900 LLIA002684-004](https://device.report/m/cc7ef1922e5a5aa59b8a4e9e263e427018912f7d4f8a0df3126a523059e30537.pdf) | **300** | 484.4 W | 83.13 / 71.29 / 60.63 / 52.35 | **61.78** | Exact package count and close form |
| [PRO GRANDE LLIA002684-005](https://device.report/m/d16b1ad3f6a10f1b0949127f111c0e76d0115c951818450ac1e4a2f1aa086f16) | 288 | 497.7 W | 84.15 / 69.52 / 58.68 / 50.54 | **58.43** | Near-exact package count |
| [PRO ULTRA LLIA002684-006](https://device.report/m/b2d88a912242cefab260e457e26f5051aaed70f509c66f134c41c6873906698b.pdf) | 432 | 772.6 W | 102.62 / 91.28 / 79.62 / 69.90 | 68.86 | Larger family boundary |
| [PRO MIDI LLIA002684-007](https://device.report/m/cd36bb1799fb6a1da84f940ca9786c153a8917f22b6e6e4a5e214e9597ca0168.pdf) | 216 | **380.8 W** | 90.27 / 81.82 / 69.60 / 57.88 | **61.44** | Second-closest measured input |

The scaling formula is `reported grid average × [(360 / 300) ÷ (measured watts / report packages)]`. It adjusts drive only. It does **not** claim linear equivalence across different emitting areas, package spacing, lenses, wavelength mixes, drivers, or grid footprints. Its value is the unusually tight 58–62 mW/cm² result among the four nearest family members—not any one decimal place.

### 1.2 Highest-confidence SAIDI-linked independent check

The KALA Elite is the strongest newly found cross-check because the brand relationship is high-confidence and the tested product is a tall panel. Light Therapy Insiders averaged nine spectrometer readings at six inches across the panel edges and center and reported **84 mW/cm²**. KALA's own product page claims **161 mW/cm² at six inches**, so the disclosed independent average is about **48% lower** than the seller headline. The reviewer uses affiliate links and did not publish a calibration certificate, so this is Tier B rather than Tier A. It validates the neighborhood of the raw LightLab comparator values and the conservative 90 mW/cm² timer anchor; it does not establish the PL300's distance falloff or body-area average. [[19]](pl300_source_docs/saidi_linked_brand_independent_test_audit_2026-08-11.csv)

The broader brand search found useful Hooga reviewer data—86 mW/cm² for PRO1500 and 81.7 for Ultra1500 six-inch nine-point averages—but could not tie those tested units to SAIDI independently, so they are context only. Current Mito accredited tests cannot be back-projected through a historical supplier relationship. VEVOR and Mitogen exposed seller values without independent methods; HigherDOSE and KALA mask tests have non-transferable geometry; no comparable independent panel test was located for HOLYLOOK, BGTHNG, SZOKLED, or Haigvel. The audit records these negative and excluded results so they cannot silently influence the estimate. [[19]](pl300_source_docs/saidi_linked_brand_independent_test_audit_2026-08-11.csv)

## 2. Measurements found online

| Source and geometry | Tier / method | 6 in | 12 in | 24 in | 36 in | Retained from 6 in |
|---|---|---:|---:|---:|---:|---|
| Bestqool Pro300; 36.4 × 13.5 in, 300 LEDs | A; LightLab spectral meter, center | 68.90 | 58.97 | — | — | 12 in: **85.6%** |
| KALA Elite; narrow tall 231-package panel | B; reviewer nine-position spectrometer average | **84.0** | — | — | — | High-confidence SAIDI-linked absolute check; no falloff shape |
| KOZE X; 36 × 12 in, 300 dual-chip LEDs | A; LightLab cosine-corrected spectral method, center | 87.57 | 71.36 | — | — | 12 in: **81.5%** |
| PlatinumLED BIOMAX 900; ~36 in, 300 LEDs, 484.4 W | A; LightLab visible+NIR meters, 49-point grid average | 83.13 | 71.29 | 52.35 | — | 12: **85.8%**; 24: **63.0%** |
| Helio Glow; 29.9 × 11.8 in, 216 LEDs | A; LightLab visible+NIR spectral meters, 231-point grid | 71.72 | 75.01 | 65.25 | 49.38 | 12: **104.6%**; 24: **91.0%**; 36: **68.9%** |
| Red Light Rising Advantage1500; 500 LEDs | B; reviewer spectrometer | 60 | 50 | 28 | — | 12: **83.3%**; 24: **46.7%** |
| older MitoPRO1500; 300 LEDs | B; reviewer spectrometer | 86 | — | 40 | — | 24: **46.5%** |
| RDPRO1500; 300 dual-chip LEDs | C; owner solar meter plus spectral correction | 84 | 80 | 75 at 20 in | 50 at 31 in | 12: **95.2%**; 20: **89.3%**; 31: **59.5%** |
| BioMax 900 four-panel array | B; reviewer spectrometer | 84 | 71 | 61 | — | 12: **84.5%**; 24: **72.6%** |
| Full Body Red Light Panel; 67.6 × 16.3 in, 840 LEDs | D; manufacturer manual, method absent | 154.6 | 141.0 | 108.0 | — | 12: **91.2%**; 24: **69.9%** |
| Hooga SaunaPRO; 39.9 × 10.9 in, 280 LEDs | D; manufacturer manual, method absent | 70 | 55 | — | — | 12: **78.6%** |
| RLT Home Total Spectrum series; five current panels | B; Electropossible HP350IR table | 98.7–121.62 | 84.1–102.23 | 59.0–74.91 | 42.7–66.35 | median 12: **85.2%**; 24: **61.6%** |
| RLT Home COMPACT; 30.3 × 11.8 in, 216 LEDs, 30° lens | B; Electropossible HP350IR | 99.0 | 86.0 | 63.2 | 47.2 | 12: **86.9%**; 24: **63.8%** |
| RLT Home Total Spectrum ULTRA | A; LightLab visible+NIR spectral meters | 85.70 | 67.99 | 60.51 | 45.55 | 12: **79.3%**; 24: **70.6%**; 36: **53.2%** |
| Supplied PL300 seller graphic; 36 × 12 in, 300 LEDs | D; seller graphic, method absent | 145 | 136 | 105 | — | 12: **93.8%**; 24: **72.4%** |
| Current SAIDI-family RLP300 catalog; 35.8 × 11.3 in, 300 dual-chip LEDs, 420 W | D; seller catalog, meter absent, 30° lens claim | 144.5 | 125.5 | — | — | 12: **86.9%**; catalog also reports 110.4 at 18 in |

All irradiance values are mW/cm². The Helio center reading increases slightly between 6 and 12 inches. That is not a transcription error: the lab's mapped results show the same behavior, consistent with a focused array whose beam overlap changes in the near field. It is a useful warning against forcing every large-panel curve to be monotonically decreasing at very close distances.

The older BioMax reviewer entry is a four-panel array, so it is included only as an extended-source geometry check. The newer BIOMAX 900 LightLab row is a single 300-LED panel and is a direct form-factor comparator. Its center values were 79.92 / 75.21 / 61.92 / 54.07 mW/cm² at 6 / 12 / 18 / 24 inches; the table uses the more relevant 49-point averages of 83.13 / 71.29 / 60.63 / 52.35. The manufacturer-manual and seller rows are retained because they add distance points, but they are not treated as independent validation.

## 3. Normalized comparison with the PL300 models

Normalizing each curve to `E(6 in) = 1.000` reduces—not eliminates—bias from different meter spectral responses and absolute calibration.

| Curve | 12 in / 6 in | 24 in / 6 in | 36 in / 6 in | Interpretation |
|---|---:|---:|---:|---|
| PL300 seller claim | **0.938** | **0.724** | — | Slow falloff, but inside the observed large-array range |
| Expanded comparison median | **0.852** (15 curves) | **0.634** (12 curves) | **0.488** (7 curves) | Descriptive benchmark, not a PL300 prediction |
| Most-likely and timer curves | **0.86** | **0.63** | — | Shared evidence-based shape; different 6-inch anchors |
| Idealized 60° red / 60° NIR | 0.761 | 0.412 | 0.241 | Faster falloff than the observed comparison range at 12 and 24 in |
| Idealized 60° red / 30° NIR | **0.870** | **0.581** | 0.393 | Closest model to the 12-in median; inside the 24-in range |
| Old Lambertian extended-panel model | 0.586 | 0.247 | 0.129 | Steeper than every included large-array center curve at 12 and 24 in |

The available 12-inch normalized values span **0.786–1.046**; the twelve 24-inch values span **0.465–0.910**. Seven curves provide 36-inch values, but they still mix panel sizes, methods, and optics; their 0.488 median is descriptive rather than a PL300 extrapolation. The separately displayed RLT Home COMPACT row is already part of the five-panel series and is not counted twice.

The reviewer comparison also undermines a simplistic reading of nominal beam angle: a claimed 60° MitoPRO1500 and a claimed 30° Advantage1500 both retained about 46–47% at 24 inches. The reviewer found that the larger angle label did not produce the expected wider field. Treat the PL300's recalled “60°” lens as one input to a scenario, not a measured optical transfer function.

## 4. What this means for a 10-minute session

Ten minutes delivers `dose (J/cm²) = irradiance (mW/cm²) × 0.6`.

At the default six-inch timer anchor, a nominal **10 J/cm²** session takes about **111 seconds per side**. Across the 60–90 mW/cm² workable interval, that same timer could deliver approximately **6.7–10.0 J/cm²**; reaching 10 J/cm² would take about **111–167 seconds**. The separate 161.241 hotspot stress case would deliver **17.9 J/cm²** in the timer's 111 seconds, or reach 10 J/cm² in about **62 seconds**. The visualizer displays the working interval and stress case separately. These are sensitivity calculations, not probability statements.

## 4.1 Electrical-to-optical sanity check

The 360 W purchase claim does not imply 360 W of emitted light. Three laboratory comparators report approximately 25.3%, 29.6%, and 36.4% electrical-to-reported-radiant conversion. Applied to 360 W, that produces an analog range of roughly **91–131 W optical**, with **105 W** as the rounded winner. A 360 W draw is also electrically plausible: divided over 300 package positions it is about 1.2 W per package, or about 0.6 W per die if two dies are active. This validates plausibility, not the exact wall draw or center irradiance.

If the photographed 6-inch PL300 value were accurate and its *shape* happened to equal the empirical medians, a purely illustrative calculation would give about **138 mW/cm² at 12 inches** and **113 mW/cm² at 24 inches**, or roughly **83 and 68 J/cm² in ten minutes**. This is not a new dose estimate: it combines one disputed absolute anchor with other products' normalized curves. It exists only to show why slow large-array falloff does not make ten minutes automatically conservative.

For a ten-minute session to deliver 8–10 J/cm² at the body, the measured body-position irradiance must be about **13.3–16.7 mW/cm²**. For 12–15 J/cm², it must be **20–25 mW/cm²**. Distance alone cannot guarantee either range.

Practical measurement protocol:

1. Warm the panel to a repeatable state and lock the same red/NIR mode and brightness.
2. Measure at the body plane—not at the panel face—at 12, 18, 24, 30, and 36 inches.
3. Record center plus four off-center points; report the center and the five-point average separately.
4. Keep the meter normal to the panel and record its model, serial/range option, calibration date, spectral range, and correction method.
5. Use the measured body-plane value in the dose calculator instead of selecting an optical model.

## 5. Source notes

1. [Bestqool Pro300 LightLab report LLIA002330-004](pl300_source_docs/comparable_panel_reports/bestqool-pro300-lightlab-LLIA002330-004.pdf) — accredited-lab report using a Gigahertz-Optik BTS2048-VL-TEC spectral irradiance meter; 3/6/12-inch center readings and 500 W wall consumption.
2. [Helio Glow LightLab distance-grid report LLIA002905-002](pl300_source_docs/comparable_panel_reports/helio-glow-lightlab-grid-all-channels.pdf) and [Helio's independent-testing page](https://heliocure.com/pages/independent-testing) — mapped 6/12/24/36-inch measurements; manufacturer-hosted report from an external laboratory.
3. [Light Therapy Insiders treatment-protocol measurements](https://www.lighttherapyinsiders.com/red-light-therapy-treatment-protocols/) — direct spectrometer measurements for the older Advantage1500 and MitoPRO1500; the site discloses affiliate revenue.
4. [Light Therapy Insiders treatment-area measurements](https://www.lighttherapyinsiders.com/red-light-therapy-treatment-area/) — direct measurements for a four-panel BioMax 900 arrangement; included only as a larger-array geometry comparison.
5. [RDPRO1500 owner measurement thread](https://www.reddit.com/r/redlighttherapy/comments/1sjbzgp/measuring_my_rdpro1500_irradiance/) — named Tenmars meter and GembaRed correction workflow; anecdotal and not equivalent to calibrated spectroradiometry.
6. [Full Body Red Light Panel manufacturer manual](pl300_source_docs/comparable_panel_reports/full-body-red-light-panel-manual-2025.pdf) — five claimed distance values; meter and protocol not disclosed.
7. [Hooga SaunaPRO manual](https://manuals.plus/hooga/saunapro-red-light-therapy-panel-manual.pdf) — two claimed distance values and a 60° specification; measurement method absent and documentation internally inconsistent.
8. [Supplied PL300 seller graphic and transcription](pl300_source_docs/seller_listing_screenshots_2026-07-13/) — the seller curve being checked, preserved as a claim.
9. [Row-level comparison dataset](pl300_source_docs/comparable_panel_falloff_2026-07-13.csv) — machine-readable values, evidence tiers, geometry, methods, source URLs, and limitations.
10. [RLT Home current third-party testing page](https://rlthome.com/pages/3rd-party-testing) — reports calibrated LightLab center values and HP350IR distance values for current large panels, and notes that position-dependent variation decreases with distance.
11. [OHSP350IR official specifications](https://www.hopoocolor.com/product/detail/OHSP350IR.html) — 0–60 mW/cm² standard test range, customized ranges supported, and stated ±8% irradiance accuracy.
12. [KOZE X Series test disclosure](https://kozehealth.com/products/koze-x-series) — closest dimensional match found: 36 × 12 inches, 300 dual-chip LEDs; LightLab result 87.57 mW/cm² at 6 inches and 71.36 at 12. The same page's solar-meter values are kept separate.
13. [PlatinumLED BIOMAX 900 LightLab grid report LLIA002684-004](https://device.report/m/cc7ef1922e5a5aa59b8a4e9e263e427018912f7d4f8a0df3126a523059e30537.pdf) — 300 LEDs, 484.4 W measured input, 49-point visible+NIR grids at 6 / 12 / 18 / 24 inches; provides center, average, minimum, and maximum values.
14. [Current SAIDI-family RLP300 catalog PDF](https://ae-pic-a1.aliexpress-media.com/kf/Sc185cd2550724e058d2ebfe424d88e6bv.pdf) — close family claim of 144.5 / 125.5 / 110.4 mW/cm² at 6 / 12 / 18 inches, 300 dual-chip packages, 420 W ±5%, and 30° lens. It is seller literature, not independent testing.
15. [User-reported purchase configuration](pl300_source_docs/user_reported_purchase_configuration_2026-08-11.txt) — configuration-specific 360 W and 630/660/810/830/850 = 2:2:2:1:1 claims, kept separate from family variants.
16. [Bestqool Pro300 LightLab radiant-output report LLIA002330-006](https://device.report/m/cec7b59ce0b2453238368c9064cf7c185f9733c89bc1c539c5f3b29c45987d05.pdf) — 148.319 W reported radiant output and 586 W measured input.
17. [PlatinumLED BIOMAX 900 LightLab integrating-sphere report](https://device.report/m/288eb2b79389520a564a11a4214703e2bf0402d7a42fdc0129390a99f78bd128) — 490.9 W input and a radiant-energy slope corresponding to approximately 179 W.
18. [Complete device.report LightLab family dataset](pl300_source_docs/device_report_lightlab_family_2026-08-11.csv) — seven same-method reports with raw averages, measured input, drive-normalized values, direct report links, and similarity notes.
19. [SAIDI-linked brand independent-test audit](pl300_source_docs/saidi_linked_brand_independent_test_audit_2026-08-11.csv) — records the KALA Elite nine-position spectrometer average and all inclusion/exclusion decisions for the requested brand list.
20. [KALA Elite independent panel comparison](https://www.lighttherapyinsiders.com/red-light-therapy-at-home-device/) — nine six-inch spectrometer readings averaged 84 mW/cm²; commercially affiliated reviewer.
21. [KALA Elite official specification](https://kalaredlight.com/en-us/products/kala-red-light-elite-panel) — seller claim of 161 mW/cm² at six inches, retained only as a comparison claim.
22. [Hooga PRO1500 review](https://www.lighttherapyinsiders.com/hooga-pro-1500-review/) and [Ultra1500 review](https://www.lighttherapyinsiders.com/hooga-ultra-1500-review/) — disclosed nine-position spectrometer averages; factory lineage remains unresolved.

## Evidence gaps

- No independent multi-distance PL300 measurement was found.
- No discovered PL300 document confirms the lens angle, red/NIR angle split, center-versus-average convention, meter, stabilization time, or calibration method behind the seller curve.
- The comparison is too heterogeneous for a formal prediction interval: panels differ in dimensions, wavelengths, chip arrangements, optics, drive power, and test methods.
- The seven available 36-inch curves remain too heterogeneous in panel size, optics, and method to choose a reliable PL300 extrapolation.
- The photographed meter's range option, serial number, calibration certificate, stabilization protocol, and exact probe-plane geometry remain unknown.
