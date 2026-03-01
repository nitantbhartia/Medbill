"""Medical billing glossary — 100+ terms for SEO and user education."""

from __future__ import annotations

TERMS: list[dict] = [
    # --- Core Billing ---
    {"term": "CPT Code", "slug": "cpt-code", "category": "Billing Basics",
     "definition": "Current Procedural Terminology code. A 5-digit number assigned to every medical service or procedure. Used by providers and insurers to standardize billing. Example: 99213 = standard office visit.",
     "cta_url": "/tools/cpt-code-lookup/", "cta_label": "Look up a CPT code"},
    {"term": "ICD-10 Code", "slug": "icd-10-code", "category": "Billing Basics",
     "definition": "International Classification of Diseases, 10th revision. A diagnosis code that tells the insurer why a service was performed. Each claim must have at least one ICD-10 code that supports the CPT code billed.",
     "cta_url": "/guides/icd10-drg-codes-explained", "cta_label": "Learn about ICD-10 codes"},
    {"term": "DRG", "slug": "drg", "category": "Billing Basics",
     "definition": "Diagnosis-Related Group. A classification system that groups hospital inpatient stays into categories for payment purposes. Medicare pays a fixed amount per DRG regardless of how long you stay or how many tests you get.",
     "cta_url": "/guides/icd10-drg-codes-explained", "cta_label": "Learn about DRG codes"},
    {"term": "Chargemaster", "slug": "chargemaster", "category": "Billing Basics",
     "definition": "A hospital&rsquo;s master list of prices for every service, procedure, supply, and drug. Chargemaster prices are typically 3&ndash;10x higher than what insurers actually pay. This is the starting price before any negotiation or discount.",
     "cta_url": "/hospitals/", "cta_label": "Check hospital pricing"},
    {"term": "Itemized Bill", "slug": "itemized-bill", "category": "Billing Basics",
     "definition": "A detailed statement listing every individual charge on your bill with CPT codes, descriptions, quantities, and prices. You have the right to request one. This is the document you need to dispute billing errors.",
     "cta_url": "/guides/how-to-get-an-itemized-hospital-bill", "cta_label": "How to get an itemized bill"},
    {"term": "Superbill", "slug": "superbill", "category": "Billing Basics",
     "definition": "A detailed receipt from a healthcare provider listing services, CPT codes, ICD-10 diagnoses, and charges. Commonly given by outpatient providers so patients can submit claims to insurance for reimbursement.",
     "cta_url": "/guides/what-is-a-superbill", "cta_label": "Superbill guide"},
    {"term": "UB-04", "slug": "ub-04", "category": "Billing Basics",
     "definition": "The standard claim form used by hospitals and institutional providers to bill insurance. Contains all charges, diagnosis codes, procedure codes, and provider information for an inpatient or outpatient visit."},
    {"term": "Revenue Code", "slug": "revenue-code", "category": "Billing Basics",
     "definition": "A 4-digit code on hospital bills that categorizes the type of service or department (e.g., 0250 = pharmacy, 0450 = emergency room). Used alongside CPT codes on institutional claims."},

    # --- Insurance ---
    {"term": "EOB", "slug": "eob", "category": "Insurance",
     "definition": "Explanation of Benefits. A statement from your insurer showing what was billed, what they paid, and what you owe. This is NOT a bill &mdash; it&rsquo;s a summary of how your claim was processed. Compare it to your actual bill.",
     "cta_url": "/tools/eob-decoder/", "cta_label": "Decode your EOB"},
    {"term": "Deductible", "slug": "deductible", "category": "Insurance",
     "definition": "The amount you must pay out-of-pocket before your insurance starts paying. If your deductible is $2,000, you pay the first $2,000 of covered services each year. After that, insurance kicks in.",
     "cta_url": "/guides/copay-vs-coinsurance-vs-deductible", "cta_label": "Deductible vs copay guide"},
    {"term": "Copay", "slug": "copay", "category": "Insurance",
     "definition": "A fixed dollar amount you pay for a covered service. Example: $30 for an office visit, $100 for an ER visit. Copays do not count toward your deductible in most plans.",
     "cta_url": "/guides/copay-vs-coinsurance-vs-deductible", "cta_label": "Copay vs coinsurance guide"},
    {"term": "Coinsurance", "slug": "coinsurance", "category": "Insurance",
     "definition": "The percentage of costs you pay after meeting your deductible. If your coinsurance is 20%, you pay 20% and insurance pays 80%. This continues until you hit your out-of-pocket maximum.",
     "cta_url": "/guides/copay-vs-coinsurance-vs-deductible", "cta_label": "Understand coinsurance"},
    {"term": "Out-of-Pocket Maximum", "slug": "out-of-pocket-maximum", "category": "Insurance",
     "definition": "The most you have to pay for covered services in a plan year. After you reach this amount, your insurance pays 100%. Includes deductibles, copays, and coinsurance. Does NOT include premiums or out-of-network charges.",
     "cta_url": "/guides/out-of-pocket-maximum-explained", "cta_label": "OOP max guide"},
    {"term": "Prior Authorization", "slug": "prior-authorization", "category": "Insurance",
     "definition": "Approval from your insurance company before getting a service. Required for many surgeries, imaging, and specialty drugs. If you skip it, the claim may be denied and you could owe the full amount.",
     "cta_url": "/guides/prior-authorization-explained", "cta_label": "Prior auth guide"},
    {"term": "Allowed Amount", "slug": "allowed-amount", "category": "Insurance",
     "definition": "The maximum amount your insurance will pay for a covered service. Also called &ldquo;eligible amount&rdquo; or &ldquo;negotiated rate.&rdquo; If the provider charges more, you may owe the difference (balance billing) unless protections apply."},
    {"term": "In-Network", "slug": "in-network", "category": "Insurance",
     "definition": "A provider or facility that has a contract with your insurance company to accept negotiated rates. In-network care costs significantly less than out-of-network care. Always verify network status before non-emergency services."},
    {"term": "Out-of-Network", "slug": "out-of-network", "category": "Insurance",
     "definition": "A provider or facility with no contract with your insurer. You may owe the full charge or a much higher cost-sharing amount. The No Surprises Act protects you from surprise out-of-network bills in certain situations.",
     "cta_url": "/tools/surprise-bill-checker/", "cta_label": "Check surprise bill protections"},
    {"term": "Claim Denial", "slug": "claim-denial", "category": "Insurance",
     "definition": "When your insurance company refuses to pay for a service. Common reasons: no prior authorization, service not medically necessary, coding errors. You have the right to appeal every denial.",
     "cta_url": "/tools/insurance-denial-appeal-letter-generator/", "cta_label": "Generate appeal letter"},
    {"term": "Coordination of Benefits", "slug": "coordination-of-benefits", "category": "Insurance",
     "definition": "Rules that determine which insurance plan pays first when you have more than one. The primary plan pays first, then the secondary plan covers remaining eligible costs. Errors here are a common cause of claim denials."},

    # --- Billing Errors ---
    {"term": "Upcoding", "slug": "upcoding", "category": "Billing Errors",
     "definition": "When a provider bills for a more expensive service than was actually performed. Example: billing a Level 5 ER visit (99285) when a Level 3 (99283) was appropriate. This is one of the most common billing errors.",
     "cta_url": "/scan", "cta_label": "Scan for upcoding"},
    {"term": "Unbundling", "slug": "unbundling", "category": "Billing Errors",
     "definition": "Billing individual components of a procedure separately instead of using a single comprehensive code. This inflates the total charge. NCCI edits define which codes should be bundled together.",
     "cta_url": "/scan", "cta_label": "Check for unbundling"},
    {"term": "Duplicate Charge", "slug": "duplicate-charge", "category": "Billing Errors",
     "definition": "Being billed twice for the same service on the same date. This can happen due to data entry errors, system glitches, or billing department mistakes. Always check your itemized bill for exact duplicate lines.",
     "cta_url": "/scan", "cta_label": "Scan for duplicates"},
    {"term": "Balance Billing", "slug": "balance-billing", "category": "Billing Errors",
     "definition": "When an out-of-network provider bills you for the difference between their charge and what insurance paid. The No Surprises Act prohibits this for emergency services and certain situations at in-network facilities.",
     "cta_url": "/tools/surprise-bill-checker/", "cta_label": "Check balance billing protections"},
    {"term": "Phantom Charges", "slug": "phantom-charges", "category": "Billing Errors",
     "definition": "Charges for services, supplies, or medications you never received. Examples: being charged for a private room when you had a shared room, or medications that were ordered but never administered.",
     "cta_url": "/scan", "cta_label": "Scan for phantom charges"},

    # --- Debt & Collections ---
    {"term": "FDCPA", "slug": "fdcpa", "category": "Debt & Collections",
     "definition": "Fair Debt Collection Practices Act. A federal law that limits what debt collectors can do. They cannot harass you, lie about the amount, or threaten actions they cannot legally take. You can demand debt validation within 30 days.",
     "cta_url": "/collection-notice", "cta_label": "Generate FDCPA letter"},
    {"term": "Debt Validation", "slug": "debt-validation", "category": "Debt & Collections",
     "definition": "Your legal right to demand proof that a debt collector owns your debt and the amount is correct. Under the FDCPA, you have 30 days from first contact to request this. Collectors must stop collection activity until they respond.",
     "cta_url": "/collection-notice", "cta_label": "Send validation letter"},
    {"term": "Statute of Limitations", "slug": "statute-of-limitations", "category": "Debt & Collections",
     "definition": "The time period during which a creditor can sue you to collect a debt. Varies by state from 3 to 10 years for medical debt. After it expires, collectors can still contact you but generally cannot file a lawsuit.",
     "cta_url": "/statute-of-limitations", "cta_label": "Check your state&rsquo;s SOL"},
    {"term": "Charity Care", "slug": "charity-care", "category": "Debt & Collections",
     "definition": "Financial assistance programs at nonprofit hospitals. Under IRS 501(r), nonprofit hospitals must have a Financial Assistance Policy and offer free or discounted care to patients who qualify based on income. You can apply retroactively.",
     "cta_url": "/charity-care", "cta_label": "Check eligibility"},
    {"term": "Financial Assistance Policy (FAP)", "slug": "financial-assistance-policy", "category": "Debt & Collections",
     "definition": "A written policy that nonprofit hospitals are required to maintain under IRS 501(r). It must specify income thresholds for free and discounted care, and hospitals must make reasonable efforts to inform patients before pursuing collection.",
     "cta_url": "/charity-care", "cta_label": "Find your hospital&rsquo;s FAP"},
    {"term": "Extraordinary Collection Actions", "slug": "extraordinary-collection-actions", "category": "Debt & Collections",
     "definition": "Aggressive collection tactics like lawsuits, wage garnishment, liens, and credit reporting. Under IRS 501(r), nonprofit hospitals cannot take these actions until they have made reasonable efforts to determine financial assistance eligibility."},
    {"term": "Pay for Delete", "slug": "pay-for-delete", "category": "Debt & Collections",
     "definition": "A negotiation strategy where you offer to pay a debt (often at a discount) in exchange for the collector removing the account from your credit report. Not guaranteed to work, but commonly attempted for medical debt.",
     "cta_url": "/settle-debt", "cta_label": "Generate settlement offer"},

    # --- Pricing & Benchmarks ---
    {"term": "Medicare Rate", "slug": "medicare-rate", "category": "Pricing",
     "definition": "The amount Medicare pays for a specific service. Determined by CMS based on the Physician Fee Schedule or OPPS. Often used as a benchmark for &ldquo;fair pricing&rdquo; because it reflects the actual cost of care plus a reasonable margin.",
     "cta_url": "/tools/medicare-rate-lookup/", "cta_label": "Look up Medicare rate"},
    {"term": "Markup Ratio", "slug": "markup-ratio", "category": "Pricing",
     "definition": "How much a hospital charges compared to Medicare. A 3.5x markup means the hospital charges 3.5 times what Medicare pays. The national average is about 3.4x. Hospitals with markups above 5x are considered predatory.",
     "cta_url": "/hospitals/", "cta_label": "Check hospital markup"},
    {"term": "Price Transparency", "slug": "price-transparency", "category": "Pricing",
     "definition": "Federal rule requiring hospitals to publicly post their prices for all services in machine-readable format. Since January 2021, hospitals must publish negotiated rates with each insurer. Compliance has been slow and enforcement weak.",
     "cta_url": "/guides/hospital-price-transparency-laws", "cta_label": "Price transparency guide"},
    {"term": "Good Faith Estimate", "slug": "good-faith-estimate", "category": "Pricing",
     "definition": "A written cost estimate that providers must give uninsured and self-pay patients before scheduled services. Required under the No Surprises Act. If the final bill exceeds the estimate by $400+, you can dispute it.",
     "cta_url": "/tools/good-faith-estimate-calculator/", "cta_label": "Good faith estimate tool"},
    {"term": "Facility Fee", "slug": "facility-fee", "category": "Pricing",
     "definition": "A separate charge for using a hospital or outpatient facility, on top of the doctor&rsquo;s professional fee. Hospital-owned clinics often charge facility fees that independent practices do not. This can add hundreds to thousands of dollars to your bill."},
    {"term": "Professional Fee", "slug": "professional-fee", "category": "Pricing",
     "definition": "The charge for the physician or provider&rsquo;s services, separate from any facility fee. On a hospital bill, you may receive separate bills from the hospital (facility fee) and the doctor (professional fee)."},

    # --- Laws & Protections ---
    {"term": "No Surprises Act", "slug": "no-surprises-act", "category": "Laws",
     "definition": "Federal law effective January 2022 that protects patients from surprise out-of-network bills for emergency services, air ambulance, and non-emergency services at in-network facilities by out-of-network providers.",
     "cta_url": "/guides/no-surprises-act-explained", "cta_label": "No Surprises Act guide"},
    {"term": "501(r)", "slug": "501r", "category": "Laws",
     "definition": "IRS section requiring tax-exempt (nonprofit) hospitals to maintain a Financial Assistance Policy, limit charges to insured rates for assistance-eligible patients, and make reasonable collection effort before taking extraordinary collection actions.",
     "cta_url": "/charity-care", "cta_label": "Check charity care eligibility"},
    {"term": "HIPAA", "slug": "hipaa", "category": "Laws",
     "definition": "Health Insurance Portability and Accountability Act. Primarily known for patient privacy protections. Relevant to billing because it governs how your medical and billing information can be shared, including with collection agencies."},
    {"term": "EMTALA", "slug": "emtala", "category": "Laws",
     "definition": "Emergency Medical Treatment and Labor Act. Requires hospitals with emergency departments to provide stabilizing treatment to anyone regardless of ability to pay. Does not regulate how much they can charge &mdash; only that they must treat you."},

    # --- Hospital Types ---
    {"term": "Nonprofit Hospital", "slug": "nonprofit-hospital", "category": "Hospital Types",
     "definition": "A hospital exempt from federal income tax under IRC 501(c)(3). Required to provide community benefits including charity care. Must comply with IRS 501(r) requirements. Despite the name, many nonprofits generate significant surplus revenue.",
     "cta_url": "/guides/for-profit-vs-nonprofit-hospital-billing", "cta_label": "Nonprofit vs for-profit guide"},
    {"term": "For-Profit Hospital", "slug": "for-profit-hospital", "category": "Hospital Types",
     "definition": "A hospital owned by private investors or publicly traded companies. Not required to offer charity care under federal law (though many states require it). Generally have higher markups than nonprofit hospitals.",
     "cta_url": "/guides/for-profit-vs-nonprofit-hospital-billing", "cta_label": "Compare hospital types"},
    {"term": "ASC", "slug": "asc", "category": "Hospital Types",
     "definition": "Ambulatory Surgery Center. An outpatient facility where surgeries and procedures are performed without overnight stays. Typically 40&ndash;60% cheaper than the same procedure at a hospital. A key option for price-conscious patients.",
     "cta_url": "/surgery-centers/", "cta_label": "Find surgery centers"},
    {"term": "Critical Access Hospital", "slug": "critical-access-hospital", "category": "Hospital Types",
     "definition": "A small rural hospital (25 beds or fewer) designated by CMS. Receives cost-based reimbursement from Medicare rather than fixed DRG payments. Often the only hospital within a large geographic area."},
]


def get_all_terms() -> list[dict]:
    """Return all glossary terms sorted alphabetically."""
    return sorted(TERMS, key=lambda t: t["term"].lower())


def get_terms_by_category() -> dict[str, list[dict]]:
    """Return terms grouped by category."""
    cats: dict[str, list[dict]] = {}
    for t in sorted(TERMS, key=lambda t: t["term"].lower()):
        cat = t["category"]
        if cat not in cats:
            cats[cat] = []
        cats[cat].append(t)
    return cats


def get_term(slug: str) -> dict | None:
    """Find a single term by slug."""
    for t in TERMS:
        if t["slug"] == slug:
            return t
    return None
