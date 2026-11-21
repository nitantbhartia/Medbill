"""The one CaseView every ClaimCoach route returns. A locked view never holds the paid kit."""

from __future__ import annotations

from datetime import date

import appeal_kit
import appeal_rules
import cc_cases
import cc_purchases
import config
from appeal_kit import _lower_label, _pretty_date
from appeal_letter import DENIAL_REASONS, PLAN_TYPES

SENT_STATUSES = ("sent", "decided")


def _iso(value) -> str | None:
    return str(value)[:10] if value else None


def next_level(case: dict) -> dict | None:
    """The next step after an upheld appeal. Its deadline counts from the date on the final denial letter, when known."""
    if case["outcome"] != "upheld":
        return None
    final_denial = date.fromisoformat(case["decision_letter_date"]) if case["decision_letter_date"] else None
    level = appeal_rules.next_level(case["plan_type"], final_denial)
    if level:
        level["file_by"] = level["file_by"].isoformat() if level["file_by"] else None
    return level


def _level_label(case: dict) -> str:
    return appeal_rules.route(case["plan_type"], case["service_timing"], None, None)["level_label"]


def _timeline(case: dict) -> list[dict]:
    sent = case["status"] in SENT_STATUSES
    decided = case["status"] == "decided"
    steps = [{"label": "Denial notice", "date": case["notice_date"], "done": True}]
    if sent:
        steps.append({"label": "Sent", "date": _iso(case["sent_at"]), "done": True})
    else:
        steps.append({"label": "File by", "date": case["file_by"], "done": False})
    if sent and case["decision_due"]:
        steps.append({"label": "Decision usually due", "date": case["decision_due"], "done": decided})
    if decided:
        steps.append({"label": "Decision", "date": case["decided_at"], "done": True})
    return steps


def _next_step(case: dict, level_label: str) -> dict:
    if case["needs_confirmation"] and case["status"] == "draft":
        return {"kind": "confirm", "label": "Check the details we read from your letter"}
    if case["status"] not in SENT_STATUSES:
        if case["service_timing"] == "urgent":
            return {"kind": "urgent", "label": "Ask for an expedited appeal and call your doctor today"}
        if case["file_by"]:
            label = f"File your {_lower_label(level_label)} by {_pretty_date(case['file_by'])}"
        else:
            label = "Check your letter for the deadline"
        return {"kind": "file_appeal", "label": label}
    if case["status"] == "sent":
        due = _pretty_date(case["decision_due"])
        return {"kind": "wait_for_decision", "label": f"Your insurer's decision is usually due by {due}" if due else "Wait for your insurer's decision"}
    if case["outcome"] == "upheld":
        return {"kind": "next_level", "label": "Your insurer kept its decision. See what you can do next"}
    return {"kind": "done", "label": "This appeal is closed"}


def build_case_view(case_id: int) -> dict:
    case = cc_cases.get_case(case_id)
    extracted = case["extracted"]
    locked = not cc_purchases.is_unlocked(case_id)
    reason_key = case["denial_reason"] or "other"
    route = appeal_rules.route(
        case["plan_type"], case["service_timing"],
        date.fromisoformat(case["notice_date"]) if case["notice_date"] else None, None,
    )
    checklist = appeal_kit.evidence_checklist(reason_key, case["for_whom"])
    return {
        "case_id": case_id,
        "locked": locked,
        "status": case["status"],
        "for_whom": case["for_whom"],
        "service_timing": case["service_timing"],
        "outcome": case["outcome"],
        "summary": {
            "insurer": extracted.get("insurer_name"),
            "service": extracted.get("service_description"),
            "service_date": extracted.get("service_date"),
            "claim_number": extracted.get("claim_number"),
            "notice_date": case["notice_date"],
            "amount_denied": case["amount_denied"],
            "reason_key": reason_key,
            "reason_label": DENIAL_REASONS.get(reason_key, DENIAL_REASONS["other"]),
            "plain_reason": case["plain_reason"],
            "denial_reason_text": extracted.get("denial_reason_text"),
            "printed_window_text": extracted.get("printed_appeal_window_text"),
            "patient_name": extracted.get("patient_name"),
        },
        "route": {
            "plan_type": case["plan_type"],
            "plan_label": PLAN_TYPES.get(case["plan_type"]),
            "level": case["level"],
            "level_label": route["level_label"],
            "file_by": case["file_by"],
            "deadline_source": case["deadline_source"],
            "decision_window_days": route["decision_window_days"],
            "decision_due": case["decision_due"],
            "send_to": {
                "address": extracted.get("appeal_address"),
                "fax": extracted.get("appeal_fax"),
                "phone": extracted.get("appeal_phone"),
            },
        },
        "needs_confirmation": case["needs_confirmation"],
        "evidence_checklist": checklist[:config.CC_FREE_CHECKLIST_ITEMS] if locked else checklist,
        "letter": {"letter_text": case["letter_text"]} if case["letter_text"] and not locked else None,
        "timeline": _timeline(case),
        "next_step": _next_step(case, route["level_label"]),
        "next_level": next_level(case),
        "crosspromo": "billkarma" if appeal_kit.wants_billkarma(case) else None,
        "rule_source_url": route["source_url"],
        "price": {"product_id": config.CC_APPEAL_KIT_PRODUCT_ID},
    }


def case_summary(case: dict) -> dict:
    extracted = case["extracted"]
    reason_key = case["denial_reason"] or "other"
    return {
        "case_id": case["id"],
        "insurer": extracted.get("insurer_name"),
        "service": extracted.get("service_description"),
        "reason_label": DENIAL_REASONS.get(reason_key, DENIAL_REASONS["other"]),
        "file_by": case["file_by"],
        "deadline_source": case["deadline_source"],
        "status": case["status"],
        "locked": not cc_purchases.is_unlocked(case["id"]),
        "outcome": case["outcome"],
        "next_step": _next_step(case, _level_label(case)),
        "for_whom": case["for_whom"],
        "service_timing": case["service_timing"],
        "notice_date": case["notice_date"],
        "amount_denied": case["amount_denied"],
    }
