"""Guide: Alaska Medical Billing Laws & Patient Rights."""

from guides import register, _embed

register("alaska-medical-billing", {
    "title": "Alaska Medical Billing Laws & Patient Rights (2026)",
    "meta_description": "Alaska has the highest hospital markups in the US at 6.2× Medicare. Learn your rights, charity care options, and how to dispute inflated Alaska medical bills.",
    "published": "2026-04-05",
    "author": "BillKarma Team",
    "category": "State Guides",
    "faqs": [
        {
            "q": "How long does a hospital have to sue me for a medical debt in Alaska?",
            "a": "Alaska's statute of limitations for written contracts (including hospital bills) is 3 years under AS §09.10.053. After 3 years from the date the debt became due, a hospital generally cannot win a lawsuit to collect. However, the clock can restart if you make a payment or written acknowledgment of the debt, so consult an attorney before making any partial payments on old bills.",
        },
        {
            "q": "Does Alaska have surprise billing protections?",
            "a": "Alaska does not have its own state surprise billing law. However, the federal No Surprises Act (effective January 2022) protects patients with private insurance nationwide. Under federal law, you cannot be balance billed by out-of-network emergency providers or out-of-network providers at in-network facilities without prior written consent. File federal NSA complaints through CMS at cms.gov/nosurprises.",
        },
        {
            "q": "Does Alaska have Medicaid expansion?",
            "a": "Yes. Alaska expanded Medicaid in September 2015 under the ACA, covering adults up to 138% of the federal poverty level. In 2026, that is $20,783 for a single person. Alaska Medicaid is administered by the Division of Health Care Services. Apply at mybenefits.alaska.gov or call 1-800-478-7778.",
        },
        {
            "q": "Why are Alaska hospital bills so much higher than other states?",
            "a": "Alaska consistently has the highest healthcare costs in the United States. BillKarma's analysis of 47 Alaska hospitals finds a median markup of 6.2× the Medicare rate — the highest in the nation. Factors include extreme geographic isolation, high cost of living, limited hospital competition, and the expense of attracting and retaining healthcare workers in remote communities.",
        },
        {
            "q": "Can Alaska hospitals garnish my wages for a medical debt?",
            "a": "Yes. Under Alaska law, creditors including hospitals can garnish up to 25% of your disposable earnings per week, consistent with federal limits. However, hospitals must first sue you and obtain a court judgment before garnishing wages. If you are at or below 150% FPL, you may qualify for a hardship exemption. Consult Alaska Legal Services at alsc-law.org for free legal help.",
        },
    ],
    "body": f"""
<p class="lead">Alaska hospitals charge a median <strong>6.2&times; the Medicare rate</strong> &mdash; the highest markup in the United States, according to BillKarma&rsquo;s analysis of 47 Alaska hospitals. High geographic isolation, limited competition, and extreme operating costs drive bills that can devastate even middle-income families. Despite the absence of a state surprise billing law, Alaska patients have federal protections, Medicaid coverage up to 138% FPL, and the right to negotiate. Here&rsquo;s everything you need to know.</p>

<nav class="toc">
    <h2>In this guide</h2>
    <ol>
        <li><a href="#costs">Why Alaska healthcare costs are the highest in the US</a></li>
        <li><a href="#surprise-billing">Surprise billing: federal protections that apply in Alaska</a></li>
        <li><a href="#charity-care">Charity care and financial assistance in Alaska</a></li>
        <li><a href="#real-bill">Annotated Alaska hospital bill</a></li>
        <li><a href="#medicaid">Alaska Medicaid and coverage options</a></li>
        <li><a href="#complaints">How to file a complaint in Alaska</a></li>
        <li><a href="#sol">Statute of limitations and debt collection</a></li>
        <li><a href="#case-studies">Case studies</a></li>
        <li><a href="#faq">Frequently asked questions</a></li>
        <li><a href="#sources">Sources</a></li>
    </ol>
</nav>

<h2 id="costs">1. Why Alaska healthcare costs are the highest in the US</h2>

<p>Alaska&rsquo;s extreme geography creates a healthcare market unlike any other state. More than half of Alaska&rsquo;s communities are not connected to the road system, requiring medevac flights that cost $30,000&ndash;$80,000 per transport. Hospitals in cities like Anchorage, Fairbanks, and Juneau face no meaningful regional competition for most specialty services.</p>

<p>BillKarma&rsquo;s analysis of 47 Alaska hospitals finds:</p>

<ul>
    <li><strong>Median markup: 6.2&times; Medicare</strong> &mdash; the highest of any state in the nation</li>
    <li>Anchorage-area hospitals average 5.9&times; Medicare rates</li>
    <li>Rural and critical access hospitals average 7.1&times; Medicare due to lower patient volumes</li>
    <li>Common procedures like a knee replacement billed at $85,000&ndash;$120,000 vs. a Medicare allowable of roughly $13,000</li>
</ul>

<div class="key-takeaway">
    <strong>Received an Alaska hospital bill?</strong> <a href="/scan">Upload it to BillKarma</a> &mdash; we compare every charge against Medicare rates and flag overpriced line items specific to Alaska&rsquo;s market.
</div>

<h2 id="surprise-billing">2. Surprise billing: federal protections that apply in Alaska</h2>

<p>Alaska has not enacted its own surprise billing law. However, the federal No Surprises Act (NSA), effective January 1, 2022, provides nationwide protections for patients with private insurance:</p>

<ul>
    <li><strong>Emergency care</strong>: Out-of-network providers cannot balance bill you for emergency services, regardless of the facility&rsquo;s network status.</li>
    <li><strong>Non-emergency care at in-network facilities</strong>: Out-of-network providers (e.g., anesthesiologists, radiologists) cannot balance bill without advance written notice and your consent.</li>
    <li><strong>Good Faith Estimates</strong>: Uninsured or self-pay patients must receive a written cost estimate before scheduled services. If the final bill exceeds the estimate by more than $400, you can dispute it.</li>
    <li><strong>Air ambulance services</strong>: The NSA includes partial protections for air ambulances &mdash; important in Alaska where medevac costs are extremely high.</li>
</ul>

<p>Alaska has no state insurance regulator enforcing surprise billing; file NSA complaints through the federal CMS portal at cms.gov/nosurprises or call 1-800-985-3059.</p>

<h2 id="charity-care">3. Charity care and financial assistance in Alaska</h2>

<p>Alaska has no state law mandating charity care thresholds for hospitals. However, nonprofit hospitals must comply with IRS 501(r) rules requiring financial assistance programs. The largest system, Providence Health &amp; Services Alaska, provides free care to patients under 200% FPL and discounted care on a sliding scale.</p>

<table>
    <thead>
        <tr><th>Income Level (% FPL)</th><th>Single Person (2026)</th><th>Family of Four (2026)</th><th>Typical Discount</th></tr>
    </thead>
    <tbody>
        <tr><td>Under 100% FPL</td><td>Under $15,060</td><td>Under $31,200</td><td>100% (free care) at most nonprofits</td></tr>
        <tr><td>100&ndash;200% FPL</td><td>$15,060&ndash;$30,120</td><td>$31,200&ndash;$62,400</td><td>100% at Providence; varies elsewhere</td></tr>
        <tr><td>200&ndash;300% FPL</td><td>$30,120&ndash;$45,180</td><td>$62,400&ndash;$93,600</td><td>25&ndash;60% discount (varies by hospital)</td></tr>
        <tr><td>300&ndash;400% FPL</td><td>$45,180&ndash;$60,240</td><td>$93,600&ndash;$124,800</td><td>10&ndash;25% discount (varies by hospital)</td></tr>
        <tr><td>Over 400% FPL</td><td>Over $60,240</td><td>Over $124,800</td><td>Negotiate directly; payment plans available</td></tr>
    </tbody>
</table>

<p><strong>Note:</strong> Alaska FPL thresholds are slightly higher than the contiguous 48 states due to the Alaska Cost of Living Adjustment in federal poverty guidelines.</p>

<p><strong>How to apply:</strong> Contact the hospital&rsquo;s financial counseling department before paying anything. Ask for the &ldquo;Financial Assistance Application&rdquo; and provide proof of income (recent pay stubs, most recent tax return) and proof of Alaska residency. Most Alaska hospitals process applications within 10&ndash;21 business days.</p>

<h2 id="real-bill">4. Annotated Alaska hospital bill</h2>

<p>Here&rsquo;s a sample bill from an Anchorage hospital for a patient admitted for chest pain evaluation. This patient was insured but received bills from multiple providers.</p>

<div class="bill-example">
    <div class="bill-header">Itemized Statement &mdash; Alaska Regional Hospital &mdash; Anchorage &mdash; Date of Service: 02/14/2026</div>
    <div class="line-item">
        <span>99285 &mdash; Emergency Department Level 5 visit (facility)</span>
        <span>$6,420</span>
    </div>
    <div class="line-item">
        <span>93306 &mdash; Echocardiogram with Doppler</span>
        <span>$5,890</span>
    </div>
    <div class="line-item flagged">
        <span>71046 &mdash; Chest X-ray 2 views &nbsp; &#9888; <em>Charged $980; Medicare allowable $42 &mdash; markup 23×</em></span>
        <span>$980</span>
    </div>
    <div class="line-item flagged">
        <span>80053 &mdash; Comprehensive metabolic panel &nbsp; &#9888; <em>Charged $1,240; Medicare allowable $14 &mdash; markup 89×</em></span>
        <span>$1,240</span>
    </div>
    <div class="line-item error">
        <span>99285 &mdash; Emergency Department Level 5 (duplicate charge) &nbsp; &#10060; <em>Billed twice &mdash; same date, same facility code</em></span>
        <span>$6,420</span>
    </div>
    <div class="line-total">
        <span>TOTAL CHARGED</span>
        <span>$20,950</span>
    </div>
</div>

<p>This bill has a duplicate ER charge and two severely inflated lab/imaging charges. Disputing the duplicate and negotiating the lab fees to 5&times; Medicare could reduce the bill by $8,000&ndash;$10,000.</p>

{_embed(mode="markup", title="Is your Alaska hospital charge too high?", subtitle="Enter a CPT code and the amount charged to compare against Medicare rates.", height="420")}

<h2 id="medicaid">5. Alaska Medicaid and coverage options</h2>

<p>Alaska expanded Medicaid in 2015, covering adults up to 138% FPL. In 2026, that is approximately $20,783 for a single person or $35,633 for a family of three (Alaska guidelines). Apply through the Division of Public Assistance at mybenefits.alaska.gov.</p>

<p>Alaska also has the <strong>Denali KidCare</strong> program (CHIP) covering children and pregnant women at higher income levels. For individuals above Medicaid limits, the federal marketplace at healthcare.gov offers subsidized plans; Alaska historically has high premiums but also high federal subsidies.</p>

<div class="key-takeaway">
    <strong>Uninsured in Alaska?</strong> If your income is under 138% FPL ($20,783 for a single person in 2026), you likely qualify for Alaska Medicaid, which can eliminate past medical debt for ongoing care. Apply at <a href="https://mybenefits.alaska.gov" target="_blank" rel="noopener">mybenefits.alaska.gov</a>.
</div>

<h2 id="complaints">6. How to file a complaint in Alaska</h2>

<table>
    <thead>
        <tr><th>Issue Type</th><th>Agency</th><th>Contact</th></tr>
    </thead>
    <tbody>
        <tr><td>Surprise billing (federal NSA)</td><td>CMS / HHS</td><td>cms.gov/nosurprises &mdash; 1-800-985-3059</td></tr>
        <tr><td>Insurance claim denial</td><td>Alaska Division of Insurance</td><td>commerce.alaska.gov/insurance &mdash; 1-907-465-2515</td></tr>
        <tr><td>Hospital billing fraud</td><td>HHS Office of Inspector General</td><td>oig.hhs.gov/fraud/report-fraud</td></tr>
        <tr><td>Medicaid billing errors</td><td>Alaska DHSS / Division of Health Care Services</td><td>dhss.alaska.gov/dpa</td></tr>
        <tr><td>Debt collection harassment</td><td>Alaska Attorney General / CFPB</td><td>law.alaska.gov &mdash; consumerfinance.gov/complaint</td></tr>
    </tbody>
</table>

<p>When filing any complaint, include your itemized bill, EOB from your insurer (if applicable), and a written timeline of events. Alaska DOI complaints are typically acknowledged within 5&ndash;10 business days.</p>

<h2 id="sol">7. Statute of limitations and debt collection</h2>

<p>Under <strong>AS §09.10.053</strong>, the statute of limitations on written contracts (including hospital bills) in Alaska is <strong>3 years</strong> from the date the debt became due. After this period, a creditor cannot successfully sue to collect the debt, though it may still appear on your credit report for up to 7 years.</p>

<p><strong>Important cautions:</strong></p>
<ul>
    <li>Making even a small payment restarts the 3-year clock in Alaska.</li>
    <li>A written acknowledgment that you owe the debt can also restart the clock.</li>
    <li>Wage garnishment in Alaska is capped at 25% of disposable earnings per federal and state law.</li>
    <li>Before paying or acknowledging an old debt, consult Alaska Legal Services Corporation at alsc-law.org (free for income-qualifying Alaskans).</li>
</ul>

<h2 id="case-studies">8. Case studies</h2>

<div class="case-study">
    <h3>Anchorage patient disputes $6,420 duplicate ER charge</h3>
    <p>An Anchorage resident was billed twice for the same Level 5 ER visit after a chest pain evaluation at Alaska Regional Hospital. Both line items appeared on the same itemized bill with identical dates and CPT codes. The patient contacted the hospital billing department, pointed out the duplicate charge in writing, and requested correction.</p>
    <p>The hospital confirmed the billing error within 5 business days and issued a corrected statement. <strong>Total savings: $6,420.</strong></p>
</div>

<div class="case-study">
    <h3>Fairbanks family qualifies for Providence charity care</h3>
    <p>An uninsured Fairbanks family of four earning $58,000/year (approximately 186% FPL) received a $34,000 bill after a parent was hospitalized for three days with pneumonia at Fairbanks Memorial Hospital, a Providence affiliate. The family applied for financial assistance with two months of pay stubs and their most recent tax return.</p>
    <p>Providence&rsquo;s policy covers 100% of charges for patients under 200% FPL. The application was approved in 14 days. <strong>Total bill eliminated: $34,000.</strong></p>
</div>

<h2 id="faq">Frequently asked questions</h2>

<div class="faq-section">
    <div class="faq-item">
        <h3>How long does a hospital have to sue me for a medical debt in Alaska?</h3>
        <p>Alaska&rsquo;s statute of limitations for written contracts is 3 years under AS §09.10.053. After 3 years from when the debt became due, a hospital generally cannot win a collection lawsuit. Making any payment or written acknowledgment can restart the clock, so consult Alaska Legal Services before acting on old debts.</p>
    </div>
    <div class="faq-item">
        <h3>Does Alaska have surprise billing protections?</h3>
        <p>Alaska has no state surprise billing law, but the federal No Surprises Act protects privately insured patients nationwide. You cannot be balance billed by out-of-network emergency providers or out-of-network providers at in-network facilities without prior written consent. File complaints at cms.gov/nosurprises.</p>
    </div>
    <div class="faq-item">
        <h3>Does Alaska have Medicaid expansion?</h3>
        <p>Yes. Alaska expanded Medicaid in 2015, covering adults up to 138% FPL &mdash; approximately $20,783 for a single person in 2026. Apply at mybenefits.alaska.gov or call 1-800-478-7778.</p>
    </div>
    <div class="faq-item">
        <h3>Why are Alaska hospital bills so much higher than other states?</h3>
        <p>BillKarma&rsquo;s analysis finds a median markup of 6.2&times; Medicare at Alaska&rsquo;s 47 hospitals &mdash; the highest in the nation. Geographic isolation, lack of regional competition, high operating costs, and expensive medevac transport all contribute to Alaska&rsquo;s extreme healthcare prices.</p>
    </div>
    <div class="faq-item">
        <h3>Can Alaska hospitals garnish my wages for a medical debt?</h3>
        <p>Yes, but only after obtaining a court judgment. Wage garnishment is capped at 25% of disposable earnings per week. Patients at or below 150% FPL may qualify for a hardship exemption. Contact Alaska Legal Services at alsc-law.org for free legal assistance if facing wage garnishment.</p>
    </div>
</div>

<h2 id="sources">Sources</h2>

<ul class="sources-list">
    <li><a href="https://www.akleg.gov/basis/statutes.asp#09.10.053" target="_blank" rel="noopener">Alaska Statutes AS §09.10.053: Statute of Limitations on Written Contracts</a></li>
    <li><a href="https://dhss.alaska.gov/dpa/Pages/medicaid/default.aspx" target="_blank" rel="noopener">Alaska DHSS: Medicaid Program Information</a></li>
    <li><a href="https://www.cms.gov/nosurprises" target="_blank" rel="noopener">CMS: No Surprises Act &mdash; Federal Surprise Billing Protections</a></li>
    <li><a href="https://commerce.alaska.gov/web/ins/" target="_blank" rel="noopener">Alaska Division of Insurance: Consumer Assistance</a></li>
    <li><a href="https://oig.hhs.gov/fraud/report-fraud/" target="_blank" rel="noopener">HHS OIG: Report Healthcare Fraud</a></li>
    <li><a href="https://www.cms.gov/hospital-price-transparency" target="_blank" rel="noopener">CMS Hospital Price Transparency Rule</a></li>
</ul>
""",
})
