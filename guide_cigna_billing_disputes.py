"""Guide: Cigna Billing Disputes"""
from guides import register, _embed

register("cigna-billing-disputes-guide", {
    "title": "Cigna Billing Disputes: Denials, Medical Necessity Appeals, and EOB Errors",
    "meta_description": "How to dispute Cigna insurance denials using the myCigna portal, appeal medical necessity decisions, resolve EOB errors, and navigate Cigna's behavioral health billing differences.",
    "published": "2026-04-10",
    "author": "BillKarma Team",
    "category": "Insurance & Coverage",
    "faqs": [
        {
            "q": "How do I file an appeal with Cigna?",
            "a": "Log in to myCigna.com, go to Claims, find the denied claim, and select 'Appeal this Decision.' You can also call the Member Services number on your ID card or mail a written appeal to the address listed on your Explanation of Benefits. Most plans allow 180 days from the EOB date.",
        },
        {
            "q": "Does Cigna handle behavioral health billing separately?",
            "a": "Yes. Many Cigna commercial plans carve out behavioral health benefits to Cigna Behavioral Health, a subsidiary. Mental health and substance use disorder claims are processed separately from medical claims. If you have a behavioral health billing issue, call the Cigna Behavioral Health line on your ID card rather than general Member Services.",
        },
        {
            "q": "What is Cigna's medical necessity review process?",
            "a": "When Cigna denies a claim as not medically necessary, it applies coverage criteria from its Medical Coverage Policies (available on cigna.com). Your appeal should directly address those criteria. You can also request a peer-to-peer review between your treating physician and Cigna's medical director.",
        },
        {
            "q": "What is the myCigna portal and what can I do there for billing disputes?",
            "a": "myCigna.com is Cigna's member portal. You can access EOBs, file and track appeals, send secure messages to Member Services, request prior authorizations, check claim status, and view your plan's Summary of Benefits and Coverage—all without calling.",
        },
        {
            "q": "How long does Cigna have to respond to an appeal?",
            "a": "For post-service (retrospective) appeals, Cigna has 60 days. For pre-service (prospective) appeals, 30 days. For urgent concurrent care appeals, Cigna must respond within 72 hours. These timelines are required under ACA regulations.",
        },
    ],
    "body": """<article>
<div class="answer-box"><strong>Quick Answer:</strong> Start a Cigna billing dispute by pulling your EOB from myCigna.com and identifying the exact denial reason. File a written appeal within 180 days citing Cigna's own Medical Coverage Policy criteria. For mental health denials, contact Cigna Behavioral Health separately. If Cigna upholds its denial, request IRO external review—its decision is binding.</div>

<nav class="toc">
    <h2>In this guide</h2>
    <ol>
        <li><a href="#mycigna">Using the myCigna Portal for Disputes</a></li>
        <li><a href="#eob-errors">Finding and Fixing EOB Errors</a></li>
        <li><a href="#medical-necessity">Medical Necessity Appeals</a></li>
        <li><a href="#behavioral-health">Cigna Behavioral Health Billing</a></li>
        <li><a href="#appeal-steps">Step-by-Step Appeal Process</a></li>
        <li><a href="#iro">External Review (IRO)</a></li>
        <li><a href="#timelines">Timelines and Contacts</a></li>
    </ol>
</nav>

<h2 id="mycigna">Using the myCigna Portal for Disputes</h2>

<p>myCigna.com is your command center for any billing dispute. Before calling or mailing anything, log in and:</p>

<ul>
    <li>Navigate to <strong>Claims</strong> and locate the denied or underpaid claim by date of service</li>
    <li>Click through to the Explanation of Benefits (EOB) PDF—download and save it</li>
    <li>Note the <strong>reason code</strong> on the EOB (e.g., "medical necessity not established," "prior authorization required," "non-covered service")</li>
    <li>Check your <strong>plan documents</strong> under "Plan Information" to confirm whether the service is covered at all</li>
    <li>Use the <strong>Secure Message</strong> feature to create a written record of your dispute without waiting on hold</li>
</ul>

<p>The portal also lets you initiate an appeal directly: click "Appeal this Decision" on the denied claim page. This timestamps your request and creates a case number you can reference in all follow-up.</p>

<h2 id="eob-errors">Finding and Fixing EOB Errors</h2>

<p>Many Cigna billing disputes are not complex coverage denials—they are simple errors in how a claim was processed. The most common EOB errors include:</p>

<table>
    <thead>
        <tr><th>Error Type</th><th>How to Spot It</th><th>How to Fix It</th></tr>
    </thead>
    <tbody>
        <tr>
            <td>Wrong network status</td>
            <td>Provider is listed as out-of-network but you verified in-network before the visit</td>
            <td>Call Cigna with the provider's NPI number; request network status verification for the date of service</td>
        </tr>
        <tr>
            <td>Wrong CPT code</td>
            <td>The procedure code on the EOB doesn't match what was performed</td>
            <td>Contact your provider's billing office; ask them to submit a corrected claim with the accurate CPT code</td>
        </tr>
        <tr>
            <td>Duplicate processing</td>
            <td>Cigna lists two payments for the same claim or refuses to pay because it says it already paid</td>
            <td>Call Member Services with both claim numbers; request a claim audit</td>
        </tr>
        <tr>
            <td>Deductible/coinsurance miscalculation</td>
            <td>Your patient responsibility exceeds what the plan document says</td>
            <td>Compare your Summary of Benefits and Coverage to the EOB; dispute the math in writing</td>
        </tr>
        <tr>
            <td>Pre-auth shown as missing when it was obtained</td>
            <td>EOB says "prior auth not obtained" but your records show auth was approved</td>
            <td>Cite the auth number in your appeal; attach the approval letter from Cigna</td>
        </tr>
    </tbody>
</table>

<h2 id="medical-necessity">Medical Necessity Appeals</h2>

<p>Cigna publishes its <strong>Medical Coverage Policies (MCPs)</strong> on cigna.com. These are the exact criteria Cigna's reviewers use to determine whether a service is medically necessary. When Cigna denies a claim for medical necessity, the denial letter must cite the specific policy that applies.</p>

<p>Your appeal strategy:</p>
<ol>
    <li><strong>Download the applicable MCP</strong> from cigna.com and read the coverage criteria carefully.</li>
    <li><strong>Ask your physician to write a letter</strong> that addresses each criterion in the MCP by name—don't just say the service was needed, say it met criterion 2(b) because of specific clinical findings.</li>
    <li><strong>Request a peer-to-peer review</strong> between your physician and Cigna's medical director within 48 hours of the denial. This is often the fastest path to reversal.</li>
    <li><strong>Attach clinical evidence:</strong> lab results, imaging reports, specialist notes, and published treatment guidelines from specialty societies (e.g., American College of Cardiology guidelines for cardiac procedures).</li>
</ol>

<p>If Cigna's first-level review upholds the denial, request escalation to a second-level review by a different clinical reviewer. Cigna's process typically includes two internal review levels before external review.</p>

<h2 id="behavioral-health">Cigna Behavioral Health Billing</h2>

<p>Mental health and substance use disorder (SUD) coverage is often carved out to <strong>Cigna Behavioral Health (CBH)</strong>, which applies its own network, prior auth requirements, and coverage criteria separate from your medical plan. This is a major source of billing confusion.</p>

<p>Key differences with Cigna Behavioral Health:</p>
<ul>
    <li><strong>Separate network:</strong> A provider in Cigna's medical network may not be in the CBH network. Always verify behavioral health providers through CBH specifically.</li>
    <li><strong>Separate prior auth:</strong> Inpatient psychiatric admissions, residential treatment, intensive outpatient programs (IOPs), and partial hospitalization programs (PHPs) almost always require CBH prior auth, separate from any medical prior auth.</li>
    <li><strong>Mental Health Parity Act protections:</strong> Federal law requires Cigna to apply no stricter limitations to mental health and SUD benefits than it applies to comparable medical and surgical benefits. If you believe Cigna is applying tighter criteria to behavioral health than to comparable medical services, cite the Mental Health Parity and Addiction Equity Act (MHPAEA) in your appeal.</li>
    <li><strong>Appeals through CBH:</strong> File behavioral health appeals with Cigna Behavioral Health specifically—not Cigna's general Member Services.</li>
</ul>

<p>For mental health parity complaints, you can also file with your state insurance commissioner or with the Department of Labor (ERISA plans).</p>

""" + _embed("dispute", title="Dispute a Cigna Bill", subtitle="BillKarma flags overcharges and coverage errors instantly.") + """

<h2 id="appeal-steps">Step-by-Step Appeal Process</h2>

<ol>
    <li><strong>Log in to myCigna.com</strong> and download your EOB for the denied claim.</li>
    <li><strong>Identify the specific denial reason</strong> and find the relevant Cigna Medical Coverage Policy at cigna.com.</li>
    <li><strong>Call Member Services</strong> (or CBH for behavioral health) to ask whether the denial can be resolved informally or whether a peer-to-peer is available before filing a formal appeal.</li>
    <li><strong>Gather documentation:</strong> physician letter, medical records, prior auth approval (if applicable), and clinical guidelines.</li>
    <li><strong>File your written appeal</strong> at myCigna.com or by certified mail within 180 days of the EOB. Reference your claim number and the specific MCP criteria.</li>
    <li><strong>Track the response:</strong> Cigna has 60 days for post-service appeals. If no response, follow up in writing.</li>
    <li>If denied at Level 1, request <strong>Level 2 internal review</strong> if available, then proceed to IRO external review.</li>
</ol>

<h2 id="iro">External Review (IRO)</h2>

<p>After exhausting internal appeals, you have the right to Independent Review Organization (IRO) external review. The IRO is neutral and its decision is binding on Cigna. Request IRO review within <strong>4 months</strong> of Cigna's final internal denial. Cigna's denial letter will provide contact information for the approved IRO process in your state.</p>

<h2 id="timelines">Timelines and Key Contacts</h2>

<ul>
    <li><strong>Internal appeal deadline:</strong> 180 days from EOB date</li>
    <li><strong>Cigna response (post-service):</strong> 60 days</li>
    <li><strong>Cigna response (pre-service):</strong> 30 days</li>
    <li><strong>Cigna response (urgent/expedited):</strong> 72 hours</li>
    <li><strong>IRO external review deadline:</strong> 4 months from final internal denial</li>
    <li><strong>Cigna Member Services:</strong> Number on your ID card; general commercial line <strong>1-800-244-6224</strong></li>
    <li><strong>Cigna Behavioral Health:</strong> Number on your ID card (separate from medical line)</li>
    <li><strong>myCigna.com:</strong> Member portal for EOBs, appeals, and secure messaging</li>
    <li><strong>EBSA (ERISA plans):</strong> 1-866-444-3272</li>
</ul>

<ul class="sources-list">
    <li><a href="https://www.cigna.com/individuals-families/member-guide/appeals-and-disputes" target="_blank" rel="noopener">Cigna &mdash; Appeals and Disputes</a></li>
    <li><a href="https://www.cigna.com/legal/coverage-policies" target="_blank" rel="noopener">Cigna &mdash; Medical Coverage Policies</a></li>
    <li><a href="https://www.dol.gov/agencies/ebsa/laws-and-regulations/laws/mental-health-parity" target="_blank" rel="noopener">Department of Labor &mdash; Mental Health Parity (MHPAEA)</a></li>
    <li><a href="https://www.cms.gov/CCIIO/Programs-and-Initiatives/Health-Insurance-Market-Reforms/External-Appeals" target="_blank" rel="noopener">CMS &mdash; ACA External Review Requirements</a></li>
</ul>
</article>""",
})
