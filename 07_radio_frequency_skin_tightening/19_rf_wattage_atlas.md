# Home RF wattage atlas: rated, measured and inferred power

*Updated 2026-10-09. 135 comparison records, including model families, regional revisions, accessories and professional modes; this is not 135 unique devices or an exhaustive worldwide census.*

The largest number in a listing is often the wrong number to compare. **The clearest numeric home RF bench result in this corpus is original wired NEWA: 10 W into 360 Ω.** A manufacturer manual specifies 20 W for EU Silk’n FaceTite MultiPlatform H2501; the current North American H2502/HA2502 manual specifies 15 W. Higher advertised generic outputs exist, but load, duty cycle and facial applicability are generally missing.

Open the [searchable wattage chart and full comparison ledger](rf_power_explorer.html). Use separate views for RF specifications, seller claims, input/charger watts, and battery estimates. Unknown output stays visible and is never plotted as zero. The [used-market and generic-device value tiers](index.html#doc22) separate conditional model matches from generic units with no verifiable output.

## What each watt figure means

| Quantity | What it establishes | What it does not establish |
|---|---|---|
| Adapter capacity, V × A | Rated DC supply capacity | Actual operating consumption or RF output; a battery can also supply transient energy |
| Charging consumption | Electrical use while charging | Treatment watts, battery energy, or RF watts |
| RF maximum / RMS rating | Manufacturer/regulatory RF specification, with the stated load and mode | Continuous output throughout a treatment or absorbed dermal power |
| Numeric bench measurement | Reported output at the stated electrical test load | In-vivo dermal dose, an independent comparative lab result, or better outcomes |
| Battery V × Ah ÷ runtime | Nominal average whole-device electrical-energy budget under that runtime condition | RF share, full-power runtime, or measured electrical consumption |
| Curve read-off | Approximate manufacturer plot value | A fresh independent measurement, or an exact value at an untested load |

## Home RF: regulatory specifications first

These are **headline maximum ratings**, not a common-load comparison. The original sensiLift’s actual selectable setting differs from its headline hardware maximum.

| Device / exact version | RF specification | Highest disclosed treatment setting | Numeric measured output public? | Load / temperature | Evidence |
|---|---:|---:|---|---|---|
| NEWA Original wired 3DEEP | 10 W ±20% | Not separately disclosed | 10 W | 360 Ω; 42°C sensor shutoff | [P01](https://www.accessdata.fda.gov/cdrh_docs/reviews/DEN150005.pdf) |
| Silk’n Titan AllWays | 10 W ±20% | Not separately disclosed | No exact result; specification / passing tests only | Undisclosed Ω; Undisclosed | [P06](https://www.accessdata.fda.gov/cdrh_docs/pdf23/K230013.pdf) |
| Sensica sensiLift original | 9 W ±1 hardware; 6.5 W highest setting | 6.5 W | No exact result; specification / passing tests only | 200 Ω; 40°C shutoff | [P03](https://www.accessdata.fda.gov/cdrh_docs/pdf17/K170499.pdf) |
| Sensica sensiLift Pro ST300 | 6 W ±1 | 6 W | No exact result; specification / passing tests only | 200 Ω; 40 ±0.5°C maximum | [P04](https://www.accessdata.fda.gov/cdrh_docs/pdf25/K250341.pdf) |
| TriPollar STOP U UXV | 5.7 W ±10% RMS | 5.7 W | No exact result; specification / passing tests only | 200 Ω; Temperature-controlled; exact numeric cutoff not confirmed here | [P05](https://www.accessdata.fda.gov/cdrh_docs/pdf20/K203665.pdf) |
| CurrentBody Skin RF ST030 (US) | 5 W ±1 | 5 W | No exact result; specification / passing tests only | 200 Ω; 40.5 ±0.5°C maximum | [P02](https://www.accessdata.fda.gov/cdrh_docs/pdf23/K232424.pdf) |

**What this group found:** FDA records give a useful 5–10 W handheld RF specification range, but only NEWA supplies an explicit 10 W numerical bench result here. “Tests passed” is not a published watt measurement. Surface cutoffs around 40–43°C are controller limits, not measurements of dermal temperature at 1–3 mm.

### NEWA pulse timing: a conditional estimate

The De Novo record gives 300 ms or 450 ms pulses per 750 ms cycle: duty factors 0.40 and 0.60. If its 10 W measurement is on-pulse power, then **10 × duty factor = 4 or 6 W** before further regulation. The public document calls its measured value “total power” without fully defining the averaging convention. Consequently this atlas does **not** place 4/6 W in the measured-output column or use it as a verified continuous-treatment ranking. Energy for any pulse would also require the applicable power convention. [P01](https://www.accessdata.fda.gov/cdrh_docs/reviews/DEN150005.pdf)

## Manual specifications and higher advertised values

| Device / configuration | Published value | Classification and limitation | Evidence |
|---|---:|---|---|
| Silk’n FaceTite MultiPlatform H2501 EU | 20 W maximum RF | Manufacturer IFU; exact-model U.S. clearance not established here | [P19](https://data.silkn.com/m/3675be4e752dbebb/original/FaceTite-MultiPlatform-UM.pdf) |
| Silk’n Titan MultiPlatform H2502 + HA2502 current NA | 15 W maximum RF | Current official IFU; 24 W adapter separately specified | [P17](https://data.silkn.com/asset/2a5aa6ed-322e-4d0b-afbe-5fc694289137/Titan-MultiPlatform-UM-NA.pdf) · [P21](https://www.silkn.com/skincare-devices/facial-rejuvenation-devices/titan-multiplatform-with-free-gel-SKUS000057.html?cgid=skin-care_facial-rejuvenation) |
| Silk’n H2502 + HA2502 historical IFU | 20 W; bare head 10 W | Historical mirror; not a second unique device; conflicts with current manual | [P76](https://device.report/m/91cc6032d88734ec2f9d4e9b1543aaadd7e9190fba691abbffb4ee4fcb4c0481) |
| Silk’n Titan Mini H2600 / original Titan H2111/H2112 | 10 W maximum RF | Distinct battery vs corded products | [P18](https://data.silkn.com/m/1b96e6d4c98d2a1a/original/Titan-Mini-UM-NA.pdf) · [P20](https://m.media-amazon.com/images/I/91wCR6lIVGS.pdf) |
| AMIRO R3 Turbo / R1 PRO US | 15 W advertised | No load-test report; 8→15 W predecessor/region discrepancy | [P29](https://amirobeauty.com/products/amiro-high-radiofrequency-skincare-device) · [P30](https://amirobeauty.com/products/r3-turbo-facial-rf-skin-tightening-device) · [P31](https://amirobeauty.com/pages/30-day-challenge) |
| MimiSilk Vera | 4.5 / 9 / 18 W advertised | RF output claim; DLUS’s 18 W supply/consumption lead does not verify it | [P24](https://www.mimisilk.com/products/mimisilk-vera-rf-sculpt-6-25mhz-gel-free-radio-frequency-skin-lifting-device) · [P25](https://www.mimisilk.com/blogs/news/how-to-use-mimisilk-vera-rf-sculpt-full-guide-expected-results) · [P28](https://mycosmeticslondon.co.uk/products/professional-rf-facial-device-for-skin-lifting) |
| MLAY RF01 | 25 W face / 50 W body claimed | Seller/brand listing; 50 W total input; peak/continuous convention missing | [P33](https://mlay.co/product/rf01/) |
| FREYARA Mini 3in1 | 20–50 W handle claim | Seller claim; 72 W supply capacity is a separate figure | [P36](https://it.freyara.com/products/mini-3in1-rf-dispositivo-di-bellezza-ringiovanimento-lifting-rimozione-delle-rughe-rassodamento-della-pelle-per-viso-e-occhi) |
| FREYARA 2in1 | 20–30 W tripolar / 50–60 W hexapolar | Two handles on one console; not interchangeable facial modes | [P37](https://it.freyara.com/products/dispositivo-di-bellezza-rf-2in1-con-3-sonde-e-6-sonde-ringiovanimento-sollevamento-rimozione-delle-rughe-rassodamento-della-pelle-per-viso-e-occhi) |
| MYCHWAY CET/RET | 60–110 W CET / 130–300 W RET claimed | Electrode-size-dependent seller values; separate tabletop class | [P39](https://us.mychway.com/product/cet-ret-rf-face-lifting-skin-care-winkle-removal) |
| TriPollar STOP VX2 Model U | 5.7 W at 200 Ω in text; plot reads about 6.6 W* | Same manual disagrees with its own curve; plotted points are approximate read-offs | [P105](https://cdn.shopify.com/s/files/1/0276/3089/5193/files/STOP_VX2.pdf?v=1691504919) |
| MLAY S3 handheld | 25 W face / 14 W body* | Current official product claims; load and duty convention absent | [P111](https://www.mlayofficial.com/products/mlay-rf-beauty-instrument-s3) |
| MLAY RF02 S02B | 36 W rated input; RF output undisclosed | Current official product page; keep separate from brochure RF02/S06 variant | [P112](https://www.mlayofficial.com/products/mlay-rf-instrument-rf02) · [P113](https://exhibitorsearch.messefrankfurt.com/images/original/document_downloads/10000391202501/397636/1739246184332_3510192324.pdf) |
| MLAY RF02 / S06 brochure variant | 38 W output* | Indexed brochure claim; source host returned 404; exact relation to S02B unresolved | [P113](https://exhibitorsearch.messefrankfurt.com/images/original/document_downloads/10000391202501/397636/1739246184332_3510192324.pdf) |
| MYCHWAY MS-76F1SBMAX | Face 70 W*, eye 40 W*, body 80 W* | Supplier manual; system input also 80 W; load/duty absent | [P114](https://manual.mychway.com/UserManual/ms-76f1sbmax-en-20250327.pdf) |

**Second-round manual recovery:** 22 exact-family YA-MAN English/Japanese manuals, three AMIRO manuals, three TriPollar manuals, two Panasonic manuals and the FOREO FAQ 103 manual are in the dated source register. YA-MAN’s extracted figures include 21 W whole-device consumption (Bloom 6); 18 W while charging (Bloom 5); 9 W while charging (Bloom WR); 4.5 W system/charging figures (Bright Lift, Deep Lift and Shiny NEO); 15–20 W whole-device consumption (Prestige S/SS/SP/SP III/PRO and EX Eye Pro); and 5 W while charging (CaviSpa Core PLUS). Those figures are not RF output. Exact manuals for Bloom Red, Shiny M18, Prestige SP II, HRF10, Photo PLUS Hyper, CaviSpa Core and legacy variants are preserved even where no defensible watts were printed. Panasonic EH-SR85/SR86 specifications say about 7 W while charging. AMIRO manuals add 5 V × 2 A / 2600 mAh for R1 Pro, 5 V × 3 A / 1500 mAh for S2 Seal Max, and 5 V × 3 A / 1200 mAh for S1; adapter and battery input values do not disclose treatment RF.

In the source register, each manual has both the manufacturer URL and a preserved local PDF link where the host allowed capture. The indexed MLAY brochure is the exception: its source host now returns 404, so a labeled excerpt of the indexed claims is archived with that limitation.

**What this group found:** a global “highest watts” list changes depending on whether it includes body probes, regional manuals or unsupported seller claims. The chart keeps those classes separate. A 300 W tabletop/body headline does not identify a 300 W facial home protocol. Values marked * are lower-confidence supplier/marketing output claims or approximate plot read-offs; the row detail links to the exact evidence. No relative collagen-effectiveness score is derived from watts.

## Battery and runtime audit

The equations are **E_nominal (Wh) = V_nominal × capacity_mAh / 1000** and **P_nominal-average (W) = E_nominal / (runtime_minutes / 60)**. These are arithmetic energy budgets, without an assumed RF-conversion efficiency. Cell voltage is mandatory: device/adapter voltage cannot replace it. Usable battery energy, ageing, intensity, duty control, other modalities and shutdown reserve are unknown.

| Device | Verified nominal battery | Runtime basis | Nominal average whole-device budget | What remains unknown |
|---|---|---|---:|---|
| FOREO FAQ 101 / FAQ 102 | 3.7 V × 1000 mAh = 3.7 Wh | Up to 30 minutes, official manuals | 7.4 W at that runtime | RF share and highest-setting runtime |
| Silk’n Titan Mini H2600 | 3.7 V × 600 mAh = 2.22 Wh | 30 minutes, official product graphic | 4.44 W | Full-power runtime; 10 W is a maximum |
| Silk’n Titan MultiPlatform H2502 | 3.7 V × 4000 mAh = 14.8 Wh | 40 minutes, official comparison graphic | 22.2 W | Mode/load under runtime claim; effective battery energy |
| Silk’n Titan AllWays | 3.7 V × 2600 mAh = 9.62 Wh | Exact official runtime not confirmed | Not calculated | Pasted secondary 20-minute claim would imply 28.86 W, so deserves rechecking |
| Silk’n FaceTite MultiPlatform H2501 | 4000 mAh; cell voltage unresolved | Runtime/model match unresolved | Not calculated | The 12 V rating is not verified cell voltage |
| AMIRO R3 Turbo | Pasted 2600 mAh lead; exact original manual not recovered | Unknown | Not calculated | Assumed 3.7 V would yield 9.62 Wh, not a verified battery spec |
| sensiLift Pro | Rechargeable; 21.6 W supply capacity disclosed | Capacity/runtime unknown | Not calculated | RF is specified separately at 6 ±1 W |
| Panasonic EH-SR85 / SR86 / SR90 | Li-ion; capacity not disclosed in consulted specs | About 7 / 4 / 4 days under usage conditions | Not calculated | 7 W is charging consumption, not RF |
| YA-MAN Photo PLUS Deep Lift | Capacity unresolved | Approximately 30 minutes on current official page | Not calculated | Pasted 4.5 W charging figure not recovered in current listing |
| MimiSilk Vera / wired NEWA / CurrentBody / STOP U | Corded treatment | No battery calculation | Not applicable | Actual RF is separately tested/specified/unknown |

Battery sources: [P22](https://www.foreo.com/manuals/faq-swiss-101) · [P23](https://www.foreo.com/manuals/faq-swiss-102) · [P18](https://data.silkn.com/m/1b96e6d4c98d2a1a/original/Titan-Mini-UM-NA.pdf) · [P73](https://www.silkn.com/skin-tightening/titan-mini-with-free-gel-SKUS000056.html) · [P17](https://data.silkn.com/asset/2a5aa6ed-322e-4d0b-afbe-5fc694289137/Titan-MultiPlatform-UM-NA.pdf) · [P06](https://www.accessdata.fda.gov/cdrh_docs/pdf23/K230013.pdf) · [P19](https://data.silkn.com/m/3675be4e752dbebb/original/FaceTite-MultiPlatform-UM.pdf) · [P04](https://www.accessdata.fda.gov/cdrh_docs/pdf25/K250341.pdf) · [P42](https://panasonic.jp/face/products/EH-SR90/spec.html) · [P43](https://panasonic.jp/face/products/EH-SR85/spec.html) · [P44](https://panasonic.jp/face/products/EH-SR86/spec.html) · [P45](https://www.ya-man-tokyo-japan.com/products/forface/photo-plus-deep-lift.html)

**What this section found:** known capacity plus runtime can test the consistency of a continuous-output claim; it cannot estimate RF watts reliably. “Up to” runtime has no specified test setting and is not a hard upper/lower RF bound. The atlas deliberately omits arbitrary 50–80% conversion-efficiency guesses from its device ranking.

## Load curves, thermal control and depth

The chart above plots the manual’s output-versus-load markers for the original Titan, current Titan MultiPlatform, Titan Mini and STOP VX2. An asterisk marks approximate visual read-offs from source plots, not bench measurements. The STOP VX2 manual also states 5.7 W at 200 Ω, while the curve appears closer to 6.6 W at the same load; both are preserved and the conflict is called out. The Titan Mini curve appears to be about 2.6 W at 200 Ω, not the earlier pasted estimate of 2.7 W. Open the preserved IFUs from each chart row to inspect the source plots. Different loads and graph scales do not support a normalized rank. [P17](https://data.silkn.com/asset/2a5aa6ed-322e-4d0b-afbe-5fc694289137/Titan-MultiPlatform-UM-NA.pdf) · [P18](https://data.silkn.com/m/1b96e6d4c98d2a1a/original/Titan-Mini-UM-NA.pdf) · [P20](https://m.media-amazon.com/images/I/91wCR6lIVGS.pdf) · [P105](https://cdn.shopify.com/s/files/1/0276/3089/5193/files/STOP_VX2.pdf?v=1691504919)

No verified product-specific temperature-versus-depth comparison was established for Vera, generic tabletop devices and the established handhelds. Electrical RF watts, skin-sensor temperature and collagen-remodeling outcomes are distinct measurements. The [clinical evidence map](index.html#doc11) and [MHz/temperature review](index.html#doc13) remain the outcome references.

## Professional and other thermal context

The chart includes professional context behind a separate filter: Thermage FLX 400 W; XERF 400 W at 6.78 MHz / 300 W at 2 MHz; Volnewmer 115 W; Oligio 145 W; TempSure 120 W wrinkle / 300 W tissue heating; Secret RF 25 W at 500 Ω; Potenza/Prime 50 W at 200 Ω; Genius 50 W; PRO MAX 100 W platform (some handpieces/indications limited to 65 W); and Venus 75/150 W applicators. These are FDA specifications, not measured tissue dose or unsupervised home-use ratings. [P48](https://www.accessdata.fda.gov/cdrh_docs/pdf17/K170758.pdf) · [P49](https://www.accessdata.fda.gov/cdrh_docs/pdf25/K251327.pdf) · [P50](https://www.accessdata.fda.gov/cdrh_docs/pdf24/K240248.pdf) · [P51](https://www.accessdata.fda.gov/cdrh_docs/pdf22/K221989.pdf) · [P10](https://www.accessdata.fda.gov/cdrh_docs/pdf17/K171262.pdf) · [P59](https://www.accessdata.fda.gov/cdrh_docs/pdf17/K170325.pdf) · [P61](https://www.accessdata.fda.gov/cdrh_docs/pdf25/K254185.pdf) · [P62](https://www.accessdata.fda.gov/cdrh_docs/pdf18/K180945.pdf) · [P63](https://www.accessdata.fda.gov/cdrh_docs/pdf24/K242996.pdf) · [P54](https://www.accessdata.fda.gov/cdrh_docs/pdf20/K201164.pdf) · [P55](https://www.accessdata.fda.gov/cdrh_docs/pdf23/K232192.pdf) · [P56](https://www.accessdata.fda.gov/cdrh_docs/pdf25/K252845.pdf)

NIRA’s 2 W is **optical** output; Tria is fractional laser; Ulthera and Sofwave are ultrasound. They appear in a separate “Other thermal / optical” inventory with no RF bar. See [thermal comparisons and pasted-research reconciliation](index.html#doc21), [RF versus laser](index.html#doc9), [non-fractional laser power](../06_non_fractional_lasers/power_comparison_visualizer.html), and [fractional laser research](../03_fractional_laser_resurfacing/index.html).

## Specific remaining gaps

- Same-load RF tests at 100/150/200/360/500 Ω, including on-pulse, RMS and session-average conventions.
- Exact used-device labels, manufacturing revisions and supplied attachments for Silk’n listings; the screenshots mentioned in the pasted text were not attached in this request.
- Vera/DLUS OEM contract or matching regulatory/model labels; generic units’ calibrated temperature cutoffs and the test load/duty convention for supplier claims.
- Depth-resolved thermal maps and clinical trials that would justify an efficacy comparison, rather than a wattage comparison.

## Sources and complete inventory

Every numerical record has source IDs and evidence notes in the [chart](rf_power_explorer.html), [CSV](data/rf_power_atlas_2026-10-09.csv) and [JSON ledger](data/rf_power_atlas_2026-10-09.json). [Rendered source register and intake map](index.html#doc21) · [Verbose recovery log](source_docs/research_resource_log_2026-10-09.txt). Records carried forward from the 51-row October 2 census show their older check date; unverified historic or generic leads remain unranked.
