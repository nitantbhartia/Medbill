"""Guide: One Big Beautiful Bill Act 2026 - Medicaid Cuts."""

from guides import register, _embed

_calc_embed = _embed(mode="cost", title="Look up what Medicare pays for any procedure", subtitle="Use Medicare rates as your negotiation benchmark if you lose Medicaid coverage.", height="400")

register("medicaid-cuts-2026", {
    "title": "One Big Beautiful Bill Act 2026: How Medicaid Cuts Affect You and What to Do Next",
    "meta_description": "The OBBBA cuts $1 trillion from Medicaid over 10 years, with 11.8 million people projected to lose coverage. Learn how it affects you and your options.",
    "published": "2026-03-02",
    "author": "BillKarma Team",
    "category": "Health Insurance",
    "faqs": [
        {
            "q": "What is the One Big Beautiful Bill Act and how does it affect Medicaid?",
            "a": "The One Big Beautiful Bill Act (OBBBA), signed into law on July 4, 2025, cuts federal Medicaid funding by approximately $1 trillion over 10 years. The CBO estimates 11.8 million people will lose Medicaid coverage directly, with an additional 3.1 million losing coverage under marketplace plans. Key changes include new work requirements, more frequent eligibility checks, elimination of expansion incentives for non-expansion states, and new cost-sharing of up to $35 per service for expansion enrollees.",
        },
        {
            "q": "What are the Medicaid work requirements under the OBBBA?",
            "a": "Starting December 2026, certain Medicaid enrollees ages 19 to 64 must log at least 80 hours per month of community engagement, which includes employment, volunteering, or education. Exemptions exist for parents of children under 13, disabled veterans, individuals with substance use disorders or disabling mental disorders, and those with serious or complex medical conditions. Failure to document compliance can result in loss of coverage.",
        },
        {
            "q": "How often will Medicaid eligibility be checked under the new law?",
            "a": "Beginning January 2027, states must check eligibility for Medicaid expansion enrollees every 6 months, up from the current 12-month cycle. States may begin implementing work requirements before January 2027. More frequent checks increase the risk of losing coverage due to paperwork issues, even if you still qualify.",
        },
        {
            "q": "Will I have to pay copays on Medicaid now?",
            "a": "Yes, for Medicaid expansion recipients. The OBBBA allows states to impose cost-sharing of up to $35 per healthcare service for Medicaid expansion enrollees. This means every doctor visit, lab test, or prescription could carry a copay. Traditional Medicaid enrollees (pregnant women, children, elderly, disabled) are not subject to these new cost-sharing requirements.",
        },
        {
            "q": "What should I do if I lose Medicaid coverage?",
            "a": "Apply for marketplace coverage immediately. You qualify for a Special Enrollment Period when you lose Medicaid. If your income is below 400% FPL, you may qualify for premium subsidies. Also apply for hospital charity care programs at any hospital where you receive care. The No Surprises Act and Good Faith Estimate protections apply to all uninsured patients. Upload any bills to BillKarma to check for errors and overcharges.",
        },
        {
            "q": "Does the OBBBA affect Medicare too?",
            "a": "Yes. CBO estimates the law will trigger a $45 billion cut to Medicare in 2026, growing to $75 billion by 2034, through automatic sequestration. These cuts primarily affect provider reimbursement rates rather than beneficiary benefits directly, but they may reduce the number of providers willing to accept Medicare patients.",
        },
    ],
    "body": f"""
<p class="lead">On July 4, 2025, the One Big Beautiful Bill Act became law. It cuts <strong>$1 trillion from Medicaid over 10 years</strong>. The Congressional Budget Office estimates <strong>11.8 million people will lose coverage directly</strong>, with another 3.1 million losing marketplace coverage. New work requirements begin December 2026, eligibility checks double in frequency starting January 2027, and expansion enrollees now face copays of up to $35 per service. If you or someone you know relies on Medicaid, here is what changed and what to do about it.</p>

<nav class="toc">
    <h2>In this guide</h2>
    <ol>
        <li><a href="#what-changed">What the law actually changed</a></li>
        <li><a href="#who-affected">Who is affected</a></li>
        <li><a href="#work-requirements">Work requirements: what you need to know</a></li>
        <li><a href="#eligibility-checks">More frequent eligibility checks</a></li>
        <li><a href="#cost-sharing">New cost-sharing for expansion enrollees</a></li>
        <li><a href="#timeline">Implementation timeline</a></li>
        <li><a href="#what-to-do">What to do if you lose coverage</a></li>
        <li><a href="#protect-yourself">How to protect yourself from high medical bills</a></li>
        <li><a href="#faq">Frequently asked questions</a></li>
        <li><a href="#sources">Sources</a></li>
    </ol>
</nav>

<h2 id="what-changed">1. What the law actually changed</h2>

<p>The OBBBA is a budget reconciliation law that made sweeping changes to federal spending. The Medicaid provisions are among the most consequential. Here are the five major changes:</p>

<table>
    <thead>
        <tr><th>Change</th><th>What it does</th><th>When it takes effect</th></tr>
    </thead>
    <tbody>
        <tr><td><strong>Work requirements</strong></td><td>Requires 80 hours/month of "community engagement" for enrollees ages 19&ndash;64</td><td>December 2026</td></tr>
        <tr><td><strong>Eligibility redetermination</strong></td><td>States must re-verify expansion enrollee eligibility every 6 months (was 12 months)</td><td>January 2027</td></tr>
        <tr><td><strong>Cost-sharing</strong></td><td>States can charge expansion enrollees up to $35 per healthcare service</td><td>Effective immediately</td></tr>
        <tr><td><strong>Expansion incentive elimination</strong></td><td>Removes enhanced federal matching for states that newly expand Medicaid</td><td>January 2026</td></tr>
        <tr><td><strong>Provider funding for reproductive services</strong></td><td>Withholds one year of Medicaid funding from certain reproductive health providers</td><td>July 2025&ndash;July 2026</td></tr>
    </tbody>
</table>

<p>The CBO projects these changes will reduce federal Medicaid spending by approximately $1 trillion over the next decade. The largest savings come from people losing coverage due to work requirement documentation failures and more frequent eligibility checks &mdash; not from people who are ineligible.</p>

<div class="key-takeaway">
    <strong>Critical distinction:</strong> Research from Arkansas (the only state that previously implemented Medicaid work requirements) showed that 95% of enrollees who lost coverage were working or qualified for an exemption &mdash; they lost coverage due to paperwork and reporting failures, not because they didn&rsquo;t meet the requirements. The same pattern is expected nationwide.
</div>

<h2 id="who-affected">2. Who is affected</h2>

<p>The impact falls most heavily on four groups:</p>

<p><strong>Medicaid expansion enrollees (ages 19&ndash;64).</strong> The 21 million adults covered through Medicaid expansion in 40 states face all three major changes: work requirements, six-month eligibility checks, and new cost-sharing. The Urban Institute estimates that 3 in 10 young adults ages 18&ndash;24 enrolled in Medicaid are vulnerable to losing coverage.</p>

<p><strong>Low-income workers in jobs without health benefits.</strong> Many Medicaid expansion enrollees are already working &mdash; as home health aides, retail workers, gig economy workers, and restaurant employees. They work irregular hours that make monthly documentation difficult, and their employers typically do not offer health insurance.</p>

<p><strong>People with mental health and substance use conditions.</strong> While exemptions exist for "disabling mental disorders" and substance use disorders, qualifying for the exemption requires documentation from a healthcare provider. Many people in this population have inconsistent access to the providers who would need to certify their exemption.</p>

<p><strong>Rural communities.</strong> Rural hospitals receive a disproportionate share of Medicaid revenue. The KFF estimates that Medicaid spending in rural areas will decrease by $155 billion over 10 years. The OBBBA does include $50 billion in rural hospital relief funding, but this offsets only about a third of the projected losses.</p>

<h2 id="work-requirements">3. Work requirements: what you need to know</h2>

<p>Starting December 2026, Medicaid expansion enrollees ages 19&ndash;64 must document 80 hours per month of "community engagement." Qualifying activities include:</p>

<ul>
    <li>Employment (including part-time and self-employment)</li>
    <li>Job training or vocational education</li>
    <li>Community service or volunteer work</li>
    <li>Education (college, GED programs)</li>
    <li>Caregiving for a non-dependent</li>
</ul>

<p><strong>Who is exempt:</strong></p>

<ul>
    <li>Parents or caretakers of children under age 13</li>
    <li>Disabled veterans</li>
    <li>People who are blind or disabled</li>
    <li>People with substance use disorders</li>
    <li>People with "disabling" mental disorders</li>
    <li>People with "serious or complex" medical conditions</li>
    <li>Pregnant individuals</li>
</ul>

<div class="key-takeaway">
    <strong>The documentation trap:</strong> The requirement is not just to work 80 hours &mdash; it&rsquo;s to <em>document</em> 80 hours. States will establish reporting portals, but Arkansas&rsquo;s experience showed that the reporting systems were difficult to access, frequently crashed, and were not available by phone for people without internet. If your state implements work requirements, set calendar reminders to report monthly. Do not assume your eligibility will be maintained automatically.
</div>

<h2 id="eligibility-checks">4. More frequent eligibility checks</h2>

<p>Starting January 2027, states must re-verify Medicaid expansion eligibility every six months instead of every 12 months. This doubles the opportunities for "procedural disenrollment" &mdash; losing coverage because of a paperwork failure rather than an actual change in eligibility.</p>

<p>During the 2023&ndash;2024 Medicaid unwinding (when pandemic-era continuous enrollment ended), <strong>69% of all disenrollments were procedural</strong>, meaning the person likely still qualified but was dropped for not returning paperwork or because the state couldn&rsquo;t verify their information. With checks now happening twice as often, procedural disenrollment is expected to increase significantly.</p>

<p><strong>How to protect yourself:</strong></p>

<ol>
    <li>Keep your contact information current with your state Medicaid agency at all times</li>
    <li>Respond to every piece of mail from your state Medicaid office immediately</li>
    <li>Check your eligibility status online every month (most states have online portals)</li>
    <li>Save copies of all submitted documents</li>
    <li>If you are disenrolled, you have the right to appeal &mdash; file the appeal within 10 days to maintain coverage during the appeal process</li>
</ol>

<h2 id="cost-sharing">5. New cost-sharing for expansion enrollees</h2>

<p>The OBBBA allows states to impose copays of up to <strong>$35 per healthcare service</strong> on Medicaid expansion enrollees. For someone earning $18,000/year (just under 138% FPL for an individual), even a few medical visits per month at $35 each could consume a significant portion of disposable income.</p>

<table>
    <thead>
        <tr><th>Service</th><th>Potential cost-sharing</th><th>Impact on low-income enrollee ($18,000/year income)</th></tr>
    </thead>
    <tbody>
        <tr><td>Primary care visit</td><td>Up to $35</td><td>0.2% of annual income per visit</td></tr>
        <tr><td>Specialist visit</td><td>Up to $35</td><td>0.2% of annual income per visit</td></tr>
        <tr><td>ER visit</td><td>Up to $35</td><td>0.2% of annual income per visit</td></tr>
        <tr><td>Prescription drug</td><td>Up to $35</td><td>0.2% of annual income per fill</td></tr>
        <tr><td>Lab work</td><td>Up to $35</td><td>0.2% of annual income per test</td></tr>
        <tr><td><strong>Example: Monthly total (2 visits + 3 prescriptions)</strong></td><td><strong>Up to $175</strong></td><td><strong>11.7% of monthly income</strong></td></tr>
    </tbody>
</table>

<p>Not all states will implement the maximum $35 copay. Watch for your state&rsquo;s specific implementation plan. Traditional Medicaid enrollees (children, pregnant women, elderly, and disabled individuals) are not subject to these new copays.</p>

<h2 id="timeline">6. Implementation timeline</h2>

<table>
    <thead>
        <tr><th>Date</th><th>What happens</th><th>Who&rsquo;s affected</th></tr>
    </thead>
    <tbody>
        <tr><td>July 4, 2025</td><td>OBBBA signed into law</td><td>Everyone</td></tr>
        <tr><td>July 2025&ndash;July 2026</td><td>Reproductive health provider funding withheld</td><td>Patients at affected clinics</td></tr>
        <tr><td>January 2026</td><td>Enhanced FMAP for new expansion states eliminated</td><td>10 non-expansion states</td></tr>
        <tr><td>2026 (varies by state)</td><td>States begin implementing cost-sharing</td><td>Expansion enrollees</td></tr>
        <tr><td>December 2026</td><td>Work requirements take effect</td><td>Expansion enrollees ages 19&ndash;64</td></tr>
        <tr><td>January 2027</td><td>Six-month eligibility checks begin</td><td>Expansion enrollees</td></tr>
    </tbody>
</table>

<div class="key-takeaway">
    <strong>Don&rsquo;t wait until December.</strong> If you are a Medicaid expansion enrollee, start preparing now. Gather documentation of your work hours or exemption status. Update your contact information with your state agency. And explore alternative coverage options in case you lose eligibility.
</div>

<h2 id="what-to-do">7. What to do if you lose coverage</h2>

<p>If you lose Medicaid, you have several paths forward. The key is to act fast &mdash; gaps in coverage leave you vulnerable to catastrophic medical bills.</p>

<p><strong>Path 1: ACA Marketplace coverage.</strong> Losing Medicaid triggers a <a href="https://www.healthcare.gov/" target="_blank" rel="noopener">Special Enrollment Period</a> on the ACA marketplace. You have 60 days from your loss of coverage to enroll. If your income is below 400% FPL, you qualify for premium subsidies under the original ACA formula. Use the <a href="/guides/aca-subsidy-cliff-2026">ACA subsidy cliff guide</a> to understand current subsidy levels.</p>

<p><strong>Path 2: Employer-sponsored insurance.</strong> If your employer offers coverage, losing Medicaid is a qualifying event that allows you to enroll outside of open enrollment. Check with your HR department immediately.</p>

<p><strong>Path 3: CHIP for children.</strong> Even if you lose your own Medicaid, your children may still qualify for CHIP. Income limits for CHIP are typically 200&ndash;300% FPL, and many states cover children up to 400% FPL. Apply at <a href="https://www.insurekidsnow.gov/" target="_blank" rel="noopener">InsureKidsNow.gov</a>.</p>

<p><strong>Path 4: Hospital financial assistance.</strong> If you can&rsquo;t afford any insurance, <a href="/charity-care">check your eligibility for hospital charity care</a>. Nonprofit hospitals (60% of all U.S. hospitals) must offer financial assistance. Many provide free care for patients under 200% FPL and discounted care up to 400% FPL.</p>

<p><strong>Path 5: Community health centers.</strong> Federally Qualified Health Centers serve patients on a sliding fee scale regardless of insurance status. Find one at <a href="https://findahealthcenter.hrsa.gov/" target="_blank" rel="noopener">FindAHealthCenter.hrsa.gov</a>.</p>

<h2 id="protect-yourself">8. How to protect yourself from high medical bills</h2>

<p>Whether you keep Medicaid with new copays or lose coverage entirely, every dollar matters more now. Here is how to minimize your medical costs:</p>

<ol>
    <li><strong>Scan every bill for errors.</strong> <a href="/scan">Upload your bills to BillKarma</a> to check for duplicate charges, upcoding, and inflated markups. Billing errors affect 30&ndash;40% of hospital bills.</li>
    <li><strong>Request itemized bills.</strong> Never pay a summary bill. <a href="/guides/how-to-get-an-itemized-medical-bill">Request a line-by-line breakdown</a> and review every charge.</li>
    <li><strong>Use Medicare rates as your benchmark.</strong> Our <a href="/calculator">cost calculator</a> shows what Medicare pays for every CPT code. If you&rsquo;re uninsured, offering 150&ndash;200% of the Medicare rate is a fair starting point for negotiation.</li>
    <li><strong>Ask for self-pay discounts upfront.</strong> If you&rsquo;re now uninsured, ask every provider for their cash-pay or self-pay rate before receiving services.</li>
    <li><strong>Get Good Faith Estimates.</strong> The No Surprises Act gives uninsured patients the right to a written estimate before any scheduled service. If the final bill exceeds the estimate by $400+, you can dispute it.</li>
    <li><strong>Apply for charity care before you owe.</strong> <a href="/charity-care">Check your eligibility</a> at every hospital before receiving care, not after you get the bill.</li>
</ol>

{_calc_embed}

<div class="case-study">
    <h3>Case study: Former Medicaid enrollee saves $3,200 on ER bill</h3>
    <p><strong>Situation:</strong> Keisha, 34, lost her Medicaid expansion coverage in a previous state unwinding due to a paperwork issue. Before she could re-enroll, she needed emergency care for a kidney stone. The ER bill: $4,800.</p>
    <p><strong>What she did:</strong> She <a href="/scan">uploaded the bill to BillKarma</a>, which flagged a duplicate CT scan charge ($980) and an upcoded ER visit level (billed as Level 5, which matched a Level 3 visit). She also applied for the hospital&rsquo;s charity care program, qualifying for a 40% discount based on her income.</p>
    <p><strong>Result:</strong> After the billing corrections ($980 duplicate + $320 upcoding adjustment) and the 40% charity care discount on the remaining balance, her final bill dropped from $4,800 to <strong>$1,600</strong>. Total savings: $3,200.</p>
</div>

<h2 id="faq">Frequently asked questions</h2>

<div class="faq-section">
    <div class="faq-item">
        <h3>What is the One Big Beautiful Bill Act and how does it affect Medicaid?</h3>
        <p>The OBBBA, signed July 4, 2025, cuts $1 trillion from Medicaid over 10 years. The CBO projects 11.8 million people will lose coverage directly. Key changes include work requirements (80 hours/month starting December 2026), six-month eligibility checks (starting January 2027), copays up to $35 per service for expansion enrollees, and elimination of enhanced matching for new expansion states.</p>
    </div>
    <div class="faq-item">
        <h3>Do I have to work to keep my Medicaid?</h3>
        <p>Starting December 2026, Medicaid expansion enrollees ages 19&ndash;64 must document 80 hours/month of "community engagement" (work, volunteering, education, or job training). Exemptions exist for parents of children under 13, disabled veterans, people with disabilities, substance use disorders, serious medical conditions, and pregnant individuals. The key challenge is documenting compliance, not the requirement itself.</p>
    </div>
    <div class="faq-item">
        <h3>What happens if I lose Medicaid coverage?</h3>
        <p>Losing Medicaid triggers a 60-day Special Enrollment Period for ACA marketplace plans. If your income is below 400% FPL, you may qualify for premium subsidies. You should also check employer coverage options, CHIP for children, <a href="/charity-care">hospital financial assistance</a>, and community health centers. Acting quickly is critical to avoid gaps in coverage.</p>
    </div>
    <div class="faq-item">
        <h3>Will I have to pay copays on Medicaid?</h3>
        <p>If you are a Medicaid expansion enrollee, states can now charge up to $35 per healthcare service under the OBBBA. This applies to doctor visits, prescriptions, lab work, and other services. Traditional Medicaid enrollees (children, pregnant women, elderly, disabled) are not affected by the new cost-sharing provisions. Not all states will implement the maximum amount &mdash; check your state&rsquo;s plan.</p>
    </div>
    <div class="faq-item">
        <h3>How does this affect Medicare?</h3>
        <p>The CBO estimates the OBBBA will trigger $45 billion in Medicare cuts in 2026, growing to $75 billion by 2034, through automatic sequestration. These cuts primarily reduce provider reimbursement rates. Medicare beneficiary benefits are not directly reduced, but fewer providers may accept Medicare if reimbursement rates fall, potentially affecting access to care.</p>
    </div>
    <div class="faq-item">
        <h3>What if I was dropped from Medicaid by mistake?</h3>
        <p>You have the right to appeal any Medicaid disenrollment. File your appeal within 10 days of receiving the termination notice to maintain coverage during the appeal process. During the 2023&ndash;2024 unwinding, 69% of disenrollments were procedural (paperwork issues, not ineligibility). Contact your state Medicaid agency or call 1-800-318-2596 (the federal marketplace line) for help.</p>
    </div>
</div>

<h2 id="sources">Sources</h2>

<ul class="sources-list">
    <li><a href="https://www.ama-assn.org/health-care-advocacy/federal-advocacy/changes-medicaid-aca-and-other-key-provisions-one-big" target="_blank" rel="noopener">AMA: Changes to Medicaid, the ACA, and Other Key Provisions of the One Big Beautiful Bill Act</a></li>
    <li><a href="https://www.americanprogress.org/article/the-truth-about-the-one-big-beautiful-bill-acts-cuts-to-medicaid-and-medicare/" target="_blank" rel="noopener">Center for American Progress: The Truth About the OBBBA&rsquo;s Cuts to Medicaid and Medicare</a></li>
    <li><a href="https://www.urban.org/urban-wire/medicaid-cuts-one-big-beautiful-bill-act-leave-3-10-young-adults-vulnerable-losing" target="_blank" rel="noopener">Urban Institute: Medicaid Cuts Leave 3 in 10 Young Adults Vulnerable to Losing Coverage</a></li>
    <li><a href="https://www.cbo.gov/" target="_blank" rel="noopener">Congressional Budget Office: Budgetary Impact Analysis of the One Big Beautiful Bill Act</a></li>
    <li><a href="https://www.kff.org/medicaid/" target="_blank" rel="noopener">Kaiser Family Foundation: Medicaid Enrollment and Spending Data</a></li>
    <li><a href="https://www.propel.app/blog/medicaid-cuts-explained-big-beautiful-bill-updates/" target="_blank" rel="noopener">Propel: Medicaid Cuts Explained &mdash; What the Big Beautiful Bill Means for Recipients</a></li>
    <li><a href="https://www.cms.gov/medical-bill-rights" target="_blank" rel="noopener">CMS: Medical Bill Rights for Patients</a></li>
    <li><a href="https://www.healthcare.gov/" target="_blank" rel="noopener">HealthCare.gov: Apply for Marketplace Coverage</a></li>
</ul>
""",
})
