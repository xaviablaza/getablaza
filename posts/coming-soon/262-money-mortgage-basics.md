---
title: Mortgage Math
description: Amortization, points, PMI, prepayment. 15 vs 30 year. ARM vs fixed. The largest debt most people carry and the math behind every payment.
date: '2026-07-01'
scheduled: '2027-03-19'
tags:
- p-and-l-engineering
- coming-soon
- money
layout: layouts/post.njk
templateEngineOverride: md
image: /img/xavi-linkedin-profile.jpg
draft: true
generated_by: templeton-deep-copy-import
source_format: html
inspiration_url: https://templeton.host/money/mortgage-basics/
inspiration_category: money
---

> Source-copy draft imported from [https://templeton.host/money/mortgage-basics/](https://templeton.host/money/mortgage-basics/). Names, domain references, and local media paths were adapted for Xavi Ablaza / getablaza.com.

[←Back to Personal Finance](/money/)

[inventory](/money/inventory/)[graph](/money/graph/)

Personal Finance

# Mortgage Math

DebtDifficulty: ★★★☆☆

Amortization, points, PMI, prepayment. 15 vs 30 year. ARM vs fixed. The largest debt most people carry and the math behind every payment.

## Interactive Visualization

⏮◀◀▶▶STEP0.25x1xZOOM

t=0s

## Prerequisites (2)

[Interest Rate Mathlvl 2](/money/interest-rate-math/)[Moderate-Interest Debtlvl 3](/money/moderate-debt-strategy/)

## Unlocks (1)

[Rent vs Buylvl 3](/money/rent-vs-buy/)

## Referenced by Business (6)

Where this personal-finance concept shows up inside the operating-finance graph.

[real estateBusiness

The debt instrument underlying RE at every scale - amortization, rate structures, and prepayment math are foundational](/business/real-estate/)[CollateralBusiness

A mortgage is the canonical collateral-backed loan at individual scale - the house itself secures the debt, PMI exists when collateral (down payment) is insufficient, and the entire amortization structure reflects the lender pricing risk against the pledged asset](/business/collateral/)[principal balanceBusiness

Individual-scale principal balance management on the largest liability most people carry - same amortization mechanics, prepayment decisions, and interest cost planning](/business/principal-balance/)[mortgage principalBusiness

Mortgage principal is the central input to amortization, PMI triggers, and prepayment decisions - all covered here at the individual homeowner scale](/business/mortgage-principal/)[home equityBusiness

Home equity is home value minus mortgage balance; amortization mechanics show how each payment shifts from interest to principal, building equity over time](/business/home-equity/)[amortized costsBusiness

Mortgage amortization is the personal-finance instance of amortized costs - spreading a large lump-sum (home purchase) into equal periodic payments over 15-30 years, same principle as spreading business costs over accounting periods](/business/amortized-costs/)

Most households carry their largest single debt through a mortgage, and small rate or term decisions can change total interest by tens of thousands of dollars.

TL;DR:

Mortgage Math explains how **mortgages**, **amortization**, **points**, **PMI**, **prepayment**, **ARMs**, and **fixed-rate mortgages** determine every payment and total cost, giving the ability to compare true costs across choices.

## The Problem - What Goes Wrong Without Mortgage Math

Many homebuyers focus on monthly payment size alone. That mistake hides how much interest accrues over decades. A $300,000 mortgage at 4% for 30 years yields a monthly payment of about $1,432 and total payments of $515,610, so total interest equals about $215,610. Small changes in rate or term can change that interest by tens or hundreds of thousands of dollars.

People often accept a lower monthly payment because it feels affordable. That trade-off pushes more of each early payment into interest and delays building equity. For example if the same $300,000 is financed for 15 years at 3.25%, the monthly payment rises to roughly $2,100 but total payments fall to about $378,000 and total interest to about $78,000. The difference in interest paid between the two options is roughly $137,000. That is real money lost to time and contract structure.

Another common blind spot is fees and small percentages. **Points** cost 1% of the loan per point up front. Buying 2 points on a $300,000 loan costs $6,000. **PMI** often costs 0.3% to 1.5% annually on the loan amount until equity reaches about 20%. For a $285,000 loan with PMI at 0.75% yearly, the charge is about $2,137 per year or $178 per month.

Adjustable-rate mortgages or **ARMs** create a different failure mode. A 3.0% ARM with a 2/2/5 cap structure may start cheap but can rise 3-5 percentage points over time, dramatically increasing monthly payments.

If borrowers fail to model amortization, points, PMI, prepayment, and rate volatility together, then monthly affordability, lifetime interest, and liquidity needs are misestimated. IF income is uncertain AND the borrower values payment stability, THEN a fixed-rate mortgage may reduce unexpected shortfalls BECAUSE payments do not change with market indexes. This description builds on the math in Interest Rate Math and Moderate-Interest Debt and shows how those concepts scale over decades.

## How It Actually Works - Mechanics and Formulas

Start with the standard annuity formula for a fully amortizing loan. For loan principal LLL, monthly interest rate rrr (annual rate divided by 12), and number of months nnn, the monthly payment MMM is:

M=Lr(1+r)n(1+r)n−1M = L \frac{r(1+r)^n}{(1+r)^n - 1}M=L(1+r)n−1r(1+r)n​

Example 1. A $300,000 loan at 4.00% annual interest means r=0.04/12=0.003333...r = 0.04/12 = 0.003333...r=0.04/12=0.003333... and n=360n = 360n=360. Plugging into the formula gives M≈1,432.25M \approx 1,432.25M≈1,432.25. Total paid over 30 years is $1,432.25 \times 360 \approx 515,610$, so total interest is about $215,610$.

How amortization works. Each monthly payment splits into interest and principal. Interest for month t equals outstanding balance at month t-1 times rrr. Principal payment equals M−M -M− interest. Early payments are mostly interest; later payments shift toward principal. For the $300,000$ 4% example, the first payment has roughly $1,000$ interest and $432$ principal. After 12 months the outstanding balance decreases by roughly $5,000$ to $6,000 depending on rounding, so cumulative interest paid in year one is about $11,900$ to $12,200$.

Points and their math. One **point** equals 1% of the loan amount paid at closing. Buying points lowers the mortgage rate according to the lender's schedule. Example: paying 2 points on $300,000 costs $6,000. If that reduces the rate from 4.00% to 3.50%, monthly payment falls from $1,432 to about $1,347, saving roughly $85 per month. Break even in months is $6,000 / 85 \approx 71 months, or about 5.9 years.

PMI calculations. **PMI** typically runs from 0.3% to 1.5% annually of the outstanding loan balance. For a $285,000 loan with 5% down on a $300,000 house and PMI at 0.75% annually, the PMI is $285,000 \times 0.0075 = $2,137.50 per year, or $178 per month. PMI usually ends when LTV hits 78% to 80% depending on contract and home value.

Prepayment math. Extra principal payments reduce the outstanding balance immediately. This accelerates the amortization schedule and reduces interest paid in future periods. One-off prepayment of $10,000 on the $300,000 4% loan directly reduces interest accrual because each future month’s interest multiplies a smaller balance. Roughly, this $10,000 prepayment saves about $10,000 \times total effective interest over remaining term ratio, often yielding several thousand dollars in interest savings. Exact savings require recomputing the amortization schedule with the lower balance.

ARMs versus fixed-rate mortgages. **ARM** mechanics combine an index plus a margin, an initial rate, and rate caps. A 5/1 ARM might have a 3.00% initial rate for five years, then adjust annually. Caps of 2/2/5 mean the rate cannot rise more than 2 points at first adjustment, 2 at subsequent adjustments, and 5 total over life. IF the borrower expects to move or refinance within the fixed initial period AND rate volatility is modest, THEN an ARM may lower near-term interest expense BECAUSE initial ARM rates often are 0.25% to 1.00% lower than comparable fixed rates. Conversely IF the borrower plans to stay long term AND values payment certainty, THEN a fixed-rate mortgage may lower the risk of large payment increases BECAUSE the rate remains constant for the loan term.

## The Decision Framework - IF/THEN/BECAUSE for Common Choices

Start with the central trade-off: lower monthly payment versus higher lifetime interest. Express decisions as IF/THEN/BECAUSE statements with concrete thresholds.

IF the expected real return from investing your money is in the range 5-7% AND your mortgage interest rate is in the range 3-5%, THEN investing extra cash may outperform prepaying principal over a long horizon BECAUSE investments may earn 2-4 percentage points more than your mortgage rate after inflation and taxes.

IF the expected real return is below 3% OR the borrower values guaranteed reduction of debt and reduced balance-sheet leverage, THEN prepaying principal may make sense BECAUSE prepayment yields a guaranteed effective return equal to the mortgage rate.

Choosing 15-year versus 30-year. IF monthly cash flow must be constrained to within 25% to 35% of gross monthly income, THEN a 30-year mortgage may be necessary BECAUSE its payment can be 30% to 50% lower than a comparable 15-year payment for the same loan amount. For example, on $300,000 a 30-year at 4.0% is about $1,432 per month while a 15-year at 3.25% is about $2,100 per month.

IF the borrower can afford the higher payment AND wants to minimize total interest paid, THEN a 15-year mortgage often reduces total interest by 50% or more BECAUSE the term cuts years of compounding and usually offers lower rates by 0.5 to 1.0 percentage points.

Buying points decisions. IF the borrower plans to hold the mortgage longer than the break-even period (commonly 4-8 years) AND can fund points with liquid cash, THEN buying points may lower lifetime cost BECAUSE the reduced monthly payment accumulates savings exceeding the upfront points cost after the break-even horizon.

PMI trade-offs. IF the borrower can raise the down payment from 5% to 20% without disrupting emergency savings of 3-6 months of expenses, THEN avoiding PMI may save $1,000 to $3,000 per year or more depending on loan size and PMI rate BECAUSE PMI directly increases annual cost until equity thresholds are met.

Refinancing. IF current market rates are at least 0.75% to 1.00% below your existing rate AND planned tenure in the house exceeds the break-even time for refinance costs, THEN refinancing may reduce total interest or monthly payments BECAUSE the lower rate reduces the numerator in the annuity payment formula and compounds over remaining term.

These rules build on Interest Rate Math and Moderate-Interest Debt by quantifying when guaranteed savings from prepayment or refinancing beat probabilistic investment gains.

## Edge Cases and Limitations - When This Framework Breaks Down

This framework omits several real-world complications. List of important limitations follows.

1) Income volatility and job risk. If household income could fall by 20% to 50% within a few years, then locking into a high monthly payment may increase default risk. IF income is uncertain AND liquidity is low, THEN prioritizing a lower monthly payment may reduce risk BECAUSE it preserves cash for emergencies. This guidance does not model unemployment insurance or social safety nets.

2) Local housing market volatility and negative equity risk. In declining markets, an early prepayment or extra principal does not guarantee avoidance of a loss on sale if home price drops 10-30%. The math above assumes stable or rising house prices and does not account for transaction costs such as 5-8% selling fees.

3) Taxes and policy changes. The mortgage interest deduction depends on tax brackets and itemization thresholds. The framework assumes no unexpected tax law changes. IF tax deductibility evaporates or changes significantly, THEN the after-tax effective mortgage rate can shift by 0.5 to 1.5 percentage points BECAUSE tax benefits alter the net cost of interest.

4) Lender-specific rules. Prepayment penalties, lender recast fees, or nonstandard PMI cancellation policies can materially alter outcomes. Some loans carry prepayment penalties equal to 1% to 3% of the prepaid amount for a limited period. This framework assumes no significant penalty unless explicitly stated.

5) Behavioral factors. The model treats guaranteed returns from prepayment as mathematically comparable to investment returns. It does not capture psychological value from lower debt balances or utility from cash liquidity.

6) Short holding periods. If the borrower plans to sell within 2-4 years, then upfront points rarely pay back and ARMs or lower-cost initial-rate structures can be preferable. This framework assumes medium to long holding periods unless otherwise specified.

In short, these rules work best for borrowers with stable income, typical transaction costs of 5-8%, and holding periods of at least 3-7 years. Cases outside those ranges require bespoke modeling because small shifts in assumptions can change recommended trade-offs.

## Worked Examples (3)

### Monthly Payment and Year-One Interest for a $300,000 30-Year at 4.00%

Loan amount $L = $300,000, annual rate = 4.00%, term = 30 years (n = 360 months).

1. Compute monthly rate $r = 0.04/12 = 0.003333333.
2. Apply the amortizing loan formula M=Lr(1+r)n(1+r)n−1M = L \frac{r(1+r)^n}{(1+r)^n - 1}M=L(1+r)n−1r(1+r)n​ and calculate $M \approx 300{,}000 \times \frac{0.0033333(1.0033333)^{360}}{(1.0033333)^{360}-1} \approx $1,432.25.
3. Compute first month interest = $300,000 \times 0.0033333 \approx $1,000$; first month principal = $1,432.25 - 1,000 = $432.25.
4. Estimate year-one interest by summing monthly interest approximations or using an amortization table; year-one interest is about $11,900 to $12,200 depending on rounding. Total paid over 30 years is $1,432.25 \times 360 \approx $515,610andtotalinterest and total interest andtotalinterest\approx $215,610.

**Insight:** This example shows how a modest monthly payment can hide large cumulative interest. Early payments mostly cover interest, so principal falls slowly in the first years.

### Compare 30-Year at 4.00% versus 15-Year at 3.25% for $300,000

Loan $300,000. Option A: 30 years at 4.00% (monthly $1,432 approx). Option B: 15 years at 3.25% (monthly about $2,100).

1. Option A monthly payment using formula is about $1,432.25; total payments $1,432.25 \times 360 \approx $515,610; total interest $\approx $215,610.
2. Option B monthly payment for 15 years at 3.25% is approximately $2,100; total payments $2,100 \times 180 \approx $378,000; total interest $\approx $78,000.
3. Compute interest difference: $215,610 - $78,000 \approx $137,610 saved by choosing the 15-year mortgage.
4. Compare cash flow: Option B increases monthly spending by about $668, which could be 30% to 50% higher depending on household income.

**Insight:** Paying for a shorter term yields large interest savings, but requires higher monthly cash flow. The trade-off is explicit: pay more now to save tens of thousands later.

### Buying Points: 2 Points on $300,000 to Lower Rate from 4.00% to 3.50%

Loan $300,000. Upfront points = 2% = $6,000. Rate without points 4.00% gives $M\_1 \approx $1,432.25. Rate with points 3.50% gives $M\_2 \approx $1,347.13.

1. Compute monthly savings = $1,432.25 - $1,347.13 = $85.12.
2. Compute break-even months = upfront cost / monthly savings = $6,000 / 85.12 \approx 70.5 months, or about 5.9 years.
3. If the borrower plans to keep the loan longer than about 6 years, the points-paid path reduces lifetime payments; if shorter, points likely increase lifetime cost due to the upfront expense.

**Insight:** Points convert up-front cash into a lower ongoing payment. The break-even horizon is critical and often sits in the 4-8 year range for common scenarios.

## Key Takeaways

- ✓

  Monthly payment masks lifetime cost: a $300,000 loan at 4.00% costs about $215,000 in interest over 30 years versus about $78,000 over 15 years on the same principal.
- ✓

  One point equals 1% of loan; buying points costs cash now to save money later, with typical break-even horizons of 4-8 years.
- ✓

  PMI typically costs 0.3% to 1.5% annually until equity reaches about 20%, often adding $100 to $300 per month on typical loans.
- ✓

  Extra principal payments immediately reduce future interest; a one-time $10,000 prepayment often saves several thousand dollars in interest depending on remaining term and rate.
- ✓

  ARMs can start 0.25% to 1.00% lower than fixed rates but carry adjustment risk; caps (for example 2/2/5) limit adjustments but do not eliminate them.

## Common Mistakes

- ✗

  Choosing lowest monthly payment without computing total interest. This ignores the $50,000 to $200,000 differences in interest across terms and rates.
- ✗

  Buying points without calculating break-even. People often pay 1% to 3% of loan in points and then move in 2-3 years, losing the upfront cash with no net savings.
- ✗

  Ignoring PMI costs when comparing mortgage offers. A loan with 5% down plus PMI can cost $1,000 to $3,000 more per year than a 20% down loan, depending on loan size and PMI rate.
- ✗

  Assuming ARMs remain cheap long term. Initial ARM rates can be 0.5% to 1.0% lower than fixed, but a 3% to 5% rate swing over time can raise payments beyond the initial savings.

## Practice

easy

Easy: Calculate the monthly payment for a $250,000 mortgage at 3.75% annual rate over 30 years. Show total paid and total interest.

**Hint:** Use the annuity formula M=Lr(1+r)n(1+r)n−1M = L \frac{r(1+r)^n}{(1+r)^n - 1}M=L(1+r)n−1r(1+r)n​ with r=0.0375/12r = 0.0375/12r=0.0375/12 and n=360n = 360n=360.

Show solution

Monthly rate r=0.0375/12=0.003125r = 0.0375/12 = 0.003125r=0.0375/12=0.003125. Using the formula gives $M \approx $1,157.79. Total paid over 360 months = $1,157.79 \times 360 \approx $416,804. Total interest = $416,804 - $250,000 \approx $166,804.

medium

Medium: Choose between a 30-year, $400,000 loan at 4.25% and a 15-year at 3.50%. Compute monthly payments and total interest. Then state which option lowers total interest and by how much.

**Hint:** Compute MMM for each case and total paid. For 30-year use n = 360, for 15-year use n = 180.

Show solution

30-year at 4.25%: r=0.0425/12=0.0035417r = 0.0425/12 = 0.0035417r=0.0425/12=0.0035417. Monthly $M\_{30} \approx $1,966. Total paid $1,966 \times 360 \approx $707,760. Total interest $\approx $307,760. 15-year at 3.50%: r=0.035/12=0.0029167r = 0.035/12 = 0.0029167r=0.035/12=0.0029167. Monthly $M\_{15} \approx $2,856. Total paid $2,856 \times 180 \approx $514,080. Total interest $\approx $114,080. Interest difference $\approx $193,680, so the 15-year option lowers total interest by about $193,680, though monthly payment increases by $890.

hard

Hard: You have a $350,000 loan at 4.50% fixed for 30 years. A lender offers a 3.75% rate if you pay 2 points now. Calculate the break-even time for paying 2 points. Include assumptions and compute months to break-even.

**Hint:** Compute monthly payments at 4.50% and at 3.75%. Upfront point cost is 2% of $350,000 = $7,000. Break-even months = upfront cost / monthly savings.

Show solution

Monthly rates: r1 = 0.045/12 = 0.00375; r2 = 0.0375/12 = 0.003125. Compute payments. At 4.50% for 30 years, $M\_1 \approx $1,773. At 3.75% for 30 years, $M\_2 \approx $1,620. Monthly savings = $1,773 - $1,620 = $153. Upfront cost = $7,000. Break-even months = $7,000 / 153 \approx 45.8 months, or about 3.8 years. Assumption: no refinance or sale within 3.8 years.

## Connections

This lesson builds directly on Interest Rate Math (/money/interest-rate-math) and Moderate-Interest Debt (/money/moderate-interest-debt). Understanding amortization formulas and the investment-versus-debt trade-offs in those prerequisites enables correct comparisons between prepaying principal, buying points, and investing excess cash. Mastery of this material unlocks practical topics like mortgage refinancing analysis (/money/refinancing), housing decision economics (/money/housing-capital), and portfolio allocation when carrying mortgage debt (/money/portfolio-with-debt).

**Disclaimer:** This content is for educational and informational purposes only and does not constitute financial, investment, tax, or legal advice. It is not a recommendation to buy, sell, or hold any security or financial product. You should consult a qualified financial advisor, tax professional, or attorney before making financial decisions. Past performance is not indicative of future results. The author is not a registered investment advisor, broker-dealer, or financial planner.

[← back to tree](/money/)[browse all →](/money/inventory/)
