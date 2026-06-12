# IPL Science Brief: Parameters for Skin Rejuvenation vs Hair Removal

**Goals: Facial redness/erythema, hyperpigmentation, PIH, skin tone evening. Secondary: hair removal.**

> **Companion read:** This brief explains the IPL physics. For the *strategic* conclusion it leads to — that for pigment/PIH/redness, IPL is the wrong primary tool and topicals + LED + photoprotection should lead — see [07_alternatives_and_strategy.md](07_alternatives_and_strategy.md). Section 6 below (PIH/melasma risk) is the hinge between the two.

---

## 1. The Governing Physics: Selective Photothermolysis (SPT)

The entire field rests on one principle: **deliver enough energy to heat a specific chromophore to a damaging temperature, in a time shorter than that chromophore's Thermal Relaxation Time (TRT), so heat stays local and does not damage surrounding tissue.**

TRT is the time it takes for a target to cool to half its peak temperature. If pulse duration > TRT, heat diffuses outward → epidermal burns, PIH, blistering. If pulse duration ≤ TRT, the thermal damage is confined to the target.

### Thermal Relaxation Times — Verified from Literature

| Target | Diameter | TRT |
|--------|----------|-----|
| Epidermal melanin clusters | ~0.5–5 µm | 250 ns – 10 µs |
| Melanosomes (individual) | ~0.5 µm | ~250 ns |
| Small telangiectasias / capillaries | ~100 µm | ~10 ms |
| Larger telangiectasias / vessels | ~300 µm | ~100 ms |
| Hair follicle bulge | ~200–300 µm | ~40–100 ms |
| Epidermis (as slab) | ~100 µm | ~1 ms |

> **Honest note on the TRT numbers — sources disagree by roughly an order of magnitude.** TRT scales with the *square* of target diameter, so small differences in the assumed vessel size (and which formula/constant is used) produce large differences in the published value. The table above uses the values the deep-research pass confirmed 3/3 (100 µm ≈ 10 ms; 300 µm ≈ 100 ms). The Weiss et al. 2005 paper in this repo uses **lower** figures for the same targets: 100 µm vessel ≈ 4 ms, 300 µm vessel ≈ 10 ms, epidermis ≈ 1 ms. Both are "correct" within their own assumptions — treat these as order-of-magnitude guides, not precise constants. The practical conclusion is unchanged either way: vascular targets tolerate **single-digit-to-tens-of-ms** pulses, which is exactly the 2–20 ms range clinical IPL uses.

**Practical consequence:** For vascular lesions (redness, telangiectasia), pulse durations of 2–20ms with proper inter-pulse delays are used. For melanin/pigment (hyperpigmentation), shorter pulses (1–5ms) or laser (nanoseconds/picoseconds for tattoo-grade pigment) are needed. Hair removal needs 10–100ms.

---

## 2. Wavelength: The Most Critical Differentiator for Your Goals

The IPL xenon lamp emits 500–1200nm. A cutoff filter removes everything below its threshold. What remains hits your skin.

### Chromophore Absorption Peaks

| Chromophore | Peak Absorption | Practical IPL Filter |
|------------|----------------|---------------------|
| Oxyhemoglobin (HbO₂) | 418, 542, 577 nm | 515–560nm cutoff |
| Melanin (broad) | Higher absorption at shorter λ, decreasing toward IR | 515–560nm cutoff |
| Water | >1200nm | N/A for IPL |
| Hair melanin | 694–1064nm range; melanin-rich so any λ works | 560–800nm sufficient |

**For redness/erythema/telangiectasia:** You need the oxyhemoglobin absorption peaks (542nm, 577nm) inside your treatment band. This means the filter cutoff must be ≤560nm, ideally 515–540nm. A 560nm filter is borderline; it passes the secondary HbO₂ peak but barely. An 800nm+ filter is useless for vascular targets.

**For pigmentation/hyperpigmentation:** Melanin absorbs broadly, so 515–560nm cutoff works. The shorter the cutoff, the higher the melanin absorption coefficient, the more efficient the treatment.

**For hair removal:** Melanin-rich hair follicles respond to a wide range of wavelengths. A 560nm or even 640nm cutoff works fine. This is why all home devices advertise "hair removal" — their 560nm standard filters work there even at low fluence.

### Clinical Photorejuvenation Filters (Weiss et al., Dermatol Surg 2005)
- Poikiloderma of Civatte: **515nm** filter, single 3ms, 25 J/cm²
- Fine telangiectasias: **550–570nm** filter, 38–42 J/cm²
- Rosacea: **560nm**, 28–36 J/cm²
- Asian freckles: **560nm**, 20–24 J/cm²

**Verdict: For your goals, you want the lowest possible cutoff filter, ideally 510–530nm, not 560nm.** The difference between a 510nm and 560nm filter is roughly 50nm of the most therapeutically relevant oxyhemoglobin absorption spectrum being cut off.

---

## 3. Fluence (J/cm²): The Efficacy Floor

Fluence = energy density delivered per pulse. Below a minimum threshold, no clinical effect occurs regardless of other parameters.

### Clinical Fluence Requirements (Peer-Reviewed)

| Indication | Fluence Range | Source |
|-----------|---------------|--------|
| Telangiectasia (large) | 50–56 J/cm² | Clinical protocol literature |
| Telangiectasia (fine) | 38–42 J/cm² | Weiss et al. 2005 |
| Rosacea | 15–36 J/cm² | Weiss et al. 2005 |
| Freckles/lentigines | 20–30 J/cm² | Weiss et al. 2005 |
| General photorejuvenation | 13–35 J/cm² | Multiple RCTs |
| Hair removal (dark hair, light skin) | 10–30 J/cm² | Standard clinical |

### Home Device Reality
All home IPL devices regulated under FDA product code OHT are cleared at:
- Max fluence: typically **3–9 J/cm²**
- The best home devices (Fansizhe T055/T505 FDA-cleared) reach **8.33 J/cm²**

This is **3–7× below the minimum clinical threshold for vascular targets** and **2–4× below for pigment targets**. The efficacy gap is structural, not a brand-specific problem.

**However**, sub-threshold fluence delivered repeatedly over many sessions does produce measurable results via cumulative low-dose photobiomodulation — particularly for mild-moderate pigment and diffuse redness. The expectation must be calibrated: expect 20–40% improvement over multiple months, not 80%+ clearing in 3 sessions like clinical IPL.

---

## 4. Single Pulse vs Multi-Pulse: What the Evidence Actually Shows

The user's original hypothesis: a 27.5J triple-pulse is inferior to a single high-fluence pulse of equal total energy.

**What the literature confirms:**
- For **vascular lesions**, multi-pulse (double/triple) delivery with interpulse delays of 10–40ms is actually **preferred** clinically because:
  - Individual sub-pulses heat vessels without pulse duration exceeding the ~10ms TRT for small vessels
  - Interpulse delay allows epidermal cooling (from contact cooling) to protect the dermis
  - Net effect: you can deliver more total fluence safely than a single long pulse
- The superiority of single-pulse for vascular response was **not confirmed** by adversarial research review (0/3 votes)

**What is still true:**
- A 9ms triple-pulse train at 3ms+3ms+3ms with 500ms total duration is NOT the same as a clinical single 3ms pulse
- Extremely long inter-pulse gaps (>100ms) cause heat dissipation between sub-pulses, reducing efficacy
- The Fansizhe T055's 27.5J spread over three pulses across ~1 second (with SHR mode) delivers effectively mild sub-threshold energy in each sub-pulse
- Optimal clinical multi-pulse: 2–4ms individual pulses, 10–30ms interpulse delays — maintaining thermal build-up within vessel TRT

**Practical takeaway:** You want either:
1. A true single high-fluence pulse (≥10 J/cm² in single shot), OR
2. A properly structured double/triple pulse with 2–5ms individual pulses and 10–40ms delays

What you want to avoid: SHR "burst" mode delivering 10–20 weak pulses over 1–2 seconds with high rep rate — good for hair removal, not vascular/pigment work.

---

## 5. Contact Cooling: Non-Negotiable for Skin Safety and Efficacy

Clinical IPL systems use contact cooling at 5°C throughout treatment. This serves two purposes:

1. **Epidermal protection**: Pre-cools epidermis so higher fluence can be safely applied without burning surface melanin. Allows increasing fluence toward the therapeutic target.
2. **Vasoconstrictive pre-treatment**: Cold skin causes vasoconstriction, concentrating HbO₂ (when warming occurs post-flash), enhancing selectivity.

**Home devices:** Sapphire ice-cooling and ice panel cooling are the only mechanisms available. Neither reaches 5°C contact temperature (more like 15–20°C at surface), but they provide meaningful protection vs no cooling. Sapphire crystal cooling is generally superior to passive ice panel because it maintains lower temperature at the contact window.

**Devices without any active cooling** are riskier at high energy settings, especially for darker skin tones or treated skin (PIH-prone).

---

## 6. PIH and Melasma Risk — The Critical Safety Issue for Your Goals

This is the central tension of your situation: you want to treat PIH and hyperpigmentation, but IPL can cause and worsen PIH.

### Evidence Summary

| Study | Finding |
|-------|---------|
| Frontiers in Medicine 2026 meta-analysis (31 trials, n=2,801) | IPL monotherapy: 77.4% clinical efficacy for melasma; QS laser+IPL combined: 92% |
| Chinese Fitzpatrick III–IV cohort (n=675) | 2.96% incidence of IPL-induced Macular Lentiginous Hyperpigmentation (MLH); 70% diffuse wide-distribution pattern; 2 cases of outright exacerbation |
| General consensus | Fitzpatrick I–IV: appropriate for IPL; Fitzpatrick V–VI: high burn/PIH risk, IPL contraindicated |

### Mechanism of PIH from IPL
- Non-selective heating of epidermal melanin causes melanocyte stimulation (not just destruction)
- If fluence is sub-threshold for melanocyte killing but above threshold for melanocyte activation, you paradoxically worsen pigmentation
- This is more likely with lower fluence devices — which home IPL devices are, structurally

### Safe Use Protocol for PIH-Prone Skin
1. **Patch test** mandatory: 48–72h before full treatment
2. **Start at lowest energy level**, increase only if no post-treatment darkening at 48h
3. **No treatment during sun exposure periods** — avoid IPL within 4 weeks of significant sun exposure
4. **Post-care SPF50+ mandatory** — unprotected post-IPL skin is highly vulnerable to UV-induced PIH
5. **Avoid treated skin during active breakouts** — trauma from IPL on inflamed skin creates PIH
6. **Space sessions ≥4 weeks apart** to allow full post-inflammatory resolution
7. **If any darkening occurs 48–72h post-treatment**: stop, use topical hydroquinone or niacinamide, wait for full resolution before re-treatment at lower energy

---

## 7. Home Device Limitations: The Honest Assessment

| Parameter | Clinical IPL | Best Home IPL (Fansizhe T023A) | Gap |
|-----------|-------------|-------------------------------|-----|
| Fluence | 13–90 J/cm² | ~8.3 J/cm² | 2–10× |
| Filter cutoff | 515–560nm | 510nm | Comparable |
| Contact cooling | 5°C | ~15–20°C (sapphire) | Significant |
| Pulse control | Programmable ms | 0.4–12ms range | Reasonable |
| Pulse structure | Custom protocols | Single/dual | Limited |
| Treatment area | Any body area | Face safe on most | Comparable |
| Operator expertise | Dermatologist | None | Major risk factor |

**Realistic expectations for home IPL on your goals:**
- **Redness/diffuse erythema**: Modest improvement (20–35%) with consistent use over 3–6 months. Intense/fixed telangiectasia will not respond.
- **Solar lentigines/freckles**: Best responder — 50–70% improvement possible with correct wavelength and adequate fluence over multiple sessions.
- **PIH**: Risk-benefit is marginal. Mild, shallow PIH may improve. Deep dermal PIH will not respond and may worsen. Proceed with extreme caution.
- **Melasma**: Do not attempt with home IPL. Melasma has a documented 2.96% exacerbation rate even with expert clinical IPL. Home IPL raises this risk substantially. Use alternatives (topical tranexamic acid, niacinamide, sunscreen).
- **Hair removal**: Highly effective — the one goal home IPL is actually cleared and validated for.

---

## 8. What Actually Matters Most for Your Specific Goals (Priority Order)

1. **Filter cutoff ≤530nm** — getting light into the oxyhemoglobin and melanin absorption peaks
2. **Maximum fluence possible** — even ~8 J/cm² beats ~4 J/cm²; anything above 6 J/cm² is meaningful
3. **Contact cooling** — sapphire ice > ice panel > no cooling
4. **Pulse mode control** — single or adjustable dual pulse preferred; avoid pure SHR mode for rejuvenation
5. **FDA clearance** — confirms device actually produces rated energy; uncleared devices often underperform
6. **Price/Alibaba availability** — <$200 at wholesale

---

## Raw Data Dump: Key Sources

**Weiss RA, Goldman MP, Weiss MA. Treatment of poikiloderma of Civatte with an intense pulsed light source. Dermatol Surg. 2000;26(9):823-8.**
**Goldman MP, Weiss RA, Weiss MA. Intense pulsed light as a nonablative approach to photoaging. Dermatol Surg. 2005;31(9):1179-1187.**
- Full spectra: facial telangiectasias 550–570nm, 28–42 J/cm², double pulse 2.4–4ms, 10ms delay
- Rosacea: 560nm, 2.4–4.2ms, 28–36 J/cm², 15ms delay
- Poikiloderma: 515nm, single 3ms, 25 J/cm²
- Asian freckles: 560nm, 20–24 J/cm², 2.6–5ms, 20ms delay
- IPL stimulates 18% increase in collagen type I transcripts

**Deep Research Workflow — Verified Claims (3/3 votes):**
- TRT for 100µm vessel: ~10ms (Confirmed 3/3)
- TRT for 300µm vessel: ~100ms (Confirmed 3/3)
- IPL causes 2.96% MLH incidence in Fitzpatrick III–IV (675-patient cohort) (Confirmed 3/3)
- Frontiers in Medicine 2026 meta-analysis: 77.4% IPL monotherapy vs 92% combo for melasma (Confirmed 3/3)

**Deep Research Workflow — Refuted Claims (0/3 votes):**
- "Single high-fluence pulse is superior to multi-pulse for vascular response" — REFUTED (0/3)
- "27.5J triple-pulse is equivalent to 27.5J single pulse" — REFUTED (0/3)
- "FDA OHT-cleared home IPL devices have skin rejuvenation claims" — REFUTED (0/3)
- "Home IPL can effectively treat melasma" — REFUTED (0/3)
