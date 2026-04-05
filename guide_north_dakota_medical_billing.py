"""Guide: North Dakota Medical Billing Rights."""

from guides import register, _embed

register("north-dakota-medical-billing", {
    "title": "North Dakota Medical Billing Laws & Rights (2026)",
    "meta_description": "ND NDCC §26.1-36-09.16 bans surprise billing and Medicaid covers adults up to 138% FPL. Learn your rights and how to dispute inflated hospital bills in North Dakota.",
    "published": "2026-04-05",
    "author": "BillKarma Team",
    "category": "State Guides",
    "faqs": [
        {
            "q": "Does North Dakota have surprise billing protections?",
            "a": "Yes. NDCC §26.1-36-09.16 prohibits balance billing by out-of-network providers in certain situations, and the federal No Surprises Act (effective January 2022) provides comprehensive protections statewide. Out-of-network providers at in-network facilities generally cannot bill you beyond your in-network cost-sharing. File complaints with the ND Insurance Department at insurance.nd.gov.",
        },
        {
            "q": "How do I apply for charity care at a North Dakota hospital?",
            "a": "Request a financial assistance application from the hospital's financial counseling office. ND nonprofit hospitals are required to provide charity care under IRS 501(r) rules. Bring proof of income (pay stubs or tax return) and proof of ND residency. Apply before making any payment to preserve your eligibility for retroactive consideration.",
        },
        {
            "q": "Does North Dakota have Medicaid expansion?",
            "a": "Yes. North Dakota expanded Medicaid in 2014 under the ACA. Medicaid covers adults ages 19–64 with household income at or below 138% of the federal poverty level — approximately $20,120 for a single person in 2026. Apply through the ND Department of Human Services at dhs.nd.gov.",
        },
        {
            "q": "What is the statute of limitations on medical debt in North Dakota?",
            "a": "Under NDCC §28-01-16, the statute of limitations on written contracts in North Dakota is 6 years. After 6 years from the date of last activity, a creditor cannot successfully sue you in court to collect the debt. Making a payment or acknowledging the debt in writing can restart this clock.",
        },
        {
            "q": "How much of my wages can be garnished for a medical debt in North Dakota?",
            "a": "North Dakota follows the federal garnishment limit: creditors may garnish the lesser of 25% of your disposable earnings or the amount by which your weekly disposable income exceeds 30 times the federal minimum wage. Certain income such as Social Security benefits is fully exempt from garnishment.",
        },
    ],
    "body": f"""
<p class="lead">North Dakota hospital charges average <strong>4.4&times; the Medicare rate</strong> &mdash; and BillKarma&rsquo;s analysis of 41 ND hospitals shows significant variation across the state. NDCC §26.1-36-09.16 protects patients from surprise balance bills, Medicaid covers adults up to 138% FPL since the 2014 expansion, and nonprofit hospitals must offer charity care. Here&rsquo;s what every North Dakota patient needs to know.</p>

<nav class="toc">
    <h2>In this guide</h2>
    <ol>
        <li><a href="#surprise-billing">North Dakota surprise billing protections</a></li>
        <li><a href="#charity-care">Charity care: who qualifies and how to apply</a></li>
        <li><a href="#real-bill">Annotated North Dakota hospital bill</a></li>
        <li><a href="#major-hospitals">ND hospital systems and their billing grades</a></li>
        <li><a href="#complaints">How to file a complaint in North Dakota</a></li>
        <li><a href="#statute-of-limitations">Statute of limitations on medical debt</a></li>
        <li><a href="#case-studies">Case studies</a></li>
        <li><a href="#faq">Frequently asked questions</a></li>
        <li><a href="#sources">Sources</a></li>
    </ol>
</nav>

<h2 id="surprise-billing">1. North Dakota surprise billing protections</h2>

<p>North Dakota NDCC §26.1-36-09.16 prohibits insurers from requiring enrollees to pay more than their in-network cost-sharing when out-of-network providers deliver care at in-network facilities. The federal No Surprises Act reinforces these protections and extends them to additional situations beginning January 1, 2022.</p>

<p>Key protections under North Dakota law and federal rules:</p>

<ul>
    <li><strong>Emergency services</strong>: No balance billing from any out-of-network provider for emergency care, regardless of facility network status.</li>
    <li><strong>Non-emergency services at in-network facilities</strong>: Ancillary providers (anesthesiologists, radiologists, lab services) cannot balance bill without prior written consent and advance cost disclosure.</li>
    <li><strong>Good Faith Estimates</strong>: Uninsured or self-pay patients must receive a written cost estimate before scheduled services.</li>
    <li><strong>Independent Dispute Resolution</strong>: Payment disputes between insurers and providers go to binding arbitration &mdash; not passed on to the patient.</li>
</ul>

<div class="key-takeaway">
    <strong>Received a surprise bill from a North Dakota hospital?</strong> <a href="/scan">Upload your bill to BillKarma</a> &mdash; we automatically flag balance billing violations and charges that exceed what ND law allows.
</div>

<h2 id="charity-care">2. Charity care: who qualifies and how to apply</h2>

<p>Every nonprofit hospital in North Dakota must provide financial assistance under IRS 501(r) rules. Hospitals must notify patients in writing about available assistance programs and maintain a published financial assistance policy. Many ND hospitals use a standardized income-based sliding scale.</p>

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

<p><strong>How to apply:</strong> Contact the hospital&rsquo;s financial counseling or patient accounts office and request the &ldquo;Financial Assistance Application.&rdquo; You will typically need:</p>

<ul>
    <li>Two recent pay stubs or most recent federal tax return</li>
    <li>Proof of North Dakota residency (utility bill, lease, or ND driver&rsquo;s license)</li>
    <li>Your itemized hospital bill</li>
    <li>Documentation of any government benefits or other income sources</li>
</ul>

<p>Apply before paying anything. Under IRS 501(r) rules, nonprofit hospitals cannot pursue aggressive collections (lawsuits, garnishment, credit reporting) while an application is under review. Most ND hospitals process applications within 10&ndash;14 business days.</p>

<h2 id="real-bill">3. Annotated North Dakota hospital bill</h2>

<p>Here&rsquo;s a sample ER bill from a Fargo-area hospital for a patient treated for a broken wrist. The patient had in-network coverage but the orthopedic specialist was out-of-network.</p>

<div class="bill-example">
    <div class="bill-header">Itemized Statement &mdash; Sanford Medical Center Fargo &mdash; Date of Service: 01/22/2026</div>
    <div class="line-item">
        <span>99283 &mdash; Emergency Department Level 3 visit (facility)</span>
        <span>$2,640</span>
    </div>
    <div class="line-item">
        <span>73100 &mdash; X-ray wrist, two views</span>
        <span>$480</span>
    </div>
    <div class="line-item flagged">
        <span>29075 &mdash; Cast application, forearm (out-of-network orthopedist) &nbsp; &#9888; <em>Potential balance bill violation &mdash; verify provider was out-of-network at in-network facility</em></span>
        <span>$1,840</span>
    </div>
    <div class="line-item flagged">
        <span>J3010 &mdash; Fentanyl citrate injection &nbsp; &#9888; <em>Charged $310; Medicare allowable $2.50 &mdash; markup 124x</em></span>
        <span>$310</span>
    </div>
    <div class="line-item error">
        <span>73100 &mdash; X-ray wrist (duplicate) &nbsp; &#10060; <em>Billed twice &mdash; same date, same code</em></span>
        <span>$480</span>
    </div>
    <div class="line-total">
        <span>TOTAL CHARGED</span>
        <span>$5,750</span>
    </div>
</div>

<p>This bill has three problems: a potential balance billing violation from the out-of-network orthopedist, a 124&times; markup on a common pain medication, and a duplicate imaging charge. Disputing all three could reduce this bill by $2,000&ndash;$2,800.</p>

{_embed(mode="markup", title="Is your North Dakota hospital charge too high?", subtitle="Enter a CPT code and the amount charged to compare against Medicare rates.", height="420")}

<h2 id="major-hospitals">4. ND hospital systems and their billing grades</h2>

<table>
    <thead>
        <tr><th>Hospital System</th><th>Region</th><th>Avg Markup vs. Medicare</th><th>Charity Care Threshold</th></tr>
    </thead>
    <tbody>
        <tr><td>Sanford Health (Fargo)</td><td>Fargo</td><td>4.2&times;</td><td>200% FPL (free), sliding to 300%</td></tr>
        <tr><td>Essentia Health (Fargo)</td><td>Fargo</td><td>4.0&times;</td><td>200% FPL (free), sliding to 350%</td></tr>
        <tr><td>CHI St. Alexius (Bismarck)</td><td>Bismarck</td><td>4.6&times;</td><td>200% FPL (free), 300% sliding</td></tr>
        <tr><td>Sanford Health (Bismarck)</td><td>Bismarck</td><td>4.4&times;</td><td>200% FPL (free)</td></tr>
        <tr><td>Altru Health System</td><td>Grand Forks</td><td>3.9&times;</td><td>200% FPL (free), sliding to 300%</td></tr>
        <tr><td>Trinity Health (Minot)</td><td>Minot</td><td>4.8&times;</td><td>200% FPL (free)</td></tr>
    </tbody>
</table>

<div class="key-takeaway">
    <strong>Comparing North Dakota hospitals?</strong> Use our <a href="/hospitals/">hospital directory</a> to see billing transparency grades, markup levels, and charity care availability for every ND hospital before scheduling a procedure.
</div>

<h2 id="complaints">5. How to file a complaint in North Dakota</h2>

<p>North Dakota has multiple agencies handling different types of billing complaints. Match your issue to the right agency:</p>

<table>
    <thead>
        <tr><th>Issue Type</th><th>Agency</th><th>Contact</th></tr>
    </thead>
    <tbody>
        <tr><td>Surprise billing / balance billing</td><td>ND Insurance Department</td><td>insurance.nd.gov &mdash; 1-800-247-0560</td></tr>
        <tr><td>Insurance claim denial</td><td>ND Insurance Department</td><td>File online at insurance.nd.gov</td></tr>
        <tr><td>Charity care denial</td><td>ND Department of Human Services</td><td>dhs.nd.gov &mdash; 1-800-755-2604</td></tr>
        <tr><td>Medicaid billing errors</td><td>ND Medicaid</td><td>dhs.nd.gov/medicaid</td></tr>
        <tr><td>Hospital billing fraud</td><td>ND AG / HHS OIG</td><td>oig.hhs.gov/fraud/report-fraud</td></tr>
    </tbody>
</table>

<p>When filing a complaint, include your itemized bill, any written correspondence with the hospital or insurer, your EOB (Explanation of Benefits), and a clear timeline of what occurred. The ND Insurance Department acknowledges most complaints within 5&ndash;7 business days.</p>

<h2 id="statute-of-limitations">6. Statute of limitations on medical debt</h2>

<p>Under NDCC §28-01-16, the statute of limitations on written contracts in North Dakota is <strong>6 years</strong>. After 6 years from the date of last activity, a creditor cannot win a court judgment to compel payment of a medical debt.</p>

<p>Key points to understand:</p>

<ul>
    <li>The SOL clock generally starts on the date of service or the date of last payment, whichever is later.</li>
    <li>Making any partial payment or acknowledging the debt in writing restarts the 6-year clock.</li>
    <li>The SOL prevents a lawsuit but does not erase the debt &mdash; collectors can still contact you.</li>
    <li>North Dakota&rsquo;s 6-year SOL is longer than New Hampshire (3 years) but shorter than Rhode Island and West Virginia (both 10 years).</li>
</ul>

<div class="key-takeaway">
    <strong>Being contacted by a medical debt collector in North Dakota?</strong> Know your rights under the federal Fair Debt Collection Practices Act (FDCPA). You can request debt validation in writing within 30 days of first contact, and collectors must cease contact if you send a written cease-and-desist letter.
</div>

<h2 id="case-studies">7. Case studies</h2>

<div class="case-study">
    <h3>Fargo patient resolves out-of-network lab billing under No Surprises Act</h3>
    <p>A Fargo patient had a scheduled outpatient procedure at an in-network hospital. The hospital sent lab samples to an out-of-network laboratory, which billed the patient $1,100 beyond her in-network deductible. Under the federal No Surprises Act, ancillary services at in-network facilities cannot generate balance bills without prior written consent.</p>
    <p>The patient filed a complaint with the ND Insurance Department. The department confirmed the violation and required reprocessing at in-network rates. <strong>Total savings: $1,100.</strong></p>
</div>

<div class="case-study">
    <h3>Bismarck resident qualifies for retroactive Medicaid after hospitalization</h3>
    <p>An uninsured Bismarck resident earning $16,800/year (115% FPL) was hospitalized for three days following a car accident, resulting in a $22,400 bill. A hospital social worker identified Medicaid eligibility. The patient applied for ND Medicaid and was enrolled retroactively to the date of hospitalization.</p>
    <p>Medicaid covered the full hospitalization cost. <strong>Total bill eliminated: $22,400.</strong></p>
</div>

<h2 id="faq">Frequently asked questions</h2>

<div class="faq-section">
    <div class="faq-item">
        <h3>Does North Dakota have surprise billing protections?</h3>
        <p>Yes. NDCC §26.1-36-09.16 prohibits balance billing in certain situations, and the federal No Surprises Act applies statewide. Out-of-network providers at in-network facilities generally cannot bill beyond your in-network cost-sharing. File complaints with the ND Insurance Department at insurance.nd.gov.</p>
    </div>
    <div class="faq-item">
        <h3>How do I apply for charity care at a North Dakota hospital?</h3>
        <p>Contact the hospital&rsquo;s financial counseling office and request a financial assistance application. Bring proof of income and ND residency. Apply before making any payments &mdash; hospitals may not retroactively grant assistance after payment is received.</p>
    </div>
    <div class="faq-item">
        <h3>Does North Dakota have Medicaid expansion?</h3>
        <p>Yes. North Dakota expanded Medicaid in 2014. Adults ages 19&ndash;64 with income at or below 138% FPL (approximately $20,120/year for a single person) qualify. Apply through ND DHS at dhs.nd.gov.</p>
    </div>
    <div class="faq-item">
        <h3>What is the statute of limitations on medical debt in North Dakota?</h3>
        <p>Under NDCC §28-01-16, the SOL is 6 years. After 6 years from the date of last activity, creditors cannot win a court judgment. Making any payment or written acknowledgment can reset this clock.</p>
    </div>
    <div class="faq-item">
        <h3>How much can a creditor garnish from my wages in North Dakota?</h3>
        <p>North Dakota follows the federal cap of 25% of disposable earnings or the amount exceeding 30 times the federal minimum wage per week, whichever is less. Social Security and certain other income is fully exempt from garnishment.</p>
    </div>
</div>

<h2 id="sources">Sources</h2>

<ul class="sources-list">
    <li><a href="https://www.legis.nd.gov/cencode/t28c01.pdf" target="_blank" rel="noopener">NDCC §28-01-16: Statute of Limitations on Written Contracts</a></li>
    <li><a href="https://www.insurance.nd.gov/consumers/health-insurance" target="_blank" rel="noopener">ND Insurance Department: Health Insurance Consumer Resources</a></li>
    <li><a href="https://www.dhs.nd.gov/services/medical-services/medicaid" target="_blank" rel="noopener">ND Department of Human Services: Medicaid Program</a></li>
    <li><a href="https://www.cms.gov/nosurprises" target="_blank" rel="noopener">CMS: No Surprises Act Consumer Resources</a></li>
    <li><a href="https://www.cms.gov/hospital-price-transparency" target="_blank" rel="noopener">CMS Hospital Price Transparency Rule</a></li>
    <li><a href="https://oig.hhs.gov/fraud/report-fraud/" target="_blank" rel="noopener">HHS OIG: Report Healthcare Fraud</a></li>
</ul>
""",
})
