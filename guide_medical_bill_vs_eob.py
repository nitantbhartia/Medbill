"""Guide: Medical Bill vs. EOB Mismatch."""

from guides import register, _embed

register("medical-bill-vs-eob-mismatch", {
    "title": "Your Medical Bill and EOB Don\u2019t Match: Exactly What to Do (Step by Step)",
    "meta_description": "Your hospital bill says one amount, your EOB says another. Learn the 5 most common reasons for the mismatch and how to fix each one to avoid overpaying.",
    "published": "2026-03-03",
    "author": "BillKarma Team",
    "category": "Medical Bills",
    "faqs": [
        {
            "q": "Why is my medical bill different from my EOB?",
            "a": "Five common reasons: the provider billed the full chargemaster rate but your insurer negotiated a lower allowed amount, your insurer denied part of the claim (leaving more for you to pay), the provider billed codes your insurer disagrees with, your insurer applied the charges to your deductible differently than expected, or the provider sent the bill before your insurer finished processing the claim. The EOB is your insurer's version of the math. The provider bill is the provider's version. They should reconcile, but often don't.",
        },
        {
            "q": "Should I pay the medical bill or wait for the EOB?",
            "a": "Always wait for the EOB before paying a medical bill. The EOB shows the insurer's allowed amount, what the insurer paid, and what you actually owe. If you pay the provider bill before the EOB arrives, you may overpay because the provider billed the full chargemaster rate, not the negotiated rate. If a provider pressures you to pay before insurance processes the claim, say: 'I will pay my patient responsibility after my insurance has processed this claim and I have reviewed the EOB.'",
        },
        {
            "q": "What if my bill is higher than what my EOB says I owe?",
            "a": "If your provider bill exceeds the 'patient responsibility' amount on your EOB, the provider is likely billing you incorrectly. Call the billing department and reference your EOB: 'My EOB shows my patient responsibility is $X, but your bill says $Y. Can you adjust this?' The provider is contractually obligated to accept the insurer's allowed amount as payment in full (for in-network care). You should only owe the patient responsibility amount shown on the EOB, which includes your deductible, copay, and coinsurance.",
        },
        {
            "q": "What does 'amount not covered' mean on my EOB?",
            "a": "'Amount not covered' typically means charges your insurer will not pay, which may become your responsibility. Common reasons: the service is not covered by your plan, the provider used a code your insurer doesn't recognize, the service was deemed not medically necessary, or the provider is out of network. If the amount not covered seems wrong, call your insurer to ask for the specific denial reason and whether you can appeal.",
        },
        {
            "q": "Can I dispute a bill that doesn't match my EOB?",
            "a": "Yes. Start by calling the provider's billing department with your EOB in hand. Quote the specific amounts: allowed amount, insurer payment, and patient responsibility. If the provider won't adjust, call your insurer and ask them to contact the provider directly. If the bill is for balance billing (the difference between the chargemaster rate and the allowed amount for in-network care), this is prohibited under most insurance contracts and the No Surprises Act for emergency services.",
        },
        {
            "q": "How long should I wait for an EOB before paying?",
            "a": "Insurance claims typically take 14-45 days to process. If you haven't received an EOB within 30 days of service, call your insurer to check the claim status. Don't pay a provider bill until you've received and reviewed the EOB. If a provider sends you to collections before your insurer has processed the claim, dispute the collection with a letter stating the claim is pending with your insurer.",
        },
    ],
    "body": f"""
<p class="lead">You got a bill from your doctor for $2,400. Your Explanation of Benefits says you owe $680. Which one do you pay? <strong>The EOB is almost always right.</strong> Yet millions of patients overpay every year because they pay the provider bill without checking it against the EOB. Here is exactly how to read both documents, spot the mismatch, and make sure you pay only what you actually owe.</p>

<nav class="toc">
    <h2>In this guide</h2>
    <ol>
        <li><a href="#bill-vs-eob">Bill vs. EOB: what each document tells you</a></li>
        <li><a href="#five-reasons">5 reasons they don&rsquo;t match</a></li>
        <li><a href="#read-eob">How to read your EOB</a></li>
        <li><a href="#fix-mismatch">How to fix each type of mismatch</a></li>
        <li><a href="#never-overpay">The golden rule: never pay before the EOB</a></li>
        <li><a href="#when-eob-wrong">What if the EOB is wrong?</a></li>
        <li><a href="#faq">Frequently asked questions</a></li>
        <li><a href="#sources">Sources</a></li>
    </ol>
</nav>

<h2 id="bill-vs-eob">1. Bill vs. EOB: what each document tells you</h2>

<p>Your medical bill and your Explanation of Benefits are two different documents from two different parties, describing the same service. They should agree on what you owe. They often don&rsquo;t.</p>

<table>
    <thead>
        <tr><th>Document</th><th>Sent by</th><th>What it shows</th><th>What to trust</th></tr>
    </thead>
    <tbody>
        <tr><td><strong>Provider bill</strong></td><td>Doctor, hospital, or lab</td><td>The provider&rsquo;s charges at their rates (often the chargemaster price)</td><td>The CPT codes and service descriptions (what was done)</td></tr>
        <tr><td><strong>EOB</strong></td><td>Your insurance company</td><td>What your insurer allows, pays, and what you owe</td><td>The &ldquo;patient responsibility&rdquo; amount (what you actually owe)</td></tr>
    </tbody>
</table>

<p><strong>The key insight:</strong> For in-network care, your provider has a contract with your insurer to accept the <strong>allowed amount</strong> as payment in full. The provider&rsquo;s chargemaster price is irrelevant. If the provider bills you $2,400 but the insurer&rsquo;s allowed amount is $900 and the insurer pays $220, your patient responsibility is <strong>$680</strong> (the allowed amount minus the insurer&rsquo;s payment). Not $2,400. Not $2,180. Exactly $680.</p>

<div class="bill-example">
    <div class="bill-header">Example: Office visit + blood work &mdash; Bill vs. EOB</div>
    <div class="line-item">
        <span>Provider charges (chargemaster rate)</span>
        <span>$2,400</span>
    </div>
    <div class="line-item">
        <span>Insurance allowed amount (negotiated rate)</span>
        <span>$900</span>
    </div>
    <div class="line-item">
        <span>Insurance contractual adjustment (provider writes off)</span>
        <span>-$1,500</span>
    </div>
    <div class="line-item">
        <span>Insurance paid</span>
        <span>$220</span>
    </div>
    <div class="line-item flagged">
        <span><strong>Your patient responsibility (what you actually owe)</strong></span>
        <span><strong>$680</strong></span>
    </div>
</div>

<div class="key-takeaway">
    <strong>If you pay the provider bill ($2,400) instead of the EOB amount ($680), you overpay by $1,720.</strong> This happens more than you think. Some providers send bills before insurance processes the claim. Others bill the chargemaster rate and leave it to patients to reconcile. Always check the EOB first.
</div>

<h2 id="five-reasons">2. Five reasons they don&rsquo;t match</h2>

<h3>Reason 1: The bill arrived before the claim was processed</h3>
<p>Providers often send bills within days of your visit. Insurance claims take 14&ndash;45 days to process. If you get a bill before the EOB, the bill likely shows the full chargemaster rate because the provider doesn&rsquo;t know what your insurer will allow yet.</p>
<p><strong>Fix:</strong> Wait for the EOB. Call the provider and say: &ldquo;I&rsquo;d like to wait until my insurance processes this claim before paying.&rdquo;</p>

<h3>Reason 2: The insurer denied part of the claim</h3>
<p>Your insurer may have denied one or more services on the claim &mdash; not medically necessary, not covered, prior authorization missing, or coding error. The denied charges may show up on your provider bill as your responsibility.</p>
<p><strong>Fix:</strong> Check your EOB for any denied services. If the denial seems wrong, <a href="/guides/insurance-denial-appeal-win">appeal the denial</a>. Don&rsquo;t pay denied charges until you&rsquo;ve exhausted the appeal process.</p>

<h3>Reason 3: The provider is balance billing you</h3>
<p>Balance billing is when a provider charges you the difference between their chargemaster rate and the insurer&rsquo;s allowed amount. For in-network providers, this is a contract violation. For out-of-network emergency services, it&rsquo;s prohibited by the <a href="/guides/no-surprises-act-explained">No Surprises Act</a>.</p>
<p><strong>Fix:</strong> If your in-network provider bills more than your EOB&rsquo;s patient responsibility amount, call and say: &ldquo;This appears to be balance billing. Your contract with [insurer] requires you to accept the allowed amount as payment in full. Please adjust the bill to match my EOB.&rdquo;</p>

<h3>Reason 4: Coding errors caused a different allowed amount</h3>
<p>If the provider submitted the wrong CPT code, the insurer may have processed the claim at a lower (or higher) allowed amount. The provider&rsquo;s bill shows one set of codes and charges; the EOB shows different amounts because the codes were adjusted or rejected.</p>
<p><strong>Fix:</strong> Compare the CPT codes on the provider bill to the codes on the EOB. If they differ, ask the provider to resubmit with the correct codes. <a href="/scan">Upload your bill to BillKarma</a> to check for coding errors automatically.</p>

<h3>Reason 5: The deductible was applied differently than expected</h3>
<p>Your insurer applies charges to your deductible based on the allowed amount, not the chargemaster rate. If you haven&rsquo;t met your deductible, the EOB may show a larger patient responsibility than you expected because the full allowed amount is applied to the deductible.</p>
<p><strong>Fix:</strong> Check your deductible status on your insurer&rsquo;s member portal. Verify the math: patient responsibility should equal the lesser of (allowed amount minus insurer payment) or (remaining deductible plus applicable coinsurance).</p>

<h2 id="read-eob">3. How to read your EOB</h2>

<p>Every EOB has the same five critical numbers. Here is what each means:</p>

<table>
    <thead>
        <tr><th>EOB field</th><th>What it means</th><th>Example</th></tr>
    </thead>
    <tbody>
        <tr><td><strong>Billed amount</strong></td><td>What the provider charged (chargemaster rate)</td><td>$2,400</td></tr>
        <tr><td><strong>Allowed amount</strong></td><td>What your insurer says the service should cost (negotiated rate)</td><td>$900</td></tr>
        <tr><td><strong>Contractual adjustment</strong></td><td>The difference the provider writes off (billed minus allowed)</td><td>-$1,500</td></tr>
        <tr><td><strong>Plan paid</strong></td><td>What your insurer actually paid the provider</td><td>$220</td></tr>
        <tr><td><strong>Patient responsibility</strong></td><td>What you owe (allowed amount minus plan paid)</td><td><strong>$680</strong></td></tr>
    </tbody>
</table>

<p><strong>The only number that matters is patient responsibility.</strong> That is what you owe. Not the billed amount. Not the allowed amount. The patient responsibility &mdash; which includes your deductible, copay, and/or coinsurance.</p>

<p>Your EOB may also show:</p>
<ul>
    <li><strong>Deductible applied:</strong> How much of the charge went toward your annual deductible</li>
    <li><strong>Coinsurance:</strong> Your percentage share after the deductible (typically 20%)</li>
    <li><strong>Copay:</strong> Your flat fee per visit (if applicable)</li>
    <li><strong>Not covered:</strong> Charges your plan won&rsquo;t pay (may be your responsibility or the provider&rsquo;s write-off)</li>
</ul>

<h2 id="fix-mismatch">4. How to fix each type of mismatch</h2>

<h3>Scenario A: Bill is higher than EOB patient responsibility</h3>
<p><strong>This is the most common mismatch.</strong> The provider bill shows the chargemaster rate or hasn&rsquo;t been adjusted for insurance.</p>
<p><strong>Script:</strong> &ldquo;Hi, I received a bill for $[bill amount] for services on [date]. My EOB from [insurer] shows my patient responsibility is $[EOB amount]. The allowed amount is $[allowed amount], and my insurer paid $[plan paid]. Can you please adjust my bill to $[EOB patient responsibility]?&rdquo;</p>
<p>If they push back: &ldquo;Your contract with [insurer] requires you to accept the allowed amount as payment in full. Billing me above the patient responsibility amount shown on the EOB appears to be balance billing, which is prohibited under your provider agreement.&rdquo;</p>

<h3>Scenario B: EOB shows denied charges that appear on the bill</h3>
<p>Some charges were denied by your insurer. The provider may bill you for the denied amount.</p>
<p><strong>Steps:</strong></p>
<ol>
    <li>Check the denial reason on the EOB (code + description)</li>
    <li>If the denial is a coding error, ask the provider to resubmit with correct codes</li>
    <li>If the denial is for medical necessity or coverage, <a href="/guides/insurance-denial-appeal-win">appeal the denial</a></li>
    <li>Tell the provider: &ldquo;I am appealing the denial with my insurer. Please do not bill me for denied charges until the appeal is resolved.&rdquo;</li>
</ol>

<h3>Scenario C: Bill from out-of-network provider you didn&rsquo;t choose</h3>
<p>If an out-of-network provider treated you at an in-network facility (common with anesthesiologists, radiologists, and pathologists), the <a href="/guides/no-surprises-act-explained">No Surprises Act</a> protects you. Your cost-sharing should be based on in-network rates.</p>
<p><strong>Script:</strong> &ldquo;I received this service at an in-network facility and did not choose this out-of-network provider. Under the No Surprises Act, my cost-sharing should be calculated at the in-network rate. Please adjust the bill accordingly.&rdquo;</p>

<h3>Scenario D: Multiple bills for the same visit</h3>
<p>It&rsquo;s common to receive separate bills from the hospital (facility fee), the doctor (professional fee), the anesthesiologist, the lab, and the radiologist &mdash; all for one visit. Each should have its own EOB.</p>
<p><strong>Steps:</strong> Match each bill to its corresponding EOB. Each one should reconcile independently. <a href="/scan">Upload all bills to BillKarma</a> to check for duplicate charges across multiple bills for the same visit.</p>

<div class="case-study">
    <h3>Case study: Patient catches $1,860 balance billing error</h3>
    <p><strong>Situation:</strong> Jennifer had outpatient knee surgery at an in-network hospital. She received a bill for $4,200. Her EOB showed an allowed amount of $2,340, insurer payment of $1,872, and patient responsibility of $468.</p>
    <p><strong>The problem:</strong> The hospital billed her $4,200 &mdash; the chargemaster rate &mdash; instead of the $468 patient responsibility on the EOB. The $1,860 difference between $4,200 and $2,340 should have been written off as a contractual adjustment.</p>
    <p><strong>What she did:</strong> She called billing with her EOB, quoted the allowed amount and patient responsibility, and the bill was adjusted in one phone call. She also <a href="/scan">scanned the bill on BillKarma</a> and found a duplicate charge for surgical supplies ($280), which further reduced her bill.</p>
    <p><strong>Result:</strong> Final bill: $188 (after the $280 duplicate was removed from the $468 patient responsibility). <strong>Total savings: $4,012.</strong></p>
</div>

<h2 id="never-overpay">5. The golden rule: never pay before the EOB</h2>

<p>The single most effective way to avoid overpaying is to <strong>never pay a medical bill before you receive and review the EOB</strong>. Here is the process:</p>

<ol>
    <li><strong>Receive a bill.</strong> Don&rsquo;t pay it yet.</li>
    <li><strong>Check your insurer&rsquo;s portal for the EOB.</strong> EOBs are often available online before the paper copy arrives.</li>
    <li><strong>If no EOB yet, call your insurer.</strong> Ask: &ldquo;Has the claim for [date of service] at [provider] been processed?&rdquo;</li>
    <li><strong>Once you have the EOB, compare.</strong> Match the CPT codes, allowed amounts, and patient responsibility.</li>
    <li><strong>If they match, pay the patient responsibility amount.</strong></li>
    <li><strong>If they don&rsquo;t match, call the provider.</strong> Use the scripts in Section 4 above.</li>
    <li><strong>Scan the bill for errors.</strong> <a href="/scan">Upload to BillKarma</a> to check for duplicate charges, upcoding, and inflated markups even if the amounts match.</li>
</ol>

<div class="key-takeaway">
    <strong>If a provider threatens collections before your insurer has processed the claim,</strong> send a letter stating: &ldquo;I am disputing this bill pending insurance claim processing. My claim is pending with [insurer], claim reference #[number]. Please do not refer this account to collections while the claim is being processed.&rdquo; Providers cannot legally send you to collections for a bill that is still being processed by insurance.
</div>

<h2 id="when-eob-wrong">6. What if the EOB is wrong?</h2>

<p>Sometimes the EOB itself contains errors. Signs the EOB may be wrong:</p>

<ul>
    <li>The allowed amount seems too high or too low for the service</li>
    <li>Your deductible balance doesn&rsquo;t match what you&rsquo;ve paid year-to-date</li>
    <li>A service is denied that should be covered (wrong code, wrong diagnosis)</li>
    <li>The EOB shows an out-of-network rate for an in-network provider</li>
    <li>Preventive care that should be free is being applied to your deductible</li>
</ul>

<p>If the EOB is wrong, call your insurer and ask them to reprocess the claim. Common fixable errors:</p>

<ul>
    <li><strong>Preventive care coded incorrectly:</strong> If a routine screening (colonoscopy, mammogram, annual physical) was processed as diagnostic instead of preventive, you may owe a deductible/copay when it should be free. Ask your provider to resubmit with the correct preventive care diagnosis code.</li>
    <li><strong>Wrong provider network status:</strong> If an in-network provider was processed as out-of-network, call your insurer to correct the provider&rsquo;s network status on the claim.</li>
    <li><strong>Coordination of benefits error:</strong> If you have two insurance plans, the primary insurer may not have been identified correctly. Call both insurers to correct the coordination of benefits order.</li>
</ul>

<h2 id="faq">Frequently asked questions</h2>

<div class="faq-section">
    <div class="faq-item">
        <h3>Why is my medical bill different from my EOB?</h3>
        <p>The provider bill shows the chargemaster rate (before insurance). The EOB shows the negotiated allowed amount and your actual patient responsibility. For in-network care, you owe only the patient responsibility on the EOB. Common causes of mismatch: bill arrived before insurance processed the claim, denied charges, balance billing, or coding errors.</p>
    </div>
    <div class="faq-item">
        <h3>Should I pay the bill or the EOB amount?</h3>
        <p>Pay the &ldquo;patient responsibility&rdquo; amount on the EOB, not the provider bill amount. For in-network care, the provider is contractually required to accept the insurer&rsquo;s allowed amount as payment in full. If your bill exceeds the EOB patient responsibility, call the provider to request an adjustment.</p>
    </div>
    <div class="faq-item">
        <h3>How long should I wait for an EOB before paying?</h3>
        <p>Claims typically process in 14&ndash;45 days. Wait until you&rsquo;ve received and reviewed the EOB before paying any medical bill. Check your insurer&rsquo;s online portal for faster access to EOBs. If no EOB appears within 30 days, call your insurer to check the claim status.</p>
    </div>
    <div class="faq-item">
        <h3>What if my provider is balance billing me?</h3>
        <p>Balance billing (charging more than the allowed amount) is prohibited for in-network providers under their insurance contracts. For out-of-network emergency services, it&rsquo;s prohibited by the No Surprises Act. Call the provider with your EOB and request they adjust the bill to the patient responsibility amount. If they refuse, contact your insurer for help.</p>
    </div>
    <div class="faq-item">
        <h3>Can the EOB itself be wrong?</h3>
        <p>Yes. Common EOB errors: preventive care coded as diagnostic (costing you a copay when it should be free), wrong provider network status, incorrect deductible calculation, or coordination of benefits error. Call your insurer to request a claim reprocessing if the EOB amounts seem incorrect.</p>
    </div>
</div>

<h2 id="sources">Sources</h2>

<ul class="sources-list">
    <li><a href="https://www.cms.gov/medical-bill-rights" target="_blank" rel="noopener">CMS: Know Your Medical Bill Rights</a></li>
    <li><a href="https://www.consumerfinance.gov/about-us/blog/know-your-rights-and-protections-when-it-comes-to-medical-bills-and-collections/" target="_blank" rel="noopener">CFPB: Know Your Rights with Medical Bills and Collections</a></li>
    <li><a href="https://www.healthcare.gov/using-marketplace-coverage/getting-emergency-care/" target="_blank" rel="noopener">HealthCare.gov: Understanding Your EOB and Billing Rights</a></li>
    <li><a href="https://www.cms.gov/nosurprises" target="_blank" rel="noopener">CMS: No Surprises Act Protections</a></li>
    <li><a href="https://www.patientrightsadvocate.org/how-to-fight-medical-bill-overcharges" target="_blank" rel="noopener">Patient Rights Advocate: How to Fight Medical Bill Overcharges</a></li>
</ul>
""",
})
