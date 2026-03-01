"""Savings Estimator — instant overcharge estimate from bill amount + hospital."""

from __future__ import annotations

from db import get_db
from tools_engine import FPL_2026


def estimate_savings(
    bill_amount: float,
    hospital_name: str = "",
    zip_code: str = "",
    insurance_status: str = "insured",
    income: float = 0,
    household_size: int = 0,
) -> dict:
    """Return a personalized savings estimate and action plan."""
    hospital = _find_hospital(hospital_name) if hospital_name.strip() else None

    markup = _get_markup(hospital)
    estimated_fair = bill_amount / markup if markup and markup > 1 else bill_amount
    estimated_savings = max(0, bill_amount - estimated_fair)

    charity_eligible = _check_charity_care(hospital, income, household_size)
    actions = _build_actions(
        bill_amount, hospital, markup, charity_eligible, insurance_status,
    )

    return {
        "bill_amount": bill_amount,
        "hospital": _hospital_summary(hospital) if hospital else None,
        "markup": round(markup, 1) if markup else None,
        "estimated_fair_price": round(estimated_fair, 2),
        "estimated_savings_low": round(estimated_savings * 0.4, 2),
        "estimated_savings_high": round(estimated_savings * 0.85, 2),
        "charity_care": charity_eligible,
        "actions": actions,
        "insurance_status": insurance_status,
    }


def _find_hospital(name: str) -> dict | None:
    token = name.strip()
    if not token:
        return None
    like = f"%{token}%"
    with get_db() as db:
        row = db.execute(
            """
            SELECT h.facility_id, h.name, h.city, h.state, h.ownership,
                   h.is_nonprofit,
                   COALESCE(fbm.billing_grade, bm.billing_grade) AS billing_grade,
                   COALESCE(fbm.avg_markup, bm.avg_markup_vs_medicare) AS avg_markup
            FROM hospitals h
            LEFT JOIN facility_billing_metrics fbm ON fbm.facility_id = h.facility_id
            LEFT JOIN billing_metrics bm ON bm.facility_id = h.facility_id
            WHERE h.name LIKE ?
            ORDER BY CASE WHEN lower(h.name) = lower(?) THEN 0 ELSE 1 END, h.name
            LIMIT 1
            """,
            (like, token),
        ).fetchone()
    return dict(row) if row else None


def _get_markup(hospital: dict | None) -> float | None:
    if not hospital:
        return 3.4  # national average
    return hospital.get("avg_markup") or 3.4


def _hospital_summary(hospital: dict) -> dict:
    return {
        "name": hospital.get("name"),
        "city": hospital.get("city"),
        "state": hospital.get("state"),
        "billing_grade": (hospital.get("billing_grade") or "N/A").upper(),
        "avg_markup": round(hospital.get("avg_markup") or 0, 1),
        "is_nonprofit": bool(hospital.get("is_nonprofit")),
        "ownership": hospital.get("ownership"),
    }


def _check_charity_care(
    hospital: dict | None, income: float, household_size: int,
) -> dict | None:
    if not income or household_size < 1:
        return None

    size = min(household_size, 8)
    fpl_base = FPL_2026.get(size, FPL_2026[8] + ((size - 8) * 5500))
    fpl_pct = (income / fpl_base) * 100 if fpl_base else 0

    is_nonprofit = False
    if hospital:
        is_nonprofit = bool(hospital.get("is_nonprofit"))
        ownership = (hospital.get("ownership") or "").lower()
        if not is_nonprofit and ("nonprofit" in ownership or "non-profit" in ownership):
            is_nonprofit = True

    if fpl_pct <= 200:
        discount = "100% (full forgiveness likely)"
    elif fpl_pct <= 300:
        discount = "75-100%"
    elif fpl_pct <= 400:
        discount = "25-75%"
    else:
        discount = "unlikely"

    return {
        "fpl_percent": round(fpl_pct, 1),
        "estimated_discount": discount,
        "is_nonprofit": is_nonprofit,
        "eligible": fpl_pct <= 400,
    }


def _build_actions(
    bill_amount: float,
    hospital: dict | None,
    markup: float | None,
    charity: dict | None,
    insurance_status: str,
) -> list[dict]:
    actions = []

    # 1. Scan for errors (always recommended)
    actions.append({
        "priority": 1,
        "title": "Scan your bill for errors",
        "description": "Upload your bill and our AI checks every charge against Medicare rates, flags duplicates, unbundling, and coding mistakes.",
        "impact": "high",
        "url": "/scan",
        "button": "Scan My Bill — Free",
    })

    # 2. Charity care (if eligible)
    if charity and charity["eligible"] and charity.get("is_nonprofit", True):
        actions.append({
            "priority": 2,
            "title": "Apply for charity care",
            "description": f"At {charity['fpl_percent']:.0f}% of FPL, you likely qualify for {charity['estimated_discount']} off your bill.",
            "impact": "high",
            "url": "/charity-care",
            "button": "Check Eligibility",
        })

    # 3. Negotiate (for high-markup hospitals)
    if markup and markup > 3:
        actions.append({
            "priority": 3,
            "title": "Negotiate using Medicare benchmarks",
            "description": f"This hospital charges {markup:.1f}x Medicare rates on average. Use that data to negotiate a lower bill.",
            "impact": "high" if markup > 5 else "medium",
            "url": "/tools/medical-bill-negotiation-script-generator/",
            "button": "Get Negotiation Script",
        })

    # 4. Dispute (for bills with likely errors)
    if bill_amount > 500:
        actions.append({
            "priority": 4,
            "title": "File a formal dispute",
            "description": "Send a written dispute letter requesting an itemized review and billing correction.",
            "impact": "medium",
            "url": "/tools/medical-bill-dispute-letter-generator/",
            "button": "Generate Dispute Letter",
        })

    # 5. Insurance-specific
    if insurance_status == "uninsured":
        actions.append({
            "priority": 2,
            "title": "Request the uninsured/cash-pay rate",
            "description": "Hospitals are required to offer self-pay discounts. These are often 40-60% below list price.",
            "impact": "high",
            "url": "/guides/hospital-cash-pay-rates",
            "button": "Learn More",
        })

    # 6. No Surprises Act
    if insurance_status == "out_of_network":
        actions.append({
            "priority": 2,
            "title": "Check No Surprises Act protections",
            "description": "If this was emergency care or at an in-network facility, federal law may cap your costs.",
            "impact": "high",
            "url": "/tools/surprise-bill-checker/",
            "button": "Check Protections",
        })

    actions.sort(key=lambda a: a["priority"])
    return actions
