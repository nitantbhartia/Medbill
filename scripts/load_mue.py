"""Load a CMS medically unlikely edits (MUE) file. Download the practitioner, outpatient hospital or equipment file from
https://www.cms.gov/medicare/coding-billing/national-correct-coding-initiative-ncci-edits/medically-unlikely-edits

  python scripts/load_mue.py --csv mue_practitioner.csv --setting practitioner --version "2026 Q1" --date 2026-01-01"""

import argparse
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import cms_loader
from db import init_db


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--csv", required=True)
    parser.add_argument("--setting", required=True, choices=["practitioner", "outpatient", "equipment"])
    parser.add_argument("--version", required=True)
    parser.add_argument("--date", required=True)
    args = parser.parse_args()
    init_db()
    print(f"Loaded {cms_loader.load_mue_limits(args.csv, args.setting, args.version, args.date)} limits")


if __name__ == "__main__":
    main()
