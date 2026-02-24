"""Medical debt fighting tools: SOL calculator, FDCPA letters, charity care, settlement offers."""
import logging
from datetime import date, timedelta

log = logging.getLogger(__name__)

# Statute of limitations by state (years). Source: state civil procedure codes.
# "partial_resets_sol" = making a partial payment restarts the clock.
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

# 2025 Federal Poverty Level guidelines (annual, for continental US)
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


def check_sol(state: str, start_date: str) -> dict:
    """Check statute of limitations for a medical debt.

    Args:
        state: Two-letter state code
        start_date: ISO date string (YYYY-MM-DD) of last payment or date of service
    """
    code = state.upper().strip()
    if code not in SOL_BY_STATE:
        return {"status": "error", "message": f"Unknown state: {state}"}

    try:
        dt = date.fromisoformat(start_date)
    except (ValueError, TypeError):
        return {"status": "error", "message": "Invalid date format. Use YYYY-MM-DD."}

    info = SOL_BY_STATE[code]
    sol_years = info["years"]
    expiry = date(dt.year + sol_years, dt.month, dt.day)
    today = date.today()
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


def generate_fdcpa_letter(
    user_name: str,
    user_address: str,
    collector_name: str,
    collector_address: str,
    account_number: str,
    amount: str,
    date_of_notice: str,
) -> dict:
    """Generate an FDCPA debt validation letter.

    The letter invokes 15 U.S.C. § 1692g(b) to dispute the debt
    and demand validation. It does NOT acknowledge the debt as valid.
    """
    today_str = date.today().strftime("%B %d, %Y")

    letter = f"""{user_name}
{user_address}

{today_str}

{collector_name}
{collector_address}

Re: Account #{account_number} — Amount Claimed: ${amount}

Dear Sir or Madam:

I am writing in response to your communication dated {date_of_notice} regarding the above-referenced account. I do not recognize this debt as valid.

Pursuant to my rights under the Fair Debt Collection Practices Act, 15 U.S.C. § 1692g(b), I am formally disputing this debt in its entirety and requesting that you provide the following validation:

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

This letter is not an acknowledgment that I owe this debt, nor a promise to pay. It is solely a request for validation as permitted by federal law.

Sincerely,

{user_name}

Sent via USPS Certified Mail"""

    return {
        "status": "ok",
        "letter_text": letter,
        "user_name": user_name,
        "collector_name": collector_name,
        "account_number": account_number,
        "amount": amount,
        "disclaimer": LEGAL_DISCLAIMER,
    }


def get_fpl(household_size: int) -> int:
    """Return Federal Poverty Level for a given household size."""
    if household_size <= 0:
        return FPL_2025[1]
    if household_size <= 8:
        return FPL_2025[household_size]
    return FPL_2025[8] + FPL_PER_ADDITIONAL * (household_size - 8)


def check_charity_care(income: float, household_size: int) -> dict:
    """Check likely charity care eligibility based on FPL.

    Most nonprofit hospitals offer:
    - Full write-off at 200% FPL or below
    - Partial discount (25-75%) at 200-400% FPL
    """
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
        discount_range = "50-75%"
        message = (
            f"At {fpl_pct}% of the Federal Poverty Level, you likely qualify for "
            f"a significant discount ({discount_range}) at most nonprofit hospitals."
        )
    elif fpl_pct <= 400:
        eligibility = "possible_partial"
        discount_range = "25-50%"
        message = (
            f"At {fpl_pct}% of the Federal Poverty Level, you may qualify for "
            f"a partial discount ({discount_range}) at many nonprofit hospitals."
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
        "next_steps": [
            "Ask the hospital for their Financial Assistance Application (they must provide one).",
            "Gather documents: most recent tax return and 2-3 recent pay stubs.",
            "Submit the application — hospitals must review all applications regardless of income.",
            "If denied, appeal. Many denials are reversed on appeal.",
        ],
    }


def generate_settlement_letter(
    user_name: str,
    user_address: str,
    collector_name: str,
    collector_address: str,
    account_number: str,
    original_amount: str,
    offer_amount: str,
) -> dict:
    """Generate a 'pay for delete' settlement offer letter.

    Does NOT acknowledge the debt as valid. Conditions payment on written
    confirmation of credit bureau deletion.
    """
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
