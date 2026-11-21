"""Guide: Medicare's WISeR Prior Authorization Pilot: What Patients Should Know."""

from guides import register

register("medicare-wiser-prior-authorization", {
    "title": "Medicare WISeR Prior Authorization: A 2026 Patient Guide",
    "meta_description": "Medicare's WISeR pilot requires prior authorization for some services in 6 states. What a non-affirmation means, who pays, and how to appeal a denial.",
    "published": "2026-11-20",
    "reviewed_on": "2026-11-20",
    "author": "BillKarma Team",
    "category": "Patient Rights",
    "faqs": [
        {
            "q": "Does WISeR apply to Medicare Advantage?",
            "a": "No. CMS says WISeR does not apply to people with Medicare Advantage and will have no impact on them. It applies only to Original Medicare (Parts A and B) in Arizona, New Jersey, Ohio, Oklahoma, Texas and Washington.",
        },
        {
            "q": "What does 'non-affirmed' mean?",
            "a": "It means the reviewer found that, based on the records sent, the planned service did not meet Medicare's coverage, coding or payment rules. CMS says a non-affirmation does not stop the provider from doing the service and sending a claim, and a human clinician must review every non-affirmation. Your provider can resubmit with more records as many times as needed and can ask for a peer-to-peer talk with a reviewer.",
        },
        {
            "q": "Can I be billed if my procedure was not affirmed?",
            "a": "It depends on whether you were properly warned. CMS's operational guide says a provider who gets a non-affirmation for medical necessity should give you an Advance Beneficiary Notice of Non-coverage (ABN) before doing the service. Under CMS's ABN rules, a provider who cannot show it gave you proper advance notice generally cannot shift the cost to you. If you signed an ABN and chose Option 1, you may owe the bill if Medicare denies the claim, but you keep the right to appeal.",
        },
        {
            "q": "How long do I have to appeal a denied claim?",
            "a": "For Original Medicare, you have 120 days from the date you receive your Medicare Summary Notice (MSN) to ask for a redetermination, the first level of appeal. Medicare assumes you got the notice 5 days after the date printed on it. The Medicare contractor generally decides within 60 days.",
        },
        {
            "q": "Is WISeR ending?",
            "a": "Not as of November 2026. CMS lists the model as running from January 1, 2026 through December 31, 2031. On July 16, 2026, the Senate voted 46-50 against taking up a resolution (S.J.Res. 198) that would have overturned it.",
        },
        {
            "q": "Who can help me for free?",
            "a": "Call 1-800-MEDICARE (1-800-633-4227; TTY 1-877-486-2048) or your State Health Insurance Assistance Program (SHIP). Medicare.gov says SHIPs give free help with denials and appeals. Find your state's SHIP at shiphelp.org.",
        },
    ],
    "body": f"""
<p class="lead">As of November 2026, Medicare&rsquo;s WISeR pilot is still running in six states after a July 2026 Senate vote kept it in place, and October 2026 reporting on released records described delays and high rejection rates in at least one state. If you have Original Medicare in Arizona, New Jersey, Ohio, Oklahoma, Texas or Washington and a listed procedure was delayed or &ldquo;not affirmed,&rdquo; you still have rights: your provider can resubmit, you generally can&rsquo;t be billed for a denied service unless you were warned in writing first, and you can appeal a denied claim within 120 days of your Medicare Summary Notice.</p>

<nav class="toc">
    <h2>In this guide</h2>
    <ol>
        <li><a href="#what-is-wiser">What WISeR is, and who it affects</a></li>
        <li><a href="#your-bill">What this means for your bill</a></li>
        <li><a href="#services">Which services need prior authorization</a></li>
        <li><a href="#how-it-works">How the review works and how long it takes</a></li>
        <li><a href="#not-affirmed">If your procedure was &ldquo;not affirmed&rdquo;</a></li>
        <li><a href="#appeal">If you got a bill or a denied claim: step by step</a></li>
        <li><a href="#news">The debate: what critics and CMS say</a></li>
        <li><a href="#faq">Frequently asked questions</a></li>
        <li><a href="#sources">Sources</a></li>
    </ol>
</nav>

<h2 id="what-is-wiser">1. What WISeR is, and who it affects</h2>

<p>WISeR stands for the Wasteful and Inappropriate Service Reduction Model. The Centers for Medicare &amp; Medicaid Services (CMS) announced it in the Federal Register on July 1, 2025. It adds <strong>prior authorization</strong> (approval before a service is done) to Original Medicare for a short list of planned, non-emergency services. CMS says the model runs for six years, from January 1, 2026 through December 31, 2031.</p>

<p>Private technology companies, which CMS calls &ldquo;participants,&rdquo; do the reviews. They may use AI tools, but CMS says a non-affirmation &ldquo;cannot be performed solely by technology&rdquo; and needs a human clinician&rsquo;s review. Each state has one company:</p>

<ul>
    <li><strong>Arizona:</strong> Zyter</li>
    <li><strong>New Jersey:</strong> Genzeon</li>
    <li><strong>Ohio:</strong> Innovaccer</li>
    <li><strong>Oklahoma:</strong> Humata Health</li>
    <li><strong>Texas:</strong> Cohere Health</li>
    <li><strong>Washington:</strong> Virtix Health</li>
</ul>

<p><strong>Not affected:</strong> people with Medicare Advantage, which CMS says WISeR &ldquo;does not apply to.&rdquo; Emergency services, inpatient-only services, and services that would put you at substantial risk if delayed are excluded.</p>

<h2 id="your-bill">2. What this means for your bill</h2>

<p>WISeR changes the paperwork, not what Medicare covers. Three points matter most:</p>

<ul>
    <li><strong>Your provider requests approval, not you.</strong> The doctor, hospital or supplier sends the request. If they skip it, the claim goes through <em>pre-payment review</em> (records are checked before Medicare pays).</li>
    <li><strong>A warning comes before a bill.</strong> If a service is not affirmed and the provider still plans to do it, CMS&rsquo;s guide says the provider should give you an <strong>Advance Beneficiary Notice of Non-coverage (ABN)</strong>, form CMS-R-131, first. Under CMS&rsquo;s ABN rules, a provider who cannot show it gave proper advance notice generally cannot shift the cost to you.</li>
    <li><strong>Your appeal rights stay the same.</strong> CMS says WISeR &ldquo;preserves all Medicare appeals rights for providers and beneficiaries.&rdquo;</li>
</ul>

<div class="key-takeaway">
    <h3>Key takeaway</h3>
    <p>Before you pay a bill tied to a WISeR service, look for two things: a signed ABN and a Medicare Summary Notice showing the claim was denied. If either is missing, ask the billing office why. Our guide to <a href="/guides/medicare-summary-notice-vs-hospital-bill/">matching your Medicare Summary Notice to a hospital bill</a> walks through the comparison line by line.</p>
</div>

<h2 id="services">3. Which services need prior authorization</h2>

<p>CMS&rsquo;s WISeR Provider and Supplier Operational Guide (version 7.0, updated July 24, 2026) lists 13 service groups. Skin and tissue substitutes are included only in states and Medicare contractor areas with an active local coverage rule for them.</p>

<table>
    <thead>
        <tr>
            <th>Service group</th>
            <th>What it is, in plain terms</th>
        </tr>
    </thead>
    <tbody>
        <tr><td>Knee arthroscopic lavage and debridement</td><td>Scope surgery to wash out or trim a knee with osteoarthritis</td></tr>
        <tr><td>Induced lesions of nerve tracts</td><td>Using heat or other energy to block pain signals in a nerve</td></tr>
        <tr><td>Vagus nerve stimulation</td><td>An implanted device that stimulates a nerve in the neck</td></tr>
        <tr><td>Phrenic nerve stimulator</td><td>An implant that helps control breathing</td></tr>
        <tr><td>Electrical nerve stimulators</td><td>Devices that send small electrical pulses to ease pain</td></tr>
        <tr><td>Incontinence control devices</td><td>Implants or devices to control bladder leakage</td></tr>
        <tr><td>Sacral nerve stimulation for urinary incontinence</td><td>An implant near the tailbone for bladder control</td></tr>
        <tr><td>Diagnosis and treatment of impotence</td><td>Tests and treatments for erectile dysfunction</td></tr>
        <tr><td>Percutaneous vertebral augmentation</td><td>Injecting cement into a fractured spine bone (such as kyphoplasty)</td></tr>
        <tr><td>Epidural steroid injections for pain</td><td>Steroid shots near the spine (facet joint injections are excluded)</td></tr>
        <tr><td>Cervical fusion</td><td>Surgery that joins bones in the neck</td></tr>
        <tr><td>Hypoglossal nerve stimulation</td><td>An implant for obstructive sleep apnea</td></tr>
        <tr><td>Skin and tissue substitutes</td><td>Lab-made or donated tissue applied to chronic leg and foot wounds</td></tr>
    </tbody>
</table>

<p>Two services in the original 2025 notice are on hold. CMS published a delay notice in April 2026, and CMS&rsquo;s guide and KFF identify them as percutaneous image-guided lumbar decompression for spinal stenosis and deep brain stimulation. CMS says it will announce any new start date in the Federal Register.</p>

<h2 id="how-it-works">4. How the review works and how long it takes</h2>

<p>Your provider sends records to the state&rsquo;s WISeR company, directly or through its Medicare contractor. CMS&rsquo;s guide sets these targets:</p>

<table>
    <thead>
        <tr>
            <th>Step</th>
            <th>Time frame</th>
        </tr>
    </thead>
    <tbody>
        <tr><td>Standard prior authorization decision</td><td>Within 3 calendar days of the request</td></tr>
        <tr><td>Expedited (urgent) decision</td><td>Within 2 calendar days</td></tr>
        <tr><td>Provider sends records for pre-payment review</td><td>45 calendar days from the records request</td></tr>
        <tr><td>Pre-payment review decision</td><td>Within 3 calendar days of getting all records</td></tr>
        <tr><td>Resubmissions after a non-affirmation</td><td>No limit; same 3- or 2-day targets</td></tr>
    </tbody>
</table>

<p>CMS&rsquo;s guide says you also get a copy of the decision. Since July 2026, clinicians with a strong approval record (at least 10 requests and a minimum approval rate) can be exempted, which CMS calls &ldquo;gold carding.&rdquo;</p>

<h2 id="not-affirmed">5. If your procedure was &ldquo;not affirmed&rdquo;</h2>

<p>CMS defines a non-affirmation as a finding that a future service did not meet Medicare&rsquo;s coverage, coding or payment requirements. It is not a claim denial, and CMS says it does not prevent your provider from doing the service and sending a claim.</p>

<p><strong>What your provider can do:</strong></p>
<ul>
    <li><strong>Resubmit</strong> with more records, such as imaging, therapy notes or test results. CMS sets no limit on resubmissions.</li>
    <li><strong>Ask for peer-to-peer review</strong> as part of a resubmission: a call with a clinician reviewer who has expertise in the condition.</li>
    <li><strong>Give you an ABN</strong> if it still plans to do the service and expects Medicare to deny payment.</li>
</ul>

<p><strong>What you can do:</strong></p>
<ul>
    <li>Ask for the decision, the reason, and whether missing records were the issue.</li>
    <li>Ask whether they will resubmit or request peer-to-peer review, and when.</li>
    <li>Ask: &ldquo;Will I get an ABN before you do this service?&rdquo; An ABN lists the service, an estimated cost and why Medicare may not pay.</li>
</ul>

<p>Per CMS&rsquo;s ABN tutorial, <strong>Option 1</strong> means you get the service, accept financial responsibility if Medicare doesn&rsquo;t pay, and the provider files a claim you can appeal. <strong>Option 2</strong> means no claim is filed, so you have no appeal rights. <strong>Option 3</strong> means you decline the service and can&rsquo;t be charged for it.</p>

<div class="key-takeaway">
    <h3>Key takeaway</h3>
    <p>A non-affirmation is a starting point, not a final answer. Your provider can resubmit as often as needed, and you can ask for an ABN before any service that might be denied. Our <a href="/guides/insurance-prior-authorization-denied/">guide to prior authorization denials</a> has more questions to bring to your doctor&rsquo;s office.</p>
</div>

<h2 id="appeal">6. If you got a bill or a denied claim: step by step</h2>

<p>When a WISeR service is billed and Medicare denies the claim, that denial goes through the regular Medicare appeals process. Here is the order to work in:</p>

<ol>
    <li><strong>Find your Medicare Summary Notice (MSN).</strong> Medicare.gov says the MSN is &ldquo;not a bill.&rdquo; It lists what was billed, what Medicare paid and the most you may owe. You can sign up for electronic MSNs at Medicare.gov.</li>
    <li><strong>Match it to the bill.</strong> Check that the service, date and amount on the provider&rsquo;s bill match the MSN. A bill for more than the &ldquo;maximum you may be billed&rdquo; on the MSN is worth a call.</li>
    <li><strong>Check for an ABN.</strong> Ask the billing office for a copy of any ABN you signed. If you didn&rsquo;t get one, ask in writing why you are being billed. CMS&rsquo;s claims manual says a provider who cannot show it gave adequate advance notice cannot use the ABN rules to shift liability to you. Medicare decides liability case by case, and you can appeal that decision too.</li>
    <li><strong>Ask for an itemized bill</strong> and hold payment on the disputed line while you check it.</li>
    <li><strong>File a redetermination</strong> (the first level of appeal) within 120 days of receiving the MSN. Medicare assumes you received it 5 days after the date on it. Use form CMS-20027 or a signed letter with your name, Medicare number, the services and dates, and why you disagree. Send it to the contractor address on the last page of your MSN.</li>
    <li><strong>Include your doctor&rsquo;s support:</strong> a letter on medical necessity and the records sent for prior authorization.</li>
    <li><strong>Track the deadlines.</strong> The contractor generally decides within 60 days. If you disagree, you have 180 days to ask for level 2 (reconsideration by an independent contractor).</li>
</ol>

<p>For each appeal level, see <a href="/guides/how-to-dispute-medicare-bill/">how to dispute a Medicare bill</a>.</p>

<p><strong>Who to call:</strong> 1-800-MEDICARE (1-800-633-4227; TTY 1-877-486-2048), or your <strong>State Health Insurance Assistance Program (SHIP)</strong>, which Medicare.gov says gives free help with denials and appeals (find yours at shiphelp.org). If a bill goes to collections or ends up in court, consider talking to a consumer attorney or legal aid.</p>

<h2 id="news">7. The debate: what critics and CMS say</h2>

<p>The figures below come from news reports and advocacy groups, not CMS audits, and some are disputed.</p>

<ul>
    <li><strong>Delays:</strong> A June 2026 KFF Health News report, run by CBS News, described delays and errors, including nearly 100 University of Washington patients waiting for epidurals, per a report from Sen. Maria Cantwell&rsquo;s office.</li>
    <li><strong>Released records:</strong> In October 2026, KUOW reported on CMS records released by the Electronic Frontier Foundation, an advocacy group. Per KUOW, they show Washington&rsquo;s vendor, Virtix Health, rejected 53% of 6,096 claims in early 2026 and was put on a corrective action plan, which CMS confirmed closed in August. Virtix blamed incomplete documentation and says 84.3% of requests are affirmed after resubmission; the two figures measure different things.</li>
    <li><strong>Payment:</strong> KUOW reported that the records show vendors receive 25% of averted procedure costs, reduced for slow or inaccurate decisions. Critics, including the Washington State Hospital Association, say a share-of-savings design could reward denials.</li>
</ul>

<p><strong>CMS&rsquo;s position:</strong> CMS innovation center director Abe Sutton told KFF Health News the model &ldquo;aims to reduce inappropriate care without delaying appropriate care,&rdquo; and said payment backlogs were being resolved. CMS has said every non-affirmation is reviewed by a human clinician, and a CMS spokesperson told KFF Health News in 2025 that vendors are barred from pay tied to denial rates.</p>

<p><strong>In Congress:</strong> In May 2026, the Government Accountability Office concluded the WISeR notice counts as a rule under the Congressional Review Act. On July 16, 2026, the Senate voted 46&ndash;50 against taking up S.J.Res. 198, which would have overturned it. As of November 2026, WISeR remains in effect.</p>

<div class="key-takeaway">
    <h3>Key takeaway</h3>
    <p>Whatever happens to the pilot, your deadlines still apply. Don&rsquo;t let the 120-day window pass while you wait on phone calls. File the redetermination in writing, keep copies, and check the hospital bill itself for errors. You can <a href="/scan">check your bill free</a> to compare each line to Medicare rates before you pay anything.</p>
</div>

<h2 id="faq">Frequently asked questions</h2>

<div class="faq-section">
    <div class="faq-item">
        <h3>Does WISeR apply to Medicare Advantage?</h3>
        <p>No. CMS says WISeR does not apply to people with Medicare Advantage and will have no impact on them. It applies only to Original Medicare (Parts A and B) in Arizona, New Jersey, Ohio, Oklahoma, Texas and Washington.</p>
    </div>
    <div class="faq-item">
        <h3>What does &ldquo;non-affirmed&rdquo; mean?</h3>
        <p>It means the reviewer found that, based on the records sent, the planned service did not meet Medicare&rsquo;s coverage, coding or payment rules. CMS says a non-affirmation does not stop the provider from doing the service and sending a claim, and a human clinician must review every non-affirmation. Your provider can resubmit with more records as many times as needed and can ask for a peer-to-peer talk with a reviewer.</p>
    </div>
    <div class="faq-item">
        <h3>Can I be billed if my procedure was not affirmed?</h3>
        <p>It depends on whether you were properly warned. CMS&rsquo;s operational guide says a provider who gets a non-affirmation for medical necessity should give you an Advance Beneficiary Notice of Non-coverage (ABN) before doing the service. Under CMS&rsquo;s ABN rules, a provider who cannot show it gave you proper advance notice generally cannot shift the cost to you. If you signed an ABN and chose Option 1, you may owe the bill if Medicare denies the claim, but you keep the right to appeal.</p>
    </div>
    <div class="faq-item">
        <h3>How long do I have to appeal a denied claim?</h3>
        <p>For Original Medicare, you have 120 days from the date you receive your Medicare Summary Notice (MSN) to ask for a redetermination, the first level of appeal. Medicare assumes you got the notice 5 days after the date printed on it. The Medicare contractor generally decides within 60 days.</p>
    </div>
    <div class="faq-item">
        <h3>Is WISeR ending?</h3>
        <p>Not as of November 2026. CMS lists the model as running from January 1, 2026 through December 31, 2031. On July 16, 2026, the Senate voted 46&ndash;50 against taking up a resolution (S.J.Res. 198) that would have overturned it.</p>
    </div>
    <div class="faq-item">
        <h3>Who can help me for free?</h3>
        <p>Call 1-800-MEDICARE (1-800-633-4227; TTY 1-877-486-2048) or your State Health Insurance Assistance Program (SHIP). Medicare.gov says SHIPs give free help with denials and appeals. Find your state&rsquo;s SHIP at shiphelp.org.</p>
    </div>
</div>

<h2 id="sources">Sources</h2>

<ul class="sources-list">
    <li><a href="https://www.cms.gov/priorities/innovation/innovation-models/wiser" target="_blank" rel="noopener">CMS &mdash; WISeR (Wasteful and Inappropriate Service Reduction) Model</a></li>
    <li><a href="https://www.cms.gov/priorities/innovation/files/document/wiser-model-frequently-asked-questions" target="_blank" rel="noopener">CMS &mdash; WISeR Model Frequently Asked Questions</a></li>
    <li><a href="https://www.cms.gov/priorities/innovation/files/wiser-provider-supplier-guide.pdf" target="_blank" rel="noopener">CMS &mdash; WISeR Provider and Supplier Operational Guide, Version 7.0 (July 24, 2026)</a></li>
    <li><a href="https://www.federalregister.gov/documents/2025/07/01/2025-12195/medicare-program-implementation-of-prior-authorization-for-select-services-for-the-wasteful-and" target="_blank" rel="noopener">Federal Register &mdash; Implementation of Prior Authorization for Select Services for the WISeR Model (July 1, 2025)</a></li>
    <li><a href="https://public-inspection.federalregister.gov/2026-06616.pdf" target="_blank" rel="noopener">Federal Register &mdash; Notice delaying two WISeR services (April 2026)</a></li>
    <li><a href="https://www.cms.gov/Outreach-and-Education/Medicare-Learning-Network-MLN/MLNProducts/ABN-Tutorial/formCMSR131tutorial111915f.html" target="_blank" rel="noopener">CMS &mdash; Advance Beneficiary Notice of Non-coverage Tutorial (MLN909183)</a></li>
    <li><a href="https://www.cms.gov/regulations-and-guidance/guidance/manuals/downloads/clm104c30.pdf" target="_blank" rel="noopener">CMS &mdash; Medicare Claims Processing Manual, Chapter 30: Financial Liability Protections</a></li>
    <li><a href="https://www.cms.gov/medicare/appeals-grievances/fee-for-service/first-level-appeal-redetermination-medicare-contractor" target="_blank" rel="noopener">CMS &mdash; First Level of Appeal: Redetermination by a Medicare Contractor</a></li>
    <li><a href="https://www.medicare.gov/providers-services/claims-appeals-complaints/appeals/original-medicare" target="_blank" rel="noopener">Medicare.gov &mdash; Appeals in Original Medicare</a></li>
    <li><a href="https://www.medicare.gov/basics/forms-publications-mailings/mailings/costs-and-coverage/medicare-summary-notice" target="_blank" rel="noopener">Medicare.gov &mdash; Medicare Summary Notice (MSN)</a></li>
    <li><a href="https://www.medicare.gov/basics/your-medicare-rights/get-help-with-your-rights-protections" target="_blank" rel="noopener">Medicare.gov &mdash; Get help with your rights &amp; protections (SHIP)</a></li>
    <li><a href="https://www.senate.gov/legislative/LIS/roll_call_votes/vote1192/vote_119_2_00199.htm" target="_blank" rel="noopener">U.S. Senate &mdash; Roll Call Vote on Motion to Proceed to S.J.Res. 198 (July 16, 2026)</a></li>
    <li><a href="https://www.gao.gov/products/b-337994" target="_blank" rel="noopener">GAO &mdash; Decision B-337994 on the WISeR Model notice under the Congressional Review Act</a></li>
    <li><a href="https://www.kff.org/medicare/examining-the-potential-impact-of-medicares-new-wiser-model/" target="_blank" rel="noopener">KFF &mdash; Examining the Potential Impact of Medicare&rsquo;s New WISeR Model</a></li>
    <li><a href="https://www.cbsnews.com/news/medicare-ai-program-wiser-prior-authorization-errors-delays/" target="_blank" rel="noopener">KFF Health News via CBS News &mdash; Medicare&rsquo;s AI Push Snarls Patients and Doctors in Errors and Delays (June 2026)</a></li>
    <li><a href="https://kffhealthnews.org/news/article/ai-medicare-prior-authorization-trump-pilot-program-wiser/" target="_blank" rel="noopener">KFF Health News &mdash; AI Will Soon Have a Say in Approving or Denying Medicare Treatments (September 2025)</a></li>
    <li><a href="https://www.kuow.org/health-care/2026-10-27/records-show-confusion-finger-pointing-during-ai-medicare-rollout" target="_blank" rel="noopener">KUOW &mdash; Records show confusion, finger-pointing during AI Medicare rollout (October 27, 2026)</a></li>
</ul>
""",
})
