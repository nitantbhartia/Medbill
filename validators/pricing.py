from db import get_db
import config


def get_medicare_rate(cpt_code: str, locality: str = "0000000") -> float | None:
    """Look up the Medicare facility rate for a CPT code and locality."""
    with get_db() as db:
        row = db.execute(
            "SELECT facility_rate FROM medicare_rates "
            "WHERE cpt_code = ? AND locality = ? "
            "ORDER BY effective_year DESC LIMIT 1",
            (cpt_code, locality),
        ).fetchone()
        if row and row["facility_rate"]:
            return row["facility_rate"]

        # Fall back to any locality
        row = db.execute(
            "SELECT facility_rate FROM medicare_rates "
            "WHERE cpt_code = ? AND facility_rate IS NOT NULL "
            "ORDER BY effective_year DESC LIMIT 1",
            (cpt_code,),
        ).fetchone()
        return row["facility_rate"] if row else None


def get_medicare_locality(zip_code: str) -> str:
    """Map a zip code to a Medicare pricing locality. Simplified lookup."""
    with get_db() as db:
        row = db.execute(
            "SELECT DISTINCT locality FROM medicare_rates "
            "WHERE state = (SELECT state FROM users WHERE zip_code = ? LIMIT 1) LIMIT 1",
            (zip_code,),
        ).fetchone()
    return row["locality"] if row else "0000000"


def check_pricing(item: dict, locality: str) -> dict | None:
    """Compare a line item's charge against Medicare rates."""
    if not item.get("cpt_code") or not item.get("charged_amount"):
        return None

    medicare_rate = get_medicare_rate(item["cpt_code"], locality)
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

    return {
        "type": "price_markup",
        "severity": severity,
        "line_item": item,
        "charged": item["charged_amount"],
        "medicare_rate": medicare_rate,
        "markup_multiple": round(markup, 1),
        "potential_savings": max(0, round(savings, 2)),
        "message": (
            f"You were charged ${item['charged_amount']:,.2f} for {item['description']}. "
            f"Medicare pays ${medicare_rate:,.2f} for this in your area. "
            f"That's a {markup:.1f}x markup."
        ),
    }
