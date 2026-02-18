"""Load public hospital datasets into Medbill SEO tables.

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
from typing import Iterable

sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))

import db
from hospital_seo import slugify, state_slug_from_code, upsert_hospital_directory_row


def parse_float(value: str | None) -> float | None:
    if value is None:
        return None
    txt = str(value).strip().replace(",", "").replace("$", "").replace("%", "")
    if txt == "":
        return None
    try:
        return float(txt)
    except ValueError:
        return None


def parse_int(value: str | None) -> int | None:
    num = parse_float(value)
    if num is None:
        return None
    return int(num)


def first(row: dict, keys: Iterable[str]) -> str | None:
    for key in keys:
        if key in row and row[key] not in (None, ""):
            return row[key]
    return None


def load_general_info(path: str) -> int:
    count = 0
    with open(path, newline="", encoding="utf-8-sig") as f:
        reader = csv.DictReader(f)
        for row in reader:
            facility_id = first(row, ("Facility ID", "facility_id", "ccn"))
            name = first(row, ("Facility Name", "Hospital Name", "name"))
            state = first(row, ("State", "state"))
            city = first(row, ("City/Town", "City", "city"))
            if not facility_id or not name:
                continue
            data = {
                "facility_id": str(facility_id).strip(),
                "name": name.strip(),
                "address": first(row, ("Address", "Facility Address", "address")),
                "city": city,
                "state": state,
                "state_slug": state_slug_from_code(state or ""),
                "zip": first(row, ("ZIP Code", "Zip Code", "ZIP", "zip")),
                "county": first(row, ("County Name", "County", "county")),
                "phone": first(row, ("Phone Number", "phone")),
                "hospital_type": first(row, ("Hospital Type", "hospital_type")),
                "ownership": first(row, ("Hospital Ownership", "ownership")),
                "emergency_services": first(row, ("Emergency Services", "emergency_services")),
                "overall_rating": parse_int(first(row, ("Hospital overall rating", "Overall Rating", "overall_rating"))),
                "bed_count": parse_int(first(row, ("Number of Beds", "Beds", "bed_count"))),
                "teaching_status": first(row, ("Teaching Status", "teaching_status")),
                "system_affiliation": first(row, ("System Affiliation", "system_affiliation")),
                "slug": slugify(f"{name}-{city or ''}"),
                "last_updated": first(row, ("Last Updated", "Date", "last_updated")),
            }
            upsert_hospital_directory_row(data)
            count += 1
    return count


def load_hcahps(path: str) -> int:
    count = 0
    with open(path, newline="", encoding="utf-8-sig") as f:
        reader = csv.DictReader(f)
        with db.get_db() as conn:
            for row in reader:
                facility_id = first(row, ("Facility ID", "facility_id", "ccn"))
                if not facility_id:
                    continue
                conn.execute(
                    """
                    INSERT INTO hospital_quality (
                        facility_id, hcahps_summary, patient_experience_score,
                        readmission_score, mortality_score, updated_at
                    ) VALUES (?, ?, ?, ?, ?, COALESCE(?, CURRENT_DATE))
                    ON CONFLICT(facility_id) DO UPDATE SET
                        hcahps_summary=excluded.hcahps_summary,
                        patient_experience_score=excluded.patient_experience_score,
                        readmission_score=excluded.readmission_score,
                        mortality_score=excluded.mortality_score,
                        updated_at=excluded.updated_at
                    """,
                    (
                        str(facility_id).strip(),
                        first(row, ("HCAHPS Summary Star Rating", "hcahps_summary")),
                        parse_float(first(row, ("Patient Experience Score", "patient_experience_score"))),
                        parse_float(first(row, ("Readmission Score", "readmission_score"))),
                        parse_float(first(row, ("Mortality Score", "mortality_score"))),
                        first(row, ("Last Updated", "last_updated")),
                    ),
                )
                count += 1
    return count


def load_cost_reports(path: str) -> int:
    count = 0
    with open(path, newline="", encoding="utf-8-sig") as f:
        reader = csv.DictReader(f)
        with db.get_db() as conn:
            for row in reader:
                facility_id = first(row, ("Facility ID", "facility_id", "ccn"))
                if not facility_id:
                    continue
                conn.execute(
                    """
                    INSERT INTO hospital_financials (
                        facility_id, total_charges, total_revenue, cost_to_charge_ratio,
                        charity_care_amount, charity_care_pct, nonprofit_status,
                        has_financial_assistance_policy, financial_assistance_url,
                        irs_990_url, updated_at
                    ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, COALESCE(?, CURRENT_DATE))
                    ON CONFLICT(facility_id) DO UPDATE SET
                        total_charges=excluded.total_charges,
                        total_revenue=excluded.total_revenue,
                        cost_to_charge_ratio=excluded.cost_to_charge_ratio,
                        charity_care_amount=excluded.charity_care_amount,
                        charity_care_pct=excluded.charity_care_pct,
                        nonprofit_status=excluded.nonprofit_status,
                        has_financial_assistance_policy=excluded.has_financial_assistance_policy,
                        financial_assistance_url=excluded.financial_assistance_url,
                        irs_990_url=excluded.irs_990_url,
                        updated_at=excluded.updated_at
                    """,
                    (
                        str(facility_id).strip(),
                        parse_float(first(row, ("Total Charges", "total_charges"))),
                        parse_float(first(row, ("Total Revenue", "total_revenue"))),
                        parse_float(first(row, ("Cost to Charge Ratio", "cost_to_charge_ratio"))),
                        parse_float(first(row, ("Charity Care Amount", "charity_care_amount"))),
                        parse_float(first(row, ("Charity Care Percent", "charity_care_pct"))),
                        parse_int(first(row, ("Nonprofit Status", "nonprofit_status"))),
                        parse_int(first(row, ("Has Financial Assistance Policy", "has_financial_assistance_policy"))),
                        first(row, ("Financial Assistance URL", "financial_assistance_url")),
                        first(row, ("IRS 990 URL", "irs_990_url")),
                        first(row, ("Last Updated", "last_updated")),
                    ),
                )
                count += 1
    return count


def load_prices(path: str) -> int:
    count = 0
    with open(path, newline="", encoding="utf-8-sig") as f:
        reader = csv.DictReader(f)
        with db.get_db() as conn:
            for row in reader:
                facility_id = first(row, ("Facility ID", "facility_id", "ccn"))
                cpt_code = first(row, ("CPT Code", "cpt_code", "code"))
                if not facility_id or not cpt_code:
                    continue
                conn.execute(
                    """
                    INSERT INTO hospital_procedure_prices (
                        facility_id, cpt_code, description, gross_charge, cash_price,
                        medicare_rate, avg_negotiated_rate, min_negotiated_rate,
                        max_negotiated_rate, state_avg_rate, last_updated
                    ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, COALESCE(?, CURRENT_DATE))
                    ON CONFLICT(facility_id, cpt_code) DO UPDATE SET
                        description=excluded.description,
                        gross_charge=excluded.gross_charge,
                        cash_price=excluded.cash_price,
                        medicare_rate=excluded.medicare_rate,
                        avg_negotiated_rate=excluded.avg_negotiated_rate,
                        min_negotiated_rate=excluded.min_negotiated_rate,
                        max_negotiated_rate=excluded.max_negotiated_rate,
                        state_avg_rate=excluded.state_avg_rate,
                        last_updated=excluded.last_updated
                    """,
                    (
                        str(facility_id).strip(),
                        str(cpt_code).strip(),
                        first(row, ("Description", "description")),
                        parse_float(first(row, ("Gross Charge", "gross_charge"))),
                        parse_float(first(row, ("Cash Price", "cash_price"))),
                        parse_float(first(row, ("Medicare Rate", "medicare_rate"))),
                        parse_float(first(row, ("Avg Negotiated Rate", "avg_negotiated_rate"))),
                        parse_float(first(row, ("Min Negotiated Rate", "min_negotiated_rate"))),
                        parse_float(first(row, ("Max Negotiated Rate", "max_negotiated_rate"))),
                        parse_float(first(row, ("State Avg Rate", "state_avg_rate"))),
                        first(row, ("Last Updated", "last_updated")),
                    ),
                )
                count += 1
    return count


def main() -> None:
    parser = argparse.ArgumentParser(description="Load hospital SEO datasets into Medbill DB")
    parser.add_argument("--general-csv", required=True, help="CMS Hospital General Information CSV")
    parser.add_argument("--hcahps-csv", help="CMS HCAHPS CSV")
    parser.add_argument("--cost-csv", help="CMS cost report CSV")
    parser.add_argument("--prices-csv", help="Normalized hospital prices CSV")
    args = parser.parse_args()

    db.init_db()

    general_count = load_general_info(args.general_csv)
    hcahps_count = load_hcahps(args.hcahps_csv) if args.hcahps_csv else 0
    cost_count = load_cost_reports(args.cost_csv) if args.cost_csv else 0
    prices_count = load_prices(args.prices_csv) if args.prices_csv else 0

    print(
        f"Loaded hospitals={general_count}, hcahps={hcahps_count}, "
        f"cost_reports={cost_count}, prices={prices_count}"
    )


if __name__ == "__main__":
    main()
