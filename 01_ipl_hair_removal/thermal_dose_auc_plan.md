# Thermal Dose / Area-Under-Curve Plan — IPL Simulator

**Date:** 2026-07-10
**Status:** Research + design plan (no code yet)
**Context:** The simulator already integrates the Arrhenius damage integral (Ω) over the full temperature trace. This plan defines how to make the time–temperature tradeoff more visible and educational: isoeffect curves, an "equivalent constant temperature" readout, and a side-by-side comparison mode that shows a short-hot pulse producing the same Ω as a longer-cooler exposure.

---

## 1. What's already in the simulator

The current model (`shr_thermal_simulator.html`, lines 472–540) already does the right physics:

- **Arrhenius rate:** `arrheniusRate(T) = A · exp(−Eₐ / RT)` with A = 3.1×10⁹⁸ s⁻¹, Eₐ = 6.3×10⁵ J/mol (from Ataie-Fashtami et al. 2011, a published diode hair-removal simulation).
- **Cumulative Ω:** `omegaF`, `omegaBg`, `omegaE` are integrated at every 0.25 ms timestep over the entire temperature trace — this already IS "area under the curve," just not a simple °C·s rectangle but the exponentially weighted Arrhenius integral.
- **Ω=1 criterion:** treated as a model endpoint (~63% denaturation in a first-order rate model).
- **Reference table:** already shows that Ω=1 at constant temperature requires ~1.95 s at 60 °C, ~68 ms at 65 °C, ~2.6 ms at 70 °C.
- **Why not CEM43:** explained in the UI — CEM43 was built for minute-scale hyperthermia; photothermal kinetics research uses Arrhenius for sub-second laser heating.

**What's missing:** The user can't *see* the tradeoff. The Ω number is abstract. There's no way to compare two exposures and say "these are equivalent damage." The concept of "area under the curve" needs to be made tangible.

---

## 2. The core formula and why it works

### 2.1 The Arrhenius damage integral

\[
\Omega(\tau) = \int_0^\tau A \cdot e^{-E_a / (R \cdot T(t))} \, dt
\]

| Symbol | Meaning | Value used | Units |
|--------|---------|------------|-------|
| Ω | Dimensionless damage integral | Ω≥1 ≈ irreversible injury threshold | — |
| A | Frequency factor (collision attempts per second) | 3.1×10⁹⁸ | s⁻¹ |
| Eₐ | Activation energy for protein denaturation | 6.3×10⁵ | J/mol |
| R | Universal gas constant | 8.314 | J/(mol·K) |
| T(t) | Absolute temperature as function of time | from simulation | K |
| τ | Total exposure duration | from simulation | s |

### 2.2 Why this captures "area under the curve"

The Arrhenius rate r(T) = A·exp(−Eₐ/RT) is an *exponential function of temperature*. At 35 °C (baseline body temp), r(35) ≈ 3×10⁻¹¹ s⁻¹ — negligible. At 65 °C, r(65) ≈ 14.7 s⁻¹ — Ω=1 in ~68 ms. At 70 °C, r(70) ≈ 387 s⁻¹ — Ω=1 in ~2.6 ms.

The integral accumulates these rate contributions over time. This means:

- **A brief spike to 80 °C** contributes an enormous instantaneous rate but for very few milliseconds.
- **A long plateau at 55 °C** contributes a tiny rate but for hundreds of milliseconds.
- **They can produce the same Ω.** That's the key insight.

### 2.3 Time–temperature equivalence (isoeffect)

For constant temperature T, the time to reach Ω=1 is:

\[
t_{\Omega=1}(T) = \frac{1}{A \cdot e^{-E_a / (RT)}}
\]

At the model's parameters:

| Temperature (°C) | Time to Ω=1 | Time to Ω=0.1 |
|---|---|---|
| 50 | ~8.3 minutes | ~50 seconds |
| 55 | ~22 seconds | ~2.2 seconds |
| 60 | ~1.95 seconds | ~195 ms |
| 65 | ~68 ms | ~6.8 ms |
| 70 | ~2.6 ms | ~0.26 ms |
| 75 | ~0.11 ms | ~0.011 ms |
| 80 | ~5 µs | ~0.5 µs |

This table IS the time–temperature equivalence. Every row is an "isoeffect pair." The simulator already has the maths; the user just can't see this curve.

### 2.4 The rule-of-thumb shortcut

Above ~55 °C, the Arrhenius rate approximately doubles for every ~0.5 °C increase (at these Eₐ values). Or equivalently: **time-to-damage halves for every ~0.5 °C rise.** That's why 68 ms at 65 °C ≈ 2.6 ms at 70 °C — a 5 °C difference → roughly 2¹⁰ ≈ 26× shorter time.

---

## 3. Research gathered: what the literature says

### 3.1 The Arrhenius model is the standard for short-pulse laser damage

| Source | Key finding |
|--------|-------------|
| **Ataie-Fashtami et al. (2011)** — *Photomed Laser Surg* | Used A=3.1×10⁹⁸, Eₐ=6.3×10⁵ for 810 nm diode hair removal simulation. Ω≥1 = irreversible injury criterion. This is the parameter pair already in the simulator. |
| **Ahmed, Noojin & Denton (2022)** — *J Biomed Opt* 27(3), 035001 | Derived nonisothermal correction for the damage integral. For short (<1 s) laser exposures, the isothermal Arrhenius plot overestimates damage; correction factor δc ranges from −0.93 (0.05 s) to 0.0 (20 s steady-state). The frequency factor A must be adjusted for the temperature ramp shape. |
| **Denton et al. (2019)** — *J Biomed Opt* | Empirical Arrhenius kinetics for photothermal damage; explicitly states CEM43 is "most useful for long-duration hyperthermia" and is NOT appropriate for sub-second laser heating. |
| **Henriques & Moritz (1947)** — *Arch Pathol* | Original skin burn integral. Two parameter regimes: 44–50 °C (P=2.185×10¹²⁴, ΔE/R=93,535 K) and ≥50 °C (P=1.823×10⁵¹, ΔE/R=39,110 K). Ω≥0.53 = first-degree, Ω≥1.0 = second-degree at basal layer. |
| **Pearce (2013)** — *Int J Hyperthermia* | Comprehensive review of Arrhenius parameters across tissue types. Documents the ln(A) vs. Eₐ compensation law: ln(A) = 3.832×10⁻⁴·Eₐ − 10.042. This means A and Eₐ are NOT independent — you can't pick them separately. |
| **Okebiorun & Elgohary (2020)** — *J Phys Conf Ser* | Monte Carlo + bioheat + Arrhenius model for 3 skin types with 694/755/1064 nm. Found 10–15 J/cm² at 755 nm optimal for light/moderate skin. |
| **Fiskerstrand, Svaasand & Nelson (2003)** — *Lasers Surg Med* | Clinical + modeling comparison of single vs. split diode pulses. Used 65 °C as follicular damage threshold. Found similar hair reduction from one 30 ms pulse vs. two 45 ms pulses separated by 40 ms — which makes sense under Arrhenius: the split pulses accumulate similar total Ω despite lower individual peaks. |
| **Rogachefsky et al. (2002)** — *Dermatol Surg* | Defined Thermal Damage Time (TDT) as 170–1000 ms, optimal ~400 ms for 810 nm diode. TDT is a *diffusion* timescale, not a damage threshold — it describes how long heat takes to spread from absorber to stem cells. |

### 3.2 Why CEM43 is the wrong tool here

CEM43 (Cumulative Equivalent Minutes at 43 °C) uses a simpler model:

\[
\text{CEM43} = \sum t_i \cdot R^{(43 - T_i)}
\]

where R ≈ 2 for T ≥ 43 °C, R ≈ 4 for T < 43 °C.

This works for **minute-scale hyperthermia** (oncology, 39–45 °C). It breaks down for sub-second laser pulses because:
- The R=2 rule was fitted to cell-survival curves at 43–57 °C over minutes, not milliseconds.
- At laser-peak temperatures (60–100 °C), the damage kinetics are dominated by protein denaturation with a much steeper temperature dependence (the Arrhenius Eₐ of ~6×10⁵ J/mol gives a much larger rate change per degree than R=2).
- Denton et al. (2019) explicitly state CEM43 is for "long-duration hyperthermia."

The simulator already notes this (line 154). No change needed.

---

## 4. What to add to the simulator (the plan)

### 4.1 Isoeffect curve chart *(new card, high priority)*

**What:** A small static or interactive chart showing `time to Ω=1` vs. `temperature` on log-linear axes.

**Why:** This single chart makes the time–temperature tradeoff instantly visible. The user sees the steep curve: at 60 °C it takes seconds; at 70 °C it takes milliseconds; at 50 °C it takes minutes. They can read off any pair.

**Implementation:**
- SVG or Canvas, ~300×200 px.
- X-axis: temperature 45–80 °C (linear).
- Y-axis: time to Ω=1 (log scale, seconds to microseconds).
- Mark the model's current follicle peak temperature on the curve.
- Optionally show the Ω=0.1 and Ω=10 curves as dashed lines.
- Label the three regimes: "hyperthermia zone" (45–55 °C, minutes), "thermal damage time zone" (55–70 °C, ms–s, relevant to hair removal), "vaporization zone" (>100 °C, µs, outside the model).

### 4.2 Equivalent constant-temperature readout *(new gauge, high priority)*

**What:** Convert the integrated Ω back into an intuitive number: "This exposure delivers the same Ω as holding the follicle at **XX.X °C for 100 ms**."

**Why:** Ω = 0.047 means nothing to most users. But "equivalent to 61.3 °C for 100 ms" is concrete.

**How:** Given the integrated Ω from the simulation, solve for T_eq such that:

\[
t_{\text{ref}} \cdot A \cdot e^{-E_a / (R \cdot T_{eq})} = \Omega
\]

\[
T_{eq} = \frac{E_a}{R \cdot \ln(A \cdot t_{\text{ref}} / \Omega)} - 273.15
\]

Pick t_ref = 100 ms (a round number in the middle of typical pulse durations). If T_eq comes out < 45 °C, show "<45 °C" (below meaningful damage). If > 100 °C, cap at ">100 °C" (vaporization, outside model validity).

**Display:** "Equivalent to **XX °C** held for 100 ms" — a single number with context.

### 4.3 Dose composition bar *(new gauge, medium priority)*

**What:** A stacked horizontal bar showing what fraction of the total Ω came from different temperature bands.

**Why:** Shows that a short spike can dominate the dose even if it's brief, OR that a long warm tail can accumulate significant dose even without a high peak.

**How:** During simulation, accumulate Ω in four bins:
- **<50 °C** — sub-threshold (negligible contribution)
- **50–60 °C** — slow accumulation zone
- **60–70 °C** — coagulation zone
- **>70 °C** — rapid-denaturation zone

Display as a stacked bar colored from cool (blue) to hot (red). Width proportional to Ω contribution. This makes it obvious whether the dose comes from "tall and brief" or "moderate and sustained."

### 4.4 Side-by-side comparison mode *(new feature, medium priority)*

**What:** Let the user lock the current simulation as "Scenario A," change parameters, and see "Scenario B" overlaid with matching Ω.

**Why:** The user's exact question — "very high for very short can damage, but also not as high for much longer can damage just as well" — is best demonstrated by comparing two scenarios that produce the same Ω via different paths.

**How:**
- "Lock current as A" button.
- Change parameters → live "B" simulation.
- Show side-by-side gauges: peak temp, Ω, equivalent constant temp.
- When Ω_A ≈ Ω_B (within 10%), highlight in green: "These two exposures are approximately equivalent in modeled damage despite different peak temperatures."
- Pre-load two built-in comparison presets (e.g., "Single 65 °C spike vs. sustained 55 °C soak").

### 4.5 Assumptions panel *(new card, high priority — educational)*

**What:** An explicit, user-facing list of every assumption in the dose model.

**Why:** The user asked for "all the assumptions defined." Currently they're scattered in comments and footnotes. They should be collected in one place the user can read.

**Content:**

| # | Assumption | Why it matters | How to challenge it |
|---|---|---|---|
| 1 | **One Arrhenius parameter pair for all compartments.** A=3.1×10⁹⁸, Eₐ=6.3×10⁵ J/mol from Ataie-Fashtami 2011. | Follicle stem cells, dermal collagen, and epidermal keratinocytes likely have different denaturation kinetics. The same Ω means different things in different tissues. | Tissue-specific parameters exist (Pearce 2013 compiles many) but none are validated for human follicle stem cells specifically. |
| 2 | **Ω=1 is ~63% denaturation in a first-order rate model.** | Real tissue injury is not a single first-order reaction. Multiple proteins denature at different rates; apoptosis is activated at lower temperatures via different pathways. | Could use Ω=0.1 (onset) and Ω=10 (near-complete) as a band rather than a single threshold. |
| 3 | **The Arrhenius model assumes a single activation energy.** | Real protein denaturation has temperature-dependent Eₐ. Henriques & Moritz used TWO parameter regimes (above/below 50 °C). The single-pair model is a simplification. | Could implement the two-regime Henriques model for epidermis and compare. |
| 4 | **The temperature nodes are lumped averages, not spatial profiles.** | Real tissue has temperature gradients. The follicle stem cells (bulge) are at a specific depth and receive heat by diffusion, not direct absorption. A lumped node smooths this. | A spatially-resolved model would need geometry (follicle depth, diameter, blood perfusion) that home IPL filings don't disclose. |
| 5 | **Nonisothermal correction is NOT applied.** | Ahmed et al. (2022) showed that for sub-second heating ramps, the isothermal Arrhenius integral overestimates damage because A must be adjusted downward. The current model uses the raw isothermal A. | Could apply δc(τ) correction factor, but it was derived for RPE cells at 2 µm, not hair follicles at 560–1200 nm. |
| 6 | **No apoptotic or non-thermal pathway.** | Omi et al. (2017) and others show IPL can trigger apoptosis (programmed cell death) at temperatures below the coagulation threshold. The Arrhenius model only captures thermal coagulation. | The "SHR zone" (45–50 °C) exposure time is tracked separately but not converted to a damage prediction. This is deliberate. |
| 7 | **Ω is a model criterion, not a clinical prediction.** | The literature does not contain a validated Ω-to-hair-reduction curve. Ω=1 is a modeling convention that says "the model predicts damage at this level" — not "this setting removes hair." | Real clinical efficacy depends on session count, anatomical site, hair cycle phase, and individual variation. |
| 8 | **The vaporization ceiling (100 °C) clamps the integral.** | Above ~100 °C, water boils, tissue properties change abruptly, and the linear heat model is invalid. The model caps all nodes at 100 °C. This means Ω for very high fluences is *underestimated* — real tissue would experience steam bubbles and explosive vaporization, not just more denaturation. | Keep the cap but note it when peak Tf hits 100 °C. |

### 4.6 Ω-band shading on the temperature chart *(low priority, visual enhancement)*

**What:** On the existing temperature-over-time chart, shade the background to show how much each millisecond at each temperature contributes to Ω.

**Why:** Makes the "area under the curve" literally visible — the user sees that the area above 60 °C is heavily weighted.

**How:** Light colored bands behind the temperature traces:
- Green: <50 °C (negligible Ω contribution)
- Yellow: 50–60 °C (slow accumulation, minutes to Ω=1)
- Orange: 60–70 °C (fast, ms to seconds)
- Red: >70 °C (nearly instantaneous, µs to ms)

---

## 5. Implementation order (recommended)

1. **Assumptions panel (#4.5)** — simplest, pure HTML/text, highest educational value. Write the assumptions explicitly.
2. **Equivalent constant-temperature readout (#4.2)** — a single gauge, one formula, one new `<div>` in the gauges grid. Big impact for small code.
3. **Isoeffect curve chart (#4.1)** — a static SVG, pre-computed from the Arrhenius formula. No simulation needed. Can be drawn once.
4. **Dose composition bar (#4.3)** — requires binning Ω during the simulation loop (adds ~4 accumulators).
5. **Ω-band shading on chart (#4.6)** — visual polish on the existing D3/SVG chart.
6. **Side-by-side comparison (#4.4)** — most complex, requires state management for locked scenario.

Items 1–3 together would transform the educational value of the tool for ~150 lines of code.

---

## 6. Specific answers to the user's questions

> "how the area under the curve of the follicle temp may be more important"

**It already is.** The simulator already integrates Ω over the full curve and uses that for its verdict, not peak temperature alone. The verdict logic (line 605–616) checks `omegaBg >= OMEGA_CRIT`, not `peakTf >= 65`.

The problem is that this isn't *visible*. The user sees a temperature trace with a 65 °C reference line and a peak temperature gauge — the visual language says "peak matters." The Ω gauge is present but abstract.

> "very high for very short can damage.. but also not as high for much longer can damage just as well"

**Yes, and the Arrhenius integral formalizes exactly this.** The isoeffect curve (section 4.1) will make it explicit. The comparison mode (section 4.4) will let the user prove it to themselves by dialing in two different parameter sets that produce the same Ω.

Concrete example using the model's parameters:
- **Scenario A:** Single 6.3 J/cm², 12 ms pulse, dark hair → follicle peaks at ~69 °C for a few ms, then cools. Ω ≈ some value.
- **Scenario B:** Multiple 1.7 J/cm² sub-flashes at 250 ms gaps → follicle never exceeds ~48 °C but spends seconds above 45 °C. Ω is computed over the full trace.

The user can compare and see whether B's area-under-curve catches up to A's spike.

> "i think theres a formula to be had here"

**There is, and it's already implemented: the Arrhenius damage integral.** The formula is:

\[
\Omega = \int_0^\tau 3.1 \times 10^{98} \cdot e^{-6.3 \times 10^5 / (8.314 \cdot T(t))} \, dt
\]

What's missing is the *inverse*: given an Ω value, what constant temperature for 100 ms would produce it? That's the "equivalent constant temperature" readout (section 4.2).

---

## 7. Open questions for the user

1. **Should the assumptions panel replace or supplement the existing "Temperature reality-check" card?** Currently that card (lines 138–154 in the HTML) covers some assumptions. The new panel would be more exhaustive.

2. **Do you want the isoeffect curve to be interactive?** (Slider that moves a point along the curve, showing "at XX °C, Ω=1 in YY ms") Or static?

3. **For the comparison mode, should the two scenarios share the same chart?** Overlaid traces with different colors? Side-by-side charts? Both have space constraints on mobile.

4. **Should the "equivalent constant temperature" use 100 ms as the reference time, or should the user be able to change it?** 100 ms is a natural choice (typical pulse duration, middle of the TDT range). But letting the user pick "show me equivalent to 30 ms" or "equivalent to 400 ms" would be more flexible.

5. **Do you want the nonisothermal correction (Ahmed 2022) applied as an option?** This would add a toggle "Apply nonisothermal correction" that adjusts A downward for short pulses. It's more physically correct but adds complexity and was derived for a different tissue type.

---

## Sources

1. Ataie-Fashtami L, et al. Simulation of diode hair-removal thermal damage. *Photomed Laser Surg* 2011. [DOI: 10.1089/pho.2010.2895](https://journals.sagepub.com/doi/10.1089/pho.2010.2895)
2. Ahmed EM, Noojin GD, Denton ML. Damage integral and other predictive formulas for nonisothermal heating during laser exposure. *J Biomed Opt* 2022;27(3):035001. [DOI: 10.1117/1.JBO.27.3.035001](https://doi.org/10.1117/1.JBO.27.3.035001)
3. Denton ML, et al. Effect of ambient temperature and intracellular pigmentation on photothermal damage rate kinetics. *J Biomed Opt* 2019. [PMCID: PMC6977020](https://pmc.ncbi.nlm.nih.gov/articles/PMC6977020/)
4. Henriques FC, Moritz AR. Studies of thermal injury I–V. *Arch Pathol* 1947.
5. Pearce JA. Comparative analysis of mathematical models of cell death and thermal damage. *Int J Hyperthermia* 2013. [DOI: 10.3109/02656736.2013.786140](https://pubmed.ncbi.nlm.nih.gov/22486200/)
6. Okebiorun JO, Elgohary MA. Optothermal response and tissue damage analysis during laser hair removal. *J Phys: Conf Ser* 2020;1472:012003. [DOI: 10.1088/1742-6596/1472/1/012003](https://iopscience.iop.org/article/10.1088/1742-6596/1472/1/012003)
7. Fiskerstrand EJ, Svaasand LO, Nelson JS. Hair removal with long-pulsed diode lasers: comparison of two pulse structures. *Lasers Surg Med* 2003. [PMID: 12766964](https://pubmed.ncbi.nlm.nih.gov/12766964/)
8. Rogachefsky AS, et al. Super-long-pulsed 810 nm diode & the concept of thermal damage time. *Dermatol Surg* 2002. [PMID: 12030874](https://pubmed.ncbi.nlm.nih.gov/12030874/)
9. Sapareto SA, Dewey WC. Thermal dose determination in cancer therapy. *Int J Radiat Oncol Biol Phys* 1984. [DOI: 10.1016/0360-3016(84)90379-1](https://pubmed.ncbi.nlm.nih.gov/6373667/)
10. Dewey WC. Arrhenius relationships from the molecule and cell to the clinic. *Int J Hyperthermia* 2009. [DOI: 10.1080/02656730902807319](https://pubmed.ncbi.nlm.nih.gov/19219695/)
