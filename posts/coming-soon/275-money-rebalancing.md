---
title: Rebalancing
description: 'Portfolio drift from target allocation. Calendar vs threshold rebalancing. Tax-efficient methods: direct new contributions, rebalance in tax-advantaged accounts.'
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
inspiration_url: https://templeton.host/money/rebalancing/
inspiration_category: money
---

> Source-copy draft imported from [https://templeton.host/money/rebalancing/](https://templeton.host/money/rebalancing/). Names, domain references, and local media paths were adapted for Xavi Ablaza / getablaza.com.

[←Back to Personal Finance](/money/)

[inventory](/money/inventory/)[graph](/money/graph/)

Personal Finance

# Rebalancing

InvestingDifficulty: ★★★☆☆

Portfolio drift from target allocation. Calendar vs threshold rebalancing. Tax-efficient methods: direct new contributions, rebalance in tax-advantaged accounts.

## Interactive Visualization

⏮◀◀▶▶STEP0.25x1xZOOM

t=0s

## Prerequisites (1)

[Asset Allocationlvl 3](/money/asset-allocation/)

## Unlocks (1)

[Tax-Loss Harvestinglvl 4](/money/tax-loss-harvesting/)

A 60/40 portfolio can become a 75/25 portfolio after a single 2-year stock rally, increasing expected volatility by a material amount and changing your risk profile without you noticing.

TL;DR:

Rebalancing is the practice of returning a portfolio to its **target allocation** so risk stays aligned with goals; understanding it helps control volatility, manage taxes, and set rules that trade off cost, frequency, and tax impact.

## The Problem - What Goes Wrong When You Ignore Rebalancing

Portfolios drift. Small differences in returns compound into sizable allocation shifts. Imagine a $100,000 portfolio targeting **60% stocks / 40% bonds**. Stocks return 25% over 12 months and bonds return 5%. Stocks grow from $60,000 to $75,000. Bonds grow from $40,000 to $42,000. Total becomes $117,000 and the stock weight becomes $75,000 / $117,000 = 64.1% rather than 60. A 4.1 percentage point drift occurred in one year. Repeated year-after-year outperformance can produce a 10-15 percentage point drift over 3-5 years. That drift matters. A 60/40 portfolio typically exhibits historical annualized volatility near 7-10%. Moving to 70/30 can raise volatility to roughly 9-12% depending on correlations. Higher volatility increases short-term drawdowns. If your plan expects 3-6 months of expenses in a cash buffer and a 60/40 glide path, a shifted allocation may raise the chance of a 20-30% drawdown in a 1-3 year period. Worse, many investors react emotionally when the unexpected happens. Without rules, people tend to sell winners after gains and buy winners after losses - the opposite of systematic rebalancing. IF an investor lets allocations drift by more than 5-10 percentage points AND retirement date is within 5-10 years, THEN portfolio risk may materially exceed planned tolerance BECAUSE expected returns and volatility are functions of allocation. Another consequence is tax drag. Selling winners in a taxable account can crystallize capital gains taxes of 15-23% for long-term gains depending on income, which reduces the net benefit of a rebalance. Ignoring rebalancing creates invisible risk increases, behavioral pitfalls, and possible tax surprises. This section identifies the cost side of that trade-off with concrete numbers so later rules can compare costs and benefits.

## How It Actually Works - Mechanics, Formulas, and Real Numbers

Start with definitions. **Rebalancing** is the act of buying or selling assets so each asset class returns to its target weight. Two common methods exist: calendar rebalancing and threshold rebalancing. Calendar rebalancing trades on a fixed schedule - for example every 6 or 12 months. Threshold rebalancing trades whenever an asset class moves outside a band - for example plus-or-minus 3-7 percentage points from target. Key formulas. Current weight of asset i is wi=Vi/Vtotalw\_i = V\_i / V\_{total}wi​=Vi​/Vtotal​ where ViV\_iVi​ is the asset value and VtotalV\_{total}Vtotal​ is portfolio value. Amount to trade to reach target weight tit\_iti​ is Ti=ti⋅Vtotal−ViT\_i = t\_i \cdot V\_{total} - V\_iTi​=ti​⋅Vtotal​−Vi​. Example with numbers. Suppose target tstocks=0.60t\_{stocks}=0.60tstocks​=0.60 and $V\_{total} = $120,000 after returns. Current stocks $V\_{stocks} = $78,000. Then $T\_{stocks} = 0.60 \cdot 120,000 - 78,000 = $72,000 - $78,000 = -$6,000. Negative means sell $6,000 of stocks. Transaction cost and tax estimates matter. If trade commissions are $0-$10 per trade and bid-ask spreads are 0.01-0.10%, direct execution cost is roughly 0-0.1% of trade value. Realized capital gains on a $6,000 sale with a 20% tax rate impose a tax bill near $1,200 if gains equal full sale amount, though in practice only the realized gain portion is taxable. Turnover comparisons. A threshold rule of 5 percentage points typically triggers 5-15% annualized turnover depending on market volatility; a calendar annual rebalance can produce 10-25% turnover depending on how far allocations moved in that year. IF an investor wants lower realized gains in taxable accounts AND can tolerate some drift, THEN a wider threshold such as 7-10 percentage points may reduce taxable trades BECAUSE fewer triggers occur; however that increases allocation drift and therefore risk. Another practical mechanism is using $new contributions to buy the underweight asset class. For example, if monthly contributions equal $1,000 and current allocation is 65/35 while target is 60/40, directing new contributions of $1,000 per month entirely to bonds reduces drift without taxable sells. This method trades off speed of correction versus immediate tax payments and requires regular discipline. The formulas above plus examples give the arithmetic to compute trades, turnover, and a first-order estimate of tax impact.

## The Decision Framework - IF/THEN/BECAUSE Rules for Practical Choices

Problem-first: investors need rules that balance tax cost, transaction cost, behavioral control, and drift. Here is a compact decision tree you can apply to most portfolios. IF the account is tax-advantaged - for example a 401(k) or IRA - AND internal fund options let you trade without tax consequences, THEN prefer rebalancing inside those accounts BECAUSE trades do not realize capital gains and tax drag is avoided. IF the account is taxable AND expected realized capital gains exceed $5,000 in a trade (example threshold), THEN consider alternatives such as directing $new contributions to the underweight asset or rebalancing using tax-loss harvesting BECAUSE selling winners would create an immediate tax bill of roughly 15-23% on long-term gains. IF drift is less than 3-7 percentage points, AND transaction costs are $5-$50 per trade with spreads below 0.2%, THEN letting small drift persist may be acceptable because expected reduction in future realized gains may exceed the cost saved from immediate rebalancing. IF the investor requires strict risk control - for example a retiree within 0-5 years of planned withdrawals - AND target volatility must stay within +/-2 percentage points of plan, THEN rebalance more often such as quarterly or when drift hits +/-3 percentage points BECAUSE small allocation shifts materially change expected drawdowns in that horizon. Practical steps to implement. Step 1 - pick target bands: narrow bands like 1-3 percentage points keep allocations tight but raise turnover; wider bands like 5-10 percentage points reduce turnover but increase drift. Step 2 - assign accounts: use tax-advantaged accounts first for rebalancing trades; use taxable accounts only when tax-efficient methods are unavailable. Step 3 - use contributions and withdrawals: direct new contributions to underweight asset classes and make withdrawals from overweight classes where feasible to rebalance without selling in taxable accounts. Step 4 - quantify trade-offs: estimate expected tax on a sell using your marginal capital gains rate and compare to transaction costs plus the value of restored risk alignment; if tax cost is greater than expected benefit over a 2-5 year horizon, delaying rebalancing may be preferable. This framework makes trade-offs explicit so choices depend on numbers rather than vague instincts.

## Edge Cases and Limitations - When This Framework Breaks Down

What it does not handle well. First, concentrated or illiquid positions. If 40% of your portfolio is employer stock worth $200,000 and you target 60/40 across total assets, simple rebalancing math fails because selling large blocks can incur price impact or company-specific lockup penalties. IF a position is illiquid OR subject to trading restrictions, THEN rebalancing triggers additional costs beyond taxes BECAUSE price impact and regulatory limits can materially raise execution cost. Second, tax complexity beyond capital gains. The framework above assumes a flat long-term capital gains rate of 15-23% and ordinary income for short-term gains. It does not model state taxes (which can be 0-13% in some states), net investment income tax of 3.8% for high incomes, or wash sale rules that affect tax-loss harvesting. Third, behavioral timing and market regimes. Systematic rebalancing can underperform for prolonged trending markets. For example, selling winners during a 5-year bull market may reduce cumulative returns by 1-3 percentage points annualized versus a buy-and-hold approach in some scenarios. IF an investor believes a structural regime change will persist for 5-10 years, THEN rebalancing mechanically could reduce long-run return BECAUSE it forces buying assets that underperform the trend. Fourth, small accounts and micro-costs. For accounts under $5,000, proportional fixed costs such as $4 commission or $1 mutual fund trading fee can represent 0.1-0.5% of assets per trade, making frequent rebalancing uneconomic. Limitations summary. This lesson does not model individual tax brackets, state taxes, employer stock restrictions, or margin and options strategies. It also assumes liquid, widely traded ETFs or mutual funds with spreads under 0.2%. IF any of those conditions do not hold, THEN this framework requires modification BECAUSE taxes, illiquidity, or special rules materially change the maths and trade-offs.

## Worked Examples (3)

### Simple 60/40 Rebalance After One Year

Start with $100,000: $60,000 stocks and $40,000 bonds. After one year stocks return 20% and bonds return 4%. No taxes if inside a 401(k).

1. Compute new values: stocks $60,000  *1.20 = $72,000; bonds $40,000*  1.04 = $41,600; total = $113,600.
2. Compute current weights: stocks weight = $72,000 / $113,600 = 0.634 (63.4%); bonds weight = 36.6%.
3. Compute target dollar amounts for 60/40: target stocks = 0.60 \* 113,600 = $68,160; target bonds = $45,440.
4. Compute trade amounts: sell stocks $72,000 - $68,160 = $3,840 and buy bonds $45,440 - $41,600 = $3,840 (consistent).
5. Estimate transaction cost: if trading ETFs with 0.05% spread and zero commission, cost ~ $3,840 \* 0.0005 = $1.92. No tax inside 401(k).

**Insight:** Rebalancing in a tax-advantaged account restored the target risk profile at negligible transaction cost. Using the formula Ti=tiVtotal−ViT\_i = t\_i V\_{total} - V\_iTi​=ti​Vtotal​−Vi​ yields exact trade amounts.

### Taxable Account: Sell vs Add New Contributions

A taxable account has $200,000 with target 70% stocks / 30% bonds. Stocks have grown 40% over two years; bonds have grown 2%. Stocks initial was $140,000, now $196,000; bonds initial $60,000, now $61,200; total $257,200. Investor has $1,000 monthly new contributions.

1. Compute current weights: stocks = $196,000 / $257,200 = 76.2%; bonds = 23.8%. Drift = 6.2 percentage points.
2. Compute target dollar amounts: target stocks = 0.70 \* 257,200 = $180,040; target bonds = $77,160.
3. If selling to rebalance now, sell stocks of $196,000 - $180,040 = $15,960. If long-term gains tax rate is 15%, expected tax = $15,960 \* 0.15 = $2,394. Net proceeds after tax ~ $13,566 to buy bonds.
4. Alternative: direct $1,000 monthly contributions to bonds. Over 12 months that adds $12,000 to bonds, bringing bonds to $61,200 + $12,000 = $73,200 and total roughly $269,200. New stock weight ~ $196,000 / 269,200 = 72.8%. Drift reduced from 76.2% to 72.8% without realizing gains and without tax bill.
5. Compare outcomes: immediate rebalance costs $2,394 tax plus small transaction cost; contribution approach costs time and requires $12,000 over a year to achieve similar reduction of drift.

**Insight:** When tax cost of selling winners is higher than the value of immediate risk reduction, directing new contributions to the underweight asset can be a tax-efficient alternative, especially when contributions of $5,000-$20,000 per year are available.

### Multiple Account Rebalancing Using Tax-Advantaged Buckets

Total portfolio $200,000 split across a 401(k) $100,000, an IRA $50,000, and taxable $50,000. Target overall allocation is 60/40. Within accounts current allocations are: 401(k) 70/30, IRA 60/40, Taxable 50/50.

1. Compute total stocks: 401(k) stocks = $70,000; IRA stocks = $30,000; Taxable stocks = $25,000. Total stocks = $125,000. Total bonds = $75,000.
2. Target stocks dollar = 0.60 \* $200,000 = $120,000, so overall stocks overweight by $5,000.
3. IF trades inside 401(k) and IRA have no tax consequences, THEN rebalance inside those accounts first. For example, move $5,000 of stocks into bonds inside the 401(k) by selling mutual fund A and buying fund B, bringing 401(k) from 70/30 to roughly 65/35 internally.
4. Avoid selling taxable holdings if possible. Instead, direct future contributions to taxable bonds or make withdrawals from taxable stocks when needed. That keeps capital gains tax deferred.
5. Result: overall allocation returns to 60/40 with minimal tax impact by using internal tax-advantaged trades and external contributions.

**Insight:** Rebalancing across multiple account types is mostly a bookkeeping and routing exercise. Favor tax-advantaged accounts for trades that would otherwise trigger capital gains in taxable accounts.

## Key Takeaways

- ✓

  Rebalancing fixes invisible risk: a 5-15 percentage point drift can occur in 1-5 years and can raise portfolio volatility by 1-3 percentage points depending on asset mix.
- ✓

  Two main methods exist: calendar rebalancing (every 6-12 months) versus threshold rebalancing (bands of +/-3-7 percentage points); expect turnover roughly 5-25% annualized depending on choice.
- ✓

  IF the account is tax-advantaged AND trades are available, THEN prefer rebalancing inside those accounts BECAUSE it avoids capital gains taxes; quantify expected tax savings using your long-term rate of 15-23% as a baseline.
- ✓

  Direct new contributions to the underweight asset class when possible; for example $1,000 monthly contributions can substitute for selling $12,000 in a taxable account over a year.
- ✓

  Estimate trade-offs numerically before trading: compare expected tax bill (for example $2,000 on a $10,000 gain at 20%) to transaction costs and the value of restored risk control over a 2-5 year horizon.

## Common Mistakes

- ✗

  Ignoring tax impact when rebalancing taxable accounts. Why wrong: selling winners can trigger a 15-23% long-term capital gains tax plus state taxes of 0-13%, which can negate much of the rebalancing benefit.
- ✗

  Using overly tight bands like +/-1 percentage point for small portfolios under $10,000. Why wrong: fixed trading costs and spreads (0.01-0.5%) make frequent small trades economically inefficient and increase turnover.
- ✗

  Treating rebalancing as purely performance chasing. Why wrong: mechanical rebalancing is a risk-management tool. Selling winners during a long trend can reduce returns by 1-3 percentage points annualized; this trade-off is intentional for risk control.
- ✗

  Rebalancing across tax wrappers without accounting for rules. Why wrong: moving assets between a taxable account and an IRA or Roth by selling and repurchasing triggers taxes or prohibited exchanges; prefer internal rebalancing and contribution routing instead.

## Practice

easy

Easy: You have $50,000 split 60/40 (stocks/bonds). Stocks return 15% and bonds return 3% over 1 year. Compute new dollar values, new weights, and the dollar amount to trade to restore 60/40.

**Hint:** Use Vnew=Vold∗(1+return)V\_{new} = V\_{old} \* (1+return)Vnew​=Vold​∗(1+return). Then compute T=t⋅Vtotal−ViT = t \cdot V\_{total} - V\_iT=t⋅Vtotal​−Vi​.

Show solution

Stocks new = $30,000  *1.15 = $34,500. Bonds new = $20,000*  1.03 = $20,600. Total = $55,100. Stocks weight = 34,500 / 55,100 = 62.6%. Target stocks = 0.60 \* 55,100 = $33,060. Sell stocks $34,500 - $33,060 = $1,440 and buy bonds $1,440.

medium

Medium: You have $150,000 target 70/30 in a taxable account. Current split is 80/20 because stocks doubled from $60,000 to $120,000 while bonds remained $30,000. You can either sell $15,000 of stocks now or direct $3,000 monthly contributions to bonds. Assume 15% long-term capital gains tax rate. Compare tax cost now versus waiting 5 months of contributions.

**Hint:** Selling $15,000 triggers tax = realized gain portion \* 15%. Contributions of $3,000 per month reduce drift by $15,000 after 5 months without tax.

Show solution

If selling now, estimated tax = $15,000 \* 0.15 = $2,250. Net proceeds after tax = $12,750. Using contributions of $3,000 monthly for 5 months, total $15,000 added to bonds reduces drift without tax. Trade-off: immediate alignment vs paying $2,250 in tax. If near-term risk control value exceeds $2,250 for your horizon, selling may be preferred; otherwise contributions avoid the tax bill.

hard

Hard: Total portfolio $300,000 with three accounts: 401(k) $120,000 at 75/25, IRA $80,000 at 60/40, taxable $100,000 at 50/50. Target overall allocation is 60/40. Long-term capital gains tax is 15%. Design a rebalance that restores target with minimal tax. Show amounts to move inside tax-advantaged accounts and if any taxable sells are required.

**Hint:** Compute total stocks and bonds. Use internal trades in 401(k) and IRA first. Compute residual imbalance in the taxable account and consider directing new contributions or partial sales.

Show solution

Compute stocks: 401(k) stocks = 0.75*120,000 = $90,000. IRA stocks = 0.60*80,000 = $48,000. Taxable stocks = 0.50*100,000 = $50,000. Total stocks = $188,000. Total portfolio = $300,000. Target stocks = 0.60*  300,000 = $180,000. Overweight stocks by $8,000. Rebalance inside tax-advantaged accounts first: Move $8,000 of stocks into bonds across 401(k) and/or IRA by internal trades - for example sell $8,000 of stock fund in 401(k) bringing 401(k) stocks from $90,000 to $82,000 and bonds from $30,000 to $38,000. After internal rebalancing, overall stocks equal target and no taxable sells are required. Taxable account remains at 50/50 and requires no sales. This avoids capital gains taxes entirely.

## Connections

Prerequisites: This lesson builds on Asset Allocation (d3) - see /money/asset-allocation-d3 where we covered how stocks/bonds split drives 90%+ of portfolio variance and age-based glide paths. It also assumes familiarity with Target-date funds as a default option - see /money/target-date-funds for trade-offs between passive glide paths and manual rebalancing. Downstream concepts unlocked by mastering rebalancing include Tax-loss harvesting and timing - /money/tax-loss-harvesting which requires knowing when to deliberately realize losses while rebalancing, Withdrawal sequencing and tax-efficient retirement drawdown strategies - /money/withdrawal-strategies which rely on keeping allocations aligned across taxable and tax-advantaged accounts, and Glide-path customization for retirement risk control - /money/glide-paths where small allocation errors compound into materially different retirement outcomes.

**Disclaimer:** This content is for educational and informational purposes only and does not constitute financial, investment, tax, or legal advice. It is not a recommendation to buy, sell, or hold any security or financial product. You should consult a qualified financial advisor, tax professional, or attorney before making financial decisions. Past performance is not indicative of future results. The author is not a registered investment advisor, broker-dealer, or financial planner.

[← back to tree](/money/)[browse all →](/money/inventory/)
