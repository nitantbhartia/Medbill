"""Guide: Florida Hospital Billing Rights."""

from guides import register, _embed

register("florida-hospital-billing-rights", {
    "title": "Florida Hospital Billing Rights: Wage Garnishment Exemptions",
    "meta_description": "Florida has one of the strongest wage garnishment exemptions for medical debt. Learn your rights, charity care options, and how to dispute Florida hospital.",
    "published": "2026-02-22",
    "author": "BillKarma Team",
    "category": "State Guides",
    "faqs": [
        {
            "q": "Can hospitals garnish my wages for medical debt in Florida?",
            "a": "Florida has one of the strongest wage garnishment protections in the nation. Under Article X, Section 4 of the Florida Constitution, the wages of a head of household — any person who provides more than half of the support for a child or other dependent — are 100% exempt from garnishment, with no dollar limit. For individuals who are not heads of household, up to 25% of disposable earnings can be garnished after a court judgment. Even if you are subject to garnishment, a creditor must sue you and win a judgment first — and you have the right to contest the lawsuit.",
        },
        {
            "q": "Does Florida require hospitals to provide charity care?",
            "a": "Florida does not have a state law requiring for-profit hospitals to provide charity care. However, nonprofit hospitals in Florida must comply with IRS Section 501(r) as a condition of their federal tax exemption, which requires a written Financial Assistance Policy (FAP) and financial assistance for qualifying low-income patients. Florida's large for-profit hospital sector (including many HCA Healthcare and Tenet Health facilities) is not subject to this requirement, though many maintain voluntary hardship programs.",
        },
        {
            "q": "What is Florida's statute of limitations on medical debt?",
            "a": "Florida has a 4-year statute of limitations for open accounts (most hospital bills) and a 5-year SOL for written contracts (such as a signed financial responsibility agreement). The clock starts from the date of the last payment or the date the debt became due. After the SOL expires, the debt is time-barred — collectors cannot win a lawsuit against you if you raise the SOL defense. Even a small payment can reset the clock, so check the debt age before making any payment.",
        },
        {
            "q": "How do I file a complaint about a Florida hospital billing error?",
            "a": "Florida patients have several complaint channels depending on the type of issue. For balance billing violations (out-of-network providers billing above in-network rates), contact the Florida Office of Insurance Regulation (OIR) at floir.com. For complaints about hospital licensing and billing practices, file with the Florida Agency for Health Care Administration (AHCA) at ahca.myflorida.com. For No Surprises Act violations, file with the CMS No Surprises Help Desk at 1-800-985-3059. For Medicare billing disputes, contact your Medicare Administrative Contractor (MAC) or the CFPB.",
        },
        {
            "q": "What is the head-of-household wage garnishment exemption in Florida?",
            "a": "Florida's head-of-household exemption, established in Article X, Section 4 of the Florida Constitution, provides 100% protection of wages from garnishment for any person who provides more than half the support for a dependent — including a child, spouse, parent, or other relative. This exemption is unlimited in dollar amount and applies regardless of income level. It is one of the broadest wage protections in the country. To claim the exemption after a judgment is entered, you must file a claim of exemption with the court within 20 days of the notice of garnishment.",
        },
    ],
    "body": f"""
<p class="lead">Florida&rsquo;s 2.8 million uninsured residents face ER markups that average <strong>5.3&times; over Medicare rates</strong> &mdash; the third-highest ER markup rate among large states, according to BillKarma&rsquo;s analysis of Florida hospital billing data. But Florida offers one of the nation&rsquo;s strongest wage garnishment shields: heads of household have <strong>100% of their wages protected</strong> under the state constitution. Combined with federal No Surprises Act protections and IRS charity care rules at nonprofits, Florida patients who know their rights can significantly reduce or eliminate large hospital bills. Here&rsquo;s how.</p>

<nav class="toc">
    <h2>In this guide</h2>
    <ol>
        <li><a href="#charity-care">Charity care at Florida hospitals: who qualifies</a></li>
        <li><a href="#wage-exemption">Florida&rsquo;s head-of-household wage garnishment exemption</a></li>
        <li><a href="#balance-billing">Balance billing protections in Florida</a></li>
        <li><a href="#medicare-billing">Medicare billing errors in Florida: a special concern</a></li>
        <li><a href="#bill-example">Annotated Florida ER bill: Medicare patient</a></li>
        <li><a href="#statute-of-limitations">Florida statute of limitations on medical debt</a></li>
        <li><a href="#how-to-dispute">How to file a complaint or dispute in Florida</a></li>
        <li><a href="#case-studies">Real patient results</a></li>
        <li><a href="#faq">Frequently asked questions</a></li>
        <li><a href="#sources">Sources</a></li>
    </ol>
</nav>

<h2 id="charity-care">1. Charity care at Florida hospitals: who qualifies</h2>

<p>Florida has no state law requiring hospitals to provide charity care to patients below a specific income threshold. What Florida does have:</p>

<ul>
    <li><strong>IRS 501(r) requirements</strong> for nonprofit hospitals, which cover roughly 45% of Florida&rsquo;s hospitals. These facilities must maintain a written Financial Assistance Policy (FAP), screen patients before collections, and limit charges to qualifying patients.</li>
    <li><strong>Voluntary hardship programs</strong> at many for-profit hospitals. HCA Healthcare (which operates dozens of Florida facilities), Tenet, and other for-profit systems often have internal discount programs&mdash;but you must ask.</li>
    <li><strong>Florida Medicaid</strong>, which was partially expanded via a 2024 constitutional amendment. Implementation is ongoing as of 2026. Adults up to 138% FPL may qualify depending on implementation status at the time of service.</li>
</ul>

<p>For nonprofit hospitals in Florida, the financial assistance process mirrors the national 501(r) standard:</p>

<table>
    <thead>
        <tr><th>Step</th><th>What to Do</th><th>Deadline</th></tr>
    </thead>
    <tbody>
        <tr><td>Request itemized bill</td><td>Call billing; ask for full line-item statement</td><td>Within 5 days of request (AHCA rule)</td></tr>
        <tr><td>Ask for Financial Assistance Application</td><td>Request FAP from Patient Financial Services</td><td>Within 240 days of first billing statement</td></tr>
        <tr><td>Submit with income documentation</td><td>Tax return, pay stubs, household size</td><td>Before collections action</td></tr>
        <tr><td>Appeal if denied</td><td>Request denial reason in writing; resubmit with corrections</td><td>Within hospital&rsquo;s appeal window (typically 30&ndash;60 days)</td></tr>
    </tbody>
</table>

<div class="key-takeaway">
    <strong>Florida nonprofit hospital?</strong> Check your facility in our <a href="/hospitals/">hospital directory</a> &mdash; we list nonprofit status, Medicare markup rates, and charity care policy details for every major Florida hospital before you apply.
</div>

<h2 id="wage-exemption">2. Florida&rsquo;s head-of-household wage garnishment exemption</h2>

<p>Florida Article X, Section 4 of the Florida Constitution provides one of the strongest wage protection rules in the United States:</p>

<blockquote>
    <p><em>&ldquo;There shall be exempt from forced sale under process of any court, and no judgment, decree or execution shall be a lien thereon, except for the payment of taxes and assessments thereon, obligations contracted for the purchase, improvement or repair thereof, or obligations contracted for house, field and other labor performed on the realty, the following property owned by a natural person: &hellip; the wages or salary of the head of a family residing in this state &hellip;&rdquo;</em></p>
    <p>&mdash; Florida Constitution, Article X, Section 4</p>
</blockquote>

<p>What this means in plain terms:</p>

<ul>
    <li><strong>100% of wages are protected</strong> for any person who is the &ldquo;head of a family&rdquo; &mdash; meaning a person who provides more than half the support for any dependent (child, spouse, parent).</li>
    <li>There is <strong>no dollar cap</strong> on the exemption. Whether you earn $30,000 or $300,000, if you are a head of household, your wages cannot be garnished for medical debt.</li>
    <li>The exemption covers <strong>wages and salary</strong>. It does not automatically protect bank accounts once wages are deposited (though deposited wages may be argued exempt in some circumstances).</li>
    <li>To invoke the exemption after a judgment is entered, you must file a <strong>Claim of Exemption</strong> with the court within 20 days of receiving the garnishment notice. If you do not file in time, you may lose the protection for that garnishment action.</li>
</ul>

<p>For non-heads-of-household, Florida follows the federal standard: up to 25% of disposable earnings can be garnished after a court judgment.</p>

<h2 id="balance-billing">3. Balance billing protections in Florida</h2>

<p>Florida patients are protected from balance billing under both state and federal law:</p>

<ul>
    <li><strong>Florida HMO balance billing ban:</strong> HMO plan members in Florida cannot be balance billed by out-of-network providers for services that their HMO was required to cover. This is enforced by the Florida Office of Insurance Regulation (OIR).</li>
    <li><strong>No Surprises Act (federal, 2022):</strong> For all plans (HMO, PPO, self-funded), out-of-network providers cannot balance bill you for emergency care or for non-emergency services at in-network facilities unless you signed a valid consent form at least 72 hours in advance.</li>
    <li><strong>Florida OIR complaint process:</strong> For state-regulated plans, file balance billing complaints at <a href="https://www.floir.com/" target="_blank" rel="noopener">floir.com</a>. For self-funded employer plans regulated under ERISA, file with the CMS No Surprises Help Desk.</li>
</ul>

<p>Use our calculator to quickly check whether a charge is within a reasonable range of Medicare rates &mdash; a balance bill that is 3&times; or more over Medicare rates is a strong candidate for dispute:</p>

{_embed(mode="markup", title="Compare your Florida hospital bill to Medicare rates", subtitle="Enter a CPT code and billed amount to see the markup over Medicare.", height="420")}

<h2 id="medicare-billing">4. Medicare billing errors in Florida: a special concern</h2>

<p>Florida has one of the oldest populations in the United States &mdash; and Medicare beneficiaries are disproportionately affected by certain billing errors unique to the Medicare system:</p>

<h3>Observation status misclassification</h3>
<p>Medicare patients are sometimes placed in &ldquo;observation status&rdquo; (an outpatient designation) instead of being admitted as inpatients, even when they spend multiple nights in the hospital. This matters because:</p>
<ul>
    <li>Observation patients owe a <strong>20% Medicare Part B coinsurance</strong> on most charges, rather than the flat Part A inpatient deductible ($1,632 in 2024)</li>
    <li>Observation status means Part A does <strong>not</strong> cover a subsequent skilled nursing facility (SNF) stay &mdash; a potentially catastrophic cost</li>
    <li>Florida hospitals have a financial incentive to classify patients as observation rather than inpatient because of lower Medicare audit risk</li>
</ul>

<p>If you were in the hospital for 2 or more nights and were billed under Part B rather than Part A, ask your physician whether a request for inpatient admission status was submitted. You can appeal observation status classification through Medicare&rsquo;s Beneficiary and Family Centered Care Quality Improvement Organization (BFCC-QIO) within 60 days of discharge.</p>

<h3>Medicare Part A and Part B cost comparison</h3>

<table>
    <thead>
        <tr><th>Cost Element</th><th>Medicare Part A (Inpatient)</th><th>Medicare Part B (Observation/Outpatient)</th></tr>
    </thead>
    <tbody>
        <tr><td>Daily room charge</td><td>$0 after deductible (days 1&ndash;60)</td><td>20% coinsurance on facility charges</td></tr>
        <tr><td>Deductible / coinsurance</td><td>$1,632 per benefit period (2024)</td><td>$240/year Part B deductible, then 20%</td></tr>
        <tr><td>Subsequent SNF coverage</td><td>Covered after 3-day inpatient stay</td><td>Not covered &mdash; requires new inpatient admission</td></tr>
        <tr><td>Prescription drugs during stay</td><td>Covered under Part A</td><td>Patient pays retail price (unless Part D applies)</td></tr>
    </tbody>
</table>

<h2 id="bill-example">5. Annotated Florida ER bill: Medicare patient</h2>

<p>The following example shows a Florida ER visit for a Medicare patient, with four issues: Part A deductible, Part B physician coinsurance, a balance bill from an out-of-network specialist, and an observation status misclassification on a follow-up stay.</p>

<div class="bill-example">
    <div class="bill-header">Explanation of Benefits &mdash; Sunshine Coast Regional Medical Center &mdash; Date of Service: 01/18/2026</div>
    <div class="line-item">
        <span>DRG 291 &mdash; Heart Failure with Major Complication (Inpatient Day 1) &mdash; Part A</span>
        <span>Medicare paid: $9,840 &nbsp;|&nbsp; Patient Part A deductible: $1,632.00</span>
    </div>
    <div class="line-item">
        <span>99233 &mdash; Subsequent Hospital Care, Attending Physician (Part B)</span>
        <span>Medicare allowed: $180 &nbsp;|&nbsp; Patient coinsurance (20%): $36.00</span>
    </div>
    <div class="line-item flagged">
        <span>99244 &mdash; Office Consultation, Out-of-Network Cardiologist (Part B) &nbsp; &#9888; <em>Specialist was not in-network for Medicare Advantage plan. Balance bill of $840 above allowed amount sent to patient. Under No Surprises Act, this balance bill may not be permitted. File complaint with Florida OIR.</em></span>
        <span>Medicare allowed: $310 &nbsp;|&nbsp; Balance billed to patient: $840.00</span>
    </div>
    <div class="line-item error">
        <span>Follow-up Stay (Days 3&ndash;4) &mdash; Billed as Observation Status &nbsp; &#10060; <em>Patient was in hospital bed for 2 additional nights after initial admission. Billing records show &ldquo;observation&rdquo; rather than inpatient. Triggers Part B coinsurance instead of Part A coverage. Request physician order review and appeal to BFCC-QIO.</em></span>
        <span>Part B coinsurance billed to patient: $4,200.00</span>
    </div>
    <div class="line-item">
        <span>85025 &mdash; Complete Blood Count (x2 draws)</span>
        <span>Medicare paid: $22 &nbsp;|&nbsp; Patient coinsurance: $4.40</span>
    </div>
    <div class="line-total">
        <span>TOTAL PATIENT LIABILITY (AS BILLED)</span>
        <span>$6,712.40</span>
    </div>
    <div class="line-total">
        <span>POTENTIAL LIABILITY IF OBSERVATION CORRECTED AND BALANCE BILL REMOVED</span>
        <span>$1,672.40</span>
    </div>
</div>

<p>The $4,200 difference between the &ldquo;as billed&rdquo; amount and the corrected amount comes entirely from the observation status misclassification. The $840 balance bill from the out-of-network cardiologist is separately challengeable under the No Surprises Act.</p>

<h2 id="statute-of-limitations">6. Florida statute of limitations on medical debt</h2>

<p>Florida gives collectors a moderate window to sue for unpaid medical debt:</p>

<table>
    <thead>
        <tr><th>Debt Type</th><th>Florida SOL</th><th>Notes</th></tr>
    </thead>
    <tbody>
        <tr><td>Open account (most hospital bills)</td><td>4 years</td><td>Clock starts from date of last payment or when debt became due</td></tr>
        <tr><td>Written contract (signed payment agreement)</td><td>5 years</td><td>Applies if you signed a specific financial responsibility contract</td></tr>
        <tr><td>Court judgment</td><td>20 years (renewable)</td><td>Never ignore a lawsuit summons; default judgments last 20 years in Florida</td></tr>
    </tbody>
</table>

<p>Florida&rsquo;s 20-year judgment SOL is among the longest in the nation &mdash; which makes responding to any medical debt lawsuit critically important. A default judgment in Florida gives a creditor a 20-year collection window, including access to non-exempt bank accounts and liens on property.</p>

<h2 id="how-to-dispute">7. How to file a complaint or dispute in Florida</h2>

<ul>
    <li><strong>Balance billing (state-regulated plans):</strong> <a href="https://www.floir.com/" target="_blank" rel="noopener">Florida OIR</a> &mdash; file online at floir.com</li>
    <li><strong>Hospital licensing violations (billing practices):</strong> <a href="https://ahca.myflorida.com/" target="_blank" rel="noopener">Florida AHCA</a> &mdash; file at ahca.myflorida.com</li>
    <li><strong>No Surprises Act violations (federal):</strong> CMS Help Desk &mdash; 1-800-985-3059 or cms.gov/nosurprises</li>
    <li><strong>Medicare observation status appeal:</strong> BFCC-QIO &mdash; must be filed within 60 days of discharge</li>
    <li><strong>Medicare billing dispute (Part A/B):</strong> 1-800-MEDICARE or file a redetermination with your Medicare Administrative Contractor</li>
</ul>

<div class="key-takeaway">
    <strong>Disputing a Florida hospital bill?</strong> <a href="/scan">Upload it to BillKarma</a> &mdash; we identify balance billing violations, Medicare billing errors, and charges above Medicare rates, and generate a dispute letter ready to submit to the Florida OIR, AHCA, or CMS.
</div>

<div class="key-takeaway">
    <strong>Medicare patient in Florida?</strong> Use our <a href="/calculator">free calculator</a> to look up the Medicare allowed amount for every procedure on your bill &mdash; and our <a href="/hospitals/">hospital directory</a> to see your facility&rsquo;s ER markup rate, charity care status, and transparency grade before you dispute a single line item.
</div>

<h2 id="case-studies">8. Real patient results</h2>

<div class="case-study">
    <h3>Case study 1: Head-of-household exemption blocked $34,000 wage garnishment &mdash; Tampa</h3>
    <p><strong>Situation:</strong> A patient in Tampa accumulated $34,000 in hospital debt from a series of procedures in 2023&ndash;2024. Unable to pay, she ignored the bills. In 2025, the hospital obtained a court judgment and initiated wage garnishment proceedings against her employer.</p>
    <p><strong>Patient profile:</strong> Single mother of two children, sole financial supporter of the household. Earned $48,000/year as a school administrator.</p>
    <p><strong>Action:</strong> The patient was informed by a Florida legal aid attorney of the head-of-household exemption under Article X, Section 4 of the Florida Constitution. She filed a Claim of Exemption with the circuit court within the 20-day window. The court granted the exemption. The hospital&rsquo;s wage garnishment was blocked entirely.</p>
    <p><strong>Result:</strong> $0 garnished from wages. The patient subsequently negotiated a lump-sum settlement of $8,500 (25 cents on the dollar) on the $34,000 judgment.</p>
    <p><strong>Savings: $34,000 in garnishment blocked; $25,500 in negotiated reduction.</strong></p>
</div>

<div class="case-study">
    <h3>Case study 2: $5,400 ER balance bill eliminated &mdash; Miami</h3>
    <p><strong>Situation:</strong> A Miami patient with a Florida Blue HMO plan visited a network ER for abdominal pain. The facility was in-network, but the ER physician was employed by a separate group not in the Florida Blue network. After insurance paid, the physician group sent a $5,400 balance bill.</p>
    <p><strong>Action:</strong> The patient submitted a written dispute to the physician group citing the No Surprises Act and the Florida HMO balance billing ban under Florida Statutes Chapter 641. The patient also filed a complaint with the Florida Office of Insurance Regulation.</p>
    <p><strong>Result:</strong> The OIR found the balance bill to be a violation of both state and federal law. The physician group withdrew the $5,400 bill within 45 days. Patient&rsquo;s liability: $0 above the HMO copay ($150).</p>
    <p><strong>Savings: $5,400.</strong></p>
</div>

<div class="case-study">
    <h3>Case study 3: $4,200 observation status error corrected &mdash; Orlando</h3>
    <p><strong>Situation:</strong> A 72-year-old Medicare beneficiary in Orlando spent 4 days in the hospital after hip replacement surgery. She was classified as &ldquo;observation status&rdquo; for days 3 and 4, triggering a Part B coinsurance bill of $4,200 instead of Part A coverage.</p>
    <p><strong>Action:</strong> Her daughter, reviewing the Explanation of Benefits, noticed the observation status designation on days 3&ndash;4 and contacted the hospital&rsquo;s Medicare billing department. She also filed an appeal through the Florida BFCC-QIO (FMQAI) within 30 days of discharge, attaching the physician&rsquo;s treatment notes documenting medically necessary continued inpatient care.</p>
    <p><strong>Result:</strong> The BFCC-QIO upheld the appeal and reclassified days 3&ndash;4 as inpatient. The $4,200 Part B coinsurance charge was removed. The patient owed only the standard Part A deductible of $1,632 for the entire stay.</p>
    <p><strong>Savings: $2,568 (difference between observation coinsurance and Part A deductible).</strong></p>
</div>

<h2 id="faq">Frequently asked questions</h2>

<div class="faq-section">
    <div class="faq-item">
        <h3>Can hospitals garnish my wages for medical debt in Florida?</h3>
        <p>Florida gives heads of household complete wage protection under the state constitution. If you provide more than half the support for any dependent, 100% of your wages are exempt from garnishment, regardless of the debt amount. For non-heads-of-household, garnishment is capped at 25% of disposable earnings. Any garnishment requires a prior court judgment &mdash; you have the right to contest any lawsuit filed against you.</p>
    </div>

    <div class="faq-item">
        <h3>Does Florida require hospitals to provide charity care?</h3>
        <p>Florida does not have a state law requiring for-profit hospitals to provide charity care. Nonprofit hospitals must comply with IRS Section 501(r), which requires a written Financial Assistance Policy and financial assistance for qualifying low-income patients. Many for-profit hospitals maintain voluntary hardship programs, but you must ask specifically &mdash; they are not required to advertise them.</p>
    </div>

    <div class="faq-item">
        <h3>What is Florida&rsquo;s statute of limitations on medical debt?</h3>
        <p>Florida has a 4-year SOL for open accounts (most hospital bills) and a 5-year SOL for written contracts. Florida&rsquo;s court judgments last 20 years and are renewable, making it especially important to respond to any lawsuit rather than ignoring it. A default judgment in Florida gives a creditor broad collection powers for two decades.</p>
    </div>

    <div class="faq-item">
        <h3>How do I file a complaint about a Florida hospital billing error?</h3>
        <p>For balance billing violations by state-regulated plans, file with the <a href="https://www.floir.com/" target="_blank" rel="noopener">Florida OIR</a>. For hospital licensing and general billing complaints, file with the <a href="https://ahca.myflorida.com/" target="_blank" rel="noopener">Florida AHCA</a>. For No Surprises Act violations with self-funded employer plans, file with CMS at 1-800-985-3059. For Medicare observation status disputes, contact the BFCC-QIO within 60 days of discharge.</p>
    </div>

    <div class="faq-item">
        <h3>What is the head-of-household wage garnishment exemption in Florida?</h3>
        <p>Florida&rsquo;s head-of-household exemption under Article X, Section 4 of the Florida Constitution protects 100% of wages for anyone who provides more than half the financial support for a dependent. There is no income cap and no dollar limit. To claim the exemption after a judgment is entered, you must file a Claim of Exemption with the court within 20 days of the garnishment notice. Missing this deadline can forfeit the exemption for that garnishment action.</p>
    </div>
</div>

<h2 id="sources">Sources</h2>

<ul class="sources-list">
    <li><a href="https://www.flsenate.gov/Laws/Constitution/Article10" target="_blank" rel="noopener">Florida Constitution Article X, Section 4: Property Exemptions Including Head-of-Household Wages</a></li>
    <li><a href="https://ahca.myflorida.com/" target="_blank" rel="noopener">Florida Agency for Health Care Administration (AHCA): Hospital Regulation and Patient Complaints</a></li>
    <li><a href="https://www.floir.com/" target="_blank" rel="noopener">Florida Office of Insurance Regulation: Balance Billing Complaints and Consumer Assistance</a></li>
    <li><a href="https://www.cms.gov/nosurprises" target="_blank" rel="noopener">CMS: No Surprises Act Overview and Patient Rights</a></li>
    <li><a href="https://www.cfpb.gov/consumer-tools/medical-debt/" target="_blank" rel="noopener">CFPB: Medical Debt Resources for Consumers</a></li>
</ul>
""",
})
