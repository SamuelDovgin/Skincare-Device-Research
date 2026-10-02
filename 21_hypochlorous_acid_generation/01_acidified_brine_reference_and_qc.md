# Scaled Acidified-Brine Recipe, Time Curves, and QC

*Updated 2026-08-27. This is a device-specific preparation and measurement guide, not a medical, cosmetic, disinfection, or product-certification claim.*

## 0. Bottom line

The planner's default working recipe is now the user's Amazon/Chloe-observed batch, scaled from **250 mL for 15 minutes at approximately 300 ppm FAC and pH 4.5**:

- **250 mL purified or distilled water**;
- **1.50 g non-iodized table salt**; and
- **0.625 mL vinegar**, with acidity unspecified in the review.

The displayed amount and time scale from that observation: **more than 250 mL takes proportionally longer, and less than 250 mL takes proportionally less**. The working rate is approximately **20 ppm/min in 250 mL**, or **5 mg FAC-equivalent/min total**. The exact Eco One manual and its 500 mL / 200 ppm / 8-minute check remain important alternate source anchors, but the planner no longer uses them as the default timing basis. The [skincare HOCl recipe developer](hypochlorous_acid_calibration_planner.html) opens on the observed Amazon/Chloe recipe and keeps the documented and market-salt modes as explicit alternatives. Final pH and FAC still have to be measured together. [[1]](source_docs/eco-one-user-manual.pdf) [[8]](source_docs/FDA_510k_K180305_Hychloderm_0.01pct_HOCl.pdf) [[9]](source_docs/Zhang_2023_0.01pct_HOCl_blepharitis_RCT.pdf) [[11]](https://store.hocl.com/ecoone/) [[12]](https://ewco.com/system-ecoloxone) [[19]](https://www.amazon.com/dp/B08SMD6WRF)

## 1. Why this formula is the most likely

The conclusion is not an average of unrelated online recipes. It gives the exact one-liter manual the most weight, then asks whether independent sources reproduce the same starting condition.

| Source | Water | Salt | 5% vinegar | Time and reported output | Evidence use |
|---|---:|---:|---:|---|---|
| Eco One user manual | 1.0 L | 2.00 g | 1 tsp ≈ 5 mL | 3/5/8/16 min → 40/60/100/200 ppm | Primary recipe and nominal time curve |
| Farah & Al-Haj Ali 2021 | 1.0 L distilled | 2.00 g | 5.0 mL | Usually about 10 min; figure shows 250 ppm; starting solution described as pH 4–6 | Independent exact-ratio confirmation |
| Stony Brook Eco One experiments | 1.0 L tap | 2.00 g | 1 tsp ≈ 5 mL | 20 min; measured batches included 257.6 ppm/pH 4.58 and 352.5 ppm/pH 4.95 | Real-output variability, not a promise |
| HYPO 7.5 manual | 7.5 L | 2 supplied scoops | 2 supplied scoops for 200 ppm | 8 min → 200 ppm; 20 min → 500 ppm | Confirms a vinegar/pH workflow, but unknown scoop masses block exact per-liter transfer |
| CN114134513A example | 0.4 L | 0.50 g (1.25 g/L) | 1.0 mL (2.5 mL/L) | 3 min → 50–100 ppm; 6 min → 100–150 ppm | Patent example showing device dependence, not validation |

The first three sources converge on **2 g/L salt + about 5 mL/L 5% vinegar**. That agreement is stronger than the recipes from a different cell, volume, power supply, or unknown scoop. [[1]](source_docs/eco-one-user-manual.pdf) [[2]](source_docs/farah-al-haj-ali-2021-electrolyzed-water.pdf) [[3]](source_docs/stony-brook-eco-one-hocl-study-2021.pdf)

## 2. Step-by-step preparation

1. Confirm that the exact generator manual permits 5% white vinegar **before** electrolysis and that the selected volume keeps the electrodes safely immersed. A salt-only, capsule-only, unknown, PWPAM, bleach, or chlorine-tablet path is excluded.
2. Add the selected 200–1,000 mL of purified or distilled water. For purified water, 200 mL is approximately 200 g. Keep the power connector dry and confirm the selected amount safely covers the electrodes. Only the 1,000 mL recipe/program table is manufacturer-published.
3. Weigh the selected plain food-grade non-iodized NaCl rate: documented mode uses 2.00 g/L (0.40–2.00 g across 200–1,000 mL); experimental market-salt mode uses 0.60 g/L (0.12–0.60 g).
4. Measure the displayed manual amount of 5% distilled white vinegar before electrolysis: 5.0 mL/L. The pH selector does not change this dose because no validated dose-to-final-pH curve was found. Do not substitute cleaning vinegar, concentrated acetic acid, or an unknown acidity.
5. Add the salt and vinegar before electrolysis and mix/assemble exactly as the manual directs.
6. Choose a target. In the default Amazon/Chloe mode, the 250 mL / ≈300 ppm / 15-minute observation is the primary anchor: time increases with volume and target FAC. The documented 2.00 g/L mode retains the published 1 L 3/5/8/16/40-minute anchors, and the experimental 0.60 g/L mode retains its separate 3.14 conductivity scenario; neither alternative replaces the default working calibration.
7. At cycle completion, measure final FAC and pH with methods that cover the expected ranges.
8. Log the water, salt/vinegar lots, time, device, test methods, FAC, and pH. Never add acid or salt to rescue the completed chlorine-containing batch.

## 3. How the water and output sliders work

The developer opens on the Amazon/Chloe observed-rate recipe and treats that as the default timing basis for its working calculations. It exposes the published one-liter FAC points as convenience preset buttons while keeping the controls continuous: water moves in 1 mL increments, FAC in 1 ppm increments, and target and starting-water pH in 0.01 increments. The pH buttons include the user-observed value (4.5), the observed endpoint center (4.77), and market median (5.35), but only change the final-measurement comparison. The default local FAC trace is scaled from the 250 mL observation; its shaded 0.8–1.4× range is a visible sensitivity scenario informed by real output variability, not a confidence interval. The documented and market modes remain explicit alternative models.

```text
default observed point = 250 mL / ≈300 ppm / 15 min
default time = 15 min × planned volume / 250 mL × target FAC / 300 ppm
default salt = 6.00 g/L × planned volume
default vinegar = 2.50 mL/L × planned volume

documented alternate anchors = (3 min, 40 ppm), (5 min, 60 ppm), (8 min, 100 ppm),
                                (16 min, 200 ppm), (40 min, 500 ppm)
market alternate salt time factor = (2.00 / selected salt g/L)^0.95
salt = selected salt g/L × water volume
finished FAC and pH = measured outputs
```

The proportional time rule assumes that current, electrode immersion, mixing, temperature, salt conductivity, and Faradaic efficiency remain comparable as volume changes. The published 500 mL / 200 ppm / 8-minute point validates the relationship at one half-liter condition; it does not validate all sub-liter volumes or target combinations. The device specification gives 110/220 V, 50/60 Hz mains compatibility but does not disclose DC output voltage, current, or watts, so the calculator applies **no wattage multiplier**. It relies on the empirical production table instead. [[12]](https://ewco.com/system-ecoloxone)

Real output is not exact. The same nominal recipe produced published values above the manual curve: about 250 ppm at a reported usual 10-minute cycle in one paper, and 257.6 or 352.5 ppm after 20 minutes in two Eco One experimental batches. Water chemistry, test method, electrode condition, current, temperature, gas loss, and other device/process variables plausibly contribute. [[2]](source_docs/farah-al-haj-ali-2021-electrolyzed-water.pdf) [[3]](source_docs/stony-brook-eco-one-hocl-study-2021.pdf)

## 2A. Amazon/Chloe recipe: default working calibration

The user-supplied Amazon review by **Chloe** (January 20, 2026) reports **500 mL water, 3 g non-iodized table salt, 1.25 mL vinegar, and 15 minutes**, with a photographed result near **400 ppm FAC and pH 4.5**. [[19]](https://www.amazon.com/dp/B08SMD6WRF) On 2026-08-27, the user ran **250 mL for 15 minutes** and observed approximately **300 ppm FAC and pH 4.5** from the supplied photographs. That observation is now the primary working calibration for the Amazon/Chloe recipe. The FAC value remains an approximate coarse-strip observation, not an exact assay; the pH strip is likewise a visual estimate and may be affected by the salty sample.

| Record | Water | Salt | Vinegar | Time | Reported/observed FAC | Reported/observed pH | Evidence class |
|---|---:|---:|---:|---:|---:|---:|---|
| Chloe Amazon review | 500 mL | 3.00 g | 1.25 mL; acidity unspecified | 15 min | ≈400 ppm | ≈4.5 | User review and photograph; anecdotal |
| User reproduction | 250 mL | 1.50 g* | 0.625 mL* | 15 min | ≈300 ppm | ≈4.5 | User-supplied photo; primary working calibration |

\* The local-rate calibration assumes the 250 mL run used the **volume-scaled review amounts**. If the full review amounts—3.00 g salt and 1.25 mL vinegar—were used in 250 mL, the batch had twice the review concentrations and must be logged as a different recipe; do not use it to calibrate the scaled review rate.

The default working creation rate is approximately **20 ppm/min within 250 mL**, equivalent to approximately **5 mg FAC-equivalent/min total** (300 mg/L × 0.25 L ÷ 15 min). The calculator treats that observation as the **primary rate for every batch generated by this locked Amazon/Chloe recipe**: it multiplies time by planned volume ÷ 250 mL and by target FAC ÷ 300 ppm. If that same total rate held at 500 mL, a 15-minute run would correspond to approximately 150 ppm, not 400 ppm. The original review claim implies approximately 26.7 ppm/min within 500 mL, or 13.3 mg/min total; it remains historical source context rather than an active competing calculation.

```text
default Amazon/Chloe timing = 15 min × planned volume / 250 mL
                              × target FAC / 300 ppm
```

This is now the recipe's primary working model, but it remains an observed local rate rather than a new manufacturer program or a universal chlorine-production rate. It assumes the same device, cell, water, locked ingredient rates, current behavior, temperature, and test method. It does not make the Amazon device manual compatible with vinegar. [[14]](source_docs/IUPAC_2019_electrochemical_terminology_Faraday_law.pdf) [[17]](source_docs/Khalid_2020_electrolysis_parameters_NaCl_voltage_time.pdf) [[19]](https://www.amazon.com/dp/B08SMD6WRF)

### Why changing generator salt would change the electrolysis model

Salt does not supply a simple independent “ppm per gram” control. IUPAC's electrochemical definitions give the governing relationship: electric current is the rate of charge transfer, and the amount transformed at an electrode is proportional to charge under Faraday's laws. For a real chlorine cell, useful output also depends on **Faradaic/current efficiency**—the fraction of charge that produces the desired chlorine chemistry rather than competing reactions. [[16]](source_docs/IUPAC_2019_electrochemical_terminology_Faraday_law.pdf)

```text
charge, Q = integral(current, dt)
electrochemical product ∝ Q × Faradaic efficiency
time for a target ∝ required product / (current × efficiency)
```

NaCl concentration can change both terms in the denominator. In a fixed-voltage laboratory cell, Khalid et al. found that increasing NaCl increased solution conductivity and influenced current and chlorine production; voltage, salt concentration, and time interacted rather than forming a transferable one-variable rule. A separate electrochlorination study identified NaCl concentration as a major determinant of current efficiency and power consumption. Those cells and concentration ranges differ from Eco One, so they support the **existence and direction of salt effects**, not a numeric Eco One multiplier. [[17]](source_docs/Khalid_2020_electrolysis_parameters_NaCl_voltage_time.pdf) [[18]](https://www.sciencedirect.com/science/article/pii/S1226086X12002638)

The control architecture determines what happens next:

- In a **constant-voltage** device, lower conductivity will usually reduce current, so a target charge generally takes longer; chloride transport and current efficiency can also change.
- In a **regulated constant-current** device, the controller may increase voltage to hold current, so the same charge could take similar time until voltage/compliance, heating, mass-transfer, or efficiency limits intervene.
- Eco One discloses neither control mode nor DC voltage/current traces, and publishes no FAC curve at 0.60 g/L feed.

For an unvalidated sensitivity scenario, the experimental mode fits conductivity as proportional to concentration raised to **0.95**. That exponent is consistent with Khalid et al.'s approximately 17-fold conductivity increase for a 20-fold NaCl increase. The resulting Eco One scenario is:

```text
salt time factor = (2.00 g/L / selected salt g/L)^0.95
at 0.60 g/L: factor = 3.14
1 L, 100 ppm: 8.00 min × 3.14 = 25.1 min
```

This is deliberately not the naive 3.33× inverse-concentration ratio, because dilute-solution molar conductivity changes with concentration. It is still an **optimistic central estimate**: lower chloride may reduce current efficiency, while a current-regulated device could partly compensate. The tool keeps the actual time visible, labels the model, constructs a cycle/partial-cycle plan, and requires measured FAC for the next-fresh-batch correction.

### Why 100 ppm is the skincare evidence reference

The 100 ppm setting is the strongest cross-source starting point for the requested **skincare developer** because it is simultaneously:

- an exact eight-minute Eco One manual milestone;
- the dilute-water equivalent of 0.01% w/v HOCl (0.10 g/L = 100 mg/L ≈ 100 ppm);
- the stated concentration in the Hychloderm K180305 finished, buffered skin/wound solution; and
- the concentration used in a randomized 2023 adjunctive eyelid-hygiene trial. [[1]](source_docs/eco-one-user-manual.pdf) [[8]](source_docs/FDA_510k_K180305_Hychloderm_0.01pct_HOCl.pdf) [[9]](source_docs/Zhang_2023_0.01pct_HOCl_blepharitis_RCT.pdf)

This is a **concentration reference, not a product-equivalence inference**. The cleared product and trial formulation control identity, buffer, impurities, stability, packaging, and use conditions that this generator worksheet cannot reproduce. A facial-skin antisepsis study also found 0.01% HOCl less effective than chlorhexidine on its primary bacterial-growth comparison, which is a useful counterweight to “more science” being misread as universal superiority. [[10]](https://pubmed.ncbi.nlm.nih.gov/33247899/)

## 4. What the pH selector and graph mean

The Eco One manual says vinegar lowers pH and identifies pH 4–6 as the range in which HOCl is dominant. The Farah preparation also describes the pre-electrolysis solution as pH 4–6. The larger HYPO 7.5 system instructs the operator to verify final pH 5–6. The Stony Brook Eco One batches measured pH 4.58 and 4.95 after 20 minutes. [[1]](source_docs/eco-one-user-manual.pdf) [[2]](source_docs/farah-al-haj-ali-2021-electrolyzed-water.pdf) [[3]](source_docs/stony-brook-eco-one-hocl-study-2021.pdf) [[4]](source_docs/hypo-7-5-product-manual.pdf)

No source provides a trustworthy pH measurement at every minute or a validated vinegar-dose/final-pH curve for this exact home recipe. The developer therefore treats target pH as a **comparison goal**, not a recipe input:

```text
manual vinegar = 5.0 mL/L × planned volume
selected pH = comparison target for the measured final result
published pH evidence = 4.58 and 4.95 after 20 minutes
```

The observed endpoint center is the mean of the two Stony Brook final readings, pH 4.58 and 4.95, for the published 5 mL/L recipe after 20 minutes. The graph shows those two endpoint observations and the selected target as separate marks. It deliberately omits a pH reaction curve because real source-water alkalinity, buffering, electrolysis, chlorine speciation, temperature, and gas transfer were not measured through time.

## 5. Market-median experimental recipe

The current disclosure ledger found five facial/skin sprays with usable numeric pH values: 4.50, 4.60, 5.35, 5.50, and 5.50 after using the midpoint once for each published range. Their median is **pH 5.35**. Four traceable formulations disclosed numeric NaCl: 0.06%, 0.06%, 0.06%, and a 0.8–1.0% range whose midpoint is 0.90%. Their median is **0.06% w/v = 0.60 g/L**. [[13]](data/hocl_market_ph_salt_2026-08-25.csv)

These are disclosure-biased finished-product medians, not validated generator inputs. Briotech's current SDS alone spans 8–10 g/L NaCl, showing that commercial skin sprays do not share one salt concentration. At the user's request, the selectable market button repurposes 0.60 g/L as a clearly labeled **experimental generator feed**, loads pH 5.35 as the measurement target, and applies the 3.14× conductivity time factor. It is a calibration recipe, not evidence that Eco One will reproduce a commercial formulation. [[14]](source_docs/FDA_510k_K181074_Simple_Science_facial_eyelid_cleanser.pdf) [[15]](source_docs/briotech-topical-skin-spray-sds-2022.pdf)

| Measured final pH | Guide interpretation | What to do |
|---:|---|---|
| ≤ 3.0 or > 7.0 | Stop | Do not use or counter-adjust the completed batch. Review the manual/process outside the active run. |
| > 3.0 to < 4.0 | Stop/investigate | Below the documented recipe expectation. Do not chase it with more or less vinegar. |
| 4.0–4.9 | Plausible recipe range | Pair with FAC and method quality; a repeat is needed to judge process consistency. |
| 5.0–6.0 | Preferred documented overlap | Both the Eco One expectation and HYPO 7.5 final check overlap here. Pair with FAC. |
| 6.1–6.5 | Plausible but outside the exact 4–6 expectation | Recheck method and repeat a fresh manual-compatible batch before treating it as calibrated. |
| 6.6–7.0 | Investigate | Outside the cited working bands; do not add acid to the completed batch. |

CDC explains that pH changes the HOCl/hypochlorite balance and warns that acid mixed with hypochlorite can release toxic chlorine gas. That is why pH and FAC are measured as a pair—and why the guide never offers an after-the-fact acid correction. [[5]](https://www.cdc.gov/infection-control/hcp/disinfection-sterilization/chemical-disinfectants.html)

## 6. FAC is a measurement, not a product claim

Use a fresh FAC method whose chart covers the expected result. A 0–10 ppm pool strip that saturates cannot distinguish 100 from 200 or 350 ppm. Record the test lot/expiry and package dip/read timing when available.

A measured 40, 60, 100, or 200 ppm result is a batch observation. It does not establish exact HOCl-only concentration, purity, byproducts, sterility, shelf life, skin safety, eye safety, inhalation safety, contact time, or regulatory efficacy. The generator recipe and documented program describe production; they do not authorize an intended use.

## 7. Do not transfer this formula to PWPAM

The supplied PWPAM manual says salt plus water, identifies the output as sodium hypochlorite, and gives cleaning directions. It does not authorize vinegar or a pH-controlled cycle. See the [PWPAM manual boundary](index.html#doc3). [[6]](../19_diy_topical_formulation/source_docs/pwpam_manual_2026-08-24_recipe-and-use.jpg)

## Evidence gaps

- No independent time-series study measured both pH and FAC at each Eco One manual milestone.
- The manufacturer publishes its main production table at 1 L, with one separate 500 mL / 200 ppm / 8-minute point. Other 200–999 mL combinations remain proportional extrapolations that need measured calibration; electrode immersion at the selected amount must be confirmed from the exact device geometry/manual.
- No titration curve or buffer/alkalinity model validates changing vinegar to hit a chosen pH. The calculator therefore locks vinegar to the manual 5 mL/L instead of pretending to solve the dose.
- DC output voltage, current, and watts were not found. Wall-input voltage is not enough to derive electrolysis power, so no wattage correction is used.
- The Eco One control mode (constant voltage, constant current, or another feedback strategy), current trace, conductivity range, and FAC/time curve at alternative NaCl concentrations were not found. The 0.95 exponent and 3.14× low-salt factor are therefore an explicit engineering scenario, not a device measurement.
- Market pH and NaCl disclosure is sparse. The two medians describe only the products with traceable numeric values.
- The Stony Brook values show substantial between-batch/output variation but do not isolate which variable caused it.
- Vinegar is specified volumetrically; the approximate gram conversion is convenient for logging, not an acid assay.
- No home recipe measurement establishes cosmetic, facial, eye, aerosol, or face-contact-bedding suitability.

## Sources

1. [Eco One user manual](source_docs/eco-one-user-manual.pdf) — primary one-liter formula and 3/5/8/16-minute nominal FAC rows.
2. [Farah & Al-Haj Ali, 2021](source_docs/farah-al-haj-ali-2021-electrolyzed-water.pdf) — peer-reviewed 2 g/L + 5 mL/L preparation and 250 ppm strip result.
3. [Stony Brook Eco One study, 2021](source_docs/stony-brook-eco-one-hocl-study-2021.pdf) — same recipe with measured Eco One FAC and pH observations.
4. [HYPO 7.5 product manual](source_docs/hypo-7-5-product-manual.pdf) — different-scale vinegar-compatible generator with pH/FAC verification.
5. [CDC, Chemical Disinfectants](https://www.cdc.gov/infection-control/hcp/disinfection-sterilization/chemical-disinfectants.html) — pH/speciation context and acid/hypochlorite warning.
6. User-supplied [PWPAM recipe/use manual page](../19_diy_topical_formulation/source_docs/pwpam_manual_2026-08-24_recipe-and-use.jpg) — salt-only device boundary.
7. [CN114134513A](https://patents.google.com/patent/CN114134513A/en) — different-volume patent example; supports device dependence, not validation.
8. [FDA 510(k) K180305 Hychloderm summary](source_docs/FDA_510k_K180305_Hychloderm_0.01pct_HOCl.pdf) — finished, buffered 0.01% HOCl skin/wound solution and product-specific intended-use/testing boundary.
9. [Zhang et al., 2023](source_docs/Zhang_2023_0.01pct_HOCl_blepharitis_RCT.pdf) — randomized adjunctive eyelid-hygiene trial using 0.01% topical HOCl.
10. [Tran et al., 2021](https://pubmed.ncbi.nlm.nih.gov/33247899/) — direct facial-skin antisepsis comparison; 0.01% HOCl did not outperform chlorhexidine and is not a universal efficacy benchmark.
11. [Official Eco One product page](https://store.hocl.com/ecoone/) — current one-liter 40/60/100/200/500 ppm production table, optional-vinegar language, device capacity, and additional-cycle claim; accessed 2026-08-25.
12. [EWCO Eco One technical page](https://ewco.com/system-ecoloxone) — 500 mL / 200 ppm / 8-minute production point and 110/220 V, 50/60 Hz mains specification; accessed 2026-08-25.
13. [Market pH/NaCl disclosure ledger](data/hocl_market_ph_salt_2026-08-25.csv) — product-level numeric inputs, midpoint handling, inclusion flags, and median rows; compiled 2026-08-25.
14. [FDA 510(k) K181074 Simple Science facial/eyelid cleanser](source_docs/FDA_510k_K181074_Simple_Science_facial_eyelid_cleanser.pdf) — primary 0.06% NaCl finished-product disclosure.
15. [Briotech Topical Skin Spray SDS](source_docs/briotech-topical-skin-spray-sds-2022.pdf) — primary 0.8–1.0% NaCl composition range.
16. [IUPAC electrochemical terminology and Faraday-law definitions](source_docs/IUPAC_2019_electrochemical_terminology_Faraday_law.pdf) — current, charge, and amount-transformed relationship; primary terminology source.
17. [Khalid et al., 2020](source_docs/Khalid_2020_electrolysis_parameters_NaCl_voltage_time.pdf) — controlled different-cell experiments varying 0.05%, 0.53%, and 1% NaCl, voltage, and time; supports conductivity/current/chlorine interaction, not Eco One calibration.
18. [Choi, Shim & Yoon, 2013](https://www.sciencedirect.com/science/article/pii/S1226086X12002638) — electrochlorination experiment identifying NaCl concentration as a major influence on current efficiency and power consumption.
19. User-supplied [Amazon PWPAM review capture](https://www.amazon.com/dp/B08SMD6WRF) and 2026-08-27 reproduction photograph — Chloe’s 500 mL recipe/source record and the user’s approximate 250 mL / 15-minute / ≈300 ppm observation; primary working calibration for the Amazon/Chloe recipe, not independent validation or a universal device rate.


## Formula verification — 2026-09-06

**Verified arithmetic does not predict final pH.** Scaling the recorded 250 mL / 300 mg/L / 15-minute observation gives 75 mg FAC-equivalent produced, or 5 mg/min; the same-yield estimate for 500 mL and 300 mg/L is 30 minutes. This is conditional on identical current efficiency and device operation. The ingredient assumptions remain 1.5 g salt and 0.625 mL vinegar in the calibration run; a different actual dose invalidates that calibration. Neither the source review nor a strip photograph establishes vinegar compatibility for a salt-only manual.

**pH 4.5 implies about 99.9% HOCl within the HOCl/OCl⁻ pair**, using `fraction = 1/(1 + 10^(pH − 7.5))`. At pH 5.5 it is 99.0%, at 6.5 it is 90.9%, and at 7.5 it is 50%. This equation computes a species ratio from measured pH, not pH from vinegar or run time. Starting-water pH cannot replace alkalinity/buffer capacity; pH numbers cannot be averaged to calculate mixture pH. Temperature, ionic strength, electrochemical reactions, and chlorine demand also matter. [EPA equilibrium study](https://nepis.epa.gov/Exe/ZyPURL.cgi?Dockey=P1000GU9.TXT).

**FAC units:** an available-chlorine measurement generally reports mg/L as Cl₂. At 300 mg/L FAC and pH 4.5, the estimate is 299.7 mg/L as Cl₂ attributable to HOCl, equivalent to about **221.8 mg/L molecular HOCl** (`×52.46/70.90`). It is not automatically 300 mg/L molecular HOCl. The pH and FAC methods must be compatible with the sample; confirm the test's reporting basis. No pH calculation establishes contaminants, microbial quality, skin suitability, or shelf life.

**Unverified formula:** the low-salt time multiplier `(2/0.6)^0.95 ≈ 3.14` is arithmetically correct but is not a validated generator transfer law. A conductivity exponent borrowed from another cell cannot establish current efficiency or controller behavior for this generator. Treat its time as an illustrative scenario, not a verified recipe. Finished chlorine batches must not be acid-adjusted to chase a target; follow the exact compatible device manual. [CDC chemical-disinfectants guidance](https://www.cdc.gov/infection-control/hcp/disinfection-sterilization/chemical-disinfectants.html).

[Audit source notes](../19_diy_topical_formulation/source_docs/research_resource_log_2026-09-06.txt).
