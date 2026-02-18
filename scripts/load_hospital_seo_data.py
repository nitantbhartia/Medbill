"""Bulk load hospital SEO datasets.

Usage:
python scripts/load_hospital_seo_data.py \
  --general-csv data/hospitals/Hospital_General_Information.csv \
  --hcahps-csv data/hospitals/HCAHPS_Hospital.csv \
  --cost-csv data/hospitals/Hospital_Cost_Report.csv \
  --prices-csv data/hospitals/Hospital_Prices.csv
"""

from __future__ import annotations

import argparse
import csv
import os
import sys
from datetime import date

sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))

import db
from hospital_etl import (
    load_cms_general,
    load_cost_reports,
    load_hcahps,
    normalize_price_rows,
    parse_float,
    upsert_hospital_price,
)


def load_prices(path: str, data_year: int | None = None) -> int:
    with open(path, newline="", encoding="utf-8-sig") as f:
        rows = list(csv.DictReader(f))

    count = 0
    year = data_year or date.today().year
    for src_row in rows:
        facility_id = src_row.get("Facility ID") or src_row.get("facility_id") or src_row.get("ccn")
        code = src_row.get("CPT Code") or src_row.get("cpt_code") or src_row.get("code")
        if not facility_id or not code:
            continue

        normalized = normalize_price_rows([src_row])
        if not normalized:
            continue
        row = normalized[0]
        row["min_negotiated_rate"] = parse_float(src_row.get("Min Negotiated Rate") or src_row.get("min_negotiated_rate"))
        row["max_negotiated_rate"] = parse_float(src_row.get("Max Negotiated Rate") or src_row.get("max_negotiated_rate"))
        row["avg_negotiated_rate"] = parse_float(src_row.get("Avg Negotiated Rate") or src_row.get("avg_negotiated_rate"))
        upsert_hospital_price(str(facility_id).strip(), row, data_year=year)
        count += 1

    return count


def main() -> None:
    parser = argparse.ArgumentParser(description="Load hospital SEO datasets into Medbill DB")
    parser.add_argument("--general-csv", required=True, help="CMS Hospital General Information CSV")
    parser.add_argument("--hcahps-csv", help="CMS HCAHPS CSV")
    parser.add_argument("--cost-csv", help="CMS cost report CSV")
    parser.add_argument("--prices-csv", help="Normalized hospital prices CSV")
    parser.add_argument("--year", type=int, help="data year override for prices")
    args = parser.parse_args()

    db.init_db()

    general_count = load_cms_general(args.general_csv)
    hcahps_count = load_hcahps(args.hcahps_csv) if args.hcahps_csv else 0
    cost_count = load_cost_reports(args.cost_csv) if args.cost_csv else 0
    prices_count = load_prices(args.prices_csv, data_year=args.year) if args.prices_csv else 0

    print(
        f"Loaded hospitals={general_count}, hcahps={hcahps_count}, "
        f"cost_reports={cost_count}, prices={prices_count}"
    )


if __name__ == "__main__":
    main()
