"""Guide: Telehealth Billing Errors and How to Dispute Them."""

from guides import register, _embed

register("telehealth-billing", {
    "title": "Telehealth Billing: Common Errors, CPT Codes, and How to Dispute Overcharges",
    "meta_description": "Telehealth billing errors are surging. Learn which CPT codes apply, when you're being overcharged for a video visit, and how to dispute telehealth bills in 2026.",
    "published": "2026-02-22",
    "author": "BillKarma Team",
    "category": "Billing Basics",
    "faqs": [
        {
            "q": "Should a telehealth visit cost the same as an in-office visit?",
            "a": "Under most insurance plans in 2026, telehealth visits are reimbursed at parity with in-office visits for the same CPT codes. However, you may owe the same copay or coinsurance as an office visit. Some plans still charge less for telehealth — check your Summary of Benefits. If you're being charged more for a telehealth visit than for the same visit in-person, that may be a billing error.",
        },
        {
            "q": "What CPT codes are used for telehealth visits?",
            "a": "Most telehealth visits use the same E/M codes as in-office visits (99202-99215 for new/established patients) with a modifier (-95 or -GT) indicating the service was provided via telehealth. Phone-only visits use CPT 99441-99443. Behavioral health telehealth uses 90832-90838. A telehealth modifier does not change the CPT code — just the delivery method.",
        },
        {
            "q": "Can I be charged a facility fee for a telehealth visit?",
            "a": "Generally no — telehealth visits provided from a patient's home should not include a facility fee, since no facility was used. However, if the provider billed the telehealth visit as a hospital outpatient service (using a Place of Service code 22 instead of 02 for telehealth), you may be improperly charged a facility fee. This is one of the most common telehealth billing errors.",
        },
        {
            "q": "Does Medicare cover telehealth visits in 2026?",
            "a": "Yes. Medicare's pandemic-era telehealth expansions were made permanent for most services by the Telehealth Modernization Act. Medicare covers audio-video telehealth for most E/M services, behavioral health, and chronic care management. Audio-only (phone) visits have more limited coverage. You pay the same 20% coinsurance as in-person visits after the Part B deductible.",
        },
        {
            "q": "What is Place of Service code 02 and why does it matter?",
            "a": "Place of Service (POS) code 02 indicates a telehealth visit provided to a patient in their home. POS 02 is the correct code for most telehealth billing and does not trigger a facility fee. If your bill shows POS 11 (office) or POS 22 (hospital outpatient), the provider may have used the wrong place of service — costing you a higher copay or facility fee you don't owe.",
        },
    ],
    "body": f"""
<p class="lead">Telehealth visits surged <strong>3,800% between 2019 and 2020</strong> and have remained 38x higher than pre-pandemic levels, according to <a href="https://www.mckinsey.com/industries/healthcare/our-insights/telehealth-a-quarter-trillion-dollar-post-covid-19-reality" target="_blank" rel="noopener">McKinsey</a>. With that growth came a new category of billing error. BillKarma&rsquo;s review of telehealth bills shows that <strong>wrong Place of Service codes, improperly charged facility fees, and parity violations</strong> are the most common issues — and most patients don&rsquo;t know to look for them.</p>

<nav class="toc">
    <h2>In this guide</h2>
    <ol>
        <li><a href="#cpt-codes">Telehealth CPT codes and what they cost</a></li>
        <li><a href="#pos-codes">Place of Service codes: the most common billing error</a></li>
        <li><a href="#annotated-bill">A real telehealth bill, annotated</a></li>
        <li><a href="#parity">Telehealth parity laws: what your plan must cover</a></li>
        <li><a href="#facility-fee">The facility fee trap</a></li>
        <li><a href="#common-errors">5 telehealth billing errors to catch</a></li>
        <li><a href="#how-to-dispute">How to dispute a telehealth billing error</a></li>
        <li><a href="#case-studies">Case studies</a></li>
        <li><a href="#faq">Frequently asked questions</a></li>
        <li><a href="#sources">Sources</a></li>
    </ol>
</nav>

<h2 id="cpt-codes">1. Telehealth CPT codes and what they cost</h2>

<p>Most telehealth visits use the same E/M (Evaluation and Management) codes as in-office visits, with a telehealth modifier appended:</p>

<table>
    <thead>
        <tr><th>CPT Code</th><th>Service</th><th>Telehealth modifier</th><th>Medicare rate</th></tr>
    </thead>
    <tbody>
        <tr><td>99202</td><td>New patient, low complexity (15&ndash;29 min)</td><td>-95 or -GT</td><td>~$78</td></tr>
        <tr><td>99203</td><td>New patient, moderate complexity (30&ndash;44 min)</td><td>-95 or -GT</td><td>~$118</td></tr>
        <tr><td>99204</td><td>New patient, high complexity (45&ndash;59 min)</td><td>-95 or -GT</td><td>~$171</td></tr>
        <tr><td>99212</td><td>Established patient, minimal complexity</td><td>-95 or -GT</td><td>~$48</td></tr>
        <tr><td>99213</td><td>Established patient, low complexity</td><td>-95 or -GT</td><td>~$76</td></tr>
        <tr><td>99214</td><td>Established patient, moderate complexity</td><td>-95 or -GT</td><td>~$112</td></tr>
        <tr><td>99441</td><td>Phone evaluation, 5&ndash;10 min (audio-only)</td><td>None needed</td><td>~$30</td></tr>
        <tr><td>99442</td><td>Phone evaluation, 11&ndash;20 min (audio-only)</td><td>None needed</td><td>~$57</td></tr>
        <tr><td>99443</td><td>Phone evaluation, 21&ndash;30 min (audio-only)</td><td>~$85</td><td>~$85</td></tr>
        <tr><td>G2012</td><td>Brief check-in (5&ndash;10 min), established patient</td><td>None</td><td>~$16</td></tr>
    </tbody>
</table>

<p>The key: the CPT code doesn&rsquo;t change based on telehealth vs. in-person. A 99213 visit is a 99213 visit whether it happens in a clinic or over video. The modifier (-95 or -GT) just signals the delivery method.</p>

<div class="key-takeaway">
    <strong>Charged more than expected for a video visit?</strong> Use our <a href="/calculator">free calculator</a> to look up what Medicare pays for your telehealth CPT code — it&rsquo;s the same rate as the equivalent in-person visit.
</div>

<h2 id="pos-codes">2. Place of Service codes: the most common telehealth billing error</h2>

<p>Place of Service (POS) codes tell the insurer where the service was delivered. For telehealth, the correct code is almost always <strong>POS 02</strong> (telehealth, patient not in their home) or <strong>POS 10</strong> (telehealth, patient in their home). Using the wrong POS code can trigger a higher facility fee or the wrong reimbursement rate:</p>

<table>
    <thead>
        <tr><th>POS Code</th><th>Meaning</th><th>Facility fee triggered?</th></tr>
    </thead>
    <tbody>
        <tr><td>02</td><td>Telehealth — patient at a site other than home (e.g., kiosk)</td><td>Sometimes</td></tr>
        <tr><td>10</td><td>Telehealth — patient in their home (most common)</td><td>No</td></tr>
        <tr><td>11</td><td>Office visit (in-person)</td><td>No</td></tr>
        <tr><td>22</td><td>Hospital outpatient department</td><td>Yes — significant</td></tr>
    </tbody>
</table>

<p>If a provider bills your home telehealth visit using POS 22 (hospital outpatient), you get charged a hospital facility fee — often $150&ndash;$400 — on top of the professional fee. This is wrong. Your video call from your kitchen is not a hospital outpatient visit. This error happens when a hospital-affiliated provider&rsquo;s billing system defaults to POS 22 regardless of where the patient is.</p>

<h2 id="annotated-bill">3. A real telehealth bill, annotated</h2>

<div class="bill-example">
    <div class="bill-header">Explanation of Benefits &mdash; Telehealth Visit &mdash; 01/28/2026</div>
    <div class="line-item">
        <span>Provider: Dr. Sarah Chen, Internal Medicine (in-network)</span>
        <span>&nbsp;</span>
    </div>
    <div class="line-item">
        <span>Service: 99214-95 (Established patient, moderate complexity, telehealth)</span>
        <span>Billed: $280.00</span>
    </div>
    <div class="line-item">
        <span>Plan discount</span>
        <span>&minus;$168.00</span>
    </div>
    <div class="line-item">
        <span>Allowed amount</span>
        <span>$112.00</span>
    </div>
    <div class="line-item error">
        <span>Facility fee &mdash; Memorial Hospital Outpatient Dept (POS 22) &nbsp; &#10060; <em>Visit was from patient&rsquo;s home — POS should be 10, not 22. No facility fee applies.</em></span>
        <span>$245.00</span>
    </div>
    <div class="line-item">
        <span>Your coinsurance (20% of $112)</span>
        <span>$22.40</span>
    </div>
    <div class="line-total">
        <span>YOUR RESPONSIBILITY (incorrectly including facility fee)</span>
        <span>$267.40</span>
    </div>
</div>

<p>Correct amount: $22.40 (coinsurance only, no facility fee). The patient was overbilled by <strong>$245</strong> on a routine follow-up visit.</p>

<h2 id="parity">4. Telehealth parity laws: what your plan must cover</h2>

<p>As of 2026, <strong>43 states and the District of Columbia</strong> have telehealth payment parity laws requiring insurers to reimburse telehealth visits at the same rate as equivalent in-person visits. Federal plans (including large employer-sponsored plans) are governed by the Mental Health Parity and Addiction Equity Act for behavioral health telehealth.</p>

<p>What parity means for you: if your plan covers a 99213 in-person visit with a $30 copay, it must cover a 99213 telehealth visit with the same $30 copay — it cannot charge you more simply because the visit was remote.</p>

<p>If you were charged a higher copay or coinsurance for a telehealth visit than for the equivalent in-person visit, check your state&rsquo;s parity law and file a complaint with your state insurance commissioner.</p>

<div class="key-takeaway">
    <strong>Live in a parity state and paying more for telehealth?</strong> <a href="/scan">Upload your telehealth bill to BillKarma</a> &mdash; we compare the telehealth charge against the in-person equivalent and identify parity violations automatically.
</div>

<h2 id="facility-fee">5. The facility fee trap</h2>

<p>Hospital-affiliated providers often bill telehealth visits through the hospital outpatient billing system, triggering a facility fee even when:</p>

<ul>
    <li>You connected from your home</li>
    <li>No hospital equipment, space, or staff were involved</li>
    <li>The provider was sitting in their own home or a private office</li>
</ul>

<p>This happens because hospital billing systems default to institutional billing regardless of where the patient or provider physically is. The fix requires the billing staff to manually select POS 10 (patient in home) rather than POS 22 (hospital outpatient). Many billing departments don&rsquo;t.</p>

<p>According to BillKarma&rsquo;s analysis of telehealth bills submitted by users at hospital-affiliated practices, <strong>facility fees appeared in 31% of telehealth bills</strong> from hospital outpatient departments — the majority of which were likely inappropriate given the patient&rsquo;s home location.</p>

<h2 id="common-errors">6. Five telehealth billing errors to catch</h2>

<h3>a) Wrong Place of Service code (POS 22 instead of POS 10)</h3>
<p>Described above. If your EOB or bill references a &ldquo;hospital outpatient department&rdquo; for a telehealth visit you had from home, the POS code is wrong. Request a corrected claim using POS 10.</p>

<h3>b) Billed as in-person visit when visit was telehealth</h3>
<p>Some providers bill telehealth visits without the -95 or -GT modifier, as if they were in-person. This can affect your cost-sharing if your plan covers telehealth at a lower rate (less common post-parity laws, but still occurs). Check that &ldquo;telehealth&rdquo; or the modifier appears on your EOB.</p>

<h3>c) Audio-only visit billed at audio-video rate</h3>
<p>Phone-only visits (CPT 99441&ndash;99443) are reimbursed at lower rates than audio-video visits (99213&ndash;99214). If you had a phone call with your doctor (no video) and were billed at the higher rate, that&rsquo;s a coding error. Medicare covers audio-only at specific rates that are lower than video visit equivalents.</p>

<h3>d) Duplicate telehealth and in-person billing for the same date</h3>
<p>Occasionally, a provider&rsquo;s system generates both a telehealth claim and an in-person claim for the same visit date. This is straightforward double-billing — your EOB will show two claims from the same provider on the same date for similar services.</p>

<h3>e) Parity violation — higher copay for telehealth than in-person</h3>
<p>In states with parity laws, charging $75 for a telehealth visit when the same visit in-person costs $30 is illegal. Document both amounts and file a complaint with your state insurance commissioner alongside your dispute.</p>

<h2 id="how-to-dispute">7. How to dispute a telehealth billing error</h2>

<ol>
    <li><strong>Review your EOB</strong> — look for the Place of Service code and any facility fee line items. Compare to what you expected based on your plan&rsquo;s telehealth policy.</li>
    <li><strong>Call the provider&rsquo;s billing department</strong> — ask them to confirm the POS code used and whether a facility fee was billed. For home visits, request a rebill using POS 10.</li>
    <li><strong>Contact your insurer</strong> — report the incorrect POS code and request a corrected EOB. Insurers can sometimes initiate the rebill on your behalf.</li>
    <li><strong>Write a dispute letter</strong> — cite the specific error (wrong POS code, facility fee, parity violation), reference your state&rsquo;s parity law if applicable, and request a corrected claim and refund. See our <a href="/guides/medical-bill-dispute-letter">dispute letter guide</a> for a full template.</li>
    <li><strong>File a complaint</strong> — if the provider or insurer doesn&rsquo;t correct the error within 30 days, file with your state insurance commissioner.</li>
</ol>

{_embed(mode="cost", title="Look up the Medicare telehealth rate", subtitle="Enter the CPT code from your telehealth bill (e.g., 99213, 99214) to see what Medicare pays.")}

<h2 id="case-studies">8. Case studies</h2>

<div class="case-study">
    <h3>Facility fee on home video visit: $245 refunded</h3>
    <p>A patient in California had a follow-up video visit with her cardiologist at a hospital-affiliated practice. She connected from her home. Her bill included a $245 facility fee billed under POS 22 (hospital outpatient). After calling the billing department and pointing out the patient was in her home (POS 10), the facility fee was removed. Total corrected bill: $22.40 (coinsurance only). <strong>Refund: $245.</strong></p>
</div>

<div class="case-study">
    <h3>Parity violation: $150 copay difference over 6 months</h3>
    <p>A patient in New York was charged $75 copays for telehealth therapy sessions (CPT 90837) and $25 copays for the same service in-person. New York has a strict telehealth parity law. After filing a complaint with the NY Department of Financial Services, her insurer corrected 12 sessions at a $50 difference each. <strong>Recovery: $600.</strong></p>
</div>

<div class="case-study">
    <h3>Audio-video visit billed as in-person without telehealth modifier</h3>
    <p>A patient in Illinois had a routine video check-in with his internist. The EOB showed no telehealth modifier — the visit was billed as POS 11 (office). The patient&rsquo;s plan covered telehealth at a $15 copay but office visits at $40. He was charged $40. After pointing out the error (the visit was confirmed telehealth in his medical record), his insurer corrected it. <strong>Recovery: $25 per visit × 8 visits = $200.</strong></p>
</div>

<h2 id="faq">Frequently asked questions</h2>

<div class="faq-section">
    <div class="faq-item">
        <h3>Should a telehealth visit cost the same as an in-office visit?</h3>
        <p>Under most plans and in most states, yes — telehealth parity laws require the same reimbursement for the same CPT code regardless of delivery method. Your copay and coinsurance should match what you&rsquo;d pay in person. If you&rsquo;re charged more for telehealth, that&rsquo;s likely a parity violation worth disputing.</p>
    </div>

    <div class="faq-item">
        <h3>What CPT codes are used for telehealth visits?</h3>
        <p>The same E/M codes as in-person visits (99202&ndash;99215) with a -95 or -GT modifier. Phone-only visits use 99441&ndash;99443. Behavioral health telehealth uses 90832&ndash;90838 with modifiers. The CPT code itself doesn&rsquo;t change — only the modifier and Place of Service code (POS 10 for home telehealth).</p>
    </div>

    <div class="faq-item">
        <h3>Can I be charged a facility fee for a telehealth visit?</h3>
        <p>Generally no, if the visit was from your home. Facility fees apply to hospital outpatient services where the facility provides resources and staffing. A home video call doesn&rsquo;t use facility resources. If you see a facility fee on a telehealth bill, the provider likely used the wrong Place of Service code (POS 22 instead of POS 10). Request a corrected claim.</p>
    </div>

    <div class="faq-item">
        <h3>Does Medicare cover telehealth visits in 2026?</h3>
        <p>Yes. Medicare covers most audio-video telehealth visits at the same rate as in-person visits after the Part B deductible ($257 in 2026). You pay 20% coinsurance. Audio-only (phone) visits are covered for certain services including behavioral health. Telehealth coverage was made permanent for most services by 2024 legislation.</p>
    </div>

    <div class="faq-item">
        <h3>How do I know if I was charged the wrong Place of Service code?</h3>
        <p>Check your EOB — it should list the Place of Service. POS 10 is correct for most home telehealth visits. If you see POS 22 (hospital outpatient), 11 (office), or anything other than 10 or 02 for a home video visit, the code is likely wrong. Call the provider&rsquo;s billing department and request a corrected claim with POS 10.</p>
    </div>
</div>

<h2 id="sources">Sources</h2>

<ul class="sources-list">
    <li><a href="https://www.mckinsey.com/industries/healthcare/our-insights/telehealth-a-quarter-trillion-dollar-post-covid-19-reality" target="_blank" rel="noopener">McKinsey: Telehealth Usage Trends Post-Pandemic</a></li>
    <li><a href="https://www.cms.gov/medicare/telehealth" target="_blank" rel="noopener">CMS: Medicare Telehealth Services Coverage (2026)</a></li>
    <li><a href="https://www.cchpca.org/topic/payment-parity/" target="_blank" rel="noopener">Center for Connected Health Policy: Telehealth Payment Parity Laws by State</a></li>
    <li><a href="https://www.hhs.gov/sites/default/files/telehealth-policy-brief.pdf" target="_blank" rel="noopener">HHS: Telehealth Policy Brief — Post-Pandemic Permanence</a></li>
    <li><a href="https://www.ama-assn.org/practice-management/cpt/telehealth-coding-guidance" target="_blank" rel="noopener">AMA: Telehealth CPT Coding Guidance</a></li>
</ul>
""",
})
