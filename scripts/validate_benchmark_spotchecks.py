"""Manual benchmark spot-check utility.

Usage:
  python3 scripts/validate_benchmark_spotchecks.py --hospital "Mayo" --limit 10
  python3 scripts/validate_benchmark_spotchecks.py --hospital "Cleveland" --cpt 99285 --limit 5
"""

from __future__ import annotations

import argparse

from db import get_db


def fmt_money(v):
    return f"${v:,.2f}" if isinstance(v, (int, float)) else "N/A"


def main() -> None:
    parser = argparse.ArgumentParser(description="Validate hospital price-vs-Medicare markup spot checks")
    parser.add_argument("--hospital", required=True, help="Hospital name substring to match")
    parser.add_argument("--cpt", help="Optional CPT filter")
    parser.add_argument("--limit", type=int, default=20)
    args = parser.parse_args()

    with get_db() as db:
        hospitals = db.execute(
            """
            SELECT facility_id, name, city, state
            FROM hospitals
            WHERE lower(name) LIKE lower(?)
            ORDER BY name
            LIMIT 5
            """,
            (f"%{args.hospital}%",),
        ).fetchall()

        if not hospitals:
            print(f"No hospitals found matching: {args.hospital}")
            return

        for h in hospitals:
            print(f"\n=== {h['name']} ({h['city']}, {h['state']}) [{h['facility_id']}] ===")
            rows = db.execute(
                """
                SELECT cpt_code, description, gross_charge, medicare_rate, markup_vs_medicare
                FROM hospital_prices
                WHERE facility_id = ?
                  AND gross_charge IS NOT NULL
                  AND medicare_rate IS NOT NULL
                  AND medicare_rate > 0
                  AND (? IS NULL OR cpt_code = ?)
                ORDER BY gross_charge DESC
                LIMIT ?
                """,
                (h["facility_id"], args.cpt, args.cpt, args.limit),
            ).fetchall()

            if not rows:
                print("No comparable price rows found.")
                continue

            mismatch = 0
            for r in rows:
                expected = r["gross_charge"] / r["medicare_rate"] if r["medicare_rate"] else None
                stored = r["markup_vs_medicare"]
                delta = abs((stored or 0) - (expected or 0)) if (stored is not None and expected is not None) else None
                if delta is not None and delta > 0.05:
                    mismatch += 1
                print(
                    f"{r['cpt_code']}: {r['description'] or 'N/A'} | gross={fmt_money(r['gross_charge'])} | "
                    f"medicare={fmt_money(r['medicare_rate'])} | stored={stored:.2f}x | expected={expected:.2f}x"
                )

            print(f"Rows checked: {len(rows)} | Markup mismatches (>0.05x): {mismatch}")


if __name__ == "__main__":
    main()
