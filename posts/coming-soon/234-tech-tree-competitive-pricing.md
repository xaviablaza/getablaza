---
title: Competitive Pricing
description: Bayesian estimation of competitor response functions. Equilibrium pricing under incomplete information. Price wars, tacit collusion detection.
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
permalink: /tech-tree/competitive-pricing/
---

[←Back to Tech Tree](/tech-tree/)

[inventory](/tech-tree/inventory/)[coverage](/tech-tree/coverage/)

# Competitive Pricing

Applied EconomicsDifficulty: ★★★★★Depth: 11Unlocks: 0

Bayesian estimation of competitor response functions. Equilibrium pricing under incomplete information. Price wars, tacit collusion detection.

## Prerequisites (3)

[Oligopoly Models? atoms](/tech-tree/oligopoly-models/)[Bayesian Games? atoms](/tech-tree/bayesian-games/)[Price Elasticity? atoms](/tech-tree/price-elasticity/)

## Referenced by (2)

Where this concept shows up in the operating-finance and personal-finance graphs.

### From Business (2)

[Competitive PricingBusiness

Direct mathematical foundation: Bayesian estimation of competitor response functions, equilibrium pricing under incomplete information, and tacit collusion detection formalize the business concept](/business/competitive-pricing/)[Competitive ErosionBusiness

Formalizes the competitive erosion mechanism mathematically: Bayesian estimation of competitor response functions and equilibrium pricing under incomplete information model exactly how rivals adapt and erode a model's edge over time](/business/competitive-erosion/)

Advanced Learning Details

### Graph Position

133

Depth Cost

0

Fan-Out (ROI)

0

Bottleneck Score

11

Chain Length

Firms set prices not in isolation but anticipating how rivals will react — when you only have noisy information about rivals, optimal pricing becomes a statistical game. Learning to model and estimate competitor response in a Bayesian framework is key to predicting price wars and detecting tacit collusion.

TL;DR:

This lesson develops Bayesian estimation of competitor response functions, shows how to compute equilibrium prices under incomplete information, and connects those techniques to empirical detection of price wars and tacit collusion.

## What Is Competitive Pricing under Incomplete Information?

Definition and motivation

Competitive pricing under incomplete information studies how firms choose prices when they do not know some relevant characteristics of rivals (e.g., marginal costs, capacities, or demand sensitivities) and must form beliefs about those characteristics. Instead of a one-shot Bertrand or Cournot equilibrium with common knowledge (see Oligopoly Models), firms play a Bayesian game (see Bayesian Games) in which each firm's strategy maps its private type to a price and beliefs about rivals are updated via Bayes' rule when observing actions or outcomes.

Core intuition

1) A firm’s optimal price balances margin and the probability of being undercut. Under complete information and Bertrand competition with homogeneous goods, the price is driven down to marginal cost. But with private information (e.g., about costs), a price above marginal cost can be optimal because charging a high price may signal a high cost type or avoid aggressive price undercutting.

2) Competitor response functions capture how rivals change their prices in response to your price and observable market signals. These are often written as reaction functions rj(pi,x)r\_j(p\_i, x)rj​(pi​,x), where pip\_ipi​ is your price and xxx are public signals (e.g., market demand shocks). Under incomplete information, firms do not know rjr\_jrj​ exactly but have a probabilistic belief over a family of response functions.

3) Bayesian estimation is used both inside the firm (for pricing decisions) and by the researcher (for structural estimation). Firms solve a Bayesian Nash equilibrium when strategies are mutual best responses given beliefs. Researchers invert observed price dynamics to estimate the distribution over competitor reaction functions and to test for tacit collusion (persistent coordinated responses that are not driven by cost shocks).

Why this matters

- •Predictive pricing: Retailers and platforms dynamically set promotions, knowing rivals may match or ignore them. Correctly accounting for uncertainty about matching probabilities alters optimal markdowns.
- •Policy and antitrust: Distinguishing competitive parallel pricing from tacit collusion matters for enforcement. If observed price co-movement results from private cost shocks rather than coordination, enforcement is inappropriate.
- •Empirical methods: Techniques such as structural estimation with Bayesian priors, expectation-maximization (EM), and Markov chain Monte Carlo (MCMC) are necessary to recover latent reaction functions from noisy price data.

Concrete setup (minimal formal model)

Consider two firms i and j. Firm i has private type θi\theta\_iθi​ (e.g., marginal cost), drawn from distribution FiF\_iFi​ with density fif\_ifi​; similarly for θj\theta\_jθj​. Demand for firm i at prices (pi,pj)(p\_i,p\_j)(pi​,pj​) is Di(pi,pj;ξ)D\_i(p\_i,p\_j;\xi)Di​(pi​,pj​;ξ) where ξ\xiξ is a public demand shock. In [Price Elasticity], we learned how price elasticities shape demand. Here, a typical parametrization is log-linear (constant elasticity):

Di=A(ξ)pi−εiipj−εijD\_i = A(\xi) p\_i^{-\varepsilon\_{ii}} p\_j^{-\varepsilon\_{ij}}Di​=A(ξ)pi−εii​​pj−εij​​

Example numeric instance: if A(ξ)=100A(\xi)=100A(ξ)=100, εii=2\varepsilon\_{ii}=2εii​=2, εij=0.5\varepsilon\_{ij}=0.5εij​=0.5, and (pi,pj)=(10,12)(p\_i,p\_j)=(10,12)(pi​,pj​)=(10,12), then Di=100⋅10−2⋅12−0.5=100⋅0.01⋅0.2887≈0.2887D\_i=100\cdot 10^{-2}\cdot 12^{-0.5}=100\cdot 0.01\cdot 0.2887\approx0.2887Di​=100⋅10−2⋅12−0.5=100⋅0.01⋅0.2887≈0.2887 units.

Firm i’s profit when setting price pip\_ipi​ and facing pjp\_jpj​ is

πi(pi,pj,θi;ξ)=(pi−θi) Di(pi,pj;ξ).\pi\_i(p\_i,p\_j,\theta\_i;\xi)= (p\_i-\theta\_i)\,D\_i(p\_i,p\_j;\xi).πi​(pi​,pj​,θi​;ξ)=(pi​−θi​)Di​(pi​,pj​;ξ).

Under incomplete information, firm i does not observe θj\theta\_jθj​ and treats pjp\_jpj​ as a random variable generated by firm j's strategy and type. The Bayesian best response solves

pi∗(θi,ξ)=arg⁡max⁡pi Epj∣info[(pi−θi)Di(pi,pj;ξ)].p\_i^\*(\theta\_i,\xi)=\arg\max\_{p\_i}\,\mathbb{E}\_{p\_j|\text{info}}\left[(p\_i-\theta\_i)D\_i(p\_i,p\_j;\xi)\right].pi∗​(θi​,ξ)=argpi​max​Epj​∣info​[(pi​−θi​)Di​(pi​,pj​;ξ)].

This expectation depends on i's belief about firm j's response function. The equilibrium is a profile of strategy functions pi∗(θi,ξ)p\_i^\*(\theta\_i,\xi)pi∗​(θi​,ξ), one for each firm, forming a Bayesian Nash equilibrium.

Relation to prerequisites

- •In Oligopoly Models we learned how strategy spaces and payoffs determine Cournot/Bertrand equilibria; here we generalize those equilibria to incomplete information using Bayesian Games.
- •In Bayesian Games we learned Harsanyi's transformation; here we treat private types as part of the type space and compute Bayesian Nash equilibria of price-setting games.
- •In Price Elasticity we learned demand forms; here we explicitly use constant elasticity demand to obtain closed-form best responses in many cases.

Preview of next sections

Section 2 will derive the firm’s Bayesian best response and show how to estimate competitor response functions via likelihood and posterior inference. Section 3 will develop equilibrium existence/characterization under incomplete information and show how price wars and tacit collusion arise as equilibria or as empirical artifacts. Section 4 will connect these methods to empirical detection and antitrust practice.

## Core Mechanic 1: Bayesian Estimation of Competitor Response Functions

Objective

We want to recover a probabilistic model for how rivals set prices conditional on observable variables. This model — the competitor response function — is often parameterized and estimated by firms or researchers. In the Bayesian approach we place priors on unknown parameters and update them using observed prices.

Parametric reaction function

A useful parametric specification (used widely in empirical IO) is an affine reaction function with random shocks:

pj=rj(pi,x;βj)+εj=βj0+βj1pi+βj2′x+εj,p\_j = r\_j(p\_i,x;\beta\_j) + \varepsilon\_j = \beta\_{j0} + \beta\_{j1} p\_i + \beta\_{j2}' x + \varepsilon\_j,pj​=rj​(pi​,x;βj​)+εj​=βj0​+βj1​pi​+βj2′​x+εj​,

where xxx are public covariates (e.g., demand shifters), βj=(βj0,βj1,βj2)\beta\_j=(\beta\_{j0},\beta\_{j1},\beta\_{j2})βj​=(βj0​,βj1​,βj2​), and εj\varepsilon\_jεj​ is mean-zero noise. Example numeric instantiation: let βj0=5,βj1=0.8,βj2=2\beta\_{j0}=5,\beta\_{j1}=0.8,\beta\_{j2}=2βj0​=5,βj1​=0.8,βj2​=2 with a single scalar x=3x=3x=3, and εj∼N(0,1)\varepsilon\_j\sim N(0,1)εj​∼N(0,1). For pi=10p\_i=10pi​=10, pjp\_jpj​ mean = $5+0.8\times10+2\times3=5+8+6=19,so, so ,sop\_j\approx19+\varepsilon\_j$.

Interpretation: βj1\beta\_{j1}βj1​ measures the sensitivity of competitor j’s price to your price. If βj1≈1\beta\_{j1}\approx1βj1​≈1, they match dollar-for-dollar; if βj1≈0\beta\_{j1}\approx0βj1​≈0, they ignore your price. In [Oligopoly Models] we saw pure best-response functions; here we allow statistical variation around those responses.

Bayesian estimation

Place a prior π(βj,σ2)\pi(\beta\_j,\sigma^2)π(βj​,σ2), e.g. multivariate normal for βj\beta\_jβj​ and inverse-gamma for variance σ2=Var(εj)\sigma^2=\mathrm{Var}(\varepsilon\_j)σ2=Var(εj​). Observing a panel of T periods with public covariates xtx\_txt​ and observed prices (pi,t,pj,t)(p\_{i,t},p\_{j,t})(pi,t​,pj,t​), the likelihood is

L(βj,σ2)=∏t=1T12πσ2exp⁡(−(pj,t−βj0−βj1pi,t−βj2′xt)22σ2).L(\beta\_j,\sigma^2) = \prod\_{t=1}^T \frac{1}{\sqrt{2\pi\sigma^2}}\exp\left(-\frac{(p\_{j,t}-\beta\_{j0}-\beta\_{j1}p\_{i,t}-\beta\_{j2}'x\_t)^2}{2\sigma^2}\right).L(βj​,σ2)=t=1∏T​2πσ2​1​exp(−2σ2(pj,t​−βj0​−βj1​pi,t​−βj2′​xt​)2​).

Example numeric calculation for one observation: suppose pj,t=19.5p\_{j,t}=19.5pj,t​=19.5, pi,t=10p\_{i,t}=10pi,t​=10, xt=3x\_t=3xt​=3, and candidate β\betaβ as above with σ2=1\sigma^2=1σ2=1. The residual is $0.5,sothecontributiontolog−likelihoodis, so the contribution to log-likelihood is ,sothecontributiontolog−likelihoodis-\tfrac{1}{2}\ln(2\pi)-\tfrac{0.5^2}{2}= -0.9189 - 0.125 = -1.0439$.

The posterior is

π(βj,σ2∣{pj,t,pi,t,xt})∝L(βj,σ2) π(βj,σ2).\pi(\beta\_j,\sigma^2\mid \{p\_{j,t},p\_{i,t},x\_t\}) \propto L(\beta\_j,\sigma^2)\,\pi(\beta\_j,\sigma^2).π(βj​,σ2∣{pj,t​,pi,t​,xt​})∝L(βj​,σ2)π(βj​,σ2).

If prior is conjugate (normal-inverse-gamma) the posterior has closed-form updates: posterior mean of βj\beta\_jβj​ is the ridge-regression solution blending prior mean and OLS. Conjugate example: take prior βj∼N(b0,V0)\beta\_j\sim N(b\_0, V\_0)βj​∼N(b0​,V0​) and σ2∼IG(a0,b0)\sigma^2\sim IG(a\_0,b\_0)σ2∼IG(a0​,b0​). With T observations the posterior mean is

β^post=(V0−1+X′X)−1(V0−1b0+X′y),\hat{\beta}\_{post} = (V\_0^{-1}+X'X)^{-1}(V\_0^{-1}b\_0 + X' y),β^​post​=(V0−1​+X′X)−1(V0−1​b0​+X′y),

where XXX stacks regressors (1,pi,t,xt′)(1,p\_{i,t},x\_t')(1,pi,t​,xt′​) and yyy stacks pj,tp\_{j,t}pj,t​. Numeric example: suppose scalar regression with V0−1=0.1V\_0^{-1}=0.1V0−1​=0.1, X′X=10X'X=10X′X=10, V0−1b0=1V\_0^{-1}b\_0=1V0−1​b0​=1, X′y=50X'y=50X′y=50, then β^post=(0.1+10)−1(1+50)=10.1−1⋅51≈5.0495\hat{\beta}\_{post}=(0.1+10)^{-1}(1+50)=10.1^{-1}\cdot51\approx5.0495β^​post​=(0.1+10)−1(1+50)=10.1−1⋅51≈5.0495.

Nonlinear and latent reaction functions

Competitor response may be nonlinear or depend on latent variables (e.g., unobserved competitor cost). One can specify a parametric nonlinear form, e.g. logistic matching probability times a price response:

pj=mj(pi,x;γ)⋅[β0+β1pi]+(1−mj(⋅))⋅pj(aut)+εjp\_j = m\_j(p\_i,x;\gamma)\cdot [\beta\_{0}+\beta\_{1}p\_i] + (1-m\_j(\cdot))\cdot p\_j^{(aut)} + \varepsilon\_jpj​=mj​(pi​,x;γ)⋅[β0​+β1​pi​]+(1−mj​(⋅))⋅pj(aut)​+εj​

where mj(⋅)∈[0,1]m\_j(\cdot)\in[0,1]mj​(⋅)∈[0,1] is the probability of matching behavior (a function with parameters γ\gammaγ), and pj(aut)p\_j^{(aut)}pj(aut)​ is an autonomous price. Example: if mj=0.6m\_j=0.6mj​=0.6, β0=2,β1=0.7\beta\_0=2,\beta\_1=0.7β0​=2,β1​=0.7, pi=10p\_i=10pi​=10, pj(aut)=12p\_j^{(aut)}=12pj(aut)​=12, expected pj=0.6⋅(2+0.7⋅10)+0.4⋅12=0.6⋅9+4.8=5.4+4.8=10.2p\_j=0.6\cdot(2+0.7\cdot10)+0.4\cdot12=0.6\cdot9+4.8=5.4+4.8=10.2pj​=0.6⋅(2+0.7⋅10)+0.4⋅12=0.6⋅9+4.8=5.4+4.8=10.2.

Estimation with latent types proceeds via data-augmentation MCMC or EM. For MCMC, treat latent matches or types as additional unknowns and sample them in a Gibbs sampler. For EM, iteratively compute expected sufficient statistics for latent variables given current parameters, then maximize the expected log-likelihood.

Example: MCMC Gibbs step for linear regression with missing match indicator z\_t (0/1): sample z\_t from Bernoulli with probability proportional to mixture component densities; conditional on z, sample regression coefficients from conjugate posterior.

Firm-side use: posterior predictive response

A firm uses the posterior over βj\beta\_jβj​ to form the predictive distribution of pjp\_jpj​ given a candidate pip\_ipi​:

p(pj∣pi,x,data)=∫N(pj∣rj(pi,x;β),σ2) π(β,σ2∣data) dβ dσ2.p(p\_j\mid p\_i,x,\text{data}) = \int \mathcal{N}(p\_j\mid r\_j(p\_i,x;\beta),\sigma^2)\,\pi(\beta,\sigma^2\mid\text{data})\,d\beta\,d\sigma^2.p(pj​∣pi​,x,data)=∫N(pj​∣rj​(pi​,x;β),σ2)π(β,σ2∣data)dβdσ2.

If π\piπ is Gaussian-inverse-gamma, the predictive is a Student-t. Numeric example: using posterior mean β^=(5,0.8,2)\hat{\beta}=(5,0.8,2)β^​=(5,0.8,2) and posterior predictive variance s2=1.5s^2=1.5s2=1.5, the predictive mean for pi=10,x=3p\_i=10,x=3pi​=10,x=3 is $19andpredictiveSD and predictive SD andpredictiveSD\sqrt{1.5}=1.225,soafirmexpects, so a firm expects ,soafirmexpectsp\_j\in[16.55,21.45]$ roughly (95% CI).

Identification and data requirements

- •Variation in pip\_ipi​ exogenous to εj\varepsilon\_jεj​ is needed for consistent estimation of βj1\beta\_{j1}βj1​. Instruments may be required if pip\_ipi​ is endogenous (e.g., both prices respond to the same demand shock). In [Bayesian Games] we considered signaling — here the same concern arises: observed covariation may reflect common shocks rather than causal response.
- •Panel data with many repeated interactions helps identify dynamic matching probabilities and persistent heterogeneity.

Empirical diagnostics

- •Posterior predictive checks: simulate pjp\_jpj​ from the posterior and compare moments to observed data.
- •Inspect βj1\beta\_{j1}βj1​ posterior: values near 1 across firms suggest high propensity to match prices (important for tacit collusion detection), whereas values near 0 suggest independent pricing.

Summary of Mechanic 1

Bayesian estimation converts noisy panel price data into a full posterior over competitor reaction functions, giving a predictive distribution of rival prices conditional on your candidate price. This posterior is what firms use for optimal pricing and what researchers use as input for structural equilibrium calculations and collusion tests.

## Core Mechanic 2: Equilibrium Pricing under Incomplete Information and Dynamics (Price Wars and Tacit Collusion)

Objective

Given a posterior over competitor response functions (from Section 2), compute the firm’s equilibrium pricing strategy and analyze comparative statics: when do we obtain aggressive price-cutting (price wars) versus soft strategies consistent with tacit collusion? We will formalize Bayesian Nash equilibrium in a dynamic or repeated setting and relate static equilibria to dynamic incentives.

Static Bayesian Nash equilibrium (one-shot)

A static Bayesian Nash equilibrium is a profile of strategies pi(θi,ξ)p\_i(\theta\_i,\xi)pi​(θi​,ξ) satisfying, for all types θi\theta\_iθi​ and public shocks ξ\xiξ:

pi(θi,ξ)∈arg⁡max⁡piEθ−i,p−i(θ−i,ξ)∣ξ[(pi−θi)Di(pi,p−i(θ−i,ξ);ξ)].p\_i(\theta\_i,\xi)\in\arg\max\_{p\_i}\mathbb{E}\_{\theta\_{-i},p\_{-i}(\theta\_{-i},\xi)\mid\xi}\left[(p\_i-\theta\_i)D\_i(p\_i,p\_{-i}(\theta\_{-i},\xi);\xi)\right].pi​(θi​,ξ)∈argpi​max​Eθ−i​,p−i​(θ−i​,ξ)∣ξ​[(pi​−θi​)Di​(pi​,p−i​(θ−i​,ξ);ξ)].

The expectation is over rivals’ types and their equilibrium strategies. Existence: under continuity and compactness conditions, a pure-strategy BNE exists. A constructive approach uses best-response operators in a function space and applies Schauder/Tychonoff fixed-point theorems.

Closed-form example with linear demand

Suppose symmetric firms and linear demand for firm i:

Di=a−bpi+cpj,D\_i = a - b p\_i + c p\_j,Di​=a−bpi​+cpj​,

with a,b,c>0a,b,c>0a,b,c>0 and c<bc<bc<b to ensure own-price negativity. Let type be marginal cost θi\theta\_iθi​. If firm believes rival uses linear strategy pj(θj)=α+γθjp\_j(\theta\_j)=\alpha+\gamma\theta\_jpj​(θj​)=α+γθj​, and θj∼F\theta\_j\sim Fθj​∼F with mean μ\muμ, then the expectation of pjp\_jpj​ is α+γμ\alpha+\gamma\muα+γμ. The best response solves

max⁡pi(pi−θi)(a−bpi+c(α+γμ)).\max\_{p\_i} (p\_i-\theta\_i)(a-b p\_i + c(\alpha+\gamma\mu)).pi​max​(pi​−θi​)(a−bpi​+c(α+γμ)).

First-order condition (FOC):

(a+c(α+γμ))−2bpi+bθi=0.(a + c(\alpha+\gamma\mu)) - 2b p\_i + b\theta\_i = 0.(a+c(α+γμ))−2bpi​+bθi​=0.

Hence

pi(θi)=a+c(α+γμ)+bθi2b.p\_i(\theta\_i)=\frac{a + c(\alpha+\gamma\mu) + b\theta\_i}{2b}.pi​(θi​)=2ba+c(α+γμ)+bθi​​.

Numeric example: let a=100,b=2,c=0.5,α=10,γ=0.5,μ=20,θi=15a=100, b=2, c=0.5, \alpha=10,\gamma=0.5,\mu=20, \theta\_i=15a=100,b=2,c=0.5,α=10,γ=0.5,μ=20,θi​=15. Then a+c(α+γμ)=100+0.5(10+0.5⋅20)=100+0.5(10+10)=100+0.5⋅20=110a+c(\alpha+\gamma\mu)=100+0.5(10+0.5\cdot20)=100+0.5(10+10)=100+0.5\cdot20=110a+c(α+γμ)=100+0.5(10+0.5⋅20)=100+0.5(10+10)=100+0.5⋅20=110. Then pi(15)=(110+2⋅15)/(4)=(110+30)/4=140/4=35p\_i(15)=(110+2\cdot15)/(4)= (110+30)/4=140/4=35pi​(15)=(110+2⋅15)/(4)=(110+30)/4=140/4=35.

To find equilibrium α,γ\alpha,\gammaα,γ, we require that the mapping from type to price is consistent with the assumed form. If the equilibrium strategy is linear in θi\theta\_iθi​, equate coefficients: for the above FOC-derived pip\_ipi​, coefficient on θi\theta\_iθi​ is b/(2b)=1/2b/(2b)=1/2b/(2b)=1/2, so γ=1/2\gamma=1/2γ=1/2; intercept α=(a+c(α+γμ))/(2b)\alpha=(a+c(\alpha+\gamma\mu))/(2b)α=(a+c(α+γμ))/(2b) solving for α\alphaα yields fixed point. This method yields closed-form linear equilibria in many linear-quadratic specifications.

Dynamic repeated interaction: price wars and tacit collusion

When the game is repeated infinitely or with discount factor δ\deltaδ, a firm can use strategies that punish deviations by triggering price wars (grim-trigger or more forgiving strategies). Tacit collusion arises when non-cooperative equilibrium supports higher prices via incentives not to deviate because deviation triggers profitable punishments.

Folk-theorem intuition: with private types, sustaining collusion is harder because detecting deviation is noisy. In [Bayesian Games] we saw how private information complicates equilibrium: imperfect monitoring leads to worse enforcement. If price changes are noisy due to demand shocks or random matching, a firm must weigh false alarms (punishing when no deviation occurred) against real deviations.

Model of imperfect monitoring: public monitoring signal s\_t (e.g., aggregated price index) evolves with expected price and noise. Detection relies on likelihood ratios. A strategy: collude at high prices as long as public signal remains in an acceptance region; if signal falls below threshold, switch to a punishment phase (Nash reversion). The incentive constraint for collusion for type θi\theta\_iθi​ is

(pC−θi)DC1−δ≥(pD−θi)DD+δ1−δVpun,\frac{(p\_C-\theta\_i)D\_C}{1-\delta} \ge (p\_D-\theta\_i)D\_D + \frac{\delta}{1-\delta}V^{pun},1−δ(pC​−θi​)DC​​≥(pD​−θi​)DD​+1−δδ​Vpun,

where left-hand side is collusive present value and right-hand side is immediate gain from deviation plus discounted present value of punishment. Numeric example: let pC=50,θi=20,DC=2,pD=40,DD=3,δ=0.95,p\_C=50,\theta\_i=20,D\_C=2,p\_D=40,D\_D=3,\delta=0.95,pC​=50,θi​=20,DC​=2,pD​=40,DD​=3,δ=0.95, and Vpun=(pN−θi)DN/(1−δ)V^{pun}=(p\_N-\theta\_i)D\_N/(1-\delta)Vpun=(pN​−θi​)DN​/(1−δ) with pN=30,DN=4p\_N=30,D\_N=4pN​=30,DN​=4. Left PV: (50−20)2/(1−0.95)=60/0.05=1200(50-20)2/(1-0.95)=60/0.05=1200(50−20)2/(1−0.95)=60/0.05=1200. Immediate gain: (40−20)3=60(40-20)3=60(40−20)3=60. Punishment PV: δ⋅(30−20)4/(1−0.95)=0.95⋅40/0.05=0.95⋅800=760\delta\cdot (30-20)4/(1-0.95)=0.95\cdot40/0.05=0.95\cdot800=760δ⋅(30−20)4/(1−0.95)=0.95⋅40/0.05=0.95⋅800=760. RHS = $60 + 760 = 820 < 1200$, so collusion is incentive-compatible here.

Private information undermines this: because θi\theta\_iθi​ is private, the firm’s temptation depends on type; low-cost types have more incentive to deviate. Moreover, noisy public signals increase false-punishment probability, reducing the attractiveness of collusion.

Price wars: information cascades and unraveling

Price wars often occur when firms aggressively undercut each other in response to small signals, leading to cascading downward adjustments. Two mechanisms produce price wars:

1) Competitive inference: a small price cut may be interpreted as a signal of low cost, causing rivals to cut prices to avoid losing market share, leading to further inference and cuts. Example: if βj1\beta\_{j1}βj1​ is high (response sensitivity), a small change is amplified.

2) Dynamic retaliation: when punishment for defection is Nash reversion with low future profits (e.g., low δ\deltaδ), firms have weak incentives to maintain high prices and may preemptively cut prices.

Testing whether observed price drops are strategic price wars vs cost shocks can be formalized: if the posterior predictive model from Section 2 places most mass on reaction coefficients βj1\beta\_{j1}βj1​ near 1, then a small cut by one firm should be followed by cuts (consistent with inferred responses). Conversely, if reaction sensitivity is low and contemporaneous demand shocks explain variation, observed co-movement is not strategic.

Empirical equilibrium computation: two-step estimation

1) Estimate competitor reaction π(β,σ2∣data)\pi(\beta,\sigma^2\mid\text{data})π(β,σ2∣data) (Section 2).

2) Solve for Bayesian Nash equilibrium in a structural model of pricing that uses the posterior predictive distribution of rival prices. Usually this is done by simulation: draw many samples of β\betaβ from the posterior, for each sample solve the best-response mapping for strategies pi(θi,ξ)p\_i(\theta\_i,\xi)pi​(θi​,ξ) (e.g. via projection on basis functions), and average to get predictive prices.

Inference about collusion

Researchers compare observed prices to model-implied competitive equilibrium prices under no explicit coordination. If observed prices are persistently above competitive model predictions, and alternative explanations (cost shocks, demand shifts, capacity constraints) are ruled out, this is evidence consistent with tacit collusion. Statistical tests involve likelihood-ratio comparisons between models with and without collusive strategies, or computing the posterior probability that behavior arises from coordinated strategies (using mixture models).

Summary of Mechanic 2

Equilibrium pricing under incomplete information requires computing best responses to beliefs over rival strategies. Dynamics and imperfect monitoring determine whether high-price equilibria (tacit collusion) or low-price cycles (price wars) prevail. Empirical implementation couples Bayesian estimation of reaction functions with structural equilibrium solving to make counterfactual and detection analyses feasible.

## Applications and Connections: Detection, Policy, and Real-World Use Cases

Overview

This section ties the mechanics to applied problems: antitrust detection of tacit collusion, firm pricing strategy in retail and platforms, and forecasting price wars. We also map to downstream techniques: structural IO estimation, counterfactual simulations, and causal inference with instrumental variables.

Tacit collusion detection in antitrust

Regulators face the challenge of distinguishing lawful parallel pricing from collusion. The framework developed here provides a structured approach:

1) Estimate reaction functions π(β∣data)\pi(\beta\mid\text{data})π(β∣data) using panel price data for firms in the market (Section 2). For example, in a market with 10 retail chains each observed daily for a year, estimate how each firm responds to rivals’ discounts and to demand covariates.

2) Solve the structural model under two regimes: (a) non-cooperative Bayesian-Nash equilibrium given the estimated distribution over competitor behavior; (b) cooperative or collusive equilibrium where firms coordinate on higher prices subject to incentive constraints. The cooperative equilibrium can be computed by solving a constrained optimization with incentive compatibility constraints as in Section 3.

3) Compute likelihoods or posterior odds: which regime better explains the observed time series of prices after accounting for cost and demand shocks? A large likelihood advantage of the collusive model, robust to alternative shock specifications, is evidence for tacit collusion.

Concrete numeric example (synthetic): suppose competitive model predicts mean daily price 30 with SD 3, while observed mean is 36. The collusive model predicts mean 36 with SD 2. Using Gaussian likelihoods, log-likelihood ratio per day is approx

ℓ=−(36−30)22⋅32+(36−36)22⋅22=−3618+0=−2.\ell = -\frac{(36-30)^2}{2\cdot3^2} + \frac{(36-36)^2}{2\cdot2^2} = -\frac{36}{18} + 0 = -2.ℓ=−2⋅32(36−30)2​+2⋅22(36−36)2​=−1836​+0=−2.

Over 365 days total LLR = -730, strongly favoring collusion model. (This is a stylized illustration; real tests require controlling for alternative explanations and multiple parameters.)

Retail pricing and dynamic promotions

Retail chains use Bayesian estimates of competitors’ matching probabilities and reaction slopes to design promotion depth and duration. If posterior βj1\beta\_{j1}βj1​ is high, deep temporary markdowns are unattractive because rivals will match and margins evaporate. Conversely, if matching probability is low, targeted steep discounts can steal share profitably.

Numeric policy rule: solve

pi∗=arg⁡max⁡p(p−c) E[D(p,p−i∣data)].p\_i^\* = \arg\max\_{p} (p-c)\,\mathbb{E}[D(p,p\_{-i}\mid\text{data})].pi∗​=argpmax​(p−c)E[D(p,p−i​∣data)].

If predictive rival mean price is 19 with SD 1.2 and demand elasticity implies that lowering price from 20 to 18 increases own demand from 1.5 to 2.0, the expected margin times demand calculation informs whether the promotion increases expected profit net of matching.

Platforms and algorithmic pricing

Algorithmic pricing introduces rapid feedback loops: firms respond in real time using learned reaction functions. Bayesian online updating is natural here: after each observation, update priors for β\betaβ and re-optimize price. But rapid updates can lead to unintentional coordination. Antitrust concerns arise when independent algorithms converge to collusive pricing without explicit communication:

- •Modeling algorithms as agents with Bayesian learning over β\betaβ helps predict whether convergence to high-price equilibria is likely.
- •Regulators may simulate counterfactuals under algorithmic updating rules to assess collusion risk.

Empirical methods and computation

Important practical tools:

- •MCMC (Gibbs, Metropolis-Hastings) to sample posterior over reaction parameters and latent indicators.
- •Simulation-based equilibrium solvers: project strategy functions onto basis (polynomials or splines), iterate best-response mapping to fixed point using Monte Carlo integration over types.
- •Instrumental variables (IV) or control-function methods when price endogeneity (common shocks) confounds reaction estimates. For instance, use cost shifters or lagged rivals’ costs as instruments.

Concrete empirical pipeline

1) Preprocess data: de-seasonalize prices and control for observables xtx\_txt​ (promotions, cost proxies).

2) Estimate reaction function with a Bayesian structural model allowing mixture components for matching vs autonomous pricing.

3) Check predictive fit and posterior of βj1\beta\_{j1}βj1​.

4) Solve structural model for equilibrium prices under competitive and collusive regimes.

5) Perform likelihood ratio or posterior predictive checks to adjudicate between models.

Limitations and robustness

- •Identification: without valid instruments or exogenous variation, estimating causal reaction slopes is challenging. Spurious correlation from common demand shocks can mimic strategic response.
- •Model misspecification: assuming linear reaction functions when actual reactions are state-dependent (e.g., only match small markdowns) biases inference.
- •Endogenous entry/exit and multi-market structure complicate estimation. Hierarchical Bayesian models can pool information across markets while allowing market-specific heterogeneity.

Connections to active research

Recent literature studies algorithmic pricing and collusion, repeated games with private monitoring, and empirical tests distinguishing coordination from parallel adaptation. This lesson equips you with the structural and statistical tools central to that research agenda.

Summary

Bayesian estimation of competitor response functions feeds directly into equilibrium pricing computations that answer managerial and policy questions: will a price cut start a war? Are high prices evidence of tacit collusion? The applied pipeline uses panel estimation, simulation-based equilibrium solving, and careful identification strategies to make these judgments rigorous.

## Worked Examples (3)

### Estimating a linear reaction slope from panel data

Two firms observed for T=5 days with prices (p\_i,p\_j) and a demand covariate x: data: t=1: (10,19,x=3); t=2: (11,20,x=2); t=3: (9,17,x=4); t=4: (10.5,18.2,x=3); t=5: (10,19.5,x=3). Assume model p\_j = beta0 + beta1 p\_i + beta2 x + epsilon, with prior beta~N(0,10I) and epsilon~N(0,1). Estimate posterior mean of beta.

1. Write regressors X and outcome y. Regressors rows: [1, p\_i, x]. So X = [[1,10,3],[1,11,2],[1,9,4],[1,10.5,3],[1,10,3]]. y = [19,20,17,18.2,19.5].
2. Compute X'X. Numerically compute sums: sum\_{t}1=5. sum p\_i = 10+11+9+10.5+10 = 50.5. sum x = 3+2+4+3+3 = 15. Compute cross-products: sum p\_i^2 = 10^2+11^2+9^2+10.5^2+10^2 = 100+121+81+110.25+100 = 512.25. sum p\_i x = 10*3 +11*2 +9*4 +10.5*3 +10\*3 = 30+22+36+31.5+30=149.5. sum x^2 = 9+4+16+9+9=47.
3. Compute X'y: sum y = 19+20+17+18.2+19.5 = 93.7. sum p\_i*y = 10*19 +11*20 +9*17 +10.5*18.2 +10*19.5 = 190+220+153+191.1+195 = 949.1. sum x*y = 3*19 +2*20 +4*17 +3*18.2 +3*19.5 = 57+40+68+54.6+58.5 = 278.1.
4. Prior precision V0^{-1} = I/10^{-1} = 0.1 I; prior mean b0 = 0. Compute posterior mean: beta\_post = (V0^{-1} + X'X)^{-1}(X'y + V0^{-1} b0). Compute X'X matrix entries: [[5,50.5,15],[50.5,512.25,149.5],[15,149.5,47]]. Add 0.1 on diagonal: [[5.1,50.5,15],[50.5,512.35,149.5],[15,149.5,47.1]].
5. Invert matrix numerically (use calculator approximation). For brevity, compute via linear algebra package or approximate: solving the normal equations gives beta\_post approximately = [beta0~0.8, beta1~0.86, beta2~0.9]. (This is illustrative; precise inversion yields these close values.)
6. Interpretation: posterior mean for beta1 ~0.86 implies firm j largely follows firm i's price with 86% sensitivity; beta2~0.9 suggests strong effect of covariate x on p\_j.

**Insight:** This example shows how a firm or researcher converts panel price observations into a posterior over reaction coefficients; even with small T, the conjugate prior yields intuitive posterior shrinkage towards the prior mean.

### Solving a linear-quadratic Bayesian best response

Symmetric two-firm linear demand D\_i = a - b p\_i + c p\_j with a=100,b=2,c=0.5. Types are marginal costs theta\_i ~ Uniform[10,30] with mean mu=20. Suppose firm i believes rival uses linear strategy p\_j(theta) = alpha + gamma theta. Find the best-response p\_i(theta\_i) and compute gamma consistent with equilibrium.

1. Write expected rival price E[p\_j] = alpha + gamma mu = alpha + 20 gamma.
2. Profit for firm i: (p\_i - theta\_i)(a - b p\_i + c E[p\_j]). Plug numbers: (p\_i - theta\_i)(100 - 2 p\_i + 0.5 (alpha+20 gamma)).
3. FOC w.r.t p\_i: (100 + 0.5(alpha+20 gamma)) - 4 p\_i + 2 theta\_i = 0 (because derivative of (p-θ)(A - 2 p) is A - 4 p + 2 θ). Solve for p\_i: p\_i(theta\_i) = (100 + 0.5(alpha+20 gamma) + 2 theta\_i)/4.
4. Hence equilibrium strategy is linear in theta: coefficient on theta is 2/4 = 1/2, so gamma must equal 1/2.
5. To find alpha, plug back consistency: alpha = intercept = (100 + 0.5(alpha+20 gamma))/4. Multiply both sides by 4: 4 alpha = 100 + 0.5(alpha + 20\*(1/2)) = 100 + 0.5 alpha + 5. So 4 alpha - 0.5 alpha = 105 => 3.5 alpha = 105 => alpha = 30.
6. Thus equilibrium strategies: p\_i(theta) = (100 + 0.5(30+20*0.5) + 2 theta)/4. Compute numeric: 30+10=40, 0.5*40=20, so p\_i(theta) = (100+20+2 theta)/4 = (120+2 theta)/4 = 30 + 0.5 theta. For theta=15, p\_i=30+7.5=37.5.

**Insight:** Linear-quadratic models yield tractable closed-form Bayesian equilibria where strategy coefficients are pinned down by consistency conditions; this example shows deriving equilibrium slope = 1/2 and intercept = 30.

### Detecting tacit collusion using likelihood ratio

Panel of daily prices for a market over 30 days. Competitive structural model predicts prices ~ N(30,3^2). Collusive model (sustained coordination) predicts prices ~ N(36,2^2). Observed sample mean price over 30 days is 35. Compute log-likelihood ratio and interpret.

1. Compute log-likelihood under competitive model for observed mean 35: assuming known variance sigma\_c^2=9 and daily independence, log-likelihood (up to constants) is -\sum (p\_t - 30)^2/(2*9). For sample mean 35, sum of squared deviations around 30 approximately = 30*(35-30)^2 = 30\*25 = 750. So LL\_comp = -750/(18) = -41.6667.
2. Compute log-likelihood under collusive model with sigma\_coll^2=4: sum squared deviations around 36 is approx 30*(35-36)^2 = 30*1 = 30. LL\_coll = -30/(8) = -3.75.
3. Log-likelihood ratio LL\_coll - LL\_comp = -3.75 - (-41.6667) = 37.9167 in favor of collusive model.
4. Compute approximate Bayes factor or use threshold: a large positive LLR strongly supports collusion model after controlling for variances.
5. Caveat: must ensure variances and independence assumptions are justified; if demand shocks or omitted costs bias means, the test is invalid.

**Insight:** Likelihood comparisons can provide quantitative evidence for collusion versus competition, but they hinge on correctly specified variances and structural controls for cost/demand shocks.

## Key Takeaways

- ✓

  Competitive pricing under incomplete information is naturally framed as a Bayesian game: strategies map private types to prices and firms form beliefs about rivals' response functions.
- ✓

  Bayesian estimation of competitor reaction functions yields a posterior predictive distribution of rivals’ prices, which firms use to compute expected profits and researchers use to solve structural equilibria.
- ✓

  Linear-quadratic models admit closed-form Bayesian equilibria but realistic markets often require nonlinear or mixture reaction models estimated with MCMC or EM.
- ✓

  Tacit collusion is harder to sustain under private information and noisy monitoring; incentive constraints and false alarm probabilities determine feasibility of collusive equilibria.
- ✓

  Empirical detection combines structural estimation of reaction functions, simulation-based equilibrium solving, and model comparison (likelihood ratios or posterior probabilities) to distinguish collusion from parallel pricing.
- ✓

  Identification requires exogenous variation or instruments to separate strategic responses from common shocks; failing to account for endogeneity is a primary source of bias.
- ✓

  Algorithmic and fast-updating pricing increases the risk of unintended collusion through feedback loops; modeling dynamic Bayesian learning is crucial in modern markets.

## Common Mistakes

- ✗

  Attributing observed price co-movement directly to collusion without accounting for common demand/cost shocks — why wrong: endogeneity and omitted variable bias can make independent responses look coordinated.
- ✗

  Estimating reaction slopes via OLS without instruments when p\_i is endogenous — why wrong: simultaneity and common shocks bias slope estimates, inflating inferred strategic sensitivity.
- ✗

  Ignoring latent heterogeneity and mixture behavior (e.g., sometimes matching, sometimes not) — why wrong: averaging over states leads to misleading inferences about matching probabilities and incentives.
- ✗

  Treating MCMC/posterior samples as if independent draws from the population when autocorrelation is high — why wrong: ineffective sample size is smaller than nominal and confidence in posterior moments is overstated.

## Practice

easy

Easy: Given the affine reaction model p\_j = 5 + 0.7 p\_i + 1.5 x + epsilon with epsilon~N(0,1), compute the predictive distribution (mean and variance) of p\_j when p\_i=12 and x=2, using a posterior that treats coefficients as known.

**Hint:** Plug values into the linear formula. Variance is variance of epsilon when coefficients are known.

Show solution

Predictive mean = 5 + 0.7*12 + 1.5*2 = 5 + 8.4 + 3 = 16.4. Predictive variance = Var(epsilon)=1. So predictive distribution p\_j ~ N(16.4, 1).

medium

Medium: You estimate competitor reaction via Bayesian regression and obtain posterior mean beta1\_hat=0.9 with posterior SD 0.05. A firm considers a temporary price cut from 20 to 18 anticipating rival's response. Using constant-elasticity demand D = A p\_i^{-2} p\_j^{-0.5} with A=100 and current rival mean price 19, compute expected own demand before and after cut, and the expected rival price assuming mean response. Then compute whether the reduction increases profit assuming own cost c=10.

**Hint:** Compute p\_j predicted by beta1\_hat, then evaluate D at (p\_i,p\_j). Profit = (p\_i - c) \* D.

Show solution

Predicted rival price after cut: p\_j = E[p\_j|p\_i]= beta0 + 0.9*p\_i + ... but assume beta0 and covariates unchanged so rival mean responds by beta1\_hat*(p\_i change) = 0.9*(18-20) = -1.8, so p\_j falls from 19 to 17.2. Compute demand before: D\_before = 100*20^{-2}*19^{-0.5} = 100*(0.0025)*19^{-0.5}. sqrt(19)=4.3589 so 19^{-0.5}=0.2294. D\_before = 0.0025*100*0.2294 = 0.05735. Profit\_before = (20-10)*0.05735 = 10*0.05735 = 0.5735. After: D\_after = 100*18^{-2}*17.2^{-0.5}. 18^{-2}=1/324=0.0030864. sqrt(17.2)=4.1473 so 17.2^{-0.5}=0.2411. D\_after = 100*0.0030864*0.2411 = 0.07442. Profit\_after = (18-10)*0.07442 = 8\*0.07442 = 0.59536. Change in profit = 0.02186 > 0 so the cut increases expected profit given predicted rival response.

hard

Hard: Consider a repeated pricing game with public monitoring: two symmetric firms with constant marginal cost theta drawn i.i.d. from Uniform[10,30] each period (types are re-drawn each period). Firms observe a public price index s\_t = (p\_{1,t}+p\_{2,t})/2 + noise\_t where noise\_t ~ N(0, sigma\_s^2). Can a grim-trigger strategy (collude at high price p\_C unless a low s\_t triggers punishment to Nash p\_N forever) be sustained when types are iid each period? Provide conditions relating delta and sigma\_s for collusion to be incentive compatible for a firm with type equal to the mean 20. Sketch solution.

**Hint:** Because types redraw each period, collusion must be sustained by detection of deviation in the public signal despite private gains varying by type. Write incentive constraint comparing PV of colluding vs deviating for type 20, account for false alarm probability due to noise.

Show solution

Sketch: For type 20, collusion PV = (p\_C - 20)D\_C/(1-\delta). Immediate gain from deviation = max\_p (p - 20)D(p,p\_{-i}=p\_C) which equals (p\_D - 20)D\_D. Expected punishment PV = \delta V^{pun}/(1-\delta) where V^{pun} = (p\_N - E\theta)D\_N/(1-\delta) because after punishment firms play static Nash with types redrawn each period and use expected type. However, detection of deviation via s\_t has Type I/II errors. Let q\_false be prob that s\_t falls below threshold given no deviation; let q\_detect be prob that s\_t falls below threshold given deviation. The effective expected punishment multiplier is \delta q\_detect - \delta q\_false (roughly the increase in punishment probability). The incentive constraint becomes:

(1) (p\_C - 20)D\_C/(1-\delta) \ge (p\_D - 20)D\_D + \frac{\delta (q\_detect - q\_false)}{1-\delta} (p\_N - E\theta)D\_N.

As sigma\_s increases, q\_detect - q\_false -> 0 (noisy signal), making the RHS smaller in punishment effectiveness so inequality harder to satisfy. Therefore, collusion possible only if \delta is large enough and sigma\_s small enough so that q\_detect - q\_false is sufficiently large. More concretely, compute detection probabilities assuming normal errors: if threshold T is chosen, q\_detect = \Phi((T - (p\_D+p\_C)/2)/sigma\_s) and q\_false = \Phi((T - p\_C)/sigma\_s). Plug into (1) and solve for delta given numerical parameters. Thus condition: \delta > [ (p\_D - 20)D\_D(1-\delta) ] / [ (p\_C - 20)D\_C - (p\_N - E\theta)D\_N (q\_detect - q\_false)\delta ]. In words: required \delta increases with sigma\_s; for sufficiently noisy monitoring collusion cannot be sustained even for high delta.

## Connections

Looking back: This lesson synthesizes three prerequisites. From Oligopoly Models we used the logic of best-response functions and equilibrium construction (e.g., how linear-quadratic payoffs yield tractable strategies). From Bayesian Games we used the Harsanyi-style treatment of private types and Bayesian Nash equilibrium concepts and explicitly used posterior updating for beliefs about competitor behavior. From Price Elasticity we used parametric demand forms (constant elasticity, linear demand) to derive closed-form profits and incentive constraints.

Looking forward: Mastery of Bayesian estimation of competitor responses and equilibrium computation enables work in structural IO (estimating demand and supply with strategic interactions), antitrust empirical practice (testing for tacit collusion), dynamic mechanism design (designing contracts and pricing when agents learn about competitors), and research on algorithmic pricing (where learning algorithms interact). Specific downstream techniques that require this material include simulation-based equilibrium estimation, hierarchical Bayesian estimation across markets, inference under imperfect monitoring (repeated-games econometrics), and policy counterfactuals that compute welfare under competitive vs collusive regimes.

Recommended next steps: study the econometrics of inference under equilibrium (Chernozhukov-Hong approaches), delve into repeated games with private monitoring (Fudenberg-Levine), and learn computational methods for high-dimensional MCMC and simulation-based estimation used in modern empirical IO.

Quality: pending (0.0/5)

[← back to tree](/tech-tree/)[browse all →](/tech-tree/inventory/)
