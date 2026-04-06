"""Guide: How to Appeal a Denied Insurance Claim (And Why You'll Probably Win)."""

from guides import register, _embed

register("how-to-appeal-insurance-denial-and-win", {
    "title": "How to Appeal a Denied Insurance Claim (And Win) (2026)",
    "meta_description": "Under 1% of denied claims are appealed, yet 44-80% of appeals succeed. Learn the step-by-step process to write a winning appeal letter.",
    "published": "2026-02-27",
    "author": "BillKarma Team",
    "category": "Insurance Basics",
    "faqs": [
        {
            "q": "What percentage of insurance claim appeals actually succeed?",
            "a": "Between 44% and 80% of appealed insurance claim denials are overturned, depending on the plan type and denial reason. KFF data shows ACA marketplace plans overturn about 44% of internal appeals. State insurance department data and Department of Labor reports show success rates up to 80% for certain denial types, particularly coding errors and prior authorization denials. The odds are strongly in your favor.",
        },
        {
            "q": "How long do I have to appeal a denied insurance claim?",
            "a": "Most insurance plans give you 180 days (about 6 months) from the date of the denial notice to file an internal appeal. For external reviews, you typically have 4 months after exhausting internal appeals. For urgent care situations, you can request an expedited appeal that must be decided within 72 hours. Check your denial letter for the exact deadline, as some plans allow less time.",
        },
        {
            "q": "Does it cost anything to file an insurance appeal?",
            "a": "No. Filing an internal appeal and requesting an external review are both completely free under federal law. Insurance companies are required to provide a fair appeals process at no cost to you. You may choose to hire a medical billing advocate or patient advocate for help, but this is optional and not required to file a successful appeal.",
        },
        {
            "q": "What is an external review and why is it so powerful?",
            "a": "An external review is an independent evaluation of your denied claim by a reviewer who does not work for your insurance company. It is available after you exhaust internal appeals. The external reviewer's decision is legally binding, meaning your insurer must comply if the reviewer overturns the denial. About 40-45% of external reviews result in the denial being overturned. It is free to request.",
        },
        {
            "q": "Can I appeal a claim that was denied months ago?",
            "a": "Yes, as long as you are within the appeal deadline stated on your denial notice. Most plans allow 180 days from the denial date. Even if you have already paid the bill, you can still appeal. If your appeal succeeds, your insurer will reimburse you or pay the provider, who must then refund your payment. Keep all receipts and proof of payment.",
        },
        {
            "q": "What should I include in an appeal letter to maximize my chances of winning?",
            "a": "Include your claim number, the specific denial reason and code, a clear explanation of why the denial should be overturned, a letter of medical necessity from your treating physician, relevant medical records and test results, documentation of prior treatments tried, and any peer-reviewed clinical guidelines supporting the service. Keep the tone factual and professional. Attach everything rather than making the reviewer search for information.",
        },
    ],
    "body": f"""
<p class="lead">Your insurance denied your claim. Most people just pay the bill or give up. But here&rsquo;s what the insurance industry doesn&rsquo;t want you to know: <strong>fewer than 1% of denied claims are appealed</strong>, yet when patients DO appeal, they win <strong>44&ndash;80% of the time</strong>. Among ACA marketplace plans, only 0.1% of denied claims are appealed&mdash;a staggeringly low number given the success rates. A 2024 KFF poll found that 55% of Americans say regulating insurer claim decisions should be a &ldquo;top priority.&rdquo; The math is overwhelmingly in your favor. This guide shows you exactly how to appeal, step by step, so you can join the small percentage of patients who fight back&mdash;and win.</p>

<div class="answer-box"><strong>Quick answer</strong>Request the denial reason in writing (insurers must provide it), then file an internal appeal within 180 days citing medical necessity. If denied again, request an external review — an independent reviewer overturns 40% of appeals. It costs you nothing.</div>

<nav class="toc">
    <h2>In this guide</h2>
    <ol>
        <li><a href="#why-denied">Why claims get denied &mdash; the top 10 reasons</a></li>
        <li><a href="#success-rates">The appeal success rates nobody talks about</a></li>
        <li><a href="#appeal-rights">Understanding your appeal rights</a></li>
        <li><a href="#three-level-process">The 3-level appeal process</a></li>
        <li><a href="#winning-letter">How to write a winning appeal letter</a></li>
        <li><a href="#expedited-appeals">Expedited appeals for urgent care</a></li>
        <li><a href="#real-wins">5 real appeal wins</a></li>
        <li><a href="#when-to-escalate">When to escalate beyond appeals</a></li>
        <li><a href="#faq">Frequently asked questions</a></li>
        <li><a href="#sources">Sources</a></li>
    </ol>
</nav>

<h2 id="why-denied">1. Why claims get denied &mdash; the top 10 reasons</h2>

<p>Understanding why your claim was denied is the first step to overturning it. Not all denials are created equal&mdash;some are simple paperwork errors that can be fixed with a phone call, while others require a formal appeal with clinical evidence. Here are the 10 most common denial reasons, ranked by frequency:</p>

<table>
    <thead>
        <tr><th>#</th><th>Denial Reason</th><th>How Common</th><th>Typical Fix</th></tr>
    </thead>
    <tbody>
        <tr><td>1</td><td>Prior authorization not obtained</td><td>Most common (~25% of denials)</td><td>Retroactive auth request or appeal with clinical documentation</td></tr>
        <tr><td>2</td><td>Out-of-network provider</td><td>~15&ndash;20%</td><td>Check if <a href="/guides/no-surprises-act-explained">No Surprises Act</a> applies; appeal citing lack of in-network availability</td></tr>
        <tr><td>3</td><td>Service deemed not medically necessary</td><td>~15&ndash;20%</td><td>Letter of medical necessity from treating physician + clinical guidelines</td></tr>
        <tr><td>4</td><td>Coding error (wrong CPT/ICD-10 code)</td><td>~10&ndash;15%</td><td>Correct code resubmission &mdash; <a href="/scan">upload your bill to check for coding errors</a></td></tr>
        <tr><td>5</td><td>Timely filing limit exceeded</td><td>~8&ndash;10%</td><td>Provider-side issue; demand provider refile or absorb the cost</td></tr>
        <tr><td>6</td><td>Pre-existing condition exclusion</td><td>Rare post-ACA (&lt;2%)</td><td>Cite ACA protections &mdash; most exclusions are illegal since 2014</td></tr>
        <tr><td>7</td><td>Duplicate claim submitted</td><td>~5%</td><td>Administrative correction; call the billing department</td></tr>
        <tr><td>8</td><td>Experimental or investigational treatment</td><td>~3&ndash;5%</td><td>Peer-reviewed evidence + external review (high success rate)</td></tr>
        <tr><td>9</td><td>Missing or incomplete information</td><td>~5%</td><td>Resubmit with complete documentation</td></tr>
        <tr><td>10</td><td>Maximum benefit or visit limit exceeded</td><td>~2&ndash;3%</td><td>Appeal citing medical necessity for continued treatment</td></tr>
    </tbody>
</table>

<div class="key-takeaway">
    <strong>Before you appeal, check the codes.</strong> Many denials stem from coding errors that are invisible to patients. <a href="/scan">Upload your denied bill to BillKarma</a> to check for CPT/ICD-10 coding errors that may have caused the denial&mdash;a corrected code resubmission has an 80%+ success rate and often doesn&rsquo;t even require a formal appeal.
</div>

<p>Check what Medicare pays for the denied service. This gives you a concrete benchmark to reference in your appeal and shows whether the charge itself is reasonable:</p>

{_embed(mode="cost", title="Look up your denied service", subtitle="Enter the CPT code from your denial notice to see the Medicare rate.")}

<h2 id="success-rates">2. The appeal success rates nobody talks about</h2>

<p>Insurance companies count on patients accepting denials without question. The data shows why that&rsquo;s a mistake:</p>

<table>
    <thead>
        <tr><th>Data Source</th><th>Plan Type</th><th>Appeal Success Rate</th><th>Key Finding</th></tr>
    </thead>
    <tbody>
        <tr><td>KFF (2023 data)</td><td>ACA marketplace plans</td><td>44% of internal appeals overturned</td><td>Only 0.1% of denied claims are ever appealed</td></tr>
        <tr><td>HHS OIG (2022)</td><td>Medicare Advantage</td><td>75% of appealed PA denials overturned</td><td>13% of initial PA denials were for services that met Medicare coverage rules</td></tr>
        <tr><td>Department of Labor</td><td>Employer-sponsored (ERISA) plans</td><td>50&ndash;60% of internal appeals succeed</td><td>External review overturns another 40% of remaining denials</td></tr>
        <tr><td>State insurance departments</td><td>Fully insured commercial plans</td><td>40&ndash;80% depending on state and denial type</td><td>External review decisions are binding on the insurer</td></tr>
        <tr><td>CMS external review data</td><td>All plan types combined</td><td>~40&ndash;45% of external reviews overturn denial</td><td>Patients win nearly half the time even after losing internal appeals</td></tr>
    </tbody>
</table>

<p><strong>What this means in practice:</strong> If your claim was denied and the service cost $5,000, the expected value of filing a free appeal is between $2,200 and $4,000 (44&ndash;80% &times; $5,000). Filing takes an afternoon of work. Not filing guarantees you pay the full amount.</p>

<p>Success rates vary by denial type. Some denials are much easier to overturn than others:</p>

<table>
    <thead>
        <tr><th>Denial Type</th><th>Estimated Appeal Success Rate</th><th>Why</th></tr>
    </thead>
    <tbody>
        <tr><td>Coding error</td><td>~80%</td><td>Clear-cut fix once the correct code is submitted</td></tr>
        <tr><td><a href="/guides/prior-authorization">Prior authorization</a> not obtained</td><td>~60%</td><td>Often an administrative failure, not a clinical judgment</td></tr>
        <tr><td>Not medically necessary</td><td>~50%</td><td>Strong physician letter + clinical guidelines tip the scales</td></tr>
        <tr><td>Out-of-network provider</td><td>~35&ndash;50%</td><td>Depends on whether emergency or NSA protections apply</td></tr>
        <tr><td>Experimental/investigational</td><td>~40%</td><td>External review is especially effective for these</td></tr>
        <tr><td>Service not covered by plan</td><td>~20%</td><td>Hardest to overturn; may require external review or regulatory complaint</td></tr>
    </tbody>
</table>

<div class="key-takeaway">
    <strong>The bottom line:</strong> The appeal process is free. The worst outcome is the same &ldquo;no&rdquo; you already have. And the best outcome is saving hundreds to tens of thousands of dollars. If your denied claim is worth more than $200, appeal it. Every time.
</div>

<h2 id="appeal-rights">3. Understanding your appeal rights</h2>

<p>Federal law (the Affordable Care Act) guarantees your right to appeal any insurance denial. But the specific process and protections depend on your plan type. Here&rsquo;s what you need to know:</p>

<h3>Internal appeals</h3>

<p>Every health insurance plan must offer at least one level of internal appeal, where a different reviewer at the insurance company (not the person who made the original denial) re-examines your claim. Most plans offer two levels of internal appeal before external review.</p>

<ul>
    <li><strong>Deadline to file:</strong> Typically 180 days from the denial notice date</li>
    <li><strong>Insurer&rsquo;s response time:</strong> 30 days for non-urgent claims; 72 hours for urgent claims</li>
    <li><strong>Your right to submit new evidence:</strong> You can (and should) submit additional documentation not included in the original claim</li>
    <li><strong>Your right to see the insurer&rsquo;s criteria:</strong> You can request the specific clinical criteria or guidelines the insurer used to deny your claim</li>
</ul>

<h3>External review</h3>

<p>After exhausting internal appeals, you have the right to an <strong>external review</strong>&mdash;an independent evaluation by a reviewer who does not work for your insurer. This is one of the most powerful patient protections in healthcare, and most people don&rsquo;t know it exists.</p>

<ul>
    <li><strong>Who reviews:</strong> An independent physician or clinical expert in the relevant specialty, hired by an independent review organization (IRO)</li>
    <li><strong>Binding decision:</strong> If the external reviewer overturns your denial, the insurer <strong>must comply</strong>. They cannot appeal.</li>
    <li><strong>Cost:</strong> Free to you</li>
    <li><strong>Deadline:</strong> 4 months after your final internal appeal denial</li>
    <li><strong>Response time:</strong> 45 days standard; 72 hours for urgent cases</li>
</ul>

<h3>ERISA plans vs. fully insured plans</h3>

<p>Your appeal process differs based on how your employer&rsquo;s plan is funded:</p>

<table>
    <thead>
        <tr><th>Plan Type</th><th>How to Identify</th><th>Appeal Process</th><th>Regulatory Body</th></tr>
    </thead>
    <tbody>
        <tr><td><strong>Fully insured</strong> (insurance company bears the risk)</td><td>Small employers, ACA marketplace plans, individual plans</td><td>State-regulated; external review through state insurance department</td><td>State insurance commissioner</td></tr>
        <tr><td><strong>Self-funded / ERISA</strong> (employer bears the risk)</td><td>Most large employers (500+ employees)</td><td>Federally regulated; external review through HHS-designated IRO</td><td>U.S. Department of Labor (DOL)</td></tr>
    </tbody>
</table>

<p>To find out which type you have, check your plan documents or call your HR department. The appeals process is similar for both, but the regulatory bodies you escalate to differ.</p>

<h3>State insurance department complaints</h3>

<p>Regardless of plan type, you can file a complaint with your <a href="https://www.naic.org/state_web_map.htm" target="_blank" rel="noopener">state insurance department</a>. State regulators investigate complaints and can pressure insurers to reverse decisions. This is a powerful tool, especially when combined with a formal appeal.</p>

<h2 id="three-level-process">4. The 3-level appeal process</h2>

<p>Here is the full appeal process, level by level, with exact timelines and what to expect at each stage:</p>

<h3>Level 1: First internal appeal</h3>

<table>
    <thead>
        <tr><th>Detail</th><th>What to Know</th></tr>
    </thead>
    <tbody>
        <tr><td><strong>Deadline to file</strong></td><td>180 days from denial notice (check your letter for exact date)</td></tr>
        <tr><td><strong>Who reviews</strong></td><td>A different reviewer at your insurance company (not the original decision-maker)</td></tr>
        <tr><td><strong>Insurer&rsquo;s response time</strong></td><td>30 days for non-urgent; 72 hours for urgent</td></tr>
        <tr><td><strong>How to file</strong></td><td>Written letter to insurer&rsquo;s appeals department (address on denial notice), or online portal</td></tr>
        <tr><td><strong>What to include</strong></td><td>Appeal letter, letter of medical necessity, medical records, peer-reviewed guidelines</td></tr>
        <tr><td><strong>Success rate</strong></td><td>44&ndash;60% depending on plan type</td></tr>
    </tbody>
</table>

<p><strong>Steps:</strong></p>
<ol>
    <li>Note the deadline from your denial letter. Mark it on your calendar immediately.</li>
    <li>Call the appeals department (number on the denial notice) and ask: What is the exact reason? What clinical criteria were used? What documentation would help overturn this?</li>
    <li>Contact your doctor&rsquo;s office and request a letter of medical necessity, clinical notes, and any peer-reviewed evidence supporting the service.</li>
    <li>Write your appeal letter (see Section 5 below).</li>
    <li>Submit via certified mail, insurer portal, or fax with confirmation page. Keep copies of everything.</li>
    <li>Follow up 5&ndash;7 business days after submission to confirm receipt.</li>
</ol>

<h3>Level 2: Second internal appeal (if applicable)</h3>

<p>Some plans offer a second level of internal review, typically by a senior medical director. If your Level 1 appeal is denied, your denial notice will indicate whether a second internal appeal is available. Use this level to submit any new documentation gathered since Level 1&mdash;updated test results, additional specialist opinions, or new clinical guidelines.</p>

<p><strong>Timeline:</strong> Same as Level 1 (30 days non-urgent, 72 hours urgent).</p>

<h3>Level 3: External review (independent, binding)</h3>

<p>This is your most powerful tool. After exhausting internal appeals, you can request an external review. An independent physician or specialist who does not work for your insurer examines your case from scratch.</p>

<table>
    <thead>
        <tr><th>Detail</th><th>What to Know</th></tr>
    </thead>
    <tbody>
        <tr><td><strong>Deadline to request</strong></td><td>4 months after final internal appeal denial</td></tr>
        <tr><td><strong>Who reviews</strong></td><td>Independent physician/specialist assigned by state or federal IRO</td></tr>
        <tr><td><strong>Response time</strong></td><td>45 days standard; 72 hours for urgent cases</td></tr>
        <tr><td><strong>Decision is binding</strong></td><td>Yes &mdash; the insurer MUST comply if the reviewer overturns the denial</td></tr>
        <tr><td><strong>Cost to you</strong></td><td>Free</td></tr>
        <tr><td><strong>Success rate</strong></td><td>~40&ndash;45%</td></tr>
    </tbody>
</table>

<p><strong>When external review is especially effective:</strong></p>
<ul>
    <li>&ldquo;Not medically necessary&rdquo; denials where your treating physician strongly supports the service</li>
    <li>Experimental or investigational treatment denials backed by peer-reviewed literature</li>
    <li>Denials based on the insurer&rsquo;s proprietary guidelines that conflict with widely accepted clinical standards</li>
    <li>Cases where the internal reviewers did not have the relevant specialty expertise</li>
</ul>

<div class="key-takeaway">
    <strong>Don&rsquo;t stop at Level 1.</strong> Even if your first appeal is denied, the external review gives you a nearly 50/50 shot at overturning it. When you combine the success rates: if you have a 50% chance at Level 1 and a 40% chance at Level 3, your cumulative probability of winning at some point in the process is approximately 70%. The math favors persistence.
</div>

<h2 id="winning-letter">5. How to write a winning appeal letter</h2>

<p>Your appeal letter is the most important document in the process. It should be clear, specific, factual, and organized. Here is the structure that works:</p>

<h3>What to include</h3>

<ol>
    <li><strong>Your identifying information</strong> &mdash; Name, member ID, claim number, date of service, denied service (CPT code and description)</li>
    <li><strong>The denial reason</strong> &mdash; Quote the denial code and reason directly from your denial notice. Show you understand what they said.</li>
    <li><strong>Why the denial is wrong</strong> &mdash; Address the specific reason head-on with facts and evidence.</li>
    <li><strong>Clinical evidence</strong> &mdash; Letter of medical necessity from your treating physician, medical records (office notes, test results, imaging), documentation of prior treatments tried and failed</li>
    <li><strong>Peer-reviewed support</strong> &mdash; Clinical guidelines from recognized organizations (ACR, AAOS, APA, NCCN) and peer-reviewed studies supporting the treatment</li>
    <li><strong>Specific request</strong> &mdash; State exactly what you want: &ldquo;I respectfully request that you reverse the denial and authorize coverage for [service].&rdquo;</li>
</ol>

<h3>What NOT to include</h3>

<ul>
    <li>Emotional appeals or personal hardship stories (save these for escalation to regulators, not clinical reviewers)</li>
    <li>Threats of lawsuits (this doesn&rsquo;t help at the appeal stage)</li>
    <li>General complaints about the insurance company</li>
    <li>Irrelevant medical history that doesn&rsquo;t relate to the denied service</li>
</ul>

<h3>Sample appeal letter template</h3>

<div class="case-study">
    <h3>Appeal letter &mdash; &ldquo;not medically necessary&rdquo; denial</h3>
    <p><em>[Your Name]<br>[Your Address]<br>[City, State, ZIP]<br>[Date]</em></p>
    <p><em>[Insurance Company] Appeals Department<br>[Address from denial notice]</em></p>
    <p><strong>RE: Appeal of Claim Denial<br>Member ID: [YOUR MEMBER ID]<br>Claim Number: [CLAIM NUMBER]<br>Date of Service: [DATE]<br>Denied Service: [SERVICE DESCRIPTION] (CPT [CODE])<br>Denial Reason: [REASON AND CODE FROM DENIAL NOTICE]</strong></p>
    <p>Dear Appeals Department,</p>
    <p>I am writing to appeal the denial of claim [CLAIM NUMBER] for [service description] (CPT [code]) performed on [date]. The claim was denied as &ldquo;[denial reason]&rdquo; (denial code [code]). I believe this denial should be overturned based on the following clinical evidence.</p>
    <p><strong>Clinical history:</strong> [2&ndash;3 sentences describing your condition, when symptoms began, and what you&rsquo;ve already tried. Be specific: dates, number of visits, specific treatments.]</p>
    <p><strong>Why this service is medically necessary:</strong> [2&ndash;3 sentences directly addressing the denial reason. Cite clinical guidelines by name. Reference your doctor&rsquo;s letter of medical necessity. Explain why the denied service is the appropriate next step given your treatment history.]</p>
    <p><strong>Enclosed documentation:</strong></p>
    <ol>
        <li>Letter of medical necessity from Dr. [NAME], [specialty]</li>
        <li>Office visit notes from [DATES]</li>
        <li>[Other treatment records: physical therapy notes, lab results, imaging, etc.]</li>
        <li>[Peer-reviewed guidelines or studies, if applicable]</li>
    </ol>
    <p>I respectfully request that you reverse the denial of this claim and authorize coverage for [service]. Please contact me at [phone] or [email] if you need additional information.</p>
    <p><em>Sincerely,<br>[Your Name]</em></p>
</div>

<p><strong>Tips for a strong appeal:</strong></p>
<ul>
    <li>Reference the specific denial code and reason &mdash; show you understand exactly why it was denied</li>
    <li>Include concrete facts: dates, number of therapy sessions, specific test results, failed medications</li>
    <li>Cite clinical guidelines by name (ACR Appropriateness Criteria, NCCN Guidelines, AAOS Clinical Practice Guidelines)</li>
    <li>Attach every supporting document &mdash; do not make the reviewer search for information</li>
    <li>Keep the tone professional and factual, never confrontational</li>
    <li>Have your doctor co-sign the appeal or submit a separate supporting letter</li>
</ul>

<div class="key-takeaway">
    <strong>Coding errors are the easiest wins.</strong> <a href="/scan">Upload your denied bill to BillKarma</a> to check whether a CPT or ICD-10 coding error caused the denial. A corrected code resubmission has the highest success rate of any appeal type and often resolves within days.
</div>

<h2 id="expedited-appeals">6. Expedited appeals for urgent care</h2>

<p>If waiting for the standard 30-day appeal timeline would seriously jeopardize your health, you have the right to an <strong>expedited (urgent) appeal</strong>. The insurer must respond within <strong>72 hours</strong>.</p>

<p><strong>When to request an expedited appeal:</strong></p>
<ul>
    <li>Denial of a service you need immediately to prevent serious harm (e.g., cancer treatment, emergency surgery authorization)</li>
    <li>Insurer is terminating coverage for ongoing treatment mid-course (e.g., ending authorization for a hospital stay while you&rsquo;re still in the hospital)</li>
    <li>Prior authorization denial for a time-sensitive procedure</li>
    <li>Your doctor states in writing that waiting 30 days could seriously worsen your condition</li>
</ul>

<p><strong>How to request:</strong></p>
<ol>
    <li>Call the insurer&rsquo;s appeals department and state: &ldquo;I am requesting an expedited appeal under the ACA. My physician has documented that a standard timeline would jeopardize my health.&rdquo;</li>
    <li>Have your doctor call the insurer directly or fax a statement supporting the urgency.</li>
    <li>You can file an internal appeal and request an external review <strong>simultaneously</strong> for urgent cases &mdash; you do not need to wait for the internal appeal to finish.</li>
    <li>The insurer must respond within 72 hours. If they don&rsquo;t, escalate to your state insurance department immediately.</li>
</ol>

<p><strong>For concurrent review situations</strong> (insurer trying to end authorization during an ongoing hospital stay): You have the right to remain in the hospital while the expedited appeal is processed. The insurer cannot terminate coverage during the appeal without giving you at least 24 hours&rsquo; notice.</p>

<p>For a step-by-step walkthrough of the standard appeal process with additional letter templates, see our companion <a href="/guides/how-to-appeal-insurance-denial">insurance denial appeal guide</a>.</p>

<h2 id="real-wins">7. 5 real appeal wins</h2>

<p>These case studies show the range of denials that get overturned on appeal&mdash;and the dollar amounts at stake.</p>

<div class="case-study">
    <h3>Case 1: Prior authorization denial overturned &mdash; $23,000 surgery</h3>
    <p>A 58-year-old patient was scheduled for a laparoscopic cholecystectomy (gallbladder removal) after repeated gallstone attacks. The surgeon&rsquo;s office submitted a prior authorization request, but the insurer denied it, stating that &ldquo;conservative management has not been exhausted.&rdquo; The patient had already been to the ER twice for acute attacks and had been on a restricted diet for four months with no improvement.</p>
    <p>The surgeon submitted a peer-to-peer appeal with the insurer&rsquo;s medical director, presenting the two ER visits, ultrasound results showing multiple gallstones, and the American College of Surgeons guideline recommending cholecystectomy after recurrent symptomatic gallstones. The medical director reversed the denial on the phone call.</p>
    <p><strong>Billed:</strong> $23,000 &rarr; <strong>Patient owed after insurance:</strong> $1,800 (in-network deductible/coinsurance) &rarr; <strong>Savings: $21,200</strong></p>
</div>

<div class="case-study">
    <h3>Case 2: &ldquo;Not medically necessary&rdquo; MRI reversed &mdash; $8,500</h3>
    <p>A 45-year-old patient was referred for a brain MRI (CPT 70553) after six weeks of persistent headaches, visual disturbances, and a neurological exam showing papilledema. The insurer denied the MRI as &ldquo;not medically necessary,&rdquo; citing its internal guideline that imaging for headaches requires failure of at least 8 weeks of conservative treatment.</p>
    <p>The patient&rsquo;s neurologist wrote a letter of medical necessity explaining that papilledema (swelling of the optic nerve) is a clinical emergency sign that requires immediate imaging to rule out intracranial mass or elevated intracranial pressure. The letter cited the American Academy of Neurology guidelines, which state that imaging is &ldquo;immediately indicated&rdquo; for headaches with abnormal neurological exam findings. The appeal was approved in 12 days.</p>
    <p><strong>Billed:</strong> $8,500 &rarr; <strong>Patient owed after insurance:</strong> $250 (copay) &rarr; <strong>Savings: $8,250</strong></p>
</div>

<div class="case-study">
    <h3>Case 3: Out-of-network emergency reversed &mdash; $14,000 ER bill</h3>
    <p>A patient on vacation had a severe asthma attack and was taken by ambulance to the nearest ER, which was out-of-network. The ER visit included CPT 99285 (Level 5 ER visit), a chest X-ray, arterial blood gas, nebulizer treatments, and overnight observation. The insurer processed the entire visit as out-of-network, applying a $5,000 out-of-network deductible and paying only 50% of the &ldquo;reasonable and customary&rdquo; amount. The patient received a bill for $14,000.</p>
    <p>The patient appealed citing the <a href="/guides/no-surprises-act-explained">No Surprises Act</a>, which requires emergency services to be covered at in-network cost-sharing rates regardless of network status. The insurer reprocessed the claim at in-network rates, applying the patient&rsquo;s $1,500 in-network deductible and 80/20 coinsurance.</p>
    <p><strong>Original patient responsibility:</strong> $14,000 &rarr; <strong>After appeal:</strong> $2,100 (deductible + coinsurance at in-network rates) &rarr; <strong>Savings: $11,900</strong></p>
</div>

<div class="case-study">
    <h3>Case 4: Coding error corrected on appeal &mdash; $3,200</h3>
    <p>A patient received an outpatient procedure and the claim was denied because the diagnosis code (ICD-10) submitted did not support the procedure code (CPT). The provider had submitted ICD-10 code M54.5 (low back pain) with CPT 62323 (lumbar epidural steroid injection), but the insurer&rsquo;s system required a more specific radiculopathy code (M54.16 or M54.17) to authorize the injection.</p>
    <p>The patient requested the claim details from both the insurer and the provider. After identifying the mismatch, the provider resubmitted with the correct, more specific ICD-10 code that matched the clinical documentation. The claim was processed and paid within 10 days of resubmission.</p>
    <p><strong>Originally denied:</strong> $3,200 &rarr; <strong>After code correction:</strong> $480 (patient coinsurance) &rarr; <strong>Savings: $2,720</strong></p>
</div>

<div class="case-study">
    <h3>Case 5: External review win after two internal denials &mdash; $45,000 cancer treatment</h3>
    <p>A patient with stage III colorectal cancer was prescribed a targeted therapy (cetuximab) in combination with chemotherapy after genetic testing showed the tumor was KRAS wild-type&mdash;meaning it was likely to respond to the targeted drug. The insurer denied coverage, calling the combination &ldquo;experimental&rdquo; for the patient&rsquo;s specific staging, despite NCCN (National Comprehensive Cancer Network) guidelines listing it as a recommended regimen.</p>
    <p>The patient&rsquo;s oncologist filed a first internal appeal with the NCCN guidelines, three peer-reviewed clinical trials, and a letter explaining the genetic testing rationale. Denied. A second internal appeal was filed with additional supporting literature and a letter from a second oncologist at an academic medical center. Denied again.</p>
    <p>The patient then requested an external review. The independent reviewer&mdash;a board-certified oncologist&mdash;examined the case, agreed with the treating oncologist&rsquo;s clinical reasoning, and overturned the denial, citing the NCCN guidelines and the tumor&rsquo;s genetic profile. The decision was binding.</p>
    <p><strong>Treatment cost:</strong> $45,000 &rarr; <strong>Patient owed with coverage:</strong> $4,500 (out-of-pocket max) &rarr; <strong>Savings: $40,500</strong></p>
</div>

<div class="key-takeaway">
    <strong>Notice the pattern:</strong> In every case, the patient won by combining (1) specific clinical documentation with (2) recognized medical guidelines and (3) persistence through the process. Case 5 shows why you should never stop at the internal appeal&mdash;the external review exists precisely for situations where the insurer&rsquo;s own reviewers get it wrong.
</div>

<h2 id="when-to-escalate">8. When to escalate beyond appeals</h2>

<p>If you&rsquo;ve exhausted the appeal process&mdash;or if the insurer isn&rsquo;t following the rules&mdash;you have additional options:</p>

<h3>State insurance commissioner complaint</h3>

<p>Every state has an insurance department that regulates insurers and investigates consumer complaints. Filing a complaint is free and can be done online in most states. State regulators have the power to order insurers to reprocess claims, pay penalties, and change practices.</p>

<ul>
    <li><strong>When to file:</strong> If the insurer missed response deadlines, didn&rsquo;t provide required information, or upheld a denial you believe violates state law</li>
    <li><strong>How to file:</strong> Visit your state insurance department website or use the <a href="https://www.naic.org/state_web_map.htm" target="_blank" rel="noopener">NAIC directory</a> to find your state&rsquo;s complaint portal</li>
    <li><strong>What to include:</strong> Denial letters, appeal correspondence, supporting documentation, and a clear description of the issue</li>
</ul>

<h3>CMS complaint for Medicare/Medicaid</h3>

<p>If your denial involves a Medicare Advantage plan, Medicaid managed care plan, or ACA marketplace plan, you can file a complaint with the Centers for Medicare &amp; Medicaid Services (CMS). CMS has enforcement authority over these plans and can require them to comply with coverage rules.</p>

<ul>
    <li><strong>Medicare:</strong> Call 1-800-MEDICARE (1-800-633-4227) or file at <a href="https://www.medicare.gov/claims-appeals" target="_blank" rel="noopener">medicare.gov</a></li>
    <li><strong>Marketplace plans:</strong> File at <a href="https://www.cms.gov/nosurprises" target="_blank" rel="noopener">cms.gov/nosurprises</a> or call 1-800-985-3059</li>
</ul>

<h3>Hiring a patient advocate</h3>

<p>For high-dollar denials ($10,000+), consider hiring a professional patient advocate or <a href="/guides/medical-billing-advocates">medical billing advocate</a>. They specialize in navigating the appeals process and often work on contingency (taking a percentage of the savings). An advocate is especially valuable when:</p>

<ul>
    <li>The denial involves complex clinical documentation (cancer treatment, specialty drugs, surgical procedures)</li>
    <li>You&rsquo;ve been denied at multiple levels and need fresh eyes on the strategy</li>
    <li>You don&rsquo;t have time or energy to manage the process yourself (common during active treatment)</li>
    <li>The dollar amount at stake justifies the cost</li>
</ul>

<h3>If your bill has already gone to collections</h3>

<p>A denied claim that results in a patient bill can eventually be sent to collections. If this has happened to you, you still have rights. Visit our <a href="/fight-debt">debt defense tools</a> to understand your options for validating the debt, disputing inaccurate amounts, and negotiating settlements. A successful appeal can eliminate the debt entirely.</p>

<div class="key-takeaway">
    <strong>Don&rsquo;t pay a denied claim without fighting.</strong> The entire appeal process&mdash;from first internal appeal through binding external review&mdash;is designed to give you multiple chances to get the right answer. Use every level available to you. And <a href="/scan">upload your bill to BillKarma</a> at any point in the process to check for coding errors and overcharges that strengthen your case.
</div>

<h2 id="faq">Frequently asked questions</h2>

<div class="faq-section">
    <div class="faq-item">
        <h3>What percentage of insurance claim appeals actually succeed?</h3>
        <p>Between 44% and 80%, depending on the plan type and denial reason. KFF data shows ACA marketplace plans overturn about 44% of internal appeals. State insurance departments report even higher success rates for certain denial types, particularly coding errors (~80%) and prior authorization denials (~60%). External reviews overturn an additional 40&ndash;45% of denials that survive internal appeals.</p>
    </div>

    <div class="faq-item">
        <h3>How long do I have to appeal a denied insurance claim?</h3>
        <p>Most plans give you 180 days (about 6 months) from the denial date to file an internal appeal. For external reviews, you typically have 4 months after your final internal appeal denial. For urgent situations where waiting could harm your health, you can request an expedited appeal with a 72-hour response requirement. Always check your denial letter for the exact deadline.</p>
    </div>

    <div class="faq-item">
        <h3>Does it cost anything to file an insurance appeal?</h3>
        <p>No. Both internal appeals and external reviews are free under federal law. Insurance companies are required to provide a fair appeals process at no charge. You may choose to hire a <a href="/guides/medical-billing-advocates">medical billing advocate</a> for help, but this is optional.</p>
    </div>

    <div class="faq-item">
        <h3>What is an external review and why is it so powerful?</h3>
        <p>An external review is an independent evaluation by a physician or clinical expert who does not work for your insurer. It is available after you exhaust internal appeals. The reviewer&rsquo;s decision is legally binding&mdash;your insurer must comply if the reviewer overturns the denial. About 40&ndash;45% of external reviews result in the denial being overturned. It is free to request and available for most types of denials.</p>
    </div>

    <div class="faq-item">
        <h3>Can I appeal a claim denial even after I have already paid the bill?</h3>
        <p>Yes. Paying a bill does not waive your right to appeal. If your appeal succeeds, the insurer will pay the provider, and you will receive a refund for what you already paid. Keep all receipts and proof of payment. File your appeal within the deadline regardless of whether you have paid.</p>
    </div>

    <div class="faq-item">
        <h3>What should I do if my insurer does not respond to my appeal within the required timeframe?</h3>
        <p>If your insurer fails to respond within 30 days (non-urgent) or 72 hours (urgent), file an immediate complaint with your state insurance department. You may also have the right to proceed directly to external review. Document the dates of your submission and the missed deadline. Failure to respond within regulatory timelines is a violation that state regulators take seriously.</p>
    </div>
</div>

<h2 id="sources">Sources</h2>

<ul class="sources-list">
    <li><a href="https://www.kff.org/private-insurance/issue-brief/claims-denials-and-appeals-in-aca-marketplace-plans/" target="_blank" rel="noopener">KFF: Claims Denials and Appeals in ACA Marketplace Plans (2023 Data)</a></li>
    <li><a href="https://www.kff.org/health-policy/poll-finding/kff-health-tracking-poll/" target="_blank" rel="noopener">KFF Health Tracking Poll: Public Priorities for Health Policy</a></li>
    <li><a href="https://oig.hhs.gov/oei/reports/OEI-09-18-00260.asp" target="_blank" rel="noopener">HHS OIG: Medicare Advantage Prior Authorization Denials (2022)</a></li>
    <li><a href="https://www.dol.gov/sites/dolgov/files/EBSA/about-ebsa/our-activities/resource-center/publications/your-rights-after-a-claim-is-denied.pdf" target="_blank" rel="noopener">U.S. Department of Labor: Your Rights After a Health Insurance Claim Is Denied (ERISA)</a></li>
    <li><a href="https://www.healthcare.gov/appeal-insurance-company-decision/appeals/" target="_blank" rel="noopener">HealthCare.gov: How to Appeal a Health Insurance Company Decision</a></li>
    <li><a href="https://www.cms.gov/cciio/resources/consumer-assistance-grants" target="_blank" rel="noopener">CMS: Consumer Assistance Program &mdash; Appeals and External Review</a></li>
    <li><a href="https://www.cms.gov/nosurprises" target="_blank" rel="noopener">CMS: No Surprises Act &mdash; Consumer Protections</a></li>
    <li><a href="https://www.naic.org/state_web_map.htm" target="_blank" rel="noopener">NAIC: State Insurance Commissioner Directory</a></li>
    <li><a href="https://www.commonwealthfund.org/publications/issue-briefs/2023/feb/health-insurance-claim-denials" target="_blank" rel="noopener">Commonwealth Fund: Understanding Health Insurance Claim Denials</a></li>
</ul>
""",
})
