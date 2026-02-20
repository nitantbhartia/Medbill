"""Recompute benchmark averages and billing grades."""

from __future__ import annotations

import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))

import db
from hospital_seo import (
    log_refresh,
    recompute_benchmarks,
    recompute_billing_metrics,
    recompute_facility_billing_metrics,
)


def main() -> None:
    db.init_db()
    benchmarks = recompute_benchmarks()
    metrics = recompute_billing_metrics()
    facility_metrics = recompute_facility_billing_metrics()
    log_refresh(
        "billing_metrics",
        metrics + facility_metrics,
        "success",
        f"benchmarks={benchmarks} facility_metrics={facility_metrics}",
    )
    print({"benchmarks": benchmarks, "metrics": metrics, "facility_metrics": facility_metrics})


if __name__ == "__main__":
    main()
