"""Guide: The No Surprises Act Explained."""

from guides import register, _embed

register("no-surprises-act-explained", {
    "title": "The No Surprises Act: Your Rights When You Get a Medical Bill",
    "meta_description": "The No Surprises Act protects you from surprise out-of-network bills. Learn what's covered, how to spot violations, and what to do if you get a surprise bill.",
    "published": "2026-02-18",
    "author": "BillKarma Team",
    "category": "Patient Rights",
    "faqs": [
        {
            "q": "What is the No Surprises Act?",
            "a": "The No Surprises Act is a federal law that took effect January 1, 2022. It protects patients from surprise medical bills when they receive emergency care or are treated by out-of-network providers at in-network facilities. Under the law, patients can only be charged in-network cost-sharing rates in these situations, regardless of whether the provider is in their insurance network.",
        },
        {
            "q": "Does the No Surprises Act apply to me if I have insurance?",
            "a": "Yes, if you have private health insurance (through an employer, marketplace, or individual plan). The law applies to most commercial insurance plans. It does not apply to Medicare, Medicaid, TRICARE, or VA benefits, which have their own protections. Uninsured patients receive separate protections under the law, including the right to a good faith estimate before scheduled services.",
        },
        {
            "q": "What should I do if I receive a surprise bill?",
            "a": "First, check if the No Surprises Act applies (emergency care, or out-of-network provider at an in-network facility where you did not consent to out-of-network billing). If it does, contact your insurance company and the provider's billing department. Cite the No Surprises Act and request the bill be reprocessed at in-network rates. If the provider refuses, file a complaint at cms.gov/nosurprises or call 1-800-985-3059.",
        },
        {
            "q": "What is a good faith estimate under the No Surprises Act?",
            "a": "If you are uninsured or self-pay, healthcare providers must give you a written good faith estimate of expected charges before a scheduled service. If the final bill exceeds the estimate by $400 or more, you can dispute it through the patient-provider dispute resolution process. You must file within 120 days of receiving the bill.",
        },
        {
            "q": "Does the No Surprises Act cover ground ambulance bills?",
            "a": "No. Ground ambulance services are currently exempt from the No Surprises Act. Air ambulance services are covered, meaning you cannot be surprise-billed by an out-of-network air ambulance provider. Ground ambulance billing remains one of the most common sources of surprise medical bills, and legislation to address it is being considered.",
        },
    ],
    "body": f"""
<p class="lead">Before 2022, one in five ER visits resulted in a surprise bill&mdash;an unexpected charge from a doctor or provider who wasn&rsquo;t in your insurance network, even though you went to an in-network hospital. The average surprise bill was <strong>$1,219</strong>. The No Surprises Act changed that. Here&rsquo;s what the law actually covers, where the gaps are, and exactly what to do if you get a bill that violates it.</p>

<nav class="toc">
    <h2>In this guide</h2>
    <ol>
        <li><a href="#what-it-covers">What the No Surprises Act covers</a></li>
        <li><a href="#what-it-doesnt">What it does NOT cover</a></li>
        <li><a href="#how-it-works">How the protections work in practice</a></li>
        <li><a href="#good-faith-estimates">Good faith estimates for uninsured patients</a></li>
        <li><a href="#spot-violation">How to spot a No Surprises Act violation</a></li>
        <li><a href="#what-to-do">What to do if you get a surprise bill</a></li>
        <li><a href="#real-examples">Real examples of No Surprises Act protections</a></li>
        <li><a href="#faq">Frequently asked questions</a></li>
        <li><a href="#sources">Sources</a></li>
    </ol>
</nav>

<h2 id="what-it-covers">1. What the No Surprises Act covers</h2>

<p>The No Surprises Act (NSA) protects you in three specific scenarios:</p>

<h3>a) Emergency services</h3>

<p>If you go to an ER, you cannot be billed at out-of-network rates&mdash;regardless of whether the hospital or any provider who treats you is in your network. This includes the ER physician, radiologist, anesthesiologist, and any specialist called in during your emergency visit. (For more on how ER bills work, see our <a href="/guides/why-emergency-room-bills-are-so-high">ER bill guide</a>.)</p>

<p><strong>What this means for your bill:</strong> Your cost-sharing (deductible, copay, coinsurance) must be calculated at in-network rates. The provider cannot bill you for the difference between what they charge and what your insurance pays (this practice was called &ldquo;balance billing&rdquo;).</p>

<h3>b) Out-of-network providers at in-network facilities</h3>

<p>If you go to an in-network hospital for a scheduled procedure and are treated by an out-of-network provider you didn&rsquo;t choose (a common scenario with anesthesiologists, pathologists, and radiologists), you&rsquo;re protected. The out-of-network provider must bill you at in-network rates.</p>

<h3>c) Air ambulance services</h3>

<p>Out-of-network air ambulance providers cannot balance bill you. Your cost-sharing is limited to in-network rates. (Note: ground ambulances are <strong>not</strong> covered.)</p>

<div class="key-takeaway">
    <strong>The core rule:</strong> You cannot be billed more than your in-network cost-sharing amount for emergency services, or for out-of-network providers at in-network facilities that you did not choose. The provider and your insurer work out the payment between themselves.
</div>

<h2 id="what-it-doesnt">2. What it does NOT cover</h2>

<p>The No Surprises Act has important gaps:</p>

<table>
    <thead>
        <tr><th>Not Covered</th><th>Why It Matters</th></tr>
    </thead>
    <tbody>
        <tr><td>Ground ambulances</td><td>Average ground ambulance bill: $1,200. Out-of-network ground ambulance bills remain a major source of surprise charges.</td></tr>
        <tr><td>Out-of-network providers you consent to</td><td>If you sign a written consent form agreeing to out-of-network care at least 72 hours before a scheduled service, the NSA protections may not apply.</td></tr>
        <tr><td>Post-stabilization transfers</td><td>After an ER visit, if you are stable and voluntarily transfer to an out-of-network facility, the NSA may not cover the transfer facility&rsquo;s charges.</td></tr>
        <tr><td>Medicare, Medicaid, TRICARE, VA</td><td>These programs have their own billing protections. The NSA specifically applies to commercial insurance plans.</td></tr>
        <tr><td>Non-emergency out-of-network care you choose</td><td>If you voluntarily go to an out-of-network provider for non-emergency care, standard out-of-network billing applies.</td></tr>
    </tbody>
</table>

<div class="key-takeaway">
    <strong>Seeing charges on your bill that look out-of-network?</strong> <a href="/scan">Upload your bill to BillKarma</a> &mdash; we automatically identify which charges fall under No Surprises Act protections and show you exactly what you should owe instead.
</div>

<h2 id="how-it-works">3. How the protections work in practice</h2>

<p>Here&rsquo;s what happens behind the scenes when the NSA applies to your bill:</p>

<ol>
    <li><strong>You receive care.</strong> An out-of-network provider treats you in a covered scenario (ER visit, or at an in-network facility).</li>
    <li><strong>The provider bills your insurance.</strong> Your insurer processes the claim and calculates your cost-sharing at in-network rates.</li>
    <li><strong>You pay only in-network cost-sharing.</strong> Your deductible, copay, and coinsurance are based on your plan&rsquo;s in-network rates. No balance billing.</li>
    <li><strong>Provider and insurer negotiate.</strong> If the provider and insurer disagree on payment, they enter an Independent Dispute Resolution (IDR) process. This happens between them&mdash;you are not involved and owe nothing additional.</li>
</ol>

<div class="key-takeaway">
    <strong>Did your ER visit produce bills from multiple providers you never chose?</strong> <a href="/scan">Scan your bill with BillKarma</a> &mdash; we break down every charge and highlight which ones qualify for No Surprises Act protection so you know exactly what to dispute.
</div>

<div class="case-study">
    <h3>Example: How the NSA saves you money</h3>
    <p>You go to an in-network ER with chest pain. The ER doctor is in-network, but the cardiologist called in to read your EKG is out-of-network. The cardiologist bills $1,800 for an interpretation (CPT 93010).</p>
    <p><strong>Without the NSA:</strong> Your insurance pays the &ldquo;out-of-network allowable&rdquo; of $250. The cardiologist bills you for the remaining $1,550. You owe <strong>$1,550</strong> in surprise charges plus your normal copay.</p>
    <p><strong>With the NSA:</strong> Your insurance processes the claim at in-network rates. Your copay/coinsurance is calculated on the in-network rate (let&rsquo;s say $300). You owe your normal cost-sharing on $300&mdash;perhaps <strong>$60</strong> in coinsurance. The cardiologist and your insurer sort out the rest.</p>
    <p><strong>Savings: $1,490.</strong></p>
</div>

<h2 id="good-faith-estimates">4. Good faith estimates for uninsured patients</h2>

<p>If you are uninsured or choose to self-pay, the No Surprises Act gives you a separate set of protections. (For additional strategies to reduce your bill as an uninsured patient, see our <a href="/guides/how-to-negotiate-medical-bills">negotiation guide</a>.)</p>

<ul>
    <li><strong>Right to a good faith estimate:</strong> Before any scheduled service, the provider must give you a written estimate of expected charges. You can also request one at any time.</li>
    <li><strong>$400 dispute threshold:</strong> If the final bill exceeds the good faith estimate by <strong>$400 or more</strong>, you can dispute it through the patient-provider dispute resolution process.</li>
    <li><strong>120-day filing window:</strong> You have 120 days from the date of the bill to initiate a dispute.</li>
    <li><strong>Independent review:</strong> A third-party reviewer examines the estimate and the final bill. If they side with you, the provider must accept a payment amount determined by the reviewer.</li>
</ul>

<div class="key-takeaway">
    <strong>For uninsured patients:</strong> Always request a good faith estimate in writing before any scheduled procedure. This creates a documented price commitment and gives you legal standing to dispute if the final bill is significantly higher.
</div>

<h2 id="spot-violation">5. How to spot a No Surprises Act violation</h2>

<p>Here&rsquo;s what a surprise bill looks like in practice. This patient went to an in-network ER, but the radiologist and anesthesiologist were out-of-network:</p>

<div class="bill-example">
    <div class="bill-header">Patient Bills Received &mdash; Memorial Hospital ER &mdash; Date of Service: 01/10/2026</div>
    <div class="line-item">
        <span><strong>Hospital bill (in-network)</strong></span>
        <span></span>
    </div>
    <div class="line-item">
        <span>99284 &mdash; ER Visit Level 4</span>
        <span>$2,890.00</span>
    </div>
    <div class="line-item">
        <span>74178 &mdash; CT Abdomen w/Contrast</span>
        <span>$2,400.00</span>
    </div>
    <div class="line-item">
        <span><strong>Separate bill from radiology group (out-of-network)</strong></span>
        <span></span>
    </div>
    <div class="line-item error">
        <span>74178-26 &mdash; CT Interpretation &nbsp; &#10060; <em>NSA violation: out-of-network provider at in-network ER</em></span>
        <span>$1,100.00</span>
    </div>
    <div class="line-item">
        <span><strong>Separate bill from anesthesia group (out-of-network)</strong></span>
        <span></span>
    </div>
    <div class="line-item error">
        <span>01916 &mdash; Anesthesia for CT &nbsp; &#10060; <em>NSA violation: patient did not choose this provider</em></span>
        <span>$1,800.00</span>
    </div>
    <div class="line-total">
        <span>TOTAL SURPRISE BILLS</span>
        <span>$2,900.00</span>
    </div>
</div>

<p>Under the No Surprises Act, the patient should owe only their in-network cost-sharing on the two surprise bills&mdash;not $2,900. If these were processed at in-network rates (approximately $180 + $240 in cost-sharing), the savings would be <strong>$2,480</strong>.</p>

<p>Check your bill for these red flags:</p>

<table>
    <thead>
        <tr><th>Red Flag</th><th>What It Means</th><th>Example</th></tr>
    </thead>
    <tbody>
        <tr><td>&ldquo;Out-of-network&rdquo; charges on an ER bill</td><td>ER visits are always covered by the NSA, regardless of network status.</td><td>An ER radiologist&rsquo;s bill says &ldquo;out-of-network, patient responsibility: $2,100&rdquo;</td></tr>
        <tr><td>Balance billing from a provider you didn&rsquo;t choose</td><td>If you went to an in-network hospital and received an out-of-network provider bill, this may violate the NSA.</td><td>An anesthesiologist sends a separate $3,400 bill for a surgery at an in-network hospital.</td></tr>
        <tr><td>Cost-sharing above in-network rates</td><td>Your copay/coinsurance should be calculated at in-network rates for NSA-covered services.</td><td>Your insurer applies a $5,000 out-of-network deductible instead of your $1,500 in-network deductible for an ER visit.</td></tr>
        <tr><td>A bill that exceeds a good faith estimate by $400+</td><td>If you&rsquo;re uninsured and received a written estimate, the $400 threshold triggers dispute rights.</td><td>Estimate said $3,200 for a knee MRI; final bill is $4,800.</td></tr>
    </tbody>
</table>

<p>If you suspect a surprise bill, look up the CPT codes to see what the in-network rate should be. The gap between what you were billed and the Medicare benchmark gives you a sense of how much may be in dispute:</p>

{_embed(mode="markup", title="Check your surprise bill", subtitle="Enter a CPT code and the amount you were billed to see the Medicare rate.", height="420")}

<p>You can also <a href="/scan">upload your bill to BillKarma</a> and our scanner automatically checks for potential No Surprises Act violations alongside other billing errors.</p>

<h2 id="what-to-do">6. What to do if you get a surprise bill</h2>

<ol>
    <li><strong>Confirm the NSA applies.</strong> Was it an emergency visit? Was it an out-of-network provider at an in-network facility you didn&rsquo;t consent to? If yes, you&rsquo;re protected.</li>
    <li><strong>Contact your insurance company.</strong> Call the member services number on your insurance card. Tell them you believe you have a No Surprises Act-protected claim and ask them to reprocess it at in-network rates.</li>
    <li><strong>Contact the provider&rsquo;s billing department.</strong> Tell them the bill violates the No Surprises Act. Cite the specific situation (emergency care, or out-of-network provider at an in-network facility). Request they resubmit to your insurer or adjust the bill.</li>
    <li><strong>Do not pay the surprise amount.</strong> Pay only your in-network cost-sharing (copay, coinsurance). Do not pay balance-billed amounts while the dispute is active.</li>
    <li><strong>File a complaint if the provider refuses.</strong> File at <a href="https://www.cms.gov/nosurprises" target="_blank" rel="noopener">cms.gov/nosurprises</a> or call the No Surprises Help Desk at 1-800-985-3059.</li>
    <li><strong>For uninsured disputes (good faith estimate):</strong> Initiate the patient-provider dispute resolution process at <a href="https://www.cms.gov/nosurprises/consumers/uninsured-or-self-pay-patients" target="_blank" rel="noopener">cms.gov/nosurprises</a> within 120 days.</li>
</ol>

<div class="key-takeaway">
    <strong>Keep all documents.</strong> Save your <a href="/guides/understanding-explanation-of-benefits">EOB</a>, the surprise bill, any good faith estimates, and records of all phone calls. These are your evidence if you need to file a formal complaint. Need help writing a dispute letter? See our <a href="/guides/how-to-dispute-a-medical-bill">step-by-step dispute guide</a>.
</div>

<div class="key-takeaway">
    <strong>Want to know what hospitals in your area typically charge for common procedures?</strong> Check <a href="/hospitals/">BillKarma&rsquo;s hospital directory</a> &mdash; it shows real pricing data so you can compare facilities and arrive at your next appointment armed with facts.
</div>

<h2 id="real-examples">7. Real examples of No Surprises Act protections</h2>

<div class="case-study">
    <h3>Example 1: Out-of-network anesthesiologist at in-network surgery center</h3>
    <p>A patient had outpatient knee surgery at an in-network surgery center. The anesthesiologist was out-of-network and billed <strong>$4,200</strong> for general anesthesia (CPT 01382). Under the NSA, the patient&rsquo;s cost-sharing was recalculated at in-network rates&mdash;a $60 copay instead of the $3,200 balance bill they initially received. <strong>Savings: $3,140.</strong></p>
</div>

<div class="case-study">
    <h3>Example 2: ER visit with out-of-network radiologist</h3>
    <p>A patient went to an in-network ER for a fall and had a CT scan. The ER doctor was in-network, but the radiologist who read the CT was out-of-network. The radiologist billed <strong>$1,100</strong> for the CT interpretation (CPT 74178-26). The patient&rsquo;s insurer initially processed it as out-of-network. After citing the NSA, it was reprocessed at in-network rates. The patient owed only their $40 copay. <strong>Savings: $870.</strong></p>
</div>

<div class="case-study">
    <h3>Example 3: Good faith estimate exceeded by $1,600</h3>
    <p>An uninsured patient received a good faith estimate of <strong>$2,400</strong> for an outpatient MRI. The final bill was <strong>$4,000</strong>&mdash;$1,600 over the estimate. The patient filed a dispute through the patient-provider dispute resolution process. The independent reviewer determined the reasonable charge was $2,700. <strong>Savings: $1,300.</strong></p>
</div>

<h2 id="faq">Frequently asked questions</h2>

<div class="faq-section">
    <div class="faq-item">
        <h3>What is the No Surprises Act?</h3>
        <p>The No Surprises Act is a federal law effective January 1, 2022, that protects patients from surprise medical bills in emergency situations and from out-of-network providers at in-network facilities. You can only be charged in-network cost-sharing rates in these situations.</p>
    </div>

    <div class="faq-item">
        <h3>Does the No Surprises Act apply to me if I have insurance?</h3>
        <p>Yes, if you have private health insurance (employer, marketplace, or individual plan). It does not apply to Medicare, Medicaid, TRICARE, or VA benefits, which have their own protections. Uninsured patients receive separate protections including the right to good faith estimates.</p>
    </div>

    <div class="faq-item">
        <h3>What should I do if I receive a surprise bill?</h3>
        <p>Contact your insurance company and the provider&rsquo;s billing department. Cite the No Surprises Act and request the bill be reprocessed at in-network rates. If they refuse, file a complaint at <a href="https://www.cms.gov/nosurprises" target="_blank" rel="noopener">cms.gov/nosurprises</a> or call 1-800-985-3059. Our <a href="/guides/how-to-dispute-a-medical-bill">dispute guide</a> has detailed templates.</p>
    </div>

    <div class="faq-item">
        <h3>What is a good faith estimate under the No Surprises Act?</h3>
        <p>A written estimate of expected charges that healthcare providers must give uninsured or self-pay patients before scheduled services. If the final bill exceeds the estimate by $400 or more, you can dispute it within 120 days through the patient-provider dispute resolution process.</p>
    </div>

    <div class="faq-item">
        <h3>Does the No Surprises Act cover ground ambulance bills?</h3>
        <p>No. Ground ambulance services are currently exempt. Air ambulance services are covered&mdash;you cannot be surprise-billed by an out-of-network air ambulance provider. Ground ambulance billing remains one of the most common sources of surprise bills.</p>
    </div>
</div>

<h2 id="sources">Sources</h2>

<ul class="sources-list">
    <li><a href="https://www.cms.gov/nosurprises" target="_blank" rel="noopener">CMS: No Surprises Act &mdash; Overview and Consumer Resources</a></li>
    <li><a href="https://www.cms.gov/nosurprises/consumers/uninsured-or-self-pay-patients" target="_blank" rel="noopener">CMS: Good Faith Estimates for Uninsured Patients</a></li>
    <li><a href="https://www.congress.gov/bill/116th-congress/house-bill/133" target="_blank" rel="noopener">No Surprises Act (Consolidated Appropriations Act, 2021) &mdash; Full Text</a></li>
    <li><a href="https://www.kff.org/private-insurance/issue-brief/no-surprises-act-implementation/" target="_blank" rel="noopener">KFF: No Surprises Act Implementation &mdash; What to Know</a></li>
    <li><a href="https://www.healthaffairs.org/content/forefront/no-surprises-act-year-later" target="_blank" rel="noopener">Health Affairs: The No Surprises Act, Impact Analysis</a></li>
    <li><a href="https://www.cms.gov/files/document/federal-independent-dispute-resolution-idr-process-guidance-disputes.pdf" target="_blank" rel="noopener">CMS: Independent Dispute Resolution (IDR) Process Guidance</a></li>
</ul>
""",
})
