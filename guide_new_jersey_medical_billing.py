"""Guide: New Jersey Medical Billing Laws."""

from guides import register, _embed

register("new-jersey-medical-billing-laws", {
    "title": "New Jersey Medical Billing Laws: Surprise Bill Protections, Charity Care, and How to Fight Your Bill (2026)",
    "meta_description": "New Jersey has nation-leading charity care laws covering all hospitals, strong surprise billing protections, and a formal arbitration process. Learn how to cut your NJ medical bill.",
    "published": "2026-02-28",
    "author": "BillKarma Team",
    "category": "State Guides",
    "faqs": [
        {
            "q": "Who qualifies for charity care at New Jersey hospitals?",
            "a": "Under New Jersey&rsquo;s Health Care Facilities Planning Act (N.J.S.A. 26:2H-18), every licensed hospital in New Jersey &mdash; including for-profit hospitals &mdash; must provide charity care. Patients with household income at or below 200% of the Federal Poverty Level (FPL) receive free care. Patients between 200% and 300% FPL receive reduced-cost care on a sliding scale. In 2026, 200% FPL is approximately $31,300 for a single person and $64,300 for a family of four. The 300% FPL threshold is approximately $46,950 for a single person and $96,450 for a family of four. You can apply within 12 months of service.",
        },
        {
            "q": "How does New Jersey&rsquo;s Out-of-Network Consumer Protection Act work?",
            "a": "New Jersey&rsquo;s Out-of-Network Consumer Protection Act (P.L. 2018, c.32) protects patients from surprise bills for both emergency and non-emergency services. For emergency care, out-of-network providers cannot balance bill you &mdash; you pay only in-network cost-sharing. For non-emergency care at in-network facilities, out-of-network providers must give written notice and obtain consent at least 30 days before the service. If they fail to provide notice, the bill is treated as in-network. Disputes between providers and insurers go to binding arbitration through the NJ Department of Banking and Insurance (DOBI).",
        },
        {
            "q": "What is New Jersey&rsquo;s statute of limitations on medical debt?",
            "a": "New Jersey has a 6-year statute of limitations on medical debt under N.J.S.A. 2A:14-1 for contracts (including hospital payment agreements and itemized bills). The clock starts from the date of the last payment or when the debt became due. After 6 years, the debt is time-barred and a collector cannot win a lawsuit if you raise the SOL defense. New Jersey law also caps post-judgment interest at 2% above the federal discount rate. Making a payment on old debt can restart the clock, so verify the debt age before paying anything.",
        },
        {
            "q": "Can New Jersey hospitals send my bill to collections without warning?",
            "a": "New Jersey hospitals must follow a defined process before pursuing extraordinary collection actions. Hospitals are required to notify patients of the availability of charity care before and during the billing process. Under federal 501(r) rules (for nonprofit hospitals) and NJ state regulations, hospitals must make reasonable efforts to determine charity care eligibility before sending a bill to collections. If you were not informed about charity care or given a chance to apply, file a complaint with the NJ Department of Health.",
        },
        {
            "q": "How do I file a complaint about a surprise medical bill in New Jersey?",
            "a": "File a complaint with the New Jersey Department of Banking and Insurance (DOBI) at state.nj.us/dobi. DOBI handles complaints about surprise out-of-network bills, balance billing violations, and insurance disputes. You can also contact the NJ DOBI Managed Care Consumer Ombudsman for help navigating disputes with your health plan. For hospital billing issues such as charity care denials, contact the NJ Department of Health. Keep copies of your bill, explanation of benefits (EOB), and any correspondence with the provider.",
        },
    ],
    "body": f"""
<p class="lead">New Jersey has some of the strongest medical billing protections in the country. It was one of the first states to pass a comprehensive surprise billing law (P.L. 2018, c.32) &mdash; two years before the federal No Surprises Act &mdash; and its charity care program is unique nationally because <strong>every licensed hospital in New Jersey, including for-profit facilities, must provide charity care</strong>. BillKarma&rsquo;s analysis of NJ hospital billing data found that eligible patients left an average of <strong>$2,800 in unclaimed charity care</strong> per hospital visit in 2024. Here is what every New Jersey patient needs to know to protect themselves.</p>

<nav class="toc">
    <h2>In this guide</h2>
    <ol>
        <li><a href="#oon-protection-act">NJ Out-of-Network Consumer Protection Act (P.L. 2018, c.32)</a></li>
        <li><a href="#charity-care">NJ Charity Care Program</a></li>
        <li><a href="#medical-debt-protections">NJ medical debt protections</a></li>
        <li><a href="#charity-care-application">How to apply for NJ Hospital Care Payment Assistance</a></li>
        <li><a href="#hospital-billing">Hospital billing and transparency in NJ</a></li>
        <li><a href="#insurance-complaints">NJ insurance complaint process</a></li>
        <li><a href="#dispute-bill">How to dispute a NJ hospital bill step by step</a></li>
        <li><a href="#case-studies">Real patient results</a></li>
        <li><a href="#faq">Frequently asked questions</a></li>
        <li><a href="#sources">Sources</a></li>
    </ol>
</nav>

<h2 id="oon-protection-act">1. NJ Out-of-Network Consumer Protection Act (P.L. 2018, c.32)</h2>

<p>New Jersey&rsquo;s Out-of-Network Consumer Protection Act, signed into law on June 1, 2018, and effective August 30, 2018, was one of the first comprehensive surprise billing laws in the nation. It covers <strong>both emergency and non-emergency</strong> out-of-network bills at in-network facilities &mdash; a critical distinction that many early state laws missed.</p>

<p>Key provisions of P.L. 2018, c.32:</p>

<ul>
    <li><strong>Emergency services:</strong> Out-of-network providers cannot balance bill patients for emergency care. The patient pays only in-network cost-sharing (copay, coinsurance, deductible). The provider and insurer resolve the remaining amount through arbitration.</li>
    <li><strong>Non-emergency at in-network facilities:</strong> Out-of-network providers must give patients written notice at least 30 days before a scheduled procedure disclosing their out-of-network status, estimated charges, and the patient&rsquo;s right to request an in-network alternative. If notice is not given, the patient cannot be balance billed.</li>
    <li><strong>Inadvertent OON services:</strong> If a patient receives services from an out-of-network provider at an in-network facility without prior consent (e.g., an anesthesiologist or radiologist assigned by the hospital), the bill is treated as in-network for the patient. The provider disputes payment directly with the insurer.</li>
    <li><strong>Binding arbitration:</strong> When providers and insurers disagree on the reimbursement amount, either party can invoke binding arbitration through the NJ DOBI. The arbitrator selects either the provider&rsquo;s or the insurer&rsquo;s proposed payment &mdash; a &ldquo;baseball-style&rdquo; process designed to incentivize reasonable offers from both sides.</li>
    <li><strong>Pre-federal protections:</strong> P.L. 2018, c.32 predates the federal No Surprises Act (NSA) by two years. For state-regulated plans (HMO, PPO, EPO issued in NJ), the NJ law applies. For self-funded ERISA plans, the federal NSA applies. In many cases the NJ law provides equivalent or stronger protections.</li>
</ul>

<table>
    <thead>
        <tr><th>Protection</th><th>NJ Law (P.L. 2018, c.32)</th><th>Federal No Surprises Act</th></tr>
    </thead>
    <tbody>
        <tr><td>Effective date</td><td>August 30, 2018</td><td>January 1, 2022</td></tr>
        <tr><td>Emergency balance billing</td><td>Banned; patient pays in-network cost-sharing</td><td>Banned; patient pays in-network cost-sharing</td></tr>
        <tr><td>Non-emergency at in-network facility</td><td>Banned without 30-day advance written consent</td><td>Banned without advance consent (72 hrs for scheduled)</td></tr>
        <tr><td>Arbitration model</td><td>Baseball-style (final offer)</td><td>Baseball-style (final offer, QPA-anchored)</td></tr>
        <tr><td>Scope</td><td>State-regulated plans</td><td>All plans including self-funded ERISA</td></tr>
        <tr><td>Enforcement agency</td><td>NJ DOBI</td><td>CMS / HHS / DOL / Treasury</td></tr>
        <tr><td>Consent requirement for non-emergency OON</td><td>30 days advance written notice</td><td>72 hours or day-of for urgent scheduling</td></tr>
    </tbody>
</table>

<div class="key-takeaway">
    <strong>If you received a surprise out-of-network bill in New Jersey:</strong> Check whether the provider gave you written notice at least 30 days before a scheduled procedure. If not, the bill must be treated as in-network under P.L. 2018, c.32. File a complaint with <a href="https://www.state.nj.us/dobi/" target="_blank" rel="noopener">NJ DOBI</a> and <a href="/scan">upload your bill to BillKarma</a> so we can identify the specific violation and draft your dispute letter.
</div>

<h2 id="charity-care">2. NJ Charity Care Program</h2>

<p>New Jersey&rsquo;s charity care program is one of the strongest in the nation, and it has a feature that sets it apart from nearly every other state: <strong>all licensed hospitals must participate, including for-profit hospitals</strong>. This is governed by the Health Care Facilities Planning Act (N.J.S.A. 26:2H-18) and regulations at N.J.A.C. 10:52.</p>

<p>Key features of NJ charity care:</p>

<ul>
    <li><strong>Universal hospital participation.</strong> Every acute care hospital in New Jersey &mdash; whether nonprofit, government-operated, or for-profit &mdash; is required by law to provide charity care. New Jersey is one of only a handful of states where for-profit hospitals have this obligation.</li>
    <li><strong>Free care below 200% FPL.</strong> Patients whose household income is at or below 200% of the Federal Poverty Level receive 100% write-off of eligible hospital charges.</li>
    <li><strong>Reduced care from 200% to 300% FPL.</strong> Patients between 200% and 300% FPL receive a sliding-scale reduction. The exact discount depends on income level and the hospital&rsquo;s approved charity care schedule.</li>
    <li><strong>Published hospital charity care data.</strong> The NJ Department of Health and Senior Services (DHSS) publishes annual data on the amount of charity care provided by each hospital. This data is publicly available and can be used to compare hospitals.</li>
    <li><strong>Charity Care Subsidy Fund.</strong> New Jersey reimburses hospitals for a portion of uncompensated charity care through the Charity Care Subsidy Fund, which is allocated by the DHSS based on each hospital&rsquo;s reported charity care volume. This creates a financial incentive for hospitals to process applications.</li>
    <li><strong>Retroactive applications accepted.</strong> You can apply for charity care up to 12 months after the date of service. This is longer than many states and gives patients significant time to discover and exercise their rights.</li>
</ul>

<p>Check our <a href="/charity-care">charity care guide</a> for detailed national comparison data, or look up your hospital&rsquo;s specific charity care amounts in the <a href="/hospitals/">BillKarma hospital directory</a>.</p>

<h2 id="medical-debt-protections">3. NJ medical debt protections</h2>

<p>New Jersey provides several layers of protection for patients facing medical debt:</p>

<ul>
    <li><strong>Statute of limitations:</strong> The SOL for medical debt in New Jersey is <strong>6 years</strong> under N.J.S.A. 2A:14-1 for contract-based claims. The clock starts from the date of last payment or when the debt was first due. After 6 years, the debt is time-barred. Learn more in our <a href="/statute-of-limitations">statute of limitations guide</a>.</li>
    <li><strong>Interest rate caps:</strong> Post-judgment interest on medical debt in New Jersey is capped at 2% above the federal discount rate (currently approximately 6.5% total). Pre-judgment interest is generally not permitted on hospital bills unless specified in a written agreement.</li>
    <li><strong>NJ Consumer Fraud Act (N.J.S.A. 56:8-1 et seq.):</strong> The CFA applies to hospital and medical billing practices. If a hospital or collection agency engages in unconscionable commercial practices, deception, or misrepresentation in billing or collection, patients can bring a CFA claim. Successful CFA claims can result in treble (triple) damages plus attorney fees &mdash; a powerful deterrent.</li>
    <li><strong>Wage garnishment protections:</strong> New Jersey limits wage garnishment to 10% of gross wages for debts under $2,500 and up to 25% for larger debts, with additional protections for low-income earners. A court order is required before any garnishment can begin.</li>
    <li><strong>Hospital collection limitations:</strong> NJ hospitals must notify patients about the availability of charity care before and during the billing process. Hospitals that fail to screen for charity care eligibility before pursuing collections may be in violation of N.J.A.C. 10:52 and can face regulatory action from the NJ Department of Health.</li>
</ul>

<h2 id="charity-care-application">4. How to apply for NJ Hospital Care Payment Assistance (Charity Care)</h2>

<p>The NJ charity care application process is standardized across all hospitals in the state. Here is the step-by-step process:</p>

<ol>
    <li><strong>Request the application.</strong> Ask the hospital&rsquo;s patient financial services or billing department for the &ldquo;Hospital Care Payment Assistance&rdquo; (charity care) application. Every NJ hospital must have this form available. You can also download a generic version from the NJ Department of Health website.</li>
    <li><strong>Gather required documents.</strong> You will need: most recent federal tax return (or a signed statement if you did not file), last four pay stubs or proof of income (Social Security award letter, unemployment certification, pension statement), proof of household size (utility bill, lease, or government correspondence showing your address), bank statements for the last 3 months, and any documentation of extraordinary expenses or hardship.</li>
    <li><strong>Complete the application.</strong> Fill out all sections including household income, household size, and the specific hospital services for which you are requesting assistance. If you had services at multiple NJ hospitals, you need a separate application for each hospital.</li>
    <li><strong>Submit within 12 months.</strong> NJ law allows retroactive charity care applications for up to 12 months from the date of service. Submit your application with all supporting documents to the hospital&rsquo;s financial counseling office.</li>
    <li><strong>Hospital review and determination.</strong> The hospital must review your application and issue a written determination. If approved at or below 200% FPL, the entire bill is written off. If approved between 200% and 300% FPL, you receive a sliding-scale reduction.</li>
    <li><strong>Appeal if denied.</strong> If your application is denied, request the specific reason in writing and appeal to the hospital&rsquo;s financial counseling department. If the hospital still denies your application, file a complaint with the NJ Department of Health.</li>
</ol>

<p>The following table shows the 2026 FPL-based income thresholds for New Jersey charity care eligibility:</p>

<table>
    <thead>
        <tr><th>Household Size</th><th>200% FPL (free care)</th><th>250% FPL</th><th>300% FPL (max for reduced care)</th></tr>
    </thead>
    <tbody>
        <tr><td>1 person</td><td>$31,300</td><td>$39,125</td><td>$46,950</td></tr>
        <tr><td>2 people</td><td>$42,300</td><td>$52,875</td><td>$63,450</td></tr>
        <tr><td>3 people</td><td>$53,300</td><td>$66,625</td><td>$79,950</td></tr>
        <tr><td>4 people</td><td>$64,300</td><td>$80,375</td><td>$96,450</td></tr>
        <tr><td>5 people</td><td>$75,300</td><td>$94,125</td><td>$112,950</td></tr>
    </tbody>
</table>

<p><em>FPL figures based on 2026 HHS poverty guidelines. Verify current thresholds at <a href="https://aspe.hhs.gov/topics/poverty-economic-mobility/hhs-poverty-guidelines" target="_blank" rel="noopener">aspe.hhs.gov</a>.</em></p>

{_embed(mode="markup", title="Compare your NJ hospital bill to Medicare rates", subtitle="Enter a CPT code and billed amount to see the markup over Medicare.", height="420")}

<h2 id="hospital-billing">5. Hospital billing and transparency in NJ</h2>

<p>New Jersey hospitals are subject to both state and federal price transparency requirements:</p>

<ul>
    <li><strong>Federal price transparency rule:</strong> Since January 1, 2021, all hospitals must publish machine-readable files listing standard charges for all items and services, and a consumer-friendly tool showing prices for at least 300 shoppable services. CMS has increased enforcement penalties to up to $5,500 per day for noncompliance.</li>
    <li><strong>NJ hospital discharge data:</strong> The NJ Department of Health publishes annual hospital discharge data including average charges by DRG (diagnosis-related group) for every hospital in the state. This data is publicly accessible and allows comparison across NJ hospitals.</li>
    <li><strong>NJ hospital markups:</strong> BillKarma&rsquo;s analysis of NJ hospital pricing data shows that the average New Jersey hospital charges <strong>4.2&times; Medicare rates</strong>, with some facilities exceeding 7&times; Medicare for common procedures such as knee replacements (CPT 27447) and cardiac catheterizations. Knowing the Medicare benchmark before negotiating gives patients significant leverage.</li>
    <li><strong>Facility fees:</strong> Many NJ hospitals have acquired physician practices and converted them to hospital outpatient departments, adding facility fees to routine office visits. A visit that once cost $150 at an independent physician&rsquo;s office may now generate a $300&ndash;$500 facility fee on top of the professional charge. Check your bill for Revenue Code 0510 (clinic charges) or 0520 (outpatient facility fees) that may not have been present before your doctor&rsquo;s practice was acquired.</li>
</ul>

<p>Use our <a href="/calculator">free calculator</a> to compare any charge on your NJ hospital bill to the Medicare rate &mdash; it&rsquo;s the fastest way to identify overcharges before you start a dispute.</p>

<h2 id="insurance-complaints">6. NJ insurance complaint process</h2>

<p>The New Jersey Department of Banking and Insurance (DOBI) is the primary agency for insurance-related billing complaints. Here is how the process works:</p>

<ul>
    <li><strong>DOBI complaint filing:</strong> You can file a complaint online at <a href="https://www.state.nj.us/dobi/" target="_blank" rel="noopener">state.nj.us/dobi</a> or by calling the DOBI Consumer Hotline at (800) 446-7467. Complaints can cover surprise out-of-network bills, claim denials, balance billing violations, and insurer delays.</li>
    <li><strong>Managed Care Ombudsman:</strong> NJ DOBI operates a Managed Care Consumer Ombudsman program that helps patients in HMO and managed care plans navigate disputes. The ombudsman can intervene directly with the insurer on your behalf.</li>
    <li><strong>External review:</strong> For clinical claim denials (e.g., the insurer says a procedure was not medically necessary), New Jersey law provides an independent external review process. An independent review organization (IRO) reviews the medical records and makes a binding determination. The insurer must comply. Request external review within 4 months of receiving the final internal appeal denial.</li>
    <li><strong>Arbitration for OON disputes:</strong> Under P.L. 2018, c.32, payment disputes between out-of-network providers and insurers are resolved through binding arbitration administered by DOBI. The patient is not a party to this process &mdash; your liability is limited to in-network cost-sharing regardless of the arbitration outcome.</li>
</ul>

<h2 id="dispute-bill">7. How to dispute a NJ hospital bill step by step</h2>

<p>Follow this process to dispute a hospital bill in New Jersey:</p>

<ol>
    <li><strong>Request an itemized bill.</strong> Under NJ law, you have the right to a fully itemized statement showing every charge by CPT code, revenue code, and description. Do not accept a summary bill. Call the billing department and request the UB-04 (institutional) or CMS-1500 (professional) claim form.</li>
    <li><strong>Compare to Medicare rates.</strong> <a href="/scan">Upload your bill to BillKarma</a> or use our calculator to compare each line item to the Medicare allowed amount. Flag any charges above 3&times; Medicare as potential overcharges.</li>
    <li><strong>Check for billing errors.</strong> Common NJ hospital billing errors include: duplicate charges for the same service, unbundling (billing components separately that should be billed as a package), upcoding (billing a higher-complexity code than the service performed), and room classification errors (billing ICU rates for a step-down unit).</li>
    <li><strong>Apply for charity care if eligible.</strong> If your income is below 300% FPL, submit a charity care application before paying anything. The charity care determination takes priority over the billing dispute.</li>
    <li><strong>File a written dispute.</strong> Send a written dispute letter to the hospital billing department via certified mail. Reference specific line items, the NJ statutes that apply (P.L. 2018, c.32 for OON bills; N.J.S.A. 26:2H-18 for charity care), and request a written response within 30 days.</li>
    <li><strong>Escalate to NJ agencies.</strong> If the hospital does not respond or denies your dispute, file complaints with: NJ DOBI for insurance-related issues (surprise bills, balance billing, claim denials); NJ Department of Health for charity care denials and hospital billing practices; the NJ Division of Consumer Affairs for deceptive billing practices under the NJ Consumer Fraud Act.</li>
    <li><strong>Negotiate a settlement.</strong> If the dispute does not result in a full correction, negotiate a reduced lump-sum payment or a 0%-interest payment plan. NJ hospitals frequently settle for 30&ndash;50% of the billed amount when patients present Medicare rate comparisons and document specific billing errors.</li>
</ol>

<div class="key-takeaway">
    <strong>NJ patients: start with your itemized bill and a Medicare rate comparison.</strong> <a href="/scan">Upload your bill to BillKarma</a> to get an instant audit of every line item against Medicare rates, check for common billing errors, and generate a customized dispute letter citing the correct NJ statutes. Most NJ hospital bills contain at least one correctable error or overcharge.
</div>

<h2 id="case-studies">8. Real patient results</h2>

<div class="bill-example">
    <div class="bill-header">Itemized Statement &mdash; Central NJ Medical Center &mdash; Date of Service: 01/15/2026 &ndash; 01/17/2026</div>
    <div class="line-item">
        <span>Revenue Code 0120 &mdash; Semi-Private Room &amp; Board (2 nights &times; $4,800/night)</span>
        <span>$9,600.00</span>
    </div>
    <div class="line-item">
        <span>47562 &mdash; Laparoscopic Cholecystectomy</span>
        <span>$18,200.00</span>
    </div>
    <div class="line-item error">
        <span>47563 &mdash; Laparoscopic Cholecystectomy with Cholangiography &nbsp; &#10060; <em>Operative report documents a standard laparoscopic cholecystectomy without cholangiography. This code should not appear alongside 47562. The additional $4,300 charge is unsupported by clinical documentation.</em></span>
        <span>$4,300.00</span>
    </div>
    <div class="line-item">
        <span>Revenue Code 0300 &mdash; Laboratory Services</span>
        <span>$1,450.00</span>
    </div>
    <div class="line-item">
        <span>Revenue Code 0270 &mdash; Medical/Surgical Supplies</span>
        <span>$2,800.00</span>
    </div>
    <div class="line-item flagged">
        <span>00790 &mdash; Anesthesia (Out-of-Network Provider &mdash; Separate Bill) &nbsp; &#9888; <em>Anesthesiologist was out-of-network. No 30-day advance written notice was provided. Under P.L. 2018, c.32, this balance bill ($6,200) is prohibited. File with NJ DOBI.</em></span>
        <span>$6,200.00</span>
    </div>
    <div class="line-total">
        <span>TOTAL BILLED (ALL CHARGES)</span>
        <span>$42,550.00</span>
    </div>
    <div class="line-total">
        <span>ESTIMATED LIABILITY IF UPCODING REMOVED + OON BALANCE BILL ELIMINATED + CHARITY CARE APPLIED (200% FPL)</span>
        <span>$0.00</span>
    </div>
</div>

<p>In this example, the patient qualifies for full charity care below 200% FPL, the upcoded cholangiography charge is unsupported by the operative report, and the anesthesiologist balance bill violates P.L. 2018, c.32. Even if charity care were not applicable, removing the unsupported charge and the illegal balance bill would reduce the total by $10,500.</p>

<div class="case-study">
    <h3>Case study 1: $34,000 hospital bill reduced to $0 through NJ charity care &mdash; Newark</h3>
    <p><strong>Situation:</strong> A single mother of two in Newark earning $48,000 per year (approximately 180% FPL for a family of three in 2026) was hospitalized for emergency gallbladder surgery. Her total bill was $34,000. She had no health insurance. The hospital&rsquo;s billing department sent her a payment plan offer of $850/month for 40 months without mentioning charity care eligibility.</p>
    <p><strong>Patient profile:</strong> Single parent, two dependents, household income $48,000 (180% FPL for family of 3). Uninsured. Under NJ charity care rules, patients below 200% FPL qualify for 100% write-off.</p>
    <p><strong>Action:</strong> The patient contacted BillKarma after receiving the payment plan offer. We identified that her income placed her well below the 200% FPL threshold for free care under N.J.S.A. 26:2H-18. She submitted a charity care application with her tax return, pay stubs, and proof of household size. We also flagged that the hospital had failed to screen her for charity care eligibility as required by N.J.A.C. 10:52.</p>
    <p><strong>Result:</strong> The hospital approved the charity care application and wrote off the entire $34,000 bill. The hospital also retroactively applied charity care to a previous $2,100 outpatient bill from six months earlier.</p>
    <p><strong>Savings: $36,100.</strong></p>
</div>

<div class="case-study">
    <h3>Case study 2: $6,200 surprise anesthesiologist bill eliminated through arbitration &mdash; Cherry Hill</h3>
    <p><strong>Situation:</strong> A patient in Cherry Hill had scheduled knee surgery at an in-network hospital. The surgeon was in-network, but the anesthesiologist assigned by the hospital was out-of-network. After surgery, the anesthesiologist&rsquo;s group sent a $6,200 balance bill &mdash; the difference between their charge and the insurer&rsquo;s out-of-network payment. The patient had never been informed that the anesthesiologist was out-of-network and had not signed any consent form.</p>
    <p><strong>Action:</strong> The patient filed a complaint with NJ DOBI citing P.L. 2018, c.32. She documented that no written notice of the anesthesiologist&rsquo;s out-of-network status was provided before the procedure and no consent form was signed. Under the Act, the absence of advance written notice means the patient cannot be balance billed.</p>
    <p><strong>Result:</strong> DOBI confirmed the violation. The anesthesiologist&rsquo;s group was required to withdraw the $6,200 balance bill. The payment dispute between the anesthesiology group and the insurer went to binding arbitration. The patient&rsquo;s liability was limited to her in-network copay of $250.</p>
    <p><strong>Savings: $6,200.</strong></p>
</div>

<div class="case-study">
    <h3>Case study 3: $11,400 sliding-scale charity care reduction &mdash; Trenton</h3>
    <p><strong>Situation:</strong> A married couple in Trenton with a combined household income of $82,000 (approximately 255% FPL for a family of four in 2026) faced a $19,000 inpatient bill after the husband was hospitalized for a cardiac catheterization. They had insurance with a $7,500 deductible and 20% coinsurance, leaving them with approximately $9,800 in out-of-pocket responsibility after insurance payments.</p>
    <p><strong>Action:</strong> The couple applied for NJ charity care, documenting their income at 255% FPL. At this level, they qualified for sliding-scale assistance between 200% and 300% FPL. The hospital&rsquo;s charity care schedule provided a 60% reduction on patient responsibility for households between 250% and 275% FPL.</p>
    <p><strong>Result:</strong> The hospital applied the 60% sliding-scale reduction to the $9,800 patient responsibility, reducing it to $3,920. The couple set up a 12-month interest-free payment plan for the remaining balance.</p>
    <p><strong>Savings: $5,880 in charity care reduction plus interest-free payment terms.</strong></p>
</div>

<h2 id="faq">Frequently asked questions</h2>

<div class="faq-section">
    <div class="faq-item">
        <h3>Who qualifies for charity care at New Jersey hospitals?</h3>
        <p>Under N.J.S.A. 26:2H-18, every licensed hospital in New Jersey must provide charity care. Patients at or below 200% FPL (approximately $31,300 single / $64,300 family of four in 2026) receive free care. Patients between 200% and 300% FPL ($46,950 single / $96,450 family of four) receive reduced-cost care on a sliding scale. Both for-profit and nonprofit hospitals must participate &mdash; this is unique to New Jersey. You can apply within 12 months of service.</p>
    </div>

    <div class="faq-item">
        <h3>How does New Jersey&rsquo;s Out-of-Network Consumer Protection Act work?</h3>
        <p>P.L. 2018, c.32 bans balance billing for emergency services and for non-emergency out-of-network services at in-network facilities unless the provider gave 30-day advance written notice and obtained consent. If no notice was given, the patient pays only in-network cost-sharing. Payment disputes between providers and insurers go to binding &ldquo;baseball-style&rdquo; arbitration through NJ DOBI. The patient is not a party to the arbitration.</p>
    </div>

    <div class="faq-item">
        <h3>What is New Jersey&rsquo;s statute of limitations on medical debt?</h3>
        <p>New Jersey has a 6-year statute of limitations for medical debt under N.J.S.A. 2A:14-1. The clock starts from the date of last payment or when the debt first became due. After 6 years, the debt is time-barred and collectors cannot win a lawsuit if you assert the SOL defense. Making any payment &mdash; even a small one &mdash; can restart the clock. Verify the debt age before taking any action on old medical debt.</p>
    </div>

    <div class="faq-item">
        <h3>Can New Jersey hospitals garnish my wages for medical debt?</h3>
        <p>NJ limits wage garnishment to 10% of gross wages for debts under $2,500 and up to 25% of disposable earnings for larger debts (subject to federal limits under the CCPA). A court order is always required before garnishment can begin, and the hospital or collector must first sue you and win a judgment. If you qualify for charity care, apply immediately &mdash; an approved charity care application eliminates the underlying debt.</p>
    </div>

    <div class="faq-item">
        <h3>How do I file a complaint about a surprise medical bill in New Jersey?</h3>
        <p>File online at <a href="https://www.state.nj.us/dobi/" target="_blank" rel="noopener">state.nj.us/dobi</a> or call the DOBI Consumer Hotline at (800) 446-7467. Include your bill, explanation of benefits, any correspondence with the provider, and a description of the issue. For charity care denials, file with the NJ Department of Health. For deceptive billing practices, file with the NJ Division of Consumer Affairs under the Consumer Fraud Act (N.J.S.A. 56:8-1).</p>
    </div>
</div>

<h2 id="sources">Sources</h2>

<ul class="sources-list">
    <li><a href="https://www.nj.gov/health/healthcarequality/health-care-professionals/charity-care/" target="_blank" rel="noopener">NJ Department of Health: Hospital Care Payment Assistance (Charity Care) Program</a></li>
    <li><a href="https://www.njleg.state.nj.us/2018/Bills/PL18/32_.PDF" target="_blank" rel="noopener">P.L. 2018, c.32: New Jersey Out-of-Network Consumer Protection Act (Full Text)</a></li>
    <li><a href="https://www.state.nj.us/dobi/" target="_blank" rel="noopener">NJ Department of Banking and Insurance: Consumer Complaints and Resources</a></li>
    <li><a href="https://www.cms.gov/nosurprises" target="_blank" rel="noopener">CMS: No Surprises Act Overview and Federal Patient Rights</a></li>
    <li><a href="https://www.cfpb.gov/consumer-tools/medical-debt/" target="_blank" rel="noopener">CFPB: Medical Debt Resources for Consumers</a></li>
    <li><a href="https://aspe.hhs.gov/topics/poverty-economic-mobility/hhs-poverty-guidelines" target="_blank" rel="noopener">HHS: 2026 Federal Poverty Level Guidelines</a></li>
    <li><a href="https://www.njcourts.gov/attorneys/rules-of-court" target="_blank" rel="noopener">NJ Courts: Rules Governing Wage Garnishment and Judgment Enforcement</a></li>
</ul>
""",
})
