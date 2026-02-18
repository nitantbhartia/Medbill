"""Recompute benchmark averages and billing grades."""

from __future__ import annotations

import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))

import db
from hospital_seo import log_refresh, recompute_benchmarks, recompute_billing_metrics


def main() -> None:
    db.init_db()
    benchmarks = recompute_benchmarks()
    metrics = recompute_billing_metrics()
    log_refresh("billing_metrics", metrics, "success", f"benchmarks={benchmarks}")
    print({"benchmarks": benchmarks, "metrics": metrics})


if __name__ == "__main__":
    main()
