---
title: Debt Consolidation
description: Balance transfers, personal loans, refinancing. When consolidation reduces total cost vs when it just moves the problem around.
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
inspiration_url: https://templeton.host/money/debt-consolidation/
inspiration_category: money
---

> Source-copy draft imported from [https://templeton.host/money/debt-consolidation/](https://templeton.host/money/debt-consolidation/). Names, domain references, and local media paths were adapted for Xavi Ablaza / getablaza.com.

[←Back to Personal Finance](/money/)

[inventory](/money/inventory/)[graph](/money/graph/)

Personal Finance

# Debt Consolidation

DebtDifficulty: ★★☆☆☆

Balance transfers, personal loans, refinancing. When consolidation reduces total cost vs when it just moves the problem around.

## Interactive Visualization

⏮◀◀▶▶STEP0.25x1xZOOM

t=0s

## Prerequisites (2)

[Interest Rate Mathlvl 2](/money/interest-rate-math/)[Credit Scorelvl 2](/money/credit-score-mechanics/)

## Referenced by Business (2)

Where this personal-finance concept shows up inside the operating-finance graph.

[Personal LoanBusiness

Exact individual-scale mirror - personal loans, balance transfers, and refinancing are the consolidation tools consumers use to restructure debt](/business/personal-loan/)[Expected Total CostBusiness

Individual-scale version of comparing expected total cost across consolidation options - balance transfers, personal loans, refinancing evaluated by whether total interest paid decreases or just moves around](/business/expected-total-cost/)

Carrying high-interest debt can silently add 20-40% more cost over time than borrowers expect. A single decision about consolidation can change whether you pay $2,000 or $6,000 extra on a $10,000 balance.

TL;DR:

Debt consolidation - combining multiple debts into one vehicle like a balance transfer, personal loan, or refinance - can cut interest costs and simplify payments, but it only reduces total cost when fees, term changes, and behavior are favorable.

## What Goes Wrong - Real costs when debt compounds

Problem first. Carrying several high-rate accounts turns simple balances into long-term interest drains. Consider a $12,000 single credit card balance at 20% APR with a 2% minimum monthly payment. The approximate monthly rate is r=0.20/12≈0.0167r=0.20/12\approx0.0167r=0.20/12≈0.0167. If the minimum is 2% of balance, the payment starts at $0.02\times12{,}000= $240. With only minimums and interest compounding, the payoff time easily exceeds 8-12 years and total interest can exceed $10{,}000 to $15{,}000 depending on rate and payment behavior. That outcome surprises people who compare only balances and not cumulative interest.

Another concrete failure is juggling multiple cards. Imagine three cards with balances B1=B\_1=B1​= $4{,}000 at 18% APR, B2=B\_2=B2​= $3{,}500 at 22% APR, and B3=B\_3=B3​= $2{,}500 at 16% APR. The weighted average APR is 4,000×0.18+3,500×0.22+2,500×0.1610,000≈0.188\frac{4{,}000\times0.18+3{,}500\times0.22+2{,}500\times0.16}{10{,}000}\approx0.18810,0004,000×0.18+3,500×0.22+2,500×0.16​≈0.188 or 18.8% APR. Paying the minimum total of 2% on each card produces small reductions in principal and large cumulative interest - often adding $5{,}000 to $12{,}000 in extra cost over multi-year periods.

Why this happens numerically. With revolving debt, interest compounds monthly at r=APR/12r=\text{APR}/12r=APR/12, and the interest portion each month is Interest=r×balance\text{Interest}=r\times\text{balance}Interest=r×balance. If payments are barely above interest accrual, principal falls slowly. For example, if monthly interest on $12{,}000$ at 20% APR is $12{,}000\times0.20/12 = $200, then a $240 payment reduces principal by only $40 that month. Long sequences of such small reductions produce very large total interest paid.

Behavioral component. Having many accounts often raises credit utilization and mental friction. Utilization of 60-80% on several cards (versus 10-30% target ranges) tends to increase perceived borrowing strain and may reduce the chance of increasing payments from $240 to $400 monthly, a change that would reduce payoff time from 10 years to roughly 3-4 years for the same $12{,}000 balance. The math in "Interest Rate Math" is directly relevant here.

IF a borrower faces multiple accounts with an average APR above 15% AND monthly payments are barely above interest accrual, THEN balances will amortize extremely slowly and total interest cost will likely exceed 50% of the starting principal over a multi-year term BECAUSE the monthly interest (r=APR/12r=\text{APR}/12r=APR/12) consumes most of the payment and principal declines little. This explains why consolidation can look attractive even when not reducing the APR much.

## How It Actually Works - Mechanics, formulas, and real numbers

Insight up front. Consolidation bundles debts into a single instrument with its own APR, term, and fees. Whether total cost falls depends on three numeric levers: new APR, loan term length, and transaction fees. Key terms first. **Debt Consolidation** means combining multiple debts into one obligation. **Balance Transfer** is a credit-card-based transfer with promotional APRs like 0% for 12-18 months and fees often 2-5% of transfer volume. **Personal Loan** is an installment loan with fixed APRs commonly 6-18% for borrowers with decent credit. **Refinancing** refers to replacing an existing large loan - for example, a car or mortgage - with a new loan at a different APR and term.

Formulas matter. For an installment loan with principal LLL, monthly nominal rate r=APR/12r=\text{APR}/12r=APR/12, and nnn months, the fixed monthly payment is

P=rL1−(1+r)−nP=\dfrac{rL}{1-(1+r)^{-n}}P=1−(1+r)−nrL​.

Total amount paid equals P×nP\times nP×n. Total interest equals P×n−LP\times n - LP×n−L. For revolving balance transfers with a promotional 0% APR for mmm months and fee fff (as a decimal), the immediate cost equals f×Lf\times Lf×L. The strategy reduces future interest if and only if the avoided interest over the period exceeds the fee and any post-promo APR costs.

Example calculations. Take L=L=L= $10{,}000acrosscardsaveragingAPR20 across cards averaging APR 20% (monthly acrosscardsaveragingAPR20r=0.20/12\approx0.0167).OptionA−leaveas−isandpayfixed). Option A - leave as-is and pay fixed ).OptionA−leaveas−isandpayfixedP=$ $350/month. Option B - consolidate into a $5−year(-year (−year(n=60)personalloanat10) personal loan at 10% APR ()personalloanat10r=0.10/12\approx0.008333).Loanpayment). Loan payment ).LoanpaymentP\_B= = =\dfrac{0.008333\times10{,}000}{1-(1+0.008333)^{-60}}\approx$ $212/month$. Total paid A = $350\times T\_Awhere where whereT\_A$ is payoff months under original terms; early estimates with $350/monthmightshow might show mightshowT\_A\approx40$ months and total interest $350\times40-10{,}000= $4{,}000. Total paid B = $212\times60= $12{,}720; interest $= $2{,}720. Net savings = $1{,}280. These numbers show that a lower APR and disciplined payments reduce total interest.

Balance transfer specifics. If a card offers 0% for 12 months with a 3% fee, transferring $10{,}000 costs $300 upfront. If the borrower pays $850/month, the entire $10{,}000 is cleared in 12 months and $300 is the only extra cost. If instead payments are $300/month, after 12 months the remaining balance will incur the card's standard APR, often 18-25%, making the transfer less beneficial.

IF a consolidation lowers the APR by at least 4-8 percentage points AND the borrower uses the same or higher monthly payment toward principal, THEN total interest paid will typically fall by 20-60% BECAUSE interest is a linear function of APR and time under comparable payment schedules. This depends on the consolidation not increasing the term excessively and on fees being small relative to interest savings.

## The Decision Framework - IF/THEN/BECAUSE steps to evaluate consolidation

Problem first. People consolidate for convenience or lower monthly payments without checking whether total cost falls. The decision framework below turns that mistake into a checklist with numeric thresholds.

Step 1 - Gather numbers. Record total principal LtotalL\_{total}Ltotal​, weighted average APR APRold\text{APR}\_{old}APRold​, current monthly payment PoldP\_{old}Pold​, and payoff months if payments stay constant noldn\_{old}nold​. Example targets: LtotalL\_{total}Ltotal​ commonly $2{,}000$ to $50{,}000$, $\text{APR}\_{old}between12 between 12% and 26%, and between12n\_{old}$ from 12 to 120 months.

Step 2 - Identify consolidation offer terms. For a balance transfer include promotional APR APRpromo\text{APR}\_{promo}APRpromo​ and promo months mmm, plus fee fff (typical range 0-5%). For a personal loan include APR APRnew\text{APR}\_{new}APRnew​ and term nnewn\_{new}nnew​ (common terms 24, 36, 60 months). For refinancing include closing costs CCC and term changes Δn\Delta nΔn.

Step 3 - Compute total cost for each option. For installment consolidation use Pnew=rnewLtotal1−(1+rnew)−nnewP\_{new}=\dfrac{r\_{new}L\_{total}}{1-(1+r\_{new})^{-n\_{new}}}Pnew​=1−(1+rnew​)−nnew​rnew​Ltotal​​ and total cost =Pnew×nnew+C=P\_{new}\times n\_{new}+C=Pnew​×nnew​+C where rnew=APRnew/12r\_{new}=\text{APR}\_{new}/12rnew​=APRnew​/12. For a balance transfer with APRpromo=0\text{APR}\_{promo}=0APRpromo​=0 and fee fff, compute immediate fee =f×Ltotal=f\times L\_{total}=f×Ltotal​ and remaining balance after mmm months given payment PPP. If the remaining balance after mmm months would be zero, cost is f×Ltotalf\times L\_{total}f×Ltotal​; otherwise add post-promo interest at standard APR.

Step 4 - Compare and check thresholds. Compute savings S=TotalCostold−TotalCostnewS=\text{TotalCost}\_{old}-\text{TotalCost}\_{new}S=TotalCostold​−TotalCostnew​. If S>0S>0S>0 by at least 5-10% of LtotalL\_{total}Ltotal​ then consolidation produces meaningful savings. Also apply behavioral filters. IF the consolidation reduces APR by less than 1-2 percentage points OR lengthens the term by more than 12-24 months, THEN the consolidation may only shift payments later and could increase total interest BECAUSE lower monthly payments extend time and increase cumulative interest, offsetting small APR improvements. IF a balance-transfer promo requires paying off within mmm months and current payment discipline is low, THEN promotional savings are unlikely because failure to pay in mmm months can trigger 18-25% APR afterwards BECAUSE the promotional benefit evaporates and the transfer fee becomes sunk cost.

Step 5 - Credit effects and liquidity. Calculate utilization impact. Closing old cards can increase utilization ratio if revolving limits fall. If utilizationbefore=balancelimit≈60%\text{utilization}\_{before}=\frac{balance}{limit}\approx60\%utilizationbefore​=limitbalance​≈60% and closing a $5{,}000$ limit reduces total limit by 20-30%, utilization could jump to 75-80%, risking a 20-50 point FICO swing in some profiles. IF maintaining or increasing total available credit is required to keep utilization under 30%, THEN consider leaving low-interest cards open after consolidation BECAUSE utilization is a 30% FICO component and closing lines raises utilization proportionally.

Step 6 - Behavioral guardrails. Set a target monthly payment PtargetP\_{target}Ptarget​ equal to at least the previous principal-reduction portion plus 5-20% extra. For example, if previous Pold=P\_{old}=Pold​= $400 with interest portion $200, then aim for Ptarget≥300P\_{target}\ge300Ptarget​≥300. IF PtargetP\_{target}Ptarget​ is not feasible, THEN consolidation that reduces only monthly payments may postpone the real problem BECAUSE it lowers immediate strain but increases total interest over time.

## Edge Cases and Limitations - when the framework breaks down

Limitations first. This framework ignores several realistic elements that can flip the decision. List of important exceptions follows.

1) Variable-rate and future-rate risk. If the new instrument uses a variable APR tied to LIBOR or SOFR and current variable margin is low, initial APR might be attractive at 3-5% but could rise by 2-6 percentage points within 12-36 months. Example: a variable loan starts at 5% APR and could reach 9-11% in 2-3 years if rates increase by 4-6 percentage points. IF a borrower expects rates to rise, THEN choosing a variable-rate consolidation may end up costing more than a fixed-rate option BECAUSE interest resets upward and compounds at the higher rate.

2) Behavioral recidivism - re-accumulating debt. Consolidation that frees up available credit can create temptation. Consider someone with $10{,}000 consolidated into a $10{,}000 personal loan and $10{,}000 of freed credit on cards. IF spending returns and balance climbs to $8{,}000 at 20% APR while the loan remains at 10% and a minimum payment schedule is followed, THEN total interest across both obligations can exceed the pre-consolidation cost BECAUSE the new revolving balance accrues high-rate interest and extends total indebtedness.

3) Taxes, legal, and bankruptcy interactions. This framework does not consider tax-deductible interest like certain student loan or mortgage interest. For example, converting student loan debt that is 3-5% tax-deductible into a non-deductible personal loan at 7% can increase after-tax cost by 2-4 percentage points. Also, bankruptcy rules and dischargeability differ by debt type - consolidating may change legal posture. IF a debt is likely to be discharged or negotiated legally, THEN consolidation into an instrument with stronger collection terms may be counterproductive BECAUSE it can remove protections and alter creditor claims.

4) Fees, prepayment penalties, and closing costs. Many refinances include closing costs in the range $500 to $5{,}000. A $3{,}000 closing cost on a $100{,}000 mortgage requires multi-year windows to recoup. IF the borrower plans to move or pay off within 1-3 years, THEN refinancing with high upfront costs may not pay back BECAUSE the amortized savings per month times planned months may be less than the upfront expense.

5) Credit profile extremes. Borrowers with very low FICO scores often cannot access lower APR personal loans. Offers with APRs of 25-35% are common, which provide no benefit versus existing cards. IF new APR is higher than current weighted APR, THEN consolidation increases cost BECAUSE interest rate multiplies principal.

Each of these scenarios requires recalculating total costs numerically and testing sensitivity across plausible ranges. This framework therefore works best when all numeric inputs - APR ranges, fees, and expected term lengths - are estimated within +/−10-20% accuracy.

## Worked Examples (3)

### Balance Transfer Promo - pay off during promo

Credit cards total $10,000 at an average APR of 20%. A 0% balance transfer for 12 months with a 3% fee is available. Monthly budget allows $850 toward the debt.

1. Compute upfront fee: $fL = 0.03\times10{,}000 = $300.
2. Under promo, all transferred balance accrues no interest for 12 months. Monthly payment $P = $850 means total paid in 12 months = $850\times12 = $10{,}200.
3. Since $10{,}200 > $10{,}000, the balance will be fully repaid within 12 months; the $200 excess reduces fee+principal but is not necessary. Total cost equals principal $10{,}000 + fee $300 = $10{,}300.
4. If no transfer were used and payments stayed $850 monthly at 20% APR, approximate months to payoff is roughly 15 months and total interest could be about $600 to $1,200 depending on exact amortization. With the promo, interest avoided is roughly $600 to $1,200 while cost is $300 fee, net savings $300 to $900.

**Insight:** If payments are large enough to retire the balance within the promotional window, a 0% promo with a 2-4% fee usually saves money. The saved interest is often 2-4 times the fee when APRs are 18-24% and payoff occurs within the promo period.

### Personal Loan Consolidation - lower APR, longer term trade-off

Total revolving balances $12,000 at weighted APR 22%. Current monthly payment Pold=P\_{old}=Pold​= $400. Offer: 36-month personal loan at 11% APR with no origination fee.

1. Compute monthly rate new: rnew=0.11/12≈0.0091667r\_{new}=0.11/12\approx0.0091667rnew​=0.11/12≈0.0091667.
2. Compute new monthly payment: $P\_{new}=\dfrac{0.0091667\times12{,}000}{1-(1+0.0091667)^{-36}}\approx $388.
3. Total paid new = $388\times36 = $13{,}968. Interest paid = $1{,}968.
4. Estimate old scenario if $400 continues: approximate months to payoff for 22% APR might be about 45 months with total paid $400\times45 = $18{,}000 and interest $6{,}000.
5. Compare savings: $18{,}000 - $13{,}968 = $4{,}032 saved in total payments.

**Insight:** Even when monthly payment falls slightly from $400 to $388, the sharp APR reduction from 22% to 11% can shrink total interest by roughly $4{,}000 on $12{,}000 of debt because time under high APR is shortened and interest per month is lower.

### Refinancing with closing costs - short horizon trap

Auto loan $20,000 at 6.5% APR with 48 months remaining and monthly payment $476. Offer: refinance to 4% APR for remaining 48 months but with $800 in origination fees financed into the loan.

1. If refinancing, new principal becomes $20{,}800. Monthly rate r=0.04/12≈0.003333r=0.04/12\approx0.003333r=0.04/12≈0.003333.
2. New monthly payment $P\_{new}=\dfrac{0.003333\times20{,}800}{1-(1+0.003333)^{-48}}\approx $467.
3. Total paid new = $467\times48 = $22{,}416. Interest paid = $22{,}416 - $20{,}800 = $1{,}616.
4. Original loan: total remaining payment $476\times48 = $22{,}848. Interest remaining = $22{,}848 - $20{,}000 = $2{,}848.
5. Savings = $22{,}848 - $22{,}416 = $432 over 48 months, or about $9/month. If the borrower plans to sell the car in 12 months, savings over 12 months would be negative because the $800 fee would not be recouped.

**Insight:** Small APR reductions with moderate fees require sufficiently long remaining terms to break even. For a $800 fee and monthly saving of $9, break-even is roughly $800/9 \approx 89 months, so refinancing is not worthwhile for short horizons like 12-24 months.

## Key Takeaways

- ✓

  Compute total cost, not just monthly payment: use P=rL1−(1+r)−nP=\dfrac{rL}{1-(1+r)^{-n}}P=1−(1+r)−nrL​ to compare options.
- ✓

  Balance transfers with 0% for 12-18 months plus 2-4% fees help only if the balance is cleared within that window; otherwise promo fees become sunk costs.
- ✓

  A lower APR reduces interest linearly; a reduction of 4-8 percentage points often yields 20-60% lower total interest on multi-year balances.
- ✓

  Watch term length: lengthening the loan by 12-36 months can erase APR gains and increase total interest by 5-30% relative to shorter terms.
- ✓

  Consider credit utilization changes: closing $5{,}000 of credit limit on a $15{,}000 total limit raises utilization by ~33% and can cost 10-50 FICO points in some profiles.
- ✓

  Always compare upfront fees (2-5% or $500-$5{,}000) to projected interest savings over your realistic holding period before consolidating.

## Common Mistakes

- ✗

  Comparing only monthly payments. Why wrong: lower monthly payments can come with longer terms, increasing total interest by 5-30% on typical personal loan consolidations.
- ✗

  Ignoring transfer and origination fees. Why wrong: a 3% fee on $10{,}000 equals $300, which can wipe out the first 3-6 months of interest savings on a 0% promo.
- ✗

  Assuming credit score is unaffected. Why wrong: closing old cards after consolidation can raise utilization from 30% to 50-80%, costing an estimated 10-50 FICO points for many borrowers.
- ✗

  Using consolidation to gain breathing room and then re-borrowing. Why wrong: freeing $10{,}000 of credit and then re-accumulating $7{,}000 at 20% APR adds new interest that often nullifies prior savings.

## Practice

easy

Easy: You have $6{,}000 across two cards: $3{,}500 at 19% APR and $2{,}500 at 24% APR. A 0% balance transfer for 12 months is available with a 3% fee. You can pay $600/month. Should you transfer and will the balance be paid during the promo? Show math.

**Hint:** Compute fee 3% of $6,000 then check if $600\times12 covers principal plus fee.

Show solution

Fee = 0.03\times6{,}000 = $180. Total owed after transfer = $6{,}000 + $180 = $6{,}180. Payment capacity over promo = $600\times12 = $7{,}200. Since $7{,}200 > $6{,}180, the borrower can pay off the balance within 12 months. Therefore transferring likely saves interest. Estimated avoided interest: rough interest at weighted APR: weighted APR = (3,500\times0.19+2,500\times0.24)/6,000 = (665+600)/6,000 = 1,265/6,000 = 0.2108 or 21.08% APR. Approx annual interest avoided on $6,000 for one year = $6,000\times0.2108 = $1,265. Net savings approx $1,265 - $180 = $1,085.

medium

Medium: You owe $15{,}000 at weighted APR 21% and pay $450/month now. A personal loan offer is 11% APR for 60 months with a 1% origination fee added to principal. Calculate new monthly payment, total cost, and whether consolidation reduces total payments. Show calculations.

**Hint:** Compute new principal including 1% fee, then use installment formula for PPP. Compare total paid now estimated by continuing $450/month until payoff versus the loan total.

Show solution

Origination fee = 0.01\times15{,}000 = $150. New principal L = $15{,}150. Monthly rate r = 0.11/12 = 0.0091667. New payment P\_new = rL/(1-(1+r)^{-60}) = 0.0091667\times15{,}150 / (1-(1+0.0091667)^{-60}) ≈ $325. Total paid new = $325\times60 = $19{,}500. Interest paid = $19{,}500 - $15{,}150 = $4{,}350.

Estimate old payoff if $450/month continues at 21% APR. Monthly r\_old = 0.21/12 = 0.0175. Solve for n using amortization approximation or use financial calculator: approximate payoff months n\_old ≈ 58 months. Total paid old ≈ $450\times58 = $26{,}100. Interest old ≈ $26{,}100 - $15{,}000 = $11{,}100. Savings ≈ $26{,}100 - $19{,}500 = $6{,}600. Therefore consolidation reduces total payments substantially, from about $26,100 to $19,500, because of the APR drop from 21% to 11%.

hard

Hard: You have $20{,}000 mortgage at 5% APR with 10 years remaining and monthly payment $212. A refinance offer lowers APR to 3% but includes $1,200 closing costs. You plan to sell the house in 3 years. Should you refinance? Show break-even math for the 3-year horizon.

**Hint:** Compute remaining balance and total payments over 3 years for both current and refinanced loan, include closing costs, and compare totals.

Show solution

Current loan monthly r\_old = 0.05/12 = 0.0041667. Current payment P = $212 (given). Over 3 years (36 months) total paid\_old = $212\times36 = $7{,}632. Compute remaining principal after 36 months. Use amortization formula for remaining balance: B = L(1+r\_old)^{36} - P\times((1+r\_old)^{36}-1)/r\_old. Numeric computation yields remaining principal ≈ $20{,}000\times(1.0041667)^{36} - 212\times((1.0041667)^{36}-1)/0.0041667 ≈ $15{,}900 (approx). Total cost over 3 years equals payments $7,632 plus implied principal reduction $20,000 - $15,900 = $4,100; sum equals $11,732 but for comparison we look at cash outflow, which is $7,632.

Refinance: new APR 3% r\_new = 0.03/12 = 0.0025. If refinanced for remaining 10 years (120 months), new payment P\_new = r\_new L\_{new}/(1-(1+r\_new)^{-120}) where L\_{new}= $20,000 + $1,200 = $21,200. Compute P\_new ≈ 0.0025\times21,200/(1-(1.0025)^{-120}) ≈ $204. Over 36 months total paid\_new = $204\times36 = $7,344. Add closing costs already included in principal; cash outflow is $7,344 but the loan principal remaining after 36 months will be higher because of the financed closing costs. Remaining principal after 36 months is computed similarly and is roughly $17,600.

Compare cash paid over 36 months: current = $7,632; refinance = $7,344. Net cash savings = $288 over 36 months or $8/month. However, because the refinance keeps a higher remaining principal due to the $1,200 cost, net equity after sale could be about $1,700 lower than without refinancing. IF the borrower plans to sell in 3 years, THEN refinancing with $1,200 closing costs typically does not make sense unless monthly cashflow savings exceed the closing cost amortized over the holding period BECAUSE small monthly savings multiplied by a short holding period often do not repay the upfront fees. In this example the refinance gives only $288 savings over 3 years, so it likely is not worthwhile.

## Connections

Prerequisites used: Interest Rate Math (/money/interest-rate-math) for APR, monthly rate conversion, and amortization formulas; Credit Score (/money/credit-score) for utilization and score effects. Downstream topics unlocked by mastering consolidation: Loan Amortization and Repayment Strategies (/money/loan-amortization) because consolidation choices change amortization schedules; Mortgage and Auto Refinance Decisions (/money/mortgage-refinancing) because the cost vs horizon calculus is identical; Long-term Credit Planning (/money/credit-planning) since consolidation affects credit mix and utilization which feed into future borrowing costs.

**Disclaimer:** This content is for educational and informational purposes only and does not constitute financial, investment, tax, or legal advice. It is not a recommendation to buy, sell, or hold any security or financial product. You should consult a qualified financial advisor, tax professional, or attorney before making financial decisions. Past performance is not indicative of future results. The author is not a registered investment advisor, broker-dealer, or financial planner.

[← back to tree](/money/)[browse all →](/money/inventory/)
