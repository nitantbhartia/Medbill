"""Load California hospital chargemasters (filed with HCAI) into the description -> code lookup.

HCAI posts the files on its chargemaster page, which changes each year, so the link is not kept in code:
  python scripts/load_hcai_chargemasters.py --discover        # lists the download links on the current page
  python scripts/load_hcai_chargemasters.py --file chargemaster.csv [--source-url URL]

--file takes either HCAI's per-hospital workbook (.xlsx, as in the yearly zip) or a CSV with a facility name column, a description
column and a CPT/HCPCS code column (names are matched loosely). --dir loads every .xlsx under a folder (the unzipped yearly file).
Needs `pip install openpyxl` (not a production dependency). The yearly zips are on data.chhs.ca.gov (linked from HCAI's chargemaster page) and are 0.3 to 1 GB."""

import argparse
import csv
import os
import re
from pathlib import Path
import sys
from urllib.request import Request, urlopen

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import code_lookup
import config
from db import init_db

COLUMN_WORDS = {"facility_name": ("facility_name", "facname", "hospital", "facility"),
                "description": ("description", "desc"),
                "code": ("cpt", "hcpcs", "procedure_code", "code")}


def find_column(headers: list[str], field: str) -> str:
    for word in COLUMN_WORDS[field]:
        for header in headers:
            if word in header.lower().replace(" ", "_"):
                return header
    raise SystemExit(f"No {field} column in: {headers}")


def discover() -> None:
    html = urlopen(Request(config.HCAI_CHARGEMASTER_PAGE, headers={"User-Agent": "BillKarma data research"}), timeout=60).read().decode("utf-8", "ignore")
    for link in sorted(set(re.findall(r'href="([^"]+\.(?:zip|csv|xlsx))"', html, re.I))):
        print(link)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--discover", action="store_true")
    parser.add_argument("--file")
    parser.add_argument("--dir")
    parser.add_argument("--source-url")
    args = parser.parse_args()
    if args.discover:
        return discover()
    if not args.file and not args.dir:
        parser.error("give --file, --dir or --discover")
    init_db()
    if args.dir:
        totals = {"loaded": 0, "skipped_unknown_hospital": 0}
        for workbook in sorted(Path(args.dir).rglob("*.xlsx")):
            result = code_lookup.load_chargemaster(code_lookup.hcai_workbook_rows(str(workbook)), args.source_url)
            totals = {key: totals[key] + result[key] for key in totals}
        return print(totals)
    if args.file.endswith(".xlsx"):
        return print(code_lookup.load_chargemaster(code_lookup.hcai_workbook_rows(args.file), args.source_url))
    with open(args.file, newline="", encoding="utf-8-sig") as handle:
        reader = csv.DictReader(handle)
        columns = {field: find_column(reader.fieldnames, field) for field in COLUMN_WORDS}
        rows = ({field: row[column] for field, column in columns.items()} for row in reader)
        print(code_lookup.load_chargemaster(rows, args.source_url))


if __name__ == "__main__":
    main()
