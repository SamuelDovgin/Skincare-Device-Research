# HIFU Science Brief

## 1. What HIFU/MFU is doing

HIFU stands for high-intensity focused ultrasound. In aesthetic skin devices, the core idea is that acoustic energy is concentrated below the skin surface so the focal zone heats or mechanically disrupts a small volume of tissue while the epidermis is spared or cooled. FDA's original Ulthera classification describes the device type as focused ultrasound that produces localized mechanical motion, localized heating for tissue coagulation, or mechanical membrane disruption [[1]](source_docs/fda-k072505-ulthera-de-novo-classification.pdf).

That makes HIFU different from:

- **Fractional lasers:** optical energy absorbed by chromophores, creating microscopic thermal zones along light paths.
- **RF:** electrical current/resistive heating, governed by electrode geometry, impedance, and tissue temperature.
- **Microneedling:** mechanical puncture, sometimes with RF energy delivered through needles.

HIFU's promise is layer-specific heating without puncturing the skin. Its difficulty is that the operator has to know where the focal zone is actually landing.

## 2. Target depths are the whole story

Ulthera's IFU lists image/treat transducers at 1.5 mm, 3.0 mm, and 4.5 mm treatment depths, with DeepSEE imaging to 8 mm [[2]](source_docs/ulthera-us-instructions-for-use-2021.pdf). In SPT mode, Ulthera maps 3.0 and/or 4.5 mm to the SMAS/fibrous layer and 1.5 and/or 3.0 mm to the dermal layer [[2]](source_docs/ulthera-us-instructions-for-use-2021.pdf).

This is why home HIFU claims cannot be evaluated only by "shots" or heat sensation. A shot that lands too shallow may be irritation or superficial heat. A shot that lands too deep, too close to bone, thyroid, nerve-sensitive zones, or facial fat can be harmful. The clinical device stack tries to control that with:

- labeled transducer depth;
- line length and thermal coagulation point spacing;
- ultrasound gel/coupling;
- real-time or pre-treatment visualization where available;
- trained operator anatomy knowledge;
- exclusion zones and complication management.

## 3. Thermal coagulation points and line geometry

Ulthera therapy creates a line of discrete thermal coagulation points (TCPs). The IFU describes treatment line length of 5-25 mm, TCP spacing of 1-5 mm with 1.5 mm standard spacing, and an example where a 25 mm line at 1.5 mm center-to-center spacing produces 17 TCPs [[2]](source_docs/ulthera-us-instructions-for-use-2021.pdf).

That geometry matters. A clinic treatment is not a random collection of "shots." It is a planned distribution of focal points across tissue layers and anatomical zones. Too-close line spacing, gel pockets, transducer tilt, or poor contact can create burns or scarring risk [[2]](source_docs/ulthera-us-instructions-for-use-2021.pdf).

## 4. Ulthera versus Sofwave geometry

Ulthera is the deepest and most explicitly layer-mapped clinic anchor in this folder. It uses 1.5/3.0/4.5 mm treatment depths and DeepSEE visualization to confirm coupling and appropriate depth, such as avoiding bone [[2]](source_docs/ulthera-us-instructions-for-use-2021.pdf)[[3]](source_docs/fda-k260618-ulthera-prime-2026.pdf).

Sofwave is a separate clinic ultrasound approach. FDA summaries describe high-frequency ultrasonic pulses, an applicator with an array of ultrasonic transducers, thermoelectric cooling, and treatment depth around 1-2 mm [[4]](source_docs/fda-k191421-sofacia-sofwave.pdf)[[5]](source_docs/fda-k211483-sofwave-lifting-indications.pdf). Its clinical evidence and FDA-cleared indications matter, but it should not be treated as the same focal-depth stack as Ultherapy.

Practical translation:

| Device lane | Typical target in this archive | What to remember |
|-------------|--------------------------------|------------------|
| Ulthera / Ultherapy | Deeper dermal and fibrous/SMAS-adjacent laxity | Most useful anchor for "HIFU lift" discussion; visualization and transducer depth are central |
| Sofwave | Shallower dermal heating for wrinkles/lifting indications | FDA-cleared clinic ultrasound with cooling, but different from Ulthera's 4.5 mm visualized stack |
| Body-contouring HIFU | Subcutaneous adipose disruption | Not a facial lifting analog; e.g. SCIZER is waist-circumference reduction at 13 mm focal depth [[6]](source_docs/fda-k230100-classys-scizer.pdf) |
| Home HIFU/MFU | Consumer maintenance claims | Not verified as a low-density version of any clinic protocol in this source pass |

## 5. Why the fractional-laser analogy breaks

The fractional-laser folder can compare home and clinic devices by a reasonably shared concept: fractional optical columns. A home fractional laser may be weaker, lower density, shallower, slower, or less complete, but the device family can still be described with wavelength, spot size, pulse energy, microbeam density, coverage, and treatment area.

For HIFU/MFU, "same mechanism but less density" is not enough. The most important variables are not simply number of shots:

- focal depth and focal-zone geometry;
- coupling quality and gel layer;
- acoustic path through curved facial anatomy;
- layer selection;
- spacing between lines and TCPs;
- avoidance of bone, thyroid, vessels, nerves, and orbital zones;
- operator training and response to adverse effects.

That is why this folder treats home HIFU as a consumer ultrasound-maintenance category unless proven otherwise, not as a budget Ultherapy clone.

## 6. What home-device evidence can and cannot show

The PubMed-indexed home-used HIFU mouse paper is a useful signal that a small ultrasound device can affect dermal thickness and collagen-related markers under controlled experimental conditions [[7]](https://pubmed.ncbi.nlm.nih.gov/36704876/). But the study used mouse backs, not human faces; it tested histology and markers, not blinded human lifting outcomes; and it does not establish safe user technique around eyes, jawline, thyroid, facial fat, or nerves.

So the evidence is not "home HIFU is fake." The more accurate read is: **home HIFU has plausible biology, but the current public evidence does not establish clinic-equivalent facial lifting or a safe self-treatment protocol.**

## 7. Safety physics in one paragraph

HIFU gets its value from depositing energy below the surface. That is also the risk. The same focused energy that can create a collagen-remodeling injury can create burns, scarring, nerve symptoms, fat/volume loss, focal atrophy, or unwanted contour change if it lands in the wrong place or repeats too aggressively. Ulthera's IFU and the MFU-V adverse-event review both make that risk boundary real enough to respect [[2]](source_docs/ulthera-us-instructions-for-use-2021.pdf)[[8]](https://pubmed.ncbi.nlm.nih.gov/39625163/).

## Sources

1. FDA K072505 / De Novo classification order for Ulthera. [Local PDF](source_docs/fda-k072505-ulthera-de-novo-classification.pdf) - FDA's generic device description for focused ultrasound aesthetic use.
2. Ulthera System Instructions for Use, 2021. [Local PDF](source_docs/ulthera-us-instructions-for-use-2021.pdf) - Transducer depths, TCP spacing, DeepSEE imaging, SPT mode, and adverse-event warnings.
3. FDA K260618, Ulthera expanded knee indication. [Local PDF](source_docs/fda-k260618-ulthera-prime-2026.pdf) - DeepSEE visualization to 8 mm and current captured indications.
4. FDA K191421, Sofacia/Sofwave facial lines and wrinkles. [Local PDF](source_docs/fda-k191421-sofacia-sofwave.pdf) - Sofwave/Sofacia depth, cooling, and initial wrinkle indication.
5. FDA K211483, Sofwave lifting indications. [Local PDF](source_docs/fda-k211483-sofwave-lifting-indications.pdf) - Sofwave eyebrow and submental/neck indications.
6. FDA K230100, Classys SCIZER. [Local PDF](source_docs/fda-k230100-classys-scizer.pdf) - HIFU waist-circumference reduction and 13 mm fat-layer focus.
7. PubMed 36704876, home-used HIFU mouse wrinkle study. https://pubmed.ncbi.nlm.nih.gov/36704876/ - Mouse-back study using 4 MHz / 1.5 mm focal-depth home-used HIFU.
8. PubMed 39625163, MFU-V adverse-event review. https://pubmed.ncbi.nlm.nih.gov/39625163/ - Review of literature and MAUDE reports including lipoatrophy, neurologic sequelae, and scarring.
