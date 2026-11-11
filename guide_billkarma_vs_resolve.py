"""Guide: BillKarma vs Resolve Medical Bills."""

from guides import register, _embed

register("billkarma-vs-resolve-medical-bills", {
    "title": "BillKarma vs Resolve Medical Bills: Which Fits Your Bill?",
    "meta_description": "Resolve assigns a human advocate for bills of $5,000+ and takes 10–25% of savings. BillKarma sends a written dispute for a flat $29–$149. When each is the better choice.",
    "published": "2026-11-11",
    "author": "BillKarma Team",
    "category": "Negotiating Bills",
    "faqs": [
        {
            "q": "What is the main difference between BillKarma and Resolve?",
            "a": "Resolve assigns a human advocate who negotiates by phone and charges a share of the savings. BillKarma checks the bill against Medicare rates and sends a written dispute to the hospital for a flat fee, with automatic follow-ups.",
        },
        {
            "q": "Does Resolve take small medical bills?",
            "a": "Resolve's How We Work page lists debts of $5,000 or more. For smaller bills, a written dispute, a financial assistance application or doing it yourself is usually the better route.",
        },
        {
            "q": "Which is cheaper, BillKarma or Resolve?",
            "a": "BillKarma, on almost every bill. Its flat fee is $29 to $149. Resolve charges 25% of savings on bills of $5,000 to $15,000 and 10% above that, with minimum fees of up to $1,000 or $2,500. Resolve does more for that price, including phone negotiation and insurance appeals.",
        },
        {
            "q": "Can Resolve help with insurance denials?",
            "a": "Yes. Resolve says it appeals denied or underpaid claims when appropriate. BillKarma's dispute service doesn't handle insurance denials; it disputes hospital charges.",
        },
        {
            "q": "What happens if neither lowers my bill?",
            "a": "Resolve refunds its deposit in full if it finds no savings. BillKarma refunds its flat fee in full if the bill isn't reduced within 45 days.",
        },
    ],
    "body": f"""
<p class="lead"><strong>Short answer:</strong> pick <a href="https://www.resolvemedicalbills.com/how-we-work" target="_blank" rel="noopener">Resolve</a> if your bill is over about $15,000, involves insurance denials, or you want a person making the calls. Pick BillKarma if the bill is under that, the problem is errors or prices far above Medicare, and you'd rather pay <strong>$29&ndash;$149 flat</strong> than <strong>10%&ndash;25% of your savings</strong>.</p>

<p>We make BillKarma, so read this with that in mind. Every fact about Resolve below comes from Resolve's own website, checked in November 2026, and we say plainly where Resolve is the better choice.</p>

<nav class="toc">
    <h2>In this guide</h2>
    <ol>
        <li><a href="#side-by-side">Side by side</a></li>
        <li><a href="#cost">What each costs on real bill sizes</a></li>
        <li><a href="#resolve-better">When Resolve is the better choice</a></li>
        <li><a href="#billkarma-better">When BillKarma is the better choice</a></li>
        <li><a href="#neither">When you need neither</a></li>
        <li><a href="#faq">Frequently asked questions</a></li>
        <li><a href="#sources">Sources</a></li>
    </ol>
</nav>

<h2 id="side-by-side">1. Side by side</h2>

<table>
    <thead>
        <tr><th></th><th>Resolve</th><th>BillKarma</th></tr>
    </thead>
    <tbody>
        <tr><td><strong>How it works</strong></td><td>A dedicated advocate reviews the bill, calls the hospital and insurer, and negotiates</td><td>Checks every line against Medicare rates, writes a dispute letter, sends it to billing and follows up automatically</td></tr>
        <tr><td><strong>Bills it takes</strong></td><td>Debts of $5,000 or more; insured, uninsured or in collections</td><td>Hospital and facility bills of any size</td></tr>
        <tr><td><strong>Fee</strong></td><td>25% of savings ($5k&ndash;$15k bills), 10% (over $15k)</td><td>Flat: $29 (under $1k), $49 ($1k&ndash;$5k), $99 ($5k&ndash;$20k), $149 (over $20k)</td></tr>
        <tr><td><strong>Minimum fee</strong></td><td>Lower of $1,000 or half the savings; $2,500 on bills over $15k</td><td>None beyond the flat fee</td></tr>
        <tr><td><strong>Upfront</strong></td><td>$249 or $499 deposit, applied to the fee</td><td>The flat fee</td></tr>
        <tr><td><strong>If nothing is saved</strong></td><td>Deposit refunded</td><td>Fee refunded if not reduced within 45 days</td></tr>
        <tr><td><strong>Phone negotiation</strong></td><td>Yes</td><td>No, written only</td></tr>
        <tr><td><strong>Insurance appeals</strong></td><td>Yes, when appropriate</td><td>No</td></tr>
        <tr><td><strong>Charity care applications</strong></td><td>Yes</td><td>Free eligibility check; certified mailing $9</td></tr>
        <tr><td><strong>Typical timeline</strong></td><td>About 4 months on average</td><td>Letter sent right away; follow-ups on days 7, 14, 30, 45</td></tr>
    </tbody>
</table>

<div class="key-takeaway">
    <strong>Find out what's wrong first.</strong> <a href="/scan">Upload your bill to BillKarma</a> &mdash; the check is free and shows which charges are duplicates or far above Medicare, whichever service you use next.
</div>

<h2 id="cost">2. What each costs on real bill sizes</h2>

<p>These use each company's published prices. The savings figures are examples to show the math, not predictions.</p>

<table>
    <thead>
        <tr><th>Bill</th><th>Example savings</th><th>Resolve fee</th><th>BillKarma fee</th></tr>
    </thead>
    <tbody>
        <tr><td>$2,400 ER visit</td><td>$900</td><td>Not offered (under $5,000)</td><td>$49</td></tr>
        <tr><td>$8,000 outpatient surgery</td><td>$3,000</td><td>$1,000 (minimum fee: lower of $1,000 or half of $3,000)</td><td>$99</td></tr>
        <tr><td>$12,000 surgery</td><td>$4,000</td><td>$1,000 (25%)</td><td>$99</td></tr>
        <tr><td>$40,000 inpatient stay</td><td>$15,000</td><td>$2,500 (minimum fee)</td><td>$149</td></tr>
    </tbody>
</table>

<p>The fee gap is large. The real question is whether a human advocate would win a bigger reduction than a written dispute. On a big, messy bill, often yes. On a bill with a clear duplicate or an obvious overcharge, usually not. For every major service's prices, see <a href="/guides/medical-bill-negotiation-service-cost/">what medical bill negotiation services cost</a>. Weighing Goodbill instead? Read <a href="/guides/billkarma-vs-goodbill-medical-bills/">BillKarma vs Goodbill</a>.</p>

{_embed(mode="markup", title="How far above Medicare is your charge?", subtitle="Enter a billing code and the amount charged.", height="420")}

<h2 id="resolve-better">3. When Resolve is the better choice</h2>

<ul>
    <li><strong>Large bills.</strong> On bills over about $15,000, a 10% fee with a person on the phone can be worth it.</li>
    <li><strong>Insurance problems.</strong> Denied or underpaid claims need an appeal to the insurer. Resolve handles that; BillKarma doesn't.</li>
    <li><strong>You want someone to handle everything.</strong> A named advocate who makes calls and does the paperwork.</li>
    <li><strong>Credit report worries.</strong> Resolve says it works to keep medical bills off credit reports.</li>
</ul>

<div class="key-takeaway">
    <strong>Know your hospital before you call.</strong> Check our <a href="/hospitals/">hospital directory</a> &mdash; the billing phone number, financial assistance policy and how far its prices run above Medicare.
</div>

<h2 id="billkarma-better">4. When BillKarma is the better choice</h2>

<ul>
    <li><strong>Bills under $5,000.</strong> Resolve doesn't list them; BillKarma's fee is $29 or $49.</li>
    <li><strong>Clear errors.</strong> Duplicate lines, wrong quantities or services you didn't receive. A written dispute fixes these without a negotiator.</li>
    <li><strong>You want a paper trail.</strong> Every request is in writing and dated.</li>
    <li><strong>You want to keep the savings.</strong> A flat fee means a $3,000 reduction costs you $99, not $1,000.</li>
</ul>

<h2 id="neither">5. When you need neither</h2>

<p>If your income is under the hospital's limit and it's a nonprofit hospital, apply for <a href="/guides/hospital-financial-assistance-charity-care/">financial assistance</a> first. It can erase the bill for free, and the nonprofit Dollar For will help you apply at no cost. You can also <a href="/guides/how-to-dispute-a-medical-bill/">dispute the bill yourself</a> with our free letters.</p>

<h2 id="faq">Frequently asked questions</h2>

<div class="faq-section">
    <div class="faq-item">
        <h3>What is the main difference between BillKarma and Resolve?</h3>
        <p>Resolve assigns a human advocate who negotiates by phone and charges a share of the savings. BillKarma checks the bill against Medicare rates and sends a written dispute for a flat fee, with automatic follow-ups.</p>
    </div>
    <div class="faq-item">
        <h3>Does Resolve take small medical bills?</h3>
        <p>Resolve's How We Work page lists debts of $5,000 or more. For smaller bills, a written dispute, a financial assistance application or doing it yourself is usually the better route.</p>
    </div>
    <div class="faq-item">
        <h3>Which is cheaper, BillKarma or Resolve?</h3>
        <p>BillKarma, on almost every bill: $29 to $149 flat. Resolve charges 25% of savings on bills of $5,000 to $15,000 and 10% above that, with minimum fees. Resolve does more for that price, including phone negotiation and insurance appeals.</p>
    </div>
    <div class="faq-item">
        <h3>Can Resolve help with insurance denials?</h3>
        <p>Yes. Resolve says it appeals denied or underpaid claims when appropriate. BillKarma's dispute service doesn't; see <a href="/guides/how-to-appeal-insurance-denial/">how to appeal an insurance denial</a>.</p>
    </div>
    <div class="faq-item">
        <h3>What happens if neither lowers my bill?</h3>
        <p>Resolve refunds its deposit in full if it finds no savings. BillKarma refunds its flat fee in full if the bill isn't reduced within 45 days.</p>
    </div>
</div>

<h2 id="sources">Sources</h2>

<ul class="sources-list">
    <li><a href="https://www.resolvemedicalbills.com/how-we-work" target="_blank" rel="noopener">Resolve: How we work, services, bill sizes and fees (checked Nov 2026)</a></li>
    <li><a href="https://resolvemedicalbills.com/faqs/how-much-does-it-cost-to-work-with-resolve" target="_blank" rel="noopener">Resolve: How much does it cost? (checked Nov 2026)</a></li>
    <li><a href="https://www.resolvemedicalbills.com/faq" target="_blank" rel="noopener">Resolve: FAQ, timeline and credit help (checked Nov 2026)</a></li>
    <li><a href="https://triagecancer.org/dollar-for-charity-care" target="_blank" rel="noopener">Triage Cancer: Dollar For's free charity care help</a></li>
    <li><a href="https://www.irs.gov/charities-non-profits/financial-assistance-policies-faps" target="_blank" rel="noopener">IRS: Financial assistance policies for nonprofit hospitals (Section 501(r))</a></li>
</ul>
""",
})
