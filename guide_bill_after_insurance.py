"""Guide: Why Do I Still Owe Money After Insurance Paid?"""

from guides import register, _embed

register("why-you-owe-after-insurance-paid", {
    "title": "Why Do I Still Owe Money After Insurance Paid? A Complete Guide",
    "meta_description": "You had insurance and they paid — so why is there still a balance? Learn the 7 reasons you owe after insurance, spot billing errors, and fight back.",
    "published": "2026-02-27",
    "author": "BillKarma Team",
    "category": "Insurance Basics",
    "faqs": [
        {
            "q": "Why do I still owe money after my insurance paid?",
            "a": "The most common reasons are: your deductible hasn't been fully met, you owe coinsurance or a copay (your cost-share), an out-of-network provider was involved, the service wasn't covered, there's a billing error, you're being illegally balance billed, or there's a coordination of benefits issue with two insurances. At least 3 of these — billing errors, illegal balance billing, and COB issues — are disputable.",
        },
        {
            "q": "How do I know if my remaining balance is correct?",
            "a": "Compare your medical bill to your Explanation of Benefits (EOB) line by line. The 'patient responsibility' on your EOB should match your bill exactly. If the bill is higher, the provider may not have applied the insurance payment, may be balance billing illegally, or may have a coding error. Upload both documents to BillKarma for an automatic comparison.",
        },
        {
            "q": "Can I dispute the amount I owe after insurance?",
            "a": "Yes. Start by comparing your bill to your EOB. If they don't match, call the provider's billing department with your EOB. If you suspect a coding error, request an itemized bill. If you're being balance billed by an out-of-network provider at an in-network facility, file a complaint under the No Surprises Act. About 40-50% of billing disputes result in a reduction.",
        },
        {
            "q": "What is balance billing and is it legal?",
            "a": "Balance billing is when a provider bills you for the difference between their charge and what insurance paid. For in-network providers, it's always prohibited — they agreed to accept the insurance-negotiated rate. For out-of-network providers at in-network facilities (like an anesthesiologist at your in-network hospital), the No Surprises Act makes balance billing illegal in most cases.",
        },
        {
            "q": "What if I can't afford the balance after insurance?",
            "a": "You have options: ask for a payment plan (most providers offer 0% interest plans), apply for the hospital's financial assistance program (nonprofit hospitals are required to have one), request a hardship discount, or negotiate the balance down — especially if it exceeds what Medicare would pay for the same services.",
        },
        {
            "q": "How do I check if I've hit my out-of-pocket maximum?",
            "a": "Log into your insurer's member portal and look for 'Benefits' or 'My Claims' — your running deductible and out-of-pocket accumulator should be listed. You can also call the number on the back of your insurance card and ask for your current accumulator balance. If you've hit your OOP max, you should owe $0 for any further covered in-network services.",
        },
    ],
    "body": f"""
<p class="lead">You had insurance, you went to an in-network doctor, and your insurer paid &mdash; so why is there still a balance? The answer usually comes down to one of 7 specific reasons, and at least 3 of them may be billing errors you can fight. A 2023 <a href="https://www.kff.org/health-costs/poll-finding/kff-health-care-debt-survey/" target="_blank" rel="noopener">KFF survey</a> found that 67% of adults with medical debt were surprised by bills they thought their insurance would cover. This guide walks you through every reason you might still owe, how to tell whether the balance is legitimate, and exactly what to do about it.</p>

<nav class="toc">
    <h2>In this guide</h2>
    <ol>
        <li><a href="#how-payment-works">How insurance payment actually works</a></li>
        <li><a href="#seven-reasons">7 reasons you still owe after insurance</a></li>
        <li><a href="#decode-eob">How to decode your Explanation of Benefits</a></li>
        <li><a href="#common-errors">The 3 most common billing errors after insurance payment</a></li>
        <li><a href="#illegal-balance-billing">When you&rsquo;re being illegally balance billed</a></li>
        <li><a href="#dispute-balance">How to dispute the remaining balance</a></li>
        <li><a href="#cant-afford">What if you can&rsquo;t afford the patient balance</a></li>
        <li><a href="#oop-max">Checking if you&rsquo;ve hit your out-of-pocket maximum</a></li>
        <li><a href="#faq">Frequently asked questions</a></li>
        <li><a href="#sources">Sources</a></li>
    </ol>
</nav>

<h2 id="how-payment-works">1. How insurance payment actually works</h2>

<p>Before you can evaluate whether your remaining balance is correct, you need to understand the claim process. Every medical bill goes through 5 steps before you receive a patient responsibility amount:</p>

<table>
    <thead>
        <tr><th>Step</th><th>What happens</th><th>Who does it</th></tr>
    </thead>
    <tbody>
        <tr><td><strong>1. Provider bills</strong></td><td>Your doctor or hospital submits a claim with CPT codes, diagnosis codes, and their chargemaster price</td><td>Provider&rsquo;s billing department</td></tr>
        <tr><td><strong>2. Insurance processes</strong></td><td>Your insurer reviews the claim, checks network status, verifies coverage, and applies the negotiated rate</td><td>Insurance company</td></tr>
        <tr><td><strong>3. Allowed amount determined</strong></td><td>Insurance calculates the &ldquo;allowed amount&rdquo; &mdash; the negotiated rate for in-network providers. Everything above this is written off.</td><td>Insurance company</td></tr>
        <tr><td><strong>4. Insurance pays their share</strong></td><td>Insurance pays the allowed amount minus your cost-sharing (deductible, copay, coinsurance)</td><td>Insurance company &rarr; provider</td></tr>
        <tr><td><strong>5. You owe the rest</strong></td><td>Your share of the allowed amount &mdash; based on deductible status, copay, and coinsurance &mdash; becomes your &ldquo;patient responsibility&rdquo;</td><td>Provider bills you</td></tr>
    </tbody>
</table>

<div class="key-takeaway">
    <strong>The key number is the allowed amount, not the billed amount.</strong> For in-network providers, you should never owe anything based on the provider&rsquo;s full charge. Your cost-sharing is calculated on the allowed amount only. If your bill is based on the billed amount instead of the allowed amount, that&rsquo;s an error. <a href="/scan">Upload your bill to BillKarma</a> to check instantly.
</div>

<h2 id="seven-reasons">2. 7 reasons you still owe after insurance</h2>

<table>
    <thead>
        <tr><th>#</th><th>Reason</th><th>Typical amount</th><th>Can you fight it?</th></tr>
    </thead>
    <tbody>
        <tr><td>1</td><td><strong>Deductible not met yet</strong> &mdash; you pay 100% of the allowed amount until your annual deductible is satisfied</td><td>$500&ndash;$9,450</td><td>Only if the deductible was applied incorrectly</td></tr>
        <tr><td>2</td><td><strong>Coinsurance / copay</strong> &mdash; your cost-share after the deductible is met (e.g., 20% coinsurance or $50 copay)</td><td>$20&ndash;$3,000+</td><td>Only if the wrong rate was applied</td></tr>
        <tr><td>3</td><td><strong>Out-of-network provider</strong> &mdash; even at an in-network facility, some providers (anesthesiologists, radiologists, pathologists) may be out-of-network</td><td>$500&ndash;$10,000+</td><td>Yes &mdash; No Surprises Act protections apply</td></tr>
        <tr><td>4</td><td><strong>Non-covered service</strong> &mdash; your plan excludes the service (cosmetic, experimental, not medically necessary per the insurer)</td><td>Full billed amount</td><td>Yes &mdash; appeal the coverage denial</td></tr>
        <tr><td>5</td><td><strong>Billing error</strong> &mdash; wrong CPT code, duplicate charge, upcoding, or unbundling</td><td>$100&ndash;$5,000+</td><td>Yes &mdash; request an itemized bill and dispute</td></tr>
        <tr><td>6</td><td><strong>Balance billing</strong> &mdash; provider bills you the gap between their charge and what insurance paid (illegal in many cases)</td><td>$200&ndash;$20,000+</td><td>Yes &mdash; illegal under the No Surprises Act for emergency and in-network facility care</td></tr>
        <tr><td>7</td><td><strong>Coordination of benefits issue</strong> &mdash; if you have two insurances, the primary and secondary may not have coordinated correctly</td><td>Varies widely</td><td>Yes &mdash; contact both insurers to fix the coordination</td></tr>
    </tbody>
</table>

<p>Reasons 1 and 2 are legitimate cost-sharing &mdash; they&rsquo;re what you agreed to when you enrolled in the plan. But even these can be wrong if the amounts are calculated incorrectly. Reasons 3 through 7 are all potentially disputable.</p>

<div class="key-takeaway">
    <strong>Not sure which reason applies to your bill?</strong> <a href="/scan">Upload your bill and EOB to BillKarma</a> &mdash; we identify which of these 7 reasons is driving your remaining balance and tell you whether it&rsquo;s worth disputing.
</div>

<h2 id="decode-eob">3. How to decode your Explanation of Benefits</h2>

<p>Your Explanation of Benefits (EOB) is the document your insurance sends after processing a claim. It&rsquo;s the Rosetta Stone for understanding why you owe what you owe. Here&rsquo;s how to link the EOB to your bill with a side-by-side comparison:</p>

<div class="bill-example">
    <div class="bill-header">Side-by-side: EOB vs. Medical Bill &mdash; Outpatient knee MRI</div>
    <div class="line-item" style="border-bottom: 2px solid #D1D5DB; padding-bottom: 8px;">
        <span><strong>Line</strong></span>
        <span><strong>EOB says &rarr; Bill says</strong></span>
    </div>
    <div class="line-item">
        <span>Service: MRI knee w/o contrast (CPT 73721)</span>
        <span>EOB: 73721 &rarr; Bill: 73721 &#10004;</span>
    </div>
    <div class="line-item">
        <span>Provider billed</span>
        <span>EOB: $2,800 &rarr; Bill: $2,800 &#10004;</span>
    </div>
    <div class="line-item">
        <span>Allowed amount (negotiated rate)</span>
        <span>EOB: $620 &rarr; Bill: not shown (normal)</span>
    </div>
    <div class="line-item">
        <span>Insurance paid</span>
        <span>EOB: $496 &rarr; Bill: &ldquo;Insurance payment: $496&rdquo; &#10004;</span>
    </div>
    <div class="line-item">
        <span>Applied to deductible</span>
        <span>EOB: $0 (deductible already met) &rarr; Bill: n/a &#10004;</span>
    </div>
    <div class="line-item">
        <span>Coinsurance (20%)</span>
        <span>EOB: $124 &rarr; Bill: $124 &#10004;</span>
    </div>
    <div class="line-total">
        <span>YOUR RESPONSIBILITY</span>
        <span>EOB: $124 &rarr; Bill: $124 &#10004; Match</span>
    </div>
</div>

<p>When the EOB and bill match, you can be reasonably confident the balance is correct. But here&rsquo;s what a mismatch looks like:</p>

<div class="bill-example">
    <div class="bill-header">Mismatch example: EOB vs. Bill &mdash; same MRI</div>
    <div class="line-item">
        <span>EOB patient responsibility</span>
        <span>$124</span>
    </div>
    <div class="line-item error">
        <span>Bill amount due &nbsp; &#10060; <em>Bill is $2,180 higher than EOB</em></span>
        <span>$2,304</span>
    </div>
    <div class="line-item flagged">
        <span>What happened: provider subtracted insurance payment ($496) from billed amount ($2,800) instead of from allowed amount ($620)</span>
        <span>$2,800 &minus; $496 = $2,304 (wrong)</span>
    </div>
    <div class="line-total">
        <span>CORRECT AMOUNT YOU OWE</span>
        <span>$124 (per EOB)</span>
    </div>
</div>

<p>For a deeper dive into reading every line of your EOB, see our <a href="/guides/understanding-explanation-of-benefits">complete guide to understanding your EOB</a>.</p>

{_embed(mode="cost", title="Look up the Medicare rate for any service on your bill", subtitle="Enter a CPT code from your bill or EOB to see what Medicare pays.")}

<h2 id="common-errors">4. The 3 most common billing errors after insurance payment</h2>

<p>BillKarma&rsquo;s analysis of thousands of post-insurance bills shows three error patterns that account for the majority of incorrect remaining balances:</p>

<h3>Error 1: Insurance payment applied to billed amount instead of allowed amount</h3>

<div class="bill-example">
    <div class="bill-header">Error pattern: Wrong base amount &mdash; ER visit</div>
    <div class="line-item">
        <span>Provider billed (chargemaster price)</span>
        <span>$4,200</span>
    </div>
    <div class="line-item">
        <span>Insurance allowed amount</span>
        <span>$1,100</span>
    </div>
    <div class="line-item">
        <span>Insurance paid (80% of allowed)</span>
        <span>$880</span>
    </div>
    <div class="line-item error">
        <span>Bill says you owe: $4,200 &minus; $880 &nbsp; &#10060;</span>
        <span>$3,320</span>
    </div>
    <div class="line-item">
        <span>You actually owe: 20% of $1,100 (allowed amount)</span>
        <span>$220</span>
    </div>
    <div class="line-total">
        <span>OVERCHARGE</span>
        <span>$3,100</span>
    </div>
</div>

<p><strong>Why this happens:</strong> The provider&rsquo;s billing system subtracted the insurance payment from the full chargemaster price instead of the allowed amount. In-network providers must write off the difference between billed and allowed amounts &mdash; that $3,100 is a contractual adjustment, not your responsibility.</p>

<h3>Error 2: Duplicate charges that insurance only paid once</h3>

<div class="bill-example">
    <div class="bill-header">Error pattern: Duplicate line item &mdash; lab work</div>
    <div class="line-item">
        <span>CBC (CPT 85025) &mdash; first charge</span>
        <span>$182</span>
    </div>
    <div class="line-item error">
        <span>CBC (CPT 85025) &mdash; duplicate charge &nbsp; &#10060; <em>Same test, same date</em></span>
        <span>$182</span>
    </div>
    <div class="line-item">
        <span>Insurance processed and paid on one</span>
        <span>Paid: $8</span>
    </div>
    <div class="line-item flagged">
        <span>Provider bills you for the &ldquo;denied&rdquo; duplicate</span>
        <span>$182</span>
    </div>
    <div class="line-total">
        <span>AMOUNT TO DISPUTE</span>
        <span>$182</span>
    </div>
</div>

<p><strong>Why this happens:</strong> The same service was entered twice in the billing system. Insurance correctly denied the duplicate, but the provider&rsquo;s system passed the denied charge to you. Request an itemized bill and point out the duplicate date and CPT code.</p>

<h3>Error 3: Wrong CPT code changes your cost-sharing</h3>

<div class="bill-example">
    <div class="bill-header">Error pattern: Upcoded visit level &mdash; office visit</div>
    <div class="line-item error">
        <span>Billed: 99215 (Level 5 office visit) &nbsp; &#10060; <em>Highest-level visit for a routine follow-up</em></span>
        <span>Allowed: $248</span>
    </div>
    <div class="line-item">
        <span>Should be: 99214 (Level 4 office visit)</span>
        <span>Allowed: $186</span>
    </div>
    <div class="line-item">
        <span>Your 20% coinsurance on 99215</span>
        <span>$49.60</span>
    </div>
    <div class="line-item">
        <span>Your 20% coinsurance on 99214 (correct)</span>
        <span>$37.20</span>
    </div>
    <div class="line-total">
        <span>OVERCHARGE</span>
        <span>$12.40 (per visit &mdash; adds up across multiple visits)</span>
    </div>
</div>

<p><strong>Why this happens:</strong> Upcoding &mdash; billing a higher-level service than what was provided &mdash; inflates the allowed amount, which in turn inflates your coinsurance. While $12 per visit seems small, across a year of specialist visits it adds up to hundreds of dollars. <a href="/scan">Upload your bill to BillKarma</a> to check every CPT code against what was actually performed.</p>

{_embed(mode="markup", title="Check if your charge is inflated", subtitle="Enter the CPT code and amount billed to compare against Medicare rates.", height="420")}

<h2 id="illegal-balance-billing">5. When you&rsquo;re being illegally balance billed</h2>

<p>Balance billing is when a provider bills you the gap between their charge and what insurance paid. Under the <a href="/guides/no-surprises-act-explained">No Surprises Act</a> (effective January 1, 2022), balance billing is <strong>illegal</strong> in these situations:</p>

<ul>
    <li><strong>Emergency services</strong> &mdash; any emergency room visit, regardless of whether the facility or any provider is in-network</li>
    <li><strong>Out-of-network providers at in-network facilities</strong> &mdash; anesthesiologists, radiologists, pathologists, neonatologists, and assistant surgeons who happen to be out-of-network while you&rsquo;re at an in-network hospital</li>
    <li><strong>Air ambulance services</strong> &mdash; provided by out-of-network air ambulance operators</li>
</ul>

<p>In all of these cases, you can only be charged <strong>in-network cost-sharing rates</strong>. The provider and insurer must negotiate the rest between themselves &mdash; you are kept out of the middle.</p>

<div class="case-study">
    <h3>Example: Anesthesiologist balance bill at in-network hospital</h3>
    <p>A patient in Florida had shoulder surgery at an in-network hospital. The surgeon was in-network; the anesthesiologist was not. The anesthesiologist billed $6,200. Insurance paid $1,800 based on in-network rates. The anesthesiologist&rsquo;s office sent the patient a bill for $4,400 &mdash; the &ldquo;balance&rdquo; between their charge and the insurance payment.</p>
    <p>Under the No Surprises Act, this is illegal. The patient should only owe in-network cost-sharing (in this case, a $150 copay). After filing a complaint with CMS, the $4,400 bill was withdrawn. <strong>Savings: $4,250.</strong></p>
</div>

<p><strong>How to file a No Surprises Act complaint:</strong></p>
<ol>
    <li>Call the No Surprises Help Desk at <strong>1-800-985-3059</strong></li>
    <li>File online at <a href="https://www.cms.gov/nosurprises/consumers" target="_blank" rel="noopener">cms.gov/nosurprises</a></li>
    <li>Include your EOB, the provider&rsquo;s bill, and documentation that the facility was in-network</li>
</ol>

<p>For a complete breakdown of your rights, see our <a href="/guides/no-surprises-act-explained">No Surprises Act guide</a>.</p>

<h2 id="dispute-balance">6. How to dispute the remaining balance</h2>

<p>Follow these 5 steps to dispute a post-insurance balance you believe is incorrect:</p>

<h3>Step 1: Get your EOB and an itemized bill</h3>
<p>You need both documents. The EOB comes from your insurer (check your online portal or call the number on your insurance card). The itemized bill &mdash; with CPT codes for every line item &mdash; comes from the provider. You have a legal right to an itemized bill; request it in writing if the provider resists.</p>

<h3>Step 2: Compare them line by line</h3>
<p>Check that: (a) the patient responsibility on the EOB matches the bill total, (b) every CPT code on the bill appears on the EOB, (c) no duplicate charges exist, and (d) network status is correct. <a href="/scan">Upload both to BillKarma</a> for an automated comparison.</p>

<h3>Step 3: Call the provider&rsquo;s billing department</h3>
<p>Reference your EOB claim number and the specific discrepancy. Use this language: &ldquo;My EOB for claim [number] shows patient responsibility of [amount]. Your bill shows [higher amount]. Can you explain the difference and correct the account?&rdquo;</p>

<h3>Step 4: Call your insurer if the provider won&rsquo;t adjust</h3>
<p>If the provider insists the bill is correct but it doesn&rsquo;t match the EOB, escalate to your insurance company. Ask the insurer to send a corrected EOB or contact the provider directly to resolve the discrepancy.</p>

<h3>Step 5: File a formal dispute or complaint</h3>
<p>If neither the provider nor the insurer resolves it, file a written dispute. For No Surprises Act violations, file with CMS. For other billing errors, contact your <a href="https://www.naic.org/state_web_map.htm" target="_blank" rel="noopener">state insurance commissioner</a>. For persistent issues, consider contacting a <a href="/guides/medical-billing-advocate">medical billing advocate</a>.</p>

<div class="key-takeaway">
    <strong>Document everything.</strong> Keep a log of every call (date, time, representative name, reference number, what was said). Written disputes carry more weight than phone calls &mdash; follow up every call with an email or letter summarizing what was agreed.
</div>

<h2 id="cant-afford">7. What if you can&rsquo;t afford the patient balance</h2>

<p>Even when the balance is correct, you have options if you can&rsquo;t pay it all at once:</p>

<table>
    <thead>
        <tr><th>Option</th><th>How it works</th><th>Who qualifies</th></tr>
    </thead>
    <tbody>
        <tr><td><strong>Payment plan</strong></td><td>Most providers offer 0% interest plans spreading the balance over 6&ndash;24 months</td><td>Anyone &mdash; just ask</td></tr>
        <tr><td><strong>Financial assistance / charity care</strong></td><td>Nonprofit hospitals are required by law to offer financial assistance. Discounts of 50&ndash;100% are common for patients under 400% of the federal poverty level.</td><td>Income-based &mdash; typically under $62,400/year for an individual (2026)</td></tr>
        <tr><td><strong>Hardship discount</strong></td><td>Even for-profit providers often offer 20&ndash;40% discounts for financial hardship. Ask for the &ldquo;prompt pay&rdquo; or &ldquo;uninsured&rdquo; discount even if you have insurance.</td><td>Anyone experiencing hardship</td></tr>
        <tr><td><strong>Negotiate the balance</strong></td><td>Offer to pay a lump sum that&rsquo;s less than the full balance. Providers often accept 40&ndash;60% of the bill to avoid sending it to collections.</td><td>Anyone &mdash; works best if the bill is 90+ days old</td></tr>
        <tr><td><strong>Medical credit card (use caution)</strong></td><td>Cards like CareCredit offer 0% intro periods, but deferred interest kicks in if not paid in full by the end of the promo period</td><td>Anyone approved &mdash; but read the terms carefully</td></tr>
    </tbody>
</table>

<div class="case-study">
    <h3>Financial assistance reduced a $4,800 balance to $0</h3>
    <p>A single mother in Illinois earning $38,000/year had a $4,800 patient balance after insurance paid for her son&rsquo;s emergency appendectomy. The nonprofit hospital&rsquo;s financial assistance policy covered 100% of the balance for patients under 250% of the federal poverty level. She applied, provided two pay stubs and a tax return, and the entire balance was written off within 3 weeks. <strong>Savings: $4,800.</strong></p>
</div>

<p>For a deeper guide on each of these options, see our guides on <a href="/guides/hospital-financial-assistance">hospital financial assistance programs</a> and <a href="/guides/copay-vs-coinsurance-vs-deductible">understanding your cost-sharing</a>.</p>

<h2 id="oop-max">8. Checking if you&rsquo;ve hit your out-of-pocket maximum</h2>

<p>If you&rsquo;ve had a major medical event or ongoing treatment, you may have already hit your out-of-pocket maximum &mdash; meaning you should owe <strong>$0</strong> for any further covered in-network services. In 2026, the ACA cap is <strong>$9,450 for individuals</strong> and <strong>$18,900 for families</strong>.</p>

<p>Here&rsquo;s how to check:</p>

<ol>
    <li><strong>Log into your insurer&rsquo;s member portal.</strong> Look for &ldquo;Benefits Summary&rdquo; or &ldquo;Accumulator&rdquo; &mdash; it shows your year-to-date deductible and OOP max progress.</li>
    <li><strong>Call the number on the back of your insurance card.</strong> Ask: &ldquo;What is my current out-of-pocket accumulator balance for this plan year?&rdquo;</li>
    <li><strong>Check your most recent EOB.</strong> Many EOBs include a running accumulator showing how much you&rsquo;ve paid toward the deductible and OOP max so far.</li>
    <li><strong>Add up your payments manually.</strong> If the portal numbers don&rsquo;t seem right, tally every copay, coinsurance, and deductible payment from your EOBs for the year.</li>
</ol>

<div class="case-study">
    <h3>Patient billed $1,400 after OOP max was met</h3>
    <p>A patient in Pennsylvania undergoing chemotherapy hit her $8,000 out-of-pocket maximum in August. In September, she received a $1,400 bill for infusion services. Her insurer&rsquo;s accumulator confirmed the OOP max was met, but the oncology clinic&rsquo;s billing system hadn&rsquo;t synced. She sent the clinic a screenshot of her insurer&rsquo;s accumulator page and the bill was corrected to $0 within two weeks. <strong>Savings: $1,400.</strong></p>
</div>

<p>For a full breakdown of what counts (and what doesn&rsquo;t) toward your OOP max, see our <a href="/guides/out-of-pocket-maximum">out-of-pocket maximum guide</a>.</p>

<div class="key-takeaway">
    <strong>Getting bills for a high-cost treatment year?</strong> Use our <a href="/calculator">free calculator</a> to look up Medicare rates for each CPT code on your bill. If your total cost-sharing across all your bills this year exceeds your plan&rsquo;s OOP max, something is wrong &mdash; and you should dispute every bill after the cap was hit.
</div>

<h2 id="faq">Frequently asked questions</h2>

<div class="faq-section">
    <div class="faq-item">
        <h3>Why do I still owe money after my insurance paid?</h3>
        <p>The most common reasons are: your deductible hasn&rsquo;t been fully met, you owe coinsurance or a copay (your cost-share), an out-of-network provider was involved, the service wasn&rsquo;t covered, there&rsquo;s a billing error, you&rsquo;re being illegally balance billed, or there&rsquo;s a coordination of benefits issue with two insurances. Compare your bill to your <a href="/guides/understanding-explanation-of-benefits">EOB</a> &mdash; if the numbers don&rsquo;t match, you likely have grounds to dispute.</p>
    </div>

    <div class="faq-item">
        <h3>How do I know if my remaining balance is correct?</h3>
        <p>Compare your medical bill to your Explanation of Benefits (EOB) line by line. The &ldquo;patient responsibility&rdquo; on your EOB should match your bill exactly. If the bill is higher, the provider may not have applied the insurance payment correctly, may be balance billing, or may have a coding error. <a href="/scan">Upload both documents to BillKarma</a> for an automatic side-by-side comparison.</p>
    </div>

    <div class="faq-item">
        <h3>Can I dispute the amount I owe after insurance?</h3>
        <p>Yes. Start by comparing your bill to your EOB. If they don&rsquo;t match, call the provider&rsquo;s billing department with your EOB claim number. If you suspect a coding error, request an itemized bill. If you&rsquo;re being balance billed by an out-of-network provider at an in-network facility, file a complaint under the <a href="/guides/no-surprises-act-explained">No Surprises Act</a>. About 40&ndash;50% of billing disputes result in a reduction.</p>
    </div>

    <div class="faq-item">
        <h3>What is balance billing and is it legal?</h3>
        <p>Balance billing is when a provider bills you the gap between their charge and what insurance paid. For in-network providers, it&rsquo;s always prohibited. For out-of-network providers at in-network facilities or in emergencies, the No Surprises Act makes it illegal. If you receive a balance bill in either of these situations, file a complaint at <a href="https://www.cms.gov/nosurprises" target="_blank" rel="noopener">cms.gov/nosurprises</a> or call 1-800-985-3059.</p>
    </div>

    <div class="faq-item">
        <h3>What if I can&rsquo;t afford the balance after insurance?</h3>
        <p>Ask for a 0% interest payment plan, apply for the hospital&rsquo;s financial assistance program (nonprofit hospitals are required to have one), negotiate a lump-sum discount, or request a hardship reduction. Many providers will accept 40&ndash;60% of the bill to avoid sending it to collections. See our <a href="/guides/copay-vs-coinsurance-vs-deductible">cost-sharing guide</a> for details on what you should actually owe.</p>
    </div>

    <div class="faq-item">
        <h3>How do I check if I&rsquo;ve hit my out-of-pocket maximum?</h3>
        <p>Log into your insurer&rsquo;s member portal and look for your accumulator balance, or call the number on the back of your insurance card. In 2026, the ACA cap is $9,450 for individuals and $18,900 for families. If you&rsquo;ve hit it, you owe $0 for further covered in-network services. See our <a href="/guides/out-of-pocket-maximum">out-of-pocket maximum guide</a> for common billing traps.</p>
    </div>
</div>

<h2 id="sources">Sources</h2>

<ul class="sources-list">
    <li><a href="https://www.cms.gov/nosurprises" target="_blank" rel="noopener">CMS: No Surprises Act &mdash; Consumer Protections</a></li>
    <li><a href="https://www.kff.org/health-costs/poll-finding/kff-health-care-debt-survey/" target="_blank" rel="noopener">KFF: Health Care Debt Survey (2023)</a></li>
    <li><a href="https://www.cms.gov/cciio/resources/data-resources/marketplace-puf" target="_blank" rel="noopener">CMS: 2026 ACA Out-of-Pocket Maximum Limits</a></li>
    <li><a href="https://www.kff.org/private-insurance/issue-brief/claims-denials-and-appeals-in-aca-marketplace-plans/" target="_blank" rel="noopener">KFF: Claims Denials and Appeals in ACA Marketplace Plans</a></li>
    <li><a href="https://www.healthcare.gov/health-care-law-protections/appeals/" target="_blank" rel="noopener">HealthCare.gov: How to Appeal a Health Insurance Decision</a></li>
    <li><a href="https://www.naic.org/state_web_map.htm" target="_blank" rel="noopener">NAIC: State Insurance Commissioner Directory</a></li>
</ul>
""",
})
