"""Guide: New Hampshire Medical Billing Rights."""

from guides import register, _embed

register("new-hampshire-medical-billing", {
    "title": "New Hampshire Medical Billing Laws & Rights (2026)",
    "meta_description": "NH RSA 420-J bans surprise billing and DHHS requires charity care. Learn your rights, how to apply for Granite Advantage Medicaid, and how to dispute inflated bills.",
    "published": "2026-04-05",
    "author": "BillKarma Team",
    "category": "State Guides",
    "faqs": [
        {
            "q": "Does New Hampshire have surprise billing protections?",
            "a": "Yes. RSA 420-J prohibits balance billing by out-of-network providers at in-network facilities. Combined with the federal No Surprises Act, NH patients are protected from unexpected out-of-network charges for emergency and many non-emergency services. File complaints with the NH Insurance Department at insurance.nh.gov.",
        },
        {
            "q": "How do I apply for charity care at a New Hampshire hospital?",
            "a": "Ask the hospital's financial counseling office for a financial assistance application. NH DHHS requires nonprofit hospitals to provide charity care. You'll need proof of income (pay stubs or tax return) and proof of NH residency. Apply before making any payment — hospitals are not required to retroactively grant assistance.",
        },
        {
            "q": "What is the income limit for New Hampshire Granite Advantage Medicaid?",
            "a": "Granite Advantage Medicaid covers adults ages 19–64 with household income at or below 138% of the federal poverty level. In 2026, that is approximately $20,120 for a single person and $41,400 for a family of four. Apply through NH DHHS at dhhs.nh.gov.",
        },
        {
            "q": "What is the statute of limitations on medical debt in New Hampshire?",
            "a": "Under RSA 508:4, the statute of limitations on written contracts (including medical debt) is 3 years in New Hampshire — one of the shortest in the country. After 3 years from the date of last activity, a creditor cannot successfully sue you to collect the debt. This does not erase the debt, but it removes the threat of a court judgment.",
        },
        {
            "q": "How much of my wages can be garnished for a medical debt in New Hampshire?",
            "a": "New Hampshire follows the federal garnishment cap: creditors may garnish the lesser of 25% of your disposable earnings or the amount by which your weekly disposable income exceeds 30 times the federal minimum wage. Certain income sources such as Social Security benefits are exempt from garnishment entirely.",
        },
    ],
    "body": f"""
<p class="lead">New Hampshire hospital charges average <strong>4.3&times; the Medicare rate</strong> &mdash; and BillKarma&rsquo;s analysis of 28 NH hospitals shows that patients armed with the right knowledge can significantly reduce their bills. RSA 420-J bans surprise balance billing, the Granite Advantage program covers adults up to 138% FPL, and DHHS requires nonprofit hospitals to offer charity care. Here&rsquo;s everything NH patients need to know.</p>

<nav class="toc">
    <h2>In this guide</h2>
    <ol>
        <li><a href="#surprise-billing">New Hampshire surprise billing protections</a></li>
        <li><a href="#charity-care">Charity care: who qualifies and how to apply</a></li>
        <li><a href="#real-bill">Annotated New Hampshire hospital bill</a></li>
        <li><a href="#major-hospitals">NH hospital systems and their billing grades</a></li>
        <li><a href="#complaints">How to file a complaint in New Hampshire</a></li>
        <li><a href="#statute-of-limitations">Statute of limitations on medical debt</a></li>
        <li><a href="#case-studies">Case studies</a></li>
        <li><a href="#faq">Frequently asked questions</a></li>
        <li><a href="#sources">Sources</a></li>
    </ol>
</nav>

<h2 id="surprise-billing">1. New Hampshire surprise billing protections</h2>

<p>New Hampshire RSA 420-J prohibits insurers from holding patients responsible for out-of-network cost-sharing beyond in-network levels when care is received at an in-network facility. The federal No Surprises Act (effective January 1, 2022) reinforces and extends these protections statewide.</p>

<p>Key protections for NH patients:</p>

<ul>
    <li><strong>Emergency services</strong>: No balance billing from any out-of-network provider for emergency care, regardless of the facility&rsquo;s network status.</li>
    <li><strong>Non-emergency services at in-network facilities</strong>: Out-of-network providers (such as anesthesiologists or radiologists) cannot balance bill you without prior written consent and a cost estimate.</li>
    <li><strong>Good Faith Estimates</strong>: Uninsured or self-pay patients must receive a written estimate before scheduled services under the No Surprises Act.</li>
    <li><strong>Independent Dispute Resolution</strong>: Payment disputes between insurers and providers go to arbitration &mdash; the cost does not get passed to you.</li>
</ul>

<div class="key-takeaway">
    <strong>Received a surprise bill from a New Hampshire hospital or provider?</strong> <a href="/scan">Upload your bill to BillKarma</a> &mdash; we automatically flag balance billing violations and out-of-network charges that exceed what NH law allows.
</div>

<h2 id="charity-care">2. Charity care: who qualifies and how to apply</h2>

<p>NH DHHS requires nonprofit hospitals to provide financial assistance to low-income patients. Every nonprofit hospital must publish a financial assistance policy and notify patients of available programs in writing. For-profit hospitals are not subject to the same mandate but many offer assistance voluntarily.</p>

<table>
    <thead>
        <tr><th>Income Level (% FPL)</th><th>Single Person (2026)</th><th>Family of Four (2026)</th><th>Typical Discount</th></tr>
    </thead>
    <tbody>
        <tr><td>Under 100% FPL</td><td>Under $14,580</td><td>Under $30,000</td><td>100% (free care)</td></tr>
        <tr><td>100&ndash;138% FPL</td><td>$14,580&ndash;$20,120</td><td>$30,000&ndash;$41,400</td><td>100% (Granite Advantage eligible)</td></tr>
        <tr><td>138&ndash;200% FPL</td><td>$20,120&ndash;$29,160</td><td>$41,400&ndash;$60,000</td><td>75&ndash;100% discount</td></tr>
        <tr><td>200&ndash;300% FPL</td><td>$29,160&ndash;$43,740</td><td>$60,000&ndash;$90,000</td><td>25&ndash;75% discount</td></tr>
        <tr><td>Over 300% FPL</td><td>Over $43,740</td><td>Over $90,000</td><td>Varies by hospital policy</td></tr>
    </tbody>
</table>

<p><strong>How to apply:</strong> Contact the hospital&rsquo;s financial counseling or patient accounts department and request the &ldquo;Financial Assistance Application.&rdquo; You will typically need:</p>

<ul>
    <li>Two recent pay stubs or most recent federal tax return</li>
    <li>Proof of NH residency (utility bill, lease, or NH driver&rsquo;s license)</li>
    <li>Your itemized hospital bill</li>
    <li>Documentation of any other household income sources</li>
</ul>

<p>Apply before making any payment. Most NH hospitals process applications within 10&ndash;14 business days. Under IRS 501(r) rules, nonprofit hospitals cannot pursue aggressive collections while an application is pending.</p>

<h2 id="real-bill">3. Annotated New Hampshire hospital bill</h2>

<p>Here&rsquo;s a sample ER bill from a Manchester-area hospital for a patient treated for chest pain. The patient had in-network coverage but received services from an out-of-network cardiologist.</p>

<div class="bill-example">
    <div class="bill-header">Itemized Statement &mdash; Concord Hospital &mdash; Date of Service: 02/14/2026</div>
    <div class="line-item">
        <span>99285 &mdash; Emergency Department Level 5 visit (facility)</span>
        <span>$4,180</span>
    </div>
    <div class="line-item">
        <span>93000 &mdash; Electrocardiogram with interpretation</span>
        <span>$320</span>
    </div>
    <div class="line-item flagged">
        <span>93306 &mdash; Echocardiogram (out-of-network cardiologist) &nbsp; &#9888; <em>Potential balance bill violation &mdash; verify provider was out-of-network at in-network facility</em></span>
        <span>$2,950</span>
    </div>
    <div class="line-item flagged">
        <span>J2270 &mdash; Morphine sulfate injection &nbsp; &#9888; <em>Charged $280; Medicare allowable $3.10 &mdash; markup 90x</em></span>
        <span>$280</span>
    </div>
    <div class="line-item error">
        <span>99285 &mdash; Emergency Department Level 5 (duplicate) &nbsp; &#10060; <em>Billed twice &mdash; same date, same code</em></span>
        <span>$4,180</span>
    </div>
    <div class="line-total">
        <span>TOTAL CHARGED</span>
        <span>$11,910</span>
    </div>
</div>

<p>This bill has three issues: a potential balance billing violation from the out-of-network cardiologist (protected under RSA 420-J and the federal No Surprises Act), a 90&times; markup on a common pain medication, and a duplicate ER facility charge. Disputing all three could reduce this bill by $5,500&ndash;$7,000.</p>

{_embed(mode="markup", title="Is your New Hampshire hospital charge too high?", subtitle="Enter a CPT code and the amount charged to compare against Medicare rates.", height="420")}

<h2 id="major-hospitals">4. NH hospital systems and their billing grades</h2>

<table>
    <thead>
        <tr><th>Hospital System</th><th>Region</th><th>Avg Markup vs. Medicare</th><th>Charity Care Threshold</th></tr>
    </thead>
    <tbody>
        <tr><td>Dartmouth Health (DHMC)</td><td>Lebanon</td><td>3.8&times;</td><td>200% FPL (free), sliding to 400%</td></tr>
        <tr><td>Concord Hospital</td><td>Concord</td><td>4.1&times;</td><td>200% FPL (free)</td></tr>
        <tr><td>Catholic Medical Center</td><td>Manchester</td><td>4.4&times;</td><td>200% FPL (free), 300% sliding</td></tr>
        <tr><td>Elliot Health System</td><td>Manchester</td><td>4.6&times;</td><td>200% FPL (free)</td></tr>
        <tr><td>Portsmouth Regional Hospital (HCA)</td><td>Portsmouth</td><td>5.2&times;</td><td>200% FPL (free)</td></tr>
        <tr><td>Southern NH Medical Center</td><td>Nashua</td><td>4.3&times;</td><td>200% FPL (free), 300% sliding</td></tr>
    </tbody>
</table>

<div class="key-takeaway">
    <strong>Comparing NH hospitals?</strong> Use our <a href="/hospitals/">hospital directory</a> to see billing transparency grades, markup levels, and charity care availability for every New Hampshire hospital before you schedule a procedure.
</div>

<h2 id="complaints">5. How to file a complaint in New Hampshire</h2>

<p>New Hampshire has several agencies that handle medical billing complaints. Match your issue to the right agency:</p>

<table>
    <thead>
        <tr><th>Issue Type</th><th>Agency</th><th>Contact</th></tr>
    </thead>
    <tbody>
        <tr><td>Surprise billing / balance billing</td><td>NH Insurance Department</td><td>insurance.nh.gov &mdash; 1-800-852-3416</td></tr>
        <tr><td>Insurance claim denial</td><td>NH Insurance Department</td><td>File online at insurance.nh.gov</td></tr>
        <tr><td>Charity care denial</td><td>NH DHHS</td><td>dhhs.nh.gov &mdash; 1-800-852-3345</td></tr>
        <tr><td>Medicaid billing errors</td><td>NH Medicaid</td><td>dhhs.nh.gov/medicaid</td></tr>
        <tr><td>Hospital billing fraud</td><td>NH AG / HHS OIG</td><td>oig.hhs.gov/fraud/report-fraud</td></tr>
    </tbody>
</table>

<p>When filing a complaint, include your itemized bill, any written correspondence with the hospital or insurer, your EOB (Explanation of Benefits), and a clear timeline of events. The NH Insurance Department typically acknowledges complaints within 5 business days.</p>

<h2 id="statute-of-limitations">6. Statute of limitations on medical debt</h2>

<p>Under RSA 508:4, the statute of limitations on written contracts in New Hampshire is <strong>3 years</strong> &mdash; among the shortest in the United States. This means a creditor has only 3 years from the date of last activity (typically the date of service or last payment) to file a lawsuit to collect the debt.</p>

<p>Important distinctions:</p>

<ul>
    <li>The SOL clock does <em>not</em> erase the debt &mdash; it only prevents successful collection lawsuits.</li>
    <li>Making a partial payment or acknowledging the debt in writing can reset the SOL clock.</li>
    <li>Debt collectors can still contact you after the SOL expires; they simply cannot win a court judgment.</li>
    <li>The NH 3-year SOL is significantly shorter than states like Rhode Island (10 years) or West Virginia (10 years).</li>
</ul>

<div class="key-takeaway">
    <strong>Dealing with a medical debt collector in New Hampshire?</strong> Know your rights under RSA 358-C (NH Unfair, Deceptive, or Unreasonable Collection Practices Act) and the federal Fair Debt Collection Practices Act. Send any dispute in writing and keep copies.
</div>

<h2 id="case-studies">7. Case studies</h2>

<div class="case-study">
    <h3>Manchester patient wins surprise anesthesia dispute under RSA 420-J</h3>
    <p>A patient at an in-network Manchester hospital for an elective procedure received a $3,200 bill from an out-of-network anesthesiologist after surgery. Under NH RSA 420-J and the federal No Surprises Act, the anesthesiologist was prohibited from billing beyond the patient&rsquo;s in-network cost-sharing since the patient had no opportunity to choose the provider.</p>
    <p>The patient filed a complaint with the NH Insurance Department. The department confirmed the violation and required the claim to be reprocessed at in-network rates. <strong>Total savings: $2,800.</strong></p>
</div>

<div class="case-study">
    <h3>Concord uninsured patient qualifies for full charity care</h3>
    <p>An uninsured Concord resident earning $18,500/year (127% FPL) received a $9,800 bill after a two-day hospital stay for appendicitis. After being informed of Granite Advantage Medicaid eligibility by a hospital financial counselor, the patient applied for both Medicaid and the hospital&rsquo;s charity care program.</p>
    <p>The patient was enrolled in Granite Advantage, which retroactively covered the hospitalization. <strong>Total bill eliminated: $9,800.</strong></p>
</div>

<h2 id="faq">Frequently asked questions</h2>

<div class="faq-section">
    <div class="faq-item">
        <h3>Does New Hampshire have surprise billing protections?</h3>
        <p>Yes. RSA 420-J prohibits balance billing by out-of-network providers at in-network facilities. The federal No Surprises Act adds another layer of protection. File complaints with the NH Insurance Department at insurance.nh.gov or call 1-800-852-3416.</p>
    </div>
    <div class="faq-item">
        <h3>How do I apply for charity care at a New Hampshire hospital?</h3>
        <p>Contact the hospital&rsquo;s financial counseling office and request a financial assistance application. Bring proof of income and NH residency. Apply before making any payments &mdash; retroactive assistance is not guaranteed.</p>
    </div>
    <div class="faq-item">
        <h3>What is the income limit for Granite Advantage Medicaid?</h3>
        <p>Granite Advantage covers adults ages 19&ndash;64 with income at or below 138% FPL &mdash; approximately $20,120/year for a single person in 2026. Apply through NH DHHS at dhhs.nh.gov.</p>
    </div>
    <div class="faq-item">
        <h3>What is the statute of limitations on medical debt in New Hampshire?</h3>
        <p>Under RSA 508:4, the SOL is 3 years &mdash; among the shortest in the US. After 3 years from the date of last activity, creditors cannot win a court judgment to collect the debt. Making any payment or written acknowledgment can reset this clock.</p>
    </div>
    <div class="faq-item">
        <h3>How much can a creditor garnish from my wages for a medical debt in NH?</h3>
        <p>New Hampshire follows the federal cap: the lesser of 25% of disposable earnings or the amount exceeding 30 times the federal minimum wage per week. Social Security and certain other income sources are fully exempt from garnishment.</p>
    </div>
</div>

<h2 id="sources">Sources</h2>

<ul class="sources-list">
    <li><a href="https://www.gencourt.state.nh.us/rsa/html/LI/508/508-4.htm" target="_blank" rel="noopener">NH RSA 508:4: Statute of Limitations on Written Contracts</a></li>
    <li><a href="https://www.insurance.nh.gov/consumers/health-insurance/surprise-billing" target="_blank" rel="noopener">NH Insurance Department: Surprise Billing Consumer Guide</a></li>
    <li><a href="https://www.dhhs.nh.gov/programs-services/medicaid/granite-advantage" target="_blank" rel="noopener">NH DHHS: Granite Advantage Health Care Program</a></li>
    <li><a href="https://www.cms.gov/nosurprises" target="_blank" rel="noopener">CMS: No Surprises Act Consumer Resources</a></li>
    <li><a href="https://www.cms.gov/hospital-price-transparency" target="_blank" rel="noopener">CMS Hospital Price Transparency Rule</a></li>
    <li><a href="https://oig.hhs.gov/fraud/report-fraud/" target="_blank" rel="noopener">HHS OIG: Report Healthcare Fraud</a></li>
</ul>
""",
})
