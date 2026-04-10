"""Guide: Insurance Prior Authorization Denied"""
from guides import register, _embed

register("insurance-prior-authorization-denied", {
    "title": "Prior Authorization Denied: How to Appeal and Get Your Procedure Covered",
    "meta_description": "What to do when insurance denies prior authorization—peer-to-peer review, the internal and IRO appeals ladder, No Surprises Act timelines, and how to escalate to your state insurance commissioner.",
    "published": "2026-04-10",
    "author": "BillKarma Team",
    "category": "Insurance & Coverage",
    "faqs": [
        {
            "q": "What are the most common reasons prior authorization is denied?",
            "a": "The most common reasons are: (1) medical necessity not established under the plan's clinical criteria; (2) the drug or service is not on the plan's formulary or approved list; (3) a required first-step therapy was not tried first (step therapy); (4) the provider submitted incomplete or incorrect information; and (5) the service is listed as experimental or investigational by the plan.",
        },
        {
            "q": "What is a peer-to-peer review and how do I request one?",
            "a": "A peer-to-peer review is a direct phone conversation between your treating physician and the insurance plan's medical director. Your doctor makes the case for medical necessity directly—often overturning denials that written submissions alone couldn't fix. Ask your doctor's office to request peer-to-peer review within 24–48 hours of the denial notice.",
        },
        {
            "q": "How long does an insurance company have to decide a prior auth request?",
            "a": "Under federal rules and the No Surprises Act, standard prior auth decisions must be made within 7 calendar days, urgent decisions within 72 hours, and concurrent care decisions (for ongoing treatment) within 24 hours. Many states have stricter timelines. If your insurer misses these deadlines, the delay itself is a violation you can report to your state insurance commissioner.",
        },
        {
            "q": "What is an Independent Review Organization (IRO) and when can I use it?",
            "a": "An IRO is a neutral third-party reviewer that evaluates prior auth appeals after you exhaust your insurer's internal process. Under the ACA, you have the right to IRO review after losing a Level 1 internal appeal for most coverage denials. The IRO's decision is binding on your insurer in most states.",
        },
        {
            "q": "Can my insurer require step therapy before covering the drug my doctor prescribed?",
            "a": "Yes, but many states have step therapy override laws that require insurers to waive the step therapy requirement when it would be harmful, when you've already tried and failed the required first-line drugs, or when the required drug is not clinically appropriate. Check your state's step therapy override rights and include that documentation in your appeal.",
        },
    ],
    "body": """<article>
<div class="answer-box"><strong>Quick Answer:</strong> When prior authorization is denied, your fastest path to reversal is a peer-to-peer review between your doctor and the insurer's medical director—request this within 48 hours of the denial. If that fails, file a formal internal appeal with clinical evidence addressing the specific denial criteria. If still denied, escalate to IRO external review. Under the No Surprises Act, standard prior auth decisions must come within 7 days—if your insurer is slow, file a complaint with your state insurance commissioner.</div>

<nav class="toc">
    <h2>In this guide</h2>
    <ol>
        <li><a href="#why-denied">Why Prior Auth Gets Denied</a></li>
        <li><a href="#first-steps">First Steps After a Denial</a></li>
        <li><a href="#peer-to-peer">Peer-to-Peer Review: Your Fastest Option</a></li>
        <li><a href="#appeals-ladder">The Appeals Ladder: Internal → IRO → State Commissioner</a></li>
        <li><a href="#timelines-nsa">Federal Timelines Under the No Surprises Act</a></li>
        <li><a href="#formulary-step">Formulary and Step Therapy Denials</a></li>
        <li><a href="#sample-appeal">Building a Strong Appeal Letter</a></li>
        <li><a href="#contacts">Key Contacts and Deadlines</a></li>
    </ol>
</nav>

<h2 id="why-denied">Why Prior Auth Gets Denied</h2>

<p>Prior authorization denials fall into a small number of recurring categories. Knowing which type you're facing determines your appeal strategy:</p>

<table>
    <thead>
        <tr><th>Denial Category</th><th>What It Means</th><th>How Often It's Reversed on Appeal</th></tr>
    </thead>
    <tbody>
        <tr>
            <td>Medical necessity not established</td>
            <td>The insurer's clinical reviewers say the service doesn't meet their coverage criteria</td>
            <td>High — peer-to-peer and clinical evidence overturn these frequently</td>
        </tr>
        <tr>
            <td>Step therapy / fail-first requirement</td>
            <td>Insurer requires you to try a cheaper drug or less intensive treatment first</td>
            <td>High — state override laws and documented contraindications are strong grounds</td>
        </tr>
        <tr>
            <td>Not on formulary / not approved</td>
            <td>The drug or device is not on the insurer's approved list</td>
            <td>Moderate — formulary exception requests succeed with strong physician documentation</td>
        </tr>
        <tr>
            <td>Experimental / investigational</td>
            <td>Insurer classifies the treatment as not yet proven standard of care</td>
            <td>Moderate — FDA approval, peer-reviewed literature, and specialty society guidelines help</td>
        </tr>
        <tr>
            <td>Incomplete submission</td>
            <td>The provider didn't submit all required information</td>
            <td>Very high — most resolve by resubmitting with complete documentation</td>
        </tr>
        <tr>
            <td>Network or coverage exclusion</td>
            <td>The service or provider is not covered under your specific plan</td>
            <td>Low without plan exception — focus on whether the exclusion was correctly applied</td>
        </tr>
    </tbody>
</table>

<h2 id="first-steps">First Steps After a Denial</h2>

<p>When you receive a prior auth denial:</p>

<ol>
    <li><strong>Get the written denial letter.</strong> If your provider received the denial, ask them to send you a copy. The letter must state the specific reason for denial and the clinical criteria that were applied.</li>
    <li><strong>Find the insurer's clinical policy.</strong> Most insurers publish their coverage guidelines online. Search for the insurer name plus "clinical policy" or "medical coverage policy" plus the service name. Your appeal should directly address the listed criteria.</li>
    <li><strong>Call your insurer's Member Services immediately.</strong> Ask for the denial reason in plain language and whether a peer-to-peer review is available. Note the representative's name and the date.</li>
    <li><strong>Tell your doctor's office the same day.</strong> They need to request peer-to-peer review quickly—this window often closes after 48–72 hours.</li>
</ol>

<h2 id="peer-to-peer">Peer-to-Peer Review: Your Fastest Option</h2>

<p>A peer-to-peer review is a direct phone call between your treating physician and the insurance company's medical director or clinical reviewer. It is often the single most effective tool for overturning prior auth denials—particularly medical necessity denials—and it costs nothing.</p>

<p>How to make it work:</p>
<ul>
    <li><strong>Act quickly:</strong> Most insurers allow peer-to-peer requests within 24–72 hours of the denial. Your doctor's office should call the insurer's utilization management line the same day or the next morning.</li>
    <li><strong>Brief your doctor beforehand:</strong> The physician should go into the call with specific clinical evidence—lab values, imaging results, failed prior treatments—ready to address the insurer's stated denial criteria point by point.</li>
    <li><strong>Document the call:</strong> Your doctor's office should note who participated, what was discussed, and the outcome. Get the insurer's response in writing after the call.</li>
    <li><strong>If the insurer won't schedule peer-to-peer:</strong> This is itself a potential violation in some states. Proceed to formal internal appeal immediately.</li>
</ul>

<h2 id="appeals-ladder">The Appeals Ladder: Internal → IRO → State Commissioner</h2>

<p>If peer-to-peer review doesn't resolve the denial, escalate through the formal appeals process:</p>

<h3>Step 1: Internal Appeal</h3>
<p>File a written appeal within the deadline on your denial letter (typically <strong>180 days</strong> for commercial plans under ACA rules; <strong>60 days</strong> for Medicare Advantage plans). Your appeal package should include:</p>
<ul>
    <li>Physician letter of medical necessity addressing the insurer's specific denial criteria</li>
    <li>Relevant medical records (lab results, imaging, prior treatment history)</li>
    <li>Published clinical guidelines from specialty societies supporting the treatment</li>
    <li>Any state override laws that apply (step therapy, experimental treatment)</li>
</ul>
<p>The insurer must respond within <strong>7 days</strong> for pre-service prior auth appeals under No Surprises Act rules (30 days under older ACA rules for some plan types). Urgent prior auth appeals require a decision within <strong>72 hours</strong>.</p>

<h3>Step 2: IRO External Review</h3>
<p>If the insurer upholds its denial at the internal level, request review by an Independent Review Organization. You typically have <strong>4 months</strong> from the final internal denial to file. The IRO is accredited and neutral—its decision is binding on the insurer under state and federal law.</p>
<p>Send the IRO everything: the denial letters, all appeal submissions, physician letters, records, and clinical guidelines. IRO reviewers consider only the written record, so more evidence is always better.</p>

<h3>Step 3: State Insurance Commissioner Complaint</h3>
<p>If the IRO upholds the denial—or if the insurer violated procedural rules at any point (missed deadlines, failed to offer peer-to-peer, failed to provide a written denial)—file a complaint with your state insurance commissioner. Most state insurance departments have online complaint forms and will investigate within 30–45 days.</p>
<p>For self-funded employer plans governed by ERISA, file with the Department of Labor's Employee Benefits Security Administration (EBSA) at 1-866-444-3272 or askebsa.dol.gov.</p>

""" + _embed("dispute", title="Check Your Prior Auth Denial", subtitle="BillKarma helps you identify the strongest grounds for your appeal.") + """

<h2 id="timelines-nsa">Federal Timelines Under the No Surprises Act</h2>

<p>The No Surprises Act (NSA) and implementing CMS rules impose strict prior authorization response timelines. Violation of these timelines is grounds for a complaint to your state insurance commissioner or CMS:</p>

<table>
    <thead>
        <tr><th>Request Type</th><th>Required Response Time</th><th>Applies To</th></tr>
    </thead>
    <tbody>
        <tr><td>Standard prior auth (new request)</td><td>7 calendar days</td><td>Most commercial plans under ACA</td></tr>
        <tr><td>Urgent (expedited) prior auth</td><td>72 hours</td><td>All plan types</td></tr>
        <tr><td>Concurrent care (ongoing treatment)</td><td>24 hours</td><td>Decisions that would interrupt ongoing care</td></tr>
        <tr><td>Prior auth appeal (pre-service, standard)</td><td>30 days</td><td>Commercial plans</td></tr>
        <tr><td>Prior auth appeal (urgent)</td><td>72 hours</td><td>Commercial plans</td></tr>
        <tr><td>Medicare Advantage prior auth</td><td>3 business days (standard) / 24 hours (urgent)</td><td>All MA plans</td></tr>
    </tbody>
</table>

<p>Beginning in 2026, CMS rules also require health plans to provide specific clinical reasons for every prior auth denial—generic "not medically necessary" responses without citing specific criteria are no longer permitted for many plan types.</p>

<h2 id="formulary-step">Formulary and Step Therapy Denials</h2>

<p>Pharmacy prior auth denials require a slightly different approach:</p>

<ul>
    <li><strong>Formulary exception:</strong> Request through your insurer's pharmacy benefit manager (PBM). Your prescribing physician must document why the formulary alternative won't work for you—contraindications, prior treatment failures, or unique clinical circumstances.</li>
    <li><strong>Step therapy override:</strong> If you're denied because you haven't "failed" a cheaper drug first, but you can't take that drug (allergy, contraindication, prior failure), your state may have a step therapy override law. At least 30 states require insurers to waive step therapy when documented medical reasons exist.</li>
    <li><strong>Non-medical switching:</strong> If your insurer is forcing you to switch from a drug that has been working to a different drug for cost reasons, some states prohibit non-medical switching for stable patients. Check your state's protections.</li>
</ul>

<h2 id="sample-appeal">Building a Strong Appeal Letter</h2>

<p>A winning prior auth appeal letter has four components:</p>
<ol>
    <li><strong>Statement of facts:</strong> Claim or auth number, date of denial, service or drug requested, and the denial reason cited in the insurer's letter.</li>
    <li><strong>Clinical argument:</strong> Address each denial criterion by name from the insurer's clinical policy. Don't make general statements—respond to each specific criterion.</li>
    <li><strong>Supporting evidence:</strong> List each document attached (physician letter, medical records, published guidelines, lab results). The IRO will only see what you submit.</li>
    <li><strong>Requested relief:</strong> State explicitly: "I request that [INSURER] approve prior authorization for [SERVICE] effective [DATE]."</li>
</ol>

<h2 id="contacts">Key Contacts and Deadlines</h2>

<ul>
    <li><strong>Internal appeal deadline:</strong> 180 days from denial (commercial) / 60 days from denial (Medicare Advantage)</li>
    <li><strong>IRO external review deadline:</strong> 4 months from final internal denial</li>
    <li><strong>Insurer's utilization management line:</strong> Printed on your insurance card or denial letter</li>
    <li><strong>No Surprises Help Desk:</strong> 1-800-985-3059 (for federal NSA violations)</li>
    <li><strong>EBSA (ERISA employer plans):</strong> 1-866-444-3272 / askebsa.dol.gov</li>
    <li><strong>State insurance commissioner:</strong> Search "[your state] insurance commissioner complaint" for the online form</li>
    <li><strong>CMS (Medicare Advantage):</strong> 1-800-MEDICARE (1-800-633-4227)</li>
</ul>

<ul class="sources-list">
    <li><a href="https://www.cms.gov/nosurprises" target="_blank" rel="noopener">CMS &mdash; No Surprises Act (Prior Auth Rules)</a></li>
    <li><a href="https://www.cms.gov/CCIIO/Programs-and-Initiatives/Health-Insurance-Market-Reforms/External-Appeals" target="_blank" rel="noopener">CMS &mdash; ACA External Review Requirements</a></li>
    <li><a href="https://www.dol.gov/agencies/ebsa/laws-and-regulations/laws/erisa" target="_blank" rel="noopener">Department of Labor &mdash; ERISA Appeals Rights</a></li>
    <li><a href="https://www.ncsl.org/health/state-prior-authorization-laws" target="_blank" rel="noopener">NCSL &mdash; State Prior Authorization Laws</a></li>
    <li><a href="https://www.kff.org/private-insurance/issue-brief/claims-denials-and-appeals-in-aca-marketplace-plans/" target="_blank" rel="noopener">KFF &mdash; Claims Denials and Appeals in ACA Plans</a></li>
</ul>
</article>""",
})
