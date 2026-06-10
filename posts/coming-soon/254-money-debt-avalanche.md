---
title: Debt Avalanche
description: Pay highest interest rate first, minimums on everything else. Mathematically optimal - minimizes total interest paid over time.
date: '2026-07-01'
scheduled: '2026-06-10'
tags:
- p-and-l-engineering
- coming-soon
- money
layout: layouts/post.njk
templateEngineOverride: md
image: /img/xavi-linkedin-profile.jpg
draft: false
generated_by: templeton-deep-copy-import
source_format: html
inspiration_url: https://templeton.host/money/debt-avalanche/
inspiration_category: money
---

> Source-copy draft imported from [https://templeton.host/money/debt-avalanche/](https://templeton.host/money/debt-avalanche/). Names, domain references, and local media paths were adapted for Xavi Ablaza / getablaza.com.

[←Back to Personal Finance](/money/)

[inventory](/money/inventory/)[graph](/money/graph/)

Personal Finance

# Debt Avalanche

DebtDifficulty: ★★☆☆☆

Pay highest interest rate first, minimums on everything else. Mathematically optimal - minimizes total interest paid over time.

## Interactive Visualization

⏮◀◀▶▶STEP0.25x1xZOOM

t=0s

## Prerequisites (2)

[Interest Rate Mathlvl 2](/money/interest-rate-math/)[Budgetinglvl 1](/money/budget-basics/)

## Unlocks (1)

[Moderate-Interest Debtlvl 3](/money/moderate-debt-strategy/)

## Referenced by Business (6)

Where this personal-finance concept shows up inside the operating-finance graph.

[interest rateBusiness

Strategy directly parameterized by interest rate - paying highest rate first minimizes total interest, making rate comparison the core decision variable](/business/interest-rate/)[cost minimizationBusiness

Debt avalanche is personal-scale cost minimization - pay highest-rate first to minimize total interest paid over time, same objective function (minimize cumulative cost) applied to household liabilities](/business/cost-minimization/)[high-interest debtBusiness

Direct execution strategy: once you've identified high-interest debt, avalanche is the mathematically optimal payoff order - highest rate first, minimums on everything else](/business/high-interest-debt/)[Debt SnowballBusiness

Direct counterpart strategy - snowball trades mathematical optimality (avalanche) for behavioral optimality. Understanding the tradeoff between total interest minimization and completion-rate motivation requires knowing both.](/business/debt-snowball/)[EBITDA OptimizationBusiness

Sizing cost programs by ROI and executing highest-ROI first is the same greedy ordering as paying highest-interest debt first - rank financial actions by rate of return, execute in order](/business/ebitda-optimization/)[Exit SequencingBusiness

Identical structure: rank cost programs by ROI and fund highest-return first, just as avalanche ranks debts by interest rate and pays highest first. Both are greedy ordering by rate of return on deployed capital.](/business/exit-sequencing/)

Credit card interest can turn a $3,000 balance into $6,000 in 3 years at 20% APR if only minimums are paid. Knowing which debt to attack first can save hundreds to thousands of dollars.

TL;DR:

The Debt Avalanche method pays the debt with the highest interest rate first while paying minimums on others, which tends to minimize total interest paid over time.

## The Problem - What Goes Wrong Without a Priority

What goes wrong. Many budgets allocate an extra $200 a month to debt without a clear order. That $200 may go to the largest balance, the smallest balance, or the most emotionally annoying creditor. The result: identical cash applied differently produces vastly different total interest paid. For example, consider two debts: a $5,000 credit card at 19% APR and a $5,000 personal loan at 8% APR. If $300 extra per month is applied to the loan at 8% instead of the 19% card, total interest paid over 3 years can be 20% to 40% higher than the optimal allocation. Those are hundreds to thousands of dollars lost to suboptimal ordering.

The insight. **Debt Avalanche** focuses scarce extra cash on the debt with the highest interest rate. It keeps all other debts current by paying only minimums while accelerating repayment of the costly account. Mathematically this approach minimizes cumulative interest when interest rates and compounding are the main drivers. The method relies on the principle from Interest Rate Math (d2) that a higher APR compounds faster, producing larger interest charges per dollar carried.

Practical application. Start by listing each debt with current balance, APR, and required minimum payment. Example table: $6,500 at 21% APR, min $130; $12,000 at 6% APR, min $240; $3,000 at 15% APR, min $75. Allocate available extra cash to the 21% account first. IF the highest-rate debt is paid off AND no new high-rate debt appears, THEN total interest paid will typically be lower BECAUSE every extra dollar paid immediately reduces the portion of the debt that would have incurred the highest per-dollar interest.

Trade-offs documented. Focusing on the highest-rate debt may keep a large-balance, low-rate loan outstanding for longer. That outcome can mean lower monthly psychological wins, such as fewer closed accounts in the short term. IF emotional momentum matters more than minimizing dollars, THEN a different approach may improve adherence BECAUSE behavioral payoffs can increase total repayment speed despite being suboptimal mathematically. The method assumes disciplined budgeting from Budgeting (d1) so minimums are met and no new high-rate debt accumulates.

## How It Actually Works - Mechanics, Formulas, and Numbers

What goes wrong. People often treat payments as fungible without quantifying how APRs affect interest accrual. A $1,000 balance at 20% APR accumulates about $200 yearly in interest, while the same $1,000 at 8% APR accumulates about $80. Paying down the 8% first leaves the 20% balance to compound larger absolute interest charges each month.

The insight. The core arithmetic is simple: interest per period ≈ balance × periodic rate. For monthly compounding, periodic rate = APR / 12. So monthly interest on a balance B with APR r is I=B×(r/12).TheAvalancheminimizestotalinterestbyreducingthehighest−riskB×rtermsearliest.ConsidertwodebtsAandBwithbalancesI = B × (r/12). The Avalanche minimizes total interest by reducing the highest-risk B × r terms earliest. Consider two debts A and B with balances I=B×(r/12).TheAvalancheminimizestotalinterestbyreducingthehighest−riskB×rtermsearliest.ConsidertwodebtsAandBwithbalancesB\_A and $B\_B and APRs r\_A and r\_B where r\_A > r\_B. Applying an extra payment P to debt A reduces future interest by approximately P × r\_A each year; applying P to debt B reduces future interest by about P × r\_B each year. The higher r yields more annual interest prevented per dollar paid early.

Formula examples. If APRs are 18% and 6% then annual interest avoided per dollar is 0.18 versus 0.06. So paying $1,000 to the 18% account avoids roughly $180/year; applied to the 6% account it avoids roughly $60/year.

Stepwise mechanics. 1) List debts with balance Bi, APR ri, and minimum Mi. 2) Ensure total payments cover sum(Mi). 3) Assign any extra cash E to the debt with max ri. 4) When that debt reaches $0, reassign E to the remaining highest ri. This repeats until all debts are cleared. Mathematically this greedy algorithm minimizes total interest under fixed interest rates and no prepayment penalties.

IF interest rates change frequently OR penalties apply, THEN the pure greedy choice may not minimize cost BECAUSE rate volatility or fees can alter the effective cost-per-dollar of prepayment. For example, a mortgage with prepayment penalty or step-up rate may need special handling. Quantitative caveat: the strategy saves more when the spread r\_max - r\_next is larger. If r\_max - r\_next < 1 percentage point, total interest savings over multi-year horizons may be only 1% to 5% of total interest, which could be small in dollar terms for some portfolios.

## The Decision Framework - When to Use Avalanche and Alternatives

What goes wrong. People pick a method emotionally and then ignore trade-offs. That choice can lead to worse financial outcomes or lower adherence. Examples: prioritizing the smallest balance - the Snowball - closes accounts faster but can cost 5% to 30% more interest compared to Avalanche depending on balances and rates. Picking Avalanche without checking minimums risks late fees on neglected accounts if the budget is overstretched.

The insight. Make decisions with conditional rules. Use a small, clear decision tree that balances math and behavior. The rules emphasize IF/THEN/BECAUSE reasoning so trade-offs stay explicit and actionable.

Decision rules.

- •IF total emergency savings < 3-6 months of expenses AND any debt APR > 15%, THEN keep at least $1,000 to $3,000 liquid and apply extra cash cautiously BECAUSE high-rate debt is costly but running out of cash invites new high-rate borrowing.
- •IF r\_max - r\_next ≥ 2 percentage points AND budgeted extra cash E ≥ $100/month, THEN apply Avalanche because expected interest savings over 3 years will often exceed 5% of interest paid BECAUSE each dollar targets the highest APR where interest accrues fastest.
- •IF behavioral factors reduce likelihood of sticking to the plan by more than 30%, THEN consider a hybrid: allocate 70% of E to highest-rate debt and 30% to smallest-balance accounts BECAUSE partial psychological wins can improve persistence and still capture most interest savings.
- •IF any debt has prepayment penalties, balance transfer offers, or variable promotional rates, THEN model the specific contract terms numerically before prioritizing BECAUSE contractual costs can exceed the interest-rate differential.

Practical checklist. 1) From Budgeting (d1), confirm E after essentials and minimums. 2) From Interest Rate Math (d2), compute monthly periodic rates and expected interest avoided per extra dollar. 3) Choose Avalanche IF the math advantage is material and adherence risk is low. 4) Reevaluate annually or when any APR changes by more than 1 percentage point.

Trade-offs framed. Avalanche minimizes dollars paid in interest under standard conditions. The trade-off is that it may delay the psychological payoff of closed accounts and visible progress. IF psychological payoff increases repayment speed enough, THEN a non-Avalanche plan can outperform Avalanche in calendar time BECAUSE behavior changes cash flow more than marginal interest savings sometimes.

## Edge Cases and Limitations - Where Avalanche Breaks Down

What goes wrong. Blindly applying Avalanche can produce bad outcomes in at least two scenarios: when interest rates change, and when contracts include fees or tax consequences. These issues can make the greedy choice suboptimal.

Limitation 1 - Variable rates and promotional terms. Credit cards with 0% APR for 12 months then 22% APR can invert priorities mid-plan. IF a balance has a promotional rate of 0% for 12 months AND another card currently charges 20% APR, THEN a strict Avalanche allocation may let the 20% balance grow more interest BECAUSE the promo timer changes the effective cost of each dollar over time. Practical step: treat promotional segments as separate instruments and model cash flows month by month.

Limitation 2 - Prepayment penalties and fees. Some private student loans or mortgages levy prepayment fees of 1% to 3% of prepayments. IF paying down a mortgage early triggers a 2% prepayment penalty AND the mortgage rate is 4% while a credit card is 18%, THEN paying the mortgage first could cost more BECAUSE the penalty can counteract the lower interest rate advantage. Always compute net savings after fees.

Limitation 3 - Tax and investment opportunity costs. High-deductible mortgage interest may be tax-deductible partially for some taxpayers. IF a mortgage interest is deductible at 20% effective tax benefit AND its APR is 4% while a credit card is 18%, THEN the after-tax spread is slightly smaller but still large; however, IF expected investment returns on cash are 5-7% and are tax-advantaged, THEN using cash to invest instead of paying low-rate debt can sometimes be preferable BECAUSE the opportunity cost may exceed the interest saved. This scenario depends on risk tolerance and certainty of returns.

Limitation 4 - Behavioral adherence. Avalanche is optimal only if payments are made consistently. IF adherence drops below 70% due to lack of psychological wins, THEN total time to debt freedom may increase and interest could be larger BECAUSE missed or late payments incur fees and damage credit, which may raise future borrowing costs.

Documented practical rule. Before committing to strict Avalanche, run a 12-month cash-flow simulation. If any debt APR or fee changes during that window, treat the instrument as time-segmented. That step converts uncertain outcomes into quantifiable numbers and reduces surprises.

## Worked Examples (3)

### Single High-Rate Credit Card vs Personal Loan

Balance A: $5,000 at 19% APR, minimum $100. Balance B: $7,000 at 8% APR, minimum $140. Monthly extra cash E = $400 above all minimums.

1. Compute monthly periodic rates: r\_A = 0.19/12 = 0.015833; r\_B = 0.08/12 = 0.006667.
2. Pay minimums first: total minimums = $240. Available to allocate = E = $400.
3. Apply E to highest APR (A): monthly payment to A = $100 + $400 = $500; payment to B = $140 (minimum only).
4. Estimate months to payoff roughly with constant payment and ignoring interest compounding formula for clarity: using amortization, approximate payoff for A with payment $500 and monthly interest 1.5833% yields about 11 to 12 months. For B paying only $140 per month at 0.6667% monthly interest, payoff time is roughly 61 to 65 months. Exact amortization formula gives N = ln(P/(P - B\*r\_month)) / ln(1 + r\_month).
5. Total interest comparison: paying $400 to A first avoids approximately $400 × 0.19 = $76 per year in interest compared to paying the same to B which would avoid $400 × 0.08 = $32 per year. Over 1 year this is a savings of about $44; over the 11 months until A is gone, the avoided interest compounds, producing total savings on the order of several hundred dollars compared to the reverse order.
6. Insight: The clear numeric advantage is that each dollar applied to the 19% APR reduces expected interest by about 0.11% to 0.12% per month more than applying it to the 8% account. That accumulates meaningfully within the first year.

**Insight:** This example shows why applying the $400 to the 19% debt first reduces total interest quickly. It also highlights that the lower-rate loan remains longer, but total dollars paid in interest are smaller.

### Multiple Credit Cards with Small Balances

Card 1: $1,200 at 22% APR, min $36. Card 2: $2,800 at 17% APR, min $84. Card 3: $6,000 at 12% APR, min $150. Monthly extra cash E = $300 after minimums.

1. Compute monthly rates: r1 = 0.22/12 = 0.018333; r2 = 0.17/12 = 0.014167; r3 = 0.12/12 = 0.01.
2. Total minimums = $270. Available E = $300 allocated to highest APR account, Card 1.
3. Payment to Card 1 = $36 + $300 = $336. Time to pay Card 1: amortization formula with monthly rate 0.018333 and payment 336 yields about 4 to 5 months.
4. Once Card 1 is cleared, roll the $336 to Card 2: new payment to Card 2 = $84 + $336 = $420. Time to pay Card 2 at 0.014167 monthly rate is roughly 7 to 8 months. After Card 2 clears, roll payments to Card 3, accelerating payoff.
5. Interest saved compared to Snowball (pay smallest balance but sometimes lower rate): since Card 1 is both smallest and highest rate here, Avalanche and Snowball match initially. But if Card 2 had a lower rate than Card 3 despite smaller balance, Avalanche would have favored Card 3, saving potentially 5% to 15% of total interest over the payoff period depending on balances.

**Insight:** This example demonstrates speed of elimination for high-rate small balances and the compounding benefit of rolling payments. It also shows cases where Avalanche and Snowball match, and when they diverge.

### Mixed Loan with Promotional 0% Offer

Store card: $2,500 at 0% for 12 months then 24% APR. Card B: $4,000 at 20% APR. Monthly extra cash E = $500 after minimums. Minimums moratorium included such that both are current.

1. What goes wrong if ignoring promo: applying Avalanche to Card B (20% APR) will be correct now but the 0% promo will flip to 24% after 12 months if any balance remains.
2. Model month-by-month: For first 12 months apply $500 to the 20% card. Suppose after 12 months Card B is reduced by $5,000 equivalent in payments making it near zero. The store card still has some balance; when its rate jumps to 24% it becomes the highest APR.
3. IF planning horizon < 12 months AND ability to clear the promo balance within that time, THEN prioritize the 20% card because the promo is temporally cheaper BECAUSE the 0% protects that balance temporarily. IF the promo balance cannot be cleared within 12 months, THEN allocate part of E to the promo balance early to avoid the post-promo spike BECAUSE the future 24% rate will be more costly than treating it as a time-segmented high-rate loan.
4. Compute break-even: roughly, if you can pay off the 0% $2,500 within 6 months by allocating 50% of E, you avoid the 24% penalty. If not, model post-promo interest on remaining balance.

**Insight:** This example teaches that time-limited promotional rates should be treated as separate instruments. Avalanche logic must include timing or it can accidentally leave large high-rate balances after promo expiry.

## Key Takeaways

- ✓

  **Debt Avalanche** targets the highest APR first, which typically minimizes total interest paid across debts under stable rates.
- ✓

  Compute monthly periodic rate as APR/12 to estimate interest avoided per extra dollar; paying $1,000 at 18% avoids about $180/year in interest versus $60/year at 6%.
- ✓

  Use IF/THEN/BECAUSE rules: IF the highest APR exceeds the next by ≥ 2 percentage points AND extra monthly cash ≥ $100, THEN Avalanche usually gives measurable savings BECAUSE interest avoided per dollar is materially larger.
- ✓

  Model promotional and variable-rate debt as time-segmented obligations; treat prepayment penalties and fees explicitly in the math. If penalties are 1% to 3%, include them in net savings calculations.
- ✓

  Consider behavioral trade-offs: IF psychological momentum matters and adherence would otherwise drop >30%, THEN a hybrid or Snowball may yield better real-world outcomes BECAUSE maintained payments and fewer missed months reduce fees and total interest.

## Common Mistakes

- ✗

  Ignoring promotional timing. Many treat a 0% promo like a 24% permanent rate and vice versa. That error misallocates cash because timing changes the effective cost per dollar.
- ✗

  Neglecting minimums and fees. Applying all extra cash to one debt while missing minimums on another can create late fees of $25 to $40 and penalties that exceed interest savings. AVAILABILITY of minimum coverage must be verified first.
- ✗

  Forgetting to re-evaluate. APRs can change; some cards reset to higher rates after 6 to 18 months. Not recalculating after rate changes can flip the optimal priority and increase interest by 5% to 20%.
- ✗

  Overlooking tax or investment opportunity costs. Paying down a deductible mortgage at 4% while foregoing a 5-7% expected tax-advantaged investment return may carry an opportunity cost when measured in after-tax expected returns.

## Practice

easy

Easy: Two debts: $3,000 at 16% APR (min $90) and $4,500 at 7% APR (min $110). Monthly extra cash E = $250. Which debt gets E under Debt Avalanche and how much interest does that save in the first year compared to applying E to the 7% debt? Show the math.

**Hint:** Compute avoided interest per dollar: 0.16 vs 0.07. Multiply E by APR difference to approximate annual savings.

Show solution

Highest APR is 16% so allocate E = $250 to the 16% debt. Annual interest avoided per dollar if paid to 16% instead of 7% ≈ 0.16 - 0.07 = 0.09. Annual savings ≈ $250 × 0.09 = $22.50. More accurate monthly compounding raises this slightly, so expect $22 to $25 saved in the first year.

medium

Medium: Three debts: A $8,000 student loan at 5% APR, min $160. B $2,000 credit card at 19% APR, min $50. C $10,000 auto loan at 6% APR, min $200. Monthly extra E = $300. Compare total interest paid over the next 12 months if E goes to Avalanche (B first) versus Snowball (B first only if smallest). Compute approximate difference.

**Hint:** Both methods will target B first because it is smallest and highest APR. Consider the case where Snowball and Avalanche differ if B were not the smallest. For this prompt, show that both align and calculate interest reduction by applying E to B.

Show solution

B is both smallest and highest APR, so both methods allocate E = $300 to B initially. Monthly rates: r\_B = 0.19/12 = 0.015833. Interest avoided per month on $300 ≈ $300×0.015833 = $4.75, so over 12 months ≈ $57. Annual interest avoided vs paying $300 to a lower-rate loan like 6% would be $300×(0.19-0.06)≈$39/year. Since both methods match here, difference ≈ $0 over the 12 months for priority; absolute interest saved by applying E to B vs spreading is roughly $57 to $80 depending on comparison. Conclusion: in this setup Avalanche and Snowball produce nearly identical results for the first 12 months.

hard

Hard: Edge case with promo: Card X $5,000 at 0% for 12 months then 24% APR. Card Y $6,000 at 18% APR. Monthly extra E = $600 after minimums. Emergency savings = $2,000. Use a 12-month plan to minimize interest paid over that year considering possible post-promo spike. Show recommended allocation under IF/THEN/BECAUSE logic and compute interest in year 1 and projected interest if promo balance remains after month 12.

**Hint:** Consider clearing the promotional balance within 12 months versus focusing on the 18% account. Compute payments needed to clear $5,000 in 12 months and compare interest avoided on the 18% debt.

Show solution

Option A: Clear promo in 12 months. Needed monthly extra to clear $5,000 = $5,000/12 ≈ $417 plus any minimums. With E = $600, allocate $417 to Card X and $183 to Card Y. Interest on Card Y at 18% for year 1 on remaining balance approximates B\_Y × 0.18; if payments reduce Y moderately, estimate interest ≈ $6,000×0.18 - payment reductions ≈ $1,080 - small reductions ~ $900 to $1,050. Card X pays near zero interest in year 1 because of promo. Option B: Apply all E to Card Y. Card Y receives $600 extra, reducing principal faster; Card X remains at $5,000 and after month 12 it converts to 24% APR. Projected cost after promo: if Card X still has $5,000 at 24%, yearly interest becomes $1,200. IF the promo cannot be cleared within 12 months, THEN allocate at least $417/month to Card X BECAUSE post-promo 24% would dramatically increase interest costs. So recommended allocation under IF/THEN/BECAUSE: IF capable of applying ~$417/month to Card X while maintaining $2,000 emergency cash, THEN do so and allocate leftover $183 to Card Y to minimize year-1 plus post-promo interest BECAUSE clearing the promo prevents a jump to 24% which would add about $200 to $300/year in interest for every $1,000 left after month 12. Numerical conclusion: Option A yields near-zero interest on Card X year 1 and reduces interest on Y modestly; Option B risks paying about $1,200 extra the following year if Card X remains full. Therefore Option A minimizes expected multi-year interest.

## Connections

Prerequisites referenced: Interest Rate Math (d2) at /money/d2 provides the formulas for APR versus periodic rate, amortization schedules, and compounding mechanics used here. Budgeting (d1) at /money/d1 supplies the zero-based allocation and envelope logic needed to guarantee minimum payments and fund the extra cash E. Downstream concepts unlocked: Debt Consolidation and Refinance analysis at /money/d5 requires this debt-priority understanding to evaluate which balances to consolidate for net interest improvement; Retirement vs Debt decisions at /money/d7 need avalanche-based interest forecasts to compare after-tax expected investment returns of 5-7% with debt APRs. Understanding Avalanche also enables accurate cash-flow modeling for bankruptcy planning at /money/d10 because it clarifies realistic repayment timelines and expected interest exposure.

**Disclaimer:** This content is for educational and informational purposes only and does not constitute financial, investment, tax, or legal advice. It is not a recommendation to buy, sell, or hold any security or financial product. You should consult a qualified financial advisor, tax professional, or attorney before making financial decisions. Past performance is not indicative of future results. The author is not a registered investment advisor, broker-dealer, or financial planner.

[← back to tree](/money/)[browse all →](/money/inventory/)
