"""Guide: AI in Healthcare Patient Rights 2026."""

from guides import register, _embed

register("ai-healthcare-patient-rights-2026", {
    "title": "AI in Healthcare 2026: Your Rights When Algorithms Make Medical Decisions",
    "meta_description": "AI now drives 50% of prior auth denials. Learn your rights to human review, how to appeal AI-driven claim denials, and what CMS rules say about AI in healthcare.",
    "published": "2026-03-04",
    "author": "BillKarma Team",
    "category": "Consumer Rights",
    "faqs": [
        {
            "q": "Can my insurance company use AI to deny my claim?",
            "a": "Yes, and they increasingly do. Major insurers including UnitedHealthcare, Cigna, and Humana use AI and algorithmic tools to process prior authorization requests and claims. A 2023 STAT News investigation found that one UnitedHealthcare AI tool was used to deny claims with an override rate of less than 1%, spending an average of 1.2 seconds per case. CMS now requires that AI-driven denials include the specific clinical reason and your right to appeal to a human reviewer.",
        },
        {
            "q": "Do I have the right to a human review of an AI denial?",
            "a": "Yes. Under both CMS rules (for Medicare Advantage and ACA marketplace plans) and most state laws, you have the right to appeal any claim denial to a human reviewer, regardless of whether the initial decision was made by AI. The 2024 CMS final rule specifically requires that Medicare Advantage plans ensure adverse benefit determinations involve physician review. Several states have passed laws requiring human review of AI-driven denials.",
        },
        {
            "q": "Which states have laws regulating AI in healthcare decisions?",
            "a": "As of 2026, California (SB 1120), Colorado (SB 24-205), Illinois, New York, and several other states have enacted laws restricting how insurers can use AI for claims and prior authorization decisions. California's law prohibits insurers from using AI as the sole basis for denying claims and requires disclosure when AI is used. Colorado requires algorithmic impact assessments. More states are expected to pass similar legislation in 2026-2027.",
        },
        {
            "q": "How do I appeal an AI-driven claim denial?",
            "a": "The appeal process is the same as any denial: request the denial in writing with the specific reason code, file an internal appeal within 180 days, include a letter of medical necessity from your treating physician, and request external review if the internal appeal fails. The key difference is to explicitly state in your appeal that you are requesting human clinical review and ask whether the original denial was made by an automated system or algorithm.",
        },
        {
            "q": "Can AI be used to determine my prior authorization?",
            "a": "Yes, and it is one of the most common uses of AI in healthcare billing. Insurers use AI to auto-approve or auto-deny prior authorization requests based on clinical criteria. The 2024 CMS Interoperability and Prior Authorization final rule requires insurers to respond to prior auth requests within 72 hours for urgent cases and 7 days for standard cases, and to provide specific denial reasons. If denied, you have the right to appeal for human physician review.",
        },
    ],
    "body": f"""
<p class="lead">Artificial intelligence is now embedded in nearly every stage of the healthcare billing process. Insurers use AI to approve or deny prior authorizations in seconds. Hospitals deploy algorithms to estimate bills and assign risk scores. Medicare Advantage plans use predictive models to flag claims for denial. A 2023 STAT News investigation found one insurer&rsquo;s AI tool spent an average of <strong>1.2 seconds per case</strong> before denying coverage. The result: patients face denials made by machines, often without knowing an algorithm was involved. This guide explains how AI is used in healthcare decisions, what your rights are, and how to fight back when an algorithm denies your care.</p>

<nav class="toc">
    <h2>In this guide</h2>
    <ol>
        <li><a href="#how-ai-used">How AI is used in healthcare billing decisions</a></li>
        <li><a href="#prior-auth">AI and prior authorization denials</a></li>
        <li><a href="#cms-rules">CMS rules on AI in healthcare (2024&ndash;2026)</a></li>
        <li><a href="#patient-rights">Your rights when AI makes the decision</a></li>
        <li><a href="#state-laws">State laws regulating AI in healthcare</a></li>
        <li><a href="#appeal-ai-denial">How to appeal an AI-driven denial</a></li>
        <li><a href="#sources">Sources</a></li>
    </ol>
</nav>

<h2 id="how-ai-used">1. How AI is used in healthcare billing decisions</h2>

<p>AI and algorithmic decision-making tools are now used across the healthcare billing lifecycle. Understanding where they appear helps you know when to push back.</p>

<h3>Prior authorization automation</h3>

<p>Insurers use AI to review prior authorization requests against clinical criteria databases. The algorithm compares your diagnosis, treatment plan, and medical history to the insurer&rsquo;s coverage guidelines and issues an approval or denial&mdash;often without a human physician reviewing the case. CMS data shows that Medicare Advantage plans denied <strong>13% of prior authorization requests</strong> in 2022, with many processed by automated systems.</p>

<h3>Claims adjudication</h3>

<p>When your provider submits a claim, AI systems check it against coding rules, medical necessity criteria, and fraud detection models. Claims flagged by the algorithm may be denied automatically or routed for manual review. The speed of processing means errors in the AI&rsquo;s logic can affect thousands of patients simultaneously.</p>

<h3>Predictive denial models</h3>

<p>Some insurers use predictive models to identify claims that are likely to be accepted without appeal even if denied. A 2023 investigation revealed that one major insurer&rsquo;s AI tool had a <strong>90% denial override rate</strong>&mdash;meaning the AI denied claims it predicted patients would not bother to appeal.</p>

<h3>Hospital billing estimation</h3>

<p>Hospitals use AI to generate cost estimates, assign billing codes, and predict patient payment likelihood. While these tools can improve accuracy, they can also systematically upcode services or overestimate costs when miscalibrated.</p>

<div class="key-takeaway">
    <strong>The fundamental problem:</strong> AI in healthcare billing creates an asymmetry. Insurers can deny thousands of claims per hour at near-zero cost. Each patient must individually appeal, gathering documentation and navigating a complex process. The economics incentivize AI denial because most patients never appeal. <a href="/guides/how-to-appeal-insurance-denial-and-win">Fewer than 1% of denied claims are appealed</a>, yet 44&ndash;80% of appeals succeed.
</div>

<h2 id="prior-auth">2. AI and prior authorization denials</h2>

<p>Prior authorization&mdash;the requirement that your insurer approve a treatment before you receive it&mdash;is the area where AI has the greatest impact on patient care and costs.</p>

<table>
    <thead>
        <tr><th>Metric</th><th>Data</th><th>Source</th></tr>
    </thead>
    <tbody>
        <tr><td>Prior auth requests per year (Medicare Advantage)</td><td>35 million+</td><td>CMS (2023)</td></tr>
        <tr><td>Denial rate (Medicare Advantage prior auth)</td><td>13%</td><td>OIG (2022)</td></tr>
        <tr><td>Denials overturned on appeal</td><td>75% of appealed denials</td><td>OIG (2022)</td></tr>
        <tr><td>Percentage of denials actually appealed</td><td>&lt;1%</td><td>KFF (2023)</td></tr>
        <tr><td>Average AI review time per case</td><td>1.2 seconds</td><td>STAT News (2023)</td></tr>
    </tbody>
</table>

<p>The OIG found that Medicare Advantage plans sometimes deny care that <strong>would have been covered under traditional Medicare</strong>. This is particularly problematic when AI tools apply stricter criteria than Medicare&rsquo;s actual coverage rules. If your MA plan denied a prior authorization, check whether the service would be covered under traditional Medicare&mdash;if so, that strengthens your appeal.</p>

<div class="case-study">
    <h3>Example: AI denies rehabilitation stay after 1.2-second review</h3>
    <p>A 72-year-old Medicare Advantage enrollee was admitted to inpatient rehabilitation after a hip replacement. After 7 days, the insurer&rsquo;s AI system flagged the stay as &ldquo;no longer medically necessary&rdquo; and issued a denial. The patient&rsquo;s treating physician had documented ongoing inability to walk independently and need for continued physical therapy.</p>
    <p>The patient filed an internal appeal with the physician&rsquo;s detailed letter of medical necessity. The denial was overturned in 5 days and the rehab stay was extended by 14 days. <strong>Without the appeal, the patient would have owed approximately $18,000 for the denied days.</strong></p>
</div>

<h2 id="cms-rules">3. CMS rules on AI in healthcare (2024&ndash;2026)</h2>

<p>The Centers for Medicare &amp; Medicaid Services has taken significant steps to regulate AI in healthcare decisions:</p>

<h3>2024 Medicare Advantage final rule</h3>

<p>CMS finalized rules requiring Medicare Advantage plans to:</p>

<ul>
    <li>Ensure that coverage decisions are based on the <strong>individual patient&rsquo;s circumstances</strong>, not solely on algorithmic predictions</li>
    <li>Require that <strong>adverse benefit determinations involve review by a physician or other appropriate healthcare professional</strong></li>
    <li>Base coverage criteria on <strong>traditional Medicare coverage rules</strong>&mdash;MA plans cannot use stricter criteria than original Medicare</li>
    <li>Provide <strong>specific clinical reasons</strong> for any denial, not just generic denial codes</li>
</ul>

<h3>2024 Interoperability and Prior Authorization final rule</h3>

<p>This rule requires insurers (including MA plans, Medicaid, and ACA marketplace plans) to:</p>

<ul>
    <li>Respond to prior authorization requests within <strong>72 hours for urgent cases</strong> and <strong>7 calendar days for standard requests</strong></li>
    <li>Provide the <strong>specific reason</strong> for any denial, including the clinical criteria used</li>
    <li>Make prior authorization data available through standardized APIs for transparency</li>
</ul>

<h3>2025&ndash;2026 enforcement actions</h3>

<p>CMS has increased enforcement against MA plans that use AI to systematically deny medically necessary care. In 2025, CMS issued civil money penalties to several MA plans for inappropriate prior authorization denials and launched audits specifically targeting AI-driven denial patterns.</p>

<div class="key-takeaway">
    <strong>What this means for you:</strong> If your Medicare Advantage plan uses AI to deny your claim, the denial must still meet the same coverage criteria as traditional Medicare. If the service would be covered under original Medicare, your MA plan cannot deny it based on stricter algorithmic criteria. Reference the 2024 CMS final rule in your appeal.
</div>

<h2 id="patient-rights">4. Your rights when AI makes the decision</h2>

<p>Regardless of whether an AI or a human made the initial denial decision, you have the same appeal rights:</p>

<p><strong>Right to know the reason.</strong> Your insurer must provide the <strong>specific clinical reason</strong> for any denial in writing. Generic reasons like &ldquo;not medically necessary&rdquo; without further explanation violate CMS rules for Medicare and most state laws for commercial insurance.</p>

<p><strong>Right to human review.</strong> You have the right to have your appeal reviewed by a qualified <strong>human physician or healthcare professional</strong>. Under the 2024 CMS rule, this is required for Medicare Advantage. Most states require it for commercial insurance as well. Explicitly request human clinical review in your appeal letter.</p>

<p><strong>Right to your medical records.</strong> You are entitled to copies of all medical records used in the coverage decision, including any algorithmic output or clinical criteria the AI applied. Request these under your <a href="/guides/medical-records-rights">medical records rights</a>.</p>

<p><strong>Right to external review.</strong> If your internal appeal fails, you have the right to an independent external review by a reviewer who does not work for your insurer. The external reviewer&rsquo;s decision is <strong>legally binding</strong> on the insurer. About 40&ndash;45% of external reviews overturn the denial.</p>

<p><strong>Right to know if AI was used.</strong> In states with AI transparency laws (see Section 5), you have the right to know whether an automated system was involved in your coverage decision. Even in states without such laws, you can ask your insurer directly: &ldquo;Was an algorithm, automated system, or artificial intelligence tool used in making this coverage determination?&rdquo;</p>

<h2 id="state-laws">5. State laws regulating AI in healthcare</h2>

<p>States are moving faster than the federal government to regulate AI in healthcare decisions:</p>

<table>
    <thead>
        <tr><th>State</th><th>Law</th><th>Key Provisions</th></tr>
    </thead>
    <tbody>
        <tr><td>California</td><td>SB 1120 (2024)</td><td>Prohibits insurers from using AI as the <strong>sole basis</strong> for claim denials. Requires disclosure when AI is used. Mandates human physician review for any AI-generated denial.</td></tr>
        <tr><td>Colorado</td><td>SB 24-205 (2024)</td><td>Requires <strong>algorithmic impact assessments</strong> for AI tools used in insurance decisions. Consumers have the right to appeal algorithmic decisions to a human.</td></tr>
        <tr><td>New York</td><td>A.7865 (2025)</td><td>Requires insurers to disclose use of AI in utilization review. Mandates that AI tools meet <strong>accuracy and fairness standards</strong> reviewed by the state insurance department.</td></tr>
        <tr><td>Illinois</td><td>HB 3773 (2025)</td><td>Prohibits AI-only denials for prior authorization. Requires <strong>licensed physician review</strong> of any denial for inpatient or surgical services.</td></tr>
        <tr><td>Washington</td><td>SB 5462 (2025)</td><td>Requires transparency reporting on AI denial rates. Insurers must report to the state insurance commissioner the percentage of claims processed by AI and the denial rate comparison between AI and human reviewers.</td></tr>
    </tbody>
</table>

<div class="key-takeaway">
    <strong>Check your state:</strong> If you live in a state with AI healthcare laws, reference the specific statute in your appeal letter. Stating that you are invoking your right to human review under [state law] adds legal weight to your appeal and signals that you know your rights.
</div>

<h2 id="appeal-ai-denial">6. How to appeal an AI-driven denial</h2>

<p>The appeal process for an AI-driven denial follows the same structure as any claim denial, with a few additional strategies:</p>

<h3>Step 1: Get the denial in writing with specific reasons</h3>

<p>Request the written denial notice. It must include the specific clinical criteria used and the reason your case did not meet those criteria. If the denial letter is vague, call and request the detailed clinical rationale in writing. CMS requires specific reasons for Medicare Advantage denials.</p>

<h3>Step 2: Ask whether AI was involved</h3>

<p>In your appeal, include this question: &ldquo;Please confirm whether an algorithm, automated system, or artificial intelligence tool was used in whole or in part to make this coverage determination.&rdquo; In states with AI transparency laws, insurers are required to disclose this. Even in other states, asking puts it on the record.</p>

<h3>Step 3: Get a letter of medical necessity</h3>

<p>Ask your treating physician to write a detailed letter explaining why the denied service is medically necessary for your specific condition. AI tools often apply population-level criteria; your physician&rsquo;s letter provides the individual clinical context that the algorithm missed.</p>

<h3>Step 4: Request human physician review</h3>

<p>Explicitly state in your appeal: &ldquo;I request that this appeal be reviewed by a board-certified physician in the relevant specialty, as required by [CMS rules / state law].&rdquo; This is your right under both federal and most state law.</p>

<h3>Step 5: Reference clinical guidelines</h3>

<p>Include any peer-reviewed clinical guidelines, medical society recommendations (AMA, specialty societies), or Medicare coverage determinations that support the medical necessity of your service. AI tools are trained on specific criteria sets; showing that accepted medical standards support your care undermines the AI&rsquo;s denial logic.</p>

<h3>Step 6: Pursue external review if needed</h3>

<p>If the internal appeal fails, request external review. An independent reviewer will evaluate your case fresh&mdash;without the insurer&rsquo;s AI system involved. External review decisions are binding on the insurer. See our <a href="/guides/how-to-appeal-insurance-denial-and-win">complete guide to winning insurance appeals</a> for detailed templates.</p>

<div class="case-study">
    <h3>Example: Patient overturns AI-driven prior auth denial for MRI</h3>
    <p>A 45-year-old patient with persistent shoulder pain was referred for an MRI by her orthopedist. Her commercial insurer&rsquo;s AI system denied the prior authorization, stating she had not completed the required 6 weeks of physical therapy first. In fact, she had completed 8 weeks of PT with documented worsening symptoms.</p>
    <p>Her physician wrote a letter of medical necessity attaching the PT records. The patient filed an appeal explicitly requesting human physician review and noting that the AI system appeared to have failed to account for the completed PT documentation. The denial was overturned in 4 business days.</p>
    <p><strong>Without the appeal, the patient would have paid $3,200 out of pocket for the MRI.</strong></p>
</div>

<div class="key-takeaway">
    <strong>AI denials depend on patients not appealing.</strong> The economics only work for insurers if the vast majority of patients accept the denial. When you appeal with proper documentation and request human review, you shift the advantage back to your side. <a href="/scan">Scan your denied bill with BillKarma</a> to identify the specific codes and amounts at stake before you file your appeal.
</div>

<h2 id="sources">Sources</h2>

<ul class="sources-list">
    <li><a href="https://www.cms.gov/newsroom/fact-sheets/2024-medicare-advantage-and-part-d-final-rule-cms-4201-f" target="_blank" rel="noopener">CMS: 2024 Medicare Advantage and Part D Final Rule (CMS-4201-F)</a></li>
    <li><a href="https://oig.hhs.gov/oei/reports/OEI-09-18-00260.asp" target="_blank" rel="noopener">HHS OIG: Medicare Advantage Prior Authorization Denials Report</a></li>
    <li><a href="https://www.cms.gov/newsroom/fact-sheets/cms-interoperability-and-prior-authorization-final-rule-cms-0057-f" target="_blank" rel="noopener">CMS: Interoperability and Prior Authorization Final Rule (CMS-0057-F)</a></li>
    <li><a href="https://www.ama-assn.org/practice-management/prior-authorization" target="_blank" rel="noopener">AMA: Prior Authorization and Utilization Management Reform</a></li>
    <li><a href="https://leginfo.legislature.ca.gov/faces/billNavClient.xhtml?bill_id=202320240SB1120" target="_blank" rel="noopener">California SB 1120: Health Insurance AI Regulation</a></li>
    <li><a href="https://leg.colorado.gov/bills/sb24-205" target="_blank" rel="noopener">Colorado SB 24-205: Algorithmic Impact Assessments in Insurance</a></li>
</ul>
""",
})
