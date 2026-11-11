"""Re-benchmark hospital markups against Medicare's OPPS rate and regrade every hospital.

Production does this once automatically at startup; run by hand to force it:
    python scripts/rebenchmark_hospital_prices.py
"""

from __future__ import annotations

import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import db  # noqa: E402
from hospital_etl import rebenchmark_hospital_prices  # noqa: E402
from hospital_seo import generate_and_save_hospital_content, recompute_benchmarks, recompute_billing_metrics  # noqa: E402


def main() -> None:
    db.init_db()
    with db.get_db() as conn:
        before = dict(conn.execute("SELECT billing_grade, COUNT(*) FROM billing_metrics GROUP BY billing_grade").fetchall())
    rows = rebenchmark_hospital_prices()
    recompute_benchmarks()
    recompute_billing_metrics()
    generate_and_save_hospital_content()
    with db.get_db() as conn:
        after = dict(conn.execute("SELECT billing_grade, COUNT(*) FROM billing_metrics GROUP BY billing_grade").fetchall())
    print({"price_rows": rows, "grades_before": before, "grades_after": after})


if __name__ == "__main__":
    main()
