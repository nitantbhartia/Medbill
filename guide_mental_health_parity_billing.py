"""Guide: Mental Health Parity: Making Insurers Cover Therapy & Psychiatry (2026)"""

from guides import register, _embed

register("mental-health-parity-billing", {
    "title": "Mental Health Parity: Making Insurers Cover Therapy & Psychiatry (2026)",
    "meta_description": "The Mental Health Parity law requires insurers to cover therapy and psychiatry as well as physical care — but violations are common. Here's how to identify them and fight back.",
    "published": "2026-04-05",
    "author": "BillKarma Team",
    "category": "Insurance & Coverage",
    "faqs": [
        {
            "q": "What is the Mental Health Parity and Addiction Equity Act?",
            "a": "The Mental Health Parity and Addiction Equity Act (MHPAEA), passed in 2008 and significantly strengthened by final rules in 2024, requires that health insurance plans covering mental health and substance use disorder (MH/SUD) benefits do so at parity with medical and surgical benefits. This means the copays, deductibles, prior authorization requirements, visit limits, and network adequacy standards for mental health care cannot be more restrictive than those for equivalent physical health care. Violations are common — and patients have legal tools to fight them.",
        },
        {
            "q": "What are the most common mental health parity violations?",
            "a": "The most common violations are: (1) requiring prior authorization for mental health or substance use visits but not for comparable medical visits; (2) applying visit limits to therapy sessions but not to physical therapy; (3) having narrower provider networks for psychiatrists and therapists compared to primary care physicians; (4) requiring step therapy (trying cheaper treatments first) for psychiatric medications but not for medical medications; and (5) higher out-of-pocket maximums for mental health services than for equivalent medical services.",
        },
        {
            "q": "How do I request a parity analysis from my insurer?",
            "a": "Under the 2024 MHPAEA final rule, insurers must provide a written comparative analysis of any non-quantitative treatment limitation (NQTL) applied to mental health benefits upon request. Send a written request to your insurer's compliance department asking for the NQTL comparative analysis for the specific limitation you believe violates parity — for example, prior authorization for outpatient therapy. They must respond within 30 days (or as required by your state). If they cannot justify the limitation, they must remove it.",
        },
        {
            "q": "Where do I file a mental health parity complaint?",
            "a": "It depends on your plan type. For employer-sponsored plans (ERISA plans), file a complaint with the U.S. Department of Labor's Employee Benefits Security Administration (EBSA) at dol.gov/ebsa. For ACA marketplace or individual plans, file with your state insurance commissioner. For Medicaid managed care plans, file with your state Medicaid agency. For Medicare Advantage plans, file with CMS. You can also file an ERISA internal appeal with your employer's plan administrator and, if denied, sue in federal court.",
        },
        {
            "q": "Can my insurer require prior authorization for therapy?",
            "a": "Yes — but only if they apply the same prior authorization requirements to comparable medical or surgical benefits. If your plan requires prior auth for therapy visits but not for equivalent outpatient medical visits (like cardiology follow-ups), that is a parity violation. The test is whether the limitation is applied more stringently to mental health care than to medical care — and if it is, you can challenge it.",
        },
    ],
    "body": f"""
<p class="lead">The Mental Health Parity and Addiction Equity Act (MHPAEA) has been federal law since 2008 — but <strong>insurers violate it constantly</strong>. Requiring more prior auths for therapy than for physical therapy, narrower psychiatry networks than cardiology networks, and step therapy for psychiatric meds but not medical ones are all violations. The 2024 final rule gave patients stronger tools to fight back. This guide explains what parity means, what violations look like, and exactly how to challenge your insurer.</p>

<nav class="toc">
    <h2>In this guide</h2>
    <ol>
        <li><a href="#what-is-parity">What the MHPAEA requires</a></li>
        <li><a href="#quantitative-vs-nqtl">Quantitative vs. non-quantitative treatment limitations</a></li>
        <li><a href="#common-violations">Common parity violations to look for</a></li>
        <li><a href="#2024-rule">The 2024 final rule: what changed</a></li>
        <li><a href="#requesting-analysis">How to request your insurer's NQTL analysis</a></li>
        <li><a href="#filing-complaint">How to file a parity complaint</a></li>
        <li><a href="#erisa-appeals">ERISA appeals and litigation</a></li>
        <li><a href="#faq">Frequently asked questions</a></li>
        <li><a href="#sources">Sources</a></li>
    </ol>
</nav>

<h2 id="what-is-parity">1. What the MHPAEA requires</h2>

<p>The Mental Health Parity and Addiction Equity Act (MHPAEA) applies to:</p>

<ul>
    <li>Large employer group health plans (50+ employees)</li>
    <li>Individual and small group plans sold through ACA marketplaces</li>
    <li>Medicaid managed care organizations</li>
    <li>Children's Health Insurance Program (CHIP)</li>
    <li>Federal Employee Health Benefit plans</li>
</ul>

<p>The law does <em>not</em> require plans to cover mental health benefits — but if they do, those benefits must be at parity with medical and surgical benefits. In practice, virtually all employer and ACA plans cover mental health, so parity applies broadly.</p>

<p>Parity applies across <strong>six benefit classifications</strong>:</p>

<ol>
    <li>Inpatient, in-network</li>
    <li>Inpatient, out-of-network</li>
    <li>Outpatient, in-network</li>
    <li>Outpatient, out-of-network</li>
    <li>Emergency care</li>
    <li>Prescription drugs</li>
</ol>

<p>For each classification, the limitations applied to mental health and substance use disorder (MH/SUD) benefits cannot be more restrictive than those applied to the "predominant" medical and surgical benefits in that same classification.</p>

<h2 id="quantitative-vs-nqtl">2. Quantitative vs. non-quantitative treatment limitations</h2>

<table>
    <thead>
        <tr><th>Type</th><th>Definition</th><th>Examples</th></tr>
    </thead>
    <tbody>
        <tr><td><strong>Quantitative Treatment Limitations (QTLs)</strong></td><td>Numeric limits expressed as a count or dollar amount</td><td>Visit limits ("20 therapy sessions/year"), day limits ("30 inpatient psychiatric days"), dollar limits ("$500 mental health benefit cap")</td></tr>
        <tr><td><strong>Non-Quantitative Treatment Limitations (NQTLs)</strong></td><td>Non-numeric criteria that limit the scope or duration of benefits</td><td>Prior authorization requirements, step therapy, network adequacy standards, geographic limitations, fail-first protocols, reimbursement rate-setting, clinical criteria for coverage</td></tr>
    </tbody>
</table>

<p>NQTLs are where most violations occur and where the law is most complex. The 2024 rule requires insurers to conduct and document a comparative analysis showing that any NQTL applied to MH/SUD benefits is no more stringent — in both design and application — than limitations applied to medical and surgical benefits.</p>

<h2 id="common-violations">3. Common parity violations to look for</h2>

<p>Review your Explanation of Benefits (EOB), plan documents (Summary Plan Description), and any denial letters for these patterns:</p>

<ol>
    <li><strong>Prior authorization asymmetry.</strong> Your plan requires prior auth for outpatient therapy visits but not for outpatient visits to a cardiologist or endocrinologist. Both are outpatient specialist care — prior auth cannot apply more stringently to mental health.</li>
    <li><strong>Visit limits on therapy.</strong> A cap of 20 or 30 therapy sessions per year when there is no equivalent visit cap on other specialist care is a QTL parity violation.</li>
    <li><strong>Narrow psychiatry networks.</strong> If your plan has 10 in-network primary care physicians per 1,000 enrollees but only 1–2 in-network psychiatrists per 1,000 enrollees, that network inadequacy may violate parity. Signs: "No in-network therapists available," long wait times, or being unable to find a provider who is accepting patients.</li>
    <li><strong>Step therapy for psychiatric medications.</strong> Being required to try and fail on generic medications before your plan covers a brand-name psychiatric drug, when equivalent medical conditions don't face the same requirement.</li>
    <li><strong>Different reimbursement rates.</strong> If your plan reimburses mental health providers at rates that make it economically impossible for them to participate in-network while medical providers are reimbursed at standard rates, this is a parity violation under the 2024 rule.</li>
    <li><strong>Higher out-of-pocket maximums.</strong> Separate (higher) deductibles or out-of-pocket maximums for mental health services compared to medical services in the same benefit classification.</li>
</ol>

<div class="key-takeaway">
    <strong>Your EOB is the evidence.</strong> Upload your EOB and insurance denial letters to <a href="/fight-debt">BillKarma</a> — we can help identify patterns consistent with parity violations across your mental health claims.
</div>

<h2 id="2024-rule">4. The 2024 final rule: what changed</h2>

<p>The Department of Labor, Treasury, and Health and Human Services issued a final MHPAEA rule in September 2024 that significantly strengthened enforcement:</p>

<ul>
    <li><strong>Affirmative obligation to design parity.</strong> Plans must affirmatively ensure NQTLs comply with parity — they cannot wait for patients to challenge violations. This is a shift from the pre-2024 framework where the burden was largely on the patient.</li>
    <li><strong>Data analysis required.</strong> Plans must collect and evaluate data on outcomes (such as prior authorization denial rates and out-of-network utilization rates) to assess whether their NQTLs create a disparity in access to MH/SUD care. If the data shows a disparity, the plan must take corrective action.</li>
    <li><strong>Network adequacy parity.</strong> The 2024 rule explicitly clarifies that network composition — including provider reimbursement rates — is an NQTL subject to parity analysis. "Ghost networks" (directories listing providers who don't actually take new patients) can now be challenged as parity violations.</li>
    <li><strong>Increased transparency.</strong> Plans must provide NQTL comparative analyses to participants and beneficiaries, regulators, or employers within 10 business days of a request (down from 30 days in practice).</li>
    <li><strong>State insurance parity laws.</strong> Many states have parity laws that go beyond federal MHPAEA requirements. Check your state insurance commissioner's website for state-specific protections.</li>
</ul>

<h2 id="requesting-analysis">5. How to request your insurer's NQTL analysis</h2>

<p>Under MHPAEA, you have the right to request a written comparative analysis of any NQTL applied to your mental health benefits. Here is how:</p>

<ol>
    <li><strong>Identify the specific limitation.</strong> Be specific in your request: "prior authorization requirements for outpatient mental health visits," not just "mental health coverage." The more specific, the harder it is for the insurer to stall.</li>
    <li><strong>Send a written request.</strong> Email or certified mail to the insurer's compliance department or appeals department. Reference MHPAEA Section 2726(a)(8) and the plan's obligation to provide a comparative analysis.</li>
    <li><strong>Sample language:</strong> "Pursuant to the Mental Health Parity and Addiction Equity Act (29 U.S.C. § 1185a) and the 2024 Final Rule, I request the written comparative analysis for the non-quantitative treatment limitation of [prior authorization / step therapy / network adequacy] as applied to [outpatient mental health / substance use disorder] benefits under my plan."</li>
    <li><strong>Document the response.</strong> The insurer must provide the analysis or explain why the limitation complies with parity. An inadequate response — or a refusal to provide the analysis — is itself grounds for a regulatory complaint.</li>
</ol>

<h2 id="filing-complaint">6. How to file a parity complaint</h2>

<table>
    <thead>
        <tr><th>Plan type</th><th>Where to file</th><th>Contact</th></tr>
    </thead>
    <tbody>
        <tr><td>Employer-sponsored (ERISA) plan</td><td>Dept. of Labor — Employee Benefits Security Administration (EBSA)</td><td>dol.gov/ebsa or 1-866-444-3272</td></tr>
        <tr><td>ACA marketplace / individual plan</td><td>State insurance commissioner</td><td>Search "[your state] insurance commissioner"</td></tr>
        <tr><td>Small group ACA plan</td><td>State insurance commissioner</td><td>Same as above</td></tr>
        <tr><td>Medicaid managed care</td><td>State Medicaid agency</td><td>Search "[your state] Medicaid complaint"</td></tr>
        <tr><td>Medicare Advantage</td><td>CMS — Medicare complaint process</td><td>1-800-MEDICARE or cms.gov</td></tr>
        <tr><td>Federal employee plan (FEHB)</td><td>Office of Personnel Management</td><td>opm.gov/healthcare-insurance</td></tr>
    </tbody>
</table>

<p>When filing a complaint:</p>
<ul>
    <li>Include your plan documents or Summary Plan Description</li>
    <li>Include copies of any denial letters</li>
    <li>Include your EOBs showing the disparity in treatment</li>
    <li>Reference the specific MHPAEA provision you believe was violated</li>
    <li>Include the insurer's response to your NQTL analysis request (or note that they refused to provide one)</li>
</ul>

<h2 id="erisa-appeals">7. ERISA appeals and litigation</h2>

<p>For employer-sponsored plans (which cover most working Americans), the process before litigation is:</p>

<ol>
    <li><strong>Internal appeal.</strong> File a formal internal appeal with your plan administrator within 180 days of the denial. You are entitled to a full and fair review. For mental health denials, request that the review be conducted by a mental health professional with appropriate expertise.</li>
    <li><strong>External review.</strong> After exhausting internal appeals, request an independent external review. For urgent care, external review can happen simultaneously with internal appeal. Under the ACA, most plans must offer external review.</li>
    <li><strong>ERISA lawsuit.</strong> If internal and external appeals are exhausted, you can sue the plan in federal court under ERISA Section 502(a). MHPAEA violations are an independent basis for relief. Courts have awarded attorneys' fees in MHPAEA cases, making it feasible for patients to find representation on a contingency basis.</li>
</ol>

<p>The most important cases in recent years — including <em>Wit v. United Behavioral Health</em> (9th Circuit) — have established that insurers must use generally accepted medical standards when making mental health coverage decisions, not internally developed cost-control guidelines that diverge from clinical standards of care.</p>

{_embed(mode="fight", title="Denied mental health coverage?", subtitle="BillKarma can help identify parity violations in your EOB and denial letters.")}

<h2 id="faq">Frequently asked questions</h2>

<div class="faq-section">
    <div class="faq-item">
        <h3>What is the Mental Health Parity and Addiction Equity Act?</h3>
        <p>MHPAEA requires that health plans covering mental health and substance use disorder benefits do so at parity with medical and surgical benefits. Copays, prior auth requirements, visit limits, and network standards for mental health cannot be more restrictive than for equivalent physical health care. The 2024 final rule strengthened enforcement and added data analysis requirements for insurers.</p>
    </div>

    <div class="faq-item">
        <h3>Does parity mean my insurer has to cover therapy?</h3>
        <p>No — parity only applies if your plan already covers mental health benefits. But virtually all employer plans and ACA marketplace plans are required to cover mental health as an essential health benefit (under the ACA). If your plan covers mental health, parity requires coverage terms to be no more restrictive than equivalent medical coverage.</p>
    </div>

    <div class="faq-item">
        <h3>My insurer denied my therapy claim as "not medically necessary." Is that a parity violation?</h3>
        <p>It may be. Ask your insurer what clinical criteria they used to make the "not medically necessary" determination. Under the 2024 rule, clinical criteria for mental health coverage cannot deviate from generally accepted standards of care. If they are using internal guidelines that are more restrictive than clinical standards, that is grounds for an appeal and potentially a parity complaint.</p>
    </div>

    <div class="faq-item">
        <h3>What is an NQTL comparative analysis and why should I request one?</h3>
        <p>A Non-Quantitative Treatment Limitation (NQTL) comparative analysis is the insurer's documentation showing that any non-numeric restriction on mental health benefits (like prior auth requirements or step therapy) is no more stringent than restrictions on comparable medical benefits. If the insurer cannot produce a credible analysis, or if the analysis reveals a disparity, you have strong grounds for a complaint or appeal.</p>
    </div>

    <div class="faq-item">
        <h3>There are no in-network therapists available in my area. Is that a parity violation?</h3>
        <p>Potentially yes. Under the 2024 rule, network composition is a non-quantitative treatment limitation subject to parity analysis. If your insurer's network has significantly fewer accessible mental health providers than medical providers — as evidenced by long wait times, providers not accepting new patients, or geographic gaps — that may violate parity. File a complaint with your state insurance commissioner (for ACA plans) or the DOL (for employer plans), and document your unsuccessful attempts to find an in-network provider.</p>
    </div>
</div>

<h2 id="sources">Sources</h2>

<ul class="sources-list">
    <li><a href="https://www.dol.gov/agencies/ebsa/laws-and-regulations/laws/mental-health-parity" target="_blank" rel="noopener">DOL: Mental Health Parity and Addiction Equity Act — EBSA</a></li>
    <li><a href="https://www.federalregister.gov/documents/2024/09/09/2024-19170/requirements-related-to-the-mental-health-parity-and-addiction-equity-act" target="_blank" rel="noopener">Federal Register: MHPAEA Final Rule (2024)</a></li>
    <li><a href="https://www.cms.gov/cciio/programs-and-initiatives/other-insurance-protections/mhpaea_factsheet" target="_blank" rel="noopener">CMS: Mental Health Parity Fact Sheet</a></li>
    <li><a href="https://www.kff.org/mental-health/issue-brief/mental-health-parity-at-a-crossroads/" target="_blank" rel="noopener">KFF: Mental Health Parity at a Crossroads</a></li>
    <li><a href="https://www.healthaffairs.org/content/forefront/mental-health-parity-compliance-whats-really-happening" target="_blank" rel="noopener">Health Affairs: Mental Health Parity Compliance — What's Really Happening</a></li>
    <li><a href="https://www.dol.gov/sites/dolgov/files/ebsa/about-ebsa/our-activities/resource-center/publications/mhpaea-self-compliance-tool.pdf" target="_blank" rel="noopener">DOL: MHPAEA Self-Compliance Tool for Patients and Employers</a></li>
</ul>
""",
})
