# PL300 Panel: Measured Specs, Claimed Specs, and Dose Model

*Compiled 2026-07-12; falloff model updated 2026-07-13. Research orientation only, not medical advice. Confidence labels: **verified from supplied measurement photo**, **seller claim**, **inference**, and **model**.*

## 0. Bottom line

The strongest device-specific fact is a repeatable center-point measurement of **161.145 mW/cm² average at approximately 6 inches in red+NIR mode** (161.241 and 161.049 mW/cm²; 0.12% spread). A probable NIR-only photo reads **84.771 mW/cm²**, making the visible-red contribution approximately **76.374 mW/cm² by subtraction**. The panel is therefore unusually high-output at that close distance.

The five newly preserved originals materially strengthen provenance: the panel, ruler/distance setup, and HP350IR appear in the same frames, and two photos clearly show the same 161.241 mW/cm² result with 660.4 nm peak and 24.1 nm half-width. [[11]](pl300_source_docs/meter_photos/) **Meter-range caveat:** Hopoocolor's standard OHSP350IR specification lists a 0–60 mW/cm² irradiance range and says customized ranges are available. The photographed 161 mW/cm² result exceeds that standard range. Confidence is high that the screen says 161.241 and that the measurement is repeatable; absolute accuracy still requires confirmation that this meter is the calibrated high-range version. [[6]](https://www.hopoocolor.com/product/detail/OHSP350IR.html)

Everything beyond the measured position is less certain. Newly supplied seller graphics claim **145 / 136 / 113 / 105 mW/cm² at 6 / 12 / 18 / 24 inches** and increasingly broad coverage. Those figures are useful as a company-family curve, but the graphic omits the meter, mode, protocol, and area-averaging method. It also disagrees with the owner's stronger 6-inch reading. The visualizer now keeps four different things separate: the raw seller curve, that curve scaled to the owner's 6-inch anchor, a recalled **60° lens scenario**, and the older Lambertian model. [[13]](pl300_source_docs/seller_listing_screenshots_2026-07-13/)

The practical consequence is substantial: **10 minutes per side is not a low-dose session at full output under any of the extended-source/lens scenarios here**. At 36 inches it is approximately **12.5 J/cm² under the old Lambertian model, 23.3 J/cm² under a 60°/60° lens model, or 38.0 J/cm² under an unverified 60° red / 30° NIR split model**. The seller curve does not extend to 36 inches. Measure the treatment position or dim the panel before treating any of those numbers as real.

## 1. Why this page exists

The existing RLT folder focused on small handheld devices. This page adds the user's larger PL300 half-body panel as a distinct device-specific lane: what the photos establish, what the listings merely claim, what can be calculated, and what remains unknown. The accompanying [PL300 dose visualizer](pl300_dose_visualizer.html) turns those values into session-time estimates while keeping modeled and measured output separate.

## 2. Evidence map

| Claim or question | Best available evidence | Finding | Confidence / caveat |
|---|---|---|---|
| Combined output at ~6 in | Two supplied OHSP350IR-type meter photos | 161.241 and 161.049 mW/cm²; mean **161.145 mW/cm²** | **Measured-photo verified**; center point, not area average |
| Dominant combined peak | Same photos | 660.4 and 660.6 nm | **Measured-photo verified**; does not independently verify all five claimed wavelengths |
| NIR-only output | Darker supplied meter photo | ~84.771 mW/cm², dominant peak ~850.4 nm | **Probable measurement**; photo is less legible and mode state is inferred |
| Visible-red output | Combined mean minus probable NIR-only result | ~76.374 mW/cm²; ~47.4% of combined output | **Inference**, not a direct red-only measurement |
| Output at 6/12/18/24 in | Newly supplied seller irradiance graphic | 145 / 136 / 113 / 105 mW/cm² | **Seller claim**; no meter, mode, protocol, or center/average definition [[13]](pl300_source_docs/seller_listing_screenshots_2026-07-13/) |
| Output at other distances | Seller-curve interpolation, lens-array, Lambertian, and inverse-square calculations | Visualizer shows each separately | **Models**; only the owner's ~6 in point is measured |
| Lens angle | User recollection plus an anecdotal SAIDI configuration report | 60°/60° primary scenario; 60° red / 30° NIR alternate | **Unverified scenario**, not a discovered PL300 document; supplied images do not state beam angle |
| Panel construction | Listing screenshots and physical photos | PL300; 300 lenses/packages; claimed dual-chip; four visible fans; digital controls | Mixed: model/count claimed; fans/controls visually observed |
| Wavelength set | Listing screenshots | 630, 660, 810, 830, 850 nm | **Seller claim**; meter images verify dominant peaks near 660 and 850 nm only |
| Dosing benefit | PBM literature, not this product | Nonlinear responses are plausible; human optima remain indication- and protocol-specific | Does **not** clinically validate the PL300 or its presets |
| Is the old 94.4 mW/cm² 12-in model implausibly low? | Old Lambertian model plus external comparators | Not inherently, but it is now the bottom of a 94.4–151.1 mW/cm² model span. A 500 W Bestqool Pro300 measured 58.97 mW/cm² at 12 in in an accredited lab; a community RDPRO1500 report using GembaRed's correction method reported ~80 mW/cm² | Comparators are different panels and cannot calibrate this PL300 [[7]](https://manuals.plus/m/1f6c5530043c6b5ec7e207cd20c205ad0841ef0ecee2e9d40f26befd08b15c4a)[[8]](https://www.reddit.com/r/redlighttherapy/comments/1sjbzgp/measuring_my_rdpro1500_irradiance/) |

## 3. Complete known spec sheet

### 3.1 Seller-advertised and visually observed

| Specification | Known value | Status |
|---|---:|---|
| Model | PL300 | Consistent across supplied material |
| Intended coverage | Half-body / full-body therapy | Seller claim |
| LED lens/package count | 300 | Seller claim; physically plausible from photos |
| LED construction | Dual-chip | Seller claim; die allocation and simultaneous-drive behavior unverified |
| Claimed wavelengths | 630 / 660 / 810 / 830 / 850 nm | Seller claim |
| Dimensions, listing A | 91.4 × 30 × 7 cm (36 × 11.81 × 2.76 in) | Seller claim |
| Dimensions, listing B | ~35.8 × 12 × 2.6 in | Seller claim; final digit partly obscured |
| Weight | 21.2 lb (~9.6 kg) | Seller claim |
| Input | 100–240 V AC | Seller claim |
| Power consumption | 520 W in one listing; 540 W in another | Conflicting seller claims; wall draw unmeasured |
| Advertised irradiance | 170 or max 175 mW/cm² | Seller claim; distance/method absent |
| Advertised distance curve | 145 / 136 / 113 / 105 mW/cm² at 6 / 12 / 18 / 24 in | Seller claim; method absent |
| Advertised coverage | 45 × 22 / 58 × 34 / 67 × 46 / 76 × 59 in at 6 / 12 / 18 / 24 in | Seller claim; intensity threshold defining “coverage” absent |
| Lens / beam angle | Possibly 60°; an anecdotal SAIDI report describes 60° red and 30° NIR | Unverified; not printed in the supplied PL300 material or current manufacturer pages checked |
| EMF | 0.0 µT at 4 in | Seller claim; not independently measured |
| Cooling | Four rear fans visible | Visually observed |
| Controls | Digital control display visible | Visually observed; timer/dimming/pulse behavior not fully established |
| Customization | Logo, shape, and wavelength customization | Seller claim |

### 3.2 Direct meter readings and derived quantities

| Reading | Measurement A | Measurement B | Probable NIR-only C |
|---|---:|---:|---:|
| Total irradiance | 161.241 mW/cm² | 161.049 mW/cm² | ~84.771 mW/cm² |
| FWHM / half-width | 24.1 nm | ~24.8 nm | ~43.0 nm |
| Dominant peak | 660.4 nm | 660.6 nm | ~850.4 nm |
| Displayed NIR band field | 86.2459 mW/cm² | 79.8194 mW/cm² | Obscured |
| Displayed "near red" field | 1.9653 mW/cm² | 1.9949 mW/cm² | Obscured |

The displayed "near red" field is a meter-defined sub-band, not the panel's total red output. It cannot be reconciled with the combined total and the visible 660 nm peak as a full red-channel value.

At the combined measured mean, output accumulates at approximately **9.67 J/cm² per minute**: 30 seconds ≈ 4.83 J/cm²; 1 minute ≈ 9.67 J/cm²; 2 minutes ≈ 19.34 J/cm². This is surface fluence at the meter point, not absorbed dose at a biological target.

## 4. Distance, lens, and dose model

The dose equation is:

`time (seconds) = target fluence (J/cm²) × 1000 / irradiance (mW/cm²)`

The earlier 15-inch estimate of 26 mW/cm² used inverse-square scaling from the 6-inch reading. That remains a poor near-field default for a 36 × 12-inch extended source. The newly supplied seller curve also shows much slower falloff. It does not, however, validate one exact optical model.

### 4.1 Seller curve: raw and anchored

The seller graphic reports four combined-output points. Because its 6-inch value is 145 mW/cm² while the owner's repeatable center reading is 161.145 mW/cm², the visualizer offers a **shape-only calibration**:

`scaled seller E(d) = seller E(d) × 161.145 / 145`

It uses log-linear interpolation only between 6 and 24 inches. It does not extrapolate outside the source graphic's range.

| Distance | Seller raw claim | Seller shape scaled to measured 6 in | 10-minute dose from scaled curve |
|---:|---:|---:|---:|
| 6 in | 145 mW/cm² | 161.1 mW/cm² | 96.7 J/cm² |
| 12 in | 136 mW/cm² | 151.1 mW/cm² | 90.7 J/cm² |
| 18 in | 113 mW/cm² | 125.6 mW/cm² | 75.3 J/cm² |
| 24 in | 105 mW/cm² | 116.7 mW/cm² | 70.0 J/cm² |

Scaling preserves the seller's claimed falloff shape; it does not turn the other distances into measurements. A different center-versus-area definition could explain some of the 6-inch disagreement.

### 4.2 Rectangular lens-array scenario

For a rectangular 36 × 12-inch emitting area, model each point's angular intensity as `I(θ) ∝ cos^m(θ)`. If the quoted beam angle `β` is full-width at half maximum (FWHM), then:

`m = ln(0.5) / ln(cos(β / 2))`

For `β = 60°`, `m ≈ 4.819`. For `β = 30°`, `m ≈ 19.994`. The center-axis geometric factor is numerically integrated across the panel face:

`J(d,m) = ∬A d^(m+1) / (d² + x² + y²)^((m+3)/2) dx dy`

Each channel is normalized to its own 6-inch anchor:

`Echannel(d) = Echannel(6) × J(d,mchannel) / J(6,mchannel)`

The combined 60°/60° scenario uses 161.145 mW/cm² at 6 inches. The alternate 60° red / 30° NIR scenario uses the inferred 76.374 red and probable 84.771 NIR anchors. The alternate exists because one anecdotal SAIDI configuration report describes that split; it is not verified for this unit. [[17]](https://www.reddit.com/r/redlighttherapy/comments/1mgeqa0/halffull_body_panel_idea_light_vs_sgrow_vs_saidi/)

| Distance | Seller-scaled, 6–24 in only | 60° red + 60° NIR | 60° red + 30° NIR | Old Lambertian | 10-min dose range across available extended-source models |
|---:|---:|---:|---:|---:|---:|
| 6 in | 161.1 | 161.1 | 161.1 | 161.1 | 96.7 J/cm² |
| 12 in | 151.1 | 122.7 | 140.2 | 94.4 | 56.6–90.7 J/cm² |
| 18 in | 125.6 | 89.6 | 115.2 | 59.3 | 35.6–75.3 J/cm² |
| 24 in | 116.7 | 66.4 | 93.7 | 39.8 | 23.9–70.0 J/cm² |
| 30 in | — | 50.2 | 76.7 | 28.1 | 16.9–46.0 J/cm² |
| 36 in | — | 38.8 | 63.4 | 20.8 | 12.5–38.0 J/cm² |

All irradiances are mW/cm². These are center-axis calculations, not area averages. They ignore discrete LED spacing, side lobes, spectral meter response, body curvature, clothing, skin angle, and panel-to-panel manufacturing variation.

### 4.3 Coverage geometry

A simple full-angle footprint for a `W × H` panel is:

`footprint width = W + 2d tan(β/2)` and `footprint height = H + 2d tan(β/2)`

With a 12 × 36-inch panel and 60° beam, that predicts about **18.9 × 42.9 inches at 6 inches** and **39.7 × 63.7 inches at 24 inches**. The seller claims 22 × 45 and 59 × 76 inches, respectively. This does not necessarily contradict a 60° FWHM lens: “coverage” may be drawn to a much lower intensity threshold than half maximum, and overlapping edge emitters widen the visible field.

### 4.4 What this changes for a 10-minute, three-times-weekly plan

Ten minutes delivers `dose = irradiance × 0.6`. To keep a 10-minute session near the archive's cautious **8–10 J/cm² per side** planning lane, the measured treatment-position irradiance would need to be only **13.3–16.7 mW/cm²**. For **12–15 J/cm²**, it would need to be **20–25 mW/cm²**. At 36 inches, even the old Lambertian model is ~20.8 mW/cm²; the lens scenarios are ~38.8–63.4 mW/cm².

Therefore, “10 minutes each side, three times weekly” should be treated as a fixed-time ritual that requires **meter-guided distance or dimming**, not as an automatically conservative dose. The seller curve has no 30- or 36-inch observation, so it cannot resolve the uncertainty.

## 4.5 What GembaRed says

GembaRed is a vendor/technical commentator, not a clinical guideline body. Its recurring position is that industry irradiance claims are often inflated by broadband solar meters, that the popular ">100 mW/cm² at 6 inches" benchmark is marketing rather than a clinically established threshold, and that high irradiance can add superficial heat without reliably improving penetration. Its current YouTube search results frame **5–20 mW/cm²** as a commonly recommended clinical range, question whether panels are too powerful, and emphasize exposure time and total joules rather than intensity alone. [[9]](https://gembared.com/blogs/musings/budget-intensity-measurements-pt2-tes-1333-solar-power-meter)[[10]](https://www.youtube.com/watch?v=BYbdGoA5SLQ)

That viewpoint is directionally consistent with the device-measurement problem here, but it should not be treated as settled consensus. GembaRed's claim that essentially no panels deliver 100 mW/cm² conflicts with some calibrated spectroradiometer readings and accredited lab results on high-output devices. The useful takeaway is narrower: identify the meter, verify its range/calibration, distinguish center from area-average irradiance, avoid heat, and do not use a marketing threshold as a treatment target.

## 5. Practical use of the visualizer

1. Prefer **Custom measured irradiance** whenever a reading exists at the real body position and panel mode.
2. Measure center plus four corners at 12, 18, 24, 30, and 36 inches to characterize uniformity and distance falloff. A 10-minute 8–10 J/cm² session requires 13.3–16.7 mW/cm² at the body.
3. Keep mode, distance, angle, panel warm-up, meter orientation, and body position fixed.
4. Treat the preset bands as research-oriented starting ranges, not outcome predictions or toxicity thresholds.
5. Reduce or stop if warmth, redness, dryness, headache, eye symptoms, unusual fatigue, or pigment change persists. Use appropriate opaque eye protection and seek clinician input for photosensitizing medicines, eye disease, suspicious lesions, pregnancy, photosensitive epilepsy, or medically unstable areas.

## Evidence gaps

- Actual wall-power draw (520 vs 540 W conflict).
- Independent EMF measurement and its meter/method.
- Area-average irradiance and edge-to-center uniformity.
- Measured output at any distance other than approximately 6 inches.
- Direct red-only measurement and independent output for each claimed wavelength.
- Exact LED die allocation, lens angle, pulsing frequency/duty cycle, dimming method, flicker, timer range, and whether both chips can run simultaneously at full drive. The 60° and 60°/30° layouts remain scenarios.
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
15. [SAIDI official PL-series page](https://www.saidipro.com/products/pl-series.html) — current family page; PL300 was not visible when checked, which limits exact-variant attribution.
16. [Current Shenzhen SAIDI PL300 marketplace listing](https://indonesian.alibaba.com/product-detail/Saidi-Full-Body-Use-High-Irradiation-1601631569253.html) — close match on model, dimensions, LED count, five-wavelength dual-chip architecture, and 170 mW/cm² claim; its 420 W figure illustrates listing/variant drift.
17. [Community SAIDI panel configuration discussion](https://www.reddit.com/r/redlighttherapy/comments/1mgeqa0/halffull_body_panel_idea_light_vs_sgrow_vs_saidi/) — anecdotal report of 60° red / 30° NIR lenses; included only to define an alternate scenario, not as proof of this PL300's optics.
