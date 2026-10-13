"""Combine and clean the three URA-style private-home sale files into one table (Aug 2020 - Dec 2025).
Run from the folder holding properties23.csv, properties2024.csv and properties2025.csv:  python clean_2020_2025.py
Writes properties_2020_2025_clean.csv and prints a cleaning log."""
import pandas as pd, numpy as np
COLS = ['project', 'street', 'type', 'district', 'segment', 'tenure', 'commence', 'sale', 'price', 'area', 'level', 'date']
a = pd.read_csv('properties23.csv')[COLS]; b = pd.read_csv('properties2024.csv')[COLS]; c = pd.read_csv('properties2025.csv')[COLS]
a['source'], b['source'], c['source'] = 'properties23.csv', 'properties2024.csv', 'properties2025.csv'
d = pd.concat([a, b, c], ignore_index=True)
d['month_start'] = pd.to_datetime(d.date, format='%b-%y')
log = [f'raw rows: {len(a):,} + {len(b):,} + {len(c):,} = {len(d):,}']
# 1) Mar-Jul 2021 in properties23.csv: exact-row groups have even multiplicity (2x, 4x, ...). Keep half of each group.
dbl = (d.source == 'properties23.csv') & d.month_start.between('2021-03-01', '2021-07-01')
g = d[dbl].groupby(COLS, dropna=False)
# Stop rather than silently halve a block that does not match the documented pattern.
multiplicity = g.size()
if (multiplicity % 2).any():
    raise ValueError("Mar-Jul 2021 block contains an odd-multiplicity exact-row group; inspect the source before halving.")
keep_idx = g.apply(lambda x: x.index[: len(x) // 2]).explode().astype(int)
n_before = dbl.sum(); d = pd.concat([d[~dbl], d.loc[keep_idx]]).sort_index()
log.append(f'Mar-Jul 2021 even-multiplicity block: {n_before:,} rows -> {len(keep_idx):,} (each exact-row group halved)')
# 2) Harmonise labels
d['tenure'] = d.tenure.replace({'99 years': '99-yr', 'freehold': 'Freehold', 'freenhold': 'Freehold', 'other': '999-yr/other',
                                 'others': '999-yr/other', 'less than 99 years': 'Under 99-yr'})
d['year'] = d.month_start.dt.year; d['month'] = d.month_start.dt.month
d['quarter'] = d.month_start.dt.to_period('Q').astype(str)
d['psf'] = d.price / d.area
d['floor'] = d.level.str.extract(r'(\d+) to')[0].astype(float); d.loc[d.level.str.startswith('B'), 'floor'] = 0
d['lease_used'] = np.where(d.tenure == '99-yr', d.year - d.commence, np.nan)
# 3) Flags (kept, not dropped). The supplied 2024 input already contains rebuilt prices;
# this cleaner marks that provenance rather than rebuilding or recovering original transaction prices.
d['sub_sale'] = d.sale.eq('Sub Sale')                    # only recorded from 2024; absent from the 2020-23 file
d['price_rebuilt_2024'] = d.source.eq('properties2024.csv')  # 2024 prices = whole-dollar psf x area; relative rounding varies with psf
d['exact_dup'] = d.duplicated(COLS, keep='first')        # remaining exact duplicates (kept by default, as in the 2025 guides)
log.append(f'Sub Sale rows (2024-25 only): {d.sub_sale.sum():,}; remaining exact duplicates flagged: {d.exact_dup.sum():,}')
gaps = sorted(set(pd.period_range('2020-08', '2025-12', freq='M').astype(str)) - set(d.month_start.dt.to_period('M').astype(str)))
log.append(f'months with no data: {gaps}')
d.drop(columns=['month_start']).to_csv('properties_2020_2025_clean.csv', index=False)
log.append(f'clean rows: {len(d):,}  ->  properties_2020_2025_clean.csv')
print('\n'.join(log))
