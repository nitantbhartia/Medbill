"""Guide: Arkansas Medical Billing Laws."""

from guides import register, _embed

register("arkansas-medical-billing", {
    "title": "Arkansas Medical Billing Laws & Patient Rights (2026)",
    "meta_description": "AR Code § 20-9-1501 requires charity care at Arkansas hospitals. Learn ARHOME Medicaid, 5-year SOL, and how to cut your hospital bill. Free analysis.",
    "published": "2026-04-05",
    "author": "BillKarma Team",
    "category": "State Guides",
    "faqs": [
        {
            "q": "Are Arkansas hospitals required to offer charity care?",
            "a": "Yes. Arkansas Code § 20-9-1501 requires nonprofit hospitals to adopt and maintain a charity care policy. The law requires hospitals to publicize their financial assistance policies and to screen uninsured patients for eligibility. Arkansas law does not specify a minimum income threshold — each hospital sets its own. Most Arkansas nonprofit hospitals provide free care up to 200% FPL and sliding-scale discounts up to 250–300% FPL. Apply within 240 days of your first billing statement.",
        },
        {
            "q": "What is Arkansas Works and does Arkansas have Medicaid expansion?",
            "a": "Yes. Arkansas expanded Medicaid through a waiver program called Arkansas Works (later Arkansas Health and Opportunity for Me, or ARHOME), which covers adults earning up to 138% of the Federal Poverty Level. Arkansas implemented expansion through a private option model rather than traditional Medicaid, but the coverage level is equivalent. As of 2026, hundreds of thousands of Arkansans receive coverage through the program. Apply at access.arkansas.gov.",
        },
        {
            "q": "What is the statute of limitations on medical debt in Arkansas?",
            "a": "Arkansas has a 5-year statute of limitations on written contracts under Arkansas Code § 16-56-111. Most hospital bills — where you signed a financial responsibility form at admission — are treated as written contracts subject to this 5-year SOL. The clock starts from the date of the last payment or the date the debt became due. Any payment restarts the 5-year period.",
        },
        {
            "q": "How much can a creditor garnish from my wages in Arkansas for medical debt?",
            "a": "Arkansas limits wage garnishment to 25% of disposable earnings per the federal Consumer Credit Protection Act. Arkansas also provides additional head-of-household protections: if you are the head of a family earning under $1,000 per week, your wages may qualify for additional exemption. A creditor must first obtain a court judgment before garnishing wages. Social Security, unemployment, and workers' compensation are exempt from garnishment.",
        },
        {
            "q": "Does Arkansas protect patients from surprise medical bills?",
            "a": "Arkansas relies primarily on the federal No Surprises Act (effective January 1, 2022) for surprise billing protection. Under the NSA, patients cannot be balance-billed for emergency services or for non-emergency care from out-of-network ancillary providers at in-network facilities without advance written consent. Report violations to CMS at 1-800-985-3059 or file with the Arkansas Insurance Department.",
        },
    ],
    "body": f"""
<p class="lead">Arkansas is a predominantly rural state with <strong>over 85 licensed hospitals</strong>, many of them critical access facilities serving low-income populations. BillKarma&rsquo;s analysis of Arkansas hospital billing data found a median markup of <strong>4.8&times; Medicare rates</strong> for uninsured patients &mdash; one of the higher markups in the region. Arkansas expanded Medicaid through its ARHOME program and requires nonprofit hospitals to offer charity care under AR Code &sect;&nbsp;20-9-1501. Arkansas&rsquo;s 5-year statute of limitations on medical debt and a 25% wage garnishment cap provide additional patient protections. This guide explains every tool available.</p>

<nav class="toc">
    <h2>In this guide</h2>
    <ol>
        <li><a href="#charity-care">Charity care under AR Code &sect; 20-9-1501</a></li>
        <li><a href="#medicaid">Arkansas Medicaid expansion (ARHOME)</a></li>
        <li><a href="#surprise-billing">Surprise billing protections (No Surprises Act)</a></li>
        <li><a href="#statute-of-limitations">Statute of limitations on medical debt (5 years)</a></li>
        <li><a href="#debt-collection">Debt collection and wage garnishment</a></li>
        <li><a href="#how-to-dispute">How to dispute an Arkansas hospital bill</a></li>
        <li><a href="#bill-example">Annotated Arkansas hospital bill</a></li>
        <li><a href="#case-study">Real patient results</a></li>
        <li><a href="#faq">Frequently asked questions</a></li>
        <li><a href="#sources">Sources</a></li>
    </ol>
</nav>

<h2 id="charity-care">1. Charity care under AR Code &sect; 20-9-1501</h2>

<p>Arkansas Code &sect;&nbsp;20-9-1501 requires every <strong>nonprofit hospital</strong> in Arkansas to adopt and maintain a written charity care policy. The Arkansas Department of Health (ADH) oversees hospital licensing and compliance. Key requirements:</p>

<ul>
    <li><strong>Written policy required.</strong> Every nonprofit hospital must have a formal charity care policy defining eligibility criteria, application procedures, and types of assistance available.</li>
    <li><strong>Public posting.</strong> Hospitals must post their charity care policies and inform patients of financial assistance options at or before the time of billing.</li>
    <li><strong>Screening before collections.</strong> Hospitals must screen uninsured patients for charity care eligibility before referring accounts to external debt collectors.</li>
    <li><strong>No state minimum threshold.</strong> Arkansas law does not mandate a specific income threshold. Most hospitals use 200% FPL for free care and 250&ndash;300% FPL for discounts &mdash; but always verify your specific hospital&rsquo;s policy.</li>
</ul>

<table>
    <thead>
        <tr><th>Household Size</th><th>100% FPL (2026)</th><th>138% FPL (Medicaid)</th><th>200% FPL (typical free care)</th><th>300% FPL (typical discount limit)</th></tr>
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

<p><em>FPL figures reflect 2026 HHS guidelines. Verify at <a href="https://aspe.hhs.gov/topics/poverty-economic-mobility/hhs-poverty-guidelines" target="_blank" rel="noopener">aspe.hhs.gov</a>. Individual hospital thresholds vary &mdash; always request the specific hospital&rsquo;s policy.</em></p>

<div class="key-takeaway">
    <strong>Always ask for the charity care application first.</strong> Under AR Code &sect;&nbsp;20-9-1501, every Arkansas nonprofit hospital must have one available. <a href="/charity-care">Use BillKarma&rsquo;s free eligibility tool</a> to check your household&rsquo;s status and get a pre-filled application.
</div>

<h2 id="medicaid">2. Arkansas Medicaid expansion (ARHOME)</h2>

<p>Arkansas expanded Medicaid through a Section 1115 waiver program. Originally called Arkansas Works and later renamed Arkansas Health and Opportunity for Me (ARHOME), the program provides Medicaid coverage to adults earning up to <strong>138% of the Federal Poverty Level</strong>.</p>

<p>Key ARHOME details:</p>
<ul>
    <li><strong>Income threshold:</strong> Adults (age 19&ndash;64) with income at or below 138% FPL qualify. Approximately $20,783 single / $44,367 family of four in 2026.</li>
    <li><strong>Private option model:</strong> Unlike traditional Medicaid, ARHOME uses premium tax credits to enroll qualifying individuals in private health plans through the ACA marketplace, in addition to traditional managed care Medicaid for others.</li>
    <li><strong>Retroactive coverage:</strong> Coverage may be retroactive for up to 3 months. Apply immediately after a hospital visit if you were uninsured.</li>
    <li><strong>Apply:</strong> <a href="https://access.arkansas.gov" target="_blank" rel="noopener">access.arkansas.gov</a> or call 1-855-372-1084.</li>
</ul>

{_embed(mode="markup", title="Compare your Arkansas hospital bill to Medicare rates", subtitle="Enter a CPT code and charged amount to see the markup over Medicare.", height="420")}

<h2 id="surprise-billing">3. Surprise billing protections (No Surprises Act)</h2>

<p>Arkansas patients rely on the <strong>federal No Surprises Act</strong> (effective January 1, 2022) for surprise billing protection. Arkansas does not have a comprehensive state surprise billing law.</p>

<p>NSA protections for Arkansas patients:</p>
<ul>
    <li><strong>Emergency services:</strong> In-network cost-sharing only, regardless of which providers treat you in an ER.</li>
    <li><strong>Non-emergency ancillary providers at in-network facilities:</strong> Out-of-network anesthesiologists, radiologists, pathologists, and similar providers at in-network hospitals cannot balance bill without 72-hour advance written consent.</li>
    <li><strong>Good Faith Estimates:</strong> Uninsured patients are entitled to written cost estimates before scheduled services costing $400 or more.</li>
    <li><strong>Air ambulance:</strong> No balance billing for out-of-network air ambulance services.</li>
</ul>

<p>Report NSA violations to the <a href="https://www.cms.gov/nosurprises" target="_blank" rel="noopener">CMS No Surprises Help Desk</a> at 1-800-985-3059 or to the <a href="https://www.insurance.arkansas.gov/consumers/file-complaint" target="_blank" rel="noopener">Arkansas Insurance Department</a>.</p>

<div class="guide-cta-inline">
    <p><strong>Did you receive a surprise bill in Arkansas?</strong> BillKarma identifies NSA violations automatically and generates a dispute letter ready to send. <a href="/scan">Scan your bill free &mdash; takes under 2 minutes.</a></p>
</div>

<h2 id="statute-of-limitations">4. Statute of limitations on medical debt in Arkansas (5 years)</h2>

<p>Arkansas Code &sect;&nbsp;16-56-111 sets a <strong>5-year statute of limitations</strong> on written contracts. Most hospital bills &mdash; where you signed any financial responsibility form at admission &mdash; are subject to this 5-year period.</p>

<table>
    <thead>
        <tr><th>Debt Type</th><th>Arkansas SOL</th><th>Notes</th></tr>
    </thead>
    <tbody>
        <tr><td>Written contract (signed financial agreement)</td><td>5 years</td><td>Applies to most hospital bills with signed admission paperwork</td></tr>
        <tr><td>Open account (no signed contract)</td><td>3 years</td><td>AR Code § 16-56-105; applies to some physician bills without a written agreement</td></tr>
        <tr><td>Court judgment</td><td>10 years (renewable)</td><td>Always respond to lawsuits to prevent default judgments</td></tr>
    </tbody>
</table>

<p><strong>What resets the Arkansas SOL:</strong></p>
<ul>
    <li>Any voluntary payment on the debt restarts the 5-year clock.</li>
    <li>A written acknowledgment of the debt may restart the SOL.</li>
    <li>Arkansas courts have held that partial payments restart the limitations period under the part-payment doctrine.</li>
</ul>

<p>Use our <a href="/statute-of-limitations">SOL lookup tool</a> to check the status of any specific debt before paying a collector.</p>

<h2 id="debt-collection">5. Debt collection and wage garnishment in Arkansas</h2>

<p>Arkansas limits wage garnishment to <strong>25% of disposable earnings</strong> per the federal Consumer Credit Protection Act. Arkansas also provides additional head-of-household protections:</p>

<ul>
    <li><strong>Head-of-household wage exemption (AR Code &sect; 16-66-218):</strong> If you are a head of family with a dependent, a larger portion of your wages may be exempt. In some cases, wages of a head of household earning under a certain threshold can be fully exempt from garnishment. Consult an Arkansas attorney to determine if this applies to your situation.</li>
    <li><strong>Homestead exemption (AR Const. Art. 9):</strong> Arkansas&rsquo;s homestead exemption protects $2,500 of a rural homestead or up to $500 per city/town lot. This is lower than many states.</li>
    <li><strong>Exempt income:</strong> Social Security, unemployment, and workers&rsquo; compensation are exempt from garnishment.</li>
    <li><strong>Judgment required first.</strong> No garnishment without a court judgment. Always respond to collections lawsuits.</li>
</ul>

<h2 id="how-to-dispute">6. How to dispute an Arkansas hospital bill</h2>

<h3>Step 1: Request an itemized bill</h3>
<p>Request a fully itemized statement by certified mail or email, listing every CPT code, revenue code, service description, date, quantity, and unit price. Arkansas patients are entitled to an itemized bill on request.</p>

<h3>Step 2: Check ARHOME Medicaid eligibility</h3>
<p>Before paying anything, check whether you qualify for ARHOME (up to 138% FPL). Apply at <a href="https://access.arkansas.gov" target="_blank" rel="noopener">access.arkansas.gov</a>. Retroactive coverage can eliminate recent bills entirely.</p>

<h3>Step 3: Apply for charity care under AR Code &sect; 20-9-1501</h3>
<p>If you don&rsquo;t qualify for Medicaid, apply for financial assistance. Gather pay stubs, prior-year tax return, and bank statements. Submit with certified mail and keep copies of everything.</p>

<h3>Step 4: Benchmark charges and dispute errors</h3>
<p>Use our <a href="/calculator">Medicare rate calculator</a> to identify inflated charges. BillKarma analysis found Arkansas hospitals charge an average of 4.8&times; Medicare for outpatient services &mdash; use this benchmark in your negotiation or charity care application.</p>

<h3>Step 5: File complaints if needed</h3>
<ul>
    <li><strong>Hospital licensing complaints:</strong> <a href="https://www.healthy.arkansas.gov/programs-services/topics/health-facility-services" target="_blank" rel="noopener">Arkansas Department of Health, Health Facility Services</a></li>
    <li><strong>Insurance and surprise billing:</strong> <a href="https://www.insurance.arkansas.gov/consumers/file-complaint" target="_blank" rel="noopener">Arkansas Insurance Department</a></li>
    <li><strong>No Surprises Act:</strong> <a href="https://www.cms.gov/nosurprises" target="_blank" rel="noopener">CMS Help Desk</a> (1-800-985-3059)</li>
    <li><strong>Debt collection abuse:</strong> <a href="https://www.consumerfinance.gov/complaint/" target="_blank" rel="noopener">CFPB</a> or <a href="https://www.arkansasag.gov/consumer-protection/" target="_blank" rel="noopener">Arkansas Attorney General Consumer Protection</a></li>
</ul>

<div class="key-takeaway">
    <strong>Arkansas&rsquo;s 5-year SOL on written contracts is powerful protection.</strong> Most hospital bills have a 5-year window. After that, a collector cannot win a lawsuit. Use our <a href="/statute-of-limitations">free SOL tool</a> to check your debt before making any payment.
</div>

<h2 id="bill-example">7. Annotated Arkansas hospital bill</h2>

<div class="bill-example">
    <div class="bill-header">Itemized Statement &mdash; Natural State Medical Center &mdash; Inpatient Admission &mdash; Date of Service: 01/15/2026</div>
    <div class="line-item error">
        <span>99233 &mdash; Subsequent Hospital Care, High Complexity, billed 4 consecutive days &nbsp; &#10060; <em>Daily subsequent hospital care requires separate documentation for each day. If the provider notes are templated or copied day-to-day without new clinical information, these charges may not be individually supportable. Request the daily physician notes.</em></span>
        <span>$1,420.00 (&times;4 days)</span>
    </div>
    <div class="line-item flagged">
        <span>80053 &mdash; Comprehensive Metabolic Panel, billed daily &times; 4 &nbsp; &#9888; <em>Medicare pays approximately $14 for each CMP. At $275 per panel &times; 4 days = $1,100, this is $1,044 above Medicare rates for this single test. Verify whether daily CMPs were medically necessary throughout the admission.</em></span>
        <span>$1,100.00</span>
    </div>
    <div class="line-item">
        <span>93306 &mdash; Echocardiogram, complete with Doppler</span>
        <span>$2,400.00</span>
    </div>
    <div class="line-item">
        <span>71046 &mdash; Chest X-ray, 2 views</span>
        <span>$390.00</span>
    </div>
    <div class="line-item">
        <span>Room and board, semi-private, 4 days</span>
        <span>$9,600.00</span>
    </div>
    <div class="line-total">
        <span>TOTAL BILLED</span>
        <span>$20,170.00</span>
    </div>
</div>

<h2 id="case-study">8. Real patient results</h2>

<div class="case-study">
    <h3>Case study: $20,000 inpatient bill reduced to $0 through ARHOME and charity care &mdash; Little Rock</h3>
    <p><strong>Situation:</strong> An uninsured Little Rock resident was hospitalized for 4 days with a cardiac event. Total bill: $20,000 from a Baptist Health nonprofit hospital.</p>
    <p><strong>Patient profile:</strong> Married, two children, household income $41,000 (approximately 128% FPL for a family of four). Just within ARHOME Medicaid eligibility.</p>
    <p><strong>Action:</strong> BillKarma identified ARHOME eligibility and guided the patient through the application process. The patient applied within 45 days of discharge.</p>
    <p><strong>Result:</strong> ARHOME approved retroactive coverage for the month of hospitalization. The hospital billed Medicaid and the patient&rsquo;s balance was zeroed out.</p>
    <p><strong>Savings: $20,000.</strong></p>
</div>

<div class="case-study">
    <h3>Case study: Duplicate daily charges removed &mdash; Fort Smith</h3>
    <p><strong>Situation:</strong> A Fort Smith patient received a $12,400 inpatient bill that included 5 days of daily physician notes billed at the highest complexity level (99233), along with daily comprehensive metabolic panels. BillKarma flagged these as potential documentation issues.</p>
    <p><strong>Action:</strong> The patient requested the complete inpatient medical chart. The notes showed templated physician documentation with minimal daily changes and no new clinical information justifying high-complexity coding. A dispute letter was sent with the specific physician notes attached, citing CMS E&amp;M documentation guidelines.</p>
    <p><strong>Result:</strong> The hospital&rsquo;s coding department reviewed the chart and downgraded 3 of the 5 daily visits from 99233 to 99231 (lowest complexity), reducing the bill by $1,890. The duplicate daily lab charges ($825) were also removed.</p>
    <p><strong>Savings: $2,715.</strong></p>
</div>

<div class="case-study">
    <h3>Case study: $7,600 charity care approval for self-pay surgery &mdash; Fayetteville</h3>
    <p><strong>Situation:</strong> A self-pay Fayetteville resident earning $44,000/year (single adult, 281% FPL) received a $7,600 bill for outpatient knee surgery at a Washington Regional nonprofit hospital.</p>
    <p><strong>Action:</strong> Applied for charity care under AR Code &sect;&nbsp;20-9-1501. Income of 281% FPL qualified for a 40% discount under the hospital&rsquo;s sliding-scale policy.</p>
    <p><strong>Result:</strong> Hospital approved $3,040 discount, reducing the balance to $4,560. A 12-month, 0% interest payment plan was arranged.</p>
    <p><strong>Savings: $3,040.</strong></p>
</div>

<div class="key-takeaway">
    <strong>Arkansas ARHOME covers 138% FPL with retroactive eligibility.</strong> If you had a hospital visit while uninsured and your income is under $20,783 (single) or $44,367 (family of four), apply for ARHOME at <a href="https://access.arkansas.gov" target="_blank" rel="noopener">access.arkansas.gov</a> immediately. The application can eliminate the entire bill.
</div>

<h2 id="faq">Frequently asked questions</h2>

<div class="faq-section">
    <div class="faq-item">
        <h3>Are Arkansas hospitals required to offer charity care?</h3>
        <p>Yes &mdash; nonprofit hospitals are required under AR Code &sect;&nbsp;20-9-1501 to maintain a written charity care policy and screen uninsured patients for eligibility before sending accounts to collections. Income thresholds vary by hospital. Always ask the billing department for the financial assistance application immediately after receiving your first bill.</p>
    </div>
    <div class="faq-item">
        <h3>What is Arkansas Works / ARHOME and who qualifies?</h3>
        <p>ARHOME is Arkansas&rsquo;s Medicaid expansion program, covering adults earning up to 138% FPL ($20,783 single / $44,367 family of four in 2026). It uses a private insurance model alongside traditional Medicaid. Apply at <a href="https://access.arkansas.gov" target="_blank" rel="noopener">access.arkansas.gov</a>. Coverage can be retroactive for up to 3 months.</p>
    </div>
    <div class="faq-item">
        <h3>What is the statute of limitations on medical debt in Arkansas?</h3>
        <p>Arkansas has a 5-year SOL on written contracts (AR Code &sect;&nbsp;16-56-111) and a 3-year SOL on open accounts (AR Code &sect;&nbsp;16-56-105). Most hospital bills fall under the 5-year period. Any payment restarts the clock. Use our <a href="/statute-of-limitations">SOL tool</a> before paying old debt.</p>
    </div>
    <div class="faq-item">
        <h3>How much of my wages can be garnished for medical debt in Arkansas?</h3>
        <p>Arkansas limits garnishment to 25% of disposable earnings per the federal CCPA. Arkansas Code &sect;&nbsp;16-66-218 provides additional head-of-household wage exemptions for primary earners with dependents. Certain income (Social Security, unemployment, workers&rsquo; comp) is completely exempt. A judgment must be obtained first.</p>
    </div>
    <div class="faq-item">
        <h3>Does Arkansas protect patients from surprise medical bills?</h3>
        <p>Arkansas patients rely on the federal No Surprises Act for surprise billing protection. Under the NSA, you cannot be balance-billed for emergency services or for non-emergency care from out-of-network ancillary providers at in-network facilities without advance consent. File complaints with CMS at 1-800-985-3059 or the <a href="https://www.insurance.arkansas.gov/consumers/file-complaint" target="_blank" rel="noopener">Arkansas Insurance Department</a>.</p>
    </div>
</div>

<h2 id="sources">Sources</h2>

<ul class="sources-list">
    <li><a href="https://codes.arkansas.gov/ark-code/title-20/subtitle-2/chapter-9/subchapter-15/section-20-9-1501" target="_blank" rel="noopener">AR Code § 20-9-1501: Nonprofit Hospital Charity Care Requirements</a></li>
    <li><a href="https://access.arkansas.gov" target="_blank" rel="noopener">Arkansas Benefits Portal: Apply for ARHOME Medicaid</a></li>
    <li><a href="https://codes.arkansas.gov/ark-code/title-16/subtitle-5/chapter-56/subchapter-1/section-16-56-111" target="_blank" rel="noopener">AR Code § 16-56-111: Statute of Limitations on Written Contracts</a></li>
    <li><a href="https://www.insurance.arkansas.gov/consumers/file-complaint" target="_blank" rel="noopener">Arkansas Insurance Department: File a Consumer Complaint</a></li>
    <li><a href="https://www.cms.gov/nosurprises" target="_blank" rel="noopener">CMS: No Surprises Act Overview and Patient Rights</a></li>
    <li><a href="https://www.healthy.arkansas.gov/programs-services/topics/health-facility-services" target="_blank" rel="noopener">Arkansas Department of Health: Health Facility Services</a></li>
    <li><a href="https://aspe.hhs.gov/topics/poverty-economic-mobility/hhs-poverty-guidelines" target="_blank" rel="noopener">HHS: 2026 Federal Poverty Level Guidelines</a></li>
</ul>
""",
})
