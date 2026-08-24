# Peptide Formula Ingredient Audit and Concentration Estimator

*Audited 2026-08-14. This is a formulation and value model, not a finished-product assay, manufacturer invoice, efficacy ranking, or estimate of total cost of goods.*

## 0. Bottom line

The prior 25-product scan was incomplete at the ingredient level. The audit now contains **150 product–ingredient records**: **149 peptide, protein, or peptide-complex lines** plus one adjacent PDRN/Sodium DNA line that is retained for context but excluded from peptide-mass totals.

The largest corrections were not cosmetic:

- **Peach & Lily Copper Peptide Pro** contains 13 peptide lines, not only its 0.2% copper-peptide headline.
- **Theramid Copper Peptide** has 18 peptide-like lines in the current North American formula; a shorter regional formula also exists, so region and access date matter.
- **Theramid Derma-Peptides** and **Medik8 Liquid Peptides Advanced MP** each resolve to 13 peptide/protein INCI lines.
- **Paula's Choice Pro-Collagen Booster** resolves to six current peptide INCI identities.
- **COSRX The 6 Peptide Skin Booster** and **COSRX Blue Peptide Bakuchiol** now name all six peptide lines rather than using a generic “six peptides” label.
- **NIOD CAIS3** was missing Tripeptide-29 and had simplified Trifluoroacetyl Tripeptide-2 to a different name.
- **Allies of Skin** currently advertises a 1% “Copper Tripeptide Complex,” but its current INCI does not visibly identify Copper Tripeptide-1. The estimator therefore treats that headline as an opaque complex, not confirmed GHK-Cu.

The new [formula audit and concentration explorer](peptide_formula_audit.html) sorts the 25 products by bottle price, price per mL, estimated purchased peptide-technology mass, retail dollars per gram of that technology, estimated active-equivalent peptide mass, disclosure support, or ingredient count. Every product opens into an ingredient-level table with the low/base/high concentration, estimated bottle amount, basis, and source links.

## 1. What the amount columns mean

The low/base/high columns are **amount scenarios**, not ingredient-price estimates:

- **Low** is a conservative plausible formula loading.
- **Base** is the most likely working estimate from the evidence available.
- **High** is a plausible upper sensitivity case, not a confidence bound.

Two different amount concepts are shown because they answer different questions.

### Active-equivalent peptide mass

This estimates the mass of the peptide molecule itself. For a roughly water-density formula:

```text
active peptide mg in bottle ≈ bottle mL × final active percentage × 10
```

For example, 0.005% Acetyl Hexapeptide-8 in a 30 mL bottle is approximately 1.5 mg.

### Purchased peptide-technology mass

This estimates the grams of the raw premix, solution, suspension, or complex added by the formulator, carrier included:

```text
purchased technology g ≈ bottle mL × technology percentage ÷ 100
```

A 30 mL bottle containing 3% Matrixyl 3000 therefore has about 0.9 g of purchased Matrixyl 3000 technology. It does **not** have 0.9 g of pure Palmitoyl Tripeptide-1 plus Palmitoyl Tetrapeptide-7.

### Why both are necessary

The molecule view lets us compare claimed peptide mass. The purchased-technology view is closer to what a formulator weighs into a batch and is therefore more useful for ingredient-economics work. Neither is an efficacy-equivalent dose: one milligram of a growth factor, lipopeptide, expression peptide, and copper peptide cannot be assigned the same biological value.

## 2. Concentration estimation hierarchy

Every line receives the strongest applicable method. Retail price is never an input.

| Priority | Amount method | Example | What remains uncertain |
|---:|---|---|---|
| 1 | Published final-formula concentration | Good Molecules 25/25/5 ppm; NIOD 1% + 1% | Claim wording, assay method, regional formula |
| 2 | Published commercial-technology percentage × a supplier/patent assay | Matrixyl 3000; Matrixyl Synthe'6; Argireline solution | Whether the brand uses the same grade/version |
| 3 | Published complex percentage with undisclosed component assay | Medik8 30%; GF15 15%; BIO GF Complex 8% | Pure peptide/protein fraction and component split |
| 4 | Manufacturer use-rate scenario for the matching material class | COSRX six-peptide formula; DERMA E | Exact supplier, suspension strength, and use rate |
| 5 | Broad material-class prior constrained by the INCI and formula context | Unnamed late-list peptides | Nearly all molecule-level detail |

The FDA requires cosmetic ingredients to be declared generally in descending order, but ingredients at 1% or less can be listed in any order after the ingredients above 1%. That makes INCI order a weak constraint for most peptides, not a measuring instrument. It supports wide priors and consistency checks; it does not support false decimal precision. [FDA cosmetic labeling summary](https://www.fda.gov/cosmetics/cosmetics-labeling-regulations/summary-cosmetics-labeling-requirements)

## 3. Supplier-assay conversions used in the model

These examples show why a headline percentage cannot automatically be read as pure peptide.

### Argireline solution

A published Argireline technical document describes the solution as 0.05% Argireline powder and recommends 3–10% of that solution in a finished formula. A 10% finished-formula use level therefore corresponds to approximately **0.005% Acetyl Hexapeptide-8**, or **1.5 mg in 30 mL**. [Argireline technical information](https://doctorsheltonsolution.com/special/compliance/studies/arg-4.pdf)

### Matrixyl 3000

The Matrixyl 3000 patent example identifies approximately 0.01% Palmitoyl Tripeptide-1 and 0.005% Palmitoyl Tetrapeptide-7 in the commercial technology. At 3% Matrixyl 3000 in a finished formula, that becomes approximately **0.0003% PT-1** and **0.00015% PT-7**. [Matrixyl 3000 patent composition](https://patents.google.com/patent/US6974799B2/lv)

### Matrixyl Synthe'6

A patent describing the commercial Synthe'6 material reports approximately 0.025% Palmitoyl Tripeptide-38 in the premix. At 2% Synthe'6, the final formula contains approximately **0.0005% PT-38**. [Synthe'6 composition](https://patentimages.storage.googleapis.com/9c/04/e9/84ccee710561e0/EP2732806A1.pdf)

### Undisclosed six-peptide formulas

For COSRX The 6 Peptide Skin Booster, the model starts from the six current INCI identities and uses matching supplier use-rate/assay classes where possible. It also constrains the total purchased peptide technologies to **0.15% / 1.0% / 4.0%** of the formula. The 150 mL bottle therefore contains an estimated **0.225 / 1.5 / 6.0 g** of purchased peptide technologies and **10.77 / 47.7 / 237 mg** of peptide active equivalents. This is deliberately broad. The base is a best estimate, not a published COSRX assay. [COSRX product and current INCI](https://www.cosrx.com/products/the-6-peptide-skin-booster-serum)

## 4. Audit corrections by product

| Product | Audited peptide lines | Important correction or limitation |
|---|---:|---|
| The Ordinary Multi-Peptide + HA | 7 | Historical 25.1% technology claim is retained only as a high scenario, not presented as current dose. |
| The Ordinary Multi-Peptide + Copper Peptides 1% | 8 | The 1% copper-peptide headline is separate from the seven other peptide lines and is conditionally modeled as Copper Tripeptide-1. |
| The Ordinary GF15 | 3 | Generic “growth factors” expanded to all three current Nicotiana-derived INCI names. |
| Good Molecules Copper Peptide + PDRN | 3 peptides + PDRN | Added Caprooyl Tetrapeptide-3 and Tridecapeptide-1; Sodium DNA is not counted as peptide mass. |
| Geek & Gorgeous Power Peptides | 6 | X50 expanded into Copper Palmitoyl Heptapeptide-14 and Heptapeptide-15 Palmitate. |
| Theramid Copper Peptide | 18 | Current North American formula expanded; regional formula variability flagged. |
| Theramid Derma-Peptides | 13 | Nine named commercial technologies expanded into their current peptide/protein INCI lines. |
| Medik8 Liquid Peptides Advanced MP | 13 | “30% multi-peptide complex” expanded into its current peptide/protein INCI lines. |
| Paula's Choice Pro-Collagen Booster | 6 | Generic six-peptide label replaced with all current INCI identities. |
| Minimalist Multi-Peptides 10% | 7 | Bio-Placenta expanded into five growth-factor INCI lines plus two Matrixyl peptides. |
| The INKEY List Collagen Peptide | 4 | Both SYN-TACKS component INCI lines added. |
| COSRX Blue Peptide Bakuchiol | 6 | All current peptide identities added. |
| COSRX The 6 Peptide Skin Booster | 6 | All current peptide identities added. |
| Drunk Elephant Protini | 9 | Blend expanded into nine peptide/protein lines. |
| Peach & Lily Copper Peptide Pro | 13 | Twelve non-copper peptides added to the prior copper-only representation. |
| NIOD CAIS3 | 6 | Tripeptide-29 added; Trifluoroacetyl Tripeptide-2 restored to its full identity. |
| Allies of Skin Copper Tripeptide & Ectoin | 2 modeled peptide technologies | Current INCI does not visibly confirm Copper Tripeptide-1; the 1% complex remains opaque. |

No additional peptide-identity omission was found in the current source used for the remaining rows. “No omission found” does not prove a formula has not changed; each row retains its current product source and access context in the dataset.

## 5. Value results

### Most useful transparent purchased-technology deals

The retail-per-technology-gram metric is the cleaner value screen when the technology percentage is published. On the base assumptions:

| Product | Estimated purchased technology | Retail per technology gram | Interpretation |
|---|---:|---:|---|
| Theramid Derma-Peptides 35% | 10.5 g | **$3.43/g** | Strongest disclosed multi-technology loading per retail dollar; pure-active fractions remain largely undisclosed. |
| The Ordinary Matrixyl 10% + HA | 3.0 g | **$3.63/g** | Excellent total technology value; the 6% Matrixyl 3000 / 4% Synthe'6 split is modeled. |
| Minimalist Multi-Peptides 10% | 3.0 g | **$4.33/g** | Strong disclosed 7% Matrixyl 3000 + 3% Bio-Placenta loading; growth-factor assay remains unknown. |
| Geek & Gorgeous Power Peptides | 2.7003 g | **$6.96/g** | Particularly interpretable because all four commercial technology percentages are published. |
| Timeless Matrixyl 3000 | 2.4 g | **$11.65/g** | Simple, high-confidence 8% single-technology comparison. |

Argireline 10% and GF15 15% also rank near the top by purchased-solution grams, but those grams are mostly carrier. They should not be interpreted as having more peptide molecules than the rows below them.

### What the active-equivalent ranking says

The active-equivalent ranking is dominated by the strongest copper claims:

1. **Theramid Copper Peptide 3%** if the 3% pure-copper-peptide claim is taken literally.
2. **The Ordinary Multi-Peptide + Copper Peptides 1%** if the 1% headline is treated as Copper Tripeptide-1 active.
3. **NIOD CAIS3** with published 1% GHK-Cu plus 1% GHK.
4. **Peach & Lily** with a published 0.2% copper-peptide headline.

This ranking is the most sensitive to claim semantics and grade identity. It is not appropriate to use a 1% GHK-Cu suspension price as though it were the price of 100% pure powder, and the model does not do that.

### Practical best-deal interpretation

- **Best disclosed multi-technology load per dollar:** Theramid Derma-Peptides, conditional on its current 35% technology claim.
- **Best fully itemized technology formula at a low price:** Geek & Gorgeous Power Peptides.
- **Best simple high-load Matrixyl benchmark:** Timeless Matrixyl 3000.
- **Best inexpensive modeled 10% technology bottle:** The Ordinary Matrixyl 10% + HA, with the split caveat.
- **Largest claimed pure copper load per retail dollar:** Theramid Copper Peptide, conditional on the 3% claim and North American formula.
- **Best exact ppm transparency control:** Good Molecules Super Peptide. Its high retail dollars per peptide milligram are a consequence of the tiny disclosed peptide mass, not proof that it is a bad finished product.

## 6. Assumptions that remain unresolved

1. Formula density is approximated as 1 g/mL.
2. Product websites can show different formulas or claims by region and can change without preserving a revision history.
3. “Peptide complex,” “growth-factor solution,” and named commercial technology percentages include carriers unless a source explicitly says otherwise.
4. The same INCI molecule can be purchased as pure powder, a standard suspension, a concentrated suspension, an encapsulate, or a proprietary blend. Those forms have different assays and costs.
5. The model assumes a supplier assay only when a named technology or a clearly labeled analogue supports it. It does not assume every brand bought the cited supplier's exact SKU.
6. For ingredients at 1% or less, INCI order may be arbitrary under U.S. labeling rules. Position therefore changes the prior only modestly.
7. Published product percentages may describe a technology, complex, or solution rather than pure peptide. Conditional claims are labeled.
8. Manufacturer recommended use rates describe plausible formulation practice, not evidence that a particular brand used the midpoint.
9. Low/base/high ranges are scenario bands, not statistical intervals.
10. Retail dollars per active milligram and retail dollars per technology gram do not compare efficacy, stability, delivery, packaging, testing, or non-peptide ingredients.
11. Sodium DNA/PDRN is retained in the Good Molecules audit because it is central to the product positioning, but it is excluded from peptide totals.
12. Manufacturer discounts, contract prices, minimum order quantities, wastage, freight, QC, formulation labor, filling, packaging, testing, and retailer margin are outside this amount model.

## 7. Data files and reproducibility

- [Audited ingredient-line dataset](data/peptide_formula_ingredient_audit.csv) — one row per product–ingredient identity with concentration, amount, basis, estimate class, and sources.
- [Product value summary](data/peptide_formula_value_summary.csv) — all 25 formulas with active-equivalent and purchased-technology scenarios plus sortable value metrics.
- [Public ingredient-price source ledger](data/peptide_price_source_records.csv) — 40 supplier, distributor, marketplace, research-grade, and no-price records kept separate by material form.
- [Formula price scenario dataset](data/peptide_price_scenario_model.csv) — the separate forward-cost model; it does not reverse-calculate from finished retail price.

The datasets are generated by `tools/build_peptide_formula_audit.py`. The interactive explorer consumes the generated CSVs directly.

## 8. Selected current formula sources

- [The Ordinary Multi-Peptide + HA](https://theordinary.com/en-us/multi-peptide-ha-serum-100613.html)
- [The Ordinary Multi-Peptide + Copper Peptides 1%](https://theordinary.com/en-us/multi-peptide-copper-peptides-1-serum-100625.html)
- [The Ordinary GF15](https://theordinary.com/en-us/gf-15-solution-growth-factors-serum-100702.html)
- [COSRX The 6 Peptide Skin Booster](https://www.cosrx.com/products/the-6-peptide-skin-booster-serum)
- [Peach & Lily Copper Peptide Pro](https://www.peachandlily.com/products/copper-peptide-pro-firming-serum)
- [Medik8 Liquid Peptides Advanced MP](https://us.medik8.com/products/liquid-peptides-advanced-mp)
- [Theramid Copper Peptide, North America](https://nichebeautylab.com/collections/bestseller-north-america/products/copper-peptide)
- [Theramid Derma-Peptides](https://nichebeautylab.com/collections/serums/products/derma-peptides)
- [NIOD CAIS3](https://niod.com/en-cv/copper-amino-isolate-serum-3-11-cais3-serum-100368.html)
- [Allies of Skin Copper Tripeptide & Ectoin](https://us.allies.shop/products/copper-tripeptide-ectoin-advanced-repair-serum)
