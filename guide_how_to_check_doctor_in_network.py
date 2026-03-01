"""Guide: How to Check If Your Doctor Is In-Network."""

from guides import register, _embed

register("how-to-check-doctor-in-network", {
    "title": "How to Check If Your Doctor Is In-Network Before Your Visit",
    "meta_description": "Don&rsquo;t get surprise out-of-network bills. Learn 5 ways to verify your doctor is in-network before your appointment, plus what to do if your provider drops your plan.",
    "published": "2026-03-01",
    "author": "BillKarma Team",
    "category": "Insurance",
    "faqs": [
        {
            "q": "How do I know if my doctor is in-network?",
            "a": "The most reliable way is to log into your health insurance company\u2019s website or app and search the provider directory for your doctor by name. You can also call the number on the back of your insurance card and ask a representative to confirm your doctor\u2019s network status. Always verify within 2\u20134 weeks of your appointment because networks change quarterly.",
        },
        {
            "q": "What happens if I accidentally see an out-of-network doctor?",
            "a": "If you accidentally see an out-of-network provider, you may owe the full billed amount minus whatever your insurer reimburses at the out-of-network rate, which is typically 50\u201370% less than the in-network rate. However, the No Surprises Act protects you from surprise out-of-network bills at in-network facilities for emergency services and certain non-emergency situations where you had no choice of provider. File an appeal with your insurer and request in-network pricing if you were not informed.",
        },
        {
            "q": "Can my doctor drop my insurance mid-treatment?",
            "a": "Yes, doctors can leave insurance networks at any time, though most contracts require 60\u201390 days\u2019 notice. If your doctor drops your plan mid-treatment, most states have continuity of care laws that require your insurer to cover ongoing treatment at in-network rates for 60\u2013120 days. Contact your insurance company immediately to request a continuity of care exception.",
        },
        {
            "q": "Is my doctor in-network if the hospital is in-network?",
            "a": "Not necessarily. A hospital can be in-network while individual doctors who practice there \u2014 including anesthesiologists, radiologists, pathologists, and assistant surgeons \u2014 may be out-of-network. This is one of the most common sources of surprise medical bills. The No Surprises Act now protects patients from surprise bills from out-of-network providers at in-network facilities in many situations.",
        },
        {
            "q": "How often do provider networks change?",
            "a": "Insurance networks can change quarterly. Doctors join and leave networks throughout the year based on contract negotiations. A directory listing from six months ago may be outdated. Always verify network status within two to four weeks of your scheduled appointment, and ask for written confirmation with an effective date range.",
        },
        {
            "q": "Does the No Surprises Act protect me from all out-of-network bills?",
            "a": "No. The No Surprises Act protects you from surprise out-of-network bills for emergency services, air ambulance services, and non-emergency services at in-network facilities where you did not choose the out-of-network provider. It does not protect you if you knowingly choose an out-of-network provider, visit an out-of-network facility for a scheduled procedure, or receive ground ambulance services.",
        },
    ],
    "body": f"""
<p class="lead">You book an appointment, show your insurance card, and assume everything is covered. Then a bill arrives for $3,000 because your doctor wasn&rsquo;t actually in your insurance network. This scenario happens to an estimated 1 in 5 Americans each year. Out-of-network care costs <strong>2&ndash;5x more</strong> than in-network care for the same service, and the difference comes straight out of your pocket. The good news: verifying your doctor&rsquo;s network status takes less than 10 minutes and can save you thousands. This guide shows you exactly how to do it.</p>

<nav class="toc">
    <h2>In this guide</h2>
    <ol>
        <li><a href="#why-network-status-matters">Why in-network vs. out-of-network matters</a></li>
        <li><a href="#five-ways-to-verify">5 ways to verify your doctor is in-network</a></li>
        <li><a href="#common-traps">Common traps: in-network doctor, out-of-network facility</a></li>
        <li><a href="#specialists-and-ancillary">What about specialists, anesthesiologists, and labs</a></li>
        <li><a href="#doctor-drops-network">What to do if your doctor drops your network mid-treatment</a></li>
        <li><a href="#no-surprises-act">How the No Surprises Act protects you</a></li>
        <li><a href="#accidentally-out-of-network">What to do if you accidentally see an out-of-network provider</a></li>
        <li><a href="#faq">Frequently asked questions</a></li>
        <li><a href="#sources">Sources</a></li>
    </ol>
</nav>

<h2 id="why-network-status-matters">1. Why in-network vs. out-of-network matters</h2>

<p>When a doctor is &ldquo;in-network,&rdquo; it means they have a contract with your insurance company to accept negotiated rates for their services. These rates are typically 40&ndash;60% lower than the provider&rsquo;s full billed charges. When a doctor is &ldquo;out-of-network,&rdquo; no such contract exists &mdash; the provider can bill whatever they choose, and your insurance covers far less (or nothing at all).</p>

<p>The financial difference is dramatic. Here&rsquo;s what the same services cost in-network vs. out-of-network for a patient with a typical PPO plan:</p>

<table>
    <thead>
        <tr><th>Service</th><th>In-Network Cost (Your Share)</th><th>Out-of-Network Cost (Your Share)</th><th>Difference</th></tr>
    </thead>
    <tbody>
        <tr><td>Primary care visit (99213)</td><td>$30 copay</td><td>$185&ndash;$350</td><td>6&ndash;12x more</td></tr>
        <tr><td>Specialist visit (99214)</td><td>$50 copay</td><td>$250&ndash;$500</td><td>5&ndash;10x more</td></tr>
        <tr><td>MRI (knee, CPT 73721)</td><td>$150&ndash;$400 (coinsurance)</td><td>$1,200&ndash;$3,500</td><td>3&ndash;9x more</td></tr>
        <tr><td>Outpatient surgery (arthroscopy)</td><td>$500&ndash;$2,000 (coinsurance)</td><td>$5,000&ndash;$15,000</td><td>3&ndash;8x more</td></tr>
    </tbody>
</table>

<p>Three factors drive this gap:</p>

<ul>
    <li><strong>No negotiated rate.</strong> In-network providers agree to accept the insurer&rsquo;s contracted rate as payment in full. Out-of-network providers have no such agreement and bill their full chargemaster price, which is often 3&ndash;10x the Medicare rate.</li>
    <li><strong>Higher cost-sharing.</strong> Most plans apply a separate, higher <a href="/guides/copay-vs-coinsurance-vs-deductible">deductible and coinsurance</a> for out-of-network care. A plan might cover 80% in-network but only 50% out-of-network &mdash; and that 50% is calculated on the insurer&rsquo;s &ldquo;allowed amount,&rdquo; not the provider&rsquo;s full charge.</li>
    <li><strong>Balance billing.</strong> Out-of-network providers can &ldquo;balance bill&rdquo; you for the difference between what they charge and what your insurer pays. If a surgeon charges $10,000, your insurer pays $4,000 as the allowed amount, and you owe the remaining $6,000 on top of your coinsurance. The No Surprises Act now restricts this practice in many situations, but not all.</li>
</ul>

<div class="key-takeaway">
    <strong>Bottom line:</strong> Seeing an out-of-network provider can cost you 2&ndash;5x more for the same service. A 10-minute verification call before your appointment is the single most effective way to avoid a surprise bill. Use our <a href="/calculator">calculator</a> to compare what Medicare pays for your procedure vs. what you were charged.
</div>

<h2 id="five-ways-to-verify">2. Five ways to verify your doctor is in-network</h2>

<p>Never assume a doctor is in-network just because they were last year, because the office staff said so informally, or because the facility is in-network. Use at least two of these five methods to confirm:</p>

<h3>a) Search your insurer&rsquo;s online provider directory</h3>

<p>Log into your health insurance company&rsquo;s website or app and use the &ldquo;Find a Doctor&rdquo; or &ldquo;Provider Directory&rdquo; tool. Search for your doctor by name, specialty, and location. The directory should show whether the provider is in-network for your specific plan (not just the insurer &mdash; plans within the same insurer can have different networks). Take a screenshot of the result with the date visible. This is your documentation if a billing dispute arises later.</p>

<p><strong>Important caveat:</strong> Online directories are notoriously inaccurate. A 2024 CMS study found that up to 48% of provider directory listings contained at least one inaccuracy &mdash; wrong address, wrong phone number, or incorrect network status. Use this as a starting point, not your only verification.</p>

<h3>b) Call your insurance company directly</h3>

<p>Call the member services number on the back of your insurance card. Ask: &ldquo;Is Dr. [Name] at [Address] in-network for my specific plan, [Plan Name/ID]?&rdquo; Write down the representative&rsquo;s name, the date and time of the call, and the reference number. If the representative confirms the doctor is in-network, ask them to note this confirmation in your account.</p>

<h3>c) Call the doctor&rsquo;s office</h3>

<p>Call the provider&rsquo;s billing or front desk and ask: &ldquo;Do you accept [Insurance Company], [Plan Name]?&rdquo; Be specific about your plan name &mdash; a provider might accept Blue Cross Blue Shield PPO but not Blue Cross Blue Shield HMO. Ask the office to verify with their credentialing department, not just the front desk receptionist, who may not know the current contract status.</p>

<h3>d) Check your insurance ID card</h3>

<p>Your insurance card lists your plan type (HMO, PPO, EPO, POS) and network name. Some cards print the network name explicitly (e.g., &ldquo;Aetna Open Access&rdquo; or &ldquo;UnitedHealthcare Choice Plus&rdquo;). When you call the provider&rsquo;s office, reference this network name. The office can cross-check it against their contracts. If your card lists a network like &ldquo;First Health&rdquo; or &ldquo;PHCS,&rdquo; mention that specifically &mdash; some providers participate in rental networks without realizing it.</p>

<h3>e) Get written confirmation</h3>

<p>For expensive procedures or specialist visits, request written confirmation of network status from your insurer. This can be an email, a letter, or a secure message through the insurer&rsquo;s member portal. Written confirmation is the strongest evidence you can have if you later receive a surprise out-of-network bill. Some insurers offer a &ldquo;pre-visit coverage check&rdquo; or &ldquo;benefits verification&rdquo; that documents the provider&rsquo;s network status and your expected cost-sharing in writing.</p>

<h3>Pre-visit verification checklist</h3>

<ul>
    <li>Searched insurer&rsquo;s online provider directory and saved a screenshot with date</li>
    <li>Called insurer&rsquo;s member services and noted the representative&rsquo;s name and reference number</li>
    <li>Called provider&rsquo;s office and confirmed they accept your specific plan</li>
    <li>For procedures: confirmed the facility is also in-network</li>
    <li>For procedures: asked about ancillary providers (anesthesia, pathology, lab)</li>
    <li>Requested written confirmation for any visit expected to exceed $500</li>
</ul>

<div class="key-takeaway">
    <strong>The two-call rule:</strong> Always verify with both the insurer and the provider&rsquo;s office. The insurer may show the doctor as in-network, but the provider may have recently terminated their contract. The provider may say they accept your insurance, but they may be out-of-network for your specific plan tier. Two calls take five minutes each and can save thousands.
</div>

<h2 id="common-traps">3. Common traps: in-network doctor, out-of-network facility (and vice versa)</h2>

<p>One of the most expensive mistakes in healthcare billing is assuming that if one provider is in-network, everyone involved in your care is too. Here are the traps patients fall into most often:</p>

<h3>Trap 1: Your doctor is in-network, but the facility is not</h3>

<p>You verify that your surgeon is in-network and schedule a procedure. But the surgery center or hospital where the procedure takes place is out-of-network. You receive an in-network bill from the surgeon and a massive out-of-network bill from the facility. This is common with ambulatory surgery centers and smaller hospitals that may not contract with all insurers.</p>

<h3>Trap 2: The facility is in-network, but your doctor is not</h3>

<p>You choose an in-network hospital, but the doctor who treats you there &mdash; an ER physician, hospitalist, or specialist &mdash; is an independent contractor who doesn&rsquo;t participate in your network. Before the No Surprises Act, this was the leading cause of surprise medical bills. The law now protects patients in many of these situations, but gaps remain for scheduled, elective procedures where you chose the out-of-network provider. See our <a href="/guides/no-surprises-act-explained">No Surprises Act guide</a> for details.</p>

<h3>Trap 3: Your doctor moves to a new practice or location</h3>

<p>Your doctor was in-network at their old practice. They move to a new practice, and you follow them. The new practice may not have the same insurance contracts. Your doctor is the same person, but their network status changed with their employer. Always re-verify when a doctor changes locations.</p>

<div class="key-takeaway">
    <strong>Verify everyone, not just your main doctor.</strong> Before any scheduled procedure, ask: &ldquo;Is the facility in-network? Are all the physicians who may be involved &mdash; including anesthesiologists, radiologists, and pathologists &mdash; in-network for my plan?&rdquo; Get the answer in writing when possible.
</div>

<h2 id="specialists-and-ancillary">4. What about specialists, anesthesiologists, and labs during a procedure</h2>

<p>When you have a scheduled surgery or procedure, your main surgeon is only one of several providers who will bill you separately. Each one can have a different network status:</p>

<table>
    <thead>
        <tr><th>Provider Type</th><th>Who They Are</th><th>Risk of Being Out-of-Network</th></tr>
    </thead>
    <tbody>
        <tr><td>Primary surgeon</td><td>The doctor you chose and scheduled with</td><td>Low (you verified this)</td></tr>
        <tr><td>Anesthesiologist</td><td>Administers anesthesia during surgery</td><td><strong>High</strong> &mdash; often independent contractors</td></tr>
        <tr><td>Assistant surgeon</td><td>Assists during complex procedures</td><td><strong>High</strong> &mdash; assigned day-of, rarely disclosed in advance</td></tr>
        <tr><td>Pathologist</td><td>Analyzes tissue samples or biopsies</td><td>Moderate &mdash; contracted separately from the facility</td></tr>
        <tr><td>Radiologist</td><td>Reads imaging (X-rays, CT scans, MRIs)</td><td>Moderate &mdash; often a separate billing group</td></tr>
        <tr><td>Lab/reference lab</td><td>Processes blood work and specimens</td><td><strong>High</strong> &mdash; facility may send samples to an out-of-network lab</td></tr>
    </tbody>
</table>

<p>Before any scheduled procedure, take these steps:</p>

<ol>
    <li><strong>Ask your surgeon&rsquo;s office</strong> for the names of the anesthesiology group, pathology group, and any other providers who will be involved. Verify each one&rsquo;s network status with your insurer.</li>
    <li><strong>Ask the facility</strong> which laboratory they send specimens to. If it&rsquo;s out-of-network, request that your samples be sent to an in-network lab instead.</li>
    <li><strong>Request in writing</strong> that only in-network providers be assigned to your case. While this is not always possible (especially in emergencies), making the request creates a paper trail if a surprise bill arises.</li>
    <li><strong>Know your No Surprises Act protections.</strong> For non-emergency services at an in-network facility, if an out-of-network provider treats you without your advance consent, the <a href="/guides/no-surprises-act-explained">No Surprises Act</a> generally requires that you only pay in-network cost-sharing amounts.</li>
</ol>

<div class="case-study">
    <h3>Case study: surprise anesthesiologist bill after knee surgery</h3>
    <p>A 38-year-old woman in Virginia scheduled knee arthroscopy at an in-network surgery center with an in-network orthopedic surgeon. She verified both the surgeon and the facility before her procedure. Six weeks later, she received a $4,200 bill from the anesthesiologist, who was an independent contractor and out-of-network. Her insurer paid $800 toward the anesthesia charge, leaving her with $3,400. She filed a complaint under the No Surprises Act because the anesthesiologist was assigned to her case at an in-network facility without her choice. The bill was re-processed at in-network rates, and her final responsibility dropped to $350 &mdash; her in-network coinsurance. <strong>Savings: $3,850.</strong></p>
</div>

{_embed(mode="cost", cpt="00740", title="Look up anesthesia and procedure costs", subtitle="Enter the CPT code from your bill to see what Medicare pays.")}

<h2 id="doctor-drops-network">5. What to do if your doctor drops your network mid-treatment</h2>

<p>It happens more often than you think: you&rsquo;re in the middle of treatment for a chronic condition, pregnancy, or post-surgical recovery, and your doctor sends a letter saying they&rsquo;re leaving your insurance network. Suddenly, continuing care with the same doctor means paying out-of-network rates.</p>

<h3>Continuity of care laws</h3>

<p>Most states have continuity of care protections that require insurers to cover ongoing treatment at in-network rates for a transition period after a provider leaves the network. The specifics vary by state, but here&rsquo;s what&rsquo;s typical:</p>

<ul>
    <li><strong>Transition period:</strong> 60&ndash;120 days of continued in-network coverage, depending on the state.</li>
    <li><strong>Qualifying conditions:</strong> Continuity of care protections typically apply to patients who are in an active course of treatment, pregnant (usually through postpartum), terminally ill, scheduled for surgery, or undergoing cancer treatment.</li>
    <li><strong>What you must do:</strong> You usually need to request the continuity of care exception in writing from your insurer within 30 days of receiving notice that your doctor is leaving the network. The doctor must also agree to accept the in-network rate during the transition period.</li>
</ul>

<h3>Steps to take immediately</h3>

<ol>
    <li><strong>Call your insurer</strong> and ask for a &ldquo;continuity of care exception&rdquo; or &ldquo;transition of care exception.&rdquo; Reference your state&rsquo;s continuity of care law if applicable.</li>
    <li><strong>Get the exception in writing</strong> with the specific dates it covers and confirmation that in-network cost-sharing applies.</li>
    <li><strong>Ask your doctor</strong> if they will accept your insurer&rsquo;s in-network rate during the transition period. Most providers will agree to this to retain patients.</li>
    <li><strong>Start searching for an in-network replacement</strong> during the transition period. Ask your current doctor for a referral to an in-network colleague.</li>
</ol>

<div class="key-takeaway">
    <strong>Don&rsquo;t panic if your doctor leaves your network.</strong> You have rights. Contact your insurer immediately to request a continuity of care exception. Most states require insurers to honor in-network rates for 60&ndash;120 days for patients in active treatment. For a full breakdown of how insurance networks function, see our <a href="/guides/how-health-insurance-works">guide to how health insurance works</a>.
</div>

<h2 id="no-surprises-act">6. How the No Surprises Act protects you from surprise out-of-network bills</h2>

<p>The <a href="/guides/no-surprises-act-explained">No Surprises Act</a>, effective January 1, 2022, is the most significant federal protection against unexpected out-of-network bills. Here&rsquo;s what it covers and what it doesn&rsquo;t:</p>

<h3>What the No Surprises Act protects</h3>

<ul>
    <li><strong>Emergency services.</strong> If you go to an emergency room, you cannot be balance billed by out-of-network providers &mdash; including the ER physician, radiologist, and any specialist called in during your emergency. You pay only your in-network cost-sharing amount, regardless of the provider&rsquo;s network status.</li>
    <li><strong>Out-of-network providers at in-network facilities.</strong> If you receive non-emergency care at an in-network hospital or surgery center and an out-of-network provider treats you without your informed consent (e.g., an anesthesiologist or pathologist you didn&rsquo;t choose), the provider cannot balance bill you beyond in-network cost-sharing.</li>
    <li><strong>Air ambulance services.</strong> Out-of-network air ambulance providers cannot balance bill you beyond in-network cost-sharing amounts.</li>
</ul>

<h3>What the No Surprises Act does NOT protect</h3>

<ul>
    <li>Ground ambulance services (a known gap in the law)</li>
    <li>Situations where you knowingly choose an out-of-network provider and sign a written consent to waive your protections</li>
    <li>Post-stabilization care if you consent to out-of-network transfer</li>
    <li>Out-of-network facilities for scheduled, elective procedures</li>
</ul>

<p>If you believe you received a surprise out-of-network bill that should be covered under the No Surprises Act, you can file a complaint with the federal No Surprises Help Desk at 1-800-985-3059 or through <a href="https://www.cms.gov/nosurprises" target="_blank" rel="noopener">cms.gov/nosurprises</a>. For a deeper dive, read our <a href="/guides/no-surprises-act-explained">complete No Surprises Act guide</a>.</p>

<div class="case-study">
    <h3>Case study: emergency room visit with out-of-network ER physician</h3>
    <p>A 52-year-old man in Ohio went to his nearest emergency room &mdash; an in-network hospital &mdash; for chest pain. He was treated by an ER physician, received lab work, and had a CT scan. Two months later, he received a $6,800 bill from the ER physician group, which was out-of-network. His insurer had paid the facility charges at in-network rates but processed the physician&rsquo;s bill at out-of-network rates. He filed a No Surprises Act complaint. The bill was reprocessed: he owed only his $250 ER copay instead of $6,800. <strong>Savings: $6,550.</strong></p>
</div>

<h2 id="accidentally-out-of-network">7. What to do if you accidentally see an out-of-network provider</h2>

<p>If you&rsquo;ve already received care from an out-of-network provider and have a large bill, take these steps:</p>

<p><strong>Step 1 &mdash; Determine if the No Surprises Act applies.</strong> Was the service an emergency? Were you at an in-network facility when an out-of-network provider treated you without your informed consent? If yes, file a complaint and request the bill be reprocessed at in-network rates.</p>

<p><strong>Step 2 &mdash; Call your insurer and request an in-network exception.</strong> Explain the circumstances. If you relied on inaccurate directory information, the insurer may agree to reprocess the claim at in-network rates. Reference the directory listing (this is why you take screenshots). Some states require insurers to honor in-network rates when their own directory listed the provider as in-network at the time of service.</p>

<p><strong>Step 3 &mdash; Negotiate directly with the provider.</strong> Out-of-network providers are often willing to negotiate, especially if the alternative is a lengthy collections process. Ask for a reduction to the Medicare rate or the insurer&rsquo;s allowed amount. Many providers will accept 150&ndash;200% of Medicare as a reasonable rate. Use our <a href="/calculator">calculator</a> to look up the Medicare rate for your service to know your target price.</p>

<p><strong>Step 4 &mdash; File a formal appeal with your insurer.</strong> Submit a written appeal requesting in-network coverage. Include documentation of any directory errors, lack of informed consent, or emergency circumstances. For guidance on writing an effective appeal, see our <a href="/guides/out-of-network-medical-bills">out-of-network bills guide</a>.</p>

<p><strong>Step 5 &mdash; Request an itemized bill.</strong> Before paying anything, request a fully itemized statement with CPT codes and individual charges. Compare each line item against the Medicare rate using our <a href="/calculator">calculator</a>. Out-of-network charges that exceed 300% of the Medicare rate are strong candidates for negotiation.</p>

<p><strong>Step 6 &mdash; <a href="/scan">Upload your bill to BillKarma</a>.</strong> We&rsquo;ll analyze every line item, flag charges that exceed Medicare benchmarks, identify No Surprises Act protections that may apply, and help you build your case for a reduction.</p>

<div class="key-takeaway">
    <strong>Don&rsquo;t pay an out-of-network bill immediately.</strong> You have 30&ndash;90 days before most providers send a bill to collections. Use that time to verify your rights, file appeals, and negotiate. Many out-of-network bills can be reduced by 40&ndash;70% through negotiation or regulatory complaints. Check our <a href="/hospitals/">hospital directory</a> to see if your provider has financial assistance programs that may apply.
</div>

<h2 id="faq">Frequently asked questions</h2>

<div class="faq-section">
    <div class="faq-item">
        <h3>How do I know if my doctor is in-network?</h3>
        <p>The most reliable way is to log into your health insurance company&rsquo;s website or app and search the provider directory for your doctor by name. You can also call the number on the back of your insurance card and ask a representative to confirm your doctor&rsquo;s network status. Always verify within 2&ndash;4 weeks of your appointment because networks change quarterly.</p>
    </div>

    <div class="faq-item">
        <h3>What happens if I accidentally see an out-of-network doctor?</h3>
        <p>If you accidentally see an out-of-network provider, you may owe the full billed amount minus whatever your insurer reimburses at the out-of-network rate, which is typically 50&ndash;70% less than the in-network rate. However, the No Surprises Act protects you from surprise out-of-network bills at in-network facilities for emergency services and certain non-emergency situations where you had no choice of provider. File an appeal with your insurer and request in-network pricing if you were not informed.</p>
    </div>

    <div class="faq-item">
        <h3>Can my doctor drop my insurance mid-treatment?</h3>
        <p>Yes, doctors can leave insurance networks at any time, though most contracts require 60&ndash;90 days&rsquo; notice. If your doctor drops your plan mid-treatment, most states have continuity of care laws that require your insurer to cover ongoing treatment at in-network rates for 60&ndash;120 days. Contact your insurance company immediately to request a continuity of care exception.</p>
    </div>

    <div class="faq-item">
        <h3>Is my doctor in-network if the hospital is in-network?</h3>
        <p>Not necessarily. A hospital can be in-network while individual doctors who practice there &mdash; including anesthesiologists, radiologists, pathologists, and assistant surgeons &mdash; may be out-of-network. This is one of the most common sources of surprise medical bills. The No Surprises Act now protects patients from surprise bills from out-of-network providers at in-network facilities in many situations.</p>
    </div>

    <div class="faq-item">
        <h3>How often do provider networks change?</h3>
        <p>Insurance networks can change quarterly. Doctors join and leave networks throughout the year based on contract negotiations. A directory listing from six months ago may be outdated. Always verify network status within two to four weeks of your scheduled appointment, and ask for written confirmation with an effective date range.</p>
    </div>

    <div class="faq-item">
        <h3>Does the No Surprises Act protect me from all out-of-network bills?</h3>
        <p>No. The No Surprises Act protects you from surprise out-of-network bills for emergency services, air ambulance services, and non-emergency services at in-network facilities where you did not choose the out-of-network provider. It does not protect you if you knowingly choose an out-of-network provider, visit an out-of-network facility for a scheduled procedure, or receive ground ambulance services.</p>
    </div>
</div>

<h2 id="sources">Sources</h2>

<ul class="sources-list">
    <li><a href="https://www.cms.gov/nosurprises" target="_blank" rel="noopener">CMS &mdash; No Surprises Act: Overview, Protections, and Complaint Process</a></li>
    <li><a href="https://www.kff.org/health-costs/issue-brief/surprise-medical-bills/" target="_blank" rel="noopener">Kaiser Family Foundation &mdash; Surprise Medical Bills: Prevalence and Impact on Consumers</a></li>
    <li><a href="https://www.commonwealthfund.org/publications/issue-briefs/2023/provider-directory-accuracy" target="_blank" rel="noopener">Commonwealth Fund &mdash; Provider Directory Accuracy and Its Impact on Out-of-Network Billing</a></li>
    <li><a href="https://www.cms.gov/cciio/resources/regulations-and-guidance/continuity-of-care" target="_blank" rel="noopener">CMS &mdash; Continuity of Care and Network Adequacy Requirements</a></li>
    <li><a href="https://www.healthaffairs.org/doi/10.1377/hlthaff.2022.01541" target="_blank" rel="noopener">Health Affairs &mdash; The No Surprises Act: Early Implementation and Consumer Impact</a></li>
    <li><a href="https://www.naic.org/cipr-topics/topic-network-adequacy.htm" target="_blank" rel="noopener">National Association of Insurance Commissioners &mdash; Network Adequacy and Provider Directory Standards</a></li>
</ul>
""",
})
