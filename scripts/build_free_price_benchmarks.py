"""Build no-API fair-price benchmarks from free sources.

Usage:
  python3 scripts/build_free_price_benchmarks.py --year 2026
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
from free_pricing import (  # noqa: E402
    load_target_codes,
    recompute_fair_price_bands,
    refresh_price_observations,
    summarize_scope_coverage,
)


def main() -> None:
    parser = argparse.ArgumentParser(description="Build free-source fair-price benchmark bands")
    parser.add_argument("--year", type=int, default=2026, help="Data year for hospital_prices pull")
    parser.add_argument("--codes-file", help="Optional txt/csv of CPT/HCPCS codes")
    parser.add_argument("--code-limit", type=int, default=50, help="Max number of shoppable codes")
    parser.add_argument("--exclude-user-bills", action="store_true", help="Skip user bill observations")
    parser.add_argument("--min-zip", type=int, default=8, help="Minimum samples to publish ZIP-level band")
    parser.add_argument("--min-city", type=int, default=12, help="Minimum samples to publish city-level band")
    parser.add_argument("--min-state", type=int, default=20, help="Minimum samples to publish state-level band")
    parser.add_argument("--min-national", type=int, default=40, help="Minimum samples to publish national-level band")
    args = parser.parse_args()

    db.init_db()

    codes = load_target_codes(path=args.codes_file, limit=args.code_limit)
    observations = refresh_price_observations(
        codes=codes,
        data_year=args.year,
        include_user_bills=not args.exclude_user_bills,
    )
    bands = recompute_fair_price_bands(
        codes=codes,
        min_sample_zip=args.min_zip,
        min_sample_city=args.min_city,
        min_sample_state=args.min_state,
        min_sample_national=args.min_national,
    )
    coverage = summarize_scope_coverage(codes)

    summary = {
        "codes": len(codes),
        "observations": asdict(observations),
        "bands": asdict(bands),
        "coverage": coverage,
    }
    print(json.dumps(summary, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
