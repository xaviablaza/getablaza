---
title: Conjugate Priors
description: Beta-Binomial, Normal-Normal, Gamma-Poisson conjugacy. Closed-form posterior updates. Exponential family and sufficient statistics.
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
permalink: /tech-tree/conjugate-priors/
---

[←Back to Tech Tree](/tech-tree/)

[inventory](/tech-tree/inventory/)[coverage](/tech-tree/coverage/)

# Conjugate Priors

Probability & StatisticsDifficulty: ★★★★☆Depth: 8Unlocks: 3

Beta-Binomial, Normal-Normal, Gamma-Poisson conjugacy. Closed-form posterior updates. Exponential family and sufficient statistics.

## Prerequisites (2)

[Bayesian Inference5 atoms](/tech-tree/bayesian-inference/)[Common Distributions6 atoms](/tech-tree/common-distributions/)

## Unlocks (2)

[Hierarchical Bayesian Modelslvl 5](/tech-tree/hierarchical-models/)[Bayesian Forecastinglvl 5](/tech-tree/bayesian-forecasting/)

Advanced Learning Details

### Graph Position

84

Depth Cost

3

Fan-Out (ROI)

1

Bottleneck Score

8

Chain Length

Conjugate priors turn Bayesian updating from numerical slog into simple algebra: with the right prior the posterior stays in the same family and updates are closed-form.

TL;DR:

A conjugate prior is a prior distribution that, when combined with a likelihood from a given family, yields a posterior in the same distributional family — enabling closed-form posterior updates (Beta-Binomial, Gamma-Poisson, Normal-Normal) and exposing sufficient statistics via the exponential-family structure.

## What Is a Conjugate Prior?

Definition and motivation

A conjugate prior for a likelihood family is a prior distribution p(θ) such that the posterior p(θ | data) lies in the same parametric family as p(θ). Conjugacy is valuable because it turns Bayesian Inference (the prerequisite where we update priors with likelihoods to get posteriors) into simple algebraic updates instead of requiring numerical integration or sampling.

Formal statement

If the likelihood p(x | θ) belongs to a family L and the prior p(θ) belongs to a family P, we say P is conjugate to L if for any dataset x the posterior p(θ | x) ∈ P. The algebraic consequence is that the posterior parameters are updated by adding data-dependent terms to prior parameters: these update rules are closed form and often involve sufficient statistics (sums, counts, means).

Why care?

- •Computational efficiency: closed-form updates avoid MCMC when the model uses conjugate pairs.
- •Interpretability: updates are simple additions (e.g., add successes and failures to Beta parameters).
- •Predictive distributions: marginalizing parameters often yields known, simple predictive distributions (Beta-Binomial, Negative Binomial from Gamma-Poisson mix).
- •Building blocks: conjugate pairs form the core of hierarchical models, empirical Bayes, Kalman filters, and message passing.

A simple motivating example (Beta-Binomial)

In Common Distributions (prerequisite) we learned the Binomial likelihood for n Bernoulli trials with success probability θ and the Beta distribution as a flexible prior on θ. The Beta(a,b) density is

p(θ)=Γ(a+b)Γ(a)Γ(b)θa−1(1−θ)b−1,0<θ<1.p(\theta)=\frac{\Gamma(a+b)}{\Gamma(a)\Gamma(b)}\theta^{a-1}(1-\theta)^{b-1}, \quad 0<\theta<1.p(θ)=Γ(a)Γ(b)Γ(a+b)​θa−1(1−θ)b−1,0<θ<1.

The Binomial likelihood for k successes in n trials is

p(k∣θ)=(nk)θk(1−θ)n−k.p(k|\theta)=\binom{n}{k}\theta^{k}(1-\theta)^{n-k}.p(k∣θ)=(kn​)θk(1−θ)n−k.

Multiply prior and likelihood to get posterior up to normalization:

p(θ∣k,n)∝θa−1+k(1−θ)b−1+n−k,p(\theta|k, n) \propto \theta^{a-1+k}(1-\theta)^{b-1+n-k},p(θ∣k,n)∝θa−1+k(1−θ)b−1+n−k,

which is again a Beta distribution: Beta(a+k, b+n-k). This is conjugacy: Beta is conjugate to Binomial.

Numeric example (concrete)

Let the prior be Beta(2,3) (so a=2, b=3). Observe k=8 successes in n=20 trials. Posterior is:

Posterior =Beta(a+k,b+n−k)=Beta(2+8,  3+20−8)=Beta(10,15).\text{Posterior }=\text{Beta}(a+k, b+n-k)=\text{Beta}(2+8,\;3+20-8)=\text{Beta}(10,15).Posterior =Beta(a+k,b+n−k)=Beta(2+8,3+20−8)=Beta(10,15).

So the posterior mean is 1010+15=1025=0.4\frac{10}{10+15}=\frac{10}{25}=0.410+1510​=2510​=0.4. This single arithmetic update — add successes to a, failures to b — is the essence of conjugacy.

Intuition from sufficient statistics

Conjugate updates typically depend only on a small set of summary statistics of the data (sufficient statistics). For Binomial/Bernoulli that statistic is the count of successes k (or equivalently the sample mean times n). This is the same reason the Beta prior only needs two parameters (a,b): they act like pseudo-counts that add to the observed counts.

Preview of families we will study

- •Beta-Binomial (Bernoulli/Binomial likelihood + Beta prior)
- •Gamma-Poisson (Poisson likelihood + Gamma prior)
- •Normal-Normal (Normal likelihood with known variance + Normal prior on mean)

Each produces closed-form posterior parameters, posterior predictive distributions with closed forms, and clear sufficient statistics.

## Core Mechanic 1: Beta-Binomial and Gamma-Poisson Conjugacy

Beta-Binomial conjugacy — derivation and predictive distribution

Setup. Observations x\_1, ..., x\_n are iid Bernoulli(θ) (or equivalently we observe k successes in n Binomial(n,θ) trials). Prior: θ ~ Beta(a,b). Likelihood: p(k|θ)=\binom{n}{k}θ^{k}(1-θ)^{n-k}. Posterior (derive):

p(θ∣k,n)∝θa−1(1−θ)b−1⋅θk(1−θ)n−k=θa+k−1(1−θ)b+n−k−1.p(\theta|k,n) \propto \theta^{a-1}(1-\theta)^{b-1} \cdot \theta^{k}(1-\theta)^{n-k} = \theta^{a+k-1}(1-\theta)^{b+n-k-1}.p(θ∣k,n)∝θa−1(1−θ)b−1⋅θk(1−θ)n−k=θa+k−1(1−θ)b+n−k−1.

Hence

θ∣k,n∼Beta(a+k,  b+n−k).\theta|k,n \sim \text{Beta}(a+k,\; b+n-k).θ∣k,n∼Beta(a+k,b+n−k).

Numeric example. Prior Beta(1,1) (uniform), observe k=30 successes in n=100. Posterior is Beta(1+30, 1+70)=Beta(31,71). Posterior mean = 31/102 ≈ 0.3039.

Posterior predictive for a single future Bernoulli trial

The posterior predictive probability that the next trial is a success is

p(xnew=1∣k,n)=∫01θ  p(θ∣k,n) dθ=a+ka+b+n.p(x\_{\text{new}}=1 | k,n) = \int\_0^1 \theta \; p(\theta|k,n) \, d\theta = \frac{a+k}{a+b+n}.p(xnew​=1∣k,n)=∫01​θp(θ∣k,n)dθ=a+b+na+k​.

Numeric example: with Beta(1,1) prior and k=30, n=100, this equals (1+30)/(1+1+100)=31/102 ≈ 0.3039.

Predictive for m future trials (Beta-Binomial)

The predictive distribution for the number y of successes in m future trials (m>0) is the Beta-Binomial:

p(y∣k,n)=(my)B(a+k+y,b+n−k+m−y)B(a+k,b+n−k),p(y|k,n)=\binom{m}{y} \frac{B(a+k+y, b+n-k+m-y)}{B(a+k,b+n-k)},p(y∣k,n)=(ym​)B(a+k,b+n−k)B(a+k+y,b+n−k+m−y)​,

where B(·,·) is the Beta function. Numeric example: with prior Beta(2,3), observed k=8,n=20, compute probability of y=2 successes in m=5 future trials:

Posterior parameters: a'=10, b'=15. Then

p(y=2)=(52)B(10+2,15+5−2)B(10,15)=10⋅B(12,18)B(10,15).p(y=2)=\binom{5}{2}\frac{B(10+2,15+5-2)}{B(10,15)} =10\cdot\frac{B(12,18)}{B(10,15)}.p(y=2)=(25​)B(10,15)B(10+2,15+5−2)​=10⋅B(10,15)B(12,18)​.

You can compute B via Gamma: B(12,18)=\Gamma(12)\Gamma(18)/\Gamma(30) etc., or use software. The closed form keeps things analytic.

Gamma-Poisson conjugacy — derivation and predictive distribution

Setup. Observed counts x\_1,...,x\_n drawn iid Poisson(λ). Likelihood:

p(x∣λ)=∏i=1ne−λλxixi!=e−nλλ∑xi⋅∏i1xi!.p({\bf x}|\lambda)=\prod\_{i=1}^n e^{-\lambda}\frac{\lambda^{x\_i}}{x\_i!}=e^{-n\lambda}\lambda^{\sum x\_i} \cdot \prod\_i\frac{1}{x\_i!}.p(x∣λ)=i=1∏n​e−λxi​!λxi​​=e−nλλ∑xi​⋅i∏​xi​!1​.

Prior: λ ~ Gamma(α, β) with the rate parametrization (shape α, rate β) so

p(λ)=βαΓ(α)λα−1e−βλ,  λ>0.p(\lambda)=\frac{\beta^{\alpha}}{\Gamma(\alpha)}\lambda^{\alpha-1}e^{-\beta\lambda},\;\lambda>0.p(λ)=Γ(α)βα​λα−1e−βλ,λ>0.

Multiply prior and likelihood (ignore data-only constants):

p(λ∣x)∝λα−1+∑xie−(β+n)λ.p(\lambda|{\bf x}) \propto \lambda^{\alpha-1+\sum x\_i} e^{-(\beta+n)\lambda}.p(λ∣x)∝λα−1+∑xi​e−(β+n)λ.

This is Gamma(α + Σ x\_i, β + n). Numeric example: prior Gamma(2,1) (α=2,β=1). Data x = {3,2,4} => Σ x\_i = 9, n=3. Posterior: Gamma(2+9, 1+3) = Gamma(11,4). Posterior mean = (α')/(β') = 11/4 = 2.75.

Predictive distribution for a new observation

Marginalizing λ yields a closed-form predictive for a new count x':

p(x′∣x)=∫0∞p(x′∣λ)p(λ∣x) dλ=Γ(α′+x′)Γ(α′) x′!(β′β′+1)α′(1β′+1)x′,p(x'|{\bf x}) = \int\_0^{\infty} p(x'|\lambda) p(\lambda|{\bf x}) \, d\lambda = \frac{\Gamma(\alpha'+x')}{\Gamma(\alpha')\, x'!} \left(\frac{\beta'}{\beta'+1}\right)^{\alpha'} \left(\frac{1}{\beta'+1}\right)^{x'},p(x′∣x)=∫0∞​p(x′∣λ)p(λ∣x)dλ=Γ(α′)x′!Γ(α′+x′)​(β′+1β′​)α′(β′+11​)x′,

where α' = α+Σ x\_i and β' = β+n. This is a form of the (Poisson–Gamma) Negative Binomial-like mixture. Numeric example: With prior Gamma(2,1) and data {3,2,4} we had α'=11, β'=4. The predictive probability that next count x'=2 is

p(x′=2)=Γ(13)Γ(11)⋅2!(45)11(15)2.p(x'=2)=\frac{\Gamma(13)}{\Gamma(11)\cdot 2!}\left(\frac{4}{5}\right)^{11}\left(\frac{1}{5}\right)^2.p(x′=2)=Γ(11)⋅2!Γ(13)​(54​)11(51​)2.

Compute numerically: Γ(13)/Γ(11)=11·12=132, so p=132/(2) · (4/5)^{11} · (1/5)^2 =66 · (4/5)^{11} · (1/25). You can plug values to obtain a numerical probability.

What these two conjugate pairs teach

- •Posterior parameter updates are additive: add observed counts or sums to prior pseudo-counts or pseudo-sums.
- •Posterior predictive distributions are mixtures with closed forms, useful for forecasting and model checking.
- •The sufficient statistics (k for Binomial, Σx for Poisson) are the only necessary summaries of the data for updating the prior.

## Core Mechanic 2: Normal-Normal Conjugacy and the Exponential Family

Normal-Normal conjugacy (known variance) — closed-form posterior and derivation

Setup. Observations x\_1,...,x\_n are iid Normal(μ, σ^2) with known variance σ^2. Prior on the mean: μ ~ Normal(μ\_0, τ\_0^2). This is the standard conjugate pair for location with known variance. The posterior for μ is Normal(μ\_n, τ\_n^2) with

τn2=(1τ02+nσ2)−1,μn=τn2(μ0τ02+nxˉσ2).\tau\_n^2 = \left(\frac{1}{\tau\_0^2} + \frac{n}{\sigma^2}\right)^{-1}, \quad
\mu\_n = \tau\_n^2\left(\frac{\mu\_0}{\tau\_0^2} + \frac{n\bar{x}}{\sigma^2}\right).τn2​=(τ02​1​+σ2n​)−1,μn​=τn2​(τ02​μ0​​+σ2nxˉ​).

Derivation (completing the square). The likelihood is

p(x∣μ)∝exp⁡(−12σ2∑i=1n(xi−μ)2)=exp⁡(−n2σ2(xˉ−μ)2)⋅(data-only).p({\bf x}|\mu) \propto \exp\left(-\frac{1}{2\sigma^2}\sum\_{i=1}^n (x\_i-\mu)^2\right) = \exp\left(-\frac{n}{2\sigma^2}(\bar{x}-\mu)^2 \right)\cdot (\text{data-only}).p(x∣μ)∝exp(−2σ21​i=1∑n​(xi​−μ)2)=exp(−2σ2n​(xˉ−μ)2)⋅(data-only).

The prior is

p(μ)∝exp⁡(−12τ02(μ−μ0)2).p(\mu) \propto \exp\left(-\frac{1}{2\tau\_0^2}(\mu-\mu\_0)^2\right).p(μ)∝exp(−2τ02​1​(μ−μ0​)2).

Multiplying and completing the square in μ gives a Normal posterior with precision (inverse variance) equal to the sum of prior precision and data precision: $1/\tau\_n^2 = 1/\tau\_0^2 + n/\sigma^2$. The posterior mean is a precision-weighted average of μ\_0 and the sample mean \bar{x}.

Numeric example. Prior μ\_0=0, τ\_0^2=1. Known σ^2=2. Data: x = {1.2, 0.8, 1.5} so n=3, \bar{x}=(1.2+0.8+1.5)/3=3.5/3≈1.1667.

Compute precisions: 1/τ\_0^2 = 1, n/σ^2 = 3/2 = 1.5, so 1/τ\_n^2 = 2.5 => τ\_n^2 = 0.4. Posterior mean μ\_n = 0.4*(0/1 + 3*1.1667/2) = 0.4\*(1.75005) ≈ 0.70002. So μ|data ≈ N(0.7000, 0.4).

Posterior predictive for a new observation x\_{new}

The predictive distribution integrates over μ and is Normal with mean μ\_n and variance σ^2 + τ\_n^2:

xnew∣x∼N(μn,σ2+τn2).x\_{new}|{\bf x} \sim N(\mu\_n, \sigma^2 + \tau\_n^2).xnew​∣x∼N(μn​,σ2+τn2​).

Numeric example: variance = 2 + 0.4 = 2.4, so predictive standard deviation ≈ 1.549.

Sufficient statistics and reduction of data

For Normal with known variance, the sufficient statistic for μ is the sample mean \bar{x} (and n). That is, the posterior depends only on n and \bar{x}, not on the full sample. In other words, the data reduce to two numbers: n and \bar{x}. This mirrors the Beta-Binomial case where the sufficient statistic is k.

Exponential family and general conjugacy structure

Many common likelihoods (Bernoulli/Binomial, Poisson, Normal, Exponential, Gamma, etc.) belong to the exponential family. A one-parameter exponential family has density (w.r.t. base measure):

p(x∣η)=h(x)exp⁡(ηT(x)−A(η)),p(x|\eta) = h(x)\exp\left(\eta T(x) - A(\eta)\right),p(x∣η)=h(x)exp(ηT(x)−A(η)),

where η is the natural parameter, T(x) is the sufficient statistic for a single observation, and A(η) is the log-partition function.

A natural conjugate prior for η has the form

p(η∣ξ,ν)∝exp⁡(ηξ−νA(η))⋅g(ξ,ν),p(\eta|\xi,\nu) \propto \exp\left(\eta\xi - \nu A(\eta)\right)\cdot g(\xi,\nu),p(η∣ξ,ν)∝exp(ηξ−νA(η))⋅g(ξ,ν),

where ξ and ν are hyperparameters encoding prior pseudo-observations and g normalizes. After observing n iid samples with sufficient statistic S = Σ T(x\_i), the posterior becomes

p(η∣S,ξ,ν)∝exp⁡(η(ξ+S)−(ν+n)A(η)),p(\eta|S,\xi,\nu) \propto \exp\left(\eta(\xi+S) - (\nu+n)A(\eta)\right),p(η∣S,ξ,ν)∝exp(η(ξ+S)−(ν+n)A(η)),

so updates are additive: ξ' = ξ + S, ν' = ν + n. This is the generic conjugate-update pattern.

Concrete mapping to Beta-Binomial

For Bernoulli, T(x)=x and A(η)=\log(1+e^{η}). The Beta prior in θ-space corresponds to a conjugate prior in the natural parameter space via a change of variables; however, the additive-pseudo-count view is simplest: in Beta(a,b) the parameters (a-1, b-1) can be seen as pseudo-success and pseudo-failure counts that add to observed counts.

Why this matters

- •Exponential-family conjugacy yields compact, interpretable updates and exposes sufficient statistics.
- •It provides the algebraic backbone for many Bayesian algorithms (e.g., variational Bayes, belief propagation) where conjugacy leads to closed-form coordinate updates.
- •Recognizing natural parameters and sufficient statistics lets you derive conjugate priors for new exponential-family models quickly.

## Applications and Connections

Practical use cases

1) A/B testing and online experimentation

In A/B tests with binary outcomes (click/no-click), Beta-Binomial conjugacy lets you update beliefs about conversion probabilities in real time. Example: uniform-prior Beta(1,1). Group A observes 30 successes in 100 trials → Beta(31,71). Group B observes 40 successes in 120 trials → Beta(41,81). The probability that p\_A > p\_B can be computed analytically via Beta integrals or approximated via Monte Carlo sampling from the two Betas. These closed forms make sequential decision rules easy (stop when P(p\_A>p\_B)>0.95).

Numeric snippet (compare posteriors). Posterior means: A = 31/102 ≈ 0.304, B = 41/122 ≈ 0.336. But the posterior distributions capture uncertainty; the probability p\_A>p\_B requires integrating their joint Beta densities and is tractable numerically.

2) Count data and rare-event smoothing

For estimating rates (traffic accidents per month, email arrivals), Poisson likelihood with Gamma prior gives a Gamma posterior. The Gamma prior acts as regularization: for small-sample areas it pulls extreme sample means toward the prior mean (empirical Bayes uses pooled data to set hyperparameters). Predicting future counts uses the Gamma–Poisson mixture (negative-binomial predictive) to capture over-dispersion beyond a simple Poisson.

3) Measurement, sensor fusion, and filtering

Normal-Normal conjugacy with known variance is exactly the static version of the Kalman filter's update step: combine prior estimate and new measurements weighted by their precisions. In many engineering settings where sensor noise variance is known, these closed-form updates are used continuously.

4) Hierarchical models and empirical Bayes

Conjugate models are building blocks for hierarchical Bayes. For example, modeling click rates p\_i for many websites with p\_i ~ Beta(α,β) and data Binomial for each site yields closed-form per-site posteriors. Empirical Bayes sets α,β via marginal likelihood (which can be computed for conjugate families), giving shrinkage estimates that pool information across units.

Connections to downstream methods

- •Variational inference and message passing exploit exponential-family conjugacy to produce closed-form coordinate updates. Learning these conjugate pairs prepares you to derive variational updates.
- •Gibbs sampling: when conditional posteriors are from conjugate families, Gibbs samplers simplify (draw from standard distributions instead of generic MCMC steps).
- •Predictive modeling: closed-form posterior predictive distributions supply analytic credible intervals and predictive checks.

Numeric case study (decision example)

Suppose a small clinic records 2 successes in 5 trials for a new treatment. With prior Beta(1,1), posterior Beta(3,4). The expected success probability is 3/7 ≈ 0.4286 and the predictive probability of next trial success is (3)/(7+1?) — careful: the predictive for a single Bernoulli is (a')/(a'+b') = 3/7 ≈ 0.4286 (same as posterior mean). If a competing treatment has posterior predictive 0.35, you might choose the new treatment. Conjugacy makes these computations trivial and transparent.

When conjugacy is not enough

Real models often lack conjugacy (complex likelihoods, non-exponential-family components). Still, conjugate models serve as approximations, initialization for numerical methods, or local updates within larger models (e.g., conditional conjugacy in parts of hierarchical models).

Summary

Conjugate priors give you closed-form Bayesian updates, analytic predictive distributions, and clear sufficient statistics. Recognizing conjugacy (or mapping a model into the exponential family) buys tractability and insight — foundational for modern Bayesian computation and modeling.

## Worked Examples (3)

### Beta-Binomial update (simple)

Prior: Beta(2,3). Data: observe k=8 successes out of n=15 Bernoulli trials. Compute the posterior and posterior mean.

1. Write prior parameters: a=2, b=3.
2. Write data: k=8 successes, n=15 trials, so failures = n-k = 7.
3. Posterior parameters: a' = a + k = 2 + 8 = 10; b' = b + (n - k) = 3 + 7 = 10.
4. Therefore posterior is Beta(10,10).
5. Posterior mean = a'/(a'+b') = 10/(10+10) = 10/20 = 0.5.

**Insight:** A Beta prior acts as pseudo-counts: the posterior parameters are simply prior counts plus observed counts. Here the prior expectation (2/5=0.4) is pulled toward the data (8/15≈0.533); the posterior mean 0.5 is between them.

### Gamma-Poisson with predictive

Prior: Gamma(3,2) (shape α=3, rate β=2). Data: observed daily counts {4,1,5,2} (n=4, sum Σx = 12). Compute the posterior for λ and the predictive probability that tomorrow's count equals 3.

1. Write prior parameters: α=3, β=2.
2. Sum data: n=4, Σx = 4+1+5+2 = 12.
3. Posterior parameters: α' = α + Σx = 3 + 12 = 15; β' = β + n = 2 + 4 = 6.
4. Posterior: λ | data ~ Gamma(15, 6) with mean α'/β' = 15/6 = 2.5.
5. Predictive for x'=3: use the marginal formula

   p(x'=3) = Γ(α'+3)/(Γ(α')3!) · (β'/(β'+1))^{α'} · (1/(β'+1))^{3}.
6. Plug numbers: Γ(18)/Γ(15) = 15·16·17 = 4080. Then 3! = 6, and (β'/(β'+1))^{α'} = (6/7)^{15}, (1/(β'+1))^{3} = (1/7)^{3}. So

   p = 4080/6 · (6/7)^{15} · (1/343) = 680 · (6/7)^{15} · (1/343).
7. Compute numerically if desired: (6/7)^{15} ≈ 0.1051, so p ≈ 680 · 0.1051 / 343 ≈ 715. - compute: 680\*0.1051≈71.468; divide by 343 ≈0.2085. So p ≈ 0.2085.

**Insight:** Gamma prior adds pseudo-counts to the total event rate; the predictive distribution accounts for parameter uncertainty and broadens the forecast relative to a plug-in Poisson with λ=posterior mean.

### Normal-Normal conjugacy (known variance) and credible interval

Prior: μ ~ N(1.0, 0.25) (μ\_0=1.0, τ\_0^2=0.25). Known observation variance σ^2 = 0.5. Data: x = {0.8, 1.2, 0.9, 1.5} (n=4). Compute posterior for μ and a 95% posterior credible interval for μ.

1. Compute sample mean: \bar{x} = (0.8+1.2+0.9+1.5)/4 = 4.4/4 = 1.1.
2. Compute precisions: 1/τ\_0^2 = 1/0.25 = 4. Data precision: n/σ^2 = 4/0.5 = 8. Sum precision = 12, so τ\_n^2 = 1/12 ≈ 0.083333.
3. Compute posterior mean: μ\_n = τ\_n^2*(μ\_0/τ\_0^2 + n\bar{x}/σ^2) = (1/12)*(1.0*4 + 4*1.1/0.5). Compute 4*1.1/0.5 = 4*2.2 = 8.8. So μ\_n = (1/12)*(4 + 8.8) = (1/12)*12.8 = 1.066666... ≈ 1.0667.
4. Posterior: μ | data ~ N(1.0667, 0.083333). Posterior standard deviation = sqrt(0.083333) ≈ 0.288675.
5. 95% credible interval (approx): μ\_n ± 1.96*sd ≈ 1.0667 ± 1.96*0.288675 ≈ 1.0667 ± 0.5659 ⇒ [0.5008, 1.6326].

**Insight:** Posterior mean is a precision-weighted average of prior mean and sample mean. The credible interval shrinks as data precision increases; here the data had higher precision (8) than the prior (4) so the posterior leans toward the sample mean.

## Key Takeaways

- ✓

  A conjugate prior yields a posterior in the same family as the prior; updates are closed-form additive changes to prior parameters using sufficient statistics.
- ✓

  Beta-Binomial: Beta(a,b) prior + Binomial(k|n,θ) ⇒ posterior Beta(a+k, b+n-k); predictive probability for the next success is (a+k)/(a+b+n). Example: Beta(2,3) + k=8,n=20 ⇒ Beta(10,15).
- ✓

  Gamma-Poisson: Gamma(α,β) prior + Poisson data (Σx) ⇒ posterior Gamma(α+Σx, β+n); predictive for new counts is the Poisson–Gamma mixture with a closed-form (Negative-Binomial-like) PMF. Example: Gamma(2,1) + counts {3,2,4} ⇒ Gamma(11,4).
- ✓

  Normal-Normal (known σ^2): Normal(μ\_0,τ\_0^2) prior + Normal likelihood ⇒ posterior Normal with precision equal to the sum of prior and data precisions, and mean equal to the precision-weighted average. Example calculations give explicit μ\_n and τ\_n^2.
- ✓

  Exponential-family conjugacy: if p(x|η)=h(x) exp(η·T(x)-A(η)), a conjugate prior can be written as exp(η·ξ - ν A(η)), and posterior updates are ξ' = ξ + Σ T(x\_i), ν' = ν + n.
- ✓

  Closed-form posteriors enable fast inference, predictive distributions, empirical Bayes, and are building blocks for hierarchical models, variational inference, Gibbs sampling, and message passing.

## Common Mistakes

- ✗

  Mixing rate and scale parameterizations for the Gamma distribution: Gamma(α,β) can be parametrized with rate β or scale θ=1/β. Using the wrong form changes posterior updates (e.g., β + n vs. β + n) — always specify whether β is rate or scale.
- ✗

  Forgetting to include both successes and failures when updating Beta parameters: the Beta update requires adding k to a and (n-k) to b. Adding only k (and ignoring failures) yields an incorrect posterior.
- ✗

  Using the posterior mean as a plug-in for predictive variance without accounting for uncertainty: e.g., for Poisson data, plugging λ̂ = E[λ|data] into Poisson(λ̂) underestimates predictive variance compared to integrating λ out using the Gamma–Poisson mixture.
- ✗

  Assuming conjugacy always holds: not all likelihoods have simple conjugate priors; forcing a conjugate prior (or misidentifying the sufficient statistics) can lead to wrong updates — check the algebra or map to the exponential-family form.

## Practice

easy

Easy: Beta-Binomial update. Prior Beta(3,3). You observe 12 successes out of 20 trials. Find the posterior distribution and its mean.

**Hint:** Add successes to a and failures to b: a' = a + k, b' = b + n - k.

Show solution

a' = 3 + 12 = 15; b' = 3 + 8 = 11. Posterior = Beta(15,11). Posterior mean = 15/(15+11) = 15/26 ≈ 0.5769.

medium

Medium: Predictive probability under Gamma-Poisson. Prior Gamma(2,3) (shape α=2, rate β=3). Data: counts {0,1,2,0,1} (n=5, Σx=4). Compute the predictive probability that the next day's count is 2.

**Hint:** Posterior α' = α + Σx, β' = β + n. Then use the marginal predictive formula for p(x').

Show solution

α' = 2 + 4 = 6; β' = 3 + 5 = 8. Predictive p(x'=2) = Γ(6+2)/(Γ(6)2!) · (β'/(β'+1))^{6} · (1/(β'+1))^{2}. Compute Γ(8)/Γ(6) = 6·7 = 42. So p = 42/2 · (8/9)^{6} · (1/9)^{2} = 21 · (8/9)^{6} · (1/81). Numerically (8/9)^{6}≈0.5132, so p≈21\*0.5132/81≈10.777/81≈0.1330.

hard

Hard: Exponential-family conjugacy derivation. Suppose the likelihood is a one-parameter exponential family p(x|η) = h(x) exp(η T(x) - A(η)). Show that the conjugate prior of the canonical form p(η|ξ,ν) ∝ exp(η ξ - ν A(η)) leads to posterior parameters ξ' = ξ + Σ T(x\_i) and ν' = ν + n, and then apply this general formula to derive the Beta-Binomial update mapping (identify η, T(x), A(η), ξ, and ν).

**Hint:** Multiply prior and likelihood for n iid observations, collect terms multiplying η and A(η), and read off the updated hyperparameters. For Bernoulli, rewrite likelihood in canonical form to find η = log(θ/(1-θ)).

Show solution

Posterior ∝ p(η|ξ,ν) · ∏\_{i=1}^n p(x\_i|η) ∝ exp(η ξ - ν A(η)) · ∏\_i h(x\_i) exp(η T(x\_i) - A(η)) = (data-only) · exp(η (ξ + Σ T(x\_i)) - (ν + n) A(η)). Thus posterior has the same canonical form with ξ' = ξ + Σ T(x\_i) and ν' = ν + n. For Bernoulli(θ), write p(x|θ) = θ^{x}(1-θ)^{1-x} = exp(x log θ + (1-x) log(1-θ)) = h(x) exp(η T(x) - A(η)) with η = log(θ/(1-θ)), T(x)=x, and A(η)=log(1+e^{η}). The conjugate prior in θ-space is Beta, which corresponds to pseudo-counts: choosing ξ = a-1 (sum of pseudo T) and ν = a+b-2 (pseudo sample size) yields posterior updates a' = a + Σ x, b' = b + n - Σ x. Equivalently, in the standard Beta parametrization, the update is a' = a + k, b' = b + n - k.

## Connections

Looking back: This lesson builds directly on Bayesian Inference (we used the prior×likelihood→posterior operation repeatedly) and Common Distributions (Bernoulli/Binomial, Poisson, Normal, Gamma, Beta). In Bayesian Inference, you learned the general Bayes rule; conjugate priors are special cases where Bayes rule yields algebraic, closed-form updates. In Common Distributions, you learned parametric forms; here we used those densities and simple algebra to derive posteriors.

Looking forward: mastering conjugacy and the exponential-family viewpoint enables several downstream techniques:

- •Hierarchical Bayesian modeling and Empirical Bayes (estimating hyperparameters analytically using marginal likelihoods built from conjugate forms).
- •Gibbs sampling: conditional posteriors are standard distributions when components are conjugate, making samplers efficient.
- •Variational inference and message passing: conjugacy gives closed-form coordinate updates because posteriors stay in the same family.
- •Kalman filters and state-space models: Normal-Normal conjugacy underlies the update equations.

Specific requirements: if you intend to implement online A/B testing, bandit algorithms with Beta priors, or count forecasting with Poisson–Gamma models, you'll directly use the formulas here. If you move to non-conjugate models, you will often approximate them via exponential-family conjugates (Laplace approximations, variational families), so understanding conjugacy is essential foundationally.

Quality: pending (0.0/5)

[← back to tree](/tech-tree/)[browse all →](/tech-tree/inventory/)
