"""State medical billing rights data for the /rights/ hub."""

from __future__ import annotations

# SOL data from tools_engine — kept in sync
STATE_SOL_YEARS = {
    "AL": 6, "AK": 3, "AZ": 6, "AR": 5, "CA": 4, "CO": 6, "CT": 6, "DE": 3,
    "FL": 5, "GA": 6, "HI": 6, "ID": 5, "IL": 5, "IN": 6, "IA": 10, "KS": 5,
    "KY": 5, "LA": 3, "ME": 6, "MD": 3, "MA": 6, "MI": 6, "MN": 6, "MS": 3,
    "MO": 10, "MT": 8, "NE": 5, "NV": 6, "NH": 3, "NJ": 6, "NM": 6, "NY": 6,
    "NC": 3, "ND": 6, "OH": 6, "OK": 5, "OR": 6, "PA": 4, "RI": 10, "SC": 3,
    "SD": 6, "TN": 6, "TX": 4, "UT": 6, "VT": 6, "VA": 5, "WA": 6, "WV": 5,
    "WI": 6, "WY": 10,
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
    "WI": "Wisconsin", "WY": "Wyoming",
}

# Balance billing protections beyond federal No Surprises Act
BALANCE_BILLING_LAWS = {
    "CA": "Comprehensive. AB 72 prohibits balance billing for emergency and certain non-emergency services at in-network facilities.",
    "CO": "Strong. Prohibits balance billing for emergency services and at in-network facilities.",
    "CT": "Strong. Patients pay only in-network cost-sharing for surprise out-of-network bills.",
    "FL": "Moderate. HB 221 protects against balance billing in emergencies and at in-network facilities.",
    "GA": "Moderate. Surprise Billing Consumer Protection Act covers emergency and certain non-emergency services.",
    "IL": "Strong. Patients cannot be balance billed for emergency services or at in-network facilities.",
    "MD": "Strong. Patients pay only in-network rates for surprise out-of-network bills.",
    "MI": "Limited. Relies primarily on federal No Surprises Act protections.",
    "MN": "Moderate. Protects patients from surprise bills in emergency and some non-emergency settings.",
    "NJ": "Strong. Out-of-network providers at in-network facilities must accept in-network payment.",
    "NY": "Comprehensive. Surprise Bill Law protects against emergency and in-network facility surprise bills since 2015.",
    "NC": "Limited. Relies primarily on federal No Surprises Act protections.",
    "OH": "Limited. HB 388 provides some surprise billing protections; relies heavily on federal law.",
    "OR": "Strong. Patients only responsible for in-network cost-sharing for surprise bills.",
    "PA": "Moderate. Act 112 prohibits balance billing for emergency and certain surgical services.",
    "TX": "Strong. SB 1264 prohibits balance billing for emergency and certain facility-based services.",
    "VA": "Moderate. Balance billing protections for emergency services and at in-network facilities.",
    "WA": "Comprehensive. Balance Billing Protection Act covers emergency and non-emergency surprise bills.",
}

# Charity care highlights (state-specific requirements beyond federal 501(r))
CHARITY_CARE_LAWS = {
    "CA": "Hospitals must offer charity care to patients under 400% FPL. No collection actions until eligibility is determined. AB 774.",
    "CT": "Bed tax-funded charity care. Hospitals must screen all uninsured patients for eligibility.",
    "IL": "Hospital Uninsured Patient Discount Act requires discounts for uninsured patients under 600% FPL at nonprofit hospitals.",
    "MD": "Unique all-payer rate setting system. Hospitals must provide free care to patients under 200% FPL.",
    "NJ": "Charity Care Act requires all hospitals (including for-profit) to provide charity care. Funded by state pool.",
    "NY": "Financial assistance required for uninsured patients under 300% FPL. Hospitals cannot charge uninsured more than lowest negotiated rate.",
    "OR": "ORS 442.614 requires charity care policies. Hospitals cannot charge uninsured more than the amount typically paid by insured patients.",
    "PA": "Act 106 allows hospitals participating in Tobacco Settlement Fund to provide charity care.",
    "TX": "Nonprofit hospitals must adopt charity care policies as condition of tax exemption. No state minimum requirements beyond federal.",
    "WA": "Charity care required for patients under 300% FPL. RCW 70.170 mandates reporting and eligibility screening.",
}

# Collection-specific protections
COLLECTION_PROTECTIONS = {
    "CA": "Medical debt cannot appear on credit reports for 12 months after date of service. Hospitals must wait 150 days before sending to collections.",
    "CO": "Hospitals cannot send to collections within 60 days of first bill. Must provide notice of financial assistance options.",
    "CT": "Nonprofit hospitals cannot sue patients under 250% FPL. Must screen for charity care before pursuing collections.",
    "IL": "Collection agencies must provide written notice of charity care availability within 30 days of first contact.",
    "MD": "Hospitals must wait 45 days after billing before pursuing collections. Must notify patients of financial assistance.",
    "MN": "Hospitals must notify patients of financial assistance and provide 120 days to apply before pursuing collection.",
    "NJ": "All hospitals must screen for charity care before pursuing collections. 4-year collection statute for hospital bills.",
    "NY": "Hospitals cannot report to credit agencies or pursue collections for patients under 400% FPL until financial assistance is determined. Must offer interest-free payment plans.",
    "NC": "Nonprofit hospitals must wait 240 days before extraordinary collection actions. Must make reasonable efforts to determine financial assistance eligibility.",
    "OR": "Hospitals must screen for financial assistance before pursuing collection actions. Cannot charge interest above 9%.",
    "TX": "No specific state delay beyond federal protections, but nonprofit hospitals must demonstrate charity care efforts for tax exemption.",
    "WA": "Hospitals must screen for charity care eligibility before pursuing extraordinary collection actions. Must offer payment plans.",
}


def get_all_states() -> list[dict]:
    """Return all states with basic rights data, sorted by name."""
    states = []
    for code, name in sorted(STATE_NAMES.items(), key=lambda x: x[1]):
        states.append({
            "code": code,
            "name": name,
            "slug": name.lower().replace(" ", "-"),
            "sol_years": STATE_SOL_YEARS.get(code, 6),
            "has_balance_billing_law": code in BALANCE_BILLING_LAWS,
            "has_charity_care_law": code in CHARITY_CARE_LAWS,
            "has_collection_protections": code in COLLECTION_PROTECTIONS,
        })
    return states


def get_state_rights(slug: str) -> dict | None:
    """Return full rights data for a single state by slug."""
    # Find state by slug
    code = None
    for c, name in STATE_NAMES.items():
        if name.lower().replace(" ", "-") == slug.lower():
            code = c
            break
    if not code:
        return None

    name = STATE_NAMES[code]
    sol = STATE_SOL_YEARS.get(code, 6)

    # Federal rights apply everywhere
    federal_rights = [
        "No Surprises Act protects against balance billing for emergency services and at in-network facilities.",
        "Medical debt under $500 cannot appear on credit reports (effective 2023).",
        "Medical debt cannot appear on credit reports until at least 12 months after date of service.",
        "Paid medical debt is removed from credit reports.",
        "FDCPA protects against abusive debt collection practices. You can demand debt validation within 30 days.",
        "IRS 501(r) requires nonprofit hospitals to offer financial assistance policies.",
        "Hospitals must provide a Good Faith Estimate to uninsured/self-pay patients before scheduled services.",
    ]

    state_rights = []
    if code in BALANCE_BILLING_LAWS:
        state_rights.append(BALANCE_BILLING_LAWS[code])
    if code in CHARITY_CARE_LAWS:
        state_rights.append(CHARITY_CARE_LAWS[code])
    if code in COLLECTION_PROTECTIONS:
        state_rights.append(COLLECTION_PROTECTIONS[code])

    return {
        "code": code,
        "name": name,
        "slug": slug,
        "sol_years": sol,
        "federal_rights": federal_rights,
        "state_rights": state_rights,
        "balance_billing": BALANCE_BILLING_LAWS.get(code),
        "charity_care": CHARITY_CARE_LAWS.get(code),
        "collection_protections": COLLECTION_PROTECTIONS.get(code),
    }
