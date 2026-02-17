from datetime import datetime

from db import get_db
import config
from validators.geo import get_medicare_locality as _geo_medicare_locality, extract_zip


def get_medicare_rate(cpt_code: str, locality: str = "0000000", date_of_service: str | None = None) -> float | None:
    """
    Look up the Medicare facility rate for a CPT code and locality.
    If date_of_service is provided, match rates by that year first.
    """
    target_year = None
    if date_of_service:
        try:
            target_year = datetime.strptime(date_of_service, "%Y-%m-%d").year
        except ValueError:
            pass

    with get_db() as db:
        # Try exact locality + year match
        if target_year:
            row = db.execute(
                "SELECT facility_rate FROM medicare_rates "
                "WHERE cpt_code = ? AND locality = ? AND effective_year = ?",
                (cpt_code, locality, target_year),
            ).fetchone()
            if row and row["facility_rate"]:
                return row["facility_rate"]

        # Try exact locality, most recent year
        row = db.execute(
            "SELECT facility_rate FROM medicare_rates "
            "WHERE cpt_code = ? AND locality = ? "
            "ORDER BY effective_year DESC LIMIT 1",
            (cpt_code, locality),
        ).fetchone()
        if row and row["facility_rate"]:
            return row["facility_rate"]

        # Fall back to any locality, match year if available
        if target_year:
            row = db.execute(
                "SELECT facility_rate FROM medicare_rates "
                "WHERE cpt_code = ? AND effective_year = ? AND facility_rate IS NOT NULL "
                "LIMIT 1",
                (cpt_code, target_year),
            ).fetchone()
            if row and row["facility_rate"]:
                return row["facility_rate"]

        # Final fallback: any locality, most recent year
        row = db.execute(
            "SELECT facility_rate FROM medicare_rates "
            "WHERE cpt_code = ? AND facility_rate IS NOT NULL "
            "ORDER BY effective_year DESC LIMIT 1",
            (cpt_code,),
        ).fetchone()
        return row["facility_rate"] if row else None


def get_medicare_locality(zip_code: str, provider_address: str | None = None) -> str:
    """Resolve Medicare pricing locality using ZIP-driven mapping first."""
    return _geo_medicare_locality(zip_code, provider_address)


def validate_geo_match(user_zip: str, provider_address: str | None) -> str | None:
    """
    Check if the user's zip code and provider address are in different areas.
    Returns a warning string if mismatch, else None.
    """
    if not provider_address or not user_zip:
        return None

    provider_zip = extract_zip(provider_address)
    if not provider_zip:
        return None

    if provider_zip[:3] == user_zip[:3]:
        return None  # same 3-digit prefix = same metro area

    return (
        f"Your zip code ({user_zip}) and the provider's address appear to be "
        f"in different areas. Medicare rates vary by location — make sure "
        f"your zip code is correct for the most accurate comparison."
    )


def get_opps_rate(cpt_code: str, date_of_service: str | None = None) -> float | None:
    """Look up the Medicare OPPS (hospital outpatient) rate for a CPT code."""
    target_year = None
    if date_of_service:
        try:
            target_year = datetime.strptime(date_of_service, "%Y-%m-%d").year
        except ValueError:
            pass

    with get_db() as db:
        if target_year:
            row = db.execute(
                "SELECT national_payment_rate FROM hospital_opps_rates "
                "WHERE cpt_code = ? AND effective_year = ?",
                (cpt_code, target_year),
            ).fetchone()
            if row and row["national_payment_rate"]:
                return row["national_payment_rate"]

        row = db.execute(
            "SELECT national_payment_rate FROM hospital_opps_rates "
            "WHERE cpt_code = ? AND national_payment_rate IS NOT NULL "
            "ORDER BY effective_year DESC LIMIT 1",
            (cpt_code,),
        ).fetchone()
        return row["national_payment_rate"] if row else None


def check_pricing(item: dict, locality: str) -> dict | None:
    """Compare a line item's charge against Medicare rates."""
    if not item.get("cpt_code") or not item.get("charged_amount"):
        return None

    medicare_rate = get_medicare_rate(
        item["cpt_code"], locality, item.get("date_of_service")
    )
    if not medicare_rate:
        return None

    markup = item["charged_amount"] / medicare_rate

    if markup > config.HIGH_MARKUP_THRESHOLD:
        severity = "high"
    elif markup > config.MEDICARE_MARKUP_THRESHOLD:
        severity = "medium"
    else:
        return None

    savings = item["charged_amount"] - (medicare_rate * config.MEDICARE_MARKUP_THRESHOLD)

    opps_rate = get_opps_rate(item["cpt_code"], item.get("date_of_service"))

    patient_resp = item.get("patient_responsibility")

    if patient_resp is not None:
        message = (
            f"Your provider billed ${item['charged_amount']:,.2f} for {item['description']}. "
            f"After insurance, your responsibility is ${patient_resp:,.2f}. "
            f"Medicare pays ${medicare_rate:,.2f} for this service."
        )
    else:
        message = (
            f"You were charged ${item['charged_amount']:,.2f} for {item['description']}. "
            f"Medicare pays ${medicare_rate:,.2f} for this in your area. "
            f"That's a {markup:.1f}x markup."
        )
    if opps_rate:
        total_medicare = medicare_rate + opps_rate
        message += (
            f" (Medicare total with hospital fee: ${total_medicare:,.2f})"
        )

    result = {
        "type": "price_markup",
        "severity": severity,
        "line_item": item,
        "charged": item["charged_amount"],
        "medicare_rate": medicare_rate,
        "markup_multiple": round(markup, 1),
        "potential_savings": max(0, round(savings, 2)),
        "message": message,
    }
    if patient_resp is not None:
        result["patient_responsibility"] = patient_resp
    if opps_rate:
        result["opps_rate"] = opps_rate
        result["total_medicare"] = round(medicare_rate + opps_rate, 2)

    return result
