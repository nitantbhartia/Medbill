"""Guide: Nursing Home Billing Errors."""

from guides import register, _embed

register("nursing-home-billing", {
    "title": "Nursing Home Billing: Common Errors and How to Dispute Them",
    "meta_description": "Nursing homes average $8,929/month. Medicare covers only days 1–100. Learn the most common nursing home billing errors—therapy upcoding, phantom charges—and how to dispute.",
    "published": "2026-04-05",
    "author": "BillKarma Team",
    "category": "Billing Basics",
    "faqs": [
        {
            "q": "How many days does Medicare cover in a nursing home?",
            "a": "Medicare Part A covers up to 100 days per benefit period in a skilled nursing facility (SNF) following a qualifying 3-day inpatient hospital stay. Days 1&ndash;20 are fully covered. Days 21&ndash;100 require a daily copay of $204 (2026). Day 101 and beyond are not covered by Medicare Part A at all. After Medicare ends, Medicaid covers long-term nursing home care for patients who qualify financially.",
        },
        {
            "q": "What is therapy upcoding in nursing home billing?",
            "a": "Therapy upcoding means billing Medicare for more therapy minutes than were actually provided or documented. Under the PDPM (Patient-Driven Payment Model) system, SNFs are paid based on patient characteristics and documented therapy needs. The HHS Office of Inspector General has found therapy upcoding in SNF claims at rates exceeding 25% in some audits. Request the MDS (Minimum Data Set) assessment to verify what therapy was documented.",
        },
        {
            "q": "What are ancillary charges on a nursing home bill?",
            "a": "Ancillary charges are costs beyond the room and board rate, such as medications, medical supplies, incontinence products, and specialty therapies. These should be itemized separately. Common errors include charges for items already included in the daily Medicare rate (the &ldquo;consolidated billing&rdquo; rule), charges for supplies never provided, and personal care items like toiletries billed at grossly inflated prices.",
        },
        {
            "q": "Can I dispute a nursing home bill after discharge?",
            "a": "Yes. You generally have up to 1 year to dispute Medicare claims through the appeals process. For private-pay or Medicaid disputes, the timeframe varies by state. Request an itemized statement and compare it against the Medicare Summary Notice (MSN) you receive after discharge. Discrepancies between what the facility billed and what Medicare paid are a common starting point for disputes.",
        },
        {
            "q": "What is the difference between skilled nursing and custodial care for Medicare coverage?",
            "a": "Medicare Part A only covers &ldquo;skilled nursing care&rdquo; &mdash; care that requires a licensed nurse or therapist, such as wound care, IV medications, or physical therapy. It does not cover &ldquo;custodial care,&rdquo; which is assistance with daily activities like bathing, dressing, and eating. Once a patient&rsquo;s need for skilled care ends, Medicare coverage stops even if the patient remains in the facility.",
        },
    ],
    "body": f"""
<p class="lead">The average nursing home costs <strong>$8,929/month</strong> for a semi-private room and $10,025/month for a private room (Genworth 2025 Cost of Care Survey). Medicare covers only the first 100 days per benefit period &mdash; and only if you received a qualifying 3-day hospital inpatient stay (not observation status). Billing errors in nursing home statements are extremely common: the HHS Office of Inspector General has flagged therapy upcoding in SNF claims at rates exceeding 25% in federal audits. This guide explains how nursing home billing works and how to catch the most common errors.</p>

<nav class="toc">
    <h2>In this guide</h2>
    <ol>
        <li><a href="#medicare-coverage">Medicare SNF coverage: what&rsquo;s actually covered</a></li>
        <li><a href="#bill-breakdown">What&rsquo;s on a nursing home bill</a></li>
        <li><a href="#real-bill">Annotated nursing home statement</a></li>
        <li><a href="#common-errors">7 most common nursing home billing errors</a></li>
        <li><a href="#how-to-audit">How to audit a nursing home bill</a></li>
        <li><a href="#how-to-dispute">How to dispute nursing home charges</a></li>
        <li><a href="#case-studies">Case studies</a></li>
        <li><a href="#faq">Frequently asked questions</a></li>
        <li><a href="#sources">Sources</a></li>
    </ol>
</nav>

<h2 id="medicare-coverage">1. Medicare SNF coverage: what&rsquo;s actually covered</h2>

<p>Medicare Part A covers skilled nursing facility (SNF) care under very specific rules. Understanding these rules is the first step to catching billing errors.</p>

<table>
    <thead>
        <tr><th>Days in SNF</th><th>Medicare Coverage (2026)</th><th>Patient Daily Copay</th><th>What You Owe</th></tr>
    </thead>
    <tbody>
        <tr><td>Days 1&ndash;20</td><td>100% covered</td><td>$0</td><td>Nothing (after qualifying stay)</td></tr>
        <tr><td>Days 21&ndash;100</td><td>Covered after daily copay</td><td>$204/day</td><td>Up to $16,320 total</td></tr>
        <tr><td>Day 101+</td><td>Not covered</td><td>N/A</td><td>Full cost (Medicaid or private pay)</td></tr>
    </tbody>
</table>

<p><strong>The qualifying inpatient stay requirement</strong> is one of the most common billing traps. To qualify for Medicare SNF coverage, you must have been formally admitted as a hospital inpatient (not under &ldquo;observation status&rdquo;) for at least 3 consecutive days. Patients kept under observation status &mdash; even overnight for multiple nights &mdash; do not qualify. This distinction can cost thousands. Read our guide to <a href="/guides/observation-status">observation status billing</a> to understand the difference.</p>

<div class="key-takeaway">
    <strong>Received a nursing home bill you&rsquo;re not sure about?</strong> <a href="/scan">Upload it to BillKarma</a> &mdash; we flag therapy upcoding, duplicate charges, and items that should be included in the daily Medicare rate.
</div>

<h2 id="bill-breakdown">2. What&rsquo;s on a nursing home bill</h2>

<p>Nursing home statements combine several charge categories, each with their own billing rules:</p>

<table>
    <thead>
        <tr><th>Charge Category</th><th>Revenue Code Range</th><th>What It Covers</th><th>Common Error</th></tr>
    </thead>
    <tbody>
        <tr><td>Room &amp; board (semi-private)</td><td>0100&ndash;0119</td><td>Daily room, meals, basic nursing</td><td>Wrong room type billed</td></tr>
        <tr><td>Room &amp; board (private)</td><td>0120&ndash;0139</td><td>Private room, meals, basic nursing</td><td>Private rate billed without consent</td></tr>
        <tr><td>Physical therapy</td><td>0420&ndash;0429</td><td>PT sessions and evaluations</td><td>More minutes billed than provided</td></tr>
        <tr><td>Occupational therapy</td><td>0430&ndash;0439</td><td>OT sessions and evaluations</td><td>Upcoded therapy categories</td></tr>
        <tr><td>Speech therapy</td><td>0440&ndash;0449</td><td>Speech/language pathology</td><td>Sessions billed not in care plan</td></tr>
        <tr><td>Pharmacy/medications</td><td>0250&ndash;0259</td><td>All drugs administered</td><td>Part D drugs billed to Medicare Part A</td></tr>
        <tr><td>Medical supplies</td><td>0270&ndash;0279</td><td>Wound care, catheters, etc.</td><td>Supplies included in per diem billed separately</td></tr>
    </tbody>
</table>

<h2 id="real-bill">3. Annotated nursing home statement</h2>

<p>Here&rsquo;s a sample monthly statement for a Medicare patient in a skilled nursing facility after hip replacement surgery.</p>

<div class="bill-example">
    <div class="bill-header">Monthly Statement &mdash; Sunrise Skilled Nursing &amp; Rehab &mdash; Billing Period: 03/01&ndash;03/31/2026</div>
    <div class="line-item">
        <span>Revenue 0119 &mdash; Semi-private room &amp; board (31 days &times; $485/day)</span>
        <span>$15,035</span>
    </div>
    <div class="line-item flagged">
        <span>Revenue 0420 &mdash; Physical therapy (42 units billed) &nbsp; &#9888; <em>Treatment log shows 28 units provided &mdash; 14 units overbilled</em></span>
        <span>$4,200</span>
    </div>
    <div class="line-item error">
        <span>Revenue 0250 &mdash; Metoprolol 50mg (chronic medication) &nbsp; &#10060; <em>Chronic medications covered under Medicare Part D should not be billed to Part A SNF claim</em></span>
        <span>$340</span>
    </div>
    <div class="line-item error">
        <span>Revenue 0270 &mdash; Wound care supplies (gauze, tape, saline) &nbsp; &#10060; <em>Routine wound care supplies included in per-diem rate &mdash; cannot be billed separately</em></span>
        <span>$280</span>
    </div>
    <div class="line-item flagged">
        <span>Personal hygiene kit (shampoo, soap, lotion) &nbsp; &#9888; <em>Standard kit charged at $85 &mdash; retail value under $12</em></span>
        <span>$85</span>
    </div>
    <div class="line-total">
        <span>TOTAL BILLED THIS PERIOD</span>
        <span>$19,940</span>
    </div>
</div>

<p>Three errors are visible: therapy overbilling by 14 units, a chronic medication incorrectly billed to Part A instead of Part D, and routine wound care supplies billed separately despite being included in the per-diem rate. Total overcharges: approximately $1,060 before the hygiene kit markup.</p>

{_embed(mode="markup", title="Check nursing home charges against Medicare rates", subtitle="Enter a CPT or revenue code to compare charges.", height="420")}

<h2 id="common-errors">4. Seven most common nursing home billing errors</h2>

<p><strong>1. Therapy upcoding.</strong> Billing for more physical, occupational, or speech therapy minutes than documented. Under PDPM (Patient-Driven Payment Model), SNFs are paid based on patient classification categories that depend on therapy needs. Request the MDS (Minimum Data Set) assessment and compare documented therapy minutes to what was billed.</p>

<p><strong>2. Consolidated billing violations.</strong> Medicare Part A pays SNFs a bundled per-diem rate that includes most services. Billing for services separately that are supposed to be included in this rate is one of the most common audit findings. Common examples: routine lab work, basic medical supplies, and standard nursing care.</p>

<p><strong>3. Incorrect room type billing.</strong> Being billed for a private room when you were in a semi-private room, or being moved to a less expensive room mid-stay but billed at the original rate throughout.</p>

<p><strong>4. Medicare Part D drugs billed to Part A.</strong> Medications a patient was taking before admission (maintenance drugs) should be covered by Medicare Part D. Billing them to Part A is an error that SNFs cannot charge patients for.</p>

<p><strong>5. Phantom charges for services not provided.</strong> Therapy sessions billed on days when the patient was hospitalized, asleep, or documented as refusing treatment. Cross-reference the bill against the nursing home&rsquo;s own daily care log (which you can request).</p>

<p><strong>6. Personal supply markups.</strong> Hygiene products, toiletries, and personal items billed at 5&ndash;10&times; retail cost. Many of these items are included in the room and board rate and should not be billed separately at all.</p>

<p><strong>7. Incorrect discharge date billing.</strong> Continuing to bill for the discharge day after a patient has left. By Medicare rules, the discharge day is not billable.</p>

<div class="key-takeaway">
    <strong>Not sure what Medicare should pay?</strong> Use our <a href="/calculator">free calculator</a> to look up Medicare rates for any nursing home service code &mdash; then compare against what the facility billed.
</div>

<h2 id="how-to-audit">5. How to audit a nursing home bill</h2>

<p>Auditing a nursing home bill requires three documents: the itemized statement from the facility, your Medicare Summary Notice (MSN) from CMS, and the MDS (Minimum Data Set) assessment that determined your care plan and therapy classification.</p>

<ol>
    <li><strong>Request an itemized statement.</strong> You are entitled to one. Ask for it in writing within the first 30 days of receiving any bill.</li>
    <li><strong>Compare to your Medicare Summary Notice.</strong> The MSN lists every service Medicare paid for on your behalf. If the facility billed Medicare for something not on your MSN, ask why.</li>
    <li><strong>Request the MDS assessment.</strong> The Minimum Data Set is the clinical assessment that determines your PDPM category and therapy needs. It&rsquo;s part of your medical record &mdash; you have the right to a copy. Compare documented therapy minutes to what was billed.</li>
    <li><strong>Check the daily treatment log.</strong> If therapy is billed on a specific date, the daily nursing or therapy notes should confirm it was provided. Absent documentation is grounds for a dispute.</li>
    <li><strong>Cross-check consolidated billing.</strong> CMS publishes a list of services included in the SNF consolidated billing rate. Any of those services billed separately is an error.</li>
</ol>

<h2 id="how-to-dispute">6. How to dispute nursing home charges</h2>

<p>For Medicare claims, you have the right to appeal any service Medicare denies or any claim you believe was incorrect. The appeals process has five levels:</p>

<ol>
    <li><strong>Redetermination</strong>: Submit within 120 days to the Medicare Administrative Contractor (MAC). Free. Resolved within 60 days.</li>
    <li><strong>Reconsideration</strong>: Submit within 180 days to a Qualified Independent Contractor (QIC). Free. Resolved within 60 days.</li>
    <li><strong>ALJ Hearing</strong>: Submit within 60 days if the amount in dispute exceeds $180 (2026). Free.</li>
    <li><strong>Medicare Appeals Council</strong>: Submit within 60 days of ALJ decision.</li>
    <li><strong>Federal Court</strong>: For amounts over $1,870 (2026).</li>
</ol>

<p>For non-Medicare billing disputes, send a written dispute letter to the facility&rsquo;s billing department with a copy of the itemized statement, your notes on what was and wasn&rsquo;t provided, and a request for a line-by-line review. See our <a href="/guides/dispute-letter-template">dispute letter template</a> for a starting point.</p>

<h2 id="case-studies">7. Case studies</h2>

<div class="case-study">
    <h3>Therapy upcoding: 14 overbilled PT units reversed</h3>
    <p>A family member of a nursing home patient noticed that the monthly statement showed 42 physical therapy units, but the care plan specified a maximum of 30 units per week and the patient had been hospitalized for 3 days mid-month. They requested the daily therapy logs.</p>
    <p>The logs showed 28 units provided, not 42. The family filed a Medicare redetermination request. The facility credited the 14-unit overage. <strong>Total savings: $840.</strong></p>
</div>

<div class="case-study">
    <h3>Chronic medications billed to Medicare Part A instead of Part D</h3>
    <p>A Medicare patient&rsquo;s monthly SNF statement included $620 in maintenance medications (lisinopril, atorvastatin, metformin) that she had been taking prior to her SNF admission. These are Part D drugs and cannot be billed to Part A.</p>
    <p>The patient&rsquo;s daughter disputed the charges with documentation showing the medications were on the pre-admission medication list. The facility reversed the charges. <strong>Refund: $620.</strong></p>
</div>

<div class="case-study">
    <h3>Observation status trap: $12,400 SNF bill avoided</h3>
    <p>A patient hospitalized for 4 nights was classified under &ldquo;observation status&rdquo; for the first 2 nights before being changed to formal inpatient admission. When transferred to a SNF, Medicare denied coverage because the patient did not have a full 3-day qualifying inpatient stay.</p>
    <p>An advocate helped the family appeal the observation status classification to the hospital. After review, the hospital changed the first 2 nights to inpatient admission status. <strong>Medicare coverage restored: $12,400 SNF bill covered.</strong></p>
</div>

<h2 id="faq">Frequently asked questions</h2>

<div class="faq-section">
    <div class="faq-item">
        <h3>How many days does Medicare cover in a nursing home?</h3>
        <p>Medicare Part A covers up to 100 days per benefit period in a skilled nursing facility following a qualifying 3-day inpatient hospital stay. Days 1&ndash;20 are fully covered at no cost. Days 21&ndash;100 require a daily copay of $204 (2026). Day 101+ is not covered by Medicare; Medicaid covers long-term care for qualifying patients.</p>
    </div>
    <div class="faq-item">
        <h3>What is therapy upcoding in nursing home billing?</h3>
        <p>Therapy upcoding means billing Medicare for more therapy minutes than were actually provided or documented. The HHS Office of Inspector General has found therapy upcoding in SNF claims at rates exceeding 25% in some audits. Request the MDS assessment and daily therapy logs to verify what was documented vs. what was billed.</p>
    </div>
    <div class="faq-item">
        <h3>What are ancillary charges on a nursing home bill?</h3>
        <p>Ancillary charges are costs beyond room and board, such as medications, medical supplies, and specialty therapies. Common errors include charges for items already included in the daily Medicare rate (the consolidated billing rule), supplies never provided, and personal care items billed at inflated prices.</p>
    </div>
    <div class="faq-item">
        <h3>Can I dispute a nursing home bill after discharge?</h3>
        <p>Yes. You generally have up to 120 days to file a Medicare redetermination (first level appeal). Request an itemized statement and compare it against your Medicare Summary Notice. Discrepancies between what the facility billed and what Medicare paid are common starting points for disputes. Use our <a href="/guides/dispute-letter-template">dispute letter template</a> to start the process.</p>
    </div>
    <div class="faq-item">
        <h3>What is the difference between skilled nursing and custodial care for Medicare?</h3>
        <p>Medicare Part A only covers &ldquo;skilled nursing care&rdquo; requiring a licensed nurse or therapist, such as wound care, IV medications, or physical therapy. It does not cover &ldquo;custodial care&rdquo; (help with bathing, dressing, eating). Once a patient&rsquo;s need for skilled care ends, Medicare coverage stops even if the patient remains in the facility.</p>
    </div>
</div>

<h2 id="sources">Sources</h2>

<ul class="sources-list">
    <li><a href="https://www.cms.gov/Medicare/Medicare-Fee-for-Service-Payment/SNFPPS/PDPM" target="_blank" rel="noopener">CMS: Patient-Driven Payment Model (PDPM) for SNFs</a></li>
    <li><a href="https://oig.hhs.gov/oei/reports/oei-02-18-00530.asp" target="_blank" rel="noopener">HHS OIG: Vulnerabilities in SNF Billing Under PDPM</a></li>
    <li><a href="https://www.medicare.gov/publications/10153-medicare-skilled-nursing-facility-care.pdf" target="_blank" rel="noopener">Medicare: Skilled Nursing Facility Care (CMS Publication 10153)</a></li>
    <li><a href="https://www.genworth.com/aging-and-you/finances/cost-of-care.html" target="_blank" rel="noopener">Genworth: 2025 Cost of Care Survey</a></li>
    <li><a href="https://www.kff.org/medicare/fact-sheet/medicare-and-medicaid-nursing-home-coverage/" target="_blank" rel="noopener">KFF: Medicare and Medicaid Nursing Home Coverage</a></li>
    <li><a href="https://www.medicare.gov/coverage/skilled-nursing-facility-snf-care" target="_blank" rel="noopener">Medicare.gov: Skilled Nursing Facility Coverage Rules</a></li>
</ul>
""",
})
