# 09 — DIY vitamin C potency likelihood model

**Status:** transparent planning heuristic, not a stability assay. Compiled 2026-08-14.

## Bottom line

The [DIY potency likelihood visualizer](diy_vitamin_c_potency_visualizer.html) is designed for a narrow use case: a small, water-based batch made from L-ascorbic acid (LAA), water, and optional DIY co-ingredients. It asks what a home user can reasonably observe or measure—pH, age, color, storage temperature, light, container, headspace/opening, water quality, concentration, and stabilizers—and turns those inputs into two outputs:

1. an **intact LAA likelihood score**, which is a model score rather than a measured percentage; and
2. a **relative chemical-state allocation** that places the remainder into broad degradation families.

It intentionally does **not** estimate microbial safety, purchased-product shelf life, exact DHA/LAA ratios, or the concentration of any individual byproduct. A stability-indicating HPLC/LC method is the appropriate way to quantify LAA and degradation products.

## Why color is included—but not trusted as a potency meter

Yellowing is useful as an observation because deeper yellow/orange/brown color often means that downstream colored products have accumulated. It is not a calibrated proxy for intact LAA. A clear batch can lose LAA before enough colored material is visible; a pale-yellow batch can still contain a meaningful amount of LAA; and pH, oxygen, light, heat, trace metals, concentration, packaging, and co-ingredients change both the degradation rate and the products that accumulate. The visualizer therefore treats color as a **conservative warning input** with a large uncertainty, not as “yellow equals X% remaining.”

The color control is a continuous **0–100 position** from clear/white to brown. The named bands below are orientation labels layered onto that continuous slider; they are not laboratory color measurements:

| Visual observation | Model treatment | Practical interpretation |
|---|---:|---|
| Clear / white | no color warning | Does not prove full potency. Use age and storage history. |
| Faint straw | small warning | Early oxidation or a small amount of colored downstream material is plausible. |
| Pale yellow | modest warning | Use promptly if the batch is fresh and otherwise well controlled. |
| Yellow | meaningful warning | The model moves toward “remake soon,” especially after the first week. |
| Gold | strong warning | Conservative replacement is preferred. |
| Orange | very strong warning | Remake now rather than trying to rescue the batch. |
| Brown | maximum warning | Treat intact LAA as untrustworthy and discard/remake. |

Unexpected green, blue, gray/black, particles, gas, clouding, a new odor, or visible contamination is not interpreted by the model. Do not use the chart to explain those findings; discard the batch.

## Evidence map and what is actually being inferred

The evidence is heterogeneous. The strongest sources establish mechanisms and directional effects; they do not provide a validated shelf-life equation for a home serum. Product patents and formulation studies help bound realistic packaging and pH choices, but their vehicles, preservatives, filling processes, and analytical methods are not interchangeable with a DIY water batch.

| Input or model feature | Evidence anchor | What the model uses | Confidence |
|---|---|---|---|
| Acidic pH is generally more favorable for LAA stability than higher pH | The review of commercial and aqueous products discusses pH dependence and the increase in ionized ascorbate at higher pH. [[1]](https://pmc.ncbi.nlm.nih.gov/articles/PMC8773188/) | A smooth pH multiplier with the most favorable zone around pH 3.0–3.5; sharply more pressure above pH 4.5–5.0. | Directional: medium-high |
| Temperature and time accelerate degradation | Aqueous self-degradation work reports faster loss at higher temperature and longer time, with first-order behavior under its tested conditions. [[2]](https://pmc.ncbi.nlm.nih.gov/articles/PMC6049385/) | Temperature multiplier and an exponential age term. | Directional: high; numeric transfer: low |
| Brown products are promoted in some higher-pH aqueous conditions | The same study found more strongly brown products around pH 5.8–6.8, while pH 4.5 favored less-colored intermediates at its measured wavelength. [[2]](https://pmc.ncbi.nlm.nih.gov/articles/PMC6049385/) | Higher-pH pathway allocation and an earlier remake warning at higher pH. | Directional: medium |
| Light, formulation, and pH affect degradation | Cream formulation work found pH, concentration, viscosity, and ingredients changed photostability; dark degradation was much slower than UV in that cream vehicle. [[3]](https://pmc.ncbi.nlm.nih.gov/articles/PMC3167265/) | Light multiplier and a warning that cream data cannot be copied directly to DIY water. | Directional: medium; numeric transfer: low |
| Oxygen/headspace matters | The review summarizes a linear relationship between headspace oxygen and first-order degradation under one tested condition. [[1]](https://pmc.ncbi.nlm.nih.gov/articles/PMC8773188/) | Low/normal/high opening and headspace as a coarse oxygen proxy. | Directional: medium |
| Trace metals can alter stability | Small amounts of trace elements changed aqueous ascorbic-acid stability in a controlled study. [[4]](https://pmc.ncbi.nlm.nih.gov/articles/PMC3510389/) | Distilled/deionized water receives a modest advantage over tap/unknown water. | Directional: medium; magnitude: low |
| Chelation can block metal-catalyzed redox cycling | A solution study found EDDHA and DTPA strongly inhibited iron- and copper-catalyzed ascorbate oxidation. [[5]](https://pubmed.ncbi.nlm.nih.gov/3566770/) | A measured-chelator checkbox gives a limited credit, with an explicit formulation-compatibility caveat. | Mechanism: medium-high; DIY magnitude: low |
| Ferulic acid + vitamin E can stabilize LAA in a designed system | The ferulic-acid study used 15% LAA, 1% vitamin E, 0.5% ferulic acid, and pH ≤3.5; it reported high chemical stability after one month at 45°C in its formulation. [[6]](https://www.sciencedirect.com/science/article/pii/S0022202X1532491X) | The CEF-style preset receives a credit only as an experiment-specific directional assumption. | Formulation-specific: medium; DIY transfer: low |
| Concentration changes apparent stability | The review summarizes an aqueous comparison in which a 1% solution lost more over 27 days than a 10% solution under the cited test conditions. [[1]](https://pmc.ncbi.nlm.nih.gov/articles/PMC8773188/) | Low concentration receives more pressure; higher concentration receives a modest credit, not a guarantee. | Directional: medium |
| Low-pH, light-protected, low-headspace packaging is plausible for stability | A stabilized-composition patent recommends low pH, deionized water, chelation, light-impermeable packaging, low temperature, and minimal headspace. [[7]](https://data.epo.org/publication-server/rest/v1.2/patents/EP0486499NWB1/document.pdf) | Supports the direction of the container, water, temperature, and headspace inputs. | Formulation/patent: medium; DIY transfer: low |

### Important out-of-domain evidence

Some numerical examples are useful as anchors but should not be treated as the model’s calibration set:

- In one review summary, a 1% aqueous solution lost about 21% after 27 days at room temperature and light, while a 10% solution lost about 8% under the cited conditions. [[1]](https://pmc.ncbi.nlm.nih.gov/articles/PMC8773188/) Those are particular test conditions, not a DIY guarantee.
- In one cream, dark-degradation rate constants were far lower than UV rates. [[3]](https://pmc.ncbi.nlm.nih.gov/articles/PMC3167265/) A cream’s viscosity, antioxidants, emulsifiers, and package mean that the number cannot be transplanted to a water serum.
- The EP patent reports long residual-LAA periods in carefully controlled vehicles and packaging. [[7]](https://data.epo.org/publication-server/rest/v1.2/patents/EP0486499NWB1/document.pdf) That is evidence for design levers, not evidence that a home dropper batch has the same shelf life.
- An aqueous stability thesis reports much shorter half-lives at higher temperature and higher concentration in its own formulation conditions. [[8]](https://ruj.uj.edu.pl/entities/publication/f7e4f3c0-5e44-4e97-bced-8182dc6b0dd1) It is useful context for temperature sensitivity, not a cosmetic-shelf-life validation.

## What the broad byproduct categories mean

The visualizer avoids pretending that a pie slice is an identified molecule. The categories are pathway families:

| Visualizer category | Chemistry it represents | Typical color expectation |
|---|---|---|
| **Intact LAA** | Reduced L-ascorbic acid, the intended active form | Fresh dilute aqueous LAA is usually clear/colorless, although raw materials and formulas can have a faint tint. |
| **DHA / early oxidation** | Monodehydroascorbate and dehydroascorbic acid, the initial oxidation region | No universal consumer-visible color. DHA is not intact LAA, and its bottle color cannot be used as a fixed percentage marker. |
| **DKG + cleavage acids** | 2,3-diketogulonic acid and later small acids such as threonic/oxalic-related products | Generally colorless or too dilute to explain strong visible color on their own. |
| **Acidic furans / carbonyls** | Furfural, 2-furoic acid, 3-hydroxy-2-pyrone, furanones, and related carbonyl products reported under acidic/heat/oxygen-limited routes | Parent compounds may be colorless-to-amber; later reactions can contribute to yellow/orange/brown color. |
| **Higher-pH products** | A different mixture of furans, ketones, and acids reported under alkaline or less-acidic conditions | Individual compounds are not a home color key; the mixture can age toward yellow/brown. |
| **Browning / condensation** | Later reactions among carbonyl products and, when present, amino compounds or other nucleophiles; colored furanones and polymeric/condensation bodies | Most relevant to deepening yellow, orange, red-brown, and brown appearance. |

The most useful simplified route for a pH-3.0–3.5 DIY batch is:

```text
LAA → monodehydroascorbate → DHA → DKG → smaller acids/carbonyls
                                      ↘ furans/furanones → colored condensation products
```

The exact branch depends on oxygen, pH, heat, light, metals, solvent, and other ingredients. The older DIY degradation section in the topic provides the longer byproduct inventory and color caveats: [rendered DIY degradation section](../08_vitamin_c_serums/index.html#doc3).

## Model construction

### 1. Pressure multipliers

The visualizer combines dimensionless multipliers into a relative pressure score:

```text
pressure = temperature × pH × light × air × container × water
           × concentration × stabilizer
```

The baseline is intentionally simple: roughly pH 3.3, room temperature, dark storage, normal dropper exposure, distilled water, 15% LAA, no modeled stabilizer. The visualizer uses a 55-day planning constant only to make age changes smooth and comparable. It is not a published rate constant and should not be read as one.

The pH term is based on a Henderson–Hasselbalch-style ionization proxy using an approximate LAA pKa of 4.1. It is not a complete mechanistic kinetic model. pH values above the intended acidic range receive greater pressure because more ascorbate is ionized and because the product distribution changes.

### 2. Survival and color warning

```text
survival = exp(− days × pressure / 55)
score = 100 × [0.72 × survival + 0.28 × (1 − color warning)]
        − pH measurement uncertainty
```

The 72/28 blend keeps color from becoming the entire answer while still allowing deep orange/brown color to move the recommendation decisively. The score is rounded in the interface and described as a **likelihood score**, not “percent LAA remaining.”

### 3. Relative allocation

The remainder, `1 − modeled chemical state`, is allocated among DHA, DKG/cleavage acids, acidic furans/carbonyls, higher-pH products, and browning/condensation using smooth pH-, age-, temperature-, and color-sensitive weights. Those weights are normalized to 100% of the modeled remainder. They are not measured concentrations and should not be used to make a toxicology claim about any one product.

### 4. Remake rule

The model produces a separate replacement window because a chemical score does not establish preservation. It starts at a deliberately conservative **7 days** for an unpreserved DIY water batch and adjusts for temperature, pH, package/light/air, water, measured stabilizers, and pH confidence. It is capped at:

- **7 days** when no preservative is selected;
- **5 days** when preservative status is unknown; or
- **14 days** when a compatible preservative is accurately measured.

Even in the best modeled case, the window is capped at 21 days before the unpreserved cap is applied. This is a personal DIY replacement recommendation, not a safety or shelf-life claim. Brown/orange color, unexpected odor, gas, particles, contamination, or a strong new sting overrides the score: remake/discard.

## How to use the controls

- **pH:** use a calibrated meter if possible. “pH 3.3” is meaningful only if the batch was actually measured after all pH-adjusting ingredients were added.
- **Color:** compare the same bottle against white paper under similar light. Record the first day it shifted from clear to straw/yellow; do not photograph it as though the RGB value were an assay.
- **Container:** a small amber dropper is not the same as a wide-mouth jar. An opaque airless pump gets a directional credit, but it does not automatically solve water activity, preservative compatibility, or filling contamination.
- **Headspace/opening:** this is a proxy for oxygen exposure. Nitrogen flushing and dissolved oxygen are not measured by the interface.
- **Stabilizers:** check only ingredients that were actually measured and dissolved in a compatible system. Ferulic acid plus vitamin E is not obtained by simply sprinkling both into water; the CEF-style preset is explicitly an experiment, not a recipe validation.
- **Microbial preservation:** select “none” unless a compatible preservative was accurately weighed and the finished formula was checked for pH and compatibility. The chart does not estimate microbial counts.

## What would improve the model

The next meaningful upgrade is not more decimal places. It would be a small, controlled personal dataset: same recipe and bottle, logged pH, temperature, opening count, standardized color photos, and periodic HPLC measurement of LAA/DHA. That could estimate a personal color-to-assay relationship for one exact formula. It would not automatically transfer to a different water source, pH, container, stabilizer, or concentration.

## Sources

1. [Chemical Stability of Ascorbic Acid Integrated into Commercial Products: A Review](https://pmc.ncbi.nlm.nih.gov/articles/PMC8773188/) — aqueous and commercial stability context; pH, oxygen, concentration, heat, light, DHA/DKG and downstream products.
2. [Effects of reaction parameters on self-degradation of L-ascorbic acid and self-degradation kinetics](https://pmc.ncbi.nlm.nih.gov/articles/PMC6049385/) — temperature/time effects, first-order behavior under tested conditions, and pH-dependent brown products.
3. [Photostability and Interaction of Ascorbic Acid in Cream Formulations](https://pmc.ncbi.nlm.nih.gov/articles/PMC3167265/) — formulation-, pH-, concentration-, and light-dependent degradation in a cream; not a DIY-water shelf-life study.
4. [Influence of Trace Elements on Stabilization of Aqueous Solutions of Ascorbic Acid](https://pmc.ncbi.nlm.nih.gov/articles/PMC3510389/) — trace-element effects in aqueous solution.
5. [Stabilization of ascorbate solution by chelating agents that block redox cycling of metal ions](https://pubmed.ncbi.nlm.nih.gov/3566770/) — chelator mechanism for iron/copper-catalyzed oxidation.
6. [Ferulic Acid Stabilizes a Solution of Vitamins C and E and Doubles its Photoprotection of Skin](https://www.sciencedirect.com/science/article/pii/S0022202X1532491X) — CEF-style system; strong formulation-specific stability result, not DIY proof.
7. [EP0486499B1 — Stable ascorbic acid compositions](https://data.epo.org/publication-server/rest/v1.2/patents/EP0486499NWB1/document.pdf) — low-pH, chelation, packaging, headspace, and temperature design examples from a patent.
8. [Badanie trwałości witaminy C w preparatach kosmetycznych](https://ruj.uj.edu.pl/entities/publication/f7e4f3c0-5e44-4e97-bced-8182dc6b0dd1) — formulation-specific half-life context across temperatures; included as out-of-domain context, not calibration.
9. [Stability of aqueous solutions of ascorbate for basic research and for intravenous administration](https://pmc.ncbi.nlm.nih.gov/articles/PMC10552410/) — acidic environment and redox-active metal control context.
10. [Topical L-ascorbic acid: percutaneous absorption studies](https://pubmed.ncbi.nlm.nih.gov/11207686/) — topical LAA concentration/pH context; not a storage study.
