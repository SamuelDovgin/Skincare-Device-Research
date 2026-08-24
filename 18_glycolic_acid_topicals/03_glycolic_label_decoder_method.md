# Glycolic Label Decoder: pH, Ionization, and Evidence Limits

*Compiled 2026-08-23. Cosmetic-formulation education, not a peel calculator, treatment prescription, safety clearance, or prediction of irritation or efficacy.*

## 0. Bottom line

“7% glycolic acid” is an incomplete description. If final pH is disclosed, the [glycolic label decoder](glycolic_label_decoder.html) can show an **ideal dilute-solution ionization scenario** and why two products with the same headline percentage can present different acid environments. It cannot recover the actual free-acid activity, buffer capacity, skin delivery, or safety of a finished formula.

## 1. Model specification

For the monoprotic acid equilibrium `HA ⇌ H⁺ + A⁻`, the ideal Henderson–Hasselbalch relationship gives:

`un-ionized fraction = 1 / (1 + 10^(pH − pKa))`

The tool uses a glycolic-acid `pKa = 3.83 at 25 °C`, a value cataloged by PubChem from an IUPAC ionization-constant source. [[1]](https://pubchem.ncbi.nlm.nih.gov/compound/Glycolic-Acid)

It then shows:

`illustrative un-ionized-acid equivalent = labeled glycolic-acid % × un-ionized fraction`

Example: at pH 3.83, the ideal model is 50% un-ionized; a labeled 5% formula would therefore display a 2.5% illustrative un-ionized equivalent. That is arithmetic, not a measured assay of the bottle.

## 2. Evidence ladder for every output

| Model layer | Class | Boundary |
|---|---|---|
| Labeled percentage and disclosed final pH | User-entered / manufacturer claim | Verify current region/formula; not independently measured here |
| pKa 3.83 at 25 °C | Primary-source parameter catalog | Temperature and solution conditions matter |
| Henderson–Hasselbalch fraction | Chemistry calculation | Assumes ideal equilibrium behavior |
| Percentage × fraction | Illustrative proxy | Not thermodynamic activity, tissue dose, peel depth, or irritation probability |

Real finished products can contain glycolate salts, neutralizers, buffers, polymers, solvents, emulsions, other acids, and water-binding ingredients. Activity coefficients and partitioning can make the simple calculation diverge from measured behavior.

## 3. Regulatory and practical boundary

FDA's current AHA consumer page summarizes the Cosmetic Ingredient Review framework of no more than 10% AHA, final pH at least 3.5, and sun-protection formulation or directions. [[2]](https://www.fda.gov/cosmetics/cosmetic-ingredients/alpha-hydroxy-acids) The tool marks inputs outside that **consumer-framework screen** for clarification. It does not declare inputs inside the boundary safe or effective.

The model should be used to ask better label questions:

- Is final pH disclosed for the exact formula?
- Is the percentage glycolic acid, total AHA, or a supplier solution?
- Is the formula buffered or partially neutralized?
- What vehicle and supportive ingredients are present?
- Does the product carry clear frequency, compromised-skin, and sun-sensitivity directions?

## 4. Deterministic checks

The tool's built-in self-test verifies:

- pH = pKa gives a 0.5 un-ionized fraction;
- increasing pH lowers the modeled un-ionized fraction;
- increasing labeled percentage at fixed pH raises the illustrative equivalent proportionally;
- results remain finite and between zero and the entered labeled percentage across the allowed grid.

## Evidence gaps

- No finished products were independently titrated or assayed for this tool.
- The calculation does not include buffer capacity, water activity, vehicle, contact time, temperature variation, or skin partitioning.
- An un-ionized fraction is not a validated irritation, penetration, exfoliation, collagen, or pigment endpoint.
- Labels often omit pH; the correct output in that case is **cannot calculate**, not an assumed pH.

## Sources

1. NIH/NLM PubChem. [Glycolic Acid, CID 757](https://pubchem.ncbi.nlm.nih.gov/compound/Glycolic-Acid) — dissociation constant catalog including pKa 3.83 at 25 °C.
2. FDA. [Alpha Hydroxy Acids](https://www.fda.gov/cosmetics/cosmetic-ingredients/alpha-hydroxy-acids) — consumer AHA framework, UV-sensitivity warning, and the role of concentration, pH, and other ingredients.
3. Wohlrab J et al. [Formulation of topical acidic products and acidification of the skin](https://pubmed.ncbi.nlm.nih.gov/33864274/) — finished 2% and 10% glycolic emulsions and short in-vivo skin-pH/barrier observations; formula-specific, not validation of the present proxy.
4. [Glycolic formulation and product-selection guide](index.html#doc2) — vehicle, routine, patch-test, and stop-rule context.
