# Regulatory and Device Landscape

*Compiled 2026-07-06. This is research orientation, not medical/legal advice. Confidence legend: verified / limited claim / inference.*

## 0. Bottom line

In the United States, medical/aesthetic microneedling is not an open consumer-device lane. FDA's core category is:

- **Regulation:** 21 CFR 878.4430
- **Product code:** `QAI`
- **Class:** II
- **Use status:** prescription for legally marketed medical microneedling devices
- **Authorized indication family:** facial acne scars, facial wrinkles, neck wrinkles, and abdominal scars in specified adult populations/body areas
- **OTC status:** FDA says it has not authorized any microneedling medical devices for OTC sale

The live openFDA product-code `QAI` snapshot captured 2026-07-06 returned **26 records** with API metadata last updated **2026-06-22**. [[1]](data/openfda-qai-510k-2026-07-06.json)

## 1. Why this page exists

Microneedling marketing is a swampy little place: "FDA cleared," "FDA approved," "FDA facility," "professional grade," "at-home collagen induction," and "RF microneedling" get mixed together. This page separates:

- FDA-reviewed medical microneedling devices.
- superficial cosmetic rollers that may not be medical devices.
- non-medical marketing claims that sound medical.
- RF microneedling, which is regulated through RF/electrosurgical device pathways and carries a 2025 FDA safety warning.

## 2. FDA's microneedling category

### 2.1 The formal definition

FDA identifies a microneedling device for aesthetic use as a device using one or more needles to mechanically puncture and injure skin tissue for aesthetic use. The category **does not include** devices intended for transdermal delivery of topical products such as cosmetics, drugs, or biologics. [[2]](source_docs/fda-den160029-skinpen-precision-system-de-novo-summary.pdf)

| Field | FDA anchor |
|---|---|
| Generic type | Microneedling device for aesthetic use |
| Regulation | 21 CFR 878.4430 |
| Product code | QAI |
| Classification | Class II |
| Initial De Novo | DEN160029, SkinPen Precision System |
| Prescription status | Rx, 21 CFR 801.109 |
| Core special-control risks | infection/cross-contamination, adverse tissue reaction, electrical/EMC risks, nerve/vessel/tissue damage, scarring, hyper/hypopigmentation, mechanical/software malfunction |

### 2.2 Device vs non-device boundary

FDA's 2020 guidance says claims and design both matter. A product is more likely to be a regulated medical device when it:

- claims to treat scars, wrinkles, deep facial lines, cellulite, stretch marks, acne, dermatoses, alopecia, or wound healing;
- claims to stimulate collagen production, angiogenesis, or healing response;
- penetrates beyond the stratum corneum into living layers of skin;
- has needle length/sharpness/control features designed to reach living skin. [[3]](source_docs/fda-guidance-regulatory-considerations-microneedling-products-2020.pdf)

A product may avoid device status when it does not penetrate living skin and only claims to exfoliate, improve appearance, give smoother feel, or give a luminous look. That lower-regulatory path also means it should not be treated as a proven acne-scar/wrinkle treatment.

## 3. Legally marketed uses and patient safety line

FDA's microneedling page says it has legally authorized devices to improve:

- facial acne scars;
- facial wrinkles;
- abdominal scars;
- and, through specific device clearances, neck/periorbital wrinkle indications in defined populations. [[4]](source_docs/fda-microneedling-devices-page-2026-07-06.html)

FDA also says:

- no microneedling medical devices have been authorized for over-the-counter sale; [[4]](source_docs/fda-microneedling-devices-page-2026-07-06.html)
- microneedling devices are not approved to deliver cosmetics, topical medications, vitamin solutions, drugs, biologics, or PRP into skin; [[4]](source_docs/fda-microneedling-devices-page-2026-07-06.html)
- reusing a needle cartridge is unsafe and inconsistent with FDA authorization; [[4]](source_docs/fda-microneedling-devices-page-2026-07-06.html)
- the procedure may not be suitable for patients with bleeding/clotting disorders, immune suppression, uncontrolled diabetes, active infection/rash/cold sores, eczema/psoriasis/vitiligo/autoimmune disease, isotretinoin use within 6 months, keloid history, darker skin types where PIH risk is relevant, tanning/sun plans, malignancy/chemo/radiation/steroids, pregnancy/breastfeeding, or allergy to stainless steel/topical anesthetics. [[4]](source_docs/fda-microneedling-devices-page-2026-07-06.html)

## 4. openFDA QAI dataset snapshot

Captured: 2026-07-06  
API endpoint: `https://api.fda.gov/device/510k.json?search=product_code:QAI&limit=100`  
API metadata last updated: 2026-06-22  
Total records returned: 26  
Local files: [JSON](data/openfda-qai-510k-2026-07-06.json) / [CSV](data/openfda-qai-510k-2026-07-06.csv)

| Decision date | K / De Novo | Device | Applicant | Country | Read |
|---|---|---|---|---|---|
| 2018-03-01 | DEN160029 | SkinPen Precision System | Bellus Medical | US | Category-creating De Novo |
| 2018-09-07 | K180778 | Exceed Microneedling Device | Mt. Derm GmbH | DE | Facial wrinkle device |
| 2019-07-19 | K182407 | Exceed Microneedling device | Mt. Derm GmbH | DE | Acne-scar extension |
| 2020-04-09 | K192138 | Rejuvapen NXT | Refine USA | US | Acne-scar/standard QAI lane |
| 2020-04-10 | K200044 | SkinStylus SteriLock MicroSystem | Esthetic Education | US | Abdominal scarring lane |
| 2021-04-02 | K202243 | SkinPen Precision System | Crown Aesthetics | US | Neck wrinkle + acne-scar update |
| 2021-05-25 / 2021-11-24 | K203144 / K212558 | MicroPen EVO | Eclipse Medcorp | US | Prescription microneedling lane |
| 2021-07-09 / 2025-10-30 | K202517 / K252752 | Cytrellis Dermal Micro-Coring / ellacor | Cytrellis Biosystems | US | Adjacent micro-coring, not standard pen needling |
| 2022-10-21 | K222199 | Collagen P.I.N. | Induction Therapies | US | Percutaneous induction needling |
| 2022-12-20 | K221070 | DP4 Microneedling device | Equipmed USA | US | Professional microneedling |
| 2023-08-11 | K230420 | Dr. Pen Microneedling System (A20) | Guangzhou Ekai Electronic Technology | CN | Rx acne-scar indication |
| 2024-08-29 | K241400 | SkinPen Precision Elite System | Crown Aesthetics | US | Current SkinPen generation |
| 2025-08-25 | K243800 | PRO Pen Microneedling System | Dermalogica | US | Acne-scar indication, professional skincare entrant |
| 2026-02-19 | K253002 | SkinStylus SteriLock MicroSystem | Esthetic Medical | US | Periorbital wrinkle indication |
| 2026-05-13 | K252591 | Automatic Micro Needle System (CODE-X) | Woorhi Mechatronics | KR | Rx acne-scar indication |

Full table is in the CSV. The key trend is not "microneedling is newly consumer-safe"; it is that the professional prescription device category remains active and global.

## 5. Device examples with source-file anchors

| Device | Local source | FDA indication / key details | Safety/design note |
|---|---|---|---|
| SkinPen Precision System | [DEN160029 summary](source_docs/fda-den160029-skinpen-precision-system-de-novo-summary.pdf) | Facial acne scars in adults 22+ | Rx; sterile single-use cartridge; not for topical/drug/biologic delivery; >1.5 mm acne-scar safety/effectiveness not evaluated |
| SkinPen Precision System, K202243 | [K202243 PDF](source_docs/fda-k202243-skinpen-neck-wrinkles.pdf) | Neck wrinkles FST II-IV and facial acne scars all FST aged 22+ | Neck study used up to 2.5 mm under physician supervision |
| Exceed Microneedling Device | [K180778 PDF](source_docs/fda-k180778-exceed-facial-wrinkles.pdf) | Facial wrinkles in glabellar, periorbital, and cheek-fold areas; FST I-III; adults 22+ | Rx; 6 needles; 1.5 mm needle length in summary |
| Dr. Pen Microneedling System (A20) | [K230420 PDF](source_docs/fda-k230420-dr-pen-microneedling-system.pdf) | Facial acne scars in adults 22+ | Rx; recommended 1.5 mm; max setting 2.0 mm; 14 needles; 33G; sterile single-use cartridges |
| Dermalogica PRO Pen | [K243800 PDF](source_docs/fda-k243800-dermalogica-pro-pen.pdf) | Facial acne scars in adults 22+ | Rx Class II; 14-pin cartridge; max penetration 1.5 mm; testing included depth accuracy, sterility, fluid ingress, cleaning/disinfection validation |
| SkinStylus SteriLock MicroSystem, K253002 | [K253002 PDF](source_docs/fda-k253002-skinstylus-sterilock-periorbital-wrinkles.pdf) | Periorbital wrinkles in FST I-VI, adults 34+ | 36 needles, 2.5 mm max; 2026 clearance; periorbital-specific endpoint |
| CODE-X Automatic Micro Needle System | [K252591 PDF](source_docs/fda-k252591-code-x-microneedling-system.pdf) | Facial acne scars in adults 22+ | Rx; 12/14-pin cartridges; recommended 1.5 mm; max 2.0 mm; predicate Dr. Pen K230420 |

## 6. Consumer/home category

There are two very different home categories:

| Home product type | Example | What the claim means |
|---|---|---|
| Superficial cosmetic roller | StackedSkincare 0.2 mm roller | Product page positions it as cosmetic at-home use for appearance/texture/product performance, not medical scar remodeling. [[5]](https://stackedskincare.com/products/microneedling-face-refining-tool-2-0) |
| Deeper home stamp/roller with scar claims | Banish 0.5 mm stamp; replaceable 0.25-1.0 mm heads | The claim set overlaps medical-sounding outcomes. FDA has not authorized OTC microneedling medical devices; "FDA-cleared facility" wording is not the same as FDA-cleared device/indication. [[4]](source_docs/fda-microneedling-devices-page-2026-07-06.html)[[6]](https://banish.com/products/banish-kit-3-0) |
| Dissolvable microneedle patches | CurrentBody forehead/eye patches | These are cosmetic/transdermal patch-style products, not SkinPen-style mechanical medical microneedling; product claims are hydration/fine-line focused. [[7]](https://us.currentbody.com/products/currentbody-skin-rf-microneedling-treatment) |
| "RF microneedling" home kits | CurrentBody RF + microneedling patches | The microneedles and RF are separate; it is not a needle-electrode RF microneedling device. FDA's RF microneedling home-use warning applies to true RF microneedling devices, not to every product using the phrase. [[7]](https://us.currentbody.com/products/currentbody-skin-rf-microneedling-treatment)[[8]](source_docs/fda-rf-microneedling-safety-communication-2025-10-15.html) |

## 7. RF microneedling line

FDA's 2025 RF microneedling safety communication is the hard line:

- issued 2025-10-15;
- reports serious complications with RF microneedling for dermatologic/aesthetic procedures: burns, scarring, fat loss, disfigurement, nerve damage, and need for medical/surgical intervention;
- states RF microneedling is a medical procedure, not a cosmetic treatment;
- says these devices should not be used at home;
- describes RF microneedling devices as Class II devices cleared through 510(k). [[8]](source_docs/fda-rf-microneedling-safety-communication-2025-10-15.html)

RF microneedling is therefore in-office/procedure research, not a shopping lane for home devices.

## 8. Red-flag claim decoder

| Claim | How to interpret it |
|---|---|
| "FDA approved microneedling pen" | Usually wrong language. Most are Class II 510(k)-cleared or De Novo-authorized, not PMA-approved. Ask for K-number and indication. |
| "Made in an FDA-cleared facility" | Facility language does not prove the device is cleared for scars/wrinkles or OTC sale. |
| "Professional grade at home" | Conflicts with FDA's no-OTC-medical-device statement if the product is truly medical microneedling. |
| "Use with vitamin C/PRP/exosomes" | FDA does not authorize microneedling devices for transdermal delivery of cosmetics, drugs, biologics, vitamin solutions, or PRP. |
| "RF microneedling pen for home use" | Avoid. FDA says RF microneedling devices should not be used at home. |
| "All skin types" | Check whether the actual clearance/study included FST V-VI; many wrinkle clearances are narrower than marketing language. |

## Evidence gaps

- openFDA QAI gives useful clearance metadata but does not fully extract indications, depth, cartridge design, and study details; those require individual summaries/IFUs.
- The QAI product code captures adjacent mechanical technologies such as micro-coring; dataset rows need manual interpretation.
- RF microneedling devices are not all under QAI; they should be tracked separately through their RF/electrosurgical 510(k) summaries.
- Consumer product pages change frequently; current home roller/stamp pricing and claims should be periodically rechecked.

## Sources

1. openFDA device 510(k) API query, product code QAI, captured 2026-07-06. [JSON](data/openfda-qai-510k-2026-07-06.json) / [CSV](data/openfda-qai-510k-2026-07-06.csv) - primary dataset for 26 QAI records and API last-updated metadata.
2. FDA De Novo Summary DEN160029, SkinPen Precision System. [Local PDF](source_docs/fda-den160029-skinpen-precision-system-de-novo-summary.pdf) - primary source for QAI/878.4430, Rx status, category definition, and topical-delivery exclusion.
3. FDA Guidance, Regulatory Considerations for Microneedling Products. [Local PDF](source_docs/fda-guidance-regulatory-considerations-microneedling-products-2020.pdf) - primary source for device/non-device boundary and claim examples.
4. FDA Microneedling Devices page. [Local HTML](source_docs/fda-microneedling-devices-page-2026-07-06.html) - primary source for legally authorized uses, no OTC authorization, risk list, contraindication prompts, cartridge reuse warning, and topical/PRP delivery boundary.
5. StackedSkincare Microneedling Face Refining Tool page, accessed 2026-07-06. https://stackedskincare.com/products/microneedling-face-refining-tool-2-0 - product-source example of 0.2 mm at-home cosmetic positioning.
6. Banish Kit 3.0 / Banisher 3.0 product pages, accessed 2026-07-06. https://banish.com/products/banish-kit-3-0 and https://banish.com/products/banisher-heads - product-source examples of 0.5 mm home stamp and replaceable 0.25-1.0 mm heads with scar/fine-line/dark-spot claims.
7. CurrentBody Skin RF Microneedling Treatment and Forehead Microneedling Patch pages, accessed 2026-07-06. https://us.currentbody.com/products/currentbody-skin-rf-microneedling-treatment and https://us.currentbody.com/products/currentbody-skin-forehead-microneedling-patch - product-source examples of dissolvable microneedle patches plus separate RF wand.
8. FDA RF Microneedling Safety Communication, issued 2025-10-15. [Local HTML](source_docs/fda-rf-microneedling-safety-communication-2025-10-15.html) - primary source for RF microneedling risks and no-home-use warning.
