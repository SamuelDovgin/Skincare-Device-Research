#!/usr/bin/env python3
"""Build the dated RF wattage research ledger and reader artifacts.

Run with --capture to preserve/recheck the source corpus; without it, regenerate
artifacts from the curated records and existing capture-status register.
"""
import argparse
import csv
import hashlib
import json
import re
import shutil
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
TOP = ROOT / '07_radio_frequency_skin_tightening'
DATE = '2026-10-09'
DATA = TOP / 'data'
SRC = TOP / 'source_docs' / 'power_audit_2026-10-09'
SRC.mkdir(exist_ok=True)
SOURCES = []

def source(sid, title, url, claim, kind='official product', limits='Published specification or claim; not an independent measurement of RF absorbed by skin.'):
    SOURCES.append(dict(id=sid, title=title, url=url, source_class=kind, support=claim, limits=limits))
    return sid

for sid, knum, title, claim in [
    ('P01','DEN150005','NEWA De Novo','10 W measured at 360 Ω; 8–12 W acceptance; 300/450 ms pulses per 750 ms; 42°C shutoff.'),
    ('P02','K232424','CurrentBody ST030','5 ±1 W at 200 Ω; 9 V/1.5 A supply; 40.5 ±0.5°C maximum.'),
    ('P03','K170499','sensiLift original','9 ±1 W hardware specification; selectable 3.5/5/6.5 W; validated at 200 Ω; 40°C shutoff.'),
    ('P04','K250341','sensiLift Pro ST300','6 ±1 W; selectable 3.5/5/6 W; 200 Ω validation; 40 ±0.5°C target.'),
    ('P05','K203665','TriPollar STOP U UXV','5.7 W ±10% RMS at 200 Ω; 8 V/1.5 A supply.'),
    ('P06','K230013','Silk’n Titan AllWays','10 W ±20%; 3.7 V, 2600 mAh battery; output measurement numbers not published.'),
    ('P07','K162784','Silk’n HST','RF-containing combined-energy home-use device; primary code OHS, not a separate PAY-only inventory.'),
    ('P08','K222012','FOREO FAQ 101','FDA device record; 510(k) statement does not disclose comparable RF wattage.'),
    ('P09','K240616','FOREO FAQ 102','FDA device record; 510(k) statement does not disclose comparable RF wattage.'),
    ('P10','K171262','TempSure','Professional 4 MHz platform; wrinkle mode up to 120 W; other modes up to 300 W.'),
    ('P11','K222685','NIRA Model 2','1450 ±20 nm; maximum optical power 2 W; original/model 2 fluence and pulse-train comparison.'),
    ('P12','K141868','Tria FANp','Earlier fractional laser FDA record; does not establish power for a later FRX revision.'),
    ('P13','K182774','TriPollar STOP U','STOP-family record, not all worldwide STOP models.'),
    ('P14','K220322','TriPollar STOP U UXV','Updated STOP-family indication; not a new unrelated device.'),
    ('P15','K233766','Geneo X Elite','Tabletop combined platform; distinct from handheld home models.'),
    ('P16','K242227','Geneo X Elite update','Later submission for same family; avoid double counting.'),
]:
    url = f'https://www.accessdata.fda.gov/cdrh_docs/reviews/{knum}.pdf' if knum.startswith('DEN') else f'https://www.accessdata.fda.gov/cdrh_docs/pdf{knum[1:3]}/{knum}.pdf'
    source(sid,title+' — '+knum,url,claim,'primary regulatory','FDA-submitted evidence; exact named model and intended use only. Regulatory specification is not a measured dermal dose.')

source('P17','Silk’n Titan MultiPlatform current North American IFU H2502 / HA2502','https://data.silkn.com/asset/2a5aa6ed-322e-4d0b-afbe-5fc694289137/Titan-MultiPlatform-UM-NA.pdf','15 W combined maximum; 12 V/2 A/24 W adapter; 3.7 V/4000 mAh battery; 43°C cutoff; RF/load curves.','official manual')
source('P18','Silk’n Titan Mini H2600 IFU','https://data.silkn.com/m/1b96e6d4c98d2a1a/original/Titan-Mini-UM-NA.pdf','10 W RF maximum; 3.7 V/600 mAh; up to 30 min; 5 V/2 A charger; 43°C cutoff.','official manual')
source('P19','Silk’n FaceTite MultiPlatform H2501 EU IFU','https://data.silkn.com/m/3675be4e752dbebb/original/FaceTite-MultiPlatform-UM.pdf','EU H2501 RF maximum 20 W; 4000 mAh battery; retain regional model distinction.','official manual')
source('P20','Original Silk’n Titan manufacturer IFU','https://m.media-amazon.com/images/I/91wCR6lIVGS.pdf','10 W maximum RF; H2111/H2112; 12 V/1.5 A supply.','official manual')
source('P21','Silk’n current Titan MultiPlatform product','https://www.silkn.com/skincare-devices/facial-rejuvenation-devices/titan-multiplatform-with-free-gel-SKUS000057.html?cgid=skin-care_facial-rejuvenation','Current product identity and link to current North American IFU; cordless/usable while charging.')
source('P22','FOREO FAQ 101 manual','https://www.foreo.com/manuals/faq-swiss-101','1000 mAh at 3.7 V; up to 30 minutes use per charge.','official manual')
source('P23','FOREO FAQ 102 manual','https://www.foreo.com/manuals/faq-swiss-102','1000 mAh at 3.7 V; up to 30 minutes use per charge.','official manual')
source('P24','MimiSilk Vera product','https://www.mimisilk.com/products/mimisilk-vera-rf-sculpt-6-25mhz-gel-free-radio-frequency-skin-lifting-device','6.25 MHz; claims 4.5/9/18 W settings; corded; high-setting dermal temperature claims.')
source('P25','MimiSilk Vera use guide','https://www.mimisilk.com/blogs/news/how-to-use-mimisilk-vera-rf-sculpt-full-guide-expected-results','4.5/9/18 W and 45/48/52°C marketing setting table.')
source('P26','MimiSilk professional-frequency claims','https://www.mimisilk.com/blogs/news/professional-grade-rf-frequency-at-home-how-mimisilk-vera-closes-the-gap-safely','18 W claim; 2.5–3 mm claimed penetration; faster results narrative; no cited exact-device load test.')
source('P27','DLUS D2 supplier lead in Chinese device directory','https://imeirongyi.com/vs/mid-10-temp-125-einfoids-843%2C906.html','Directory names Shenzhen Guangxiang; 6.25 MHz; 18 W supply power; April 2023 listing.','secondary directory','Lead only: not primary factory documentation and not proof of MimiSilk OEM identity. Power and corded/cordless descriptions need label confirmation.')
source('P28','DLUS D2 retailer','https://mycosmeticslondon.co.uk/products/professional-rf-facial-device-for-skin-lifting','Seller lists 18 W power consumption and rechargeable/cordless; conflicts with corded description in pasted notes.','seller listing','Source establishes what seller advertises, not a verified battery or measured RF output.')
source('P29','AMIRO R1 PRO US listing','https://amirobeauty.com/products/amiro-high-radiofrequency-skincare-device','15 W marketing value; RF test load and duty cycle not stated.')
source('P30','AMIRO submitted R3 URL (redirects to R1 PRO)','https://amirobeauty.com/products/r3-turbo-facial-rf-skin-tightening-device','Submitted R3 product URL now redirects to R1 PRO. Use P31 for the R3 15 W upgrade claim.','official product','Redirect is not an exact current R3 product specification; no RF load test or battery confirmation.')
source('P31','AMIRO upgrade comparison','https://amirobeauty.com/pages/30-day-challenge','Explicit 8 W to 15 W upgrade narrative; cannot reconcile all regional R1 specifications.')
source('P32','Sensica SensiFirm','https://sensica.com/products/sensifirm','10 ±1 W; 1 ±0.05 MHz; 41°C surface auto-stop; body product.')
source('P33','MLAY RF01','https://mlay.co/product/rf01/','1 MHz; claimed output 25 W face / 50 W body; rated input 50 W.','seller/brand listing','Multiple MLAY domains; this is an attributed listing, not independently authenticated factory identity or a load test. 50 W output and 50 W input cannot establish continuous equal power.')
source('P34','MLAY catalogue','https://www.mlayofficial.com/collections/all','RF01/RF02/S3 inventory extension; no comparable RF output verified for RF02/S3.')
source('P35','Konmison LB056B','https://www.konmison.com/product-item/3-in-1-rf-radio-frequency-facial-machine/','2 MHz bipolar; 55 W consumption; 1–15 J/cm² claimed output energy; continuous mode.')
source('P36','FREYARA Mini 3in1 RF','https://it.freyara.com/products/mini-3in1-rf-dispositivo-di-bellezza-ringiovanimento-lifting-rimozione-delle-rughe-rassodamento-della-pelle-per-viso-e-occhi','1 MHz; 20–50 W handle power claim; 24 V/3 A supply capacity.','seller listing')
source('P37','FREYARA 2in1 RF','https://it.freyara.com/products/dispositivo-di-bellezza-rf-2in1-con-3-sonde-e-6-sonde-ringiovanimento-sollevamento-rimozione-delle-rughe-rassodamento-della-pelle-per-viso-e-occhi','Related 2-probe device; separate product identity and power descriptors.','seller listing')
source('P38','FREYARA 3in1 manual FY04.0208US','https://img.freyara.com/catalog/instruction/FY04.0208US.pdf','Supplier manual; technical evidence recovery for generic 3-probe family.','supplier manual')
source('P39','MYCHWAY CET RET Face Lifting','https://us.mychway.com/product/cet-ret-rf-face-lifting-skin-care-winkle-removal','RET S/M/L/XL 130/150/200/300 W; CET S/M/L/XL 65/60/70/110 W seller claims.','seller listing','Not a comparable handheld facial load measurement; electrode size and modality must stay explicit; no exact-model U.S. clearance verified here.')
source('P40','MYCHWAY MS-11Y3 supplier manual','https://manual.mychway.com/UserManual/ms-11y3instructionnew.pdf','Generic RF machine manual; avoid equating its supply power to skin RF.','supplier manual')
source('P41','NEO Alpha / NEO Plus manufacturer','https://www.rf-skincare.com/shop/view.html?cpage_pq=182&spage_pq=181&uid=32','NEO Alpha RF controller marketing; 300 W headline in pasted research remains mode/consumption ambiguous.')
source('P42','Panasonic EH-SR90 specification','https://panasonic.jp/face/products/EH-SR90/spec.html','7 W explicitly while charging; approximately 4 days runtime under manufacturer use conditions.')
source('P43','Panasonic EH-SR85 specification','https://panasonic.jp/face/products/EH-SR85/spec.html','Charging consumption and runtime conditions; not RF output.')
source('P44','Panasonic EH-SR86 specification','https://panasonic.jp/face/products/EH-SR86/spec.html','Charging consumption and runtime conditions; not RF output.')
source('P45','YA-MAN Photo PLUS Deep Lift','https://www.ya-man-tokyo-japan.com/products/forface/photo-plus-deep-lift.html','Charging consumption and D×LIFT runtime; no RF watts disclosed.')
source('P46','Medicube AGE-R Ultra Tune40.68','https://medicube.us/products/age-r-ultra-tune-40-68','40.68 MHz RF marketing; no comparable output W confirmed.')
source('P47','EvenSkyn Lumo FAQs','https://www.evenskyn.com/pages/lumo-faqs','Existing Lumo/Lumo+ inventory; retain undisclosed output rather than inventing watts.')

PRO = [
 ('K170758','Thermage FLX'),('K251327','XERF'),('K240248','Volnewmer'),('K221989','Oligio'),
 ('K180189','InMode platform / Morpheus8 lead'),('K192695','InMode platform update / Morpheus8 lead'),
 ('K201164','Venus Viva MD'),('K232192','Venus Versa Pro'),('K252845','Venus NOVA'),
 ('K232903','Pollogen Legend X'),('K243217','Pollogen Legend X update'),
 ('K170325','Secret RF'),('K192545','Potenza'),('K254185','Potenza Prime lead'),
 ('K180945','Genius'),('K242996','EndyMed PRO MAX'),('K233996','Ulthera System / PRIME'),
 ('K243035','Ulthera update'),('K211483','Sofwave'),('K223237','Sofwave update'),
 ('K231537','Sofwave update'),('K240687','Sofwave update'),('K163137','Original NIRA'),
 ('K190678','TempSure update'),('K231910','DermRays Revive')]
for i,(k,title) in enumerate(PRO,48):
    source(f'P{i:02}',title+' — '+k,f'https://www.accessdata.fda.gov/cdrh_docs/pdf{k[1:3]}/{k}.pdf','Pasted regulatory lead rechecked against FDA document; see record notes before assigning a marketed alias.','primary regulatory','Different modes, indications and technologies. A K-number is not a patent mapping or comparative efficacy result.')

source('P73','Silk’n Titan Mini product/runtime','https://www.silkn.com/skin-tightening/titan-mini-with-free-gel-SKUS000056.html','30 minute Mini runtime; comparison panel advertises 40 minutes for MultiPlatform.')
source('P74','EndyMed US9844682B2','https://patents.google.com/patent/US9844682B2/en','Granted 2017-12-19; skin-treatment device/method; EndyMed assignee.','primary patent','Patent embodiment is not measured product performance; no legal freedom-to-operate opinion.')
source('P75','EL Global Trade US11317961B2','https://patents.google.com/patent/US11317961B2/en','Granted 2022-05-03; movable electrode skin-treatment design; assignment record includes EL Global Trade.','primary patent','Technical/family association; exact Pro model claim mapping not established.')
source('P76','Historical H2502 manufacturer IFU mirrored on device.report','https://device.report/m/91cc6032d88734ec2f9d4e9b1543aaadd7e9190fba691abbffb4ee4fcb4c0481','Older H2502/HA2502 manual names 10 W bare and 20 W combined; revision conflicts with current official IFU.','manufacturer manual mirror','Historical document, lower retrieval authority than current manufacturer-hosted IFU; do not assign 20 W to all H2502 units.')
source('P77','NEO Plus RF-300W directory','https://prod.danawa.com/info/?pcode=14102141','Directory explicitly calls 300 W consumption (소비전력).','secondary directory','Supports ambiguity check only, not measured output or exact Alpha electrical identity.')
source('P78','DLUS D3 optical device vendor lead','https://halohk.com/collections/vendors?page=13&q=halohk','Vendor describes D3 as 1064 nm optical device; D3 should not be merged into D2 RF inventory.','seller listing','Claim-only adjacent lead; no verified optical output or FDA model mapping.')

# Round 2: manufacturer manuals and exact-model disclosures recovered after the
# first atlas. A published charger/system rating remains separate from RF output.
YAMAN_MANUALS = [
 ('P79','YA-MAN Bloom 6 YJFS16PN official IFU','https://www.ya-man.co.jp/en/asset/docs/bloom-6/YJFS16PN-1-001E.pdf','Rated supply DC9V 3A; approx. 21 W device power consumption; Li-ion; approx. 30 min operation. No isolated RF watts.'),
 ('P80','YA-MAN Bloom 5 YJFS16 official IFU','https://www.ya-man.co.jp/en/asset/docs/bloom-5/YJFS16-1-001E.pdf','Rated supply DC9V 2A; approx. 18 W power consumption while charging; approx. 30 min operation. No isolated RF watts.'),
 ('P81','YA-MAN Bloom WR S12 official IFU','https://www.ya-man.co.jp/en/asset/docs/bloom-wr/S12-E.pdf','Rated supply DC5V 2A; approx. 9 W while charging; approx. 40 min operation. No RF-output watts.'),
 ('P82','YA-MAN Bloom Red S10 official IFU','https://www.ya-man.co.jp/en/asset/docs/bloom-red/S10-2-002E.pdf','Official exact-family manual recovered; RF watts and separately comparable treatment output not disclosed in extracted specification.'),
 ('P83','YA-MAN Bright Lift HRF-40 official IFU','https://www.ya-man.co.jp/en/asset/docs/bright-lift/HRF40-E.pdf','5V/1A-or-higher supply; approx. 4.5 W system consumption; Li-ion; approx. 40 min operating time. RF watts not separately stated.'),
 ('P84','YA-MAN Photo PLUS Deep Lift YJFA1 official IFU','https://www.ya-man.co.jp/en/asset/docs/photo-plus-deep-lift/YJFA1-E.pdf','5V/1A rated charging-base input; approx. 4.5 W while charging; approx. 30 min at max D×LIFT level. No RF watts.'),
 ('P85','YA-MAN Photo PLUS Shiny NEO YJFM18 official IFU','https://www.ya-man.co.jp/en/asset/docs/photo-plus-shiny-neo/YJFM18-1-001E.pdf','5V/1A charging-base input; approx. 4.5 W while charging; approx. 30 min at max DYHP power. No RF watts.'),
 ('P86','YA-MAN Photo PLUS Shiny M18 official IFU','https://www.ya-man.co.jp/en/asset/docs/photo-plus-shiny/M18-3-001E.pdf','Official model manual archived; charging/electrical ratings are not RF-output watts.'),
 ('P87','YA-MAN Photo PLUS Prestige S M20 official IFU','https://www.ya-man.co.jp/en/asset/docs/photo-plus-prestige-s/M20-6-001EA.pdf','Rated supply DC9V 2A; approx. 15 W device power consumption; Li-ion. No isolated RF watts.'),
 ('P88','YA-MAN Photo PLUS Prestige SS M21 official IFU','https://www.ya-man.co.jp/en/asset/docs/photo-plus-prestige-ss/M21-1-001E.pdf','Rated supply DC12V 3A; approx. 20 W device power consumption. No isolated RF watts.'),
 ('P89','YA-MAN Photo PLUS Prestige SP M22 official IFU','https://www.ya-man.co.jp/en/asset/docs/photo-plus-prestige-sp/M22-1-001E.pdf','Rated supply DC9V 2A; approx. 18 W device power consumption. No isolated RF watts.'),
 ('P90','YA-MAN Photo PLUS Prestige SP II YJFM24V official IFU','https://www.ya-man.co.jp/en/asset/docs/m24v/YJFM24V_1_001E.pdf','Exact-model English IFU archived; no separable RF watt specification established.'),
 ('P91','YA-MAN Photo PLUS Prestige SP III YJFM25 official IFU','https://www.ya-man.co.jp/en/asset/docs/photo-plus-prestige-sp-III/YJFM25-1-001E.pdf','Rated supply DC9V 2A; approx. 18 W device power consumption. No isolated RF watts.'),
 ('P92','YA-MAN Photo PLUS Prestige PRO M30 official IFU','https://www.ya-man.co.jp/en/asset/docs/photo-plus-prestige-pro/M30-1-001E.pdf','Rated supply DC12V 5A; approx. 20 W device power consumption. No isolated RF watts.'),
 ('P93','YA-MAN Photo PLUS EX eye pro HRF-20-EYE official IFU','https://www.ya-man.co.jp/en/asset/docs/photo-plus-ex-eye-pro/HRF20EYE-3-001E.pdf','Rated supply DC9V 2A; approx. 13 W device power consumption; Li-ion. No isolated RF watts.'),
 ('P94','YA-MAN Photo PLUS HRF-10 official IFU','https://www.ya-man.co.jp/en/asset/docs/photo-plus/HRF10-4-001EA.pdf','Exact-model official IFU archived; no verified isolated RF-output watts.'),
 ('P95','YA-MAN Photo PLUS Hyper HRF-11 official IFU','https://www.ya-man.co.jp/en/asset/docs/photo-plus-hyper/15_en.pdf','Exact-family official IFU archived; no verified isolated RF-output watts.'),
 ('P96','YA-MAN Cavi Spa RF Core PLUS HRF-51 official IFU','https://www.ya-man.co.jp/en/asset/docs/cavispa-rf-core-plus/HRF51-3-001E.pdf','Rated output DC9V 2A; approx. 5 W while charging; Li-ion. No isolated RF watts.'),
 ('P97','YA-MAN Cavi Spa RF Core HRF-17 official IFU','https://www.ya-man.co.jp/en/asset/docs/cavispa-rf-core/2_en.pdf','Exact-family official IFU archived; no verified isolated RF-output watts.'),
 ('P98','YA-MAN Photo PLUS EX Smooth S HRF-20L-2 Japanese IFU','https://www.ya-man.co.jp/wp/wp-content/uploads/manuals/pdf/HRF20L2.pdf','Exact legacy-model Japanese IFU; retained for model identification, not used to assign watts without a verified read-off.','official manual (Japanese)'),
 ('P99','YA-MAN Photo PLUS Smart HRF-11-SE Japanese IFU','https://www.ya-man.co.jp/wp/wp-content/uploads/manuals/pdf/HRF-11-SE.pdf','Exact legacy-model Japanese IFU; retained for model identification, not used to assign watts without a verified read-off.','official manual (Japanese)'),
 ('P100','YA-MAN Cavi Spa RF Core EX HRF-18 Japanese IFU','https://www.ya-man.co.jp/wp/wp-content/uploads/manuals/pdf/HRF-18.pdf','Exact legacy-model Japanese IFU; retained for model identification, not used to assign watts without a verified read-off.','official manual (Japanese)'),
]
for item in YAMAN_MANUALS:
    sid,title,url,claim,*kind = item
    source(sid,title,url,claim,kind[0] if kind else 'official manual','Manual power/charger figures describe whole-device electrical use; they are not isolated RF output or a measured dermal dose.')

source('P101','AMIRO S2 Seal Max official manual','https://cdn.shopify.com/s/files/1/0053/8866/4950/files/S2_Seal-Max.pdf?v=1695808061','Model S2 manual: 5V×3A / 15W adapter specification, 1500mAh battery, 1–2.6MHz RF; no comparable RF watts.','official manual','15W is a charging-adapter rating, not treatment RF output; cell voltage and operating runtime are not stated in the manual excerpt.')
source('P102','AMIRO R1 Pro official manual','https://cdn.shopify.com/s/files/1/0053/8866/4950/files/AMIRO_R1_Pro_Facial_RF_Skin_Tightening_Device_cc6c678a-c5de-4303-a2c8-a5fdfbdcf314.pdf?v=1679051689','Manual rates input 5V×2A and battery capacity 2600mAh; does not state a comparable RF watt output or battery cell voltage.','official manual','USB charging supply capacity is not RF output; retail 15W headline remains a marketing claim.')
source('P103','AMIRO S1 official manual','https://cdn.shopify.com/s/files/1/0053/8866/4950/files/S1_Facial_Device_User_Manual.pdf?v=1679041661','Manual rates input 5V×3A, 1200mAh battery, about 90-minute charge; no comparable RF watts.','official manual','Charging input and capacity do not disclose RF output; battery cell voltage/runtime are not stated in the technical line.')
source('P104','FOREO FAQ 103 Diamond official manual','https://assets.foreo.com/files/static/manuals/2021-05/FAQ_103_manual_english_0.pdf?VersionId=JMzeFe3bj2gj6KF55YvdnVR9R8HfcvrO','Li-ion 3.7V/1000mAh; up to 30 min per charge; RF output watts not disclosed.','official manual','Nominal whole-device energy is 3.7Wh; 7.4W average at the stated runtime is not an RF rating.')
source('P105','TriPollar STOP VX2 official manual','https://cdn.shopify.com/s/files/1/0276/3089/5193/files/STOP_VX2.pdf?v=1691504919','Manual states 5.7W at 200Ω and includes output-power/load graph; plotted point appears about 6.6W at 200Ω. 8V×1.5A adapter; 1MHz.','official manual','The manual specification and its own graph conflict near 200Ω; digitized graph points are approximate, starred read-offs, not independent measurements.')
source('P106','TriPollar STOP VX GOLD 2 official manual','https://cdn.shopify.com/s/files/1/0266/4782/2418/files/TriPollar_STOP_Vx_GOLD_2_6d2cdfe1-3869-44be-9569-0e4bdcde6bc5.pdf?v=1677751224','Rated 5V max 2A; RF frequency 1.0–1.25MHz; no comparable RF output watts.','official manual','10W is the maximum supply rating, not RF output.')
source('P107','TriPollar ENVIG EDGE official manual','https://cdn.shopify.com/s/files/1/0266/4782/2418/files/TRIPOLLAR-ENVIG_EDGE.pdf?v=1688564333','5V max 2A; approx. 30 min continuous use per full charge; RF output watts and battery capacity not disclosed.','official manual','10W USB adapter ceiling is not a treatment-output rating; runtime alone cannot identify RF watts.')
source('P108','Panasonic VITALIFT RF EH-SR85 official manual','https://panasonic.jp/content/dam/panasonic/jp/ja/pim-assets/support/manual/000/000/000/377/553/000000000377553/eh-sr85.pdf','Official manual archived; product specification separately says approx. 7W while charging; RF output watts not disclosed.','official manual','Charging consumption, battery runtime and RF treatment watts are different quantities.')
source('P109','Panasonic VITALIFT RF EX EH-SR86 official manual','https://panasonic.jp/content/dam/panasonic/jp/ja/pim-assets/support/manual/000/000/002/714/737/000000002714737/p_eh-sr86_01.pdf','Official manual archived; product specification separately says approx. 7W while charging; RF output watts not disclosed.','official manual','Charging consumption, battery runtime and RF treatment watts are different quantities.')
source('P110','MLAY RF01 official current product page','https://www.mlayofficial.com/products/mlay-rf01?country=DZ&currency=USD&variant=45451682021684','Current page claims 25W face / 50W body, 50W rated input, 1MHz.','official product claim','No stated test load, duty cycle or independent output measurement; output/input equality at body setting should not be assumed continuous.')
source('P111','MLAY S3 official current product page','https://www.mlayofficial.com/products/mlay-rf-beauty-instrument-s3','Current page claims 25W face / 14W body, 1MHz, 100–240VAC; no current rating, load or duty convention.','official product claim','Output claims are not accompanied by a test load or independent measurement; flagged low confidence.')
source('P112','MLAY RF02 official current product page','https://www.mlayofficial.com/products/mlay-rf-instrument-rf02','Current S02B/RF02 page states 36W rated input, 1MHz; does not state isolated RF output.','official product claim','Rated whole-device input is not RF output; keep separate from similarly named brochure variants.')
source('P113','MLAY supplier brochure indexed by Messe Frankfurt','https://exhibitorsearch.messefrankfurt.com/images/original/document_downloads/10000391202501/397636/1739246184332_3510192324.pdf','Indexed brochure lists RF01/S05 48W, S03 12W with 3.7V/2000mAh, RF02/S06 38W, and S04 13W with 7.4V/650mAh; 1MHz.','manufacturer brochure (indexed copy)','Host URL returned 404 during this pass; values are dated brochure claims without test load/duty or a confirmed identity match to current retail models. Local excerpt records exactly what was recovered.')
source('P114','MYCHWAY MS-76F1SBMAX supplier manual','https://manual.mychway.com/UserManual/ms-76f1sbmax-en-20250327.pdf','Manual lists 80W system input; Face RF 70W, Eye RF 40W and Body RF 80W at 1MHz.','supplier manual','Supplier manual output ratings are unverified claims; body RF equals the stated system input, and load/duty convention is absent. Flag all RF values low confidence.')
source('P115','FDA K250308 hair-growth comb record (clearance-attribution check)','https://www.accessdata.fda.gov/cdrh_docs/pdf25/K250308.pdf','FDA record identifies Dongguan Boyuan hair-growth device models; it does not identify MLAY S3.','primary regulatory','Used to check a retailer attribution only; not evidence that MLAY S3 is cleared under K250308.')

# Dated eBay scan. These are market snapshots, not technical evidence; the
# local notes preserve the observed listing metadata without mirroring pages.
source('P116','eBay US search: 5 in 1 RF facial machine (2026-10-09)','https://www.ebay.com/sch/i.html?_nkw=5+in+1+RF+facial+machine&_sop=12','Signed-out eBay search showed 53 results for this query. The page mixed inexpensive handheld multi-function listings with unrelated salon equipment; examples included near-identical generic 5-in-1 RF/LED devices.','marketplace search snapshot','Result count and listings are volatile, location-dependent and not an exact-model census; price and listing claims do not establish RF output, thermal control or safety.')
source('P117','eBay indexed Toe Talk DMR-2121 search cards (2026 snapshot)','https://www.ebay.com/shop/5-in-1-facial-machine?_nkw=5+in+1+facial+machine','An indexed eBay card for Toe Talk DMR-2121 showed $89.99 and 415 sold; another seller card showed $44.95. A separately opened Toe Talk item uses model DR-04, so those identifiers are not merged.','marketplace search snapshot','The 415 figure is one indexed seller/listing counter from an older crawl, not current live inventory or total model sales; no manufacturer RF watt or test-load report was found.')
source('P118','eBay Toe Talk DR-04 5-in-1 RF/EMS listing','https://www.ebay.com/itm/167388282080','Listing item specifics call the model DR-04 and RF/EMS; the captured page showed $35, 5 available and 1 sold, with a last-updated date of 2025-09-26.','marketplace listing snapshot','Stale/volatile seller page; its identifier conflicts with DMR-2121 search cards. It gives no RF watts, test load, duty cycle or thermal cutoff.')
source('P119','eBay Silk’n FaceTite H2111/H2112 ended listing','https://www.ebay.com/itm/287135673661','Used listing identified FaceTite H2111/H2112, a 12 V supply field, and a GBP 72.86 ask before the seller ended it on 2026-07-03 because of a listing error.','marketplace listing snapshot','Ended listing was not marked sold. Same H numbers occur in a Silk’n Titan IFU, but regional naming/revision identity is not established; do not automatically transfer its 10 W claim.')
source('P120','eBay NEWA Lift Pink corded used listing','https://www.ebay.com/itm/377242951684','Used NEWA Lift Pink listing at $149 plus $22 shipping; page showed 3 sold and last one available, last updated 2026-09-27.','marketplace listing snapshot','Seller listing does not show a verified model/revision link to the FDA DEN150005 wired 3DEEP device; its 10 W/360 Ω result must not be assigned until the unit label/manual is matched.')
source('P121','eBay TriPollar STOP X search / used listings','https://www.ebay.com/shop/tripollar-stop-x?_nkw=tripollar+stop+x','Search page showed 9 results; used STOP X listings included asks around $175-$239, with one listing explicitly named STOP X Model U.','marketplace search snapshot','Prices, listing count and regional variants change. Confirm exact model/region, condition, return rights and included adapter; a marketplace listing is not a performance test.')
source('P122','eBay sold TriPollar STOP VX listing','https://www.ebay.com/itm/147459239957','STOP VX device-only/no-gel listing recorded as sold for $250 on 2026-07-25.','marketplace sold listing snapshot','STOP VX is not STOP X, STOP VX2 or STOP VX Gold 2; the price must not be joined to another revision’s wattage or manual.')
source('P123','eBay IFAE A083 6-in-1 home RF listing','https://www.ebay.com/itm/358278680145','Seller-identified IFAE A083 6-in-1 home RF device listing ended 2026-08-02 at an ask of $78; seller condition said open/used item, damaged box, like new.','marketplace listing snapshot','Ended listing is not evidence of a completed sale or current price; no exact-model IFU, RF wattage, test load or temperature-control documentation recovered.')
source('P124','eBay unbranded SC114 dot-matrix RF listing','https://www.ebay.com/itm/307199923652','Ended listing described an unbranded rechargeable SC114 dot-matrix RF facial device; auction ended 2026-10-02 at $69.99 with zero bids and $99 Buy It Now shown.','marketplace listing snapshot','Seller data also listed 220 V and rechargeable battery, a conflict needing label verification. No RF output, load, duty cycle or thermal cutoff documented; not a recommendation.')
source('P125','Pollogen official STOP X regional-model FAQ','https://pollogen.com/faq/','Official FAQ maps the U.S. STOP X to model STOP U; EU/APAC STOP X has two RF levels. Use the FDA STOP U record only for a verified U.S. Model U unit.','official manufacturer FAQ','Regional model mapping does not establish that every eBay STOP X is the U.S. revision, nor does the FDA specification establish clinical superiority or tissue dose.')
source('P126','Aura Self Beauty SC114 reseller specification','https://auraselfbeauty.com/products/rf-skin-tightening-device?variant=45254990823503','Reseller page displayed $89.99 and identifies model SC114; it states rated power 5 W, 1 MHz, 9 V/500 mA supply, 144 dot-matrix electrodes and a 15-minute auto-off timer. It also says rechargeable and roughly 3–4 hours of use per charge.','reseller product specification','Not a manufacturer IFU or an independent test. The 5 W field is ambiguous (not identified as isolated RF output) and the stated adapter capacity is 4.5 W; catalog claims may be copied across sellers. A timer is not a measured temperature cutoff; price is a dated retailer ask.')
source('P127','Ahood / Vilnason SC114 reseller specification','https://ahoodstore.com/collections/frontpage/products/radio-frequency-facial-lifting-machine','Reseller listing displayed €45.07 and identifies Vilnason / model SC114; it repeats 5 W, 1 MHz, 9 V/500 mA supply, rechargeable, 144 dot-matrix electrodes and 15-minute auto-off claims. It says an instruction manual is included but does not provide a downloadable manual.','reseller product specification','Same apparent OEM product-copy family as P126, not independent confirmation. No isolated RF output, test load, duty convention or measured thermal control; 5 W wording is not proof of 5 W RF. Price is a dated regional retailer ask.')

def capture(s):
    import requests
    ext = '.pdf' if '.pdf' in s['url'].lower() else '.html'
    dest=SRC/(s['id']+ext)
    try:
        r=requests.get(s['url'],timeout=35,headers={'User-Agent':'Mozilla/5.0'})
        ok=r.status_code==200 and (r.content.startswith(b'%PDF') if ext=='.pdf' else len(r.content)>500)
        if ok:
            dest.write_bytes(r.content)
            return dict(id=s['id'],status=f'HTTP {r.status_code}',resolved_url=r.url,local=str(dest.relative_to(TOP)),sha256=hashlib.sha256(r.content).hexdigest())
        return dict(id=s['id'],status=f'HTTP {r.status_code}; capture unavailable',resolved_url=r.url,local=None)
    except Exception as e:
        return dict(id=s['id'],status=type(e).__name__+': '+str(e)[:160],local=None)

def preserve_ebay_snapshot():
    """Preserve observed marketplace metadata without mirroring eBay pages."""
    note=SRC/'ebay_marketplace_snapshot_2026-10-09.txt'
    if not note.exists():
        note.write_text('''eBay marketplace observations — 2026-10-09 (America/Chicago)

These are a dated, signed-out browser snapshot and indexed search-card observations, not an exhaustive or persistent inventory. Prices and counters can vary by location, seller, account state, and time. Listing claims are not technical verification. The eBay HTML pages are not mirrored; this note preserves only the observations used in the RF atlas.

P116 — Search query “5 in 1 RF facial machine”: 53 results. The results mixed handheld RF/LED multifunction listings with unrelated salon equipment; near-identical generic units appeared at low prices. Search URL: https://www.ebay.com/sch/i.html?_nkw=5+in+1+RF+facial+machine&_sop=12

P117 — Indexed Toe Talk DMR-2121 search cards showed one listing at $89.99 with 415 sold and another seller card at $44.95. This 415 counter was from an older indexed crawl, not a live total. Search URL: https://www.ebay.com/shop/5-in-1-facial-machine?_nkw=5+in+1+facial+machine

P118 — Toe Talk DR-04 item 167388282080 showed $35, five available and one sold; the page identified RF/EMS and model DR-04, and listed 2025-09-26 as its last update. This identifier is kept separate from DMR-2121. Item: https://www.ebay.com/itm/167388282080

P119 — Used Silk’n FaceTite listing identified H2111/H2112 and a 12 V field, with a GBP 72.86 ask. Seller ended it on 2026-07-03 for a listing error; it was not marked sold. Item: https://www.ebay.com/itm/287135673661

P120 — Used corded NEWA Lift Pink listing asked $149 plus $22 shipping and showed three sold / last one available; last updated 2026-09-27. The listing did not provide a verified revision/label link to the FDA DEN150005 original wired 3DEEP device. Item: https://www.ebay.com/itm/377242951684

P121 — TriPollar STOP X search showed nine results and used asks around $175–$239; one listing explicitly said STOP X Model U. Market page: https://www.ebay.com/shop/tripollar-stop-x?_nkw=tripollar+stop+x

P122 — A distinct TriPollar STOP VX device-only/no-gel listing recorded a $250 sale on 2026-07-25. Do not merge it with STOP X, STOP VX2, or STOP VX Gold 2. Item: https://www.ebay.com/itm/147459239957

P123 — Seller-identified IFAE A083 6-in-1 home RF listing ended 2026-08-02 with a $78 ask, described as open/used with damaged box; not confirmed sold. Item: https://www.ebay.com/itm/358278680145

P124 — Unbranded SC114 dot-matrix rechargeable RF listing ended 2026-10-02 at $69.99 with zero bids and a $99 Buy It Now shown. Seller fields conflicted between 220 V and rechargeable battery. Item: https://www.ebay.com/itm/307199923652

No RF wattage, test load, duty cycle, measured tissue temperature, or verified thermal cutoff was recovered from these marketplace pages. The output rankings in the rendered tier page therefore use linked FDA/manual evidence only when a specific model mapping is defensible; the generic devices remain unranked for predictable heating.
''',encoding='utf-8')
    return note

def write_corpus(do_capture):
    status_file=DATA/f'rf_power_capture_status_{DATE}.json'
    statuses=json.loads(status_file.read_text()) if status_file.exists() else []
    by={s['id']:s for s in statuses}
    market_note=preserve_ebay_snapshot()
    for s in SOURCES:
        if s['id'] in {f'P{x}' for x in range(116,125)}:
            by[s['id']]=dict(id=s['id'],status='Dated browser-observation summary; eBay HTML intentionally not mirrored',
                resolved_url=s['url'],local=str(market_note.relative_to(TOP)),
                sha256=hashlib.sha256(market_note.read_bytes()).hexdigest())
    if do_capture:
        pending=[s for s in SOURCES if not (by.get(s['id'],{}).get('local') and (TOP/by[s['id']]['local']).is_file())]
        with ThreadPoolExecutor(max_workers=8) as pool:
            statuses.extend(pool.map(capture,pending))
        by={s['id']:s for s in statuses}
    # The Messe Frankfurt document host now returns 404. Preserve the exact
    # indexed brochure claims as a short, clearly labeled excerpt rather than
    # pretending the unavailable PDF was downloaded.
    if any(s['id']=='P113' for s in SOURCES):
        excerpt=SRC/'P113_indexed_excerpt.txt'
        excerpt.write_text('''MLAY brochure excerpt preserved from Messe Frankfurt indexed document text\n\nOriginal document URL (returned HTTP 404 when checked 2026-10-09):\nhttps://exhibitorsearch.messefrankfurt.com/images/original/document_downloads/10000391202501/397636/1739246184332_3510192324.pdf\n\nClaims recovered from the indexed brochure entry:\n- RF01 / S05: 48 W output; non-battery; 1 MHz.\n- S03: 12 W; 3.7 V, 2000 mAh; 1 MHz.\n- RF02 / S06: 38 W; non-battery; 1 MHz.\n- S04: 13 W; 7.4 V, 650 mAh; 1 MHz.\n\nThese are brochure claims, not independent measurements. Test load, duty convention, exact version, and identity relationship to current retail MLAY models were not established. The source PDF could not be locally preserved because its host returned 404; this excerpt preserves only the indexed statements used in the atlas.\n''',encoding='utf-8')
        by['P113']=dict(id='P113',status='Indexed brochure text excerpt; source PDF host returned 404',resolved_url=next(s['url'] for s in SOURCES if s['id']=='P113'),local=str(excerpt.relative_to(TOP)),sha256=hashlib.sha256(excerpt.read_bytes()).hexdigest())
        statuses=[by.get(s['id'],dict(id=s['id'],status='URL checked via browser/search; local capture pending',local=None)) for s in SOURCES]
    status_file.write_text(json.dumps(statuses,ensure_ascii=False,indent=2)+'\n')
    for s in SOURCES:s.update(by.get(s['id'],dict(status='URL checked via browser/search; local capture pending',local=None)))
    (DATA/f'rf_power_sources_{DATE}.json').write_text(json.dumps(SOURCES,ensure_ascii=False,indent=2)+'\n')
    return SOURCES

ROWS=[]
def device(brand,model,sids,category='Home face RF',rf=None,treatment=None,measured=None,load=None,
           basis='Unknown',input_w=None,input_kind='Undisclosed',v=None,mah=None,runtime=None,
           freq='Undisclosed',temperature='Undisclosed',clearance='Not verified for this exact model',notes='',rf_label=None,
           curve_data=None,curve_label=None,confidence=None):
    ids=sids.split()
    lookup={s['id']:s for s in SOURCES}
    if confidence is None and any(term in basis.lower() for term in ('claim','marketing','pasted lead','ambiguous')):
        confidence='low'
    label=rf_label or (f'{rf:g} W' if rf is not None else 'Not disclosed / not verified')
    if confidence=='low' and rf is not None and not label.endswith('*'):
        label += '*'
    ROWS.append(dict(id=f'D{len(ROWS)+1:03}',brand=brand,model=model,category=category,
        rf_max_w=rf,treatment_max_w=treatment,measured_w=measured,load_ohm=load,basis=basis,
        rf_label=label,confidence=confidence,curve_data=curve_data,curve_label=curve_label,
        input_w=input_w,input_kind=input_kind,battery_v=v,battery_mah=mah,runtime_min=runtime,
        battery_wh=round(v*mah/1000,3) if v is not None and mah is not None else None,
        average_total_w=round(v*mah/1000/(runtime/60),3) if None not in (v,mah,runtime) else None,
        frequency=freq,temperature=temperature,clearance=clearance,notes=notes,source_ids=ids,
        product_url=next((lookup[x]['url'] for x in ids if x in lookup),None),
        checked=DATE))

def build_rows():
    ROWS.clear()
    device('NEWA','Original wired 3DEEP','P01 P74',rf=10,measured=10,load=360,basis='Numeric FDA bench result',freq='1 MHz',temperature='42°C sensor shutoff',clearance='DEN150005',notes='10 W bench result is explicit. Pulse duration 300/450 ms in 750 ms cycles. 4/6 W duty-average scenarios require 10 W to mean on-pulse power; document does not settle its averaging convention.',rf_label='10 W ±20%')
    device('CurrentBody','Skin RF ST030 (US)','P02',rf=5,treatment=5,load=200,basis='FDA specification',input_w=13.5,input_kind='9 V × 1.5 A external supply capacity',freq='1 MHz',temperature='40.5 ±0.5°C maximum',clearance='K232424',notes='Power validation passed; exact measured number not published.',rf_label='5 W ±1')
    device('Sensica','sensiLift original','P03 P75',rf=9,treatment=6.5,load=200,basis='FDA specification',input_w=13.5,input_kind='9 V × 1.5 A external supply (comparison in Pro filing)',freq='1 MHz',temperature='40°C shutoff',clearance='K170499',notes='9 W hardware maximum differs from 3.5/5/6.5 W selectable skin-level settings. Validation passed, no numeric measured output published.',rf_label='9 W ±1 hardware; 6.5 W highest setting')
    device('Sensica','sensiLift Pro ST300','P04 P75',rf=6,treatment=6,load=200,basis='FDA specification',input_w=21.6,input_kind='12 V × 1.8 A external supply capacity',freq='1 ±0.05 MHz',temperature='40 ±0.5°C maximum',clearance='K250341',notes='Selectable 3.5/5/6 W; validation passed; numeric measured results not disclosed.',rf_label='6 W ±1')
    device('Sensica','SensiFirm body','P32',category='Home body RF',rf=10,basis='Manufacturer specification',freq='1 ±0.05 MHz',temperature='41°C auto-stop (brand)',notes='Body/cellulite product; do not substitute its area or protocol for facial use.',rf_label='10 W ±1')
    for model,sid,k in [('STOP U','P13','K182774'),('STOP U UXV','P05 P14','K203665 / K220322')]:
        device('TriPollar',model,sid,rf=5.7,treatment=5.7,load=200,basis='FDA specification',input_w=12 if 'UXV' in model else None,input_kind='8 V × 1.5 A external supply capacity',freq='1 MHz',temperature='Temperature-controlled; exact numeric cutoff not confirmed here',clearance=k,notes='Maximum RMS RF specification, not a numerical measurement report.',rf_label='5.7 W ±10% RMS')
    device('Silk’n','HST / legacy Titan clearance family','P07',rf=10,basis='FDA specification',freq='1 MHz',clearance='K162784 (OHS primary)',notes='Combined RF/optical system; exact retail alias must be matched to its label.')
    device('Silk’n','Titan original H2111/H2112','P20',rf=10,basis='Manufacturer manual',input_w=18,input_kind='12 V × 1.5 A supply capacity',freq='1 MHz',notes='Corded. Shared model numbers in FaceTite manuals do not prove identical regional output. IFU graph read-offs are approximate, not a new measurement.',clearance='See HST family; retail label match required',curve_data=[{'load_ohm':50,'rf_w':8.5},{'load_ohm':100,'rf_w':9.4},{'load_ohm':150,'rf_w':8.7},{'load_ohm':200,'rf_w':6.8}],curve_label='Original IFU plotted markers; approximate read-offs*')
    device('Silk’n','Titan AllWays','P06',rf=10,basis='FDA specification',v=3.7,mah=2600,freq='1 MHz',clearance='K230013',notes='9.62 Wh nominal battery. Pasted 20-minute runtime has not been confirmed in this FDA record; no battery-average output inferred.',rf_label='10 W ±20%')
    device('Silk’n','Titan MultiPlatform H2502 + HA2502 (current NA IFU)','P17 P21 P73',rf=15,basis='Manufacturer manual',input_w=24,input_kind='12 V × 2 A supply capacity',v=3.7,mah=4000,runtime=40,freq='1 MHz ±30%',temperature='43°C surface cutoff',notes='Current official IFU says 15 W combined. Historical 20 W IFU is separate below. 40-minute website runtime is not a specified full-power load test. Curve points below are visual read-offs from the IFU plot, not bench data.',curve_data=[{'load_ohm':63,'rf_w':14.5},{'load_ohm':80,'rf_w':11.3},{'load_ohm':100,'rf_w':9.3},{'load_ohm':150,'rf_w':7.5}],curve_label='Current NA IFU plot; approximate read-offs*')
    device('Silk’n','Titan MultiPlatform H2502 + HA2502 (historical IFU)','P76 P17',rf=20,basis='Historical manual conflict',input_w=24,input_kind='12 V × 2 A supply capacity',freq='1 MHz ±30%',temperature='43°C surface cutoff',notes='Historical manufacturer manual mirrored by device.report. Current official NA manual is 15 W. Same name/model cannot identify revision; not an extra unique device.')
    device('Silk’n','Titan MultiPlatform H2502 bare head (historical)','P76',rf=10,basis='Historical manual conflict',input_w=24,input_kind='Supply capacity',freq='1 MHz ±30%',notes='Older manual explicitly distinguishes bare 10 W head from 20 W combined configuration. Current manual only lists combined 15 W; do not transfer bare rating across revisions.')
    device('Silk’n','FaceTite MultiPlatform H2501 EU','P19',rf=20,basis='Manufacturer manual',input_w=24,input_kind='12 V × 2 A adapter capacity',mah=4000,freq='1 MHz ±30%',notes='Battery mAh disclosed, cell nominal voltage not established from this IFU. Device 12 V rating must not be used as battery voltage.')
    device('Silk’n','Titan Mini H2600','P18 P73',rf=10,basis='Manufacturer manual',input_w=10,input_kind='5 V × 2 A charging supply capacity',v=3.7,mah=600,runtime=30,freq='1 MHz ±30%',temperature='43°C surface cutoff',notes='2.22 Wh / 0.5 h = 4.44 W nominal total-draw estimate. Stated runtime is not a continuous 10 W test. Curve points below are visual read-offs from the IFU plot, not bench data.',curve_data=[{'load_ohm':150,'rf_w':7.6},{'load_ohm':175,'rf_w':6.3},{'load_ohm':200,'rf_w':2.6},{'load_ohm':225,'rf_w':2.3},{'load_ohm':250,'rf_w':2.0}],curve_label='H2600 IFU plot; approximate read-offs*')
    for model,claim in [('Silhouette (legacy body)','24 W'),('FaceTite Mini FAC01 (legacy EU)','13 W'),('Original FaceTite H2111/H2112 (regional)','12 W'),('FaceTite Z / Revive / Essential / Prestige H2120/H2130','10 W'),('FaceTite Mini H2600 regional alias','10 W')]:
        device('Silk’n',model,'U01',category='Home body RF' if 'Silhouette' in model else 'Home face RF',basis='Pasted lead only',notes=f'Pasted claim: {claim}. Exact manufacturer IFU/revision not independently recovered in this pass; excluded from numerical ranking. H2600 alias may duplicate Titan Mini.')
        if model=='Original FaceTite H2111/H2112 (regional)':
            ROWS[-1].update(source_ids=['U01','P119','P20'],checked=DATE,
                notes='Pasted lead says 12 W. The used eBay listing identifies H2111/H2112 and a 12 V supply field but no RF output. A Silk’n Titan IFU uses the same H numbers and says 10 W; matching regional FaceTite/Titan revisions has not been established. Do not transfer either number until the unit label and exact IFU are matched; the eBay listing ended and was not marked sold.')
    for model,sid,k in [('FAQ 101','P22 P08','K222012'),('FAQ 102','P23 P09','K240616')]:
        device('FOREO',model,sid,v=3.7,mah=1000,runtime=30,basis='RF undisclosed; battery data',clearance=k,notes='3.7 Wh and up to 30 min give 7.4 W nominal whole-device average under the matching runtime condition. RF, EMS, LED and electronics share energy.')
    device('FOREO','FAQ 103 Diamond','P104',v=3.7,mah=1000,runtime=30,basis='RF undisclosed; battery data',notes='Official manual: 3.7V/1000mAh and up to 30 min per charge, giving 3.7Wh and a nominal 7.4W whole-device average under that stated runtime. RF, EMS, LED and electronics share the budget; no RF watts disclosed.')
    device('MimiSilk','Vera RF Sculpt','P24 P25 P26 P27 P28',rf=18,basis='Marketing RF claim',freq='6.25 MHz claimed',temperature='49–50°C FAQ vs 52°C guide claimed dermal values; no measured thermal map',notes='Brand calls 18 W output; similar DLUS listing says 18 W supply/consumption. OEM connection unconfirmed. Corded Vera, no battery estimate.',rf_label='4.5 / 9 / 18 W claimed')
    device('DLUS','D2','P28 P27',category='Generic handheld RF',input_w=18,input_kind='Seller consumption / directory supply power',basis='Seller input; RF unknown',freq='6.25 MHz claimed',notes='Directory names Shenzhen Guangxiang. Retailer says rechargeable/cordless; pasted notes say mains. No battery voltage/capacity/runtime verified. Factory relationship to Vera is a lead.')
    device('AMIRO','R1 PRO (US listing)','P29 P31 P102',rf=15,basis='Marketing RF claim',input_w=10,input_kind='5 V × 2 A manual-rated USB input; RF not separately rated',mah=2600,freq='Undisclosed in manual',notes='Retail page advertises 15W, but the exact official manual lists 5V×2A and 2600mAh without an RF watt or cell voltage. Regional/version ambiguity and 8W→15W predecessor claim remain; treat 15W as low-confidence marketing, not measured output.',rf_label='15 W claim; 8 W predecessor discrepancy*')
    device('AMIRO','R3 Turbo','P30 P31',rf=15,basis='Marketing RF claim',notes='Explicit 8 to 15 W upgrade claim. No same-model official manual recovered; battery cell voltage/runtime unknown.',rf_label='15 W upgrade claim*')
    device('AMIRO','S2 Seal Max','P101',category='Home face RF',input_w=15,input_kind='5 V × 3 A charging-adapter rating (manual)',mah=1500,freq='1 / 1.5 / 2 / 2.6 MHz',notes='Exact S2 Seal Max manual lists 1500mAh and a 15W maximum adapter while charging, but no cell voltage/runtime or RF watt output. Adapter capacity is not treatment output.')
    device('AMIRO','S2 Seal (non-Max; exact revision unresolved)','L01',basis='Prior inventory; RF unknown',notes='The recovered S2 Seal Max manual does not establish the non-Max unit’s output or internal battery specifications.')
    device('AMIRO','S1 Facial RF stamping device','P103',category='Home face RF',input_w=15,input_kind='5 V × 3 A manual-rated charging input',mah=1200,notes='Official manual lists 5V×3A input, 1200mAh battery and approx. 90-minute charge; cell voltage/runtime and isolated RF watts are not stated.')
    device('MLAY','RF01 face probe (current official listing)','P110 P33',category='Generic tabletop RF',rf=25,basis='Manufacturer output claim',input_w=50,input_kind='Rated total input (listing)',freq='1 MHz',temperature='Temperature adjustment claimed; calibrated numerical cutoff unverified',notes='Official page claims 25W face output and 50W total input. No test load/duty convention; not independently measured.',rf_label='25 W face claim*')
    device('MLAY','RF01 body probe (current official listing)','P110 P33',category='Generic tabletop RF',rf=50,basis='Manufacturer output claim',input_w=50,input_kind='Rated total input (listing)',freq='1 MHz',notes='Official page claims 50W RF body output against 50W total input. Do not assume equal continuous RF and input; peak/control convention and load are absent.',rf_label='50 W body claim*')
    device('MLAY','S3 handheld · face output claim','P111',category='Generic handheld RF',rf=25,basis='Manufacturer output claim',freq='1 MHz',notes='Current official page claims 25W face and 14W body output, 100–240VAC and 50/60Hz. It gives no current, test load or duty convention; not independently measured.',rf_label='25 W face claim*')
    device('MLAY','S3 handheld · body output claim','P111',category='Generic handheld RF',rf=14,basis='Manufacturer output claim',freq='1 MHz',notes='Same S3 body with separate body setting. Manufacturer claim lacks load/duty convention; do not compare as a measured facial output.',rf_label='14 W body claim*')
    device('MLAY','RF02 desktop S02B (current official listing)','P112 P34',category='Generic tabletop RF',input_w=36,input_kind='36 W rated whole-device input (manufacturer page)',freq='1 MHz',basis='Manufacturer rated input; RF unknown',notes='Official listing states 36W rated input and 1MHz, but no isolated RF watt output. Keep separate from the S06 brochure’s differently identified “RF02 Home Use” 38W claim.')
    device('MLAY','RF01 Home Use · S05 brochure variant','P113',category='Generic tabletop RF',rf=48,basis='Manufacturer brochure output claim',freq='1 MHz',notes='Indexed MLAY brochure says 48W output and non-battery. Model/version relationship to current RF01 (25W face / 50W body, 50W input) is unresolved; no test load or duty convention.',rf_label='48 W brochure claim*')
    device('MLAY','S03 Home Use RF device · brochure variant','P113',category='Generic handheld RF',rf=12,v=3.7,mah=2000,freq='1 MHz',basis='Manufacturer brochure output claim',notes='Indexed brochure claim: 12W output, 3.7V/2000mAh battery, 1MHz. Runtime/load/duty and model relationship to current MLAY products are unresolved.',rf_label='12 W brochure claim*')
    device('MLAY','RF02 Home Use · S06 brochure variant','P113',category='Generic tabletop RF',rf=38,freq='1 MHz',basis='Manufacturer brochure output claim',notes='Indexed brochure claims 38W output and no battery. It is not proven to be the same S02B sold as current RF02; current S02B page instead states 36W rated input. Keep separate; neither supplies a load/duty convention.',rf_label='38 W brochure claim*')
    device('MLAY','S04 Home Use RF device · brochure variant','P113',category='Generic handheld RF',rf=13,v=7.4,mah=650,freq='1 MHz',basis='Manufacturer brochure output claim',notes='Indexed brochure claim: 13W output, 7.4V/650mAh battery (4.81Wh nominal), 1MHz. Runtime/load/duty and exact model relationship are unresolved; no watt average inferred.',rf_label='13 W brochure claim*')
    device('Konmison','LB056B three-probe tabletop','P35',category='Generic tabletop RF',input_w=55,input_kind='Power consumption',freq='2 MHz bipolar',basis='Supplier input; RF unknown',temperature='Numeric skin cutoff unverified',notes='1–15 J/cm² seller energy claim cannot be converted to watts without time and electrode area. Listing also says IPL+RF; exact optical hardware unspecified.')
    device('FREYARA','Mini 3in1 RF / FY04.0208US family','P36 P38',category='Generic tabletop RF',rf=50,basis='Seller handle-power claim',input_w=72,input_kind='24 V × 3 A supply capacity',freq='1 MHz intended by listing (printed mHz)',notes='20–50 W handle claim, no load/duty convention. Appearance does not prove same factory/electronics as Konmison.',rf_label='20–50 W handle claim')
    device('FREYARA','2in1 RF tripolar handle','P37',category='Generic tabletop RF',rf=30,basis='Seller handle-power claim',input_w=72,input_kind='24 V × 3 A supply capacity',freq='1 MHz intended by listing (printed mHz)',notes='Seller lists tripolar 20–30 W; keep separate from hexapolar handle.',rf_label='20–30 W handle claim')
    device('FREYARA','2in1 RF hexapolar handle','P37',category='Generic tabletop RF',rf=60,basis='Seller handle-power claim',input_w=72,input_kind='24 V × 3 A supply capacity',freq='1 MHz intended by listing (printed mHz)',notes='Seller lists hexapolar 50–60 W. Same console as tripolar row; not a separate unique device.',rf_label='50–60 W handle claim')
    for model in ['Allfond triangular 3-probe family','RF01 generic / unnamed private-label family','Margotan private-label handheld lead']:
        device('OEM / unbranded',model,'U01',category='Generic tabletop RF' if 'Margotan' not in model else 'Generic handheld RF',basis='Pasted supplier lead only',notes='No exact model/label/IFU matching. Do not import a lookalike seller’s watts, temperature cutoff or FDA clearance.')
    for mode,vals in [('RET',[('S',130),('M',150),('L',200),('XL',300)]),('CET',[('S',65),('M',60),('L',70),('XL',110)])]:
        for size,w in vals:
            device('MYCHWAY',f'CET RET console · {mode} {size} electrode','P39',category='Generic tabletop RF',rf=w,basis='Seller output claim',notes='Console/electrode configuration, not eight unique devices. No specified load, duty cycle or independently measured output. Larger body electrodes cannot define a facial maximum.')
    device('MYCHWAY','MS-11Y3 generic RF family','P40',category='Generic tabletop RF',notes='Supplier manual preserved; no unambiguous comparable RF-output figure extracted.')
    for mode,w in [('Face RF',70),('Eye RF',40),('Body RF',80)]:
        device('MYCHWAY',f'MS-76F1SBMAX · {mode} configuration','P114',category='Generic tabletop RF',rf=w,input_w=80,input_kind='80 W system input, supplier manual',freq='1 MHz',basis='Supplier manual output claim',notes=f'Supplier manual claims {w} W for {mode} and lists 80 W system input. The body claim equals the entire stated input; load and duty convention are absent. Treat as low-confidence brochure/manual output, not independent measurement.',rf_label=f'{w} W {mode.lower()} claim*')
    device('NEO','Alpha controller','P41 P77',category='Generic tabletop RF',basis='Ambiguous power headline',notes='300 W headline in pasted research and Q&A; Alpha face/Soft RF power not established. No numeric RF ranking; directory consumption for Plus does not prove Alpha equivalence.')
    device('NEO','Plus RF-300W','P77 P41',category='Generic tabletop RF',input_w=300,input_kind='Secondary directory consumption, label unverified',basis='Directory input; RF unknown',notes='300 W consumption is not 300 W RF output. Separate from handheld home devices.')
    # Retain the full October 2 market census, replacing broad rows resolved above.
    old=json.loads((DATA/'rf_market_census_2026-10-02.json').read_text())
    old_sources={s['id']:s for s in json.loads((DATA/'rf_sources_2026-10-02.json').read_text())}
    skip={'MimiSilk','CurrentBody','NEWA','Sensica','Silkn','Konmison','AMIRO'}
    for x in old:
        if x['brand'] in skip or x['brand']=='Professional' and 'Thermage' in x['model']:continue
        if x['brand']=='TriPollar' and 'STOP Vx2 / STOP Vx Gold2' in x['model']:
            device('TriPollar','STOP VX2 Model U','P105',rf=5.7,load=200,basis='Manufacturer manual',input_w=12,input_kind='8 V × 1.5 A DC supply capacity',freq='1 MHz',notes='Manual text specifies 5.7 W at 200 Ω; its own plotted curve reads about 6.6 W at that load. Preserve both because the manual is internally inconsistent. Curve read-offs are approximate, not a lab measurement.',rf_label='5.7 W @ 200 Ω; own graph ≈6.6 W*',curve_data=[{'load_ohm':50,'rf_w':0.1},{'load_ohm':100,'rf_w':0.1},{'load_ohm':150,'rf_w':0.1},{'load_ohm':200,'rf_w':6.6},{'load_ohm':300,'rf_w':5.0},{'load_ohm':400,'rf_w':3.7},{'load_ohm':500,'rf_w':3.2}],curve_label='STOP VX2 Model U manual plot; approximate read-offs*')
            device('TriPollar','STOP VX Gold 2','P106',input_w=10,input_kind='5 V × 2 A maximum adapter rating',freq='1.0–1.25 MHz',basis='Official manual; RF output undisclosed',notes='Official exact-family manual gives a 10 W maximum supply rating and 1.0–1.25MHz RF frequency, but no comparable RF output watts.')
            continue
        if x['brand']=='TriPollar' and 'ENVIG EDGE' in x['model']:
            device('TriPollar','ENVIG EDGE','P107',category='Home face RF',input_w=10,input_kind='5 V × 2 A USB input rating',runtime=30,basis='Official manual; RF output undisclosed',notes='Manual gives 30 minutes continuous use per full charge, but no battery capacity or RF watt output. 10 W USB adapter rating is not treatment power.')
            continue
        cats='Professional RF' if x['brand']=='Professional' else 'Home body RF' if 'Cavispa' in x['model'] else 'Home face RF'
        ids=x['source_ids'].split(); sid=next((s for s in ids if s in old_sources),None)
        device(x['brand'],x['model'],'L01',category=cats,freq=x['rf_frequency_mhz'],temperature=x['temperature_claim'],basis='Prior inventory; RF unknown',notes='Carried forward from 2026-10-02 market census; comparable RF-output watts not established. '+x['evidence'])
        ROWS[-1].update(prior_source_ids=ids,checked='2026-10-02',product_url=old_sources[sid]['url'] if sid else None)
        if x['brand']=='YA-MAN':
            model=x['model']
            ya={
                'Bloom 6':('P79',21,'Manual power consumption approx. 21 W; whole-device, not isolated RF. Rated supply DC9V×3A; manual also lists about 30 min operation.'),
                'Bloom 5':('P80',18,'Manual specifies approx. 18 W while charging and DC9V×2A rated supply; approx. 30 min operating time. Charging use is not treatment draw.'),
                'Bloom WR':('P81',9,'Manual specifies approx. 9 W while charging, DC5V×2A and about 40 min operation; no RF output watt.'),
                'Bloom Red':('P82',None,'Exact-family manual checked; it gives no comparable RF-output watt in the recovered specification.'),
                'Bright Lift':('P83',4.5,'Manual specifies approx. 4.5 W whole-device consumption, Li-ion and about 40 min operation; RF is not separately rated.'),
                'Deep Lift':('P84',4.5,'Manual specifies approx. 4.5 W while charging and about 30 min at maximum D×LIFT; charging draw is not RF output.'),
                'Shiny NEO':('P85',4.5,'Manual specifies approx. 4.5 W while charging and about 30 min at maximum DYHP power; charging draw is not RF output.'),
                'Shiny M18':('P86',None,'Exact-model manual archived; no independently verified isolated RF watts assigned.'),
                'Prestige S':('P87',15,'Manual specifies approx. 15 W whole-device consumption and DC9V×2A rated supply; RF output is not isolated.'),
                'Prestige SS':('P88',20,'Manual specifies approx. 20 W whole-device consumption and DC12V×3A rated supply; RF output is not isolated.'),
                'Prestige SP II':('P90',None,'Exact-model manual archived; no separately stated RF output watt recovered.'),
                'Prestige SP III':('P91',18,'Manual specifies approx. 18 W whole-device consumption and DC9V×2A rated supply; RF output is not isolated.'),
                'Prestige SP':('P89',18,'Manual specifies approx. 18 W whole-device consumption and DC9V×2A rated supply; RF output is not isolated.'),
                'Prestige PRO':('P92',20,'Manual specifies approx. 20 W whole-device consumption and DC12V×5A rated supply; RF output is not isolated.'),
                'EX eye pro':('P93',13,'Exact HRF-20-EYE manual specifies approx. 13 W whole-device consumption and DC9V×2A supply; this is not RF watts.'),
                'Photo PLUS EX':('P93',13,'P93 specifically documents HRF-20-EYE at approx. 13 W whole-device consumption; do not generalize this rating to every EX regional unit.'),
                'Photo PLUS HRF10':('P94',None,'Exact-model official manual archived; no isolated RF watt assigned.'),
                'Photo PLUS Hyper':('P95',None,'Exact-family official manual archived; no isolated RF watt assigned.'),
                'Cavispa RF Core PLUS':('P96',5,'Manual specifies approx. 5 W while charging and DC9V×2A charger output; RF output is not stated.'),
                'Cavispa RF Core':('P97',None,'Exact HRF-17 official manual archived; adjacent Core EX/Premium aliases are not assumed identical.'),
                'Cavispa RF Core EX':('P100',None,'Exact HRF-18 Japanese manual archived; no comparable RF watts transcribed.'),
                'EX Smooth S':('P98',None,'Exact HRF-20L-2 Japanese manual archived; no comparable RF watts transcribed.'),
                'Smart':('P99',None,'Exact HRF-11-SE Japanese manual archived; no comparable RF watts transcribed.'),
            }
            model_lower=model.lower()
            match_order=sorted((k for k in ya if k!='Photo PLUS EX'),key=len,reverse=True)+['Photo PLUS EX']
            item=next(((k,ya[k]) for k in match_order if k.lower() in model_lower),None)
            if item:
                _,(msid,w,power_note)=item
                sources=[msid,'L01']
                if 'Panasonic' in model:sources=['L01']
                if w is not None:
                    ROWS[-1].update(input_w=w,input_kind='Manufacturer whole-device power / charging figure; RF not isolated')
                if 'Deep Lift' in model:
                    ROWS[-1].update(runtime_min=30)
                ROWS[-1].update(source_ids=sources,checked=DATE,product_url=next(s['url'] for s in SOURCES if s['id']==msid),notes=power_note+' RF output watts remain undisclosed.')
        if x['brand']=='Panasonic' and any(k in x['model'] for k in ['EH-SR90','EH-SR85','EH-SR86']):
            sid={'EH-SR90':'P42','EH-SR85':'P43','EH-SR86':'P44'}[next(k for k in ['EH-SR90','EH-SR85','EH-SR86'] if k in x['model'])]
            manual={'EH-SR85':'P108','EH-SR86':'P109'}.get(next(k for k in ['EH-SR90','EH-SR85','EH-SR86'] if k in x['model']))
            ROWS[-1].update(input_w=7,input_kind='Approx. 7 W while charging (not RF output)',source_ids=([manual] if manual else [])+[sid,'L01'],checked=DATE,notes='Official manual/specification checked. Approx. 7 W is explicitly charging consumption; runtime and lithium-ion battery disclosure do not provide RF watts.')
        if 'Deep Lift' in x['model']:
            ROWS[-1].update(runtime_min=30,source_ids=['P84','P45','L01'],input_w=4.5,input_kind='Approx. 4.5 W while charging (official manual)',checked=DATE,notes='Official manual specifies approx. 4.5 W while charging and about 30 min at maximum D×LIFT level. Neither number identifies isolated RF output.')
    for brand,model,sid,w,freq,load in [
        ('Solta','Thermage FLX','P48',400,'6.78 MHz',None),
        ('Lutronic','XERF · 6.78 MHz mode','P49',400,'6.78 MHz',None),
        ('Lutronic','XERF · 2 MHz mode','P49',300,'2 MHz',None),
        ('Classys','Volnewmer','P50',115,'6.78 MHz',None),
        ('Wontech','Oligio','P51',145,'6.78 MHz',None),
        ('Cynosure','TempSure wrinkle mode','P10 P71',120,'4 MHz',None),
        ('Cynosure','TempSure tissue-heating mode','P10 P71',300,'4 MHz',None),
        ('Cutera / Ilooda','Secret RF','P59',25,'2 MHz',500),
        ('Jeisys','Potenza','P60 P61',50,'1 / 2 MHz',200),
        ('Jeisys','Potenza Prime','P61',50,'1 / 2 MHz',200),
        ('Lutronic','Genius','P62',50,'460 kHz',None),
        ('EndyMed','PRO MAX platform','P63',100,'1 MHz',None),
        ('Venus','Viva MD Diamondpolar','P54',75,'1 MHz',None),
        ('Venus','Versa Pro Diamondpolar','P55',75,'1 MHz',None),
        ('Venus','Versa Pro Octipolar','P55',150,'1 MHz',None),
        ('Venus','NOVA Octipolar','P56',150,'1 MHz',None),
        ('Venus','NOVA Diamondpolar','P56',75,'1 MHz',None),
    ]:
        device(brand,model,sid,category='Professional RF',rf=w,load=load,basis='FDA specification',freq=freq,clearance=' / '.join(re.findall(r'K\d{6}', ' '.join(next(s['title'] for s in SOURCES if s['id']==a) for a in sid.split()))),notes='Professional context. Platform maximum, mode and applicator matter; not a home protocol, continuous absorbed skin power, or efficacy ranking.')
    device('InMode','Morpheus8 / cleared platform association','P52 P53',category='Professional RF',rf=65,basis='FDA specification',freq='1 MHz ±2%',notes='FDA submission gives a 65 W RF specification for the named system context. Applicator, mode and treatment settings still govern; this is not a home-use rating or a measured tissue dose.')
    device('Pollogen','Legend X','P57 P58',category='Professional RF',basis='FDA records reviewed; output not stated',notes='Two FDA records for the Legend X family reviewed; no comparable RF output watt was stated in the captured evidence. Do not transfer a different platform’s maximum.')
    device('Pollogen','Geneo X Elite','P15 P16',category='Professional RF',rf=6,basis='FDA specification',freq='1 MHz ±10%',notes='K233766 reports maximum RF output 6.0 W ±20% and continuous output; its predicate column lists 5.7 W ±10%. The extracted output table does not identify a test load. K242227 is a later family update, not a second device.',rf_label='6.0 W ±20%')
    for brand,model,sid,freq,w in [('NIRA','Original Precision / Model 2 Pro','P11 P70','1450 ±20 nm',2),('Tria','FANp / older Age-Defying fractional laser','P12','1440 nm',None),('Merz','Ulthera System / Ultherapy PRIME','P64 P65','Focused ultrasound',None),('Sofwave','SUPERB platform','P66 P67 P68 P69','Ultrasound',None),('DermRays','Revive','P72','1064 nm',None),('DLUS','D3 optical lead','P78','1064 nm seller claim',None)]:
        device(brand,model,sid,category='Other thermal / optical',basis='Separate technology',freq=freq,notes=(f'{w} W maximum optical output; not RF watts. ' if w else '')+'Retained from pasted thermal comparison; see original technology topic. Do not rank alongside RF output.')

    # Used-market leads are separate from verified product specifications. The
    # generic cohort and unresolved model IDs intentionally have no RF value.
    device('TriPollar','STOP X / Model U (U.S. used-market candidate)','P05 P13 P121 P125',rf=5.7,load=200,
        basis='FDA STOP U specification + official U.S. model mapping (conditional)',
        input_w=12,input_kind='8 V × 1.5 A external supply capacity (STOP U UXV family)',freq='1 MHz',
        temperature='Temperature-controlled; exact numeric cutoff not confirmed here',
        clearance='K182774 / K203665; exact listing label not verified',
        notes='eBay STOP X asks were about $175–$239; one listing called it Model U. Pollogen maps U.S. STOP X to STOP U; the 5.7 W ±10% RMS at 200 Ω FDA figure is conditional on the exact U.S. unit label matching that family. Do not transfer it to non-U.S. STOP X, STOP VX, VX2, or VX Gold 2.',
        rf_label='5.7 W ±10% RMS (conditional U.S. mapping)',confidence='medium')
    device('TriPollar','STOP VX (legacy used-market candidate; exact revision unverified)','P122',
        basis='Used-sale evidence only; RF output not recovered',
        notes='Distinct STOP VX listing sold device-only/no gel for $250 on 2026-07-25. No exact STOP VX IFU or output rating was recovered. Keep separate from STOP X, STOP VX2 and STOP VX Gold 2; sale does not establish production status or performance.',confidence='low')
    device('Toe Talk','DMR-2121 5-in-1 RF/EMS (indexed marketplace lead)','P116 P117',category='Generic handheld RF',
        basis='Marketplace identity only; RF output unknown',
        notes='One older indexed eBay card showed $89.99 and 415 sold; another showed $44.95. The sold counter is listing-specific and stale. No exact manufacturer manual, RF wattage, test load, duty cycle or thermal-control specification recovered; DMR-2121 is not merged with DR-04.',confidence='low')
    device('Toe Talk','DR-04 5-in-1 RF/EMS','P116 P118',category='Generic handheld RF',
        basis='Marketplace identity only; RF output unknown',
        notes='eBay item 167388282080 showed $35, five available and one sold. No exact manufacturer manual, RF wattage, test load, duty cycle or thermal cutoff recovered. Do not assume it is the DMR-2121.',confidence='low')
    device('IFAE','A083 6-in-1 home RF (seller-identified)','P123',category='Generic handheld RF',
        basis='Marketplace identity only; RF output unknown',
        notes='eBay listing ended at a $78 ask on 2026-08-02 and was not confirmed sold. No exact IFU or RF output/thermal-control evidence recovered.',confidence='low')
    device('Unbranded / Vilnason','SC114 dot-matrix rechargeable RF handset','P124 P126 P127',category='Generic handheld RF',
        basis='Low-confidence reseller rated-power claim; RF output unknown',
        input_w=4.5,input_kind='Reseller-stated 9 V × 0.5 A supply capacity; not RF output',
        freq='1 MHz reseller claim',temperature='15-minute auto-off timer claimed; numeric thermal cutoff undisclosed',
        rf_label='Unknown RF; 5 W device-power claim*',
        notes='eBay auction ended at $69.99 with zero bids; $99 Buy It Now was shown, and seller fields conflict between 220 V and rechargeable. Two reseller pages identify SC114 and repeat “rated power 5 W,” 1 MHz and a 9 V/500 mA supply (4.5 W capacity), but do not label 5 W as isolated RF output. The internal rechargeable battery/use-time claims and supply field are not reconciled. The 15-minute timer is not a measured temperature cutoff. No exact-model manual PDF, RF test load or duty cycle recovered; low confidence, not an RF watt ranking.',confidence='low')
    device('Unbranded / assorted sellers','5-in-1 RF/LED facial handset cohort (eBay search snapshot)','P116',category='Generic handheld RF',
        basis='Search cohort; not one device; RF output unknown',
        notes='The 53-result eBay query mixed near-identical low-cost handheld RF/LED listings with unrelated salon equipment. This is a market cohort placeholder, not a unique model. No cohort-level wattage or safety inference is defensible.',confidence='low')

def preserve_intake():
    originals=[('U01','89c3ea94-dd3b-4ae7-9840-282881c342fc','MimiSilk, battery and generic follow-ups'),('U02','0529d88a-b329-44a1-b9c1-399605271eec','Home temperature, clearance and wattage notes'),('U03','cb07707e-8814-4562-b73b-a02cd4af150b','Patent/FDA and thermal-device report'),('U04','52390a5d-6ed7-4f22-8955-d3b2c299286b','Duplicate patent/FDA report')]
    manifest=[]
    for sid,folder,title in originals:
        original=Path('/Users/samueldovgin/.codex/attachments')/folder/'Pasted text.txt'
        dest=SRC/(sid+'_user_research.txt')
        if original.exists():shutil.copyfile(original,dest)
        manifest.append(dict(id=sid,title=title,local=str(dest.relative_to(TOP)),sha256=hashlib.sha256(dest.read_bytes()).hexdigest(),source_class='user-supplied research transcript',support='Research leads and original conversation; not primary evidence.',limits='Citations were pasted as labels without URLs. Original images mentioned in text were not supplied here.'))
    (DATA/f'rf_power_intake_{DATE}.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2)+'\n')
    return manifest

def write_ledger():
    build_rows()
    assert len({r['id'] for r in ROWS})==len(ROWS)
    assert all(r['rf_max_w'] is None for r in ROWS if r['category']=='Other thermal / optical')
    assert next(r for r in ROWS if r['model']=='LB056B three-probe tabletop')['rf_max_w'] is None
    assert next(r for r in ROWS if r['model']=='sensiLift original')['treatment_max_w']==6.5
    payload=dict(date=DATE,scope='Records include model families, modes, accessories and historical revisions; not a count of unique devices.',devices=ROWS,sources=SOURCES)
    (DATA/f'rf_power_atlas_{DATE}.json').write_text(json.dumps(payload,ensure_ascii=False,indent=2)+'\n')
    (DATA/'rf_power_atlas.js').write_text('window.RF_POWER_ATLAS='+json.dumps(payload,ensure_ascii=False).replace('</','<\/')+';\n')
    fields=list(ROWS[0])
    fields+=['prior_source_ids']
    with (DATA/f'rf_power_atlas_{DATE}.csv').open('w',newline='') as f:
        writer=csv.DictWriter(f,fieldnames=fields,lineterminator="\n");writer.writeheader()
        def csv_value(v):
            if isinstance(v,list):
                return ' '.join(v) if all(isinstance(x,str) for x in v) else json.dumps(v,ensure_ascii=False)
            if isinstance(v,dict):return json.dumps(v,ensure_ascii=False)
            return v
        for r in ROWS:writer.writerow({k:csv_value(v) for k,v in r.items()})
    return payload

def refs(ids):
    lookup={s['id']:s for s in SOURCES}
    return ' · '.join(f'[{sid}]({lookup[sid]["url"]})' for sid in ids.split() if sid in lookup)

def write_documents(intake):
    n=len(ROWS)
    head=f'# Home RF wattage atlas: rated, measured and inferred power\n\n*Updated {DATE}. {n} comparison records, including model families, regional revisions, accessories and professional modes; this is not {n} unique devices or an exhaustive worldwide census.*\n\n'
    doc=head+'''The largest number in a listing is often the wrong number to compare. **The clearest numeric home RF bench result in this corpus is original wired NEWA: 10 W into 360 Ω.** A manufacturer manual specifies 20 W for EU Silk’n FaceTite MultiPlatform H2501; the current North American H2502/HA2502 manual specifies 15 W. Higher advertised generic outputs exist, but load, duty cycle and facial applicability are generally missing.

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
'''
    for model,sids in [('Original wired 3DEEP','P01'),('Titan AllWays','P06'),('sensiLift original','P03'),('sensiLift Pro ST300','P04'),('STOP U UXV','P05'),('Skin RF ST030 (US)','P02')]:
        r=next(x for x in ROWS if x['model']==model)
        setting=f"{r['treatment_max_w']:g} W" if r['treatment_max_w'] is not None else 'Not separately disclosed'
        measured=f"{r['measured_w']:g} W" if r['measured_w'] is not None else 'No exact result; specification / passing tests only'
        doc+=f"| {r['brand']} {model} | {r['rf_label']} | {setting} | {measured} | {r['load_ohm'] or 'Undisclosed'} Ω; {r['temperature']} | {refs(sids)} |\n"
    doc+='''
**What this group found:** FDA records give a useful 5–10 W handheld RF specification range, but only NEWA supplies an explicit 10 W numerical bench result here. “Tests passed” is not a published watt measurement. Surface cutoffs around 40–43°C are controller limits, not measurements of dermal temperature at 1–3 mm.

### NEWA pulse timing: a conditional estimate

The De Novo record gives 300 ms or 450 ms pulses per 750 ms cycle: duty factors 0.40 and 0.60. If its 10 W measurement is on-pulse power, then **10 × duty factor = 4 or 6 W** before further regulation. The public document calls its measured value “total power” without fully defining the averaging convention. Consequently this atlas does **not** place 4/6 W in the measured-output column or use it as a verified continuous-treatment ranking. Energy for any pulse would also require the applicable power convention. '''+refs('P01')+'''

## Manual specifications and higher advertised values

| Device / configuration | Published value | Classification and limitation | Evidence |
|---|---:|---|---|
| Silk’n FaceTite MultiPlatform H2501 EU | 20 W maximum RF | Manufacturer IFU; exact-model U.S. clearance not established here | '''+refs('P19')+''' |
| Silk’n Titan MultiPlatform H2502 + HA2502 current NA | 15 W maximum RF | Current official IFU; 24 W adapter separately specified | '''+refs('P17 P21')+''' |
| Silk’n H2502 + HA2502 historical IFU | 20 W; bare head 10 W | Historical mirror; not a second unique device; conflicts with current manual | '''+refs('P76')+''' |
| Silk’n Titan Mini H2600 / original Titan H2111/H2112 | 10 W maximum RF | Distinct battery vs corded products | '''+refs('P18 P20')+''' |
| AMIRO R3 Turbo / R1 PRO US | 15 W advertised | No load-test report; 8→15 W predecessor/region discrepancy | '''+refs('P29 P30 P31')+''' |
| MimiSilk Vera | 4.5 / 9 / 18 W advertised | RF output claim; DLUS’s 18 W supply/consumption lead does not verify it | '''+refs('P24 P25 P28')+''' |
| MLAY RF01 | 25 W face / 50 W body claimed | Seller/brand listing; 50 W total input; peak/continuous convention missing | '''+refs('P33')+''' |
| FREYARA Mini 3in1 | 20–50 W handle claim | Seller claim; 72 W supply capacity is a separate figure | '''+refs('P36')+''' |
| FREYARA 2in1 | 20–30 W tripolar / 50–60 W hexapolar | Two handles on one console; not interchangeable facial modes | '''+refs('P37')+''' |
| MYCHWAY CET/RET | 60–110 W CET / 130–300 W RET claimed | Electrode-size-dependent seller values; separate tabletop class | '''+refs('P39')+''' |
| TriPollar STOP VX2 Model U | 5.7 W at 200 Ω in text; plot reads about 6.6 W* | Same manual disagrees with its own curve; plotted points are approximate read-offs | '''+refs('P105')+''' |
| MLAY S3 handheld | 25 W face / 14 W body* | Current official product claims; load and duty convention absent | '''+refs('P111')+''' |
| MLAY RF02 S02B | 36 W rated input; RF output undisclosed | Current official product page; keep separate from brochure RF02/S06 variant | '''+refs('P112 P113')+''' |
| MLAY RF02 / S06 brochure variant | 38 W output* | Indexed brochure claim; source host returned 404; exact relation to S02B unresolved | '''+refs('P113')+''' |
| MYCHWAY MS-76F1SBMAX | Face 70 W*, eye 40 W*, body 80 W* | Supplier manual; system input also 80 W; load/duty absent | '''+refs('P114')+''' |

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

Battery sources: '''+refs('P22 P23 P18 P73 P17 P06 P19 P04 P42 P43 P44 P45')+'''

**What this section found:** known capacity plus runtime can test the consistency of a continuous-output claim; it cannot estimate RF watts reliably. “Up to” runtime has no specified test setting and is not a hard upper/lower RF bound. The atlas deliberately omits arbitrary 50–80% conversion-efficiency guesses from its device ranking.

## Load curves, thermal control and depth

The chart above plots the manual’s output-versus-load markers for the original Titan, current Titan MultiPlatform, Titan Mini and STOP VX2. An asterisk marks approximate visual read-offs from source plots, not bench measurements. The STOP VX2 manual also states 5.7 W at 200 Ω, while the curve appears closer to 6.6 W at the same load; both are preserved and the conflict is called out. The Titan Mini curve appears to be about 2.6 W at 200 Ω, not the earlier pasted estimate of 2.7 W. Open the preserved IFUs from each chart row to inspect the source plots. Different loads and graph scales do not support a normalized rank. '''+refs('P17 P18 P20 P105')+'''

No verified product-specific temperature-versus-depth comparison was established for Vera, generic tabletop devices and the established handhelds. Electrical RF watts, skin-sensor temperature and collagen-remodeling outcomes are distinct measurements. The [clinical evidence map](index.html#doc11) and [MHz/temperature review](index.html#doc13) remain the outcome references.

## Professional and other thermal context

The chart includes professional context behind a separate filter: Thermage FLX 400 W; XERF 400 W at 6.78 MHz / 300 W at 2 MHz; Volnewmer 115 W; Oligio 145 W; TempSure 120 W wrinkle / 300 W tissue heating; Secret RF 25 W at 500 Ω; Potenza/Prime 50 W at 200 Ω; Genius 50 W; PRO MAX 100 W platform (some handpieces/indications limited to 65 W); and Venus 75/150 W applicators. These are FDA specifications, not measured tissue dose or unsupervised home-use ratings. '''+refs('P48 P49 P50 P51 P10 P59 P61 P62 P63 P54 P55 P56')+'''

NIRA’s 2 W is **optical** output; Tria is fractional laser; Ulthera and Sofwave are ultrasound. They appear in a separate “Other thermal / optical” inventory with no RF bar. See [thermal comparisons and pasted-research reconciliation](index.html#doc21), [RF versus laser](index.html#doc9), [non-fractional laser power](../06_non_fractional_lasers/power_comparison_visualizer.html), and [fractional laser research](../03_fractional_laser_resurfacing/index.html).

## Specific remaining gaps

- Same-load RF tests at 100/150/200/360/500 Ω, including on-pulse, RMS and session-average conventions.
- Exact used-device labels, manufacturing revisions and supplied attachments for Silk’n listings; the screenshots mentioned in the pasted text were not attached in this request.
- Vera/DLUS OEM contract or matching regulatory/model labels; generic units’ calibrated temperature cutoffs and the test load/duty convention for supplier claims.
- Depth-resolved thermal maps and clinical trials that would justify an efficacy comparison, rather than a wattage comparison.

## Sources and complete inventory

Every numerical record has source IDs and evidence notes in the [chart](rf_power_explorer.html), [CSV](data/rf_power_atlas_2026-10-09.csv) and [JSON ledger](data/rf_power_atlas_2026-10-09.json). [Rendered source register and intake map](index.html#doc21) · [Verbose recovery log](source_docs/research_resource_log_2026-10-09.txt). Records carried forward from the 51-row October 2 census show their older check date; unverified historic or generic leads remain unranked.
'''
    (TOP/'19_rf_wattage_atlas.md').write_text(doc)
    (TOP/'20_generic_rf_and_mimisilk_oem_audit.md').write_text('''# Generic RF devices and the MimiSilk / DLUS manufacturer lead

*Updated 2026-10-09. Supplier descriptions establish advertised claims, not measured treatment output. See the [wattage chart](rf_power_explorer.html) and [power methodology](index.html#doc19).*

**The generic market has higher advertised numbers, but less usable output evidence.** The best next step is to identify the exact device, probe and power convention before attempting an output estimate. A common shell, frequency or RF01 name is insufficient to identify a factory or electronics.

## Generic/OEM comparison

| Unit / configuration | RF watts | Electrical input / supply | Evidence and unresolved issue |
|---|---|---|---|
| MLAY RF01 face / body | 25 / 50 W seller output claim | 50 W rated input | '''+refs('P33')+''' — output convention/load missing; equality at body maximum cannot be assumed continuous |
| MLAY S3 handheld | 25 W face / 14 W body output claims | No input watt or load disclosed | '''+refs('P111')+''' — current official page; starred manufacturer claims, not bench data |
| MLAY RF02 S02B current retail page | RF output not stated | 36 W rated input | '''+refs('P112')+''' — whole-device input is not RF output |
| MLAY RF02 / S06 brochure variant | 38 W output claim* | Power input convention absent | '''+refs('P113')+''' — indexed brochure; host is now 404; no identity match to S02B |
| MLAY S03 / S04 brochure handheld variants | 12 W* / 13 W* output claims | S03: 3.7 V × 2000 mAh; S04: 7.4 V × 650 mAh | '''+refs('P113')+''' — same indexed source; runtime, load and duty cycle unavailable |
| MLAY RF01 / S05 brochure variant | 48 W output claim* | Non-battery configuration; input not stated | '''+refs('P113')+''' — separate from current RF01 page; version match unresolved |
| Konmison LB056B | Not disclosed | 55 W consumption | '''+refs('P35')+''' — 2 MHz; 1–15 J/cm² energy claim; no valid watt conversion without time/area |
| FREYARA Mini 3in1 | 20–50 W handle claim | 24 V × 3 A = 72 W supply capacity | '''+refs('P36 P38')+''' — three-probe triangular family; no same-unit FDA/bench match |
| FREYARA 2in1 tripolar / hexapolar | 20–30 / 50–60 W handle claims | 72 W supply capacity | '''+refs('P37')+''' — separate handles and contact area; seller’s mHz typography is retained as an ambiguity |
| MYCHWAY CET/RET console | CET S/M/L/XL: 65/60/70/110 W; RET: 130/150/200/300 W | 110–220 V AC, total input not established here | '''+refs('P39')+''' — face/body electrode modes, not interchangeable handheld outputs |
| MYCHWAY MS-11Y3 | Comparable output unknown | Unresolved | '''+refs('P40')+''' — supplier manual preserved; vague clinical claims do not define watts |
| MYCHWAY MS-76F1SBMAX | Face 70 W*, eye 40 W*, body 80 W* | 80 W system input | '''+refs('P114')+''' — supplier manual claims; no load/duty convention and body claim equals total input |
| NEO Alpha / Plus | 300 W headline; face/Soft output unresolved | Plus directory calls 300 W consumption | '''+refs('P41 P77')+''' — exact Alpha electrical identity and load testing unresolved |
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

Sources: '''+refs('P24 P25 P26 P27 P28')+'''

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
''')
    write_intake_document(intake)

def write_intake_document(intake):
    d='''# Submitted research, FDA / patent crosswalk and source recovery

*Compiled 2026-10-09. All four supplied text files preserved verbatim. Original conversation statements remain leads unless the new source records substantiate them.*

Start with the [wattage chart](rf_power_explorer.html), [rated versus actual power](index.html#doc19), and [generic/OEM investigation](index.html#doc20). This page explains where the supplied material went and retains its broader patent and thermal-device context.

## Intake and de-duplication

| ID | Supplied material | Preservation and use |
|---|---|---|
'''
    for x in intake:d+=f"| {x['id']} | {x['title']} | [Preserved original transcript]({x['local']}); {x['sha256'][:12]}… checksum |\n"
    d+='''
U03 and U04 have identical SHA-256 checksums and identical content. Both originals are retained; they are counted once as an evidence lead. U01/U02 overlap substantially, so repeated answers do not provide independent corroboration. The text mentions eBay photographs that were not included with these four files; pictured labels therefore remain pasted descriptions.

| Supplied research lane | Logical location now | Reconciliation |
|---|---|---|
| Ranked home watts; rated vs measured | [Power atlas](index.html#doc19) and [chart](rf_power_explorer.html) | Distinguishes explicit bench numbers, specification, seller claim, input and unknown |
| Silk’n names, regional revisions and curves | Power atlas + model/configuration rows | H2501 EU 20 W; current H2502 NA 15 W; historical 20 W conflict retained |
| Batteries, runtime and likely draw | Power atlas battery table and battery chart view | Verified voltage required; estimates describe whole-device budgets |
| MimiSilk factory, ownership and claims | [MimiSilk/OEM audit](index.html#doc20) | D2 connection is a lead; ownership unverified; output/temperature claims separated |
| Generic triangular RF, MLAY, NEO and MYCHWAY | Generic/OEM table and separate chart class | Higher advertised outputs retained with probe/input limitations |
| Target temperatures and heating depth | [Temperature research](index.html#doc13), [clinical map](index.html#doc11), power metadata | Surface cutoff is distinct from alleged dermal temperature |
| FDA submissions over the last decade | Below + preserved FDA PDFs | Submissions are not unique products; tabletop platforms and optical/RF combination codes matter |
| Professional RF/patents | Below + [professional guide](index.html#doc17) | Mode specifications extracted where clear; patent-to-product mappings retained as leads |
| NIRA/Tria/ultrasound/LED comparisons | Below and existing laser/ultrasound topics | Optical watts and acoustic energy do not enter RF ranking |

## Home FDA cross-reference

The pasted list contains ten handheld home 510(k) records: Silk’n HST K162784; sensiLift K170499; STOP U K182774; STOP U UXV K203665 and K220322; FAQ 101 K222012; Titan AllWays K230013; CurrentBody K232424; FAQ 102 K240616; sensiLift Pro K250341. Their PDFs/letters are linked in P02–P09/P13–P14 below. NEWA DEN150005 is a 2015 De Novo authorization and a useful predicate; it lies outside an October 2016–October 2026 new-clearance window.

Geneo X Elite K233766 and K242227 are tabletop combined systems, not additional handheld families. The latter FDA PDF endpoint was unavailable in this pass, so its exact details/date remain an intake lead. These counts describe **the supplied working inventory**, not a certified complete FDA search. The pasted claim of “11 PAY-primary submissions” is not independently reproduced here; all claimed counts should be audited against a systematic database export before describing them as exhaustive.

The actual letters/summary are controlling for the model, code and indication. A 510(k) substantial-equivalence clearance is distinct from a patent grant, FDA registration/listing, marketing approval language and a new randomized efficacy trial.

## Patent leads retained from the supplied report

Only the two home-device patent records marked “record rechecked” were independently opened for this pass. The other entries are preserved research leads with patent links; **exact product coverage and legal status are not newly certified**. Do not infer efficacy, a device’s wattage or freedom to operate from a grant or a shared manufacturer.

| Product / family lead | Supplied issued-patent identifiers | Supplied FDA association | Status in this update |
|---|---|---|---|
'''
    patent_rows=[
        ('NEWA',['9844682'],'DEN150005','Record rechecked (P74); technical association, not a power test'),
        ('sensiLift',['11317961'],'K170499 / K250341','Record rechecked (P75); exact Pro coverage unconfirmed'),
        ('Ulthera / Ultherapy PRIME',['10537304','11123039','11723622','12102473'],'K233996 / K243035','Pasted manufacturer-marking lead; mapping not re-audited'),
        ('XERF',['12721667'],'K251327','Pasted multi-frequency technical association; claim mapping pending'),
        ('Thermage FLX',['10245440','10940327','11833364'],'K170758','Manufacturer-family lead'),
        ('Morpheus8',['11779388','12496121','12502214'],'K180189 / K192695','Platform/handpiece and patent claim mapping pending'),
        ('Venus Viva MD',['11197713','11207210','12653604'],'K201164','Manufacturer-family lead'),
        ('Venus Versa Pro',['11298259','11890486'],'K232192','Manufacturer-family lead'),
        ('Venus NOVA',['11547866','11684794','11890486'],'K252845','Manufacturer-family lead'),
        ('Legend X',['11717679','12064623','12642576'],'K232903 / K243217','Manufacturer-family lead'),
        ('Secret RF',['11779389'],'K170325','Ilooda technical association lead'),
        ('Potenza / Prime',['12508424','12533511'],'K192545 / K254185','Jeisys family allocation unresolved'),
        ('Sofwave',['12521575','12551731'],'K211483 / K223237 / K231537 / K240687','Ultrasound family lead; K231537 capture unavailable'),
    ]
    for model,pats,fda,status in patent_rows:
        links=' · '.join(f'[US{p}](https://patents.google.com/patent/US{p}B2/en)' for p in pats)
        d+=f'| {model} | {links} | {fda} | {status} |\n'
    d+='''
## Other thermal mechanisms retained

| Technology / device | Relevant supplied finding | Proper interpretation / home topic |
|---|---|---|
| NIRA original / Model 2 Pro | FDA K222685 compares 1450 ±20 nm, 2 W maximum optical power; original 0.8 s vs Model 2 2.0–3.1 s trains | P11/P70; optical power, not RF. No transfer to Pro 3 without exact record; [non-fractional lasers](../06_non_fractional_lasers/index.html) |
| NIRA patent US10695582 | Pasted 37–45°C, 2–8°C rise, 2–10 s and 0.5 mm example | Patent embodiment lead, not a verified marketed-device temperature; [patent record](https://patents.google.com/patent/US10695582B2/en) |
| Tria older fractional laser / newer FRX | Pasted 210–250 µm thermal microcolumns and clinical results | Earlier trial lead; do not assign to the newest FRX; [fractional topic](../03_fractional_laser_resurfacing/index.html) |
| Ulthera / Ultherapy PRIME | Pasted 1.5/3/4.5 mm focal depths | Professional ultrasound and anatomy control; [HIFU topic](../11_hifu_skin_tightening/index.html) |
| Sofwave SUPERB | Ultrasound heating with surface cooling | Professional context, not RF watts; P66–P69 |
| LYMA 808 nm / red-NIR LEDs / Omnilux | Pasted nonthermal collagen claims | Photobiomodulation lane; [LED topic](../04_red_light_therapy_handheld/index.html); no RF equivalence |
| DLUS D3 | New seller 1064 nm optical lead | Different modality from D2; optical power and exact clearance unknown (P78) |

**What this section found:** wavelength/frequency and nominal power alone do not identify depth, injury pattern or collagen benefit. The existing topic clinical pages hold outcome evidence; this update adds no new measured human comparison between home RF and those modalities.

## Source register and local recovery

P identifiers are unique to this October 9 pass. L01 is the prior [October 2 device census](data/rf_market_census_2026-10-02.json) and [source registry](data/rf_sources_2026-10-02.json); carried-forward rows retain their older date and source IDs. [Verbose log](source_docs/research_resource_log_2026-10-09.txt) · [Machine-readable source register](data/rf_power_sources_2026-10-09.json) · [CSV](data/rf_power_atlas_2026-10-09.csv) · [Full JSON](data/rf_power_atlas_2026-10-09.json).

| ID / canonical source | Supports | Preservation / limits |
|---|---|---|
'''
    for s in SOURCES:
        local=f"[Local {'PDF' if s['local'].endswith('.pdf') else 'capture'}]({s['local']})" if s.get('local') else 'URL-only; capture unavailable'
        support=s['support']
        used=[r for r in ROWS if s['id'] in r['source_ids'] and r['rf_max_w'] is not None]
        if s['id'].startswith('P') and int(s['id'][1:])>=48 and int(s['id'][1:])<=72 and used:
            support+=' '+ '; '.join(r['model']+': '+r['rf_label'] for r in used)+'.'
        d+=f"| {s['id']} · [{s['title']}]({s['url']}) | {support} | {local}; {s['source_class']}. {s['limits']} |\n"
    (TOP/'21_submitted_research_and_source_register.md').write_text(d)
    log=f'RF power research resource log — {DATE}\nScope: {len(ROWS)} comparison records, not unique devices; home focus plus generic and professional context.\nNew document map: 19 power methods; 20 OEM/MimiSilk; 21 intake and source crosswalk; 22 used-market tiers; rf_power_explorer.html chart.\n\n'
    for s in SOURCES+intake:
        local=s.get('local')
        log+=f"[{s['id']}] {s['title']}\nURL: {s.get('url','User attachment; original has no canonical URLs')}\nResolved URL: {s.get('resolved_url','Not applicable / not captured')}\nAccessed: {DATE} America/Chicago\nClass: {s['source_class']}\nUsed in: 19_rf_wattage_atlas; 20_generic_rf_and_mimisilk_oem_audit; 21_submitted_research_and_source_register; data/chart rows linked by source ID.\nSupports: {s['support']}\nKey record: "
        related=[r for r in ROWS if s['id'] in r['source_ids']]
        log+=json.dumps([dict(model=r['model'],RF=r['rf_label'],input_w=r['input_w'],input_kind=r['input_kind'],load_ohm=r['load_ohm'],battery_wh=r['battery_wh'],runtime_min=r['runtime_min'],temperature=r['temperature'],notes=r['notes']) for r in related],ensure_ascii=False)+'\n'
        log+=f"Finding: Specifications and attribution retained separately from direct measurements; no new independent comparative lab or clinical study.\nLimits: {s['limits']}\nLocal preservation: {local+'; sha256 '+s.get('sha256','') if local else 'URL-only — no usable lawful local copy available'}\nStatus/recheck: {s.get('status','User-supplied; unverified original claims')}; volatile product claims dated snapshot.\n\n"
    for lid,title,local in [('L01','October 2 market census / source register','data/rf_market_census_2026-10-02.json'),('L02','Existing RF viewer, README and clinical methodology','README.md'),('L03','Existing root and neighboring laser navigation','../README.md')]:
        log+=f'[{lid}] {title}\nURL: local archive\nAccessed: {DATE}\nClass: local archive\nUsed in: inventory continuity/navigation and outcome boundaries.\nSupports: Archive scope and previous source provenance, not newly measured power.\nLimits: Older claims are not current hardware measurements.\nLocal preservation: {local}\nStatus/recheck: retained, no unrelated edits overwritten.\n\n'
    log+='Change note: EU H2501 20 W versus current NA H2502 15 W kept separate; historical H2502 20 W not generalized. NEWA 4/6 W duty averages conditional only. Pasted efficiency scenarios are not device estimates. U03/U04 duplicates retained but not counted independently. DLUS cordless description conflicts with prior corded notes. Broad FDA counts and most product/patent mappings remain submitted leads.\n'
    (TOP/'source_docs'/f'research_resource_log_{DATE}.txt').write_text(log)
    (SRC/'README.md').write_text('# RF power audit source captures\n\n[Rendered recovery register](../../index.html#doc21) · [Power methodology](../../index.html#doc19) · [Used-market tiers](../../index.html#doc22) · [Verbose log](../research_resource_log_2026-10-09.txt).\n\nFDA PDFs, public manufacturer/supplier manuals and dated product-page captures are unchanged research evidence. HTML captures may contain third-party scripts; consult the rendered register for claims and canonical sources. The eBay snapshot is preserved as a dated metadata summary, not a mirrored listing archive. User transcripts U01–U04 are preserved verbatim as unverified intake; U03/U04 are identical. Local capture success is separate from clinical or technical verification. See the register for every filename, source URL, limitations and checksum.\n')

if __name__=='__main__':
    ap=argparse.ArgumentParser();ap.add_argument('--capture',action='store_true');args=ap.parse_args()
    write_corpus(args.capture)
    intake=preserve_intake()
    payload=write_ledger()
    write_documents(intake)
    print(json.dumps({'records':len(ROWS),'sources':len(SOURCES),'captured':sum(bool(s.get('local')) for s in SOURCES),'unavailable':[s['id'] for s in SOURCES if not s.get('local')]},indent=2))
