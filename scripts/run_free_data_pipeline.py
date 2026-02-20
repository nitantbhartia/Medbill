"""End-to-end free data pipeline runner.

Stages:
1) (Optional) Load transparency index CSV
2) Parse/download top-300 hospital MRF files
3) Build fair-price percentile bands from MRF + user bill observations

Usage:
  python3 scripts/run_free_data_pipeline.py --year 2026 --transparency-index-csv data/hospitals/transparency_index.csv
"""

from __future__ import annotations

import argparse
import json
import os
import sys
from dataclasses import asdict

ROOT = os.path.dirname(os.path.dirname(__file__))
if ROOT not in sys.path:
    sys.path.insert(0, ROOT)

import db  # noqa: E402
from free_pricing import load_target_codes, recompute_fair_price_bands, refresh_price_observations  # noqa: E402
from hospital_etl import load_transparency_index, refresh_top300_transparency  # noqa: E402


def main() -> None:
    parser = argparse.ArgumentParser(description="Run free-only pricing data pipeline")
    parser.add_argument("--year", type=int, default=2026, help="Data year for hospital_prices and fair bands")
    parser.add_argument("--files-dir", default="", help="Directory of local transparency files (optional)")
    parser.add_argument("--transparency-index-csv", help="Optional CSV to refresh transparency file URLs")
    parser.add_argument("--codes-file", help="Optional txt/csv shoppable code list")
    parser.add_argument("--code-limit", type=int, default=50, help="Max shoppable codes for band building")
    parser.add_argument("--skip-top300-refresh", action="store_true", help="Skip transparency file parse stage")
    parser.add_argument("--skip-user-bills", action="store_true", help="Exclude user bill observations")
    args = parser.parse_args()

    db.init_db()

    summary: dict[str, object] = {
        "year": args.year,
    }

    if args.transparency_index_csv:
        loaded = load_transparency_index(args.transparency_index_csv)
        summary["transparency_index_rows"] = loaded

    if not args.skip_top300_refresh:
        top300 = refresh_top300_transparency(files_dir=args.files_dir, data_year=args.year)
        summary["top300_refresh"] = top300

    codes = load_target_codes(path=args.codes_file, limit=args.code_limit)
    observations = refresh_price_observations(
        codes=codes,
        data_year=args.year,
        include_user_bills=not args.skip_user_bills,
    )
    bands = recompute_fair_price_bands(codes=codes)
    summary["codes"] = len(codes)
    summary["observations"] = asdict(observations)
    summary["bands"] = asdict(bands)

    print(json.dumps(summary, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
