# Peptide Ingredient Price Finder and Retail-Comparison Scenario Model

*Compiled 2026-08-14. This is a procurement and formulation estimate, not a manufacturer invoice, finished-product COGS audit, medical claim, or efficacy ranking. Confidence describes the cost model, not the peptide’s clinical value.*

## 0. Bottom line

The ingredient-price research is now materially stronger, but it still cannot prove what most brands paid. The source-record ledger now contains **46 ingredient/material records** and explicitly separates formulation-grade inputs from research vials, pure-material cross-checks, and quote gaps.

The interactive cost comparison now displays **one best estimate per formulation**. Low/base/high fields remain only in the machine-readable audit as legacy sensitivity columns; they are no longer presented as three equally plausible answers.

The 25-formulation scenario model makes a forward estimate for every product by combining:

1. an observed or explicitly inferred formula amount;
2. a public price anchor for the same material, a clearly labeled analogue, or a deliberately wide inferred category band; and
3. `purchased material amount × unit price`.

It does **not** back-solve a price from the retail bottle. Retail price is shown only as an observed comparison point, and the retail multiple is `observed retail price ÷ modeled peptide/material input cost`.

The most defensible rows are Timeless Matrixyl 3000, Timeless Matrixyl Synthe’6, The INKEY List Collagen Peptide, and Good Molecules Super Peptide because their formula disclosure can be paired with a reasonably matched public material price. The least defensible rows are proprietary growth-factor blends, undisclosed multi-peptide serums, and formulas whose headline percentage refers to a complex rather than a pure peptide.

## 1. What changed from the earlier cost model

The older bottle model was useful for showing order of magnitude, but it mixed three different things: pure peptide powder, ready-to-use commercial suspension, and branded premix. This update keeps them separate.

### New source layers

| Layer | Meaning | Example |
|---|---|---|
| Direct supplier pack ladder | A public price for a named material at multiple sizes | Formulate Labs PT-1 suspension; Trulux Matrixyl 3000 |
| Distributor / formulator retail | A public price for a commercial technology sold to small formulators | The Herbarie SYN-TACKS |
| Marketplace bulk signal | A seller-listed quantity/price that may be useful as a floor but needs verification | GHK-Cu, PDRN, Matrixyl powder |
| Research-grade catalog | Historical context only; excluded from the product-cost model | ChemicalBook Tetrapeptide-21 vials, Biosynth Hexapeptide-9, lab recombinant proteins |
| No-price record | Identity/use documentation exists, but no matched public price is defensible | BIO GF Complex, Neøclair Pro, Matrixyl Morphomics |

The complete source ledger is [`data/peptide_price_source_records.csv`](data/peptide_price_source_records.csv). The earlier source-first discussion remains in [ingredient-by-ingredient peptide price research](08_peptide_ingredient_price_research.md).

## 2. Calculation rules

For each priced line:

```text
forward line cost = purchased material amount (g) × public or inferred unit anchor ($/g)
```

For a disclosed percentage, the working conversion is:

```text
amount (g) ≈ bottle volume (mL) × formula percentage ÷ 100
```

Density is approximated as 1 g/mL. This is smaller than the uncertainty created by undisclosed assay, carrier content, and supplier grade.

### Three different “amounts” are kept distinct

- **Pure active mass:** the molecule itself, such as 0.1% Copper Tripeptide-1.
- **Commercial technology mass:** the premix or complex, such as 3% Matrixyl 3000. The carrier is included in the priced material.
- **Ready-to-use suspension mass:** the grams of a supplier suspension added to a formula. The suspension may contain only 0.01–1% peptide, so its $/g cannot be treated as pure-peptide $/g.

### Legacy sensitivity columns

These are retained for audit history, not as the current reader-facing output:

- **Low:** larger-pack, lower-cost, or bulk/public-floor case where the source supports it.
- **Base:** the most useful visible small-to-mid-size formulator case, or a midpoint of the public pack ladder.
- **High:** small-lot, high-documentation, research-grade, or wide analogue case.

The interactive model selects one best heuristic estimate and labels its confidence. When there is no matched price, it uses a clearly italicized category estimate or marks the material as a quote gap.

## 3. Public price anchors from the expanded scan

The table shows the material price, not a pure-peptide-equivalent price unless the row explicitly says “pure powder.” Formulate Labs pages generally describe a carrier suspension with a selectable peptide strength, so their price is best used for a small or mid-size formulator buying a ready-to-use raw material.

| Material | Public $/g low / base / high | Form | Typical supplier-use clue | Price confidence |
|---|---:|---|---|---|
| Acetyl Hexapeptide-8 | $8.84 / $10.50 / $14.00 | Formulate Labs 0.05–0.5% suspension | 2–10% suspension input | High |
| Acetyl Octapeptide-3 | $67.40 / $80.10 / $106.80 | Formulate Labs 0.05–0.5% suspension | 2–10% input | High |
| Copper Tripeptide-1 | $0.80 / $0.95 / $1.25 | Formulate Labs 0.1–1% suspension | 0.01–0.1% pure-active typical | High |
| SYN-AKE INCI | $125.04 / $148.58 / $198.13 | Formulate Labs 0.05–0.5% suspension | 2–8% suspension input | High |
| Palmitoyl Tripeptide-1 | $8.83 / $10.50 / $14.00 | Formulate Labs 0.01–0.1% suspension | 1–10% input | High |
| Palmitoyl Tetrapeptide-7 | $6.44 / $7.65 / $10.20 | Formulate Labs 0.02–0.2% suspension | 1–10% input | High |
| Palmitoyl Tripeptide-5 | $7.64 / $9.08 / $12.11 | Formulate Labs 0.1–1% suspension | 1–3% input | High |
| Palmitoyl Tripeptide-38 | $4.63 / $5.48 / $7.33 | Formulate Labs 0.03–0.3% suspension | 2–10% input | High |
| Palmitoyl Tripeptide-8 | $44.93 / $53.40 / $71.20 | Formulate Labs 0.03–0.3% suspension | 1–5% input | High |
| Palmitoyl Pentapeptide-4 | $7.84 / $9.30 / $12.42 | Formulate Labs 0.05–0.5% suspension | 3–8% of standard suspension for 3–5 ppm active | High |
| Palmitoyl Hexapeptide-12 | $23.29 / $27.68 / $36.91 | Formulate Labs 0.01–0.1% suspension | 1–5% input | High |
| Pentapeptide-18 | $73.08 / $86.85 / $115.80 | Formulate Labs 0.05–0.5% suspension | 2–10% input | High |
| Tetrapeptide-21 | $50.56 / $60.08 / $80.11 | Formulate Labs 0.01–0.1% suspension | 1–5% input | High |
| Tripeptide-1 / GHK | $12.05 / $14.32 / $19.09 | Formulate Labs 0.01–0.1% suspension | 1–10% input | High |
| Caprooyl Tetrapeptide-3 | $7.64 / $9.08 / $12.11 | Formulate Labs 0.03–0.3% suspension | 0.3–2.5% input | High |
| Nonapeptide-1 | $19.69 / $23.40 / $31.20 | Formulate Labs 0.001–0.01% suspension | 1–5% input | High |
| Oligopeptide-68 | $64.63 / $76.80 / $102.40 | Formulate Labs 0.001–0.01% suspension | 2–10% input | High |
| EGF / sh-Oligopeptide-1 | $349 / $378 / $420 | Formulate Labs 0.08–0.8% refrigerated suspension | 1–10 ppm active | High, small-lot ceiling |
| Matrixyl 3000 | $1.14 / $2.31 / $2.70 | Trulux commercial premix | 3–8% premix | High |
| Matrixyl Synthe’6 | $1.27 / $2.53 / $2.95 | Trulux commercial premix | branded blend | High |
| SYN-COLL | $0.75 / $1.50 / $1.85 | Trulux commercial premix | branded blend | Medium |
| SYN-TACKS | $1.06 / $2.00 / $10.00 | The Herbarie commercial solution | 1% | High |
| X50 Antiaging | $0.67 / $0.75 / $0.83 | Commercial delivery premix | branded active | Medium |
| TEGO PEP 4-17 | **$2.18 selected** | Escentials 2,300 ppm branded cosmetic solution | 0.5–5% input | High |
| Progeline | **$1.00 selected** | New Directions commercial glycerin/water solution | 0.2–2% input | High |
| Collaxyl / Hexapeptide-9 | **$1.04 selected** | Bellahut water/glycerin cosmetic concentrate | 0.5–5% input | Medium |
| Sodium DNA / PDRN | **$10.00 selected** | Cosmetic powder marketplace category benchmark | 0.02–1% supplier guidance | Low |

Formula Labs source pages: [AHP-8](https://www.formulatelabs.ai/materials/acetyl-hexapeptide-8), [AO-3](https://www.formulatelabs.ai/materials/acetyl-octapeptide-3), [Copper Tripeptide-1](https://www.formulatelabs.ai/materials/copper-tripeptide-1), [SYN-AKE INCI](https://www.formulatelabs.ai/materials/dipeptide-diaminobutyroyl-benzylamide-diacetate), [PT-1](https://www.formulatelabs.ai/materials/palmitoyl-tripeptide-1), [PT-7](https://www.formulatelabs.ai/materials/palmitoyl-tetrapeptide-7), [PT-5](https://www.formulatelabs.ai/materials/palmitoyl-tripeptide-5), [PT-38](https://www.formulatelabs.ai/materials/palmitoyl-tripeptide-38), [PT-8](https://www.formulatelabs.ai/materials/palmitoyl-tripeptide-8), [PP-4](https://www.formulatelabs.ai/materials/palmitoyl-pentapeptide-4), [PH-12](https://www.formulatelabs.ai/materials/palmitoyl-hexapeptide-12), [PP-18](https://www.formulatelabs.ai/materials/pentapeptide-18), [TP-21](https://www.formulatelabs.ai/materials/tetrapeptide-21), [GHK](https://www.formulatelabs.ai/materials/tripeptide-1), [ChroNOline-class PT-3](https://www.formulatelabs.ai/materials/caprooyl-tetrapeptide-3), [Nonapeptide-1](https://www.formulatelabs.ai/materials/nonapeptide-1), [OP-68](https://www.formulatelabs.ai/materials/oligopeptide-68), and [EGF](https://www.formulatelabs.ai/materials/epidermal-growth-factor).

## 4. Retail comparison across all 25 formulations

The observed retail price is included so the reader can see the commercial multiple, but the model never uses retail price to choose an ingredient price. The full machine-readable table is [`data/peptide_price_scenario_model.csv`](data/peptide_price_scenario_model.csv).

| Formulation | Retail | Most-likely loading assumption | Modeled peptide/material input cost | Retail ÷ base input | Confidence |
|---|---:|---|---:|---:|---|
| The Ordinary Argireline Solution 10% | $9.70 / 30 mL | 3.0 g of 0.05% ARGIRELINE solution = 1.5 mg peptide; priced as 0.30 g of a potency-equivalent 0.5% public suspension | **$2.65–3.15–4.20** | 3.08× | Medium |
| The Ordinary Matrixyl 10% + HA | $10.90 / 30 mL | 6% Matrixyl 3000 + 4% Synthe’6 | **$3.58–7.18–8.40** | 1.52× | Medium |
| The Ordinary Multi-Peptide + HA | $19.90 / 30 mL | 7 named peptides; 0.05/0.20/0.80% total material | **$0.30–6.50–55.00** | 3.06× | Low |
| The Ordinary Multi-Peptide + Copper | $32.00 / 30 mL | 1% copper-peptide technology; pure fraction unknown | **$0.70–5.20–31.00** | 6.15× | Low |
| The Ordinary GF 15% Solution | $15.50 / 30 mL | 15% commercial GF solution | **$4.50–45.00–225.00** | 0.34× | Low |
| Good Molecules Super Peptide | $12.00 / 30 mL | 25/25/5 ppm exact disclosure | **$0.02–0.06–0.11** | 200× | High |
| Good Molecules Copper Peptide + PDRN | $12.00 / 30 mL | GHK-Cu indexed at 0.1%; PDRN and minor peptides estimated | **$3.28 best estimate** | 3.66× | Low |
| Geek & Gorgeous Power Peptides | $18.80 / 30 mL | 3% M3000 + 2% Synthe’6 + 4% TEGO + 0.001% X50 | **$4.18 best estimate** | 4.50× | High |
| Theramid Copper Peptide 3% | $49.00 / 30 mL | 3% GHK-Cu + 13% additional complex | **$4.62–20.36–79.10** | 2.41× | Low |
| Theramid Derma-Peptides 35% | $36.00 / 30 mL | Nine commercial technologies, all percentages stated | **$33.00–72.00–217.00** | 0.50× | Low |
| Medik8 Liquid Peptides Advanced MP | $95.00 / 30 mL | 30% unnamed multi-peptide complex | **$9.00–45.00–180.00** | 2.11× | Low |
| Paula’s Choice Pro-Collagen Booster | $59.00 / 20 mL | Six peptides; 0.05/0.25/1.00% total material | **$0.05–2.00–45.00** | 29.50× | Low |
| Naturium Multi-Peptide Advanced | $25.00 / 30 mL | Three named peptides; 0.01/0.05/0.25% total material | **$0.02–0.20–3.00** | 125× | Low |
| Minimalist Multi-Peptides 10% | $12.99 / 30 mL | 7% Matrixyl 3000 + 3% Bio-Placenta complex | **$3.30–10.25–23.70** | 1.27× | Low |
| The INKEY List Collagen Peptide | $17.00 / 30 mL | 1% Matrixyl 3000 + 1% SYN-TACKS | **$0.66–1.29–3.81** | 13.18× | Medium |
| Timeless Matrixyl 3000 | $27.95 / 30 mL | 8% Matrixyl 3000 | **$2.74–5.54–6.48** | 5.04× | High |
| Timeless Matrixyl Synthe’6 | $28.95 / 30 mL | 2% Matrixyl Synthe’6 | **$0.76–1.52–1.77** | 19.05× | High |
| COSRX Blue Peptide Bakuchiol | $27.00 / 50 mL | Six named peptides; 0.02/0.10/0.30% total material | **$0.05–1.50–12.00** | 18.00× | Low |
| COSRX 6 Peptide Skin Booster | $25.00 / 150 mL | Six named peptides; 0.02/0.10/0.30% total material | **$0.03–2.50–25.00** | 10.00× | Low |
| DERMA E Advanced Peptides | $31.95 / 30 mL | AHP-8 + PT-38; 0.01/0.05/0.20% total material | **$0.02–0.30–3.00** | 106.50× | Low |
| Drunk Elephant Protini | $72.00 / 50 mL | Nine peptides/growth factors; 0.04/0.16/0.40% total material | **$0.05–2.00–20.00** | 36.00× | Low |
| Peach & Lily Copper Peptide Pro | $49.00 / 30 mL | Official 0.2% copper-peptide headline | **$0.05–0.06–0.08** | 817× | High, conditional |
| NIOD CAIS3 | $72.00 / 15 mL | 1% GHK-Cu + 1% GHK | **$1.93–2.30–3.05** | 31.30× | High |
| Allies Copper Tripeptide & Ectoin | $199.00 / 30 mL | 1% + 2% + 2% peptide-complex headlines | **$6.10–8.40–14.80** | 23.69× | Low |
| Q+A Multi-Peptide | $13.00 / 30 mL | Four peptides; 0.03/0.10/0.30% total material | **$0.02–0.50–5.00** | 26× | Low |

### Worked quantity bridge: The Ordinary Argireline Solution 10%

The **10%** in the product name is treated as the amount of commercial ARGIRELINE solution, not 10% pure Acetyl Hexapeptide-8. The supplier technical sheet describes that solution as **0.05% peptide**. In a water-like 30 g bottle, the working estimate is therefore:

```text
30 g bottle × 10% commercial solution = 3.0 g commercial solution
3.0 g solution × 0.05% peptide assay = 0.0015 g = 1.5 mg peptide
1.5 mg peptide ÷ 0.5% assay = 0.30 g potency-equivalent Formulate Labs suspension
0.30 g × $8.84 / $10.50 / $14.00 per g = $2.65 / $3.15 / $4.20
$9.70 retail ÷ $3.15 base replacement cost = 3.08×
```

The Formulate Labs page supplies the public price ladder for its own **0.5% suspension**; it does not establish The Ordinary’s supplier or procurement price. The conversion to 0.30 g is necessary because pricing 3.0 g of the ten-times-stronger 0.5% material would overstate the replacement amount by 10×.

### How to interpret the extremes

- A **very high retail multiple** often means the formula has tiny disclosed peptide mass, cheap commercial premix, or a deliberately conservative input model. It is not proof of excess profit.
- A **retail multiple below 1×** usually means the scenario used a small-lot or high-documentation public price that the brand almost certainly does not pay at the same scale, or that the material is not matched to the branded complex.
- A **blank or low-confidence ingredient line** is more informative than a fabricated total. The model shows where a supplier quote, TDS, COA, or finished-product assay would change the result.

## 5. Itemized concentration assumptions by formulation

The following are the actual working assumptions behind the summary table. Percentages are final-formula percentages of either pure active, commercial premix, or purchased suspension as labeled. “Amount” is the corresponding approximate mass in the stated bottle. These are guesses whenever the brand did not publish the amount.

### Exact or near-exact rows

- **Good Molecules Super Peptide, 30 mL:** Acetyl Hexapeptide-8 **25 ppm = 0.00075 g**; Acetyl Octapeptide-3 **25 ppm = 0.00075 g**; Copper Tripeptide-1 **5 ppm = 0.00015 g**. These are the strongest amount inputs in the model.
- **Peach & Lily Copper Peptide Pro, 30 mL:** copper peptide headline **0.2% = 0.060 g**. The model uses the Formulate Labs Copper Tripeptide-1 suspension only as a conditional proxy because “copper peptide” may refer to a complex.
- **NIOD CAIS3, 15 mL:** GHK-Cu **1% = 0.150 g**; uncomplexed GHK/Tripeptide-1 **1% = 0.150 g**. Myristoyl Nonapeptide-3, Tripeptide-2, and Acetyl Tetrapeptide-2 remain unpriced because their amounts are not stated.
- **Timeless Matrixyl 3000, 30 mL:** Matrixyl 3000 **8% = 2.400 g** commercial premix.
- **Timeless Matrixyl Synthe’6, 30 mL:** Matrixyl Synthe’6 **2% = 0.600 g** commercial premix.
- **The INKEY List Collagen Peptide, 30 mL:** Matrixyl 3000 **1% = 0.300 g**; SYN-TACKS **1% = 0.300 g**.
- **The Ordinary Matrixyl 10% + HA, 30 mL:** assumed Matrixyl 3000 **6% = 1.800 g** and Matrixyl Synthe’6 **4% = 1.200 g**. This split is not a current official assay.
- **Geek & Gorgeous Power Peptides, 30 mL:** Matrixyl 3000 **3% = 0.900 g**; Synthe’6 **2% = 0.600 g**; TEGO PEP 4-17 **4% = 1.200 g**; X50 **0.001% = 0.0003 g**. The selected public inputs are $1.14/g, $0.88/g, $2.18/g, and $0.67/g respectively, producing the **$4.18** best estimate. TEGO now uses the matched 2,300 ppm cosmetic solution; ChemicalBook and other research/pure-peptide records are excluded.

### Partially disclosed commercial technologies

- **Theramid Copper Peptide 3%, 30 mL:** GHK-Cu **3% = 0.900 g**; additional peptide complex **13% = 3.900 g**. The GHK-Cu line has a direct suspension anchor; the complex uses an explicit 1/5/20 $/g inference band.
- **Theramid Derma-Peptides 35%, 30 mL:** Matrixyl 3000 **5% = 1.500 g**; Synthe’6 **3% = 0.900 g**; Matrixyl Morphomics **3% = 0.900 g**; Munapsys **5% = 1.500 g**; BIO GF Complex **8% = 2.400 g**; Melanostatine **4% = 1.200 g**; Nutecyl **3% = 0.900 g**; Skinarch **2% = 0.600 g**; Neøclair Pro **2% = 0.600 g**.
- **Minimalist Multi-Peptides 10%, 30 mL:** Matrixyl 3000 **7% = 2.100 g**; Bio-Placenta/growth-factor-style complex **3% = 0.900 g**. The second line is not a pure peptide and has no matched public price.
- **Allies Copper Tripeptide & Ectoin, 30 mL:** Copper Tripeptide Complex **1% = 0.300 g**; Acetyl Hexapeptide-8 Complex **2% = 0.600 g**; Copper Lysinate Complex **2% = 0.600 g**. Ectoin is excluded from peptide input cost.
- **The Ordinary GF 15% Solution, 30 mL:** commercial growth-factor solution **15% = 4.500 g**. The model uses an inferred $1/10/50 per g band because the plant-made EGF/IGF/TGF blend has no matched public price.

### Undisclosed formulas: the chosen working guess

For products with no final percentage, I used named-peptide count, common supplier input rates, and whether the formula is a concentrated serum or a large low-cost booster. The base cases generally land around **0.03–0.30% total purchased peptide material**, with wider low/high cases to show how fragile the estimate is.

- **The Ordinary Multi-Peptide + HA:** AHP-8 **0.005/0.02/0.08%**; Pentapeptide-18 **0.002/0.01/0.04%**; PT-1/PT-7/PT-38 **0.002/0.01/0.04% each**; SYN-AKE **0.001/0.005/0.02%**; Relistase **0.001/0.005/0.02%**. Exact mass and total blend percentage are unknown.
- **The Ordinary Multi-Peptide + Copper:** GHK-Cu **0.02/0.10/0.30%**; the remaining named peptides together **0.01/0.05/0.30%**. The “1%” product name is not treated as 1% pure GHK-Cu.
- **Good Molecules Copper Peptide + PDRN:** GHK-Cu **0.1% = 0.030 g** as an indexed but not brand-published value; Caprooyl Tetrapeptide-3 and Tridecapeptide-1 each **0.001/0.01/0.03%**; Sodium DNA **0.02/0.10/0.30%**.
- **Paula’s Choice Pro-Collagen Booster:** six peptides combined **0.05/0.25/1.00%**, or approximately **0.010/0.050/0.200 g** in 20 mL. The high case is intentionally generous because the brand discloses identities but not individual doses.
- **Naturium Multi-Peptide Advanced:** AHP-8 **0.002/0.01/0.05%**; Copper Palmitoyl Heptapeptide-14 and Palmitoyl sh-Hexapeptide-13 together **0.008/0.04/0.20%**.
- **COSRX Blue Peptide Bakuchiol:** six named peptides together **0.02/0.10/0.30%**, or **0.010/0.050/0.150 g** in 50 mL.
- **COSRX 6 Peptide Skin Booster:** AHP-8, GHK-Cu, sh-Polypeptide-121, SYN-AKE, OP-68, and PT-8 together **0.02/0.10/0.30%**, or **0.025/0.150/0.450 g** in 150 mL.
- **DERMA E Advanced Peptides:** AHP-8 and PT-38 together **0.01/0.05/0.20%**, or **0.003/0.015/0.060 g** in 30 mL.
- **Drunk Elephant Protini:** nine peptide/growth-factor INCI names together **0.04/0.16/0.40%**, or **0.020/0.080/0.200 g** in 50 mL. The growth-factor solution possibility widens the high case.
- **Q+A Multi-Peptide:** PT-1, PT-7, Acetyl Hexapeptide-1, and sh-Polypeptide-69 together **0.03/0.10/0.30%**, or **0.010/0.030/0.090 g** in 30 mL.

### Manufacturer-use-rate overlay: COSRX 6 Peptide Skin Booster

Yes, the manufacturer-recommended amount is useful here—but it answers a different question from peptide concentration. The COSRX product instructions say to apply **2–3 pumps** after cleansing. The accompanying finished-formula study describes 20 subjects and a September 18–October 31, 2023 test period. That supports an application-exposure scenario; it does **not** disclose how much of each of the six peptides is in the bottle, and the clinical outcomes cannot be assigned to the peptides alone because the formula also contains niacinamide, N-acetyl glucosamine, hyaluronic acid, adenosine, and other ingredients.

To turn the use instruction into a usable estimate, I added a separate application overlay rather than altering the concentration estimate above. Pump mass is not published, so the dispenser assumptions are deliberately broad. The base case interpolates the instruction to **2.5 pumps** and assumes **0.30 g per pump**.

| Scenario | Pumps/use | Assumed product per pump | Estimated product applied/use | Approx. uses from 150 mL | Product used in 30 days at once daily |
|---|---:|---:|---:|---:|---:|
| Low | 2 | 0.20 g | **0.40 g** | **375** | 12.0 g |
| Base | 2.5 | 0.30 g | **0.75 g** | **200** | 22.5 g |
| High | 3 | 0.50 g | **1.50 g** | **100** | 45.0 g |

This makes the manufacturer instruction materially better than assuming an arbitrary “one use” amount from the bottle size alone. It lets us estimate product exposure, bottle duration, and a modelled material-input cost per application. It still cannot tell us whether, for example, Acetyl Hexapeptide-8 is 0.001%, 0.01%, or 0.1% of the formula.

Using the current bottle-level input scenarios (**$0.03 / $2.50 / $25.00 per 150 mL bottle**), the aligned application-cost overlay is:

| Scenario | Bottle input scenario | Uses/bottle | Modelled peptide/material input per application |
|---|---:|---:|---:|
| Low | $0.03 | 375 | **$0.00008** |
| Base | $2.50 | 200 | **$0.0125** |
| High | $25.00 | 100 | **$0.25** |

These are **not** measured peptide doses, total manufacturing costs, or clinical values. They are simply the bottle-level material estimate divided by the estimated number of applications. The low/high spread remains wide because both the formula loading and the pump mass are uncertain. The machine-readable overlay is [`data/peptide_application_use_rate_scenarios.csv`](data/peptide_application_use_rate_scenarios.csv).

The correct interpretation is therefore: **use “2–3 pumps” to estimate how much finished product a person applies; keep the six-peptide concentration as a separate low/base/high formulation assumption.** The strongest next evidence would be a COSRX technical sheet, a finished-product assay, or a manufacturer statement giving the concentration of each peptide—not the clinical trial result alone.

## 6. Common concentration patterns used for the guesses

These are the practical patterns that made the model’s guesses less arbitrary:

1. **Branded commercial premixes:** usually modeled at the stated 1–8% technology level when the product discloses it. The percentage is the premix, not pure peptide.
2. **Pure lipopeptide suspensions:** supplier pages commonly show 1–10% input of a suspension whose active assay is 0.01–1%. That often implies final pure active in the ppm-to-low-basis-point range.
3. **Expression-line peptides:** AHP-8, AO-3, Pentapeptide-18, and SYN-AKE show a much wider material price spread. Small-lot suspension prices are high; bulk powder snippets can be implausibly low. The model preserves both rather than picking a fake “true” number.
4. **Recombinant growth factors:** the Formula Labs EGF page states 1–10 ppm active targets and sells refrigerated small vials. For retail formulas, the model uses a wide bulk-solution inference band rather than applying $349–420/g small-vial pricing directly.
5. **PDRN / Sodium DNA:** the material is highly grade-dependent. Source, molecular-weight distribution, salmon/biotech origin, endotoxin controls, and PN-versus-PDRN identity matter more than the word “PDRN.”
6. **Undisclosed multi-peptide products:** the base assumption is not “every named peptide is 1%.” It is a total material load scaled to product format and named-peptide count, then split across ingredients only for sensitivity analysis.

## 7. What a creator is most likely paying

The best practical guess is a three-part answer:

- A **large manufacturer buying a branded premix** is likely below small-pack public prices, often closer to the low end of the Trulux/Herbarie ladder, but the contract is private.
- A **small or mid-size formulator buying documented suspension material** may pay near the middle or high end of the Formula Labs ladder, especially for low-assay, high-documentation peptides such as OP-68, Pentapeptide-18, PT-8, TP-21, or AO-3.
- A **research or prototype buyer** can pay the research-grade ceiling, but that should never be used to infer normal retail-product COGS.

That is why the most plausible retail comparison is not one number. It is a base scenario plus a source/grade range, with a separate flag when the product’s formula amount is unknown.

## Assumptions and evidence gaps

- Retail prices are observed list-price snapshots from the companion product scan; they are not used to choose ingredient prices.
- Formula density is approximated at 1 g/mL.
- Percentage-to-gram conversions treat the listed percentage as a mass percentage of the purchased material unless the row explicitly says pure active.
- Formulate Labs price ladders can change and may depend on the selected strength/carrier. The source record preserves the visible page values but does not claim that every variant has identical pricing.
- Commercial trademarks are kept separate from generic INCI analogues. Matrixyl 3000 is not silently replaced by PT-1/PT-7; SYN-AKE is not silently replaced by a bulk snippet; PDRN is not silently replaced by a nucleic-acid research reagent.
- “No public price” is a valid result. BIO GF Complex, Matrixyl Morphomics, Neøclair Pro, Copper Lysinate Complex, MiniProtein systems, and several growth-factor blends remain quote-only or insufficiently specified.
- Formulation costs beyond peptide input—water, solvents, humectants, preservation, packaging, filling, QC, stability, regulatory work, freight, cold-chain, distributor margin, and royalties—are excluded.
- A high peptide-input estimate does not show that a brand is profitable or unprofitable. It shows that the visible public material price is not a reliable proxy for the brand’s contract price.

## Sources and reproducibility

1. [Formulate Labs material catalogue](https://www.formulatelabs.ai/materials) — current catalogue index used to identify the expanded direct-price records.
2. [Formulate Labs EGF](https://www.formulatelabs.ai/materials/epidermal-growth-factor) — recombinant sh-Oligopeptide-1 pack ladder, 0.08%/0.8% strengths, and 1–10 ppm active guidance.
3. [Trulux Matrixyl 3000](https://trulux.com/products/matrixyl-3000/) — public commercial-premix pack ladder and blend identity.
4. [Trulux Matrixyl Synthe’6](https://trulux.com/products/matrixyl-synthe-6/) — public commercial-premix pack ladder and PT-38 relationship.
5. [Trulux SYN-COLL](https://trulux.com/products/syn-coll/) — public commercial-premix pricing for PT-5 technology.
6. [The Herbarie SYN-TACKS](https://www.theherbarie.com/Syn-Tacks.html) — public pack ladder, commercial INCI, and 1% use recommendation.
7. [New Directions Australia Matrixyl 3000](https://www.newdirections.com.au/Raw-Materials-Cosmetic-Ingredients/Active-Ingredients/Matrixyl-R-3000-Active-Ingredients) — independent distributor cross-check.
8. [Formula Labs terms](https://www.formulatelabs.ai/terms) — prices are indications subject to change; current-access-date treatment.
9. [Ingredient price source-record ledger](data/peptide_price_source_records.csv) — 39 row machine-readable source trail.
10. [25-formulation scenario dataset](data/peptide_price_scenario_model.csv) — every product row, assumption string, source-record IDs, and cost range.
11. [COSRX application-use-rate overlay](data/peptide_application_use_rate_scenarios.csv) — manufacturer’s 2–3-pump instruction converted into low/base/high product-exposure scenarios.
11. [Earlier ingredient-by-ingredient price research](08_peptide_ingredient_price_research.md) — prior marketplace, distributor, trade-data, identity, and no-price records.
12. [Interactive best-cost visual](peptide_cost_model.html) — one selected heuristic cost and retail multiple for each of the 25 formulas, with independently priceable-line coverage preserved as a separate evidence-quality field and modeled assumptions shown in italics. The scenario ranges remain in this document and its CSV for auditability.

## Evidence gaps

The next highest-value research would be direct RFQs or distributor replies for TEGO PEP 4-17, Matrixyl Morphomics, BIO GF Complex, MiniProtein systems, Neøclair Pro, Copper Lysinate Complex, Nutecyl variants, and each branded growth-factor complex. A finished-product LC-MS/HPLC assay would improve the formula-amount side more than another low-quality marketplace price listing.
