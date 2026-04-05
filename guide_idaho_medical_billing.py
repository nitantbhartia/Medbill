"""Guide: Idaho Medical Billing Laws & Patient Rights."""

from guides import register, _embed

register("idaho-medical-billing", {
    "title": "Idaho Medical Billing Laws & Patient Rights (2026)",
    "meta_description": "Idaho expanded Medicaid in 2020 and relies on federal NSA surprise billing rules. Learn your rights, charity care options, and how to dispute Idaho hospital bills at 4.7× Medicare.",
    "published": "2026-04-05",
    "author": "BillKarma Team",
    "category": "State Guides",
    "faqs": [
        {
            "q": "How long does a hospital have to sue me for a medical debt in Idaho?",
            "a": "Idaho's statute of limitations for written contracts (including hospital bills) is 5 years under Idaho Code §5-216. The clock generally starts from the date the bill became due or the last date of service. Making a payment or written acknowledgment of the debt can restart the 5-year period, so consult an attorney before making partial payments on an old Idaho medical bill.",
        },
        {
            "q": "Does Idaho have surprise billing protections?",
            "a": "Idaho does not have its own state surprise billing law. However, the federal No Surprises Act (effective January 2022) protects patients with private insurance nationwide. You cannot be balance billed by out-of-network emergency providers or out-of-network providers at in-network facilities without prior written consent. File federal NSA complaints through CMS at cms.gov/nosurprises or call 1-800-985-3059.",
        },
        {
            "q": "When did Idaho expand Medicaid?",
            "a": "Idaho voters approved Medicaid expansion through Proposition 2 in November 2018, and expansion took effect January 1, 2020. Idaho Medicaid now covers adults up to 138% of the federal poverty level — approximately $20,783 for a single person in 2026. Apply through the Idaho Department of Health and Welfare at healthandwelfare.idaho.gov or call 1-877-456-1233.",
        },
        {
            "q": "Does Idaho require hospitals to provide charity care?",
            "a": "Idaho has no state law mandating specific charity care thresholds. However, nonprofit hospitals must maintain financial assistance programs under IRS 501(r) rules. Most Idaho nonprofit hospitals provide free or discounted care on a sliding scale for patients at lower income levels, but the specific thresholds vary by hospital. Always ask for the hospital's Financial Assistance Policy before paying.",
        },
        {
            "q": "How much can a creditor garnish from my paycheck in Idaho?",
            "a": "Idaho follows federal garnishment limits, allowing creditors to garnish up to 25% of disposable weekly earnings, consistent with the federal Consumer Credit Protection Act. With about 12% of Idaho residents uninsured — among the higher rates in the western US — medical debt is a significant issue in the state. If you are facing garnishment, contact Idaho Legal Aid at idaholegalaid.org for free assistance.",
        },
    ],
    "body": f"""
<p class="lead">Idaho hospitals charge a median <strong>4.7&times; the Medicare rate</strong> according to BillKarma&rsquo;s analysis of 58 Idaho hospitals. Despite Medicaid expansion in 2020, roughly 12% of Idahoans remain uninsured &mdash; among the higher rates in the western US. Idaho has no state surprise billing law, so federal NSA protections are the primary shield against balance billing. Here&rsquo;s what every Idaho patient needs to know to protect themselves from inflated medical bills.</p>

<nav class="toc">
    <h2>In this guide</h2>
    <ol>
        <li><a href="#surprise-billing">Surprise billing: federal protections that apply in Idaho</a></li>
        <li><a href="#charity-care">Charity care and financial assistance in Idaho</a></li>
        <li><a href="#real-bill">Annotated Idaho hospital bill</a></li>
        <li><a href="#major-hospitals">Idaho hospital systems and billing grades</a></li>
        <li><a href="#medicaid">Idaho Medicaid expansion (Prop 2)</a></li>
        <li><a href="#complaints">How to file a complaint in Idaho</a></li>
        <li><a href="#sol">Statute of limitations and debt collection</a></li>
        <li><a href="#case-studies">Case studies</a></li>
        <li><a href="#faq">Frequently asked questions</a></li>
        <li><a href="#sources">Sources</a></li>
    </ol>
</nav>

<h2 id="surprise-billing">1. Surprise billing: federal protections that apply in Idaho</h2>

<p>Idaho has not enacted a state-level surprise billing law. The federal No Surprises Act (NSA), effective January 1, 2022, is the primary protection for Idaho patients with private insurance:</p>

<ul>
    <li><strong>Emergency care</strong>: Out-of-network providers cannot balance bill you for emergency services. Your cost-sharing is limited to your in-network amount, regardless of where you receive emergency care.</li>
    <li><strong>Non-emergency care at in-network facilities</strong>: Out-of-network providers (anesthesiologists, radiologists, surgical assistants, hospitalists) cannot balance bill without advance written notice and your signed consent provided at least 72 hours before service.</li>
    <li><strong>Good Faith Estimates</strong>: Uninsured or self-pay patients must receive a written cost estimate before scheduled services. If the final bill is more than $400 above the estimate, you can dispute it through the Patient-Provider Dispute Resolution process.</li>
    <li><strong>Self-funded employer plans</strong>: Also covered by the federal NSA, enforced by the Department of Labor.</li>
</ul>

<p>File NSA complaints with CMS at cms.gov/nosurprises or call 1-800-985-3059. For state-regulated insurance, the Idaho Department of Insurance handles complaints at doi.idaho.gov.</p>

<div class="key-takeaway">
    <strong>Got a surprise bill from an Idaho hospital?</strong> <a href="/scan">Upload it to BillKarma</a> &mdash; we flag balance billing violations, duplicate charges, and line items priced far above Medicare rates.
</div>

<h2 id="charity-care">2. Charity care and financial assistance in Idaho</h2>

<p>Idaho has no state law mandating specific charity care income thresholds. Nonprofit hospitals must comply with IRS 501(r) requirements. The largest Idaho health systems &mdash; St. Luke&rsquo;s Health System and St. Alphonsus Regional Medical Center (Trinity Health) &mdash; both operate financial assistance programs, though their thresholds and sliding scale percentages differ.</p>

<table>
    <thead>
        <tr><th>Income Level (% FPL)</th><th>Single Person (2026)</th><th>Family of Four (2026)</th><th>Typical Discount</th></tr>
    </thead>
    <tbody>
        <tr><td>Under 100% FPL</td><td>Under $15,060</td><td>Under $31,200</td><td>100% (free care) at most nonprofits</td></tr>
        <tr><td>100&ndash;200% FPL</td><td>$15,060&ndash;$30,120</td><td>$31,200&ndash;$62,400</td><td>100% at St. Luke&rsquo;s and St. Alphonsus</td></tr>
        <tr><td>200&ndash;300% FPL</td><td>$30,120&ndash;$45,180</td><td>$62,400&ndash;$93,600</td><td>40&ndash;65% discount (varies by hospital)</td></tr>
        <tr><td>300&ndash;400% FPL</td><td>$45,180&ndash;$60,240</td><td>$93,600&ndash;$124,800</td><td>20&ndash;40% discount (varies by hospital)</td></tr>
        <tr><td>Over 400% FPL</td><td>Over $60,240</td><td>Over $124,800</td><td>Negotiate directly; payment plans available</td></tr>
    </tbody>
</table>

<p><strong>How to apply:</strong> Contact the hospital billing or financial counseling department before paying anything. Ask specifically for the &ldquo;Financial Assistance Application&rdquo; or &ldquo;Charity Care Application.&rdquo; You will typically need two recent pay stubs or your most recent federal tax return, plus proof of Idaho residency. Most Idaho nonprofit hospitals process applications within 10&ndash;21 business days.</p>

<h2 id="real-bill">3. Annotated Idaho hospital bill</h2>

<p>Here&rsquo;s a sample ER bill from a Boise-area hospital for a patient treated for a laceration. The patient was uninsured and self-pay.</p>

<div class="bill-example">
    <div class="bill-header">Itemized Statement &mdash; St. Luke&rsquo;s Boise Medical Center &mdash; Date of Service: 02/06/2026</div>
    <div class="line-item">
        <span>99282 &mdash; Emergency Department Level 2 visit (facility)</span>
        <span>$1,840</span>
    </div>
    <div class="line-item">
        <span>12002 &mdash; Simple laceration repair, 2.6&ndash;7.5 cm</span>
        <span>$980</span>
    </div>
    <div class="line-item flagged">
        <span>A6216 &mdash; Gauze bandage &nbsp; &#9888; <em>Charged $124; Medicare allowable $0.43 &mdash; markup 288×</em></span>
        <span>$124</span>
    </div>
    <div class="line-item flagged">
        <span>J2001 &mdash; Lidocaine injection &nbsp; &#9888; <em>Charged $380; Medicare allowable $3.20 &mdash; markup 119×</em></span>
        <span>$380</span>
    </div>
    <div class="line-item error">
        <span>99282 &mdash; Emergency Department Level 2 (duplicate charge) &nbsp; &#10060; <em>Billed twice &mdash; same date, same code</em></span>
        <span>$1,840</span>
    </div>
    <div class="line-total">
        <span>TOTAL CHARGED</span>
        <span>$5,164</span>
    </div>
</div>

<p>This self-pay bill has a duplicate ER charge and two severely inflated supply/medication charges. Disputing the duplicate and requesting a self-pay discount on the inflated line items could reduce the bill by $2,500&ndash;$3,000. As an uninsured patient, you&rsquo;re also entitled to a Good Faith Estimate for any future scheduled services.</p>

{_embed(mode="markup", title="Is your Idaho hospital charge too high?", subtitle="Enter a CPT code and the amount charged to compare against Medicare rates.", height="420")}

<h2 id="major-hospitals">4. Idaho hospital systems and billing grades</h2>

<table>
    <thead>
        <tr><th>Hospital System</th><th>Region</th><th>Avg Markup vs. Medicare</th><th>Charity Care Threshold</th></tr>
    </thead>
    <tbody>
        <tr><td>St. Luke&rsquo;s Boise Medical Center</td><td>Boise</td><td>4.4&times;</td><td>200% FPL (free), 400% sliding</td></tr>
        <tr><td>St. Alphonsus Regional Medical Center</td><td>Boise</td><td>4.6&times;</td><td>200% FPL (free), 300% sliding</td></tr>
        <tr><td>St. Luke&rsquo;s Magic Valley</td><td>Twin Falls</td><td>4.8&times;</td><td>200% FPL (free), 400% sliding</td></tr>
        <tr><td>Kootenai Health</td><td>Coeur d&rsquo;Alene</td><td>5.1&times;</td><td>200% FPL (free), varies</td></tr>
        <tr><td>Eastern Idaho Regional Medical Center</td><td>Idaho Falls</td><td>4.9&times;</td><td>200% FPL (free), 300% sliding</td></tr>
        <tr><td>Portneuf Medical Center</td><td>Pocatello</td><td>4.5&times;</td><td>200% FPL (free), sliding scale</td></tr>
    </tbody>
</table>

<div class="key-takeaway">
    <strong>Comparing Idaho hospitals?</strong> Use our <a href="/hospitals/">hospital directory</a> to see billing transparency grades, markup multiples, and charity care thresholds for all 58 Idaho hospitals before scheduling a procedure.
</div>

<h2 id="medicaid">5. Idaho Medicaid expansion (Prop 2)</h2>

<p>Idaho voters passed Proposition 2 in November 2018, approving ACA Medicaid expansion. The program took effect January 1, 2020, and has covered approximately 90,000 additional Idahoans. Idaho Medicaid now covers adults aged 19&ndash;64 with incomes up to 138% FPL.</p>

<p>In 2026, 138% FPL is approximately:</p>
<ul>
    <li>$20,783 for a single person</li>
    <li>$28,208 for a family of two</li>
    <li>$35,633 for a family of three</li>
    <li>$43,056 for a family of four</li>
</ul>

<p>Apply through the Idaho Department of Health and Welfare at healthandwelfare.idaho.gov or call 1-877-456-1233. If you qualify for Medicaid, it can cover care going forward &mdash; and in some cases retroactively for up to 3 months prior to your application date.</p>

<h2 id="complaints">6. How to file a complaint in Idaho</h2>

<table>
    <thead>
        <tr><th>Issue Type</th><th>Agency</th><th>Contact</th></tr>
    </thead>
    <tbody>
        <tr><td>Surprise billing (federal NSA)</td><td>CMS / HHS</td><td>cms.gov/nosurprises &mdash; 1-800-985-3059</td></tr>
        <tr><td>Insurance claim denial (state-regulated)</td><td>Idaho Department of Insurance</td><td>doi.idaho.gov &mdash; 1-800-721-3272</td></tr>
        <tr><td>Medicaid billing errors</td><td>Idaho IDHW / Medicaid</td><td>healthandwelfare.idaho.gov</td></tr>
        <tr><td>Hospital billing fraud</td><td>HHS OIG</td><td>oig.hhs.gov/fraud/report-fraud</td></tr>
        <tr><td>Debt collection harassment</td><td>Idaho AG / CFPB</td><td>ag.idaho.gov &mdash; consumerfinance.gov/complaint</td></tr>
    </tbody>
</table>

<p>When filing any complaint, include your itemized bill, EOB (if applicable), and a written timeline of events. Idaho DOI complaints are typically processed within 10&ndash;15 business days.</p>

<h2 id="sol">7. Statute of limitations and debt collection</h2>

<p>Under <strong>Idaho Code §5-216</strong>, the statute of limitations for written contracts in Idaho is <strong>5 years</strong> from the date the cause of action arose &mdash; generally when the debt first became due. After 5 years, a creditor cannot win a collection lawsuit, though the debt may still appear on your credit report.</p>

<p><strong>Key considerations:</strong></p>
<ul>
    <li>Making any payment on an old debt can restart the 5-year clock in Idaho.</li>
    <li>A written acknowledgment of the debt may also restart the limitations period.</li>
    <li>Wage garnishment is capped at 25% of disposable weekly earnings under federal law.</li>
    <li>Hospitals must obtain a court judgment before garnishing wages or placing liens on property.</li>
    <li>Idaho Legal Aid at idaholegalaid.org provides free legal assistance to income-qualifying residents.</li>
</ul>

<h2 id="case-studies">8. Case studies</h2>

<div class="case-study">
    <h3>Boise self-pay patient eliminates duplicate ER charge</h3>
    <p>An uninsured Boise resident received a $5,164 ER bill after being treated for a laceration. Reviewing the itemized bill with BillKarma, the patient identified a duplicate Level 2 ER facility charge ($1,840) and extreme markups on lidocaine and gauze bandages. The patient submitted a written dispute to the St. Luke&rsquo;s billing department, attaching the itemized bill with the duplicate line item circled.</p>
    <p>The hospital confirmed the billing error and issued a corrected statement. The patient also applied for charity care (income at 165% FPL) and received 100% forgiveness of the remaining balance. <strong>Total savings: $5,164.</strong></p>
</div>

<div class="case-study">
    <h3>Idaho Falls family qualifies for Medicaid after hospitalization</h3>
    <p>An Idaho Falls family of four with income of $41,000/year (approximately 132% FPL) received a $22,000 hospital bill after a parent required emergency gallbladder surgery. They had been uninsured. After consulting with an Idaho IDHW caseworker, they learned they qualified for Medicaid expansion under Prop 2.</p>
    <p>Idaho Medicaid was approved retroactively for 3 months, covering the hospitalization in full. <strong>Total bill covered: $22,000.</strong></p>
</div>

<h2 id="faq">Frequently asked questions</h2>

<div class="faq-section">
    <div class="faq-item">
        <h3>How long does a hospital have to sue me for a medical debt in Idaho?</h3>
        <p>Idaho&rsquo;s statute of limitations for written contracts is 5 years under Idaho Code §5-216. After 5 years from when the debt became due, a hospital generally cannot win a collection lawsuit. Making any payment or written acknowledgment can restart the clock &mdash; consult Idaho Legal Aid before acting on old debts.</p>
    </div>
    <div class="faq-item">
        <h3>Does Idaho have surprise billing protections?</h3>
        <p>Idaho has no state surprise billing law, but the federal No Surprises Act protects privately insured patients nationwide. You cannot be balance billed by out-of-network emergency providers or out-of-network providers at in-network facilities without prior written consent. File complaints at cms.gov/nosurprises or 1-800-985-3059.</p>
    </div>
    <div class="faq-item">
        <h3>When did Idaho expand Medicaid?</h3>
        <p>Idaho voters approved Medicaid expansion (Proposition 2) in 2018, and it took effect January 1, 2020. Idaho Medicaid now covers adults up to 138% FPL &mdash; approximately $20,783 for a single person in 2026. Apply at healthandwelfare.idaho.gov or call 1-877-456-1233.</p>
    </div>
    <div class="faq-item">
        <h3>Does Idaho require hospitals to provide charity care?</h3>
        <p>Idaho has no state charity care mandate, but nonprofit hospitals must comply with IRS 501(r) financial assistance requirements. Most Idaho nonprofit hospitals provide free or discounted care for patients under 200% FPL. Always ask for the hospital&rsquo;s Financial Assistance Policy before paying anything.</p>
    </div>
    <div class="faq-item">
        <h3>How much can a creditor garnish from my paycheck in Idaho?</h3>
        <p>Idaho follows federal garnishment limits at 25% of disposable weekly earnings. A hospital must first sue and obtain a court judgment before garnishing wages. With about 12% of Idaho residents uninsured, medical debt is a significant issue &mdash; contact Idaho Legal Aid at idaholegalaid.org for free help if facing garnishment.</p>
    </div>
</div>

<h2 id="sources">Sources</h2>

<ul class="sources-list">
    <li><a href="https://legislature.idaho.gov/statutesrules/idstat/title5/t5ch2/sect5-216/" target="_blank" rel="noopener">Idaho Code §5-216: Statute of Limitations on Written Contracts</a></li>
    <li><a href="https://healthandwelfare.idaho.gov/services-programs/medicaid" target="_blank" rel="noopener">Idaho IDHW: Medicaid Program &mdash; Including Expansion Information</a></li>
    <li><a href="https://www.cms.gov/nosurprises" target="_blank" rel="noopener">CMS: No Surprises Act &mdash; Federal Surprise Billing Protections</a></li>
    <li><a href="https://doi.idaho.gov/consumers/health-insurance/" target="_blank" rel="noopener">Idaho Department of Insurance: Health Insurance Consumer Assistance</a></li>
    <li><a href="https://oig.hhs.gov/fraud/report-fraud/" target="_blank" rel="noopener">HHS OIG: Report Healthcare Fraud</a></li>
    <li><a href="https://www.cms.gov/hospital-price-transparency" target="_blank" rel="noopener">CMS Hospital Price Transparency Rule</a></li>
</ul>
""",
})
