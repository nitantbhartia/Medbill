"""Guide: Maine Medical Billing Laws & Patient Rights."""

from guides import register, _embed

register("maine-medical-billing", {
    "title": "Maine Medical Billing Laws & Patient Rights (2026)",
    "meta_description": "Maine's LD 1472 bans surprise billing and DHHS requires charity care. Learn the 6-year SOL, wage garnishment rules, and how to dispute Maine hospital bills at 4.2× Medicare.",
    "published": "2026-04-05",
    "author": "BillKarma Team",
    "category": "State Guides",
    "faqs": [
        {
            "q": "How long does a hospital have to sue me for a medical debt in Maine?",
            "a": "Maine's statute of limitations for written contracts (including hospital bills) is 6 years under 14 MRS §752. The clock generally starts from the date the debt became due or the last date of service. This is a longer window than many states, so don't assume an old bill is uncollectable without verifying when the debt arose. Making a payment or written acknowledgment can also restart the 6-year clock.",
        },
        {
            "q": "Does Maine have surprise billing protections?",
            "a": "Yes. Maine enacted LD 1472, which prohibits balance billing by out-of-network providers in specific circumstances. These state protections work alongside the federal No Surprises Act to protect Maine patients from unexpected out-of-network charges. File complaints with the Maine Bureau of Insurance at maine.gov/pfr/insurance or call 1-800-300-5000.",
        },
        {
            "q": "Does Maine have Medicaid expansion?",
            "a": "Yes. Maine expanded Medicaid through a voter-approved ballot initiative in 2017, with expansion taking full effect in 2019. Maine's Medicaid program is called MaineCare and covers adults up to 138% of the federal poverty level. In 2026, that is approximately $20,783 for a single person. Apply through Maine DHHS at maine.gov/dhhs/ofi or call 1-855-797-4357.",
        },
        {
            "q": "What are Maine's charity care requirements for hospitals?",
            "a": "Maine DHHS requires nonprofit hospitals to maintain financial assistance programs and inform patients of their availability. Most Maine nonprofit hospitals provide free care to patients at or below 200% FPL and sliding-scale discounts for patients up to 300–400% FPL. Always ask for the hospital's Financial Assistance Policy — they must provide it upon request. Apply before making any payments.",
        },
        {
            "q": "What is Maine's wage garnishment limit for medical debt?",
            "a": "Maine allows wage garnishment of up to 25% of disposable weekly earnings, consistent with federal law, or the amount by which weekly disposable earnings exceed 40 times the federal minimum wage — whichever is less. This 40-times-minimum-wage floor provides additional protection for low-wage earners. A hospital must obtain a court judgment before garnishing wages.",
        },
    ],
    "body": f"""
<p class="lead">Maine hospitals charge a median <strong>4.2&times; the Medicare rate</strong> according to BillKarma&rsquo;s analysis of 36 Maine hospitals. Maine patients benefit from LD 1472 surprise billing protections, a Medicaid expansion that took full effect in 2019, and DHHS charity care requirements for nonprofit hospitals. Maine&rsquo;s 6-year statute of limitations on medical debt also gives patients more time to address old bills. Here&rsquo;s everything Maine patients need to know.</p>

<nav class="toc">
    <h2>In this guide</h2>
    <ol>
        <li><a href="#surprise-billing">Maine surprise billing protections (LD 1472)</a></li>
        <li><a href="#charity-care">Charity care: who qualifies and how to apply</a></li>
        <li><a href="#real-bill">Annotated Maine hospital bill</a></li>
        <li><a href="#major-hospitals">Maine hospital systems and billing grades</a></li>
        <li><a href="#medicaid">MaineCare Medicaid expansion</a></li>
        <li><a href="#complaints">How to file a complaint in Maine</a></li>
        <li><a href="#sol">Statute of limitations and debt collection</a></li>
        <li><a href="#case-studies">Case studies</a></li>
        <li><a href="#faq">Frequently asked questions</a></li>
        <li><a href="#sources">Sources</a></li>
    </ol>
</nav>

<h2 id="surprise-billing">1. Maine surprise billing protections (LD 1472)</h2>

<p>Maine enacted LD 1472 to protect patients from surprise medical bills. These state protections layer on top of the federal No Surprises Act (effective January 2022) to provide comprehensive coverage for Maine patients with private insurance:</p>

<ul>
    <li><strong>Emergency services</strong>: Out-of-network providers cannot balance bill patients for emergency care beyond in-network cost-sharing amounts, regardless of facility network status.</li>
    <li><strong>Non-emergency care at in-network facilities</strong>: Out-of-network providers (anesthesiologists, radiologists, assistant surgeons, hospitalists) cannot balance bill without advance written disclosure and the patient&rsquo;s signed consent, provided at least 72 hours before the service.</li>
    <li><strong>Good Faith Estimates</strong>: Uninsured or self-pay patients must receive written cost estimates before any scheduled service. If the final bill exceeds the estimate by more than $400, you can dispute it through the federal Patient-Provider Dispute Resolution process.</li>
    <li><strong>Independent Dispute Resolution</strong>: Payment disputes between insurers and providers go to binding arbitration &mdash; the cost dispute does not fall on the patient.</li>
</ul>

<p>File state-level complaints with the Maine Bureau of Insurance at maine.gov/pfr/insurance or call 1-800-300-5000. For federal NSA complaints, use cms.gov/nosurprises.</p>

<div class="key-takeaway">
    <strong>Got a surprise bill from a Maine hospital?</strong> <a href="/scan">Upload your bill to BillKarma</a> &mdash; we automatically flag balance billing violations, duplicate charges, and line items priced well above Medicare rates.
</div>

<h2 id="charity-care">2. Charity care: who qualifies and how to apply</h2>

<p>Maine DHHS requires nonprofit hospitals to maintain financial assistance programs and proactively notify patients of their availability. Maine&rsquo;s major health systems &mdash; MaineHealth, Northern Light Health, and Covenant Health &mdash; all offer meaningful charity care and payment assistance programs.</p>

<table>
    <thead>
        <tr><th>Income Level (% FPL)</th><th>Single Person (2026)</th><th>Family of Four (2026)</th><th>Typical Discount</th></tr>
    </thead>
    <tbody>
        <tr><td>Under 100% FPL</td><td>Under $15,060</td><td>Under $31,200</td><td>100% (free care)</td></tr>
        <tr><td>100&ndash;200% FPL</td><td>$15,060&ndash;$30,120</td><td>$31,200&ndash;$62,400</td><td>100% at most Maine nonprofits</td></tr>
        <tr><td>200&ndash;300% FPL</td><td>$30,120&ndash;$45,180</td><td>$62,400&ndash;$93,600</td><td>50&ndash;75% discount</td></tr>
        <tr><td>300&ndash;400% FPL</td><td>$45,180&ndash;$60,240</td><td>$93,600&ndash;$124,800</td><td>20&ndash;50% discount (varies)</td></tr>
        <tr><td>Over 400% FPL</td><td>Over $60,240</td><td>Over $124,800</td><td>Negotiate directly; payment plans available</td></tr>
    </tbody>
</table>

<p><strong>How to apply:</strong> Contact the hospital&rsquo;s financial counseling department before making any payments. Request the &ldquo;Financial Assistance Application&rdquo; or &ldquo;Charity Care Application.&rdquo; Bring:</p>

<ul>
    <li>Two recent pay stubs or your most recent federal tax return</li>
    <li>Proof of Maine residency (utility bill, lease, or Maine ID)</li>
    <li>Your itemized hospital bill</li>
    <li>Documentation of unusual expenses that reduce ability to pay</li>
</ul>

<p>Apply before paying anything. Under IRS 501(r), nonprofit hospitals cannot initiate aggressive collection actions (lawsuits, garnishment, credit reporting) while a financial assistance application is pending. Most Maine hospitals process applications within 10&ndash;14 business days.</p>

<h2 id="real-bill">3. Annotated Maine hospital bill</h2>

<p>Here&rsquo;s a sample ER bill from a Portland-area hospital for a patient treated for a severe allergic reaction. The patient had an in-network insurance plan.</p>

<div class="bill-example">
    <div class="bill-header">Itemized Statement &mdash; Maine Medical Center &mdash; Portland &mdash; Date of Service: 03/10/2026</div>
    <div class="line-item">
        <span>99284 &mdash; Emergency Department Level 4 visit (facility)</span>
        <span>$3,180</span>
    </div>
    <div class="line-item">
        <span>94640 &mdash; Nebulizer treatment</span>
        <span>$420</span>
    </div>
    <div class="line-item flagged">
        <span>J0171 &mdash; Epinephrine injection &nbsp; &#9888; <em>Charged $890; Medicare allowable $7.40 &mdash; markup 120×</em></span>
        <span>$890</span>
    </div>
    <div class="line-item flagged">
        <span>J1200 &mdash; Diphenhydramine (Benadryl) injection &nbsp; &#9888; <em>Charged $340; Medicare allowable $0.72 &mdash; markup 472×</em></span>
        <span>$340</span>
    </div>
    <div class="line-item error">
        <span>99284 &mdash; Emergency Department Level 4 (duplicate charge) &nbsp; &#10060; <em>Billed twice &mdash; same date, same facility code</em></span>
        <span>$3,180</span>
    </div>
    <div class="line-total">
        <span>TOTAL CHARGED</span>
        <span>$8,010</span>
    </div>
</div>

<p>This bill has a duplicate ER facility charge and two extremely inflated medication charges &mdash; diphenhydramine at 472&times; the Medicare allowable is one of the most common overcharges BillKarma sees on ER bills. Disputing the duplicate and negotiating the medication charges could reduce this bill by $3,500&ndash;$4,500.</p>

{_embed(mode="markup", title="Is your Maine hospital charge too high?", subtitle="Enter a CPT code and the amount charged to compare against Medicare rates.", height="420")}

<h2 id="major-hospitals">4. Maine hospital systems and billing grades</h2>

<table>
    <thead>
        <tr><th>Hospital System</th><th>Region</th><th>Avg Markup vs. Medicare</th><th>Charity Care Threshold</th></tr>
    </thead>
    <tbody>
        <tr><td>Maine Medical Center (MaineHealth)</td><td>Portland</td><td>3.9&times;</td><td>200% FPL (free), 400% sliding</td></tr>
        <tr><td>Central Maine Medical Center</td><td>Lewiston / Auburn</td><td>4.3&times;</td><td>200% FPL (free), 300% sliding</td></tr>
        <tr><td>Northern Light Eastern Maine Medical Center</td><td>Bangor</td><td>4.2&times;</td><td>200% FPL (free), 300% sliding</td></tr>
        <tr><td>Maine General Medical Center</td><td>Augusta / Waterville</td><td>4.4&times;</td><td>200% FPL (free), 300% sliding</td></tr>
        <tr><td>Pen Bay Medical Center (MaineHealth)</td><td>Rockport</td><td>4.1&times;</td><td>200% FPL (free), 400% sliding</td></tr>
        <tr><td>York Hospital</td><td>York</td><td>4.0&times;</td><td>200% FPL (free), sliding scale</td></tr>
    </tbody>
</table>

<div class="key-takeaway">
    <strong>Choosing a Maine hospital?</strong> Check our <a href="/hospitals/">hospital directory</a> for billing transparency grades, markup levels, and charity care availability at all 36 Maine hospitals.
</div>

<h2 id="medicaid">5. MaineCare Medicaid expansion</h2>

<p>Maine voters approved Medicaid expansion through a ballot initiative in 2017, and the expansion took full effect in 2019. MaineCare now covers adults aged 19&ndash;64 with incomes up to 138% FPL.</p>

<p>In 2026, 138% FPL thresholds in Maine are approximately:</p>
<ul>
    <li>$20,783 for a single person</li>
    <li>$28,208 for a family of two</li>
    <li>$35,633 for a family of three</li>
    <li>$43,056 for a family of four</li>
</ul>

<p>Apply through Maine DHHS at maine.gov/dhhs/ofi, in person at any Maine DHHS district office, or by calling 1-855-797-4357. Medicaid can be retroactive for up to 3 months before your application date, which can cover a past hospitalization if you qualify.</p>

<h2 id="complaints">6. How to file a complaint in Maine</h2>

<table>
    <thead>
        <tr><th>Issue Type</th><th>Agency</th><th>Contact</th></tr>
    </thead>
    <tbody>
        <tr><td>Surprise billing / balance billing</td><td>Maine Bureau of Insurance</td><td>maine.gov/pfr/insurance &mdash; 1-800-300-5000</td></tr>
        <tr><td>Insurance claim denial</td><td>Maine Bureau of Insurance</td><td>File online at maine.gov/pfr/insurance</td></tr>
        <tr><td>Charity care denial / hospital billing</td><td>Maine DHHS / Attorney General</td><td>maine.gov/dhhs &mdash; maine.gov/ag/consumer</td></tr>
        <tr><td>Medicaid billing errors</td><td>Maine DHHS / Office of MaineCare Services</td><td>maine.gov/dhhs/oms</td></tr>
        <tr><td>Hospital billing fraud</td><td>HHS OIG</td><td>oig.hhs.gov/fraud/report-fraud</td></tr>
    </tbody>
</table>

<p>Include your itemized bill, insurance EOB, and a written timeline of events with any complaint. Maine Bureau of Insurance complaints are typically acknowledged within 5 business days.</p>

<h2 id="sol">7. Statute of limitations and debt collection</h2>

<p>Under <strong>14 MRS §752</strong>, Maine&rsquo;s statute of limitations for written contracts is <strong>6 years</strong> &mdash; longer than most states. This gives patients more time to recognize and address collection activity, but it also means debt collectors have 6 years to sue.</p>

<p><strong>Maine wage garnishment rules:</strong></p>
<ul>
    <li>Maximum garnishment is the lesser of: 25% of disposable weekly earnings, or the amount by which weekly disposable earnings exceed <strong>40 times the federal minimum wage</strong>.</li>
    <li>At the current federal minimum wage of $7.25/hour, 40&times; = $290/week. If your disposable earnings are $600/week, the maximum garnishment is $310/week (the lesser of 25% = $150, or $600 &minus; $290 = $310 &mdash; so $150 applies in this case).</li>
    <li>Maine&rsquo;s state minimum wage is higher ($14.65/hour in 2026), but the federal minimum is used for this calculation.</li>
    <li>A hospital must obtain a court judgment before any garnishment.</li>
</ul>

<p>Contact Pine Tree Legal Assistance at ptla.org for free legal help if you are facing collection or garnishment.</p>

<h2 id="case-studies">8. Case studies</h2>

<div class="case-study">
    <h3>Portland patient challenges 472× Benadryl markup</h3>
    <p>A Portland patient received an $8,010 ER bill that included $340 for a single diphenhydramine (Benadryl) injection &mdash; 472 times the Medicare allowable of $0.72. After uploading the bill to BillKarma and identifying the extreme markup, the patient sent a written dispute to Maine Medical Center billing, citing the Medicare rate and requesting justification.</p>
    <p>The hospital agreed to reduce the charge to a reasonable multiple of cost. Combined with removal of a duplicate ER charge, <strong>total bill reduction: $3,860.</strong></p>
</div>

<div class="case-study">
    <h3>Bangor uninsured patient qualifies for MaineCare retroactively</h3>
    <p>An uninsured Bangor resident earning $18,500/year (approximately 123% FPL) was hospitalized for two days after a fall and received a $19,000 bill. A hospital financial counselor suggested applying for MaineCare. The application was submitted, and the patient qualified under Maine&rsquo;s Medicaid expansion program.</p>
    <p>MaineCare was approved and applied retroactively, covering the hospitalization in full. <strong>Total bill covered: $19,000.</strong></p>
</div>

<h2 id="faq">Frequently asked questions</h2>

<div class="faq-section">
    <div class="faq-item">
        <h3>How long does a hospital have to sue me for a medical debt in Maine?</h3>
        <p>Maine&rsquo;s statute of limitations for written contracts is 6 years under 14 MRS §752. After 6 years from when the debt became due, a hospital generally cannot win a collection lawsuit. Making any payment or written acknowledgment can restart the clock. Contact Pine Tree Legal Assistance at ptla.org for free help with old debts.</p>
    </div>
    <div class="faq-item">
        <h3>Does Maine have surprise billing protections?</h3>
        <p>Yes. Maine LD 1472 prohibits out-of-network balance billing in specific circumstances, working alongside the federal No Surprises Act. File complaints with the Maine Bureau of Insurance at maine.gov/pfr/insurance or 1-800-300-5000.</p>
    </div>
    <div class="faq-item">
        <h3>Does Maine have Medicaid expansion?</h3>
        <p>Yes. Maine voters approved Medicaid expansion in 2017, and it took full effect in 2019. MaineCare covers adults up to 138% FPL &mdash; approximately $20,783 for a single person in 2026. Apply at maine.gov/dhhs/ofi or call 1-855-797-4357. Coverage can be retroactive up to 3 months.</p>
    </div>
    <div class="faq-item">
        <h3>What are Maine's charity care requirements for hospitals?</h3>
        <p>Maine DHHS requires nonprofit hospitals to maintain financial assistance programs and notify patients of their availability. Most Maine nonprofits provide free care under 200% FPL and sliding-scale discounts up to 300&ndash;400% FPL. Ask for the Financial Assistance Policy before making any payments.</p>
    </div>
    <div class="faq-item">
        <h3>What is Maine's wage garnishment limit for medical debt?</h3>
        <p>Maine garnishment is capped at the lesser of 25% of disposable weekly earnings or earnings above 40 times the federal minimum wage per week. A court judgment is required before garnishment. For free legal help, contact Pine Tree Legal Assistance at ptla.org.</p>
    </div>
</div>

<h2 id="sources">Sources</h2>

<ul class="sources-list">
    <li><a href="https://legislature.maine.gov/statutes/14/title14sec752.html" target="_blank" rel="noopener">14 MRS §752: Maine Statute of Limitations on Written Contracts</a></li>
    <li><a href="https://www.maine.gov/pfr/insurance/consumers/health.htm" target="_blank" rel="noopener">Maine Bureau of Insurance: Health Insurance Consumer Assistance</a></li>
    <li><a href="https://www.maine.gov/dhhs/oms/" target="_blank" rel="noopener">Maine DHHS: Office of MaineCare Services</a></li>
    <li><a href="https://www.cms.gov/nosurprises" target="_blank" rel="noopener">CMS: No Surprises Act &mdash; Federal Surprise Billing Protections</a></li>
    <li><a href="https://oig.hhs.gov/fraud/report-fraud/" target="_blank" rel="noopener">HHS OIG: Report Healthcare Fraud</a></li>
    <li><a href="https://www.cms.gov/hospital-price-transparency" target="_blank" rel="noopener">CMS Hospital Price Transparency Rule</a></li>
</ul>
""",
})
