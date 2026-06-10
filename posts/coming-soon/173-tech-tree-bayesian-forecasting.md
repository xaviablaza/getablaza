---
title: Bayesian Forecasting
description: Posterior predictive distributions for time series. Structural time series models. Bayesian model averaging and model selection. Demand forecasting with uncertainty quantification.
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
permalink: /tech-tree/bayesian-forecasting/
---

[←Back to Tech Tree](/tech-tree/)

[inventory](/tech-tree/inventory/)[coverage](/tech-tree/coverage/)

# Bayesian Forecasting

Probability & StatisticsDifficulty: ★★★★★Depth: 12Unlocks: 1

Posterior predictive distributions for time series. Structural time series models. Bayesian model averaging and model selection. Demand forecasting with uncertainty quantification.

## Prerequisites (3)

[State-Space Models? atoms](/tech-tree/state-space-models/)[Hierarchical Bayesian Models? atoms](/tech-tree/hierarchical-models/)[Conjugate Priors? atoms](/tech-tree/conjugate-priors/)

## Unlocks (1)

[Dynamic Pricinglvl 5](/tech-tree/dynamic-pricing/)

## Referenced by (1)

Where this concept shows up in the operating-finance and personal-finance graphs.

### From Business (1)

[Value MigrationBusiness

The backtested prediction protocol is posterior predictive forecasting - updating beliefs about where value flows next given observed migration patterns, with uncertainty quantification over future states](/business/value-migration/)

Advanced Learning Details

### Graph Position

230

Depth Cost

1

Fan-Out (ROI)

1

Bottleneck Score

12

Chain Length

Forecasting without honest uncertainty is betting in the dark; Bayesian forecasting turns every forecast into a full probability statement so you can trade off risk, inventory, and service levels explicitly.

TL;DR:

Bayesian forecasting constructs posterior predictive distributions for future time series observations by integrating parameter and latent-state uncertainty, enabling coherent uncertainty quantification, principled model averaging, and robust demand forecasts with interpretable predictive intervals.

## What Is Bayesian Forecasting?

Definition and motivation

Bayesian forecasting is the process of producing probability distributions for future observations of a time series by conditioning on historical data and integrating over posterior uncertainty in both parameters and latent states. Formally, for observed data y1:Ty\_{1:T}y1:T​ and future horizon h≥1h\ge 1h≥1, the posterior predictive distribution is

p(yT+h∣y1:T)=∫p(yT+h∣θ,xT+h,y1:T) p(xT+h,θ∣y1:T) dxT+h dθ.p(y\_{T+h}\mid y\_{1:T})
= \int p(y\_{T+h}\mid \theta, x\_{T+h}, y\_{1:T})\,p(x\_{T+h},\theta\mid y\_{1:T})\,d x\_{T+h}\,d\theta.p(yT+h​∣y1:T​)=∫p(yT+h​∣θ,xT+h​,y1:T​)p(xT+h​,θ∣y1:T​)dxT+h​dθ.

This identity is the backbone: it separates aleatory uncertainty (conditional observation noise given states and parameters) from epistemic uncertainty (uncertainty about parameters θ\thetaθ and future latent states xT+hx\_{T+h}xT+h​).

Why care: uncertainty quantification, decision-making, and model comparison

- •Inventory/demand applications require not just a point forecast but tail probabilities to set stock levels and service-level constraints.
- •Bayesian forecasts naturally produce predictive intervals, predictive densities, and full probabilistic statements useful in expected-cost decisions.
- •Because we explicitly model parameter and structural uncertainty, Bayesian forecasting supports Bayesian model averaging (BMA) to hedge against model misspecification.

Relation to prerequisites

- •In State-Space Models, we learned how the Kalman filter and smoothing produce filtering and smoothing distributions for the latent state when parameters are known; Bayesian forecasting builds on that by treating parameters as uncertain and integrating them out.
- •In Hierarchical Bayesian Models, we learned partial pooling and hyperpriors; in forecasting this allows sharing information across related series (e.g., stores) so that forecasts borrow strength.
- •In Conjugate Priors, we learned closed-form posterior updates (e.g., Gamma-Poisson); those conjugate cases produce closed-form posterior predictives, which are computationally cheap and interpretable.

Concrete simple formula and numeric example

Consider IID Poisson counts yt∼Pois(λ)y\_t\sim\mathrm{Pois}(\lambda)yt​∼Pois(λ) with prior λ∼Gamma(α,β)\lambda\sim\mathrm{Gamma}(\alpha,\beta)λ∼Gamma(α,β) (shape-rate). The posterior is λ∣y1:T∼Gamma(α+∑yt, β+T)\lambda\mid y\_{1:T}\sim\mathrm{Gamma}(\alpha+\sum y\_t,\ \beta+T)λ∣y1:T​∼Gamma(α+∑yt​, β+T) and the posterior predictive for a future single count is Negative Binomial (Gamma-Poisson mixture):

p(yT+1=k∣y1:T)=Γ(α+S+k)k! Γ(α+S)(β+Tβ+T+1)α+S(1β+T+1)kp(y\_{T+1}=k\mid y\_{1:T}) = {\Gamma(\alpha+S+k)\over k!\,\Gamma(\alpha+S)}\left({\beta+T\over\beta+T+1}\right)^{\alpha+S}\left({1\over\beta+T+1}\right)^{k}p(yT+1​=k∣y1:T​)=k!Γ(α+S)Γ(α+S+k)​(β+T+1β+T​)α+S(β+T+11​)k

where S=∑t=1TytS=\sum\_{t=1}^T y\_tS=∑t=1T​yt​. Numeric example: if T=10T=10T=10, S=50S=50S=50, prior α=2,β=1\alpha=2,\beta=1α=2,β=1, then posterior shape =52=52=52, rate =11=11=11. The predictive mean is (α+S)/(β+T)=52/11≈4.727(\alpha+S)/(\beta+T) = 52/11 \approx 4.727(α+S)/(β+T)=52/11≈4.727 and the predictive variance is higher than the mean due to parameter uncertainty; the distribution is Negative Binomial with those parameters.

Key conceptual point

The posterior predictive is the unique object you should use for decision-making: it already accounts for parameter and latent-state uncertainty. The different computational strategies (closed-form conjugate, analytic Kalman-filter propagation, Monte Carlo integration, Sequential Monte Carlo) are simply ways to evaluate or approximate this integral.

## Core Mechanic 1: Posterior Predictive Calculation — Closed Form and Kalman Cases

Two canonical, illuminating cases give intuition and practical recipes: (A) conjugate observation models (e.g., Poisson-Gamma, Normal-Inverse-Gamma) and (B) linear Gaussian state-space models where Kalman filter analytic formulas produce predictive distributions conditional on parameters. Both yield explicit predictive forms that we can extend to parameter uncertainty by analytic marginalization or Monte Carlo.

A. Conjugate observation models (closed-form predictive)

If the observation model and prior are conjugate, integration over parameters yields closed-form posterior predictives. Example: Normal mean with unknown variance (Normal-Inverse-Gamma conjugacy). Suppose

yt∣μ,σ2∼N(μ,σ2),(μ,σ2)∼NIG(μ0,κ0,α0,β0)y\_t\mid \mu,\sigma^2 \sim \mathcal N(\mu,\sigma^2),\qquad (\mu,\sigma^2)\sim \mathrm{NIG}(\mu\_0,\kappa\_0,\alpha\_0,\beta\_0)yt​∣μ,σ2∼N(μ,σ2),(μ,σ2)∼NIG(μ0​,κ0​,α0​,β0​)

In this case the one-step posterior predictive is a Student-t:

yT+1∣y1:T∼t2αT(μT,βT(κT+1)αTκT)y\_{T+1}\mid y\_{1:T} \sim t\_{2\alpha\_T}\left(\mu\_T,\frac{\beta\_T(\kappa\_T+1)}{\alpha\_T\kappa\_T}\right)yT+1​∣y1:T​∼t2αT​​(μT​,αT​κT​βT​(κT​+1)​)

with posterior hyperparameters κT=κ0+T\kappa\_T=\kappa\_0+TκT​=κ0​+T, μT=(κ0μ0+Tyˉ)/κT\mu\_T=(\kappa\_0\mu\_0+T\bar y)/\kappa\_TμT​=(κ0​μ0​+Tyˉ​)/κT​, αT=α0+T/2\alpha\_T=\alpha\_0+T/2αT​=α0​+T/2, βT=β0+12∑(yt−yˉ)2+κ0T(yˉ−μ0)22κT\beta\_T=\beta\_0+\tfrac12\sum (y\_t-\bar y)^2+\tfrac{\kappa\_0 T(\bar y-\mu\_0)^2}{2\kappa\_T}βT​=β0​+21​∑(yt​−yˉ​)2+2κT​κ0​T(yˉ​−μ0​)2​. Numeric example: prior μ0=0,κ0=1,α0=2,β0=2\mu\_0=0,\kappa\_0=1,\alpha\_0=2,\beta\_0=2μ0​=0,κ0​=1,α0​=2,β0​=2, data T=4T=4T=4 with y=(3,4,2,5)y=(3,4,2,5)y=(3,4,2,5) so yˉ=3.5\bar y=3.5yˉ​=3.5, sample variance ∑(yt−yˉ)2=5\sum(y\_t-\bar y)^2=5∑(yt​−yˉ​)2=5. Then κT=5\kappa\_T=5κT​=5, μT=(1∗0+4∗3.5)/5=2.8\mu\_T=(1\*0+4\*3.5)/5=2.8μT​=(1∗0+4∗3.5)/5=2.8, αT=4\alpha\_T=4αT​=4, and βT=2+2.5+1∗4∗(3.5−0)22∗5=4.5+4925=6.46\beta\_T=2+2.5+\tfrac{1\*4\*(3.5-0)^2}{2\*5}=4.5+\tfrac{49}{25}=6.46βT​=2+2.5+2∗51∗4∗(3.5−0)2​=4.5+2549​=6.46 (approx). The predictive is approximately t8(2.8, scale2≈6.46∗(6/5)/(4∗5))t\_8(2.8,\:\text{scale}^2\approx 6.46\*(6/5)/(4\*5))t8​(2.8,scale2≈6.46∗(6/5)/(4∗5)) — compute numerically to get predictive mean 2.8 and heavier tails than Gaussian.

Why this matters: the predictive Student-t reflects uncertainty in both mean and variance; credible intervals are wider than plug-in intervals.

B. Linear-Gaussian state-space: Kalman predictive and marginalization over parameters

Consider the Dynamic Linear Model (DLM):

State evolution: xt+1=Ftxt+wtx\_{t+1}=F\_t x\_t + w\_txt+1​=Ft​xt​+wt​, wt∼N(0,Wt)w\_t\sim\mathcal N(0,W\_t)wt​∼N(0,Wt​)

Observation: yt=Htxt+vty\_t=H\_t x\_t + v\_tyt​=Ht​xt​+vt​, vt∼N(0,Vt)v\_t\sim\mathcal N(0,V\_t)vt​∼N(0,Vt​)

If parameters (Ft,Ht,Wt,Vt)(F\_t,H\_t,W\_t,V\_t)(Ft​,Ht​,Wt​,Vt​) are known, the Kalman filter gives the predictive distribution for yT+1y\_{T+1}yT+1​:

xT∣T−1∼N(mT∣T−1,CT∣T−1),yT+1∣y1:T∼N(HT+1mT∣T−1, HT+1CT∣T−1HT+1⊤+VT+1).x\_{T\mid T-1}\sim\mathcal N(m\_{T\mid T-1}, C\_{T\mid T-1}),\qquad y\_{T+1}\mid y\_{1:T}\sim\mathcal N(H\_{T+1}m\_{T\mid T-1},\ H\_{T+1}C\_{T\mid T-1}H\_{T+1}^\top+V\_{T+1}).xT∣T−1​∼N(mT∣T−1​,CT∣T−1​),yT+1​∣y1:T​∼N(HT+1​mT∣T−1​, HT+1​CT∣T−1​HT+1⊤​+VT+1​).

Concrete numeric example: local level model with scalar state xt+1=xt+ηtx\_{t+1}=x\_t+\eta\_txt+1​=xt​+ηt​ (W=0.5W=0.5W=0.5), observations yt=xt+ϵty\_t=x\_t+\epsilon\_tyt​=xt​+ϵt​ (V=1V=1V=1), prior x0∼N(0,1)x\_0\sim\mathcal N(0,1)x0​∼N(0,1). After observing T=3T=3T=3 data y=(1.2,0.9,1.5)y=(1.2,0.9,1.5)y=(1.2,0.9,1.5), the Kalman filter produces m3∣3≈1.2m\_{3\mid3}\approx1.2m3∣3​≈1.2, C3∣3≈0.4C\_{3\mid3}\approx0.4C3∣3​≈0.4 and the one-step ahead predictive mean for y4y\_4y4​ is $1.2withvariance with variance withvarianceC\_{3\mid3}+V\approx0.4+1=1.4$.

Marginalizing over parameters: combine Kalman conditionals with posterior over parameters. If unknown variances have conjugate priors (Inverse-Gamma), marginal predictive can be Student-t-like; otherwise sample from p(θ∣y)p(\theta\mid y)p(θ∣y) (via MCMC) and average Kalman predictive densities:

p(yT+1∣y1:T)≈1M∑i=1Mp(yT+1∣y1:T,θ(i)),θ(i)∼p(θ∣y1:T).p(y\_{T+1}\mid y\_{1:T}) \approx \frac{1}{M} \sum\_{i=1}^M p(y\_{T+1}\mid y\_{1:T},\theta^{(i)}),\qquad \theta^{(i)}\sim p(\theta\mid y\_{1:T}).p(yT+1​∣y1:T​)≈M1​i=1∑M​p(yT+1​∣y1:T​,θ(i)),θ(i)∼p(θ∣y1:T​).

This Monte Carlo marginalization is simple and effective: run MCMC for parameters, and for each draw run a Kalman update to compute the conditional predictive, then average or simulate draws.

Tips for practice

- •Always distinguish predictive variance due to observation noise vs parameter uncertainty; report both when you can.
- •Use conjugacy for fast benchmarks and sanity checks; use MCMC/SMC for nonconjugate structural models.

## Core Mechanic 2: Structural Time Series, Parameter Uncertainty, and Bayesian Model Averaging

Structural time series models and their expressiveness

A structural time series specifies interpretable latent components: level, trend, seasonality, regression effects, interventions, and time-varying coefficients. For example, a commonly used local linear trend plus seasonality model for scalar observations is

State vector: xt=[ℓt, bt, st1,…,stS−1]⊤x\_t=[\ell\_t,\, b\_t,\, s\_t^1,\dots,s\_t^{S-1}]^\topxt​=[ℓt​,bt​,st1​,…,stS−1​]⊤ with evolution

ℓt+1=ℓt+bt+ηℓ,t,bt+1=bt+ηb,t,{st+1j} rotate with sum-to-zero constraint+ηs,t.\begin{aligned}
\ell\_{t+1} &= \ell\_t + b\_t + \eta\_{\ell,t},\\
b\_{t+1} &= b\_t + \eta\_{b,t},\\
\{s\_{t+1}^j\} &\text{ rotate with sum-to-zero constraint} + \eta\_{s,t}.
\end{aligned}ℓt+1​bt+1​{st+1j​}​=ℓt​+bt​+ηℓ,t​,=bt​+ηb,t​, rotate with sum-to-zero constraint+ηs,t​.​

Observation: yt=ℓt+st+Ztβ+vty\_t=\ell\_t + s\_t + Z\_t \beta + v\_tyt​=ℓt​+st​+Zt​β+vt​ where ZtβZ\_t\betaZt​β are regression covariates with coefficients β\betaβ. This structure is richer than ARIMA: components have direct interpretation, which is invaluable in business contexts (trend vs seasonal vs promotion lift).

Parameter uncertainty and hierarchical priors

In practice you often have multiple related time series (SKU/store pairs). In Hierarchical Bayesian Models we learned partial pooling — use a hierarchical prior on coefficients βj\beta\_jβj​ or innovation variances to borrow strength. For example, for store-specific promotion effect βi∼N(μβ,τβ2)\beta\_i\sim\mathcal N(\mu\_\beta,\tau\_\beta^2)βi​∼N(μβ​,τβ2​) with hyperpriors on (μβ,τβ)(\mu\_\beta,\tau\_\beta)(μβ​,τβ​). Posterior sharing reduces overfitting for low-data series while allowing high-data series to dominate.

Computational strategies: MCMC, SMC, and particle MCMC

Structural models rarely conjugate fully. Two common approaches:

1) MCMC with forward-filter backward-sample (FFBS): sample parameters θ\thetaθ (e.g., variances, regression coefficients) using Metropolis or Gibbs; conditionally, sample the latent states via the Kalman smoother (or FFBS for linear-Gaussian) to produce draws from p(x1:T∣y1:T,θ)p(x\_{1:T}\mid y\_{1:T},\theta)p(x1:T​∣y1:T​,θ). Each sample yields a draw from the joint posterior; simulate future yT+hy\_{T+h}yT+h​ by forward-propagating the state and adding observation noise.

2) Sequential Monte Carlo / Particle Filters: useful for online updating and non-linear/non-Gaussian models. Particle MCMC (e.g., Particle Gibbs) provides exact (up to Monte Carlo error) draws from the joint posterior.

Numeric sketch: FFBS for DLM

Given parameter draw θ(i)\theta^{(i)}θ(i), run Kalman filter forward to obtain filtering distributions, then run backward sampling to draw x1:T(i)x\_{1:T}^{(i)}x1:T(i)​. Forward-simulate xT+1(i)x\_{T+1}^{(i)}xT+1(i)​ and yT+1(i)y\_{T+1}^{(i)}yT+1(i)​. Repeat across i=1…Mi=1\dots Mi=1…M samples to obtain Monte Carlo predictive draws. Example numbers: 1000 posterior draws produce 1000 predictive draws, from which empirical predictive mean, 90% interval, and predictive quantiles are computed.

Bayesian model averaging (BMA) and model selection

BMA weights models by posterior model probability:

p(yT+h∣y1:T)=∑k=1Kp(yT+h∣Mk,y1:T) p(Mk∣y1:T),p(y\_{T+h}\mid y\_{1:T}) = \sum\_{k=1}^K p(y\_{T+h}\mid M\_k, y\_{1:T})\,p(M\_k\mid y\_{1:T}),p(yT+h​∣y1:T​)=k=1∑K​p(yT+h​∣Mk​,y1:T​)p(Mk​∣y1:T​),

with

p(Mk∣y)=p(y∣Mk)p(Mk)∑jp(y∣Mj)p(Mj),p(y∣Mk)=∫p(y∣θk,Mk)p(θk∣Mk)dθkp(M\_k\mid y)=\frac{p(y\mid M\_k)p(M\_k)}{\sum\_{j} p(y\mid M\_j)p(M\_j)},\qquad p(y\mid M\_k)=\int p(y\mid\theta\_k,M\_k)p(\theta\_k\mid M\_k)d\theta\_kp(Mk​∣y)=∑j​p(y∣Mj​)p(Mj​)p(y∣Mk​)p(Mk​)​,p(y∣Mk​)=∫p(y∣θk​,Mk​)p(θk​∣Mk​)dθk​

The marginal likelihood p(y∣Mk)p(y\mid M\_k)p(y∣Mk​) is often computed by Laplace approximation, bridge sampling, or thermodynamic integration. Numeric example: two models with log marginal likelihoods log⁡p(y∣M1)=−120\log p(y\mid M\_1)=-120logp(y∣M1​)=−120, log⁡p(y∣M2)=−125\log p(y\mid M\_2)=-125logp(y∣M2​)=−125, equal priors p(M1)=p(M2)=0.5p(M\_1)=p(M\_2)=0.5p(M1​)=p(M2​)=0.5. Then posterior odds favor M1M\_1M1​ by factor e5≈148.4e^{5}\approx148.4e5≈148.4, so p(M1∣y)≈0.993p(M\_1\mid y)\approx 0.993p(M1​∣y)≈0.993 and p(M2∣y)≈0.007p(M\_2\mid y)\approx0.007p(M2​∣y)≈0.007.

Model averaging vs selection in forecasting

- •BMA accounts for model uncertainty and often yields better calibrated predictive distributions than selecting a single model.
- •If a single model is strongly dominant (as above), BMA reduces to that model. If models have complementary strengths (e.g., one captures promotions, another long-run trend), BMA blends predictive densities to reduce worst-case risk.

Model stacking (an alternative) optimizes weights to minimize a predictive loss (e.g., log-score) on holdout data rather than using marginal likelihoods; it often improves predictive performance in practice when models are misspecified.

Practical warnings and diagnostics

- •Check calibration (PIT histograms, predictive coverage). A well-calibrated model yields uniform PIT and correct empirical coverage of posterior predictive intervals.
- •Inspect predictive tails. For inventory, tail underestimation is costly.
- •Use predictive scoring rules (log score, CRPS) on holdout sets to compare models and weighting schemes.

## Applications and Connections: Demand Forecasting with Uncertainty Quantification

Demand forecasting is the canonical application where Bayesian forecasting shines: decisions (ordering, pricing, promotions) depend on tails and asymmetric loss. Below I show concrete modeling patterns, loss-based decision rules, and numeric illustrations.

Count data and overdispersion: Poisson-Gamma & Negative Binomial predictive

For counts, start with Poisson likelihood and add hierarchical priors or latent overdispersion. The Gamma-Poisson conjugacy yields a Negative Binomial predictive that captures extra-Poisson variance due to parameter uncertainty.

Numeric worked mini-case: single SKU daily demand

Observations: 30 days with total sales S=150 (mean 5/day). Prior λ∼Gamma(2,1)\lambda\sim\mathrm{Gamma}(2,1)λ∼Gamma(2,1) (shape-rate). Posterior: λ∣y∼Gamma(152,31)\lambda\mid y\sim\mathrm{Gamma}(152,31)λ∣y∼Gamma(152,31), posterior mean $152/31\approx4.903$. One-day predictive is Negative Binomial with mean $152/31\approx4.903$ and variance $4.903+4.903^2/(152)\approx 4.903+0.158\approx5.061$. Compare to plug-in Poisson variance 4.903: the predictive variance is slightly larger.

In-store hierarchy: partial pooling for items/stores

Suppose we have 50 stores and want per-store daily rate λi\lambda\_iλi​. A hierarchical model

λi∼Gamma(α,β),yit∼Pois(λi)\lambda\_i\sim\mathrm{Gamma}(\alpha,\beta),\qquad y\_{it}\sim\mathrm{Pois}(\lambda\_i)λi​∼Gamma(α,β),yit​∼Pois(λi​)

with hyperpriors on (α,β)(\alpha,\beta)(α,β) implements partial pooling. In Hierarchical Bayesian Models we learned how posteriors shrink store estimates toward the chain mean proportionally to information; this reduces forecast variance for low-volume stores.

Promotion and regression effects

Add covariates xitx\_{it}xit​ (price, promotion flag) in a log-linear rate:

log⁡λit=Zitβi+uit,βi∼N(μβ,Σβ)\log\lambda\_{it} = Z\_{it}\beta\_i + u\_{it},\qquad \beta\_i\sim\mathcal N(\mu\_\beta,\Sigma\_\beta)logλit​=Zit​βi​+uit​,βi​∼N(μβ​,Σβ​)

Posterior uncertainty in βi\beta\_iβi​ propagates into predictive uncertainty. To compute predictive uplift under a promotion, simulate posterior draws βi(s)\beta\_i^{(s)}βi(s)​ and produce predictive draws for future periods under different ZitZ\_{it}Zit​ — this yields posterior distributions over promotional lift.

Inventory decision example: Newsvendor loss

If stock level qqq incurs underage cost cuc\_ucu​ per unit sold but not stocked and overage cost coc\_oco​ per leftover unit, the Bayes-optimal quantity minimizes posterior expected loss and corresponds to the posterior predictive quantile:

q∗=F−1(cucu+co),F is the CDF of yT+1∣y1:T.q^\* = F^{-1}\left(\frac{c\_u}{c\_u+c\_o}\right),\qquad F\text{ is the CDF of }y\_{T+1}\mid y\_{1:T}.q∗=F−1(cu​+co​cu​​),F is the CDF of yT+1​∣y1:T​.

Numeric example: if stockout cost cu=10c\_u=10cu​=10, leftover cost co=2c\_o=2co​=2, optimal service quantile is $10/(10+2)=0.8333.IftheposteriorpredictivenegativebinomialCDFevaluatedat. If the posterior predictive negative binomial CDF evaluated at .IftheposteriorpredictivenegativebinomialCDFevaluatedatq=9is0.81andat is 0.81 and at is0.81andatq=10is0.87,choose is 0.87, choose is0.87,chooseq^\*=10$.

Assessing and communicating uncertainty

- •Report predictive mean, median, and multiple quantiles (e.g., 5%, 50%, 95%). For demand planning, also report expected stockouts given a replenishment policy and the tail probability beyond a large threshold.
- •Use probabilistic forecasts in downstream stochastic optimization (e.g., stochastic inventory, dynamic pricing) rather than plugging in point forecasts.

Scaling considerations

- •For many similar series, exploit hierarchical structure and amortized inference (e.g., variational Bayes, amortized MCMC) to scale.
- •Use model selection/stacking to combine cheap parametric models with expensive simulation-based models; stack weights are fit to maximize predictive performance on held-out recent windows.

Summary of applied recipe

1) Specify structural components you believe matter (trend, seasonality, covariates).

2) Choose priors that express domain knowledge; use hierarchical priors for pools of series.

3) Fit via MCMC/SMC/variational methods; validate predictive calibration on holdout data (coverage, PIT).

4) Use posterior predictive draws for decision tasks (newsvendor quantiles, expected costs, promotion uplift distributions).

This pipeline turns time-series forecasting into a decision-ready probabilistic system that explicitly balances bias-variance and model uncertainty.

## Worked Examples (3)

### Gamma-Poisson Posterior Predictive (Simple Demand)

You observe daily sales for an SKU over T=10 days with counts y: 6,4,7,3,5,6,8,4,3,4 (sum S=50). Prior for rate λ is Gamma(α=2, β=1) (shape-rate). Compute the posterior for λ and the predictive probability of seeing k=7 units tomorrow.

1. Compute sufficient statistic: S = sum y\_t = 50, T = 10.
2. Posterior shape = α\_post = α + S = 2 + 50 = 52. Posterior rate = β\_post = β + T = 1 + 10 = 11. Therefore λ | y ∼ Gamma(52,11).
3. The posterior predictive for y\_{T+1} is the Gamma-Poisson (Negative Binomial) mixture: for k≥0,

   p(y\_{T+1}=k|y)= {Γ(α\_post+k)\over k! Γ(α\_post)} (β\_post/(β\_post+1))^{α\_post} (1/(β\_post+1))^{k}.
4. Plug numbers for k=7: compute (β\_post/(β\_post+1))^{α\_post} = (11/12)^{52}. Numerically (11/12)^{52} ≈ exp(52  *ln(11/12)) ≈ exp(52*  -0.087011) ≈ exp(-4.5246) ≈ 0.0108.
5. Compute the combinatorial prefactor: Γ(52+7)/(7! Γ(52)) = (52·53·...·58)/7! (Gamma ratio). Compute numerator product: 52*53*54*55*56*57*58 ≈ (use calculator) ≈ 1.366×10^{12}. 7! = 5040. Ratio ≈ 2.71×10^{8}. Then multiply by (1/12)^7 ≈ 1/(35,831,808) ≈ 2.79×10^{-8}. Multiply: 2.71×10^{8}  *0.0108*  2.79×10^{-8} ≈ (2.71×10^{8}  *2.79×10^{-8})*  0.0108 ≈ 7.56 \* 0.0108 ≈ 0.0817 (approx).
6. Thus the posterior predictive probability of observing exactly 7 units tomorrow is approximately 0.082. The predictive mean is α\_post/β\_post = 52/11 ≈ 4.727, which matches the empirical mean 5 initially but shrinks due to prior.

**Insight:** This example shows how conjugacy yields closed-form posterior and predictive distributions; the predictive variance exceeds the Poisson variance due to uncertainty in λ.

### Kalman-Based Predictive with Unknown Noise Variance

Local level model x\_{t+1}=x\_t+η\_t, y\_t=x\_t+ε\_t with η\_t∼N(0,σ\_w^2), ε\_t∼N(0,σ\_v^2). Prior x\_0∼N(0,1). Observed y: 1.2, 0.9, 1.5 (T=3). Assume σ\_w^2=0.5 known, but σ\_v^2 unknown with prior Inverse-Gamma(α=3, β=2). Compute the one-step-ahead predictive distribution for y\_4 marginalizing σ\_v^2 approximately using conjugacy (Student-t predictive), and give predictive mean and variance numerically (approx).

1. Run Kalman filter treating σ\_v^2 as symbolic to get filtering mean m\_3 and variance C\_3. With initial prior m\_0=0, C\_0=1, known σ\_w^2=0.5: after 3 observations the filter gives m\_3≈1.2 and C\_3≈0.4 (these are approximate from standard recursion).
2. Conditional on σ\_v^2, the one-step predictive for y\_4 is Normal with mean m\_3 and variance C\_3+σ\_v^2: y\_4|σ\_v^2,y ∼ N(m\_3, C\_3+σ\_v^2).
3. Use conjugacy: prior for σ\_v^2 is Inv-Gamma(α,β). The marginal predictive integrating σ\_v^2 yields a Student-t with 2α degrees of freedom, location m\_3, and scale depending on β and C\_3. Specifically,

   y\_4|y ∼ t\_{2α}\left(m\_3,\frac{β(1+C\_3)}{α}\right).
4. Plug numbers: α=3, β=2, m\_3≈1.2, C\_3≈0.4. Degrees of freedom = 6. Scale variance = β(1+C\_3)/α = 2*(1+0.4)/3 = 2*1.4/3 = 2.8/3 ≈ 0.9333. So predictive is t\_6(1.2, variance≈0.9333).
5. Predictive mean equals m\_3=1.2 (for df>1). Predictive variance for Student-t = scale  *df/(df-2) = 0.9333*  6/4 = 0.9333 \* 1.5 = 1.4. So predictive std ≈ 1.183. This matches intuition: predictive variance equals C\_3 plus posterior mean of σ\_v^2 and extra df inflation.

**Insight:** This example demonstrates how combining Kalman conditioning on latent state with conjugate priors on noise variance yields a Student-t posterior predictive that accounts for parameter uncertainty analytically.

### Bayesian Model Averaging for Two Competing Forecast Models

Two competing models M1 and M2 are fit to the same time series. Log marginal likelihoods are: log p(y|M1) = -120, log p(y|M2) = -125. Prior model probabilities equal. Compute posterior model probabilities, then compute the BMA one-step predictive as weighted average of the models' predictive densities. Suppose model predictive means are μ1=10 (variance 4) and μ2=12 (variance 9); compute BMA predictive mean and approximate variance assuming independence conditional on model choice.

1. Compute Bayes factors: log BF\_{1,2} = -120 - (-125) = 5. So BF\_{1,2} = e^{5} ≈ 148.413.
2. With equal priors, posterior probability p(M1|y) = BF\_{1,2} / (1 + BF\_{1,2}) = 148.413 / 149.413 ≈ 0.9933. p(M2|y) ≈ 0.0067.
3. BMA predictive mean = p(M1|y) μ1 + p(M2|y) μ2 = 0.9933*10 + 0.0067*12 = 9.933 + 0.0804 = 10.0134 ≈ 10.01.
4. To approximate predictive variance, use law of total variance: Var(Y) = E[Var(Y|M)] + Var(E[Y|M]). Compute E[Var]=0.9933*4 + 0.0067*9 = 3.9732 + 0.0603 = 4.0335.
5. Compute Var(E[Y|M]) = 0.9933*(10-10.0134)^2 + 0.0067*(12-10.0134)^2 ≈ 0.9933*(0.00018) + 0.0067*(3.944) ≈ 0.00018 + 0.0264 ≈ 0.0266. Total variance ≈ 4.0335 + 0.0266 ≈ 4.0601. Predictive std ≈ 2.015.
6. Thus BMA predictive mean ≈10.01 and variance ≈4.06, nearly the M1 forecast but with tiny additional variance from model uncertainty.

**Insight:** BMA can heavily weight a dominant model but still formally account for model uncertainty; when marginal likelihoods are close, BMA yields meaningful mixtures and often better calibration.

## Key Takeaways

- ✓

  The posterior predictive p(y\_{T+h}|y\_{1:T}) is the decision-oriented object: always integrate over both parameter and latent-state uncertainty before making decisions.
- ✓

  Conjugate models (Gamma-Poisson, Normal-Inverse-Gamma) yield closed-form predictive distributions (Negative Binomial, Student-t) that transparently reflect parameter uncertainty; always compute these for sanity checks.
- ✓

  For linear Gaussian state-space models, Kalman filter gives conditional predictive distributions; marginalize parameters by Monte Carlo (draw θ, run Kalman) or analytically when conjugate priors exist.
- ✓

  Structural time series with interpretable components (trend, seasonality, regression effects) are especially useful in business forecasting and should be combined with hierarchical priors for many related series.
- ✓

  Bayesian model averaging uses marginal likelihoods to weight models and produces better-calibrated predictive distributions than selecting a single model in the presence of model uncertainty; stacking is a pragmatic alternative optimizing predictive scores.
- ✓

  Use posterior predictive draws for decision problems (newsvendor quantiles, expected stockouts, stochastic optimization); the optimal action is often a quantile of the predictive.
- ✓

  Calibration checks (PIT, predictive coverage, scoring rules like log score and CRPS) are essential to validate probabilistic forecasts.

## Common Mistakes

- ✗

  Plug-in forecasting: using point estimates of parameters (e.g., MLE or posterior mean) and ignoring parameter uncertainty — this typically underestimates predictive variance and leads to overconfident decisions.
- ✗

  Misinterpreting posterior predictive samples as independent when they are correlated via shared parameter draws — when computing effective quantiles or intervals, use the empirical distribution of independent predictive draws (one per posterior sample) rather than naive bootstrap of conditional draws.
- ✗

  Using marginal likelihoods without checking sensitivity to priors — marginal likelihoods can be strongly influenced by diffuse priors; prefer predictive scoring on holdout data or use robust priors when computing BMA weights.
- ✗

  Confusing observation overdispersion with time-varying mean — model choice between a Negative Binomial (overdispersion) and a structural state evolution (latent dynamics) should be guided by residual diagnostics and PIT plots.

## Practice

easy

Easy — Conjugate Poisson-Gamma predictive: You observe T=5 days with counts 2,3,1,4,2 (S=12). Prior for λ is Gamma(α=1.5, β=0.5). Compute the posterior for λ and the posterior predictive mean and variance for next-day demand.

**Hint:** Posterior shape = α+S, rate = β+T; predictive mean = (α+S)/(β+T), predictive variance = mean + mean^2/(α+S).

Show solution

S=12, posterior shape = 1.5+12=13.5, posterior rate = 0.5+5=5.5. Predictive mean = 13.5/5.5 ≈ 2.4545. Predictive variance = mean + mean^2/(13.5) ≈ 2.4545 + (6.024)/(13.5) ≈ 2.4545 + 0.446 ≈ 2.9005.

medium

Medium — Kalman predictive with parameter draws: Consider a scalar local level model with unknown observation variance σ\_v^2 and known state noise σ\_w^2=0.2. You have posterior samples for σ\_v^2: {0.5, 1.0, 1.5}. For each σ\_v^2 sample, the Kalman one-step conditional predictive variance after filtering is C\_3+σ\_v^2 where C\_3=0.3 and predictive mean m\_3=2.0. Compute the Monte Carlo approximation to the marginal predictive mean and variance using these three parameter draws (equal weights).

**Hint:** Average the conditional predictive means (all equal) for marginal mean; use law of total variance for marginal variance: E[Var]+Var(E[·|σ]).

Show solution

Conditional predictive means are all 2.0, so marginal mean = 2.0. Conditional variances are 0.3+0.5=0.8, 0.3+1.0=1.3, 0.3+1.5=1.8. E[Var]=mean of these = (0.8+1.3+1.8)/3=3.9/3=1.3. Var(E[·|σ])=Var(2.0,2.0,2.0)=0. Total marginal variance = 1.3. So predictive mean 2.0 and variance 1.3.

hard

Hard — Hierarchical count forecasting with partial pooling: You have counts for two stores over 4 days each: store A: 10,12,9,11 (sum S\_A=42), store B: 1,0,2,1 (sum S\_B=4). Model y\_{it}∼Pois(λ\_i) and λ\_i∼Gamma(α,β) with hyperprior α=2 fixed, but unknown β with prior p(β)∝1/β (improper Jeffreys). Derive the joint posterior up to proportionality for (λ\_A,λ\_B,β) and describe how you would compute posterior predictive for day 5 for both stores using MCMC. (You are not required to run code, but show formulas and sampling scheme.)

**Hint:** Write likelihoods for each store and the hierarchical prior; marginal posterior for β can be targeted with MCMC; conditional posteriors for λ\_i given β are Gamma (due to conjugacy).

Show solution

Likelihood: p(y|λ)=Π\_i Π\_t e^{-λ\_i}λ\_i^{y\_{it}}/y\_{it}! ∝ Π\_i λ\_i^{S\_i} e^{-T λ\_i}. Prior: p(λ\_i|β)=β^{α}/Γ(α) λ\_i^{α-1} e^{-β λ\_i}. Joint posterior (up to constant):

p(λ\_A,λ\_B,β|y) ∝ p(β) Π\_i [λ\_i^{S\_i} e^{-T λ\_i} λ\_i^{α-1} e^{-β λ\_i}] = (1/β) Π\_i λ\_i^{S\_i+α-1} e^{-(T+β)λ\_i}.

So conditional λ\_i | β,y ∼ Gamma(shape = S\_i+α, rate = T+β). For our numbers: T=4, α=2 gives λ\_A|β ∼ Gamma(42+2=44, 4+β), λ\_B|β ∼ Gamma(4+2=6,4+β).

The marginal posterior for β (up to constant) after integrating out λ\_i is:

p(β|y) ∝ (1/β) Π\_i [Γ(S\_i+α)/( (T+β)^{S\_i+α} )].

Explicitly: p(β|y) ∝ (1/β) (1/(4+β)^{44})(1/(4+β)^{6}) = (1/β)/(4+β)^{50}, up to multiplicative constants from Γ() which are constant in β. So p(β|y) ∝ β^{-1}(4+β)^{-50}. Sample β via Metropolis-Hastings or slice sampling on β>0.

Gibbs-within-MH scheme:

1) Given current β, sample λ\_A ∼ Gamma(44,4+β), λ\_B ∼ Gamma(6,4+β).

2) Update β with Metropolis-Hastings proposing β' (e.g., log-normal random walk) targeting p(β|y) ∝ β^{-1}(4+β)^{-50}.

Posterior predictive for day 5 for store i: simulate λ\_i^{(s)} from posterior draws and then simulate y\_{i,5}^{(s)} ∼ Poisson(λ\_i^{(s)}) to get predictive samples. From these, compute predictive mean and credible intervals.

## Connections

Looking back: This lesson builds directly on the prerequisites. From State-Space Models we used the Kalman filter and smoothing for conditional latent-state inference and built predictive formulas for linear-Gaussian models; the FFBS sampler and forward propagation are direct descendants of those algorithms. From Hierarchical Bayesian Models we used partial pooling to borrow strength across series via hierarchical priors on rates or regression coefficients. From Conjugate Priors we exploited Gamma-Poisson and Normal-Inverse-Gamma conjugacy to derive closed-form posterior predictives (Negative Binomial and Student-t), which serve as both computational shortcuts and diagnostic checks. Looking forward: mastering Bayesian forecasting enables rigorous downstream tasks — stochastic inventory optimization (newsvendor and multi-period ordering), Bayesian decision analysis for promotions and pricing, probabilistic supply chain simulation, causal impact evaluation with state-space counterfactuals, and automated model combination (stacking) pipelines in production. Specific downstream methods that rely on these techniques include probabilistic machine learning methods for hierarchical time series (forecast reconciliation with Bayesian priors), sequential decision making under uncertainty (POMDPs), and Bayesian experimental design for pricing or promotion trials where posterior predictive simulations guide sample-size planning. Practical deployment often requires combining these inferential foundations with computational tools: particle filtering for online updates, variational inference or amortized MCMC for scaling to thousands of series, and robust predictive scoring and calibration routines for continual monitoring.

Quality: pending (0.0/5)

[← back to tree](/tech-tree/)[browse all →](/tech-tree/inventory/)
