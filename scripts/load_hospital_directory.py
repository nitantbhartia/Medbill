"""Load hospital datasets into canonical SEO tables.

Examples:
python scripts/load_hospital_directory.py --source cms_general --path data/hospitals/general.csv
python scripts/load_hospital_directory.py --source hcahps --path data/hospitals/hcahps.csv
python scripts/load_hospital_directory.py --source cost_reports --path data/hospitals/cost.csv
python scripts/load_hospital_directory.py --source provider_of_services --path data/hospitals/pos.csv
python scripts/load_hospital_directory.py --source medicare_rates --path data/hospitals/pfs.csv --year 2026
python scripts/load_hospital_directory.py --source transparency_index --path data/hospitals/transparency_index.csv
"""

from __future__ import annotations

import argparse
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))

import db
from hospital_etl import (
    load_cms_general,
    load_cost_reports,
    load_hcahps,
    load_medicare_rates,
    load_provider_of_services,
    load_transparency_index,
)


SOURCES = {
    "cms_general": load_cms_general,
    "hcahps": load_hcahps,
    "cost_reports": load_cost_reports,
    "provider_of_services": load_provider_of_services,
    "medicare_rates": load_medicare_rates,
    "transparency_index": load_transparency_index,
}


def main() -> None:
    parser = argparse.ArgumentParser(description="Load hospital directory sources")
    parser.add_argument("--source", required=True, choices=sorted(SOURCES.keys()))
    parser.add_argument("--path", required=True, help="CSV path for selected source")
    parser.add_argument("--year", type=int, help="effective year for medicare rates")
    args = parser.parse_args()

    db.init_db()
    fn = SOURCES[args.source]
    if args.source == "medicare_rates":
        count = fn(args.path, effective_year=args.year)
    else:
        count = fn(args.path)
    print(f"Loaded source={args.source} records={count}")


if __name__ == "__main__":
    main()
