# IPL patent-source manifest

This folder preserves the three mirrored US patent PDFs used by the rendered [patent panel](../index.html#patents). Patents establish claimed inventions and chronology; they do **not** establish that a marketed device implements every claim, that a parameter set is clinically effective, or that a consumer protocol is safe.

| Local capture | Patent | Why it is retained | Provenance / integrity |
|---|---|---|---|
| `us-patent-5405368-esc-broadband-ipl.pdf` | [US 5,405,368 A](https://patents.google.com/patent/US5405368A/en), *Method and apparatus for therapeutic electromagnetic treatment* | Early broadband-flashlamp architecture, filtering, exposure-area, cooling, and energy-density claims | USPTO-generated PDF captured 2026-07-01; SHA-256 `0811263bf39e3f2172e4880b9534b24bc5a90555461603674c9319b1e2a64c17`. The current mirror opens inconsistently in Poppler and should be reacquired before text extraction. |
| `us-patent-5735844-anderson-hair-removal.pdf` | [US 5,735,844 A](https://patents.google.com/patent/US5735844A/en), *Hair removal using optical pulses* | Large-spot optical hair-removal, fluence, wavelength, and contact-cooling claims | USPTO PDF Builder capture dated 2026-07-01; SHA-256 `b408dd9ec80a5f96a977860f94a91262bb65bec4b279b70ac199674946ee2648`. |
| `us-patent-8950406-alma-lasers-ipl.pdf` | [US 8,950,406 B2](https://patents.google.com/patent/US8950406B2/en), *Method and apparatus for light-based hair removal* | Rapid low-fluence pulse-train and coherent-or-incoherent light claims closest to modern SHR/IPL comparisons | USPTO PDF Builder capture dated 2026-07-01; SHA-256 `688ca6bf8dfa7575734a257dc747c750bdfe86888a4fc1fc82b626a609416888`. |

## Evidence boundary and remaining gap

- Use the live patent record to verify current legal status and family relationships; this local corpus is an analysis snapshot.
- Patent examples and claimed ranges are not head-to-head outcome data and are not inputs for personal dosing.
- The US 5,405,368 mirror needs a fresh official capture because its cross-reference table is malformed for at least one standards-compliant PDF parser.

*Manifest added 2026-08-23. Hashes describe the local files at that date.*
