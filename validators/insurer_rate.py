"""The insurer's contracted rate at this hospital, from the hospital's own price file."""

import config
from payer_rates import find_contracted_rate


def check_insurer_rate(item: dict, facility_id: str, insurer: str, hospital_name: str) -> dict | None:
    """Flag a line whose amount the patient is asked to pay is above the insurer's contracted rate for that code."""
    code, charged = item.get("cpt_code"), item.get("charged_amount")
    if not code or not charged:
        return None
    contracted = find_contracted_rate(facility_id, code, insurer)
    if not contracted:
        return None
    # With an insurance breakdown the patient's share is what they owe; without one the bill asks for the full charge.
    asked = item.get("patient_responsibility")
    if asked is None:
        asked = charged if item.get("insurance_paid") is None and item.get("insurance_adjustment") is None else None
    if asked is None or asked <= contracted["rate"] * config.INSURER_RATE_TOLERANCE:
        return None
    savings = round(min(asked - contracted["rate"], charged), 2)
    return {
        "type": "insurer_rate",
        "severity": "high",
        "line_item": item,
        "charged": charged,
        "insurer": contracted["payer"],
        "contracted_rate": contracted["rate"],
        "rate_source_url": contracted["source_url"],
        "rate_year": contracted["year"],
        "hospital_name": hospital_name,
        "potential_savings": savings,
        "message": (f"{contracted['payer']}'s contracted rate at {hospital_name} for code {code} is "
                    f"${contracted['rate']:,.2f}. This bill asks for ${asked:,.2f}."),
        "evidence": {"source": "hospital_price_file", "data_date": contracted["file_updated"], "sample_size": 1,
                     "limitations": "Contracted rates vary by plan. Confirm your plan with the hospital."},
    }
