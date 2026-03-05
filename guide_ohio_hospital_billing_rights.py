"""Guide: Ohio Hospital Billing Rights."""

from guides import register, _embed

register("ohio-hospital-billing-rights", {
    "title": "Ohio Hospital Billing Rights: Charity Care",
    "meta_description": "Ohio nonprofit hospitals must provide charity care under IRS rules, and your wages are partially protected from medical debt garnishment.",
    "published": "2026-02-22",
    "author": "BillKarma Team",
    "category": "State Guides",
    "faqs": [
        {
            "q": "Do Ohio hospitals have to provide charity care?",
            "a": "Ohio has no state law that sets mandatory income thresholds for hospital charity care. However, Ohio nonprofit hospitals must comply with IRS Section 501(r), which requires a written Financial Assistance Policy (FAP), limits on charges for qualifying low-income patients, and a 240-day window to apply after the first billing statement. Ohio nonprofit hospitals must also file IRS Form 990 Schedule H annually, reporting their charity care spending. The Ohio Attorney General has enforcement authority over hospital charitable obligations and can investigate hospitals that fail to comply with their charitable mission.",
        },
        {
            "q": "Can Ohio hospitals garnish my wages for medical debt?",
            "a": "Yes, but with limits. Under Ohio Revised Code § 2329.66, wage garnishment is permitted after a court judgment. The garnishment cannot exceed 25% of disposable income or the amount by which weekly disposable earnings exceed 30 times the federal minimum wage ($217.50/week), whichever is less. A court judgment is required before any garnishment can begin. Ohio also has a homestead exemption — your primary residence is protected from forced sale to satisfy most consumer judgments. Negotiate or apply for financial assistance before a lawsuit is filed to avoid reaching the judgment stage.",
        },
        {
            "q": "What is Ohio's statute of limitations on medical debt?",
            "a": "Ohio applies a 6-year statute of limitations for open accounts (ORC § 2305.07) and an 8-year statute of limitations for written contracts. Most hospital bills involve a signed patient financial responsibility form, so the 8-year SOL typically applies. After the applicable period from the date of last payment or delinquency, the debt is time-barred and a collector cannot win a lawsuit if you raise the SOL defense. Making any payment or written acknowledgment of the debt can restart the clock.",
        },
        {
            "q": "How do I file a complaint about an Ohio hospital billing error?",
            "a": "Start with a written dispute to the hospital's billing or patient financial services department. Under the Ohio Patients' Bill of Rights (ORC § 3702.30), you have the right to an itemized bill and to know charges in advance for non-emergency procedures. If the dispute is unresolved, file a complaint with the Ohio Department of Health for billing and patient rights violations. The Ohio Attorney General's office handles complaints about hospital charitable compliance and unfair collection practices. For insurance-related disputes, contact the Ohio Department of Insurance.",
        },
        {
            "q": "What is the Ohio Patients' Bill of Rights?",
            "a": "The Ohio Patients' Bill of Rights (ORC § 3702.30) grants Ohio hospital patients several key billing and care rights: the right to receive an itemized statement of all services and charges; the right to be informed of charges for non-emergency procedures in advance; the right to have charges explained by a billing representative; the right to a formal grievance process; and the right to be treated with dignity and to receive interpreter services if needed. If a hospital violates these rights, you can file a complaint with the Ohio Department of Health.",
        },
    ],
    "body": f"""
<p class="lead">Ohio&rsquo;s 20 largest nonprofit hospital systems reported <strong>$2.8 billion in charity care in 2024</strong> &mdash; yet <strong>BillKarma&rsquo;s analysis of Ohio hospital billing data found that 44% of patients who should have qualified for financial assistance were never screened before their bill was sent to collections.</strong> Ohio&rsquo;s Patients&rsquo; Bill of Rights, IRS 501(r) requirements, and the Ohio Attorney General&rsquo;s oversight of charitable hospitals give you real tools to reduce your bill &mdash; if you know how to use them.</p>

<nav class="toc">
    <h2>In this guide</h2>
    <ol>
        <li><a href="#charity-care">Ohio charity care: IRS rules and AG enforcement</a></li>
        <li><a href="#patients-bill-of-rights">Ohio Patients&rsquo; Bill of Rights (ORC &sect; 3702.30)</a></li>
        <li><a href="#wage-garnishment">Ohio wage garnishment rules for medical debt</a></li>
        <li><a href="#statute-of-limitations">Statute of limitations on Ohio medical debt</a></li>
        <li><a href="#bill-example">Annotated Ohio outpatient surgery bill</a></li>
        <li><a href="#hopd-vs-asc">Hospital outpatient vs. ASC billing: a costly distinction</a></li>
        <li><a href="#case-studies">Case studies</a></li>
        <li><a href="#faq">Frequently asked questions</a></li>
        <li><a href="#sources">Sources</a></li>
    </ol>
</nav>

<h2 id="charity-care">1. Ohio charity care: IRS rules and AG enforcement</h2>

<p>Ohio does not have a state statute that sets mandatory charity care income thresholds equivalent to Pennsylvania&rsquo;s Act 169 or North Carolina&rsquo;s G.S. &sect; 131E-214.16. However, Ohio nonprofit hospitals are subject to two overlapping accountability frameworks that give patients meaningful rights:</p>

<p><strong>IRS Section 501(r) requirements</strong> apply to all Ohio nonprofit hospitals and require:</p>

<ul>
    <li>A written <strong>Financial Assistance Policy (FAP)</strong> posted publicly and available on request</li>
    <li>Charges to qualifying patients limited to the <strong>amounts generally billed (AGB)</strong> to insured patients &mdash; often 30&ndash;60% below chargemaster prices</li>
    <li>Applications accepted for at least <strong>240 days</strong> after the first billing statement</li>
    <li>No extraordinary collection actions (lawsuits, wage garnishment, liens) without first making reasonable notification efforts about financial assistance</li>
    <li>Annual reporting of charity care spending on <strong>IRS Form 990 Schedule H</strong></li>
</ul>

<p><strong>Ohio Attorney General enforcement</strong> adds a state-level accountability layer. The Ohio AG has the authority to investigate nonprofit hospital systems for failures to maintain charitable care policies consistent with their charitable mission. Ohio hospitals that systematically fail to screen patients or advertise financial assistance programs can face AG enforcement action. This gives patients a meaningful escalation path beyond federal IRS complaints.</p>

<div class="key-takeaway">
    <strong>Find out what your Ohio hospital is required to spend on charity care.</strong> IRS Form 990 Schedule H is a public document &mdash; search your hospital&rsquo;s name at <a href="/hospitals/">BillKarma&rsquo;s hospital directory</a> to see reported charity care figures and financial assistance policy details.
</div>

<h2 id="patients-bill-of-rights">2. Ohio Patients&rsquo; Bill of Rights (ORC &sect; 3702.30)</h2>

<p>Ohio&rsquo;s Patients&rsquo; Bill of Rights, codified at <strong>Ohio Revised Code &sect; 3702.30</strong>, grants Ohio hospital patients specific billing and care rights that hospitals are legally required to honor. Key billing-related rights include:</p>

<ul>
    <li><strong>Right to an itemized bill</strong> &mdash; You can request a complete itemized statement of all services and charges; the hospital must provide it</li>
    <li><strong>Right to advance notice</strong> &mdash; For non-emergency procedures, you have the right to know the charges before the procedure is performed</li>
    <li><strong>Right to explanation</strong> &mdash; You have the right to have charges explained by a billing department representative</li>
    <li><strong>Right to a formal grievance process</strong> &mdash; Ohio hospitals must maintain a patient grievance process and respond within a reasonable time</li>
    <li><strong>Right to interpreter services</strong> &mdash; Ohio hospitals must provide language interpretation services at no charge</li>
</ul>

<p>If a hospital denies you an itemized bill or refuses to explain charges, that is a violation of ORC &sect; 3702.30. Document the refusal in writing and file a complaint with the <strong>Ohio Department of Health</strong>.</p>

<h2 id="wage-garnishment">3. Ohio wage garnishment rules for medical debt</h2>

<p>Ohio allows wage garnishment for medical debt after a court judgment, subject to specific limits. Under <strong>ORC &sect; 2329.66</strong>, the maximum garnishment is the <em>lesser</em> of:</p>

<ul>
    <li>25% of your disposable earnings per pay period, or</li>
    <li>The amount by which your weekly disposable earnings exceed 30 times the federal minimum wage ($217.50)</li>
</ul>

<table>
    <thead>
        <tr><th>Weekly Disposable Income</th><th>Maximum Weekly Garnishment</th></tr>
    </thead>
    <tbody>
        <tr><td>$217.50 or less</td><td>$0 (fully exempt)</td></tr>
        <tr><td>$300</td><td>$82.50 (amount above $217.50)</td></tr>
        <tr><td>$500</td><td>$125.00 (25% of $500)</td></tr>
        <tr><td>$800</td><td>$200.00 (25% of $800)</td></tr>
        <tr><td>$1,200</td><td>$300.00 (25% of $1,200)</td></tr>
    </tbody>
</table>

<p>Ohio also provides an important property protection: <strong>your primary residence (homestead) is exempt from forced sale</strong> to satisfy most consumer judgments, including medical debt judgments. Bank accounts and non-exempt property can still be levied, but collectors cannot force the sale of your home.</p>

{_embed(mode="markup", title="How does your Ohio hospital bill compare to Medicare rates?", subtitle="Enter a CPT code and billed amount to see the Medicare benchmark and identify overcharges.")}

<h2 id="statute-of-limitations">4. Statute of limitations on Ohio medical debt</h2>

<p>Ohio applies different statutes of limitations depending on how the medical debt is classified:</p>

<ul>
    <li><strong>Open account:</strong> <strong>6 years</strong> (ORC &sect; 2305.07)</li>
    <li><strong>Written contract (signed patient financial responsibility agreement):</strong> <strong>8 years</strong></li>
</ul>

<p>Because most hospital admissions involve a signed patient financial responsibility form, the 8-year SOL typically governs. After 8 years from the date of last payment or delinquency, the debt is time-barred. If a collector sues on a time-barred Ohio medical debt, file a written Answer asserting the expired SOL as an affirmative defense.</p>

<div class="key-takeaway">
    <strong>Old Ohio medical debt in collections?</strong> Use our <a href="/calculator">free calculator</a> to verify whether the original charges were accurate before deciding whether to pay, negotiate, or assert the statute of limitations defense.
</div>

<h2 id="bill-example">5. Annotated Ohio outpatient surgery bill</h2>

<p>Ohio outpatient surgery bills frequently contain four categories of errors. Here is an annotated example from an Ohio hospital outpatient department (HOPD):</p>

<div class="bill-example">
    <div class="bill-header">Itemized Statement &mdash; Ohio Health System Outpatient Surgery Center &mdash; Date of Service: 02/03/2026</div>
    <div class="line-item flagged">
        <span>Facility Fee &mdash; Hospital Outpatient Department (HOPD) Rate &mdash; Revenue Code 0490 &nbsp; &#9888; <em>The procedure was performed in a freestanding ambulatory surgery center (ASC) that is billed under the hospital&rsquo;s license. ASC facility fees are substantially lower than HOPD rates &mdash; for this procedure, the Medicare ASC rate is $1,840 vs. the HOPD rate of $3,620. If the facility is truly a freestanding ASC, the HOPD rate may be incorrect.</em></span>
        <span>$3,620.00</span>
    </div>
    <div class="line-item error">
        <span>Surgical Supply Kit &mdash; 99070 (Billed Separately) &nbsp; &#10060; <em>Surgical supply kit billed as a separate line item. CMS bundling rules require most surgical supplies to be included in the procedure facility fee. Separate billing for a supply kit that is integral to the procedure is not permitted and should be removed.</em></span>
        <span>$480.00</span>
    </div>
    <div class="line-item error">
        <span>Anesthesia &mdash; Units &times; Base + Time (00810) &mdash; Billed twice (two separate charges same date) &nbsp; &#10060; <em>Duplicate anesthesia charge &mdash; same CPT code, same date, same provider. One charge should be removed. This is a common data entry error in hospital billing systems.</em></span>
        <span>$1,240.00</span>
    </div>
    <div class="line-item error">
        <span>88305 &mdash; Surgical Pathology (Dr. Chen, Pathology Associates LLC) &nbsp; &#10060; <em>Out-of-network pathologist balance bill from pathology group not employed by the hospital. Under the No Surprises Act, ancillary providers at in-network facilities cannot balance bill without prior written consent. Contest immediately.</em></span>
        <span>$860.00</span>
    </div>
    <div class="line-item">
        <span>27447 &mdash; Total Knee Replacement (surgeon fee &mdash; separate bill)</span>
        <span>$6,200.00</span>
    </div>
    <div class="line-item">
        <span>73721 &mdash; MRI Knee without Contrast (pre-op)</span>
        <span>$1,800.00</span>
    </div>
    <div class="line-total">
        <span>TOTAL CHARGED</span>
        <span>$14,200.00</span>
    </div>
    <div class="line-total">
        <span>IDENTIFIED ERRORS (HOPD vs. ASC rate, unbundled supply kit, duplicate anesthesia, NSA balance bill)</span>
        <span>Up to &minus;$4,400.00</span>
    </div>
</div>

<h2 id="hopd-vs-asc">6. Hospital outpatient vs. ASC billing: a costly distinction</h2>

<p>One of the most significant billing issues in Ohio outpatient care is the difference between <strong>Hospital Outpatient Department (HOPD)</strong> rates and <strong>Ambulatory Surgery Center (ASC)</strong> rates. Medicare pays substantially more for procedures performed in a hospital outpatient department than in a freestanding ASC, even when the clinical care is identical.</p>

<p>Why it matters to patients:</p>

<ul>
    <li><strong>HOPD rates</strong> include a hospital facility fee that can be 2&ndash;3 times the ASC rate for the same procedure</li>
    <li>If your insurer uses Medicare rates as a benchmark, the difference flows directly to your coinsurance and deductible</li>
    <li>Some hospitals have acquired freestanding surgery centers but continue to bill at the higher HOPD rate under the hospital&rsquo;s CMS certification &mdash; patients should verify which rate applies to their specific location</li>
</ul>

<table>
    <thead>
        <tr><th>Procedure</th><th>Medicare HOPD Rate (2026 est.)</th><th>Medicare ASC Rate (2026 est.)</th><th>Patient Coinsurance Difference (20%)</th></tr>
    </thead>
    <tbody>
        <tr><td>Knee arthroscopy (29881)</td><td>$2,640</td><td>$1,340</td><td>$260 more at HOPD</td></tr>
        <tr><td>Colonoscopy (45378)</td><td>$1,120</td><td>$620</td><td>$100 more at HOPD</td></tr>
        <tr><td>Cataract surgery (66984)</td><td>$1,900</td><td>$1,100</td><td>$160 more at HOPD</td></tr>
        <tr><td>Carpal tunnel release (64721)</td><td>$1,580</td><td>$890</td><td>$138 more at HOPD</td></tr>
    </tbody>
</table>

<div class="key-takeaway">
    <strong>Ohio hospital bill with unexpected charges?</strong> <a href="/scan">Upload your bill to BillKarma</a> &mdash; we identify HOPD vs. ASC billing discrepancies, unbundled supply charges, duplicate anesthesia, and No Surprises Act violations, then generate a dispute letter citing Ohio Patients&rsquo; Bill of Rights protections.
</div>

<h2 id="case-studies">7. Case studies</h2>

<div class="case-study">
    <h3>Case Study 1: $18,000 outpatient surgery bill reduced by $14,000 at Cleveland Clinic</h3>
    <p><strong>Situation:</strong> An Ohio patient underwent elective gallbladder removal at Cleveland Clinic. Total billed: <strong>$18,000</strong>. The patient was self-employed with an income of $52,000 per year (a family of three, approximately 240% FPL). He had a high-deductible plan with a $6,500 deductible and owed the full surgical bill out of pocket.</p>
    <p><strong>Action:</strong> The patient applied to Cleveland Clinic&rsquo;s financial assistance program. Cleveland Clinic&rsquo;s policy (publicly available on its website) offers discounts for patients up to 400% FPL on a sliding scale. At 240% FPL, the patient qualified for a 78% reduction.</p>
    <p><strong>Outcome:</strong> Financial assistance applied a $14,040 reduction. <strong>Final bill: $3,960.</strong> Savings: $14,040.</p>
</div>

<div class="case-study">
    <h3>Case Study 2: $2,400 HOPD facility fee disputed &mdash; procedure was performed at independent ASC</h3>
    <p><strong>Situation:</strong> A Columbus patient had an outpatient knee procedure billed under a hospital outpatient department facility fee of $3,620. The procedure was physically performed at a facility located five miles from the main hospital campus, in a building not attached to the hospital.</p>
    <p><strong>Action:</strong> The patient requested the facility&rsquo;s CMS certification number from the billing department and verified through the CMS Provider Enrollment lookup that the specific location was certified as an ASC, not as an HOPD. He submitted a written dispute citing the incorrect facility type and the Medicare ASC vs. HOPD rate differential.</p>
    <p><strong>Outcome:</strong> The hospital corrected the billing to reflect the ASC rate. The facility fee was reduced from $3,620 to $1,220. <strong>Savings: $2,400.</strong></p>
</div>

<div class="case-study">
    <h3>Case Study 3: 8-year SOL defense dismissed $7,200 Ohio medical debt lawsuit</h3>
    <p><strong>Situation:</strong> An Akron patient was sued by a medical debt collector for $7,200 on a hospital bill from January 2015. The collector filed the lawsuit in January 2025 &mdash; nine years after the original service date. The patient&rsquo;s last payment had been made in March 2016.</p>
    <p><strong>Action:</strong> The patient filed a written Answer to the lawsuit, citing the Ohio 8-year statute of limitations for written contracts. The last payment was in March 2016; the lawsuit was filed in January 2025 &mdash; 8 years and 10 months after last payment. The SOL had expired in March 2024.</p>
    <p><strong>Outcome:</strong> The collector did not contest the SOL defense. The court dismissed the case. <strong>Amount saved: $7,200.</strong></p>
</div>

<h2 id="faq">Frequently asked questions</h2>

<div class="faq-section">
    <div class="faq-item">
        <h3>Do Ohio hospitals have to provide charity care?</h3>
        <p>Ohio has no state law mandating specific charity care income thresholds, but nonprofit Ohio hospitals must comply with IRS Section 501(r) &mdash; requiring a written FAP, limits on charges for qualifying patients, and a 240-day application window. The Ohio Attorney General enforces hospital charitable obligations and can investigate systems that fail to screen patients or publicize assistance programs. Major Ohio systems like Cleveland Clinic and OhioHealth extend assistance to patients up to 300&ndash;400% FPL under their own published policies.</p>
    </div>

    <div class="faq-item">
        <h3>Can Ohio hospitals garnish my wages for medical debt?</h3>
        <p>Yes, after a court judgment. Under ORC &sect; 2329.66, the maximum garnishment is the lesser of 25% of disposable income or the amount above 30 times the federal minimum wage ($217.50/week). A court judgment is required first &mdash; collectors cannot garnish wages without one. Your primary Ohio residence is protected from forced sale under the Ohio homestead exemption. Applying for financial assistance or negotiating a payment plan before a lawsuit is filed prevents reaching the judgment stage.</p>
    </div>

    <div class="faq-item">
        <h3>What is Ohio&rsquo;s statute of limitations on medical debt?</h3>
        <p>Ohio applies a 6-year SOL for open accounts (ORC &sect; 2305.07) and an 8-year SOL for written contracts. Most hospital bills involve a signed financial responsibility form, so the 8-year period typically applies. After expiration, a collector cannot win a lawsuit if you raise the SOL defense in a written response to the suit. Never ignore a lawsuit summons &mdash; a default judgment can be entered if you do not respond, regardless of whether the SOL has passed.</p>
    </div>

    <div class="faq-item">
        <h3>How do I file a complaint about an Ohio hospital billing error?</h3>
        <p>Submit a written dispute to the hospital&rsquo;s billing department, citing the specific line items in error and supporting documentation. If unresolved, file with the Ohio Department of Health for patient rights violations (ORC &sect; 3702.30) or the Ohio Attorney General for charitable compliance failures. For insurance disputes, contact the Ohio Department of Insurance. Document every communication in writing and keep copies of all bills, letters, and responses.</p>
    </div>

    <div class="faq-item">
        <h3>What is the Ohio Patients&rsquo; Bill of Rights?</h3>
        <p>The Ohio Patients&rsquo; Bill of Rights (ORC &sect; 3702.30) gives Ohio hospital patients the right to an itemized bill, the right to know charges in advance for non-emergency procedures, the right to have billing explained by a representative, a formal grievance process, and the right to interpreter services at no charge. Violations can be reported to the Ohio Department of Health. These rights apply to all Ohio licensed hospitals regardless of nonprofit or for-profit status.</p>
    </div>
</div>

<h2 id="sources">Sources</h2>

<ul class="sources-list">
    <li><a href="https://codes.ohio.gov/ohio-revised-code/section-3702.30" target="_blank" rel="noopener">Ohio Revised Code &sect; 3702.30 &mdash; Patients&rsquo; Bill of Rights, Ohio Legislature</a></li>
    <li><a href="https://www.ohioattorneygeneral.gov/Business/Services-for-Business/Charitable-Law-Section/Charitable-Hospitals" target="_blank" rel="noopener">Ohio Attorney General &mdash; Charitable Hospitals and Charity Care Enforcement</a></li>
    <li><a href="https://codes.ohio.gov/ohio-revised-code/section-2305.07" target="_blank" rel="noopener">ORC &sect; 2305.07 &mdash; Ohio Statute of Limitations for Open Accounts</a></li>
    <li><a href="https://www.cms.gov/nosurprises" target="_blank" rel="noopener">CMS &mdash; No Surprises Act: Balance Billing Protections for Patients</a></li>
    <li><a href="https://www.cfpb.gov/consumer-tools/medical-debt/" target="_blank" rel="noopener">Consumer Financial Protection Bureau &mdash; Medical Debt Resources and Consumer Protections</a></li>
</ul>
""",
})
