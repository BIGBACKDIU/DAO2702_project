# Cleaning provenance and reproducibility

The repository supplies both the analysis-ready series and the preprocessing inputs. `properties23.csv` and `properties2024.csv` are the supplied input extracts; `properties2025.csv` is already at the repository root. Run the cleaner from that root:

```bash
python -m pip install -r requirements-repro.txt
python clean_2020_2025.py
```

It writes `properties_2020_2025_clean.csv` and prints the log reproduced in `cleaning_log.txt`. The existing eleven `data/*.partNN` files are byte slices of the supplied cleaned file; concatenate them in numeric order to obtain that file without preprocessing.

## What the cleaner checks and changes

- March–July 2021: it verifies that every exact-row group has even multiplicity before retaining half of each group. This documents the source-block correction; it does not establish whether every remaining identical unit is a duplicate transaction.
- August–October 2021: absent from the supplied extract and left as missing months. No interpolation is performed.
- Labels are harmonised; floor, calendar fields, price per sqft and lease used are derived.
- Remaining exact duplicates are flagged, not globally deleted. Cross-year analyses exclude sub sales because the earlier extract does not record them.
- **2024 provenance boundary:** the supplied `properties2024.csv` already contains prices reconstructed from rounded price per sqft and area. This cleaner flags those rows. It does not recover original negotiated prices or reproduce an earlier conversion from the original 2024 source export. The rounding limits price-ending analysis.

## Verification on 13 October 2026

Byte-exact cleaned-file reproduction in the recorded environment: **False**. A parsed-table comparison is used if library formatting changes the bytes.

| Package | Version |
|---|---|
| pandas | 2.3.3 |
| numpy | 2.3.5 |
| scipy | 1.16.3 |
| matplotlib | 3.10.8 |

### Supplied input and output SHA-256

- `properties23.csv`: `ab8e4dadf69a39b5207099789fdac7e48726f5b36adac8b9e5054b4254e867fc`
- `properties2024.csv`: `5de83d97e48a1f54b079a2e6e27bb7883a89c5082ca72bdc43cca8ec5df3e7b6`
- `properties2025.csv`: `e12f1469f4f71f2bd93f6ab5f31715daadb9de3524e2725a186930577788c6f8`
- `properties_2020_2025_clean.csv`: `edede72a9ab8c628d30ce9605dc6a6c7ddb8864f22a734c5a92c78117aacf8b6`

These hashes establish file integrity; the script and checks establish which transformations were applied. They cannot prove that an upstream extract is complete.
