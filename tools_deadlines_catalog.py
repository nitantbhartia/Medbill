"""Catalog entries for the date-math tools in tools_deadlines.py."""

from __future__ import annotations

from typing import Any

FOOTNOTE = "Informational only, not legal advice. Your hospital and your state have the final word."
FA_GUIDE = "/guides/hospital-financial-assistance-charity-care/"
PAID_GUIDE = "/guides/financial-assistance-after-paying-hospital-bill/"
MEDICAID_GUIDE = "/guides/hospital-bill-medicaid-pending/"
LEAD_MAGNET = {
    "key": "charity_care_guide",
    "title": "Free guide: How to Apply for Hospital Financial Assistance (Step by Step)",
    "description": "Includes sample application, required documents checklist, and what to say.",
    "button_label": "Send Me the Guide",
}


def _cta(headline: str, body: str, guide_label: str, guide_url: str) -> dict[str, str]:
    return {
        "headline": headline,
        "body": body,
        "primary_label": "Upload My Bill to Check It",
        "primary_url": "/scan",
        "secondary_label": guide_label,
        "secondary_url": guide_url,
        "footnote": FOOTNOTE,
    }


DEADLINE_TOOLS: list[dict[str, Any]] = [
    {
        "slug": "hospital-financial-assistance-deadline",
        "title": "Hospital Financial Assistance Deadline Calculator",
        "category": "Debt and collections",
        "description": "See when a nonprofit hospital may start collection actions and how long you have to apply for financial assistance under IRS 501(r) rules.",
        "keywords": ["hospital financial assistance deadline", "501r 240 day application period", "hospital 120 days collections"],
        "inline_nudge": "Nonprofit hospitals must wait at least 120 days after the first bill before collection actions, and must take aid applications for at least 240 days.",
        "form_fields": [
            {"name": "first_bill_date", "label": "Date of the first bill after discharge (or discharge date if no bill yet)", "type": "date"},
            {"name": "hospital_nonprofit", "label": "Is the hospital a nonprofit?", "type": "select", "options": ["unsure", "yes", "no"]},
        ],
        "lead_magnet": LEAD_MAGNET,
        "ctas": {
            "window_open": _cta(
                "You are still inside the application period.",
                "Apply for financial assistance before the deadline. Upload your bill and we will check it for errors while you apply.",
                "How to Apply for Financial Assistance", FA_GUIDE,
            ),
            "window_closed": _cta(
                "The 240-day minimum has passed, but you can still ask.",
                "Many hospitals accept late applications, and some states allow more time. Upload your bill to check it for errors.",
                "Already Paid? You May Still Get Help", PAID_GUIDE,
            ),
            "for_profit": _cta(
                "501(r) deadlines do not apply to for-profit hospitals.",
                "The hospital may still have its own assistance policy, and your state may set rules. Upload your bill to check it for errors.",
                "Hospital Financial Assistance Guide", FA_GUIDE,
            ),
        },
    },
    {
        "slug": "medicaid-retroactive-coverage-checker",
        "title": "Medicaid Retroactive Coverage Checker",
        "category": "Insurance problems",
        "description": "Check whether a past hospital visit falls inside Medicaid's retroactive coverage window, including the shorter windows for applications filed from January 1, 2027.",
        "keywords": ["medicaid retroactive coverage", "medicaid 3 month retroactive", "medicaid retroactive coverage 2027"],
        "inline_nudge": "Medicaid can pay for care from before you applied, but only for a few months back, and the window gets shorter for applications filed from January 1, 2027.",
        "form_fields": [
            {"name": "care_date", "label": "Date of hospital care", "type": "date"},
            {"name": "application_date", "label": "Date the Medicaid application was (or will be) filed", "type": "date"},
            {"name": "expansion_adult", "label": "Is the applicant an adult in the ACA Medicaid expansion group?", "type": "select", "options": ["unsure", "yes", "no"]},
        ],
        "lead_magnet": LEAD_MAGNET,
        "ctas": {
            "inside_window": _cta(
                "This care date is inside the retroactive window.",
                "Tell the hospital you applied and ask it to hold the bill. Upload your bill to check it for errors in the meantime.",
                "Hospital Bill With Medicaid Pending", MEDICAID_GUIDE,
            ),
            "depends_on_group": _cta(
                "This care date is covered for some applicants but not others.",
                "Check whether you are in the ACA expansion group, and ask the hospital about financial assistance too.",
                "Hospital Bill With Medicaid Pending", MEDICAID_GUIDE,
            ),
            "outside_window": _cta(
                "This care date is before the retroactive window.",
                "Hospital financial assistance can still help with this bill. Upload it to check for errors.",
                "Hospital Financial Assistance Guide", FA_GUIDE,
            ),
            "current_coverage": _cta(
                "This care is in or after the month of the application.",
                "If you are approved, regular coverage may pay it. Ask the hospital to hold the bill until Medicaid decides.",
                "Hospital Bill With Medicaid Pending", MEDICAID_GUIDE,
            ),
        },
    },
]
