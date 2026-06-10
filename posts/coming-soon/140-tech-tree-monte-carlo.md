---
title: Monte Carlo Methods
description: Using random sampling to estimate quantities. Integration, simulation.
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
permalink: /tech-tree/monte-carlo/
---

[←Back to Tech Tree](/tech-tree/)

[inventory](/tech-tree/inventory/)[coverage](/tech-tree/coverage/)

# Monte Carlo Methods

Probability & StatisticsDifficulty: ★★★★☆Depth: 6Unlocks: 4

Using random sampling to estimate quantities. Integration, simulation.

## Interactive Visualization

⏮◀◀▶▶STEP0.25x1xZOOM

t=0s

## Core Concepts

- -Expectation representation: the numerical quantity of interest is an expectation E\_p[f(X)] (an integral under a probability measure)
- -Monte Carlo estimator: approximate that expectation by averaging f(X) over random draws (use sample average of independent or simulated samples)
- -Error governed by variance: estimator accuracy is determined by Var(f(X)); root-mean-square error scales like 1/sqrt(N); reducing variance improves accuracy

## Key Symbols & Notation

I\_hat\_N = (1/N) sum\_{i=1}^N f(X\_i)

## Essential Relationships

- -Integral-expectation identity: integral f(x) p(x) dx = E\_p[f(X)]
- -Importance-sampling identity: if samples are from q, E\_p[f(X)] = E\_q[(p(X)/q(X)) \* f(X)], so the estimator replaces f(X) by weight\*(f(X)) when sampling from q

## Prerequisites (2)

[Law of Large Numbers5 atoms](/tech-tree/law-large-numbers/)[Common Distributions6 atoms](/tech-tree/common-distributions/)

## Unlocks (1)

[MCMClvl 4](/tech-tree/mcmc/)

## Referenced by (2)

Where this concept shows up in the operating-finance and personal-finance graphs.

### From Business (2)

[FIREBusiness

Monte Carlo simulation is the standard FIRE planning methodology - modeling sequence of returns risk and withdrawal success probability across thousands of simulated paths](/business/fire/)[Option PricingBusiness

Monte Carlo integration is the unifying computational method across all three perspectives - pricing path-dependent options via simulated risk-neutral paths, estimating marginal likelihoods by sampling the parameter space, and evaluating high-dimensional integrals where analytic solutions do not exist](/business/option-pricing/)

Advanced Learning Details

### Graph Position

62

Depth Cost

4

Fan-Out (ROI)

1

Bottleneck Score

6

Chain Length

### Cognitive Load

6

Atomic Elements

57

Total Elements

L4

Percentile Level

L4

Atomic Level

### All Concepts (25)

- - Monte Carlo integration: estimating definite integrals by treating the integral as an expectation and approximating that expectation by sampling
- - Monte Carlo estimator: using the (possibly weighted) sample mean of function evaluations as an estimator for an expectation or integral
- - Importance sampling: drawing samples from an alternative (proposal) distribution and weighting them to estimate a target expectation
- - Importance weight: the weight applied to a sample from a proposal distribution to correct for the difference from the target distribution
- - Rejection sampling: obtaining samples from a target distribution by sampling from a proposal and accepting/rejecting with a probabilistic rule
- - Markov Chain Monte Carlo (MCMC): generating (dependent) samples by running a Markov chain whose stationary distribution is the target distribution
- - Metropolis–Hastings algorithm: a general MCMC scheme using a proposal distribution and an accept/reject step based on an acceptance probability
- - Gibbs sampling: an MCMC method that samples sequentially from conditional distributions of each component
- - Ergodicity / stationarity of Markov chains (in the Monte Carlo context): conditions under which time averages along the chain converge to target expectations
- - Burn-in and thinning (practical MCMC procedures): discarding initial iterations to reduce initialization bias and optionally thinning to reduce autocorrelation
- - Effective sample size (ESS): a measure of how many independent samples a correlated (e.g., MCMC) sample is worth
- - Variance reduction techniques (general concept): methods to reduce estimator variance for a given sample budget
- - Control variates: a variance reduction technique that uses covariance with a function of known expectation to reduce variance of the estimator
- - Antithetic variates: a variance reduction technique that uses negatively correlated sample pairs to reduce variance
- - Stratified sampling: dividing the domain into strata and sampling within each stratum to reduce estimator variance
- - Quasi–Monte Carlo (QMC): replacing random sampling with low-discrepancy (quasi-random) sequences to reduce integration error
- - Pseudo-random vs true random numbers: the idea that most practical Monte Carlo uses deterministic pseudo-random number generators and implications for sampling
- - Convergence rate of Monte Carlo estimators: the typical root-n error decay (error ∝ 1/sqrt(n)) for standard Monte Carlo sampling
- - Estimator variance and standard error in Monte Carlo: variance of the estimator determines sampling error and can be estimated from sample variance
- - Constructing Monte Carlo confidence intervals: using approximate normality of the sample-mean estimator (via CLT) to form intervals around estimates
- - Bias vs variance trade-offs in Monte Carlo estimators: understanding sources of bias (e.g., biased estimators, burn-in) and variance (sampling variability)
- - Weighted estimators normalization: necessity to normalize importance weights when using non-normalized proposal/target densities
- - Acceptance probability in MH: the role of the acceptance probability in controlling step acceptance and chain mixing
- - Relationship between autocorrelation and effective sample size: autocorrelation in MCMC increases estimator variance and reduces ESS
- - Practical diagnostics for Monte Carlo: basic diagnostics (trace plots, acceptance rate, autocorrelation plots) to assess simulation quality

### Teaching Strategy

Multi-session curriculum - substantial prior knowledge and complex material. Use mastery gates and deliberate practice.

When an integral is too messy to compute and a system is too complex to solve, you can still *estimate* the answer—by simulating randomness and averaging. That’s the core promise of Monte Carlo methods: convert hard math into repeated sampling.

TL;DR:

Monte Carlo methods estimate a quantity by writing it as an expectation I = E\_p[f(X)] and approximating it with a sample average Î\_N = (1/N)∑\_{i=1}^N f(X\_i). The estimator is unbiased under mild conditions, converges by the Law of Large Numbers, and has root-mean-square error ≈ √(Var(f(X))/N). Most practical skill comes from controlling variance (and thus error) rather than “just sampling more.”

## What Is Monte Carlo? (Expectation as the target)

Monte Carlo methods are a family of techniques that use random sampling to estimate numerical quantities. They are especially useful when:

- •The quantity is naturally an *average under uncertainty* (probability).
- •The exact computation involves a high-dimensional integral.
- •A deterministic algorithm exists but is too expensive.

### Why Monte Carlo exists (motivation)

Many problems can be phrased as: “What is the average value of some function under some distribution?”

Examples:

- •Integration: ∫ f(x) dx can be written as an expectation under a convenient distribution.
- •Risk: expected loss E[L] under uncertainty.
- •Physics/graphics: expected sensor/lighting response.
- •Bayesian inference: posterior expectations E[f(θ) | data].

The key idea is to **turn the numerical goal into an expectation**.

### The central representation

Let X be a random variable with distribution p (density or pmf). Let f be a function. The target quantity is:

I = E\_p[f(X)]

If X is continuous with density p(x):

I = ∫ f(x) p(x) dx

If X is discrete with pmf p(x):

I = ∑\_x f(x) p(x)

This seems like we replaced “compute an integral/sum” with “compute an expectation,” but expectations *suggest a strategy*: sample X from p and average f(X).

### The Monte Carlo estimator

Draw independent samples X₁, X₂, …, X\_N ∼ p, then compute:

Î\_N = (1/N) ∑\_{i=1}^N f(X\_i)

This is the **Monte Carlo estimator** (also called the sample mean estimator).

### What you get “for free”

You already know the Law of Large Numbers (LLN), so you already have the convergence story:

Î\_N → I as N → ∞ (under mild conditions)

Monte Carlo is powerful because:

- •It works in *any dimension* (1D, 10D, 1000D).
- •The estimator is usually simple.
- •You can attach *error bars* using variance.

### What you pay

Monte Carlo is not magic; it trades algebraic difficulty for computational effort:

- •Error decreases slowly: typically like 1/√N.
- •If f(X) has high variance, you need many samples.
- •Sampling from p might itself be hard (leading to MCMC later).

A useful mental model:

- •Deterministic numerical methods can converge fast in low dimension.
- •Monte Carlo converges slowly, but its rate does *not* deteriorate dramatically with dimension (often the main reason it wins in high-dimensional problems).

## Core Mechanic 1: Building the estimator (sampling and averaging)

Monte Carlo begins with a simple thought: if I = E[f(X)], then repeatedly observing f(X) and averaging should approximate I.

### Why the sample average makes sense

If X₁, …, X\_N are i.i.d. from p, then each f(X\_i) is an i.i.d. sample from the distribution of f(X). The expectation of f(X) is I.

So the sample mean:

Î\_N = (1/N) ∑\_{i=1}^N f(X\_i)

is a natural plug-in estimator.

### Unbiasedness (a key sanity check)

Under the condition that E[|f(X)|] exists (finite), we can compute:

E[Î\_N]

= E[(1/N) ∑\_{i=1}^N f(X\_i)]

= (1/N) ∑\_{i=1}^N E[f(X\_i)]

= (1/N) ∑\_{i=1}^N E[f(X)]

= (1/N) · N · I

= I

So **Î\_N is unbiased**.

Unbiasedness does *not* guarantee small error for finite N, but it does mean we are not systematically “off” in one direction.

### Consistency via LLN

By the (strong) Law of Large Numbers, if E[|f(X)|] < ∞:

Î\_N → I almost surely as N → ∞

This is the convergence guarantee: with enough samples, the estimate stabilizes.

### Interpreting Monte Carlo as “integration by sampling”

Many integrals can be rewritten in expectation form. Suppose you want:

J = ∫\_a^b g(x) dx

Pick a distribution over [a, b]. The most common is uniform:

X ∼ Uniform(a, b), p(x) = 1/(b−a)

Then:

E[g(X)]

= ∫\_a^b g(x) · (1/(b−a)) dx

Multiply both sides by (b−a):

∫\_a^b g(x) dx = (b−a) E[g(X)]

So a Monte Carlo estimator for J is:

Ĵ\_N = (b−a) (1/N) ∑\_{i=1}^N g(X\_i), X\_i ∼ Uniform(a,b)

This is the basic Monte Carlo integration recipe.

### A geometric view: estimating areas/volumes

A classic Monte Carlo use case is estimating the area of a shape S inside a bounding box B. If X is uniform over B:

P(X ∈ S) = Area(S)/Area(B)

So Area(S) = Area(B) · P(X ∈ S)

Estimate P(X ∈ S) with an average of indicator values:

Î\_N = (1/N) ∑\_{i=1}^N 1{X\_i ∈ S}

This viewpoint is important because it shows:

- •Monte Carlo works with *indicator functions*.
- •The same averaging principle handles probability estimation and integration.

### Practical detail: randomness as a resource

Computers produce pseudo-random numbers. For Monte Carlo you typically need:

- •A uniform(0,1) generator
- •Transformations to sample from other distributions (e.g., normal)

Many Monte Carlo algorithms are really about constructing samples from p efficiently. In this node, we assume we can sample from p directly (later, MCMC removes this assumption).

### Implementation skeleton

A minimal Monte Carlo estimator looks like:

1. 1)Choose p (a distribution you can sample from).
2. 2)Define f(x) so that E\_p[f(X)] is your quantity of interest.
3. 3)Draw samples X₁, …, X\_N.
4. 4)Compute Î\_N = (1/N)∑ f(X\_i).
5. 5)Quantify uncertainty (next section).

## Core Mechanic 2: Error is governed by variance (1/√N and why variance reduction matters)

Monte Carlo is simple to write down, but to use it well you must understand **how the error behaves**.

### Why error analysis matters

If Monte Carlo error decreased like 1/N, doubling samples would halve your error. But the typical scaling is slower: **1/√N**.

That means:

- •To reduce error by 10×, you need about 100× more samples.
- •You should often spend effort reducing variance instead of brute-force sampling.

### Variance of the Monte Carlo estimator

Assume X₁, …, X\_N are i.i.d. from p and Var(f(X)) is finite.

Let μ = E[f(X)] = I and σ² = Var(f(X)).

Compute Var(Î\_N):

Î\_N = (1/N) ∑\_{i=1}^N f(X\_i)

Because the samples are independent:

Var(Î\_N)

= Var((1/N) ∑ f(X\_i))

= (1/N²) ∑ Var(f(X\_i))

= (1/N²) · N · σ²

= σ² / N

So the standard deviation (standard error) is:

SD(Î\_N) = σ / √N

This directly yields the typical Monte Carlo error scale.

### Root-mean-square error (RMSE)

RMSE is a clean “average size of error” measure:

RMSE(Î\_N) = √(E[(Î\_N − I)²])

For an unbiased estimator, RMSE equals the standard deviation:

E[Î\_N] = I ⇒ RMSE(Î\_N) = √(Var(Î\_N)) = σ/√N

So, in the unbiased Monte Carlo setting:

RMSE ≈ √(Var(f(X))/N)

This is the key performance law.

### The Central Limit Theorem (practical error bars)

LLN tells you convergence eventually, but CLT tells you what happens at large finite N.

Under mild conditions:

√N (Î\_N − I) ⇒ Normal(0, σ²)

Equivalently:

Î\_N ≈ Normal(I, σ²/N)

So an approximate 95% confidence interval is:

Î\_N ± 1.96 · (σ/√N)

In practice σ is unknown, so you estimate it from the samples:

s² = (1/(N−1)) ∑\_{i=1}^N (f(X\_i) − Î\_N)²

Then use s/√N as the estimated standard error.

### Why variance is the real enemy

Notice what the formula depends on:

- •N (samples)
- •Var(f(X)) (problem-dependent)

You can always increase N, but if Var(f(X)) is huge, you may need an impractical amount of computation.

So Monte Carlo practice is often: change *how you sample* or *how you write the expectation* so that the variance drops.

### Variance reduction (preview-level)

Here are common variance reduction ideas (you don’t need to master all here, but you should recognize them):

| Technique | Core idea | When it helps | Typical tradeoff |
| --- | --- | --- | --- |
| Control variates | Use a correlated quantity with known expectation to cancel noise | When you can find a strong correlated control | Requires analytic expectation of control |
| Antithetic variates | Sample negatively correlated pairs | Symmetric problems, monotone f | Needs special sampling design |
| Stratified sampling | Force coverage across regions | When distribution has important subregions | More bookkeeping |
| Importance sampling | Sample more from “important” regions and reweight | Rare events, heavy tails, sharp peaks | Can explode variance if proposal is bad |

The unifying idea: **variance reduction improves accuracy at fixed N**.

### Independence assumption (and why MCMC will matter)

The clean variance result Var(Î\_N)=σ²/N relies on independence.

If samples are dependent (as in Markov chains), the estimator still often converges, but the effective sample size is lower:

Var(Î\_N) ≈ (σ²\_eff)/N

where σ²\_eff > σ² when there is positive autocorrelation.

This is the bridge to [MCMC](/tech-tree/mcmc/): when direct sampling is hard, you accept dependence and then analyze it carefully.

### A pacing check: what you should feel confident about now

At this point, you should be able to:

- •Recognize I = E\_p[f(X)] as an integral/sum under p.
- •Write down Î\_N as a sample average.
- •Predict error decreases like 1/√N.
- •Understand that reducing Var(f(X)) is as valuable as increasing N.

## Application/Connection: Monte Carlo for integration and simulation (and the road to MCMC)

Monte Carlo is both a numerical integration tool and a simulation framework. The same estimator supports many workflows.

## 1) Monte Carlo integration in higher dimensions

A major reason Monte Carlo is famous: high-dimensional integrals are painful for grid methods.

Suppose you want:

I = ∫\_{ℝ^d} h(**x**) d**x**

If you can choose a distribution p(**x**) that covers the important region, rewrite:

I = ∫ h(**x**) d**x**

= ∫ (h(**x**)/p(**x**)) p(**x**) d**x**

= E\_p[ h(X)/p(X) ]

Then estimate:

Î\_N = (1/N) ∑\_{i=1}^N h(X\_i)/p(X\_i), X\_i ∼ p

This is the general “change of measure” trick that leads directly to **importance sampling**.

## 2) Simulation to estimate system performance

Often you don’t have a closed-form model; you have a simulator. Monte Carlo says:

- •Randomly generate inputs.
- •Run the simulator.
- •Average the outputs.

Example template:

- •X = random demand, noise, arrivals, etc.
- •f(X) = cost from your simulation.
- •I = E[f(X)] = expected cost.

The estimator is still Î\_N.

## 3) Estimating probabilities as expectations

Probabilities are expectations of indicators:

P(A) = E[1{A}]

So if you can simulate the experiment producing event A, you can estimate the probability by:

P̂\_N(A) = (1/N) ∑ 1{A\_i}

This becomes crucial for:

- •rare event probabilities
- •reliability and risk

But note: for rare events, 1{A} has very small mean and may have problematic variance relative to the mean, motivating specialized methods (often importance sampling).

## 4) Choosing N based on desired accuracy

Since SD(Î\_N) ≈ σ/√N, to target a standard error ≤ ε:

σ/√N ≤ ε

Solve for N:

√N ≥ σ/ε

N ≥ (σ/ε)²

This is the core scaling law.

Two important practical notes:

1) σ is unknown; estimate it from a pilot run.

2) If f has heavy tails (variance very large or infinite), the CLT-based planning can fail; you may need robust methods or different parameterizations.

## 5) Connection to MCMC

Everything so far assumed you can sample X ∼ p easily.

In Bayesian inference, p might be a posterior distribution:

p(θ | data) ∝ p(data | θ) p(θ)

Often you can evaluate p up to a constant but cannot sample from it directly.

MCMC methods construct a Markov chain whose stationary distribution is p and then approximate:

E\_p[f(θ)] ≈ (1/N) ∑ f(θ\_i)

So MCMC is best understood as:

- •Monte Carlo estimator is the same.
- •The sampling mechanism changes (dependent samples).
- •Error analysis must account for autocorrelation.

If Monte Carlo is the “averaging engine,” MCMC is one of the main ways to generate the inputs to that engine.

## 6) A compact mental checklist

When applying Monte Carlo, ask:

1) What exactly is I? (Write it as E\_p[f(X)].)

2) Can I sample from p? If not, do I need a different p or MCMC?

3) What is Var(f(X)) likely to be? Where does it get large?

4) Do I need variance reduction to make this feasible?

5) How will I report uncertainty (standard error / confidence interval)?

That workflow is the practical “shape” of Monte Carlo methods.

## Worked Examples (3)

### Estimating an integral via Uniform sampling

Estimate I = ∫\_0^1 x² dx using Monte Carlo, and derive the estimator’s variance and RMSE in closed form.

1. Rewrite as an expectation under Uniform(0,1):

   Let X ∼ Uniform(0,1).

   Then p(x)=1 on [0,1], so

   E[X²] = ∫\_0^1 x² · 1 dx = ∫\_0^1 x² dx = I.
2. So the Monte Carlo estimator is:

   Î\_N = (1/N) ∑\_{i=1}^N X\_i²,

   with X\_i i.i.d. ∼ Uniform(0,1).
3. Compute the true value (for reference):

   I = ∫\_0^1 x² dx

   = [x³/3]\_0^1

   = 1/3.
4. Compute variance of f(X)=X².

   First compute E[X²] and E[X⁴]:

   E[X²] = 1/3.

   E[X⁴] = ∫\_0^1 x⁴ dx = [x⁵/5]\_0^1 = 1/5.

   So

   Var(X²) = E[X⁴] − (E[X²])²

   = 1/5 − (1/3)²

   = 1/5 − 1/9

   = (9−5)/45

   = 4/45.
5. Compute variance of the estimator:

   Var(Î\_N) = Var(X²)/N = (4/45)/N.
6. Compute RMSE (unbiased case):

   RMSE(Î\_N) = √(Var(Î\_N))

   = √((4/45)/N)

   = (2/√45) · 1/√N

   = (2/(3√5)) · 1/√N.

**Insight:** Even in this friendly 1D integral, Monte Carlo converges like 1/√N. The constant depends on Var(f(X)); here it’s modest, so the estimator is fairly well-behaved.

### Estimating π via area probability (indicator Monte Carlo)

Use Monte Carlo to estimate π by sampling points uniformly in the square [−1,1]×[−1,1] and counting how many fall inside the unit circle.

1. Define the geometry:

   Let B be the square [−1,1]×[−1,1].

   Area(B)=4.

   Let S be the unit disk x² + y² ≤ 1.

   Area(S)=π·1²=π.
2. Convert area to probability:

   If (**X**,**Y**) is uniform over B, then

   P((**X**,**Y**) ∈ S) = Area(S)/Area(B) = π/4.
3. Express probability as an expectation:

   Define f(**X**,**Y**) = 1{X²+Y² ≤ 1}.

   Then

   E[f(**X**,**Y**)] = P((**X**,**Y**) ∈ S) = π/4.
4. Monte Carlo estimator:

   Draw i.i.d. samples (**X**\_i, **Y**\_i) uniform over B.

   Compute

   p̂\_N = (1/N) ∑\_{i=1}^N 1{X\_i²+Y\_i² ≤ 1}.

   Then estimate

   π̂\_N = 4 p̂\_N.
5. Quantify variance:

   Each indicator is Bernoulli with success probability p = π/4.

   So

   Var(f) = p(1−p).

   Thus

   Var(p̂\_N) = p(1−p)/N.

   And

   Var(π̂\_N) = 16 Var(p̂\_N)

   = 16 p(1−p)/N.
6. Interpret scaling:

   Since p≈0.785, p(1−p)≈0.168.

   So SD(π̂\_N) ≈ √(16·0.168/N) = √(2.688/N) ≈ 1.64/√N.

   To get ≈0.01 typical error you’d need on the order of (1.64/0.01)² ≈ 26,896 samples.

**Insight:** This iconic example shows both the universality and the slowness of Monte Carlo: the estimator is easy, but high precision requires many samples because error shrinks only like 1/√N.

### Confidence interval for a simulation output (unknown variance)

You simulate a random system and observe outputs f(X\_i). Show how to compute a Monte Carlo estimate and an approximate 95% confidence interval using the sample variance.

1. Run the simulation:

   Generate i.i.d. inputs X₁,…,X\_N ∼ p.

   Compute outputs Y\_i = f(X\_i).
2. Compute the Monte Carlo estimate:

   Î\_N = (1/N) ∑\_{i=1}^N Y\_i.
3. Estimate variance from data:

   Compute sample variance

   s² = (1/(N−1)) ∑\_{i=1}^N (Y\_i − Î\_N)².
4. Estimate standard error:

   SE ≈ s/√N.
5. Form an approximate 95% confidence interval:

   Using CLT,

   Î\_N ≈ Normal(I, σ²/N).

   Replace σ with s:

   CI₉₅% ≈ Î\_N ± 1.96 · (s/√N).

   (For small N, a t-interval with N−1 degrees of freedom is often used.)
6. Decide if you need more samples:

   If the half-width 1.96·s/√N is too large, increase N.

   Since half-width scales like 1/√N, reducing it by a factor k requires ≈k² more samples.

**Insight:** Monte Carlo is rarely just a point estimate. In practice you almost always want uncertainty reporting, and the sample variance gives you an operational way to do that.

## Key Takeaways

- ✓

  Most Monte Carlo problems start by expressing the target as an expectation: I = E\_p[f(X)].
- ✓

  The basic Monte Carlo estimator is the sample average: Î\_N = (1/N)∑ f(X\_i) with X\_i ∼ p.
- ✓

  Under mild conditions, Î\_N is unbiased: E[Î\_N]=I, and consistent by LLN.
- ✓

  If Var(f(X))=σ² is finite and samples are i.i.d., then Var(Î\_N)=σ²/N and SD(Î\_N)=σ/√N.
- ✓

  RMSE typically scales like 1/√N, so high precision can require many samples.
- ✓

  The constant in the error (σ) matters: variance reduction can be as important as increasing N.
- ✓

  The CLT provides approximate error bars: Î\_N ≈ Normal(I, σ²/N), enabling confidence intervals from the sample variance.
- ✓

  When direct sampling from p is hard, Monte Carlo remains the estimator but you need different sampling machinery—often [MCMC](/tech-tree/mcmc/).

## Common Mistakes

- ✗

  Forgetting to rewrite the target correctly as E\_p[f(X)] (missing a scaling factor like (b−a) in Uniform integration).
- ✗

  Assuming error decreases like 1/N instead of 1/√N, leading to unrealistic sample-size expectations.
- ✗

  Ignoring variance: using a Monte Carlo estimator with extremely high Var(f(X)) and being surprised by unstable results.
- ✗

  Reporting Î\_N without any uncertainty estimate (no standard error / confidence interval), making results hard to interpret.

## Practice

easy

(Integration as expectation) Use Monte Carlo to estimate J = ∫\_0^2 e^{−x} dx by sampling X ∼ Uniform(0,2). Write J as (b−a)E[g(X)] and give the estimator Ĵ\_N.

**Hint:** For X ∼ Uniform(0,2), p(x)=1/2 on [0,2]. Relate ∫ g(x) dx to E[g(X)].

Show solution

Let g(x)=e^{−x} and X ∼ Uniform(0,2).

Then

E[g(X)] = ∫\_0^2 e^{−x} · (1/2) dx.

So

∫\_0^2 e^{−x} dx = 2 E[e^{−X}].

Monte Carlo estimator:

Ĵ\_N = 2 · (1/N)∑\_{i=1}^N e^{−X\_i}, with X\_i i.i.d. ∼ Uniform(0,2).

easy

(Error scaling) Suppose Var(f(X)) = 9. How many i.i.d. samples N are needed so that SD(Î\_N) ≤ 0.1?

**Hint:** Use SD(Î\_N)=σ/√N with σ=√Var(f(X)).

Show solution

σ=√9=3.

We need 3/√N ≤ 0.1 ⇒ √N ≥ 30 ⇒ N ≥ 900.

medium

(Indicator variance) You estimate a probability p = P(A) using p̂\_N = (1/N)∑1{A\_i}. Derive Var(p̂\_N) and find the worst-case (largest) variance over p ∈ [0,1].

**Hint:** 1{A} is Bernoulli(p). The variance of Bernoulli(p) is p(1−p). Maximize this quadratic.

Show solution

Each indicator Z\_i=1{A\_i} is Bernoulli(p), so Var(Z\_i)=p(1−p).

Since p̂\_N is the mean of i.i.d. Z\_i,

Var(p̂\_N)=p(1−p)/N.

The function p(1−p)=p−p² is maximized at p=1/2, giving maximum variance (1/4)/N.

## Connections

Next, extend Monte Carlo to cases where direct sampling is difficult: [MCMC](/tech-tree/mcmc/).

Related foundations you may want to review or connect:

- •[Law of Large Numbers](/tech-tree/law-of-large-numbers/)
- •[Central Limit Theorem](/tech-tree/central-limit-theorem/)
- •[Variance and Standard Deviation](/tech-tree/variance/)
- •[Importance Sampling](/tech-tree/importance-sampling/)

Quality: A (4.4/5)

[← back to tree](/tech-tree/)[browse all →](/tech-tree/inventory/)
