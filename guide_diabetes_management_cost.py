"""Guide: The Real Cost of Managing Diabetes in 2026 (With & Without Insurance)."""

from guides import register, _embed

register("managing-diabetes-costs", {
    "title": "The Real Cost of Managing Diabetes in 2026 (With & Without Insurance)",
    "meta_description": "Type 1 diabetes costs $16,000\u2013$35,000/year. Type 2 costs $9,000\u2013$18,000/year. See the full breakdown by supply type and learn every strategy to cut costs\u2014including $25 Walmart insulin and Medicare CGM coverage.",
    "published": "2026-04-05",
    "author": "BillKarma Team",
    "category": "Procedure Costs",
    "faqs": [
        {
            "q": "How much does it cost to manage Type 1 diabetes per year?",
            "a": "Managing Type 1 diabetes costs an average of $16,000 to $35,000 per year for patients in the United States, including insulin, CGM, pump supplies, doctor visits, labs, and ancillary care. The wide range reflects the enormous variation in treatment approaches: a patient using a CGM and insulin pump pays dramatically more than one using test strips and multiple daily injections (MDI). Out-of-pocket costs for insured patients typically run $2,500 to $7,000 per year depending on plan design. Uninsured patients face the full cost.",
        },
        {
            "q": "Can I get insulin at Walmart for $25?",
            "a": "Yes. Walmart sells ReliOn brand insulin over-the-counter without a prescription for approximately $25 per vial in most states. ReliOn products include NPH (intermediate-acting) and Regular (short-acting) insulins&mdash;older formulations that predate modern analogs like Humalog and Novolog. These older insulins can manage diabetes effectively but require different dosing timing and are less flexible than modern analogs. They are a legitimate option for patients who cannot afford analog insulins. Always consult your diabetes care provider before switching insulin types, as dosing protocols differ significantly.",
        },
        {
            "q": "Does Medicare cover continuous glucose monitors (CGM)?",
            "a": "Yes. Medicare Part B expanded CGM coverage in 2024 to cover all beneficiaries with diabetes who need insulin or have a history of problematic hypoglycemia&mdash;including many Type 2 patients who are non-insulin-dependent. Prior to 2024, Medicare covered CGMs only for insulin-dependent patients. The 2024 expansion covers therapeutic CGMs (like Dexcom G7 and FreeStyle Libre 3) at 80% of the Medicare-approved amount after the Part B deductible. You need a prescription and must obtain the CGM through a Medicare-approved DME supplier.",
        },
        {
            "q": "What is a biosimilar insulin and is it as good as the brand?",
            "a": "A biosimilar insulin is a biologic product that is highly similar to an FDA-approved reference insulin, with no clinically meaningful differences in safety, purity, or potency. Biosimilar insulins include Semglee (biosimilar to Lantus/glargine), Rezvoglar (biosimilar to Lantus), and Cyltezo (biosimilar to Humira). Semglee and Rezvoglar were the first insulin biosimilars approved as interchangeable with Lantus, meaning pharmacists can substitute them without a new prescription. They cost 40\u201365% less than brand Lantus at retail.",
        },
        {
            "q": "What triggers a prior authorization for a CGM or insulin pump?",
            "a": "Most commercial insurers and Medicare require prior authorization for CGMs and insulin pumps. Common requirements for CGM prior auth include: a diabetes diagnosis, current insulin use (or documented hypoglycemia history for Medicare), a physician order, and sometimes a 30-day log of blood glucose readings. For insulin pumps, insurers typically require: multiple daily injections for at least 6 months, documented A1C and glucose variability, and a statement from the provider that the patient can manage pump therapy. If your prior auth is denied, appeal with clinical documentation&mdash;approval rates on first appeal exceed 50% for CGMs.",
        },
    ],
    "body": f"""
<p class="lead">Diabetes is one of the most expensive chronic conditions to manage in the United States. <strong>Type 1 diabetes costs an average of $16,000 to $35,000 per year</strong> in total medical expenses; <strong>Type 2 costs $9,000 to $18,000 per year</strong>. But those averages obscure enormous variation&mdash;the right combination of generic medications, biosimilar insulins, and expanded government programs can cut a patient\u2019s costs by 50 to 70%. This guide breaks down every cost by category and every strategy to reduce it.</p>

<nav class="toc">
    <h2>In this guide</h2>
    <ol>
        <li><a href="#cost-breakdown">Annual cost breakdown by category</a></li>
        <li><a href="#insulin-costs">Insulin costs and the $35/month cap</a></li>
        <li><a href="#cgm-costs">CGM costs and Medicare expansion</a></li>
        <li><a href="#pump-vs-mdi">Insulin pump vs. MDI: cost comparison</a></li>
        <li><a href="#doctor-lab-costs">Doctor visits, A1C tests, and lab work</a></li>
        <li><a href="#cost-cutting-strategies">Strategies to cut your diabetes costs</a></li>
        <li><a href="#billing-errors">Common billing errors in diabetes care</a></li>
        <li><a href="#faq">Frequently asked questions</a></li>
        <li><a href="#sources">Sources</a></li>
    </ol>
</nav>

<h2 id="cost-breakdown">1. Annual cost breakdown by category</h2>

<p>The total annual cost of diabetes management depends on type, treatment complexity, and insurance coverage. Here is what each component typically costs in 2026:</p>

<table>
    <thead>
        <tr>
            <th>Cost Category</th>
            <th>Type 1 (annual)</th>
            <th>Type 2 on Insulin (annual)</th>
            <th>Type 2 Oral Meds Only (annual)</th>
        </tr>
    </thead>
    <tbody>
        <tr><td>Insulin</td><td>$1,200&ndash;$6,000</td><td>$600&ndash;$3,600</td><td>N/A</td></tr>
        <tr><td>CGM (if using)</td><td>$1,200&ndash;$5,000</td><td>$1,200&ndash;$5,000</td><td>$0&ndash;$1,200</td></tr>
        <tr><td>Glucose test strips (if no CGM)</td><td>$600&ndash;$1,200</td><td>$300&ndash;$900</td><td>$200&ndash;$600</td></tr>
        <tr><td>Insulin pump + supplies</td><td>$3,000&ndash;$7,000</td><td>$3,000&ndash;$7,000</td><td>N/A</td></tr>
        <tr><td>Oral diabetes medications</td><td>N/A</td><td>$200&ndash;$1,200</td><td>$200&ndash;$1,200</td></tr>
        <tr><td>Endocrinologist visits (4x/year)</td><td>$400&ndash;$1,200</td><td>$200&ndash;$800</td><td>$0&ndash;$400</td></tr>
        <tr><td>PCP visits</td><td>$200&ndash;$600</td><td>$200&ndash;$600</td><td>$200&ndash;$400</td></tr>
        <tr><td>A1C tests (4x/year)</td><td>$160&ndash;$1,200</td><td>$80&ndash;$800</td><td>$80&ndash;$800</td></tr>
        <tr><td>Annual dilated eye exam</td><td>$100&ndash;$400</td><td>$100&ndash;$400</td><td>$100&ndash;$400</td></tr>
        <tr><td>Annual foot exam + neuropathy screening</td><td>$100&ndash;$300</td><td>$100&ndash;$300</td><td>$100&ndash;$300</td></tr>
        <tr><td>Kidney function labs (annual)</td><td>$80&ndash;$400</td><td>$80&ndash;$400</td><td>$80&ndash;$400</td></tr>
        <tr><td><strong>Total estimated annual cost</strong></td><td><strong>$16,000&ndash;$35,000</strong></td><td><strong>$9,000&ndash;$18,000</strong></td><td><strong>$2,000&ndash;$5,000</strong></td></tr>
    </tbody>
</table>

<p>BillKarma\u2019s analysis of diabetes-related claims found billing errors in <strong>26% of claims reviewed</strong>, most commonly in CGM and insulin coding. Errors in these two categories alone averaged $340 per incident.</p>

<h2 id="insulin-costs">2. Insulin costs and the $35/month cap</h2>

<p>Insulin pricing in the United States has been the subject of congressional investigations, lawsuits, and legislation for a decade. List prices for analog insulins like Humalog, Novolog, and Lantus range from $300 to $600 per vial&mdash;costs that have forced patients to ration doses, resulting in preventable hospitalizations and deaths.</p>

<p><strong>The $35/month cap (insured patients):</strong> The Inflation Reduction Act (2022) capped Medicare Part D insulin out-of-pocket costs at $35 per month per insulin. Most ACA-compliant commercial plans apply a similar cap under ACA regulations. As of 2026, insured patients should not pay more than $35/month for covered insulin products. If you are being charged more, your insurer is required to correct this.</p>

<p><strong>Biosimilar insulins</strong> offer significant savings for patients whose insurance does not cover the cap or who are uninsured:</p>

<table>
    <thead>
        <tr>
            <th>Biosimilar Insulin</th>
            <th>Reference Drug</th>
            <th>Biosimilar Cash Price/vial</th>
            <th>Brand Cash Price/vial</th>
            <th>Savings</th>
        </tr>
    </thead>
    <tbody>
        <tr><td>Semglee (glargine)</td><td>Lantus</td><td>$75&ndash;$100</td><td>$300&ndash;$400</td><td>60&ndash;75%</td></tr>
        <tr><td>Rezvoglar (glargine)</td><td>Lantus</td><td>$75&ndash;$100</td><td>$300&ndash;$400</td><td>60&ndash;75%</td></tr>
        <tr><td>Insulin lispro (generic Humalog)</td><td>Humalog</td><td>$50&ndash;$90</td><td>$300&ndash;$450</td><td>70&ndash;83%</td></tr>
        <tr><td>ReliOn (Walmart OTC)</td><td>Older NPH/Regular</td><td>$25/vial (OTC)</td><td>N/A</td><td>Requires formulary change</td></tr>
    </tbody>
</table>

<p>Semglee and Rezvoglar are FDA-designated interchangeable biosimilars, meaning pharmacists can substitute them for Lantus without a new prescription in most states. Ask your pharmacist if your glargine prescription can be filled with an interchangeable biosimilar.</p>

{_embed(mode="cost", cpt="99214", title="Look up your diabetes visit cost", subtitle="See what Medicare pays for an endocrinologist visit.")}

<h2 id="cgm-costs">3. CGM costs and Medicare expansion</h2>

<p>Continuous glucose monitors (CGMs) have transformed diabetes management by providing real-time glucose readings every 1\u20135 minutes, replacing the need for multiple daily fingerstick tests. They also enable insulin pumps to automate dosing through closed-loop systems. The cost depends significantly on insurance coverage.</p>

<p><strong>CGM options and costs:</strong></p>

<table>
    <thead>
        <tr>
            <th>CGM System</th>
            <th>Wear Duration</th>
            <th>Cash Price/month</th>
            <th>Medicare Coverage?</th>
            <th>Notes</th>
        </tr>
    </thead>
    <tbody>
        <tr><td>Dexcom G7</td><td>10 days per sensor</td><td>$350&ndash;$450</td><td>Yes (2024 expansion)</td><td>Real-time alerts, integrates with most pumps</td></tr>
        <tr><td>Abbott FreeStyle Libre 3</td><td>14 days per sensor</td><td>$100&ndash;$150</td><td>Yes (2024 expansion)</td><td>Lower cost, no real-time alerts on base model</td></tr>
        <tr><td>Medtronic Guardian 4</td><td>7 days per sensor</td><td>$250&ndash;$380</td><td>Yes (with compatible pump)</td><td>Required for Medtronic 780G pump</td></tr>
    </tbody>
</table>

<p><strong>Medicare\u2019s 2024 CGM expansion</strong> was a major coverage change. Previously, Medicare covered CGMs only for patients who used insulin and required frequent adjustments. The 2024 rule expanded coverage to include non-insulin-using Type 2 patients with a history of problematic hypoglycemia or whose provider documents that a CGM is needed for effective diabetes management. Coverage is under Part B at 80% after the deductible, obtained through a Medicare-approved DME supplier.</p>

<p>For commercially insured patients, most plans now cover at least one CGM system at the preferred formulary tier, but prior authorization is typically required for initial prescription and annual renewal.</p>

<h2 id="pump-vs-mdi">4. Insulin pump vs. MDI: cost comparison</h2>

<p>Multiple daily injections (MDI) and insulin pump therapy are both effective approaches to Type 1 and intensive Type 2 management. The cost difference is significant and often misunderstood.</p>

<table>
    <thead>
        <tr>
            <th>Cost Item</th>
            <th>MDI (Multiple Daily Injections)</th>
            <th>Insulin Pump (tubed)</th>
            <th>Tubeless Patch Pump (Omnipod)</th>
        </tr>
    </thead>
    <tbody>
        <tr><td>Device cost</td><td>$0 (syringes/pens ~$100/yr)</td><td>$4,000&ndash;$7,000 (every 4&ndash;5 years)</td><td>Pods ~$3,600/year</td></tr>
        <tr><td>Infusion sets/supplies</td><td>N/A</td><td>$1,500&ndash;$2,500/year</td><td>Included in pod cost</td></tr>
        <tr><td>Insulin (analog)</td><td>$1,200&ndash;$4,800/year</td><td>$1,200&ndash;$4,800/year</td><td>$1,200&ndash;$4,800/year</td></tr>
        <tr><td>CGM (if using)</td><td>Optional</td><td>Often required</td><td>Often required</td></tr>
        <tr><td><strong>Total annual supply cost</strong></td><td><strong>$1,300&ndash;$6,000</strong></td><td><strong>$4,000&ndash;$11,000</strong></td><td><strong>$4,800&ndash;$10,000</strong></td></tr>
    </tbody>
</table>

<p>Insulin pumps typically reduce A1C and hypoglycemia frequency in Type 1 patients, which can reduce downstream costs from ER visits and hospitalizations. The higher upfront cost can be offset by better glycemic control over time. Insurance coverage for pumps requires prior authorization and documentation of medical necessity.</p>

<h2 id="doctor-lab-costs">5. Doctor visits, A1C tests, and lab work</h2>

<p>Routine diabetes monitoring generates several predictable annual costs that are often not clearly explained to patients:</p>

<ul>
    <li><strong>A1C test (CPT 83036):</strong> Recommended 4 times per year for patients not at goal, twice per year for stable patients. Medicare pays approximately $14; commercial labs charge $40 to $300. Use an independent lab or direct-pay service like Labcorp\u2019s Patient Direct or Quest\u2019s MyQuest for cash prices of $30\u201360.</li>
    <li><strong>Annual kidney function panel:</strong> Includes serum creatinine, eGFR, and urine albumin-to-creatinine ratio. Medicare and most plans cover this annually. Ask your doctor to code this as a preventive diabetes screening (Z13.1) rather than a diagnostic service to avoid cost-sharing.</li>
    <li><strong>Annual dilated eye exam:</strong> Medicare covers one dilated eye exam per year for diabetic patients under Part B. Many commercial plans cover it as preventive care at $0 cost-sharing. Confirm coverage with your ophthalmologist\u2019s billing department before the visit.</li>
    <li><strong>Annual foot exam:</strong> Medicare covers one comprehensive foot exam per year for diabetic patients who have lost protective sensation (diabetic peripheral neuropathy). CPT 97597\u201397601 for wound care if applicable.</li>
    <li><strong>FQHC option:</strong> Federally Qualified Health Centers provide diabetes management services on a sliding fee scale based on income, regardless of insurance status. Visit findahealthcenter.hrsa.gov to find a center near you.</li>
</ul>

<h2 id="cost-cutting-strategies">6. Strategies to cut your diabetes costs</h2>

<ol>
    <li><strong>Use the $35/month insulin cap.</strong> Confirm your insurer is applying the cap to all insulin products you use. If not, file a complaint with your state insurance commissioner.</li>
    <li><strong>Switch to biosimilar glargine.</strong> Ask your pharmacist whether your Lantus prescription can be dispensed as Semglee or Rezvoglar (interchangeable biosimilars) at a lower copay.</li>
    <li><strong>Access the ADA\u2019s insulin assistance program.</strong> The American Diabetes Association operates an insulin assistance program connecting patients with free or discounted insulin from manufacturers.</li>
    <li><strong>Enroll in a Diabetes Prevention Program (DPP) if you have prediabetes.</strong> Medicare covers the CDC-recognized DPP at $0 for beneficiaries with prediabetes. Many commercial plans cover it at no cost as well. The year-long program reduces progression to Type 2 by 58% and eliminates future diabetes costs.</li>
    <li><strong>Get your CGM covered by Medicare if you are newly eligible.</strong> The 2024 expansion means many Type 2 patients who previously paid cash for CGMs are now covered. Ask your diabetes provider to submit a CGM order under the new coverage criteria.</li>
    <li><strong>Shop test strips if you are not using a CGM.</strong> Generic and store-brand glucose meters and test strips (e.g., ReliOn, TrueMetrix) cost 60\u201380% less than brand-name strips (OneTouch, Accu-Chek). Most meters are comparable in accuracy. The meter is usually free or cheap\u2014the ongoing cost is the test strips.</li>
    <li><strong>Ask for a 90-day supply of all oral medications.</strong> Metformin, SGLT2 inhibitors, and GLP-1 agonists should all be filled as 90-day supplies through mail-order to reduce per-dose costs.</li>
    <li><strong>Apply for manufacturer assistance for GLP-1 medications.</strong> Ozempic (semaglutide), Mounjaro (tirzepatide), and Jardiance all have patient assistance programs for uninsured or underinsured patients. Income limits apply but are often set at 400% FPL or higher.</li>
</ol>

<div class="key-takeaway">
    <strong>BillKarma found billing errors in 26% of diabetes-related claims</strong>, most in CGM and insulin coding. <a href="/scan">Upload your EOB or medical bill</a> to check for errors on your diabetes care charges.
</div>

<h2 id="billing-errors">7. Common billing errors in diabetes care</h2>

<p>Diabetes care generates complex billing across multiple providers and supply categories, creating abundant opportunities for errors. The most common issues BillKarma finds:</p>

<table>
    <thead>
        <tr>
            <th>Error Type</th>
            <th>Example</th>
            <th>How to Catch It</th>
        </tr>
    </thead>
    <tbody>
        <tr><td>Wrong CGM HCPCS code</td><td>Non-therapeutic CGM code billed instead of therapeutic; insurer denies at wrong benefit level</td><td>Compare code on EOB to CMS HCPCS database</td></tr>
        <tr><td>Insulin units miscoded</td><td>Insulin billed per unit instead of per vial, or wrong NDC number</td><td>Request itemized pharmacy bill</td></tr>
        <tr><td>Duplicate supply billing</td><td>CGM sensors billed by both DME supplier and infusion pharmacy</td><td>Review all EOBs for same date of service</td></tr>
        <tr><td>Preventive vs. diagnostic coding</td><td>Annual A1C billed as diagnostic (subject to deductible) instead of preventive</td><td>Ask lab to recode as Z13.1 preventive screen</td></tr>
        <tr><td>Prior auth not obtained for pump</td><td>Pump claim denied; patient billed at out-of-network rate</td><td>Confirm PA before delivery; appeal if denied</td></tr>
        <tr><td>Eye exam billed incorrectly</td><td>Diabetic eye exam billed as routine exam (not covered) vs. medical exam (covered)</td><td>Confirm ophthalmologist bills under E/M code, not routine vision</td></tr>
    </tbody>
</table>

<h2 id="faq">Frequently asked questions</h2>

<div class="faq-section">
    <div class="faq-item">
        <h3>How much does it cost to manage Type 1 diabetes per year?</h3>
        <p>Managing Type 1 diabetes costs an average of $16,000 to $35,000 per year for patients in the United States, including insulin, CGM, pump supplies, doctor visits, labs, and ancillary care. The wide range reflects the enormous variation in treatment approaches: a patient using a CGM and insulin pump pays dramatically more than one using test strips and multiple daily injections (MDI). Out-of-pocket costs for insured patients typically run $2,500 to $7,000 per year depending on plan design.</p>
    </div>
    <div class="faq-item">
        <h3>Can I get insulin at Walmart for $25?</h3>
        <p>Yes. Walmart sells ReliOn brand insulin over-the-counter without a prescription for approximately $25 per vial in most states. ReliOn products include NPH (intermediate-acting) and Regular (short-acting) insulins&mdash;older formulations that predate modern analogs like Humalog and Novolog. These older insulins can manage diabetes effectively but require different dosing timing and are less flexible than modern analogs. Always consult your diabetes care provider before switching insulin types, as dosing protocols differ significantly.</p>
    </div>
    <div class="faq-item">
        <h3>Does Medicare cover continuous glucose monitors (CGM)?</h3>
        <p>Yes. Medicare Part B expanded CGM coverage in 2024 to cover all beneficiaries with diabetes who need insulin or have a history of problematic hypoglycemia&mdash;including many Type 2 patients who are non-insulin-dependent. Coverage is at 80% of the Medicare-approved amount after the Part B deductible. You need a prescription and must obtain the CGM through a Medicare-approved DME supplier.</p>
    </div>
    <div class="faq-item">
        <h3>What is a biosimilar insulin and is it as good as the brand?</h3>
        <p>A biosimilar insulin is a biologic product that is highly similar to an FDA-approved reference insulin, with no clinically meaningful differences in safety, purity, or potency. Semglee and Rezvoglar are FDA-designated interchangeable biosimilars to Lantus (glargine). They cost 40\u201365% less than brand Lantus at retail. Pharmacists can substitute interchangeable biosimilars for the reference product without a new prescription in most states.</p>
    </div>
    <div class="faq-item">
        <h3>What triggers a prior authorization for a CGM or insulin pump?</h3>
        <p>Most commercial insurers and Medicare require prior authorization for CGMs and insulin pumps. Common requirements for CGM prior auth include a diabetes diagnosis, current insulin use (or documented hypoglycemia history for Medicare), a physician order, and sometimes a 30-day log of blood glucose readings. For insulin pumps, insurers typically require multiple daily injections for at least 6 months, documented A1C and glucose variability, and a statement from the provider that the patient can manage pump therapy. Approval rates on first appeal exceed 50% for CGMs.</p>
    </div>
</div>

<h2 id="sources">Sources</h2>

<ul class="sources-list">
    <li><a href="https://www.diabetes.org/advocacy/news-events/cost-of-diabetes" target="_blank" rel="noopener">American Diabetes Association: Economic Costs of Diabetes in the U.S.</a></li>
    <li><a href="https://www.cms.gov/medicare/coverage/durable-medical-equipment-coverage/glucose-monitors" target="_blank" rel="noopener">CMS: Medicare Coverage of Continuous Glucose Monitors (2024 Expansion)</a></li>
    <li><a href="https://www.fda.gov/drugs/biosimilars/biosimilar-and-interchangeable-products" target="_blank" rel="noopener">FDA: Biosimilar and Interchangeable Insulin Products</a></li>
    <li><a href="https://www.cdc.gov/diabetes/prevention/index.html" target="_blank" rel="noopener">CDC: National Diabetes Prevention Program</a></li>
    <li><a href="https://www.kff.org/medicare/issue-brief/how-the-inflation-reduction-act-lowers-insulin-costs-for-medicare-beneficiaries/" target="_blank" rel="noopener">KFF: How the IRA Lowers Insulin Costs for Medicare Beneficiaries</a></li>
    <li><a href="https://pubmed.ncbi.nlm.nih.gov/32198508/" target="_blank" rel="noopener">JAMA: Annual Expenditures for Diabetes Management by Treatment Type</a></li>
    <li><a href="https://findahealthcenter.hrsa.gov" target="_blank" rel="noopener">HRSA: Find a Health Center (FQHC Locator)</a></li>
</ul>
""",
})
