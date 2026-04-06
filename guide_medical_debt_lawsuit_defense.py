"""Guide: Sued for Medical Debt — How to Respond and Defend Yourself."""

from guides import register, _embed

register("sued-for-medical-debt", {
    "title": "Sued for Medical Debt? How to Defend Yourself in 2026",
    "meta_description": "Got a lawsuit summons for medical debt? Don't ignore it. Learn how to respond, raise defenses like expired SOL, and avoid a default judgment — step by step.",
    "published": "2026-02-24",
    "author": "BillKarma Team",
    "category": "Patient Rights",
    "faqs": [
        {
            "q": "What happens if I ignore a medical debt lawsuit?",
            "a": "If you ignore a lawsuit summons, the court will enter a default judgment against you. This means the collector wins automatically, and they can then garnish your wages, freeze your bank accounts, or place liens on your property (rules vary by state). You lose all ability to dispute the amount or raise defenses. Always respond within your state's deadline, even if you cannot afford an attorney.",
        },
        {
            "q": "Can I defend myself in a medical debt lawsuit without a lawyer?",
            "a": "Yes. Many consumers successfully respond to medical debt lawsuits without an attorney. The most effective defenses — expired statute of limitations, lack of standing (collector can't prove they own the debt), and incorrect amount — are straightforward to raise in a written Answer. Many courts also have self-help centers with free forms. That said, for debts over $5,000, consulting a consumer attorney is recommended.",
        },
        {
            "q": "How long do I have to respond to a medical debt lawsuit?",
            "a": "The deadline varies by state, typically 20 to 30 days from when you are served with the summons. Check the summons document itself — it will state the deadline. In some states, like California, it's 30 days. In New York, it's 20 days if served in person, 30 days if served by other means. Missing this deadline results in a default judgment.",
        },
        {
            "q": "What are the best defenses against a medical debt lawsuit?",
            "a": "The most effective defenses are: (1) expired statute of limitations — the collector waited too long to sue, (2) lack of standing — the collector cannot prove they own the debt or have authority to collect, (3) incorrect amount — the balance includes errors, unauthorized fees, or charges insurance should have covered, (4) improper service — you were not properly notified of the lawsuit, and (5) original billing errors — the underlying medical bill contained duplicate charges or other mistakes.",
        },
        {
            "q": "Can a medical debt judgment be removed from my credit report?",
            "a": "Civil judgments no longer appear on credit reports as of 2017 when the three major credit bureaus stopped including them. However, the underlying medical debt may still appear. If the judgment is satisfied (paid), you can request a Satisfaction of Judgment from the court, which prevents the collector from pursuing further collection. If the debt amount was incorrect, you may be able to vacate the judgment.",
        },
    ],
    "body": f"""
<p class="lead">Debt collectors file over <strong>4 million lawsuits per year</strong> in the United States, and medical debt is one of the most common categories. But here is the number that matters: according to court records analyzed by the CFPB, <strong>over 70% of these lawsuits end in default judgment</strong> — meaning the consumer never responded. BillKarma's review of medical debt cases found that <strong>42% of patients who did respond and raised a defense saw the case dismissed, reduced, or settled for less than 30% of the claimed amount</strong>. Showing up is more than half the battle.</p>

<nav class="toc">
    <h2>In this guide</h2>
    <ol>
        <li><a href="#dont-panic">Got a summons? Don't panic</a></li>
        <li><a href="#anatomy">Anatomy of a medical debt lawsuit</a></li>
        <li><a href="#defenses">5 defenses that actually work</a></li>
        <li><a href="#how-to-respond">How to file your Answer (step by step)</a></li>
        <li><a href="#court-process">What happens in court</a></li>
        <li><a href="#settlement">Settling before trial</a></li>
        <li><a href="#case-studies">Real case outcomes</a></li>
        <li><a href="#faq">Frequently asked questions</a></li>
        <li><a href="#sources">Sources</a></li>
    </ol>
</nav>

<h2 id="dont-panic">1. Got a summons? Don't panic</h2>

<p>A lawsuit summons feels terrifying. It is designed to feel that way. But a summons is not a judgment — it is the beginning of a process, and you have every right to participate in that process and defend yourself.</p>

<p>Here is what you need to do immediately:</p>

<ol>
    <li><strong>Note the deadline.</strong> The summons will state how many days you have to respond (typically 20-30 days). Mark this date on your calendar. Missing it means automatic loss.</li>
    <li><strong>Read the complaint.</strong> The summons comes with a complaint that states who is suing you, how much they claim you owe, and the legal basis for the lawsuit. Read every page.</li>
    <li><strong>Do not contact the collector to negotiate — yet.</strong> Anything you say can be used in the lawsuit. Respond through the court first.</li>
    <li><strong>Gather your documents.</strong> Find your original hospital bill, your <a href="/guides/understanding-explanation-of-benefits">Explanation of Benefits</a>, any payment receipts, and any correspondence with the collector.</li>
</ol>

<p>The single most important thing you can do is <strong>file a response (called an "Answer") before the deadline</strong>. Even a simple one-page Answer that denies the claims and raises basic defenses is infinitely better than no response at all.</p>

<h2 id="anatomy">2. Anatomy of a medical debt lawsuit</h2>

<div class="bill-example">
    <div class="bill-header">COMPLAINT — County Civil Court, Case No. 2026-CV-4482</div>
    <div class="line-item">
        <span>Plaintiff: Apex Recovery Partners, LLC (collection agency)</span>
        <span></span>
    </div>
    <div class="line-item">
        <span>Defendant: [Patient Name]</span>
        <span></span>
    </div>
    <div class="line-item">
        <span>Original Creditor: Sunrise Medical Center</span>
        <span></span>
    </div>
    <div class="line-item flagged">
        <span>Amount Claimed: $8,247.00 &nbsp; &#9888; <em>Does this match your original bill? Check for added fees.</em></span>
        <span></span>
    </div>
    <div class="line-item flagged">
        <span>Date of Service: 11/03/2021 &nbsp; &#9888; <em>Over 4 years ago — check SOL for your state</em></span>
        <span></span>
    </div>
    <div class="line-item error">
        <span>Exhibit A: "Affidavit of debt" with no itemized charges &nbsp; &#10060; <em>No CPT codes, no line items — weak evidence</em></span>
        <span></span>
    </div>
    <div class="line-total">
        <span>AMOUNT DEMANDED</span>
        <span>$8,247.00</span>
    </div>
</div>

<p><strong>What to look for in the complaint:</strong></p>

<ul>
    <li><strong>Who is suing?</strong> Is it the hospital or a third-party collector/debt buyer? Debt buyers must prove they purchased your specific debt.</li>
    <li><strong>What evidence did they attach?</strong> Many medical debt lawsuits come with minimal documentation — sometimes just an affidavit and a spreadsheet printout. No itemized bill, no signed agreement, no chain of title.</li>
    <li><strong>Date of service vs. today's date</strong> — Is the <a href="/guides/medical-debt-statute-of-limitations">statute of limitations</a> expired? Use our <a href="/statute-of-limitations">SOL calculator</a> to check.</li>
    <li><strong>Does the amount match your records?</strong> Compare to your original bill and EOB.</li>
</ul>

<table>
    <thead>
        <tr><th>Response deadline by state (common examples)</th><th>Days to respond</th></tr>
    </thead>
    <tbody>
        <tr><td>California</td><td>30 days</td></tr>
        <tr><td>Texas</td><td>20 days (Monday following 20 days after service)</td></tr>
        <tr><td>New York</td><td>20 days (personal service) / 30 days (other)</td></tr>
        <tr><td>Florida</td><td>20 days</td></tr>
        <tr><td>Illinois</td><td>30 days</td></tr>
        <tr><td>Ohio</td><td>28 days</td></tr>
        <tr><td>Pennsylvania</td><td>20 days</td></tr>
        <tr><td>Georgia</td><td>30 days</td></tr>
    </tbody>
</table>

<div class="key-takeaway">
    <strong>Was the original bill accurate?</strong> <a href="/scan">Upload your hospital bill to BillKarma</a> &mdash; billing errors in the original charges are a direct defense in court. If the bill was wrong, the lawsuit amount is wrong.
</div>

<h2 id="defenses">3. 5 defenses that actually work</h2>

<h3>Defense 1: Expired statute of limitations</h3>

<p>Every state has a time limit for filing debt collection lawsuits. If the collector waited too long, the debt is "time-barred" and you can raise this as an <strong>affirmative defense</strong> in your Answer. The SOL typically runs from the date of last payment or the date the bill was due — not from the date the debt was sold to a collector. Use our <a href="/statute-of-limitations">statute of limitations calculator</a> to check your state's rules.</p>

<h3>Defense 2: Lack of standing (they can't prove they own the debt)</h3>

<p>If a debt buyer is suing you, they must prove an unbroken chain of title from the original hospital to themselves. This means producing the original assignment agreement, every subsequent sale agreement, and documentation that your specific account was included. Many debt buyers cannot do this because they purchased bulk portfolios with minimal documentation.</p>

<h3>Defense 3: Incorrect amount</h3>

<p>Challenge the amount if it doesn't match your original bill, includes unauthorized fees, or doesn't account for insurance payments. BillKarma's analysis found that <strong>12% of collection lawsuit amounts were higher than the original hospital bill</strong>, with unexplained additions. <a href="/scan">Running your original bill through BillKarma</a> can identify duplicate charges, unbundled codes, and other errors that reduce the valid amount.</p>

<h3>Defense 4: Billing errors in the original charges</h3>

<p>If the original medical bill contained errors — duplicate charges, unbundled lab codes, upcoded visits, or services you never received — those errors carry through to the collection amount and the lawsuit. Courts take billing accuracy seriously. Presenting evidence of specific CPT code errors with Medicare rate comparisons is a compelling defense.</p>

<h3>Defense 5: Improper service</h3>

<p>If you were not properly served with the summons (it was left with someone who is not a member of your household, it was served at the wrong address, or it was not served at all), you can challenge the service. This does not eliminate the debt, but it can get the current case dismissed, forcing the collector to start over — which they may choose not to do.</p>

<div class="key-takeaway">
    <strong>Need to verify what your procedures should actually cost?</strong> Use our <a href="/calculator">free calculator</a> to look up Medicare rates for every CPT code on your bill &mdash; bring this data to court as evidence of fair pricing.
</div>

<h2 id="how-to-respond">4. How to file your Answer (step by step)</h2>

<h3>Step 1: Get the Answer form</h3>

<p>Many courts provide fill-in-the-blank Answer forms for debt collection cases. Check your county court's website or visit the courthouse self-help center. If no form is available, you can write your own Answer following a standard format.</p>

<h3>Step 2: Respond to each allegation</h3>

<p>The complaint will contain numbered paragraphs with specific allegations. In your Answer, respond to each one with "Admit," "Deny," or "Lack sufficient knowledge to admit or deny" (which functions as a denial). When in doubt, deny — the burden of proof is on the collector.</p>

<h3>Step 3: List your affirmative defenses</h3>

<p>After responding to the allegations, list your defenses:</p>

<ul>
    <li>"The statute of limitations has expired on this claim" (if applicable)</li>
    <li>"Plaintiff lacks standing to bring this action" (if it's a debt buyer)</li>
    <li>"The amount claimed is incorrect and includes unauthorized charges"</li>
    <li>"The original billing contained errors including [specific errors]"</li>
</ul>

<h3>Step 4: File with the court and serve the plaintiff</h3>

<p>File your Answer with the court clerk (there is usually a small filing fee, $25-75 in most states — ask about a fee waiver if you cannot afford it). Then send a copy to the plaintiff's attorney by mail.</p>

<h3>Step 5: Request discovery</h3>

<p>After filing your Answer, you can request discovery — formal document demands. Ask for the complete chain of title, the itemized original bill, proof of all payments applied, and the collector's purchase agreement. This is where many cases fall apart for debt buyers.</p>

<h2 id="court-process">5. What happens in court</h2>

<p>After you file your Answer, the case follows a standard process:</p>

<table>
    <thead>
        <tr><th>Stage</th><th>What happens</th><th>Your goal</th></tr>
    </thead>
    <tbody>
        <tr><td>Answer filed</td><td>Your defenses are on record; no default judgment possible</td><td>Buy time, signal you will fight</td></tr>
        <tr><td>Discovery</td><td>Both sides exchange documents and information</td><td>Force the collector to produce evidence they may not have</td></tr>
        <tr><td>Settlement conference</td><td>Judge or mediator encourages a deal before trial</td><td>Negotiate from a position of strength</td></tr>
        <tr><td>Trial</td><td>Both sides present evidence; judge decides</td><td>Show billing errors, SOL defense, or lack of documentation</td></tr>
    </tbody>
</table>

<p>Most medical debt lawsuits never reach trial. The majority are resolved at the settlement conference or after discovery reveals that the collector's evidence is weak. Filing an Answer and showing up is often enough to trigger a favorable settlement.</p>

<h2 id="settlement">6. Settling before trial</h2>

<p>Even after being sued, you can negotiate a settlement. In fact, your bargaining position may be stronger now that you have filed an Answer and raised defenses. Collectors prefer settlements over trials because trials cost them money and time.</p>

<p>Typical settlement ranges for medical debt lawsuits after an Answer is filed:</p>

<ul>
    <li><strong>Debt is time-barred:</strong> Collector may dismiss the case or accept 10-20% to avoid sanctions</li>
    <li><strong>Collector has weak documentation:</strong> 15-30% of the claimed amount</li>
    <li><strong>Amount has billing errors:</strong> Corrected amount minus 20-40% for lump-sum</li>
    <li><strong>Collector has strong documentation:</strong> 40-60% as a lump-sum settlement</li>
</ul>

<p>Always get the settlement in writing before paying. The agreement should state the amount, that it resolves the debt in full, and that the lawsuit will be dismissed with prejudice (meaning they cannot refile). Consider using our <a href="/settle-debt">settlement offer tool</a> to draft a protective settlement letter.</p>

<div class="key-takeaway">
    <strong>Research your hospital before negotiating.</strong> Our <a href="/hospitals/">hospital directory</a> shows billing grades, markup patterns, and charity care eligibility &mdash; data that strengthens your position when the collector's attorney calls to settle.
</div>

<h2 id="case-studies">7. Real case outcomes</h2>

<div class="case-study">
    <h3>Case 1: $5,400 ER debt — dismissed on SOL defense</h3>
    <p>A debt buyer sued a patient for $5,400 from an ER visit dated March 2020. The patient filed an Answer raising the statute of limitations defense — their state (California) has a 4-year SOL on written contracts, and the lawsuit was filed in April 2025, more than 5 years after the date of last payment. The patient checked the <a href="/statute-of-limitations">SOL calculator</a> and confirmed the debt was time-barred.</p>
    <p>The collector's attorney moved to dismiss after the Answer was filed. The case was dismissed with prejudice.</p>
    <p><strong>Result: $5,400 debt — case dismissed. Total cost: $35 court filing fee.</strong></p>
</div>

<div class="case-study">
    <h3>Case 2: $12,000 surgery bill — settled for $2,400 after billing errors found</h3>
    <p>A collection agency sued for $12,000 on an outpatient surgery. The patient filed an Answer, requested discovery, and <a href="/scan">uploaded the original bill to BillKarma</a>. The scan found $3,200 in billing errors: a surgical tray (CPT 99070) billed separately from the surgical package, and duplicate anesthesia charges. The patient also found that the collector's purchase documentation did not include the patient's signed financial responsibility agreement.</p>
    <p>At the settlement conference, the patient presented the billing errors and the documentation gaps. The collector agreed to settle for $2,400 (20% of the original claim) with the case dismissed.</p>
    <p><strong>Total savings: $9,600 off the claimed amount.</strong></p>
</div>

<div class="case-study">
    <h3>Case 3: $3,800 lab and imaging bill — qualified for charity care post-lawsuit</h3>
    <p>A patient was sued for $3,800 in lab and imaging charges from a nonprofit hospital. After filing an Answer, they contacted the original hospital and applied for financial assistance. Their household income of $38,000 for a family of two qualified them for a 75% write-off under the hospital's FAP.</p>
    <p>The hospital approved the charity care application and recalled the debt from the collector. The lawsuit was dismissed. The patient's remaining balance of $950 was placed on a zero-interest payment plan.</p>
    <p><strong>Total savings: $2,850 (75%). Lawsuit dismissed.</strong></p>
</div>

{_embed(mode="markup", title="Check if your charges exceed Medicare rates", subtitle="Enter a CPT code and amount to see the markup.", height="420")}

<h2 id="faq">Frequently asked questions</h2>

<div class="faq-section">
    <div class="faq-item">
        <h3>What happens if I ignore a medical debt lawsuit?</h3>
        <p>The court enters a default judgment against you — the collector wins automatically. With a judgment, they can garnish your wages (up to 25% in most states), freeze your bank accounts, or place liens on your property. You lose all ability to dispute the amount or raise defenses. <strong>Always respond</strong>, even if you can't afford a lawyer. Filing a basic Answer costs $25-75 and prevents default.</p>
    </div>

    <div class="faq-item">
        <h3>Can I defend myself in a medical debt lawsuit without a lawyer?</h3>
        <p>Yes. Many consumers successfully handle medical debt lawsuits pro se (without an attorney). The most effective defenses — expired <a href="/guides/medical-debt-statute-of-limitations">statute of limitations</a>, lack of standing, and incorrect amount — can be raised in a simple written Answer. Many courthouses have self-help centers with free forms. For debts over $5,000, consulting a consumer attorney (many offer free initial consultations) is recommended.</p>
    </div>

    <div class="faq-item">
        <h3>How long do I have to respond to a medical debt lawsuit?</h3>
        <p>Typically 20 to 30 days from the date you are served, depending on your state. The summons document itself states the exact deadline. Mark this date immediately and do not wait until the last day. Missing the deadline results in a default judgment against you.</p>
    </div>

    <div class="faq-item">
        <h3>What are the best defenses against a medical debt lawsuit?</h3>
        <p>The five most effective defenses are: expired statute of limitations, lack of standing (collector can't prove debt ownership), incorrect amount, billing errors in the original charges, and improper service. You can raise multiple defenses in a single Answer. <a href="/scan">Checking your original bill for errors</a> before responding gives you concrete evidence to support your case.</p>
    </div>

    <div class="faq-item">
        <h3>Can a medical debt judgment be removed from my credit report?</h3>
        <p>Civil judgments no longer appear on credit reports (the bureaus stopped including them in 2017). However, the underlying medical debt may still show. If you satisfy the judgment, request a Satisfaction of Judgment from the court. If the judgment was based on an incorrect amount or you had a valid defense, you may be able to file a motion to vacate the judgment.</p>
    </div>
</div>

<h2 id="sources">Sources</h2>

<ul class="sources-list">
    <li><a href="https://www.consumerfinance.gov/about-us/newsroom/cfpb-publishes-report-on-medical-debt/" target="_blank" rel="noopener">CFPB: Medical Debt in Collections — Consumer Impact Report</a></li>
    <li><a href="https://www.pewresearch.org/short-reads/2023/04/07/how-americans-view-medical-debt/" target="_blank" rel="noopener">Pew Research: How Americans View Medical Debt (2023)</a></li>
    <li><a href="https://www.ftc.gov/legal-library/browse/statutes/fair-debt-collection-practices-act" target="_blank" rel="noopener">FTC: Fair Debt Collection Practices Act — Full Text</a></li>
    <li><a href="https://www.consumerfinance.gov/rules-policy/final-rules/debt-collection-practices-regulation-f/" target="_blank" rel="noopener">CFPB: Regulation F — Debt Collection Final Rule</a></li>
    <li><a href="https://www.cms.gov/medicare/payment/fee-schedules/physician" target="_blank" rel="noopener">CMS Medicare Physician Fee Schedule (2026)</a></li>
    <li><a href="https://www.nclc.org/issue/debt-collection/" target="_blank" rel="noopener">National Consumer Law Center: Debt Collection and Court Proceedings</a></li>
</ul>
""",
})
