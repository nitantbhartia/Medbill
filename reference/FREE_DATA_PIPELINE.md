# Free Data Pipeline (No Paid API)

This pipeline builds fair-price benchmarks from free/public inputs and first-party bill uploads.

## What It Uses

- `hospital_prices` (MRF-derived rates from hospital transparency files)
- `line_items` + `bills` (user-uploaded bill outcomes)
- `medicare_rates` (benchmark spine already in DB)

## New Tables

- `price_observations`: canonical row-level observations (MRF + user bill).
- `fair_price_bands`: percentile bands by geography and code.

## Geography Fallback

Benchmarks are computed and resolved in this order:

1. ZIP (`geo_scope=zip`, `geo_value=33101`)
2. City+State (`geo_scope=city`, `geo_value=MIAMI|FL`)
3. State (`geo_scope=state`, `geo_value=FL`)
4. National (`geo_scope=national`, `geo_value=US`)

## Scripts

### 1) Build fair-price bands only

```bash
python3 scripts/build_free_price_benchmarks.py --year 2026
```

Key options:

- `--codes-file`: custom CPT list
- `--code-limit`: default `50`
- `--exclude-user-bills`: ignore bill-derived observations
- `--min-zip --min-city --min-state --min-national`: sample thresholds

### 2) Run full free pipeline

```bash
python3 scripts/run_free_data_pipeline.py \
  --year 2026 \
  --transparency-index-csv data/hospitals/transparency_index.csv \
  --files-dir data/hospitals/mrf
```

This does:

1. Load transparency index URLs (optional).
2. Refresh top-300 hospital MRF parses.
3. Build observation table + fair-price bands.

## Recommended Run Cadence

- Monthly:
  - `run_free_data_pipeline.py`
- Daily:
  - `build_free_price_benchmarks.py` (to include fresh user bill outcomes)

## Suggested Product Wiring

- For pre-care shopping:
  - Use `fair_price_bands.p50` as expected allowed amount.
- For bill check:
  - Compare observed allowed/billed values against `p50/p75/p90`.
- Show a confidence indicator:
  - `sample_size` + `confidence_mean`.
