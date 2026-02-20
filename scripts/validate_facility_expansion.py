"""Validation queries for ASC + imaging expansion."""

from __future__ import annotations

import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))

import db  # noqa: E402


def run() -> None:
    db.init_db()
    with db.get_db() as conn:
        print("\nFacility type distribution")
        rows = conn.execute(
            """
            SELECT
                f.facility_type,
                COUNT(*) AS count,
                AVG(fm.avg_markup) AS avg_markup,
                SUM(CASE WHEN fm.billing_grade IS NOT NULL THEN 1 ELSE 0 END) AS graded
            FROM facilities f
            LEFT JOIN facility_billing_metrics fm ON fm.facility_id = f.facility_id
            GROUP BY f.facility_type
            ORDER BY count DESC
            """
        ).fetchall()
        for r in rows:
            print(dict(r))

        print("\nHospital-owned vs independent ASC pricing")
        rows = conn.execute(
            """
            SELECT
                f.is_hospital_owned,
                COUNT(*) AS facility_count,
                AVG(fm.avg_markup) AS avg_markup,
                AVG(CASE fm.billing_grade
                    WHEN 'A' THEN 1 WHEN 'B' THEN 2 WHEN 'C' THEN 3 WHEN 'D' THEN 4 WHEN 'F' THEN 5 ELSE NULL END
                ) AS avg_grade_score
            FROM facilities f
            LEFT JOIN facility_billing_metrics fm ON fm.facility_id = f.facility_id
            WHERE f.facility_type = 'asc'
            GROUP BY f.is_hospital_owned
            """
        ).fetchall()
        for r in rows:
            print(dict(r))

        print("\nCross-facility CPT 45378 comparison")
        rows = conn.execute(
            """
            WITH all_prices AS (
                SELECT facility_id, cpt_code, gross_charge, markup_vs_medicare FROM hospital_prices
                UNION ALL
                SELECT facility_id, cpt_code, gross_charge, markup_vs_medicare FROM procedure_prices
            )
            SELECT
                COALESCE(f.facility_type, 'hospital') AS facility_type,
                COALESCE(f.is_hospital_owned, 0) AS is_hospital_owned,
                COUNT(*) AS facilities_with_data,
                AVG(p.gross_charge) AS avg_charge,
                AVG(p.markup_vs_medicare) AS avg_markup,
                MIN(p.gross_charge) AS min_charge,
                MAX(p.gross_charge) AS max_charge
            FROM all_prices p
            LEFT JOIN facilities f ON f.facility_id = p.facility_id
            WHERE p.cpt_code = '45378'
            GROUP BY COALESCE(f.facility_type, 'hospital'), COALESCE(f.is_hospital_owned, 0)
            ORDER BY avg_charge ASC
            """
        ).fetchall()
        for r in rows:
            print(dict(r))


if __name__ == "__main__":
    run()
