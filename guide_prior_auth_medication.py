"""Guide: Prior Authorization for Medication."""

from guides import register, _embed

register("prior-authorization-for-medication", {
    "title": "Prior Authorization for Medication: How to Get Approved (2026)",
    "meta_description": "Learn how prior authorization for medication works, which drugs require PA, what to do when denied, and how new 2026 CMS rules limit Medicare Advantage delays.",
    "published": "2026-04-05",
    "author": "BillKarma Team",
    "category": "Prior Authorization",
    "faqs": [
        {
            "q": "How long does prior authorization take for a medication?",
            "a": "For non-urgent medications, prior authorization typically takes 3 to 10 business days after your doctor submits all required documentation. For urgent requests, the timeline is 24 to 72 hours. Starting in 2026, new CMS rules require Medicare Advantage plans to decide urgent PA requests within 24 hours and standard requests within 72 hours. Many commercial insurers are also tightening turnaround times under state laws.",
        },
        {
            "q": "What happens if my insurance denies prior authorization for my medication?",
            "a": "You have several options: (1) appeal the denial — 33% of PA denials are overturned on appeal; (2) ask your doctor to request a peer-to-peer review with the insurer's medical director; (3) file an exception request if you've tried step therapy drugs and they failed; (4) contact the drug manufacturer's patient assistance program, which may provide the medication free or at reduced cost while the appeal is pending; (5) check if a therapeutic alternative covered by your plan is clinically appropriate.",
        },
        {
            "q": "What is step therapy and can I skip it?",
            "a": "Step therapy (also called 'fail first') requires you to try and fail a cheaper drug before the insurer will cover a more expensive one. You can request a step therapy exception if: you previously tried the required drug and it failed; the required drug is contraindicated for your condition; the required drug would cause a clinically significant adverse reaction; or immediate access is medically necessary. Most states require insurers to have a step therapy exception process. Document your medical history carefully.",
        },
        {
            "q": "What is gold carding for prior authorization?",
            "a": "Gold carding is a policy that exempts prescribers from prior authorization requirements when they have a high historical approval rate (typically 90%+) for specific drug classes. A gold-carded physician can prescribe covered medications without submitting a PA request. Texas, Louisiana, Arkansas, and several other states have enacted gold carding laws. CMS is developing a gold carding framework for Medicare Advantage. If your doctor is frequently prescribing a drug that requires PA, it's worth asking whether they qualify for exemption.",
        },
        {
            "q": "Can I get my medication while the prior authorization is being reviewed?",
            "a": "Yes, in some situations. Your pharmacist can dispense an emergency supply (typically 30 days) for maintenance medications in many states. Your doctor can submit the PA request while you receive a bridge supply. Manufacturer patient assistance programs can often provide medications quickly for financial hardship cases. Some states require plans to cover a temporary supply of a drug when a formulary change removes a drug a patient is already taking.",
        },
    ],
    "body": f"""
<p class="lead">Prior authorization for medication is one of the biggest sources of treatment delay in U.S. healthcare. Physicians report spending an average of 14 hours per week on PA paperwork. Patients face an average delay of <strong>6.4 days</strong> to access approved medications&mdash;and <strong>33% of PA denials are overturned on appeal</strong>, meaning a third of initial denials were wrong. Here is how to navigate the process and get your medication approved.</p>

<div class="answer-box" style="background:#e8f5e9;border-left:4px solid #2e7d32;padding:1.25rem 1.5rem;margin:1.5rem 0;border-radius:4px;">
    <strong>Direct answer:</strong> Prior authorization requires your doctor to get insurer approval before your plan will cover a medication. If denied, appeal immediately&mdash;one-third of denials are overturned. Your doctor can also request a peer-to-peer review, which resolves many denials quickly. For ongoing issues, check if your prescriber qualifies for gold card exemption or whether a manufacturer patient assistance program can bridge coverage during disputes.
</div>

<nav class="toc">
    <h2>In this guide</h2>
    <ol>
        <li><a href="#which-drugs">Which drugs typically require prior authorization</a></li>
        <li><a href="#step-therapy">Step therapy: the &ldquo;fail first&rdquo; requirement</a></li>
        <li><a href="#how-to-submit">How to get your doctor to submit a PA request</a></li>
        <li><a href="#timelines">PA timelines and the new 2026 CMS rules</a></li>
        <li><a href="#denied">What to do if PA is denied</a></li>
        <li><a href="#gold-carding">Gold carding: exemptions for high-approval prescribers</a></li>
        <li><a href="#paying-oop">Cost of going without PA vs. paying out of pocket</a></li>
        <li><a href="#faq">Frequently asked questions</a></li>
        <li><a href="#sources">Sources</a></li>
    </ol>
</nav>

<h2 id="which-drugs">1. Which drugs typically require prior authorization</h2>

<p>Not every prescription requires PA. Insurers and pharmacy benefit managers (PBMs) apply PA requirements selectively to control costs for high-utilization or high-cost drugs. The most common categories:</p>

<table>
    <thead>
        <tr><th>Drug Category</th><th>Examples</th><th>Why PA Is Required</th></tr>
    </thead>
    <tbody>
        <tr><td><strong>GLP-1 receptor agonists</strong></td><td>Ozempic, Wegovy, Mounjaro, Zepbound</td><td>High cost; insurer wants to confirm diabetes or obesity diagnosis criteria met</td></tr>
        <tr><td><strong>Biologics and biosimilars</strong></td><td>Humira, Enbrel, Dupixent, Keytruda</td><td>Very high cost ($20,000&ndash;$500,000/year); insurer verifies diagnosis and failed alternatives</td></tr>
        <tr><td><strong>Specialty drugs</strong></td><td>Stelara, Skyrizi, Rinvoq, Ocrevus</td><td>High cost; limited prescribers; complex administration requirements</td></tr>
        <tr><td><strong>ADHD medications</strong></td><td>Adderall, Vyvanse, Concerta, Strattera</td><td>Controlled substances with abuse potential; insurer verifies diagnosis</td></tr>
        <tr><td><strong>Sleep medications</strong></td><td>Quviviq, Belsomra, Dayvigo</td><td>Brand-only coverage; generic alternatives available</td></tr>
        <tr><td><strong>Brand when generic available</strong></td><td>Any brand drug with an AB-rated generic</td><td>Cost control; insurer covers generic automatically, brand requires justification</td></tr>
        <tr><td><strong>Antipsychotics / mood stabilizers</strong></td><td>Abilify Maintena, Invega Sustenna</td><td>High cost injectables; diagnosis verification</td></tr>
    </tbody>
</table>

<p>Your specific plan&rsquo;s formulary determines which drugs require PA. Find this information in your plan&rsquo;s drug list (formulary), available on your insurer&rsquo;s website. Look for &ldquo;PA&rdquo; or &ldquo;ST&rdquo; (step therapy) next to specific drugs.</p>

<h2 id="step-therapy">2. Step therapy: the &ldquo;fail first&rdquo; requirement</h2>

<p>Step therapy requires you to try a less expensive drug before your insurer will cover the one your doctor prescribed. For example, before covering a biologic like Humira for rheumatoid arthritis, a plan may require you to try and fail methotrexate and at least one other conventional DMARD.</p>

<p><strong>You can request a step therapy exception if any of these apply:</strong></p>

<ul>
    <li>You previously tried the required step therapy drug and it was ineffective or caused an adverse reaction&mdash;document this with medical records</li>
    <li>The required drug is contraindicated for your condition (e.g., a kidney disease patient cannot safely take NSAIDs required in the step protocol)</li>
    <li>You are already clinically stable on the prescribed medication and switching would cause harm</li>
    <li>The required drug is not available due to a shortage</li>
    <li>A clinician determines that trying the required drug would cause irreversible harm</li>
</ul>

<p>As of 2026, more than 30 states have enacted step therapy exception laws that require insurers to have a clear exception process and respond within defined timelines. Check whether your state has such a law and cite it explicitly in your exception request.</p>

<h2 id="how-to-submit">3. How to get your doctor to submit a PA request</h2>

<p>The PA process begins with your prescribing doctor, not with you. Here is how to move it forward quickly:</p>

<ol>
    <li><strong>Ask your doctor at the appointment.</strong> Before leaving, confirm whether the prescription will require PA. Many EMR systems flag this automatically at the point of prescribing.</li>
    <li><strong>Make sure the PA request is submitted promptly.</strong> PA is submitted by your doctor&rsquo;s office, not by you. Ask specifically who in the office handles PA submissions and confirm it will be submitted within 24 hours.</li>
    <li><strong>Provide complete documentation proactively.</strong> The most common cause of PA delay is missing documentation. Relevant documentation includes: current diagnosis codes, supporting lab results or imaging, a list of prior medications tried and their outcomes, and the specific clinical indication for the requested drug.</li>
    <li><strong>Ask your doctor to call the insurer&rsquo;s medical director directly (peer-to-peer review)</strong> if the PA is delayed or denied. This single step resolves a large proportion of denials before formal appeals are necessary.</li>
    <li><strong>Check the status.</strong> Call your insurance company 2 business days after submission to confirm the PA request was received and is being processed. Get a reference number.</li>
</ol>

<h2 id="timelines">4. PA timelines and the new 2026 CMS rules</h2>

<p>PA decision timelines vary by plan type and urgency:</p>

<ul>
    <li><strong>Urgent / expedited requests:</strong> 24&ndash;72 hours (federal minimum for marketplace and Medicare Advantage plans)</li>
    <li><strong>Non-urgent (standard) requests:</strong> 3&ndash;10 business days for most commercial plans; 72 hours for Medicare Advantage under 2026 CMS rules</li>
    <li><strong>Appeals after denial:</strong> 30&ndash;60 days for standard appeal; 72 hours for expedited</li>
</ul>

<p><strong>New CMS Prior Authorization rules effective 2026:</strong> CMS finalized a rule in 2024 requiring Medicare Advantage plans and Medicaid managed care plans to:</p>

<ul>
    <li>Respond to urgent PA requests within <strong>24 hours</strong> (reduced from 72 hours)</li>
    <li>Respond to standard PA requests within <strong>72 hours</strong> (reduced from 7 days)</li>
    <li>Share PA data through standardized FHIR APIs, making it easier for patients and providers to track PA status electronically</li>
    <li>Provide specific reasons for PA denials and cite the clinical criteria used</li>
    <li>Limit PA requirements to evidence-based clinical criteria only</li>
</ul>

<p>These rules apply to Medicare Advantage plans, Medicaid managed care plans, and marketplace QHP issuers. Commercial employer-sponsored plans are not covered by this rule but many states have enacted similar requirements.</p>

<h2 id="denied">5. What to do if PA is denied</h2>

<p>A PA denial is not final. Here are your options in order of how quickly they typically resolve:</p>

<ol>
    <li>
        <strong>Peer-to-peer review (fastest).</strong> Your doctor calls the insurer&rsquo;s medical director. This is a physician-to-physician conversation about your specific case. Many denials reverse at this stage within 1&ndash;2 days. Ask your doctor to request this immediately.
    </li>
    <li>
        <strong>Formal appeal.</strong> Submit a written appeal with a letter of medical necessity, clinical guidelines supporting the drug&rsquo;s use for your condition, and documentation of any failed alternatives. A BillKarma analysis found <strong>33% of PA denials are overturned on appeal</strong>.
    </li>
    <li>
        <strong>Exception request.</strong> If denied for step therapy reasons, submit a step therapy exception request with documentation of why the required alternatives are inappropriate for you.
    </li>
    <li>
        <strong>External review.</strong> If your internal appeal is denied, request external review by an independent organization. The IRO&rsquo;s decision is binding on the insurer.
    </li>
    <li>
        <strong>Manufacturer patient assistance programs (PAPs).</strong> Most major pharmaceutical manufacturers offer programs that provide medications free or at dramatically reduced cost to patients who meet income criteria or who are fighting coverage denials. Apply at the manufacturer&rsquo;s website or through NeedyMeds.org or RxAssist.org while your appeal is pending.
    </li>
    <li>
        <strong>State insurance commissioner complaint.</strong> If the insurer violated required timelines or failed to provide adequate denial reasons, file a complaint with your state&rsquo;s insurance commissioner.
    </li>
</ol>

<div class="key-takeaway">
    <strong>Don&rsquo;t wait to start the appeal.</strong> PA approval timelines and appeal timelines both count as days you&rsquo;re without medication. Submit your appeal on day 1 of a denial. Apply for manufacturer assistance simultaneously. Your doctor&rsquo;s peer-to-peer review request can happen in parallel. These are not sequential steps&mdash;run them concurrently.
</div>

<h2 id="gold-carding">6. Gold carding: exemptions for high-approval prescribers</h2>

<p>Gold carding exempts a prescriber from prior authorization requirements for specific drug classes based on their historical approval rate. If a doctor&rsquo;s PA requests for a drug class are approved 90%+ of the time, requiring PA for that physician wastes everyone&rsquo;s time.</p>

<p><strong>States with gold carding laws (as of 2026):</strong></p>

<ul>
    <li><strong>Texas</strong> &mdash; requires health plans to exempt physicians with a 90%+ approval rate from PA requirements for specific services or drugs</li>
    <li><strong>Louisiana</strong> &mdash; 90% approval rate threshold; applies to Medicaid managed care and commercial plans</li>
    <li><strong>Arkansas, West Virginia, Virginia</strong> &mdash; enacted gold carding laws requiring insurer compliance</li>
    <li><strong>CMS</strong> &mdash; developing a gold carding framework for Medicare Advantage plans; expected finalization in 2026</li>
</ul>

<p>If your prescribing doctor frequently prescribes a drug that requires PA, ask their office whether they have applied for or qualify for gold card status with your specific insurer. If not, encourage them to&mdash;it removes the PA burden for all of their patients on that drug.</p>

<h2 id="paying-oop">7. Cost of going without PA vs. paying out of pocket</h2>

<p>Sometimes patients consider skipping the PA process and paying out of pocket. This almost never makes financial sense for specialty medications, but for some lower-cost drugs it may be worth comparing:</p>

<ul>
    <li><strong>GoodRx / discount pharmacies:</strong> For generic medications and some brands, GoodRx or Cost Plus Drugs prices may be lower than your plan&rsquo;s cost-sharing even with coverage. Check before filing a PA.</li>
    <li><strong>Specialty drugs:</strong> Almost never cheaper out of pocket. Biologics that cost $20,000&ndash;$100,000+/year have $0 list price programs through manufacturers for qualifying patients, but these are separate from PA processes.</li>
    <li><strong>GLP-1 medications:</strong> Without insurance coverage, Wegovy lists at approximately $1,350/month; Ozempic at $1,000/month. Manufacturer savings cards may reduce this to $25/month for eligible commercially insured patients during disputes.</li>
    <li><strong>The real cost of waiting:</strong> For conditions like cancer, autoimmune disease, or severe mental illness, treatment delay has clinical consequences. Pursue all appeal options aggressively and simultaneously.</li>
</ul>

<div class="cta-box" style="background:#f3f4f6;border:2px solid #4f46e5;padding:1.5rem;margin:2rem 0;border-radius:6px;text-align:center;">
    <strong style="font-size:1.1rem;">PA denied for your medication?</strong>
    <p style="margin:.75rem 0;">BillKarma can generate a customized PA appeal letter based on your denial reason and drug type&mdash;and help you find manufacturer assistance programs while you wait.</p>
    <a href="/fight-debt" style="background:#4f46e5;color:#fff;padding:.75rem 1.5rem;border-radius:4px;text-decoration:none;font-weight:600;">Appeal My PA Denial &rarr;</a>
</div>

<h2 id="faq">Frequently asked questions</h2>

<div class="faq-section">
    <div class="faq-item">
        <h3>How long does prior authorization take for a medication?</h3>
        <p>Standard requests: 3&ndash;10 business days. Urgent requests: 24&ndash;72 hours. Under new 2026 CMS rules, Medicare Advantage plans must decide urgent PA requests within 24 hours and standard requests within 72 hours.</p>
    </div>

    <div class="faq-item">
        <h3>What happens if my insurance denies prior authorization for my medication?</h3>
        <p>Appeal immediately&mdash;33% of PA denials are overturned. Your doctor can request a peer-to-peer review with the insurer&rsquo;s medical director. File a step therapy exception if applicable. Contact the manufacturer&rsquo;s patient assistance program for bridge coverage while appealing.</p>
    </div>

    <div class="faq-item">
        <h3>What is step therapy and can I skip it?</h3>
        <p>Step therapy requires you to try a cheaper drug before your insurer covers a more expensive one. You can request an exception if you previously tried and failed the required drug, if it is contraindicated, or if switching would cause clinical harm. Document your medical history carefully and reference your state&rsquo;s step therapy exception law.</p>
    </div>

    <div class="faq-item">
        <h3>What is gold carding for prior authorization?</h3>
        <p>Gold carding exempts prescribers with a 90%+ historical PA approval rate from having to submit PA requests for specific drug classes. Texas, Louisiana, and several other states have enacted gold carding laws. CMS is developing a gold carding framework for Medicare Advantage.</p>
    </div>

    <div class="faq-item">
        <h3>Can I get my medication while the prior authorization is being reviewed?</h3>
        <p>In many states, pharmacists can dispense an emergency 30-day supply for maintenance medications. Your doctor can provide samples. Manufacturer patient assistance programs can often provide medications quickly. Ask your pharmacist and doctor&rsquo;s office about bridge options on the day of denial.</p>
    </div>
</div>

<h2 id="sources">Sources</h2>

<ul class="sources-list">
    <li><a href="#" target="_blank" rel="noopener">CMS: Advancing Interoperability and Improving Prior Authorization Processes Final Rule (2024)</a></li>
    <li><a href="#" target="_blank" rel="noopener">AMA: 2025 AMA Prior Authorization Physician Survey</a></li>
    <li><a href="#" target="_blank" rel="noopener">KFF: Prior Authorization in Medicare Advantage (2024)</a></li>
    <li><a href="#" target="_blank" rel="noopener">National Academy for State Health Policy: State Prior Authorization and Step Therapy Laws (2025)</a></li>
    <li><a href="#" target="_blank" rel="noopener">CMS: Medicare Advantage Prior Authorization Compliance Data (2025)</a></li>
</ul>
""",
})
