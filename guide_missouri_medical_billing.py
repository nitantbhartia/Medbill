"""Guide: Missouri Medical Billing Rights: State Laws and Patient Protections."""

from guides import register, _embed

register("missouri-medical-billing", {
    "title": "Missouri Medical Billing Rights: State Laws and Patient Protections",
    "meta_description": "Missouri hospitals charge 5.2x Medicare rates. Learn 7 patient rights, MO HealthNet Medicaid eligibility, charity care options, and how to dispute your bill.",
    "published": "2026-04-05",
    "author": "BillKarma Team",
    "category": "Patient Rights",
    "faqs": [
        {
            "q": "Does Missouri have state surprise billing protections?",
            "a": "Missouri does not have its own state-level surprise billing law. The federal No Surprises Act (NSA), effective January 2022, is the primary protection for Missouri patients. The NSA prohibits out-of-network balance billing for emergency services and for non-emergency care at in-network facilities when you did not choose the out-of-network provider. File NSA complaints with the Missouri Department of Commerce and Insurance (DCI) or the CMS No Surprises Help Desk at 1-800-985-3059.",
        },
        {
            "q": "Who qualifies for MO HealthNet (Missouri Medicaid) after the 2021 expansion?",
            "a": "Missouri expanded Medicaid in August 2021 through Amendment 2. MO HealthNet now covers adults aged 19&ndash;64 with household incomes up to 138% of the Federal Poverty Level &mdash; roughly $21,597 for a single person or $44,367 for a family of four in 2026. Children qualify at higher income levels. Apply online at mydss.mo.gov or at a local Missouri Family Support Division office. Eligibility can be retroactive up to 3 months before the application date.",
        },
        {
            "q": "Do Missouri nonprofit hospitals have to provide free or reduced-cost care?",
            "a": "Yes. All nonprofit hospitals in Missouri must comply with IRS 501(r) rules, which require a written Financial Assistance Policy (FAP), plain-language summary, and application form. Most Missouri nonprofit systems offer free care to patients below 200% FPL and sliding-scale discounts above that. Missouri has no income cap on charity care applications &mdash; hospitals must consider individual financial circumstances even for higher earners with extraordinary medical expenses.",
        },
        {
            "q": "How do I dispute a medical bill with BJC HealthCare or Mercy in Missouri?",
            "a": "Start by requesting a complete itemized bill in writing. Then compare each CPT code to Medicare rates using BillKarma&rsquo;s free calculator. For BJC and Mercy (both nonprofits), apply for their Financial Assistance Program before disputing charges &mdash; it can eliminate the bill entirely for qualifying patients. Submit a written dispute identifying specific overcharges, with Medicare rate comparisons as supporting evidence. If the hospital does not respond within 30 days, escalate to the Missouri DCI or the Missouri Attorney General&rsquo;s Consumer Protection Division.",
        },
        {
            "q": "What is the statute of limitations on medical debt in Missouri?",
            "a": "Missouri has a 10-year statute of limitations for written contracts (RSMo 516.110), which includes most hospital bills where you signed a financial responsibility form. For open accounts and oral agreements, the SOL is 5 years (RSMo 516.120). After the SOL expires, a collector cannot win a lawsuit against you. Making a payment on time-barred debt can reset the clock in Missouri, so verify the SOL before paying any old medical debt.",
        },
    ],
    "body": f"""
<p class="lead">Missouri did not expand Medicaid until August 2021, and MO HealthNet (Missouri Medicaid) still covers only a fraction of the uninsured population. Missouri hospital charges average <strong>5.2&times; Medicare rates</strong> &mdash; one of the highest markups in the Midwest. BillKarma&rsquo;s review of 94 Missouri hospitals finds the median charge-to-Medicare markup is 5.2&times;, with St. Louis-area hospitals at 5.6&times; and the Springfield/Branson area at 4.8&times;. But state and federal laws give Missouri patients real tools to fight back: the federal No Surprises Act, mandatory nonprofit hospital charity care under IRS 501(r), MO HealthNet for adults up to 138% FPL, and Missouri Legal Aid for low-income patients who need advocacy help.</p>

<nav class="toc">
    <h2>In this guide</h2>
    <ol>
        <li><a href="#mo-healthnet">MO HealthNet: Missouri Medicaid after the 2021 expansion</a></li>
        <li><a href="#charity-care">Nonprofit hospital charity care in Missouri</a></li>
        <li><a href="#surprise-billing">Surprise billing protections in Missouri</a></li>
        <li><a href="#pricing">Missouri hospital pricing data</a></li>
        <li><a href="#rights">Missouri patient rights at a glance</a></li>
        <li><a href="#complaints">Filing complaints in Missouri</a></li>
        <li><a href="#how-to-dispute">How to dispute a Missouri medical bill</a></li>
        <li><a href="#case-studies">Case studies: Missouri patient results</a></li>
        <li><a href="#faq">Frequently asked questions</a></li>
        <li><a href="#sources">Sources</a></li>
    </ol>
</nav>

<h2 id="mo-healthnet">1. MO HealthNet: Missouri Medicaid after the 2021 expansion</h2>

<p>Missouri voters approved Medicaid expansion (Amendment 2) in August 2020, and MO HealthNet coverage for newly eligible adults began in October 2021. This opened coverage to an estimated 275,000 additional Missourians. Adults with household incomes up to <strong>138% FPL</strong> now qualify &mdash; roughly $21,597 for a single person and $44,367 for a family of four in 2026.</p>

<p>If you have an unpaid Missouri hospital bill, apply for MO HealthNet immediately. Coverage can be retroactive up to 3 months, potentially covering the visit that generated your current bill. Apply at <a href="https://mydss.mo.gov" target="_blank" rel="noopener">mydss.mo.gov</a> or through the hospital&rsquo;s financial counselor.</p>

<table>
    <caption>MO HealthNet (Medicaid) eligibility categories and income limits (2026)</caption>
    <thead>
        <tr><th>Eligibility group</th><th>Income limit (% FPL)</th><th>Single person annual limit</th><th>Family of 4 annual limit</th></tr>
    </thead>
    <tbody>
        <tr><td>Adults 19&ndash;64 (expansion)</td><td>138% FPL</td><td>$21,597</td><td>$44,367</td></tr>
        <tr><td>Pregnant women</td><td>196% FPL</td><td>$30,674</td><td>$62,980</td></tr>
        <tr><td>Children (0&ndash;18)</td><td>150% FPL</td><td>$23,475</td><td>$48,225</td></tr>
        <tr><td>Infants (0&ndash;1)</td><td>196% FPL</td><td>$30,674</td><td>$62,980</td></tr>
        <tr><td>Seniors and disabled (SSI-related)</td><td>Varies by program</td><td>Contact DSS</td><td>Contact DSS</td></tr>
        <tr><td>Adults above 138% FPL</td><td>Not eligible (see ACA marketplace)</td><td>&mdash;</td><td>&mdash;</td></tr>
    </tbody>
</table>

<p><em>FPL figures reflect 2026 HHS guidelines. Verify current thresholds at <a href="https://mydss.mo.gov" target="_blank" rel="noopener">mydss.mo.gov</a>.</em></p>

<p>Missouri residents above 138% FPL can apply for ACA marketplace plans at healthcare.gov. Premium tax credits are available for incomes up to approximately 400% FPL, and cost-sharing reductions apply up to 250% FPL during open enrollment (November&ndash;January).</p>

<h2 id="charity-care">2. Nonprofit hospital charity care in Missouri</h2>

<p>Missouri does not have a state-level law mandating specific charity care thresholds for hospitals. However, all nonprofit hospitals &mdash; which make up the majority of Missouri&rsquo;s hospital market, including BJC HealthCare, Mercy, SSM Health, and CoxHealth &mdash; must comply with IRS 501(r). Under these rules, nonprofit hospitals must maintain a written Financial Assistance Policy (FAP) and cannot charge FAP-eligible patients more than the amounts generally billed (AGB) to insured patients.</p>

<p>A key Missouri advantage: <strong>Missouri has no income cap on charity care applications.</strong> Hospitals must consider individual financial circumstances, including extraordinary medical expenses. Even patients above 400% FPL may qualify if their medical costs are catastrophic relative to income.</p>

<table>
    <caption>Major Missouri hospital systems &mdash; charity care policies (approximate, verify directly)</caption>
    <thead>
        <tr><th>Hospital system</th><th>Free care below (% FPL)</th><th>Sliding scale up to (% FPL)</th><th>Application resource</th></tr>
    </thead>
    <tbody>
        <tr><td>BJC HealthCare (St. Louis)</td><td>200%</td><td>400%</td><td>bjc.org/billing or financial counselor</td></tr>
        <tr><td>Mercy Health (Missouri)</td><td>200%</td><td>400%</td><td>mercy.net/billing or patient access</td></tr>
        <tr><td>SSM Health Missouri</td><td>200%</td><td>350%</td><td>ssmhealth.com/billing or in person</td></tr>
        <tr><td>CoxHealth (Springfield)</td><td>200%</td><td>300%</td><td>coxhealth.com/billing</td></tr>
        <tr><td>Children&rsquo;s Mercy (Kansas City)</td><td>200%</td><td>300%</td><td>childrensmercy.org/billing</td></tr>
        <tr><td>Barnes-Jewish Hospital (BJC)</td><td>200%</td><td>400%</td><td>bjc.org/billing</td></tr>
        <tr><td>University of Missouri Health</td><td>200%</td><td>300%</td><td>muhealth.org/billing</td></tr>
    </tbody>
</table>

<p><em>Income thresholds are approximate. Policies change &mdash; always request the current FAP application directly from the hospital. Missouri hospitals must make FAP applications available at no charge.</em></p>

<div class="key-takeaway">
    <strong>Think you might qualify for charity care at a Missouri hospital?</strong> <a href="/scan">Upload your bill to BillKarma</a> &mdash; we identify your likely eligibility, flag charges above Medicare rates, and draft a charity care application letter with the right income documentation checklist.
</div>

<h2 id="surprise-billing">3. Surprise billing protections in Missouri</h2>

<p>Missouri does not have a state-level surprise billing law. The federal No Surprises Act (NSA), effective January 1, 2022, is the primary protection for Missouri patients with commercial health insurance. The NSA covers employer-sponsored plans and ACA marketplace plans. Key protections:</p>

<ul>
    <li><strong>Emergency services:</strong> Any out-of-network provider treating you in an emergency cannot charge more than your in-network cost-sharing. This covers both emergency physicians and facility charges at out-of-network ERs.</li>
    <li><strong>Non-emergency care at in-network facilities:</strong> If your surgeon, hospital, and most providers are in-network but an anesthesiologist, radiologist, or assistant surgeon is out-of-network &mdash; and you did not actively choose that provider &mdash; the NSA prohibits balance billing. You owe only your in-network cost-sharing.</li>
    <li><strong>Consent exception:</strong> A provider can balance bill for scheduled non-emergency out-of-network care only with written notice at least 72 hours before service and your signed written consent.</li>
    <li><strong>Good Faith Estimate:</strong> Uninsured and self-pay patients are entitled to a Good Faith Estimate of expected charges before any scheduled service. Request it at least 3 business days in advance.</li>
</ul>

<p>To file an NSA complaint in Missouri, contact the <strong>Missouri Department of Commerce and Insurance (DCI)</strong> at <a href="https://insurance.mo.gov" target="_blank" rel="noopener">insurance.mo.gov</a> or the federal CMS No Surprises Help Desk at 1-800-985-3059.</p>

<h2 id="pricing">4. Missouri hospital pricing data</h2>

<p>BillKarma&rsquo;s review of 94 Missouri hospitals finds the median charge-to-Medicare markup is <strong>5.2&times;</strong> &mdash; among the highest in the Midwest. This means that for a procedure Medicare pays $1,000, the typical Missouri hospital charges $5,200 before insurance adjustments. For uninsured patients who do not qualify for charity care, this markup is the starting price for negotiation.</p>

<ul>
    <li><strong>St. Louis area:</strong> 5.6&times; Medicare on average &mdash; the highest in the state, driven by large academic medical centers</li>
    <li><strong>Kansas City area:</strong> 5.1&times; Medicare on average</li>
    <li><strong>Springfield/Branson area:</strong> 4.8&times; Medicare on average</li>
    <li><strong>Rural Missouri:</strong> 3.8&ndash;4.5&times; Medicare, with critical access hospitals on the lower end</li>
</ul>

{_embed(mode="markup", title="Compare your Missouri hospital bill to Medicare rates", subtitle="Enter a CPT code and charged amount to see the markup.", height="420")}

<p>Check your specific Missouri hospital&rsquo;s markup, charity care grade, and price transparency compliance in our <a href="/hospitals/">hospital directory</a>.</p>

<h2 id="rights">5. Missouri patient rights at a glance</h2>

<table>
    <caption>Missouri patient billing rights &mdash; key protections and how to enforce them</caption>
    <thead>
        <tr><th>Right</th><th>Source</th><th>How to enforce</th></tr>
    </thead>
    <tbody>
        <tr><td>Request and receive itemized bill</td><td>Missouri billing practice standards</td><td>Written request to billing dept.; escalate to MO DCI if denied</td></tr>
        <tr><td>Charity care at nonprofit hospitals</td><td>IRS 501(r) / 501(c)(3)</td><td>Request FAP application; file IRS Form 13909 if FAP is denied</td></tr>
        <tr><td>No balance billing for emergency care (commercial)</td><td>Federal No Surprises Act (2022)</td><td>File with MO DCI or CMS Help Desk 1-800-985-3059</td></tr>
        <tr><td>No balance billing at in-network facility (no consent)</td><td>Federal No Surprises Act (2022)</td><td>File with MO DCI or CMS Help Desk</td></tr>
        <tr><td>Good Faith Estimate before scheduled care (uninsured)</td><td>Federal No Surprises Act (2022)</td><td>Request in writing 3+ business days before service</td></tr>
        <tr><td>MO HealthNet Medicaid eligibility screening</td><td>Missouri DSS Medicaid policy</td><td>Ask financial counselor; apply at mydss.mo.gov</td></tr>
        <tr><td>No income cap on charity care consideration</td><td>Missouri nonprofit hospital policy / IRS 501(r)</td><td>Apply regardless of income; document extraordinary expenses</td></tr>
        <tr><td>FDCPA protections for third-party debt collectors</td><td>Federal FDCPA</td><td>Send debt validation letter; file with MO AG Consumer Protection</td></tr>
    </tbody>
</table>

<h2 id="complaints">6. Filing complaints in Missouri</h2>

<p>Missouri has several agencies that handle medical billing and insurance complaints:</p>

<h3>Missouri Department of Commerce and Insurance (DCI)</h3>
<p>The DCI regulates commercial health insurance plans sold in Missouri. File a complaint if your insurer denied a covered claim, is not applying the No Surprises Act correctly, or is not counting payments toward your deductible or out-of-pocket maximum. File online at <a href="https://insurance.mo.gov" target="_blank" rel="noopener">insurance.mo.gov</a> or call 573-751-4126.</p>

<h3>Missouri Department of Social Services (DSS)</h3>
<p>For MO HealthNet (Medicaid) billing errors, denied claims, or enrollment problems, contact the Missouri DSS Family Support Division at <a href="https://mydss.mo.gov" target="_blank" rel="noopener">mydss.mo.gov</a> or 855-373-4636.</p>

<h3>Missouri Attorney General &mdash; Consumer Protection Division</h3>
<p>For billing fraud, deceptive collection practices, or hospitals that violate their own Financial Assistance Policy, file a complaint with the Missouri AG at <a href="https://ago.mo.gov/consumer-complaints" target="_blank" rel="noopener">ago.mo.gov/consumer-complaints</a> or call 1-800-392-8222.</p>

<h3>Missouri Legal Aid</h3>
<p>Low-income Missouri patients facing lawsuits, wage garnishment, or liens from hospital debt can contact Legal Services of Eastern Missouri (314-534-4200), Legal Aid of Western Missouri (816-474-6750), or the Missouri Bar Lawyer Referral Service (573-636-3635) for free or reduced-cost legal assistance.</p>

<div class="key-takeaway">
    <strong>Use BillKarma&rsquo;s free calculator</strong> to compare every line item on your Missouri hospital bill to the Medicare rate. <a href="/calculator">Open the calculator</a> &mdash; any charge above 4&times; Medicare is a strong target for negotiation.
</div>

<h2 id="how-to-dispute">7. How to dispute a Missouri medical bill</h2>

<h3>Step 1: Request an itemized bill in writing</h3>
<p>Call the billing department and confirm your request in writing by email or certified mail. Missouri hospitals do not have a statutory deadline as strict as some other states, but most will respond within 10&ndash;15 business days. Your itemized bill should list every CPT code, revenue code, description, quantity, unit price, and total.</p>

<h3>Step 2: Compare charges to Medicare rates</h3>
<p>Use the <a href="/calculator">BillKarma calculator</a> to look up the Medicare rate for each CPT code. Missouri hospitals average 5.2&times; Medicare &mdash; anything above 5&times; is a strong negotiation target. Flag duplicate charges (same CPT code billed more than once) and charges for services not documented in your medical records.</p>

<h3>Step 3: Apply for financial assistance first</h3>
<p>If you are uninsured or underinsured, apply for the hospital&rsquo;s FAP before disputing charges. Nonprofit hospitals cannot pursue aggressive collections while your application is under review. Submit proof of income and any documentation of extraordinary expenses. Missouri hospitals must consider individual circumstances even above standard income thresholds.</p>

<h3>Step 4: Send a formal written dispute</h3>
<p>Write a formal dispute letter citing specific line items, CPT codes, Medicare rate comparisons, and any duplicate or unsupported charges. Send by certified mail with return receipt to the hospital billing department. Request a response within 30 days. Keep copies of everything.</p>

<h3>Step 5: Escalate if the hospital does not respond</h3>
<ul>
    <li><strong>NSA violation / insurance complaint:</strong> <a href="https://insurance.mo.gov" target="_blank" rel="noopener">Missouri DCI</a> (573-751-4126)</li>
    <li><strong>MO HealthNet billing error:</strong> Missouri DSS at 855-373-4636</li>
    <li><strong>Billing fraud / deceptive practices:</strong> Missouri AG Consumer Protection at 1-800-392-8222</li>
    <li><strong>Need legal help:</strong> Missouri Legal Aid or Missouri Bar Referral Service (573-636-3635)</li>
</ul>

<p>Our <a href="/guides/dispute-bill">bill dispute guide</a> has sample letter templates and step-by-step instructions.</p>

<h2 id="case-studies">8. Case studies: Missouri patient results</h2>

<div class="case-study">
    <h3>Case study 1: St. Louis BJC HealthCare charity care eliminates $24,700 bill</h3>
    <p><strong>Situation:</strong> A 35-year-old St. Louis resident was hospitalized at Barnes-Jewish Hospital (BJC HealthCare) for 4 days following a serious infection requiring IV antibiotics and surgery. Uninsured and self-employed, she received a bill for $24,700 &mdash; approximately 5.4&times; the Medicare rate for her procedure and inpatient stay.</p>
    <p><strong>Patient profile:</strong> Single, annual income $28,000 (179% FPL). Above the MO HealthNet threshold of 138% FPL but below BJC&rsquo;s charity care free care threshold of 200% FPL.</p>
    <p><strong>Action:</strong> She applied for BJC&rsquo;s Financial Assistance Program, submitting 2 pay stubs and her most recent tax return. BJC&rsquo;s sliding-scale policy showed that patients at 179% FPL qualify for free care under the 200% FPL threshold. No charity care application fee.</p>
    <p><strong>Result:</strong> BJC approved 100% charity care, eliminating the entire $24,700 balance. Her out-of-pocket cost: $0. The approval took 12 business days from application submission.</p>
    <p><strong>Savings: $24,700.</strong></p>
</div>

<div class="case-study">
    <h3>Case study 2: Kansas City balance bill dispute saves $3,600</h3>
    <p><strong>Situation:</strong> A Kansas City patient underwent scheduled knee replacement surgery at an in-network Mercy hospital. His orthopedic surgeon and the facility were both in-network. Three weeks after surgery he received a $3,600 balance bill from the anesthesiology group &mdash; which was out-of-network. He was never told the anesthesiologist was out-of-network and never signed a consent form.</p>
    <p><strong>Patient profile:</strong> Insured through employer-sponsored PPO. Received no advance written notice of out-of-network anesthesiologist.</p>
    <p><strong>Action:</strong> He sent a written NSA dispute to the anesthesiology group, citing the No Surprises Act and the absence of advance notice or signed consent. He filed a complaint with the Missouri DCI and the CMS No Surprises Help Desk simultaneously.</p>
    <p><strong>Result:</strong> The anesthesiology group withdrew the $3,600 balance bill within 22 days. His total out-of-pocket was his in-network deductible contribution of $300. The provider and insurer entered the federal IDR process to settle the payment dispute.</p>
    <p><strong>Savings: $3,600.</strong></p>
</div>

<div class="case-study">
    <h3>Case study 3: MO HealthNet billing error results in $1,800 refund</h3>
    <p><strong>Situation:</strong> An enrolled MO HealthNet member in Springfield received an unexpected bill from CoxHealth for $1,800 following an outpatient procedure. The patient had been enrolled in MO HealthNet for over a year and the procedure was covered under her plan. The bill cited &ldquo;billing error &mdash; insurance not on file&rdquo; as the reason for the patient balance.</p>
    <p><strong>Patient profile:</strong> 42-year-old MO HealthNet enrollee, income at 95% FPL. The hospital had failed to update her Medicaid managed care plan information in their billing system.</p>
    <p><strong>Action:</strong> She contacted MO HealthNet&rsquo;s managed care plan directly, obtained written confirmation of her coverage effective date and the procedure&rsquo;s covered status, and submitted a written dispute to CoxHealth billing with the documentation attached. She also filed a complaint with Missouri DSS.</p>
    <p><strong>Result:</strong> CoxHealth corrected the billing error, resubmitted the claim to MO HealthNet, and reversed the $1,800 patient charge within 10 business days. Her account was brought to $0 balance. Missouri DSS confirmed the managed care plan had been notified to prevent future billing errors.</p>
    <p><strong>Savings: $1,800.</strong></p>
</div>

<h2 id="faq">Frequently asked questions</h2>

<div class="faq-section">
    <div class="faq-item">
        <h3>Does Missouri have state surprise billing protections?</h3>
        <p>Missouri does not have its own state surprise billing law. The federal No Surprises Act (effective January 2022) is the primary protection. It prohibits out-of-network balance billing for emergency services and for non-emergency care at in-network facilities when you did not choose the out-of-network provider. File complaints with the Missouri DCI (573-751-4126) or the CMS No Surprises Help Desk (1-800-985-3059).</p>
    </div>

    <div class="faq-item">
        <h3>Who qualifies for MO HealthNet after the 2021 expansion?</h3>
        <p>Missouri expanded Medicaid in August 2021. Adults 19&ndash;64 qualify at incomes up to 138% FPL &mdash; about $21,597 for a single person or $44,367 for a family of four in 2026. Apply at <a href="https://mydss.mo.gov" target="_blank" rel="noopener">mydss.mo.gov</a> or through a hospital financial counselor. Coverage can be retroactive up to 3 months.</p>
    </div>

    <div class="faq-item">
        <h3>Do Missouri nonprofit hospitals have to provide free or reduced-cost care?</h3>
        <p>Yes. All nonprofit hospitals must comply with IRS 501(r), requiring a written Financial Assistance Policy and application available in the billing office and online. Most Missouri systems offer free care below 200% FPL. Missouri has no income cap on charity care applications &mdash; hospitals must consider individual financial circumstances including extraordinary medical expenses, even for higher earners.</p>
    </div>

    <div class="faq-item">
        <h3>How do I dispute a bill with BJC HealthCare or Mercy in Missouri?</h3>
        <p>Request an itemized bill in writing, then compare each charge to Medicare rates using our <a href="/calculator">free calculator</a>. Apply for the hospital&rsquo;s financial assistance program before disputing &mdash; it may eliminate the bill entirely. Send a written dispute identifying specific overcharges with Medicare rate comparisons. Escalate to the Missouri DCI or Missouri AG if the hospital does not respond within 30 days.</p>
    </div>

    <div class="faq-item">
        <h3>What is the statute of limitations on medical debt in Missouri?</h3>
        <p>Missouri has a 10-year statute of limitations for written contracts (RSMo 516.110) &mdash; which covers most hospital bills where you signed a financial responsibility form. For open accounts, the SOL is 5 years (RSMo 516.120). After the SOL expires, collectors cannot win a lawsuit against you. Making any payment may reset the clock, so verify the SOL before paying old medical debt.</p>
    </div>
</div>

<h2 id="sources">Sources</h2>

<ul class="sources-list">
    <li><a href="https://mydss.mo.gov" target="_blank" rel="noopener">Missouri Department of Social Services: MO HealthNet / Medicaid Eligibility and Applications</a></li>
    <li><a href="https://insurance.mo.gov" target="_blank" rel="noopener">Missouri Department of Commerce and Insurance: Consumer Complaints and Insurance Resources</a></li>
    <li><a href="https://ago.mo.gov/consumer-complaints" target="_blank" rel="noopener">Missouri Attorney General: Consumer Protection Division Complaints</a></li>
    <li><a href="https://www.irs.gov/charities-non-profits/community-health-needs-assessment-for-charitable-hospital-organizations-section-501r3" target="_blank" rel="noopener">IRS: Section 501(r) Requirements for Charitable Hospitals</a></li>
    <li><a href="https://www.cms.gov/nosurprises" target="_blank" rel="noopener">CMS: No Surprises Act &mdash; Patient Protections and Complaint Process</a></li>
    <li><a href="https://revisor.mo.gov/main/OneSection.aspx?section=516.110" target="_blank" rel="noopener">RSMo 516.110: Missouri Statute of Limitations &mdash; Written Contracts (10 years)</a></li>
    <li><a href="https://www.kff.org/medicaid/state-indicator/medicaid-income-eligibility-limits-for-adults-at-application/" target="_blank" rel="noopener">KFF: Medicaid Income Eligibility Limits for Adults by State (2026)</a></li>
</ul>
""",
})
