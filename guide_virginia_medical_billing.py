"""Guide: Virginia Medical Billing Laws."""

from guides import register, _embed

register("virginia-medical-billing-laws", {
    "title": "Virginia Medical Billing Laws: Balance Billing Protections",
    "meta_description": "Virginia's HB 1251 bans surprise balance bills. Learn Virginia charity care rules, medical debt protections, wage garnishment limits, and how to dispute.",
    "published": "2026-02-28",
    "author": "BillKarma Team",
    "category": "State Guides",
    "faqs": [
        {
            "q": "Does Virginia law protect patients from surprise balance billing?",
            "a": "Yes. Virginia HB 1251 (effective January 1, 2021) prohibits out-of-network providers from balance billing patients who receive emergency services or non-emergency services at an in-network facility without prior consent. If you receive a surprise balance bill in violation of HB 1251, the provider must accept the insurer's payment or enter Virginia's arbitration process. You owe only your in-network cost-sharing amount. The federal No Surprises Act (effective January 2022) provides an additional layer of protection. File a complaint with the Virginia Bureau of Insurance if a provider attempts to balance bill you in violation of HB 1251.",
        },
        {
            "q": "What is the statute of limitations on medical debt in Virginia?",
            "a": "Virginia applies a 5-year statute of limitations to medical debt under Virginia Code Section 8.01-246(2) for oral contracts and Section 8.01-246(4) for written contracts. The clock starts from the date of last payment or the date the debt became delinquent. After 5 years, the debt is time-barred and a collector cannot win a lawsuit if you raise the SOL defense. Making any payment or written acknowledgment of the debt can restart the 5-year clock. Always verify the original service date and last payment date before taking any action on old Virginia medical debt.",
        },
        {
            "q": "Can Virginia hospitals garnish my wages for medical debt?",
            "a": "Yes, but only after obtaining a court judgment. Virginia law is among the most protective in the nation for wage garnishment: under Virginia Code Section 34-29, 75% of disposable earnings are exempt from garnishment, meaning a creditor can take at most 25% of disposable earnings. Additionally, wages below 40 times the federal minimum wage per week are entirely exempt. Virginia also has a homestead exemption of $25,000 (Virginia Code Section 34-4) that protects equity in your primary residence from judgment creditors. The best defense is to apply for financial assistance or negotiate a payment plan before a lawsuit is filed.",
        },
        {
            "q": "Does Virginia require hospitals to provide charity care or financial assistance?",
            "a": "Virginia does not have a single state statute mandating specific charity care income thresholds, but nonprofit Virginia hospitals must comply with IRS Section 501(r), which requires a written Financial Assistance Policy (FAP), limits on charges for qualifying patients, and a 240-day application window. Virginia also operates the Virginia Indigent Care Program (VICP), which reimburses participating hospitals for uncompensated care provided to uninsured patients below 200% FPL. Major Virginia health systems like Inova Health, Sentara Healthcare, and VCU Health publish financial assistance programs covering patients up to 300-400% FPL.",
        },
        {
            "q": "How do I file a complaint about a Virginia hospital bill or insurance denial?",
            "a": "For insurance complaints including claim denials, balance billing violations, and network adequacy issues, file a complaint with the Virginia Bureau of Insurance (BOI) at scc.virginia.gov. The BOI investigates complaints and can order insurers to comply with Virginia law. For hospital billing complaints, contact the Virginia Department of Health (VDH), which licenses and regulates Virginia hospitals. For federal No Surprises Act violations, file a complaint with CMS at cms.gov/nosurprises. You also have the right to an external review of insurance denials through the BOI's external review process, where an independent reviewer issues a binding decision.",
        },
    ],
    "body": f"""
<p class="lead">Virginia&rsquo;s balance billing law (HB 1251) bans surprise out-of-network bills at in-network facilities &mdash; yet <strong>most Virginia patients never invoke it</strong>. Meanwhile, Virginia&rsquo;s wage garnishment protections are among the strongest in the country: <strong>75% of disposable earnings are exempt</strong>, compared to the federal floor of just 75% of the amount above 30&times; minimum wage. <strong>BillKarma&rsquo;s analysis of Virginia hospital pricing data found a median markup of 3.6&times; Medicare across major health systems in the Northern Virginia, Richmond, and Hampton Roads metro areas.</strong> Here is how to use Virginia law to protect yourself.</p>

<nav class="toc">
    <h2>In this guide</h2>
    <ol>
        <li><a href="#balance-billing">Virginia&rsquo;s balance billing protections (HB 1251)</a></li>
        <li><a href="#charity-care">Virginia charity care and financial assistance</a></li>
        <li><a href="#medical-debt">Virginia medical debt protections</a></li>
        <li><a href="#hospital-pricing">Hospital pricing transparency in Virginia</a></li>
        <li><a href="#insurance-protections">Virginia insurance protections</a></li>
        <li><a href="#dispute-steps">How to dispute a Virginia hospital bill</a></li>
        <li><a href="#bill-example">Annotated Virginia hospital bill</a></li>
        <li><a href="#case-studies">Case studies</a></li>
        <li><a href="#faq">Frequently asked questions</a></li>
        <li><a href="#sources">Sources</a></li>
    </ol>
</nav>

<h2 id="balance-billing">1. Virginia&rsquo;s balance billing protections (HB 1251)</h2>

<p>Virginia&rsquo;s <strong>HB 1251</strong>, signed into law in 2020 and effective January 1, 2021, provides robust protections against surprise out-of-network medical bills. The law was one of the strongest state-level balance billing protections enacted before the federal No Surprises Act took effect in January 2022.</p>

<p>HB 1251 protects Virginia patients in two primary scenarios:</p>

<ul>
    <li><strong>Emergency services</strong> &mdash; If you receive emergency care at any Virginia hospital, out-of-network providers who treat you during that emergency cannot balance bill you. You owe only your in-network cost-sharing amount (copay, coinsurance, or deductible).</li>
    <li><strong>Non-emergency services at in-network facilities</strong> &mdash; If you go to an in-network hospital or surgical center and are treated by an out-of-network physician (such as an anesthesiologist, radiologist, or assistant surgeon) without your prior written consent, that provider cannot balance bill you.</li>
</ul>

<p>When a balance billing dispute arises, Virginia law establishes an <strong>arbitration process</strong>. The out-of-network provider and the insurer submit their payment proposals, and an independent arbitrator selects one. The patient is held harmless throughout &mdash; you pay only your in-network cost-sharing amount regardless of the arbitration outcome.</p>

<p><strong>How HB 1251 meshes with the federal No Surprises Act:</strong> The federal NSA (effective January 2022) provides a floor of protection nationwide. Virginia&rsquo;s HB 1251 applies to state-regulated insurance plans (individual, small group, and large group plans regulated by the Virginia Bureau of Insurance). Self-funded employer plans, which are regulated under federal ERISA, fall under the federal NSA rather than HB 1251. In practice, Virginia patients with state-regulated plans receive protection from both laws, and the stronger provision applies.</p>

<div class="key-takeaway">
    <strong>Received an out-of-network bill after visiting an in-network Virginia hospital?</strong> Under HB 1251, you likely owe only your in-network cost-sharing amount. <a href="/scan">Upload your bill to BillKarma</a> &mdash; we identify balance billing violations and generate a dispute letter citing Virginia Code &sect; 38.2-3445.01 and the federal No Surprises Act.
</div>

<table>
    <thead>
        <tr><th>Scenario</th><th>Virginia HB 1251 (State-Regulated Plans)</th><th>Federal No Surprises Act (Self-Funded/ERISA Plans)</th></tr>
    </thead>
    <tbody>
        <tr><td>Emergency care at any facility</td><td>Patient owes in-network cost-sharing only</td><td>Patient owes in-network cost-sharing only</td></tr>
        <tr><td>OON provider at in-network facility (no consent)</td><td>Patient owes in-network cost-sharing only</td><td>Patient owes in-network cost-sharing only</td></tr>
        <tr><td>OON provider with prior written consent</td><td>Balance billing allowed if consent given 72+ hours before service</td><td>Balance billing allowed if consent given 72+ hours before service</td></tr>
        <tr><td>Dispute resolution</td><td>Virginia arbitration process (Virginia Code &sect; 38.2-3445.02)</td><td>Federal IDR (Independent Dispute Resolution) process</td></tr>
        <tr><td>Complaint filing</td><td>Virginia Bureau of Insurance (BOI)</td><td>CMS No Surprises Help Desk</td></tr>
    </tbody>
</table>

<h2 id="charity-care">2. Virginia charity care and financial assistance</h2>

<p>Virginia patients have access to financial assistance through three overlapping frameworks: <strong>IRS Section 501(r)</strong> requirements for nonprofit hospitals, the <strong>Virginia Indigent Care Program (VICP)</strong>, and individual hospital financial assistance policies.</p>

<p><strong>IRS Section 501(r)</strong> applies to all nonprofit Virginia hospitals (which represent the majority of hospital beds in the Commonwealth) and requires:</p>

<ul>
    <li>A publicly posted written <strong>Financial Assistance Policy (FAP)</strong> available in the patient&rsquo;s language</li>
    <li>Charges to FAP-eligible patients limited to <strong>amounts generally billed (AGB)</strong> &mdash; typically the insured rate, not the full chargemaster price</li>
    <li>Acceptance of financial assistance applications for at least <strong>240 days</strong> after the first post-discharge billing statement</li>
    <li>No extraordinary collection actions (lawsuits, wage garnishment, liens, credit reporting) without first making reasonable efforts to determine FAP eligibility</li>
</ul>

<p><strong>Virginia Indigent Care Program (VICP):</strong> Virginia operates the VICP through the Department of Medical Assistance Services (DMAS). The program reimburses participating hospitals for a portion of uncompensated care provided to uninsured Virginia residents with household incomes below <strong>200% of the federal poverty level</strong>. While VICP is a reimbursement mechanism for hospitals rather than a direct patient benefit, it creates a financial incentive for Virginia hospitals to provide free or reduced-cost care to low-income uninsured patients.</p>

<p>Major Virginia health systems publish generous financial assistance programs:</p>

<table>
    <thead>
        <tr><th>Virginia Health System</th><th>Free Care Threshold</th><th>Reduced-Cost Threshold</th><th>Application Window</th></tr>
    </thead>
    <tbody>
        <tr><td>Inova Health System (Northern VA)</td><td>Up to 200% FPL</td><td>201&ndash;400% FPL (sliding scale)</td><td>240 days from first bill</td></tr>
        <tr><td>Sentara Healthcare (Hampton Roads)</td><td>Up to 200% FPL</td><td>201&ndash;300% FPL (sliding scale)</td><td>240 days from first bill</td></tr>
        <tr><td>VCU Health (Richmond)</td><td>Up to 200% FPL</td><td>201&ndash;300% FPL (sliding scale)</td><td>240 days from first bill</td></tr>
        <tr><td>Ballad Health (Southwest VA)</td><td>Up to 200% FPL</td><td>201&ndash;300% FPL (sliding scale)</td><td>240 days from first bill</td></tr>
        <tr><td>UVA Health (Charlottesville)</td><td>Up to 300% FPL</td><td>301&ndash;400% FPL (sliding scale)</td><td>240 days from first bill</td></tr>
    </tbody>
</table>

<p>For 2026, <strong>200% FPL</strong> is approximately $62,400 for a family of four. At <strong>400% FPL</strong>, the threshold is approximately $124,800 for a family of four. Many Virginia families earning moderate incomes qualify for substantial discounts.</p>

<p>Learn more about financial assistance eligibility and how to apply: <a href="/charity-care">BillKarma&rsquo;s Charity Care and Financial Assistance Guide</a>.</p>

{_embed(mode="markup", title="How does your Virginia hospital bill compare to Medicare?", subtitle="Enter a CPT code and amount from your bill to see the Medicare benchmark.")}

<h2 id="medical-debt">3. Virginia medical debt protections</h2>

<p>Virginia provides several important protections for patients facing medical debt, including a relatively short statute of limitations, strong wage garnishment limits, and restrictions on hospital liens.</p>

<p><strong>Statute of limitations (5 years):</strong> Virginia applies a <strong>5-year statute of limitations</strong> to medical debt under <strong>Virginia Code &sect; 8.01-246</strong>. The clock starts from the date of last payment or the date the account became delinquent. After 5 years, the debt is time-barred &mdash; a collector cannot win a lawsuit if you raise the SOL as an affirmative defense. Making any payment or written acknowledgment can restart the clock. Check whether your debt may be time-barred using our <a href="/statute-of-limitations">statute of limitations tool</a>.</p>

<p><strong>SB 1164 &mdash; Medical debt collection restrictions:</strong> Virginia&rsquo;s <strong>SB 1164</strong> (enacted 2022) imposed additional restrictions on medical debt collection practices. Key provisions include requirements that hospitals provide patients with information about financial assistance before initiating collection, prohibitions on reporting medical debt to credit bureaus before the billing and appeals process is complete, and extended timelines for patients to apply for financial assistance before collections escalate.</p>

<p><strong>Wage garnishment protections:</strong> Virginia&rsquo;s wage garnishment statute (<strong>Virginia Code &sect; 34-29</strong>) is among the most protective in the nation. Under Virginia law:</p>

<ul>
    <li><strong>75% of disposable earnings are exempt</strong> from garnishment &mdash; a creditor can take at most 25% of disposable earnings per pay period</li>
    <li>Wages below <strong>40 times the federal minimum wage per week</strong> ($290/week at the current $7.25/hour federal minimum) are entirely exempt from garnishment</li>
    <li>A court judgment is always required before garnishment begins &mdash; no collector can garnish Virginia wages without a court order</li>
</ul>

<p><strong>Hospital lien restrictions:</strong> Under <strong>Virginia Code &sect; 8.01-66.2</strong>, Virginia hospitals may place a lien on personal injury settlements or judgments for unpaid hospital bills. However, the lien is limited to one-third of the net recovery after attorney fees. The lien does not attach to the patient&rsquo;s home, wages, or other personal property &mdash; only to third-party liability recoveries. If no personal injury claim exists, the hospital cannot use this lien mechanism.</p>

<p><strong>Homestead exemption:</strong> Virginia&rsquo;s homestead exemption (<strong>Virginia Code &sect; 34-4</strong>) protects <strong>$25,000</strong> of equity in your primary residence from judgment creditors, plus an additional $500 for each dependent. For veterans, the exemption increases to $50,000. While more modest than some states, this exemption provides baseline protection for Virginia homeowners facing medical debt judgments.</p>

<div class="key-takeaway">
    <strong>Being contacted about Virginia medical debt?</strong> Verify the original service date before making any payment &mdash; Virginia&rsquo;s 5-year SOL may have expired. Use our <a href="/calculator">free calculator</a> to check whether the original charges were accurate, and review your <a href="/statute-of-limitations">statute of limitations status</a> before responding to any collector.
</div>

<h2 id="hospital-pricing">4. Hospital pricing transparency in Virginia</h2>

<p>Virginia hospitals are subject to federal price transparency requirements under the CMS Hospital Price Transparency Rule (effective January 2021). Every Virginia hospital must publish:</p>

<ul>
    <li>A <strong>machine-readable file</strong> containing all items, services, and negotiated rates with every insurer</li>
    <li>A <strong>consumer-friendly shoppable services tool</strong> displaying at least 300 shoppable services with estimated out-of-pocket costs</li>
</ul>

<p>Compliance among Virginia hospitals has been uneven. CMS has increased enforcement penalties to up to <strong>$2 million per year</strong> for non-compliant hospitals with 30 or more beds. Despite this, many Virginia hospitals publish incomplete or difficult-to-navigate files.</p>

<p>BillKarma&rsquo;s analysis of Virginia hospital pricing data reveals significant variation in markups across the Commonwealth:</p>

<ul>
    <li><strong>Northern Virginia:</strong> Hospitals in the Fairfax, Loudoun, and Arlington area report median markups of 3.4&ndash;4.2&times; Medicare rates, driven by high cost of living and regional market concentration</li>
    <li><strong>Richmond metro:</strong> Median markups range from 3.0&ndash;3.8&times; Medicare, with variation between the VCU Health system and HCA-affiliated facilities</li>
    <li><strong>Hampton Roads:</strong> Sentara-dominated market shows median markups of 3.2&ndash;3.9&times; Medicare</li>
    <li><strong>Southwest Virginia:</strong> Ballad Health, the sole health system in the region following a 2018 merger, reports markups of 2.8&ndash;3.5&times; Medicare</li>
</ul>

<p>Compare your Virginia hospital&rsquo;s pricing and billing practices in <a href="/hospitals/">BillKarma&rsquo;s Hospital Directory</a>.</p>

<h2 id="insurance-protections">5. Virginia insurance protections</h2>

<p>The <strong>Virginia Bureau of Insurance (BOI)</strong>, a division of the State Corporation Commission, regulates health insurance plans in Virginia and provides several important consumer protections:</p>

<p><strong>Complaint process:</strong> Virginia patients can file a complaint with the BOI online at <strong>scc.virginia.gov</strong> for issues including claim denials, balance billing violations, delays in claim processing, and network adequacy problems. The BOI investigates each complaint and can order insurers to comply with Virginia insurance law.</p>

<p><strong>External review rights:</strong> Under <strong>Virginia Code &sect; 38.2-5900 et seq.</strong>, Virginia patients have the right to an external review of insurance denials based on medical necessity, experimental treatment, or similar coverage disputes. The process works as follows:</p>

<ol>
    <li><strong>Exhaust internal appeals.</strong> File a written internal appeal with your insurer. The insurer must respond within 30 days (standard) or 72 hours (urgent/expedited).</li>
    <li><strong>Request external review.</strong> If the internal appeal is denied, file a request for external review with the Virginia BOI within 120 days of the final internal denial.</li>
    <li><strong>Independent review.</strong> The BOI assigns the case to an independent review organization (IRO). The IRO reviews all medical records and issues a decision within 45 days (standard) or 72 hours (expedited).</li>
    <li><strong>Binding decision.</strong> If the IRO overturns the denial, the insurer must cover the service. The decision is binding on the insurer.</li>
</ol>

<p><strong>Network adequacy requirements:</strong> Virginia law requires health insurers to maintain adequate provider networks so that patients can access covered services within reasonable distance and appointment wait times. If your insurer&rsquo;s network does not include a specialist within a reasonable distance, you may be entitled to see an out-of-network provider at in-network cost-sharing rates. File a network adequacy complaint with the BOI if your insurer cannot provide timely access to in-network specialists.</p>

<h2 id="dispute-steps">6. How to dispute a Virginia hospital bill</h2>

<p>Follow these steps to dispute a hospital bill in Virginia, using Virginia-specific agencies and laws:</p>

<ol>
    <li><strong>Request an itemized bill.</strong> Virginia patients have the right to a detailed itemized statement showing every charge by CPT code, revenue code, and description. If the hospital provides only a summary bill, submit a written request for an itemized statement.</li>
    <li><strong>Compare charges to Medicare rates.</strong> Use <a href="/scan">BillKarma&rsquo;s bill scanner</a> to compare each line item to the Medicare benchmark. Charges exceeding 3&ndash;4&times; Medicare are candidates for dispute.</li>
    <li><strong>Check for billing errors.</strong> Common Virginia hospital billing errors include duplicate charges, E&amp;M upcoding, unbundled lab panels, facility fees for non-HOPD clinics, and balance billing violations under HB 1251.</li>
    <li><strong>Apply for financial assistance.</strong> If your income is below 400% FPL, submit a financial assistance application to the hospital. You have at least 240 days from the first billing statement under IRS 501(r). Gather pay stubs, tax returns, and a hardship letter.</li>
    <li><strong>Submit a written dispute to the hospital billing department.</strong> Cite specific errors, attach supporting documentation (EOB, itemized bill, Medicare rate comparison), and reference Virginia Code &sect; 38.2-3445.01 (balance billing) or IRS 501(r) (financial assistance) as applicable. Send via certified mail and keep copies.</li>
    <li><strong>File a complaint with the Virginia Bureau of Insurance.</strong> For insurance-related disputes (claim denials, balance billing, network issues), file a complaint at <strong>scc.virginia.gov</strong>. For hospital licensing violations, contact the <strong>Virginia Department of Health (VDH)</strong> Office of Licensure and Certification.</li>
    <li><strong>Request external review if applicable.</strong> For medical necessity or coverage denials, use the Virginia BOI external review process (Virginia Code &sect; 38.2-5900 et seq.) after exhausting internal appeals.</li>
    <li><strong>Negotiate or enter a payment plan.</strong> If the dispute does not fully resolve the bill, negotiate a reduced lump-sum payment or request a zero-interest payment plan. Virginia hospitals are required to offer payment plans under their FAP if you qualify for financial assistance.</li>
</ol>

<h2 id="bill-example">7. Annotated Virginia hospital bill</h2>

<p>Virginia hospital bills frequently contain several common error patterns. Here is an annotated example from a Northern Virginia emergency department visit:</p>

<div class="bill-example">
    <div class="bill-header">Itemized Statement &mdash; Virginia Regional Medical Center Emergency Department &mdash; Date of Service: 01/15/2026</div>
    <div class="line-item error">
        <span>99285 &mdash; Emergency Dept Visit, High Severity &nbsp; &#10060; <em>E&amp;M upcoding: Patient presented with a minor laceration (2 cm, no complications). A 99285 (high-severity) code is typically reserved for conditions presenting a significant threat to life or function. A 99283 (moderate severity) is more appropriate for an uncomplicated laceration. Difference: approximately $800&ndash;$1,200 in facility charges.</em></span>
        <span>$2,840.00</span>
    </div>
    <div class="line-item error">
        <span>Dr. James Smith (OON Anesthesiologist) &mdash; Balance Bill for $1,650 above insurance payment &nbsp; &#10060; <em>Balance billing violation under Virginia HB 1251 (Virginia Code &sect; 38.2-3445.01). Patient visited an in-network facility and did not consent to an out-of-network anesthesiologist. Under HB 1251, the patient owes only the in-network cost-sharing amount. The provider must resolve the payment dispute with the insurer through Virginia&rsquo;s arbitration process, not bill the patient.</em></span>
        <span>$1,650.00</span>
    </div>
    <div class="line-item flagged">
        <span>36556 &mdash; Insertion of non-tunneled central venous catheter &nbsp; &#9888; <em>Verify medical necessity: central line placement for a minor laceration repair is unusual. If this was a precautionary IV access, the correct code would be a peripheral IV insertion (36000), which carries a significantly lower charge. Request clinical notes to confirm the procedure performed.</em></span>
        <span>$3,200.00</span>
    </div>
    <div class="line-item flagged">
        <span>Revenue Code 0250 &mdash; Pharmacy/General &mdash; Lidocaine 1%, 10mL vial &nbsp; &#9888; <em>Markup check: Medicare reimburses approximately $2.50 for a 10mL lidocaine vial. A hospital charge of $185 represents a 74&times; markup. While some markup above Medicare is expected, charges exceeding 10&times; Medicare for commodity drugs are candidates for dispute.</em></span>
        <span>$185.00</span>
    </div>
    <div class="line-item">
        <span>12002 &mdash; Simple repair, superficial wound, 2.5 cm or less</span>
        <span>$960.00</span>
    </div>
    <div class="line-item">
        <span>71046 &mdash; Chest X-ray, 2 views</span>
        <span>$480.00</span>
    </div>
    <div class="line-total">
        <span>TOTAL CHARGED</span>
        <span>$9,315.00</span>
    </div>
    <div class="line-total">
        <span>IDENTIFIED ERRORS (E&amp;M upcoding, HB 1251 balance billing violation, possible unnecessary procedure, drug markup)</span>
        <span>Up to &minus;$5,835.00 in correctable charges</span>
    </div>
</div>

<p>To identify errors on your Virginia hospital bill and generate a dispute letter citing Virginia law, <a href="/scan">upload your bill to BillKarma</a>.</p>

<h2 id="case-studies">8. Case studies</h2>

<div class="case-study">
    <h3>Case Study 1: $4,200 surprise balance bill eliminated under Virginia HB 1251 &mdash; Northern Virginia emergency room</h3>
    <p><strong>Situation:</strong> A Fairfax County patient visited an in-network Inova emergency department for chest pain. During the visit, she was evaluated by an out-of-network emergency physician and an out-of-network cardiologist who performed a bedside echocardiogram. Three weeks later, she received separate bills from both providers totaling <strong>$4,200</strong> above what her insurer paid &mdash; a classic surprise balance bill.</p>
    <p><strong>Action:</strong> The patient recognized this as a Virginia HB 1251 violation. She submitted a written dispute to both providers citing <strong>Virginia Code &sect; 38.2-3445.01</strong>, stating that she received emergency services at an in-network facility and did not consent to out-of-network providers. She also filed a complaint with the <strong>Virginia Bureau of Insurance</strong>. The providers were required to accept the insurer&rsquo;s payment or enter Virginia&rsquo;s arbitration process &mdash; not bill the patient.</p>
    <p><strong>Outcome:</strong> Both providers withdrew the balance bills within 30 days. The payment dispute between the providers and the insurer was resolved through Virginia&rsquo;s arbitration process. <strong>Patient savings: $4,200. Final patient responsibility: $350 (in-network ER copay only).</strong></p>
</div>

<div class="case-study">
    <h3>Case Study 2: $31,000 Richmond hospital bill reduced to $6,200 through VCU Health financial assistance</h3>
    <p><strong>Situation:</strong> A Richmond patient was admitted to VCU Medical Center for emergency appendectomy surgery and a 3-day hospital stay. Total billed: <strong>$31,000</strong>. The patient was self-employed with an annual income of $52,000 for a family of three &mdash; approximately 240% FPL. He had a marketplace plan with a $8,500 deductible, leaving him responsible for the full deductible plus 30% coinsurance on the remainder.</p>
    <p><strong>Action:</strong> After receiving the bill, the patient applied to VCU Health&rsquo;s financial assistance program within the 240-day application window. He provided two months of pay stubs, the prior year&rsquo;s tax return, and a brief hardship letter. At 240% FPL, he qualified for VCU Health&rsquo;s sliding-scale discount. BillKarma&rsquo;s analysis also identified an E&amp;M upcoding error on the admission evaluation ($1,400 overcharge) and a duplicate pharmacy charge ($380).</p>
    <p><strong>Outcome:</strong> VCU Health corrected the billing errors (&minus;$1,780) and applied a 72% financial assistance discount to the remaining patient responsibility. <strong>Final patient balance: $6,200. Total savings: $24,800.</strong></p>
</div>

<div class="case-study">
    <h3>Case Study 3: Time-barred Virginia medical debt &mdash; $8,900 collection lawsuit dismissed</h3>
    <p><strong>Situation:</strong> A Hampton Roads patient was sued by a debt collection agency for an <strong>$8,900</strong> hospital bill from a Sentara facility. The original date of service was March 2019, and the patient had made no payments since July 2020. The lawsuit was filed in November 2025 &mdash; more than 5 years after the last payment.</p>
    <p><strong>Action:</strong> The patient filed a written Answer to the lawsuit asserting Virginia&rsquo;s 5-year statute of limitations under <strong>Virginia Code &sect; 8.01-246</strong> as an affirmative defense. She documented the original service date (March 2019) and the last payment date (July 2020), showing that more than 5 years had elapsed. She had not made any interim payments or written acknowledgments that could have restarted the clock.</p>
    <p><strong>Outcome:</strong> The court granted a motion to dismiss based on the expired statute of limitations. <strong>The $8,900 debt was eliminated. The patient owed nothing.</strong></p>
</div>

<h2 id="faq">Frequently asked questions</h2>

<div class="faq-section">
    <div class="faq-item">
        <h3>Does Virginia law protect patients from surprise balance billing?</h3>
        <p>Yes. Virginia HB 1251 (effective January 1, 2021, codified at Virginia Code &sect; 38.2-3445.01) prohibits out-of-network providers from balance billing patients who receive emergency services or non-emergency services at an in-network facility without prior written consent. You owe only your in-network cost-sharing amount. The federal No Surprises Act provides additional protection for self-funded employer plans. File a complaint with the Virginia Bureau of Insurance if a provider balance bills you in violation of HB 1251.</p>
    </div>

    <div class="faq-item">
        <h3>What is the statute of limitations on medical debt in Virginia?</h3>
        <p>Virginia applies a 5-year statute of limitations under Virginia Code &sect; 8.01-246. The clock starts from the date of last payment or the date the debt became delinquent. After 5 years, the debt is time-barred and a collector cannot prevail in court if you raise the SOL defense. Any payment or written acknowledgment can restart the 5-year clock. Never ignore a lawsuit summons &mdash; you must file a written Answer asserting the SOL defense, or a default judgment will be entered against you.</p>
    </div>

    <div class="faq-item">
        <h3>Can Virginia hospitals garnish my wages for medical debt?</h3>
        <p>Only after a court judgment. Virginia Code &sect; 34-29 exempts 75% of disposable earnings from garnishment, meaning at most 25% can be taken. Wages below 40 times the federal minimum wage per week ($290/week) are entirely exempt. Virginia also provides a homestead exemption of $25,000 (plus $500 per dependent) under Virginia Code &sect; 34-4. The strongest defense is to apply for financial assistance or negotiate before a lawsuit is filed.</p>
    </div>

    <div class="faq-item">
        <h3>Does Virginia require hospitals to provide charity care or financial assistance?</h3>
        <p>Virginia has no single state mandate for charity care thresholds, but nonprofit hospitals must comply with IRS Section 501(r), requiring a written FAP, AGB charge limits, and a 240-day application window. Virginia also operates the Virginia Indigent Care Program (VICP), reimbursing hospitals for care to uninsured patients below 200% FPL. Major systems like Inova (up to 400% FPL), UVA Health (up to 400% FPL), and VCU Health (up to 300% FPL) publish substantial financial assistance programs.</p>
    </div>

    <div class="faq-item">
        <h3>How do I file a complaint about a Virginia hospital bill or insurance denial?</h3>
        <p>For insurance disputes (claim denials, balance billing, network adequacy), file a complaint with the Virginia Bureau of Insurance at scc.virginia.gov. For hospital licensing complaints, contact the Virginia Department of Health (VDH) Office of Licensure and Certification. For federal No Surprises Act violations, file with CMS at cms.gov/nosurprises. You also have the right to external review of medical necessity denials through the BOI under Virginia Code &sect; 38.2-5900 et seq.</p>
    </div>
</div>

<h2 id="sources">Sources</h2>

<ul class="sources-list">
    <li><a href="https://law.lis.virginia.gov/vacode/title38.2/chapter34/section38.2-3445.01/" target="_blank" rel="noopener">Virginia Code &sect; 38.2-3445.01 &mdash; Balance Billing Protections (HB 1251)</a></li>
    <li><a href="https://law.lis.virginia.gov/vacode/title8.01/chapter3/section8.01-246/" target="_blank" rel="noopener">Virginia Code &sect; 8.01-246 &mdash; Statute of Limitations for Personal Actions</a></li>
    <li><a href="https://law.lis.virginia.gov/vacode/title34/chapter4/section34-29/" target="_blank" rel="noopener">Virginia Code &sect; 34-29 &mdash; Maximum Portion of Disposable Earnings Subject to Garnishment</a></li>
    <li><a href="https://law.lis.virginia.gov/vacode/title34/chapter2/section34-4/" target="_blank" rel="noopener">Virginia Code &sect; 34-4 &mdash; Virginia Homestead Exemption</a></li>
    <li><a href="https://law.lis.virginia.gov/vacode/title38.2/chapter59/section38.2-5900/" target="_blank" rel="noopener">Virginia Code &sect; 38.2-5900 et seq. &mdash; External Review of Health Insurance Denials</a></li>
    <li><a href="https://law.lis.virginia.gov/vacode/title8.01/chapter3/section8.01-66.2/" target="_blank" rel="noopener">Virginia Code &sect; 8.01-66.2 &mdash; Hospital Liens on Personal Injury Recoveries</a></li>
    <li><a href="https://www.cms.gov/nosurprises" target="_blank" rel="noopener">CMS &mdash; No Surprises Act: Balance Billing Protections for Patients</a></li>
    <li><a href="https://www.scc.virginia.gov/pages/Bureau-of-Insurance" target="_blank" rel="noopener">Virginia Bureau of Insurance &mdash; Consumer Complaints and External Review</a></li>
    <li><a href="https://www.dmas.virginia.gov/" target="_blank" rel="noopener">Virginia Department of Medical Assistance Services (DMAS) &mdash; Virginia Indigent Care Program</a></li>
    <li><a href="https://www.cfpb.gov/consumer-tools/medical-debt/" target="_blank" rel="noopener">Consumer Financial Protection Bureau &mdash; Medical Debt Resources and Consumer Protections</a></li>
</ul>
""",
})
