---
title: Expected Value
description: Long-run average of a random variable. E[X] = sum of x*P(x).
date: '2026-07-01'
scheduled: '2026-06-10'
tags:
- p-and-l-engineering
- coming-soon
- tech-tree
layout: layouts/post.njk
templateEngineOverride: md
image: /img/xavi-linkedin-profile.jpg
draft: false
permalink: /tech-tree/expected-value/
---

[←Back to Tech Tree](/tech-tree/)

[inventory](/tech-tree/inventory/)[coverage](/tech-tree/coverage/)

# Expected Value

Probability & StatisticsDifficulty: ★★☆☆☆Depth: 3Unlocks: 74

Long-run average of a random variable. E[X] = sum of x\*P(x).

## Interactive Visualization

⏮◀◀▶▶STEP0.25x1xZOOM

t=0s

## Core Concepts

- -Expected value = the theoretical long-run average of a random variable (the value the sample mean approaches under repeated independent draws)
- -Definition as a probability-weighted average: for discrete X, E[X] = sum\_x x \* P(X = x); for continuous X, E[X] = integral x \* f\_X(x) dx
- -Existence criterion: the expectation is defined only if the weighted sum/integral converges (finite); otherwise E[X] may be infinite or undefined

## Key Symbols & Notation

E[X] (expectation operator on random variable X)

## Essential Relationships

- -Linearity: E[aX + b] = a \* E[X] + b for constants a,b

## Prerequisites (1)

[Random Variables6 atoms](/tech-tree/random-variables/)

## Unlocks (11)

[Variancelvl 2](/tech-tree/variance/)[Entropylvl 3](/tech-tree/entropy/)[Game Theory Introductionlvl 3](/tech-tree/game-theory-intro/)[Law of Large Numberslvl 3](/tech-tree/law-large-numbers/)[Stochastic Gradient Descentlvl 4](/tech-tree/sgd/)[Mechanism Designlvl 4](/tech-tree/mechanism-design/)[Bias-Variance Tradeofflvl 4](/tech-tree/bias-variance/)[Reinforcement Learning Introductionlvl 4](/tech-tree/rl-intro/)

+3 more...

## Referenced by (72)

Where this concept shows up in the operating-finance and personal-finance graphs.

### From Business (48)

[opportunity costBusiness

Quantifying opportunity cost requires comparing the expected values of competing alternatives - E[X\_chosen] vs E[X\_forgone] - making expected value the core mathematical operation behind every opportunity cost calculation](/business/opportunity-cost/)[Hiring TargetsBusiness

Consistently exceeding hiring targets requires pipeline math: expected\_hires = candidates × screen\_pass\_rate × interview\_pass\_rate × offer\_accept\_rate. Setting and beating targets is applied expected value over a recruiting funnel.](/business/hiring-targets/)[claimsBusiness

Pricing insurance to cover average claims is literally computing E[X] over the claims distribution - the premium must at least equal the expected payout per policy plus expenses](/business/claims/)[Pipeline VolumeBusiness

Weighted pipeline volume is literally expected value: sum of (deal\_value × close\_probability) across all opportunities](/business/pipeline-volume/)[personal financeBusiness

The moderate-interest debt gray zone (4-7% APR) is an expected value comparison: guaranteed return of debt payoff vs probabilistic ~7-10% market return](/business/personal-finance/)[risk-neutralBusiness

Risk-neutral agents maximize expected value directly - E[v\_i x\_i(b) - p\_i(b)] - with no adjustment for variance or higher moments. The equivalence between risk-neutrality and pure expected-value maximization is the core mathematical consequence.](/business/risk-neutral/)[Forced BorrowingBusiness

Quantifies why maintaining liquidity is rational: E[cost avoided] = P(liquidity crisis) × forced borrowing cost ($5K-$20K), making the buffer's value calculable as a probability-weighted savings](/business/forced-borrowing/)[rent-vs-buy decisionBusiness

Probabilistic version: if skiing days are drawn from a distribution, the optimal buy-timing minimizes E[total cost] = E[min(days,tau)]\*rent + I(days>=tau)\*B, a direct expected value calculation.](/business/rent-vs-buy-decision/)[insuranceBusiness

Insurance pricing IS expected value computation: premium = E[claims] + margin, so the core question 'how much to charge' reduces to estimating E[X] over the loss distribution](/business/insurance/)[Expected ReturnBusiness

Direct mathematical definition: E[X] = sum x\*P(x). Expected return IS expected value applied to project cash flows. You need this to state the concept precisely.](/business/expected-return/)[Guaranteed ReturnBusiness

A guaranteed 50-100% return is an expected value with zero variance, which formalizes why it dominates any probabilistic alternative - no risk-adjusted comparison can beat a certain payoff of that magnitude.](/business/guaranteed-return/)[Stock ReturnsBusiness

A stock return is literally the expected value of an operating outcome distribution - understanding E[X] = sum of x\*P(x) is the mathematical foundation for reasoning about what returns actually are and why they vary](/business/stock-returns/)[Expected PayoffBusiness

Expected payoff under mixed strategies is literally E[u\_i(s)] where s is drawn from the joint mixed strategy profile; the entire concept reduces to computing expected value of a random variable whose distribution is determined by players' mixing probabilities.](/business/expected-payoff/)[Contingent LiabilitiesBusiness

Provisioning for contingent liabilities requires computing expected loss = P(materializing) × potential obligation amount, the fundamental expected value calculation](/business/contingent-liabilities/)[Risk-Adjusted ValueBusiness

Risk-adjusted value is expected value penalized for uncertainty - the formula E[V] - λσ² starts from E[X] = Σ x·P(x) and subtracts a risk penalty, so expected value is the mathematical primitive being modified](/business/risk-adjusted-value/)[VarianceBusiness

Expected value is the quantity the business concept holds constant - understanding that E[X] alone is insufficient to characterize a distribution requires understanding both first and second moments together](/business/variance/)[AlphaBusiness

Alpha is formally E[R\_portfolio] - E[R\_benchmark]; understanding expected value as a weighted average over outcomes is the mathematical foundation for defining and measuring any 'spread' between your performance and a reference rate](/business/alpha/)[Expected Market ReturnBusiness

Expected market return is literally E[R] = sum of r\*P(r) over the distribution of possible market outcomes - the statistical expected value applied to return distributions](/business/expected-market-return/)[Capital AllocationBusiness

NPV - the CFO's primary capital allocation tool - is literally expected value of discounted future cash flows. Every automation investment decision reduces to E[returns] vs E[costs], weighted by probability of each outcome.](/business/capital-allocation/)[Capital BudgetingBusiness

NPV - the core tool of capital budgeting - is the expected present value of a project's uncertain future cash flows. Each period's cash flow is weighted by probability and discounted, making NPV a direct application of E[X] over a time-indexed random variable.](/business/capital-budgeting/)[investment decisionBusiness

Direct mathematical formalization: E[X] = sum of (payoff \* probability) is exactly the calculation implied by 'cost, probability of success, and a payoff'](/business/investment-decision/)[UnderwritingBusiness

ROI underwriting is fundamentally expected value calculation - probability-weighted outcomes across scenarios (base, upside, downside) to arrive at an investment decision](/business/underwriting/)[Off-Balance-Sheet RisksBusiness

Valuing a contingent liability requires computing E[cost] = P(trigger) × magnitude. A co-signed loan has expected cost = P(default) × $50K; a tax assessment with range $20K-$80K needs a probability-weighted value. Expected value is the mathematical primitive for converting uncertain off-balance-sheet items into comparable dollar figures.](/business/off-balance-sheet-risks/)[Co-SigningBusiness

The true cost of co-signing is E[loss] = P(default) × obligation\_amount; people systematically fail to compute this expected value for contingent liabilities, which is why $50K loans and $20-80K tax exposures catch co-signers off guard](/business/co-signing/)[Tax AssessmentsBusiness

Contingent tax liabilities are best modeled as expected values: P(triggered) × assessment\_amount. This is the correct framework for deciding how much to reserve against a liability that may or may not materialize](/business/tax-assessments/)[investment returnsBusiness

The 5-7% real return IS an expected value of a random variable - understanding E[X] as a probability-weighted long-run average is the mathematical concept that makes 'expected returns' a precise claim rather than a guess](/business/investment-returns/)[mortgage rateBusiness

The core comparison is guaranteed return (paydown saves 3-5% with certainty) vs E[X] of investment portfolio (5-7% expected but with variance) - understanding expected value formalizes when the spread justifies the risk](/business/mortgage-rate/)[Lifetime ValueBusiness

LTV is literally an expected value computation: E[revenue\_per\_period] times E[customer\_lifetime]. The LTV = ARPU / churn formula derives from summing a geometric series of retention probabilities, but the core concept is the long-run average value of the customer-lifetime random variable.](/business/lifetime-value/)[entry feeBusiness

The core math behind entry fees: a rational bidder participates iff E[payoff from mechanism] >= entry fee. A bidder with v=0 has E[value]=0, so any positive entry fee makes participation negative-EV, which is exactly why entry fees cause revenue to differ across mechanisms with identical allocations.](/business/entry-fee/)[Bid ShadingBusiness

The optimal bid shade maximizes E[(v - b) \* P(win|b)] - the tradeoff between surplus captured per win (v - b) and probability of winning, which is a direct expected value optimization](/business/bid-shading/)[Bet SizingBusiness

The yield function Y(x) computes E[return | invest x] - expected value is the mathematical core that makes the yield function calculable and bet sizing optimizable rather than intuitive](/business/bet-sizing/)[ROI underwritingBusiness

ROI underwriting is fundamentally expected value computation: probability-weighted cash flows across scenarios, discounted back to present value](/business/roi-underwriting/)[pre-tax vs post-taxBusiness

The Traditional vs Roth decision is an expected value comparison under uncertainty: E[tax cost] of paying known rate now vs E[tax cost] of paying unknown future rate, weighted by beliefs about future bracket placement](/business/pre-tax-vs-post-tax/)[RefinancingBusiness

Variable-rate refinancing options (ARMs, introductory teaser rates that reset) require expected value analysis across rate scenarios to compare against fixed-rate alternatives - the core question is whether E[total cost under variable] < total cost under fixed](/business/refinancing/)[Roth vs TraditionalBusiness

Stripped of dogma, the decision is: compare E[marginal\_rate\_at\_withdrawal] to marginal\_rate\_at\_contribution. You must estimate the expected value of a future tax rate under uncertainty (career trajectory, legislative risk, retirement income mix) - not memorize 'Roth is always better for young people.'](/business/roth-vs-traditional/)[high-interest debtBusiness

The decision to attack debt vs invest is an expected value comparison: E[debt payoff] = guaranteed APR return with zero variance vs E[market] ≈ 7-10% with substantial variance - the guaranteed return dominates when rates are comparable because it carries no risk](/business/high-interest-debt/)[Early Mortgage PrepaymentBusiness

The formal comparison: E[investing] is higher but uncertain, while prepayment is a guaranteed return equal to the mortgage rate - the decision hinges on whether you value expected value or certainty](/business/early-mortgage-prepayment/)[Expected Total CostBusiness

Expected total cost is literally an expected value calculation - E[Total Cost] = sum of cost\_i \* P(scenario\_i) across possible outcomes for each consolidation option](/business/expected-total-cost/)[index fundsBusiness

The core case for index funds is an expected value argument: active manager alpha is zero-sum before fees and negative-sum after fees, so the expected return of passive indexing exceeds the expected return of active management net of costs.](/business/index-funds/)[Emergency FundBusiness

The entire rationale for an emergency fund is an EV calculation: E[cost of no buffer] (penalty APR, late fees, new debt at high rates) exceeds the opportunity cost of idle cash](/business/emergency-fund/)[Hurdle RateBusiness

Expected return E[R] of the opportunity is compared against the hurdle rate threshold - the entire pricing decision reduces to whether E[R] exceeds the minimum acceptable return](/business/hurdle-rate/)[Future ValueBusiness

"Expected return" is E[X] applied to investment returns; future value under uncertainty requires computing the expectation over a return distribution rather than assuming a fixed rate](/business/future-value/)[Discounted Cash FlowBusiness

Real DCF operates on uncertain future cash flows - each CF\_t is a random variable, and the valuation is E[Σ CF\_t / (1+r)^t]. Probability-weighted scenarios are expected value calculations.](/business/discounted-cash-flow/)[Net Present ValueBusiness

NPV is the expected value of discounted future cash flows - E[CF\_t / (1+r)^t] summed over periods. Uncertain automation payoffs require computing expectations over probability-weighted outcomes.](/business/net-present-value/)[Portfolio AlphaBusiness

Alpha is literally defined as excess expected return over a benchmark. E[R\_portfolio] - E[R\_benchmark] = alpha. Cannot define, measure, or reason about portfolio alpha without expected value as the foundational concept.](/business/portfolio-alpha/)[NPVBusiness

NPV is a weighted sum of expected cash flows where weights are discount factors: NPV = sum of E[CF\_t] / (1+r)^t - understanding E[X] = sum x\*P(x) is the mathematical foundation for collapsing uncertain future payoffs into a single present value](/business/npv/)[Internal Rate of ReturnBusiness

NPV is structurally an expected value computation - sum of future cash flows weighted by discount factors, identical form to E[X] = sum of x\*P(x)](/business/internal-rate-of-return/)[LBO ModelingBusiness

LBO returns analysis computes probability-weighted IRR/MOIC across base, upside, and downside scenarios - the core of investment committee decision-making](/business/lbo-modeling/)

### From Money (24)

[Compound InterestMoney

Future value depends on expected return distributions](/money/compound-interest/)[Opportunity CostMoney

Opportunity cost is the expected value of the next-best alternative](/money/opportunity-cost/)[Employer 401k MatchMoney

100% match is a guaranteed return exceeding any expected market return](/money/employer-match/)[Debt ConsolidationMoney

Compare expected total cost across consolidation options](/money/debt-consolidation/)[Insurance BasicsMoney

Insurance pricing is an expected value calculation: premium vs probability times loss](/money/insurance-basics/)[Disability InsuranceMoney

Income replacement value is the discounted expected future earnings stream](/money/disability-insurance/)[Life InsuranceMoney

Coverage amount is the present value of expected remaining income stream](/money/life-insurance/)[Moderate-Interest DebtMoney

Compare guaranteed debt payoff return vs uncertain market expected return](/money/moderate-debt-strategy/)[Pre-Tax vs Post-TaxMoney

Traditional vs Roth is an expected value comparison under tax rate uncertainty](/money/pre-tax-vs-post-tax/)[Traditional vs Roth IRAMoney

Optimal wrapper depends on expected future vs current tax rate](/money/traditional-vs-roth-ira/)[15% Savings RateMoney

The target assumes expected real market returns of 5-7%](/money/target-savings-rate/)[529 Education SavingsMoney

Education cost growth vs investment growth is an expected value comparison](/money/529-education-savings/)[Asset ClassesMoney

Return is the expected value of the outcome distribution](/money/asset-classes/)[Dollar-Cost AveragingMoney

DCA vs lump sum is an expected value comparison - lump sum wins roughly 2/3 of the time](/money/dollar-cost-averaging/)[Rent vs BuyMoney

Break-even analysis compares expected total costs of renting vs owning](/money/rent-vs-buy/)[Rental Property MathMoney

NOI and cap rate are expected return calculations from the property cash flow distribution](/money/rental-property-math/)[Return on EquityMoney

Redeployment decisions compare expected returns across different uses of capital](/money/return-on-equity/)[Real Estate LeverageMoney

Leveraged returns amplify both expected gains and expected losses](/money/real-estate-leverage/)[Roth Conversion LadderMoney

Optimal conversion amount depends on expected future tax rates](/money/roth-conversion-ladder/)[Large Purchase PlanningMoney

Time horizon determines which vehicle maximizes expected risk-adjusted value](/money/large-purchase-planning/)[FIRE MathMoney

Safe withdrawal rate depends on expected real portfolio returns](/money/fire-math/)[Career as AssetMoney

Career decisions are expected value calculations on human capital](/money/career-as-asset/)[Options BasicsMoney

Option premium equals the risk-neutral expected payoff](/money/options-basics/)[Alternative InvestmentsMoney

Illiquidity premium compensates for uncertain exit timing and higher variance](/money/alternative-investments/)

Advanced Learning Details

### Graph Position

29

Depth Cost

74

Fan-Out (ROI)

29

Bottleneck Score

3

Chain Length

### Cognitive Load

5

Atomic Elements

13

Total Elements

L0

Percentile Level

L3

Atomic Level

### All Concepts (5)

- - Expected value: a single-number summary of a random variable representing its long-run average outcome
- - Expectation defined for discrete random variables as a probability-weighted average of possible outcomes
- - Interpretation of expectation as the average result one would observe over many repeated independent trials (long-run frequency interpretation)
- - Existence/finition condition: the expectation is meaningful only when the defining sum converges to a finite value
- - Support-based summation: the expectation is computed by summing only over the random variable's possible values (its support)

### Teaching Strategy

Self-serve tutorial - low prerequisites, straightforward concepts.

If you repeatedly play a lottery, flip a biased coin for points, or measure noisy sensor readings, you eventually want one number that summarizes what you “typically” get. Expected value is that number: the long-run average you should plan around, even though any single outcome can differ.

TL;DR:

The expected value (expectation) E[X] of a random variable X is its probability-weighted average. Discrete: E[X] = ∑ₓ x·P(X=x). Continuous: E[X] = ∫ x f\_X(x) dx. Expectation is linear (E[aX+b]=aE[X]+b) and generalizes to E[g(X)]. It may be infinite or undefined if the weighted sum/integral doesn’t converge.

## What Is Expected Value?

### Why we need it (motivation)

A random variable X can take many values depending on chance. If you want to:

- •compare two gambling games,
- •decide whether an insurance policy is “fair,”
- •estimate average runtime of a randomized algorithm,
- •or reason about average loss in machine learning,

you need a single summary number.

Expected value is the *theoretical long-run average*: if you repeatedly draw independent samples X₁, X₂, … from the same distribution, the sample mean

Xˉn=1n∑i=1nXi\bar X\_n = \frac{1}{n}\sum\_{i=1}^n X\_iXˉn​=n1​i=1∑n​Xi​

tends to get close to a fixed value. That fixed value (when it exists) is E[X]. (A later node formalizes this as the Law of Large Numbers.)

### Intuition first: “average with weights”

Suppose outcomes x happen with probabilities p(x). An ordinary average gives each outcome equal weight. Expected value gives outcome x the weight p(x).

So if big outcomes are rare, they still matter—but only proportionally to how often they occur.

### Definition (discrete)

If X is discrete with possible values x and probability mass function P(X = x), the expectation is

E[X]=∑xx P(X=x).\mathbb{E}[X] = \sum\_x x\,\mathbb{P}(X=x).E[X]=x∑​xP(X=x).

You can read this as “sum over all outcomes: (value) × (chance of that value).”

### Definition (continuous)

If X is continuous with probability density function f\_X(x), then

E[X]=∫−∞∞x fX(x) dx.\mathbb{E}[X] = \int\_{-\infty}^{\infty} x\, f\_X(x)\, dx.E[X]=∫−∞∞​xfX​(x)dx.

This is the same idea: infinitely many possible values, so the weighted average becomes an integral.

### Units and interpretation

- •E[X] has the *same units* as X. If X is dollars, E[X] is dollars.
- •E[X] is not necessarily a value X can actually take (e.g., the average of 0 and 1 is 0.5).

### Difficulty calibration note

We’ll treat the following as **core** vs **optional/advanced**:

- •**Core:** compute E[X] for discrete/continuous distributions; linearity; interpretation.
- •**Optional/Advanced:** existence/undefined expectations; heavy tails; expectation of functions E[g(X)].

You can learn and apply expected value well with the core, then come back for the optional parts when you need them.

## Core Mechanic 1: Computing E[X] as a Probability-Weighted Average

### Discrete examples: build the pattern

For a discrete X, you need two things:

1) the set of possible values {x}, and

2) the probability of each value p(x).

Then compute the weighted sum ∑ x p(x).

#### Example pattern: dice

Let X be the value of a fair six-sided die. Then P(X=k)=1/6 for k∈{1,2,3,4,5,6}.

E[X]=∑k=16k⋅16=16(1+2+3+4+5+6)=3.5.\mathbb{E}[X] = \sum\_{k=1}^6 k\cdot \frac{1}{6} = \frac{1}{6}(1+2+3+4+5+6)=3.5.E[X]=k=1∑6​k⋅61​=61​(1+2+3+4+5+6)=3.5.

Notice 3.5 is not an outcome on the die—expected value is a *planning* number, not a predicted single roll.

### Continuous examples: computing E[X] with integrals

For continuous X, the density f\_X(x) plays the role of “probability per unit x.” The integral

∫xfX(x)dx\int x f\_X(x) dx∫xfX​(x)dx

is the continuous weighted average.

#### Example pattern: Uniform(0,1)

If X ∼ Uniform(0,1), then f\_X(x)=1 for x∈[0,1] and 0 otherwise.

E[X]=∫01x⋅1 dx=[x22]01=12.\mathbb{E}[X]=\int\_0^1 x\cdot 1\, dx = \left[\frac{x^2}{2}\right]\_0^1 = \frac{1}{2}.E[X]=∫01​x⋅1dx=[2x2​]01​=21​.

### Expectation as “center of mass” (intuition)

A useful physical analogy: imagine each value x has “mass” p(x) (discrete) or density f(x)dx (continuous). The expected value is the balance point.

- •If probability mass shifts right, E[X] increases.
- •If you add a rare but huge outcome, E[X] can jump noticeably.

### Sanity checks when computing

1) **Range check:** If X is always between a and b, then E[X] must lie between a and b.

2) **Symmetry:** If a distribution is symmetric around 0, often E[X]=0 (when it exists).

3) **Weights sum to 1:** For discrete, verify ∑ p(x)=1; for continuous, ∫ f(x)dx=1.

### Core takeaway

Computing expectation is usually straightforward bookkeeping—until you meet distributions with extremely large values or tails. That’s where the next sections add nuance.

## Core Mechanic 2: Linearity of Expectation (the "superpower")

### Why linearity matters

Many random variables are built from simpler pieces:

- •total reward = sum of per-step rewards,
- •total cost = sum of random costs,
- •total heads = sum of indicator variables,
- •ML loss over a dataset = average of per-example losses.

Computing the full distribution of a sum can be hard. Expected value often stays easy because expectation is *linear*.

### Linearity rules (core)

For random variables X and Y (no independence required):

E[X+Y]=E[X]+E[Y].\mathbb{E}[X+Y] = \mathbb{E}[X] + \mathbb{E}[Y].E[X+Y]=E[X]+E[Y].

For constants a, b:

E[aX+b]=a E[X]+b.\mathbb{E}[aX+b] = a\,\mathbb{E}[X] + b.E[aX+b]=aE[X]+b.

More generally, for any finite sum:

E[∑i=1nXi]=∑i=1nE[Xi].\mathbb{E}\Big[\sum\_{i=1}^n X\_i\Big] = \sum\_{i=1}^n \mathbb{E}[X\_i].E[i=1∑n​Xi​]=i=1∑n​E[Xi​].

### Mini-derivation (discrete)

Assume (X,Y) are discrete.

Start with the definition:

E[X+Y]=∑x,y(x+y) P(X=x,Y=y).\mathbb{E}[X+Y] = \sum\_{x,y} (x+y)\,\mathbb{P}(X=x, Y=y).E[X+Y]=x,y∑​(x+y)P(X=x,Y=y).

Split the sum:

E[X+Y]=∑x,yx P(X=x,Y=y)+∑x,yy P(X=x,Y=y).\mathbb{E}[X+Y] = \sum\_{x,y} x\,\mathbb{P}(X=x, Y=y) + \sum\_{x,y} y\,\mathbb{P}(X=x, Y=y).E[X+Y]=x,y∑​xP(X=x,Y=y)+x,y∑​yP(X=x,Y=y).

Now notice:

∑yP(X=x,Y=y)=P(X=x)\sum\_{y} \mathbb{P}(X=x, Y=y) = \mathbb{P}(X=x)y∑​P(X=x,Y=y)=P(X=x)

so

∑x,yx P(X=x,Y=y)=∑xx P(X=x)=E[X].\sum\_{x,y} x\,\mathbb{P}(X=x, Y=y) = \sum\_x x\,\mathbb{P}(X=x) = \mathbb{E}[X].x,y∑​xP(X=x,Y=y)=x∑​xP(X=x)=E[X].

Similarly the second term becomes E[Y]. Therefore E[X+Y]=E[X]+E[Y].

### Indicators: a common trick

Define an indicator random variable I for an event A:

- •I = 1 if A happens
- •I = 0 otherwise

Then

E[I]=1⋅P(A)+0⋅(1−P(A))=P(A).\mathbb{E}[I] = 1\cdot \mathbb{P}(A) + 0\cdot (1-\mathbb{P}(A)) = \mathbb{P}(A).E[I]=1⋅P(A)+0⋅(1−P(A))=P(A).

This turns probability questions into expectation questions.

Example: Let X be the number of heads in n coin flips (not necessarily fair). Let Iᵢ indicate “flip i is heads.” Then X = ∑ᵢ Iᵢ, so

E[X]=∑i=1nE[Ii]=∑i=1nP(heads on i).\mathbb{E}[X] = \sum\_{i=1}^n \mathbb{E}[I\_i] = \sum\_{i=1}^n \mathbb{P}(\text{heads on } i).E[X]=i=1∑n​E[Ii​]=i=1∑n​P(heads on i).

If the coin has P(heads)=p each time, then E[X]=np.

### What linearity does *not* say

A classic confusion is to assume expectation distributes over products:

- •Generally, **E[XY] ≠ E[X]E[Y]**.

That equality holds under independence (and some integrability conditions), but linearity alone doesn’t give it.

## Optional/Advanced: Expectation of Functions E[g(X)] and Existence Issues

### E[g(X)] (operator viewpoint)

Expected value is not just a number attached to X—it’s an *operator* that maps a random variable to a number.

Often we care about a transformed quantity g(X):

- •squared error: g(X) = (X−c)²
- •absolute deviation: g(X)=|X|
- •utility in economics: g(X)=u(X)
- •loss in ML: g(X)=ℓ(X, y)

#### Definition (discrete)

E[g(X)]=∑xg(x) P(X=x).\mathbb{E}[g(X)] = \sum\_x g(x)\,\mathbb{P}(X=x).E[g(X)]=x∑​g(x)P(X=x).

#### Definition (continuous)

E[g(X)]=∫−∞∞g(x) fX(x) dx.\mathbb{E}[g(X)] = \int\_{-\infty}^{\infty} g(x)\, f\_X(x)\, dx.E[g(X)]=∫−∞∞​g(x)fX​(x)dx.

This is the same weighted-average idea, just applied after transforming the outcomes.

### Law of the unconscious statistician (LOUTS)

A subtle but powerful point: to compute E[g(X)], you usually **do not** need the distribution of Y=g(X). You can compute directly from X’s distribution using the formulas above.

### When expectation does not exist (or is infinite)

So far, we’ve treated expectation as always producing a finite number. But expectation is only well-defined when the weighted sum/integral *converges*.

A practical sufficient condition is that the absolute expectation is finite:

- •Discrete: $∑x∣x∣ P(X=x)<∞\sum\_x |x|\,\mathbb{P}(X=x) < \infty∑x​∣x∣P(X=x)<∞$
- •Continuous: $∫−∞∞∣x∣ fX(x) dx<∞\int\_{-\infty}^{\infty} |x|\, f\_X(x)\, dx < \infty∫−∞∞​∣x∣fX​(x)dx<∞$

If these diverge, several things can happen:

| Situation | What it means | Typical phrase |
| --- | --- | --- |
| E[X] is a finite real number | weighted average converges | “expectation exists” |
| E[X] = +∞ or −∞ | one-sided integral/sum diverges | “infinite expectation” |
| undefined | positive and negative parts both diverge | “does not exist” |

#### Heavy tails (intuition)

A heavy-tailed distribution puts enough probability on huge values that the “average” never settles.

A famous example is the Cauchy distribution: it’s symmetric, but its tails are so heavy that E[X] is undefined (the integral does not converge in the required sense). That’s why sample means of Cauchy draws behave wildly even for large n.

### Why this matters in practice

- •In modeling, assuming E[X] exists lets you use many theorems (LLN, variance formulas, etc.).
- •In risk/finance, rare catastrophic outcomes can dominate expectation.
- •In ML, expectation of loss is usually well-defined, but certain data distributions (extreme outliers) can make empirical averages unstable.

If you’re learning expectation for the first time, don’t let this scare you: most standard distributions used early (Bernoulli, Binomial, Uniform, Normal, Exponential) have finite expectations. But it’s important to know that “average” is not guaranteed by definition—it’s a property that may or may not hold.

## Applications and Connections: From Fair Games to SGD

### Fairness and pricing (games, insurance)

A gamble is often called “fair” if its expected payoff is 0 (or if the price equals expected payout).

If you pay cost c to play and receive random payout X, then net payoff is X−c. By linearity:

E[X−c]=E[X]−c.\mathbb{E}[X-c] = \mathbb{E}[X] - c.E[X−c]=E[X]−c.

A fair price is c = E[X] (ignoring risk preferences).

### Expected loss (machine learning viewpoint)

In supervised learning, we often minimize **expected risk**:

R(θ)=E(x,y)∼D [ℓ(θ;x,y)].R(\theta) = \mathbb{E}\_{(x,y)\sim \mathcal{D}}\,[\ell(\theta; x,y)].R(θ)=E(x,y)∼D​[ℓ(θ;x,y)].

We don’t know the true distribution 𝒟, so we approximate R(θ) with the empirical average over data:

R^(θ)=1n∑i=1nℓ(θ;xi,yi).\hat R(\theta) = \frac{1}{n}\sum\_{i=1}^n \ell(\theta; x\_i, y\_i).R^(θ)=n1​i=1∑n​ℓ(θ;xi​,yi​).

The idea “sample average ≈ expected value” is exactly the intuition behind expected value and what the Law of Large Numbers formalizes.

### Why SGD works with expectation

Stochastic Gradient Descent uses a random mini-batch to estimate the gradient of expected loss.

If g(θ) is the gradient computed from a random sample, SGD relies on it being (approximately) **unbiased**:

E[g(θ)]=∇R(θ).\mathbb{E}[g(\theta)] = \nabla R(\theta).E[g(θ)]=∇R(θ).

This is an expectation statement: on average, the noisy gradient points in the true direction.

### Connecting expectation to what comes next

- •**Variance** measures spread around the mean μ = E[X] using E[(X−μ)²].
- •**Entropy** uses an expectation too: H(X)=E[−log p(X)] (discrete).
- •**Law of Large Numbers** explains the long-run convergence of sample means to E[X].
- •**Game theory** uses expected payoff when players randomize strategies.

Expected value is the first “global” summary of a distribution you should reach for: it’s simple, composable via linearity, and it’s the backbone of many later definitions.

## Worked Examples (3)

### Compute E[X] for a simple discrete gamble

A game pays $10 with probability 0.2, pays $2 with probability 0.5, and pays $0 with probability 0.3. Let X be the payout in dollars. Find E[X] and a fair entry price c (ignoring risk).

1. List outcomes and probabilities:

   - •x=10 with p=0.2
   - •x=2 with p=0.5
   - •x=0 with p=0.3
2. Apply the discrete expectation formula:

   E[X]=∑xx P(X=x)=10(0.2)+2(0.5)+0(0.3).\mathbb{E}[X]=\sum\_x x\,\mathbb{P}(X=x)=10(0.2)+2(0.5)+0(0.3).E[X]=x∑​xP(X=x)=10(0.2)+2(0.5)+0(0.3).
3. Compute:

   10(0.2)=2

   2(0.5)=1

   0(0.3)=0

   So

   E[X]=2+1+0=3.\mathbb{E}[X]=2+1+0=3.E[X]=2+1+0=3.
4. A fair entry price c makes expected net payoff zero:

   Net payoff = X − c

   E[X−c]=E[X]−c=0⇒c=E[X]=3.\mathbb{E}[X-c]=\mathbb{E}[X]-c=0 \Rightarrow c=\mathbb{E}[X]=3.E[X−c]=E[X]−c=0⇒c=E[X]=3.

**Insight:** Expected value treats each payout as contributing “value × frequency.” Even though $10 is large, it happens only 20% of the time, so it contributes $2 to the average.

### Use linearity with indicator variables: expected number of successes

You run 5 independent trials. Trial i succeeds with probability pᵢ (not necessarily the same across trials). Let X be the total number of successes. Compute E[X].

1. Define indicator variables:

   Let Iᵢ = 1 if trial i succeeds, else 0.

   Then the total number of successes is

   X=∑i=15Ii.X = \sum\_{i=1}^5 I\_i.X=i=1∑5​Ii​.
2. Compute each indicator’s expectation:

   E[Ii]=1⋅pi+0⋅(1−pi)=pi.\mathbb{E}[I\_i] = 1\cdot p\_i + 0\cdot (1-p\_i)=p\_i.E[Ii​]=1⋅pi​+0⋅(1−pi​)=pi​.
3. Apply linearity of expectation (no extra assumptions needed beyond finiteness):

   E[X]=E[∑i=15Ii]=∑i=15E[Ii]=∑i=15pi.\mathbb{E}[X] = \mathbb{E}\left[\sum\_{i=1}^5 I\_i\right] = \sum\_{i=1}^5 \mathbb{E}[I\_i] = \sum\_{i=1}^5 p\_i.E[X]=E[i=1∑5​Ii​]=i=1∑5​E[Ii​]=i=1∑5​pi​.

**Insight:** Linearity lets you avoid computing the distribution of X. Even if the trials have different probabilities, the expected total is just the sum of the individual success probabilities.

### Continuous expectation: E[X] for an exponential distribution

Let X have an exponential distribution with rate λ>0, meaning f\_X(x)=λe^{−λx} for x≥0 and 0 otherwise. Compute E[X].

1. Start from the definition:

   E[X]=∫−∞∞xfX(x) dx=∫0∞x λe−λx dx.\mathbb{E}[X] = \int\_{-\infty}^{\infty} x f\_X(x)\,dx = \int\_0^{\infty} x\, \lambda e^{-\lambda x}\,dx.E[X]=∫−∞∞​xfX​(x)dx=∫0∞​xλe−λxdx.
2. Compute the integral using integration by parts.

   Let u = x so du = dx.

   Let dv = \lambda e^{-\lambda x} dx so v = -e^{-\lambda x}.

   Then

   ∫0∞x λe−λxdx=[x(−e−λx)]0∞−∫0∞(−e−λx) dx.\int\_0^{\infty} x\, \lambda e^{-\lambda x} dx = \left[x(-e^{-\lambda x})\right]\_0^{\infty} - \int\_0^{\infty} (-e^{-\lambda x})\,dx.∫0∞​xλe−λxdx=[x(−e−λx)]0∞​−∫0∞​(−e−λx)dx.
3. Evaluate the boundary term:

   As x→∞, x e^{−λx} → 0, so x(−e^{−λx}) → 0.

   At x=0, x(−e^{0}) = 0.

   So

   [x(−e−λx)]0∞=0.\left[x(-e^{-\lambda x})\right]\_0^{\infty} = 0.[x(−e−λx)]0∞​=0.
4. Compute the remaining integral:

   −∫0∞(−e−λx)dx=∫0∞e−λxdx=[−1λe−λx]0∞=0−(−1λ)=1λ.-\int\_0^{\infty} (-e^{-\lambda x}) dx = \int\_0^{\infty} e^{-\lambda x} dx = \left[-\frac{1}{\lambda}e^{-\lambda x}\right]\_0^{\infty} = 0 - \left(-\frac{1}{\lambda}\right)=\frac{1}{\lambda}.−∫0∞​(−e−λx)dx=∫0∞​e−λxdx=[−λ1​e−λx]0∞​=0−(−λ1​)=λ1​.
5. Therefore

   E[X]=1λ.\mathbb{E}[X] = \frac{1}{\lambda}.E[X]=λ1​.

**Insight:** For continuous variables, expectation is still a weighted average—just spread across a continuum. The exponential distribution’s mean 1/λ matches the intuition: higher rate λ means shorter expected waiting time.

## Key Takeaways

- ✓

  Expected value E[X] is the theoretical long-run average of a random variable, aligning with the sample mean under repeated draws (formalized later by LLN).
- ✓

  Discrete expectation is a probability-weighted sum: E[X]=∑ₓ x·P(X=x). Continuous expectation is a probability-weighted integral: E[X]=∫ x f\_X(x) dx.
- ✓

  Linearity is the main computational tool: E[X+Y]=E[X]+E[Y] and E[aX+b]=aE[X]+b, without needing independence.
- ✓

  Indicator variables convert probabilities into expectations: if I is 1 on event A and 0 otherwise, then E[I]=P(A).
- ✓

  Expectation generalizes to transformations: E[g(X)] = ∑ g(x)p(x) or ∫ g(x)f(x)dx (often without finding the distribution of g(X)).
- ✓

  E[X] may be infinite or undefined for heavy-tailed distributions; finiteness typically requires ∑ |x|p(x) < ∞ or ∫ |x|f(x)dx < ∞.
- ✓

  Expected value is foundational for variance, entropy, fair games, and optimizing expected loss in machine learning.

## Common Mistakes

- ✗

  Thinking E[X] must be a value X can actually take (e.g., expecting a die to roll 3.5).
- ✗

  Forgetting that probabilities must sum/integrate to 1 before computing E[X], leading to incorrect weighted averages.
- ✗

  Assuming E[XY]=E[X]E[Y] without checking independence (linearity does not apply to products).
- ✗

  Ignoring existence: applying expectation formulas to heavy-tailed cases where the sum/integral diverges, producing misleading “answers.”

## Practice

easy

A biased coin lands heads with probability p. Let X be the payout where you get $1 for heads and $0 for tails. Compute E[X].

**Hint:** List the two outcomes (1 and 0) and weight by their probabilities.

Show solution

Outcomes: X=1 with probability p, and X=0 with probability 1−p.

E[X]=1⋅p+0⋅(1−p)=p.\mathbb{E}[X] = 1\cdot p + 0\cdot (1-p) = p.E[X]=1⋅p+0⋅(1−p)=p.

So the expected payout is p dollars.

medium

Let X be the result of a fair six-sided die. Define Y = 2X − 1. Compute E[Y] using linearity (do not re-sum from scratch).

**Hint:** First recall E[X] for a fair die, then apply E[aX+b]=aE[X]+b.

Show solution

For a fair die, $E[X]=3.5.\mathbb{E}[X]=3.5.E[X]=3.5.$ Using linearity:

E[Y]=E[2X−1]=2E[X]−1=2(3.5)−1=7−1=6.\mathbb{E}[Y]=\mathbb{E}[2X-1]=2\mathbb{E}[X]-1=2(3.5)-1=7-1=6.E[Y]=E[2X−1]=2E[X]−1=2(3.5)−1=7−1=6.

hard

Optional/advanced: Let X take values 1,2,3,… with probability P(X=k)=c/k^2 for k≥1. (a) Find c. (b) Does E[X] exist as a finite number?

**Hint:** Use that ∑\_{k=1}^∞ 1/k^2 converges (to π²/6). For part (b), examine ∑ k·(c/k²).

Show solution

(a) We need probabilities to sum to 1:

∑k=1∞ck2=c∑k=1∞1k2=1.\sum\_{k=1}^{\infty} \frac{c}{k^2} = c \sum\_{k=1}^{\infty} \frac{1}{k^2} = 1.k=1∑∞​k2c​=ck=1∑∞​k21​=1.

Using $∑k=1∞1k2=π26,\sum\_{k=1}^{\infty} \frac{1}{k^2} = \frac{\pi^2}{6},∑k=1∞​k21​=6π2​,$ we get

c⋅π26=1⇒c=6π2.c\cdot \frac{\pi^2}{6}=1 \Rightarrow c=\frac{6}{\pi^2}.c⋅6π2​=1⇒c=π26​.

(b) Compute expectation:

E[X]=∑k=1∞k⋅ck2=c∑k=1∞1k.\mathbb{E}[X] = \sum\_{k=1}^{\infty} k\cdot \frac{c}{k^2} = c\sum\_{k=1}^{\infty} \frac{1}{k}.E[X]=k=1∑∞​k⋅k2c​=ck=1∑∞​k1​.

But ∑\_{k=1}^∞ 1/k diverges, so E[X] is infinite (does not exist as a finite number). In this case we say the expectation diverges to +∞.

## Connections

Next nodes you can unlock and why they depend on expected value:

- •[Variance](/tech-tree/variance/): uses the mean μ = E[X] and defines spread via $Var(X)=E[(X−μ)2].\mathrm{Var}(X)=\mathbb{E}[(X-\mu)^2].Var(X)=E[(X−μ)2].$
- •[Entropy](/tech-tree/entropy/): can be written as an expectation, e.g. discrete $H(X)=E[−log⁡p(X)].H(X)=\mathbb{E}[-\log p(X)].H(X)=E[−logp(X)].$
- •[Law of Large Numbers](/tech-tree/law-large-numbers/): formal statement that the sample mean approaches E[X] under conditions.
- •[Game Theory Introduction](/tech-tree/game-theory-intro/): expected payoff evaluates mixed (randomized) strategies.
- •[Stochastic Gradient Descent](/tech-tree/sgd/): relies on unbiased gradient estimates, an expectation identity $E[g(θ)]≈∇R(θ).\mathbb{E}[g(\theta)]\approx \nabla R(\theta).E[g(θ)]≈∇R(θ).$

Quality: A (4.5/5)

[← back to tree](/tech-tree/)[browse all →](/tech-tree/inventory/)
