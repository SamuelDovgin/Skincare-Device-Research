#!/usr/bin/env node

import fs from "node:fs/promises";
import { Workbook } from "/Users/samueldovgin/.cache/codex-runtimes/codex-primary-runtime/dependencies/node/node_modules/@oai/artifact-tool/dist/artifact_tool.mjs";

const sourcePath = new URL("../12_peptides_in_skincare/data/peptide_price_source_records.csv", import.meta.url);
const csvText = await fs.readFile(sourcePath, "utf8");
const workbook = await Workbook.fromCSV(csvText, { sheetName: "Price Sources" });
const sheet = workbook.worksheets.getItem("Price Sources");
const values = sheet.getUsedRange().values;
const headers = values[0].map(String);
const rows = values.slice(1).map((row) => Object.fromEntries(headers.map((header, index) => [header, row[index] ?? ""])));

const enrichmentHeaders = ["best_anchor_usd_per_g", "procurement_fit", "model_role", "eligibility_reason"];
const outputHeaders = [...headers.filter((header) => !enrichmentHeaders.includes(header)), ...enrichmentHeaders];

const superseded = new Map([
  ["PROGELINE", ["pure/research material; not the branded cosmetic solution", "excluded", "Superseded by the New Directions Progeline commercial solution. Do not apply this powder/research range to a formula naming Progeline."]],
  ["PDRN", ["unverified marketplace bulk signal", "excluded", "The listing does not adequately verify the cosmetic Sodium DNA specification, source, molecular-weight distribution, or QC package used in the finished product."]],
  ["FGF2", ["research/small-lot recombinant protein", "excluded", "A milligram-scale recombinant-protein price is not a routine cosmetic-formulation input price; retained only as historical evidence."]],
  ["MATRIXYL-PURE", ["cosmetic pure-peptide powder", "evidence-only", "Chemistry is relevant, but the material form must not be applied to a product that names a commercial Matrixyl premix."]],
  ["HEX9", ["research-grade catalog material", "excluded", "Superseded by the Bellahut Collaxyl cosmetic concentrate; the research catalog is not used in product-cost estimates."]],
]);

function prices(value) {
  return String(value || "").split("|").map(Number).filter(Number.isFinite);
}

function classify(row) {
  if (superseded.has(row.record_id)) return superseded.get(row.record_id);
  if (String(row.record_id).startsWith("NO-PRICE-")) {
    return ["matched cosmetic technology; public quote unavailable", "quote-gap", "The material identity is formulation-relevant, but no auditable public pack price was found. A supplier quote is required."];
  }
  if (String(row.record_id).startsWith("FL-")) {
    return ["cosmetic-grade formulated suspension", "replacement-benchmark", "Doseable cosmetic material with a public pack ladder. Eligible as a matched pure-INCI replacement benchmark, not as evidence of the brand's actual supplier or invoice."];
  }
  if (/^(TRULUX|NEW-DIR|HERBARIE|MUNAPSYS|SKINARCH|X50)/.test(String(row.record_id))) {
    return ["cosmetic commercial premix or solution", "preferred", "The public material is sold for cosmetic formulation in the same commercial-input class named by the product."];
  }
  return ["material form requires case review", "evidence-only", "Retained for source comparison, but not automatically eligible for a finished-product cost estimate."];
}

for (const row of rows) {
  const [fit, role, reason] = classify(row);
  const anchors = prices(row.unit_anchor_usd_per_g);
  row.best_anchor_usd_per_g = anchors.length ? String(anchors[0]) : "";
  row.procurement_fit = fit;
  row.model_role = role;
  row.eligibility_reason = reason;
}

const newRows = [
  {
    record_id: "ESCENTIALS-TEGO", ingredient_key: "tetrapeptide_21", ingredient_name: "TEGO PEP 4-17 / Tetrapeptide-21",
    material_form: "commercial cosmetic solution; 2,300 ppm Tetrapeptide-21 in butylene glycol/water", source_name: "Escentials of Australia",
    source_url: "https://www.escentialsofaustralia.com/products/productid1564", access_date: "2026-08-14",
    pack_examples: "A$26/5 g; A$99/25 g; A$365/100 g; A$1,560/500 g; normalized at 0.70 USD/AUD",
    unit_anchor_usd_per_g: "2.18|2.56|3.64", price_status: "direct public cosmetic pack ladder", formulation_use_rate: "0.5-5%; refrigerated; cool-down below 40 C",
    confidence: "high", notes: "Exact cosmetic material class for formulas naming TEGO PEP 4-17. Public 500 g price is the selected manufacturer-oriented anchor; direct Evonik contract pricing may be lower.",
    best_anchor_usd_per_g: "2.18", procurement_fit: "matched branded cosmetic solution", model_role: "preferred",
    eligibility_reason: "Same named commercial technology, cosmetic carrier system, peptide assay, formulation guidance, and public multi-pack price ladder."
  },
  {
    record_id: "NEW-DIR-PROGELINE", ingredient_key: "trifluoroacetyl_tripeptide_2", ingredient_name: "Progeline / Trifluoroacetyl Tripeptide-2",
    material_form: "commercial cosmetic solution; glycerin/water/Tripeptide-2", source_name: "New Directions Australia",
    source_url: "https://www.newdirections.com.au/RMAA1KPROGELIN", access_date: "2026-08-14",
    pack_examples: "A$66/17 g; A$275/100 g; A$770/500 g; A$1,430/1 kg; normalized at 0.70 USD/AUD",
    unit_anchor_usd_per_g: "1.00|1.08|2.72", price_status: "direct public cosmetic pack ladder", formulation_use_rate: "0.2-2%; add below 40 C; final pH 4-6",
    confidence: "high", notes: "Correct commercial solution class for a formula naming Progeline; the 1 kg public pack is the selected anchor.",
    best_anchor_usd_per_g: "1.00", procurement_fit: "matched branded cosmetic solution", model_role: "preferred",
    eligibility_reason: "Same named commercial cosmetic technology with public pack prices and supplier dosing guidance."
  },
  {
    record_id: "BELLAHUT-COLLAXYL", ingredient_key: "hexapeptide_9", ingredient_name: "Collaxyl / Hexapeptide-9",
    material_form: "water/glycerin cosmetic concentrate; density 1.10-1.15 g/mL", source_name: "Bellahut",
    source_url: "https://bellahut.com/mobile/itemslarge/39/19-106/Pure-Collaxyl-Peptide", access_date: "2026-08-14",
    pack_examples: "$29.95/10 mL; $49.95/20 mL; $59.95/30 mL; $89.95/60 mL; $139.95/120 mL; normalized using midpoint density 1.125 g/mL",
    unit_anchor_usd_per_g: "1.04|1.33|2.66", price_status: "direct public cosmetic concentrate ladder", formulation_use_rate: "0.5-5%; cool-down below 40 C; refrigerated storage",
    confidence: "medium", notes: "Correct ready-to-formulate material class; exact peptide assay is not published, so this is a concentrate price rather than a pure-Hexapeptide-9 price.",
    best_anchor_usd_per_g: "1.04", procurement_fit: "cosmetic commercial concentrate", model_role: "preferred",
    eligibility_reason: "Sold specifically as a cosmetic-formulation additive with use rate, INCI, physical properties, and public multi-size prices."
  },
  {
    record_id: "SKINCAREACTIVE-PDRN", ingredient_key: "sodium_dna_pdrn", ingredient_name: "Sodium DNA / PDRN",
    material_form: "99.8% cosmetic-grade Sodium DNA powder", source_name: "SkincareActive",
    source_url: "https://skincareactive.com/products/sodium-dna/", access_date: "2026-08-14",
    pack_examples: "COA/TDS/sample and commercial quote available; no public pack price", unit_anchor_usd_per_g: "", price_status: "cosmetic supplier quote required",
    formulation_use_rate: "0.02-1%; 0.2-0.3% water-based formula reference", confidence: "medium",
    notes: "Strong formulation/specification match but no public price. Useful for dose selection and RFQ requirements, not a zero-cost line.",
    best_anchor_usd_per_g: "", procurement_fit: "matched cosmetic powder; public quote unavailable", model_role: "quote-gap",
    eligibility_reason: "Material specification and use rate match topical formulation, but price remains private."
  },
  {
    record_id: "ALIBABA-PDRN-COS", ingredient_key: "sodium_dna_pdrn", ingredient_name: "Sodium DNA / PDRN",
    material_form: "cosmetic-grade PDRN/Sodium DNA powder marketplace listings", source_name: "Alibaba cosmetic raw-material listings",
    source_url: "https://www.alibaba.com/showroom/polydeoxyribonucleotide.html", access_date: "2026-08-14",
    pack_examples: "Visible cosmetic-grade examples about $4.80-10/g at 1 g MOQ and $10-15/g for higher-assay small lots",
    unit_anchor_usd_per_g: "4.80|10.00|15.00", price_status: "public cosmetic marketplace range", formulation_use_rate: "supplier-dependent; cross-check against 0.02-1% cosmetic use guidance",
    confidence: "low", notes: "Selected $10/g category anchor is a public cosmetic-powder replacement estimate, not a verified brand quote. Require COA, source, molecular-weight, endotoxin, and protein-content confirmation.",
    best_anchor_usd_per_g: "10.00", procurement_fit: "cosmetic powder; marketplace specification not fully verified", model_role: "replacement-benchmark",
    eligibility_reason: "Correct topical material class and explicit cosmetic positioning, but seller-level specification and lot quality require verification."
  },
  {
    record_id: "AMERIGO-FGF2STAB", ingredient_key: "sh_polypeptide_1", ingredient_name: "FGF2-STAB / sh-Polypeptide-1",
    material_form: "thermostable cosmetic FGF2 powder", source_name: "Amerigo Scientific / Enantis",
    source_url: "https://www.amerigoscientific.com/fgf2-stab-thermostable-fgf2-for-cosmetics-item-531111.html", access_date: "2026-08-14",
    pack_examples: "$721 catalog display, but accessible page does not establish the package mass", unit_anchor_usd_per_g: "", price_status: "cosmetic catalog price lacks unit basis",
    formulation_use_rate: "0.001% final product (10 micrograms/mL)", confidence: "medium",
    notes: "Correct cosmetics-specific material and use rate, but no $/g is calculated until the $721 package size is verified.",
    best_anchor_usd_per_g: "", procurement_fit: "matched cosmetics-specific growth factor; unit price incomplete", model_role: "quote-gap",
    eligibility_reason: "Formulation fit is strong; the visible price is not model-eligible because the package mass is missing."
  }
];

const newRecordIds = new Set(newRows.map((row) => row.record_id));
for (let index = rows.length - 1; index >= 0; index--) {
  if (newRecordIds.has(rows[index].record_id)) rows.splice(index, 1);
}
for (const row of newRows) rows.push(row);

function csvCell(value) {
  const text = String(value ?? "");
  return /[",\r\n]/.test(text) ? `"${text.replaceAll('"', '""')}"` : text;
}

const output = [outputHeaders, ...rows.map((row) => outputHeaders.map((header) => row[header] ?? ""))]
  .map((row) => row.map(csvCell).join(","))
  .join("\n") + "\n";

await fs.writeFile(sourcePath, output, "utf8");
const jsPath = new URL("../12_peptides_in_skincare/data/peptide_price_source_records.js", import.meta.url);
await fs.writeFile(jsPath, `window.PEPTIDE_PRICE_SOURCE_RECORDS = ${JSON.stringify(rows)};\n`, "utf8");

const inspection = await workbook.inspect({ kind: "sheet", include: "id,name", maxChars: 1000 });
console.log(`Updated ${rows.length} source records and browser fallback. Artifact-tool import check: ${inspection.ndjson ? "ok" : "completed"}.`);
