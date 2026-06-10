---
title: Maximum Likelihood Estimation
description: Finding parameters that maximize probability of observed data.
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
permalink: /tech-tree/mle/
---

[←Back to Tech Tree](/tech-tree/)

[inventory](/tech-tree/inventory/)[coverage](/tech-tree/coverage/)

# Maximum Likelihood Estimation

Probability & StatisticsDifficulty: ★★★☆☆Depth: 6Unlocks: 44

Finding parameters that maximize probability of observed data.

## Interactive Visualization

⏮◀◀▶▶STEP0.25x1xZOOM

t=0s

## Core Concepts

- -Likelihood function: the joint probability (pmf) or density (pdf) of the observed data viewed as a function of the parameter(s) with the data fixed.
- -Maximum-likelihood principle: the MLE is the parameter value that maximizes the likelihood function (a point estimate chosen to make the observed data most probable).
- -Score / first-order condition: internal maximizers satisfy that the derivative (gradient) of the log-likelihood with respect to the parameter equals zero (score = 0).

## Key Symbols & Notation

theta - the parameter (scalar or vector) being estimated.L(theta) - the likelihood function: the joint probability/density of the observed data expressed as a function of theta.

## Essential Relationships

- -argmax\_theta L(theta) = argmax\_theta log L(theta): the logarithm is monotone so maximizing log-likelihood gives the same estimator and simplifies products to sums.

## Prerequisites (2)

[Common Distributions6 atoms](/tech-tree/common-distributions/)[Derivatives6 atoms](/tech-tree/derivatives-basic/)

## Unlocks (6)

[Machine Learning Introductionlvl 3](/tech-tree/ml-intro/)[Bayesian Inferencelvl 4](/tech-tree/bayesian-inference/)[Logistic Regressionlvl 3](/tech-tree/logistic-regression/)[KL Divergencelvl 4](/tech-tree/kl-divergence/)[Confidence Intervalslvl 3](/tech-tree/confidence-intervals/)[Cross-Validationlvl 4](/tech-tree/cross-validation/)

Advanced Learning Details

### Graph Position

68

Depth Cost

44

Fan-Out (ROI)

20

Bottleneck Score

6

Chain Length

### Cognitive Load

6

Atomic Elements

32

Total Elements

L1

Percentile Level

L4

Atomic Level

### All Concepts (13)

- - Likelihood function: viewing the probability or density of observed data as a function of the model parameter(s) (data fixed, parameter variable)
- - Log-likelihood: the natural logarithm of the likelihood used to simplify calculations
- - Maximum likelihood estimator (MLE): the parameter value(s) that maximize the likelihood/log-likelihood
- - IID-product form of the likelihood for independent observations: the joint likelihood is the product of individual densities/probabilities
- - Use of the log to convert the product-form likelihood into a sum (computational/numerical simplification)
- - Score function: the derivative(s) of the log-likelihood with respect to parameter(s)
- - Likelihood equations: setting the score(s) to zero to obtain candidate MLE(s)
- - Observed information: the negative second derivative (Hessian) of the log-likelihood at a parameter value (measures curvature)
- - Fisher information: the expected information (expected value of the observed information or variance of the score)
- - Approximate variance/standard error of an MLE obtained from (observed or Fisher) information
- - Invariance property of MLE: the MLE of a function g(θ) is g(θ̂)
- - Practical issues for MLE: existence/non-uniqueness, boundary solutions, and need to check second-order conditions for maxima
- - Distinction in role between 'likelihood as a function of parameters' and 'probability/density as a function of data'

### Teaching Strategy

Multi-session curriculum - substantial prior knowledge and complex material. Use mastery gates and deliberate practice.

You’ve collected data. You believe it came from a distribution with some unknown parameter θ. Maximum Likelihood Estimation (MLE) is the idea of choosing θ so that, under your model, the data you actually saw would be as probable as possible.

TL;DR:

Fix the observed data and view the joint pmf/pdf as a function of θ: L(θ). The MLE is θ̂ = argmaxθ L(θ). In practice we maximize the log-likelihood ℓ(θ) = log L(θ), and interior optima satisfy the score equation ∇θ ℓ(θ) = 0 (plus a second-order/endpoint check).

## What Is Maximum Likelihood Estimation?

### The problem MLE is trying to solve (why)

In statistics and machine learning, we often start with a *model family*—a distribution we think could plausibly generate our data, but with unknown parameter(s). Examples:

- •Bernoulli(p) for binary outcomes (unknown p)
- •Poisson(λ) for counts (unknown λ)
- •Normal(μ, σ²) for measurements (unknown μ and/or σ²)

You then observe data: x₁, x₂, …, xₙ. The central question is:

> Which parameter value θ makes these observations most plausible under the model?

MLE answers: choose the θ that maximizes the probability (for discrete) or density (for continuous) of what you observed.

### Likelihood vs probability (intuition)

This is the most important mental switch:

- •**Probability/density**: treat θ as fixed, data as random.
- •**Likelihood**: treat the observed data as fixed, and treat θ as the variable.

Formally, suppose the data are generated i.i.d. from a distribution with pmf/pdf f(x | θ). After you observe x₁, …, xₙ, define the **likelihood function**

L(θ) = ∏ᵢ f(xᵢ | θ)

This is not “the probability of θ”. It is a function that scores different θ values by how well they explain the observed data.

### A concrete picture

Imagine coin flips: xᵢ ∈ {0, 1}, where 1 = heads. If you see 9 heads out of 10 flips, then:

- •p = 0.9 should give a high likelihood
- •p = 0.1 should give a very low likelihood

The MLE picks the p that yields the highest L(p).

### Definition: maximum-likelihood estimator

The **maximum likelihood estimator** (MLE) is

θ̂ = argmaxθ L(θ)

Often θ is scalar, but in many ML models θ is a vector **θ** (weights). Then we write

**θ̂** = argmax\_{**θ**} L(**θ**)

### Why we often maximize log-likelihood instead

L(θ) is a product of many terms. Products can be:

- •numerically tiny (underflow)
- •algebraically messy

Because log is strictly increasing, maximizing L(θ) is equivalent to maximizing the **log-likelihood**:

ℓ(θ) = log L(θ) = log(∏ᵢ f(xᵢ | θ))

Use log rules:

ℓ(θ)

= log(∏ᵢ f(xᵢ | θ))

= ∑ᵢ log f(xᵢ | θ)

So MLE becomes:

θ̂ = argmaxθ ℓ(θ)

This “sum of per-example contributions” is one reason likelihood-based methods scale well to large datasets.

### When MLE is a modeling commitment

MLE is only as good as the model family f(x | θ). If the model is wrong (e.g., assuming normality for heavy-tailed data), the MLE still returns the best-fitting θ *within that family*—but it may not be a good description of reality. This is not a flaw of calculus; it’s the consequence of the assumptions.

## Core Mechanic 1: Building the Likelihood (and Log-Likelihood)

### Start from a generative story (why)

To write down a likelihood, you need a story for how the data are generated. The story is the distribution f(x | θ).

Typical assumptions:

1. 1)**Independence**: xᵢ’s do not influence each other given θ.
2. 2)**Identical distribution**: all xᵢ share the same parameter θ.

These are simplifying assumptions, but they give the clean factorization:

L(θ) = f(x₁, …, xₙ | θ) = ∏ᵢ f(xᵢ | θ)

If independence is not justified (time series, spatial data), the likelihood changes form—but the MLE principle is the same.

### Discrete vs continuous: pmf vs pdf

- •If x is discrete (Bernoulli, Poisson), f(x | θ) is a **pmf** and L(θ) is a true probability.
- •If x is continuous (Normal), f(x | θ) is a **pdf** and L(θ) is a density value (not a probability of an exact point). You can still maximize it.

### Likelihood is not bounded by 1

A common surprise: densities can exceed 1, so L(θ) can exceed 1. That’s fine. Only probabilities must be ≤ 1.

### The log-likelihood decomposes nicely

With i.i.d. data:

ℓ(θ) = ∑ᵢ log f(xᵢ | θ)

This gives you:

- •easier differentiation
- •easier numerical optimization
- •an “average loss” viewpoint: (1/n)ℓ(θ)

In machine learning, we often *minimize* negative log-likelihood (NLL):

NLL(θ) = −ℓ(θ) = −∑ᵢ log f(xᵢ | θ)

### A helpful comparison table

| Object | Notation | Data treated as | Parameter treated as | Typical use |
| --- | --- | --- | --- | --- |
| pmf/pdf | f(x | θ) | random | fixed | forward probabilities/densities |
| likelihood | L(θ) = ∏ᵢ f(xᵢ | θ) | fixed (observed) | variable | estimation |
| log-likelihood | ℓ(θ) = ∑ᵢ log f(xᵢ | θ) | fixed | variable | calculus/optimization |
| negative log-likelihood | −ℓ(θ) | fixed | variable | ML loss minimization |

### A note on vector parameters

If θ is a vector **θ** ∈ ℝᵈ, then:

- •the likelihood is L(**θ**)
- •the log-likelihood is ℓ(**θ**)
- •derivatives become gradients ∇\_{**θ**} ℓ(**θ**)

The geometry matters: you’re maximizing a surface over ℝᵈ, not a curve over ℝ.

## Core Mechanic 2: Maximizing the Log-Likelihood (Score and Conditions)

### Why calculus enters (why)

Once you have ℓ(θ), estimation becomes an optimization problem. For many classical distributions, you can solve it analytically by taking derivatives and setting them to zero.

The key idea: an interior maximum of a differentiable function has derivative 0.

### The score function (first-order condition)

Define the **score** as the derivative (or gradient) of the log-likelihood:

- •Scalar θ: s(θ) = dℓ(θ)/dθ
- •Vector **θ**: **s**(**θ**) = ∇\_{**θ**} ℓ(**θ**)

**First-order condition (FOC)** for an interior optimum:

s(θ̂) = 0

(or **s**(**θ̂**) = **0**)

This gives candidate solutions.

### Second-order condition (is it a max?)

Setting the derivative to zero finds critical points: maxima, minima, or saddle points.

- •Scalar θ: check d²ℓ(θ)/dθ² < 0 at θ̂ for a local maximum.
- •Vector **θ**: check the Hessian **H**(**θ**) = ∇²\_{**θ**} ℓ(**θ**). A sufficient condition for a strict local maximum is that **H**(**θ̂**) is negative definite.

### Boundary solutions matter

Sometimes the maximum occurs at the boundary of the parameter space.

Example: Bernoulli p must satisfy 0 ≤ p ≤ 1. If all outcomes are 1, the likelihood increases as p → 1, so the MLE is p̂ = 1 (a boundary point). In that case, the derivative-based interior condition may not apply.

### Why log-likelihood often yields simple equations

Because log turns products into sums, differentiation typically yields sums you can simplify.

A pattern you’ll see repeatedly:

1. 1)Write ℓ(θ) = ∑ᵢ log f(xᵢ | θ)
2. 2)Differentiate term-by-term
3. 3)Set the resulting expression to 0
4. 4)Solve for θ̂

### When there is no closed form

In many ML models (logistic regression, neural nets), ℓ(**θ**) is differentiable but does not yield an algebraic closed-form solution.

Then MLE becomes **numerical optimization**:

- •gradient ascent on ℓ(**θ**)
- •gradient descent on −ℓ(**θ**)
- •Newton / quasi-Newton methods using curvature information

Even when we can’t solve the score equation analytically, the score still guides algorithms.

### A small but powerful conceptual link

Maximizing log-likelihood is equivalent to minimizing average surprise:

(1/n)NLL(θ) = −(1/n)∑ᵢ log f(xᵢ | θ)

So MLE chooses the parameter that makes the observed data as *unsurprising* as possible under the model.

## Application/Connection: How MLE Shows Up in Machine Learning and Statistics

### MLE as the engine behind many ML losses (why)

A large fraction of “standard losses” in machine learning are just negative log-likelihoods for some probabilistic model.

- •Linear regression with Gaussian noise ⇒ squared error loss
- •Logistic regression ⇒ Bernoulli likelihood ⇒ cross-entropy loss
- •Softmax classification ⇒ categorical likelihood ⇒ multinomial cross-entropy

So MLE isn’t just a statistics technique—it’s a unifying design principle for objective functions.

### Example: Gaussian likelihood ⇒ squared error

Assume:

yᵢ = μ(xᵢ; **w**) + εᵢ, εᵢ ∼ Normal(0, σ²)

Then:

f(yᵢ | xᵢ, **w**) = (1/√(2πσ²)) exp(−(yᵢ − μ(xᵢ; **w**))² / (2σ²))

Log-likelihood (dropping constants not depending on **w**):

ℓ(**w**)

= ∑ᵢ [ −(yᵢ − μ(xᵢ; **w**))² / (2σ²) ] + const

Maximizing ℓ(**w**) ⇔ minimizing ∑ᵢ (yᵢ − μ(xᵢ; **w**))²

That is least squares.

### Example: Bernoulli likelihood ⇒ cross-entropy

If yᵢ ∈ {0,1} and model predicts pᵢ = σ(**w**ᵀ**xᵢ**), then

f(yᵢ | **xᵢ**, **w**) = pᵢ^{yᵢ} (1 − pᵢ)^{1−yᵢ}

NLL is

−ℓ(**w**) = −∑ᵢ [ yᵢ log pᵢ + (1−yᵢ) log(1−pᵢ) ]

That is binary cross-entropy.

### Statistical properties you’ll later connect to

MLE is popular because, under regularity conditions and for large n:

- •**Consistency**: θ̂ → θ (in probability)
- •**Asymptotic normality**: √n(θ̂ − θ) ≈ Normal(0, I(θ)⁻¹)
- •**Efficiency**: achieves optimal variance among many estimators (Cramér–Rao ideas)

You don’t need these proofs yet, but they explain why MLE is often the default.

### MLE vs Bayesian inference (a preview)

MLE chooses a single best θ.

Bayesian inference treats θ as random and updates a prior p(θ) to a posterior:

p(θ | data) ∝ p(data | θ) p(θ)

Notice p(data | θ) is exactly the likelihood (up to notation). So MLE and Bayes share the same core ingredient; Bayes adds a prior.

### A conceptual bridge to KL divergence

In many settings, maximizing expected log-likelihood is equivalent to minimizing KL divergence between the true data-generating distribution and your model family. This is one reason KL divergence shows up everywhere in ML.

### Connecting to confidence intervals

Once you have θ̂, you often want uncertainty. Many confidence interval methods start from the curvature of ℓ(θ) near θ̂ (observed Fisher information / Hessian). So MLE is a gateway to inference, not just point estimation.

## Worked Examples (3)

### Bernoulli MLE: estimating a coin’s bias

Let x₁,…,xₙ be i.i.d. Bernoulli(p), where xᵢ ∈ {0,1}. We observe k = ∑ᵢ xᵢ heads (1s). Find the MLE p̂.

1. Write the pmf for one observation:

   f(xᵢ | p) = p^{xᵢ}(1−p)^{1−xᵢ}
2. Write the likelihood (independence ⇒ product):

   L(p) = ∏ᵢ p^{xᵢ}(1−p)^{1−xᵢ}
3. Collect exponents using ∑ᵢ xᵢ = k and ∑ᵢ (1−xᵢ) = n−k:

   L(p) = p^k (1−p)^{n−k}
4. Take logs to simplify:

   ℓ(p) = log L(p)

   = log(p^k (1−p)^{n−k})

   = k log p + (n−k) log(1−p)
5. Differentiate (score) and set to zero (interior solution):

   dℓ/dp = k·(1/p) + (n−k)·(−1/(1−p))

   = k/p − (n−k)/(1−p)

   Set dℓ/dp = 0:

   k/p = (n−k)/(1−p)
6. Solve for p:

   k(1−p) = p(n−k)

   k − kp = pn − pk

   k = pn

   p̂ = k/n
7. Check it is a maximum (second derivative):

   d²ℓ/dp² = −k/p² − (n−k)/(1−p)² < 0 for p ∈ (0,1)

   So the critical point is a (strict) local maximum.

**Insight:** For Bernoulli data, the MLE equals the sample mean: p̂ = (1/n)∑ᵢ xᵢ. This is a recurring theme: MLE often matches intuitive “frequency” estimators.

### Poisson MLE: estimating a rate from counts

Let x₁,…,xₙ be i.i.d. Poisson(λ), with λ > 0. Find the MLE λ̂.

1. Write the pmf for one observation:

   f(xᵢ | λ) = e^{−λ} λ^{xᵢ} / xᵢ!
2. Likelihood:

   L(λ) = ∏ᵢ [ e^{−λ} λ^{xᵢ} / xᵢ! ]
3. Simplify the product:

   L(λ) = (∏ᵢ e^{−λ}) (∏ᵢ λ^{xᵢ}) / (∏ᵢ xᵢ!)

   = e^{−nλ} λ^{∑ᵢ xᵢ} / (∏ᵢ xᵢ!)
4. Log-likelihood (dropping constants that do not depend on λ):

   ℓ(λ) = log L(λ)

   = (−nλ) + (∑ᵢ xᵢ) log λ − ∑ᵢ log(xᵢ!)
5. Differentiate and set to zero:

   dℓ/dλ = −n + (∑ᵢ xᵢ)/λ

   Set dℓ/dλ = 0:

   −n + (∑ᵢ xᵢ)/λ = 0

   (∑ᵢ xᵢ)/λ = n
6. Solve:

   λ̂ = (1/n)∑ᵢ xᵢ
7. Second derivative check:

   d²ℓ/dλ² = −(∑ᵢ xᵢ)/λ² < 0 for λ > 0 (assuming not all xᵢ are 0)

   So it’s a maximum.

**Insight:** Again, the MLE matches the sample mean. For Poisson, the mean equals λ, so the MLE is the natural plug-in estimator.

### Normal MLE (μ known σ² unknown): estimating variance carefully

Let x₁,…,xₙ be i.i.d. Normal(μ, σ²). Assume μ is known. Find the MLE for σ².

1. Write the pdf:

   f(xᵢ | σ²) = (1/√(2πσ²)) exp(−(xᵢ−μ)² / (2σ²))
2. Likelihood:

   L(σ²) = ∏ᵢ (1/√(2πσ²)) exp(−(xᵢ−μ)² / (2σ²))
3. Log-likelihood:

   ℓ(σ²)

   = ∑ᵢ [ −(1/2)log(2πσ²) − (xᵢ−μ)²/(2σ²) ]

   = −(n/2)log(2πσ²) − (1/(2σ²))∑ᵢ (xᵢ−μ)²
4. Differentiate w.r.t. σ²:

   dℓ/d(σ²)

   = −(n/2)·(1/σ²) + (1/2)(∑ᵢ (xᵢ−μ)²)·(1/(σ²)²)

   Explanation: derivative of −(1/(2σ²))S is +(1/2)S·(1/(σ²)²), where S = ∑ᵢ (xᵢ−μ)²
5. Set derivative to zero:

   −(n/2)(1/σ²) + (1/2)S(1/(σ²)²) = 0
6. Multiply both sides by 2(σ²)² to clear fractions:

   −nσ² + S = 0
7. Solve:

   σ̂²\_MLE = S/n = (1/n)∑ᵢ (xᵢ−μ)²
8. Second derivative check (sketch): curvature is negative at the solution for σ² > 0, giving a maximum.

**Insight:** The MLE for σ² uses 1/n, not 1/(n−1). The 1/(n−1) version is the unbiased sample variance; MLE prioritizes likelihood maximization, not unbiasedness.

## Key Takeaways

- ✓

  The likelihood L(θ) is the joint pmf/pdf of the observed data, viewed as a function of θ with the data fixed.
- ✓

  The MLE is θ̂ = argmaxθ L(θ); in practice we maximize ℓ(θ) = log L(θ) because it turns products into sums.
- ✓

  For i.i.d. data, ℓ(θ) = ∑ᵢ log f(xᵢ | θ), which is computationally and conceptually convenient.
- ✓

  Interior optima satisfy the score equation: ∇θ ℓ(θ̂) = 0; then you must verify it’s a maximum (curvature) or check boundaries.
- ✓

  Many familiar estimators are MLEs (e.g., Bernoulli p̂ = sample mean; Poisson λ̂ = sample mean).
- ✓

  Many ML loss functions are negative log-likelihoods (cross-entropy, squared error under Gaussian noise).
- ✓

  MLE depends on the assumed model family; it returns the best fit within that family, even if the family is misspecified.

## Common Mistakes

- ✗

  Treating L(θ) as a probability distribution over θ (it is not); only in Bayesian inference do we form p(θ | data).
- ✗

  Forgetting parameter constraints (e.g., p ∈ [0,1], σ² > 0) and missing boundary maxima.
- ✗

  Setting the score to zero and stopping—without checking whether the critical point is a maximum (second derivative/Hessian) or whether multiple maxima exist.
- ✗

  Confusing the MLE variance formula (divide by n) with the unbiased sample variance (divide by n−1).

## Practice

easy

Uniform(0, θ) MLE: Suppose x₁,…,xₙ are i.i.d. Uniform(0, θ) with θ > 0. Derive the MLE θ̂.

**Hint:** Write f(x|θ) = 1/θ for 0 ≤ x ≤ θ, and 0 otherwise. The likelihood is zero if θ is smaller than any observed value.

Show solution

For one observation: f(xᵢ|θ) = 1/θ if 0 ≤ xᵢ ≤ θ, else 0.

Likelihood:

L(θ) = ∏ᵢ (1/θ) · 𝟙{xᵢ ≤ θ}

= θ^{−n} · 𝟙{maxᵢ xᵢ ≤ θ}.

If θ < max xᵢ, then L(θ)=0. For θ ≥ m where m = max xᵢ, L(θ)=θ^{−n}, which decreases as θ increases.

So the maximum occurs at the smallest feasible θ, i.e. θ̂ = maxᵢ xᵢ.

medium

Normal(μ, σ²) MLE for μ when σ² is known: Given x₁,…,xₙ i.i.d. Normal(μ, σ²) with σ² known, derive μ̂.

**Hint:** Write ℓ(μ) and differentiate. The exponent contains ∑ᵢ (xᵢ−μ)².

Show solution

Log-likelihood (dropping constants not involving μ):

ℓ(μ) = −(1/(2σ²))∑ᵢ (xᵢ−μ)².

Differentiate:

dℓ/dμ = −(1/(2σ²))∑ᵢ 2(xᵢ−μ)(−1)

= (1/σ²)∑ᵢ (xᵢ−μ)

Set to zero:

∑ᵢ (xᵢ−μ) = 0

∑ᵢ xᵢ − nμ = 0

μ̂ = (1/n)∑ᵢ xᵢ.

Second derivative is −n/σ² < 0, so it’s a maximum.

medium

Boundary case for Bernoulli: You observe x₁,…,xₙ all equal to 1 (all successes). What is the MLE for p? Explain why the score equation approach can be misleading here.

**Hint:** Write ℓ(p) = n log p when k = n, and remember p must be in [0,1].

Show solution

If all xᵢ = 1, then k = n.

Likelihood: L(p)=p^n.

Log-likelihood: ℓ(p)=n log p, which increases as p increases on (0,1].

Thus the MLE is the boundary point p̂ = 1.

Why score can mislead: dℓ/dp = n/p, which never equals 0 for p ∈ (0,1]. The maximum is not an interior critical point; it occurs at the boundary, so the score=0 condition does not apply.

## Connections

Next nodes you can unlock and why they connect:

- •[Machine Learning Introduction](/tech-tree/ml-intro/): Many ML algorithms are posed as maximizing likelihood or minimizing negative log-likelihood.
- •[Bayesian Inference](/tech-tree/bayesian-inference/): Bayes’ rule uses the likelihood p(data | θ) as a core component; MLE is a useful baseline/limit case.
- •[Logistic Regression](/tech-tree/logistic-regression/): Logistic regression is typically fit by MLE; its cross-entropy objective is the Bernoulli negative log-likelihood.
- •[KL Divergence](/tech-tree/kl-divergence/): Expected negative log-likelihood relates to cross-entropy and KL; MLE can be viewed as choosing parameters that minimize KL to the true distribution (under conditions).
- •[Confidence Intervals](/tech-tree/confidence-intervals/): Curvature of the log-likelihood around θ̂ underpins standard errors and interval estimates.

Quality: A (4.6/5)

[← back to tree](/tech-tree/)[browse all →](/tech-tree/inventory/)
