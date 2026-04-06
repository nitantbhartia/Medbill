"""Guide: How to Read Your Explanation of Benefits (EOB)."""

from guides import register, _embed

register("explanation-of-benefits-eob", {
    "title": "How to Read Your Explanation of Benefits (EOB) — Line by Line",
    "meta_description": "An EOB is not a bill — it's a record of how your insurance processed a claim. Learn what every column means and how to spot billing errors before you pay.",
    "published": "2026-04-05",
    "author": "BillKarma Team",
    "category": "Insurance Basics",
    "faqs": [
        {
            "q": "Is an Explanation of Benefits (EOB) a bill?",
            "a": "No. An EOB is a statement from your insurance company showing how a claim was processed. It is not a request for payment. After receiving your EOB, you will get a separate bill from the provider for the 'patient responsibility' amount shown on the EOB. Always compare the two — they should match.",
        },
        {
            "q": "What is the 'allowed amount' on an EOB?",
            "a": "The allowed amount is the maximum your insurance company will pay for a specific service based on its contract with the provider. For in-network providers, the billed amount is often higher than the allowed amount — the difference is written off as a 'contractual adjustment' or 'discount.' You only owe your share of the allowed amount, not the full billed amount.",
        },
        {
            "q": "What does 'denied' mean on an EOB?",
            "a": "A denied claim means the insurer has declined to pay for that service. Common reasons include: the service wasn't covered under your plan, it required prior authorization that wasn't obtained, the provider was out-of-network, or the claim had a coding error. A denial doesn't mean you automatically owe the full amount — you have the right to appeal.",
        },
        {
            "q": "How do I get a copy of my EOB?",
            "a": "You can access your EOBs through your insurer's online member portal (usually under 'My Claims' or 'Claim History'), by calling the member services number on your insurance card, or by requesting paper copies by mail. You typically receive an EOB after every claim is processed.",
        },
        {
            "q": "What should I do if my EOB doesn't match my bill?",
            "a": "If a provider bills you more than the 'patient responsibility' shown on your EOB, that is likely a billing error. Contact the provider's billing department, show them the EOB, and ask them to correct the bill to match. If the provider insists the higher amount is correct, contact your insurer's member services to investigate.",
        },
    ],
    "body": f"""
<p class="lead">Every time your insurance processes a medical claim, they send you an Explanation of Benefits (EOB). Most Americans throw it away assuming it&rsquo;s junk mail. That is a mistake. <strong>31% of patients who compare their EOB to their provider bill find a discrepancy</strong> &mdash; and the EOB is the document that proves what you actually owe. Here is how to read it, line by line.</p>

<nav class="toc">
    <h2>In this guide</h2>
    <ol>
        <li><a href="#what-is-eob">What an EOB is (and is not)</a></li>
        <li><a href="#key-columns">The key columns explained</a></li>
        <li><a href="#contractual-adjustment">The contractual adjustment: why billed &ne; what you owe</a></li>
        <li><a href="#status-codes">What &ldquo;paid,&rdquo; &ldquo;denied,&rdquo; and &ldquo;in process&rdquo; mean</a></li>
        <li><a href="#spot-errors">How to spot billing errors on your EOB</a></li>
        <li><a href="#compare-to-bill">Comparing your EOB to your provider bill</a></li>
        <li><a href="#keeping-eobs">Keeping EOBs for taxes and records</a></li>
        <li><a href="#faq">Frequently asked questions</a></li>
        <li><a href="#sources">Sources</a></li>
    </ol>
</nav>

<h2 id="what-is-eob">1. What an EOB is (and is not)</h2>

<p>An <strong>Explanation of Benefits (EOB)</strong> is a document your insurance company sends after a medical claim is processed. It explains:</p>

<ul>
    <li>What service was provided and by whom</li>
    <li>What the provider charged (billed amount)</li>
    <li>What your insurance agreed to pay (allowed amount)</li>
    <li>What your insurance actually paid</li>
    <li>What you owe (patient responsibility)</li>
</ul>

<p><strong>An EOB is not a bill.</strong> You should not send a payment in response to an EOB. Wait for the provider&rsquo;s bill, then compare it to your EOB. The provider&rsquo;s bill should ask for the exact &ldquo;patient responsibility&rdquo; amount shown on your EOB &mdash; not more.</p>

<p><strong>EOB vs. Remittance Advice (RA):</strong> When the insurer pays the provider, the provider also receives a document called a Remittance Advice (RA). The RA is the provider&rsquo;s version of the EOB &mdash; it tells the billing department exactly what insurance paid and what the patient owes. When the EOB and the provider&rsquo;s bill disagree, it often means the billing department didn&rsquo;t correctly apply the RA before sending your bill.</p>

<h2 id="key-columns">2. The key columns explained</h2>

<p>EOBs vary by insurer, but every EOB contains the same core information, usually in a table with these columns:</p>

<table>
    <thead>
        <tr><th>Column</th><th>What It Means</th><th>Example</th></tr>
    </thead>
    <tbody>
        <tr>
            <td><strong>Service date</strong></td>
            <td>The date you received the service</td>
            <td>03/15/2026</td>
        </tr>
        <tr>
            <td><strong>Provider</strong></td>
            <td>The doctor, hospital, or facility that submitted the claim</td>
            <td>Riverside Radiology Group</td>
        </tr>
        <tr>
            <td><strong>Service / Procedure code</strong></td>
            <td>The CPT code (procedure) or HCPCS code for the service billed</td>
            <td>CPT 71046 (chest X-ray, 2 views)</td>
        </tr>
        <tr>
            <td><strong>Billed amount</strong></td>
            <td>What the provider charged your insurance company</td>
            <td>$850.00</td>
        </tr>
        <tr>
            <td><strong>Allowed amount</strong></td>
            <td>The maximum your insurer will pay for this service based on its contracted rate with the provider</td>
            <td>$310.00</td>
        </tr>
        <tr>
            <td><strong>Discount / Contractual adjustment</strong></td>
            <td>The difference between the billed amount and the allowed amount that the provider writes off under the network contract</td>
            <td>$540.00</td>
        </tr>
        <tr>
            <td><strong>Insurance paid</strong></td>
            <td>The amount your insurer paid to the provider after applying deductible, coinsurance, and benefit rules</td>
            <td>$248.00</td>
        </tr>
        <tr>
            <td><strong>Patient responsibility</strong></td>
            <td>The amount you owe the provider (deductible, copay, or coinsurance applied to this claim)</td>
            <td>$62.00</td>
        </tr>
        <tr>
            <td><strong>Deductible applied</strong></td>
            <td>How much of this claim went toward your deductible</td>
            <td>$0.00 (deductible already met)</td>
        </tr>
        <tr>
            <td><strong>Copay</strong></td>
            <td>Any flat fee applied to this visit</td>
            <td>$0.00</td>
        </tr>
        <tr>
            <td><strong>Coinsurance</strong></td>
            <td>Your percentage share (20% of $310 = $62)</td>
            <td>$62.00</td>
        </tr>
    </tbody>
</table>

<div class="bill-example">
    <div class="bill-header">EOB Example &mdash; Chest X-Ray at In-Network Radiology Group</div>
    <div class="line-item">
        <span>Billed amount (what provider charged)</span>
        <span>$850.00</span>
    </div>
    <div class="line-item">
        <span>Contractual adjustment (written off per network contract)</span>
        <span>&minus;$540.00</span>
    </div>
    <div class="line-item">
        <span>Allowed amount (insurer&rsquo;s contracted rate)</span>
        <span>$310.00</span>
    </div>
    <div class="line-item">
        <span>Deductible applied</span>
        <span>$0.00 (already met)</span>
    </div>
    <div class="line-item">
        <span>Your coinsurance (20% of $310)</span>
        <span>$62.00</span>
    </div>
    <div class="line-item">
        <span>Insurance paid (80% of $310)</span>
        <span>$248.00</span>
    </div>
    <div class="line-total">
        <span>YOU OWE THE PROVIDER</span>
        <span>$62.00</span>
    </div>
</div>

{_embed(mode="cost", cpt="71046", title="Look up radiology costs", subtitle="See Medicare&rsquo;s rate for common imaging procedures as a cost benchmark.")}

<h2 id="contractual-adjustment">3. The contractual adjustment: why billed &ne; what you owe</h2>

<p>The most confusing part of any EOB is the gap between the billed amount and the allowed amount. In the example above, the provider billed $850 but the allowed amount is only $310. Why?</p>

<p>When a provider joins an insurance network, they sign a contract agreeing to accept a negotiated rate for each service. That rate is the allowed amount. The difference between what they billed ($850) and what they&rsquo;re actually paid ($310 total from insurance + patient) is the <strong>contractual adjustment</strong> &mdash; the provider writes it off. They cannot collect it from you.</p>

<p><strong>This is why in-network care is cheaper.</strong> An out-of-network provider has no such contract. They can bill $850 and pursue the full amount. Your insurance might pay a portion (if you have out-of-network coverage), and the provider can balance bill you for the rest.</p>

<div class="key-takeaway">
    <strong>You only owe your share of the allowed amount, never the billed amount.</strong> If a provider bills you the full $850 instead of the $62 shown on your EOB, that is a billing error. Show the provider your EOB and ask them to correct the bill.
</div>

<h2 id="status-codes">4. What &ldquo;paid,&rdquo; &ldquo;denied,&rdquo; and &ldquo;in process&rdquo; mean</h2>

<p>Each claim on an EOB has a status. Common statuses and what to do about them:</p>

<table>
    <thead>
        <tr><th>Status</th><th>What It Means</th><th>What to Do</th></tr>
    </thead>
    <tbody>
        <tr>
            <td><strong>Paid</strong></td>
            <td>The claim was approved and processed. Insurance paid their share.</td>
            <td>Wait for the provider&rsquo;s bill and compare to the &ldquo;patient responsibility&rdquo; column.</td>
        </tr>
        <tr>
            <td><strong>Denied</strong></td>
            <td>The claim was rejected. Insurance will not pay.</td>
            <td>Read the denial reason code. If you believe the denial is wrong, file an appeal with your insurer within the deadline (usually 180 days). You do not automatically owe the full amount &mdash; wait until the appeal is resolved.</td>
        </tr>
        <tr>
            <td><strong>In process / Pending</strong></td>
            <td>The claim has been received but not yet adjudicated. Insurance needs more information or is reviewing the claim.</td>
            <td>Wait. Do not pay the provider&rsquo;s bill until the EOB shows a final status. Call your insurer if it remains pending after 45 days.</td>
        </tr>
        <tr>
            <td><strong>Patient responsibility only</strong></td>
            <td>The service was covered, but your deductible is not yet met. You owe 100% of the allowed amount.</td>
            <td>Pay the provider the amount shown on the EOB. It counts toward your deductible.</td>
        </tr>
    </tbody>
</table>

<h2 id="spot-errors">5. How to spot billing errors on your EOB</h2>

<p>Your EOB is your primary tool for catching billing errors. Here is what to look for:</p>

<ol>
    <li>
        <strong>Services you did not receive.</strong> Check the service date, procedure code, and provider. If you see a charge for a service you didn&rsquo;t have, that is a potential duplicate or phantom charge. Call your provider&rsquo;s billing department immediately.
    </li>
    <li>
        <strong>Wrong date of service.</strong> A date that doesn&rsquo;t match your records could indicate your claim was mixed up with another patient&rsquo;s.
    </li>
    <li>
        <strong>Wrong provider name.</strong> If the provider listed isn&rsquo;t who you saw, a claim may have been filed under the wrong provider number &mdash; especially common with group practices.
    </li>
    <li>
        <strong>Upcoded procedures.</strong> The procedure code determines what you&rsquo;re charged. An office visit coded as a 99214 (detailed exam) instead of a 99213 (standard exam) can cost you significantly more in deductible or coinsurance. If the complexity of the visit code seems higher than what occurred, ask your provider for the medical record that justifies it.
    </li>
    <li>
        <strong>Unbundled procedures.</strong> Some procedures have global codes that cover the whole service. When a provider separately bills for components that should be bundled into the global code, you&rsquo;re overcharged. This shows up as multiple procedure codes for what should have been one charge.
    </li>
    <li>
        <strong>Denied preventive care.</strong> ACA-required preventive services (annual physicals, mammograms, colonoscopies) must be covered at $0 cost-sharing when billed correctly. If your EOB shows cost-sharing for a service that was supposed to be preventive, the provider may have used the wrong billing code.
    </li>
</ol>

<h2 id="compare-to-bill">6. Comparing your EOB to your provider bill</h2>

<p>When you receive a bill from your provider, follow these steps:</p>

<ol>
    <li><strong>Match the date of service.</strong> Find the corresponding EOB for the same date and provider. Your insurer&rsquo;s member portal lets you filter by date.</li>
    <li><strong>Compare the &ldquo;patient responsibility&rdquo; on the EOB to the &ldquo;amount due&rdquo; on the bill.</strong> They should be identical. If the bill is higher, that is a discrepancy.</li>
    <li><strong>Check that the allowed amount was applied.</strong> The provider should not be billing you the full billed amount. If their bill shows a number close to the billed amount (not the allowed amount), they may not have applied the insurance payment yet &mdash; or it&rsquo;s an error.</li>
    <li><strong>Confirm payment credit.</strong> The bill should show the insurance payment as a credit. If it doesn&rsquo;t show the insurance payment at all, the billing department may not have processed the EOB yet. Call before paying.</li>
    <li><strong>Do not pay a bill that exceeds your EOB&rsquo;s patient responsibility</strong> until you have spoken with both the provider&rsquo;s billing department and your insurer to resolve the discrepancy.</li>
</ol>

<div class="case-study">
    <h3>Case study: EOB comparison prevents $1,400 overpayment</h3>
    <p><strong>Situation:</strong> Sarah had a colonoscopy in February. Her EOB showed: billed amount $3,200, allowed amount $1,100, contractual adjustment $2,100, insurance paid $880, patient responsibility $220 (20% coinsurance, deductible already met).</p>
    <p><strong>The bill:</strong> Three weeks later, she received a bill from the gastroenterology center for $1,620 &mdash; seven times what her EOB said she owed.</p>
    <p><strong>The problem:</strong> The billing system had not applied the insurance payment. The $880 insurance payment had not been credited, and the remaining balance was calculated from the full billed amount rather than the allowed amount.</p>
    <p><strong>The fix:</strong> Sarah called the billing department, referenced her EOB, and the correct bill of $220 was issued. <a href="/fight-debt">BillKarma can help you dispute overcharges like this one.</a> <strong>Savings: $1,400.</strong></p>
</div>

<h2 id="keeping-eobs">7. Keeping EOBs for taxes and records</h2>

<p>EOBs are important financial records. Here is how to manage them:</p>

<ul>
    <li><strong>Keep EOBs for at least three years</strong> in case of IRS audit. If you claim medical expense deductions (itemized deductions exceeding 7.5% of AGI), your EOBs are the supporting documentation.</li>
    <li><strong>Keep indefinitely for major procedures.</strong> If you had surgery, a hospitalization, or treatment for a serious condition, keep those EOBs permanently. Billing disputes and insurance appeals can resurface years later.</li>
    <li><strong>Download PDFs from your member portal.</strong> Most insurers archive EOBs for 2&ndash;3 years online. Download and save copies yourself &mdash; don&rsquo;t rely on the insurer&rsquo;s portal being accessible indefinitely.</li>
    <li><strong>Prescription EOBs are separate.</strong> If your pharmacy benefits are managed by a separate PBM (Pharmacy Benefit Manager), your drug EOBs come from a different source. Check your insurer&rsquo;s member portal or the PBM portal separately.</li>
</ul>

<div class="key-takeaway">
    <strong>BillKarma uses your EOB to catch discrepancies.</strong> When you <a href="/scan">upload your medical bill and EOB</a>, BillKarma compares the two documents line by line. If the provider is billing more than your EOB&rsquo;s patient responsibility, or if the allowed amount was not applied, BillKarma flags it and guides you through the dispute process.
</div>

<h2 id="faq">Frequently asked questions</h2>

<div class="faq-section">
    <div class="faq-item">
        <h3>Is an Explanation of Benefits (EOB) a bill?</h3>
        <p>No. An EOB is a statement from your insurance company showing how a claim was processed. Wait for a separate bill from the provider and compare it to the patient responsibility amount on your EOB before paying.</p>
    </div>

    <div class="faq-item">
        <h3>What is the &lsquo;allowed amount&rsquo; on an EOB?</h3>
        <p>The maximum your insurance will pay for a service under its contract with the provider. In-network providers write off the difference between their billed amount and the allowed amount. You only owe your share (deductible/coinsurance) of the allowed amount.</p>
    </div>

    <div class="faq-item">
        <h3>What does &lsquo;denied&rsquo; mean on an EOB?</h3>
        <p>The insurer declined to pay for the service. Read the denial reason code. You have the right to appeal. A denial does not automatically mean you owe the full billed amount &mdash; wait until the appeal is resolved before paying.</p>
    </div>

    <div class="faq-item">
        <h3>How do I get a copy of my EOB?</h3>
        <p>Log in to your insurer&rsquo;s member portal under &ldquo;My Claims&rdquo; or &ldquo;Claim History.&rdquo; You can also call member services or request paper copies by mail. You receive an EOB after every claim is processed.</p>
    </div>

    <div class="faq-item">
        <h3>What should I do if my EOB doesn&rsquo;t match my bill?</h3>
        <p>Contact the provider&rsquo;s billing department, show them your EOB, and ask them to correct the bill to match the patient responsibility amount. If they insist the higher amount is correct, contact your insurer&rsquo;s member services to investigate.</p>
    </div>
</div>

<h2 id="sources">Sources</h2>

<ul class="sources-list">
    <li><a href="#" target="_blank" rel="noopener">HealthCare.gov: Explanation of Benefits</a></li>
    <li><a href="#" target="_blank" rel="noopener">Centers for Medicare &amp; Medicaid Services: Reading Your Medicare Summary Notice</a></li>
    <li><a href="#" target="_blank" rel="noopener">Consumer Financial Protection Bureau: Medical Billing Errors Report (2025)</a></li>
    <li><a href="#" target="_blank" rel="noopener">American Medical Association: CPT Code Guidelines</a></li>
    <li><a href="#" target="_blank" rel="noopener">Kaiser Family Foundation: Understanding Your Health Insurance EOB</a></li>
</ul>
""",
})
