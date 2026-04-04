"""Guide: Good Faith Estimate &mdash; Your Right to Know Costs Before Treatment."""

from guides import register, _embed

register("good-faith-estimate-rights", {
    "title": "Good Faith Estimate: Your Right to Know Costs Before Treatment",
    "meta_description": "Under the No Surprises Act, providers must give you a cost estimate in advance. Learn your GFE rights, how to request one, and what to do if the final bill is higher.",
    "published": "2026-02-27",
    "author": "BillKarma Team",
    "category": "Patient Rights",
    "faqs": [
        {
            "q": "What is a Good Faith Estimate?",
            "a": "A Good Faith Estimate (GFE) is a written document that healthcare providers must give uninsured or self-pay patients before scheduled, non-emergency services. It lists every expected charge for the procedure, including fees from all providers involved. The requirement was created by the No Surprises Act and took effect January 1, 2022. If your final bill exceeds the GFE by $400 or more, you have the legal right to dispute it.",
        },
        {
            "q": "Do I qualify for a Good Faith Estimate if I have insurance?",
            "a": "Yes, if you choose to pay out of pocket instead of using your insurance. The No Surprises Act requires GFEs for anyone who is uninsured or who chooses to self-pay. Simply tell the provider you will be paying out of pocket and request a GFE. If you plan to use your insurance, you can instead request an Advanced Explanation of Benefits (AEOB), which serves a similar purpose for insured patients.",
        },
        {
            "q": "How far in advance should I receive my Good Faith Estimate?",
            "a": "If you schedule a service at least 3 business days in advance, the provider must deliver the GFE within 1 business day after scheduling. If you schedule 10 or more business days ahead, the provider must deliver it within 3 business days after scheduling. You can also request a GFE at any time, and the provider must respond within 3 business days.",
        },
        {
            "q": "What can I do if my bill exceeds the Good Faith Estimate by $400 or more?",
            "a": "You can initiate the patient-provider dispute resolution process through HHS. File a dispute within 120 calendar days of receiving the bill. An independent reviewer will examine the GFE and the final bill. If the reviewer sides with you, the provider must accept the payment amount determined by the reviewer. There is a $25 administrative fee to file, which may be refunded if you win.",
        },
        {
            "q": "Can a hospital refuse to give me a Good Faith Estimate?",
            "a": "No. Under the No Surprises Act, healthcare providers and facilities are legally required to provide a Good Faith Estimate to any uninsured or self-pay patient who requests one or who schedules a service. If a provider refuses, you can file a complaint with the Centers for Medicare and Medicaid Services (CMS) at cms.gov/nosurprises or call 1-800-985-3059.",
        },
        {
            "q": "Does the Good Faith Estimate include all charges from all providers?",
            "a": "It should. The GFE must include expected charges from the primary provider and all co-providers or co-facilities reasonably expected to be involved, such as anesthesiologists, radiologists, and labs. Each provider's name, NPI, and expected charges must be listed. If a provider is missing from the GFE and later sends you a bill, that charge counts toward the $400 dispute threshold.",
        },
    ],
    "body": f"""
<p class="lead">Under the No Surprises Act, every uninsured or self-pay patient has the <strong>right</strong> to a written cost estimate before non-emergency treatment. It&rsquo;s called a Good Faith Estimate (GFE), and it&rsquo;s one of the most powerful &mdash; and underused &mdash; patient protections in federal law. If the final bill exceeds the estimate by <strong>$400 or more</strong>, you can dispute it through a formal federal process. Yet most patients have never heard of it, and many hospitals don&rsquo;t volunteer the information. Here&rsquo;s exactly how it works and how to use it.</p>

<nav class="toc">
    <h2>In this guide</h2>
    <ol>
        <li><a href="#what-is-gfe">What is a Good Faith Estimate?</a></li>
        <li><a href="#who-qualifies">Who qualifies for a GFE</a></li>
        <li><a href="#what-must-be-included">What must be included in a GFE</a></li>
        <li><a href="#how-to-request">How to request a Good Faith Estimate</a></li>
        <li><a href="#real-example">Real example: GFE vs. actual bill for a knee MRI</a></li>
        <li><a href="#how-to-dispute">How to dispute when the bill exceeds the GFE by $400+</a></li>
        <li><a href="#hospital-tricks">Common hospital tricks to avoid GFE obligations</a></li>
        <li><a href="#insured-patients">GFE for insured patients: the Advanced EOB</a></li>
        <li><a href="#faq">Frequently asked questions</a></li>
        <li><a href="#sources">Sources</a></li>
    </ol>
</nav>

<h2 id="what-is-gfe">1. What is a Good Faith Estimate?</h2>

<p>A Good Faith Estimate (GFE) is a written, itemized estimate of the total expected cost for a scheduled healthcare service. It was established by <strong>Section 112</strong> of the No Surprises Act (part of the Consolidated Appropriations Act of 2021) and took effect on <strong>January 1, 2022</strong>.</p>

<p>The law requires every healthcare provider and healthcare facility to provide a GFE to patients who are either uninsured or who choose to self-pay (not use their insurance) for a scheduled, non-emergency service. The GFE must be provided automatically when a service is scheduled, or within 3 business days if a patient requests one.</p>

<h3>Why it matters</h3>

<p>Before the GFE requirement, patients who asked &ldquo;how much will this cost?&rdquo; were routinely told &ldquo;we can&rsquo;t tell you until we see the final claim.&rdquo; The GFE changes that. It creates a <strong>legally binding cost commitment</strong> &mdash; not a vague range, but a specific itemized estimate. If the provider exceeds that estimate by $400 or more, the patient has a federal right to challenge the bill through an independent dispute resolution process.</p>

<div class="key-takeaway">
    <strong>The $400 rule:</strong> If your final bill is <strong>$400 or more</strong> above the Good Faith Estimate, you can dispute the entire bill &mdash; not just the overage &mdash; through the HHS patient-provider dispute resolution process. You have <strong>120 calendar days</strong> from receiving the bill to file.
</div>

<h2 id="who-qualifies">2. Who qualifies for a GFE</h2>

<p>The Good Faith Estimate requirement applies to a broader group of patients than most people realize:</p>

<table>
    <thead>
        <tr><th>Patient Type</th><th>Qualifies for GFE?</th><th>Details</th></tr>
    </thead>
    <tbody>
        <tr><td>Uninsured &mdash; no health coverage at all</td><td>Yes</td><td>Automatically entitled to a GFE for any scheduled non-emergency service</td></tr>
        <tr><td>Self-pay &mdash; has insurance but chooses not to use it</td><td>Yes</td><td>If you tell the provider you are paying out of pocket, you qualify. This is common when cash-pay prices are lower than the insured rate after deductible.</td></tr>
        <tr><td>Insured &mdash; using insurance to pay</td><td>Not for GFE (see AEOB below)</td><td>Insured patients using their coverage receive a different protection called an Advanced Explanation of Benefits. See <a href="#insured-patients">Section 8</a>.</td></tr>
        <tr><td>Medicare / Medicaid beneficiaries</td><td>No</td><td>Federal program beneficiaries are covered by program-specific billing protections instead</td></tr>
    </tbody>
</table>

<h3>The self-pay option most patients don&rsquo;t know about</h3>

<p>Here&rsquo;s a strategy many patients miss: even if you have insurance, you can choose to pay out of pocket for a specific service. This triggers the GFE requirement. Why would you do this? Because some providers offer cash-pay rates that are <strong>lower</strong> than what you&rsquo;d pay after your deductible. A knee MRI might cost $2,200 through insurance (applied to your $3,000 deductible) but only $450 at a cash-pay rate at a freestanding imaging center.</p>

<p>When you elect self-pay, you get a GFE with an itemized price commitment &mdash; and the $400 dispute protection if the provider overcharges.</p>

{_embed(mode="cost", cpt="73721", title="Compare knee MRI costs", subtitle="See what a knee MRI should cost in your area based on Medicare rates.", height="380")}

<div class="key-takeaway">
    <strong>Thinking about self-pay?</strong> Use the <a href="/calculator">BillKarma cost calculator</a> to compare cash-pay rates against your insurance cost (factoring in your deductible) before you decide. If cash-pay is cheaper, request a GFE to lock in the price.
</div>

<h2 id="what-must-be-included">3. What must be included in a GFE</h2>

<p>A valid Good Faith Estimate isn&rsquo;t a napkin with a dollar amount scrawled on it. Federal regulations (45 CFR &sect; 149.610) specify exactly what must appear:</p>

<table>
    <thead>
        <tr><th>Required Element</th><th>What It Means for You</th></tr>
    </thead>
    <tbody>
        <tr><td>Patient name and date of birth</td><td>Confirms the estimate is for you and your specific service</td></tr>
        <tr><td>Description of the primary service or item</td><td>Plain-language explanation of the procedure you&rsquo;re getting</td></tr>
        <tr><td>Itemized list of expected charges</td><td>Each individual service, supply, and fee &mdash; not a single lump sum</td></tr>
        <tr><td>CPT / HCPCS codes for each item</td><td>The billing codes allow you to verify pricing independently using tools like <a href="/calculator">our calculator</a></td></tr>
        <tr><td>ICD-10 diagnosis codes</td><td>The diagnosis codes justify the medical necessity of the services</td></tr>
        <tr><td>Name and NPI of each provider/facility</td><td>Every provider expected to bill you must be listed &mdash; the surgeon, anesthesiologist, lab, facility, etc.</td></tr>
        <tr><td>Service location</td><td>Where the service will be performed (affects pricing significantly)</td></tr>
        <tr><td>Expected date of service</td><td>When the procedure is scheduled</td></tr>
        <tr><td>Disclaimer about patient dispute rights</td><td>The GFE must include a notice that you can dispute a final bill that exceeds the estimate by $400+</td></tr>
    </tbody>
</table>

<div class="key-takeaway">
    <strong>Check every GFE for completeness.</strong> If any of these elements are missing, ask the provider to correct and reissue the estimate. An incomplete GFE weakens the provider&rsquo;s position if a dispute arises later. Pay special attention to co-providers &mdash; if the anesthesiologist isn&rsquo;t listed, their charges still count toward the $400 threshold.
</div>

<h2 id="how-to-request">4. How to request a Good Faith Estimate</h2>

<p>Providers are required to give you a GFE automatically when you schedule a service, but in practice many don&rsquo;t unless you ask. Here&rsquo;s the step-by-step process:</p>

<h3>Step 1: Schedule your procedure</h3>
<p>When you call to schedule, tell the scheduler: &ldquo;I am self-pay (or uninsured). I&rsquo;d like a Good Faith Estimate as required under the No Surprises Act.&rdquo; Say this on the recorded line, and note the date, time, and name of the person you spoke with.</p>

<h3>Step 2: Contact the billing department directly</h3>
<p>Don&rsquo;t rely on the scheduler to relay your request. Call the provider&rsquo;s billing department separately and repeat the request. Ask for the GFE to be emailed or mailed to you in writing. Verbal quotes are not Good Faith Estimates.</p>

<h3>Step 3: Confirm the GFE includes all providers</h3>
<p>When you receive the GFE, check that it lists charges from every provider who will be involved: the primary physician, anesthesiologist, radiologist, pathologist, lab, facility, and any assistant surgeons. If anyone is missing, call back and ask for a complete estimate.</p>

<h3>Step 4: Know the timeline</h3>

<table>
    <thead>
        <tr><th>Scenario</th><th>Provider Must Deliver GFE Within</th></tr>
    </thead>
    <tbody>
        <tr><td>Service scheduled at least 10 business days out</td><td>3 business days after scheduling</td></tr>
        <tr><td>Service scheduled 3&ndash;9 business days out</td><td>1 business day after scheduling</td></tr>
        <tr><td>You request a GFE (no service scheduled)</td><td>3 business days after your request</td></tr>
    </tbody>
</table>

<h3>Step 5: Save everything</h3>
<p>Keep a copy of the GFE in a safe place. Save the email, screenshot the portal, or photograph the paper copy. This document is your primary evidence if you need to dispute the final bill. Also save any communication where you requested the GFE, including call logs and email confirmations.</p>

<div class="key-takeaway">
    <strong>Pro tip:</strong> Request GFEs from <strong>multiple providers</strong> for the same procedure. Since GFEs include CPT codes, you can directly compare prices across facilities. A knee MRI GFE from a hospital might list $2,800 while a freestanding imaging center lists $475 for the exact same CPT code. Use the <a href="/calculator">BillKarma calculator</a> to verify that quoted prices are reasonable before you commit.
</div>

<h2 id="real-example">5. Real example: GFE vs. actual bill for a knee MRI</h2>

<p>Here&rsquo;s what a Good Faith Estimate dispute looks like in practice. This patient scheduled a knee MRI at a hospital outpatient imaging center as a self-pay patient and received a GFE before the procedure:</p>

<div class="bill-example">
    <div class="bill-header">Good Faith Estimate &mdash; Regional Medical Center &mdash; Knee MRI &mdash; Issued 03/01/2026</div>
    <div class="line-item">
        <span>73721 &mdash; MRI Knee w/o Contrast</span>
        <span>$1,350.00</span>
    </div>
    <div class="line-item">
        <span>73721-26 &mdash; Professional Interpretation (Radiologist)</span>
        <span>$280.00</span>
    </div>
    <div class="line-item">
        <span>Facility fee</span>
        <span>$420.00</span>
    </div>
    <div class="line-total">
        <span>GFE TOTAL</span>
        <span>$2,050.00</span>
    </div>
</div>

<p>Four weeks later, the patient received the actual bill:</p>

<div class="bill-example">
    <div class="bill-header">Actual Bill &mdash; Regional Medical Center &mdash; Date of Service: 03/10/2026</div>
    <div class="line-item">
        <span>73721 &mdash; MRI Knee w/o Contrast</span>
        <span>$1,350.00</span>
    </div>
    <div class="line-item">
        <span>73721-26 &mdash; Professional Interpretation (Radiologist)</span>
        <span>$280.00</span>
    </div>
    <div class="line-item">
        <span>Facility fee</span>
        <span>$420.00</span>
    </div>
    <div class="line-item error">
        <span>76000 &mdash; Fluoroscopy guidance &nbsp; &#10060; <em>Not on GFE</em></span>
        <span>$385.00</span>
    </div>
    <div class="line-item error">
        <span>99213 &mdash; Office visit (radiologist consult) &nbsp; &#10060; <em>Not on GFE</em></span>
        <span>$245.00</span>
    </div>
    <div class="line-total">
        <span>ACTUAL TOTAL</span>
        <span>$2,680.00</span>
    </div>
</div>

<p>The final bill exceeded the GFE by <strong>$630</strong> &mdash; well over the $400 dispute threshold. The two additional charges ($385 + $245 = $630) were not listed on the Good Faith Estimate. The patient had clear grounds to file a dispute.</p>

<div class="case-study">
    <h3>What happened next</h3>
    <p>The patient filed a dispute through the HHS patient-provider dispute resolution process, submitting the GFE and the final bill as evidence. The independent reviewer determined the fluoroscopy guidance was not medically necessary for a standard knee MRI and the office visit was not a separately billable service. The reviewer set the final allowed charge at <strong>$2,100</strong> &mdash; $50 above the GFE to account for minor supply cost variation. <strong>Savings: $580.</strong></p>
</div>

<p>Want to check whether specific CPT codes on your GFE or bill are priced fairly? Look up each code:</p>

{_embed(mode="markup", title="Check your GFE charges", subtitle="Enter a CPT code and amount from your estimate or bill to compare against Medicare rates.", height="420")}

<p>Already received a bill that looks higher than your estimate? <a href="/scan">Upload both documents to BillKarma</a> and we&rsquo;ll compare them line by line and flag every charge that exceeds the GFE.</p>

<h2 id="how-to-dispute">6. How to dispute when the bill exceeds the GFE by $400+</h2>

<p>The No Surprises Act created a formal <strong>patient-provider dispute resolution (PPDR)</strong> process administered by the Department of Health and Human Services. Here&rsquo;s exactly how it works:</p>

<h3>Step 1: Confirm the $400 threshold is met</h3>
<p>Compare your final bill to the GFE. Add up every charge that was not on the GFE, plus any charge that increased from the estimated amount. If the total difference is $400 or more, you qualify for the dispute process. Use the <a href="/calculator">BillKarma calculator</a> to verify each line item&rsquo;s reasonableness as additional evidence.</p>

<h3>Step 2: File within 120 calendar days</h3>
<p>You have <strong>120 calendar days</strong> from the date you received the bill (not the date of service) to initiate a dispute. Don&rsquo;t wait &mdash; gather your documents and file as soon as you confirm the discrepancy.</p>

<h3>Step 3: Submit your dispute to HHS</h3>
<p>File through the CMS dispute portal at <a href="https://www.cms.gov/nosurprises/consumers/uninsured-or-self-pay-patients" target="_blank" rel="noopener">cms.gov/nosurprises</a> or call <strong>1-800-985-3059</strong>. You will need to provide:</p>

<ul>
    <li>A copy of the Good Faith Estimate</li>
    <li>A copy of the final bill</li>
    <li>Your contact information</li>
    <li>A brief description of the discrepancy</li>
    <li>A $25 administrative fee (may be refunded if you prevail)</li>
</ul>

<h3>Step 4: The provider responds</h3>
<p>After you file, the provider has <strong>10 business days</strong> to submit their response, including any documentation justifying the higher charges. The provider may also choose to resolve the dispute directly with you during this period by reducing the bill to match the GFE.</p>

<h3>Step 5: Independent review</h3>
<p>An independent Selected Dispute Resolution (SDR) entity reviews both sides. They consider: the GFE, the final bill, any documentation from the provider explaining the increase, and whether the additional charges were reasonably foreseeable at the time the GFE was issued.</p>

<h3>Step 6: Binding determination</h3>
<p>The reviewer issues a determination within <strong>30 business days</strong>. If they side with you, the provider must accept the payment amount set by the reviewer. If they side with the provider, you owe the billed amount. The determination is binding on both parties.</p>

<div class="key-takeaway">
    <strong>Key advantage:</strong> You do not need a lawyer for the PPDR process. It was designed for individual patients. The $25 filing fee is deliberately low. The process is conducted via written submissions &mdash; no hearings, no courtrooms. Your strongest evidence is a complete GFE and a final bill that clearly exceeds it.
</div>

<h2 id="hospital-tricks">7. Common hospital tricks to avoid GFE obligations</h2>

<p>Not every provider makes the GFE process easy. Here are the most common tactics hospitals use to sidestep their obligations, and how to counter each one:</p>

<table>
    <thead>
        <tr><th>Hospital Tactic</th><th>Why They Do It</th><th>How to Counter</th></tr>
    </thead>
    <tbody>
        <tr>
            <td>&ldquo;We don&rsquo;t provide estimates for that service&rdquo;</td>
            <td>Staff may not be trained on the GFE requirement or may hope you&rsquo;ll drop the request</td>
            <td>Cite the No Surprises Act, Section 112. Say: &ldquo;Federal law requires you to provide a Good Faith Estimate. I&rsquo;d like to speak with your compliance officer.&rdquo;</td>
        </tr>
        <tr>
            <td>Giving a verbal quote instead of a written GFE</td>
            <td>A verbal quote is not enforceable &mdash; they can later claim they said something different</td>
            <td>Insist on a written estimate. Say: &ldquo;I need the Good Faith Estimate in writing with CPT codes and provider details as required by 45 CFR 149.610.&rdquo;</td>
        </tr>
        <tr>
            <td>Providing a GFE that lists only the primary provider</td>
            <td>Omitting the anesthesiologist, radiologist, or lab means those charges aren&rsquo;t &ldquo;estimated&rdquo; &mdash; giving the hospital an argument that the GFE was accurate for what it covered</td>
            <td>Ask: &ldquo;Does this include all co-providers and co-facilities? Please list every provider who will bill me.&rdquo; Missing providers&rsquo; charges still count toward the $400 threshold.</td>
        </tr>
        <tr>
            <td>Adding a disclaimer that the GFE is &ldquo;not a guarantee&rdquo;</td>
            <td>Attempting to undermine your dispute rights with fine print</td>
            <td>The law is clear: the $400 dispute right applies regardless of disclaimer language. A disclaimer does not override federal law.</td>
        </tr>
        <tr>
            <td>Pressuring you to provide insurance information</td>
            <td>If they classify you as insured, they don&rsquo;t have to provide a GFE &mdash; only an AEOB (which has weaker protections currently)</td>
            <td>You have the right to elect self-pay. Say: &ldquo;I am choosing to self-pay for this service. Please process me as a self-pay patient and provide a Good Faith Estimate.&rdquo;</td>
        </tr>
        <tr>
            <td>Delaying the GFE until after the service</td>
            <td>If they never provide the GFE, you have nothing to dispute against</td>
            <td>Document every request with dates. If the GFE is not provided within the required timeline, file a complaint at <a href="https://www.cms.gov/nosurprises" target="_blank" rel="noopener">cms.gov/nosurprises</a> before your procedure.</td>
        </tr>
    </tbody>
</table>

<div class="key-takeaway">
    <strong>Already received a bill without ever getting a GFE?</strong> <a href="/scan">Upload your bill to BillKarma</a> to identify overcharges, then contact the provider&rsquo;s billing department and cite their failure to provide a GFE as additional leverage in your negotiation. Failure to provide a GFE is itself a violation of the No Surprises Act. You can also check <a href="/hospitals/">hospital pricing data</a> to see whether the facility has a history of price transparency compliance.
</div>

<h2 id="insured-patients">8. GFE for insured patients: the Advanced EOB</h2>

<p>If you plan to use your insurance, the Good Faith Estimate requirement doesn&rsquo;t directly apply to you. Instead, the No Surprises Act created a parallel protection called the <strong>Advanced Explanation of Benefits (AEOB)</strong>.</p>

<h3>What is an Advanced EOB?</h3>
<p>An AEOB is a document your insurance company provides before a scheduled service. It shows:</p>

<ul>
    <li>Whether the provider is in-network or out-of-network</li>
    <li>The estimated allowed amount for each service</li>
    <li>Your estimated cost-sharing (deductible, copay, coinsurance)</li>
    <li>How much of your deductible has been met</li>
    <li>Whether prior authorization is required or has been obtained</li>
</ul>

<h3>How the AEOB differs from a GFE</h3>

<table>
    <thead>
        <tr><th>Feature</th><th>Good Faith Estimate (GFE)</th><th>Advanced EOB (AEOB)</th></tr>
    </thead>
    <tbody>
        <tr><td>Who receives it</td><td>Uninsured or self-pay patients</td><td>Insured patients using coverage</td></tr>
        <tr><td>Who provides it</td><td>The healthcare provider</td><td>Your insurance company (based on provider&rsquo;s submission)</td></tr>
        <tr><td>$400 dispute right</td><td>Yes &mdash; federal dispute process</td><td>Not currently &mdash; AEOB enforcement rules are still being finalized</td></tr>
        <tr><td>Legal requirement</td><td>Fully in effect since January 2022</td><td>Implementation has been delayed; full rollout pending</td></tr>
        <tr><td>What it shows</td><td>Provider&rsquo;s expected charges, CPT codes, diagnosis codes</td><td>Insurer&rsquo;s estimated allowed amounts and your cost-sharing</td></tr>
    </tbody>
</table>

<h3>What insured patients should do now</h3>
<p>While AEOB implementation is still rolling out, insured patients can take these steps to get cost clarity before a procedure:</p>

<ol>
    <li><strong>Call your insurer</strong> and ask for a pre-service cost estimate. Many insurers will provide one informally even without a formal AEOB.</li>
    <li><strong>Ask the provider for a cost estimate</strong> even if you&rsquo;re insured. They&rsquo;re not legally required to give you a GFE, but many billing departments will provide an informal estimate if asked.</li>
    <li><strong>Check your benefits summary</strong> to understand your deductible status, copay amounts, and coinsurance percentages before scheduling.</li>
    <li><strong>Consider self-pay</strong> if the cash price is lower than your insured cost after deductible. This triggers the full GFE protection. Use our <a href="/calculator">cost calculator</a> to compare.</li>
</ol>

<p>For a deeper understanding of how the No Surprises Act protects both insured and uninsured patients, see our <a href="/guides/no-surprises-act-explained">complete No Surprises Act guide</a>.</p>

<div class="key-takeaway">
    <strong>Facing a large bill you weren&rsquo;t expecting?</strong> Whether you&rsquo;re insured or self-pay, <a href="/scan">scanning your bill with BillKarma</a> is the fastest way to find overcharges, coding errors, and charges that exceed reasonable benchmarks. Our scanner checks every line against Medicare rates and flags the charges most worth disputing. Need help negotiating? Our <a href="/guides/how-to-negotiate-medical-bills">negotiation guide</a> walks you through the process step by step.
</div>

<h2 id="faq">Frequently asked questions</h2>

<div class="faq-section">
    <div class="faq-item">
        <h3>What is a Good Faith Estimate?</h3>
        <p>A Good Faith Estimate (GFE) is a written, itemized estimate of expected charges that healthcare providers must give uninsured or self-pay patients before scheduled non-emergency services. It was established by the No Surprises Act and took effect January 1, 2022. If the final bill exceeds the GFE by $400 or more, you have the right to dispute it through a federal process.</p>
    </div>

    <div class="faq-item">
        <h3>Do I qualify for a Good Faith Estimate if I have insurance?</h3>
        <p>Yes, if you choose to pay out of pocket instead of using your insurance. Tell the provider you will be self-pay and request a GFE. If you plan to use your insurance, you can request an Advanced Explanation of Benefits (AEOB) from your insurer instead, though AEOB enforcement is still being phased in.</p>
    </div>

    <div class="faq-item">
        <h3>How far in advance should I receive my Good Faith Estimate?</h3>
        <p>If you schedule at least 10 business days ahead, the provider must deliver the GFE within 3 business days after scheduling. If you schedule 3&ndash;9 business days out, it must arrive within 1 business day. If you request a GFE without scheduling, the provider has 3 business days to respond.</p>
    </div>

    <div class="faq-item">
        <h3>What can I do if my bill exceeds the Good Faith Estimate by $400 or more?</h3>
        <p>File a dispute through the HHS patient-provider dispute resolution process at <a href="https://www.cms.gov/nosurprises/consumers/uninsured-or-self-pay-patients" target="_blank" rel="noopener">cms.gov/nosurprises</a> or call 1-800-985-3059. You have 120 calendar days from the date you received the bill. An independent reviewer will examine both documents and issue a binding determination. The filing fee is $25.</p>
    </div>

    <div class="faq-item">
        <h3>Can a hospital refuse to give me a Good Faith Estimate?</h3>
        <p>No. Federal law requires healthcare providers and facilities to provide a GFE to any uninsured or self-pay patient who requests one or schedules a service. If a provider refuses, file a complaint with CMS at <a href="https://www.cms.gov/nosurprises" target="_blank" rel="noopener">cms.gov/nosurprises</a> or call 1-800-985-3059. Document your request including dates and names of staff you spoke with.</p>
    </div>

    <div class="faq-item">
        <h3>Does the Good Faith Estimate include all charges from all providers?</h3>
        <p>It should. The GFE must list expected charges from the primary provider and all co-providers or co-facilities reasonably expected to be involved &mdash; including anesthesiologists, radiologists, labs, and the facility itself. Each provider&rsquo;s name, NPI, and estimated charges must appear. If a provider is missing and later sends a bill, that charge counts toward the $400 dispute threshold.</p>
    </div>
</div>

<h2 id="sources">Sources</h2>

<ul class="sources-list">
    <li><a href="https://www.cms.gov/nosurprises/consumers/uninsured-or-self-pay-patients" target="_blank" rel="noopener">CMS: Good Faith Estimates for Uninsured or Self-Pay Patients</a></li>
    <li><a href="https://www.cms.gov/nosurprises" target="_blank" rel="noopener">CMS: No Surprises Act &mdash; Overview and Consumer Resources</a></li>
    <li><a href="https://www.hhs.gov/about/news/2021/12/27/hhs-kicks-off-new-year-with-new-protections-from-surprise-medical-bills.html" target="_blank" rel="noopener">HHS: Patient-Provider Dispute Resolution Process &mdash; Final Rule</a></li>
    <li><a href="https://www.congress.gov/bill/116th-congress/house-bill/133" target="_blank" rel="noopener">No Surprises Act (Consolidated Appropriations Act, 2021) &mdash; Section 112: Good Faith Estimates</a></li>
    <li><a href="https://www.federalregister.gov/documents/2021/10/07/2021-21441/requirements-related-to-surprise-billing-part-i" target="_blank" rel="noopener">Federal Register: Requirements Related to Surprise Billing &mdash; Good Faith Estimate Provisions (45 CFR 149.610)</a></li>
    <li><a href="https://www.kff.org/private-insurance/issue-brief/no-surprises-act-implementation/" target="_blank" rel="noopener">KFF: No Surprises Act Implementation &mdash; What to Know</a></li>
</ul>
""",
})
