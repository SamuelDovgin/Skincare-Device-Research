# Comparable Red-Light Panel Irradiance Falloff

*Online measurement scan completed 2026-07-13. This is a measurement-method comparison and PL300 model check, not medical advice or a product endorsement.*

## Bottom line

The PL300 seller's **falloff shape is plausible for a large LED array**, even though its absolute irradiance remains unverified. Normalized to each source's own 6-inch value, the seller retains **93.8% at 12 inches** and **72.4% at 24 inches**. Across the broader comparison set, the median retained centerline output is **85.6% at 12 inches** and **69.9% at 24 inches**. The seller curve is therefore toward the slow-falloff end at 12 inches and almost on the observed median at 24 inches.

That finding changes the model interpretation:

- The old Lambertian curve falls substantially faster than every included large-array centerline curve at both 12 and 24 inches. It is useful as a steep-falloff sensitivity bound, not as the most evidence-aligned default.
- The idealized **60° red / 60° NIR** curve also falls somewhat faster than the observed comparison range.
- The unverified **60° red / 30° NIR** split is closest to the empirical median at 12 inches and remains inside the observed range at 24 inches. This is a shape match, not proof that the PL300 has that lens configuration.
- Beam-angle labels alone do not predict a panel's distance curve. Array dimensions, emitter spacing, focal overlap, channel optics, drive level, and measurement location all matter.

Most importantly, normalized falloff cannot validate an absolute dose. Accredited spectral measurements on similarly sized panels were around **69–72 mW/cm² at 6 inches**, while reviewer measurements on older large panels were roughly **60–86 mW/cm²**. The supplied PL300 meter photos show about **161 mW/cm²**, but that result exceeds the standard published range of the identified meter family unless it is a customized high-range unit. A measurement at the actual body position is still the deciding evidence.

## 1. How the comparison was built

The search prioritized sources that reported at least two explicit distances on the same panel and mode. Evidence is separated into four tiers:

| Tier | Source type | What it can establish |
|---|---|---|
| A | Accredited laboratory report using spectral irradiance equipment | Strongest available irradiance/method evidence for that tested unit |
| B | Independent reviewer measurement using a spectrometer | Useful direct comparison; less controlled and potentially commercially conflicted |
| C | Owner measurement with a named broadband meter and correction method | Anecdotal shape check; absolute values remain meter- and correction-dependent |
| D | Manufacturer manual or seller graphic without a disclosed meter/protocol | Company claim; useful for claimed curve shape only |

The comparison uses **center-point or source-designated readings**, because that is what most sources provide. Center output is not the same as the illuminated-area average. The complete row-level dataset, including geometry, method, notes, and URLs, is preserved in [`comparable_panel_falloff_2026-07-13.csv`](pl300_source_docs/comparable_panel_falloff_2026-07-13.csv).

## 2. Measurements found online

| Source and geometry | Tier / method | 6 in | 12 in | 24 in | 36 in | Retained from 6 in |
|---|---|---:|---:|---:|---:|---|
| Bestqool Pro300; 36.4 × 13.5 in, 300 LEDs | A; LightLab spectral meter, center | 68.90 | 58.97 | — | — | 12 in: **85.6%** |
| Helio Glow; 29.9 × 11.8 in, 216 LEDs | A; LightLab visible+NIR spectral meters, 231-point grid | 71.72 | 75.01 | 65.25 | 49.38 | 12: **104.6%**; 24: **91.0%**; 36: **68.9%** |
| Red Light Rising Advantage1500; 500 LEDs | B; reviewer spectrometer | 60 | 50 | 28 | — | 12: **83.3%**; 24: **46.7%** |
| older MitoPRO1500; 300 LEDs | B; reviewer spectrometer | 86 | — | 40 | — | 24: **46.5%** |
| RDPRO1500; 300 dual-chip LEDs | C; owner solar meter plus spectral correction | 84 | 80 | 75 at 20 in | 50 at 31 in | 12: **95.2%**; 20: **89.3%**; 31: **59.5%** |
| BioMax 900 four-panel array | B; reviewer spectrometer | 84 | 71 | 61 | — | 12: **84.5%**; 24: **72.6%** |
| Full Body Red Light Panel; 67.6 × 16.3 in, 840 LEDs | D; manufacturer manual, method absent | 154.6 | 141.0 | 108.0 | — | 12: **91.2%**; 24: **69.9%** |
| Hooga SaunaPRO; 39.9 × 10.9 in, 280 LEDs | D; manufacturer manual, method absent | 70 | 55 | — | — | 12: **78.6%** |
| Supplied PL300 seller graphic; 36 × 12 in, 300 LEDs | D; seller graphic, method absent | 145 | 136 | 105 | — | 12: **93.8%**; 24: **72.4%** |

All irradiance values are mW/cm². The Helio center reading increases slightly between 6 and 12 inches. That is not a transcription error: the lab's mapped results show the same behavior, consistent with a focused array whose beam overlap changes in the near field. It is a useful warning against forcing every large-panel curve to be monotonically decreasing at very close distances.

The BioMax entry is a four-panel array, so it is included as an extended-source geometry check rather than a direct PL300 analog. The manufacturer-manual rows are retained because they add distance points, but they are not treated as independent validation.

## 3. Normalized comparison with the PL300 models

Normalizing each curve to `E(6 in) = 1.000` reduces—not eliminates—bias from different meter spectral responses and absolute calibration.

| Curve | 12 in / 6 in | 24 in / 6 in | 36 in / 6 in | Interpretation |
|---|---:|---:|---:|---|
| PL300 seller claim | **0.938** | **0.724** | — | Slow falloff, but inside the observed large-array range |
| Broader comparison median | **0.856** (7 curves) | **0.699** (5 curves) | — | Descriptive benchmark, not a PL300 prediction |
| Idealized 60° red / 60° NIR | 0.761 | 0.412 | 0.241 | Faster falloff than the observed comparison range at 12 and 24 in |
| Idealized 60° red / 30° NIR | **0.870** | **0.581** | 0.393 | Closest model to the 12-in median; inside the 24-in range |
| Old Lambertian extended-panel model | 0.586 | 0.247 | 0.129 | Steeper than every included large-array center curve at 12 and 24 in |

The available 12-inch normalized values span **0.786–1.046**; the five 24-inch values span **0.465–0.910**. Only the narrow-beam Helio panel supplies a strong 36-inch laboratory observation, so there is not enough comparable evidence to define a credible 36-inch median or envelope.

The reviewer comparison also undermines a simplistic reading of nominal beam angle: a claimed 60° MitoPRO1500 and a claimed 30° Advantage1500 both retained about 46–47% at 24 inches. The reviewer found that the larger angle label did not produce the expected wider field. Treat the PL300's recalled “60°” lens as one input to a scenario, not a measured optical transfer function.

## 4. What this means for a 10-minute session

Ten minutes delivers `dose (J/cm²) = irradiance (mW/cm²) × 0.6`.

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

## Evidence gaps

- No independent multi-distance PL300 measurement was found.
- No discovered PL300 document confirms the lens angle, red/NIR angle split, center-versus-average convention, meter, stabilization time, or calibration method behind the seller curve.
- The comparison is too heterogeneous for a formal prediction interval: panels differ in dimensions, wavelengths, chip arrangements, optics, drive power, and test methods.
- There are too few comparable measurements beyond 24 inches to choose a reliable 36-inch empirical curve.
- The owner's meter range option and current calibration certificate remain unknown.
