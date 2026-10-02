# Recipes and prototype worksheets

*Compiled 2026-08-15. These are conservative educational worksheets, not medical prescriptions or validated shelf-stable cosmetic formulas. Use one active at a time, patch test, and stop for persistent burning, swelling, rash, blistering, or worsening pigmentation.*

## 0. Bottom line

The safest DIY recipe is the one with the fewest moving parts and the shortest storage time. Start with **one ingredient, one goal, one small batch, one measured pH, and one discard rule**. Do not attempt to recreate a commercial multi-active serum by combining powders in a dropper bottle.

## 1. Worksheet A — fresh L-ascorbic-acid test solution

This is the only recipe in this topic that earns a “first candidate” label. It is a learning batch, not an exact copy of C E Ferulic and not a shelf-stable serum. The classic absorption study found LAA delivery below pH 3.5; the existing [vitamin C protocol](../08_vitamin_c_serums/index.html#doc3) contains the archive's more detailed vitamin C discussion. [[1]](https://pubmed.ncbi.nlm.nih.gov/11207686/)

### Target

| Component | 10 g test batch |
|---|---:|
| L-ascorbic acid powder | 1.00 g |
| Distilled/deionized water | 9.00 g |
| Preservative | **None in this learning worksheet** |
| Target pH | Measure; do not guess. A classic LAA delivery target is below pH 3.5, but lower is not automatically better for tolerance. |

### Method

1. Verify the powder identity, lot, and expiry; do not use food powder with unknown contaminants or flavoring.
2. Clean and dry the tools and container. Weigh both ingredients by mass.
3. Dissolve the powder in the water. Do not add baking soda “until it feels right.”
4. Measure pH after the powder is fully dissolved and the solution has equilibrated. If you cannot measure pH, do not treat the batch as a controlled formulation.
5. Make a single-use aliquot or discard the remainder rather than storing a multi-use dropper bottle.
6. Apply only to intact skin after a patch test. Keep it away from eyes, lips, broken skin, and immediately after devices or exfoliating acids.

### What this does not prove

- It does not prove a specific percentage remains after storage.
- It does not measure LAA versus dehydroascorbic acid.
- It does not reproduce the C E Ferulic solvent, vitamin E, ferulic-acid, preservative, packaging, or manufacturing system.
- Refrigeration does not make an unpreserved water batch safe for repeated use.

## 1A. The user's adjustable Vitamin C worksheet

Use the [Vitamin C recipe scaler](vitamin_c_recipe_scaler.html) to select **finished LAA-equivalent % w/w**, starting water amount, and target pH. The default is now **20% w/w after estimated CO₂ loss**, with **15.84 g starting water** and **target pH 3.30**. All concentration presets use this finished-mass basis.

| Quantity | Unrounded model amount | Displayed amount |
|---|---:|---:|
| L-ascorbic acid | 3.986905 g | **3.99 g** |
| Initial baking-soda estimate | 0.226041 g | **0.23 g** |
| Distilled water | 15.84 g | **15.84 g** |
| Estimated mass after CO₂ loss | 19.934527 g | **19.93 g** |
| LAA-equivalent concentration | 20% w/w | **20.00% w/w** |

The model solves `LAA = water × w / (1 − w × (1 + k × (1 − 44.01/84.007)))`, where `w` is the target mass fraction and `k` is bicarbonate grams per gram LAA from the pH model. At pH 3.30 and pKa₁ 4.17, `k ≈ 0.056696`. Rounded weighed quantities will differ slightly from the unrounded model; weigh the finished mixture and measure pH. The target is total acid plus ascorbate expressed as LAA-equivalent, not an assay of potency or un-ionized acid. [Chemical-property reference](https://pubchem.ncbi.nlm.nih.gov/compound/54670067).

### Formula audit and default update — 2026-09-06

The old 3.168 g LAA / 15.84 g water recipe gave approximately 16.592% w/w after estimated gas loss. At the user's request, the scaler now increases LAA and its associated bicarbonate estimate to reach 20% of estimated finished mass. It no longer preserves the old powder-to-water loading convention. At pH targets 3.00, 3.30, and 3.50, the new 20% default estimates respectively **0.12, 0.23, and 0.34 g bicarbonate**.

The ideal acid/base model still neglects activity effects and the small free-H⁺ charge-balance correction. Actual final volume, retained CO₂, assay, evaporation and measurement error remain uncalibrated. Final pH must be measured after dissolution and degassing. The cited pig-skin study supports delivery below pH 3.5; choosing % w/w here does not establish that every study's “20%” shares this exact concentration basis or vehicle. No home-serum safety, potency or shelf life was validated. [Audit source notes](source_docs/research_resource_log_2026-09-06.txt).

### Timing and measurement notes

- Use the experimental LAA batch in the **morning** and keep Differin/adapalene in the **evening**. Do not introduce the DIY batch and another exfoliating acid at the same time.
- A 0–6 pH strip is more useful than a 0–14 strip for this acidic range, but a narrower 2.8–4.4 strip or a properly calibrated meter gives better resolution. The target strip color does **not** need to be green; green generally indicates a more neutral reading, not the acidic LAA range.
- A plain, identity-labeled L-ascorbic-acid powder with a lot number, expiry, assay/COA, and cosmetic or pharmaceutical quality is the appropriate raw-material profile. Do not order an unknown powder merely because its marketing color looks right. A green, blue, gray, or strongly off-color powder is a reason to pause and verify identity rather than correct it with pH or baking soda.
- This remains an unpreserved water batch. Use a clean small container, minimize repeated dropper contact, protect it from heat/light/air, and treat it as a short-lived experiment. Refrigeration slows oxidation but does not establish microbial safety or shelf life. [[7]](https://www.fda.gov/cosmetics/potential-contaminants-cosmetics/microbiological-safety-and-cosmetics)
- Bicarbonate is not a preservation system. Aqueous ascorbate solutions have measurable buffer capacity and still require experimental stability control; the pH target does not establish potency or microbial shelf life. [[10]](https://pmc.ncbi.nlm.nih.gov/articles/PMC10552410/)

## 2. Worksheet B — glycolic acid decision template

Glycolic acid has human evidence at 5% in a cream and an FDA consumer framework of ≤10% with final pH ≥3.5 and sun-protection directions. [[2]](https://pubmed.ncbi.nlm.nih.gov/9598014/)[[3]](https://www.fda.gov/cosmetics/cosmetic-ingredients/alpha-hydroxy-acids)

I would not recommend a first-time home user make a multi-use glycolic-acid toner from crystals. The correct worksheet is:

| Required input | Must be known before mixing |
|---|---|
| Raw material | cosmetic-grade glycolic acid with known assay and impurities |
| Acid equivalent | calculated from assay; do not assume “5% powder” means “5% free acid” after neutralization |
| Final pH | measured after complete mixing; a plausible learning band is 3.5–4.0, not an unmeasured guess |
| Vehicle | a compatible water/gel/emulsion system, not tap water |
| Preservation | a complete preservative system at supplier-recommended pH and use level, ideally challenge-tested |
| Exposure | small area, low frequency, no same-night retinoid/Tria/other acid |
| Storage | opaque, low-touch, documented; discard if no validated shelf life |

### Practical recommendation

Buy a finished glycolic-acid product with disclosed concentration, pH, directions, and packaging unless you already have a calibrated pH meter, mass-based formulation process, compatible base, and preservation knowledge. The archive's [glycolic-acid topic](../18_glycolic_acid_topicals/index.html#doc1) explains the evidence and routine fit.

## 3. Worksheet C — niacinamide/NAG educational prototype

Published studies support 4–5% niacinamide for appearance of aging, blotchiness, and pigmentation, and 2% NAG has a small split-face pigmentation study; one study reported greater effect with 4% niacinamide + 2% NAG. These are finished formulations, not proof that any water mixture will behave the same way. [[4]](https://pubmed.ncbi.nlm.nih.gov/16029679/)[[5]](https://pubmed.ncbi.nlm.nih.gov/17348991/)[[6]](https://pubmed.ncbi.nlm.nih.gov/19845667/)

| Component | Educational target for a **single-use** test |
|---|---:|
| Niacinamide | 4% w/w |
| N-acetyl glucosamine | 2% w/w |
| Distilled/deionized water or finished neutral gel base | q.s. to 100% |
| Final pH | mildly acidic-to-neutral; measure and follow raw-material/base specifications |
| Preservation | none in a single-use test; validated system required for multi-use |

This is lower chemical risk than a low-pH acid, but it is still a water product. Do not make a month-sized bottle. A ready-made preserved product is more reproducible.

## 4. Worksheet D — HA hydration experiment

HA is best treated as a dispersion exercise, not a “strong active” recipe. If a learning experiment is done at all, use a tiny amount of a known sodium-hyaluronate grade and a preserved base designed for it. The exact use level depends on molecular weight and supplier specification; a generic percentage cannot be safely copied across powders.

Avoid:

- sprinkling dry HA directly onto the face;
- estimating a pinch or scoop;
- mixing into a full bottle of water without a preservative;
- assuming high molecular weight and low molecular weight HA are interchangeable;
- using a post-procedure, broken, or infected skin surface.

## 5. Combinations to avoid in a first experiment

- LAA + glycolic acid in one batch: no clear benefit, more pH/irritation/stability complexity.
- Glycolic acid + salicylic acid: more exfoliation burden and no need for a DIY stack.
- LAA + copper peptide or metal-containing actives: redox/compatibility uncertainty.
- Any powder serum + Tria, microneedling, or RF microneedling on the same session: exposure and barrier risk change after procedures.
- Any DIY active + a new retinoid at the same time: attribution becomes impossible and irritation risk rises.

## 6. Stop rules

Stop and rinse if there is intense burning, swelling, hives, blistering, eye exposure, or pain that persists. Stop the experiment if irritation is followed by darkening, because inflammation can create or worsen post-inflammatory hyperpigmentation. Seek medical advice for persistent dermatitis, facial swelling, eye symptoms, or a rapidly changing pigmented lesion.

### Sources

1. Pinnell SR et al. https://pubmed.ncbi.nlm.nih.gov/11207686/ — LAA pH/delivery context.
2. Thibault P et al. https://pubmed.ncbi.nlm.nih.gov/9598014/ — 5% glycolic human trial.
3. FDA AHA page. https://www.fda.gov/cosmetics/cosmetic-ingredients/alpha-hydroxy-acids — pH/concentration/sun warning.
4. Bissett DL et al. https://pubmed.ncbi.nlm.nih.gov/16029679/ — 5% niacinamide clinical study.
5. Bissett DL et al. https://pubmed.ncbi.nlm.nih.gov/17348991/ — 2% NAG study.
6. Bissett DL et al. https://pubmed.ncbi.nlm.nih.gov/19845667/ — 4% niacinamide + 2% NAG combination study.
7. U.S. FDA. https://www.fda.gov/cosmetics/potential-contaminants-cosmetics/microbiological-safety-and-cosmetics — contamination routes and why preservation/storage matter.
8. PubChem. https://pubchem.ncbi.nlm.nih.gov/compound/54670067 — L-ascorbic-acid molecular weight, pKa references, and aqueous pH entries.
9. PubChem. https://pubchem.ncbi.nlm.nih.gov/compound/Sodium-bicarbonate — sodium-bicarbonate molecular weight and aqueous alkalinity reference.
10. Stability of aqueous solutions of ascorbate for basic research and for intravenous administration. https://pmc.ncbi.nlm.nih.gov/articles/PMC10552410/ — experimental buffer-capacity and stability-control context; not a topical shelf-life study.
