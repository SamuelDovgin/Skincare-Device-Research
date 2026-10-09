# Generic RF devices and the MimiSilk / DLUS manufacturer lead

*Updated 2026-10-09. Supplier descriptions establish advertised claims, not measured treatment output. See the [wattage chart](rf_power_explorer.html) and [power methodology](index.html#doc19).*

**The generic market has higher advertised numbers, but less usable output evidence.** The best next step is to identify the exact device, probe and power convention before attempting an output estimate. A common shell, frequency or RF01 name is insufficient to identify a factory or electronics.

## Generic/OEM comparison

| Unit / configuration | RF watts | Electrical input / supply | Evidence and unresolved issue |
|---|---|---|---|
| MLAY RF01 face / body | 25 / 50 W seller output claim | 50 W rated input | [P33](https://mlay.co/product/rf01/) — output convention/load missing; equality at body maximum cannot be assumed continuous |
| MLAY S3 handheld | 25 W face / 14 W body output claims | No input watt or load disclosed | [P111](https://www.mlayofficial.com/products/mlay-rf-beauty-instrument-s3) — current official page; starred manufacturer claims, not bench data |
| MLAY RF02 S02B current retail page | RF output not stated | 36 W rated input | [P112](https://www.mlayofficial.com/products/mlay-rf-instrument-rf02) — whole-device input is not RF output |
| MLAY RF02 / S06 brochure variant | 38 W output claim* | Power input convention absent | [P113](https://exhibitorsearch.messefrankfurt.com/images/original/document_downloads/10000391202501/397636/1739246184332_3510192324.pdf) — indexed brochure; host is now 404; no identity match to S02B |
| MLAY S03 / S04 brochure handheld variants | 12 W* / 13 W* output claims | S03: 3.7 V × 2000 mAh; S04: 7.4 V × 650 mAh | [P113](https://exhibitorsearch.messefrankfurt.com/images/original/document_downloads/10000391202501/397636/1739246184332_3510192324.pdf) — same indexed source; runtime, load and duty cycle unavailable |
| MLAY RF01 / S05 brochure variant | 48 W output claim* | Non-battery configuration; input not stated | [P113](https://exhibitorsearch.messefrankfurt.com/images/original/document_downloads/10000391202501/397636/1739246184332_3510192324.pdf) — separate from current RF01 page; version match unresolved |
| Konmison LB056B | Not disclosed | 55 W consumption | [P35](https://www.konmison.com/product-item/3-in-1-rf-radio-frequency-facial-machine/) — 2 MHz; 1–15 J/cm² energy claim; no valid watt conversion without time/area |
| FREYARA Mini 3in1 | 20–50 W handle claim | 24 V × 3 A = 72 W supply capacity | [P36](https://it.freyara.com/products/mini-3in1-rf-dispositivo-di-bellezza-ringiovanimento-lifting-rimozione-delle-rughe-rassodamento-della-pelle-per-viso-e-occhi) · [P38](https://img.freyara.com/catalog/instruction/FY04.0208US.pdf) — three-probe triangular family; no same-unit FDA/bench match |
| FREYARA 2in1 tripolar / hexapolar | 20–30 / 50–60 W handle claims | 72 W supply capacity | [P37](https://it.freyara.com/products/dispositivo-di-bellezza-rf-2in1-con-3-sonde-e-6-sonde-ringiovanimento-sollevamento-rimozione-delle-rughe-rassodamento-della-pelle-per-viso-e-occhi) — separate handles and contact area; seller’s mHz typography is retained as an ambiguity |
| MYCHWAY CET/RET console | CET S/M/L/XL: 65/60/70/110 W; RET: 130/150/200/300 W | 110–220 V AC, total input not established here | [P39](https://us.mychway.com/product/cet-ret-rf-face-lifting-skin-care-winkle-removal) — face/body electrode modes, not interchangeable handheld outputs |
| MYCHWAY MS-11Y3 | Comparable output unknown | Unresolved | [P40](https://manual.mychway.com/UserManual/ms-11y3instructionnew.pdf) — supplier manual preserved; vague clinical claims do not define watts |
| MYCHWAY MS-76F1SBMAX | Face 70 W*, eye 40 W*, body 80 W* | 80 W system input | [P114](https://manual.mychway.com/UserManual/ms-76f1sbmax-en-20250327.pdf) — supplier manual claims; no load/duty convention and body claim equals total input |
| NEO Alpha / Plus | 300 W headline; face/Soft output unresolved | Plus directory calls 300 W consumption | [P41](https://www.rf-skincare.com/shop/view.html?cpage_pq=182&spage_pq=181&uid=32) · [P77](https://prod.danawa.com/info/?pcode=14102141) — exact Alpha electrical identity and load testing unresolved |
| Allfond / unnamed RF01 / Margotan | Unknown | Exact unit label missing | Pasted leads only; no transferred specs from lookalikes |

**What this group found:** the new FREYARA 2in1 listing actually distinguishes 20–30 W and 50–60 W handles; the triangular Mini lists 20–50 W. Combining those claims into one generic “50 W machine” would erase meaningful differences. No independent comparative RF load test for these generic units was found.

## MimiSilk Vera versus DLUS D2

| Question | Current finding | Confidence |
|---|---|---|
| Does Vera advertise 6.25 MHz and 18 W? | Yes; product and brand guide | Verified marketing claim, not measured RF |
| What does D2’s 18 W mean? | Chinese directory says supply power; retailer says consumption | Listing evidence, not RF output |
| Who is named for D2? | Pasted text and indexed directory identify Shenzhen Guangxiang Technology (深圳市光向科技有限公司) | Secondary supplier lead; directory direct capture blocked |
| Are Vera and D2 the same internals? | No contract, shared internal model, factory label or teardown recovered | Unconfirmed |
| Are they both corded? | Vera is described as corded; D2 retailer describes rechargeable/cordless | Do not merge; battery details not verified |
| Does a verified Vera K-number exist in this corpus? | None supplied or matched here | Clearance remains unverified; search absence is not proof of noncompliance |
| Does a higher MHz prove 2.5–3 mm heating or better collagen? | No exact-device depth map found | Marketing claim unresolved |
| Is Level 3 temperature consistent? | Product FAQ 49–50°C versus guide 52°C in prior/pasted capture trail | Conflicting claimed dermal values, not measured controller cutoff |

Sources: [P24](https://www.mimisilk.com/products/mimisilk-vera-rf-sculpt-6-25mhz-gel-free-radio-frequency-skin-lifting-device) · [P25](https://www.mimisilk.com/blogs/news/how-to-use-mimisilk-vera-rf-sculpt-full-guide-expected-results) · [P26](https://www.mimisilk.com/blogs/news/professional-grade-rf-frequency-at-home-how-mimisilk-vera-closes-the-gap-safely) · [P27](https://imeirongyi.com/vs/mid-10-temp-125-einfoids-843%2C906.html) · [P28](https://mycosmeticslondon.co.uk/products/professional-rf-facial-device-for-skin-lifting)

**What this section found:** similarity makes D2 a worthwhile OEM lead, but a secondary directory is not a factory statement connecting it to Vera. The 18 W supply/consumption versus RF-output discrepancy is a reason to request evidence, not a basis for declaring that Vera has a known lower output. The chart retains Vera’s 18 W in the marketing view only.

The pasted ownership claim (Label Skincare Limited; Hong Kong registration 3495922; U.S. trademark application 99732522) is preserved as a **lead that was not independently verified in this pass**. Even verified brand ownership would not establish the factory. The pasted “12 years” history discrepancy likewise remains unresolved rather than being promoted to a finding of misrepresentation.

## What can be inferred honestly?

If the **same unit** has verified maximum continuous input consumption and no other energy source, continuous RF output must leave allowance for conversion/control losses. An adapter label alone is capacity, and a battery can support short peaks beyond charger output. These qualifications prevent a reliable device-specific lower bound.

The pasted 18 W × 50/60/70/80% calculations (9/10.8/12.6/14.4 W) are arithmetic scenarios. No Vera efficiency measurement supports those percentages, and D2 equivalence is unconfirmed. **They are not a likely-wattage estimate and are excluded from the ranking.** The same rule applies to a 55 W generic machine: consumption cannot be relabeled as RF.

## Evidence request for a seller or factory

1. Exact factory legal name, brand/model label, probe model, manufacturing revision, manual and adapter label; OEM identity evidence connecting those records.
2. RF power versus characterized impedance, with on-pulse/RMS/session-average convention; applicable electrode pair/area and all mode limits.
3. RF frequency/waveform, pulse timing, temperature sensing position, calibrated cutoff, contact/movement interlocks and test conditions.
4. Measured temperature versus time at surface and specified tissue depths; clinical protocol and exact-model outcome evidence.
5. If claiming U.S. clearance, K-number or De Novo number, named model and cleared indication; listing/registration alone is insufficient.

These are documentation requests, not instructions to open energized equipment or increase treatment intensity. Bench verification belongs with an RF-qualified laboratory. A wall wattmeter measures electrical consumption, not the RF delivered to a load or absorbed by dermis.

## Recovery trail

[Full device ledger](data/rf_power_atlas_2026-10-09.json) · [Source register](index.html#doc21) · [Verbose dated log](source_docs/research_resource_log_2026-10-09.txt) · [Original pasted MimiSilk/generic research](source_docs/power_audit_2026-10-09/U01_user_research.txt).
