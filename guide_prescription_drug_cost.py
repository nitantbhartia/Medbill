"""Guide: How to Pay Less for Prescription Drugs in 2026."""

from guides import register, _embed

register("prescription-drug-cost-without-insurance", {
    "title": "How to Pay Less for Prescription Drugs in 2026",
    "meta_description": "130 million Americans take at least one prescription drug. Learn 11 proven strategies\u2014from GoodRx to Cost Plus Drugs\u2014that can cut your drug costs by 50\u201390%.",
    "published": "2026-04-05",
    "author": "BillKarma Team",
    "category": "Procedure Costs",
    "faqs": [
        {
            "q": "Is GoodRx always cheaper than my insurance copay?",
            "a": "Not always. GoodRx is frequently cheaper than your insurance copay for generic medications, especially at large pharmacy chains like Walmart, Costco, and Kroger. But if you have a low-tier copay (e.g., $5\u2013$10 for a Tier 1 generic) or you\u2019re close to your out-of-pocket maximum, using your insurance may be cheaper. Always compare both prices at the pharmacy counter before deciding. One important note: using GoodRx instead of insurance means the payment does not count toward your deductible or out-of-pocket maximum.",
        },
        {
            "q": "What is Cost Plus Drugs and how does it work?",
            "a": "Cost Plus Drugs (costplusdrugs.com), founded by Mark Cuban, sells generic medications at manufacturing cost plus a 15% markup plus a small pharmacy dispensing fee. For many common generics, this results in prices dramatically lower than retail pharmacy prices. For example, imatinib (generic Gleevec for leukemia) costs under $20 per month on Cost Plus Drugs vs. thousands at retail. It requires a valid prescription but no insurance. It works best for generic medications you take long-term.",
        },
        {
            "q": "How do I find manufacturer patient assistance programs?",
            "a": "Most major pharmaceutical manufacturers offer patient assistance programs (PAPs) for low-income patients who are uninsured or underinsured. To find them, go directly to the manufacturer\u2019s website and search for &ldquo;patient assistance&rdquo; or visit NeedyMeds.org, which maintains a free database of over 4,000 programs. Requirements typically include income at or below 200\u2013400% of the federal poverty level, U.S. residency, and no coverage for the specific drug. The application is usually handled by your doctor&rsquo;s office.",
        },
        {
            "q": "What is the $35/month insulin cap?",
            "a": "The Inflation Reduction Act (2022) capped Medicare Part D insulin cost-sharing at $35 per month per insulin product. The Affordable Care Act extended similar caps to most commercial health plans. As of 2026, most insured patients should not pay more than $35 per month for insulin through their health plan. If you are being charged more than $35, contact your insurer&mdash;this is likely a billing error. Uninsured patients do not benefit from the cap but can access $25 over-the-counter ReliOn insulin at Walmart.",
        },
        {
            "q": "When should I ask my doctor for a 90-day supply?",
            "a": "For any chronic maintenance medication you take daily, a 90-day supply typically costs 20\u201333% less per dose than three 30-day fills, especially through mail-order pharmacy. Most plans allow 90-day fills for maintenance medications (blood pressure, cholesterol, diabetes, thyroid, antidepressants) after the first 30-day fill. Ask your doctor to write the prescription for a 90-day supply with refills, and contact your insurance\u2019s mail-order pharmacy. This can save $100\u2013$600 per year for patients on multiple chronic medications.",
        },
    ],
    "body": f"""
<p class="lead">An estimated <strong>130 million Americans</strong> take at least one prescription drug, and 29% report not filling a prescription in the past year because of cost&mdash;most without knowing the alternatives available to them. Generic strategies, discount programs, and direct-to-consumer pharmacies can cut typical drug costs by <strong>50 to 90%</strong>. This guide covers every major strategy, who it works for, and how to use it.</p>

<nav class="toc">
    <h2>In this guide</h2>
    <ol>
        <li><a href="#generic-vs-brand">Generic vs. brand-name drugs</a></li>
        <li><a href="#discount-programs">GoodRx, Blink Health, and discount card programs</a></li>
        <li><a href="#cost-plus">Mark Cuban\u2019s Cost Plus Drugs and direct-to-consumer options</a></li>
        <li><a href="#manufacturer-assistance">Manufacturer patient assistance programs</a></li>
        <li><a href="#supply-strategies">90-day supply, pill splitting, and OTC switches</a></li>
        <li><a href="#insurance-strategies">Working your insurance plan harder</a></li>
        <li><a href="#government-programs">Government programs: Medicare Extra Help, SPAP, insulin cap</a></li>
        <li><a href="#comparison-table">Strategy comparison table</a></li>
        <li><a href="#faq">Frequently asked questions</a></li>
        <li><a href="#sources">Sources</a></li>
    </ol>
</nav>

<h2 id="generic-vs-brand">1. Generic vs. brand-name drugs</h2>

<p>Generic drugs contain the same active ingredient, strength, dosage form, and route of administration as their brand-name counterparts. The FDA requires generics to be bioequivalent&mdash;meaning they are absorbed into the bloodstream at the same rate and to the same extent as the original. They are not inferior medications. The price difference is purely the result of economics: brand manufacturers recover research and development costs during their patent exclusivity period, after which any manufacturer can produce the generic.</p>

<p>Generics cost <strong>80 to 85% less</strong> than brand-name drugs on average, according to the FDA. The practical impact for patients is enormous:</p>

<table>
    <thead>
        <tr>
            <th>Drug (Condition)</th>
            <th>Brand Name</th>
            <th>Brand Cash Price/mo</th>
            <th>Generic Name</th>
            <th>Generic Cash Price/mo</th>
            <th>Savings</th>
        </tr>
    </thead>
    <tbody>
        <tr><td>Cholesterol</td><td>Lipitor</td><td>$250&ndash;$350</td><td>Atorvastatin</td><td>$5&ndash;$15</td><td>95%</td></tr>
        <tr><td>Blood pressure</td><td>Norvasc</td><td>$180&ndash;$280</td><td>Amlodipine</td><td>$4&ndash;$10</td><td>97%</td></tr>
        <tr><td>Diabetes (Type 2)</td><td>Glucophage</td><td>$120&ndash;$200</td><td>Metformin</td><td>$4&ndash;$12</td><td>94%</td></tr>
        <tr><td>Migraine (acute)</td><td>Imitrex</td><td>$300&ndash;$500</td><td>Sumatriptan</td><td>$15&ndash;$50</td><td>90%</td></tr>
        <tr><td>Antidepressant</td><td>Lexapro</td><td>$200&ndash;$300</td><td>Escitalopram</td><td>$8&ndash;$20</td><td>93%</td></tr>
        <tr><td>Thyroid</td><td>Synthroid</td><td>$50&ndash;$90</td><td>Levothyroxine</td><td>$8&ndash;$18</td><td>80%</td></tr>
    </tbody>
</table>

<p>Always ask your prescriber: &ldquo;Is there a generic available for this medication?&rdquo; and &ldquo;Would the generic work for my situation?&rdquo; For most chronic conditions, the generic works identically. The main exceptions are a small number of narrow therapeutic index drugs (certain thyroid medications, epilepsy drugs) where your doctor may prefer to keep you on a consistent formulation.</p>

<h2 id="discount-programs">2. GoodRx, Blink Health, and discount card programs</h2>

<p><strong>GoodRx</strong> is a free service that negotiates discounted rates with pharmacy benefit managers and passes those savings to users. You do not need insurance to use it&mdash;simply show the GoodRx coupon (app or printed) at the pharmacy counter. GoodRx is accepted at most major pharmacy chains and many independent pharmacies.</p>

<p>GoodRx works best for generic medications. For brand-name drugs, the discount is typically modest. Prices vary significantly by pharmacy, so always compare prices across nearby locations in the app before filling.</p>

<p><strong>When GoodRx may NOT be your best option:</strong></p>
<ul>
    <li>Your insurance copay is already lower than the GoodRx price (common for Tier 1 generics on good plans).</li>
    <li>You are close to your out-of-pocket maximum&mdash;using GoodRx means the spend doesn\u2019t count toward your OOP max.</li>
    <li>The drug qualifies for a manufacturer copay card that reduces your cost to $0 or near-zero.</li>
</ul>

<p><strong>Alternatives to GoodRx:</strong></p>

<table>
    <thead>
        <tr>
            <th>Program</th>
            <th>Best For</th>
            <th>Requires Membership?</th>
            <th>Website</th>
        </tr>
    </thead>
    <tbody>
        <tr><td>GoodRx</td><td>Generics at retail pharmacies</td><td>No (free)</td><td>goodrx.com</td></tr>
        <tr><td>RxSaver</td><td>Alternative prices to compare with GoodRx</td><td>No (free)</td><td>rxsaver.com</td></tr>
        <tr><td>Blink Health</td><td>Generics, pay online, pick up in store</td><td>No (free)</td><td>blinkhealth.com</td></tr>
        <tr><td>NeedyMeds</td><td>Finding assistance programs + discount cards</td><td>No (free)</td><td>needymeds.org</td></tr>
        <tr><td>Cost Plus Drugs</td><td>Long-term generic maintenance meds</td><td>No (free)</td><td>costplusdrugs.com</td></tr>
    </tbody>
</table>

<h2 id="cost-plus">3. Mark Cuban\u2019s Cost Plus Drugs and direct-to-consumer options</h2>

<p>Cost Plus Drugs, launched in 2022, operates on a radical transparency model: it charges the actual manufacturing cost of the drug plus a flat 15% markup plus a dispensing fee. For generic medications, this can be dramatically cheaper than any other option. The service requires a valid prescription from your doctor but does not require insurance.</p>

<p>Examples of Cost Plus Drugs pricing compared to retail:</p>

<ul>
    <li>Imatinib 400mg (generic Gleevec, leukemia): <strong>$19/month</strong> vs. $9,000+ retail</li>
    <li>Tamoxifen 20mg (breast cancer prevention): <strong>$5/month</strong> vs. $150+ retail</li>
    <li>Rosuvastatin 10mg (Crestor generic): <strong>$4/month</strong> vs. $40+ retail</li>
    <li>Metformin ER 1000mg (diabetes): <strong>$6/month</strong> vs. $25+ retail</li>
</ul>

<p>Cost Plus Drugs is a mail-order pharmacy, so it works best for maintenance medications you refill regularly. It does not carry every drug, and it does not carry brand-name medications. Check availability before transferring a prescription.</p>

{_embed(mode="cost", cpt="99213", title="Look up your prescription costs", subtitle="Compare drug prices across programs for your medication.")}

<h2 id="manufacturer-assistance">4. Manufacturer patient assistance programs</h2>

<p>Every major pharmaceutical manufacturer offers a patient assistance program (PAP) for brand-name drugs that provides free or heavily discounted medication to patients who cannot afford it. These programs are separate from and usually more generous than the copay cards marketed to commercially insured patients.</p>

<p>Major programs by manufacturer include:</p>

<ul>
    <li><strong>Pfizer RxPathways</strong> &mdash; covers Eliquis, Ibrance, Xeljanz, and others for eligible patients</li>
    <li><strong>Lilly Cares Foundation</strong> &mdash; covers Humalog, Trulicity, Jardiance, Taltz, and more; insulin at $35/month for eligible patients</li>
    <li><strong>Novo Nordisk Patient Assistance</strong> &mdash; covers Ozempic, Victoza, Tresiba, and other insulins</li>
    <li><strong>AstraZeneca AZ&amp;Me</strong> &mdash; covers Farxiga, Brilinta, and other AZ medications</li>
    <li><strong>Bristol Myers Squibb Patient Assistance Foundation</strong> &mdash; covers Eliquis (co-sponsored with Pfizer), Opdivo, and others</li>
</ul>

<p>Most programs require income at or below 200\u2013400% of the federal poverty level and U.S. residency. Applications are typically submitted by your doctor\u2019s office. <strong>NeedyMeds.org</strong> maintains a free, searchable database of over 4,000 assistance programs&mdash;search by drug name to find the specific program and eligibility criteria.</p>

<h2 id="supply-strategies">5. 90-day supply, pill splitting, and OTC switches</h2>

<p><strong>90-day supply:</strong> For any maintenance medication (taken daily for a chronic condition), switching from a 30-day supply to a 90-day mail-order fill typically reduces cost per dose by 20 to 33%. Most health plans encourage this through lower copays on mail-order 90-day fills. Ask your doctor to write prescriptions for 90-day supplies with refills for all chronic medications.</p>

<p><strong>Pill splitting:</strong> For medications where double-strength tablets cost approximately the same as single-strength, your doctor may prescribe double-strength tablets and instruct you to split them with an inexpensive pill splitter. This effectively doubles your supply at the same cost. This works for certain blood pressure medications, statins, and antidepressants where the tablet is scored and splittable. <em>Never split capsules, extended-release tablets, or enteric-coated tablets without your doctor\u2019s explicit guidance.</em></p>

<p><strong>Over-the-counter switches:</strong> Several drugs that previously required a prescription are now available over-the-counter (OTC) at a lower cost than the prescription version:</p>

<ul>
    <li><strong>Cetirizine (Zyrtec)</strong>: OTC generic ~$10/month vs. prescription allergy medications</li>
    <li><strong>Loratadine (Claritin)</strong>: OTC generic ~$5/month</li>
    <li><strong>Fluticasone nasal spray (Flonase)</strong>: OTC ~$15/month vs. prescription alternatives</li>
    <li><strong>Omeprazole (Prilosec)</strong>: OTC generic ~$8/month vs. prescription Nexium or Dexilant</li>
    <li><strong>Miconazole, clotrimazole</strong>: OTC antifungals vs. prescription alternatives</li>
</ul>

<p>In some cases, your insurance will not cover the OTC version even if a prescription form exists, so the OTC version may be cheaper out of pocket. Confirm with your pharmacist.</p>

<h2 id="insurance-strategies">6. Working your insurance plan harder</h2>

<p>Most patients accept the tier their drug is placed on without realizing they have options to lower cost-sharing through their insurance plan itself.</p>

<ol>
    <li><strong>Request a formulary exception.</strong> If your drug is on Tier 3 or Tier 4, you or your doctor can request a formulary exception to have it covered at a lower tier, citing medical necessity. This works when you have tried lower-tier alternatives and they were ineffective or caused adverse effects.</li>
    <li><strong>Request a tier exception.</strong> A tier exception asks the plan to apply a lower tier\u2019s cost-sharing to your specific drug without changing its formulary placement. Most plans allow one exception per plan year with physician documentation.</li>
    <li><strong>Ask your doctor for samples.</strong> Physician offices receive free samples of brand-name medications from pharmaceutical representatives. A 2\u20134 week sample supply can bridge the gap while you apply for assistance or await a prior authorization decision.</li>
    <li><strong>Appeal a prior authorization denial.</strong> If your insurer denied a prior auth for a medication your doctor prescribed, you can appeal with clinical documentation. An urgent/expedited appeal must receive a decision within 72 hours. See our guide on <a href="/guides/insurance-denial-appeal">appealing insurance denials</a>.</li>
    <li><strong>Use manufacturer copay cards for commercially insured patients.</strong> For expensive brand-name drugs (CGRP migraine drugs, GLP-1s, biologics), manufacturers offer copay assistance cards that reduce your out-of-pocket to $0\u201335/month for commercially insured patients. These are not available to Medicare or Medicaid beneficiaries.</li>
</ol>

<h2 id="government-programs">7. Government programs: Medicare Extra Help, SPAP, insulin cap</h2>

<p><strong>Medicare Extra Help (Low Income Subsidy):</strong> Medicare beneficiaries with limited income and assets may qualify for the Extra Help program, which significantly reduces Part D premiums, deductibles, and copays. In 2026, eligible beneficiaries pay $0 to $11 per prescription. An estimated 3 million Medicare beneficiaries who qualify for Extra Help have not enrolled. Apply through SSA.gov or your State Health Insurance Assistance Program (SHIP).</p>

<p><strong>State Pharmaceutical Assistance Programs (SPAPs):</strong> Many states operate their own drug assistance programs for residents who fall into the gap between Medicaid and full Medicare coverage. Eligibility and benefits vary by state. The Medicare Rights Center maintains a directory of SPAP programs at medicarerights.org.</p>

<p><strong>$35/month insulin cap:</strong> The Inflation Reduction Act capped Medicare Part D insulin cost-sharing at $35 per month per insulin. Most ACA-compliant commercial plans apply a similar cap. If you are paying more than $35/month for insulin through an insured plan, contact your insurer immediately&mdash;this is likely a billing or adjudication error that they are required to correct.</p>

<p><strong>Medicaid and CHIP:</strong> If your income is at or below 138% of the federal poverty level, you likely qualify for Medicaid, which covers most medications at minimal or no cost. Use <a href="https://www.healthcare.gov" target="_blank" rel="noopener">healthcare.gov</a> to check eligibility.</p>

<div class="key-takeaway">
    <strong>29% of Americans report not filling a prescription due to cost</strong>&mdash;most without knowing about Cost Plus Drugs, patient assistance programs, or discount cards that could bring their cost to near zero. <a href="/fight-debt">Let BillKarma help you find savings</a> on your current medications.
</div>

<h2 id="comparison-table">8. Strategy comparison table</h2>

<table>
    <thead>
        <tr>
            <th>Strategy</th>
            <th>Works Best For</th>
            <th>Insurance Required?</th>
            <th>Typical Savings</th>
            <th>Counts Toward Deductible?</th>
        </tr>
    </thead>
    <tbody>
        <tr><td>Generic substitution</td><td>Any drug with a generic available</td><td>No</td><td>80&ndash;95%</td><td>If using insurance</td></tr>
        <tr><td>GoodRx / discount card</td><td>Generics at retail pharmacy</td><td>No</td><td>30&ndash;80%</td><td>No</td></tr>
        <tr><td>Cost Plus Drugs</td><td>Generic maintenance meds</td><td>No</td><td>50&ndash;99%</td><td>No</td></tr>
        <tr><td>Manufacturer PAP</td><td>Brand drugs, uninsured/underinsured</td><td>No</td><td>100% (free)</td><td>No</td></tr>
        <tr><td>Manufacturer copay card</td><td>Brand drugs, commercially insured</td><td>Yes (commercial only)</td><td>90&ndash;100%</td><td>Varies by plan</td></tr>
        <tr><td>90-day mail-order supply</td><td>Chronic maintenance meds</td><td>Yes (usually)</td><td>20&ndash;33%</td><td>Yes</td></tr>
        <tr><td>Pill splitting</td><td>Selected medications only</td><td>No</td><td>50%</td><td>If using insurance</td></tr>
        <tr><td>OTC switch</td><td>Allergy, GI, antifungal</td><td>No</td><td>40&ndash;80%</td><td>Only with HSA/FSA</td></tr>
        <tr><td>Medicare Extra Help</td><td>Low-income Medicare beneficiaries</td><td>Medicare only</td><td>Up to 95%</td><td>Yes</td></tr>
        <tr><td>SPAP</td><td>State residents in income gap</td><td>Varies by state</td><td>50&ndash;100%</td><td>Varies</td></tr>
    </tbody>
</table>

<h2 id="faq">Frequently asked questions</h2>

<div class="faq-section">
    <div class="faq-item">
        <h3>Is GoodRx always cheaper than my insurance copay?</h3>
        <p>Not always. GoodRx is frequently cheaper than your insurance copay for generic medications, especially at large pharmacy chains like Walmart, Costco, and Kroger. But if you have a low-tier copay (e.g., $5\u201310 for a Tier 1 generic) or you\u2019re close to your out-of-pocket maximum, using your insurance may be cheaper. Always compare both prices at the pharmacy counter before deciding. One important note: using GoodRx instead of insurance means the payment does not count toward your deductible or out-of-pocket maximum.</p>
    </div>
    <div class="faq-item">
        <h3>What is Cost Plus Drugs and how does it work?</h3>
        <p>Cost Plus Drugs (costplusdrugs.com), founded by Mark Cuban, sells generic medications at manufacturing cost plus a 15% markup plus a small pharmacy dispensing fee. For many common generics, this results in prices dramatically lower than retail pharmacy prices. For example, imatinib (generic Gleevec for leukemia) costs under $20 per month on Cost Plus Drugs vs. thousands at retail. It requires a valid prescription but no insurance. It works best for generic medications you take long-term.</p>
    </div>
    <div class="faq-item">
        <h3>How do I find manufacturer patient assistance programs?</h3>
        <p>Most major pharmaceutical manufacturers offer patient assistance programs (PAPs) for low-income patients who are uninsured or underinsured. To find them, go directly to the manufacturer\u2019s website and search for &ldquo;patient assistance&rdquo; or visit NeedyMeds.org, which maintains a free database of over 4,000 programs. Requirements typically include income at or below 200\u2013400% of the federal poverty level, U.S. residency, and no coverage for the specific drug. The application is usually handled by your doctor\u2019s office.</p>
    </div>
    <div class="faq-item">
        <h3>What is the $35/month insulin cap?</h3>
        <p>The Inflation Reduction Act (2022) capped Medicare Part D insulin cost-sharing at $35 per month per insulin product. The Affordable Care Act extended similar caps to most commercial health plans. As of 2026, most insured patients should not pay more than $35 per month for insulin through their health plan. If you are being charged more than $35, contact your insurer&mdash;this is likely a billing error. Uninsured patients do not benefit from the cap but can access $25 over-the-counter ReliOn insulin at Walmart.</p>
    </div>
    <div class="faq-item">
        <h3>When should I ask my doctor for a 90-day supply?</h3>
        <p>For any chronic maintenance medication you take daily, a 90-day supply typically costs 20\u201333% less per dose than three 30-day fills, especially through mail-order pharmacy. Most plans allow 90-day fills for maintenance medications (blood pressure, cholesterol, diabetes, thyroid, antidepressants) after the first 30-day fill. Ask your doctor to write the prescription for a 90-day supply with refills, and contact your insurance\u2019s mail-order pharmacy. This can save $100\u2013$600 per year for patients on multiple chronic medications.</p>
    </div>
</div>

<h2 id="sources">Sources</h2>

<ul class="sources-list">
    <li><a href="https://www.fda.gov/drugs/generic-drugs/generic-drug-facts" target="_blank" rel="noopener">FDA: Generic Drug Facts &mdash; Bioequivalence and Safety</a></li>
    <li><a href="https://www.kff.org/health-costs/issue-brief/cost-related-nonadherence-to-medications/" target="_blank" rel="noopener">KFF: Cost-Related Medication Nonadherence in the United States</a></li>
    <li><a href="https://www.cms.gov/medicare/part-d/costs/low-income-subsidy" target="_blank" rel="noopener">CMS: Medicare Extra Help (Low Income Subsidy) Program</a></li>
    <li><a href="https://costplusdrugs.com" target="_blank" rel="noopener">Mark Cuban Cost Plus Drug Company &mdash; Pricing Methodology</a></li>
    <li><a href="https://www.needymeds.org" target="_blank" rel="noopener">NeedyMeds: Patient Assistance Program Database</a></li>
    <li><a href="https://www.congress.gov/bill/117th-congress/house-bill/5376" target="_blank" rel="noopener">Inflation Reduction Act of 2022 &mdash; Medicare Drug Price Negotiation and Insulin Cap</a></li>
    <li><a href="https://www.healthaffairs.org/doi/10.1377/hlthaff.2023.00589" target="_blank" rel="noopener">Health Affairs: Impact of Cost Plus Drugs on Prescription Drug Affordability</a></li>
</ul>
""",
})
