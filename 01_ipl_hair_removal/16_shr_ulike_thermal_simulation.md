# IPL/SHR Follicle Heating — What Temperature Actually Produces Damage?

*Compiled 2026-07-01; substantially revised 2026-07-10. Research orientation, not medical advice. The paired simulator is an exposure model, not a device-setting or patient-safety calculator.*

> **[Open the revised interactive thermal simulator](shr_thermal_simulator.html).** It now answers the temperature question with a time–temperature curve and a published Arrhenius damage integral. It no longer treats 65 °C as an instantaneous switch or 45–50 °C as a proven “accumulation kill” threshold.

## 0. Bottom line

1. **There is no single “right temperature.”** Thermal injury depends on both temperature and dwell time. The simulator uses the Arrhenius parameter pair reported in an 810 nm hair-removal simulation: frequency factor **A = 3.1 × 10^98 s−1**, activation energy **E = 6.3 × 10^5 J/mol**, and **Ω = 1** as its irreversible-injury criterion.[[1]](https://journals.sagepub.com/doi/10.1089/pho.2010.2895)
2. **Under that one published parameterization**, constant temperature would need about **1.95 s at 60 °C**, **0.50 s at 62 °C**, **67.5 ms at 65 °C**, **9.4 ms at 68 °C**, or **2.6 ms at 70 °C** to reach Ω = 1. A 1 ms excursion to 65 °C gives only Ω ≈ 0.015. That is why the full temperature history matters more than whether a curve briefly touches a horizontal line.
3. **“65 °C damages follicles” remains a useful modeling convention, not a universal instant switch.** Fiskerstrand et al. used 65 °C as a follicular damage threshold in a heat-diffusion model paired with a 29-patient clinical comparison, but their one-pulse and split-pulse systems produced similar hair reduction despite very different modeled peaks.[[2]](https://pubmed.ncbi.nlm.nih.gov/12766964/)
4. **45–50 °C is an SHR protocol description, not a validated permanent-destruction threshold.** Professional low-fluence/high-repetition studies show real hair reduction and lower pain, but histology suggests apoptosis may contribute and no paper validates one universal 45 °C follicle-stem-cell kill line.[[3]](https://pmc.ncbi.nlm.nih.gov/articles/PMC5515709/)[[4]](https://ijdvl.com/methods-to-overcome-poor-responses-and-challenges-of-laser-hair-removal-in-dark-skin/)
5. **Heating the pigmented hair is not identical to destroying every regenerative target.** The shaft/bulb is the absorber and heat source; durable reduction depends on injury to vulnerable follicular structures around it. Human histology after one ruby-laser treatment has even found acute damage without evidence of permanent follicle death.[[5]](https://pubmed.ncbi.nlm.nih.gov/10100652/)
6. **No public home-IPL specification is sufficient to calculate a real follicle temperature.** Wavelength spectrum, depth-dependent fluence, absorption/scattering, hair geometry and melanin, pulse shape, overlap, contact, and cooling boundary conditions are missing. The simulator therefore reports a transparent *central illustrative trace* and labels its Ω output as a model criterion—not a prediction.
7. **Returning near baseline is not the same as erasing pulse history.** Direct hair experiments used ≥2 s pulse spacing plus an air blower so measured temperature returned to ambient, yet subsequent pulses still produced larger temperature rises. Around a 55 °C pulse, the induced response lasted about 5 s; after >70 °C it persisted beyond 60 s. That was shown with alexandrite/Nd:YAG on isolated hair, not broadband IPL in living skin, so the simulator exposes it as an optional cross-wavelength sensitivity rather than silently assuming it.[[9]](thermal_model_source_docs/PMC10107531_hair_temperature_avalanche_fulltext.xml)

## 1. Why the old version needed correction

The earlier simulator had two useful ideas: short inter-pulse gaps produce thermal carryover, and the deep nonpigmented target warms more slowly than the pigmented heater. But its injury logic had three problems:

- It called a brief peak above **65 °C** an immediate “coagulation kill,” even though thermal denaturation is time-dependent.
- It integrated simple **degree-seconds above 40 °C** and labeled the result “CEM43-style,” then used an arbitrary threshold to declare an “accumulation kill.” That was neither the CEM43 equation nor a validated follicle endpoint.
- It treated **45–50 °C**—a temperature range repeated in SHR explanations—as a lethal floor. The clinical SHR literature supports outcomes, not that specific universal kill threshold.

The revised version separates three questions:

| Question | Revised output |
|---|---|
| Does the pigmented heater itself accumulate generic coagulative injury? | Hair/follicle-heater Arrhenius **Ω** |
| Does the slower deeper regenerative-tissue proxy accumulate that injury? | Deep-target Arrhenius **Ω** |
| Does the curve enter the temperature range associated with gradual-heating SHR descriptions? | **Time at or above 45 °C**, explicitly descriptive and nonlethal |

It also calculates epidermal Ω with the same parameter set as a sensitivity warning while plainly stating that the coefficients are not validated separately for each compartment.

## 2. The injury equation and what Ω means

The thermal damage integral is:

\[
\Omega(t)=\int_0^t A\exp\left(-\frac{E}{R\,T(\tau)}\right)d\tau
\]

where temperature is in Kelvin and **R = 8.314 J·mol−1·K−1**. In the first-order interpretation, the modeled transformed fraction is **1 − e^−Ω**; Ω = 1 corresponds to about **63%** transformation.[[1]](https://journals.sagepub.com/doi/10.1089/pho.2010.2895)

### Constant-temperature reference table

| Tissue temperature | Time to Ω = 1 with the selected A/E pair | What to remember |
|---:|---:|---|
| 50 °C | 37.0 min | Far longer than a home-IPL burst |
| 55 °C | 62.4 s | Still a sustained exposure |
| 60 °C | 1.95 s | Seconds, not milliseconds |
| 62 °C | 0.502 s | About half a second |
| 65 °C | 67.5 ms | The familiar rule of thumb becomes time-dependent |
| 68 °C | 9.4 ms | Within a long IPL/laser pulse scale |
| 70 °C | 2.6 ms | A short high-temperature exposure can accumulate substantial Ω |
| 72 °C | 0.72 ms | Very brief exposure can cross the model criterion |

This table is **not a clinical dosing table**. It only demonstrates the selected equation. Arrhenius parameter pairs vary enormously by tissue, temperature range, and measured endpoint. Photothermal cell experiments also warn that CEM43 is most useful for long-duration hyperthermia, while short laser injury is better represented by transient Arrhenius integration—and even that can under- or overpredict individual damage.[[6]](thermal_model_source_docs/PMC6977020_photothermal_damage_rate_kinetics_fulltext.xml)[[7]](https://pmc.ncbi.nlm.nih.gov/articles/PMC5459687/)

## 3. What human hair-removal studies actually measured

### 3.1 Temperature measurements

Topping et al. fired a 15 J/cm² normal-mode ruby laser into ex vivo human facelift skin while recording the exposed deep surface with thermal imaging. The most common follicular rise was **5–10 °C**, while follicles from one patient exceeded a **30 °C rise**; higher-temperature follicles showed deeper and broader injury. The study supports a temperature–damage relationship but also shows large follicle-to-follicle and patient-to-patient variability.[[8]](https://pubmed.ncbi.nlm.nih.gov/10884072/)

A newer bench study measured human-hair photothermal responses to alexandrite and Nd:YAG hair-removal lasers and found nonlinear changes over repeated low-fluence pulses as hair structure and water content changed. Crucially, the investigators deliberately used **≥2 s separation and an air blower so measured hair temperature returned to ambient between pulses**. Even with that thermal reset, the same hair developed hysteresis and progressively greater temperature rises. At pulse temperatures around **55 ± 2.5 °C**, the induced response had an approximately **5 s** lifetime; when pulses pushed hair above about **70 °C**, it persisted for **more than 60 s**. Up to 50 low-fluence pulses at 0.5 Hz produced thermal gain approaching or exceeding 2 in parts of the experiment.[[9]](thermal_model_source_docs/PMC10107531_hair_temperature_avalanche_fulltext.xml)

That result forces a two-layer interpretation:

- **Thermal carryover:** the next pulse starts above baseline because excess temperature remains.
- **Pulse-history sensitivity:** temperature may return to baseline while the hair's optical/structural response has not; the next pulse can still generate a larger rise.

The second layer is direct hair evidence, but its magnitude is not validated for a broadband xenon spectrum, sapphire-cooled contact, an in-skin follicle, or a four-pulse home burst. The simulator therefore gives it a clearly labeled on/off control and caps the illustrative gain at 2 rather than treating the laser result as a measured IPL coefficient.

### 3.2 Histology

- Grossman et al. found permanent loss in some normal-mode ruby-laser sites but said the biological mechanism and responsible targets remained uncertain; miniaturization of the bulb/papilla was one plausible pathway.[[10]](https://jamanetwork.com/journals/jamadermatology/fullarticle/189173)
- Goldberg and Silapunt found selective acute follicular injury after 50 ms Nd:YAG pulses in six patients, but the tested fluences did not significantly change average injury depth.[[11]](https://pubmed.ncbi.nlm.nih.gov/11241524/)
- Kato et al. found immediate moderate follicular damage and, one month later, cystic change and foreign-body giant cells after ruby or alexandrite exposure.[[12]](thermal_model_source_docs/Kato_2002_histological_changes_hair_removal_lasers.pdf)
- A separate 3 ms ruby-laser histology study found **no evidence of permanent follicle death after one treatment**, an important limit on any one-flash “kill” claim.[[5]](https://pubmed.ncbi.nlm.nih.gov/10100652/)

The responsible biological endpoint is therefore not simply “the shaft reached X °C.” Heater injury, outer-root-sheath injury, bulge/hair-germ stem cells, matrix/papilla damage, apoptosis, miniaturization, and the hair-cycle stage can produce different short- and long-term outcomes.

## 4. Thermal clocks: TRT is not TDT, and neither is the injury threshold

| Quantity | Evidence range | Correct interpretation |
|---|---:|---|
| Epidermal thermal relaxation | about 1.6–10 ms | Surface heat can diffuse rapidly; clinical sequential-pulse gaps often allow partial epidermal cooling.[[13]](https://pmc.ncbi.nlm.nih.gov/articles/PMC5108992/)[[14]](https://www.ncbi.nlm.nih.gov/books/NBK580525/) |
| Hair shaft/follicle thermal relaxation | about 40–100 ms for 200–300 µm follicles; smaller targets can be faster | **TRT means the time to lose 50% of induced heat**, not the time to reach baseline. An IPL-specific Monte Carlo/heat-diffusion study used this definition and found close pulse stacking more efficient than a stack with longer off-times.[[15]](https://pmc.ncbi.nlm.nih.gov/articles/PMC9541334/)[[26]](thermal_model_source_docs/PMC5718238_broadband_IPL_pulse_structure_model_fulltext.xml) |
| Hair pulse-history sensitivity | about 5 s near 55 °C; >60 s above 70 °C in one isolated-hair experiment | A separate response-memory clock can outlast measurable temperature excess; direct alexandrite/Nd:YAG evidence, not yet validated for home IPL.[[9]](thermal_model_source_docs/PMC10107531_hair_temperature_avalanche_fulltext.xml) |
| Thermal Damage Time (extended target) | reported 170–1000 ms; one best clinical result at 400 ms | A diffusion timescale for transferring heat from absorber to a larger vulnerable target—not “hold any temperature for 400 ms and it dies.”[[17]](https://pubmed.ncbi.nlm.nih.gov/12030874/)[[18]](https://jcasonline.com/thermal-kinetic-selectivity-and-lasers/) |
| Arrhenius Ω | depends on the entire temperature trace | The injury model. TDT affects the trace; it does not replace the damage equation. |

This distinction matters for a four-pulse home burst. At a 250 ms gap, a terminal follicle with a 100 ms TRT half-time retains about **18%** of its original excess temperature under a single-exponential approximation; one with a 40 ms half-time retains about **1%**. Neither is “fully baseline,” and the slower deep-tissue tail can be larger. Separately, the measured-laser response-memory experiment suggests prior pulses could still modify later hair heating after the temperature tail becomes small. None of those facts proves Ω reached a damaging endpoint.

## 5. What the professional SHR evidence proves

Professional “in-motion” SHR is not merely two to four stamps at one spot. It combines low-to-moderate per-pulse fluence, high repetition, continuous motion, overlap, and many hits within a treatment pass.

| Study | Exposure | Result |
|---|---|---|
| Braun 2009 | 810 nm, 5–10 J/cm² at 10 Hz vs 25–40 J/cm² at 1 Hz | Comparable 86–91% reduction; low-fluence mode much less painful.[[19]](https://pubmed.ncbi.nlm.nih.gov/19916262/) |
| Omi 2017 | dynamic 10 Hz/10 J/cm² vs static 1 Hz/30 J/cm² | No significant efficacy difference; histology favored an apoptosis explanation for long-term effect.[[3]](https://pmc.ncbi.nlm.nih.gov/articles/PMC5515709/) |
| Koo 2014 | low-fluence multi-pass vs high-fluence single-pass 810 nm | 40.7% vs 33.5% reduction, not significantly different; low-fluence mode less painful.[[20]](https://pubmed.ncbi.nlm.nih.gov/24752608/) |
| Li 2016 | SHR vs high-fluence mode, same 810 nm platform | 90.2% vs 87% reduction and lower pain with SHR.[[21]](https://pubmed.ncbi.nlm.nih.gov/27419804/) |
| Wanitphakdeedecha 2012 | diode SHR vs high-fluence Nd:YAG | Nd:YAG produced greater reduction, 54.2% vs 35.7%.[[22]](https://pubmed.ncbi.nlm.nih.gov/21923659/) |
| Barolet 2012 | 15 J/cm² at 5 Hz | Significant 12-month reduction after four monthly sessions.[[23]](https://pubmed.ncbi.nlm.nih.gov/22437967/) |

These studies support **the clinical delivery method and outcomes**. They do not validate a home burst at roughly 1.7 J/cm² per sub-pulse, an undisclosed intra-burst gap, or a universal 45 °C destruction endpoint.

## 6. Ulike Air 10: what is verified, marketed, and still unknown

As of 2026-07-10, Ulike's current Air 10 page says SHR delivers **26 J per four-pulse burst**, **four flashes per second**, dual light sources, and contact cooling to **65 °F**.[[24]](https://www.ulike.com/products/sapphire-air-10-ipl-hair-removal) Those are manufacturer claims, not independent tissue-temperature measurements.

FDA K241998 is stronger for the UI20-family hardware envelope: OTC hair-removal indication, **550–1200 nm**, **0.88–3.20 ms** pulse width, multiple pulse modes, and a maximum accumulated fluence around **6.67 J/cm²** for listed configurations.[[25]](https://www.accessdata.fda.gov/cdrh_docs/pdf24/K241998.pdf)

The decisive missing values are:

- exact optical energy in each of the four sub-pulses;
- exact edge-to-edge gap inside one four-pulse burst;
- repetition/overlap delivered to the *same follicle* during real gliding;
- wavelength-resolved output and depth-dependent fluence;
- measured epidermal, shaft/bulb, and perifollicular temperature histories.

The simulator's Air 10 preset therefore encodes **one transparent interpretation** of the marketed 26 J / four-pulse / four-per-second description. It is not an asserted oscilloscope trace.

## 7. Revised simulator design

The model keeps its educational three-compartment heat flow:

1. **Epidermis:** a competing optical absorber with fast heat loss and optional surface cooling.
2. **Pigmented hair/follicle heater:** absorption rises with the hair slider; cooling time rises with diameter/coarseness.
3. **Deeper regenerative target:** heated only by diffusion from the pigmented compartment and cooled more slowly.
4. **Optional hair pulse-history state:** a cross-wavelength sensitivity layer that decays on the measured ~5 s low-temperature clock (or >60 s hot-exposure clock) and can increase later hair-pulse absorption. It is capped and switchable because no home-IPL study supplies a validated coefficient.

### 7.1 Cooling and response-memory equations

The important correction is that published follicle TRT is a **half-time**. The simulator converts it to the exponential constant before integrating:

\[
\tau_F=\frac{TRT_{50}}{\ln 2},\qquad
f_{residual}(\Delta t)=e^{-\Delta t/\tau_F}=2^{-\Delta t/TRT_{50}}
\]

The optional pulse-history sensitivity is intentionally separate from temperature. Between pulses its state `M` decays exponentially; after a pulse it is updated from the modeled amount by which peak hair temperature exceeded the 45 °C experimental onset:

\[
M(t+\Delta t)=M(t)e^{-\Delta t/\tau_M},\qquad
G_M=\min\left(2,1+0.0125M\right)
\]

The next hair-heating increment is multiplied by `G_M`. The **5 s** low-temperature decay clock and reported persistence beyond **60 s** after >70 °C come from Viera-Mármol et al.; treating 60 s as a hot-state exponential constant is a sensitivity approximation, not a fitted result. The **0.0125 per °C slope** is an illustrative interpolation and the **×2 cap** is a conservative calibration to the paper's approximately twofold low-fluence multi-pulse gain—not a measured IPL coefficient.[[9]](thermal_model_source_docs/PMC10107531_hair_temperature_avalanche_fulltext.xml)

| Model input | Value/range | Evidence class |
|---|---:|---|
| Baseline tissue temperature | 35 °C | Illustrative assumption |
| Follicle TRT half-time | 20–100 ms by hair slider; terminal-follicle evidence emphasized at 40–100 ms | Primary-source bracket plus illustrative fine-hair extension |
| Epidermal fast time constant | 8 ms; optional 45 ms coupling to a 22 °C surface sink | Illustrative lumped calibration informed by epidermal-TRT literature |
| Heater → deep-target / deep-target → baseline clocks | 120 / 500 ms | Illustrative lumped representation of slower diffusion; not measured Ulike/IPL values |
| Pulse-history decay | 5 s low-temperature; 60 s hot sensitivity scenario | Primary measured qualitative clocks, simplified as exponentials |
| Pulse-history gain slope/cap | 0.0125 per °C; maximum ×2 | Illustrative interpolation / calibration |
| Heating coefficients | Code constants `AF0`, `KE` | Calibration—not measured device/tissue conversion |
| Skin melanosome anchors | 2–40% across Fitzpatrick I–VI, logarithmically spaced | Primary-source optical-model anchors; approximate Fitzpatrick assignment, not individual measurement[[27]](thermal_model_source_docs/PMC10732256_skin_tone_melanosome_optical_model_fulltext.xml) |

The three thermal nodes are integrated at **0.25 ms**. Optical energy deposited into the epidermis and hair is followed by first-order cooling; the deep target is driven by the heater-to-target temperature difference and loses heat on its slower clock. This is not an energy-conserving finite-element bioheat model, which is why absolute temperature remains explicitly illustrative.

### 7.2 Skin-tone audit: how much light does the model divert from hair?

The old simulator used an undocumented six-value optical-depth array. The audit found that its overall shape was close to a newer reflectance-validated computational model, but the provenance and interpolation were missing. Else et al. assigned **six logarithmically spaced epidermal melanosome fractions from 2% to 40%** to approximate Fitzpatrick I–VI.[[27]](thermal_model_source_docs/PMC10732256_skin_tone_melanosome_optical_model_fulltext.xml) The revised simulator uses that log spacing, preserves its prior Fitzpatrick III calibration (`µ = 0.30`), and derives:

\[
\mu(s)=0.30\left(20^{1/5}\right)^{s-3},\qquad
A_{epi}=1-e^{-\mu},\qquad
T_{hair}=e^{-\mu}
\]

`A_epi` is the fraction assigned to epidermal absorption and `T_hair` is the complementary transmission proxy multiplying hair heating. This is deliberately a simple competition layer: it does not perform wavelength-resolved transport, account for back-scattering, or claim that every photon not absorbed in the epidermis reaches the follicle.

| Fitzpatrick anchor | Melanosome fraction used | Epidermal absorption proxy | Transmission/hair-heating proxy | Hair-heating factor vs III |
|---:|---:|---:|---:|---:|
| I | 2.0% | 8.7% | 91.3% | 123% |
| II | 3.6% | 15.2% | 84.8% | 114% |
| III | 6.6% | 25.9% | 74.1% | 100% |
| IV | 12.1% | 42.1% | 57.9% | 78% |
| V | 22.0% | 63.0% | 37.0% | 50% |
| VI | 40.0% | 83.6% | 16.4% | 22% |

The headline conclusion is therefore substantial but uncertain: **within this simplified model, moving from Fitzpatrick III to VI reduces the hair-heating coefficient by about 78%, while moving from III to IV reduces it about 22%.** That is a modeled optical-competition effect, not a clinical efficacy percentage. Fitzpatrick was designed around UV response and is too coarse/subjective to quantify individual epidermal melanin precisely; measured colorimetry or a device skin sensor is more defensible for real dosing.[[27]](thermal_model_source_docs/PMC10732256_skin_tone_melanosome_optical_model_fulltext.xml)

Half increments (for example III–IV at 3.5) are geometric interpolations on this continuous curve. They improve sensitivity exploration but do not create validated “Fitzpatrick 3.5” biology.

### 7.3 Cooling default

Contact cooling is now **off by default for every device and illustrative preset**. Turning it on applies a constant 22 °C sink through the model's cooling time constant. Because real window temperature and heat-extraction capacity can drift during a long session, the on/off control should be read as a bracket: **off = conservative late-session/no-effective-cooling scenario; on = sustained idealized cooling scenario**. The simulator still does not model device warm-up as a function of shot count or time.

It now reports:

- peak temperature for all three illustrative traces;
- **heater Ω**, **deep-target Ω**, and **epidermis Ω**;
- modeled transformation fraction **1 − e^−Ω**;
- time the deep-target proxy spends at or above 45 °C, labeled **SHR-zone exposure only**;
- residual heat before the next flash;
- pulse-history gain separately from residual temperature;
- time after the last flash for the heater and deep target to return to within 1 °C of the 35 °C model baseline;
- same-total single-vs-split comparison;
- a short comfort note that explicitly states the simulator does not model or predict pain.

The built-in `SANITY()` sweep now covers 2,592 parameter combinations and 19 invariants, including finite/nonnegative Ω, monotonic Arrhenius dwell time, energy-split identity, pulse stacking, integer and half-step melanin competition, cooling direction, the 65 °C ≈ 67.5 ms reference, exact TRT-half-time conversion, nonnegative pulse-history influence, and capture of near-baseline recovery. Append `?selftest=1` to the simulator URL to run it and expose the result in `data-model-sanity` on the root HTML element.

## 8. How to use it without overreading it

1. Start with the **temperature × time** slider. Compare 60, 65, and 70 °C to see why peak alone is misleading.
2. Load a device. Green spec tags are disclosed in FDA or primary device material; the inter-pulse gap remains an explicit unknown.
3. Compare one flash with the same total split across several pulses. Read both **peak** and **Ω**.
4. Shorten the gap. Peak carryover should rise as the gap moves inside the follicle-TRT range.
5. Toggle **pulse-history sensitivity** off and on. The difference is the current best evidence-based bracket between a residual-heat-only calculation and a laser-measured hair-memory scenario; it is not an IPL confidence interval.
6. Move skin tone in 0.5 steps and read the displayed melanosome anchor, epidermal-absorption proxy, and relative hair-heating factor. Treat half steps as interpolation only.
7. Turn cooling on only when exploring sustained effective cooling; the default-off trace is the conservative late-session bracket.
8. If the heater Ω crosses 1 but the deep-target Ω does not, read the result as **heater/lining injury without demonstrated durable-target injury**.
9. If the curve enters 45–50 °C but Ω stays low, read it as **SHR-like exposure**, not a kill.
10. Never use a “below” epidermis score as a safety clearance. The optical coefficients, skin state, placement, overlap, and actual cooling are not known.

## Evidence gaps

- No peer-reviewed paper validates the selected Arrhenius A/E pair specifically for human bulge stem cells, hair germ, matrix, or dermal papilla during IPL.
- The 2011 parameter pair was adopted from generic tissue/protein-denaturation modeling; using it for all three simulator compartments is a transparent simplification.
- The temperature curves remain lumped and calibrated, not Monte Carlo light transport plus finite-element bioheat transfer.
- The Fitzpatrick slider now has published-model melanosome anchors, but Fitzpatrick class remains a subjective UV-response category rather than a direct individual melanin measurement. Half steps are interpolations.
- The broad IPL spectrum is collapsed into one effective absorption coefficient; wavelength-dependent penetration is not modeled.
- No study directly compares fixed-spot two-to-four-pulse home modes with a matched-total single flash while measuring follicle temperature and long-term hair outcome.
- Ulike's exact intra-burst timing and per-sub-pulse energy remain unpublished in the sources reviewed.
- Professional SHR outcome studies do not establish that home SHR uses the same thermal mechanism or per-follicle dose.
- The 2023 pulse-history experiment used isolated hair and alexandrite/Nd:YAG lasers. Its ~5 s and >60 s response lifetimes do not establish the magnitude of the effect for broadband home IPL in living skin.
- Cooling is binary and time-invariant. The model does not predict how quickly a particular sapphire window warms or how much effective cooling remains after repeated shots.

## Sources

1. Ataie-Fashtami L, et al. *Simulation of Heat Distribution and Thermal Damage Patterns of Diode Hair-Removal Lasers.* Photomed Laser Surg. 2011;29:509-515. https://journals.sagepub.com/doi/10.1089/pho.2010.2895 — 810 nm LITCIT model; Arrhenius equation, A/E pair, Ω≥1 criterion, and long-pulse findings.
2. Fiskerstrand EJ, Svaasand LO, Nelson JS. *Hair removal with long pulsed diode lasers: a comparison between two systems with different pulse structures.* Lasers Surg Med. 2003;32:399-404. https://pubmed.ncbi.nlm.nih.gov/12766964/ — 29-patient comparison plus heat-diffusion model using 65 °C damage convention.
3. Omi T. *Static and dynamic modes of 810 nm diode laser hair removal compared: a clinical and histological study.* Laser Ther. 2017;26:31-37. https://pmc.ncbi.nlm.nih.gov/articles/PMC5515709/ — matched clinical outcome and apoptosis-oriented histology.
4. Arsiwala SZ, Majid IM. *Methods to overcome poor responses and challenges of laser hair removal in dark skin.* IJDVL. 2019;85:3-9. https://ijdvl.com/methods-to-overcome-poor-responses-and-challenges-of-laser-hair-removal-in-dark-skin/ — review source for progressive-photothermolysis 45–50 °C description.
5. McCoy S, Evans A, James C. *Histological study of hair follicles treated with a 3-msec pulsed ruby laser.* Lasers Surg Med. 1999;24:142-150. https://pubmed.ncbi.nlm.nih.gov/10100652/ — no evidence of permanent follicle death after one treatment.
6. Denton ML, et al. *Effect of ambient temperature and intracellular pigmentation on photothermal damage rate kinetics.* J Biomed Opt. 2019;24:065002. https://pmc.ncbi.nlm.nih.gov/articles/PMC6977020/ — empirical transient photothermal Arrhenius analysis and limitations; [local full text](thermal_model_source_docs/PMC6977020_photothermal_damage_rate_kinetics_fulltext.xml).
7. Ye H, De S. *Thermal injury of skin and subcutaneous tissues: a review of experimental approaches and numerical models.* Burns. 2017;43:909-932. https://pmc.ncbi.nlm.nih.gov/articles/PMC5459687/ — tissue-specific Arrhenius parameters and limitations of burn modeling.
8. Topping A, et al. *The temperatures reached and the damage caused to hair follicles by the normal-mode ruby laser when used for depilation.* Ann Plast Surg. 2000;44:581-590. https://pubmed.ncbi.nlm.nih.gov/10884072/ — ex vivo human thermal imaging and histology.
9. Viera-Mármol G, et al. *Measurements of hair temperature avalanche effect with alexandrite and Nd:YAG hair removal lasers.* Lasers Surg Med. 2023;55:89-98. https://pmc.ncbi.nlm.nih.gov/articles/PMC10107531/ — direct hair photothermal measurement; [local full text](thermal_model_source_docs/PMC10107531_hair_temperature_avalanche_fulltext.xml).
10. Grossman MC, et al. *Permanent hair removal by normal-mode ruby laser.* Arch Dermatol. 1996;132:1299-1302. https://jamanetwork.com/journals/jamadermatology/fullarticle/189173 — clinical/histologic permanent-loss observations with mechanism uncertainty.
11. Goldberg DJ, Silapunt S. *Histologic evaluation of a millisecond Nd:YAG laser for hair removal.* Lasers Surg Med. 2001;28:159-161. https://pubmed.ncbi.nlm.nih.gov/11241524/ — selective acute follicular thermal injury.
12. Kato T, et al. *Histological Changes Elicited by Hair Removal Lasers.* J Nippon Med Sch. 2002;69:564-570. https://doi.org/10.1272/jnms.69.564 — immediate and one-month histology; [local open-access PDF](thermal_model_source_docs/Kato_2002_histological_changes_hair_removal_lasers.pdf).
13. Kono T, et al. *Theoretical review of the treatment of pigmented lesions in Asian skin.* Laser Ther. 2016;25:179-184. https://pmc.ncbi.nlm.nih.gov/articles/PMC5108992/ — basal-layer TRT estimate.
14. Gade A, et al. *Intense Pulsed Light (IPL) Therapy.* StatPearls. Updated 2024. https://www.ncbi.nlm.nih.gov/books/NBK580525/ — sequential-pulse delay and IPL overview.
15. Byalakere Shivanna C, et al. *Comparison of submillisecond pulse and long-pulse 1064 nm Nd:YAG laser hair removal.* J Cosmet Dermatol. 2022;21:3393-3397. https://pmc.ncbi.nlm.nih.gov/articles/PMC9541334/ — hair-shaft TRT range.
16. Goel A, Rai K. *Methods to Overcome Poor Response and Challenges of Facial Laser Hair Reduction.* J Clin Aesthet Dermatol. 2022;15:38-41. https://pmc.ncbi.nlm.nih.gov/articles/PMC9239120/ — terminal-follicle TRT and poor-response considerations.
17. Rogachefsky AS, et al. *Evaluation of a new super-long-pulsed 810 nm diode laser for the removal of unwanted hair: the concept of thermal damage time.* Dermatol Surg. 2002;28:410-414. https://pubmed.ncbi.nlm.nih.gov/12030874/ — TDT 170–1000 ms and best result in the tested 400 ms condition.
18. Altshuler GB, et al. *Extended theory of selective photothermolysis.* Lasers Surg Med. 2001;29:416-432. https://pubmed.ncbi.nlm.nih.gov/11891730/ — absorber/target separation and TDT framework.
19. Braun M. *Comparison of high-fluence, single-pass diode laser to low-fluence, multiple-pass diode laser for hair reduction.* J Drugs Dermatol. 2009. https://pubmed.ncbi.nlm.nih.gov/19916262/ — professional high-repetition outcome and pain comparison.
20. Koo B, et al. *A comparison of two 810 diode lasers for hair removal: low fluence, multiple pass versus high fluence, single pass.* Lasers Surg Med. 2014. https://pubmed.ncbi.nlm.nih.gov/24752608/
21. Li W, et al. *A prospective randomized controlled clinical trial to compare SHR mode and HR mode of 810 nm diode laser.* J Cosmet Laser Ther. 2016. https://pubmed.ncbi.nlm.nih.gov/27419804/
22. Wanitphakdeedecha R, et al. *A prospective randomized study comparing diode SHR with long-pulsed Nd:YAG.* J Eur Acad Dermatol Venereol. 2012. https://pubmed.ncbi.nlm.nih.gov/21923659/
23. Barolet D. *Low fluence-high repetition rate diode laser hair removal 12-month evaluation.* Lasers Surg Med. 2012. https://pubmed.ncbi.nlm.nih.gov/22437967/
24. Ulike Air 10 official product page. https://www.ulike.com/products/sapphire-air-10-ipl-hair-removal — current manufacturer claims for 26 J/four-pulse SHR burst, four flashes/s, dual lights, and 65 °F contact cooling; accessed 2026-07-10.
25. FDA K241998, Shenzhen Ulike Smart Electronics UI20-family Ice Cooling IPL Hair Removal Device. https://www.accessdata.fda.gov/cdrh_docs/pdf24/K241998.pdf — primary regulatory source for indication, wavelength, fluence, spot size, pulse width, and pulse modes.
26. Ash C, et al. *Mathematical modeling of the optimum pulse structure for safe and effective photo epilation using broadband pulsed light.* J Appl Clin Med Phys. 2012;13:290-299. https://pmc.ncbi.nlm.nih.gov/articles/PMC5718238/ — IPL-specific Monte Carlo/heat-diffusion model; TRT as 50% heat loss, 40–100 ms follicle half-time, and close-versus-spaced pulse stacking; [local full text](thermal_model_source_docs/PMC5718238_broadband_IPL_pulse_structure_model_fulltext.xml).
27. Else TR, et al. *Effects of skin tone on photoacoustic imaging and oximetry.* J Biomed Opt. 2024;29(S1):S11506. https://pmc.ncbi.nlm.nih.gov/articles/PMC10732256/ — reflectance-validated computational skin model using six logarithmically spaced melanosome fractions from 2% to 40% assigned to approximate Fitzpatrick I–VI; supports the continuous sensitivity curve, not individual IPL dosing; [local full text](thermal_model_source_docs/PMC10732256_skin_tone_melanosome_optical_model_fulltext.xml).

Local source manifest: [thermal_model_source_docs/README.md](thermal_model_source_docs/README.md).
