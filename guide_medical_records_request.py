"""Guide: How to Request Your Medical Records — HIPAA Rights."""

from guides import register, _embed

register("how-to-request-medical-records", {
    "title": "How to Request Your Medical Records: Your HIPAA Rights (2026)",
    "meta_description": "HIPAA guarantees your right to your medical records within 30 days. Learn exactly how to request them, what providers can charge, and what to do if denied.",
    "published": "2026-04-05",
    "author": "BillKarma Team",
    "category": "Patient Rights",
    "faqs": [
        {
            "q": "Can a hospital deny my medical records because I have an unpaid bill?",
            "a": "No. Withholding medical records because of an unpaid balance is a HIPAA violation. You have an unconditional right to access your records regardless of your payment status. If a provider refuses, file a complaint with the HHS Office for Civil Rights (OCR) at hhs.gov/ocr. The provider can still pursue collection of the unpaid bill separately — they simply cannot hold your records hostage.",
        },
        {
            "q": "How long does a provider have to respond to my records request?",
            "a": "Under HIPAA, providers must respond within 30 days of receiving your request. They may take one 30-day extension if they notify you in writing before the original deadline expires. If a provider misses both deadlines without explanation, that is a HIPAA violation and you can file a complaint with HHS OCR.",
        },
        {
            "q": "What can providers charge for medical records?",
            "a": "Providers may charge a 'reasonable cost-based fee.' For electronic records, HHS guidance states that per-page fees are NOT permitted — providers can only charge the actual labor cost to retrieve and transmit the records. For paper copies, per-page fees vary by state but are typically $0.25–$0.75/page. You can request records electronically to minimize or eliminate fees.",
        },
        {
            "q": "How do I request records for a deceased family member?",
            "a": "You need legal authority to access a deceased person's records. Qualifying roles include: executor or administrator of the estate (with letters testamentary), personal representative named in a will, or surviving next-of-kin where state law grants this right. Submit documentation of your authority along with the records request. A power of attorney expires at death and is not sufficient.",
        },
        {
            "q": "Can I access my records through a patient portal app?",
            "a": "Yes. The 2021 CMS Interoperability Rule requires hospitals and health systems to allow third-party apps to access your records via FHIR API. Apps like Apple Health, CommonHealth, and others can pull your records directly from Epic, Cerner, and other EHR systems. This is free, immediate, and requires no paper forms.",
        },
        {
            "q": "What if I disagree with something in my medical record?",
            "a": "HIPAA gives you the right to request an amendment to your medical record. Submit a written request to the provider explaining what you believe is incorrect and why. The provider has 60 days to respond (with one 60-day extension). If they deny the amendment, you can submit a statement of disagreement that must be appended to your record going forward.",
        },
    ],
    "body": f"""
<p class="lead">HIPAA gives every patient an unconditional right to their medical records — and providers must respond within 30 days. Yet most patients don't know what to request, where to ask, or what they can legally be charged. BillKarma's analysis found that <strong>28% of billing errors are only detectable by comparing the medical record to the itemized bill</strong> — meaning your records are not just a right, they are a financial protection tool.</p>

<div class="answer-box" style="background:#e8f5e9;border-left:4px solid #2e7d32;padding:16px 20px;margin:24px 0;border-radius:4px;">
    <strong>Quick answer:</strong> Submit a written HIPAA records request with your name, date of birth, dates of service, specific records needed, and preferred delivery method. Providers must respond within 30 days. Electronic records must be provided at minimal or no cost. They cannot deny access because you owe money.
</div>

<nav class="toc">
    <h2>In this guide</h2>
    <ol>
        <li><a href="#what-you-can-request">What records you can request</a></li>
        <li><a href="#where-to-request">Where to send your request</a></li>
        <li><a href="#how-to-request">How to make the request (step by step)</a></li>
        <li><a href="#timeline-and-fees">Timeline and what they can charge</a></li>
        <li><a href="#what-they-cannot-do">What providers cannot do</a></li>
        <li><a href="#deceased-family-member">Requesting records for a deceased family member</a></li>
        <li><a href="#amendment-rights">Your right to amend your records</a></li>
        <li><a href="#billkarma-use">Why BillKarma needs your records</a></li>
        <li><a href="#faq">Frequently asked questions</a></li>
        <li><a href="#sources">Sources</a></li>
    </ol>
</nav>

<h2 id="what-you-can-request">1. What records you can request</h2>

<p>HIPAA covers your entire "designated record set" — anything a provider uses to make decisions about your care or billing. In practice, you can request:</p>

<table>
    <thead>
        <tr><th>Record type</th><th>What it contains</th><th>Why it matters for billing</th></tr>
    </thead>
    <tbody>
        <tr><td><strong>Progress notes</strong></td><td>Physician and nurse documentation of each encounter</td><td>Confirms the services actually delivered vs. what was billed</td></tr>
        <tr><td><strong>Discharge summary</strong></td><td>Summary of inpatient stay, diagnoses, treatment</td><td>Verifies admission/discharge dates and diagnosis codes</td></tr>
        <tr><td><strong>Lab results</strong></td><td>Blood work, urinalysis, pathology reports</td><td>Confirms tests were ordered and performed</td></tr>
        <tr><td><strong>Imaging reports</strong></td><td>Radiology reads for X-rays, CT, MRI, ultrasound</td><td>Confirms imaging billed was actually interpreted</td></tr>
        <tr><td><strong>Operative notes</strong></td><td>Surgeon's documentation of procedures performed</td><td>Catches CPT code upcoding and phantom procedures</td></tr>
        <tr><td><strong>Medication administration record (MAR)</strong></td><td>Every drug given, dose, time</td><td>Catches drugs billed but not administered</td></tr>
        <tr><td><strong>Billing records</strong></td><td>Charges, CPT codes, ICD-10 codes, claim forms</td><td>Direct comparison to itemized bill</td></tr>
        <tr><td><strong>Insurance EOB</strong></td><td>Explanation of benefits from your insurer</td><td>Shows what was billed vs. what was allowed vs. what you owe</td></tr>
    </tbody>
</table>

<p>You can request all of these, or just the ones relevant to your situation. For billing disputes, request the itemized bill, discharge summary, progress notes, and medication administration record at minimum.</p>

<h2 id="where-to-request">2. Where to send your request</h2>

<p>The right destination depends on where you received care:</p>

<ul>
    <li><strong>Hospital inpatient or ER visit:</strong> The hospital's Medical Records Department (also called Health Information Management or HIM). Find the contact on the hospital's website under "Patient Services" or "Medical Records."</li>
    <li><strong>Physician office visit:</strong> The physician's office directly. If you saw a specialist at a hospital-owned practice, their records are separate from the hospital's records.</li>
    <li><strong>Patient portals:</strong> MyChart (Epic), Health Online (Cerner), FollowMyHealth, and others allow you to download records electronically at no cost. This is the fastest method for recent visits.</li>
    <li><strong>Third-party apps:</strong> Under the 2021 CMS Interoperability Rule, you can authorize apps like Apple Health or CommonHealth to pull records directly via FHIR API — no paper forms required.</li>
</ul>

<div class="key-takeaway">
    <strong>Use a patient portal first.</strong> If your provider is on Epic, Cerner, or a major EHR system, your records are often available immediately through the portal at no cost. Only submit a formal written request if portal access is unavailable or incomplete.
</div>

<h2 id="how-to-request">3. How to make the request (step by step)</h2>

<ol>
    <li><strong>Locate the provider's HIPAA authorization form.</strong> Most hospitals have this on their website or in the patient portal. If not, a written request works — no specific form is required by HIPAA.</li>
    <li><strong>Include all required information:</strong> your full legal name, date of birth, dates of service (or date range), specific records you are requesting, how you want to receive them (electronic, paper, portal), and your signature.</li>
    <li><strong>Specify electronic delivery.</strong> Write "Please provide records in electronic format (PDF or standard electronic format) to minimize fees." This eliminates per-page charges.</li>
    <li><strong>Submit with proof of delivery.</strong> For written requests, send via certified mail or email with read receipt. Keep a copy of everything you submit.</li>
    <li><strong>Log the date.</strong> The 30-day clock starts when the provider receives your request, not when you send it. Note the delivery confirmation date.</li>
    <li><strong>Follow up on day 25.</strong> If you haven't received records or an acknowledgment by day 25, call the medical records department. Reference the submission date and request a status update in writing.</li>
    <li><strong>Escalate if ignored.</strong> If the provider misses the 30-day deadline without granting an extension, file a complaint at <a href="https://www.hhs.gov/ocr/complaints/" target="_blank" rel="noopener">hhs.gov/ocr</a>. This is a federal HIPAA violation.</li>
</ol>

<h2 id="timeline-and-fees">4. Timeline and what they can charge</h2>

<p>HIPAA is specific about both how fast providers must respond and what they can bill you:</p>

<table>
    <thead>
        <tr><th>Scenario</th><th>HIPAA requirement</th><th>Practical tip</th></tr>
    </thead>
    <tbody>
        <tr><td>Standard request</td><td>Respond within <strong>30 days</strong></td><td>Request via portal for same-day access</td></tr>
        <tr><td>Extension (one allowed)</td><td>Up to <strong>30 additional days</strong> with written notice to you before day 30</td><td>If they miss day 30 without notice, file with OCR</td></tr>
        <tr><td>Electronic records fee</td><td>Labor cost only — <strong>no per-page fees</strong></td><td>Explicitly request electronic format in writing</td></tr>
        <tr><td>Paper copy fee</td><td>Reasonable cost-based fee (state laws vary: typically $0.25–$0.75/page)</td><td>Request electronic to avoid; some states cap fees further</td></tr>
        <tr><td>Denial</td><td>Provider must give written reason and instructions to appeal</td><td>Most denials are reversible; escalate to OCR if unresolved</td></tr>
    </tbody>
</table>

<p>HHS has clarified that when a patient requests electronic records to be sent to a third-party app (via FHIR API or direct app access), providers must provide them <strong>at no charge</strong>. The fee prohibition for electronic records is broadly construed.</p>

<h2 id="what-they-cannot-do">5. What providers cannot do</h2>

<p>These actions are HIPAA violations — if a provider attempts them, you have grounds to file a complaint:</p>

<ul>
    <li><strong>Deny access because you have an unpaid bill.</strong> Outstanding balances have zero effect on your right to records. Full stop.</li>
    <li><strong>Charge excessive fees for electronic records.</strong> Per-page fees for electronic delivery are not permitted under HHS guidance.</li>
    <li><strong>Take longer than 60 days without a written explanation.</strong> Even with the extension, 60 days is the absolute maximum.</li>
    <li><strong>Require you to use a specific form.</strong> HIPAA requires only a written request with identifying information. Providers may have their own forms, but cannot require them if you submit a valid written request.</li>
    <li><strong>Release records to the wrong person</strong> without your written authorization. This protects you as well as obligates the provider.</li>
</ul>

<p>To file a complaint: visit <a href="https://www.hhs.gov/ocr/complaints/" target="_blank" rel="noopener">hhs.gov/ocr</a>, call 1-800-368-1019, or submit online. Complaints must generally be filed within 180 days of the violation. There is no cost to file.</p>

<h2 id="deceased-family-member">6. Requesting records for a deceased family member</h2>

<p>HIPAA continues to protect a deceased person's health information for 50 years after death. To access a deceased family member's records, you must establish legal authority. Accepted forms of authority include:</p>

<ul>
    <li><strong>Executor or administrator of the estate</strong> — present letters testamentary or letters of administration issued by the probate court</li>
    <li><strong>Personal representative named in a valid will</strong> — present the relevant will documentation</li>
    <li><strong>Surviving next-of-kin</strong> where state law grants access rights (varies by state)</li>
</ul>

<p>Note: A power of attorney expires at death and does not establish authority to access records posthumously. If no formal authority exists, consult a probate attorney about your options before requesting records.</p>

<p>Common reasons to access a deceased family member's records: resolving estate billing disputes, malpractice investigations, disability or life insurance claims, and understanding hereditary health conditions.</p>

<h2 id="amendment-rights">7. Your right to amend your records</h2>

<p>HIPAA gives you the right to request a correction if your records contain information you believe is inaccurate or incomplete. The process:</p>

<ol>
    <li>Submit a written amendment request to the provider's medical records department</li>
    <li>Explain specifically what you believe is wrong and provide supporting documentation if available</li>
    <li>The provider has <strong>60 days</strong> to respond (with one 60-day extension, notified in writing)</li>
    <li>If the provider denies the amendment, they must give you a written reason and allow you to submit a <strong>statement of disagreement</strong> — which must be appended to your record</li>
</ol>

<p>Providers can deny amendment requests if the record was created by another provider, the information is accurate and complete as written, or the record would not be available for inspection under HIPAA. But the denial and your rebuttal become part of the permanent record.</p>

<h2 id="billkarma-use">8. Why BillKarma needs your records</h2>

<p>BillKarma cross-references your medical records against your itemized bill and EOB to catch errors that are invisible without clinical documentation. The most common errors that require record comparison include:</p>

<ul>
    <li><strong>Phantom procedures:</strong> A CPT code billed for a procedure not documented in the operative or progress notes</li>
    <li><strong>Upcoded services:</strong> A higher-complexity evaluation and management (E&M) code billed than the documentation supports</li>
    <li><strong>Drugs not administered:</strong> Medications appearing on the charge list that are not in the medication administration record</li>
    <li><strong>Wrong admission dates:</strong> An inpatient stay billed for more days than the discharge summary reflects</li>
    <li><strong>Duplicate tests:</strong> Lab or imaging billed twice when records show it was performed once</li>
</ul>

<div class="key-takeaway">
    <strong>BillKarma finding:</strong> 28% of billing errors are only detectable by comparing the medical record to the itemized bill. Upload both to <a href="/scan">BillKarma's scanner</a> to run a complete cross-check.
</div>

{_embed(mode="scan", title="Cross-check your bill against your medical records", subtitle="Upload your itemized bill and records to find errors invisible to a bill-only review.")}

<h2 id="faq">Frequently asked questions</h2>

<div class="faq-section">
    <div class="faq-item">
        <h3>Can a hospital deny my medical records because I have an unpaid bill?</h3>
        <p>No — this is a HIPAA violation. Your right to access records is unconditional and unrelated to payment status. File a complaint at hhs.gov/ocr if a provider attempts this.</p>
    </div>

    <div class="faq-item">
        <h3>How long does a provider have to respond to my records request?</h3>
        <p>30 days from receipt of your request, with one optional 30-day extension (they must notify you in writing before the first deadline expires). Missing both deadlines is a federal violation.</p>
    </div>

    <div class="faq-item">
        <h3>What can providers charge for medical records?</h3>
        <p>For electronic records: labor cost only — per-page fees are not permitted. For paper: a reasonable cost-based fee (often $0.25–$0.75/page, capped by state law). Request electronic format to minimize fees.</p>
    </div>

    <div class="faq-item">
        <h3>How do I request records for a deceased family member?</h3>
        <p>You need legal authority: executor of the estate (with letters testamentary), personal representative in the will, or surviving next-of-kin where state law permits. A power of attorney expires at death.</p>
    </div>

    <div class="faq-item">
        <h3>Can I access my records through a patient portal app?</h3>
        <p>Yes. Under the 2021 CMS Interoperability Rule, hospitals must allow third-party apps to pull your records via FHIR API at no charge. Apple Health, CommonHealth, and similar apps support this.</p>
    </div>

    <div class="faq-item">
        <h3>What if I disagree with something in my medical record?</h3>
        <p>Submit a written amendment request. The provider has 60 days to respond. If they deny it, you can submit a statement of disagreement that becomes a permanent part of your record.</p>
    </div>
</div>

<h2 id="sources">Sources</h2>

<ul class="sources-list">
    <li><a href="https://www.hhs.gov/hipaa/for-individuals/medical-records/index.html" target="_blank" rel="noopener">HHS: Your Health Information Rights under HIPAA</a></li>
    <li><a href="https://www.hhs.gov/hipaa/for-professionals/privacy/guidance/access/index.html" target="_blank" rel="noopener">HHS OCR: HIPAA Right of Access — Guidance and FAQs</a></li>
    <li><a href="https://www.cms.gov/regulations-and-guidance/guidance/interoperability/index" target="_blank" rel="noopener">CMS: 2021 Interoperability and Patient Access Final Rule (FHIR API)</a></li>
    <li><a href="https://www.hhs.gov/ocr/complaints/index.html" target="_blank" rel="noopener">HHS Office for Civil Rights: File a HIPAA Complaint</a></li>
    <li><a href="https://www.healthit.gov/topic/patient-access-information" target="_blank" rel="noopener">HealthIT.gov: Patient Access to Health Information</a></li>
</ul>
""",
})
