# PL300 Panel: Measured Specs, Claimed Specs, and Dose Model

*Compiled 2026-07-12; meter-photo, power, and falloff audit updated 2026-08-11. Research orientation only, not medical advice. Confidence labels: **verified from supplied measurement photo**, **seller claim**, **inference**, and **model**.*

## 0. Bottom line

The strongest device-specific fact is **one unique readable center-point screen showing 161.241 mW/cm² at approximately 6 inches in red+NIR mode**. Photos 02 and 03 are duplicate or near-duplicate photographs of that same screen, not independent repeat measurements. An older transcription recorded 161.049 mW/cm² and a probable NIR-only image around 84.771 mW/cm², but those underlying screens are not independently readable in the preserved originals. They are retained as transcript-level context, not averaged into the audited anchor.

The five preserved originals strengthen provenance because the panel, ruler/distance setup, and HP350IR appear in the same frames. The readable screen also shows a 660.4 nm peak and 24.1 nm half-width. [[11]](pl300_source_docs/meter_photos/) **Meter-range caveat:** Hopoocolor's standard OHSP350IR specification lists a 0–60 mW/cm² irradiance range, ±8% irradiance accuracy, and customized ranges on request. The photographed 161.241 mW/cm² exceeds the standard range. The screen transcription is high-confidence; absolute accuracy is only provisional until the meter's high-range option, serial number, calibration, and probe-plane geometry are confirmed. [[6]](https://www.hopoocolor.com/product/detail/OHSP350IR.html)

Everything beyond the photographed position is less certain. Seller graphics claim **145 / 136 / 113 / 105 mW/cm² at 6 / 12 / 18 / 24 inches** and increasingly broad coverage, but omit the meter, mode, stabilization, center-versus-average convention, and measurement grid. Current SAIDI-family RLP300 literature separately reports **144.5 / 125.5 / 110.4 mW/cm² at 6 / 12 / 18 inches**, a **30° lens**, and **420 W ±5%**, while the current SAIDI DL300 page lists **480 VA** for a closely related 300-LED form factor. These are family/variant clues, not serial-number proof. [[13]](pl300_source_docs/seller_listing_screenshots_2026-07-13/)[[19]](https://ae-pic-a1.aliexpress-media.com/kf/Sc185cd2550724e058d2ebfe424d88e6bv.pdf)[[20]](https://www.saidipgl.com/en/dl-series/dl300.html)

**Audited winner estimates:** the purchase configuration's **360 W electrical-input claim** is physically plausible and is now the strongest configuration-specific value, although the unit has not been checked with a wall meter. Measured comparator conversion efficiencies map that input to approximately **105 W optical radiant power**, with a practical analog range of **90–130 W**. Seven same-method 2025 LightLab reports found on device.report constrain irradiance tightly, and the strongest independent SAIDI-linked check found—a nine-position spectrometer average on the KALA Elite—reported **84 mW/cm² at six inches** versus KALA's 161 claim. After normalizing measured input per emitter package to the claimed PL300 drive, the four closest LightLab family panels converge around 58–62 mW/cm² at six inches. Allowing for tighter PL300 optics and the owner screen without treating either as proven gives a rounded most-likely curve of **70 / 60 / 50 / 43 mW/cm²** and a conservative timer curve of **90 / 77 / 66 / 57 mW/cm² at 6 / 12 / 18 / 24 inches**. The workable interval is **60–90 / 51–77 / 44–66 / 38–57 mW/cm²**. The supplied **161.241 mW/cm²** screen remains visible as a separate hotspot stress scenario. This interval is workable uncertainty, not a statistical confidence interval. [[28]](pl300_source_docs/device_report_lightlab_family_2026-08-11.csv)[[35]](pl300_source_docs/saidi_linked_brand_independent_test_audit_2026-08-11.csv)

The purchased wavelength allocation, **630 / 660 / 810 / 830 / 850 nm = 2:2:2:1:1**, is treated as a nominal emitter allocation: **25% / 25% / 25% / 12.5% / 12.5%**, or **50% red and 50% near-infrared by allocation**. The visualizer uses equal radiant output per ratio part as a provisional dose partition; actual per-band energy can differ with drive current and diode efficiency. The ratio does not halve the total red+NIR joule dose. Because the listing does not say whether it counts packages, diode dies, or calibrated radiant watts, the visualizer does not apply speculative biological weighting to the five bands.

An expanded scan of multi-distance measurements from comparable large arrays supports a greater decline than the original planning curve. Normalized to each source's own 6-inch value, 15 comparison curves retain a median **85.2% at 12 inches** and 12 retain **63.4% at 24 inches**; the seller retains **93.8% and 72.4%**. The revised curves retain about 86%, 73%, and 63% at 12, 18, and 24 inches. Large-panel geometry still falls more slowly than point-source inverse square in the near field, but lens angle alone cannot validate the seller shape. The complete device.report BIOMAX/PRO family is especially useful because all seven reports used the same two spectral meters, 49-point grid, stabilized combined mode, and four distances. See the [comparable-panel falloff analysis](06_comparable_panel_irradiance_falloff.md) and preserved datasets. [[18]](06_comparable_panel_irradiance_falloff.md)[[28]](pl300_source_docs/device_report_lightlab_family_2026-08-11.csv)

The practical consequence is substantial: **10 minutes per side is not a low-dose session at full output under any of the extended-source/lens scenarios here**. At 36 inches it is approximately **12.5 J/cm² under the old Lambertian model, 23.3 J/cm² under a 60°/60° lens model, or 38.0 J/cm² under an unverified 60° red / 30° NIR split model**. The seller curve does not extend to 36 inches. Measure the treatment position or dim the panel before treating any of those numbers as real.

## 1. Why this page exists

The existing RLT folder focused on small handheld devices. This page adds the user's larger PL300 half-body panel as a distinct device-specific lane: what the photos establish, what the listings merely claim, what can be calculated, and what remains unknown. The accompanying [PL300 dose visualizer](pl300_dose_visualizer.html) turns those values into session-time estimates while keeping modeled and measured output separate.

## 2. Evidence map

| Claim or question | Best available evidence | Finding | Confidence / caveat |
|---|---|---|---|
| Combined output at ~6 in | One unique readable HP350IR-type meter screen, photographed twice | **161.241 mW/cm²** | **Measured-photo verified transcription**; center point, not area average; range/calibration caveat |
| Dominant combined peak | Same photos | 660.4 and 660.6 nm | **Measured-photo verified**; does not independently verify all five claimed wavelengths |
| NIR-only output | Older photo transcription | ~84.771 mW/cm², dominant peak ~850.4 nm | **Transcript-level probable measurement**; preserved originals do not independently support a precise value |
| Visible-red output | 161.241 minus the transcript-level probable NIR-only result | ~76.470 mW/cm² | **Weak inference**, not a direct red-only measurement; excluded from the audited default curve |
| Purchased wavelength allocation | User-reported purchase specification | 630 / 660 / 810 / 830 / 850 = **2:2:2:1:1**; nominally 50% red / 50% NIR | **Configuration-specific claim**; package-count, die-count, and radiant-power ratios are not interchangeable [[25]](pl300_source_docs/user_reported_purchase_configuration_2026-08-11.txt) |
| Output at 6/12/18/24 in | Newly supplied seller irradiance graphic | 145 / 136 / 113 / 105 mW/cm² | **Seller claim**; no meter, mode, protocol, or center/average definition [[13]](pl300_source_docs/seller_listing_screenshots_2026-07-13/) |
| Output at other distances | Audited synthesis led by seven same-method device.report LightLab grids, power-normalized close analogs, seller curve, and lens-array calculations | Most likely: 70 / 60 / 50 / 43; timer anchor: 90 / 77 / 66 / 57 mW/cm² at 6 / 12 / 18 / 24 in | **Model**; 60–90 mW/cm² six-inch working interval shown separately from the 161.241 hotspot stress case [[28]](pl300_source_docs/device_report_lightlab_family_2026-08-11.csv) |
| Electrical input power | Configuration-specific purchase claim checked against current SAIDI-family documentation | Winner **360 W claimed**; practical working range ~340–420 W pending measurement | **Plausible claim**, not a wall-meter result; 360 W averages 1.2 W per 300 package positions |
| Optical radiant power | Three laboratory analogs convert approximately 25.3%, 29.6%, and 36.4% of electrical input to reported radiant output | Winner estimate **~105 W**, practical 90–130 W analog range | **Analog-based inference**; not a direct PL300 optical-power measurement [[22]](pl300_source_docs/comparable_panel_reports/helio-glow-lightlab-grid-all-channels.pdf)[[26]](https://device.report/m/cec7b59ce0b2453238368c9064cf7c185f9733c89bc1c539c5f3b29c45987d05.pdf)[[27]](https://device.report/m/288eb2b79389520a564a11a4214703e2bf0402d7a42fdc0129390a99f78bd128) |
| Lens angle | Current RLP300 family catalog plus an anecdotal SAIDI configuration report | Current family sheet says 30°; anecdote says 60° red / 30° NIR | **Variant uncertainty**; neither establishes the exact PL300 optics |
| Panel construction | Listing screenshots and physical photos | PL300; 300 lenses/packages; claimed dual-chip; four visible fans; digital controls | Mixed: model/count claimed; fans/controls visually observed |
| Wavelength set | Listing screenshots | 630, 660, 810, 830, 850 nm | **Seller claim**; meter images verify dominant peaks near 660 and 850 nm only |
| Dosing benefit | PBM literature, not this product | Nonlinear responses are plausible; human optima remain indication- and protocol-specific | Does **not** clinically validate the PL300 or its presets |
| Which falloff shape best matches other large arrays? | Accredited lab reports, disclosed HP350IR tests, reviewer spectrometer tests, owner measurements, and manufacturer charts normalized to each panel's 6-in value | Seller shape: 0.938 at 12 in and 0.724 at 24 in; expanded medians: 0.852 and 0.634; revised curves: about 0.86 and 0.63 | **Shape comparison only**; different panels and meters cannot calibrate this PL300 [[18]](06_comparable_panel_irradiance_falloff.md) |

## 3. Complete known spec sheet

### 3.1 Seller-advertised and visually observed

| Specification | Known value | Status |
|---|---:|---|
| Model | PL300 | Consistent across supplied material |
| Intended coverage | Half-body / full-body therapy | Seller claim |
| LED lens/package count | 300 | Seller claim; physically plausible from photos |
| LED construction | Dual-chip | Seller claim; die allocation and simultaneous-drive behavior unverified |
| Claimed wavelengths | 630 / 660 / 810 / 830 / 850 nm | Seller claim |
| Purchased wavelength ratio | 2:2:2:1:1 in the wavelength order above | Configuration-specific claim; interpreted as nominal allocation, not measured radiant-power equality |
| Dimensions, listing A | 91.4 × 30 × 7 cm (36 × 11.81 × 2.76 in) | Seller claim |
| Dimensions, listing B | ~35.8 × 12 × 2.6 in | Seller claim; final digit partly obscured |
| Weight | 21.2 lb (~9.6 kg) | Seller claim |
| Input | 100–240 V AC | Seller claim |
| Power consumption | **360 W in the purchase information**; 420 W ±5% in current family literature; 520/540 W in other listing variants | 360 W is the best configuration-specific claim and is physically plausible; wall draw remains unmeasured |
| Advertised irradiance | 170 or max 175 mW/cm² | Seller claim; distance/method absent |
| Advertised distance curve | 145 / 136 / 113 / 105 mW/cm² at 6 / 12 / 18 / 24 in | Seller claim; method absent |
| Advertised coverage | 45 × 22 / 58 × 34 / 67 × 46 / 76 × 59 in at 6 / 12 / 18 / 24 in | Seller claim; intensity threshold defining “coverage” absent |
| Lens / beam angle | Possibly 60°; an anecdotal SAIDI report describes 60° red and 30° NIR | Unverified; not printed in the supplied PL300 material or current manufacturer pages checked |
| EMF | 0.0 µT at 4 in | Seller claim; not independently measured |
| Cooling | Four rear fans visible | Visually observed |
| Controls | Digital control display visible | Visually observed; timer/dimming/pulse behavior not fully established |
| Customization | Logo, shape, and wavelength customization | Seller claim |

### 3.2 Direct meter readings and derived quantities

| Reading | Preserved readable screen A | Older transcript B | Probable NIR-only transcript C |
|---|---:|---:|---:|
| Total irradiance | 161.241 mW/cm² | 161.049 mW/cm² | ~84.771 mW/cm² |
| FWHM / half-width | 24.1 nm | ~24.8 nm | ~43.0 nm |
| Dominant peak | 660.4 nm | 660.6 nm | ~850.4 nm |
| Displayed NIR band field | 86.2459 mW/cm² | 79.8194 mW/cm² | Obscured |
| Displayed "near red" field | 1.9653 mW/cm² | 1.9949 mW/cm² | Obscured |

Only column A is independently readable from the preserved originals. Columns B and C remain in the historical audit trail but do not establish repeatability. The displayed "near red" field is a meter-defined sub-band, not the panel's total red output. It cannot be reconciled with the combined total and the visible 660 nm peak as a full red-channel value.

At the one readable 161.241 mW/cm² point, output would accumulate at approximately **9.67 J/cm² per minute** if the reading is accurate: 30 seconds ≈ 4.84 J/cm²; 1 minute ≈ 9.67 J/cm²; 2 minutes ≈ 19.35 J/cm². At the revised most-likely **70 mW/cm²** estimate, the corresponding rate is **4.2 J/cm² per minute**; at the **90 mW/cm²** timer anchor it is **5.4 J/cm² per minute**. These are incident point fluences, not an area average or absorbed biological dose.

### 3.3 Wavelength allocation and photon interpretation

The stated ratio sums to eight parts. For a transparent working visualization, equal radiant output per part partitions total red+NIR dose as follows:

| Band | Nominal allocation share | Share of photons if radiant energy follows the ratio |
|---:|---:|---:|
| 630 nm | 25.0% | 21.4% |
| 660 nm | 25.0% | 22.4% |
| 810 nm | 25.0% | 27.6% |
| 830 nm | 12.5% | 14.1% |
| 850 nm | 12.5% | 14.5% |

The photon shares differ because, for equal radiant energy, photon count is proportional to wavelength. The planner remains energy-based in J/cm² because that is how the clinical protocols report dose; it does not assume that one 850-nm joule is biologically interchangeable with one 630-nm joule. If all 600 dies in 300 dual-chip packages follow the ratio, the nominal count would be 150 / 150 / 150 / 75 / 75 dies. That count is illustrative until the package pairing and drive currents are documented.

The readable meter screen's displayed NIR field is 86.2459 of 161.241 mW/cm², or approximately **53.5% NIR** if that field is interpreted as integrated NIR. That is compatible with a nominal 50:50 split within the meter and setup uncertainty, but the field definition is not sufficiently documented to replace the purchase specification.

## 4. Distance, lens, and dose model

The dose equation is:

`time (seconds) = target fluence (J/cm²) × 1000 / irradiance (mW/cm²)`

The earlier 15-inch estimate of 26 mW/cm² used inverse-square scaling from the 6-inch reading. That remains a poor near-field default for a 36 × 12-inch extended source. The newly supplied seller curve also shows much slower falloff. It does not, however, validate one exact optical model.

### 4.1 Seller curve: raw and anchored

The seller graphic reports four combined-output points. Because its 6-inch value is 145 mW/cm² while the one readable owner screen shows 161.241 mW/cm², the visualizer retains this **shape-only sensitivity model**:

`scaled seller E(d) = seller E(d) × 161.241 / 145`

It uses log-linear interpolation only between 6 and 24 inches. It does not extrapolate outside the source graphic's range.

| Distance | Seller raw claim | Seller shape scaled to measured 6 in | 10-minute dose from scaled curve |
|---:|---:|---:|---:|
| 6 in | 145 mW/cm² | 161.1 mW/cm² | 96.7 J/cm² |
| 12 in | 136 mW/cm² | 151.1 mW/cm² | 90.7 J/cm² |
| 18 in | 113 mW/cm² | 125.6 mW/cm² | 75.3 J/cm² |
| 24 in | 105 mW/cm² | 116.7 mW/cm² | 70.0 J/cm² |

Scaling preserves the seller's claimed falloff shape; it does not turn the other distances into measurements. A different center-versus-area definition could explain some of the 6-inch disagreement.

### 4.2 Most-likely curve, device.report-weighted timer curve, and workable interval

The closest-comparator audit produces two deliberately rounded curves:

| Distance | Most-likely point estimate | Conservative timer anchor | Workable interval | Outer hotspot stress case | Basis |
|---:|---:|---:|---:|---:|---|
| 6 in | **70 mW/cm²** | **90 mW/cm²** | **60–90** | 161.241 | Four closest same-method family reports normalize to 58.4–61.8; 70 allows for tighter optics, while 90 stays at the upper edge of credible lab-grid evidence |
| 12 in | **60 mW/cm²** | **77 mW/cm²** | **51–77** | 138 | About 86% retention, matching the BIOMAX 900 grid and broader comparison median |
| 18 in | **50 mW/cm²** | **66 mW/cm²** | **44–66** | 118 | Rounded mapped-grid retention after preserving near-field array behavior |
| 24 in | **43 mW/cm²** | **57 mW/cm²** | **38–57** | 105 | About 63% retention, matching the BIOMAX 900 49-point grid |

The **70 mW/cm²** curve is the best estimate. The **90 mW/cm²** timer curve is deliberately cautious for session timing because underestimating irradiance would lengthen exposure. At six inches, a nominal 10 J/cm² timer setting takes about 111 seconds. Across the 60–90 working interval that timer delivers roughly **6.7–10.0 J/cm²**; the separate 161.241 stress case would deliver **17.9 J/cm²**. This split is more workable than one 60–161 envelope while preserving the exact-unit warning.

#### Why the device.report family changed the answer

LightLab tested seven BIOMAX/PRO panels under a common protocol: BTS2048-VL-TEC and BTS2048-NIR spectral meters, combined visible+NIR reporting, stabilized operation, a 49-point target grid, and 6/12/18/24-inch positions. That removes much of the method noise that made the earlier cross-brand comparison hard to weight. The complete transcription and formulas are preserved in the [same-method family dataset](pl300_source_docs/device_report_lightlab_family_2026-08-11.csv). [[24]](https://device.report/m/cc7ef1922e5a5aa59b8a4e9e263e427018912f7d4f8a0df3126a523059e30537.pdf)[[29]](https://device.report/m/c1072ea1abfbeaac9ffb660ea87223874e564664f10ca36b0eabe2da47d85f58.pdf)[[30]](https://device.report/m/f1c6b008415d2f4a98696a7b7f09617d269281f18504314801cdaac7787e4505)[[31]](https://device.report/m/869e5e0f9161fa349510ff891910f7c7fcd2645df62e19f0bb0ba69a22949f9d)[[32]](https://device.report/m/d16b1ad3f6a10f1b0949127f111c0e76d0115c951818450ac1e4a2f1aa086f16)[[33]](https://device.report/m/b2d88a912242cefab260e457e26f5051aaed70f509c66f134c41c6873906698b.pdf)[[34]](https://device.report/m/cd36bb1799fb6a1da84f940ca9786c153a8917f22b6e6e4a5e214e9597ca0168.pdf)

The normalization is intentionally simple and auditable: `scaled grid average = reported grid average × [(360 W / 300 packages) ÷ (measured report watts / report packages)]`. BIOMAX 600, BIOMAX 900, PRO GRANDE, and PRO MIDI are closest by input or package count; their scaled six-inch averages are **58.54, 61.78, 58.43, and 61.44 mW/cm²**. This is not a claim that watts and irradiance scale perfectly. Panel area, spacing, lenses, driver efficiency, wavelength mix, and grid footprint still differ. For that reason 60 is used as the lower working edge, 70 as the rounded winner, and 90—not the old 100—as the conservative timer edge.

These remain point/small-grid models, not a whole-body dose map. The working interval is an auditable planning interval, not a statistical confidence interval; the photo stress point is excluded because its range option, location, and repeatability remain unresolved. A calibrated Helio Glow mapping illustrates why the distinction matters: at 6 inches it reported **71.72 mW/cm² center, 26.31 mW/cm² area average, 86.14 mW/cm² maximum, and 135.77 W radiant power across the target plane**. That center-to-average ratio is device- and grid-specific, so it should not be copied onto the PL300, but it makes any unqualified whole-body dose based on a center hotspot indefensible.

#### What the SAIDI-linked brand check added

KALA Elite is the only newly located device that combines a high-confidence SAIDI relationship, panel geometry, and an independent disclosed measurement method. Light Therapy Insiders took nine spectrometer readings across the edges and center and reported an **84 mW/cm² average at six inches**. KALA's own page claims **161 mW/cm² at six inches**, making the independent average about 48% lower than the headline claim. The reviewer uses affiliate links, so this remains Tier B rather than an accredited-laboratory result. It supports the existing raw-comparator cluster and the 90 mW/cm² timer anchor; it does not justify raising the 70 mW/cm² most-likely PL300 point. [[35]](pl300_source_docs/saidi_linked_brand_independent_test_audit_2026-08-11.csv)

Independent reviewer measurements were also found for Hooga PRO1500, Ultra1500, Ultra360, and HG300. The two large models averaged **86 and 81.7 mW/cm² at six inches**, but the tested units cannot be independently tied to SAIDI, so they remain category context rather than PL300 calibration. Current Mito Red Light products have strong accredited LightLab data, but a historical/product-specific SAIDI relationship cannot be transferred to current panels. Mitogen and VEVOR yielded only seller values, HigherDOSE and KALA mask tests use non-transferable geometry, and no comparable independent panel radiometry was located for HOLYLOOK, BGTHNG, SZOKLED, or Haigvel. The complete inclusion/exclusion audit is preserved in the linked CSV. [[35]](pl300_source_docs/saidi_linked_brand_independent_test_audit_2026-08-11.csv)

The power check does not assume that 360 electrical watts become 360 optical watts. Three mixed red/NIR laboratory comparators span approximately **25.3% radiant conversion** (Bestqool: 148.319 W radiant / 586 W input), **29.6%** (Helio: 135.77 W / 458.4 W), and **36.4%** (BIOMAX: approximately 179 W / 490.9 W from the integrating-sphere energy slope). Applied to 360 W, those ratios imply roughly **91 / 107 / 131 W radiant**. The rounded winner is therefore **105 W optical**, with **90–130 W** as a practical analog range. The nominal 50:50 red/NIR allocation does not change total watts; differences in wavelength-specific efficiency, drive current, and fan/driver consumption are absorbed into that range. This checks energy conservation but cannot uniquely predict center-point irradiance: lens overlap, emitting area, grid footprint, and the distinction between maximum and average all intervene.

### 4.3 Rectangular lens-array scenario

For a rectangular 36 × 12-inch emitting area, model each point's angular intensity as `I(θ) ∝ cos^m(θ)`. If the quoted beam angle `β` is full-width at half maximum (FWHM), then:

`m = ln(0.5) / ln(cos(β / 2))`

For `β = 60°`, `m ≈ 4.819`. For `β = 30°`, `m ≈ 19.994`. The center-axis geometric factor is numerically integrated across the panel face:

`J(d,m) = ∬A d^(m+1) / (d² + x² + y²)^((m+3)/2) dx dy`

Each channel is normalized to its own 6-inch anchor:

`Echannel(d) = Echannel(6) × J(d,mchannel) / J(6,mchannel)`

The legacy combined 60°/60° sensitivity scenario uses 161.241 mW/cm² at 6 inches. The alternate 60° red / 30° NIR scenario uses weakly inferred red and transcript-level NIR anchors. Neither is the new default. The alternate exists because one anecdotal SAIDI configuration report describes that split; it is not verified for this unit. [[17]](https://www.reddit.com/r/redlighttherapy/comments/1mgeqa0/halffull_body_panel_idea_light_vs_sgrow_vs_saidi/)

| Distance | Seller-scaled, 6–24 in only | 60° red + 60° NIR | 60° red + 30° NIR | Old Lambertian | 10-min dose range across available extended-source models |
|---:|---:|---:|---:|---:|---:|
| 6 in | 161.1 | 161.1 | 161.1 | 161.1 | 96.7 J/cm² |
| 12 in | 151.1 | 122.7 | 140.2 | 94.4 | 56.6–90.7 J/cm² |
| 18 in | 125.6 | 89.6 | 115.2 | 59.3 | 35.6–75.3 J/cm² |
| 24 in | 116.7 | 66.4 | 93.7 | 39.8 | 23.9–70.0 J/cm² |
| 30 in | — | 50.2 | 76.7 | 28.1 | 16.9–46.0 J/cm² |
| 36 in | — | 38.8 | 63.4 | 20.8 | 12.5–38.0 J/cm² |

All irradiances are mW/cm². These are center-axis calculations, not area averages. They ignore discrete LED spacing, side lobes, spectral meter response, body curvature, clothing, skin angle, and panel-to-panel manufacturing variation.

The external measurement scan supplies an empirical model check, not another selectable dose curve. At 12 inches, seven large-array curves retained 0.786–1.046 of their 6-inch center value; at 24 inches, five curves retained 0.465–0.910. Their medians were 0.856 and 0.699. The PL300 seller curve sits inside both ranges; the 60°/30° scenario also sits inside both; the 60°/60° and old Lambertian scenarios fall below the observed comparison ranges. Because the inputs mix accredited laboratories, reviewer tests, owner measurements, and manufacturer claims, the visualizer displays the empirical curves for shape comparison but does not use them to calculate PL300 dose. [[18]](06_comparable_panel_irradiance_falloff.md)

### 4.4 Coverage geometry

A simple full-angle footprint for a `W × H` panel is:

`footprint width = W + 2d tan(β/2)` and `footprint height = H + 2d tan(β/2)`

With a 12 × 36-inch panel and 60° beam, that predicts about **18.9 × 42.9 inches at 6 inches** and **39.7 × 63.7 inches at 24 inches**. The seller claims 22 × 45 and 59 × 76 inches, respectively. This does not necessarily contradict a 60° FWHM lens: “coverage” may be drawn to a much lower intensity threshold than half maximum, and overlapping edge emitters widen the visible field.

### 4.5 What this changes for a 10-minute, three-times-weekly plan

Ten minutes delivers `dose = irradiance × 0.6`. To keep a 10-minute session near the archive's cautious **8–10 J/cm² per side** planning lane, the measured treatment-position irradiance would need to be only **13.3–16.7 mW/cm²**. For **12–15 J/cm²**, it would need to be **20–25 mW/cm²**. At 36 inches, even the old Lambertian model is ~20.8 mW/cm²; the lens scenarios are ~38.8–63.4 mW/cm².

Therefore, “10 minutes each side, three times weekly” should be treated as a fixed-time ritual that requires **meter-guided distance or dimming**, not as an automatically conservative dose. The seller curve has no 30- or 36-inch observation, so it cannot resolve the uncertainty.

## 4.6 What GembaRed says

GembaRed is a vendor/technical commentator, not a clinical guideline body. Its recurring position is that industry irradiance claims are often inflated by broadband solar meters, that the popular ">100 mW/cm² at 6 inches" benchmark is marketing rather than a clinically established threshold, and that high irradiance can add superficial heat without reliably improving penetration. Its current YouTube search results frame **5–20 mW/cm²** as a commonly recommended clinical range, question whether panels are too powerful, and emphasize exposure time and total joules rather than intensity alone. [[9]](https://gembared.com/blogs/musings/budget-intensity-measurements-pt2-tes-1333-solar-power-meter)[[10]](https://www.youtube.com/watch?v=BYbdGoA5SLQ)

That viewpoint is directionally consistent with the device-measurement problem here, but it should not be treated as settled consensus. GembaRed's claim that essentially no panels deliver 100 mW/cm² conflicts with some calibrated spectroradiometer readings and accredited lab results on high-output devices. The useful takeaway is narrower: identify the meter, verify its range/calibration, distinguish center from area-average irradiance, avoid heat, and do not use a marketing threshold as a treatment target.

## 5. Practical use of the visualizer

1. Prefer **Custom measured irradiance** whenever a reading exists at the real body position and panel mode. For broad exposures, use a body-plane grid average rather than a center hotspot.
2. Measure center plus four corners at 12, 18, 24, 30, and 36 inches to characterize uniformity and distance falloff. A 10-minute 8–10 J/cm² session requires 13.3–16.7 mW/cm² at the body.
3. Keep mode, distance, angle, panel warm-up, meter orientation, and body position fixed.
4. Treat the preset bands as research-oriented starting ranges, not outcome predictions or toxicity thresholds.
5. Reduce or stop if warmth, redness, dryness, headache, eye symptoms, unusual fatigue, or pigment change persists. Use appropriate opaque eye protection and seek clinician input for photosensitizing medicines, eye disease, suspicious lesions, pregnancy, photosensitive epilepsy, or medically unstable areas.

## Evidence gaps

- Actual wall-power draw; 360 W is the strongest configuration-specific claim, while current close-family literature spans 420–480 VA and older variants claim 520–540 W.
- Direct integrating-sphere or mapped target-plane optical radiant power; ~105 W and 90–130 W are analog-based only.
- Independent EMF measurement and its meter/method.
- Area-average irradiance and edge-to-center uniformity.
- Measured output at any distance other than approximately 6 inches.
- Direct red-only measurement and independent output for each claimed wavelength; the 2:2:2:1:1 statement does not establish radiant watts per band.
- Exact package/die pairing, wavelength-specific drive currents, lens angle, pulsing frequency/duty cycle, dimming method, flicker, timer range, and whether both chips can run simultaneously at full drive. The 60° and 60°/30° layouts remain scenarios.
- Manual/IFU, serial/variant identity, manufacturer confirmation, product-specific certifications, electrical safety report, warranty, and service parts. SAIDI is probable, not serial-number verified.
- Product-specific clinical testing; none was supplied or found.

## Sources

1. [User-supplied PL300 photo/spec audit](pl300_source_docs/user_supplied_pl300_photo_spec_audit_2026-07-12.txt) — transcription and interpretation of supplied listing, product, ruler, and meter photographs; primary evidence for device-specific values above.
2. [Ideatherapy RL-series touch-screen manual](https://www.ideatherapy.com/wp-content/uploads/2025/04/RL-Series-Touch-Screen-Manual.pdf) — current comparator for the common 300-LED, ~36.2 × 11.8 × 2.5-inch, five-wavelength panel form factor; not proof that this PL300 is the same model.
3. [PubMed protocol: two vs three weekly 660-nm PBM sessions](https://pubmed.ncbi.nlm.nih.gov/36749255/) — 660 nm, 6.4 mW/cm², ~8.02 J/cm², 21 minutes; supports the protocol anchor, not PL300 equivalence.
4. [PubMed: periocular wrinkle-volume trial](https://pubmed.ncbi.nlm.nih.gov/36780572/) — supports the 3.8 J/cm² human facial-study anchor used in the visualizer.
5. [Foundational biphasic-dose review](https://pmc.ncbi.nlm.nih.gov/articles/PMC2790317/) — supports the inverted-U concept while not establishing a universal human optimum.
6. [Hopoocolor OHSP350IR official specifications](https://www.hopoocolor.com/product/detail/OHSP350IR.html) — 380–1050 nm, ±0.5 nm wavelength accuracy, stated ±8% irradiance accuracy, standard 0–60 mW/cm² range with custom ranges available.
7. [Bestqool Pro300 / LightLab report LLIA002330-004](https://manuals.plus/m/1f6c5530043c6b5ec7e207cd20c205ad0841ef0ecee2e9d40f26befd08b15c4a) — accredited-lab comparator: 300 dual-chip LEDs, 500 W wall power, 68.9 mW/cm² at 6 in and 58.97 mW/cm² at 12 in using a spectral irradiance meter.
8. [Community RDPRO1500 measurement](https://www.reddit.com/r/redlighttherapy/comments/1sjbzgp/measuring_my_rdpro1500_irradiance/) — anecdotal comparator reporting ~80 mW/cm² at 12 in after a Tenmars reading was processed using GembaRed's correction method.
9. [GembaRed: solar-meter correction and intensity claims](https://gembared.com/blogs/musings/budget-intensity-measurements-pt2-tes-1333-solar-power-meter) — argues common solar meters read red/NIR panels roughly 2× high and rejects 100 mW/cm² as a universal target.
10. [GembaRed YouTube: “Clinical Grade Intensity Does Not Sell”](https://www.youtube.com/watch?v=BYbdGoA5SLQ) and [“15 Minutes for Optimal Red Light Therapy Dosing”](https://www.youtube.com/watch?v=t4dy2ooKW_M) — GembaRed's current video framing on lower clinical irradiance, treatment time, and dose.
11. [Original PL300 meter photographs](pl300_source_docs/meter_photos/) — five supplied originals showing the panel, ruler setup, and HP350IR; photos 02/03 clearly show 161.241 mW/cm², 24.1 nm half-width, and 660.4 nm peak. Other screens are too obscured for independent numeric transcription.
12. [Whole-body PBM dosing evidence](05_whole_body_pbm_dosing_evidence.md) — protocol-by-protocol human evidence and PL300 12-inch translation.
13. [Original seller-listing screenshots and transcription](pl300_source_docs/seller_listing_screenshots_2026-07-13/) — PL300 product parameters plus the seller's irradiance/coverage-by-distance graphic; preserved as claims, not independent measurements.
14. [SAIDI official company site](https://www.saidipgl.com/) — supports the probable manufacturer's identity, OEM/ODM role, and company history; company-level certification statements are not treated as PL300-specific evidence.
15. [SAIDI official PL-series page](https://www.saidipgl.com/products/pl-series.html) — current family page; only PL75, PL100, and PL200 were visible when checked, which limits exact-variant attribution.
16. [Current Shenzhen SAIDI PL300 marketplace listing](https://indonesian.alibaba.com/product-detail/Saidi-Full-Body-Use-High-Irradiation-1601631569253.html) — close match on model, dimensions, LED count, five-wavelength dual-chip architecture, and 170 mW/cm² claim; its 420 W figure illustrates listing/variant drift.
17. [Community SAIDI panel configuration discussion](https://www.reddit.com/r/redlighttherapy/comments/1mgeqa0/halffull_body_panel_idea_light_vs_sgrow_vs_saidi/) — anecdotal report of 60° red / 30° NIR lenses; included only to define an alternate scenario, not as proof of this PL300's optics.
18. [Comparable-panel irradiance falloff analysis](06_comparable_panel_irradiance_falloff.md) — accredited laboratory, independent reviewer, owner, manufacturer-manual, and seller curves normalized to their own 6-inch values; includes the preserved CSV and source reports.
19. [Current SAIDI-family catalog PDF](https://ae-pic-a1.aliexpress-media.com/kf/Sc185cd2550724e058d2ebfe424d88e6bv.pdf) — reports 300 × 5 W packages, 420 W ±5%, and 144.5 mW/cm² at 6 inches for a current close family/variant; not proof of this unit's serial configuration.
20. [SAIDI DL300 official page](https://www.saidipgl.com/en/dl-series/dl300.html) — current 300-LED, five-wavelength, 21.2-lb family comparator listing 480 VA; illustrates family/variant power drift, not exact PL300 identity.
21. [RLT Home current third-party testing page](https://rlthome.com/pages/3rd-party-testing) — publishes calibrated LightLab and HP350IR distance measurements for large panels and explicitly notes position-dependent near-field readings.
22. [Helio Glow LightLab mapped-grid report](pl300_source_docs/comparable_panel_reports/helio-glow-lightlab-grid-all-channels.pdf) — 231-point target-plane mapping used to separate center, maximum, area average, and radiant power.
23. [KOZE X Series LightLab disclosure](https://kozehealth.com/products/koze-x-series) — closest dimensional comparator found: 36 × 12 inches, 300 dual-chip LEDs; 87.57 mW/cm² at 6 inches and 71.36 at 12 using a cosine-corrected LightLab method.
24. [PlatinumLED BIOMAX 900 LightLab grid report LLIA002684-004](https://device.report/m/cc7ef1922e5a5aa59b8a4e9e263e427018912f7d4f8a0df3126a523059e30537.pdf) — 300 LEDs, 484.4 W measured input, and 49-point visible+NIR grids at 6 / 12 / 18 / 24 inches.
25. [User-reported purchase configuration](pl300_source_docs/user_reported_purchase_configuration_2026-08-11.txt) — records the purchased 630/660/810/830/850 nm, 2:2:2:1:1, 360 W configuration separately from family and marketplace variants.
26. [Bestqool Pro300 LightLab radiant-output report LLIA002330-006](https://device.report/m/cec7b59ce0b2453238368c9064cf7c185f9733c89bc1c539c5f3b29c45987d05.pdf) — integrating-sphere-style report of 148.319 W radiant output with 586 W measured input for a close 300-LED comparator.
27. [PlatinumLED BIOMAX 900 LightLab integrating-sphere report](https://device.report/m/288eb2b79389520a564a11a4214703e2bf0402d7a42fdc0129390a99f78bd128) — reported 490.9 W input and a radiant-energy rise corresponding to approximately 179 W over the measured interval; used only as an efficiency analog.
28. [Same-method device.report LightLab family dataset](pl300_source_docs/device_report_lightlab_family_2026-08-11.csv) — seven reports, raw 49-point values, measured input, per-package normalization, direct report links, and similarity notes.
29. [BIOMAX 300 LightLab report LLIA002684-001](https://device.report/m/c1072ea1abfbeaac9ffb660ea87223874e564664f10ca36b0eabe2da47d85f58.pdf) — 100 packages, 174.8 W, and four 49-point distance grids.
30. [BIOMAX 450 LightLab report LLIA002684-002](https://device.report/m/f1c6b008415d2f4a98696a7b7f09617d269281f18504314801cdaac7787e4505) — 150 packages, 248.8 W, and four 49-point distance grids.
31. [BIOMAX 600 LightLab report LLIA002684-003](https://device.report/m/869e5e0f9161fa349510ff891910f7c7fcd2645df62e19f0bb0ba69a22949f9d) — 200 packages, 345.6 W, and four 49-point distance grids; closest measured input to the PL300 claim.
32. [BIOMAX PRO GRANDE LightLab report LLIA002684-005](https://device.report/m/d16b1ad3f6a10f1b0949127f111c0e76d0115c951818450ac1e4a2f1aa086f16) — 288 packages, 497.7 W, and four 49-point distance grids.
33. [BIOMAX PRO ULTRA LightLab report LLIA002684-006](https://device.report/m/b2d88a912242cefab260e457e26f5051aaed70f509c66f134c41c6873906698b.pdf) — 432 packages, 772.6 W, and four 49-point distance grids; useful method-family boundary but less similar in size and power.
34. [BIOMAX PRO MIDI LightLab report LLIA002684-007](https://device.report/m/cd36bb1799fb6a1da84f940ca9786c153a8917f22b6e6e4a5e214e9597ca0168.pdf) — 216 packages, 380.8 W, and four 49-point distance grids; closest measured input after BIOMAX 600.
35. [SAIDI-linked brand independent-test audit](pl300_source_docs/saidi_linked_brand_independent_test_audit_2026-08-11.csv) — model-level audit of KALA, VEVOR, HigherDOSE, Hooga, Mitogen, Mito, HOLYLOOK, BGTHNG, SZOKLED, and Haigvel, including direct test links, method, reported values, lineage confidence, and PL300 inclusion decisions.
36. [KALA Elite independent panel comparison](https://www.lighttherapyinsiders.com/red-light-therapy-at-home-device/) — nine spectrometer readings at six inches averaged 84 mW/cm²; reviewer discloses affiliate support.
37. [KALA Elite official specification](https://kalaredlight.com/en-us/products/kala-red-light-elite-panel) — 161 mW/cm² six-inch claim used only for claim-versus-independent comparison.
38. [Hooga PRO1500 independent review](https://www.lighttherapyinsiders.com/hooga-pro-1500-review/) and [Ultra1500 review](https://www.lighttherapyinsiders.com/hooga-ultra-1500-review/) — nine-position six-inch averages of 86 and 81.7 mW/cm²; category context only because tested-unit SAIDI lineage is unresolved.
39. [Mito Red Light independent-test library](https://mitoredlight.com/pages/independent-test-data) — current ISO/IEC 17025 LightLab reports; not treated as SAIDI evidence because current product sourcing cannot be inferred from a historical relationship.
