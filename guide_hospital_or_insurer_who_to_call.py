"""Guide: Hospital or Insurance? Who to Call for Each Bill Problem."""

from guides import register

register("hospital-or-insurer-who-to-call", {
    "title": "Hospital or Insurance? Who to Call for Each Bill Problem",
    "meta_description": "Call your insurer about denials and EOB amounts. Call the hospital about charges, codes and aid. A 14-row table shows who to call first for each problem.",
    "published": "2026-11-20",
    "reviewed_on": "2026-11-20",
    "author": "BillKarma Team",
    "category": "Taking Action",
    "faqs": [
        {
            "q": "Should I call the hospital or my insurance company about a bill?",
            "a": "Call the insurer when the problem is about coverage: a denied claim, how much the plan paid, or how a claim was processed. Call the hospital when the problem is about the bill itself: charges, codes, a missing insurance claim, financial assistance or a payment plan. If the hospital bill and your Explanation of Benefits (EOB) disagree, start with the hospital and ask them to match the EOB.",
        },
        {
            "q": "How long do I have to appeal a denied insurance claim?",
            "a": "HealthCare.gov says you must file an internal appeal within 180 days (6 months) of getting the denial notice. For care you already received, the insurer must finish the appeal within 60 days. If the insurer still says no, you can ask for an external review within 4 months of the final denial.",
        },
        {
            "q": "Who do I call about a surprise out-of-network bill?",
            "a": "Start with your insurer to confirm the claim was processed under the No Surprises Act, then call the provider that sent the bill. If it is not fixed, call the No Surprises Help Desk at 1-800-985-3059. Federal rules bar an out-of-network provider covered by the law from billing you more than your in-network cost-sharing amount.",
        },
        {
            "q": "Can a hospital bill me if I have Medicaid?",
            "a": "A provider that takes part in Medicaid must accept the Medicaid payment as payment in full, under 42 CFR 447.15. You may still owe any cost-sharing your state Medicaid program allows. If you get a full bill, call the hospital to make sure they have your Medicaid information, then contact your state Medicaid agency or your Medicaid health plan.",
        },
        {
            "q": "What if my bill is in collections but I think it is wrong?",
            "a": "Send the collector a written dispute within the 30-day dispute period shown on its validation notice. The CFPB says the collector must then pause collecting the disputed amount until it responds. Also call the hospital: if it is a nonprofit and you apply for financial assistance within its application period, it must suspend extraordinary collection actions while it decides. You can file a complaint with the CFPB if a collector does not follow the rules.",
        },
        {
            "q": "How long does a hospital have to send my medical and billing records?",
            "a": "Under the HIPAA access rule, a provider must act on your request within 30 days. It can take one extension of up to 30 more days if it tells you in writing why and when it will finish. Your right covers billing records as well as medical records.",
        },
    ],
    "body": f"""
<p class="lead">Call your insurance company when the problem is about coverage: a denial, what the plan paid or how a claim was processed. Call the hospital when the problem is about the bill itself: the charges, the codes, financial assistance or a payment plan. The table below covers 14 common problems, who to call first, who to call next and the rule that backs you up.</p>

<nav class="toc">
    <h2>In this guide</h2>
    <ol>
        <li><a href="#quick-rule">The quick rule: who owns what</a></li>
        <li><a href="#decision-table">The decision table: 14 bill problems</a></li>
        <li><a href="#make-the-call-count">How to make the call count</a></li>
        <li><a href="#escalate">When a call doesn&rsquo;t fix it: where to escalate</a></li>
        <li><a href="#faq">Frequently asked questions</a></li>
        <li><a href="#sources">Sources</a></li>
    </ol>
</nav>

<h2 id="quick-rule">1. The quick rule: who owns what</h2>

<p>Two companies touch every insured hospital bill. Each one controls different parts of it.</p>

<ul>
    <li><strong>Your insurer owns the claim.</strong> It decides what is covered, what it pays and what share is yours. That decision shows up on your <a href="/guides/explanation-of-benefits-eob/">Explanation of Benefits</a> (EOB), the statement the insurer sends after it processes a claim. An EOB is not a bill.</li>
    <li><strong>The hospital owns the bill.</strong> It decides what to charge, which billing codes to use, whether you qualify for financial assistance and whether you can pay over time.</li>
    <li><strong>A collection agency owns nothing on its own.</strong> It collects for the hospital or for whoever bought the debt. You often deal with both the collector and the hospital.</li>
</ul>

<p>A simple test: if the fix means changing what the <em>plan</em> paid, call the insurer. If the fix means changing what the <em>hospital</em> charged or how it filed, call the hospital. When you aren&rsquo;t sure, start with the hospital billing office and ask, &ldquo;Is this something you can fix, or does the insurer need to?&rdquo;</p>

<div class="key-takeaway">
    <h3>Key takeaway</h3>
    <p>Before you call anyone, put the hospital bill and the EOB side by side. If the &ldquo;amount you owe&rdquo; doesn&rsquo;t match, the hospital is usually your first call. To see the charges line by line, <a href="/scan">check your bill free</a> against Medicare rates.</p>
</div>

<h2 id="decision-table">2. The decision table: 14 bill problems</h2>

<p>Find your problem in the left column. &ldquo;Call first&rdquo; is the party that can usually fix it fastest. &ldquo;Then&rdquo; is your next step if the first call doesn&rsquo;t work. The last column names the rule or document you can point to. Deadlines are federal rules as of November 2026; your plan or state may add more protections.</p>

<table>
    <thead>
        <tr>
            <th>Your problem</th>
            <th>Call first</th>
            <th>Then</th>
            <th>Your right / source</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>Claim denied</td>
            <td>Insurer. Ask for the denial reason in writing.</td>
            <td>Hospital: ask if a code, a prior approval or a form was missing, and if they will send a corrected claim. Then file an internal appeal.</td>
            <td>Appeal within 180 days of the denial notice. For care you already got, the insurer has 60 days to decide. External review within 4 months of a final denial (HealthCare.gov).</td>
        </tr>
        <tr>
            <td>Bill shows no insurance payment</td>
            <td>Hospital. Confirm they have your current insurance card and filed a claim.</td>
            <td>Insurer: confirm the claim arrived. Ask the hospital to hold the bill while it processes.</td>
            <td>No EOB for that date usually means no claim was processed. See our <a href="/guides/explanation-of-benefits-eob-guide/">EOB guide</a>.</td>
        </tr>
        <tr>
            <td>Amount owed differs from your EOB</td>
            <td>Hospital. Ask them to bill you the &ldquo;patient responsibility&rdquo; shown on the EOB.</td>
            <td>Insurer, if the hospital says the EOB is wrong. Ask whether a corrected claim is coming.</td>
            <td>Your EOB is the insurer&rsquo;s record of your share. Keep a copy with your notes.</td>
        </tr>
        <tr>
            <td>Out-of-network bill after an ER visit</td>
            <td>Insurer. Ask if the claim was processed under the No Surprises Act at in-network cost sharing.</td>
            <td>The provider that billed you. If not fixed, the No Surprises Help Desk: 1-800-985-3059.</td>
            <td>An out-of-network provider covered by the law must not bill you more than your cost-sharing amount (45 CFR 149.410).</td>
        </tr>
        <tr>
            <td>Charge for something you didn&rsquo;t get</td>
            <td>Hospital. Ask for an <a href="/guides/how-to-get-itemized-hospital-bill/">itemized bill</a> and a review of that line.</td>
            <td>Insurer, if it paid for that line, so the claim can be corrected too.</td>
            <td>Your HIPAA right of access covers billing records, not just medical records (45 CFR 164.501, 164.524).</td>
        </tr>
        <tr>
            <td>Wrong codes or wrong level of care</td>
            <td>Hospital. Ask for a coding review of the specific code.</td>
            <td>Insurer, once the hospital sends a corrected claim, to confirm your new share.</td>
            <td>Request the records the codes came from. See <a href="/guides/upcoding-unbundling-hospital-bills/">upcoding and unbundling</a>.</td>
        </tr>
        <tr>
            <td>You need financial assistance</td>
            <td>Hospital financial counselor or billing office. Ask for the application and policy.</td>
            <td>Apply in writing and keep proof of when you sent it.</td>
            <td>Nonprofit hospitals must accept applications for at least 240 days from the first bill after discharge (IRS, Section 501(r)).</td>
        </tr>
        <tr>
            <td>You want a payment plan</td>
            <td>Hospital billing office.</td>
            <td>Get the monthly amount, any interest and the length in writing before you pay.</td>
            <td>Terms are set by hospital policy. See <a href="/guides/hospital-payment-plans/">hospital payment plans</a>.</td>
        </tr>
        <tr>
            <td>Bill is in collections</td>
            <td>Collector, in writing, within the 30-day dispute period on its notice.</td>
            <td>Hospital: ask about the account status and apply for financial assistance if you may qualify.</td>
            <td>After a written dispute in time, the collector must pause collecting the disputed amount until it responds (CFPB). Complaints go to the CFPB.</td>
        </tr>
        <tr>
            <td>Hospital bill doesn&rsquo;t match your Medicare Summary Notice</td>
            <td>Hospital. Compare to the &ldquo;Maximum You May Be Billed&rdquo; on your MSN.</td>
            <td>1-800-MEDICARE (1-800-633-4227). To appeal, file by the date on the MSN.</td>
            <td>The MSN shows the most the provider may bill you. Appeals go to the contractor listed on the MSN (Medicare.gov).</td>
        </tr>
        <tr>
            <td>Medicaid patient got a full bill</td>
            <td>Hospital. Confirm they have your Medicaid ID and billed Medicaid.</td>
            <td>Your state Medicaid agency or Medicaid health plan.</td>
            <td>Participating providers must accept Medicaid&rsquo;s payment as payment in full, apart from allowed cost sharing (42 CFR 447.15).</td>
        </tr>
        <tr>
            <td>Price far above your estimate</td>
            <td>Hospital. Ask for the itemized bill and how it compares line by line to the estimate.</td>
            <td>Uninsured or self-pay: the federal patient-provider dispute process. Insured: your insurer, to check how the claim was paid.</td>
            <td>Self-pay patients can dispute a bill $400 or more above the good faith estimate, using a bill dated within the last 120 days. Fee: $25 (CMS).</td>
        </tr>
        <tr>
            <td>You need your records</td>
            <td>Hospital medical records department. Ask in writing for medical and billing records.</td>
            <td>The hospital&rsquo;s privacy officer, if the deadline passes.</td>
            <td>The hospital must act within 30 days, with one 30-day extension if it tells you why in writing (45 CFR 164.524).</td>
        </tr>
        <tr>
            <td>Provider bills you the gap after an insurer-provider payment dispute</td>
            <td>Insurer. Ask if the payment dispute is settled and whether it has paid.</td>
            <td>No Surprises Help Desk (1-800-985-3059) or your state insurance department.</td>
            <td>The dispute is between the plan and the provider. Any amount owed is due within 30 days of the decision (45 CFR 149.510). Your share stays at cost sharing (45 CFR 149.410).</td>
        </tr>
    </tbody>
</table>

<p><strong>About that last row.</strong> When an out-of-network provider and an insurer disagree on price under the No Surprises Act, they can use a federal process called independent dispute resolution (IDR). It settles what the plan pays the provider. It does not raise what you owe. If a provider bills you for the difference, don&rsquo;t pay that part. Call the insurer and report the bill to the help desk.</p>

<div class="key-takeaway">
    <h3>Key takeaway</h3>
    <p>Many fixes start with paperwork you are entitled to: the itemized bill, your billing records and the EOB. Ask for them in writing so the clock starts. Our guide to <a href="/guides/how-to-get-itemized-hospital-bill/">getting an itemized hospital bill</a> has the exact wording.</p>
</div>

<h2 id="make-the-call-count">3. How to make the call count</h2>

<p>A call can fix a simple mistake fast. These steps keep a record of it.</p>

<ol>
    <li><strong>Gather three things first.</strong> The bill (account number, date of service), the EOB or MSN for the same date, and your insurance card. Highlight the line you are calling about.</li>
    <li><strong>Say the problem in one sentence.</strong> Example: &ldquo;My EOB says I owe $240 for the March 4 visit, but your bill says $1,120. Can you bill me the EOB amount?&rdquo; One clear ask beats a long story.</li>
    <li><strong>Ask who can fix it.</strong> &ldquo;Is this something you can correct, or does it need to go to the insurer?&rdquo; If they send you elsewhere, ask what to tell the other side. Our <a href="/guides/medical-bill-dispute-phone-scripts/">phone scripts</a> have more wording.</li>
    <li><strong>Ask for a hold.</strong> Ask the hospital to pause billing on the account while the issue is reviewed, and to note that in your file.</li>
    <li><strong>Write it all down.</strong> Date, time, the person&rsquo;s name, a reference number and what they promised to do by when.</li>
    <li><strong>Follow up in writing.</strong> Send a short letter or portal message that repeats what was agreed. A call leaves no record you control. A letter does. Our <a href="/guides/medical-bill-dispute-letter/">dispute letter guide</a> has a template.</li>
    <li><strong>Watch the deadlines.</strong> Put the appeal date, the 30-day collector dispute window or the financial assistance deadline on your calendar the same day.</li>
</ol>

<h2 id="escalate">4. When a call doesn&rsquo;t fix it: where to escalate</h2>

<p>If the hospital, insurer or collector doesn&rsquo;t respond, these offices can take a complaint. Each one covers a different part of the problem.</p>

<table>
    <thead>
        <tr>
            <th>Office</th>
            <th>Contact</th>
            <th>Best for</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>Your state insurance department</td>
            <td>Find yours through the NAIC directory</td>
            <td>Problems with an insurance company: slow claims, denials, appeal handling</td>
        </tr>
        <tr>
            <td>No Surprises Help Desk (CMS)</td>
            <td>1-800-985-3059</td>
            <td>Surprise out-of-network bills, bills above a good faith estimate</td>
        </tr>
        <tr>
            <td>Medicare</td>
            <td>1-800-MEDICARE (1-800-633-4227), TTY 1-877-486-2048, 24 hours a day</td>
            <td>Medicare claims, MSN questions, help with appeals</td>
        </tr>
        <tr>
            <td>Consumer Financial Protection Bureau</td>
            <td>consumerfinance.gov/complaint</td>
            <td>Debt collectors, including collectors of medical debt</td>
        </tr>
        <tr>
            <td>State attorney general or consumer protection office</td>
            <td>Find yours through USA.gov</td>
            <td>Complaints against businesses, including billing practices</td>
        </tr>
    </tbody>
</table>

<div class="key-takeaway">
    <h3>Key takeaway</h3>
    <p>The call starts the fix. The letter proves it happened. If you are disputing charges with the hospital, <a href="/scan">check your bill free</a> first so your letter names the exact lines and codes you are questioning.</p>
</div>

<p>When you file, attach copies (not originals) of the bill, the EOB or MSN and your call notes. Your notes from step 5 above become your timeline.</p>

<p>If you are taken to court over a medical bill, or your wages are being garnished, a phone call is no longer enough. Consider talking to a consumer attorney or your local legal aid office. Our guide to <a href="/guides/medical-debt-collections-rights/">your rights in medical debt collections</a> explains the basics.</p>

<h2 id="faq">Frequently asked questions</h2>

<div class="faq-section">
    <div class="faq-item">
        <h3>Should I call the hospital or my insurance company about a bill?</h3>
        <p>Call the insurer when the problem is about coverage: a denied claim, how much the plan paid, or how a claim was processed. Call the hospital when the problem is about the bill itself: charges, codes, a missing insurance claim, financial assistance or a payment plan. If the hospital bill and your Explanation of Benefits (EOB) disagree, start with the hospital and ask them to match the EOB.</p>
    </div>
    <div class="faq-item">
        <h3>How long do I have to appeal a denied insurance claim?</h3>
        <p>HealthCare.gov says you must file an internal appeal within 180 days (6 months) of getting the denial notice. For care you already received, the insurer must finish the appeal within 60 days. If the insurer still says no, you can ask for an external review within 4 months of the final denial.</p>
    </div>
    <div class="faq-item">
        <h3>Who do I call about a surprise out-of-network bill?</h3>
        <p>Start with your insurer to confirm the claim was processed under the No Surprises Act, then call the provider that sent the bill. If it is not fixed, call the No Surprises Help Desk at 1-800-985-3059. Federal rules bar an out-of-network provider covered by the law from billing you more than your in-network cost-sharing amount.</p>
    </div>
    <div class="faq-item">
        <h3>Can a hospital bill me if I have Medicaid?</h3>
        <p>A provider that takes part in Medicaid must accept the Medicaid payment as payment in full, under 42 CFR 447.15. You may still owe any cost-sharing your state Medicaid program allows. If you get a full bill, call the hospital to make sure they have your Medicaid information, then contact your state Medicaid agency or your Medicaid health plan.</p>
    </div>
    <div class="faq-item">
        <h3>What if my bill is in collections but I think it is wrong?</h3>
        <p>Send the collector a written dispute within the 30-day dispute period shown on its validation notice. The CFPB says the collector must then pause collecting the disputed amount until it responds. Also call the hospital: if it is a nonprofit and you apply for financial assistance within its application period, it must suspend extraordinary collection actions while it decides. You can file a complaint with the CFPB if a collector does not follow the rules.</p>
    </div>
    <div class="faq-item">
        <h3>How long does a hospital have to send my medical and billing records?</h3>
        <p>Under the HIPAA access rule, a provider must act on your request within 30 days. It can take one extension of up to 30 more days if it tells you in writing why and when it will finish. Your right covers billing records as well as medical records.</p>
    </div>
</div>

<h2 id="sources">Sources</h2>

<ul class="sources-list">
    <li><a href="https://www.healthcare.gov/appeal-insurance-company-decision/internal-appeals/" target="_blank" rel="noopener">HealthCare.gov &mdash; Internal appeals</a></li>
    <li><a href="https://www.healthcare.gov/appeal-insurance-company-decision/external-review/" target="_blank" rel="noopener">HealthCare.gov &mdash; External review</a></li>
    <li><a href="https://www.cms.gov/medical-bill-rights" target="_blank" rel="noopener">CMS &mdash; Medical bill rights and the No Surprises Help Desk</a></li>
    <li><a href="https://www.cms.gov/medical-bill-rights/help/dispute-a-bill" target="_blank" rel="noopener">CMS &mdash; Dispute a bill that is $400 or more above your good faith estimate</a></li>
    <li><a href="https://www.law.cornell.edu/cfr/text/45/149.410" target="_blank" rel="noopener">45 CFR 149.410 &mdash; Balance billing in cases of emergency services</a></li>
    <li><a href="https://www.law.cornell.edu/cfr/text/45/149.510" target="_blank" rel="noopener">45 CFR 149.510 &mdash; Independent dispute resolution process</a></li>
    <li><a href="https://www.law.cornell.edu/cfr/text/45/164.524" target="_blank" rel="noopener">45 CFR 164.524 &mdash; Access of individuals to protected health information</a></li>
    <li><a href="https://www.law.cornell.edu/cfr/text/45/164.501" target="_blank" rel="noopener">45 CFR 164.501 &mdash; Definition of designated record set</a></li>
    <li><a href="https://www.law.cornell.edu/cfr/text/42/447.15" target="_blank" rel="noopener">42 CFR 447.15 &mdash; Acceptance of state payment as payment in full</a></li>
    <li><a href="https://www.irs.gov/charities-non-profits/billing-and-collections-section-501r6" target="_blank" rel="noopener">IRS &mdash; Billing and collections, Section 501(r)(6)</a></li>
    <li><a href="https://www.consumerfinance.gov/ask-cfpb/what-information-does-a-debt-collector-have-to-give-me-about-the-debt-en-331/" target="_blank" rel="noopener">CFPB &mdash; What information does a debt collector have to give me about the debt?</a></li>
    <li><a href="https://www.medicare.gov/providers-services/claims-appeals-complaints/appeals/original-medicare" target="_blank" rel="noopener">Medicare.gov &mdash; Appeals in Original Medicare</a></li>
    <li><a href="https://www.medicare.gov/publications/summarynoticeb.pdf" target="_blank" rel="noopener">Medicare.gov &mdash; What is in your Medicare Summary Notice (Part B)</a></li>
    <li><a href="https://www.medicare.gov/talk-to-someone" target="_blank" rel="noopener">Medicare.gov &mdash; Talk to someone (1-800-MEDICARE)</a></li>
    <li><a href="https://content.naic.org/state-insurance-departments" target="_blank" rel="noopener">NAIC &mdash; State insurance departments</a></li>
    <li><a href="https://www.usa.gov/state-consumer" target="_blank" rel="noopener">USA.gov &mdash; State consumer protection offices</a></li>
</ul>
""",
})
