"""Guide: Medical Bills After a Car Accident."""

from guides import register, _embed

register("car-accident-medical-bills", {
    "title": "Medical Bills After a Car Accident: Who Pays",
    "meta_description": "After a car accident, medical bills can come from PIP, MedPay, at-fault insurance, or your health plan. Learn who pays, how subrogation works, and how to.",
    "published": "2026-02-26",
    "author": "BillKarma Team",
    "category": "Patient Rights",
    "faqs": [
        {
            "q": "Who pays my medical bills after a car accident?",
            "a": "It depends on your state and insurance coverage. In no-fault states, your own PIP (Personal Injury Protection) coverage pays first, regardless of who caused the accident. In at-fault states, the at-fault driver's liability insurance pays. MedPay (Medical Payments coverage) pays regardless of fault in both state types. Your health insurance can also be used, but your insurer may seek reimbursement from the at-fault party through subrogation.",
        },
        {
            "q": "What is PIP insurance and do I have to have it?",
            "a": "PIP (Personal Injury Protection) is insurance that pays your medical bills after a car accident regardless of who is at fault. It is required in the 12 no-fault states (Florida, Hawaii, Kansas, Kentucky, Massachusetts, Michigan, Minnesota, New Jersey, New York, North Dakota, Pennsylvania, Utah) and optional in many others. PIP typically covers $10,000-$50,000 in medical expenses, lost wages, and funeral costs.",
        },
        {
            "q": "What is subrogation and how does it affect me?",
            "a": "Subrogation is the process where your health insurance company seeks reimbursement from the at-fault driver's insurance after paying your medical bills. If your health insurer pays $30,000 for accident-related care and the at-fault driver's insurer later settles with you for $50,000, your health insurer can claim back the $30,000 from your settlement. This is why settlement amounts often seem large but the patient keeps less than expected.",
        },
        {
            "q": "Can a hospital put a lien on my accident settlement?",
            "a": "Yes. In most states, hospitals can file a medical lien against your personal injury settlement or judgment. This means the hospital gets paid from your settlement before you receive any money. Hospital liens are particularly common when patients are uninsured or when treatment exceeds PIP or MedPay limits. You can negotiate the lien amount, often reducing it by 25-50%.",
        },
        {
            "q": "Should I use my health insurance for car accident injuries?",
            "a": "Yes, in most cases. Using your health insurance gets you the benefit of negotiated in-network rates, which can be 40-70% lower than hospital chargemaster prices. Without insurance, hospitals may bill at full rates and place a lien on your settlement. The downside is subrogation: your health insurer may seek reimbursement from any settlement. Even so, the lower negotiated rates usually result in a better financial outcome.",
        },
    ],
    "body": f"""
<p class="lead">The average car accident injury claim involves <strong>$20,000&ndash;$50,000</strong> in medical bills. A serious crash with surgery, hospitalization, and rehabilitation can exceed <strong>$200,000</strong>. Who pays those bills&mdash;and in what order&mdash;depends on your state, your insurance coverage, and who was at fault. Getting this wrong can cost you tens of thousands of dollars. Here&rsquo;s how it works.</p>

<nav class="toc">
    <h2>In this guide</h2>
    <ol>
        <li><a href="#who-pays">Who pays: the coverage hierarchy</a></li>
        <li><a href="#no-fault-states">No-fault states and PIP coverage</a></li>
        <li><a href="#at-fault">At-fault states and liability claims</a></li>
        <li><a href="#subrogation">Health insurance subrogation explained</a></li>
        <li><a href="#liens">Hospital liens and provider liens</a></li>
        <li><a href="#negotiate">Negotiating your medical bills after an accident</a></li>
        <li><a href="#protect-yourself">Steps to protect yourself</a></li>
        <li><a href="#faq">Frequently asked questions</a></li>
        <li><a href="#sources">Sources</a></li>
    </ol>
</nav>

<h2 id="who-pays">1. Who pays: the coverage hierarchy</h2>

<p>After a car accident, multiple insurance sources may cover your medical bills. The order in which they pay depends on your state and what coverage you carry:</p>

<table>
    <thead>
        <tr><th>Coverage Type</th><th>Who Pays</th><th>Typical Limits</th><th>Fault Required?</th></tr>
    </thead>
    <tbody>
        <tr><td><strong>PIP</strong> (Personal Injury Protection)</td><td>Your own auto insurance</td><td>$10,000&ndash;$50,000</td><td>No</td></tr>
        <tr><td><strong>MedPay</strong> (Medical Payments)</td><td>Your own auto insurance</td><td>$1,000&ndash;$25,000</td><td>No</td></tr>
        <tr><td><strong>At-fault liability</strong></td><td>Other driver&rsquo;s auto insurance</td><td>$25,000&ndash;$300,000+</td><td>Yes</td></tr>
        <tr><td><strong>Health insurance</strong></td><td>Your health plan</td><td>Up to plan limits</td><td>No</td></tr>
        <tr><td><strong>Uninsured/underinsured motorist</strong></td><td>Your own auto insurance</td><td>$25,000&ndash;$300,000+</td><td>Other driver at fault but uninsured</td></tr>
    </tbody>
</table>

<p><strong>The typical payment order:</strong> PIP or MedPay pays first (no-fault coverage). If bills exceed those limits, your health insurance or the at-fault driver&rsquo;s liability insurance covers the remainder. If the other driver is uninsured, your uninsured motorist coverage kicks in.</p>

<div class="key-takeaway">
    <strong>Do not skip filing with your health insurance.</strong> Many accident victims avoid using health insurance, thinking the at-fault driver&rsquo;s insurer will pay everything. But liability claims take months to settle, and hospitals don&rsquo;t wait. Using your health insurance gets you in-network rates immediately and prevents collections while the liability claim is pending. For a primer on deductibles, coinsurance, and how claims flow, see <a href="/guides/how-health-insurance-works">our guide to how health insurance works</a>.
</div>

<h2 id="no-fault-states">2. No-fault states and PIP coverage</h2>

<p>In no-fault states, your own auto insurance pays your medical bills first, regardless of who caused the accident. This is called <strong>Personal Injury Protection (PIP)</strong>.</p>

<table>
    <thead>
        <tr><th>No-Fault State</th><th>Minimum PIP Requirement</th><th>Key Notes</th></tr>
    </thead>
    <tbody>
        <tr><td>Florida</td><td>$10,000</td><td>Must seek treatment within 14 days of accident</td></tr>
        <tr><td>Hawaii</td><td>$10,000</td><td>Covers medical, wage loss, funeral expenses</td></tr>
        <tr><td>Kansas</td><td>$4,500</td><td>Lower minimum; additional coverage recommended</td></tr>
        <tr><td>Kentucky</td><td>$10,000</td><td>Choice no-fault: can opt out of no-fault system</td></tr>
        <tr><td>Massachusetts</td><td>$8,000</td><td>Covers reasonable and necessary medical expenses</td></tr>
        <tr><td>Michigan</td><td>$50,000+</td><td>Highest PIP requirements; lifetime unlimited was standard until 2020 reform</td></tr>
        <tr><td>Minnesota</td><td>$40,000</td><td>Covers medical and rehabilitation expenses</td></tr>
        <tr><td>New Jersey</td><td>$15,000</td><td>Choice between standard and basic policies</td></tr>
        <tr><td>New York</td><td>$50,000</td><td>Covers medical, lost wages (80%), and other expenses</td></tr>
        <tr><td>North Dakota</td><td>$30,000</td><td>Covers medical and rehabilitation</td></tr>
        <tr><td>Pennsylvania</td><td>$5,000</td><td>Choice no-fault: can choose full tort or limited tort</td></tr>
        <tr><td>Utah</td><td>$3,000</td><td>Lowest minimum PIP requirement</td></tr>
    </tbody>
</table>

<p><strong>The PIP problem:</strong> PIP limits are often far too low for serious injuries. A single ER visit with imaging can use up $5,000&ndash;$10,000 of PIP coverage. If you need surgery, PIP may be exhausted within days. Once PIP runs out, remaining bills fall to your health insurance, MedPay, or the at-fault driver&rsquo;s liability coverage.</p>

<div class="case-study">
    <h3>Case study: $78,000 in medical bills after a rear-end collision in Florida</h3>
    <p><strong>Situation:</strong> Sarah was rear-ended at a stoplight in Florida. She suffered a herniated disc requiring surgery. Her medical bills totaled <strong>$78,000</strong>. Her PIP coverage was the Florida minimum: $10,000.</p>
    <p><strong>The payment breakdown:</strong></p>
    <ul>
        <li>PIP paid: <strong>$10,000</strong> (exhausted immediately on ER visit and initial imaging)</li>
        <li>Health insurance paid: <strong>$41,000</strong> at in-network negotiated rates (the hospital billed $58,000, but the allowed amount was $41,000)</li>
        <li>Sarah&rsquo;s health insurance cost-sharing: <strong>$6,200</strong> (deductible + coinsurance, up to her OOP max)</li>
        <li>At-fault driver&rsquo;s liability settlement: <strong>$95,000</strong></li>
    </ul>
    <p><strong>But then subrogation hit:</strong> Sarah&rsquo;s health insurer filed a subrogation claim for the $41,000 they paid, reducing her settlement by that amount. After attorney fees (33% = $31,350) and subrogation ($41,000), Sarah kept <strong>$22,650</strong> from the $95,000 settlement.</p>
    <p><strong>What saved her money:</strong> Sarah&rsquo;s attorney negotiated the subrogation claim down to $28,000 (a 32% reduction) and the hospital reduced a $4,500 outstanding balance to $2,200. <strong>Final net to Sarah: $33,450.</strong></p>
    <p>Before accepting any hospital bill at face value, <a href="/scan">upload it to BillKarma</a> to check for duplicate charges, upcoding, and inflated fees that inflate your lien or settlement deductions.</p>
</div>

{_embed(mode="cost", cpt="99284", title="Check your ER visit costs", subtitle="See what Medicare pays for your ER visit level.")}

<h2 id="at-fault">3. At-fault states and liability claims</h2>

<p>In the 38 at-fault (tort) states, the driver who caused the accident is financially responsible for the other party&rsquo;s medical bills through their <strong>bodily injury liability insurance</strong>.</p>

<p><strong>How a liability claim works:</strong></p>
<ol>
    <li>You file a claim with the at-fault driver&rsquo;s insurance company.</li>
    <li>The insurer investigates fault and reviews your medical records and bills.</li>
    <li>You negotiate a settlement that covers medical bills, lost wages, pain and suffering, and other damages.</li>
    <li>If you cannot agree, you may need to file a lawsuit before the statute of limitations expires (typically 2&ndash;4 years, varying by state).</li>
</ol>

<p><strong>The timing problem:</strong> Liability claims take <strong>3&ndash;18 months</strong> to settle. Your medical bills arrive in weeks. Hospitals and providers will not wait for your liability settlement&mdash;they will send bills to collections or place liens on your anticipated settlement. This is why using PIP, MedPay, or health insurance in the meantime is critical. Compare ER and hospital charges in your area using our <a href="/hospitals/">hospital directory</a> to know whether the facility&rsquo;s pricing is fair.</p>

<h2 id="subrogation">4. Health insurance subrogation explained</h2>

<p>Subrogation is the process where your health insurer recovers the money they paid for your accident-related care from the at-fault driver&rsquo;s insurance. It works like this:</p>

<ol>
    <li>You use your health insurance to pay for accident-related treatment.</li>
    <li>Your health insurer pays the providers at negotiated rates.</li>
    <li>You settle with the at-fault driver&rsquo;s insurance for your damages.</li>
    <li>Your health insurer files a subrogation claim against your settlement to recover what they paid.</li>
</ol>

<p><strong>Can you reduce a subrogation claim?</strong> Often, yes. Many states have laws limiting subrogation, and your attorney can negotiate the amount down. Common reduction strategies include:</p>

<ul>
    <li><strong>The &ldquo;made whole&rdquo; doctrine:</strong> In many states, the insurer cannot subrogate unless you have been fully compensated (&ldquo;made whole&rdquo;) for all your damages.</li>
    <li><strong>Common fund doctrine:</strong> If your attorney recovered the settlement, the insurer may be required to pay a proportionate share of attorney fees, reducing the subrogation amount by one-third.</li>
    <li><strong>Direct negotiation:</strong> Insurers often accept 50&ndash;70% of the subrogation amount to avoid litigation.</li>
</ul>

<h2 id="liens">5. Hospital liens and provider liens</h2>

<p>When a hospital treats a car accident patient, they may file a <strong>hospital lien</strong> against any future personal injury settlement or judgment. This gives the hospital a legal right to be paid from your settlement before you receive money.</p>

<p><strong>Key facts about medical liens:</strong></p>
<ul>
    <li>Most states allow hospital liens, though rules vary on filing procedures and limits.</li>
    <li>Some states cap lien amounts at a percentage of the settlement (often 33&ndash;50%).</li>
    <li>Liens can be negotiated. Hospitals frequently accept 50&ndash;75% of the lien amount to avoid a lengthy legal fight. See <a href="/guides/how-to-negotiate-medical-bills">our guide to negotiating medical bills</a> for proven strategies.</li>
    <li>If you have health insurance, using it instead of being billed at chargemaster rates can dramatically reduce the lien amount (in-network rates are 40&ndash;70% lower). Check your hospital&rsquo;s pricing patterns in our <a href="/hospitals/">hospital pricing directory</a>.</li>
</ul>

<div class="key-takeaway">
    <strong>Liens eat into your settlement.</strong> A $100,000 settlement can shrink fast: attorney fees (33% = $33,333) + hospital lien ($30,000) + health insurance subrogation ($20,000) = $83,333 in deductions, leaving you $16,667. Negotiating liens and subrogation claims is essential&mdash;this is why having an experienced personal injury attorney matters.
</div>

<h2 id="negotiate">6. Negotiating your medical bills after an accident</h2>

<p><strong>Always use health insurance when possible.</strong> In-network rates are dramatically lower than chargemaster prices. A hospital might bill $45,000 for a surgery, but the health insurance allowed amount might be $18,000. Using health insurance means a smaller subrogation claim later. Use our <a href="/calculator">cost calculator</a> to look up what Medicare pays for each procedure on your bill&mdash;this gives you a fair-market benchmark for negotiating liens.</p>

<p><strong>Audit every bill.</strong> Accident-related medical bills are prone to the same errors as any medical bill: duplicate charges, upcoding, unbundled lab tests, and inflated supply charges. <a href="/scan">Upload your bills to BillKarma</a> to catch errors before they become part of a lien or settlement calculation.</p>

<p><strong>Negotiate liens before settling.</strong> Contact the hospital lien holder before you finalize a settlement and negotiate a reduction. Hospitals know that if the case goes to trial and the patient loses, the lien may be worthless. This gives you leverage.</p>

<p><strong>Negotiate subrogation with your health insurer.</strong> Your attorney can argue for a reduction based on the made-whole doctrine, common fund doctrine, or state-specific limitations on subrogation.</p>

<p><strong>Keep records of everything.</strong> Document all medical visits, bills, payments, insurance correspondence, and settlement negotiations. A detailed paper trail strengthens your position in every negotiation.</p>

<h2 id="protect-yourself">7. Steps to protect yourself</h2>

<ol>
    <li><strong>File a police report at the scene.</strong> This documents the accident and establishes fault, which is critical for any liability claim.</li>
    <li><strong>Seek medical attention within 72 hours.</strong> Delayed treatment weakens your injury claim. In Florida, PIP requires treatment within 14 days.</li>
    <li><strong>Use your PIP/MedPay first.</strong> These pay regardless of fault with no subrogation in most states.</li>
    <li><strong>File with your health insurance.</strong> This gets you negotiated rates and prevents collections during the months-long liability claim process. If you received out-of-network emergency care, the <a href="/guides/no-surprises-act">No Surprises Act</a> may protect you from balance billing.</li>
    <li><strong>Do not give a recorded statement to the other driver&rsquo;s insurer</strong> without consulting an attorney. Anything you say can be used to deny or reduce your claim.</li>
    <li><strong>Do not sign medical record releases</strong> from the other driver&rsquo;s insurance company. They may use your full medical history to argue that your injuries were pre-existing.</li>
    <li><strong>Consult a personal injury attorney for claims over $10,000.</strong> Attorney fees (typically 33%) are usually more than offset by higher settlements and reduced liens.</li>
    <li><strong>Be aware of the statute of limitations.</strong> Each state sets a deadline for filing a personal injury lawsuit, typically 2&ndash;4 years from the accident date. Missing this deadline forfeits your right to sue.</li>
</ol>

<div class="key-takeaway">
    <strong>The biggest mistake after a car accident:</strong> Not using health insurance because you assume the other driver&rsquo;s insurance will cover everything. Liability claims take months. Hospitals send bills to collections in weeks. Use every coverage source available to you&mdash;PIP, MedPay, and health insurance&mdash;while the liability claim is pending. <a href="/scan">Scan every bill with BillKarma</a> to ensure you are only paying for accurate, legitimate charges.
</div>

<h2 id="faq">Frequently asked questions</h2>

<div class="faq-section">
    <div class="faq-item">
        <h3>Who pays my medical bills after a car accident?</h3>
        <p>In no-fault states, your PIP coverage pays first regardless of fault. In at-fault states, the at-fault driver&rsquo;s liability insurance pays. MedPay covers you regardless of fault in both state types. Health insurance can also be used, though the insurer may seek reimbursement from the at-fault party through subrogation.</p>
    </div>

    <div class="faq-item">
        <h3>What is PIP insurance and do I have to have it?</h3>
        <p>PIP (Personal Injury Protection) pays your medical bills after an accident regardless of fault. It is required in the 12 no-fault states and optional in many others. PIP limits range from $3,000 (Utah) to $50,000+ (Michigan, New York), and can be exhausted quickly with serious injuries.</p>
    </div>

    <div class="faq-item">
        <h3>What is subrogation and how does it affect me?</h3>
        <p>Subrogation is when your health insurer recovers money they paid for your accident care from the at-fault driver&rsquo;s insurance or your settlement. It reduces the amount you keep from a settlement. Subrogation claims can often be negotiated down by 30&ndash;50% through legal doctrines like made-whole and common fund.</p>
    </div>

    <div class="faq-item">
        <h3>Can a hospital put a lien on my accident settlement?</h3>
        <p>Yes. Most states allow hospital liens on personal injury settlements. The lien amount can often be negotiated down by 25&ndash;50%. Using health insurance instead of being billed at full chargemaster rates significantly reduces the potential lien amount.</p>
    </div>

    <div class="faq-item">
        <h3>Should I use my health insurance for car accident injuries?</h3>
        <p>Yes. Health insurance gets you lower negotiated rates (40&ndash;70% less than chargemaster prices), prevents collections while a liability claim is pending, and usually results in a better overall financial outcome even after subrogation. Always file with PIP or MedPay first if available.</p>
    </div>
</div>

<h2 id="sources">Sources</h2>

<ul class="sources-list">
    <li><a href="#" target="_blank" rel="noopener">Insurance Information Institute: Auto Insurance Basics and No-Fault Laws</a></li>
    <li><a href="#" target="_blank" rel="noopener">National Association of Insurance Commissioners: PIP Coverage by State</a></li>
    <li><a href="#" target="_blank" rel="noopener">American Bar Association: Understanding Subrogation in Personal Injury Cases</a></li>
    <li><a href="#" target="_blank" rel="noopener">National Conference of State Legislatures: Auto Insurance Statute of Limitations by State</a></li>
    <li><a href="#" target="_blank" rel="noopener">Insurance Research Council: Auto Injury Insurance Claims Study (2025)</a></li>
    <li><a href="#" target="_blank" rel="noopener">Centers for Disease Control and Prevention: Motor Vehicle Crash Injuries and Costs</a></li>
</ul>
""",
})
