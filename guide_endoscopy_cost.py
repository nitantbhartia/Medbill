"""Guide: Endoscopy Cost."""

from guides import register, _embed

register("endoscopy-cost", {
    "title": "Endoscopy Cost in 2026: Upper GI, Lower GI & What Insurance Pays",
    "meta_description": "Upper endoscopy costs $1,500–$6,000; colonoscopy $2,000–$4,500. Learn what insurance covers, how to verify anesthesia is in-network, and common GI billing errors.",
    "published": "2026-04-05",
    "author": "BillKarma Team",
    "category": "Procedure Costs",
    "faqs": [
        {
            "q": "Is an endoscopy covered by insurance?",
            "a": "It depends on why you are having it. A medically necessary endoscopy&mdash;ordered because of symptoms like GERD, bleeding, difficulty swallowing, or unexplained anemia&mdash;is covered as a diagnostic procedure subject to your deductible and coinsurance. A preventive endoscopy for colorectal cancer screening (colonoscopy) is covered at $0 cost-sharing under the ACA. However, if your screening colonoscopy results in a polyp removal, some insurers reclassify it as diagnostic and begin charging cost-sharing. Always verify this policy with your insurer before the procedure.",
        },
        {
            "q": "Why is anesthesia billed separately for an endoscopy?",
            "a": "The anesthesiologist or CRNA who administers sedation for your endoscopy is typically a separate provider from the gastroenterologist performing the procedure. They bill independently using their own codes (anesthesia time units, typically 00740 for upper GI or 00810 for lower GI). If the anesthesia provider is out-of-network while your gastroenterologist and facility are in-network, you may receive a surprise balance bill. Always ask your facility whether the anesthesia providers are in-network with your insurance before scheduling.",
        },
        {
            "q": "Is an ambulatory surgery center cheaper than a hospital for an endoscopy?",
            "a": "Yes, significantly. Ambulatory surgery centers (ASCs) typically charge 35&ndash;50% less than hospital outpatient departments for the same endoscopy procedure. This affects both the facility fee and, in some cases, anesthesia fees. If your procedure is not urgent and you have flexibility in scheduling, asking for an ASC location can substantially reduce your out-of-pocket cost. Your gastroenterologist can often perform the same procedure at either location.",
        },
        {
            "q": "What is the difference between a diagnostic and preventive colonoscopy for billing?",
            "a": "A preventive (screening) colonoscopy is performed when you have no symptoms, as part of routine colorectal cancer screening. Under the ACA, it is covered at $0 cost-sharing. A diagnostic colonoscopy is performed because of symptoms (rectal bleeding, change in bowel habits, abnormal imaging) and is subject to your deductible and coinsurance. The billing trap: if a polyp is found and removed during what started as a preventive colonoscopy, some insurers reclassify the entire procedure as diagnostic, charging you cost-sharing. Laws in some states prohibit this reclassification. Ask your insurer about their policy before you schedule.",
        },
        {
            "q": "What CPT codes are used for endoscopy?",
            "a": "Common endoscopy CPT codes include: 43239 (upper GI endoscopy with biopsy), 43235 (diagnostic EGD), 45378 (diagnostic colonoscopy), 45380 (colonoscopy with biopsy), 45385 (colonoscopy with polypectomy), 44388 (colonoscopy through stoma), and 91110 (capsule endoscopy). Each of these has a different Medicare-allowed amount and different cost-sharing implications. Knowing your CPT code lets you look up the Medicare rate, which is a useful benchmark for what the procedure should cost.",
        },
    ],
    "body": f"""
<p class="lead">Endoscopy is among the most common outpatient procedures in the US&mdash;more than 75 million are performed annually. Yet billing errors affect <strong>29% of endoscopy claims</strong>, according to BillKarma&rsquo;s analysis, most commonly from out-of-network anesthesia charges that patients did not expect. Here is what endoscopy costs with and without insurance in 2026, what your insurance should pay, and how to avoid the most common billing pitfalls.</p>

<nav class="toc">
    <h2>In this guide</h2>
    <ol>
        <li><a href="#cost-by-type">Cost by procedure type</a></li>
        <li><a href="#anesthesia">Anesthesia: the most common surprise charge</a></li>
        <li><a href="#facility-type">Hospital outpatient vs. ambulatory surgery center</a></li>
        <li><a href="#what-insurance-covers">What insurance covers: diagnostic vs. preventive</a></li>
        <li><a href="#billing-errors">Common endoscopy billing errors</a></li>
        <li><a href="#before-scheduling">Questions to ask before scheduling</a></li>
        <li><a href="#cpt-codes">CPT codes and Medicare rates</a></li>
        <li><a href="#faq">Frequently asked questions</a></li>
        <li><a href="#sources">Sources</a></li>
    </ol>
</nav>

<h2 id="cost-by-type">1. Cost by procedure type</h2>

<p>Endoscopy is not one procedure&mdash;it is a family of procedures using a flexible camera to visualize different parts of the GI tract. Costs vary significantly by procedure type, facility, and geography:</p>

<table>
    <thead>
        <tr><th>Procedure</th><th>CPT Code(s)</th><th>Without Insurance</th><th>With Insurance (Est. OOP)</th><th>Medicare Allowable (Approx.)</th></tr>
    </thead>
    <tbody>
        <tr><td><strong>Upper endoscopy (EGD), diagnostic</strong></td><td>43235</td><td>$1,500&ndash;$4,000</td><td>$300&ndash;$1,200</td><td>$285&ndash;$450</td></tr>
        <tr><td><strong>Upper endoscopy with biopsy</strong></td><td>43239</td><td>$2,000&ndash;$6,000</td><td>$400&ndash;$1,800</td><td>$320&ndash;$520</td></tr>
        <tr><td><strong>Colonoscopy, diagnostic</strong></td><td>45378</td><td>$2,000&ndash;$4,500</td><td>$300&ndash;$1,500</td><td>$320&ndash;$480</td></tr>
        <tr><td><strong>Colonoscopy with polypectomy</strong></td><td>45385</td><td>$2,500&ndash;$5,000</td><td>$500&ndash;$2,000</td><td>$420&ndash;$600</td></tr>
        <tr><td><strong>Flexible sigmoidoscopy</strong></td><td>45330</td><td>$1,000&ndash;$3,000</td><td>$200&ndash;$900</td><td>$175&ndash;$280</td></tr>
        <tr><td><strong>Capsule endoscopy</strong></td><td>91110</td><td>$800&ndash;$8,000</td><td>$300&ndash;$2,500</td><td>$650&ndash;$900</td></tr>
    </tbody>
</table>

<p>The wide ranges above reflect geographic variation and facility type. The same diagnostic colonoscopy can cost $800 at an independent ASC in a midwestern city or $4,500 at an academic medical center in a major metro area. Use our <a href="/calculator">cost calculator</a> to look up Medicare-allowed rates for your specific CPT code and ZIP code.</p>

<div class="key-takeaway">
    <strong>Medicare rates as a benchmark:</strong> The Medicare-allowed amount for an endoscopy represents the floor for what a procedure should cost. Provider charges of 5&ndash;10x the Medicare rate are common but not inevitable. If your EOB shows a billed amount dramatically higher than these benchmarks, the procedure was not necessarily more expensive&mdash;it was likely just billed at a higher chargemaster rate before the insurance discount was applied.
</div>

<h2 id="anesthesia">2. Anesthesia: the most common surprise charge</h2>

<p>Most endoscopies use moderate sedation or monitored anesthesia care (MAC). The person administering the sedation&mdash;usually an anesthesiologist or CRNA (certified registered nurse anesthetist)&mdash;is typically a separate provider from the gastroenterologist, and they bill separately.</p>

<p>This creates the most common endoscopy billing problem: <strong>your gastroenterologist and the facility are in-network, but the anesthesia provider is out-of-network.</strong> Under the No Surprises Act, if you had no ability to choose the anesthesia provider (which you typically do not in a GI suite), this out-of-network billing is prohibited. But the bill may still arrive, and you may still need to dispute it.</p>

<div class="bill-example">
    <div class="bill-header">Endoscopy Bill Breakdown &mdash; Colonoscopy at Hospital Outpatient</div>
    <div class="line-item">
        <span>Facility fee (hospital outpatient)</span>
        <span>$3,200.00</span>
    </div>
    <div class="line-item">
        <span>Gastroenterologist professional fee</span>
        <span>$850.00</span>
    </div>
    <div class="line-item">
        <span>Anesthesia (separate bill, may be OON)</span>
        <span>$920.00</span>
    </div>
    <div class="line-item">
        <span>Pathology (if biopsy taken, another separate bill)</span>
        <span>$400.00</span>
    </div>
    <div class="line-total">
        <span>TOTAL BILLED (before insurance)</span>
        <span>$5,370.00</span>
    </div>
</div>

<p>Notice that a &ldquo;$3,200 colonoscopy&rdquo; can generate four separate bills totaling over $5,000. The anesthesia and pathology bills are the ones most likely to surprise patients who thought they had verified their colonoscopy was covered.</p>

<p><strong>How to verify anesthesia network status:</strong> Call your insurer and ask: &ldquo;I am scheduled for a colonoscopy at [facility name] on [date]. Can you tell me which anesthesia groups or CRNAs are in-network at that facility?&rdquo; Then call the facility and ask which anesthesia group they use. Cross-reference the names. If the facility cannot guarantee in-network anesthesia, ask whether you can request a specific in-network provider or whether the procedure can be done at a different location with in-network anesthesia coverage.</p>

<h2 id="facility-type">3. Hospital outpatient vs. ambulatory surgery center</h2>

<p>Where you have your endoscopy is one of the biggest drivers of cost. The procedure is identical; only the billing location changes:</p>

<table>
    <thead>
        <tr><th>Facility Type</th><th>Avg. Facility Fee (Colonoscopy)</th><th>Relative Cost</th><th>Notes</th></tr>
    </thead>
    <tbody>
        <tr><td><strong>Hospital outpatient department</strong></td><td>$2,500&ndash;$4,500</td><td>Highest</td><td>Includes hospital overhead; subject to hospital-specific cost-sharing on some plans</td></tr>
        <tr><td><strong>Ambulatory surgery center (ASC)</strong></td><td>$1,200&ndash;$2,500</td><td>35&ndash;50% less than hospital</td><td>Often same gastroenterologist; lower overhead; may require separate anesthesia verification</td></tr>
        <tr><td><strong>Independent GI center</strong></td><td>$900&ndash;$2,000</td><td>Lowest</td><td>May have narrower network participation; verify insurance acceptance before scheduling</td></tr>
    </tbody>
</table>

<p>The savings from choosing an ASC over a hospital outpatient department are real and can exceed $1,500 per procedure. Most gastroenterologists perform procedures at multiple locations. When you call to schedule, simply ask: &ldquo;Do you also perform procedures at an ambulatory surgery center? Is that location in-network with [insurance plan]? How does the cost compare?&rdquo;</p>

<h2 id="what-insurance-covers">4. What insurance covers: diagnostic vs. preventive</h2>

<p><strong>Medically necessary (diagnostic) endoscopy:</strong> If your endoscopy is ordered because of symptoms&mdash;GERD, GI bleeding, unexplained anemia, difficulty swallowing, abdominal pain&mdash;it is billed as a diagnostic procedure. Your insurance covers it, but it is subject to your deductible and coinsurance. A patient with a $1,500 deductible who has not yet met it will pay the full facility fee up to $1,500 before insurance cost-sharing kicks in.</p>

<p><strong>Preventive colonoscopy (ACA screening):</strong> Under the ACA, colorectal cancer screening colonoscopies are covered at $0 cost-sharing when performed at recommended intervals for average-risk adults (starting at age 45). This is one of the most valuable benefits in American health insurance&mdash;a $3,000+ procedure with no cost to the patient. However, two traps exist:</p>

<ul>
    <li><strong>The polyp trap:</strong> If a polyp is found and removed, some insurers reclassify the entire colonoscopy as &ldquo;diagnostic&rdquo; (CPT 45385 instead of 45378) and apply cost-sharing. Federal law now limits this reclassification for many plan types, but self-funded employer plans and some grandfathered plans may still do it. Verify your plan&rsquo;s policy in writing before the procedure.</li>
    <li><strong>The observation status trap:</strong> If your endoscopy requires a brief hospital admission for monitoring afterward and you are placed in &ldquo;observation status&rdquo; rather than &ldquo;inpatient status,&rdquo; your cost-sharing structure changes significantly. Observation status is billed under outpatient rules and can result in much higher out-of-pocket costs. This is more common with complex upper GI procedures than colonoscopies.</li>
</ul>

{_embed(mode="cost", cpt="45378", title="Look up colonoscopy costs", subtitle="See what Medicare pays for endoscopy procedures in your area.")}

<h2 id="billing-errors">5. Common endoscopy billing errors</h2>

<p>BillKarma identifies billing errors in 29% of endoscopy claims. The most frequent errors:</p>

<ol>
    <li><strong>Out-of-network anesthesia at an in-network facility.</strong> The most common error. Dispute under the No Surprises Act if you did not choose the anesthesia provider. See <a href="/guides/balance-billing">our balance billing guide</a> for the dispute process.</li>
    <li><strong>Wrong facility CPT code.</strong> Hospital outpatient endoscopy uses facility CPT codes with higher reimbursement than ASC codes. If you had your procedure at an ASC but it was billed using hospital outpatient codes, the facility was overbilled, which inflates your cost-sharing.</li>
    <li><strong>Unbundled biopsy charges.</strong> When a biopsy is taken during an endoscopy, it should typically be bundled with the main procedure code (e.g., 43239 includes biopsy). Some providers bill separately for the biopsy on top of the main procedure code, which is improper. Check for duplicate procedure charges on your EOB.</li>
    <li><strong>Pathology billed twice.</strong> If tissue is sent to pathology, the pathologist bills separately. Occasionally, the pathology is billed by both the pathologist and the facility. Look for duplicate line items on your combined bills.</li>
    <li><strong>Preventive colonoscopy reclassified without basis.</strong> If your screening colonoscopy was reclassified as diagnostic and you did not have a polyp removed, this may be a coding error. Request documentation of the specific code change and reason.</li>
</ol>

<h2 id="before-scheduling">6. Questions to ask before scheduling</h2>

<ol>
    <li>Is my gastroenterologist in-network with my insurance plan?</li>
    <li>Is the facility (hospital or ASC) where the procedure will be performed in-network?</li>
    <li>Which anesthesia group or CRNA will administer sedation, and are they in-network?</li>
    <li>If a biopsy is taken, which pathology lab will receive the tissue, and is that lab in-network?</li>
    <li>Can I have this procedure at an ASC instead of the hospital outpatient department to reduce costs?</li>
    <li>Is this procedure being ordered as preventive (screening) or diagnostic? How will it be coded?</li>
    <li>If I am on a high-deductible plan and have not met my deductible, what is the estimated out-of-pocket cost?</li>
</ol>

<h2 id="cpt-codes">7. CPT codes and Medicare rates</h2>

<p>Knowing the CPT code for your procedure lets you look up the Medicare-allowed amount, which is the most widely available benchmark for procedure cost. Medicare pays roughly 20&ndash;30% of what commercial insurers pay, but the relative pricing between procedures is consistent. Here are the key codes:</p>

<table>
    <thead>
        <tr><th>CPT Code</th><th>Description</th><th>Medicare Facility Rate (Approx.)</th></tr>
    </thead>
    <tbody>
        <tr><td>43235</td><td>Upper GI endoscopy (EGD), diagnostic</td><td>$285&ndash;$380</td></tr>
        <tr><td>43239</td><td>Upper GI endoscopy with biopsy</td><td>$320&ndash;$520</td></tr>
        <tr><td>45378</td><td>Colonoscopy, diagnostic</td><td>$320&ndash;$480</td></tr>
        <tr><td>45380</td><td>Colonoscopy with biopsy</td><td>$390&ndash;$540</td></tr>
        <tr><td>45385</td><td>Colonoscopy with polypectomy (snare technique)</td><td>$420&ndash;$600</td></tr>
        <tr><td>91110</td><td>Capsule endoscopy, esophagus through ileum</td><td>$650&ndash;$900</td></tr>
        <tr><td>00740</td><td>Anesthesia for upper GI endoscopy</td><td>$180&ndash;$350 (time-based)</td></tr>
        <tr><td>00810</td><td>Anesthesia for lower GI endoscopy</td><td>$200&ndash;$380 (time-based)</td></tr>
    </tbody>
</table>

<p>If you receive a bill that seems high, <a href="/fight-debt">upload it to BillKarma</a> to compare against Medicare benchmarks and check for common coding errors.</p>

<h2 id="faq">Frequently asked questions</h2>

<div class="faq-section">
    <div class="faq-item">
        <h3>Is an endoscopy covered by insurance?</h3>
        <p>Medically necessary endoscopies are covered as diagnostic procedures, subject to your deductible and coinsurance. Preventive colonoscopies for colorectal cancer screening are covered at $0 cost-sharing under the ACA for average-risk adults starting at age 45. If a polyp is found and removed, some insurers reclassify the colonoscopy as diagnostic and begin charging cost-sharing&mdash;verify your plan&rsquo;s policy before scheduling.</p>
    </div>

    <div class="faq-item">
        <h3>Why is anesthesia billed separately for an endoscopy?</h3>
        <p>The anesthesiologist or CRNA is a separate provider who bills independently. If they are out-of-network while your gastroenterologist and facility are in-network, you may receive a surprise balance bill. Under the No Surprises Act, if you did not choose the anesthesia provider, this out-of-network billing is illegal. Always verify anesthesia network status before your procedure.</p>
    </div>

    <div class="faq-item">
        <h3>Is an ambulatory surgery center cheaper than a hospital for an endoscopy?</h3>
        <p>Yes. ASCs typically charge 35&ndash;50% less than hospital outpatient departments for the same procedure. If you have flexibility in scheduling location, asking your gastroenterologist about ASC availability can save $1,000&ndash;$1,500 or more per procedure.</p>
    </div>

    <div class="faq-item">
        <h3>What is the difference between a diagnostic and preventive colonoscopy for billing?</h3>
        <p>A preventive (screening) colonoscopy is covered at $0 under the ACA. A diagnostic colonoscopy (ordered because of symptoms) is subject to your deductible and coinsurance. The billing trap: if a polyp is removed during a screening colonoscopy, some insurers reclassify it as diagnostic and add cost-sharing. Ask your insurer about this policy before scheduling, especially if you have a high deductible.</p>
    </div>

    <div class="faq-item">
        <h3>What CPT codes are used for endoscopy?</h3>
        <p>Key codes: 43235 (diagnostic EGD), 43239 (EGD with biopsy), 45378 (diagnostic colonoscopy), 45380 (colonoscopy with biopsy), 45385 (colonoscopy with polypectomy), 91110 (capsule endoscopy). Anesthesia uses 00740 (upper GI) and 00810 (lower GI). Knowing your code lets you look up the Medicare-allowed rate as a cost benchmark.</p>
    </div>
</div>

<h2 id="sources">Sources</h2>

<ul class="sources-list">
    <li><a href="#" target="_blank" rel="noopener">American Society for Gastrointestinal Endoscopy: Procedure Cost Data (2025)</a></li>
    <li><a href="#" target="_blank" rel="noopener">Centers for Medicare &amp; Medicaid Services: Physician Fee Schedule 2026</a></li>
    <li><a href="#" target="_blank" rel="noopener">American Cancer Society: Colorectal Cancer Screening Guidelines (2025)</a></li>
    <li><a href="#" target="_blank" rel="noopener">HealthCare.gov: Preventive Care Coverage &mdash; ACA Requirements</a></li>
    <li><a href="#" target="_blank" rel="noopener">CMS: Ambulatory Surgery Center Payment Rates (2026)</a></li>
    <li><a href="#" target="_blank" rel="noopener">BillKarma Internal Data: GI Procedure Billing Error Analysis (2026)</a></li>
</ul>
""",
})
