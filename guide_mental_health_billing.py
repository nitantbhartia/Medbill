"""Guide: Mental Health Billing and Parity Rights."""

from guides import register, _embed

register("mental-health-billing-and-parity-rights", {
    "title": "Mental Health Billing: Your Rights Under Parity Laws and How to Fight Denials",
    "meta_description": "Insurers must cover mental health the same as physical health under federal parity law. Learn your rights, how to spot violations, and how to appeal a denial.",
    "published": "2026-02-19",
    "author": "BillKarma Team",
    "category": "Patient Rights",
    "faqs": [
        {
            "q": "What is mental health parity and why does it matter?",
            "a": "The Mental Health Parity and Addiction Equity Act (MHPAEA) requires most health insurance plans to cover mental health and substance use disorder services no more restrictively than physical health services. If your plan covers 20 physical therapy visits per year, it generally cannot limit mental health therapy to fewer visits.",
        },
        {
            "q": "My insurance denied my therapy claim. Can I appeal?",
            "a": "Yes, and you should. Denial rates for mental health claims are higher than for medical/surgical claims, but appeal success rates are also high. Request the denial reason in writing, document the medical necessity of your treatment, and file an internal appeal. If that fails, request an external review—the external reviewer's decision is binding on the insurer.",
        },
        {
            "q": "What does 'out-of-network' mean for mental health billing?",
            "a": "If your therapist or psychiatrist is out-of-network, your insurer may cover a portion of the cost at a lower reimbursement rate. However, parity law requires the out-of-network mental health benefit to be no more restrictive than the out-of-network medical/surgical benefit. If your plan covers 70% of out-of-network surgeon fees, it must cover 70% of out-of-network psychiatrist fees too.",
        },
        {
            "q": "What is a mental health parity violation?",
            "a": "A parity violation occurs when an insurer applies more restrictive limitations to mental health coverage than to comparable medical coverage. Examples include: requiring prior authorization for mental health but not medical visits, limiting mental health to 30 sessions per year when physical therapy has no annual limit, or applying higher cost-sharing for mental health than for primary care.",
        },
        {
            "q": "Can my insurer require prior authorization for mental health visits?",
            "a": "Only if they also require prior authorization for equivalent medical/surgical services. If your insurer requires prior authorization for therapy sessions but not for physical therapy or specialist visits, that is a potential parity violation. Document the disparity and file a complaint with your state insurance commissioner.",
        },
        {
            "q": "What CPT codes are used for mental health billing?",
            "a": "Common mental health CPT codes include 90837 (individual therapy, 60 min), 90834 (individual therapy, 45 min), 90847 (family therapy with patient), 90853 (group therapy), 99213/99214 (psychiatric E&M visit), and 96130-96133 (psychological testing). Each has a specific Medicare/Medicaid rate that can be used as a benchmark.",
        },
    ],
    "body": f"""
<p class="lead">Federal law has required insurance parity for mental health since 2008—but insurers deny mental health claims at rates <strong>4–6 times higher</strong> than medical/surgical claims, according to a 2023 AHIP analysis. If your therapy or psychiatry claim was denied, limited, or subjected to prior authorization hurdles that don't apply to other medical care, you may be facing an illegal parity violation. Here's how to identify it and fight back.</p>

<nav class="toc">
    <h2>In this guide</h2>
    <ol>
        <li><a href="#what-is-parity">What is mental health parity?</a></li>
        <li><a href="#parity-violations">Common parity violations to look for</a></li>
        <li><a href="#cpt-codes">Mental health CPT codes and billing basics</a></li>
        <li><a href="#reading-your-eob">Reading your EOB for mental health claims</a></li>
        <li><a href="#appeal-a-denial">How to appeal a mental health claim denial</a></li>
        <li><a href="#out-of-network">Out-of-network mental health rights</a></li>
        <li><a href="#file-a-complaint">Filing a parity complaint</a></li>
        <li><a href="#faq">Frequently asked questions</a></li>
        <li><a href="#sources">Sources</a></li>
    </ol>
</nav>

<h2 id="what-is-parity">1. What is mental health parity?</h2>

<p>The Mental Health Parity and Addiction Equity Act (MHPAEA), passed in 2008 and strengthened in 2021 and 2024, requires most group health plans and health insurance issuers to provide coverage for mental health (MH) and substance use disorder (SUD) services that is comparable to coverage for medical and surgical services.</p>

<p>Parity applies to three types of coverage limits:</p>

<ul>
    <li><strong>Quantitative treatment limits (QTLs)</strong> — Numerical limits like visit caps, day limits for inpatient stays, or dollar maximums. If your plan allows unlimited physical therapy visits, it cannot cap mental health therapy visits.</li>
    <li><strong>Non-quantitative treatment limits (NQTLs)</strong> — Non-numerical restrictions like prior authorization requirements, step therapy protocols (requiring cheaper treatments first), and fail-first policies. If prior auth isn't required for a cardiologist visit, it generally can't be required for a psychiatrist visit.</li>
    <li><strong>Financial requirements</strong> — Copays, coinsurance, and deductibles. Mental health cost-sharing cannot be higher than for comparable medical services.</li>
</ul>

<div class="key-takeaway">
    <strong>Parity applies within benefit classifications.</strong> The comparison is made between mental health and medical/surgical benefits within the same classification: inpatient in-network, inpatient out-of-network, outpatient in-network, and outpatient out-of-network. Each must be compared separately.
</div>

<h2 id="parity-violations">2. Common parity violations to look for</h2>

<p>These are the most frequently documented parity violations. Compare your mental health benefit against your medical/surgical benefit in each category:</p>

<table>
    <thead>
        <tr><th>What to Compare</th><th>Potential Violation If...</th></tr>
    </thead>
    <tbody>
        <tr><td>Visit limits</td><td>Mental health capped at 30 visits/year; physical therapy is unlimited</td></tr>
        <tr><td>Prior authorization</td><td>Required for therapy but not for specialist or physical therapy visits</td></tr>
        <tr><td>Step therapy</td><td>Must try medication before therapy is covered; no equivalent requirement for medical conditions</td></tr>
        <tr><td>Inpatient day limits</td><td>Psychiatric inpatient limited to 30 days; medical/surgical inpatient has no day limit</td></tr>
        <tr><td>Copay/coinsurance</td><td>Therapy copay is $60; primary care copay is $30 (same classification, different rate)</td></tr>
        <tr><td>Network adequacy</td><td>No in-network psychiatrists accepting new patients within 50 miles (de facto restriction)</td></tr>
        <tr><td>Medical necessity criteria</td><td>Insurer applies more stringent "medical necessity" standards to mental health than to medical care</td></tr>
    </tbody>
</table>

<div class="case-study">
    <h3>Example: Visit cap parity violation — $3,200 in denied claims reversed</h3>
    <p>A patient's employer health plan capped outpatient mental health therapy at 30 visits per year. Physical therapy had no annual visit limit. The patient had exceeded 30 therapy visits and was denied coverage for the remaining sessions. After filing a parity complaint with the Department of Labor (the agency overseeing employer plans), the insurer was required to retroactively cover all denied sessions and remove the visit cap. <strong>Total recovered: $3,200.</strong></p>
</div>

<h2 id="cpt-codes">3. Mental health CPT codes and billing basics</h2>

<p>Understanding the billing codes used for mental health services helps you verify that your claims were submitted correctly and your insurer processed them fairly:</p>

<table>
    <thead>
        <tr><th>CPT Code</th><th>Service</th><th>Medicare Rate (approx.)</th></tr>
    </thead>
    <tbody>
        <tr><td>90837</td><td>Individual psychotherapy, 60 minutes</td><td>$115–$145</td></tr>
        <tr><td>90834</td><td>Individual psychotherapy, 45 minutes</td><td>$85–$110</td></tr>
        <tr><td>90832</td><td>Individual psychotherapy, 30 minutes</td><td>$65–$85</td></tr>
        <tr><td>90847</td><td>Family psychotherapy with patient present</td><td>$115–$135</td></tr>
        <tr><td>90853</td><td>Group psychotherapy</td><td>$35–$55</td></tr>
        <tr><td>99214</td><td>Psychiatric E&amp;M, moderate complexity (psychiatrist office visit)</td><td>$110–$155</td></tr>
        <tr><td>90792</td><td>Psychiatric diagnostic evaluation with medical services</td><td>$175–$250</td></tr>
        <tr><td>96130</td><td>Psychological testing, first hour</td><td>$130–$180</td></tr>
    </tbody>
</table>

{_embed(mode="cost", title="Look up your mental health billing code", subtitle="Enter the CPT code from your bill or EOB to see what Medicare pays.")}

<p>Common mental health billing errors include:</p>

<ul>
    <li><strong>Wrong session length code</strong> — Billed as 90837 (60 min) when the session was 45 minutes (90834). This happens when a practice uses a standard template rather than documenting actual session length.</li>
    <li><strong>Missing modifier</strong> — Telehealth therapy sessions require specific modifiers (e.g., -95 or GT) to be covered. If your telehealth claim was denied, verify the modifier was included.</li>
    <li><strong>Incorrect diagnosis code</strong> — An incorrect ICD-10 code can cause a denial even when the service itself is covered. Ask your provider to confirm the diagnosis code submitted matches your actual diagnosis.</li>
</ul>

<h2 id="reading-your-eob">4. Reading your EOB for mental health claims</h2>

<p>Your Explanation of Benefits (EOB) is the key document for identifying parity issues. For every mental health claim, check:</p>

<ol>
    <li><strong>The denial reason code</strong> — Look for denial codes like "not medically necessary," "benefit limit reached," "prior authorization required," or "out-of-network provider." Each triggers a different response strategy.</li>
    <li><strong>The allowed amount</strong> — This is what your insurer agrees the service is worth. If the allowed amount for a therapy session is dramatically lower than for equivalent medical visits, that may indicate a parity violation.</li>
    <li><strong>Your cost-sharing</strong> — Compare your copay or coinsurance for mental health against what you pay for primary care or specialist visits. They should be the same within each classification.</li>
</ol>

<p>See our <a href="/guides/how-to-read-your-eob">complete EOB guide</a> for help reading each section of your explanation of benefits.</p>

<h2 id="appeal-a-denial">5. How to appeal a mental health claim denial</h2>

<p>When a mental health claim is denied, you have a structured appeals process with legal teeth:</p>

<ol>
    <li><strong>Get the denial in writing.</strong> Your insurer must provide a written denial with the specific reason and the clinical criteria used to make the decision. Request a copy of the "medical necessity criteria" they applied.</li>
    <li><strong>Obtain a letter of medical necessity.</strong> Your therapist, psychiatrist, or prescribing physician documents why the treatment is clinically necessary—the diagnosis, treatment goals, and why this specific type and frequency of care is appropriate.</li>
    <li><strong>File the internal appeal.</strong> Submit the letter of medical necessity plus any supporting clinical documentation (treatment notes, assessment results) to the insurer's appeals department. Most plans allow 60–180 days to file. Do not miss this deadline.</li>
    <li><strong>Request the insurer's criteria.</strong> Ask them to provide the specific clinical criteria they use to determine medical necessity for mental health. Compare this against the criteria they use for medical/surgical decisions. Divergence is evidence of a parity violation.</li>
    <li><strong>Request external review if the internal appeal is denied.</strong> Under the ACA, you have the right to an independent external review by a third party. The external reviewer's decision is binding on the insurer. Mental health denials are frequently overturned at this stage.</li>
</ol>

<div class="case-study">
    <h3>Example: "Not medically necessary" denial reversed on external review</h3>
    <p>A patient receiving intensive outpatient therapy (IOP) for depression had claims denied after session 20, with the insurer citing "medical necessity not established." The treating psychiatrist submitted a letter documenting the patient's GAD-7 score, treatment response, and clinical rationale for continued care. The internal appeal was denied. On external review, the independent reviewer found the insurer's criteria more restrictive than evidence-based guidelines for equivalent medical conditions—a parity violation. All sessions were covered retroactively. <strong>Total recovered: $4,800.</strong></p>
</div>

<h2 id="out-of-network">6. Out-of-network mental health rights</h2>

<p>Finding an in-network mental health provider can be genuinely difficult—therapist and psychiatrist networks are notoriously thin. Many patients end up going out-of-network. Here's what you're entitled to:</p>

<ul>
    <li><strong>Parity applies to OON benefits too.</strong> If your plan covers 70% of out-of-network surgeon fees, it must cover 70% of out-of-network psychiatrist fees. The coinsurance rate cannot be higher for mental health.</li>
    <li><strong>Submit claims for reimbursement.</strong> Even if your provider doesn't bill insurance directly, you can submit "superbills" (itemized receipts with CPT codes) to your insurer for out-of-network reimbursement.</li>
    <li><strong>Request a network adequacy exception.</strong> If no in-network providers are accepting new patients in your area, you can request that your insurer grant out-of-network coverage at in-network cost-sharing. Document your search attempts first—call at least 5–10 in-network providers and note that they're not accepting new patients or have wait times over 45 days.</li>
    <li><strong>Check the No Surprises Act.</strong> Some mental health services in hospital settings may be covered by No Surprises Act protections. See our <a href="/guides/no-surprises-act-explained">No Surprises Act guide</a> for details.</li>
</ul>

<div class="key-takeaway">
    <strong>Network adequacy exceptions are underused.</strong> If you cannot find an in-network mental health provider accepting new patients within a reasonable time and distance, most states require insurers to grant a single-case agreement allowing you to see an out-of-network provider at in-network rates. Ask your insurer directly for this exception.
</div>

<h2 id="file-a-complaint">7. Filing a parity complaint</h2>

<p>If your insurer denies your internal appeal and the external review doesn't go your way, or if you've documented a clear parity violation, you have several complaint channels:</p>

<table>
    <thead>
        <tr><th>Your Plan Type</th><th>Where to Complain</th><th>Agency</th></tr>
    </thead>
    <tbody>
        <tr><td>Employer-sponsored (ERISA plan)</td><td>Department of Labor Employee Benefits Security Administration</td><td><a href="https://www.dol.gov/agencies/ebsa" target="_blank" rel="noopener">dol.gov/agencies/ebsa</a></td></tr>
        <tr><td>Individual/marketplace plan</td><td>State Department of Insurance</td><td>Your state insurance commissioner</td></tr>
        <tr><td>Medicaid managed care</td><td>State Medicaid agency</td><td>Your state Medicaid office</td></tr>
        <tr><td>Any plan (federal oversight)</td><td>Department of Health and Human Services OCR</td><td><a href="https://www.hhs.gov/civil-rights/filing-a-complaint" target="_blank" rel="noopener">hhs.gov</a></td></tr>
    </tbody>
</table>

<p>When filing, include: your policy number, the specific services denied, the dates of denial, the medical necessity criteria the insurer applied, and documentation of how the treatment limits compare to equivalent medical benefits. The more specific your complaint, the more likely the agency can investigate.</p>

<h2 id="faq">Frequently asked questions</h2>

<div class="faq-section">
    <div class="faq-item">
        <h3>What is mental health parity and why does it matter?</h3>
        <p>The Mental Health Parity and Addiction Equity Act (MHPAEA) requires most health plans to cover mental health and substance use disorder services no more restrictively than physical health services. This means visit limits, prior authorization requirements, and cost-sharing must be comparable between mental health and medical/surgical benefits.</p>
    </div>

    <div class="faq-item">
        <h3>My insurance denied my therapy claim. Can I appeal?</h3>
        <p>Yes, and you should. Obtain the denial reason in writing, get a letter of medical necessity from your provider, and file an internal appeal. If denied again, request an independent external review—this is your right under the ACA, and external reviewers overturn mental health denials at high rates.</p>
    </div>

    <div class="faq-item">
        <h3>What does 'out-of-network' mean for mental health billing?</h3>
        <p>If your therapist or psychiatrist is out-of-network, your insurer covers a portion of the cost at a lower rate. However, parity law requires out-of-network mental health reimbursement to be no more restrictive than for out-of-network medical/surgical providers. If you can't find an in-network provider, request a network adequacy exception for in-network coverage.</p>
    </div>

    <div class="faq-item">
        <h3>What is a mental health parity violation?</h3>
        <p>A parity violation occurs when an insurer applies more restrictive limits to mental health coverage than to equivalent medical coverage. Common examples: requiring prior authorization for therapy but not physical therapy, capping mental health visits when medical visits are unlimited, or charging higher copays for psychiatry than for primary care.</p>
    </div>

    <div class="faq-item">
        <h3>Can my insurer require prior authorization for mental health visits?</h3>
        <p>Only if they require prior authorization for equivalent medical/surgical services. If prior auth is required for therapy but not for physical therapy or specialist visits, that's a potential parity violation. Document the disparity and file a complaint with your state insurance commissioner or the Department of Labor (for employer plans).</p>
    </div>

    <div class="faq-item">
        <h3>What CPT codes are used for mental health billing?</h3>
        <p>Common codes include 90837 (60-minute therapy, ~$120), 90834 (45-minute therapy, ~$90), 90847 (family therapy, ~$120), 90853 (group therapy, ~$45), and 99214 (psychiatric office visit, ~$130). Use our <a href="/calculator">cost calculator</a> to look up any code from your bill.</p>
    </div>
</div>

<h2 id="sources">Sources</h2>

<ul class="sources-list">
    <li><a href="https://www.cms.gov/CCIIO/Programs-and-Initiatives/Other-Insurance-Protections/mhpaea_factsheet" target="_blank" rel="noopener">CMS: Mental Health Parity and Addiction Equity Act (MHPAEA)</a></li>
    <li><a href="https://www.dol.gov/agencies/ebsa/laws-and-regulations/laws/mental-health-parity" target="_blank" rel="noopener">Department of Labor: MHPAEA Compliance Guidance</a></li>
    <li><a href="https://www.hhs.gov/sites/default/files/mhpaea-report-to-congress-2022.pdf" target="_blank" rel="noopener">HHS: MHPAEA Report to Congress (2022)</a></li>
    <li><a href="https://kffhealthnews.org/news/article/mental-health-parity-insurance-denials/" target="_blank" rel="noopener">KFF Health News: Mental Health Coverage Denials and Parity</a></li>
    <li><a href="https://www.cms.gov/medicare/payment/fee-schedules/physician" target="_blank" rel="noopener">CMS Medicare Physician Fee Schedule — Mental Health CPT Rates (2026)</a></li>
    <li><a href="https://www.naic.org/documents/prod_serv_consumer_mental_health_guide.pdf" target="_blank" rel="noopener">NAIC: Consumer Guide to Mental Health Benefits</a></li>
</ul>
""",
})
