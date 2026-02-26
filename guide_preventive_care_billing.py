"""Guide: Preventive Care Billing."""

from guides import register, _embed

register("preventive-care-billing", {
    "title": "Preventive Care Billing: What's Free Under Insurance and What Gets Billed",
    "meta_description": "The ACA requires insurers to cover preventive care at no cost. Learn which services are free, when preventive turns diagnostic, and how to fight wrongly-billed preventive visits.",
    "published": "2026-02-26",
    "author": "BillKarma Team",
    "category": "Insurance",
    "faqs": [
        {
            "q": "Why did I get a bill for a preventive care visit that should be free?",
            "a": "The most common reason is that the visit was coded as diagnostic rather than preventive. If your doctor addresses a new symptom, orders a test to investigate a complaint, or diagnoses a condition during a wellness visit, the visit code may change from preventive (e.g., CPT 99395) to an office visit (e.g., CPT 99213), which is subject to your deductible and copay. Ask your provider to use the correct preventive care codes.",
        },
        {
            "q": "Is a colonoscopy free under the ACA?",
            "a": "A screening colonoscopy (CPT 45378) is free for adults over 45 with no symptoms. However, if polyps are found and removed during the procedure, many insurers reclassify it as diagnostic (CPT 45385), which triggers cost-sharing. The ACA was updated to prohibit this reclassification for polyp removal during routine screening, but some plans have been slow to comply. If you were charged, appeal it.",
        },
        {
            "q": "What preventive services are free for women?",
            "a": "Under the ACA, women's preventive services covered at no cost include well-woman visits, mammograms (annually starting at age 40), cervical cancer screening (Pap smear), HPV testing, contraception and contraceptive counseling, breastfeeding support and supplies, screening for gestational diabetes, and screening for interpersonal and domestic violence. These must be covered without cost-sharing on all ACA-compliant plans.",
        },
        {
            "q": "Are vaccines free under the ACA?",
            "a": "Yes. All vaccines recommended by the Advisory Committee on Immunization Practices (ACIP) must be covered at no cost on ACA-compliant plans. This includes flu shots, COVID-19 vaccines, shingles vaccines, Tdap, HPV vaccine, and others. The vaccine must be given by an in-network provider to qualify for zero cost-sharing.",
        },
        {
            "q": "How do I appeal a preventive care bill?",
            "a": "First, check the CPT code on your EOB. If a preventive service was coded as diagnostic, call your provider and ask them to resubmit with the correct preventive code. If the insurer still denies it, file a written appeal citing the ACA preventive care mandate and the specific USPSTF recommendation that applies. Include the correct CPT code and the USPSTF grade (A or B) in your appeal letter.",
        },
    ],
    "body": f"""
<p class="lead">Under the Affordable Care Act, dozens of preventive services must be covered <strong>at zero cost</strong> to the patient&mdash;no copay, no deductible, no coinsurance. Yet millions of Americans receive surprise bills for preventive care every year. The problem isn&rsquo;t usually the law&mdash;it&rsquo;s how visits get coded. When a &ldquo;wellness check&rdquo; is billed as a &ldquo;diagnostic visit,&rdquo; your free screening suddenly costs $200&ndash;$500. Here&rsquo;s what&rsquo;s actually free, what triggers a bill, and how to fight back.</p>

<nav class="toc">
    <h2>In this guide</h2>
    <ol>
        <li><a href="#aca-mandate">The ACA preventive care mandate</a></li>
        <li><a href="#free-services">Complete list of no-cost preventive services</a></li>
        <li><a href="#preventive-vs-diagnostic">When preventive turns diagnostic</a></li>
        <li><a href="#common-traps">Common billing traps with preventive care</a></li>
        <li><a href="#fight-back">How to fight a wrongly-billed preventive visit</a></li>
        <li><a href="#protect-yourself">Protecting yourself before your visit</a></li>
        <li><a href="#faq">Frequently asked questions</a></li>
        <li><a href="#sources">Sources</a></li>
    </ol>
</nav>

<h2 id="aca-mandate">1. The ACA preventive care mandate</h2>

<p>Section 2713 of the Affordable Care Act requires all non-grandfathered health insurance plans to cover recommended preventive services without cost-sharing. The services that qualify are determined by three bodies:</p>

<ul>
    <li><strong>U.S. Preventive Services Task Force (USPSTF)</strong> &mdash; Services with an &ldquo;A&rdquo; or &ldquo;B&rdquo; recommendation grade</li>
    <li><strong>Advisory Committee on Immunization Practices (ACIP)</strong> &mdash; All recommended vaccines</li>
    <li><strong>Health Resources and Services Administration (HRSA)</strong> &mdash; Women&rsquo;s and children&rsquo;s preventive services</li>
</ul>

<p><strong>Key requirements:</strong> The service must be performed by an <strong>in-network provider</strong>, and it must be a <strong>screening</strong> (no symptoms), not a diagnostic workup. Plans must cover these services with zero copay, zero deductible, and zero coinsurance.</p>

<div class="key-takeaway">
    <strong>Important:</strong> Grandfathered plans (those that existed before March 23, 2010, and have not made significant changes) are exempt from the preventive care mandate. Check with your insurer if you are unsure whether your plan is grandfathered.
</div>

<h2 id="free-services">2. Complete list of no-cost preventive services</h2>

<p>The following services must be covered at no cost on ACA-compliant plans when ordered for screening purposes by an in-network provider:</p>

<table>
    <thead>
        <tr><th>Service</th><th>Who Qualifies</th><th>Common CPT Code</th><th>Frequency</th></tr>
    </thead>
    <tbody>
        <tr><td>Annual wellness visit</td><td>All adults</td><td>99395&ndash;99397</td><td>Annually</td></tr>
        <tr><td>Blood pressure screening</td><td>All adults</td><td>99213 (part of wellness)</td><td>Annually</td></tr>
        <tr><td>Cholesterol screening</td><td>Adults 20+; higher risk starting at 17</td><td>80061</td><td>Every 4&ndash;6 years</td></tr>
        <tr><td>Colorectal cancer screening</td><td>Adults 45&ndash;75</td><td>45378 (colonoscopy)</td><td>Every 10 years</td></tr>
        <tr><td>Depression screening</td><td>All adults</td><td>96127</td><td>Annually</td></tr>
        <tr><td>Diabetes screening (Type 2)</td><td>Adults 35&ndash;70 who are overweight</td><td>82947</td><td>Every 3 years</td></tr>
        <tr><td>Hepatitis B screening</td><td>Adults at increased risk</td><td>87340</td><td>As recommended</td></tr>
        <tr><td>Hepatitis C screening</td><td>All adults 18&ndash;79</td><td>86803</td><td>Once</td></tr>
        <tr><td>HIV screening</td><td>Adults 15&ndash;65</td><td>87389</td><td>At least once</td></tr>
        <tr><td>Lung cancer screening (low-dose CT)</td><td>Adults 50&ndash;80 with 20+ pack-year smoking history</td><td>71271</td><td>Annually</td></tr>
        <tr><td>Mammogram</td><td>Women 40+</td><td>77067</td><td>Every 1&ndash;2 years</td></tr>
        <tr><td>Cervical cancer screening (Pap)</td><td>Women 21&ndash;65</td><td>88175</td><td>Every 3 years</td></tr>
        <tr><td>Contraception</td><td>Women of reproductive age</td><td>Various</td><td>As prescribed</td></tr>
        <tr><td>All ACIP-recommended vaccines</td><td>All ages per schedule</td><td>Various</td><td>Per ACIP schedule</td></tr>
        <tr><td>Obesity screening and counseling</td><td>All adults with BMI 30+</td><td>99401&ndash;99404</td><td>As recommended</td></tr>
        <tr><td>STI screening</td><td>Sexually active adults at increased risk</td><td>87491, 87591</td><td>Annually</td></tr>
    </tbody>
</table>

<p>This is not exhaustive&mdash;USPSTF maintains over 80 recommendations with A or B grades. The full list is available at the USPSTF website.</p>

<h2 id="preventive-vs-diagnostic">3. When preventive turns diagnostic (and bills you)</h2>

<p>This is where most surprise bills come from. A visit that starts as preventive can be reclassified as diagnostic based on what happens during the appointment:</p>

<table>
    <thead>
        <tr><th>Scenario</th><th>Billed As</th><th>Cost to You</th></tr>
    </thead>
    <tbody>
        <tr><td>Annual wellness exam, no complaints discussed</td><td>Preventive (99395)</td><td>$0</td></tr>
        <tr><td>Annual wellness exam + &ldquo;I&rsquo;ve had headaches lately&rdquo;</td><td>Preventive (99395) + Diagnostic (99213)</td><td>$0 + copay/deductible for 99213</td></tr>
        <tr><td>Screening mammogram, no abnormalities</td><td>Preventive (77067)</td><td>$0</td></tr>
        <tr><td>Screening mammogram, abnormality found, additional imaging</td><td>Preventive (77067) + Diagnostic (77066)</td><td>$0 + cost-sharing for 77066</td></tr>
        <tr><td>Screening colonoscopy, no polyps</td><td>Preventive (45378)</td><td>$0</td></tr>
        <tr><td>Screening colonoscopy, polyps removed</td><td>Should still be preventive (45378/45385)</td><td>$0 (if plan complies with ACA update)</td></tr>
    </tbody>
</table>

<div class="case-study">
    <h3>Case study: $340 bill for a &ldquo;free&rdquo; annual physical</h3>
    <p><strong>Situation:</strong> Jennifer scheduled her annual wellness exam, which should be covered at 100%. During the visit, she mentioned occasional lower back pain. Her doctor spent 5 minutes discussing it and suggested stretches.</p>
    <p><strong>The bill:</strong> The office billed both a preventive visit (99395, $0 to Jennifer) and a separate office visit (99213, $185 physician fee + $155 facility fee = <strong>$340</strong>) for addressing the back pain complaint. Jennifer&rsquo;s deductible had not been met, so she owed the full $340.</p>
    <p><strong>What she did:</strong> Jennifer called the billing department and asked them to rebill the visit under the preventive code only, since the back pain discussion was brief and no separate workup was ordered. The office refused. She then filed an appeal with her insurance company, citing that the back pain was discussed incidentally and did not constitute a separate evaluation. <strong>The insurer agreed and reprocessed the claim as preventive only. Jennifer&rsquo;s bill: $0. Savings: $340.</strong></p>
</div>

{_embed(mode="cost", cpt="99395", title="Look up preventive visit costs", subtitle="See what Medicare pays for wellness exam codes.")}

<h2 id="common-traps">4. Common billing traps with preventive care</h2>

<p><strong>The &ldquo;dual visit&rdquo; split bill:</strong> As in Jennifer&rsquo;s case, mentioning any symptom or health concern during a preventive visit can trigger a second, diagnostic visit code. Suddenly your $0 wellness visit has a $150&ndash;$400 diagnostic charge attached to it. Some providers do this routinely.</p>

<p><strong>Lab work coded as diagnostic:</strong> Blood work ordered during your annual wellness exam should be coded as screening (preventive). But if the lab or provider codes it as diagnostic&mdash;for example, a lipid panel coded under a diagnostic ICD-10 code instead of a screening code&mdash;it hits your deductible. Always check the diagnosis code (ICD-10) on your lab results, not just the procedure code.</p>

<p><strong>Out-of-network providers at in-network facilities:</strong> Your in-network doctor&rsquo;s office may use an out-of-network lab. The preventive care mandate only requires zero cost-sharing with in-network providers. If an out-of-network lab processes your &ldquo;free&rdquo; screening blood work, you may receive a bill.</p>

<p><strong>Colonoscopy polyp removal reclassification:</strong> Historically, insurers reclassified a screening colonoscopy as diagnostic if polyps were found and removed, triggering cost-sharing that could exceed <strong>$1,500</strong>. The ACA was updated to prohibit this, but some plans have been slow to update their claims processing. If you are billed for polyp removal during a screening colonoscopy, appeal immediately.</p>

<div class="key-takeaway">
    <strong>The ICD-10 code matters as much as the CPT code.</strong> A cholesterol test (CPT 80061) coded with an ICD-10 screening diagnosis (Z13.220) is free. The same test coded with a diagnostic diagnosis (E78.5, hyperlipidemia) is subject to cost-sharing. Ask your provider to use screening diagnosis codes for preventive services.
</div>

<h2 id="fight-back">5. How to fight a wrongly-billed preventive visit</h2>

<ol>
    <li><strong>Get the EOB and itemized bill.</strong> Check the CPT codes and ICD-10 diagnosis codes. Identify whether the service was coded as preventive or diagnostic.</li>
    <li><strong>Call the provider&rsquo;s billing department.</strong> Ask them to review and resubmit the claim with the correct preventive CPT and ICD-10 codes. Many billing errors are resolved at this step.</li>
    <li><strong>File a formal appeal with your insurer.</strong> If the provider won&rsquo;t change the codes, appeal directly with your insurance company. Cite the specific ACA preventive care requirement and the USPSTF recommendation grade (A or B) for the service.</li>
    <li><strong>Include supporting documentation.</strong> Attach the USPSTF recommendation, the relevant CPT code, and a letter explaining that the service was a routine screening without diagnostic intent.</li>
    <li><strong>File a complaint if needed.</strong> If the insurer denies your appeal, file a complaint with your state insurance commissioner and the U.S. Department of Health and Human Services. ACA preventive care coverage is a federal requirement, and regulators take violations seriously.</li>
</ol>

<h2 id="protect-yourself">6. Protecting yourself before your visit</h2>

<p><strong>Schedule separately.</strong> If you have health concerns to discuss, book a separate appointment from your wellness visit. This prevents the dual-visit billing problem entirely.</p>

<p><strong>Tell the front desk the visit is preventive.</strong> When scheduling, explicitly say &ldquo;I&rsquo;m scheduling my annual wellness exam&rdquo; and confirm it will be billed as a preventive visit. Ask for the CPT code they plan to use.</p>

<p><strong>Be cautious about discussing symptoms.</strong> During your wellness visit, if the doctor asks &ldquo;any concerns?&rdquo; and you mention a new symptom, that can trigger a diagnostic code. If you have something to discuss, say: &ldquo;I&rsquo;d like to schedule a follow-up to discuss that separately.&rdquo;</p>

<p><strong>Verify lab orders are coded as screening.</strong> Before blood work is drawn, ask the provider to confirm the orders use screening ICD-10 codes. This takes 30 seconds and can save you hundreds of dollars.</p>

<p><strong>Confirm in-network status for all providers.</strong> Verify that the lab, imaging center, and any specialists involved in your preventive care are in-network. The zero cost-sharing guarantee only applies to in-network providers.</p>

<div class="key-takeaway">
    <strong>One sentence can save you hundreds:</strong> Before your annual wellness exam, tell the scheduling staff: &ldquo;This is a preventive wellness visit only. Please bill it under the preventive care code.&rdquo; This sets the expectation and creates a record that the visit was intended as preventive.
</div>

<h2 id="faq">Frequently asked questions</h2>

<div class="faq-section">
    <div class="faq-item">
        <h3>Why did I get a bill for a preventive care visit that should be free?</h3>
        <p>Most likely, the visit was coded as diagnostic rather than preventive. This happens when a new symptom is discussed, a diagnostic test is ordered, or the provider uses a diagnostic ICD-10 code instead of a screening code. Request the EOB, check the CPT and ICD-10 codes, and ask the provider to resubmit with preventive codes if the service was truly a screening.</p>
    </div>

    <div class="faq-item">
        <h3>Is a colonoscopy free under the ACA?</h3>
        <p>A screening colonoscopy for adults 45&ndash;75 is free under the ACA. If polyps are removed during the screening, it should still be covered at no cost (the ACA was updated to address this). If your insurer charges you for polyp removal during a screening colonoscopy, file an appeal.</p>
    </div>

    <div class="faq-item">
        <h3>What preventive services are free for women?</h3>
        <p>Free women&rsquo;s preventive services include well-woman visits, mammograms (annually from age 40), Pap smears, HPV testing, all FDA-approved contraceptives, breastfeeding support, gestational diabetes screening, and domestic violence screening. All must be provided at zero cost by in-network providers.</p>
    </div>

    <div class="faq-item">
        <h3>Are vaccines free under the ACA?</h3>
        <p>Yes. All ACIP-recommended vaccines (flu, COVID-19, shingles, Tdap, HPV, pneumonia, etc.) must be covered at no cost when administered by an in-network provider. If you are charged, the vaccine was likely given by an out-of-network provider or your plan is grandfathered.</p>
    </div>

    <div class="faq-item">
        <h3>How do I appeal a preventive care bill?</h3>
        <p>Start by asking the provider to resubmit with the correct preventive CPT and ICD-10 codes. If that fails, file a written appeal with your insurer citing the ACA Section 2713 preventive care mandate and the specific USPSTF recommendation. Include the CPT code, the USPSTF grade, and documentation that the service was a routine screening.</p>
    </div>
</div>

<h2 id="sources">Sources</h2>

<ul class="sources-list">
    <li><a href="#" target="_blank" rel="noopener">U.S. Preventive Services Task Force: A and B Recommendations (2026)</a></li>
    <li><a href="#" target="_blank" rel="noopener">Centers for Medicare &amp; Medicaid Services: Preventive Care Benefits Under the ACA</a></li>
    <li><a href="#" target="_blank" rel="noopener">HealthCare.gov: Preventive Health Services for Adults</a></li>
    <li><a href="#" target="_blank" rel="noopener">Advisory Committee on Immunization Practices: Recommended Immunization Schedule (2026)</a></li>
    <li><a href="#" target="_blank" rel="noopener">Kaiser Family Foundation: Preventive Services Tracker</a></li>
    <li><a href="#" target="_blank" rel="noopener">U.S. Department of Health and Human Services: ACA Section 2713 Implementation FAQ</a></li>
</ul>
""",
})
