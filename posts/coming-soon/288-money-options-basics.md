---
title: Options Basics
description: Calls, puts, strike price, expiration, premium. Covered calls for income, protective puts for insurance. Why 90% of retail options traders lose money.
date: '2026-07-01'
scheduled: '2027-04-14'
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
inspiration_url: https://templeton.host/money/options-basics/
inspiration_category: money
---

> Source-copy draft imported from [https://templeton.host/money/options-basics/](https://templeton.host/money/options-basics/). Names, domain references, and local media paths were adapted for Xavi Ablaza / getablaza.com.

[←Back to Personal Finance](/money/)

[inventory](/money/inventory/)[graph](/money/graph/)

Personal Finance

# Options Basics

InvestingDifficulty: ★★★★☆

Calls, puts, strike price, expiration, premium. Covered calls for income, protective puts for insurance. Why 90% of retail options traders lose money.

## Interactive Visualization

⏮◀◀▶▶STEP0.25x1xZOOM

t=0s

## Prerequisites (2)

[Asset Classeslvl 3](/money/asset-classes/)[Diversificationlvl 3](/money/diversification/)

## Referenced by Business (11)

Where this personal-finance concept shows up inside the operating-finance graph.

[SecurityBusiness

Options are derivative securities - contracts whose value derives from an underlying security. Understanding the base concept of a security is prerequisite to understanding derivatives built on top of them.](/business/security/)[Broker-DealerBusiness

Options trading requires broker-dealer accounts with tiered approval levels; suitability obligations and margin requirements are broker-dealer regulatory concepts that directly constrain which options strategies an individual can execute](/business/broker-dealer/)[Zero-sum GameBusiness

Options contracts are textbook zero-sum instruments - every dollar the option buyer profits, the option seller loses, making them the clearest personal-finance-scale example of zero-sum dynamics](/business/zero-sum-game/)[Risk-Adjusted ValueBusiness

Options pricing is risk-adjusted value at individual scale - the premium of a put or call literally prices the risk-adjusted value of a contingent payoff, and protective puts / covered calls reshape an asset's risk profile](/business/risk-adjusted-value/)[entry feeBusiness

An option premium is literally an entry fee - a nonzero payment for the right to participate in an allocation (exercise). If the option expires worthless (analogous to v=0), you still paid the premium. Individual-scale instance of the same mechanism design concept.](/business/entry-fee/)[SkewBusiness

Options payoffs are inherently skewed (capped premium loss, unbounded upside on calls). Implied volatility skew - the smile/smirk in option prices across strikes - is the market's real-time pricing of tail risk and asymmetry. Options are the primary instrument for expressing views on skew.](/business/skew/)[VolatilityBusiness

Options are literally priced on volatility (Black-Scholes vega). Implied vs realized volatility is the central concept in options valuation and strategy selection](/business/volatility/)[convexityBusiness

Options are the canonical convex instrument at individual scale - their payoff is convex in the underlying price (limited downside premium, unlimited upside). Understanding personal options builds intuition for why businesses seek convex payoff structures.](/business/convexity/)[trading ordersBusiness

Options orders are a concrete individual-scale example of high-dimensional parameterized trading actions - each order specifies strike price, expiration, quantity, and type (call/put), forming exactly the kind of continuous multi-parameter action space this concept describes](/business/trading-orders/)[optionsBusiness

Direct individual-scale mirror - same instruments (calls, puts, strike, expiration, premium) applied to personal portfolios rather than corporate treasury or deal structuring](/business/options/)[Option PricingBusiness

Option pricing is the mathematical machinery that determines the premiums, fair values, and Greeks for the calls and puts described in options-basics; understanding pricing transforms options from a gambling feel to a quantifiable risk-transfer instrument](/business/option-pricing/)

Many retail traders lose 80-90% of options trades despite buying upside with small capital. Losses often come from predictable time decay and illiquid pricing, not from bad stock calls.

TL;DR:

Options are contracts that give the right to buy or sell an asset at a set strike by expiration; mastering premiums, strikes, expiration, and basic strategies like covered calls and protective puts lets a portfolio trade income or insurance with quantifiable trade-offs.

## The Problem - What Goes Wrong When Options Are Misunderstood

Traders often treat options like cheap leverage and expect large returns from small investments. That expectation has consequences when 70-90% of retail options positions end in loss over typical 1-3 month horizons. A concrete dollar example shows why. Suppose a trader buys one call on Stock A at $100 with strike $105, expiration 30 days, paying a premium of $3 per share or $300 per contract. If the stock rises to $103 by expiration, the call expires worthless and the trader loses 100% of the $300 premium. By contrast, buying 100 shares at $100 costs $10,000 and a $3 rise yields a $300 gain or +3% return on capital. The option buyer lost $300 or -100% of the contract premium while the share buyer gained $300 or +3% of capital. This mismatch is common because options transfer time risk to buyers and pay that risk to sellers.

Bid-ask spreads and commissions create another predictable drain. With a quoted premium of $0.80 and a bid-ask spread of $0.50, execution cost can be 62% of the premium up front. For illiquid contracts with open interest under 10 contracts, spreads often exceed $0.75 on premiums below $2. That friction makes hitting break-even harder than simple payoff math suggests.

Sellers face different hazards. Selling naked puts or calls can expose traders to asymmetric losses. Example: selling one naked put at strike $90 for $2 premium on a $100 stock collects $200, yet a collapse to $40 yields an unrealized loss of $4,000 before assignment or margin events. Many retail accounts lack the margin cushion for a 40-60% move, and forced liquidation can lock in large losses.

Behavioral drivers add a final predictable element. Over 60% of retail traders buy options within 1-2 weeks of earnings or news when implied volatility typically spikes 20-100% higher than normal. If implied volatility falls post-event by 10-40%, premiums can collapse even when the stock moves in the favored direction. That means a 5-10% favorable move in the underlying can still produce a net loss of 30-100% of premium for the buyer.

IF a trader treats options as free leverage AND ignores time decay and liquidity, THEN losses of 50-100% of premium within 1-30 days are likely BECAUSE options lose extrinsic value as expiration approaches and markets price in short-term risk. The practical failure here is predictable and measurable: poor sizing, buying short-dated high-IV options, and neglecting spreads create a steep expected loss even before directional outcomes are considered.

## How It Actually Works - Mechanics, Payoffs, and Formulas

A precise model clarifies outcomes. Start with definitions. A **call** is the right to buy 100 shares at strike KbyexpirationK by expiration KbyexpirationT. A **put** is the right to sell 100 shares at strike KbyK by KbyT. The **premium** p is the price paid per share. **Strike** K and **expiration** T determine the binary payoff structure at expiry.

Payoffs at expiration for one option contract (100 shares) are formulaic. For a long call: payoff = max(S\_T - K, 0) - p. For a long put: payoff = max(K - S\_T, 0) - p. Break-even conditions follow directly. For a call buyer: S\_T must exceed K + p to break even. For a put buyer: S\_T must be below K - p to break even. Example numbers make this concrete. Buy call K = $105, p = $3, S\_T = $110 gives payoff = $5 - $3 = $2 per share or $200 per contract, a +66% return on the $300 premium if used as speculative capital.

Intrinsic and extrinsic value partition premium p. Intrinsic value = max(S\_0 - K, 0) for calls and = max(K - S\_0, 0) for puts at time 0. Extrinsic value equals p minus intrinsic value. Time value declines through **theta**, usually -$0.01 to -$5.00 per contract per day depending on premium and time to expiry. **Implied volatility** IV drives extrinsic value. IV ranges commonly from 15% to 60% for equities; a 10 percentage point rise in IV can increase p by 10-50% depending on strike and time.

Covered call and protective put illustrate two opposite trade-offs.

Covered call formula: hold 100 shares purchased at S\_0 and sell one call at strike K receiving premium p. Payoff at expiration = (S\_T - S\_0) for S\_T <= K plus (K - S\_0 + p) for S\_T > K. Example: S\_0 = $50, K = $55, p = $2 yields collected premium $200. If S\_T <= $55, investor keeps premium plus any share appreciation up to $55. Upside is capped at $55; maximum gain = ($55 - $50) + $2 = $7 per share or $700 per contract = 14% on $5,000 capital.

Protective put formula: hold 100 shares at S\_0 and buy one put at strike K paying p. Payoff at expiration = max(S\_T, K) - S\_0 - p. This creates a floor near K - p. Example: S\_0 = $80, K = $70, p = $1.50 creates a floor value of $68.50 per share, limiting downside to about $11.5 per share or -14.4% on $80 stock, at an insurance cost of $150 per contract.

IF one values limited upside for steady income AND owns 100+ shares, THEN selling covered calls may generate 0.5-3.0% monthly yield BECAUSE the seller collects premium upfront while assuming obligation to sell at strike K. IF avoiding large downside tail risk AND willing to pay insurance, THEN buying protective puts may cap loss to a known level BECAUSE the put transfers tail risk to put sellers in exchange for premium p.

## The Decision Framework - IF/THEN/BECAUSE Rules for Choosing Strategies

Start with the investment objective measured in numbers. Define income target as X% per month or insurance as a maximum tolerated loss of Y% over Z months. Example objectives: earn 1-2% monthly income on a stock position or limit a position drawdown to 10-15% over 3 months.

IF the primary goal is income of 0.5-3.0% per month AND the investor holds 100 shares per contract, THEN selling covered calls may match the objective BECAUSE selling options collects premium upfront and reduces small downside exposure by the amount of premium. Trade-off details matter numerically. For a $50 stock with 100 shares, selling a call that pays $2 premium generates $200 cash against $5,000 stock or 4.0% immediate yield. The upside is capped at (K - S\_0) + p, which might be 5-15% over the short term. This converts volatile upside into steady coupon like returns of 0.5-3% per month.

IF the primary goal is protecting a concentrated position and capital available is 100 shares per contract, THEN buying a protective put with strike K near expected worst-case S\_BE = K - p may be appropriate BECAUSE the put sets a numeric floor. For a $100 stock, buying a put at K = $90 costing p = $1.50 limits downside to about $8.50 per share or -8.5% from $100, at a cost of $150 per contract. Compare that cost to expected loss distribution: if one estimates a 5-15% chance of a loss greater than 15% over 6 months, and the put cost is 1-3% of position value, purchase may be rational.

IF trading purely for directional exposure with limited capital AND implied volatility is low relative to realized volatility estimates, THEN buying calls or puts may offer leverage BECAUSE options amplify delta exposure for a lower initial cash outlay. However expect theta decay of 0.5-5% of option value per day for short-dated options, so the timing edge must exceed decay.

Sizing constraints are practical and numeric. Minimum capital per option contract typically equals share price times 100. For a $50 stock that is $5,000 per contract. Position sizing rules often limit risk to 1-3% of portfolio per trade; on a $100,000 portfolio that equals $1,000 to $3,000 risk. Use stop-loss equivalents or predefined hedges to monetize that risk. IF margins or assigned positions threaten greater than 3-5% of portfolio, THEN reducing position size or using spreads may be preferable BECAUSE assignment or sudden moves can force outsized losses.

Spreads and combinations change the payoff math. Debit spreads lower maximum loss at the cost of capping maximum gain, typically reducing premium by 20-80% and lowering theta magnitude by similar percentages. Use numbers to choose strikes and expiration so that expected reward-to-cost ratios exceed hurdle rates of 2:1 or greater when speculating.

## Edge Cases and Limitations - Where This Framework Breaks Down

This framework omits at least two practical scenarios where outcomes deviate sharply from simple payoff math.

Scenario 1 - Overnight or gap risk. If a stock gaps from $100 to $60 overnight, a protective put with strike $70 and premium $1.50 may not prevent price slippage beyond modeled losses if the option is illiquid or the market shows wide spreads. For example, if bid-ask spreads widen to $3 overnight on low-liquidity puts, execution can cost double the quoted premium. IF a trader counts on perfect execution at quoted prices AND the security gaps overnight, THEN realized protection may be substantially worse than the theoretical floor BECAUSE liquidity can vanish and markets reprice between sessions.

Scenario 2 - Illiquid options and hidden costs. For options with open interest < 50 and average daily volume under 10 contracts, bid-ask spreads often exceed 10-30% of premium. A quoted premium of $0.80 with a $0.30 spread forces a 37.5% round-trip cost before directional moves. IF a strategy assumes low transaction cost AND trades small-premium strikes, THEN expected returns shrink by 20-60% due to spreads and commissions BECAUSE trading friction dominates small-premium strategies.

Other limitations include taxation and assignment. Option gains held under common account types may be short-term taxed at ordinary rates of 22-37% for gains, while long-term equity holds may be taxed at 0-20% depending on income. Assignment risk with American-style options near ex-dividend dates can force early exercise; for example, selling a call right before an expected $0.50 dividend can lead to early assignment if the call is deep in-the-money, changing realized outcomes by the dividend amount.

Model assumptions also break in extremes. Black-Scholes and similar models assume continuous trading, lognormal returns, and stable volatility; during IV spikes of 100-300% or liquidity crises, those models fail. IF market stress pushes IV from 30% to 150% in 1 day, THEN option pricing and hedge costs can diverge by multiples BECAUSE market makers widen quotes and hedging costs skyrocket.

This lesson therefore provides a measurable framework, not a guarantee. It does not account for tax-loss harvesting opportunities, account-level margin interactions across multiple positions, or broker-specific execution quality. For each trade, quantify liquidity metrics (open interest, spread as percentage of premium) and stress-test the position for a 20-60% move to judge suitability.

## Worked Examples (3)

### Covered Call on a $100 Stock to Generate Income

Hold 100 shares purchased at $100 per share. Sell 1 call with strike $110, expiration 30 days, premium $2.50 per share or $250 per contract.

1. Initial capital deployed: $10,000 for 100 shares. Premium received: $250, net cash outlay remains $10,000 but $250 is collected upfront.
2. If at expiration S\_T <= $110, the call expires worthless. Total return = (S\_T - $100) \* 100 + $250. If S\_T = $105, return = $500 + $250 = $750, or 7.5% over 30 days on $10,000 capital.
3. If at expiration S\_T > $110, shares are called away at $110. Proceeds = $11,000 + $250 premium = $11,250. Gross profit = $11,250 - $10,000 = $1,250 or 12.5% over 30 days. Upside capped at 12.5% in this example.
4. Annualized, 12.5% over 1 month implies ~150% per year, but rolling and tax effects reduce realized annualized gains; expect 6-36% annualized depending on churn and taxes.

**Insight:** Selling covered calls converts part of upside into immediate yield of 2.5% on capital in this example and caps upside. The strategy produces stable monthly income when the underlying is flat to modestly rising, but it sacrifices large upside beyond the strike.

### Protective Put as Insurance for a $80 Position

Hold 100 shares at S\_0 = $80. Buy 1 put with strike K = $70, expiration 3 months, premium p = $1.50 per share or $150 per contract.

1. Cost of insurance: $150, which equals 0.1875% of the $80 x 100 = $8,000 position value for 3 months.
2. If at expiration S\_T >= $70, the put expires worthless. Net position value = S\_T \* 100 - $150. If S\_T = $85, net value = $8,500 - $150 = $8,350, realized gain = $350 or +4.375% on $8,000.
3. If at expiration S\_T < $70, the put is exercised, effectively selling at $70. Net proceeds = $7,000 - $150 = $6,850. Worst-case loss relative to $8,000 initial = $1,150 or -14.375%. This is the effective floor.
4. Compare to no insurance: if S\_T = $50 without a put, position value = $5,000 and loss = $3,000 or -37.5%. The put reduced worst-case loss from -37.5% to -14.375% at a cost of $150.

**Insight:** Protective puts cap downside to a quantifiable floor at a known cost. The decision is numeric: if the expected probability-weighted loss without insurance exceeds $150 over 3 months, the put may have positive expected value for the holder.

### Buying a Short-Dated Call for Leverage

Buy 1 call on Stock B with current price S\_0 = $100, strike K = $105, expiration 14 days, premium p = $2.00 or $200 per contract.

1. Break-even at expiration requires S\_T = K + p = $105 + $2 = $107. If S\_T = $110, payoff = $5 - $2 = $3 per share or $300 per contract, which is +150% on the $200 premium.
2. If the stock moves to $103 at expiration, payoff = max(103 - 105, 0) - 2 = -2 per share or -$200, a -100% loss on premium.
3. Theta estimate for short-dated option might be -$5 to -$20 per day depending on IV; over 7 days theta could erode 35-70% of value if IV does not rise. If theta is -$10/day, one week costs $70 out of $200 premium, leaving $130 if other factors constant.
4. Implied volatility sensitivity: if IV drops by 5 percentage points and vega is $10 per point, premium falls by $50, increasing required S\_T for break-even.

**Insight:** Short-dated calls offer high percentage returns if the underlying rapidly moves favorably, but they are subject to rapid time decay and IV moves that commonly cause total premium loss within 7-30 days.

## Key Takeaways

- ✓

  A call payoff at expiration equals max(S\_T - K, 0) minus premium p; break-even for a call buyer is S\_T = K + p.
- ✓

  Covered calls can generate 0.5-3.0% monthly income on stock positions but cap upside equal to strike profit plus collected premium.
- ✓

  Protective puts create a floor near K - p; insurance cost is p, commonly 0.1-3.0% of position value per month depending on strike and IV.
- ✓

  Theta commonly erodes 0.5-5% of option value per day for short-dated contracts; factor time decay into expected returns and holding period.
- ✓

  Liquidity metrics matter: require open interest > 50 and spreads under 20% of premium for practical execution to avoid paying 20-60% in round-trip friction.

## Common Mistakes

- ✗

  Buying short-dated options before major events without pricing for implied volatility. Why wrong: IV often rises by 20-100% before events and then collapses 10-40% after, turning a favorable underlying move into a net loss because premiums fall.
- ✗

  Underestimating assignment and margin risk when selling naked options. Why wrong: a single 40% price drop can create losses multiples of premium collected, and forced margin calls can liquidate positions at bad prices.
- ✗

  Ignoring bid-ask spreads and open interest when trading small-premium contracts. Why wrong: with premiums under $2, spreads of $0.30-$0.75 can consume 15-60% of premium, making break-even much harder than textbook payoffs suggest.
- ✗

  Treating options as free leverage without sizing constraints. Why wrong: options expose capital to rapid time decay and tail events; risking more than 1-3% of portfolio on speculative options can produce ruinous losses.

## Practice

easy

Easy: You buy one call with strike K = $120, premium p = $4, on a stock currently at S\_0 = $115. What is the break-even stock price at expiration and payoff if S\_T = $130?

**Hint:** Break-even for a call is K + p. Payoff = max(S\_T - K, 0) - p.

Show solution

Break-even = K + p = $120 + $4 = $124. If S\_T = $130, payoff = (130 - 120) - 4 = $6 per share or $600 per contract.

medium

Medium: You own 200 shares at $40 each. Compare two choices for the next 3 months: A) sell 2 covered calls strike $45 premium $1.20 each; B) buy 2 protective puts strike $35 premium $0.80 each. Compute net P&L at expiration for S\_T = $50 and S\_T = $30, and state which choice protects against a large drop.

**Hint:** Covered call premium collected = 2  *100*  1.20. Put cost = 2  *100*  0.80. Compute outcomes for both stock levels.

Show solution

Initial position value = 200  *$40 = $8,000. Premium collected A = 200*  $1.20 = $240. Cost B = 200 \* $0.80 = $160.

If S\_T = $50: A) calls are exercised at $45: proceeds from sale = 200  *$45 = $9,000 plus premium $240 = $9,240. Profit = $9,240 - $8,000 = $1,240. B) puts expire worthless: value = 200*  $50 = $10,000 minus put cost $160 = $9,840. Profit = $9,840 - $8,000 = $1,840. So B outperforms at high upside by $600.

If S\_T = $30: A) calls expire worthless: value = 200  *$30 = $6,000 plus premium $240 = $6,240. Loss = $1,760 or -22% on $8,000. B) puts exercised at $35: proceeds = 200*  $35 = $7,000 minus put cost $160 = $6,840. Loss = $1,160 or -14.5% on $8,000. So B protects better against large drops.

Conclusion: Protective puts cost $160 to reduce a worst-case loss from -22% to -14.5% in this example.

hard

Hard: On a $200,000 diversified portfolio (60% equities / 40% bonds), an investor has a concentrated $40,000 position in a single stock. They wish to cap downside at 10% over 6 months for that stock. Protective puts at 6-month strike K = 90% of current price cost p = 2.5% of position value. Compute the insurance cost and the portfolio-level expected reduction in max drawdown if the stock falls 40% while the rest of the portfolio falls 10%. Show post-loss portfolio value with and without insurance.

**Hint:** Insurance cost = 2.5% of $40,000. Without insurance, drawdown equals stock loss plus portfolio other losses proportionally. With insurance, capped loss on that position is 10% plus cost.

Show solution

Position cost: $40,000. Insurance cost = 2.5% \* $40,000 = $1,000.

Scenario: stock falls 40% -> concentrated position declines to $24,000 without insurance (loss $16,000). The rest of portfolio (other $160,000) falls 10% -> declines to $144,000 (loss $16,000). Total portfolio without insurance = $24,000 + $144,000 = $168,000. Total loss = $32,000 or -16% on $200,000.

With insurance: capped loss on stock limited to 10% plus paid premium. Stock net after cap = $40,000 \* (1 - 0.10) = $36,000 minus premium $1,000 paid upfront gives effective stock value = $35,000. The rest still at $144,000. Portfolio with insurance = $35,000 + $144,000 = $179,000. Total loss = $21,000 or -10.5% on $200,000.

Conclusion: Paying $1,000 for puts reduces portfolio max drawdown from -16% to -10.5% in this stress scenario, an absolute improvement of 5.5 percentage points at a cost of 0.5% of portfolio value.

## Connections

This lesson builds on Asset Classes (/money/asset-classes) where stocks and bonds were compared by risk and return, and on Diversification (/money/diversification) where correlation and risk reduction through breadth were covered. Mastering Options Basics unlocks downstream topics including Options Strategies and Income Generation (/money/options-strategies) and Volatility, Greeks, and Risk Management (/money/volatility-and-greeks). Those downstream topics require understanding of strike, premium, expiration, and payoff math to model hedges, compute expected hedging costs, and size positions across a multi-asset portfolio.

**Disclaimer:** This content is for educational and informational purposes only and does not constitute financial, investment, tax, or legal advice. It is not a recommendation to buy, sell, or hold any security or financial product. You should consult a qualified financial advisor, tax professional, or attorney before making financial decisions. Past performance is not indicative of future results. The author is not a registered investment advisor, broker-dealer, or financial planner.

[← back to tree](/money/)[browse all →](/money/inventory/)
