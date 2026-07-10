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

A newer bench study measured human-hair photothermal responses to alexandrite and Nd:YAG hair-removal lasers and found nonlinear changes over repeated low-fluence pulses as hair structure and water content changed. That makes a fixed linear “J/cm² → °C” conversion even less defensible across a pulse train.[[9]](thermal_model_source_docs/PMC10107531_hair_temperature_avalanche_fulltext.xml)

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
| Hair shaft/follicle thermal relaxation | roughly 10–100 ms | A pulse arriving inside this range can raise the next heater peak; the exact value changes with diameter.[[15]](https://pmc.ncbi.nlm.nih.gov/articles/PMC9541334/)[[16]](https://pmc.ncbi.nlm.nih.gov/articles/PMC9239120/) |
| Thermal Damage Time (extended target) | reported 170–1000 ms; one best clinical result at 400 ms | A diffusion timescale for transferring heat from absorber to a larger vulnerable target—not “hold any temperature for 400 ms and it dies.”[[17]](https://pubmed.ncbi.nlm.nih.gov/12030874/)[[18]](https://jcasonline.com/thermal-kinetic-selectivity-and-lasers/) |
| Arrhenius Ω | depends on the entire temperature trace | The injury model. TDT affects the trace; it does not replace the damage equation. |

This distinction matters for a four-pulse home burst. A 250 ms gap is longer than the nominal TRT of many follicles, so the **heater peak** may mostly reset. A slower deep-tissue tail can remain, but its existence does not prove Ω reached a damaging endpoint.

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

It now reports:

- peak temperature for all three illustrative traces;
- **heater Ω**, **deep-target Ω**, and **epidermis Ω**;
- modeled transformation fraction **1 − e^−Ω**;
- time the deep-target proxy spends at or above 45 °C, labeled **SHR-zone exposure only**;
- residual heat before the next flash;
- same-total single-vs-split comparison;
- a separate unitless pain-summation cue.

The built-in `SANITY()` sweep now covers 1,944 parameter combinations and 15 invariants, including finite/nonnegative Ω, monotonic Arrhenius dwell time, energy-split identity, pulse stacking, melanin competition, cooling direction, and the 65 °C ≈ 67.5 ms reference. Append `?selftest=1` to the simulator URL to run it and expose the result in `data-model-sanity` on the root HTML element.

## 8. How to use it without overreading it

1. Start with the **temperature × time** slider. Compare 60, 65, and 70 °C to see why peak alone is misleading.
2. Load a device. Green spec tags are disclosed in FDA or primary device material; the inter-pulse gap remains an explicit unknown.
3. Compare one flash with the same total split across several pulses. Read both **peak** and **Ω**.
4. Shorten the gap. Peak carryover should rise as the gap moves inside the follicle-TRT range.
5. If the heater Ω crosses 1 but the deep-target Ω does not, read the result as **heater/lining injury without demonstrated durable-target injury**.
6. If the curve enters 45–50 °C but Ω stays low, read it as **SHR-like exposure**, not a kill.
7. Never use a “below” epidermis score as a safety clearance. The optical coefficients, skin state, placement, overlap, and actual cooling are not known.

## Evidence gaps

- No peer-reviewed paper validates the selected Arrhenius A/E pair specifically for human bulge stem cells, hair germ, matrix, or dermal papilla during IPL.
- The 2011 parameter pair was adopted from generic tissue/protein-denaturation modeling; using it for all three simulator compartments is a transparent simplification.
- The temperature curves remain lumped and calibrated, not Monte Carlo light transport plus finite-element bioheat transfer.
- The Fitzpatrick slider is a qualitative melanin-competition sensitivity test, not a measured mapping from Fitzpatrick type to epidermal optical depth.
- The broad IPL spectrum is collapsed into one effective absorption coefficient; wavelength-dependent penetration is not modeled.
- No study directly compares fixed-spot two-to-four-pulse home modes with a matched-total single flash while measuring follicle temperature and long-term hair outcome.
- Ulike's exact intra-burst timing and per-sub-pulse energy remain unpublished in the sources reviewed.
- Professional SHR outcome studies do not establish that home SHR uses the same thermal mechanism or per-follicle dose.

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

Local source manifest: [thermal_model_source_docs/README.md](thermal_model_source_docs/README.md).
