"""Guide: Short-Term Health Insurance: 2026 Risks & Alternatives."""

from guides import register, _embed

register("short-term-health-insurance", {
    "title": "Short-Term Health Insurance: 2026 Risks & Alternatives",
    "meta_description": "Short-term health plans cost $100–$200/mo but exclude pre-existing conditions and ACA protections. See when they make sense and what alternatives exist in 2026.",
    "published": "2026-04-05",
    "author": "BillKarma Team",
    "category": "Insurance Basics",
    "faqs": [
        {
            "q": "What is short-term health insurance?",
            "a": "Short-term health insurance is a limited-duration medical plan designed to fill temporary gaps in coverage&mdash;typically between jobs, before Medicare eligibility, or during a waiting period for employer coverage to begin. These plans are not subject to the Affordable Care Act&rsquo;s consumer protections and do not count as minimum essential coverage. They typically cost $100 to $200 per month for a healthy adult but exclude pre-existing conditions, mental health treatment, maternity care, and preventive services.",
        },
        {
            "q": "How long can a short-term health plan last in 2026?",
            "a": "Under the Biden administration&rsquo;s 2024 rule (reinstated and finalized), short-term plans are limited to an initial term of no more than 3 months, with a maximum total duration of 4 months including any renewals. This reversed the Trump-era expansion that allowed plans up to 3 years. Some states impose even stricter limits&mdash;California, New York, and several others ban short-term plans entirely. Check your state&rsquo;s rules before enrolling.",
        },
        {
            "q": "Do short-term health plans cover pre-existing conditions?",
            "a": "No. Short-term plans are exempt from the ACA&rsquo;s pre-existing condition protections. Insurers can deny coverage entirely, exclude specific conditions, or charge higher premiums based on your health history. If you have a pre-existing condition&mdash;including well-controlled conditions like diabetes, hypertension, or past cancer treatment&mdash;a short-term plan will almost certainly exclude claims related to that condition, even if it was diagnosed years before enrollment.",
        },
        {
            "q": "What happens if I get sick with a short-term health plan?",
            "a": "If you experience a significant health event&mdash;a hospitalization, new diagnosis, or serious injury&mdash;on a short-term plan, you are exposed to significant financial risk. Claims can be denied for any condition that the insurer deems &ldquo;pre-existing,&rdquo; a definition they interpret broadly. Balance billing is common because many short-term plans have very limited provider networks. Claim denial rates on short-term plans average 25 to 35%, compared to under 8% for ACA marketplace plans, according to KFF data.",
        },
        {
            "q": "What are the alternatives to short-term health insurance?",
            "a": "Before buying a short-term plan, consider: (1) ACA Special Enrollment Period&mdash;losing job-based coverage is a qualifying life event that opens a 60-day window to enroll in a marketplace plan; (2) Medicaid&mdash;available year-round with no enrollment window if your income qualifies; (3) COBRA&mdash;continues your employer coverage for up to 18 months, though premiums are high; (4) spouse&rsquo;s or parent&rsquo;s employer plan if eligible. Each of these provides ACA-compliant coverage with pre-existing condition protections that short-term plans lack.",
        },
    ],
    "body": f"""
<p class="lead">Short-term health insurance plans average <strong>$100 to $200 per month</strong>&mdash;far less than ACA marketplace premiums&mdash;but that low price comes with hidden exposure. These plans exclude pre-existing conditions, mental health treatment, maternity care, and preventive services, and they carry claim denial rates of <strong>25 to 35%</strong>. In 2026, federal rules limit them to 4 months total coverage. This guide explains when short-term plans are appropriate, their critical limitations, and the alternatives that provide real coverage for most situations.</p>

<nav class="toc">
    <h2>In this guide</h2>
    <ol>
        <li><a href="#what-is">What is short-term health insurance?</a></li>
        <li><a href="#cost-table">Costs and coverage limits compared</a></li>
        <li><a href="#exclusions">What short-term plans do not cover</a></li>
        <li><a href="#billing-risks">How short-term plan billing differs</a></li>
        <li><a href="#when-it-makes-sense">When a short-term plan actually makes sense</a></li>
        <li><a href="#alternatives">Alternatives to short-term health insurance</a></li>
        <li><a href="#claim-denied">What to do if your claim is denied</a></li>
        <li><a href="#case-study">Real-world case study</a></li>
        <li><a href="#faq">Frequently asked questions</a></li>
        <li><a href="#sources">Sources</a></li>
    </ol>
</nav>

<h2 id="what-is">1. What is short-term health insurance?</h2>

<p>Short-term health insurance (STHI) is a category of limited-duration medical coverage sold by private insurers. These plans are specifically designed for healthy people who face temporary gaps in coverage&mdash;most commonly between jobs, before Medicare kicks in at 65, or while waiting for an employer plan&rsquo;s waiting period to end.</p>

<p>Short-term plans are exempt from the Affordable Care Act&rsquo;s essential health benefits requirements, meaning they do not have to cover the 10 categories of care that ACA plans must include. They also do not count as minimum essential coverage, so enrollees are technically uninsured for ACA purposes (though the ACA&rsquo;s individual mandate penalty was reduced to $0 federally in 2019; some states still impose one).</p>

<div class="key-takeaway">
    <strong>Short-term plans are not health insurance in the ACA sense.</strong> They are indemnity-style products that pay for some medical costs but are designed to limit insurer exposure&mdash;not to provide comprehensive coverage. Read every exclusion before enrolling.
</div>

<h2 id="cost-table">2. Costs and coverage limits compared</h2>

<table>
    <thead>
        <tr>
            <th>Feature</th>
            <th>Short-Term Plan</th>
            <th>ACA Marketplace Plan (Silver)</th>
            <th>COBRA</th>
        </tr>
    </thead>
    <tbody>
        <tr><td>Average monthly premium (individual, age 35)</td><td>$100&ndash;$200</td><td>$350&ndash;$550 (before subsidy)</td><td>$550&ndash;$800 (full employer + employee cost)</td></tr>
        <tr><td>Maximum coverage duration (2026)</td><td>4 months</td><td>Annual (renewable)</td><td>18 months</td></tr>
        <tr><td>Pre-existing condition coverage</td><td>No</td><td>Yes (ACA mandated)</td><td>Yes (continuation of employer plan)</td></tr>
        <tr><td>Minimum essential coverage</td><td>No</td><td>Yes</td><td>Yes</td></tr>
        <tr><td>Mental health &amp; substance use coverage</td><td>Usually excluded</td><td>Required</td><td>Required (same as employer plan)</td></tr>
        <tr><td>Maternity coverage</td><td>Usually excluded</td><td>Required</td><td>Required</td></tr>
        <tr><td>Preventive care (no cost sharing)</td><td>Not required</td><td>Required</td><td>Required</td></tr>
        <tr><td>Claim denial rate (avg.)</td><td>25&ndash;35%</td><td>7&ndash;9%</td><td>7&ndash;9%</td></tr>
    </tbody>
</table>

<h2 id="exclusions">3. What short-term plans do not cover</h2>

<p>Understanding exclusions is more important than understanding what short-term plans do cover. The following are standard exclusions in virtually all short-term plans sold in 2026:</p>

<ul>
    <li><strong>Pre-existing conditions:</strong> Any condition diagnosed or treated before your effective date&mdash;or for which you had symptoms&mdash;is excluded. Some plans use a lookback period of 3 to 5 years. Others use a broader definition that can exclude treatment for any condition you had ever been told about by a doctor.</li>
    <li><strong>Mental health and substance use disorders:</strong> Most short-term plans exclude or severely limit mental health treatment and substance use disorder care.</li>
    <li><strong>Maternity and newborn care:</strong> Pregnancy, prenatal visits, labor and delivery, and newborn care are excluded from virtually all short-term plans unless purchased as a separate rider (at significant additional cost).</li>
    <li><strong>Preventive care:</strong> Annual exams, vaccines, cancer screenings, and well-child visits are not required and often excluded.</li>
    <li><strong>Prescription drugs:</strong> Coverage is limited or absent on most short-term plans. Some cover generic drugs only; most do not cover specialty medications.</li>
    <li><strong>Balance billing:</strong> Short-term plans often have very limited provider networks or no network at all. Out-of-network providers can bill you directly for the difference between their charge and the plan&rsquo;s payment&mdash;balance billing that is prohibited on ACA plans for in-network care.</li>
</ul>

<h2 id="billing-risks">4. How short-term plan billing differs</h2>

<p>Billing disputes are significantly more common on short-term plans than on ACA-compliant coverage. The key differences that create financial risk:</p>

<p><strong>Pre-existing condition investigations:</strong> When you file a claim, the short-term insurer has the right to review your complete medical history&mdash;including records from prior providers, prescription fill history, and health questionnaire answers. Any condition they can tie to a prior symptom or diagnosis can be excluded retroactively, even if you disclosed everything accurately at enrollment.</p>

<p><strong>Lack of network protections:</strong> ACA plans prohibit balance billing for emergency care at out-of-network hospitals. Short-term plans do not have this protection. If you go to an ER that is out of the plan&rsquo;s narrow network, you can be balance billed for the full difference between the provider&rsquo;s charge and the plan&rsquo;s payment.</p>

<p><strong>Benefit limits:</strong> Many short-term plans cap total coverage at $250,000 to $1 million per year. A serious hospitalization&mdash;a cardiac event, a major accident, a cancer diagnosis&mdash;can easily exceed these limits, leaving you responsible for hundreds of thousands of dollars.</p>

<div class="bill-example">
    <div class="bill-header">Short-Term Plan Claim Denial &mdash; Actual EOB Example (anonymized) &mdash; 2026</div>
    <div class="line-item error"><span>ER Visit: Chest Pain &mdash; Admitted for observation &nbsp; &#10060; <em>Denied: Pre-existing condition (hypertension documented 2022)</em></span><span>$8,400.00 denied</span></div>
    <div class="line-item error"><span>Cardiologist Consult &mdash; Inpatient &nbsp; &#10060; <em>Denied: Related to excluded pre-existing condition</em></span><span>$1,200.00 denied</span></div>
    <div class="line-item flagged"><span>Balance bill from out-of-network ER physician group &nbsp; &#9888; <em>Balance billing not prohibited under short-term plan</em></span><span>$2,200.00 owed</span></div>
    <div class="line-total"><span>TOTAL PATIENT LIABILITY (after short-term plan &ldquo;coverage&rdquo;)</span><span>$11,800.00</span></div>
</div>

<h2 id="when-it-makes-sense">5. When a short-term plan actually makes sense</h2>

<p>Despite their limitations, short-term plans are appropriate in one specific scenario: a <strong>healthy person under 40 facing a coverage gap of fewer than 3 months</strong> who has no pre-existing conditions, no ongoing prescriptions, and no planned medical procedures. The clearest use case:</p>

<ul>
    <li>You are 27, healthy, between jobs, and start a new job in 6 weeks that includes employer health insurance.</li>
    <li>You have no chronic conditions, no current prescriptions, and no planned medical care.</li>
    <li>You primarily want protection against a catastrophic accident or sudden illness during the gap.</li>
    <li>You have confirmed that a marketplace Special Enrollment Period is not available or results in a higher total cost for a 6-week gap than a short-term plan.</li>
</ul>

<p>In this narrow scenario, a short-term plan&rsquo;s $100 to $200/month premium and high deductible provides some catastrophic protection at low cost. Outside this scenario&mdash;especially if you have any pre-existing conditions or the gap exceeds 90 days&mdash;a short-term plan&rsquo;s exclusions create more risk than they offset.</p>

<h2 id="alternatives">6. Alternatives to short-term health insurance</h2>

<table>
    <thead>
        <tr>
            <th>Alternative</th>
            <th>Best For</th>
            <th>Key Requirement</th>
            <th>Pre-existing Conditions?</th>
        </tr>
    </thead>
    <tbody>
        <tr><td>ACA Marketplace SEP</td><td>Anyone who lost job-based coverage</td><td>Loss of coverage = qualifying event (60-day window)</td><td>Covered</td></tr>
        <tr><td>Medicaid</td><td>Low-income individuals and families</td><td>Income at or below ~138% FPL; year-round enrollment</td><td>Covered</td></tr>
        <tr><td>COBRA</td><td>People who want to keep their exact plan and provider network</td><td>Must elect within 60 days of losing coverage</td><td>Covered (continuation of employer plan)</td></tr>
        <tr><td>Spouse&rsquo;s / parent&rsquo;s plan</td><td>Eligible dependents</td><td>Employer plan must allow mid-year additions on qualifying event</td><td>Covered</td></tr>
        <tr><td>Health sharing ministries</td><td>Healthy individuals with religious affiliation</td><td>Membership requirements; not insurance; significant coverage risks</td><td>Usually excluded</td></tr>
    </tbody>
</table>

<div class="guide-cta-inline">
    <p><strong>Not sure which coverage option is right for your gap situation?</strong> <a href="/scan">Upload your current coverage details to BillKarma</a>&mdash;we walk you through your options based on your specific situation, including ACA eligibility, Medicaid income thresholds, and COBRA timelines.</p>
</div>

<h2 id="claim-denied">7. What to do if your short-term plan claim is denied</h2>

<p>Short-term plans are not required to follow the ACA&rsquo;s internal appeals and external review requirements. Your rights are more limited than with ACA-compliant coverage&mdash;but you are not without options:</p>

<ol>
    <li><strong>Request the denial in writing with the specific exclusion cited.</strong> The insurer must give you the contractual basis for the denial. Get the exact language from the Evidence of Coverage document that they are relying on.</li>
    <li><strong>Review your application and health questionnaire answers.</strong> If the denial is based on a pre-existing condition you disclosed accurately and the plan accepted your enrollment, you have a basis to dispute the characterization.</li>
    <li><strong>File an internal appeal.</strong> Even though short-term plans are not required to have formal appeal processes, many offer one. Submit your physician&rsquo;s documentation that the condition being denied was not pre-existing.</li>
    <li><strong>File a complaint with your state insurance commissioner.</strong> State departments of insurance can investigate unfair claims practices. Even if short-term plans are exempt from ACA rules, they are still subject to state insurance laws prohibiting bad faith claims handling.</li>
    <li><strong>Consult a patient advocate or attorney.</strong> If the denied amount is large ($5,000+), a patient advocate or insurance bad-faith attorney can review whether the denial has a legal basis. Many work on contingency.</li>
</ol>

<h2 id="case-study">8. Real-world case study</h2>

<div class="case-study">
    <h3>Short-term plan denies $22,000 appendectomy &mdash; appeals process and state complaint recover $18,400</h3>
    <p>A 31-year-old teacher in Tennessee left her job in August and bought a short-term health plan for $148/month while she looked for a new teaching position. In September, she was rushed to the ER with acute appendicitis and underwent an emergency appendectomy. Hospital bill: <strong>$22,800</strong>.</p>
    <p>The short-term insurer denied the claim, citing a pre-existing condition: a prior ER visit for abdominal pain two years earlier that was ultimately diagnosed as a muscle strain. The insurer characterized this as evidence of &ldquo;pre-existing gastrointestinal symptoms.&rdquo;</p>
    <p>She filed an internal appeal with a letter from her surgeon explaining that appendicitis is an acute, unpredictable event with no relationship to prior abdominal pain episodes. The insurer denied the appeal. She filed a complaint with the Tennessee Department of Commerce and Insurance, citing bad faith claims handling. The state opened an investigation. After 60 days, the insurer agreed to pay <strong>$18,400</strong> of the $22,800 claim. She negotiated the remaining $4,400 balance directly with the hospital to $1,200. <strong>Total recovered through appeals and negotiation: $21,600.</strong></p>
</div>

<div class="key-takeaway">
    <strong>Got a denied claim from a short-term plan?</strong> <a href="/scan">Upload your denial letter to BillKarma</a>&mdash;we review the specific exclusion cited, identify whether the denial has a valid contractual basis, and help you prepare an appeal or state complaint.
</div>

<h2 id="faq">Frequently asked questions</h2>

<div class="faq-section">
    <div class="faq-item">
        <h3>What is short-term health insurance?</h3>
        <p>Short-term health insurance is a limited-duration medical plan designed to fill temporary coverage gaps. These plans are not subject to ACA consumer protections and do not count as minimum essential coverage. They typically cost $100 to $200 per month but exclude pre-existing conditions, mental health treatment, maternity care, and preventive services.</p>
    </div>
    <div class="faq-item">
        <h3>How long can a short-term health plan last in 2026?</h3>
        <p>Under the 2024 Biden administration rule, short-term plans are limited to an initial term of no more than 3 months, with a maximum total duration of 4 months including renewals. Some states ban short-term plans entirely, including California and New York.</p>
    </div>
    <div class="faq-item">
        <h3>Do short-term health plans cover pre-existing conditions?</h3>
        <p>No. Short-term plans are exempt from the ACA&rsquo;s pre-existing condition protections. Insurers can deny coverage, exclude specific conditions, or charge higher premiums based on your health history. Claims related to any condition the insurer classifies as pre-existing will be denied.</p>
    </div>
    <div class="faq-item">
        <h3>What happens if I get sick with a short-term health plan?</h3>
        <p>You face significant financial risk. Claim denial rates on short-term plans average 25 to 35%, compared to under 8% for ACA marketplace plans. Claims can be denied retroactively if the insurer determines the condition was pre-existing. Balance billing is common because many short-term plans have very limited networks.</p>
    </div>
    <div class="faq-item">
        <h3>What are the alternatives to short-term health insurance?</h3>
        <p>Before buying a short-term plan, consider: ACA Special Enrollment Period (triggered by job loss), Medicaid (year-round enrollment if income qualifies), COBRA (continues employer coverage for 18 months), or a spouse&rsquo;s employer plan. Each provides ACA-compliant coverage with pre-existing condition protections that short-term plans lack.</p>
    </div>
</div>

<h2 id="sources">Sources</h2>

<ul class="sources-list">
    <li><a href="https://www.kff.org/private-insurance/issue-brief/short-term-limited-duration-health-insurance/" target="_blank" rel="noopener">KFF: Short-Term Limited Duration Health Insurance</a></li>
    <li><a href="https://www.federalregister.gov/documents/2024/04/03/2024-06566/short-term-limited-duration-insurance" target="_blank" rel="noopener">Federal Register: 2024 Rule Limiting Short-Term Plan Duration</a></li>
    <li><a href="https://www.cms.gov/marketplace/technical-assistance-resources/special-enrollment-periods" target="_blank" rel="noopener">CMS: ACA Marketplace Special Enrollment Periods</a></li>
    <li><a href="https://www.healthcare.gov/glossary/minimum-essential-coverage/" target="_blank" rel="noopener">HealthCare.gov: Minimum Essential Coverage</a></li>
    <li><a href="https://www.dol.gov/general/topic/health-plans/cobra" target="_blank" rel="noopener">U.S. Department of Labor: COBRA Continuation Coverage</a></li>
    <li><a href="https://www.healthaffairs.org/doi/10.1377/hlthaff.2019.00234" target="_blank" rel="noopener">Health Affairs: Consumer Protections and Short-Term Health Plans</a></li>
</ul>
""",
})
