"""Compare charges against regional procedure benchmarks."""

from db import get_db

# Zip prefix → region mapping (simplified)
ZIP_TO_REGION = {
    "0": "northeast", "1": "northeast", "2": "southeast",
    "3": "southeast", "4": "midwest", "5": "midwest",
    "6": "midwest", "7": "southeast", "8": "west", "9": "west",
}


def _get_region(zip_code: str) -> str:
    if not zip_code:
        return "national"
    return ZIP_TO_REGION.get(zip_code[0], "national")


def get_benchmark(cpt_code: str, zip_code: str = "") -> dict | None:
    """Look up benchmark data for a CPT code, preferring regional data."""
    region = _get_region(zip_code)

    with get_db() as db:
        # Try regional first
        if region != "national":
            row = db.execute(
                "SELECT * FROM procedure_benchmarks WHERE cpt_code = ? AND region = ?",
                (cpt_code, region),
            ).fetchone()
            if row:
                return dict(row)

        # Fall back to national
        row = db.execute(
            "SELECT * FROM procedure_benchmarks WHERE cpt_code = ? AND region = 'national'",
            (cpt_code,),
        ).fetchone()
        return dict(row) if row else None


def check_benchmark(item: dict, zip_code: str = "") -> dict | None:
    """Compare a line item's charge against regional benchmarks.

    Flags charges above the 75th percentile as noteworthy context.
    This is informational — tells the patient where their charge falls
    relative to what other hospitals charge.
    """
    if not item.get("cpt_code") or not item.get("charged_amount"):
        return None

    benchmark = get_benchmark(item["cpt_code"], zip_code)
    if not benchmark or not benchmark.get("median_charged"):
        return None

    charged = item["charged_amount"]
    median = benchmark["median_charged"]
    p75 = benchmark.get("p75_charged") or median
    p25 = benchmark.get("p25_charged") or median

    if charged <= p75:
        return None

    # Determine percentile bucket
    if charged > benchmark.get("max_charged", charged):
        percentile_label = "above the highest reported price"
    elif charged > p75:
        percentile_label = "above the 75th percentile"
    else:
        return None

    severity = "low"
    if charged > p75 * 1.5:
        severity = "medium"

    return {
        "type": "benchmark_outlier",
        "severity": severity,
        "line_item": item,
        "charged": charged,
        "median_charged": median,
        "p25_charged": p25,
        "p75_charged": p75,
        "sample_size": benchmark.get("sample_size", 0),
        "region": benchmark.get("region", "national"),
        "potential_savings": round(max(0, charged - median), 2),
        "message": (
            f"Your charge of ${charged:,.2f} for {item.get('description', 'this service')} "
            f"is {percentile_label} nationally. "
            f"The median hospital charge is ${median:,.2f} "
            f"(based on {benchmark.get('sample_size', 'N/A')} bills)."
        ),
    }
