"""Guide: Prior Authorization — Why Insurance Delays Your Care and How to Fight Back."""

from guides import register, _embed

register("prior-authorization", {
    "title": "Prior Authorization: Why Insurance Delays Your Care (And How to Fight Back)",
    "meta_description": "Insurance plans improperly denied 13% of valid prior auth requests, yet 75% of appeals succeed. Learn what triggers PA requirements, why requests get denied, and how to appeal.",
    "published": "2026-02-19",
    "author": "BillKarma Team",
    "category": "Insurance Basics",
    "faqs": [
        {
            "q": "What is prior authorization?",
            "a": "Prior authorization (PA), also called pre-authorization or pre-certification, is a requirement that your doctor get approval from your health insurance plan before they provide a specific service, drug, or procedure. Without it, your insurance may deny coverage for that service. PA is most common for brand-name drugs, specialty medications, MRI/CT scans, elective surgeries, and certain therapies.",
        },
        {
            "q": "How long does prior authorization take?",
            "a": "For non-urgent services, insurance plans are generally required to respond to PA requests within 3-15 business days depending on your state and plan type. For urgent requests, most plans must respond within 72 hours. A 2024 CMS rule tightened these timelines for Medicare Advantage plans to 7 calendar days for non-urgent and 72 hours for urgent requests. Commercially insured patients should check their plan documents for exact timelines.",
        },
        {
            "q": "What are the most common reasons prior authorization is denied?",
            "a": "The most common denial reasons are: the service isn't covered under your plan, the insurer requires you to try a less expensive treatment first (step therapy), the documentation submitted doesn't demonstrate medical necessity, the provider used the wrong code in the request, or the service requires a specialist referral that wasn't obtained. Many denials are due to administrative errors rather than genuine coverage issues.",
        },
        {
            "q": "Can I get care without prior authorization in an emergency?",
            "a": "Yes. Federal law requires health plans to cover emergency care without prior authorization. Under the No Surprises Act and the Affordable Care Act, insurers must cover emergency services at in-network cost-sharing levels regardless of whether the facility or provider is in-network, and without requiring PA. However, if an ER visit is later reclassified as non-emergency, the plan may retroactively apply PA requirements — this is worth fighting in an appeal.",
        },
        {
            "q": "What is step therapy and is it legal to require it?",
            "a": "Step therapy (also called fail-first) requires patients to try less expensive treatments before a plan will authorize a preferred treatment. It is legal in most circumstances, but many states have enacted laws limiting how step therapy can be applied, particularly when a patient has already tried and failed prior treatments. If you've already tried a medication and it didn't work, document that history and submit it with your PA request to request an exemption.",
        },
        {
            "q": "Do I have the right to an expedited appeal for a prior authorization denial?",
            "a": "Yes. If waiting for a standard appeal timeline would seriously jeopardize your health, you have the right to request an expedited (urgent) internal appeal. The plan must respond within 72 hours. If the internal appeal is denied, you can request an independent external review through your state's external review process, which must be completed within 72 hours for urgent cases under most state laws.",
        },
    ],
    "body": f"""
<p class="lead">In 2022, the American Medical Association found that <strong>94% of physicians</strong> reported that prior authorization had delayed necessary patient care, and 33% said PA had led to a serious adverse event for a patient. Prior authorization requests now take doctors&rsquo; offices an average of <strong>14 hours per week</strong> to process &mdash; and patients often absorb those delays in the form of postponed procedures, lapses in medication, and unexpected bills when the process fails. Here&rsquo;s how prior authorization actually works, why it gets denied, and what you can do about it.</p>

<nav class="toc">
    <h2>In this guide</h2>
    <ol>
        <li><a href="#what-is-pa">What is prior authorization?</a></li>
        <li><a href="#what-triggers-pa">What triggers a PA requirement?</a></li>
        <li><a href="#how-pa-works">How the prior authorization process works</a></li>
        <li><a href="#why-denied">Why PA requests get denied</a></li>
        <li><a href="#how-to-appeal">How to appeal a prior authorization denial</a></li>
        <li><a href="#expedited">Expedited appeals and urgent care situations</a></li>
        <li><a href="#new-rules">New PA rules in 2024&ndash;2026</a></li>
        <li><a href="#case-studies">Case studies: PA denials reversed</a></li>
        <li><a href="#faq">Frequently asked questions</a></li>
        <li><a href="#sources">Sources</a></li>
    </ol>
</nav>

<h2 id="what-is-pa">1. What is prior authorization?</h2>

<p>Prior authorization (PA) &mdash; also called pre-authorization, pre-certification, or pre-approval &mdash; is a process where your health insurance plan requires your doctor to obtain approval before you receive certain services, drugs, or procedures. Without that approval, your insurance may refuse to pay for the service, leaving you with the full bill.</p>

<p>PA was originally designed to prevent unnecessary or unsafe care. In practice, it has become a cost-control mechanism that affects care decisions daily. The services most commonly requiring PA include:</p>

<ul>
    <li>Brand-name and specialty drugs (particularly biologics)</li>
    <li>MRI and CT imaging</li>
    <li>Elective surgeries (joint replacement, bariatric surgery, some spine procedures)</li>
    <li>Inpatient hospital admissions for certain conditions</li>
    <li>Physical, occupational, and speech therapy beyond initial visits</li>
    <li>Home health and durable medical equipment</li>
    <li>Certain mental health and substance use disorder treatments</li>
</ul>

<div class="key-takeaway">
    <strong>PA is on your doctor&rsquo;s end, but the impact is on yours.</strong> If your doctor&rsquo;s office forgets to get PA, or the PA is denied and they don&rsquo;t appeal, you may receive the service and then get hit with a large bill. Always confirm PA status before any scheduled procedure or new prescription.
</div>

<h2 id="what-triggers-pa">2. What triggers a PA requirement?</h2>

<p>Your insurance plan publishes a list of services and drugs that require PA. This is typically found in your plan&rsquo;s formulary (drug list) and medical policy documents, accessible through your insurer&rsquo;s member portal. Common triggers:</p>

<table>
    <thead>
        <tr><th>Service Type</th><th>Common PA Trigger</th><th>Typical PA Required</th></tr>
    </thead>
    <tbody>
        <tr><td>Brand-name drug with a generic available</td><td>Always</td><td>Yes &mdash; must try generic first (step therapy)</td></tr>
        <tr><td>Specialty biologic (e.g., Humira, Dupixent)</td><td>Always</td><td>Yes &mdash; requires diagnosis documentation and often step therapy</td></tr>
        <tr><td>MRI or CT scan</td><td>Often</td><td>Yes for most plans &mdash; requires clinical justification</td></tr>
        <tr><td>Elective surgery (knee replacement, hernia)</td><td>Usually</td><td>Yes &mdash; requires diagnosis and conservative treatment history</td></tr>
        <tr><td>ER visit (retroactive review)</td><td>Sometimes</td><td>Plan may review after the fact for &ldquo;non-emergency&rdquo; reclassification</td></tr>
        <tr><td>Mental health inpatient admission</td><td>Often</td><td>Yes &mdash; and concurrent review (ongoing approval) may be required</td></tr>
        <tr><td>Physical therapy beyond initial visits</td><td>Common</td><td>Yes &mdash; typically after 6&ndash;12 visits</td></tr>
    </tbody>
</table>

<div class="key-takeaway">
    <strong>75% of appealed PA denials are overturned.</strong> If your PA was denied, appeal it &mdash; especially if the service is genuinely medically necessary. Most initial denials are not final decisions. See our <a href="/guides/how-to-appeal-an-insurance-denial">insurance denial appeal guide</a> for a step-by-step process.
</div>

<p><strong>How to check before you schedule:</strong> Call the member services number on your insurance card and ask: &ldquo;Does procedure code [CPT code] require prior authorization under my plan?&rdquo; Your doctor&rsquo;s office should also check as a routine step, but verifying yourself prevents surprises. Use our <a href="/calculator">calculator</a> to look up CPT codes if you don&rsquo;t have the code handy.</p>

<h2 id="how-pa-works">3. How the prior authorization process works</h2>

<p>The PA process involves multiple parties and can break down at several points:</p>

<ol>
    <li><strong>Your doctor submits the request</strong> &mdash; Either through the insurer&rsquo;s online portal, by fax, or by phone. The request includes CPT codes, diagnosis codes (ICD-10), clinical notes supporting medical necessity, and sometimes peer-reviewed literature.</li>
    <li><strong>The insurer reviews the request</strong> &mdash; A clinical reviewer (often a nurse, then a medical director if denied) applies the insurer&rsquo;s clinical criteria to determine medical necessity. These criteria are proprietary and are not always disclosed to physicians or patients.</li>
    <li><strong>Decision is issued</strong> &mdash; Approved, denied, or pended (additional information requested). Denials must include a reason and information on appeal rights.</li>
    <li><strong>If approved</strong> &mdash; The authorization number is issued. The service must typically be rendered within a specified window (30&ndash;180 days depending on the plan). Note: PA approval is not a guarantee of payment &mdash; the insurer can still deny the claim on other grounds later.</li>
    <li><strong>If denied</strong> &mdash; Your doctor can appeal internally, or you can appeal directly as the patient. You have independent appeal rights regardless of what your doctor does.</li>
</ol>

<div class="bill-example">
    <div class="bill-header">Sample PA Timeline: MRI of the Lumbar Spine (CPT 72148)</div>
    <div class="line-item">
        <span>Day 1 &mdash; Doctor&rsquo;s office submits PA request with diagnosis codes and clinical notes</span>
        <span></span>
    </div>
    <div class="line-item flagged">
        <span>Day 5 &mdash; Insurer sends &ldquo;additional information needed&rdquo; notice &nbsp; &#9888; <em>Missing: 6 weeks of conservative treatment documentation</em></span>
        <span></span>
    </div>
    <div class="line-item">
        <span>Day 7 &mdash; Doctor&rsquo;s office submits physical therapy notes showing 8 weeks of prior treatment</span>
        <span></span>
    </div>
    <div class="line-item error">
        <span>Day 12 &mdash; PA denied. Reason: &ldquo;Not medically necessary — conservative therapy not yet exhausted&rdquo; &nbsp; &#10060; <em>Even though 8 weeks of therapy were documented</em></span>
        <span></span>
    </div>
    <div class="line-item">
        <span>Day 13 &mdash; Patient files urgent appeal citing the submitted therapy notes</span>
        <span></span>
    </div>
    <div class="line-item">
        <span>Day 16 &mdash; Appeal approved. MRI authorized.</span>
        <span></span>
    </div>
</div>

<h2 id="why-denied">4. Why PA requests get denied</h2>

<p>A 2022 HHS Office of Inspector General report found that Medicare Advantage plans denied <strong>13% of prior authorization requests</strong> for services that met Medicare coverage rules &mdash; meaning they were denying care that should have been approved. Of those denied claims that were appealed, <strong>75% were ultimately overturned.</strong> That gap between initial denials and appeal reversals reveals the most important truth about PA: many denials are wrong, and many patients don&rsquo;t know to fight them.</p>

<p>The most common reasons for denial:</p>

<table>
    <thead>
        <tr><th>Denial Reason</th><th>What It Actually Means</th><th>Fix</th></tr>
    </thead>
    <tbody>
        <tr><td>Not medically necessary</td><td>Insurer&rsquo;s criteria not met — may be a documentation gap</td><td>Submit additional clinical notes, specialist letters, peer-reviewed literature</td></tr>
        <tr><td>Step therapy not completed</td><td>Must try first-line treatment first</td><td>Document failed prior treatments, or request step therapy exception</td></tr>
        <tr><td>Service not covered</td><td>May be accurate, or may be a miscoded request</td><td>Verify CPT and ICD codes; check your plan&rsquo;s coverage documents</td></tr>
        <tr><td>Wrong provider type</td><td>Service must be performed by a different specialist</td><td>Ensure the requesting provider has the right credentials for the service</td></tr>
        <tr><td>Incomplete information</td><td>Documentation package was missing required elements</td><td>Call the insurer and ask exactly what documentation is needed, then resubmit</td></tr>
    </tbody>
</table>

<div class="key-takeaway">
    <strong>Already received a bill from a denied service?</strong> <a href="/scan">Upload it to BillKarma</a> &mdash; we check whether the underlying charges are accurately coded, which is often the root cause of a PA denial and the strongest basis for an appeal.
</div>

<h2 id="how-to-appeal">5. How to appeal a prior authorization denial</h2>

<h3>Step 1: Get the denial letter and read it carefully</h3>
<p>Your insurer must provide a written denial that includes the specific reason for denial, the clinical criteria used, and instructions on how to appeal. If you received a verbal denial, request the written determination before doing anything else.</p>

<h3>Step 2: Identify the real issue</h3>
<p>Most PA denials fall into two categories: (a) administrative issues that can be fixed quickly, or (b) medical necessity disputes that require clinical documentation. Administrative fixes (wrong CPT code, missing prior authorization form, wrong provider type) can often be resolved with a phone call. Medical necessity disputes require your physician&rsquo;s involvement.</p>

<h3>Step 3: File the internal appeal</h3>
<p>You and your doctor can both file an internal appeal. You have the right to file independently &mdash; you don&rsquo;t need to wait for your doctor to act. The appeal must typically include:</p>
<ul>
    <li>A written statement explaining why you believe the service is medically necessary</li>
    <li>A letter from your treating physician supporting the service</li>
    <li>Copies of relevant test results, imaging reports, or treatment history</li>
    <li>Any peer-reviewed literature supporting the treatment (especially for newer therapies)</li>
    <li>Documentation of any prior treatments tried and failed (critical for step therapy denials)</li>
</ul>

<h3>Step 4: Request a peer-to-peer review</h3>
<p>Your doctor can request a peer-to-peer review &mdash; a direct conversation between your physician and the insurer&rsquo;s medical director who issued the denial. This is often the fastest way to get a denial reversed. During the call, your doctor makes the clinical case directly to the reviewer. Peer-to-peer success rates are higher than written appeals for complex cases.</p>

<h3>Step 5: External appeal</h3>
<p>If the internal appeal is denied and the amount in dispute is significant, you have the right to an external independent review. An independent organization (not your insurer) reviews the denial. Under federal law, plans must cover the service if the external reviewer approves it. External appeals for medical necessity are upheld in the patient&rsquo;s favor approximately 40&ndash;45% of the time.</p>

<h2 id="expedited">6. Expedited appeals and urgent care situations</h2>

<p>If waiting for a standard appeal timeline would seriously jeopardize your health or your ability to regain maximum function, you can request an <strong>expedited (urgent) appeal</strong>. The plan must respond within 72 hours. To qualify for expedited review, your physician typically needs to document that the standard timeline poses a health risk.</p>

<p>For situations where care is already happening (e.g., a hospitalization that might be terminated mid-stay due to a PA denial), you can request a <strong>concurrent review appeal</strong>. You have the right to remain in the hospital while this appeal is processed, and the plan cannot terminate coverage during the appeal period without giving you at least a day&rsquo;s notice.</p>

<div class="key-takeaway">
    <strong>Need the CPT code for your procedure?</strong> Use our <a href="/calculator">free calculator</a> to look up any service code &mdash; having the exact CPT code is the first step in verifying whether your plan requires PA and what the Medicare rate should be.
</div>

<p>Emergency care is never subject to prior authorization requirements. Under federal law (and the ACA), emergency services must be covered at in-network cost-sharing regardless of network status, without requiring PA. If an insurer tries to retroactively deny a genuine emergency visit as &ldquo;non-emergency,&rdquo; you can appeal citing the prudent layperson standard: the ER visit was appropriate because a reasonable person with the same symptoms would have believed they needed emergency care.</p>

<h2 id="new-rules">7. New PA rules in 2024&ndash;2026</h2>

<p>Federal regulators have tightened prior authorization requirements significantly in recent years:</p>

<table>
    <thead>
        <tr><th>Rule</th><th>Effective Date</th><th>Key Change</th></tr>
    </thead>
    <tbody>
        <tr><td>CMS Interoperability &amp; Prior Authorization Final Rule</td><td>January 2024</td><td>Medicare Advantage, Medicaid, and CHIP plans must respond to urgent PA requests within 72 hours, non-urgent within 7 calendar days. Must state specific denial reasons.</td></tr>
        <tr><td>Gold Carding</td><td>Various states, 2022&ndash;2026</td><td>Several states require insurers to exempt physicians with high PA approval rates from routine PA requirements (&ldquo;gold carding&rdquo;). Check if your state has this protection.</td></tr>
        <tr><td>Step Therapy Exceptions</td><td>Many states</td><td>Dozens of states now require health plans to provide an exception to step therapy requirements when a patient has previously failed a required first-line drug, when it would cause adverse effects, or when a physician documents medical necessity.</td></tr>
        <tr><td>Prior Auth Transparency</td><td>Federal, 2024</td><td>Plans must publish their PA criteria publicly, including which services require PA and the clinical criteria used to make decisions.</td></tr>
    </tbody>
</table>

<h2 id="case-studies">8. Case studies: PA denials reversed</h2>

<div class="case-study">
    <h3>Case Study 1: Humira denied for rheumatoid arthritis — reversed on appeal</h3>
    <p>A patient with rheumatoid arthritis was prescribed Humira (adalimumab) by her rheumatologist. Her insurer denied the PA, citing step therapy requirements: she needed to try and fail two less expensive DMARDs (disease-modifying antirheumatic drugs) first, specifically methotrexate and hydroxychloroquine. The patient had tried methotrexate three years earlier with a previous insurer, but the new insurer had no record of it.</p>
    <p>Her rheumatologist obtained her prior treatment records and submitted them with a peer-to-peer review request, showing the documented methotrexate failure and intolerance to hydroxychloroquine. The medical director reversed the denial the same day. <strong>Result: Humira approved, no disruption in care.</strong></p>
    <p>Key lesson: Bring your treatment history to every PA request. Prior insurer records count toward step therapy requirements.</p>
</div>

<div class="case-study">
    <h3>Case Study 2: Lumbar MRI denied, appeal overturned — $1,800 claim covered</h3>
    <p>A patient with six weeks of lower back pain and leg numbness was referred for an MRI (CPT 72148). Her Medicare Advantage plan denied the PA, citing that &ldquo;conservative therapy had not been exhausted.&rdquo; She had completed eight sessions of physical therapy, which were documented in the chart.</p>
    <p>The denial letter cited the wrong clinical criteria &mdash; it referenced criteria for patients with fewer than six weeks of symptoms, but her symptoms had lasted six weeks. She filed a written internal appeal attaching her PT records and the denial letter&rsquo;s own criteria language, pointing out the discrepancy. The plan reversed the denial within five days. <strong>MRI approved; $1,800 imaging bill covered.</strong></p>
</div>

<div class="case-study">
    <h3>Case Study 3: Mental health inpatient, PA withdrawn mid-stay — expedited appeal</h3>
    <p>A patient admitted to a psychiatric facility for severe depression received notice on day four that her insurer was terminating authorization for further inpatient care. Her treatment team filed an expedited internal appeal, submitting documentation that she remained at risk for self-harm and did not meet discharge criteria. The plan was required to respond within 72 hours. The plan reversed the termination and authorized an additional three days of inpatient care. <strong>Coverage restored; $4,200 in additional inpatient charges covered.</strong></p>
</div>

{_embed(mode="cost", title="Look up the CPT code for your procedure", subtitle="Enter your procedure or service to see the billing code and Medicare rate.")}

<h2 id="faq">Frequently asked questions</h2>

<div class="faq-section">
    <div class="faq-item">
        <h3>What is prior authorization?</h3>
        <p>Prior authorization is a requirement that your insurance company approve a service, drug, or procedure before you receive it. Without approval, your plan may deny coverage. PA is most common for brand-name drugs, specialty medications, MRI/CT scans, elective surgeries, and certain therapies.</p>
    </div>

    <div class="faq-item">
        <h3>How long does prior authorization take?</h3>
        <p>For non-urgent services, most plans are required to respond within 3&ndash;15 business days. A 2024 CMS rule requires Medicare Advantage plans to respond within 7 calendar days for non-urgent requests and 72 hours for urgent ones. Commercial plan timelines vary &mdash; check your plan documents for specifics.</p>
    </div>

    <div class="faq-item">
        <h3>What are the most common reasons prior authorization is denied?</h3>
        <p>The most common reasons are: missing documentation of medical necessity, step therapy requirements not yet met, incorrect codes submitted in the request, or service not covered under the plan. Many denials are administrative errors &mdash; a 2022 OIG report found 75% of appealed PA denials were overturned. Always appeal a denial before accepting it.</p>
    </div>

    <div class="faq-item">
        <h3>Can I get care without prior authorization in an emergency?</h3>
        <p>Yes. Federal law requires health plans to cover emergency care without prior authorization. If an insurer tries to retroactively reclassify your ER visit as non-emergency, you can appeal using the &ldquo;prudent layperson&rdquo; standard &mdash; a reasonable person with your symptoms would have sought emergency care. See our <a href="/guides/how-to-appeal-an-insurance-denial">insurance denial appeal guide</a>.</p>
    </div>

    <div class="faq-item">
        <h3>What is step therapy and is it legal to require it?</h3>
        <p>Step therapy requires you to try lower-cost treatments before a plan will authorize a preferred treatment. It is legal in most cases, but many states require plans to grant exceptions when a patient has previously tried and failed the first-line treatment, or when it would cause adverse effects. Document prior treatment history and submit it with your PA request.</p>
    </div>

    <div class="faq-item">
        <h3>Do I have the right to an expedited appeal for a prior authorization denial?</h3>
        <p>Yes. If waiting would seriously jeopardize your health, you can request an expedited (urgent) internal appeal. The plan must respond within 72 hours. If denied, you can request an expedited external independent review, which must also be completed within 72 hours under most state laws.</p>
    </div>
</div>

<h2 id="sources">Sources</h2>

<ul class="sources-list">
    <li><a href="https://oig.hhs.gov/oei/reports/OEI-09-18-00260.asp" target="_blank" rel="noopener">HHS OIG: Medicare Advantage Prior Authorization Denials (2022)</a></li>
    <li><a href="https://www.ama-assn.org/practice-management/prior-authorization/prior-authorization-and-the-physician" target="_blank" rel="noopener">AMA: 2022 Prior Authorization Physician Survey</a></li>
    <li><a href="https://www.cms.gov/newsroom/fact-sheets/cms-interoperability-and-prior-authorization-final-rule-cms-0057-f" target="_blank" rel="noopener">CMS: Interoperability and Prior Authorization Final Rule (2024)</a></li>
    <li><a href="https://www.kff.org/private-insurance/issue-brief/prior-authorization-in-medicare-advantage/" target="_blank" rel="noopener">KFF: Prior Authorization in Medicare Advantage (2023)</a></li>
    <li><a href="https://www.cms.gov/regulations-and-guidance/guidance/manuals/downloads/bp102c04.pdf" target="_blank" rel="noopener">CMS: Medicare Managed Care Manual — Appeals and Grievances</a></li>
    <li><a href="https://www.ncsl.org/health/prior-authorization-state-laws" target="_blank" rel="noopener">NCSL: State Prior Authorization Laws (2025)</a></li>
</ul>
""",
})
