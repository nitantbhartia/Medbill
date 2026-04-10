"""Guide: Aetna Billing Disputes"""
from guides import register, _embed

register("aetna-insurance-billing-disputes", {
    "title": "Aetna Billing Disputes: Denials, Prior Auth, and Balance Bills",
    "meta_description": "How to dispute Aetna insurance denials, navigate prior auth appeals, use the Independent Review Organization process, and handle CVS Health integration billing issues.",
    "published": "2026-04-10",
    "author": "BillKarma Team",
    "category": "Insurance & Coverage",
    "faqs": [
        {
            "q": "How do I file an appeal with Aetna?",
            "a": "Log in to your Aetna member account at aetna.com, find the denied claim under Claims & EOBs, and select 'File an Appeal.' You can also call the Member Services number on your ID card or mail a written appeal to the address on your EOB. You have 180 days from the EOB date to file a standard appeal.",
        },
        {
            "q": "What is Aetna's Independent Review Organization process?",
            "a": "After Aetna upholds a denial at the first internal appeal level, you can request external review by an Independent Review Organization (IRO). The IRO is a neutral third party; its decision is binding on Aetna. Request IRO review within 4 months of Aetna's final internal denial.",
        },
        {
            "q": "How has the CVS Health merger affected Aetna billing?",
            "a": "Since CVS Health acquired Aetna in 2018, some pharmacy and specialty drug benefits are now administered through CVS Caremark rather than Aetna directly. If you have a pharmacy benefit denial, contact CVS Caremark (1-800-552-8159) rather than Aetna's medical line. Prior auth for specialty drugs flows through Caremark.",
        },
        {
            "q": "What procedures typically require prior auth with Aetna?",
            "a": "Aetna commonly requires prior authorization for: inpatient hospital stays, outpatient surgery at ASCs, MRI and CT scans (some plans), specialty drugs, durable medical equipment over a threshold cost, skilled nursing facility placement, and home health services. Check your plan documents or call Member Services before scheduling.",
        },
        {
            "q": "Can I get a peer-to-peer review with Aetna's medical director?",
            "a": "Yes. When Aetna denies a prior auth or claims medical necessity isn't met, your treating physician can request a peer-to-peer call with Aetna's medical director. This often resolves denials faster than a written appeal. Ask your doctor's office to call Aetna's clinical line within 48 hours of the denial.",
        },
    ],
    "body": """<article>
<div class="answer-box"><strong>Quick Answer:</strong> To dispute an Aetna denial, log in to aetna.com to find your EOB and denial reason, then file a written appeal within 180 days. If Aetna upholds its denial, request an Independent Review Organization (IRO) external review—the IRO's decision binds Aetna. For pharmacy or specialty drug denials, contact CVS Caremark, not Aetna's medical line.</div>

<nav class="toc">
    <h2>In this guide</h2>
    <ol>
        <li><a href="#eob-and-portal">Your EOB and the Aetna Member Portal</a></li>
        <li><a href="#internal-appeal">Filing Aetna's Internal Appeal</a></li>
        <li><a href="#iro">The IRO External Review Process</a></li>
        <li><a href="#prior-auth">Prior Auth Denials and Peer-to-Peer Review</a></li>
        <li><a href="#cvs-integration">CVS Health Integration: Pharmacy and Specialty Drug Billing</a></li>
        <li><a href="#timelines">Timelines and Contacts</a></li>
    </ol>
</nav>

<h2 id="eob-and-portal">Your EOB and the Aetna Member Portal</h2>

<p>Every Aetna coverage decision generates an Explanation of Benefits (EOB). The EOB shows what was billed, what Aetna paid, your cost-sharing responsibility, and—critically—the reason for any denial or reduction.</p>

<p>Access your EOBs at <strong>aetna.com</strong> under "Claims &amp; EOBs." The portal also shows real-time claim status and lets you initiate appeals online. Download and save the EOB PDF for the claim you are disputing before doing anything else.</p>

<p>On the EOB, locate:</p>
<ul>
    <li><strong>Reason code:</strong> A short description or code explaining why the claim was denied or reduced (e.g., "not medically necessary," "prior authorization required," "out-of-network provider")</li>
    <li><strong>Claim number:</strong> Reference this on all correspondence</li>
    <li><strong>Appeals deadline:</strong> Aetna prints the filing deadline directly on the EOB for many plans</li>
</ul>

<h2 id="internal-appeal">Filing Aetna's Internal Appeal</h2>

<p>You have <strong>180 days from the EOB date</strong> to file a Level 1 internal appeal for most commercial Aetna plans. The steps are straightforward:</p>

<ol>
    <li><strong>Gather your documents:</strong> EOB, itemized bill from the provider, physician letter of medical necessity (if applicable), and any clinical records that support coverage.</li>
    <li><strong>Write a concise appeal letter:</strong> State the claim number, date of service, denial reason cited on the EOB, and why you believe the denial is wrong. One to two pages is enough.</li>
    <li><strong>Submit:</strong> Online at aetna.com, by fax to the number on your EOB, or by certified mail to the appeals address on your EOB. Keep a copy of everything.</li>
    <li><strong>Track the response:</strong> Aetna must respond within 30 days for pre-service appeals and 60 days for post-service claims. Expedited (urgent) appeals get a 72-hour response.</li>
</ol>

<p>If Aetna upholds the denial at Level 1, you typically have a second internal appeal level before you reach IRO review, depending on your plan type. Check your Summary Plan Description (SPD) or call Member Services to confirm whether your plan requires one or two internal appeal levels.</p>

<table>
    <thead>
        <tr><th>Appeal Level</th><th>Who Reviews</th><th>Filing Deadline</th><th>Aetna's Response Time</th></tr>
    </thead>
    <tbody>
        <tr><td>Level 1 Internal Appeal</td><td>Aetna's internal reviewers</td><td>180 days from EOB</td><td>30 days (pre-service) / 60 days (post-service)</td></tr>
        <tr><td>Level 2 Internal Appeal (if applicable)</td><td>Different Aetna reviewers</td><td>Per your plan documents</td><td>30–60 days</td></tr>
        <tr><td>External Review (IRO)</td><td>Independent Review Organization</td><td>4 months from final internal denial</td><td>45 days (standard) / 72 hours (expedited)</td></tr>
        <tr><td>State Insurance Complaint</td><td>State insurance commissioner</td><td>Varies by state</td><td>Varies</td></tr>
    </tbody>
</table>

<h2 id="iro">The IRO External Review Process</h2>

<p>After exhausting Aetna's internal appeal levels, you have the right to request independent external review. The IRO is accredited by URAC or similar body and has no financial relationship with Aetna. Its decision is <strong>legally binding on Aetna</strong> in most states under the ACA and applicable state law.</p>

<p>To request IRO review:</p>
<ol>
    <li>Submit a written request to the IRO listed in Aetna's final denial letter, or ask Aetna to provide the approved IRO list for your state.</li>
    <li>Send the IRO your appeal records, EOBs, physician letters, and clinical documentation. The IRO reviews what you submit—more evidence is better.</li>
    <li>The IRO must render a decision within <strong>45 days</strong> for standard reviews and <strong>72 hours</strong> for expedited urgent cases.</li>
    <li>If the IRO overturns Aetna's denial, Aetna must pay the claim. If the IRO upholds the denial, your next step is a state insurance commissioner complaint or, for ERISA plans, a federal EBSA complaint.</li>
</ol>

<h2 id="prior-auth">Prior Auth Denials and Peer-to-Peer Review</h2>

<p>Prior authorization denials are the most frequent source of Aetna billing disputes. When Aetna denies a prior auth:</p>

<ul>
    <li><strong>Request a peer-to-peer review immediately.</strong> Your physician calls Aetna's medical director to discuss the clinical rationale. This costs nothing and often reverses denials that are based on incomplete information in the file.</li>
    <li><strong>Review Aetna's clinical policy bulletin.</strong> Aetna publishes clinical policy bulletins (CPBs) on its website that explain exactly what criteria a service must meet to be covered. Your appeal should address each criterion point by point.</li>
    <li><strong>Submit clinical guidelines.</strong> Evidence from peer-reviewed medical journals, specialty society guidelines, or CMS coverage determinations that support the appropriateness of the service strengthen your case significantly.</li>
</ul>

<p>Common procedures that frequently require Aetna prior auth and face denial include: MRI and advanced imaging, inpatient psychiatric admissions, sleep studies (polysomnography), spinal injections, and specialty biologics.</p>

<h2 id="cvs-integration">CVS Health Integration: Pharmacy and Specialty Drug Billing</h2>

<p>Since CVS Health acquired Aetna in 2018, pharmacy benefits for most Aetna commercial and Medicare plans are administered through <strong>CVS Caremark</strong>. This split creates a common source of confusion:</p>

<ul>
    <li><strong>Medical denials</strong> (hospital, physician, outpatient services): Contact Aetna Member Services</li>
    <li><strong>Pharmacy and specialty drug denials</strong>: Contact CVS Caremark at <strong>1-800-552-8159</strong> or caremark.com</li>
    <li><strong>Specialty drugs</strong> (biologics, infusion therapies, specialty injectables): Handled through CVS Specialty—call <strong>1-800-237-2767</strong></li>
</ul>

<p>If a specialty drug was denied because it wasn't dispensed through a CVS Specialty pharmacy but you used a different specialty pharmacy your doctor recommended, you may be able to file a network exception request. Ask your doctor's office to submit a medical necessity exception with documentation showing why the alternative pharmacy was used.</p>

""" + _embed("dispute", title="Dispute an Aetna Bill", subtitle="BillKarma analyzes your claim against standard rates.") + """

<h2 id="timelines">Timelines and Key Contacts</h2>

<ul>
    <li><strong>File internal appeal:</strong> Within 180 days of EOB date</li>
    <li><strong>Request IRO external review:</strong> Within 4 months of final internal denial</li>
    <li><strong>Aetna Member Services (commercial):</strong> Number on your ID card; general line <strong>1-888-632-3862</strong></li>
    <li><strong>Aetna Medicare Member Services:</strong> <strong>1-800-282-5366</strong></li>
    <li><strong>CVS Caremark (pharmacy):</strong> <strong>1-800-552-8159</strong></li>
    <li><strong>CVS Specialty:</strong> <strong>1-800-237-2767</strong></li>
    <li><strong>EBSA (ERISA plan complaints):</strong> <strong>1-866-444-3272</strong></li>
</ul>

<ul class="sources-list">
    <li><a href="https://www.aetna.com/individuals-families/using-your-aetna-benefits/appeals-grievances.html" target="_blank" rel="noopener">Aetna &mdash; Appeals and Grievances</a></li>
    <li><a href="https://www.cms.gov/CCIIO/Resources/Fact-Sheets-and-FAQs/aca_implementation_faqs" target="_blank" rel="noopener">CMS &mdash; ACA External Review Requirements</a></li>
    <li><a href="https://www.dol.gov/agencies/ebsa" target="_blank" rel="noopener">Department of Labor &mdash; EBSA (ERISA Plans)</a></li>
    <li><a href="https://www.caremark.com" target="_blank" rel="noopener">CVS Caremark &mdash; Pharmacy Benefits</a></li>
</ul>
</article>""",
})
