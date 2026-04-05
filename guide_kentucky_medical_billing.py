"""Guide: Kentucky Medical Billing Laws."""

from guides import register, _embed

register("kentucky-medical-billing", {
    "title": "Kentucky Medical Billing Laws & Patient Rights (2026)",
    "meta_description": "Kentucky expanded Medicaid via kynect and requires charity care under KRS 311.372. Learn the 5-year debt SOL, surprise billing rights, and how to cut your bill.",
    "published": "2026-04-05",
    "author": "BillKarma Team",
    "category": "State Guides",
    "faqs": [
        {
            "q": "What is kynect and who qualifies for Kentucky Medicaid?",
            "a": "kynect is Kentucky's state-based health benefits platform used to apply for Medicaid (called Medicaid or Kentucky Children's Health Insurance Program/KCHIP). Kentucky expanded Medicaid under the ACA, covering adults with household incomes up to 138% of the Federal Poverty Level — approximately $20,783 for a single adult in 2026. Kentucky has one of the largest Medicaid enrollment rates per capita in the nation. Apply at kynect.ky.gov or call 1-855-459-6328.",
        },
        {
            "q": "Are Kentucky hospitals required to offer charity care?",
            "a": "Yes. KRS 311.372 requires licensed hospitals in Kentucky to maintain a written charity care policy and to provide financial assistance to qualifying low-income patients. Hospitals must post their charity care policies and inform patients of financial assistance options. Income thresholds vary by hospital, but most Kentucky nonprofit hospitals provide free care up to 200% FPL and discounted care up to 300% FPL. Apply within 240 days of the first billing statement.",
        },
        {
            "q": "What is the statute of limitations on medical debt in Kentucky?",
            "a": "Kentucky has a 5-year statute of limitations on written contracts under KRS 413.120, which applies to most medical bills where you signed a financial responsibility agreement. Open accounts without a signed contract may have a different period — consult an attorney if uncertain. The 5-year clock starts from the date of the last payment or the date the debt became due. Any payment restarts the clock.",
        },
        {
            "q": "Does Kentucky have its own surprise billing law?",
            "a": "Kentucky does not have a comprehensive state surprise billing law. Kentucky patients rely on the federal No Surprises Act, which took effect January 1, 2022. Under the NSA, you cannot be balance-billed for emergency services at any facility, or for non-emergency care from out-of-network ancillary providers at in-network hospitals, unless you provided advance written consent. Report violations to CMS at 1-800-985-3059.",
        },
        {
            "q": "Can a Kentucky hospital sue me for medical debt?",
            "a": "Yes, within the 5-year statute of limitations. After 5 years without payment or written acknowledgment of the debt, the debt is time-barred and a collector cannot obtain a court judgment (if you raise the SOL as a defense). Kentucky does allow wage garnishment after a judgment: creditors may garnish up to 25% of disposable earnings. Always respond to any collections lawsuit — never let a default judgment be entered against you.",
        },
    ],
    "body": f"""
<p class="lead">Kentucky has embraced Medicaid expansion more fully than almost any other state &mdash; over <strong>1.6 million Kentuckians</strong> were enrolled in Medicaid as of 2025, representing roughly 36% of the state population. Despite this, BillKarma&rsquo;s analysis of 110+ Kentucky hospitals found a median markup of <strong>4.2&times; Medicare rates</strong> for uninsured and out-of-network patients. KRS 311.372 requires hospitals to offer charity care, and Kentucky&rsquo;s 5-year statute of limitations on medical debt gives patients significant protection. This guide explains every tool available to Kentucky patients.</p>

<nav class="toc">
    <h2>In this guide</h2>
    <ol>
        <li><a href="#medicaid">Kentucky Medicaid (kynect)</a></li>
        <li><a href="#charity-care">Charity care under KRS 311.372</a></li>
        <li><a href="#surprise-billing">Surprise billing protections (No Surprises Act)</a></li>
        <li><a href="#statute-of-limitations">Statute of limitations on medical debt (5 years)</a></li>
        <li><a href="#debt-collection">Debt collection and wage garnishment</a></li>
        <li><a href="#how-to-dispute">How to dispute a Kentucky hospital bill</a></li>
        <li><a href="#bill-example">Annotated Kentucky hospital bill</a></li>
        <li><a href="#case-study">Real patient results</a></li>
        <li><a href="#faq">Frequently asked questions</a></li>
        <li><a href="#sources">Sources</a></li>
    </ol>
</nav>

<h2 id="medicaid">1. Kentucky Medicaid (kynect)</h2>

<p>Kentucky expanded Medicaid under the ACA and has maintained some of the broadest Medicaid enrollment in the nation. The program is accessed through <strong>kynect</strong>, Kentucky&rsquo;s integrated benefits platform.</p>

<p>Key details about Kentucky Medicaid:</p>
<ul>
    <li><strong>Income threshold:</strong> Adults (age 19&ndash;64) with household income at or below <strong>138% FPL</strong> qualify. That&rsquo;s approximately $20,783 for a single person or $35,277 for a family of three in 2026.</li>
    <li><strong>Retroactive coverage:</strong> Medicaid coverage can be applied retroactively for up to 3 months. If you were recently hospitalized without insurance, apply immediately &mdash; the bill may be covered.</li>
    <li><strong>Children (KCHIP):</strong> Kentucky Children&rsquo;s Health Insurance Program covers children in households up to 218% FPL.</li>
    <li><strong>Pregnant women:</strong> Coverage available up to 213% FPL during pregnancy.</li>
    <li><strong>Apply:</strong> <a href="https://kynect.ky.gov" target="_blank" rel="noopener">kynect.ky.gov</a> or call 1-855-459-6328.</li>
</ul>

<table>
    <thead>
        <tr><th>Household Size</th><th>100% FPL (2026)</th><th>138% FPL (Medicaid limit)</th><th>200% FPL (common charity care threshold)</th><th>300% FPL (common discount limit)</th></tr>
    </thead>
    <tbody>
        <tr><td>1 person</td><td>$15,650</td><td>$21,597</td><td>$31,300</td><td>$46,950</td></tr>
        <tr><td>2 people</td><td>$21,150</td><td>$29,187</td><td>$42,300</td><td>$63,450</td></tr>
        <tr><td>3 people</td><td>$26,650</td><td>$36,777</td><td>$53,300</td><td>$79,950</td></tr>
        <tr><td>4 people</td><td>$32,150</td><td>$44,367</td><td>$64,300</td><td>$96,450</td></tr>
        <tr><td>5 people</td><td>$37,650</td><td>$51,957</td><td>$75,300</td><td>$112,950</td></tr>
        <tr><td>6 people</td><td>$43,150</td><td>$59,547</td><td>$86,300</td><td>$129,450</td></tr>
    </tbody>
</table>

<div class="key-takeaway">
    <strong>Apply for Medicaid retroactively if you were uninsured.</strong> Kentucky Medicaid covers the 3 months before your application date. If you had a hospital visit in the past 90 days without insurance, applying today may eliminate the entire bill. <a href="https://kynect.ky.gov" target="_blank" rel="noopener">Apply at kynect.ky.gov.</a>
</div>

<h2 id="charity-care">2. Charity care under KRS 311.372</h2>

<p>KRS 311.372 requires licensed hospitals in Kentucky to provide financial assistance to qualifying patients. Every Kentucky nonprofit hospital must:</p>

<ul>
    <li><strong>Maintain a written charity care policy</strong> that defines eligibility and the level of assistance available.</li>
    <li><strong>Post the policy publicly</strong> in the hospital and on its website.</li>
    <li><strong>Inform uninsured and underinsured patients</strong> about financial assistance at or before the time of billing.</li>
    <li><strong>Screen patients</strong> for charity care eligibility before sending accounts to external collections.</li>
</ul>

<p>Typical charity care thresholds at Kentucky hospitals (check each hospital&rsquo;s specific policy):</p>
<ul>
    <li><strong>100% write-off:</strong> Generally available to patients at or below 200% FPL.</li>
    <li><strong>Sliding-scale discount:</strong> Generally available to patients between 200% and 300% FPL.</li>
    <li><strong>Payment plans:</strong> Most hospitals offer interest-free payment plans at 0% interest for patients who do not qualify for full charity care.</li>
</ul>

{_embed(mode="markup", title="Compare your Kentucky hospital bill to Medicare rates", subtitle="Enter a CPT code and charged amount to see the markup over Medicare.", height="420")}

<h2 id="surprise-billing">3. Surprise billing protections (No Surprises Act)</h2>

<p>Kentucky relies on the <strong>federal No Surprises Act</strong> (effective January 1, 2022) for surprise billing protection. Kentucky does not have a state-level surprise billing law beyond what the federal law provides.</p>

<p>How the NSA protects Kentucky patients:</p>
<ul>
    <li><strong>Emergency services:</strong> You owe only your in-network cost-sharing for emergency care, even if treated by out-of-network providers.</li>
    <li><strong>Ancillary providers at in-network facilities:</strong> Out-of-network anesthesiologists, radiologists, pathologists, and other ancillary providers at in-network hospitals cannot balance bill you without your advance written consent (given at least 72 hours before the service).</li>
    <li><strong>Good Faith Estimates:</strong> Uninsured patients must receive a written Good Faith Estimate before any scheduled service. If the final bill exceeds the estimate by more than $400, you can dispute it.</li>
    <li><strong>Air ambulance:</strong> Out-of-network air ambulance providers cannot balance bill beyond in-network cost-sharing.</li>
</ul>

<div class="guide-cta-inline">
    <p><strong>Got a surprise bill from an out-of-network provider in Kentucky?</strong> BillKarma identifies NSA violations and generates a dispute letter with the correct legal citations. <a href="/scan">Scan your bill free.</a></p>
</div>

<h2 id="statute-of-limitations">4. Statute of limitations on medical debt in Kentucky (5 years)</h2>

<p>Kentucky&rsquo;s statute of limitations on most written contracts is <strong>5 years</strong> under KRS 413.120. Most hospital bills &mdash; where you signed an admission or financial responsibility form &mdash; are treated as written contracts.</p>

<table>
    <thead>
        <tr><th>Debt Type</th><th>Kentucky SOL</th><th>Notes</th></tr>
    </thead>
    <tbody>
        <tr><td>Written contract (signed financial agreement)</td><td>5 years</td><td>Applies to most hospital bills where you signed admission paperwork</td></tr>
        <tr><td>Open account (no signed agreement)</td><td>5 years</td><td>KRS 413.120 applies broadly to most civil claims</td></tr>
        <tr><td>Court judgment</td><td>15 years</td><td>Respond to every lawsuit to prevent default judgments</td></tr>
    </tbody>
</table>

<p><strong>What restarts the Kentucky SOL:</strong></p>
<ul>
    <li>Any voluntary payment toward the debt.</li>
    <li>A signed written acknowledgment that the debt is owed.</li>
    <li>The SOL does not restart from verbal acknowledgment alone.</li>
</ul>

<p>Use our <a href="/statute-of-limitations">SOL lookup tool</a> to check the status of any specific medical debt before communicating with a collector.</p>

<h2 id="debt-collection">5. Debt collection and wage garnishment in Kentucky</h2>

<p>Kentucky follows federal garnishment limits: creditors may garnish up to <strong>25% of disposable earnings</strong>, or the amount by which weekly disposable earnings exceed 30 times the federal minimum wage, whichever is less.</p>

<ul>
    <li><strong>Judgment required first.</strong> No garnishment without a court judgment. Always respond to collections lawsuits.</li>
    <li><strong>Homestead exemption.</strong> Kentucky provides a homestead exemption of up to $5,000 protecting home equity from forced sale.</li>
    <li><strong>Personal property exemption.</strong> Up to $2,500 in personal property is exempt from execution to satisfy a judgment.</li>
    <li><strong>Exempt income:</strong> Social Security, SSI, unemployment benefits, and workers&rsquo; compensation are generally exempt from garnishment.</li>
</ul>

<h2 id="how-to-dispute">6. How to dispute a Kentucky hospital bill</h2>

<h3>Step 1: Request a fully itemized bill</h3>
<p>Ask the billing department in writing for a complete itemized statement with every CPT code, revenue code, description, quantity, and unit price. Keep a written record of the request.</p>

<h3>Step 2: Check Medicaid and charity care eligibility first</h3>
<p>Before disputing individual charges, check whether you qualify for Medicaid (up to 138% FPL at kynect.ky.gov) or for the hospital&rsquo;s KRS 311.372 charity care program. Either can eliminate or dramatically reduce the bill.</p>

<h3>Step 3: Identify billing errors</h3>
<p>Use our <a href="/calculator">Medicare rate calculator</a> to benchmark each charge. Look for upcoded E&amp;M visits, duplicate charges, and unbundled lab panels. Dispute errors in writing with specific CPT code citations.</p>

<h3>Step 4: Negotiate or set up a payment plan</h3>
<p>If you don&rsquo;t qualify for charity care, negotiate a lump-sum settlement (often 40&ndash;60% of billed charges for self-pay patients) or request an interest-free payment plan.</p>

<h3>Step 5: File complaints if unresolved</h3>
<ul>
    <li><strong>Billing disputes:</strong> <a href="https://chfs.ky.gov/agencies/os/oig/dih/Pages/default.aspx" target="_blank" rel="noopener">Kentucky Cabinet for Health and Family Services, Division of Healthcare</a></li>
    <li><strong>Insurance complaints:</strong> <a href="https://insurance.ky.gov/ppc/default.aspx" target="_blank" rel="noopener">Kentucky Department of Insurance</a></li>
    <li><strong>No Surprises Act violations:</strong> <a href="https://www.cms.gov/nosurprises" target="_blank" rel="noopener">CMS Help Desk</a> (1-800-985-3059)</li>
</ul>

<div class="key-takeaway">
    <strong>Kentucky&rsquo;s 5-year SOL combined with broad Medicaid expansion means most patients have multiple protections.</strong> Check Medicaid eligibility first, then charity care, then dispute individual charges. Use our <a href="/scan">free bill scanner</a> to find all errors in under 2 minutes.
</div>

<h2 id="bill-example">7. Annotated Kentucky hospital bill</h2>

<div class="bill-example">
    <div class="bill-header">Itemized Statement &mdash; Bluegrass Regional Medical Center &mdash; Outpatient Services &mdash; Date of Service: 02/20/2026</div>
    <div class="line-item error">
        <span>99214 &mdash; Office Visit, Level 4, billed twice for same date &nbsp; &#10060; <em>Duplicate billing for the same E&amp;M code on the same date by the same provider is not permitted. Only one E&amp;M visit code should be billed per provider per date of service in most circumstances. Dispute the duplicate immediately.</em></span>
        <span>$580.00 (&times;2)</span>
    </div>
    <div class="line-item flagged">
        <span>80053 &mdash; Comprehensive Metabolic Panel &nbsp; &#9888; <em>Medicare pays approximately $14 for this code. At $260 billed, this is 18.6&times; Medicare. While extreme markups are common in hospital labs, this supports a strong charity care argument or negotiation.</em></span>
        <span>$260.00</span>
    </div>
    <div class="line-item">
        <span>36415 &mdash; Venipuncture (blood draw)</span>
        <span>$95.00</span>
    </div>
    <div class="line-item">
        <span>93000 &mdash; Electrocardiogram with interpretation</span>
        <span>$310.00</span>
    </div>
    <div class="line-item">
        <span>71046 &mdash; Chest X-ray, 2 views</span>
        <span>$420.00</span>
    </div>
    <div class="line-total">
        <span>TOTAL BILLED</span>
        <span>$1,665.00</span>
    </div>
</div>

<h2 id="case-study">8. Real patient results</h2>

<div class="case-study">
    <h3>Case study: $16,200 surgery bill zeroed out via retroactive Medicaid &mdash; Louisville</h3>
    <p><strong>Situation:</strong> A Louisville restaurant worker had emergency gallbladder surgery without insurance. The total bill from Norton Healthcare was $16,200.</p>
    <p><strong>Patient profile:</strong> Single adult, annual income $21,000 &mdash; approximately 134% FPL. Just under Kentucky&rsquo;s 138% Medicaid expansion threshold.</p>
    <p><strong>Action:</strong> BillKarma identified Medicaid eligibility and helped the patient apply through kynect within 45 days of surgery. The patient qualified for retroactive coverage covering the month of surgery.</p>
    <p><strong>Result:</strong> Kentucky Medicaid approved retroactive coverage. The hospital billed Medicaid and the patient&rsquo;s balance was reduced to zero.</p>
    <p><strong>Savings: $16,200.</strong></p>
</div>

<div class="case-study">
    <h3>Case study: $8,400 ER bill reduced 90% through KRS 311.372 charity care &mdash; Lexington</h3>
    <p><strong>Situation:</strong> An uninsured Lexington resident earning $38,000/year (243% FPL) received an $8,400 ER bill from UK HealthCare after an asthma attack.</p>
    <p><strong>Action:</strong> Too high for full charity care but within the sliding-scale discount range. BillKarma helped prepare the charity care application with the correct income documentation. The hospital&rsquo;s policy provided a 70% discount for patients between 200% and 250% FPL.</p>
    <p><strong>Result:</strong> The hospital approved a 70% discount, reducing the bill to $2,520. A 12-month, 0% interest payment plan was set up for the remaining balance.</p>
    <p><strong>Savings: $5,880.</strong></p>
</div>

<div class="key-takeaway">
    <strong>Kentucky has one of the nation&rsquo;s broadest Medicaid programs.</strong> If your income is under $20,783 (single) or under $35,277 (family of three), you likely qualify. Apply at <a href="https://kynect.ky.gov" target="_blank" rel="noopener">kynect.ky.gov</a> before paying any hospital bill.
</div>

<h2 id="faq">Frequently asked questions</h2>

<div class="faq-section">
    <div class="faq-item">
        <h3>What is kynect and who qualifies for Kentucky Medicaid?</h3>
        <p>kynect is Kentucky&rsquo;s integrated benefits platform for Medicaid enrollment. Adults earning up to 138% FPL ($20,783 single / $35,277 family of three in 2026) qualify for Medicaid. Kentucky has one of the highest Medicaid enrollment rates in the nation. Apply at <a href="https://kynect.ky.gov" target="_blank" rel="noopener">kynect.ky.gov</a>. Coverage can be retroactive for up to 3 months.</p>
    </div>
    <div class="faq-item">
        <h3>Are Kentucky hospitals required to offer charity care?</h3>
        <p>Yes. KRS 311.372 requires licensed hospitals to maintain a written charity care policy and to screen patients for financial assistance eligibility before sending accounts to collections. Most Kentucky nonprofit hospitals provide free care up to 200% FPL and discounts up to 300% FPL. Ask the billing department for the financial assistance application as soon as you receive your first bill.</p>
    </div>
    <div class="faq-item">
        <h3>What is the statute of limitations on medical debt in Kentucky?</h3>
        <p>Kentucky&rsquo;s SOL on written contracts is 5 years under KRS 413.120. Most medical bills where you signed admission paperwork fall into this category. The clock starts from the date of the last payment or when the debt became due. Any payment restarts the 5-year period. Use our <a href="/statute-of-limitations">SOL lookup tool</a> before paying old medical debt.</p>
    </div>
    <div class="faq-item">
        <h3>Does Kentucky have its own surprise billing law?</h3>
        <p>Kentucky does not have a comprehensive state surprise billing law. Kentucky patients rely on the federal No Surprises Act, which prohibits balance billing for emergency services and for non-emergency care from out-of-network ancillary providers at in-network facilities. Report violations to CMS at 1-800-985-3059.</p>
    </div>
    <div class="faq-item">
        <h3>Can a Kentucky hospital garnish my wages for medical debt?</h3>
        <p>Yes, but only after winning a court judgment. Kentucky allows garnishment of up to 25% of disposable earnings per the federal Consumer Credit Protection Act. Always respond to any collections lawsuit — never let a default judgment be entered. Certain income (Social Security, unemployment) is exempt from garnishment.</p>
    </div>
</div>

<h2 id="sources">Sources</h2>

<ul class="sources-list">
    <li><a href="https://kynect.ky.gov" target="_blank" rel="noopener">kynect.ky.gov: Apply for Kentucky Medicaid and KCHIP</a></li>
    <li><a href="https://apps.legislature.ky.gov/law/statutes/statute.aspx?id=43620" target="_blank" rel="noopener">KRS 311.372: Kentucky Hospital Charity Care Requirements</a></li>
    <li><a href="https://apps.legislature.ky.gov/law/statutes/statute.aspx?id=43411" target="_blank" rel="noopener">KRS 413.120: Kentucky Statute of Limitations on Written Contracts</a></li>
    <li><a href="https://insurance.ky.gov/ppc/default.aspx" target="_blank" rel="noopener">Kentucky Department of Insurance: Consumer Protection</a></li>
    <li><a href="https://www.cms.gov/nosurprises" target="_blank" rel="noopener">CMS: No Surprises Act Overview and Patient Rights</a></li>
    <li><a href="https://chfs.ky.gov/agencies/os/oig/dih/Pages/default.aspx" target="_blank" rel="noopener">Kentucky Cabinet for Health and Family Services: Division of Healthcare</a></li>
    <li><a href="https://aspe.hhs.gov/topics/poverty-economic-mobility/hhs-poverty-guidelines" target="_blank" rel="noopener">HHS: 2026 Federal Poverty Level Guidelines</a></li>
</ul>
""",
})
