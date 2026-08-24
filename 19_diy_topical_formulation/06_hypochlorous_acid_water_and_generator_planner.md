# Hypochlorous Acid Water: DIY Generation, Quality Control, Fabric Use, and Face-Use Boundaries

*Compiled 2026-08-22. Research orientation, not medical, infection-control, or chemical-safety advice. This page is a controlled home-experiment framework, not a validated disinfectant manufacturing protocol. Confidence labels: **verified** = primary/regulatory or peer-reviewed source; **limited** = small, product-specific, or mechanistic evidence; **inference** = transparent extrapolation; **unknown** = the needed home-use data do not exist.*

## 0. Bottom line

For the project you described, I would split the plan in two:

1. **Pillowcase experiment:** if you still want to explore it, make a small batch of electrolyzed saline, measure free available chlorine (FAC) and pH after every early run, use it only on clean, washable fabric, and treat the result as a hygiene experiment—not proven acne treatment or a substitute for laundering.
2. **Future face spray:** buy a finished product explicitly labeled for facial/dermal use. A measured DIY batch can tell you its chlorine concentration and approximate HOCl fraction, but it cannot prove skin compatibility, sterility, electrode-material purity, preservative/stability performance, or suitability around the eyes.
3. **Do not use pool chlorine tablets.** They are concentrated pool-water chemicals such as calcium hypochlorite or chlorinated isocyanurates, not a facial spray ingredient. They can bleach or damage fabric, irritate skin and lungs, and create dangerous gas if mishandled or mixed with acid. [[1]](https://www.cdc.gov/infection-control/hcp/disinfection-sterilization/chemical-disinfectants.html)

My target for a **pillowcase-oriented, mildly acidic batch** is:

| Measurement | Preferred target | Working QC window | Reject / stop condition |
|---|---:|---:|---|
| Free available chlorine (FAC) | 180–220 ppm | 150–250 ppm | 0–99 ppm is below this project's target; >250 ppm dilute and retest |
| Final pH | 5.5–6.2 | 5.0–6.5 | <4.0, strong irritating fumes, or pH that keeps drifting: stop and discard |
| Approximate HOCl fraction | 95–99% | >90% | pH ≥7 is not the mildly acidic target |
| Appearance | Clear/colorless | Clear/colorless | Brown/green tint, particles, flakes, or obvious electrode corrosion: discard |

These are **quality-control targets for this experiment**, not regulatory safety limits and not proof that a batch disinfects a pillowcase. FAC measures free chlorine collectively; pH is what lets you estimate whether most of that FAC is HOCl rather than hypochlorite (OCl⁻).

## 1. What you are actually making

The hardware is a small electrochlorination cell: chloride from salt is oxidized at an electrode while water is reduced at the other electrode. The output is a mixture of chlorine species, not a magical “HOCl-only” liquid. The balance among dissolved chlorine, HOCl, and OCl⁻ depends on pH, chlorine concentration, current, electrode material, cell geometry, water chemistry, temperature, and time. [[2]](https://pmc.ncbi.nlm.nih.gov/articles/PMC8119747/)[[3]](https://doi.org/10.1016/j.jwpe.2021.102228)

HOCl is a weak acid with a pKa near 7.5. A useful approximation is:

```text
HOCl fraction = 1 / (1 + 10^(pH − 7.5))
```

Approximate speciation when the measured FAC is 200 ppm:

| Final pH | Approx. FAC present as HOCl | Approx. HOCl within 200 ppm FAC |
|---:|---:|---:|
| 4.5 | 99.9% | 200 ppm |
| 5.0 | 99.7% | 199 ppm |
| 5.5 | 99.0% | 198 ppm |
| 6.0 | 96.9% | 194 ppm |
| 6.2 | 95.2% | 191 ppm |
| 6.5 | 90.9% | 182 ppm |
| 7.0 | 76.0% | 152 ppm |
| 7.5 | 50.0% | 100 ppm |
| 8.0 | 24.0% | 48 ppm |

That is why **200 ppm FAC at pH 5.8** is a much more useful description than “200 ppm HOCl” based only on a recipe. The chlorine strip does not identify HOCl by itself.

There is also no advantage to making the solution extremely acidic. At lower pH, dissolved chlorine and chlorine-gas behavior become a larger concern, while the HOCl fraction is already essentially maximal around pH 5–6. Do not chase a pH of 2–3 to make a “stronger” facial or fabric spray.

## 2. The starting recipe and what it does—and does not—prove

A peer-reviewed dental-office perspective describes this starting formulation for a portable electrolyzed-water unit:

| For a 1,000 mL starting batch | Amount |
|---|---:|
| Distilled or purified water | 1,000 mL |
| Pure, non-iodized sodium chloride | 2.00 g |
| Distilled white vinegar, 5% acidity | 5.0 mL |
| Initial electrolysis trial | About 10 minutes, only if the generator permits this recipe |

The report measured FAC and pH rather than assuming that the recipe always produced one exact concentration. Its example was around 250 ppm FAC with a slightly acidic pH, while other units and settings can produce very different outputs. [[2]](https://pmc.ncbi.nlm.nih.gov/articles/PMC8119747/)

Use the proportions only as a **calibration starting point**:

```text
starting water (mL) = chosen batch-water volume
salt (g) = 2.00 × chosen volume (L)
5% vinegar (mL) = 5.0 × chosen volume (L)
initial trial time = 10 minutes, only if the unit's manual allows acidified brine
```

Examples:

| Chosen batch | Water | Salt | 5% vinegar |
|---:|---:|---:|---:|
| 250 mL | 250 mL | 0.50 g | 1.25 mL |
| 500 mL | 500 mL | 1.00 g | 2.50 mL |
| 750 mL | 750 mL | 1.50 g | 3.75 mL |
| 1,000 mL | 1,000 mL | 2.00 g | 5.00 mL |
| 1,500 mL | 1,500 mL | 3.00 g | 7.50 mL |
| 2,000 mL | 2,000 mL | 4.00 g | 10.00 mL |

The [Electrolyzed-water spray planner](hypochlorous_water_planner.html) performs this scaling and then walks through the measurement result. It separates first-batch planning, setup calibration, and measured-batch logging; accepts exact batch size, planning target, setup identity, temperature, cell condition, bottle material, and storage notes; and keeps the salt/acid ratio locked when the evidence does not support independent adjustment. Do not substitute a generator's own recipe with this one if its manual forbids vinegar, specifies a capsule, uses a divided cell, or gives a different brine concentration.

### A necessary vinegar correction

Five milliliters of 5% vinegar in unbuffered water does not mathematically guarantee a starting pH of 4–6. Commercial vinegar acidity, water alkalinity, the cell, gas exchange, and the cathodic reaction all matter. Measure the **final pH after electrolysis**. Never use the amount of vinegar as a proxy for pH.

### What each variable can plausibly change

The planner now separates **recipe inputs**, **process inputs**, and **measured outputs**. That distinction matters: a recipe can set a starting condition, but it cannot certify the result.

| Variable changed | Likely directional effect | What cannot be inferred |
|---|---|---|
| Starting water volume increases while salt/acid ratios stay fixed | Starting ingredient concentrations remain the same. At the same target FAC, the total chlorine mass required rises with volume, so time should usually rise when current and efficiency are unchanged. If time stays fixed, FAC may fall because the generated chlorine is distributed through more water. | Final FAC and final pH still depend on current, cell geometry, current efficiency, water chemistry, temperature, and mixing. |
| Salt concentration increases | Conductivity and FAC commonly increase for the same device; the cited report also describes higher initial salt as producing higher FAC. [[2]](https://pmc.ncbi.nlm.nih.gov/articles/PMC8119747/) | Salt is not a reliable pH control. More salt can also change current and electrode stress, so the planner does not provide an independent salt slider. |
| Permitted vinegar increases before electrolysis | Starting pH will usually move downward. | The size of the pH change is not predictable without water alkalinity and device behavior. Do not independently increase vinegar to chase final pH. |
| Electrolysis time or current increases | FAC and ORP commonly rise; the report describes pH, FAC, and ORP as time/current dependent and reports that higher amperage can raise FAC while lowering pH. [[2]](https://pmc.ncbi.nlm.nih.gov/articles/PMC8119747/) | The time-to-FAC relationship need not stay linear and pH can drift differently across devices. |
| The planner's FAC target changes | The comparison point, dilution calculation, and next-time estimate change. | The target selector does not alter the actual recipe, current, or output. |
| Final measured pH rises | The estimated fraction of FAC present as HOCl falls. | pH cannot tell you the total FAC; FAC cannot tell you the HOCl fraction. Both tests are required. |

The practical rule is **change one process variable on a fresh batch and remeasure both outputs**. The planner keeps salt and permitted vinegar locked to the cited starting ratio because independent “more salt” and “more acid” sliders would imply a degree of safe control that the source does not establish.

### Why time must include volume

FAC is a concentration in mg/L (numerically similar to ppm in dilute water). Holding the FAC target constant while doubling water volume doubles the approximate total free-chlorine mass that must be generated:

```text
total free-chlorine mass (mg) ≈ FAC (mg/L) × volume (L)
```

Under a **local constant-current, approximately constant-efficiency assumption**, a volume-aware timing estimate is:

```text
planned time ≈ reference time
               × (planned volume / reference volume)
               × (target FAC / measured reference FAC)
```

That means a reference run of 1,000 mL for 10 minutes at 200 ppm points to about 5 minutes for 500 mL at the same 200 ppm target, or about 20 minutes for 2,000 mL—before allowing for efficiency changes. This is the physically appropriate starting relationship because electrochemical product formation depends on passed charge, while the measured concentration also divides by solution volume. The evidence also shows that FAC changes with processing time/current and that generator construction, electrolyte, temperature, and electrode condition matter. [[2]](https://pmc.ncbi.nlm.nih.gov/articles/PMC8119747/)

The planner therefore stores **planned volume** separately from **reference-run volume**. It applies the full volume ratio, caps the target-to-measured FAC correction, widens the sensitivity band when volume changes, and requires FAC plus pH testing of the new batch. A fixed-cycle or fixed-fill device manual overrides this estimate.

### Paired QC bands and confidence

The upgraded planner reports three different things:

1. **Measured QC band:** where the final FAC and final pH land together.
2. **Estimated speciation:** the approximate HOCl share calculated from final pH, and approximate HOCl within measured FAC.
3. **Process-repeatability confidence:** how much confidence to place in reproducing the same band, based on test method and repeated fresh batches.

| Paired result | Planner band | Meaning |
|---|---|---|
| FAC 180–220 ppm **and** pH 5.5–6.2 | Preferred measured band | Central target for this pillowcase experiment; still requires confirmation. |
| FAC 150–250 ppm **and** pH 5.0–6.5, outside the preferred pair | Working measured band | Reasonable process result; avoid chasing an exact number. |
| FAC 100–149 ppm **or** pH 4.0–4.9 / 6.6–7.0 | Recalibrate next batch | Useful process data, but not the standardized target. |
| FAC >250 ppm, pH <4, pH >7, invalid measurement, or failure signals | Stop / outside project band | Dilute high FAC when appropriate and retest, or reject the batch/process result. Never correct final pH by adding acid. |

Confidence is deliberately narrower than a generic “pass.” A single paired FAC+pH result is **low process confidence**. A suitable-range chlorine method plus a calibrated pH meter or narrow-range strip and at least one matching fresh confirmation can reach **moderate process-repeatability confidence**. Three or more paired batches in the same band with better-range methods can reach **higher process-repeatability confidence**. None of these tiers establish skin safety, sterility, shelf life, acne benefit, or regulatory disinfection.

The time-adjustment display also includes an **illustrative sensitivity band**. It widens for coarse or single-run measurements, for a larger change from the reference volume, and narrows with better methods and repeated batches. It is not a statistical confidence interval; it makes the local current/time/volume assumption visible instead of presenting one exact minute as certain.

## 3. Equipment checklist

### Measurement equipment

- A **free-chlorine/FAC test** whose range includes approximately 100–300 ppm. A pool strip that only reads 0–10 ppm will saturate and is not useful for this project.
- Fresh narrow-range pH strips that visibly resolve roughly pH 4–7/8, or a pH meter calibrated with pH 4 and pH 7 buffers. A universal 0–14 strip can be too coarse near the decision boundaries; a calibrated meter is preferable for repeated generator calibration.
- A scale that resolves at least 0.1 g; 0.01 g is better for 250–500 mL batches.
- A clean syringe, pipette, or measuring cylinder for 1–10 mL vinegar. Do not estimate 2.5 mL with a random kitchen spoon.

### Generation and storage equipment

- A purpose-built electrolyzed-water generator with a documented cell and operating instructions. Do not build electrodes from nails, copper wire, random stainless utensils, or unknown metal plates.
- Distilled or purified water for repeatability. Low-mineral water reduces one source of variation, though the generator manual controls what water is allowed.
- Pure, non-iodized salt with no anti-caking blend, seasoning, or salt substitute unless the device specifically calls for it.
- A clean, opaque or amber, chemically compatible spray bottle. HDPE is a reasonable default. Do not make or store the batch in a metal container.
- A label showing date, water source, salt mass, vinegar volume, generator, run time, FAC, pH, and discard date.

### Workspace controls

Generate in ordinary room ventilation, not in a sealed cabinet, closet, car, or tiny bathroom. Electrolysis produces gases, including hydrogen, and chlorine odor or irritation is a stop signal—not a concentration target. Keep your face away from the vessel. Wear eye protection if splashing is possible. Never combine the batch with bleach, ammonia, hydrogen peroxide, pool chemicals, or other cleaners.

## 4. Exact first-run procedure

1. **Choose the use before choosing the recipe.** If the eventual goal includes facial use, buy a skin-labeled finished spray for the face instead of treating a DIY generator as a cosmetic manufacturing device.
2. **Read the generator's manual.** Confirm allowed water, salt, vinegar/activator, maximum volume, operating time, cleaning, and storage instructions. A device marketed as a “sodium hypochlorite generator” is not automatically a skin product.
3. **Start small.** Use 500 mL for the first experiment. The scaled starting formulation is 500 mL water, 1.00 g salt, and 2.50 mL 5% vinegar only when compatible with the device.
4. **Clean and inspect the cell.** Rinse it with water and check for scale, discoloration, loose coating, flakes, or corrosion. Do not scrape a coated electrode with metal.
5. **Measure the water.** Record the actual volume. Water temperature and mineral content can change output, so use the same water source for calibration runs.
6. **Add and dissolve the salt completely.** Undissolved salt at the electrode is not a controlled dose.
7. **Add vinegar only when the manual permits acidified brine.** Do not add acid to an already-electrolyzed or chlorine-containing batch.
8. **Run the manual-compatible cycle with ventilation.** Ten minutes is the initial trial time from the published 1-L starting protocol, not a universal promise of 200 ppm. If the device permits variable time, the planner can scale that reference by planned volume; fixed-cycle or fixed-fill instructions override the estimate.
9. **Optionally measure the starting-mixture pH before electrolysis.** This is useful for recording process drift, not for repeatedly adding acid until a target appears.
10. **Wait briefly for bubbles to dissipate after the run.** Do not lean over the container or intentionally sniff it. Gently mix without vigorous agitation.
11. **Take samples into separate clean cups.** Do not dip a dirty strip into the storage bottle and do not return tested liquid to the bottle.
12. **Measure FAC promptly, then final pH.** Record both readings and the test method. A pH result without FAC is incomplete; an FAC result without pH is also incomplete.
13. **Use the paired decision band below.** Do not keep “fixing” the same finished batch by pouring in vinegar or other chemicals.

## 5. How to interpret every result

### FAC result

| Measured FAC | Interpretation for this project | Next action |
|---:|---|---|
| 0–25 ppm | Process, test, or generator failure is likely; this is not the target batch. | Check the strip range and method, then repeat with a fresh batch. |
| 25–49 ppm | Low active chlorine. | Do not standardize it for the pillowcase experiment; recalibrate. |
| 50–99 ppm | It may have antimicrobial activity, but it is below the selected porous-fabric target. | Keep as a data point, not as the target recipe. |
| 100–149 ppm | A real, measurable low-concentration batch; the rayon study found 100 ppm more effective than 50 ppm under its laboratory conditions. | Accept only as a weaker experimental batch; adjust the next run if you want ~200 ppm. |
| 150–179 ppm | Good practical range. | Usually keep it; do not chase exactly 200 ppm. |
| 180–220 ppm | Target range. | Keep the recipe and verify it on two more batches. |
| 221–250 ppm | Still within the working QC window. | Use or dilute slightly; record it. |
| 251–500 ppm | Stronger than needed for this project. | Dilute with measured distilled water and retest FAC and pH. |
| >500 ppm | Outside the intended low-concentration experiment. | Do not use on face or bedding; dilute only if the generator/manual supports the intended use, then retest. |

The rayon experiment tested 50 and 100 ppm slightly acidic solution, not a 200 ppm home pillowcase spray. At 100 ppm, the study reported a larger reduction on rayon after longer spray/contact exposure than at 50 ppm; that is useful evidence about porous-surface difficulty, not proof that a cotton pillowcase treated at home will reduce acne. [[4]](https://pmc.ncbi.nlm.nih.gov/articles/PMC4976267/)

### pH result

| Final pH | Read | Action |
|---:|---|---|
| <4.0 | Too acidic for this home process; gas/irritation risk is less comfortable to manage. | Stop, ventilate, do not spray, and do not rescue the batch with more chemicals. |
| 4.0–4.9 | Very HOCl-dominant but more acidic than needed. | Prefer a better-calibrated next batch; do not use if there is irritating odor or eye/throat discomfort. |
| 5.0–6.5 | Preferred mildly acidic working zone. | Evaluate FAC, appearance, and odor together. |
| 6.6–7.0 | FAC may be adequate, but the output is moving away from the chosen target. | Recheck the meter/strip and adjust the next batch or choose a better-controlled unit. |
| >7.0 | It is not the mildly acidic HOCl-dominant batch you were trying to make. | Do not add vinegar to the finished batch; change the next starting process or device. |

If a batch has 200 ppm FAC and pH 8.0, the strip still reads 200 ppm, but only about one-quarter of that FAC is estimated to be HOCl. If a batch has 200 ppm FAC and pH 5.8, roughly 98% is estimated to be HOCl. Neither calculation proves the batch is sterile, skin-safe, or an EPA-registered disinfectant.

### Non-numeric stop signals

Discard the batch and investigate the generator if it is visibly colored, has particles or flakes, produces a strong pungent odor, irritates the eyes or throat, or gives wildly inconsistent results across identical runs. If you suspect chlorine exposure, leave the area for fresh air and follow poison-control or emergency guidance; do not stay nearby trying to diagnose the batch by smell. [[5]](https://www.cdc.gov/chemical-emergencies/chemical-fact-sheets/chlorine.html)

## 6. Calibration: make the machine predictable

The first successful batch is not yet a recipe. The recipe is the combination of **one generator + one cell + one water source + one salt + one starting formulation + one run time** that repeatedly produces the measured result.

Use this calibration sequence:

1. Keep volume, water, salt, vinegar, temperature, and generator unchanged.
2. Start at 10 minutes if the device permits the starting formulation.
3. Measure FAC and pH.
4. Change only the time on the next fresh batch. Use a modest change—usually a 2-minute step or no more than roughly 25–50% longer than the previous run.
5. Measure again. Record a table such as `8 min → 92 ppm`, `10 min → 118 ppm`, `12 min → 148 ppm`, `14 min → 183 ppm`, `16 min → 214 ppm`. These are illustrative calibration data, not predictions.
6. Repeat the chosen setting two or three times and record **both FAC and final pH**. A chlorine cluster such as 193 / 207 / 199 ppm with all final pH readings in the same working band is repeatable enough for a low-stakes home experiment; 80 / 260 / 145 ppm or pH values that cross multiple bands means the process is not controlled.
7. Recheck periodically. Electrode wear, scaling, water composition, strip aging, temperature, and power supply can shift output.

If FAC is low, do **not** change salt, vinegar, volume, and time all at once. If pH is high, do **not** pour vinegar into the finished batch; use only a documented next-batch adjustment that the device manual allows, or choose a device with better pH/concentration control. The [planner](hypochlorous_water_planner.html) gives a conservative next-time estimate from your measured result, but it labels that output as an estimate and still requires a fresh batch and a new test.

If the **planned volume changes**, treat the calibrated run as a reference rather than pretending it is the same recipe outcome. Keep the reference volume, reference time, and measured reference FAC linked together; scale the proposed time by the volume ratio; then test the new batch. For example, moving from a measured 500 mL run to 1,000 mL at the same FAC target approximately doubles the starting time estimate under the constant-current model. The new 1,000 mL batch does not inherit the reference batch's pH or confidence label until it is measured.

## 7. Dilution math when FAC is too high

Once chlorine is already generated, dilution is more predictable than trying to stop electrolysis at an exact second.

```text
C1 × V1 = C2 × V2
final volume = (measured FAC × current volume) / target FAC
water to add = final volume − current volume
```

Examples for a target of 200 ppm:

| Measured batch | Current volume | Add distilled water | Approx. final volume |
|---:|---:|---:|---:|
| 250 ppm | 500 mL | 125 mL | 625 mL |
| 300 ppm | 500 mL | 250 mL | 750 mL |
| 400 ppm | 500 mL | 500 mL | 1,000 mL |
| 500 ppm | 500 mL | 750 mL | 1,250 mL |
| 600 ppm | 500 mL | 1,000 mL | 1,500 mL |

After dilution, measure FAC and pH again. FAC should follow the volume math approximately; pH does not have to change linearly. If the diluted solution is still outside the QC window, do not keep improvising.

## 8. Pillowcase use: what is reasonable to infer

The strongest relevant evidence I found is a laboratory study on rayon sheets. It tested slightly acidic HOCl water at 50 and 100 ppm, with spray exposure and a further wet-contact period. The 100 ppm condition performed materially better than 50 ppm on rayon, but this was not a cotton pillowcase, not a home-use study, and not an acne trial. [[4]](https://pmc.ncbi.nlm.nih.gov/articles/PMC4976267/)

If you choose to explore the fabric idea anyway:

1. **Launder first.** HOCl is reactive and is consumed by skin oil, sweat, proteins, dead skin, and product residue. Spraying is not washing and should never become a reason to stop changing pillowcases.
2. **Start with one inexpensive, white or colorfast pillowcase.** Follow the care label and test a hidden seam for discoloration. Chlorine chemistry can bleach some fabrics and damage dyes.
3. **Use a measured, mildly acidic batch, not a pool chemical.** The experimental target is 150–250 ppm FAC at pH 5.0–6.5; the evidence does not establish that 200 ppm is necessary or optimal.
4. **Use even coverage.** The face-contact region should be uniformly damp, not just hit with two perfume-like spritzes from far away. Do not saturate the pillow, mattress, foam, or electrical bedding.
5. **Treat contact time as an extrapolation.** The rayon study used minutes of spray exposure plus 5 minutes of wet contact in a controlled box. It did not validate a home pillowcase procedure. If you copy the general idea, keep the fabric visibly damp for several minutes, then let it dry completely before sleeping on it.
6. **Stop if there is odor, bleaching, residue, or irritation.** Do not sleep on fabric that smells strongly of chlorine or remains wet.
7. **Do not claim an acne result.** There is no controlled study showing that nightly 200 ppm HOCl on a pillowcase reduces acne by a known percentage. Any improvement would be an individual observation with many confounders.

For a normal household goal, my order of preference remains: regular laundering and clean pillowcases first; a measured fabric experiment only as an optional adjunct; no pool tablets, bleach, or unknown concentrated generator output.

## 9. Face use in a future spray bottle

I would not make the DIY batch your first facial spray. The decisive gap is not merely FAC or pH. A consumer skin product also needs control over raw-material identity, electrode contamination, microbial quality, packaging, stability, eye/skin irritation, and the actual labeled use.

For a future face trial, choose a finished product that:

- explicitly says face, dermal, or skin use;
- lists water, sodium chloride, and hypochlorous acid without fragrance or essential oils;
- gives a pH and preferably a concentration or active-ingredient statement;
- has a batch/expiration or stability statement and a reputable manufacturer;
- comes in a light-protective, clean spray package;
- is patch-tested before full-face use.

The current manufacturer pages I checked include several examples: Prequel Universal Skin Solution lists face/body use, three simple ingredients, pH 5.5 ±, and a $17 4-oz bottle; Briotech Topical Skin Spray lists 0.014% / 140 ppm HOCl and pH 4.0–5.2, although the U.S. product page showed sold out at the time checked; Tower 28 SOS lists face use, three simple ingredients, and pH 4.5. These are manufacturer claims, not independent comparative proof. [[12]](https://prequelskin.com/products/universal-skin-solution-hypochlorous-acid-spray)[[13]](https://shopbriotech.com/products/topical-skin-spray)[[14]](https://www.tower28beauty.com/products/sos-daily-facial-rescue-spray)

If you try a finished facial spray:

1. Patch test a small area for a day or two.
2. Apply to clean, dry skin according to the product label.
3. Let it dry before moisturizer or another active.
4. Do not mix it in the bottle with acids, peroxide, bleach, ammonia, retinoids, or other products.
5. Avoid deliberate inhalation and do not spray directly into the eyes unless the product is specifically labeled for that use.
6. Rinse and stop if it burns, causes persistent redness, worsens a rash, or produces respiratory/eye symptoms.
7. Treat it as a calming/hygiene adjunct, not a replacement for diagnosis or evidence-based acne, rosacea, eczema, or wound care.

## 10. Which product should you buy?

### My recommendation for your exact plan

**If you want to make the water yourself:** the best match I could verify is the **Ecoloxtech Eco One** rather than the tiny PWPAM unit. The Eco One page states that it uses a titanium electrolysis cell, includes free-chlorine and pH test paper, supports measurements up to 500 ppm with a dilution step, and is listed at $199.99 when checked on 2026-08-22. It still is not a facial-safety certification; you would use it as a measured DIY generator for the pillowcase experiment and continue to buy a finished facial spray for your skin. [[10]](https://store.hocl.com/ecoone/)

**If you want the simplest face path:** buy a current, skin-labeled finished product such as **Prequel Universal Skin Solution**; I would not buy a generator for face use until you have a strong reason to accept the extra measurement and contamination burden. [[12]](https://prequelskin.com/products/universal-skin-solution-hypochlorous-acid-spray)

**If you want a low-cost hardware experiment:** the **PWPAM B08SMD6WRF** is inexpensive and includes a chlorine strip, but I do **not** recommend it for your intended dual-use plan. Its live Amazon listing calls it a sodium-hypochlorite generator, gives 300–1,000 ppm cleaning recipes, says to rinse after skin contact, and tells users to leave the area after high-concentration spraying. That is exactly the wrong product identity for “I want to make a gentle face spray later.” [[11]](https://www.amazon.com/dp/B08SMD6WRF)

| Product | What it is good for | Why I would / would not choose it |
|---|---|---|
| **Ecoloxtech Eco One** | Measured DIY salt-water generation | Best balance of documented cell, pH/FAC testing, and concentration workflow; still a DIY cleaner system, not a facial product. |
| **Hypo 7.5** | Higher-throughput generation with preset 200/500 ppm modes | Technically convenient but $2,199 and makes 7.5 L; extreme overkill for a pillowcase experiment. [[9]](https://store.hocl.com/hypo) |
| **Force of Nature appliance** | EPA-registered 220 ppm cleaner for hard, non-porous surfaces | Good if your goal changes to household surfaces; its label is not a facial or pillowcase authorization. It uses single-use activator capsules and says to discard after 14 days. [[6]](https://www3.epa.gov/pesticides/chem_search/ppls/094363-00001-20210505.pdf) |
| **PWPAM B08SMD6WRF** | Cheap sodium-hypochlorite cleaning experiment | Not recommended for face; no pH workflow and its own listing directs users toward higher cleaning concentrations and skin rinsing. [[11]](https://www.amazon.com/dp/B08SMD6WRF) |
| **Prequel / Briotech / Tower 28 facial sprays** | Future facial use | Preferable for the face because they are sold and labeled as skin products; do not assume their facial label transfers to pillowcase disinfection. [[12]](https://prequelskin.com/products/universal-skin-solution-hypochlorous-acid-spray)[[13]](https://shopbriotech.com/products/topical-skin-spray)[[14]](https://www.tower28beauty.com/products/sos-daily-facial-rescue-spray) |

### Why not chlorine tablets?

Chlorine tablets are designed for dosing pools or emergency water treatment, where the label controls the amount, water volume, contact time, pH, and intended route. The active chemistry may be calcium hypochlorite, sodium dichloroisocyanurate, trichloroisocyanuric acid, or another product-specific compound. They may contain stabilizers or leave residues that are irrelevant or undesirable for a face spray. [[1]](https://www.cdc.gov/infection-control/hcp/disinfection-sterilization/chemical-disinfectants.html)[[7]](https://www.poison.org/articles/pool-chemical-safety-192)

They also create a much worse handling problem: concentrated tablets can irritate skin and lungs, bleach fabric, corrode materials, and react dangerously with acids. Never combine them with vinegar, bleach, ammonia, peroxide, or an electrolyzed-water batch.

## 11. Storage and discard rules

HOCl/electrolyzed water loses FAC through chlorine volatilization and chemical decomposition. Closed, dark, cool storage is better than an open, warm, light-exposed container, but no generic home-batch shelf life can be assumed. Studies found faster losses in open or light-exposed conditions, and product labels vary: the PWPAM listing says one week sealed, while Force of Nature's EPA-labeled solution says 14 days in its approved bottle. [[6]](https://www3.epa.gov/pesticides/chem_search/ppls/094363-00001-20210505.pdf)[[8]](https://pubmed.ncbi.nlm.nih.gov/26869019/)[[9]](https://store.hocl.com/hypo)

For an unvalidated DIY batch, I would:

- make 250–500 mL while calibrating;
- use an opaque, closed bottle and minimize headspace/openings;
- label the batch and keep it cool and dark;
- recheck FAC if keeping it beyond a few days;
- discard if FAC falls below your chosen working range, pH drifts materially, the liquid changes color, particles appear, or odor becomes irritating;
- never claim months of shelf life based on clear appearance or a mild smell.

## Evidence gaps

- No controlled clinical study was found showing that DIY 150–250 ppm HOCl sprayed on a pillowcase improves acne, rosacea, eczema, or skin texture.
- The relevant porous-surface study used rayon sheets and laboratory bacterial inocula, not cotton bedding loaded with sebum, cosmetics, and sweat.
- A high-range chlorine strip is practical but less precise than laboratory spectrophotometry or a validated DPD method; it does not identify HOCl separately from OCl⁻.
- A pH/FAC pass does not prove sterility, electrode-material purity, absence of chlorate/other byproducts, or long-term stability.
- Current product pricing, stock, packaging, and formulas can change; the product comparison is a dated snapshot captured 2026-08-22.

## Sources

1. CDC, [Chemical Disinfectants](https://www.cdc.gov/infection-control/hcp/disinfection-sterilization/chemical-disinfectants.html) — hypochlorite forms, fabric bleaching/corrosion, organic-load effects, and chlorine-gas warning when mixed with acid or ammonia.
2. Farah RI and Al-Haj Ali SN, [Electrolyzed Water Generated On-Site as a Promising Disinfectant in the Dental Office During the COVID-19 Pandemic](https://pmc.ncbi.nlm.nih.gov/articles/PMC8119747/) — 2 g/L salt + 5 mL 5% vinegar starting method, roughly 10-minute electrolysis, FAC/pH verification, and equipment dependence.
3. Ampiaw RE et al., [Electrolyzed water as a disinfectant: A systematic review of factors affecting the production and efficiency of hypochlorous acid](https://doi.org/10.1016/j.jwpe.2021.102228) — water/electrolyte properties, electrode material, current, storage, pH, and production variability.
4. [Inactivation of bacteria on surfaces by sprayed slightly acidic hypochlorous acid water](https://pmc.ncbi.nlm.nih.gov/articles/PMC4976267/) — 50/100 ppm, pH 6, glass vs rayon, spray duration, and the limitation of porous surfaces.
5. CDC, [Chlorine](https://www.cdc.gov/chemical-emergencies/chemical-fact-sheets/chlorine.html) — respiratory/eye irritation, exposure symptoms, and leaving/ventilating after chlorine exposure.
6. U.S. EPA, [HOCl 180 label, EPA Reg. No. 94363-1](https://www3.epa.gov/pesticides/chem_search/ppls/094363-00001-20210505.pdf) — 0.018% active ingredient, hard non-porous surface directions, 2-minute wet contact, incompatibility with acids/hydrogen peroxide, and storage language.
7. CDC, [What to know about chlorine safety](https://www.poison.org/articles/pool-chemical-safety-192) — pool tablet categories, concentrated chemical handling, and skin/eye/respiratory cautions.
8. Xuan X-T et al., [Storage Stability of Slightly Acidic Electrolyzed Water and Circulating Electrolyzed Water](https://pubmed.ncbi.nlm.nih.gov/26869019/) — storage in open/closed and light/dark conditions and changes in available chlorine, pH, and ORP.
9. Hypochlorous Acid Water, [Hypo 7.5 generator product page](https://store.hocl.com/hypo) — manufacturer-stated 7.5 L capacity, 200/500 ppm modes, run times, price, and included strips; marketing/product evidence, not independent validation.
10. Ecoloxtech, [Eco One Portable Hypochlorous Acid Generator](https://store.hocl.com/ecoone/) — manufacturer-stated titanium cell, testing workflow, pH guidance, current product price, and included test papers; marketing/product evidence.
11. Amazon, [PWPAM Sodium Hypochlorite Generator, ASIN B08SMD6WRF](https://www.amazon.com/dp/B08SMD6WRF) — current product identity, 5 V/10 W/titanium listing, included strip, cleaning concentration recipes, skin-rinse warning, and ventilation instruction.
12. Prequel, [Universal Skin Solution Hypochlorous Acid Spray](https://prequelskin.com/products/universal-skin-solution-hypochlorous-acid-spray) — current face/body positioning, pH 5.5 ±, ingredients, use instructions, and price.
13. Briotech, [Topical Skin Spray](https://shopbriotech.com/products/topical-skin-spray) — current face/body positioning, stated 0.014% / 140 ppm HOCl, pH 4.0–5.2, ingredients, and product availability snapshot.
14. Tower 28, [SOS Daily Rescue Facial Spray](https://www.tower28beauty.com/products/sos-daily-facial-rescue-spray) — current facial positioning, pH 4.5, ingredients, and skin-organization recognition claims; manufacturer evidence.
