"""Guide: Medicaid Patient Billing Rights"""

from guides import register, _embed

register("medicaid-billing-rights", {
    "title": "Medicaid Billing Rights: What Providers Can and Cannot Charge You",
    "meta_description": "Medicaid patients cannot be balance billed. Learn your billing rights, how to file complaints, retroactive eligibility rules, and what to do if a provider refuses Medicaid mid-treatment.",
    "published": "2026-04-10",
    "author": "BillKarma Team",
    "category": "Patient Rights",
    "faqs": [
        {
            "q": "Can a provider balance bill a Medicaid patient?",
            "a": "No. Providers who participate in Medicaid accept Medicaid payment as payment in full. They cannot bill Medicaid patients for any amounts beyond Medicaid's required cost-sharing (which is zero or nominal for most services). If you are Medicaid-enrolled and a provider sends you a bill beyond your applicable cost-sharing, this is an illegal balance bill.",
        },
        {
            "q": "What happens if a provider says they 'don't take Medicaid' after I've already been treated?",
            "a": "If the provider is enrolled in Medicaid, they must bill Medicaid and accept its payment. If they are not enrolled in Medicaid, they can only bill you at their normal rates for non-emergency services. For emergency services, federal law requires treatment regardless of payment source. If a Medicaid-enrolled provider tries to collect from you after the fact, file a complaint with your state Medicaid agency.",
        },
        {
            "q": "What is retroactive Medicaid eligibility?",
            "a": "Retroactive Medicaid eligibility allows your Medicaid coverage to apply to medical bills incurred up to three months before you applied, if you would have been eligible during that period. This can wipe out bills you received before you knew you qualified for Medicaid. You must apply for retroactive eligibility at your state Medicaid office within the time limit.",
        },
        {
            "q": "What is a Medicaid fair hearing?",
            "a": "A Medicaid fair hearing is an administrative proceeding you can request when your state Medicaid agency denies, reduces, or terminates your benefits. You have the right to a hearing before an impartial reviewer. Most states require you to request a hearing within 90 days of the adverse action notice. You can bring a representative, present evidence, and question witnesses.",
        },
        {
            "q": "Does Medicaid have cost-sharing like Medicare?",
            "a": "Most Medicaid enrollees pay little or no cost-sharing. Federal law limits Medicaid cost-sharing based on income level. For beneficiaries at or below 100% of the federal poverty level, cost-sharing is zero for most services. Nominal copays (usually $1&ndash;$4) may apply at higher income levels, but providers cannot deny services if you cannot pay even a nominal copay.",
        },
    ],
    "body": f"""<article>
<div class="answer-box"><strong>Quick Answer:</strong> Medicaid patients have strong federal billing protections. Providers cannot balance bill you, cost-sharing is zero or nominal for most enrollees, and coverage can apply retroactively up to three months. If a provider bills you incorrectly, file a complaint with your state Medicaid agency and request a fair hearing if benefits are denied.</div>

<nav class="toc">
    <h2>In this guide</h2>
    <ol>
        <li><a href="#no-balance-billing">No Balance Billing for Medicaid Patients</a></li>
        <li><a href="#cost-sharing">Cost-Sharing Limits</a></li>
        <li><a href="#mid-treatment">When a Provider Refuses Medicaid Mid-Treatment</a></li>
        <li><a href="#retroactive">Retroactive Medicaid Eligibility</a></li>
        <li><a href="#complaints">How to File a Medicaid Billing Complaint</a></li>
        <li><a href="#fair-hearing">Fair Hearing Rights</a></li>
        <li><a href="#managed-care">Medicaid Managed Care Billing</a></li>
    </ol>
</nav>

<h2 id="no-balance-billing">No Balance Billing for Medicaid Patients</h2>

<p>This is the most important rule in Medicaid billing: <strong>providers who accept Medicaid cannot charge Medicaid patients more than their applicable Medicaid cost-sharing.</strong> Federal law (42 U.S.C. &sect;1396a) prohibits balance billing Medicaid enrollees.</p>

<p>When a Medicaid-enrolled provider accepts Medicaid as your payer, they accept Medicaid's payment as payment in full. They cannot bill you for:</p>
<ul>
    <li>The difference between their usual charge and what Medicaid paid</li>
    <li>Any additional amount above your Medicaid cost-sharing</li>
    <li>Services that Medicaid denied as not covered, unless they told you in advance the service wasn't covered and you agreed in writing to be responsible</li>
</ul>

<p>This protection applies regardless of how low Medicaid's reimbursement rate is. Even if the provider feels underpaid by Medicaid, they accepted those terms when they enrolled as a Medicaid provider. The shortfall is their business problem, not yours.</p>

<div class="key-takeaway">
    <strong>If you receive a bill that exceeds your Medicaid cost-sharing, do not pay it.</strong> Contact your state Medicaid agency's fraud and abuse hotline. Keep the bill as documentation. This is a violation of your federal rights.
</div>

<h2 id="cost-sharing">Cost-Sharing Limits</h2>

<p>Federal regulations cap Medicaid cost-sharing based on your income level. For most Medicaid enrollees, out-of-pocket costs are zero or near zero:</p>

<table>
    <thead>
        <tr><th>Income Level (% Federal Poverty Level)</th><th>Maximum Cost-Sharing</th><th>Notes</th></tr>
    </thead>
    <tbody>
        <tr><td>&le;100% FPL</td><td>Nominal or zero</td><td>Providers cannot deny service if you can't pay</td></tr>
        <tr><td>101%&ndash;150% FPL</td><td>Nominal (typically $1&ndash;$4 per service)</td><td>Still cannot be denied care for inability to pay</td></tr>
        <tr><td>151%&ndash;200% FPL</td><td>Up to 10% of cost of service</td><td>State-specific rules apply</td></tr>
        <tr><td>Pregnant women</td><td>$0</td><td>No cost-sharing for pregnancy-related services</td></tr>
        <tr><td>Children under 18</td><td>$0 for preventive services</td><td>CHIP has similar protections</td></tr>
        <tr><td>Emergency services</td><td>$0 for all eligible individuals</td><td>Emergency care is always zero cost-sharing</td></tr>
    </tbody>
</table>

<p>Critically: <strong>providers cannot deny you Medicaid-covered services because you cannot pay a nominal copay.</strong> If you have no ability to pay even a $3 copay, the provider must still provide the service and bill Medicaid. They may bill you for the copay amount, but they cannot refuse treatment.</p>

<h2 id="mid-treatment">When a Provider Refuses Medicaid Mid-Treatment</h2>

<p>One of the most distressing scenarios: you receive care, then the provider claims they don't take Medicaid when the bill comes. This happens more than it should. Here's how to respond:</p>

<h3>If the provider is enrolled in Medicaid</h3>
<p>Check your state Medicaid website's provider directory. If the provider is listed as an enrolled Medicaid provider and they treated you, they are required to bill Medicaid. Refusing to accept Medicaid payment from an enrolled beneficiary violates federal law. Contact your state Medicaid agency's provider relations office and your state's Medicaid fraud unit.</p>

<h3>If the provider is not enrolled in Medicaid</h3>
<p>For non-emergency services, a non-enrolled provider legally can bill you at regular rates. However:</p>
<ul>
    <li>You should have been told before receiving care that they don't accept Medicaid</li>
    <li>If you were in an emergency, federal EMTALA law required them to treat you; your Medicaid coverage should still apply for the emergency stabilization portion</li>
    <li>Ask if they will enroll in Medicaid retroactively to cover your treatment&mdash;providers can request retroactive enrollment for specific claims</li>
</ul>

<h3>At an in-network Medicaid facility</h3>
<p>If the facility accepts Medicaid but an individual provider within the facility (specialist, anesthesiologist) does not, you generally cannot be billed beyond applicable cost-sharing for services received at a Medicaid-enrolled facility. The facility is responsible for ensuring billing compliance.</p>

<h2 id="retroactive">Retroactive Medicaid Eligibility</h2>

<p>Most states allow Medicaid coverage to apply retroactively for up to <strong>three months before the month you applied</strong>. This means if you were hospitalized in January, received a $40,000 bill, and applied for Medicaid in March, your January bills may be covered if you would have been eligible in January.</p>

<p>To claim retroactive eligibility:</p>
<ol>
    <li>Apply for Medicaid as soon as possible. Some states require you to specifically request retroactive coverage.</li>
    <li>Gather documentation of your income and household size for the retroactive months.</li>
    <li>Once approved, notify your providers and give them your Medicaid number. They can resubmit claims to Medicaid for the covered period.</li>
    <li>If providers have already sent your bill to collections, notify the collection agency of your Medicaid coverage. The debt may be extinguished.</li>
</ol>

<p><strong>Note:</strong> The Affordable Care Act eliminated mandatory retroactive eligibility for expansion Medicaid populations in some states. Rules vary by state and eligibility category. Contact your state Medicaid office or a benefits navigator to confirm your state's rules.</p>

{_embed("dispute", title="Review Your Medicaid Bill", subtitle="BillKarma checks for illegal balance billing and Medicaid billing errors.")}

<h2 id="complaints">How to File a Medicaid Billing Complaint</h2>

<p>If a provider has illegally billed you beyond your Medicaid cost-sharing:</p>

<ol>
    <li><strong>Contact your state Medicaid agency.</strong> Every state has a Medicaid helpline. Find it at medicaid.gov/state-overviews. Provide the provider's name, the bill amount, your Medicaid ID number, and the service date.</li>
    <li><strong>File a provider complaint.</strong> Most state Medicaid agencies have a provider complaint process separate from the appeals process. This triggers a review of the provider's billing practices.</li>
    <li><strong>Report to the Medicaid Fraud Control Unit (MFCU).</strong> Every state has an MFCU that investigates Medicaid fraud and abuse, including illegal billing of beneficiaries. If a provider is systematically billing Medicaid patients, this is a pattern the MFCU investigates.</li>
    <li><strong>Contact the HHS Office of Inspector General.</strong> File a complaint at oig.hhs.gov/hotline for federal-level review.</li>
    <li><strong>Dispute the bill in writing.</strong> Send a letter to the provider citing 42 C.F.R. &sect;447.15 (the federal regulation prohibiting balance billing of Medicaid beneficiaries) and requesting immediate correction.</li>
</ol>

<h2 id="fair-hearing">Fair Hearing Rights</h2>

<p>If your state Medicaid agency denies, reduces, or terminates your benefits&mdash;or denies a service authorization request&mdash;you have the right to a <strong>fair hearing</strong>.</p>

<p>Key facts about Medicaid fair hearings:</p>
<ul>
    <li>You must receive written notice of any adverse action and your right to request a hearing</li>
    <li>Most states require you to request a hearing within <strong>90 days</strong> of the notice (some states allow less time)</li>
    <li>If you request a hearing before your benefits are terminated, your benefits must continue at the same level pending the hearing outcome</li>
    <li>You have the right to review your case file, present evidence, and be represented by a person of your choice (including an attorney, advocate, or family member)</li>
    <li>The hearing must be conducted by an impartial reviewer who was not involved in the original decision</li>
</ul>

<p>Fair hearings are free to request and are an important protection. Medicaid agencies deny services for administrative reasons that are often correctable with proper documentation. Do not accept a denial without requesting a fair hearing.</p>

<h2 id="managed-care">Medicaid Managed Care Billing</h2>

<p>Most Medicaid enrollees today receive care through Medicaid Managed Care Organizations (MCOs)&mdash;private health plans contracted by the state to deliver Medicaid services. Billing rules are similar but have some differences:</p>

<ul>
    <li>Your MCO maintains a provider network. Non-emergency out-of-network services may require prior authorization.</li>
    <li>The same federal balance billing prohibition applies: MCO-contracted providers cannot bill you more than your cost-sharing.</li>
    <li>MCOs have their own grievance and appeals processes, which you must use before requesting a Medicaid fair hearing.</li>
    <li>If your MCO denies a service and you exhaust the MCO appeals process, you can then request a state fair hearing.</li>
    <li>In emergencies, the MCO must cover services from any provider regardless of network, at cost-sharing rates no higher than in-network.</li>
</ul>

<ul class="sources-list">
    <li><a href="https://www.medicaid.gov/medicaid/eligibility/index.html" target="_blank" rel="noopener">Medicaid.gov &mdash; Eligibility</a></li>
    <li><a href="https://www.cms.gov/regulations-guidance/guidance/transmittals/downloads/r2762cp.pdf" target="_blank" rel="noopener">CMS &mdash; Medicaid Balance Billing Prohibition</a></li>
    <li><a href="https://www.medicaid.gov/medicaid/beneficiary-support/appeals-and-grievances/index.html" target="_blank" rel="noopener">Medicaid.gov &mdash; Appeals and Grievances</a></li>
    <li><a href="https://oig.hhs.gov/fraud/medicaid-fraud-control-units-mfcu/" target="_blank" rel="noopener">HHS OIG &mdash; Medicaid Fraud Control Units</a></li>
</ul>
</article>""",
})
