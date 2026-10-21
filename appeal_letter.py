"""Insurance denial appeal letter, written from the intake answers.

The letter is a draft: the customer reviews and approves it before it is sent.
"""

from datetime import date

PLAN_TYPES = {
    "employer": "Employer or union plan",
    "individual": "Marketplace or individual plan",
    "medicare_advantage": "Medicare Advantage plan",
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

_REASON_ARGUMENTS = {
    "medical_necessity": (
        "The plan denied this service as not medically necessary. My treating provider ordered it to treat "
        "my condition, and a letter of medical necessity from my provider is enclosed. Please send me the "
        "clinical criteria or guideline used to make this decision and the name and credentials of the "
        "reviewer. I also ask that this appeal be reviewed by a physician in the same or a similar specialty "
        "as my treating provider, and that my provider be offered a peer-to-peer review."
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
        "The plan denied this service as experimental or investigational. This treatment is an accepted "
        "standard of care for my condition. Please send me the specific plan provision and the evidence "
        "the plan relied on, and reconsider the denial in light of the enclosed medical records and "
        "provider statement."
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

_ENCLOSURES = [
    "Copy of the denial letter or Explanation of Benefits",
    "Letter of medical necessity from my treating provider (if available)",
    "Relevant medical records",
    "Authorized representative form (if required by the plan)",
]


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
        f"Amount denied: ${case['amount_denied']:,.2f}",
    ]
    service = case.get("service_description") or "the service listed above"
    urgent = case.get("service_timing") == "urgent"
    paragraphs = [
        today.strftime("%B %d, %Y").replace(" 0", " "),
        f"{case['insurer_name']}\nAttn: Appeals Department\n{case.get('insurer_appeal_address') or '[APPEALS ADDRESS]'}",
        "RE: " + ("Request for EXPEDITED appeal" if urgent else "Request for internal appeal") + "\n" + "\n".join(reference_lines),
        "To the Appeals Department:",
        f"I am writing to appeal the denial of coverage for {service}, which I received notice of on "
        f"{case['denial_date']}. Please treat this letter as my formal request for an internal appeal.",
        _REASON_ARGUMENTS.get(case["denial_reason"], _REASON_ARGUMENTS["other"]),
    ]
    if urgent:
        paragraphs.append(
            "My provider has indicated that waiting the standard time for a decision could seriously "
            "jeopardize my health. I request an expedited decision within 72 hours."
        )
    if case.get("plan_type") in _RIGHTS:
        paragraphs.append(_RIGHTS[case["plan_type"]])
    paragraphs.append(
        "Please overturn the denial and process the claim for payment. Send your written decision to the "
        "address below, and contact me if you need anything else to decide this appeal."
    )
    paragraphs.append("Enclosures:\n" + "\n".join(f"- {item}" for item in _ENCLOSURES))
    signature = [
        "Sincerely,",
        "",
        case["patient_name"],
        case.get("mailing_address") or "[YOUR ADDRESS]",
        case.get("phone") or "",
        case["email"],
    ]
    paragraphs.append("\n".join(line for line in signature if line is not None).rstrip())
    return "\n\n".join(paragraphs)
