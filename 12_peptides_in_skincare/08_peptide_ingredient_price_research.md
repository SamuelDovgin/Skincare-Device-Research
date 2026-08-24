# Ingredient-by-Ingredient Peptide Price Research

## Public procurement proxies for the 25-formulation scan

**Access date:** 2026-08-14<br>
**Research lane:** raw-material and commercial-peptide pricing only<br>
**Related model:** [Peptide Ingredient Cost Model](index.html#doc7)

## Bottom line

The creator’s actual cost is usually private. A finished-skincare brand may buy a peptide through a distributor, under a negotiated contract, at a different assay, in a carrier solution, or as a proprietary blend. Public webpages therefore cannot prove what a brand paid. They can, however, establish a defensible set of **public replacement-cost anchors**.

This document is deliberately source-first. It does **not** reverse-calculate a supplier price from a retail bottle, a product’s selling price, or a desired total. It does not allocate an unexplained bottle total across ingredients. It does not force component line items to sum to a product-level estimate.

Where a formulation percentage and a public unit price are both independently available, a later model may make a simple forward calculation:

`published unit price × independently disclosed formula amount = source-based line estimate`

That is a transparent scenario, not the creator’s invoice. If either input is missing, the line remains **not priced**.

## Procurement-fit correction: cosmetic inputs now outrank research vials

The source audit found a structural error in the earlier research: several chemically related prices came from milligram research vials or pure powders even though the finished formula would normally use a cosmetic solution, concentrate, or branded premix. Those records remain in the evidence ledger for traceability, but they are now labeled **excluded** or **evidence only** and cannot feed the product-cost model.

| Material | Selected formulation source | One best public anchor | Why this source wins |
|---|---|---:|---|
| TEGO PEP 4-17 | Escentials of Australia cosmetic solution; 2,300 ppm Tetrapeptide-21 | **$2.18/g** at the public 500 g pack, using 0.70 USD/AUD | Same named technology, carrier class, assay, refrigeration guidance, and 0.5–5% formulation use rate |
| Progeline | New Directions Australia glycerin/water/Tripeptide-2 solution | **$1.00/g** at the public 1 kg pack | Same named commercial solution with 0.2–2% use guidance |
| Collaxyl / Hexapeptide-9 | Bellahut water/glycerin cosmetic concentrate | **$1.04/g** at 120 mL, normalized with the published density range | Ready-to-formulate concentrate with INCI, 0.5–5% use rate, storage, and public pack ladder |
| Sodium DNA / PDRN | Cosmetic powder listings plus a 99.8% quote-only topical supplier record | **$10/g** category benchmark | Correct topical material class; still low confidence because seller specifications and QC vary materially |
| FGF2-STAB | Cosmetics-specific thermostable FGF2 listing | **Quote required** | The visible $721 price has no verifiable package mass, so no $/g is calculated |

The ChemicalBook Tetrapeptide-21 listing supplied in the audit is explicitly packaged as **2 mg, 5 mg, or 10 mg vials**. It is therefore not used for Geek & Gorgeous or any other skincare-formulation cost estimate.

## How to read the price evidence

### Price categories kept separate

| Category | What the number represents | Can it stand in for pure peptide? |
|---|---|---|
| Pure or near-pure powder | An INCI/CAS ingredient listing, generally with a stated purity | Sometimes, but assay, salt form, endotoxin, and scale still matter |
| Branded commercial technology | A supplier’s named blend, usually peptide(s) plus water, glycerin, glycols, polymer, or delivery system | No. Use the blend price as a blend price |
| Formulated suspension or solution | A supplier’s ready-to-use suspension with a stated concentration or carrier system | No. It is a finished raw material, not pure peptide |
| Research-grade catalog material | Small-vial material sold for laboratory work | Usually a high ceiling, not a cosmetic manufacturing cost |
| Import or trade-data signal | Declared shipment value or marketplace transaction signal | Only a cross-check; unit, freight, and classification may be unclear |
| No public price | Identity or technical information was found, but no defensible public price was located | Do not substitute an unrelated peptide |

The normalized figures below preserve the source’s original currency and commercial form where conversion would create false precision. USD-per-gram comparisons are rounded and are used only when the listing makes the unit basis reasonably clear. For example, `$80–200/g powder` and `$4.6–7.3/g formulated suspension` are not contradictory prices for the same thing; they are different grades and purchasing contexts.

### Confidence labels

- **High:** a public price, unit basis, and material identity are clear enough to quote directly.
- **Medium:** the listing is usable but its grade, unit basis, carrier, or marketplace context limits comparability.
- **Low:** trade data, a placeholder, an ambiguous marketplace quote, or a product containing the ingredient rather than the ingredient itself.
- **No price:** the searches produced technical or identity sources but no responsible public price anchor.

### What “likely creator cost” means here

The phrase means a **procurement scenario inferred from public scale and grade evidence**, not a claim about a named brand’s books. A small indie formulator buying 50 g from a specialty distributor may face something close to the small-lot listing; a large manufacturer buying a kilogram or more may negotiate below the public quote. Contract manufacturing, testing, cold-chain handling, minimum orders, import duty, and stability work are excluded.

## Price map: direct and commercial technology anchors

The table is an index, not a reconciliation. Each row stands on its own evidence. “Public anchor” is the range actually found in the sources, while “reasonable scenario” is the narrowest procurement interpretation that can be made without pretending the public source is an invoice.

| Ingredient or technology | What was priced | Public anchor | Reasonable procurement scenario | Confidence |
|---|---|---:|---|---|
| Acetyl Hexapeptide-8 / Argireline | Bulk powder listings; separate formulated suspension | Pure powder listings: about **$1–42/kg**; FormulateLabs suspension: about **$8,838–14,000/kg** | Bulk powder is the relevant first scenario; use suspension only when the formulation buys an Argireline-type liquid | Medium |
| Matrixyl 3000 | Sederma/Trulux commercial blend | About **$1.14–2.70/g** across 1 kg to 50 g public pack sizes | Commercial Matrixyl 3000 blend, not 8–10% pure Palmitoyl Tripeptide-1/Tetrapeptide-7 | High |
| Matrixyl Synthe’6 | Sederma/Trulux commercial blend | About **$1.27–2.95/g** across 1 kg to 50 g public pack sizes | Commercial Synthe’6 blend; do not replace it with a pure PT-38 quote without labeling the substitution | High |
| Palmitoyl Tripeptide-38 | Pure INCI suspension and specialty powder listings | FormulateLabs suspension about **$4.63–7.33/g**; small-lot powder listings about **$80–200/g** | Use the suspension band for a ready-to-formulate INCI material; use the powder band only for small-lot/high-purity sourcing | Medium |
| Palmitoyl Tripeptide-5 / SYN-COLL | Commercial SYN-COLL and pure/raw listings | Commercial blend about **$0.75–1.85/g**; small-lot raw listings about **$20–85/g** | Commercial SYN-COLL is the relevant anchor when a label names SYN-COLL | Medium |
| Pentapeptide-18 / Leuphasyl | Formulated suspension | About **$73–116/g** at 100 g to 1 kg pack sizes | Ready-to-use commercial suspension; no public pure-powder price located | Medium |
| Dipeptide Diaminobutyroyl Benzylamide Diacetate / SYN-AKE | Pure/small-lot and bulk supplier listings | About **$0.50–6/kg** in bulk quote snippets versus about **$80/g** small-lot | Large grade/scale spread; use a scenario band rather than one “true” price | Low–Medium |
| GHK-Cu / Copper Tripeptide-1 | Cosmetic powder listings and specialty small lot | About **$40–45/kg** bulk marketplace listing; about **$7.99/g** 10 g specialty listing | Bulk cosmetic powder is the most useful creator-cost scenario; specialty price is a ceiling | Medium |
| Caprooyl Tetrapeptide-3 | Bulk powder and formulated suspension | About **$100–120/kg** bulk listing; FormulateLabs suspension about **$7.64–12.11/g**; small-lot listing about **$100–200/g** | Use the bulk powder only for a pure-material scenario; use suspension when the formulation buys a ChroNOline-class active | Medium |
| Tridecapeptide-1 | Import/sample trade signal and quote-only supplier | Volza shows a **10 g sample at $26.32**; supplier pages provide no regular public price | Treat the sample shipment as a low-confidence ceiling, not a stable manufacturing rate | Low |
| Palmitoyl Tripeptide-1 | Pure powder listings | About **$20–85/g** small/mid-lot; one FOB quote about **$25–30/g** | Pure peptide only where the formula actually buys pure PT-1; otherwise use the Matrixyl blend price | Medium |
| Palmitoyl Tetrapeptide-7 | Pure powder listings | About **$4–9/kg** bulk listing versus about **$50–95/g** small-lot listings | Treat bulk quote as an uncertain floor and small lot as a ceiling; Matrixyl 3000 is usually the better commercial proxy | Low–Medium |
| Palmitoyl Hexapeptide-12 | Pure powder and formulated INCI suspension | About **$27.68/g** suspension; about **$100–150/g** specialty powder | Choose based on whether the formula names the pure peptide or a supplier suspension | Medium |
| Trifluoroacetyl Tripeptide-2 / Progeline | New Directions commercial cosmetic solution | **$1.00/g** selected 1 kg public anchor; smaller public packs reach about $2.72/g | Use the matched glycerin/water/Tripeptide-2 solution, not pure/research peptide | High |
| Palmitoyl Pentapeptide-4 / Matrixyl | Pure powder listings | About **$28–132/g**, with one much higher Chinese quote | Use the lower public range cautiously; do not confuse this with Matrixyl 3000 | Medium |
| Melanostatine-5 / Nonapeptide-1 | Powder marketplace and formulated suspension | About **$25–110/g** small-lot marketplace range; FormulateLabs suspension about **$19.69–31.20/g** | Commercial cosmetic suspension is the cleaner anchor; marketplace powder quotes are noisy | Low–Medium |
| Acetyl Hexapeptide-1 / Munapsys | Commercial active solution | About **AU$1.76–3.56/g** from 1 kg to 17 g packs | Commercial Munapsys solution; not pure Acetyl Hexapeptide-1 | High |
| Skinarch | Commercial active blend | **MXN 7,039.41/kg** public 1 kg listing | Blend price only; the blend contains a carrier and a proprietary peptide technology | Medium |
| X50 Antiaging | Commercial X50 active/premix | About **UAH 0.67–0.83/g** at 100–10 g listings | Commercial X50 active; no pure price for Copper Heptapeptide-14 Pantothenate or Heptapeptide-15 Palmitate found | Medium |
| Oligopeptide-68 | Pure/raw marketplace and formulated suspension | About **$25–400/g** raw listings; FormulateLabs suspension about **$64.63–102.40/g** | Use suspension band for a formulation raw material; raw marketplace range is highly uncertain | Low–Medium |
| Acetyl Octapeptide-3 / SNAP-8 | Small-lot listing and diluted active | About **£48.65–52.39/g** listing with unit ambiguity; 15 mL premix about **€21.20** | Do not treat the premix as pure; verify the seller’s unit basis before using the powder quote | Low–Medium |
| SYN-TACKS | Commercial solution | The Herbarie lists **$655/lb** at the largest pack, about **$1.44/g**, with higher small-pack prices | Commercial SYN-TACKS solution; no pure peptide price needed for a label that names the technology | High |
| TEGO PEP 4-17 / Tetrapeptide-21 | Escentials commercial cosmetic solution | **$2.18/g** selected 500 g public anchor; $2.56–3.64/g at 100–5 g | Use the matched 2,300 ppm TEGO solution; pure and research-vial prices are excluded | High |
| GF MiniProtein / Expression Line MiniProtein | Branded recombinant-growth-factor technologies | No public ingredient price | Contract or distributor quote required; do not substitute commodity EGF/FGF | No price |

## Expanded Formulate Labs catalogue scan

**New scan date: 2026-08-14.** Formulate Labs materially improves the evidence base because its material pages expose a public pack ladder, a named INCI, an active-strength option, recommended formulation use rates, carrier format, and, for many entries, a composition panel. These are **ready-to-formulate suspension prices**, not pure-peptide powder prices and not the price a large brand necessarily pays under contract.

The most useful interpretation is: “What would a small or mid-size formulator pay for a documented, drop-in cosmetic material at the listed pack size?” It is not: “What is the molecule worth?” or “What did a finished-product creator pay?”

| Formulate Labs material | Public pack ladder | Supplier use-rate / assay information | How it changes the model |
|---|---:|---|---|
| Acetyl Hexapeptide-8 | **$8.84–14.00/g** across 18 kg to 100 g | 0.05% standard / 0.5% lab concentrate; 2–10% suspension use | Gives a ready-to-use Argireline-class ceiling; do not mix with $/kg powder listings |
| Acetyl Octapeptide-3 | **$67.40–106.80/g** | 0.05% standard / 0.5% lab concentrate; 2–10% use | Adds a direct SNAP-8-class material reference |
| Copper Tripeptide-1 | **$0.80–1.25/g** | 0.1% standard / 1% lab concentrate; 0.5–10% use; 0.01–0.1% pure-active typical | Replaces the former dependence on noisy GHK-Cu marketplace powder quotes for suspension scenarios |
| Dipeptide Diaminobutyroyl Benzylamide Diacetate | **$125.04–198.13/g** | 0.05% standard / 0.5% lab concentrate; 2–8% use | Shows why SYN-AKE has a very different cost profile from bulk snippet prices |
| Palmitoyl Tripeptide-1 | **$8.83–14.00/g** | 0.01% standard / 0.1% lab concentrate; 1–10% use | Supplies a pure-INCI cross-check for Matrixyl 3000’s components |
| Palmitoyl Tetrapeptide-7 | **$6.44–10.20/g** | 0.02% standard / 0.2% lab concentrate; 1–10% use | Same component-level cross-check; not the Matrixyl 3000 blend price |
| Palmitoyl Tripeptide-5 | **$7.64–12.11/g** | 0.1% standard / 1% lab concentrate; 1–3% use | Direct pure-INCI analogue for Syn-Coll scenarios |
| Palmitoyl Tripeptide-38 | **$4.63–7.33/g** | 0.03% standard / 0.3% lab concentrate; 2–10% use | Direct pure-INCI analogue for Synthe’6 scenarios |
| Palmitoyl Tripeptide-8 | **$44.93–71.20/g** | 0.03% standard / 0.3% lab concentrate; 1–5% use | Adds a priced neurocosmetic/sensitive-skin reference |
| Palmitoyl Pentapeptide-4 | **$7.84–12.42/g** | 0.05% standard / 0.5% lab concentrate; 3–8% standard-suspension input for 3–5 ppm active | Replaces broad powder-only ranges for ready-to-use pal-KTTKS material |
| Palmitoyl Hexapeptide-12 | **$23.29–36.91/g** | 0.01% standard / 0.1% lab concentrate; 1–5% use | Adds a direct Biopeptide-EL-class pure-INCI suspension reference |
| Pentapeptide-18 | **$73.08–115.80/g** | 0.05% standard / 0.5% lab concentrate; 2–10% use | Adds a high-cost expression-line peptide reference |
| Tetrapeptide-21 | **$50.56–80.11/g** | 0.01% standard / 0.1% lab concentrate; 1–5% use | Separates pure TP-21 from TEGO Pep 4-17 commercial-premix pricing |
| Tripeptide-1 / uncomplexed GHK | **$12.05–19.09/g** | 0.01% standard / 0.1% lab concentrate; 1–10% use | Provides a matched non-copper GHK reference for NIOD-style formulas |
| Caprooyl Tetrapeptide-3 | **$7.64–12.11/g** | 0.03% standard / 0.3% lab concentrate; 0.3–2.5% use | Adds a suspension reference beside much cheaper industrial powder listings |
| Nonapeptide-1 | **$19.69–31.20/g** | 0.001% standard / 0.01% lab concentrate; 1–5% use | Adds a direct Melanostatine-5-class suspension reference |
| Oligopeptide-68 | **$64.63–102.40/g** | 0.001% standard / 0.01% lab concentrate; 2–10% use | Adds a direct β-White-class suspension reference |
| Recombinant sh-Oligopeptide-1 / EGF | **$349–420/g** for 1–10 g vials | 0.08% standard / 0.8% concentrate; 1–10 ppm active stated | Shows the small-vial recombinant-protein ceiling; not a bulk cosmetic quote |
| SYN-TACKS component analogues | **$89.00–93.49/g** for two component suspensions | 0.001–0.01% component options | Useful only as component sensitivity; the Herbarie commercial SYN-TACKS ladder remains the matched blend source |

The complete record-by-record ledger is in [`data/peptide_price_source_records.csv`](data/peptide_price_source_records.csv). It preserves the source URL, material form, pack examples, normalized USD/g anchor, use-rate evidence, and whether the price is direct, marketplace, research-grade, or no-price.

### What the new source set does not prove

- It does not prove that a retail brand bought the same material, at the same assay, or at the same pack size.
- A suspension’s **$/g is a price for the suspension**, not the pure peptide. The page’s active percentage must be retained when converting to a pure-active equivalent.
- The lowest public pack price is not automatically the likely creator price. Contract manufacturing, distributor margins, cold-chain, COA/SDS documentation, and minimum orders can move the real number.
- A matched branded complex remains preferable to a pure-INCI analogue when the formula names the trade technology. The new pages let the model show both rather than silently substituting one for the other.

## Ingredient records and source trails

The records below show what each source contributes. A source that proves identity, assay, or recommended use level is valuable even when it does not publish a price; it prevents an unrelated price from being attached to the ingredient.

### Acetyl Hexapeptide-8 / Argireline

LookChem shows a 99% supplier listing at **$42/kg with a 1 kg MOQ**, while another supplier snippet shows **$5–25/kg at a 25 kg MOQ**. Echemi displays a **$1/kg** quote, but that is treated as a suspicious low outlier rather than a base case. [[1]](https://mingqichem.lookchem.com/products/CasNo-616204-22-9-Acetyl-Hexapeptide-8-37402717.html) [[2]](https://senyi.lookchem.com/products/CasNo-616204-22-9-Cosmetics-Raw-Material-Argireline-Powder-Acetyl-Hexapeptide-8-HexapeptideCAS-616204-22-9-26087729.html) [[3]](https://www.echemi.com/produce/pr2604291965-factory-supply-acetyl-hexapeptide-8-argireline-cas-616204-22-9-99.html)

FormulateLabs gives a different product: an Acetyl Hexapeptide-8 suspension at **$1,400/100 g, $10,500/kg, and $159,090.91/18 kg**, or roughly **$8.84–14/g**. That is a formulated suspension and must not be mixed with the $/kg pure-powder quotes. [[4]](https://www.formulatelabs.ai/materials/acetyl-hexapeptide-8)

**Use in the formulation crosswalk:** The Ordinary’s “Argireline Solution 10%” is a commercial solution headline, not proof that the bottle contains 10% pure peptide. A source-first model should price it as an Argireline-type solution only if the supplier concentration and pack form are matched.

### Matrixyl 3000 and its two component peptides

Trulux publicly lists the commercial Matrixyl 3000 blend at **AU$207.80/50 g, AU$356.10/100 g, and AU$1,760/1 kg**. Using a rounded 0.65 USD/AUD conversion only for orientation gives approximately **$2.70/g, $2.31/g, and $1.14/g**. The official composition document identifies the material as a carrier mixture containing Palmitoyl Tripeptide-1 and Palmitoyl Tetrapeptide-7. [[5]](https://trulux.com/products/matrixyl-3000/) [[6]](https://www.ewlerp.com/___country___/uploadedfile/rawmaterial/cat2/reg%20non-animal%20testing%20%20statement%20_MATRIXYL%203000.pdf)

New Directions Australia independently lists Matrixyl 3000 at **AU$60.50/17 g, AU$330/100 g, AU$1,100/500 g, and AU$1,749/kg**, which is directionally consistent with the Trulux commercial-premix ladder after currency conversion. [[6a]](https://www.newdirections.com.au/1-Kg-Matrixyl-R-3000)

This is the relevant public anchor when a finished formula says **Matrixyl 3000**. It is not valid to take the bottle’s Matrixyl percentage and quietly treat that percentage as pure Palmitoyl Tripeptide-1 plus Palmitoyl Tetrapeptide-7.

Pure-peptide sources are useful as a sensitivity check. Rhine lists Palmitoyl Tripeptide-1 at **$20–85/g**, while Echemi shows a **$25–30/g** FOB quote. Palmitoyl Tetrapeptide-7 marketplace snippets range from **$4–9/kg** at one bulk MOQ to **$50–95/g** in small lots. These ranges are not a substitute for the commercial Matrixyl price. [[7]](https://www.rhinebiotech.com/cosmetic-raw-materials/62318807.html) [[8]](https://www.echemi.com/produce/pr2501271072-wholesale-price-cosmetic-grade-beauty-product-palmitoyl-tripeptide-1-cas-147732-56-7.html) [[9]](https://www.made-in-china.com/price/prodetail_Herbal-Extract_wpvYimQbbFcr.html) [[10]](https://www.alibaba.com/insights/palmitoyl-tetrapeptide-7.html)

### Matrixyl Synthe’6 and Palmitoyl Tripeptide-38

Trulux lists Matrixyl Synthe’6 at **AU$227/50 g, AU$389.60/100 g, and AU$1,947.70/1 kg**, approximately **$2.95/g, $2.53/g, and $1.27/g** at the same rounded conversion. [[11]](https://trulux.com/products/matrixyl-synthe-6/)

As a second public cross-check, New Directions lists **1 kg of Matrixyl Synthe’6 at AU$1,357.40**, or approximately **$0.88/g** using the same rounded conversion. This is a single distributor pack point, so I keep the broader Trulux ladder as the main low/base/high anchor rather than pretending the one listing is a full market range. [[11a]](https://www.newdirections.com.au/epages/newdirections.sf/en_AU/?ObjectPath=%2FShops%2Fnewdirections%2FProducts%2FRMAA1KMATRSYN6)

FormulateLabs separately lists Palmitoyl Tripeptide-38 as a pure-INCI suspension at **$732.79/100 g, $5,480/kg, and $83,251.40/18 kg**, or about **$4.63–7.33/g**. It explicitly distinguishes that product from Matrixyl Synthe’6. Small-lot powder listings are much higher, around **$80–200/g**. [[12]](https://www.formulatelabs.ai/materials/palmitoyl-tripeptide-38) [[13]](https://www.rhinebiotech.com/dp-cosmetic-peptide-palmitoyl-tripeptide-38-k5540493.html) [[14]](https://www.tradeindia.com/products/palmitoyl-tripeptide-38-8615510.html)

### Palmitoyl Tripeptide-5 / SYN-COLL

Trulux’s public SYN-COLL pricing is approximately **$0.75/g at 1 kg**, rising to roughly **$1.5–1.85/g** at smaller packs. Rhine’s pure/raw listing is about **$20–85/g**. The correct source choice follows the label: SYN-COLL should use the commercial blend anchor; a pure Palmitoyl Tripeptide-5 claim should use the pure/raw band. [[15]](https://trulux.com/products/syn-coll/) [[13]](https://www.rhinebiotech.com/dp-cosmetic-peptide-palmitoyl-tripeptide-38-k5540493.html)

### Pentapeptide-18 / Leuphasyl

FormulateLabs lists Pentapeptide-18 as a suspension at **$11,580/100 g, $86,850/kg, and $1,315,475.27/18 kg**. That normalizes to approximately **$73.08–115.80/g**. TCS NEXUS and Saien provide B2B technical/supplier pages but no public unit price, so the suspension range is the only reasonably explicit public cost anchor found. [[16]](https://www.formulatelabs.ai/materials/pentapeptide-18) [[17]](https://www.tcspeptides.com/products/pentapeptide-18/) [[18]](https://www.saienbiotech.com/product/pentapeptide-18-enkephalin-mimetic-peptide-leuphasyl/)

### SYN-AKE / Dipeptide Diaminobutyroyl Benzylamide Diacetate

A small-lot LookChem listing shows about **$80/g at a 1 g MOQ**. ChemicalBook supplier snippets show radically lower bulk quotes, including roughly **$0.50–6/kg** and a separate **$500/kg** supplier quote. DSM’s formulation guideline confirms the branded technology and use context but does not publish price. [[19]](https://mingqichem.lookchem.com/products/CasNo-823202-99-9-Syn-ake-37236641.html) [[20]](https://www.chemicalbook.com/Manufacturers/Dipeptide-diaminobutyroyl-benzylamide-diacetate.htm) [[21]](https://www.dsm.com/content/dam/protected/personal-care/en_US/peptides/peptides_distributor/syn-ake_formulation_guidelines_2020-01.pdf)

The spread is not a typo: it mixes a tiny high-purity listing, bulk supplier snippets, and uncertain marketplace quote units. The responsible output is a wide sensitivity band, not a single midpoint.

### GHK-Cu / Copper Tripeptide-1

Alibaba search results show a cosmetic-grade **99% GHK-Cu listing at roughly $40–45/kg for 1 kg**. Vitaco and ExperChem provide higher-quality technical descriptions, including powder and purity information, but do not publish a price. Albochem’s specialty listing shows **$79.90/10 g**, or **$7.99/g**, which is treated as a small-lot ceiling. [[22]](https://www.alibaba.com/search/page?SearchScene=imageTextSearch&productId=1601385656954) [[23]](https://vitacobio.com/ghk-cu-raw-material.html) [[24]](https://experchem.com/files/files/file/58f05bb6-f076-49ce-8cc7-a2f260680da3/Copper-tripeptide-1-Productinformation-ExperChem-Rohstoff.pdf) [[25]](https://albochem.com/product/ghk-cu-raw-powder-copperii-glycyl-l-histidyl-l-lysinate-%E2%89%A599-purity-10-grams/)

The bulk powder quote is the most useful scenario for a creator’s ingredient cost when a formula truly uses pure Copper Tripeptide-1. It should not automatically be applied to a proprietary **Copper Tripeptide Complex**, liposomal material, or a finished copper-peptide serum.

### Palmitoyl Hexapeptide-12, Progeline, Matrixyl, and other pure-peptide listings

- **Palmitoyl Hexapeptide-12:** FormulateLabs lists approximately **$27.68/g** for a 1 kg suspension. Greenway lists **$150/g** at 1–1,000 g and **$100/g** at larger quantity; BioMart shows small 50–100 mg prices. [[26]](https://www.formulatelabs.ai/materials/palmitoyl-hexapeptide-12) [[27]](https://www.greenwaybiochem.com/Cosmetic-Peptide-Anti-Wrinkle-Palmitoyl-Hexapeptide-12-Powder-617?d=1.7) [[28]](https://www.biomart.cn/infosupply/118238363.htm)
- **Trifluoroacetyl Tripeptide-2 / Progeline:** New Directions lists the commercial glycerin/water/Tripeptide-2 solution at **AU$66/17 g, AU$275/100 g, AU$770/500 g, and AU$1,430/kg**. Using 0.70 USD/AUD gives a selected 1 kg anchor of approximately **$1.00/g**. The older pure-peptide and research-catalog records are retained only as excluded evidence. [[29]](https://www.newdirections.com.au/RMAA1KPROGELIN) [[30]](https://cms.safic-alcan.com/app/uploads/2026/01/tds_PROGELINE_TDS_2021_EN-58642.pdf)
- **Palmitoyl Pentapeptide-4 / Matrixyl:** public listings range from roughly **$28–32/g** at LookChem to **$132/g** at W&Z Biotech, with another very high Chinese listing. This is Matrixyl, not Matrixyl 3000. [[31]](https://jiuzhoushiye.lookchem.com/products/CasNo-214047-00-4-Palmitoyl-pentapeptide-4-CAS-NO-214047-00-4-37542146.html) [[32]](https://www.wzbiotech.com/Raw-Material-Cosmetics-Peptides-Matrixyl-Acetate-Palmitoyl-Pentapeptide-4-CAS-214047-00-4-1940?page=3&tag=wholesale)
- **Palmitoyl Tripeptide-8:** ChemicalBook displays a listing around **$75/kg for 1 kg** and **$750 for 10 kg**, but the price presentation is ambiguous. GlobalSources provides technical context without price. This is a low-confidence floor, not a verified contract quote. [[33]](https://www.chemicalbook.com/ProductDetail_EN_palmitoyl-tripeptide-8_2495020.htm) [[34]](https://pdt.static.globalsources.com/IMAGES/PDT/SPEC/252/K1220540252.pdf)

### Melanostatine-5 / Nonapeptide-1

FormulateLabs lists Nonapeptide-1 suspension at **$3,120/100 g, $23,400/kg, and $354,438.37/18 kg**, approximately **$19.69–31.20/g**. AbMole and GLPBio show research-grade 1–10 mg catalog prices from approximately **$60–295**, which are useful as a high ceiling but not a cosmetic manufacturing quote. Alibaba marketplace results include much broader and less reliable bands. [[35]](https://www.formulatelabs.ai/materials/nonapeptide-1) [[36]](https://www.abmole.com/products/nonapeptide-1-acetate-salt.html) [[37]](https://www.glpbio.com/nonapeptide-1-acetate-salt-melanostatine-5-acetate-salt.html) [[38]](https://www.alibaba.com/countrysearch/CN/melanostatin-5.html)

### Munapsys, Skinarch, and X50 commercial technologies

New Directions Australia gives unusually useful pack-size pricing for **Munapsys**: **AU$60.50/17 g, AU$275/100 g, AU$990/500 g, and AU$1,760/1 kg**. That is approximately **AU$1.76–3.56/g** for a commercial active solution whose INCI includes water, glycerin, caprylyl glycol, and Acetyl Hexapeptide-1. [[39]](https://www.newdirections.com.au/Raw-Materials-Cosmetic-Ingredients/Active-Ingredients/Munapsys-Active-Ingredients) [[40]](https://www.newdirections.com.au/epages/newdirections.sf/en_AU/?ObjectPath=%2FShops%2FNewDirections%2FProducts%2FRMAA1LMUNAPSYS)

Pochteca lists **Skinarch 1 kg at MXN 7,039.41**. Aston identifies the material as a Lipotrue technology containing a carrier and Palmitoyl Tetrapeptide-72 Amide but does not show a public price. [[41]](https://sip.pochteca.net/index.php/skinarchtm-1kg.html) [[42]](https://www.aston-chemicals.com/single-product?id=2060)

Technical Art of Science and the INFINITEC composition sheet show that X50 is a delivery system containing **Copper Heptapeptide-14 Pantothenate** and **Heptapeptide-15 Palmitate** at very low concentrations, not a bottle of pure peptide powder. A Ukrainian distributor displays pack prices of **UAH 38.45/1 g, UAH 289.80/10 g, and UAH 2,360.90/100 g**, which is approximately **UAH 38.45/g, UAH 28.98/g, and UAH 23.61/g**. At the access-date exchange rate this is roughly **$0.67–0.83/g** for the 10–100 g packs, but the page needs seller confirmation because its display is a commercial premix/active, not pure peptide. [[43]](https://www.technicalartofscience.com/product/x50-antiaging-powder/) [[44]](https://www.ewlerp.com/___country___/uploadedfile/rawmaterial/cb/X50%20Antiaging%20Solution_Composition%20Breakdown.pdf) [[45]](https://xn----utbcjbgv0e.com.ua/en/x50-antiaging-d-t-i-10-gr.html)

### Oligopeptide-68 and Acetyl Octapeptide-3 / SNAP-8

Oligopeptide-68 is unusually expensive in public listings. FormulateLabs lists a suspension at approximately **$64.63–102.40/g**. Alibaba listings range from roughly **$25–400/g**, including one quote around **€164–251/g** by quantity; a Chinese supplier displays still higher RMB/kg prices. These are not a coherent commodity market, so the suspension range is the more useful ready-to-formulate anchor. [[46]](https://www.formulatelabs.ai/materials/oligopeptide-68) [[47]](https://www.alibaba.com/product-detail/oligopeptide-68-Cosmetic-raw-materials-CAS_1601360959757.html) [[48]](https://www.yzjbio.com/products/show36323389.html)

Alibaba displays an Acetyl Octapeptide-3 listing around **£48.65–52.39/g**, but the unit presentation should be verified with the seller. A consumer/DIY supplier lists a **15 mL SNAP-8 active at €21.20**, which is a diluted product and cannot be treated as pure peptide. [[49]](https://www.alibaba.com/product-detail/Cosmetic-Grade-Acetyl-Octapeptide-3-CAS_1601700412589.html) [[50]](https://www.beautylabthestore.gr/en/cosmetics-active-ingredients)

### TEGO PEP 4-17 / Tetrapeptide-21

Escentials of Australia sells the actual TEGO PEP 4-17 cosmetic solution at **A$26/5 g, A$99/25 g, A$365/100 g, and A$1,560/500 g**. The page identifies Tetrapeptide-21 in butylene glycol/water, **2,300 ppm peptide content**, refrigeration, cool-down processing, and a **0.5–5%** use rate. At the working 0.70 USD/AUD conversion, the 500 g pack is approximately **$2.18/g** and is the selected public creator-cost anchor. [[51]](https://www.escentialsofaustralia.com/products/productid1564)

Evonik formulation material independently supports the commercial use context. Pure Tetrapeptide-21, Formulate Labs’ generic suspension, Qualitide, LookChem, and ChemicalBook records are useful identity or market-context evidence, but they are not price substitutes for the branded solution. ChemicalBook’s 2–10 mg vial listing is specifically excluded from the cost model. [[52]](https://personal-care.evonik.com/pim/fragment/personal-care/en/formulation/FORM_505263) [[53]](https://glenncorp.com/productapplications/cosmetics/) [[54]](https://www.formulatelabs.ai/materials/tetrapeptide-21)

### SYN-TACKS

The Herbarie provides a pack-size ladder for the commercial SYN-TACKS solution: **$10 for 1/3 oz, $54.95 for 1 oz, $218.64 for 4 oz, and $655 for 1 lb**. The largest pack is approximately **$1.44/g**; smaller packs are materially more expensive. DSM’s technical guideline confirms that SYN-TACKS is a commercial peptide technology, not a pure peptide powder. [[56]](https://www.theherbarie.com/Syn-Tacks.html) [[57]](https://www.dsm.com/content/dam/protected/personal-care/en_US/peptides/peptides_distributor/SYN-TACKS_Formulation%20Guidelines_2013-06.pdf)

### Caprooyl Tetrapeptide-3 and Tridecapeptide-1

Caprooyl Tetrapeptide-3 has unusually visible public pricing. CNCSBIO lists **$120/kg at 1–24 kg, $110/kg at 25–499 kg, and $100/kg at 500 kg or more**, with 98% specification and industrial-grade labeling. FormulateLabs lists a different material—a made-to-order aqueous suspension—at **$1,210.67/100 g, $9,080/kg, and $137,538.11/18 kg**, or roughly **$7.64–12.11/g**. EC21 shows a small-lot quote of **$200/g at 1 g**, decreasing to **$100/g at 100 g**. [[58]](https://www.cncsbio.com/anti-aging-raw-materials/63688129.html) [[59]](https://www.formulatelabs.ai/materials/caprooyl-tetrapeptide-3) [[60]](https://www.ec21.com/product-details/Top-Quality-Anti-Aging-Cosmetics--11965330.html)

Tridecapeptide-1 is less transparent. GSS offers a quote-only 99% material with 1 g, 10 g, and 1 kg MOQ options. Volza records a **10 g sample shipment at $26.32**, which is about **$2.63/g** if the shipment value and quantity are interpreted literally, but it is not a regular supplier price. [[61]](https://cosmetics-add.com/product/tridecapeptide-1/) [[62]](https://www.volza.com/p/cosmetic-peptide/import/hsn-code-2937190000/)

### Other named peptides where search evidence is sparse

- **Acetylarginyltryptophyl Diphenylglycine / Relistase:** a public price-list snippet shows a line at **14,000** but does not make the currency, pack size, or date sufficiently clear. The correct status is no reliable public unit price; the line is retained only as a search lead. [[63]](https://www.scribd.com/document/708282727/Scale-Price-List) [[64]](https://turkish.peptide-powder.com/doc/41054193/cas1334583-93-5-acetylarginyltryptophyl-diphenylglycine-powder-for-anti-age.pdf)
- **Hexapeptide-9 / Collaxyl:** Bellahut lists the water/glycerin cosmetic concentrate at **$29.95/10 mL through $139.95/120 mL**, with a published density of 1.10–1.15 g/mL and 0.5–5% use guidance. The selected 120 mL anchor is about **$1.04/g** using midpoint density. The ChemicalBook/Biosynth research catalog is excluded. [[65]](https://bellahut.com/mobile/itemslarge/39/19-106/Pure-Collaxyl-Peptide)
- **Tripeptide-2:** no clean public raw-material price was found; the name is often mixed with other peptide complexes or research products. Leave it unpriced unless a supplier quote identifies the exact CAS, grade, and pack.
- **Copper Lysinate Complex:** technical documents identify the complex and use levels, but no public matched price was found. Do not substitute GHK-Cu powder. [[66]](https://www.ewlerp.com/___country___/uploadedfile/rawmaterial/cat3/Tox%20file%20Neodermyl%20v2%20131107.pdf)
- **Bio-Placenta:** a retail raw-material page lists the five-growth-factor blend and a **793 Turkish lira** product price, but the pack size is not clear in the accessible page and the material is a complex. Treat it as a finished-active retail signal only, not a unit cost. [[67]](https://www.kozmetikhammaddeler.com/urun/bio-placenta-2-107)

### Proprietary blends with no responsible public price

The following technologies were identified in the 25 formulations, but a public raw-material price could not be found with enough unit clarity to attach a number:

| Ingredient/technology | Evidence found | Why it remains unpriced |
|---|---|---|
| Matrixyl Morphomics | Supplier identity and a marketplace “from $584.70/kg” placeholder; noisy import data | The marketplace value is not clearly a live supplier quote; import data has conflicting declared values |
| BIO GF Complex | Finished-product pages identify five recombinant growth-factor components and example use levels | No raw-material price or assay for the complex was published |
| Nutecyl / C-Pep Nutecyl | Corum trade identity and TDS; one trade-data signal around $137/kg for a related CC version | Standard Nutecyl and Nutecyl MB price was not public; related variant is not interchangeable |
| Neoclair Pro / Acetyl Tetrapeptide-2 | Aston and SpecialChem identity/INCI pages | Supplier pages require a quote or sample request |
| GF MiniProtein and Expression Line MiniProtein | Product pages and product marketing identify branded growth-factor technologies | No public distributor price; recombinant protein analogues would be misleading |
| Copper Tripeptide Complex, Acetyl Hexapeptide-8 Complex, Copper Lysinate Complex | Brand pages disclose complex percentages | Pure peptide fraction and complex supplier price are not published |
| Palmitoyl sh-Hexapeptide-13 Serine SP Amide | INCI/product identity | No public raw price found |
| sh-Polypeptide-69 and other uncommon signal peptides | INCI identity or supplier catalogue pages | No reliable price with an explicit unit basis found |

The correct output for these rows is “no public price,” not a borrowed price from GHK-Cu, Matrixyl, EGF, or another chemically different material.

### Recombinant growth factors and sh-/oligo-polypeptides

Growth-factor-style materials are especially easy to overstate. Public supplier pages often show a purity or recommended ppm use level but hide the price behind a quote request. A few public signals exist:

- **sh-Polypeptide-1 / FGF2:** Amerigo/Enantis identifies FGF2-STAB as a cosmetics-specific thermostable material used at **0.001% final formula**. The visible catalog price is **$721**, but the accessible page does not establish package mass; it is therefore a **quote/unit-basis gap**, not a $/g input. Research-protein catalogs remain excluded from normal cosmetic COGS. [[70]](https://www.amerigoscientific.com/fgf2-stab-thermostable-fgf2-for-cosmetics-item-531111.html) [[71]](https://kosmetika.martinabubakova.cz/assets/files/FGF2-STAB-Technical-documentation-2024.pdf)
- **sh-Oligopeptide-1 / EGF:** Alibaba shows a listing around **£29.89–74.72/g**, but the sample/quantity presentation is ambiguous. A separate supplier lists 1 kg MOQ with no price. [[73]](https://www.alibaba.com/product-detail/In-Stock-Anti-wrinkle-Peptide-Oligopeptide_1601676279217.html) [[74]](https://www.landnutra-ingredients.com/cosmetic-ingredients/sh-oligopeptide-1-powder.html)
- **sh-Oligopeptide-2 / IGF-1:** supplier pages identify a liposomal liquid and use levels around **1–10 ppm**, but no public price is shown. [[75]](https://biofdnc-global.com/page/?in_id=9&pid=product_detail) [[76]](https://www.immobazyme.com/cosmeticpeptides)
- **sh-Polypeptide-9 / VEGF and sh-Polypeptide-11 / acidic FGF:** supplier pages provide identity, purity, or product catalogues, but the material is quote-only. [[77]](https://www.faithful-chemical.com/peptide-raw-powder/sh-polypeptide-9.html) [[78]](https://cosmetics-add.com/product/sh-polypeptide-11/) [[79]](https://www.chamt.co.kr/file/pr/%28F%29%5BCHAMeditech%5D%20Cosmetics%20Raw%20Materials.pdf)
- **sh-Polypeptide-121 / HumaColl 21:** Geltor’s formulation sheet gives a 0.10% example use level but no public price. [[80]](https://geltor.com/wp-content/uploads/2023/09/FormulationSheets_09-2023.pdf)

These signals are useful for showing that recombinant materials may be orders of magnitude more expensive than commodity cosmetic peptides, but they are not enough to assign a line cost to a finished formula without a pack size, assay, and supplier quote.

### PDRN / Sodium DNA

The prior **$0.08–0.15/g bulk signal is excluded** because it did not adequately verify a topical cosmetic specification. Current cosmetic-marketplace examples cluster around roughly **$4.80–15/g** for small-lot PDRN/Sodium DNA powder; the model selects **$10/g** as a low-confidence category benchmark. A separate topical supplier record documents 99.8% assay, source/QC expectations, and **0.02–1%** formulation guidance but requires a quote. [[81]](https://www.alibaba.com/showroom/polydeoxyribonucleotide.html) [[82]](https://skincareactive.com/products/sodium-dna/) [[83]](https://www.tradeindia.com/products/polydeoxyribonucleotide-pdrn-sodium-dna-100403-24-5-9663403.html)

Do not apply a Sodium DNA price to an undisclosed “PDRN complex” unless the molecular source and grade are matched.

## Formulation crosswalk: what can actually be priced

This crosswalk maps the source-backed ingredient work to the 25 formulations in the companion model. It is intentionally conservative. A “forward line estimate possible” entry means a future calculation may multiply an **independently disclosed amount** by a **source-backed unit price**. It does not mean the brand paid that amount, and it does not mean all formula lines can be added into a complete bottle cost.

| Formulation | Ingredient or technology | Amount status in the companion model | Source-backed pricing route | Forward line estimate status |
|---|---|---|---|---|
| The Ordinary Argireline Solution 10% | Acetyl Hexapeptide-8 / Argireline solution | Product headline is a commercial-solution level; pure assay unknown | Commercial solution source, not pure powder | Possible only with a matched solution concentration |
| The Ordinary Matrixyl 10% + HA | Matrixyl 3000; Matrixyl Synthe’6 | Companion model uses assumed split | Trulux commercial blend prices | Do not use the assumed split as published amount; no source-first total |
| The Ordinary Multi-Peptide + HA | Seven named peptides | Individual amounts not disclosed | Ingredient-specific sources where available | Mostly not priced; no residual allocation |
| The Ordinary Multi-Peptide + Copper | GHK-Cu plus named peptides | 1% headline is a technology claim, not pure GHK-Cu assay | GHK-Cu powder sources plus individual peptide sources | Only the verified material/amount pair can be calculated |
| The Ordinary GF 15% Solution | Proprietary plant-made growth-factor technologies | 15% solution, pure protein unknown | No matched public GF complex price | Not priced |
| Good Molecules Super Peptide | Acetyl Hexapeptide-8, Acetyl Octapeptide-3, Copper Tripeptide-1 | Exact ppm and mg totals disclosed | Specific raw sources above | Forward line estimates possible for all three, but source grade matters |
| Good Molecules Copper Peptide with PDRN | GHK-Cu, Caprooyl Tetrapeptide-3, Tridecapeptide-1, Sodium DNA | Copper figure indexed, other amounts unknown | GHK-Cu and PDRN sources; no direct prices for every peptide | Partial only; unknown items stay unpriced |
| Geek & Gorgeous Power Peptides | Matrixyl 3000, Synthe’6, TEGO PEP, X50 | Official use levels disclosed | Trulux, TEGO supplier sources, X50 premix | Possible by line, but each commercial technology remains separate |
| Theramid Copper | GHK-Cu and 13% peptide complex | 3% and 13% claims disclosed; complex composition not fully quantified | GHK-Cu powder; no matched complex price | GHK-Cu line may be scenario-priced; 13% complex not priced |
| Theramid Derma-Peptides 35% | Nine named commercial technologies | All technology percentages disclosed | Trulux, Munapsys, Skinarch, X50, and specific technology sources | Partial; no residual allocation for unpriced technologies |
| Medik8 Liquid Peptides Advanced MP | 30% commercial complex, 13 peptides | Complex total disclosed; component doses not disclosed | Matched branded technology prices only | Not a complete line model |
| Paula’s Choice Pro-Collagen Booster | Six peptides | Identities/amounts not itemized | Pure peptide sources only where exact identity is known | Not priced as a total |
| Naturium Multi-Peptide Advanced | Acetyl Hexapeptide-8, Copper Palmitoyl Heptapeptide-14, Palmitoyl sh-Hexapeptide-13 | Amounts not disclosed | X50-related and exact-identity sources | Not priced |
| Minimalist Multi-Peptides 10% | Matrixyl 3000 and Bio-Placenta/growth-factor complex | 7%/3% blend claims | Matrixyl public blend price; Bio GF no public price | Matrixyl scenario only |
| The INKEY List Collagen Peptide | Matrixyl 3000 and SYN-TACKS | 1%/1% technology levels | Trulux and Herbarie | Forward line estimates possible, kept as separate commercial blends |
| Timeless Matrixyl 3000 | Matrixyl 3000 | 8% disclosed | Trulux blend price | Possible as independent blend line |
| Timeless Matrixyl Synthe’6 | Matrixyl Synthe’6 | 2% disclosed | Trulux blend price | Possible as independent blend line |
| COSRX Blue Peptide Bakuchiol | Copper Tripeptide-1 plus five named peptides | Amounts not disclosed | GHK-Cu and exact-identity sources | Not priced as a total |
| COSRX 6 Peptide Skin Booster | Six named peptides | Amounts not disclosed | GHK-Cu, SYN-AKE, Oligopeptide-68, PT-8, Argireline, growth-factor sources | Not priced as a total |
| DERMA E Advanced Peptides | Acetyl Hexapeptide-8, Palmitoyl Tripeptide-38 | Amounts not disclosed | Argireline and PT-38 sources | No line estimate without independent amounts |
| Drunk Elephant Protini | Nine signal peptides and growth factors | Amounts not disclosed | Exact ingredient sources only; many quote-only | Not priced |
| Peach & Lily Copper Peptide Pro | Copper peptide 0.2% headline | Concentration disclosed; complex identity needs confirmation | GHK-Cu powder only as a conditional proxy | Possible conditional line estimate |
| NIOD CAIS3 | GHK-Cu 1% and GHK 1%; other peptides unquantified | Two headline concentrations disclosed | GHK-Cu source; no matched pure GHK source | Partial only |
| Allies Copper Tripeptide & Ectoin | Three named peptide complexes | 1%/2%/2% complex levels disclosed | No public matched complex prices | Not priced as pure peptides |
| Q+A Multi-Peptide | Several named peptides | Amounts not disclosed | Exact-identity sources where available | Not priced as a total |

## What this changes in the companion visual

The original cost model should no longer display a reverse-calculated **applied unit cost** as if it were a supplier quote. The corrected source-first display should use these labels:

- **Source-backed unit price:** the public price range actually found for that ingredient or named commercial technology.
- **Formula amount:** the amount disclosed by the product or clearly labeled as a model assumption.
- **Forward line estimate:** only `source-backed unit price × formula amount`; blank or “not priced” when either input is missing.
- **Evidence:** the exact source link(s), with source type and confidence.
- **Unreconciled:** line estimates are not allocated to make a bottle total and are not required to sum to any product-level number.

The visual should not show “applied unit cost,” “residual allocation,” or “sum of line estimates = modeled bottle cost.” The old bottle-level scenario values can remain available as a clearly labeled legacy model, but they must not be presented as source prices.

## Assumptions and unresolved questions

1. **Brand procurement is private.** Public list prices are replacement-cost proxies, not invoices.
2. **Pack size changes the price.** The same named material can differ by 10× or more between a 1 g sample, a 50 g pack, a 1 kg pack, and a negotiated contract.
3. **Carrier content matters.** A commercial blend priced per gram may contain only a small assay of the named peptide.
4. **Purity and salt form matter.** Copper complexes, acetate salts, lyophilized powders, aqueous solutions, and liposomal products are not interchangeable.
5. **Marketplace units require verification.** Some listings show a price per item, per gram, per vial, or per pack without making the basis obvious in the search result.
6. **Currency conversions are rounded.** They are for order-of-magnitude comparison, not a historical invoice reconstruction.
7. **Formula amounts are often the real bottleneck.** A precise raw price cannot produce a precise line cost when the label gives only an ingredient name or a blend percentage.
8. **Trade data can be noisy.** Declared shipment values may include freight, multiple units, customs classification errors, or non-comparable grades.
9. **No analog substitution.** When Neoclair Pro, BIO GF Complex, Nutecyl, Matrixyl Morphomics, or a growth-factor complex has no public price, the model leaves it unpriced.
10. **Clinical value is out of scope.** A higher raw-material price does not establish better efficacy, and a lower price does not establish poor efficacy.

## Source index

The numbered links in the records above are the source trail used for the price map. Sources include supplier listings, official technical documents, distributor pages, marketplaces, and research-grade catalogues. Their role is labeled in the text so a reader can distinguish a price quote from an identity or composition source.

For the original retail formulation claims and ingredient concentrations, use the product/source keys in the companion [rendered cost-model page](index.html#doc7) and the topic’s preserved source documents. This separate document intentionally focuses on the additional ingredient-price search rather than repeating every retail-product citation.
