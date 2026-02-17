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

        line_items = db.execute(
            "SELECT * FROM line_items WHERE bill_id = ?", (neg["bill_id"],)
        ).fetchall()

        previous_messages = db.execute(
            "SELECT * FROM negotiation_messages WHERE negotiation_id = ? ORDER BY id",
            (negotiation_id,),
        ).fetchall()

    neg = dict(neg)
    findings = [dict(f) for f in findings]
    items = [dict(li) for li in line_items]
    stage = neg["current_stage"]
    stage_config = NEGOTIATION_STAGES.get(stage, NEGOTIATION_STAGES["stage_1"])

    hospital_responses = [
        dict(m) for m in previous_messages if m["direction"] == "inbound"
    ]
    last_response = hospital_responses[-1]["body"] if hospital_responses else None

    insured = _is_insurance_processed(items)

    insurance_context = ""
    if insured:
        insurance_context = """
INSURANCE STATUS: Insurance has already processed this claim. The patient's
responsibility (deductible/copay/coinsurance) has been determined.

IMPORTANT FRAMING:
- Do NOT argue that the hospital should charge the Medicare rate
- Do NOT compare the billed amount to the Medicare rate as the main argument
- DO acknowledge that insurance has processed the claim
- DO reference the patient's actual out-of-pocket responsibility
- DO ask for billing errors to be corrected and resubmitted to insurance
- DO ask about prompt-pay discounts and financial assistance programs
- DO use Medicare rates only as context for what is reasonable, not as a demand
"""
    else:
        insurance_context = """
INSURANCE STATUS: Self-pay / no insurance processing detected.
- DO compare charges to Medicare rates and median hospital prices
- DO ask for a self-pay or cash rate
- DO request specific dollar adjustments based on fair pricing
"""

    prompt = f"""You are a medical billing advocate writing on behalf of a patient.

ROLE: Authorized representative communicating with hospital billing
about factual billing errors. NOT a lawyer. NOT giving legal advice.

STAGE: {stage_config['name']}
TONE: {stage_config['tone']}

PATIENT ACCOUNT: {neg['account_number']}
HOSPITAL: {neg['hospital_name']}
PATIENT BALANCE: ${neg['original_amount']:,.2f}
{insurance_context}
FINDINGS:
{json.dumps(findings, indent=2, default=str)}

{"HOSPITAL PREVIOUS RESPONSE: " + last_response if last_response else "This is the initial dispute letter."}

RULES:
- NEVER threaten lawsuits or legal action
- NEVER give medical opinions or dispute medical necessity
- NEVER use words: illegal, fraud, scam, criminal, demand, require
- DO cite specific CPT codes and Medicare rates as context
- DO reference applicable regulations (informational, not threatening)
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


def _is_insurance_processed(items: list[dict]) -> bool:
    """Return True if any line item shows insurance has processed the claim."""
    return any(
        li.get("insurance_paid") or li.get("patient_responsibility")
        for li in items
    )


def generate_phone_script(bill_id: int) -> str:
    """Generate a phone script aware of whether insurance has already processed.

    When insurance has processed, the script frames arguments around the
    patient's actual responsibility — not the billed charge — and asks for
    corrections to be resubmitted, plus prompt-pay / financial-assistance
    options.  When no insurance info exists, it negotiates as self-pay.
    """
    with get_db() as db:
        bill = db.execute("SELECT * FROM bills WHERE id = ?", (bill_id,)).fetchone()
        findings = db.execute(
            "SELECT * FROM findings WHERE bill_id = ? ORDER BY "
            "CASE severity WHEN 'high' THEN 0 WHEN 'medium' THEN 1 ELSE 2 END",
            (bill_id,),
        ).fetchall()
        line_items = db.execute(
            "SELECT * FROM line_items WHERE bill_id = ?", (bill_id,)
        ).fetchall()

    if not bill or not findings:
        return ""

    bill = dict(bill)
    findings = [dict(f) for f in findings]
    items = [dict(li) for li in line_items]

    total_savings = sum(
        json.loads(f["details"]).get("potential_savings", 0)
        for f in findings if f.get("details")
    )

    provider = bill.get("provider_name", "the provider")
    insured = _is_insurance_processed(items)
    total_patient_owes = bill.get("total_patient_owes") or 0

    lines = [
        "BEFORE YOU CALL",
        "---------------",
        "Have ready: your itemized bill, your insurance Explanation of Benefits (EOB), and a pen.",
        "Ask for: the billing department, then a supervisor if the first person can't help.",
        "Record: the name of everyone you speak with and any reference numbers.",
        "",
        "WHAT TO SAY",
        "-----------",
    ]

    if insured and total_patient_owes > 0:
        lines.append(
            f"\"Hi, I'm calling about my account with {provider}. "
            f"I see my insurance has processed this claim and my "
            f"patient responsibility is ${total_patient_owes:,.2f}. "
            f"Before I pay, I have a few questions about the charges."
        )
    else:
        lines.append(
            f"\"Hi, I'm calling about my account with {provider}. "
            "I've reviewed my itemized bill and have some specific questions."
        )
    lines.append("")

    for i, finding in enumerate(findings[:5], 1):
        details = json.loads(finding["details"]) if finding.get("details") else {}
        li = details.get("line_item", {})
        lines.append(f"POINT {i}:")
        lines.extend(_phone_lines_for_finding(finding, details, li))
        lines.append("")

    if insured:
        lines.append(
            "If any of these charges are incorrect, I'd appreciate them being "
            "corrected and resubmitted to my insurance so my patient responsibility "
            "is recalculated. I'd also like to ask about any prompt-pay discounts "
            "or financial assistance programs.\""
        )
    elif total_savings > 0:
        lines.append(
            f"Altogether, I believe these adjustments total approximately "
            f"${total_savings:,.2f}. I'd like to request a corrected bill.\""
        )
    else:
        lines.append(
            "I'd like to request a corrected bill that addresses these items.\""
        )
    lines.append("")

    lines.append("IF THEY PUSH BACK")
    lines.append("------------------")

    if insured:
        lines.extend([
            "If they say \"your insurance determined what you owe\":",
            "  \"I understand, but I want to verify the charges are correct first. "
            "If there's a billing error, it should be corrected and resubmitted "
            "to my insurance. Can someone review these specific items?\"",
            "",
            "If they say the charges are correct:",
            "  \"OK. Do you offer a prompt-pay discount if I pay today? "
            "I'd also like information about your financial assistance program "
            "and any payment plan options.\"",
            "",
            "If they refuse any help:",
            "  \"I'd like to speak with a supervisor or patient advocate. "
            "I'll also be sending this request in writing for your records.\"",
        ])
    else:
        lines.extend([
            "If they say \"that's our standard rate\":",
            "  \"I understand, but these charges are well above Medicare rates. "
            "What is your self-pay or cash price for these services?\"",
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
    """Return talking-point lines for a single finding.

    Automatically adapts language when the line item has patient_responsibility
    or insurance_paid (i.e. insurance already processed).
    """
    ftype = finding["finding_type"]
    patient_resp = li.get("patient_responsibility")
    has_insurance = patient_resp is not None or li.get("insurance_paid") is not None

    if ftype == "duplicate_charge":
        line = (
            f"I see {li.get('description', 'a charge')} "
            f"(CPT {li.get('cpt_code', 'N/A')}) appears to be billed twice "
            f"on {li.get('date_of_service', 'the same date')}. "
            f"Can you confirm whether this was actually performed twice?"
        )
        if has_insurance:
            line += (
                " If this is an error, it should be corrected and resubmitted "
                "to my insurance so my responsibility is recalculated."
            )
        else:
            line += (
                f" If not, that's ${details.get('potential_savings', 0):,.2f} "
                f"that should be removed."
            )
        return [line]

    if ftype == "price_markup":
        if has_insurance and patient_resp:
            point = (
                f"For {li.get('description', 'a service')} "
                f"(CPT {li.get('cpt_code', 'N/A')}), my patient responsibility "
                f"is ${patient_resp:,.2f}. I've looked into this and Medicare "
                f"reimburses ${details.get('medicare_rate', 0):,.2f} for this service."
            )
            if details.get("total_medicare"):
                point += (
                    f" Even including the facility fee, Medicare's total is "
                    f"${details['total_medicare']:,.2f}."
                )
            point += (
                " I'd appreciate any options to reduce my out-of-pocket, "
                "such as a prompt-pay discount or fair-price adjustment."
            )
        else:
            point = (
                f"I was charged ${details.get('charged', 0):,.2f} for "
                f"{li.get('description', 'a service')} "
                f"(CPT {li.get('cpt_code', 'N/A')}). "
                f"The Medicare rate is ${details.get('medicare_rate', 0):,.2f} "
                f"-- that's a {details.get('markup_multiple', 0)}x markup."
            )
            if details.get("total_medicare"):
                point += (
                    f" Even including the hospital facility fee, Medicare's total is "
                    f"${details['total_medicare']:,.2f}."
                )
            point += " What is your self-pay or fair-price rate for this?"
        return [point]

    if ftype == "unbundling":
        line = (
            f"I see both {details.get('code_1', 'a comprehensive code')} and "
            f"{details.get('code_2', 'a component code')} were billed together. "
            f"Under NCCI coding rules, {details.get('code_2', 'the component code')} "
            f"is included in {details.get('code_1', 'the comprehensive code')} "
            f"and shouldn't be billed separately."
        )
        if has_insurance:
            line += (
                " If corrected, this should be resubmitted to my insurance."
            )
        else:
            line += (
                f" That's ${details.get('potential_savings', 0):,.2f} "
                f"that should be removed."
            )
        return [line]

    if ftype == "upcoding":
        line = (
            f"I was billed for a Level {details.get('billed_level', '')} visit, "
            f"but my symptoms and treatment may be more consistent with "
            f"Level {details.get('likely_level', '')}. "
        )
        if has_insurance:
            line += (
                "Can you review the documentation? If the level is adjusted, "
                "it should be resubmitted to my insurance."
            )
        else:
            line += (
                f"The difference is ${details.get('potential_savings', 0):,.2f}. "
                f"Can you review the documentation to confirm the visit level?"
            )
        return [line]

    if ftype == "quantity_flag":
        return [
            f"I'm seeing {li.get('quantity', '')} units of "
            f"'{li.get('description', 'a service')}' on my bill. "
            f"Can you confirm that quantity is correct?"
        ]

    if ftype == "benchmark_outlier":
        if has_insurance and patient_resp:
            return [
                f"For {li.get('description', 'this service')}, my out-of-pocket "
                f"is ${patient_resp:,.2f}. The median hospital charge nationally "
                f"is ${details.get('median_charged', 0):,.2f} "
                f"(based on {details.get('sample_size', 'thousands of')} claims). "
                f"Given that, are there any options to reduce my balance?"
            ]
        return [
            f"My charge of ${details.get('charged', 0):,.2f} for "
            f"{li.get('description', 'this service')} is above what most hospitals charge. "
            f"The median charge nationally is ${details.get('median_charged', 0):,.2f} "
            f"based on {details.get('sample_size', 'thousands of')} bills. "
            f"Can we discuss a more reasonable price?"
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
    """Generate a written message aware of insurance processing status.

    When insurance has processed, the letter acknowledges the patient's
    responsibility amount and asks for corrections to be resubmitted plus
    discount options — instead of arguing about the billed charge.
    """
    with get_db() as db:
        bill = db.execute("SELECT * FROM bills WHERE id = ?", (bill_id,)).fetchone()
        findings = db.execute(
            "SELECT * FROM findings WHERE bill_id = ? ORDER BY "
            "CASE severity WHEN 'high' THEN 0 WHEN 'medium' THEN 1 ELSE 2 END",
            (bill_id,),
        ).fetchall()
        line_items = db.execute(
            "SELECT * FROM line_items WHERE bill_id = ?", (bill_id,)
        ).fetchall()

    if not bill or not findings:
        return ""

    bill = dict(bill)
    findings = [dict(f) for f in findings]
    items = [dict(li) for li in line_items]

    total_savings = sum(
        json.loads(f["details"]).get("potential_savings", 0)
        for f in findings if f.get("details")
    )
    has_nsa = any(f["finding_type"] == "no_surprises_act" for f in findings)

    insured = _is_insurance_processed(items)
    total_patient_owes = bill.get("total_patient_owes") or 0

    lines = [
        "Subject: Billing Inquiry - Request for Itemized Review",
        "",
        "Dear Billing Department,",
        "",
    ]

    if insured and total_patient_owes > 0:
        lines.append(
            f"I am writing regarding my account with "
            f"{bill.get('provider_name', 'your facility')}. I understand my "
            f"insurance has processed this claim and my patient responsibility "
            f"is ${total_patient_owes:,.2f}. Before making payment, I would like "
            f"to raise the following questions about the underlying charges:"
        )
    else:
        lines.append(
            f"I am writing regarding my account with "
            f"{bill.get('provider_name', 'your facility')}. After carefully "
            f"reviewing my itemized bill, I have identified the following "
            f"concerns that I believe require correction:"
        )
    lines.append("")

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

    if insured:
        lines.append(
            "If any of the above items are billing or coding errors, I respectfully "
            "request they be corrected and the claim resubmitted to my insurance "
            "so my patient responsibility is recalculated. I would also appreciate "
            "information about any prompt-pay discounts, financial assistance "
            "programs, or payment plan options available to me."
        )
    else:
        lines.append(
            "I respectfully request a line-by-line review of these charges and a "
            "corrected bill. I would also appreciate information about any financial "
            "assistance programs, prompt-pay discounts, or payment plan options."
        )

    if not insured and total_savings > 0:
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
    """Return a single numbered line for a written message.

    Adapts language when insurance has processed (patient_responsibility
    present) versus self-pay.
    """
    ftype = finding["finding_type"]
    patient_resp = li.get("patient_responsibility")
    has_insurance = patient_resp is not None or li.get("insurance_paid") is not None

    if ftype == "duplicate_charge":
        line = (
            f"{num}. Possible duplicate: {li.get('description', 'A service')} "
            f"(CPT {li.get('cpt_code', 'N/A')}) appears billed more than once "
            f"on {li.get('date_of_service', 'the same date')}."
        )
        if has_insurance:
            line += (
                " If this is an error, please correct and resubmit to my insurance."
            )
        else:
            line += (
                f" If this is an error, the adjustment would be "
                f"${details.get('potential_savings', 0):,.2f}."
            )
        return line

    if ftype == "price_markup":
        if has_insurance and patient_resp:
            line = (
                f"{num}. Pricing question: For {li.get('description', 'a service')} "
                f"(CPT {li.get('cpt_code', 'N/A')}), my patient responsibility is "
                f"${patient_resp:,.2f}. Medicare reimburses "
                f"${details.get('medicare_rate', 0):,.2f} for this service."
            )
        else:
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
        line = (
            f"{num}. Coding concern: {details.get('code_1', 'A comprehensive code')} "
            f"and {details.get('code_2', 'a component code')} were billed together. "
            f"Per NCCI Procedure-to-Procedure edits, "
            f"{details.get('code_2', 'the component code')} is included in "
            f"{details.get('code_1', 'the comprehensive code')} and should "
            f"not be separately reimbursed."
        )
        if has_insurance:
            line += " Please correct and resubmit to my insurance."
        else:
            line += (
                f" Adjustment: ${details.get('potential_savings', 0):,.2f}."
            )
        return line

    if ftype == "upcoding":
        line = (
            f"{num}. Coding question: I was billed for a Level "
            f"{details.get('billed_level', '')} visit "
            f"(CPT {li.get('cpt_code', 'N/A')}), "
            f"but my visit may qualify as Level {details.get('likely_level', '')}. "
            f"I request a review of the clinical documentation."
        )
        if has_insurance:
            line += " If adjusted, please resubmit to my insurance."
        return line

    if ftype == "quantity_flag":
        return (
            f"{num}. Quantity question: {li.get('description', 'A service')} "
            f"was billed for {li.get('quantity', '')} units. Please confirm "
            f"this quantity is accurate."
        )

    if ftype == "benchmark_outlier":
        if has_insurance and patient_resp:
            return (
                f"{num}. Pricing context: For {li.get('description', 'a service')} "
                f"(CPT {li.get('cpt_code', 'N/A')}), my out-of-pocket is "
                f"${patient_resp:,.2f}. The national median hospital charge "
                f"is ${details.get('median_charged', 0):,.2f} "
                f"(based on {details.get('sample_size', 'N/A')} claims). "
                f"I would appreciate any available discount."
            )
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
