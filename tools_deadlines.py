"""Date-math free tools: the 501(r) collection timeline and the Medicaid retroactive coverage window."""

from __future__ import annotations

from datetime import date, datetime, timedelta
from typing import Any

import config

DATE_FORMATS = ("%Y-%m-%d", "%m/%d/%Y")
RETRO_CHANGE_DATE = date.fromisoformat(config.MEDICAID_RETRO_CHANGE_DATE)
TOOL_NOTE = "Informational only, not legal advice. No result here is a promise of coverage or of a lower bill."


def parse_date(value: Any, label: str) -> date:
    text = str(value or "").strip()
    if not text:
        raise ValueError(f"Enter the {label}.")
    for fmt in DATE_FORMATS:
        try:
            return datetime.strptime(text, fmt).date()
        except ValueError:
            continue
    raise ValueError(f"Enter the {label} as a date like 2026-11-20.")


def _answer(payload: dict[str, Any], key: str) -> str:
    value = str(payload.get(key) or "").strip().lower()
    return value if value in ("yes", "no") else "unsure"


def _fmt(d: date) -> str:
    return f"{d:%B} {d.day}, {d.year}"


def _fmt_relative(d: date, today: date) -> str:
    delta = (d - today).days
    if delta == 0:
        return f"{_fmt(d)} (today)"
    if delta > 0:
        return f"{_fmt(d)} ({delta} days from today)"
    return f"{_fmt(d)} ({-delta} days ago)"


# --- Tool 1: hospital-financial-assistance-deadline ---

def collection_timeline(first_bill: date) -> tuple[date, date]:
    """Earliest extraordinary collection action date and the end of the 501(r) application period."""
    earliest_action = first_bill + timedelta(days=config.FA_501R_ECA_WAIT_DAYS)
    application_end = first_bill + timedelta(days=config.FA_501R_APPLICATION_PERIOD_DAYS)
    return earliest_action, application_end


def _for_profit_result(first_bill: date) -> tuple[str, str, dict[str, Any]]:
    summary = (
        "The federal 501(r) deadlines apply only to nonprofit hospitals, so they do not set the timeline for a for-profit hospital. "
        "Your state's law and the hospital's own policy do."
    )
    details = {
        "first_bill_date": _fmt(first_bill),
        "next_steps": [
            "Ask the billing office for the hospital's written financial assistance policy. Many for-profit hospitals have one even though federal law does not require it.",
            "Check your state's rules. Some states require all hospitals to offer charity care or limit how and when they can collect.",
            "Ask for an itemized bill and check it for errors before you pay.",
            "Not sure the hospital is for-profit? Ask whether it is a 501(c)(3) nonprofit, or search its name in the IRS Tax Exempt Organization Search.",
        ],
        "note": TOOL_NOTE,
    }
    return "for_profit", summary, details


def _fa_next_steps(today: date, earliest_action: date, application_end: date) -> list[str]:
    if today > application_end:
        return [
            "Ask for financial assistance anyway. The 240 days are a minimum: many hospitals accept later applications, and some states allow more time.",
            "If collection actions started before the 120-day mark, or without written notice at least 30 days ahead, ask the hospital to reverse them.",
            "Ask for an itemized bill and check it for errors.",
        ]
    steps = [f"Apply for financial assistance by {_fmt(application_end)}. Ask for the application and the plain-language summary of the policy."]
    if today < earliest_action:
        steps.append(
            f"Before {_fmt(earliest_action)}, the hospital may not report you to credit bureaus, sell the debt, take you to court, or take similar steps. "
            "It must also send written notice at least 30 days before starting any of them."
        )
    else:
        steps.append("Collection actions may be allowed now, but only after written notice at least 30 days ahead. Applying now pauses them while the hospital reviews your application.")
    steps.append("Keep a copy of everything you send and write down the date you sent it.")
    steps.append("If you entered the discharge date because no bill has come yet, the real dates start from the first bill, so they will be later.")
    return steps


def run_financial_assistance_deadline(payload: dict[str, Any], today: date | None = None) -> tuple[str, str, dict[str, Any]]:
    today = today or date.today()
    first_bill = parse_date(payload.get("first_bill_date"), "date of the first bill after discharge")
    nonprofit = _answer(payload, "hospital_nonprofit")
    if nonprofit == "no":
        return _for_profit_result(first_bill)

    earliest_action, application_end = collection_timeline(first_bill)
    state = "window_open" if today <= application_end else "window_closed"
    lead = "If the hospital is a nonprofit, under" if nonprofit == "unsure" else "Under"
    summary = (
        f"{lead} IRS 501(r) rules, collection actions like credit reporting or court action may not start before {_fmt(earliest_action)}, "
        f"and the hospital must accept financial assistance applications through at least {_fmt(application_end)}."
    )
    details = {
        "first_bill_date": _fmt(first_bill),
        "earliest_collection_action_date": _fmt_relative(earliest_action, today),
        "application_period_ends": _fmt_relative(application_end, today),
        "next_steps": _fa_next_steps(today, earliest_action, application_end),
        "sources": [config.FA_501R_ECA_SOURCE_URL, config.FA_501R_APPLICATION_PERIOD_SOURCE_URL],
        "note": TOOL_NOTE,
    }
    return state, summary, details


# --- Tool 2: medicaid-retroactive-coverage-checker ---

def month_start(d: date, months_back: int = 0) -> date:
    """First day of the month `months_back` months before d's month (negative moves forward)."""
    index = d.year * 12 + d.month - 1 - months_back
    return date(index // 12, index % 12 + 1, 1)


def retro_months(application: date, expansion_adult: bool) -> int:
    if application < RETRO_CHANGE_DATE:
        return config.MEDICAID_RETRO_MONTHS
    return config.MEDICAID_RETRO_MONTHS_EXPANSION_ADULT if expansion_adult else config.MEDICAID_RETRO_MONTHS_OTHER


def retro_window_start(application: date, expansion_adult: bool) -> date:
    return month_start(application, retro_months(application, expansion_adult))


def latest_application_date(care: date, expansion_adult: bool) -> date:
    """Last day an application can be filed and still have its retroactive window reach the care date."""
    application_month = month_start(care)
    for months_after in range(config.MEDICAID_RETRO_MONTHS, 0, -1):
        candidate = month_start(care, -months_after)
        if retro_months(candidate, expansion_adult) >= months_after:
            application_month = candidate
            break
    return month_start(application_month, -1) - timedelta(days=1)


def _rule_text(application: date, group: str) -> str:
    if application < RETRO_CHANGE_DATE:
        return f"{config.MEDICAID_RETRO_MONTHS} months before the month of application (42 CFR 435.915)"
    by_group = {
        "yes": f"{config.MEDICAID_RETRO_MONTHS_EXPANSION_ADULT} month for ACA expansion adults",
        "no": f"{config.MEDICAID_RETRO_MONTHS_OTHER} months for applicants outside the ACA expansion group",
        "unsure": f"{config.MEDICAID_RETRO_MONTHS_EXPANSION_ADULT} month for ACA expansion adults, {config.MEDICAID_RETRO_MONTHS_OTHER} for everyone else",
    }
    return f"{by_group[group]}, for applications filed on or after {_fmt(RETRO_CHANGE_DATE)} (P.L. 119-21 sec. 71112)"


def _medicaid_summary(state: str, care: date, application: date, start: date) -> str:
    if state == "current_coverage":
        return (
            f"Care on {_fmt(care)} is in or after the month of the application, so it is not retroactive. "
            "If you are approved, many states start coverage on the first day of the month you apply."
        )
    if state == "inside_window":
        return (
            f"Care on {_fmt(care)} falls inside the retroactive window. An application filed {_fmt(application)} "
            f"can reach back to {_fmt(start)}, if you were eligible in those months."
        )
    if state == "depends_on_group":
        return (
            f"Care on {_fmt(care)} falls inside the window only if you are not an ACA expansion adult. "
            "For applications filed on or after January 1, 2027, expansion adults get 1 month back and others get 2."
        )
    return f"Care on {_fmt(care)} is before the retroactive window, which starts {_fmt(start)} for an application filed {_fmt(application)}."


def _medicaid_next_steps(state: str, application: date, apply_by: date, today: date) -> list[str]:
    steps = []
    if state == "outside_window" and apply_by >= today:
        steps.append(f"To reach this care date, the application must be filed by {_fmt(apply_by)}.")
    if state == "depends_on_group" and apply_by >= today:
        steps.append(f"If you are an ACA expansion adult, file by {_fmt(apply_by)} to reach this care date.")
    if today < RETRO_CHANGE_DATE and application < RETRO_CHANGE_DATE:
        steps.append(f"Filing before {_fmt(RETRO_CHANGE_DATE)} keeps the 3-month window. Applications filed on or after that date get 1 or 2 months.")
    if state in ("inside_window", "depends_on_group"):
        steps.append("You must have been eligible (income, household, state residency) in the month of the care for it to be covered.")
        steps.append("On the application, say yes to unpaid medical bills in past months and list this hospital stay.")
    if state == "outside_window":
        steps.append("Ask the hospital about financial assistance. Nonprofit hospitals must offer it, and it can cover care Medicaid does not.")
    steps.append("Tell the hospital billing office you applied for Medicaid and ask it to hold the bill while the application is decided.")
    steps.append("State rules and waivers can differ. Confirm the window with your state Medicaid agency.")
    return steps


def run_medicaid_retro_checker(payload: dict[str, Any], today: date | None = None) -> tuple[str, str, dict[str, Any]]:
    today = today or date.today()
    care = parse_date(payload.get("care_date"), "date of hospital care")
    application = parse_date(payload.get("application_date"), "Medicaid application date")
    group = _answer(payload, "expansion_adult")

    groups = {"yes": [True], "no": [False], "unsure": [True, False]}[group]
    starts = [retro_window_start(application, expansion_adult) for expansion_adult in groups]
    if care >= month_start(application):
        state = "current_coverage"
    elif care >= max(starts):
        state = "inside_window"
    elif care >= min(starts):
        state = "depends_on_group"
    else:
        state = "outside_window"
    apply_by = latest_application_date(care, expansion_adult=group != "no")

    details = {
        "care_date": _fmt(care),
        "application_date": _fmt(application),
        "retroactive_rule": _rule_text(application, group),
        "retroactive_coverage_can_start": _fmt(min(starts)) if state == "depends_on_group" else _fmt(max(starts)),
        "next_steps": _medicaid_next_steps(state, application, apply_by, today),
        "sources": [config.MEDICAID_RETRO_SOURCE_URL, config.MEDICAID_RETRO_LAW_URL, config.MEDICAID_RETRO_CMS_BULLETIN_URL],
        "note": TOOL_NOTE,
    }
    return state, _medicaid_summary(state, care, application, max(starts)), details
