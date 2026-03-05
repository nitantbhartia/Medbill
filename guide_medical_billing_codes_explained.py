"""Guide: Medical Billing Codes Explained."""

from guides import register, _embed

register("medical-billing-codes-explained", {
    "title": "Medical Billing Codes Explained: CPT",
    "meta_description": "Confused by medical billing codes? Plain-English guide to CPT, ICD-10, HCPCS, and DRG codes on your hospital bill. Learn to spot upcoding and billing errors.",
    "published": "2026-03-01",
    "author": "BillKarma Team",
    "category": "Billing Basics",
    "faqs": [
        {
            "q": "What are the main types of codes on a medical bill?",
            "a": "There are four main coding systems you&rsquo;ll see on medical bills. CPT (Current Procedural Terminology) codes describe what the doctor did &mdash; the procedure or service. ICD-10 codes describe the diagnosis or reason for the visit. HCPCS codes cover supplies, equipment, and drugs not included in CPT. DRG codes are used by hospitals to bundle all services for an inpatient stay into a single payment category. Your bill may contain codes from one or all of these systems depending on where and how you received care.",
        },
        {
            "q": "How do I look up what a CPT code means?",
            "a": "You can look up any CPT code using the American Medical Association&rsquo;s CPT code lookup tool at apps.ama-assn.org. You can also use our free calculator at BillKarma to see both what the code means and what Medicare pays for it in your area. Request an itemized bill from your provider if you don&rsquo;t already have one &mdash; it should list CPT codes next to each charge.",
        },
        {
            "q": "What is upcoding and how do I spot it?",
            "a": "Upcoding is when a provider bills a higher-level code than the service actually delivered. For example, billing a Level 5 office visit (CPT 99215) when you had a routine 10-minute follow-up that should be a Level 3 (CPT 99213). Signs of upcoding include charges for extended or comprehensive visits when your visit was brief, charges for complex procedures when you received a simple one, and total charges that seem out of proportion to the care you received. Compare the code description against your actual experience.",
        },
        {
            "q": "What is unbundling in medical billing?",
            "a": "Unbundling is when a provider bills separately for services that should be billed together under a single code. For example, if a surgeon bills individually for each component of a procedure that has one all-inclusive CPT code, the total is artificially inflated. Medicare&rsquo;s National Correct Coding Initiative (NCCI) maintains a list of code pairs that should not be billed separately. You can check NCCI edits at the CMS website.",
        },
        {
            "q": "Do ICD-10 codes affect how much I pay?",
            "a": "Yes, ICD-10 diagnosis codes directly affect what you pay. Your insurer uses the ICD-10 code to determine whether a service is covered and at what level. A wrong diagnosis code can result in a claim denial, higher cost-sharing, or the service being classified as not medically necessary. For example, a screening colonoscopy coded as diagnostic (rather than preventive) can shift hundreds of dollars in costs to the patient because preventive screenings are covered at 100% under the ACA.",
        },
        {
            "q": "Can I request the billing codes on my medical bill?",
            "a": "Yes. Under federal law, you have the right to request an itemized bill that includes CPT codes, ICD-10 diagnosis codes, and the charge for each line item. Call the provider&rsquo;s billing department and specifically ask for an itemized statement with procedure codes and diagnosis codes. If they only send a summary bill with descriptions like &ldquo;Lab Services&rdquo; or &ldquo;Office Visit,&rdquo; call back and request the version with codes. You need the codes to verify charges and compare against Medicare rates.",
        },
    ],
    "body": f"""
<p class="lead">Every charge on your medical bill is driven by a code &mdash; a short alphanumeric string that tells your insurer what was done, why it was done, and how much to pay. These codes determine whether your claim is approved or denied, whether you owe $50 or $5,000, and whether you&rsquo;ve been overcharged. Yet most patients never see these codes, and fewer still understand them. Medical billing errors appear on an estimated <strong>49&ndash;80% of hospital bills</strong>, and the majority of those errors involve incorrect, duplicated, or inflated codes. Understanding the basics of <a href="/guides/what-are-cpt-codes">CPT</a>, <a href="/guides/icd10-drg-codes">ICD-10, and DRG</a> codes gives you the power to read your bill, spot mistakes, and fight back.</p>

<nav class="toc">
    <h2>In this guide</h2>
    <ol>
        <li><a href="#why-codes-matter">Why billing codes matter to patients</a></li>
        <li><a href="#cpt-codes">CPT codes explained</a></li>
        <li><a href="#icd10-codes">ICD-10 codes explained</a></li>
        <li><a href="#hcpcs-codes">HCPCS codes explained</a></li>
        <li><a href="#drg-codes">DRG codes explained</a></li>
        <li><a href="#billing-code-errors">How billing codes lead to errors</a></li>
        <li><a href="#fight-your-bill">How to use billing codes to fight your bill</a></li>
        <li><a href="#faq">Frequently asked questions</a></li>
        <li><a href="#sources">Sources</a></li>
    </ol>
</nav>

<h2 id="why-codes-matter">1. Why billing codes matter to patients</h2>

<p>Billing codes are not just administrative details &mdash; they are the single biggest factor in what you pay. Every line item on your hospital bill corresponds to a code. That code determines three things:</p>

<ul>
    <li><strong>Whether your insurance covers the service.</strong> If the diagnosis code doesn&rsquo;t match the procedure code, or if the code is classified as &ldquo;not medically necessary,&rdquo; your insurer may deny the claim entirely &mdash; leaving you with the full bill.</li>
    <li><strong>How much the provider gets paid.</strong> Each CPT code has a Medicare-assigned dollar value. Hospitals and doctors use this as a baseline, then mark up. A higher-level code means a higher charge.</li>
    <li><strong>Whether you&rsquo;ve been overcharged.</strong> Upcoding (billing a higher code than warranted), unbundling (billing separately for bundled services), and duplicate codes are the three most common <a href="/guides/common-hospital-billing-errors">billing errors</a>. You can&rsquo;t catch them if you don&rsquo;t know what the codes mean.</li>
</ul>

<div class="key-takeaway">
    <strong>The bottom line:</strong> You don&rsquo;t need to memorize thousands of codes. You just need to know the four coding systems (CPT, ICD-10, HCPCS, DRG), how to look them up, and what red flags to watch for. This guide covers all of that in plain English.
</div>

<h2 id="cpt-codes">2. CPT codes explained</h2>

<p>CPT stands for Current Procedural Terminology. These are five-digit numeric codes maintained by the American Medical Association (AMA) that describe every medical service and procedure a doctor can perform. When your bill says &ldquo;Office Visit &mdash; $350,&rdquo; there&rsquo;s a CPT code behind that charge that specifies exactly what level of visit it was.</p>

<p>CPT codes fall into three main categories:</p>

<ul>
    <li><strong>Category I (most common):</strong> Standard procedures and services &mdash; office visits, surgeries, lab tests, imaging. These are the codes you&rsquo;ll see on nearly every bill.</li>
    <li><strong>Category II:</strong> Tracking codes used for performance measurement. These don&rsquo;t generate charges.</li>
    <li><strong>Category III:</strong> Temporary codes for new or experimental procedures.</li>
</ul>

<h3>The 10 most common CPT codes patients see</h3>

<table>
    <thead>
        <tr><th>CPT Code</th><th>Description</th><th>Typical Charge</th><th>Medicare Rate</th></tr>
    </thead>
    <tbody>
        <tr><td>99213</td><td>Office visit, established patient, Level 3 (15&ndash;20 min, low complexity)</td><td>$150&ndash;$300</td><td>$112</td></tr>
        <tr><td>99214</td><td>Office visit, established patient, Level 4 (25&ndash;35 min, moderate complexity)</td><td>$250&ndash;$450</td><td>$167</td></tr>
        <tr><td>99203</td><td>Office visit, new patient, Level 3 (30 min, low complexity)</td><td>$200&ndash;$400</td><td>$142</td></tr>
        <tr><td>99285</td><td>Emergency department visit, Level 5 (high complexity, immediate threat)</td><td>$1,000&ndash;$3,500</td><td>$472</td></tr>
        <tr><td>99283</td><td>Emergency department visit, Level 3 (moderate complexity)</td><td>$500&ndash;$1,500</td><td>$180</td></tr>
        <tr><td>80053</td><td>Comprehensive metabolic panel (blood test, 14 components)</td><td>$100&ndash;$400</td><td>$11</td></tr>
        <tr><td>85025</td><td>Complete blood count (CBC) with differential</td><td>$50&ndash;$200</td><td>$8</td></tr>
        <tr><td>71046</td><td>Chest X-ray, two views</td><td>$200&ndash;$750</td><td>$27</td></tr>
        <tr><td>73721</td><td>MRI of lower extremity joint (e.g., knee), without contrast</td><td>$1,000&ndash;$4,500</td><td>$240</td></tr>
        <tr><td>29881</td><td>Knee arthroscopy with meniscectomy</td><td>$5,000&ndash;$15,000</td><td>$980</td></tr>
    </tbody>
</table>

<p>Notice the gap between what hospitals charge and what Medicare pays. A comprehensive metabolic panel (CPT 80053) that Medicare values at $11 can appear on a hospital bill for $400 &mdash; a 3,500% markup. This is why looking up the <a href="/guides/what-are-cpt-codes">CPT code</a> on your bill and comparing it to the Medicare rate is the single most powerful tool you have for spotting overcharges.</p>

{_embed(mode="cost", cpt="99214", title="Look up any CPT code on your bill", subtitle="Enter a CPT code to see the Medicare rate and compare it to your charge.")}

<div class="key-takeaway">
    <strong>Pro tip:</strong> Request an itemized bill with CPT codes. If your bill only shows descriptions like &ldquo;Lab Services &mdash; $847,&rdquo; you can&rsquo;t verify anything. The CPT code is the key that unlocks the Medicare rate, the code description, and the ability to spot errors. <a href="/scan">Upload your bill to BillKarma</a> and we&rsquo;ll decode every code for you automatically.
</div>

<h2 id="icd10-codes">3. ICD-10 codes explained</h2>

<p>ICD-10 stands for the International Classification of Diseases, 10th Revision. While CPT codes describe <em>what was done</em>, ICD-10 codes describe <em>why it was done</em> &mdash; the diagnosis. Every claim submitted to your insurer must include at least one ICD-10 code that justifies the medical necessity of the service.</p>

<p>ICD-10 codes are alphanumeric, starting with a letter followed by up to six characters. They are extremely specific. For example:</p>

<ul>
    <li><strong>E11.9</strong> &mdash; Type 2 diabetes mellitus without complications</li>
    <li><strong>E11.65</strong> &mdash; Type 2 diabetes mellitus with hyperglycemia</li>
    <li><strong>M54.5</strong> &mdash; Low back pain</li>
    <li><strong>J06.9</strong> &mdash; Acute upper respiratory infection, unspecified</li>
    <li><strong>I10</strong> &mdash; Essential hypertension (high blood pressure)</li>
</ul>

<h3>Why ICD-10 codes matter for your wallet</h3>

<p>The ICD-10 code on your claim determines coverage. Here are three common scenarios where the wrong diagnosis code costs patients money:</p>

<ul>
    <li><strong>Preventive vs. diagnostic:</strong> A screening colonoscopy coded with ICD-10 Z12.11 (encounter for screening for malignant neoplasm of colon) is covered at 100% under the ACA with no cost-sharing. The same colonoscopy coded with K63.5 (polyp of colon) becomes a <em>diagnostic</em> procedure, and you may owe $1,000+ in coinsurance. If polyps are found during a preventive screening, the primary code should still reflect the screening purpose.</li>
    <li><strong>Medical necessity denials:</strong> If the ICD-10 code doesn&rsquo;t support the procedure, your insurer may deny the claim as &ldquo;not medically necessary.&rdquo; For example, an MRI billed with a diagnosis of &ldquo;general knee pain&rdquo; may be denied, while the same MRI with a specific diagnosis of &ldquo;internal derangement of knee&rdquo; is approved.</li>
    <li><strong>Pre-existing conditions and underwriting:</strong> While the ACA prohibits coverage denial for pre-existing conditions, incorrect ICD-10 codes can still create problems for certain supplemental or non-ACA-compliant plans.</li>
</ul>

<div class="key-takeaway">
    <strong>Check your diagnosis codes.</strong> Request your claim from your insurer (or look at your Explanation of Benefits) and verify that the ICD-10 codes match your actual diagnosis. If a routine screening was coded as diagnostic, or if the diagnosis code doesn&rsquo;t match what your doctor told you, ask the provider&rsquo;s billing department to correct and resubmit the claim. For a deeper dive, see our <a href="/guides/icd10-drg-codes">ICD-10 and DRG codes guide</a>.
</div>

<h2 id="hcpcs-codes">4. HCPCS codes explained</h2>

<p>HCPCS stands for Healthcare Common Procedure Coding System (pronounced &ldquo;hick-picks&rdquo;). HCPCS has two levels:</p>

<ul>
    <li><strong>Level I:</strong> This is just the CPT code system described above. The terms are used interchangeably.</li>
    <li><strong>Level II:</strong> These are alphanumeric codes (a letter followed by four digits) that cover items not included in CPT &mdash; durable medical equipment, prosthetics, orthotics, supplies, ambulance services, and drugs administered in a clinical setting.</li>
</ul>

<p>Common HCPCS Level II codes you may see on a bill:</p>

<table>
    <thead>
        <tr><th>HCPCS Code</th><th>Description</th><th>Typical Charge</th><th>Medicare Rate</th></tr>
    </thead>
    <tbody>
        <tr><td>J0135</td><td>Adalimumab (Humira) injection, 20 mg</td><td>$2,500&ndash;$6,000</td><td>$1,190</td></tr>
        <tr><td>E0601</td><td>CPAP device (continuous positive airway pressure)</td><td>$500&ndash;$2,000</td><td>$360</td></tr>
        <tr><td>L1832</td><td>Knee orthosis, custom-fitted</td><td>$400&ndash;$1,500</td><td>$290</td></tr>
        <tr><td>A4253</td><td>Blood glucose test strips, 50 per box</td><td>$30&ndash;$120</td><td>$10</td></tr>
        <tr><td>A0427</td><td>Ambulance service, ALS emergency transport</td><td>$1,500&ndash;$5,000</td><td>$490</td></tr>
    </tbody>
</table>

<p>HCPCS codes are where some of the most extreme markups appear. Drug charges in hospital settings routinely exceed the Medicare rate by 300&ndash;800%. Durable medical equipment (DME) like knee braces and CPAP machines are often billed at several times the rate you could purchase them for retail. Always compare the HCPCS code on your bill against the Medicare fee schedule, and check whether you can obtain supplies or equipment from an independent DME supplier for less. For more on drug charges specifically, see our guide to <a href="/guides/hospital-drug-charges">hospital drug pricing</a>.</p>

<h2 id="drg-codes">5. DRG codes explained</h2>

<p>DRG stands for Diagnosis-Related Group. Unlike CPT codes, which bill for each individual service, DRG codes bundle <em>everything</em> for an inpatient hospital stay into a single payment. When you&rsquo;re admitted to the hospital, Medicare (and most insurers) doesn&rsquo;t pay the hospital per procedure &mdash; it pays a lump sum based on the DRG code assigned to your stay.</p>

<p>Here&rsquo;s how it works:</p>

<ol>
    <li>You&rsquo;re admitted to the hospital for pneumonia.</li>
    <li>During your stay, you receive chest X-rays, blood tests, IV antibiotics, respiratory therapy, and nursing care.</li>
    <li>At discharge, the hospital assigns DRG 194 (simple pneumonia with major complication or comorbidity) to your stay.</li>
    <li>Medicare pays the hospital a fixed amount for DRG 194 &mdash; roughly $9,500 &mdash; regardless of how many individual tests and treatments were performed.</li>
</ol>

<h3>Why DRG codes matter to patients</h3>

<ul>
    <li><strong>DRG upcoding:</strong> Hospitals have a financial incentive to assign a higher-severity DRG because it pays more. A pneumonia stay coded as DRG 194 (with major complication) pays ~$9,500, while DRG 195 (without major complication) pays ~$6,800. If complication codes are added to your chart that don&rsquo;t reflect your actual condition, the hospital collects more &mdash; and your coinsurance may be higher.</li>
    <li><strong>Observation vs. inpatient:</strong> Whether you&rsquo;re classified as &ldquo;inpatient&rdquo; (and assigned a DRG) or &ldquo;observation&rdquo; status drastically affects your bill. Observation status means the DRG system doesn&rsquo;t apply, and you may be billed for each service individually at outpatient rates &mdash; often costing more. See our <a href="/guides/observation-status-explained">observation status guide</a> for details.</li>
</ul>

<div class="key-takeaway">
    <strong>After any hospital stay:</strong> Request your discharge summary and medical records, which will include the DRG code. Search the DRG code online to see its description and severity level. If the DRG describes complications you didn&rsquo;t have, or a severity level that doesn&rsquo;t match your experience, contact the hospital&rsquo;s billing department and ask for a review. For a complete breakdown, see our <a href="/guides/icd10-drg-codes">ICD-10 and DRG codes guide</a>.
</div>

<h2 id="billing-code-errors">6. How billing codes lead to errors</h2>

<p>According to a 2024 analysis by the American Medical Association, coding errors are present on nearly half of all medical claims. Three types of coding errors are most common &mdash; and most costly for patients.</p>

<h3>a) Upcoding</h3>

<p>Upcoding occurs when a provider bills a higher-level code than the service delivered. The most common upcoding scenario involves office visit levels. CPT codes 99211 through 99215 represent five levels of office visit complexity, with 99215 being the most complex and expensive. A routine 15-minute follow-up (Level 3, CPT 99213, Medicare rate ~$112) billed as a complex visit (Level 5, CPT 99215, Medicare rate ~$211) nearly doubles the charge.</p>

<p>For more on how often this happens, see our <a href="/guides/medical-billing-errors-statistics-2026">medical billing error statistics</a>.</p>

<h3>b) Unbundling</h3>

<p>Unbundling is billing separately for services that should be combined under a single code. For example, a comprehensive metabolic panel (CPT 80053) includes 14 individual blood tests. If the lab bills each test separately instead of using the panel code, the total can be 3&ndash;5x higher. Medicare&rsquo;s NCCI edits specifically prohibit unbundling, but it still occurs frequently on hospital bills.</p>

<h3>c) Wrong modifier or missing modifier</h3>

<p>Modifiers are two-digit codes appended to CPT codes to provide additional context. For example, modifier -59 indicates a &ldquo;distinct procedural service&rdquo; that should be paid separately. A missing modifier can cause a legitimate charge to be denied. A wrong modifier can cause an improper charge to slip through. The most commonly misused modifier is -25, which allows a provider to bill an office visit separately from a procedure performed during the same encounter.</p>

<div class="bill-example">
    <div class="bill-header">Itemized Statement &mdash; Regional Medical Center &mdash; Date of Service: 01/22/2026</div>
    <div class="line-item">
        <span>99214 &mdash; Office visit, established patient, Level 4</span>
        <span>$310.00</span>
    </div>
    <div class="line-item flagged">
        <span>99215 &mdash; Office visit, established patient, Level 5 &nbsp; &#9888; <em>Possible upcoding: visit was 20 min for a routine follow-up</em></span>
        <span>$425.00</span>
    </div>
    <div class="line-item">
        <span>36415 &mdash; Venipuncture (blood draw)</span>
        <span>$35.00</span>
    </div>
    <div class="line-item flagged">
        <span>82947 &mdash; Glucose, quantitative, blood &nbsp; &#9888; <em>Unbundling: this test is included in the metabolic panel below</em></span>
        <span>$65.00</span>
    </div>
    <div class="line-item flagged">
        <span>82310 &mdash; Calcium, total &nbsp; &#9888; <em>Unbundling: also included in the metabolic panel</em></span>
        <span>$55.00</span>
    </div>
    <div class="line-item">
        <span>80053 &mdash; Comprehensive metabolic panel</span>
        <span>$245.00</span>
    </div>
    <div class="line-item">
        <span>85025 &mdash; Complete blood count (CBC) with differential</span>
        <span>$110.00</span>
    </div>
    <div class="line-total">
        <span>TOTAL CHARGED</span>
        <span>$1,245.00</span>
    </div>
</div>

<p><strong>What this bill should look like after corrections:</strong></p>
<ul>
    <li>99215 downgraded to 99213 (routine follow-up): saves ~$200</li>
    <li>82947 and 82310 removed (already included in 80053 panel): saves $120</li>
    <li><strong>Corrected total: ~$925 &mdash; savings of $320</strong></li>
</ul>

<div class="key-takeaway">
    <strong>Spot these red flags on any bill:</strong> Two office visit codes on the same date, individual lab tests billed alongside a panel that includes them, a Level 5 visit (99215) for a routine follow-up, and any code you don&rsquo;t recognize. <a href="/scan">Upload your bill to BillKarma</a> &mdash; we automatically flag upcoding, unbundling, and duplicate charges.
</div>

<h2 id="fight-your-bill">7. How to use billing codes to fight your bill</h2>

<p>Billing codes give you a concrete, data-driven way to challenge medical charges. Here&rsquo;s the step-by-step process:</p>

<h3>Step 1 &mdash; Get the codes</h3>

<p>Request an itemized bill with CPT codes, ICD-10 diagnosis codes, and HCPCS codes for every line item. If the billing department sends a summary bill without codes, call back and specifically request the &ldquo;itemized statement with procedure and diagnosis codes.&rdquo; You have a legal right to this information.</p>

<h3>Step 2 &mdash; Look up each code</h3>

<p>For each CPT or HCPCS code, look up two things: (1) the code description, to verify it matches the service you actually received, and (2) the Medicare rate for your geographic area, which serves as the fair-market benchmark. Use our <a href="/calculator">free calculator</a> to look up any code instantly.</p>

<h3>Step 3 &mdash; Flag discrepancies</h3>

<p>Compare each line item against three criteria:</p>
<ul>
    <li><strong>Accuracy:</strong> Does the code description match what actually happened during your visit?</li>
    <li><strong>Duplication:</strong> Is the same service billed twice, or are individual components billed alongside a comprehensive code?</li>
    <li><strong>Markup:</strong> Is the charge more than 3x the Medicare rate? Markups above 300% are a strong negotiation lever.</li>
</ul>

<h3>Step 4 &mdash; Dispute with data</h3>

<p>Contact the billing department with specific code-level objections. Instead of saying &ldquo;my bill is too high,&rdquo; say: &ldquo;CPT 99215 was billed for a 20-minute routine follow-up. The documentation supports a Level 3 visit, CPT 99213. I&rsquo;m requesting a coding review and adjustment.&rdquo; Billing departments take code-level disputes far more seriously than general complaints.</p>

{_embed(mode="cost", cpt="99213", title="Compare your bill to Medicare rates", subtitle="Enter any CPT code to see what Medicare pays in your area.")}

<div class="case-study">
    <h3>Upcoding caught on an ER bill &mdash; $1,800 saved</h3>
    <p>A 38-year-old woman visited the ER for a sprained ankle. She was seen for 25 minutes, received an X-ray, an ACE bandage, and discharge instructions. Her bill showed CPT 99285 &mdash; the highest-level ER visit code, reserved for cases involving immediate threats to life or limb. The Medicare rate for 99285 is ~$472, and she was charged $2,400.</p>
    <p>She requested her medical records and confirmed no life-threatening condition was documented. She filed a written dispute arguing the visit should be coded as 99283 (moderate complexity ER visit, Medicare rate ~$180). The hospital reviewed the chart, agreed the documentation did not support a Level 5 visit, and recoded to 99283. Her charge dropped from $2,400 to $600. <strong>Savings: $1,800.</strong></p>
</div>

<div class="case-study">
    <h3>Unbundled lab charges reversed &mdash; $430 saved</h3>
    <p>A 55-year-old man with diabetes received routine blood work at his annual physical. His bill included a comprehensive metabolic panel (CPT 80053) for $285 <em>plus</em> five individual tests that are already components of that panel &mdash; glucose ($65), calcium ($55), sodium ($60), potassium ($60), and creatinine ($55). The individual tests totaled $295 on top of the panel charge.</p>
    <p>He contacted the billing department, cited the NCCI edit rules prohibiting unbundling of panel components, and requested removal of the five duplicate charges. After a 10-minute phone call, all five individual charges were removed. His lab portion of the bill dropped from $580 to $150 (after applying a more reasonable rate for the panel). <strong>Savings: $430.</strong></p>
</div>

<h2 id="faq">Frequently asked questions</h2>

<div class="faq-section">
    <div class="faq-item">
        <h3>What are the main types of codes on a medical bill?</h3>
        <p>There are four main coding systems on medical bills. CPT codes describe what the doctor did (procedures and services). ICD-10 codes describe the diagnosis (why it was done). HCPCS codes cover supplies, equipment, and drugs. DRG codes bundle all services for an inpatient stay into a single payment category. Your bill may include codes from one or all of these systems.</p>
    </div>

    <div class="faq-item">
        <h3>How do I look up what a CPT code means?</h3>
        <p>You can look up any CPT code using the AMA&rsquo;s CPT code lookup tool at apps.ama-assn.org, or use our <a href="/calculator">free calculator</a> to see both the code description and the Medicare rate for your area. Always request an itemized bill with CPT codes &mdash; you need the codes to verify charges and compare against benchmarks.</p>
    </div>

    <div class="faq-item">
        <h3>What is upcoding and how do I spot it?</h3>
        <p>Upcoding is billing a higher-level code than the service delivered. The most common example is billing a Level 5 office visit (CPT 99215) for a routine 15-minute follow-up that should be Level 3 (CPT 99213). Signs of upcoding: charges for &ldquo;comprehensive&rdquo; visits when yours was brief, and total charges that seem disproportionate to the care you received. Compare the code description to your actual experience.</p>
    </div>

    <div class="faq-item">
        <h3>What is unbundling in medical billing?</h3>
        <p>Unbundling is billing separately for services that should be billed under a single code. For example, billing individual blood tests alongside a comprehensive metabolic panel that already includes those tests. Medicare&rsquo;s NCCI edits prohibit this practice. If you see individual lab tests on a bill that also includes a panel code, those individual tests are likely duplicates.</p>
    </div>

    <div class="faq-item">
        <h3>Do ICD-10 codes affect how much I pay?</h3>
        <p>Yes. ICD-10 diagnosis codes determine whether your insurer covers a service and at what level. A wrong diagnosis code can cause a claim denial or shift hundreds of dollars in costs to you. The most common example: a preventive colonoscopy coded as &ldquo;diagnostic&rdquo; instead of &ldquo;screening&rdquo; can change your cost from $0 to over $1,000 in coinsurance.</p>
    </div>

    <div class="faq-item">
        <h3>Can I request the billing codes on my medical bill?</h3>
        <p>Yes. You have a legal right to an itemized bill with CPT codes, ICD-10 codes, and charges for each line item. Call the provider&rsquo;s billing department and specifically ask for an &ldquo;itemized statement with procedure and diagnosis codes.&rdquo; If they send a summary without codes, call back and insist. You need the codes to verify charges and compare against Medicare rates.</p>
    </div>
</div>

<h2 id="sources">Sources</h2>

<ul class="sources-list">
    <li><a href="https://www.ama-assn.org/practice-management/cpt/cpt-overview-and-code-approval" target="_blank" rel="noopener">American Medical Association &mdash; CPT Code Overview and Code Approval Process</a></li>
    <li><a href="https://www.cms.gov/medicare/coding-billing/icd-10-codes" target="_blank" rel="noopener">CMS &mdash; ICD-10 Code Sets and Classification System</a></li>
    <li><a href="https://www.cms.gov/medicare/coding-billing/healthcare-common-procedure-system" target="_blank" rel="noopener">CMS &mdash; Healthcare Common Procedure Coding System (HCPCS)</a></li>
    <li><a href="https://www.cms.gov/medicare/payment/prospective-payment-systems/acute-inpatient-pps" target="_blank" rel="noopener">CMS &mdash; Acute Inpatient PPS: Diagnosis-Related Groups (DRGs)</a></li>
    <li><a href="https://www.cms.gov/medicare/coding-billing/national-correct-coding-initiative" target="_blank" rel="noopener">CMS &mdash; National Correct Coding Initiative (NCCI) Edits</a></li>
    <li><a href="https://oig.hhs.gov/reports-and-publications/featured-topics/upcoding/" target="_blank" rel="noopener">HHS Office of Inspector General &mdash; Reports on Upcoding in Medicare Claims</a></li>
    <li><a href="https://www.healthaffairs.org/doi/10.1377/hlthaff.2024.00123" target="_blank" rel="noopener">Health Affairs &mdash; Prevalence and Cost of Billing Errors in U.S. Hospital Claims</a></li>
    <li><a href="https://www.medpac.gov/document/march-2024-report-to-the-congress/" target="_blank" rel="noopener">MedPAC &mdash; March 2024 Report to Congress: Hospital Payment and Coding Practices</a></li>
</ul>
""",
})
