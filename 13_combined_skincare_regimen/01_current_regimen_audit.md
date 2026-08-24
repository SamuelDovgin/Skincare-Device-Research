# Current Regimen Audit

*Compiled 2026-07-12; window-UVA analysis added 2026-08-12. Research orientation, not medical advice.*

## 0. Bottom line

Your regimen is not missing a miracle active. It is **high-evidence but crowded**: daily vitamin C, azelaic acid, adapalene, a fractional laser, and full-body RLT can coexist across a week, but the Tria/azelaic/adapalene cluster should not be treated as one ordinary evening.

The new cross-atlas audit reaches the same conclusion with a broader peer-reviewed ledger: the routine already overlaps six of the first eleven ranked atlas positions. The main missing layer is exact product, dose, endpoint, and schedule verification. Read the rendered [highest-value categories versus the current routine](../16_skin_improvement_evidence_atlas/index.html#doc8).

## 1. The supplied routine

| Window | Current steps | Audit |
|---|---|---|
| Morning | Wash → Trader Joe's vitamin C → CeraVe lotion | Keep; cleanser can become a water rinse if skin is dry/tight |
| Daily | 10-minute full-body PL300 RLT panel | Re-audit: time alone is not dose. At 12 inches, the current modeled point-reading range converts ten minutes to roughly 31–79 J/cm² per side, well above the archive's cautious 8–10 J/cm² whole-body starting lane; measure or dim rather than assuming daily use is conservative |
| If outside | Round Lab SPF 50 face → random body sunscreen | Keep broad-spectrum protection for meaningful outdoor exposure; the photographed indirect-light desk is analyzed separately below and does not justify a blanket “indoor sunscreen is mandatory” rule |
| After gym | Wash → Tria Age-Defying laser → Good Molecules azelaic acid → “Cretaceous” moisturizer | Split: Tria needs clean, dry skin, but azelaic acid immediately afterward adds avoidable sting/irritation risk |
| Bedtime | Wash → adapalene 0.1% → CeraVe moisturizer | Strong core on non-Tria nights; a third cleanse is unnecessary when post-gym and bedtime are close |

## 2. Sunscreen at this desk: room-specific UVA model

### Decision answer

The photographed setup is **not zero UVA**, but it is also not equivalent to sitting in a direct sunbeam. Interpreting the two-window view as about **80° combined**, with the face about **2 m away**, visible sky roughly **5–30° above the outdoor horizon**, no direct sun on the skin, double-pane clear glass, insect screens/mullions, and no rear windows:

- **Central estimate:** **3.5% of simultaneous outdoor facial UVA**.
- **Plausible range:** approximately **1–9%**, driven mostly by unknown glazing/coating transmission, sky conditions, exact facial orientation, and how much of the apparent window is open sky rather than houses/trees.
- **Eight-hour interpretation:** about **17 outdoor-UVA-equivalent minutes** at the central estimate; the 1–9% sensitivity range is about **5–43 minutes**. This is a relative dose analogy, not a biological safety threshold.
- **If “80° wide” means each window rather than both together:** the central estimate rises to roughly **5–7%**, with an intentionally conservative upper sensitivity near **14%**.

For collagen preservation, this supports a nuanced conclusion: **indoor sunscreen at this desk is an optional maximum-photoprotection step, not a demonstrated necessity**. Keeping direct sunlight off the skin is the highest-value control. Sunscreen, a partial blind, verified UV-rejecting film, or a different desk angle becomes more compelling during immediate Tria recovery, with melasma or a photosensitive disorder, or if a direct sun patch begins reaching the face.

### The face-oriented calculation

For a vertical face looking toward an approximately rectangular patch of diffuse sky, the fraction of all front-hemisphere diffuse irradiance contributed by that patch is:

`A_face = [2 sin(W/2) / pi] × [(alpha_2 - alpha_1)/2 + (sin(2 alpha_2) - sin(2 alpha_1))/4]`

Angles are in radians. `W` is horizontal angular width; `alpha_1` and `alpha_2` are the lower and upper sky elevations. This is a projected-solid-angle calculation: rays closer to the direction the face points receive more weight than rays arriving at a grazing angle.

The indoor-to-outdoor UVA proxy is then:

`R_UVA = A_face × f_diffuse × T_glass × T_screen/frame`

| Input | Central value | Sensitivity used | Evidence class / reason |
|---|---:|---:|---|
| Horizontal sky width `W` | 80° combined | 70–90°; 160° alternate interpretation | User estimate plus photographs; measured input with interpretation uncertainty |
| Visible-sky elevation | 5–30° | 10–30° to 0–35° | Photo-derived illustrative geometry; lower view is partly blocked by houses and trees |
| Face-projected aperture `A_face` | 0.160 | 0.125–0.221 | Equation output, not a measured irradiance |
| Outdoor UVA diffuse fraction `f_diffuse` | 0.60 | 0.40–0.80 | Illustrative atmospheric assumption; varies with sun angle, clouds, aerosols, and ground reflectance [[5]](https://onlinelibrary.wiley.com/doi/full/10.1111/php.70084) |
| Double-pane UVA transmission `T_glass` | 0.48 | 0.30–0.60 | Literature-informed assumption; a fenestration review reports 48% UV transmission for standard double-pane insulating glass, but the actual unit/coating is unknown [[6]](https://www.mdpi.com/2075-5309/13/7/1670) |
| Screen, mullion, and frame transmission | 0.75 | 0.65–0.85 | Illustrative open-area factor inferred from the photographs; not spectrally measured |

Central result:

`0.160 × 0.60 × 0.48 × 0.75 = 0.0346`, or **3.46%**.

The sensitivity endpoints are not a confidence interval. They are a deliberately broad product of plausible inputs:

`0.125 × 0.40 × 0.30 × 0.65 = 0.0098` (**about 1%**)

`0.221 × 0.80 × 0.60 × 0.85 = 0.0902` (**about 9%**)

### Contending with the Lab Muffin calculation

Lab Muffin's framework is directionally correct: when direct sun is excluded, only diffuse sky seen through the window can contribute, and window geometry can make exposure fractional. [[7]](https://labmuffin.com/should-you-wear-sunscreen-indoors-an-analysis-with-video/) Applying her unweighted hemispheric sky-view fraction to this room gives:

- apparent sky solid angle: `80° × [sin(30°) - sin(5°)] = 0.577 steradian`;
- fraction of the full sky hemisphere: `0.577 / (2 pi) = 9.18%`;
- indoor UVA proxy: `0.0918 × 0.60 × 0.48 × 0.75 = 1.98%`.

The independent central estimate here is higher—**3.5% rather than 2.0%**—because a face looking toward the windows should not weight every direction in the sky hemisphere equally. The projected-solid-angle model gives more weight to light arriving near the facial normal. Conversely, monitors, a turned head, window obliquity, trees/houses, and a low-E coating can push the real exposure below the central estimate. This is why the decision uses a range rather than presenting 2.0% or 3.5% as a measurement.

### What the research confirms—and what it does not

- Measurements across 77 windows found that most eliminated wavelengths below 320 nm, while indoor UV varied substantially with glass, solar angle, direct versus diffuse light, and distance; room reflections contributed little to the room-average exposure. [[8]](https://pubmed.ncbi.nlm.nih.gov/33373097/)
- Ordinary single smooth glass has transmitted up to 74.3% UVA in experimental testing while blocking UVB, but **double pane does not automatically mean a known UVA rating**. Two layers generally lower transmission; low-E, laminated, tinted, or UV-film constructions can lower it much further. Thickness alone is less informative than composition and coating. [[9]](https://pubmed.ncbi.nlm.nih.gov/19614895/)[[10]](https://pubmed.ncbi.nlm.nih.gov/23458389/)
- The UV Index is erythema-weighted and cannot be multiplied directly by this UVA percentage to obtain an “indoor UV Index.” Because the glass removes almost all UVB, indoor erythemal exposure should be much smaller than the UVA percentage suggests. [[11]](https://www.epa.gov/sunsafety/calculating-uv-index-0)
- Repeated suberythemal UVA can alter human skin, but the controlled human studies used known lamp doses and do not establish a clinical photoaging threshold for this much lower, unmeasured indoor exposure. [[12]](https://pubmed.ncbi.nlm.nih.gov/7490465/)

**What would make this an actual measurement:** the glazing manufacturer/model and its wavelength-resolved transmission curve, or a calibrated spectroradiometer/UVA radiometer measured at face position across representative clear and cloudy days. A consumer UV-Index sensor is not an adequate substitute because it may be nearly blind to the long-wave UVA that passes through glass.

## 3. Keep / change / do not add

### Keep

- Broad-spectrum SPF 50 for outdoor or direct-window exposure; at this specific indirect-light desk, daily indoor use is optional rather than mandatory. Reapply after sweat and according to the label while outdoors.
- Adapalene 0.1% once daily **at most**, on a schedule the skin tolerates. The label supports moisturizer and reducing/stopping if severe irritation develops. [[1]](https://dailymed.nlm.nih.gov/dailymed/drugInfo.cfm?setid=5d5340d6-e1da-46e4-973c-40cf8e907aa3)
- Azelaic acid for acne/redness/pigment goals. Evidence is stronger for those indications than for anti-aging itself. [[2]](https://pubmed.ncbi.nlm.nih.gov/37550898/)
- Vitamin C in the morning if it remains comfortable and has not oxidized.
- Bland moisturizer after active/device sessions.
- RLT only after converting a treatment-plane measurement into fluence for a named endpoint. The current daily ten-minute PL300 practice is not trial-matchable: modern facial studies used measured wavelength, irradiance, fluence, geometry, and usually 2–3 sessions weekly, while the current whole-body audit uses a cautious 8–10 J/cm² starting exposure twice weekly. This does not prove the current practice is harmful; it shows that “10 minutes daily” is not an evidence-defined dose. [[13]](https://pubmed.ncbi.nlm.nih.gov/40167796/)

### Change

- Create three night types: **Tria**, **adapalene**, and **recovery**.
- On Tria nights: cleanse, dry, use the device per IFU, moisturize. Do not automatically apply azelaic acid and adapalene afterward.
- On adapalene nights: gentle cleanse, dry, pea-size layer, moisturizer. Do not add a second retinoid.
- On recovery nights: moisturizer only; sunscreen the next morning.
- Merge the after-gym and bedtime washes when practical.

### Do not add now

- Tretinoin, retinol, retinal, or another retinoid on top of adapalene.
- AHA/glycolic/lactic peel nights during a high-frequency Tria course.
- A home microneedling, RF-microneedling, HIFU, or strong IPL “rejuvenation” stack.
- More antioxidant/brightening serums until sunscreen timing and irritation are stable.

## 4. A practical weekly starting framework

This is a conservative template, not a personalized prescription or a claim about a required drug-device washout:

| Day type | Evening |
|---|---|
| Tria day | Cleanse → fully dry → Tria per IFU → bland moisturizer |
| Adapalene day | Cleanse → fully dry → adapalene 0.1% → moisturizer |
| Recovery day | Cleanse/rinse → moisturizer only |

The Tria IFU labels a five-nights/week, 12-week course. That cadence leaves little room for nightly adapalene without stacking. Choose the priority for that course with a dermatologist if you need both at high frequency; do not turn the two rest nights into mandatory aggressive-active nights when skin is still reactive. [[3]](../03_fractional_laser_resurfacing/tria_smoothbeauty/source_docs/tria-smoothbeauty-instructions-for-use.pdf)

## 5. Stop/scale-back rules

- Persistent burning, worsening redness, cracking, marked peeling, swelling, blistering, scabbing, or darkening: stop the newest/aggressive step and allow recovery.
- Severe adapalene irritation: the Drug Facts label says stop and ask a doctor before restarting. [[1]](https://dailymed.nlm.nih.gov/dailymed/drugInfo.cfm?setid=5d5340d6-e1da-46e4-973c-40cf8e907aa3)
- Skin still red/swollen from Tria: the IFU says do not re-treat.
- New or worsening pigment after the laser deserves early caution, especially with a history of melasma/PIH.

## Evidence gaps

- “Trader Joe vitamin C serum” and “Cretaceous moisturizer” are not exact product identities.
- No controlled trial establishes an exact number of hours between OTC adapalene, 10% azelaic acid, and this home fractional laser.
- The PL300 now has a device audit and modeled range, but no measured treatment-plane grid at the actual body/face position. At 12 inches, ten minutes is modeled at roughly 31–79 J/cm² per side; the current cautious whole-body planning lane starts at 8–10 J/cm² twice weekly. Use the rendered [whole-body PBM dose audit](../markdown-viewer.html?file=04_red_light_therapy_handheld/05_whole_body_pbm_dosing_evidence.md), not the old minutes-only assumption.
- The desk estimate is a geometry-and-transmission model, not a skin-level UV measurement. The largest unresolved input is the double-pane unit's actual UVA transmission/low-E specification.

## Sources

1. DailyMed adapalene gel 0.1%. https://dailymed.nlm.nih.gov/dailymed/drugInfo.cfm?setid=5d5340d6-e1da-46e4-973c-40cf8e907aa3 - once-daily limit, irritation, sunscreen, moisturizer, and stop guidance.
2. King S et al. Azelaic acid systematic review. https://pubmed.ncbi.nlm.nih.gov/37550898/ - RCT evidence for acne, rosacea, and melasma; none eligible for skin aging.
3. Tria SmoothBeauty IFU. [Local PDF](../03_fractional_laser_resurfacing/tria_smoothbeauty/source_docs/tria-smoothbeauty-instructions-for-use.pdf) - labeled preparation, cadence, contraindications, expected reactions, and stop rules.
4. AAD Practice Safe Sun. https://www.aad.org/public/everyday-care/sun-protection/shade-clothing-sunscreen/practice-safe-sun - SPF, protective clothing, and reapplication guidance.
5. Parisi AV et al. *Measurement and modeling of diffuse ultraviolet radiation: A review.* Photochem Photobiol. 2026. https://onlinelibrary.wiley.com/doi/full/10.1111/php.70084 - diffuse/direct UVA ratios vary with clouds, aerosols, albedo, scattering, and solar zenith angle.
6. Onatayo DA, Srinivasan RS, Shah B. *Ultraviolet Radiation Transmission in Buildings' Fenestration: Part I.* Buildings. 2023. https://www.mdpi.com/2075-5309/13/7/1670 - review/table reporting approximately 48% UV transmission for standard double-pane insulating glass and much lower transmission for some treated systems; used here as a cross-spectrum proxy rather than a measured UVA value for this room.
7. Wong M. *Should You Wear Sunscreen Indoors? The Science.* Lab Muffin Beauty Science. 2020. https://labmuffin.com/should-you-wear-sunscreen-indoors-an-analysis-with-video/ - secondary-source sky-view framework reproduced and challenged here with a face-projected model.
8. Zhou S et al. *Factors affecting wavelength-resolved ultraviolet irradiance indoors and their impacts on indoor photochemistry.* Indoor Air. 2021. https://pubmed.ncbi.nlm.nih.gov/33373097/ - 77-window measurement/model study; direct/diffuse light, window type, angle, and distance mattered, and room-average reflected UV was minor.
9. Duarte I et al. *The role of glass as a barrier against the transmission of ultraviolet radiation.* Photodermatol Photoimmunol Photomed. 2009. https://pubmed.ncbi.nlm.nih.gov/19614895/ - ordinary smooth glass transmitted up to 74.3% UVA in the experiment, whereas all tested glass blocked UVB.
10. Almutawa F et al. *Current status of photoprotection by window glass, automobile glass, window films, and sunglasses.* 2013. https://pubmed.ncbi.nlm.nih.gov/23458389/ - glass type and coating dominate UVA protection; thickness has a smaller effect.
11. U.S. EPA. *Calculating the UV Index.* https://www.epa.gov/sunsafety/calculating-uv-index-0 - explains erythemal spectral weighting and why UVI is not a UVA radiometer.
12. Lowe NJ et al. *Low doses of repetitive ultraviolet A induce morphologic changes in human skin.* J Invest Dermatol. 1995. https://pubmed.ncbi.nlm.nih.gov/7490465/ - repeated controlled suberythemal UVA caused histologic changes, but does not validate a threshold for modeled indoor window exposure.
13. Bragato EF et al. *Role of photobiomodulation application frequency in facial rejuvenation.* Lasers Med Sci. 2025. https://pubmed.ncbi.nlm.nih.gov/40167796/ - sham-controlled 660 nm facial trial at 8.05 J/cm²; two versus three weekly sessions did not meaningfully differ.
14. Geronemus R et al. *A treatment system for enhanced efficacy of a 1440 nm fractional non-ablative laser.* J Cosmet Laser Ther. 2016. https://pubmed.ncbi.nlm.nih.gov/26727154/ - current 5-times-weekly, 12-week Tria schedule closely matches published use, but all faces received laser and no sham-laser control isolated the device effect.
