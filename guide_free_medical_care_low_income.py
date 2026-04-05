"""Guide: Free Medical Care for Low-Income Patients: 12 Programs (2026)"""

from guides import register, _embed

register("free-medical-care-low-income", {
    "title": "Free Medical Care for Low-Income Patients: 12 Programs (2026)",
    "meta_description": "12 programs that provide free or heavily discounted medical care to low-income patients in 2026 — including Medicaid, FQHCs, Hill-Burton hospitals, and charity care.",
    "published": "2026-04-05",
    "author": "BillKarma Team",
    "category": "Financial Assistance",
    "faqs": [
        {
            "q": "Who qualifies for free medical care?",
            "a": "Eligibility varies by program. Medicaid generally covers adults up to 138% of the federal poverty level (FPL) in expansion states, or lower in non-expansion states. Federally Qualified Health Centers (FQHCs) use a sliding fee scale — anyone under 200% FPL pays reduced fees and those under 100% FPL typically pay nothing. Hospital charity care programs vary by institution but often cover patients up to 200–400% FPL. You don't need to be destitute to qualify for help — a family of four earning up to $60,000–$80,000 may qualify for significant discounts.",
        },
        {
            "q": "What is the Hill-Burton Act and am I eligible?",
            "a": "The Hill-Burton Act provided federal construction funds to hospitals in exchange for an obligation to provide free or reduced-cost care to people who cannot afford to pay. Some hospitals received these funds and still carry that obligation. Eligibility is based on income — typically 100–200% of the federal poverty level. To find obligated facilities in your area, use HRSA's Hill-Burton Obligated Facility Locator at findahealthcenter.hrsa.gov or call 1-800-638-0742.",
        },
        {
            "q": "How do I find a Federally Qualified Health Center near me?",
            "a": "Use HRSA's Find a Health Center tool at findahealthcenter.hrsa.gov. Enter your zip code to see all FQHCs within a set radius. You can filter by services offered. There are over 1,400 FQHC locations nationally, serving every county in the US. Call ahead to confirm their sliding fee scale and what services they provide.",
        },
        {
            "q": "What if I already received a bill — can these programs apply retroactively?",
            "a": "For hospital charity care, yes — in most cases you can apply for financial assistance retroactively, even after receiving a bill. Nonprofit hospitals under IRS 501(r) must accept charity care applications until the bill is paid in full. For Medicaid, retroactive coverage up to 3 months before the application date is available in some states. Act quickly — hospitals must pause collections while a financial assistance application is under review.",
        },
        {
            "q": "Are free clinics the same as Federally Qualified Health Centers?",
            "a": "No. FQHCs receive federal funding and must meet federal quality and staffing requirements. Free clinics are typically nonprofit organizations staffed by volunteer healthcare providers and funded by donations. Free clinics often have no income cutoff and charge nothing, but services may be more limited and wait times longer. There are over 1,200 free clinics in the US. Find one at freeclinics.us.",
        },
    ],
    "body": f"""
<p class="lead">Medical care in the US is expensive — but there are <strong>12 federal, state, and nonprofit programs</strong> that provide free or heavily reduced care to qualifying patients. Most people only know about Medicaid. But if you don't qualify for Medicaid, there are 11 other options. A family of four earning $70,000 may qualify for a sliding-scale community health center, hospital charity care, and manufacturer drug assistance — all at once.</p>

<nav class="toc">
    <h2>In this guide</h2>
    <ol>
        <li><a href="#programs">All 12 programs at a glance</a></li>
        <li><a href="#medicaid-chip">1–2: Medicaid and CHIP</a></li>
        <li><a href="#fqhc-free-clinics">3–4: FQHCs and free clinics</a></li>
        <li><a href="#hospital-charity">5–6: Hospital charity care and Hill-Burton</a></li>
        <li><a href="#federal-programs">7–10: Federal programs for specific populations</a></li>
        <li><a href="#drug-assistance">11–12: Prescription drug assistance</a></li>
        <li><a href="#how-to-apply">How to apply and what to bring</a></li>
        <li><a href="#faq">Frequently asked questions</a></li>
        <li><a href="#sources">Sources</a></li>
    </ol>
</nav>

<h2 id="programs">1. All 12 programs at a glance</h2>

<table>
    <thead>
        <tr><th>#</th><th>Program</th><th>Typical income threshold</th><th>Who it serves</th></tr>
    </thead>
    <tbody>
        <tr><td>1</td><td>Medicaid</td><td>Up to 138% FPL (expansion states)</td><td>Low-income adults, families, pregnant women, elderly, disabled</td></tr>
        <tr><td>2</td><td>CHIP</td><td>Up to 200–300% FPL (varies by state)</td><td>Children in families who earn too much for Medicaid</td></tr>
        <tr><td>3</td><td>Federally Qualified Health Centers (FQHCs)</td><td>Sliding scale; free under 100% FPL</td><td>Anyone regardless of insurance or immigration status</td></tr>
        <tr><td>4</td><td>Free Clinics</td><td>Varies; many have no income limit</td><td>Uninsured adults, typically</td></tr>
        <tr><td>5</td><td>Hospital Charity Care (IRS 501r)</td><td>Typically 200–400% FPL</td><td>Patients of nonprofit hospitals with outstanding bills</td></tr>
        <tr><td>6</td><td>Hill-Burton Act facilities</td><td>Up to 100–200% FPL</td><td>Patients near federally obligated hospitals or clinics</td></tr>
        <tr><td>7</td><td>Ryan White HIV/AIDS Program</td><td>Up to 500% FPL for some services</td><td>People living with HIV who are uninsured or underinsured</td></tr>
        <tr><td>8</td><td>Indian Health Service (IHS)</td><td>No income limit</td><td>American Indians and Alaska Natives</td></tr>
        <tr><td>9</td><td>National Health Service Corps (NHSC) sites</td><td>Sliding scale</td><td>Anyone at NHSC-approved community health sites</td></tr>
        <tr><td>10</td><td>VA Health Care</td><td>No income limit (priority groups vary)</td><td>Veterans of US military service</td></tr>
        <tr><td>11</td><td>State pharmaceutical assistance programs</td><td>Varies by state</td><td>Low-income residents needing prescription drugs</td></tr>
        <tr><td>12</td><td>Manufacturer patient assistance programs</td><td>Typically under 300–400% FPL</td><td>Uninsured or underinsured patients needing specific brand-name drugs</td></tr>
    </tbody>
</table>

<h2 id="medicaid-chip">2. Medicaid and CHIP</h2>

<h3>1. Medicaid</h3>
<p>Medicaid is the largest source of free health coverage in the US, serving over 80 million Americans. In the 40 states that expanded Medicaid under the ACA, adults with incomes up to <strong>138% of the federal poverty level</strong> ($20,780/year for an individual in 2026) qualify. Non-expansion states have narrower eligibility, often covering only pregnant women, children, and very low-income parents.</p>
<ul>
    <li><strong>What it covers:</strong> Doctor visits, hospital care, prescriptions, mental health, substance use treatment, dental (in many states), and long-term care</li>
    <li><strong>Cost:</strong> Free for most recipients; small copays in some states</li>
    <li><strong>Retroactive coverage:</strong> Some states cover up to 3 months before your application date</li>
    <li><strong>How to apply:</strong> Healthcare.gov or your state Medicaid agency (search "[your state] Medicaid apply")</li>
</ul>

<h3>2. Children's Health Insurance Program (CHIP)</h3>
<p>CHIP covers children in families that earn too much for Medicaid but cannot afford private insurance — typically up to <strong>200–300% FPL</strong>, though some states go higher. Coverage costs little to nothing.</p>
<ul>
    <li><strong>What it covers:</strong> Routine checkups, immunizations, prescriptions, dental, vision, emergency care</li>
    <li><strong>How to apply:</strong> Healthcare.gov or InsureKidsNow.gov</li>
</ul>

<h2 id="fqhc-free-clinics">3. FQHCs and free clinics</h2>

<h3>3. Federally Qualified Health Centers (FQHCs)</h3>
<p>There are over <strong>1,400 FQHC organizations</strong> operating roughly 14,000 service sites across every US county, including rural areas. FQHCs receive federal funding and are required to serve all patients regardless of ability to pay, using a sliding fee scale.</p>
<ul>
    <li><strong>Income under 100% FPL:</strong> Pay nothing or minimal fees</li>
    <li><strong>Income 100–200% FPL:</strong> Reduced fees on a sliding scale</li>
    <li><strong>Income over 200% FPL:</strong> Full fee, but often still lower than private practices</li>
    <li><strong>What they cover:</strong> Primary care, dental, mental health, substance use, pharmacy, vision, and more — varies by site</li>
    <li><strong>How to find one:</strong> findahealthcenter.hrsa.gov — enter your zip code</li>
</ul>

<h3>4. Free Clinics</h3>
<p>Over <strong>1,200 free clinics</strong> operate across the US, primarily serving uninsured adults. They are typically staffed by volunteer physicians, nurses, and pharmacists, and funded by donations. Many have no income threshold — if you are uninsured, you qualify.</p>
<ul>
    <li><strong>What they cover:</strong> Primary care, often prescription dispensing; limited specialty care</li>
    <li><strong>Limitation:</strong> Services more limited than FQHCs; wait times may be longer</li>
    <li><strong>How to find one:</strong> freeclinics.us or ask your local health department</li>
</ul>

<div class="key-takeaway">
    <strong>You don't need to be insured or a citizen to use an FQHC.</strong> FQHCs serve all patients regardless of insurance status or immigration status. They are often the fastest path to care for uninsured patients. <a href="/fight-debt">BillKarma can help if you've received a bill before finding these resources.</a>
</div>

<h2 id="hospital-charity">4. Hospital charity care and Hill-Burton</h2>

<h3>5. Hospital Charity Care (IRS 501r)</h3>
<p>Every nonprofit hospital — about 60% of US hospitals — must maintain a financial assistance program (FAP) under IRS Section 501(r). These programs can reduce or entirely eliminate your bill. Income thresholds vary, but many cover patients up to <strong>200–400% of the federal poverty level</strong>.</p>
<ul>
    <li><strong>Income under 100–138% FPL:</strong> Many hospitals provide 100% write-off (free care)</li>
    <li><strong>Income 138–300% FPL:</strong> Discounts typically range from 40–80% of the billed amount</li>
    <li><strong>Income 300–400% FPL:</strong> Discounts of 10–40% at many facilities</li>
    <li><strong>How to apply:</strong> Ask the hospital billing department for their financial assistance application; you typically need recent tax returns, pay stubs, and a bank statement</li>
    <li><strong>Key rule:</strong> The hospital must pause collection activity while your application is being reviewed</li>
</ul>

<h3>6. Hill-Burton Act</h3>
<p>The Hill-Burton Act of 1946 provided federal construction grants and loans to hospitals and other health facilities. In return, those facilities are obligated to provide a certain amount of free or reduced-cost care "in perpetuity" to patients who cannot pay. Many facilities are still discharging this obligation today.</p>
<ul>
    <li><strong>Eligibility:</strong> Generally 100–200% FPL, though the facility sets specific thresholds</li>
    <li><strong>How to find obligated facilities:</strong> HRSA Hill-Burton Obligated Facilities list at hrsa.gov, or call 1-800-638-0742</li>
    <li><strong>Important:</strong> You must apply at the facility — you can apply before or after services are received, and even after a bill has been sent to collections</li>
    <li><strong>Types of facilities:</strong> Hospitals, nursing homes, clinics, and other health facilities that received Hill-Burton funds</li>
</ul>

<h2 id="federal-programs">5. Federal programs for specific populations</h2>

<h3>7. Ryan White HIV/AIDS Program</h3>
<p>The Ryan White Program funds comprehensive care for people living with HIV who are uninsured, underinsured, or otherwise unable to afford care. It covers HIV medications (through the AIDS Drug Assistance Program), primary medical care, dental, mental health, and case management. Income limits are generous — some services are available to patients up to <strong>500% FPL</strong>.</p>
<ul>
    <li><strong>How to find services:</strong> hab.hrsa.gov or your state health department</li>
</ul>

<h3>8. Indian Health Service (IHS)</h3>
<p>The Indian Health Service provides comprehensive health care to American Indians and Alaska Natives through a network of hospitals, health centers, and clinics. There is <strong>no income limit</strong> — eligibility is based on tribal membership or Alaska Native status, not income.</p>
<ul>
    <li><strong>How to access:</strong> ihs.gov — enter your location to find the nearest IHS facility</li>
</ul>

<h3>9. National Health Service Corps (NHSC) Sites</h3>
<p>The NHSC places healthcare providers in high-need communities in exchange for loan repayment. NHSC-approved sites must offer a sliding fee discount program. These sites are often FQHCs, but not always. Use HRSA's tool to find NHSC sites near you.</p>

<h3>10. VA Health Care</h3>
<p>Veterans enrolled in VA health care receive comprehensive services — primary care, mental health, surgery, prescriptions, and more — at low or no cost. There is no income requirement to enroll, though copays vary by "priority group" based on service-connected conditions and income.</p>
<ul>
    <li><strong>How to enroll:</strong> va.gov/health-care/apply or call 1-877-222-8387</li>
    <li><strong>Key point:</strong> Many veterans who are eligible never enroll — enrollment does not commit you to using only the VA</li>
</ul>

<h2 id="drug-assistance">6. Prescription drug assistance</h2>

<h3>11. State pharmaceutical assistance programs</h3>
<p>Many states run programs to help low- and moderate-income residents afford prescription drugs. These programs vary widely — some provide free medications, others provide rebates or help pay Medicare Part D costs. Search "[your state] pharmaceutical assistance program" or check NeedyMeds.org.</p>

<h3>12. Manufacturer patient assistance programs</h3>
<p>Most major pharmaceutical manufacturers operate programs that provide free or heavily discounted brand-name drugs to qualifying patients. Income limits vary but are often generous — up to <strong>300–400% FPL</strong> in many cases.</p>
<ul>
    <li><strong>RxAssist:</strong> rxassist.org — database of manufacturer programs</li>
    <li><strong>NeedyMeds:</strong> needymeds.org — broader database including state, nonprofit, and manufacturer programs</li>
    <li><strong>Partnership for Prescription Assistance:</strong> pparx.org</li>
    <li><strong>To apply:</strong> Most require a prescription from your doctor, proof of income, and an application from the manufacturer's website</li>
</ul>

<div class="key-takeaway">
    <strong>Already received a bill? You can still apply for many of these programs.</strong> Hospital charity care, Hill-Burton, and manufacturer assistance programs can often be applied retroactively. <a href="/fight-debt">BillKarma can help you identify which programs apply to your specific situation.</a>
</div>

<h2 id="how-to-apply">7. How to apply and what to bring</h2>

<p>For most financial assistance programs, you will need some combination of the following:</p>

<ol>
    <li><strong>Proof of income:</strong> Recent pay stubs (last 30–60 days), or last year's federal tax return (Form 1040). If unemployed, bring a termination letter or documentation of benefits received.</li>
    <li><strong>Photo ID:</strong> Driver's license, state ID, or passport. Some programs accept foreign identification documents.</li>
    <li><strong>Proof of address:</strong> Utility bill, lease, or official mail — must match your current address.</li>
    <li><strong>Social Security number:</strong> Required for Medicaid, CHIP, and most federal programs. Not required for FQHCs or free clinics.</li>
    <li><strong>Your medical bill:</strong> For charity care applications, bring your itemized bill with account number.</li>
    <li><strong>Insurance information:</strong> Even if inadequate, bring your insurance card. Some programs require you to be uninsured or underinsured — your insurer denial letter may be needed.</li>
</ol>

{_embed(mode="fight", title="Have a bill you can't pay?", subtitle="BillKarma can help identify financial assistance programs for your specific bill.")}

<h2 id="faq">Frequently asked questions</h2>

<div class="faq-section">
    <div class="faq-item">
        <h3>Who qualifies for free medical care?</h3>
        <p>It depends on the program, but many people who assume they don't qualify actually do. A family of four earning up to $60,000–$80,000 may qualify for sliding-scale FQHCs, hospital charity care at some facilities, and CHIP for their children — simultaneously. You don't have to be destitute to get help.</p>
    </div>

    <div class="faq-item">
        <h3>Can I use an FQHC if I'm not a US citizen?</h3>
        <p>Yes. FQHCs are federally required to serve all patients regardless of citizenship or immigration status. Free clinics also typically have no citizenship requirement. You do not need a Social Security number to receive care at most FQHCs.</p>
    </div>

    <div class="faq-item">
        <h3>What is the Hill-Burton obligation and how do I find it?</h3>
        <p>Facilities that received Hill-Burton federal construction funds must provide free or reduced care to patients who cannot pay. To find obligated facilities, use HRSA's online locator at hrsa.gov or call 1-800-638-0742. Apply directly at the facility — eligibility is based on income, typically 100–200% FPL.</p>
    </div>

    <div class="faq-item">
        <h3>Can I apply for charity care after a bill goes to collections?</h3>
        <p>Yes. Under IRS 501(r), nonprofit hospitals must accept financial assistance applications until a bill is paid in full. If the hospital sent your bill to collections before informing you about financial assistance, they may have violated federal rules. Submit your application immediately — collection activity must pause while the application is under review.</p>
    </div>

    <div class="faq-item">
        <h3>Are manufacturer patient assistance programs legitimate?</h3>
        <p>Yes — they are run directly by the pharmaceutical manufacturers (Pfizer, AstraZeneca, Eli Lilly, Novo Nordisk, etc.) and have provided free medications to millions of patients. Apply through the manufacturer's official website or via NeedyMeds.org, which aggregates programs across manufacturers. Never pay a third party to "apply for you."</p>
    </div>
</div>

<h2 id="sources">Sources</h2>

<ul class="sources-list">
    <li><a href="https://findahealthcenter.hrsa.gov/" target="_blank" rel="noopener">HRSA: Find a Health Center — FQHC Locator</a></li>
    <li><a href="https://www.hrsa.gov/hill-burton/index.html" target="_blank" rel="noopener">HRSA: Hill-Burton Free and Reduced-Cost Health Care Program</a></li>
    <li><a href="https://www.medicaid.gov/medicaid/eligibility/index.html" target="_blank" rel="noopener">CMS: Medicaid Eligibility</a></li>
    <li><a href="https://www.insurekidsnow.gov/" target="_blank" rel="noopener">InsureKidsNow.gov: CHIP Enrollment</a></li>
    <li><a href="https://hab.hrsa.gov/about-ryan-white-hivaids-program" target="_blank" rel="noopener">HRSA: Ryan White HIV/AIDS Program</a></li>
    <li><a href="https://www.ihs.gov/" target="_blank" rel="noopener">Indian Health Service</a></li>
    <li><a href="https://www.va.gov/health-care/eligibility/" target="_blank" rel="noopener">VA Health Care Eligibility and Enrollment</a></li>
    <li><a href="https://www.needymeds.org/" target="_blank" rel="noopener">NeedyMeds: Manufacturer and State Drug Assistance Programs</a></li>
    <li><a href="https://www.irs.gov/charities-non-profits/community-health-needs-assessment-for-charitable-hospital-organizations-section-501r3" target="_blank" rel="noopener">IRS Section 501(r): Nonprofit Hospital Charity Care Requirements</a></li>
</ul>
""",
})
