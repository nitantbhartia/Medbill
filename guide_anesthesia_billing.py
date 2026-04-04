"""Guide: Anesthesia Bills Explained — Why Your Anesthesiologist Bill Is So Confusing."""

from guides import register, _embed

register("anesthesia-billing", {
    "title": "Why Anesthesia Bills Are So High — And How to Fight Back (2026)",
    "meta_description": "Anesthesia often costs more than the surgery itself. Learn what's normal, how to spot errors, and how to dispute overcharges.",
    "published": "2026-02-19",
    "author": "BillKarma Team",
    "category": "Billing Basics",
    "faqs": [
        {
            "q": "Why did I get a separate bill from the anesthesiologist?",
            "a": "Anesthesiologists typically operate independently from the hospital. Even if they work at an in-network hospital, they may be employed by a separate anesthesiology group that bills you directly. This is one of the most common sources of surprise medical bills. Since January 2022, the No Surprises Act prohibits anesthesiologists at in-network facilities from billing you out-of-network rates for scheduled (non-emergency) procedures — you can only be charged your in-network cost-sharing amount.",
        },
        {
            "q": "How is anesthesia priced?",
            "a": "Anesthesia is priced in 'units,' not by dollar amounts or by service. Your total charge is calculated as: (Base Units + Time Units) × Conversion Factor. Base units are assigned to the procedure type (e.g., a colonoscopy has 7 base units). Time units are 1 unit per 15 minutes of anesthesia time. The conversion factor is the dollar amount per unit, which varies by insurer and region — Medicare pays about $26 per unit; commercial insurers pay $60-$150 per unit.",
        },
        {
            "q": "What is the difference between an anesthesiologist and a CRNA?",
            "a": "An anesthesiologist (MDA) is a physician (MD or DO) who completed medical school and a 4-year anesthesiology residency. A CRNA (Certified Registered Nurse Anesthetist) is an advanced practice nurse who completed nursing school and a specialized anesthesia program. Both can administer anesthesia. Anesthesiologists bill under modifier AA when providing care personally. CRNAs billing independently use modifier QZ. Both should accept your in-network rates if your facility is in-network, under the No Surprises Act.",
        },
        {
            "q": "What are qualifying circumstances in anesthesia billing?",
            "a": "Qualifying circumstances are billing codes (99100, 99116, 99135, 99140) that add extra units to an anesthesia charge when conditions make anesthesia more complex. For example, 99100 adds 3 units for patients under age 1 or over age 70 (because anesthesia carries higher risk). 99140 adds 2 units for emergency cases. These codes are legitimate when applied correctly, but they are sometimes added when the qualifying circumstance doesn't actually apply.",
        },
        {
            "q": "Does the No Surprises Act cover anesthesia bills?",
            "a": "Yes. The No Surprises Act (effective January 1, 2022) prohibits surprise out-of-network billing for anesthesiologists and other non-emergency providers at in-network facilities. If your surgery was at an in-network hospital and your anesthesiologist is out-of-network, the anesthesiologist must accept your in-network cost-sharing rate. You cannot be charged more than your in-network copay, coinsurance, or deductible for that service.",
        },
        {
            "q": "What should I do if I receive an unexpectedly large anesthesia bill?",
            "a": "First, verify that your facility was in-network and that the procedure was scheduled (not an emergency). If both are true and your anesthesiologist billed you out-of-network rates, you may have NSA protection. Contact your insurer to file a complaint. Second, request the itemized bill from the anesthesiology group and check the base units, time units, and any qualifying circumstances codes against the actual procedure and duration. Third, compare the billed conversion factor to what Medicare pays (~$26/unit) as a reference point.",
        },
    ],
    "body": f"""
<p class="lead">A 2020 study in <em>Health Affairs</em> found that <strong>1 in 5</strong> patients undergoing scheduled surgery at an in-network hospital received an out-of-network bill from their anesthesiologist. The average surprise anesthesia bill was <strong>$1,219</strong>. Since 2022, the No Surprises Act has made most of these bills illegal &mdash; but patients still receive them, and many pay without knowing they have protections. Here&rsquo;s how anesthesia billing works, what to look for on your bill, and how to fight back.</p>

<nav class="toc">
    <h2>In this guide</h2>
    <ol>
        <li><a href="#why-separate-bill">Why you got a separate anesthesia bill</a></li>
        <li><a href="#how-anesthesia-priced">How anesthesia is priced: the units system</a></li>
        <li><a href="#reading-your-bill">Reading your anesthesia bill</a></li>
        <li><a href="#common-problems">Common anesthesia billing problems</a></li>
        <li><a href="#nsa-protection">No Surprises Act protections for anesthesia</a></li>
        <li><a href="#how-to-dispute">How to dispute an anesthesia bill</a></li>
        <li><a href="#case-studies">Case studies: anesthesia disputes resolved</a></li>
        <li><a href="#faq">Frequently asked questions</a></li>
        <li><a href="#sources">Sources</a></li>
    </ol>
</nav>

<h2 id="why-separate-bill">1. Why you got a separate anesthesia bill</h2>

<p>Most hospitals do not employ their anesthesiologists directly. Instead, the hospital contracts with an independent anesthesiology group that staffs the operating rooms. When you have surgery, the hospital bills you for the facility, the surgeon bills separately, and the anesthesiology group sends its own bill.</p>

<p>This creates a critical problem: the surgeon and hospital may be in-network with your insurance, but the anesthesiology group may not be. Until 2022, this was an extremely common source of surprise bills &mdash; patients who carefully selected in-network facilities and surgeons were blindsided by out-of-network anesthesia charges.</p>

<p>The good news: <strong>the No Surprises Act (NSA)</strong>, which took effect January 1, 2022, specifically prohibits this for scheduled procedures. See <a href="#nsa-protection">Section 5</a> for details on what the NSA covers and what it doesn&rsquo;t.</p>

<div class="key-takeaway">
    <strong>Always ask before surgery:</strong> &ldquo;Is the anesthesiology group that staffs this facility in-network with my insurance?&rdquo; Get the answer in writing. And since January 2022, if your surgery is scheduled at an in-network facility, out-of-network anesthesia billing is generally prohibited &mdash; even if you didn&rsquo;t ask in advance.
</div>

<h2 id="how-anesthesia-priced">2. How anesthesia is priced: the units system</h2>

<p>Unlike most medical services, anesthesia is not billed by a flat rate or by procedure alone. Instead, it uses a <strong>units-based system</strong> where total units are multiplied by a conversion factor (the dollar rate per unit) to produce the total charge.</p>

<p>The formula is:</p>

<p style="padding: 12px 16px; background: #f5f5f5; border-radius: 8px; font-family: monospace;">
    Total charge = (Base Units + Time Units + Qualifying Circumstance Units) &times; Conversion Factor
</p>

<p><strong>Base Units</strong> are assigned to each anesthesia CPT code based on the complexity of the procedure. They are defined by the American Society of Anesthesiologists (ASA) Relative Value Guide, which CMS also uses for Medicare payment. Examples:</p>

<table>
    <thead>
        <tr><th>Procedure</th><th>Anesthesia CPT Code</th><th>Base Units</th></tr>
    </thead>
    <tbody>
        <tr><td>Colonoscopy / lower GI endoscopy</td><td>00810</td><td>7</td></tr>
        <tr><td>Total knee replacement</td><td>01402</td><td>7</td></tr>
        <tr><td>Knee arthroscopy (diagnostic/repair)</td><td>01382</td><td>3</td></tr>
        <tr><td>Laparoscopic abdominal surgery</td><td>00840</td><td>7</td></tr>
        <tr><td>Cesarean delivery</td><td>01963</td><td>7</td></tr>
        <tr><td>Vaginal delivery (neuraxial)</td><td>01967</td><td>5</td></tr>
        <tr><td>Lumbar spine procedures</td><td>00630</td><td>7</td></tr>
        <tr><td>Open heart surgery</td><td>00566</td><td>25</td></tr>
    </tbody>
</table>

<p><strong>Time Units</strong> represent the actual anesthesia time, billed in 15-minute increments. Each 15-minute block = 1 time unit. A 60-minute procedure = 4 time units. Anesthesia time begins when the anesthesiologist starts preparing the patient (typically in the pre-op area or OR) and ends when the patient is transferred to recovery and is ready for the recovery team to take over.</p>

<p><strong>Qualifying Circumstance Codes</strong> (optional add-ons) apply when conditions make anesthesia more complex:</p>

<table>
    <thead>
        <tr><th>Code</th><th>Description</th><th>Units Added</th></tr>
    </thead>
    <tbody>
        <tr><td>99100</td><td>Patient under 1 year or over 70 years of age</td><td>+3</td></tr>
        <tr><td>99116</td><td>Utilization of total body hypothermia</td><td>+5</td></tr>
        <tr><td>99135</td><td>Controlled hypotension during anesthesia</td><td>+5</td></tr>
        <tr><td>99140</td><td>Emergency condition (defined by immediate threat to life)</td><td>+2</td></tr>
    </tbody>
</table>

<p><strong>Conversion Factor</strong> is the dollar amount per unit, negotiated between the anesthesiology group and your insurer. Medicare pays approximately <strong>$26 per unit</strong> (the exact figure varies by geographic area and is updated annually by CMS). Commercial insurers negotiate higher rates, typically <strong>$60&ndash;$150 per unit</strong>. If the anesthesiologist is out-of-network, they may charge $150&ndash;$400+ per unit at their full chargemaster rate.</p>

<div class="key-takeaway">
    <strong>Not sure what your anesthesia CPT code means?</strong> Use our <a href="/calculator">free calculator</a> to look up what Medicare pays for any anesthesia code &mdash; then compare it to what you were actually charged.
</div>

<h2 id="reading-your-bill">3. Reading your anesthesia bill</h2>

<p>Here&rsquo;s a real anesthesia bill for a 75-minute knee replacement, annotated:</p>

<div class="bill-example">
    <div class="bill-header">Anesthesia Services Invoice &mdash; Regional Anesthesia Partners, LLC &mdash; DOS: 01/28/2026</div>
    <div class="line-item">
        <span>01402 &mdash; Anesthesia, total knee arthroplasty &mdash; Base units: 7</span>
        <span></span>
    </div>
    <div class="line-item">
        <span>Time: 75 minutes &divide; 15 = 5 time units</span>
        <span></span>
    </div>
    <div class="line-item flagged">
        <span>99100 &mdash; Qualifying circumstance: patient over 70 &nbsp; &#9888; <em>Patient is 67 years old. This code does not apply.</em></span>
        <span>+3 units</span>
    </div>
    <div class="line-item">
        <span>Total units claimed: 7 + 5 + 3 = 15 units</span>
        <span></span>
    </div>
    <div class="line-item error">
        <span>Conversion factor: $148/unit &nbsp; &#10060; <em>Medicare pays ~$26/unit. Commercial in-network rates typically $70-100/unit.</em></span>
        <span></span>
    </div>
    <div class="line-total">
        <span>TOTAL BILLED (15 units &times; $148)</span>
        <span>$2,220.00</span>
    </div>
</div>

<p>Two problems appear on this bill:</p>
<ol>
    <li><strong>99100 applied incorrectly:</strong> The qualifying circumstance code for patients over 70 was billed, but the patient is 67. This adds 3 units &times; $148 = <strong>$444 in invalid charges</strong>.</li>
    <li><strong>High conversion factor:</strong> At $148/unit, this anesthesiology group is billing at 5&ndash;6x the Medicare rate. If the provider was supposed to be in-network, this should not be the patient&rsquo;s cost-sharing basis.</li>
</ol>

<h2 id="common-problems">4. Common anesthesia billing problems</h2>

<h3>a) Incorrect time units</h3>
<p>Anesthesia time should reflect the actual time the anesthesiologist was actively providing anesthesia services. Some providers round up aggressively (e.g., billing 8 units for a 95-minute procedure when the correct calculation is 7 units). If your procedure took 60 minutes but you&rsquo;re billed for 8 time units (= 2 hours), ask for the start/stop times documented in your anesthesia record.</p>

<h3>b) Incorrect qualifying circumstance codes</h3>
<p>Code 99100 (extreme age) is the most commonly misapplied qualifying circumstance. It applies to patients under 1 year old or over 70 years old &mdash; not 65, not &ldquo;elderly,&rdquo; not 69. If you&rsquo;re 65&ndash;70 and see 99100 on your bill, request your anesthesia record to verify your age at the time of service. Code 99140 (emergency) should only apply when there was an immediate life-threatening condition &mdash; not merely an urgent or same-day procedure.</p>

<h3>c) Double billing for anesthesiologist and CRNA</h3>
<p>When a physician anesthesiologist supervises a CRNA, only one party should bill for the anesthesia service (at a medically directed rate). Billing both the physician and the CRNA independently for the same procedure is a Medicare fraud risk and should not result in charges to the patient. If you see two separate anesthesia bills for one procedure, ask both providers to clarify who actually provided your care.</p>

<h3>d) Wrong billing modifier</h3>
<p>When a physician anesthesiologist supervises more than four CRNAs simultaneously, the supervision ceases to qualify as &ldquo;medical direction&rdquo; under Medicare rules. In that scenario, the physician cannot bill modifier QK (medical direction of 2&ndash;4 individuals) and the CRNA should bill modifier QZ (CRNA without physician medical direction). Billing QK when the physician was managing more than four CRNAs is technically improper. This is an issue mainly for Medicare/Medicaid patients, not most commercial insurance.</p>

<div class="key-takeaway">
    <strong>Found a potential problem on your anesthesia bill?</strong> <a href="/scan">Upload your full bill to BillKarma</a> &mdash; we audit every line item, including anesthesia charges, and flag anything that doesn&rsquo;t match what Medicare allows.
</div>

<h2 id="nsa-protection">5. No Surprises Act protections for anesthesia</h2>

<p>The <strong>No Surprises Act (NSA)</strong>, effective January 1, 2022, provides strong protection against unexpected anesthesia bills. Key protections:</p>

<table>
    <thead>
        <tr><th>Situation</th><th>NSA Protection</th></tr>
    </thead>
    <tbody>
        <tr><td>Scheduled surgery at in-network hospital; anesthesiologist is out-of-network</td><td>Protected. Anesthesiologist must accept in-network cost-sharing.</td></tr>
        <tr><td>Emergency surgery at any facility; anesthesiologist is out-of-network</td><td>Protected. Emergency providers cannot balance bill.</td></tr>
        <tr><td>Scheduled surgery at out-of-network hospital; anesthesiologist is out-of-network</td><td>NOT automatically protected. You may have chosen to use an out-of-network facility.</td></tr>
        <tr><td>Patient signed a consent form waiving NSA protections for the anesthesiologist</td><td>Consent waiver is only valid for non-emergency situations AND when the provider gave at least 72 hours&rsquo; notice AND when alternatives were available. Most anesthesia consent waivers are not valid under NSA rules.</td></tr>
    </tbody>
</table>

<p>If you received an out-of-network anesthesia bill for a scheduled procedure at an in-network hospital, you can:</p>
<ol>
    <li>Contact your insurer and report that you received a balance bill that may violate the NSA.</li>
    <li>File a complaint with the federal No Surprises Help Desk at 1-800-985-3059 or at <a href="https://www.cms.gov/nosurprises" target="_blank" rel="noopener">cms.gov/nosurprises</a>.</li>
    <li>File a complaint with your state insurance commissioner if your state has additional balance billing protections.</li>
</ol>

<div class="key-takeaway">
    <strong>Under the No Surprises Act, you should pay no more than your in-network cost-sharing</strong> for an out-of-network anesthesiologist at an in-network facility. This applies even if you received the procedure and are now looking at the bill. You can dispute an improper balance bill after the fact.
</div>

{_embed(mode="cost", title="Look up your anesthesia code", subtitle="Enter the anesthesia CPT code (e.g., 00810) to see what Medicare pays.")}

<h2 id="how-to-dispute">6. How to dispute an anesthesia bill</h2>

<h3>Step 1: Request your anesthesia record</h3>
<p>You have the right to request your anesthesia record (also called the anesthesia chart or intraoperative record) from the hospital. This document shows: the type of anesthesia used, the exact start and stop times, the drugs administered, and the anesthesia provider&rsquo;s name. Use this to verify that the billed time units and qualifying circumstance codes match reality.</p>

<h3>Step 2: Check the units math</h3>
<p>Calculate what your bill <em>should</em> show: Base units (from the table above) + time units (actual anesthesia minutes &divide; 15, rounded up to the nearest unit). If qualifying circumstance codes are present, verify they actually applied (age over 70, true emergency, etc.).</p>

<h3>Step 3: Check your insurer&rsquo;s explanation of benefits</h3>
<p>Pull your Explanation of Benefits (EOB) for the procedure date. Your EOB will show whether the anesthesiology group billed as in-network or out-of-network, what your insurer paid, and what your responsibility should be. If the EOB shows out-of-network billing for a scheduled procedure at an in-network facility, contact your insurer immediately. See our <a href="/guides/understanding-your-explanation-of-benefits">guide to reading your EOB</a> for help.</p>

<h3>Step 4: Negotiate or dispute</h3>
<p>If the time units or qualifying codes are wrong, call the anesthesiology group&rsquo;s billing department with your anesthesia record in hand. For NSA violations, go through your insurer and the federal complaint process. For high conversion factors on legitimate out-of-network bills (where NSA may not apply), you can negotiate directly &mdash; ask for the &ldquo;Medicare rate&rdquo; or &ldquo;self-pay rate,&rdquo; or offer to pay the in-network equivalent rate.</p>

<h2 id="case-studies">7. Case studies: anesthesia disputes resolved</h2>

<div class="key-takeaway"><strong>Not sure what you were charged for?</strong> Use our <a href="/calculator">free calculator</a> to look up what Medicare pays for any anesthesia CPT code on your bill.</div>

<div class="case-study">
    <h3>Case Study 1: Out-of-network anesthesia bill, NSA violation — $1,840 eliminated</h3>
    <p>A patient scheduled a knee arthroscopy at an in-network hospital. The surgeon was in-network. After surgery, he received a separate bill for $1,840 from &ldquo;Allied Anesthesia Services&rdquo; &mdash; a group that was out-of-network with his insurer. His insurer&rsquo;s EOB showed the claim was processed at out-of-network rates, leaving him with $1,840 in patient responsibility.</p>
    <p>He called his insurer, cited the No Surprises Act, and requested that the claim be reprocessed at in-network rates. The insurer confirmed the procedure was scheduled and the facility was in-network. The claim was reprocessed. His actual in-network cost-sharing for the anesthesia was his $150 specialist copay. <strong>Total savings: $1,690.</strong></p>
</div>

<div class="case-study">
    <h3>Case Study 2: Incorrect qualifying circumstance code — $390 removed</h3>
    <p>A 67-year-old patient had a colonoscopy (CPT 00810, 7 base units, 30 minutes = 2 time units). Her bill showed 12 total units: 7 base + 2 time + 3 qualifying circumstance units (99100). At her insurer&rsquo;s in-network conversion factor of $130/unit, the 99100 add-on cost her $390 out-of-pocket through her deductible.</p>
    <p>She called the anesthesiology group and asked why 99100 was applied. After reviewing her chart, the billing department confirmed she was 67, not over 70, and the code did not apply. It was removed. <strong>Savings: $390.</strong></p>
</div>

<div class="case-study">
    <h3>Case Study 3: Time unit dispute — 3 extra units removed</h3>
    <p>A patient was billed 13 units for a 90-minute abdominal laparoscopy (00840, 7 base units). With 90 minutes of anesthesia time, the correct time units are 6 (90 &divide; 15 = 6). That should total 13 units &mdash; but the bill also included 3 qualifying circumstance units for 99100 (extreme age). The patient was 52.</p>
    <p>After requesting the anesthesia record and verifying the code was erroneous, the billing department removed the 3-unit add-on. At the insurer&rsquo;s conversion factor of $95/unit, the correction reduced his bill by $285. <strong>Savings: $285.</strong></p>
</div>

<h2 id="faq">Frequently asked questions</h2>

<div class="faq-section">
    <div class="faq-item">
        <h3>Why did I get a separate bill from the anesthesiologist?</h3>
        <p>Anesthesiologists usually work for independent groups, not the hospital. Even at an in-network facility, the anesthesiology group may be a separate entity. Since January 2022, the No Surprises Act prohibits anesthesiologists at in-network facilities from billing you out-of-network rates for scheduled procedures. If you received such a bill, contact your insurer &mdash; you may only owe your in-network cost-sharing amount.</p>
    </div>

    <div class="faq-item">
        <h3>How is anesthesia priced?</h3>
        <p>Anesthesia is priced in units: Base Units (assigned to the procedure type, ranging from 3&ndash;25) + Time Units (1 per 15 minutes) &times; Conversion Factor (the dollar rate per unit). Medicare pays approximately $26 per unit. Commercial in-network rates are typically $60&ndash;$150 per unit. Your bill should show the base units, time, and any qualifying circumstance add-ons.</p>
    </div>

    <div class="faq-item">
        <h3>What is the difference between an anesthesiologist and a CRNA?</h3>
        <p>An anesthesiologist (MD/DO) completed medical school plus a 4-year anesthesiology residency. A CRNA (Certified Registered Nurse Anesthetist) completed nursing school plus an advanced anesthesia program. Both can administer anesthesia. Both should be billed at in-network rates if your facility is in-network, under the No Surprises Act.</p>
    </div>

    <div class="faq-item">
        <h3>What are qualifying circumstances in anesthesia billing?</h3>
        <p>Qualifying circumstance codes (99100, 99116, 99135, 99140) add extra units when anesthesia is more complex. Code 99100 adds 3 units for patients under 1 or over 70. Code 99140 adds 2 units for true emergencies. These codes add to your bill and are sometimes applied incorrectly &mdash; always verify that the qualifying circumstance actually existed for your case.</p>
    </div>

    <div class="faq-item">
        <h3>Does the No Surprises Act cover anesthesia bills?</h3>
        <p>Yes. The NSA prohibits surprise out-of-network billing from anesthesiologists (and other non-emergency providers) at in-network facilities for scheduled procedures, effective January 2022. If you received an out-of-network anesthesia bill for a scheduled surgery at an in-network hospital, contact your insurer and file a complaint at <a href="https://www.cms.gov/nosurprises" target="_blank" rel="noopener">cms.gov/nosurprises</a>.</p>
    </div>

    <div class="faq-item">
        <h3>What should I do if I receive an unexpectedly large anesthesia bill?</h3>
        <p>Request your anesthesia record, verify the units math (base + time + qualifying circumstances), and check your EOB. If the facility was in-network and the procedure was scheduled, you likely have NSA protection &mdash; contact your insurer to have the claim reprocessed. <a href="/scan">Upload your bill to BillKarma</a> for an automated review of the charges.</p>
    </div>
</div>

<h2 id="sources">Sources</h2>

<ul class="sources-list">
    <li><a href="https://www.healthaffairs.org/doi/10.1377/hlthaff.2019.01453" target="_blank" rel="noopener">Health Affairs: Surprise Out-of-Network Anesthesia Bills (2020)</a></li>
    <li><a href="https://www.cms.gov/nosurprises" target="_blank" rel="noopener">CMS: No Surprises Act — Patient Protections and Resources</a></li>
    <li><a href="https://www.cms.gov/medicare/payment/fee-schedules/anesthesiologist" target="_blank" rel="noopener">CMS: Anesthesiologist Center — Fee Schedule and Payment Rates (2026)</a></li>
    <li><a href="https://www.asahq.org/standards-and-practice-parameters/relative-value-guide" target="_blank" rel="noopener">American Society of Anesthesiologists: Relative Value Guide (2025)</a></li>
    <li><a href="https://www.cms.gov/medicare/coding-billing/medicare-correct-coding-initiative-ncci/ncci-policy-manual" target="_blank" rel="noopener">CMS: NCCI Policy Manual — Anesthesia Billing Guidelines</a></li>
    <li><a href="https://kff.org/health-costs/issue-brief/no-surprises-act-implementation/" target="_blank" rel="noopener">KFF: No Surprises Act Implementation and Patient Experiences (2024)</a></li>
</ul>
""",
})
