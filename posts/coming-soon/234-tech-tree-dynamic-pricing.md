---
title: Dynamic Pricing
description: Real-time price optimization under demand uncertainty. Thompson sampling for prices, contextual bandits. Learn-and-earn exploration-exploitation tradeoff.
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
permalink: /tech-tree/dynamic-pricing/
---

[←Back to Tech Tree](/tech-tree/)

[inventory](/tech-tree/inventory/)[coverage](/tech-tree/coverage/)

# Dynamic Pricing

Applied EconomicsDifficulty: ★★★★★Depth: 13Unlocks: 0

Real-time price optimization under demand uncertainty. Thompson sampling for prices, contextual bandits. Learn-and-earn exploration-exploitation tradeoff.

## Prerequisites (3)

[Bayesian Forecasting? atoms](/tech-tree/bayesian-forecasting/)[Profit Maximization? atoms](/tech-tree/profit-maximization/)[Bayesian Decision Theory? atoms](/tech-tree/bayesian-decision-theory/)

Advanced Learning Details

### Graph Position

235

Depth Cost

0

Fan-Out (ROI)

0

Bottleneck Score

13

Chain Length

Optimal pricing in platforms and retail isn't just about fitting a demand curve — it's about learning demand while you sell. Dynamic pricing with Thompson sampling gives you a principled, Bayesian way to trade off learning and earning in real time.

TL;DR:

Dynamic pricing with Thompson sampling frames price selection as a Bayesian (contextual) bandit problem: maintain a posterior over demand parameters, sample a plausible demand model, choose the profit-maximizing price under that sample, update posterior with observed sales — thereby learning while earning with quantifiable regret.

## What Is Dynamic Pricing (under demand uncertainty)?

Definition and motivation

Dynamic pricing under demand uncertainty is the sequential decision problem where, at each decision epoch t = 1,2,...,T, a seller chooses a price p\_t ∈ P (continuous or discrete) for a product facing random demand D\_t(p\_t, x\_t; θ*) that depends on price, observed context x\_t (features), and unknown demand parameters θ*. The seller observes a sales outcome y\_t (e.g., quantity sold or binary purchase) and receives reward (profit) r\_t = π(p\_t, y\_t) (e.g., revenue minus costs). The goal is to maximize cumulative expected reward E[Σ\_{t=1}^T r\_t] or equivalently minimize regret relative to an oracle pricing policy that knows θ\*.

Why this matters

In practice, firms cannot wait to identify a demand model perfectly before setting prices: every price both earns revenue and provides information. This is the quintessential learn-and-earn exploration-exploitation tradeoff. In online marketplaces, ride-hailing, and airline revenue management, prices must be updated rapidly with streaming data and contexts (time-of-day, user features). The framework we develop combines Bayesian Forecasting (we reference that prerequisite below), Profit Maximization, and Bayesian Decision Theory to make coherent, optimal-seeming online pricing decisions.

Core intuition

There are two ingredients: (1) a model P(y | p, x, θ) for demand given price and context; (2) a Bayesian posterior π\_t(θ) summarizing belief about θ at time t. Thompson sampling (TS) — a Bayesian algorithm from the multi-armed bandit literature — converts beliefs into actions by: sample θ̃\_t ∼ π\_t(θ), then choose p\_t = argmax\_{p ∈ P} E[y | p, x\_t, θ̃\_t]·p (or the profit objective). TS thus implements posterior-randomized decision rules that approximate the Bayes-optimal policy while being computationally tractable.

Formalization (toy deterministic-demand example)

Suppose a linear demand curve Q(p) = a − b p + ε with ε ∼ N(0, σ^2). The seller's instantaneous expected revenue at price p, given parameters θ = (a,b), is

R(p;θ)=p⋅E[Q(p)]=p(a−bp).R(p;θ)=p⋅E[Q(p)]=p(a-bp).R(p;θ)=p⋅E[Q(p)]=p(a−bp).

The price maximizing revenue for known θ solves the first-order condition (Profit Maximization prerequisite):

ddpR(p;θ)=a−2bp=0⇒p∗(θ)=a2b.\frac{d}{dp}R(p;θ)=a-2bp=0 \Rightarrow p^\*(θ)=\frac{a}{2b}.dpd​R(p;θ)=a−2bp=0⇒p∗(θ)=2ba​.

If a and b are unknown, TS samples θ̃ from the posterior and then uses p^*(θ̃). For example, if posterior mean is (â,b̂)=(10,1) then p^*=10/2=5 and expected revenue is R(5) = 5(10 − 1·5) = 25. This concrete numeric link between posterior sample and pricing is the heart of TS.

Relation to prerequisites

- •In Bayesian Forecasting, we learned to compute posterior predictive distributions and structural model inference; TS uses the posterior over θ and the posterior predictive for demand to choose actions.
- •In Profit Maximization, we used first-order conditions to derive optimal price given parameters; TS plugs in a sampled θ to perform that maximization.
- •In Bayesian Decision Theory, we learned Bayes risk and posterior expected loss minimization; TS is a heuristic that samples from the posterior and chooses a greedy action, approximating posterior sampling of the Bayes-optimal policy while inducing exploration.

## Core Mechanic 1: Thompson Sampling for Prices (Static/Context-free)

Algorithmic skeleton

For a context-free (or time-invariant) parametric demand model P(y | p, θ), Thompson sampling proceeds:

1. 1)Initialize prior π\_0(θ).
2. 2)For each t = 1,...,T:

a. Sample θ̃\_t ∼ π\_{t-1}(θ).

b. Compute p\_t = argmax\_{p ∈ P} E[r | p, θ̃\_t] (profit-maximizing price under θ̃\_t).

c. Offer p\_t, observe y\_t (e.g., units sold), and reward r\_t.

d. Update posterior π\_t(θ) ∝ P(y\_t | p\_t, θ) π\_{t-1}(θ).

This converts posterior uncertainty into randomized pricing that automatically explores: when posterior uncertainty is large, samples vary, so prices vary; when posterior concentrates, prices stabilize.

Worked mini-example: linear-Gaussian demand with conjugate prior

Model: observed (possibly fractional) sales y\_t = a − b p\_t + ε\_t, ε\_t ∼ N(0, σ^2). Unknown parameters θ = (a,b) ∈ R^2. Take Gaussian prior θ ∼ N(μ\_0, Σ\_0). The likelihood for a single observation is Gaussian, so posterior is Gaussian. Stack data: define X\_t as t×2 matrix where each row is [1, −p\_i] for i ≤ t (note sign convention to keep coefficients positive), and y\_{1:t} the observed sales.

Posterior update (standard Bayesian linear regression):

Σt−1=Σ0−1+1σ2XtTXt,μt=Σt(Σ0−1μ0+1σ2XtTy1:t).Σ\_t^{-1} = Σ\_0^{-1} + \frac{1}{σ^2} X\_t^T X\_t, \qquad μ\_t = Σ\_t\left(Σ\_0^{-1} μ\_0 + \frac{1}{σ^2} X\_t^T y\_{1:t}\right).Σt−1​=Σ0−1​+σ21​XtT​Xt​,μt​=Σt​(Σ0−1​μ0​+σ21​XtT​y1:t​).

Numeric illustration: suppose σ^2=1, prior μ\_0=(8,0.8), Σ\_0=diag(4,0.25) (large uncertainty in intercept, modest in slope). After observing one datapoint at p\_1=5 with y\_1=6 (sold 6 units):

X\_1=[1, −5], y\_1=6.

Compute

Σ1−1=(1/4001/0.25)+11[1,−5]T[1,−5]=(0.25+10+(−5)0+(−5)4+25)=(1.25−5−529).Σ\_1^{-1}=\begin{pmatrix}1/4 & 0\\0 & 1/0.25\end{pmatrix} + \frac{1}{1}[1, -5]^T[1, -5] = \begin{pmatrix}0.25+1 & 0+(-5)\\0+(-5) & 4+25\end{pmatrix} = \begin{pmatrix}1.25 & -5\\-5 & 29\end{pmatrix}.Σ1−1​=(1/40​01/0.25​)+11​[1,−5]T[1,−5]=(0.25+10+(−5)​0+(−5)4+25​)=(1.25−5​−529​).

Then invert to find Σ\_1 (compute numerically), and μ\_1 using the formula. One can then sample θ̃\_2 ∼ N(μ\_1, Σ\_1) and compute p\_2 = ã/(2 b̃) where θ̃\_2=(ã,b̃). If ã=9.2 and b̃=1.05 (a possible draw), p\_2≈9.2/(2·1.05)≈4.38.

Why conjugacy matters

Conjugate Gaussian updates are algebraically simple and fast; they let us sample θ̃\_t instantly and compute closed-form optimal prices p^\*(θ̃\_t). This is important in real-time systems. In nonconjugate models (e.g., logistic purchase probability), one can use approximate posterior sampling (MCMC, Laplace, variational) or embedding in particle filters.

Regret intuition and theoretical guarantees (sketch)

Define Bayes regret after T steps as BR(T)=E[Σ\_{t=1}^T (r^*(x\_t,θ*) − r(p\_t, y\_t))] where expectation is over θ\* drawn from the prior and all randomness. For parametric linear-Gaussian models under boundedness assumptions, Thompson sampling achieves regret scaling like O(d√T log T) for d-dimensional parameter θ (results from linear bandit literature). In the pricing context, continuous action spaces and possibly non-linear revenue curves complicate bounds; one common approach is to show that the revenue function is Lipschitz in θ and p and then couple posterior concentration with discretization of P to get regret bounds. These theoretical tools rely on Bayesian Forecasting-type concentration results for posteriors and on Profit Maximization derivatives to bound loss from a sampled parameter.

## Core Mechanic 2: Contextual Bandits and Practical Extensions

Contextual extension: models where demand depends on context x\_t

Often demand varies with observable covariates x\_t (user features, time of day, inventory state). The demand model is P(y | p, x, θ). In a linear contextual pricing model you might write

yt=xtTβ+γpt+εty\_t = x\_t^T β + γ p\_t + ε\_tyt​=xtT​β+γpt​+εt​

or equivalently include interactions with price:

yt=xtTβ+ptxtTφ+εt,y\_t = x\_t^T β + p\_t x\_t^T φ + ε\_t,yt​=xtT​β+pt​xtT​φ+εt​,

where θ = (β, φ) and the revenue objective is R(p; θ, x\_t) = p⋅E[y\_t | p, x\_t, θ]. The action set of prices can be continuous; the maximization step for sampled θ̃ is a small optimization problem possibly convex (or closed-form for simple models).

Thompson sampling in contextual bandits

TS generalizes straightforwardly: sample θ̃\_t ∼ π\_{t-1}(θ), then pick p\_t = argmax\_{p∈P} E[r | p, x\_t, θ̃\_t]. Posterior updates incorporate the context as design matrix rows depend on x\_t and p\_t. The linear-Gaussian conjugate update becomes:

Let φ(p,x) be the feature vector (e.g., φ = [x; p x]) so y\_t = φ(p\_t,x\_t)^T θ + ε\_t. Stack Φ\_t rows φ(p\_i,x\_i) for i≤t. Then

Σt−1=Σ0−1+1σ2ΦtTΦt,μt=Σt(Σ0−1μ0+1σ2ΦtTy1:t).Σ\_t^{-1} = Σ\_0^{-1} + \frac{1}{σ^2} Φ\_t^T Φ\_t, \qquad μ\_t = Σ\_t\left(Σ\_0^{-1} μ\_0 + \frac{1}{σ^2} Φ\_t^T y\_{1:t}\right).Σt−1​=Σ0−1​+σ21​ΦtT​Φt​,μt​=Σt​(Σ0−1​μ0​+σ21​ΦtT​y1:t​).

Numeric example (2-dim context)

Let x\_t ∈ R be a single context (e.g., time-of-day indicator), model y = β\_0 + β\_1 x + φ p + ε (no interaction for simplicity). Then φ(p,x)=[1, x, p]^T and θ=(β\_0, β\_1, φ). Suppose Σ\_0=I·9, μ\_0=0, σ^2=4. At t=1, x\_1=1, p\_1=5, observe y\_1=7. Then Φ\_1=[1,1,5], compute Σ\_1^{-1}=I/9 + (1/4) Φ\_1^T Φ\_1 = diag(1/9,1/9,1/9) + (1/4)[1;1;5][1,1,5]. Numeric operations produce Σ\_1 and μ\_1, enabling sampling and pricing.

Practical issues and extensions

1) Discrete vs continuous price sets. If P is continuous but the revenue maximization is non-convex, one practical solution is to optimize p by gradient methods on the sampled revenue function R(p; θ̃\_t, x\_t) or to discretize P finely and treat it as a multi-armed bandit. Example: discretize P into K=100 grid points and run TS over K arms where arm k has parametric likelihood induced by offering that price. Discretization creates approximation error bounded by the Lipschitz constant of revenue.

2) Binary purchase models and generalized linear models (GLMs). If customers either purchase or not, model the purchase probability as logistic: Pr(y=1 | p,x,θ) = σ(φ(p,x)^T θ). Conjugacy is lost; approximate posteriors via Laplace approximation (Gaussian around MAP) or variational inference. TS then samples θ̃ from the approximate posterior. Numeric example: φ=[1, p], θ prior N(0,10I), observe a purchase at p=3, update via Laplace.

3) Inventory and constrained pricing (connection to Profit Maximization). When inventory I\_t is limited, the decision must account for remaining stock: the reward is revenue but actions affect future feasibility. One can embed TS into approximate dynamic programming: sample θ̃\_t, compute approximate dynamic program (e.g., myopic price that accounts for remaining inventory through a shadow value λ estimated by dual ascent), and act greedily under θ̃\_t. This is a practical and Bayesian-aware heuristic for learn-and-earn when capacity constraints are active.

4) Heteroskedastic noise and nonstationarity. In many e-commerce settings the noise variance or θ itself drifts. Two practical remedies: (a) use discounting/forgetting in the posterior (e.g., treat prior update with weight α<1) or (b) structure θ evolution with a state-space model and apply particle or Kalman filters (this directly leverages Bayesian Forecasting skills). Numeric example: a random-walk prior θ\_{t+1}=θ\_t+η\_t with η\_t∼N(0,Σ\_η) inserted into the conjugate update yields a Kalman filter.

Theoretical note: regret scaling and model misspecification

When the model is correctly specified, TS for linear contextual bandits has regret bounds O(d√T log T). However, pricing models are often misspecified (wrong functional form, unobserved confounders). In misspecified settings, Bayesian posteriors can concentrate on pseudo-true parameters; TS may then concentrate on suboptimal prices. Robust approaches include: robust priors, model averaging (also in Bayesian Forecasting), and explicit exploration bonuses (upper-confidence bound methods) calibrated to misspecification magnitude.

## Applications and Connections: From Theory to Production

Real-world use cases

1) Online retail and e-commerce: personalized prices (coupons, dynamic discounts) where x\_t contains user features, device, and historical elasticity signals. A pipeline uses a Bayesian contextual demand model updated daily with streaming logs and Thompson sampling to select A/B test-like prices at the user session level.

2) Ride-hailing and surge pricing: supply-demand imbalance interacts with price to control demand and reallocate supply. Context includes location and current fleet state; demand is stochastic and partially observed. TS can be applied when demand response is parametrically modeled, but constraints from policy (caps) and fairness require additional constraints in the optimization step.

3) Revenue management (airlines, hotels): fare classes and inventory controls combined with TS-type learning for unobserved price sensitivities; here the state includes remaining seats (connects to the inventory extension above).

Industry implementation pattern

- •Model selection and priors: practitioners often use hierarchical priors across SKUs (Bayesian Forecasting and Bayesian model averaging) to borrow strength and stabilize early decisions. For example, a hierarchical normal prior for intercepts a\_i ∼ N(μ\_a, τ\_a^2) across products i, updated with pooled data.

- •Computational considerations: closed-form conjugate models are favored in real-time systems. For nonconjugate models, use fast Laplace approximations or sequential Monte Carlo with a moderate number of particles (e.g., 100–1000) to represent π\_t(θ).

- •Business constraints: include minimum advertised prices, competitor reactions, regulatory fairness constraints. These constraints alter the argmax step: instead of pure revenue maximization, solve a constrained optimization incorporating fairness/legality.

Connections to research and further reading

- •Theoretical papers on Thompson sampling include Agrawal and Goyal (2013) for multi-armed bandits and Russo and Van Roy for information-theoretic analyses. For linear contextual bandits and regret bounds see Abbasi-Yadkori et al. (2011) and Dani et al. (2008). These results underpin regret guarantees referenced earlier.

- •For dynamic pricing with inventory and learning, see Besbes and Zeevi (2009, 2015) for nonstochastic and stochastic demand settings, and Ferreira et al. (2016) for structural approaches.

What this enables

Mastering TS-based dynamic pricing enables data-driven, principled pricing in settings where demand is unknown and decisions must be sequential. It connects Bayesian Forecasting (posterior computation and model selection), Profit Maximization (analytic pricing rules given parameters), and Bayesian Decision Theory (posterior-based decisions to manage exploration-exploitation). Practically, it opens pathways to personalized pricing, real-time experimentation at scale, and integration with inventory and supply-side constraints.

## Worked Examples (3)

### Linear demand — single-step Thompson pricing

Model: y = a - b p + ε, ε∼N(0,1). Prior: a∼N(10,4), b∼N(1,0.25), independent. One observation at p=4 yields y=7. Compute posterior, draw θ̃, and compute the priced p next period.

1. Write design row for p=4: X=[1, -4]. Observed y=7.
2. Compute prior precisions: Σ\_0^{-1}=diag(1/4,1/0.25)=diag(0.25,4).
3. Compute Σ\_1^{-1}=Σ\_0^{-1}+X^TX = [[0.25+1, 0+(-4)], [0+(-4), 4+16]] = [[1.25, -4], [-4,20]].
4. Invert Σ\_1^{-1} to get Σ\_1. The determinant is 1.25\*20 - (-4)^2 = 25 - 16 = 9. So Σ\_1 = (1/9) [[20, 4], [4, 1.25]]. Numerically Σ\_1 ≈ [[2.222,0.444],[0.444,0.139]].
5. Compute μ\_1 = Σ\_1(Σ\_0^{-1}μ\_0 + X^T y) with μ\_0=[10,1]^T. First compute Σ\_0^{-1}μ\_0 = [0.25*10, 4*1] = [2.5, 4]. X^T y = [1*7, -4*7] = [7, -28]. Sum = [9.5, -24]. Multiply μ\_1 = Σ\_1  *[9.5, -24] ≈ [2.222*9.5 + 0.444*(-24), 0.444*9.5 + 0.139\*(-24)] ≈ [21.11 -10.66, 4.22 -3.33] ≈ [10.45,0.89].
6. Sample θ̃ from N(μ\_1,Σ\_1); for a concrete sample take ã=10.0, b̃=0.95. Compute myopic revenue-maximizing price p^\* = ã/(2 b̃) ≈ 10/(1.9) ≈ 5.263.

**Insight:** This example demonstrates how a single observation updates beliefs about intercept and slope, how conjugate algebra gives a posterior, and how a sampled parameter yields a practical price decision using the Profit Maximization first-order condition.

### Contextual pricing with one feature

Model: y\_t = β\_0 + β\_1 x\_t + φ p\_t + ε\_t, ε∼N(0,4). Prior θ∼N(0,9I\_3). At t=1, x\_1=2, p\_1=3, y\_1=5. Compute posterior and the price for t=2 for context x\_2=1 by sampling θ̃ and solving for optimal p.

1. Feature vector φ(p,x)=[1, x, p] so φ\_1=[1,2,3].
2. Compute Σ\_0^{-1} = (1/9) I\_3 ≈ diag(0.1111). The data precision term is (1/σ^2) φ\_1^T φ\_1 = (1/4)[1;2;3][1,2,3].
3. Compute Σ\_1^{-1} = diag(0.1111)\*3 + (1/4)[[1,2,3]^T[1,2,3]] (numerically sum elementwise). Concretely, Σ\_1^{-1} = [[0.1111+0.25, 0+0.5, 0+0.75],[0+0.5,0.1111+1,0+1.5],[0+0.75,0+1.5,0.1111+2.25]] = [[0.3611,0.5,0.75],[0.5,1.1111,1.5],[0.75,1.5,2.3611]].
4. Invert Σ\_1^{-1} numerically to get Σ\_1 (compute via linear algebra; suppose Σ\_1 ≈ M).
5. Compute μ\_1 = Σ\_1(Σ\_0^{-1}μ\_0 + (1/4) φ\_1^T y\_1), with μ\_0=0 and (1/4) φ\_1^T y\_1 = (1/4)[1;2;3]*5 = [1.25,2.5,3.75]. Multiply to get μ\_1 (numerical). Sample θ̃ (e.g., θ̃=[1.1,0.4,-0.8]). For context x\_2=1, revenue under θ̃ is R(p)=p(β\_0 + β\_1*1 + φ p) = p(c + φ p) where c=β\_0+β\_1. With given θ̃, c=1.1+0.4=1.5 and φ=-0.8, so R(p)=p(1.5 -0.8 p). Maximize: derivative 1.5 - 1.6 p = 0 ⇒ p^\*=1.5/1.6≈0.9375.
6. Offer p\_2≈0.94 and observe y\_2; continue updates.

**Insight:** This shows how context enters the design matrix, how posterior sampling yields parameter draws that depend on context history, and how the sampled model changes optimal prices across contexts even with the same prior.

### Discrete-price Thompson with binary purchases and inventory

Binary purchase model: Pr(buy | p) = σ(α - β p) with σ logistic. There are 5 discrete prices P={1,2,3,4,5}. Prior on (α,β) is independent normal N(0,4). Inventory I=3 and horizon T=5. Use Thompson sampling with discretized actions; simulate two steps with observed outcomes buy/no-buy.

1. Initialize prior: α∼N(0,4), β∼N(0,4). For a discrete action set, TS draws θ̃ and selects the price with highest immediate expected revenue p⋅Pr(buy|p,θ̃) while ensuring inventory>0.
2. Draw θ̃\_1 from the prior; suppose θ̃\_1=(1.2,0.4). Compute purchase probabilities for each price p: q(p)=σ(1.2-0.4p). Numerically: q(1)=σ(0.8)=0.69, q(2)=σ(0.4)=0.60, q(3)=σ(0.0)=0.5, q(4)=σ(-0.4)=0.40, q(5)=σ(-0.8)=0.31. Expected revenue r(p)=p\*q(p): r(1)=0.69, r(2)=1.2, r(3)=1.5, r(4)=1.6, r(5)=1.55. The maximum is at p=4 with r=1.6, so choose p\_1=4.
3. Offer p\_1=4 and observe outcome. Suppose y\_1=1 (sale). Inventory decreases to I=2. Update posterior using the likelihood Bernoulli(y|σ(α-βp)). The posterior is nonconjugate; perform a Laplace approximation: compute MAP by maximizing log prior + log likelihood. With one positive observation at p=4, the MAP will shift α upward relative to prior and β upward or downward depending on p and y. Suppose the Laplace approximation yields posterior approx N(μ\_1,Σ\_1) with μ\_1=(0.8,0.35).
4. Second round: sample θ̃\_2~N(μ\_1,Σ\_1); suppose θ̃\_2=(0.9,0.3). Compute q(p) for each p and r(p) as before. If p=3 yields highest r, choose p\_2=3. Suppose observe y\_2=0 (no sale). Update posterior with the negative observation; the posterior shifts to reflect lower intercept or higher price sensitivity.
5. Continue until inventory or horizon ends. The Thompson sampler implicitly balances exploration (trying different prices early to learn α,β) and exploitation (charging higher prices when confident).

**Insight:** This example demonstrates TS with nonconjugate Bernoulli likelihoods, discrete price grids, and inventory constraints. It shows how approximate posteriors (Laplace) are used in practice and how inventory reduces exploration when stock is scarce.

## Key Takeaways

- ✓

  Dynamic pricing under uncertainty is a sequential decision problem: prices both earn revenue and reveal demand information; Thompson sampling formalizes this as posterior sampling followed by myopic optimization.
- ✓

  In parametric linear-Gaussian models, conjugate updates allow closed-form posteriors and trivial sampling, enabling efficient real-time Thompson sampling: posterior mean + covariance update formulas are central.
- ✓

  Contextual bandits extend pricing to include observable features x\_t; treat the feature map φ(p,x) as the regression basis and apply Bayesian linear regression updates for posterior learning.
- ✓

  Practical systems often need discretization, approximations (Laplace, variational), hierarchical priors, and state-dependent extensions (inventory, time-varying parameters) — all compatible with the TS idea.
- ✓

  Theoretical regret bounds (e.g., O(d√T log T) for linear bandits) give assurance when models are well-specified; misspecification requires robustness via model averaging or explicit exploration bonuses.
- ✓

  Every pricing decision reduces to: sample plausible demand parameters (Bayesian Forecasting), compute profit-maximizing price (Profit Maximization), and act to minimize posterior expected loss (Bayesian Decision Theory).

## Common Mistakes

- ✗

  Treating Thompson sampling as purely random exploration: TS is posterior-directed; randomness reflects epistemic uncertainty. Using arbitrary epsilon-greedy exploration ignores posterior structure and is often suboptimal.
- ✗

  Ignoring model misspecification: applying TS with a wrong functional form can lead to concentration on pseudo-true parameters and persistent suboptimal pricing. Use Bayesian model averaging or test robustness.
- ✗

  Failing to account for constraints (inventory, fairness): optimizing unconstrained expected revenue under sampled θ̃ may violate real-world constraints; always include constraints in the argmax step.
- ✗

  Assuming conjugacy always holds: many realistic purchase models (logistic, Poisson arrivals with censoring) are nonconjugate and require approximate inference; naive Gaussian updates will mislead.

## Practice

easy

Easy: Linear-Gaussian single-parameter. Demand y = a - p + ε with ε∼N(0,1). Prior a∼N(8,4). At t=1 you set p\_1=3 and observe y\_1=5. Compute the posterior for a and the Thompson-sampled price at t=2 (assume posterior variance remains the computed value and sample = posterior mean).

**Hint:** Treat slope as known (=1). Posterior for a in Bayesian linear regression with known variance: variance decreases by 1, mean is weighted average of prior mean and observed y + p.

Show solution

Model implies y\_1=a - 3 + ε so the observation gives a = y\_1 + 3 - ε. Likelihood for a: N(y\_1+3,1). Prior a∼N(8,4). Posterior variance 1/(1/4 + 1/1) = 1/(0.25+1)=1/1.25=0.8. Posterior mean = 0.8*( (1/4)*8 + 1*(y\_1+3) ) =0.8*(2 + (5+3))=0.8*(10)=8. So posterior is N(8,0.8). If we sample the mean ã=8, the optimal price p^*=ã/(2\*1)=4.

medium

Medium: Contextual linear pricing. Suppose y = β\_0 + β\_1 x + φ p + ε, ε∼N(0,1). Prior θ∼N(0, I·9). You have two observations: (x=0,p=2,y=5) and (x=1,p=4,y=3). Compute Σ\_2 and μ\_2 (write formula and give numeric vector result approximately).

**Hint:** Stack feature rows φ=[1,x,p]. Use Σ\_0^{-1}=(1/9)I and σ^2=1. Compute Σ\_2^{-1}=Σ\_0^{-1}+Σ φ\_i φ\_i^T and μ\_2=Σ\_2(Σ\_0^{-1}μ\_0 + Σ φ\_i y\_i).

Show solution

Compute φ\_1=[1,0,2], φ\_2=[1,1,4]. Sum Φ^TΦ = φ\_1φ\_1^T + φ\_2φ\_2^T = [[1+1,0+1,2+4],[0+1,0+1,0+4],[2+4,2+4,4+16]] = [[2,1,6],[1,1,4],[6,4,20]]. Σ\_0^{-1}=(1/9)I≈0.1111I. Thus Σ\_2^{-1}≈[[2.1111,1,6],[1,1.1111,4],[6,4,20.1111]]. Invert numerically to get Σ\_2 (compute via linear algebra; suppose Σ\_2≈[[0.80,-0.15,-0.18],[-0.15,0.55,-0.06],[-0.18,-0.06,0.07]]). Next compute Σ\_0^{-1}μ\_0=0 and Φ^T y = φ\_1*y\_1+φ\_2*y\_2 = [1*5+1*3,0*5+1*3,2*5+4*3] = [8,3,10+12=22]. So μ\_2 = Σ\_2  *[8,3,22] ≈ numeric multiplication yields μ\_2≈[ (0.8*8) + (-0.15*3) + (-0.18*22) , ... ] ≈ [6.4 -0.45 -3.96, ...] ≈ [1.99, ...] (complete remaining entries similarly).

hard

Hard: Inventory-aware Thompson. You manage a small stock I=2 over T=3 periods. Demand per offer is Bernoulli with probability σ(α−β p). Prior α,β iid N(0,4). Devise a myopic Thompson policy that accounts for inventory by adding a shadow value λ to future sales (i.e., treat effective price p' = p + λ). Explain how to choose λ heuristically and show one simulated update step with a concrete λ=0.5 and a sampled θ̃=(1.0,0.5).

**Hint:** Shadow value λ reduces current price attractiveness if inventory should be saved. With sampled θ̃ compute expected revenue with effective price p' and choose p maximizing p·σ(α−β p) − opportunity term λ·σ(...)?

Show solution

Myopic inventory-aware TS: sample θ̃, then choose p to maximize p·Pr(buy|p,θ̃) + λ·(−Pr(buy|p,θ̃))? More consistently, view λ as marginal value of saving one unit, so the immediate objective becomes: choose p to maximize (p + λ)·Pr(buy|p,θ̃) because selling yields revenue p but costs λ in option value of losing one unit. With λ=0.5 and θ̃=(1.0,0.5), compute q(p)=σ(1.0−0.5 p). Evaluate for discrete p∈{1,2,3}: q(1)=σ(0.5)=0.62 => objective (p+λ)q=1.5*0.62=0.93. p=2: q=σ(0.0)=0.5 => (2.5)*0.5=1.25. p=3: q=σ(−0.5)=0.38 => (3.5)\*0.38=1.33. The maximum is at p=3. So offer p=3. If sale occurs, inventory→1 and posterior updates (Laplace or other). The heuristic λ can be chosen from a deterministic dynamic program under current posterior mean (compute shadow price via finite-horizon DP) or tuned to match desired service level.

## Connections

This lesson explicitly integrates three prerequisites. From Bayesian Forecasting we use posterior computation, posterior predictive distributions, and tools for state-space or time-varying parameters (e.g., Kalman/particle filters) when demand drifts. From Profit Maximization we repeatedly use first-order conditions and constrained optimization (shadow prices for inventory) to convert a sampled demand model into a concrete price. From Bayesian Decision Theory we borrow the conceptual framing: actions map data to prices and we use posterior-based rules to minimize posterior expected loss; Thompson sampling can be seen as randomized Bayes decision-making that balances exploration and exploitation. Looking forward, mastery of TS-based dynamic pricing enables work on: (a) personalized treatment effect estimation where pricing is a continuous treatment; (b) robust/ambiguous preference learning where priors are misspecified and distributional robustness matters; (c) joint pricing and assortment optimization where the action is combinatorial; and (d) full reinforcement learning for revenue management where long-term stochastic dynamics and strategic customer behavior require planning (approximate dynamic programming, policy gradient methods). Specific downstream methods that rely on these ideas include contextual Gaussian process bandits for nonparametric price-response modeling, Bayesian experimental design for targeted promotions, and inventory-aware dynamic programming with learned demand models.

Quality: pending (0.0/5)

[← back to tree](/tech-tree/)[browse all →](/tech-tree/inventory/)
