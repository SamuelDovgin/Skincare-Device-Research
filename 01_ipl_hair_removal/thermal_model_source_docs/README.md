# IPL thermal-model source manifest

*Created 2026-07-10. These local files support the temperature/damage audit in [`16_shr_ulike_thermal_simulation.md`](../16_shr_ulike_thermal_simulation.md) and [`shr_thermal_simulator.html`](../shr_thermal_simulator.html).*

| Local file | Source and access | Evidence role |
|---|---|---|
| [`PMC6977020_photothermal_damage_rate_kinetics_fulltext.xml`](PMC6977020_photothermal_damage_rate_kinetics_fulltext.xml) | Denton et al., *Journal of Biomedical Optics* 2019; [PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC6977020/); full-text XML retrieved from Europe PMC 2026-07-10 | Primary photothermal cell experiment. Supports transient Arrhenius integration, Ω=1 boundary convention, strong tissue/endpoint dependence of A/E, and why CEM43 is mainly a long-duration hyperthermia metric. Not hair-follicle-specific. |
| [`PMC10107531_hair_temperature_avalanche_fulltext.xml`](PMC10107531_hair_temperature_avalanche_fulltext.xml) | Viera-Mármol et al., *Lasers in Surgery and Medicine* 2023; [PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC10107531/); full-text XML retrieved from Europe PMC 2026-07-10 | Primary bench measurement of human-hair photothermal response to alexandrite and Nd:YAG hair-removal lasers. Supports nonlinear temperature response over repeated pulses and cautions against a fixed fluence-to-temperature conversion. |
| [`Kato_2002_histological_changes_hair_removal_lasers.pdf`](Kato_2002_histological_changes_hair_removal_lasers.pdf) | Kato et al., *Journal of Nippon Medical School* 2002; [J-STAGE article](https://www.jstage.jst.go.jp/article/jnms/69/6/69_6_564/_article/-char/en); official open-access PDF retrieved 2026-07-10 | Primary human histology after ruby/alexandrite hair removal. Supports immediate follicular damage plus one-month cystic and foreign-body changes; does not establish a universal temperature threshold. |

## Linked primary papers not mirrored

- Ataie-Fashtami et al. 2011, DOI [10.1089/pho.2010.2895](https://journals.sagepub.com/doi/10.1089/pho.2010.2895): hair-removal-specific LITCIT model and the Arrhenius parameter pair now used in the simulator. Publisher full text is restricted, so this project links the official record rather than preserving an unauthorized copy.
- Fiskerstrand et al. 2003, [PubMed 12766964](https://pubmed.ncbi.nlm.nih.gov/12766964/): clinical comparison plus heat-diffusion model using a 65 °C damage convention. Publisher full text is restricted.
- Topping et al. 2000, [PubMed 10884072](https://pubmed.ncbi.nlm.nih.gov/10884072/): ex vivo human-follicle thermal imaging and histology. Publisher full text is restricted.
- McCoy et al. 1999, [PubMed 10100652](https://pubmed.ncbi.nlm.nih.gov/10100652/): histology after one 3 ms ruby-laser treatment; no evidence of permanent follicle death after one treatment. Publisher full text is restricted.

## Scope note

This corpus anchors the **damage-model correction**. Device-specific FDA filings and manuals remain in the parent IPL folder and `fda_data_pipeline/`; professional SHR outcome studies remain linked from doc 16 and the simulator source list.
