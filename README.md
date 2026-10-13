# DAO2702 Project | Singapore Homebuyer Story 2025

A reproducible Singapore private-homebuyer analysis notebook using 2025 transaction data, a historical 2020–2025 series, MRT station information, and geographic datasets.

[Read the visual guide](https://singapore-family-homebuyer-guide.bigbavkdiu.chatgpt.site).

## Open in Google Colab

[![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/BIGBACKDIU/DAO2702_project/blob/main/Singapore_Homebuyer_Story_2025_v4_Colab.ipynb)

1. Open the notebook via the badge above.
2. Run the new Colab setup cell near the top. It downloads the input files from the public repository into the Colab working directory and verifies their SHA-256 hashes.
3. Run the remaining notebook cells normally. The family v4 analysis was revised on 13 October 2026 to reconcile model and observed prices, explain the different growth comparisons and new-sale estimates, and add ten-year ownership scenarios. The local notebook and this Colab version share the same analysis cells; this version adds a download setup cell. See [the cell-by-cell change log](COHERENCE_CHANGES_2026_10_13.md).

### Dataset files

- `properties2025.csv`: 2025 property transactions
- `data/properties_2020_2025_clean.csv.part01` to `.part11`: **byte-exact slices** of `properties_2020_2025_clean.csv`; the setup cell joins these into the original CSV in Colab
- `sg_map.json`: Singapore geographic boundaries
- `sg_mrt.json`: Singapore MRT/LRT geographic data
- `project_coords.csv`: property-project coordinates
- `mrt_station_openings.csv`: MRT line / station opening timeline

The historical CSV is stored in 11 parts because of an upload-connection size limit. No data was changed or reprocessed. The Colab setup cell reconstructs it transparently before analysis.

### Input integrity

- `properties2025.csv` SHA-256: `e12f1469f4f71f2bd93f6ab5f31715daadb9de3524e2725a186930577788c6f8`
- Reconstructed `properties_2020_2025_clean.csv` SHA-256: `edede72a9ab8c628d30ce9605dc6a6c7ddb8864f22a734c5a92c78117aacf8b6`

The GitHub notebook omits stored execution outputs to keep downloads small; running it regenerates the charts and tables. External data-source attributions appear within the notebook.

## Reproduce preprocessing

The repository now includes the supplied `properties23.csv` and `properties2024.csv` inputs, `clean_2020_2025.py`, its recorded `cleaning_log.txt`, and [provenance and hash checks](CLEANING_PROVENANCE.md). From the repository root:

```bash
python -m pip install -r requirements-repro.txt
python clean_2020_2025.py
```

The cleaner verifies even multiplicity before halving the March–July 2021 block. Missing months remain gaps; remaining duplicates are flagged. The supplied 2024 input is already price-reconstructed; the cleaner flags that provenance and cannot recover original prices. The verified rebuild has the same rows, labels and flags as the supplied cleaned table within negligible floating-point round-trip tolerance, but its byte hash differs. The Colab analysis continues to use the original hash-checked eleven-part file.

## Reading the new ownership check

The ten-year table uses 2026-Q3 index-proxy starting prices and assumed price changes of -20%, zero and +20% over ten years. These are financial stress scenarios, not predicted returns or confidence bounds. Equity excludes selling costs and CPF refunds. Calendar ageing begins with the guide’s 2025 lease bands.
