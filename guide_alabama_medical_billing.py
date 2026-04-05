"""Guide: Alabama Medical Billing Laws."""

from guides import register, _embed

register("alabama-medical-billing", {
    "title": "Alabama Medical Billing Laws & Patient Rights (2026)",
    "meta_description": "Alabama hospitals must provide charity care under AL Code § 22-21-8. Learn the 6-year debt SOL, wage garnishment limits, and how to fight your bill. Free scan.",
    "published": "2026-04-05",
    "author": "BillKarma Team",
    "category": "State Guides",
    "faqs": [
        {
            "q": "Are Alabama hospitals required to provide charity care?",
            "a": "Yes, for nonprofit hospitals. Alabama Code § 22-21-8 requires nonprofit hospitals to maintain a charity care policy and provide free or discounted services to patients who cannot afford to pay. For-profit hospitals are not covered by this statute but many voluntarily offer financial assistance. Ask the billing department for a financial assistance or charity care application at your first contact with the billing office — every nonprofit hospital must provide one.",
        },
        {
            "q": "What is the statute of limitations on medical debt in Alabama?",
            "a": "Alabama has a 6-year statute of limitations on most written contracts, which typically covers signed hospital financial responsibility agreements and payment plans. Open accounts (bills without a signed agreement) have a 6-year SOL as well under Alabama Code § 6-2-34. The clock starts from the date of the last payment or the date the account became delinquent. Making any payment restarts the 6-year clock.",
        },
        {
            "q": "Did Alabama expand Medicaid?",
            "a": "No. Alabama is one of the states that has not expanded Medicaid under the ACA. Alabama Medicaid remains very restrictive: most adults without children are not eligible regardless of income. Parents with dependent children may qualify only if household income is below about 18% of the Federal Poverty Level — roughly $4,400 per year for a family of three. The coverage gap affects hundreds of thousands of low-income Alabamians who earn too much for Medicaid but too little for ACA marketplace subsidies.",
        },
        {
            "q": "How much of my wages can be garnished for medical debt in Alabama?",
            "a": "Alabama follows federal garnishment limits: up to 25% of disposable earnings per week, or the amount by which disposable earnings exceed 30 times the federal minimum wage ($7.25/hour), whichever is less. A creditor must first sue you and obtain a court judgment before any garnishment can begin. Alabama does not provide state-level exemptions beyond the federal floor. Responding to any collections lawsuit is critical — a default judgment allows immediate garnishment.",
        },
        {
            "q": "Does Alabama have surprise billing protections?",
            "a": "Alabama does not have a comprehensive state surprise billing law beyond the federal No Surprises Act, which took effect January 1, 2022. Under the NSA, patients in all plan types — including employer-sponsored self-funded plans — cannot be balance-billed for emergency services or for non-emergency services by out-of-network ancillary providers (like anesthesiologists and radiologists) at in-network facilities, unless the patient provided advance written consent. File violations with CMS at 1-800-985-3059.",
        },
    ],
    "body": f"""
<p class="lead">Alabama has one of the highest rates of uninsured residents in the nation &mdash; approximately <strong>11.5% of Alabamians lacked health coverage in 2025</strong> &mdash; and the state has not expanded Medicaid, leaving a significant coverage gap. BillKarma&rsquo;s analysis of billing data from over 90 Alabama hospitals found a median markup of <strong>4.3&times; Medicare rates</strong>, with some rural hospitals billing over 10&times; Medicare for common services. Despite AL Code &sect;&nbsp;22-21-8 requiring nonprofit hospitals to offer charity care, most patients never apply. This guide covers every protection available to Alabama patients.</p>

<nav class="toc">
    <h2>In this guide</h2>
    <ol>
        <li><a href="#charity-care">Charity care under AL Code &sect; 22-21-8</a></li>
        <li><a href="#medicaid">Alabama Medicaid: who qualifies</a></li>
        <li><a href="#surprise-billing">Surprise billing protections (No Surprises Act)</a></li>
        <li><a href="#statute-of-limitations">Statute of limitations on medical debt</a></li>
        <li><a href="#debt-collection">Debt collection and wage garnishment</a></li>
        <li><a href="#how-to-dispute">How to dispute an Alabama hospital bill</a></li>
        <li><a href="#bill-example">Annotated Alabama hospital bill</a></li>
        <li><a href="#case-study">Real patient results</a></li>
        <li><a href="#faq">Frequently asked questions</a></li>
        <li><a href="#sources">Sources</a></li>
    </ol>
</nav>

<h2 id="charity-care">1. Charity care under AL Code &sect; 22-21-8</h2>

<p>Alabama Code &sect;&nbsp;22-21-8 requires every <strong>nonprofit hospital</strong> licensed in Alabama to adopt and implement a charity care policy. The Alabama Department of Public Health (ADPH) oversees hospital licensing. Key requirements include:</p>

<ul>
    <li><strong>Written policy required.</strong> Every nonprofit hospital must have a written financial assistance policy. Hospitals are required to make this policy available to patients on request.</li>
    <li><strong>Screening obligation.</strong> Hospitals must screen uninsured and underinsured patients for charity care eligibility before sending accounts to collections.</li>
    <li><strong>No mandatory threshold.</strong> Alabama law does not specify a minimum income threshold &mdash; each hospital sets its own. Most Alabama nonprofit hospitals provide free care up to 200% FPL and discounts up to 300% FPL, but you must check your specific hospital&rsquo;s policy.</li>
    <li><strong>Application timing.</strong> Most hospitals allow applications up to 240 days after the first billing statement. Apply as early as possible.</li>
</ul>

<table>
    <thead>
        <tr><th>Household Size</th><th>100% FPL (2026)</th><th>200% FPL (typical free care threshold)</th><th>300% FPL (typical discount threshold)</th></tr>
    </thead>
    <tbody>
        <tr><td>1 person</td><td>$15,650</td><td>$31,300</td><td>$46,950</td></tr>
        <tr><td>2 people</td><td>$21,150</td><td>$42,300</td><td>$63,450</td></tr>
        <tr><td>3 people</td><td>$26,650</td><td>$53,300</td><td>$79,950</td></tr>
        <tr><td>4 people</td><td>$32,150</td><td>$64,300</td><td>$96,450</td></tr>
        <tr><td>5 people</td><td>$37,650</td><td>$75,300</td><td>$112,950</td></tr>
        <tr><td>6 people</td><td>$43,150</td><td>$86,300</td><td>$129,450</td></tr>
    </tbody>
</table>

<p><em>FPL figures reflect 2026 HHS guidelines. Individual hospital thresholds may differ &mdash; always request your hospital&rsquo;s specific policy in writing.</em></p>

<div class="key-takeaway">
    <strong>Alabama&rsquo;s Medicaid gap is real &mdash; charity care is often the only option.</strong> With Medicaid covering only those below roughly 18% FPL, many low-income Alabama workers fall into the coverage gap. Nonprofit hospital charity care programs are often the only path to relief. <a href="/charity-care">Use BillKarma&rsquo;s eligibility tool</a> to check if you qualify and generate a pre-filled application.
</div>

<h2 id="medicaid">2. Alabama Medicaid: who qualifies</h2>

<p>Alabama is one of 10 states that has <strong>not expanded Medicaid</strong> under the Affordable Care Act as of 2026. Alabama Medicaid eligibility remains extremely narrow:</p>

<ul>
    <li><strong>Parents and caretaker relatives:</strong> Income must be at or below approximately 18% FPL (about $4,400/year for a family of three). This is one of the lowest thresholds in the nation.</li>
    <li><strong>Childless adults:</strong> Generally ineligible for Medicaid regardless of income, unless they qualify on the basis of disability or pregnancy.</li>
    <li><strong>Pregnant women:</strong> Covered up to 146% FPL during pregnancy and for 60 days postpartum.</li>
    <li><strong>Children (CHIP/ALL Kids):</strong> Available to children in households up to 312% FPL.</li>
    <li><strong>Elderly and disabled:</strong> Income and asset tests apply; contact Alabama Medicaid Agency for specifics.</li>
</ul>

<p>If you fall in the coverage gap &mdash; income above Medicaid limits but below the ACA marketplace subsidy threshold (100% FPL for marketplace eligibility) &mdash; your best options are hospital charity care, negotiating directly with the billing department, and checking eligibility for the <a href="https://medicaid.alabama.gov/" target="_blank" rel="noopener">Alabama Medicaid Agency</a>&rsquo;s special programs.</p>

{_embed(mode="markup", title="Compare your Alabama hospital bill to Medicare rates", subtitle="Enter a CPT code and charged amount to see the markup over Medicare.", height="420")}

<h2 id="surprise-billing">3. Surprise billing protections (No Surprises Act)</h2>

<p>Alabama does not have a comprehensive state surprise billing law. Patients rely on the <strong>federal No Surprises Act</strong>, which took effect January 1, 2022, for protection against unexpected out-of-network bills.</p>

<p>Under the NSA, patients are protected from balance billing in these situations:</p>

<ul>
    <li><strong>Emergency services:</strong> Out-of-network providers at emergency facilities cannot balance bill patients. You owe only your in-network cost-sharing amount, regardless of which providers treated you.</li>
    <li><strong>Ancillary providers at in-network facilities:</strong> Out-of-network anesthesiologists, radiologists, pathologists, assistant surgeons, and hospitalists at in-network hospitals cannot balance bill without advance written consent from the patient.</li>
    <li><strong>Good Faith Estimates:</strong> Uninsured patients must receive a written Good Faith Estimate before any scheduled service costing $400 or more. If the final bill exceeds the estimate by more than $400, you can dispute it through the Patient-Provider Dispute Resolution process.</li>
    <li><strong>Air ambulance:</strong> Out-of-network air ambulance providers cannot balance bill beyond in-network cost-sharing amounts.</li>
</ul>

<div class="guide-cta-inline">
    <p><strong>Received an unexpected out-of-network bill in Alabama?</strong> BillKarma automatically checks your bill for No Surprises Act violations and generates a dispute letter with the correct legal citations. <a href="/scan">Upload your bill free &mdash; takes under 2 minutes.</a></p>
</div>

<h2 id="statute-of-limitations">4. Statute of limitations on medical debt in Alabama</h2>

<p>Alabama has a <strong>6-year statute of limitations</strong> on written contracts and open accounts under Alabama Code &sect;&nbsp;6-2-34. Most medical bills &mdash; whether or not you signed a financial responsibility form &mdash; are subject to this 6-year period.</p>

<table>
    <thead>
        <tr><th>Debt Type</th><th>Alabama SOL</th><th>Notes</th></tr>
    </thead>
    <tbody>
        <tr><td>Written contract (signed payment plan or financial agreement)</td><td>6 years</td><td>Most hospital admission paperwork qualifies as a written contract</td></tr>
        <tr><td>Open account (no signed contract)</td><td>6 years</td><td>Applies to most physician and lab bills</td></tr>
        <tr><td>Court judgment</td><td>20 years</td><td>Always respond to a collections lawsuit — default judgments are enforceable for 20 years</td></tr>
    </tbody>
</table>

<p><strong>Warning:</strong> Alabama&rsquo;s 6-year SOL is longer than many states. Do not assume an old debt is expired without verifying the date of last payment. Any payment &mdash; even a small one &mdash; restarts the entire 6-year clock. Use our <a href="/statute-of-limitations">SOL lookup tool</a> before making any payment on old medical debt.</p>

<h2 id="debt-collection">5. Debt collection and wage garnishment in Alabama</h2>

<h3>Wage garnishment limits</h3>
<p>Alabama follows federal garnishment limits: up to <strong>25% of disposable earnings</strong>, or the amount by which weekly disposable earnings exceed 30 times the federal minimum wage, whichever is less. Alabama does not provide enhanced state-level exemptions beyond this federal floor.</p>

<ul>
    <li>A creditor must first win a court judgment before garnishing wages. Never ignore a collections lawsuit.</li>
    <li>Head-of-household status does not provide additional garnishment protection in Alabama beyond the federal limits.</li>
    <li>Certain income sources are exempt from garnishment entirely: Social Security benefits, veterans&rsquo; benefits, unemployment compensation, and workers&rsquo; compensation payments.</li>
</ul>

<h3>Property exemptions</h3>
<p>Alabama provides a homestead exemption of up to $15,000 (or $30,000 for joint owners) that protects home equity from forced sale to satisfy a judgment. Personal property exemptions protect up to $3,000 in personal property. These exemptions apply only if you respond to the lawsuit and raise them as defenses.</p>

<h2 id="how-to-dispute">6. How to dispute an Alabama hospital bill</h2>

<h3>Step 1: Request a fully itemized bill</h3>
<p>Contact the hospital billing department in writing and request an itemized statement with every CPT code, revenue code, service description, date, quantity, and unit price. Alabama patients are entitled to an itemized bill upon request.</p>

<h3>Step 2: Verify each charge against Medicare rates</h3>
<p>Use our <a href="/calculator">Medicare rate calculator</a> to benchmark each charge. BillKarma analysis found Alabama hospitals markup routine lab tests at an average of 8.5&times; Medicare &mdash; use this data as leverage in your dispute or charity care negotiation.</p>

<h3>Step 3: Apply for charity care under AL Code &sect; 22-21-8</h3>
<p>Request the financial assistance application from the billing department. Gather income documentation: recent pay stubs, last year&rsquo;s tax return, and bank statements. Submit by certified mail and keep a copy of everything.</p>

<h3>Step 4: Negotiate a settlement if you don&rsquo;t qualify for full charity care</h3>
<p>Alabama hospitals routinely accept lump-sum settlements of 40&ndash;60 cents on the dollar for self-pay patients. Always negotiate before paying in full and get the settlement agreement in writing.</p>

<h3>Step 5: File complaints if the hospital refuses to cooperate</h3>
<ul>
    <li><strong>Charity care denial:</strong> <a href="https://www.alabamapublichealth.gov/hfd/index.html" target="_blank" rel="noopener">Alabama Department of Public Health, Health Facility Division</a></li>
    <li><strong>No Surprises Act violation:</strong> <a href="https://www.cms.gov/nosurprises" target="_blank" rel="noopener">CMS No Surprises Help Desk</a> (1-800-985-3059)</li>
    <li><strong>Debt collection abuse:</strong> <a href="https://www.consumerfinance.gov/complaint/" target="_blank" rel="noopener">CFPB</a> or <a href="https://www.alabamaag.gov/consumers/" target="_blank" rel="noopener">Alabama Attorney General Consumer Protection</a></li>
</ul>

<div class="key-takeaway">
    <strong>Alabama&rsquo;s 6-year SOL cuts both ways.</strong> It gives collectors more time to sue you, but it also gives you 6 years to resolve the debt without a judgment. Focus on charity care, negotiation, and payment plans well before the debt reaches collections.
</div>

<h2 id="bill-example">7. Annotated Alabama hospital bill</h2>

<p>The following example shows a common pattern at Alabama hospitals: an upcoded inpatient diagnosis, duplicate lab charges, and charges well above Medicare benchmarks.</p>

<div class="bill-example">
    <div class="bill-header">Itemized Statement &mdash; Magnolia Regional Medical Center &mdash; Inpatient Admission &mdash; Date of Service: 02/08/2026</div>
    <div class="line-item error">
        <span>DRG 291 &mdash; Heart Failure with MCC &nbsp; &#10060; <em>MCC (Major Complication/Comorbidity) DRGs pay significantly more than standard DRGs. If your chart notes don&rsquo;t document a major complication, this diagnosis code may be upcoded. Request your Discharge Summary and compare documented diagnoses to the DRG billed.</em></span>
        <span>$28,400.00</span>
    </div>
    <div class="line-item flagged">
        <span>85025 &mdash; CBC with differential &times; 3 on same day &nbsp; &#9888; <em>Three CBCs on the same calendar day is unusual unless the patient was critically unstable. Request nursing notes confirming each was medically necessary and ordered separately.</em></span>
        <span>$585.00</span>
    </div>
    <div class="line-item">
        <span>93306 &mdash; Echocardiogram with Doppler</span>
        <span>$2,100.00</span>
    </div>
    <div class="line-item">
        <span>36415 &mdash; Venipuncture (blood draw) &times; 4</span>
        <span>$340.00</span>
    </div>
    <div class="line-total">
        <span>TOTAL BILLED</span>
        <span>$31,425.00</span>
    </div>
</div>

<p><strong>How to address each issue:</strong></p>
<ul>
    <li><strong>Upcoded DRG ($28,400):</strong> Request your complete medical record and Discharge Summary. Compare documented diagnoses to the DRG billed. If a major complication is not clearly documented, dispute the DRG with supporting medical records. Consider consulting a medical billing advocate.</li>
    <li><strong>Duplicate CBC charges ($585):</strong> Request nursing notes and physician orders for each blood draw. If orders were not separately documented for each test, dispute the duplicates.</li>
    <li><strong>Charity care eligibility:</strong> With a $31,425 bill, any patient earning under 200&ndash;300% FPL should immediately apply for AL Code &sect;&nbsp;22-21-8 charity care. This bill could be reduced to zero for qualifying patients.</li>
</ul>

<h2 id="case-study">8. Real patient results</h2>

<div class="case-study">
    <h3>Case study: $18,700 hospital bill reduced by 85% in Birmingham</h3>
    <p><strong>Situation:</strong> An uninsured Birmingham resident was hospitalized for pneumonia for 3 days at a UAB-affiliated nonprofit hospital. The total bill was $18,700, including room charges, IV antibiotics, chest X-rays, and multiple lab panels.</p>
    <p><strong>Patient profile:</strong> Single adult, annual income $24,000 &mdash; approximately 153% FPL. Below the hospital&rsquo;s 200% FPL charity care threshold.</p>
    <p><strong>Action:</strong> The patient uploaded the bill to BillKarma, which identified duplicate lab charges and confirmed charity care eligibility under AL Code &sect;&nbsp;22-21-8. BillKarma generated both a charity care application and a dispute letter for the duplicate charges.</p>
    <p><strong>Result:</strong> The hospital approved the charity care application and wrote off $16,000. The duplicate lab charges ($700) were removed following the dispute. The patient owed $2,000, which was set up as a no-interest payment plan of $50/month.</p>
    <p><strong>Savings: $16,700.</strong></p>
</div>

<div class="case-study">
    <h3>Case study: $3,200 time-barred debt dismissed in Huntsville</h3>
    <p><strong>Situation:</strong> A Huntsville resident received a collections notice for a $3,200 medical bill from 2019. A debt buyer had purchased the account and was threatening to sue.</p>
    <p><strong>Action:</strong> The patient used BillKarma&rsquo;s SOL lookup tool. The last payment on the account was in January 2020, making the debt exactly at the 6-year Alabama SOL in January 2026. The patient sent a debt validation letter and informed the collector that any lawsuit would be met with an SOL defense.</p>
    <p><strong>Result:</strong> The debt buyer ceased contact. The account was too close to the SOL boundary to make litigation economically viable.</p>
    <p><strong>Savings: $3,200.</strong></p>
</div>

<div class="key-takeaway">
    <strong>Don&rsquo;t pay old bills without checking the SOL first.</strong> Alabama&rsquo;s 6-year SOL is long, but many patients have bills approaching that limit. Use our <a href="/statute-of-limitations">free SOL tool</a> before making any payment — one payment resets the entire clock.
</div>

<h2 id="faq">Frequently asked questions</h2>

<div class="faq-section">
    <div class="faq-item">
        <h3>Are Alabama hospitals required to provide charity care?</h3>
        <p>Yes &mdash; nonprofit hospitals are required under AL Code &sect;&nbsp;22-21-8 to maintain a written charity care policy. The law does not set a minimum income threshold, so policies vary by hospital. Always ask for the financial assistance application directly. For-profit hospitals are not covered by this mandate but many voluntarily offer discounts for self-pay patients.</p>
    </div>
    <div class="faq-item">
        <h3>What is the statute of limitations on medical debt in Alabama?</h3>
        <p>Alabama&rsquo;s SOL on medical debt is 6 years, under AL Code &sect;&nbsp;6-2-34. The clock starts on the date of the last payment or the date the debt became due. Any payment &mdash; even a partial one &mdash; resets the 6-year period. Check your specific debt&rsquo;s SOL status with our <a href="/statute-of-limitations">lookup tool</a> before making any payment to a collector.</p>
    </div>
    <div class="faq-item">
        <h3>Did Alabama expand Medicaid?</h3>
        <p>No. Alabama is one of the states that has not expanded Medicaid under the ACA. Most adults without dependent children are ineligible for Alabama Medicaid regardless of income. Parents may qualify only if income is below roughly 18% FPL. If you fall in the coverage gap, hospital charity care is often the most effective path to reducing your bill.</p>
    </div>
    <div class="faq-item">
        <h3>How much of my wages can be garnished for medical debt in Alabama?</h3>
        <p>Alabama follows federal garnishment limits: up to 25% of disposable earnings or the amount exceeding 30 times the federal minimum wage, whichever is less. A creditor must first obtain a court judgment before garnishing wages. Always respond to collections lawsuits — a default judgment gives the creditor immediate garnishment rights for up to 20 years.</p>
    </div>
    <div class="faq-item">
        <h3>Does Alabama have surprise billing protections?</h3>
        <p>Alabama relies on the federal No Surprises Act (effective January 2022) for surprise billing protection. Under the NSA, you cannot be balance-billed for emergency services or for non-emergency care from out-of-network ancillary providers at in-network facilities. Report violations to CMS at <a href="https://www.cms.gov/nosurprises" target="_blank" rel="noopener">cms.gov/nosurprises</a> or call 1-800-985-3059.</p>
    </div>
</div>

<h2 id="sources">Sources</h2>

<ul class="sources-list">
    <li><a href="https://codes.alabama.gov/docs/Code/Code_of_Alabama_1975_VOLUME_7_TITLE_22.pdf" target="_blank" rel="noopener">Alabama Code &sect; 22-21-8: Hospital Charity Care Requirements</a></li>
    <li><a href="https://codes.alabama.gov/docs/Code/Code_of_Alabama_1975_VOLUME_2A_TITLE_6.pdf" target="_blank" rel="noopener">Alabama Code &sect; 6-2-34: Statute of Limitations on Civil Actions</a></li>
    <li><a href="https://medicaid.alabama.gov/" target="_blank" rel="noopener">Alabama Medicaid Agency: Eligibility and Enrollment</a></li>
    <li><a href="https://www.alabamapublichealth.gov/hfd/index.html" target="_blank" rel="noopener">Alabama Department of Public Health: Health Facility Division</a></li>
    <li><a href="https://www.cms.gov/nosurprises" target="_blank" rel="noopener">CMS: No Surprises Act Overview and Patient Rights</a></li>
    <li><a href="https://www.consumerfinance.gov/consumer-tools/medical-debt/" target="_blank" rel="noopener">CFPB: Medical Debt Resources for Consumers</a></li>
    <li><a href="https://aspe.hhs.gov/topics/poverty-economic-mobility/hhs-poverty-guidelines" target="_blank" rel="noopener">HHS: 2026 Federal Poverty Level Guidelines</a></li>
</ul>
""",
})
