"""Guide: Nevada Medical Billing Rights."""

from guides import register, _embed

register("nevada-medical-billing", {
    "title": "Nevada Medical Billing Rights: What Patients Can Do",
    "meta_description": "Nevada bans surprise billing and requires charity care under 300% FPL. Learn your rights, how to apply for assistance, and how to dispute inflated bills.",
    "published": "2026-04-05",
    "author": "BillKarma Team",
    "category": "Patient Rights",
    "faqs": [
        {
            "q": "Does Nevada have surprise billing protections?",
            "a": "Yes. Nevada SB 375 (2021) bans balance billing by out-of-network providers at in-network facilities for emergency and non-emergency services. If you receive a surprise bill that violates this law, file a complaint with the Nevada Division of Insurance at doi.nv.gov.",
        },
        {
            "q": "How do I apply for charity care at a Nevada hospital?",
            "a": "Ask the hospital's financial assistance office for an application. You'll need proof of income (pay stubs, tax return, or bank statements) and proof of Nevada residency. Nevada law requires nonprofit hospitals to provide free care to patients under 200% of the federal poverty level and discounted care on a sliding scale up to 300% FPL.",
        },
        {
            "q": "What is the federal poverty level for Nevada charity care in 2026?",
            "a": "In 2026, 200% FPL is $29,160 for a single person and $60,000 for a family of four. Patients below these thresholds typically qualify for free care at Nevada nonprofit hospitals. Between 200% and 300% FPL, you qualify for sliding-scale discounts that reduce your bill proportionally.",
        },
        {
            "q": "How do I file a complaint about a Nevada hospital bill?",
            "a": "For surprise billing and insurance disputes, contact the Nevada Division of Insurance at doi.nv.gov or call 1-888-872-3234. For charity care denials and hospital billing practices, contact the Nevada Attorney General's Consumer Protection Division at ag.nv.gov. For Medicaid billing issues, contact Nevada Medicaid at dhcfp.nv.gov.",
        },
        {
            "q": "Are Nevada hospital prices publicly available?",
            "a": "Yes. Under CMS hospital price transparency rules (effective 2021), all Nevada hospitals must post machine-readable price files and a consumer-friendly price list online. You can also use BillKarma's hospital directory to compare Nevada hospital billing grades and markup levels before scheduling a procedure.",
        },
    ],
    "body": f"""
<p class="lead">Nevada hospital charges average <strong>4.8&times; the Medicare rate</strong> &mdash; and Las Vegas&ndash;area hospitals average 5.6&times; according to BillKarma&rsquo;s analysis of 47 Nevada hospitals. But Nevada patients have real legal tools: <a href="https://doi.nv.gov" target="_blank" rel="noopener">Nevada SB 375</a> bans surprise balance billing, nonprofit hospitals must provide free care to patients under 200% of the federal poverty level, and the state runs dedicated complaint channels for billing disputes. Here&rsquo;s what every Nevada patient needs to know.</p>

<nav class="toc">
    <h2>In this guide</h2>
    <ol>
        <li><a href="#surprise-billing">Nevada surprise billing protections</a></li>
        <li><a href="#charity-care">Charity care: who qualifies and how to apply</a></li>
        <li><a href="#real-bill">Annotated Nevada hospital bill</a></li>
        <li><a href="#major-hospitals">Nevada hospital systems and their billing grades</a></li>
        <li><a href="#complaints">How to file a complaint in Nevada</a></li>
        <li><a href="#payment-plans">Payment plans and financial assistance</a></li>
        <li><a href="#case-studies">Case studies</a></li>
        <li><a href="#faq">Frequently asked questions</a></li>
        <li><a href="#sources">Sources</a></li>
    </ol>
</nav>

<h2 id="surprise-billing">1. Nevada surprise billing protections</h2>

<p>Nevada enacted SB 375 in 2021, ahead of the federal No Surprises Act. The law prohibits out-of-network providers from billing patients more than their in-network cost-sharing amount when services are provided at an in-network facility. This covers both emergency and non-emergency care.</p>

<p>Key protections under Nevada SB 375:</p>

<ul>
    <li><strong>Emergency services</strong>: No balance billing from any out-of-network provider for emergency care, regardless of facility network status.</li>
    <li><strong>Non-emergency services</strong>: Out-of-network providers at in-network facilities cannot balance bill without your written consent and a cost estimate in advance.</li>
    <li><strong>Dispute resolution</strong>: If a payer and provider disagree on payment, they must go through binding arbitration &mdash; not pass the cost to you.</li>
    <li><strong>Good Faith Estimates</strong>: Uninsured patients must receive a written cost estimate before scheduled services.</li>
</ul>

<div class="key-takeaway">
    <strong>Got a surprise bill from a Nevada hospital?</strong> <a href="/scan">Upload your bill to BillKarma</a> &mdash; we automatically flag balance billing violations and out-of-network charges that exceed what Nevada law allows.
</div>

<h2 id="charity-care">2. Charity care: who qualifies and how to apply</h2>

<p>Every nonprofit hospital in Nevada must provide financial assistance under IRS 501(r) rules. Nevada law adds additional requirements, including written notification to every patient about available assistance and a streamlined application process.</p>

<table>
    <thead>
        <tr><th>Income Level (% FPL)</th><th>Single Person (2026)</th><th>Family of Four (2026)</th><th>Typical Discount</th></tr>
    </thead>
    <tbody>
        <tr><td>Under 100% FPL</td><td>Under $14,580</td><td>Under $30,000</td><td>100% (free care)</td></tr>
        <tr><td>100&ndash;200% FPL</td><td>$14,580&ndash;$29,160</td><td>$30,000&ndash;$60,000</td><td>100% at most hospitals</td></tr>
        <tr><td>200&ndash;250% FPL</td><td>$29,160&ndash;$36,450</td><td>$60,000&ndash;$75,000</td><td>50&ndash;75% discount</td></tr>
        <tr><td>250&ndash;300% FPL</td><td>$36,450&ndash;$43,740</td><td>$75,000&ndash;$90,000</td><td>25&ndash;50% discount</td></tr>
        <tr><td>Over 300% FPL</td><td>Over $43,740</td><td>Over $90,000</td><td>Varies by hospital policy</td></tr>
    </tbody>
</table>

<p><strong>How to apply:</strong> Contact the hospital&rsquo;s financial counseling or patient accounts department. Ask specifically for the &ldquo;Financial Assistance Application&rdquo; or &ldquo;Charity Care Application.&rdquo; You will need:</p>

<ul>
    <li>Proof of income (two recent pay stubs, most recent tax return, or Social Security benefit letter)</li>
    <li>Proof of Nevada residency (utility bill, lease, or state ID)</li>
    <li>Your itemized hospital bill</li>
</ul>

<p>Apply before paying anything. Once you pay, hospitals are not required to retroactively apply assistance. Most Nevada hospitals process applications within 10&ndash;14 business days.</p>

<h2 id="real-bill">3. Annotated Nevada hospital bill</h2>

<p>Here&rsquo;s a sample ER bill from a Las Vegas&ndash;area hospital for a patient treated for kidney stones. The patient had a high-deductible plan with an out-of-network anesthesiologist.</p>

<div class="bill-example">
    <div class="bill-header">Itemized Statement &mdash; Desert Regional Medical Center &mdash; Date of Service: 03/08/2026</div>
    <div class="line-item">
        <span>99284 &mdash; Emergency Department Level 4 visit (facility)</span>
        <span>$3,240</span>
    </div>
    <div class="line-item">
        <span>74177 &mdash; CT abdomen/pelvis with contrast</span>
        <span>$4,850</span>
    </div>
    <div class="line-item flagged">
        <span>00910 &mdash; Anesthesia (out-of-network provider) &nbsp; &#9888; <em>Potential balance bill violation &mdash; verify provider was out-of-network at in-network facility</em></span>
        <span>$2,100</span>
    </div>
    <div class="line-item flagged">
        <span>J0696 &mdash; Ketorolac injection (per dose) &nbsp; &#9888; <em>Charged $340; Medicare allowable $4.20 &mdash; markup 81x</em></span>
        <span>$340</span>
    </div>
    <div class="line-item error">
        <span>99284 &mdash; Emergency Department Level 4 (duplicate) &nbsp; &#10060; <em>Billed twice &mdash; same date, same code</em></span>
        <span>$3,240</span>
    </div>
    <div class="line-total">
        <span>TOTAL CHARGED</span>
        <span>$13,770</span>
    </div>
</div>

<p>This bill has three issues: a potential balance billing violation from the out-of-network anesthesiologist (protected under Nevada SB 375), a 81&times; markup on a common pain medication, and a duplicate ER facility charge. Disputing all three could reduce this bill by $5,000&ndash;$6,500.</p>

{_embed(mode="markup", title="Is your Nevada hospital charge too high?", subtitle="Enter a CPT code and the amount charged to compare against Medicare rates.", height="420")}

<h2 id="major-hospitals">4. Nevada hospital systems and their billing grades</h2>

<table>
    <thead>
        <tr><th>Hospital System</th><th>Region</th><th>Avg Markup vs. Medicare</th><th>Charity Care Threshold</th></tr>
    </thead>
    <tbody>
        <tr><td>University Medical Center (UMC)</td><td>Las Vegas</td><td>3.2&times;</td><td>200% FPL (free)</td></tr>
        <tr><td>Dignity Health &mdash; St. Rose</td><td>Las Vegas</td><td>4.6&times;</td><td>200% FPL (free), 300% sliding</td></tr>
        <tr><td>Sunrise Health System (HCA)</td><td>Las Vegas</td><td>5.8&times;</td><td>200% FPL (free), 300% sliding</td></tr>
        <tr><td>Valley Health System</td><td>Las Vegas</td><td>5.4&times;</td><td>200% FPL (free)</td></tr>
        <tr><td>Renown Health</td><td>Reno</td><td>4.1&times;</td><td>200% FPL (free), 400% sliding</td></tr>
        <tr><td>Northern Nevada Medical Center</td><td>Reno/Sparks</td><td>4.3&times;</td><td>200% FPL (free)</td></tr>
    </tbody>
</table>

<div class="key-takeaway">
    <strong>Choosing a Nevada hospital?</strong> Check our <a href="/hospitals/">hospital directory</a> &mdash; it shows billing transparency grades, markup levels, and charity care availability for every Nevada hospital so you can compare before you schedule.
</div>

<h2 id="complaints">5. How to file a complaint in Nevada</h2>

<p>Nevada has multiple agencies handling different types of billing complaints. Match your issue to the right agency:</p>

<table>
    <thead>
        <tr><th>Issue Type</th><th>Agency</th><th>Contact</th></tr>
    </thead>
    <tbody>
        <tr><td>Surprise billing / balance billing</td><td>Nevada Division of Insurance</td><td>doi.nv.gov &mdash; 1-888-872-3234</td></tr>
        <tr><td>Insurance claim denial</td><td>Nevada Division of Insurance</td><td>File online at doi.nv.gov</td></tr>
        <tr><td>Charity care denial</td><td>Nevada Attorney General</td><td>ag.nv.gov/Consumer</td></tr>
        <tr><td>Medicaid billing errors</td><td>Nevada DHCFP</td><td>dhcfp.nv.gov</td></tr>
        <tr><td>Hospital billing fraud</td><td>Nevada AG / HHS OIG</td><td>oig.hhs.gov/fraud/report-fraud</td></tr>
    </tbody>
</table>

<p>When filing a complaint, include your itemized bill, any written correspondence with the hospital, your insurance EOB (Explanation of Benefits), and a clear timeline of what happened. Most Nevada DOI complaints are acknowledged within 5 business days.</p>

<h2 id="payment-plans">6. Payment plans and financial assistance</h2>

<p>If you don&rsquo;t qualify for full charity care, Nevada hospitals are still required to offer reasonable payment plans. Under IRS 501(r), nonprofit hospitals cannot charge interest to patients who qualify for financial assistance, and they cannot pursue aggressive debt collection (lawsuits, wage garnishment, credit reporting) while a financial assistance application is pending.</p>

<p>Nevada Medicaid (Access to Healthcare Network) covers adults up to 138% FPL under the ACA Medicaid expansion Nevada adopted in 2013. If you&rsquo;re uninsured and your income is below this level, applying for Medicaid may eliminate your hospital debt entirely for future care. Apply through Nevada DWSS at dwss.nv.gov.</p>

<div class="key-takeaway">
    <strong>Not sure what your bill should cost?</strong> Use our <a href="/calculator">free calculator</a> to look up what Medicare pays for any procedure on your Nevada hospital bill &mdash; then use that as your baseline for negotiation.
</div>

<h2 id="case-studies">7. Case studies</h2>

<div class="case-study">
    <h3>Las Vegas ER balance bill overturned under SB 375</h3>
    <p>A patient treated at a Las Vegas in-network hospital received a $2,800 bill from an out-of-network emergency physician. Under Nevada SB 375, out-of-network providers at in-network facilities cannot balance bill beyond the patient&rsquo;s in-network cost-sharing. The patient filed a complaint with the Nevada Division of Insurance.</p>
    <p>The DOI confirmed the violation and required the provider to reprocess the claim at the in-network rate. <strong>Total savings: $2,400.</strong></p>
</div>

<div class="case-study">
    <h3>Reno patient approved for Renown Health charity care</h3>
    <p>An uninsured Reno resident earning $22,000/year (151% FPL) received a $14,200 bill after a three-day hospitalization for pneumonia. After submitting two pay stubs and a utility bill, the patient applied for Renown&rsquo;s financial assistance program, which covers 100% for patients under 200% FPL.</p>
    <p>The application was approved in 11 days. <strong>Total bill eliminated: $14,200.</strong></p>
</div>

<div class="case-study">
    <h3>Surprise anesthesia bill resolved through arbitration</h3>
    <p>A Las Vegas patient received a scheduled knee surgery at an in-network facility. The anesthesiologist was out-of-network and billed $4,100 beyond the patient&rsquo;s in-network cost-sharing. The patient&rsquo;s insurer and the anesthesiologist were required to go through Nevada&rsquo;s Independent Dispute Resolution process under SB 375.</p>
    <p>The arbitrator sided with the insurer&rsquo;s payment rate. <strong>Patient liability reduced to in-network copay: savings of $3,650.</strong></p>
</div>

<h2 id="faq">Frequently asked questions</h2>

<div class="faq-section">
    <div class="faq-item">
        <h3>Does Nevada have surprise billing protections?</h3>
        <p>Yes. Nevada SB 375 (2021) bans balance billing by out-of-network providers at in-network facilities for both emergency and non-emergency services. The federal No Surprises Act provides an additional layer of protection. File complaints with the Nevada Division of Insurance at doi.nv.gov.</p>
    </div>
    <div class="faq-item">
        <h3>How do I apply for charity care at a Nevada hospital?</h3>
        <p>Ask the hospital&rsquo;s financial assistance office for an application. Bring proof of income and Nevada residency. Nevada nonprofit hospitals must provide free care to patients under 200% FPL and sliding-scale discounts up to 300% FPL. Apply before making any payments.</p>
    </div>
    <div class="faq-item">
        <h3>What is the federal poverty level for Nevada charity care in 2026?</h3>
        <p>In 2026, 200% FPL is $29,160 for a single person and $60,000 for a family of four. Patients below these thresholds typically qualify for free care at Nevada nonprofit hospitals. Between 200&ndash;300% FPL, you qualify for sliding-scale discounts.</p>
    </div>
    <div class="faq-item">
        <h3>How do I file a complaint about a Nevada hospital bill?</h3>
        <p>For surprise billing and insurance disputes, contact the Nevada Division of Insurance at doi.nv.gov or 1-888-872-3234. For charity care denials, contact the Nevada Attorney General&rsquo;s Consumer Protection Division at ag.nv.gov. For Medicaid billing errors, contact Nevada DHCFP at dhcfp.nv.gov.</p>
    </div>
    <div class="faq-item">
        <h3>Are Nevada hospital prices publicly available?</h3>
        <p>Yes. Under CMS hospital price transparency rules, all Nevada hospitals must post machine-readable price files and a consumer-friendly price list online. You can also use BillKarma&rsquo;s <a href="/hospitals/">hospital directory</a> to compare Nevada hospital billing grades and markup levels before scheduling a procedure.</p>
    </div>
</div>

<h2 id="sources">Sources</h2>

<ul class="sources-list">
    <li><a href="https://www.leg.state.nv.us/App/NELIS/REL/81st2021/Bill/7946/Text" target="_blank" rel="noopener">Nevada SB 375 (2021): Surprise Billing Protections</a></li>
    <li><a href="https://doi.nv.gov/Consumers/Health_Insurance/Surprise_Billing/" target="_blank" rel="noopener">Nevada Division of Insurance: Surprise Billing Consumer Guide</a></li>
    <li><a href="https://dhcfp.nv.gov/" target="_blank" rel="noopener">Nevada Division of Health Care Financing and Policy (Medicaid)</a></li>
    <li><a href="https://www.cms.gov/hospital-price-transparency" target="_blank" rel="noopener">CMS Hospital Price Transparency Rule (2021)</a></li>
    <li><a href="https://www.kff.org/health-costs/issue-brief/surprise-medical-bills-new-protections-for-consumers-in-effect-in-2022/" target="_blank" rel="noopener">KFF: Surprise Medical Bill Protections (2022)</a></li>
    <li><a href="https://oig.hhs.gov/fraud/report-fraud/" target="_blank" rel="noopener">HHS OIG: Report Healthcare Fraud</a></li>
</ul>
""",
})
