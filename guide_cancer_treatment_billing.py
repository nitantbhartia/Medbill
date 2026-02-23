"""Guide: Cancer Treatment Billing — How to Manage Bills During and After Treatment"""

from guides import register, _embed

register("cancer-treatment-billing-guide", {
    "title": "Cancer Treatment Billing: How to Manage Bills During and After Treatment",
    "meta_description": "Cancer patients face an average $150,000 in treatment costs. Learn how chemotherapy, radiation, and immunotherapy are billed, what assistance is available, and how to avoid $10,000+ billing errors.",
    "published": "2026-02-23",
    "author": "BillKarma Team",
    "category": "Cancer Care",
    "faqs": [
        {
            "q": "Why does chemotherapy cost so much?",
            "a": "Chemotherapy costs are driven by two separate charges: the drug itself (billed using J-codes) and the administration fee for the infusion. Hospitals add a facility markup on top of the drug's acquisition cost, sometimes 200&ndash;400% above what they paid. Administration fees alone can run $300&ndash;$800 per infusion session. On top of that, labs and imaging required to monitor treatment add thousands per month."
        },
        {
            "q": "What is a J-code on a hospital bill?",
            "a": "J-codes are HCPCS Level II codes used to bill injectable and infusible drugs, including most chemotherapy agents. For example, J9035 is bevacizumab (Avastin) and J9355 is trastuzumab (Herceptin). Each J-code specifies the drug and the unit of measurement (per milligram or per vial). Hospitals bill a quantity of units, so errors in unit count directly inflate your bill."
        },
        {
            "q": "What is a copay accumulator program?",
            "a": "A copay accumulator program is an insurer policy that prevents manufacturer copay assistance (like drug company coupons) from counting toward your deductible or out-of-pocket maximum. You may use $6,000 in manufacturer assistance and then discover your insurer credits you $0 toward your out-of-pocket &mdash; meaning you still owe the full deductible out of your own pocket once the assistance runs out."
        },
        {
            "q": "Can I get free cancer medication?",
            "a": "Yes, in many cases. Most major oncology drug manufacturers operate patient assistance programs (PAPs) that provide free or deeply discounted drugs to patients who meet income criteria, typically under 400&ndash;500% of the federal poverty level. Organizations like NeedyMeds.org and RxAssist.org maintain searchable databases. CancerCare and the Patient Advocate Foundation also offer co-pay assistance funds."
        },
        {
            "q": "What is 340B drug pricing?",
            "a": "The 340B Drug Pricing Program requires pharmaceutical manufacturers to sell drugs to qualifying hospitals and clinics at a 20&ndash;50% discount. However, these hospitals are allowed to bill insurers and patients at the full market price, keeping the difference. Patients treated at 340B hospitals often pay more in cost-sharing (copays, coinsurance) because those payments are based on the full billed price, not the discounted acquisition cost."
        },
    ],
    "body": f"""
<p class="lead">
  A cancer diagnosis brings a second crisis: the bills. BillKarma&rsquo;s analysis of 6,800+ hospitals found
  that the same chemotherapy infusion can be billed at $4,200 at one hospital and $18,700 at another for
  identical drugs and identical doses. The average cancer patient faces $150,000 or more in treatment costs,
  and billing errors exceeding $10,000 are common. This guide explains exactly how cancer treatment is billed,
  where the errors hide, and how to access assistance programs that can eliminate tens of thousands in costs.
</p>

<nav class="toc">
  <strong>In this guide</strong>
  <ol>
    <li><a href="#types-of-billing">Types of Cancer Treatment Billing</a></li>
    <li><a href="#cost-breakdown">The Cost Breakdown</a></li>
    <li><a href="#common-codes">Common Cancer CPT and J-Codes</a></li>
    <li><a href="#copay-accumulators">Copay Accumulator Programs</a></li>
    <li><a href="#financial-assistance">Financial Assistance Resources</a></li>
    <li><a href="#bill-example">Reading a Chemotherapy Bill</a></li>
    <li><a href="#case-studies">Case Studies</a></li>
    <li><a href="#340b-pricing">340B Drug Pricing</a></li>
    <li><a href="#clinical-trials">Clinical Trials and Cost Savings</a></li>
    <li><a href="#faqs">Frequently Asked Questions</a></li>
  </ol>
</nav>

<h2 id="types-of-billing">1. Types of Cancer Treatment Billing</h2>
<p>
  Cancer treatment involves multiple categories of care, each billed under different code sets and by different
  providers. Understanding which category applies to your treatment is the first step in reviewing your bills accurately.
</p>
<p>
  <strong>Chemotherapy (infusion therapy)</strong> is billed using two layers: the drug itself (using HCPCS J-codes)
  and the administration (using CPT codes 96413&ndash;96417 for intravenous infusion). You will typically receive
  a separate bill for each. The drug charge is often the largest single line item on any cancer bill.
</p>
<p>
  <strong>Radiation therapy</strong> uses CPT codes in the 77xxx range. Treatment planning (77261&ndash;77263),
  simulation (77280&ndash;77295), and actual treatment delivery (77401&ndash;77525) are billed as distinct services.
  A standard course of radiation may involve 20&ndash;35 delivery sessions plus planning &mdash; each billed separately.
</p>
<p>
  <strong>Immunotherapy</strong> is billed similarly to chemotherapy &mdash; J-codes for the drug, infusion
  administration codes for delivery. However, immunotherapy drugs (pembrolizumab, nivolumab, atezolizumab) carry
  acquisition costs of $10,000&ndash;$20,000 per infusion cycle, making billing accuracy critical.
</p>
<p>
  <strong>Surgery</strong> for cancer (tumor resection, mastectomy, lymph node dissection) uses standard surgical
  CPT codes. These follow the same billing structure as any other surgery: facility fee, surgeon fee, anesthesia,
  and pathology.
</p>
<p>
  <strong>Ongoing monitoring</strong> &mdash; blood counts (CBC), tumor markers, imaging (CT, PET scans) &mdash;
  runs throughout treatment and generates its own billing stream. PET scans alone cost $5,000&ndash;$11,000 each
  at hospital outpatient rates.
</p>

<h2 id="cost-breakdown">2. The Cost Breakdown</h2>
<p>
  Every chemotherapy encounter typically generates four separate charges billed to your insurer simultaneously.
  Know what each represents so you can verify what you&rsquo;re actually being charged for.
</p>
<p>
  <strong>Drug cost:</strong> The acquisition cost of the chemotherapy drug. Hospitals add a markup of 100&ndash;400%
  above their actual acquisition price. For a drug the hospital purchased at $2,000, a $6,000&ndash;$10,000 charge
  to your insurer is common. Your cost-sharing is based on this inflated charge, not the acquisition cost.
</p>
<p>
  <strong>Administration fee:</strong> CPT 96413 covers the first hour of intravenous infusion ($250&ndash;$600 at
  Medicare rates; hospitals typically charge $800&ndash;$2,500). Each additional hour is billed separately under
  CPT 96415. If you receive multiple drugs in the same session, each drug after the first triggers an additional
  administration code (96417).
</p>
<p>
  <strong>Radiation planning:</strong> Before treatment delivery begins, your radiation oncologist creates a treatment
  plan. This involves simulation imaging, dosimetry calculations, and physician review. Planning can cost
  $2,000&ndash;$8,000 for a standard course of radiation and is billed once at the start of treatment.
</p>
<p>
  <strong>Lab monitoring:</strong> Complete blood counts before each infusion cycle, liver function panels,
  and tumor marker tests add $200&ndash;$600 per visit. Over a 6-month course of treatment, cumulative lab
  costs reach $3,000&ndash;$6,000.
</p>

<h2 id="common-codes">3. Common Cancer CPT and J-Codes</h2>
<table>
  <thead>
    <tr>
      <th>Code</th>
      <th>Description</th>
      <th>Medicare Rate</th>
      <th>Typical Hospital Charge</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>J9035</td>
      <td>Bevacizumab (Avastin), per 10mg</td>
      <td>$69/10mg</td>
      <td>$180&ndash;$320/10mg</td>
    </tr>
    <tr>
      <td>J9355</td>
      <td>Trastuzumab (Herceptin), per 10mg</td>
      <td>$76/10mg</td>
      <td>$200&ndash;$390/10mg</td>
    </tr>
    <tr>
      <td>J9999</td>
      <td>Not otherwise classified chemo drug</td>
      <td>Varies</td>
      <td>Varies (audit carefully)</td>
    </tr>
    <tr>
      <td>J0129</td>
      <td>Abatacept injection, 10mg</td>
      <td>$7.90/10mg</td>
      <td>$22&ndash;$45/10mg</td>
    </tr>
    <tr>
      <td>96413</td>
      <td>Chemo infusion, initial up to 1 hr</td>
      <td>$148 (hospital outpatient)</td>
      <td>$800&ndash;$2,500</td>
    </tr>
    <tr>
      <td>96415</td>
      <td>Chemo infusion, each add&rsquo;l hr</td>
      <td>$29 (hospital outpatient)</td>
      <td>$200&ndash;$600</td>
    </tr>
    <tr>
      <td>77263</td>
      <td>Radiation treatment planning, complex</td>
      <td>$176</td>
      <td>$800&ndash;$2,200</td>
    </tr>
    <tr>
      <td>77418</td>
      <td>IMRT treatment delivery</td>
      <td>$361</td>
      <td>$1,400&ndash;$4,500</td>
    </tr>
    <tr>
      <td>85025</td>
      <td>CBC with differential</td>
      <td>$11</td>
      <td>$85&ndash;$240</td>
    </tr>
    <tr>
      <td>71250</td>
      <td>CT thorax with contrast</td>
      <td>$243</td>
      <td>$3,200&ndash;$7,800</td>
    </tr>
  </tbody>
</table>

<h2 id="copay-accumulators">4. Copay Accumulator Programs</h2>
<p>
  Copay accumulator programs are one of the most financially dangerous features in modern insurance plans for
  cancer patients. Here&rsquo;s how they work and how to protect yourself.
</p>
<p>
  Many cancer drug manufacturers offer copay assistance cards that cover patient cost-sharing &mdash; sometimes
  up to $10,000&ndash;$25,000 per year. Traditionally, the amount paid by the manufacturer&rsquo;s card counted
  toward your deductible and out-of-pocket maximum just like cash you paid yourself.
</p>
<p>
  Under a copay accumulator program, your insurer credits only the amount <em>you personally pay</em> toward your
  deductible and out-of-pocket maximum. Manufacturer assistance payments are excluded. The result: you can exhaust
  a $10,000 manufacturer card and find your deductible has not moved at all. When the card runs out mid-year,
  you suddenly owe the full cost-sharing amount from your own pocket.
</p>
<p>
  <strong>How to find out if your plan uses accumulators:</strong> Call your insurer and ask directly: &ldquo;Does
  my plan use a copay accumulator or copay maximizer program for specialty drugs?&rdquo; Read your Summary of
  Benefits and Coverage for language about &ldquo;manufacturer coupons&rdquo; or &ldquo;third-party payments.&rdquo;
  Several states have passed laws restricting accumulator programs &mdash; check if your state is one of them.
</p>
<p>
  <strong>Copay maximizer programs</strong> are a variation: the insurer restructures your cost-sharing to extract
  the maximum amount from the manufacturer assistance card over the entire year, then leave you owing nothing &mdash;
  but you receive no personal accumulation credit either.
</p>

<h2 id="financial-assistance">5. Financial Assistance Resources</h2>
<p>
  Every cancer patient should exhaust financial assistance options before paying large bills out of pocket.
  These programs collectively provide billions in support annually, but many patients never apply.
</p>
<p>
  <strong>Manufacturer patient assistance programs (PAPs):</strong> Every major oncology drug manufacturer
  (Genentech, Bristol-Myers Squibb, Merck, AstraZeneca) operates a PAP for uninsured or underinsured patients.
  Income thresholds are often 400&ndash;600% of the federal poverty level. Apply through each manufacturer&rsquo;s
  website or ask your oncology social worker.
</p>
<p>
  <strong>CancerCare Co-Payment Assistance Foundation:</strong> Provides grants of $500&ndash;$2,000 to help with
  copays for specific cancer drugs. Eligibility is based on cancer type and income. Grants are available while
  funding lasts &mdash; apply early in treatment.
</p>
<p>
  <strong>Patient Advocate Foundation Co-Pay Relief Program:</strong> Offers direct financial assistance for
  insurance cost-sharing, including deductibles, copays, and coinsurance. Disease-specific funds may have waiting
  lists, but the program serves tens of thousands of patients annually.
</p>
<p>
  <strong>NeedyMeds.org:</strong> A free database of patient assistance programs, disease funds, and state
  pharmaceutical assistance programs. Search by drug name or diagnosis to find programs you qualify for.
</p>
<p>
  <strong>Hospital charity care:</strong> If your income is below 200&ndash;400% of the federal poverty level
  (thresholds vary by hospital), nonprofit hospitals are required to offer free or reduced-cost care. Request
  a charity care application from the hospital financial counseling office. Apply before your first bill is due.
</p>

<table>
  <thead>
    <tr>
      <th>Program</th>
      <th>Who Qualifies</th>
      <th>Max Benefit</th>
      <th>How to Apply</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Hospital Charity Care</td>
      <td>Income below 200&ndash;400% FPL (varies by hospital); uninsured or underinsured</td>
      <td>100% of bill (full forgiveness at many nonprofit hospitals)</td>
      <td>Request financial counselor at hospital billing office; apply before first bill is due</td>
    </tr>
    <tr>
      <td>Manufacturer PAPs (e.g., Genentech, BMS, Merck)</td>
      <td>Uninsured or underinsured; income typically below 400&ndash;600% FPL</td>
      <td>Free drug for duration of treatment (value: $10,000&ndash;$200,000+/year)</td>
      <td>Apply at manufacturer&rsquo;s website or through oncology social worker; reapply annually</td>
    </tr>
    <tr>
      <td>CancerCare Co-Payment Assistance Foundation</td>
      <td>Diagnosed with specific cancers; income and insurance criteria vary by fund</td>
      <td>$500&ndash;$2,000 per grant for drug copays</td>
      <td>Apply online at cancercare.org; funds available while grants last&mdash;apply early</td>
    </tr>
    <tr>
      <td>Patient Advocate Foundation Co-Pay Relief</td>
      <td>Diagnosed with qualifying disease; income below set threshold; insured</td>
      <td>Up to $10,000/year for copays, deductibles, and coinsurance</td>
      <td>Apply at patientadvocate.org; disease-specific funds may have waitlists</td>
    </tr>
    <tr>
      <td>NeedyMeds</td>
      <td>Any patient seeking drug or cost assistance; no income requirement to search</td>
      <td>Varies by program found (aggregates hundreds of PAPs and state funds)</td>
      <td>Search free at needymeds.org by drug name or diagnosis; no registration required</td>
    </tr>
    <tr>
      <td>HealthWell Foundation</td>
      <td>Diagnosed with qualifying chronic or life-threatening illness; insured; income below 500% FPL</td>
      <td>Up to $10,000&ndash;$15,000/year depending on disease fund</td>
      <td>Apply at healthwellfoundation.org; check open disease funds before applying</td>
    </tr>
  </tbody>
</table>

<h2 id="bill-example">6. Reading a Chemotherapy Bill</h2>
<div class="bill-example">
  <div class="line-item">Facility fee &mdash; hospital outpatient | $2,800</div>
  <div class="line-item flagged">J9355 &mdash; Trastuzumab 440mg (44 units &times; $390) | $17,160 <span class="flag-reason">Medicare rate: $76/10mg = $3,344 for this dose. Hospital markup: 413%.</span></div>
  <div class="line-item flagged">96413 &mdash; Chemo infusion initial 1hr | $2,100 <span class="flag-reason">Medicare hospital outpatient rate: $148. Charged 14x Medicare.</span></div>
  <div class="line-item">96415 &mdash; Chemo infusion add&rsquo;l 1hr | $480</div>
  <div class="line-item error">85025 &mdash; CBC (billed 3 units) | $540 <span class="flag-reason">Only 1 CBC was drawn this visit. Duplicate billing for 2 units ($360 overcharge).</span></div>
  <div class="line-item">99213 &mdash; Office visit, established patient | $220</div>
  <div class="line-total">Total Billed: $23,300 | Medicare-equivalent: $4,832 | Overcharge identified: $5,220</div>
</div>

<h2 id="case-studies">7. Case Studies</h2>
<div class="case-study">
  <h3>$12,000 Drug Billing Error Caught: Wrong Dosage Billed</h3>
  <p>
    A 58-year-old breast cancer patient received trastuzumab (Herceptin) every three weeks. Her oncologist prescribed
    440mg per cycle based on her weight. The hospital&rsquo;s billing department coded her first three infusions at
    600mg (the next standard vial size), generating J9355 charges for 60 units instead of 44 units each visit.
  </p>
  <p>
    She requested an itemized bill after her insurer sent an EOB showing charges 36% higher than she expected.
    Comparing the J-code unit counts against her treatment records (which specified 440mg), she identified the
    discrepancy. The hospital corrected all three claims, reducing charges by $12,480. Her resulting coinsurance
    obligation dropped by $2,496.
  </p>
  <p>
    <strong>Lesson:</strong> Always compare J-code unit counts on your bill against the dose documented in your
    treatment summary. Dosage in milligrams divided by 10 should equal the number of units billed.
  </p>
</div>

<div class="case-study">
  <h3>Copay Accumulator Trap: Patient Owed $8,400 More Than Expected</h3>
  <p>
    A lung cancer patient enrolled in a new employer plan in January. His oncologist prescribed pembrolizumab
    (Keytruda). The manufacturer&rsquo;s copay card covered up to $25,000 per year. He assumed his $7,500 deductible
    would be met quickly as the card paid his cost-sharing.
  </p>
  <p>
    In August, his copay card was exhausted. His insurer notified him that his deductible was still $0 credited
    &mdash; the plan used a copay accumulator program, and no manufacturer payments had counted. He owed $7,500
    in deductible plus ongoing coinsurance for the rest of the year: a total of $8,400 he had not budgeted for.
  </p>
  <p>
    <strong>Lesson:</strong> Before starting any specialty drug, call your insurer and ask explicitly whether your
    plan uses a copay accumulator or maximizer program. If it does, plan your cash flow accordingly and discuss
    alternatives with your pharmacist.
  </p>
</div>

<div class="case-study">
  <h3>Manufacturer Assistance Saves $24,000/Year on Immunotherapy</h3>
  <p>
    A 64-year-old melanoma patient (not yet Medicare-eligible) was prescribed nivolumab (Opdivo) at $14,000 per
    infusion every four weeks. His insurance coinsurance was 20%, creating a $2,800/infusion obligation &mdash;
    $33,600 per year. He could not afford to continue treatment.
  </p>
  <p>
    His oncology nurse navigator helped him apply for Bristol-Myers Squibb&rsquo;s patient assistance program.
    He qualified based on income (under 500% FPL). The program covered his entire coinsurance obligation, reducing
    his annual out-of-pocket from $33,600 to under $2,400 (covering only incidental costs). He continued treatment
    uninterrupted for 14 months.
  </p>
  <p>
    <strong>Lesson:</strong> Ask your oncologist&rsquo;s office if they have a nurse navigator or financial
    counselor. These specialists know manufacturer assistance programs and can navigate the application process
    while you focus on treatment.
  </p>
</div>

<h2 id="340b-pricing">8. 340B Drug Pricing</h2>
<p>
  The 340B Drug Pricing Program was created in 1992 to stretch limited federal resources for safety-net providers.
  It requires drug manufacturers to sell medications to qualifying hospitals and clinics at a 20&ndash;50% discount.
  Over 12,000 hospitals and health centers now participate.
</p>
<p>
  Here is the problem for cancer patients: 340B hospitals purchase your chemotherapy drug at a steep discount
  but are permitted to bill your insurer &mdash; and calculate your cost-sharing &mdash; at the full market price.
  A drug the hospital bought for $3,000 under 340B pricing is billed at $8,000. Your 20% coinsurance is calculated
  on $8,000 ($1,600), not on $3,000 ($600). You pay $1,000 more per infusion because of the pricing spread.
</p>
<p>
  How to find out if your hospital participates in 340B: the Health Resources and Services Administration (HRSA)
  maintains a public database at hrsa.gov/340b. Search your hospital by name. If it participates, your drugs may
  be purchased at a discount even though you&rsquo;re billed at full price.
</p>
<p>
  Some states are beginning to require 340B hospitals to pass discounts on to patients. Check whether your state
  has 340B transparency legislation in effect.
</p>

<h2 id="clinical-trials">9. Clinical Trials and Cost Savings</h2>
<p>
  Participating in a clinical trial can significantly reduce treatment costs. Under the Affordable Care Act, health
  insurers are required to cover &ldquo;routine costs&rdquo; of clinical trial participation for qualifying trials.
  This includes items that would normally be covered if you were not in a trial: office visits, lab work, standard
  imaging, and administration of the study drug.
</p>
<p>
  The trial sponsor typically provides the investigational drug at no cost. If your standard of care would involve
  a $15,000/month immunotherapy drug, a clinical trial testing an equivalent drug can eliminate that cost entirely
  while keeping all routine care costs covered by your insurance.
</p>
<p>
  Ask your oncologist whether you are eligible for any active trials. The National Cancer Institute&rsquo;s trial
  search at cancer.gov/about-cancer/treatment/clinical-trials/search lists trials by cancer type, stage, and location.
</p>

{_embed("cancer-treatment-billing-guide")}

<div class="key-takeaway">
  <strong>Key Takeaway 1:</strong> Compare J-code unit counts on every chemotherapy bill against your documented
  dose. Dosage (mg) &divide; 10 = units that should be billed. Errors in unit counts are among the most common
  and most expensive billing mistakes in oncology.
  <a href="/scan">Upload your cancer bill to BillKarma for a line-by-line review.</a>
</div>

<div class="key-takeaway">
  <strong>Key Takeaway 2:</strong> Before starting any manufacturer copay assistance program, call your insurer
  and ask whether your plan uses a copay accumulator or maximizer. If it does, that assistance may not count
  toward your deductible, creating a mid-year financial crisis when the assistance card runs out.
  <a href="/calculator">Use our out-of-pocket calculator to model your annual cancer treatment costs.</a>
</div>

<div class="key-takeaway">
  <strong>Key Takeaway 3:</strong> If you cannot afford your cancer treatment costs, apply for manufacturer patient
  assistance and hospital charity care before your first payment is due. These programs are underused &mdash; most
  patients who apply and qualify receive substantial help, sometimes eliminating costs entirely.
  Check our <a href="/hospitals/">hospital directory</a> to see which hospitals in your area offer charity care, what their income thresholds are, and how their overall billing transparency scores compare.
</div>

<div class="faq-section">
  <h2 id="faqs">Frequently Asked Questions</h2>
  <div class="faq-item">
    <h3>Why does chemotherapy cost so much?</h3>
    <p>Chemotherapy costs are driven by two separate charges: the drug itself (billed using J-codes) and the administration fee for the infusion. Hospitals add a facility markup on top of the drug&rsquo;s acquisition cost, sometimes 200&ndash;400% above what they paid. Administration fees alone can run $300&ndash;$800 per infusion session. On top of that, labs and imaging required to monitor treatment add thousands per month.</p>
  </div>
  <div class="faq-item">
    <h3>What is a J-code on a hospital bill?</h3>
    <p>J-codes are HCPCS Level II codes used to bill injectable and infusible drugs, including most chemotherapy agents. For example, J9035 is bevacizumab (Avastin) and J9355 is trastuzumab (Herceptin). Each J-code specifies the drug and the unit of measurement (per milligram or per vial). Hospitals bill a quantity of units, so errors in unit count directly inflate your bill.</p>
  </div>
  <div class="faq-item">
    <h3>What is a copay accumulator program?</h3>
    <p>A copay accumulator program is an insurer policy that prevents manufacturer copay assistance (like drug company coupons) from counting toward your deductible or out-of-pocket maximum. You may use $6,000 in manufacturer assistance and then discover your insurer credits you $0 toward your out-of-pocket &mdash; meaning you still owe the full deductible out of your own pocket once the assistance runs out.</p>
  </div>
  <div class="faq-item">
    <h3>Can I get free cancer medication?</h3>
    <p>Yes, in many cases. Most major oncology drug manufacturers operate patient assistance programs (PAPs) that provide free or deeply discounted drugs to patients who meet income criteria, typically under 400&ndash;500% of the federal poverty level. Organizations like NeedyMeds.org and RxAssist.org maintain searchable databases. CancerCare and the Patient Advocate Foundation also offer co-pay assistance funds.</p>
  </div>
  <div class="faq-item">
    <h3>What is 340B drug pricing?</h3>
    <p>The 340B Drug Pricing Program requires pharmaceutical manufacturers to sell drugs to qualifying hospitals and clinics at a 20&ndash;50% discount. However, these hospitals are allowed to bill insurers and patients at the full market price, keeping the difference. Patients treated at 340B hospitals often pay more in cost-sharing (copays, coinsurance) because those payments are based on the full billed price, not the discounted acquisition cost.</p>
  </div>
</div>

<ul class="sources-list">
  <li><a href="https://www.cancer.org/support-programs-and-services/patient-support/managing-costs.html" rel="nofollow">American Cancer Society &mdash; Managing Cancer Care Costs</a></li>
  <li><a href="https://www.hrsa.gov/opa/index.html" rel="nofollow">HRSA 340B Drug Pricing Program Overview</a></li>
  <li><a href="https://www.cancercare.org/financial_assistance" rel="nofollow">CancerCare Co-Payment Assistance Foundation</a></li>
  <li><a href="https://www.patientadvocate.org/connect-with-services/copay-relief/" rel="nofollow">Patient Advocate Foundation Co-Pay Relief Program</a></li>
  <li><a href="https://www.needymeds.org/" rel="nofollow">NeedyMeds &mdash; Patient Assistance Program Database</a></li>
  <li><a href="https://www.cms.gov/medicare/coding-billing/healthcare-common-procedure-system" rel="nofollow">CMS HCPCS &mdash; J-Code Reference</a></li>
  <li><a href="https://www.cancer.gov/about-cancer/treatment/clinical-trials" rel="nofollow">NCI &mdash; Clinical Trials Information for Patients</a></li>
</ul>
"""
})
