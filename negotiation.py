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
    """Generate a phone script with prep tips, finding-specific talking points,
    benchmark/OPPS context, and objection-handling guidance."""
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
    total_savings = sum(
        json.loads(f["details"]).get("potential_savings", 0)
        for f in findings if f.get("details")
    )

    provider = bill.get("provider_name", "the provider")

    lines = [
        "BEFORE YOU CALL",
        "---------------",
        "Have ready: your itemized bill, insurance EOB, and a pen to take notes.",
        "Ask for: the billing department, then a supervisor if the first person can't help.",
        "Record: the name of everyone you speak with and any reference numbers.",
        "",
        "WHAT TO SAY",
        "-----------",
        f"\"Hi, I'm calling about my account with {provider}. "
        "I've reviewed my itemized bill and I have some specific questions.",
        "",
    ]

    for i, finding in enumerate(findings[:5], 1):
        details = json.loads(finding["details"]) if finding.get("details") else {}
        li = details.get("line_item", {})
        lines.append(f"POINT {i}:")
        lines.extend(_phone_lines_for_finding(finding, details, li))
        lines.append("")

    if total_savings > 0:
        lines.append(
            f"Altogether, I believe these adjustments total approximately "
            f"${total_savings:,.2f}. I'd like to request a corrected bill.\""
        )
    else:
        lines.append(
            "I'd like to request a corrected bill that addresses these items.\""
        )
    lines.append("")

    lines.extend([
        "IF THEY PUSH BACK",
        "------------------",
        "If they say \"that's our standard rate\":",
        "  \"I understand, but I've compared this to Medicare rates and what other "
        "hospitals charge. Can we discuss a fair-price adjustment?\"",
        "",
        "If they say they can't adjust:",
        "  \"Can I speak with a supervisor? I'd also like to know about any "
        "financial assistance or prompt-pay discount programs.\"",
        "",
        "If they refuse entirely:",
        "  \"I'll be requesting this in writing and filing a complaint with "
        "my state Attorney General's office and your patient advocate.\"",
    ])

    return "\n".join(lines)


def _phone_lines_for_finding(finding: dict, details: dict, li: dict) -> list[str]:
    """Return talking-point lines for a single finding."""
    ftype = finding["finding_type"]

    if ftype == "duplicate_charge":
        return [
            f"I see {li.get('description', 'a charge')} "
            f"(CPT {li.get('cpt_code', 'N/A')}) appears to be billed twice "
            f"on {li.get('date_of_service', 'the same date')}. "
            f"Can you confirm whether this was actually performed twice? "
            f"If not, that's ${details.get('potential_savings', 0):,.2f} that should be removed.",
        ]

    if ftype == "price_markup":
        point = (
            f"I was charged ${details.get('charged', 0):,.2f} for "
            f"{li.get('description', 'a service')} (CPT {li.get('cpt_code', 'N/A')}). "
            f"The Medicare rate for this is ${details.get('medicare_rate', 0):,.2f} "
            f"-- that's a {details.get('markup_multiple', 0)}x markup."
        )
        if details.get("total_medicare"):
            point += (
                f" Even including the hospital facility fee, Medicare's total is "
                f"${details['total_medicare']:,.2f}."
            )
        point += " Can you explain this charge or offer a fair-price adjustment?"
        return [point]

    if ftype == "unbundling":
        return [
            f"I see both {details.get('code_1', 'a comprehensive code')} and "
            f"{details.get('code_2', 'a component code')} were billed together. "
            f"Under NCCI coding rules, {details.get('code_2', 'the component code')} "
            f"is included in {details.get('code_1', 'the comprehensive code')} "
            f"and shouldn't be billed separately. "
            f"That's ${details.get('potential_savings', 0):,.2f} that should be removed.",
        ]

    if ftype == "upcoding":
        return [
            f"I was billed for a Level {details.get('billed_level', '')} ER visit, "
            f"but my symptoms and treatment may be more consistent with "
            f"Level {details.get('likely_level', '')}. "
            f"The difference is ${details.get('potential_savings', 0):,.2f}. "
            f"Can you review the documentation to confirm the visit level?",
        ]

    if ftype == "quantity_flag":
        return [
            f"I'm seeing {li.get('quantity', '')} units of "
            f"'{li.get('description', 'a service')}' on my bill. "
            f"Can you confirm that quantity is correct? "
            f"If only 1 was administered, the extra charges should be removed.",
        ]

    if ftype == "benchmark_outlier":
        return [
            f"My charge of ${details.get('charged', 0):,.2f} for "
            f"{li.get('description', 'this service')} is above what most hospitals charge. "
            f"The median charge nationally is ${details.get('median_charged', 0):,.2f} "
            f"based on {details.get('sample_size', 'thousands of')} bills. "
            f"Can we discuss a more reasonable price?",
        ]

    if ftype == "no_surprises_act":
        return [
            "I believe this bill may be subject to the No Surprises Act. "
            "If I received emergency care or care from an out-of-network provider "
            "at an in-network facility, I should not be balance-billed above "
            "the in-network rate. Can you review this?",
        ]

    return [finding["message"]]


def generate_message_script(bill_id: int) -> str:
    """Generate a written message for patient portal, text, or secure message.

    Covers all finding types with specific language, includes benchmark and
    OPPS context, and references applicable regulations.
    """
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
    total_savings = sum(
        json.loads(f["details"]).get("potential_savings", 0)
        for f in findings if f.get("details")
    )
    has_nsa = any(f["finding_type"] == "no_surprises_act" for f in findings)

    lines = [
        "Subject: Billing Inquiry - Request for Itemized Review",
        "",
        "Dear Billing Department,",
        "",
        f"I am writing regarding my account with {bill.get('provider_name', 'your facility')}. "
        "After carefully reviewing my itemized bill, I have identified the "
        "following concerns that I believe require correction:",
        "",
    ]

    for i, finding in enumerate(findings[:5], 1):
        details = json.loads(finding["details"]) if finding.get("details") else {}
        li = details.get("line_item", {})
        lines.append(_message_line_for_finding(i, finding, details, li))

    lines.append("")

    if has_nsa:
        lines.append(
            "I would also like to note that under the No Surprises Act (effective "
            "January 1, 2022), patients who receive emergency services or care "
            "from out-of-network providers at in-network facilities are protected "
            "from balance billing above the in-network rate."
        )
        lines.append("")

    lines.append(
        "I respectfully request a line-by-line review of these charges and a "
        "corrected bill. I would also appreciate information about any financial "
        "assistance programs, prompt-pay discounts, or payment plan options."
    )

    if total_savings > 0:
        lines.append("")
        lines.append(
            f"Based on my review, the total potential adjustment is approximately "
            f"${total_savings:,.2f}."
        )

    lines.append("")
    lines.append(
        "Thank you for your attention to this matter. I look forward to your "
        "response within 30 days."
    )

    return "\n".join(lines)


def _message_line_for_finding(num: int, finding: dict, details: dict, li: dict) -> str:
    """Return a single numbered line for a written message."""
    ftype = finding["finding_type"]

    if ftype == "duplicate_charge":
        return (
            f"{num}. Possible duplicate: {li.get('description', 'A service')} "
            f"(CPT {li.get('cpt_code', 'N/A')}) appears billed more than once "
            f"on {li.get('date_of_service', 'the same date')}. "
            f"If this is an error, the adjustment would be "
            f"${details.get('potential_savings', 0):,.2f}."
        )

    if ftype == "price_markup":
        line = (
            f"{num}. Pricing concern: {li.get('description', 'A service')} "
            f"(CPT {li.get('cpt_code', 'N/A')}) was charged at "
            f"${details.get('charged', 0):,.2f}, while the Medicare rate "
            f"for my area is ${details.get('medicare_rate', 0):,.2f} "
            f"({details.get('markup_multiple', 0)}x markup)."
        )
        if details.get("total_medicare"):
            line += (
                f" Including the OPPS facility fee, Medicare's total allowable "
                f"is ${details['total_medicare']:,.2f}."
            )
        return line

    if ftype == "unbundling":
        return (
            f"{num}. Coding concern: {details.get('code_1', 'A comprehensive code')} "
            f"and {details.get('code_2', 'a component code')} were billed together. "
            f"Per NCCI Procedure-to-Procedure edits, "
            f"{details.get('code_2', 'the component code')} is included in "
            f"{details.get('code_1', 'the comprehensive code')} and should "
            f"not be separately reimbursed. Adjustment: "
            f"${details.get('potential_savings', 0):,.2f}."
        )

    if ftype == "upcoding":
        return (
            f"{num}. Coding question: I was billed for a Level "
            f"{details.get('billed_level', '')} visit (CPT {li.get('cpt_code', 'N/A')}), "
            f"but my visit may qualify as Level {details.get('likely_level', '')}. "
            f"I request a review of the clinical documentation to confirm "
            f"the visit level."
        )

    if ftype == "quantity_flag":
        return (
            f"{num}. Quantity question: {li.get('description', 'A service')} "
            f"was billed for {li.get('quantity', '')} units. Please confirm "
            f"this quantity is accurate."
        )

    if ftype == "benchmark_outlier":
        return (
            f"{num}. Above-market pricing: {li.get('description', 'A service')} "
            f"(CPT {li.get('cpt_code', 'N/A')}) was charged at "
            f"${details.get('charged', 0):,.2f}. The national median hospital "
            f"charge for this procedure is ${details.get('median_charged', 0):,.2f} "
            f"(based on {details.get('sample_size', 'N/A')} claims). I request "
            f"a fair-price adjustment."
        )

    if ftype == "no_surprises_act":
        return (
            f"{num}. No Surprises Act: This bill may include balance billing "
            f"for emergency or out-of-network services at an in-network facility. "
            f"Under federal law, I should not owe more than my in-network "
            f"cost-sharing amount."
        )

    return f"{num}. {finding['message']}"
