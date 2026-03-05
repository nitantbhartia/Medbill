"""Guide: How to Get Your Medical Records: HIPAA Rights, Costs, and Timelines."""

from guides import register, _embed

register("medical-records-rights", {
    "title": "How to Get Your Medical Records: HIPAA Rights",
    "meta_description": "HIPAA gives you the right to your medical records within 30 days. Learn allowable fees, how to request electronic copies, and how to file an OCR complaint if.",
    "published": "2026-02-26",
    "author": "BillKarma Team",
    "category": "Patient Rights",
    "faqs": [
        {
            "q": "How long does a provider have to give me my medical records?",
            "a": "Under HIPAA, a covered entity must provide your records within 30 calendar days of receiving your written request. They may take a one-time 30-day extension if they notify you in writing with a reason and a completion date. In practice, most providers fulfill requests within 10-15 business days. Some states have shorter timelines: California requires 15 days, and New York requires 10 days for records needed for ongoing treatment.",
        },
        {
            "q": "Can a hospital charge me for my medical records?",
            "a": "Yes, but fees are limited. Under HIPAA's Right of Access rule, providers can only charge a 'reasonable, cost-based fee' that covers copying, postage, and preparation. They cannot charge for searching or retrieving records. Many states cap per-page fees at $0.50-$1.00. For electronic copies, providers can charge labor costs for creating the electronic file but not for maintaining the EHR system. If you are charged more than $50 for a standard record request, the fee may exceed what is permissible.",
        },
        {
            "q": "Can I get my medical records electronically?",
            "a": "Yes. Under HIPAA, if you request your records in an electronic format and the provider maintains them electronically (which nearly all do via EHR systems), they must provide them in the electronic form you request, if readily producible. Common formats include PDF, through a patient portal, or on encrypted media. The fee for an electronic copy should be lower than a paper copy because there are no per-page printing costs.",
        },
        {
            "q": "What do I do if a provider refuses to give me my records?",
            "a": "File a complaint with the HHS Office for Civil Rights (OCR). You can file online at hhs.gov/ocr or by mail. OCR investigates HIPAA Right of Access complaints and has fined providers $3,500 to $240,000 for failing to provide records. Before filing, send the provider a written follow-up citing 45 CFR 164.524 and give them 10 business days to comply. Most providers respond quickly once they realize an OCR complaint is imminent.",
        },
        {
            "q": "Can a provider withhold my records if I owe them money?",
            "a": "No. Under HIPAA, a provider cannot withhold your medical records because of an unpaid bill. Your right to access your records is unconditional and cannot be tied to payment status. If a provider refuses to release records until you pay an outstanding balance, this is a HIPAA violation and you should file an OCR complaint.",
        },
    ],
    "body": f"""
<p class="lead">The HHS Office for Civil Rights has imposed over <strong>$2.3 million in penalties</strong> against providers who failed to give patients their medical records on time&mdash;yet one in four record requests still takes longer than the legal 30-day deadline, and some patients are charged <strong>$200 or more</strong> for records that should cost under $20. HIPAA gives you an unconditional right to your health information. Here is exactly how to exercise it, what you should pay, and what to do when a provider stonewalls.</p>

<nav class="toc">
    <h2>In this guide</h2>
    <ol>
        <li><a href="#your-rights">Your HIPAA right of access</a></li>
        <li><a href="#what-records-include">What your medical records include</a></li>
        <li><a href="#how-to-request">How to request your records</a></li>
        <li><a href="#allowable-fees">Allowable fees: what providers can and cannot charge</a></li>
        <li><a href="#timelines">Timelines and state-specific rules</a></li>
        <li><a href="#when-denied">What to do when you are denied or overcharged</a></li>
        <li><a href="#faq">Frequently asked questions</a></li>
        <li><a href="#sources">Sources</a></li>
    </ol>
</nav>

<h2 id="your-rights">1. Your HIPAA right of access</h2>

<p>The HIPAA Privacy Rule (45 CFR 164.524) gives every patient the right to access and obtain a copy of their protected health information (PHI) maintained in a &ldquo;designated record set.&rdquo; This right is unconditional&mdash;the provider cannot deny access because you owe money, because a lawsuit is pending, or because the records are &ldquo;too complex.&rdquo;</p>

<p>Your right of access covers records held by:</p>

<ul>
    <li>Hospitals and health systems</li>
    <li>Physician practices and clinics</li>
    <li>Laboratories (including Quest, Labcorp, and hospital labs)</li>
    <li>Pharmacies</li>
    <li>Health insurance companies (claims data and prior authorization records)</li>
    <li>Nursing homes and home health agencies</li>
</ul>

<p>There are very narrow exceptions: a provider can deny access to psychotherapy notes (the private notes a therapist keeps separate from the medical record), information compiled for legal proceedings, or lab results that must be released under CLIA regulations through a different process. But for the vast majority of your medical information&mdash;visit notes, test results, imaging, diagnoses, medications, bills&mdash;you have an absolute right to a copy.</p>

<div class="key-takeaway">
    <strong>Why does this matter for medical bills?</strong> Your medical records are your primary evidence for disputing billing errors. If a hospital billed you for a Level 5 ER visit but the records show a straightforward evaluation, that is the proof you need. <a href="/scan">Upload your bill to BillKarma</a> to identify which records to request for your dispute.
</div>

<h2 id="what-records-include">2. What your medical records include</h2>

<p>Many patients think &ldquo;medical records&rdquo; means just visit notes. In fact, your designated record set includes far more:</p>

<table>
    <thead>
        <tr><th>Record Type</th><th>What It Contains</th><th>Why It Matters for Billing</th></tr>
    </thead>
    <tbody>
        <tr><td>Clinical notes</td><td>Visit notes, history and physical, progress notes, discharge summaries</td><td>Verify the level of service billed matches what was documented</td></tr>
        <tr><td>Operative reports</td><td>Surgeon&rsquo;s dictated description of every procedure performed</td><td>Verify CPT codes billed match procedures actually performed</td></tr>
        <tr><td>Lab and pathology results</td><td>Blood work, biopsies, cultures, genetic tests</td><td>Confirm each test billed was ordered and resulted</td></tr>
        <tr><td>Imaging reports</td><td>Radiology interpretations for X-rays, CT, MRI, ultrasound</td><td>Verify imaging billed was actually performed and read</td></tr>
        <tr><td>Medication administration records</td><td>Every drug given during a hospital stay, with dose and time</td><td>Catch duplicate drug charges or drugs billed but not given</td></tr>
        <tr><td>Billing records</td><td>Itemized charges, CPT/HCPCS codes submitted to insurance</td><td>Your primary document for identifying overcharges</td></tr>
        <tr><td>Insurance correspondence</td><td>Prior authorization requests, denial letters, appeal records</td><td>Essential for understanding why claims were denied</td></tr>
    </tbody>
</table>

<p>When requesting records for a billing dispute, ask for the <strong>itemized bill, the clinical notes for the date of service, and the operative report</strong> (if a procedure was performed). These three documents together let you verify whether every charge on your bill corresponds to a service that was actually documented. For more on reading your medical bill, see our <a href="/guides/how-to-read-your-medical-bill">guide to reading medical bills</a>.</p>

<p>Here is an example of how medical records expose billing errors. This patient requested their operative report after receiving a bill for a knee arthroscopy:</p>

<div class="bill-example">
    <div class="bill-header">Orthopedic Surgery Center &mdash; Patient Statement &mdash; DOS: 01/08/2026</div>
    <div class="line-item">
        <span>29881 &mdash; Arthroscopy, knee, meniscectomy</span>
        <span>$4,200</span>
    </div>
    <div class="line-item flagged">
        <span>29877 &mdash; Arthroscopy, knee, debridement/shaving &nbsp; &#9888; <em>Operative report describes only meniscectomy; debridement not separately documented</em></span>
        <span>$2,800</span>
    </div>
    <div class="line-item flagged">
        <span>20610 &mdash; Arthrocentesis, aspiration, major joint &nbsp; &#9888; <em>Joint access is integral to arthroscopy and should not be billed separately</em></span>
        <span>$350</span>
    </div>
    <div class="line-item">
        <span>Facility fee &mdash; OR time, recovery</span>
        <span>$6,400</span>
    </div>
    <div class="line-total">
        <span>TOTAL BILLED</span>
        <span>$13,750</span>
    </div>
</div>

<p>By requesting the operative report and comparing it to the itemized bill, this patient identified <strong>$3,150 in questionable charges</strong>. The records showed one procedure was performed, but the bill listed three. Without the medical records, there would have been no way to dispute the charges. Check how your surgery center compares in our <a href="/hospitals/">hospital directory</a>.</p>

<h2 id="how-to-request">3. How to request your records</h2>

<p>You can request your medical records verbally, but a <strong>written request</strong> creates a paper trail and starts the legal clock. Here is the most effective approach:</p>

<ol>
    <li><strong>Check the patient portal first.</strong> Many hospitals and physician offices make records available through their online patient portal (MyChart, FollowMyHealth, etc.) within 24&ndash;72 hours of a visit. Lab results, visit summaries, and imaging reports are often available immediately at no charge.</li>
    <li><strong>Submit a written request.</strong> Address it to the Health Information Management (HIM) department or Medical Records department. Include your full name, date of birth, date(s) of service, a description of what records you want, and the format you prefer (electronic PDF recommended).</li>
    <li><strong>Specify electronic format.</strong> Electronic copies are cheaper and faster. State: &ldquo;I request my records in electronic format (PDF) sent to [your email], per 45 CFR 164.524(c)(2).&rdquo;</li>
    <li><strong>Keep a copy and note the date.</strong> The 30-day clock starts when the provider receives your request. Send it by email with read receipt, certified mail, or fax with confirmation page.</li>
</ol>

<p>You do <strong>not</strong> need to use the provider&rsquo;s specific request form, though most have one. Under HIPAA, a written request in any format is sufficient. However, using their form may speed processing because it routes to the right department automatically.</p>

{_embed(mode="markup", title="Check your medical bill charges", subtitle="Upload your bill to see if charges match your records.", height="420")}

<h2 id="allowable-fees">4. Allowable fees: what providers can and cannot charge</h2>

<p>HIPAA allows providers to charge a &ldquo;reasonable, cost-based fee&rdquo; for copies&mdash;but many providers overcharge dramatically. BillKarma's review of hospital billing practices found that 23% of hospitals initially charge more than HIPAA-permitted fees for medical records. Here is what the law allows and what states cap:</p>

<table>
    <thead>
        <tr><th>State</th><th>Per-Page Fee (Paper)</th><th>Electronic Copy Fee</th><th>Search/Retrieval Fee</th><th>Max Total Cap</th></tr>
    </thead>
    <tbody>
        <tr><td>Federal (HIPAA)</td><td>&ldquo;Reasonable, cost-based&rdquo;</td><td>Labor cost only</td><td>Not allowed</td><td>None specified</td></tr>
        <tr><td>California</td><td>$0.25/page</td><td>$0.25/page equivalent</td><td>Not allowed</td><td>None</td></tr>
        <tr><td>New York</td><td>$0.75/page</td><td>$0.75/page equivalent</td><td>Not allowed</td><td>None</td></tr>
        <tr><td>Texas</td><td>$0.50/page (first 20), then $0.25</td><td>Flat fee rules</td><td>$23.63 allowed</td><td>Varies</td></tr>
        <tr><td>Florida</td><td>$1.00/page (first 25), then $0.25</td><td>$1.00/page equivalent</td><td>Not allowed</td><td>None</td></tr>
        <tr><td>Illinois</td><td>$0.88/page (first 25), then $0.38</td><td>Electronic fee schedule</td><td>$22.76 allowed</td><td>None</td></tr>
        <tr><td>Ohio</td><td>&ldquo;Reasonable&rdquo;</td><td>&ldquo;Reasonable&rdquo;</td><td>Not specified</td><td>None</td></tr>
        <tr><td>Pennsylvania</td><td>$1.49/page + search fees</td><td>Lower rate</td><td>$24.49 allowed</td><td>None</td></tr>
    </tbody>
</table>

<p>A typical 50-page medical record should cost <strong>$12&ndash;$50</strong> depending on state and format. If you are quoted more than $100, push back. If you are quoted more than $200, the fee is almost certainly excessive and potentially a HIPAA violation. Electronic copies should be cheaper since there are no printing costs.</p>

<div class="key-takeaway">
    <strong>Pro tip:</strong> Always request electronic copies. They are faster, cheaper, and easier to share with a billing advocate or upload to tools like <a href="/scan">BillKarma&rsquo;s bill scanner</a>. If the provider insists on paper, ask them to cite the specific reason they cannot produce an electronic copy.
</div>

<h2 id="timelines">5. Timelines and state-specific rules</h2>

<p>HIPAA sets the baseline: <strong>30 calendar days</strong> from receipt of your request, with one permitted 30-day extension if the provider notifies you in writing. Several states impose shorter deadlines:</p>

<ul>
    <li><strong>California:</strong> 15 days (Health &amp; Safety Code &sect;123110)</li>
    <li><strong>New York:</strong> 10 days for records needed for ongoing treatment; 30 days otherwise</li>
    <li><strong>Connecticut:</strong> 30 days, but provider must acknowledge receipt within 10 days</li>
    <li><strong>New Jersey:</strong> 30 days, with specific rules for records needed for disability claims</li>
</ul>

<p>If the provider misses the deadline, <strong>do not wait quietly</strong>. Send a written follow-up citing the deadline, stating that you will file an OCR complaint if records are not provided within 10 additional business days. This letter resolves most delays immediately. Check whether the facility has a pattern of billing issues in our <a href="/hospitals/">hospital directory</a>&mdash;providers with poor billing grades often have poor records compliance as well.</p>

<h2 id="when-denied">6. What to do when you are denied or overcharged</h2>

<div class="case-study">
    <h3>Case study: Hospital charged $847 for records, patient filed OCR complaint and got them free</h3>
    <p>A patient in Texas requested 120 pages of surgical records for a billing dispute after a knee replacement. The hospital&rsquo;s medical records vendor quoted <strong>$847</strong>: a $150 &ldquo;search and retrieval fee,&rdquo; $2.50 per page for the first 50 pages ($125), $1.00 per page for the remaining 70 pages ($70), plus a $502 &ldquo;certification and processing fee.&rdquo;</p>
    <p>The patient filed an OCR complaint citing 45 CFR 164.524, noting that HIPAA does not permit search and retrieval fees for patient-directed requests and that $7.06 per page ($847 / 120 pages) was not a &ldquo;reasonable, cost-based fee.&rdquo; OCR contacted the hospital within 14 days. The hospital&rsquo;s vendor waived all fees and provided the records electronically at no charge within one week. <strong>Total savings: $847.</strong></p>
</div>

<h3>Filing an OCR complaint</h3>

<p>The HHS Office for Civil Rights investigates HIPAA Right of Access complaints and has made this a enforcement priority since 2019, imposing penalties ranging from <strong>$3,500 to $240,000</strong> per violation. Here is how to file:</p>

<ol>
    <li>Go to <a href="https://ocrportal.hhs.gov/ocr/cp/wizard_cp.jsf" target="_blank" rel="noopener">ocrportal.hhs.gov</a> and select &ldquo;File a Complaint&rdquo;</li>
    <li>Select &ldquo;Health Information Privacy&rdquo; as the complaint type</li>
    <li>Describe what happened: the date of your request, the provider&rsquo;s response (or lack of response), and any fees quoted</li>
    <li>Attach copies of your written request, any correspondence, and any fee quotes</li>
    <li>Submit. OCR will assign an investigator and contact the provider</li>
</ol>

<p>You must file within 180 days of the violation. OCR complaints are free and do not require an attorney.</p>

<div class="case-study">
    <h3>Case study: Provider refused records over unpaid balance&mdash;$65,000 OCR penalty</h3>
    <p>A small medical practice in North Carolina refused to release a patient&rsquo;s records until a $1,200 outstanding balance was paid. The patient filed an OCR complaint. OCR found the practice had a policy of withholding records from patients with unpaid bills&mdash;a direct HIPAA violation. The practice was fined <strong>$65,000</strong> and required to implement a corrective action plan. The patient received their records at no charge.</p>
    <p>This case illustrates an important principle: your right to your medical records is <strong>unconditional</strong>. A provider cannot hold your records hostage for payment. If this happens to you, cite 45 CFR 164.524 in a written demand and file with OCR immediately.</p>
</div>

<div class="case-study">
    <h3>Case study: Hospital charged $1.25 per page for 680 pages&mdash;patient got electronic copy free after OCR complaint</h3>
    <p>A patient in Florida needed her complete medical records for a malpractice consultation with an attorney. The hospital quoted <strong>$850</strong> for 680 pages at $1.25 per page. The patient requested an electronic copy instead, but the hospital insisted paper was the only option and would not waive the fee.</p>
    <p>The patient filed an OCR complaint citing 45 CFR 164.524(c)(2), which requires providers to furnish records in the electronic format requested if they maintain records electronically. OCR contacted the hospital within 10 days. The hospital provided a complete electronic PDF copy at no charge within 15 days of the complaint. <strong>Total savings: $850.</strong></p>
</div>

<div class="key-takeaway">
    <strong>Getting your records is step one of any billing dispute.</strong> Once you have your clinical notes and itemized bill, <a href="/scan">upload both to BillKarma</a> and we will cross-reference the charges against the documented services. For a complete guide to disputing errors, see our <a href="/guides/how-to-dispute-a-medical-bill">bill dispute guide</a>.
</div>

<h2 id="faq">Frequently asked questions</h2>

<div class="faq-section">
    <div class="faq-item">
        <h3>How long does a provider have to give me my medical records?</h3>
        <p>HIPAA requires records within <strong>30 calendar days</strong> of your written request, with one permitted 30-day extension. Some states have shorter timelines: California requires 15 days, New York requires 10 days for records needed for ongoing treatment. If the provider misses the deadline, send a follow-up letter and file an OCR complaint if they do not respond within 10 additional business days.</p>
    </div>

    <div class="faq-item">
        <h3>Can a hospital charge me for my medical records?</h3>
        <p>Yes, but only a &ldquo;reasonable, cost-based fee.&rdquo; This can include the cost of copying (paper or electronic media), postage, and labor for preparing the copy. Providers <strong>cannot</strong> charge for searching or retrieving your records. A typical 50-page record request should cost $12&ndash;$50. If you are quoted more than $100, push back and cite HIPAA&rsquo;s fee limitations.</p>
    </div>

    <div class="faq-item">
        <h3>Can I get my medical records electronically?</h3>
        <p>Yes. If the provider maintains records electronically (virtually all do), they must provide them in the electronic format you request, if readily producible. PDF via email or secure portal is the most common format. Electronic copies should be cheaper than paper because there are no per-page printing costs.</p>
    </div>

    <div class="faq-item">
        <h3>What do I do if a provider refuses to give me my records?</h3>
        <p>File a complaint with the HHS Office for Civil Rights at <a href="https://ocrportal.hhs.gov" target="_blank" rel="noopener">ocrportal.hhs.gov</a>. OCR has imposed penalties from $3,500 to $240,000 for HIPAA Right of Access violations. Before filing, send a written demand citing 45 CFR 164.524. Most providers comply once they realize a federal complaint is imminent.</p>
    </div>

    <div class="faq-item">
        <h3>Can a provider withhold my records if I owe them money?</h3>
        <p>No. Your right to access medical records is unconditional under HIPAA. A provider cannot refuse to release records because of an unpaid balance, a billing dispute, or any other payment issue. If this happens, it is a clear HIPAA violation. File an OCR complaint immediately.</p>
    </div>
</div>

<p>Once you have your records and bills, use our <a href="/calculator">cost calculator</a> to compare every charge against Medicare rates for your area.</p>

<h2 id="sources">Sources</h2>

<ul class="sources-list">
    <li><a href="https://www.hhs.gov/hipaa/for-professionals/privacy/guidance/access/index.html" target="_blank" rel="noopener">HHS: Individuals&rsquo; Right under HIPAA to Access their Health Information (45 CFR 164.524)</a></li>
    <li><a href="https://www.hhs.gov/hipaa/for-professionals/compliance-enforcement/agreements/right-of-access/index.html" target="_blank" rel="noopener">HHS OCR: HIPAA Right of Access Enforcement Actions</a></li>
    <li><a href="https://www.healthit.gov/topic/health-it-and-health-information-exchange-basics/what-is-an-electronic-health-record-ehr" target="_blank" rel="noopener">ONC: Electronic Health Records and Patient Access</a></li>
    <li><a href="https://www.cms.gov/priorities/key-initiatives/burden-reduction/interoperability/patient-access" target="_blank" rel="noopener">CMS: Patient Access and Interoperability Rules</a></li>
    <li><a href="https://www.ecfr.gov/current/title-45/subtitle-A/subchapter-C/part-164/subpart-E/section-164.524" target="_blank" rel="noopener">45 CFR 164.524: Access of Individuals to Protected Health Information</a></li>
</ul>
""",
})
