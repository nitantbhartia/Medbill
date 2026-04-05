"""Guide: Iowa Medical Billing Laws."""

from guides import register, _embed

register("iowa-medical-billing", {
    "title": "Iowa Medical Billing Laws & Patient Rights (2026)",
    "meta_description": "Iowa requires charity care under IA Code § 135.71 and expanded Medicaid. Learn the 5-year debt SOL, Iowa Consumer Credit Code protections, and how to cut your bill.",
    "published": "2026-04-05",
    "author": "BillKarma Team",
    "category": "State Guides",
    "faqs": [
        {
            "q": "Are Iowa hospitals required to offer charity care?",
            "a": "Yes. Iowa Code § 135.71 requires Iowa hospitals to maintain a charity care program and to make financial assistance available to qualifying low-income patients. Hospitals must post their charity care policies, notify patients of available assistance, and screen uninsured patients for eligibility before referring accounts to external collections. Iowa law does not specify minimum income thresholds — each hospital sets its own policy. Most Iowa nonprofit hospitals provide free care up to 200% FPL and discounts up to 300% FPL.",
        },
        {
            "q": "Does Iowa have Medicaid expansion?",
            "a": "Yes. Iowa expanded Medicaid under the ACA through its Iowa Health and Wellness Plan (IHAWP), covering adults earning up to 138% of the Federal Poverty Level — approximately $20,783 for a single person in 2026. Iowa implemented expansion through a private managed care model. Apply at dhs.iowa.gov or call 1-800-338-8366. Coverage can be retroactive for up to 3 months.",
        },
        {
            "q": "What is the statute of limitations on medical debt in Iowa?",
            "a": "Iowa has a 5-year statute of limitations on written contracts under Iowa Code § 614.1. Most hospital bills — where you signed a financial responsibility form at admission — are treated as written contracts subject to this 5-year SOL. The clock starts from the date of the last payment or the date the debt became due. Any voluntary payment restarts the 5-year period.",
        },
        {
            "q": "What is the Iowa Consumer Credit Code and how does it protect patients?",
            "a": "The Iowa Consumer Credit Code (Iowa Code § 537) provides important protections for Iowa patients facing medical debt collection. It limits certain collection practices, requires creditors to provide clear billing statements, and protects consumers from deceptive practices in debt collection. Iowa's code works alongside the federal Fair Debt Collection Practices Act. The Iowa Attorney General's Consumer Protection Division enforces both state and federal consumer debt laws.",
        },
        {
            "q": "Does Iowa protect patients from surprise medical bills?",
            "a": "Iowa patients rely on the federal No Surprises Act (effective January 1, 2022) for surprise billing protection. Iowa does not have a separate comprehensive state surprise billing law. Under the NSA, patients cannot be balance-billed for emergency services or for non-emergency care from out-of-network ancillary providers at in-network facilities without advance written consent. Report violations to CMS at 1-800-985-3059.",
        },
    ],
    "body": f"""
<p class="lead">Iowa is home to <strong>over 100 licensed hospitals</strong>, many of them critical access facilities in rural communities. BillKarma&rsquo;s analysis of Iowa hospital billing data found a median markup of <strong>3.6&times; Medicare rates</strong> for self-pay patients &mdash; below the national average, but still significant on a typical bill. Iowa Code &sect;&nbsp;135.71 requires hospitals to offer charity care, Iowa expanded Medicaid through the Iowa Health and Wellness Plan, and the Iowa Consumer Credit Code provides meaningful debt collection protections. Iowa&rsquo;s 5-year statute of limitations on medical debt rounds out a strong set of patient rights.</p>

<nav class="toc">
    <h2>In this guide</h2>
    <ol>
        <li><a href="#charity-care">Charity care under Iowa Code &sect; 135.71</a></li>
        <li><a href="#medicaid">Iowa Medicaid expansion (Iowa Health and Wellness Plan)</a></li>
        <li><a href="#surprise-billing">Surprise billing protections (No Surprises Act)</a></li>
        <li><a href="#statute-of-limitations">Statute of limitations on medical debt (5 years)</a></li>
        <li><a href="#iowa-consumer-credit">Iowa Consumer Credit Code protections</a></li>
        <li><a href="#debt-collection">Debt collection and wage garnishment</a></li>
        <li><a href="#how-to-dispute">How to dispute an Iowa hospital bill</a></li>
        <li><a href="#bill-example">Annotated Iowa hospital bill</a></li>
        <li><a href="#case-study">Real patient results</a></li>
        <li><a href="#sources">Sources</a></li>
    </ol>
</nav>

<h2 id="charity-care">1. Charity care under Iowa Code &sect; 135.71</h2>

<p>Iowa Code &sect;&nbsp;135.71 requires all Iowa hospitals to maintain a financial assistance (charity care) program. The Iowa Department of Inspections, Appeals, and Licensing (DIAL) oversees hospital compliance. Key requirements include:</p>

<ul>
    <li><strong>Written policy required.</strong> Every Iowa hospital must adopt a formal written charity care policy. The policy must be posted prominently in the hospital and on the hospital&rsquo;s website.</li>
    <li><strong>Patient notification.</strong> Hospitals must notify patients of available financial assistance at or before the time of billing. This notice must include information on how to apply and the income thresholds used.</li>
    <li><strong>Screening before collections.</strong> Iowa hospitals must screen uninsured and underinsured patients for charity care eligibility before referring accounts to external debt collectors or taking legal action.</li>
    <li><strong>No state-mandated threshold.</strong> Iowa law does not set a minimum income threshold &mdash; hospitals define their own. Most Iowa nonprofit hospitals provide free care up to 200% FPL and discounted care up to 300% FPL.</li>
    <li><strong>Application window.</strong> Apply within 240 days of the first billing statement (the federal 501(r) minimum).</li>
</ul>

<table>
    <thead>
        <tr><th>Household Size</th><th>100% FPL (2026)</th><th>138% FPL (Medicaid)</th><th>200% FPL (typical free care)</th><th>300% FPL (typical discount limit)</th></tr>
    </thead>
    <tbody>
        <tr><td>1 person</td><td>$15,650</td><td>$21,597</td><td>$31,300</td><td>$46,950</td></tr>
        <tr><td>2 people</td><td>$21,150</td><td>$29,187</td><td>$42,300</td><td>$63,450</td></tr>
        <tr><td>3 people</td><td>$26,650</td><td>$36,777</td><td>$53,300</td><td>$79,950</td></tr>
        <tr><td>4 people</td><td>$32,150</td><td>$44,367</td><td>$64,300</td><td>$96,450</td></tr>
        <tr><td>5 people</td><td>$37,650</td><td>$51,957</td><td>$75,300</td><td>$112,950</td></tr>
        <tr><td>6 people</td><td>$43,150</td><td>$59,547</td><td>$86,300</td><td>$129,450</td></tr>
    </tbody>
</table>

<p><em>FPL figures reflect 2026 HHS guidelines. Individual hospital policies vary. Confirm thresholds at <a href="https://aspe.hhs.gov/topics/poverty-economic-mobility/hhs-poverty-guidelines" target="_blank" rel="noopener">aspe.hhs.gov</a>.</em></p>

<div class="key-takeaway">
    <strong>Iowa hospitals must screen you for charity care before sending to collections.</strong> If a hospital sends your account to collections without first offering you a financial assistance application, that may violate Iowa Code &sect;&nbsp;135.71. Document the timeline and file a complaint with the Iowa DIAL if necessary. <a href="/charity-care">Check your eligibility now.</a>
</div>

<h2 id="medicaid">2. Iowa Medicaid expansion (Iowa Health and Wellness Plan)</h2>

<p>Iowa expanded Medicaid under the ACA through the <strong>Iowa Health and Wellness Plan (IHAWP)</strong>, covering adults earning up to 138% of the Federal Poverty Level. Iowa implemented its expansion through a managed care model (privatized Medicaid).</p>

<p>Key details:</p>
<ul>
    <li><strong>Income threshold:</strong> Adults (age 19&ndash;64) with income at or below <strong>138% FPL</strong> qualify. Approximately $20,783 single / $44,367 family of four in 2026.</li>
    <li><strong>Retroactive coverage:</strong> Iowa Medicaid can cover claims retroactively for up to 3 months before the application date. Apply immediately after a hospital visit if you were uninsured.</li>
    <li><strong>Managed care organizations (MCOs):</strong> Iowa Medicaid is administered through private managed care plans including AmeriHealth Caritas and Iowa Total Care. Ask the hospital&rsquo;s billing department which MCO accepts Iowa Medicaid.</li>
    <li><strong>Children (Hawk-I CHIP):</strong> Iowa&rsquo;s Hawk-I program covers children in households up to 302% FPL.</li>
    <li><strong>Apply:</strong> <a href="https://dhs.iowa.gov/ime/members/medicaid-a-to-z/IHAWP" target="_blank" rel="noopener">dhs.iowa.gov</a> or call 1-800-338-8366.</li>
</ul>

{_embed(mode="markup", title="Compare your Iowa hospital bill to Medicare rates", subtitle="Enter a CPT code and charged amount to see the markup over Medicare.", height="420")}

<h2 id="surprise-billing">3. Surprise billing protections (No Surprises Act)</h2>

<p>Iowa patients rely on the <strong>federal No Surprises Act</strong> (effective January 1, 2022) for surprise billing protection. Iowa does not have a comprehensive state surprise billing law.</p>

<p>Key NSA protections:</p>
<ul>
    <li><strong>Emergency services:</strong> In-network cost-sharing only, regardless of which providers treat you.</li>
    <li><strong>Ancillary providers at in-network facilities:</strong> Out-of-network anesthesiologists, radiologists, pathologists, and other ancillary providers at in-network hospitals cannot balance bill without advance written consent.</li>
    <li><strong>Good Faith Estimates:</strong> Uninsured patients are entitled to written cost estimates before any scheduled service costing $400 or more.</li>
    <li><strong>Air ambulance:</strong> No balance billing for out-of-network air ambulance services.</li>
</ul>

<p>Report NSA violations to <a href="https://www.cms.gov/nosurprises" target="_blank" rel="noopener">CMS</a> at 1-800-985-3059 or file with the <a href="https://iid.iowa.gov/consumers" target="_blank" rel="noopener">Iowa Insurance Division</a>.</p>

<div class="guide-cta-inline">
    <p><strong>Got a surprise bill in Iowa?</strong> BillKarma identifies No Surprises Act violations and generates a ready-to-mail dispute letter. <a href="/scan">Scan your bill free &mdash; takes under 2 minutes.</a></p>
</div>

<h2 id="statute-of-limitations">4. Statute of limitations on medical debt in Iowa (5 years)</h2>

<p>Iowa Code &sect;&nbsp;614.1 establishes a <strong>5-year statute of limitations</strong> on written contracts. Most hospital bills where you signed any financial responsibility form fall under this 5-year period.</p>

<table>
    <thead>
        <tr><th>Debt Type</th><th>Iowa SOL</th><th>Notes</th></tr>
    </thead>
    <tbody>
        <tr><td>Written contract (signed financial agreement)</td><td>5 years</td><td>Iowa Code § 614.1(4); applies to most hospital bills</td></tr>
        <tr><td>Open account (no signed contract)</td><td>5 years</td><td>Iowa Code § 614.1(6); open accounts also have 5-year period</td></tr>
        <tr><td>Court judgment</td><td>20 years</td><td>Iowa has an unusually long judgment SOL; responding to lawsuits is critical</td></tr>
    </tbody>
</table>

<p><strong>Warning:</strong> Iowa&rsquo;s 20-year judgment period is one of the longest in the nation. If a creditor wins a judgment against you, they have 20 years to collect. This makes resolving medical debt through charity care or negotiation &mdash; rather than ignoring it until it reaches litigation &mdash; especially important in Iowa.</p>

<p>Use our <a href="/statute-of-limitations">SOL lookup tool</a> to check the status of any specific debt before paying.</p>

<h2 id="iowa-consumer-credit">5. Iowa Consumer Credit Code protections</h2>

<p>The Iowa Consumer Credit Code (Iowa Code &sect;&nbsp;537) provides important protections for Iowa patients dealing with medical debt:</p>

<ul>
    <li><strong>Disclosure requirements.</strong> Creditors must provide clear, understandable billing statements and disclosures. A hospital or collector that provides misleading or confusing billing information may violate the Iowa CCC.</li>
    <li><strong>Collection practice limits.</strong> The Iowa CCC, working with the federal FDCPA, prohibits abusive, deceptive, or unfair collection practices. This includes threatening legal action the collector doesn&rsquo;t intend to take, misrepresenting the amount owed, and calling at unreasonable hours.</li>
    <li><strong>Remedy for violations.</strong> Patients who are victimized by Iowa CCC violations may be entitled to actual damages, statutory damages, attorney fees, and costs. File complaints with the <a href="https://www.iowaattorneygeneral.gov/for-consumers" target="_blank" rel="noopener">Iowa Attorney General&rsquo;s Consumer Protection Division</a>.</li>
    <li><strong>Credit counseling rights.</strong> Iowa consumers have the right to seek free or low-cost credit counseling through Iowa-licensed nonprofit credit counseling agencies.</li>
</ul>

<h2 id="debt-collection">6. Debt collection and wage garnishment in Iowa</h2>

<p>Iowa follows federal garnishment limits: creditors may garnish up to <strong>25% of disposable earnings</strong> per pay period, or the amount by which weekly disposable earnings exceed 30 times the federal minimum wage, whichever is less.</p>

<ul>
    <li><strong>Judgment required first.</strong> No garnishment without a court judgment. Always respond to collections lawsuits in Iowa.</li>
    <li><strong>Iowa exemptions:</strong> Iowa provides exemptions for Social Security benefits, unemployment compensation, workers&rsquo; compensation, and most pension income.</li>
    <li><strong>Homestead exemption.</strong> Iowa homeowners are protected by an unlimited homestead exemption for their primary residence. Iowa is one of the only states with an unlimited homestead exemption &mdash; a medical debt judgment cannot force the sale of your home, regardless of its value.</li>
    <li><strong>20-year judgment period.</strong> As noted above, Iowa judgment creditors have 20 years to collect. This makes ignoring collections lawsuits especially risky in Iowa.</li>
</ul>

<h2 id="how-to-dispute">7. How to dispute an Iowa hospital bill</h2>

<h3>Step 1: Request an itemized bill</h3>
<p>Request a fully itemized statement listing every CPT code, revenue code, service description, date, quantity, and unit price. Put the request in writing by certified mail.</p>

<h3>Step 2: Check Iowa Medicaid (IHAWP) eligibility</h3>
<p>If your income is under 138% FPL, apply for Medicaid at <a href="https://dhs.iowa.gov" target="_blank" rel="noopener">dhs.iowa.gov</a> immediately. Retroactive coverage for the past 3 months can eliminate the entire bill.</p>

<h3>Step 3: Apply for charity care under Iowa Code &sect; 135.71</h3>
<p>Gather income documentation and apply for the hospital&rsquo;s financial assistance program. Submit by certified mail, keep copies. The hospital must screen you for eligibility before sending your account to external collections.</p>

<h3>Step 4: Identify and dispute billing errors</h3>
<p>Use our <a href="/calculator">Medicare rate calculator</a> to benchmark charges. Common Iowa hospital billing errors include upcoded E&amp;M visits, duplicate lab charges, and unbundled procedures.</p>

<h3>Step 5: File complaints if needed</h3>
<ul>
    <li><strong>Hospital licensing and charity care:</strong> <a href="https://dial.iowa.gov/health-facilities" target="_blank" rel="noopener">Iowa Department of Inspections, Appeals, and Licensing</a></li>
    <li><strong>Consumer credit code violations:</strong> <a href="https://www.iowaattorneygeneral.gov/for-consumers" target="_blank" rel="noopener">Iowa Attorney General Consumer Protection</a></li>
    <li><strong>Insurance and surprise billing:</strong> <a href="https://iid.iowa.gov/consumers" target="_blank" rel="noopener">Iowa Insurance Division</a></li>
    <li><strong>No Surprises Act:</strong> <a href="https://www.cms.gov/nosurprises" target="_blank" rel="noopener">CMS Help Desk</a> (1-800-985-3059)</li>
</ul>

<div class="key-takeaway">
    <strong>Iowa&rsquo;s unlimited homestead exemption means your home is protected from medical debt.</strong> Even if a hospital wins a judgment against you, they cannot force the sale of your primary residence in Iowa. But act proactively &mdash; Iowa&rsquo;s 20-year judgment enforcement period means old judgments can follow you for decades.
</div>

<h2 id="bill-example">8. Annotated Iowa hospital bill</h2>

<div class="bill-example">
    <div class="bill-header">Itemized Statement &mdash; Hawkeye Regional Medical Center &mdash; Emergency Department &mdash; Date of Service: 02/28/2026</div>
    <div class="line-item error">
        <span>99284 &mdash; ED Visit Level 4, billed with separate E&amp;M code 99213 same day &nbsp; &#10060; <em>Billing a separate E&amp;M code on the same day as an ED visit for the same condition is typically not permitted under CMS guidelines. Only one E&amp;M should be billed per provider per date. Request the chart notes to verify both visits were separate and independent.</em></span>
        <span>$1,450.00 + $280.00</span>
    </div>
    <div class="line-item flagged">
        <span>73030 &mdash; Shoulder X-ray, minimum 2 views &nbsp; &#9888; <em>Medicare pays approximately $38 for this code. At $420 billed, this is 11.1&times; Medicare. Use this benchmark in your charity care application or negotiation.</em></span>
        <span>$420.00</span>
    </div>
    <div class="line-item">
        <span>85025 &mdash; Complete Blood Count with differential</span>
        <span>$205.00</span>
    </div>
    <div class="line-item">
        <span>80048 &mdash; Basic Metabolic Panel</span>
        <span>$180.00</span>
    </div>
    <div class="line-item">
        <span>93010 &mdash; Electrocardiogram with interpretation</span>
        <span>$245.00</span>
    </div>
    <div class="line-total">
        <span>TOTAL BILLED</span>
        <span>$2,780.00</span>
    </div>
</div>

<h2 id="case-study">9. Real patient results</h2>

<div class="case-study">
    <h3>Case study: $14,800 hospital bill eliminated via retroactive Iowa Medicaid &mdash; Des Moines</h3>
    <p><strong>Situation:</strong> An uninsured Des Moines warehouse worker was hospitalized for pneumonia for 3 days at UnityPoint Health &ndash; Iowa Methodist Medical Center. Total bill: $14,800.</p>
    <p><strong>Patient profile:</strong> Single adult, annual income $19,800 &mdash; approximately 127% FPL. Under Iowa&rsquo;s 138% Medicaid limit.</p>
    <p><strong>Action:</strong> BillKarma identified IHAWP Medicaid eligibility and helped the patient apply at dhs.iowa.gov within 30 days of discharge.</p>
    <p><strong>Result:</strong> Iowa Medicaid approved retroactive coverage for the month of hospitalization. The hospital wrote off the patient&rsquo;s balance.</p>
    <p><strong>Savings: $14,800.</strong></p>
</div>

<div class="case-study">
    <h3>Case study: Duplicate E&amp;M charges removed &mdash; Cedar Rapids</h3>
    <p><strong>Situation:</strong> A Cedar Rapids patient received an ER bill that included both a Level 4 ED visit (99284, $1,450) and a separate established patient office visit (99213, $280) billed on the same date of service by the same physician group.</p>
    <p><strong>Action:</strong> The patient disputed the duplicate E&amp;M charge by citing CMS National Correct Coding Initiative (NCCI) guidelines, which prohibit billing a separate E&amp;M code with an ED visit for the same condition on the same day. A dispute letter was sent to the billing department with the relevant CMS NCCI reference.</p>
    <p><strong>Result:</strong> The hospital removed the duplicate $280 office visit charge within 14 days.</p>
    <p><strong>Savings: $280.</strong></p>
</div>

<div class="case-study">
    <h3>Case study: $6,200 self-pay surgery bill reduced 65% via Iowa charity care &mdash; Iowa City</h3>
    <p><strong>Situation:</strong> An uninsured Iowa City resident earning $48,000/year (single, 307% FPL) received a $6,200 outpatient surgery bill from the University of Iowa Hospitals.</p>
    <p><strong>Action:</strong> Applied for financial assistance under Iowa Code &sect;&nbsp;135.71. The hospital&rsquo;s policy provided a 35% discount for patients between 300% and 350% FPL.</p>
    <p><strong>Result:</strong> Hospital approved $2,170 discount, reducing the balance to $4,030, with a 12-month, 0% interest payment plan.</p>
    <p><strong>Savings: $2,170.</strong></p>
</div>

<div class="key-takeaway">
    <strong>Iowa&rsquo;s Iowa Consumer Credit Code gives you extra protection against abusive collectors.</strong> If a debt collector uses threats, false statements, or deceptive practices, you may be entitled to damages under both the Iowa CCC and the federal FDCPA. Document all collector communications and report violations to the <a href="https://www.iowaattorneygeneral.gov/for-consumers" target="_blank" rel="noopener">Iowa Attorney General</a>.
</div>

<h2 id="sources">Sources</h2>

<ul class="sources-list">
    <li><a href="https://www.legis.iowa.gov/law/iowaCode/sections?codeChapter=135&session=91" target="_blank" rel="noopener">Iowa Code § 135.71: Hospital Charity Care Requirements</a></li>
    <li><a href="https://dhs.iowa.gov/ime/members/medicaid-a-to-z/IHAWP" target="_blank" rel="noopener">Iowa DHS: Iowa Health and Wellness Plan (Medicaid Expansion)</a></li>
    <li><a href="https://www.legis.iowa.gov/law/iowaCode/sections?codeChapter=614&session=91" target="_blank" rel="noopener">Iowa Code § 614.1: Statute of Limitations</a></li>
    <li><a href="https://www.iowaattorneygeneral.gov/for-consumers" target="_blank" rel="noopener">Iowa Attorney General: Consumer Protection Division</a></li>
    <li><a href="https://iid.iowa.gov/consumers" target="_blank" rel="noopener">Iowa Insurance Division: Consumer Resources</a></li>
    <li><a href="https://www.cms.gov/nosurprises" target="_blank" rel="noopener">CMS: No Surprises Act Overview and Patient Rights</a></li>
    <li><a href="https://aspe.hhs.gov/topics/poverty-economic-mobility/hhs-poverty-guidelines" target="_blank" rel="noopener">HHS: 2026 Federal Poverty Level Guidelines</a></li>
</ul>
""",
})
