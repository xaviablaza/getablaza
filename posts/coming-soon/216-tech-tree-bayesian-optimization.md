---
title: Bayesian Optimization
description: Global optimization with probabilistic surrogate models. Acquisition functions.
date: '2026-07-01'
scheduled: '2027-02-01'
tags:
- p-and-l-engineering
- coming-soon
- tech-tree
layout: layouts/post.njk
templateEngineOverride: md
image: /img/xavi-linkedin-profile.jpg
draft: true
generated_by: templeton-deep-copy-import
source_format: html
inspiration_url: https://templeton.host/tech-tree/bayesian-optimization/
inspiration_category: tech-tree
---

> Source-copy draft imported from [https://templeton.host/tech-tree/bayesian-optimization/](https://templeton.host/tech-tree/bayesian-optimization/). Names, domain references, and local media paths were adapted for Xavi Ablaza / getablaza.com.

[←Back to Tech Tree](/tech-tree/)

[inventory](/tech-tree/inventory/)[coverage](/tech-tree/coverage/)

# Bayesian Optimization

OptimizationDifficulty: ★★★★★Depth: 9Unlocks: 0

Global optimization with probabilistic surrogate models. Acquisition functions.

## Interactive Visualization

⏮◀◀▶▶STEP0.25x1xZOOM

t=0s

## Core Concepts

- -Probabilistic surrogate model: predictive distribution summarized by predictive mean and predictive variance at any input (captures uncertainty about f)
- -Acquisition function: a utility function that scores inputs by trading exploration (uncertainty) and exploitation (predicted objective)
- -Sequential closed-loop decision: iteratively select inputs by optimizing the acquisition, evaluate the true objective, and update the surrogate

## Key Symbols & Notation

f(x) - unknown objective function to be minimized or maximizedmu(x), sigma^2(x) - surrogate predictive mean and predictive variance at input x

## Essential Relationships

- -At each iteration: compute mu(x), sigma^2(x); form acquisition a(x; mu, sigma^2); choose x\_next = argmax\_x a(x); evaluate f(x\_next); update the surrogate via Bayesian conditioning to get new mu, sigma^2

## Prerequisites (2)

[Bayesian Inference5 atoms](/tech-tree/bayesian-inference/)[Convex Optimization5 atoms](/tech-tree/convex-optimization/)

Advanced Learning Details

### Graph Position

132

Depth Cost

0

Fan-Out (ROI)

0

Bottleneck Score

9

Chain Length

### Cognitive Load

6

Atomic Elements

70

Total Elements

L4

Percentile Level

L4

Atomic Level

### All Concepts (25)

- - Probabilistic surrogate model for objective functions (modeling f(x) as a random function)
- - Gaussian process (GP) as a common choice of surrogate prior over functions
- - Kernel / covariance function defining similarity between inputs and smoothness assumptions
- - GP predictive (posterior) distribution at a new input: predictive mean and predictive variance
- - Closed-form GP predictive equations (mean and variance computed from training covariances)
- - Observation noise modeling via additive noise variance in the GP
- - Hyperparameters of the kernel (covariance) and noise, and their learning
- - Marginal likelihood (evidence) for hyperparameter selection (type-II ML, evidence maximization)
- - Hyperparameter marginalization (integrating over hyperparameters) as alternative to point estimates
- - Acquisition function: a utility function defined on surrogate predictive distribution to pick next query
- - Specific acquisition functions: Expected Improvement (EI)
- - Specific acquisition functions: Probability of Improvement (PI)
- - Specific acquisition functions: Upper Confidence Bound (UCB)
- - Specific acquisition functions: Knowledge Gradient, Entropy Search / Predictive Entropy Search
- - Thompson sampling (sampling a function from posterior and optimizing it) for acquisition
- - Exploration–exploitation trade-off as operationalized by acquisition functions and their parameters
- - Sequential model-based optimization loop: fit surrogate -> optimize acquisition -> evaluate -> update
- - Acquisition optimization as a separate (often non-convex) inner optimization problem
- - Batch / parallel Bayesian optimization (selecting multiple points per iteration) and required adjustments
- - Handling expensive black-box objectives where each evaluation is costly and gradients are unavailable
- - Regret metrics (simple regret, cumulative regret) used to evaluate BO performance and convergence
- - Scalability constraints of GP-based BO (cubic cost in number of observations, memory limits)
- - Computational strategies: sparse/approximate GPs, inducing points to scale BO
- - Noisy / stochastic objective handling in BO (impact on acquisition computation)
- - Using prior knowledge or warm-start (transfer learning / multi-task BO) to initialize surrogate

### Teaching Strategy

Multi-session curriculum - substantial prior knowledge and complex material. Use mastery gates and deliberate practice.

When evaluating f(x) is expensive (a lab experiment, a simulation, training a model), you can’t afford thousands of trials. Bayesian optimization turns each evaluation into maximal information: it builds a probabilistic surrogate for f, uses uncertainty to decide where to sample next, and repeats—often finding near-optimal solutions in tens of evaluations rather than thousands.

TL;DR:

Bayesian optimization (BO) is a global, sample-efficient strategy for optimizing an unknown, expensive black-box function f(x). It maintains a probabilistic surrogate model that provides a predictive mean μ(x) and predictive variance σ²(x), then chooses the next query by maximizing an acquisition function that balances exploitation (low/high μ) and exploration (high σ). The loop is: fit surrogate → optimize acquisition → evaluate f at selected x → update surrogate.

## What Is Bayesian Optimization?

## Why it exists (motivation before formulas)

Many real optimization problems don’t match the assumptions that make classical optimization fast:

- •**f(x) is expensive**: each evaluation could be minutes to days.
- •**f(x) is derivative-free**: you can’t compute ∇f, and finite differences are too costly.
- •**f(x) is nonconvex**: local methods can get stuck.
- •**f(x) can be noisy**: repeated evaluations differ.

If each evaluation is precious, the core question becomes:

> Which x should I evaluate next to learn the most about where the optimum might be?

Bayesian optimization answers this using probability: it represents uncertainty about f and uses that uncertainty to guide where to sample.

## Definition (what it is)

Let f(x) be an **unknown objective** you want to minimize or maximize over a domain 𝒳 ⊂ ℝᵈ.

Bayesian optimization is a **sequential decision procedure** that:

1. 1)Maintains a **probabilistic surrogate model** for f.
2. 2)Uses the surrogate’s **predictive distribution** at each x to compute an **acquisition function** a(x).
3. 3)Selects the next evaluation point by optimizing the acquisition:

xₙ₊₁ ∈ argmaxₓ∈𝒳 a(x)

4. 4)Evaluates the real objective (expensive): yₙ₊₁ = f(xₙ₊₁) (possibly with noise)
5. 5)Updates the surrogate with the new data and repeats.

The surrogate gives, at any x:

- •Predictive mean μ(x) (what we think f(x) is)
- •Predictive variance σ²(x) (how uncertain we are)

This pair (μ, σ²) is the “sufficient interface” most BO algorithms need.

## Key intuition: exploration vs exploitation

If you only chase the best current μ(x), you might get stuck exploiting a wrong region.

If you only chase high σ(x), you waste evaluations in uncertain but unpromising regions.

Acquisition functions formalize a **trade-off**:

- •**Exploitation**: favor x with good predicted objective value.
- •**Exploration**: favor x where uncertainty is high and you could discover better outcomes.

## What BO is not

It’s not “Bayesian” in the sense that your final answer must be a full posterior over the optimum; often we just want a good x after few evaluations.

It’s not restricted to Gaussian processes (GPs), though GPs are the canonical choice.

It’s not guaranteed to find the global optimum in finite time—but it is often extremely effective when evaluations are expensive.

## A minimal mathematical statement

Assume we have data 𝒟ₙ = {(xᵢ, yᵢ)}ᵢ₌₁ⁿ.

A surrogate produces a predictive distribution for f(x) given 𝒟ₙ.

We summarize that as:

f(x) | 𝒟ₙ ≈ 𝒩( μₙ(x), σ²ₙ(x) )

Then a common pattern is:

aₙ(x) = Acquisition( μₙ(x), σₙ(x) )

and choose xₙ₊₁ maximizing aₙ.

This single loop—**model → acquisition → evaluate → update**—is the heart of Bayesian optimization.

## Core Mechanic 1: Probabilistic Surrogate Models (μ(x), σ²(x))

## Why surrogates matter

If evaluations are expensive, you want to extract maximum value from each one. A surrogate is a cheaper function you can evaluate anywhere, with uncertainty that reflects limited data.

A good surrogate should:

- •Fit observed data well
- •Generalize smoothly (if appropriate)
- •Provide **calibrated uncertainty**: σ²(x) large where you haven’t learned, small near data

That uncertainty is what enables principled exploration.

## The canonical surrogate: Gaussian Processes (GPs)

A GP is a distribution over functions. Informally:

f(·) ∼ GP(m(·), k(·, ·))

- •m(x) is the prior mean (often 0)
- •k(x, x′) is the kernel (covariance) controlling smoothness and correlation

If observations are noisy:

yᵢ = f(xᵢ) + εᵢ, εᵢ ∼ 𝒩(0, σ²\_noise)

Given data, the GP posterior at a test point x is Gaussian:

f(x) | 𝒟ₙ ∼ 𝒩( μₙ(x), σ²ₙ(x) )

### The GP posterior (showing the key structure)

Let **X** ∈ ℝⁿˣᵈ be the matrix of inputs, **y** ∈ ℝⁿ be outputs, and define:

- •**K** = k(**X**, **X**) ∈ ℝⁿˣⁿ with Kᵢⱼ = k(xᵢ, xⱼ)
- •**k**(x) = k(**X**, x) ∈ ℝⁿ with kᵢ(x) = k(xᵢ, x)

With Gaussian noise, the effective covariance is **K** + σ²\_noise **I**.

Then:

μₙ(x) = m(x) + **k**(x)ᵀ ( **K** + σ²\_noise **I** )⁻¹ ( **y** − m(**X**) )

σ²ₙ(x) = k(x, x) − **k**(x)ᵀ ( **K** + σ²\_noise **I** )⁻¹ **k**(x)

#### What these formulas are saying (intuition)

- •μₙ(x) is a **weighted combination of observed values**, where weights depend on similarity via the kernel.
- •σ²ₙ(x) is **prior variance minus explained variance**. It shrinks near observed points.

A useful mental model:

- •If x is near many data points, **k**(x) is large in magnitude, and uncertainty shrinks.
- •If x is far from data, **k**(x) is near 0, and σ²ₙ(x) ≈ k(x, x): you revert to prior uncertainty.

## Kernel choice and hyperparameters

The kernel encodes your belief about f.

Common kernels:

| Kernel | Typical assumption about f | Notes |
| --- | --- | --- |
| RBF / squared exponential | Very smooth | Strong inductive bias; often works in low d |
| Matérn(ν=3/2, 5/2) | Rougher than RBF | Common in BO; more realistic for many objectives |
| ARD versions | Different lengthscales per dimension | Helps identify irrelevant dimensions |

Hyperparameters (lengthscales, variance, noise) are often learned by maximizing marginal likelihood.

## Beyond GPs (when and why)

GPs scale as 𝒪(n³) with n evaluations due to matrix inversion (though there are approximations). In high d or with many evaluations, you might use:

| Surrogate | Strength | Weakness |
| --- | --- | --- |
| Random forest / TPE-style models | Works for mixed categorical/continuous; robust | Uncertainty is heuristic; less smooth |
| Bayesian neural nets | Flexible in high d | Harder to calibrate and fit; heavier compute |
| Linear models with Bayesian treatment | Fast | Too simple unless features are strong |

BO doesn’t require GPs; it requires **predictive distributions** (or at least μ and σ).

## The role of noise

Many objectives are noisy: y = f(x) + ε.

Noise affects:

- •How aggressively σ shrinks at data points
- •Whether repeated sampling at the same x is valuable

With high noise, the surrogate remains uncertain even near observed x, which can lead the acquisition to re-sample.

## A geometric interpretation (uncertainty as distance)

For stationary kernels (like RBF/Matérn), correlation decays with distance. So σ(x) tends to increase as x moves away from observed points.

This gives you a helpful picture:

- •μ(x) is “interpolating/extrapolating” values.
- •σ(x) is “how far you are from what you know,” adjusted by kernel geometry.

This is precisely what BO needs: a map of promising regions and unknown regions.

## Core Mechanic 2: Acquisition Functions (Turning Uncertainty Into Decisions)

## Why an acquisition function is needed

Even with a perfect surrogate posterior, you still need a rule to decide the next experiment.

We want a(x) to be:

- •**Cheap** to evaluate (compared to f)
- •High where sampling is expected to help
- •Able to balance exploration/exploitation

The acquisition is a utility function computed from the predictive distribution at x.

Assume for simplicity (common in GPs):

f(x) | 𝒟ₙ ∼ 𝒩( μ(x), σ²(x) )

(We’ll omit subscript n for readability.)

## Expected Improvement (EI)

### Idea

If you are minimizing f, define the best observed value so far:

f\_best = minᵢ yᵢ

Improvement at x is:

I(x) = max(0, f\_best − f(x))

Because f(x) is random under the surrogate, I(x) is random. EI takes its expectation:

EI(x) = 𝔼[ I(x) ]

### Closed form under Gaussian predictive distributions

Let Z = (f\_best − μ(x)) / σ(x) (for σ(x) > 0).

Let φ and Φ be the standard normal PDF and CDF.

Then:

EI(x) = (f\_best − μ(x)) Φ(Z) + σ(x) φ(Z)

#### Interpreting the two terms

- •(f\_best − μ) Φ(Z) is the exploitation component: large when μ is better than f\_best.
- •σ φ(Z) is the exploration component: large when uncertainty σ is high.

If σ → 0, EI tends to max(0, f\_best − μ): pure exploitation.

### Practical notes

- •EI can become numerically tricky when σ is tiny.
- •With observation noise, “best observed” can be misleading; variants use best posterior mean.

## Probability of Improvement (PI)

### Idea

Prefer x where f(x) beats f\_best with high probability:

PI(x) = 𝔼[ 1{ f(x) ≤ f\_best − ξ } ]

(For minimization; ξ ≥ 0 is a margin encouraging exploration.)

With Gaussian predictive distribution:

PI(x) = Φ( (f\_best − ξ − μ(x)) / σ(x) )

PI is simple but can over-exploit: it ignores how much improvement you get.

## Upper/Lower Confidence Bound (UCB/LCB)

### Idea

Construct an optimistic bound using uncertainty.

For **maximization**:

UCB(x) = μ(x) + κ σ(x)

For **minimization** (lower confidence bound):

LCB(x) = μ(x) − κ σ(x)

Choose x that maximizes UCB (or minimizes LCB). κ controls exploration:

- •Larger κ → more exploration
- •Smaller κ → more exploitation

### Why this is attractive

- •Very simple
- •Often strong theoretical guarantees (GP-UCB under assumptions)
- •Works naturally with batch variants and constraints

## Thompson Sampling (TS)

### Idea

Instead of building a deterministic a(x), sample a function from the posterior and optimize it.

1. 1)Sample f̃(·) ∼ posterior
2. 2)Pick xₙ₊₁ ∈ argminₓ f̃(x)

This naturally balances exploration and exploitation through posterior randomness.

## Comparing acquisitions (when to use what)

| Acquisition | Strength | Weakness | Typical use |
| --- | --- | --- | --- |
| EI | Good default; intuitive trade-off | Sensitive to noise and best-so-far definition | General BO with moderate noise |
| PI | Simple, stable | Over-exploitation; needs ξ tuning | When you only care about probability of beating a target |
| UCB/LCB | Easy; strong theory | Needs κ schedule; may over-explore | When you want theoretical regret control |
| Thompson sampling | Simple decision rule; parallel-friendly | Requires posterior sampling; can be noisy | Batch BO and large-scale approximations |

## Acquisition optimization is its own optimization problem

Key subtlety: the acquisition a(x) is nonconvex even if the surrogate is smooth.

So BO typically nests two optimizations:

- •Outer: optimize f via sequential evaluations
- •Inner: optimize a(x) cheaply but carefully

Common inner-loop strategies:

- •Multi-start gradient-based optimization (if a is differentiable)
- •Random search + local refinement
- •Evolutionary methods (CMA-ES) when a is rugged or constraints are complex

Because evaluating a(x) is cheap, you can afford many restarts.

## Constraints and feasibility

Sometimes you optimize f(x) subject to constraints cⱼ(x) ≤ 0.

A common idea: model constraints with surrogates too, and modify acquisition:

- •Multiply by probability of feasibility:

a\_constrained(x) = a(x) · P(feasible | x)

This encourages points that are both promising and likely feasible.

## Summary of the acquisition role

Surrogates provide beliefs (μ, σ²). Acquisition functions convert beliefs into actions (which x to try next). The “Bayesian” part is not just uncertainty estimation—it’s **decision-making under uncertainty**.

## Application/Connection: The Sequential Closed-Loop BO Algorithm (and Practical Design Choices)

## Why the closed loop matters

Bayesian optimization is fundamentally **adaptive experimentation**.

A non-adaptive baseline would pre-select a grid or random set of points and evaluate all of them. BO instead uses each new y to redirect future evaluations. This adaptivity is what yields sample efficiency.

## The standard BO loop (step-by-step)

We’ll write it for minimization.

### 0) Define the problem

- •Domain 𝒳 ⊂ ℝᵈ (box constraints, manifolds, or mixed spaces)
- •Evaluation budget N (max number of expensive calls)
- •Optional noise model and constraints

### 1) Initialization (space-filling)

Choose n₀ initial points, often via:

- •Latin hypercube sampling
- •Sobol sequences
- •Random uniform

You want broad coverage so early uncertainty is meaningful.

### 2) Fit/update surrogate

Given 𝒟ₙ, fit GP hyperparameters (or update posterior).

Compute μₙ(x), σ²ₙ(x) as needed.

### 3) Choose acquisition aₙ(x)

Common defaults:

- •EI for many continuous problems
- •LCB/UCB when you want a stable knob κ

### 4) Optimize acquisition (inner problem)

Compute:

xₙ₊₁ ∈ argmaxₓ aₙ(x)

In practice, you approximate this argmax with multi-start optimization.

### 5) Evaluate the true objective

Observe yₙ₊₁ = f(xₙ₊₁) + ε.

Update 𝒟ₙ₊₁ = 𝒟ₙ ∪ {(xₙ₊₁, yₙ₊₁)}.

### 6) Stop

Stop when budget is exhausted or improvement saturates.

Return:

x\* = argmin\_{(xᵢ, yᵢ) ∈ 𝒟} yᵢ

or return argmin μₙ(x) if you prefer posterior mean minimizer.

## Practical choices that strongly affect results

### 1) Input scaling and warping

BO is sensitive to geometry. If one coordinate spans [0, 10⁶] and another [0, 1], kernels can behave poorly.

Standard practice:

- •Normalize each dimension to [0, 1]
- •Consider log transforms for positive scale parameters

### 2) Handling categorical and conditional parameters

Hyperparameter tuning often has:

- •categorical choices (optimizer ∈ {SGD, Adam})
- •conditional parameters (momentum only if SGD)

GPs struggle with pure categorical spaces unless encoded carefully.

Alternatives:

- •Tree-structured Parzen estimator (TPE)
- •Random-forest surrogates
- •One-hot with specialized kernels (works sometimes)

### 3) Batch Bayesian optimization (parallel evaluations)

If you can evaluate B points in parallel, you want {x₁,…,x\_B}.

Approaches:

- •q-EI (joint expected improvement)
- •Thompson sampling draws multiple posterior samples
- •Greedy with “fantasy” observations (update surrogate with predicted outcomes)

Batch BO is harder because points should be diverse, not redundant.

### 4) High-dimensional BO

BO with standard GPs can degrade when d is large (say d ≥ 20–50).

Reasons:

- •Distances concentrate; kernels become less informative
- •Acquisition optimization becomes harder

Common mitigations:

| Strategy | Idea |
| --- | --- |
| ARD lengthscales | Detect irrelevant dimensions |
| Additive kernels | f(x) ≈ ∑ fⱼ(x\_{Sⱼ}) |
| Random embeddings | Optimize in a low-dimensional subspace |
| Trust-region BO | Restrict search locally and expand/shrink |

### 5) Multi-fidelity and cost-aware BO

Sometimes you can evaluate cheaper approximations:

- •fewer training epochs
- •smaller dataset
- •lower-resolution simulation

Multi-fidelity BO models f(x, s) where s is fidelity (cost). The acquisition trades off information vs cost.

### 6) Connections to Bayesian inference and decision theory

You already know Bayesian inference: prior → posterior.

BO adds an action layer:

posterior → decision rule (acquisition) → new data → posterior

This is a small instance of **Bayesian experimental design**.

## When BO is a good fit

Use BO when:

- •evaluations are expensive (≲ 10³ evaluations)
- •derivatives are not available
- •dimension is moderate or structure exists

Avoid or rethink BO when:

- •evaluations are cheap (use gradient-based or evolutionary methods)
- •dimension is huge with no structure
- •objective is extremely noisy and nonstationary without modeling that noise

## A mental model to keep

Think of BO as building a “map” of f:

- •μ(x) is the current best guess of the landscape.
- •σ(x) is the fog-of-war.
- •The acquisition decides where to scout next.

With that model, most design decisions become: how should the fog behave, and what scouting strategy do you want?

## Worked Examples (3)

### Compute Expected Improvement (EI) from μ(x), σ(x) at candidate points

You are minimizing f. You have observed best value so far f\_best = 1.20.

Your surrogate gives predictive distributions at two candidate points:

- •Point A: μ(A) = 1.10, σ(A) = 0.05
- •Point B: μ(B) = 1.25, σ(B) = 0.30

Assume Gaussian predictive distributions. Compute EI(A) and EI(B) and decide which point EI prefers.

1. For minimization, EI(x) = (f\_best − μ(x)) Φ(Z) + σ(x) φ(Z), where Z = (f\_best − μ(x)) / σ(x).
2. Point A:

   Z\_A = (1.20 − 1.10) / 0.05

   = 0.10 / 0.05

   = 2.0
3. Look up (or approximate): Φ(2.0) ≈ 0.97725 and φ(2.0) ≈ 0.05399.
4. Compute EI(A):

   EI(A) = (1.20 − 1.10) Φ(2.0) + 0.05 φ(2.0)

   = 0.10 · 0.97725 + 0.05 · 0.05399

   = 0.097725 + 0.0026995

   ≈ 0.1004245
5. Point B:

   Z\_B = (1.20 − 1.25) / 0.30

   = (−0.05) / 0.30

   = −0.166666…
6. Approximate: Φ(−0.1667) ≈ 0.4338. Also φ(−0.1667) = φ(0.1667) ≈ 0.393 (since φ is symmetric).
7. Compute EI(B):

   EI(B) = (1.20 − 1.25) Φ(−0.1667) + 0.30 φ(−0.1667)

   = (−0.05) · 0.4338 + 0.30 · 0.393

   = −0.02169 + 0.1179

   ≈ 0.09621

**Insight:** Even though B has worse predicted mean (μ(B) > f\_best), its large uncertainty gives it a sizable exploration term σ φ(Z). EI still slightly prefers A here because A already looks better than f\_best and is fairly certain. EI often picks points that are either clearly good (low μ) or highly uncertain (high σ), and the balance depends on Z.

### Derive the UCB/LCB rule as an optimistic decision under uncertainty

Assume you are maximizing f. Your surrogate gives f(x) | 𝒟 ∼ 𝒩( μ(x), σ²(x) ). Show how choosing x that maximizes μ(x) + κ σ(x) can be interpreted as optimizing an optimistic bound (a high quantile) of the predictive distribution.

1. For a Gaussian random variable, a (1 − α) quantile is:

   q\_{1−α}(x) = μ(x) + z\_{1−α} σ(x)

   where z\_{1−α} is the standard normal quantile (e.g., z\_{0.95} ≈ 1.645).
2. If we choose κ = z\_{1−α}, then:

   q\_{1−α}(x) = μ(x) + κ σ(x).
3. Selecting x by maximizing UCB(x) = μ(x) + κ σ(x) is equivalent to:

   x\_{next} ∈ argmaxₓ q\_{1−α}(x).
4. This is an explicit optimism strategy:

   - •μ(x) measures predicted performance (exploitation)
   - •κ σ(x) adds a bonus for uncertainty (exploration)
5. As κ increases, you act more optimistic about uncertain regions; as κ → 0, you recover pure greedy exploitation x = argmax μ(x).

**Insight:** UCB can be seen as “optimize a high-confidence optimistic scenario” of the function. This interpretation also explains why κ is a natural exploration knob: it literally selects which predictive quantile you optimize.

### One full BO iteration on a toy 1D problem using LCB

You are minimizing f(x) over 𝒳 = [0, 1]. You currently have 3 observations:

(x, y) = (0.1, 0.80), (0.5, 0.30), (0.9, 0.60)

Your surrogate (already fit) provides the following summaries at candidate points:

- •x = 0.2: μ = 0.55, σ = 0.20
- •x = 0.4: μ = 0.35, σ = 0.05
- •x = 0.7: μ = 0.40, σ = 0.15

Use LCB with κ = 2 to pick the next point.

1. For minimization, define:

   LCB(x) = μ(x) − κ σ(x)

   with κ = 2.
2. Compute LCB(0.2):

   LCB = 0.55 − 2 · 0.20

   = 0.55 − 0.40

   = 0.15
3. Compute LCB(0.4):

   LCB = 0.35 − 2 · 0.05

   = 0.35 − 0.10

   = 0.25
4. Compute LCB(0.7):

   LCB = 0.40 − 2 · 0.15

   = 0.40 − 0.30

   = 0.10
5. Pick x that minimizes LCB:

   min{0.15, 0.25, 0.10} occurs at x = 0.7.

   So choose x\_next = 0.7 to evaluate f.
6. After evaluating and observing y\_next = f(0.7), you append (0.7, y\_next) to 𝒟 and refit/update the surrogate, which will typically reduce σ near 0.7 and adjust μ nearby.

**Insight:** Even though x = 0.4 has the best predicted mean (μ = 0.35), its uncertainty is tiny, so LCB doesn’t see much chance of discovering something dramatically better. x = 0.7 has slightly worse μ but much larger σ, so the uncertainty bonus makes it attractive as a potentially better region.

## Key Takeaways

- ✓

  Bayesian optimization is designed for **expensive, black-box** objectives where you must be sample-efficient.
- ✓

  The surrogate’s predictive mean μ(x) estimates performance; predictive variance σ²(x) encodes epistemic uncertainty about f(x).
- ✓

  Acquisition functions are decision rules that trade off exploitation (good μ) and exploration (large σ).
- ✓

  Expected Improvement (EI) quantifies expected gain over the current best and has a closed form under Gaussian predictions.
- ✓

  UCB/LCB adds an uncertainty bonus/penalty μ ± κσ and can be interpreted as optimizing a predictive quantile.
- ✓

  BO is a **closed loop**: fit surrogate → optimize acquisition → evaluate f → update surrogate; the inner acquisition optimization is itself nonconvex.
- ✓

  Initialization, scaling, noise modeling, and acquisition optimization quality often matter as much as the choice of acquisition function.
- ✓

  In high dimensions or mixed discrete/continuous spaces, standard GP-based BO may need structural assumptions (ARD/additivity/trust regions) or different surrogates.

## Common Mistakes

- ✗

  Treating σ(x) as observation noise instead of **model uncertainty**: σ reflects what you don’t know about f, not just randomness in y.
- ✗

  Poor acquisition optimization (too few restarts, bad bounds) leading to selecting suboptimal xₙ₊₁ and undercutting BO’s benefits.
- ✗

  Ignoring input scaling/warping: kernels and lengthscales become ill-conditioned, making μ and σ unreliable.
- ✗

  Using EI/PI with noisy observations without adjusting the “best so far” concept, causing the acquisition to chase noise artifacts.

## Practice

easy

You are minimizing f. Current best observed value is f\_best = 0.50. For a candidate x, your surrogate gives μ(x) = 0.55 and σ(x) = 0.10. Compute PI(x) with margin ξ = 0.02, i.e., PI = Φ((f\_best − ξ − μ)/σ).

**Hint:** Compute Z = (0.50 − 0.02 − 0.55)/0.10, then evaluate Φ(Z).

Show solution

Z = (0.48 − 0.55)/0.10 = (−0.07)/0.10 = −0.7.

So PI = Φ(−0.7) ≈ 0.241 (since Φ(0.7) ≈ 0.759).

medium

For minimization using LCB with κ = 1.5, compare two candidates:

A: μ = 0.20, σ = 0.01

B: μ = 0.23, σ = 0.05

Which does LCB choose, and why?

**Hint:** Compute LCB = μ − κσ for each; smaller is preferred.

Show solution

LCB(A) = 0.20 − 1.5·0.01 = 0.20 − 0.015 = 0.185.

LCB(B) = 0.23 − 1.5·0.05 = 0.23 − 0.075 = 0.155.

LCB chooses B because its larger uncertainty creates a bigger exploration benefit, yielding a lower optimistic bound despite a worse mean.

hard

Suppose a GP surrogate uses an RBF kernel with very small lengthscale ℓ in every dimension. Qualitatively, what happens to μ(x) and σ(x) away from observed points, and how might that affect BO behavior?

**Hint:** Think about k(x, x′) decaying with distance relative to ℓ; small ℓ means correlation drops quickly.

Show solution

With very small ℓ, k(x, x′) decays extremely fast, so points are only correlated in tiny neighborhoods. Away from observed points, **k**(x) ≈ 0, so μ(x) reverts toward the prior mean m(x) and σ²(x) approaches the prior variance k(x, x). As a result, much of the domain looks highly uncertain, and acquisitions like UCB/EI may over-explore broadly rather than leveraging smooth generalization. BO may behave like near-random exploration unless enough data densely covers the space.

## Connections

Prerequisites: [Bayesian Inference](/tech-tree/bayesian-inference/), [Convex Optimization](/tech-tree/convex-optimization/)

Related next nodes and supporting ideas:

- •[Gaussian Processes](/tech-tree/gaussian-processes/) (common surrogate; kernels; posterior mean/variance)
- •[Kernel Methods](/tech-tree/kernel-methods/) (how k(x, x′) shapes μ and σ)
- •[Multi-armed Bandits](/tech-tree/bandits/) (exploration/exploitation; UCB and TS connections)
- •[Hyperparameter Optimization](/tech-tree/hyperparameter-optimization/) (a major practical use-case for BO)
- •[Black-box Optimization](/tech-tree/black-box-optimization/) (broader family including evolutionary strategies)
- •[Constrained Optimization](/tech-tree/constrained-optimization/) (BO with feasibility models and constrained acquisitions)

Quality: A (4.2/5)

[← back to tree](/tech-tree/)[browse all →](/tech-tree/inventory/)
