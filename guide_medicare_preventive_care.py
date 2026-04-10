"""Guide: Medicare Free Preventive Care Services"""

from guides import register, _embed

register("medicare-free-preventive-care", {
    "title": "Medicare Free Preventive Care: What's Covered and How to Avoid Surprise Bills",
    "meta_description": "Medicare covers many preventive services at no cost. Learn which screenings are free, the AWV vs regular physical trap, and how to avoid being billed when your 'free' visit isn't.",
    "published": "2026-04-10",
    "author": "BillKarma Team",
    "category": "Procedure Costs",
    "faqs": [
        {
            "q": "Is the Medicare Annual Wellness Visit free?",
            "a": "Yes, the Annual Wellness Visit (AWV) is free&mdash;no deductible or coinsurance if billed correctly. However, if your doctor addresses a new medical problem, a separate problem, or adjusts your medications during the visit, they may bill it as an additional office visit (E&M service) in addition to or instead of the AWV. You could receive a bill for the non-preventive portion.",
        },
        {
            "q": "Does Medicare cover an annual physical exam for free?",
            "a": "No. A traditional annual physical (comprehensive examination) is not a covered Medicare benefit. The Annual Wellness Visit (AWV) is not the same as a physical exam&mdash;the AWV focuses on health risk assessment and prevention planning, not a head-to-toe physical. If you ask your doctor for a physical and they provide one, you will be billed for an office visit.",
        },
        {
            "q": "Is a Medicare colonoscopy completely free?",
            "a": "Screening colonoscopies are covered at 100% with no cost to you. However, if polyps are found and removed during the procedure, it may be reclassified as a therapeutic (not purely screening) colonoscopy, triggering coinsurance. This reclassification trap is one of the most common Medicare billing surprises. Ask your gastroenterologist before the procedure how they will bill if polyps are removed.",
        },
        {
            "q": "How often does Medicare cover a mammogram?",
            "a": "Medicare covers a screening mammogram once every 12 months for women age 40 and older at no cost (no deductible or coinsurance). A diagnostic mammogram (ordered because of symptoms or abnormal findings) is covered but subject to the 20% Part B coinsurance.",
        },
        {
            "q": "What preventive vaccines does Medicare cover for free?",
            "a": "Medicare Part B covers the flu vaccine, COVID-19 vaccine, and pneumococcal vaccine at no cost. The hepatitis B vaccine is also covered for at-risk beneficiaries. Shingles (Shingrix) and Tdap vaccines are covered under Part D drug plans, not Part B, so your cost depends on your Part D plan.",
        },
    ],
    "body": f"""<article>
<div class="answer-box"><strong>Quick Answer:</strong> Medicare covers dozens of preventive services at no cost&mdash;no deductible, no coinsurance. But the most common trap is the Annual Wellness Visit: if your doctor addresses any new problem during your "free" AWV, you can be billed for an additional office visit. Know which services are covered, how they must be billed, and how to protect yourself from preventive care surprise bills.</div>

<nav class="toc">
    <h2>In this guide</h2>
    <ol>
        <li><a href="#welcome-to-medicare">Welcome to Medicare Visit</a></li>
        <li><a href="#awv">Annual Wellness Visit vs. Regular Physical</a></li>
        <li><a href="#cancer-screenings">Cancer Screenings</a></li>
        <li><a href="#cardiovascular">Cardiovascular Screenings</a></li>
        <li><a href="#diabetes">Diabetes Screening and Education</a></li>
        <li><a href="#mental-health">Depression and Mental Health Screening</a></li>
        <li><a href="#vaccines">Vaccines</a></li>
        <li><a href="#surprise-bills">How to Avoid Preventive Care Surprise Bills</a></li>
    </ol>
</nav>

<h2 id="welcome-to-medicare">Welcome to Medicare Visit</h2>

<p>In your first 12 months of Medicare Part B enrollment, you are entitled to a one-time <strong>Welcome to Medicare Preventive Visit</strong> (also called the "Initial Preventive Physical Examination" or IPPE). This is a free visit that covers:</p>
<ul>
    <li>A review of your medical and social history</li>
    <li>A physical examination and measurement of height, weight, BMI, and blood pressure</li>
    <li>Detection of cognitive impairment</li>
    <li>Review and update of your written preventive care plan</li>
    <li>Referrals for other preventive services you may need</li>
</ul>

<p>The Welcome to Medicare visit is free only when it is billed as a preventive service (HCPCS code G0402). If your doctor bills it as a regular evaluation and management (E&M) office visit instead, you'll be charged the 20% Part B coinsurance. Confirm before or after the visit that the billing code was preventive.</p>

<h2 id="awv">Annual Wellness Visit vs. Regular Physical</h2>

<p>This is the most important distinction in Medicare preventive care&mdash;and the source of more surprise bills than any other preventive service.</p>

<h3>Annual Wellness Visit (AWV): Free</h3>
<p>Starting in your second year of Medicare Part B (after the Welcome to Medicare visit), you can have an Annual Wellness Visit once per calendar year at no cost. The AWV covers:</p>
<ul>
    <li>Health risk assessment questionnaire</li>
    <li>Review of your health and family history</li>
    <li>Blood pressure, height, weight, BMI measurements</li>
    <li>Cognitive function assessment</li>
    <li>Personalized prevention plan with a 5-10 year screening schedule</li>
    <li>Depression screening</li>
</ul>

<h3>Regular Physical Examination: Not Covered</h3>
<p>A comprehensive physical examination&mdash;where the doctor examines your whole body, listens to your lungs, checks your reflexes, etc.&mdash;is <em>not</em> a covered Medicare service. This is one of the most common Medicare myths. If you go to your doctor requesting a "full physical," Medicare will not pay for it and you'll be billed as a regular office visit.</p>

<div class="key-takeaway">
    <strong>The AWV Billing Trap:</strong> If during your "free" Annual Wellness Visit your doctor notices you've developed a new problem (a skin lesion, elevated blood pressure requiring treatment, a new complaint), they will often appropriately bill a separate E&M service in addition to the AWV. The AWV portion remains free; the E&M visit triggers your 20% coinsurance. This is legal and proper billing&mdash;but it surprises many patients who expected to pay nothing. Ask your doctor at the start of the visit to flag if they intend to bill anything beyond the AWV.
</div>

<h2 id="cancer-screenings">Cancer Screenings</h2>

<p>Medicare covers the following cancer screenings at no cost to you:</p>

<table>
    <thead>
        <tr><th>Screening</th><th>Frequency</th><th>Who Is Covered</th><th>Cost</th></tr>
    </thead>
    <tbody>
        <tr><td>Screening mammogram</td><td>Once every 12 months</td><td>Women age 40+</td><td>$0</td></tr>
        <tr><td>Screening colonoscopy (high risk)</td><td>Every 2 years</td><td>High-risk individuals</td><td>$0 (screening only)</td></tr>
        <tr><td>Screening colonoscopy (average risk)</td><td>Every 10 years</td><td>Age 45+, average risk</td><td>$0 (screening only)</td></tr>
        <tr><td>Fecal occult blood test</td><td>Once every 12 months</td><td>Age 45+</td><td>$0</td></tr>
        <tr><td>Flexible sigmoidoscopy</td><td>Every 4 years (or after FOBT)</td><td>Age 45+</td><td>$0</td></tr>
        <tr><td>Lung cancer screening CT</td><td>Annually</td><td>Age 50&ndash;77, current/recent smoker</td><td>$0</td></tr>
        <tr><td>Cervical cancer screening (Pap)</td><td>Every 24 months (or 12 months if high risk)</td><td>Women</td><td>$0</td></tr>
        <tr><td>PSA test (prostate)</td><td>Once every 12 months</td><td>Men age 50+</td><td>$0</td></tr>
    </tbody>
</table>

<h3>The Colonoscopy Billing Trap</h3>
<p>If your doctor finds and removes polyps during a screening colonoscopy, the procedure may be reclassified as a diagnostic or therapeutic colonoscopy, triggering 20% coinsurance on the total procedure cost. The colonoscopy itself can cost $1,500&ndash;$3,000, meaning your share could be $300&ndash;$600.</p>
<p>Federal law (the ACA) established protections against this for private insurance, but Medicare billing rules differ. Many Medicare patients are surprised by a coinsurance bill after a colonoscopy. Ask your gastroenterologist: "If you find and remove a polyp, will you bill this as a screening or therapeutic colonoscopy?"</p>

<h2 id="cardiovascular">Cardiovascular Screenings</h2>

<p>Medicare covers the following cardiovascular screenings at no cost once every 5 years:</p>
<ul>
    <li>Cholesterol (total, HDL, LDL) test</li>
    <li>Lipid panel (triglycerides)</li>
    <li>Lipoprotein test</li>
</ul>

<p>Medicare also covers:</p>
<ul>
    <li><strong>Abdominal aortic aneurysm (AAA) ultrasound:</strong> One-time screening for men who have ever smoked (at least 100 cigarettes in their lifetime), in the first 12 months of Medicare enrollment</li>
    <li><strong>Cardiovascular behavioral counseling:</strong> 15-minute intensive counseling sessions for people with cardiovascular disease risk factors, covered in primary care settings</li>
</ul>

<h2 id="diabetes">Diabetes Screening and Education</h2>

<p>Medicare covers:</p>
<ul>
    <li><strong>Diabetes screening tests:</strong> Up to two fasting blood glucose tests per year if you have risk factors (obesity, hypertension, family history of diabetes)</li>
    <li><strong>Diabetes self-management training:</strong> Up to 10 hours of initial training and 2 hours annually for follow-up, at no cost after you meet your Part B deductible. Must be referred by your doctor and provided by an accredited program.</li>
    <li><strong>Diabetes prevention program:</strong> Two years of intensive behavioral counseling and lifestyle coaching for people with prediabetes, at no cost through Medicare-recognized suppliers</li>
    <li><strong>Diabetes supplies:</strong> Blood glucose monitors, test strips, and lancets covered under Medicare Part B DME benefit (with 20% coinsurance)</li>
</ul>

<h2 id="mental-health">Depression and Mental Health Screening</h2>

<p>Medicare covers annual depression screening at no cost when done in a primary care setting. This includes:</p>
<ul>
    <li>One annual depression screening per year (PHQ-2 or PHQ-9 questionnaire)</li>
    <li>Alcohol misuse screening and counseling (four sessions per year)</li>
    <li>Opioid use disorder screening and referral</li>
    <li>Tobacco cessation counseling (up to 8 sessions per year)</li>
    <li>Obesity screening and intensive behavioral counseling (weekly for first month, then as appropriate)</li>
</ul>

<h2 id="vaccines">Vaccines</h2>

<p>Medicare Part B covers these vaccines at no cost (no deductible, no coinsurance):</p>
<ul>
    <li><strong>Flu vaccine:</strong> One per season, from any provider that accepts Medicare</li>
    <li><strong>COVID-19 vaccine and boosters:</strong> Current authorized vaccines at no cost</li>
    <li><strong>Pneumococcal vaccines:</strong> PCV15 and/or PPSV23 (two vaccines in a series)</li>
    <li><strong>Hepatitis B vaccine:</strong> For at-risk beneficiaries (includes people with diabetes, kidney disease, occupational exposure)</li>
</ul>

<p>Note: The shingles (Shingrix) vaccine and Tdap vaccine are covered under Medicare Part D, not Part B. Your cost depends on your Part D plan formulary.</p>

{_embed("cost", title="Estimate Medicare Preventive Care Costs", subtitle="See what you'd pay for screenings and wellness visits.")}

<h2 id="surprise-bills">How to Avoid Preventive Care Surprise Bills</h2>

<p>Follow these steps to protect yourself from unexpected bills when receiving Medicare-covered preventive services:</p>

<ol>
    <li><strong>Before the visit:</strong> Tell your doctor's office you are scheduling your Annual Wellness Visit specifically and ask them to bill it as a preventive service (CPT codes G0438 or G0439, not 99213 or similar E&M codes).</li>
    <li><strong>During the visit:</strong> At the start, tell your doctor you want to keep the visit to AWV/preventive topics only. If you have new complaints, offer to schedule a separate appointment for those. This prevents accidental "dual billing."</li>
    <li><strong>During a colonoscopy consultation:</strong> Ask how the procedure will be billed if polyps are found. Get the answer in writing or note who said what.</li>
    <li><strong>After the visit:</strong> Check your Medicare Summary Notice within 1&ndash;2 months. Confirm the billing code shown is a preventive code. If it shows an E&M code (99202&ndash;99215) and you only had a preventive visit, dispute the billing.</li>
    <li><strong>For any free service you were charged for:</strong> Ask the provider's billing department to review the coding. Many preventive billing errors are corrected with a simple call. If not, file a Medicare redetermination request.</li>
</ol>

<ul class="sources-list">
    <li><a href="https://www.medicare.gov/coverage/preventive-screening-services" target="_blank" rel="noopener">Medicare.gov &mdash; Preventive &amp; Screening Services</a></li>
    <li><a href="https://www.cms.gov/medicare/prevention" target="_blank" rel="noopener">CMS &mdash; Medicare Prevention</a></li>
    <li><a href="https://www.medicare.gov/coverage/yearly-wellness-visits" target="_blank" rel="noopener">Medicare.gov &mdash; Annual Wellness Visits</a></li>
    <li><a href="https://www.kff.org/medicare/issue-brief/preventive-services-covered-by-private-health-plans-under-the-aca/" target="_blank" rel="noopener">KFF &mdash; Preventive Services Coverage</a></li>
</ul>
</article>""",
})
