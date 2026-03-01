"""Guide: What Is a Superbill."""

from guides import register, _embed

register("what-is-a-superbill", {
    "title": "What Is a Superbill? How to Get Out-of-Network Insurance Reimbursement",
    "meta_description": "A superbill lets you get reimbursed by insurance for out-of-network care. Learn what a superbill is, how to request one, and how to submit it for maximum reimbursement.",
    "published": "2026-03-01",
    "author": "BillKarma Team",
    "category": "Insurance",
    "faqs": [
        {
            "q": "What is a superbill in medical billing?",
            "a": "A superbill is a detailed receipt from a healthcare provider that contains all the information your insurance company needs to process an out-of-network claim. It includes the provider\u2019s name, NPI number, tax ID, your diagnosis codes (ICD-10), procedure codes (CPT), dates of service, and the amount you paid. Unlike a regular receipt, a superbill is formatted specifically for insurance reimbursement. You submit it to your insurer, and they reimburse you based on your out-of-network benefits.",
        },
        {
            "q": "Can I get reimbursed by insurance using a superbill?",
            "a": "Yes, if your health insurance plan includes out-of-network benefits. Most PPO and POS plans reimburse a percentage of out-of-network charges after you meet your out-of-network deductible. HMO plans typically do not cover out-of-network care except in emergencies, so a superbill would not result in reimbursement under most HMO plans. Check your plan\u2019s Summary of Benefits to confirm your out-of-network coverage before submitting.",
        },
        {
            "q": "How long does it take to get reimbursed after submitting a superbill?",
            "a": "Most insurance companies process out-of-network claims within 30 to 45 days of receiving a complete superbill. Some insurers take up to 60 days. If your claim is denied or delayed, call the number on the back of your insurance card and ask for a status update. Keep copies of everything you submit, including the date you mailed or uploaded the superbill.",
        },
        {
            "q": "What is the difference between a superbill and an invoice?",
            "a": "A regular invoice or receipt shows the provider\u2019s name, the date, and the amount you paid. A superbill includes all of that plus the specific CPT procedure codes, ICD-10 diagnosis codes, the provider\u2019s NPI number, tax ID, place of service code, and other fields that insurance companies require to adjudicate a claim. Without these fields, your insurer will reject the submission.",
        },
        {
            "q": "Do all providers give superbills?",
            "a": "Most out-of-network providers are familiar with superbills and will provide one if you ask. Therapists, psychologists, psychiatrists, dietitians, chiropractors, acupuncturists, and other specialists who frequently see patients on a cash-pay basis typically have superbills ready to generate from their billing software. Some providers issue them automatically after each visit; others require you to request one. Always ask before or at the time of your appointment.",
        },
        {
            "q": "Can I submit a superbill for therapy or mental health visits?",
            "a": "Yes. Therapy is one of the most common uses for superbills. Many therapists and psychologists do not accept insurance directly but will provide a superbill so you can seek reimbursement from your insurer. Under the Mental Health Parity and Addiction Equity Act, your insurer must cover mental health services at the same level as medical services, including out-of-network benefits. If your plan covers 60% of out-of-network medical visits, it must also cover 60% of out-of-network therapy.",
        },
    ],
    "body": f"""
<p class="lead">You paid out of pocket for a doctor visit, a therapy session, or a specialist appointment &mdash; and now you want your insurance to reimburse you. The tool that makes this possible is called a <strong>superbill</strong>. A superbill is a detailed receipt your provider gives you that contains every piece of information your insurance company needs to process an out-of-network claim: diagnosis codes, procedure codes, the provider&rsquo;s NPI, and more. If your plan has out-of-network benefits, submitting a superbill can get you <strong>40&ndash;80%</strong> of your payment back. This guide walks you through every step &mdash; from requesting a superbill to maximizing your reimbursement.</p>

<nav class="toc">
    <h2>In this guide</h2>
    <ol>
        <li><a href="#what-is-a-superbill">What is a superbill?</a></li>
        <li><a href="#when-you-need-one">When you need a superbill</a></li>
        <li><a href="#required-information">What information a superbill must contain</a></li>
        <li><a href="#how-to-request">How to request a superbill from your provider</a></li>
        <li><a href="#how-to-submit">How to submit a superbill to your insurance</a></li>
        <li><a href="#reimbursement-amounts">How much you&rsquo;ll get reimbursed</a></li>
        <li><a href="#common-mistakes">Common superbill mistakes that cause claim denials</a></li>
        <li><a href="#faq">Frequently asked questions</a></li>
        <li><a href="#sources">Sources</a></li>
    </ol>
</nav>

<h2 id="what-is-a-superbill">1. What is a superbill?</h2>

<p>A superbill is a standardized document that your healthcare provider creates after a visit. It includes every data element your insurance company needs to adjudicate an out-of-network claim &mdash; procedure codes (CPT), diagnosis codes (ICD-10), the provider&rsquo;s National Provider Identifier (NPI), place of service, and the fee charged. Think of it as a receipt designed specifically for insurance reimbursement.</p>

<h3>Superbill vs. regular receipt</h3>

<table>
    <thead>
        <tr><th>Element</th><th>Regular Receipt</th><th>Superbill</th></tr>
    </thead>
    <tbody>
        <tr><td>Provider name and address</td><td>Yes</td><td>Yes</td></tr>
        <tr><td>Date of service</td><td>Yes</td><td>Yes</td></tr>
        <tr><td>Amount paid</td><td>Yes</td><td>Yes</td></tr>
        <tr><td>CPT procedure codes</td><td>No</td><td>Yes</td></tr>
        <tr><td>ICD-10 diagnosis codes</td><td>No</td><td>Yes</td></tr>
        <tr><td>Provider NPI number</td><td>No</td><td>Yes</td></tr>
        <tr><td>Provider tax ID (EIN)</td><td>No</td><td>Yes</td></tr>
        <tr><td>Place of service code</td><td>No</td><td>Yes</td></tr>
        <tr><td>Patient date of birth</td><td>Rarely</td><td>Yes</td></tr>
    </tbody>
</table>

<p>When you see an in-network provider, the provider files the claim directly with your insurer. You never touch the paperwork. When you see an out-of-network provider, you typically pay the full fee upfront, and the provider does <em>not</em> file a claim for you. The superbill is what allows you to file that claim yourself and get reimbursed.</p>

<div class="key-takeaway">
    <strong>Key distinction:</strong> A superbill is not a bill &mdash; it&rsquo;s a receipt with medical codes. You have already paid the provider. The superbill is what you submit to your insurance company to get a portion of that payment back. <a href="/guides/how-health-insurance-works">Learn how insurance reimbursement works</a>.
</div>

<h2 id="when-you-need-one">2. When you need a superbill</h2>

<p>You need a superbill any time you pay a provider out of pocket and want to seek reimbursement from your insurance. The most common scenarios include:</p>

<ul>
    <li><strong>Out-of-network providers</strong> &mdash; Your provider doesn&rsquo;t accept your insurance, but your plan (PPO or POS) has out-of-network benefits that will reimburse part of the cost.</li>
    <li><strong>Therapy and mental health</strong> &mdash; Many therapists, psychologists, and psychiatrists operate on a cash-pay basis. Superbills are the standard way their patients get reimbursed.</li>
    <li><strong>Specialists</strong> &mdash; Dermatologists, nutritionists, acupuncturists, chiropractors, and other specialists who practice outside insurance networks.</li>
    <li><strong>Cash-pay visits by choice</strong> &mdash; Some patients prefer to pay cash for privacy or convenience, then submit a superbill later for partial reimbursement.</li>
    <li><strong>Out-of-area care</strong> &mdash; You received care while traveling and the provider was not in your plan&rsquo;s network.</li>
</ul>

<p>Before requesting a superbill, verify that your insurance plan has out-of-network benefits. Most PPO plans do. Most HMO plans do <em>not</em> (except for emergencies). Check your plan&rsquo;s Summary of Benefits and Coverage, or call the member services number on the back of your insurance card. For more on how plan types differ, see our <a href="/guides/how-health-insurance-works">guide to how health insurance works</a>.</p>

<h2 id="required-information">3. What information a superbill must contain</h2>

<p>A superbill is only useful if it contains every field your insurer requires. Missing even one element &mdash; especially the NPI or diagnosis code &mdash; will result in a denied claim. Here is what a complete superbill looks like:</p>

<div class="bill-example">
    <div class="bill-header">Superbill &mdash; Sample &mdash; Date of Service: 02/15/2026</div>
    <div class="line-item">
        <span><strong>Provider Name:</strong> Dr. Sarah Chen, PhD, Licensed Psychologist</span>
        <span></span>
    </div>
    <div class="line-item">
        <span><strong>Provider NPI:</strong> 1234567890 &nbsp; &#9888; <em>Required &mdash; 10-digit National Provider Identifier</em></span>
        <span></span>
    </div>
    <div class="line-item">
        <span><strong>Tax ID (EIN):</strong> 12-3456789</span>
        <span></span>
    </div>
    <div class="line-item">
        <span><strong>Office Address:</strong> 450 Park Ave, Suite 301, New York, NY 10022</span>
        <span></span>
    </div>
    <div class="line-item">
        <span><strong>Patient Name:</strong> Jane Smith &nbsp;|&nbsp; <strong>DOB:</strong> 04/12/1988</span>
        <span></span>
    </div>
    <div class="line-item">
        <span><strong>Diagnosis (ICD-10):</strong> F41.1 &mdash; Generalized anxiety disorder &nbsp; &#9888; <em>Required &mdash; must match the CPT code</em></span>
        <span></span>
    </div>
    <div class="line-item">
        <span><strong>Procedure (CPT):</strong> 90837 &mdash; Psychotherapy, 53&ndash;60 minutes</span>
        <span>$250.00</span>
    </div>
    <div class="line-item">
        <span><strong>Place of Service:</strong> 11 (Office) &nbsp; &#9888; <em>Required &mdash; 2-digit CMS code</em></span>
        <span></span>
    </div>
    <div class="line-total">
        <span>TOTAL PAID BY PATIENT</span>
        <span>$250.00</span>
    </div>
</div>

<h3>Required fields checklist</h3>

<ul>
    <li><strong>Provider&rsquo;s full name and credentials</strong> (MD, PhD, LCSW, etc.)</li>
    <li><strong>Provider&rsquo;s NPI number</strong> &mdash; a unique 10-digit identifier issued by CMS. You can verify any provider&rsquo;s NPI at the NPPES NPI Registry.</li>
    <li><strong>Provider&rsquo;s tax ID (EIN or SSN)</strong></li>
    <li><strong>Provider&rsquo;s office address and phone number</strong></li>
    <li><strong>Patient&rsquo;s full legal name and date of birth</strong></li>
    <li><strong>Date of service</strong></li>
    <li><strong>CPT code(s)</strong> &mdash; the specific procedure or service codes. See our <a href="/guides/cpt-codes-explained">CPT codes guide</a> for common codes.</li>
    <li><strong>ICD-10 diagnosis code(s)</strong> &mdash; the medical reason for the visit</li>
    <li><strong>Fee charged per CPT code</strong></li>
    <li><strong>Place of service code</strong> &mdash; a 2-digit code indicating where care was provided (11 = office, 02 = telehealth, etc.)</li>
    <li><strong>Provider&rsquo;s signature</strong> (some insurers require it; include it to be safe)</li>
</ul>

<div class="key-takeaway">
    <strong>Pro tip:</strong> Before you leave the provider&rsquo;s office, review the superbill and verify that the NPI, CPT codes, and ICD-10 codes are all present. A superbill missing any of these three fields will almost certainly be rejected by your insurer. Use our <a href="/calculator">free calculator</a> to look up the Medicare rate for your CPT codes so you know what a fair reimbursement looks like.
</div>

<h2 id="how-to-request">4. How to request a superbill from your provider</h2>

<p>Most out-of-network providers are familiar with superbills. Many therapists and specialists generate them automatically. But if your provider doesn&rsquo;t offer one unprompted, you need to ask. Here&rsquo;s exactly what to say:</p>

<h3>Script: requesting a superbill</h3>

<p>&ldquo;Hi, I&rsquo;m paying out of pocket for today&rsquo;s visit and I&rsquo;d like to submit a claim to my insurance for out-of-network reimbursement. Could you please provide me with a superbill that includes your NPI number, the CPT codes for today&rsquo;s services, the ICD-10 diagnosis codes, and the place of service code? I need all of those fields for my insurer to process the claim.&rdquo;</p>

<h3>When to ask</h3>

<ul>
    <li><strong>Before the appointment</strong> &mdash; Confirm the provider can generate a superbill. Ask during scheduling: &ldquo;Do you provide superbills for insurance reimbursement?&rdquo;</li>
    <li><strong>At checkout</strong> &mdash; Request the superbill before you leave. Some providers email it within 24&ndash;48 hours; confirm the timeline.</li>
    <li><strong>After the visit</strong> &mdash; If you forgot to ask, call or email the office. Most providers can generate a superbill retroactively for past visits.</li>
</ul>

<h3>What if your provider doesn&rsquo;t know what a superbill is?</h3>

<p>This is rare, but it happens &mdash; especially with newer practices or non-traditional providers. In that case, explain that you need a receipt that includes CPT codes, ICD-10 codes, and their NPI number. Any modern electronic health record (EHR) system can generate a superbill. If the provider truly cannot produce one, ask for an itemized receipt with as much detail as possible and add the missing fields yourself using the provider&rsquo;s NPI lookup at <a href="https://npiregistry.cms.hhs.gov/" target="_blank" rel="noopener">npiregistry.cms.hhs.gov</a>.</p>

<h2 id="how-to-submit">5. How to submit a superbill to your insurance</h2>

<p>Once you have a complete superbill, submitting it to your insurer is straightforward. Here is the step-by-step process:</p>

<p><strong>Step 1 &mdash; Get the out-of-network claim form.</strong> Go to your insurer&rsquo;s website and download the out-of-network (or &ldquo;member reimbursement&rdquo;) claim form. Most major insurers &mdash; Aetna, Blue Cross Blue Shield, Cigna, UnitedHealthcare &mdash; have this form available in the member portal. You can also call member services and ask them to mail or email it.</p>

<p><strong>Step 2 &mdash; Fill out the claim form.</strong> The form asks for your subscriber information (name, member ID, group number, date of birth), the patient&rsquo;s information (if different from the subscriber), and the provider&rsquo;s information. Most of this is on your insurance card and the superbill itself.</p>

<p><strong>Step 3 &mdash; Attach the superbill.</strong> Attach the superbill as supporting documentation. Some insurers also want a copy of the receipt showing you paid the provider. Attach both if you have them.</p>

<p><strong>Step 4 &mdash; Submit the claim.</strong> You can typically submit by:</p>
<ul>
    <li><strong>Online portal</strong> &mdash; Upload the claim form and superbill through your insurer&rsquo;s member portal. This is the fastest method.</li>
    <li><strong>Mail</strong> &mdash; Send the claim form, superbill, and receipt to the address listed on the form. Use certified mail so you have proof of delivery.</li>
    <li><strong>Fax</strong> &mdash; Some insurers accept claims by fax. Check the claim form for the fax number.</li>
</ul>

<p><strong>Step 5 &mdash; Track the claim.</strong> Log into your insurer&rsquo;s portal to check the claim status. Most claims are processed within 30&ndash;45 days. If it&rsquo;s been more than 45 days with no update, call member services with your claim reference number.</p>

<div class="key-takeaway">
    <strong>Submit monthly, not annually.</strong> If you have recurring out-of-network visits (like weekly therapy), submit your superbills monthly rather than waiting until year-end. This gets you reimbursed faster and reduces the chance of losing paperwork. Many therapists will provide a monthly superbill that lists all sessions for that month on a single document.
</div>

{_embed(mode="cost", cpt="90837", title="Look up the Medicare rate for your visit", subtitle="Enter your CPT code to see what Medicare pays &mdash; this is the baseline your insurer uses to calculate reimbursement.")}

<h2 id="reimbursement-amounts">6. How much you&rsquo;ll get reimbursed</h2>

<p>Your reimbursement amount depends on three factors: your out-of-network deductible, your plan&rsquo;s allowed amount (also called the usual, customary, and reasonable rate &mdash; or UCR), and your coinsurance percentage.</p>

<h3>How the calculation works</h3>

<p>Here&rsquo;s a simplified example for a $250 therapy session (CPT 90837):</p>

<table>
    <thead>
        <tr><th>Factor</th><th>Amount</th><th>Explanation</th></tr>
    </thead>
    <tbody>
        <tr><td>You paid the provider</td><td>$250</td><td>Full fee, paid at the time of service</td></tr>
        <tr><td>Your insurer&rsquo;s allowed amount (UCR)</td><td>$180</td><td>What your insurer considers &ldquo;reasonable&rdquo; for this service in your area</td></tr>
        <tr><td>Out-of-network deductible met?</td><td>Yes</td><td>You&rsquo;ve already met your annual out-of-network deductible</td></tr>
        <tr><td>Out-of-network coinsurance</td><td>60%</td><td>Your plan pays 60% of the allowed amount after deductible</td></tr>
        <tr><td>Your reimbursement</td><td>$108</td><td>60% of $180 = $108</td></tr>
        <tr><td>Your final out-of-pocket cost</td><td>$142</td><td>$250 &minus; $108 = $142</td></tr>
    </tbody>
</table>

<h3>Key terms that affect your reimbursement</h3>

<ul>
    <li><strong>UCR (Usual, Customary, and Reasonable) rate</strong> &mdash; The maximum amount your insurer considers fair for a service in your geographic area. Your insurer calculates reimbursement based on this amount, not on what you actually paid. If you paid $250 but the UCR is $180, the insurer only considers $180.</li>
    <li><strong>Out-of-network deductible</strong> &mdash; The amount you must pay out of pocket before your insurer starts reimbursing out-of-network claims. This is separate from (and usually higher than) your in-network deductible. Common amounts: $1,000&ndash;$5,000 per year.</li>
    <li><strong>Out-of-network coinsurance</strong> &mdash; The percentage your plan pays after the deductible is met. Typical out-of-network coinsurance ranges from 40% to 70%. See our <a href="/guides/copay-vs-coinsurance-vs-deductible">copay vs. coinsurance vs. deductible guide</a> for details.</li>
    <li><strong>Out-of-network out-of-pocket maximum</strong> &mdash; The most you&rsquo;ll pay in a year for out-of-network care. After you hit this cap, your plan pays 100%. Not all plans have an out-of-network out-of-pocket maximum &mdash; check your Summary of Benefits.</li>
</ul>

<div class="case-study">
    <h3>Case study: therapy patient getting reimbursed through superbills</h3>
    <p>Maria, a 34-year-old in Chicago, sees an out-of-network therapist weekly at $200 per session (CPT 90837). Her PPO plan has a $1,500 out-of-network deductible and 60% coinsurance with a UCR of $165 for 90837 in her zip code. For the first 10 sessions ($2,000 total), she met her deductible. Starting with session 10, her insurer began reimbursing 60% of $165 = <strong>$99 per session</strong>. Over the remaining 42 sessions in the year, Maria was reimbursed <strong>$4,158</strong> on $8,400 in therapy costs. Her effective cost dropped from $200 to $101 per session &mdash; a 50% savings.</p>
</div>

<div class="case-study">
    <h3>Case study: specialist visit reimbursement with a superbill</h3>
    <p>David, a 52-year-old in Denver, saw an out-of-network dermatologist for a suspicious mole evaluation and biopsy. The visit included CPT 99203 (new patient office visit, Level 3, $325) and CPT 11102 (tangential biopsy of skin, $285) &mdash; total $610. His PPO plan had already met the $2,000 out-of-network deductible from earlier claims. His plan&rsquo;s UCR for 99203 was $195 and for 11102 was $165 &mdash; total allowed amount of $360. With 50% out-of-network coinsurance, David was reimbursed <strong>$180</strong>. His final cost was $430 instead of $610 &mdash; a <strong>$180 savings</strong> for 15 minutes of paperwork.</p>
</div>

<h2 id="common-mistakes">7. Common superbill mistakes that cause claim denials</h2>

<p>Insurance companies deny out-of-network claims for specific, avoidable reasons. Here are the most common mistakes and how to prevent them:</p>

<h3>a) Missing or incorrect NPI number</h3>

<p>The provider&rsquo;s NPI is the single most important field on a superbill. If it&rsquo;s missing, incorrect, or doesn&rsquo;t match the provider who rendered the service, your claim will be denied. Before submitting, verify the NPI at <a href="https://npiregistry.cms.hhs.gov/" target="_blank" rel="noopener">npiregistry.cms.hhs.gov</a>.</p>

<h3>b) Diagnosis code doesn&rsquo;t support the procedure code</h3>

<p>Every CPT code must be paired with an ICD-10 diagnosis code that justifies the service. If a therapist bills CPT 90837 (psychotherapy) but the superbill lists ICD-10 code Z00.00 (general health exam) instead of a mental health diagnosis like F41.1 (generalized anxiety disorder), the insurer will deny the claim as not medically necessary. Ask your provider to confirm the diagnosis code matches the service.</p>

<h3>c) Missing place of service code</h3>

<p>The place of service (POS) code tells the insurer where care was delivered. Common codes: 11 (office), 02 (telehealth), 12 (patient&rsquo;s home). If this field is blank, many insurers will reject the claim outright. It&rsquo;s an easy field to overlook &mdash; make sure your provider includes it.</p>

<h3>d) Submitting past the filing deadline</h3>

<p>Every insurer has a deadline for submitting out-of-network claims, typically 90 days to one year from the date of service. If you miss this deadline, the insurer has no obligation to reimburse you. Check your plan documents for the exact filing deadline and submit promptly.</p>

<h3>e) Using the wrong claim form</h3>

<p>Each insurer has its own out-of-network claim form. Submitting a generic form or a form from the wrong insurer will delay or prevent processing. Always download the form directly from your insurer&rsquo;s member portal.</p>

<h3>f) Not including proof of payment</h3>

<p>Some insurers require proof that you paid the provider before they will process the reimbursement. Attach a credit card receipt, bank statement showing the charge, or a receipt from the provider alongside the superbill.</p>

<div class="key-takeaway">
    <strong>Claim denied?</strong> Don&rsquo;t give up. Out-of-network claim denials are often due to missing information, not ineligibility. Review the denial letter carefully &mdash; it will state the specific reason. Correct the issue and resubmit, or file a formal appeal. Our <a href="/guides/how-to-appeal-insurance-denial-and-win">guide to appealing insurance denials</a> walks you through the full process. You can also <a href="/scan">upload your bill to BillKarma</a> and we&rsquo;ll help identify what went wrong.
</div>

<h2 id="faq">Frequently asked questions</h2>

<div class="faq-section">
    <div class="faq-item">
        <h3>What is a superbill in medical billing?</h3>
        <p>A superbill is a detailed receipt from a healthcare provider that contains all the information your insurance company needs to process an out-of-network claim. It includes the provider&rsquo;s name, NPI number, tax ID, your diagnosis codes (ICD-10), procedure codes (CPT), dates of service, and the amount you paid. Unlike a regular receipt, a superbill is formatted specifically for insurance reimbursement. You submit it to your insurer, and they reimburse you based on your out-of-network benefits.</p>
    </div>

    <div class="faq-item">
        <h3>Can I get reimbursed by insurance using a superbill?</h3>
        <p>Yes, if your health insurance plan includes out-of-network benefits. Most PPO and POS plans reimburse a percentage of out-of-network charges after you meet your out-of-network deductible. HMO plans typically do not cover out-of-network care except in emergencies, so a superbill would not result in reimbursement under most HMO plans. Check your plan&rsquo;s Summary of Benefits to confirm your out-of-network coverage before submitting.</p>
    </div>

    <div class="faq-item">
        <h3>How long does it take to get reimbursed after submitting a superbill?</h3>
        <p>Most insurance companies process out-of-network claims within 30 to 45 days of receiving a complete superbill. Some insurers take up to 60 days. If your claim is denied or delayed, call the number on the back of your insurance card and ask for a status update. Keep copies of everything you submit, including the date you mailed or uploaded the superbill.</p>
    </div>

    <div class="faq-item">
        <h3>What is the difference between a superbill and an invoice?</h3>
        <p>A regular invoice or receipt shows the provider&rsquo;s name, the date, and the amount you paid. A superbill includes all of that plus the specific CPT procedure codes, ICD-10 diagnosis codes, the provider&rsquo;s NPI number, tax ID, place of service code, and other fields that insurance companies require to adjudicate a claim. Without these fields, your insurer will reject the submission.</p>
    </div>

    <div class="faq-item">
        <h3>Do all providers give superbills?</h3>
        <p>Most out-of-network providers are familiar with superbills and will provide one if you ask. Therapists, psychologists, psychiatrists, dietitians, chiropractors, acupuncturists, and other specialists who frequently see patients on a cash-pay basis typically have superbills ready to generate from their billing software. Some providers issue them automatically; others require you to request one. Always ask before or at the time of your appointment.</p>
    </div>

    <div class="faq-item">
        <h3>Can I submit a superbill for therapy or mental health visits?</h3>
        <p>Yes. Therapy is one of the most common uses for superbills. Many therapists and psychologists do not accept insurance directly but will provide a superbill so you can seek reimbursement from your insurer. Under the Mental Health Parity and Addiction Equity Act, your insurer must cover mental health services at the same level as medical services, including out-of-network benefits. If your plan covers 60% of out-of-network medical visits, it must also cover 60% of out-of-network therapy.</p>
    </div>
</div>

<h2 id="sources">Sources</h2>

<ul class="sources-list">
    <li><a href="https://www.cms.gov/medicare/coding-billing/place-of-service-codes" target="_blank" rel="noopener">CMS &mdash; Place of Service Codes for Professional Claims</a></li>
    <li><a href="https://npiregistry.cms.hhs.gov/" target="_blank" rel="noopener">CMS &mdash; NPPES NPI Registry (Provider NPI Lookup)</a></li>
    <li><a href="https://www.cms.gov/medicare/physician-fee-schedule/search" target="_blank" rel="noopener">CMS &mdash; Medicare Physician Fee Schedule (UCR Rate Reference)</a></li>
    <li><a href="https://www.cms.gov/cciici" target="_blank" rel="noopener">CMS &mdash; ICD-10 Code Sets and Guidelines</a></li>
    <li><a href="https://www.samhsa.gov/about-us/who-we-are/laws-regulations/mental-health-parity" target="_blank" rel="noopener">SAMHSA &mdash; Mental Health Parity and Addiction Equity Act (MHPAEA)</a></li>
    <li><a href="https://www.kff.org/health-costs/issue-brief/understanding-health-insurance-out-of-network-charges/" target="_blank" rel="noopener">Kaiser Family Foundation &mdash; Understanding Out-of-Network Charges and Balance Billing</a></li>
    <li><a href="https://www.ama-assn.org/practice-management/cpt/cpt-overview-and-code-approval" target="_blank" rel="noopener">American Medical Association &mdash; CPT Code Overview and Usage</a></li>
</ul>
""",
})
