import json
import re
import logging
from datetime import datetime

from google import genai
from google.genai import types

import config
from db import get_db

log = logging.getLogger(__name__)

NEGOTIATION_STAGES = {
    "stage_1": {
        "name": "Initial Dispute",
        "tone": "Professional and firm. Informed consumer, not complainer.",
    },
    "stage_2": {
        "name": "Follow-up / Counter",
        "tone": "Persistent but respectful.",
    },
    "stage_3": {
        "name": "Escalation",
        "tone": "Firm. Make clear you know your rights.",
    },
    "stage_4": {
        "name": "Final Resolution",
        "tone": "Resolution-oriented. Get the best outcome.",
    },
}

PROHIBITED_PATTERNS = [
    r"(?i)(lawsuit|sue you|legal action|attorney will|court|litigation)",
    r"(?i)(we will take legal|face legal consequences)",
    r"(?i)(medically (un)?necessary|should not have been prescribed)",
    r"(?i)(diagnosis.*(wrong|incorrect|inaccurate))",
    r"(?i)(guarantee|promise|ensure|definitely will)",
    r"(?i)(I am (a|an|the) (lawyer|attorney|doctor|physician))",
    r"(?i)(legal (counsel|representative|advisor))",
    r"(?i)(fraud|scam|criminal|steal|theft|illegal)",
    r"(?i)(demand|require you to|must immediately)",
]


def validate_outbound_email(body: str) -> dict:
    """Scan email for prohibited content. Hard fail on any match."""
    violations = []
    for pattern in PROHIBITED_PATTERNS:
        matches = re.findall(pattern, body)
        if matches:
            violations.append({"pattern": pattern, "matches": [str(m) for m in matches]})
    return {"approved": len(violations) == 0, "violations": violations}


def create_negotiation(bill_id: int, user_id: int, account_number: str, hospital_email: str = "") -> int:
    """Create a new negotiation record."""
    with get_db() as db:
        bill = db.execute("SELECT * FROM bills WHERE id = ?", (bill_id,)).fetchone()
        if not bill:
            raise ValueError(f"Bill {bill_id} not found")

        cursor = db.execute(
            "INSERT INTO negotiations (bill_id, user_id, hospital_name, hospital_email, "
            "account_number, original_amount, current_amount, fee_percentage, fee_cap) "
            "VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)",
            (
                bill_id,
                user_id,
                bill["provider_name"],
                hospital_email,
                account_number,
                bill["total_patient_owes"],
                bill["total_patient_owes"],
                config.NEGOTIATION_FEE_PERCENTAGE,
                config.NEGOTIATION_FEE_CAP,
            ),
        )
    return cursor.lastrowid


def generate_dispute_email(negotiation_id: int) -> dict:
    """Generate a dispute email for the current negotiation stage."""
    with get_db() as db:
        neg = db.execute("SELECT * FROM negotiations WHERE id = ?", (negotiation_id,)).fetchone()
        if not neg:
            raise ValueError(f"Negotiation {negotiation_id} not found")

        findings = db.execute(
            "SELECT * FROM findings WHERE bill_id = ?", (neg["bill_id"],)
        ).fetchall()

        previous_messages = db.execute(
            "SELECT * FROM negotiation_messages WHERE negotiation_id = ? ORDER BY id",
            (negotiation_id,),
        ).fetchall()

    neg = dict(neg)
    findings = [dict(f) for f in findings]
    stage = neg["current_stage"]
    stage_config = NEGOTIATION_STAGES.get(stage, NEGOTIATION_STAGES["stage_1"])

    hospital_responses = [
        dict(m) for m in previous_messages if m["direction"] == "inbound"
    ]
    last_response = hospital_responses[-1]["body"] if hospital_responses else None

    prompt = f"""You are a medical billing advocate writing on behalf of a patient.

ROLE: Authorized representative communicating with hospital billing
about factual billing errors. NOT a lawyer. NOT giving legal advice.

STAGE: {stage_config['name']}
TONE: {stage_config['tone']}

PATIENT ACCOUNT: {neg['account_number']}
HOSPITAL: {neg['hospital_name']}
ORIGINAL BILL: ${neg['original_amount']:,.2f}

FINDINGS:
{json.dumps(findings, indent=2, default=str)}

{"HOSPITAL PREVIOUS RESPONSE: " + last_response if last_response else "This is the initial dispute letter."}

RULES:
- NEVER threaten lawsuits or legal action
- NEVER give medical opinions or dispute medical necessity
- NEVER use words: illegal, fraud, scam, criminal, demand, require
- DO cite specific CPT codes and Medicare rates
- DO reference applicable regulations (informational, not threatening)
- DO request specific dollar adjustments
- DO ask about financial assistance programs
- Keep under 400 words, professional and specific

Return JSON with these fields:
- subject: email subject line
- body: email body text
- patient_summary: 2 sentences plain English summary for the patient"""

    client = genai.Client(api_key=config.GEMINI_API_KEY)
    response = client.models.generate_content(
        model=config.GEMINI_MODEL,
        contents=[prompt],
        config=types.GenerateContentConfig(
            response_mime_type="application/json",
        ),
    )

    email_data = json.loads(response.text)

    # Validate before returning
    validation = validate_outbound_email(email_data.get("body", ""))
    if not validation["approved"]:
        log.warning("Generated email failed validation: %s", validation["violations"])
        raise ValueError(f"Generated email contains prohibited content: {validation['violations']}")

    # Save as draft
    with get_db() as db:
        db.execute(
            "INSERT INTO negotiation_messages (negotiation_id, direction, stage, "
            "subject, body, patient_summary) VALUES (?, 'outbound', ?, ?, ?, ?)",
            (
                negotiation_id,
                stage,
                email_data["subject"],
                email_data["body"],
                email_data.get("patient_summary", ""),
            ),
        )

    return email_data


def approve_and_send(message_id: int) -> bool:
    """Mark a message as approved. Actual email sending is handled by the email service."""
    with get_db() as db:
        db.execute(
            "UPDATE negotiation_messages SET user_approved = 1, approved_at = ? WHERE id = ?",
            (datetime.utcnow().isoformat(), message_id),
        )
        msg = db.execute(
            "SELECT negotiation_id FROM negotiation_messages WHERE id = ?", (message_id,)
        ).fetchone()
        if msg:
            db.execute(
                "UPDATE negotiations SET status = 'awaiting_response', "
                "rounds_completed = rounds_completed + 1 WHERE id = ?",
                (msg["negotiation_id"],),
            )
    return True


def record_hospital_response(negotiation_id: int, email_body: str) -> dict:
    """Record an inbound hospital response and parse it with AI."""
    client = genai.Client(api_key=config.GEMINI_API_KEY)

    with get_db() as db:
        neg = db.execute("SELECT * FROM negotiations WHERE id = ?", (negotiation_id,)).fetchone()

    neg = dict(neg)

    prompt = f"""Analyze this hospital billing department response.

Our dispute: ${neg['original_amount']:,.2f}

Hospital response:
{email_body}

Return JSON:
- outcome: full_adjustment | partial_adjustment | rejection | info_request | payment_plan_offer | financial_aid_offer
- adjusted_amount: dollars reduced (0 if rejection)
- next_action: recommended next step
- patient_summary: 2-3 sentence plain English for user
- should_accept: true or false"""

    response = client.models.generate_content(
        model=config.GEMINI_MODEL,
        contents=[prompt],
        config=types.GenerateContentConfig(
            response_mime_type="application/json",
        ),
    )

    analysis = json.loads(response.text)

    with get_db() as db:
        db.execute(
            "INSERT INTO negotiation_messages (negotiation_id, direction, body, "
            "ai_analysis, patient_summary) VALUES (?, 'inbound', ?, ?, ?)",
            (
                negotiation_id,
                email_body,
                json.dumps(analysis),
                analysis.get("patient_summary", ""),
            ),
        )

        # Update negotiation with savings
        adjusted = analysis.get("adjusted_amount", 0)
        if adjusted > 0:
            db.execute(
                "UPDATE negotiations SET total_savings = total_savings + ?, "
                "current_amount = current_amount - ? WHERE id = ?",
                (adjusted, adjusted, negotiation_id),
            )

        # Advance stage
        stages = list(NEGOTIATION_STAGES.keys())
        current_idx = stages.index(neg["current_stage"]) if neg["current_stage"] in stages else 0
        if current_idx < len(stages) - 1:
            db.execute(
                "UPDATE negotiations SET current_stage = ? WHERE id = ?",
                (stages[current_idx + 1], negotiation_id),
            )

    return analysis


def generate_phone_script(bill_id: int) -> str:
    """Generate a phone script from bill findings."""
    with get_db() as db:
        bill = db.execute("SELECT * FROM bills WHERE id = ?", (bill_id,)).fetchone()
        findings = db.execute(
            "SELECT * FROM findings WHERE bill_id = ? ORDER BY "
            "CASE severity WHEN 'high' THEN 0 WHEN 'medium' THEN 1 ELSE 2 END",
            (bill_id,),
        ).fetchall()

    if not bill or not findings:
        return ""

    bill = dict(bill)
    findings = [dict(f) for f in findings]

    lines = [
        f'"Hi, I\'m calling about my account.',
        f"I've reviewed my itemized bill and I have a few questions.",
        "",
    ]

    for i, finding in enumerate(findings[:3], 1):
        details = json.loads(finding["details"]) if finding.get("details") else {}

        if finding["finding_type"] == "duplicate_charge":
            li = details.get("line_item", {})
            lines.append(
                f"First, I see {li.get('description', 'a charge')} "
                f"(CPT {li.get('cpt_code', 'N/A')}) appears to be billed twice "
                f"on {li.get('date_of_service', 'the same date')}. "
                f"Can you confirm whether this service was actually performed twice?"
            )
        elif finding["finding_type"] == "price_markup":
            li = details.get("line_item", {})
            lines.append(
                f"I was charged ${details.get('charged', 0):,.2f} for "
                f"{li.get('description', 'a service')} (CPT {li.get('cpt_code', 'N/A')}). "
                f"The Medicare reimbursement rate for this in my area is "
                f"${details.get('medicare_rate', 0):,.2f}. "
                f"That's a {details.get('markup_multiple', 0)}x markup. "
                f"Can you explain this charge?"
            )
        elif finding["finding_type"] == "upcoding":
            li = details.get("line_item", {})
            lines.append(
                f"I was billed for a Level {details.get('billed_level', '')} visit, "
                f"but my visit may have been a Level {details.get('likely_level', '')}. "
                f"Can you review the documentation for this visit level?"
            )
        else:
            lines.append(finding["message"])

        lines.append("")

    lines.append(
        "I'd like to request a corrected bill that addresses these items. "
        "If we can't resolve this, I'll be filing a complaint with my state's "
        'Attorney General\'s office and the hospital\'s patient advocate."'
    )

    return "\n".join(lines)
