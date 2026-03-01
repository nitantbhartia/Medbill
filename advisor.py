"""AI Bill Advisor — conversational Gemini chat with full bill context."""

from __future__ import annotations

import json
import logging
from html import escape as _he

from google import genai
from google.genai import types

import config
from analyzer import get_bill_results, compute_case_summary
from db import get_db
from state_rights import (
    STATE_SOL_YEARS,
    STATE_NAMES,
    BALANCE_BILLING_LAWS,
    CHARITY_CARE_LAWS,
    COLLECTION_PROTECTIONS,
)

log = logging.getLogger(__name__)

MAX_HISTORY_TURNS = 20
MAX_MESSAGE_LEN = 2000


def build_bill_context(bill_id: int) -> str | None:
    """Build a rich context string from a bill's data for the AI advisor."""
    results = get_bill_results(bill_id)
    if not results:
        return None

    bill = results["bill"]
    line_items = results["line_items"]
    findings = results["findings"]
    hospital = results.get("hospital_match")
    has_patient_data = results.get("has_patient_data", False)
    has_insurance = results.get("has_insurance_data", False)

    case_summary = compute_case_summary(findings)

    parts = []

    # Bill overview
    parts.append("=== BILL OVERVIEW ===")
    parts.append(f"Provider: {bill.get('provider_name', 'Unknown')}")
    parts.append(f"Bill date: {bill.get('bill_date', 'Unknown')}")
    parts.append(f"ZIP code: {bill.get('zip_code', 'Unknown')}")
    total_charged = bill.get("total_charged")
    if total_charged:
        parts.append(f"Total charged: ${total_charged:,.2f}")
    patient_owes = bill.get("total_patient_owes")
    if patient_owes:
        parts.append(f"Patient responsibility: ${patient_owes:,.2f}")
    if has_insurance:
        parts.append("Insurance: Yes (EOB data available)")
    if has_patient_data:
        parts.append("Patient cost-sharing data: Available")

    # Hospital context
    if hospital:
        parts.append("\n=== HOSPITAL PROFILE ===")
        parts.append(f"Name: {hospital.get('name', 'Unknown')}")
        parts.append(f"Location: {hospital.get('city', '')}, {hospital.get('state', '')}")
        grade = hospital.get("billing_grade")
        if grade:
            parts.append(f"Billing grade: {grade}")
        markup = hospital.get("avg_markup_vs_medicare")
        if markup:
            parts.append(f"Average markup vs Medicare: {markup:.1f}x")
        if hospital.get("is_nonprofit"):
            parts.append("Type: Nonprofit (required to offer financial assistance under IRS 501(r))")
        if hospital.get("has_financial_assistance"):
            parts.append("Financial assistance: Available")

    # Line items
    if line_items:
        parts.append(f"\n=== LINE ITEMS ({len(line_items)} charges) ===")
        for i, li in enumerate(line_items[:30], 1):
            cpt = li.get("cpt_code") or "N/A"
            desc = li.get("description") or "No description"
            charged = li.get("charged_amount")
            charge_str = f"${charged:,.2f}" if charged else "N/A"
            medicare = li.get("medicare_rate")
            medicare_str = f" | Medicare: ${medicare:,.2f}" if medicare else ""
            ins_paid = li.get("insurance_paid")
            ins_str = f" | Insurance paid: ${ins_paid:,.2f}" if ins_paid else ""
            patient = li.get("patient_responsibility")
            patient_str = f" | You owe: ${patient:,.2f}" if patient else ""
            parts.append(f"  {i}. CPT {cpt}: {desc} — Charged: {charge_str}{medicare_str}{ins_str}{patient_str}")

    # Findings
    if findings:
        total_savings = sum(float(f.get("potential_savings") or 0) for f in findings)
        parts.append(f"\n=== ANALYSIS FINDINGS ({len(findings)} issues, ${total_savings:,.2f} potential savings) ===")
        for i, f in enumerate(findings[:20], 1):
            sev = f.get("severity", "low")
            conf = f.get("confidence", "medium")
            savings = float(f.get("potential_savings") or 0)
            msg = f.get("message", "")
            ftype = f.get("finding_type", "")
            parts.append(f"  {i}. [{sev.upper()}] {msg}")
            if savings > 0:
                parts.append(f"     Potential savings: ${savings:,.2f} | Confidence: {conf} | Type: {ftype}")
            details = f.get("parsed_details") or {}
            if details.get("medicare_rate"):
                parts.append(f"     Medicare rate: ${details['medicare_rate']:,.2f}")
            if details.get("markup_multiple"):
                parts.append(f"     Markup: {details['markup_multiple']:.1f}x Medicare")

        parts.append(f"\nCase win probability: {case_summary.get('win_probability', 0)}%")
        parts.append(f"Confidence score: {case_summary.get('confidence_score', 0)}%")

    # State rights
    zip_code = bill.get("zip_code", "")
    state_code = _zip_to_state(zip_code)
    if state_code:
        state_name = STATE_NAMES.get(state_code, state_code)
        parts.append(f"\n=== STATE RIGHTS ({state_name}) ===")
        sol = STATE_SOL_YEARS.get(state_code)
        if sol:
            parts.append(f"Statute of limitations on medical debt: {sol} years")
        bb = BALANCE_BILLING_LAWS.get(state_code)
        if bb:
            parts.append(f"Balance billing protections: {bb}")
        cc = CHARITY_CARE_LAWS.get(state_code)
        if cc:
            parts.append(f"Charity care law: {cc}")
        cp = COLLECTION_PROTECTIONS.get(state_code)
        if cp:
            parts.append(f"Collection protections: {cp}")

    return "\n".join(parts)


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


SYSTEM_PROMPT = """You are BillKarma AI Advisor, a knowledgeable and empathetic medical billing expert. You help patients understand their medical bills and fight unfair charges.

CONTEXT: You have access to the patient's full bill analysis below. Use this data to give specific, personalized answers.

{bill_context}

=== YOUR ROLE ===
- Explain charges in plain English. No jargon unless the patient asks.
- Reference specific line items, CPT codes, and dollar amounts from their bill.
- When discussing savings, cite the specific findings and amounts.
- Recommend concrete next steps with links to BillKarma tools when relevant.
- If the patient asks you to generate a letter or script, do it inline using the bill data.
- Be honest about what you know and don't know. You're not a lawyer or doctor.
- Be warm, supportive, and action-oriented. These patients are stressed about money.

=== TOOLS YOU CAN RECOMMEND ===
- /scan — Upload and scan a bill for errors
- /estimate — Get a savings estimate
- /fight-debt — Fight medical debt (FDCPA letters, validation, settlement)
- /charity-care — Check charity care eligibility
- /statute-of-limitations — Check if debt is past statute of limitations
- /tools/surprise-bill-checker/ — Check No Surprises Act protections
- /tools/insurance-denial-appeal-letter-generator/ — Generate insurance appeal
- /compare/ — Compare hospital prices
- /rights/ — State-specific medical billing rights
- /glossary/ — Medical billing glossary

=== GUIDELINES ===
- Never claim to be a lawyer, doctor, or licensed professional.
- Never guarantee outcomes. Use phrases like "you may be able to" and "patients in similar situations have seen."
- Always mention that this is informational, not legal or medical advice, if the topic is sensitive.
- If asked about something outside medical billing (health advice, legal strategy, etc.), redirect to the appropriate professional.
- Keep responses concise (2-4 paragraphs max) unless the patient asks for detail.
- Use dollar amounts and percentages to make savings tangible.
- When generating letters/scripts, include [PLACEHOLDERS] for information you don't have."""


def get_advisor_response(
    bill_id: int,
    message: str,
    history: list[dict],
) -> str:
    """Get a non-streaming response from the AI advisor."""
    if not config.GEMINI_API_KEY:
        return "AI Advisor requires a Gemini API key to be configured. Please contact the site administrator."

    bill_context = build_bill_context(bill_id)
    if not bill_context:
        return "I couldn't find your bill data. Please make sure you've uploaded and scanned a bill first."

    system = SYSTEM_PROMPT.format(bill_context=bill_context)

    # Build conversation for Gemini
    contents = []
    for turn in history[-MAX_HISTORY_TURNS:]:
        role = turn.get("role", "user")
        text = turn.get("content", "")
        contents.append(types.Content(
            role=role,
            parts=[types.Part.from_text(text=text)],
        ))

    # Add current message
    contents.append(types.Content(
        role="user",
        parts=[types.Part.from_text(text=message)],
    ))

    client = genai.Client(api_key=config.GEMINI_API_KEY)
    response = client.models.generate_content(
        model=config.GEMINI_MODEL,
        contents=contents,
        config=types.GenerateContentConfig(
            system_instruction=system,
            temperature=0.7,
            max_output_tokens=2048,
        ),
    )

    return response.text or "I wasn't able to generate a response. Please try rephrasing your question."


def stream_advisor_response(
    bill_id: int,
    message: str,
    history: list[dict],
):
    """Yield streaming chunks from the AI advisor."""
    if not config.GEMINI_API_KEY:
        yield "AI Advisor requires a Gemini API key to be configured."
        return

    bill_context = build_bill_context(bill_id)
    if not bill_context:
        yield "I couldn't find your bill data. Please make sure you've uploaded and scanned a bill first."
        return

    system = SYSTEM_PROMPT.format(bill_context=bill_context)

    contents = []
    for turn in history[-MAX_HISTORY_TURNS:]:
        role = turn.get("role", "user")
        text = turn.get("content", "")
        contents.append(types.Content(
            role=role,
            parts=[types.Part.from_text(text=text)],
        ))

    contents.append(types.Content(
        role="user",
        parts=[types.Part.from_text(text=message)],
    ))

    client = genai.Client(api_key=config.GEMINI_API_KEY)

    try:
        for chunk in client.models.generate_content_stream(
            model=config.GEMINI_MODEL,
            contents=contents,
            config=types.GenerateContentConfig(
                system_instruction=system,
                temperature=0.7,
                max_output_tokens=2048,
            ),
        ):
            if chunk.text:
                yield chunk.text
    except Exception as e:
        log.error("Advisor streaming error: %s", e)
        yield "\n\nSorry, I encountered an error. Please try again."
