"""Guide: How to Appeal a Health Insurance Claim Denial."""

from guides import register, _embed

register("how-to-appeal-insurance-denial", {
    "title": "How to Appeal a Health Insurance Claim Denial: A Step-by-Step Guide",
    "meta_description": "Insurance denials get overturned 40-50% of the time on first appeal. Learn exactly how to appeal a denied claim with templates, timelines, and real examples.",
    "published": "2026-02-20",
    "author": "BillKarma Team",
    "category": "Insurance Basics",
    "faqs": [
        {
            "q": "How long do I have to appeal an insurance denial?",
            "a": "Most insurance plans give you 180 days (about 6 months) from the date of the denial notice to file an internal appeal. Some plans allow less, so check your denial letter for the exact deadline. For external reviews, you typically have 4 months after exhausting internal appeals. For urgent care situations, you can request an expedited appeal that must be decided within 72 hours.",
        },
        {
            "q": "Can I appeal a denial after I have already paid the bill?",
            "a": "Yes. Paying a medical bill does not waive your right to appeal the insurance denial. If your appeal is successful, the insurance company will reimburse you or pay the provider, who will then refund your payment. Keep all receipts and proof of payment. File your appeal within the deadline on your denial notice regardless of whether you have paid.",
        },
        {
            "q": "Does it cost anything to appeal an insurance denial?",
            "a": "No. Filing an appeal is free. Both internal appeals and external reviews cost you nothing. The insurance company is required by law to provide a free and fair appeals process. You may choose to hire a medical billing advocate or attorney, but this is optional and not required to file a successful appeal.",
        },
        {
            "q": "What if my external review is also denied?",
            "a": "If the independent external reviewer upholds the denial, you still have options. You can file a complaint with your state insurance commissioner. You can ask your doctor to submit a new prior authorization with additional clinical documentation. In some cases, you can request a different treatment that is covered and achieves the same goal. You may also consult a healthcare attorney if the denied amount is large.",
        },
        {
            "q": "Can I appeal an out-of-network denial?",
            "a": "Yes. If you received emergency care, the No Surprises Act requires your insurer to cover it at in-network rates regardless of network status. For non-emergency out-of-network care, you can appeal if you believe the service was not available in-network within a reasonable distance or wait time, or if you were referred out-of-network by an in-network provider.",
        },
        {
            "q": "What is a letter of medical necessity and how do I get one?",
            "a": "A letter of medical necessity is a document from your doctor explaining why a specific treatment or service is needed for your condition. It includes your diagnosis, symptoms, treatments already tried, and clinical evidence supporting the requested service. Ask your doctor's office to write one specifically for your appeal. Be specific about what the insurer denied and why.",
        },
    ],
    "body": f"""
<p class="lead">Insurance companies deny about 17% of in-network claims, according to KFF. But here&rsquo;s what they don&rsquo;t advertise: <strong>40&ndash;50% of first-level appeals succeed</strong>, and external reviews overturn denials another 40% of the time. Most patients never appeal&mdash;which is exactly what insurers count on. An appealed MRI denial alone can save you <strong>$2,000&ndash;$4,000</strong>. This guide walks you through every step of the appeals process, with templates, timelines, and real results.</p>

<nav class="toc">
    <h2>In this guide</h2>
    <ol>
        <li><a href="#why-claims-denied">Why claims get denied (and which denials are worth appealing)</a></li>
        <li><a href="#understanding-denial">Understanding your denial notice</a></li>
        <li><a href="#three-levels">The 3 levels of appeal</a></li>
        <li><a href="#how-to-file">How to file a first-level appeal (step by step)</a></li>
        <li><a href="#appeal-letter">Appeal letter template</a></li>
        <li><a href="#external-review">External review &mdash; your ace in the hole</a></li>
        <li><a href="#real-results">Real appeal results (case studies)</a></li>
        <li><a href="#faq">Frequently asked questions</a></li>
        <li><a href="#sources">Sources</a></li>
    </ol>
</nav>

<h2 id="why-claims-denied">1. Why claims get denied (and which denials are worth appealing)</h2>

<p>Not all denials are the same. Some are simple paperwork errors that get fixed with a phone call. Others require a formal appeal with clinical evidence. Here&rsquo;s a breakdown of the most common denial reasons, how often they succeed on appeal, and whether they&rsquo;re worth your time:</p>

<table>
    <thead>
        <tr><th>Denial Reason</th><th>How Common</th><th>Appeal Success Rate</th><th>Worth Appealing?</th></tr>
    </thead>
    <tbody>
        <tr><td>&ldquo;Not medically necessary&rdquo;</td><td>~40% of denials</td><td>~50%</td><td>Yes &mdash; get a letter of medical necessity from your doctor</td></tr>
        <tr><td>&ldquo;Prior authorization required&rdquo;</td><td>~25% of denials</td><td>~60%</td><td>Yes &mdash; often a paperwork error, not a clinical decision</td></tr>
        <tr><td>&ldquo;Out of network&rdquo;</td><td>~15% of denials</td><td>~35%</td><td>Yes &mdash; check if the <a href="/guides/no-surprises-act-explained">No Surprises Act</a> applies</td></tr>
        <tr><td>&ldquo;Service not covered&rdquo;</td><td>~10% of denials</td><td>~20%</td><td>Maybe &mdash; lower success, but worth it for expensive services</td></tr>
        <tr><td>&ldquo;Coding error&rdquo;</td><td>~10% of denials</td><td>~80%</td><td>Yes &mdash; very high success when the correct code is resubmitted</td></tr>
    </tbody>
</table>

<div class="key-takeaway">
    <strong>Bottom line:</strong> If your denied claim is worth more than $200, appeal it. The process is free, success rates are high, and the worst outcome is the same &ldquo;no&rdquo; you already have. You have nothing to lose.
</div>

<p>Before you appeal, check what Medicare pays for the denied service. This gives you a baseline for what the service is worth and strengthens your argument:</p>

{_embed(mode="cost", title="Look up your denied service", subtitle="Enter the CPT code from your denial notice to see the Medicare rate.")}

<h2 id="understanding-denial">2. Understanding your denial notice</h2>

<p>Every denial comes with a written notice&mdash;either a letter from your insurer or a section on your <a href="/guides/understanding-explanation-of-benefits">Explanation of Benefits (EOB)</a>. This notice contains everything you need to start your appeal. Here&rsquo;s what a typical denial looks like, annotated with the key elements:</p>

<div class="bill-example">
    <div class="bill-header">Explanation of Benefits &mdash; Aetna &mdash; Claim #2026-0215-7743</div>
    <div class="line-item">
        <span><strong>Patient:</strong> Jane Smith &nbsp; <strong>Member ID:</strong> AET-9928-4410</span>
        <span><strong>Date of Service:</strong> 01/28/2026</span>
    </div>
    <div class="line-item">
        <span><strong>Provider:</strong> Lakeview Orthopedic Associates (In-Network)</span>
        <span><strong>Claim #:</strong> 2026-0215-7743</span>
    </div>
    <div class="line-item" style="border-bottom: 2px solid #D1D5DB; margin-top: 8px; padding-bottom: 8px;">
        <span><strong>Service</strong></span>
        <span><strong>Billed &rarr; Allowed &rarr; Ins. Paid &rarr; You Owe</strong></span>
    </div>
    <div class="line-item flagged">
        <span>73721 &mdash; MRI Knee w/o Contrast &nbsp; &#9888; <em>DENIED &mdash; Reason: Not medically necessary (Code: NMN-401)</em></span>
        <span>$2,800 &rarr; $0 &rarr; $0 &rarr; $2,800</span>
    </div>
    <div class="line-item" style="border-top: 2px solid #D1D5DB; margin-top: 8px; padding-top: 8px;">
        <span><strong>Denial reason:</strong> The requested service has not been determined to be medically necessary based on the clinical information provided.</span>
        <span></span>
    </div>
    <div class="line-item">
        <span><strong>Your appeal rights:</strong> You have the right to appeal this decision within 180 days. Call 1-800-555-0199 or write to: Aetna Appeals, PO Box 14463, Lexington, KY 40512.</span>
        <span></span>
    </div>
</div>

<div class="key-takeaway">
    <strong>Got a denial notice like this one?</strong> <a href="/scan">Upload your EOB to BillKarma</a> &mdash; we flag whether the underlying procedure codes were billed correctly, which can reveal the fastest path to overturning a denial.
</div>

<p>Here&rsquo;s what to look for on your denial notice:</p>

<ul>
    <li><strong>Denial reason code</strong> &mdash; A short code like &ldquo;NMN-401&rdquo; or &ldquo;PA-REQ.&rdquo; This tells you the category of denial. Call the insurer and ask them to explain the code in plain language if it&rsquo;s not clear.</li>
    <li><strong>Appeal rights section</strong> &mdash; Every denial notice must include your right to appeal. This section tells you the deadline, where to send the appeal, and the phone number for questions. If you don&rsquo;t see this section, the insurer is violating federal law.</li>
    <li><strong>Deadline for appeal</strong> &mdash; Usually 180 days from the denial date. Write this date down immediately. Missing the deadline means losing your right to appeal.</li>
    <li><strong>Contact information</strong> &mdash; The address and phone number for the appeals department. This is often different from the general customer service number.</li>
    <li><strong>Clinical criteria used</strong> &mdash; Some denials reference the specific guideline or criteria the insurer used. Ask for this in writing if it&rsquo;s not included&mdash;it tells you exactly what evidence you need to provide.</li>
</ul>

<div class="key-takeaway">
    <strong>First step after any denial:</strong> Call the number on your denial notice and ask three questions: (1) What is the specific reason for the denial? (2) What clinical documentation would you need to approve this on appeal? (3) What is my exact deadline to file? Write down the answers and the name of the person you spoke with.
</div>

<h2 id="three-levels">3. The 3 levels of appeal</h2>

<p>Federal law (the Affordable Care Act) guarantees you the right to appeal any insurance denial. There are up to three levels, and each one gives you another chance to get the decision reversed:</p>

<table>
    <thead>
        <tr><th>Level</th><th>Who Reviews</th><th>Timeline</th><th>Success Rate</th><th>How to File</th></tr>
    </thead>
    <tbody>
        <tr><td><strong>Level 1:</strong> Internal appeal</td><td>Your insurance company (a different reviewer than whoever denied it)</td><td>30 days for non-urgent; 72 hours for urgent</td><td>40&ndash;50%</td><td>Letter or form to insurer&rsquo;s appeals department</td></tr>
        <tr><td><strong>Level 2:</strong> Second internal appeal</td><td>Your insurance company (senior reviewer or medical director)</td><td>30 days for non-urgent; 72 hours for urgent</td><td>25&ndash;35%</td><td>Letter to insurer (some plans skip this level)</td></tr>
        <tr><td><strong>Level 3:</strong> External review</td><td>Independent third-party reviewer (not employed by your insurer)</td><td>45 days standard; 72 hours for urgent</td><td>~40%</td><td>Request through insurer or state insurance dept.</td></tr>
    </tbody>
</table>

<p><strong>How it works:</strong> You must start with an internal appeal (Level 1). If that&rsquo;s denied, some plans offer a second internal review. After you exhaust internal appeals, you have the right to an external review&mdash;where an independent doctor or reviewer who does not work for your insurance company examines your case. The external reviewer&rsquo;s decision is <strong>binding</strong>, meaning the insurer must comply.</p>

<p><strong>Urgent (expedited) appeals:</strong> If your doctor says waiting could seriously harm your health, you can request an expedited review. The insurer must respond within 72 hours. You can file an internal appeal and request an external review at the same time for urgent cases.</p>

<h2 id="how-to-file">4. How to file a first-level appeal (step by step)</h2>

<p>Here&rsquo;s exactly what to do, in order:</p>

<h3>Step 1: Note the deadline</h3>

<p>Find the appeal deadline on your denial notice. Most plans give you 180 days (about 6 months) from the date of the denial. Mark it on your calendar. Don&rsquo;t wait until the last week&mdash;start now so you have time to gather documentation.</p>

<h3>Step 2: Call your insurance company</h3>

<p>Call the appeals department number on your denial notice (not the general customer service line). Ask:</p>
<ul>
    <li>What is the exact reason this claim was denied?</li>
    <li>What specific clinical criteria or guidelines were used?</li>
    <li>What documentation would help overturn this denial?</li>
    <li>Where should I send my written appeal?</li>
    <li>Is there a specific appeal form I should use?</li>
</ul>

<p>Write down the name of the representative, the date and time, and any reference numbers.</p>

<h3>Step 3: Get supporting documentation from your doctor</h3>

<p>This is the most important step. Contact your doctor&rsquo;s office and ask for:</p>
<ul>
    <li><strong>A letter of medical necessity</strong> &mdash; A letter from your doctor explaining why the denied service is medically necessary for your specific condition. This should reference your diagnosis, symptoms, treatments already tried, and why the denied service is the appropriate next step.</li>
    <li><strong>Clinical notes</strong> &mdash; Office visit notes, imaging results, lab results, and any other documentation that supports the medical need for the service.</li>
    <li><strong>Peer-reviewed evidence</strong> &mdash; If available, ask your doctor to cite clinical guidelines or studies that support the treatment. Insurers respond well to evidence from organizations like the American College of Radiology or the American Academy of Orthopaedic Surgeons.</li>
</ul>

<h3>Step 4: Write your appeal letter</h3>

<p>Your appeal letter should be clear, specific, and factual. Include your claim number, the denial reason, and exactly why the denial should be overturned. See the full template in the next section.</p>

<h3>Step 5: Submit and track</h3>

<p>Send your appeal letter with all supporting documentation. Use one of these methods:</p>
<ul>
    <li><strong>Insurer&rsquo;s online portal</strong> &mdash; Creates a timestamped record. Upload your letter and all attachments.</li>
    <li><strong>Certified mail with return receipt</strong> &mdash; Proof that the insurer received it and when.</li>
    <li><strong>Fax with confirmation page</strong> &mdash; Keep the confirmation showing the fax was received.</li>
</ul>

<p>After submitting, call the appeals department 5&ndash;7 business days later to confirm receipt and ask for a timeline. The insurer must respond within 30 days for non-urgent appeals.</p>

<div class="key-takeaway">
    <strong>Wondering what the denied service actually should have cost?</strong> Use the <a href="/calculator">BillKarma pricing calculator</a> to see the Medicare benchmark for your CPT code &mdash; knowing that number before you write your appeal letter gives you a concrete figure to reference.
</div>

<h2 id="appeal-letter">5. Appeal letter template</h2>

<p>Here&rsquo;s a complete sample appeal letter for a &ldquo;not medically necessary&rdquo; MRI denial. Adapt this to your situation by replacing the bracketed information:</p>

<div class="key-takeaway">
    <strong>Not sure if your denial is worth fighting?</strong> <a href="/scan">Scan your bill with BillKarma</a> &mdash; we identify coding errors and overcharges that strengthen your appeal and show exactly how much money is on the table.
</div>

<div class="case-study">
    <h3>Sample appeal letter &mdash; &ldquo;not medically necessary&rdquo; MRI denial</h3>
    <p><em>[Your Name]<br>[Your Address]<br>[City, State, ZIP]<br>[Date]</em></p>
    <p><em>Aetna Appeals Department<br>PO Box 14463<br>Lexington, KY 40512</em></p>
    <p><strong>RE: Appeal of Claim Denial<br>Member ID: [YOUR MEMBER ID]<br>Claim Number: [CLAIM NUMBER]<br>Date of Service: [DATE]<br>Denied Service: MRI Knee without Contrast (CPT 73721)</strong></p>
    <p>Dear Appeals Department,</p>
    <p>I am writing to appeal the denial of claim [CLAIM NUMBER] for an MRI of the right knee (CPT 73721) performed on [DATE]. The claim was denied as &ldquo;not medically necessary&rdquo; (denial code NMN-401). I believe this denial should be overturned based on the following clinical evidence.</p>
    <p><strong>Clinical history:</strong> I have been experiencing persistent right knee pain, swelling, and instability for the past four months. My orthopedic surgeon, Dr. [NAME], has documented the following in the enclosed clinical notes:</p>
    <ul>
        <li>Initial examination on [DATE] showed joint line tenderness and positive McMurray test, suggesting a meniscal tear</li>
        <li>I completed 6 weeks of physical therapy (12 sessions) from [DATE] to [DATE] with no improvement in symptoms</li>
        <li>X-rays on [DATE] were negative for fracture but cannot rule out soft tissue injury</li>
        <li>Conservative treatments including rest, ice, NSAIDs, and physical therapy have failed to resolve symptoms</li>
    </ul>
    <p><strong>Why MRI is medically necessary:</strong> An MRI is the standard of care for evaluating suspected meniscal tears after conservative treatment fails. The American College of Radiology Appropriateness Criteria rates MRI as &ldquo;usually appropriate&rdquo; for patients with acute knee pain, physical exam findings suggesting internal derangement, and failure of conservative management. Without an MRI, my surgeon cannot confirm the diagnosis or plan appropriate treatment.</p>
    <p><strong>Enclosed documentation:</strong></p>
    <ol>
        <li>Letter of medical necessity from Dr. [NAME], board-certified orthopedic surgeon</li>
        <li>Office visit notes from [DATES]</li>
        <li>Physical therapy records showing 12 sessions and lack of improvement</li>
        <li>X-ray results from [DATE]</li>
    </ol>
    <p>I respectfully request that you reverse the denial of this claim and authorize coverage for the MRI. Please contact me at [PHONE] or [EMAIL] if you need additional information.</p>
    <p><em>Sincerely,<br>[Your Name]</em></p>
</div>

<p><strong>Tips for a strong appeal letter:</strong></p>
<ul>
    <li>Reference the specific denial code and reason&mdash;show you understand why it was denied</li>
    <li>Include concrete facts: dates, number of therapy sessions, specific test results</li>
    <li>Cite clinical guidelines by name (e.g., ACR Appropriateness Criteria)</li>
    <li>Attach every piece of supporting documentation&mdash;do not make the reviewer hunt for information</li>
    <li>Keep the tone professional and factual, not emotional or confrontational</li>
</ul>

<p>Want help identifying the right CPT codes and rates for your appeal? <a href="/scan">Upload your bill or EOB to BillKarma</a> to get a detailed breakdown.</p>

<h2 id="external-review">6. External review &mdash; your ace in the hole</h2>

<p>If your internal appeal is denied, don&rsquo;t give up. Under the Affordable Care Act (ACA), you have the right to an <strong>external review</strong> for most insurance denials. This is one of the most powerful tools patients have&mdash;and most people don&rsquo;t know it exists.</p>

<p><strong>What makes external review different:</strong></p>
<ul>
    <li><strong>Independent reviewer</strong> &mdash; The person reviewing your case does not work for your insurance company. They are typically a physician or clinical expert in the relevant specialty, hired by an independent review organization (IRO).</li>
    <li><strong>Binding decision</strong> &mdash; If the external reviewer overturns your denial, the insurance company <strong>must</strong> comply. They cannot appeal the reviewer&rsquo;s decision.</li>
    <li><strong>High success rate</strong> &mdash; About 40% of external reviews result in the denial being overturned, according to data from state insurance departments and CMS.</li>
    <li><strong>Free to you</strong> &mdash; There is no cost to request an external review.</li>
</ul>

<p><strong>How to request an external review:</strong></p>
<ol>
    <li>You must first exhaust your internal appeals (at least one internal appeal denial).</li>
    <li>Your denial letter should include instructions for requesting an external review. If it doesn&rsquo;t, call your insurer or your state insurance department.</li>
    <li>You typically have <strong>4 months</strong> from the final internal appeal denial to request an external review.</li>
    <li>Submit the same documentation you used for your internal appeal, plus any additional evidence gathered since then.</li>
    <li>The external reviewer will make a decision within <strong>45 days</strong> (72 hours for urgent cases).</li>
</ol>

<p><strong>When external review is especially effective:</strong></p>
<ul>
    <li>&ldquo;Not medically necessary&rdquo; denials where your doctor strongly supports the service</li>
    <li>Experimental or investigational treatment denials where peer-reviewed evidence supports the treatment</li>
    <li>Denials based on insurer&rsquo;s internal guidelines that differ from widely accepted clinical standards</li>
</ul>

<p>Check how your denied service compares to standard pricing. This can strengthen your case by showing the service is routine and commonly covered:</p>

{_embed(mode="markup", title="Check pricing for your denied service", subtitle="Enter the CPT code and billed amount from your denial notice.", height="420")}

<h2 id="real-results">7. Real appeal results (case studies)</h2>

<div class="case-study">
    <h3>Case study 1: MRI denied as &ldquo;not medically necessary&rdquo; &mdash; approved on first appeal</h3>
    <p>A 42-year-old patient was referred for an MRI of the knee (CPT 73721) after four months of persistent pain and failed physical therapy. The insurer denied the claim, stating the MRI was &ldquo;not medically necessary.&rdquo; The patient&rsquo;s orthopedist wrote a letter of medical necessity documenting the failed conservative treatment (12 physical therapy sessions), persistent symptoms (pain, swelling, mechanical locking), and clinical findings (positive McMurray test suggesting a meniscal tear). The appeal was submitted with the letter, PT records, and office notes.</p>
    <p><strong>Result:</strong> First-level appeal approved within 21 days. The MRI was covered at the in-network allowed amount.</p>
    <p><strong>Billed:</strong> $2,800 &rarr; <strong>Patient owed:</strong> $60 copay &rarr; <strong>Savings: $2,740</strong></p>
</div>

<div class="case-study">
    <h3>Case study 2: ER visit denied as &ldquo;not an emergency&rdquo; &mdash; overturned using prudent layperson standard</h3>
    <p>A 55-year-old patient went to the ER at 2 a.m. with severe chest pain, shortness of breath, and dizziness. After testing, the diagnosis was gastroesophageal reflux (acid reflux)&mdash;not a heart attack. The insurer retroactively denied the ER claim, stating the condition was &ldquo;not a true emergency&rdquo; based on the final diagnosis.</p>
    <p>The patient appealed, citing the <strong>prudent layperson standard</strong>&mdash;a legal standard (defined in the ACA and most state laws) that says ER coverage should be based on the patient&rsquo;s symptoms at the time, not the final diagnosis. A reasonable person experiencing crushing chest pain at 2 a.m. would seek emergency care. The appeal included the triage notes documenting the presenting symptoms.</p>
    <p><strong>Result:</strong> Appeal approved. The insurer reversed the denial and processed the claim at in-network ER rates.</p>
    <p><strong>Billed:</strong> $4,800 &rarr; <strong>Patient owed:</strong> $600 (deductible/coinsurance) &rarr; <strong>Savings: $4,200</strong></p>
</div>

<div class="case-study">
    <h3>Case study 3: Outpatient surgery prior authorization denied &mdash; approved after resubmission</h3>
    <p>A patient was scheduled for outpatient arthroscopic knee surgery. The surgeon&rsquo;s office submitted a prior authorization request, but the insurer denied it, stating the submission was &ldquo;incomplete&rdquo;&mdash;clinical notes were missing from the request. The surgeon&rsquo;s office resubmitted the authorization with the full clinical notes, operative plan, and letter of medical necessity explaining why conservative treatment had failed.</p>
    <p><strong>Result:</strong> Approved on appeal within 14 days. The surgery proceeded as scheduled.</p>
    <p><strong>Billed:</strong> $18,000 &rarr; <strong>Patient owed:</strong> $1,500 (in-network deductible) &rarr; <strong>Without the appeal, patient would have owed: $18,000</strong></p>
</div>

<div class="case-study">
    <h3>Case study 4: Prescription drug denial overturned on external review</h3>
    <p>A patient with rheumatoid arthritis was prescribed a biologic medication after failing two other drug therapies. The insurer denied the prescription as &ldquo;not the preferred treatment,&rdquo; insisting on a third step-therapy drug first. The patient&rsquo;s rheumatologist documented that the two failed therapies met the clinical criteria for the biologic and that the insurer&rsquo;s required step-therapy drug had a contraindication for this patient. The internal appeal was denied. The patient then requested an external review.</p>
    <p><strong>Result:</strong> External reviewer (an independent rheumatologist) overturned the denial, agreeing that the biologic was medically appropriate given the patient&rsquo;s history.</p>
    <p><strong>Annual cost of the medication:</strong> $24,000 &rarr; <strong>Patient copay with coverage:</strong> $150/month &rarr; <strong>Annual savings: $22,200</strong></p>
</div>

<p>Think you have a denied claim worth appealing? Start by looking up the service to understand its value. Then <a href="/scan">upload your denial notice or EOB to BillKarma</a> for help building your appeal.</p>

<h2 id="faq">Frequently asked questions</h2>

<div class="faq-section">
    <div class="faq-item">
        <h3>How long do I have to appeal an insurance denial?</h3>
        <p>Most insurance plans give you 180 days (about 6 months) from the date of the denial notice to file an internal appeal. Some plans allow less time, so check your denial letter for the exact deadline. For external reviews, you typically have 4 months after your final internal appeal is denied. For urgent situations, you can request an expedited appeal that must be decided within 72 hours.</p>
    </div>

    <div class="faq-item">
        <h3>Can I appeal a denial after I have already paid the bill?</h3>
        <p>Yes. Paying a bill does not waive your right to appeal. If your appeal succeeds, the insurer will pay the provider, and you&rsquo;ll receive a refund for what you already paid. Keep all receipts. File your appeal within the deadline regardless of whether you&rsquo;ve paid.</p>
    </div>

    <div class="faq-item">
        <h3>Does it cost anything to appeal an insurance denial?</h3>
        <p>No. Filing an internal appeal and requesting an external review are both completely free. Insurance companies are required by law to provide a fair appeals process at no cost to you. You may choose to hire a <a href="/guides/how-to-negotiate-medical-bills">medical billing advocate</a>, but this is optional.</p>
    </div>

    <div class="faq-item">
        <h3>What if my external review is also denied?</h3>
        <p>You still have options. File a complaint with your <a href="https://www.naic.org/state_web_map.htm" target="_blank" rel="noopener">state insurance commissioner</a>. Ask your doctor about alternative treatments that achieve the same goal. For large amounts, consider consulting a healthcare attorney. You can also ask your doctor to resubmit a new prior authorization with different or additional clinical documentation.</p>
    </div>

    <div class="faq-item">
        <h3>Can I appeal an out-of-network denial?</h3>
        <p>Yes. For emergency care, the <a href="/guides/no-surprises-act-explained">No Surprises Act</a> requires coverage at in-network rates regardless of network status. For non-emergency care, you can appeal if the service wasn&rsquo;t available in-network within a reasonable distance or wait time, or if an in-network provider referred you out of network. Document the lack of in-network availability in your appeal.</p>
    </div>

    <div class="faq-item">
        <h3>What is a letter of medical necessity and how do I get one?</h3>
        <p>A letter of medical necessity is a document from your doctor explaining why a specific service is needed for your condition. It should include your diagnosis, symptoms, treatments already tried, and clinical evidence supporting the requested service. Call your doctor&rsquo;s office and specifically ask them to write one for your appeal. Tell them the denial reason so they can address it directly.</p>
    </div>
</div>

<h2 id="sources">Sources</h2>

<ul class="sources-list">
    <li><a href="https://www.kff.org/private-insurance/issue-brief/claims-denials-and-appeals-in-aca-marketplace-plans/" target="_blank" rel="noopener">KFF: Claims Denials and Appeals in ACA Marketplace Plans (2023 Data)</a></li>
    <li><a href="https://www.healthcare.gov/appeal-insurance-company-decision/appeals/" target="_blank" rel="noopener">HealthCare.gov: How to Appeal a Health Insurance Company Decision</a></li>
    <li><a href="https://www.cms.gov/cciio/resources/consumer-assistance-grants" target="_blank" rel="noopener">CMS: Consumer Assistance Program &mdash; Appeals and External Review</a></li>
    <li><a href="https://www.cms.gov/nosurprises" target="_blank" rel="noopener">CMS: No Surprises Act &mdash; Consumer Protections</a></li>
    <li><a href="https://www.naic.org/state_web_map.htm" target="_blank" rel="noopener">NAIC: State Insurance Commissioner Directory</a></li>
    <li><a href="https://www.dol.gov/sites/dolgov/files/EBSA/about-ebsa/our-activities/resource-center/publications/your-rights-after-a-claim-is-denied.pdf" target="_blank" rel="noopener">U.S. Department of Labor: Your Rights After a Health Insurance Claim Is Denied</a></li>
    <li><a href="https://www.commonwealthfund.org/publications/issue-briefs/2023/feb/health-insurance-claim-denials" target="_blank" rel="noopener">Commonwealth Fund: Understanding Health Insurance Claim Denials</a></li>
</ul>
""",
})
