"""Appeal rules by plan type: filing windows, decision windows and the next level. No AI, no DB."""

from datetime import date, timedelta

import config

VERIFIED_ON = "2026-11-20"
_DECISION_DAYS = config.APPEAL_DECISION_DAYS
_EXTERNAL_GOES_TO = (
    "An independent reviewer outside your insurer decides. Your final denial letter says how to ask for it."
)

RULES = {
    "individual": {
        "level": "internal", "level_label": "Internal appeal",
        "file_within_days": config.APPEAL_FILING_DAYS["individual"],
        "decision_days": _DECISION_DAYS,
        "next_level": "external", "next_level_label": "External review",
        "next_level_days": config.APPEAL_EXTERNAL_REVIEW_DAYS, "next_level_automatic": False,
        "next_level_goes_to": _EXTERNAL_GOES_TO,
        "source_url": "https://www.healthcare.gov/appeal-insurance-company-decision/internal-appeals",
        "verified_on": VERIFIED_ON,
    },
    "employer": {
        "level": "internal", "level_label": "Internal appeal",
        "file_within_days": config.APPEAL_FILING_DAYS["employer"],
        "decision_days": _DECISION_DAYS,
        "next_level": "external", "next_level_label": "External review",
        "next_level_days": config.APPEAL_EXTERNAL_REVIEW_DAYS, "next_level_automatic": False,
        "next_level_goes_to": (
            "An independent reviewer decides, through a federal or state process. Your final denial letter says "
            "which one and how to ask. Some employer plans have a second internal appeal first."
        ),
        "source_url": "https://www.hhs.gov/guidance/sites/default/files/hhs-guidance-documents/Internal-Appeals-External-Review-Slides-2022.pdf",
        "verified_on": VERIFIED_ON,
    },
    "medicare_advantage": {
        "level": "internal", "level_label": "Plan reconsideration",
        "file_within_days": config.APPEAL_FILING_DAYS["medicare_advantage"],
        "decision_days": _DECISION_DAYS,
        "next_level": "ire", "next_level_label": "Independent Review Entity (IRE)",
        "next_level_days": None, "next_level_automatic": True,
        "next_level_goes_to": (
            "Your plan must send your case to Medicare's independent reviewer automatically. "
            "You don't need to file anything."
        ),
        "source_url": "https://www.medicare.gov/providers-services/claims-appeals-complaints/appeals/medicare-health-plans",
        "verified_on": VERIFIED_ON,
    },
    "original_medicare": {
        "level": "internal", "level_label": "Redetermination",
        "file_within_days": config.APPEAL_FILING_DAYS["original_medicare"],
        "decision_days": dict.fromkeys(_DECISION_DAYS, config.APPEAL_ORIGINAL_MEDICARE_DECISION_DAYS),
        "next_level": "qic", "next_level_label": "QIC reconsideration",
        "next_level_days": config.APPEAL_QIC_DAYS, "next_level_automatic": False,
        "next_level_goes_to": (
            "A Qualified Independent Contractor (QIC) reviews the decision. "
            "The redetermination notice explains how to ask."
        ),
        "source_url": "https://cmsnationaltrainingprogram.cms.gov/sites/default/files/shared/Appeals%20Processes_Portrait_FINAL_508.pdf",
        "verified_on": VERIFIED_ON,
    },
    "medicaid": {
        "level": "internal", "level_label": "Plan appeal",
        "file_within_days": config.APPEAL_FILING_DAYS["medicaid"],
        "decision_days": None,  # varies by state
        "next_level": "fair_hearing", "next_level_label": "State fair hearing",
        "next_level_days": config.APPEAL_FAIR_HEARING_DAYS, "next_level_automatic": False,
        "next_level_goes_to": "Your state holds a fair hearing. The plan's decision letter explains how to ask for one.",
        "source_url": "https://www.ecfr.gov/current/title-42/chapter-IV/subchapter-C/part-438/subpart-F/section-438.402",
        "verified_on": VERIFIED_ON,
    },
}


def route(plan_type: str | None, service_timing: str | None, notice_date: date | None, printed_deadline: date | None) -> dict:
    """Where the case stands: appeal level, file-by date (and where it came from), decision window, next level."""
    rule = RULES.get(plan_type or "")
    file_by, deadline_source = None, None
    if printed_deadline:
        file_by, deadline_source = printed_deadline, "letter"
    elif rule and notice_date:
        file_by, deadline_source = notice_date + timedelta(days=rule["file_within_days"]), "default"
    if not rule:
        return {
            "level": "internal", "level_label": "Appeal", "file_by": file_by, "deadline_source": deadline_source,
            "decision_window_days": None, "next_level_label": None, "next_level_days": None, "source_url": None,
        }
    return {
        "level": rule["level"], "level_label": rule["level_label"], "file_by": file_by,
        "deadline_source": deadline_source,
        "decision_window_days": (rule["decision_days"] or {}).get(service_timing),
        "next_level_label": rule["next_level_label"], "next_level_days": rule["next_level_days"],
        "source_url": rule["source_url"],
    }


def decision_due(plan_type: str | None, service_timing: str | None, sent_on: date) -> date | None:
    """When the insurer must decide, or None when the window is unknown for this plan or timing."""
    days = route(plan_type, service_timing, None, None)["decision_window_days"]
    return sent_on + timedelta(days=days) if days else None


def next_level(plan_type: str | None, decided_on: date) -> dict | None:
    """What to do after an upheld denial, or None for an unknown plan type."""
    rule = RULES.get(plan_type or "")
    if not rule:
        return None
    days = rule["next_level_days"]
    return {
        "level": rule["next_level"], "level_label": rule["next_level_label"],
        "file_by": decided_on + timedelta(days=days) if days else None,
        "automatic": rule["next_level_automatic"], "goes_to": rule["next_level_goes_to"],
        "source_url": rule["source_url"],
    }
