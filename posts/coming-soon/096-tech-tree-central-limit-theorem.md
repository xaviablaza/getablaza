---
title: Central Limit Theorem
description: Sum of many random variables approaches normal distribution.
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
permalink: /tech-tree/central-limit-theorem/
---

[←Back to Tech Tree](/tech-tree/)

[inventory](/tech-tree/inventory/)[coverage](/tech-tree/coverage/)

# Central Limit Theorem

Probability & StatisticsDifficulty: ★★★☆☆Depth: 6Unlocks: 3

Sum of many random variables approaches normal distribution.

## Interactive Visualization

⏮◀◀▶▶STEP0.25x1xZOOM

t=0s

## Core Concepts

- -Standardization: center the sum by its mean and scale by its standard deviation times sqrt(n) (to obtain a nondegenerate limit)
- -Universal Gaussian limit: the distribution of the standardized sum approaches the standard normal as sample size grows
- -Applicability conditions: variables are independent (or suitably weakly dependent) and have finite variance

## Key Symbols & Notation

Z\_n = (sum\_{i=1}^n X\_i - n \* mu) / (sigma \* sqrt(n)) (standardized sum)N(0,1) (standard normal distribution)

## Essential Relationships

- -Z\_n converges in distribution to N(0,1) as n -> infinity under the applicability conditions

## Prerequisites (2)

[Common Distributions6 atoms](/tech-tree/common-distributions/)[Law of Large Numbers5 atoms](/tech-tree/law-large-numbers/)

## Unlocks (3)

[Hypothesis Testinglvl 3](/tech-tree/hypothesis-testing/)[Confidence Intervalslvl 3](/tech-tree/confidence-intervals/)[Concentration Inequalitieslvl 5](/tech-tree/concentration-inequalities/)

## Referenced by (1)

Where this concept shows up in the operating-finance and personal-finance graphs.

### From Money (1)

[Index FundsMoney

Broad diversification stabilizes returns via the central limit theorem](/money/index-funds/)

Advanced Learning Details

### Graph Position

62

Depth Cost

3

Fan-Out (ROI)

3

Bottleneck Score

6

Chain Length

### Cognitive Load

6

Atomic Elements

29

Total Elements

L1

Percentile Level

L4

Atomic Level

### All Concepts (11)

- - Asymptotic normality: the distribution of a suitably normalized sum (or mean) of many random variables approaches a normal distribution as sample size n → ∞
- - Standardization/normalization for CLT: subtract the sum's mean and divide by its standard deviation (scale ~√n) before taking the limit
- - Convergence in distribution (weak convergence): a mode of convergence describing convergence of cumulative distribution functions rather than pointwise values or probabilities
- - Conditions for CLT applicability: typical assumptions such as independence (or weak dependence), identical distribution (i.i.d.) OR more general Lindeberg/Feller conditions, and finite variance
- - Scaling of fluctuations: random fluctuations around the mean are O(1/√n) (standard error) rather than O(1), so variability shrinks with √n
- - Universality/robustness: the limiting normal distribution does not depend on the detailed shape of the original distribution (provided conditions hold)
- - Approximation versus exactness: for finite n the sum/mean is generally not exactly normal; normality is an asymptotic approximation
- - Relationship to finite-sample approximations: how discrete distributions (e.g., binomial, Poisson) can be approximated by normal for large parameters via the CLT
- - Rate of convergence and error bounds (qualitative): there are quantitative bounds (e.g., Berry–Esseen) that control how quickly the distribution approaches normal depending on higher moments
- - Role of characteristic functions or moment-generating functions as a standard proof/analysis tool to show convergence of distributions
- - Stability property perspective: the normal distribution is a stable attractor under summation (convolution) of many independent contributions

### Teaching Strategy

Multi-session curriculum - substantial prior knowledge and complex material. Use mastery gates and deliberate practice.

You flip a biased coin 10 times and count heads: the result is messy and discrete. You flip it 10,000 times, and suddenly the count (after the right centering and scaling) behaves like a smooth bell curve—even though each flip is just 0 or 1. The Central Limit Theorem (CLT) explains why “bell curves” appear everywhere: sums and averages of many small, mostly independent random effects tend to look normal.

TL;DR:

If X₁, …, Xₙ are i.i.d. with mean μ and finite variance σ², then the standardized sum Zₙ = (∑ᵢ Xᵢ − nμ)/(σ√n) converges in distribution to N(0,1). Equivalently, the standardized sample mean √n( X̄ₙ − μ )/σ → N(0,1). This enables normal approximations for many non-normal problems and is the backbone of hypothesis tests and confidence intervals.

## What Is the Central Limit Theorem?

### Why this theorem exists (motivation)

A single random variable can have almost any shape: discrete spikes (binomial), heavy tails, skewness, or bounded support (uniform). Yet, in practice, **aggregates**—totals, averages, measurement errors, queueing delays, polling percentages—often look approximately normal.

The CLT is the mathematical statement behind this phenomenon. It says: if you add up many independent (or weakly dependent) random variables with finite variance, then after you **center** and **scale** the sum correctly, the distribution becomes close to a normal distribution.

This matters because:

- •Normal distributions are easy to work with (tables, z-scores, quantiles).
- •Many statistical procedures assume approximate normality of an estimator.
- •It gives a universal approximation even when the original data are not normal.

### The core statement (classic i.i.d. version)

Let X₁, X₂, … be i.i.d. random variables with

- •E[Xᵢ] = μ
- •Var(Xᵢ) = σ², with 0 < σ² < ∞

Define the **standardized sum**

Zₙ = ( (∑ᵢ₌₁ⁿ Xᵢ) − nμ ) / (σ√n).

The **Central Limit Theorem** says:

Zₙ ⇒ N(0,1) as n → ∞,

where “⇒” means **converges in distribution**.

### Equivalent view: the sample mean

Since X̄ₙ = (1/n)∑ᵢ Xᵢ, we can rewrite Zₙ in terms of X̄ₙ:

Zₙ = (n X̄ₙ − nμ)/(σ√n)

= √n (X̄ₙ − μ)/σ.

So the CLT can be remembered as:

√n (X̄ₙ − μ) / σ ⇒ N(0,1).

This is the form you’ll use constantly in statistics.

### “Approaches normal” does not mean “becomes normal”

For any finite n, the distribution of a sum may still be discrete (e.g., binomial). The CLT says that **as n grows**, the standardized distribution gets closer and closer to the continuous N(0,1) curve.

### CLT vs Law of Large Numbers (LLN)

You already know the LLN: X̄ₙ → μ (in probability) as n grows. The LLN answers: *Where does X̄ₙ go?*

The CLT answers a deeper question: *How does X̄ₙ fluctuate around μ for large n?* It says those fluctuations are roughly normal with typical size σ/√n.

A useful mental picture:

- •LLN: the dart lands near the bullseye.
- •CLT: the “cloud” of dart hits around the bullseye is approximately a 2D Gaussian (in 1D here: bell curve), with radius shrinking like 1/√n.

### The nondegenerate limit idea

If you don’t scale correctly, you get trivial limits:

- •∑ᵢ Xᵢ typically grows like n, so it “blows up.”
- •X̄ₙ converges to μ, so it “collapses to a point.”

The CLT’s scaling √n is the special choice that makes the limit distribution neither explode nor collapse.

## Core Mechanic 1: Standardization (Centering and Scaling)

### Why standardization is the heart of the CLT

Different problems have different units, means, and variances. The CLT is “universal” only after we remove those superficial differences.

Standardization does two things:

1) **Centering**: subtract the mean so the distribution is centered at 0.

2) **Scaling**: divide by the standard deviation so the spread is comparable across problems.

But for sums/means, there’s an extra subtlety: the variance changes with n.

### Compute the mean and variance of a sum

Let Sₙ = ∑ᵢ₌₁ⁿ Xᵢ.

Assuming independence and identical distribution:

E[Sₙ] = E[∑ᵢ Xᵢ]

= ∑ᵢ E[Xᵢ]

= ∑ᵢ μ

= nμ.

Var(Sₙ) = Var(∑ᵢ Xᵢ)

= ∑ᵢ Var(Xᵢ) (independence)

= ∑ᵢ σ²

= nσ².

So the standard deviation of Sₙ is √(nσ²) = σ√n.

### Why divide by σ√n?

If we look at the centered sum Sₙ − nμ, its variance is still nσ². As n grows, that variance grows without bound.

To compare distributions across n, we scale it down:

Zₙ = (Sₙ − nμ)/(σ√n).

Then:

E[Zₙ] = E[Sₙ − nμ]/(σ√n)

= 0.

Var(Zₙ) = Var(Sₙ − nμ)/(σ² n)

= Var(Sₙ)/(σ² n)

= (nσ²)/(σ² n)

= 1.

So Zₙ always has mean 0 and variance 1. The CLT says: not only are the first two moments normalized, but the *whole distribution* tends to N(0,1).

### Standardizing the mean directly

Since X̄ₙ has

E[X̄ₙ] = μ,

Var(X̄ₙ) = Var(Sₙ/n) = Var(Sₙ)/n² = (nσ²)/n² = σ²/n,

the standard deviation of X̄ₙ is σ/√n.

Thus the natural z-score for the mean is:

( X̄ₙ − μ ) / (σ/√n) = √n (X̄ₙ − μ)/σ.

This is exactly Zₙ.

### What if σ is unknown?

In real data, σ is usually unknown. You replace it with the sample standard deviation s, producing the **studentized** statistic:

Tₙ = √n (X̄ₙ − μ)/s.

For normal data, Tₙ follows a t-distribution exactly. For non-normal data, Tₙ is approximately normal for large n (and more refined results connect it to t under certain conditions). In practice, the CLT justifies using normal-based inference when n is large enough.

### A small but important interpretation

Standardization doesn’t magically make data normal. It makes different n comparable and reveals the limiting bell curve behavior.

Think of Zₙ as asking:

> “How many standard deviations away from its mean is the sum/mean?”

That is exactly what a z-score measures.

## Core Mechanic 2: Universal Gaussian Limit and Conditions

### What “universal” means here

The stunning part of the CLT is that it does not care much about the original distribution’s shape.

- •Xᵢ could be Bernoulli(0.3), exponential, uniform, Poisson, a weird custom distribution…
- •As long as the conditions hold, Zₙ tends to N(0,1).

That’s why the normal distribution shows up in so many unrelated domains: it’s the **attractor** for standardized sums.

### What convergence in distribution means (practical definition)

Zₙ ⇒ Z means:

For all real x where the CDF of Z is continuous,

P(Zₙ ≤ x) → P(Z ≤ x).

Here Z ~ N(0,1). Practically: probabilities you compute using Zₙ become close to those computed using a standard normal.

### Applicability conditions (the “fine print”)

The node’s atomic concepts highlight the key assumptions. In the classic version:

1) **Independence** (or weak dependence)

- •Independence makes Var(Sₙ) add nicely.
- •Many extensions allow weak dependence (mixing conditions, martingale CLTs), but as a first rule: *strong correlations can break the CLT*.

2) **Finite variance**

- •If Var(Xᵢ) = ∞ (heavy tails), the classical CLT can fail.
- •Then sums may converge (after different scaling) to a stable non-Gaussian distribution (Lévy α-stable laws).

3) **No single term dominates** (for non-identical variables)

Even if variables aren’t identically distributed, a CLT can still hold if each term is “small” relative to the whole sum.

A common sufficient framework (informal):

- •Xᵢ are independent,
- •E[Xᵢ] exists,
- •∑ Var(Xᵢ) grows to infinity,
- •no single Var(Xᵢ) is a huge fraction of the total variance.

This is captured formally by Lindeberg or Lyapunov conditions.

### How large must n be?

The CLT is asymptotic. In finite samples, approximation quality depends on:

- •skewness and tail heaviness of Xᵢ,
- •how close p is to 0 or 1 for Bernoulli,
- •whether the distribution is bounded or heavy-tailed.

Rule-of-thumb guidance (not a theorem):

- •Often n ≈ 30 is “okay” for mild distributions.
- •For very skewed/heavy-tailed distributions, you may need much larger n.
- •For Bernoulli/binomial, a classic condition for normal approximation is np ≥ 10 and n(1−p) ≥ 10.

### CLT is about shape, not about tail guarantees

The CLT tells you the standardized distribution tends to normal, but it does not always give sharp finite-n tail bounds.

That’s why another node you’ll unlock—[Concentration Inequalities](/tech-tree/concentration-inequalities/)—is important. Concentration gives explicit finite-n bounds (often exponential) under boundedness or sub-Gaussian assumptions.

### Quick comparison: CLT vs other approximations

| Goal | Tool | What you get | Typical assumptions |
| --- | --- | --- | --- |
| Approximate distribution of sums/means | CLT | Asymptotic N(0,1) | independence, finite variance |
| Exact distribution for normal samples | t / χ² / F theory | exact finite-n | underlying normality |
| Explicit finite-n tail bounds | Hoeffding/Chernoff | non-asymptotic bounds | bounded/sub-exponential |
| Better finite-n normal approximation | Berry–Esseen | error rate O(1/√n) | finite third absolute moment |

### Berry–Esseen (a helpful refinement)

A common quantitative refinement (informal statement): if E[|Xᵢ − μ|³] is finite, then the CLT approximation error is at most C·(E|X−μ|³)/(σ³√n) for a universal constant C.

You don’t need the formula to use the idea: **more skew/heavier tails ⇒ slower convergence**.

## Application/Connection: Using the CLT for Normal Approximations and Inference

### Why applications are the point

The CLT is powerful because it converts complicated sampling distributions into something you can compute with: the standard normal.

The main workflow:

1) Identify the statistic as a sum or mean of many contributions.

2) Compute μ and σ² of each contribution.

3) Standardize with √n.

4) Approximate with N(0,1).

### Normal approximation to the sample mean

If X̄ₙ is the average of i.i.d. data with mean μ and variance σ², then for large n:

X̄ₙ ≈ N( μ, σ²/n ).

That is shorthand for:

P(X̄ₙ ≤ x) ≈ Φ( (x − μ)/(σ/√n) ),

where Φ is the standard normal CDF.

### Normal approximation to the binomial (classic example)

If Y ~ Binomial(n, p), then Y = ∑ᵢ Bᵢ with Bᵢ ~ Bernoulli(p).

Here:

μ = p,

σ² = p(1−p).

So:

(Y − np)/√(np(1−p)) ⇒ N(0,1).

Equivalently, for large n:

Y ≈ N( np, np(1−p) ).

Because binomial is discrete, practitioners often use a **continuity correction** (shift by 0.5) to improve accuracy:

P(Y ≤ k) ≈ P( Normal(np, np(1−p)) ≤ k + 0.5 ).

### Measurement error and “sum of small effects”

Suppose a sensor reading is affected by many tiny independent noise sources: thermal noise, quantization, timing jitter, etc. Each noise source may not be normal, but the total error is a sum.

The CLT predicts the total error distribution is approximately normal after aggregation—one reason Gaussian noise models are so common.

### Connection to hypothesis testing

In hypothesis testing, you often form a statistic that (after standardization) is approximately N(0,1) under the null.

Example pattern:

- •Null: E[X] = μ₀
- •Test statistic: Z = √n (X̄ₙ − μ₀)/σ
- •Under H₀, Z ≈ N(0,1)

Then p-values come from normal tail areas.

This leads directly to [Hypothesis Testing](/tech-tree/hypothesis-testing/).

### Connection to confidence intervals

A (1−α) confidence interval for μ often comes from:

X̄ₙ ± z\_{1−α/2} · (σ/√n),

where z\_{1−α/2} is a standard normal quantile.

When σ is unknown, replace σ with s and often use t-quantiles; asymptotically, z and t are similar.

This leads directly to [Confidence Intervals](/tech-tree/confidence-intervals/).

### When CLT is not enough

If you need guaranteed tail probabilities for finite n (e.g., in algorithms, reliability, risk bounds), CLT approximations may be too loose.

That motivates [Concentration Inequalities](/tech-tree/concentration-inequalities/), which provide bounds like:

P(|X̄ₙ − μ| ≥ ε) ≤ 2 exp(−2nε²/(b−a)²)

for bounded variables (Hoeffding). Different goal: not approximate the whole distribution, but bound tails.

### A practical checklist

Before using CLT-based normal approximations, ask:

- •Is the statistic a sum/average of many pieces?
- •Are pieces roughly independent (or not too correlated)?
- •Is variance finite and not dominated by rare huge outliers?
- •Is n large enough given skewness/tails?
- •If discrete, should you use continuity correction?

If the answers are mostly yes, CLT is a strong tool.

## Worked Examples (3)

### Normal approximation for a binomial probability (with continuity correction)

Let Y ~ Binomial(n = 200, p = 0.40). Approximate P(Y ≥ 90) using the CLT (normal approximation) with continuity correction.

1. Identify Y as a sum of Bernoulli trials: Y = ∑ᵢ₌₁²⁰⁰ Bᵢ with Bᵢ ∈ {0,1}, E[Bᵢ]=p, Var(Bᵢ)=p(1−p).
2. Compute mean and variance:

   μ\_Y = np = 200·0.40 = 80

   σ²\_Y = np(1−p) = 200·0.40·0.60 = 48

   So σ\_Y = √48 ≈ 6.928.
3. Apply continuity correction for “≥ 90”:

   P(Y ≥ 90) = P(Y ≥ 90.0) ≈ P(N ≥ 89.5)

   where N ~ Normal(80, 48).
4. Standardize:

   Z = (N − 80)/√48 ~ N(0,1)

   So

   P(N ≥ 89.5) = P( (N−80)/√48 ≥ (89.5−80)/√48 )

   = P( Z ≥ 9.5/6.928 ).
5. Compute the z-score:

   z ≈ 9.5 / 6.928 ≈ 1.371.
6. Use standard normal tails:

   P(Z ≥ 1.371) = 1 − Φ(1.371).

   Numerically, Φ(1.37) ≈ 0.915.

   So P(Y ≥ 90) ≈ 1 − 0.915 = 0.085 (about 8.5%).

**Insight:** Even though Y is discrete, its standardized form is close to normal when n is large and both np and n(1−p) are not small. The continuity correction (89.5 instead of 90) often noticeably improves accuracy.

### Sampling distribution of the mean and a CLT-based probability

Suppose X₁,…,Xₙ are i.i.d. with mean μ = 10 and standard deviation σ = 4 (distribution not necessarily normal). For n = 64, approximate P(X̄ₙ ≤ 9).

1. Recognize this is a sample mean problem. By the CLT:

   Zₙ = √n (X̄ₙ − μ)/σ ⇒ N(0,1).
2. Compute the standard deviation of the mean:

   SD(X̄ₙ) = σ/√n = 4/√64 = 4/8 = 0.5.
3. Approximate X̄ₙ as normal:

   X̄ₙ ≈ N( μ, σ²/n ) = N(10, 16/64) = N(10, 0.25).
4. Convert the probability to a standard normal:

   P(X̄ₙ ≤ 9)

   ≈ P( (X̄ₙ − 10)/0.5 ≤ (9 − 10)/0.5 )

   = P( Z ≤ −2 ).
5. Read from normal tables:

   P(Z ≤ −2) ≈ 0.0228.

**Insight:** The LLN says X̄ₙ gets close to 10; the CLT quantifies “close” by giving an approximate bell curve with width 0.5. The √n scaling is why uncertainty shrinks like 1/√n.

### Deriving Zₙ carefully from sums to show the √n scaling

Let X₁,…,Xₙ be i.i.d. with mean μ and variance σ². Show how Zₙ arises naturally from mean/variance calculations.

1. Start with the sum Sₙ = ∑ᵢ₌₁ⁿ Xᵢ.
2. Compute its expectation:

   E[Sₙ] = E[∑ᵢ Xᵢ]

   = ∑ᵢ E[Xᵢ]

   = ∑ᵢ μ

   = nμ.
3. Compute its variance using independence:

   Var(Sₙ) = Var(∑ᵢ Xᵢ)

   = ∑ᵢ Var(Xᵢ)

   = ∑ᵢ σ²

   = nσ².
4. Center and scale to make mean 0 and variance 1:

   Zₙ = (Sₙ − E[Sₙ]) / √Var(Sₙ)

   = (Sₙ − nμ)/√(nσ²)

   = (∑ᵢ Xᵢ − nμ)/(σ√n).
5. Rewrite via the sample mean X̄ₙ:

   Zₙ = (nX̄ₙ − nμ)/(σ√n)

   = √n (X̄ₙ − μ)/σ.

**Insight:** The CLT’s formula is not arbitrary: dividing by σ√n is exactly “subtract the mean and divide by the standard deviation.” The only new twist is that the standard deviation of a sum grows like √n.

## Key Takeaways

- ✓

  CLT (i.i.d. version): Zₙ = (∑ᵢ Xᵢ − nμ)/(σ√n) ⇒ N(0,1) when E[Xᵢ]=μ and Var(Xᵢ)=σ²∈(0,∞).
- ✓

  Equivalent mean form: √n (X̄ₙ − μ)/σ ⇒ N(0,1), so X̄ₙ is approximately N(μ, σ²/n) for large n.
- ✓

  Standardization is essential: center by the mean and scale by the standard deviation; √n appears because Var(∑)=nσ².
- ✓

  The CLT explains why normal distributions appear as aggregates of many small independent effects, even when individual terms are not normal.
- ✓

  Conditions matter: independence (or weak dependence) and finite variance are key; heavy-tailed infinite-variance variables can break the classical CLT.
- ✓

  CLT is asymptotic: approximation quality depends on n and on skewness/tails; continuity correction helps for discrete sums like binomial.
- ✓

  CLT underpins normal-approximation inference, leading directly to z-tests, t-tests (with studentization), and confidence intervals.

## Common Mistakes

- ✗

  Confusing LLN with CLT: LLN says X̄ₙ → μ; CLT describes the (approximately normal) fluctuations of X̄ₙ around μ scaled by √n.
- ✗

  Forgetting the √n scaling (or scaling by n instead): using the wrong scale makes the limit degenerate (collapse to a point) or divergent.
- ✗

  Applying CLT blindly when variance is infinite or data are extremely heavy-tailed/outlier-prone; the normal approximation may be very poor or invalid.
- ✗

  Ignoring dependence: strong correlations can invalidate the standard CLT and lead to very different behavior.

## Practice

easy

Let Y ~ Binomial(n = 100, p = 0.5). Use a CLT normal approximation with continuity correction to approximate P(Y ≤ 60).

**Hint:** Approximate Y by N(np, np(1−p)). Use k+0.5 for P(Y ≤ k). Standardize to a Z score.

Show solution

Mean μ = np = 50. Variance σ² = np(1−p) = 25, so σ = 5.

Continuity correction:

P(Y ≤ 60) ≈ P(N ≤ 60.5) where N ~ N(50,25).

Standardize:

Z = (60.5 − 50)/5 = 10.5/5 = 2.1.

So P(Y ≤ 60) ≈ Φ(2.1) ≈ 0.982.

medium

A population has mean μ = 3 and standard deviation σ = 12 (distribution unknown but finite variance). For n = 144, approximate P(|X̄ₙ − 3| ≥ 2) using the CLT.

**Hint:** Use X̄ₙ ≈ N(μ, σ²/n). Convert the event to a standard normal tail probability.

Show solution

SD(X̄ₙ) = σ/√n = 12/√144 = 12/12 = 1.

Approximate X̄ₙ ≈ N(3,1²).

We want P(|X̄ₙ − 3| ≥ 2) = P(X̄ₙ ≤ 1 or X̄ₙ ≥ 5).

Standardize with Z = (X̄ₙ − 3)/1:

P(|Z| ≥ 2) = 2·P(Z ≥ 2).

Using normal tables: P(Z ≥ 2) ≈ 0.0228.

So probability ≈ 2·0.0228 = 0.0456.

medium

Suppose X₁,…,Xₙ are i.i.d. with E[Xᵢ]=μ and Var(Xᵢ)=σ². Define Sₙ = ∑ᵢ Xᵢ. Show that the standardized sum Zₙ = (Sₙ − nμ)/(σ√n) has mean 0 and variance 1.

**Hint:** Use linearity of expectation and (under independence) additivity of variance. Remember Var(aY)=a²Var(Y).

Show solution

E[Zₙ] = E[Sₙ − nμ]/(σ√n) = (E[Sₙ] − nμ)/(σ√n).

But E[Sₙ] = ∑ᵢ E[Xᵢ] = nμ, so E[Zₙ]=0.

For variance:

Var(Zₙ) = Var(Sₙ − nμ)/(σ² n) = Var(Sₙ)/(σ² n).

Independence implies Var(Sₙ)=∑ᵢ Var(Xᵢ)=nσ².

So Var(Zₙ) = (nσ²)/(σ² n)=1.

## Connections

Unlocks and next steps:

- •[Hypothesis Testing](/tech-tree/hypothesis-testing/): CLT justifies z-statistics and asymptotic null distributions.
- •[Confidence Intervals](/tech-tree/confidence-intervals/): CLT yields X̄ₙ ± z·σ/√n style intervals (and motivates t-intervals).
- •[Concentration Inequalities](/tech-tree/concentration-inequalities/): complements CLT with finite-n tail bounds.

Related reinforcement nodes (conceptual):

- •[Law of Large Numbers](/tech-tree/law-of-large-numbers/): CLT refines LLN by describing fluctuation scale and shape.
- •[Normal Distribution](/tech-tree/normal-distribution/): CLT explains why N(0,1) appears as the universal limit for standardized sums.

Quality: A (4.5/5)

[← back to tree](/tech-tree/)[browse all →](/tech-tree/inventory/)
