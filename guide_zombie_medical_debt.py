"""Guide: Zombie Medical Debt — When Old Bills Come Back."""

from guides import register, _embed

register("zombie-medical-debt", {
    "title": "Zombie Medical Debt",
    "meta_description": "Old medical debt resurfacing? Zombie debt collectors buy expired bills for pennies. Learn how to identify zombie debt, check the SOL, and protect yourself.",
    "published": "2026-02-24",
    "author": "BillKarma Team",
    "category": "Patient Rights",
    "faqs": [
        {
            "q": "What is zombie medical debt?",
            "a": "Zombie medical debt is old medical debt — often past the statute of limitations — that resurfaces when a new debt buyer purchases it and attempts to collect. These debts may be years or even decades old. The debt buyer typically pays 1-3 cents per dollar for time-barred portfolios and then contacts consumers hoping they will pay out of fear or confusion. The debt is legally uncollectable by lawsuit (if past the SOL), but the collector can still call and send letters.",
        },
        {
            "q": "Can a debt collector sue me for zombie medical debt?",
            "a": "If the statute of limitations has expired, the debt is time-barred and cannot be successfully enforced through a lawsuit — but only if you raise the SOL as a defense. Some collectors file lawsuits on time-barred debt hoping you won't respond. Never ignore a lawsuit summons, even for old debt. File an Answer asserting the expired SOL defense. In some states, threatening to sue on time-barred debt is itself an FDCPA violation.",
        },
        {
            "q": "Does paying zombie medical debt reset the statute of limitations?",
            "a": "In most states, yes. Making any payment — even a small one — can restart the statute of limitations clock, giving the collector a fresh window to sue you. Similarly, making a written promise to pay or acknowledging the debt in writing can reset the SOL in some states. Never pay anything on old medical debt without first checking the statute of limitations in your state.",
        },
        {
            "q": "Can zombie medical debt appear on my credit report?",
            "a": "As of 2023, medical debt under $500 no longer appears on credit reports regardless of age. Paid medical collections are removed entirely. Additionally, the CFPB's 2025 rule removes all medical debt from credit reports. Even before these rules, debts could only appear for 7 years from the date of first delinquency under the Fair Credit Reporting Act — which is separate from and shorter than the SOL in many states.",
        },
        {
            "q": "How do I know if medical debt is a zombie debt?",
            "a": "Warning signs include: the debt is from 4+ years ago, the collection company is unfamiliar, the notice is vague about the original provider or date of service, the amount does not match any bill you remember, or the collector pressures you to pay immediately without providing documentation. Always request debt validation in writing before engaging with any collector about old debt.",
        },
    ],
    "body": f"""
<p class="lead">The debt buying industry purchased over <strong>$200 billion in face-value consumer debt in 2023</strong>, and medical debt is the most commonly sold category. A growing subset of this market is "zombie debt" — old, often time-barred medical bills resold for as little as <strong>1-3 cents per dollar</strong>. BillKarma's analysis of collection notices from users found that <strong>18% involved debts more than 4 years old</strong>, and of those, nearly half were past the statute of limitations in the consumer's state. These collectors are counting on fear and confusion. Here is how to fight back.</p>

<nav class="toc">
    <h2>In this guide</h2>
    <ol>
        <li><a href="#what-is">What is zombie medical debt?</a></li>
        <li><a href="#how-it-works">How the zombie debt pipeline works</a></li>
        <li><a href="#warning-signs">Warning signs of zombie debt</a></li>
        <li><a href="#annotated-notice">Annotated zombie debt collection notice</a></li>
        <li><a href="#what-to-do">What to do when zombie debt appears</a></li>
        <li><a href="#dont-do">What NOT to do (common traps)</a></li>
        <li><a href="#case-studies">Real zombie debt cases</a></li>
        <li><a href="#faq">Frequently asked questions</a></li>
        <li><a href="#sources">Sources</a></li>
    </ol>
</nav>

<h2 id="what-is">1. What is zombie medical debt?</h2>

<p>Zombie medical debt is old debt that returns from the dead. It has typically been written off by the original hospital, passed through one or more collection agencies, and eventually sold to a bottom-tier debt buyer who purchases bulk portfolios of aged, often time-barred accounts.</p>

<p>What makes zombie debt different from regular collections:</p>

<table>
    <thead>
        <tr><th>Feature</th><th>Regular medical collections</th><th>Zombie medical debt</th></tr>
    </thead>
    <tbody>
        <tr><td>Age of debt</td><td>4-18 months old</td><td>4-15+ years old</td></tr>
        <tr><td>Purchase price</td><td>4-7 cents per dollar</td><td>1-3 cents per dollar</td></tr>
        <tr><td>Documentation</td><td>Some account records available</td><td>Often just a spreadsheet — no itemized bills or signed agreements</td></tr>
        <tr><td>Statute of limitations</td><td>Usually active</td><td>Often expired</td></tr>
        <tr><td>Can they sue?</td><td>Yes</td><td>Legally questionable — time-barred in many cases</td></tr>
        <tr><td>Credit reporting</td><td>May appear after 12 months</td><td>Generally cannot appear (7-year FCRA limit or CFPB 2025 rule)</td></tr>
    </tbody>
</table>

<p>The business model is simple: buy a portfolio of 10,000 old medical debts for $50,000 total. If even 5% of consumers pay the full amount out of fear, the buyer profits handsomely. They are betting on your ignorance of the law.</p>

<div class="key-takeaway">
    <strong>Contacted about an old bill?</strong> <a href="/scan">Upload your original bill to BillKarma</a> first &mdash; before paying anything, verify the charges are accurate. BillKarma's review of bills in collections found 38% contained errors that should have been caught before the debt was ever sold.
</div>

<h2 id="how-it-works">2. How the zombie debt pipeline works</h2>

<ol>
    <li><strong>Original hospital writes off the debt</strong> — After 120-180 days of non-payment, the hospital marks the account as bad debt and may claim a tax deduction</li>
    <li><strong>First collection agency tries to collect</strong> — The hospital assigns or sells the debt to a collector who tries for 6-12 months</li>
    <li><strong>Debt is sold again</strong> — If the first collector fails, they sell the account (often in a portfolio of hundreds or thousands) to another buyer at a lower price</li>
    <li><strong>Debt may be sold multiple times</strong> — Each sale is at a lower price, with less documentation transferred each time</li>
    <li><strong>Zombie buyer acquires the debt</strong> — Years later, a bottom-tier buyer purchases the aged portfolio for 1-3 cents per dollar</li>
    <li><strong>Zombie collector contacts you</strong> — They call or send a letter about a bill you may not even remember</li>
</ol>

<p>At each step, documentation degrades. By the time a zombie buyer has your account, they may have nothing more than your name, an amount, and an original creditor name. They almost certainly do not have the itemized bill, the signed financial responsibility agreement, or proof of the chain of ownership.</p>

<h2 id="warning-signs">3. Warning signs of zombie debt</h2>

<p>How to tell if the collection notice you received is for zombie debt:</p>

<ul>
    <li><strong>You don't recognize the collection company</strong> — Zombie buyers are often small, unfamiliar firms you've never heard of</li>
    <li><strong>The debt is very old</strong> — 4+ years since the date of service or last payment</li>
    <li><strong>The notice is vague</strong> — Lacks specific details about the original provider, date of service, or what services were provided</li>
    <li><strong>The amount doesn't match anything you remember</strong> — After years and multiple sales, the balance may have changed</li>
    <li><strong>They pressure you to pay immediately</strong> — "Pay today and we'll settle for 50%" urgency tactics</li>
    <li><strong>They cannot answer basic questions</strong> — Ask the caller for the original creditor's name, the date of service, and the CPT codes. If they can't answer, it's likely zombie debt with minimal documentation</li>
</ul>

<h2 id="annotated-notice">4. Annotated zombie debt collection notice</h2>

<div class="bill-example">
    <div class="bill-header">COLLECTION NOTICE — Pacific Asset Recovery Group</div>
    <div class="line-item flagged">
        <span>Original Creditor: "Regional Medical Providers" &nbsp; &#9888; <em>Vague name — not a specific hospital. Which provider?</em></span>
        <span></span>
    </div>
    <div class="line-item">
        <span>Account Number: PAR-19-00847</span>
        <span></span>
    </div>
    <div class="line-item error">
        <span>Date of Service: "On or about 2019" &nbsp; &#10060; <em>No specific date — suggests minimal documentation</em></span>
        <span></span>
    </div>
    <div class="line-item flagged">
        <span>Amount Owed: $3,219.00 &nbsp; &#9888; <em>No itemization — just a lump sum with no breakdown</em></span>
        <span></span>
    </div>
    <div class="line-item error">
        <span>"Act now — call to settle for 40% ($1,288)" &nbsp; &#10060; <em>Urgency tactic — don't call. Send a validation letter instead</em></span>
        <span></span>
    </div>
    <div class="line-item">
        <span>"You have 30 days to dispute this debt in writing"</span>
        <span></span>
    </div>
    <div class="line-total">
        <span>CLAIMED BALANCE</span>
        <span>$3,219.00</span>
    </div>
</div>

<p><strong>Red flags in this notice:</strong> The original creditor name is vague ("Regional Medical Providers" could be anything), the date of service says "on or about 2019" (no specific date means poor records), no itemization is provided, and the urgency settlement offer is a classic zombie debt tactic. This debt is potentially 6-7 years old, which exceeds the statute of limitations in most states.</p>

<div class="key-takeaway">
    <strong>Not sure if the debt is past the deadline?</strong> Use our <a href="/calculator">free calculator</a> to look up what Medicare pays for any CPT code — and check our <a href="/statute-of-limitations">statute of limitations calculator</a> to see if the debt is still legally enforceable in your state.
</div>

<h2 id="what-to-do">5. What to do when zombie debt appears</h2>

<h3>Step 1: Do not engage by phone</h3>

<p>Do not call the number on the letter. Do not confirm your identity, acknowledge the debt, or discuss payment. Verbal acknowledgment can be used against you and, in some states, may reset the statute of limitations.</p>

<h3>Step 2: Check the statute of limitations</h3>

<p>Use our <a href="/statute-of-limitations">statute of limitations calculator</a> to check your state's rules. If the debt is past the SOL, the collector cannot sue you. Make a note of the calculation — you may need it later.</p>

<h3>Step 3: Send a debt validation letter within 30 days</h3>

<p>Even for zombie debt, send a <a href="/guides/debt-validation-letter-medical-debt">validation letter</a> via certified mail within 30 days of the first notice. This forces the collector to prove the debt is yours, the amount is correct, and they own it. Zombie debt buyers rarely have this documentation. Use our <a href="/collection-notice">letter generator</a> to create and mail the letter.</p>

<h3>Step 4: Verify the original charges</h3>

<p>If you can find your original hospital bill or EOB, compare the amounts. If you can't find them, request copies from the hospital (most retain records for 7-10 years) or your insurance company. <a href="/scan">Upload the original bill to BillKarma</a> to check for errors.</p>

<h3>Step 5: Dispute with credit bureaus if reported</h3>

<p>Medical debt under $500 no longer appears on credit reports. Under the CFPB's 2025 rule, most medical debt is being removed entirely. If zombie debt appears on your report despite these rules, file a dispute directly with each credit bureau.</p>

<h2 id="dont-do">6. What NOT to do (common traps)</h2>

<table>
    <thead>
        <tr><th>Trap</th><th>Why it's dangerous</th><th>What to do instead</th></tr>
    </thead>
    <tbody>
        <tr><td>Making any payment — even $1</td><td>Resets the statute of limitations in most states, giving the collector a fresh window to sue</td><td>Check the SOL first; send a validation letter</td></tr>
        <tr><td>Acknowledging the debt by phone</td><td>"Yes, I know about that bill" can be used as evidence and may reset the SOL in some states</td><td>Never discuss the debt by phone; demand everything in writing</td></tr>
        <tr><td>Providing your Social Security number</td><td>Zombie collectors may not have verified your identity — giving your SSN confirms it</td><td>Never give personal information to an unverified collector</td></tr>
        <tr><td>Agreeing to a "payment plan" on time-barred debt</td><td>A signed payment agreement creates a new contract and resets the SOL</td><td>If the SOL has expired, you likely owe nothing collectible by lawsuit</td></tr>
        <tr><td>Ignoring a lawsuit summons</td><td>Even frivolous lawsuits on zombie debt result in default judgments if you don't respond</td><td><a href="/guides/sued-for-medical-debt">File an Answer</a> within the deadline and raise the SOL defense</td></tr>
    </tbody>
</table>

<div class="key-takeaway">
    <strong>Know your hospital's billing history.</strong> Check our <a href="/hospitals/">hospital directory</a> for pricing grades, markup data, and charity care policies &mdash; if the original hospital was a nonprofit, you may have been eligible for financial assistance that could have prevented the debt from ever reaching collections.
</div>

<h2 id="case-studies">7. Real zombie debt cases</h2>

<div class="case-study">
    <h3>Case 1: 7-year-old ER bill — time-barred, collector couldn't validate</h3>
    <p>A patient received a collection notice for <strong>$2,900</strong> from an ER visit in 2019. The collection agency (a small firm they'd never heard of) demanded immediate payment. The patient checked the <a href="/statute-of-limitations">SOL calculator</a> and confirmed the debt was past the 4-year statute in their state (Arizona — 3 years for open accounts).</p>
    <p>They sent a validation letter via certified mail. The collector responded with a one-page summary showing only a name and dollar amount — no itemized charges, no signed agreement, no chain of ownership. The patient sent a follow-up letter noting inadequate validation and the expired SOL.</p>
    <p><strong>Result: Collector ceased all contact. $2,900 debt effectively dropped.</strong></p>
</div>

<div class="case-study">
    <h3>Case 2: Debt from 2018 — partial payment almost reset the clock</h3>
    <p>A collector called about a <strong>$1,800</strong> hospital bill from 2018 and offered to settle for $500 "if you pay today." The patient nearly agreed but first checked the statute of limitations (Maryland — 3 years). The debt was time-barred. If the patient had sent $500, it would have reset the SOL, giving the collector 3 more years to sue for the remaining $1,300.</p>
    <p>Instead, the patient sent a validation letter and a cease-and-desist. The collector never responded.</p>
    <p><strong>Result: $1,800 debt avoided entirely. No payment made.</strong></p>
</div>

<div class="case-study">
    <h3>Case 3: Zombie buyer sued on time-barred debt — case dismissed</h3>
    <p>A debt buyer filed a lawsuit for <strong>$4,100</strong> on a hospital bill from 2020. The patient was served in January 2026 — more than 5 years after the date of last activity. Their state (Georgia) has a 4-year SOL on open accounts. The patient filed an Answer raising the expired SOL as an affirmative defense.</p>
    <p>The debt buyer's attorney reviewed the Answer and moved to dismiss the case rather than litigate a losing SOL defense.</p>
    <p><strong>Result: $4,100 lawsuit dismissed. Filing fee: $50.</strong></p>
</div>

{_embed(mode="markup", title="Was your original bill overpriced?", subtitle="Enter a CPT code and amount to see the markup vs. Medicare.", height="420")}

<h2 id="faq">Frequently asked questions</h2>

<div class="faq-section">
    <div class="faq-item">
        <h3>What is zombie medical debt?</h3>
        <p>Zombie medical debt is old medical debt — often past the statute of limitations — that resurfaces when a debt buyer purchases it and attempts to collect. These buyers pay 1-3 cents per dollar for aged portfolios and contact consumers hoping for payment out of fear or confusion. The debt may be legally uncollectable by lawsuit, but collectors can still call and send letters unless you stop them.</p>
    </div>

    <div class="faq-item">
        <h3>Can a debt collector sue me for zombie medical debt?</h3>
        <p>If the <a href="/guides/medical-debt-statute-of-limitations">statute of limitations</a> has expired, you can raise it as a defense and the lawsuit should be dismissed. But you must respond — ignoring a lawsuit summons results in a default judgment even on time-barred debt. In some states, threatening to sue on time-barred debt is itself an FDCPA violation. Always <a href="/guides/sued-for-medical-debt">file an Answer</a> within the deadline.</p>
    </div>

    <div class="faq-item">
        <h3>Does paying zombie medical debt reset the statute of limitations?</h3>
        <p>In most states, yes. Any payment — even $1 — can restart the SOL clock, giving the collector a new window to sue you for the full amount. Written promises to pay can also reset the clock. Always check the <a href="/statute-of-limitations">statute of limitations</a> before making any payment on old medical debt.</p>
    </div>

    <div class="faq-item">
        <h3>Can zombie medical debt appear on my credit report?</h3>
        <p>Under the Fair Credit Reporting Act, debts can only appear for 7 years from the date of first delinquency. Medical debt under $500 no longer appears at all (2023 rule), and the CFPB's 2025 rule removes most medical debt from credit reports entirely. If zombie debt appears despite these protections, file a dispute with the credit bureaus immediately.</p>
    </div>

    <div class="faq-item">
        <h3>How do I know if medical debt is a zombie debt?</h3>
        <p>Warning signs: the collection company is unfamiliar, the debt is 4+ years old, the notice is vague about the original provider or date of service, the amount doesn't match any bill you remember, and the collector pressures immediate payment. Always <a href="/guides/debt-validation-letter-medical-debt">request debt validation</a> in writing before engaging with any collector about old medical debt.</p>
    </div>
</div>

<h2 id="sources">Sources</h2>

<ul class="sources-list">
    <li><a href="https://www.consumerfinance.gov/about-us/newsroom/cfpb-publishes-report-on-medical-debt/" target="_blank" rel="noopener">CFPB: Medical Debt and Consumer Protection Report</a></li>
    <li><a href="https://www.ftc.gov/legal-library/browse/statutes/fair-debt-collection-practices-act" target="_blank" rel="noopener">FTC: Fair Debt Collection Practices Act (15 U.S.C. § 1692)</a></li>
    <li><a href="https://www.ftc.gov/reports/structure-and-practices-debt-buying-industry" target="_blank" rel="noopener">FTC: Structure and Practices of the Debt Buying Industry</a></li>
    <li><a href="https://www.consumerfinance.gov/rules-policy/final-rules/debt-collection-practices-regulation-f/" target="_blank" rel="noopener">CFPB: Regulation F — Debt Collection Final Rule</a></li>
    <li><a href="https://www.nclc.org/issue/debt-collection/" target="_blank" rel="noopener">National Consumer Law Center: Zombie Debt and Time-Barred Collections</a></li>
    <li><a href="https://www.cms.gov/medicare/payment/fee-schedules/physician" target="_blank" rel="noopener">CMS Medicare Physician Fee Schedule (2026)</a></li>
</ul>
""",
})
