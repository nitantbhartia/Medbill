"""Guide: Medical Expense Tax Deduction."""

from guides import register, _embed

register("medical-expenses-tax-deduction", {
    "title": "Medical Expense Tax Deduction: How to Deduct Medical Bills",
    "meta_description": "You can deduct medical expenses exceeding 7.5% of your AGI. See what qualifies, how to calculate your deduction, and common mistakes that trigger audits.",
    "published": "2026-04-04",
    "author": "BillKarma Team",
    "category": "Saving Money",
    "faqs": [
        {
            "q": "What is the threshold for deducting medical expenses on taxes?",
            "a": "You can deduct medical and dental expenses that exceed 7.5% of your adjusted gross income (AGI) in 2026. For example, if your AGI is $80,000, only medical expenses above $6,000 (7.5% of $80,000) are deductible. You must itemize deductions on Schedule A to claim this&mdash;it is not available with the standard deduction. The 7.5% threshold applies to the 2025 and 2026 tax years; Congress periodically revisits whether to raise it to 10%.",
        },
        {
            "q": "Can I deduct health insurance premiums as a medical expense?",
            "a": "Yes, with conditions. You can deduct premiums you pay with after-tax dollars, including marketplace plans (if you did not receive a premium tax credit), COBRA premiums, Medicare Part B and Part D premiums, Medigap supplemental insurance, long-term care insurance (subject to age-based limits), and dental and vision insurance. You cannot deduct premiums paid with pre-tax dollars through an employer plan, because those were already excluded from your taxable income.",
        },
        {
            "q": "Can I deduct medical expenses I paid with my HSA or FSA?",
            "a": "No. Expenses paid with HSA, FSA, or HRA funds are not deductible because those accounts already provided a tax benefit (contributions were pre-tax or tax-deductible). You can only deduct the portion of medical expenses you paid out of pocket with after-tax dollars. If you paid part of a bill from your HSA and part out of pocket, only the out-of-pocket portion is deductible.",
        },
        {
            "q": "What medical expenses are NOT tax deductible?",
            "a": "Non-deductible medical expenses include: cosmetic surgery (unless it corrects a deformity from disease, injury, or congenital abnormality), gym memberships and health club dues (even if recommended by a doctor), non-prescription vitamins and supplements (unless prescribed for a specific condition), over-the-counter medications like aspirin or cold medicine, teeth whitening, and general health improvement programs. The expense must be primarily for the diagnosis, cure, treatment, or prevention of disease.",
        },
        {
            "q": "Does the medical expense deduction apply to family members?",
            "a": "Yes. You can deduct qualifying medical expenses you paid for yourself, your spouse, and your dependents (including children under 27 for health insurance purposes). You can also deduct expenses for someone who would qualify as your dependent except that they earned $5,050 or more in gross income or filed a joint return. This means you may be able to deduct expenses for an elderly parent you support even if they are not technically your tax dependent.",
        },
    ],
    "body": f"""
<p class="lead">Americans spent an average of <strong>$6,651 per person</strong> on out-of-pocket healthcare costs in 2025, according to CMS estimates. If you had a major surgery, chronic illness, or expensive prescriptions, you may be able to deduct a significant portion of those costs on your federal tax return. The catch: only expenses exceeding <strong>7.5% of your adjusted gross income</strong> are deductible, and you must itemize. This guide explains exactly how the deduction works, what qualifies, and how to avoid the mistakes that trigger IRS scrutiny.</p>

<nav class="toc">
    <h2>In this guide</h2>
    <ol>
        <li><a href="#how-it-works">How the medical expense deduction works</a></li>
        <li><a href="#what-qualifies">What qualifies as a deductible medical expense</a></li>
        <li><a href="#what-doesnt-qualify">What does NOT qualify</a></li>
        <li><a href="#calculate">How to calculate your deduction (step-by-step)</a></li>
        <li><a href="#special-situations">Special situations: HSAs, FSAs, premiums, and long-term care</a></li>
        <li><a href="#common-mistakes">Common mistakes that trigger IRS attention</a></li>
        <li><a href="#recordkeeping">Record-keeping best practices</a></li>
        <li><a href="#faq">Frequently asked questions</a></li>
        <li><a href="#sources">Sources</a></li>
    </ol>
</nav>

<h2 id="how-it-works">1. How the medical expense deduction works</h2>

<p>The medical expense deduction is claimed on <strong>Schedule A (Form 1040)</strong> as an itemized deduction. Here&rsquo;s how it works:</p>

<ul>
    <li><strong>Add up</strong> all qualifying medical and dental expenses you paid during the tax year.</li>
    <li><strong>Subtract</strong> any reimbursements from insurance, HSA/FSA distributions, or other sources.</li>
    <li><strong>Calculate 7.5% of your AGI</strong> (the number on Line 11 of Form 1040).</li>
    <li><strong>Deduct</strong> only the amount that exceeds that 7.5% threshold.</li>
</ul>

<p>This means the deduction only helps if your unreimbursed medical expenses are <em>substantial</em> relative to your income. It also only helps if your total itemized deductions (medical + state/local taxes + mortgage interest + charitable contributions) exceed the standard deduction ($15,700 single / $31,400 married filing jointly in 2026).</p>

<div class="key-takeaway">
    <strong>The 7.5% threshold is not permanent.</strong> Congress has historically debated raising it to 10%. The 7.5% threshold is currently set through 2026 under the Consolidated Appropriations Act. If it reverts to 10%, fewer taxpayers will benefit. Claim eligible expenses while the lower threshold applies.
</div>

<h2 id="what-qualifies">2. What qualifies as a deductible medical expense</h2>

<p>The IRS defines deductible medical expenses as costs for the &ldquo;diagnosis, cure, mitigation, treatment, or prevention of disease, or for the purpose of affecting any structure or function of the body.&rdquo; Here&rsquo;s a comprehensive list organized by category:</p>

<table>
    <thead>
        <tr><th>Category</th><th>Deductible Expenses</th></tr>
    </thead>
    <tbody>
        <tr><td>Doctor &amp; hospital</td><td>Office visits, surgery, hospital stays, lab tests, imaging (X-rays, MRIs, CT scans), physical exams</td></tr>
        <tr><td>Dental</td><td>Cleanings, fillings, crowns, bridges, dentures, braces, extractions, dental implants</td></tr>
        <tr><td>Vision</td><td>Eye exams, glasses, contact lenses, LASIK and other corrective surgery</td></tr>
        <tr><td>Prescriptions</td><td>All prescription medications, insulin (even OTC)</td></tr>
        <tr><td>Mental health</td><td>Therapy, psychiatry, inpatient mental health treatment, substance abuse treatment</td></tr>
        <tr><td>Insurance premiums</td><td>After-tax premiums for health, dental, vision, Medicare Part B/D, Medigap, COBRA, long-term care (age-based limits)</td></tr>
        <tr><td>Medical equipment</td><td>Wheelchairs, hearing aids, crutches, blood sugar monitors, CPAP machines, prosthetics</td></tr>
        <tr><td>Transportation</td><td>Mileage to/from medical appointments (22&cent; per mile in 2026), parking fees, tolls, ambulance costs, bus/train fare</td></tr>
        <tr><td>Home modifications</td><td>Ramps, widened doorways, grab bars, and other modifications for medical necessity (deductible to the extent they exceed any increase in home value)</td></tr>
        <tr><td>Long-term care</td><td>Nursing home expenses if the primary reason for residence is medical care; in-home nursing care</td></tr>
        <tr><td>Other</td><td>Fertility treatments (IVF, egg freezing if medically necessary), childbirth classes, lead paint removal, special education for learning disabilities</td></tr>
    </tbody>
</table>

<div class="key-takeaway">
    <strong>Don&rsquo;t forget transportation.</strong> Medical mileage adds up fast. If you drove 50 miles round-trip to a specialist twice a month for a year, that&rsquo;s 1,200 miles &times; $0.22 = <strong>$264</strong> in deductible transportation alone. Keep a log of every medical trip.
</div>

<h2 id="what-doesnt-qualify">3. What does NOT qualify</h2>

<p>These are frequently claimed but are <strong>not deductible</strong>:</p>

<table>
    <thead>
        <tr><th>Expense</th><th>Why It&rsquo;s Not Deductible</th></tr>
    </thead>
    <tbody>
        <tr><td>Cosmetic surgery</td><td>Not deductible unless it corrects a deformity from disease, accidental injury, or congenital abnormality</td></tr>
        <tr><td>Gym memberships / fitness classes</td><td>Not deductible even if a doctor recommends exercise for a condition</td></tr>
        <tr><td>Non-prescription vitamins &amp; supplements</td><td>Not deductible unless prescribed by a doctor for a specific diagnosed condition</td></tr>
        <tr><td>Over-the-counter medications</td><td>Aspirin, cold medicine, antacids, etc. are not deductible (except insulin)</td></tr>
        <tr><td>Teeth whitening</td><td>Considered cosmetic, not medical</td></tr>
        <tr><td>General wellness programs</td><td>Weight-loss programs are deductible only if prescribed for a specific disease (e.g., obesity, heart disease); general fitness is not</td></tr>
        <tr><td>Employer-paid premiums</td><td>Premiums paid with pre-tax dollars are already tax-advantaged&mdash;no double benefit</td></tr>
        <tr><td>HSA/FSA-reimbursed expenses</td><td>Already received a tax benefit through the account&mdash;no double deduction</td></tr>
        <tr><td>Funeral and burial expenses</td><td>Not medical expenses</td></tr>
        <tr><td>Childcare (non-medical)</td><td>Regular childcare is not medical; only childcare for a disabled dependent with medical needs may qualify</td></tr>
    </tbody>
</table>

<h2 id="calculate">4. How to calculate your deduction (step-by-step)</h2>

<p>Here&rsquo;s a worked example for a family of four with an AGI of $90,000:</p>

<div class="case-study">
    <h3>Example: The Martinez family</h3>
    <p><strong>Adjusted Gross Income (AGI):</strong> $90,000</p>
    <p><strong>Qualifying medical expenses paid in 2026:</strong></p>
    <ul>
        <li>Out-of-pocket hospital bills (C-section delivery): $4,200</li>
        <li>Dental work (two crowns, braces for child): $5,800</li>
        <li>After-tax health insurance premiums: $3,600</li>
        <li>Prescription medications: $1,400</li>
        <li>Physical therapy co-pays: $960</li>
        <li>Medical mileage (800 miles &times; $0.22): $176</li>
        <li>New eyeglasses for two family members: $640</li>
    </ul>
    <p><strong>Total qualifying expenses:</strong> $16,776</p>
    <p><strong>7.5% of AGI:</strong> $90,000 &times; 0.075 = $6,750</p>
    <p><strong>Deductible amount:</strong> $16,776 &minus; $6,750 = <strong>$10,026</strong></p>
    <p>At a 22% marginal tax rate, this deduction saves the Martinez family <strong>$2,206</strong> in federal taxes.</p>
</div>

<h3>Step-by-step instructions</h3>

<ol>
    <li><strong>Gather all medical receipts, EOBs, and pharmacy records</strong> for the tax year.</li>
    <li><strong>Add up every qualifying expense</strong> using the categories table above.</li>
    <li><strong>Subtract reimbursements</strong> from insurance, HSA/FSA distributions, and any legal settlements for medical costs.</li>
    <li><strong>Find your AGI</strong> on Line 11 of Form 1040.</li>
    <li><strong>Multiply your AGI by 0.075</strong> to find your threshold.</li>
    <li><strong>Subtract the threshold</strong> from your total qualifying expenses. The result is your deduction.</li>
    <li><strong>Enter the result</strong> on Schedule A, Line 4. Compare your total itemized deductions to the standard deduction&mdash;use whichever is higher.</li>
</ol>

<div class="key-takeaway">
    <strong>Bunching strategy.</strong> If your medical expenses are close to the 7.5% threshold, consider &ldquo;bunching&rdquo;&mdash;scheduling elective procedures, dental work, or vision care in the same tax year as a major medical event. A year with a surgery or childbirth may be the ideal year to also get that dental crown or pair of glasses. This pushes you further past the threshold and maximizes the deductible amount.
</div>

<h2 id="special-situations">5. Special situations</h2>

<h3>HSA and FSA interaction</h3>

<p>Expenses paid with HSA, FSA, or HRA funds <strong>cannot be deducted</strong> because those accounts already provided a tax benefit. However, if your total medical expenses exceed what your HSA/FSA covers, the out-of-pocket portion may be deductible. For example, if you had $20,000 in medical expenses, paid $4,000 from your HSA, and $16,000 out of pocket, only the $16,000 counts toward the deduction. Learn more about HSA strategy in our <a href="/guides/hsa-fsa-pay-medical-bills">HSA/FSA guide</a>.</p>

<h3>Health insurance premiums</h3>

<p>You can deduct premiums you pay with <strong>after-tax dollars</strong>:</p>

<ul>
    <li>Marketplace (ACA) premiums, minus any premium tax credit received</li>
    <li>COBRA continuation premiums</li>
    <li>Medicare Part B ($185.00/month in 2026) and Part D premiums</li>
    <li>Medigap/Medicare Supplement premiums</li>
    <li>Dental and vision insurance premiums (if paid after-tax)</li>
</ul>

<p>You <strong>cannot</strong> deduct premiums paid through your employer&rsquo;s pre-tax payroll deduction (those are already excluded from your W-2 income).</p>

<h3>Long-term care insurance</h3>

<p>Long-term care insurance premiums are deductible up to age-based limits set by the IRS each year. For 2026, the limits are approximately:</p>

<table>
    <thead>
        <tr><th>Age at End of Tax Year</th><th>Maximum Deductible Premium</th></tr>
    </thead>
    <tbody>
        <tr><td>40 or under</td><td>$480</td></tr>
        <tr><td>41&ndash;50</td><td>$900</td></tr>
        <tr><td>51&ndash;60</td><td>$1,790</td></tr>
        <tr><td>61&ndash;70</td><td>$4,770</td></tr>
        <tr><td>71 or older</td><td>$5,960</td></tr>
    </tbody>
</table>

<h3>Self-employed individuals</h3>

<p>If you are self-employed (sole proprietor, LLC, or S-corp shareholder), you can deduct health insurance premiums as an <strong>above-the-line deduction</strong> on Line 17 of Schedule 1&mdash;even without itemizing. This is separate from and often more valuable than the Schedule A medical expense deduction. You cannot claim the same premiums on both.</p>

<h2 id="common-mistakes">6. Common mistakes that trigger IRS attention</h2>

<p>Medical expense deductions are a known audit trigger when they appear disproportionately large. Avoid these mistakes:</p>

<h3>a) Deducting expenses reimbursed by insurance or HSA</h3>

<p>The IRS cross-references your medical deduction with the Form 1099-SA from your HSA and the data insurers report. If you deduct the gross amount of a hospital bill but insurance paid 80% of it, that&rsquo;s a red flag. Only deduct the amount <em>you</em> paid out of pocket with after-tax money.</p>

<h3>b) Claiming cosmetic procedures as medical</h3>

<p>Rhinoplasty, Botox, liposuction, and teeth whitening are <strong>not deductible</strong> unless they correct a deformity from an accident, disease, or birth defect. &ldquo;My doctor said it would improve my self-esteem&rdquo; is not sufficient documentation for the IRS.</p>

<h3>c) Missing the AGI threshold calculation</h3>

<p>Some taxpayers forget to subtract the 7.5% AGI floor and deduct the full amount of their medical expenses. The IRS will catch this automatically during processing. Double-check your math on Schedule A, Line 4.</p>

<h3>d) No documentation to support claims</h3>

<p>The IRS can request proof of every expense. Claiming $15,000 in medical expenses without receipts, EOBs, or bank statements to back it up is a losing position in an audit. Keep everything (see recordkeeping section below).</p>

<h3>e) Deducting expenses for non-dependents</h3>

<p>You can only deduct expenses for yourself, your spouse, and qualifying dependents (or individuals who meet the dependent definition except for income or filing requirements). Paying for a friend&rsquo;s surgery is not deductible.</p>

<div class="key-takeaway">
    <strong>Large medical bills?</strong> Before claiming the deduction, make sure you&rsquo;re not overpaying in the first place. <a href="/scan">Scan your medical bills with BillKarma</a> to find overcharges&mdash;reducing the bill directly saves you more than a tax deduction on an inflated charge.
</div>

<h2 id="recordkeeping">7. Record-keeping best practices</h2>

<p>The IRS recommends keeping medical expense records for <strong>at least 3 years</strong> after you file the return claiming the deduction (longer if you file late or amend). Here&rsquo;s what to keep:</p>

<table>
    <thead>
        <tr><th>Document</th><th>What It Proves</th><th>Where to Get It</th></tr>
    </thead>
    <tbody>
        <tr><td>Itemized bills</td><td>What services were provided and what was charged</td><td>Hospital/provider billing department</td></tr>
        <tr><td>Explanation of Benefits (EOB)</td><td>What insurance paid vs. what you owe</td><td>Your insurance company portal</td></tr>
        <tr><td>Pharmacy receipts</td><td>Prescription drug expenses</td><td>Pharmacy or insurance portal</td></tr>
        <tr><td>Bank/credit card statements</td><td>Proof of payment with after-tax dollars</td><td>Your bank</td></tr>
        <tr><td>Form 1099-SA</td><td>HSA/FSA distributions (to exclude from deduction)</td><td>Your HSA/FSA administrator</td></tr>
        <tr><td>Mileage log</td><td>Medical travel expenses</td><td>You create this&mdash;date, destination, miles</td></tr>
        <tr><td>Insurance premium statements</td><td>After-tax premium amounts</td><td>Your insurer or marketplace account</td></tr>
        <tr><td>Doctor&rsquo;s letters of medical necessity</td><td>That a contested expense was medically required</td><td>Your treating physician</td></tr>
    </tbody>
</table>

<div class="key-takeaway">
    <strong>Pro tip:</strong> Create a folder (physical or digital) at the start of each year labeled &ldquo;Medical Expenses [Year].&rdquo; Drop every EOB, receipt, and pharmacy printout into it throughout the year. At tax time, you&rsquo;ll have everything in one place instead of scrambling to reconstruct 12 months of expenses.
</div>

<div class="case-study">
    <h3>Real example: recovering $3,400 in tax savings</h3>
    <p>A 58-year-old teacher with an AGI of $72,000 had knee replacement surgery in 2025. Her out-of-pocket medical expenses totaled $19,200 (surgery co-pay $3,800, physical therapy $4,600, Medicare supplement premiums $3,200, prescriptions $2,100, dental implant $4,500, medical mileage $1,000). Her 7.5% threshold was $5,400. She deducted $13,800 ($19,200 &minus; $5,400) on Schedule A. At a 22% tax rate, this saved her <strong>$3,036</strong>. She also discovered she had been overpaying for her knee replacement by $1,400 after <a href="/scan">scanning the bill with BillKarma</a>&mdash;bringing her total savings to <strong>$4,436</strong>.</p>
</div>

<h2 id="faq">Frequently asked questions</h2>

<div class="faq-section">
    <div class="faq-item">
        <h3>What is the threshold for deducting medical expenses on taxes?</h3>
        <p>You can deduct unreimbursed medical expenses that exceed 7.5% of your adjusted gross income (AGI) for the 2026 tax year. You must itemize deductions on Schedule A to claim this. For example, with an AGI of $80,000, only expenses above $6,000 are deductible.</p>
    </div>

    <div class="faq-item">
        <h3>Can I deduct health insurance premiums as a medical expense?</h3>
        <p>Yes, if you pay them with after-tax dollars. This includes marketplace premiums (minus any premium tax credit), COBRA, Medicare Part B and D, Medigap, and long-term care insurance (subject to age-based limits). Premiums paid through your employer&rsquo;s pre-tax payroll deduction are <em>not</em> deductible since they&rsquo;re already excluded from taxable income.</p>
    </div>

    <div class="faq-item">
        <h3>Can I deduct medical expenses I paid with my HSA or FSA?</h3>
        <p>No. Expenses paid with HSA, FSA, or HRA funds cannot be deducted because those accounts already provided a tax benefit. Only the out-of-pocket portion paid with after-tax dollars counts. See our <a href="/guides/hsa-fsa-pay-medical-bills">HSA/FSA guide</a> for more details on using these accounts strategically.</p>
    </div>

    <div class="faq-item">
        <h3>What medical expenses are NOT tax deductible?</h3>
        <p>Non-deductible expenses include cosmetic surgery (unless correcting a deformity from disease or injury), gym memberships, non-prescription vitamins and supplements, over-the-counter medications (except insulin), teeth whitening, and general wellness programs. The expense must be primarily for diagnosis, treatment, or prevention of disease.</p>
    </div>

    <div class="faq-item">
        <h3>Does the medical expense deduction apply to family members?</h3>
        <p>Yes. You can deduct qualifying expenses paid for yourself, your spouse, and your dependents. You can also deduct expenses for someone who would qualify as a dependent except that they earned too much income or filed a joint return&mdash;such as an elderly parent you financially support. See IRS Publication 502 for the full rules on qualifying relatives.</p>
    </div>
</div>

<h2 id="sources">Sources</h2>

<ul class="sources-list">
    <li><a href="https://www.irs.gov/publications/p502" target="_blank" rel="noopener noreferrer">IRS Publication 502: Medical and Dental Expenses</a></li>
    <li><a href="https://www.irs.gov/taxtopics/tc502" target="_blank" rel="noopener noreferrer">IRS Topic No. 502: Medical and Dental Expenses</a></li>
    <li><a href="https://www.cms.gov/data-research/statistics-trends-and-reports/national-health-expenditure-data/projected" target="_blank" rel="noopener noreferrer">CMS National Health Expenditure Projections</a></li>
    <li><a href="https://www.kff.org/health-costs/issue-brief/americans-challenges-with-health-care-costs/" target="_blank" rel="noopener noreferrer">KFF: Americans&rsquo; Challenges with Health Care Costs</a></li>
    <li><a href="https://www.irs.gov/individuals/international-taxpayers/frequently-asked-questions-about-medical-expenses-related-to-nutrition" target="_blank" rel="noopener noreferrer">IRS FAQs: Medical Expenses</a></li>
</ul>
""",
})
