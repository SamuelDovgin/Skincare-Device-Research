# Supplement Stack Audit and Adult Upper-Limit Model

*Compiled 2026-08-23. Arithmetic safety screen for generally healthy adults age 19+, not medical advice, a dosing recommendation, or a declaration that an intake below an upper limit is safe. Pregnancy, breastfeeding, disease, deficiency treatment, medication use, and clinician-directed protocols need individualized review.*

## 0. Bottom line

Multi-ingredient “skin,” hair/nail, multivitamin, immune, and standalone products can quietly duplicate the same nutrients. The [supplement stack checker](supplement_stack_checker.html) adds the amounts entered across products and compares the minimum known total with general adult tolerable upper intake levels (ULs). It does **not** judge collagen, HA, botanicals, probiotics, carotenoids, omega-3s, drug interactions, product quality, or efficacy.

## 1. Nutrients and boundaries in the model

| Nutrient entered | Adult UL used | Intake scope |
|---|---:|---|
| Preformed vitamin A | 3,000 mcg RAE/day | Food + supplements; excludes beta-carotene/provitamin A from this arithmetic |
| Vitamin C | 2,000 mg/day | Food + supplements |
| Vitamin D | 100 mcg/day (4,000 IU) | Food + supplements; `1 mcg = 40 IU` |
| Zinc | 40 mg/day | Food + supplements |
| Selenium | 400 mcg/day | Food + supplements |
| Niacin | 35 mg/day | Supplemental/fortified sources for the general UL; high-dose nicotinamide medical protocols are a separate clinician-managed lane |
| Vitamin E | 1,000 mg/day alpha-tocopherol | Supplemental/fortified sources |

The model uses U.S. NIH Office of Dietary Supplements adult ULs current when checked on 2026-08-23. [[1]](https://ods.od.nih.gov/factsheets/VitaminA-HealthProfessional/)[[2]](https://ods.od.nih.gov/factsheets/VitaminC-HealthProfessional/)[[3]](https://ods.od.nih.gov/factsheets/VitaminD-HealthProfessional/)[[4]](https://ods.od.nih.gov/factsheets/Zinc-HealthProfessional/)[[5]](https://ods.od.nih.gov/factsheets/Selenium-HealthProfessional/)[[6]](https://ods.od.nih.gov/factsheets/Niacin-HealthProfessional/)[[7]](https://ods.od.nih.gov/factsheets/VitaminE-HealthProfessional/)

## 2. Model specification

For each nutrient:

`entered total = optional baseline intake + Σ(product amount per serving × servings per day)`

The output bands are an archive attention aid:

- **under 80% of UL:** no arithmetic alert; not a safety clearance;
- **80–100% of UL:** near-limit review, especially because unentered food/fortified/medication sources can raise the true total;
- **over 100% of UL:** exceeds the general adult UL entered in this model; reconcile labels and discuss medical use with a clinician/pharmacist rather than using the tool to adjust treatment.

If baseline food/fortified/medication intake is left blank, totals for vitamin A, C, D, zinc, and selenium are **minimum known totals**, not total intake.

## 3. Important interpretation limits

- A UL is not a target, recommended allowance, optimal skin dose, or line between harmless and toxic.
- General ULs do not apply in the same way to clinician-supervised treatment of a diagnosed condition.
- Preformed vitamin A must be separated from beta-carotene; mixed-source labels need the preformed fraction before entry.
- The niacin UL is based chiefly on supplemental nicotinic-acid flushing. Nicotinamide has a different adverse-effect pattern at high doses; the 500 mg twice-daily skin-cancer trial protocol is medical chemoprevention, not a beauty-stack target.
- Product labels may list amounts per serving while directions specify multiple servings. The tool multiplies both, so enter them carefully.
- The model does not screen smoking-related beta-carotene risk, kidney stones, liver disease, pregnancy, bleeding, allergens, laboratory interference, or medication interactions.

## 4. How to use it

1. Photograph every Supplement Facts panel and front-label directions.
2. Enter the amount **per labeled serving** and actual planned servings per day.
3. Include multivitamins, powders, gummies, fortified drink mixes, and condition-specific products.
4. Add known baseline intake where the UL includes food/fortified/medication sources; otherwise interpret the total as a floor.
5. Resolve any unit/source ambiguity with a pharmacist or clinician rather than converting by guess.
6. Save the list and take it to medication reconciliation; do not use the result to self-manage a medical-dose protocol.

## Evidence gaps

- Diet is difficult to estimate and supplement labels may not reflect measured lot potency.
- ULs are population reference values, not individualized toxicity thresholds.
- Many skin supplements have no established UL yet can still cause adverse effects or interactions.
- The checker does not query the NIH Dietary Supplement Label Database or independently verify current product labels.

## Sources

1. NIH ODS. [Vitamin A and Carotenoids: Health Professional Fact Sheet](https://ods.od.nih.gov/factsheets/VitaminA-HealthProfessional/) — adult preformed-vitamin-A UL and source/conversion boundary.
2. NIH ODS. [Vitamin C: Health Professional Fact Sheet](https://ods.od.nih.gov/factsheets/VitaminC-HealthProfessional/) — adult UL and interaction/adverse-effect context.
3. NIH ODS. [Vitamin D: Health Professional Fact Sheet](https://ods.od.nih.gov/factsheets/VitaminD-HealthProfessional/) — adult UL and mcg/IU relationship.
4. NIH ODS. [Zinc: Health Professional Fact Sheet](https://ods.od.nih.gov/factsheets/Zinc-HealthProfessional/) — adult UL, copper-depletion risk, and medication interactions.
5. NIH ODS. [Selenium: Health Professional Fact Sheet](https://ods.od.nih.gov/factsheets/Selenium-HealthProfessional/) — adult UL and excess-intake effects; updated September 2025.
6. NIH ODS. [Niacin: Health Professional Fact Sheet](https://ods.od.nih.gov/factsheets/Niacin-HealthProfessional/) — supplemental UL and nicotinic-acid/nicotinamide adverse-effect distinctions.
7. NIH ODS. [Vitamin E: Health Professional Fact Sheet](https://ods.od.nih.gov/factsheets/VitaminE-HealthProfessional/) — adult supplemental alpha-tocopherol UL and bleeding-risk basis.
8. [Safety, interactions, and product selection](index.html#doc4) — clinician gates, interaction flags, product-quality checks, and the one-change-at-a-time rule.
