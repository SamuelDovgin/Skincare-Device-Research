# SHR Mode, Ulike, and Successive Flashes — an Interactive Follicle-Heating Model

**The question:** Ulike (and most home-IPL brands now) markets an **"SHR mode"** — Super Hair Removal — that fires *successive low-energy flashes* instead of one strong pulse, on the promise that the heat "accumulates" to a higher effective dose and destroys the follicle more gently. Does that actually work at the follicle, and can you *see* whether a given set of parameters crosses the threshold for real hair damage? This doc explains the physics, pins down what Ulike's SHR actually delivers, and pairs with an **interactive simulator** where you set the flash energy, count, timing, skin tone and hair type and watch the epidermis, the follicle, and the deep stem-cell target each heat up — and whether any of them crosses the damage line.

> 🔥 **[▶ Open the interactive SHR & Multi-Flash Thermal Simulator](shr_thermal_simulator.html)** — pick an FDA-pulse-width-verified device (or go manual), set energy per-flash **or as one total that splits across your pulse count**, and watch the epidermis, follicle, and deep stem-cell target heat up live. It flags whether the follicle crosses the damage threshold **and** whether the **skin crosses its burn threshold** (driven by fluence, pulse width, skin tone & cooling), and compares a single flash to a multi-flash train. (Open `shr_thermal_simulator.html` in a browser, or via the 🔥 tool link in the IPL viewer.)

> ⚠️ Not medical advice. This synthesizes peer-reviewed laser/IPL-physics literature, Ulike's own published specs plus third-party technical reviews, and this repo's device research. The simulator is a **teaching model** — an illustrative lumped-parameter thermal integrator calibrated to published TRT/TDT values — not a validated Monte-Carlo simulation. Use it for intuition about **timing and stacking**, not to predict a number for your skin. This is the *millisecond-to-second* flash-timing question — a different timescale from the week-to-week **session cadence** in [12_treatment_cadence_guide.md](12_treatment_cadence_guide.md), and a companion to the device-specific [15_multi_flash_thermal_accumulation.md](15_multi_flash_thermal_accumulation.md).

---

## ⭐ The honest bottom line (read this first)

**"Successive flashes add up" is real physics — but only inside a timing window, and Ulike's home SHR mostly sits *outside* it on any single pass.** Three findings, all reproduced in the simulator:

1. **There are two different ways light damages a follicle, and SHR bets on the harder one.** A single strong flash spikes the follicle past ~65 °C and coagulates it *immediately* (the **peak pathway**). SHR instead keeps the follicle warm-but-not-hot and lets a **cumulative dose** build in the deep, unpigmented stem-cell target over time (the **accumulation pathway**). The accumulation pathway is gentler on skin — but it only pays off if the flashes arrive **faster than the target cools**.

2. **Ulike's SHR cadence (~4 flashes/second, ~250 ms apart) is far slower than the follicle's ~10–100 ms cooling time**, so successive flashes do **not** stack into a higher follicle *peak* — each one largely resets. That's exactly why it's "nearly painless," and also why, on a single pass at ~1.7 J/cm² per sub-flash, the model shows it landing **sub-threshold**. Professional SHR works because it uses **higher fluence (5–15 J/cm²) at ~10 Hz** — enough to hold a sustained plateau; the home version is a scaled-down, comfort-first cousin.

3. **Home SHR's real-world results come from *repetition*, not from any single burst clearing threshold** — many overlapping passes per session, 8–12 sessions, and possibly a non-thermal apoptotic pathway that shows up in the histology.[[12]](https://pmc.ncbi.nlm.nih.gov/articles/PMC5515709/) The clinical evidence is genuinely reassuring on *outcome* (SHR ≈ single-pass efficacy, with much less pain), just not on the "each flash stacks to a bigger dose" story the marketing implies.

**Practical translation:** SHR mode is a legitimate **comfort** tool, not a shortcut to more dose. The most reliable lever remains the **highest comfortable single-flash fluence** plus finishing the full course — the same conclusion this repo reached for the Fansizhe triple-pulse mode in [15_multi_flash_thermal_accumulation.md](15_multi_flash_thermal_accumulation.md).

---

## 1. What "SHR mode" actually is — and what Ulike delivers

**SHR (Super Hair Removal)** originated on professional diode-laser platforms as an **"in-motion"** technique: instead of a few strong stamps, the operator glides the handpiece continuously while it fires **many low-fluence pulses at a high repetition rate (typically ~10 Hz)**, so any given follicle is hit by dozens of overlapping weak pulses over a several-second pass. The pitch is "gradual bulk heating": raise the follicle and its surrounding stem cells to a sustained ~45–48 °C rather than a sudden ~65–70 °C spike — less pain, less epidermal risk, works across more skin types.[[10]](https://ijdvl.com/methods-to-overcome-poor-responses-and-challenges-of-laser-hair-removal-in-dark-skin/)

Home brands have since adopted the "SHR" label. Here's what Ulike's flagship **Air 10** actually delivers, from its published specs and third-party teardown-style reviews:[[18]](https://www.scienceoverfluff.com/p/ulike-technical-review-and-results)

| Spec | Value | Note |
|---|---|---|
| Flash structure | Two xenon lamps firing up to twice each → **up to 4 flashes** per burst | "Four distinct peaks with partial cooling between flashes" |
| Burst energy | **≈26 J** total across the four flashes | Marketed headline energy |
| Effective fluence | **≈6.67 J/cm²** for the *whole four-flash burst* | ⇒ only **≈1.7 J/cm² per individual sub-flash** |
| SHR cadence | **≈4 flashes/second** (~250 ms apart) | The "stubborn hair" mode |
| AutoGlide cadence | **≈2 flashes/second** (~500 ms) | Continuous mode for large areas |
| Contact cooling | Sapphire tip held **≈20 °C** (68 °F) | Protects the epidermis; enables higher settings |

The Air 3 (and similar single-pulse home devices) instead fire **one stronger flash per press** — gentler to operate, but a real single-flash dose. This is the core fork the simulator lets you explore.

**The unit-collision to watch, exactly as in [15_multi_flash_thermal_accumulation.md](15_multi_flash_thermal_accumulation.md):** "26 J / 6.67 J/cm²" is an *accumulated total*, not a single-flash figure. Whether that total behaves like one 6.67 J/cm² dose or like four independent 1.7 J/cm² doses depends entirely on the **inter-flash timing** — which is the whole point of the model below.

---

## 2. Two clocks decide whether heat "sticks"

Everything hinges on **selective photothermolysis**: deliver energy faster than a target cools (its **Thermal Relaxation Time**, TRT) and the heat stays local and builds; deliver it slower and each dose dissipates before the next arrives.[[1]](https://pubmed.ncbi.nlm.nih.gov/6836297/) TRT scales with the *square* of target size, so it differs enormously by structure:

- **Epidermis (~3–10 ms):**[[2]](https://pmc.ncbi.nlm.nih.gov/articles/PMC5108992/)[[3]](https://www.ncbi.nlm.nih.gov/books/NBK580525/) sheds heat fast — the basis for pulse-splitting and contact cooling. Clinical IPL spaces sub-pulses **10–12 ms apart** specifically to let the epidermis clear this TRT (20–40 ms for darker skin).[[3]](https://www.ncbi.nlm.nih.gov/books/NBK580525/)
- **Hair follicle / shaft (~10–100 ms, terminal ≈100 ms):**[[4]](https://pmc.ncbi.nlm.nih.gov/articles/PMC9541334/)[[5]](https://pmc.ncbi.nlm.nih.gov/articles/PMC9239120/)[[6]](https://pmc.ncbi.nlm.nih.gov/articles/PMC7190465/) **This is the stacking threshold.** Gaps under it → flashes build a higher peak. Gaps over it → no peak gain.
- **Bulge stem-cell target — Thermal Damage Time (~170–1000 ms, optimal ≈400 ms):**[[7]](https://jcasonline.com/thermal-kinetic-selectivity-and-lasers/)[[8]](https://pubmed.ncbi.nlm.nih.gov/12030874/)[[9]](https://pubmed.ncbi.nlm.nih.gov/21417915/) the cells that must die for *permanent* reduction are unpigmented and physically separated from the melanin "heater." Heat has to **diffuse** to them, which takes hundreds of ms — the **accumulation window**. This is why "many pulses over ~1 second" can work when a single millisecond flash can't reach that deep.

The gap between the follicle's own cooling (~10–100 ms) and the time heat needs to be *sustained* to reach the stem cells (~170–1000 ms) is the entire physical case for multi-flash SHR. The named mechanism is **progressive photothermolysis**: *"Repeated and fast emission of pulses of low energy progressively heats the chromophore to temperatures of 45–50° over a period of time and safeguards the epidermis from overheating as opposed to a sudden rise in temperature to 65° in conventional systems."*[[10]](https://ijdvl.com/methods-to-overcome-poor-responses-and-challenges-of-laser-hair-removal-in-dark-skin/)

---

## 3. The two damage pathways, made visible

The simulator models three structures (epidermis, follicle/bulb, bulge stem cells) as coupled thermal compartments and reports which pathway, if any, reaches threshold:

- **Peak (coagulation) pathway — the single strong flash.** All the energy arrives at once; the follicle spikes past **~65 °C** and denatures immediately. Efficient and one-and-done, but the same peak lands on the epidermis, so it hurts more and needs strong cooling. Load the **Ulike Air 3** or **Fansizhe T023A** preset: one ~6 J/cm² flash drives the follicle to ~69 °C and crosses via this pathway.
- **Accumulation (SHR) pathway — many weak flashes.** Each flash is gentle (low, comfortable peak), but if they arrive faster than the deep target cools, the **stem-cell dose builds** across the train — sustained ~45–50 °C, the "gradual bulk heating" SHR sells. Load the **Pro SHR** preset: the follicle holds a sustained plateau *below* 65 °C while the green stem-cell curve climbs across the flash train and the cumulative dose crosses threshold — **damage without a painful spike.**

The failure mode sits between them: split the energy **too thin, too slow, or too few times** and *neither* pathway reaches threshold. Load **Ulike Air 10 — SHR** (250 ms cadence, ~1.7 J/cm²/flash): the follicle sawtooths at ~45 °C and fully resets between flashes; the deep dose barely moves. Now drag the **gap dial down to ~40 ms** and watch it flip toward threshold as stacking kicks in — the clearest demonstration that **timing, not total energy, is the hero variable.**

⚠️ A safety corollary the model flags: sub-threshold heat isn't automatically harmless. On hormonal areas (face/neck), under-dosing can provoke **paradoxical hypertrichosis** — coarser regrowth — so "barely warm" is not the same as "safe there." (See the paradoxical-regrowth notes in [cadence_planner.html](cadence_planner.html) and [12_treatment_cadence_guide.md](12_treatment_cadence_guide.md).)

---

## 4. What the clinical evidence actually says about SHR

SHR is the **one** multi-pulse technique with real hair-removal-specific trial data. The pattern is consistent: usually **comparable** to single-pass high fluence, occasionally better, and **reliably less painful** — and it always works via a many-pulses-in-motion delivery, never 2–4 stamps at a fixed spot.

| Study | Comparison | Result |
|---|---|---|
| Braun 2009 [[11]](https://pubmed.ncbi.nlm.nih.gov/19916262/) | SHR (5–10 J/cm², 10 Hz) vs. single-pass (25–40 J/cm², 1 Hz) | Comparable **86–91%**; SHR much less painful |
| Omi 2017 [[12]](https://pmc.ncbi.nlm.nih.gov/articles/PMC5515709/) | Dynamic 10 Hz/10 J/cm² vs. static 1 Hz/30 J/cm² | No significant difference (**41.4%**); long-term effect attributed to **apoptosis** |
| Koo 2014 [[13]](https://pubmed.ncbi.nlm.nih.gov/24752608/) | SHR in-motion vs. single-pass | 40.7% vs. 33.5% (n.s.); SHR significantly less pain |
| Li 2016 [[14]](https://pubmed.ncbi.nlm.nih.gov/27419804/) | SHR vs. high-fluence mode, same laser | SHR slightly better (**90.2% vs. 87%**), far less painful |
| Wanitphakdeedecha 2012 [[15]](https://pubmed.ncbi.nlm.nih.gov/21923659/) | Diode SHR vs. Nd:YAG single-pass high-fluence | Nd:YAG **won** (54.2% vs. 35.7%) — SHR isn't universally superior |
| Barolet 2012 [[16]](https://pubmed.ncbi.nlm.nih.gov/22437967/) | Low-fluence 15 J/cm² at 5 Hz | Significant permanent reduction after 4 monthly sessions |

Two honest caveats. First, **home** SHR uses per-pulse fluence (~1.7 J/cm²) far below the **5–15 J/cm²** in every one of these trials — so the trials validate the *technique*, not the specific home dose. Second, even the researchers who ran these studies aren't sure "gradual bulk heating" is the operative mechanism: Omi's histology attributed the durable effect to **"induced apoptotic cell death in the follicles rather than any other mechanism."**[[12]](https://pmc.ncbi.nlm.nih.gov/articles/PMC5515709/) The outcomes are real and reproduced; the *why* isn't fully settled.

And the dose lever remains the clearest signal in the home-device data: a home 810 nm laser dose-response found **7 J/cm² → 44%, 12 → 49%, 20 → 65%** hair reduction at 12 months.[[17]](https://pubmed.ncbi.nlm.nih.gov/22886431/) Higher single-flash fluence beats splitting energy thinner.

---

## 5. The device data — what's actually disclosed

You can only pick a device in the simulator if its **pulse width is disclosed in an FDA 510(k) filing** — otherwise you enter parameters manually. This is deliberate: it stops the tool from fabricating specs. The honest state of the data, pulled from this repo's [FDA data pipeline](fda_data_pipeline/) (`verified_specs.json`) and [03_fda_510k_analysis.md](03_fda_510k_analysis.md):

| Device (family) | FDA 510(k) | Max fluence | Spot | **Pulse width** | Modes | **Inter-pulse gap** |
|---|---|---|---|---|---|---|
| **Ulike** UI20 / Sapphire Air | K241998 | 6.67 J/cm² | 3.9 cm² | **0.88–3.20 ms** ✅ | single / dual / triple + SHR | ✗ not in filing (~250 ms marketed) |
| **Fansizhe** T023A *(repo pick)* | K223928 | 6.08 J/cm² † | 3.0 cm² | **4–12 ms** ✅ | single / dual | ✗ not disclosed |
| **Fansizhe** T033 / T055 | K253881 | 8.48 J/cm² ‡ | 3.3 cm² | **0.4–12 ms** ✅ | single / dual / triple | ✗ not disclosed |
| **Fansizhe** T013C / T015 | K221569 | 4.03 J/cm² | 4.0 cm² | **4–12 ms** ✅ | single | n/a |
| **Semlamp** SL-B352 family | K260518 | 6.41 J/cm² | 4.2 cm² | **0.7–3.6 ms** ✅ | single / dual / triple + **SHR button** | ✗ not disclosed |
| **IONKA / Chuangtong** FZ-608/100/200 | K230739 | 5.43 J/cm² | 3.0 cm² | **0.5–0.8 ms** ✅ | single | n/a |
| **Cyden** Flash&Go | K122280 | 5.0 J/cm² | 6.0 cm² | **5 ms** ✅ | single | n/a |

† Video-measured single flash (cleared family baseline 5.5 J/cm²). ‡ The 8.48 headline is a **summed** three-sub-pulse total, not a single-flash figure.

**The one spec nobody publishes is the inter-pulse gap** — the millisecond delay between sub-pulses in a dual/triple/SHR mode. It's the single most important number for whether multi-flash "accumulation" is real (Section 2), and it appears in **no** FDA filing, catalog, or manual found in this research. That's why the simulator flags it "not disclosed" and hands it to you. Ulike's ~250 ms is a *marketed SHR repetition* cadence (4 flashes/s), not a filed intra-burst gap. Many more Ulike-family and competitor filings exist (K250194, K251984, K260742, Mlay, Philips Lumea, Alovea…) but omit pulse width entirely, so they're reachable only via **Manual**.

## 6. How to use the simulator

Open **[shr_thermal_simulator.html](shr_thermal_simulator.html)**:

1. **Pick a device** from the dropdown (or a 🧪 illustrative scenario, or Manual). The panel shows exactly what's FDA-verified (green) vs. not disclosed (red).
2. **Feel the hero dial.** On the Ulike default, drag the **gap from 250 → 40 ms** — the single most important thing to see. Stacking appears as the gap drops under the follicle's cooling time.
3. **Check skin safety.** Watch the **Skin burn risk** gauge. Then shorten the **pulse width** (or pick IONKA's 0.5–0.8 ms), darken the skin, and turn **cooling off** — the epidermis climbs into the burn zone while the follicle barely changes, because the skin's short TRT makes it far more pulse-width-sensitive. This is why real devices pair short pulses with strong contact cooling.
4. **Split a total.** Switch energy input to **"Total energy (J) ÷ pulses"**, set the spot size, and enter e.g. **28 J across 3 pulses** (the Fansizhe T033 triple claim) — the tool divides it into per-flash fluence and shows whether the split can match one strong flash.
5. **Compare** single vs. multi with the checkbox, and try the **Pro SHR** scenario to see the accumulation pathway cross threshold without a painful peak.

Controls: energy (**per-flash J/cm²** or **total J ÷ pulses**) · **spot size** · **gap** (hero) · **flash count** · **pulse width** (drives skin safety) · **skin tone** · **hair coarseness** · **contact cooling** · single-flash compare. A built-in `SANITY()` self-test sweeps 10,000+ parameter combinations and asserts the physics stays monotonic and bounded (run it from the browser console).

---

## ⚠️ Evidence gaps — read before treating any output as settled

- **The model is illustrative.** It reproduces the *qualitative* physics (shapes, timing thresholds, tradeoffs) from published TRT/TDT values. Absolute temperatures and the "damage threshold" are deliberately conservative stand-ins; real follicle heating depends on melanin distribution, perfusion, spot size and optical scattering a lumped model can't resolve.
- **Ulike's exact intra-burst timing is not published.** "Four flashes with partial cooling between" is qualitative; the millisecond gap between the four sub-flashes of a single Air 10 burst isn't disclosed, so the "250 ms" figure is the *SHR-mode repetition* cadence, not necessarily the intra-burst gap.
- **Home SHR per-pulse fluence sits below the clinical SHR trial range** (5–15 J/cm²), so those trials validate the technique, not the home dose.
- **SHR's mechanism is still debated** — bulk heating vs. an apoptosis-driven pathway.[[12]](https://pmc.ncbi.nlm.nih.gov/articles/PMC5515709/)
- **TDT range disagreement:** 170–1000 ms (optimal ~400) vs. a narrower 200–400 ms simulation estimate.[[8]](https://pubmed.ncbi.nlm.nih.gov/12030874/)[[9]](https://pubmed.ncbi.nlm.nih.gov/21417915/)
- **No study directly compares single-pulse vs. fixed-spot multi-pulse for hair at matched total fluence** — the specific configuration home "accumulate" modes offer sits in a genuine gap between the evidence bases (see [15_multi_flash_thermal_accumulation.md](15_multi_flash_thermal_accumulation.md)).

---

## 📚 Sources

1. Anderson RR, Parrish JA. Selective photothermolysis. *Science* 1983;220:524-527. https://pubmed.ncbi.nlm.nih.gov/6836297/
2. Kono T, et al. Theoretical review of pigmented-lesion treatment in Asian skin. *Laser Ther* 2016 — basal-layer TRT 1.6–2.8 ms. https://pmc.ncbi.nlm.nih.gov/articles/PMC5108992/
3. Gade A, et al. Intense Pulsed Light (IPL) Therapy. *StatPearls* 2024 — inter-pulse delay 10–12 ms (20–40 ms darker skin). https://www.ncbi.nlm.nih.gov/books/NBK580525/
4. Byalakere Shivanna C, et al. FRAC3 vs long-pulse 1064 nm Nd:YAG hair removal. *J Cosmet Dermatol* 2022 — hair-shaft TRT 10–100 ms. https://pmc.ncbi.nlm.nih.gov/articles/PMC9541334/
5. Goel A, Rai K. Facial laser hair reduction. *J Clin Aesthet Dermatol* 2022 — terminal-follicle TRT 10–50 ms. https://pmc.ncbi.nlm.nih.gov/articles/PMC9239120/
6. Bhat YJ, et al. Laser treatment in hirsutism. *Dermatol Pract Concept* 2020 — terminal-hair TRT ≈100 ms. https://pmc.ncbi.nlm.nih.gov/articles/PMC7190465/
7. Altshuler GB, et al. Extended theory of selective photothermolysis. *Lasers Surg Med* 2001 (via JCAS summary) — Thermal Damage Time. https://jcasonline.com/thermal-kinetic-selectivity-and-lasers/
8. Rogachefsky AS, et al. Super-long-pulsed 810 nm diode & the concept of thermal damage time. *Dermatol Surg* 2002 — TDT 170–1000 ms; optimal ≈400 ms. https://pubmed.ncbi.nlm.nih.gov/12030874/
9. Ataie-Fashtami L, et al. Simulation of diode hair-removal thermal damage. *Photomed Laser Surg* 2011 — narrower 200–400 ms TDT for hair. https://pubmed.ncbi.nlm.nih.gov/21417915/
10. Arsiwala SZ, Majid IM. Overcoming poor responses in dark skin. *IJDVL* 2019 — progressive photothermolysis (45–50 °C). https://ijdvl.com/methods-to-overcome-poor-responses-and-challenges-of-laser-hair-removal-in-dark-skin/
11. Braun M. Low-fluence high-rep vs high-fluence low-rep 810 nm diode. *J Drugs Dermatol* 2009 — 86–91%, comparable. https://pubmed.ncbi.nlm.nih.gov/19916262/
12. Omi T. Static vs dynamic 810 nm diode hair removal. *Laser Ther* 2017 — no significant difference; apoptosis mechanism. https://pmc.ncbi.nlm.nih.gov/articles/PMC5515709/
13. Koo B, et al. Low-fluence multi-pass vs high-fluence single-pass 810 diode. *Lasers Surg Med* 2014. https://pubmed.ncbi.nlm.nih.gov/24752608/
14. Li W, et al. SHR vs HR 810 nm diode, axillary hair. *J Cosmet Laser Ther* 2016 — 90.2% vs 87%; less pain. https://pubmed.ncbi.nlm.nih.gov/27419804/
15. Wanitphakdeedecha R, et al. Diode SHR vs Nd:YAG single-pass. *JEADV* 2012 — Nd:YAG won (54.2% vs 35.7%). https://pubmed.ncbi.nlm.nih.gov/21923659/
16. Barolet D. Low-fluence high-rep diode, 12-month. *Lasers Surg Med* 2012 — 15 J/cm² @5 Hz, significant permanent reduction. https://pubmed.ncbi.nlm.nih.gov/22437967/
17. Wheeland RG. Home 810 nm laser dose-response. 2012 — 7/12/20 J/cm² → 44/49/65% at 12 mo. https://pubmed.ncbi.nlm.nih.gov/22886431/
18. Ulike Air 10 specifications (dual xenon, up to 4 flashes, ≈26 J burst, ≈6.67 J/cm², ~4 flashes/s SHR, sapphire cooling ≈20 °C) — manufacturer specs + third-party technical review. https://www.scienceoverfluff.com/p/ulike-technical-review-and-results
19. FDA 510(k) subject-device pulse-width specs (K241998 Ulike UI20 0.88–3.20 ms; K223928 Fansizhe 4–12 ms; K253881 0.4–12 ms; K260518 Semlamp 0.7–3.6 ms; K230739 IONKA 0.5–0.8 ms; K122280 Cyden 5 ms) — this repo's [FDA data pipeline](fda_data_pipeline/) `verified_specs.json` + [03_fda_510k_analysis.md](03_fda_510k_analysis.md), read directly from each 510(k) summary. Searchable at https://www.accessdata.fda.gov/scripts/cdrh/cfdocs/cfpmn/pmn.cfm

*Compiled 2026-07-01 (device-picker & skin-safety update). Numbered citations are peer-reviewed/StatPearls sources on TRT/TDT/SHR physics and the SHR clinical trials; Ulike device figures are from the manufacturer and a third-party technical review (source 18). Pairs with the interactive [shr_thermal_simulator.html](shr_thermal_simulator.html) and the device-specific analysis in [15_multi_flash_thermal_accumulation.md](15_multi_flash_thermal_accumulation.md).*
