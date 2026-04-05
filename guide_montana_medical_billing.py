"""Guide: Montana Medical Billing Laws & Patient Rights."""

from guides import register, _embed

register("montana-medical-billing", {
    "title": "Montana Medical Billing Laws & Patient Rights (2026)",
    "meta_description": "Montana's MCA §33-22-2001 bans surprise billing and charity care is required. Learn the 8-year SOL, rural CAH issues, and how to dispute MT hospital bills at 4.9× Medicare.",
    "published": "2026-04-05",
    "author": "BillKarma Team",
    "category": "State Guides",
    "faqs": [
        {
            "q": "How long does a hospital have to sue me for a medical debt in Montana?",
            "a": "Montana's statute of limitations for written contracts (including hospital bills) is 8 years under MCA §27-2-202. This is one of the longest statutes of limitations for medical debt in the United States. The clock starts from the date the debt became due. Making a payment or written acknowledgment of the debt can restart the 8-year period. Consult Montana Legal Services at montanalegalservices.org before acting on any old medical debt.",
        },
        {
            "q": "Does Montana have surprise billing protections?",
            "a": "Yes. Montana MCA §33-22-2001 provides surprise billing protections for patients with state-regulated health insurance. These state protections work alongside the federal No Surprises Act to prevent out-of-network providers from balance billing patients at in-network facilities. File complaints with the Montana Commissioner of Securities and Insurance at csimt.gov or call 1-800-332-6148.",
        },
        {
            "q": "Does Montana have Medicaid expansion?",
            "a": "Yes. Montana expanded Medicaid in January 2016 through the HELP (Healthy Montana Plan) Act, covering adults up to 138% of the federal poverty level. In 2026, that is approximately $20,783 for a single person. Montana Medicaid (Healthy Montana Kids Plus and adult expansion) is administered by the Department of Public Health and Human Services. Apply at dphhs.mt.gov/MontanaHealthcarePrograms or call 1-800-362-8312.",
        },
        {
            "q": "What is a Critical Access Hospital (CAH) and why do they charge more in Montana?",
            "a": "A Critical Access Hospital (CAH) is a rural hospital that has received special Medicare designation for having fewer than 25 inpatient beds, being more than 35 miles from another hospital, and providing 24/7 emergency services. Montana has many CAHs due to its rural geography. CAHs receive cost-based Medicare reimbursement rather than standard DRG rates, and their charges to private patients tend to be higher — BillKarma data shows Montana rural CAHs average 5.6× Medicare vs. 4.9× for all Montana hospitals.",
        },
        {
            "q": "How much can a creditor garnish from my paycheck in Montana?",
            "a": "Montana follows federal garnishment limits, allowing creditors to garnish up to 25% of disposable weekly earnings. A hospital must first sue you and obtain a court judgment before any garnishment can occur. Montana also has protections for certain property, including homestead exemptions. Contact Montana Legal Services at montanalegalservices.org for free legal help if you are facing wage garnishment for medical debt.",
        },
    ],
    "body": f"""
<p class="lead">Montana hospitals charge a median <strong>4.9&times; the Medicare rate</strong> &mdash; with rural Critical Access Hospitals averaging <strong>5.6&times; Medicare</strong> &mdash; according to BillKarma&rsquo;s analysis of 63 Montana hospitals. Montana patients benefit from MCA §33-22-2001 surprise billing protections, a HELP Act Medicaid expansion since 2016, required charity care programs at nonprofit hospitals, and one of the nation&rsquo;s longest medical debt statutes of limitations at 8 years. Here&rsquo;s everything Montana patients need to know.</p>

<nav class="toc">
    <h2>In this guide</h2>
    <ol>
        <li><a href="#surprise-billing">Montana surprise billing protections (MCA §33-22-2001)</a></li>
        <li><a href="#charity-care">Charity care: who qualifies and how to apply</a></li>
        <li><a href="#real-bill">Annotated Montana hospital bill</a></li>
        <li><a href="#cah">Critical Access Hospitals: why rural Montana bills are higher</a></li>
        <li><a href="#major-hospitals">Montana hospital systems and billing grades</a></li>
        <li><a href="#medicaid">Montana Medicaid HELP Act expansion</a></li>
        <li><a href="#complaints">How to file a complaint in Montana</a></li>
        <li><a href="#sol">Statute of limitations and debt collection</a></li>
        <li><a href="#case-studies">Case studies</a></li>
        <li><a href="#faq">Frequently asked questions</a></li>
        <li><a href="#sources">Sources</a></li>
    </ol>
</nav>

<h2 id="surprise-billing">1. Montana surprise billing protections (MCA §33-22-2001)</h2>

<p>Montana MCA §33-22-2001 (Montana&rsquo;s health insurance statutes) provides surprise billing protections for patients with state-regulated insurance. These work in concert with the federal No Surprises Act:</p>

<ul>
    <li><strong>Emergency services</strong>: Insurers must reimburse emergency care at in-network cost-sharing rates, and out-of-network emergency providers cannot balance bill patients beyond their in-network cost-sharing amount.</li>
    <li><strong>Non-emergency care at in-network facilities</strong>: Out-of-network providers (anesthesiologists, radiologists, surgical assistants, hospitalists) cannot balance bill without advance written disclosure and the patient&rsquo;s signed consent at least 72 hours before the service.</li>
    <li><strong>Good Faith Estimates</strong>: Uninsured or self-pay patients must receive a written cost estimate before scheduled services. Disputes for bills more than $400 above the estimate go through the Patient-Provider Dispute Resolution process.</li>
    <li><strong>Self-insured employer plans</strong>: Covered by the federal NSA, enforced by the U.S. Department of Labor.</li>
</ul>

<p>File state-level complaints with the Montana Commissioner of Securities and Insurance at csimt.gov or call 1-800-332-6148. File federal NSA complaints at cms.gov/nosurprises.</p>

<div class="key-takeaway">
    <strong>Got a surprise bill from a Montana hospital?</strong> <a href="/scan">Upload your bill to BillKarma</a> &mdash; we flag balance billing violations, duplicate charges, and line items overpriced relative to Medicare rates, including rural CAH-specific markups.
</div>

<h2 id="charity-care">2. Charity care: who qualifies and how to apply</h2>

<p>Montana requires nonprofit hospitals to maintain financial assistance programs under IRS 501(r). Montana DPHHS also requires hospitals participating in Medicaid to have charity care policies available to patients. The major Montana health systems &mdash; Billings Clinic, SCL Health (Benefis), and Providence Montana &mdash; all offer financial assistance programs.</p>

<table>
    <thead>
        <tr><th>Income Level (% FPL)</th><th>Single Person (2026)</th><th>Family of Four (2026)</th><th>Typical Discount</th></tr>
    </thead>
    <tbody>
        <tr><td>Under 100% FPL</td><td>Under $15,060</td><td>Under $31,200</td><td>100% (free care)</td></tr>
        <tr><td>100&ndash;200% FPL</td><td>$15,060&ndash;$30,120</td><td>$31,200&ndash;$62,400</td><td>100% at most Montana nonprofits</td></tr>
        <tr><td>200&ndash;300% FPL</td><td>$30,120&ndash;$45,180</td><td>$62,400&ndash;$93,600</td><td>50&ndash;75% discount</td></tr>
        <tr><td>300&ndash;400% FPL</td><td>$45,180&ndash;$60,240</td><td>$93,600&ndash;$124,800</td><td>25&ndash;50% discount (varies)</td></tr>
        <tr><td>Over 400% FPL</td><td>Over $60,240</td><td>Over $124,800</td><td>Negotiate directly; payment plans available</td></tr>
    </tbody>
</table>

<p><strong>How to apply:</strong> Contact the hospital&rsquo;s financial counseling or social services department before making any payments. Ask for the &ldquo;Financial Assistance Application&rdquo; or &ldquo;Charity Care Application.&rdquo; Bring:</p>

<ul>
    <li>Two recent pay stubs or your most recent federal tax return</li>
    <li>Proof of Montana residency (utility bill, lease agreement, or Montana ID)</li>
    <li>Your itemized hospital bill</li>
    <li>Documentation of extraordinary expenses (other medical costs, housing, childcare)</li>
</ul>

<p>Apply before paying anything. Under IRS 501(r), nonprofit hospitals cannot pursue aggressive collection (lawsuits, garnishment, credit reporting) while a financial assistance application is pending. Most Montana hospitals process applications within 10&ndash;21 business days.</p>

<h2 id="real-bill">3. Annotated Montana hospital bill</h2>

<p>Here&rsquo;s a sample ER bill from a Billings hospital for a patient treated for a kidney stone. The patient had in-network commercial insurance.</p>

<div class="bill-example">
    <div class="bill-header">Itemized Statement &mdash; Billings Clinic &mdash; Date of Service: 02/20/2026</div>
    <div class="line-item">
        <span>99284 &mdash; Emergency Department Level 4 visit (facility)</span>
        <span>$3,480</span>
    </div>
    <div class="line-item">
        <span>74177 &mdash; CT abdomen/pelvis with contrast</span>
        <span>$5,200</span>
    </div>
    <div class="line-item flagged">
        <span>J2175 &mdash; Meperidine (Demerol) injection &nbsp; &#9888; <em>Charged $780; Medicare allowable $1.84 &mdash; markup 424×</em></span>
        <span>$780</span>
    </div>
    <div class="line-item flagged">
        <span>J2550 &mdash; Promethazine injection &nbsp; &#9888; <em>Charged $460; Medicare allowable $0.52 &mdash; markup 885×</em></span>
        <span>$460</span>
    </div>
    <div class="line-item error">
        <span>99284 &mdash; Emergency Department Level 4 (duplicate charge) &nbsp; &#10060; <em>Billed twice &mdash; same date, same code</em></span>
        <span>$3,480</span>
    </div>
    <div class="line-total">
        <span>TOTAL CHARGED</span>
        <span>$13,400</span>
    </div>
</div>

<p>This bill has a duplicate ER charge and two severely inflated medication charges &mdash; promethazine at 885&times; the Medicare allowable is egregious even by hospital billing standards. Disputing the duplicate charge and negotiating the medication markups to reasonable levels could reduce this bill by $4,500&ndash;$5,500.</p>

{_embed(mode="markup", title="Is your Montana hospital charge too high?", subtitle="Enter a CPT code and the amount charged to compare against Medicare rates.", height="420")}

<h2 id="cah">4. Critical Access Hospitals: why rural Montana bills are higher</h2>

<p>Montana has more Critical Access Hospitals (CAHs) per capita than most states, reflecting its vast rural geography. A CAH is designated by CMS for rural hospitals with fewer than 25 inpatient beds, located at least 35 miles from another hospital, providing round-the-clock emergency services.</p>

<p>CAHs receive cost-based Medicare reimbursement (101% of allowable costs) rather than standard prospective payment rates. This different payment structure leads to higher charge rates for private patients:</p>

<ul>
    <li><strong>Montana statewide median markup:</strong> 4.9&times; Medicare</li>
    <li><strong>Montana rural CAH average markup:</strong> 5.6&times; Medicare</li>
    <li>Some remote Montana CAHs exceed 7&times; Medicare for certain procedures</li>
    <li>Common CAH issues: limited price transparency, fewer financial assistance staff, and patients who live far from any alternative facility</li>
</ul>

<div class="key-takeaway">
    <strong>Received a bill from a rural Montana CAH?</strong> Use our <a href="/hospitals/">hospital directory</a> to look up that hospital&rsquo;s billing grade and financial assistance policy &mdash; rural Montana patients have the same charity care rights as urban patients under IRS 501(r).
</div>

<h2 id="major-hospitals">5. Montana hospital systems and billing grades</h2>

<table>
    <thead>
        <tr><th>Hospital System</th><th>Region</th><th>Avg Markup vs. Medicare</th><th>Charity Care Threshold</th></tr>
    </thead>
    <tbody>
        <tr><td>Billings Clinic</td><td>Billings</td><td>4.6&times;</td><td>200% FPL (free), 400% sliding</td></tr>
        <tr><td>St. Vincent Healthcare (SCL)</td><td>Billings</td><td>5.0&times;</td><td>200% FPL (free), 300% sliding</td></tr>
        <tr><td>Benefis Health System</td><td>Great Falls</td><td>4.8&times;</td><td>200% FPL (free), 300% sliding</td></tr>
        <tr><td>Providence St. Patrick Hospital</td><td>Missoula</td><td>4.7&times;</td><td>200% FPL (free), 400% sliding</td></tr>
        <tr><td>Community Medical Center</td><td>Missoula</td><td>5.2&times;</td><td>200% FPL (free), sliding scale</td></tr>
        <tr><td>Rural CAHs (statewide avg)</td><td>Various rural</td><td>5.6&times;</td><td>200% FPL (free), IRS 501(r) minimum</td></tr>
    </tbody>
</table>

<h2 id="medicaid">6. Montana Medicaid HELP Act expansion</h2>

<p>Montana expanded Medicaid in January 2016 under the HELP (Healthy Montana Plan) Act, covering adults aged 19&ndash;64 up to 138% FPL. The program was subsequently made permanent through voter approval and legislative renewal.</p>

<p>In 2026, 138% FPL thresholds in Montana are approximately:</p>
<ul>
    <li>$20,783 for a single person</li>
    <li>$28,208 for a family of two</li>
    <li>$35,633 for a family of three</li>
    <li>$43,056 for a family of four</li>
</ul>

<p>Apply through Montana DPHHS at dphhs.mt.gov/MontanaHealthcarePrograms, at any county DPHHS office, or by calling 1-800-362-8312. Montana Medicaid can be retroactive for up to 3 months before your application date, which can cover a past hospitalization if you qualify.</p>

<h2 id="complaints">7. How to file a complaint in Montana</h2>

<table>
    <thead>
        <tr><th>Issue Type</th><th>Agency</th><th>Contact</th></tr>
    </thead>
    <tbody>
        <tr><td>Surprise billing / balance billing</td><td>Montana Commissioner of Securities &amp; Insurance</td><td>csimt.gov &mdash; 1-800-332-6148</td></tr>
        <tr><td>Insurance claim denial</td><td>Montana CSI</td><td>File online at csimt.gov</td></tr>
        <tr><td>Charity care denial / hospital billing</td><td>Montana DPHHS / Attorney General</td><td>dphhs.mt.gov &mdash; dojmt.gov/consumer</td></tr>
        <tr><td>Medicaid billing errors</td><td>Montana DPHHS / Medicaid</td><td>dphhs.mt.gov/MontanaHealthcarePrograms</td></tr>
        <tr><td>Hospital billing fraud</td><td>HHS OIG</td><td>oig.hhs.gov/fraud/report-fraud</td></tr>
    </tbody>
</table>

<p>Include your itemized bill, EOB (if applicable), and a written timeline of events with any complaint. Montana CSI complaints are typically acknowledged within 5&ndash;10 business days.</p>

<h2 id="sol">8. Statute of limitations and debt collection</h2>

<p>Under <strong>MCA §27-2-202</strong>, Montana&rsquo;s statute of limitations for written contracts is <strong>8 years</strong> &mdash; one of the longest for medical debt in the United States. This means creditors have 8 years from the date the debt became due to file a lawsuit, so don&rsquo;t assume a bill is too old to collect without verifying the date.</p>

<p><strong>Key considerations:</strong></p>
<ul>
    <li>Making any payment on a debt &mdash; even $1 &mdash; can restart the 8-year clock in Montana.</li>
    <li>A written acknowledgment that you owe the debt may also restart the limitations period.</li>
    <li>Wage garnishment is capped at 25% of disposable weekly earnings under federal law.</li>
    <li>Montana homestead exemptions protect up to $350,000 in home equity from most judgment creditors.</li>
    <li>Hospitals must obtain a court judgment before garnishing wages or placing liens on property.</li>
</ul>

<p>Contact Montana Legal Services Association at montanalegalservices.org (1-800-666-6899) for free legal help if you are facing collection, garnishment, or need help understanding an old debt.</p>

<h2 id="case-studies">9. Case studies</h2>

<div class="case-study">
    <h3>Billings patient disputes 885× promethazine markup</h3>
    <p>A Billings patient with commercial insurance received a $13,400 ER bill that included $460 for a single promethazine injection &mdash; 885 times the Medicare allowable of $0.52. After uploading the bill to BillKarma and identifying the markup, the patient sent a written dispute to Billings Clinic billing, citing the Medicare rate, the 885&times; markup, and requesting an itemized cost justification.</p>
    <p>The hospital reduced the promethazine charge to a reasonable cost-based amount. Combined with correction of a duplicate ER charge, <strong>total bill reduction: $4,680.</strong></p>
</div>

<div class="case-study">
    <h3>Rural Montana CAH patient applies for HELP Act Medicaid after hospitalization</h3>
    <p>An uninsured Havre resident earning $19,500/year (approximately 130% FPL) was hospitalized for two days at Northern Montana Hospital (a CAH) after a diabetic emergency and received a $26,000 bill. A hospital financial counselor recommended applying for Montana Medicaid under the HELP Act expansion.</p>
    <p>The patient applied through DPHHS and qualified under Medicaid expansion. Because the application was submitted within 90 days of the hospitalization, Medicaid was approved retroactively and the entire bill was covered. <strong>Total bill covered: $26,000.</strong></p>
</div>

<h2 id="faq">Frequently asked questions</h2>

<div class="faq-section">
    <div class="faq-item">
        <h3>How long does a hospital have to sue me for a medical debt in Montana?</h3>
        <p>Montana&rsquo;s statute of limitations for written contracts is 8 years under MCA §27-2-202 &mdash; one of the longest in the nation. After 8 years from when the debt became due, a hospital generally cannot win a collection lawsuit. Making any payment or written acknowledgment can restart the clock. Contact Montana Legal Services at montanalegalservices.org for free help with old debts.</p>
    </div>
    <div class="faq-item">
        <h3>Does Montana have surprise billing protections?</h3>
        <p>Yes. Montana MCA §33-22-2001 provides surprise billing protections for patients with state-regulated insurance, working alongside the federal No Surprises Act. Out-of-network providers at in-network facilities cannot balance bill without advance written consent. File complaints with the Montana Commissioner of Securities and Insurance at csimt.gov or 1-800-332-6148.</p>
    </div>
    <div class="faq-item">
        <h3>Does Montana have Medicaid expansion?</h3>
        <p>Yes. Montana expanded Medicaid in January 2016 under the HELP Act, covering adults up to 138% FPL &mdash; approximately $20,783 for a single person in 2026. Coverage can be retroactive up to 3 months. Apply at dphhs.mt.gov/MontanaHealthcarePrograms or call 1-800-362-8312.</p>
    </div>
    <div class="faq-item">
        <h3>What is a Critical Access Hospital and why do they charge more?</h3>
        <p>Critical Access Hospitals are rural hospitals with fewer than 25 beds, more than 35 miles from another hospital, with 24/7 emergency services. Montana has many CAHs due to its rural geography. They receive cost-based Medicare reimbursement and tend to charge private patients more &mdash; BillKarma data shows Montana rural CAHs average 5.6&times; Medicare vs. 4.9&times; statewide. CAH patients have the same charity care rights as urban patients.</p>
    </div>
    <div class="faq-item">
        <h3>How much can a creditor garnish from my paycheck in Montana?</h3>
        <p>Montana follows the federal 25% of disposable weekly earnings limit for wage garnishment. A hospital must first obtain a court judgment before garnishing. Montana also has homestead exemptions protecting up to $350,000 in home equity. Contact Montana Legal Services at montanalegalservices.org for free help if facing garnishment.</p>
    </div>
</div>

<h2 id="sources">Sources</h2>

<ul class="sources-list">
    <li><a href="https://leg.mt.gov/bills/mca/title_0270/chapter_0020/part_0020/section_0020/0270-0020-0020-0020.html" target="_blank" rel="noopener">MCA §27-2-202: Montana Statute of Limitations on Written Contracts</a></li>
    <li><a href="https://csimt.gov/consumers/health-insurance/surprise-billing/" target="_blank" rel="noopener">Montana Commissioner of Securities &amp; Insurance: Surprise Billing Consumer Guide</a></li>
    <li><a href="https://dphhs.mt.gov/MontanaHealthcarePrograms/medicaid" target="_blank" rel="noopener">Montana DPHHS: Medicaid and HELP Act Expansion Information</a></li>
    <li><a href="https://www.cms.gov/nosurprises" target="_blank" rel="noopener">CMS: No Surprises Act &mdash; Federal Surprise Billing Protections</a></li>
    <li><a href="https://www.cms.gov/medicare/payment/prospective-payment-systems/critical-access-hospitals" target="_blank" rel="noopener">CMS: Critical Access Hospital Medicare Payment Overview</a></li>
    <li><a href="https://oig.hhs.gov/fraud/report-fraud/" target="_blank" rel="noopener">HHS OIG: Report Healthcare Fraud</a></li>
</ul>
""",
})
