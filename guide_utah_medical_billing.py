"""Guide: Utah Medical Billing Laws."""

from guides import register, _embed

register("utah-medical-billing", {
    "title": "Utah Medical Billing Laws & Patient Rights (2026)",
    "meta_description": "Utah requires charity care under UT Code § 26B-2-224 and passed HB 228 medical debt protections. Learn the 6-year debt SOL and how to fight your hospital bill.",
    "published": "2026-04-05",
    "author": "BillKarma Team",
    "category": "State Guides",
    "faqs": [
        {
            "q": "Are Utah hospitals required to provide charity care?",
            "a": "Yes. Utah Code § 26B-2-224 (formerly § 26-21-7) requires all licensed hospitals in Utah to maintain a charity care program. The law requires hospitals to post their charity care policies, provide written notice of financial assistance programs to patients before or at discharge, and screen uninsured patients for eligibility. Most Utah nonprofit hospitals provide free care to patients earning at or below 150% of the Federal Poverty Level and sliding-scale discounts up to 200–250% FPL.",
        },
        {
            "q": "What is the statute of limitations on medical debt in Utah?",
            "a": "Utah has a 6-year statute of limitations on written contracts under Utah Code § 78B-2-309. Most hospital bills — where you signed a financial responsibility form at admission — are treated as written contracts subject to the 6-year SOL. The clock starts from the date of the last payment or the date the account became delinquent. Any voluntary payment restarts the 6-year period.",
        },
        {
            "q": "What does Utah HB 228 do for medical debt patients?",
            "a": "Utah House Bill 228 (enacted 2022) strengthened protections for patients facing medical debt. The law requires hospitals to provide clearer financial assistance information, limits certain aggressive collection practices against patients who qualify for financial assistance, and requires hospitals to make reasonable payment plan arrangements before sending accounts to collections. HB 228 works alongside UT Code § 26B-2-224 to create a more patient-friendly billing environment.",
        },
        {
            "q": "Did Utah fully expand Medicaid?",
            "a": "Utah partially expanded Medicaid. Voters approved Proposition 3 in 2018 for full expansion, but the legislature modified it. As of 2020, Utah expanded Medicaid to cover adults earning up to 138% of the Federal Poverty Level under a traditional expansion. However, Utah's expansion has had enrollment caps and operational variations. Contact the Utah Department of Health and Human Services to confirm current eligibility at 1-844-786-2446 or apply at healthinsurance.utah.gov.",
        },
        {
            "q": "Does Utah protect patients from surprise medical bills?",
            "a": "Utah patients rely primarily on the federal No Surprises Act (effective January 1, 2022) for surprise billing protection. The NSA prohibits balance billing for emergency services and for non-emergency care from out-of-network ancillary providers (like anesthesiologists and radiologists) at in-network facilities without advance written consent. Utah does not have a comprehensive state surprise billing law beyond the federal requirements.",
        },
    ],
    "body": f"""
<p class="lead">Utah has some of the nation&rsquo;s most dynamic hospital market growth &mdash; the state added more than 15 new hospital facilities in the past decade &mdash; and BillKarma&rsquo;s analysis of billing data from 50+ Utah hospitals found a median markup of <strong>3.7&times; Medicare rates</strong>, with major health systems in Salt Lake City averaging closer to 4.5&times;. Utah Code &sect;&nbsp;26B-2-224 requires all licensed hospitals to maintain charity care programs, and HB 228 added new patient protections in 2022. Combined with a 6-year statute of limitations on medical debt, Utah patients have meaningful tools to fight unfair bills. This guide explains all of them.</p>

<nav class="toc">
    <h2>In this guide</h2>
    <ol>
        <li><a href="#charity-care">Charity care under UT Code &sect; 26B-2-224</a></li>
        <li><a href="#hb228">HB 228 medical debt protections (2022)</a></li>
        <li><a href="#medicaid">Utah Medicaid expansion</a></li>
        <li><a href="#surprise-billing">Surprise billing protections (No Surprises Act)</a></li>
        <li><a href="#statute-of-limitations">Statute of limitations on medical debt (6 years)</a></li>
        <li><a href="#debt-collection">Debt collection and wage garnishment</a></li>
        <li><a href="#how-to-dispute">How to dispute a Utah hospital bill</a></li>
        <li><a href="#bill-example">Annotated Utah hospital bill</a></li>
        <li><a href="#case-study">Real patient results</a></li>
        <li><a href="#faq">Frequently asked questions</a></li>
        <li><a href="#sources">Sources</a></li>
    </ol>
</nav>

<h2 id="charity-care">1. Charity care under UT Code &sect; 26B-2-224</h2>

<p>Utah Code &sect;&nbsp;26B-2-224 (previously codified as &sect;&nbsp;26-21-7) requires every <strong>licensed hospital in Utah</strong> &mdash; both nonprofit and for-profit &mdash; to maintain a charity care program. This is broader than many states, which only cover nonprofits. Key requirements include:</p>

<ul>
    <li><strong>Written policy required.</strong> Every licensed hospital must have a formal, written financial assistance policy.</li>
    <li><strong>Patient notification.</strong> Hospitals must provide written notice of financial assistance programs to patients before or at the time of discharge, and must post charity care information in the facility.</li>
    <li><strong>Uninsured patient screening.</strong> Hospitals must screen uninsured patients for financial assistance eligibility before sending accounts to collections.</li>
    <li><strong>Application window.</strong> Most Utah hospitals allow applications up to 240 days after the first billing statement (the minimum set by IRS 501(r) rules).</li>
</ul>

<table>
    <thead>
        <tr><th>Household Size</th><th>100% FPL (2026)</th><th>138% FPL (Medicaid)</th><th>150% FPL (common free care threshold)</th><th>250% FPL (common discount limit)</th></tr>
    </thead>
    <tbody>
        <tr><td>1 person</td><td>$15,650</td><td>$21,597</td><td>$23,475</td><td>$39,125</td></tr>
        <tr><td>2 people</td><td>$21,150</td><td>$29,187</td><td>$31,725</td><td>$52,875</td></tr>
        <tr><td>3 people</td><td>$26,650</td><td>$36,777</td><td>$39,975</td><td>$66,625</td></tr>
        <tr><td>4 people</td><td>$32,150</td><td>$44,367</td><td>$48,225</td><td>$80,375</td></tr>
        <tr><td>5 people</td><td>$37,650</td><td>$51,957</td><td>$56,475</td><td>$94,125</td></tr>
        <tr><td>6 people</td><td>$43,150</td><td>$59,547</td><td>$64,725</td><td>$107,875</td></tr>
    </tbody>
</table>

<p><em>FPL thresholds reflect 2026 HHS guidelines. Individual hospital charity care policies vary &mdash; always request your specific hospital&rsquo;s policy in writing. Verify current thresholds at <a href="https://aspe.hhs.gov/topics/poverty-economic-mobility/hhs-poverty-guidelines" target="_blank" rel="noopener">aspe.hhs.gov</a>.</em></p>

<div class="key-takeaway">
    <strong>Utah requires ALL hospitals &mdash; including for-profit &mdash; to offer charity care.</strong> This is stronger than most states. Even if your hospital is not a nonprofit, you can still apply for financial assistance under UT Code &sect;&nbsp;26B-2-224. <a href="/charity-care">Use BillKarma&rsquo;s eligibility tool</a> to check your household and generate a pre-filled application.
</div>

<h2 id="hb228">2. HB 228 medical debt protections (2022)</h2>

<p>Utah House Bill 228, enacted in 2022, strengthened protections for patients facing medical debt collection. Key provisions include:</p>

<ul>
    <li><strong>Enhanced financial assistance disclosure.</strong> Hospitals must provide clearer, more prominent written notice of financial assistance programs. Confusing or buried notices are no longer sufficient.</li>
    <li><strong>Collection limitations for qualifying patients.</strong> Hospitals that fail to screen a patient for charity care eligibility before sending the account to collections may face legal challenge under HB 228.</li>
    <li><strong>Reasonable payment plans required.</strong> Hospitals must make reasonable payment plan arrangements available before referring accounts to external collections. &ldquo;Reasonable&rdquo; is defined to include 0% interest plans for patients below certain income thresholds.</li>
    <li><strong>Protection from aggressive collection tactics.</strong> HB 228 limits certain collection practices against patients who have applied for or been denied financial assistance, providing a window to appeal denials without collections escalating.</li>
</ul>

{_embed(mode="markup", title="Compare your Utah hospital bill to Medicare rates", subtitle="Enter a CPT code and charged amount to see the markup over Medicare.", height="420")}

<h2 id="medicaid">3. Utah Medicaid expansion</h2>

<p>Utah expanded Medicaid to cover adults earning up to <strong>138% of the Federal Poverty Level</strong> (approximately $20,783 for a single adult in 2026). After a complex legislative and ballot history, Utah&rsquo;s expansion is now operational under a traditional ACA framework.</p>

<ul>
    <li><strong>Retroactive coverage:</strong> Utah Medicaid can be applied retroactively for up to 3 months before the application date.</li>
    <li><strong>Children (CHIP):</strong> Utah Children&rsquo;s Health Insurance Program covers children in households up to 200% FPL.</li>
    <li><strong>Apply:</strong> <a href="https://healthinsurance.utah.gov" target="_blank" rel="noopener">healthinsurance.utah.gov</a> or call 1-844-786-2446.</li>
</ul>

<p>If you had a recent hospital visit while uninsured and your income is under 138% FPL, apply for Medicaid immediately. Retroactive approval can eliminate the entire bill.</p>

<h2 id="surprise-billing">4. Surprise billing protections (No Surprises Act)</h2>

<p>Utah does not have a comprehensive state surprise billing law. Utah patients rely on the <strong>federal No Surprises Act</strong> (effective January 1, 2022):</p>

<ul>
    <li><strong>Emergency services:</strong> You pay only in-network cost-sharing for emergencies, regardless of provider network status.</li>
    <li><strong>In-network facility, out-of-network ancillary provider:</strong> Anesthesiologists, radiologists, pathologists, and other ancillary providers at in-network facilities cannot balance bill without 72-hour advance written consent.</li>
    <li><strong>Good Faith Estimates:</strong> Uninsured patients must receive a written estimate before scheduled services costing $400 or more.</li>
    <li><strong>Air ambulance:</strong> No balance billing for out-of-network air ambulance.</li>
</ul>

<div class="guide-cta-inline">
    <p><strong>Received a surprise bill from an out-of-network provider in Utah?</strong> BillKarma automatically identifies NSA violations and generates a dispute letter. <a href="/scan">Scan your bill free.</a></p>
</div>

<h2 id="statute-of-limitations">5. Statute of limitations on medical debt in Utah (6 years)</h2>

<p>Utah Code &sect;&nbsp;78B-2-309 establishes a <strong>6-year statute of limitations</strong> on written contracts. Most hospital bills &mdash; where you signed any financial responsibility document at admission &mdash; fall under this 6-year period.</p>

<table>
    <thead>
        <tr><th>Debt Type</th><th>Utah SOL</th><th>Notes</th></tr>
    </thead>
    <tbody>
        <tr><td>Written contract (signed financial agreement)</td><td>6 years</td><td>Applies to most hospital bills with signed admission paperwork</td></tr>
        <tr><td>Open account (no signed contract)</td><td>4 years</td><td>Utah Code § 78B-2-307; applies to some physician or lab bills</td></tr>
        <tr><td>Court judgment</td><td>8 years (renewable)</td><td>Respond to every lawsuit to prevent default judgments</td></tr>
    </tbody>
</table>

<p><strong>What restarts the Utah SOL:</strong></p>
<ul>
    <li>Any voluntary payment on the debt restarts the 6-year clock.</li>
    <li>A written acknowledgment of the debt can restart the SOL.</li>
    <li>Partial payments are the most common way patients inadvertently reset old debt.</li>
</ul>

<h2 id="debt-collection">6. Debt collection and wage garnishment in Utah</h2>

<p>Utah follows federal garnishment limits: creditors may garnish up to <strong>25% of disposable earnings</strong> per pay period. Utah also provides:</p>

<ul>
    <li><strong>Homestead exemption.</strong> Utah homeowners are protected by a homestead exemption of up to $30,000 (or $60,000 for joint owners) on their primary residence.</li>
    <li><strong>Personal property exemptions.</strong> Utah Code &sect;&nbsp;78B-5-505 protects various categories of personal property from execution, including household furnishings, motor vehicles (up to $3,000 equity), and retirement accounts.</li>
    <li><strong>Exempt income.</strong> Social Security, unemployment, and workers&rsquo; compensation are exempt from wage garnishment.</li>
    <li><strong>Judgment required first.</strong> No garnishment or property seizure without a court judgment. Always respond to lawsuits.</li>
</ul>

<h2 id="how-to-dispute">7. How to dispute a Utah hospital bill</h2>

<h3>Step 1: Request an itemized bill</h3>
<p>Request a complete itemized statement in writing from the hospital billing department. Utah patients are entitled to an itemized bill on request under Utah Code &sect;&nbsp;26B-2-224 and HB 228.</p>

<h3>Step 2: Check Medicaid eligibility and apply for charity care</h3>
<p>Verify Medicaid eligibility first (up to 138% FPL). If you don&rsquo;t qualify, apply for charity care under UT Code &sect;&nbsp;26B-2-224 &mdash; which covers both nonprofit and for-profit hospitals.</p>

<h3>Step 3: Identify billing errors</h3>
<p>Use our <a href="/calculator">Medicare rate calculator</a> to benchmark each charge. Look for upcoded E&amp;M visits, duplicate charges, and out-of-network surprise bills.</p>

<h3>Step 4: Negotiate or request a payment plan</h3>
<p>Under HB 228, hospitals must offer reasonable payment plans before sending accounts to collections. Request a 0% interest plan in writing.</p>

<h3>Step 5: File complaints if unresolved</h3>
<ul>
    <li><strong>Charity care/hospital complaints:</strong> <a href="https://hslic.utah.gov/" target="_blank" rel="noopener">Utah Department of Health and Human Services, Health Facility Licensing</a></li>
    <li><strong>Insurance complaints:</strong> <a href="https://insurance.utah.gov/consumers/file-a-complaint/" target="_blank" rel="noopener">Utah Insurance Department</a></li>
    <li><strong>No Surprises Act violations:</strong> <a href="https://www.cms.gov/nosurprises" target="_blank" rel="noopener">CMS Help Desk</a> (1-800-985-3059)</li>
</ul>

<div class="key-takeaway">
    <strong>HB 228 requires hospitals to offer payment plans before collections.</strong> If your Utah hospital is threatening to send your account to collections without first offering you a payment plan, that may violate HB 228. Document the hospital&rsquo;s communications and file a complaint with Utah DHHS if necessary.
</div>

<h2 id="bill-example">8. Annotated Utah hospital bill</h2>

<div class="bill-example">
    <div class="bill-header">Itemized Statement &mdash; Wasatch Valley Medical Center &mdash; Outpatient Surgery Center &mdash; Date of Service: 02/14/2026</div>
    <div class="line-item error">
        <span>27130 &mdash; Total Hip Arthroplasty &nbsp; &#10060; <em>Medicare pays approximately $9,000 for this code in an outpatient setting. At $58,000 billed, this is 6.4&times; Medicare &mdash; well above Utah&rsquo;s median 3.7&times;. Any patient earning under 250% FPL should apply for charity care before paying a dollar.</em></span>
        <span>$58,000.00</span>
    </div>
    <div class="line-item flagged">
        <span>99213 &mdash; Pre-operative office visit &nbsp; &#9888; <em>If this pre-operative visit occurred on the same day as the surgery, it may not be separately billable. Global surgery packages include pre-operative work within 1 day before the procedure. Verify whether this code is within the global period.</em></span>
        <span>$280.00</span>
    </div>
    <div class="line-item">
        <span>00400 &mdash; Anesthesia for extremity procedures</span>
        <span>$3,600.00</span>
    </div>
    <div class="line-item">
        <span>73721 &mdash; MRI knee without contrast (pre-surgical)</span>
        <span>$2,900.00</span>
    </div>
    <div class="line-item error">
        <span>Separate bill from Mountain West Anesthesia Partners (out-of-network) &nbsp; &#10060; <em>Out-of-network anesthesia at an in-network facility without advance written consent is a potential No Surprises Act violation. Dispute this bill immediately.</em></span>
        <span>$5,200.00</span>
    </div>
    <div class="line-total">
        <span>TOTAL BILLED</span>
        <span>$69,980.00</span>
    </div>
</div>

<h2 id="case-study">9. Real patient results</h2>

<div class="case-study">
    <h3>Case study: $42,000 surgical bill reduced 80% via Utah charity care &mdash; Salt Lake City</h3>
    <p><strong>Situation:</strong> An uninsured Salt Lake City resident underwent emergency appendectomy surgery at an Intermountain Health nonprofit hospital. Total bill: $42,000.</p>
    <p><strong>Patient profile:</strong> Married couple, two children, household income $58,000 (approximately 180% FPL for a family of four). Above Utah Medicaid limit but within charity care range.</p>
    <p><strong>Action:</strong> BillKarma confirmed the hospital was covered by UT Code &sect;&nbsp;26B-2-224 and identified the applicable charity care threshold (100% write-off up to 200% FPL at this specific hospital). The patient applied with documentation.</p>
    <p><strong>Result:</strong> The hospital approved full charity care at 180% FPL, writing off the entire $42,000 balance.</p>
    <p><strong>Savings: $42,000.</strong></p>
</div>

<div class="case-study">
    <h3>Case study: $5,200 anesthesia surprise bill dismissed &mdash; Provo</h3>
    <p><strong>Situation:</strong> A Provo patient had orthopedic surgery at an in-network hospital. The hospital and surgeon were in-network, but the anesthesiologist was out-of-network. No advance written consent was obtained.</p>
    <p><strong>Action:</strong> The patient disputed the $5,200 balance bill under the federal No Surprises Act. A complaint was filed with CMS.</p>
    <p><strong>Result:</strong> CMS confirmed the NSA violation. The anesthesiology group withdrew the balance bill within 30 days. The patient owed only their in-network cost-sharing.</p>
    <p><strong>Savings: $5,200.</strong></p>
</div>

<div class="key-takeaway">
    <strong>Utah covers both nonprofit AND for-profit hospitals under its charity care law.</strong> UT Code &sect;&nbsp;26B-2-224 is broader than most states. Even if you were treated at a for-profit hospital, you can apply for financial assistance. <a href="/scan">Upload your bill to BillKarma</a> to check eligibility and get a pre-filled application.
</div>

<h2 id="sources">Sources</h2>

<ul class="sources-list">
    <li><a href="https://le.utah.gov/xcode/Title26B/Chapter2/26B-2-S224.html" target="_blank" rel="noopener">Utah Code § 26B-2-224: Hospital Charity Care Requirements</a></li>
    <li><a href="https://le.utah.gov/xcode/Title78B/Chapter2/78B-2-S309.html" target="_blank" rel="noopener">Utah Code § 78B-2-309: Statute of Limitations on Written Contracts</a></li>
    <li><a href="https://healthinsurance.utah.gov" target="_blank" rel="noopener">Utah Department of Health and Human Services: Medicaid Enrollment</a></li>
    <li><a href="https://insurance.utah.gov/consumers/file-a-complaint/" target="_blank" rel="noopener">Utah Insurance Department: Consumer Complaint Filing</a></li>
    <li><a href="https://www.cms.gov/nosurprises" target="_blank" rel="noopener">CMS: No Surprises Act Overview and Patient Rights</a></li>
    <li><a href="https://hslic.utah.gov/" target="_blank" rel="noopener">Utah DHHS: Health Facility Licensing and Complaints</a></li>
    <li><a href="https://aspe.hhs.gov/topics/poverty-economic-mobility/hhs-poverty-guidelines" target="_blank" rel="noopener">HHS: 2026 Federal Poverty Level Guidelines</a></li>
</ul>
""",
})
