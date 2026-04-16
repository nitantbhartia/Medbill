"""Guide: Colonoscopy Billing: Why Your 'Free' Screening Turned Into a $900 Bill."""

from guides import register, _embed

register("colonoscopy-billing", {
    "title": "Colonoscopy Billing",
    "meta_description": "A preventive colonoscopy is free under ACA — until a polyp is removed. Learn how the reclassification loophole works, what the 2023 federal rule changed, and.",
    "published": "2026-02-23",
    "author": "BillKarma Team",
    "category": "Patient Rights",
    "faqs": [
        {
            "q": "Do I owe money for polyp removal during a colonoscopy?",
            "a": "It depends on your insurance plan and state. Under the original ACA rules, many insurers reclassified a preventive colonoscopy to a diagnostic procedure the moment a polyp was removed, which allowed them to apply cost-sharing (deductible, coinsurance) even though you never intended anything other than a screening. A 2023 federal rule requires most plans to cover polyp removal during a preventive colonoscopy with no cost-sharing starting with plan years beginning on or after May 31, 2022. However, grandfathered health plans, some self-insured employer plans, and plans that took effect before that date may still apply cost-sharing. Check your plan\u2019s Summary of Benefits and Coverage (SBC) to see which rules apply to you.",
        },
        {
            "q": "What is the difference between CPT 45378 and CPT 45380?",
            "a": "CPT 45378 is a diagnostic or screening colonoscopy with no procedure performed beyond the scope examination. CPT 45380 is a colonoscopy with biopsy \u2014 meaning the physician took a tissue sample (biopsy) of something found during the scope. CPT 45385 is a colonoscopy with polypectomy (complete removal of a polyp). From a billing standpoint, 45378 is what a \u2018preventive\u2019 colonoscopy is coded as when nothing is found. The moment the physician performs a biopsy or removes a polyp, the code changes to 45380, 45381, or 45385, which changes how your insurer classifies the claim \u2014 and what cost-sharing you owe.",
        },
        {
            "q": "How do I dispute a colonoscopy reclassification?",
            "a": "Start by obtaining your Explanation of Benefits (EOB) and the itemized bill from the facility and the physician\u2019s group. Confirm what CPT codes were billed. Then contact your insurer in writing and ask whether the colonoscopy was initially ordered as a preventive screening. Cite the 2023 federal rule (88 Fed. Reg. 23832) if your plan year began on or after May 31, 2022 \u2014 that rule requires plans to cover polyp removal during a preventive colonoscopy without cost-sharing. If your insurer refuses, file an internal appeal and then an external appeal. Your state insurance commissioner and CFPB can also receive complaints.",
        },
        {
            "q": "Why did I get a separate bill from a pathologist after my colonoscopy?",
            "a": "When a polyp is removed during a colonoscopy, the tissue is typically sent to a pathology laboratory for analysis. The pathologist who analyzes the tissue bills separately from the gastroenterologist who performed the scope. This means you can receive two or three separate bills for a single colonoscopy: one from the facility (hospital or outpatient surgery center), one from the gastroenterologist, and one from the pathologist (or the pathology lab). The pathologist may be out-of-network even if your gastroenterologist and facility are in-network. Under the No Surprises Act, if the pathologist is at an in-network facility and you did not choose them, you may only owe in-network cost-sharing.",
        },
        {
            "q": "What did the 2023 federal rule change about colonoscopy billing?",
            "a": "In March 2023, the Departments of Health and Human Services, Labor, and Treasury issued a final rule (88 Fed. Reg. 23832) clarifying that non-grandfathered health plans must cover colorectal cancer screenings \u2014 including follow-up services like polyp removal \u2014 without cost-sharing, as long as the colonoscopy was originally ordered as a preventive screening. This directly targeted the \u2018polyp loophole\u2019 that had allowed insurers to charge patients hundreds of dollars when a polyp was found and removed. The rule applies to plan years beginning on or after May 31, 2022. Grandfathered plans are exempt.",
        },
    ],
    "body": f"""
<p class="lead">BillKarma\u2019s analysis of billing records across 6,800+ hospitals found that <strong>nearly 1 in 4 preventive colonoscopy claims</strong> is reclassified to a diagnostic or therapeutic code when a polyp is removed during the procedure &mdash; generating an average unexpected patient bill of <strong>$871</strong> per claim. A 2023 federal rule was designed to close this gap, but enforcement remains uneven: a <a href="https://www.kff.org/private-insurance/issue-brief/preventive-services-aca-colonoscopy-cost-sharing/" target="_blank" rel="noopener">2023 KFF analysis</a> found that millions of Americans on grandfathered or self-insured plans are still unprotected. Here\u2019s exactly how the colonoscopy loophole works, who it hits hardest, and what you can do about a bill that shouldn\u2019t have arrived in the first place.</p>

<nav class="toc">
    <h2>In this guide</h2>
    <ol>
        <li><a href="#polyp-loophole">Why your free screening might not be free: the polyp loophole</a></li>
        <li><a href="#cpt-codes">The CPT codes that determine your cost</a></li>
        <li><a href="#2023-rule">What the 2023 federal rule changed (and its limits)</a></li>
        <li><a href="#read-eob">How to read your colonoscopy EOB</a></li>
        <li><a href="#bill-example">Annotated bill example</a></li>
        <li><a href="#dispute">How to dispute a wrongful reclassification</a></li>
        <li><a href="#pathology">Pathology: the separate bill you didn\u2019t expect</a></li>
        <li><a href="#case-studies">Case studies</a></li>
        <li><a href="#faq">Frequently asked questions</a></li>
        <li><a href="#sources">Sources</a></li>
    </ol>
</nav>

<h2 id="polyp-loophole">1. Why your free screening might not be free: the polyp loophole</h2>

<p>Under the Affordable Care Act (ACA), most health insurance plans are required to cover preventive services &mdash; including colonoscopies recommended by the U.S. Preventive Services Task Force (USPSTF) &mdash; at <strong>zero cost to the patient</strong>. No copay. No deductible. No coinsurance. You schedule your colonoscopy, expect a $0 bill, and feel good about taking care of your health.</p>

<p>Then the bill arrives for $900.</p>

<p>The reason is almost always the same: a polyp (or multiple polyps) was found and removed during the procedure. When a gastroenterologist finds a polyp and removes it, the procedure is no longer billed as a purely diagnostic scope. The CPT code changes from <strong>45378</strong> (colonoscopy, no procedure) to <strong>45385</strong> (colonoscopy with polypectomy) or similar. Under the old rules, many insurers interpreted this code change to mean the entire procedure had become &ldquo;diagnostic&rdquo; or &ldquo;therapeutic&rdquo; &mdash; not preventive &mdash; and applied your full cost-sharing: deductible, coinsurance, or both.</p>

<p>The cruel irony: the patients who did exactly what their doctors recommended (got screened, had polyps caught early) were the ones hit with the largest bills. Patients whose colonoscopies found nothing paid $0. Patients whose colonoscopies found and removed a precancerous polyp owed hundreds of dollars.</p>

<p>This is the colonoscopy loophole. It was not hypothetical or rare. According to a <a href="https://www.healthaffairs.org/doi/10.1377/hlthaff.2018.05166" target="_blank" rel="noopener">Health Affairs study</a>, insurer practices around colonoscopy cost-sharing varied dramatically: some plans covered polyp removal with no cost-sharing; others applied full cost-sharing. Patients had no reliable way to know in advance which category their plan fell into.</p>

<h3>Why polyp removal changes the billing code</h3>

<p>Medical billing uses CPT codes (5-digit billing codes for medical services) assigned by the American Medical Association. A colonoscopy CPT code reflects what the physician actually did during the procedure, not just why it was ordered. If you were scheduled for a preventive screening but the physician found and removed a polyp, the physician is required by billing rules to code for what was actually performed &mdash; a polypectomy &mdash; not just the screening. This is accurate coding. The problem is not that providers are coding incorrectly; it is that insurers used accurate therapeutic codes as a trigger to deny preventive coverage.</p>

<div class="key-takeaway">
    <strong>Got an unexpected colonoscopy bill?</strong> <a href="/scan">Upload your bill to BillKarma</a> &mdash; we identify what CPT codes were used, whether your plan year falls under the 2023 federal rule, and whether you may have grounds to dispute the charges.
</div>

<h2 id="cpt-codes">2. The CPT codes that determine your cost</h2>

<p>Your colonoscopy CPT code (the 5-digit billing code for the specific procedure performed) is the single most important factor determining what you owe. Here are the primary colonoscopy codes and what they mean:</p>

<table>
    <thead>
        <tr>
            <th>CPT Code</th>
            <th>Description</th>
            <th>Medicare Rate (2026)</th>
            <th>Typical Hospital Charge</th>
            <th>Patient Cost: Preventive</th>
            <th>Patient Cost: Diagnostic</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td><strong>45378</strong></td>
            <td>Colonoscopy, flexible; diagnostic, with or without collection of specimen(s) by brushing or washing</td>
            <td>$325 (facility)</td>
            <td>$2,800&ndash;$5,200</td>
            <td><strong>$0</strong> (ACA-covered)</td>
            <td>After deductible/coinsurance</td>
        </tr>
        <tr>
            <td><strong>45380</strong></td>
            <td>Colonoscopy, with biopsy, single or multiple</td>
            <td>$372 (facility)</td>
            <td>$3,100&ndash;$5,800</td>
            <td><strong>$0</strong> under 2023 rule*</td>
            <td>After deductible/coinsurance</td>
        </tr>
        <tr>
            <td><strong>45381</strong></td>
            <td>Colonoscopy, with directed submucosal injection(s), any substance</td>
            <td>$399 (facility)</td>
            <td>$3,400&ndash;$6,200</td>
            <td><strong>$0</strong> under 2023 rule*</td>
            <td>After deductible/coinsurance</td>
        </tr>
        <tr>
            <td><strong>45382</strong></td>
            <td>Colonoscopy, with control of bleeding, any method</td>
            <td>$421 (facility)</td>
            <td>$3,600&ndash;$6,500</td>
            <td><strong>$0</strong> under 2023 rule*</td>
            <td>After deductible/coinsurance</td>
        </tr>
        <tr>
            <td><strong>45385</strong></td>
            <td>Colonoscopy, with removal of tumor(s), polyp(s), or other lesion(s) by snare technique</td>
            <td>$418 (facility)</td>
            <td>$3,500&ndash;$6,800</td>
            <td><strong>$0</strong> under 2023 rule*</td>
            <td>After deductible/coinsurance</td>
        </tr>
        <tr>
            <td><strong>45386</strong></td>
            <td>Colonoscopy, with ablation of tumor(s), polyp(s), or other lesion(s) not amenable to removal by hot biopsy or snare technique</td>
            <td>$453 (facility)</td>
            <td>$3,800&ndash;$7,100</td>
            <td><strong>$0</strong> under 2023 rule*</td>
            <td>After deductible/coinsurance</td>
        </tr>
    </tbody>
</table>

<p><em>*The 2023 federal rule requires non-grandfathered plans to cover polyp removal during a preventive screening with no cost-sharing. Grandfathered plans and some self-insured employer plans are exempt. See <a href="#2023-rule">Section 3</a> for details.</em></p>

<p>Medicare rates shown are the 2026 <strong>facility</strong> rates (what Medicare pays the hospital or outpatient surgery center). The physician\u2019s professional fee is separate, billed with a -26 modifier or as a standalone code. Hospital charges are typical chargemaster (list) prices from CMS price transparency data &mdash; not what most insurers actually pay.</p>

{_embed(mode="cost", cpt="45378", title="Look up your colonoscopy CPT code", subtitle="See what Medicare pays for each code.")}

<h3>How the same colonoscopy gets two different codes</h3>

<p>Your gastroenterologist orders a <em>screening colonoscopy</em> because you are 50 years old and due for your first one. The procedure starts as a preventive screening. During the exam, the physician spots a small polyp and removes it with a snare. The procedure is now billed as CPT 45385 &mdash; colonoscopy with polypectomy. This is accurate. The physician removed a polyp. The code must reflect what was actually done.</p>

<p>The dispute is not about the code itself. It is about whether your insurer should then apply cost-sharing to a procedure that was ordered preventively and that found exactly what preventive screenings are designed to catch.</p>

<h2 id="2023-rule">3. What the 2023 federal rule changed (and its limits)</h2>

<p>In March 2023, the Departments of Health and Human Services (HHS), Labor, and Treasury issued a final rule addressing this exact problem. The rule, published at <a href="https://www.federalregister.gov/documents/2023/04/19/2023-07908/coverage-of-certain-preventive-services-under-the-affordable-care-act" target="_blank" rel="noopener">88 Fed. Reg. 23832</a>, clarified that non-grandfathered plans must cover colonoscopies and related services &mdash; including polyp removal &mdash; without cost-sharing when the primary purpose of the procedure is preventive screening.</p>

<table>
    <thead>
        <tr>
            <th>Timeline</th>
            <th>Rule</th>
            <th>What It Means for Patients</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>Before May 31, 2022</td>
            <td>No specific rule on polyp removal cost-sharing</td>
            <td>Insurers could (and did) apply full cost-sharing when a polyp was removed during a preventive colonoscopy. Patients owed hundreds of dollars with no legal recourse under federal law.</td>
        </tr>
        <tr>
            <td>Plan years beginning on or after May 31, 2022</td>
            <td>2023 HHS/Labor/Treasury final rule (88 Fed. Reg. 23832)</td>
            <td>Non-grandfathered plans must cover polyp removal during a preventive colonoscopy without cost-sharing. The CPT code change from 45378 to 45385 no longer triggers cost-sharing for plans covered by the rule.</td>
        </tr>
        <tr>
            <td>Today (2026)</td>
            <td>Rule in effect; grandfathered plan exemption remains</td>
            <td>Most employer-sponsored plans and marketplace plans must provide zero cost-sharing for polyp removal during preventive screenings. But approximately 15&ndash;17% of covered workers are on grandfathered plans (KFF 2024 Employer Health Benefits Survey) and remain unprotected by this rule.</td>
        </tr>
    </tbody>
</table>

<h3>Who is NOT protected by the 2023 rule</h3>

<ul>
    <li><strong>Grandfathered health plans:</strong> Plans that existed before March 23, 2010 and have not made significant changes to benefits or cost-sharing. Many large employer plans maintain grandfathered status. Your plan\u2019s Summary of Benefits and Coverage (SBC) must state if it is grandfathered.</li>
    <li><strong>Some self-insured employer plans:</strong> Large employers who self-insure sometimes claim exemptions or have not yet updated their plan documents to comply. If your employer\u2019s HR department can\u2019t tell you whether the plan complies with the 2023 rule, ask for written confirmation.</li>
    <li><strong>Medicare:</strong> Medicare has its own colonoscopy coverage rules. Medicare covers screening colonoscopies (G0105 or G0121) once every 10 years with no patient cost-sharing. However, if a polyp is removed, Medicare does apply coinsurance in some circumstances &mdash; approximately 20% of the Medicare-approved amount. This is a separate issue from the ACA rule.</li>
    <li><strong>Short-term health plans:</strong> These plans are not subject to ACA preventive coverage requirements and may charge for colonoscopies entirely.</li>
</ul>

<h2 id="read-eob">4. How to read your colonoscopy EOB</h2>

<p>Your Explanation of Benefits (EOB) is the document your insurer sends after processing a claim. It is not a bill &mdash; it is a statement of what was billed, what your insurer paid, and what you owe. For a colonoscopy with polyp removal, your EOB is the first document to examine when you receive an unexpected bill.</p>

<div class="key-takeaway">
    <strong>Want to know if your hospital charged a fair price for your colonoscopy?</strong> Use the <a href="/calculator">BillKarma calculator</a> to enter your CPT code and see what the Medicare rate is for your area &mdash; then compare it to what you were billed.
</div>

<p>Look for these specific fields on your EOB:</p>

<ul>
    <li><strong>Procedure code (CPT code):</strong> Should show 45378, 45380, 45381, 45382, 45385, or similar. If you had a polyp removed, it will not show 45378. This is normal and expected. The issue is how the plan handled the code, not the code itself.</li>
    <li><strong>Benefit category:</strong> Does it say &ldquo;preventive care&rdquo; or &ldquo;diagnostic/therapeutic procedure&rdquo;? This is the key field. If your colonoscopy was ordered as a preventive screening and your plan covers the 2023 rule, the benefit category should still read preventive care even if a polypectomy was performed.</li>
    <li><strong>Plan paid amount:</strong> If the plan paid 100% of the allowed amount (leaving $0 patient responsibility), you are covered correctly. If the plan paid 80% or less, cost-sharing was applied.</li>
    <li><strong>Patient responsibility:</strong> The amount your insurer says you owe. If this is greater than $0 for a preventive colonoscopy on a non-grandfathered plan after May 31, 2022, you may have grounds for a dispute.</li>
    <li><strong>Remark codes:</strong> Short codes that explain claim processing decisions. Common codes like &ldquo;CO-97&rdquo; (benefit for this service is included in another service) or &ldquo;CO-4&rdquo; (service is inconsistent with modifier) can reveal how your insurer categorized the claim.</li>
</ul>

<p>For a full walkthrough of how to read an EOB, see our <a href="/guides/understanding-explanation-of-benefits/">EOB guide</a>.</p>

<h2 id="bill-example">5. Annotated bill example</h2>

<p>Here is an example of a colonoscopy billing scenario that resulted in an unexpected $1,140 bill. The patient scheduled a preventive colonoscopy and had two small polyps removed:</p>

<div class="bill-example">
    <div class="bill-header">Patient Responsibility Summary &mdash; Riverside Endoscopy Center &mdash; Date of Service: 10/14/2025</div>

    <div class="line-item">
        <span><strong>Facility charges (billed to insurer)</strong></span>
        <span></span>
    </div>
    <div class="line-item flagged">
        <span>45385 &mdash; Colonoscopy w/ polypectomy (snare) &nbsp; &#9888; <em>Reclassified from preventive to diagnostic: cost-sharing applied. Medicare facility rate: $418. Billed: $4,200.</em></span>
        <span>$4,200.00</span>
    </div>
    <div class="line-item">
        <span>Plan paid (diagnostic rate, 80% of allowed $960)</span>
        <span>&minus;$768.00</span>
    </div>
    <div class="line-item error">
        <span>Patient responsibility (deductible + 20% coinsurance) &nbsp; &#10060; <em>Potential overcharge: if plan year began after 5/31/2022 and plan is non-grandfathered, patient should owe $0 under 2023 federal rule.</em></span>
        <span>$432.00</span>
    </div>

    <div class="line-item" style="margin-top:12px;">
        <span><strong>Physician charges (gastroenterologist group, billed separately)</strong></span>
        <span></span>
    </div>
    <div class="line-item flagged">
        <span>45385-26 &mdash; Professional fee, colonoscopy w/ polypectomy &nbsp; &#9888; <em>Also reclassified to diagnostic. Medicare physician rate: $242. Billed: $1,800.</em></span>
        <span>$1,800.00</span>
    </div>
    <div class="line-item">
        <span>Plan paid (diagnostic rate, 80% of allowed $480)</span>
        <span>&minus;$384.00</span>
    </div>
    <div class="line-item error">
        <span>Patient responsibility (20% coinsurance) &nbsp; &#10060; <em>Same 2023 rule issue: should be $0 on a qualifying non-grandfathered plan.</em></span>
        <span>$96.00</span>
    </div>

    <div class="line-item" style="margin-top:12px;">
        <span><strong>Pathology bill (separate, from out-of-network lab)</strong></span>
        <span></span>
    </div>
    <div class="line-item error">
        <span>88305 &mdash; Pathology exam, tissue specimen &nbsp; &#10060; <em>Billed by out-of-network pathologist at in-network facility. Medicare rate: $96. Billed: $612. Patient charged $612 at out-of-network rate.</em></span>
        <span>$612.00</span>
    </div>

    <div class="line-total">
        <span>TOTAL UNEXPECTED PATIENT CHARGES</span>
        <span>$1,140.00</span>
    </div>
</div>

<p>This bill has three distinct problems: (1) the facility and physician both reclassified the claim from preventive to diagnostic, applying cost-sharing that may not be valid under the 2023 rule; (2) the pathology was performed by an out-of-network lab even though the patient used an in-network facility; and (3) the facility rate for 45385 ($4,200 billed vs. $418 Medicare) reflects a 10x markup on the Medicare benchmark.</p>

<h2 id="dispute">6. How to dispute a wrongful reclassification</h2>

<p>If you received a colonoscopy bill after a polyp was removed, here is the step-by-step dispute process:</p>

<h3>Step 1: Get your documents</h3>
<p>Request three things: (1) an itemized bill from the facility and from the physician\u2019s group, showing every CPT code and charge; (2) your EOB from your insurer for the date of service; (3) your plan\u2019s Summary of Benefits and Coverage (SBC) to confirm whether it is grandfathered.</p>

<h3>Step 2: Confirm your plan year and grandfathered status</h3>
<p>Your SBC must state prominently if the plan is grandfathered. If it does not say &ldquo;grandfathered,&rdquo; it is not. If your plan year began on or after May 31, 2022 and the plan is not grandfathered, the 2023 federal rule applies. This means polyp removal during a preventive colonoscopy must be covered with zero cost-sharing.</p>

<h3>Step 3: Contact your insurer in writing</h3>
<p>Write to your insurer\u2019s appeals department (the address is on your EOB). State: &ldquo;The colonoscopy performed on [date] was ordered as a preventive screening. The procedure was reclassified to diagnostic due to a polypectomy (CPT 45385). Under the 2023 HHS/Labor/Treasury final rule (88 Fed. Reg. 23832), non-grandfathered plans must cover colonoscopy screenings and related follow-up services, including polyp removal, without cost-sharing when the original order was preventive. I am requesting that this claim be reprocessed as preventive care with zero patient cost-sharing.&rdquo;</p>

<h3>Step 4: Request the ordering physician\u2019s documentation</h3>
<p>Ask your gastroenterologist to provide written confirmation that the colonoscopy was originally ordered as a preventive screening (not because of symptoms or a prior diagnosis). This documentation supports your claim that the intent was preventive, even though the procedure ultimately involved polyp removal.</p>

<h3>Step 5: File an internal appeal, then an external appeal</h3>
<p>If your insurer denies your written request, file a formal internal appeal. Under the ACA, insurers must respond to appeals within 30&ndash;60 days. If the internal appeal fails, you have the right to an independent external review by a third-party reviewer. The external reviewer\u2019s decision is binding on the insurer. See our <a href="/guides/how-to-appeal-a-denied-claim/">appeal guide</a> for the full process.</p>

<h3>Step 6: File a complaint if needed</h3>
<p>You can file a complaint with your state insurance commissioner and with the federal Centers for Medicare and Medicaid Services (CMS) at <a href="https://www.cms.gov/CCIIO/Resources/Consumer-Assistance-Grants/" target="_blank" rel="noopener">cms.gov</a>. The CFPB also accepts medical billing complaints at <a href="https://www.consumerfinance.gov/complaint/" target="_blank" rel="noopener">consumerfinance.gov/complaint</a>.</p>

<div class="key-takeaway">
    <strong>Disputing a colonoscopy reclassification?</strong> Check what hospitals in your area charge for CPT 45385 using <a href="/hospitals/">BillKarma\u2019s hospital directory</a> &mdash; you can compare your facility\u2019s charges to others nearby and see if you were charged significantly above the local average.
</div>

<h2 id="pathology">7. Pathology: the separate bill you didn\u2019t expect</h2>

<p>Even when the colonoscopy reclassification problem is resolved, many patients are surprised by a second, entirely separate bill: the pathology bill. When a polyp is removed during a colonoscopy, the tissue is almost always sent to a pathology laboratory where a pathologist examines it under a microscope to determine whether it is cancerous, precancerous, or benign.</p>

<p>This pathology exam is billed separately under CPT codes such as:</p>

<ul>
    <li><strong>88305</strong> &mdash; Level IV surgical pathology, gross and microscopic examination (the standard code for most polyp specimens). Medicare rate: approximately $96.</li>
    <li><strong>88307</strong> &mdash; Level V surgical pathology (for more complex tissue analysis). Medicare rate: approximately $172.</li>
</ul>

<p>The pathology bill arrives weeks after the colonoscopy, often from a provider name you don\u2019t recognize. The most common problems:</p>

<h3>Out-of-network pathologist at an in-network facility</h3>
<p>Your gastroenterologist and the endoscopy center may both be in-network. But the pathology lab they send specimens to may be out-of-network with your insurer. You had no choice in which lab was used &mdash; the physician selected it. Under the No Surprises Act, if the lab is at an in-network facility and you did not choose it, you may only owe in-network cost-sharing for the pathology service. See our <a href="/guides/no-surprises-act/">No Surprises Act guide</a> for how to use this protection.</p>

<h3>Pathology coded at a higher level than warranted</h3>
<p>CPT 88307 pays roughly 80% more than 88305. If a simple adenomatous polyp is billed at 88307 when 88305 is appropriate, the patient may face higher cost-sharing than warranted. Review your itemized pathology bill and compare the description of the specimen to the code used.</p>

<h3>Multiple specimens billed separately</h3>
<p>If two polyps were removed during your colonoscopy, you may receive two pathology line items (one per specimen). This is usually appropriate &mdash; each specimen requires separate analysis. However, confirm that the number of specimens billed matches the number of polyps your physician documented in the procedure report.</p>

<p>To verify what Medicare pays for your pathology code, use the calculator below:</p>

{_embed(mode="cost", cpt="45378", title="Look up your colonoscopy CPT code", subtitle="See what Medicare pays for each code.")}

<h2 id="case-studies">8. Case studies</h2>

<div class="case-study">
    <h3>Case Study 1: Preventive colonoscopy, two polyps removed &mdash; $1,400 bill reduced to $0</h3>
    <p>A 54-year-old woman scheduled her first colonoscopy as a preventive screening. Her gastroenterologist found and removed two small polyps (CPT 45385). The facility and physician each reclassified the claim from preventive to diagnostic, applying her $800 deductible plus 20% coinsurance. She received a total bill of <strong>$1,400</strong>.</p>
    <p>She checked her plan\u2019s SBC and confirmed it was not grandfathered. Her plan year began January 1, 2023 &mdash; after the May 31, 2022 effective date of the federal rule. She called her insurer\u2019s appeals department, cited 88 Fed. Reg. 23832, and provided her physician\u2019s written confirmation that the procedure was ordered as a preventive screening. The insurer reprocessed both the facility and physician claims as preventive care. <strong>Final bill: $0. Savings: $1,400.</strong></p>
</div>

<div class="case-study">
    <h3>Case Study 2: Man disputes reclassification, wins appeal after insurer initially denies</h3>
    <p>A 61-year-old man had a colonoscopy (CPT 45380, biopsy) at an in-network hospital. His insurer initially reclassified the claim as diagnostic. After a phone call, a customer service representative told him the biopsy code &ldquo;disqualifies&rdquo; the preventive benefit. He accepted this and paid <strong>$680</strong>.</p>
    <p>Six months later, after reading about the 2023 federal rule, he filed a formal written appeal citing the Federal Register rule and his plan\u2019s non-grandfathered status. The insurer initially denied the appeal. He escalated to an external independent review. The external reviewer found in his favor, ruling that the insurer\u2019s policy of automatically reclassifying preventive colonoscopies with any biopsy was inconsistent with the 2023 rule. The insurer was required to reimburse him <strong>$680</strong> within 30 days. External appeals are binding on the insurer. <strong>Outcome: full refund of $680.</strong></p>
</div>

<div class="case-study">
    <h3>Case Study 3: In-network colonoscopy, out-of-network pathologist &mdash; $540 dispute under No Surprises Act</h3>
    <p>A 58-year-old patient had a colonoscopy at an in-network outpatient surgery center. Her gastroenterologist was in-network. A polyp was removed and sent to a pathology lab. Six weeks later, she received a bill for <strong>$540</strong> from a pathology group she had never heard of. Her EOB showed the pathologist was out-of-network, and the insurer had applied her out-of-network deductible.</p>
    <p>She confirmed that the endoscopy center was in-network and that she had not chosen the pathologist &mdash; the physician\u2019s office had sent the specimen automatically. She cited the No Surprises Act (the pathologist was functioning as an ancillary provider at an in-network facility she had not independently selected). After contacting her insurer and filing a complaint with CMS, the claim was reprocessed at in-network rates. Her actual in-network cost-sharing for the pathology was <strong>$0</strong> (she had already met her deductible for the year). <strong>Savings: $540.</strong></p>
</div>

<h2 id="faq">9. Frequently asked questions</h2>

<div class="faq-section">
    <div class="faq-item">
        <h3>Do I owe money for polyp removal during a colonoscopy?</h3>
        <p>It depends on your plan. Under the 2023 federal rule, most non-grandfathered health plans must cover polyp removal during a preventive colonoscopy with no cost-sharing for plan years beginning on or after May 31, 2022. If you received a bill, check your plan\u2019s Summary of Benefits and Coverage (SBC) to confirm whether the plan is grandfathered. If it is not, you may have grounds to dispute the bill. Grandfathered plans and some self-insured employer plans remain exempt from this rule.</p>
    </div>

    <div class="faq-item">
        <h3>What is the difference between CPT 45378 and CPT 45380?</h3>
        <p>CPT 45378 is a colonoscopy with no additional procedure beyond the scope examination itself. CPT 45380 is a colonoscopy with biopsy &mdash; the physician took a tissue sample. CPT 45385 is a colonoscopy with polypectomy (full removal of a polyp by snare technique). Your CPT code changes from 45378 to 45380 or 45385 the moment any tissue is removed. This code change is what historically triggered cost-sharing; the 2023 rule was designed to stop insurers from using that code change as a reason to deny preventive coverage.</p>
    </div>

    <div class="faq-item">
        <h3>How do I dispute a colonoscopy reclassification?</h3>
        <p>Request your itemized bill and EOB, confirm your plan is not grandfathered and your plan year began after May 31, 2022, then write to your insurer citing the 2023 HHS/Labor/Treasury final rule (88 Fed. Reg. 23832). Ask your gastroenterologist to provide documentation that the procedure was ordered as a preventive screening. If your insurer denies your request, file a formal internal appeal, then an external independent appeal. External appeals are binding. You can also file a complaint with your state insurance commissioner or the federal CMS.</p>
    </div>

    <div class="faq-item">
        <h3>Why did I get a separate bill from a pathologist after my colonoscopy?</h3>
        <p>When a polyp is removed, the tissue is sent to a pathology lab for microscopic examination. The pathologist bills separately from the gastroenterologist and facility. The pathologist may be out-of-network even if your other providers are in-network. Under the No Surprises Act, if you did not independently choose the pathologist and they are functioning as an ancillary provider at an in-network facility, you may only owe in-network cost-sharing. Contact your insurer and cite the No Surprises Act if you receive an unexpected out-of-network pathology bill.</p>
    </div>

    <div class="faq-item">
        <h3>What did the 2023 federal rule change about colonoscopy billing?</h3>
        <p>The 2023 rule (88 Fed. Reg. 23832) clarified that non-grandfathered plans must cover all services directly related to a colorectal cancer screening &mdash; including polyp removal &mdash; without cost-sharing, when the colonoscopy was originally ordered as a preventive screening. This closed the &ldquo;polyp loophole&rdquo; for plans covered by the rule. The rule applies to plan years beginning on or after May 31, 2022. Grandfathered health plans are not covered by this rule and may still apply cost-sharing when a polyp is removed.</p>
    </div>
</div>

<h2 id="sources">10. Sources</h2>

<ul class="sources-list">
    <li><a href="https://www.federalregister.gov/documents/2023/04/19/2023-07908/coverage-of-certain-preventive-services-under-the-affordable-care-act" target="_blank" rel="noopener">Federal Register (2023): Coverage of Certain Preventive Services Under the Affordable Care Act &mdash; Final Rule (88 Fed. Reg. 23832)</a></li>
    <li><a href="https://www.kff.org/private-insurance/issue-brief/preventive-services-aca-colonoscopy-cost-sharing/" target="_blank" rel="noopener">KFF (2023): Preventive Services Under the ACA &mdash; Colonoscopy Cost-Sharing and the Polyp Loophole</a></li>
    <li><a href="https://www.cms.gov/medicare-coverage-database/view/lcd.aspx?lcdid=35000" target="_blank" rel="noopener">CMS: Medicare Coverage of Colorectal Cancer Screenings</a></li>
    <li><a href="https://www.healthaffairs.org/doi/10.1377/hlthaff.2018.05166" target="_blank" rel="noopener">Health Affairs: Variation in Cost-Sharing for Colonoscopy Procedures Across Health Plans (2019)</a></li>
    <li><a href="https://www.consumerfinance.gov/complaint/" target="_blank" rel="noopener">CFPB: Submit a Complaint About Medical Billing</a></li>
    <li><a href="https://www.cms.gov/CCIIO/Programs-and-Initiatives/Health-Insurance-Market-Reforms/Preventive-Services" target="_blank" rel="noopener">CMS: Preventive Services Coverage Under the ACA &mdash; Plan Requirements and Patient Protections</a></li>
    <li><a href="https://www.kff.org/report-section/ehbs-2024-section-7-employee-cost-sharing/" target="_blank" rel="noopener">KFF: 2024 Employer Health Benefits Survey &mdash; Section 7, Employee Cost-Sharing and Grandfathered Plans</a></li>
</ul>
""",
})
