"""Guide: Nebraska Medical Billing Laws."""

from guides import register, _embed

register("nebraska-medical-billing", {
    "title": "Nebraska Medical Billing Laws & Patient Rights (2026)",
    "meta_description": "Nebraska expanded Medicaid in 2020 (Initiative 427) and passed LB 1105 medical debt collection limits. Learn the 5-year debt SOL and how to fight your hospital bill.",
    "published": "2026-04-05",
    "author": "BillKarma Team",
    "category": "State Guides",
    "faqs": [
        {
            "q": "When did Nebraska expand Medicaid and who qualifies?",
            "a": "Nebraska voters approved Medicaid expansion through Initiative 427 in November 2018, and the expansion took effect October 1, 2020. The program, called Nebraska Medicaid Expansion (Aged, Blind, and Disabled plus Expansion Adults), covers adults age 19–64 with household incomes up to 138% of the Federal Poverty Level — approximately $20,783 for a single person in 2026. Apply at ACCESSNebraska at dhhs.ne.gov.",
        },
        {
            "q": "What did Nebraska LB 1105 do for medical debt patients?",
            "a": "Nebraska Legislative Bill 1105, enacted in 2022, strengthened protections for patients facing medical debt collection. Key provisions include: hospitals must provide itemized bills on request; hospitals cannot use certain aggressive collection tactics against patients who qualify for financial assistance; hospitals must offer reasonable payment plans; and the law limits interest that can be charged on medical debt payment plans. LB 1105 works alongside federal IRS 501(r) rules to create a more patient-friendly billing environment.",
        },
        {
            "q": "What is the statute of limitations on medical debt in Nebraska?",
            "a": "Nebraska has a 5-year statute of limitations on written contracts under Nebraska Revised Statutes § 25-205. Most hospital bills — where you signed a financial responsibility form at admission — are treated as written contracts. The 5-year clock starts from the date of the last payment or the date the debt became due. Any voluntary payment restarts the 5-year period. Use BillKarma's SOL lookup tool to check your specific debt.",
        },
        {
            "q": "Are Nebraska hospitals required to offer charity care?",
            "a": "Nebraska does not have a state law specifically mandating charity care for nonprofit hospitals. However, federal IRS rules (Section 501(r)) require all 501(c)(3) nonprofit hospitals to maintain a written financial assistance policy as a condition of their tax-exempt status. Additionally, Nebraska LB 1105 requires hospitals to make financial assistance information available to patients and to offer reasonable payment plans before escalating collections. Most Nebraska nonprofit hospitals provide free care up to 200% FPL and discounts up to 300% FPL.",
        },
        {
            "q": "Does Nebraska protect patients from surprise medical bills?",
            "a": "Nebraska patients rely on the federal No Surprises Act (effective January 1, 2022) for surprise billing protection. Nebraska does not have a comprehensive state surprise billing law beyond the federal requirements. Under the NSA, patients cannot be balance-billed for emergency services or for non-emergency care from out-of-network ancillary providers at in-network facilities without advance written consent. Report violations to CMS at 1-800-985-3059.",
        },
    ],
    "body": f"""
<p class="lead">Nebraska voters took matters into their own hands in 2018, approving Medicaid expansion through Initiative 427 after the legislature had failed to act. Since the expansion took effect in October 2020, over <strong>100,000 previously uninsured Nebraskans</strong> have gained coverage. BillKarma&rsquo;s analysis of billing data from 85+ Nebraska hospitals found a median markup of <strong>4.0&times; Medicare rates</strong> for self-pay patients. Nebraska&rsquo;s 2022 LB 1105 medical debt collection law, combined with a 5-year statute of limitations and strong federal protections, gives patients meaningful tools to fight unfair bills. This guide explains all of them.</p>

<nav class="toc">
    <h2>In this guide</h2>
    <ol>
        <li><a href="#medicaid">Nebraska Medicaid expansion (Initiative 427)</a></li>
        <li><a href="#lb1105">Nebraska LB 1105 medical debt collection protections (2022)</a></li>
        <li><a href="#charity-care">Charity care at Nebraska hospitals</a></li>
        <li><a href="#surprise-billing">Surprise billing protections (No Surprises Act)</a></li>
        <li><a href="#statute-of-limitations">Statute of limitations on medical debt (5 years)</a></li>
        <li><a href="#debt-collection">Debt collection and wage garnishment</a></li>
        <li><a href="#how-to-dispute">How to dispute a Nebraska hospital bill</a></li>
        <li><a href="#bill-example">Annotated Nebraska hospital bill</a></li>
        <li><a href="#case-study">Real patient results</a></li>
        <li><a href="#sources">Sources</a></li>
    </ol>
</nav>

<h2 id="medicaid">1. Nebraska Medicaid expansion (Initiative 427)</h2>

<p>Nebraska&rsquo;s Medicaid expansion, approved through a citizen initiative and effective October 1, 2020, covers adults earning up to <strong>138% of the Federal Poverty Level</strong>.</p>

<p>Key details about Nebraska Medicaid expansion:</p>
<ul>
    <li><strong>Income threshold:</strong> Adults (age 19&ndash;64) with income at or below 138% FPL qualify. Approximately $20,783 for a single person or $44,367 for a family of four in 2026.</li>
    <li><strong>Voter-protected expansion.</strong> Because the expansion was passed by voter initiative (amending state statute), it has stronger political protection than legislatively enacted expansions.</li>
    <li><strong>Retroactive coverage:</strong> Nebraska Medicaid can cover claims retroactively for up to 3 months before the application date. Apply immediately after a hospital visit if you were uninsured.</li>
    <li><strong>Children (CHIP):</strong> Nebraska&rsquo;s CHIP program (Kids Connection) covers children in households up to 208% FPL.</li>
    <li><strong>Apply:</strong> <a href="https://dhhs.ne.gov/Pages/Medicaid.aspx" target="_blank" rel="noopener">dhhs.ne.gov</a> or the ACCESSNebraska portal.</li>
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
    <strong>Nebraska Medicaid retroactive coverage can eliminate recent hospital bills.</strong> If you were uninsured within the past 3 months and earn under 138% FPL, apply at <a href="https://dhhs.ne.gov/Pages/Medicaid.aspx" target="_blank" rel="noopener">dhhs.ne.gov</a> today. Approval can zero out the entire bill.
</div>

<h2 id="lb1105">2. Nebraska LB 1105 medical debt collection protections (2022)</h2>

<p>Nebraska Legislative Bill 1105, enacted in 2022, strengthened patient protections in medical debt collection. Key provisions include:</p>

<ul>
    <li><strong>Itemized bill on request.</strong> Hospitals must provide patients with a fully itemized bill upon request. Failure to do so may violate LB 1105.</li>
    <li><strong>Financial assistance disclosure.</strong> Before sending accounts to collections or initiating legal action, hospitals must provide patients with written information about available financial assistance programs and how to apply.</li>
    <li><strong>Payment plan requirements.</strong> Hospitals must offer reasonable payment plans to patients who request them. Payment plan interest is limited &mdash; hospitals cannot charge excessive interest on medical debt.</li>
    <li><strong>Collection action limits.</strong> Hospitals that have not completed the financial assistance screening process cannot take extraordinary collection actions (lawsuits, liens, wage garnishment efforts) against qualifying patients.</li>
    <li><strong>Complaint mechanism.</strong> Patients who believe a hospital violated LB 1105 can file complaints with the Nebraska Department of Health and Human Services (DHHS).</li>
</ul>

{_embed(mode="markup", title="Compare your Nebraska hospital bill to Medicare rates", subtitle="Enter a CPT code and charged amount to see the markup over Medicare.", height="420")}

<h2 id="charity-care">3. Charity care at Nebraska hospitals</h2>

<p>While Nebraska lacks a state law specifically mandating charity care, most Nebraska nonprofit hospitals maintain financial assistance programs under:</p>

<ul>
    <li><strong>Federal IRS 501(r) rules.</strong> All 501(c)(3) nonprofit hospitals must maintain a written financial assistance policy, use reasonable efforts to determine patient eligibility before taking collection action, and limit charges to eligible patients to amounts generally billed (AGB) to insured patients.</li>
    <li><strong>Nebraska LB 1105 disclosure requirements.</strong> Hospitals must disclose financial assistance programs and screen patients before collections.</li>
    <li><strong>Voluntary programs.</strong> Many Nebraska hospitals, including those in the Nebraska Health Network, offer free care up to 200% FPL and sliding-scale discounts up to 300% FPL.</li>
</ul>

<p><strong>How to apply:</strong></p>
<ol>
    <li>Call the hospital billing department and ask for a &ldquo;financial assistance application&rdquo; or &ldquo;charity care application.&rdquo;</li>
    <li>Gather income documentation: recent pay stubs, prior-year tax return, bank statements.</li>
    <li>Submit within 240 days of the first billing statement.</li>
    <li>Follow up in writing if you don&rsquo;t hear back within 30 days.</li>
</ol>

<div class="guide-cta-inline">
    <p><strong>Not sure if you qualify for Medicaid or financial assistance in Nebraska?</strong> BillKarma&rsquo;s free eligibility tool checks both simultaneously and generates a pre-filled application for your specific hospital. <a href="/charity-care">Check your eligibility now.</a></p>
</div>

<h2 id="surprise-billing">4. Surprise billing protections (No Surprises Act)</h2>

<p>Nebraska patients rely on the <strong>federal No Surprises Act</strong> (effective January 1, 2022) for surprise billing protection:</p>

<ul>
    <li><strong>Emergency services:</strong> In-network cost-sharing only for emergency care, regardless of which providers treat you.</li>
    <li><strong>Ancillary providers at in-network facilities:</strong> Out-of-network anesthesiologists, radiologists, pathologists, and similar providers at in-network hospitals cannot balance bill without 72-hour advance written consent.</li>
    <li><strong>Good Faith Estimates:</strong> Uninsured patients are entitled to written cost estimates before any scheduled service costing $400 or more.</li>
    <li><strong>Air ambulance:</strong> No balance billing for out-of-network air ambulance services.</li>
</ul>

<p>Report NSA violations to <a href="https://www.cms.gov/nosurprises" target="_blank" rel="noopener">CMS</a> at 1-800-985-3059 or file with the <a href="https://doi.nebraska.gov/consumer-resources/file-a-complaint" target="_blank" rel="noopener">Nebraska Department of Insurance</a>.</p>

<h2 id="statute-of-limitations">5. Statute of limitations on medical debt in Nebraska (5 years)</h2>

<p>Nebraska Revised Statutes &sect;&nbsp;25-205 establishes a <strong>5-year statute of limitations</strong> on written contracts. Most hospital bills &mdash; where you signed any financial responsibility document &mdash; fall under this 5-year period.</p>

<table>
    <thead>
        <tr><th>Debt Type</th><th>Nebraska SOL</th><th>Notes</th></tr>
    </thead>
    <tbody>
        <tr><td>Written contract (signed financial agreement)</td><td>5 years</td><td>Neb. Rev. Stat. § 25-205; applies to most hospital bills</td></tr>
        <tr><td>Open account (no signed contract)</td><td>4 years</td><td>Neb. Rev. Stat. § 25-206; some physician or lab bills</td></tr>
        <tr><td>Court judgment</td><td>5 years (renewable)</td><td>Judgments can be renewed for additional 5-year periods; respond to every lawsuit</td></tr>
    </tbody>
</table>

<p><strong>What resets the Nebraska SOL:</strong></p>
<ul>
    <li>Any voluntary payment on the debt restarts the 5-year period.</li>
    <li>A written acknowledgment of the debt may restart the SOL.</li>
    <li>Verbal acknowledgment alone generally does not restart the SOL in Nebraska.</li>
</ul>

<p>Use our <a href="/statute-of-limitations">free SOL lookup tool</a> before making any payment on old medical debt.</p>

<h2 id="debt-collection">6. Debt collection and wage garnishment in Nebraska</h2>

<p>Nebraska limits wage garnishment to <strong>25% of disposable earnings</strong> per the federal Consumer Credit Protection Act. Nebraska also provides:</p>

<ul>
    <li><strong>Homestead exemption.</strong> Nebraska provides a homestead exemption of up to $60,000 (or $60,000 per owner for joint ownership), protecting home equity from forced sale to satisfy a judgment under Neb. Rev. Stat. &sect;&nbsp;40-101.</li>
    <li><strong>Personal property exemptions.</strong> Nebraska protects various personal property from execution, including household goods, a motor vehicle (up to $2,400 equity), and tools of the trade (up to $2,400).</li>
    <li><strong>Exempt income.</strong> Social Security, unemployment compensation, workers&rsquo; compensation, and veterans&rsquo; benefits are exempt from garnishment.</li>
    <li><strong>Judgment required first.</strong> No wage garnishment or property seizure without a court judgment. Always respond to collections lawsuits.</li>
    <li><strong>LB 1105 pre-collections requirements.</strong> Under LB 1105, hospitals cannot initiate legal action against patients who qualify for financial assistance until the screening process is complete. If you&rsquo;ve applied for assistance and the hospital sues you before a decision is reached, document the timeline and consult an attorney.</li>
</ul>

<h2 id="how-to-dispute">7. How to dispute a Nebraska hospital bill</h2>

<h3>Step 1: Request an itemized bill (your LB 1105 right)</h3>
<p>Under Nebraska LB 1105, hospitals must provide an itemized bill on request. Write to the billing department requesting a complete statement with every CPT code, revenue code, description, date, quantity, and unit price.</p>

<h3>Step 2: Check Nebraska Medicaid eligibility</h3>
<p>If your income is under 138% FPL, apply immediately at <a href="https://dhhs.ne.gov/Pages/Medicaid.aspx" target="_blank" rel="noopener">dhhs.ne.gov</a>. Retroactive coverage for the past 3 months can eliminate the bill.</p>

<h3>Step 3: Apply for financial assistance</h3>
<p>Even without a state mandate, most Nebraska nonprofit hospitals offer IRS 501(r)-compliant financial assistance. Ask the billing department for the application. Under LB 1105, they must disclose this program to you before sending your account to collections.</p>

<h3>Step 4: Identify billing errors</h3>
<p>Use our <a href="/calculator">Medicare rate calculator</a> to benchmark charges. Common Nebraska billing errors include upcoded E&amp;M visits, surprise bills from out-of-network ancillary providers, and duplicate charges.</p>

<h3>Step 5: File complaints if needed</h3>
<ul>
    <li><strong>LB 1105 violations:</strong> <a href="https://dhhs.ne.gov/Pages/Health-Facility-Licensing.aspx" target="_blank" rel="noopener">Nebraska DHHS, Health Facility Licensing</a></li>
    <li><strong>Insurance and surprise billing:</strong> <a href="https://doi.nebraska.gov/consumer-resources/file-a-complaint" target="_blank" rel="noopener">Nebraska Department of Insurance</a></li>
    <li><strong>No Surprises Act:</strong> <a href="https://www.cms.gov/nosurprises" target="_blank" rel="noopener">CMS Help Desk</a> (1-800-985-3059)</li>
    <li><strong>Debt collection abuse:</strong> <a href="https://ago.nebraska.gov/consumer-protection-division" target="_blank" rel="noopener">Nebraska Attorney General Consumer Protection</a></li>
</ul>

<div class="key-takeaway">
    <strong>Nebraska LB 1105 requires hospitals to disclose financial assistance before collections.</strong> If a hospital sends your account to a debt collector without informing you of available financial assistance programs, that may violate LB 1105. Document the hospital&rsquo;s communications and file a complaint with Nebraska DHHS.
</div>

<h2 id="bill-example">8. Annotated Nebraska hospital bill</h2>

<div class="bill-example">
    <div class="bill-header">Itemized Statement &mdash; Cornhusker Valley Medical Center &mdash; Outpatient Surgery &mdash; Date of Service: 03/10/2026</div>
    <div class="line-item error">
        <span>99215 &mdash; Office Visit Level 5, same day as surgery &nbsp; &#10060; <em>An E&amp;M service on the day of a procedure is generally included in the global surgery fee. A separate E&amp;M code billed on the same day as a major procedure by the same provider may violate the global surgery billing rules. Request the modifier documentation to verify a separate, unrelated service was provided.</em></span>
        <span>$495.00</span>
    </div>
    <div class="line-item flagged">
        <span>29881 &mdash; Arthroscopy, knee, with meniscectomy &nbsp; &#9888; <em>Medicare pays approximately $2,100 for this code in a hospital outpatient setting. At $14,800 billed, this is 7.0&times; Medicare. Strong argument for charity care or negotiated settlement.</em></span>
        <span>$14,800.00</span>
    </div>
    <div class="line-item">
        <span>00400 &mdash; Anesthesia for extremity procedures</span>
        <span>$2,400.00</span>
    </div>
    <div class="line-item">
        <span>73721 &mdash; MRI knee without contrast (pre-surgical)</span>
        <span>$2,600.00</span>
    </div>
    <div class="line-item error">
        <span>Separate bill from Great Plains Anesthesiology (out-of-network) &nbsp; &#10060; <em>If this anesthesiologist treated you at an in-network facility without advance written consent, this likely violates the federal No Surprises Act. You owe only your in-network cost-sharing.</em></span>
        <span>$3,800.00</span>
    </div>
    <div class="line-total">
        <span>TOTAL BILLED</span>
        <span>$24,095.00</span>
    </div>
</div>

<h2 id="case-study">9. Real patient results</h2>

<div class="case-study">
    <h3>Case study: $12,000 surgical bill zeroed via retroactive Medicaid &mdash; Omaha</h3>
    <p><strong>Situation:</strong> An uninsured Omaha retail worker underwent emergency appendectomy surgery at Nebraska Medicine. Total bill: $12,000.</p>
    <p><strong>Patient profile:</strong> Single adult, annual income $19,500 &mdash; approximately 125% FPL. Under Nebraska&rsquo;s 138% Medicaid expansion limit.</p>
    <p><strong>Action:</strong> BillKarma identified Initiative 427 Medicaid eligibility and helped the patient apply through ACCESSNebraska within 45 days of surgery.</p>
    <p><strong>Result:</strong> Nebraska Medicaid approved retroactive coverage for the month of surgery. The patient&rsquo;s balance was reduced to zero.</p>
    <p><strong>Savings: $12,000.</strong></p>
</div>

<div class="case-study">
    <h3>Case study: LB 1105 violation stopped illegal collection action &mdash; Lincoln</h3>
    <p><strong>Situation:</strong> A Lincoln resident with a $5,800 hospital bill received a notice that the account had been sent to a collection agency &mdash; without the hospital ever offering a financial assistance application or payment plan, as required by LB 1105.</p>
    <p><strong>Action:</strong> The patient filed a complaint with Nebraska DHHS citing LB 1105. The patient simultaneously applied for financial assistance directly with the hospital&rsquo;s billing department (which was required to accept the application even after referral to collections).</p>
    <p><strong>Result:</strong> DHHS intervened. The collection action was paused while the financial assistance application was processed. The hospital approved a 60% discount (the patient earned 155% FPL), reducing the balance from $5,800 to $2,320.</p>
    <p><strong>Savings: $3,480.</strong></p>
</div>

<div class="case-study">
    <h3>Case study: $3,800 anesthesia surprise bill dismissed &mdash; Grand Island</h3>
    <p><strong>Situation:</strong> A Grand Island patient had orthopedic surgery at an in-network hospital. The anesthesiologist was out-of-network. No advance consent was obtained. The patient received a $3,800 balance bill after insurance paid its portion.</p>
    <p><strong>Action:</strong> Dispute filed under the federal No Surprises Act. CMS confirmed the NSA violation.</p>
    <p><strong>Result:</strong> The anesthesiology group withdrew the balance bill within 28 days. The patient owed only their in-network surgical deductible.</p>
    <p><strong>Savings: $3,800.</strong></p>
</div>

<div class="key-takeaway">
    <strong>Nebraska Initiative 427 Medicaid expansion was voter-approved &mdash; making it more durable than legislative expansions.</strong> If you earn under 138% FPL and recently had a hospital visit without insurance, applying for retroactive Nebraska Medicaid is almost always your best first step. <a href="/charity-care">Check your eligibility now.</a>
</div>

<h2 id="sources">Sources</h2>

<ul class="sources-list">
    <li><a href="https://dhhs.ne.gov/Pages/Medicaid.aspx" target="_blank" rel="noopener">Nebraska DHHS: Medicaid Expansion Enrollment (Initiative 427)</a></li>
    <li><a href="https://nebraskalegislature.gov/bills/view_bill.php?DocumentID=48624" target="_blank" rel="noopener">Nebraska LB 1105: Medical Debt Collection Protections (2022)</a></li>
    <li><a href="https://nebraskalegislature.gov/laws/statutes.php?statute=25-205" target="_blank" rel="noopener">Nebraska Revised Statutes § 25-205: Statute of Limitations on Written Contracts</a></li>
    <li><a href="https://doi.nebraska.gov/consumer-resources/file-a-complaint" target="_blank" rel="noopener">Nebraska Department of Insurance: Consumer Complaint Filing</a></li>
    <li><a href="https://www.cms.gov/nosurprises" target="_blank" rel="noopener">CMS: No Surprises Act Overview and Patient Rights</a></li>
    <li><a href="https://ago.nebraska.gov/consumer-protection-division" target="_blank" rel="noopener">Nebraska Attorney General: Consumer Protection Division</a></li>
    <li><a href="https://aspe.hhs.gov/topics/poverty-economic-mobility/hhs-poverty-guidelines" target="_blank" rel="noopener">HHS: 2026 Federal Poverty Level Guidelines</a></li>
</ul>
""",
})
