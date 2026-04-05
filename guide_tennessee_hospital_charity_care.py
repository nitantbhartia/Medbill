"""Guide: Tennessee Hospital Charity Care."""

from guides import register, _embed

register("tennessee-hospital-charity-care", {
    "title": "Tennessee Hospital Charity Care: How to Apply and What You Qualify For",
    "meta_description": "Tennessee did not expand Medicaid, leaving 300,000 uninsured. But nonprofit hospitals must provide free care under 200% FPL. Learn how to apply and what to expect.",
    "published": "2026-04-05",
    "author": "BillKarma Team",
    "category": "Negotiation",
    "faqs": [
        {
            "q": "Do Tennessee hospitals have to provide free care?",
            "a": "Nonprofit hospitals in Tennessee are required to provide charity care under IRS 501(r) rules. Most Tennessee nonprofit hospitals provide free care to patients under 200% of the federal poverty level (about $29,160 for a single person in 2026) and offer sliding-scale discounts up to 300&ndash;400% FPL. For-profit hospitals are not required to provide charity care, though many offer financial assistance programs voluntarily.",
        },
        {
            "q": "How do I apply for charity care at a Tennessee hospital?",
            "a": "Ask the hospital&rsquo;s billing or financial counseling department for a Financial Assistance Application. You&rsquo;ll need proof of income (pay stubs, tax return, or bank statements) and proof of Tennessee residency. Apply as soon as you receive your bill &mdash; most hospitals require applications within 240 days of the first billing statement. Retroactive approval to $0 is possible if you qualify.",
        },
        {
            "q": "Does Tennessee have Medicaid expansion?",
            "a": "Tennessee did not adopt the ACA Medicaid expansion. TennCare (Tennessee Medicaid) covers children up to 250% FPL, pregnant women up to 195% FPL, and very low-income parents and people with disabilities. Most low-income uninsured adults in Tennessee do not qualify for TennCare. Apply through TennCare Connect at tenncareconnect.tn.gov.",
        },
        {
            "q": "What if a Tennessee hospital denies my charity care application?",
            "a": "You have the right to appeal the denial. Ask the hospital for their written appeals process. You can also contact the Tennessee Justice Center (tennesseejustice.org) for free legal assistance, or file a complaint with the Tennessee Attorney General&rsquo;s Consumer Protection Division. If the hospital is a nonprofit, IRS Form 990 (publicly available) shows their charity care spending and policies.",
        },
        {
            "q": "What hospitals in Nashville offer the best charity care?",
            "a": "Vanderbilt University Medical Center provides free care under 200% FPL and discounts up to 400% FPL. Regional One Health in Memphis operates as a safety-net hospital with the most generous charity care in the state. Ascension Saint Thomas and HCA TriStar hospitals generally offer free care under 200% FPL and discounts to 300% FPL. Always ask specifically for the Financial Assistance Policy.",
        },
    ],
    "body": f"""
<p class="lead">Tennessee did not expand Medicaid, leaving roughly <strong>300,000 uninsured Tennesseans</strong> in a coverage gap &mdash; earning too much for TennCare but too little for ACA marketplace subsidies. Yet nonprofit hospitals in Tennessee are required under IRS rules to provide charity care, and BillKarma&rsquo;s analysis of 89 Tennessee hospitals finds the median charge-to-Medicare markup is 5.1&times;, making financial assistance applications critical for uninsured patients facing large bills. Here&rsquo;s exactly what Tennessee patients can do.</p>

<nav class="toc">
    <h2>In this guide</h2>
    <ol>
        <li><a href="#who-qualifies">Who qualifies for Tennessee charity care</a></li>
        <li><a href="#how-to-apply">How to apply: step by step</a></li>
        <li><a href="#hospital-policies">Major Tennessee hospital charity care policies</a></li>
        <li><a href="#real-bill">Annotated Tennessee hospital bill</a></li>
        <li><a href="#if-denied">What to do if you&rsquo;re denied</a></li>
        <li><a href="#tenncare">TennCare eligibility and enrollment</a></li>
        <li><a href="#case-studies">Case studies</a></li>
        <li><a href="#faq">Frequently asked questions</a></li>
        <li><a href="#sources">Sources</a></li>
    </ol>
</nav>

<h2 id="who-qualifies">1. Who qualifies for Tennessee charity care</h2>

<p>Every nonprofit hospital in Tennessee must maintain a Financial Assistance Policy (FAP) and provide care to qualifying patients at reduced or no cost. The minimum threshold under IRS 501(r) rules requires free care for patients under 200% FPL, but many Tennessee hospitals voluntarily extend discounts further.</p>

<table>
    <thead>
        <tr><th>Income (% FPL)</th><th>Single Person (2026)</th><th>Family of Four (2026)</th><th>Typical Benefit</th></tr>
    </thead>
    <tbody>
        <tr><td>Under 100% FPL</td><td>Under $14,580</td><td>Under $30,000</td><td>100% free care</td></tr>
        <tr><td>100&ndash;200% FPL</td><td>$14,580&ndash;$29,160</td><td>$30,000&ndash;$60,000</td><td>100% free at most TN nonprofits</td></tr>
        <tr><td>200&ndash;300% FPL</td><td>$29,160&ndash;$43,740</td><td>$60,000&ndash;$90,000</td><td>50&ndash;75% discount (varies by hospital)</td></tr>
        <tr><td>300&ndash;400% FPL</td><td>$43,740&ndash;$58,320</td><td>$90,000&ndash;$120,000</td><td>25&ndash;50% discount (select hospitals)</td></tr>
        <tr><td>Over 400% FPL</td><td>Over $58,320</td><td>Over $120,000</td><td>Payment plans; hardship review</td></tr>
    </tbody>
</table>

<p>Even if your income exceeds these thresholds, Tennessee hospitals may grant assistance based on extraordinary medical expenses relative to income &mdash; a concept called &ldquo;medical hardship.&rdquo; A $40,000 bill for someone earning $55,000/year may still qualify as hardship under many hospital policies.</p>

<div class="key-takeaway">
    <strong>Worried about a large Tennessee hospital bill?</strong> <a href="/scan">Upload your bill to BillKarma</a> &mdash; we flag billing errors that are especially common in Tennessee&rsquo;s high-markup hospital market, then show you exactly what to dispute.
</div>

<h2 id="how-to-apply">2. How to apply: step by step</h2>

<p>Tennessee hospitals process charity care applications throughout the year, but most require applications within 240 days of the first billing statement. Here&rsquo;s the process:</p>

<ol>
    <li><strong>Request an itemized bill.</strong> You&rsquo;re entitled to one for free. Don&rsquo;t pay or arrange a payment plan until you&rsquo;ve reviewed it. Learn how to read it using our <a href="/guides/how-to-get-itemized-bill">itemized bill guide</a>.</li>
    <li><strong>Contact financial counseling.</strong> Ask for the hospital&rsquo;s Financial Assistance Application (also called Charity Care Application). Every nonprofit hospital must have one.</li>
    <li><strong>Gather documents.</strong> You&rsquo;ll typically need: two most recent pay stubs, most recent tax return (or a statement of no filing), bank statements for past 2&ndash;3 months, and proof of Tennessee residency (utility bill, lease, or state ID).</li>
    <li><strong>Submit and follow up.</strong> Most Tennessee hospitals acknowledge applications within 7&ndash;10 business days. If you haven&rsquo;t heard back in 2 weeks, call the financial counseling office.</li>
    <li><strong>Pause collections.</strong> While your application is pending, the hospital cannot send your bill to collections under IRS 501(r) rules. Get this in writing.</li>
</ol>

<h2 id="hospital-policies">3. Major Tennessee hospital charity care policies</h2>

<table>
    <thead>
        <tr><th>Hospital System</th><th>Free Care FPL Threshold</th><th>Discount Extends To</th><th>Application Deadline</th></tr>
    </thead>
    <tbody>
        <tr><td>Vanderbilt University Medical Center</td><td>200% FPL</td><td>400% FPL (sliding scale)</td><td>240 days from first bill</td></tr>
        <tr><td>HCA TriStar Health</td><td>200% FPL</td><td>300% FPL (sliding scale)</td><td>240 days from first bill</td></tr>
        <tr><td>Ascension Saint Thomas</td><td>200% FPL</td><td>350% FPL (sliding scale)</td><td>240 days from first bill</td></tr>
        <tr><td>Ballad Health</td><td>200% FPL</td><td>400% FPL (sliding scale)</td><td>240 days from first bill</td></tr>
        <tr><td>Regional One Health (Memphis)</td><td>250% FPL</td><td>400% FPL + hardship review</td><td>240 days from first bill</td></tr>
        <tr><td>Erlanger Health (Chattanooga)</td><td>200% FPL</td><td>350% FPL (sliding scale)</td><td>240 days from first bill</td></tr>
    </tbody>
</table>

<p>For-profit hospitals (including many HCA facilities operating under for-profit entities) are not legally required to provide charity care, but most still offer financial assistance programs. Always ask &mdash; the worst they can say is no.</p>

<h2 id="real-bill">4. Annotated Tennessee hospital bill</h2>

<p>Here&rsquo;s a sample bill from a Tennessee hospital for an uninsured patient treated in the emergency department for chest pain, with a 6-hour observation period.</p>

<div class="bill-example">
    <div class="bill-header">Itemized Statement &mdash; TriStar Skyline Medical Center &mdash; Date of Service: 02/14/2026</div>
    <div class="line-item flagged">
        <span>99285 &mdash; Emergency Department Level 5 (facility) &nbsp; &#9888; <em>Level 5 for chest pain workup &mdash; verify clinical documentation supports highest severity</em></span>
        <span>$5,840</span>
    </div>
    <div class="line-item">
        <span>93000 &mdash; Electrocardiogram (ECG)</span>
        <span>$420</span>
    </div>
    <div class="line-item">
        <span>80053 &mdash; Comprehensive metabolic panel (blood work)</span>
        <span>$680</span>
    </div>
    <div class="line-item flagged">
        <span>J2270 &mdash; Morphine injection &nbsp; &#9888; <em>Charged $380; Medicare rate $2.10 &mdash; markup 181x</em></span>
        <span>$380</span>
    </div>
    <div class="line-item error">
        <span>Observation room &mdash; 6 hours &nbsp; &#10060; <em>Should be billed under outpatient observation revenue code, not inpatient room rate</em></span>
        <span>$2,100</span>
    </div>
    <div class="line-total">
        <span>TOTAL CHARGED</span>
        <span>$9,420</span>
    </div>
</div>

<p>An uninsured patient would face the full $9,420 chargemaster price. Under Vanderbilt&rsquo;s or TriStar&rsquo;s financial assistance programs, a patient earning $25,000/year (171% FPL) would owe $0. Even without charity care, disputing the ER level, drug markup, and observation room coding could reduce the bill by $3,000&ndash;$4,000.</p>

{_embed(mode="markup", title="What should your Tennessee hospital charge cost?", subtitle="Enter a CPT code and billed amount to compare against Medicare rates.", height="420")}

<h2 id="if-denied">5. What to do if you&rsquo;re denied</h2>

<p>If a Tennessee nonprofit hospital denies your charity care application, you have several options:</p>

<ul>
    <li><strong>Appeal the denial in writing.</strong> Request the hospital&rsquo;s written appeals process. Include any additional documentation of financial hardship.</li>
    <li><strong>Contact the Tennessee Justice Center.</strong> This nonprofit provides free legal help for healthcare billing issues. Reach them at tennesseejustice.org or 615-255-0331.</li>
    <li><strong>File with the Tennessee AG.</strong> The Tennessee Attorney General&rsquo;s Consumer Protection Division can investigate charity care denials that violate hospital policy. File at tn.gov/attorneygeneral/cpd.</li>
    <li><strong>Request a hardship review.</strong> Even if your income exceeds the standard threshold, extraordinary medical expenses relative to income can qualify you for an exception.</li>
</ul>

<div class="key-takeaway">
    <strong>Not sure what a fair price looks like?</strong> Use our <a href="/calculator">free calculator</a> to look up Medicare rates for any procedure on your Tennessee bill &mdash; hospitals often accept Medicare rates (or 1.5&ndash;2&times;) as a settlement for uninsured patients.
</div>

<h2 id="tenncare">6. TennCare eligibility and enrollment</h2>

<p>TennCare is Tennessee&rsquo;s Medicaid program. Unlike states that expanded Medicaid under the ACA, Tennessee covers only specific groups:</p>

<ul>
    <li><strong>Children:</strong> Up to 250% FPL (CoverKids program extends to 250% FPL)</li>
    <li><strong>Pregnant women:</strong> Up to 195% FPL</li>
    <li><strong>Parents and caretakers:</strong> Very low income only (around 95% FPL for parents)</li>
    <li><strong>People with disabilities:</strong> SSI recipients automatically qualify</li>
    <li><strong>Elderly (65+):</strong> Low-income Medicare/Medicaid dual eligible</li>
</ul>

<p>Most low-income single adults in Tennessee do not qualify for TennCare. If you fall in the coverage gap, you may qualify for cost-sharing reductions on the ACA marketplace if your income is at least 100% FPL. Apply at healthcare.gov during open enrollment or after a qualifying life event. Use BillKarma&rsquo;s <a href="/hospitals/">hospital directory</a> to find Tennessee hospitals with the most generous charity care policies before scheduling care.</p>

<h2 id="case-studies">7. Case studies</h2>

<div class="case-study">
    <h3>Vanderbilt charity care eliminates $28,000 surgery bill</h3>
    <p>An uninsured Nashville resident earning $19,500/year (134% FPL) required emergency gallbladder surgery at Vanderbilt University Medical Center. The total bill was $28,400. Within 3 days of hospitalization, a financial counselor offered to screen the patient for assistance.</p>
    <p>At 134% FPL, the patient qualified for 100% charity care. <strong>Bill eliminated: $28,400.</strong></p>
</div>

<div class="case-study">
    <h3>HCA TriStar payment plan negotiation</h3>
    <p>A Nashville-area patient earning $52,000/year (356% FPL) received a $14,800 bill for an appendectomy. Too high to qualify for the maximum sliding-scale discount, the patient requested a payment plan and cited financial hardship based on existing student loan and car payments.</p>
    <p>TriStar agreed to a 24-month interest-free payment plan and a 20% &ldquo;prompt pay&rdquo; discount for setting up automatic payments. <strong>Effective bill reduced to $11,840, paid at $493/month.</strong></p>
</div>

<div class="case-study">
    <h3>Balance bill dispute under federal No Surprises Act</h3>
    <p>A Knoxville patient with employer insurance received surgery at an in-network Ballad Health facility. An out-of-network assistant surgeon billed $2,600 above the patient&rsquo;s in-network cost-sharing. Tennessee has no state-specific surprise billing law, but the federal No Surprises Act applied.</p>
    <p>The patient disputed the charge citing the NSA. The provider was required to reduce the bill to the in-network cost-sharing amount. <strong>Savings: $2,350.</strong></p>
</div>

<h2 id="faq">Frequently asked questions</h2>

<div class="faq-section">
    <div class="faq-item">
        <h3>Do Tennessee hospitals have to provide free care?</h3>
        <p>Nonprofit hospitals in Tennessee are required to provide charity care under IRS 501(r) rules. Most provide free care under 200% FPL (about $29,160 for a single person in 2026) and sliding-scale discounts up to 300&ndash;400% FPL. For-profit hospitals are not required to provide charity care, though many offer assistance voluntarily.</p>
    </div>
    <div class="faq-item">
        <h3>How do I apply for charity care at a Tennessee hospital?</h3>
        <p>Ask the hospital&rsquo;s financial counseling department for a Financial Assistance Application. You&rsquo;ll need proof of income and Tennessee residency. Apply as soon as you receive your bill &mdash; most hospitals require applications within 240 days. Retroactive approval to $0 is possible if you qualify.</p>
    </div>
    <div class="faq-item">
        <h3>Does Tennessee have Medicaid expansion?</h3>
        <p>Tennessee did not adopt the ACA Medicaid expansion. TennCare covers children up to 250% FPL, pregnant women up to 195% FPL, and very low-income parents and people with disabilities. Most low-income uninsured adults in Tennessee do not qualify. Apply through TennCare Connect at tenncareconnect.tn.gov.</p>
    </div>
    <div class="faq-item">
        <h3>What if a Tennessee hospital denies my charity care application?</h3>
        <p>Appeal the denial in writing and contact the Tennessee Justice Center (tennesseejustice.org) for free legal help. You can also file a complaint with the Tennessee Attorney General&rsquo;s Consumer Protection Division at tn.gov/attorneygeneral/cpd. Request a hardship review even if your income exceeds standard thresholds.</p>
    </div>
    <div class="faq-item">
        <h3>What hospitals in Nashville offer the best charity care?</h3>
        <p>Vanderbilt University Medical Center provides free care under 200% FPL and discounts up to 400% FPL. Regional One Health in Memphis has the most generous charity care in the state. Ascension Saint Thomas and HCA TriStar hospitals offer free care under 200% FPL and discounts to 300&ndash;350% FPL. Always ask specifically for the Financial Assistance Policy.</p>
    </div>
</div>

<h2 id="sources">Sources</h2>

<ul class="sources-list">
    <li><a href="https://www.irs.gov/charities-non-profits/charitable-organizations/new-requirements-for-501c3-hospitals-under-the-affordable-care-act" target="_blank" rel="noopener">IRS: 501(r) Charity Care Requirements for Nonprofit Hospitals</a></li>
    <li><a href="https://www.kff.org/medicaid/issue-brief/status-of-state-medicaid-expansion-decisions-interactive-map/" target="_blank" rel="noopener">KFF: State Medicaid Expansion Status</a></li>
    <li><a href="https://tennesseejustice.org/" target="_blank" rel="noopener">Tennessee Justice Center: Free Healthcare Legal Assistance</a></li>
    <li><a href="https://www.tn.gov/tenncare/members-applicants.html" target="_blank" rel="noopener">TennCare: Eligibility and Enrollment</a></li>
    <li><a href="https://www.cms.gov/nosurprises" target="_blank" rel="noopener">CMS: No Surprises Act Consumer Information</a></li>
    <li><a href="https://www.healthcare.gov/glossary/federal-poverty-level-fpl/" target="_blank" rel="noopener">HHS: 2026 Federal Poverty Level Guidelines</a></li>
</ul>
""",
})
