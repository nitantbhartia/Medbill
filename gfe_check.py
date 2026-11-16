"""Good Faith Estimate vs bill: the difference, the CMS dispute threshold, the deadline, and the paperwork."""

from __future__ import annotations

import math
from datetime import date, timedelta

import config


def _parse_amount(value, label: str, problems: list[str]) -> float | None:
    text = str(value if value is not None else "").replace("$", "").replace(",", "").strip()
    try:
        amount = float(text)
    except ValueError:
        problems.append(f"Enter the {label} as a number, like 1850.00.")
        return None
    if not math.isfinite(amount) or amount < 0 or amount > config.GFE_MAX_AMOUNT_USD:
        problems.append(f"Enter a {label} between $0 and ${config.GFE_MAX_AMOUNT_USD:,}.")
        return None
    return round(amount, 2)


def _parse_bill_date(value, today: date, problems: list[str]) -> date | None:
    try:
        bill_date = date.fromisoformat(str(value or "").strip())
    except ValueError:
        problems.append("Enter the date printed on the bill.")
        return None
    if bill_date > today:
        problems.append("The bill date can't be in the future.")
        return None
    return bill_date


def _money(amount: float) -> str:
    return f"${amount:,.2f}"


def _dispute_letter(provider: str, estimate: float, billed: float, bill_date: date, today: date) -> str:
    return "\n".join([
        f"{today:%B} {today.day}, {today.year}",
        "",
        "Your name: ______________________________",
        "Your address: ____________________________",
        "Account number: _________________________",
        "",
        f"Billing Department, {provider}",
        "",
        "Re: Request for a corrected bill that matches my Good Faith Estimate",
        "",
        "Dear Billing Department,",
        "",
        f"I am a self-pay patient. Before my care, {provider} gave me a Good Faith Estimate "
        f"with total expected charges of {_money(estimate)}. The bill dated {bill_date:%B} {bill_date.day}, "
        f"{bill_date.year} totals {_money(billed)}, which is {_money(billed - estimate)} more than the estimate.",
        "",
        "Please send me, in writing:",
        "",
        "- a corrected bill, or a written explanation of why each charge above the estimate could not have been "
        "included in the estimate",
        "- an itemized bill with billing codes, so I can compare it to the estimate line by line",
        "",
        "I have enclosed a copy of the Good Faith Estimate and the bill. Please do not send this account to "
        "collections while it is under review.",
        "",
        "If we cannot agree on the amount, I may use the federal patient-provider dispute resolution process "
        "run by the Centers for Medicare & Medicaid Services.",
        "",
        "Thank you,",
        "",
        "______________________________",
    ])


def _checklist() -> list[str]:
    return [
        "A copy of your Good Faith Estimate (paper or digital).",
        "A copy of your bill. Send copies only, never originals.",
        "Your provider's name and contact information.",
        f"The ${config.GFE_DISPUTE_FEE_USD} administrative fee. It is non-refundable; if the dispute is decided "
        "in your favor, it is deducted from what you owe the provider.",
        "Your own record of the date you got the estimate and that you told the provider you were not using insurance.",
    ]


def check_estimate(payload: dict, today: date | None = None) -> dict:
    """Compare a bill to its Good Faith Estimate. Raises ValueError listing what to fix."""
    today = today or date.today()
    problems: list[str] = []
    provider = str(payload.get("provider_name") or "").strip()[: config.GFE_FIELD_MAX_CHARS]
    if not provider:
        problems.append("Add the provider or facility name.")
    estimate = _parse_amount(payload.get("estimate_total"), "Good Faith Estimate total", problems)
    billed = _parse_amount(payload.get("bill_total"), "bill total", problems)
    bill_date = _parse_bill_date(payload.get("bill_date"), today, problems)
    self_pay = payload.get("self_pay")
    if not isinstance(self_pay, bool):
        problems.append("Say whether you were uninsured or paid without using insurance.")
    if problems:
        raise ValueError(" ".join(problems))

    difference = round(billed - estimate, 2)
    deadline = bill_date + timedelta(days=config.GFE_DISPUTE_DEADLINE_DAYS)
    meets_threshold = difference >= config.GFE_DISPUTE_THRESHOLD_USD
    return {
        "provider_name": provider,
        "difference": difference,
        "meets_threshold": meets_threshold,
        "threshold": config.GFE_DISPUTE_THRESHOLD_USD,
        "self_pay": self_pay,
        "deadline": deadline.isoformat(),
        "days_left": (deadline - today).days,
        "info_url": config.GFE_DISPUTE_INFO_URL,
        "filing_url": config.GFE_DISPUTE_FILING_URL,
        "fee": config.GFE_DISPUTE_FEE_USD,
        "letter": _dispute_letter(provider, estimate, billed, bill_date, today) if self_pay and difference > 0 else None,
        "checklist": _checklist() if self_pay and meets_threshold else None,
    }
