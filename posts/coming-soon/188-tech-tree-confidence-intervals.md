---
title: Confidence Intervals
description: Range of plausible values for population parameter.
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
permalink: /tech-tree/confidence-intervals/
---

[←Back to Tech Tree](/tech-tree/)

[inventory](/tech-tree/inventory/)[coverage](/tech-tree/coverage/)

# Confidence Intervals

Probability & StatisticsDifficulty: ★★★☆☆Depth: 7Unlocks: 0

Range of plausible values for population parameter.

## Interactive Visualization

⏮◀◀▶▶STEP0.25x1xZOOM

t=0s

## Core Concepts

- -Interval estimate: a data-derived range intended to contain the population parameter

## Key Symbols & Notation

theta (true population parameter)theta\_hat (point estimator of theta)se(theta\_hat) (standard error of the estimator)

## Prerequisites (2)

[Central Limit Theorem6 atoms](/tech-tree/central-limit-theorem/)[Maximum Likelihood Estimation6 atoms](/tech-tree/mle/)

Advanced Learning Details

### Graph Position

83

Depth Cost

0

Fan-Out (ROI)

0

Bottleneck Score

7

Chain Length

### Cognitive Load

4

Atomic Elements

38

Total Elements

L2

Percentile Level

L2

Atomic Level

### All Concepts (15)

- - Confidence interval (CI) as an interval-valued estimator: a data-dependent interval [L(X), U(X)] intended to capture the true (fixed) population parameter with prescribed long-run frequency
- - Confidence level (1 - α): the prescribed long-run proportion of such intervals that contain the true parameter
- - Frequentist interpretation nuance: the CI statement refers to randomness of the interval (over repeated samples), not a probabilistic statement about the fixed parameter
- - Interval estimator vs point estimator: CI gives a range of plausible values, not a single best estimate
- - Margin of error (MOE): the half-width of the CI (distance from point estimate to each endpoint)
- - Standard error (SE) of an estimator used inside the CI: an estimate of the estimator's sampling standard deviation
- - Critical value: a quantile from a reference distribution (e.g., z\* or t\*) used to scale the SE to achieve the desired confidence level
- - t-distribution adjustment for unknown variance / small samples: replacing normal critical values with t\_{·, df} and the role of degrees of freedom
- - One-sided vs two-sided CIs: construction and interpretation differences
- - Exact vs approximate CIs: exact when a pivot with known finite-sample distribution is available; approximate when relying on large-sample (asymptotic) results
- - Pivotal quantity: a function of data and parameter whose distribution does not depend on the unknown parameter, used to derive exact CIs
- - Coverage probability and nominal vs actual coverage: the intended (nominal) confidence level may differ from the true long-run coverage in finite samples
- - Relationship between CI width and sample size / variability / confidence level: how n, σ (or estimated SE), and 1-α affect interval length
- - Practical construction variants: analytic CIs (exact or asymptotic) and resampling-based CIs (bootstrap percentile, basic, etc.)
- - Equivalence between two-sided CI and two-sided hypothesis test: parameter values excluded by the (1-α) CI correspond to values rejected by a level-α two-sided test

### Teaching Strategy

Quick unlock - significant prerequisite investment but simple final step. Verify prerequisites first.

Point estimates (like θ̂) give you a single best guess. Confidence intervals add the missing piece: how uncertain that guess is, using a principled link between your data, your estimator’s sampling variation, and probability.

TL;DR:

A (1 − α) confidence interval (CI) is a random interval computed from data that contains the fixed true parameter θ with probability 1 − α over repeated sampling. Most common CIs look like

θ̂ ± (critical value) · se(θ̂)

where se(θ̂) measures typical sampling error. Interpretation is about the procedure’s long-run coverage, not the probability that θ lies in a specific realized interval.

## What Is a Confidence Interval?

### Why we need more than a point estimate

Suppose you estimate a population parameter θ (a mean, a proportion, a regression coefficient) using a point estimator θ̂ computed from sample data. Even if θ̂ is “good” (unbiased or consistent), it will vary from sample to sample.

If we only report θ̂, we hide an essential fact: a different random sample would yield a different estimate. A confidence interval is an **interval estimate**: a data-derived range intended to contain θ.

### The key idea: θ is fixed, the interval is random

A common beginner intuition is: “After I compute an interval, there’s a 95% probability that θ is inside.” That’s not the frequentist definition.

In frequentist statistics, θ is a fixed (unknown) constant. Randomness comes from the sampling process. So a confidence interval is a **random interval** [L(X), U(X)] computed from random data X.

A (1 − α) CI is a procedure that satisfies the **coverage property**:

P( L(X) ≤ θ ≤ U(X) ) = 1 − α

The probability is over repeated sampling of X under the assumed model.

### What “95% confidence” really means

Imagine repeating the same experiment many times, each time computing a 95% CI using the same method. About 95% of those intervals will contain the true θ. About 5% will miss it.

Once you have computed one interval from your one dataset, the interval is no longer random; it’s a fixed numerical range. The method used to compute it is what carries the 95% guarantee.

### A quick contrast: probability statements vs confidence statements

- •Probability statement (Bayesian-style): P(θ ∈ [a, b] | data) = 0.95
- •Confidence statement (frequentist): P([L(X), U(X)] contains θ) = 0.95

They sound similar, but condition on different things. Confidence intervals do not, by default, assign probabilities to θ.

### Anatomy of a typical CI

Most classical CIs follow a common template:

θ̂ ± (critical value) · se(θ̂)

- •θ̂ is your point estimate
- •se(θ̂) is its **standard error** (typical sampling deviation)
- •the critical value sets the desired coverage (often from a Normal or t distribution)

This is the “margin of error” idea made precise.

### Where the template comes from (preview)

The template is a consequence of: (1) a sampling distribution for θ̂, often approximately Normal via the Central Limit Theorem (CLT), and (2) a pivot or standardized statistic whose distribution we can control.

You already know the CLT: sums/averages of many random variables tend toward a Normal distribution. Confidence intervals are where that knowledge becomes actionable.

## Core Mechanic 1: Sampling Distributions, Standard Error, and the CLT

### Why sampling distributions matter

A confidence interval is a statement about what happens across repeated samples. So we need the distribution of θ̂ across those repeated samples: the **sampling distribution**.

If θ̂ has a distribution centered at θ with some spread, we can pick an interval around θ̂ that captures θ most of the time.

### Standard error: the scale of estimator noise

The **standard error** se(θ̂) is the standard deviation of θ̂’s sampling distribution:

se(θ̂) = √Var(θ̂)

You can read it as: “How much θ̂ typically wiggles due to sampling.”

Crucially:

- •Standard deviation (SD) describes variability in raw data.
- •Standard error (SE) describes variability in an estimator across samples.

### Example: mean of i.i.d. data

Let X₁, …, Xₙ be i.i.d. with mean μ and variance σ². The sample mean is

μ̂ = X̄ = (1/n) ∑ᵢ Xᵢ

Then

E[X̄] = μ

Var(X̄) = σ² / n

se(X̄) = σ / √n

So uncertainty shrinks like 1/√n. This is why sample size helps, but with diminishing returns.

### Using the CLT to get an approximate Normal sampling distribution

For large n, the CLT says

(X̄ − μ) / (σ/√n) ≈ Normal(0, 1)

Equivalently,

X̄ ≈ Normal( μ, σ²/n )

This approximation is the workhorse behind many “Wald-type” confidence intervals.

### Unknown σ: replacing it creates extra uncertainty

In real problems, σ is usually unknown. We estimate it with the sample standard deviation s.

When data are Normal, we have an exact result:

T = (X̄ − μ) / (s/√n) ∼ t\_{n−1}

That t distribution is wider than Normal(0,1), reflecting the extra uncertainty from estimating σ.

### General pattern (beyond means)

Often, for an estimator θ̂ (like an MLE), we have an asymptotic Normal approximation:

θ̂ ≈ Normal( θ, Var(θ̂) )

Then a standardized version

Z = (θ̂ − θ) / se(θ̂)

is approximately Normal(0,1). This is the bridge from sampling distribution to an interval.

### What you need to build a CI in practice

To construct a CI, you typically need:

1) A point estimator θ̂

2) An estimate of its standard error se(θ̂)

3) A critical value c such that

P(−c ≤ Z ≤ c) = 1 − α

Then solve the inequality for θ.

### Breathing room: why “standard error” is the star

If you remember only one operational fact:

A CI width is controlled primarily by se(θ̂).

Everything else (Normal vs t, exact vs approximate, 90% vs 95%) is a multiplier on that base uncertainty. If your SE estimate is poor, your CI will be misleading.

## Core Mechanic 2: Building Confidence Intervals via Pivots (and the Wald Form)

### Why pivots are powerful

To build an interval, we want a statistic with a known distribution that does **not** depend on the unknown θ (or depends on it in a controllable way). Such a statistic is called a **pivot**.

Once we have a pivot, we can take quantiles of its distribution and algebraically rearrange to isolate θ.

### The classic Normal-based (Wald) derivation

Assume we have an estimator θ̂ such that

Z = (θ̂ − θ) / se(θ̂) ≈ Normal(0, 1)

Let z\_{1−α/2} be the (1 − α/2) quantile of the standard Normal. Then

P( −z\_{1−α/2} ≤ Z ≤ z\_{1−α/2} ) ≈ 1 − α

Substitute Z:

P( −z\_{1−α/2} ≤ (θ̂ − θ)/se(θ̂) ≤ z\_{1−α/2} ) ≈ 1 − α

Now solve for θ. Multiply through by se(θ̂) (positive):

P( −z\_{1−α/2}·se(θ̂) ≤ θ̂ − θ ≤ z\_{1−α/2}·se(θ̂) ) ≈ 1 − α

Rearrange terms:

Left inequality:

θ̂ − θ ≥ −z·se

⇒ −θ ≥ −z·se − θ̂

⇒ θ ≤ θ̂ + z·se

Right inequality:

θ̂ − θ ≤ z·se

⇒ −θ ≤ z·se − θ̂

⇒ θ ≥ θ̂ − z·se

Combine:

P( θ̂ − z\_{1−α/2}·se(θ̂) ≤ θ ≤ θ̂ + z\_{1−α/2}·se(θ̂) ) ≈ 1 − α

So the (approximate) (1 − α) CI is

[ θ̂ − z\_{1−α/2}·se(θ̂), θ̂ + z\_{1−α/2}·se(θ̂) ]

This is the famous “estimate ± margin of error.”

### When to use t instead of z

If your pivot is t-distributed (common for means with unknown σ under Normal data), you replace z\_{1−α/2} with t\_{n−1, 1−α/2}.

### Interpreting the critical value

Common two-sided critical values:

| Confidence | α | z\_{1−α/2} (approx) |
| --- | --- | --- |
| 90% | 0.10 | 1.645 |
| 95% | 0.05 | 1.96 |
| 99% | 0.01 | 2.576 |

Higher confidence means a larger multiplier, hence wider intervals.

### One-sided confidence intervals

Sometimes you only care about an upper bound or lower bound.

For an upper (1 − α) bound, you want

P( Z ≤ z\_{1−α} ) = 1 − α

leading to an upper confidence bound:

θ ≤ θ̂ + z\_{1−α}·se(θ̂)

Similarly for a lower bound.

### Beyond Wald: why alternative constructions exist

The Wald CI is simple, but it can behave poorly when:

- •sample size is small
- •parameter is near a boundary (e.g., probability p near 0 or 1)
- •estimator distribution is skewed

This is why you will later see intervals like Wilson score intervals (for proportions), likelihood-based intervals, or bootstrap intervals.

Still, the pivot logic remains the same: find (or approximate) a statistic with a known distribution, then invert it.

### A useful comparison table

| Method | Form | Needs | Pros | Cons |
| --- | --- | --- | --- | --- |
| z/Wald CI | θ̂ ± z·se | se(θ̂), Normal approx | Simple, general | Can mis-cover in small n / boundaries |
| t CI (mean) | X̄ ± t·(s/√n) | Normal data (or robust large n) | Better small-sample than z | Still assumes reasonably symmetric behavior |
| Likelihood-based | {θ: 2(ℓ(θ̂)−ℓ(θ)) ≤ c} | Log-likelihood ℓ(θ) | Often better shape/constraints | More computation, theory |
| Bootstrap | quantiles of θ̂\* | resampling procedure | Flexible | Can fail for dependent data or weird estimators |

For this node, the main goal is to master what a CI means and how the standard “critical value × SE” construction arises.

## Application / Connection: Using Confidence Intervals in Real Work

### What CIs let you do

Confidence intervals are a lingua franca for uncertainty.

They let you:

- •communicate estimation uncertainty (more informative than a point estimate)
- •compare groups (do intervals overlap? cautiously interpreted)
- •connect to hypothesis tests (CI inversion)
- •reason about practical significance (is the whole interval within a “good enough” range?)

### CI ↔ hypothesis test connection (inversion idea)

A two-sided (1 − α) CI for θ corresponds to a two-sided hypothesis test at level α:

H₀: θ = θ₀

Rule:

- •Reject H₀ if θ₀ is outside the (1 − α) CI.
- •Fail to reject if θ₀ is inside.

Why this works: both procedures are built from the same pivot and critical region.

### Planning and sample size (precision thinking)

Suppose your CI has half-width (margin of error) m:

m = z\_{1−α/2} · se(θ̂)

For a mean with known σ:

m = z · (σ/√n)

Solve for n to achieve desired precision m:

m = zσ/√n

⇒ √n = zσ/m

⇒ n = (zσ/m)²

This turns “How many samples do we need?” into a quantitative design question.

### Practical interpretation: what you can safely say

Given a 95% CI [L, U], it’s correct to say:

- •“Using this method, we constructed an interval that would cover θ in 95% of repeated samples.”
- •“Values of θ far outside [L, U] are not very compatible with the data under the model.”

Be cautious with:

- •“There is a 95% probability θ is in [L, U].” (frequentist CIs don’t mean that)

### Width drivers and trade-offs

CI width increases when:

- •confidence level increases (95% → 99%)
- •data are noisier (larger σ, larger Bernoulli variance p(1−p))
- •sample size decreases
- •the estimator is inefficient (larger Var(θ̂))

CI width decreases when:

- •n increases
- •you use a more efficient estimator (e.g., MLE under correct model)

### Connection to MLE (a prerequisite you already know)

For many MLEs θ̂, under regularity conditions:

θ̂ ≈ Normal( θ, I(θ)^{-1} )

where I(θ) is Fisher information (or n times per-sample information). In practice we plug in θ̂:

se(θ̂) ≈ √( I(θ̂)^{-1} )

Then a Wald CI becomes

θ̂ ± z\_{1−α/2} · √( I(θ̂)^{-1} )

This is one of the most common “automatic CI” outputs in statistical software.

### “Compatible values” mindset

A CI is often best treated as the set of parameter values that are reasonably compatible with your observed data under the assumed model.

This mindset helps you avoid the trap of treating 0.049 vs 0.051 p-values as fundamentally different: an interval shows a continuum of plausible effects.

### A final caution: the model assumptions matter

Coverage (the 95% guarantee) depends on the assumptions used to derive se(θ̂) and the pivot distribution:

- •independence assumptions
- •identical distribution / stationarity
- •correct likelihood model for MLE-based SEs
- •large-sample approximations actually being “large enough”

If those fail, your interval can under-cover (too narrow) or over-cover (too wide).

## Worked Examples (3)

### CI for a population mean μ with unknown σ (t interval)

You measure a quantity in n = 16 independent trials. The sample mean is X̄ = 12.4 and the sample standard deviation is s = 2.0. Assume the data are approximately Normal. Construct a 95% CI for μ.

1. Identify the estimator and its SE:

   μ̂ = X̄ = 12.4

   se(μ̂) = s/√n = 2.0/√16 = 2.0/4 = 0.5
2. Choose the correct critical value:

   Because σ is unknown and we assume Normal data, use a t distribution with df = n − 1 = 15.

   For a 95% two-sided interval, use t\_{15, 0.975} ≈ 2.131.
3. Compute the margin of error:

   ME = t · se = 2.131 · 0.5 = 1.0655
4. Form the interval:

   Lower = 12.4 − 1.0655 = 11.3345

   Upper = 12.4 + 1.0655 = 13.4655

   So the 95% CI is approximately [11.33, 13.47].

**Insight:** The interval width is driven by se = s/√n. If you quadruple n, √n doubles and the CI half-width roughly halves (holding s similar). The switch from z to t is a small-sample correction for estimating σ.

### Wald CI for a Bernoulli proportion p (large-sample Normal approximation)

In n = 400 trials, you observe x = 92 successes. Estimate the population success probability p and compute an approximate 95% CI using the Wald method.

1. Compute the point estimate:

   The MLE for p is p̂ = x/n = 92/400 = 0.23
2. Compute the estimated standard error:

   For a Bernoulli proportion,

   Var(p̂) = p(1−p)/n

   Plug in p̂ for p:

   se(p̂) ≈ √( p̂(1−p̂)/n )

   = √( 0.23·0.77 / 400 )

   = √( 0.1771 / 400 )

   = √( 0.00044275 )

   ≈ 0.02105
3. Use z critical value for 95%:

   z\_{0.975} ≈ 1.96
4. Compute margin of error:

   ME = 1.96 · 0.02105 ≈ 0.0413
5. Form the interval:

   Lower = 0.23 − 0.0413 = 0.1887

   Upper = 0.23 + 0.0413 = 0.2713

   So the 95% Wald CI is approximately [0.189, 0.271].

**Insight:** This works well here because n is large and p̂ is not near 0 or 1. For smaller n or extreme proportions, Wald intervals can misbehave (even going below 0 or above 1), motivating better alternatives like Wilson or likelihood-based intervals.

### Designing sample size for a target margin of error (mean, planning stage)

You want a 95% CI for a mean μ with margin of error at most m = 0.5. Prior studies suggest σ ≈ 3. How large should n be (approx)?

1. Start from the margin of error formula (Normal approximation):

   m = z\_{0.975} · (σ/√n)
2. Solve for n:

   0.5 = 1.96 · (3/√n)

   ⇒ 0.5 = 5.88 / √n

   ⇒ √n = 5.88 / 0.5 = 11.76

   ⇒ n = (11.76)² = 138.2976
3. Round up to ensure the margin of error target:

   Choose n = 139 (or 140 for convenience).

**Insight:** Precision requirements translate into quadratic sample size growth: halving the margin of error requires roughly 4× as many samples. This is a practical consequence of the 1/√n rate from the CLT.

## Key Takeaways

- ✓

  A (1 − α) confidence interval is a random interval procedure with coverage P(L(X) ≤ θ ≤ U(X)) = 1 − α over repeated samples.
- ✓

  θ is fixed (unknown); the interval is random before you see data. After computing it, the interval is fixed but the method has a long-run guarantee.
- ✓

  Most common CIs take the form θ̂ ± (critical value) · se(θ̂). The SE controls the basic width.
- ✓

  The CLT and asymptotic Normality (often for MLEs) justify many practical CIs via the pivot Z = (θ̂ − θ)/se(θ̂).
- ✓

  Use t critical values for mean CIs when σ is unknown (especially in small samples under Normal assumptions).
- ✓

  Higher confidence levels widen intervals; larger n narrows them at rate 1/√n.
- ✓

  Two-sided (1 − α) CIs correspond to two-sided hypothesis tests at level α: reject θ = θ₀ iff θ₀ is outside the CI.
- ✓

  Coverage depends on assumptions (independence, correct model, adequate sample size). Bad assumptions can lead to under-coverage (too-narrow intervals).

## Common Mistakes

- ✗

  Interpreting a 95% CI as “there is a 95% probability that θ is in this particular interval” (that’s not the frequentist meaning).
- ✗

  Confusing SD with SE: SD is variability in data; SE is variability in an estimator across samples.
- ✗

  Using z = 1.96 automatically in small samples for means with unknown σ (should often use t with df = n − 1).
- ✗

  Trusting Wald intervals near boundaries (e.g., proportions near 0 or 1) or with small n, where coverage can be poor.

## Practice

easy

You have n = 25 observations with X̄ = 80 and s = 10. Assuming approximate Normality, compute a 95% CI for μ.

**Hint:** Use a t interval: X̄ ± t\_{n−1,0.975} · s/√n with df = 24.

Show solution

se = s/√n = 10/√25 = 10/5 = 2.

Critical value: t\_{24,0.975} ≈ 2.064.

ME = 2.064 · 2 = 4.128.

CI = 80 ± 4.128 = [75.872, 84.128] ≈ [75.87, 84.13].

medium

In a survey of n = 200 people, x = 30 respond “yes.” Compute an approximate 90% Wald CI for the proportion p.

**Hint:** p̂ = x/n. Use z\_{0.95} ≈ 1.645 and se(p̂) ≈ √(p̂(1−p̂)/n).

Show solution

p̂ = 30/200 = 0.15.

se ≈ √(0.15·0.85/200) = √(0.1275/200) = √(0.0006375) ≈ 0.02525.

ME = 1.645 · 0.02525 ≈ 0.0415.

90% CI ≈ 0.15 ± 0.0415 = [0.1085, 0.1915] ≈ [0.109, 0.192].

hard

A parameter estimator θ̂ is approximately Normal with se(θ̂) = 0.8. (a) Give a 95% Wald CI in terms of θ̂. (b) What happens to the CI width if you want 99% instead?

**Hint:** Use θ̂ ± z·se with z\_{0.975} ≈ 1.96 and z\_{0.995} ≈ 2.576. Compare margins of error.

Show solution

(a) 95% CI: θ̂ ± 1.96·0.8 = θ̂ ± 1.568, i.e., [θ̂ − 1.568, θ̂ + 1.568].

(b) 99% CI: θ̂ ± 2.576·0.8 = θ̂ ± 2.0608. The half-width increases from 1.568 to 2.061 (about 31% wider), because the critical value is larger.

## Connections

- •[Central Limit Theorem](/tech-tree/central-limit-theorem/)
- •[Maximum Likelihood Estimation](/tech-tree/maximum-likelihood-estimation/)
- •[Hypothesis Testing](/tech-tree/hypothesis-testing/)
- •[Fisher Information](/tech-tree/fisher-information/)
- •[Bootstrap Methods](/tech-tree/bootstrap-methods/)
- •[Bayesian Credible Intervals](/tech-tree/bayesian-credible-intervals/)

Quality: A (4.2/5)

[← back to tree](/tech-tree/)[browse all →](/tech-tree/inventory/)
