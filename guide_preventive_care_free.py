"""Guide: What Preventive Care Is Free Under Your Insurance in 2026?"""

from guides import register, _embed

register("what-preventive-care-is-free", {
    "title": "What Preventive Care Is Free Under Your Insurance in 2026?",
    "meta_description": "The ACA requires most plans to cover USPSTF Grade A/B preventive services at $0. Here is the full list of free screenings, vaccines, and counseling — and how to fight a wrongful charge.",
    "published": "2026-04-05",
    "author": "BillKarma Team",
    "category": "Insurance Basics",
    "faqs": [
        {
            "q": "Does free preventive care apply before I meet my deductible?",
            "a": "Yes. ACA-compliant plans must cover USPSTF Grade A and B preventive services at $0 cost-sharing with no deductible requirement. You pay nothing for covered preventive services even if you have not spent a dollar toward your deductible yet.",
        },
        {
            "q": "What happens if I talk about a health problem during my preventive visit?",
            "a": "If your provider addresses a new or ongoing medical problem during a preventive visit, they may bill a separate evaluation and management (E&M) code in addition to the preventive visit code. That second service is not preventive and can trigger your deductible and coinsurance. Ask your provider to schedule a separate visit for any problems, or to clearly code the visit as preventive-only.",
        },
        {
            "q": "Do grandfathered health plans have to cover preventive care for free?",
            "a": "No. Grandfathered plans — those that existed before March 23, 2010 and have not made significant changes — are exempt from the ACA's preventive care requirements. If your plan is grandfathered, check your Summary of Benefits and Coverage (SBC) document.",
        },
        {
            "q": "What is the Braidwood case and does it affect my free preventive care?",
            "a": "In Braidwood Management v. Becerra, a federal court ruled that USPSTF recommendations issued after 2010 may not be enforceable as mandatory coverage. This is being litigated and may affect PrEP, some cancer screenings, and other recommendations added after the ACA passed. As of 2026, most insurers continue to cover preventive services, but check your plan's current coverage.",
        },
        {
            "q": "How do I dispute a charge for preventive care that should have been free?",
            "a": "Start by requesting the Explanation of Benefits (EOB) and the claim's CPT codes. If you were charged cost-sharing for a preventive service (CPT codes 99381–99397 or HCPCS Z-codes), file an internal appeal with your insurer citing ACA Section 2713. If the appeal is denied, file a complaint with your state insurance commissioner or the federal marketplace at HealthCare.gov.",
        },
    ],
    "body": f"""
<p class="lead">Under the Affordable Care Act, most health insurance plans are required to cover a broad list of preventive services at <strong>absolutely no cost to you</strong> &mdash; no copay, no coinsurance, no deductible. Yet BillKarma data shows that <strong>42% of patients who should pay $0 for preventive care are incorrectly charged</strong>. Knowing exactly what is covered, and how to fight a wrongful bill, can save you hundreds every year.</p>

<nav class="toc">
    <h2>In this guide</h2>
    <ol>
        <li><a href="#how-it-works">How the ACA preventive care rule works</a></li>
        <li><a href="#screenings">Free screenings by category</a></li>
        <li><a href="#vaccines">Free vaccines for adults and children</a></li>
        <li><a href="#medications">Free preventive medications</a></li>
        <li><a href="#counseling">Free counseling services</a></li>
        <li><a href="#billing-trap">The preventive visit billing trap</a></li>
        <li><a href="#dispute">How to dispute a wrongful charge</a></li>
        <li><a href="#faq">Frequently asked questions</a></li>
        <li><a href="#sources">Sources</a></li>
    </ol>
</nav>

<h2 id="how-it-works">1. How the ACA preventive care rule works</h2>

<p>ACA Section 2713 requires non-grandfathered health plans to cover preventive services recommended by the U.S. Preventive Services Task Force (USPSTF) with a Grade A or B rating at <strong>zero cost-sharing</strong>. That means no copay, no coinsurance, and no deductible applied &mdash; even on high-deductible plans. The same rule applies to Advisory Committee on Immunization Practices (ACIP) vaccine recommendations and HRSA women&rsquo;s and children&rsquo;s preventive care guidelines.</p>

<div class="key-takeaway">
    <strong>The key rule:</strong> The service must be delivered by an in-network provider for the $0 requirement to apply. Going out-of-network for a preventive service may still trigger cost-sharing depending on your plan type. Always confirm the provider is in-network before the visit.
</div>

<table>
    <thead>
        <tr><th>Recommendation Source</th><th>What It Covers</th><th>Grade Required</th></tr>
    </thead>
    <tbody>
        <tr><td><strong>USPSTF</strong></td><td>Screenings, counseling, preventive medications for adults</td><td>Grade A or B</td></tr>
        <tr><td><strong>ACIP</strong></td><td>Vaccines for children and adults</td><td>Any ACIP recommendation</td></tr>
        <tr><td><strong>HRSA Bright Futures</strong></td><td>Well-child visits, developmental screenings</td><td>All recommendations</td></tr>
        <tr><td><strong>HRSA Women&rsquo;s Guidelines</strong></td><td>Well-woman visits, contraception, breastfeeding support</td><td>All recommendations</td></tr>
    </tbody>
</table>

<h2 id="screenings">2. Free screenings by category</h2>

<p>The following screenings are covered at $0 for patients who meet the age and risk criteria. Coverage applies when the service is ordered for screening purposes &mdash; not to investigate symptoms.</p>

<table>
    <thead>
        <tr><th>Screening</th><th>Who Qualifies</th><th>Frequency</th></tr>
    </thead>
    <tbody>
        <tr><td>Blood pressure screening</td><td>All adults 18+</td><td>At least every 2 years if normal</td></tr>
        <tr><td>Cholesterol screening</td><td>Adults 35+ (men), 20+ with risk factors</td><td>Every 5 years</td></tr>
        <tr><td>Colorectal cancer (colonoscopy, stool tests)</td><td>Adults ages 45&ndash;75</td><td>Colonoscopy every 10 years; stool tests annually</td></tr>
        <tr><td>Cervical cancer (Pap smear)</td><td>Women ages 21&ndash;65</td><td>Every 3 years (Pap alone); every 5 years (Pap + HPV co-test, ages 30&ndash;65)</td></tr>
        <tr><td>Breast cancer (mammogram)</td><td>Women ages 40&ndash;74</td><td>Every 1&ndash;2 years (ongoing debate on optimal interval)</td></tr>
        <tr><td>Lung cancer (low-dose CT)</td><td>Adults ages 50&ndash;80, 20+ pack-year smoking history, currently smoke or quit within 15 years</td><td>Annually</td></tr>
        <tr><td>Diabetes screening</td><td>Adults ages 35&ndash;70 who are overweight or obese</td><td>Every 3 years</td></tr>
        <tr><td>HIV screening</td><td>All adults ages 15&ndash;65; younger/older if at increased risk</td><td>At least once; annually if high risk</td></tr>
        <tr><td>Hepatitis B screening</td><td>Adults at increased risk; all adolescents</td><td>Once; periodically if risk persists</td></tr>
        <tr><td>Hepatitis C screening</td><td>Adults ages 18&ndash;79</td><td>Once for most; annually if ongoing risk</td></tr>
        <tr><td>STI screening (chlamydia, gonorrhea, syphilis)</td><td>Sexually active women under 24; older women at increased risk; pregnant women</td><td>Annually</td></tr>
        <tr><td>Vision screening</td><td>Children through age 5</td><td>At well-child visits</td></tr>
        <tr><td>Hearing screening</td><td>Newborns</td><td>Once at birth</td></tr>
    </tbody>
</table>

{_embed(mode="cpt", cpt="82270", title="Look up colonoscopy and screening costs", subtitle="See what Medicare pays for common preventive screenings.")}

<h2 id="vaccines">3. Free vaccines for adults and children</h2>

<p>All vaccines recommended by the Advisory Committee on Immunization Practices (ACIP) must be covered at $0 cost-sharing for both adults and children. The list below covers the most commonly billed vaccines:</p>

<ul>
    <li><strong>Flu (influenza):</strong> Annually for everyone 6 months and older</li>
    <li><strong>Tdap / Td:</strong> Tdap once as an adult, Td booster every 10 years</li>
    <li><strong>MMR (measles, mumps, rubella):</strong> Two doses if not previously vaccinated</li>
    <li><strong>Varicella (chickenpox):</strong> Two doses if not immune</li>
    <li><strong>HPV (Gardasil 9):</strong> Routine at ages 11&ndash;12; catch-up through age 26 covered at $0 under ACA; ages 27&ndash;45 covered at $0 on plans that follow ACIP recommendations (coverage varies)</li>
    <li><strong>Pneumococcal (PCV15, PCV20, PPSV23):</strong> Adults 65+; younger adults with certain conditions</li>
    <li><strong>Shingles (Shingrix):</strong> Adults 50+ (two doses)</li>
    <li><strong>COVID-19:</strong> Recommended doses per current ACIP schedule</li>
    <li><strong>Hepatitis A:</strong> Two doses; all children at age 1, catch-up for adults at risk</li>
    <li><strong>Hepatitis B:</strong> Three doses; recommended for all unvaccinated adults through age 59; ages 60+ based on shared decision-making</li>
    <li><strong>RSV vaccine:</strong> Adults 60+ (one dose, shared decision-making)</li>
</ul>

<div class="key-takeaway">
    <strong>Watch for administration fees:</strong> Some providers bill a separate vaccine administration fee in addition to the vaccine itself. Both the vaccine and its administration must be covered at $0 under ACA-compliant plans. If you are charged an administration fee for a covered vaccine, that is a billing error. See our guide to <a href="/guides/hpv-vaccine-cost/">HPV vaccine billing</a> for a specific example.
</div>

<h2 id="medications">4. Free preventive medications</h2>

<p>The ACA also requires coverage of certain medications prescribed for prevention &mdash; not treatment &mdash; at no cost-sharing. Key examples include:</p>

<ul>
    <li><strong>Aspirin:</strong> Low-dose for adults ages 40&ndash;59 with 10% or greater 10-year cardiovascular disease risk who are not at increased bleeding risk (USPSTF Grade B)</li>
    <li><strong>Statins:</strong> Low-to-moderate dose for adults ages 40&ndash;75 with one or more CVD risk factors and 10%+ 10-year CVD event risk (USPSTF Grade B)</li>
    <li><strong>PrEP (pre-exposure prophylaxis for HIV):</strong> For adults at increased risk of HIV infection &mdash; this includes the medication and required monitoring labs (USPSTF Grade A; subject to Braidwood litigation)</li>
    <li><strong>Folic acid:</strong> 0.4&ndash;0.8 mg daily for people planning or capable of pregnancy (USPSTF Grade A)</li>
    <li><strong>Fluoride supplementation:</strong> For children ages 6 months through 5 years without fluoride in their water supply</li>
</ul>

<h2 id="counseling">5. Free counseling services</h2>

<p>Behavioral health counseling for prevention &mdash; not treatment of a diagnosed condition &mdash; is covered at $0 under ACA guidelines:</p>

<ul>
    <li><strong>Obesity counseling:</strong> Adults with a BMI of 30 or higher; intensive behavioral counseling for weight loss</li>
    <li><strong>Tobacco and smoking cessation:</strong> All adults who use tobacco; at least two quit-attempt counseling sessions per year</li>
    <li><strong>Depression screening:</strong> All adults; adolescents ages 12&ndash;18</li>
    <li><strong>Alcohol misuse screening and counseling:</strong> All adults 18+</li>
    <li><strong>Domestic and intimate partner violence screening:</strong> Women of reproductive age</li>
    <li><strong>Healthy diet and physical activity counseling:</strong> Adults with cardiovascular risk factors</li>
</ul>

<p>Well-woman visits and well-child visits (per Bright Futures schedule) are also covered in full. The well-woman visit covers a comprehensive preventive exam including the services above relevant to women&rsquo;s health. Well-child visits at ages 0, 1, 2, 4, 6, 9, 12, 15, 18, 24, and 30 months and annually from ages 3 through 21 are covered at $0.</p>

<h2 id="billing-trap">6. The preventive visit billing trap</h2>

<p>The single most common billing problem with preventive care: you go in for your annual physical and mention a symptom or existing condition. Your provider addresses it during the same visit. The visit is now partially &ldquo;diagnostic,&rdquo; and you receive a bill for cost-sharing on the diagnostic portion.</p>

<ol>
    <li><strong>What happens in the billing system:</strong> The provider bills a preventive visit code (e.g., CPT 99395 for adults ages 40&ndash;64) plus a separate evaluation and management (E&M) code (e.g., 99213 or 99214) for the problem addressed. Insurance covers the preventive code at $0 but applies your deductible and coinsurance to the E&M code.</li>
    <li><strong>This is legal</strong> &mdash; the provider is allowed to bill for both services on the same day. You are not being scammed. But you can manage it.</li>
    <li><strong>How to avoid it:</strong> At the start of your preventive visit, tell your provider explicitly: &ldquo;I&rsquo;d like this coded as a preventive visit only. If we need to address any problems, can we schedule a separate appointment or a separate visit today?&rdquo;</li>
    <li><strong>How to catch it after the fact:</strong> Review your EOB. If you see both a preventive code (99381&ndash;99397) and an E&M code billed on the same day, you will likely have a patient balance on the E&M. This is only a billing error if the provider did not actually address a separate problem.</li>
    <li><strong>If you were charged cost-sharing on the preventive code itself</strong> (not the E&M), that is always a billing error and should be disputed.</li>
</ol>

<div class="case-study">
    <h3>Case study: $180 charge on a free annual physical</h3>
    <p><strong>Situation:</strong> Maria went in for her annual preventive exam. While there, she mentioned her knee had been bothering her. The provider examined the knee and recommended an X-ray. Maria received a bill for $180 afterward.</p>
    <p><strong>What happened:</strong> The provider billed CPT 99395 (preventive visit, covered at $0) and CPT 99213 (office visit for knee complaint, subject to her $1,500 deductible). The $180 represented the allowed amount for the E&M visit, applied to her unmet deductible.</p>
    <p><strong>What she could have done:</strong> Asked the provider to schedule a separate visit for the knee complaint. The preventive visit would remain $0. The knee visit would still apply to her deductible, but she would have had the choice to delay it.</p>
    <p><strong>Lesson:</strong> Keep your preventive visit clean. Save non-urgent concerns for a separate appointment, or at least understand upfront that addressing them will trigger cost-sharing.</p>
</div>

<h2 id="dispute">7. How to dispute a wrongful charge for preventive care</h2>

<p>If you receive a bill for a service that should have been free, follow these steps:</p>

<ol>
    <li><strong>Get the CPT codes.</strong> Request an itemized bill from your provider showing the exact CPT codes billed. Preventive visits are coded 99381&ndash;99397. Individual screenings have their own codes (e.g., colonoscopy screening: G0121; mammogram: 77067).</li>
    <li><strong>Check your EOB.</strong> Log into your insurer&rsquo;s portal and pull the Explanation of Benefits for the date of service. Confirm whether the claim was processed as preventive. If the claim shows a patient liability on a preventive code, the insurer processed it incorrectly.</li>
    <li><strong>Call your insurer first.</strong> Many errors are resolved with a single call. Reference ACA Section 2713 and the specific USPSTF Grade A/B recommendation. Ask the insurer to reprocess the claim as preventive.</li>
    <li><strong>File a formal internal appeal</strong> if the call does not resolve it. Submit in writing. Include your EOB, the itemized bill, the CPT code in question, and a printout of the USPSTF recommendation showing Grade A or B status and that you meet the age/risk criteria.</li>
    <li><strong>File a complaint externally</strong> if the internal appeal fails. Options: your state insurance commissioner&rsquo;s office, the federal marketplace complaint portal at HealthCare.gov, or the Department of Labor (for employer-sponsored plans). External review is free and the insurer must comply with the decision.</li>
    <li><strong>Use BillKarma.</strong> <a href="/fight-debt">Upload your bill</a> and we will identify which charges should have been covered at $0 and generate a dispute letter with the correct regulatory citations.</li>
</ol>

<div class="key-takeaway">
    <strong>BillKarma finding:</strong> 42% of patients who qualify for $0 preventive care are incorrectly charged. The most common errors are applying a deductible to a covered screening, billing a vaccine administration fee as non-preventive, and misclassifying a preventive visit as a standard office visit. If your bill looks wrong, it probably is. <a href="/fight-debt">Let BillKarma check it.</a>
</div>

<h2 id="faq">Frequently asked questions</h2>

<div class="faq-section">
    <div class="faq-item">
        <h3>Does free preventive care apply before I meet my deductible?</h3>
        <p>Yes. ACA-compliant plans must cover USPSTF Grade A and B preventive services at $0 regardless of your deductible status. You pay nothing for covered preventive services even if you have not spent anything toward your deductible yet.</p>
    </div>

    <div class="faq-item">
        <h3>What happens if I talk about a health problem during my preventive visit?</h3>
        <p>The provider may bill a separate evaluation and management code for the problem discussed, which is not considered preventive. That portion can trigger your deductible and coinsurance. To avoid this, ask your provider to schedule a separate visit for any problems, or at minimum understand upfront that addressing them will result in additional charges.</p>
    </div>

    <div class="faq-item">
        <h3>Do grandfathered health plans have to cover preventive care for free?</h3>
        <p>No. Grandfathered plans are exempt from ACA preventive care requirements. Check your Summary of Benefits and Coverage document to see if your plan is grandfathered.</p>
    </div>

    <div class="faq-item">
        <h3>What is the Braidwood case and does it affect my free preventive care?</h3>
        <p>The Braidwood litigation challenges whether USPSTF recommendations issued after 2010 can be mandated as free coverage. As of 2026, most insurers continue to cover the full list of preventive services, but PrEP and some newer recommendations may face plan-by-plan variation while the case is resolved. Check your plan&rsquo;s current Summary of Benefits.</p>
    </div>

    <div class="faq-item">
        <h3>How do I dispute a charge for preventive care that should have been free?</h3>
        <p>Request the itemized bill with CPT codes, compare it to your EOB, and file an internal appeal with your insurer citing ACA Section 2713 and the specific USPSTF Grade A/B recommendation. If the internal appeal fails, escalate to your state insurance commissioner or the federal marketplace complaint portal.</p>
    </div>
</div>

<h2 id="sources">Sources</h2>

<ul class="sources-list">
    <li><a href="#" target="_blank" rel="noopener">U.S. Preventive Services Task Force: A and B Recommendations (2026)</a></li>
    <li><a href="#" target="_blank" rel="noopener">HealthCare.gov: Preventive Care Benefits for Adults</a></li>
    <li><a href="#" target="_blank" rel="noopener">ACA Section 2713: Coverage of Preventive Health Services</a></li>
    <li><a href="#" target="_blank" rel="noopener">Centers for Disease Control and Prevention: ACIP Vaccine Recommendations</a></li>
    <li><a href="#" target="_blank" rel="noopener">HRSA: Women&rsquo;s Preventive Services Guidelines</a></li>
    <li><a href="#" target="_blank" rel="noopener">Braidwood Management, Inc. v. Becerra, 5th Circuit Court of Appeals</a></li>
    <li><a href="#" target="_blank" rel="noopener">Kaiser Family Foundation: Preventive Services Coverage Under the ACA (2025)</a></li>
</ul>
""",
})
