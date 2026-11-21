"""Guide: EOB Denial Codes Decoded: CO-45, PR-1, CO-97 and More."""

from guides import register

register("eob-denial-codes-explained", {
    "title": "EOB Denial Codes Decoded: CO-45, PR-1, CO-97 and More",
    "meta_description": "What EOB denial codes like CO-45, PR-1 and CO-97 mean in plain English, who owes the amount, and what to do next, with a lookup table of 17 common codes.",
    "published": "2026-11-20",
    "reviewed_on": "2026-11-20",
    "author": "BillKarma Team",
    "category": "Understanding Your Bill",
    "faqs": [
        {
            "q": "What does CO-45 mean on my EOB?",
            "a": "CO-45 means the provider charged more than the amount your plan allows under its fee schedule or contract. CO stands for Contractual Obligation, which assigns that amount to the provider, not you. An in-network provider generally may not bill you the difference for covered services.",
        },
        {
            "q": "What is the difference between CO and PR on an EOB?",
            "a": "Both are group codes that say who is responsible for an adjustment. CO (Contractual Obligation) assigns the amount to the provider. PR (Patient Responsibility) assigns it to you, such as your deductible (PR-1), coinsurance (PR-2) or copay (PR-3).",
        },
        {
            "q": "What does CO-97 mean?",
            "a": "CO-97 means the plan treats this service as part of the payment for another service it already processed (bundling). The CO group assigns the amount to the provider, so ask them to remove it if it shows up on your bill.",
        },
        {
            "q": "My EOB uses codes I can't find on any list. Why?",
            "a": "Some insurers print their own short codes instead of the standard X12 codes. The EOB should explain them. Look for a legend at the bottom or back of the EOB, or call the number on your card and ask for the full reason in writing.",
        },
        {
            "q": "How long do I have to appeal a denied claim?",
            "a": "For most job-based and individual plans, federal rules give you at least 180 days after you receive the denial to file an internal appeal. External review requests are generally due within four months of the final denial. Original Medicare appeals are due by the date on your Medicare Summary Notice.",
        },
    ],
    "body": f"""
<p class="lead">EOB denial codes are short labels that tell you why your health plan did not pay part of a bill, and who owes the rest. The two letters in front matter most: <strong>CO</strong> generally means the provider absorbs that amount, while <strong>PR</strong> means it is your share. Use the table below to decode the combos you are most likely to see, then decide what to do next.</p>

<nav class="toc">
    <h2>In this guide</h2>
    <ol>
        <li><a href="#how-to-read">How to read a code like CO-45</a></li>
        <li><a href="#lookup-table">Lookup table: 17 common codes</a></li>
        <li><a href="#example">Example: one line, four codes</a></li>
        <li><a href="#group-codes">Group codes: CO, PR, OA and PI</a></li>
        <li><a href="#remark-codes">Remark codes (RARCs)</a></li>
        <li><a href="#insurer-codes">When your EOB uses the insurer&rsquo;s own codes</a></li>
        <li><a href="#what-to-do">What to do, step by step</a></li>
        <li><a href="#appeal-rights">Your appeal rights</a></li>
        <li><a href="#faq">Frequently asked questions</a></li>
        <li><a href="#sources">Sources</a></li>
    </ol>
</nav>

<h2 id="how-to-read">1. How to read a code like CO-45</h2>

<p>An EOB (explanation of benefits) is the statement your plan sends after it processes a claim. It is not a bill. Each line may carry up to three codes:</p>

<ul>
    <li><strong>Group code</strong> (two letters, like CO or PR). This says who is responsible for the adjusted amount.</li>
    <li><strong>Claim Adjustment Reason Code</strong>, or CARC (a number, like 45). This says why the amount was adjusted.</li>
    <li><strong>Remark code</strong>, or RARC (letters and numbers, like M15 or N130). This adds detail.</li>
</ul>

<p>So <strong>CO-45</strong> reads as: group CO (Contractual Obligation) + reason 45 (charge is more than the allowed amount). X12, the group behind the standard for electronic insurance transactions, keeps the official code lists. CMS explains that group codes &ldquo;assign financial responsibility&rdquo; for the unpaid part of a claim.</p>

<div class="key-takeaway">
    <h3>Key takeaway</h3>
    <p>Before you pay, match each dollar on your bill to a group code on the EOB. Amounts marked CO are generally the provider&rsquo;s to absorb; amounts marked PR are yours. New to EOBs? Start with our <a href="/guides/explanation-of-benefits-eob/">explanation of benefits guide</a>.</p>
</div>

<h2 id="lookup-table">2. Lookup table: 17 common codes</h2>

<p>Official wording is from the X12 reason code list. The group shown is a common pairing; plans can pair a reason with a different group, so check what your EOB prints.</p>

<table>
    <thead>
        <tr>
            <th>Code</th>
            <th>Official reason (X12)</th>
            <th>Plain English</th>
            <th>What you can do</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>PR-1</td>
            <td>Deductible amount</td>
            <td>This goes toward your deductible. You owe it.</td>
            <td>Confirm the provider bills you no more than this amount.</td>
        </tr>
        <tr>
            <td>PR-2</td>
            <td>Coinsurance amount</td>
            <td>Your percentage share after the deductible.</td>
            <td>Check the math against your plan&rsquo;s coinsurance rate.</td>
        </tr>
        <tr>
            <td>PR-3</td>
            <td>Co-payment amount</td>
            <td>Your flat copay for the visit.</td>
            <td>Make sure you weren&rsquo;t charged the copay twice.</td>
        </tr>
        <tr>
            <td>CO-45</td>
            <td>Charge exceeds fee schedule/maximum allowable or contracted/legislated fee arrangement</td>
            <td>The provider charged more than the plan allows. With CO, the provider writes off the difference.</td>
            <td>If the bill includes this amount, ask the provider to remove it. If you see PR-45 instead, ask the plan why.</td>
        </tr>
        <tr>
            <td>CO-97</td>
            <td>The benefit for this service is included in the payment/allowance for another service/procedure that has already been adjudicated</td>
            <td>&ldquo;Bundled.&rdquo; This service is treated as part of another one already paid.</td>
            <td>Don&rsquo;t pay it separately. See our <a href="/guides/upcoding-unbundling-hospital-bills/">unbundling guide</a>.</td>
        </tr>
        <tr>
            <td>CO-16</td>
            <td>Claim/service lacks information or has submission/billing error(s)</td>
            <td>The claim was missing something or had a billing mistake.</td>
            <td>Ask the provider to fix and resubmit the claim. The remark code says what was missing.</td>
        </tr>
        <tr>
            <td>OA-18</td>
            <td>Exact duplicate claim/service</td>
            <td>The plan already got this exact claim.</td>
            <td>Usually nothing. Make sure you aren&rsquo;t billed twice for the same service.</td>
        </tr>
        <tr>
            <td>CO-50</td>
            <td>Non-covered services because this is not deemed a &ldquo;medical necessity&rdquo; by the payer</td>
            <td>The plan decided the service wasn&rsquo;t medically necessary.</td>
            <td>Ask for the criteria used and records from your doctor. Consider an appeal.</td>
        </tr>
        <tr>
            <td>CO-96 or PR-96</td>
            <td>Non-covered charge(s)</td>
            <td>The plan doesn&rsquo;t cover this charge. The remark code should say why.</td>
            <td>Read the remark code. If the group is PR, ask the plan which plan rule it used.</td>
        </tr>
        <tr>
            <td>PR-204</td>
            <td>This service/equipment/drug is not covered under the patient&rsquo;s current benefit plan</td>
            <td>Your plan excludes this item.</td>
            <td>Check your plan documents. Ask about an appeal or an exception.</td>
        </tr>
        <tr>
            <td>CO-197</td>
            <td>Precertification/authorization/notification/pre-treatment absent</td>
            <td>Nobody got prior approval before the service.</td>
            <td>Ask the provider if it requested approval, and ask the plan about an appeal.</td>
        </tr>
        <tr>
            <td>CO-29</td>
            <td>The time limit for filing has expired</td>
            <td>The provider sent the claim too late.</td>
            <td>Late filing is generally the provider&rsquo;s issue when the group is CO. Ask them to remove the charge.</td>
        </tr>
        <tr>
            <td>PR-27 (or PR-26)</td>
            <td>Expenses incurred after coverage terminated (26: prior to coverage)</td>
            <td>The plan thinks your coverage had ended (or hadn&rsquo;t started).</td>
            <td>Check your coverage dates. If you had other insurance, give it to the provider.</td>
        </tr>
        <tr>
            <td>CO-31</td>
            <td>Patient cannot be identified as our insured</td>
            <td>The plan couldn&rsquo;t match you to a member.</td>
            <td>Give the provider your exact name, birth date and member ID so it can resubmit.</td>
        </tr>
        <tr>
            <td>CO-22</td>
            <td>This care may be covered by another payer per coordination of benefits</td>
            <td>The plan thinks another insurer should pay first.</td>
            <td>Answer the plan&rsquo;s coordination of benefits questions. See our <a href="/guides/coordination-of-benefits-dual-insurance/">dual coverage guide</a>.</td>
        </tr>
        <tr>
            <td>OA-23</td>
            <td>The impact of prior payer(s) adjudication including payments and/or adjustments</td>
            <td>This reflects what your first insurer already paid or adjusted.</td>
            <td>Normal when you have two plans. Compare against the first plan&rsquo;s EOB.</td>
        </tr>
        <tr>
            <td>PR-119</td>
            <td>Benefit maximum for this time period or occurrence has been reached</td>
            <td>You used up the plan&rsquo;s limit for this service.</td>
            <td>Count your visits and ask the plan for its tally if it seems off.</td>
        </tr>
    </tbody>
</table>

<p>Per X12, codes like 16 and 96 must come with at least one remark code. If none is shown, ask for it.</p>

<h2 id="example">3. Example: one line, four codes</h2>

<p><strong>Example</strong> (sample numbers, not a real bill): a hospital bills $1,200 for a service. Your EOB shows:</p>

<ul>
    <li>Billed: $1,200. Allowed: $700.</li>
    <li>CO-45: $500 (the $1,200 charge minus the $700 allowed amount). The provider absorbs this.</li>
    <li>PR-1: $200 toward your deductible.</li>
    <li>PR-2: $100 coinsurance (20% of the remaining $500).</li>
    <li>Plan paid: $400.</li>
</ul>

<p>Check: $500 + $200 + $100 + $400 = $1,200. Your share is the PR lines only: $200 + $100 = <strong>$300</strong>. If the hospital bills you $800, the extra $500 is the CO-45 amount to question.</p>

<h2 id="group-codes">4. Group codes: CO, PR, OA and PI</h2>

<p>X12 says group codes &ldquo;categorize a payment adjustment.&rdquo; There are four in current use:</p>

<table>
    <thead>
        <tr>
            <th>Group</th>
            <th>Stands for</th>
            <th>What it means for you</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>CO</td>
            <td>Contractual Obligation</td>
            <td>CMS says CO &ldquo;assigns responsibility to the provider.&rdquo; Under Medicare, a Medicare contractor states the beneficiary &ldquo;may not be billed&rdquo; for these amounts.</td>
        </tr>
        <tr>
            <td>PR</td>
            <td>Patient Responsibility</td>
            <td>Your share: deductible, coinsurance, copay, or a non-covered service. CMS says Medicare patients may be billed only when PR is used.</td>
        </tr>
        <tr>
            <td>OA</td>
            <td>Other Adjustment</td>
            <td>Used when neither CO nor PR fits, such as OA-18 or OA-23. For Medicare, a contractor says neither patient nor supplier can be held responsible for it.</td>
        </tr>
        <tr>
            <td>PI</td>
            <td>Payor Initiated Reduction</td>
            <td>A cut the plan made on its own. Ask who is expected to cover it.</td>
        </tr>
    </tbody>
</table>

<p>That CMS rule is for Medicare. For private plans, HealthCare.gov says: &ldquo;A preferred provider may not balance bill you for covered services.&rdquo; (Balance billing means billing you the gap between the charge and the allowed amount.) Out-of-network providers differ; our <a href="/guides/balance-billing/">balance billing guide</a> covers when they can and can&rsquo;t bill you.</p>

<div class="key-takeaway">
    <h3>Key takeaway</h3>
    <p>If your hospital bill is higher than the PR total on your EOB, the difference is worth questioning. <a href="/scan">Check your bill free</a> to compare each line with Medicare rates and spot duplicates before you pay.</p>
</div>

<h2 id="remark-codes">5. Remark codes (RARCs)</h2>

<p>Remittance Advice Remark Codes add detail to a reason code. X12 describes two types: <strong>supplemental</strong> codes that explain a specific adjustment, and <strong>informational</strong> codes that start with &ldquo;Alert:&rdquo; and are never tied to one adjustment. A few you may see:</p>

<ul>
    <li><strong>M15:</strong> separately billed services were bundled because they are part of the same procedure.</li>
        <li><strong>N130:</strong> check your plan&rsquo;s benefit documents for limits on this service.</li>
        <li><strong>MA130:</strong> the claim had incomplete or invalid information, so the provider must send a new, corrected claim. There are no appeal rights on this one; it is a fix-and-resubmit job for the provider.</li>
    <li><strong>MA01:</strong> an alert that you may appeal if you disagree with the decision.</li>
</ul>

<h2 id="insurer-codes">6. When your EOB uses the insurer&rsquo;s own codes</h2>

<p>Not every EOB prints X12 codes. Some insurers use their own short codes instead. The Maryland Insurance Administration notes that &ldquo;the insurer may use codes to explain denial reasons,&rdquo; and that you should see an explanation of those codes on the EOB. CMS says remark code descriptions usually appear at the bottom of the EOB.</p>

<p>If the legend is vague, you can get more. For most job-based and individual plans, a denial notice must include the denial code and its meaning and the standard the plan used. On request, the plan must also give you the diagnosis and treatment codes and their meanings.</p>

<h2 id="what-to-do">7. What to do, step by step</h2>

<ol>
    <li><strong>Line up the EOB and the bill.</strong> Get an <a href="/guides/how-to-get-itemized-hospital-bill/">itemized bill</a>.</li>
    <li><strong>Add up the PR amounts.</strong> That is generally the most you should owe for the claim.</li>
    <li><strong>Flag any CO amount on your bill.</strong> Quote the EOB line and code to the billing office and ask them to remove it.</li>
    <li><strong>Sort fixable from disputable.</strong> Codes like 16 and 31 usually mean the provider needs to correct and resubmit the claim. Codes like 50, 96, 197 and 204 are plan decisions you can appeal.</li>
    <li><strong>Ask the plan for the full reason in writing.</strong> Use the request below.</li>
    <li><strong>Ask the provider to pause billing</strong> on disputed lines while you wait. Keep copies and dates.</li>
</ol>

<p>Sample request to your health plan:</p>

<pre>
To: [PLAN NAME] Member Services / Appeals
Member: [YOUR NAME], ID [MEMBER ID]
Claim: [CLAIM NUMBER], date of service [DATE], provider [PROVIDER NAME]

My EOB dated [EOB DATE] shows code [CODE, e.g. CO-50] on [SERVICE].
Please send me, free of charge:
1. The specific reason for this decision and the plan provision it is based on.
2. The denial code and its meaning, and the diagnosis and treatment codes
   and their meanings.
3. Any internal rule, guideline or criteria used to decide this claim.
4. If this was a medical necessity decision, the clinical reasoning.
5. Copies of all documents relevant to this claim.
6. Your appeal steps and deadlines.

[YOUR SIGNATURE], [DATE], [PHONE OR EMAIL]
</pre>

<div class="key-takeaway">
    <h3>Key takeaway</h3>
    <p>A denial code is the start of a conversation, not the end. Get the full reason and criteria in writing, then follow our <a href="/guides/how-to-appeal-insurance-denial/">step-by-step appeal guide</a> if the plan&rsquo;s decision still looks wrong.</p>
</div>

<h2 id="appeal-rights">8. Your appeal rights</h2>

<p>Two federal rules set the floor for most plans as of November 2026:</p>

<ul>
    <li><strong>29 CFR 2560.503-1</strong> (job-based plans under ERISA). A denial notice must give the specific reason, the plan provision used, and any internal guideline relied on (or offer a free copy). You get at least <strong>180 days</strong> to file an internal appeal and free access to documents relevant to your claim. With one appeal level, the plan generally must decide within 72 hours for urgent care, 30 days for care not yet received, and 60 days for care already received.</li>
    <li><strong>45 CFR 147.136</strong> (most non-grandfathered group and individual plans). It adopts the ERISA rules, adds the denial code requirement, and gives you the right to an <strong>external review</strong> by an independent reviewer. Under the federal process, you have <strong>four months</strong> after receiving the final denial to ask for one. Grandfathered plans (older plans that haven&rsquo;t changed much) are generally exempt from most of this section.</li>
</ul>

<p>Original Medicare is separate: you must file your first appeal by the date printed on your Medicare Summary Notice. Our guide to the <a href="/guides/medicare-summary-notice-vs-hospital-bill/">Medicare Summary Notice vs. your hospital bill</a> explains how to read it.</p>

<p>Your denial letter should list your exact deadlines. If a lot is at stake, consider talking to your state insurance department, legal aid, or a consumer attorney.</p>

<h2 id="faq">Frequently asked questions</h2>

<div class="faq-section">
    <div class="faq-item">
        <h3>What does CO-45 mean on my EOB?</h3>
        <p>CO-45 means the provider charged more than the amount your plan allows under its fee schedule or contract. CO stands for Contractual Obligation, which assigns that amount to the provider, not you. An in-network provider generally may not bill you the difference for covered services.</p>
    </div>
    <div class="faq-item">
        <h3>What is the difference between CO and PR on an EOB?</h3>
        <p>Both are group codes that say who is responsible for an adjustment. CO (Contractual Obligation) assigns the amount to the provider. PR (Patient Responsibility) assigns it to you, such as your deductible (PR-1), coinsurance (PR-2) or copay (PR-3).</p>
    </div>
    <div class="faq-item">
        <h3>What does CO-97 mean?</h3>
        <p>CO-97 means the plan treats this service as part of the payment for another service it already processed (bundling). The CO group assigns the amount to the provider, so ask them to remove it if it shows up on your bill.</p>
    </div>
    <div class="faq-item">
        <h3>My EOB uses codes I can&rsquo;t find on any list. Why?</h3>
        <p>Some insurers print their own short codes instead of the standard X12 codes. The EOB should explain them. Look for a legend at the bottom or back of the EOB, or call the number on your card and ask for the full reason in writing.</p>
    </div>
    <div class="faq-item">
        <h3>How long do I have to appeal a denied claim?</h3>
        <p>For most job-based and individual plans, federal rules give you at least 180 days after you receive the denial to file an internal appeal. External review requests are generally due within four months of the final denial. Original Medicare appeals are due by the date on your Medicare Summary Notice.</p>
    </div>
</div>

<h2 id="sources">Sources</h2>

<ul class="sources-list">
    <li><a href="https://x12.org/codes/claim-adjustment-reason-codes" target="_blank" rel="noopener">X12 &mdash; Claim Adjustment Reason Codes</a></li>
    <li><a href="https://x12.org/codes/claim-adjustment-group-codes" target="_blank" rel="noopener">X12 &mdash; Claim Adjustment Group Codes</a></li>
    <li><a href="https://x12.org/codes/remittance-advice-remark-codes" target="_blank" rel="noopener">X12 &mdash; Remittance Advice Remark Codes</a></li>
    <li><a href="https://www.cms.gov/medicare/coding-billing/electronic-billing/health-care-payment-remittance-advice" target="_blank" rel="noopener">CMS &mdash; Health Care Payment and Remittance Advice</a></li>
    <li><a href="https://med.noridianmedicare.com/web/jddme/topics/ra/claim-adjustment-group-codes" target="_blank" rel="noopener">Noridian Medicare &mdash; Claim Adjustment Group Codes</a></li>
    <li><a href="https://www.healthcare.gov/glossary/balance-billing/" target="_blank" rel="noopener">HealthCare.gov &mdash; Balance Billing (glossary)</a></li>
    <li><a href="https://cms.gov/medical-bill-rights/help/guides/explanation-of-benefits" target="_blank" rel="noopener">CMS &mdash; How to read an explanation of benefits (EOB)</a></li>
    <li><a href="https://insurance.maryland.gov/Consumer/Pages/EOB.aspx" target="_blank" rel="noopener">Maryland Insurance Administration &mdash; Explanation of Benefits</a></li>
    <li><a href="https://www.law.cornell.edu/cfr/text/29/2560.503-1" target="_blank" rel="noopener">29 CFR 2560.503-1 &mdash; Claims procedure (via Cornell LII)</a></li>
    <li><a href="https://www.law.cornell.edu/cfr/text/45/147.136" target="_blank" rel="noopener">45 CFR 147.136 &mdash; Internal claims and appeals and external review processes (via Cornell LII)</a></li>
    <li><a href="https://www.medicare.gov/providers-services/claims-appeals-complaints/appeals/original-medicare" target="_blank" rel="noopener">Medicare.gov &mdash; Appeals in Original Medicare</a></li>
</ul>
""",
})
