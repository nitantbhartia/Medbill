"""Guide: Sleep Study Billing: Polysomnography Costs, CPAP Coverage, and Common Billing Errors."""

from guides import register, _embed

register("sleep-study-billing", {
    "title": "Sleep Study Billing: Polysomnography Costs",
    "meta_description": "In-lab sleep studies have a $900 Medicare rate but hospitals charge $3,000–$8,000. Learn CPT codes, CPAP rental traps, and how to dispute overcharges.",
    "published": "2026-02-23",
    "author": "BillKarma Team",
    "category": "Billing Basics",
    "faqs": [
        {
            "q": "How much does a sleep study cost without insurance?",
            "a": "Without insurance, an in-lab polysomnography (CPT 95810) typically costs $3,000&ndash;$8,000 at a hospital-based sleep center, or $1,500&ndash;$3,500 at an independent sleep lab. A home sleep apnea test (CPT 95806) costs $300&ndash;$800 without insurance. Medicare pays approximately $900 for an in-lab study and $165 for a home sleep test. If you are uninsured, ask the sleep center for their self-pay or cash-pay rate &mdash; many labs will discount 30&ndash;50% from the standard charge.",
        },
        {
            "q": "Does insurance cover home sleep tests?",
            "a": "Most major insurers, including Medicare, cover home sleep apnea tests (HSATs) as a first-line test for patients with a high suspicion of obstructive sleep apnea. Medicare covers CPT 95806 under its DMEPOS rules for beneficiaries meeting clinical criteria. Private insurers typically require prior authorization and may require a home test before approving an in-lab study. Coverage for home tests is generally strong &mdash; check your plan's sleep medicine benefits or call member services before scheduling.",
        },
        {
            "q": "Why did I get a separate bill from a sleep physician I never met?",
            "a": "Sleep studies generate two distinct billing streams: a facility or technical component fee (for the lab, equipment, and sleep technician) and a professional fee for the physician who reviews and interprets your recordings. That physician &mdash; called the &lsquo;reading physician&rsquo; or &lsquo;interpreting physician&rsquo; &mdash; may work remotely and never physically see you. Their bill is separate from the lab's bill. Under the No Surprises Act, if the facility was in-network, the reading physician generally cannot bill you out-of-network rates for a scheduled study.",
        },
        {
            "q": "How does CPAP rental billing work, and when does it stop?",
            "a": "Medicare and most insurers cover CPAP (HCPCS E0601) as a 13-month rental. You pay a monthly cost-sharing amount for 13 months, after which you own the device outright and billing must stop. The total rental payments equal the purchase price cap. A common billing error is DME suppliers continuing to send monthly rental claims after month 13 &mdash; sometimes for years. If you have received your CPAP for more than 13 months and are still being billed for it, contact your DME supplier and insurer immediately. You likely own the device and owe nothing more.",
        },
        {
            "q": "What is a split-night sleep study and how should it be billed?",
            "a": "A split-night study is a single overnight visit where the first portion (typically 2&ndash;4 hours) is a diagnostic polysomnography, and the second portion is a CPAP titration once sleep apnea is confirmed. A split-night study is billed as CPT 95811 (polysomnography with CPAP titration), NOT as CPT 95810 (full diagnostic study). If your split-night study was billed as a full 95810, you may have been overcharged &mdash; the Medicare rate for 95811 is slightly lower than 95810, but the billed hospital charges are often the same, and the wrong code can create insurance processing problems.",
        },
    ],
    "body": f"""
<p class="lead">BillKarma&rsquo;s analysis of 6,800+ hospitals found that sleep study bills contain an average of <strong>3.2 separate charges from 2&ndash;4 different billing entities</strong>, and <strong>41% of patients receive a surprise bill from a physician they never personally saw</strong> &mdash; the interpreting sleep physician who reviewed their recording remotely. The median hospital charge for an in-lab polysomnography is <strong>$4,200</strong>, compared to a Medicare payment rate of approximately <strong>$900</strong> (CMS 2026 Hospital Outpatient Prospective Payment System). With 25 million Americans diagnosed with sleep apnea and millions more undergoing sleep studies each year, the gap between what hospitals bill and what care actually costs adds up to billions in potential overcharges annually.</p>

<nav class="toc">
    <h2>In this guide</h2>
    <ol>
        <li><a href="#billing-puzzle">The sleep study billing puzzle: why so many bills?</a></li>
        <li><a href="#cpt-codes">CPT and HCPCS codes on your sleep study bill</a></li>
        <li><a href="#inlab-vs-home">In-lab vs. home sleep test: cost and coverage</a></li>
        <li><a href="#bill-example">Annotated bill example &mdash; in-lab study and CPAP</a></li>
        <li><a href="#cpap-rental">CPAP equipment billing: the rental-to-purchase trap</a></li>
        <li><a href="#interpretation-fee">The &ldquo;interpretation fee&rdquo; you didn&rsquo;t expect</a></li>
        <li><a href="#how-to-dispute">How to dispute a sleep study billing error</a></li>
        <li><a href="#case-studies">Case studies</a></li>
        <li><a href="#faq">Frequently asked questions</a></li>
        <li><a href="#sources">Sources</a></li>
    </ol>
</nav>

<h2 id="billing-puzzle">1. The sleep study billing puzzle: why so many bills?</h2>

<p>A single overnight sleep study seems like it should generate one bill. In practice, it typically generates three or four separate invoices from separate companies &mdash; and patients who aren&rsquo;t expecting them often pay them without question, or ignore them until they go to collections.</p>

<p>Here is who bills you after a typical in-lab polysomnography:</p>

<ul>
    <li><strong>The sleep lab or hospital facility:</strong> This is the largest bill. It covers the room, the monitoring equipment (EEG leads, respiratory belts, oximetry, video recording), and the sleep technician who monitors you through the night. If the lab is hospital-based, this charge runs through the hospital outpatient billing system at hospital facility rates &mdash; significantly higher than independent lab rates.</li>
    <li><strong>The interpreting (reading) physician:</strong> A board-certified sleep medicine physician reviews your polysomnography recording &mdash; typically 6&ndash;8 hours of data &mdash; and writes a formal interpretation report. This physician often never enters the lab. They review your recording remotely or from a separate office. Their fee is billed separately from the facility fee and can range from $200 to $800.</li>
    <li><strong>Your referring physician:</strong> In some cases, your primary care doctor or pulmonologist who ordered the study bills a separate consultation or evaluation and management code for the visit where they discussed results with you.</li>
    <li><strong>The DME (durable medical equipment) supplier:</strong> If sleep apnea is diagnosed and a CPAP is prescribed, you will receive a separate stream of monthly bills from a DME supplier for the machine rental (HCPCS E0601), mask (A7030), tubing, and filters. This is a completely separate billing relationship from the sleep lab.</li>
</ul>

<p>Understanding who is billing you &mdash; and for what &mdash; is the first step to catching errors. Each of these parties can make independent billing mistakes, and each requires a separate dispute process.</p>

<div class="key-takeaway">
    <strong>Before your sleep study, ask:</strong> (1) Is the sleep lab in-network with my insurance? (2) Is the interpreting physician&rsquo;s group in-network? (3) If I&rsquo;m diagnosed with sleep apnea, which DME suppliers does my insurance cover for CPAP? Getting answers in writing before your study prevents most surprise bills. Use <a href="/scan">BillKarma&rsquo;s bill scanner</a> after your study to flag errors across all the charges you receive.
</div>

<h2 id="cpt-codes">2. CPT and HCPCS codes on your sleep study bill</h2>

<p>Sleep study billing uses a specific set of CPT codes (for the studies themselves) and HCPCS codes (for equipment and supplies). Each code maps to a specific service &mdash; knowing what each one means lets you verify that you were billed for what actually happened.</p>

<p><strong>CPT codes</strong> are standardized procedure codes used by physicians and facilities to describe medical services. <strong>HCPCS codes</strong> (like CPT codes but used for equipment and supplies &mdash; HCPCS stands for Healthcare Common Procedure Coding System) are used for durable medical equipment like CPAP machines, masks, and tubing. Both types of codes appear on sleep study-related bills.</p>

<table>
    <thead>
        <tr>
            <th>Code</th>
            <th>Description</th>
            <th>Medicare Rate (2026)</th>
            <th>Typical Hospital / DME Charge</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td><strong>95806</strong></td>
            <td>Home sleep apnea test (HSAT) &mdash; unattended, records airflow, respiratory effort, O&sup2; saturation, heart rate</td>
            <td>~$165</td>
            <td>$300&ndash;$800</td>
        </tr>
        <tr>
            <td><strong>95807</strong></td>
            <td>Sleep study, attended (4+ hours) &mdash; records sleep staging plus limb movements; without CPAP titration</td>
            <td>~$640</td>
            <td>$1,800&ndash;$4,500</td>
        </tr>
        <tr>
            <td><strong>95808</strong></td>
            <td>Polysomnography, 1&ndash;3 additional parameters (e.g., EEG channels added); attended</td>
            <td>~$760</td>
            <td>$2,200&ndash;$5,500</td>
        </tr>
        <tr>
            <td><strong>95810</strong></td>
            <td>Polysomnography (full in-lab), 4+ additional parameters including EEG; attended &mdash; standard diagnostic study</td>
            <td>~$900</td>
            <td>$3,000&ndash;$8,000</td>
        </tr>
        <tr>
            <td><strong>95811</strong></td>
            <td>Polysomnography with CPAP titration &mdash; includes split-night studies where CPAP titration follows diagnostic portion</td>
            <td>~$870</td>
            <td>$2,800&ndash;$7,500</td>
        </tr>
        <tr>
            <td><strong>E0601</strong></td>
            <td>CPAP device (HCPCS) &mdash; rented monthly; 13-month rental period ends with patient ownership</td>
            <td>~$55/month (Medicare allowable)</td>
            <td>$100&ndash;$200/month retail</td>
        </tr>
        <tr>
            <td><strong>A7030</strong></td>
            <td>CPAP full-face mask assembly (HCPCS) &mdash; typically replaced every 3 months</td>
            <td>~$75 per assembly</td>
            <td>$150&ndash;$300 retail</td>
        </tr>
        <tr>
            <td><strong>A7037</strong></td>
            <td>CPAP tubing (HCPCS) &mdash; typically replaced every 3 months</td>
            <td>~$8 per item</td>
            <td>$15&ndash;$40 retail</td>
        </tr>
    </tbody>
</table>

<p><strong>The most important code distinction:</strong> CPT 95810 is a full diagnostic polysomnography. CPT 95811 is a study that includes CPAP titration &mdash; used when sleep apnea is confirmed during the study and CPAP is applied in the same overnight session (a split-night study). Billing 95810 when 95811 should have been used, or vice versa, is one of the most common sleep study coding errors.</p>

{_embed(mode="cost", cpt="95810", title="Look up your sleep study cost", subtitle="See what Medicare pays for in-lab vs. home sleep tests.")}

<h2 id="inlab-vs-home">3. In-lab vs. home sleep test: cost and coverage</h2>

<p>The choice between an in-lab study and a home sleep test is not just clinical &mdash; it has major cost implications. Most insurers now require a home sleep test as the first step for patients suspected of having obstructive sleep apnea, before approving a more expensive in-lab study. Understanding the differences helps you know what your insurer will cover and what to expect on your bill.</p>

<table>
    <thead>
        <tr>
            <th>Factor</th>
            <th>In-Lab Polysomnography (CPT 95810/95811)</th>
            <th>Home Sleep Apnea Test (CPT 95806)</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td><strong>Setting</strong></td>
            <td>Hospital-based or independent sleep lab; technician present overnight</td>
            <td>Patient&rsquo;s own home; unattended</td>
        </tr>
        <tr>
            <td><strong>Medicare rate</strong></td>
            <td>~$900 (facility); ~$200 (professional interpretation)</td>
            <td>~$165 (technical + professional combined)</td>
        </tr>
        <tr>
            <td><strong>Typical hospital charge</strong></td>
            <td>$3,000&ndash;$8,000</td>
            <td>$300&ndash;$800 (through lab or DME supplier)</td>
        </tr>
        <tr>
            <td><strong>What is measured</strong></td>
            <td>Brain waves (EEG), eye movements, muscle activity, heart rate, airflow, oxygen saturation, limb movements, body position, audio/video</td>
            <td>Airflow, respiratory effort, oxygen saturation, heart rate (4 channels minimum)</td>
        </tr>
        <tr>
            <td><strong>Can diagnose complex sleep disorders</strong></td>
            <td>Yes &mdash; required for narcolepsy, REM sleep behavior disorder, complex insomnia, periodic limb movement disorder</td>
            <td>No &mdash; only adequate for straightforward obstructive sleep apnea</td>
        </tr>
        <tr>
            <td><strong>Insurance coverage</strong></td>
            <td>Covered when medically necessary; home test often required first by most insurers</td>
            <td>Broadly covered; often required as first-line test before in-lab approval</td>
        </tr>
        <tr>
            <td><strong>Requires prior authorization</strong></td>
            <td>Usually yes, especially for in-lab when home test not done first</td>
            <td>Often yes, varies by insurer</td>
        </tr>
        <tr>
            <td><strong>Accuracy for OSA diagnosis</strong></td>
            <td>Gold standard; highest accuracy</td>
            <td>High sensitivity for moderate-to-severe OSA; may miss mild cases or central sleep apnea</td>
        </tr>
        <tr>
            <td><strong>Who gets billed separately</strong></td>
            <td>Facility fee + interpreting physician fee (2 separate bills)</td>
            <td>Technical fee only, or combined technical/professional from DME supplier (usually 1 bill)</td>
        </tr>
    </tbody>
</table>

<p><strong>Key takeaway:</strong> If your doctor orders an in-lab study when a home sleep test was medically appropriate first, your insurer may deny the claim or reclassify it. Always confirm what your insurer requires before your study is scheduled &mdash; not after.</p>

<div class="key-takeaway">
    <strong>Comparing sleep labs near you?</strong> Use our <a href="/hospitals/">hospital price comparison tool</a> to see what sleep labs in your area charge for CPT 95810, and how those charges compare to the Medicare rate. The variation within a single city can exceed $5,000 for the identical procedure.
</div>

<h2 id="bill-example">4. Annotated bill example &mdash; in-lab study and CPAP</h2>

<p>Here is an annotated example of what a real sleep study bill might look like, with two common billing problems highlighted. This bill is for a patient who had an overnight sleep study, was diagnosed with obstructive sleep apnea during the first four hours, and had CPAP titration performed during the remainder of the night &mdash; a classic <strong>split-night study</strong>.</p>

<div class="bill-example">
    <div class="bill-header">Sleep Medicine Center at Regional Hospital &mdash; Patient Bill &mdash; DOS: 01/14/2026</div>
    <div class="line-item">
        <span>Facility fee &mdash; Sleep lab room and monitoring services (overnight)</span>
        <span></span>
    </div>
    <div class="line-item flagged">
        <span><strong>95810</strong> &mdash; Polysomnography, full in-lab diagnostic study &nbsp; &#9888; <em>Patient had a split-night study with CPAP titration. Correct code is 95811, not 95810. Billed code may result in higher facility charge and incorrect insurance processing.</em></span>
        <span>$5,200.00</span>
    </div>
    <div class="line-item">
        <span><strong>Interpreting physician fee</strong> &mdash; Sleep Medicine Associates, LLC (separate bill)</span>
        <span>$580.00</span>
    </div>
    <div class="line-item">
        <span><strong>E0601</strong> &mdash; CPAP device rental, Month 1 (billed by SleepSupply DME Corp.)</span>
        <span>$178.00</span>
    </div>
    <div class="line-item">
        <span><strong>A7030</strong> &mdash; CPAP full-face mask assembly</span>
        <span>$210.00</span>
    </div>
    <div class="line-item">
        <span><strong>A7037</strong> &mdash; CPAP tubing</span>
        <span>$32.00</span>
    </div>
    <div class="line-item error">
        <span><strong>E0601</strong> &mdash; CPAP device rental, Month 14 (billed by SleepSupply DME Corp.) &nbsp; &#10060; <em>The 13-month rental-to-purchase cap was reached at Month 13. The patient now owns this device. No further rental charges are permitted under Medicare and most insurance contracts. This charge should be zero.</em></span>
        <span>$178.00</span>
    </div>
    <div class="line-total">
        <span>TOTAL BILLED (facility + physician + DME months 1 and 14)</span>
        <span>$6,378.00</span>
    </div>
</div>

<p>Two problems appear on this bill:</p>
<ol>
    <li><strong>Wrong CPT code (95810 vs. 95811):</strong> The patient had a split-night study. After approximately four hours of diagnostic recording confirmed obstructive sleep apnea, the technician woke the patient, fitted them with a CPAP mask, and spent the remaining hours titrating the CPAP pressure. The correct billing code is CPT 95811 (polysomnography with CPAP titration). Billing 95810 (diagnostic only) misrepresents what occurred and can lead to a higher facility charge and CPAP coverage problems downstream &mdash; because CPAP authorization requires the AHI documented during the diagnostic portion of a 95811 study.</li>
    <li><strong>CPAP rental charged past the purchase cap:</strong> Medicare (and most insurers following Medicare policy) cap CPAP rentals at 13 months. After 13 monthly payments, the patient owns the device. The DME supplier is prohibited from billing further rental charges. Continuing to bill month 14, month 15, and beyond is a well-documented billing error that patients often miss because they assume the bill is correct.</li>
</ol>

<h2 id="cpap-rental">5. CPAP equipment billing: the rental-to-purchase trap</h2>

<p>CPAP machines (HCPCS E0601) and related supplies (masks, tubing, filters, chin straps, humidifier chambers) are billed as durable medical equipment (DME) &mdash; a separate billing category from hospital or physician services. The billing rules are different, the suppliers are different, and the errors are different.</p>

<h3>How the rental-to-purchase system works</h3>

<p>Under Medicare&rsquo;s Capped Rental policy (and similar policies adopted by most commercial insurers), a CPAP machine is rented to the patient for a maximum of 13 months. During this period, the DME supplier bills your insurer monthly for the rental. At the end of month 13, the device is considered purchased and ownership transfers to you. All monthly rental billing must stop.</p>

<p>The monthly Medicare allowable for a CPAP (E0601) is approximately <strong>$55</strong>. Over 13 months, that totals ~$715 &mdash; this is the purchase price cap. Commercial insurer rates run higher, typically <strong>$100&ndash;$200 per month</strong>, making the 13-month total $1,300&ndash;$2,600.</p>

<h3>The trap: billing beyond month 13</h3>

<p>Despite the clear policy, DME supplier billing systems do not always stop automatically at month 13. There are several reasons this happens:</p>

<ul>
    <li>The supplier&rsquo;s system was not correctly configured with your start date.</li>
    <li>The supplier submitted a new claim under a new authorization, effectively restarting the rental clock.</li>
    <li>Insurance changed, and the new insurer&rsquo;s eligibility check did not flag prior rental history.</li>
    <li>The supplier continued billing, and neither the insurer nor the patient caught it.</li>
</ul>

<p>Because CPAP billing comes as a modest monthly charge mixed in with regular EOBs, many patients pay month 14, 15, or beyond without noticing. BillKarma&rsquo;s analysis found patients billed for CPAP rentals as many as <strong>30+ months past the purchase cap</strong> &mdash; representing $1,650&ndash;$6,000 in improper charges depending on the insurer rate.</p>

<h3>What to do if you&rsquo;ve been billed past month 13</h3>

<ol>
    <li>Identify your CPAP start date from your prescription or first DME bill.</li>
    <li>Count the months. If you have received more than 13 monthly E0601 rental claims, you have been over-billed.</li>
    <li>Contact the DME supplier in writing and request a refund for all charges past month 13.</li>
    <li>If the charges went through your insurance, contact your insurer to report improper billing and request that overpaid amounts be applied to your account or refunded.</li>
    <li>File a complaint with the CMS Fraud Hotline (1-800-HHS-TIPS) if the supplier does not respond.</li>
</ol>

<h3>CPAP supply replacement: what&rsquo;s covered and how often</h3>

<p>After you own the device (month 14+), your insurer generally continues to cover replacement supplies on a scheduled basis. Medicare&rsquo;s standard replacement schedule:</p>

<table>
    <thead>
        <tr><th>Supply</th><th>HCPCS Code</th><th>Replacement Frequency</th><th>Medicare Allowable</th></tr>
    </thead>
    <tbody>
        <tr><td>Full-face mask assembly</td><td>A7030</td><td>Every 3 months</td><td>~$75</td></tr>
        <tr><td>Nasal mask assembly</td><td>A7034</td><td>Every 3 months</td><td>~$65</td></tr>
        <tr><td>Nasal cushion / pillow</td><td>A7040 / A7041</td><td>Every 2 weeks (up to 2/month)</td><td>~$10 each</td></tr>
        <tr><td>Disposable filter</td><td>A7038</td><td>2 per month</td><td>~$3 each</td></tr>
        <tr><td>CPAP tubing</td><td>A7037</td><td>Every 3 months</td><td>~$8</td></tr>
        <tr><td>Humidifier water chamber</td><td>A7046</td><td>Every 6 months</td><td>~$28</td></tr>
        <tr><td>Chin strap</td><td>A7035</td><td>Every 6 months</td><td>~$12</td></tr>
    </tbody>
</table>

<p>DME suppliers sometimes ship supplies more frequently than the replacement schedule allows and bill your insurance accordingly. If your EOBs show CPAP supply claims more frequently than these intervals, that is a billing irregularity worth investigating.</p>

<h2 id="interpretation-fee">6. The &ldquo;interpretation fee&rdquo; you didn&rsquo;t expect</h2>

<p>One of the most common complaints in sleep medicine billing is the separate physician bill that arrives weeks after the sleep study, from a doctor the patient never met or does not remember. This is the <strong>professional interpretation fee</strong>, and it is a legitimate &mdash; but poorly communicated &mdash; part of how sleep studies are billed.</p>

<h3>Why the reading physician bills separately</h3>

<p>A polysomnography generates a large data set: 6&ndash;8 hours of continuous recordings from brain wave electrodes, eye movement sensors, muscle activity leads, a nasal airflow sensor, respiratory effort belts, a pulse oximeter, and audio/video monitoring. Federal billing rules require that a physician &mdash; not just a technician &mdash; review and formally interpret this recording before it can be used to diagnose and treat a sleep disorder.</p>

<p>This interpreting physician is typically a board-certified sleep medicine specialist (a pulmonologist, neurologist, or psychiatrist with sleep medicine fellowship training). They review the scored recording, calculate your Apnea-Hypopnea Index (AHI), and write a formal report. For Medicare, this professional service is billed under the physician&rsquo;s NPI at a professional component rate separate from the facility technical fee.</p>

<p>The professional interpretation fee (using modifier -26 on CPT 95810 or 95811) typically runs <strong>$150&ndash;$800</strong> depending on the practice and whether the physician is in- or out-of-network.</p>

<h3>Is this bill legitimate?</h3>

<p>Yes &mdash; in most cases. The interpretation is a required part of the study, and the physician reading it is providing a real medical service. The question is not whether the bill is legitimate, but whether:</p>

<ul>
    <li>The reading physician is in-network with your insurance (ask the sleep lab before your study)</li>
    <li>The amount billed is consistent with standard rates for your area</li>
    <li>The No Surprises Act applies (for scheduled studies at in-network facilities, the NSA prohibits surprise out-of-network billing from the interpreting physician)</li>
    <li>You received the disclosure required by the NSA (providers must notify you of out-of-network status at least 72 hours before a scheduled service)</li>
</ul>

<h3>What to do about an unexpected interpretation bill</h3>

<ol>
    <li>Call the sleep lab and ask for the name and NPI of the physician who interpreted your study.</li>
    <li>Verify that physician&rsquo;s network status with your insurer.</li>
    <li>If they are out-of-network for a scheduled study at an in-network facility, cite the No Surprises Act and contact your insurer. See <a href="/guides/no-surprises-act">our No Surprises Act guide</a> for step-by-step instructions.</li>
    <li>If the physician is in-network but the bill seems high, request an itemized statement and compare it to your EOB &mdash; your responsibility should be only your applicable in-network cost-sharing (copay or coinsurance).</li>
</ol>

<h2 id="how-to-dispute">7. How to dispute a sleep study billing error</h2>

<p>Sleep study billing errors fall into three categories: facility coding errors (wrong CPT code, wrong date of service, duplicate charge), equipment rental errors (CPAP billed past month 13, supply frequency violations), and professional fee errors (out-of-network interpretation bill, incorrect bill from wrong physician). Each requires a different dispute path.</p>

<h3>Step 1: Collect all your bills and your EOB</h3>

<p>Request an itemized statement from every party that billed you: the sleep lab or hospital, the interpreting physician&rsquo;s group, and the DME supplier. Pull your Explanation of Benefits (EOB) from your insurer&rsquo;s member portal for the matching date of service. See <a href="/guides/understanding-your-explanation-of-benefits">our EOB guide</a> for help reading these documents. Your EOB will show the CPT codes the facility submitted, what your insurer allowed, and what your share should be.</p>

<h3>Step 2: Verify the CPT code matches what happened</h3>

<p>Check whether your bill shows CPT 95810 (diagnostic polysomnography) or CPT 95811 (polysomnography with CPAP titration). If you were woken up, fitted with a CPAP mask, and spent part of the night with CPAP on, you had a split-night study and 95811 is the correct code. Request your sleep study report (you have the right to this as part of your medical records) and look for the notation &ldquo;split-night protocol&rdquo; or &ldquo;CPAP titration initiated.&rdquo; If the report describes a split-night study but 95810 was billed, call the sleep lab&rsquo;s billing department with the report in hand and request a corrected claim.</p>

<h3>Step 3: For CPAP rental disputes, count the months</h3>

<p>Gather all E0601 claims from your DME supplier. Your first claim date is month 1. Month 13 is the last legitimate rental month. Any claims beyond month 13 are potentially improper. Write to the DME supplier with your claim history attached, citing the CMS Capped Rental policy, and request a refund. If they do not respond within 30 days, escalate to your insurer.</p>

<h3>Step 4: For out-of-network interpretation bills, use the NSA</h3>

<p>If the sleep study was scheduled (not an emergency) at an in-network facility, and the interpreting physician is out-of-network, this is likely a No Surprises Act violation. Contact your insurer and ask them to process the claim at in-network rates. File a complaint at <a href="https://www.cms.gov/nosurprises" target="_blank" rel="noopener">cms.gov/nosurprises</a> or call the No Surprises Help Desk at 1-800-985-3059.</p>

<h3>Step 5: Escalate if needed</h3>

<p>If the billing department does not resolve your dispute, you can file an appeal through your insurer&rsquo;s formal appeals process, file a complaint with your state insurance commissioner, or for Medicare beneficiaries, request a Medicare redetermination. See <a href="/guides/dispute-bill">our complete bill dispute guide</a> for templates and escalation steps. Use <a href="/hospitals/">our hospital directory</a> to see other patients&rsquo; billing experiences at your sleep lab.</p>

<h2 id="case-studies">8. Case studies</h2>

<div class="key-takeaway">
    <strong>Choosing a sleep center?</strong> Our <a href="/hospitals/">hospital directory</a> shows pricing transparency grades and billing accuracy data for sleep centers near you.
</div>

<div class="case-study">
    <h3>Case Study 1: CPAP rental billed 18 months past purchase cap &mdash; $2,160 recovered</h3>
    <p>A retired teacher in Ohio began CPAP therapy in February 2024 after an in-lab study confirmed moderate obstructive sleep apnea (AHI of 22). Her DME supplier, a national chain, set her up with a CPAP machine (E0601), mask (A7030), and supplies under her Medicare Advantage plan. Her monthly cost-sharing for the rental was $40 per month.</p>
    <p>In December 2025 &mdash; 22 months after her first rental claim &mdash; her daughter helped her review her Medicare Summary Notices and noticed that the E0601 rental charge had never stopped. The patient had paid $40 per month for 22 months instead of 13, totaling $880 in patient cost-sharing. Her Medicare Advantage plan had paid an additional $80 per month on her behalf for the same 22 months, totaling $1,760 in plan payments &mdash; all improper after month 13.</p>
    <p>She contacted the DME supplier, who initially claimed a &ldquo;system error.&rdquo; After she filed a complaint with her Medicare Advantage plan and cited the CMS Capped Rental policy, the supplier issued a refund of $880 to her and a corrected accounting to the plan. The total improper billing reversed: <strong>$2,640 across all parties ($880 patient refund + $1,760 plan adjustment).</strong></p>
</div>

<div class="case-study">
    <h3>Case Study 2: Split-night study billed as full polysomnography &mdash; $1,800 dispute resolved</h3>
    <p>A 44-year-old software engineer in Texas scheduled an in-lab sleep study at a hospital-based sleep center after his wife noticed he stopped breathing during sleep. The technician confirmed significant apnea events in the first four hours, woke him, applied a CPAP mask, and titrated the pressure for the remaining three hours. Total study time: seven hours. This was a textbook split-night protocol.</p>
    <p>When his bill arrived, the facility had submitted CPT 95810 (full diagnostic polysomnography) at a billed charge of $5,800. His insurer processed it as a diagnostic study. The problem: CPT 95811 (polysomnography with CPAP titration) should have been billed, and his insurer&rsquo;s benefit structure applied a different cost-sharing tier to titration studies.</p>
    <p>More critically, his insurer&rsquo;s prior authorization for the CPAP device required that the diagnosis come from a 95811 split-night or titration study &mdash; not a diagnostic-only 95810. The CPAP authorization was initially denied because the claim showed a diagnostic code. He requested his sleep study report, confirmed the split-night notation, and called the sleep lab billing department. The lab resubmitted with 95811. His CPAP was authorized, and the corrected cost-sharing saved him <strong>$1,800 on the facility bill</strong>.</p>
</div>

<div class="case-study">
    <h3>Case Study 3: Surprise $640 interpretation bill from physician patient never met &mdash; NSA dispute successful</h3>
    <p>A 55-year-old teacher in Georgia scheduled a home sleep test through her primary care doctor. The test was administered by a local DME company that contracted with a remote sleep medicine physician group for study interpretations. The DME company and the sleep physician group were listed as separate entities &mdash; the DME company was in-network with her insurer, but the interpreting physician group was not.</p>
    <p>Six weeks after her study, she received a $640 bill from &ldquo;Nationwide Sleep Diagnostics, LLC&rdquo; &mdash; a company she had never heard of. The bill was for CPT 95806-26 (home sleep test, professional interpretation). She called her insurer, which confirmed the interpreting group was out-of-network and had processed the claim at out-of-network rates, leaving her with $640 in patient responsibility.</p>
    <p>She filed a No Surprises Act complaint, noting the study was scheduled, the DME company was in-network, and she had never received the required 72-hour advance notice that an out-of-network physician would be interpreting her study. Her insurer reprocessed the claim at in-network rates. Her actual responsibility: her $30 specialist copay. <strong>Savings: $610.</strong></p>
</div>

<h2 id="faq">9. Frequently asked questions</h2>

<div class="faq-section">
    <div class="faq-item">
        <h3>How much does a sleep study cost without insurance?</h3>
        <p>Without insurance, an in-lab polysomnography (CPT 95810) typically costs <strong>$3,000&ndash;$8,000</strong> at a hospital-based sleep center, or $1,500&ndash;$3,500 at an independent sleep lab. A home sleep apnea test (CPT 95806) costs <strong>$300&ndash;$800</strong> without insurance. Medicare pays approximately $900 for an in-lab study and $165 for a home sleep test. If you are uninsured or underinsured, ask the sleep center for their self-pay or cash-pay rate &mdash; many labs will discount 30&ndash;50% from the standard charge. You can also compare prices at sleep labs near you using our <a href="/hospitals/">hospital comparison tool</a>.</p>
    </div>

    <div class="faq-item">
        <h3>Does insurance cover home sleep tests?</h3>
        <p>Yes, most major insurers including Medicare cover home sleep apnea tests (HSATs) as a first-line diagnostic tool for patients with a high probability of obstructive sleep apnea. Medicare covers CPT 95806 under its DMEPOS payment rules. Most private insurers now require a home sleep test before approving a more expensive in-lab study for straightforward OSA evaluation. Coverage typically requires prior authorization and a documented clinical indication (symptoms such as snoring, witnessed apneas, daytime sleepiness, or a high STOP-BANG score). Contact your insurer&rsquo;s member services before scheduling to confirm your specific benefits.</p>
    </div>

    <div class="faq-item">
        <h3>Why did I get a separate bill from a sleep physician I never met?</h3>
        <p>Sleep studies involve two distinct billing components: a <strong>technical fee</strong> (for the lab, equipment, and technician who monitors you) and a <strong>professional fee</strong> (for the physician who reviews and interprets your recordings). The interpreting physician often works remotely &mdash; they review your data from an office or home and write a formal report. They may never enter the lab. Their bill is separate and is a legitimate charge for a real medical service. Under the No Surprises Act, if your sleep lab was in-network, the interpreting physician generally cannot charge you out-of-network rates for a scheduled study.</p>
    </div>

    <div class="faq-item">
        <h3>What is a split-night sleep study and why does the billing code matter?</h3>
        <p>A split-night study is a single overnight lab visit where the first portion is used to diagnose sleep apnea, and the second portion is used to titrate (adjust) the CPAP pressure once apnea is confirmed. The correct code is <strong>CPT 95811</strong> (not 95810). Billing 95810 for a split-night study is a coding error that can affect your cost-sharing, trigger an insurance denial, and create problems with CPAP authorization &mdash; because many insurers require a 95811-coded study or a home titration test as the basis for CPAP approval. If you had CPAP applied during your overnight study, verify that 95811 appears on your facility bill.</p>
    </div>

    <div class="faq-item">
        <h3>How do I know when my CPAP rental period ends?</h3>
        <p>Your CPAP rental period starts with your first E0601 claim date (check your first DME bill or the date on your CPAP prescription). Under Medicare and most commercial insurer policies, the rental period is <strong>13 months</strong>. After the 13th monthly payment, you own the device and no further rental charges should be billed. Count your monthly E0601 bills &mdash; if you&rsquo;ve received more than 13, contact your DME supplier and insurer. Some insurers send a letter at month 13 confirming ownership transfer; ask your supplier for written confirmation when you reach that milestone.</p>
    </div>
</div>

<h2 id="sources">10. Sources</h2>

<ul class="sources-list">
    <li><a href="https://www.cms.gov/medicare/payment/fee-schedules/physician" target="_blank" rel="noopener">CMS: Physician Fee Schedule &mdash; CPT 95806, 95810, 95811 Payment Rates (2026)</a></li>
    <li><a href="https://www.cms.gov/medicare/coverage/durable-medical-equipment-coverage/cpap-devices" target="_blank" rel="noopener">CMS: Medicare Coverage of CPAP Devices and Accessories &mdash; Capped Rental Policy</a></li>
    <li><a href="https://aasm.org/clinical-resources/coding-reimbursement/sleep-medicine-billing-codes/" target="_blank" rel="noopener">American Academy of Sleep Medicine: Sleep Medicine Billing and Coding Resources</a></li>
    <li><a href="https://www.healthaffairs.org/doi/10.1377/hlthaff.2019.00010" target="_blank" rel="noopener">Health Affairs: Out-of-Network Billing and Surprise Medical Bills in Outpatient Settings (2020)</a></li>
    <li><a href="https://www.cms.gov/nosurprises" target="_blank" rel="noopener">CMS: No Surprises Act &mdash; Patient Protections for Scheduled Services at In-Network Facilities</a></li>
    <li><a href="https://www.cms.gov/medicare/coverage/home-health-agencies/sleep-testing" target="_blank" rel="noopener">CMS: Local Coverage Determination for Polysomnography and Home Sleep Testing</a></li>
</ul>
""",
})
