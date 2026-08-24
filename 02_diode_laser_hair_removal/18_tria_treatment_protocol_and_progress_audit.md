# Tria treatment protocol and progress audit

*Decision aid updated 2026-08-23. Follow the manual for the exact 4X or Precision unit in hand. This page organizes the archive’s primary files; it does not replace clinical advice or the IFU.*

## Bottom line

The diode-laser topic already answers which used Tria to buy, how 810 nm differs from IPL, and how pulse geometry changes heating. The missing practical layer was a **post-purchase protocol that separates adherence, coverage, device condition, and biological response**.

For a Tria 4X, the current archived IFU says to treat the same area every two weeks for up to three months (or until the desired reduction), after a 24-hour patch test. Its cited clinical study reported average hair-count reductions of 61% three weeks after treatment 1, 70% after treatment 2, 60% one month after treatment 3, and 33% twelve months after treatment 3. Those are study averages after only three treatments—not a personal guarantee and not proof of complete permanent removal. [[1]](Tria_4X_IFU_2ndGen_current.pdf)

## 1. Eligibility and preflight

Do not begin until every item is true:

- The hair is naturally brown or black; the manual excludes white, gray, blond, and red hair because there may be too little target pigment.
- The skin passes the exact unit’s skin sensor and falls within its labeled light-to-medium range. Never defeat the sensor.
- The treatment area is allowed by the manual. Do not use around the eyes, on the ears/nipples/genitals/anus, on dark spots or lesions the IFU excludes, or over tattoos.
- There is no manual-listed medicine, photosensitivity, pregnancy, skin condition, recent procedure, infection, or impaired-healing reason to stop and ask a clinician.
- Hair has been removed by shaving as directed. Waxing, plucking, or epilating can remove the chromophore the laser needs; the Precision IFU directs users to stop those methods six weeks before treatment. [[2]](Tria_Precision_IFU_HRLp.pdf)
- A representative patch test was completed on this body area and observed for 24 hours. Repeat after a meaningful tan or other change in skin status. [[1]](Tria_4X_IFU_2ndGen_current.pdf)

## 2. The 12-week treatment plan

| Week | Action | What to record |
|---|---|---|
| 0 | Baseline photos in fixed light; count hairs in a small marked audit square; patch test; first full treatment if passed | Model/serial, battery behavior, level, area, pulses, minutes, pain 0–10, immediate response |
| 2 | Treatment 2 | Same fields; note missed lanes, shutdowns, or sensor refusals |
| 4 | Treatment 3 | Same fields; repeat standardized photo and audit-square count before shaving |
| 6 | Treatment 4 | Same fields; distinguish true regrowth from hairs shedding after treatment |
| 8 | Treatment 5 | Same fields; check whether usable pulses/session or battery endurance has changed |
| 10 | Treatment 6 | Same fields; do not add sessions to compensate for weak response |
| 12 | Primary audit | Fixed-light photo, audit-square count, hair caliber/spacing notes, adverse effects, and device-health summary |
| 24+ | Optional durability audit | Same photo/count without pretending a short-term shed is permanent reduction |

The companion [progress-log template](data/tria_progress_log_template.csv) is intentionally device-agnostic enough for 4X or Precision, but it keeps body areas separate so a strong underarm response cannot hide a weak leg response.

## 3. Coverage without stacking

The archived 4X quick-start guide estimates roughly 25 pulses for the upper lip, 100 per underarm, 200 per bikini side, and 600 per upper or lower leg side, with about 5 mm (¼ inch) overlap. Treat those numbers as **coverage checks**, not dose targets: body size and exact boundary differ, and firing extra pulses on a completed spot is not beneficial. [[3]](source_docs/tria_4x_manual_timeline/2017_Tria_4X_QSG_15017B_Channel.pdf)

Use lanes:

1. Divide the area into small strips.
2. Place the circular treatment window flat.
3. Advance by the manual’s overlap distance, once per position.
4. If interrupted, mark the last completed lane rather than restarting the area.
5. Record actual pulses and time; a large unexplained fall usually means incomplete coverage, battery limitation, or a smaller boundary.

Higher settings can improve efficacy, but the correct setting is the highest **tolerable and permitted** level—not the highest number at any cost. The quick-start guide says levels 2–3 were two to three times more effective than level 1 in the referenced data, while the IFU also documents mild-to-moderate pain/discomfort as common. [[1]](Tria_4X_IFU_2ndGen_current.pdf) [[3]](source_docs/tria_4x_manual_timeline/2017_Tria_4X_QSG_15017B_Channel.pdf)

## 4. The week-12 audit

### A. Adherence

- Were sessions actually 14 ± 2 days apart?
- Was hair shaved rather than pulled from the follicle?
- Were settings and coverage reasonably stable?
- Were sun exposure and new products/procedures documented?

### B. Device health

- Does the unit reach a full charge and complete a comparable area?
- Are shutdowns heat-related and recoverable, or worsening across sessions?
- Is the fan/exhaust clear, treatment window intact, and contact/sensor behavior stable?
- Did total pulses fall despite the same mapped area?

Use the [post-repair shutdown diagnosis](index.html#doc5) if a Precision repeatedly cuts out, and the [4X-versus-Precision guide](index.html#doc4) before attributing normal form-factor limits to a fault.

### C. Biological response

Compare only standardized, pre-shave observations:

- hair count within the same marked audit square;
- spacing/density, not just a favorable photo angle;
- proportion of visibly finer or lighter regrowth;
- time until stubble becomes visible;
- persistent erythema, blistering, crusting, pigment change, or other adverse effects.

### Decision

| Finding | Interpretation | Next step |
|---|---|---|
| Clear count/density improvement, tolerable skin response, stable device | Protocol is producing a signal | Complete the labeled course, then use only IFU-supported touch-ups |
| No clear change, but irregular cadence or under-coverage | Execution failure remains plausible | Correct one variable and repeat a predeclared audit interval; do not stack pulses |
| No clear change despite good adherence, eligible hair/skin, and stable device | Nonresponse or endpoint mismatch is plausible | Stop escalating and reassess expectations/device choice |
| Worsening shutdowns, reduced endurance, or inconsistent triggering | Hardware/battery condition may confound outcome | Diagnose/repair or replace before judging efficacy |
| Burn-like response, blistering, prolonged redness, or pigment change | Safety endpoint failed | Stop treatment and follow the IFU/seek medical assessment as appropriate |

## Evidence gaps

- The archived Tria outcomes are manufacturer-submitted clinical data with no untreated control described in the consumer IFU.
- Hair-count timing matters; transient shedding can exaggerate short follow-up improvement.
- Response varies by body area, hair caliber, hormone status, skin tone, delivered level, and coverage.
- Used-device battery condition and optical output are rarely measured independently.
- The pulse-count examples are approximate coverage aids, not validated personalized dosing.

### Sources

1. [Archived Tria Hair Removal Laser 4X current IFU](Tria_4X_IFU_2ndGen_current.pdf) — primary instructions, contraindications, 24-hour patch test, two-week cadence, clinical-study outcomes, and adverse reactions.
2. [Archived Tria Precision IFU](Tria_Precision_IFU_HRLp.pdf) — primary Precision eligibility, hair-removal preparation, patch testing, cadence, and touch-up guidance.
3. [Archived 2017 Tria 4X quick-start guide](source_docs/tria_4x_manual_timeline/2017_Tria_4X_QSG_15017B_Channel.pdf) — manufacturer pulse/time approximations, overlap guidance, and level-effect statement.
4. [Archived older Tria 4X IFU](Tria_4X_IFU_older.pdf) — version comparison source; use the manual matching the exact device/version.
