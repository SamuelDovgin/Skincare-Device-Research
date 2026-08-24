#!/usr/bin/env python3
"""Build the peptide formula ingredient inventory and product-level value summary.

The model never infers concentration from retail price. It uses, in order:
published final-formula dose; published commercial-technology dose plus supplier
assay; otherwise an INCI-position/material-class prior.
"""

from __future__ import annotations

import csv
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
TOPIC = ROOT / "12_peptides_in_skincare"
OUT_LINES = TOPIC / "data/peptide_formula_ingredient_audit.csv"
OUT_PRODUCTS = TOPIC / "data/peptide_formula_value_summary.csv"
OUT_LINES_JS = TOPIC / "data/peptide_formula_ingredient_audit.js"
OUT_PRODUCTS_JS = TOPIC / "data/peptide_formula_value_summary.js"
OUT_SCENARIOS_JS = TOPIC / "data/peptide_price_scenario_model.js"
OUT_COST_JS = TOPIC / "data/peptide_cost_model.js"

PRODUCTS = {}
with (TOPIC / "data/peptide_cost_model.csv").open() as handle:
    for row in csv.DictReader(handle):
        PRODUCTS[row["id"]] = row

with (TOPIC / "data/peptide_price_scenario_model.csv").open() as handle:
    PRICE_SCENARIOS = list(csv.DictReader(handle))

# Percent final formula, not fractions. The three bands are sensitivity scenarios.
PRIORS = {
    "copper": {
        "early": (0.005, 0.02, 0.10), "middle": (0.001, 0.01, 0.05), "late": (0.0001, 0.001, 0.01)},
    "expression": {
        "early": (0.001, 0.005, 0.02), "middle": (0.0002, 0.001, 0.01), "late": (0.00002, 0.0002, 0.002)},
    "lipopeptide": {
        "early": (0.0001, 0.001, 0.01), "middle": (0.00003, 0.0003, 0.003), "late": (0.00001, 0.0001, 0.001)},
    "growth_factor": {
        "early": (0.00001, 0.00010, 0.001), "middle": (0.000001, 0.00001, 0.0001), "late": (0.0000001, 0.000001, 0.00001)},
    "polypeptide": {
        "early": (0.0001, 0.001, 0.01), "middle": (0.00001, 0.0001, 0.001), "late": (0.000001, 0.00001, 0.0001)},
    "other": {
        "early": (0.0005, 0.005, 0.05), "middle": (0.00005, 0.0005, 0.005), "late": (0.000005, 0.00005, 0.0005)},
}

def zone(position: int) -> str:
    if position <= 10:
        return "early"
    if position <= 20:
        return "middle"
    return "late"

def item(name, material_class, position, exact=None, basis=None, technology=None,
         estimate_class=None, basis_url=None, include=True):
    return {"name": name, "class": material_class, "position": position,
            "exact": exact, "basis": basis, "technology": technology or "",
            "estimate_class": estimate_class, "basis_url": basis_url or "",
            "include": include}

M3000_PT1 = lambda pct: pct * 0.00010   # premix contains ~0.01% PT-1
M3000_PT7 = lambda pct: pct * 0.00005   # premix contains ~0.005% PT-7
S6_PT38 = lambda pct: pct * 0.00025     # premix contains ~0.025% PT-38

URL = {
    "to_argireline": "https://theordinary.com/en-us/argireline-solution-10-serum-100403.html",
    "to_matrixyl": "https://theordinary.com/en-us/matrixyl-10-ha-serum-100431.html",
    "to_multi_ha": "https://theordinary.com/en-us/multi-peptide-ha-serum-100613.html",
    "to_copper": "https://theordinary.com/en-us/multi-peptide-copper-peptides-1-serum-100625.html",
    "to_gf15": "https://theordinary.com/en-us/gf-15-solution-growth-factors-serum-100702.html",
    "gm_super": "https://v1.goodmolecules.com/products/super-peptide-serum",
    "gm_copper_pdrn": "https://www.goodmolecules.com/s/good-molecules-copper-peptide-serum-with-pdrn-30ml",
    "gng_power": "https://geekandgorgeous.com/products/power-peptides",
    "theramid_copper": "https://nichebeautylab.com/collections/bestseller-north-america/products/copper-peptide",
    "theramid_derma": "https://nichebeautylab.com/collections/serums/products/derma-peptides",
    "medik8_advanced": "https://us.medik8.com/products/liquid-peptides-advanced-mp",
    "paulas_choice": "https://www.paulaschoice.co.uk/pro-collagen-multi-peptide-booster/m3020.html",
    "naturium": "https://naturium.com/products/multi-peptide-advanced-serum",
    "minimalist": "https://www.ulta.com/p/multi-peptides-10-anti-aging-face-serum-reduces-fine-lines-wrinkles-mkt77005961",
    "inkey": "https://uk.theinkeylist.com/collections/myinkey-loyalty-points/products/collagen-peptide-serum",
    "timeless_m3000": "https://www.timelessha.com/products/matrixyl-3000-serum-1-oz",
    "timeless_s6": "https://www.timelessha.com/products/matrixyl-synthe6-serum-1-oz",
    "cosrx_blue": "https://www.cosrx.com/collections/new/products/cosrx-the-blue-peptide-bakuchiol-plump-glow-serum",
    "cosrx_six": "https://www.cosrx.com/products/the-6-peptide-skin-booster-serum",
    "dermae": "https://dermae.com/products/advanced-peptides-and-flora-collagen-serum",
    "drunk_elephant": "https://www.drunkelephant.com/protini-polypeptide-cream-50-ml-856556004739.html",
    "peach_lily": "https://www.peachandlily.com/products/copper-peptide-pro-firming-serum",
    "niod_cais3": "https://niod.com/en-cv/copper-amino-isolate-serum-3-11-cais3-serum-100368.html",
    "allies_copper": "https://us.allies.shop/products/copper-tripeptide-ectoin-advanced-repair-serum",
    "qa_multi": "https://us.qandaskin.com/products/multi-peptide-facial-serum",
}

TECH_URL = {
    "argireline_assay": "https://doctorsheltonsolution.com/special/compliance/studies/arg-4.pdf",
    "matrixyl_3000_assay": "https://patents.google.com/patent/US6974799B2/lv",
    "matrixyl_s6_assay": "https://patentimages.storage.googleapis.com/9c/04/e9/84ccee710561e0/EP2732806A1.pdf",
    "tego_assay": "https://www.escentialsofaustralia.com/products/productid1564",
    "inci_rule": "https://www.fda.gov/cosmetics/cosmetics-labeling-regulations/summary-cosmetics-labeling-requirements",
}

# Purchased peptide technology as percent of the finished formula. These bands
# estimate the premix/solution/complex added by the formulator, including its
# carrier. They must not be read as pure-peptide percentages.
TECH = {
    "to_argireline": ((10, 10, 10), "published 10% ARGIRELINE-solution headline"),
    "to_matrixyl": ((10, 10, 10), "published 10% total peptide-technology headline; 6/4 split modeled"),
    "to_multi_ha": ((5, 14, 25.1), "current loading undisclosed; base uses typical supplier rates; 25.1% is a historical technology claim used only as the high case"),
    "to_copper": ((6, 15, 26.1), "1% copper-peptide headline plus the Multi-Peptide technology scenario"),
    "to_gf15": ((15, 15, 15), "published 15% total growth-factor solution"),
    "gm_super": ((0.0055, 0.0055, 0.0055), "published 25/25/5 ppm pure-active total; no separate commercial-input rate disclosed"),
    "gm_copper_pdrn": ((0.12, 0.31, 0.75), "independent 0.1% copper and 0.2% PDRN index plus modeled minor peptide inputs"),
    "gng_power": ((9.001, 9.001, 9.001), "published 3% + 2% + 4% + 0.001% commercial technologies"),
    "theramid_copper": ((16, 16, 16), "published 3% copper peptide plus 13% additional peptide complex"),
    "theramid_derma": ((35, 35, 35), "published nine-technology total"),
    "medik8_advanced": ((30, 30, 30), "published 30% multi-peptide complex"),
    "paulas_choice": ((1, 4, 8), "six named peptide materials; total technology loading undisclosed"),
    "naturium": ((0.1, 0.5, 1), "three late-list peptide materials; total loading undisclosed"),
    "minimalist": ((10, 10, 10), "published 7% Matrixyl 3000 plus 3% Bio-Placenta complex"),
    "inkey": ((2, 2, 2), "published 1% Matrixyl 3000 plus 1% SYN-TACKS"),
    "timeless_m3000": ((8, 8, 8), "published 8% Matrixyl 3000"),
    "timeless_s6": ((2, 2, 2), "published 2% Matrixyl Synthe'6"),
    "cosrx_blue": ((0.10, 0.60, 2.0), "six undisclosed peptides; manufacturer-use-rate and INCI-position scenario"),
    "cosrx_six": ((0.15, 1.0, 4.0), "six undisclosed peptides; manufacturer-use-rate scenario constrained below the preceding niacinamide line"),
    "dermae": ((0.05, 0.5, 2.0), "two undisclosed peptide inputs; manufacturer-use-rate scenario"),
    "drunk_elephant": ((0.10, 0.80, 3.0), "nine undisclosed peptide/protein inputs; low-dose growth-factor scenario"),
    "peach_lily": ((0.22, 0.50, 1.5), "published 0.2% copper-peptide headline plus twelve undisclosed peptide inputs"),
    "niod_cais3": ((2.0, 2.05, 2.5), "published 1% GHK-Cu + 1% GHK plus four undisclosed peptide inputs"),
    "allies_copper": ((3, 3, 3), "published 1% opaque copper-tripeptide complex + 2% AHP-8 complex; current INCI does not confirm GHK-Cu"),
    "qa_multi": ((1.2, 3.2, 5.5), "modeled 1/3/5% Matrixyl-like input plus minor peptide solutions"),
}

AUDIT = {
    "to_multi_ha": "Seven current peptide INCI lines retained; historical 25.1% technology claim is not treated as current dose.",
    "to_copper": "Eight current peptide INCI lines retained; 1% headline is kept separate from pure-active equivalence.",
    "to_gf15": "Replaced generic growth-factor label with the three current Nicotiana-derived INCI names.",
    "gm_copper_pdrn": "Added Caprooyl Tetrapeptide-3 and Tridecapeptide-1; Sodium DNA is adjacent PDRN and excluded from peptide-mass totals.",
    "gng_power": "Expanded X50 into both Copper Palmitoyl Heptapeptide-14 and Heptapeptide-15 Palmitate.",
    "theramid_copper": "Expanded the current North American formula to 18 peptide-like lines; formula differs by region.",
    "theramid_derma": "Expanded the nine commercial technologies into 13 current INCI peptide/protein lines.",
    "medik8_advanced": "Expanded the 30% complex into 13 current peptide/protein INCI lines.",
    "paulas_choice": "Expanded the generic six-peptide label into all six current INCI identities.",
    "minimalist": "Expanded Bio-Placenta into five growth-factor INCI lines plus the two Matrixyl 3000 peptides.",
    "inkey": "Added both SYN-TACKS component INCI lines; four peptide lines total.",
    "cosrx_blue": "Expanded the six-peptide claim into the six current INCI identities.",
    "cosrx_six": "Expanded the six-peptide claim into the six current INCI identities.",
    "drunk_elephant": "Expanded the blend into nine peptide/protein INCI lines.",
    "peach_lily": "Added the twelve peptides omitted by the prior copper-only row; 13 current peptide lines total.",
    "niod_cais3": "Added Tripeptide-29 and preserved Trifluoroacetyl Tripeptide-2 instead of collapsing it to Tripeptide-2.",
    "allies_copper": "Current INCI does not visibly contain Copper Tripeptide-1; the 1% headline remains an opaque complex, not assumed GHK-Cu.",
}

DISPLAY_NAME = {
    "cosrx_blue": "Blue Peptide Bakuchiol Plump Glow Serum",
    "naturium": "Multi-Peptide Advanced Serum",
    "qa_multi": "Multi-Peptide Facial Serum",
}

F = {}
F["to_argireline"] = [item("Acetyl Hexapeptide-8", "expression", 3, (0.005,)*3,
    "10% ARGIRELINE solution × published ~0.05% peptide assay", "ARGIRELINE peptide solution",
    "published_technology_supplier_assay", TECH_URL["argireline_assay"])]
F["to_matrixyl"] = [
    item("Palmitoyl Tripeptide-1", "lipopeptide", 4, (M3000_PT1(3), M3000_PT1(6), M3000_PT1(8)), "modeled 3/6/8% Matrixyl 3000 × supplier assay", "Matrixyl 3000", "modeled_technology_supplier_assay", TECH_URL["matrixyl_3000_assay"]),
    item("Palmitoyl Tetrapeptide-7", "lipopeptide", 5, (M3000_PT7(3), M3000_PT7(6), M3000_PT7(8)), "modeled 3/6/8% Matrixyl 3000 × supplier assay", "Matrixyl 3000", "modeled_technology_supplier_assay", TECH_URL["matrixyl_3000_assay"]),
    item("Palmitoyl Tripeptide-38", "lipopeptide", 6, (S6_PT38(2), S6_PT38(4), S6_PT38(5)), "modeled 2/4/5% Synthe'6 × supplier assay", "Matrixyl Synthe'6", "modeled_technology_supplier_assay", TECH_URL["matrixyl_s6_assay"]),]

TO_MULTI = [
    item("Acetyl Hexapeptide-8", "expression", 4, (0.001,0.0025,0.005), "modeled 2/5/10% ARGIRELOX-type input × ~0.05% AHP-8 assay", "ARGIRELOX", "modeled_technology_supplier_assay", TECH_URL["argireline_assay"]),
    item("Pentapeptide-18", "expression", 5),
    item("Palmitoyl Tripeptide-1", "lipopeptide", 6, (M3000_PT1(1),M3000_PT1(3),M3000_PT1(8)), "supplier 1/3/8% Matrixyl 3000 scenario", "Matrixyl 3000", "modeled_technology_supplier_assay", TECH_URL["matrixyl_3000_assay"]),
    item("Palmitoyl Tetrapeptide-7", "lipopeptide", 7, (M3000_PT7(1),M3000_PT7(3),M3000_PT7(8)), "supplier 1/3/8% Matrixyl 3000 scenario", "Matrixyl 3000", "modeled_technology_supplier_assay", TECH_URL["matrixyl_3000_assay"]),
    item("Palmitoyl Tripeptide-38", "lipopeptide", 8, (S6_PT38(.5),S6_PT38(2),S6_PT38(4)), "supplier 0.5/2/4% Synthe'6 scenario", "Matrixyl Synthe'6", "modeled_technology_supplier_assay", TECH_URL["matrixyl_s6_assay"]),
    item("Dipeptide Diaminobutyroyl Benzylamide Diacetate", "expression", 9, (0.002,0.005,0.012), "1/2/4% SYN-AKE × 0.2-0.3% peptide assay", "SYN-AKE", "modeled_technology_supplier_assay"),
    item("Acetylarginyltryptophyl Diphenylglycine", "other", 10),]
F["to_multi_ha"] = TO_MULTI
F["to_copper"] = [item("Copper Tripeptide-1", "copper", 4, (1,1,1), "official 1% copper-peptide headline; treated conditionally as Copper Tripeptide-1", "GHK-Cu", "published_claim_conditional")] + [dict(x, position=x["position"]+1) for x in TO_MULTI]
F["to_gf15"] = [
    item("Nicotiana Benthamiana Hexapeptide-40 sh-Oligopeptide-1", "growth_factor", 3, (0.00001,0.0001,0.001), "15% total GF solution; individual assay undisclosed", "15% GF solution", "modeled_with_published_complex"),
    item("Nicotiana Benthamiana Hexapeptide-40 sh-Polypeptide-76", "growth_factor", 4, (0.00001,0.0001,0.001), "15% total GF solution; individual assay undisclosed", "15% GF solution", "modeled_with_published_complex"),
    item("Nicotiana Benthamiana Octapeptide-30 sh-Oligopeptide-2", "growth_factor", 5, (0.00001,0.0001,0.001), "15% total GF solution; individual assay undisclosed", "15% GF solution", "modeled_with_published_complex"),]
F["gm_super"] = [item("Acetyl Hexapeptide-8","expression",12,(0.0025,)*3,"official 25 ppm",estimate_class="published_final_dose"), item("Acetyl Octapeptide-3","expression",13,(0.0025,)*3,"official 25 ppm",estimate_class="published_final_dose"), item("Copper Tripeptide-1","copper",15,(0.0005,)*3,"official 5 ppm",estimate_class="published_final_dose")]
F["gm_copper_pdrn"] = [item("Copper Tripeptide-1","copper",14,(0.1,)*3,"independent formula index; not brand-published",estimate_class="independent_secondary"), item("Sodium DNA (PDRN; not a peptide)","other",16,(0.02,0.2,0.6),"PDRN amount undisclosed; modeled",estimate_class="modeled_inci_class_prior",include=False), item("Caprooyl Tetrapeptide-3","lipopeptide",17), item("Tridecapeptide-1","other",19)]
F["gng_power"] = [
    item("Palmitoyl Tripeptide-1","lipopeptide",6,(M3000_PT1(3),)*3,"official 3% Matrixyl 3000 × supplier assay","Matrixyl 3000","published_technology_supplier_assay",TECH_URL["matrixyl_3000_assay"]), item("Palmitoyl Tetrapeptide-7","lipopeptide",7,(M3000_PT7(3),)*3,"official 3% Matrixyl 3000 × supplier assay","Matrixyl 3000","published_technology_supplier_assay",TECH_URL["matrixyl_3000_assay"]),
    item("Palmitoyl Tripeptide-38","lipopeptide",8,(S6_PT38(2),)*3,"official 2% Synthe'6 × supplier assay","Matrixyl Synthe'6","published_technology_supplier_assay",TECH_URL["matrixyl_s6_assay"]), item("Tetrapeptide-21","other",9,(0.0092,)*3,"official 4% TEGO PEP × public 2,300 ppm peptide assay","TEGO PEP 4-17","published_technology_supplier_assay",TECH_URL["tego_assay"]),
    item("Copper Palmitoyl Heptapeptide-14","copper",20,(0.0000001,0.000001,0.00001),"official 0.001% X50; component fraction undisclosed","X50 Antiaging","modeled_with_published_complex"), item("Heptapeptide-15 Palmitate","lipopeptide",21,(0.0000001,0.000001,0.00001),"official 0.001% X50; component fraction undisclosed","X50 Antiaging","modeled_with_published_complex")]

F["theramid_copper"] = [item("Copper Tripeptide-1","copper",8,(3,3,3),"official 3% claim"), *[
    item(n,c,p) for p,(n,c) in enumerate([
        ("Acetyl Hexapeptide-1","expression"),("Ascorbic Acid Polypeptide","polypeptide"),("Palmitoyl Tripeptide-1","lipopeptide"),("Palmitoyl Tetrapeptide-7","lipopeptide"),("Palmitoyl Hexapeptide-12","lipopeptide"),("Palmitoyl Tripeptide-5","lipopeptide"),("Palmitoyl Pentapeptide-4","lipopeptide"),("Tripeptide-2","other"),("Acetyl Dipeptide-1 Cetyl Ester","lipopeptide"),("Acetyl Hexapeptide-8","expression"),("Hexapeptide-9","other"),("Heptasodium Hexacarboxymethyl Dipeptide-12","other"),("Pentapeptide-3","other"),("Dipeptide Diaminobutyroyl Benzylamide Diacetate","expression"),("Nonapeptide-1","other"),("Tripeptide-1","other"),("Acetyl Tetrapeptide-2","other")],15)]]
F["theramid_derma"] = [
    item("Acetyl Hexapeptide-1","expression",12,(0.001,0.01,0.05),"published 5% Munapsys technology; peptide assay undisclosed","Munapsys","modeled_with_published_complex"),
    item("N-Prolyl Palmitoyl Tripeptide-56 Acetate","lipopeptide",13,(0.00003,0.0003,0.003),"published 3% Matrixyl Morphomics; peptide assay undisclosed","Matrixyl Morphomics","modeled_with_published_complex"),
    item("Acetyl Tetrapeptide-2","other",14,(0.00002,0.0002,0.002),"published 2% Neoclair Pro; peptide assay undisclosed","Neoclair Pro","modeled_with_published_complex"),
    item("Palmitoyl Tripeptide-38","lipopeptide",15,(S6_PT38(3),)*3,"published 3% Matrixyl Synthe'6 × supplier assay","Matrixyl Synthe'6","published_technology_supplier_assay",TECH_URL["matrixyl_s6_assay"]),
    item("Palmitoyl Tripeptide-1","lipopeptide",16,(M3000_PT1(5),)*3,"published 5% Matrixyl 3000 × supplier assay","Matrixyl 3000","published_technology_supplier_assay",TECH_URL["matrixyl_3000_assay"]),
    *[item(n,"growth_factor",p,(0.000001,0.00001,0.0001),"published 8% BIO GF Complex; individual protein assay undisclosed","BIO GF Complex","modeled_with_published_complex") for p,n in enumerate(["sh-Oligopeptide-1","sh-Oligopeptide-2","sh-Polypeptide-1","sh-Polypeptide-9","sh-Polypeptide-11"],17)],
    item("Palmitoyl Dipeptide-10","lipopeptide",22,(0.00001,0.0001,0.001),"published 2% Skinarch; peptide assay undisclosed","Skinarch","modeled_with_published_complex"),
    item("Palmitoyl Tetrapeptide-7","lipopeptide",23,(M3000_PT7(5),)*3,"published 5% Matrixyl 3000 × supplier assay","Matrixyl 3000","published_technology_supplier_assay",TECH_URL["matrixyl_3000_assay"]),
    item("Nonapeptide-1","other",24,(0.00004,0.0004,0.004),"published 4% Melanostatine technology; active assay undisclosed","Melanostatine","modeled_with_published_complex"),
]
F["medik8_advanced"] = [item(n,c,p) for p,(n,c) in enumerate([
    ("Palmitoyl Tripeptide-38","lipopeptide"),("Palmitoyl Tripeptide-5","lipopeptide"),("Palmitoyl Tripeptide-1","lipopeptide"),("Tetrapeptide-21","other"),("Palmitoyl Tetrapeptide-10","lipopeptide"),("Palmitoyl Tetrapeptide-7","lipopeptide"),("Acetyl Hexapeptide-8","expression"),("Pentapeptide-18","expression"),("Oligopeptide-1","growth_factor"),("Arginine/Lysine Polypeptide","polypeptide"),("Copper Palmitoyl Heptapeptide-14","copper"),("Heptapeptide-15 Palmitate","lipopeptide"),("Carnosine","other")],15)]
F["paulas_choice"] = [item(n,c,p) for p,(n,c) in enumerate([
    ("Palmitoyl Tetrapeptide-72 Amide","lipopeptide"),("sh-Polypeptide-121","polypeptide"),("Palmitoyl Dipeptide-5 Diaminobutyroyl Hydroxythreonine","lipopeptide"),("Palmitoyl Tripeptide-5","lipopeptide"),("Tridecapeptide-1","other"),("Tetradecyl Aminobutyroylvalylaminobutyric Urea Acetate","other")],10)]
F["naturium"] = [item("Acetyl Hexapeptide-8","expression",16),item("Copper Palmitoyl Heptapeptide-14","copper",17),item("Palmitoyl sh-Hexapeptide-13 Serine SP Amide","lipopeptide",18)]
F["minimalist"] = [
    item("Palmitoyl Tripeptide-1","lipopeptide",4,(M3000_PT1(7),)*3,"official 7% Matrixyl 3000 × supplier assay","Matrixyl 3000","published_technology_supplier_assay",TECH_URL["matrixyl_3000_assay"]), item("Palmitoyl Tetrapeptide-7","lipopeptide",5,(M3000_PT7(7),)*3,"official 7% Matrixyl 3000 × supplier assay","Matrixyl 3000","published_technology_supplier_assay",TECH_URL["matrixyl_3000_assay"]),
    *[item(n,"growth_factor",p,(0.000001,0.00001,0.0001),"official 3% Bio-Placenta complex; individual assay undisclosed","Bio-Placenta","modeled_with_published_complex") for p,n in enumerate(["sh-Oligopeptide-1","sh-Oligopeptide-2","sh-Polypeptide-1","sh-Polypeptide-9","sh-Polypeptide-11"],7)]]
F["inkey"] = [item("Palmitoyl Tripeptide-1","lipopeptide",18,(M3000_PT1(1),)*3,"official 1% Matrixyl 3000 × supplier assay","Matrixyl 3000"),item("Palmitoyl Tetrapeptide-7","lipopeptide",17,(M3000_PT7(1),)*3,"official 1% Matrixyl 3000 × supplier assay","Matrixyl 3000"),item("Palmitoyl Dipeptide-5 Diaminobutyroyl Hydroxythreonine","lipopeptide",13),item("Palmitoyl Dipeptide-5 Diaminohydroxybutyrate","lipopeptide",14)]
F["timeless_m3000"] = [item("Palmitoyl Tripeptide-1","lipopeptide",2,(M3000_PT1(8),)*3,"official 8% Matrixyl 3000 × supplier assay","Matrixyl 3000"),item("Palmitoyl Tetrapeptide-7","lipopeptide",2,(M3000_PT7(8),)*3,"official 8% Matrixyl 3000 × supplier assay","Matrixyl 3000")]
F["timeless_s6"] = [item("Palmitoyl Tripeptide-38","lipopeptide",2,(S6_PT38(2),)*3,"official 2% Synthe'6 × supplier assay","Matrixyl Synthe'6")]
F["cosrx_blue"] = [item("Copper Tripeptide-1","copper",11),item("Dipeptide Diaminobutyroyl Benzylamide Diacetate","expression",24),item("Acetyl Hexapeptide-1","expression",25),item("Acetyl Heptapeptide-4","other",26),item("Acetyl Hexapeptide-8","expression",29),item("Acetyl Octapeptide-3","expression",40)]
F["cosrx_six"] = [item("Acetyl Hexapeptide-8","expression",7),item("Copper Tripeptide-1","copper",8),item("sh-Polypeptide-121","polypeptide",9),item("Dipeptide Diaminobutyroyl Benzylamide Diacetate","expression",10),item("Oligopeptide-68","other",11),item("Palmitoyl Tripeptide-8","lipopeptide",12)]
F["dermae"] = [item("Acetyl Hexapeptide-8","expression",4),item("Palmitoyl Tripeptide-38","lipopeptide",7)]
F["drunk_elephant"] = [item(n,c,p) for p,(n,c) in enumerate([
    ("sh-Oligopeptide-1","growth_factor"),("sh-Oligopeptide-2","growth_factor"),("sh-Polypeptide-1","growth_factor"),("sh-Polypeptide-9","growth_factor"),("sh-Polypeptide-11","growth_factor"),("Copper Palmitoyl Heptapeptide-14","copper"),("Heptapeptide-15 Palmitate","lipopeptide"),("Palmitoyl Tetrapeptide-7","lipopeptide"),("Palmitoyl Tripeptide-1","lipopeptide")],10)]
F["peach_lily"] = [item(n,c,p,((.2,.2,.2) if n=="Copper Tripeptide-1" else None),("official 0.2% copper peptide" if n=="Copper Tripeptide-1" else None),estimate_class=("published_claim_conditional" if n=="Copper Tripeptide-1" else None)) for p,(n,c) in enumerate([
    ("Copper Tripeptide-1","copper"),("Acetyl Hexapeptide-8","expression"),("Palmitoyl Tripeptide-1","lipopeptide"),("Tetrapeptide-21","other"),("Tetrapeptide-30","other"),("Heptasodium Hexacarboxymethyl Dipeptide-12","other"),("Acetyl Tetrapeptide-5","other"),("Palmitoyl Tripeptide-38","lipopeptide"),("Palmitoyl Pentapeptide-4","lipopeptide"),("Dipeptide-2","other"),("Tripeptide-1","other"),("Hexapeptide-9","other"),("Nonapeptide-1","other")],6)]
F["niod_cais3"] = [item("Tripeptide-29","other",3),item("Tripeptide-1 Copper Acetate","copper",4,(1,1,1),"official 1% GHK-Cu",estimate_class="published_final_dose"),item("Tripeptide-1 Acetate","other",5,(1,1,1),"official 1% GHK",estimate_class="published_final_dose"),item("Myristoyl Nonapeptide-3","lipopeptide",6),item("Trifluoroacetyl Tripeptide-2","other",7),item("Acetyl Tetrapeptide-2","other",8)]
F["allies_copper"] = [item("Copper Tripeptide Complex (INCI identity not disclosed)","copper",1,(0.001,0.01,0.1),"official 1% complex; pure GHK-Cu not listed in current INCI","1% Copper Tripeptide Complex","modeled_with_published_complex"),item("Acetyl Hexapeptide-8","expression",14,(0.001,0.005,0.01),"official 2% AHP-8 complex; pure assay undisclosed","2% AHP-8 Complex","modeled_with_published_complex")]
F["qa_multi"] = [item("Palmitoyl Tripeptide-1","lipopeptide",4,(M3000_PT1(1),M3000_PT1(3),M3000_PT1(5)),"modeled 1/3/5% Matrikines/Matrixyl-like complex"),item("Palmitoyl Tetrapeptide-7","lipopeptide",5,(M3000_PT7(1),M3000_PT7(3),M3000_PT7(5)),"modeled 1/3/5% Matrikines/Matrixyl-like complex"),item("Acetyl Hexapeptide-1","expression",6),item("sh-Polypeptide-69","polypeptide",7)]

line_rows = []
for formula_id, ingredients in F.items():
    product = PRODUCTS[formula_id]
    product_name = DISPLAY_NAME.get(formula_id, product["product"])
    volume = float(product["volume_ml"])
    for ingredient in ingredients:
        band = ingredient["exact"] or PRIORS[ingredient["class"]][zone(ingredient["position"])]
        basis = ingredient["basis"] or f"INCI position {ingredient['position']} + {ingredient['class']} prior ({zone(ingredient['position'])} zone)"
        estimate_class = ingredient["estimate_class"] or ("published_or_supplier_derived" if ingredient["exact"] else "modeled_inci_class_prior")
        amounts = [volume * pct / 100 for pct in band]
        line_rows.append({
            "formula_id": formula_id, "product": product_name, "brand": product["brand"],
            "volume_ml": f"{volume:g}", "retail_usd": product["retail_usd"],
            "ingredient_name": ingredient["name"], "material_class": ingredient["class"],
            "inci_position": ingredient["position"], "technology": ingredient["technology"],
            "concentration_low_pct": f"{band[0]:.9g}", "concentration_base_pct": f"{band[1]:.9g}", "concentration_high_pct": f"{band[2]:.9g}",
            "amount_low_g": f"{amounts[0]:.9g}", "amount_base_g": f"{amounts[1]:.9g}", "amount_high_g": f"{amounts[2]:.9g}",
            "amount_basis": basis, "estimate_class": estimate_class,
            "included_in_peptide_mass": "yes" if ingredient["include"] else "no",
            "product_source_url": URL[formula_id],
            "basis_source_url": ingredient["basis_url"] or (URL[formula_id] if ingredient["exact"] else TECH_URL["inci_rule"]),
        })

with OUT_LINES.open("w", newline="") as handle:
    writer = csv.DictWriter(handle, fieldnames=list(line_rows[0]))
    writer.writeheader(); writer.writerows(line_rows)

summaries = []
for formula_id, product in PRODUCTS.items():
    rows = [r for r in line_rows if r["formula_id"] == formula_id]
    counted = [r for r in rows if r["included_in_peptide_mass"] == "yes"]
    active_mg = sum(float(r["amount_base_g"]) for r in counted) * 1000
    active_low = sum(float(r["amount_low_g"]) for r in counted) * 1000
    active_high = sum(float(r["amount_high_g"]) for r in counted) * 1000
    retail = float(product["retail_usd"])
    tech_band, tech_basis = TECH[formula_id]
    tech_g_band = [float(product["volume_ml"]) * pct / 100 for pct in tech_band]
    anchored_classes = {"published_or_supplier_derived", "published_technology_supplier_assay",
                        "published_final_dose", "published_claim_conditional",
                        "independent_secondary"}
    anchored_count = sum(r["estimate_class"] in anchored_classes for r in counted)
    contextual_count = sum(r["estimate_class"] != "modeled_inci_class_prior" for r in counted)
    anchored_coverage = 100 * anchored_count / len(counted) if counted else 0
    contextual_coverage = 100 * contextual_count / len(counted) if counted else 0
    summaries.append({
        "formula_id": formula_id, "product": DISPLAY_NAME.get(formula_id, product["product"]), "brand": product["brand"],
        "volume_ml": product["volume_ml"], "retail_usd": product["retail_usd"],
        "peptide_ingredient_count": len(counted), "adjacent_nonpeptide_count": len(rows) - len(counted),
        "source_anchored_amount_lines": anchored_count,
        "source_anchored_amount_coverage_pct": f"{anchored_coverage:.1f}",
        "context_supported_amount_lines": contextual_count,
        "context_supported_amount_coverage_pct": f"{contextual_coverage:.1f}",
        "estimated_active_mg_low": f"{active_low:.6g}", "estimated_active_mg_base": f"{active_mg:.6g}", "estimated_active_mg_high": f"{active_high:.6g}",
        "estimated_purchased_technology_pct_low": f"{tech_band[0]:.6g}",
        "estimated_purchased_technology_pct_base": f"{tech_band[1]:.6g}",
        "estimated_purchased_technology_pct_high": f"{tech_band[2]:.6g}",
        "estimated_purchased_technology_g_low": f"{tech_g_band[0]:.6g}",
        "estimated_purchased_technology_g_base": f"{tech_g_band[1]:.6g}",
        "estimated_purchased_technology_g_high": f"{tech_g_band[2]:.6g}",
        "retail_usd_per_estimated_active_mg": f"{retail/active_mg:.6g}" if active_mg else "",
        "retail_usd_per_purchased_technology_g": f"{retail/tech_g_band[1]:.6g}" if tech_g_band[1] else "",
        "retail_usd_per_ml": f"{retail/float(product['volume_ml']):.6g}",
        "formula_confidence": product["confidence"], "source_url": URL[formula_id],
        "technology_amount_basis": tech_basis,
        "audit_finding": AUDIT.get(formula_id, "No peptide-identity omission found in the current source used for this row."),
        "notes": "Pure-active mass is not efficacy-equivalent across peptides; purchased-technology mass includes carriers and complexes. Estimates never use finished-product retail price as an input."
    })

with OUT_PRODUCTS.open("w", newline="") as handle:
    writer = csv.DictWriter(handle, fieldnames=list(summaries[0]))
    writer.writeheader(); writer.writerows(summaries)

OUT_LINES_JS.write_text("window.PEPTIDE_FORMULA_INGREDIENT_AUDIT = " + json.dumps(line_rows, ensure_ascii=False) + ";\n")
OUT_PRODUCTS_JS.write_text("window.PEPTIDE_FORMULA_VALUE_SUMMARY = " + json.dumps(summaries, ensure_ascii=False) + ";\n")
OUT_SCENARIOS_JS.write_text("window.PEPTIDE_PRICE_SCENARIOS = " + json.dumps(PRICE_SCENARIOS, ensure_ascii=False) + ";\n")
OUT_COST_JS.write_text("window.PEPTIDE_COST_CSV = " + json.dumps((TOPIC / "data/peptide_cost_model.csv").read_text(), ensure_ascii=False) + ";\n")

print(f"WROTE {OUT_LINES} ({len(line_rows)} ingredient rows)")
print(f"WROTE {OUT_PRODUCTS} ({len(summaries)} products)")
print(f"WROTE {OUT_LINES_JS}")
print(f"WROTE {OUT_PRODUCTS_JS}")
print(f"WROTE {OUT_SCENARIOS_JS}")
print(f"WROTE {OUT_COST_JS}")
