"""Guide: Balance Billing — What It Is, When It's Illegal, and What to Do."""

from guides import register, _embed

register("balance-billing", {
    "title": "Balance Billing: What It Is, When It's Illegal, and What to Do",
    "meta_description": "Balance billing happens when out-of-network providers charge you the gap between their fee and your insurer's payment.",
    "published": "2026-02-19",
    "author": "BillKarma Team",
    "category": "Patient Rights",
    "faqs": [
        {
            "q": "What is balance billing?",
            "a": "Balance billing is when a healthcare provider bills you for the difference between their full charge and what your insurance paid. For example, if a provider charges $1,000, your insurer pays $600, and the provider bills you the remaining $400 — that $400 'balance' is a balance bill. In-network providers cannot balance bill you (their contract requires them to accept the negotiated rate). Out-of-network providers historically could, but the No Surprises Act now restricts this significantly.",
        },
        {
            "q": "Is balance billing illegal?",
            "a": "It depends on the situation. For in-network providers, balance billing is generally prohibited by their contract with your insurer. For out-of-network providers, the No Surprises Act (effective January 1, 2022) prohibits balance billing for emergency services, for non-emergency services from out-of-network providers at in-network facilities (when you didn't choose the out-of-network provider), and for air ambulance services. Balance billing from ground ambulance providers and from out-of-network facilities you chose is still generally legal.",
        },
        {
            "q": "Can I be balance billed by an in-network provider?",
            "a": "Legitimate balance bills from in-network providers should not happen — they're contractually required to accept your insurer's negotiated rate as payment in full. However, patients sometimes receive what looks like a balance bill from in-network providers due to billing errors: a service was miscoded and processed incorrectly, or the provider's claim was processed at out-of-network rates by mistake. Always check your EOB to confirm how the claim was processed before paying.",
        },
        {
            "q": "Does the No Surprises Act cover ground ambulance balance bills?",
            "a": "No. Ground ambulance is specifically excluded from the No Surprises Act. This is one of the most significant gaps in the law. Ground ambulance bills can be very large ($1,200-$2,500 or more) and providers frequently balance bill when insurers pay less than the full charge. Some states have their own ground ambulance billing protections — check with your state insurance commissioner. For unprotected ground ambulance bills, negotiating directly with the ambulance company is often your best option.",
        },
        {
            "q": "What should I do if I receive a balance bill that may violate the No Surprises Act?",
            "a": "First, confirm that your situation is covered by the NSA (emergency care, or out-of-network provider at an in-network facility for a scheduled procedure). Then contact your insurer and report that you received a balance bill. Your insurer is responsible for ensuring you pay only your in-network cost-sharing. If the insurer doesn't resolve it, file a complaint with CMS at 1-800-985-3059 or online at cms.gov/nosurprises. Also contact your state insurance commissioner.",
        },
        {
            "q": "Can I sign away my No Surprises Act protections?",
            "a": "Only in limited circumstances. For non-emergency care, a provider can ask you to waive NSA protections and consent to out-of-network billing — but only if they gave you written notice at least 72 hours before the service (or 3 hours if scheduled within 72 hours), told you your estimated cost, and confirmed that in-network alternatives are available. Providers cannot ask you to waive NSA protections for emergency care at all. A generic consent form signed at hospital admission is not a valid NSA waiver.",
        },
    ],
    "body": f"""
<p class="lead">Before 2022, 1 in 6 emergency room visits resulted in at least one out-of-network charge, according to a <em>Health Affairs</em> study &mdash; even when the patient specifically chose an in-network hospital. The average surprise out-of-network bill was <strong>$628</strong>, on top of the regular cost-sharing. The No Surprises Act changed the rules significantly, but balance billing hasn&rsquo;t disappeared. Here&rsquo;s what you need to know.</p>

<nav class="toc">
    <h2>In this guide</h2>
    <ol>
        <li><a href="#what-is-balance-billing">What is balance billing?</a></li>
        <li><a href="#when-legal">When is balance billing legal?</a></li>
        <li><a href="#no-surprises-act">No Surprises Act protections</a></li>
        <li><a href="#gaps">Gaps in the law: what NSA doesn&rsquo;t cover</a></li>
        <li><a href="#state-protections">State balance billing protections</a></li>
        <li><a href="#how-to-fight">What to do if you receive a balance bill</a></li>
        <li><a href="#case-studies">Case studies: balance billing disputes</a></li>
        <li><a href="#faq">Frequently asked questions</a></li>
        <li><a href="#sources">Sources</a></li>
    </ol>
</nav>

<h2 id="what-is-balance-billing">1. What is balance billing?</h2>

<p>When you receive medical care, there&rsquo;s typically a gap between what the provider charges and what your insurance actually pays. For an in-network provider, your insurer has a contract that sets a negotiated rate &mdash; and the provider has agreed to accept that rate as payment in full. The patient owes only their contracted cost-sharing (copay, deductible, coinsurance).</p>

<p>For an <strong>out-of-network provider</strong>, there is no such contract. The insurer pays based on their own reimbursement schedule (typically some multiple of the Medicare rate or a percentage of &ldquo;usual and customary&rdquo; charges). The provider receives that payment and may then bill the patient for the remaining &ldquo;balance&rdquo; &mdash; the gap between their full charge and what the insurer paid.</p>

<div class="bill-example">
    <div class="bill-header">How Balance Billing Works: Example</div>
    <div class="line-item">
        <span>Provider&rsquo;s full charge</span>
        <span>$2,400.00</span>
    </div>
    <div class="line-item">
        <span>Insurer&rsquo;s payment (out-of-network rate)</span>
        <span>$820.00</span>
    </div>
    <div class="line-item">
        <span>Patient cost-sharing applied by insurer (20% coinsurance)</span>
        <span>$164.00</span>
    </div>
    <div class="line-item error">
        <span>Balance bill from provider &nbsp; &#10060; <em>The remaining gap billed directly to you</em></span>
        <span>$1,416.00</span>
    </div>
    <div class="line-total">
        <span>TOTAL PATIENT COST (cost-sharing + balance bill)</span>
        <span>$1,580.00</span>
    </div>
</div>

<p>In this example, a patient who expected to pay $164 in cost-sharing receives an additional $1,416 balance bill &mdash; nearly 10x what they anticipated. This was the standard experience for millions of Americans before 2022.</p>

<div class="key-takeaway">
    <strong>Balance billing is not a billing error &mdash; it&rsquo;s a billing practice.</strong> It is legal in many circumstances. The question is whether it applies to your specific situation and whether you have legal protection against it.
</div>

<h2 id="when-legal">2. When is balance billing legal?</h2>

<p>The legality of a balance bill depends on three factors: the provider&rsquo;s network status, the type of service, and whether federal or state law prohibits it.</p>

<table>
    <thead>
        <tr><th>Situation</th><th>Can Provider Balance Bill?</th></tr>
    </thead>
    <tbody>
        <tr><td>In-network provider, any service</td><td>No &mdash; contractually prohibited</td></tr>
        <tr><td>Out-of-network provider, emergency service</td><td>No &mdash; prohibited by No Surprises Act</td></tr>
        <tr><td>Out-of-network provider at in-network facility, scheduled service (patient did not choose the provider)</td><td>No &mdash; prohibited by No Surprises Act</td></tr>
        <tr><td>Out-of-network air ambulance at in-network facility</td><td>No &mdash; prohibited by No Surprises Act</td></tr>
        <tr><td>Ground ambulance, out-of-network</td><td>Yes &mdash; not covered by No Surprises Act (federal)</td></tr>
        <tr><td>Out-of-network provider at out-of-network facility the patient chose</td><td>Generally yes &mdash; unless state law applies</td></tr>
        <tr><td>Out-of-network provider patient specifically requested (with valid written consent)</td><td>Yes &mdash; NSA allows patient-initiated waiver for scheduled care</td></tr>
    </tbody>
</table>

<h2 id="no-surprises-act">3. No Surprises Act protections</h2>

<p>The <strong>No Surprises Act (NSA)</strong>, which took effect January 1, 2022, created the first comprehensive federal protections against surprise balance billing. Here&rsquo;s what it covers:</p>

<h3>Emergency services</h3>
<p>For any emergency medical service at any facility, insurers must reimburse out-of-network providers at the greater of: (1) the insurer&rsquo;s median in-network rate, (2) the out-of-network rate established by the state, or (3) the &ldquo;qualifying payment amount.&rdquo; Providers cannot bill patients more than their in-network cost-sharing amount for emergency care. This protection applies regardless of where the emergency occurs &mdash; the ER does not need to be in-network.</p>

<h3>Non-emergency services at in-network facilities</h3>
<p>When you choose an in-network hospital, surgery center, or other facility for a scheduled procedure, any provider at that facility who participates in your care &mdash; but who is out-of-network &mdash; cannot balance bill you. This covers the anesthesiologist you didn&rsquo;t choose, the assistant surgeon, the radiologist who reads your imaging, and any other &ldquo;facility-based provider.&rdquo;</p>

<p>There is one exception: if that out-of-network provider gave you written notice at least 72 hours before your scheduled appointment (or 3 hours before if scheduled same-day), disclosed their estimated cost, and got your written consent to out-of-network billing, the balance bill may be valid. But the notice and consent requirements are strict &mdash; a generic hospital admission consent form does not count.</p>

<h3>Air ambulance</h3>
<p>Out-of-network air ambulance providers (fixed-wing and helicopter) are prohibited from balance billing patients when transporting them from a covered facility. The NSA applies to air ambulance services from any out-of-network provider when the patient is transported from a participating hospital or emergency situation.</p>

<h3>What the NSA requires of providers and insurers</h3>
<ul>
    <li>Providers must give patients notice of their NSA rights at the time of scheduling.</li>
    <li>Insurers must process claims from out-of-network providers subject to NSA at in-network cost-sharing rates.</li>
    <li>If a provider disputes the insurer&rsquo;s payment amount, they must use the federal independent dispute resolution (IDR) process &mdash; not bill the patient. The patient&rsquo;s cost-sharing is fixed at the in-network level regardless of the IDR outcome.</li>
</ul>

<div class="key-takeaway">
    <strong>Not sure if your provider is in-network?</strong> Check our <a href="/hospitals/">hospital directory</a> for network and transparency data &mdash; and if you&rsquo;ve already received a surprise bill, <a href="/scan">upload it to BillKarma</a> so we can flag whether charges were processed at the right rates.
</div>

<h2 id="gaps">4. Gaps in the law: what NSA doesn&rsquo;t cover</h2>

<h3>Ground ambulance (the biggest gap)</h3>
<p>Ground ambulance is explicitly excluded from the No Surprises Act. This is a significant protection gap because ground ambulance bills are often very large, and balance billing is common. Average ground ambulance transport costs $1,200&ndash;$2,500. Many insurers pay only $200&ndash;$600 based on their fee schedules. The remaining balance &mdash; sometimes $1,000 or more &mdash; can be billed directly to the patient.</p>

<p>Congress created the Ground Ambulance and Patient Billing (GAPAB) advisory committee under the NSA to study this issue and make recommendations. As of early 2026, no federal ground ambulance balance billing protection has been enacted. Some states have enacted their own protections &mdash; see the state section below.</p>

<h3>Out-of-network facilities the patient chose</h3>
<p>If you chose to go to an out-of-network facility, the NSA&rsquo;s facility-based provider protections don&rsquo;t automatically apply. You may still have rights under state law or through your insurer&rsquo;s out-of-network coverage, but the federal surprise billing ban was designed for situations where the out-of-network element was not a patient choice.</p>

<h3>Self-pay and uninsured patients</h3>
<p>The NSA&rsquo;s balance billing protections apply to patients with insurance coverage. Uninsured patients are addressed separately by the NSA&rsquo;s &ldquo;good faith estimate&rdquo; requirement (providers must give uninsured and self-pay patients a written cost estimate before a scheduled service), but uninsured patients are not protected from being billed the full chargemaster rate.</p>

<h2 id="state-protections">5. State balance billing protections</h2>

<p>Many states enacted balance billing protections before the NSA, and state laws can supplement federal protections &mdash; including for ground ambulance and other areas the NSA doesn&rsquo;t cover. Federal and state protections can coexist; patients generally receive whichever protection is more favorable.</p>

<table>
    <thead>
        <tr><th>State</th><th>Key Protection Beyond Federal NSA</th></tr>
    </thead>
    <tbody>
        <tr><td>California</td><td>Comprehensive protections since 2017; covers ground ambulance in most cases; holds harmless standard for in-network facilities</td></tr>
        <tr><td>New York</td><td>Surprise bill law since 2015; covers emergency and some elective services; includes arbitration for disputed amounts</td></tr>
        <tr><td>Texas</td><td>Balance billing protections for certain emergency and facility-based care; IDR process established before federal NSA</td></tr>
        <tr><td>Colorado</td><td>Surprise billing protections including for ground ambulance in certain situations</td></tr>
        <tr><td>Illinois</td><td>State surprise billing law covering emergency and non-emergency out-of-network provider situations</td></tr>
        <tr><td>Florida</td><td>Balance billing protections for HMO plan members; additional state consumer protections</td></tr>
    </tbody>
</table>

<p>To find your state&rsquo;s specific protections, contact your state insurance commissioner&rsquo;s office or visit the NCSL health insurance page. State rules vary significantly in scope and enforcement.</p>

<h2 id="how-to-fight">6. What to do if you receive a balance bill</h2>

<h3>Step 1: Identify whether NSA (or state law) applies</h3>
<p>Ask yourself: Was the service an emergency? Was the service from an out-of-network provider at an in-network facility that I chose? If either is true, you may have federal NSA protection. Was the service a ground ambulance, or did you specifically choose an out-of-network facility? If so, look to state law.</p>

<h3>Step 2: Check your Explanation of Benefits</h3>
<p>Pull the EOB for the service date and confirm how the claim was processed. Did your insurer apply in-network or out-of-network cost-sharing? If the insurer processed it at in-network rates (as required by NSA), and you&rsquo;re still receiving a bill for more than your EOB shows as patient responsibility, the balance bill may be improper. See our <a href="/guides/understanding-your-explanation-of-benefits">EOB guide</a> for help reading yours.</p>

<h3>Step 3: Contact your insurer</h3>
<p>Call member services on your insurance card and say: &ldquo;I received a balance bill for [date of service] from [provider]. I believe this may violate the No Surprises Act because [the facility was in-network / it was an emergency]. Can you confirm how this claim should be processed and whether the balance bill is appropriate?&rdquo;</p>

<h3>Step 4: File a federal complaint</h3>
<p>If your insurer doesn&rsquo;t resolve it, file a complaint with the federal No Surprises Help Desk:</p>
<ul>
    <li><strong>Phone:</strong> 1-800-985-3059</li>
    <li><strong>Online:</strong> <a href="https://www.cms.gov/nosurprises" target="_blank" rel="noopener">cms.gov/nosurprises</a></li>
</ul>
<p>CMS can investigate violations and penalize providers who improperly balance bill patients subject to NSA protections.</p>

<h3>Step 5: File a state complaint</h3>
<p>File a complaint with your state insurance commissioner&rsquo;s office, especially for ground ambulance or situations where state law may provide additional protections. State regulators can investigate and act even on situations where federal NSA is silent.</p>

<div class="key-takeaway">
    <strong>Do not pay a balance bill while you&rsquo;re investigating it.</strong> Tell the provider you are reviewing the bill for compliance with the No Surprises Act. Ask them to hold the account from collections during the review period. Most providers will comply with a reasonable request while a formal dispute is pending.
</div>

<div class="key-takeaway">
    <strong>Have an unexpected bill in hand?</strong> <a href="/scan">Scan it with BillKarma</a> first &mdash; we identify whether charges were processed at in-network or out-of-network rates and flag any other billing discrepancies before you make your first call.
</div>

<div class="case-study">
    <h3>Case Study 1: ER anesthesiologist balance bill — $1,920 eliminated</h3>
    <p>A patient went to an in-network hospital ER with a broken wrist requiring surgery. The hospital and surgeon were both in-network. After surgery, she received a separate bill from the anesthesiology group for $1,920 &mdash; citing that the anesthesiologist was out-of-network.</p>
    <p>She called her insurer, which confirmed the surgery was for an emergency condition at an in-network facility. Under the No Surprises Act, the anesthesiologist could not balance bill her for more than her in-network specialist cost-sharing. Her insurer reprocessed the anesthesia claim at in-network rates. Her actual cost-sharing for the anesthesia: <strong>her $200 copay. Total savings: $1,720.</strong></p>
</div>

<div class="case-study">
    <h3>Case Study 2: Ground ambulance balance bill — $840 negotiated down</h3>
    <p>A patient was transported to the hospital by ground ambulance after a car accident. The ambulance company was out-of-network. His insurer paid $380 toward the $1,220 total charge. The ambulance company sent him a balance bill for $840.</p>
    <p>Ground ambulance is not covered by the No Surprises Act, and his state had no additional protection. He called the ambulance company, explained that the charge was unexpected and a financial hardship, and asked for a reduction. The company offered to settle for $280 (the difference between their charge and the Medicare rate for the same transport) as a &ldquo;Medicare rate adjustment.&rdquo; He accepted. <strong>Savings: $560.</strong></p>
    <p>This case illustrates a useful strategy for unprotected balance bills: ask for the &ldquo;Medicare rate&rdquo; as a negotiating anchor. Many providers will accept it rather than send a small amount to collections.</p>
</div>

<div class="case-study">
    <h3>Case Study 3: In-network provider processed incorrectly — $590 billing error</h3>
    <p>A patient received a $590 &ldquo;balance bill&rdquo; from her in-network cardiologist. Her insurer&rsquo;s EOB showed the claim had been processed at out-of-network rates &mdash; which made no sense since the cardiologist was contracted in-network. She called the cardiologist&rsquo;s billing department, which discovered they had submitted the claim under a different NPI number (the physician&rsquo;s personal NPI instead of the group&rsquo;s NPI), and the insurer didn&rsquo;t recognize it as an in-network provider.</p>
    <p>The billing department resubmitted with the correct NPI. The insurer processed at in-network rates. <strong>The $590 balance bill became a $0 balance.</strong></p>
    <p>This is a common reason in-network patients receive unexpected bills &mdash; the claim was submitted or processed incorrectly. Always check your EOB before paying any bill that surprises you.</p>
</div>

{_embed(mode="markup", title="Check if your charge is reasonable", subtitle="Enter the CPT code and charged amount to compare against Medicare rates.", height="420")}

<h2 id="faq">Frequently asked questions</h2>

<div class="faq-section">
    <div class="faq-item">
        <h3>What is balance billing?</h3>
        <p>Balance billing is when a provider bills you for the gap between their full charge and what your insurer paid. In-network providers cannot balance bill you (they accept the negotiated rate). Out-of-network providers could historically, but the No Surprises Act now prohibits it for most emergency care and non-emergency care from out-of-network providers at in-network facilities.</p>
    </div>

    <div class="faq-item">
        <h3>Is balance billing illegal?</h3>
        <p>It depends. Balance billing from in-network providers is contractually prohibited. Balance billing from out-of-network providers is prohibited by the No Surprises Act for emergency services, non-emergency services at in-network facilities, and air ambulance. Ground ambulance and out-of-network facilities the patient chose are generally not covered. State laws vary and may provide additional protections.</p>
    </div>

    <div class="faq-item">
        <h3>Can I be balance billed by an in-network provider?</h3>
        <p>In-network providers should not balance bill you &mdash; their contract requires them to accept the negotiated rate. If you receive what looks like a balance bill from an in-network provider, check your EOB to confirm the claim was processed at in-network rates. It may be a billing error (wrong NPI submitted, claim processed incorrectly) rather than an intentional balance bill.</p>
    </div>

    <div class="faq-item">
        <h3>Does the No Surprises Act cover ground ambulance balance bills?</h3>
        <p>No. Ground ambulance is specifically excluded from the NSA. This remains a significant protection gap. If you receive a ground ambulance balance bill, check your state&rsquo;s insurance laws &mdash; some states have their own protections. If not, negotiate directly with the ambulance company using the Medicare rate as a reference point.</p>
    </div>

    <div class="faq-item">
        <h3>What should I do if I receive a balance bill that may violate the No Surprises Act?</h3>
        <p>Contact your insurer to report the balance bill. If the insurer doesn&rsquo;t resolve it, file a complaint at <a href="https://www.cms.gov/nosurprises" target="_blank" rel="noopener">cms.gov/nosurprises</a> or call 1-800-985-3059. Also contact your state insurance commissioner. Do not pay while the dispute is pending &mdash; ask the provider to hold the account from collections during your review.</p>
    </div>

    <div class="faq-item">
        <h3>Can I sign away my No Surprises Act protections?</h3>
        <p>Only under specific conditions for non-emergency scheduled care: the provider must give written notice at least 72 hours before the service, disclose the estimated cost, and confirm that in-network alternatives are available. Emergency care waivers are never valid. A generic hospital admission form is not a valid NSA waiver.</p>
    </div>
</div>

<h2 id="sources">Sources</h2>

<ul class="sources-list">
    <li><a href="https://www.healthaffairs.org/doi/10.1377/hlthaff.2019.01451" target="_blank" rel="noopener">Health Affairs: Surprise Medical Bills and Out-of-Network Charges (2020)</a></li>
    <li><a href="https://www.cms.gov/nosurprises" target="_blank" rel="noopener">CMS: No Surprises Act Patient Protections</a></li>
    <li><a href="https://www.cms.gov/regulations-and-guidance/legislation/paperreductionactof1995/pra-listing/cms-10719" target="_blank" rel="noopener">CMS: No Surprises Act Complaint Process</a></li>
    <li><a href="https://www.kff.org/health-costs/issue-brief/no-surprises-act-implementation/" target="_blank" rel="noopener">KFF: No Surprises Act — Implementation and Patient Experiences (2024)</a></li>
    <li><a href="https://www.ncsl.org/health/balance-billing-protections-state-laws" target="_blank" rel="noopener">NCSL: State Balance Billing Laws</a></li>
    <li><a href="https://www.cms.gov/files/document/ground-ambulance-advisory-committee-recommendations.pdf" target="_blank" rel="noopener">CMS: Ground Ambulance and Patient Billing Advisory Committee Report</a></li>
</ul>
""",
})
