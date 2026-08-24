# Peptide Ingredient Cost Model: What Is Probably in Each Bottle?

*Compiled 2026-08-13. US retail prices and supplier prices were checked against live pages where available; volatile prices should be rechecked before purchase. This is a research estimate, not a manufacturer COGS disclosure or medical advice. Confidence labels: **high** = finished-formula amount is published; **medium** = commercial blend percentage is published but pure-peptide assay is not; **low** = named ingredients are present but concentration is modeled.*

## 0. Bottom line

The best value depends on which “peptide cost” you mean:

1. **Best disclosed multi-pathway value:** Geek & Gorgeous Power Peptides. Its 30 mL bottle is about $18.80 and publishes 3% Matrixyl 3000, 2% Matrixyl Synthe’6, 4% TEGO PEP 4-17, and 0.001% X50 Antiaging. The revised best public replacement-cost estimate is **$4.18 per bottle** after matching TEGO to a cosmetic 2,300 ppm commercial solution rather than a research vial or pure-peptide listing. [[1]](https://geekandgorgeous.com/products/power-peptides) [[1a]](https://www.escentialsofaustralia.com/products/productid1564)
2. **Best low-cost interpretable collagen-signal experiment:** The Ordinary Matrixyl 10% + HA. At $10.90 for 30 mL, the modeled 10% commercial blend is roughly **$3.60–$7.20** using public Matrixyl supplier prices. The 6% Matrixyl 3000 / 4% Synthe’6 split is an explicit model assumption because the current product page does not publish an assay for each blend. [[2]](https://theordinary.com/en-us/matrixyl-10-ha-serum-100431.html)
3. **Best exact final-formula disclosure:** Good Molecules Super Peptide Serum. It lists **25 ppm Acetyl Hexapeptide-8, 25 ppm Acetyl Octapeptide-3, and 5 ppm Copper Tripeptide-1**—only **1.65 mg total peptide in 30 mL**—for $12. The cost of those milligrams is probably only cents to roughly fifty cents, but the small dose is the point: transparency does not mean high loading. [[3]](https://v1.goodmolecules.com/products/super-peptide-serum)
4. **Most expensive-looking raw peptide formula:** Theramid Copper Peptide. The brand claims **3% pure copper peptide plus 13% additional peptide complex** in 30 mL. If the 3% is truly 0.9 g of GHK-Cu, that alone is roughly **$3.60–$25.65** depending on bulk versus small-lot raw material; adding the 13% complex produces a broad **$7.50–$56.60** total modeled active-replacement range. That is impressive on paper, but it does not prove a proportional clinical advantage. [[4]](https://nichebeautylab.com/collections/bestseller-north-america/products/copper-peptide)
5. **Best retail $/mL is not the same as best peptide $/mL.** COSRX The 6 Peptide Skin Booster is $25 for 150 mL, but its six peptide concentrations are undisclosed. It wins the retail-volume sort, not the evidence-backed peptide-content sort. [[5]](https://www.cosrx.com/products/the-6-peptide-skin-booster-serum)

Open the [sortable cost visual](peptide_cost_model.html) for the full 25-formulation table. It selects one best heuristic estimate per formulation from the auditable scenario dataset, joins the 150-line [ingredient amount audit](data/peptide_formula_ingredient_audit.csv), and preserves the stricter independent public-price checks. Every formulation has one estimated cost and retail multiple; assumptions and proxy-derived values are italicized rather than left blank or presented as measured facts. The wider uncertainty bounds remain in the downloadable research data, not in the decision table.

## 1. What this model is and is not

This page estimates **ingredient replacement value**, not a brand’s actual manufacturing cost. It does not include water, solvents, humectants, emulsifiers, preservatives, pH adjustment, stability testing, microbiology, filling, packaging, freight, scrap, regulatory work, retailer margin, advertising, returns, or profit. A $5 modeled peptide input does not mean a $5 product costs $5 to make, and a $0.20 modeled peptide input does not mean the formula is worthless.

The central distinction is:

| Label language | What the number usually means | How the model treats it |
|---|---|---|
| “25 ppm Copper Tripeptide-1” | Final-formula mass concentration | Direct mass calculation: 25 ppm × bottle volume |
| “3% Matrixyl 3000” | 3% of a commercial supplier solution/premix | 3% of bottle mass is counted as commercial active input; pure peptide is lower and usually undisclosed |
| “1% copper peptides” | A product-level technology headline | Modeled as a range; not automatically 1% pure GHK-Cu |
| “30% multi-peptide complex” | A proprietary blend/complex | 30% commercial complex mass; its peptide assay and raw price are unknown |
| “Contains six peptides” | Presence/identity only | A low-dose uncertainty model; no concentration is inferred from INCI order |

The model uses **1 mL ≈ 1 g** for serum calculations. Creams, silicone-rich emulsions, and dense products can deviate from that assumption; this changes the result modestly compared with the much larger uncertainty in undisclosed peptide loading.

## 2. Cost equation and evidence ladder

For a disclosed final-formula percentage:

```text
modeled active mass (g) = bottle volume (mL) × disclosed percentage ÷ 100 × density assumption
modeled ingredient cost = modeled active mass × raw-material price per gram
```

For ppm disclosures, 1 ppm is treated as 1 mg/kg, so a 30 mL water-like serum contains approximately 0.03 mg per ppm. The Good Molecules Super Peptide calculation is therefore:

```text
(25 + 25 + 5 ppm) × 30 mL ≈ 1.65 mg total peptide = 0.00165 g
```

Every row in the CSV carries three levels:

- **Low:** bulk/commodity cosmetic raw material or the low end of the plausible loading range.
- **Base:** a realistic small-to-mid-scale formulator case using the public benchmark closest to the material.
- **High:** small-lot, high-purity, specialty, or deliberately conservative cost case.

The evidence ladder is: **final-formula ppm/% > official commercial-blend % > independent formula index > INCI presence/order > generic market proxy**. The last two are useful for a range, not proof of dose.

## 3. Public raw-material anchors

These are the most useful price anchors I found, checked 2026-08-13. Australian-dollar prices are converted at a rounded **US$0.65/AU$** for comparison; the chart’s ranges are intentionally wider than the exchange-rate uncertainty.

| Material | Public price evidence | Approximate comparable cost | Why it matters |
|---|---|---:|---|
| Matrixyl 3000 commercial solution | Trulux lists AU$207.80/50 g, AU$356.10/100 g, and AU$1,760/1 kg | **$1.14/g at 1 kg; $2.31/g at 100 g** | Directly prices the commercial premix used by many formulas. [[6]](https://trulux.com/products/matrixyl-3000/) |
| Matrixyl Synthe’6 commercial solution | Trulux lists AU$227/50 g, AU$389.60/100 g, and AU$1,947.70/1 kg | **$1.27/g at 1 kg; $2.53/g at 100 g** | Directly prices the Palmitoyl Tripeptide-38 premix. [[7]](https://trulux.com/products/matrixyl-synthe-6/) |
| SYN-COLL / Palmitoyl Tripeptide-5 premix | Trulux lists AU$142.40/50 g, AU$243.10/100 g, and AU$1,157.10/1 kg | **$0.75/g at 1 kg; $1.58/g at 100 g** | A useful proxy for a common signal-peptide commercial solution. [[8]](https://trulux.com/products/syn-coll/) |
| Pure/cosmetic-grade GHK-Cu | Alibaba/Made-in-China listings show roughly $3.50–$8/g at kilogram or sub-kilogram scale; Albochem lists $79.90/10 g; Xclusiv lists a high-priced pure ingredient from $285 | **$4–$8/g bulk proxy; up to about $28.50/g small-lot proxy** | Explains why a claimed 0.9 g of pure GHK-Cu can be cheap at factory scale but expensive at lab scale. [[9]](https://www.made-in-china.com/price/prodetail_Organic-Intermediate_KwtGPkbvbeAm.html) [[10]](https://albochem.com/product/ghk-cu-raw-powder-copperii-glycyl-l-histidyl-l-lysinate-%E2%89%A599-purity-10-grams/) [[11]](https://www.xclusivorganics.com/collections/peptides) |
| Cosmetic Sodium DNA/PDRN | Bulk listings range from roughly $80–$150/kg; a small-lot catalog lists ¥269.90/g for ≥95% cosmetic-grade material | **$0.08–$0.60/g bulk/industrial proxy; small-lot can be tens of dollars/g** | PDRN is a major uncertainty in Good Molecules Copper Peptide Serum because the finished formula does not publish its amount. [[12]](https://www.alibaba.com/supplier/polynucleotides-supplier-supplier-for-wholesale.html) [[13]](https://www.js-akx.com/PNO%E9%98%BF%E6%8B%89%E4%B8%81-I1506387.html) |

Large brands may pay below public small-batch prices, while a small brand may pay more after shipping, documentation, minimum-order, and quality-control costs. These are **replacement-value anchors**, not negotiated purchase orders.

## 4. Disclosed or partly disclosed formulas

The table below is the human-readable version of the most auditable rows. “Amount” means modeled material in the bottle; for a premix it is **premix mass**, not pure peptide mass.

| Product | Peptide loading and modeled bottle amount | Estimated peptide/active input cost | Confidence |
|---|---|---:|---|
| Good Molecules Super Peptide | Acetyl Hexapeptide-8 25 ppm = 0.75 mg; Acetyl Octapeptide-3 25 ppm = 0.75 mg; Copper Tripeptide-1 5 ppm = 0.15 mg; **1.65 mg total** | **$0.06 best estimate** | High |
| Geek & Gorgeous Power Peptides | Matrixyl 3000 3% = 0.9 g; Synthe’6 2% = 0.6 g; TEGO PEP 4-17 4% = 1.2 g; X50 0.001% = 0.0003 g | **$4.18 best estimate** | High |
| The Ordinary Matrixyl 10% + HA | Modeled 6% Matrixyl 3000 = 1.8 g plus 4% Synthe’6 = 1.2 g; **3.0 g premix total** | **$7.18 best estimate** | Medium |
| Timeless Matrixyl 3000 | 8% Matrixyl 3000 = **2.4 g premix** | **$5.54 best estimate** | High |
| Timeless Matrixyl Synthe’6 | 2% Synthe’6 = **0.6 g premix** | **$1.52 best estimate** | High |
| Minimalist Multi-Peptides 10% | Matrixyl 3000 7% = 2.1 g; Bio-Placenta complex 3% = 0.9 g | **$10.25 best estimate** | Low |
| The INKEY List Collagen Peptide Serum | Matrixyl 3000 1% = 0.3 g; SYN-TACKS 1% = 0.3 g | **$1.29 best estimate** | Medium |
| Theramid Copper Peptide | Claimed pure GHK-Cu 3% = 0.9 g; additional peptide complex 13% = 3.9 g | **$20.36 best estimate** | Low |
| Theramid Derma-Peptides | Nine commercial technologies totaling 35% = **10.5 g premix** | **$72.00 best estimate** | Low |
| Medik8 Liquid Peptides Advanced MP | 30% multi-peptide complex = **9.0 g commercial complex**, 13 peptide count | **$45.00 best estimate** | Low |
| The Ordinary GF 15% Solution | EGF/IGF/TGF solution at 15% = **4.5 g commercial solution** | **$45.00 best estimate** | Low |
| Peach & Lily Copper Peptide Pro Firming Serum | Official 0.2% copper peptide = **0.06 g** | **$0.06 best estimate** | High for amount; medium for raw grade |
| NIOD CAIS3 | 1% GHK-Cu = 0.15 g plus 1% GHK = 0.15 g; **0.30 g total named actives** | **$2.30 best estimate** | High for named concentrations |
| Allies Copper Tripeptide & Ectoin | 1% Copper Tripeptide Complex = 0.3 g; 2% Acetyl Hexapeptide-8 Complex = 0.6 g; 2% Copper Lysinate Complex = 0.6 g | **$8.40 best estimate** | Medium |

The official pages support the product disclosures for G&G, Theramid, The Ordinary, Peach & Lily, NIOD, Medik8, and Allies. [[1]](https://geekandgorgeous.com/products/power-peptides) [[4]](https://nichebeautylab.com/collections/bestseller-north-america/products/copper-peptide) [[14]](https://nichebeautylab.com/en-gb/collections/eu-bestseller/products/derma-peptides) [[15]](https://theordinary.com/en-us/multi-peptide-copper-peptides-1-serum-769915233179.html) [[16]](https://theordinary.com/en-us/gf-15-solution-growth-factors-serum-100702.html) [[17]](https://www.peachandlily.com/products/copper-peptide-pro-firming-serum) [[18]](https://niod.com/en-bf/copper-amino-isolate-serum-3-11-cais3-serum-100368.html) [[19]](https://us.allies.shop/products/copper-tripeptide-ectoin-advanced-repair-serum)

## 5. Undisclosed formulas: one best estimate, explicitly labeled

For a named peptide without a percentage, the reader-facing model selects the single most plausible loading from supplier-recommended rates, INCI position, product claims, and material class. The assumption is italicized in the visual. For products that claim a complex but do not disclose its percentage, the estimate uses the closest formulation-grade commercial-premix or potency-matched replacement benchmark. Retail price is never used to select the number.

| Product | Named peptides / amount assumption | Estimated cost |
|---|---|---:|
| Good Molecules Copper Peptide Serum with PDRN | Independently indexed Copper Tripeptide-1 0.1% = 30 mg, plus Caprooyl Tetrapeptide-3, Tridecapeptide-1, and Sodium DNA/PDRN; brand assay not found | **$3.28 best estimate** using potency-matched cosmetic GHK-Cu suspension and a $10/g topical PDRN powder benchmark |
| The Ordinary Multi-Peptide + HA | Seven named peptides; best estimate uses roughly **0.20% total purchased peptide material** | **$6.50 best estimate** |
| The Ordinary Multi-Peptide + Copper Peptides 1% | 1% copper-peptide technology headline plus other peptides; pure GHK-Cu fraction remains unknown | **$5.20 best estimate** |
| Paula’s Choice Pro-Collagen Multi-Peptide Booster | Six peptides; best estimate uses **0.25% total active material** | **$2.00 best estimate** |
| Naturium Multi-Peptide Advanced Serum | Acetyl Hexapeptide-8 and two specialty peptide technologies; best estimate uses **0.05% total active material** | **$0.20 best estimate** |
| COSRX Blue Peptide Bakuchiol Serum | Copper Tripeptide-1 plus five peptides; best estimate uses **0.10% total material** | **$1.50 best estimate** |
| COSRX The 6 Peptide Skin Booster | Six named peptides; best estimate uses **0.10% total material = 0.15 g in 150 mL** | **$2.50 best estimate** |
| DERMA E Advanced Peptides & Flora-Collagen | Acetyl Hexapeptide-8 and Palmitoyl Tripeptide-38; best estimate uses **0.05% total material** | **$0.30 best estimate** |
| Drunk Elephant Protini Polypeptide Cream | Nine signal/growth-factor INCI names; best estimate uses **0.16% total material = 0.08 g in 50 mL** | **$2.00 best estimate** |
| Q+A Multi-Peptide Facial Serum | Four named peptides; best estimate uses **0.10% total material** | **$0.50 best estimate** |

The official pages establish presence, size, and retail price for these products, but not a peptide-specific assay. [[20]](https://naturium.com/products/multi-peptide-advanced-serum) [[21]](https://www.cosrx.com/products/cosrx-the-blue-peptide-bakuchiol-plump-glow-serum) [[5]](https://www.cosrx.com/products/the-6-peptide-skin-booster-serum) [[22]](https://www.drunkelephant.com/protini-polypeptide-cream-50-ml-856556004739.html) [[23]](https://us.qandaskin.com/products/multi-peptide-facial-serum) [[24]](https://www.paulaschoice.com/pro-collagen-multi-peptide-booster/3020.html)

## 6. What the sortable visual shows

The chart calculates these fields from the CSV:

- **Retail $/mL:** `retail price ÷ bottle volume`.
- **Base peptide cost/bottle:** the midpoint-style estimate in the CSV.
- **Base peptide cost/mL:** `base peptide cost ÷ bottle volume`.
- **Retail-to-peptide multiple:** `retail price ÷ base peptide input cost`. This is not profit; it simply shows how much retail price exists per modeled active dollar.
- **Transparency:** 1–5 score based on whether the final formula, concentration, and commercial/pure distinction are auditable.
- **Confidence:** high/medium/low confidence in the cost estimate, not a clinical efficacy grade.

The “cost per mL” sort is useful for spotting obvious retail-value outliers, but **the base peptide cost/mL sort is only as good as the disclosure**. A low number on an undisclosed product can mean low peptide loading, cheap raw material, or simply a generous uncertainty model.

## 7. Product-level takeaways

### 7.1 Best value if you want collagen-signal technologies

The Ordinary Matrixyl 10% + HA, Timeless Matrixyl 3000, and Geek & Gorgeous Power Peptides all look inexpensive relative to public supplier-premix prices. G&G is the broadest of the three and discloses every commercial technology level. The Ordinary is cheaper per bottle and simpler. Timeless is much more expensive than the raw Matrixyl input alone would suggest, but still not expensive in absolute terms.

### 7.2 Best value if you want GHK-Cu specifically

Peach & Lily publishes 0.2% copper peptide at $49/30 mL; NIOD publishes 1% GHK-Cu plus 1% GHK at $72/15 mL; Theramid claims 3% pure copper peptide at about $49/30 mL; Allies publishes a 1% Copper Tripeptide Complex at $199/30 mL; Good Molecules is the cheapest candidate but its useful 0.1% figure is not brand-published. On modeled raw-material economics, Theramid is the most aggressive claim, while Good Molecules is the cheapest uncertainty-adjusted experiment.

### 7.3 Best value if you care about exact dose rather than headline loading

Good Molecules Super Peptide Serum wins transparency. Its 1.65 mg total peptide mass is small, but it is a number that can be checked. This is a useful counterweight to a 35% or 30% “complex” claim where the pure peptide content is unknown.

### 7.4 Premium products are not automatically raw-material frauds

Medik8, Allies, Paula’s Choice, NIOD, and Drunk Elephant can spend more on stability, packaging, testing, delivery systems, clinical testing, and formulation work. The model only says that the **peptide input alone** usually cannot explain the entire retail price. It does not say the rest of the product has no value.

## 8. Assumptions and unresolved questions

### Raw-material assumptions

- Public Trulux prices are used as the closest visible supplier benchmark for Matrixyl 3000, Synthe’6, and SYN-COLL; large contract manufacturers may negotiate lower prices.
- GHK-Cu uses a bulk range around $4–$8/g and a small-lot high case around $28.50/g. The listings differ in purity, salt form, documentation, and identity controls; they are not interchangeable quality grades.
- TEGO PEP 4-17, Munapsys, SYN-TACKS, Progeline, and Collaxyl now have public cosmetic-input pack prices. X50 has a public distributor signal. Matrixyl Morphomics, BIO GF Complex, Neoclair Pro, MiniProteins, and most proprietary growth-factor complexes still require quotes.
- Sodium DNA/PDRN is modeled as a cosmetic raw material, not injection-grade PDRN. Source, molecular-weight distribution, assay, endotoxin control, and processing can change the price by orders of magnitude.
- No royalty, trademark fee, clinical-support fee, or exclusive-distribution premium is added because those contracts are private.

### Formula assumptions

- Density is approximated as 1 g/mL. A density difference of 5–10% is smaller than the uncertainty around undisclosed peptide assay.
- A disclosed commercial-blend percentage is treated as mass of the commercial material. The underlying pure peptide fraction is not invented.
- If the product says “1% copper peptides,” the model does not automatically turn that into 0.3 g of pure GHK-Cu. It selects a formulation-grade complex or potency-matched replacement assumption unless the brand explicitly says “1% GHK-Cu” or publishes a final-formula assay.
- INCI order is used only to establish presence and rough formulation prominence. It cannot establish a concentration because ingredients below 1% can be listed in flexible order in many jurisdictions.
- For an undisclosed peptide group, the displayed mass is the single most plausible heuristic selection based on product size, named-peptide count, INCI context, and commercial-complex language. It is an estimate, not a measured assay, and is italicized in the visual.

### Product and price assumptions

- Retail prices are one-time US list-price snapshots where available; taxes, shipping, discounts, subscription pricing, and regional VAT are excluded.
- Theramid EUR prices are converted at a rounded 1.09 USD/EUR only to place the product on one chart. The underlying source price remains EUR.
- Allies’ 1 fl oz product is modeled as 30 mL and $199 from the North American page.
- The chart includes one 50 mL cream and one 150 mL toner-like booster because the user asked for many formulations. Their retail $/mL is not directly comparable with a concentrated 30 mL serum without considering usage amount.

### What would materially improve the model

- Supplier TDS/COA or assay for each branded complex.
- Direct confirmation from Good Molecules of Copper Tripeptide-1 and Sodium DNA percentage in the PDRN serum.
- Current raw quotes for TEGO PEP 4-17, X50 Antiaging, Matrixyl Morphomics, Munapsys, BIO GF Complex, and Medik8’s MiniProteins.
- Finished-product peptide assay by an independent laboratory, ideally with LC-MS/HPLC identity and mass balance.
- A full contract-manufacturing quote that separates active, base, bottle, filling, QA, stability, freight, and minimum-order economics.

## Evidence gaps

- No public source proves the actual pure-peptide mass in most consumer serums.
- Supplier “clinical” percentages often refer to the recommended use level of a premix, not the peptide molecule concentration and not the finished-product clinical dose.
- A higher modeled ingredient cost does not establish greater skin penetration or visible efficacy.
- The price landscape is live and region-dependent; this page should be refreshed before a purchase decision.
- The model estimates cost, not treatment effect. The existing [ranked clinical evidence page](02_ranked_clinical_evidence.md) remains the correct place to judge human evidence.

## Sources

1. Geek & Gorgeous, [Power Peptides](https://geekandgorgeous.com/products/power-peptides) — official 30 mL size, €15.80 price, 3% Matrixyl 3000, 2% Synthe’6, 4% TEGO PEP 4-17, and 0.001% X50 disclosure.
2. The Ordinary, [Matrixyl 10% + HA](https://theordinary.com/en-us/matrixyl-10-ha-serum-100431.html) — official price, size, INCI, and product headline.
3. Good Molecules, [Super Peptide Serum formula disclosure](https://v1.goodmolecules.com/products/super-peptide-serum) — official ppm-level final-formula disclosure preserved in the prior value audit.
4. Theramid, [Copper Peptide](https://nichebeautylab.com/collections/bestseller-north-america/products/copper-peptide) — official 30 mL product page, €44.95 regional price, 3% copper-peptide claim, INCI, and 13% additional peptide claim.
5. COSRX, [The 6 Peptide Skin Booster Serum](https://www.cosrx.com/products/the-6-peptide-skin-booster-serum) — official 150 mL size, $25 price, six-peptide positioning, and undisclosed concentrations.
6. Trulux, [Matrixyl 3000](https://trulux.com/products/matrixyl-3000/) — public 50 g through 1 kg supplier prices and INCI.
7. Trulux, [Matrixyl Synthe’6](https://trulux.com/products/matrixyl-synthe-6/) — public 50 g through 1 kg supplier prices and Palmitoyl Tripeptide-38 premix identity.
8. Trulux, [SYN-COLL](https://trulux.com/products/syn-coll/) — public 50 g through 1 kg prices and Palmitoyl Tripeptide-5 premix identity.
9. Made-in-China, [GHK-Cu bulk price listing](https://www.made-in-china.com/price/prodetail_Organic-Intermediate_KwtGPkbvbeAm.html) — seller-listed $3.50/g at 1 kg and higher small-volume tiers; marketplace evidence, not a quality certification.
10. Albochem, [≥99% GHK-Cu 10 g](https://albochem.com/product/ghk-cu-raw-powder-copperii-glycyl-l-histidyl-l-lysinate-%E2%89%A599-purity-10-grams/) — $79.90/10 g small-lot raw ingredient listing.
11. Xclusiv Organics, [peptide collection](https://www.xclusivorganics.com/collections/peptides) — high-priced pure GHK-Cu ingredient listing starting at $285; exact variant price should be rechecked.
12. Alibaba supplier index, [polynucleotide supplier ranges](https://www.alibaba.com/supplier/polynucleotides-supplier-supplier-for-wholesale.html) — bulk Sodium DNA/PDRN range around $80–$150/kg; marketplace evidence.
13. Aladdin listing, [cosmetic-grade Sodium DNA/PDRN](https://www.js-akx.com/PNO%E9%98%BF%E6%8B%89%E4%B8%81-I1506387.html) — small-lot ¥269.90/g and larger pack prices; regional catalog evidence.
14. Theramid, [Derma-Peptides](https://nichebeautylab.com/en-gb/collections/eu-bestseller/products/derma-peptides) — official 30 mL, £29/€32.95-class price and 35% multi-peptide treatment claim.
15. The Ordinary, [Multi-Peptide + Copper Peptides 1%](https://theordinary.com/en-us/multi-peptide-copper-peptides-1-serum-769915233179.html) — official $32/30 mL price, “1%” headline, and named-peptide INCI.
16. The Ordinary, [GF 15% Solution](https://theordinary.com/en-us/gf-15-solution-growth-factors-serum-100702.html) — official 15% solution claim and product price.
17. Peach & Lily, [Copper Peptide Pro Firming Serum](https://www.peachandlily.com/products/copper-peptide-pro-firming-serum) — official $49/30 mL and 0.2% copper-peptide disclosure.
18. NIOD, [CAIS3](https://niod.com/en-bf/copper-amino-isolate-serum-3-11-cais3-serum-100368.html) — official 1% GHK-Cu, 1% GHK, $72/15 mL, and INCI.
19. Allies of Skin, [Copper Tripeptide & Ectoin Advanced Repair Serum](https://us.allies.shop/products/copper-tripeptide-ectoin-advanced-repair-serum) — official $199/30 mL, 1% Copper Tripeptide Complex, 2% Acetyl Hexapeptide-8 Complex, and 2% Copper Lysinate Complex.
20. Naturium, [Multi-Peptide Advanced Serum](https://naturium.com/products/multi-peptide-advanced-serum) — official $25/30 mL, named peptides, and no individual peptide percentages.
21. COSRX, [Blue Peptide Bakuchiol Plump Glow Serum](https://www.cosrx.com/products/cosrx-the-blue-peptide-bakuchiol-plump-glow-serum) — official $27/50 mL and named-peptide formula.
22. Drunk Elephant, [Protini Polypeptide Cream](https://www.drunkelephant.com/protini-polypeptide-cream-50-ml-856556004739.html) — official 50 mL price, nine-signal-peptide claim, and INCI.
23. Q+A, [Multi-Peptide Facial Serum](https://us.qandaskin.com/products/multi-peptide-facial-serum) — official $13 price and peptide-complex positioning.
24. Paula’s Choice, [Pro-Collagen Multi-Peptide Booster](https://www.paulaschoice.com/pro-collagen-multi-peptide-booster/3020.html) — official six-peptide product; $59/20 mL retail benchmark corroborated by current retail listings.
