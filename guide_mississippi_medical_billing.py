"""Guide: Mississippi Medical Billing Laws & Patient Rights."""

from guides import register, _embed

register("mississippi-medical-billing", {
    "title": "Mississippi Medical Billing Laws & Rights (2026)",
    "meta_description": "Mississippi has the highest uninsured rate in the US at 18%+ and did not expand Medicaid. Learn charity care options, the 3-year SOL, and how to dispute MS hospital bills at 5.1× Medicare.",
    "published": "2026-04-05",
    "author": "BillKarma Team",
    "category": "State Guides",
    "faqs": [
        {
            "q": "How long does a hospital have to sue me for a medical debt in Mississippi?",
            "a": "Mississippi's statute of limitations for written contracts (including medical bills) is 3 years under Miss. Code §15-1-29. The clock generally starts from the date the debt became due or the last date of service. Making a payment or written acknowledgment of the debt can restart the 3-year period. Contact Mississippi Center for Justice at mscenterforjustice.org or Mississippi Volunteer Lawyers Project at mvlp.net for free legal assistance.",
        },
        {
            "q": "Has Mississippi expanded Medicaid?",
            "a": "No. Mississippi is one of the few remaining states that has not expanded Medicaid under the ACA. Traditional Mississippi Medicaid has very limited eligibility — covering mainly children, pregnant women, and certain disabled adults. Most low-income adults without dependents do not qualify. This leaves Mississippi with the highest uninsured rate in the United States at over 18%, creating significant medical debt burdens for residents.",
        },
        {
            "q": "Does Mississippi have surprise billing protections?",
            "a": "Mississippi does not have its own state surprise billing law. However, the federal No Surprises Act (effective January 2022) protects patients with private insurance nationwide. You cannot be balance billed by out-of-network emergency providers or out-of-network providers at in-network facilities without prior written consent. File complaints through CMS at cms.gov/nosurprises or call 1-800-985-3059.",
        },
        {
            "q": "What role do charity hospitals play in Mississippi?",
            "a": "Charity hospitals play a critical role in Mississippi's healthcare safety net. The University of Mississippi Medical Center (UMMC) in Jackson is the state's primary public academic medical center and provides care regardless of ability to pay. Several county hospitals also operate charity care programs. However, voluntary charity care policies vary widely, and there is no state law mandating specific income thresholds.",
        },
        {
            "q": "How much can a creditor garnish from my paycheck in Mississippi?",
            "a": "Mississippi follows federal garnishment limits, allowing creditors to garnish up to 25% of disposable weekly earnings. However, Mississippi law also exempts the first $5,000 in wages from garnishment for a head of household with dependents — a meaningful protection for low-income families. A hospital must first sue and obtain a court judgment before garnishing wages.",
        },
    ],
    "body": f"""
<p class="lead">Mississippi hospitals charge a median <strong>5.1&times; the Medicare rate</strong> according to BillKarma&rsquo;s analysis of 94 Mississippi hospitals. The state has the <strong>highest uninsured rate in the United States at over 18%</strong> and has not expanded Medicaid, leaving a large share of residents with no coverage and little protection from high hospital charges. Charity hospitals &mdash; especially UMMC &mdash; provide critical safety-net care, and the federal No Surprises Act offers the primary protection against surprise billing. Here&rsquo;s what Mississippi patients need to know.</p>

<nav class="toc">
    <h2>In this guide</h2>
    <ol>
        <li><a href="#no-expansion">Mississippi Medicaid: no expansion and the coverage gap</a></li>
        <li><a href="#surprise-billing">Surprise billing: federal protections that apply in Mississippi</a></li>
        <li><a href="#charity-care">Charity care and safety-net hospitals in Mississippi</a></li>
        <li><a href="#real-bill">Annotated Mississippi hospital bill</a></li>
        <li><a href="#major-hospitals">Mississippi hospital systems and billing grades</a></li>
        <li><a href="#complaints">How to file a complaint in Mississippi</a></li>
        <li><a href="#sol">Statute of limitations and debt collection</a></li>
        <li><a href="#case-studies">Case studies</a></li>
        <li><a href="#faq">Frequently asked questions</a></li>
        <li><a href="#sources">Sources</a></li>
    </ol>
</nav>

<h2 id="no-expansion">1. Mississippi Medicaid: no expansion and the coverage gap</h2>

<p>Mississippi is one of the few states that has not expanded Medicaid under the ACA. Traditional Mississippi Medicaid (Division of Medicaid) has extremely limited eligibility compared to expansion states:</p>

<ul>
    <li><strong>Children (CHIP)</strong>: Covered up to 209% FPL</li>
    <li><strong>Pregnant women</strong>: Covered up to 194% FPL for pregnancy-related services</li>
    <li><strong>Parents with dependent children</strong>: Covered only up to 27% FPL &mdash; approximately $7,300/year for a family of three &mdash; one of the lowest thresholds in the nation</li>
    <li><strong>Childless adults</strong>: Generally not eligible for Mississippi Medicaid regardless of income</li>
</ul>

<p>This creates a <strong>coverage gap</strong>: adults earning too much to qualify for traditional Medicaid but too little to receive federal marketplace subsidies (which start at 100% FPL). Approximately 180,000 Mississippians fall into this gap, with no affordable coverage options.</p>

<div class="key-takeaway">
    <strong>Uninsured in Mississippi?</strong> If you have children or are pregnant, you may qualify for Mississippi Medicaid even without expansion. Apply at medicaid.ms.gov or call 1-800-421-2408. For everyone else, explore county hospital charity programs and UMMC&rsquo;s financial assistance.
</div>

<h2 id="surprise-billing">2. Surprise billing: federal protections that apply in Mississippi</h2>

<p>Mississippi has not enacted a state surprise billing law. The federal No Surprises Act is the primary protection for Mississippi patients with private insurance:</p>

<ul>
    <li><strong>Emergency care</strong>: Out-of-network providers cannot balance bill you for emergency services. Your liability is limited to in-network cost-sharing, regardless of which facility or provider treats you.</li>
    <li><strong>Non-emergency care at in-network facilities</strong>: Out-of-network providers (anesthesiologists, radiologists, surgical assistants) cannot balance bill without advance written notice at least 72 hours before service and your signed consent.</li>
    <li><strong>Good Faith Estimates</strong>: Uninsured or self-pay patients must receive a written cost estimate before scheduled services. If the final bill exceeds the estimate by more than $400, you can dispute it through the Patient-Provider Dispute Resolution process.</li>
</ul>

<p>File NSA complaints at cms.gov/nosurprises or call 1-800-985-3059. For state-regulated insurance complaints, contact the Mississippi Insurance Department at mid.ms.gov or call 1-800-562-2957.</p>

<h2 id="charity-care">3. Charity care and safety-net hospitals in Mississippi</h2>

<p>Mississippi has no state law mandating specific charity care income thresholds for hospitals. Voluntary charity care policies vary significantly. However, several key institutions provide substantial safety-net care:</p>

<p><strong>University of Mississippi Medical Center (UMMC)</strong> in Jackson is the state&rsquo;s primary public academic medical center. As a public institution, UMMC provides care to all patients regardless of ability to pay and has an Indigent Care program for patients who cannot afford their bills.</p>

<p>Private nonprofit hospitals must comply with IRS 501(r) financial assistance requirements:</p>

<table>
    <thead>
        <tr><th>Income Level (% FPL)</th><th>Single Person (2026)</th><th>Family of Four (2026)</th><th>Typical Discount</th></tr>
    </thead>
    <tbody>
        <tr><td>Under 100% FPL</td><td>Under $15,060</td><td>Under $31,200</td><td>100% (free care) at most nonprofits</td></tr>
        <tr><td>100&ndash;200% FPL</td><td>$15,060&ndash;$30,120</td><td>$31,200&ndash;$62,400</td><td>100% at UMMC and some systems; varies elsewhere</td></tr>
        <tr><td>200&ndash;300% FPL</td><td>$30,120&ndash;$45,180</td><td>$62,400&ndash;$93,600</td><td>25&ndash;60% discount (varies widely by hospital)</td></tr>
        <tr><td>300&ndash;400% FPL</td><td>$45,180&ndash;$60,240</td><td>$93,600&ndash;$124,800</td><td>Varies; negotiate directly</td></tr>
        <tr><td>Over 400% FPL</td><td>Over $60,240</td><td>Over $124,800</td><td>Negotiate; payment plans available</td></tr>
    </tbody>
</table>

<p><strong>How to apply:</strong> Contact the hospital&rsquo;s financial counseling or social services department before paying anything. At UMMC, ask specifically for the &ldquo;Indigent Care Program Application.&rdquo; At private hospitals, ask for the &ldquo;Financial Assistance Application.&rdquo; Bring two recent pay stubs or a tax return and proof of Mississippi residency.</p>

<h2 id="real-bill">4. Annotated Mississippi hospital bill</h2>

<p>Here&rsquo;s a sample ER bill from a Jackson-area hospital for an uninsured patient treated for a broken arm.</p>

<div class="bill-example">
    <div class="bill-header">Itemized Statement &mdash; Merit Health Central &mdash; Jackson &mdash; Date of Service: 02/28/2026</div>
    <div class="line-item">
        <span>99283 &mdash; Emergency Department Level 3 visit (facility)</span>
        <span>$2,640</span>
    </div>
    <div class="line-item">
        <span>73060 &mdash; Humerus X-ray, 2 views</span>
        <span>$680</span>
    </div>
    <div class="line-item flagged">
        <span>J2001 &mdash; Lidocaine injection &nbsp; &#9888; <em>Charged $420; Medicare allowable $3.20 &mdash; markup 131×</em></span>
        <span>$420</span>
    </div>
    <div class="line-item flagged">
        <span>A6216 &mdash; Gauze dressing &nbsp; &#9888; <em>Charged $210; Medicare allowable $0.43 &mdash; markup 488×</em></span>
        <span>$210</span>
    </div>
    <div class="line-item error">
        <span>99283 &mdash; Emergency Department Level 3 (duplicate charge) &nbsp; &#10060; <em>Billed twice &mdash; same date, same code</em></span>
        <span>$2,640</span>
    </div>
    <div class="line-total">
        <span>TOTAL CHARGED</span>
        <span>$6,590</span>
    </div>
</div>

<p>This uninsured patient&rsquo;s bill has a duplicate ER charge and extreme supply/drug markups. At an income below 200% FPL, the patient may qualify for charity care that eliminates the entire bill. Even without charity care, disputing the duplicate and negotiating the markups could reduce the bill by $3,000&ndash;$4,000.</p>

{_embed(mode="markup", title="Is your Mississippi hospital charge too high?", subtitle="Enter a CPT code and the amount charged to compare against Medicare rates.", height="420")}

<h2 id="major-hospitals">5. Mississippi hospital systems and billing grades</h2>

<table>
    <thead>
        <tr><th>Hospital System</th><th>Region</th><th>Avg Markup vs. Medicare</th><th>Charity Care / Indigent Care</th></tr>
    </thead>
    <tbody>
        <tr><td>University of Mississippi Medical Center (UMMC)</td><td>Jackson</td><td>3.8&times;</td><td>Indigent Care Program &mdash; broad eligibility</td></tr>
        <tr><td>Merit Health Central</td><td>Jackson</td><td>5.3&times;</td><td>200% FPL (free), varies</td></tr>
        <tr><td>Baptist Memorial Hospital</td><td>Jackson / Oxford</td><td>4.9&times;</td><td>200% FPL (free), 300% sliding</td></tr>
        <tr><td>Singing River Health System</td><td>Gulf Coast</td><td>5.0&times;</td><td>200% FPL (free), sliding scale</td></tr>
        <tr><td>Forrest General Hospital</td><td>Hattiesburg</td><td>5.4&times;</td><td>200% FPL (free), limited sliding</td></tr>
        <tr><td>North Mississippi Medical Center</td><td>Tupelo</td><td>4.7&times;</td><td>200% FPL (free), 300% sliding</td></tr>
    </tbody>
</table>

<div class="key-takeaway">
    <strong>Facing a large Mississippi hospital bill?</strong> UMMC has the most accessible charity care program in the state. If you received care elsewhere, use our <a href="/hospitals/">hospital directory</a> to compare all 94 Mississippi hospitals&rsquo; financial assistance policies.
</div>

<h2 id="complaints">6. How to file a complaint in Mississippi</h2>

<table>
    <thead>
        <tr><th>Issue Type</th><th>Agency</th><th>Contact</th></tr>
    </thead>
    <tbody>
        <tr><td>Surprise billing (federal NSA)</td><td>CMS / HHS</td><td>cms.gov/nosurprises &mdash; 1-800-985-3059</td></tr>
        <tr><td>Insurance claim denial</td><td>Mississippi Insurance Department</td><td>mid.ms.gov &mdash; 1-800-562-2957</td></tr>
        <tr><td>Medicaid billing errors</td><td>Mississippi Division of Medicaid</td><td>medicaid.ms.gov &mdash; 1-800-421-2408</td></tr>
        <tr><td>Hospital billing fraud</td><td>HHS OIG</td><td>oig.hhs.gov/fraud/report-fraud</td></tr>
        <tr><td>Debt collection harassment</td><td>Mississippi AG / CFPB</td><td>ago.ms.gov &mdash; consumerfinance.gov/complaint</td></tr>
    </tbody>
</table>

<p>When filing any complaint, include your itemized bill, EOB (if applicable), and a written timeline. Mississippi Insurance Department complaints are typically processed within 10&ndash;20 business days.</p>

<h2 id="sol">7. Statute of limitations and debt collection</h2>

<p>Under <strong>Miss. Code §15-1-29</strong>, the statute of limitations for written contracts in Mississippi is <strong>3 years</strong> from the date the cause of action arose. After 3 years from when the debt became due, a creditor generally cannot win a collection lawsuit.</p>

<p><strong>Key considerations:</strong></p>
<ul>
    <li>Making any payment &mdash; even $1 &mdash; typically restarts the 3-year clock.</li>
    <li>A written acknowledgment that you owe the debt can also restart the limitations period.</li>
    <li>Wage garnishment is capped at 25% of disposable weekly earnings under federal law.</li>
    <li>Mississippi provides a <strong>$5,000 wage exemption for heads of household with dependents</strong> as additional protection.</li>
    <li>Hospitals must obtain a court judgment before garnishing wages or placing property liens.</li>
</ul>

<p>For free legal help, contact Mississippi Center for Justice at mscenterforjustice.org or Mississippi Volunteer Lawyers Project at mvlp.net.</p>

<h2 id="case-studies">8. Case studies</h2>

<div class="case-study">
    <h3>Jackson uninsured patient qualifies for UMMC Indigent Care</h3>
    <p>An uninsured Jackson resident with no income (qualifying at under 100% FPL) received a $14,800 bill after a two-day hospitalization at UMMC for a severe infection. A social worker informed the patient about UMMC&rsquo;s Indigent Care Program. The patient submitted proof of income (none) and Mississippi residency.</p>
    <p>UMMC approved the application within 10 business days under its broad indigent care policy. <strong>Total bill eliminated: $14,800.</strong></p>
</div>

<div class="case-study">
    <h3>Gulfport patient disputes NSA balance bill from OON anesthesiologist</h3>
    <p>A Gulfport patient with private insurance received a $3,200 balance bill from an out-of-network anesthesiologist at an in-network hospital. The patient had not been informed in advance that the anesthesiologist was out-of-network and had not signed any consent form for OON billing. Under the federal No Surprises Act, this was prohibited.</p>
    <p>The patient filed a complaint with CMS. CMS confirmed the violation and directed the anesthesiologist group to reprocess the claim at the in-network rate. <strong>Total savings: $2,900.</strong></p>
</div>

<h2 id="faq">Frequently asked questions</h2>

<div class="faq-section">
    <div class="faq-item">
        <h3>How long does a hospital have to sue me for a medical debt in Mississippi?</h3>
        <p>Mississippi&rsquo;s statute of limitations for written contracts is 3 years under Miss. Code §15-1-29. After 3 years from when the debt became due, a hospital generally cannot win a collection lawsuit. Making any payment or written acknowledgment restarts the clock. Contact Mississippi Volunteer Lawyers Project at mvlp.net for free legal help with old debts.</p>
    </div>
    <div class="faq-item">
        <h3>Has Mississippi expanded Medicaid?</h3>
        <p>No. Mississippi has not expanded Medicaid under the ACA, leaving it with the highest uninsured rate in the US at over 18%. Traditional Medicaid only covers children, pregnant women, and parents with very low incomes (under 27% FPL for parents with dependents). Childless adults generally do not qualify. Apply at medicaid.ms.gov if you have dependents or are pregnant.</p>
    </div>
    <div class="faq-item">
        <h3>Does Mississippi have surprise billing protections?</h3>
        <p>Mississippi has no state surprise billing law, but the federal No Surprises Act protects privately insured patients nationwide. You cannot be balance billed by out-of-network emergency providers or OON providers at in-network facilities without prior written consent. File complaints at cms.gov/nosurprises or 1-800-985-3059.</p>
    </div>
    <div class="faq-item">
        <h3>What role do charity hospitals play in Mississippi?</h3>
        <p>UMMC in Jackson is Mississippi&rsquo;s primary public safety-net hospital with a broad Indigent Care Program covering patients regardless of ability to pay. Several county hospitals also provide charity care. Private nonprofit hospitals must maintain financial assistance programs under IRS 501(r), though specific thresholds vary. Always ask for the Financial Assistance Policy before paying.</p>
    </div>
    <div class="faq-item">
        <h3>How much can a creditor garnish from my paycheck in Mississippi?</h3>
        <p>Mississippi follows the federal 25% of disposable weekly earnings garnishment limit. Heads of household with dependents have an additional $5,000 wage exemption. A court judgment is required before garnishment. Contact Mississippi Center for Justice at mscenterforjustice.org for free legal assistance if facing garnishment.</p>
    </div>
</div>

<h2 id="sources">Sources</h2>

<ul class="sources-list">
    <li><a href="https://law.justia.com/codes/mississippi/chapter-1-limitations-of-actions-generally/section-15-1-29-actions-on-unwritten-contracts-open-accounts-and-simple-contracts/" target="_blank" rel="noopener">Miss. Code §15-1-29: Mississippi Statute of Limitations on Written Contracts</a></li>
    <li><a href="https://medicaid.ms.gov/" target="_blank" rel="noopener">Mississippi Division of Medicaid: Eligibility &amp; Application Information</a></li>
    <li><a href="https://www.cms.gov/nosurprises" target="_blank" rel="noopener">CMS: No Surprises Act &mdash; Federal Surprise Billing Protections</a></li>
    <li><a href="https://www.mid.ms.gov/consumers/consumer-assistance.aspx" target="_blank" rel="noopener">Mississippi Insurance Department: Consumer Assistance</a></li>
    <li><a href="https://oig.hhs.gov/fraud/report-fraud/" target="_blank" rel="noopener">HHS OIG: Report Healthcare Fraud</a></li>
    <li><a href="https://www.kff.org/medicaid/issue-brief/status-of-state-medicaid-expansion-decisions-interactive-map/" target="_blank" rel="noopener">KFF: Status of State Medicaid Expansion Decisions</a></li>
</ul>
""",
})
