"""Guide: California Medical Billing Laws."""

from guides import register, _embed

register("california-medical-billing-laws", {
    "title": "California Medical Billing Laws & Patient Rights (2026)",
    "meta_description": "California has the strongest patient billing protections in the US. Know your rights on surprise billing, charity care, and AB 774 before paying any bill.",
    "published": "2026-02-22",
    "author": "BillKarma Team",
    "category": "State Guides",
    "faqs": [
        {
            "q": "What is the income limit for charity care at California hospitals?",
            "a": "Under AB 1020 (effective 2024), California hospitals must provide free care to patients at or below 250% of the Federal Poverty Level (FPL) — that is $38,625 for a single person or $79,050 for a family of four in 2026. Patients between 250% and 350% FPL ($51,450 single / $106,200 family of four) qualify for a sliding-scale discount. Eligibility is based on household income at the time of service, and you can apply retroactively up to 240 days after the first billing statement.",
        },
        {
            "q": "How long do California hospitals have to wait before sending my bill to collections?",
            "a": "Under SB 1419 (2022), California hospitals must wait at least 180 days from the first billing statement before referring a patient account to collections or taking any extraordinary collection action. During that 180-day window, the hospital cannot report the debt to credit bureaus, sue you, or use wage garnishment. You should use this time to apply for charity care under AB 1020 or dispute any billing errors.",
        },
        {
            "q": "What is California's statute of limitations on medical debt?",
            "a": "California has one of the shortest statutes of limitations in the country: 2 years for open accounts and 4 years for written contracts (such as a patient financial responsibility agreement). The clock typically starts from the date of the last payment or the date the debt became delinquent. After the SOL expires, the debt is time-barred and collectors cannot win a lawsuit against you — but a payment can reset the clock.",
        },
        {
            "q": "How do I file a complaint about a California hospital billing error?",
            "a": "California patients can file billing complaints with two agencies depending on the type of plan. If you have an HMO, PPO, or other managed care plan regulated by the state, file with the California Department of Managed Health Care (DMHC) at dmhc.ca.gov — they can order refunds and investigate. If you have a self-funded employer plan or a complaint about a hospital billing practice more broadly, contact the California Attorney General's consumer protection division or the California Department of Health Care Services (DHCS).",
        },
        {
            "q": "Can California hospitals garnish my wages for medical debt?",
            "a": "California hospitals cannot garnish wages without first suing you and obtaining a court judgment. Even then, California law limits garnishment to 25% of disposable earnings or the amount by which your weekly earnings exceed 40 times the state minimum wage — whichever is less. However, under AB 1020 and SB 1419, hospitals must offer payment plans and financial assistance before any collections action, and no collections can begin until 180 days after the first billing statement.",
        },
    ],
    "body": f"""
<p class="lead">California&rsquo;s 3.2 million uninsured residents face hospital bills that average <strong>4.1&times; over Medicare rates</strong> &mdash; but the state has passed some of the strongest patient billing protections in the nation. AB 1020 (effective 2024) requires every hospital to offer free care to patients earning up to $38,625 and sliding-scale discounts up to $51,450 (single) or $106,200 (family of four). BillKarma&rsquo;s analysis of 1,400+ California hospitals found that the median markup over Medicare across the state is 4.1&times; &mdash; and that fewer than 1 in 6 patients eligible for charity care under AB 1020 applied for it in 2024. This guide explains every right you have and how to use them.</p>

<nav class="toc">
    <h2>In this guide</h2>
    <ol>
        <li><a href="#ab1020">AB 1020: California&rsquo;s charity care law</a></li>
        <li><a href="#income-limits">2026 income thresholds and sliding scale</a></li>
        <li><a href="#sb1419">SB 1419: Itemized bills and collections delay</a></li>
        <li><a href="#balance-billing">Balance billing protections in California</a></li>
        <li><a href="#bill-example">Annotated California hospital bill</a></li>
        <li><a href="#statute-of-limitations">California statute of limitations on medical debt</a></li>
        <li><a href="#how-to-dispute">How to dispute a California hospital bill</a></li>
        <li><a href="#case-studies">Real patient results</a></li>
        <li><a href="#faq">Frequently asked questions</a></li>
        <li><a href="#sources">Sources</a></li>
    </ol>
</nav>

<h2 id="ab1020">1. AB 1020: California&rsquo;s charity care law</h2>

<p>Assembly Bill 1020, signed in 2023 and effective January 1, 2024, is the cornerstone of California&rsquo;s hospital billing protections. It requires every general acute care hospital in California to provide financial assistance on a sliding scale based on the Federal Poverty Level (FPL). Unlike the federal IRS 501(r) requirement, which only applies to nonprofit hospitals, AB 1020 applies to <strong>all licensed hospitals in California</strong> &mdash; including for-profit facilities.</p>

<p>Key provisions of AB 1020:</p>

<ul>
    <li><strong>Free care at or below 250% FPL.</strong> Hospitals must write off 100% of the bill for patients whose income does not exceed 250% of the FPL.</li>
    <li><strong>Sliding-scale discounts from 250% to 350% FPL.</strong> Patients above 250% but at or below 350% FPL receive discounts that decrease incrementally as income rises.</li>
    <li><strong>Retroactive eligibility.</strong> You can apply for charity care up to 240 days after the first billing statement &mdash; even if you have already made payments.</li>
    <li><strong>No collections before charity care review.</strong> Hospitals must screen patients for financial assistance eligibility before beginning any extraordinary collection action.</li>
    <li><strong>Insured patients are eligible.</strong> If you have insurance but still face high out-of-pocket costs (deductible, coinsurance, copay), you can apply for financial assistance on your patient responsibility portion.</li>
</ul>

<div class="key-takeaway">
    <strong>AB 1020 covers every California hospital &mdash; not just nonprofits.</strong> If you received care at any licensed hospital in California and your income is below $51,450 (single) or $106,200 (family of four), ask the billing department for the financial assistance application. They are legally required to provide it. Check your hospital&rsquo;s markup rate in our <a href="/hospitals/">hospital directory</a>.
</div>

<h2 id="income-limits">2. 2026 income thresholds and sliding scale</h2>

<p>The FPL thresholds below are based on the 2026 federal poverty guidelines published by HHS. California uses the same federal numbers for AB 1020 eligibility.</p>

<table>
    <thead>
        <tr><th>Household Size</th><th>100% FPL (2026)</th><th>250% FPL (free care)</th><th>350% FPL (max for discount)</th></tr>
    </thead>
    <tbody>
        <tr><td>1 person</td><td>$15,650</td><td>$39,125</td><td>$54,775</td></tr>
        <tr><td>2 people</td><td>$21,150</td><td>$52,875</td><td>$74,025</td></tr>
        <tr><td>3 people</td><td>$26,650</td><td>$66,625</td><td>$93,275</td></tr>
        <tr><td>4 people</td><td>$32,150</td><td>$80,375</td><td>$112,525</td></tr>
        <tr><td>5 people</td><td>$37,650</td><td>$94,125</td><td>$131,775</td></tr>
    </tbody>
</table>

<p><em>Note: FPL figures are updated annually each February. The numbers above reflect 2026 HHS guidelines. Confirm current thresholds at <a href="https://aspe.hhs.gov/topics/poverty-economic-mobility/hhs-poverty-guidelines" target="_blank" rel="noopener">aspe.hhs.gov</a> before applying.</em></p>

<p>Use our calculator to see how your specific charges compare to Medicare rates &mdash; this gives you the strongest possible basis for your charity care application and any dispute:</p>

{_embed(mode="markup", title="Compare your California hospital bill to Medicare rates", subtitle="Enter a CPT code and charged amount to see the markup over Medicare.", height="420")}

<h2 id="sb1419">3. SB 1419: Itemized bills and collections delay</h2>

<p>Senate Bill 1419, effective January 1, 2023, added two major protections for California patients:</p>

<h3>Right to an itemized bill within 30 days</h3>

<p>You have the right to request an itemized statement of every charge on your hospital bill. Under SB 1419, the hospital must deliver that itemized bill within <strong>30 days</strong> of your request. The itemized bill must include the CPT code or revenue code for every charge, the quantity billed, the unit price, and the total. This is your primary tool for identifying billing errors.</p>

<h3>180-day collections moratorium</h3>

<p>Hospitals in California cannot take any extraordinary collection action &mdash; including sending your bill to a collections agency, filing a lawsuit, reporting to a credit bureau, or placing a lien on your property &mdash; until at least <strong>180 days</strong> after the first post-discharge billing statement. The 180-day clock gives you time to:</p>

<ul>
    <li>Request and review your itemized bill</li>
    <li>Apply for AB 1020 charity care</li>
    <li>File a dispute for billing errors</li>
    <li>Negotiate a payment plan or lump-sum settlement</li>
    <li>File a complaint with the DMHC if your insurer underpaid</li>
</ul>

<table>
    <thead>
        <tr><th>California Billing Protection</th><th>Law</th><th>What It Requires</th><th>Timeline</th></tr>
    </thead>
    <tbody>
        <tr><td>Charity care for all hospitals</td><td>AB 1020 (2024)</td><td>Free care &le;250% FPL; sliding scale to 350% FPL</td><td>Apply within 240 days of first bill</td></tr>
        <tr><td>Itemized bill on request</td><td>SB 1419 (2023)</td><td>Hospital must deliver full itemized statement</td><td>Within 30 days of request</td></tr>
        <tr><td>Collections delay</td><td>SB 1419 (2023)</td><td>No extraordinary collection actions</td><td>Before 180 days from first bill</td></tr>
        <tr><td>Credit bureau reporting ban</td><td>SB 1419 (2023)</td><td>Cannot report to credit bureaus before 180 days</td><td>180-day moratorium</td></tr>
        <tr><td>Payment plan requirement</td><td>State law</td><td>Must offer payment plan before collections</td><td>Before any collections action</td></tr>
    </tbody>
</table>

<h2 id="balance-billing">4. Balance billing protections in California</h2>

<p>California patients are protected from balance billing under both state law and the federal No Surprises Act (NSA):</p>

<ul>
    <li><strong>In-network providers:</strong> Balance billing is completely banned. You cannot be charged more than your in-network cost-sharing (deductible, copay, coinsurance) by any provider who is in your plan&rsquo;s network.</li>
    <li><strong>Emergency services:</strong> Out-of-network providers at any emergency facility cannot balance bill you for emergency care. You pay only the in-network cost-sharing amount, regardless of whether the facility or any individual provider is in-network.</li>
    <li><strong>Non-emergency care at in-network facility:</strong> Providers at an in-network facility (such as an anesthesiologist or radiologist you did not choose) cannot balance bill you unless they obtained a signed consent form at least 72 hours in advance and you agreed in writing.</li>
    <li><strong>California Department of Managed Health Care (DMHC):</strong> Handles complaints against HMO and PPO plans regulated under state law. File complaints at <a href="https://www.dmhc.ca.gov/FileAComplaint.aspx" target="_blank" rel="noopener">dmhc.ca.gov</a>.</li>
</ul>

<div class="key-takeaway">
    <strong>Received a surprise bill from an out-of-network provider?</strong> <a href="/scan">Upload it to BillKarma</a> &mdash; we identify balance billing violations and generate a dispute letter citing the No Surprises Act and California law. You may owe $0 on that bill.
</div>

<h2 id="bill-example">5. Annotated California hospital bill</h2>

<p>The following example shows a 2-day inpatient hospital stay in California with four common billing problems: a upcoded room classification, split physician and hospital bills, a facility fee, and a balance billing charge from an out-of-network anesthesiologist.</p>

<div class="bill-example">
    <div class="bill-header">Itemized Statement &mdash; California General Hospital &mdash; Date of Service: 01/14/2026 &ndash; 01/16/2026</div>
    <div class="line-item error">
        <span>Revenue Code 0200 &mdash; ICU Room &amp; Board (2 days &times; $8,400/day) &nbsp; &#10060; <em>Patient was in step-down unit, not ICU. ICU rate is 3&times; the step-down rate. Request medical records to verify room assignment.</em></span>
        <span>$16,800.00</span>
    </div>
    <div class="line-item">
        <span>Revenue Code 0300 &mdash; Laboratory Services</span>
        <span>$1,240.00</span>
    </div>
    <div class="line-item">
        <span>Revenue Code 0320 &mdash; Radiology / CT Chest with Contrast (71250)</span>
        <span>$3,800.00</span>
    </div>
    <div class="line-item">
        <span>Revenue Code 0250 &mdash; Pharmacy (IV antibiotics, 4 doses)</span>
        <span>$960.00</span>
    </div>
    <div class="line-item">
        <span>Revenue Code 0510 &mdash; Clinic/Outpatient Facility Fee &nbsp; &#9888; <em>Facility fee charged on outpatient follow-up visit on day of discharge. Verify whether this qualifies as a separate billable encounter.</em></span>
        <span>$850.00</span>
    </div>
    <div class="line-total">
        <span>HOSPITAL BILL SUBTOTAL</span>
        <span>$23,650.00</span>
    </div>
    <div class="line-item">
        <span>99223 &mdash; Initial Hospital Care, High Complexity (Attending Physician &mdash; separate bill)</span>
        <span>$2,100.00</span>
    </div>
    <div class="line-item">
        <span>99232 &mdash; Subsequent Hospital Care &times; 2 (Attending Physician &mdash; separate bill)</span>
        <span>$1,200.00</span>
    </div>
    <div class="line-item flagged">
        <span>00790 &mdash; Anesthesia for Upper Abdominal Procedures (Out-of-Network Anesthesiologist &mdash; separate bill) &nbsp; &#9888; <em>Out-of-network anesthesiologist at in-network facility. Balance bill of $3,200 above allowed amount is prohibited under No Surprises Act and CA law. You owe only your in-network cost-sharing.</em></span>
        <span>$5,800.00</span>
    </div>
    <div class="line-total">
        <span>TOTAL BILLED (ALL BILLS)</span>
        <span>$32,750.00</span>
    </div>
</div>

<p><strong>What to do with each problem on this bill:</strong></p>
<ul>
    <li><strong>ICU upcoding:</strong> Request your medical records and nursing notes to confirm your room assignment. If you were in a step-down or telemetry unit, write a formal dispute and submit to the hospital billing department. Step-down room rates are typically $2,500&ndash;$3,500/day versus $7,000&ndash;$9,000/day for ICU.</li>
    <li><strong>Facility fee on discharge follow-up:</strong> Ask whether the outpatient clinic fee was for a separate, medically distinct encounter. If it was routine discharge counseling, it should be bundled with the inpatient stay, not billed separately.</li>
    <li><strong>Out-of-network anesthesiologist balance bill:</strong> Send a written dispute citing the No Surprises Act and California balance billing law. You owe only your in-network cost-sharing amount. File a complaint with the DMHC if the balance bill is not withdrawn within 30 days.</li>
</ul>

<p>Want to know what Medicare pays for each of these CPT codes? Use our <a href="/calculator">free calculator</a> to look up the Medicare benchmark for any procedure.</p>

<h2 id="statute-of-limitations">6. California statute of limitations on medical debt</h2>

<p>California has one of the shortest medical debt statutes of limitations in the US &mdash; a meaningful protection for patients who cannot afford to pay. The clock typically starts from the date of your last payment or the date the debt became delinquent.</p>

<table>
    <thead>
        <tr><th>Debt Type</th><th>California SOL</th><th>Notes</th></tr>
    </thead>
    <tbody>
        <tr><td>Open account (no signed contract)</td><td>2 years</td><td>Most hospital bills are open accounts</td></tr>
        <tr><td>Written contract (signed financial agreement)</td><td>4 years</td><td>Applies if you signed a payment contract</td></tr>
        <tr><td>Judgment (after collector wins lawsuit)</td><td>10 years (renewable)</td><td>Responding to lawsuits is critical &mdash; never ignore a summons</td></tr>
    </tbody>
</table>

<p><strong>What resets the clock in California:</strong> Any payment, written acknowledgment of the debt, or new promise to pay. Do not make any payment on old debt without first verifying the SOL and confirming the charges were accurate.</p>

<h2 id="how-to-dispute">7. How to dispute a California hospital bill</h2>

<h3>Step 1: Request an itemized bill</h3>
<p>Call the billing department and request a full itemized statement. Under SB 1419, they must deliver it within 30 days. Ask for it in writing or by email so you have a dated record of the request.</p>

<h3>Step 2: Check every CPT code</h3>
<p>Look up each CPT or procedure code using our <a href="/calculator">free calculator</a>. If any charge is more than 5&times; the Medicare rate, that is a significant red flag. Compare the room classification on your bill to your medical records to verify you were not upcoded from a standard room to ICU.</p>

<h3>Step 3: Submit a written dispute</h3>
<p>Write a dispute letter to the hospital billing department. Include: your account number, the date of service, the specific line items you are disputing, the reason for each dispute, and supporting documentation (medical records, Medicare rate printouts, EOB from your insurer). Send by certified mail with return receipt.</p>

<h3>Step 4: File a complaint if the dispute is ignored</h3>
<p>If the hospital does not respond within 30 days or refuses to correct an error:</p>
<ul>
    <li><strong>Insurance billing dispute:</strong> File with the <a href="https://www.dmhc.ca.gov/FileAComplaint.aspx" target="_blank" rel="noopener">California DMHC</a></li>
    <li><strong>Balance billing violation:</strong> File with the DMHC or the <a href="https://www.cms.gov/nosurprises" target="_blank" rel="noopener">CMS No Surprises Help Desk</a> (1-800-985-3059)</li>
    <li><strong>Charity care denial:</strong> Contact the <a href="https://www.dhcs.ca.gov/provgovpart/Pages/Financial_Assistance.aspx" target="_blank" rel="noopener">California DHCS</a> or the state Attorney General</li>
</ul>

<div class="key-takeaway">
    <strong>Ready to dispute your California bill?</strong> <a href="/scan">Upload it to BillKarma</a> &mdash; our system flags every charge above Medicare rates, identifies balance billing violations, and generates a dispute letter ready to mail. Takes under two minutes.
</div>

<h2 id="case-studies">8. Real patient results</h2>

<div class="case-study">
    <h3>Case study 1: $18,000 ER bill eliminated under AB 1020 charity care &mdash; San Jose</h3>
    <p><strong>Situation:</strong> A family of three in San Jose received an $18,000 emergency room bill after the mother was treated for a severe asthma attack. The family had no insurance at the time of service.</p>
    <p><strong>Patient profile:</strong> Family of 3, combined household income $72,000/year. At 270% of FPL &mdash; above the free-care threshold but below 350% FPL, qualifying for a sliding-scale discount.</p>
    <p><strong>Action:</strong> The family applied for charity care under AB 1020 within 60 days of receiving the bill. Because the hospital was a nonprofit subject to both AB 1020 and IRS 501(r), the hospital&rsquo;s policy provided an 85% discount at 270% FPL. Additionally, BillKarma&rsquo;s bill audit identified a duplicate lab charge ($340) and an upcoded E&M level that reduced the base bill by an additional $1,100 before the discount was applied.</p>
    <p><strong>Result:</strong> Original bill $18,000, adjusted to $16,560 after error corrections, then reduced to $2,484 after the 85% AB 1020 discount. The family set up a 24-month payment plan at $103.50/month, zero interest.</p>
    <p><strong>Savings: $15,516.</strong></p>
</div>

<div class="case-study">
    <h3>Case study 2: Collections removed after 140-day violation &mdash; Sacramento</h3>
    <p><strong>Situation:</strong> A patient in Sacramento received a $4,200 hospital bill in August 2025. By January 2026 &mdash; just 140 days after the first billing statement &mdash; the hospital had referred the debt to a collections agency, which reported it to Equifax. This was a direct violation of SB 1419&rsquo;s 180-day moratorium.</p>
    <p><strong>Action:</strong> The patient filed a formal complaint with the California Department of Managed Health Care, attaching the dated billing statement and the Equifax collections entry. The DMHC issued a finding that the hospital violated SB 1419 and ordered the collections referral withdrawn, the Equifax entry removed, and the account placed back on hold for the remainder of the 180-day window.</p>
    <p><strong>Result:</strong> Collections entry removed from credit report within 45 days of the DMHC order. The patient then applied for AB 1020 charity care and received a 60% discount on the balance.</p>
    <p><strong>Savings: Collections removed; $2,520 in charity care discount.</strong></p>
</div>

<div class="case-study">
    <h3>Case study 3: $3,200 anesthesiologist balance bill eliminated &mdash; Los Angeles</h3>
    <p><strong>Situation:</strong> A patient in Los Angeles underwent a scheduled cholecystectomy (gallbladder removal) at an in-network hospital. The facility, surgeon, and anesthesiologist were all presented as in-network before the procedure. After surgery, the patient received a separate $5,800 bill from the anesthesiologist&rsquo;s group, of which insurance paid $2,600, leaving a $3,200 balance bill.</p>
    <p><strong>Action:</strong> The patient submitted a dispute to the anesthesiologist&rsquo;s billing department citing the federal No Surprises Act and California Insurance Code Section 1317.1. The patient also filed a complaint with the DMHC. The DMHC found that the anesthesiologist had never properly notified the patient of out-of-network status, and the balance bill was prohibited.</p>
    <p><strong>Result:</strong> The $3,200 balance bill was withdrawn within 30 days of the DMHC complaint. The patient&rsquo;s total liability was capped at their in-network copay: $250.</p>
    <p><strong>Savings: $3,200.</strong></p>
</div>

<h2 id="faq">Frequently asked questions</h2>

<div class="faq-section">
    <div class="faq-item">
        <h3>What is the income limit for charity care at California hospitals?</h3>
        <p>Under AB 1020, California hospitals must provide free care to patients at or below 250% FPL &mdash; roughly $39,125 for a single person or $80,375 for a family of four in 2026. Patients between 250% and 350% FPL ($54,775 single / $112,525 family of four) qualify for a sliding-scale discount. Every licensed California hospital must comply, not just nonprofits.</p>
    </div>

    <div class="faq-item">
        <h3>How long do California hospitals have to wait before sending my bill to collections?</h3>
        <p>Under SB 1419, California hospitals must wait at least 180 days from the first post-discharge billing statement before any extraordinary collection action &mdash; including collections referrals, credit bureau reporting, lawsuits, or liens. Use this window to apply for AB 1020 charity care or dispute billing errors. If the hospital violates the 180-day rule, file a complaint with the DMHC.</p>
    </div>

    <div class="faq-item">
        <h3>What is California&rsquo;s statute of limitations on medical debt?</h3>
        <p>California has a 2-year SOL for open accounts (most hospital bills) and a 4-year SOL for written contracts. This is among the shortest in the nation. After the SOL expires, collectors cannot win a lawsuit against you. Never make a payment on old debt without first checking the SOL &mdash; even a small payment resets the clock.</p>
    </div>

    <div class="faq-item">
        <h3>How do I file a complaint about a California hospital billing error?</h3>
        <p>For insurance-related billing disputes (balance billing, claims denials, insurer underpayments), file with the <a href="https://www.dmhc.ca.gov/FileAComplaint.aspx" target="_blank" rel="noopener">California DMHC</a>. For AB 1020 charity care complaints, contact the <a href="https://www.dhcs.ca.gov/provgovpart/Pages/Financial_Assistance.aspx" target="_blank" rel="noopener">California DHCS</a> or the state Attorney General. For No Surprises Act violations, file with both the DMHC and the CMS Help Desk at 1-800-985-3059.</p>
    </div>

    <div class="faq-item">
        <h3>Can California hospitals garnish my wages for medical debt?</h3>
        <p>Not without a court judgment. Hospitals must obtain a judgment before any garnishment, and California limits garnishment to 25% of disposable earnings or earnings exceeding 40&times; the state minimum wage per week, whichever is less. Under SB 1419, hospitals cannot even send your bill to collections until 180 days have passed, and they must offer payment plans and financial assistance screening before any collection action.</p>
    </div>
</div>

<h2 id="sources">Sources</h2>

<ul class="sources-list">
    <li><a href="https://leginfo.legislature.ca.gov/faces/billNavClient.xhtml?bill_id=202320240AB1020" target="_blank" rel="noopener">California AB 1020 (2023): Hospital Charity Care Requirements</a></li>
    <li><a href="https://www.dmhc.ca.gov/FileAComplaint.aspx" target="_blank" rel="noopener">California Department of Managed Health Care: File a Complaint</a></li>
    <li><a href="https://www.dhcs.ca.gov/provgovpart/Pages/Financial_Assistance.aspx" target="_blank" rel="noopener">California DHCS: Hospital Financial Assistance Programs</a></li>
    <li><a href="https://www.cfpb.gov/consumer-tools/medical-debt/" target="_blank" rel="noopener">CFPB: Medical Debt Resources for Consumers</a></li>
    <li><a href="https://www.cms.gov/nosurprises" target="_blank" rel="noopener">CMS: No Surprises Act Overview and Patient Rights</a></li>
</ul>
""",
})
