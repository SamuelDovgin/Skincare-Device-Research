window.RF_SPEC_PROFILES = {
  asOf: "2026-10-02",
  criteria: [
    { id: "identity", label: "Exact model & use scope", help: "Named retail model, intended use and jurisdiction are traceable." },
    { id: "control", label: "Temperature/contact control", help: "Sensor/control disclosure, cutoff behavior and contact safeguards." },
    { id: "clinical", label: "Exact-model human outcomes", help: "Direct outcomes for this exact home device; study design limits remain visible." },
    { id: "technical", label: "RF dose transparency", help: "Carrier, waveform/output test conditions, electrode/coupling details." }
  ],
  scale: [
    "1 — limited public evidence / claims only / exact-model study not located",
    "2 — partial exact-model information; important method or validation gaps",
    "3 — strong model-specific primary record, with material limits",
    "4 — unusually complete, exact-model primary disclosure for this criterion"
  ],
  coverageFields: ["Exact model identity", "Carrier / geometry", "Temperature / contact feedback", "RF output under test conditions", "Exact-model human outcomes", "Regulatory / intended-use scope"],
  profiles: [
    { id: "balanced", label: "Balanced", weights: { identity: 2, control: 3, clinical: 3, technical: 2 } },
    { id: "controls", label: "Safety & controls first", weights: { identity: 2, control: 5, clinical: 1, technical: 2 } },
    { id: "outcomes", label: "Human evidence first", weights: { identity: 1, control: 2, clinical: 5, technical: 2 } },
    { id: "engineering", label: "Engineering disclosure first", weights: { identity: 1, control: 3, clinical: 1, technical: 5 } }
  ],
  devices: [
    {
      id: "currentbody", brand: "CurrentBody", model: "Skin RF ST030", range: [1, 1], topology: "Bipolar RF; approx. 2.2 cm² treatment area; gel interface",
      temperature: "FDA filing: maximum 40.5 ±0.5 °C; two redundant thermistors. Store page describes RF pause/restart at 40–41 °C.",
      output: "1 ±0.05 MHz; 5 ±1 W in FDA summary; bench validation at 200 Ω. Waveform/pulse details are in the filing.",
      clinical: "Retailer reports independent clinical studies and 89% saw an improvement at 8 weeks; public protocol details were not recovered here. K232424 is a substantial-equivalence clearance, not a new head-to-head trial.",
      useScope: "FDA 510(k) K232424; labeled for mild-to-moderate facial wrinkles in adults with Fitzpatrick I–IV. Verify current IFU and local seller/warranty.",
      price: "$385.99 U.S. official page snapshot (2026-10-02); shipping, promotion and stock can vary.",
      scores: { identity: 4, control: 4, clinical: 2, technical: 4 },
      ratingNotes: { identity: "Exact SKU and U.S. FDA filing / intended-use scope.", control: "Two redundant thermistors, controlled maximum and rapid contact stop documented.", clinical: "Human outcome claim is brand-reported; study protocol and comparator are not sufficiently exposed in the reviewed page.", technical: "Carrier, power, tolerance, load and treatment area are specified in FDA/official sources." },
      coverage: ["present", "present", "present", "present", "partial", "present"],
      verdict: "Best currently verified U.S. specification benchmark in this shortlist. Clear controls and scope; clinical advantage over peers is not established.",
      sources: [{ label: "FDA K232424", href: "source_docs/FDA_K232424_CurrentBody.pdf" }, { label: "CurrentBody U.S. specifications", href: "https://www.currentbody.us/products/currentbody-skin-radio-frequency-device" }]
    },
    {
      id: "newa", brand: "NEWA", model: "Original home RF (DEN150005; verify current generation)", range: [1, 1], topology: "Bipolar multi-electrode home RF; exact successor mapping needs verification",
      temperature: "FDA filing: RF stops above 42 °C; surface acceptance criterion 42 ±0.5 °C; one embedded thermistor described.",
      output: "1 MHz; 10 W ±20% validation at a 360 Ω load; 750 ms pulse cycle and 300 ms pulse duration in the filing.",
      clinical: "FDA De Novo home-use study: 69 enrolled, 62 completed and 59/62 met the blinded wrinkle-responder criterion. No sham-controlled comparison; exact original model only.",
      useScope: "FDA De Novo DEN150005 for a narrow home wrinkle indication and tested population. Do not transfer to NEWA Plus or another successor without model mapping.",
      price: "Current official offer/availability not verified in the 2026-10-02 research pass.",
      scores: { identity: 4, control: 3, clinical: 3, technical: 4 },
      ratingNotes: { identity: "Exact original model and FDA scope are unusually clear; present successor/retail status remains open.", control: "Numeric shutoff and validation are disclosed; a single thermistor is described rather than redundancy.", clinical: "Direct exact-model home clinical performance record, but uncontrolled and population/indication limited.", technical: "Carrier, pulse timing, waveform and load-specific power validation are available." },
      coverage: ["present", "present", "present", "present", "present", "present"],
      verdict: "Strongest direct home-use clinical/regulatory evidence reference here. Treat as a purchase candidate only after verifying exact SKU, current stock and support.",
      sources: [{ label: "FDA De Novo DEN150005", href: "source_docs/FDA_DEN150005_NEWA.pdf" }, { label: "NEWA official store status", href: "https://mynewa.com/products/newa" }]
    },
    {
      id: "sensilift", brand: "Sensica", model: "Sensilift Pro ST300", range: [1, 1], topology: "Bipolar home RF; RF delivery limited by hardware",
      temperature: "FDA filing: maximum 40 ±0.5 °C; two redundant thermistors continuously adjust output.",
      output: "1 ±0.05 MHz; maximum 6 ±1 W; 200 Ω load used for power validation.",
      clinical: "K250341 relies on bench verification and substantial equivalence; no new subject-device human outcome trial is reported in its summary.",
      useScope: "FDA 510(k) K250341; non-invasive OTC use for mild-to-moderate facial wrinkles in adults with Fitzpatrick I–IV.",
      price: "$449 in the earlier official Sensica category snapshot; recheck local model, stock, warranty and returns.",
      scores: { identity: 4, control: 4, clinical: 1, technical: 3 },
      ratingNotes: { identity: "Exact current Pro model and U.S. intended use are present in the FDA summary.", control: "Redundant sensors and controlled maximum are described in primary filing.", clinical: "No new human outcomes for ST300 were reported in the filing; this is an evidence gap, not proof of no effect.", technical: "Frequency, maximum power and load validation are disclosed, but less pulse/output detail is readily surfaced than for NEWA." },
      coverage: ["present", "present", "present", "present", "notLocated", "present"],
      verdict: "Strong controls and FDA documentation, but no new exact-model outcome trial. Compare total price and support with CurrentBody.",
      sources: [{ label: "FDA K250341", href: "source_docs/FDA_K250341_Sensilift_Pro.pdf" }, { label: "Sensica RF product information", href: "https://sensica.com/pages/rf-skin-tightening" }]
    },
    {
      id: "panasonic", brand: "Panasonic", model: "VITALIFT RF LUXE EH-SR90", range: [1, 6], topology: "Variable-frequency RF; eight-electrode head; RF, EMS, ion and LED modes",
      temperature: "No numeric surface-temperature cap, sensor count or depth-resolved temperature validated in reviewed official pages.",
      output: "Manufacturer states variable RF 1–6 MHz and eight electrodes; calibrated RF output, waveform and load are not disclosed in sources reviewed.",
      clinical: "No exact-SR90 peer-reviewed human trial located. Feature/brand claims are not a frequency-isolated result.",
      useScope: "Official Japanese consumer listing. Panasonic purchase-promotion eligibility began 2026-09-15; U.S. medical-device scope and stock/warranty were not verified.",
      price: "¥99,000 official Japan listing snapshot; regional offers and taxes differ.",
      scores: { identity: 3, control: 1, clinical: 1, technical: 2 },
      ratingNotes: { identity: "Exact manufacturer model, features and regional consumer use are documented; U.S. FDA indication was not verified.", control: "No numeric RF temperature cutoff or sensor fault response was found on the reviewed official pages.", clinical: "No current-model peer-reviewed clinical outcome trial was located in this search; that is not proof of no benefit.", technical: "Carrier range and electrode count are specified; calibrated output/waveform and thermal traces are missing." },
      coverage: ["present", "present", "notLocated", "notLocated", "notLocated", "partial"],
      verdict: "Feature-rich 6 MHz watchlist option. Wait for independent thermal characterization and exact-model outcomes before paying an MHz premium.",
      sources: [{ label: "Panasonic EH-SR90", href: "https://panasonic.jp/face/products/EH-SR90.html" }, { label: "Official purchase-period campaign", href: "https://panasonic.jp/beauty/campaign/26autumn-face-cashback.html" }]
    },
    {
      id: "yaman", brand: "YA-MAN", model: "Bloom 6 YJFS16PN1", range: [0.5, 2.5], topology: "Five-layer ring / parallel-electrode RF; resistance-factor adjustment; contact sensor",
      temperature: "No numeric RF surface cap or thermal measurement protocol verified. Official page describes resistance feedback and output/contact interruption.",
      output: "Manufacturer claims 0.5–2.5 MHz variable RF. RF watts, waveform/load validation and a depth-resolved thermal trace were not disclosed on the reviewed page.",
      clinical: "No exact Bloom 6 human outcome trial located. The 2025 multimodal YA-MAN ACE/Jmoon study does not map securely to Bloom 6 or isolate carrier frequency.",
      useScope: "Exact global product code and official manufacturer page are available; U.S. FDA OTC indication was not verified. Confirm the manual and regional warranty.",
      price: "Current authorized price/stock not verified in this pass; Japan and international bundles vary.",
      scores: { identity: 3, control: 2, clinical: 1, technical: 3 },
      ratingNotes: { identity: "Exact model code and official product information are clear; a matching U.S. medical indication is not established here.", control: "Contact and resistance feedback are described, but numeric thermal cap and independent sensor validation are absent.", clinical: "No exact Bloom 6 trial was located; the adjacent YA-MAN study has unresolved SKU and multimodal transfer.", technical: "Variable band and electrode architecture are clear; output under load and temperature-time behavior are not." },
      coverage: ["present", "present", "partial", "notLocated", "notLocated", "partial"],
      verdict: "Most interesting consumer engineering design in this scan; promising to benchmark, not established as the best remodeling device.",
      sources: [{ label: "YA-MAN Bloom 6 official specifications", href: "https://www.ya-man.com/en/products/bloom-6.php" }, { label: "YA-MAN/Jmoon clinical evidence limits", href: "index.html#doc13" }]
    },
    {
      id: "mimisilk", brand: "MimiSilk", model: "Vera RF Sculpt", range: [6.25, 6.25], topology: "Gel-free multipolar / displacement-current design (manufacturer description)",
      temperature: "Brand FAQ claims dermal 45–50 °C by level and skin below 117 °F (47.2 °C); another guide gives a different upper-level value. Measurement method and independent validation not recovered.",
      output: "Brand lists 6.25 MHz and 4.5/9/18 W levels; load, RF waveform, calibration and output measurement method were not verified.",
      clinical: "No exact Vera product-specific peer-reviewed human outcome study or regulatory clinical record located. Product testimonials and generic RF citations do not establish Vera outcomes.",
      useScope: "Exact consumer SKU and warnings are presented on the brand page; U.S. medical-device authorization / intended clinical scope was not verified.",
      price: "$699 product-page snapshot; confirm current final price, returns and warranty.",
      scores: { identity: 2, control: 1, clinical: 1, technical: 2 },
      ratingNotes: { identity: "Exact model is named, but public product claims do not establish a comparable regulatory/clinical indication.", control: "Temperature/impedance claims are manufacturer-only and the surface/dermal figures conflict or lack measurement detail.", clinical: "No product-specific clinical record was located in the reviewed sources; this is an evidence gap, not a measured outcome.", technical: "Frequency and nominal watt levels are advertised, but output test conditions, waveform and thermal validation are not disclosed." },
      coverage: ["present", "present", "partial", "partial", "notLocated", "partial"],
      verdict: "Convenience-led watchlist only. Do not treat 6.25 MHz, claimed 2.5–3 mm depth or a high claimed dermal temperature as verified dose or Thermage equivalence.",
      sources: [{ label: "MimiSilk Vera product page", href: "https://www.mimisilk.com/products/mimisilk-vera-rf-sculpt-6-25mhz-gel-free-radio-frequency-skin-lifting-device" }, { label: "Temperature FAQ claim", href: "https://www.mimisilk.com/fr/products/mimisilk-vera-rf-sculpt-6-25mhz-gel-free-radio-frequency-skin-lifting-device" }, { label: "Temperature guide comparison", href: "https://www.mimisilk.com/blogs/news/how-to-use-mimisilk-vera-rf-sculpt-full-guide-expected-results" }]
    }
  ]
};
