"""Programmatic state-level medical debt law guides.

One guide per state covering: statute of limitations, wage garnishment caps,
property exemptions, charity care requirements, and notable state laws.
"""
from guides import register

# (state_name, state_abbr, sol_years, sol_citation, wage_garn_pct, notable_law_summary, credit_rule)
_STATE_DATA = [
    ("California", "CA", 4, "Cal. Code Civ. Proc. § 337",
     "25% (or 25x state hourly min wage, whichever is less)",
     "SB 1061 (2024) prohibits medical debt from appearing on credit reports. Also strong Hospital Fair Pricing Act requires discounts for patients under 400% FPL.",
     "Medical debt is removed from credit reports under state law (SB 1061, 2024)."),
    ("Texas", "TX", 4, "Tex. Civ. Prac. & Rem. Code § 16.004",
     "Wage garnishment for medical debt is PROHIBITED (only child support, taxes, student loans)",
     "Texas has some of the strongest debtor protections in the US. Medical debt collectors cannot garnish wages at all. Homestead exemption is unlimited.",
     "Standard federal rules apply; state adds no extra credit protection."),
    ("New York", "NY", 3, "NY CPLR § 213-d (reduced from 6 years in 2022)",
     "10% of gross wages OR amount over 30x federal min wage",
     "Fair Medical Debt Reporting Act (2023) bans medical debt from credit reports. Hospital Financial Assistance Law requires nonprofit hospitals to have charity care programs for patients under 300% FPL.",
     "Medical debt cannot appear on credit reports (state law, 2023)."),
    ("Florida", "FL", 5, "Fla. Stat. § 95.11(2)(b)",
     "Wages of head of household are EXEMPT from garnishment if under $750/week",
     "Strong head-of-household exemption protects primary wage-earners from garnishment. Florida has no state income tax, but medical debt collectors actively pursue lawsuits.",
     "Standard federal rules apply."),
    ("Illinois", "IL", 10, "735 ILCS 5/13-206",
     "15% of gross wages or amount over 45x state min wage",
     "Illinois Hospital Uninsured Patient Discount Act requires hospitals to offer 25-65% discounts based on income. Medical Debt Relief Act (2024) limits reporting medical debt.",
     "Under IL law, medical debt is not reportable to credit bureaus for 1 year after billing."),
    ("Pennsylvania", "PA", 4, "42 Pa. C.S. § 5525",
     "Wage garnishment for consumer debt (including medical) is PROHIBITED",
     "Pennsylvania is one of only four states (plus NC, SC, TX) that prohibits wage garnishment for most consumer debts including medical bills.",
     "Standard federal rules apply."),
    ("Ohio", "OH", 6, "Ohio Rev. Code § 2305.06",
     "25% of disposable earnings (federal cap)",
     "Ohio has a consumer-friendly Ohio Consumer Sales Practices Act but medical debt collections are aggressive. Hospital charity care requirements are minimal.",
     "Standard federal rules apply."),
    ("Georgia", "GA", 6, "O.C.G.A. § 9-3-24",
     "25% of disposable earnings or amount over 30x federal min wage",
     "Georgia allows wage garnishment for consumer debt. No notable state medical debt protections beyond federal FDCPA.",
     "Standard federal rules apply."),
    ("North Carolina", "NC", 3, "N.C. Gen. Stat. § 1-52",
     "Wage garnishment for medical debt is PROHIBITED (only taxes, student loans, child support)",
     "North Carolina prohibits wage garnishment for medical and most consumer debt. Very short 3-year statute of limitations.",
     "Standard federal rules apply."),
    ("Michigan", "MI", 6, "MCL § 600.5807(8)",
     "25% of disposable earnings (federal cap)",
     "Michigan requires nonprofit hospitals to have financial assistance policies but enforcement is inconsistent. Debt collection is common.",
     "Standard federal rules apply."),
    ("New Jersey", "NJ", 6, "N.J.S.A. § 2A:14-1",
     "10% of gross wages if income above 250% of federal poverty level",
     "New Jersey Hospital Care Payment Assistance Program (Charity Care) provides free or reduced hospital care for uninsured patients under 300% FPL.",
     "Standard federal rules apply."),
    ("Virginia", "VA", 3, "Va. Code § 8.01-246(4)",
     "25% of disposable earnings (federal cap)",
     "Virginia has a short 3-year statute of limitations for oral or implied contracts. Written medical contracts have a 5-year SOL.",
     "Standard federal rules apply."),
    ("Washington", "WA", 6, "RCW § 4.16.040",
     "25% of disposable earnings or amount over 35x state min wage",
     "Washington Charity Care Act requires all hospitals to provide free care for patients under 300% FPL and discounts up to 400% FPL. Strong state enforcement.",
     "Standard federal rules apply."),
    ("Arizona", "AZ", 6, "A.R.S. § 12-548",
     "25% of disposable earnings (federal cap)",
     "Arizona has a 6-year statute of limitations for written contracts including medical bills. Standard consumer protections.",
     "Standard federal rules apply."),
    ("Massachusetts", "MA", 6, "M.G.L. c. 260 § 2",
     "15% of gross wages or amount over 50x federal min wage",
     "Massachusetts Health Safety Net program covers uninsured and underinsured patients. Hospital financial assistance is among the strongest in the US.",
     "Standard federal rules apply."),
    ("Tennessee", "TN", 6, "Tenn. Code Ann. § 28-3-109",
     "25% of disposable earnings (federal cap)",
     "Tennessee has no income tax and standard debt collection rules. Medical debt lawsuits are common; hospital charity care is minimal.",
     "Standard federal rules apply."),
    ("Indiana", "IN", 6, "Ind. Code § 34-11-2-9",
     "25% of disposable earnings (federal cap)",
     "Indiana standard 6-year SOL for written contracts. No notable state-specific medical debt protections.",
     "Standard federal rules apply."),
    ("Missouri", "MO", 10, "Mo. Rev. Stat. § 516.110",
     "25% of disposable earnings or amount over 30x federal min wage; head of household 10%",
     "Missouri has one of the longest statutes of limitations (10 years) for written contracts, making it especially important to verify debt age before paying.",
     "Standard federal rules apply."),
    ("Maryland", "MD", 3, "Md. Code, Cts. & Jud. Proc. § 5-101",
     "25% of disposable earnings or amount over 30x federal min wage",
     "Maryland Medical Debt Protection Act (2021) requires hospitals to provide financial assistance and prohibits aggressive collection practices.",
     "Medical debt cannot be reported to credit bureaus if under $500 (MD law mirrors federal CFPB rule)."),
    ("Wisconsin", "WI", 6, "Wis. Stat. § 893.43",
     "20% of disposable earnings",
     "Wisconsin has consumer-friendly debt collection rules and a 6-year SOL. HealthCheck/BadgerCare programs provide additional coverage for low-income residents.",
     "Standard federal rules apply."),
    ("Colorado", "CO", 6, "Colo. Rev. Stat. § 13-80-103.5",
     "25% of disposable earnings or amount over 40x state min wage",
     "Colorado HB 23-1126 prohibits medical debt from appearing on credit reports. Hospital Discounted Care law requires discounts for uninsured under 250% FPL.",
     "Medical debt is banned from credit reports under state law (HB 23-1126, 2023)."),
    ("Minnesota", "MN", 6, "Minn. Stat. § 541.05",
     "25% of disposable earnings or amount over 40x state min wage",
     "Minnesota Debt Fairness Act (2024) prohibits medical debt reporting, bans medical debt wage garnishment, and voids spousal liability for medical debt.",
     "Medical debt cannot be reported to credit bureaus (state law, 2024)."),
    ("Oregon", "OR", 6, "ORS § 12.080",
     "25% of disposable earnings or amount over $254/week",
     "Oregon Hospital Financial Assistance Law requires free care for patients under 200% FPL and discounts up to 400% FPL.",
     "Standard federal rules apply."),
    ("Nevada", "NV", 6, "NRS § 11.190(2)(c)",
     "25% of disposable earnings (federal cap)",
     "Nevada Medical Debt Protection Act (2023) prohibits credit reporting of medical debt under $10,000 and requires itemized bills on request.",
     "Medical debt under $10,000 cannot be reported to credit bureaus (state law, 2023)."),
    ("Connecticut", "CT", 6, "Conn. Gen. Stat. § 52-576",
     "25% of disposable earnings or amount over 40x federal min wage",
     "Connecticut An Act Concerning Medical Debt (2023) prohibits medical debt from credit reports and requires hospitals to screen uninsured patients for assistance.",
     "Medical debt cannot be reported to credit bureaus (state law, 2023)."),
]


def _build_guide(state: str, abbr: str, sol_years: int, sol_citation: str,
                 wage_garn: str, notable_law: str, credit_rule: str) -> dict:
    slug = f"medical-debt-laws-{state.lower().replace(' ', '-')}"
    return {
        "slug": slug,
        "title": f"{state} Medical Debt Laws: Statute of Limitations, Garnishment & Your Rights",
        "meta_description": (
            f"In {state}, medical debt has a {sol_years}-year statute of limitations ({sol_citation}). "
            f"Learn about wage garnishment rules, credit reporting, and state-specific protections for medical debt in {state}."
        ),
        "category": "State Guides",
        "published": "2026-04-15",
        "reviewed_on": "2026-04-15",
        "author": "BillKarma Team",
        "faqs": [
            {
                "q": f"What is the statute of limitations on medical debt in {state}?",
                "a": (
                    f"In {state}, the statute of limitations on medical debt is {sol_years} years, "
                    f"governed by {sol_citation}. After this period expires, creditors can no longer "
                    f"sue you to collect the debt in court — though they may still attempt to collect "
                    f"through other means, and the debt may still appear on your credit report for up to 7 years."
                ),
            },
            {
                "q": f"Can a hospital garnish my wages in {state}?",
                "a": (
                    f"In {state}, the wage garnishment rule for medical debt is: {wage_garn}. "
                    f"Garnishment only occurs after a creditor wins a lawsuit and obtains a court judgment. "
                    f"If you respond to any medical debt lawsuit, you can almost always negotiate before it reaches garnishment."
                ),
            },
            {
                "q": f"Does medical debt affect my credit in {state}?",
                "a": credit_rule + " Under federal rules, all medical debt under $500 is not reported; paid collections are removed; and unpaid debt has a 12-month grace period before reporting begins.",
            },
            {
                "q": f"What financial assistance is available for medical bills in {state}?",
                "a": (
                    f"Nonprofit hospitals in {state} are required under federal IRS rules to offer financial "
                    f"assistance programs. Many hospitals offer free care for patients under 200% of the federal "
                    f"poverty level and discounts up to 400% FPL. Apply in writing and request a copy of the "
                    f"hospital's Financial Assistance Policy (FAP)."
                ),
            },
        ],
        "body": f"""<p class="lead">Medical debt in {state} is governed by a <strong>{sol_years}-year statute of limitations</strong> ({sol_citation}). After this period, creditors cannot sue to collect the debt in court. {state} also has specific rules on wage garnishment, charity care, and credit reporting that affect how you should handle medical debt.</p>

<h2>Statute of limitations on medical debt in {state}</h2>
<p>Under {sol_citation}, the statute of limitations on written contracts (which includes most medical bills) is <strong>{sol_years} years</strong> in {state}. The clock starts from the date of last payment or last activity on the account.</p>
<p>Once this period expires, the debt is "time-barred" — the creditor cannot file a lawsuit to force payment. However:</p>
<ul>
  <li>The debt still legally exists and collectors can still request payment</li>
  <li>Making a payment or acknowledging the debt in writing can RESTART the clock</li>
  <li>The debt may still appear on your credit report for up to 7 years from first delinquency</li>
</ul>

<h2>Wage garnishment rules in {state}</h2>
<p><strong>{wage_garn}</strong></p>
<p>Wage garnishment can only occur after a creditor:</p>
<ol>
  <li>Files a civil lawsuit against you</li>
  <li>Serves you with a summons and complaint</li>
  <li>Wins a judgment (often by default if you don't respond)</li>
  <li>Obtains a separate garnishment order</li>
</ol>
<p>If you receive a lawsuit notice, ALWAYS respond — even just to request more time. Default judgments are the most common path to wage garnishment.</p>

<h2>Credit reporting rules for medical debt in {state}</h2>
<p>{credit_rule}</p>
<p>Under federal rules that apply nationwide:</p>
<ul>
  <li>Medical debt under $500 is not reported on credit files (as of 2023)</li>
  <li>Paid medical collections are removed from credit reports</li>
  <li>Unpaid medical debt has a 12-month grace period before appearing on credit reports</li>
  <li>Negative medical debt entries are removed after 7 years under FCRA</li>
</ul>

<h2>Notable {state} medical debt protections</h2>
<p>{notable_law}</p>

<h2>What to do if you have medical debt in {state}</h2>
<ol>
  <li><strong>Request an itemized bill.</strong> You have a legal right to one. Audit each line against Medicare rates before paying anything.</li>
  <li><strong>Apply for financial assistance.</strong> All nonprofit hospitals are required by IRS rules to offer charity care programs. Most cover patients up to 300–400% FPL.</li>
  <li><strong>Verify the statute of limitations.</strong> If the debt is older than {sol_years} years with no payment activity, it may be time-barred and unenforceable in court.</li>
  <li><strong>Negotiate before paying.</strong> Medical debt collectors typically buy debt for 5–10 cents on the dollar — they will often settle for 20–40% of face value.</li>
  <li><strong>Never ignore a lawsuit.</strong> Default judgments are the most common path to wage garnishment. Always respond to court notices even if only to request more time.</li>
  <li><strong>If you cannot pay, consider bankruptcy.</strong> Medical debt is fully dischargeable in Chapter 7 bankruptcy. Medical bills are the leading cause of personal bankruptcy in the US.</li>
</ol>

<div class="key-takeaway"><strong>Bottom line:</strong> In {state}, medical debt has a {sol_years}-year statute of limitations, and {wage_garn.lower() if not wage_garn.startswith('Wage') else wage_garn[0].lower() + wage_garn[1:]}. Audit your bill first, apply for charity care, and never make a payment on old debt without understanding whether it's time-barred.</div>""",
    }


for _entry in _STATE_DATA:
    _g = _build_guide(*_entry)
    register(_g["slug"], _g)
