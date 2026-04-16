"""Pillar guide: Medical Debt Laws by State — hub for 25 state spoke pages."""
from guides import register

_SLUG = "medical-debt-laws-by-state"

# (state_name, slug, sol_years, wage_garn_pct, notable_law)
_STATE_DATA = [
    ("Arizona", "medical-debt-laws-arizona", 6, "25%", "ARS 33-1131 homestead protection up to $150,000"),
    ("California", "medical-debt-laws-california", 4, "25%", "SB 1061 (2023): medical debt cannot affect credit scores"),
    ("Colorado", "medical-debt-laws-colorado", 6, "20%", "HB 23-1126: hospitals must offer charity care to those under 400% FPL"),
    ("Connecticut", "medical-debt-laws-connecticut", 6, "25%", "Medical Debt Act: income-based repayment schedules required"),
    ("Florida", "medical-debt-laws-florida", 5, "Exempt", "Head-of-household exemption bars most wage garnishment"),
    ("Georgia", "medical-debt-laws-georgia", 6, "25%", "O.C.G.A. §44-13-100 homestead exemption up to $21,500"),
    ("Illinois", "medical-debt-laws-illinois", 5, "15%", "210 ILCS 88/10: charity care required for patients under 200% FPL"),
    ("Indiana", "medical-debt-laws-indiana", 6, "25%", "IC 34-55-10-2 exemptions protect household goods and vehicles"),
    ("Maryland", "medical-debt-laws-maryland", 3, "25%", "Medical Debt Protection Act: 3-year SOL, income-based discount floors"),
    ("Massachusetts", "medical-debt-laws-massachusetts", 6, "15%", "Hospital free-care program required for patients under 400% FPL"),
    ("Michigan", "medical-debt-laws-michigan", 6, "25%", "MCL 600.5807: 6-year SOL on written contracts"),
    ("Minnesota", "medical-debt-laws-minnesota", 6, "25%", "Debt Fairness Act (2023): broad medical debt protections"),
    ("Missouri", "medical-debt-laws-missouri", 5, "25%", "Mo. Rev. Stat. §513.440 household goods exemption"),
    ("Nevada", "medical-debt-laws-nevada", 6, "25%", "NRS 239B.030: medical debt shielded from credit reporting"),
    ("New Jersey", "medical-debt-laws-new-jersey", 6, "10%", "N.J.S.A. 26:2H-18.64: charity care mandate for nonprofit hospitals"),
    ("New York", "medical-debt-laws-new-york", 3, "10%", "FMDRA (2023): 3-year SOL; income-based hospital forgiveness"),
    ("North Carolina", "medical-debt-laws-north-carolina", 3, "10%", "G.S. §1-52 3-year SOL; no wage garnishment for consumer debts"),
    ("Ohio", "medical-debt-laws-ohio", 6, "25%", "ORC 2329.66 exemptions; nonprofit hospital charity care required"),
    ("Oregon", "medical-debt-laws-oregon", 6, "25%", "ORS 441.096: financial assistance for patients under 200% FPL"),
    ("Pennsylvania", "medical-debt-laws-pennsylvania", 4, "10%", "Charity care required for patients under 200% FPL"),
    ("Tennessee", "medical-debt-laws-tennessee", 6, "25%", "T.C.A. 26-2-111 personal property exemptions"),
    ("Texas", "medical-debt-laws-texas", 4, "Exempt", "Tex. Prop. Code §42.001: wages fully exempt from garnishment"),
    ("Virginia", "medical-debt-laws-virginia", 5, "25%", "Va. Code §8.01-246: 5-year SOL on written contracts"),
    ("Washington", "medical-debt-laws-washington", 6, "25%", "RCW 70.170.060: charity care required for nonprofit hospitals"),
    ("Wisconsin", "medical-debt-laws-wisconsin", 6, "20%", "Wis. Stat. §815.18 exemptions protect primary vehicle and tools"),
]


def _build_state_table():
    rows = []
    for state, slug, sol, garn, notable in _STATE_DATA:
        rows.append(
            f'<tr>'
            f'<td><a href="/guides/{slug}/" class="font-medium text-accent-600">{state}</a></td>'
            f'<td class="text-center">{sol} years</td>'
            f'<td class="text-center">{garn}</td>'
            f'<td class="text-sm text-gray-600">{notable}</td>'
            f'</tr>'
        )
    return "\n".join(rows)


def _build_state_links():
    items = []
    for state, slug, sol, garn, notable in _STATE_DATA:
        items.append(
            f'<li><a href="/guides/{slug}/">{state} Medical Debt Laws</a> — '
            f'{sol}-year statute of limitations; wage garnishment cap {garn}</li>'
        )
    return "<ul>" + "\n".join(items) + "</ul>"


_BODY = f"""
<p class="lead">Medical debt laws vary dramatically from state to state. The statute of limitations (how long a collector can sue you), wage garnishment rules, and credit reporting protections all depend on where you live. This guide summarizes the laws in 25 states — click any state for the full guide including citations, action steps, and model letters.</p>

<div class="answer-box">
<strong>Quick Answer</strong>
Medical debt laws — including how long a collector can sue you and whether they can garnish your wages — vary by state. Three states (Texas, Florida as head-of-household, North Carolina for consumer debts) ban wage garnishment entirely. New York and Maryland recently cut their statute of limitations to 3 years. California and Nevada now bar medical debt from appearing on credit reports.
</div>

<h2>Key Medical Debt Terms Explained</h2>

<h3>Statute of Limitations (SOL)</h3>
<p>The statute of limitations is the time window in which a creditor can file a lawsuit to collect a debt. After it expires, the debt is "time-barred" — the collector cannot win a court judgment against you. Medical debt SOLs range from 3 years (New York, Maryland) to 6 years (California, Michigan, Ohio, Washington). The clock typically starts from your last payment or last activity on the account.</p>

<h3>Wage Garnishment</h3>
<p>If a collector wins a court judgment, they may be able to garnish your wages — take a percentage of your paycheck directly from your employer. Federal law caps garnishment at 25% of disposable income or 30× the federal minimum wage, whichever is less. Several states set stricter limits, and some prohibit garnishment entirely for consumer debts.</p>

<h3>Credit Reporting</h3>
<p>In 2023, the three major credit bureaus (Equifax, Experian, TransUnion) agreed to stop reporting medical debt under $500 and to give patients 1 year (instead of 6 months) before reporting any medical debt. Several states (California, Colorado, Nevada, New York) have passed laws further restricting medical debt credit reporting or banning it outright.</p>

<h2>Medical Debt Laws by State — At a Glance</h2>

<table>
<thead>
<tr>
<th>State</th>
<th>Statute of Limitations</th>
<th>Wage Garnishment Cap</th>
<th>Key Protection</th>
</tr>
</thead>
<tbody>
{_build_state_table()}
</tbody>
</table>

<p><em>This table reflects laws as of 2026. Laws change frequently — always verify current statutes before taking action.</em></p>

<h2>State-by-State Deep Dive</h2>
<p>Select your state for the full breakdown — statute of limitations details, wage garnishment rules, credit reporting protections, notable state law, and step-by-step action guides.</p>
{_build_state_links()}

<h2>Major State Law Changes in 2023–2026</h2>

<h3>New York (FMDRA 2023)</h3>
<p>The Fair Medical Debt Reporting Act cut New York's statute of limitations on medical debt to 3 years and required hospitals to provide income-based charity care for patients earning under 400% FPL. Medical debt may no longer appear on NY credit reports. <a href="/guides/medical-debt-laws-new-york/">Full New York guide →</a></p>

<h3>California (SB 1061, 2023)</h3>
<p>California became the first state to bar medical debt from affecting credit scores entirely. Collectors may still sue on time-barred debts in some cases, but no medical debt may appear on a California credit report. <a href="/guides/medical-debt-laws-california/">Full California guide →</a></p>

<h3>Colorado (HB 23-1126, 2023)</h3>
<p>Colorado requires hospitals to proactively offer charity care to patients earning under 400% FPL and prohibits extraordinary collection actions (lawsuits, wage garnishment) while a charity care application is pending. <a href="/guides/medical-debt-laws-colorado/">Full Colorado guide →</a></p>

<h3>Minnesota (Debt Fairness Act, 2023)</h3>
<p>Minnesota's Debt Fairness Act enacted sweeping consumer protections including extended notice requirements before collection actions and income-based payment plans. <a href="/guides/medical-debt-laws-minnesota/">Full Minnesota guide →</a></p>

<h3>Nevada (SB 469, 2023)</h3>
<p>Nevada now shields medical debt from credit reporting for most consumers and requires hospitals to proactively screen patients for charity care eligibility before initiating collections. <a href="/guides/medical-debt-laws-nevada/">Full Nevada guide →</a></p>

<h2>Your Rights Under Federal Law (All States)</h2>

<h3>FDCPA (Fair Debt Collection Practices Act)</h3>
<p>No matter what state you live in, the FDCPA protects you from harassment by third-party debt collectors. They cannot call before 8 AM or after 9 PM, cannot use abusive language, and must stop contacting you if you send a written cease-and-desist letter. <a href="/guides/fdcpa-rights-medical-debt-collectors/">Full FDCPA guide →</a></p>

<h3>Right to Debt Validation</h3>
<p>Within 30 days of a collector's first contact, you can send a debt validation letter demanding they prove the debt is yours and that the amount is correct. They must stop collection activity until they provide this validation. <a href="/guides/debt-validation-letter-medical-debt/">Free debt validation letter template →</a></p>

<h3>CFPB Medical Debt Rule (2025)</h3>
<p>The Consumer Financial Protection Bureau finalized a rule in 2025 banning medical debt from credit reports nationwide, effective for all new and existing medical debt. This rule is subject to potential regulatory changes — check our state guides for the latest status in your state.</p>

<h3>No Surprises Act</h3>
<p>Federal law bans surprise bills from out-of-network providers at in-network facilities for emergency care and certain non-emergency services. This applies in all 50 states. <a href="/guides/no-surprises-act-explained/">Full No Surprises Act guide →</a></p>

<h2>Steps to Take If You're Facing Medical Debt Collection</h2>
<ol>
<li><strong>Check the statute of limitations</strong> in your state (table above). If the SOL has expired, you likely cannot be successfully sued.</li>
<li><strong>Request debt validation</strong> within 30 days of the collector's first contact. Use our <a href="/guides/debt-validation-letter-medical-debt/">free validation letter template</a>.</li>
<li><strong>Apply for charity care</strong> at the hospital if you haven't already. Most nonprofit hospitals are legally required to provide charity care — and collection must pause while your application is reviewed.</li>
<li><strong>Negotiate a settlement</strong>. Medical debt collectors often accept 20–50 cents on the dollar for settled accounts. Get any agreement in writing before paying. <a href="/guides/settle-medical-debt-collections/">Settlement guide →</a></li>
<li><strong>Know your wage garnishment rights</strong> in your state (table above). If you live in Texas, Florida (head-of-household), or North Carolina, your wages may be fully protected.</li>
<li><strong>Check your credit report</strong> for errors. If medical debt appears after state or federal law bars it, you can dispute it directly with the credit bureau. <a href="/guides/medical-debt-credit-report-2026/">Medical debt credit report guide →</a></li>
</ol>
"""

register(_SLUG, {
    "title": "Medical Debt Laws by State: A Complete 2026 Guide (Statute of Limitations, Garnishment & Rights)",
    "meta_description": "Look up medical debt laws in your state: statute of limitations, wage garnishment rules, credit reporting protections, and recent 2023–2026 law changes. 25 states covered.",
    "published": "2026-04-16",
    "reviewed_on": "2026-04-16",
    "author": "BillKarma Team",
    "category": "Medical Debt",
    "faqs": [
        {"q": "What is the statute of limitations on medical debt?", "a": "The statute of limitations on medical debt varies by state, ranging from 3 years (New York, Maryland, North Carolina) to 6 years (California, Michigan, Ohio, Washington). After the SOL expires, a collector can no longer successfully sue you to collect the debt, though they may still attempt to contact you."},
        {"q": "Can my wages be garnished for medical debt?", "a": "It depends on your state. Texas bans wage garnishment for consumer debts entirely. Florida protects heads of household. North Carolina bans garnishment for consumer debts. Other states cap garnishment at 10–25% of disposable income. Federal law caps it at 25% nationwide, and states can only be stricter."},
        {"q": "Does medical debt affect my credit score?", "a": "Recent rule changes have reduced medical debt's impact on credit. Since 2023, the three major credit bureaus no longer report medical debt under $500. California, Colorado, Nevada, and New York now bar medical debt from credit reports entirely. A 2025 CFPB rule aims to ban it nationwide, though this is subject to legal challenges."},
        {"q": "What should I do if a debt collector contacts me about medical debt?", "a": "First, send a debt validation letter within 30 days to make the collector prove the debt is valid. Then check whether the statute of limitations has expired in your state. Apply for hospital charity care if you haven't already. Consider negotiating a lump-sum settlement for 20–50 cents on the dollar."},
    ],
    "body": _BODY,
})
