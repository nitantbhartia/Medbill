"""Guide: Medicare Summary Notice vs Your Hospital Bill."""

from guides import register

register("medicare-summary-notice-vs-hospital-bill", {
    "title": "Medicare Summary Notice vs Hospital Bill: How to Match",
    "meta_description": "Your Medicare Summary Notice is not a bill. Learn how to match it to your hospital bill, what you can owe in 2026, and how to appeal within 120 days.",
    "published": "2026-11-20",
    "reviewed_on": "2026-11-20",
    "author": "BillKarma Team",
    "category": "Understanding Your Bill",
    "faqs": [
        {
            "q": "Is a Medicare Summary Notice a bill?",
            "a": "No. Medicare.gov says the Medicare Summary Notice (MSN) is not a bill. It is a notice for people with Original Medicare that lists the Part A and Part B services billed to Medicare, what Medicare paid, and the most the provider may bill you. The bill itself comes from the hospital or doctor.",
        },
        {
            "q": "How often do I get a Medicare Summary Notice?",
            "a": "As of November 2026, Medicare.gov says you get an MSN every 6 months if you got any services or supplies during that period. If you sign up for electronic MSNs, you get an email with a link for any month you have a processed claim. Claims usually appear in your secure Medicare.gov account within 24 hours after Medicare processes them.",
        },
        {
            "q": "What should I do if my hospital bill is higher than the MSN says I owe?",
            "a": "The MSN column called Maximum You May Be Billed is the total the provider is able to bill you for that claim. If the hospital bill asks for more, call the billing office, give them the MSN claim date and amounts, and ask them to correct the bill or explain the difference in writing. Keep the bill on hold while you ask.",
        },
        {
            "q": "What are the Medicare deductibles in 2026?",
            "a": "According to CMS, the 2026 Part A inpatient hospital deductible is $1,736 per benefit period, and the 2026 Part B annual deductible is $283. After the Part B deductible, you usually pay 20% of the Medicare-approved amount for doctor services, plus a hospital copayment for each outpatient service.",
        },
        {
            "q": "Can a hospital bill me if I have QMB?",
            "a": "Generally, no. If you are in the Qualified Medicare Beneficiary (QMB) program, Medicare.gov says Medicare providers are not allowed to bill you for services and items Medicare covers. CMS says this applies even if the provider does not take Medicaid. You may still get a bill for a small Medicaid copayment.",
        },
        {
            "q": "How long do I have to appeal something on my MSN?",
            "a": "You have 120 days to appeal, and your MSN lists the exact date your appeal must be received. This first-level appeal is called a redetermination and goes to the Medicare Administrative Contractor listed on the MSN. Medicare.gov says the contractor generally decides within 60 days.",
        },
    ],
    "body": f"""
<p class="lead">Your Medicare Summary Notice (MSN) is not a bill. It is Medicare&rsquo;s record of what the hospital billed, what Medicare paid, and the most the hospital is allowed to bill you. When your hospital bill asks for more than the MSN&rsquo;s &ldquo;Maximum You May Be Billed&rdquo; amount, or charges you for something the MSN shows differently, you have the right to ask questions before you pay. This guide shows you how to line the two documents up, what you can owe in 2026, and how to get errors fixed.</p>

<nav class="toc">
    <h2>In this guide</h2>
    <ol>
        <li><a href="#what-is-msn">What the Medicare Summary Notice is</a></li>
        <li><a href="#reading-msn">The MSN columns that matter</a></li>
        <li><a href="#matching">How to match your hospital bill to the MSN</a></li>
        <li><a href="#what-you-owe">What you can owe in 2026</a></li>
        <li><a href="#red-flags">Red flags worth questioning</a></li>
        <li><a href="#secondary">If you have Medigap, Medicaid, or QMB</a></li>
        <li><a href="#what-to-do">What to do, step by step</a></li>
        <li><a href="#appeal">How to appeal a decision on your MSN</a></li>
        <li><a href="#faq">Frequently asked questions</a></li>
        <li><a href="#sources">Sources</a></li>
    </ol>
</nav>

<h2 id="what-is-msn">1. What the Medicare Summary Notice is</h2>

<p>The MSN is a notice for people with Original Medicare (Medicare Part A and Part B, run by the federal government). Medicare.gov says plainly: it&rsquo;s not a bill. It lists the services that providers billed to Medicare for you during a period of time.</p>

<p>There are two main versions you might see after a hospital visit:</p>
<ul>
    <li><strong>Part A MSN</strong> (hospital insurance): inpatient hospital stays, skilled nursing facility care, hospice, and home health care.</li>
    <li><strong>Part B MSN</strong> (medical insurance): doctor visits, hospital outpatient care, preventive services, and other medical care. If you were in the hospital under <em>observation</em> (an outpatient status), those services usually show up here.</li>
</ul>

<p><strong>How often it comes.</strong> As of November 2026, Medicare.gov says you get a paper MSN every 6 months if you got any services or supplies in that period. You won&rsquo;t get one if you had no services. You can switch to electronic MSNs, which arrive by email for any month you have a processed claim. You can also see claims in your secure Medicare.gov account, usually within 24 hours after Medicare processes them. That is often faster than waiting for the mail.</p>

<p><strong>If you have Medicare Advantage</strong> (a private Medicare plan), you won&rsquo;t get an MSN for those services. Your plan mails an Explanation of Benefits (EOB) instead. Our <a href="/guides/explanation-of-benefits-eob/">EOB guide</a> walks through that document.</p>

<h2 id="reading-msn">2. The MSN columns that matter</h2>

<p>The claims page of the MSN (page 3 in Medicare&rsquo;s sample notices) lists each visit and the services billed. These are the parts to focus on when you compare it to a hospital bill:</p>

<table>
    <thead>
        <tr>
            <th>MSN item</th>
            <th>What it tells you</th>
            <th>How to use it</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>Your deductible info (page 1)</td>
            <td>How much of your yearly Part B deductible, or your Part A deductible, you have met</td>
            <td>Check whether the hospital is charging you a deductible you already paid on an earlier claim</td>
        </tr>
        <tr>
            <td>Date of service and facility</td>
            <td>When and where the care happened</td>
            <td>Match each date to a date on the hospital bill</td>
        </tr>
        <tr>
            <td>Service approved?</td>
            <td>Whether Medicare approved or denied each claim or service</td>
            <td>Denied items need a closer look (see red flags below)</td>
        </tr>
        <tr>
            <td>Amount Medicare paid</td>
            <td>What Medicare paid the provider</td>
            <td>The hospital bill should show this payment as a credit</td>
        </tr>
        <tr>
            <td>Maximum You May Be Billed</td>
            <td>Medicare calls this the total amount the provider or facility is able to bill you</td>
            <td>Compare it to the balance on your hospital bill</td>
        </tr>
        <tr>
            <td>Notes</td>
            <td>Lettered notes that explain denials and adjustments</td>
            <td>Read these before you call billing</td>
        </tr>
    </tbody>
</table>

<p>The &ldquo;Maximum You May Be Billed&rdquo; amount is the number most people need. If you have other coverage, like a Medigap policy or Medicaid, it may pay some or all of that amount, so your own bill could be lower still.</p>

<h2 id="matching">3. How to match your hospital bill to the MSN</h2>

<p>Hospital bills and MSNs are organized differently, so they rarely look alike at first. A hospital summary bill may show one total. The MSN may split the same stay into several claims. Here is how to line them up:</p>

<ul>
    <li><strong>Ask for an itemized bill.</strong> An itemized bill lists each charge with its date and billing code. It is much easier to match than a one-line summary.</li>
    <li><strong>Match by date first.</strong> Find each date of service on the bill, then find the same date on the MSN. Hospital and doctor charges for the same day often appear as separate claims, sometimes on different MSNs.</li>
    <li><strong>Check the total charges.</strong> The hospital&rsquo;s full charge is usually much higher than what Medicare approves. That is normal. What matters is the amount the hospital asks <em>you</em> to pay.</li>
    <li><strong>Look for the Medicare payment.</strong> Your bill should show Medicare&rsquo;s payment and any contractual adjustment (the amount the hospital writes off under its Medicare agreement).</li>
    <li><strong>Watch the timing.</strong> If a claim is not on the MSN yet, Medicare may not have processed it. Check your Medicare.gov account before paying a bill for that date.</li>
</ul>

<div class="key-takeaway"><h3>Key takeaway</h3><p>The MSN&rsquo;s &ldquo;Maximum You May Be Billed&rdquo; column is your benchmark. If the hospital bill asks for more than that amount for the same dates, ask the billing office to explain it before you pay. You can also <a href="/scan">check your hospital bill free</a> to spot charges worth asking about.</p></div>

<h2 id="what-you-owe">4. What you can owe in 2026</h2>

<p>Original Medicare has cost sharing, so a bill after a hospital visit is not automatically a mistake. CMS published these 2026 amounts:</p>

<table>
    <thead>
        <tr>
            <th>Cost</th>
            <th>2026 amount</th>
            <th>When it applies</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>Part A inpatient hospital deductible</td>
            <td>$1,736</td>
            <td>Covers your share of the first 60 days of a covered inpatient stay in a benefit period</td>
        </tr>
        <tr>
            <td>Part A coinsurance, days 61&ndash;90</td>
            <td>$434 per day</td>
            <td>Long inpatient stays in the same benefit period</td>
        </tr>
        <tr>
            <td>Part A lifetime reserve days (after day 90)</td>
            <td>$868 per day</td>
            <td>Only if you use your lifetime reserve days</td>
        </tr>
        <tr>
            <td>Part B deductible</td>
            <td>$283 per year</td>
            <td>Before Part B pays for most outpatient and doctor services</td>
        </tr>
        <tr>
            <td>Part B coinsurance</td>
            <td>Usually 20% of the Medicare-approved amount</td>
            <td>Doctor and other provider services after the deductible</td>
        </tr>
        <tr>
            <td>Hospital outpatient copayment</td>
            <td>Varies by service</td>
            <td>Each service in a hospital outpatient department</td>
        </tr>
    </tbody>
</table>

<p>For hospital outpatient care, Medicare.gov says you usually pay the hospital a copayment for each service, and in most cases that copayment can&rsquo;t be more than the Part A deductible for each service. Critical access hospitals (small rural hospitals) are an exception.</p>

<p><strong>Example:</strong> You have not paid anything toward your 2026 Part B deductible. A doctor&rsquo;s service has a Medicare-approved amount of $300. You pay the first $283 (your deductible). On the remaining $17, you pay 20%, which is $3.40. Your share is $286.40, and Medicare pays $13.60. Your MSN would show $286.40 as the most you may be billed for that service. (This is a simplified illustration; real claims often include several services.)</p>

<h2 id="red-flags">5. Red flags worth questioning</h2>

<p>Billing offices make mistakes, and a mismatch is often a timing or posting problem. These are the situations most worth a phone call:</p>

<p><strong>The bill is higher than &ldquo;Maximum You May Be Billed.&rdquo;</strong> Medicare describes that column as the total the provider is able to bill you. A higher balance for the same dates may mean the hospital has not posted Medicare&rsquo;s payment or adjustment yet, or has billed you for something it should not have.</p>

<p><strong>You are billed for a denied service and didn&rsquo;t sign an ABN.</strong> An Advance Beneficiary Notice of Noncoverage (ABN, form CMS-R-131) is a one-page form a provider gives you <em>before</em> a service when it expects Medicare may not pay, for example because the service may not be considered medically necessary or is beyond a frequency limit. CMS&rsquo;s guidance says the provider may collect from you after you get and sign a properly issued ABN. It also says a notice can&rsquo;t be backdated to shift costs for care already given. If Medicare denied a service as not medically necessary and you did not get an ABN, ask the hospital to show you the signed form.</p>

<p><strong>You were billed for drugs during an observation stay.</strong> This one surprises many people, and it is often allowed. In observation you are an outpatient, and Medicare.gov says Part B generally doesn&rsquo;t cover prescription and over-the-counter drugs you get in an outpatient setting. These are often called &ldquo;self-administered drugs&rdquo; (pills you would normally take on your own). Because Medicare doesn&rsquo;t cover them, CMS does not require an ABN for them. A Part D drug plan may cover some of these drugs, but you may need to pay first and file a claim with your plan. Our guide to <a href="/guides/medicare-observation-status-billing/">observation status billing</a> covers this in more detail.</p>

<p><strong>You were charged a deductible twice.</strong> Compare the deductible info on page 1 of each MSN. If your MSN shows the Part B deductible already met, a second deductible charge from another claim is worth asking about.</p>

<p><strong>The bill lists dates or services that aren&rsquo;t on any MSN.</strong> Medicare.gov suggests comparing your receipts and bills to your MSN to be sure you got every service listed. The reverse matters too: a charge for a date Medicare hasn&rsquo;t seen deserves a question.</p>

<div class="key-takeaway"><h3>Key takeaway</h3><p>Not every surprise charge is an error. Self-administered drugs during observation are often billable, while a balance above &ldquo;Maximum You May Be Billed&rdquo; or a denied service with no signed ABN is worth disputing. Our guide on <a href="/guides/how-to-dispute-medicare-bill/">how to dispute a Medicare bill</a> covers the next steps.</p></div>

<h2 id="secondary">6. If you have Medigap, Medicaid, or QMB</h2>

<p><strong>Medigap.</strong> A Medicare Supplement (Medigap) policy helps pay your share of costs in Original Medicare, like copayments, coinsurance, and deductibles. If you have one, the hospital should bill it before billing you. If your bill shows the full &ldquo;Maximum You May Be Billed&rdquo; amount, ask whether the hospital sent the claim to your Medigap insurer. See our <a href="/guides/medigap-medicare-supplement/">Medigap guide</a> for how these plans work.</p>

<p><strong>Medicaid and QMB.</strong> The Qualified Medicare Beneficiary (QMB) program is a Medicare Savings Program run by your state. It helps pay Medicare premiums, deductibles, coinsurance, and copayments. Medicare.gov says that if you are in QMB, Medicare providers aren&rsquo;t allowed to bill you for services and items Medicare covers. You may still owe a small Medicaid copayment. CMS says this billing rule applies to all Medicare providers, including those that don&rsquo;t accept Medicaid.</p>

<p>Your MSN can help here. Medicare.gov says MSNs show that you are in the QMB program, and suggests showing your MSN along with your Medicare and Medicaid (or QMB) card when you get care. If a hospital bills you anyway, call 1-800-MEDICARE, and read our <a href="/guides/dual-eligible-medicare-medicaid-billing/">dual eligible billing guide</a>.</p>

<h2 id="what-to-do">7. What to do, step by step</h2>

<ol>
    <li><strong>Gather your documents.</strong> Get the hospital bill, an itemized bill, and every MSN that covers your dates of care. If you don&rsquo;t have the MSN yet, log in to your Medicare.gov account.</li>
    <li><strong>Match each date.</strong> Write the MSN&rsquo;s &ldquo;Maximum You May Be Billed&rdquo; amount next to each matching date on the hospital bill.</li>
    <li><strong>Check secondary coverage.</strong> If you have Medigap, Medicaid, QMB, or retiree coverage, confirm the hospital billed it.</li>
    <li><strong>Call the billing office.</strong> Give the dates of service, the MSN amounts, and the specific lines that don&rsquo;t match. Ask them to correct the account or explain the difference. Write down the date, the person&rsquo;s name, and what they said.</li>
    <li><strong>Ask for a hold.</strong> Ask the hospital to pause collection activity while it reviews the account.</li>
    <li><strong>Follow up in writing.</strong> If the phone call doesn&rsquo;t resolve it, send a short letter that lists the dates, the MSN amounts, and what you want corrected. Keep copies.</li>
    <li><strong>Appeal to Medicare if the problem is Medicare&rsquo;s decision.</strong> If the hospital&rsquo;s bill matches the MSN, but you think Medicare wrongly denied a service, the fix is an appeal, covered next. Medicare.gov also suggests asking the provider whether it can resubmit a denied claim with corrected information.</li>
</ol>

<div class="key-takeaway"><h3>Key takeaway</h3><p>Start with the hospital, not Medicare: most mismatches are fixed by the billing office once you show them the MSN amounts. If that doesn&rsquo;t work, put it in writing. Before you call, you can <a href="/scan">scan your bill free</a> to find the lines to ask about.</p></div>

<h2 id="appeal">8. How to appeal a decision on your MSN</h2>

<p>If you disagree with a Medicare decision, such as a denied service, you can file a first-level appeal called a <strong>redetermination</strong>. It goes to the Medicare Administrative Contractor (the company that processes Medicare claims in your area). Its address is on the last page of your MSN.</p>

<ul>
    <li><strong>Deadline:</strong> You have 120 days to appeal. Your MSN shows the exact date your appeal must be received. If you miss it, you may still be able to file if you show good cause.</li>
    <li><strong>How to file:</strong> Follow the steps on the last page of the MSN. You can circle the items you disagree with, explain why, and mail it. You can also use the Redetermination Request Form (CMS-20027) or send a written request.</li>
    <li><strong>What to include:</strong> Your name, address, and Medicare number; the items and dates you are appealing; why you think they should be covered; and helpful records, like a note from your doctor.</li>
    <li><strong>Timing:</strong> Medicare.gov says the contractor generally decides within 60 days after it gets your appeal.</li>
</ul>

<p>Appeals have more levels after a redetermination. If your case involves a large amount or a complicated question, consider talking with your State Health Insurance Assistance Program (SHIP), a consumer attorney, or legal aid.</p>

<h2 id="faq">Frequently asked questions</h2>

<div class="faq-section">
    <div class="faq-item">
        <h3>Is a Medicare Summary Notice a bill?</h3>
        <p>No. Medicare.gov says the Medicare Summary Notice (MSN) is not a bill. It is a notice for people with Original Medicare that lists the Part A and Part B services billed to Medicare, what Medicare paid, and the most the provider may bill you. The bill itself comes from the hospital or doctor.</p>
    </div>
    <div class="faq-item">
        <h3>How often do I get a Medicare Summary Notice?</h3>
        <p>As of November 2026, Medicare.gov says you get an MSN every 6 months if you got any services or supplies during that period. If you sign up for electronic MSNs, you get an email with a link for any month you have a processed claim. Claims usually appear in your secure Medicare.gov account within 24 hours after Medicare processes them.</p>
    </div>
    <div class="faq-item">
        <h3>What should I do if my hospital bill is higher than the MSN says I owe?</h3>
        <p>The MSN column called Maximum You May Be Billed is the total the provider is able to bill you for that claim. If the hospital bill asks for more, call the billing office, give them the MSN claim date and amounts, and ask them to correct the bill or explain the difference in writing. Keep the bill on hold while you ask.</p>
    </div>
    <div class="faq-item">
        <h3>What are the Medicare deductibles in 2026?</h3>
        <p>According to CMS, the 2026 Part A inpatient hospital deductible is $1,736 per benefit period, and the 2026 Part B annual deductible is $283. After the Part B deductible, you usually pay 20% of the Medicare-approved amount for doctor services, plus a hospital copayment for each outpatient service.</p>
    </div>
    <div class="faq-item">
        <h3>Can a hospital bill me if I have QMB?</h3>
        <p>Generally, no. If you are in the Qualified Medicare Beneficiary (QMB) program, Medicare.gov says Medicare providers are not allowed to bill you for services and items Medicare covers. CMS says this applies even if the provider does not take Medicaid. You may still get a bill for a small Medicaid copayment.</p>
    </div>
    <div class="faq-item">
        <h3>How long do I have to appeal something on my MSN?</h3>
        <p>You have 120 days to appeal, and your MSN lists the exact date your appeal must be received. This first-level appeal is called a redetermination and goes to the Medicare Administrative Contractor listed on the MSN. Medicare.gov says the contractor generally decides within 60 days.</p>
    </div>
</div>

<h2 id="sources">Sources</h2>

<ul class="sources-list">
    <li><a href="https://www.medicare.gov/basics/forms-publications-mailings/mailings/costs-and-coverage/medicare-summary-notice" target="_blank" rel="noopener">Medicare.gov &mdash; Medicare Summary Notice (MSN)</a></li>
    <li><a href="https://www.medicare.gov/publications/sample-part-a-medicare-summary-notice-d10.pdf" target="_blank" rel="noopener">Medicare.gov &mdash; Sample Part A Medicare Summary Notice</a></li>
    <li><a href="https://www.medicare.gov/publications/sample-part-b-medicare-summary-notice-d1.pdf" target="_blank" rel="noopener">Medicare.gov &mdash; Sample Part B Medicare Summary Notice</a></li>
    <li><a href="https://www.medicare.gov/providers-services/claims-appeals-complaints/claims/check-status" target="_blank" rel="noopener">Medicare.gov &mdash; Checking the status of a claim</a></li>
    <li><a href="https://www.cms.gov/newsroom/fact-sheets/2026-medicare-parts-b-premiums-deductibles" target="_blank" rel="noopener">CMS &mdash; 2026 Medicare Parts A &amp; B Premiums and Deductibles</a></li>
    <li><a href="https://www.medicare.gov/coverage/outpatient-hospital-services" target="_blank" rel="noopener">Medicare.gov &mdash; Outpatient hospital services</a></li>
    <li><a href="https://www.medicare.gov/coverage/prescription-drugs-outpatient" target="_blank" rel="noopener">Medicare.gov &mdash; Prescription drugs (outpatient)</a></li>
    <li><a href="https://www.cms.gov/medicare/forms-notices/beneficiary-notices-initiative/ffs-abn" target="_blank" rel="noopener">CMS &mdash; FFS Advance Beneficiary Notice of Noncoverage (ABN)</a></li>
    <li><a href="https://www.cms.gov/files/document/mln006266-medicare-advance-written-notices-non-coverage.pdf" target="_blank" rel="noopener">CMS &mdash; Medicare Advance Written Notices of Non-coverage (MLN006266)</a></li>
    <li><a href="https://www.medicare.gov/basics/costs/help/medicare-savings-programs" target="_blank" rel="noopener">Medicare.gov &mdash; Medicare Savings Programs</a></li>
    <li><a href="https://www.cms.gov/files/document/mln7936176-prohibition-billing-qualified-medicare-beneficiaries.pdf" target="_blank" rel="noopener">CMS &mdash; Prohibition on Billing Qualified Medicare Beneficiaries (MLN7936176)</a></li>
    <li><a href="https://www.medicare.gov/health-drug-plans/medigap" target="_blank" rel="noopener">Medicare.gov &mdash; What&rsquo;s Medicare Supplement Insurance (Medigap)?</a></li>
    <li><a href="https://www.medicare.gov/providers-services/claims-appeals-complaints/appeals/original-medicare" target="_blank" rel="noopener">Medicare.gov &mdash; Appeals in Original Medicare</a></li>
</ul>
""",
})
