# DAO2702 Project | Singapore Homebuyer Story 2025

A reproducible Singapore private-homebuyer analysis notebook using 2025 transaction data, a historical 2020–2025 series, MRT station information, and geographic datasets.

## Open in Google Colab

[![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/BIGBACKDIU/DAO2702_project/blob/main/Singapore_Homebuyer_Story_2025_v4_Colab.ipynb)

1. Open the notebook via the badge above.
2. Run the new Colab setup cell near the top. It downloads the input files from the public repository into the Colab working directory and verifies their SHA-256 hashes.
3. Run the remaining notebook cells normally. All **108 original notebook cells and their source code/markdown are unchanged**; only the Colab download setup cell was added and adapted for this repository.

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
