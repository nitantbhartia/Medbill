"""Guide: Telehealth & Virtual Care Insurance Coverage in 2026."""

from guides import register, _embed

register("telehealth-billing-insurance", {
    "title": "Telehealth & Virtual Care Insurance Coverage in 2026",
    "meta_description": "Most insurance plans cover telehealth visits in 2026, but coverage rules, copays, and coding requirements vary. Learn what's covered, which CPT modifiers apply, and how to avoid the billing errors that affect 23% of telehealth claims.",
    "published": "2026-04-05",
    "author": "BillKarma Team",
    "category": "Insurance & Coverage",
    "faqs": [
        {
            "q": "Does insurance cover telehealth visits in 2026?",
            "a": "Yes, most commercial insurance plans, Medicare, and all 50 state Medicaid programs cover some form of telehealth. Coverage details&mdash;copays, which services qualify, whether audio-only is allowed&mdash;vary by plan. Check your plan's Summary of Benefits or call member services before your visit to confirm coverage and avoid surprise bills.",
        },
        {
            "q": "Is telehealth the same cost as an in-person visit?",
            "a": "It depends on your plan. Many commercial plans charge the same copay for telehealth as in-person visits. Some plans charge lower copays for telehealth, particularly through insurer-preferred platforms like Teladoc or MDLive. A few plans have separate telehealth cost-sharing structures. Check your plan documents or call before scheduling.",
        },
        {
            "q": "What is modifier 95 in telehealth billing?",
            "a": "Modifier 95 indicates a synchronous (real-time) telemedicine service delivered via interactive audio and video. Providers append modifier 95 to standard E&M codes (99202&ndash;99215) when the visit is conducted via telehealth. Without this modifier, a telehealth claim may be rejected or paid at the wrong rate.",
        },
        {
            "q": "Does Medicare cover telehealth permanently after COVID?",
            "a": "Yes. Post-COVID legislation made many expanded telehealth provisions permanent. Medicare Part B now covers telehealth for mental health, primary care, specialist visits, and more. Some provisions (like allowing coverage when the patient is at home rather than a clinical site) were extended permanently by the Consolidated Appropriations Act.",
        },
        {
            "q": "Can I get a prescription via telehealth?",
            "a": "Yes for most medications. DEA rules were relaxed during COVID to allow prescribing controlled substances via telehealth without an in-person visit first. Some of those rules have been extended but the regulatory landscape is evolving. Non-controlled medications can be prescribed via telehealth without restriction in all states.",
        },
    ],
    "body": f"""
<p class="lead">Telehealth became a mainstream healthcare delivery channel during COVID&mdash;and it has stayed that way. In 2026, most commercial insurance plans, Medicare, and all 50 Medicaid programs cover telehealth visits. But coverage rules, copay structures, and billing requirements are inconsistent enough that <strong>23% of telehealth bills contain coding errors</strong>, mostly from incorrect place-of-service codes. Here is what your plan covers, what to watch out for, and how to avoid overpaying.</p>

<nav class="toc">
    <h2>In this guide</h2>
    <ol>
        <li><a href="#coverage-landscape">Telehealth coverage landscape in 2026</a></li>
        <li><a href="#medicare-medicaid">Medicare and Medicaid telehealth rules</a></li>
        <li><a href="#commercial-plans">Commercial insurance: costs and platforms</a></li>
        <li><a href="#billing-codes">CPT codes and modifiers for telehealth</a></li>
        <li><a href="#mental-health">Mental health telehealth and parity laws</a></li>
        <li><a href="#prescribing">Prescribing via telehealth: what&rsquo;s allowed</a></li>
        <li><a href="#billing-errors">Common billing errors and how to spot them</a></li>
        <li><a href="#verify">How to verify coverage before your visit</a></li>
        <li><a href="#faq">Frequently asked questions</a></li>
        <li><a href="#sources">Sources</a></li>
    </ol>
</nav>

<h2 id="coverage-landscape">1. Telehealth coverage landscape in 2026</h2>

<p>The coverage picture in 2026 is dramatically better than pre-2020. COVID-era emergency authorizations have largely been made permanent or extended, and most major insurers have integrated telehealth as a standard benefit. Here is where things stand:</p>

<table>
    <thead>
        <tr><th>Payer Type</th><th>Coverage Status</th><th>Audio-Only Allowed?</th><th>Cost-Sharing</th></tr>
    </thead>
    <tbody>
        <tr><td><strong>Large commercial plans</strong> (Aetna, Cigna, UnitedHealth, Anthem)</td><td>Covered; most services same as in-person</td><td>Yes, but lower reimbursement</td><td>Same or lower than in-person copay</td></tr>
        <tr><td><strong>Small employer / self-funded plans</strong></td><td>Varies; check your Summary of Benefits</td><td>Plan-dependent</td><td>Varies; may differ from in-person</td></tr>
        <tr><td><strong>Medicare Part B</strong></td><td>Permanent coverage for most services</td><td>Yes (with limitations)</td><td>20% after Part B deductible</td></tr>
        <tr><td><strong>Medicaid</strong></td><td>All 50 states cover some telehealth</td><td>Most states; policies vary</td><td>Low or $0 depending on state</td></tr>
        <tr><td><strong>ACA marketplace plans</strong></td><td>Covered as essential benefit</td><td>Most plans</td><td>Deductible + coinsurance or copay</td></tr>
    </tbody>
</table>

<p><strong>What is and is not covered:</strong> Most plans cover telehealth for primary care visits, specialist consultations, mental health, dermatology (with photos), and urgent care-level issues. Some plans still require in-person visits for physical exams where hands-on assessment is clinically necessary, annual wellness physicals, and certain procedures.</p>

<div class="key-takeaway">
    <strong>Audio-only vs. video:</strong> All major payers cover synchronous video telehealth. Audio-only (phone call) telehealth is covered by most plans but typically reimbursed at a lower rate. Some Medicare Advantage and commercial plans require video for certain service types. If you can use video, use video&mdash;it reduces the chance of a coding mismatch and claim denial.
</div>

<h2 id="medicare-medicaid">2. Medicare and Medicaid telehealth rules</h2>

<p><strong>Medicare:</strong> The Consolidated Appropriations Act and subsequent legislation made several COVID-era telehealth expansions permanent for Medicare. Key provisions now permanently in effect:</p>

<ul>
    <li>Patient can be at home (not just a clinical site) for mental health and most telehealth services</li>
    <li>Primary care and chronic care management visits via telehealth are covered</li>
    <li>Federally Qualified Health Centers (FQHCs) and Rural Health Clinics (RHCs) can serve as originating sites</li>
    <li>Mental health services: patients must have an in-person visit with the provider within 6 months of starting telehealth mental health treatment and annually thereafter (this requirement applies to new patients as of January 2025)</li>
    <li>Place of Service code 02 (telehealth, patient not at home) or 10 (telehealth, patient at home) must be used correctly</li>
</ul>

<p><strong>Medicaid:</strong> All 50 states cover some form of telehealth, but policies differ significantly. Most states cover both video and audio-only. A smaller number require video for all telehealth. A few states have fee-for-service Medicaid telehealth rates below in-person rates; most have moved to parity. If you are on Medicaid, call your state Medicaid program or managed care plan before a telehealth visit to confirm what is covered.</p>

<h2 id="commercial-plans">3. Commercial insurance: costs and platforms</h2>

<p>Commercial plans in 2026 generally take one of two approaches to telehealth:</p>

<p><strong>Approach 1: Preferred platform model.</strong> Your insurer contracts with telehealth platforms (Teladoc, MDLive, Amwell, Doctor on Demand) at discounted or zero-copay rates. Using these platforms costs you <strong>$0&ndash;$75 per visit</strong> depending on your plan. Using your regular doctor&rsquo;s telehealth portal may cost more (your standard specialist or primary care copay).</p>

<p><strong>Approach 2: Parity model.</strong> Your insurer treats telehealth visits identically to in-person visits. Your regular doctor bills telehealth using the same E&M codes with a telehealth modifier, and you pay your standard copay or coinsurance.</p>

<table>
    <thead>
        <tr><th>Platform</th><th>Common Insurer Partnerships</th><th>Typical Copay (insured)</th><th>Without Insurance</th></tr>
    </thead>
    <tbody>
        <tr><td>Teladoc</td><td>Aetna, many employer plans</td><td>$0&ndash;$45</td><td>$75&ndash;$95 per visit</td></tr>
        <tr><td>MDLive</td><td>Cigna, Blue Cross plans</td><td>$0&ndash;$50</td><td>$82&ndash;$108 per visit</td></tr>
        <tr><td>Amwell</td><td>Anthem, UnitedHealth</td><td>$0&ndash;$75</td><td>$79&ndash;$109 per visit</td></tr>
        <tr><td>Doctor on Demand</td><td>Various employer plans</td><td>$0&ndash;$50</td><td>$75&ndash;$100 per visit</td></tr>
        <tr><td>Your regular doctor&rsquo;s telehealth</td><td>In-network if provider is in-network</td><td>Standard office copay</td><td>Full billed rate</td></tr>
    </tbody>
</table>

<p><strong>Platform fee vs. provider fee:</strong> Some telehealth platforms charge a separate technology or platform fee on top of the provider fee. This platform fee may not be covered by insurance. Always ask before the visit whether you will receive one bill or two, and whether the platform fee is covered by your plan.</p>

{_embed(mode="cost", cpt="99213", title="Look up telehealth visit costs", subtitle="See what Medicare pays for office and telehealth E&M visits.")}

<h2 id="billing-codes">4. CPT codes and modifiers for telehealth</h2>

<p>Telehealth visits use the same Evaluation and Management (E&M) CPT codes as in-person visits. The difference is in the modifier and place-of-service code:</p>

<table>
    <thead>
        <tr><th>Code / Modifier</th><th>Description</th><th>When Used</th></tr>
    </thead>
    <tbody>
        <tr><td><strong>99202&ndash;99215</strong></td><td>Office or outpatient E&M visits (new and established patients)</td><td>Base code for all telehealth visits</td></tr>
        <tr><td><strong>Modifier 95</strong></td><td>Synchronous telemedicine service rendered via real-time interactive audio and video</td><td>Appended to E&M code for video telehealth</td></tr>
        <tr><td><strong>Modifier GT</strong></td><td>Via interactive audio and video telecommunications systems</td><td>Used by some Medicare claims</td></tr>
        <tr><td><strong>POS 02</strong></td><td>Place of service: telehealth (patient not at home)</td><td>When patient is at a clinical or remote site</td></tr>
        <tr><td><strong>POS 10</strong></td><td>Place of service: telehealth (patient at home)</td><td>When patient is at their home&mdash;most common for consumer telehealth</td></tr>
        <tr><td><strong>99441&ndash;99443</strong></td><td>Telephone E&M services (audio-only)</td><td>Phone-only visits; lower reimbursement</td></tr>
    </tbody>
</table>

<p>The POS code is the single most common source of telehealth billing errors. POS 02 (telehealth not at home) and POS 10 (telehealth at home) are different and affect reimbursement rates. Many providers default to POS 02 for all telehealth, which is incorrect when the patient is calling from home&mdash;the most common scenario for consumer telehealth.</p>

<h2 id="mental-health">5. Mental health telehealth and parity laws</h2>

<p>Mental health telehealth is among the best-covered areas in 2026. Federal parity law (the Mental Health Parity and Addiction Equity Act) requires that insurance plans cover mental health and substance use disorder services on the same terms as medical/surgical benefits. This applies to telehealth as well as in-person care.</p>

<p><strong>What this means in practice:</strong></p>
<ul>
    <li>Your copay for a telehealth therapy session cannot be higher than your copay for an equivalent in-person medical visit</li>
    <li>If your plan covers in-person psychiatry, it must cover telehealth psychiatry</li>
    <li>Prior authorization requirements for mental health telehealth cannot be more stringent than for medical telehealth</li>
</ul>

<p><strong>Medicare mental health telehealth:</strong> Medicare now permanently covers individual and group therapy, psychiatric evaluation, and medication management via telehealth. New patients must have an in-person visit within 6 months of starting telehealth mental health treatment and annually thereafter. This rule does not apply if you are an established patient.</p>

<p><strong>Substance use disorder:</strong> Telehealth coverage for opioid use disorder treatment (including buprenorphine prescribing) was expanded during COVID and most provisions have been maintained through extensions. Check current DEA rules, which are subject to change.</p>

<h2 id="prescribing">6. Prescribing via telehealth: what&rsquo;s allowed</h2>

<p>Telehealth prescribing rules are straightforward for most medications but more complex for controlled substances:</p>

<p><strong>Non-controlled medications:</strong> Can be prescribed via telehealth without restriction in all states. This includes antibiotics, blood pressure medications, antidepressants, diabetes medications, and most other commonly prescribed drugs.</p>

<p><strong>Controlled substances (DEA Schedules II&ndash;V):</strong> The DEA relaxed the Ryan Haight Act in-person requirement during COVID, allowing prescribing of controlled substances via telehealth without a prior in-person visit. These exceptions have been extended through regulatory action, but the landscape is subject to change. As of 2026, DEA-registered providers can prescribe buprenorphine (opioid use disorder treatment) via telehealth. Stimulants and benzodiazepines via telehealth have been subject to renewed scrutiny following enforcement actions against telehealth companies. Check with your provider about current rules for specific controlled substances.</p>

<p><strong>State-by-state variation:</strong> Some states impose additional prescribing restrictions beyond federal rules. Providers licensed in states with stricter rules may not be able to prescribe certain medications via telehealth even if federal law allows it.</p>

<h2 id="billing-errors">7. Common billing errors and how to spot them</h2>

<p>BillKarma data shows that <strong>23% of telehealth bills contain coding errors</strong>, most of which result in patients being overcharged or claims being incorrectly denied. The most common errors:</p>

<ul>
    <li><strong>Wrong place-of-service code.</strong> Using POS 02 (telehealth, not at home) when the patient was at home (POS 10 is correct) or using POS 11 (office) for a telehealth visit. POS 11 on a telehealth claim triggers repricing at in-person rates, which may be higher or may cause a denial.</li>
    <li><strong>Missing modifier 95.</strong> Without modifier 95 (or GT for Medicare), a telehealth claim looks like an in-person visit. If the patient was never physically in the office, the claim is incorrect and creates a documentation mismatch.</li>
    <li><strong>Platform billing separately from provider service.</strong> Some telehealth platforms bill a facility or platform fee separately from the provider&rsquo;s professional fee. If the platform fee is not covered by your plan, you will receive a surprise bill. Always verify before the visit.</li>
    <li><strong>Out-of-network telehealth provider.</strong> Telehealth platforms sometimes route you to a provider who is not in your insurance network, even if the platform itself is an insurer-preferred vendor. Confirm the individual provider is in-network before the visit.</li>
    <li><strong>Audio-only coded as video visit.</strong> Billing a phone-only call under video telehealth codes (with modifier 95) instead of telephone codes (99441&ndash;99443) is a coding error that can lead to claim denial or audit.</li>
</ul>

<div class="case-study">
    <h3>Case study: $0 telehealth visit billed as $280</h3>
    <p><strong>Situation:</strong> James used his insurer&rsquo;s preferred telehealth platform (Amwell) for a sick visit, expecting his plan&rsquo;s $0 telehealth copay. He received a bill for $280.</p>
    <p><strong>The problem:</strong> The provider used POS 11 (office) instead of POS 10 (telehealth, patient at home) and omitted modifier 95. The claim was processed as an in-person specialist visit, triggering his $280 specialist coinsurance rather than the $0 telehealth copay.</p>
    <p><strong>What he did:</strong> James <a href="/fight-debt">filed a dispute through BillKarma</a>. We identified the POS and modifier error and contacted the provider&rsquo;s billing department to resubmit with POS 10 and modifier 95. The claim was reprocessed in 12 days.</p>
    <p><strong>Result:</strong> James&rsquo;s bill was reduced to $0, matching his plan&rsquo;s telehealth benefit. <strong>A simple coding correction saved him $280.</strong></p>
</div>

<p>If you have received a telehealth bill that seems incorrect, <a href="/fight-debt">let BillKarma review it</a>. We identify place-of-service errors, missing modifiers, and parity violations automatically.</p>

<h2 id="verify">8. How to verify coverage before your visit</h2>

<ol>
    <li><strong>Check your plan&rsquo;s Summary of Benefits.</strong> Look for a &ldquo;telehealth&rdquo; or &ldquo;virtual care&rdquo; section. Note the copay or coinsurance and whether a deductible applies.</li>
    <li><strong>Call member services.</strong> Ask specifically: Is this provider/platform in-network? What is my cost-sharing for a telehealth visit? Is video required or is audio-only covered?</li>
    <li><strong>Confirm the provider is in-network.</strong> Even on insurer-preferred platforms, verify the specific provider seeing you is in-network.</li>
    <li><strong>Ask about separate fees upfront.</strong> Ask the platform or provider&rsquo;s billing team whether there is a platform fee separate from the professional fee, and whether it is covered by your plan.</li>
    <li><strong>After the visit, review the EOB.</strong> Your Explanation of Benefits will show how the claim was coded. If POS 11 appears instead of POS 02 or 10, contact the provider to correct the submission. <a href="/scan">Upload your bill to BillKarma</a> if you want a second set of eyes on the claim.</li>
</ol>

<h2 id="faq">Frequently asked questions</h2>

<div class="faq-section">
    <div class="faq-item">
        <h3>Does insurance cover telehealth visits in 2026?</h3>
        <p>Yes. Most commercial plans, Medicare, and all 50 state Medicaid programs cover telehealth. Coverage details vary by plan&mdash;check your Summary of Benefits or call member services before your visit.</p>
    </div>

    <div class="faq-item">
        <h3>Is telehealth the same cost as an in-person visit?</h3>
        <p>Often yes, though some plans charge lower copays for telehealth, particularly through insurer-preferred platforms. A few plans have separate telehealth cost-sharing. Check your plan documents.</p>
    </div>

    <div class="faq-item">
        <h3>What is modifier 95 in telehealth billing?</h3>
        <p>Modifier 95 signals that the service was delivered synchronously via interactive audio and video. Providers add it to standard E&M codes when billing telehealth. Missing modifier 95 is the second most common telehealth billing error.</p>
    </div>

    <div class="faq-item">
        <h3>Does Medicare cover telehealth permanently after COVID?</h3>
        <p>Yes. Post-COVID legislation made most expanded telehealth provisions permanent for Medicare, including allowing patients to receive services from home and covering mental health, primary care, and specialist visits via telehealth.</p>
    </div>

    <div class="faq-item">
        <h3>Can I get a prescription via telehealth?</h3>
        <p>Yes, for most medications. Non-controlled medications can be prescribed without restriction. Controlled substances can generally be prescribed via telehealth under extended DEA rules, though the regulatory environment continues to evolve for some drug categories.</p>
    </div>
</div>

<h2 id="sources">Sources</h2>

<ul class="sources-list">
    <li><a href="#" target="_blank" rel="noopener">Centers for Medicare &amp; Medicaid Services: Telehealth</a></li>
    <li><a href="#" target="_blank" rel="noopener">American Medical Association: Telehealth CPT Coding Guide (2026)</a></li>
    <li><a href="#" target="_blank" rel="noopener">U.S. DEA: Telemedicine and Controlled Substances</a></li>
    <li><a href="#" target="_blank" rel="noopener">Kaiser Family Foundation: Telehealth Policy After COVID-19</a></li>
    <li><a href="#" target="_blank" rel="noopener">National Conference of State Legislatures: State Telehealth Laws</a></li>
</ul>
""",
})
