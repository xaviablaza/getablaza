---
title: Hierarchical Bayesian Models
description: Partial pooling, hyperpriors, shrinkage estimators. Multilevel regression. Empirical Bayes as approximation. Store-level vs chain-level parameter sharing.
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
permalink: /tech-tree/hierarchical-models/
---

[←Back to Tech Tree](/tech-tree/)

[inventory](/tech-tree/inventory/)[coverage](/tech-tree/coverage/)

# Hierarchical Bayesian Models

Probability & StatisticsDifficulty: ★★★★★Depth: 9Unlocks: 2

Partial pooling, hyperpriors, shrinkage estimators. Multilevel regression. Empirical Bayes as approximation. Store-level vs chain-level parameter sharing.

## Prerequisites (2)

[Conjugate Priors? atoms](/tech-tree/conjugate-priors/)[MCMC6 atoms](/tech-tree/mcmc/)

## Unlocks (1)

[Bayesian Forecastinglvl 5](/tech-tree/bayesian-forecasting/)

## Referenced by (3)

Where this concept shows up in the operating-finance and personal-finance graphs.

### From Business (3)

[Conjoint AnalysisBusiness

Hierarchical Bayesian estimation (HB-CBC) is the modern standard for conjoint, using partial pooling across respondents to estimate individual-level part-worths from sparse per-person choice data](/business/conjoint-analysis/)[private equityBusiness

Production AI across a PE portfolio is literally hierarchical Bayesian modeling - partial pooling of operational patterns across portfolio companies with company-specific parameters. Quality systems that share infrastructure while adapting to each company's context use the same math as store-level vs chain-level parameter sharing.](/business/private-equity/)[PE Portfolio OperationsBusiness

PE firms with multiple portfolio companies use partial pooling for KPI benchmarking - the store-level vs chain-level parameter sharing maps directly to portco-level vs platform-level performance analysis](/business/pe-portfolio-operations/)

Advanced Learning Details

### Graph Position

142

Depth Cost

2

Fan-Out (ROI)

1

Bottleneck Score

9

Chain Length

When you have many related groups with small per-group data (stores, hospitals, classrooms), hierarchical Bayesian models give you principled 'partial pooling' that improves estimates and quantifies uncertainty—without forcing all groups to be identical.

TL;DR:

Hierarchical Bayesian models place priors on group-level parameters (hyperpriors) to achieve partial pooling and shrinkage; empirical Bayes offers a fast approximation by estimating hyperparameters from the marginal likelihood.

## What Is Hierarchical Bayesian Modeling?

Definition and motivation

A hierarchical Bayesian model (also called a multilevel model) is a probabilistic model in which parameters themselves have probability distributions whose parameters (hyperparameters) are also given distributions. Hierarchical structure encodes the idea of exchangeability and partial pooling: groups are similar but not identical. Rather than estimating each group's parameter independently (no pooling) or assuming all groups share a single parameter (complete pooling), hierarchical models let the data determine how much information to borrow across groups.

Why care: partial pooling reduces estimation variance while controlling bias. Consider stores estimating conversion rates: a tiny store with 2 purchases in 20 visits would have an unreliable raw estimate 0.10. A hierarchical model borrows strength from the chain-level distribution to pull (shrink) that estimate toward the chain mean, often giving dramatically better predictive performance.

Core formalism (two-level example)

The canonical two-level hierarchical model for group-specific parameters θj\theta\_jθj​ and observations yjiy\_{ji}yji​ is:

θj∼p(θj∣ϕ)(group-level, exchangeable),yji∼p(yji∣θj,ψ)(observation-level),ϕ∼p(ϕ)(hyperprior),ψ∼p(ψ)((optional) observation-level hyperparameters).\begin{aligned}
\theta\_j &\sim p(\theta\_j\mid\phi) \quad(\text{group-level, exchangeable}),\\
y\_{ji} &\sim p(y\_{ji}\mid\theta\_j, \psi) \quad(\text{observation-level}),\\
\phi &\sim p(\phi) \quad(\text{hyperprior}),\\
\psi &\sim p(\psi) \quad(\text{(optional) observation-level hyperparameters}).
\end{aligned}θj​yji​ϕψ​∼p(θj​∣ϕ)(group-level, exchangeable),∼p(yji​∣θj​,ψ)(observation-level),∼p(ϕ)(hyperprior),∼p(ψ)((optional) observation-level hyperparameters).​

Here j=1,…,Jj=1,\dots,Jj=1,…,J indexes groups (stores), i=1,…,nji=1,\dots,n\_ji=1,…,nj​ indexes observations in group jjj. Exchangeability across groups means that, before seeing data, group labels don't matter and we treat θ1,…,θJ\theta\_1,\dots,\theta\_Jθ1​,…,θJ​ as iid from p(θ∣ϕ)p(\theta\mid\phi)p(θ∣ϕ).

Concrete numeric toy: Beta-Binomial intuition

If each store has conversion counts yj∼Binomial(nj,θj)y\_j\sim\text{Binomial}(n\_j, \theta\_j)yj​∼Binomial(nj​,θj​) and we place θj∼Beta(α,β)\theta\_j\sim\text{Beta}(\alpha,\beta)θj​∼Beta(α,β) with hyperparameters (α,β)(\alpha,\beta)(α,β), then posterior inference for each θj\theta\_jθj​ is conjugate:

θj∣yj,α,β∼Beta(α+yj, β+nj−yj).\theta\_j\mid y\_j,\alpha,\beta\sim\text{Beta}(\alpha+y\_j,\,\beta+n\_j-y\_j).θj​∣yj​,α,β∼Beta(α+yj​,β+nj​−yj​).

Numeric example: a small store had y=2y=2y=2 successes in n=20n=20n=20 visits. If chain-level hyperparameters are α=5,β=95\alpha=5,\beta=95α=5,β=95 (prior mean 0.05, variance small), the posterior mean is

E[θ∣y]=α+yα+β+n=5+25+95+20=7120≈0.0583,E[\theta\mid y]=\frac{\alpha+y}{\alpha+\beta+n} =\frac{5+2}{5+95+20}=\frac{7}{120}\approx0.0583,E[θ∣y]=α+β+nα+y​=5+95+205+2​=1207​≈0.0583,

which is shrunk toward 0.05 from the raw rate $2/20=0.10$.

Contrast with complete pooling: estimating a single θ\thetaθ for all stores would ignore between-store variability; no pooling would give θ^j=yj/nj\hat{\theta}\_j=y\_j/n\_jθ^j​=yj​/nj​ with high variance for small njn\_jnj​. The hierarchical model, by introducing hyperparameters and a hyperprior, adapts the amount of pooling to the data.

Philosophy and exchangeability

In [Conjugate Priors] we learned how conjugacy gives closed-form posteriors for single-level models like Beta-Binomial and Normal-Normal. Hierarchical models extend this: conjugacy may allow analytic conditional posteriors for lower-level parameters given hyperparameters. But typically we integrate over hyperparameters (or sample them in MCMC) to get full posterior uncertainty.

Exchangeability justifies the iid assumption on θj∣ϕ\theta\_j\mid\phiθj​∣ϕ: if groups are exchangeable, the joint prior over θ1:J\theta\_{1:J}θ1:J​ factorizes into iid draws from the same mixture. Partial pooling is the Bayesian implementation of the bias-variance tradeoff: the posterior for each θj\theta\_jθj​ is shrunk toward the common prior mean, with the extent of shrinkage determined by the relative sizes of within-group noise and between-group variability.

Key quantities to watch: the hyperparameters (e.g. variance of θj\theta\_jθj​ across groups) control shrinkage; the posterior predictive distribution integrates over both θj\theta\_jθj​ and ϕ\phiϕ and is what you use for predicting new observations or new groups.

Summary sentence

Hierarchical Bayesian models let you model group heterogeneity while borrowing strength across groups via hyperpriors; this produces principled shrinkage estimators that often dominate non-hierarchical alternatives in prediction and mean squared error.

## Core Mechanic 1: Conjugate Hierarchies, Partial Pooling, and Analytic Shrinkage

Normal-Normal hierarchical model (canonical analytic case)

A central worked analytic case is the Normal-Normal hierarchical model with known observation variance. This is where the familiar shrinkage formula arises in closed form and links directly to [Conjugate Priors]. Model:

θj∼N(μ,τ2)(j=1,…,J),yj i∼N(θj,σ2),i=1,…,nj.\begin{aligned}
\theta\_j &\sim N(\mu,\tau^2) \quad(j=1,\dots,J),\\
y\_{j\,i} &\sim N(\theta\_j,\sigma^2), \quad i=1,\dots,n\_j.
\end{aligned}θj​yji​​∼N(μ,τ2)(j=1,…,J),∼N(θj​,σ2),i=1,…,nj​.​

Let yˉj=1nj∑i=1njyj,i\bar y\_j=\frac{1}{n\_j}\sum\_{i=1}^{n\_j} y\_{j,i}yˉ​j​=nj​1​∑i=1nj​​yj,i​ be the group mean and σ2/nj\sigma^2/n\_jσ2/nj​ its sampling variance. Conditional on hyperparameters (μ,τ2)(\mu,\tau^2)(μ,τ2) the posterior for θj\theta\_jθj​ is Gaussian (by conjugacy):

θj∣yˉj,μ,τ2∼N(wjyˉj+(1−wj)μ,  11/τ2+nj/σ2),\theta\_j\mid\bar y\_j,\mu,\tau^2 \sim N\left( w\_j\bar y\_j + (1-w\_j)\mu, \;\frac{1}{1/\tau^2 + n\_j/\sigma^2} \right),θj​∣yˉ​j​,μ,τ2∼N(wj​yˉ​j​+(1−wj​)μ,1/τ2+nj​/σ21​),

where the shrinkage weight is

wj=nj/σ2nj/σ2+1/τ2=τ2τ2+σ2/nj−1?w\_j = \frac{n\_j/\sigma^2}{n\_j/\sigma^2 + 1/\tau^2} = \frac{\tau^2}{\tau^2 + \sigma^2/n\_j}^{-1}?wj​=nj​/σ2+1/τ2nj​/σ2​=τ2+σ2/nj​τ2​−1?

(We prefer the intuitively clearer form below.) Solving algebra shows the posterior mean can be written as:

E[θj∣yˉj,μ,τ2]=(1−κj)μ+κjyˉj,κj=njτ2njτ2+σ2.E[\theta\_j\mid\bar y\_j,\mu,\tau^2] = (1-\kappa\_j)\mu + \kappa\_j\bar y\_j, \quad \kappa\_j = \frac{n\_j\tau^2}{n\_j\tau^2 + \sigma^2}.E[θj​∣yˉ​j​,μ,τ2]=(1−κj​)μ+κj​yˉ​j​,κj​=nj​τ2+σ2nj​τ2​.

This κj∈(0,1)\kappa\_j\in(0,1)κj​∈(0,1) is the effective weight on the data vs the group mean. When nj→∞n\_j\to\inftynj​→∞, κj→1\kappa\_j\to1κj​→1 and we rely on the data; when τ2→0\tau^2\to0τ2→0 (no between-group variability) κj→0\kappa\_j\to0κj​→0 and every group collapses to the common mean μ\muμ (complete pooling).

Concrete numeric example (normal-normal)

Suppose σ2=4\sigma^2=4σ2=4 (observation SD =2=2=2), τ2=1\tau^2=1τ2=1 (between-group SD =1=1=1), nj=5n\_j=5nj​=5 observations in group jjj, and group sample mean yˉj=10\bar y\_j=10yˉ​j​=10, hyper-mean μ=8\mu=8μ=8. Then

κj=5⋅15⋅1+4=59≈0.5556,\kappa\_j = \frac{5\cdot 1}{5\cdot 1 + 4} = \frac{5}{9} \approx 0.5556,κj​=5⋅1+45⋅1​=95​≈0.5556,

so posterior mean is

E[θj∣yˉj]=(1−0.5556)⋅8+0.5556⋅10=0.4444⋅8+0.5556⋅10=9.1111.E[\theta\_j\mid\bar y\_j]= (1-0.5556)\cdot 8 + 0.5556\cdot 10 = 0.4444\cdot 8 + 0.5556\cdot 10 = 9.1111.E[θj​∣yˉ​j​]=(1−0.5556)⋅8+0.5556⋅10=0.4444⋅8+0.5556⋅10=9.1111.

Compare: raw mean 10, pooled mean 8, shrunk estimate 9.11.

Derivation sketch

Conditional posterior precision = prior precision + data precision. Prior precision =1/τ2=1/\tau^2=1/τ2, data precision =nj/σ2=n\_j/\sigma^2=nj​/σ2. Thus posterior mean is a precision-weighted average:

E[θj∣⋅]=(1/τ2)μ+(nj/σ2)yˉj1/τ2+nj/σ2=(1−κj)μ+κjyˉj.E[\theta\_j\mid\cdot] = \frac{(1/\tau^2)\mu + (n\_j/\sigma^2)\bar y\_j}{1/\tau^2 + n\_j/\sigma^2} = (1-\kappa\_j)\mu + \kappa\_j\bar y\_j.E[θj​∣⋅]=1/τ2+nj​/σ2(1/τ2)μ+(nj​/σ2)yˉ​j​​=(1−κj​)μ+κj​yˉ​j​.

This is the canonical "shrinkage" formula. In [Conjugate Priors] you saw the Normal-Normal conjugacy; here it extends across groups with a hyperprior on μ\muμ and τ2\tau^2τ2 if desired.

James–Stein connection (brief, illuminating)

The James–Stein estimator is a (frequentist) shrinkage estimator for multivariate normal means that dominates the MLE in mean squared error for dimension ≥3\ge 3≥3. Hierarchical Bayes with an appropriate hyperprior produces shrinkage estimators with similar behavior. A heuristic connection: empirical Bayes or hierarchical Bayes produces estimators that shrink toward a common mean; in large-dimension limits the Bayes estimator approximates a form of James–Stein shrinkage.

Empirical Bayes (ML-II) approximation

If μ\muμ and τ2\tau^2τ2 are unknown, one approach is empirical Bayes: estimate them by maximizing the marginal likelihood of the observed yˉj\bar y\_jyˉ​j​'s. Marginally,

yˉj∼N(μ,τ2+σ2/nj).\bar y\_j\sim N(\mu,\tau^2 + \sigma^2/n\_j).yˉ​j​∼N(μ,τ2+σ2/nj​).

So we can compute the (log) marginal likelihood and obtain MLEs μ^,τ^2\hat\mu,\hat\tau^2μ^​,τ^2; plug them into the posterior mean formula above to get an empirical Bayes point estimate for each θj\theta\_jθj​. This ML-II step is often fast and connects to [MCMC] because you can use these estimates to initialize or inform MCMC priors.

Numeric example of empirical Bayes (method of moments)

Given JJJ observed yˉj\bar y\_jyˉ​j​ with known σ2\sigma^2σ2 and njn\_jnj​, method-of-moments estimates give

μ^=∑jwjyˉj∑jwj,with wj=1/(σ2/nj).\hat\mu = \frac{\sum\_j w\_j \bar y\_j}{\sum\_j w\_j}, \quad \text{with } w\_j = 1/(\sigma^2/n\_j).μ^​=∑j​wj​∑j​wj​yˉ​j​​,with wj​=1/(σ2/nj​).

Then estimate between-group variance via

τ2^=max⁡(0,  1J−1∑j(yˉj−μ^)2−1J∑jσ2nj).\widehat{\tau^2} = \max\left(0, \;\frac{1}{J-1}\sum\_j (\bar y\_j-\hat\mu)^2 - \frac{1}{J}\sum\_j\frac{\sigma^2}{n\_j}\right).τ2=max(0,J−11​j∑​(yˉ​j​−μ^​)2−J1​j∑​nj​σ2​).

Concrete numbers: if we have three groups with yˉ=(9,11,10)\bar y=(9,11,10)yˉ​=(9,11,10), nj=5n\_j=5nj​=5 each, σ2=4\sigma^2=4σ2=4, then sample variance of yˉ\bar yyˉ​ is $1;averagesamplingvarianceis; average sampling variance is ;averagesamplingvarianceis\sigma^2/n\_j=0.8,somethod−of−momentsgives, so method-of-moments gives ,somethod−of−momentsgives\hat\tau^2=\max(0,1-0.8)=0.2$.

Summary

This section gave the analytic backbone: conjugate normal-normal hierarchies yield explicit shrinkage weights κj\kappa\_jκj​; empirical Bayes estimates hyperparameters by marginalizing the lower-level parameters, producing fast approximate shrinkage estimators. In practice, for nonconjugate or complex multilevel regressions we use MCMC (see [MCMC]) with either centered or non-centered parameterizations to ensure efficient sampling.

## Core Mechanic 2: Multilevel Regression, Non-centered Parametrization, and Hyperpriors

Multilevel regression: varying intercepts and slopes

Hierarchical modeling becomes especially powerful when combined with regression: we let intercepts and slopes vary by group. A simple varying-intercept, varying-slope model for outcome yijy\_{ij}yij​ with predictor vector xijx\_{ij}xij​ is:

yij∼N(αj+xijTβj, σ2),(αjβj)∼N((μαμβ),  Σgroup),\begin{aligned}
y\_{ij} &\sim N(\alpha\_j + x\_{ij}^T\beta\_j,\,\sigma^2),\\[4pt]
\begin{pmatrix}\alpha\_j \\\beta\_j\end{pmatrix} &\sim N\left( \begin{pmatrix}\mu\_{\alpha} \\\mu\_{\beta}\end{pmatrix},\; \Sigma\_{\mathrm{group}} \right),
\end{aligned}yij​(αj​βj​​)​∼N(αj​+xijT​βj​,σ2),∼N((μα​μβ​​),Σgroup​),​

where αj\alpha\_jαj​ is group-specific intercept, βj\beta\_jβj​ group-specific slope vector, and Σgroup\Sigma\_{\mathrm{group}}Σgroup​ is a covariance matrix encoding how intercepts and slopes vary and covary across groups. This fully multilevel regression allows partial pooling in both intercepts and slopes and allows complex cross-group shrinkage: groups with scarce data will have their αj\alpha\_jαj​ and βj\beta\_jβj​ pulled toward population means (μα,μβ)(\mu\_\alpha,\mu\_\beta)(μα​,μβ​).

Priors on covariance matrices: separation strategy and LKJ

Priors on Σgroup\Sigma\_{\mathrm{group}}Σgroup​ are critical. A common strategy (the "separation" prior) decomposes

Σgroup=diag(τ) R diag(τ),\Sigma\_{\mathrm{group}} = \mathrm{diag}(\tau)\,R\,\mathrm{diag}(\tau),Σgroup​=diag(τ)Rdiag(τ),

where τ\tauτ is the vector of standard deviations for each random effect and RRR a correlation matrix. Priors: put half-Cauchy or half-normal priors on components of τ\tauτ (weakly informative), and an LKJ prior on RRR (Lewandowski–Kurowicka–Joe) with concentration parameter η\etaη favoring identity when η>1\eta>1η>1. Example numeric choices: τk∼HalfCauchy(0,2)\tau\_k \sim \mathrm{HalfCauchy}(0,2)τk​∼HalfCauchy(0,2), R∼LKJ(η=2)R\sim\mathrm{LKJ}(\eta=2)R∼LKJ(η=2).

Centered vs non-centered parameterizations (important for MCMC efficiency)

In [MCMC] we learned that parameterization affects convergence and mixing. For hierarchical models, two common parameterizations are:

- •Centered: directly model θj∼N(μ,τ2)\theta\_j\sim N(\mu,\tau^2)θj​∼N(μ,τ2) and sample θj\theta\_jθj​.
- •Non-centered: reparametrize θj=μ+τ ηj\theta\_j = \mu + \tau\,\eta\_jθj​=μ+τηj​, with ηj∼N(0,1)\eta\_j\sim N(0,1)ηj​∼N(0,1).

Why it matters: when group-level variance τ\tauτ is small and data are informative, centered parameterization mixes well; when τ\tauτ is large and/or data per group are small, non-centered often mixes much better. A practical rule: try both or use adaptive diagnostics. Concrete numeric illustration: if τ=0.01\tau=0.01τ=0.01 and data are abundant, centered is fine; if τ=5\tau=5τ=5 and njn\_jnj​ small, non-centered reduces funnel-shaped posterior geometry and avoids slow MCMC.

Posterior predictive checks and partial pooling

The full Bayesian workflow uses posterior predictive distributions to judge fit and to predict. For a given group jjj the posterior predictive for a new observation yj newy\_{j\,\text{new}}yjnew​ is

p(yj new∣data)=∬p(yj new∣θj,ψ) p(θj∣ϕ,data) p(ϕ∣data) dθj dϕ.p(y\_{j\,\text{new}}\mid\text{data}) = \iint p(y\_{j\,\text{new}}\mid\theta\_j,\psi)\,p(\theta\_j\mid\phi,\text{data})\,p(\phi\mid\text{data})\,d\theta\_j\,d\phi.p(yjnew​∣data)=∬p(yjnew​∣θj​,ψ)p(θj​∣ϕ,data)p(ϕ∣data)dθj​dϕ.

In practice we approximate this by MCMC draws: for each draw of ϕ\phiϕ and θj\theta\_jθj​ simulate ynewy\_{\text{new}}ynew​. Posterior predictive checks diagnose over/under-pooling: if pooled model systematically mispredicts heterogeneity, consider richer group-level structure (e.g., allow covariates to explain group differences).

Empirical Bayes vs full Bayes: tradeoffs

In empirical Bayes (ML-II) we estimate hyperparameters ϕ\phiϕ by marginal likelihood and then condition on ϕ^\hat\phiϕ^​. This often gives good point estimates and is fast for large hierarchical problems. However, it underestimates hyperparameter uncertainty: it treats ϕ^\hat\phiϕ^​ as known, which can understate posterior variance for predictions, especially with few groups. Full Bayes places hyperpriors on ϕ\phiϕ and samples it in MCMC, which captures uncertainty but costs more computation.

Numeric demonstration of marginal likelihood (for normal-normal)

Recall marginal of yˉj\bar y\_jyˉ​j​ is yˉj∼N(μ,τ2+σ2/nj)\bar y\_j\sim N(\mu, \tau^2 + \sigma^2/n\_j)yˉ​j​∼N(μ,τ2+σ2/nj​). For known σ2\sigma^2σ2 the log marginal likelihood is

ℓ(μ,τ2)=−12∑j[log⁡(τ2+σ2/nj)+(yˉj−μ)2τ2+σ2/nj]+const.\ell(\mu,\tau^2) = -\frac{1}{2}\sum\_j\left[ \log(\tau^2+\sigma^2/n\_j) + \frac{(\bar y\_j-\mu)^2}{\tau^2+\sigma^2/n\_j} \right] + \text{const}.ℓ(μ,τ2)=−21​j∑​[log(τ2+σ2/nj​)+τ2+σ2/nj​(yˉ​j​−μ)2​]+const.

For example, with J=3J=3J=3, yˉ=(9,11,10)\bar y=(9,11,10)yˉ​=(9,11,10), nj=5n\_j=5nj​=5, σ2=4\sigma^2=4σ2=4, we numerically maximize ℓ\ellℓ over μ,τ2\mu,\tau^2μ,τ2 to get empirical Bayes estimates used in the shrinkage formula.

Practical advice and diagnostics

- •Standardize predictors before hierarchical modeling; it stabilizes priors and sampling.
- •Use weakly informative priors (e.g., half-normal for scales) to regularize and avoid pathologies.
- •Compare centered vs non-centered parameterizations; non-centered is often superior when group-level variance is small relative to observation noise.
- •Check posterior predictive distributions for each group to identify misfit.

Summary

This section extended the core shrinkage idea to multilevel regressions with random effects, explained priors on covariance matrices, and provided practical sampling and parameterization advice. Non-centered parameterization and proper hyperpriors are essential tools for efficient, robust multilevel Bayesian inference.

## Applications and Connections: Store-level vs Chain-level Sharing, Empirical Bayes in Practice, and Downstream Uses

Store-level vs chain-level parameter sharing (concrete business example)

Imagine an online retailer with many stores (or merchants) belonging to a chain. We want to estimate store conversion rates θj\theta\_jθj​ and predict revenue. Options:

- •No pooling: estimate each store separately, θ^j=yj/nj\hat\theta\_j = y\_j/n\_jθ^j​=yj​/nj​, high variance for small stores.
- •Complete pooling: estimate a single chain-level θ\thetaθ, ignores useful heterogeneity.
- •Hierarchical model: θj∼p(θ∣ϕ)\theta\_j\sim p(\theta\mid\phi)θj​∼p(θ∣ϕ) with chain-level hyperprior on ϕ\phiϕ. This automatically shares information across stores: large stores dominate inference for themselves; tiny stores are shrunk toward the chain-level mean.

Concrete Beta-Binomial numeric example

Suppose store A: yA=2y\_A=2yA​=2, nA=20n\_A=20nA​=20; store B: yB=40y\_B=40yB​=40, nB=400n\_B=400nB​=400. With hyperparameters α=10,β=190\alpha=10,\beta=190α=10,β=190 (prior mean 0.05), posterior means are

- •store A: E[θA]=(10+2)/(200+20)=12/220≈0.0545E[\theta\_A]=(10+2)/(200+20)=12/220\approx0.0545E[θA​]=(10+2)/(200+20)=12/220≈0.0545 (shrunk from 0.10 to 0.0545),
- •store B: E[θB]=(10+40)/(200+400)=50/600≈0.0833E[\theta\_B]=(10+40)/(200+400)=50/600\approx0.0833E[θB​]=(10+40)/(200+400)=50/600≈0.0833 (raw 0.10 shrunk only slightly).

This demonstrates adaptive pooling: big-store estimates stay near their data; small-store estimates move toward the chain-level prior.

Empirical Bayes in large-scale problems

For thousands of stores one may use empirical Bayes to estimate hyperparameters quickly via marginal likelihood. A common pipeline:

1. 1)Aggregate store-level sufficient statistics (e.g., counts for Beta-Binomial or sample means and variances for Normal-Normal).
2. 2)Optimize marginal likelihood for hyperparameters (e.g., α,β\alpha,\betaα,β or μ,τ2\mu,\tau^2μ,τ2).
3. 3)Compute posterior summaries for each store conditional on the estimated hyperparameters.

This ML-II approach scales because it reduces high-dimensional posterior inference to a moderate-dimensional optimization; it often suffices for point predictions in industry systems. But be mindful: it ignores hyperparameter uncertainty, which can matter for decision-making, particularly when the number of groups JJJ is small.

Real-world use cases

- •A/B testing across multiple sites: hierarchical models estimate site-specific treatment effects while pooling information to improve detection power.
- •Education: estimate school-level effects (test scores) with partial pooling across schools; used in value-added models.
- •Healthcare: hospital-level outcome rates with case-mix adjustment; hierarchical models stabilize hospital estimates and reduce false positives.
- •Small-area estimation: census and survey domains with sparse data benefit from Bayesian small-area models.

Downstream tasks enabled

- •Better prediction: partial pooling often reduces out-of-sample error compared to no pooling.
- •Decision-making with uncertainty: full Bayesian posterior distributions for group-level parameters enable decision rules that account for both within-group and between-group uncertainty.
- •Hierarchical modeling of complex structures: nested hierarchies (patients within clinicians within hospitals), crossed random effects, and multi-membership models are natural extensions.

Limitations and modeling caveats

- •Model misspecification: if groups are not exchangeable (e.g., unmodeled covariates explain between-group differences), naive pooling may be inappropriate. Solution: include group-level covariates or model non-exchangeable structure.
- •Outliers and heavy tails: a Normal prior for θj\theta\_jθj​ may be too light-tailed; consider Student-t for robustness.
- •Over-shrinkage: overly-informative hyperpriors can force excessive shrinkage. Use weakly informative priors on hyperparameters and check sensitivity.

Computational practice and modern tooling

Modern probabilistic programming (Stan, PyMC, Turing, etc.) makes hierarchical Bayes accessible. Use non-centered parameterizations, LKJ priors for correlations, and adapt step sizes/warmups in HMC. For very large problems consider variational inference or empirical Bayes for speed; validate approximations against full MCMC on subsamples.

Summary

Hierarchical Bayesian models operationalize the balance between pooling and group-specific estimation. In practice, they are the default approach for multi-group inference when you want improved estimates, calibrated uncertainty, and principled borrowing of strength across related units.

## Worked Examples (3)

### Beta-Binomial Store Conversion (Small store)

Store A observed 2 purchases out of 20 visits. Chain-level prior parameters are estimated as alpha=5, beta=95 (prior mean 0.05). Compute the posterior mean and 95% credible interval for store A's conversion rate.

1. Model: y ~ Binomial(n, theta), theta ~ Beta(alpha, beta). Here y=2, n=20, alpha=5, beta=95.
2. Posterior is Beta(alpha + y, beta + n - y) = Beta(5+2, 95+20-2) = Beta(7, 113).
3. Posterior mean = (7) / (7+113) = 7/120 ≈ 0.058333.
4. Compute 95% credible interval using Beta quantiles: lower = Q\_{0.025}(Beta(7,113)), upper = Q\_{0.975}(Beta(7,113)). Numerically, use standard beta CDF/inv. Approximate: lower ≈ 0.024, upper ≈ 0.108 (compute with software).
5. Interpretation: raw rate 2/20 = 0.10; posterior mean = 0.058 (shrunk toward prior mean 0.05); credible interval reflects uncertainty from both data and prior.

**Insight:** This example shows how conjugacy (Beta-Binomial from [Conjugate Priors]) yields a closed-form posterior that shrinks a noisy small-sample estimate toward the chain-level prior mean.

### Normal-Normal Empirical Bayes (Estimating tau^2)

We observe 3 group means: ybar = (9, 11, 10), with each group having n\_j=5 observations and known observation variance sigma^2=4. Use method-of-moments (a simple empirical Bayes approach) to estimate mu and tau^2, then compute the posterior mean for group 1.

1. Model: bar\_y\_j ~ N(mu, tau^2 + sigma^2/n\_j). Here sigma^2/n\_j = 4/5 = 0.8 for each group.
2. Estimate mu by the sample mean: mu\_hat = (9+11+10)/3 = 10.
3. Compute sample variance S^2 of the bar\_y: mean 10, deviations (-1,1,0), S^2 = (1+1+0)/(3-1) = 1.
4. Estimate tau^2 by subtracting average sampling variance: tau2\_hat = max(0, S^2 - 0.8) = max(0, 0.2) = 0.2.
5. Compute shrinkage weight for group 1: kappa = n\_j  *tau2\_hat / (n\_j*  tau2\_hat + sigma^2) = 5*0.2 / (5*0.2 + 4) = 1 / (1 + 4) = 0.2.
6. Posterior mean for theta\_1: (1 - kappa)*mu\_hat + kappa*bar\_y\_1 = 0.8*10 + 0.2*9 = 8 + 1.8 = 9.8.

**Insight:** This example shows empirical Bayes (method-of-moments) producing hyperparameter estimates and the resulting shrinkage: the group mean 9 is pulled toward the pooled mean 10 by weight 0.2. It also shows numeric marginalization: bar\_y marginal variance equals between-group plus sampling variance.

### Varying-intercept Regression with Non-centered Parametrization

We have J=4 stores, each with n\_j observations of sales y\_{ij} and a predictor x\_{ij} (standardized). Model: y\_{ij} ~ N(alpha\_j + beta \* x\_{ij}, sigma^2), alpha\_j ~ N(mu\_alpha, tau\_alpha^2). Assume beta=2 (known), sigma^2=1 (known). Observed group means: bar\_y = (5.2, 4.8, 6.1, 5.5), each with n\_j=10, and pooled predictor mean is zero. Use non-centered parametrization to compute posterior samples conceptually and compute the posterior mean for alpha\_3 using mu\_alpha prior mean 5 and prior tau\_alpha ~ HalfNormal(0,1) with empirical Bayes tau\_alpha\_hat computed via method-of-moments.

1. Given beta and sigma known and x standardized with pooled mean zero, the sample group means bar\_y\_j ≈ alpha\_j + beta\*bar\_x\_j (but bar\_x\_j ≈ 0), so bar\_y\_j ≈ alpha\_j.
2. Compute pooled mean mu\_hat = mean(bar\_y) = (5.2+4.8+6.1+5.5)/4 = 5.4.
3. Sample variance of bar\_y: deviations are (-0.2,-0.6,0.7,0.1), squared sum = 0.04+0.36+0.49+0.01=0.9, so S^2 = 0.9/(4-1)=0.3.
4. Sampling variance per bar\_y = sigma^2/n\_j = 1/10 = 0.1. Method-of-moments gives tau\_alpha\_hat = max(0, S^2 - 0.1) = max(0, 0.2) = 0.2.
5. Non-centered parametrization: alpha\_j = mu\_alpha + tau\_alpha\_hat  *eta\_j, eta\_j ~ N(0,1). Posterior for eta\_j given bar\_y\_j is equivalent to the normal-normal conjugate case with observed mean bar\_y\_j and known variances; shrinkage weight kappa = n\_j*  tau2 /(n\_j  *tau2 + sigma^2) = 10*0.2/(10\*0.2+1) = 2/(2+1)=2/3 ≈ 0.6667.
6. Posterior mean for alpha\_3: (1-kappa)*mu\_hat + kappa*bar\_y\_3 = 0.3333*5.4 + 0.6667*6.1 = 1.8 + 4.0667 = 5.8667.

**Insight:** This worked example combines varying-intercept regression with non-centered parametrization logic. It shows how to compute empirical Bayes scale, then express alpha\_j via a standardized eta\_j for better MCMC conditioning; it also computes numeric posterior mean demonstrating substantial shrinkage toward pooled mean.

## Key Takeaways

- ✓

  Hierarchical Bayesian models encode exchangeability across groups via priors on group-level parameters (hyperpriors), enabling principled partial pooling.
- ✓

  In conjugate cases (e.g., Normal-Normal, Beta-Binomial) closed-form posteriors yield explicit shrinkage weights that blend group data with group-level means.
- ✓

  Empirical Bayes (ML-II) estimates hyperparameters by marginalizing over group-level parameters and optimizing the marginal likelihood, providing fast approximate pooling but underestimating hyperparameter uncertainty.
- ✓

  Multilevel regression generalizes to varying intercepts and slopes; priors on covariance matrices (separation strategy with LKJ) and non-centered parameterizations are essential for robust MCMC.
- ✓

  Shrinkage reduces mean-squared error relative to no-pooling and connects to frequentist shrinkage estimators like James–Stein; however, model specification (exchangeability, covariates) is crucial to avoid bias.
- ✓

  Posterior predictive checks and sensitivity to hyperpriors should guide modeling choices—use weakly informative priors on scales to prevent over-shrinkage.
- ✓

  Practical pipelines often use empirical Bayes for scale and initialization and full Bayesian sampling for final uncertainty quantification when feasible.

## Common Mistakes

- ✗

  Treating empirical Bayes point estimates of hyperparameters as if they were exact: this underestimates posterior uncertainty and can lead to overconfident predictions, especially with few groups.
- ✗

  Using a centered parameterization when group-level variances are poorly identified (small n\_j, large tau): leads to funnel-shaped posteriors and slow MCMC mixing—use non-centered parametrization instead.
- ✗

  Assuming exchangeability without checking covariates: if groups differ systematically by observed covariates, failing to include those covariates causes biased shrinkage toward an inappropriate common mean.
- ✗

  Overly-informative hyperpriors on scales (tau) that force unrealistic shrinkage: prefer weakly informative priors (half-normal, half-Cauchy) and perform sensitivity analysis.

## Practice

easy

Easy: Beta-Binomial partial pooling. You observe two stores: Store 1 has y1=3 successes out of n1=30, Store 2 has y2=20 successes out of n2=200. The chain-level prior is Beta(alpha=6, beta=114) (prior mean 0.05). Compute the posterior mean for each store's theta and compare to raw rates.

**Hint:** Posterior for each theta\_j is Beta(alpha + y\_j, beta + n\_j - y\_j). Posterior mean = (alpha+y)/(alpha+beta+n).

Show solution

Store 1: posterior Beta(6+3,114+30-3)=Beta(9,141). Posterior mean = 9/(9+141)=9/150=0.06. Raw rate = 3/30=0.10. Store 2: posterior Beta(6+20,114+200-20)=Beta(26,294). Posterior mean = 26/(26+294)=26/320=0.08125. Raw rate = 20/200=0.10. Both are shrunk toward prior mean 0.05; the small store shrinks more (0.06) than the large store (0.08125).

medium

Medium: Normal-Normal with unequal n\_j. You observe bar\_y = (12, 8) with n = (10, 2) and known sigma^2=9. Assume prior theta\_j ~ N(mu=10, tau^2=4). Compute posterior means and posterior variances for theta\_1 and theta\_2 using the shrinkage formula.

**Hint:** Posterior precision = 1/tau^2 + n\_j/sigma^2; posterior mean = precision^{-1}  *( (1/tau^2)*mu + (n\_j/sigma^2)\*bar\_y\_j ).

Show solution

For j=1: n1=10, bar\_y1=12. Data precision = n1/sigma^2 = 10/9 ≈ 1.1111. Prior precision = 1/tau^2 = 1/4 = 0.25. Posterior precision = 1.3611, posterior variance = 1/1.3611 ≈ 0.7347. Posterior mean = (0.25*10 + 1.1111*12)/1.3611 = (2.5 + 13.3332)/1.3611 = 15.8332/1.3611 ≈ 11.631. For j=2: n2=2, bar\_y2=8. Data precision = 2/9 ≈ 0.2222. Posterior precision = 0.25 + 0.2222 = 0.4722, posterior variance = 1/0.4722 ≈ 2.118. Posterior mean = (0.25*10 + 0.2222*8)/0.4722 = (2.5 + 1.7776)/0.4722 = 4.2776/0.4722 ≈ 9.062. Interpretation: the small-sample group 2 is shrunk much closer to mu=10 than group 1.

hard

Hard: Empirical Bayes vs Full Bayes on between-group variance. You have J=5 groups with bar\_y = (4.8, 5.1, 4.9, 5.0, 6.2), n\_j=5 each, and known sigma^2=1. (a) Compute the empirical Bayes estimate of tau^2 by maximizing the marginal likelihood numerically (or use method-of-moments approximation). (b) Suppose you put a prior tau ~ HalfNormal(0,1) and perform full Bayes: explain qualitatively how the posterior distribution for tau will differ from the point estimate, and how that affects uncertainty of individual theta\_j posteriors.

**Hint:** For (a) use marginal variance across bar\_y minus sampling variance. For (b) recall that full Bayes integrates over tau, so posterior variance for theta\_j reflects uncertainty about tau in addition to within-group noise.

Show solution

(a) Sample mean mu\_hat = (4.8+5.1+4.9+5.0+6.2)/5 = 5.2. Sample variance S^2 = ( (4.8-5.2)^2 + (5.1-5.2)^2 + (4.9-5.2)^2 + (5.0-5.2)^2 + (6.2-5.2)^2 ) / (5-1) = (0.16+0.01+0.09+0.04+1.0)/4 = 1.30/4 = 0.325. Sampling variance sigma^2/n = 1/5 = 0.2. Method-of-moments tau^2\_hat = max(0, S^2 - 0.2) = 0.125. (b) With full Bayes and prior tau ~ HalfNormal(0,1), the posterior for tau will be a distribution concentrated near 0.125 but with nonzero mass, reflecting data uncertainty. The resulting posterior for each theta\_j is a mixture over tau, so posterior variances for theta\_j will be larger than those from empirical Bayes which conditions on the point estimate; in particular, uncertainty from tau propagates into wider credible intervals for theta\_j, especially for small n\_j and when J is small.

## Connections

Looking back: this lesson builds directly on [Conjugate Priors] where Beta-Binomial and Normal-Normal conjugacy were introduced; those closed-form updates are the building blocks for analytic hierarchical calculations and for deriving marginal likelihoods used in empirical Bayes. It also assumes familiarity with [MCMC]: hierarchical models often require sampling from joint posteriors over many parameters, where non-centered parameterizations (covered here) and diagnostics from [MCMC] are essential. Looking forward: mastering hierarchical Bayes enables hierarchical generalized linear models, Gaussian processes with hierarchical kernels, Bayesian causal hierarchical models (multi-site A/B testing), and small-area estimation in official statistics. Downstream techniques that require this material include: multilevel survival analysis, hierarchical state-space models, and modern probabilistic programming best practices (e.g., priors for covariance matrices using LKJ). Empirical Bayes connects to frequentist shrinkage techniques (James–Stein, ridge regression) and to scalable approximate inference (variational Bayes, MAP/ML-II pipelines) used in large-scale industry systems.

Quality: pending (0.0/5)

[← back to tree](/tech-tree/)[browse all →](/tech-tree/inventory/)
