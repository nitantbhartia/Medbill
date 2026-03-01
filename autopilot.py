"""Autopilot Agent — AI-driven autonomous dispute lifecycle management.

The autopilot agent orchestrates the entire dispute process:
1. Analyzes the bill and selects optimal strategy
2. Generates and sends dispute communications
3. Classifies hospital responses and decides next moves
4. Escalates through channels (email → follow-up → complaint → financial assistance)
5. Reports progress to the patient at each step

Uses Gemini to make strategic decisions at each stage.
"""

from __future__ import annotations

import json
import logging
from datetime import date, timedelta

from google import genai
from google.genai import types

import config
import email_service
from analyzer import get_bill_results, compute_case_summary
from db import get_db
from dispute_workflow import build_dispute_letter, build_phone_script
from state_rights import (
    STATE_SOL_YEARS,
    BALANCE_BILLING_LAWS,
    CHARITY_CARE_LAWS,
    COLLECTION_PROTECTIONS,
)

log = logging.getLogger(__name__)


# --- Strategy Generation ---


def generate_strategy(bill_id: int) -> dict:
    """Use AI to analyze the bill and generate an optimal dispute strategy.

    Returns a strategy dict with phases, timeline, and recommended actions.
    """
    results = get_bill_results(bill_id)
    if not results:
        return {"error": "Bill not found"}

    bill = results["bill"]
    findings = results["findings"]
    hospital = results.get("hospital_match")
    case_summary = compute_case_summary(findings)

    if not findings:
        return _no_findings_strategy(bill, hospital)

    total_savings = sum(float(f.get("potential_savings") or 0) for f in findings)
    high_findings = [f for f in findings if f.get("severity") == "high"]
    is_nonprofit = bool(hospital and hospital.get("is_nonprofit"))

    # Determine state protections
    zip_code = bill.get("zip_code", "")
    state_code = _zip_to_state(zip_code)
    sol_years = STATE_SOL_YEARS.get(state_code, 6) if state_code else 6
    has_balance_billing = bool(state_code and BALANCE_BILLING_LAWS.get(state_code))
    has_charity_care = bool(state_code and CHARITY_CARE_LAWS.get(state_code))
    has_collection_protections = bool(state_code and COLLECTION_PROTECTIONS.get(state_code))

    # Build strategy phases
    phases = []

    # Phase 1: Always start with formal dispute letter
    phase1_actions = [
        {
            "action": "send_dispute_letter",
            "description": "Send formal dispute letter citing specific billing errors and Medicare rate comparisons",
            "auto": True,
            "priority": "critical",
        },
    ]

    if is_nonprofit:
        phase1_actions.append({
            "action": "file_financial_assistance",
            "description": "File IRS 501(r) financial assistance application (this hospital is nonprofit)",
            "auto": True,
            "priority": "high",
        })

    phases.append({
        "name": "Initial Dispute",
        "day": 0,
        "duration_days": 7,
        "actions": phase1_actions,
        "expected_outcome": "Hospital acknowledges receipt and begins review",
    })

    # Phase 2: First follow-up if no response
    phases.append({
        "name": "First Follow-Up",
        "day": 7,
        "duration_days": 7,
        "actions": [
            {
                "action": "send_followup",
                "description": "Send follow-up email requesting written acknowledgment",
                "auto": True,
                "priority": "high",
            },
        ],
        "expected_outcome": "Hospital responds with acknowledgment or initial offer",
    })

    # Phase 3: Escalation
    phase3_actions = [
        {
            "action": "escalation_letter",
            "description": "Send escalation letter referencing patient rights and regulatory obligations",
            "auto": True,
            "priority": "high",
        },
    ]
    if has_balance_billing:
        phase3_actions.append({
            "action": "cite_state_protections",
            "description": "Reference state-specific balance billing protections in escalation",
            "auto": True,
            "priority": "medium",
        })

    phases.append({
        "name": "Escalation",
        "day": 14,
        "duration_days": 16,
        "actions": phase3_actions,
        "expected_outcome": "Hospital makes adjustment offer or provides detailed response",
    })

    # Phase 4: Negotiate or file complaints
    phase4_actions = [
        {
            "action": "final_demand",
            "description": "Send final demand letter with 7-day deadline before filing complaints",
            "auto": True,
            "priority": "critical",
        },
    ]
    if total_savings > 500:
        phase4_actions.append({
            "action": "prepare_complaint",
            "description": "Draft complaints for state Attorney General and CMS if hospital remains unresponsive",
            "auto": False,
            "priority": "medium",
        })

    phases.append({
        "name": "Final Resolution",
        "day": 30,
        "duration_days": 15,
        "actions": phase4_actions,
        "expected_outcome": "Resolution, settlement offer, or escalation to regulatory bodies",
    })

    # Phase 5: Refund guarantee
    phases.append({
        "name": "Guarantee Review",
        "day": 45,
        "duration_days": 0,
        "actions": [
            {
                "action": "evaluate_outcome",
                "description": "Evaluate dispute outcome. Full refund if unresolved.",
                "auto": True,
                "priority": "critical",
            },
        ],
        "expected_outcome": "Confirmed savings or full refund to patient",
    })

    # AI-enhanced strategy summary
    strategy_summary = _ai_strategy_summary(bill, findings, hospital, state_code) if config.GEMINI_API_KEY else ""

    return {
        "bill_id": bill_id,
        "provider": bill.get("provider_name", "Unknown"),
        "total_charged": float(bill.get("total_charged") or 0),
        "total_savings": round(total_savings, 2),
        "finding_count": len(findings),
        "high_severity_count": len(high_findings),
        "win_probability": case_summary.get("win_probability", 0),
        "is_nonprofit": is_nonprofit,
        "state_code": state_code,
        "sol_years": sol_years,
        "phases": phases,
        "timeline_days": 45,
        "strategy_summary": strategy_summary,
        "recommended_channels": _recommend_channels(hospital, findings),
    }


def _no_findings_strategy(bill: dict, hospital: dict | None) -> dict:
    """Return strategy for bills with no identified issues."""
    actions = []
    if hospital and hospital.get("is_nonprofit"):
        actions.append({
            "action": "check_financial_assistance",
            "description": "Check financial assistance eligibility — this hospital is nonprofit",
            "priority": "high",
        })
    actions.append({
        "action": "request_itemized_bill",
        "description": "Request a fully itemized bill to check for hidden charges",
        "priority": "medium",
    })
    return {
        "bill_id": bill.get("id"),
        "provider": bill.get("provider_name", "Unknown"),
        "total_charged": float(bill.get("total_charged") or 0),
        "total_savings": 0,
        "finding_count": 0,
        "high_severity_count": 0,
        "win_probability": 0,
        "is_nonprofit": bool(hospital and hospital.get("is_nonprofit")),
        "phases": [],
        "timeline_days": 0,
        "strategy_summary": "No significant billing errors found. Consider requesting an itemized bill for a closer look.",
        "recommended_actions": actions,
    }


def _recommend_channels(hospital: dict | None, findings: list) -> list[str]:
    """Recommend dispute communication channels based on hospital and findings."""
    channels = ["email"]
    total_savings = sum(float(f.get("potential_savings") or 0) for f in findings)
    if total_savings > 2000:
        channels.append("certified_mail")
    if total_savings > 5000:
        channels.append("fax")
    return channels


def _ai_strategy_summary(
    bill: dict,
    findings: list,
    hospital: dict | None,
    state_code: str | None,
) -> str:
    """Use Gemini to generate a plain-English strategy summary."""
    total_savings = sum(float(f.get("potential_savings") or 0) for f in findings)
    high_count = sum(1 for f in findings if f.get("severity") == "high")
    finding_types = set(f.get("finding_type", "") for f in findings)

    prompt = f"""You are a medical billing advocate. Write a 2-3 sentence strategy summary for this case:

- Provider: {bill.get('provider_name', 'Unknown')}
- Total charged: ${float(bill.get('total_charged') or 0):,.2f}
- Issues found: {len(findings)} ({high_count} high severity)
- Potential savings: ${total_savings:,.2f}
- Issue types: {', '.join(finding_types)}
- Hospital type: {'Nonprofit' if hospital and hospital.get('is_nonprofit') else 'For-profit/Unknown'}
- Hospital billing grade: {hospital.get('billing_grade', 'N/A') if hospital else 'N/A'}
- State: {state_code or 'Unknown'}

Write a confident, action-oriented summary. Focus on the strongest argument and most likely path to savings. Be specific about the dollar amounts and key leverage points."""

    try:
        client = genai.Client(api_key=config.GEMINI_API_KEY)
        response = client.models.generate_content(
            model=config.GEMINI_MODEL,
            contents=prompt,
            config=types.GenerateContentConfig(
                temperature=0.5,
                max_output_tokens=300,
            ),
        )
        return (response.text or "").strip()
    except Exception as e:
        log.error("AI strategy summary failed: %s", e)
        return f"Your bill from {bill.get('provider_name', 'this provider')} has {len(findings)} identified issues totaling ${total_savings:,.2f} in potential savings. We'll dispute each one systematically."


# --- Autopilot Dashboard Data ---


def get_autopilot_status(case_id: int) -> dict | None:
    """Get full autopilot status for the real-time dashboard."""
    with get_db() as db:
        case = db.execute("SELECT * FROM dispute_cases WHERE id = ?", (case_id,)).fetchone()
        if not case:
            return None
        case = dict(case)

        bill = db.execute("SELECT * FROM bills WHERE id = ?", (case["bill_id"],)).fetchone()
        bill = dict(bill) if bill else {}

        followups = db.execute(
            "SELECT * FROM followup_queue WHERE case_id = ? ORDER BY followup_number",
            (case_id,),
        ).fetchall()
        followups = [dict(f) for f in followups]

        findings = db.execute(
            "SELECT * FROM findings WHERE bill_id = ? ORDER BY "
            "CASE severity WHEN 'high' THEN 0 WHEN 'medium' THEN 1 ELSE 2 END",
            (case["bill_id"],),
        ).fetchall()
        findings = [dict(f) for f in findings]

    total_savings = sum(float(f.get("potential_savings") or 0) for f in findings)

    # Determine current phase
    created = case.get("created_at", "")
    try:
        created_date = date.fromisoformat(created[:10]) if created else date.today()
    except (ValueError, TypeError):
        created_date = date.today()
    days_elapsed = (date.today() - created_date).days

    if case["status"] in ("resolved", "refunded"):
        current_phase = "Complete"
        phase_number = 5
    elif days_elapsed >= 30:
        current_phase = "Final Resolution"
        phase_number = 4
    elif days_elapsed >= 14:
        current_phase = "Escalation"
        phase_number = 3
    elif days_elapsed >= 7:
        current_phase = "First Follow-Up"
        phase_number = 2
    else:
        current_phase = "Initial Dispute"
        phase_number = 1

    # Parse strategy notes
    strategy_notes = []
    try:
        strategy_notes = json.loads(case.get("strategy_notes") or "[]")
    except (ValueError, TypeError):
        pass

    # Build timeline events
    timeline = _build_timeline(case, followups, strategy_notes)

    return {
        "case_id": case_id,
        "bill_id": case["bill_id"],
        "status": case["status"],
        "provider_name": bill.get("provider_name", "Unknown"),
        "total_charged": float(bill.get("total_charged") or 0),
        "total_savings": round(total_savings, 2),
        "finding_count": len(findings),
        "patient_name": case.get("patient_name", ""),
        "patient_email": case.get("patient_email", ""),
        "created_at": case.get("created_at", ""),
        "days_elapsed": days_elapsed,
        "current_phase": current_phase,
        "phase_number": phase_number,
        "phases_total": 5,
        "progress_pct": min(100, round(phase_number / 5 * 100)),
        "followups_sent": case.get("followups_sent", 0),
        "followups_total": len(config.DISPUTE_FOLLOWUP_DAYS),
        "outcome": case.get("outcome"),
        "actual_savings": case.get("actual_savings"),
        "is_nonprofit": bool(case.get("is_nonprofit")),
        "financial_assistance_filed": bool(case.get("financial_assistance_filed")),
        "timeline": timeline,
        "strategy_notes": strategy_notes,
        "next_action": _determine_next_action(case, followups, days_elapsed),
    }


def _build_timeline(case: dict, followups: list[dict], notes: list[dict]) -> list[dict]:
    """Build a chronological timeline of all dispute events."""
    events = []

    # Case created
    events.append({
        "date": case.get("created_at", "")[:10],
        "event": "Dispute activated",
        "type": "milestone",
        "detail": "Payment confirmed. Autopilot engaged.",
    })

    # Initial letter sent
    if case.get("initial_sent_at"):
        events.append({
            "date": case["initial_sent_at"][:10],
            "event": "Dispute letter sent",
            "type": "action",
            "detail": f"Formal dispute letter sent to {case.get('hospital_billing_email', 'hospital')}",
        })

    # Financial assistance
    if case.get("financial_assistance_filed"):
        events.append({
            "date": case.get("created_at", "")[:10],
            "event": "Financial assistance filed",
            "type": "action",
            "detail": "501(r) financial assistance application initiated (nonprofit hospital)",
        })

    # Follow-ups
    for fu in followups:
        if fu.get("sent_at"):
            events.append({
                "date": fu["sent_at"][:10] if fu["sent_at"] else "",
                "event": f"Follow-up #{fu['followup_number']} sent",
                "type": "action",
                "detail": "Automated follow-up sent. Awaiting response.",
            })

    # Resolution
    if case.get("resolved_at"):
        events.append({
            "date": case["resolved_at"][:10],
            "event": "Dispute resolved",
            "type": "milestone",
            "detail": f"Outcome: {case.get('outcome', 'resolved')}. Savings: ${float(case.get('actual_savings') or 0):,.2f}",
        })

    # Refund
    if case.get("refunded_at"):
        events.append({
            "date": case["refunded_at"][:10],
            "event": "Refund issued",
            "type": "milestone",
            "detail": "Full refund issued — no savings confirmed within 45 days.",
        })

    # Strategy notes
    for note in notes:
        events.append({
            "date": note.get("date", ""),
            "event": "Strategy update",
            "type": "note",
            "detail": note.get("text", ""),
        })

    # Sort by date
    events.sort(key=lambda e: e.get("date", ""))
    return events


def _determine_next_action(case: dict, followups: list[dict], days_elapsed: int) -> dict:
    """Determine the next automated action the agent will take."""
    status = case.get("status", "")

    if status in ("resolved", "refunded"):
        return {"action": "none", "description": "Case complete. No further actions."}

    if status == "refund_pending":
        return {"action": "issue_refund", "description": "Processing your guaranteed refund."}

    # Check which follow-ups haven't been sent yet
    unsent = [f for f in followups if not f.get("sent_at")]
    if unsent:
        next_fu = unsent[0]
        scheduled = next_fu.get("scheduled_for", "")
        return {
            "action": "send_followup",
            "description": f"Follow-up #{next_fu['followup_number']} scheduled for {scheduled}",
            "scheduled_for": scheduled,
        }

    if days_elapsed >= 45:
        return {"action": "evaluate_outcome", "description": "Evaluating final outcome and processing guarantee."}

    return {"action": "monitoring", "description": "Monitoring for hospital response."}


def _zip_to_state(zip_code: str) -> str | None:
    """Look up state code from ZIP code."""
    if not zip_code or len(zip_code) < 5:
        return None
    with get_db() as db:
        row = db.execute(
            "SELECT state FROM zip_latlon WHERE zip = ? LIMIT 1",
            (zip_code[:5],),
        ).fetchone()
    return row["state"] if row else None
