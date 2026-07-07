# Clinic Device Evidence Map

## 1. Clinic devices in the captured FDA corpus

The OHV openFDA snapshot captured on 2026-07-07 contains 30 records under product code `OHV`, regulation `878.4590`, the focused ultrasound aesthetic classification [[1]](data/openfda-ohv-510k-2026-07-07.csv). The visible device families include Ulthera/Ultherapy, Sofwave, LipoSonix, UltraShape, SCIZER, BeShape, and related professional systems.

No OTC home facial HIFU/MFU clearance appeared in this captured OHV dataset. That does not prove no consumer ultrasound product exists anywhere, but it does mean this archive found no FDA-cleared OTC home facial-lifting HIFU analog in the relevant product-code snapshot.

## 2. Device map

| Device / family | Captured FDA status | Main indication in captured file | Depth / geometry signal | Evidence weight | Archive read |
|-----------------|--------------------|----------------------------------|-------------------------|-----------------|--------------|
| **Ulthera / Ultherapy** | Class II focused ultrasound aesthetic device, product code OHV; prescription use [[2]](source_docs/fda-k072505-ulthera-de-novo-classification.pdf)[[3]](source_docs/fda-k260618-ulthera-prime-2026.pdf) | Eyebrow lift; submental/neck lift; decollete lines/wrinkles; abdomen/anterior arms/posterior arms/knees laxity in latest captured files [[3]](source_docs/fda-k260618-ulthera-prime-2026.pdf)[[4]](source_docs/fda-k243035-ulthera-expanded-body-indications.pdf) | DeepSEE imaging to 8 mm; transducers at 1.5/3.0/4.5 mm in IFU [[5]](source_docs/ulthera-us-instructions-for-use-2021.pdf) | Strongest clinic HIFU anchor | Best reference for "HIFU/MFU lift," but not a home-device template |
| **Sofwave / Sofacia** | Class II OHV professional ultrasound device; prescription use [[6]](source_docs/fda-k191421-sofacia-sofwave.pdf)[[7]](source_docs/fda-k211483-sofwave-lifting-indications.pdf) | Facial lines/wrinkles; eyebrow lift; submental/neck tissue lift; additional cellulite/acne-scar/arm-laxity indications in later files [[7]](source_docs/fda-k211483-sofwave-lifting-indications.pdf)[[8]](source_docs/fda-k240687-sofwave-upper-arm-laxity.pdf) | 1-2 mm treatment depth in early FDA summaries; thermoelectric cooling; array-based applicator [[6]](source_docs/fda-k191421-sofacia-sofwave.pdf)[[7]](source_docs/fda-k211483-sofwave-lifting-indications.pdf) | Human clinical data in FDA summaries | Credible clinic ultrasound, but shallower/different geometry than Ulthera |
| **SCIZER** | Class II OHV prescription HIFU device [[9]](source_docs/fda-k230100-classys-scizer.pdf) | Non-invasive waist circumference reduction | 13 mm focal depth into subcutaneous adipose tissue; up to 46 x 46 mm region [[9]](source_docs/fda-k230100-classys-scizer.pdf) | Body-contouring clinical file | Not a face-lift device; useful for separating fat-disruption HIFU from skin-lift HIFU |
| **LipoSonix / UltraShape / BeShape** | OHV records in openFDA snapshot [[1]](data/openfda-ohv-510k-2026-07-07.csv) | Body contouring / fat-disruption category in this archive's read | Not fully extracted in this pass | Dataset signal only | Keep separate from facial HIFU tightening unless source file is extracted |
| **Hironic NEW DOUBLO 2** | FDA file captured under a different product-code/regulatory lane, not OHV facial HIFU [[10]](source_docs/fda-k251334-hironic-new-doublo-2.pdf) | RF/electrosurgical tissue coagulation/hemostasis | RF output, trained healthcare professional setting [[10]](source_docs/fda-k251334-hironic-new-doublo-2.pdf) | Important naming caution | "Doublo" brand naming is not enough; the captured file is RF/electrosurgical, not a home HIFU analog |

## 3. Ulthera / Ultherapy

Ulthera is the cleanest clinic-HIFU anchor because the FDA classification and IFU describe the mechanism, intended users, transducer depths, imaging, and safety controls in detail.

Important points:

- FDA's original de novo order classified Ulthera as Class II, product code `OHV`, and a prescription device for non-invasive eyebrow lift [[2]](source_docs/fda-k072505-ulthera-de-novo-classification.pdf).
- The latest captured Ulthera indication file, K260618, adds knees to previously cleared appearance-of-laxity body indications and retains eyebrow, submental/neck, and decollete indications [[3]](source_docs/fda-k260618-ulthera-prime-2026.pdf).
- DeepSEE imaging visualizes depths up to 8 mm to help ensure coupling and confirm treatment depth such as avoiding bone [[3]](source_docs/fda-k260618-ulthera-prime-2026.pdf)[[5]](source_docs/ulthera-us-instructions-for-use-2021.pdf).
- The IFU states the system is for properly trained physicians and properly trained persons under physician supervision [[5]](source_docs/ulthera-us-instructions-for-use-2021.pdf).
- The treatment stack uses transducer depths 1.5, 3.0, and 4.5 mm, with line geometry and TCP spacing rather than unplanned "shots" [[5]](source_docs/ulthera-us-instructions-for-use-2021.pdf).

The conclusion is not that Ulthera is magic. It is that Ulthera has a regulated professional stack around a difficult problem: placing controlled ultrasound injury at the intended depth.

## 4. Sofwave / Sofacia

Sofwave is relevant because it is an FDA-cleared professional ultrasound device for aesthetic indications, but it should not be collapsed into Ultherapy.

The K191421 Sofacia/Sofwave summary describes high-frequency ultrasonic pulses, an applicator array, active cooling, a 1-2 mm treatment depth, and a 12-week clinical evaluation for facial lines/wrinkles [[6]](source_docs/fda-k191421-sofacia-sofwave.pdf). The K211483 summary adds eyebrow and submental/neck lifting indications and reports clinical performance data, including blinded photo-identification outcomes and quantitative lift measures [[7]](source_docs/fda-k211483-sofwave-lifting-indications.pdf).

Archive read:

- Sofwave is a credible clinic ultrasound option for shallower dermal heating and aesthetic indications.
- It does not substitute for an Ulthera depth-stack comparison because the FDA summaries describe a different treatment depth and energy-delivery geometry.
- It is a useful reminder that "clinic ultrasound" is not one category; depth and geometry define what the device is trying to do.

## 5. Body-contouring HIFU is not facial lifting

SCIZER is a useful caution case. It is a professional HIFU system under the OHV category, but the captured FDA summary is for non-invasive waist circumference reduction. The file describes focusing HIFU energy at 13 mm from the skin surface into subcutaneous adipose tissue, raising tissue temperature over 56 deg C, and disrupting adipose tissue [[9]](source_docs/fda-k230100-classys-scizer.pdf).

That is not a home facial tightening target. In fact, unwanted facial fat/volume loss is one of the complications people worry about with facial ultrasound. So body-contouring HIFU is a separate lane, not proof that high-energy ultrasound should be improvised on the face.

## 6. Evidence confidence by use case

| Goal | Clinic HIFU/MFU confidence | Best-supported device lane | Notes |
|------|----------------------------|----------------------------|-------|
| Brow / mild lift | Moderate | Ulthera, Sofwave | FDA indications exist; effect size is generally subtle and anatomy-dependent |
| Submental / neck laxity | Moderate | Ulthera, Sofwave | Best done by trained providers; avoid volume-loss promises |
| Deeper laxity / SMAS-adjacent target | Moderate but provider-dependent | Ulthera | DeepSEE and 3.0/4.5 mm transducers are the reason it is the HIFU anchor |
| Fine lines / superficial wrinkles | Moderate | Sofwave or other clinic modalities | Sofwave's shallower 1-2 mm depth is relevant |
| Cellulite / body laxity | Device-specific | Sofwave/Ulthera body indications depending file | Do not infer face results from body indications |
| Waist circumference / fat | Device-specific | SCIZER/LipoSonix/UltraShape-type lane | Not a skin-lifting analogy |
| DIY facial lift | Low | None found | No OTC home facial HIFU clearance found in OHV snapshot |

## Sources

1. openFDA OHV 510(k) snapshot captured 2026-07-07. [CSV](data/openfda-ohv-510k-2026-07-07.csv) - Captured OHV device families and decision dates.
2. FDA K072505 / De Novo classification order for Ulthera. [Local PDF](source_docs/fda-k072505-ulthera-de-novo-classification.pdf) - Original Class II, OHV, prescription eyebrow-lift classification.
3. FDA K260618, Ulthera expanded knee indication. [Local PDF](source_docs/fda-k260618-ulthera-prime-2026.pdf) - Current captured indications and DeepSEE imaging language.
4. FDA K243035, Ulthera abdomen/arms indication. [Local PDF](source_docs/fda-k243035-ulthera-expanded-body-indications.pdf) - Expanded body-laxity indication and literature/clinical evidence summary.
5. Ulthera System Instructions for Use, 2021. [Local PDF](source_docs/ulthera-us-instructions-for-use-2021.pdf) - Training, contraindications/precautions, transducer table, TCP geometry, and adverse events.
6. FDA K191421, Sofacia/Sofwave facial lines and wrinkles. [Local PDF](source_docs/fda-k191421-sofacia-sofwave.pdf) - Initial Sofwave/Sofacia device description and clinical study summary.
7. FDA K211483, Sofwave lifting indications. [Local PDF](source_docs/fda-k211483-sofwave-lifting-indications.pdf) - Sofwave eyebrow and submental/neck lifting indications and clinical performance data.
8. FDA K240687, Sofwave upper-arm laxity and cellulite file. [Local PDF](source_docs/fda-k240687-sofwave-upper-arm-laxity.pdf) - Later Sofwave indication expansion and applicator details.
9. FDA K230100, Classys SCIZER. [Local PDF](source_docs/fda-k230100-classys-scizer.pdf) - HIFU waist-circumference reduction, 13 mm focal depth, and adipose-disruption mechanism.
10. FDA K251334, Hironic NEW DOUBLO 2. [Local PDF](source_docs/fda-k251334-hironic-new-doublo-2.pdf) - Captured "Doublo" file is RF/electrosurgical tissue coagulation, not OHV facial HIFU.
