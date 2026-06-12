# IPL Device Research

Research project: choosing a light-based device (budget <$200, Alibaba/retail) for **facial redness/erythema, hyperpigmentation, post-inflammatory hyperpigmentation (PIH), and evening skin tone** — with **hair removal as a secondary goal**.

## TL;DR

1. **For the PRIMARY goal (pigment/PIH/redness), a home IPL device is the wrong primary tool.** Broadband IPL can *worsen* pigmentation in pigment-prone skin (~2.96% IPL-induced hyperpigmentation in Fitzpatrick III–IV). Lead instead with **iron-oxide tinted sunscreen + topicals (azelaic acid, tranexamic acid, niacinamide) + non-thermal LED (red 630–660nm / amber ~590nm)**. See **[doc 07](07_alternatives_and_strategy.md)**.
2. **No home IPL device — branded or Chinese OEM — is FDA-cleared for anything but hair removal** (all are product code OHT). Verified from the actual filings. See **[doc 03](03_fda_510k_analysis.md)**.
3. **If buying a device for the secondary hair goal:** best OEM target = **Fansizhe T023A** (510nm filter, sapphire cooling, FDA K223928 baseline 5.5 J/cm²; catalog claims 8.33 J/cm² if seller verifies 25J single-pulse output). Budget single-pulse fallback = **Fansizhe T001M/T001A**. Lowest-risk branded option = **Nood Flasher 2.0** ($169, FDA-cleared, 510nm, warranty). See **[doc 06](06_final_recommendation.md)** + **[doc 07 §5](07_alternatives_and_strategy.md)**.
4. The rejected **T055** was the right call to reject (560nm filter misses hemoglobin peaks; its big "27.5J" is summed multi-pulse marketing — FDA-cleared spec is 25J / 8.33 J/cm²).

## Documents

| # | File | What it covers |
|---|------|----------------|
| 01 | [Science brief](01_science_brief.md) | Selective photothermolysis, TRT, wavelength/chromophore physics, clinical fluence, PIH risk, home-device limits |
| 02 | [Ideal device specs](02_ideal_device_specs.md) | Target spec sheet, scoring matrix, Alibaba red flags |
| 03 | [FDA 510(k) analysis](03_fda_510k_analysis.md) | K223928/K251173/K253881/K260518 verified specs, predicate/reference devices (Ulike, IONKA), why OHT ≠ rejuvenation |
| 04 | [Fansizhe catalog](04_fansizhe_catalog_transcription.md) | Every Fansizhe model, specs, fluence, FDA status |
| 05 | [Semlamp catalog](05_semlamp_catalog_transcription.md) | Every Semlamp model, "age spot" filter heads, certs |
| 06 | [Final device recommendation](06_final_recommendation.md) | Ranked IPL picks for the hair goal + usage/safety protocol |
| 07 | [Alternatives & strategy](07_alternatives_and_strategy.md) | **The reframe**: DPL vs IPL, LED, topicals-first, branded vs OEM, evidence-based plan |

## Source PDFs (in repo)
- `FDA_510k_K221569_Fansizhe_T013C_T015C_T015K.pdf` — Fansizhe 510nm predicate, cleared 2022 (T013C/T015C/T015K, 510nm, 4.03 J/cm²)
- `FDA_510k_K223928_Fansizhe_T023_T021_T001_T011_T016.pdf` — Fansizhe 510nm family, cleared Mar 28 2023 (T023/T021/T001/T011/T016, 510nm, up to 5.75 J/cm²)
- `FDA_510k_K251173_Fansizhe_Original_Clearance.pdf` — Fansizhe original 2025 FDA 510(k), cleared Jul 14 2025 (T033/T055/T002/T050, 560nm, ≤5.4 J/cm²)
- `FDA_510k_K253881_Fansizhe_Upgrade_Clearance.pdf` — Fansizhe Special 510(k), cleared Dec 29 2025 (T033/T055/T505/SL-B505WM, 560nm, ≤8.48 J/cm², triple-pulse)
- `Weiss_IPL.pdf` — Goldman/Weiss/Weiss, *Dermatol Surg* 2005, clinical IPL photoaging parameters
- `Fansizhe_Product_Catalog_2025.pdf` — Fansizhe product catalog (English, 45pp)
- `Semlamp_Product_Catalog_English.pdf` — Semlamp product catalog

## Web Sources Added In Latest Pass
- [FDA K260518](https://www.accessdata.fda.gov/scripts/cdrh/cfdocs/cfpmn/pmn.cfm?ID=K260518) — Semlamp direct clearance, cleared Apr 21 2026 (SL-B352 family included, OHT hair removal only)

## Status / open items
- Verified against primary sources (FDA filings, catalog transcriptions, and current FDA AccessData pages).
- **Open:** real Alibaba per-unit pricing, MOQ, and single/sample-unit availability for the OEM models were not confirmed — prices in docs 02/06 are estimates. The branded Nood/Ulike route avoids the MOQ question entirely.
