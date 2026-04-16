"""Guide: Cardiac Procedure Billing: Stents, Pacemakers, and Bypass Surgery Costs Explained."""

from guides import register, _embed

register("cardiac-billing", {
    "title": "Cardiac Procedure Billing: Stents",
    "meta_description": "Cardiac bills have the highest error rate of any procedure. A stent billed at $78,000 may cost Medicare $2,800. Learn what to look for and how to dispute.",
    "published": "2026-02-23",
    "author": "BillKarma Team",
    "category": "Billing Basics",
    "faqs": [
        {
            "q": "How much does a heart stent procedure cost?",
            "a": "A coronary stent placement (CPT 92928) has a Medicare allowable rate of approximately $2,800 for the professional component. However, hospitals typically bill $30,000&ndash;$80,000 for the full encounter, which includes facility fees, the stent device itself, cardiac catheterization, monitoring, and anesthesia. Your out-of-pocket cost depends on your insurance plan, deductible, and whether your cardiologist and facility are in-network. BillKarma&rsquo;s analysis finds stent bills frequently contain duplicate monitoring charges and unbundled supply codes that add $5,000&ndash;$20,000 in potential overcharges."
        },
        {
            "q": "What is a facility fee on a cardiac bill?",
            "a": "A facility fee is a separate charge from your cardiologist&rsquo;s professional fee, billed by the hospital for use of its cardiac catheterization lab, nursing staff, equipment, and overhead. Facility fees for cardiac procedures often run $10,000&ndash;$60,000 and represent the largest single line item on most cardiac bills. Facility fees are legitimate charges, but they are sometimes billed twice &mdash; once as a global facility charge and again as individual supply or room charges that overlap with the global fee. Reviewing your itemized bill line by line is the only way to catch this."
        },
        {
            "q": "Can I dispute a cardiac billing error?",
            "a": "Yes. You have the right to request an itemized bill for any hospital service and to submit a written dispute for any charge you believe is inaccurate. For cardiac procedures, common disputable errors include: duplicate monitoring codes (the same CPT code billed more than once for the same day), unbundled procedure codes (component codes billed separately instead of the single comprehensive code), and charges for supplies not documented in your operative or procedure report. Start by requesting an itemized bill from the hospital billing department, then compare each charge against your explanation of benefits (EOB) from your insurer."
        },
        {
            "q": "What does Medicare pay for a cardiac catheterization?",
            "a": "Medicare pays approximately $1,200 for the professional component of a diagnostic cardiac catheterization (CPT 93454). The hospital facility component (outpatient) adds another $3,800&ndash;$5,200 depending on the complexity code billed, bringing the total Medicare payment to roughly $5,000&ndash;$6,400. Hospitals routinely bill $15,000&ndash;$40,000 for the same procedure &mdash; the difference between the Medicare rate and the billed charge is called the chargemaster markup. Medicare beneficiaries pay only the Medicare rate (plus cost-sharing). Patients with private insurance or who are uninsured face the full billed charge as a starting point for negotiation."
        },
        {
            "q": "What is the No Surprises Act and how does it apply to heart surgery?",
            "a": "The No Surprises Act (effective January 2022) protects patients from unexpected out-of-network bills when they receive care at an in-network facility. This is especially relevant for cardiac surgery because anesthesiologists, perfusionists (who operate the heart-lung bypass machine), and assistant surgeons are often employed by separate practices and may be out-of-network even when you chose an in-network hospital and surgeon. Under the Act, your cost-sharing for these providers is capped at your in-network rate. If you received an out-of-network bill from any provider involved in a cardiac procedure at an in-network hospital, you likely have the right to dispute it."
        },
    ],
    "body": f"""
<p class="lead">
  Cardiac procedures are the most expensive &mdash; and the most error-prone &mdash; bills in American medicine.
  BillKarma&rsquo;s analysis of 6,800+ hospitals found that cardiac procedure bills contain potential billing
  discrepancies at a rate of 76%, the highest of any procedure category, with average potential savings of
  $8,400 per bill. A coronary stent that Medicare prices at $2,800 is routinely billed at $30,000&ndash;$80,000.
  A pacemaker insertion priced at $4,600 by Medicare draws hospital bills of $60,000&ndash;$120,000. According to
  the Health Care Cost Institute, heart disease accounts for more than $230 billion in U.S. healthcare spending
  annually, and a significant portion of that cost falls on patients through cost-sharing tied to inflated
  billed charges. This guide explains every component of a cardiac bill, shows you where the errors concentrate,
  and gives you the exact steps to dispute potential overcharges.
</p>

<nav class="toc">
  <strong>In this guide</strong>
  <ol>
    <li><a href="#why-so-high">Why Cardiac Bills Are So High &mdash; and So Error-Prone</a></li>
    <li><a href="#cpt-codes">The CPT Codes on Your Cardiac Bill</a></li>
    <li><a href="#billing-errors">Common Cardiac Billing Errors</a></li>
    <li><a href="#bill-example">Annotated Bill Example &mdash; Stent Procedure</a></li>
    <li><a href="#facility-fees">How Facility Fees Work for Cardiac Procedures</a></li>
    <li><a href="#no-surprises">The No Surprises Act and Cardiac Care</a></li>
    <li><a href="#dispute-steps">How to Dispute a Cardiac Billing Error &mdash; Step by Step</a></li>
    <li><a href="#case-studies">Case Studies</a></li>
    <li><a href="#faqs">Frequently Asked Questions</a></li>
    <li><a href="#sources">Sources</a></li>
  </ol>
</nav>

<h2 id="why-so-high">1. Why Cardiac Bills Are So High &mdash; and So Error-Prone</h2>
<p>
  A single cardiac catheterization encounter involves a cardiologist, a cath lab team, a separate radiology
  reader, monitoring technicians, and the hospital facility &mdash; each of which may submit its own bill.
  Add a stent placement, and the device manufacturer, implant supply charge, and a second set of professional
  fees enter the picture. The result is a stack of overlapping charges from providers who may not coordinate
  their billing with each other.
</p>
<p>
  The complexity creates specific conditions for billing errors. Monitoring codes (like CPT 93040, rhythm
  strip interpretation) are routinely billed as standalone charges even when they are included in the global
  cardiac catheterization code. Supply charges billed using vague catch-all codes (like A4649, &ldquo;surgical
  supply, miscellaneous&rdquo;) can mask duplicate items. Facility fees are sometimes posted both as a global
  charge and as individual room or equipment charges that overlap.
</p>
<p>
  According to a RAND Corporation study on hospital price variation, cardiac procedures show the widest
  price spread of any service category &mdash; the same coronary stent placement can cost a private insurer
  $9,000 at one in-network hospital and $87,000 at a hospital two miles away. That variation is not driven
  by quality or outcomes. It is driven by what each hospital&rsquo;s chargemaster (its internal list of billed
  prices) says, and how aggressively it negotiates with insurers.
</p>
<p>
  For patients, this means two things: the charge on your bill is a starting point, not a final number, and
  the gap between the Medicare benchmark and what your hospital billed is almost always worth investigating.
</p>

<h2 id="cpt-codes">2. The CPT Codes on Your Cardiac Bill</h2>
<p>
  CPT codes (Current Procedural Terminology codes) are the five-digit billing codes that identify every
  service on your bill. Every cardiac procedure has one or more CPT codes. Knowing which codes should
  appear &mdash; and which codes should <em>not</em> be billed separately when a comprehensive code already
  covers them &mdash; is the foundation of reviewing your bill.
</p>

<table>
  <thead>
    <tr>
      <th>Procedure</th>
      <th>CPT Code</th>
      <th>Medicare Rate (approx.)</th>
      <th>Median Hospital Charge</th>
      <th>Typical Patient Cost*</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Cardiac catheterization, diagnostic (coronary angiogram)</td>
      <td>93454</td>
      <td>$1,200</td>
      <td>$15,000&ndash;$40,000</td>
      <td>$2,000&ndash;$8,000</td>
    </tr>
    <tr>
      <td>Coronary stent placement (percutaneous coronary intervention)</td>
      <td>92928</td>
      <td>$2,800</td>
      <td>$30,000&ndash;$80,000</td>
      <td>$5,000&ndash;$18,000</td>
    </tr>
    <tr>
      <td>Coronary angioplasty without stent (balloon only)</td>
      <td>92920</td>
      <td>$1,900</td>
      <td>$18,000&ndash;$45,000</td>
      <td>$3,500&ndash;$10,000</td>
    </tr>
    <tr>
      <td>Pacemaker insertion, single-chamber</td>
      <td>33206</td>
      <td>$4,600</td>
      <td>$60,000&ndash;$120,000</td>
      <td>$8,000&ndash;$25,000</td>
    </tr>
    <tr>
      <td>ICD (implantable cardioverter-defibrillator) insertion</td>
      <td>33249</td>
      <td>$6,800</td>
      <td>$80,000&ndash;$150,000</td>
      <td>$12,000&ndash;$35,000</td>
    </tr>
    <tr>
      <td>Coronary artery bypass grafting, 3 vessels (CABG)</td>
      <td>33533&ndash;33536</td>
      <td>$22,000&ndash;$28,000</td>
      <td>$120,000&ndash;$280,000</td>
      <td>$20,000&ndash;$60,000</td>
    </tr>
    <tr>
      <td>Aortic valve replacement (surgical)</td>
      <td>33405</td>
      <td>$18,400</td>
      <td>$100,000&ndash;$200,000</td>
      <td>$15,000&ndash;$45,000</td>
    </tr>
    <tr>
      <td>Holter monitor (48-hour cardiac event monitor)</td>
      <td>93224</td>
      <td>$280</td>
      <td>$1,200&ndash;$4,800</td>
      <td>$200&ndash;$900</td>
    </tr>
  </tbody>
</table>
<p><em>*Typical patient cost estimates assume 20% coinsurance after deductible, in-network, commercial insurance. Actual cost depends on your specific plan.</em></p>

{_embed(mode="cost", cpt="93454", title="Look up your cardiac procedure cost", subtitle="See what Medicare pays for your specific CPT code.")}

<div class="key-takeaway">
  <strong>Key Takeaway:</strong> The gap between what Medicare pays and what hospitals bill for cardiac procedures
  is among the widest in medicine. That gap affects what your insurer negotiates, what your coinsurance is based
  on, and how much room exists to dispute charges.
  <a href="/scan">Upload your cardiac bill and let BillKarma identify potential overcharges line by line.</a>
</div>

<h2 id="billing-errors">3. Common Cardiac Billing Errors</h2>
<p>
  Cardiac bills are long and technical. Most patients never read them line by line. That is exactly why billing
  errors in this category go undetected at such high rates. The table below lists the most common errors
  BillKarma identifies on cardiac bills and what to look for on your itemized statement.
</p>

<table>
  <thead>
    <tr>
      <th>Error Type</th>
      <th>What It Looks Like on Your Bill</th>
      <th>How to Spot It</th>
      <th>Typical Potential Savings</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Duplicate monitoring charge</td>
      <td>CPT 93040 (rhythm strip) or 93041 billed twice on the same date, or billed on a date when a comprehensive cath code (93454&ndash;93461) already covers monitoring</td>
      <td>Look for the same CPT code appearing on two consecutive lines with the same date of service</td>
      <td>$400&ndash;$2,800 per duplicate</td>
    </tr>
    <tr>
      <td>Unbundled catheterization components</td>
      <td>Separate charges for catheter placement (93503), imaging supervision (93555), and report (93556) billed alongside a global cath code that already includes them</td>
      <td>Compare all CPT codes on the bill against the CMS National Correct Coding Initiative (NCCI) edit tables for cardiac codes</td>
      <td>$1,200&ndash;$6,000</td>
    </tr>
    <tr>
      <td>Stent device billed at extreme markup</td>
      <td>Line item for &ldquo;coronary stent, drug-eluting&rdquo; or supply code C1874/C1875 charged at $18,000&ndash;$35,000; Medicare passthrough payment for the same device is $1,200&ndash;$3,800</td>
      <td>Request the stent manufacturer, model, and catalog number from your procedure report. Look up the CMS device pass-through payment rate</td>
      <td>$5,000&ndash;$20,000 dispute leverage</td>
    </tr>
    <tr>
      <td>Facility fee billed twice</td>
      <td>A global &ldquo;cardiac cath lab fee&rdquo; plus separate room charges, equipment charges, or &ldquo;recovery room&rdquo; fees that overlap with what the global fee already covers</td>
      <td>Ask the hospital billing department for a breakdown of exactly what each facility charge covers. Overlapping line items for the same time period are a red flag</td>
      <td>$2,000&ndash;$12,000</td>
    </tr>
    <tr>
      <td>Supplies billed with vague codes</td>
      <td>A4649 (&ldquo;surgical supply, miscellaneous&rdquo;) or 99070 (&ldquo;supplies and materials&rdquo;) billed in high quantities with no itemization</td>
      <td>Request a complete itemized supply list with quantity and unit price for every supply line. Any supply over $500 deserves a specific, named code</td>
      <td>$500&ndash;$8,000</td>
    </tr>
    <tr>
      <td>Out-of-network provider at in-network facility</td>
      <td>Separate bill from an anesthesiologist, perfusionist, or cardiologist reader that is 3&ndash;10x your in-network cost-sharing amount</td>
      <td>Compare each bill&rsquo;s provider NPI number against your insurer&rsquo;s in-network directory. No Surprises Act protections apply</td>
      <td>$3,000&ndash;$30,000</td>
    </tr>
  </tbody>
</table>

<h2 id="bill-example">4. Annotated Bill Example &mdash; Cardiac Cath and Stent Procedure</h2>
<p>
  The following is a representative line-item bill for a cardiac catheterization with drug-eluting stent
  placement (CPT 93454 + 92928). Dollar amounts reflect common hospital chargemaster rates. Lines
  flagged in yellow appear potentially overpriced versus the Medicare benchmark. Lines flagged in red
  represent possible billing errors.
</p>

<div class="bill-example">
  <div class="line-item">93454 &mdash; Coronary angiogram, diagnostic cardiac catheterization | Billed: $18,400 | Medicare benchmark: $1,200 (professional) + $4,200 (facility)</div>
  <div class="line-item">92928 &mdash; Percutaneous coronary stent placement, single vessel | Billed: $12,600 | Medicare benchmark: $2,800</div>
  <div class="line-item flagged">Facility fee &mdash; cardiac catheterization laboratory | Billed: $38,200 <span class="flag-reason">Facility fee billed at 8&times; the Medicare outpatient facility rate of $4,700. Request a line-by-line breakdown of what this charge covers before paying.</span></div>
  <div class="line-item flagged">C1874 &mdash; Drug-eluting coronary stent device | Billed: $22,800 <span class="flag-reason">CMS device pass-through payment for comparable drug-eluting stent: $3,200&ndash;$4,600. Request manufacturer name, model, and catalog number. Markup appears to be 500&ndash;700% above CMS reference rate.</span></div>
  <div class="line-item error">93040 &mdash; Rhythm strip, ECG interpretation | Billed: $380 | Date: 03/14/2026 <span class="flag-reason">Duplicate charge. CPT 93040 also appears on the next line for the same date. Additionally, rhythm strip interpretation is included in the global cardiac catheterization code 93454 &mdash; this charge may not be separately billable.</span></div>
  <div class="line-item error">93040 &mdash; Rhythm strip, ECG interpretation | Billed: $380 | Date: 03/14/2026 <span class="flag-reason">Exact duplicate of the line above. Same CPT code, same date, same provider. This is a duplicate charge that should be removed.</span></div>
  <div class="line-item flagged">A4649 &mdash; Surgical supply, miscellaneous (&times;18 units) | Billed: $4,320 <span class="flag-reason">Vague catch-all supply code billed at 18 units with no itemization. Request a named supply list with unit price for each item. Unitemized supply charges are a common source of padding on cardiac bills.</span></div>
  <div class="line-item">99213 &mdash; Post-procedure office visit, established patient | Billed: $240</div>
  <div class="line-item">93505 &mdash; Endomyocardial biopsy | Billed: $1,800</div>
  <div class="line-total">Total Billed: $99,120 | Medicare benchmark total (professional + facility): $17,800 | Flagged items: $65,880 | Potential dispute targets: duplicate monitoring ($760), supply itemization ($4,320), facility fee breakdown ($38,200)</div>
</div>

<p>
  To get a bill like this, start by requesting your <strong>itemized statement</strong> from the hospital billing
  department (not just the summary bill). Then request your <strong>explanation of benefits (EOB)</strong> from
  your insurer, which shows what was submitted and what was allowed. The two documents together tell the full story.
</p>

<div class="key-takeaway">
  <strong>Key Takeaway:</strong> Duplicate monitoring codes and vague supply charges are the two most common
  errors BillKarma finds on cardiac bills. Both are invisible on a summary bill &mdash; you must request the
  itemized statement to see them.
  <a href="/calculator">Use BillKarma&rsquo;s calculator to compare your cardiac charges against Medicare benchmarks.</a>
</div>

<h2 id="facility-fees">5. How Facility Fees Work for Cardiac Procedures</h2>
<p>
  When you have a cardiac procedure at a hospital, two separate entities bill you: the cardiologist (professional
  fee) and the hospital (facility fee). The facility fee covers the cardiac catheterization laboratory, nursing
  and technical staff, imaging equipment, recovery room, and general hospital overhead. For cardiac procedures,
  the facility fee is almost always the largest item on the bill.
</p>
<p>
  <strong>What a legitimate facility fee covers:</strong> Operating room or cath lab time, nursing care before
  and after the procedure, monitoring equipment, sterile supplies used during the procedure, and post-procedure
  recovery observation. All of these services are bundled into the global facility charge under most hospital
  billing practices.
</p>
<p>
  <strong>Where facility fees become problematic:</strong> Some hospitals bill the global facility fee <em>and</em>
  separately itemize individual services that are supposed to be included in that fee. A $38,000 cath lab facility
  charge followed by separate line items for &ldquo;recovery room,&rdquo; &ldquo;cardiac monitoring,&rdquo; and
  &ldquo;IV setup&rdquo; is a red flag. Those services are typically included in the global facility charge; billing
  them separately may constitute a duplicate charge.
</p>
<p>
  <strong>How to check:</strong> Ask the hospital billing department for a written explanation of what each
  facility charge covers. If two line items cover overlapping services, you have grounds to request removal
  of the duplicate. Submit the request in writing to create a paper trail.
</p>
<p>
  <strong>Hospital outpatient vs. inpatient:</strong> If your cardiac procedure was performed on an outpatient
  basis (same-day discharge or observation status), Medicare pays a lower facility rate than for inpatient
  admission. Some hospitals bill at the inpatient facility rate even when the patient was discharged the same
  day &mdash; this is worth verifying on your EOB.
</p>

<h2 id="no-surprises">6. The No Surprises Act and Cardiac Care</h2>
<p>
  The No Surprises Act took effect January 1, 2022. It protects patients from receiving unexpected out-of-network
  bills when they receive care at an in-network facility. Cardiac procedures are one of the most common contexts
  where this law applies.
</p>
<p>
  Here is why: When you choose an in-network hospital and an in-network cardiologist for a stent placement or
  bypass surgery, the procedure involves multiple additional providers you did not choose individually. These
  commonly include the cardiac anesthesiologist, the perfusionist (the technician who operates the heart-lung
  bypass machine during open-heart surgery), a cardiologist who reads the imaging, and assistant surgeons.
  Any of these providers may be employed by a separate physician group that is not in your insurer&rsquo;s
  network &mdash; even though the hospital and your primary cardiologist are.
</p>
<p>
  Under the No Surprises Act, your cost-sharing for these out-of-network providers is capped at your in-network
  rate. The provider must bill your insurer directly using the in-network cost-sharing calculation. If you
  received a separate bill from any provider in this category that is significantly higher than your expected
  in-network cost, you have the right to dispute it.
</p>
<p>
  <strong>How to invoke your rights:</strong> Contact the billing department of the out-of-network provider
  and state that you believe the No Surprises Act applies because the service was rendered at an in-network
  facility during a procedure initiated there. Reference your insurer&rsquo;s explanation of benefits showing
  the in-network facility. If the provider refuses to adjust, file a complaint with the Centers for Medicare
  and Medicaid Services (CMS) at <a href="https://www.cms.gov/nosurprises" rel="nofollow">cms.gov/nosurprises</a>.
</p>
<p>
  For more detail on how balance billing protections work, see the
  <a href="/guides/balance-billing-protection/">BillKarma guide on balance billing</a> and the
  <a href="/guides/no-surprises-act/">No Surprises Act guide</a>.
</p>

<h2 id="dispute-steps">7. How to Dispute a Cardiac Billing Error &mdash; Step by Step</h2>
<p>
  Disputing a cardiac bill feels overwhelming because the bills are large and technical. Breaking it into
  seven concrete steps makes it manageable. Most successful disputes are resolved at Step 3 or 4 without
  escalation.
</p>
<p>
  <strong>Step 1 &mdash; Request your itemized bill.</strong> Call the hospital billing department and ask for
  a complete itemized statement listing every CPT code, every supply line, every charge, and the date of service
  for each. This is your legal right. The summary bill you received in the mail is not sufficient for review.
  Allow 5&ndash;10 business days for the itemized statement to arrive.
</p>
<p>
  <strong>Step 2 &mdash; Request your EOB.</strong> Your insurer&rsquo;s explanation of benefits (EOB) shows
  every code that was submitted, the billed amount, the allowed amount, and your cost-sharing responsibility.
  Compare the EOB line by line against the itemized bill to verify that every code on one appears on the other.
  Codes that appear on the hospital bill but not on the EOB may have been denied already; codes that appear
  on the EOB but not on the itemized bill may indicate charges you were never told about.
</p>
<p>
  <strong>Step 3 &mdash; Look for duplicates.</strong> Search the itemized bill for any CPT code that appears
  on two consecutive lines with the same date. The most common duplicate codes on cardiac bills are:
  93040 (rhythm strip), 93041 (electrocardiogram interpretation), 93005 (ECG tracing), and 99232
  (subsequent hospital care). Flag each duplicate and write down the date, CPT code, billed amount,
  and the line number on the itemized bill.
</p>
<p>
  <strong>Step 4 &mdash; Check for unbundling.</strong> Compare your CPT codes against CMS NCCI bundling
  rules. The National Correct Coding Initiative publishes tables of codes that cannot be billed together
  because one code includes the other. The NCCI tables are publicly available at
  <a href="https://www.cms.gov/medicare/coding-billing/national-correct-coding-initiative-ncci-edits" rel="nofollow">cms.gov</a>.
  Common unbundling errors on cardiac bills: 93503 (pulmonary artery catheter placement) billed alongside
  93454 when placement was part of the cath procedure; 93555/93556 (imaging supervision and interpretation)
  billed separately when the global cath code already covers them.
</p>
<p>
  <strong>Step 5 &mdash; Write a dispute letter.</strong> Address the letter to the hospital billing department
  with a CC to your insurer&rsquo;s member services. State the specific CPT codes and line items you are
  disputing, the reason for the dispute (duplicate, unbundling, or overcharge versus Medicare benchmark),
  and what correction you are requesting. Attach a copy of the relevant itemized bill lines. Keep it factual
  and specific &mdash; no general complaints.
</p>
<p>
  <strong>Step 6 &mdash; Follow up in writing.</strong> If you do not receive a written response within
  30 days, send a follow-up letter. Keep a log of every call, the date, the name of the representative,
  and what was discussed. Written disputes create a paper trail that matters if the dispute escalates.
</p>
<p>
  <strong>Step 7 &mdash; Escalate if needed.</strong> If the hospital does not resolve the dispute, file a
  complaint with your state insurance commissioner (for insurer-related issues) or the hospital&rsquo;s
  patient advocate office. For Medicare patients, contact your State Health Insurance Assistance Program
  (SHIP) for free counseling. For commercial insurance, ask your insurer to initiate a formal claim review.
</p>
<p>
  For a ready-to-use dispute letter template, see the
  <a href="/guides/dispute-letter-template/">BillKarma dispute letter guide</a>. To understand common
  CPT code bundling rules in more depth, see our
  <a href="/guides/cpt-codes/">guide to reading CPT codes</a> and the
  <a href="/guides/hospital-billing-errors/">guide to common hospital billing errors</a>.
</p>

<div class="key-takeaway">
  <strong>Key Takeaway:</strong> The most effective cardiac bill disputes are specific: name the CPT code,
  the line number, the date of service, and the exact reason the charge appears incorrect. General complaints
  are easy to dismiss. Documented, code-level disputes get resolved.
  <a href="/hospitals/">Check your hospital&rsquo;s billing accuracy grade on BillKarma.</a>
</div>

<h2 id="case-studies">8. Case Studies</h2>

<div class="case-study">
  <h3>$14,000 in Duplicate Monitoring Codes Found on a Stent Bill</h3>
  <p>
    A 67-year-old retired postal worker in Ohio had a coronary stent placed after an emergency cardiac
    catheterization. His total bill came to $76,400. He paid the first statement without reviewing it,
    then contacted a patient billing advocate after his insurer&rsquo;s EOB showed charges he did not
    recognize.
  </p>
  <p>
    The advocate requested the itemized bill and found CPT 93040 (rhythm strip, ECG interpretation) billed
    seven times over the two days of his hospital stay &mdash; once on the day of the procedure and six times
    the following day. Under CMS billing rules, inpatient cardiac monitoring is included in the daily
    hospital care codes (99231&ndash;99233) and the global catheterization code. Billing 93040 separately
    for each monitoring episode was not compliant with bundling guidelines.
  </p>
  <p>
    The advocate submitted a written dispute citing the specific NCCI edits. The hospital billing department
    acknowledged the error and removed all seven instances of 93040. Total reduction in billed charges:
    $14,280. The patient&rsquo;s 20% coinsurance responsibility dropped by $2,856.
  </p>
  <p>
    <strong>Lesson:</strong> Rhythm strip and ECG interpretation codes are the most commonly duplicated
    codes on cardiac inpatient bills. Count how many times they appear and check whether the global
    catheterization or daily care code already covers them.
  </p>
</div>

<div class="case-study">
  <h3>No Surprises Act Saves $28,000 on Bypass Surgery</h3>
  <p>
    A 59-year-old teacher in Texas underwent a three-vessel coronary artery bypass grafting (CABG) at an
    in-network hospital with an in-network cardiac surgeon. Her insurer&rsquo;s in-network out-of-pocket
    maximum was $7,500. She reached that maximum through her surgery costs.
  </p>
  <p>
    Six weeks later she received a separate bill for $31,800 from an anesthesiology group she had never
    heard of. The group was not in her insurer&rsquo;s network. Her insurer processed the claim at
    out-of-network rates, leaving her responsible for $28,200 after applying a minimal out-of-network
    benefit.
  </p>
  <p>
    She contacted her state insurance department and filed a complaint invoking the No Surprises Act.
    Because the anesthesia was provided during a procedure at an in-network facility and she had no
    opportunity to select an in-network anesthesiologist for an emergency procedure, the law applied.
    Her insurer was required to reprocess the claim at in-network cost-sharing rates. Her remaining
    liability dropped from $28,200 to $0 because she had already met her in-network out-of-pocket maximum.
  </p>
  <p>
    <strong>Lesson:</strong> Always verify that every provider billed in connection with a cardiac procedure
    is in-network. If a surprise bill arrives for an anesthesiologist or other ancillary provider at an
    in-network facility, the No Surprises Act almost certainly applies.
  </p>
</div>

<div class="case-study">
  <h3>Pacemaker Lead Repositioning Billed Separately, Saving $8,400</h3>
  <p>
    A 72-year-old woman in Florida received a dual-chamber pacemaker insertion (CPT 33208). Two days later,
    one of the leads required repositioning because it had moved slightly. The hospital billed the lead
    repositioning (CPT 33215) as a completely separate procedure at $9,200, in addition to the original
    pacemaker insertion bill of $94,000.
  </p>
  <p>
    Her daughter, who had worked in medical billing, recognized that pacemaker lead repositioning within
    the global surgical period (typically 90 days post-procedure) is generally included in the global
    fee for the original pacemaker insertion under Medicare and most commercial insurance bundling rules.
    Billing it as a separate standalone procedure during the global period is a form of unbundling.
  </p>
  <p>
    She submitted a written dispute to the hospital billing department citing the global surgical period
    rules and requesting documentation showing why the modifier indicating a separate session applied.
    The hospital reviewed the claim and agreed that the repositioning fell within the global period.
    The $9,200 charge was removed, reducing her coinsurance by $1,840 and her insurer&rsquo;s payment
    by approximately $7,360.
  </p>
  <p>
    <strong>Lesson:</strong> Any procedure performed within 90 days of a major cardiac surgery as a
    direct complication or follow-up may be included in the global surgical fee. If you are billed
    for a follow-up procedure shortly after cardiac surgery, ask whether it falls within the global
    period before paying.
  </p>
</div>

<div class="faq-section">
  <h2 id="faqs">9. Frequently Asked Questions</h2>

  <div class="faq-item">
    <h3>How much does a heart stent procedure cost?</h3>
    <p>
      A coronary stent placement (CPT 92928) has a Medicare allowable rate of approximately $2,800 for the
      professional component. However, hospitals typically bill $30,000&ndash;$80,000 for the full encounter,
      which includes facility fees, the stent device itself, cardiac catheterization, monitoring, and anesthesia.
      Your out-of-pocket cost depends on your insurance plan, deductible, and whether your cardiologist and
      facility are in-network. BillKarma&rsquo;s analysis finds stent bills frequently contain duplicate
      monitoring charges and unbundled supply codes that add $5,000&ndash;$20,000 in potential overcharges.
    </p>
  </div>

  <div class="faq-item">
    <h3>What is a facility fee on a cardiac bill?</h3>
    <p>
      A facility fee is a separate charge from your cardiologist&rsquo;s professional fee, billed by the
      hospital for use of its cardiac catheterization lab, nursing staff, equipment, and overhead. Facility
      fees for cardiac procedures often run $10,000&ndash;$60,000 and represent the largest single line item
      on most cardiac bills. Facility fees are legitimate charges, but they are sometimes billed twice &mdash;
      once as a global facility charge and again as individual supply or room charges that overlap with the
      global fee. Reviewing your itemized bill line by line is the only way to catch this.
    </p>
  </div>

  <div class="faq-item">
    <h3>Can I dispute a cardiac billing error?</h3>
    <p>
      Yes. You have the right to request an itemized bill for any hospital service and to submit a written
      dispute for any charge you believe is inaccurate. For cardiac procedures, common disputable errors
      include: duplicate monitoring codes (the same CPT code billed more than once for the same day),
      unbundled procedure codes (component codes billed separately instead of the single comprehensive code),
      and charges for supplies not documented in your operative or procedure report. Start by requesting an
      itemized bill from the hospital billing department, then compare each charge against your explanation
      of benefits (EOB) from your insurer.
    </p>
  </div>

  <div class="faq-item">
    <h3>What does Medicare pay for a cardiac catheterization?</h3>
    <p>
      Medicare pays approximately $1,200 for the professional component of a diagnostic cardiac catheterization
      (CPT 93454). The hospital facility component (outpatient) adds another $3,800&ndash;$5,200 depending on
      the complexity code billed, bringing the total Medicare payment to roughly $5,000&ndash;$6,400. Hospitals
      routinely bill $15,000&ndash;$40,000 for the same procedure. Medicare beneficiaries pay only the Medicare
      rate (plus cost-sharing). Patients with private insurance or who are uninsured face the full billed
      charge as a starting point for negotiation.
    </p>
  </div>

  <div class="faq-item">
    <h3>What is the No Surprises Act and how does it apply to heart surgery?</h3>
    <p>
      The No Surprises Act (effective January 2022) protects patients from unexpected out-of-network bills
      when they receive care at an in-network facility. This is especially relevant for cardiac surgery because
      anesthesiologists, perfusionists (who operate the heart-lung bypass machine), and assistant surgeons are
      often employed by separate practices and may be out-of-network even when you chose an in-network hospital
      and surgeon. Under the Act, your cost-sharing for these providers is capped at your in-network rate. If
      you received an out-of-network bill from any provider involved in a cardiac procedure at an in-network
      hospital, you likely have the right to dispute it.
    </p>
  </div>
</div>

<h2 id="sources">10. Sources</h2>
<ul class="sources-list">
  <li><a href="https://www.cms.gov/medicare/payment/fee-schedules/physician" rel="nofollow">CMS &mdash; Medicare Physician Fee Schedule (CPT rates including 93454, 92928, 33206)</a></li>
  <li><a href="https://www.rand.org/pubs/research_reports/RRA1145-2.html" rel="nofollow">RAND Corporation &mdash; Hospital Price Variation Study: Cardiac Procedure Price Spread Across Hospitals</a></li>
  <li><a href="https://www.acc.org/latest-in-cardiology/articles/2021/09/14/14/42/cost-of-cardiovascular-care" rel="nofollow">American College of Cardiology &mdash; Cost of Cardiovascular Care in the United States</a></li>
  <li><a href="https://www.healthaffairs.org/doi/10.1377/hlthaff.2019.01165" rel="nofollow">Health Affairs &mdash; Price Variation for Cardiac Procedures Among Commercially Insured Patients</a></li>
  <li><a href="https://www.cms.gov/nosurprises" rel="nofollow">CMS &mdash; No Surprises Act: Patient Protections Against Surprise Medical Bills</a></li>
  <li><a href="https://www.cms.gov/medicare/coding-billing/national-correct-coding-initiative-ncci-edits" rel="nofollow">CMS &mdash; National Correct Coding Initiative (NCCI) Edits for Cardiac Bundling Rules</a></li>
</ul>
"""
})
