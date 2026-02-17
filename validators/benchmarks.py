"""Compare charges against regional procedure benchmarks."""

from db import get_db
from validators.geo import get_region


def _get_region(zip_code: str) -> str:
    return get_region(zip_code, None)


def get_benchmark(cpt_code: str, zip_code: str = "", provider_address: str | None = None) -> dict | None:
    """Look up benchmark data for a CPT code, preferring regional data."""
    region = get_region(zip_code, provider_address)

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


def check_benchmark(
    item: dict,
    zip_code: str = "",
    provider_address: str | None = None,
    percentile_multiplier: float = 1.0,
) -> dict | None:
    """Compare a line item's charge against regional benchmarks.

    Flags charges above the 75th percentile as noteworthy context.
    This is informational — tells the patient where their charge falls
    relative to what other hospitals charge.
    """
    if not item.get("cpt_code") or not item.get("charged_amount"):
        return None

    benchmark = get_benchmark(item["cpt_code"], zip_code, provider_address)
    if not benchmark or not benchmark.get("median_charged"):
        return None

    charged = item["charged_amount"]
    median = benchmark["median_charged"]
    p75 = benchmark.get("p75_charged") or median
    p25 = benchmark.get("p25_charged") or median

    if charged <= (p75 * percentile_multiplier):
        return None

    # Determine percentile bucket
    if charged > benchmark.get("max_charged", charged):
        percentile_label = "above the highest reported price"
    elif charged > (p75 * percentile_multiplier):
        percentile_label = "above the 75th percentile"
    else:
        return None

    severity = "low"
    if charged > p75 * 1.5:
        severity = "medium"

    patient_resp = item.get("patient_responsibility")
    region_label = benchmark.get("region", "national")

    if patient_resp is not None:
        message = (
            f"Your provider charged ${charged:,.2f} for "
            f"{item.get('description', 'this service')}; after insurance, "
            f"your responsibility is ${patient_resp:,.2f}. "
            f"The median hospital charge in the {region_label} dataset is ${median:,.2f} "
            f"(based on {benchmark.get('sample_size', 'N/A')} bills)."
        )
    else:
        message = (
            f"Your charge of ${charged:,.2f} for "
            f"{item.get('description', 'this service')} "
            f"is {percentile_label} in the {region_label} dataset. "
            f"The median hospital charge is ${median:,.2f} "
            f"(based on {benchmark.get('sample_size', 'N/A')} bills)."
        )

    result = {
        "type": "benchmark_outlier",
        "severity": severity,
        "line_item": item,
        "charged": charged,
        "median_charged": median,
        "p25_charged": p25,
        "p75_charged": p75,
        "sample_size": benchmark.get("sample_size", 0),
        "region": benchmark.get("region", "national"),
        "evidence": {
            "sample_size": benchmark.get("sample_size", 0),
            "region_source": benchmark.get("region", "national"),
        },
        "potential_savings": round(max(0, charged - median), 2),
        "message": message,
    }
    if patient_resp is not None:
        result["patient_responsibility"] = patient_resp
    return result
