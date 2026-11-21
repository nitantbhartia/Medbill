"""Guide: Contractual Adjustment on a Hospital Bill: What It Means."""

from guides import register

register("contractual-adjustment-hospital-bill", {
    "title": "Contractual Adjustment on a Hospital Bill: What It Means",
    "meta_description": "A contractual adjustment is the discount from a hospital’s full charges to your plan’s allowed amount. In network, it generally isn’t yours to pay.",
    "published": "2026-11-20",
    "reviewed_on": "2026-11-20",
    "author": "BillKarma Team",
    "category": "Understanding Your Bill",
    "faqs": [
        {
            "q": "What is a contractual adjustment on a hospital bill?",
            "a": "It is the amount the hospital takes off its full listed price because of a contract with your insurer or a government program. The charge drops to the allowed amount, which is the most the plan will pay for that service. The adjusted amount is written off. It is not a payment by your insurer and it is not a balance you owe.",
        },
        {
            "q": "Can an in-network hospital bill me for the contractual adjustment?",
            "a": "Generally no. HealthCare.gov says a preferred (in-network) provider may not balance bill you for covered services. Medicare providers who accept assignment agree to charge only the deductible and coinsurance, and federal rules require Medicaid providers to accept the state’s payment plus any required cost sharing as payment in full. If you are asked to pay the adjusted amount, ask the billing office to explain the line in writing.",
        },
        {
            "q": "What do CO and PR mean on my EOB?",
            "a": "They are claim adjustment group codes. CO stands for Contractual Obligation: CMS says these adjustments are generally a write-off for the provider and are not billed to the patient. PR stands for Patient Responsibility: an amount that may be billed to you, such as a deductible, coinsurance or copay.",
        },
        {
            "q": "Why did a contractual adjustment get reversed on my statement?",
            "a": "A reversal usually means the claim was reprocessed. The insurer may have corrected, re-priced, recouped or denied it, and the hospital moved the old write-off back onto the account. Ask for the updated EOB from your insurer and compare it with the new statement before you pay the higher balance.",
        },
        {
            "q": "Is a self-pay discount the same as a contractual adjustment?",
            "a": "No. A contractual adjustment comes from a contract between the hospital and a payer. A self-pay or uninsured discount comes from the hospital’s own policy. Nonprofit hospitals also must cap what they charge patients who qualify for financial assistance, under IRS rules, which is a separate protection.",
        },
    ],
    "body": f"""
<p class="lead">A contractual adjustment is the amount a hospital takes off its full listed price because of a contract with your insurer, Medicare or Medicaid. If the hospital is in your network, that adjusted amount generally isn&rsquo;t yours to pay: you owe only your share of the lower &ldquo;allowed amount,&rdquo; like a deductible or coinsurance. This guide walks a sample statement line by line and shows which lines are worth a question.</p>

<nav class="toc">
    <h2>In this guide</h2>
    <ol>
        <li><a href="#what-it-is">What a contractual adjustment is</a></li>
        <li><a href="#sample-statement">Decoding a sample statement</a></li>
        <li><a href="#why-not-yours">Why the adjusted amount generally isn&rsquo;t yours</a></li>
        <li><a href="#eob-codes">Matching your EOB: allowed amount, CO and PR</a></li>
        <li><a href="#reversed">What a reversed adjustment means</a></li>
        <li><a href="#self-pay">Self-pay discounts are a different thing</a></li>
        <li><a href="#red-flags">Lines that should make you ask questions</a></li>
        <li><a href="#what-to-do">What to do, step by step</a></li>
        <li><a href="#faq">Frequently asked questions</a></li>
        <li><a href="#sources">Sources</a></li>
    </ol>
</nav>

<h2 id="what-it-is">1. What a contractual adjustment is</h2>

<p>Every hospital has a price list called a chargemaster (the hospital&rsquo;s full, standard price for each service). Those full prices are the &ldquo;total charges&rdquo; at the top of your statement.</p>

<p>Insurers and government programs rarely pay those prices. They pay an <strong>allowed amount</strong>, which HealthCare.gov defines as the maximum a plan will pay for a covered service. It may also be called the &ldquo;negotiated rate&rdquo; or &ldquo;payment allowance.&rdquo;</p>

<p>The gap between the two numbers is the contractual adjustment. You may also see it called a contractual allowance, contractual write-off, insurance discount or &ldquo;adjustment &ndash; [plan name].&rdquo; Different words, same idea: the hospital agreed in advance to accept less, so it removes the difference from your account.</p>

<p>A contractual adjustment is not a payment. No money changed hands; the charge simply went away.</p>

<h2 id="sample-statement">2. Decoding a sample statement</h2>

<p>Here is how the numbers usually flow from the top of a hospital statement to the bottom. This is a <strong>Sample</strong> with made-up figures, not a real patient&rsquo;s bill.</p>

<table>
    <thead>
        <tr>
            <th>Sample statement line</th>
            <th>Amount</th>
            <th>What it means</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>Total charges</td>
            <td>$4,850.00</td>
            <td>The hospital&rsquo;s full chargemaster prices for everything on the claim.</td>
        </tr>
        <tr>
            <td>Insurance adjustment (contractual)</td>
            <td>&minus;$3,210.00</td>
            <td>The write-off down to the plan&rsquo;s allowed amount. On the EOB this would usually carry group code CO.</td>
        </tr>
        <tr>
            <td><em>Allowed amount (often not printed)</em></td>
            <td>$1,640.00</td>
            <td>$4,850.00 &minus; $3,210.00. The most the plan will pay, counting your share.</td>
        </tr>
        <tr>
            <td>Insurance paid</td>
            <td>&minus;$992.00</td>
            <td>What the plan actually sent the hospital.</td>
        </tr>
        <tr>
            <td>Patient responsibility</td>
            <td>$648.00</td>
            <td>Your share: a $400.00 deductible plus 20% coinsurance on the remaining $1,240.00 ($248.00).</td>
        </tr>
    </tbody>
</table>

<p>Check the math the same way on your own statement: total charges, minus the contractual adjustment, minus what insurance paid, should equal what the hospital says you owe ($4,850.00 &minus; $3,210.00 &minus; $992.00 = $648.00). If any payment you already made is listed, subtract that too. And your balance should match the &ldquo;what you owe&rdquo; figure on your insurer&rsquo;s explanation of benefits (EOB) for the same claim.</p>

<div class="key-takeaway">
    <h3>Key takeaway</h3>
    <p>The contractual adjustment is the hospital&rsquo;s discount, not your debt. If your statement doesn&rsquo;t add up the way the sample does, <a href="/scan">check your bill free</a> to see each line compared with Medicare rates before you pay.</p>
</div>

<h2 id="why-not-yours">3. Why the adjusted amount generally isn&rsquo;t yours</h2>

<p>Billing you for the gap between full charges and the allowed amount has a name: <strong>balance billing</strong>. Whether it&rsquo;s allowed depends on who covers you and whether the hospital is in network.</p>

<table>
    <thead>
        <tr>
            <th>Your coverage</th>
            <th>The rule on the adjusted amount</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>Private plan, in-network hospital</td>
            <td>HealthCare.gov says a preferred (in-network) provider may not balance bill you for covered services. The network contract is what sets the allowed amount.</td>
        </tr>
        <tr>
            <td>Private plan, out-of-network</td>
            <td>No network contract, so you may be billed the difference, per HealthCare.gov. The federal No Surprises Act still protects you from balance bills for emergency care and for some non-emergency care from out-of-network providers at an in-network facility, per CMS; see our <a href="/guides/balance-billing/">balance billing guide</a>.</td>
        </tr>
        <tr>
            <td>Original Medicare</td>
            <td>Providers who accept assignment agree to charge you only the Medicare deductible and coinsurance, per Medicare.gov. A hospital&rsquo;s Medicare provider agreement also bars charging you for services Medicare pays for, except deductibles, coinsurance and a few listed items (42 CFR 489.21). For doctors and suppliers who don&rsquo;t accept assignment, Medicare.gov says the charge can&rsquo;t be more than 15% above the Medicare-approved amount (the &ldquo;limiting charge&rdquo;).</td>
        </tr>
        <tr>
            <td>Medicaid</td>
            <td>Federal rules (42 CFR 447.15) require states to limit Medicaid participation to providers that accept the state&rsquo;s payment, plus any required cost sharing, as payment in full.</td>
        </tr>
    </tbody>
</table>

<p>So for in-network and Medicare or Medicaid care, the contractual adjustment should stay written off. What you owe is limited to your cost sharing on the allowed amount.</p>

<h2 id="eob-codes">4. Matching your EOB: allowed amount, CO and PR</h2>

<p>Your EOB is the statement your insurer sends after it processes a claim. CMS&rsquo;s sample EOB says it plainly: an EOB is not a bill. But it is the best tool you have for checking the hospital&rsquo;s bill. On it, look for:</p>
<ul>
    <li><strong>Provider charges</strong>: the hospital&rsquo;s full price. Should match &ldquo;total charges.&rdquo;</li>
    <li><strong>Allowed amount</strong> (or &ldquo;allowed charges&rdquo;): what the provider will be paid in total.</li>
    <li><strong>Paid by insurer</strong>: should match &ldquo;insurance paid&rdquo; on the hospital statement.</li>
    <li><strong>What you owe</strong>: should match your patient responsibility.</li>
</ul>

<p>Many EOBs, and the remittance (payment report) the insurer sends the hospital, use two-letter <strong>group codes</strong> to say who is responsible for each dollar that wasn&rsquo;t paid. The codes are maintained by X12, the standards body, and CMS defines them for Medicare this way:</p>

<table>
    <thead>
        <tr>
            <th>Group code</th>
            <th>Name</th>
            <th>What it means for you</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>CO</td>
            <td>Contractual Obligation</td>
            <td>An adjustment from a contract or a regulation. CMS says these are generally a write-off for the provider and are not billed to the patient.</td>
        </tr>
        <tr>
            <td>PR</td>
            <td>Patient Responsibility</td>
            <td>An amount that may be billed to you. CMS says it is typically used for deductibles and copays.</td>
        </tr>
        <tr>
            <td>OA</td>
            <td>Other Adjustment</td>
            <td>Used when no other group code fits. Ask what it is.</td>
        </tr>
        <tr>
            <td>PI</td>
            <td>Payer Initiated Reduction</td>
            <td>A reduction the insurer made on its own judgment. Ask the insurer to explain it.</td>
        </tr>
    </tbody>
</table>

<p>Each group code is paired with a number called a claim adjustment reason code (CARC). The one you&rsquo;ll see most with a contractual adjustment is <strong>CO-45</strong>: X12 describes reason code 45 as a charge that exceeds the fee schedule, maximum allowable or contracted fee arrangement. Reason codes 1, 2 and 3 mean deductible, coinsurance and copay, and usually appear as PR-1, PR-2 and PR-3. For more on reading the whole form, see our guide to the <a href="/guides/explanation-of-benefits-eob/">explanation of benefits</a>.</p>

<div class="key-takeaway">
    <h3>Key takeaway</h3>
    <p>CO means the hospital absorbs it; PR means it may be yours. Line up the hospital statement against your EOB before paying, and use our <a href="/guides/how-to-get-itemized-hospital-bill/">itemized bill guide</a> if the statement only shows totals.</p>
</div>

<h2 id="reversed">5. What a reversed adjustment means</h2>

<p>Sometimes a new statement shows &ldquo;adjustment reversal&rdquo; or a contractual write-off added back, and your balance jumps. That usually means the claim was reprocessed. Common reasons include a corrected claim from the hospital, a re-pricing by the insurer, the insurer taking back a payment, or a claim that was later denied.</p>

<p>A reversal is not automatically wrong, but it should come with a new EOB. Before paying a higher balance:</p>
<ul>
    <li>Ask your insurer for the reprocessed EOB and the reason codes on it.</li>
    <li>If the new EOB shows a denial, the fix may be an appeal with the insurer, not a payment to the hospital. See <a href="/guides/insurance-claim-denied-what-to-do/">what to do when a claim is denied</a>.</li>
    <li>If the EOB still shows the same allowed amount and the same &ldquo;what you owe,&rdquo; ask the hospital why its balance differs.</li>
</ul>

<h2 id="self-pay">6. Self-pay discounts are a different thing</h2>

<p>If you had no insurance, or the hospital billed you directly, you may see a &ldquo;self-pay discount&rdquo; or &ldquo;uninsured discount.&rdquo; It looks like a contractual adjustment, but it isn&rsquo;t one. There is no contract with a payer behind it. It comes from the hospital&rsquo;s own policy, so the size varies by hospital. Our <a href="/guides/hospital-cash-pay-self-pay-discount/">self-pay discount guide</a> covers how to ask for one.</p>

<p>There is a separate federal protection for nonprofit hospitals. Under IRS rules (section 501(r)(5)), a nonprofit hospital must limit what it charges a patient who qualifies for its financial assistance policy for emergency or other medically necessary care to no more than the amounts generally billed to insured patients. If you might qualify, apply for financial assistance before you accept a self-pay price.</p>

<h2 id="red-flags">7. Lines that should make you ask questions</h2>

<p>None of these prove an error. Each is a reason to ask the billing office or your insurer for an explanation.</p>
<ul>
    <li><strong>No contractual adjustment at all</strong> on an insured, in-network visit. The hospital may have billed you before the claim was processed, or billed the wrong plan.</li>
    <li><strong>Your balance equals total charges minus insurance paid.</strong> That math skips the adjustment and bills you the difference.</li>
    <li><strong>An amount coded CO on the EOB shows up in your balance.</strong> CMS says CO adjustments are generally not billed to the patient.</li>
    <li><strong>&ldquo;Adjustment reversal&rdquo;</strong> with no new EOB from your insurer.</li>
    <li><strong>&ldquo;Patient responsibility&rdquo; that is higher than &ldquo;what you owe&rdquo;</strong> on the EOB for the same dates of service.</li>
    <li><strong>A &ldquo;self-pay&rdquo; label</strong> when you gave the hospital your insurance card.</li>
    <li><strong>Several statements for one visit</strong> that each show an adjustment. Check they aren&rsquo;t the same charges twice. Our guide to <a href="/guides/multiple-bills-one-hospital-visit/">multiple bills from one visit</a> can help.</li>
</ul>

<div class="key-takeaway">
    <h3>Key takeaway</h3>
    <p>If a red-flag line shows up, you don&rsquo;t have to argue on the phone. <a href="/scan">Upload your bill</a> to see each charge compared with the Medicare rate, then raise questions in writing.</p>
</div>

<h2 id="what-to-do">8. What to do, step by step</h2>

<ol>
    <li><strong>Gather both documents.</strong> The hospital statement and your insurer&rsquo;s EOB for the same dates of service. If you have Original Medicare, use your Medicare Summary Notice; see <a href="/guides/medicare-summary-notice-vs-hospital-bill/">how it compares with a hospital bill</a>.</li>
    <li><strong>Run the sample math.</strong> Total charges minus contractual adjustment minus insurance paid minus your payments should equal your balance.</li>
    <li><strong>Compare balances.</strong> Your balance should match &ldquo;what you owe&rdquo; on the EOB. Note any difference, with the dollar amount.</li>
    <li><strong>Check the codes.</strong> Anything marked CO on the EOB generally shouldn&rsquo;t be on your bill. Anything marked PR may be.</li>
    <li><strong>Ask for an itemized bill</strong> if the statement shows only totals.</li>
    <li><strong>Write to the billing office.</strong> Name the line, the amount and the EOB claim number. Ask them to correct the balance or explain it in writing. Keep copies.</li>
    <li><strong>Ask for a hold</strong> on collections while the question is open, and ask your insurer to confirm its processing if the two documents disagree.</li>
    <li><strong>Get help if it stalls.</strong> If you think a hospital is billing you in breach of a network, Medicare or Medicaid rule, consider talking to a consumer attorney or legal aid.</li>
</ol>

<h2 id="faq">Frequently asked questions</h2>

<div class="faq-section">
    <div class="faq-item">
        <h3>What is a contractual adjustment on a hospital bill?</h3>
        <p>It is the amount the hospital takes off its full listed price because of a contract with your insurer or a government program. The charge drops to the allowed amount, which is the most the plan will pay for that service. The adjusted amount is written off. It is not a payment by your insurer and it is not a balance you owe.</p>
    </div>
    <div class="faq-item">
        <h3>Can an in-network hospital bill me for the contractual adjustment?</h3>
        <p>Generally no. HealthCare.gov says a preferred (in-network) provider may not balance bill you for covered services. Medicare providers who accept assignment agree to charge only the deductible and coinsurance, and federal rules require Medicaid providers to accept the state&rsquo;s payment plus any required cost sharing as payment in full. If you are asked to pay the adjusted amount, ask the billing office to explain the line in writing.</p>
    </div>
    <div class="faq-item">
        <h3>What do CO and PR mean on my EOB?</h3>
        <p>They are claim adjustment group codes. CO stands for Contractual Obligation: CMS says these adjustments are generally a write-off for the provider and are not billed to the patient. PR stands for Patient Responsibility: an amount that may be billed to you, such as a deductible, coinsurance or copay.</p>
    </div>
    <div class="faq-item">
        <h3>Why did a contractual adjustment get reversed on my statement?</h3>
        <p>A reversal usually means the claim was reprocessed. The insurer may have corrected, re-priced, recouped or denied it, and the hospital moved the old write-off back onto the account. Ask for the updated EOB from your insurer and compare it with the new statement before you pay the higher balance.</p>
    </div>
    <div class="faq-item">
        <h3>Is a self-pay discount the same as a contractual adjustment?</h3>
        <p>No. A contractual adjustment comes from a contract between the hospital and a payer. A self-pay or uninsured discount comes from the hospital&rsquo;s own policy. Nonprofit hospitals also must cap what they charge patients who qualify for financial assistance, under IRS rules, which is a separate protection.</p>
    </div>
</div>

<h2 id="sources">Sources</h2>

<ul class="sources-list">
    <li><a href="https://www.healthcare.gov/glossary/allowed-amount/" target="_blank" rel="noopener">HealthCare.gov &mdash; Allowed amount (glossary)</a></li>
    <li><a href="https://www.healthcare.gov/glossary/balance-billing/" target="_blank" rel="noopener">HealthCare.gov &mdash; Balance billing (glossary)</a></li>
    <li><a href="https://www.medicare.gov/basics/costs/medicare-costs/provider-accept-Medicare" target="_blank" rel="noopener">Medicare.gov &mdash; Does your provider accept Medicare as full payment?</a></li>
    <li><a href="https://www.law.cornell.edu/cfr/text/42/489.21" target="_blank" rel="noopener">Legal Information Institute &mdash; 42 CFR 489.21, Specific limitations on charges</a></li>
    <li><a href="https://www.law.cornell.edu/cfr/text/42/447.15" target="_blank" rel="noopener">Legal Information Institute &mdash; 42 CFR 447.15, Acceptance of State payment as payment in full</a></li>
    <li><a href="https://www.cms.gov/regulations-and-guidance/guidance/manuals/downloads/clm104c22.pdf" target="_blank" rel="noopener">CMS &mdash; Medicare Claims Processing Manual, Chapter 22: Remittance Advice (section 60.1, Group Codes)</a></li>
    <li><a href="https://x12.org/codes/claim-adjustment-group-codes" target="_blank" rel="noopener">X12 &mdash; Claim Adjustment Group Codes</a></li>
    <li><a href="https://x12.org/codes/claim-adjustment-reason-codes" target="_blank" rel="noopener">X12 &mdash; Claim Adjustment Reason Codes</a></li>
    <li><a href="https://www.cms.gov/files/document/11819-sample-explanation-benefits-508.pdf" target="_blank" rel="noopener">CMS &mdash; Reading Your Explanation of Benefits (EOB), Publication 11819</a></li>
    <li><a href="https://www.cms.gov/nosurprises/consumer-protections/what-are-the-new-protections" target="_blank" rel="noopener">CMS &mdash; No Surprises: What are the new protections?</a></li>
    <li><a href="https://www.irs.gov/charities-non-profits/limitation-on-charges-section-501r5" target="_blank" rel="noopener">IRS &mdash; Limitation on charges, section 501(r)(5)</a></li>
</ul>
""",
})
