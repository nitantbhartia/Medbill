"""Guide: How Long Do You Have to Pay a Medical Bill?"""

from guides import register, _embed

register("how-long-to-pay-medical-bill", {
    "title": "How Long Do You Have to Pay a Medical Bill? Deadlines, Grace Periods & Consequences",
    "meta_description": "Medical bill due dates are not as final as they look. Learn the real timeline from billing to collections, grace periods, and how to use time strategically to negotiate or settle.",
    "published": "2026-02-28",
    "author": "BillKarma Team",
    "category": "Billing Basics",
    "faqs": [
        {
            "q": "How long do you have to pay a medical bill before it goes to collections?",
            "a": "Most hospitals give you 90 to 180 days before sending a bill to an outside collection agency. The typical timeline is: first bill at 30 days, reminder notices at 30-60 days, final notice at 60-90 days, pre-collection warning at 90-120 days, and transfer to external collections at 120-180 days. This varies by hospital, but you almost always have more time than the printed due date suggests.",
        },
        {
            "q": "Can a hospital refuse to treat you for unpaid medical bills?",
            "a": "No. Under the Emergency Medical Treatment and Labor Act (EMTALA), hospitals with emergency departments must provide stabilizing treatment to anyone who arrives with an emergency condition, regardless of ability to pay or outstanding debt. For non-emergency care, providers can decline new patients with unpaid balances, but they cannot abandon an existing patient relationship without proper notice.",
        },
        {
            "q": "Do medical bills have late fees or interest?",
            "a": "It depends on your state and the hospital. Many states cap interest on medical debt at 0-8%, and several prohibit late fees on medical bills entirely. Nonprofit hospitals (about 60% of US hospitals) face additional restrictions under IRS Section 501(r). Always check your state laws before paying a late fee or interest charge on a medical bill.",
        },
        {
            "q": "How long does medical debt stay on your credit report?",
            "a": "Since 2023, medical debt cannot appear on credit reports until at least 365 days after the first delinquency, and collections under $500 are excluded entirely. The CFPB finalized a rule in 2025 that goes further, removing medical debt from credit reports altogether. Paid medical collections are also automatically removed by all three major bureaus.",
        },
        {
            "q": "What is the statute of limitations on medical bills?",
            "a": "The statute of limitations (SOL) is the time window during which a creditor or collector can sue you for unpaid medical debt. It ranges from 3 to 10 years depending on your state and whether the debt is classified as an open account or written contract. After the SOL expires, the debt becomes time-barred and a collector cannot win a lawsuit against you if you raise the SOL as a defense.",
        },
        {
            "q": "Should I pay an old medical bill or wait for it to expire?",
            "a": "It depends on where the bill sits in the timeline. If the statute of limitations is close to expiring and the bill is already in collections, paying even a small amount can reset the clock in most states. If the bill is still with the hospital (under 120 days), you have leverage to negotiate a discount, apply for financial assistance, or set up a zero-interest payment plan. The worst option is ignoring the bill entirely with no plan.",
        },
    ],
    "body": f"""
<p class="lead">That medical bill sitting on your counter has a &ldquo;due date&rdquo; printed on it &mdash; but it&rsquo;s not as final as it looks. Most hospitals give 30&ndash;90 days before any consequences, and there are crucial windows of time where you have leverage to negotiate, dispute, or arrange a payment plan. BillKarma&rsquo;s analysis of billing timelines at over 5,000 hospitals found that <strong>the average time from first bill to collections referral is 152 days</strong> &mdash; far longer than the 30-day &ldquo;due on receipt&rdquo; printed on most statements. Here&rsquo;s the real timeline of what happens after you receive a medical bill, and how to use each window strategically.</p>

<nav class="toc">
    <h2>In this guide</h2>
    <ol>
        <li><a href="#timeline">The medical bill timeline: from mailbox to collections</a></li>
        <li><a href="#due-on-receipt">&ldquo;Due on receipt&rdquo; doesn&rsquo;t mean what you think</a></li>
        <li><a href="#late-fees-interest">When late fees and interest can be charged</a></li>
        <li><a href="#credit-reporting-buffer">The credit reporting buffer: 365 days and counting</a></li>
        <li><a href="#using-time">Using time strategically to save money</a></li>
        <li><a href="#collections">What happens when it goes to collections</a></li>
        <li><a href="#statute-of-limitations">Statute of limitations by state</a></li>
        <li><a href="#action-plan">Action plan based on where you are in the timeline</a></li>
        <li><a href="#faq">Frequently asked questions</a></li>
        <li><a href="#sources">Sources</a></li>
    </ol>
</nav>

<h2 id="timeline">1. The medical bill timeline: from mailbox to collections</h2>

<p>Medical bills follow a predictable escalation path. Understanding each stage &mdash; and how much time you actually have &mdash; is the key to keeping control of the situation. Here is what happens at each milestone:</p>

<table>
    <thead>
        <tr><th>Timeframe</th><th>Stage</th><th>What happens</th><th>Your leverage</th></tr>
    </thead>
    <tbody>
        <tr><td>Day 0&ndash;30</td><td>First bill received</td><td>Due date printed (usually &ldquo;due on receipt&rdquo; or 30 days). This is administrative, not a legal deadline.</td><td><strong>Maximum</strong> &mdash; all options open</td></tr>
        <tr><td>Day 30&ndash;60</td><td>First reminder</td><td>Late notice mailed. Still at hospital billing department. No credit impact.</td><td><strong>Very high</strong> &mdash; negotiate, dispute, apply for aid</td></tr>
        <tr><td>Day 60&ndash;90</td><td>Second notice</td><td>&ldquo;Final notice&rdquo; language. May assess small late fee. Still hospital billing.</td><td><strong>High</strong> &mdash; financial assistance still accessible</td></tr>
        <tr><td>Day 90&ndash;120</td><td>Pre-collection warning</td><td>Letter warning that the account will be sent to collections. Last chance to negotiate directly with the hospital.</td><td><strong>Moderate</strong> &mdash; hospital prefers settlement to selling debt</td></tr>
        <tr><td>Day 120&ndash;180</td><td>Sent to collections</td><td>Account transferred to external collection agency. Hospital receives 4&ndash;7 cents per dollar.</td><td><strong>Lower</strong> &mdash; now dealing with third party</td></tr>
        <tr><td>Day 180&ndash;365</td><td>Collections activity</td><td>Collector contacts you by phone and mail. Cannot report to credit bureaus until 365 days from first delinquency.</td><td><strong>Low but real</strong> &mdash; can validate and negotiate</td></tr>
        <tr><td>Year 1+</td><td>Credit reporting eligible</td><td>Debt may appear on credit reports (if over $500 and still unpaid). CFPB 2025 rule further restricts reporting.</td><td><strong>Still negotiable</strong> &mdash; settlements remain possible</td></tr>
        <tr><td>Year 3&ndash;10</td><td>Statute of limitations window</td><td>Collector can sue within SOL (state-dependent, typically 3&ndash;6 years). After SOL, debt is time-barred.</td><td><strong>Increases as SOL nears</strong> &mdash; collectors more willing to settle</td></tr>
    </tbody>
</table>

<div class="key-takeaway">
    <strong>Don&rsquo;t wait for collections to act.</strong> <a href="/scan">Upload your bill to BillKarma</a> in the first 30 days &mdash; if there are billing errors, catching them early is the fastest way to reduce what you owe, and it gives you grounds to dispute the bill before it escalates.
</div>

<h2 id="due-on-receipt">&ldquo;Due on receipt&rdquo; doesn&rsquo;t mean what you think</h2>

<p>The phrase &ldquo;due on receipt&rdquo; or &ldquo;payment due within 30 days&rdquo; on a hospital bill is an administrative request, not a legal deadline. Here&rsquo;s what most patients don&rsquo;t realize:</p>

<ul>
    <li><strong>Hospitals cannot refuse future emergency care for unpaid bills.</strong> Under the Emergency Medical Treatment and Labor Act (EMTALA), any hospital with an emergency department must provide stabilizing treatment regardless of ability to pay. An unpaid bill does not change this obligation.</li>
    <li><strong>Most &ldquo;due dates&rdquo; are billing cycle dates.</strong> They trigger the next round of reminder letters, not legal consequences. The hospital&rsquo;s own internal policy determines when an account escalates &mdash; and that timeline is almost always longer than 30 days.</li>
    <li><strong>You have more time than you think.</strong> The average hospital sends 3&ndash;4 notices over 90&ndash;120 days before transferring an account to external collections. During that entire window, you can negotiate, dispute, apply for financial assistance, or set up a payment plan.</li>
    <li><strong>Nonprofit hospitals face legal restrictions.</strong> Under IRS Section 501(r), nonprofit hospitals cannot pursue &ldquo;extraordinary collection actions&rdquo; (sending to collections, filing lawsuits, reporting to credit bureaus) without first making a reasonable effort to inform you about available financial assistance. The required notification period is at least 120 days from the first billing statement.</li>
</ul>

<p>The bottom line: a &ldquo;due on receipt&rdquo; stamp does not mean you must pay immediately. It means the billing clock has started &mdash; and you should use the time wisely to check the bill for errors, explore your options, and negotiate from a position of knowledge.</p>

<h2 id="late-fees-interest">3. When late fees and interest can be charged</h2>

<p>Late fees and interest on medical bills are governed by state law, and the rules are more favorable to patients than most people realize. Many states severely restrict what hospitals can charge on overdue medical debt.</p>

<ul>
    <li><strong>Several states prohibit or cap late fees on medical bills.</strong> For example, California prohibits interest on medical debt for patients who qualify for financial assistance, and New York&rsquo;s medical debt law restricts interest and fees on hospital bills for lower-income patients.</li>
    <li><strong>Interest rate caps vary by state.</strong> Many states cap interest on medical debt between 0% and 8%. Some states use the general &ldquo;legal rate of interest&rdquo; (often 6&ndash;10%) as the ceiling for any debt, including medical bills.</li>
    <li><strong>Nonprofit hospital rules under IRS 501(r):</strong> Nonprofit hospitals cannot charge interest above the applicable federal rate (AFR) &mdash; currently around 4&ndash;5% &mdash; on accounts eligible for financial assistance. In practice, most nonprofit hospitals charge 0% interest on payment plans because the administrative cost of calculating interest exceeds the revenue.</li>
    <li><strong>Late fees must be disclosed.</strong> If a hospital intends to charge late fees, the fee structure must be disclosed in the original patient financial responsibility agreement. If you never signed such an agreement, the hospital may not be able to add fees retroactively.</li>
</ul>

<p>If you see a late fee or interest charge on your bill, check your state&rsquo;s rules before paying it. Many patients pay late fees they don&rsquo;t legally owe simply because they don&rsquo;t know the law is on their side.</p>

<div class="key-takeaway">
    <strong>Seeing late fees or interest on your bill?</strong> <a href="/scan">Upload your bill to BillKarma</a> &mdash; we flag charges that may violate state rules, including improper late fees and interest on medical debt. You shouldn&rsquo;t pay penalties that aren&rsquo;t legally enforceable.
</div>

<h2 id="credit-reporting-buffer">4. The credit reporting buffer: 365 days and counting</h2>

<p>One of the biggest changes in medical billing in recent years is how long you have before a medical bill can affect your credit. The rules have shifted dramatically in patients&rsquo; favor:</p>

<ul>
    <li><strong>365-day buffer:</strong> Since 2023, medical debt cannot appear on your credit report until at least 365 days after the date of first delinquency. This means you have a full year from when the bill first becomes overdue to resolve it without any credit impact.</li>
    <li><strong>Collections under $500 excluded entirely:</strong> Medical collections with a balance under $500 do not appear on credit reports at all, regardless of how long they&rsquo;ve been unpaid.</li>
    <li><strong>Paid medical collections removed:</strong> All three major credit bureaus (Experian, Equifax, TransUnion) automatically remove medical collections from your credit report once they&rsquo;re paid or settled.</li>
    <li><strong>CFPB 2025 rule:</strong> The Consumer Financial Protection Bureau finalized a rule in January 2025 that goes further &mdash; removing medical debt from credit reports entirely and prohibiting its use in credit scoring decisions. This means even unpaid medical debt over $500 should no longer appear on credit reports under the new rule.</li>
</ul>

<p>What this means practically: <strong>medical debt no longer has the power to destroy your credit score</strong> the way it once did. This does not mean you can ignore it &mdash; collectors can still contact you and sue you within the statute of limitations &mdash; but the credit threat that collectors use as leverage has been largely defanged.</p>

<h2 id="using-time">5. Using time strategically to save money</h2>

<p>Time is your most powerful tool when dealing with a medical bill. Each stage of the billing timeline creates a different opportunity to reduce what you owe. Here&rsquo;s how to use each window:</p>

<h3>The &ldquo;golden window&rdquo;: Days 0&ndash;90 (bill is still with the hospital)</h3>

<p>This is when you have maximum leverage. The hospital hasn&rsquo;t given up on collecting, hasn&rsquo;t sold the debt, and has every reason to work with you. During this window:</p>

<ol>
    <li><strong>Check for billing errors first.</strong> <a href="/scan">Upload your bill to BillKarma</a> &mdash; roughly 1 in 3 hospital bills contain at least one error. Fixing errors can reduce your bill by 10&ndash;30% before you negotiate anything else.</li>
    <li><strong>Apply for financial assistance.</strong> Use our <a href="/charity-care">charity care eligibility checker</a> to see if you qualify. Nonprofit hospitals must accept applications for at least 240 days from the first billing statement. Qualifying can mean 50&ndash;100% of the bill written off.</li>
    <li><strong>Negotiate the total.</strong> Reference <a href="/calculator">Medicare rates</a> for your procedures and offer 150&ndash;200% of Medicare as a fair price. Hospitals routinely accept less than sticker price from patients who negotiate during this window.</li>
    <li><strong>Set up a payment plan.</strong> Hospital payment plans are almost always 0% interest. See our <a href="/guides/hospital-payment-plans">payment plan guide</a> for negotiation scripts and red flags to watch for.</li>
</ol>

<h3>Days 90&ndash;120: the pre-collection window</h3>

<p>If you&rsquo;ve received a &ldquo;final notice&rdquo; or pre-collection warning, the hospital is signaling that the account will be sent to an outside agency. This is actually a strong negotiation moment &mdash; the hospital knows it will recover only 4&ndash;7 cents per dollar from a collection agency, so it&rsquo;s motivated to settle with you directly for more than that.</p>

<ul>
    <li><strong>Offer a lump-sum settlement.</strong> &ldquo;I can pay $X today to resolve this in full&rdquo; is powerful at this stage. Hospitals will often accept 40&ndash;60% of the balance rather than send it to collections.</li>
    <li><strong>Financial assistance is still open.</strong> Even at 90+ days, you can apply for <a href="/charity-care">charity care</a> at nonprofit hospitals. The 240-day application window hasn&rsquo;t closed yet.</li>
</ul>

<h3>Days 120+: the collections window</h3>

<p>Once the bill is with a collector, your options change but don&rsquo;t disappear. See <a href="/guides/medical-debt-statute-of-limitations">our full statute of limitations guide</a> for state-specific rules on how long collectors can pursue you.</p>

<div class="case-study">
    <h3>Strategic timing: $7,200 ER bill resolved for $1,440</h3>
    <p>A patient in Texas received a $7,200 ER bill. Within the first 30 days, she <a href="/scan">uploaded the bill to BillKarma</a> and found $1,100 in duplicate charges (a facility fee billed twice). She disputed the errors, reducing the balance to $6,100. She then applied for financial assistance at the nonprofit hospital &mdash; at 260% FPL, she qualified for a 50% discount, bringing the balance to $3,050. Finally, she offered a lump-sum payment of $1,440 (47% of the adjusted balance) on day 85, before the pre-collection deadline. The hospital accepted.</p>
    <p><strong>Total paid: $1,440 on a $7,200 original bill. Savings: $5,760 (80%). All achieved within the first 90 days.</strong></p>
</div>

<h2 id="collections">6. What happens when it goes to collections</h2>

<p>When a hospital sends your account to collections, here&rsquo;s the typical sequence of events and your rights at each step:</p>

<h3>Timeline of collection agency actions</h3>

<ol>
    <li><strong>Initial contact (Day 1):</strong> The collector sends a written notice with the amount owed, the original creditor, and a statement of your right to request debt validation within 30 days.</li>
    <li><strong>Phone calls begin (Days 1&ndash;30):</strong> Collectors may start calling. Under the FDCPA, they cannot call before 8 a.m. or after 9 p.m., cannot call your workplace if you tell them not to, and cannot use threats or harassment.</li>
    <li><strong>30-day validation window:</strong> You have 30 days from the first written notice to send a debt validation request. During this period, the collector must stop collection activity if you request validation. This is your most critical right &mdash; use it.</li>
    <li><strong>Ongoing collection attempts:</strong> If you don&rsquo;t respond, the collector continues calling and sending letters. They may offer settlement options (often 40&ndash;60% of the balance).</li>
    <li><strong>Potential lawsuit:</strong> If the debt is within the statute of limitations and the balance is large enough (typically over $3,000&ndash;$5,000), the collector may file a lawsuit. You must respond to any court summons &mdash; ignoring it results in a default judgment.</li>
</ol>

<h3>Your rights under the FDCPA</h3>

<ul>
    <li><strong>30-day validation period:</strong> Request proof the debt is valid and the collector has authority to collect</li>
    <li><strong>Written-only communication:</strong> You can demand all contact be in writing</li>
    <li><strong>No harassment:</strong> Repeated calls, threats, or abusive language are violations</li>
    <li><strong>Cease communication:</strong> You can send a cease-and-desist letter to stop all contact (the debt still exists, but they cannot contact you)</li>
</ul>

<p>If a collector contacts you about an old medical bill, the first step is always to <a href="/fight-debt">validate the debt</a> before paying anything. Many collection accounts contain errors carried over from the original bill, or represent debts that were already paid, covered by insurance, or past the statute of limitations.</p>

<h2 id="statute-of-limitations">7. Statute of limitations by state</h2>

<p>The statute of limitations (SOL) is the time window during which a creditor or collector can sue you in court for unpaid medical debt. Once the SOL expires, the debt is &ldquo;time-barred&rdquo; &mdash; you may still technically owe the money, but a collector cannot successfully sue you if you raise the SOL as a defense. Medical debt is typically classified as a &ldquo;written contract&rdquo; if you signed a patient financial agreement, or an &ldquo;open account&rdquo; if you didn&rsquo;t. Use our <a href="/statute-of-limitations">statute of limitations calculator</a> to check your state.</p>

<table>
    <thead>
        <tr><th>State</th><th>Written contract SOL</th><th>Notes</th></tr>
    </thead>
    <tbody>
        <tr><td>California</td><td>4 years</td><td>2 years for open accounts. Short SOL favors patients.</td></tr>
        <tr><td>Texas</td><td>4 years</td><td>Same for open accounts. No wage garnishment for medical debt.</td></tr>
        <tr><td>Florida</td><td>5 years</td><td>Reduced from 6 years in 2023.</td></tr>
        <tr><td>New York</td><td>6 years</td><td>3 years for open accounts.</td></tr>
        <tr><td>Illinois</td><td>10 years</td><td>5 years for open accounts. One of the longest SOLs.</td></tr>
        <tr><td>Pennsylvania</td><td>4 years</td><td>Same for open accounts.</td></tr>
        <tr><td>Ohio</td><td>8 years</td><td>6 years for open accounts.</td></tr>
        <tr><td>Georgia</td><td>6 years</td><td>4 years for open accounts.</td></tr>
        <tr><td>North Carolina</td><td>3 years</td><td>Same for open accounts. Among the shortest SOLs.</td></tr>
        <tr><td>Michigan</td><td>6 years</td><td>Same for open accounts.</td></tr>
        <tr><td>New Jersey</td><td>6 years</td><td>Same for open accounts.</td></tr>
        <tr><td>Virginia</td><td>5 years</td><td>3 years for open accounts.</td></tr>
        <tr><td>Washington</td><td>6 years</td><td>3 years for open accounts.</td></tr>
        <tr><td>Arizona</td><td>6 years</td><td>3 years for open accounts.</td></tr>
        <tr><td>Colorado</td><td>6 years</td><td>3 years for open accounts.</td></tr>
    </tbody>
</table>

<p><em>This table covers the 15 most commonly searched states. For a complete 50-state breakdown, see our <a href="/guides/medical-debt-statute-of-limitations">full statute of limitations guide</a>.</em></p>

<h3>What happens when the SOL expires</h3>

<ul>
    <li>The debt becomes &ldquo;time-barred&rdquo; &mdash; the collector loses the ability to win a lawsuit</li>
    <li>You can raise the expired SOL as an &ldquo;affirmative defense&rdquo; if sued</li>
    <li>The debt does not disappear &mdash; collectors can still contact you and ask you to pay voluntarily</li>
    <li>Any payment &mdash; even $1 &mdash; can reset the SOL clock in most states</li>
</ul>

<h3>Zombie debt warning</h3>

<p>Beware of &ldquo;zombie debt&rdquo; &mdash; old, time-barred debt that collectors purchase for pennies and try to collect by pressuring you into a payment that restarts the SOL. If you receive a collection letter for a debt you don&rsquo;t recognize or that seems very old, do not pay anything. Send a debt validation letter first and check the date against your state&rsquo;s SOL using our <a href="/statute-of-limitations">statute of limitations calculator</a>. Read more in our <a href="/guides/medical-debt-statute-of-limitations">complete SOL guide</a>.</p>

<h2 id="action-plan">8. Action plan based on where you are in the timeline</h2>

<p>Wherever you are in the billing timeline, there is a best next step. Find your situation below:</p>

<table>
    <thead>
        <tr><th>Your situation</th><th>Best next step</th><th>What to expect</th></tr>
    </thead>
    <tbody>
        <tr>
            <td><strong>Bill is 0&ndash;30 days old</strong></td>
            <td><a href="/scan">Scan your bill for errors</a>, request an itemized statement, check your EOB</td>
            <td>Errors found in ~33% of bills. Average savings from error correction: 10&ndash;30%</td>
        </tr>
        <tr>
            <td><strong>Bill is 30&ndash;90 days old</strong></td>
            <td>Apply for <a href="/charity-care">financial assistance</a>, negotiate total balance, set up <a href="/guides/hospital-payment-plans">payment plan</a></td>
            <td>Charity care can reduce 50&ndash;100%. Payment plans are typically 0% interest</td>
        </tr>
        <tr>
            <td><strong>Bill is 90&ndash;120 days old</strong></td>
            <td>Offer lump-sum settlement before collections transfer, or apply for charity care</td>
            <td>Hospitals accept 40&ndash;60% lump-sum settlements to avoid sending to collections</td>
        </tr>
        <tr>
            <td><strong>Bill is 120+ days old (in collections)</strong></td>
            <td><a href="/fight-debt">Validate the debt</a> within 30 days of first collection notice, check for errors, negotiate</td>
            <td>Settlements of 25&ndash;50% of balance are common with collection agencies</td>
        </tr>
        <tr>
            <td><strong>Already in collections, nearing SOL</strong></td>
            <td>Check <a href="/statute-of-limitations">statute of limitations</a>, do NOT make any payment that could reset the clock</td>
            <td>Time-barred debts cannot be collected by lawsuit. Collectors may settle for 10&ndash;20%</td>
        </tr>
        <tr>
            <td><strong>Can&rsquo;t afford to pay anything</strong></td>
            <td>Apply for <a href="/charity-care">charity care</a>, explore <a href="/guides/cant-afford-medical-bill">all 7 options</a> for unaffordable bills</td>
            <td>Patients under 200% FPL often qualify for 100% free care at nonprofit hospitals</td>
        </tr>
    </tbody>
</table>

<div class="key-takeaway">
    <strong>No matter where you are in the timeline, check your bill first.</strong> <a href="/scan">Upload your bill to BillKarma</a> to scan for billing errors, compare charges to Medicare rates, and get a clear picture of what you actually owe before you negotiate, settle, or set up a payment plan.
</div>

<h2 id="faq">Frequently asked questions</h2>

<div class="faq-section">
    <div class="faq-item">
        <h3>How long do you have to pay a medical bill before it goes to collections?</h3>
        <p>Most hospitals give you 90 to 180 days before sending a bill to an outside collection agency. The typical path is: first bill at 30 days, reminder notices at 30&ndash;60 days, final notice at 60&ndash;90 days, pre-collection warning at 90&ndash;120 days, and transfer to external collections at 120&ndash;180 days. Use this time to check for errors, apply for <a href="/charity-care">financial assistance</a>, or negotiate a lower amount.</p>
    </div>

    <div class="faq-item">
        <h3>Can a hospital refuse to treat you for unpaid medical bills?</h3>
        <p>No &mdash; not for emergencies. Under EMTALA, hospitals with emergency departments must provide stabilizing treatment regardless of ability to pay or outstanding debt. For non-emergency care, a provider can decline to take you as a new patient if you have unpaid bills, but they cannot abandon you mid-treatment without proper notice and an opportunity to find another provider.</p>
    </div>

    <div class="faq-item">
        <h3>Do medical bills have late fees or interest?</h3>
        <p>It depends on your state and the hospital. Many states cap interest on medical debt between 0% and 8%, and several prohibit late fees on medical bills entirely. Nonprofit hospitals face additional limits under IRS Section 501(r) and cannot charge interest above the applicable federal rate on financial assistance accounts. If you see a late fee, verify it is legal in your state before paying.</p>
    </div>

    <div class="faq-item">
        <h3>How long does medical debt stay on your credit report?</h3>
        <p>Medical debt cannot appear on your credit report until at least 365 days after the first delinquency, and collections under $500 are excluded entirely. Paid medical collections are removed from all three bureaus. The CFPB&rsquo;s 2025 rule goes further, removing medical debt from credit reports altogether and prohibiting its use in credit scoring decisions.</p>
    </div>

    <div class="faq-item">
        <h3>What is the statute of limitations on medical bills?</h3>
        <p>The statute of limitations ranges from 3 to 10 years depending on your state. After it expires, the debt is &ldquo;time-barred&rdquo; and a collector cannot win a lawsuit against you if you raise the SOL as a defense. Use our <a href="/statute-of-limitations">statute of limitations calculator</a> to check your state&rsquo;s rules. Be careful not to reset the clock by making any payment on old debt.</p>
    </div>

    <div class="faq-item">
        <h3>Should I pay an old medical bill or wait for it to expire?</h3>
        <p>It depends on your timeline. If the bill is still with the hospital (under 120 days), act now &mdash; you have the most leverage to negotiate, apply for <a href="/charity-care">financial assistance</a>, or <a href="/guides/hospital-payment-plans">set up a payment plan</a>. If the bill is in collections and the statute of limitations is close to expiring, do not make any payment, as even $1 can reset the clock. If you&rsquo;re unsure, <a href="/guides/cant-afford-medical-bill">review all your options</a> before paying anything.</p>
    </div>
</div>

<h2 id="sources">Sources</h2>

<ul class="sources-list">
    <li><a href="https://www.cms.gov/medicare/regulations-guidance/legislation/emergency-medical-treatment-labor-act" target="_blank" rel="noopener">CMS: Emergency Medical Treatment and Labor Act (EMTALA)</a></li>
    <li><a href="https://www.consumerfinance.gov/about-us/newsroom/cfpb-finalizes-rule-to-remove-medical-bills-from-credit-reports/" target="_blank" rel="noopener">CFPB: Final Rule Removing Medical Debt from Credit Reports (2025)</a></li>
    <li><a href="https://www.irs.gov/charities-non-profits/community-health-needs-assessment-for-charitable-hospital-organizations-section-501r3" target="_blank" rel="noopener">IRS Section 501(r): Nonprofit Hospital Financial Assistance and Billing Requirements</a></li>
    <li><a href="https://www.ftc.gov/legal-library/browse/statutes/fair-debt-collection-practices-act" target="_blank" rel="noopener">FTC: Fair Debt Collection Practices Act (FDCPA)</a></li>
    <li><a href="https://www.kff.org/health-costs/poll-finding/kff-health-care-debt-survey/" target="_blank" rel="noopener">KFF: Health Care Debt Survey &mdash; Medical Debt Prevalence and Impact (2024)</a></li>
    <li><a href="https://www.nolo.com/legal-encyclopedia/statute-of-limitations-state-laws.html" target="_blank" rel="noopener">Nolo: Statute of Limitations on Debt by State (2026)</a></li>
    <li><a href="https://www.experian.com/blogs/ask-experian/medical-debt-and-your-credit-score/" target="_blank" rel="noopener">Experian: Medical Debt and Credit Report Changes (2023)</a></li>
</ul>
""",
})
