#!/usr/bin/env python3
"""Generate a markdown data quality report from latest run snapshot."""

from __future__ import annotations

import argparse
import os
import sys
from datetime import datetime

ROOT = os.path.dirname(os.path.dirname(__file__))
if ROOT not in sys.path:
    sys.path.insert(0, ROOT)

import db  # noqa: E402
from data_quality import latest_quality_run  # noqa: E402


def main() -> int:
    parser = argparse.ArgumentParser(description="Generate markdown data quality report")
    parser.add_argument("--out", default="data/quality/latest_data_quality.md")
    args = parser.parse_args()

    db.init_db()
    run = latest_quality_run()
    if not run:
        print("No data_quality_runs found.")
        return 1

    checks = run.get("checks", {}).get("consistency", {}).get("checks", {})
    regressions = run.get("checks", {}).get("regressions", [])
    coverage = run.get("coverage", [])
    ts = datetime.utcnow().isoformat() + "Z"
    lines = [
        "# Data Quality Report",
        "",
        f"- Generated: {ts}",
        f"- Latest Run ID: {run['id']}",
        f"- Status: {run['status']}",
        f"- Notes: {run.get('notes') or ''}",
        "",
        "## Consistency Checks",
    ]
    for name, val in sorted(checks.items()):
        lines.append(f"- {name}: {val}")
    lines.append("")
    lines.append("## Coverage Regressions")
    if not regressions:
        lines.append("- none")
    else:
        for r in regressions:
            lines.append(
                f"- CPT {r['cpt_code']} @ {r['radius_miles']}mi: "
                f"{r['previous_ratio']:.3f} -> {r['current_ratio']:.3f} (drop {r['drop']:.3f})"
            )
    lines.append("")
    lines.append("## Coverage Samples")
    for row in coverage[:50]:
        lines.append(
            f"- CPT {row['cpt_code']} @ {row['radius_miles']}mi: "
            f"{row['covered_zips']}/{row['zip_samples']} ({row['coverage_ratio']:.3f})"
        )

    os.makedirs(os.path.dirname(args.out), exist_ok=True)
    with open(args.out, "w", encoding="utf-8") as f:
        f.write("\n".join(lines) + "\n")
    print(args.out)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

