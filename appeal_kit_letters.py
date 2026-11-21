"""The ClaimCoach kit's other documents: the request to the doctor, the phone script and the next-level request.
All templates. They quote only what was read off the insurer's notice and never state a default-table date as fact.
"""

from __future__ import annotations

from datetime import date

from appeal_kit import _lower_label, _pretty_date, _reason_label, _val, _when
from appeal_letter import PRE_SERVICE_TIMINGS, address_lines, closing_name, helping_someone, signature_block

PHONE_EXTRA_QUESTION = {
    "medical_necessity": "Who reviewed this, and what are their credentials?",
    "prior_authorization": "Was an authorization requested for this service, and if so, when and by whom?",
    "out_of_network": "How was this provider's network status decided, and is there an in-network provider for this care?",
    "coding_error": "Which code or piece of information on the claim caused the denial?",
}
UNPRINTED_DEADLINE_QUESTION = "I don't see a deadline printed on my letter. What is the last day I can file?"
CLAIM_NUMBER_ON_EVERY_PAGE = "Please put the claim number on every page."


def _doctor_timing(case: dict) -> str:
    file_by = _pretty_date(case.get("file_by"))
    if file_by and case.get("deadline_source") == "default":
        return (f"The usual deadline for this kind of plan is {file_by}. I am checking my letter for the exact date. "
                "I would be grateful to have your letter at least a week before then.")
    if file_by:
        return f"My appeal has to be filed by {file_by}. I would be grateful to have your letter at least a week before then, so I have time to file."
    return "I would be grateful to have your letter as soon as you can, so I can file on time."


def _doctor_insurer_reason(case: dict) -> str | None:
    """What the insurer said, so the doctor's letter can answer it. Only fields read off the notice."""
    reason, criteria = case.get("denial_reason_text"), case.get("criteria_cited")
    stop = "" if reason and reason.endswith(".") else "."
    if reason and criteria:
        said = f"The insurer's stated reason: '{reason}'{stop} It cited {criteria}."
    elif reason:
        said = f"The insurer's stated reason: '{reason}'{stop}"
    elif criteria:
        said = f"The insurer cited {criteria}."
    else:
        return None
    return f"{said} It would help most if your letter speaks to that directly."


def build_doctor_request(case: dict) -> str:
    """A short letter from the patient (or the person helping them) asking the provider for a letter of medical necessity."""
    insurer = _val(case, "insurer_name", "[INSURER NAME]")
    service = _val(case, "service_description", "the service listed above")
    patient = _val(case, "patient_name", "[YOUR NAME]")
    fax = case.get("insurer_appeal_fax")
    fax_line = f"You can fax your letter to me or straight to the plan at {fax}. " if fax else ""
    lines = [
        _pretty_date(date.today()),
        f"{_val(case, 'provider_name', '[PROVIDER]')}\nAttn: [DOCTOR'S NAME]",
        "RE: Request for a letter of medical necessity\n"
        f"Patient: {patient}\n"
        f"Member ID: {_val(case, 'member_id', '[MEMBER ID]')}\n"
        f"Claim or reference number: {_val(case, 'claim_number', '[CLAIM NUMBER]')}\n"
        f"Date of service: {_when(case, 'service_date', '[DATE OF SERVICE]')}",
        "Dear [DOCTOR'S NAME],",
        f"{insurer} denied coverage for {service} on {_when(case, 'denial_date', '[DATE OF DENIAL]')}. "
        f"The denial reason is listed as: {_reason_label(case)}. I am appealing this decision and I need your help. {_doctor_timing(case)}",
    ]
    insurer_reason = _doctor_insurer_reason(case)
    if insurer_reason:
        lines.append(insurer_reason)
    if case.get("service_timing") == "urgent":
        health = "their health" if helping_someone(case) else "my health"
        lines.append(f"This is urgent. Waiting could seriously harm {health}, so I am asking for an expedited appeal and would appreciate your help right away.")
    lines += [
        "I am asking for two things:\n"
        "1. A letter of medical necessity.\n"
        "2. If my plan offers it, a peer-to-peer review, where you speak directly with the insurer's reviewing doctor about this decision.",
        "It would help if the letter covered:\n"
        "- My diagnosis\n"
        "- Why this treatment or service is the right one for me\n"
        "- What was tried first, and what happened\n"
        "- What is likely to happen to my health without it",
        f"{fax_line}{CLAIM_NUMBER_ON_EVERY_PAGE}",
        "I have enclosed a copy of the denial letter. Please call me if you need anything else from me. Thank you for your help.",
        f"Sincerely,\n\n{closing_name({**case, 'patient_name': patient})}\n{case.get('phone') or '[YOUR PHONE NUMBER]'}",
    ]
    return "\n\n".join(lines)


def _deadline_question(case: dict, level: str) -> str:
    file_by = _pretty_date(case.get("file_by"))
    if file_by and case.get("deadline_source") == "letter":
        return f"What is the deadline to file my {level}? My letter says I have until {file_by}. Can you confirm that?"
    return UNPRINTED_DEADLINE_QUESTION


def phone_script(case: dict) -> list[dict]:
    """The call to the insurer, one step at a time: what to say and what to ask."""
    level = _lower_label(case.get("level_label") or "appeal")
    address = case.get("insurer_appeal_address")
    pre_service = case.get("service_timing") in PRE_SERVICE_TIMINGS
    why = ("I'm calling about a prior authorization that was denied, and I plan to appeal. Can you confirm the denial and tell me the reason in your system?"
           if pre_service else
           "I'm calling about a denied claim and I plan to appeal. Can you confirm the claim was denied and tell me the reason in your system?")
    where = f"I have this address for appeals: {address}. Is that right?" if address else "What is the address or fax number for appeals?"
    criteria_cited = case.get("criteria_cited")
    criteria = (f"Your notice cites {criteria_cited}. Please send me a complete copy in writing." if criteria_cited
                else "Which specific criteria or plan provision was used to make this decision? Please send me a copy in writing.")
    extra = PHONE_EXTRA_QUESTION.get(case.get("denial_reason"))
    patient = _val(case, "patient_name", "[YOUR NAME]")
    caller, member = (f"{case['representative_name']}. I'm helping {patient}", "The") if helping_someone(case) else (patient, "My")
    steps = [
        {"heading": "Say who you are",
         "say": f"Hello, my name is {caller}. I'm calling about claim {_val(case, 'claim_number', '[CLAIM NUMBER]')}. "
                f"{member} member ID is {_val(case, 'member_id', '[MEMBER ID]')}."},
        {"heading": "Say why you are calling", "say": why},
        {"heading": "Ask what the decision was based on", "say": f"{criteria} {extra}" if extra else criteria},
        {"heading": "Confirm the deadline and where to send your appeal", "say": f"{_deadline_question(case, level)} {where}"},
    ]
    if case.get("service_timing") == "urgent":
        health = "their health" if helping_someone(case) else "my health"
        steps.append({"heading": "Ask for an expedited appeal",
                      "say": f"Waiting for a standard decision could seriously harm {health}. I'd like to request an expedited appeal. Who do I speak to so I can start that today?"})
    steps.append({"heading": "Get a reference number",
                  "say": "Can I have a reference number for this call, and your name? I'll write down today's date and the time."})
    return steps


def _next_level_notice(case: dict, next_level: dict, denial_date: str, claim: str) -> str:
    insurer = _val(case, "insurer_name", "[INSURER NAME]")
    return (
        f"What happens next: {next_level['level_label']}\n\n"
        f"{next_level['goes_to']}\n\n"
        "Keep these ready in case the reviewer asks for them:\n"
        "- The plan's letter upholding its decision\n"
        f"- Your original denial letter dated {denial_date}\n"
        "- Your letter of medical necessity and your medical records\n"
        "- Your call notes, with dates, names and reference numbers\n"
        f"- Your claim number: {claim}\n\n"
        f"Watch your mail for a letter about the review. If you don't hear anything, call {insurer} and ask whether your case has been sent, "
        "and ask for a reference number."
    )


def build_external_review_request(case: dict, next_level: dict) -> str:
    """The next step after an upheld appeal: a note if the plan forwards the case itself, otherwise a request letter."""
    insurer = _val(case, "insurer_name", "[INSURER NAME]")
    service = _val(case, "service_description", "the service listed above")
    denial_date = _when(case, "denial_date", "[DATE OF DENIAL]")
    claim = _val(case, "claim_number", "[CLAIM NUMBER]")
    if next_level["automatic"]:
        return _next_level_notice(case, next_level, denial_date, claim)
    label = next_level["level_label"]
    final_denial = _when(case, "decision_letter_date", "[DATE OF FINAL DENIAL LETTER]")
    addressee = address_lines(None, case.get("next_level_address")) or ["[WHERE TO SEND THIS REQUEST, from your final denial letter]"]
    lines = [
        _pretty_date(date.today()),
        "\n".join([*addressee, f"Attn: {label}"]),
        f"RE: Request for {_lower_label(label)}\n"
        f"Member name: {_val(case, 'patient_name', '[YOUR NAME]')}\n"
        f"Member ID: {_val(case, 'member_id', '[MEMBER ID]')}\n"
        f"Claim or reference number: {claim}\n"
        f"Insurer: {insurer}\n"
        f"Provider: {_val(case, 'provider_name', '[PROVIDER]')}\n"
        f"Date of service: {_when(case, 'service_date', '[DATE OF SERVICE]')}\n"
        f"Date of original denial: {denial_date}\n"
        f"Date of final denial: {final_denial}",
        "To the reviewer:",
        f"I am asking for {_lower_label(label)} of the denial of coverage for {service}. {insurer} denied this on {denial_date} "
        f"and upheld its decision in a final denial letter dated {final_denial}. I disagree with that decision.",
        f"The reason given for the denial is: {_reason_label(case)}. I ask the reviewer to look at this denial again, independently, "
        "using the enclosed records and the statement from my treating provider.",
    ]
    if case.get("case_paragraph"):
        lines.append(case["case_paragraph"])
    lines += [
        "Please send your written decision to the address below. Contact me if you need anything else to start the review.",
        "Enclosures:\n"
        "- The final denial letter\n"
        f"- The original denial letter dated {denial_date}\n"
        "- My appeal letter and any response to it\n"
        "- Letter of medical necessity from my treating provider (if available)\n"
        "- Relevant medical records\n"
        "- Authorized representative form (if required)",
        signature_block(case),
    ]
    return "\n\n".join(lines)
