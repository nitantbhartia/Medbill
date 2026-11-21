"""Insurance denial appeal letter, written from the intake answers.

The letter is a draft: the customer reviews and approves it before it is sent.
"""

import re
from datetime import date

PLAN_TYPES = {
    "employer": "Employer or union plan",
    "individual": "Marketplace or individual plan",
    "medicare_advantage": "Medicare Advantage plan",
    "original_medicare": "Original Medicare (Part A or B)",
    "medicaid": "Medicaid plan",
    "other": "Other or not sure",
}

SERVICE_TIMINGS = {
    "post_service": "I already had the care (a claim was denied)",
    "pre_service": "I haven't had the care yet (a prior authorization was denied)",
    "urgent": "It's urgent: waiting could seriously harm my health",
}

DENIAL_REASONS = {
    "medical_necessity": "Not medically necessary",
    "prior_authorization": "No prior authorization",
    "out_of_network": "Out of network",
    "experimental": "Experimental or investigational",
    "not_covered": "Not a covered benefit",
    "coding_error": "Billing or coding error",
    "other": "Other or not sure",
}

RELATIONSHIPS = {"parent": "parent", "spouse": "spouse", "adult_child": "adult child", "other": None}
PRE_SERVICE_TIMINGS = ("pre_service", "urgent")
DOCTOR_LETTER_ENCLOSED = "A letter of medical necessity from my provider is enclosed."
DOCTOR_LETTER_PENDING = (
    "I have asked my provider for a letter of medical necessity and will send it as soon as I have it. "
    "Please do not decide this appeal before you receive it."
)
CRITERIA_REQUEST = "Please send me the clinical criteria or guideline used to make this decision."
STATE_ZIP_LINE = re.compile(r"^[A-Z]{2}\s+\d{5}(-\d{4})?$")

_REASON_ARGUMENTS = {
    "medical_necessity": (
        "The plan denied this service as not medically necessary. My treating provider ordered it to treat "
        "my condition. Please send me the name and credentials of the reviewer. I also ask that this appeal "
        "be reviewed by a physician in the same or a similar specialty as my treating provider, and that my "
        "provider be offered a peer-to-peer review."
    ),
    "prior_authorization": (
        "The plan denied this service for lack of prior authorization. Please review whether authorization "
        "was in fact requested, whether it was required for this service under my plan, and whether the "
        "care was urgent or emergency care that cannot require prior authorization. If authorization was "
        "required, I ask the plan to grant it retroactively, because the service was medically necessary."
    ),
    "out_of_network": (
        "The plan processed this service as out of network. I ask the plan to apply in-network cost sharing "
        "because the care was either emergency care, provided at an in-network facility by a provider I did "
        "not choose, or not available from an in-network provider within a reasonable time or distance. "
        "Where the federal No Surprises Act applies, I may not be billed more than in-network cost sharing."
    ),
    "experimental": (
        "The plan denied this service as experimental or investigational. My treating provider recommended "
        "this treatment for my condition. Please send me the specific plan provision and the evidence "
        "the plan relied on, and reconsider the denial in light of my medical records."
    ),
    "not_covered": (
        "The plan denied this service as not covered. Please identify the specific plan provision relied on "
        "and send me a copy of my plan documents. Based on my plan's description of benefits, I believe "
        "this service is covered."
    ),
    "coding_error": (
        "This denial appears to result from a billing or coding error on the claim, not from the care itself. "
        "I ask the plan to reprocess the claim once the provider submits a corrected claim, and to treat "
        "this letter as a timely appeal so my rights are preserved in the meantime."
    ),
    "other": (
        "I believe this claim was denied in error. Please review the enclosed records and reprocess the "
        "claim, and send me the specific reason for the denial and the plan provision relied on."
    ),
}

_RIGHTS = {
    "employer": (
        "Under federal claims rules for employer plans (29 CFR 2560.503-1), I am entitled to a full and fair "
        "review and to receive, free of charge, copies of all documents, records and other information "
        "relevant to my claim, including any internal rule, guideline or criterion relied on."
    ),
    "individual": (
        "Under federal rules for individual health coverage (45 CFR 147.136), I am entitled to a full and fair "
        "review, to see and respond to any new evidence the plan relies on, and to external review by an "
        "independent organization if the denial is upheld."
    ),
    "medicare_advantage": (
        "I am requesting a reconsideration of this organization determination under Medicare Advantage rules "
        "(42 CFR 422.578). If the plan upholds its decision, I understand the case is forwarded to the "
        "Independent Review Entity."
    ),
}



def _article(noun: str) -> str:
    return ("an " if noun[0].lower() in "aeiou" else "a ") + noun


def address_lines(insurer_name: str | None, address: str | None) -> list[str]:
    """An address split on commas and line breaks, one line each, without a repeat of the insurer's name.
    A trailing state and ZIP stays on the city's line."""
    parts = [part.strip() for part in re.split(r"[,\n]", address or "") if part.strip()]
    if parts and insurer_name and parts[0].lower().startswith(insurer_name.lower()):
        parts = parts[1:]
    if len(parts) > 1 and STATE_ZIP_LINE.match(parts[-1]):
        parts[-2:] = [f"{parts[-2]}, {parts[-1]}"]
    return parts


def helping_someone(case: dict) -> bool:
    return case.get("for_whom") == "someone_else" and bool(case.get("representative_name"))


def closing_name(case: dict) -> str:
    """The name line under "Sincerely,": the patient, or the helper on the patient's behalf."""
    if not helping_someone(case):
        return case["patient_name"]
    relationship = RELATIONSHIPS.get(case.get("relationship"))
    suffix = f" ({relationship})" if relationship else ""
    return f"{case['representative_name']}, on behalf of {case['patient_name']}{suffix}"


def signature_block(case: dict) -> str:
    lines = ["Sincerely,", "", closing_name(case), case.get("mailing_address") or "[YOUR ADDRESS]", case.get("phone"), case.get("email")]
    return "\n".join(line for line in lines if line is not None).rstrip()


def _quote_back(case: dict) -> str | None:
    """What the insurer's own notice said, from the fields read off it. Nothing that was not read is cited."""
    reason, criteria = case.get("denial_reason_text"), case.get("criteria_cited")
    notice = f"Your notice dated {case['denial_date']}"
    if reason and criteria:
        return f"{notice} states: '{reason}' and cites {criteria}. Please send me a complete copy of {criteria}."
    if reason:
        return f"{notice} states: '{reason}'."
    if criteria:
        return f"{notice} cites {criteria}. Please send me a complete copy of {criteria}."
    return CRITERIA_REQUEST if case.get("denial_reason") == "medical_necessity" else None


def build_appeal_letter(case: dict, today: date | None = None) -> str:
    """Draft an internal appeal letter for a denied claim from the case's intake fields."""
    today = today or date.today()
    reference_lines = [
        f"Member name: {case['patient_name']}",
        f"Member ID: {case.get('member_id') or '[MEMBER ID]'}",
        f"Claim or reference number: {case.get('claim_number') or '[CLAIM NUMBER]'}",
        f"Provider: {case.get('provider_name') or '[PROVIDER]'}",
        f"Date of service: {case.get('service_date') or '[DATE OF SERVICE]'}",
        f"Date of denial: {case['denial_date']}",
    ]
    if case.get("amount_denied") is not None:
        reference_lines.append(f"Amount denied: ${case['amount_denied']:,.2f}")
    service = case.get("service_description") or "the service listed above"
    urgent = case.get("service_timing") == "urgent"
    level = case.get("level_label") or ""
    level = level if level[:3].isupper() else level[:1].lower() + level[1:]
    request_line = f"Request for EXPEDITED {level or 'appeal'}" if urgent else f"Request for {level or 'internal appeal'}"
    address = address_lines(case["insurer_name"], case.get("insurer_appeal_address")) or ["[APPEALS ADDRESS]"]
    paragraphs = [
        today.strftime("%B %d, %Y").replace(" 0", " "),
        "\n".join([case["insurer_name"], "Attn: Appeals Department", *address]),
        "RE: " + request_line + "\n" + "\n".join(reference_lines),
        "To the Appeals Department:",
        f"I am writing to appeal the denial of coverage for {service}, which I received notice of on "
        f"{case['denial_date']}. Please treat this letter as my formal request for {_article(level or 'internal appeal')}.",
    ]
    if helping_someone(case):
        paragraphs.append(f"I am helping {case['patient_name']} with this appeal. A signed authorization is enclosed.")
    paragraphs.append(_REASON_ARGUMENTS.get(case["denial_reason"], _REASON_ARGUMENTS["other"]))
    quote = _quote_back(case)
    if quote:
        paragraphs.append(quote)
    if case.get("case_paragraph"):
        paragraphs.append(case["case_paragraph"])
    has_doctor_letter = bool(case.get("has_doctor_letter"))
    paragraphs.append(DOCTOR_LETTER_ENCLOSED if has_doctor_letter else DOCTOR_LETTER_PENDING)
    if urgent:
        if helping_someone(case):
            opening = f"{case['patient_name']}'s provider has indicated that waiting the standard time for a decision could seriously jeopardize their health."
        else:
            opening = "My provider has indicated that waiting the standard time for a decision could seriously jeopardize my health."
        paragraphs.append(f"{opening} I request an expedited decision within 72 hours.")
    if case.get("plan_type") in _RIGHTS:
        paragraphs.append(_RIGHTS[case["plan_type"]])
    ask = "approve the requested service" if case.get("service_timing") in PRE_SERVICE_TIMINGS else "process the claim for payment"
    paragraphs.append(
        f"Please reverse the denial and {ask}. Send your written decision to the address below, and contact me "
        "if you need anything else to decide this appeal."
    )
    enclosures = [
        "Copy of the denial letter or Explanation of Benefits",
        "Letter of medical necessity from my treating provider" + ("" if has_doctor_letter else " (to follow)"),
        "Relevant medical records",
    ]
    if helping_someone(case):
        enclosures.append("Signed authorized representative form")
    paragraphs.append("Enclosures:\n" + "\n".join(f"- {item}" for item in enclosures))
    paragraphs.append(signature_block(case))
    return "\n\n".join(paragraphs)
