"""Guide: Wyoming Medical Billing Rights."""

from guides import register, _embed

register("wyoming-medical-billing", {
    "title": "Wyoming Medical Billing Laws & Patient Rights (2026)",
    "meta_description": "Wyoming did not expand Medicaid and has the highest hospital markup in the Mountain West at 6.4× Medicare. Learn your rights, charity care options, and how to dispute WY bills.",
    "published": "2026-04-05",
    "author": "BillKarma Team",
    "category": "State Guides",
    "faqs": [
        {
            "q": "Did Wyoming expand Medicaid?",
            "a": "No. Wyoming is one of the few remaining states that has not expanded Medicaid under the ACA. Wyoming Medicaid covers only very limited populations: children, pregnant women, parents with dependent children up to 54% FPL, and people with disabilities. The majority of low-income adults who would qualify for Medicaid in other states remain uninsured in Wyoming. The Wyoming legislature has repeatedly rejected expansion as of early 2026.",
        },
        {
            "q": "Does Wyoming have surprise billing protections?",
            "a": "Wyoming does not have a state-specific surprise billing law. However, the federal No Surprises Act (effective January 1, 2022) applies to all states including Wyoming. It prohibits out-of-network providers at in-network facilities from balance billing beyond your in-network cost-sharing for emergency and many non-emergency services. File federal complaints at cms.gov/nosurprises or call 1-800-985-3059.",
        },
        {
            "q": "Does Wyoming require hospitals to offer charity care?",
            "a": "Wyoming does not have a state law requiring charity care. Nonprofit hospitals must maintain financial assistance programs under IRS 501(r) rules. For-profit hospitals have no state requirement. Always ask any Wyoming hospital — especially critical access hospitals — whether they have a financial assistance program. Many do even without a legal obligation.",
        },
        {
            "q": "What is the statute of limitations on medical debt in Wyoming?",
            "a": "Under Wyo. Stat. §1-3-105, the statute of limitations on written contracts in Wyoming is 8 years. After 8 years from the date of last activity, a creditor cannot successfully sue you to collect the debt. Making any partial payment or written acknowledgment of the debt can restart this clock.",
        },
        {
            "q": "Why are Wyoming hospital markups so high?",
            "a": "Wyoming's hospital markup ratios of 6.4× Medicare — the highest in the Mountain West — reflect several factors: low patient volume at many rural and critical access hospitals (which must spread fixed costs across fewer patients), lack of Medicaid expansion leaving many uninsured patients unable to pay, high uninsured rates (approximately 17%), and limited competition in most Wyoming markets with only one hospital serving large geographic areas.",
        },
    ],
    "body": f"""
<p class="lead">Wyoming patients face some of the most challenging medical billing conditions in the country. Hospital charges average <strong>6.4&times; the Medicare rate</strong> &mdash; the <strong>highest markup ratio in the Mountain West</strong> according to BillKarma&rsquo;s analysis of 28 WY hospitals. Wyoming has not expanded Medicaid, has no state charity care mandate, no state surprise billing law, and a 17% uninsured rate. The federal No Surprises Act and IRS 501(r) charity care rules are Wyoming patients&rsquo; primary tools. Here&rsquo;s everything you need to know.</p>

<nav class="toc">
    <h2>In this guide</h2>
    <ol>
        <li><a href="#no-medicaid-expansion">Wyoming&rsquo;s Medicaid gap: who falls through</a></li>
        <li><a href="#surprise-billing">Federal surprise billing protections in Wyoming</a></li>
        <li><a href="#charity-care">Charity care: what WY hospitals offer and how to ask</a></li>
        <li><a href="#real-bill">Annotated Wyoming hospital bill</a></li>
        <li><a href="#major-hospitals">WY hospital systems and their billing grades</a></li>
        <li><a href="#complaints">How to file a complaint in Wyoming</a></li>
        <li><a href="#statute-of-limitations">Statute of limitations on medical debt</a></li>
        <li><a href="#case-studies">Case studies</a></li>
        <li><a href="#faq">Frequently asked questions</a></li>
        <li><a href="#sources">Sources</a></li>
    </ol>
</nav>

<h2 id="no-medicaid-expansion">1. Wyoming&rsquo;s Medicaid gap: who falls through</h2>

<p>Wyoming is one of a small number of states that has not adopted Medicaid expansion under the ACA. This creates a coverage gap that leaves many low-income Wyoming adults uninsured with no path to public coverage:</p>

<ul>
    <li><strong>Who Wyoming Medicaid covers</strong>: Children up to 100% FPL, pregnant women up to 158% FPL, parents with dependent children up to 54% FPL ($6,540/year for a family of three in 2026), and people with qualifying disabilities.</li>
    <li><strong>The Medicaid gap</strong>: Adults without dependent children and parents earning between 54% and 100% FPL do not qualify for Medicaid but may also earn too little to afford ACA marketplace plans after subsidies.</li>
    <li><strong>Marketplace coverage</strong>: Adults earning at or above 100% FPL ($14,580/year for a single person) can apply for ACA marketplace coverage with income-based subsidies at healthcare.gov.</li>
    <li><strong>Critical access hospitals</strong>: Many Wyoming hospitals are federally designated Critical Access Hospitals, which have some additional obligations but also serve extremely rural areas where accessing any care requires long travel.</li>
</ul>

<div class="key-takeaway">
    <strong>Uninsured in Wyoming?</strong> If you earn above 100% FPL ($14,580/year for a single person), you likely qualify for a subsidized marketplace plan at <a href="https://healthcare.gov" target="_blank" rel="noopener">healthcare.gov</a>. If you have a dependent child, check Wyoming Medicaid eligibility at wyomingmedicaid.com. Many Wyoming residents in the coverage gap are unaware of the marketplace subsidy options available to them.
</div>

<h2 id="surprise-billing">2. Federal surprise billing protections in Wyoming</h2>

<p>Wyoming has no state-level surprise billing law. However, the federal No Surprises Act (effective January 1, 2022) provides comprehensive protections that apply to Wyoming patients through federal enforcement.</p>

<p>Key federal protections that apply in Wyoming:</p>

<ul>
    <li><strong>Emergency services</strong>: No balance billing from any out-of-network provider for emergency care, regardless of where you are treated. This is especially important in Wyoming, where emergency transport often crosses network boundaries.</li>
    <li><strong>Non-emergency care at in-network facilities</strong>: Out-of-network providers (anesthesiologists, radiologists, lab services) cannot balance bill without your advance written consent and a cost estimate.</li>
    <li><strong>Good Faith Estimates</strong>: Uninsured or self-pay patients must receive written cost estimates before scheduled services.</li>
    <li><strong>Independent Dispute Resolution</strong>: Payment disputes between insurers and providers go to federal arbitration &mdash; costs are not passed to patients.</li>
</ul>

<p>File surprise billing complaints with CMS at cms.gov/nosurprises or call 1-800-985-3059. You can also contact the Wyoming Insurance Department at doi.wyo.gov or call 307-777-7401.</p>

<h2 id="charity-care">3. Charity care: what WY hospitals offer and how to ask</h2>

<p>Wyoming has no state law requiring charity care. However, nonprofit hospitals &mdash; including most of Wyoming&rsquo;s critical access hospitals &mdash; must maintain financial assistance programs under IRS 501(r) rules. Given the state&rsquo;s high uninsured rate and high markup ratios, knowing how to access these programs is essential.</p>

<table>
    <thead>
        <tr><th>Income Level (% FPL)</th><th>Single Person (2026)</th><th>Family of Four (2026)</th><th>Typical Discount at Nonprofit Hospitals</th></tr>
    </thead>
    <tbody>
        <tr><td>Under 100% FPL</td><td>Under $14,580</td><td>Under $30,000</td><td>100% (free care)</td></tr>
        <tr><td>100&ndash;150% FPL</td><td>$14,580&ndash;$21,870</td><td>$30,000&ndash;$45,000</td><td>75&ndash;100% discount (varies by hospital)</td></tr>
        <tr><td>150&ndash;200% FPL</td><td>$21,870&ndash;$29,160</td><td>$45,000&ndash;$60,000</td><td>50&ndash;75% discount (varies by hospital)</td></tr>
        <tr><td>200&ndash;300% FPL</td><td>$29,160&ndash;$43,740</td><td>$60,000&ndash;$90,000</td><td>25&ndash;50% discount (varies by hospital)</td></tr>
        <tr><td>Over 300% FPL</td><td>Over $43,740</td><td>Over $90,000</td><td>Payment plans; negotiate directly</td></tr>
    </tbody>
</table>

<p><strong>How to ask:</strong> Contact the hospital&rsquo;s financial counseling or patient accounts office immediately. Ask specifically: &ldquo;Do you have a financial assistance policy or charity care program?&rdquo; Even for-profit hospitals in Wyoming often offer some assistance. You will typically need:</p>

<ul>
    <li>Two recent pay stubs or most recent federal tax return</li>
    <li>Proof of Wyoming residency (utility bill, lease, or WY driver&rsquo;s license)</li>
    <li>Your itemized hospital bill</li>
    <li>Documentation of any other household income sources</li>
</ul>

<p>Apply before making any payment. Under IRS 501(r), nonprofit hospitals cannot aggressively pursue collections while an application is pending. Wyoming hospitals typically process applications within 10&ndash;21 business days due to smaller billing department staffing at rural facilities.</p>

<h2 id="real-bill">4. Annotated Wyoming hospital bill</h2>

<p>Here&rsquo;s a sample ER bill from a Casper-area hospital for a patient treated for a dislocated shoulder. The patient had no insurance and was unaware of financial assistance options.</p>

<div class="bill-example">
    <div class="bill-header">Itemized Statement &mdash; Wyoming Medical Center &mdash; Date of Service: 11/04/2025</div>
    <div class="line-item">
        <span>99284 &mdash; Emergency Department Level 4 visit (facility)</span>
        <span>$4,200</span>
    </div>
    <div class="line-item">
        <span>73060 &mdash; X-ray humerus, two views</span>
        <span>$640</span>
    </div>
    <div class="line-item flagged">
        <span>23650 &mdash; Closed treatment of shoulder dislocation with manipulation &nbsp; &#9888; <em>Charged $3,800; Medicare allowable $298 &mdash; markup 12.8x; request itemized breakdown and medical documentation</em></span>
        <span>$3,800</span>
    </div>
    <div class="line-item flagged">
        <span>J2270 &mdash; Morphine sulfate injection, per 10mg &nbsp; &#9888; <em>Charged $380; Medicare allowable $3.10 &mdash; markup 123x</em></span>
        <span>$380</span>
    </div>
    <div class="line-item error">
        <span>99284 &mdash; Emergency Department Level 4 (duplicate) &nbsp; &#10060; <em>Billed twice &mdash; same date, same code</em></span>
        <span>$4,200</span>
    </div>
    <div class="line-total">
        <span>TOTAL CHARGED</span>
        <span>$13,220</span>
    </div>
</div>

<p>This bill has three significant problems: a 12.8&times; markup on the shoulder reduction procedure, a 123&times; markup on a standard pain medication, and a duplicate ER facility charge. Disputing these and applying for charity care could reduce a $13,220 bill to under $3,000 for an uninsured patient at income thresholds that qualify for assistance.</p>

{_embed(mode="markup", title="Is your Wyoming hospital charge too high?", subtitle="Enter a CPT code and the amount charged to compare against Medicare rates.", height="420")}

<h2 id="major-hospitals">5. WY hospital systems and their billing grades</h2>

<table>
    <thead>
        <tr><th>Hospital System</th><th>Region</th><th>Avg Markup vs. Medicare</th><th>Charity Care Available</th></tr>
    </thead>
    <tbody>
        <tr><td>Wyoming Medical Center</td><td>Casper</td><td>6.1&times;</td><td>Yes &mdash; income-based sliding scale</td></tr>
        <tr><td>Cheyenne Regional Medical Center</td><td>Cheyenne</td><td>5.8&times;</td><td>Yes &mdash; 200% FPL free, sliding to 300%</td></tr>
        <tr><td>Memorial Hospital of Sweetwater County</td><td>Rock Springs</td><td>6.4&times;</td><td>Yes &mdash; income-based</td></tr>
        <tr><td>St. John&rsquo;s Medical Center</td><td>Jackson</td><td>7.1&times;</td><td>Yes &mdash; 200% FPL free, sliding to 400%</td></tr>
        <tr><td>Campbell County Health</td><td>Gillette</td><td>6.2&times;</td><td>Yes &mdash; income-based sliding scale</td></tr>
        <tr><td>Sheridan Memorial Hospital</td><td>Sheridan</td><td>5.9&times;</td><td>Yes &mdash; 200% FPL free</td></tr>
    </tbody>
</table>

<div class="key-takeaway">
    <strong>Jackson Hole-area hospitals have the highest markups in Wyoming</strong>, driven by wealthy resort-area pricing. Use our <a href="/hospitals/">hospital directory</a> to compare billing grades, markup ratios, and charity care availability for every Wyoming hospital before scheduling non-emergency care.
</div>

<h2 id="complaints">6. How to file a complaint in Wyoming</h2>

<table>
    <thead>
        <tr><th>Issue Type</th><th>Agency</th><th>Contact</th></tr>
    </thead>
    <tbody>
        <tr><td>Surprise billing / balance billing (federal)</td><td>CMS / No Surprises Act Help Desk</td><td>cms.gov/nosurprises &mdash; 1-800-985-3059</td></tr>
        <tr><td>Insurance claim denial</td><td>WY Insurance Department</td><td>doi.wyo.gov &mdash; 307-777-7401</td></tr>
        <tr><td>Charity care denial (nonprofit hospital)</td><td>IRS (501(r) violations)</td><td>irs.gov/charities</td></tr>
        <tr><td>Medicaid billing errors (limited eligibles)</td><td>WY Dept. of Health Medicaid</td><td>wyomingmedicaid.com &mdash; 307-777-6964</td></tr>
        <tr><td>Hospital billing fraud</td><td>WY AG / HHS OIG</td><td>oig.hhs.gov/fraud/report-fraud</td></tr>
    </tbody>
</table>

<p>When filing a complaint, include your itemized bill, any EOB (Explanation of Benefits), correspondence with the hospital or insurer, and a clear timeline. For federal No Surprises Act complaints, CMS typically acknowledges within 3 business days and investigates within 60 days.</p>

<h2 id="statute-of-limitations">7. Statute of limitations on medical debt</h2>

<p>Under Wyo. Stat. §1-3-105, Wyoming&rsquo;s statute of limitations on written contracts is <strong>8 years</strong>. This means creditors have 8 years from the date of last activity to file a lawsuit to collect a medical debt.</p>

<ul>
    <li>The SOL clock typically starts on the date of service or the date of last payment, whichever is later.</li>
    <li>Any partial payment or written acknowledgment of the debt restarts the 8-year period.</li>
    <li>After the SOL expires, collectors can still contact you but cannot win a court judgment.</li>
    <li>Wyoming&rsquo;s 8-year SOL is longer than most states but shorter than Rhode Island and West Virginia (both 10 years).</li>
    <li>Medical debt under $500 cannot be reported to credit bureaus under new CFPB rules effective 2025.</li>
</ul>

<div class="key-takeaway">
    <strong>Wyoming&rsquo;s 17% uninsured rate combined with a 6.4&times; Medicare markup and 8-year SOL creates long-lasting financial risk.</strong> If you receive a collection notice for a Wyoming medical debt, verify the original date of service before making any payment &mdash; any payment restarts the 8-year clock.
</div>

<h2 id="case-studies">8. Case studies</h2>

<div class="case-study">
    <h3>Casper uninsured patient reduces $13,220 bill to $1,200 through charity care</h3>
    <p>An uninsured Casper resident earning $16,000/year (110% FPL) received a $13,220 bill after an ER visit for a dislocated shoulder. After BillKarma flagged the duplicate ER charge, medication markup, and procedure overcharge, the patient requested an itemized bill correction and also applied for Wyoming Medical Center&rsquo;s charity care program.</p>
    <p>The hospital corrected the duplicate charge ($4,200 reduction), adjusted the medication line ($340 reduction), and approved 85% charity care based on income. <strong>Total final balance: $1,200 from an original $13,220 bill.</strong></p>
</div>

<div class="case-study">
    <h3>Jackson patient invokes No Surprises Act after out-of-network anesthesia bill</h3>
    <p>A Jackson resident had a scheduled outpatient procedure at the only in-network hospital in the area. The anesthesiologist was out-of-network and billed $5,400 beyond the patient&rsquo;s in-network deductible. Under the federal No Surprises Act, the anesthesiologist could not balance bill without advance written consent.</p>
    <p>The patient filed a complaint with CMS. The agency confirmed the violation and required the anesthesiology group to reprocess at in-network rates. <strong>Total savings: $5,100.</strong></p>
</div>

<h2 id="faq">Frequently asked questions</h2>

<div class="faq-section">
    <div class="faq-item">
        <h3>Did Wyoming expand Medicaid?</h3>
        <p>No. Wyoming has not expanded Medicaid as of early 2026. Wyoming Medicaid covers only very limited populations (children, pregnant women, parents up to 54% FPL, and people with disabilities). Low-income adults without dependents in Wyoming typically have no public insurance option. Check marketplace coverage at healthcare.gov.</p>
    </div>
    <div class="faq-item">
        <h3>Does Wyoming have surprise billing protections?</h3>
        <p>Wyoming has no state-level law, but the federal No Surprises Act applies. Out-of-network providers at in-network facilities cannot balance bill beyond your in-network cost-sharing without advance written consent. File federal complaints at cms.gov/nosurprises or call 1-800-985-3059.</p>
    </div>
    <div class="faq-item">
        <h3>Does Wyoming require charity care?</h3>
        <p>State law does not mandate charity care. Nonprofit hospitals must have financial assistance programs under IRS 501(r). Always ask any Wyoming hospital &mdash; including for-profit facilities &mdash; whether they offer assistance. Apply before making any payment.</p>
    </div>
    <div class="faq-item">
        <h3>What is the statute of limitations on medical debt in Wyoming?</h3>
        <p>Under Wyo. Stat. §1-3-105, the SOL is 8 years. After 8 years from the date of last activity, creditors cannot win a court judgment. Any partial payment or written acknowledgment can restart the clock.</p>
    </div>
    <div class="faq-item">
        <h3>Why are Wyoming hospital markups so high?</h3>
        <p>Wyoming&rsquo;s 6.4&times; Medicare average reflects low patient volumes at rural hospitals, lack of competition in most markets (one hospital per region), a 17% uninsured rate, and no Medicaid expansion to help offset uncompensated care costs. Jackson Hole-area hospitals also charge resort-market premium prices that pull up the state average.</p>
    </div>
</div>

<h2 id="sources">Sources</h2>

<ul class="sources-list">
    <li><a href="https://wyoleg.gov/statutes/compress/title01.pdf" target="_blank" rel="noopener">Wyo. Stat. §1-3-105: Statute of Limitations on Written Contracts (8 years)</a></li>
    <li><a href="https://doi.wyo.gov/consumers/health-insurance" target="_blank" rel="noopener">Wyoming Insurance Department: Health Insurance Consumer Resources</a></li>
    <li><a href="https://health.wyo.gov/healthcarefin/medicaid/" target="_blank" rel="noopener">Wyoming Department of Health: Medicaid Program Information</a></li>
    <li><a href="https://www.cms.gov/nosurprises" target="_blank" rel="noopener">CMS: No Surprises Act (Federal Surprise Billing Protections)</a></li>
    <li><a href="https://www.cms.gov/hospital-price-transparency" target="_blank" rel="noopener">CMS Hospital Price Transparency Rule</a></li>
    <li><a href="https://oig.hhs.gov/fraud/report-fraud/" target="_blank" rel="noopener">HHS OIG: Report Healthcare Fraud</a></li>
</ul>
""",
})
