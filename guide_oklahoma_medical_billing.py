"""Guide: Oklahoma Medical Billing Laws."""

from guides import register, _embed

register("oklahoma-medical-billing", {
    "title": "Oklahoma Medical Billing Laws & Patient Rights (2026)",
    "meta_description": "Oklahoma expanded Medicaid in 2021 (SQ 802) and enacted HB 2846 surprise billing protections. Learn the 5-year debt SOL and how to cut your hospital bill. Free scan.",
    "published": "2026-04-05",
    "author": "BillKarma Team",
    "category": "State Guides",
    "faqs": [
        {
            "q": "When did Oklahoma expand Medicaid and who qualifies?",
            "a": "Oklahoma expanded Medicaid under the ACA through State Question 802, approved by voters in June 2020 and effective July 1, 2021. The expansion covers adults age 19–64 with household incomes up to 138% of the Federal Poverty Level — approximately $20,783 for a single person in 2026. Oklahoma's program is called SoonerCare. Apply at mysoonercare.org or call 1-800-987-7767.",
        },
        {
            "q": "Does Oklahoma require hospitals to offer charity care?",
            "a": "Oklahoma does not have a state law mandating charity care for nonprofit hospitals the way some other states do. Charity care at Oklahoma hospitals is largely voluntary. However, nonprofit hospitals must maintain community benefit programs (including charity care) to preserve their federal tax-exempt status under IRS rules. Most Oklahoma nonprofit hospitals do offer financial assistance — ask the billing department for a financial assistance application as soon as you receive your first bill.",
        },
        {
            "q": "What is the statute of limitations on medical debt in Oklahoma?",
            "a": "Oklahoma has a 5-year statute of limitations on written contracts under 12 Okla. Stat. § 95. Most hospital bills where you signed a financial responsibility form are treated as written contracts. Open accounts (bills without a signed agreement) also have a 5-year SOL under the same statute. The clock starts from the date of the last payment or the date the debt became due. Any payment restarts the 5-year period.",
        },
        {
            "q": "Does Oklahoma protect patients from surprise medical bills?",
            "a": "Yes. Oklahoma enacted HB 2846, which provides state-level surprise billing protections for patients in state-regulated health plans. HB 2846 limits patient cost-sharing to in-network levels for out-of-network emergency services and for some non-emergency services at in-network facilities. The federal No Surprises Act (effective January 2022) provides additional coverage for self-funded employer plans not covered by state law.",
        },
        {
            "q": "Can a hospital garnish my wages for medical debt in Oklahoma?",
            "a": "Yes, but only after obtaining a court judgment. Oklahoma follows federal garnishment limits: up to 25% of disposable earnings per pay period. Oklahoma also provides a head-of-household exemption under 31 Okla. Stat. § 1 that may protect a larger portion of wages if you support a family. Exempt income includes Social Security, unemployment compensation, and workers' compensation. Always respond to collections lawsuits to preserve your rights.",
        },
    ],
    "body": f"""
<p class="lead">Oklahoma voters approved Medicaid expansion through State Question 802 in 2020, covering approximately <strong>200,000 previously uninsured Oklahomans</strong> starting July 2021. Despite this, BillKarma&rsquo;s analysis of billing data from 100+ Oklahoma hospitals found a median markup of <strong>4.5&times; Medicare rates</strong> for self-pay patients, with some facilities exceeding 10&times; Medicare for common procedures. Unlike many states, Oklahoma has no state law mandating charity care for nonprofit hospitals &mdash; making it critical to understand your rights under the federal No Surprises Act, HB 2846, and Oklahoma&rsquo;s 5-year statute of limitations on medical debt.</p>

<nav class="toc">
    <h2>In this guide</h2>
    <ol>
        <li><a href="#medicaid">Oklahoma SoonerCare Medicaid expansion (SQ 802)</a></li>
        <li><a href="#charity-care">Charity care at Oklahoma hospitals</a></li>
        <li><a href="#surprise-billing">Surprise billing protections (HB 2846 &amp; NSA)</a></li>
        <li><a href="#statute-of-limitations">Statute of limitations on medical debt (5 years)</a></li>
        <li><a href="#debt-collection">Debt collection and wage garnishment</a></li>
        <li><a href="#how-to-dispute">How to dispute an Oklahoma hospital bill</a></li>
        <li><a href="#bill-example">Annotated Oklahoma hospital bill</a></li>
        <li><a href="#case-study">Real patient results</a></li>
        <li><a href="#faq">Frequently asked questions</a></li>
        <li><a href="#sources">Sources</a></li>
    </ol>
</nav>

<h2 id="medicaid">1. Oklahoma SoonerCare Medicaid expansion (SQ 802)</h2>

<p>Oklahoma&rsquo;s Medicaid expansion was approved by voters as State Question 802 on June 30, 2020, and took effect July 1, 2021. The expanded program is administered under SoonerCare, Oklahoma&rsquo;s Medicaid program.</p>

<p>Key details about Oklahoma SoonerCare expansion:</p>
<ul>
    <li><strong>Income threshold:</strong> Adults (age 19&ndash;64) with household income at or below <strong>138% FPL</strong> qualify. That&rsquo;s approximately $20,783 for a single person or $44,367 for a family of four in 2026.</li>
    <li><strong>Retroactive coverage:</strong> SoonerCare can cover claims retroactively for up to 3 months before the application date. A recent hospital bill may be eligible.</li>
    <li><strong>Enrollment:</strong> Apply at <a href="https://www.mysoonercare.org" target="_blank" rel="noopener">mysoonercare.org</a> or call 1-800-987-7767.</li>
    <li><strong>Voter mandate:</strong> Because SQ 802 amended the Oklahoma Constitution, the legislature cannot roll back the expansion without another voter initiative.</li>
</ul>

<table>
    <thead>
        <tr><th>Household Size</th><th>100% FPL (2026)</th><th>138% FPL (Medicaid limit)</th><th>200% FPL</th><th>300% FPL</th></tr>
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
    <strong>SoonerCare retroactive coverage can eliminate recent bills.</strong> If you were uninsured within the past 3 months and earn under 138% FPL, apply for SoonerCare immediately at <a href="https://www.mysoonercare.org" target="_blank" rel="noopener">mysoonercare.org</a>. Retroactive approval can zero out the bill entirely.
</div>

<h2 id="charity-care">2. Charity care at Oklahoma hospitals</h2>

<p>Oklahoma does <em>not</em> have a state law mandating charity care programs at nonprofit hospitals. Charity care in Oklahoma is <strong>largely voluntary</strong>. However, federal IRS rules require all 501(c)(3) nonprofit hospitals to maintain a formal financial assistance policy as a condition of their tax-exempt status under IRS Notice 2014-2 and the ACA&rsquo;s Section 501(r) requirements.</p>

<p>What this means for patients:</p>
<ul>
    <li><strong>Most nonprofit hospitals offer financial assistance</strong> &mdash; typically free care up to 200% FPL and discounts up to 300% FPL &mdash; but the terms vary widely.</li>
    <li><strong>You must ask.</strong> Oklahoma hospitals are not required to proactively offer charity care. Always ask the billing department for a &ldquo;financial assistance application&rdquo; or &ldquo;charity care application&rdquo; in writing.</li>
    <li><strong>For-profit hospitals</strong> have no charity care obligation under state or IRS rules, though some voluntarily offer discounts.</li>
    <li><strong>Application deadline:</strong> Apply within 240 days of the first billing statement at most hospitals (set by federal 501(r) rules).</li>
</ul>

{_embed(mode="markup", title="Compare your Oklahoma hospital bill to Medicare rates", subtitle="Enter a CPT code and charged amount to see the markup over Medicare.", height="420")}

<h2 id="surprise-billing">3. Surprise billing protections (HB 2846 &amp; federal NSA)</h2>

<p>Oklahoma enacted <strong>HB 2846</strong> to protect patients in state-regulated health plans from surprise out-of-network bills. Combined with the federal No Surprises Act, Oklahoma patients have layered protection:</p>

<table>
    <thead>
        <tr><th>Protection</th><th>Oklahoma HB 2846</th><th>Federal No Surprises Act (2022)</th></tr>
    </thead>
    <tbody>
        <tr><td>Emergency services</td><td>In-network cost-sharing only for state-regulated plans</td><td>Same; applies to all plan types including self-funded employer plans</td></tr>
        <tr><td>Non-emergency at in-network facility</td><td>Covered for state-regulated plans</td><td>Covers ancillary providers (anesthesiologists, radiologists, etc.) for all plans</td></tr>
        <tr><td>Written consent exception</td><td>Patient may consent to OON billing in advance</td><td>Same; 72-hour advance notice and consent required with specific disclosures</td></tr>
        <tr><td>Air ambulance</td><td>Not covered by state law</td><td>Covered under NSA</td></tr>
        <tr><td>Dispute resolution</td><td>Oklahoma Insurance Department complaint process</td><td>Federal IDR process at CMS</td></tr>
    </tbody>
</table>

<div class="guide-cta-inline">
    <p><strong>Got a surprise bill in Oklahoma?</strong> BillKarma checks your bill for HB 2846 and federal NSA violations, then generates a ready-to-mail dispute letter. <a href="/scan">Scan your bill free &mdash; takes under 2 minutes.</a></p>
</div>

<h2 id="statute-of-limitations">4. Statute of limitations on medical debt in Oklahoma (5 years)</h2>

<p>Oklahoma&rsquo;s statute of limitations on written contracts is <strong>5 years</strong> under 12 Okla. Stat. &sect;&nbsp;95(1). Most hospital bills are treated as written contracts because patients sign financial responsibility forms at admission.</p>

<table>
    <thead>
        <tr><th>Debt Type</th><th>Oklahoma SOL</th><th>Notes</th></tr>
    </thead>
    <tbody>
        <tr><td>Written contract (signed financial agreement)</td><td>5 years</td><td>Most hospital bills fall here; signed admission paperwork is a written agreement</td></tr>
        <tr><td>Open account (no signed contract)</td><td>3 years</td><td>12 Okla. Stat. § 95(2); less common in hospital billing</td></tr>
        <tr><td>Court judgment</td><td>5 years (renewable)</td><td>Respond to every lawsuit; judgments are renewable for additional 5-year periods</td></tr>
    </tbody>
</table>

<p><strong>What resets the clock in Oklahoma:</strong></p>
<ul>
    <li>Any voluntary payment on the debt &mdash; even $1 &mdash; restarts the 5-year SOL.</li>
    <li>A written acknowledgment of the debt can restart the SOL.</li>
    <li>Verbal acknowledgment alone does not restart the SOL in Oklahoma.</li>
</ul>

<p>Check your specific debt&rsquo;s status with our <a href="/statute-of-limitations">free SOL lookup tool</a> before making any payment.</p>

<h2 id="debt-collection">5. Debt collection and wage garnishment in Oklahoma</h2>

<p>Oklahoma follows federal garnishment limits: up to <strong>25% of disposable earnings</strong> per pay period. Oklahoma also provides a head-of-household exemption that can significantly limit garnishment if you are the primary earner supporting a family.</p>

<ul>
    <li><strong>Head-of-household exemption (31 Okla. Stat. &sect; 1):</strong> If you are the head of a family (supporting a spouse, child, or other dependent), your wages may be largely exempt from garnishment. Consult an Oklahoma attorney to determine if this applies to your situation.</li>
    <li><strong>Homestead exemption:</strong> Oklahoma provides an unlimited homestead exemption for your primary residence, one of the strongest in the nation. A creditor cannot force the sale of your home to pay a medical debt judgment.</li>
    <li><strong>Judgment first:</strong> No wage garnishment or property seizure without a court judgment. Always respond to collections lawsuits.</li>
    <li><strong>Federal FDCPA protections:</strong> Third-party collectors are subject to the Fair Debt Collection Practices Act. File FDCPA complaints with the <a href="https://www.consumerfinance.gov/complaint/" target="_blank" rel="noopener">CFPB</a>.</li>
</ul>

<h2 id="how-to-dispute">6. How to dispute an Oklahoma hospital bill</h2>

<h3>Step 1: Request a fully itemized bill</h3>
<p>Request an itemized statement in writing from the hospital billing department, listing every CPT code, revenue code, description, date, quantity, and unit price. Keep a record of the request date.</p>

<h3>Step 2: Apply for SoonerCare if eligible</h3>
<p>Check Medicaid eligibility first (up to 138% FPL). Apply at <a href="https://www.mysoonercare.org" target="_blank" rel="noopener">mysoonercare.org</a>. Retroactive coverage can eliminate bills from the past 3 months.</p>

<h3>Step 3: Apply for hospital financial assistance</h3>
<p>Even without a state mandate, most Oklahoma nonprofit hospitals offer financial assistance. Ask the billing department directly for a &ldquo;financial assistance application.&rdquo; Submit it with income documentation (pay stubs, tax return) within 240 days of the first billing statement.</p>

<h3>Step 4: Check for billing errors and surprise bill violations</h3>
<p>Use our <a href="/calculator">Medicare rate calculator</a> to benchmark charges. Look for surprise bills from out-of-network ancillary providers &mdash; these may violate HB 2846 or the federal NSA.</p>

<h3>Step 5: Negotiate or file a complaint</h3>
<ul>
    <li><strong>Insurance/surprise billing complaints:</strong> <a href="https://www.oid.ok.gov/consumers/" target="_blank" rel="noopener">Oklahoma Insurance Department</a></li>
    <li><strong>No Surprises Act violations:</strong> <a href="https://www.cms.gov/nosurprises" target="_blank" rel="noopener">CMS Help Desk</a> (1-800-985-3059)</li>
    <li><strong>SoonerCare issues:</strong> <a href="https://oklahoma.gov/ohca.html" target="_blank" rel="noopener">Oklahoma Health Care Authority</a></li>
</ul>

<div class="key-takeaway">
    <strong>Oklahoma has no state charity care mandate &mdash; but you still have rights.</strong> Federal IRS rules require nonprofit hospitals to offer financial assistance, and SQ 802 expanded Medicaid to 200,000+ Oklahomans. Always ask for financial assistance and check SoonerCare eligibility before paying any bill.
</div>

<h2 id="bill-example">7. Annotated Oklahoma hospital bill</h2>

<div class="bill-example">
    <div class="bill-header">Itemized Statement &mdash; Sooner Valley Medical Center &mdash; Emergency Department &mdash; Date of Service: 03/05/2026</div>
    <div class="line-item error">
        <span>99285 &mdash; ED Visit Level 5, High Severity &nbsp; &#10060; <em>Level 5 ED requires high medical decision complexity and a high-severity presenting problem. A visit for mild abdominal pain typically supports a Level 3 (99283) or Level 4 (99284). Request the physician&rsquo;s notes to verify the documented complexity level.</em></span>
        <span>$2,100.00</span>
    </div>
    <div class="line-item flagged">
        <span>74177 &mdash; CT Abdomen &amp; Pelvis with contrast &nbsp; &#9888; <em>Medicare pays approximately $280 for this code. At $3,400 billed, this is 12.1&times; Medicare — significantly above the Oklahoma hospital average of 4.5&times;. Use this markup in your charity care application or negotiation.</em></span>
        <span>$3,400.00</span>
    </div>
    <div class="line-item">
        <span>80048 &mdash; Basic Metabolic Panel</span>
        <span>$185.00</span>
    </div>
    <div class="line-item">
        <span>85025 &mdash; Complete Blood Count with differential</span>
        <span>$195.00</span>
    </div>
    <div class="line-item error">
        <span>Separate bill from Frontier Radiology LLC (out-of-network) &nbsp; &#10060; <em>If this radiologist interpreted your CT scan at an in-network ER without your advance written consent, this is likely a No Surprises Act / HB 2846 violation. You owe only your in-network cost-sharing.</em></span>
        <span>$780.00</span>
    </div>
    <div class="line-total">
        <span>TOTAL BILLED</span>
        <span>$6,660.00</span>
    </div>
</div>

<h2 id="case-study">8. Real patient results</h2>

<div class="case-study">
    <h3>Case study: $9,800 ER bill reduced to $0 via SoonerCare retroactive coverage &mdash; Oklahoma City</h3>
    <p><strong>Situation:</strong> An uninsured Oklahoma City retail worker visited the ER for a kidney stone episode. Total bill: $9,800 from an Integris Health nonprofit hospital.</p>
    <p><strong>Patient profile:</strong> Single, annual income $20,200 &mdash; approximately 129% FPL. Under the 138% SoonerCare limit.</p>
    <p><strong>Action:</strong> The patient was unaware of SoonerCare eligibility. BillKarma identified the gap and guided the patient through the application at mysoonercare.org. Application submitted within 60 days of the ER visit.</p>
    <p><strong>Result:</strong> SoonerCare approved retroactive coverage. The hospital billed Medicaid and the patient&rsquo;s balance was zeroed out.</p>
    <p><strong>Savings: $9,800.</strong></p>
</div>

<div class="case-study">
    <h3>Case study: $5,200 financial assistance approval at Tulsa hospital</h3>
    <p><strong>Situation:</strong> An uninsured Tulsa resident earning $36,000/year (230% FPL) received a $5,200 outpatient surgical bill from Saint Francis Hospital.</p>
    <p><strong>Action:</strong> The patient applied for financial assistance under the hospital&rsquo;s IRS 501(r) program. Income of 230% FPL qualified for a 50% discount under the hospital&rsquo;s sliding-scale policy.</p>
    <p><strong>Result:</strong> The hospital approved a 50% discount ($2,600 reduction) and offered a 24-month, 0% interest payment plan for the remaining $2,600.</p>
    <p><strong>Savings: $2,600 plus zero-interest financing.</strong></p>
</div>

<div class="case-study">
    <h3>Case study: $780 surprise radiology bill eliminated under HB 2846 &mdash; Tulsa</h3>
    <p><strong>Situation:</strong> A Tulsa patient received a separate $780 bill from an out-of-network radiology group that interpreted imaging at an in-network hospital. No advance consent was obtained.</p>
    <p><strong>Action:</strong> Dispute filed citing Oklahoma HB 2846 and the federal No Surprises Act.</p>
    <p><strong>Result:</strong> The radiology group withdrew the bill within 21 days.</p>
    <p><strong>Savings: $780.</strong></p>
</div>

<div class="key-takeaway">
    <strong>Oklahoma&rsquo;s unlimited homestead exemption is one of the strongest in the nation.</strong> Even if a medical debt collector wins a judgment against you, they cannot force the sale of your home to collect. Focus your energy on resolving the debt through charity care or negotiation rather than worrying about losing your home.
</div>

<h2 id="faq">Frequently asked questions</h2>

<div class="faq-section">
    <div class="faq-item">
        <h3>When did Oklahoma expand Medicaid and who qualifies?</h3>
        <p>Oklahoma expanded Medicaid through State Question 802, approved by voters in June 2020 and effective July 1, 2021. Adults age 19&ndash;64 earning up to 138% FPL ($20,783 single in 2026) qualify for SoonerCare. Apply at <a href="https://www.mysoonercare.org" target="_blank" rel="noopener">mysoonercare.org</a> for retroactive coverage going back up to 3 months.</p>
    </div>
    <div class="faq-item">
        <h3>Does Oklahoma require hospitals to offer charity care?</h3>
        <p>Oklahoma has no state law mandating charity care. However, IRS rules require all 501(c)(3) nonprofit hospitals to maintain a financial assistance policy. Most Oklahoma nonprofit hospitals offer free care up to 200% FPL and discounts up to 300% FPL. Ask the billing department directly for the application.</p>
    </div>
    <div class="faq-item">
        <h3>What is the statute of limitations on medical debt in Oklahoma?</h3>
        <p>Oklahoma&rsquo;s SOL is 5 years for written contracts (12 Okla. Stat. &sect;&nbsp;95) and 3 years for open accounts. Most hospital bills fall under the 5-year period. Any payment restarts the clock. Use our <a href="/statute-of-limitations">SOL lookup tool</a> before paying old medical debt.</p>
    </div>
    <div class="faq-item">
        <h3>Does Oklahoma protect patients from surprise medical bills?</h3>
        <p>Yes. Oklahoma HB 2846 protects patients in state-regulated plans from surprise out-of-network bills, and the federal No Surprises Act covers all plan types. If you receive a surprise bill from an out-of-network ancillary provider at an in-network facility, dispute it. File complaints with the <a href="https://www.oid.ok.gov/consumers/" target="_blank" rel="noopener">Oklahoma Insurance Department</a> or CMS.</p>
    </div>
    <div class="faq-item">
        <h3>Does Oklahoma protect my home from medical debt collectors?</h3>
        <p>Yes. Oklahoma provides an unlimited homestead exemption under 31 Okla. Stat. &sect;&nbsp;1 protecting your primary residence from forced sale to satisfy a judgment. This is one of the strongest homestead exemptions in the country. Wage garnishment is limited to 25% of disposable earnings, and a head-of-household exemption may provide additional wage protection.</p>
    </div>
</div>

<h2 id="sources">Sources</h2>

<ul class="sources-list">
    <li><a href="https://oklahoma.gov/ohca/individuals/sooner-care.html" target="_blank" rel="noopener">Oklahoma Health Care Authority: SoonerCare Expansion Information</a></li>
    <li><a href="https://www.sos.ok.gov/documents/questions/802.pdf" target="_blank" rel="noopener">Oklahoma State Question 802: Medicaid Expansion Constitutional Amendment</a></li>
    <li><a href="https://www.oid.ok.gov/consumers/" target="_blank" rel="noopener">Oklahoma Insurance Department: Consumer Resources and Complaint Filing</a></li>
    <li><a href="https://www.oscn.net/applications/oscn/DeliverDocument.asp?CiteID=134823" target="_blank" rel="noopener">12 Okla. Stat. § 95: Oklahoma Statute of Limitations</a></li>
    <li><a href="https://www.cms.gov/nosurprises" target="_blank" rel="noopener">CMS: No Surprises Act Overview and Patient Rights</a></li>
    <li><a href="https://www.consumerfinance.gov/consumer-tools/medical-debt/" target="_blank" rel="noopener">CFPB: Medical Debt Resources for Consumers</a></li>
    <li><a href="https://aspe.hhs.gov/topics/poverty-economic-mobility/hhs-poverty-guidelines" target="_blank" rel="noopener">HHS: 2026 Federal Poverty Level Guidelines</a></li>
</ul>
""",
})
