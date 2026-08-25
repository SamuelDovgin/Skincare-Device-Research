# Scaled Acidified-Brine Recipe, Time Curves, and QC

*Updated 2026-08-25. This is a device-specific preparation and measurement guide, not a medical, cosmetic, disinfection, or product-certification claim.*

## 0. Bottom line

For the exact Eco One one-liter manual—or another device whose own manual expressly permits the same fill and acidified-brine chemistry—the best-supported starting recipe is:

- **1,000 mL purified or distilled water**;
- **2.00 g food-grade non-iodized sodium chloride**; and
- **5.0 mL (1 teaspoon; approximately 5.0 g) of 5% distilled white vinegar**, added before electrolysis.

The exact manual reports nominal one-liter FAC outputs of **40 ppm at 3 minutes, 60 ppm at 5 minutes, 100 ppm at 8 minutes, and 200 ppm at 16 minutes**; the current official product page adds **500 ppm at 40 minutes**. The [skincare HOCl recipe developer](hypochlorous_acid_calibration_planner.html) defaults to **100 ppm at 8 minutes and 1,000 mL**, then lets the developer explore 200–1,000 mL, 40–500 ppm, and final pH 4.5–6.5. The one-liter anchors are source values; between-anchor interpolation and volume/time scaling are explicitly labeled sensitivity assumptions. The pH selector changes an illustrative pre-batch vinegar amount, never a finished-batch correction. Final pH and FAC still have to be measured together. [[1]](source_docs/eco-one-user-manual.pdf) [[8]](source_docs/FDA_510k_K180305_Hychloderm_0.01pct_HOCl.pdf) [[9]](source_docs/Zhang_2023_0.01pct_HOCl_blepharitis_RCT.pdf) [[11]](https://store.hocl.com/ecoone/)

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
3. Weigh 2.00 g/L of plain food-grade non-iodized NaCl: 0.40 g at 200 mL through 2.00 g at 1,000 mL.
4. Measure the displayed amount of 5% distilled white vinegar before electrolysis. The UI caps this at the source recipe's 5.0 mL/L; do not substitute cleaning vinegar, concentrated acetic acid, or an unknown acidity.
5. Add the salt and vinegar before electrolysis and mix/assemble exactly as the manual directs.
6. Choose a target. At 1,000 mL, 40/60/100/200/500 ppm map to the published 3/5/8/16/40-minute anchors. At another volume or between anchors, the developer shows a proportional planning estimate, not a manufacturer-validated setting.
7. At cycle completion, measure final FAC and pH with methods that cover the expected ranges.
8. Log the water, salt/vinegar lots, time, device, test methods, FAC, and pH. Never add acid or salt to rescue the completed chlorine-containing batch.

## 3. How the water and output sliders work

The developer exposes the published one-liter FAC points as convenience preset buttons while keeping the controls continuous: water moves in 1 mL increments, FAC in 1 ppm increments, and target and starting-water pH in 0.01 increments. The pH convenience buttons select common scenarios, including the observed 4.8 reference, but do not imply validated vinegar doses. Its central FAC trace is piecewise linear through the source anchors; its shaded band is a visible ±20% sensitivity band, not a confidence interval.

```text
1 L anchors = (3 min, 40 ppm), (5 min, 60 ppm), (8 min, 100 ppm),
               (16 min, 200 ppm), (40 min, 500 ppm)
planned time = interpolated 1 L time × water volume / 1,000 mL
salt = 2.00 g/L × water volume
finished FAC and pH = measured outputs
```

The proportional time rule assumes that current, electrode immersion, mixing, temperature, salt conductivity, and Faradaic efficiency remain comparable as volume changes. The official one-liter table does not validate the smaller-volume settings. That is why the UI calls them **volume-scaled estimates** and asks for the paired result to be reported back for the next fresh-batch calibration.

Real output is not exact. The same nominal recipe produced published values above the manual curve: about 250 ppm at a reported usual 10-minute cycle in one paper, and 257.6 or 352.5 ppm after 20 minutes in two Eco One experimental batches. Water chemistry, test method, electrode condition, current, temperature, gas loss, and other device/process variables plausibly contribute. [[2]](source_docs/farah-al-haj-ali-2021-electrolyzed-water.pdf) [[3]](source_docs/stony-brook-eco-one-hocl-study-2021.pdf)

### Why 100 ppm is the skincare evidence reference

The 100 ppm setting is the strongest cross-source starting point for the requested **skincare developer** because it is simultaneously:

- an exact eight-minute Eco One manual milestone;
- the dilute-water equivalent of 0.01% w/v HOCl (0.10 g/L = 100 mg/L ≈ 100 ppm);
- the stated concentration in the Hychloderm K180305 finished, buffered skin/wound solution; and
- the concentration used in a randomized 2023 adjunctive eyelid-hygiene trial. [[1]](source_docs/eco-one-user-manual.pdf) [[8]](source_docs/FDA_510k_K180305_Hychloderm_0.01pct_HOCl.pdf) [[9]](source_docs/Zhang_2023_0.01pct_HOCl_blepharitis_RCT.pdf)

This is a **concentration reference, not a product-equivalence inference**. The cleared product and trial formulation control identity, buffer, impurities, stability, packaging, and use conditions that this generator worksheet cannot reproduce. A facial-skin antisepsis study also found 0.01% HOCl less effective than chlorhexidine on its primary bacterial-growth comparison, which is a useful counterweight to “more science” being misread as universal superiority. [[10]](https://pubmed.ncbi.nlm.nih.gov/33247899/)

## 4. What the pH selector and dashed graph mean

The Eco One manual says vinegar lowers pH and identifies pH 4–6 as the range in which HOCl is dominant. The Farah preparation also describes the pre-electrolysis solution as pH 4–6. The larger HYPO 7.5 system instructs the operator to verify final pH 5–6. The Stony Brook Eco One batches measured pH 4.58 and 4.95 after 20 minutes. [[1]](source_docs/eco-one-user-manual.pdf) [[2]](source_docs/farah-al-haj-ali-2021-electrolyzed-water.pdf) [[3]](source_docs/stony-brook-eco-one-hocl-study-2021.pdf) [[4]](source_docs/hypo-7-5-product-manual.pdf)

No source provides a trustworthy pH measurement at every minute or a validated vinegar-dose/final-pH curve for this exact home recipe. The developer therefore treats the pH control as an **illustrative sensitivity model**:

```text
effective acid load = max(0, 10^(-target pH) - 10^(-water pH))
vinegar rate = 5.0 mL/L × effective acid load / reference acid load
vinegar rate is capped at the manual's 5.0 mL/L source amount
```

The reference endpoint is the mean of the two Stony Brook final readings, pH 4.58 and 4.95, for the published 5 mL/L recipe after 20 minutes. The estimated starting pH is a simple weak-acetic-acid equilibrium using 5% vinegar as approximately 0.833 M acetic acid. Real source-water alkalinity, buffering, electrolysis, chlorine speciation, temperature, and gas transfer are not captured. The dashed graph is only an eased visual bridge from the estimated starting point to the selected or capped endpoint; it is **not measured kinetics or a validated prediction**.

| Measured final pH | Guide interpretation | What to do |
|---:|---|---|
| ≤ 3.0 or > 7.0 | Stop | Do not use or counter-adjust the completed batch. Review the manual/process outside the active run. |
| > 3.0 to < 4.0 | Stop/investigate | Below the documented recipe expectation. Do not chase it with more or less vinegar. |
| 4.0–4.9 | Plausible recipe range | Pair with FAC and method quality; a repeat is needed to judge process consistency. |
| 5.0–6.0 | Preferred documented overlap | Both the Eco One expectation and HYPO 7.5 final check overlap here. Pair with FAC. |
| 6.1–6.5 | Plausible but outside the exact 4–6 expectation | Recheck method and repeat a fresh manual-compatible batch before treating it as calibrated. |
| 6.6–7.0 | Investigate | Outside the cited working bands; do not add acid to the completed batch. |

CDC explains that pH changes the HOCl/hypochlorite balance and warns that acid mixed with hypochlorite can release toxic chlorine gas. That is why pH and FAC are measured as a pair—and why the guide never offers an after-the-fact acid correction. [[5]](https://www.cdc.gov/infection-control/hcp/disinfection-sterilization/chemical-disinfectants.html)

## 5. FAC is a measurement, not a product claim

Use a fresh FAC method whose chart covers the expected result. A 0–10 ppm pool strip that saturates cannot distinguish 100 from 200 or 350 ppm. Record the test lot/expiry and package dip/read timing when available.

A measured 40, 60, 100, or 200 ppm result is a batch observation. It does not establish exact HOCl-only concentration, purity, byproducts, sterility, shelf life, skin safety, eye safety, inhalation safety, contact time, or regulatory efficacy. The generator recipe and documented program describe production; they do not authorize an intended use.

## 6. Do not transfer this formula to PWPAM

The supplied PWPAM manual says salt plus water, identifies the output as sodium hypochlorite, and gives cleaning directions. It does not authorize vinegar or a pH-controlled cycle. See the [PWPAM manual boundary](index.html#doc3). [[6]](../19_diy_topical_formulation/source_docs/pwpam_manual_2026-08-24_recipe-and-use.jpg)

## Evidence gaps

- No independent time-series study measured both pH and FAC at each Eco One manual milestone.
- The manufacturer publishes its production table at 1 L. Every 200–999 mL time result is a proportional extrapolation that needs measured calibration; electrode immersion at the selected amount must be confirmed from the exact device geometry/manual.
- No titration curve or buffer/alkalinity model validates the vinegar selector. Its amount is a source-anchored sensitivity estimate capped at 5 mL/L.
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
