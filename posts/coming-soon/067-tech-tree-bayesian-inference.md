---
title: Bayesian Inference
description: Updating probability distributions with data. Prior, likelihood, posterior.
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
permalink: /tech-tree/bayesian-inference/
---

[←Back to Tech Tree](/tech-tree/)

[inventory](/tech-tree/inventory/)[coverage](/tech-tree/coverage/)

# Bayesian Inference

Probability & StatisticsDifficulty: ★★★★☆Depth: 7Unlocks: 18

Updating probability distributions with data. Prior, likelihood, posterior.

## Interactive Visualization

⏮◀◀▶▶STEP0.25x1xZOOM

t=0s

## Core Concepts

- -Prior distribution: encoding beliefs about parameters before seeing data
- -Likelihood as a function of parameters: the data model evaluated as a function of the unknown parameter(s)
- -Posterior distribution: updated beliefs about parameters after observing data

## Key Symbols & Notation

p(theta | x) - posterior density (theta given observed data x)

## Essential Relationships

- -Bayes update: posterior(theta | x) = [prior(theta) \* likelihood(x | theta)] / evidence(x), where evidence(x) = integral over theta of prior(theta)\*likelihood(x | theta) dtheta

## Prerequisites (3)

[Bayes Theorem5 atoms](/tech-tree/bayes-theorem/)[Common Distributions6 atoms](/tech-tree/common-distributions/)[Maximum Likelihood Estimation6 atoms](/tech-tree/mle/)

## Unlocks (10)

[Bayesian Gameslvl 4](/tech-tree/bayesian-games/)[Bayesian Decision Theorylvl 4](/tech-tree/bayesian-decision-theory/)[Variational Autoencoderslvl 5](/tech-tree/vae/)[MCMClvl 4](/tech-tree/mcmc/)[Conjugate Priorslvl 4](/tech-tree/conjugate-priors/)[State-Space Modelslvl 4](/tech-tree/state-space-models/)[Bayesian Optimizationlvl 5](/tech-tree/bayesian-optimization/)[Auction Theorylvl 5](/tech-tree/auction-theory/)

+2 more...

## Referenced by (8)

Where this concept shows up in the operating-finance and personal-finance graphs.

### From Business (8)

[defect rateBusiness

Unknown defect rate is the canonical Bayesian inference problem - you place a prior distribution over the unknown parameter, observe pass/fail data, and compute the posterior distribution, which quantifies exactly how much uncertainty remains after evidence](/business/defect-rate/)[Value RealizationBusiness

Value realization is Bayesian updating in disguise: the customer holds a prior belief about product value, observes early experience as likelihood evidence, and updates their posterior. Slow value realization means weak early signals, so a skeptical prior barely moves - formalizing why first impressions dominate and why the churn window is front-loaded.](/business/value-realization/)[anchorBusiness

An anchor functions as a strong prior - you begin with the canonical form and update beliefs as each alternative concept is introduced, making the anchor-vs-alternatives structure a natural instance of prior-to-posterior updating](/business/anchor/)[Valuation UncertaintyBusiness

Valuing illiquid assets is fundamentally Bayesian - you hold a prior belief about value and update it with sparse evidence (comparable transactions, periodic appraisals, DCF assumptions), each observation shifting the posterior over true value](/business/valuation-uncertainty/)[AnchoringBusiness

Anchoring is formally modeled as insufficient updating from a prior. A rational Bayesian agent adjusts the posterior toward the likelihood of new evidence, but an anchored estimator places too much weight on the prior (the last project) and too little on the current data, producing a posterior biased toward the anchor.](/business/anchoring/)[Asset DriftBusiness

Regulatory knowledge accumulation is structurally Bayesian updating - each new regulation, ruling, or compliance event updates the firm's posterior beliefs about the regulatory landscape. The data moat IS the accumulated posterior; competitors start from the prior. The mathematical mechanism of 'knowledge accumulates' is prior-to-posterior refinement.](/business/asset-drift/)[institutional knowledgeBusiness

Institutional knowledge is accumulated priors - each observation tightens organizational posteriors, so firms with more data make better decisions with less uncertainty, which is exactly why data moats compound](/business/institutional-knowledge/)[Knowledge AssetBusiness

The mechanism by which a knowledge asset appreciates is Bayesian updating - the rubric encodes priors about quality, each application generates evidence, and refinements are posterior updates that converge on better evaluation criteria](/business/knowledge-asset/)

Advanced Learning Details

### Graph Position

84

Depth Cost

18

Fan-Out (ROI)

10

Bottleneck Score

7

Chain Length

### Cognitive Load

5

Atomic Elements

43

Total Elements

L3

Percentile Level

L3

Atomic Level

### All Concepts (16)

- - Parameters treated as random variables - represent unknown parameters by a prior distribution p(θ)
- - Likelihood as a function of parameters L(θ)=p(D|θ) (the data viewed as fixed, the function of θ)
- - Posterior distribution p(θ|D) - the full updated probability distribution over parameters after seeing data
- - Normalizing constant / marginal likelihood / evidence p(D)=∫ p(D|θ)p(θ) dθ (required to turn prior×likelihood into a proper posterior)
- - Posterior predictive distribution p(x\_new|D)=∫ p(x\_new|θ)p(θ|D) dθ for predicting new observations by integrating over parameter uncertainty
- - Conjugate priors - prior families chosen so posterior is in same parametric family as prior, enabling analytic updates
- - Maximum a posteriori (MAP) estimate - the parameter value that maximizes the posterior density (posterior mode)
- - Bayesian credible interval - interval containing a specified posterior probability for the parameter (interpretation differs from frequentist confidence interval)
- - Bayes factor / model evidence used for model comparison: ratio of marginal likelihoods of models
- - Sequential Bayesian updating - repeatedly applying Bayes rule so the posterior after one dataset becomes the prior for the next
- - Hierarchical (multilevel) Bayesian models - priors with hyperparameters (priors on priors) enabling partial pooling and modeling groups
- - Prior predictive distribution - distribution over possible datasets obtained by marginalizing parameters out under the prior
- - Uncertainty propagation by marginalization - incorporate parameter uncertainty in predictions and decisions by integrating over posterior instead of plugging in a point estimate
- - Approximate inference methods when analytic posterior is intractable: Markov Chain Monte Carlo (MCMC), importance sampling, variational inference
- - Monte Carlo estimation of posterior expectations - estimate integrals (e.g., posterior mean) by averaging functions evaluated on samples from the posterior
- - Interpretation and use of posterior summaries (posterior mean, median, mode, posterior variance) as point/uncertainty summaries

### Teaching Strategy

Quick unlock - significant prerequisite investment but simple final step. Verify prerequisites first.

You already know Bayes’ theorem as a rule for flipping conditionals: P(A|B) ∝ P(B|A)P(A). Bayesian inference is what happens when you treat the unknown quantity (often a parameter θ) as the “A” you want to reason about, and the observed dataset x as the “B” you’ve learned from—so your result is not a single best guess, but a whole updated distribution over plausible θ values.

TL;DR:

Bayesian inference updates beliefs about unknown parameters θ using data x via

p(θ∣x)=p(x∣θ) p(θ)p(x)wherep(x)=∫p(x∣θ)p(θ) dθ.p(\theta\mid x)=\frac{p(x\mid \theta)\,p(\theta)}{p(x)}\quad\text{where}\quad p(x)=\int p(x\mid\theta)p(\theta)\,d\theta.p(θ∣x)=p(x)p(x∣θ)p(θ)​wherep(x)=∫p(x∣θ)p(θ)dθ.

- •Prior p(θ): belief before data.
- •Likelihood p(x|θ): data model viewed as a function of θ.
- •Posterior p(θ|x): belief after data.
- •Evidence p(x): normalizer; also key for model comparison.

Conjugate priors make posteriors easy; otherwise you approximate (MCMC, variational inference).

## Prerequisites (and what you can skip if you don’t have calculus yet)

This node builds on ideas you may already know, but it’s easy to get tripped up by missing one small piece. Here’s the explicit checklist.

## Required prerequisites

### 1) Bayes’ theorem and conditional probability

You should be comfortable with:

- •Conditional probability: P(A∣B)=P(A∩B)P(B)P(A\mid B)=\frac{P(A\cap B)}{P(B)}P(A∣B)=P(B)P(A∩B)​.
- •Bayes’ theorem:

P(A∣B)=P(B∣A)P(A)P(B).P(A\mid B)=\frac{P(B\mid A)P(A)}{P(B)}.P(A∣B)=P(B)P(B∣A)P(A)​.

You should also understand the “proportional” form:

P(A∣B)∝P(B∣A)P(A)P(A\mid B)\propto P(B\mid A)P(A)P(A∣B)∝P(B∣A)P(A)

where the missing factor is “whatever makes it sum/integrate to 1.” Bayesian inference uses this proportionality constantly.

### 2) Common distributions (Bernoulli/binomial/Poisson/normal)

You should recognize probability mass/density functions and their parameters.

- •Bernoulli: x∈{0,1}x\in\{0,1\}x∈{0,1}, parameter θ\thetaθ.
- •Binomial: counts of successes in nnn trials.
- •Poisson: counts over time/space.
- •Normal: mean/variance.

### 3) Likelihood and MLE

You should know that the likelihood is the same expression as p(x∣θ)p(x\mid \theta)p(x∣θ) but interpreted as a function of θ\thetaθ for fixed observed xxx.

MLE chooses:

θ^MLE=arg⁡max⁡θp(x∣θ).\hat\theta\_{\text{MLE}} = \arg\max\_{\theta} p(x\mid\theta).θ^MLE​=argθmax​p(x∣θ).

Bayesian inference will generalize this: it returns a distribution over θ\thetaθ instead of one optimizer.

## Helpful (but optional) prerequisite: calculus/integration intuition

The “evidence” (also called the marginal likelihood) is:

p(x)=∫p(x∣θ)p(θ) dθp(x)=\int p(x\mid\theta)p(\theta)\,d\thetap(x)=∫p(x∣θ)p(θ)dθ

(or a sum for discrete θ\thetaθ). If you don’t have calculus yet, you can still learn most of Bayesian inference by treating this as “the normalization constant” and focusing on proportional reasoning:

p(θ∣x)∝p(x∣θ)p(θ).p(\theta\mid x) \propto p(x\mid\theta)p(\theta).p(θ∣x)∝p(x∣θ)p(θ).

You can do many practical updates with conjugate priors without doing the integral yourself.

## A crucial clarification (common misconception)

People often say “use a flat/uninformative prior.” Two important caveats:

1) **‘Flat’ depends on parameterization.** A prior that is uniform in θ\thetaθ is not uniform in ϕ=g(θ)\phi=g(\theta)ϕ=g(θ). For example, if ϕ=θ2\phi=\theta^2ϕ=θ2, then a uniform prior in θ\thetaθ induces a non-uniform prior in ϕ\phiϕ.

2) “Non-informative” is subtle. Some priors are designed to be less informative under reparameterizations (e.g., Jeffreys priors), but there is no universal free lunch.

Keep this in mind as we talk about priors: they encode assumptions, and assumptions should be made explicit.

## What Is Bayesian Inference?

## The big idea: uncertainty about parameters is a first-class object

In frequentist statistics, parameters are fixed but unknown. In Bayesian statistics, parameters are treated as uncertain quantities described by a probability distribution.

You observe data xxx (which might be a dataset like x=(x1,…,xn)x=(x\_1,\dots,x\_n)x=(x1​,…,xn​)), and you want to reason about an unknown parameter (or parameters) θ\thetaθ.

Bayesian inference is the process of updating your beliefs about θ\thetaθ after seeing xxx.

## The core equation

Bayes’ theorem in density form is:

p(θ∣x)=p(x∣θ) p(θ)p(x)p(\theta\mid x)=\frac{p(x\mid \theta)\,p(\theta)}{p(x)}p(θ∣x)=p(x)p(x∣θ)p(θ)​

Each term has a distinct job:

- •**Prior** p(θ)p(\theta)p(θ): what you believe about θ\thetaθ before seeing this data.
- •**Likelihood** p(x∣θ)p(x\mid\theta)p(x∣θ): how likely the observed data is if θ\thetaθ were the true parameter.
- •**Posterior** p(θ∣x)p(\theta\mid x)p(θ∣x): what you believe after seeing data.
- •**Evidence** p(x)p(x)p(x): the normalization constant making the posterior integrate to 1.

Often we write the update in proportional form:

p(θ∣x)∝p(x∣θ)p(θ).p(\theta\mid x) \propto p(x\mid\theta)p(\theta).p(θ∣x)∝p(x∣θ)p(θ).

That proportional form is not a shortcut; it’s a mindset: start by multiplying prior × likelihood, then normalize.

## Why this is more than “just Bayes’ theorem”

Bayes’ theorem is a single identity. Bayesian inference is a workflow:

1) Choose a probabilistic model for data: p(x∣θ)p(x\mid\theta)p(x∣θ).

2) Choose a prior over unknowns: p(θ)p(\theta)p(θ).

3) Compute or approximate the posterior: p(θ∣x)p(\theta\mid x)p(θ∣x).

4) Use the posterior for decisions/predictions.

This workflow forces you to express assumptions.

## A useful mental picture: prior × likelihood = unnormalized posterior

Suppose θ\thetaθ is one-dimensional.

- •The prior is a curve over θ\thetaθ.
- •The likelihood is another curve over θ\thetaθ (for the fixed observed data).
- •Multiplying them gives a curve that is large where both agree.
- •Normalization rescales that product so the area equals 1.

This “agreement by multiplication” is the heart of Bayesian updating.

## Bayesian inference vs MLE (how they relate)

MLE finds a point estimate maximizing the likelihood.

Bayesian inference produces a distribution. But you can recover point estimates from the posterior:

- •**MAP estimate** (maximum a posteriori):

θ^MAP=arg⁡max⁡θp(θ∣x)=arg⁡max⁡θp(x∣θ)p(θ).\hat\theta\_{\text{MAP}} = \arg\max\_{\theta} p(\theta\mid x) = \arg\max\_{\theta} p(x\mid\theta)p(\theta).θ^MAP​=argθmax​p(θ∣x)=argθmax​p(x∣θ)p(θ).

- •If the prior is uniform (and you accept that choice), MAP and MLE coincide.

The key difference: Bayesian inference quantifies uncertainty and naturally supports predictive distributions (integrating over θ\thetaθ).

## Core Mechanic 1: Prior, Likelihood, Posterior (and what each one \*means\*)

## Start with the data-generating story

A Bayesian model usually begins with a story:

1) Nature draws a parameter θ\thetaθ from a prior p(θ)p(\theta)p(θ).

2) Then Nature generates data xxx from p(x∣θ)p(x\mid\theta)p(x∣θ).

We only observe xxx. Bayesian inference asks: given xxx, what should we believe about θ\thetaθ?

## Prior p(θ): encoding beliefs and constraints

A prior can do several jobs:

- •Encode domain knowledge (e.g., a coin is probably not extremely biased).
- •Enforce constraints (e.g., θ∈[0,1]\theta\in[0,1]θ∈[0,1] for probabilities).
- •Regularize inference (prevent extreme estimates with small data).

### Example: probability parameter

If θ\thetaθ is a probability (like a Bernoulli success rate), then a natural prior is the Beta distribution:

θ∼Beta(α,β),p(θ)∝θα−1(1−θ)β−1.\theta \sim \text{Beta}(\alpha,\beta),\quad p(\theta) \propto \theta^{\alpha-1}(1-\theta)^{\beta-1}.θ∼Beta(α,β),p(θ)∝θα−1(1−θ)β−1.

Interpretation (informally): α−1\alpha-1α−1 looks like prior “successes,” β−1\beta-1β−1 like prior “failures.”

## Likelihood p(x|θ): a function of θ when x is fixed

This is a common conceptual speed bump.

- •As a probability model, p(x∣θ)p(x\mid\theta)p(x∣θ) is a distribution over possible data xxx given θ\thetaθ.
- •As a likelihood, L(θ)=p(x∣θ)L(\theta)=p(x\mid\theta)L(θ)=p(x∣θ) is a function of θ\thetaθ for the observed xxx.

**Important:** likelihoods are not probability distributions over θ\thetaθ, so they do not need to integrate to 1 over θ\thetaθ.

### IID datasets and likelihood factorization

If x=(x1,…,xn)x=(x\_1,\dots,x\_n)x=(x1​,…,xn​) are IID given θ\thetaθ, then:

p(x∣θ)=∏i=1np(xi∣θ).p(x\mid\theta)=\prod\_{i=1}^n p(x\_i\mid\theta).p(x∣θ)=i=1∏n​p(xi​∣θ).

That product is why data accumulates evidence quickly.

## Posterior p(θ|x): updated belief

The posterior is what you use for:

- •uncertainty intervals (credible intervals),
- •point summaries (posterior mean, MAP),
- •predictive distributions (posterior predictive),
- •decision-making (expected utility).

## Evidence p(x): the normalization constant with hidden power

The evidence is:

p(x)=∫p(x∣θ)p(θ) dθ.p(x)=\int p(x\mid\theta)p(\theta)\,d\theta.p(x)=∫p(x∣θ)p(θ)dθ.

You can think of it as:

- •The probability of seeing xxx under the whole model (prior + likelihood).
- •A measure of how well the model predicts the data *before* seeing it.

This becomes central in **model comparison** (Bayes factors), because it penalizes overly flexible models that spread probability mass too thin.

## A compact comparison table

| Object | Notation | What varies? | Must integrate/sum to 1 over θ? | Role |
| --- | --- | --- | --- | --- |
| Prior | p(θ)p(\theta)p(θ) | θ | Yes | Belief before data |
| Likelihood | p(x∣θ)p(x\mid\theta)p(x∣θ) | θ (x fixed) | No | Data support for θ |
| Posterior | p(θ∣x)p(\theta\mid x)p(θ∣x) | θ | Yes | Belief after data |
| Evidence | p(x)p(x)p(x) | — | — | Normalizer; model score |

## The “Bayesian update” as a sequence

If you observe data in chunks, Bayes updates are consistent.

Let data arrive as x(1)x^{(1)}x(1) then x(2)x^{(2)}x(2). Then:

p(θ∣x(1),x(2))∝p(x(2)∣θ) p(θ∣x(1)).p(\theta\mid x^{(1)},x^{(2)}) \propto p(x^{(2)}\mid\theta)\,p(\theta\mid x^{(1)}).p(θ∣x(1),x(2))∝p(x(2)∣θ)p(θ∣x(1)).

So yesterday’s posterior becomes today’s prior. This is not just poetic; it’s computationally useful and conceptually clean.

## Core Mechanic 2: Conjugacy, Posterior Predictive, and Credible Intervals

## Why conjugate priors matter

The posterior requires multiplying and normalizing:

p(θ∣x)∝p(x∣θ)p(θ).p(\theta\mid x) \propto p(x\mid\theta)p(\theta).p(θ∣x)∝p(x∣θ)p(θ).

Sometimes, that product lands in the same family as the prior. Then the posterior has a closed form, and updating is easy.

That pairing is called **conjugacy**.

Conjugacy is not required for Bayesian inference, but it’s the clearest way to learn the mechanics.

## Beta–Binomial: the canonical example

Assume xxx is the number of successes in nnn Bernoulli trials with success probability θ\thetaθ.

- •Likelihood:

p(x∣θ)=(nx)θx(1−θ)n−x.p(x\mid\theta)=\binom{n}{x}\theta^x(1-\theta)^{n-x}.p(x∣θ)=(xn​)θx(1−θ)n−x.

- •Prior: θ∼Beta(α,β)\theta\sim \text{Beta}(\alpha,\beta)θ∼Beta(α,β).

Compute the unnormalized posterior:

p(θ∣x)∝p(x∣θ)p(θ)∝[θx(1−θ)n−x][θα−1(1−θ)β−1]∝θx+α−1(1−θ)(n−x)+β−1.\begin{aligned}
p(\theta\mid x) &\propto p(x\mid\theta)p(\theta)\\
&\propto \left[\theta^x(1-\theta)^{n-x}\right]\left[\theta^{\alpha-1}(1-\theta)^{\beta-1}\right]\\
&\propto \theta^{x+\alpha-1}(1-\theta)^{(n-x)+\beta-1}.
\end{aligned}p(θ∣x)​∝p(x∣θ)p(θ)∝[θx(1−θ)n−x][θα−1(1−θ)β−1]∝θx+α−1(1−θ)(n−x)+β−1.​

So:

θ∣x∼Beta(α+x,β+n−x).\theta\mid x \sim \text{Beta}(\alpha+x,\beta+n-x).θ∣x∼Beta(α+x,β+n−x).

This reveals the “pseudo-count” intuition: successes add to α\alphaα, failures add to β\betaβ.

## Gamma–Poisson: rates for count data

If data are Poisson with rate λ\lambdaλ:

xi∣λ∼Poisson(λ),p(xi∣λ)=e−λλxixi!.x\_i\mid\lambda \sim \text{Poisson}(\lambda),\quad p(x\_i\mid\lambda)=e^{-\lambda}\frac{\lambda^{x\_i}}{x\_i!}.xi​∣λ∼Poisson(λ),p(xi​∣λ)=e−λxi​!λxi​​.

A conjugate prior is:

λ∼Gamma(α,β)\lambda \sim \text{Gamma}(\alpha,\beta)λ∼Gamma(α,β)

(using the rate-parameterization where density is proportional to λα−1e−βλ\lambda^{\alpha-1}e^{-\beta\lambda}λα−1e−βλ).

With nnn IID observations and S=∑ixiS=\sum\_i x\_iS=∑i​xi​:

λ∣x∼Gamma(α+S,β+n).\lambda\mid x \sim \text{Gamma}(\alpha+S,\beta+n).λ∣x∼Gamma(α+S,β+n).

Again: data adds to shape, and the number of observations adds to rate.

## Normal–Normal: unknown mean with known variance

If:

xi∣μ∼N(μ,σ2),σ2 knownx\_i\mid\mu \sim \mathcal{N}(\mu,\sigma^2),\quad \sigma^2\text{ known}xi​∣μ∼N(μ,σ2),σ2 known

and prior:

μ∼N(μ0,τ02),\mu \sim \mathcal{N}(\mu\_0,\tau\_0^2),μ∼N(μ0​,τ02​),

then the posterior is also normal. The posterior mean becomes a precision-weighted average of the prior mean and sample mean.

Define precision as inverse variance: κ=1/σ2\kappa=1/\sigma^2κ=1/σ2, κ0=1/τ02\kappa\_0=1/\tau\_0^2κ0​=1/τ02​.

Let xˉ=1n∑ixi\bar x=\frac{1}{n}\sum\_i x\_ixˉ=n1​∑i​xi​. Then:

τn2=1κ0+nκ,μn=τn2(κ0μ0+nκxˉ).\tau\_n^2 = \frac{1}{\kappa\_0+n\kappa},\quad \mu\_n = \tau\_n^2(\kappa\_0\mu\_0 + n\kappa\bar x).τn2​=κ0​+nκ1​,μn​=τn2​(κ0​μ0​+nκxˉ).

So:

μ∣x∼N(μn,τn2).\mu\mid x \sim \mathcal{N}(\mu\_n,\tau\_n^2).μ∣x∼N(μn​,τn2​).

This shows a deep Bayesian theme: **uncertainty shrinks with data**.

## Posterior predictive: predicting new data

Bayesian inference shines when you want to predict future observations xnewx\_{\text{new}}xnew​.

Instead of plugging in a single estimate of θ\thetaθ, you average over the posterior:

p(xnew∣x)=∫p(xnew∣θ)p(θ∣x) dθ.p(x\_{\text{new}}\mid x)=\int p(x\_{\text{new}}\mid\theta)p(\theta\mid x)\,d\theta.p(xnew​∣x)=∫p(xnew​∣θ)p(θ∣x)dθ.

This is called the **posterior predictive distribution**.

Intuition: if you are uncertain about θ\thetaθ, your predictions should reflect that uncertainty.

### Example intuition (no heavy math)

- •If the posterior over a coin’s bias is wide, your predictive probability of heads is not just “one number”; it’s informed by that width.
- •With little data, predictions are more conservative.

## Credible intervals (Bayesian) vs confidence intervals (frequentist)

A Bayesian **credible interval** is a probability statement about the parameter:

P(θ∈[a,b]∣x)=0.95.P(\theta\in[a,b]\mid x)=0.95.P(θ∈[a,b]∣x)=0.95.

A frequentist 95% confidence interval is a statement about repeated sampling behavior of the interval procedure, not directly about the realized parameter.

Both can be useful, but do not automatically interpret them the same way.

## A gentle note on computation

Conjugate priors are beautiful, but many real models are not conjugate.

In those cases:

- •you might approximate integrals (variational inference),
- •or sample from the posterior (MCMC),
- •or use Laplace approximations.

This node focuses on building the conceptual and algebraic foundation that those methods rely on.

## Application/Connection: Why Bayesian Inference Powers Modern ML (and what it unlocks)

## Why Bayesian inference is a cornerstone

Bayesian inference gives you three capabilities that show up everywhere in modern ML and statistics:

1) **Uncertainty-aware learning** (not just point estimates)

2) **Principled regularization** via priors

3) **Model comparison** via evidence

Let’s connect those to the nodes this unlocks.

## 1) Latent-variable generative modeling (Variational Autoencoders)

VAEs introduce latent variables **z** and parameters **θ**.

A typical generative story:

- •Sample latent **z** from a prior p(z)p(\mathbf{z})p(z).
- •Generate data **x** from pθ(x∣z)p\_\theta(\mathbf{x}\mid\mathbf{z})pθ​(x∣z).

Inference asks for the posterior over latent variables:

p(z∣x)=pθ(x∣z)p(z)pθ(x).p(\mathbf{z}\mid\mathbf{x})=\frac{p\_\theta(\mathbf{x}\mid\mathbf{z})p(\mathbf{z})}{p\_\theta(\mathbf{x})}.p(z∣x)=pθ​(x)pθ​(x∣z)p(z)​.

But pθ(x)=∫pθ(x∣z)p(z)dzp\_\theta(\mathbf{x})=\int p\_\theta(\mathbf{x}\mid\mathbf{z})p(\mathbf{z})d\mathbf{z}pθ​(x)=∫pθ​(x∣z)p(z)dz is usually intractable, so we approximate with variational inference (ELBO). That is Bayesian inference scaled up.

## 2) Sampling-based inference (MCMC)

When the posterior is complex:

p(θ∣x)∝p(x∣θ)p(θ)p(\theta\mid x) \propto p(x\mid\theta)p(\theta)p(θ∣x)∝p(x∣θ)p(θ)

MCMC constructs a Markov chain whose stationary distribution is the posterior, enabling:

- •posterior means/variances via Monte Carlo,
- •credible intervals,
- •posterior predictive checks.

The target distribution MCMC needs is exactly the Bayesian posterior (often only known up to a normalization constant, which is fine for many MCMC algorithms).

## 3) Bayesian optimization

Bayesian optimization maintains a posterior over functions or surrogate-model parameters (often Gaussian processes). Data updates a prior to a posterior, then an acquisition function uses that posterior uncertainty to pick the next point to evaluate.

The key idea is **exploration vs exploitation** driven by posterior uncertainty.

## 4) Auction theory and beliefs about private values

In auction settings, bidders and the designer reason about unknown private valuations and types. Bayesian models represent beliefs about those unknowns and update from signals or observed behavior. “Bayesian” in mechanism design often literally refers to priors over types.

## 5) Causal inference

Many causal workflows use Bayesian inference to:

- •estimate treatment effects with uncertainty,
- •combine prior knowledge with data,
- •perform hierarchical modeling (partial pooling).

Even when causal identification is a separate question, Bayesian inference is frequently the engine used once a causal estimand is defined.

## A final connection: regularization and MAP

If you’ve seen L2 regularization in regression, there is a Bayesian interpretation:

- •Gaussian prior on weights → L2 penalty in MAP.

This is a bridge between optimization-based ML and probabilistic modeling.

## Summary of what you should now be ready for

After this node, you should be comfortable with:

- •reading and writing p(θ∣x)p(\theta\mid x)p(θ∣x),
- •distinguishing prior vs likelihood,
- •computing simple conjugate updates,
- •understanding why evidence/normalization matters,
- •seeing why approximate inference methods exist.

That’s the conceptual toolkit you need before you dive into MCMC, variational inference, VAEs, Bayesian optimization, and Bayesian causal modeling.

## Worked Examples (3)

### Beta–Binomial update: learning a coin bias from data

You flip a coin n = 10 times and observe x = 7 heads. You model heads as Bernoulli(θ) with unknown θ. Prior: θ ~ Beta(α=2, β=2) (a mild prior preferring values near 0.5). Compute the posterior, posterior mean, and a simple predictive probability for the next flip being heads.

1. Write the likelihood for x heads in n flips:

   p(x∣θ)=(nx)θx(1−θ)n−x.p(x\mid\theta)=\binom{n}{x}\theta^x(1-\theta)^{n-x}.p(x∣θ)=(xn​)θx(1−θ)n−x.
2. Write the prior density up to proportionality:

   p(θ)∝θα−1(1−θ)β−1.p(\theta) \propto \theta^{\alpha-1}(1-\theta)^{\beta-1}.p(θ)∝θα−1(1−θ)β−1.
3. Compute unnormalized posterior:

   p(θ∣x)∝p(x∣θ)p(θ)∝θx(1−θ)n−x θα−1(1−θ)β−1∝θx+α−1(1−θ)(n−x)+β−1.\begin{aligned}
   p(\theta\mid x) &\propto p(x\mid\theta)p(\theta)\\
   &\propto \theta^x(1-\theta)^{n-x}\,\theta^{\alpha-1}(1-\theta)^{\beta-1}\\
   &\propto \theta^{x+\alpha-1}(1-\theta)^{(n-x)+\beta-1}.
   \end{aligned}p(θ∣x)​∝p(x∣θ)p(θ)∝θx(1−θ)n−xθα−1(1−θ)β−1∝θx+α−1(1−θ)(n−x)+β−1.​
4. Identify the Beta form:

   Posterior is

   θ∣x∼Beta(α+x,β+n−x)=Beta(2+7,2+3)=Beta(9,5).\theta\mid x \sim \text{Beta}(\alpha+x,\beta+n-x)=\text{Beta}(2+7,2+3)=\text{Beta}(9,5).θ∣x∼Beta(α+x,β+n−x)=Beta(2+7,2+3)=Beta(9,5).
5. Compute the posterior mean (for Beta(a,b), mean is a/(a+b)):

   E[θ∣x]=99+5=914≈0.6429.\mathbb{E}[\theta\mid x]=\frac{9}{9+5}=\frac{9}{14}\approx 0.6429.E[θ∣x]=9+59​=149​≈0.6429.
6. Compute posterior predictive probability that next flip is heads:

   P(xnew=1∣x)=∫P(xnew=1∣θ) p(θ∣x) dθ.P(x\_{\text{new}}=1\mid x)=\int P(x\_{\text{new}}=1\mid\theta)\,p(\theta\mid x)\,d\theta.P(xnew​=1∣x)=∫P(xnew​=1∣θ)p(θ∣x)dθ.

   But P(xnew=1∣θ)=θP(x\_{\text{new}}=1\mid\theta)=\thetaP(xnew​=1∣θ)=θ, so

   P(xnew=1∣x)=E[θ∣x]=914.P(x\_{\text{new}}=1\mid x)=\mathbb{E}[\theta\mid x]=\frac{9}{14}.P(xnew​=1∣x)=E[θ∣x]=149​.

**Insight:** The posterior update is just “add successes and failures” to the prior’s pseudo-counts. The predictive probability automatically accounts for uncertainty because it averages over θ instead of plugging in a single estimate.

### Gamma–Poisson update: inferring an event rate from counts

A website sees counts of signups per day. Assume x₁,…,xₙ are IID Poisson(λ). You observe n = 5 days with counts: 3, 1, 4, 0, 2 (sum S = 10). Prior: λ ~ Gamma(α=2, β=1) using the rate parameterization (density ∝ λ^{α-1} e^{-βλ}). Compute the posterior and posterior mean.

1. Write the likelihood for IID Poisson:

   p(x∣λ)=∏i=1ne−λλxixi!.p(x\mid\lambda)=\prod\_{i=1}^n e^{-\lambda}\frac{\lambda^{x\_i}}{x\_i!}.p(x∣λ)=i=1∏n​e−λxi​!λxi​​.
2. Separate terms that depend on λ:

   p(x∣λ)=(∏i=1n1xi!)e−nλλ∑ixi=C e−nλλS\begin{aligned}
   p(x\mid\lambda)
   &= \left(\prod\_{i=1}^n \frac{1}{x\_i!}\right) e^{-n\lambda} \lambda^{\sum\_i x\_i}\\
   &= C\, e^{-n\lambda}\lambda^{S}
   \end{aligned}p(x∣λ)​=(i=1∏n​xi​!1​)e−nλλ∑i​xi​=Ce−nλλS​

   where C does not depend on λ.
3. Write the prior up to proportionality:

   p(λ)∝λα−1e−βλ.p(\lambda) \propto \lambda^{\alpha-1}e^{-\beta\lambda}.p(λ)∝λα−1e−βλ.
4. Compute the unnormalized posterior:

   p(λ∣x)∝p(x∣λ)p(λ)∝(e−nλλS)(λα−1e−βλ)∝λ(α+S)−1e−(β+n)λ.\begin{aligned}
   p(\lambda\mid x) &\propto p(x\mid\lambda)p(\lambda)\\
   &\propto \left(e^{-n\lambda}\lambda^{S}\right)\left(\lambda^{\alpha-1}e^{-\beta\lambda}\right)\\
   &\propto \lambda^{(\alpha+S)-1} e^{-(\beta+n)\lambda}.
   \end{aligned}p(λ∣x)​∝p(x∣λ)p(λ)∝(e−nλλS)(λα−1e−βλ)∝λ(α+S)−1e−(β+n)λ.​
5. Recognize the Gamma form:

   λ∣x∼Gamma(α+S,β+n)=Gamma(2+10,1+5)=Gamma(12,6).\lambda\mid x \sim \text{Gamma}(\alpha+S,\beta+n)=\text{Gamma}(2+10,1+5)=\text{Gamma}(12,6).λ∣x∼Gamma(α+S,β+n)=Gamma(2+10,1+5)=Gamma(12,6).
6. Compute the posterior mean (for Gamma(shape α, rate β), mean is α/β):

   E[λ∣x]=126=2.\mathbb{E}[\lambda\mid x]=\frac{12}{6}=2.E[λ∣x]=612​=2.

**Insight:** The posterior mean blends prior information with data: the data contributes S counts and n exposure units (days). The update is algebraic because the Gamma prior is conjugate to the Poisson likelihood.

### Normal–Normal update: estimating a mean with known variance (showing shrinkage)

Assume x₁,…,xₙ are IID Normal(μ, σ²) with known σ² = 4. You observe n = 4 data points: 2, 1, 3, 2 so the sample mean is x̄ = 2. Prior: μ ~ Normal(μ₀ = 0, τ₀² = 1). Compute the posterior mean and variance.

1. Compute precisions (inverse variances):

   κ=1/σ2=1/4=0.25,κ0=1/τ02=1.\kappa=1/\sigma^2=1/4=0.25,\quad \kappa\_0=1/\tau\_0^2=1.κ=1/σ2=1/4=0.25,κ0​=1/τ02​=1.
2. Use the conjugate update formulas:

   τn2=1κ0+nκ,μn=τn2(κ0μ0+nκxˉ).\tau\_n^2 = \frac{1}{\kappa\_0+n\kappa},\quad \mu\_n = \tau\_n^2(\kappa\_0\mu\_0 + n\kappa\bar x).τn2​=κ0​+nκ1​,μn​=τn2​(κ0​μ0​+nκxˉ).
3. Plug in numbers for posterior variance:

   τn2=11+4⋅0.25=11+1=12=0.5.\tau\_n^2 = \frac{1}{1 + 4\cdot 0.25} = \frac{1}{1+1} = \frac{1}{2} = 0.5.τn2​=1+4⋅0.251​=1+11​=21​=0.5.
4. Plug in numbers for posterior mean:

   μn=0.5(1⋅0+4⋅0.25⋅2)=0.5(0+1⋅2)=1.\begin{aligned}
   \mu\_n &= 0.5\left(1\cdot 0 + 4\cdot 0.25 \cdot 2\right)\\
   &= 0.5\left(0 + 1\cdot 2\right)=1.
   \end{aligned}μn​​=0.5(1⋅0+4⋅0.25⋅2)=0.5(0+1⋅2)=1.​
5. State posterior:

   μ∣x∼N(1,0.5).\mu\mid x \sim \mathcal{N}(1, 0.5).μ∣x∼N(1,0.5).

**Insight:** Even though the sample mean is 2, the posterior mean is 1 because the prior mean 0 pulls it back (shrinkage). With more data (larger n) or lower noise (smaller σ²), the data would dominate and shrinkage would weaken.

## Key Takeaways

- ✓

  Bayesian inference treats unknown parameters θ as random variables and updates beliefs with data via p(θ∣x)∝p(x∣θ)p(θ)p(\theta\mid x) \propto p(x\mid\theta)p(\theta)p(θ∣x)∝p(x∣θ)p(θ).
- ✓

  The likelihood p(x∣θ)p(x\mid\theta)p(x∣θ) is a function of θ for fixed observed x; it is not a probability distribution over θ.
- ✓

  The evidence p(x)=∫p(x∣θ)p(θ)dθp(x)=\int p(x\mid\theta)p(\theta)d\thetap(x)=∫p(x∣θ)p(θ)dθ normalizes the posterior and enables model comparison (marginal likelihood).
- ✓

  Conjugate priors (Beta–Binomial, Gamma–Poisson, Normal–Normal) yield closed-form posteriors and build intuition for updating.
- ✓

  Posterior predictive distributions average over parameter uncertainty: p(xnew∣x)=∫p(xnew∣θ)p(θ∣x)dθp(x\_{\text{new}}\mid x)=\int p(x\_{\text{new}}\mid\theta)p(\theta\mid x)d\thetap(xnew​∣x)=∫p(xnew​∣θ)p(θ∣x)dθ.
- ✓

  MAP estimation is Bayesian point estimation: θ^MAP=arg⁡max⁡p(θ∣x)\hat\theta\_{\text{MAP}}=\arg\max p(\theta\mid x)θ^MAP​=argmaxp(θ∣x); with a uniform prior it matches MLE (but “uniform” is parameterization-dependent).
- ✓

  ‘Flat/uninformative’ priors are not automatically objective; they depend on how you parameterize the problem and can encode assumptions implicitly.

## Common Mistakes

- ✗

  Treating the likelihood as a distribution over θ and trying to interpret it as “probability θ is true.” Likelihood is not normalized over θ.
- ✗

  Forgetting the evidence/normalization and thinking p(θ∣x)=p(x∣θ)p(θ)p(\theta\mid x)=p(x\mid\theta)p(\theta)p(θ∣x)=p(x∣θ)p(θ) exactly (missing the constant that makes it integrate to 1).
- ✗

  Assuming a uniform prior is always non-informative; uniformity changes under reparameterization, so ‘uninformative’ requires care.
- ✗

  Mixing up posterior credible intervals with frequentist confidence intervals and interpreting them identically.

## Practice

easy

Beta–Binomial practice: You observe n = 20 trials with x = 2 successes. Prior is Beta(α=1, β=1). (a) What is the posterior? (b) What is the posterior mean? (c) What is the posterior predictive probability of success on the next trial?

**Hint:** Use Beta conjugacy: posterior parameters are (α+x, β+n−x). Predictive success probability is the posterior mean.

Show solution

(a) Posterior: Beta(α+x, β+n−x) = Beta(1+2, 1+18) = Beta(3, 19).

(b) Posterior mean = 3/(3+19) = 3/22 ≈ 0.13636.

(c) Posterior predictive P(next=1|data) = E[θ|data] = 3/22.

medium

Gamma–Poisson practice: Counts per hour are modeled as Poisson(λ). You observe 8 hours with total count S = 24. Prior is Gamma(α=3, β=2) (rate parameterization). Find the posterior distribution and posterior mean.

**Hint:** For Poisson with Gamma prior: posterior is Gamma(α+S, β+n). Mean is (α+S)/(β+n).

Show solution

Posterior: Gamma(α+S, β+n) = Gamma(3+24, 2+8) = Gamma(27, 10).

Posterior mean = 27/10 = 2.7.

hard

MAP vs MLE and priors: Let x₁,…,xₙ ~ Normal(μ, σ²) with known σ². (a) Write the MLE for μ. (b) If the prior is μ ~ Normal(μ₀, τ₀²), derive the MAP estimate for μ by maximizing the posterior (show the algebraic completion of squares or derivative steps).

**Hint:** The posterior is proportional to likelihood × prior. Taking logs turns products into sums. Differentiate w.r.t. μ and set to 0.

Show solution

(a) MLE: maximize ∏ᵢ N(xᵢ|μ,σ²). The maximizer is the sample mean:

μ^MLE=xˉ.\hat\mu\_{\text{MLE}}=\bar x.μ^​MLE​=xˉ.

(b) Posterior (up to proportionality):

p(μ∣x)∝[∏i=1nexp⁡(−(xi−μ)22σ2)]exp⁡(−(μ−μ0)22τ02).p(\mu\mid x) \propto \left[\prod\_{i=1}^n \exp\left(-\frac{(x\_i-\mu)^2}{2\sigma^2}\right)\right]\exp\left(-\frac{(\mu-\mu\_0)^2}{2\tau\_0^2}\right).p(μ∣x)∝[i=1∏n​exp(−2σ2(xi​−μ)2​)]exp(−2τ02​(μ−μ0​)2​).

Take logs (dropping constants not depending on μ):

ℓ(μ)=−12σ2∑i=1n(xi−μ)2−12τ02(μ−μ0)2.\ell(\mu)= -\frac{1}{2\sigma^2}\sum\_{i=1}^n (x\_i-\mu)^2 -\frac{1}{2\tau\_0^2}(\mu-\mu\_0)^2.ℓ(μ)=−2σ21​i=1∑n​(xi​−μ)2−2τ02​1​(μ−μ0​)2.

Differentiate:

dℓdμ=−12σ2⋅2∑i=1n(μ−xi)−12τ02⋅2(μ−μ0).\frac{d\ell}{d\mu}= -\frac{1}{2\sigma^2}\cdot 2\sum\_{i=1}^n (\mu-x\_i) -\frac{1}{2\tau\_0^2}\cdot 2(\mu-\mu\_0).dμdℓ​=−2σ21​⋅2i=1∑n​(μ−xi​)−2τ02​1​⋅2(μ−μ0​).

So:

dℓdμ=−1σ2(nμ−∑i=1nxi)−1τ02(μ−μ0).\frac{d\ell}{d\mu}= -\frac{1}{\sigma^2}\left(n\mu-\sum\_{i=1}^n x\_i\right) -\frac{1}{\tau\_0^2}(\mu-\mu\_0).dμdℓ​=−σ21​(nμ−i=1∑n​xi​)−τ02​1​(μ−μ0​).

Set to 0:

−1σ2(nμ−nxˉ)−1τ02(μ−μ0)=0.-\frac{1}{\sigma^2}(n\mu-n\bar x) -\frac{1}{\tau\_0^2}(\mu-\mu\_0)=0.−σ21​(nμ−nxˉ)−τ02​1​(μ−μ0​)=0.

Multiply by −1 and rearrange:

nσ2(μ−xˉ)+1τ02(μ−μ0)=0\frac{n}{\sigma^2}(\mu-\bar x) + \frac{1}{\tau\_0^2}(\mu-\mu\_0)=0σ2n​(μ−xˉ)+τ02​1​(μ−μ0​)=0

(nσ2+1τ02)μ=nσ2xˉ+1τ02μ0.\left(\frac{n}{\sigma^2}+\frac{1}{\tau\_0^2}\right)\mu = \frac{n}{\sigma^2}\bar x + \frac{1}{\tau\_0^2}\mu\_0.(σ2n​+τ02​1​)μ=σ2n​xˉ+τ02​1​μ0​.

Thus the MAP (which equals the posterior mean in this conjugate case) is:

μ^MAP=nσ2xˉ+1τ02μ0nσ2+1τ02.\hat\mu\_{\text{MAP}}=\frac{\frac{n}{\sigma^2}\bar x + \frac{1}{\tau\_0^2}\mu\_0}{\frac{n}{\sigma^2}+\frac{1}{\tau\_0^2}}.μ^​MAP​=σ2n​+τ02​1​σ2n​xˉ+τ02​1​μ0​​.

## Connections

- •Next: [MCMC](/tech-tree/mcmc/) — compute posteriors when integrals are intractable.
- •Next: [Variational Autoencoders](/tech-tree/vae/) — approximate p(z∣x)p(\mathbf{z}\mid\mathbf{x})p(z∣x) with variational inference (ELBO).
- •Next: [Bayesian Optimization](/tech-tree/bayesian-optimization/) — use posterior uncertainty to guide expensive searches.
- •Related: [Causal Inference](/tech-tree/causal-inference/) — Bayesian estimation of causal effects with uncertainty.
- •Related: [Auction Theory](/tech-tree/auction-theory/) — priors over bidder types/values and belief updates.

Quality: B (4.0/5)

[← back to tree](/tech-tree/)[browse all →](/tech-tree/inventory/)
