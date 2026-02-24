"""Medical debt fighting tools: SOL calculator, FDCPA letters, charity care, settlement offers."""
import json
import logging
import re
import urllib.error
import urllib.parse
import urllib.request
from datetime import date

log = logging.getLogger(__name__)

_MIN_DATE = date(1990, 1, 1)


def _sanitize_text(value: str) -> str:
    """Strip newlines and control characters from user input."""
    cleaned = re.sub(r"[\n\r\t]+", " ", value)
    cleaned = re.sub(r"[^\x20-\x7E]", "", cleaned)
    return cleaned.strip()


def _validate_amount(value: str) -> str:
    """Validate that amount looks like a dollar figure. Returns cleaned string."""
    cleaned = re.sub(r"[,$\s]", "", value.strip())
    try:
        num = float(cleaned)
    except ValueError:
        raise ValueError(f"Invalid amount: {value}")
    if num <= 0:
        raise ValueError("Amount must be positive")
    if num > 10_000_000:
        raise ValueError("Amount exceeds reasonable limit")
    return f"{num:,.2f}"


# ── SOL data ─────────────────────────────────────────────────────────────────
SOL_BY_STATE = {
    "AL": {"years": 6, "partial_resets_sol": True},
    "AK": {"years": 3, "partial_resets_sol": False},
    "AZ": {"years": 6, "partial_resets_sol": True},
    "AR": {"years": 5, "partial_resets_sol": True},
    "CA": {"years": 4, "partial_resets_sol": True},
    "CO": {"years": 6, "partial_resets_sol": True},
    "CT": {"years": 6, "partial_resets_sol": False},
    "DE": {"years": 3, "partial_resets_sol": True},
    "FL": {"years": 5, "partial_resets_sol": True},
    "GA": {"years": 6, "partial_resets_sol": True},
    "HI": {"years": 6, "partial_resets_sol": True},
    "ID": {"years": 5, "partial_resets_sol": True},
    "IL": {"years": 5, "partial_resets_sol": True},
    "IN": {"years": 6, "partial_resets_sol": True},
    "IA": {"years": 5, "partial_resets_sol": True},
    "KS": {"years": 5, "partial_resets_sol": True},
    "KY": {"years": 5, "partial_resets_sol": True},
    "LA": {"years": 3, "partial_resets_sol": True},
    "ME": {"years": 6, "partial_resets_sol": True},
    "MD": {"years": 3, "partial_resets_sol": True},
    "MA": {"years": 6, "partial_resets_sol": False},
    "MI": {"years": 6, "partial_resets_sol": True},
    "MN": {"years": 6, "partial_resets_sol": True},
    "MS": {"years": 3, "partial_resets_sol": True},
    "MO": {"years": 5, "partial_resets_sol": True},
    "MT": {"years": 5, "partial_resets_sol": True},
    "NE": {"years": 5, "partial_resets_sol": True},
    "NV": {"years": 6, "partial_resets_sol": True},
    "NH": {"years": 3, "partial_resets_sol": True},
    "NJ": {"years": 6, "partial_resets_sol": True},
    "NM": {"years": 6, "partial_resets_sol": True},
    "NY": {"years": 6, "partial_resets_sol": True},
    "NC": {"years": 3, "partial_resets_sol": True},
    "ND": {"years": 6, "partial_resets_sol": True},
    "OH": {"years": 6, "partial_resets_sol": True},
    "OK": {"years": 5, "partial_resets_sol": True},
    "OR": {"years": 6, "partial_resets_sol": True},
    "PA": {"years": 4, "partial_resets_sol": True},
    "RI": {"years": 10, "partial_resets_sol": True},
    "SC": {"years": 3, "partial_resets_sol": True},
    "SD": {"years": 6, "partial_resets_sol": True},
    "TN": {"years": 6, "partial_resets_sol": True},
    "TX": {"years": 4, "partial_resets_sol": True},
    "UT": {"years": 6, "partial_resets_sol": True},
    "VT": {"years": 6, "partial_resets_sol": True},
    "VA": {"years": 5, "partial_resets_sol": True},
    "WA": {"years": 6, "partial_resets_sol": True},
    "WV": {"years": 10, "partial_resets_sol": True},
    "WI": {"years": 6, "partial_resets_sol": True},
    "WY": {"years": 8, "partial_resets_sol": True},
    "DC": {"years": 3, "partial_resets_sol": True},
}

STATE_NAMES = {
    "AL": "Alabama", "AK": "Alaska", "AZ": "Arizona", "AR": "Arkansas",
    "CA": "California", "CO": "Colorado", "CT": "Connecticut", "DE": "Delaware",
    "FL": "Florida", "GA": "Georgia", "HI": "Hawaii", "ID": "Idaho",
    "IL": "Illinois", "IN": "Indiana", "IA": "Iowa", "KS": "Kansas",
    "KY": "Kentucky", "LA": "Louisiana", "ME": "Maine", "MD": "Maryland",
    "MA": "Massachusetts", "MI": "Michigan", "MN": "Minnesota", "MS": "Mississippi",
    "MO": "Missouri", "MT": "Montana", "NE": "Nebraska", "NV": "Nevada",
    "NH": "New Hampshire", "NJ": "New Jersey", "NM": "New Mexico", "NY": "New York",
    "NC": "North Carolina", "ND": "North Dakota", "OH": "Ohio", "OK": "Oklahoma",
    "OR": "Oregon", "PA": "Pennsylvania", "RI": "Rhode Island", "SC": "South Carolina",
    "SD": "South Dakota", "TN": "Tennessee", "TX": "Texas", "UT": "Utah",
    "VT": "Vermont", "VA": "Virginia", "WA": "Washington", "WV": "West Virginia",
    "WI": "Wisconsin", "WY": "Wyoming", "DC": "District of Columbia",
}

FPL_2025 = {
    1: 15650, 2: 21150, 3: 26650, 4: 32150,
    5: 37650, 6: 43150, 7: 48650, 8: 54150,
}
FPL_PER_ADDITIONAL = 5500

LEGAL_DISCLAIMER = (
    "This is a self-help document tool, not legal advice. "
    "BillKarma is not a law firm and does not provide legal representation. "
    "You are acting on your own behalf. Consult an attorney for complex situations."
)


# ── Letter types ─────────────────────────────────────────────────────────────

LETTER_TYPES = {
    "debt_validation": {
        "name": "Debt Validation Letter",
        "legal_basis": "15 U.S.C. \u00a7 1692g(b)",
        "description": (
            "Forces the collector to prove the debt is valid before they can "
            "continue collecting. They must provide the original creditor name, "
            "the amount owed with an itemized breakdown, and proof they have the "
            "right to collect."
        ),
        "best_for": (
            "Use this when you first receive a collection notice and are not sure "
            "if the debt is legitimate, if the amount is correct, or if the "
            "collector actually owns the debt."
        ),
        "what_happens": [
            "The collector must stop all collection activity until they validate the debt.",
            "They must provide proof they own the debt and the amount is correct.",
            "If they cannot validate, they must stop collecting and remove any credit reporting.",
            "If they continue collecting without validating, they violate federal law.",
        ],
        "timeline": [
            {"day": "Day 1", "event": "You send the letter via certified mail."},
            {"day": "Day 3-5", "event": "Collector receives your letter (keep tracking receipt)."},
            {"day": "Day 5-35", "event": "Collector has 30 days from receipt to respond with validation."},
            {"day": "Day 35+", "event": "If no response, the debt is likely not collectible. Save all records."},
        ],
    },
    "cease_desist": {
        "name": "Cease & Desist Letter",
        "legal_basis": "15 U.S.C. \u00a7 1692c(c)",
        "description": (
            "Demands the collector stop all contact with you. Once they receive this, "
            "they can only contact you to confirm they will stop, or to notify you of "
            "a specific legal action (lawsuit)."
        ),
        "best_for": (
            "Use this when a collector is harassing you with repeated calls, contacting "
            "you at work, or you have already validated (or dispute) the debt and want "
            "them to stop contacting you."
        ),
        "what_happens": [
            "The collector must stop all phone calls, letters, and other contact.",
            "They can only send one more letter confirming they will cease contact.",
            "They can still sue you — this letter does not make the debt go away.",
            "The debt will still appear on your credit report unless separately disputed.",
        ],
        "timeline": [
            {"day": "Day 1", "event": "You send the letter via certified mail."},
            {"day": "Day 3-5", "event": "Collector receives your letter."},
            {"day": "Day 5-10", "event": "All calls and contact should stop."},
            {"day": "Ongoing", "event": "If they continue contacting you, document every violation."},
        ],
    },
    "dispute_amount": {
        "name": "Dispute Amount Letter",
        "legal_basis": "15 U.S.C. \u00a7 1692g",
        "description": (
            "Challenges the accuracy of the debt amount when you believe the "
            "collector has the wrong figure — for example, if interest or fees "
            "were added improperly, or if you already made payments."
        ),
        "best_for": (
            "Use this when you recognize the debt but believe the amount is wrong. "
            "Maybe you already made payments, the original bill had errors, or "
            "improper fees and interest were added."
        ),
        "what_happens": [
            "The collector must provide an itemized breakdown of the amount claimed.",
            "They must account for all payments already made.",
            "They must justify all fees and interest charges.",
            "If they cannot itemize and justify the amount, you can dispute it.",
        ],
        "timeline": [
            {"day": "Day 1", "event": "You send the letter via certified mail."},
            {"day": "Day 3-5", "event": "Collector receives your letter."},
            {"day": "Day 5-35", "event": "Collector must respond with itemized statement."},
            {"day": "Day 35+", "event": "Compare their itemization to your records. Dispute any discrepancies."},
        ],
    },
}


# ── Educational content ──────────────────────────────────────────────────────

FDCPA_RIGHTS = [
    {
        "right": "Right to Validation",
        "detail": "Within 5 days of first contact, a collector must send you a written notice with the debt amount, creditor name, and your right to dispute. You have 30 days to dispute in writing.",
    },
    {
        "right": "Right to Stop Contact",
        "detail": "You can send a written cease-and-desist letter demanding they stop all communication. After that, they can only contact you to confirm they will stop, or to notify you of legal action.",
    },
    {
        "right": "Protection from Harassment",
        "detail": "Collectors cannot call before 8 AM or after 9 PM, cannot call your workplace if told not to, cannot use threatening language, and cannot discuss your debt with third parties.",
    },
    {
        "right": "Right to Sue for Violations",
        "detail": "If a collector violates the FDCPA, you can sue for up to $1,000 in statutory damages per violation, plus actual damages and attorney fees.",
    },
    {
        "right": "Protection Against False Reporting",
        "detail": "A collector cannot report a debt to credit bureaus without first providing you the required validation notice. If you dispute, they must report the debt as disputed.",
    },
]

CERTIFIED_MAIL_GUIDE = {
    "why": (
        "Certified mail creates a legal record proving the collector received your letter. "
        "Without it, the collector can claim they never got it. The tracking receipt is your proof."
    ),
    "steps": [
        "Print the letter on plain white paper. Sign it in ink.",
        "Make a copy of the signed letter for your records.",
        "Go to any USPS post office (or use usps.com).",
        "Ask for \"Certified Mail with Return Receipt\" (PS Form 3800).",
        "Fill out the green return receipt card (PS Form 3811) with the collector's address.",
        "The postal clerk will give you a tracking number. Keep this receipt.",
        "Cost is approximately $4.85 for certified mail + $3.35 for return receipt = ~$8.20 total.",
        "Track delivery at usps.com with your tracking number.",
    ],
    "tips": [
        "Keep the signed copy, the certified mail receipt, and the green return receipt card after it comes back.",
        "These three documents are your proof of mailing, delivery, and receipt.",
        "If the collector violates the FDCPA after receiving your letter, this proof is essential for any legal action.",
    ],
}

CHARITY_CARE_DOCUMENTS = [
    {
        "name": "Proof of Income",
        "items": [
            "Most recent federal tax return (Form 1040)",
            "Last 2-3 pay stubs (if employed)",
            "Social Security award letter (if receiving benefits)",
            "Unemployment benefits statement (if applicable)",
            "Self-employment records (if self-employed)",
        ],
    },
    {
        "name": "Proof of Household Size",
        "items": [
            "Most recent tax return showing dependents",
            "Birth certificates for children (some hospitals require)",
            "Marriage certificate (if applicable)",
        ],
    },
    {
        "name": "Medical Bill Information",
        "items": [
            "The hospital bill or statement of charges",
            "Account number from the bill",
            "Date(s) of service",
            "Insurance EOB (Explanation of Benefits) if you have insurance",
        ],
    },
    {
        "name": "Other Financial Information",
        "items": [
            "Bank statements (last 1-3 months, some hospitals require)",
            "List of monthly expenses (rent, utilities, etc.)",
            "Any other outstanding medical bills",
        ],
    },
]

CHARITY_CARE_PROCESS = [
    {
        "step": 1,
        "title": "Get the Application",
        "detail": (
            "Call the hospital's billing department and ask for a Financial Assistance Application. "
            "Under IRS Section 501(r), nonprofit hospitals MUST provide one. You can also check "
            "the hospital's website — they are required to post their Financial Assistance Policy online."
        ),
    },
    {
        "step": 2,
        "title": "Gather Your Documents",
        "detail": (
            "You will need proof of income (tax return, pay stubs), proof of household size, "
            "and the hospital bill. Some hospitals also ask for bank statements. "
            "See the full document checklist below."
        ),
    },
    {
        "step": 3,
        "title": "Complete and Submit the Application",
        "detail": (
            "Fill out the application completely. Attach all required documents. "
            "Submit by mail (certified recommended) or in person at the hospital billing office. "
            "Keep a copy of everything you submit."
        ),
    },
    {
        "step": 4,
        "title": "Wait for a Decision (typically 30-45 days)",
        "detail": (
            "The hospital must review your application. They may contact you for additional "
            "documents. During review, the hospital should pause any collection activity on your account."
        ),
    },
    {
        "step": 5,
        "title": "If Approved: Bill Reduced or Eliminated",
        "detail": (
            "If approved, the hospital will adjust your bill according to their sliding scale. "
            "At 200% FPL or below, most hospitals write off the entire bill. Above that, you may "
            "get a 25-75% discount. Get the approval in writing."
        ),
    },
    {
        "step": 6,
        "title": "If Denied: Appeal",
        "detail": (
            "You have the right to appeal. Write a letter explaining any hardship circumstances "
            "not captured in the initial application. Many denials are reversed on appeal. "
            "If the hospital refuses, contact your state attorney general's office."
        ),
    },
]


# ── SOL calculator ───────────────────────────────────────────────────────────

def check_sol(state: str, start_date: str) -> dict:
    """Check statute of limitations for a medical debt."""
    code = state.upper().strip()
    if code not in SOL_BY_STATE:
        return {"status": "error", "message": f"Unknown state: {state}"}

    try:
        dt = date.fromisoformat(start_date)
    except (ValueError, TypeError):
        return {"status": "error", "message": "Invalid date format. Use YYYY-MM-DD."}

    today = date.today()
    if dt > today:
        return {"status": "error", "message": "Date cannot be in the future."}
    if dt < _MIN_DATE:
        return {"status": "error", "message": "Date must be after 1990."}

    info = SOL_BY_STATE[code]
    sol_years = info["years"]
    try:
        expiry = date(dt.year + sol_years, dt.month, dt.day)
    except ValueError:
        expiry = date(dt.year + sol_years, dt.month, dt.day - 1)
    expired = today >= expiry

    return {
        "status": "ok",
        "state": code,
        "state_name": STATE_NAMES.get(code, code),
        "sol_years": sol_years,
        "start_date": start_date,
        "expiry_date": expiry.isoformat(),
        "expired": expired,
        "days_remaining": max(0, (expiry - today).days),
        "partial_resets_sol": info["partial_resets_sol"],
        "disclaimer": LEGAL_DISCLAIMER,
    }


# ── FDCPA letter generation ─────────────────────────────────────────────────

def generate_fdcpa_letter(
    letter_type: str,
    user_name: str,
    user_address: str,
    collector_name: str,
    collector_address: str,
    account_number: str,
    amount: str,
    date_of_notice: str = "",
    dispute_reason: str = "",
) -> dict:
    """Generate an FDCPA letter based on type.

    letter_type: 'debt_validation', 'cease_desist', or 'dispute_amount'
    """
    if letter_type not in LETTER_TYPES:
        raise ValueError(f"Unknown letter type: {letter_type}")

    user_name = _sanitize_text(user_name)
    user_address = _sanitize_text(user_address)
    collector_name = _sanitize_text(collector_name)
    collector_address = _sanitize_text(collector_address)
    account_number = _sanitize_text(account_number)
    amount = _validate_amount(amount)
    date_of_notice = _sanitize_text(date_of_notice) if date_of_notice else ""
    dispute_reason = _sanitize_text(dispute_reason) if dispute_reason else ""

    today_str = date.today().strftime("%B %d, %Y")
    header = f"""{user_name}
{user_address}

{today_str}

{collector_name}
{collector_address}

Re: Account #{account_number} — Amount Claimed: ${amount}

Dear Sir or Madam:"""

    if letter_type == "debt_validation":
        notice_ref = f" dated {date_of_notice}" if date_of_notice else ""
        body = f"""
I am writing in response to your communication{notice_ref} regarding the above-referenced account. I do not recognize this debt as valid.

Pursuant to my rights under the Fair Debt Collection Practices Act, 15 U.S.C. \u00a7 1692g(b), I am formally disputing this debt in its entirety and requesting that you provide the following validation:

1. The name and address of the original creditor
2. The original account number with the original creditor
3. A complete, itemized statement of the amount claimed, including all fees, interest, and charges
4. A copy of the original signed agreement or contract that creates the obligation
5. Proof that you are licensed to collect debts in my state
6. Documentation showing the chain of assignment from the original creditor to your company

Until you provide adequate validation of this debt, I demand that you:

- Cease all collection activity on this account
- Refrain from reporting this debt to any consumer reporting agency, or if already reported, notify the agencies that this debt is disputed
- Communicate with me only in writing at the address above

Please be advised that any continued collection activity or reporting without providing proper validation may constitute a violation of the FDCPA, for which I may seek statutory damages.

This letter is not an acknowledgment that I owe this debt, nor a promise to pay. It is solely a request for validation as permitted by federal law."""

    elif letter_type == "cease_desist":
        body = """
I am writing regarding the above-referenced account. Pursuant to my rights under the Fair Debt Collection Practices Act, 15 U.S.C. \u00a7 1692c(c), I am directing you to cease all further communication with me regarding this or any other alleged debt.

Effective immediately, I demand that you:

1. Stop all telephone calls to me, my family members, and my place of employment
2. Stop all written correspondence except as specifically permitted under 15 U.S.C. \u00a7 1692c(c)
3. Stop all contact with third parties regarding this alleged debt
4. Do not sell, transfer, or assign this account to any other entity without notifying me in writing

Under the FDCPA, after receiving this letter you may only contact me to:
- Confirm that you are ceasing collection efforts, or
- Notify me of a specific legal action you intend to take

Any communication beyond these exceptions will constitute a violation of federal law, for which I may seek statutory damages of up to $1,000 per violation, plus actual damages and attorney fees.

This letter does not constitute an acknowledgment that I owe this debt."""

    elif letter_type == "dispute_amount":
        reason_text = f"\n\nSpecifically, I dispute this amount because: {dispute_reason}" if dispute_reason else ""
        body = f"""
I am writing regarding the above-referenced account, on which you claim a balance of ${amount}. I dispute the accuracy of this amount.{reason_text}

Pursuant to my rights under the Fair Debt Collection Practices Act, 15 U.S.C. \u00a7 1692g, I am requesting that you provide a complete and itemized accounting of the amount you claim I owe, including:

1. The original principal balance of the debt
2. An itemized list of all interest charges, with the interest rate applied and the legal authority for charging interest
3. An itemized list of all fees and penalties, with the legal or contractual basis for each
4. A record of all payments received and credited to this account
5. The total balance after accounting for all of the above

Additionally, please provide:
- A copy of the original agreement or contract authorizing these charges
- Proof that the interest rate and fees comply with applicable state law
- Documentation of any insurance payments or adjustments applied to this account

Until you provide this itemized accounting, I dispute the entire amount claimed and demand that you:
- Cease all collection activity on this account
- Report this debt as disputed to all consumer reporting agencies

Any attempt to collect an inaccurate amount may constitute a violation of the FDCPA and applicable state consumer protection laws.

This letter is not an acknowledgment that I owe this debt or any specific amount."""

    letter = header + body + f"""

Sincerely,

{user_name}

Sent via USPS Certified Mail"""

    return {
        "status": "ok",
        "letter_type": letter_type,
        "letter_type_name": LETTER_TYPES[letter_type]["name"],
        "letter_text": letter,
        "user_name": user_name,
        "user_address": user_address,
        "collector_name": collector_name,
        "collector_address": collector_address,
        "account_number": account_number,
        "amount": amount,
        "disclaimer": LEGAL_DISCLAIMER,
        "what_happens_next": LETTER_TYPES[letter_type]["what_happens"],
        "timeline": LETTER_TYPES[letter_type]["timeline"],
    }


# ── Charity care ─────────────────────────────────────────────────────────────

def get_fpl(household_size: int) -> int:
    """Return Federal Poverty Level for a given household size."""
    if household_size <= 0:
        return FPL_2025[1]
    if household_size <= 8:
        return FPL_2025[household_size]
    return FPL_2025[8] + FPL_PER_ADDITIONAL * (household_size - 8)


def check_charity_care(income: float, household_size: int) -> dict:
    """Check likely charity care eligibility based on FPL."""
    fpl = get_fpl(household_size)
    fpl_pct = round(income / fpl * 100)

    if fpl_pct <= 200:
        eligibility = "likely_full"
        message = (
            f"At {fpl_pct}% of the Federal Poverty Level, you likely qualify for "
            "full forgiveness of your hospital bill at most nonprofit hospitals."
        )
    elif fpl_pct <= 300:
        eligibility = "likely_partial"
        message = (
            f"At {fpl_pct}% of the Federal Poverty Level, you likely qualify for "
            "a significant discount (50-75%) at most nonprofit hospitals."
        )
    elif fpl_pct <= 400:
        eligibility = "possible_partial"
        message = (
            f"At {fpl_pct}% of the Federal Poverty Level, you may qualify for "
            "a partial discount (25-50%) at many nonprofit hospitals."
        )
    else:
        eligibility = "unlikely"
        message = (
            f"At {fpl_pct}% of the Federal Poverty Level, you are above the typical "
            "charity care threshold. However, some hospitals have higher limits — "
            "it is still worth applying."
        )

    return {
        "status": "ok",
        "income": income,
        "household_size": household_size,
        "fpl": fpl,
        "fpl_percentage": fpl_pct,
        "eligibility": eligibility,
        "message": message,
        "disclaimer": LEGAL_DISCLAIMER,
        "next_steps": CHARITY_CARE_PROCESS,
        "documents_needed": CHARITY_CARE_DOCUMENTS,
    }


def search_hospitals_for_charity(db, query: str, state: str = "") -> list:
    """Search hospitals by name, return charity care info.

    Queries the hospital_directory + hospital_financials tables.
    """
    query = _sanitize_text(query)
    if len(query) < 2:
        return []

    sql = """
        SELECT
            hd.facility_id, hd.name, hd.city, hd.state, hd.ownership,
            h.is_nonprofit, h.slug, h.state_slug,
            hf.nonprofit_status, hf.charity_care_amount, hf.charity_care_pct,
            hf.has_financial_assistance, hf.has_financial_assistance_policy,
            hf.financial_assistance_url, hf.fa_income_threshold,
            hf.fa_application_url
        FROM hospital_directory hd
        LEFT JOIN hospitals h ON hd.facility_id = h.facility_id
        LEFT JOIN hospital_financials hf ON hd.facility_id = hf.facility_id
        WHERE hd.name LIKE ?
    """
    params = [f"%{query}%"]

    if state:
        sql += " AND hd.state = ?"
        params.append(state.upper().strip())

    sql += " ORDER BY hd.name LIMIT 20"

    rows = db.execute(sql, params).fetchall()
    results = []
    for r in rows:
        is_np = bool(r["is_nonprofit"] or r["nonprofit_status"])
        results.append({
            "facility_id": r["facility_id"],
            "name": r["name"],
            "city": r["city"],
            "state": r["state"],
            "ownership": r["ownership"],
            "is_nonprofit": is_np,
            "slug": r["slug"],
            "state_slug": r["state_slug"],
            "charity_care_amount": r["charity_care_amount"],
            "charity_care_pct": r["charity_care_pct"],
            "has_financial_assistance": bool(r["has_financial_assistance"] or r["has_financial_assistance_policy"]),
            "financial_assistance_url": r["financial_assistance_url"] or "",
            "fa_income_threshold": r["fa_income_threshold"] or "",
            "fa_application_url": r["fa_application_url"] or "",
        })

    return results


def get_hospital_charity_detail(db, facility_id: str) -> dict | None:
    """Get detailed charity care info for a specific hospital."""
    facility_id = _sanitize_text(facility_id)
    row = db.execute("""
        SELECT
            hd.facility_id, hd.name, hd.address, hd.city, hd.state, hd.zip,
            hd.phone, hd.ownership,
            h.is_nonprofit, h.slug, h.state_slug,
            hf.nonprofit_status, hf.total_revenue, hf.charity_care_amount,
            hf.charity_care_pct, hf.charity_care_pct_revenue,
            hf.has_financial_assistance, hf.has_financial_assistance_policy,
            hf.financial_assistance_url, hf.fa_income_threshold,
            hf.fa_application_url, hf.irs_990_url
        FROM hospital_directory hd
        LEFT JOIN hospitals h ON hd.facility_id = h.facility_id
        LEFT JOIN hospital_financials hf ON hd.facility_id = hf.facility_id
        WHERE hd.facility_id = ?
    """, (facility_id,)).fetchone()

    if not row:
        return None

    is_np = bool(row["is_nonprofit"] or row["nonprofit_status"])

    result = {
        "facility_id": row["facility_id"],
        "name": row["name"],
        "address": row["address"],
        "city": row["city"],
        "state": row["state"],
        "zip": row["zip"],
        "phone": row["phone"],
        "ownership": row["ownership"],
        "is_nonprofit": is_np,
        "slug": row["slug"],
        "state_slug": row["state_slug"],
        "charity_care_amount": row["charity_care_amount"],
        "charity_care_pct": row["charity_care_pct"],
        "charity_care_pct_revenue": row["charity_care_pct_revenue"],
        "has_financial_assistance": bool(row["has_financial_assistance"] or row["has_financial_assistance_policy"]),
        "financial_assistance_url": row["financial_assistance_url"] or "",
        "fa_income_threshold": row["fa_income_threshold"] or "",
        "fa_application_url": row["fa_application_url"] or "",
        "irs_990_url": row["irs_990_url"] or "",
    }

    # Build hospital-specific guidance
    if is_np:
        result["charity_care_status"] = "nonprofit"
        result["charity_care_message"] = (
            f"{row['name']} is a nonprofit hospital. Under IRS Section 501(r), "
            "they are required to have a Financial Assistance Program and must "
            "consider your application."
        )
    else:
        result["charity_care_status"] = "for_profit"
        result["charity_care_message"] = (
            f"{row['name']} appears to be a for-profit hospital. For-profit hospitals "
            "are not required by the IRS to offer charity care, but many still have "
            "financial assistance programs. It is worth asking."
        )

    if result["fa_income_threshold"]:
        result["charity_care_message"] += (
            f" Their reported income threshold for assistance: {result['fa_income_threshold']}."
        )

    return result


def generate_charity_care_letter(
    user_name: str,
    user_address: str,
    hospital_name: str,
    hospital_address: str,
    account_number: str,
    bill_amount: str,
    income: float,
    household_size: int,
    date_of_service: str = "",
) -> dict:
    """Generate a financial assistance application cover letter."""
    user_name = _sanitize_text(user_name)
    user_address = _sanitize_text(user_address)
    hospital_name = _sanitize_text(hospital_name)
    hospital_address = _sanitize_text(hospital_address)
    account_number = _sanitize_text(account_number)
    bill_amount = _validate_amount(bill_amount)
    date_of_service = _sanitize_text(date_of_service) if date_of_service else ""

    fpl = get_fpl(household_size)
    fpl_pct = round(income / fpl * 100)
    today_str = date.today().strftime("%B %d, %Y")
    service_ref = f" for services on {date_of_service}" if date_of_service else ""

    letter = f"""{user_name}
{user_address}

{today_str}

{hospital_name}
Financial Assistance / Patient Financial Services
{hospital_address}

Re: Financial Assistance Application — Account #{account_number}

Dear Financial Assistance Department:

I am writing to request consideration under your hospital's Financial Assistance Program (FAP) for the balance of ${bill_amount} on the above-referenced account{service_ref}.

My household consists of {household_size} person{"s" if household_size > 1 else ""} with an annual household income of ${income:,.0f}. This represents approximately {fpl_pct}% of the 2025 Federal Poverty Level for my household size.

I am unable to pay this bill in full and respectfully request that you review my application for financial assistance under your hospital's policy, as required by IRS Section 501(r) for tax-exempt hospitals.

Enclosed please find:
- Completed Financial Assistance Application (if provided separately by your hospital)
- Proof of income (most recent tax return / pay stubs)
- Proof of household size

I request that all collection activity on this account be suspended while my application is under review, as required by federal guidelines for 501(r)-compliant hospitals.

Please contact me at the address above if you require any additional documentation. I appreciate your consideration.

Sincerely,

{user_name}

Enclosures: Financial documents as listed above
Sent via USPS Certified Mail"""

    return {
        "status": "ok",
        "letter_text": letter,
        "user_name": user_name,
        "hospital_name": hospital_name,
        "account_number": account_number,
        "bill_amount": bill_amount,
        "fpl_percentage": fpl_pct,
        "disclaimer": LEGAL_DISCLAIMER,
    }


# ── Lob certified mail ───────────────────────────────────────────────────────

LOB_API = "https://api.lob.com/v1"


def _parse_address_for_lob(full_address: str) -> dict:
    """Best-effort parse of 'Street, City, ST 12345' into Lob address fields."""
    parts = [p.strip() for p in full_address.split(",")]
    result = {"address_line1": full_address, "address_city": "", "address_state": "", "address_zip": "", "address_country": "US"}
    if len(parts) >= 3:
        result["address_line1"] = parts[0]
        result["address_city"] = parts[-2].strip() if len(parts) >= 3 else ""
        # Last part typically "ST 12345"
        last = parts[-1].strip().split()
        if len(last) == 2 and len(last[0]) == 2:
            result["address_state"] = last[0]
            result["address_zip"] = last[1]
        elif len(last) >= 1:
            result["address_state"] = last[0]
    return result


def send_via_lob(db, debt_letter_id: int, api_key: str) -> dict:
    """Send a debt letter via Lob certified mail.

    Returns dict with lob_id, tracking_number, expected_delivery_date.
    Raises RuntimeError on failure.
    """
    row = db.execute("SELECT * FROM debt_letters WHERE id = ?", (debt_letter_id,)).fetchone()
    if not row:
        raise ValueError(f"Letter {debt_letter_id} not found")
    if row["status"] == "sent":
        return {"lob_id": row["lob_id"], "tracking_number": row["tracking_number"], "already_sent": True}

    user_name = row["user_name"] or ""
    user_address = row["user_address"] or ""
    collector_name = row["collector_name"] or ""
    collector_address = row["collector_address"] or ""

    # Build simple HTML version of the letter for Lob
    letter_html = _letter_text_to_lob_html(row["letter_text"] or "")

    from_addr = _parse_address_for_lob(user_address)
    to_addr = _parse_address_for_lob(collector_address)

    # Build multipart form data for Lob /v1/letters
    params = {
        "description": f"FDCPA Letter - {row['letter_type']}",
        "to[name]": collector_name,
        "to[address_line1]": to_addr["address_line1"],
        "to[address_city]": to_addr["address_city"],
        "to[address_state]": to_addr["address_state"],
        "to[address_zip]": to_addr["address_zip"],
        "to[address_country]": "US",
        "from[name]": user_name,
        "from[address_line1]": from_addr["address_line1"],
        "from[address_city]": from_addr["address_city"],
        "from[address_state]": from_addr["address_state"],
        "from[address_zip]": from_addr["address_zip"],
        "from[address_country]": "US",
        "file": letter_html,
        "color": "false",
        "double_sided": "false",
        "extra_service": "certified",
    }

    body = urllib.parse.urlencode(params).encode()
    credentials = urllib.parse.quote(api_key) + ":"
    import base64
    auth_header = "Basic " + base64.b64encode(credentials.encode()).decode()

    req = urllib.request.Request(
        f"{LOB_API}/letters",
        data=body,
        headers={
            "Authorization": auth_header,
            "Content-Type": "application/x-www-form-urlencoded",
        },
        method="POST",
    )

    try:
        with urllib.request.urlopen(req, timeout=30) as resp:
            result = json.loads(resp.read())
    except urllib.error.HTTPError as e:
        body_text = e.read().decode(errors="replace")
        log.error("Lob error %s: %s", e.code, body_text)
        raise RuntimeError(f"Lob error {e.code}: {body_text}") from e

    lob_id = result.get("id", "")
    tracking_number = result.get("tracking_number", "")
    expected_delivery = result.get("expected_delivery_date", "")

    db.execute(
        "UPDATE debt_letters SET lob_id = ?, tracking_number = ?, status = 'sent', sent_at = CURRENT_TIMESTAMP WHERE id = ?",
        (lob_id, tracking_number, debt_letter_id),
    )

    return {"lob_id": lob_id, "tracking_number": tracking_number, "expected_delivery_date": expected_delivery}


def _letter_text_to_lob_html(text: str) -> str:
    """Convert plain-text letter to minimal HTML for Lob submission."""
    escaped = text.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
    paragraphs = escaped.replace("\n\n", "</p><p>").replace("\n", "<br>")
    return (
        "<!DOCTYPE html><html><head><meta charset='utf-8'>"
        "<style>body{font-family:Times New Roman,serif;font-size:12pt;line-height:1.6;margin:0;}"
        "p{margin:0 0 12pt 0;}</style></head>"
        f"<body><p>{paragraphs}</p></body></html>"
    )


# ── Settlement letter ────────────────────────────────────────────────────────

def generate_settlement_letter(
    user_name: str,
    user_address: str,
    collector_name: str,
    collector_address: str,
    account_number: str,
    original_amount: str,
    offer_amount: str,
) -> dict:
    """Generate a 'pay for delete' settlement offer letter."""
    user_name = _sanitize_text(user_name)
    user_address = _sanitize_text(user_address)
    collector_name = _sanitize_text(collector_name)
    collector_address = _sanitize_text(collector_address)
    account_number = _sanitize_text(account_number)
    original_amount = _validate_amount(original_amount)
    offer_amount = _validate_amount(offer_amount)

    today_str = date.today().strftime("%B %d, %Y")

    letter = f"""{user_name}
{user_address}

{today_str}

{collector_name}
{collector_address}

Re: Account #{account_number} — Settlement Offer

Dear Sir or Madam:

I am writing regarding the above-referenced account, on which you claim a balance of ${original_amount}. This letter is not an acknowledgment that this debt is valid or that I am legally obligated to pay it.

I am prepared to offer a one-time lump-sum payment of ${offer_amount} as full and final settlement of this account, subject to the following conditions:

1. You agree that the payment of ${offer_amount} constitutes payment in full and final settlement of the entire balance claimed on this account.

2. Within 30 days of receiving payment, you will request deletion of all tradelines associated with this account from Equifax, Experian, and TransUnion.

3. You will not sell, transfer, or assign any remaining balance to another entity.

4. You will send me written confirmation of this agreement before I remit payment.

If these terms are acceptable, please send a written agreement on your company letterhead to the address above. I will remit payment within 10 business days of receiving your written confirmation.

Do not contact me by telephone regarding this matter. All communication must be in writing.

This offer expires 30 days from the date of this letter.

Sincerely,

{user_name}"""

    return {
        "status": "ok",
        "letter_text": letter,
        "user_name": user_name,
        "collector_name": collector_name,
        "account_number": account_number,
        "original_amount": original_amount,
        "offer_amount": offer_amount,
        "disclaimer": LEGAL_DISCLAIMER,
        "warnings": [
            "Do NOT send payment until you have written confirmation of the agreement.",
            "Making any payment may reset the statute of limitations in your state. Check the SOL calculator first.",
            "'Pay for delete' is not guaranteed enforceable. Some collectors will agree, others will not.",
        ],
    }
