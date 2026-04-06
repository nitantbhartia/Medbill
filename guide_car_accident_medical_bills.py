"""Guide: Car Accident Medical Bills: Who Pays & How It Works (2026)."""

from guides import register, _embed

register("car-accident-medical-bills", {
    "title": "Car Accident Medical Bills: Who Pays & How It Works (2026)",
    "meta_description": "Car accident medical bills average $18,500 and 34% contain billing errors. Learn who pays first, how PIP and MedPay work, and how to manage bills while your case is open.",
    "published": "2026-04-05",
    "author": "BillKarma Team",
    "category": "Understanding Your Bill",
    "faqs": [
        {
            "q": "Who pays my medical bills after a car accident?",
            "a": "Who pays first depends on whether you live in a no-fault or at-fault state. In the 12 no-fault states, your own Personal Injury Protection (PIP) insurance pays your medical bills first, regardless of who caused the accident. In at-fault states, the at-fault driver&rsquo;s liability insurance is ultimately responsible, but you may use your own MedPay or health insurance in the interim. In both cases, if your medical bills exceed insurance limits and you have a personal injury claim, you may recover additional compensation through a settlement or lawsuit.",
        },
        {
            "q": "What is PIP (Personal Injury Protection) insurance?",
            "a": "Personal Injury Protection (PIP) is a type of auto insurance that covers your medical bills regardless of who caused the accident. It is mandatory in the 12 no-fault states (Florida, Michigan, New York, New Jersey, Pennsylvania, Hawaii, Kansas, Kentucky, Massachusetts, Minnesota, North Dakota, Utah) and optional in many others. PIP typically covers $10,000 to $50,000 in medical expenses per person, plus lost wages and other expenses. It pays quickly&mdash;without waiting for fault to be determined&mdash;making it valuable for covering immediate medical costs.",
        },
        {
            "q": "What is subrogation and how does it affect my car accident settlement?",
            "a": "Subrogation is the legal right of your health insurer to be repaid from any settlement or judgment you receive if they paid your medical bills after the accident. For example, if your health insurance paid $15,000 in medical bills and you later receive a $40,000 settlement from the at-fault driver, your health insurer can claim up to $15,000 of that settlement. Your attorney can often negotiate a reduction of the subrogation lien, especially if your total damages exceed the at-fault driver&rsquo;s insurance limits.",
        },
        {
            "q": "What is a letter of protection in a personal injury case?",
            "a": "A letter of protection (LOP) is a document your personal injury attorney sends to a medical provider guaranteeing payment from any future settlement or judgment. The provider treats you now and waits for payment. This allows accident victims to receive needed medical care even when they have no insurance or have exhausted PIP limits. However, if your case does not settle or settles for less than expected, you are still personally liable for those medical bills.",
        },
        {
            "q": "Should I use my health insurance or auto insurance for car accident medical bills?",
            "a": "Use whatever pays first and covers the most. In no-fault states, PIP pays first&mdash;use it. In at-fault states, if you have MedPay, use it for immediate bills. If you have health insurance, it can pay what PIP or MedPay do not cover. The key is not to ignore bills while waiting for an at-fault driver&rsquo;s insurer to accept liability&mdash;that can take months. Use available coverage now and sort out reimbursement later through your attorney or insurer&rsquo;s subrogation process.",
        },
    ],
    "body": f"""
<p class="lead">Car accident medical billing is unlike any other healthcare billing situation. The average car accident generates <strong>$18,500 in medical bills</strong>&mdash;and BillKarma data shows <strong>34% of those bills contain errors</strong>, often inflated charges that appear when providers know a personal injury case is involved. Who pays your bills, in what order, and how much you ultimately owe depends on your state, your auto insurance coverage, and whether you have health insurance. This guide explains every piece of the puzzle.</p>

<div class="answer-box">
    <strong>Quick answer:</strong> In no-fault states (12 states), your own PIP auto insurance pays first. In at-fault states, the at-fault driver&rsquo;s liability insurance is responsible, but you&rsquo;ll use your own MedPay or health insurance in the interim. Don&rsquo;t ignore bills while waiting for the case to resolve&mdash;document everything and keep every provider informed that a PI case is pending.
</div>

<nav class="toc">
    <h2>In this guide</h2>
    <ol>
        <li><a href="#no-fault-vs-at-fault">No-fault vs. at-fault states</a></li>
        <li><a href="#pip-coverage">PIP: Personal Injury Protection</a></li>
        <li><a href="#medpay">MedPay: Medical Payments coverage</a></li>
        <li><a href="#health-insurance-role">How your health insurance fits in</a></li>
        <li><a href="#subrogation">Subrogation: when insurers want repayment</a></li>
        <li><a href="#medical-liens">Medical liens and letters of protection</a></li>
        <li><a href="#managing-open-case">Managing bills while your case is open</a></li>
        <li><a href="#negotiating-after-settlement">Negotiating bills after settlement</a></li>
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
