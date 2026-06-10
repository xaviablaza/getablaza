---
title: Common Distributions
description: Bernoulli, binomial, Poisson, uniform, normal distributions.
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
source_format: html
inspiration_url: https://templeton.host/tech-tree/common-distributions/
inspiration_category: tech-tree
---

> Source-copy draft imported from [https://templeton.host/tech-tree/common-distributions/](https://templeton.host/tech-tree/common-distributions/). Names, domain references, and local media paths were adapted for Xavi Ablaza / getablaza.com.

[←Back to Tech Tree](/tech-tree/)

[inventory](/tech-tree/inventory/)[coverage](/tech-tree/coverage/)

# Common Distributions

Probability & StatisticsDifficulty: ★★☆☆☆Depth: 5Unlocks: 59

Bernoulli, binomial, Poisson, uniform, normal distributions.

## Interactive Visualization

⏮◀◀▶▶STEP0.25x1xZOOM

t=0s

## Core Concepts

- -Support type (discrete vs continuous): the set of possible X values determines whether probabilities are assigned to points (discrete) or to intervals via densities (continuous).
- -Probability function: a function that gives probability mass (PMF) for discrete or probability density (PDF) for continuous variables; used to compute P(X in A) by summation or integration.
- -Parameterized family: a distribution is specified by a small set of parameters which uniquely determine its shape and location (e.g., success probability, rate, location and scale).

## Key Symbols & Notation

theta (generic parameter set) - the parameters that define a specific distribution within a family (e.g., p, lambda, mu, sigma).

## Essential Relationships

- -Normalization: the PMF must sum to 1 and the PDF must integrate to 1 (ensures valid probability assignments).
- -Parameters map to moments: the distribution's parameters uniquely determine its mean and variance (and hence central tendency and spread).

## Prerequisites (2)

[Random Variables6 atoms](/tech-tree/random-variables/)[Variance5 atoms](/tech-tree/variance/)

## Unlocks (10)

[Maximum Likelihood Estimationlvl 3](/tech-tree/mle/)[Bayesian Inferencelvl 4](/tech-tree/bayesian-inference/)[Entropylvl 3](/tech-tree/entropy/)[Joint Distributionslvl 3](/tech-tree/joint-distributions/)[Central Limit Theoremlvl 3](/tech-tree/central-limit-theorem/)[Monte Carlo Methodslvl 4](/tech-tree/monte-carlo/)[Conjugate Priorslvl 4](/tech-tree/conjugate-priors/)[Hypothesis Testinglvl 3](/tech-tree/hypothesis-testing/)

+2 more...

## Referenced by (3)

Where this concept shows up in the operating-finance and personal-finance graphs.

### From Business (3)

[personal financeBusiness

Options pricing (Black-Scholes) assumes log-normal return distributions - options-basics is applied distribution theory](/business/personal-finance/)[Long TailBusiness

The long tail is literally the tail of a power law (Pareto) distribution - understanding heavy-tailed vs normal distributions is the mathematical foundation for why a massive volume of rare items exists and why their aggregate value is significant](/business/long-tail/)[Return DistributionBusiness

Return distributions are specific instances of probability distributions - normal, lognormal, fat-tailed. Understanding Bernoulli, binomial, and especially normal distributions is the mathematical prerequisite for modeling investment returns.](/business/return-distribution/)

Advanced Learning Details

### Graph Position

40

Depth Cost

59

Fan-Out (ROI)

27

Bottleneck Score

5

Chain Length

### Cognitive Load

6

Atomic Elements

39

Total Elements

L2

Percentile Level

L4

Atomic Level

### All Concepts (14)

- - Probability mass function (PMF): function giving P(X=k) for discrete distributions
- - Probability density function (PDF): function f(x) whose integrals give probabilities for continuous distributions
- - Cumulative distribution function (CDF): F(x)=P(X ≤ x) for any distribution
- - Support of a distribution: the set of values X can take (e.g., {0,1} or [a,b])
- - Bernoulli distribution (single trial): binary outcome X∈{0,1} with parameter p (success probability)
- - Binomial distribution (n independent Bernoulli trials): discrete counts X∈{0,...,n} with parameters n and p
- - Poisson distribution (count of rare events): discrete X∈{0,1,2,...} with rate parameter λ
- - Continuous uniform distribution on [a,b]: constant density on interval [a,b]
- - Normal (Gaussian) distribution: continuous, bell-shaped distribution specified by mean μ and variance σ^2
- - Standard normal distribution: normal distribution with μ=0 and σ^2=1
- - Standardization (Z-score): transforming X to Z=(X−μ)/σ to compare to the standard normal
- - Interpretation of parameters: p (Bernoulli/binomial) as success probability, n as number of trials, λ as expected count/rate per interval, a and b as interval endpoints for uniform, μ and σ^2 as location and scale for normal
- - Use of PMF/PDF/CDF to compute probabilities (point probabilities for discrete via PMF, interval probabilities for continuous via integrating PDF)
- - Typical shapes/properties: symmetry of normal, constant density of uniform, skewness possible in binomial/Poisson depending on parameters

### Teaching Strategy

Deep-dive lesson - accessible entry point but dense material. Use worked examples and spaced repetition.

Most of probability and statistics is built on a surprisingly small “toolbox” of distributions. Learn a handful well, and you can model coin flips, counts of arrivals, measurement noise, and uncertainty around unknown quantities—with clean formulas for probabilities, means, and variances.

TL;DR:

A distribution is a parameterized family p(x | θ) describing how a random variable X behaves. Discrete distributions use PMFs and sum to get probabilities; continuous distributions use PDFs and integrate. This lesson covers Bernoulli, binomial, Poisson (discrete) and uniform, normal (continuous), including when to use each and their key formulas.

## What Is a Common Distribution?

### Why you should care

In real problems, you rarely invent a probability model from scratch. Instead, you pick a **distribution family**—a reusable pattern—and tune a few **parameters** θ to match the situation.

Examples:

- •A single yes/no outcome → Bernoulli(p)
- •Number of successes in n trials → Binomial(n, p)
- •Count of events over time/space with a stable average rate → Poisson(λ)
- •A value equally likely anywhere in an interval → Uniform(a, b)
- •A noisy measurement that clusters around a mean → Normal(μ, σ²)

Each family gives you:

- •A **support** (what values X can take)
- •A probability function: **PMF** (discrete) or **PDF** (continuous)
- •A small set of parameters θ (like p, λ, μ, σ)
- •Closed-form formulas for mean and variance

### Support: discrete vs continuous

The first decision is the *type* of values X can take.

- •**Discrete support**: X ∈ {0, 1, 2, …} (or a finite set). Probabilities are assigned to points.
- •You use a **PMF**: p(x) = P(X = x)
- •Probabilities over sets A are sums:
- •P(X ∈ A) = ∑\_{x ∈ A} p(x)

- •**Continuous support**: X ∈ ℝ or an interval. Probabilities are assigned to intervals (points have probability 0).
- •You use a **PDF**: f(x)
- •Probabilities over intervals are integrals:
- •P(X ∈ [c, d]) = ∫ᶜᵈ f(x) dx

A common confusion: for continuous X, f(x) is not itself a probability. It’s a *density*. You must integrate over an interval.

### Parameterized families p(x | θ)

A distribution is often written as p(x | θ) (or f(x | θ)). The parameter set θ chooses one specific member of the family.

Examples of θ:

- •Bernoulli: θ = p where 0 ≤ p ≤ 1
- •Poisson: θ = λ where λ > 0
- •Normal: θ = (μ, σ²) where σ² > 0

These parameters control “location” (where the mass sits) and “scale/spread” (how variable it is).

### A quick comparison table

| Distribution | Support | Type | Parameters θ | Typical meaning |
| --- | --- | --- | --- | --- |
| Bernoulli(p) | {0, 1} | Discrete (PMF) | p | One trial: success/failure |
| Binomial(n, p) | {0, …, n} | Discrete (PMF) | n, p | # successes in n independent trials |
| Poisson(λ) | {0, 1, 2, …} | Discrete (PMF) | λ | # events in a fixed window |
| Uniform(a, b) | [a, b] | Continuous (PDF) | a, b | “Equally likely” in an interval |
| Normal(μ, σ²) | ℝ | Continuous (PDF) | μ, σ² | Measurement noise / sums / averages |

In the next sections, we’ll build each one slowly: story → support → formula → mean/variance → how to compute probabilities.

## Core Mechanic 1: Discrete Distributions (Bernoulli, Binomial, Poisson)

### Why discrete models show up everywhere

Many systems naturally produce counts:

- •Did a user click? (0/1)
- •How many defective items in a batch?
- •How many emails arrive in an hour?

Discrete distributions let you assign probability to each integer outcome and then **sum** the relevant probabilities.

---

## Bernoulli(p)

### Story

One trial. Two outcomes.

- •X = 1 means “success”
- •X = 0 means “failure”

### Support and PMF

Support: X ∈ {0, 1}

PMF:

- •P(X = 1) = p
- •P(X = 0) = 1 − p

A compact way to write the PMF is:

- •p(x | p) = pˣ (1 − p)^(1−x), for x ∈ {0, 1}

### Mean and variance

You’ll use these constantly:

- •E[X] = p
- •Var(X) = p(1 − p)

Why E[X] = p?

- •E[X] = 0·P(X=0) + 1·P(X=1) = p

---

## Binomial(n, p)

### Story

Repeat a Bernoulli trial n times, independently, with the same success probability p. Let X be the number of successes.

Examples:

- •# heads in n coin flips
- •# conversions among n visitors (with fixed conversion rate)

### Support and PMF

Support: X ∈ {0, 1, …, n}

PMF:

- •P(X = k) = (n choose k) pᵏ (1 − p)^(n−k)

Where (n choose k) = n! / (k!(n−k)!).

### Intuition for the formula

- •pᵏ (1 − p)^(n−k): probability of any *particular* sequence with k successes
- •(n choose k): number of sequences that have exactly k successes

### Mean and variance

- •E[X] = np
- •Var(X) = np(1 − p)

A useful connection (preview of CLT): if n is large, a binomial can often be approximated by a normal:

- •X ≈ Normal(np, np(1 − p))

---

## Poisson(λ)

### Story

Poisson models counts of events in a fixed window when:

- •events occur independently (approximately)
- •the average rate is stable
- •two events don’t “pile up” at exactly the same instant (in a continuous-time idealization)

Examples:

- •calls arriving at a call center per minute
- •defects per meter of wire
- •decay events per time interval

### Support and PMF

Support: X ∈ {0, 1, 2, …}

PMF:

- •P(X = k) = e^(−λ) λᵏ / k!

Here λ is both the *rate parameter* and the mean count per window.

### Mean and variance

- •E[X] = λ
- •Var(X) = λ

That “mean = variance” fact is a diagnostic: if your observed counts have variance much bigger than the mean, a plain Poisson may be too simple.

### Connection to binomial (rare events)

A classic approximation: if n is large and p is small but np stays moderate, then:

- •Binomial(n, p) ≈ Poisson(λ) with λ = np

This is the “rare events” regime.

---

## Discrete probability calculations: summing

If X is discrete, you compute:

- •P(X ∈ A) = ∑\_{x ∈ A} p(x)

Examples:

- •For Poisson: P(X ≥ 2) = 1 − P(X=0) − P(X=1)
- •For Binomial: P(X ≤ k) = ∑\_{i=0}^k (n choose i) pⁱ (1−p)^(n−i)

In practice, you often use a CDF function from software for these sums, but it’s crucial to understand what is being summed and why.

## Core Mechanic 2: Continuous Distributions (Uniform, Normal) and PDFs

### Why continuous models matter

Many measurements are not naturally integer counts:

- •time, temperature, distance, voltage, weight

Even if the world is measured with finite precision, continuous distributions are often excellent approximations and give smooth, usable mathematics.

The key mental shift:

- •For continuous X, P(X = x) = 0 for any exact x.
- •You compute probabilities by integrating a **density** over an interval.

---

## Uniform(a, b)

### Story

“All values between a and b are equally plausible.”

Examples:

- •a randomized start time between 2pm and 3pm
- •an unknown phase angle assumed equally likely in [0, 2π]

### Support and PDF

Support: X ∈ [a, b]

PDF:

- •f(x) = 1/(b − a) for a ≤ x ≤ b
- •f(x) = 0 otherwise

### Probability of an interval

For any c, d with a ≤ c ≤ d ≤ b:

P(c ≤ X ≤ d)

= ∫ᶜᵈ 1/(b − a) dx

= (d − c)/(b − a)

So probability is proportional to interval length.

### Mean and variance

- •E[X] = (a + b)/2
- •Var(X) = (b − a)² / 12

---

## Normal(μ, σ²)

### Story

The normal (Gaussian) distribution models values that cluster around an average μ with symmetric noise.

It also appears because of aggregation:

- •sums/averages of many small effects often become approximately normal (CLT)

Examples:

- •measurement error
- •heights (roughly)
- •sensor noise

### Support and PDF

Support: X ∈ ℝ

PDF:

- •f(x) = (1/(σ√(2π))) exp(−(x−μ)²/(2σ²))

Parameters:

- •μ controls the center
- •σ (or σ²) controls the spread

### Standardization (Z-scores)

A core technique is converting to the **standard normal**.

If X ∼ Normal(μ, σ²), define:

- •Z = (X − μ)/σ

Then Z ∼ Normal(0, 1).

This lets you use standard normal tables or software CDFs:

- •P(X ≤ x) = P(Z ≤ (x−μ)/σ)

### The 68–95–99.7 rule (intuition)

For X ∼ Normal(μ, σ²):

- •P(μ − σ ≤ X ≤ μ + σ) ≈ 0.68
- •P(μ − 2σ ≤ X ≤ μ + 2σ) ≈ 0.95
- •P(μ − 3σ ≤ X ≤ μ + 3σ) ≈ 0.997

This is not a definition—just a helpful memory.

---

## Continuous probability calculations: integrating

If X is continuous with PDF f:

- •P(X ∈ A) = ∫\_{x ∈ A} f(x) dx

For an interval [c, d]:

- •P(c ≤ X ≤ d) = ∫ᶜᵈ f(x) dx

For the uniform, this integral is easy.

For the normal, there is no elementary antiderivative, so we use the CDF Φ(z) numerically.

A practical comparison:

| Task | Discrete | Continuous |
| --- | --- | --- |
| Probability at a point | P(X=x) can be > 0 | P(X=x)=0 |
| Probability over a range | sum PMF values | integrate PDF |
| Typical tool | ∑ and CDF tables | ∫ and CDF Φ |

Understanding this split (support → PMF/PDF → sum/integrate) prevents many downstream mistakes in statistics and ML.

## Application/Connection: Choosing a Distribution + How This Unlocks Next Topics

### Why model choice matters

A distribution is a compact set of assumptions. Choosing one is not just “picking a formula”—it’s deciding what outcomes are possible and what patterns are likely.

A good first pass is to match the *data type* and *generative story*.

---

## Quick chooser: which distribution should I try?

| If your variable X is… | And the story is… | Start with… |
| --- | --- | --- |
| 0/1 outcome | one trial with success prob p | Bernoulli(p) |
| integer 0…n | n independent trials, constant p | Binomial(n, p) |
| nonnegative count | events in a window at average rate λ | Poisson(λ) |
| real in [a, b] | equally likely in an interval | Uniform(a, b) |
| real-valued | symmetric noise around μ | Normal(μ, σ²) |

Then sanity-check with:

- •support: does the distribution allow impossible values?
- •mean/variance: are they in the right ballpark?
- •shape: symmetric vs skewed; heavy tail vs light tail

---

## How this connects to Maximum Likelihood Estimation (MLE)

In MLE, you assume data x₁, …, xₙ came from a distribution family p(x | θ) and pick θ that makes the observed data most likely.

Examples you’ll soon see:

- •Bernoulli/Binomial: MLE for p is the sample proportion
- •Poisson: MLE for λ is the sample mean
- •Normal: MLE for μ is the sample mean, and for σ² is the sample variance (with a particular denominator choice)

To do MLE well, you must recognize which likelihood matches your data (Bernoulli vs binomial vs Poisson, etc.).

---

## How this connects to Bayesian inference

Bayesian inference updates distributions with data:

- •posterior ∝ likelihood × prior

The likelihood often comes from a “common distribution.” Examples:

- •Bernoulli likelihood + Beta prior → Beta posterior
- •Poisson likelihood + Gamma prior → Gamma posterior
- •Normal likelihood + Normal prior (for μ) → Normal posterior

Knowing the likelihood family is step 1.

---

## How this connects to joint distributions and the CLT

- •**Joint distributions**: if you have multiple random variables (X, Y), you often assume they are independent with known marginals (e.g., X ∼ Poisson(λ₁), Y ∼ Poisson(λ₂)). From there you can build joint models.
- •**Central Limit Theorem (CLT)**: sums of many independent variables often become approximately normal. That’s why normal approximations to binomial are common, and why normal noise models appear everywhere.

---

## One more pacing note: models are approximations

A distribution is rarely “true.” It’s a simplified story that is useful if:

- •it matches the support
- •it captures the main shape
- •it predicts well enough for your decision

As you learn more, you’ll add richer families, but these five are the workhorses you’ll keep returning to.

## Worked Examples (3)

### Binomial probability: at least k successes

A website A/B test shows a conversion on a visit with probability p = 0.2, assumed constant across visitors. You observe n = 5 independent visitors. Let X be the number of conversions. Compute P(X ≥ 2).

1. Identify the distribution:

   X counts successes in n independent Bernoulli trials ⇒ X ∼ Binomial(n, p) with n=5, p=0.2.
2. Use the complement to reduce work:

   P(X ≥ 2) = 1 − P(X ≤ 1)

   = 1 − (P(X=0) + P(X=1)).
3. Compute P(X=0):

   P(X=0) = (5 choose 0) (0.2)⁰ (0.8)⁵

   = 1 · 1 · 0.8⁵

   = 0.32768.
4. Compute P(X=1):

   P(X=1) = (5 choose 1) (0.2)¹ (0.8)⁴

   = 5 · 0.2 · 0.8⁴

   = 1 · 0.4096

   = 0.4096.
5. Combine:

   P(X ≤ 1) = 0.32768 + 0.4096 = 0.73728

   P(X ≥ 2) = 1 − 0.73728 = 0.26272.

**Insight:** For discrete distributions, complements often avoid long sums. Here, summing k=2,3,4,5 is more work than subtracting k=0,1 from 1.

### Poisson probability: probability of 0 or 1 event

A server receives requests at an average rate of λ = 3 requests per minute. Model the number of requests in a minute as X ∼ Poisson(3). Compute P(X ≤ 1).

1. Write the PMF:

   P(X=k) = e^(−λ) λᵏ / k! with λ = 3.
2. Compute P(X=0):

   P(X=0) = e^(−3) 3⁰ / 0!

   = e^(−3).
3. Compute P(X=1):

   P(X=1) = e^(−3) 3¹ / 1!

   = 3e^(−3).
4. Sum:

   P(X ≤ 1) = P(X=0) + P(X=1)

   = e^(−3) + 3e^(−3)

   = 4e^(−3)

   ≈ 4 · 0.049787

   ≈ 0.19915.

**Insight:** Poisson computations are often a few terms plus a small exponential factor. Also note how λ directly sets the typical count: with λ=3, getting ≤1 is fairly unlikely (~0.20).

### Uniform PDF to probability: interval length

Let X ∼ Uniform(10, 18). Compute P(12 ≤ X ≤ 15) and the mean and variance.

1. Write the PDF:

   f(x) = 1/(18−10) = 1/8 for 10 ≤ x ≤ 18.
2. Compute the probability by integrating:

   P(12 ≤ X ≤ 15) = ∫¹²¹⁵ (1/8) dx

   = (1/8)(15−12)

   = 3/8

   = 0.375.
3. Compute the mean:

   E[X] = (a+b)/2 = (10+18)/2 = 14.
4. Compute the variance:

   Var(X) = (b−a)²/12

   = (8)²/12

   = 64/12

   = 16/3

   ≈ 5.333.

**Insight:** For a uniform distribution, probabilities are purely about lengths of intervals—no calculus tricks required beyond “constant × width.”

## Key Takeaways

- ✓

  Support matters first: discrete X assigns probability to points (PMF), continuous X assigns density and uses integrals (PDF).
- ✓

  Bernoulli(p) models one 0/1 trial with E[X]=p and Var(X)=p(1−p).
- ✓

  Binomial(n, p) models a count of successes in n independent trials: P(X=k)=(n choose k)pᵏ(1−p)^(n−k), with E[X]=np and Var(X)=np(1−p).
- ✓

  Poisson(λ) models counts in a fixed window with PMF e^(−λ)λᵏ/k!, and it has E[X]=Var(X)=λ.
- ✓

  Uniform(a, b) has constant density 1/(b−a) on [a,b], with E[X]=(a+b)/2 and Var(X)=(b−a)²/12.
- ✓

  Normal(μ, σ²) models symmetric noise; standardization Z=(X−μ)/σ converts to Normal(0,1) for probability calculations.
- ✓

  Most probability queries reduce to either a sum (discrete) or an integral (continuous), often aided by complements and CDFs.

## Common Mistakes

- ✗

  Treating a PDF value f(x) as a probability (for continuous X, only integrals over intervals are probabilities).
- ✗

  Using a binomial model when trials are not independent or when p changes from trial to trial (then Binomial(n,p) is not appropriate).
- ✗

  Confusing Poisson(λ) with Binomial(n,p): Poisson is unbounded (0,1,2,…) and is about rates per window, not a fixed number of trials.
- ✗

  Mixing up σ and σ² in the normal distribution, or forgetting to divide by σ when computing a Z-score.

## Practice

easy

Let X ∼ Bernoulli(p) with p = 0.7. Compute E[X], Var(X), and P(X=0).

**Hint:** Use E[X]=p and Var(X)=p(1−p). Also P(X=0)=1−p.

Show solution

E[X]=0.7.

Var(X)=0.7(1−0.7)=0.7·0.3=0.21.

P(X=0)=1−0.7=0.3.

medium

A factory produces items with defect probability p = 0.05 independently. In a batch of n = 20 items, let X be the number of defects. Compute P(X=0) and P(X≥1).

**Hint:** Use X ∼ Binomial(20, 0.05). P(X≥1)=1−P(X=0).

Show solution

X ∼ Binomial(20,0.05).

P(X=0) = (20 choose 0)(0.05)⁰(0.95)²⁰ = 0.95²⁰ ≈ 0.3585.

P(X≥1)=1−0.95²⁰ ≈ 1−0.3585 = 0.6415.

medium

Let X ∼ Normal(μ, σ²) with μ = 100 and σ = 15. Compute P(X ≤ 130) in terms of the standard normal CDF Φ, and give a numerical approximation.

**Hint:** Convert to Z = (X−μ)/σ. Then P(X≤x)=Φ((x−μ)/σ). Use Φ(2)≈0.9772.

Show solution

Z = (X−100)/15 so Z ∼ Normal(0,1).

P(X ≤ 130) = P(Z ≤ (130−100)/15) = Φ(30/15) = Φ(2).

Numerically, Φ(2) ≈ 0.9772.

## Connections

Next nodes you can tackle:

- •[Maximum Likelihood Estimation](/tech-tree/mle/) — use p(x | θ) to fit θ from data.
- •[Bayesian Inference](/tech-tree/bayesian-inference/) — combine priors with likelihoods from these common families.
- •[Entropy](/tech-tree/entropy/) — compute uncertainty for discrete distributions like Bernoulli and Poisson.
- •[Joint Distributions](/tech-tree/joint-distributions/) — model multiple variables, independence assumptions, marginals/conditionals.
- •[Central Limit Theorem](/tech-tree/central-limit-theorem/) — explains why normal approximations appear so often.

Quality: B (3.8/5)

[← back to tree](/tech-tree/)[browse all →](/tech-tree/inventory/)
