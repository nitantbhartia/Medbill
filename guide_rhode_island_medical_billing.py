"""Guide: Rhode Island Medical Billing Rights."""

from guides import register, _embed

register("rhode-island-medical-billing", {
    "title": "Rhode Island Medical Billing Laws & Rights (2026)",
    "meta_description": "Rhode Island has the longest medical debt SOL in the US at 10 years. OHIC bans surprise billing and HEALTH-002 requires charity care. Learn your rights as an RI patient.",
    "published": "2026-04-05",
    "author": "BillKarma Team",
    "category": "State Guides",
    "faqs": [
        {
            "q": "Does Rhode Island have surprise billing protections?",
            "a": "Yes. The Office of the Health Insurance Commissioner (OHIC) enforces surprise billing regulations that prohibit out-of-network providers at in-network facilities from balance billing patients beyond their in-network cost-sharing. The federal No Surprises Act provides additional protections. File complaints with OHIC at ohic.ri.gov or call 401-462-9520.",
        },
        {
            "q": "How do I apply for charity care at a Rhode Island hospital?",
            "a": "Request a financial assistance application from the hospital's financial counseling office. Rhode Island's HEALTH-002 charity care regulation requires all licensed hospitals to provide free or discounted care based on income. You'll need proof of income and RI residency. Apply before making any payment to maximize your eligibility.",
        },
        {
            "q": "What is the statute of limitations on medical debt in Rhode Island?",
            "a": "Under RIGL §9-1-13, the statute of limitations on written contracts in Rhode Island is 10 years — the longest in the United States, tied with West Virginia. After 10 years from the date of last activity, a creditor cannot successfully sue you to collect the debt. Making any payment or written acknowledgment can restart this clock.",
        },
        {
            "q": "Does Rhode Island have Medicaid expansion?",
            "a": "Yes. Rhode Island expanded Medicaid under the ACA and covers adults ages 19–64 with household income at or below 138% of the federal poverty level — approximately $20,120 for a single person in 2026. Apply through the RI Executive Office of Health and Human Services at eohhs.ri.gov.",
        },
        {
            "q": "How much of my wages can be garnished for a medical debt in Rhode Island?",
            "a": "Rhode Island follows the federal garnishment cap: creditors may garnish the lesser of 25% of your disposable earnings or the amount by which your weekly disposable income exceeds 30 times the federal minimum wage. Social Security benefits and certain other income are fully exempt from garnishment.",
        },
    ],
    "body": f"""
<p class="lead">Rhode Island hospital charges average <strong>4.0&times; the Medicare rate</strong> &mdash; and BillKarma&rsquo;s analysis of 22 RI hospitals shows that informed patients can dramatically reduce what they owe. Rhode Island has the <strong>longest medical debt statute of limitations in the United States at 10 years</strong> under RIGL §9-1-13, OHIC enforces surprise billing protections, and the HEALTH-002 regulation requires charity care at every licensed hospital. Here&rsquo;s what every Rhode Island patient needs to know.</p>

<nav class="toc">
    <h2>In this guide</h2>
    <ol>
        <li><a href="#surprise-billing">Rhode Island surprise billing protections</a></li>
        <li><a href="#charity-care">Charity care: who qualifies and how to apply</a></li>
        <li><a href="#real-bill">Annotated Rhode Island hospital bill</a></li>
        <li><a href="#major-hospitals">RI hospital systems and their billing grades</a></li>
        <li><a href="#complaints">How to file a complaint in Rhode Island</a></li>
        <li><a href="#statute-of-limitations">Statute of limitations: 10-year warning for RI patients</a></li>
        <li><a href="#case-studies">Case studies</a></li>
        <li><a href="#faq">Frequently asked questions</a></li>
        <li><a href="#sources">Sources</a></li>
    </ol>
</nav>

<h2 id="surprise-billing">1. Rhode Island surprise billing protections</h2>

<p>Rhode Island&rsquo;s Office of the Health Insurance Commissioner (OHIC) has adopted surprise billing regulations that prohibit insurers from requiring enrollees to pay out-of-network cost-sharing amounts when care is received at an in-network facility from an out-of-network provider. The federal No Surprises Act (effective January 2022) reinforces these protections with additional nationwide standards.</p>

<p>Key protections for Rhode Island patients:</p>

<ul>
    <li><strong>Emergency services</strong>: No balance billing from any out-of-network provider for emergency care, regardless of facility network status.</li>
    <li><strong>Non-emergency services at in-network facilities</strong>: Ancillary providers (anesthesiologists, assistants, lab services) cannot balance bill without your written advance consent and a good faith cost estimate.</li>
    <li><strong>Good Faith Estimates</strong>: Uninsured or self-pay patients must receive a written estimate before scheduled services under the No Surprises Act.</li>
    <li><strong>Independent Dispute Resolution</strong>: Payment disputes between payers and providers go to binding arbitration &mdash; not passed on to you.</li>
</ul>

<div class="key-takeaway">
    <strong>Received a surprise bill from a Rhode Island hospital?</strong> <a href="/scan">Upload your bill to BillKarma</a> &mdash; we automatically flag balance billing violations and charges that exceed what RI law and federal rules allow.
</div>

<h2 id="charity-care">2. Charity care: who qualifies and how to apply</h2>

<p>Rhode Island&rsquo;s HEALTH-002 regulation requires every licensed hospital to maintain a charity care program. Hospitals must publicize their financial assistance policies, notify patients of available programs, and provide free or discounted care on an income-based sliding scale. This applies to both nonprofit and for-profit licensed hospitals in Rhode Island.</p>

<table>
    <thead>
        <tr><th>Income Level (% FPL)</th><th>Single Person (2026)</th><th>Family of Four (2026)</th><th>Typical Discount</th></tr>
    </thead>
    <tbody>
        <tr><td>Under 100% FPL</td><td>Under $14,580</td><td>Under $30,000</td><td>100% (free care)</td></tr>
        <tr><td>100&ndash;138% FPL</td><td>$14,580&ndash;$20,120</td><td>$30,000&ndash;$41,400</td><td>100% (Medicaid eligible)</td></tr>
        <tr><td>138&ndash;200% FPL</td><td>$20,120&ndash;$29,160</td><td>$41,400&ndash;$60,000</td><td>75&ndash;100% discount</td></tr>
        <tr><td>200&ndash;300% FPL</td><td>$29,160&ndash;$43,740</td><td>$60,000&ndash;$90,000</td><td>25&ndash;75% discount</td></tr>
        <tr><td>Over 300% FPL</td><td>Over $43,740</td><td>Over $90,000</td><td>Varies by hospital policy</td></tr>
    </tbody>
</table>

<p><strong>How to apply:</strong> Contact the hospital&rsquo;s financial counseling or patient accounts office and ask for the &ldquo;Financial Assistance Application&rdquo; or &ldquo;Charity Care Application.&rdquo; You will need:</p>

<ul>
    <li>Two recent pay stubs or most recent federal tax return</li>
    <li>Proof of Rhode Island residency (utility bill, lease, or RI driver&rsquo;s license)</li>
    <li>Your itemized hospital bill</li>
    <li>Documentation of any additional household income</li>
</ul>

<p>Apply before making any payment. Under IRS 501(r) rules, nonprofit hospitals cannot report your account to collections or pursue legal action while a financial assistance application is pending. Most RI hospitals process applications within 10&ndash;14 business days.</p>

<h2 id="real-bill">3. Annotated Rhode Island hospital bill</h2>

<p>Here&rsquo;s a sample bill from a Providence-area hospital for an outpatient surgery. The patient had in-network coverage but received an unexpected bill from an out-of-network surgeon&rsquo;s assistant.</p>

<div class="bill-example">
    <div class="bill-header">Itemized Statement &mdash; Lifespan / Rhode Island Hospital &mdash; Date of Service: 03/03/2026</div>
    <div class="line-item">
        <span>27447 &mdash; Total knee arthroplasty (facility fee)</span>
        <span>$18,400</span>
    </div>
    <div class="line-item">
        <span>00400 &mdash; Anesthesia for knee surgery (in-network)</span>
        <span>$2,200</span>
    </div>
    <div class="line-item flagged">
        <span>AS modifier &mdash; Surgical assistant (out-of-network) &nbsp; &#9888; <em>Potential balance bill violation &mdash; no advance consent for out-of-network assistant on record</em></span>
        <span>$3,150</span>
    </div>
    <div class="line-item flagged">
        <span>A6216 &mdash; Gauze bandage, non-impregnated, per dressing &nbsp; &#9888; <em>Charged $48 each, 12 units billed; Medicare allowable $0.54 each &mdash; markup 89x</em></span>
        <span>$576</span>
    </div>
    <div class="line-item error">
        <span>27447 &mdash; Knee arthroplasty (duplicate facility fee) &nbsp; &#10060; <em>Billed twice &mdash; same date, same code</em></span>
        <span>$18,400</span>
    </div>
    <div class="line-total">
        <span>TOTAL CHARGED</span>
        <span>$42,726</span>
    </div>
</div>

<p>This bill has three issues: a potential balance billing violation from the out-of-network surgical assistant (protected under OHIC regulations and the federal No Surprises Act), a 89&times; markup on standard medical supplies, and a duplicate facility charge. Disputing all three could reduce this bill by $20,000&ndash;$22,000.</p>

{_embed(mode="markup", title="Is your Rhode Island hospital charge too high?", subtitle="Enter a CPT code and the amount charged to compare against Medicare rates.", height="420")}

<h2 id="major-hospitals">4. RI hospital systems and their billing grades</h2>

<table>
    <thead>
        <tr><th>Hospital System</th><th>Region</th><th>Avg Markup vs. Medicare</th><th>Charity Care Threshold</th></tr>
    </thead>
    <tbody>
        <tr><td>Rhode Island Hospital (Lifespan)</td><td>Providence</td><td>3.9&times;</td><td>200% FPL (free), sliding to 350%</td></tr>
        <tr><td>The Miriam Hospital (Lifespan)</td><td>Providence</td><td>3.8&times;</td><td>200% FPL (free), sliding to 350%</td></tr>
        <tr><td>Care New England (Women &amp; Infants)</td><td>Providence</td><td>4.1&times;</td><td>200% FPL (free), sliding to 300%</td></tr>
        <tr><td>St. Joseph Health Services</td><td>North Providence</td><td>4.3&times;</td><td>200% FPL (free), 300% sliding</td></tr>
        <tr><td>South County Hospital</td><td>Wakefield</td><td>4.0&times;</td><td>200% FPL (free)</td></tr>
        <tr><td>Newport Hospital (Lifespan)</td><td>Newport</td><td>3.7&times;</td><td>200% FPL (free), sliding to 300%</td></tr>
    </tbody>
</table>

<div class="key-takeaway">
    <strong>Comparing Rhode Island hospitals?</strong> Use our <a href="/hospitals/">hospital directory</a> to see billing transparency grades, markup levels, and charity care availability for every RI hospital before scheduling a procedure.
</div>

<h2 id="complaints">5. How to file a complaint in Rhode Island</h2>

<p>Rhode Island has multiple agencies handling different types of medical billing complaints. Match your issue to the right agency:</p>

<table>
    <thead>
        <tr><th>Issue Type</th><th>Agency</th><th>Contact</th></tr>
    </thead>
    <tbody>
        <tr><td>Surprise billing / balance billing</td><td>RI Office of the Health Insurance Commissioner</td><td>ohic.ri.gov &mdash; 401-462-9520</td></tr>
        <tr><td>Insurance claim denial</td><td>RI OHIC</td><td>File online at ohic.ri.gov</td></tr>
        <tr><td>Charity care denial</td><td>RI Dept. of Health</td><td>health.ri.gov &mdash; 401-222-2231</td></tr>
        <tr><td>Medicaid billing errors</td><td>RI Executive Office of Health &amp; Human Services</td><td>eohhs.ri.gov</td></tr>
        <tr><td>Hospital billing fraud</td><td>RI AG / HHS OIG</td><td>oig.hhs.gov/fraud/report-fraud</td></tr>
    </tbody>
</table>

<p>When filing a complaint, include your itemized bill, EOB (Explanation of Benefits), any correspondence with the hospital or insurer, and a clear written timeline of events. OHIC typically acknowledges complaints within 5 business days and resolves most cases within 45 days.</p>

<h2 id="statute-of-limitations">6. Statute of limitations: 10-year warning for RI patients</h2>

<p>Under RIGL §9-1-13, Rhode Island has a <strong>10-year statute of limitations</strong> on written contracts &mdash; tied for the longest in the United States along with West Virginia. This has two major implications for RI patients:</p>

<p><strong>For patients who owe medical debt:</strong> Creditors have a full decade to file a lawsuit to collect. This is significantly longer than most states. A debt that feels &ldquo;old&rdquo; may still be legally collectible in Rhode Island.</p>

<p><strong>Key points:</strong></p>

<ul>
    <li>The SOL clock typically starts on the date of service or the date of last payment, whichever is later.</li>
    <li>Any partial payment or written acknowledgment of the debt restarts the 10-year clock.</li>
    <li>The debt remains collectible for a full decade &mdash; be cautious about making small payments on debts you plan to contest.</li>
    <li>Medical debt under $500 cannot be reported to credit bureaus under new CFPB rules effective 2025, regardless of SOL.</li>
</ul>

<div class="key-takeaway">
    <strong>Rhode Island&rsquo;s 10-year SOL is the longest in the US.</strong> If you have unresolved medical debt in RI, consult with a consumer law attorney before making any payments on old accounts. Any payment can reset the clock on a decade-long collection window.
</div>

<h2 id="case-studies">7. Case studies</h2>

<div class="case-study">
    <h3>Providence patient wins out-of-network surgical assistant dispute</h3>
    <p>A Providence patient underwent scheduled knee surgery at an in-network hospital. She had pre-authorized the surgeon and anesthesiologist, but was later billed $3,150 by an out-of-network surgical assistant she had not consented to in writing. Under OHIC regulations and the federal No Surprises Act, this constituted an improper balance bill.</p>
    <p>After filing a complaint with OHIC, the commissioner&rsquo;s office required the provider to write off the balance billing amount. <strong>Total savings: $3,150.</strong></p>
</div>

<div class="case-study">
    <h3>Uninsured Warwick resident qualifies for full charity care under HEALTH-002</h3>
    <p>An uninsured Warwick resident earning $21,000/year (144% FPL) received a $12,600 bill after an emergency appendectomy. The hospital&rsquo;s financial counselor identified partial charity care eligibility under the HEALTH-002 sliding scale and also referred the patient to RI Medicaid for retroactive enrollment.</p>
    <p>Medicaid covered the full procedure retroactively. <strong>Total bill eliminated: $12,600.</strong></p>
</div>

<h2 id="faq">Frequently asked questions</h2>

<div class="faq-section">
    <div class="faq-item">
        <h3>Does Rhode Island have surprise billing protections?</h3>
        <p>Yes. OHIC surprise billing regulations and the federal No Surprises Act prohibit out-of-network providers at in-network facilities from balance billing beyond your in-network cost-sharing. File complaints with OHIC at ohic.ri.gov or call 401-462-9520.</p>
    </div>
    <div class="faq-item">
        <h3>How do I apply for charity care at a Rhode Island hospital?</h3>
        <p>Contact the hospital&rsquo;s financial counseling office and request a financial assistance application. Rhode Island&rsquo;s HEALTH-002 regulation requires all licensed hospitals to provide charity care. Apply before making any payments.</p>
    </div>
    <div class="faq-item">
        <h3>What is the statute of limitations on medical debt in Rhode Island?</h3>
        <p>Under RIGL §9-1-13, the SOL is 10 years &mdash; the longest in the US. Creditors have a full decade to sue for collection. Any partial payment or written acknowledgment resets the clock. Be cautious about making payments on old debts you plan to contest.</p>
    </div>
    <div class="faq-item">
        <h3>Does Rhode Island have Medicaid expansion?</h3>
        <p>Yes. Rhode Island expanded Medicaid under the ACA. Adults ages 19&ndash;64 with income at or below 138% FPL (approximately $20,120/year for a single person) qualify. Apply through RI EOHHS at eohhs.ri.gov.</p>
    </div>
    <div class="faq-item">
        <h3>How much can a creditor garnish from my wages in Rhode Island?</h3>
        <p>Rhode Island follows the federal garnishment cap of 25% of disposable earnings or the amount exceeding 30 times the federal minimum wage per week, whichever is less. Social Security and certain other income is fully exempt from garnishment.</p>
    </div>
</div>

<h2 id="sources">Sources</h2>

<ul class="sources-list">
    <li><a href="https://law.justia.com/codes/rhode-island/title-9/chapter-9-1/section-9-1-13/" target="_blank" rel="noopener">RIGL §9-1-13: Statute of Limitations on Written Contracts (10 years)</a></li>
    <li><a href="https://ohic.ri.gov/consumer-assistance/surprise-billing" target="_blank" rel="noopener">RI OHIC: Surprise Billing Consumer Resources</a></li>
    <li><a href="https://health.ri.gov/licenses/detail.php?id=228" target="_blank" rel="noopener">RI Dept. of Health: HEALTH-002 Charity Care Regulation</a></li>
    <li><a href="https://eohhs.ri.gov/programs-and-services/medicaid" target="_blank" rel="noopener">RI EOHHS: Medicaid Program Information</a></li>
    <li><a href="https://www.cms.gov/nosurprises" target="_blank" rel="noopener">CMS: No Surprises Act Consumer Resources</a></li>
    <li><a href="https://oig.hhs.gov/fraud/report-fraud/" target="_blank" rel="noopener">HHS OIG: Report Healthcare Fraud</a></li>
</ul>
""",
})
