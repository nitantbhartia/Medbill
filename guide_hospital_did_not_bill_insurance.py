"""Guide: Hospital Didn't Bill Your Insurance? What to Do First."""

from guides import register

register("hospital-did-not-bill-insurance", {
    "title": "Hospital Didn’t Bill Your Insurance? What to Do First",
    "meta_description": "If your hospital bill shows self-pay or the full charge, the claim may never have reached your insurer. How to get it billed, and who pays if it’s late.",
    "published": "2026-11-20",
    "reviewed_on": "2026-11-20",
    "author": "BillKarma Team",
    "category": "Taking Action",
    "faqs": [
        {
            "q": "How do I know if the hospital billed my insurance?",
            "a": "Look for an explanation of benefits (EOB) from your insurer for that date, and for an insurance payment or adjustment line on the bill. If there is no EOB and the balance equals the full charges, the claim was likely never processed. Call your insurer to check."
        },
        {
            "q": "Can the hospital still bill my insurance after a few months?",
            "a": "Often, yes, if the filing deadline has not passed. Original Medicare allows 12 months from the date of service, and Medicaid agencies must require claims within 12 months. Private plan deadlines are set by contract and state law. Ask the hospital to submit the claim now and confirm the deadline with your insurer."
        },
        {
            "q": "Do I have to pay if the hospital missed the timely filing deadline?",
            "a": "It depends on your coverage. Under Medicare rules, a provider responsible for late filing may not charge you except for the deductible and coinsurance you would have owed. Medicaid providers must accept Medicaid payment as payment in full, apart from allowed cost sharing. For private plans, in-network contracts and some state laws limit billing you for amounts the plan owes. Ask your insurer or state insurance department."
        },
        {
            "q": "I was uninsured when I went to the hospital but qualify for Medicaid now. Can Medicaid cover it?",
            "a": "Possibly. Federal rules require Medicaid to cover up to three months before the month you apply, if you received covered services and would have qualified then. For applications made on or after January 1, 2027, that window shrinks to one month for adults in the Medicaid expansion group and two months for others. Apply as soon as you can and tell the hospital you applied."
        },
        {
            "q": "Can the hospital send my bill to collections while the insurance claim is sorted out?",
            "a": "Ask the billing office in writing to put the account on hold while the claim is processed. Nonprofit hospitals must also follow IRS rules that generally require them to wait at least 120 days after the first post-discharge bill before extraordinary collection actions such as credit reporting or selling the debt."
        },
    ],
    "body": f"""
<p class="lead">If your hospital bill says &ldquo;self-pay,&rdquo; &ldquo;insurance not on file,&rdquo; or shows the full charge with no insurance payment, the hospital most likely never sent a claim to your insurer, or sent it with the wrong details. The fix is usually simple: give the hospital your insurance information in writing, ask it to submit or resubmit the claim, and ask it to hold your account until your insurer responds. If the hospital missed the filing deadline, the rules on whether you have to pay depend on your coverage, and they often favor you.</p>

<nav class="toc">
    <h2>In this guide</h2>
    <ol>
        <li><a href="#signs">How to tell your insurance wasn&rsquo;t billed</a></li>
        <li><a href="#first-steps">What to do first, step by step</a></li>
        <li><a href="#timely-filing">Timely filing limits</a></li>
        <li><a href="#who-pays">Who pays if the hospital filed too late</a></li>
        <li><a href="#hold">Ask the hospital to hold your account</a></li>
        <li><a href="#medicaid-retro">Uninsured then, eligible for Medicaid now</a></li>
        <li><a href="#script">Phone and letter script</a></li>
        <li><a href="#faq">Frequently asked questions</a></li>
        <li><a href="#sources">Sources</a></li>
    </ol>
</nav>

<h2 id="signs">1. How to tell your insurance wasn&rsquo;t billed</h2>

<p>When a hospital bills your insurance, your insurer sends you an <strong>explanation of benefits</strong> (EOB): a statement, not a bill, showing what was charged, what the plan paid, and what you may owe. The hospital bill that follows usually shows an insurance payment and an &ldquo;adjustment&rdquo; (the discount your plan&rsquo;s contract takes off the full price).</p>

<p>If those pieces are missing, the claim probably never made it through. Compare what you have:</p>

<table>
    <thead>
        <tr>
            <th>What you see</th>
            <th>What it usually means</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>No EOB from your insurer for that date of service</td>
            <td>The insurer has not processed a claim, or it was sent under the wrong member ID</td>
        </tr>
        <tr>
            <td>Bill says &ldquo;self-pay,&rdquo; &ldquo;private pay,&rdquo; or &ldquo;insurance not on file&rdquo;</td>
            <td>The hospital has no insurance on your account</td>
        </tr>
        <tr>
            <td>No insurance payment line and no insurance adjustment line</td>
            <td>No claim was paid or adjusted</td>
        </tr>
        <tr>
            <td>Your balance equals the total charges</td>
            <td>You are being billed full list price, as if uninsured</td>
        </tr>
        <tr>
            <td>A denial on your EOB with a reason like &ldquo;timely filing&rdquo;</td>
            <td>The claim reached the insurer after the plan&rsquo;s deadline</td>
        </tr>
    </tbody>
</table>

<p><strong>Example:</strong> A bill lists total charges of $4,200, insurance payments of $0.00, adjustments of $0.00, and a patient balance of $4,200. You have no EOB for that date. That pattern points to a claim that was never processed, not to a bill you owe in full.</p>

<p>Common causes include a mistyped member ID, a new plan at the start of the year, or the wrong plan listed first when you have two (see <a href="/guides/coordination-of-benefits-dual-insurance/">coordination of benefits</a>).</p>

<div class="key-takeaway"><h3>Key takeaway</h3><p>No EOB plus a full-charge balance usually means a missing claim, not a final bill. Learn to read the EOB with our <a href="/guides/explanation-of-benefits-eob/">explanation of benefits guide</a>, and once the claim is processed, <a href="/scan">check your bill free</a> for other errors.</p></div>

<h2 id="first-steps">2. What to do first, step by step</h2>

<ol>
    <li><strong>Call your insurer first.</strong> Use the number on your card. Ask: &ldquo;Do you have a claim from this hospital for this date of service?&rdquo; Write down the date, the rep&rsquo;s name, and a reference number. Also ask what the plan&rsquo;s filing deadline is for this hospital.</li>
    <li><strong>Confirm your coverage dates.</strong> Make sure the plan was active on the date of service. If it was not, skip to <a href="#medicaid-retro">section 6</a>.</li>
    <li><strong>Send the hospital your insurance information in writing.</strong> Include a copy of the front and back of your card, your member ID, group number, and the policyholder&rsquo;s name and date of birth. Email, the patient portal, or a letter all work. Keep a copy.</li>
    <li><strong>Ask the hospital to submit or resubmit the claim.</strong> Put it in writing and ask for the date it was sent.</li>
    <li><strong>Ask for an account hold.</strong> Request that the account stay out of collections while the claim is processed (see <a href="#hold">section 5</a>).</li>
    <li><strong>Watch for the EOB.</strong> If none arrives within a few weeks, call the insurer again.</li>
    <li><strong>Check the new bill.</strong> Once insurance has processed the claim, the hospital should send an updated statement. Ask for an <a href="/guides/how-to-get-itemized-hospital-bill/">itemized bill</a> and compare it with your EOB.</li>
</ol>

<p>Hold off on paying the full-charge balance while the claim is pending. Paying now can mean chasing a refund later.</p>

<h2 id="timely-filing">3. Timely filing limits</h2>

<p>A <strong>timely filing limit</strong> is the deadline for a provider to send a claim to an insurer. Late claims can be denied. There is no single national deadline; it depends on your coverage, the hospital&rsquo;s contract with the plan, and state law.</p>

<table>
    <thead>
        <tr>
            <th>Coverage</th>
            <th>Filing deadline</th>
            <th>Source of the rule</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>Original Medicare</td>
            <td>1 calendar year (12 months) after the date of service, with limited exceptions</td>
            <td>42 CFR 424.44</td>
        </tr>
        <tr>
            <td>Medicaid</td>
            <td>State Medicaid agencies must require claims no later than 12 months from the date of service</td>
            <td>42 CFR 447.45(d)</td>
        </tr>
        <tr>
            <td>Private insurance (example: Texas HMO and PPO plans)</td>
            <td>95 days after the date of service, unless the contract allows longer</td>
            <td>Texas Insurance Code 843.337 and 1301.102</td>
        </tr>
        <tr>
            <td>Other private plans</td>
            <td>Set by the plan and the hospital&rsquo;s network contract, and by state law where it applies</td>
            <td>Ask your insurer</td>
        </tr>
    </tbody>
</table>

<p>Medicare&rsquo;s exceptions include delays caused by a Medicare error and cases where Medicare coverage was granted retroactively. Under Original Medicare, the law requires the hospital to file the claim for you. If it is near the 12-month mark and the hospital still has not filed, Medicare.gov says you can file it yourself using form CMS-1490S.</p>

<p>The clock usually runs from the date of service, not from the date you got the bill, so act as soon as you notice the problem.</p>

<h2 id="who-pays">4. Who pays if the hospital filed too late</h2>

<p>If you gave the hospital your insurance information and it still missed the deadline, you may not have to pay the full bill. It depends on your coverage.</p>

<p><strong>Original Medicare.</strong> The Medicare Claims Processing Manual says that when the provider is responsible for not filing a timely claim, the provider may not charge the beneficiary, except for the deductible and coinsurance that would have applied if Medicare had paid. This also covers cases where the hospital had reason to believe you might have Medicare and did not take steps to get your information.</p>

<p><strong>Medicaid.</strong> Federal rules require states to limit Medicaid to providers who accept Medicaid&rsquo;s payment as payment in full, plus any cost sharing the plan allows. Our guide to <a href="/guides/medicaid-billing-rights/">Medicaid billing rights</a> covers this in more detail.</p>

<p><strong>Private insurance with an in-network hospital.</strong> Network contracts commonly include a &ldquo;hold harmless&rdquo; clause, which bars the provider from billing you for amounts the plan owes. Some states write this into law. For example, Arizona requires contracts between health care services organizations and providers to say the provider will not bill the enrollee if the organization fails to pay for covered services (A.R.S. 20-1072). How this applies to a late-filed claim depends on your plan, your state, and the contract. Your insurer can tell you whether the denial is marked as provider liability on your EOB. If it is unclear, contact your state insurance department.</p>

<p><strong>Out-of-network hospital.</strong> With no contract between the hospital and your plan, there is no network hold-harmless clause. Ask your insurer whether it will accept a late claim, and see our guide on <a href="/guides/out-of-network-medical-bills/">out-of-network bills</a>.</p>

<p>Keep proof of when you gave the hospital your insurance information. That record shows the delay was not yours. If you are pressed to pay a bill you believe the hospital is responsible for, consider talking to a consumer attorney or legal aid.</p>

<div class="key-takeaway"><h3>Key takeaway</h3><p>Filing deadlines run from the date of service, so send your insurance details in writing today. If the insurer still denies the claim, our guide on <a href="/guides/insurance-claim-denied-what-to-do/">what to do when a claim is denied</a> walks through your options.</p></div>

<h2 id="hold">5. Ask the hospital to hold your account</h2>

<p>Ask the billing office in writing to put a hold on your account while the claim is sorted out. A hold pauses statements and collection activity. Ask them to confirm the hold and its length in writing.</p>

<p>If the hospital is a nonprofit, federal tax rules add some breathing room. Under IRS rules for nonprofit hospitals, there is a 120-day notification period after the first post-discharge bill before the hospital may take extraordinary collection actions. Those include reporting you to credit bureaus, selling your debt, and legal actions such as liens or wage garnishment. The same rules give you a 240-day period to apply for financial assistance. If your balance is still large after insurance pays, see our guide to <a href="/guides/hospital-financial-assistance-charity-care/">hospital financial assistance</a>.</p>

<h2 id="medicaid-retro">6. Uninsured then, eligible for Medicaid now</h2>

<p>If you had no insurance on the date of service but your income was low, Medicaid may still be able to pay. This is called <strong>retroactive eligibility</strong>.</p>

<p><strong>As of November 2026:</strong> Federal rules require state Medicaid programs to make coverage start as early as the third month before the month you apply. Two conditions apply: you received services Medicaid covers during that time, and you would have qualified then if you had applied.</p>

<p><strong>Changing on January 1, 2027:</strong> The 2025 federal law (Public Law 119-21) shortens that window. According to CMS, for applications made on or after January 1, 2027:</p>
<ul>
    <li>Adults in the Medicaid expansion group get up to <strong>one month</strong> of retroactive coverage before the month they apply.</li>
    <li>Everyone else gets up to <strong>two months</strong>.</li>
</ul>

<p><strong>Example:</strong> You had an ER visit on October 10, 2026. If you apply in December 2026, the current three-month window reaches back to September 2026, which covers the visit. If you wait and apply in January 2027 as an expansion adult, the window reaches back only to December 2026, which does not.</p>

<p>If you think you might qualify, apply now (see <a href="/guides/how-to-apply-for-medicaid/">how to apply for Medicaid</a>). Then tell the hospital in writing that you applied and when, and ask it to hold the account until Medicaid decides. Once approved, ask the hospital to bill Medicaid for the covered dates.</p>

<div class="key-takeaway"><h3>Key takeaway</h3><p>Get every hold and promise in writing, with dates and reference numbers. If the hospital won&rsquo;t correct the bill after insurance or Medicaid processes it, follow our steps on <a href="/guides/how-to-dispute-a-medical-bill/">how to dispute a medical bill</a>.</p></div>

<h2 id="script">7. Phone and letter script</h2>

<p>Call, then send the same points in writing.</p>

<p><strong>Phone:</strong> &ldquo;Hi, I&rsquo;m calling about account number [number] for [patient name], date of service [date]. My bill shows self-pay, but I had insurance on that date. I&rsquo;d like to give you my insurance information and ask you to submit the claim. Can you also put my account on hold while the claim is processed? Can I have your name and a reference number?&rdquo;</p>

<p><strong>Letter or portal message:</strong></p>
<p>&ldquo;Re: Account [number], patient [name], date of service [date].<br>
My statement shows this account as self-pay. I had active coverage on the date of service with [insurer], member ID [ID], group number [number]. A copy of my insurance card is attached. Please submit this claim to my insurer, or resubmit it if it was sent with incorrect information, and send me written confirmation of the date it was submitted. Please place my account on hold and do not send it to collections while the claim is processed. If the claim is denied for timely filing, please explain in writing why my information was not used, since I provided it on [date]. Thank you.&rdquo;</p>

<p>For more wording, see our <a href="/guides/medical-bill-dispute-phone-scripts/">medical bill phone scripts</a>.</p>

<h2 id="faq">Frequently asked questions</h2>

<div class="faq-section">
    <div class="faq-item">
        <h3>How do I know if the hospital billed my insurance?</h3>
        <p>Look for an explanation of benefits (EOB) from your insurer for that date, and for an insurance payment or adjustment line on the bill. If there is no EOB and the balance equals the full charges, the claim was likely never processed. Call your insurer to check.</p>
    </div>
    <div class="faq-item">
        <h3>Can the hospital still bill my insurance after a few months?</h3>
        <p>Often, yes, if the filing deadline has not passed. Original Medicare allows 12 months from the date of service, and Medicaid agencies must require claims within 12 months. Private plan deadlines are set by contract and state law. Ask the hospital to submit the claim now and confirm the deadline with your insurer.</p>
    </div>
    <div class="faq-item">
        <h3>Do I have to pay if the hospital missed the timely filing deadline?</h3>
        <p>It depends on your coverage. Under Medicare rules, a provider responsible for late filing may not charge you except for the deductible and coinsurance you would have owed. Medicaid providers must accept Medicaid payment as payment in full, apart from allowed cost sharing. For private plans, in-network contracts and some state laws limit billing you for amounts the plan owes. Ask your insurer or state insurance department.</p>
    </div>
    <div class="faq-item">
        <h3>I was uninsured when I went to the hospital but qualify for Medicaid now. Can Medicaid cover it?</h3>
        <p>Possibly. Federal rules require Medicaid to cover up to three months before the month you apply, if you received covered services and would have qualified then. For applications made on or after January 1, 2027, that window shrinks to one month for adults in the Medicaid expansion group and two months for others. Apply as soon as you can and tell the hospital you applied.</p>
    </div>
    <div class="faq-item">
        <h3>Can the hospital send my bill to collections while the insurance claim is sorted out?</h3>
        <p>Ask the billing office in writing to put the account on hold while the claim is processed. Nonprofit hospitals must also follow IRS rules that generally require them to wait at least 120 days after the first post-discharge bill before extraordinary collection actions such as credit reporting or selling the debt.</p>
    </div>
</div>

<h2 id="sources">Sources</h2>

<ul class="sources-list">
    <li><a href="https://www.law.cornell.edu/cfr/text/42/424.44" target="_blank" rel="noopener">Cornell LII &mdash; 42 CFR 424.44, Time limits for filing claims (Medicare)</a></li>
    <li><a href="https://www.cms.gov/Regulations-and-Guidance/Guidance/Manuals/downloads/clm104c01.pdf" target="_blank" rel="noopener">CMS &mdash; Medicare Claims Processing Manual, Chapter 1, Section 70.4 (untimely filing and beneficiary liability)</a></li>
    <li><a href="https://www.medicare.gov/claims-appeals/how-do-i-file-a-claim" target="_blank" rel="noopener">Medicare.gov &mdash; Filing a claim</a></li>
    <li><a href="https://www.law.cornell.edu/cfr/text/42/447.45" target="_blank" rel="noopener">Cornell LII &mdash; 42 CFR 447.45, Timely claims payment (Medicaid)</a></li>
    <li><a href="https://www.law.cornell.edu/cfr/text/42/447.15" target="_blank" rel="noopener">Cornell LII &mdash; 42 CFR 447.15, Acceptance of State payment as payment in full (Medicaid)</a></li>
    <li><a href="https://www.law.cornell.edu/cfr/text/42/435.915" target="_blank" rel="noopener">Cornell LII &mdash; 42 CFR 435.915, Effective date (Medicaid retroactive eligibility)</a></li>
    <li><a href="https://www.medicaid.gov/federal-policy-guidance/downloads/cib11182025.pdf" target="_blank" rel="noopener">CMS &mdash; CMCS Informational Bulletin, November 18, 2025: Summary of Medicaid and CHIP provisions of Public Law 119-21 (Section 71112)</a></li>
    <li><a href="https://www.irs.gov/charities-non-profits/billing-and-collections-section-501r6" target="_blank" rel="noopener">IRS &mdash; Billing and collections, Section 501(r)(6)</a></li>
    <li><a href="https://www.azleg.gov/ars/20/01072.htm" target="_blank" rel="noopener">Arizona Legislature &mdash; A.R.S. 20-1072, Nonliability of enrollees for provider or hospital charges</a></li>
    <li><a href="https://tdi.texas.gov/hprovider/ppsb418faq.html" target="_blank" rel="noopener">Texas Department of Insurance &mdash; Prompt pay FAQ (95-day claim filing deadline)</a></li>
</ul>
""",
})
