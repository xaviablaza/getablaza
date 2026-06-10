---
title: Variance
description: Measure of spread. E[(X - mu)^2]. Standard deviation is sqrt(variance).
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
generated_by: templeton-deep-copy-import
permalink: /tech-tree/variance/
---

[←Back to Tech Tree](/tech-tree/)

[inventory](/tech-tree/inventory/)[coverage](/tech-tree/coverage/)

# Variance

Probability & StatisticsDifficulty: ★★☆☆☆Depth: 4Unlocks: 60

Measure of spread. E[(X - mu)^2]. Standard deviation is sqrt(variance).

## Interactive Visualization

⏮◀◀▶▶STEP0.25x1xZOOM

t=0s

## Core Concepts

- -Variance is the expected squared deviation from the mean: E[(X - mu)^2].
- -Variance is always nonnegative and equals zero exactly when the random variable is (almost surely) constant.

## Key Symbols & Notation

Var(X) (variance of X)

## Essential Relationships

- -Standard deviation = positive square root of variance: sigma = sqrt(Var(X)).
- -Variance under linear transformation: Var(aX + b) = a^2 Var(X).

## Prerequisites (1)

[Expected Value5 atoms](/tech-tree/expected-value/)

## Unlocks (3)

[Common Distributionslvl 2](/tech-tree/common-distributions/)[Covariance and Correlationlvl 3](/tech-tree/covariance-correlation/)[Layer Normalizationlvl 4](/tech-tree/layer-normalization/)

## Referenced by (22)

Where this concept shows up in the operating-finance and personal-finance graphs.

### From Business (15)

[personal financeBusiness

Asset allocation drives 90%+ of portfolio return variance - allocation decisions are literally variance decomposition and management](/business/personal-finance/)[Income StabilityBusiness

Income stability is literally the variance of the income random variable - a salaried W2 has near-zero variance while freelance/commission income has high variance, and sizing the buffer is a function of that spread](/business/income-stability/)[Investment HorizonBusiness

Annualized variance of portfolio returns shrinks as horizon lengthens (variance of mean scales as sigma^2/T), which is the mathematical reason longer horizons tolerate riskier allocations.](/business/investment-horizon/)[Expected ReturnBusiness

Variance is the exact quantity expected return ignores. The critique embedded in 'Expected Return' - that equal-EV projects aren't truly equivalent - only makes sense once you have variance as a formal measure of spread.](/business/expected-return/)[Market DownturnBusiness

Variance (and its square root, volatility) is the mathematical foundation for quantifying how much an asset can decline - a 30-50% drawdown is a statement about realized variance in the tails of the return distribution](/business/market-downturn/)[VarianceBusiness

Direct mathematical definition: Var(X) = E[(X - mu)^2]. The business concept of treating equal-expected-return projects as equivalent ignores this second moment of the return distribution](/business/variance/)[LeverageBusiness

Leverage multiplies the variance of returns by the square of the leverage ratio - a 3x leveraged position has 9x the variance, which is the mathematical basis for why leveraged capital must be treated as high-risk and other exposures reduced to keep portfolio-level variance within tolerance](/business/leverage/)[investment returnsBusiness

The spread only holds in expectation - variance of investment returns means realized outcomes can underperform the mortgage rate over any finite horizon, making the 10+ year condition a statement about when variance shrinks enough relative to the mean](/business/investment-returns/)[Standard DeviationBusiness

Standard deviation is defined as sqrt(variance); understanding E[(X - mu)^2] and its properties is the direct mathematical foundation for reasoning about sigma and distribution tightness](/business/standard-deviation/)[SkewBusiness

Skewness is the third central moment, the direct generalization of variance (second central moment) to measure distribution asymmetry. You must understand variance as E[(X-mu)^2] before skew as E[(X-mu)^3]/sigma^3 makes sense - same machinery, one degree higher.](/business/skew/)[Quality SystemsBusiness

Quality IS variance control. Reducing output variance around a target is the literal definition of process quality. SPC, Six Sigma, and production monitoring all measure and bound variance.](/business/quality-systems/)[Sharpe RatioBusiness

sigma(R) in the denominator is the square root of variance; understanding variance as E[(X-mu)^2] is the direct mathematical prerequisite for quantifying execution risk as spread around expected return](/business/sharpe-ratio/)[VolatilityBusiness

Volatility IS standard deviation, which IS sqrt(variance). This is the direct mathematical definition - variance measures spread of a random variable, volatility applies that to returns](/business/volatility/)[Financial InstrumentsBusiness

Risk-adjusted return (e.g. Sharpe ratio = (E[R] - Rf) / sigma) requires quantifying risk as variance/standard deviation of returns - variance is the mathematical foundation for the 'risk' denominator in every risk-adjusted metric](/business/financial-instruments/)[Hurdle RateBusiness

Sharpe ratio = (E[R] - hurdle) / σ directly uses standard deviation to risk-adjust returns, making variance the mathematical foundation for distinguishing a high-return-high-risk opportunity from a genuinely attractive one](/business/hurdle-rate/)

### From Money (7)

[Full Emergency FundMoney

Income volatility (variance) determines the right fund size](/money/full-emergency-fund/)[Moderate-Interest DebtMoney

Risk-adjusted comparison requires understanding return variance](/money/moderate-debt-strategy/)[Asset ClassesMoney

Risk is measured as return variance or standard deviation](/money/asset-classes/)[DiversificationMoney

Portfolio variance decreases with uncorrelated additions](/money/diversification/)[Dollar-Cost AveragingMoney

DCA reduces variance of entry price at the cost of expected return](/money/dollar-cost-averaging/)[Real Estate LeverageMoney

Leverage directly multiplies portfolio variance - amplified risk](/money/real-estate-leverage/)[Alternative InvestmentsMoney

Alternative assets have wider return distributions than public markets](/money/alternative-investments/)

Advanced Learning Details

### Graph Position

34

Depth Cost

60

Fan-Out (ROI)

27

Bottleneck Score

4

Chain Length

### Cognitive Load

5

Atomic Elements

20

Total Elements

L0

Percentile Level

L3

Atomic Level

### All Concepts (8)

- - Spread (dispersion) of a distribution as a distinct property from its mean
- - Squared deviation: (X - μ)^2 as a way to measure how far an outcome is from the mean without cancellation
- - Variance as the expected squared deviation: Var(X) = E[(X - μ)^2]
- - Standard deviation as the square root of variance
- - Units issue: variance is measured in squared units of X while standard deviation is in the same units as X
- - Variance is always nonnegative
- - Zero variance means no variability (the random variable is constant with probability 1)
- - Squaring deviations gives more weight to larger deviations (sensitivity to outliers)

### Teaching Strategy

Self-serve tutorial - low prerequisites, straightforward concepts.

You can know the “average” of a random variable and still be surprised all the time. Variance is the standard way to quantify how spread out the outcomes are around that average.

TL;DR:

Variance measures spread: Var(X) = E[(X − μ)²], where μ = E[X]. It’s always ≥ 0, equals 0 only if X is constant (almost surely), and can be computed efficiently via Var(X) = E[X²] − (E[X])². Standard deviation is √Var(X).

## What Is Variance?

### Why we need more than an average

Expected value tells you the center of a distribution: μ = E[X]. But two random variables can have the same μ and behave very differently.

Example intuition:

- •X is always 0.
- •Y is +10 half the time and −10 half the time.

Both have E[X] = E[Y] = 0, but Y “swings” wildly while X never moves. Variance is designed to capture that swing.

### Definition

Let X be a random variable with mean μ = E[X]. The **variance** of X is

Var(X) = E[(X − μ)²].

Read this as: “take the deviation from the mean, square it, then average.”

### Why squared deviation?

We want a measure of spread that:

1. 1)Treats positive and negative deviations symmetrically (so they don’t cancel).
2. 2)Penalizes larger deviations more than smaller ones.
3. 3)Plays nicely with algebra and optimization (this becomes important in statistics and ML).

Absolute deviation |X − μ| would avoid cancellation too, but squaring is the choice that leads to particularly useful identities (like Var(X) = E[X²] − μ²) and makes many derivations clean.

### Units and standard deviation

If X has units (meters, dollars, etc.), then (X − μ)² has squared units, so variance has squared units too. To get back to the original units, define the **standard deviation**:

σ = √Var(X).

Variance is the main mathematical object; standard deviation is often easier to interpret in the original scale.

### A quick geometric picture

If you think of outcomes x as points on a line, μ is the “balance point,” and (x − μ)² is the squared distance to that point. Variance is the expected squared distance to the center.

## Core Mechanic 1: Computing Variance (and the E[X²] − (E[X])² Identity)

### The direct computation

From the definition, for a discrete random variable:

Var(X) = E[(X − μ)²] = ∑ (x − μ)² P(X = x).

This is conceptually simple:

1. 1)Find μ.
2. 2)For each outcome x, compute (x − μ)².
3. 3)Weight by P(X = x) and sum.

For a continuous random variable with density f(x), replace the sum with an integral:

Var(X) = ∫ (x − μ)² f(x) dx.

### The shortcut identity: Var(X) = E[X²] − (E[X])²

Computing (x − μ)² can be tedious. There’s a standard algebraic identity that makes variance faster to compute.

Start with the definition and expand:

Var(X)

= E[(X − μ)²]

= E[X² − 2μX + μ²].

Now use linearity of expectation and the fact that μ is a constant:

E[X² − 2μX + μ²]

= E[X²] − 2μE[X] + E[μ²]

= E[X²] − 2μ·μ + μ²

= E[X²] − μ².

So:

Var(X) = E[X²] − (E[X])².

This is one of the most-used formulas in probability and statistics.

### Why this identity matters

It separates variance into two pieces you can often compute easily:

- •E[X] (first moment)
- •E[X²] (second moment)

Many common distributions have known formulas for these moments, making Var(X) almost immediate.

### Invariance to shifts (adding a constant)

A key property: shifting a random variable by a constant does not change its variance.

Let Y = X + c. Then E[Y] = E[X] + c = μ + c.

Compute variance:

Var(Y)

= E[(Y − E[Y])²]

= E[(X + c − (μ + c))²]

= E[(X − μ)²]

= Var(X).

So variance measures spread, not location.

### Scaling rule (multiplying by a constant)

If you scale outcomes, spread scales quadratically:

Let Y = aX. Then E[Y] = aμ.

Var(Y)

= E[(aX − aμ)²]

= E[a²(X − μ)²]

= a²E[(X − μ)²]

= a²Var(X).

So:

Var(aX) = a²Var(X).

This is why standard deviation scales linearly: √Var(aX) = |a| √Var(X).

### Quick reference table

| Transformation | New mean | New variance |
| --- | --- | --- |
| Y = X + c | E[Y] = μ + c | Var(Y) = Var(X) |
| Y = aX | E[Y] = aμ | Var(Y) = a²Var(X) |
| Y = aX + c | E[Y] = aμ + c | Var(Y) = a²Var(X) |

## Core Mechanic 2: Nonnegativity, When Variance Is Zero, and “Almost Surely”

### Variance is always nonnegative

From the definition:

Var(X) = E[(X − μ)²].

But (X − μ)² ≥ 0 for every outcome, because a square can’t be negative. An expectation of a nonnegative random variable is nonnegative, so:

Var(X) ≥ 0.

This is not just a technicality: it tells you variance behaves like a “size” or “energy.”

### When is variance exactly zero?

Variance is zero exactly when there is no spread at all.

Claim:

Var(X) = 0 ⇔ X = μ almost surely.

Meaning: X equals the constant μ with probability 1 (it may differ on a probability-0 set, which doesn’t affect expectations).

#### Why “if” direction is true

If X = μ (with probability 1), then X − μ = 0 (with probability 1), so (X − μ)² = 0 always. Therefore E[(X − μ)²] = 0.

#### Why “only if” direction is true

If Var(X) = E[(X − μ)²] = 0 and (X − μ)² is always ≥ 0, the only way the average can be 0 is if it is 0 wherever probability mass exists.

Formally (intuition-first):

- •If there were any positive probability that (X − μ)² > 0, then the expectation would be > 0.
- •So it must be that P((X − μ)² = 0) = 1, i.e., P(X = μ) = 1.

### “Almost surely” in plain terms

“Almost surely” (a.s.) means “with probability 1.”

It allows edge cases where X might misbehave on events of probability 0, but those events do not affect expectations, variances, or most practical probability calculations.

Example:

- •A continuous random variable might have P(X = 0) = 0, but it could still be possible that some definition changes at x = 0 without affecting anything measurable.

For variance, “Var(X) = 0 implies X is constant a.s.” is the correct statement.

### Variance as a measure of concentration

The smaller Var(X) is, the more tightly X concentrates around μ.

A very important inequality (you don’t need to master it yet, but it motivates why variance matters) is Chebyshev’s inequality:

P(|X − μ| ≥ kσ) ≤ 1/k².

It says: if variance is small, large deviations from the mean are unlikely.

This is a major reason variance is used as a compact summary of uncertainty.

## Application/Connection: Variance in Distributions, Covariance/Correlation, and Normalization in ML

### Variance in common distributions

Once you know how to compute variance, you can summarize a distribution with (mean, variance). Many families are parameterized this way.

A few examples you’ll meet soon:

- •Bernoulli(p): mean p, variance p(1 − p)
- •Binomial(n, p): mean np, variance np(1 − p)
- •Poisson(λ): mean λ, variance λ
- •Normal(μ, σ²): mean μ, variance σ²

Variance is the “second parameter” in many models because it controls spread.

### From variance to covariance and correlation

Variance is the special case of covariance when you compare a variable with itself.

Cov(X, Y) is defined as:

Cov(X, Y) = E[(X − E[X])(Y − E[Y])].

If you plug in Y = X:

Cov(X, X) = E[(X − E[X])(X − E[X])]

= E[(X − μ)²]

= Var(X).

So variance is “self-covariance.” This viewpoint is crucial later:

- •Covariance matrices describe how a **vector** random variable **X** (boldface often used for vectors) varies in multiple dimensions.
- •The diagonal entries are variances of each component.

Correlation normalizes covariance by standard deviations:

Corr(X, Y) = Cov(X, Y) / (σₓ σᵧ).

Variance is the building block for both.

### Why ML cares: normalization and training stability

In deep learning, activations can drift to have large or tiny variance across layers. If variance explodes or vanishes, gradients can become unstable.

Normalization methods (BatchNorm, LayerNorm) explicitly use mean and variance to re-center and re-scale activations.

A typical pattern for a batch of activations a:

1. 1)Compute mean μ̂
2. 2)Compute variance v̂
3. 3)Normalize: (a − μ̂) / √(v̂ + ε)

This makes the normalized activations have approximately mean 0 and variance 1.

Even if you’re not training neural nets yet, the message is:

- •Variance is not just descriptive statistics.
- •It is a control knob for stability in algorithms.

### Population variance vs sample variance (preview)

In probability, Var(X) is a **population** quantity: it assumes you know the true distribution.

In statistics, you estimate variance from samples x₁, …, xₙ. Two common formulas are:

- •“Biased” estimator: (1/n) ∑(xᵢ − x̄)²
- •“Unbiased” estimator: (1/(n−1)) ∑(xᵢ − x̄)²

You don’t need the full derivation here, but it’s helpful to recognize that variance connects probability theory (true Var) to data analysis (estimated variance).

## Worked Examples (3)

### Compute variance directly (small discrete distribution)

Let X take values {0, 1, 2} with probabilities P(0)=1/4, P(1)=1/2, P(2)=1/4. Find μ = E[X], Var(X), and σ.

1. Compute the mean:

   μ = E[X]

   = 0·(1/4) + 1·(1/2) + 2·(1/4)

   = 0 + 1/2 + 1/2

   = 1.
2. Compute squared deviations from the mean:

   (0 − 1)² = 1

   (1 − 1)² = 0

   (2 − 1)² = 1.
3. Take the expectation of squared deviation:

   Var(X) = E[(X − μ)²]

   = 1·(1/4) + 0·(1/2) + 1·(1/4)

   = 1/4 + 0 + 1/4

   = 1/2.
4. Compute standard deviation:

   σ = √Var(X) = √(1/2) ≈ 0.7071.

**Insight:** Variance is an average of squared distances to the mean. Symmetry around μ=1 makes the computation especially simple here.

### Use Var(X) = E[X²] − (E[X])² (Bernoulli case)

Let X ∼ Bernoulli(p), so X ∈ {0,1} with P(X=1)=p and P(X=0)=1−p. Compute Var(X).

1. Compute E[X]:

   E[X] = 0·(1−p) + 1·p = p.
2. Compute E[X²]: since X is 0 or 1, we have X² = X for every outcome.

   So E[X²] = E[X] = p.
3. Apply the identity:

   Var(X) = E[X²] − (E[X])²

   = p − p²

   = p(1 − p).
4. Sanity check at extremes:

   If p=0 or p=1, then Var(X)=0, matching the fact that X is constant.

   If p=1/2, then Var(X)=1/4, the maximum spread for a Bernoulli.

**Insight:** For Bernoulli variables, the shortcut is extremely fast because X² = X. This pattern (compute moments, then combine) is the standard way to get variances for many distributions.

### Effect of scaling and shifting

Suppose Var(X) = 9 and μ = E[X] = 2. Define Y = 3X − 5. Find E[Y], Var(Y), and σᵧ.

1. Compute the mean using linearity:

   E[Y] = E[3X − 5]

   = 3E[X] − 5

   = 3·2 − 5

   = 1.
2. Compute the variance using the scaling rule (shift doesn’t matter):

   Var(Y) = Var(3X − 5)

   = 3² Var(X)

   = 9·9

   = 81.
3. Compute standard deviation:

   σᵧ = √Var(Y) = √81 = 9.

**Insight:** Adding/subtracting constants moves the distribution but doesn’t change spread; multiplying by 3 triples standard deviation and multiplies variance by 9.

## Key Takeaways

- ✓

  Variance measures spread around the mean: Var(X) = E[(X − μ)²], μ = E[X].
- ✓

  Var(X) ≥ 0 always, because it is the expectation of a square.
- ✓

  Var(X) = 0 exactly when X is constant almost surely (P(X = μ) = 1).
- ✓

  Efficient computation: Var(X) = E[X²] − (E[X])².
- ✓

  Shifts don’t change variance: Var(X + c) = Var(X).
- ✓

  Scaling changes variance quadratically: Var(aX) = a²Var(X).
- ✓

  Standard deviation is the square root of variance: σ = √Var(X), restoring original units.

## Common Mistakes

- ✗

  Forgetting to compute μ = E[X] first, or using the wrong mean when plugging into E[(X − μ)²].
- ✗

  Mixing up variance and standard deviation (variance is squared units; standard deviation is √variance).
- ✗

  Thinking Var(X + c) changes with c (it doesn’t); only scaling affects variance magnitude.
- ✗

  Dropping the square when expanding (X − μ)² or misapplying Var(X) = E[X²] − (E[X])².

## Practice

easy

Let X take values {−1, 0, 1} with probabilities {1/4, 1/2, 1/4}. Compute E[X], Var(X), and σ.

**Hint:** Symmetry suggests E[X]=0. Then Var(X)=E[X²].

Show solution

Mean:

E[X] = (−1)(1/4) + 0(1/2) + 1(1/4) = 0.

Variance:

Since μ=0, Var(X)=E[X²].

E[X²] = (1)(1/4) + 0(1/2) + (1)(1/4) = 1/2.

So Var(X)=1/2.

Standard deviation:

σ = √(1/2) ≈ 0.7071.

medium

Use Var(X) = E[X²] − (E[X])². Suppose P(X=1)=0.2, P(X=3)=0.8. Compute Var(X).

**Hint:** Compute E[X] and E[X²] from the two-point distribution, then subtract.

Show solution

E[X] = 1·0.2 + 3·0.8 = 0.2 + 2.4 = 2.6.

E[X²] = 1²·0.2 + 3²·0.8 = 1·0.2 + 9·0.8 = 0.2 + 7.2 = 7.4.

Var(X) = E[X²] − (E[X])² = 7.4 − (2.6)² = 7.4 − 6.76 = 0.64.

medium

Assume Var(X)=4. Define Z = −2X + 10. Compute Var(Z) and σ\_z.

**Hint:** Use Var(aX + c) = a²Var(X). The sign of a doesn’t matter after squaring.

Show solution

Var(Z) = Var(−2X + 10) = (−2)²Var(X) = 4·4 = 16.

σ\_z = √Var(Z) = √16 = 4.

## Connections

- •Next: [Common Distributions](/tech-tree/common-distributions/)
- •Next: [Covariance and Correlation](/tech-tree/covariance-correlation/)
- •Applied ML: [Layer Normalization](/tech-tree/layer-normalization/)
- •Prerequisite review: Expected Value (already known in this path)

Quality: A (4.4/5)

[← back to tree](/tech-tree/)[browse all →](/tech-tree/inventory/)
