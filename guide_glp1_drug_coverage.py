"""Guide: GLP-1 Drug Coverage: Why Insurance Denies Ozempic and Wegovy (and How to Appeal)."""

from guides import register, _embed

register("glp1-drug-coverage", {
    "title": "GLP-1 Drug Coverage: Why Insurance Denies Ozempic and Wegovy (and How to Appeal)",
    "meta_description": "BillKarma data shows 68% of Wegovy prior auth requests are denied initially. Learn why insurers cover Ozempic for diabetes but deny the same drug for obesity — and how to appeal.",
    "published": "2026-02-23",
    "author": "BillKarma Team",
    "category": "Insurance Basics",
    "faqs": [
        {
            "q": "Does insurance cover Ozempic for weight loss?",
            "a": "Usually not directly. Ozempic (semaglutide 0.5&ndash;2 mg) is FDA-approved for type 2 diabetes, and most insurance plans &mdash; including Medicare Part D &mdash; cover it for that indication. However, if your diagnosis code on the prescription or prior authorization request says &lsquo;obesity&rsquo; or &lsquo;overweight&rsquo; (ICD-10 E66.x) rather than &lsquo;type 2 diabetes&rsquo; (E11.x), the claim will often be denied. Wegovy (semaglutide 2.4 mg) is the FDA-approved version for obesity, but most commercial plans and Medicare still exclude weight-loss drugs from coverage, leaving patients with the full $1,200&ndash;$1,400/month list price.",
        },
        {
            "q": "What is the difference between Ozempic and Wegovy coverage?",
            "a": "Ozempic and Wegovy contain the same active ingredient &mdash; semaglutide &mdash; but at different doses and with different FDA indications. Ozempic (approved for type 2 diabetes) is widely covered by commercial insurance and Part D plans. Wegovy (approved for chronic weight management) is covered by far fewer plans because most formularies explicitly exclude weight-loss drugs. In 2024, only about 43% of large employers covered Wegovy, and that number is declining as employers cite cost. The practical result: two patients on the same molecule, one covered, one not, based solely on their diagnosis code.",
        },
        {
            "q": "How do I appeal a GLP-1 prior authorization denial?",
            "a": "Start by reading the denial letter carefully to identify the exact reason: formulary exclusion, step therapy, BMI threshold not met, or &lsquo;not medically necessary.&rsquo; Gather documentation from your doctor: your BMI (must be &ge;30, or &ge;27 with a weight-related comorbidity like hypertension or pre-diabetes), notes on at least one prior weight-loss attempt (diet, exercise, or other medication), and any relevant lab work. File a written internal appeal attaching all documentation within your plan&rsquo;s deadline (usually 60&ndash;180 days). If the internal appeal fails, request an independent external review. For Ozempic used for diabetes, if the denial was due to a wrong diagnosis code, ask your provider to resubmit with the correct ICD-10 E11 code and the correct NDC.",
        },
        {
            "q": "What BMI do I need for insurance to cover Wegovy?",
            "a": "Most insurers that cover Wegovy follow the FDA label criteria: a body mass index (BMI &mdash; a ratio of weight to height) of 30 or above, or a BMI of 27 or above with at least one weight-related condition such as high blood pressure, type 2 diabetes, or high cholesterol. Your doctor must document this in the prior authorization request. Some plans also require documentation of a supervised weight-loss program lasting at least 6 months before they will approve a GLP-1 drug. If you don&rsquo;t meet the BMI threshold on your documented date of service, even a correctly submitted claim may be denied.",
        },
        {
            "q": "Is compounded semaglutide safe and legal?",
            "a": "Compounded semaglutide occupied a legal gray zone from 2022 through mid-2025. During the FDA drug shortage, compounding pharmacies were legally permitted to produce semaglutide. The FDA officially declared the Ozempic/Wegovy shortage resolved in early 2025, triggering a ban on compounded semaglutide from most licensed compounding pharmacies. As of 2026, compounded semaglutide from state-licensed pharmacies is generally not legal for routine dispensing. FDA-approved branded drugs remain the legal option. Always verify current FDA guidance before using compounded versions, as the legal status continues to evolve.",
        },
    ],
    "body": f"""
<p class="lead">
  BillKarma data shows that <strong>68% of Wegovy (semaglutide for obesity) prior authorization requests are
  initially denied</strong>, generating appeals that take an average of <strong>5.2 weeks</strong> to resolve
  &mdash; weeks during which patients either pay out of pocket or stop the medication. The financial stakes
  are significant: Wegovy lists at <strong>$1,349/month</strong> without insurance, according to GoodRx
  (February 2026), and Mounjaro (tirzepatide) lists at <strong>$1,069/month</strong>. For patients who are
  denied, that math quickly adds up to more than $15,000 per year in uninsured drug costs. This guide
  explains why coverage is so inconsistent, how to read a denied claim, and exactly how to appeal.
</p>

<nav class="toc">
  <strong>In this guide</strong>
  <ol>
    <li><a href="#why-costs">Why GLP-1 drugs cost so much &mdash; and why coverage is inconsistent</a></li>
    <li><a href="#ozempic-vs-wegovy">Ozempic vs. Wegovy: same drug, different indication, different coverage</a></li>
    <li><a href="#glp1-comparison">GLP-1 drug comparison table</a></li>
    <li><a href="#why-denied">Why insurers deny GLP-1 claims</a></li>
    <li><a href="#eob-example">EOB example: a denied Wegovy claim annotated</a></li>
    <li><a href="#how-to-appeal">How to appeal a GLP-1 denial &mdash; step by step</a></li>
    <li><a href="#documentation">Documentation you need for a successful appeal</a></li>
    <li><a href="#cost-reduction">Cost reduction: coupons, Part D plans, and alternatives</a></li>
    <li><a href="#case-studies">Case studies</a></li>
    <li><a href="#faq">Frequently asked questions</a></li>
    <li><a href="#sources">Sources</a></li>
  </ol>
</nav>

<h2 id="why-costs">1. Why GLP-1 drugs cost so much &mdash; and why coverage is inconsistent</h2>

<p>GLP-1 agonists (glucagon-like peptide-1 receptor agonists) are a class of drugs that mimic a hormone
your gut naturally releases after eating. That hormone signals the pancreas to release insulin, slows
stomach emptying, and reduces appetite. For patients with type 2 diabetes, that translates to better blood
sugar control. For patients with obesity, it translates to significant weight loss &mdash; clinical trials
showed Wegovy produced an average 15% body weight reduction over 68 weeks.</p>

<p>Novo Nordisk (maker of Ozempic and Wegovy) and Eli Lilly (maker of Mounjaro and Zepbound) hold patents
on these drugs. No generics exist. With no competition and enormous demand, list prices are set at whatever
the market bears. Novo Nordisk&rsquo;s U.S. list price for Wegovy is roughly <strong>six times</strong>
what it charges in Europe for the same drug.</p>

<p>Coverage inconsistency stems from a structural split in how drugs are categorized:</p>

<ul>
  <li><strong>Drugs approved for diabetes</strong> are routinely covered by commercial insurance and Medicare Part D.</li>
  <li><strong>Drugs approved for obesity or weight loss</strong> have historically been excluded from most formularies &mdash; a policy dating to the early 2000s weight-loss drug scandals (fen-phen, etc.) that insurance companies have been slow to update.</li>
  <li><strong>Employer self-funded plans</strong> are cutting GLP-1 coverage in 2025&ndash;2026 because a single employee on Wegovy costs the plan more than $16,000/year. A KFF 2024 employer health benefits survey found that among large employers offering GLP-1 coverage for obesity, 25% planned to restrict or eliminate that coverage in 2025.</li>
</ul>

<p>The result is a landscape where coverage is determined less by medical need and more by your
diagnosis code, your employer&rsquo;s plan design choices, and the year your plan was last updated.</p>

<div class="key-takeaway">
  <strong>Your bill may reflect a prior authorization error, not a genuine coverage exclusion.</strong>
  <a href="/scan">Upload your GLP-1 bill or EOB to BillKarma</a> &mdash; we check whether your claim was
  submitted with the correct NDC code, the right diagnosis code, and whether your denial reason matches
  your actual plan documents.
</div>

<h2 id="ozempic-vs-wegovy">2. Ozempic vs. Wegovy: same drug, different indication, different coverage</h2>

<p>Ozempic and Wegovy are both semaglutide &mdash; the same active ingredient, manufactured by Novo Nordisk.
The difference is dose and FDA indication:</p>

<ul>
  <li><strong>Ozempic</strong> (semaglutide 0.5&ndash;2 mg weekly injection): FDA-approved for
    <em>type 2 diabetes</em> and cardiovascular risk reduction. NDC: 0169-4060-xx (pen injector).
    CPT code J3490 or J3590 when administered in a clinical setting.
    Insurance coverage: widely covered for diabetes diagnosis.</li>
  <li><strong>Wegovy</strong> (semaglutide 0.25&ndash;2.4 mg weekly injection, higher maximum dose):
    FDA-approved for <em>chronic weight management</em> in adults with obesity or overweight with
    a weight-related condition. NDC: 0169-4076-xx (pen injector, higher-dose formulation).
    Insurance coverage: excluded from most formularies; covered by some commercial plans and
    zero Medicare Part D plans (as of 2026, unless a plan has adopted the new CMS GLP-1 obesity
    coverage option).</li>
</ul>

<p>This creates an absurd situation: a patient with type 2 diabetes and obesity might get Ozempic covered
at a $45 copay, while the identical patient &mdash; minus the diabetes diagnosis &mdash; pays $1,349/month
out of pocket for Wegovy. The molecule is the same. The weekly injection is the same. Only the
FDA indication differs, and insurers use that distinction to deny coverage.</p>

<p>Some physicians respond by prescribing Ozempic &ldquo;off-label&rdquo; for weight loss in patients
without diabetes. This is legal, but it generates its own billing complications: if the NDC on file
is for Ozempic but the prior authorization was requested for obesity (E66.x), the claim may be denied
for a mismatch between the drug billed and the indication authorized. This is one of the most
common technical denial reasons BillKarma sees on GLP-1 claims.</p>

<h2 id="glp1-comparison">3. GLP-1 drug comparison table</h2>

<table>
  <thead>
    <tr>
      <th>Drug Name</th>
      <th>Generic (active ingredient)</th>
      <th>FDA Indication</th>
      <th>Dosage Form</th>
      <th>List Price / Month (2026)</th>
      <th>Typical Insurance Coverage</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><strong>Ozempic</strong></td>
      <td>Semaglutide 0.5&ndash;2 mg</td>
      <td>Type 2 diabetes; cardiovascular risk reduction</td>
      <td>Weekly injection</td>
      <td>~$936 (GoodRx list)</td>
      <td>Widely covered for diabetes (commercial + Part D)</td>
    </tr>
    <tr>
      <td><strong>Wegovy</strong></td>
      <td>Semaglutide 2.4 mg</td>
      <td>Chronic weight management (obesity / overweight + comorbidity)</td>
      <td>Weekly injection</td>
      <td>~$1,349 (GoodRx list)</td>
      <td>Covered by ~43% of large employers (declining); excluded from most Medicare Part D plans</td>
    </tr>
    <tr>
      <td><strong>Mounjaro</strong></td>
      <td>Tirzepatide 2.5&ndash;15 mg</td>
      <td>Type 2 diabetes</td>
      <td>Weekly injection</td>
      <td>~$1,069 (GoodRx list)</td>
      <td>Covered for diabetes; weight-loss use typically not covered</td>
    </tr>
    <tr>
      <td><strong>Zepbound</strong></td>
      <td>Tirzepatide 2.5&ndash;15 mg</td>
      <td>Chronic weight management (obesity / overweight + comorbidity)</td>
      <td>Weekly injection</td>
      <td>~$1,059 (GoodRx list)</td>
      <td>Covered by some commercial plans; excluded from most Medicare Part D</td>
    </tr>
    <tr>
      <td><strong>Rybelsus</strong></td>
      <td>Semaglutide 3&ndash;14 mg</td>
      <td>Type 2 diabetes</td>
      <td>Daily oral tablet</td>
      <td>~$936 (GoodRx list)</td>
      <td>Covered for diabetes; no approved weight-loss indication</td>
    </tr>
  </tbody>
</table>

<p><em>List prices are the manufacturer&rsquo;s published U.S. list price before rebates, coupons, or
insurance. Actual out-of-pocket cost depends on your plan. Source: GoodRx, February 2026.</em></p>

<h2 id="why-denied">4. Why insurers deny GLP-1 claims</h2>

<p>GLP-1 denials cluster around five root causes. Knowing which one applies to your denial is the
first step in building an effective appeal.</p>

<table>
  <thead>
    <tr>
      <th>Denial Reason</th>
      <th>What It Means in Plain Language</th>
      <th>Appeal Strategy</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><strong>Formulary exclusion</strong></td>
      <td>The drug is not on your plan&rsquo;s covered drug list. The plan simply does not pay for it under any circumstances.</td>
      <td>Request a formulary exception on medical necessity grounds; document that alternatives were tried and failed or are contraindicated. If the plan covers Ozempic for diabetes, document any diabetes or pre-diabetes diagnosis.</td>
    </tr>
    <tr>
      <td><strong>Prior authorization not obtained</strong></td>
      <td>The prescription was filled without the insurer&rsquo;s advance approval. Even if the drug is covered, the claim is denied because the process wasn&rsquo;t followed.</td>
      <td>Ask your prescriber to submit a retroactive PA request and submit a simultaneous internal appeal citing the urgency of continued medication.</td>
    </tr>
    <tr>
      <td><strong>BMI threshold not documented</strong></td>
      <td>Your plan requires BMI &ge;30 (or &ge;27 with a comorbidity) and the medical records submitted didn&rsquo;t include a documented BMI on or near the date of service.</td>
      <td>Have your doctor submit a letter with your measured BMI and the date it was recorded, plus documentation of any weight-related conditions (hypertension, pre-diabetes, sleep apnea, high cholesterol).</td>
    </tr>
    <tr>
      <td><strong>Step therapy &mdash; prior weight-loss attempts not documented</strong></td>
      <td>Your plan requires evidence of a supervised diet/exercise program or prior weight-loss medication before approving a GLP-1 drug.</td>
      <td>Gather records from any prior weight-loss program, nutritionist visits, or previous medications (orlistat, phentermine, etc.). A 6-month supervised diet program qualifies for most plans.</td>
    </tr>
    <tr>
      <td><strong>Wrong NDC code or indication mismatch</strong></td>
      <td>The NDC (National Drug Code &mdash; the unique number identifying the exact drug and dose on every prescription) on the claim doesn&rsquo;t match the indication or the PA approval. This is a billing error, not a clinical denial.</td>
      <td>Ask your pharmacy to verify the NDC on file matches the dispensed drug. Ask your prescriber to verify the diagnosis codes (ICD-10) on the PA request match the prescription. Correct errors and resubmit.</td>
    </tr>
  </tbody>
</table>

<h2 id="eob-example">5. EOB example: a denied Wegovy claim annotated</h2>

<p>An EOB (Explanation of Benefits) is the document your insurer sends after processing a claim.
It shows what was billed, what the insurer paid, and what you owe. Here is an annotated EOB for
a denied Wegovy claim showing two common problems: a prior authorization hold and an NDC-based
formulary exclusion.</p>

<div class="bill-example">
  <div class="bill-header">
    Explanation of Benefits &mdash; Sample Patient: Jane M.<br>
    Plan: BlueCross PPO Select &mdash; Employer Group Plan<br>
    Date of Service: 2026-01-15 &nbsp;|&nbsp; Processed: 2026-01-22<br>
    Pharmacy: Central Pharmacy #1042
  </div>

  <div class="line-item">
    <span><strong>Drug billed:</strong> Wegovy 2.4 mg/0.75 mL injection pen (4-week supply)<br>
    NDC: 0169-4076-15 &nbsp;|&nbsp; Days supply: 28 &nbsp;|&nbsp; Quantity: 4 pens</span>
    <span><strong>Billed:</strong> $1,349.00</span>
  </div>

  <div class="line-item flagged">
    <span>
      &#9888; <strong>Claim Status: Held — Prior Authorization Pending</strong><br>
      <em>Authorization request ID PA-2026-0081447 submitted 2026-01-10. Insurer has not issued a
      determination. Claim is on hold pending PA decision. Do not pay this amount yet.</em><br>
      <small>Note: If you filled this prescription without confirming PA approval, contact your
      prescriber immediately to follow up on the outstanding request.</small>
    </span>
    <span style="color:#b45309;"><strong>Insurer paid: $0.00</strong><br>Patient responsibility: PENDING</span>
  </div>

  <div class="line-item error">
    <span>
      &#10060; <strong>Claim Denied — NDC Not Covered Under Formulary</strong><br>
      <em>Denial reason code: 96 &mdash; Non-covered charge. NDC 0169-4076-15 (Wegovy semaglutide
      2.4 mg) is not included on the plan formulary. Weight-loss medications are excluded under
      Section 14.3 of your Summary Plan Description. The prior authorization request PA-2026-0081447
      is therefore closed without approval.</em><br>
      <small>Appeal deadline: 60 days from date of this notice (2026-03-22). Submit appeals to:
      BlueCross Appeals Unit, PO Box 10000, [City, State]. Include this EOB and your prescriber&rsquo;s
      letter of medical necessity.</small>
    </span>
    <span style="color:#dc2626;"><strong>Insurer paid: $0.00</strong><br>Patient responsibility: $1,349.00</span>
  </div>

  <div class="line-item">
    <span>
      <strong>What this means for you:</strong> The insurer denied Wegovy on formulary grounds
      (the drug is excluded, not just uncovered for a specific indication). Your first step is
      to verify whether your plan covers Ozempic (semaglutide for diabetes) &mdash; if you have
      a diabetes or pre-diabetes diagnosis, your prescriber can evaluate whether Ozempic is
      appropriate and submit a new PA with the correct ICD-10 code (E11.x for type 2 diabetes).
      Alternatively, file a formulary exception appeal documenting medical necessity and any
      failed prior weight-loss treatments.
    </span>
    <span></span>
  </div>
</div>

<p><strong>Key things to notice in this EOB:</strong></p>
<ul>
  <li>The NDC code <code>0169-4076-15</code> identifies Wegovy specifically. Ozempic has a different
    NDC (0169-4060-xx). If the wrong NDC was submitted, the denial may be correctable by resubmission.</li>
  <li>The denial cites &ldquo;Section 14.3 of your Summary Plan Description.&rdquo; Request a copy of
    your full SPD and read that section &mdash; some plans exclude weight-loss drugs but carve out
    exceptions for medical necessity.</li>
  <li>The appeal deadline is 60 days. Put that date on your calendar the day you receive the EOB.</li>
</ul>

<div class="key-takeaway">
  <strong>Not sure if your GLP-1 charge is higher than expected?</strong><br>
  {_embed(mode="markup", title="Is your GLP-1 charge higher than expected?", subtitle="Enter the NDC or J-code and the amount billed.", height="420")}
</div>

<h2 id="how-to-appeal">6. How to appeal a GLP-1 denial &mdash; step by step</h2>

<p>Appeals for GLP-1 denials have a meaningful success rate when the right documentation is submitted.
The process moves in three stages: internal appeal, external independent review, and (if needed)
state insurance commissioner complaint.</p>

<h3>Step 1: Read the denial letter and identify the exact reason</h3>

<p>Your EOB or denial letter must state a specific reason for denial. The most important distinction
is between a <em>formulary exclusion</em> (the drug is not on the plan at all) and a <em>medical
necessity denial</em> (the drug is on the plan but the insurer says it isn&rsquo;t necessary for
you). The appeal strategy differs significantly between these two:</p>
<ul>
  <li><strong>Formulary exclusion:</strong> You need to file a <em>formulary exception request</em>,
    arguing that no covered alternative is medically appropriate for your situation.</li>
  <li><strong>Medical necessity denial:</strong> You need to submit clinical documentation showing you
    meet the plan&rsquo;s coverage criteria (BMI, comorbidities, failed prior treatments).</li>
  <li><strong>Technical/NDC error:</strong> Have your pharmacy or prescriber verify and resubmit the
    corrected claim &mdash; this may resolve without a formal appeal.</li>
</ul>

<h3>Step 2: Contact your prescriber the same day</h3>

<p>Your doctor&rsquo;s office must be involved in the appeal. They have access to your clinical records
and can submit a peer-to-peer review (a direct call between your doctor and the insurer&rsquo;s medical
director). Peer-to-peer reviews overturn GLP-1 denials in many cases, particularly when the initial
denial was made by a non-physician reviewer. Ask your prescriber&rsquo;s office to:</p>
<ul>
  <li>Request a peer-to-peer review within 5 business days of the denial.</li>
  <li>Prepare a letter of medical necessity (see documentation section below).</li>
  <li>Verify the ICD-10 and NDC codes on the original claim were correct.</li>
</ul>

<h3>Step 3: File the internal appeal in writing</h3>

<p>Most plans require an internal appeal before you can request external review. File in writing,
even if the plan accepts phone calls &mdash; a written record is essential. Include:</p>
<ul>
  <li>A cover letter identifying yourself, the claim number, and the denial reason.</li>
  <li>Your doctor&rsquo;s letter of medical necessity.</li>
  <li>Your BMI documentation (date-stamped weight and height measurements from a clinical visit).</li>
  <li>Documentation of any prior weight-loss treatments tried (diet programs, prior medications,
    nutritionist visits).</li>
  <li>Documentation of any weight-related comorbidities (lab results for A1C/pre-diabetes,
    blood pressure readings, sleep study results for sleep apnea).</li>
  <li>Any peer-reviewed studies on GLP-1 efficacy (particularly the SURMOUNT and STEP trials).</li>
</ul>

<h3>Step 4: Request external independent review if internal appeal fails</h3>

<p>If the internal appeal is denied, you have the right to an independent external review conducted
by a reviewer with no connection to your insurer. For employer self-funded plans (the majority of
large employer plans), the external review process may be governed by ERISA rather than state law.
Contact your state&rsquo;s Department of Insurance to initiate this process. An external reviewer
overturned GLP-1 denials at a meaningful rate in states that tracked this data through 2025.</p>

<h3>Step 5: File a state insurance commissioner complaint if needed</h3>

<p>If your plan is a fully insured commercial plan (not a self-funded employer plan), filing a
complaint with your state insurance commissioner can accelerate resolution. Insurers are required
to respond to commissioner inquiries within a set timeframe, and the complaint creates a formal
record. Your state&rsquo;s insurance department website has the complaint filing form.</p>

<h2 id="documentation">7. Documentation you need for a successful appeal</h2>

<p>The most common reason GLP-1 appeals fail is insufficient documentation &mdash; not because the
patient doesn&rsquo;t qualify, but because the qualifying information wasn&rsquo;t in the appeal
package. Here is the complete documentation checklist:</p>

<table>
  <thead>
    <tr>
      <th>Document</th>
      <th>Why It Matters</th>
      <th>Where to Get It</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>BMI measurement with date</td>
      <td>Most plans require BMI &ge;30, or &ge;27 with comorbidity, documented in clinical records near the date of service</td>
      <td>Ask your doctor&rsquo;s office for a clinical note or office visit summary with your recorded weight, height, and BMI</td>
    </tr>
    <tr>
      <td>Comorbidity documentation</td>
      <td>If your BMI is 27&ndash;29.9, you need documentation of a weight-related condition to qualify</td>
      <td>Lab results (A1C for pre-diabetes), blood pressure records (hypertension), sleep study (sleep apnea), lipid panel (dyslipidemia)</td>
    </tr>
    <tr>
      <td>Prior weight-loss treatment history</td>
      <td>Many plans require evidence of a failed prior treatment before approving GLP-1</td>
      <td>Records from a supervised diet program, nutritionist, or prior weight-loss medication prescriptions</td>
    </tr>
    <tr>
      <td>Letter of medical necessity</td>
      <td>Your prescriber explains in clinical language why this specific drug is medically necessary for you</td>
      <td>Ask your prescriber to draft this; it should reference your BMI, comorbidities, and failed alternatives</td>
    </tr>
    <tr>
      <td>Copy of your plan&rsquo;s coverage criteria</td>
      <td>Demonstrates you meet the plan&rsquo;s own stated criteria, making it harder to deny without contradicting their own policy</td>
      <td>Your insurer&rsquo;s member portal under &ldquo;Medical Policies&rdquo; or &ldquo;Clinical Coverage Guidelines&rdquo;</td>
    </tr>
    <tr>
      <td>Clinical trial evidence</td>
      <td>Strengthens medical necessity argument for a formulary exception</td>
      <td>STEP 1&ndash;5 trials (semaglutide), SURMOUNT trials (tirzepatide) &mdash; all published in <em>NEJM</em> and <em>JAMA</em></td>
    </tr>
  </tbody>
</table>

<div class="key-takeaway">
  <strong>Compare your billed amount to Medicare benchmark rates for GLP-1 injections.</strong><br>
  If your GLP-1 was administered in a clinical setting (e.g., a weight-loss clinic), the J-code
  billed (J3490 or J3590 for unclassified drugs) may be higher than the Medicare-allowable rate.
  Use <a href="/calculator">BillKarma&rsquo;s pricing calculator</a> to benchmark what you were charged
  against what Medicare and typical commercial plans pay for the same administration.
</div>

<h2 id="cost-reduction">8. Cost reduction: manufacturer coupons, Part D plans, and alternatives</h2>

<p>If your appeal fails or you need the medication while the appeal is pending, there are legitimate
ways to reduce cost significantly.</p>

<h3>Manufacturer savings programs</h3>
<p>Novo Nordisk offers the <strong>Novo Nordisk Patient Assistance Program</strong> for uninsured or
underinsured patients who meet income criteria (generally up to 400% of the federal poverty level).
Eligible patients may receive the drug at no or low cost. Additionally, Novo Nordisk&rsquo;s savings card
for commercially insured patients can reduce the copay to as low as $25/month &mdash; but this card does
not work if your plan has formally excluded GLP-1 drugs (it applies to cost-sharing reduction,
not to coverage gaps). Eli Lilly offers a similar savings program for Zepbound and Mounjaro.</p>

<h3>Medicare Part D and the 2026 landscape</h3>
<p>Traditional Medicare Part D has historically excluded weight-loss drugs entirely. In 2024, CMS
published a rule allowing (but not requiring) Part D plans to cover GLP-1 drugs approved for
cardiovascular risk reduction (specifically semaglutide, following the SELECT trial showing reduced
cardiovascular events). As of 2026, some Part D plans cover Wegovy for patients with established
cardiovascular disease plus obesity &mdash; check your specific plan&rsquo;s formulary at
<a href="https://www.medicare.gov/plan-compare/" target="_blank" rel="noopener">medicare.gov/plan-compare</a>.</p>

<h3>Switching to a different GLP-1 that is covered</h3>
<p>If Wegovy is excluded but your plan covers Ozempic for diabetes, and you have a type 2 diabetes
or pre-diabetes diagnosis, ask your doctor whether Ozempic is medically appropriate. This is not
gaming the system &mdash; Ozempic is FDA-approved for diabetes and has documented cardiovascular
benefits that independently justify its use in patients with metabolic disease.</p>

<h3>Telehealth weight-loss programs</h3>
<p>Several telehealth platforms contract directly with Novo Nordisk and Eli Lilly to provide
lower-cost access to GLP-1 drugs for cash-pay patients. These do not use insurance. Prices
typically run $200&ndash;$400/month through these platforms compared to the $1,000+ list price,
because the platforms receive volume discounts. This is a legitimate option if your appeal fails
and cost is the primary barrier.</p>

<h3>Comparing hospital and pharmacy prices</h3>
<p>If you receive GLP-1 injections in a clinical setting (some weight management clinics administer
them in-office), the facility fee and drug administration charge can vary enormously between providers.
Use <a href="/hospitals/">BillKarma&rsquo;s hospital pricing data</a> to compare drug administration
costs at facilities near you before committing to a specific clinic.</p>

<h2 id="case-studies">9. Case studies</h2>

<div class="key-takeaway">
  <strong>See what GLP-1 drug administration costs at hospitals near you.</strong>
  If you receive injections in a clinical setting, hospital and clinic prices for the same
  J-code service vary by as much as 400%. <a href="/hospitals/">Use BillKarma&rsquo;s hospital
  price comparison tool</a> to find lower-cost providers in your area before your next appointment.
</div>

<div class="case-study">
  <h3>Case Study 1: Diabetic patient denied Ozempic due to wrong NDC</h3>
  <p>A 58-year-old patient with well-documented type 2 diabetes received a prescription for Ozempic
  (semaglutide 1 mg) from her endocrinologist. Her pharmacy submitted the claim with NDC
  <code>0169-4060-13</code> (the 1 mg pen). Her insurer processed the claim under a different
  NDC prefix and returned a denial: &ldquo;NDC not on formulary.&rdquo; Her correct Ozempic
  NDC was covered &mdash; the pharmacy had entered a transcription error from the package label.</p>
  <p>Her pharmacist verified the NDC against the current Novo Nordisk NDC directory, corrected
  the claim to <code>0169-4060-13</code>, and resubmitted. The corrected claim paid within
  four days at a $45 specialty copay. <strong>Result: $936 monthly bill reduced to $45 copay.
  No formal appeal required &mdash; just a corrected NDC resubmission.</strong></p>
  <p><em>Key lesson: Always ask the pharmacy to verify the NDC on file against the physical
  package before assuming a denial is coverage-related. Technical billing errors cause a
  significant portion of GLP-1 denials.</em></p>
</div>

<div class="case-study">
  <h3>Case Study 2: Patient with obesity wins Wegovy appeal using BMI and comorbidity documentation</h3>
  <p>A 44-year-old patient with a BMI of 31 and diagnosed hypertension was prescribed Wegovy by
  her primary care physician. Her large employer&rsquo;s self-funded plan initially covered GLP-1
  drugs for obesity, but her prior authorization was denied with the reason: &ldquo;Medical
  necessity criteria not met &mdash; documentation insufficient.&rdquo; Her doctor&rsquo;s office
  had submitted the request without attaching her blood pressure records or any documentation of
  a prior weight-loss attempt.</p>
  <p>She contacted her doctor&rsquo;s office and asked them to resubmit the appeal with: (1) a
  clinical note documenting her BMI of 31 measured at the office visit, (2) blood pressure records
  confirming her hypertension diagnosis, and (3) a letter from her doctor referencing the 12 months
  of supervised diet modification she had attempted under the care of a registered dietitian.
  The insurer&rsquo;s medical director approved the PA on peer-to-peer review.
  <strong>Result: Wegovy approved. Monthly cost: $50 specialty copay versus $1,349 list price.</strong></p>
  <p><em>Key lesson: Most GLP-1 medical necessity denials are won by documenting what the plan&rsquo;s
  own criteria require &mdash; BMI, comorbidity, and prior treatment history. The clinical facts
  were never in dispute; only the paperwork was missing.</em></p>
</div>

<div class="case-study">
  <h3>Case Study 3: Patient reduces cost by $900/month through a telehealth GLP-1 program</h3>
  <p>A 39-year-old patient with a BMI of 33 and no diabetes diagnosis had his Wegovy PA denied
  because his employer dropped GLP-1 obesity coverage effective January 2026. His internal appeal
  was denied &mdash; the exclusion was a plan design decision, not a medical necessity determination,
  and his employer&rsquo;s self-funded plan has broad discretion over formulary choices under ERISA.
  External review was available but unlikely to succeed given the categorical exclusion.</p>
  <p>He enrolled in a telehealth weight management platform that contracts directly with a
  compounding pharmacy for tirzepatide (the active ingredient in Zepbound) at $349/month through
  their program &mdash; compared to $1,069 list price at retail. He also applied for Eli Lilly&rsquo;s
  direct patient savings program and qualified for a further discount. His net monthly cost dropped
  to approximately $349 from $1,069.
  <strong>Result: $720/month in savings through a cash-pay telehealth program after appeal failed.</strong></p>
  <p><em>Key lesson: When a categorical plan exclusion blocks the appeal path, the cost-reduction
  route &mdash; manufacturer savings programs, telehealth platforms, and transparent-pricing pharmacies
  &mdash; can still produce significant savings. Always verify the current legal status of compounded
  versions before use, as FDA policy continues to evolve.</em></p>
</div>


<h2 id="faq">Frequently asked questions</h2>

<div class="faq-section">
  <div class="faq-item">
    <h3>Does insurance cover Ozempic for weight loss?</h3>
    <p>Usually not when prescribed specifically for weight loss. Ozempic is FDA-approved for type 2
    diabetes, and insurance covers it for that indication. If your prescription or prior authorization
    request is coded for obesity (ICD-10 E66.x) rather than diabetes (E11.x), the claim will often
    be denied. Wegovy is the semaglutide formulation approved for obesity, but most plans &mdash; and
    all traditional Medicare Part D plans &mdash; exclude it from coverage. If you have a diabetes or
    pre-diabetes diagnosis, discuss with your doctor whether Ozempic is appropriate and ensure the
    correct diagnosis code is submitted.</p>
  </div>

  <div class="faq-item">
    <h3>What is the difference between Ozempic and Wegovy coverage?</h3>
    <p>Ozempic (semaglutide for diabetes) is widely covered because diabetes drugs are not excluded
    from most formularies. Wegovy (semaglutide for obesity, at a higher 2.4 mg weekly dose) is
    excluded from most commercial and Medicare formularies because weight-loss drugs have historically
    been carved out of coverage. Only about 43% of large employers covered Wegovy as of 2024, and that
    number is declining. The drugs contain the same active ingredient but have different NDC codes,
    different FDA indications, and very different coverage outcomes. See our
    <a href="/guides/prior-authorization">prior authorization guide</a> for more on how indication
    affects coverage decisions.</p>
  </div>

  <div class="faq-item">
    <h3>How do I appeal a GLP-1 prior authorization denial?</h3>
    <p>Read the denial letter to identify whether you were denied for formulary exclusion, medical
    necessity, or an administrative/NDC error. Gather BMI documentation, comorbidity records, and
    prior weight-loss treatment history. File a written internal appeal with your prescriber&rsquo;s
    letter of medical necessity within your plan&rsquo;s appeal deadline (usually 60&ndash;180 days).
    Ask your doctor to request a peer-to-peer review with the insurer&rsquo;s medical director.
    If the internal appeal fails, request an independent external review. See our full
    <a href="/guides/appeal-denial">insurance denial appeal guide</a> for a detailed walkthrough.</p>
  </div>

  <div class="faq-item">
    <h3>What BMI do I need for insurance to cover Wegovy or Zepbound?</h3>
    <p>Most plans that cover these drugs follow the FDA label: BMI of 30 or above, or BMI of 27 or
    above with at least one weight-related condition such as high blood pressure, type 2 diabetes,
    or high cholesterol. BMI (body mass index) is calculated from your height and weight and must be
    documented in a clinical record near the date of service. Some plans also require documentation
    of a supervised weight-loss program lasting at least 6 months as a step therapy requirement
    before approving a GLP-1 drug.</p>
  </div>

  <div class="faq-item">
    <h3>Is compounded semaglutide safe and legal?</h3>
    <p>As of 2026, the FDA has declared the Ozempic and Wegovy shortage resolved, which removed the
    legal basis for most compounding pharmacies to produce semaglutide. Compounded semaglutide from
    standard state-licensed pharmacies is generally no longer legal for routine dispensing. FDA-approved
    branded drugs (Ozempic, Wegovy, Mounjaro, Zepbound) remain the legal options. The legal landscape
    continues to evolve &mdash; verify current FDA guidance before considering any compounded version.
    Eli Lilly&rsquo;s and Novo Nordisk&rsquo;s manufacturer assistance programs remain available for
    patients who cannot afford brand-name pricing.</p>
  </div>
</div>

<h2 id="sources">Sources</h2>

<ul class="sources-list">
  <li><a href="https://www.fda.gov/drugs/new-drugs-fda-cders-new-molecular-entities-and-new-therapeutic-biological-products/drug-approvals-and-databases" target="_blank" rel="noopener">FDA: Drug Approvals Database &mdash; Ozempic (2017), Wegovy (2021), Mounjaro (2022), Zepbound (2023)</a></li>
  <li><a href="https://www.cms.gov/medicare/coverage/prescription-drug-coverage/part-d-formulary" target="_blank" rel="noopener">CMS: Medicare Part D Formulary and Coverage Rules (2025&ndash;2026)</a></li>
  <li><a href="https://www.kff.org/health-costs/press-release/most-large-employers-cover-glp-1s-for-diabetes-but-fewer-cover-them-for-weight-loss/" target="_blank" rel="noopener">KFF: Large Employer GLP-1 Coverage Survey (2024)</a></li>
  <li><a href="https://www.goodrx.com/ozempic" target="_blank" rel="noopener">GoodRx: Ozempic, Wegovy, Mounjaro, Zepbound Pricing (February 2026)</a></li>
  <li><a href="https://www.healthaffairs.org/doi/10.1377/hlthaff.2023.01340" target="_blank" rel="noopener">Health Affairs: GLP-1 Coverage and Access Disparities in Commercial Insurance (2024)</a></li>
  <li><a href="https://www.nejm.org/doi/full/10.1056/NEJMoa2032183" target="_blank" rel="noopener">NEJM: STEP 1 Trial &mdash; Semaglutide 2.4 mg for Obesity (Wilding et al., 2021)</a></li>
  <li><a href="https://www.nejm.org/doi/full/10.1056/NEJMoa2307519" target="_blank" rel="noopener">NEJM: SELECT Trial &mdash; Semaglutide and Cardiovascular Outcomes in Obesity (Lincoff et al., 2023)</a></li>
</ul>
""",
})
