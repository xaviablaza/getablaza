---
title: Time Series Foundations
description: Stationarity, autocorrelation and partial autocorrelation functions. AR, MA, ARMA, ARIMA models. Box-Jenkins methodology.
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
inspiration_url: https://templeton.host/tech-tree/time-series-foundations/
inspiration_category: tech-tree
---

> Source-copy draft imported from [https://templeton.host/tech-tree/time-series-foundations/](https://templeton.host/tech-tree/time-series-foundations/). Names, domain references, and local media paths were adapted for Xavi Ablaza / getablaza.com.

[←Back to Tech Tree](/tech-tree/)

[inventory](/tech-tree/inventory/)[coverage](/tech-tree/coverage/)

# Time Series Foundations

Probability & StatisticsDifficulty: ★★★☆☆Depth: 10Unlocks: 3

Stationarity, autocorrelation and partial autocorrelation functions. AR, MA, ARMA, ARIMA models. Box-Jenkins methodology.

## Prerequisites (2)

[Covariance and Correlation6 atoms](/tech-tree/covariance-correlation/)[Linear Regression6 atoms](/tech-tree/linear-regression/)

## Unlocks (1)

[State-Space Modelslvl 4](/tech-tree/state-space-models/)

## Referenced by (6)

Where this concept shows up in the operating-finance and personal-finance graphs.

### From Business (6)

[Cash FlowBusiness

Cash flow is inherently a time series - sequential inflows and outflows where timing, seasonality, and autocorrelation matter. Stationarity concepts explain why a single-period snapshot misleads about liquidity.](/business/cash-flow/)[real estateBusiness

RE market cycles, Case-Shiller index methodology, and mean-reversion analysis all require stationarity testing and ARIMA-family models](/business/real-estate/)[Value StreamBusiness

Determining whether a value stream appreciates or decays requires modeling its trajectory over time; stationarity tests distinguish trending streams (appreciating or decaying) from mean-reverting ones, and autocorrelation reveals whether past performance compounds into future value](/business/value-stream/)[ARRBusiness

ARR is inherently a time-indexed metric whose trajectory, trend decomposition, and forecasting rely on time series concepts like stationarity and autoregressive modeling.](/business/arr/)[Depreciating AssetBusiness

Stationarity is the core concept - a verifier is built assuming a fixed rule distribution, but non-stationarity (rules change over time) is exactly what causes the verifier to depreciate, requiring re-estimation against the new regime](/business/depreciating-asset/)[CFABusiness

CFA quantitative methods covers autoregressive models and stationarity for financial return series and economic forecasting](/business/cfa/)

Advanced Learning Details

### Graph Position

162

Depth Cost

3

Fan-Out (ROI)

1

Bottleneck Score

10

Chain Length

Many real-world datasets are sequences in time — from daily stock prices to hourly sensor readings — and understanding their time-dependent patterns lets you forecast, detect anomalies, and make decisions with confidence.

TL;DR:

Time series foundations give you tools to tell whether a sequence is stable over time, measure how past values influence future ones (autocorrelation and partial autocorrelation), build AR/MA/ARMA/ARIMA models, and apply the Box–Jenkins cycle to identify, estimate, and validate models for forecasting.

## What Is Time Series Foundations?

Time series analysis studies observations indexed by time: {Xt:t∈Z}\{X\_t: t \in \mathbb{Z}\}{Xt​:t∈Z}, where XtX\_tXt​ is the value at time ttt. The foundations of time series cover three core concepts: stationarity (is the process stable over time?), dependence (how does Xt−kX\_{t-k}Xt−k​ affect XtX\_tXt​?), and parsimonious models that capture that dependence (AR, MA, ARMA, ARIMA). These let you move from raw data to forecasts and inference.

Why care? Because many applied problems are sequential: forecasting electricity load, modeling GDP, or controlling processes in engineering. A model that respects time-dependence is usually far more accurate than treating observations as iid. The prerequisites you already know — Covariance and Correlation (measuring linear relation) and Linear Regression (estimating linear coefficients via least squares) — are used heavily: sample autocovariances extend covariance to lags, and regression ideas underpin estimation of autoregressive parameters.

Stationarity: Intuitively, a stationary time series 'behaves the same' through time. We commonly use weak (covariance) stationarity: 1) constant mean E[Xt]=μ\mathbb{E}[X\_t]=\muE[Xt​]=μ for all ttt, 2) autocovariance γ(s,t)=Cov⁡(Xs,Xt)\gamma(s,t)=\operatorname{Cov}(X\_s,X\_t)γ(s,t)=Cov(Xs​,Xt​) depends only on lag ∣t−s∣|t-s|∣t−s∣, i.e. γ(h)=Cov⁡(Xt,Xt−h)\gamma(h)=\operatorname{Cov}(X\_{t},X\_{t-h})γ(h)=Cov(Xt​,Xt−h​). Strict stationarity (distribution invariance under time shifts) is stronger but weaker in practice because many models are only second-order.

Concrete example: Random walk vs AR(1)

- •Random walk: Xt=Xt−1+εtX\_t = X\_{t-1} + \varepsilon\_tXt​=Xt−1​+εt​ with εt∼(0,σ2)\varepsilon\_t \sim (0,\sigma^2)εt​∼(0,σ2). The mean of XtX\_tXt​ depends on ttt (it drifts with accumulated noise), so it's non-stationary.
- •AR(1): Xt=ϕXt−1+εtX\_t = \phi X\_{t-1} + \varepsilon\_tXt​=ϕXt−1​+εt​, with ∣ϕ∣<1|\phi|<1∣ϕ∣<1 is stationary. For ∣ϕ∣<1|\phi|<1∣ϕ∣<1 and εt\varepsilon\_tεt​ white noise with variance σ2\sigma^2σ2, the stationary variance is

Var⁡(Xt)=σ21−ϕ2.\operatorname{Var}(X\_t)=\frac{\sigma^2}{1-\phi^2}.Var(Xt​)=1−ϕ2σ2​.

Numeric example: if ϕ=0.6\phi=0.6ϕ=0.6 and σ2=1\sigma^2=1σ2=1, then Var⁡(Xt)=1/(1−0.36)=1/0.64=1.5625.\operatorname{Var}(X\_t)=1/(1-0.36)=1/0.64=1.5625.Var(Xt​)=1/(1−0.36)=1/0.64=1.5625. This shows a finite, time-invariant variance.

Autocorrelation and autocovariance: the autocovariance at lag kkk is

γk=Cov⁡(Xt,Xt−k),\gamma\_k = \operatorname{Cov}(X\_t,X\_{t-k}),γk​=Cov(Xt​,Xt−k​),

and the autocorrelation is

ρk=γkγ0,\rho\_k = \frac{\gamma\_k}{\gamma\_0},ρk​=γ0​γk​​,

where γ0=Var⁡(Xt)\gamma\_0=\operatorname{Var}(X\_t)γ0​=Var(Xt​). These generalize the concepts from Covariance and Correlation. A quick sample calculation: suppose observed series [2,4,6,8][2,4,6,8][2,4,6,8]. The sample mean Xˉ=5\bar X=5Xˉ=5. The sample lag-1 autocovariance (using denominator nnn for simplicity) is

γ^1=14∑t=24(Xt−Xˉ)(Xt−1−Xˉ).\hat\gamma\_1 = \frac{1}{4}\sum\_{t=2}^4 (X\_t-\bar X)(X\_{t-1}-\bar X).γ^​1​=41​t=2∑4​(Xt​−Xˉ)(Xt−1​−Xˉ).

Compute terms: (4−5)(2−5)=(−1)(−3)=3(4-5)(2-5)=(-1)(-3)=3(4−5)(2−5)=(−1)(−3)=3, (6−5)(4−5)=(1)(−1)=−1(6-5)(4-5)=(1)(-1)=-1(6−5)(4−5)=(1)(−1)=−1, (8−5)(6−5)=(3)(1)=3(8-5)(6-5)=(3)(1)=3(8−5)(6−5)=(3)(1)=3. Sum = 3-1+3=5. So γ^1=5/4=1.25\hat\gamma\_1 = 5/4 = 1.25γ^​1​=5/4=1.25. The sample variance γ^0=14[(2−5)2+(4−5)2+(6−5)2+(8−5)2]=(9+1+1+9)/4=20/4=5\hat\gamma\_0 = \frac{1}{4}[(2-5)^2+(4-5)^2+(6-5)^2+(8-5)^2] = (9+1+1+9)/4 = 20/4 = 5γ^​0​=41​[(2−5)2+(4−5)2+(6−5)2+(8−5)2]=(9+1+1+9)/4=20/4=5. Thus sample autocorrelation at lag 1 is ρ^1=1.25/5=0.25\hat\rho\_1 = 1.25/5 = 0.25ρ^​1​=1.25/5=0.25.

Partial Autocorrelation (PACF): the PACF at lag kkk, denoted ϕkk\phi\_{kk}ϕkk​ or αk\alpha\_kαk​, measures the correlation between XtX\_tXt​ and Xt−kX\_{t-k}Xt−k​ after removing linear effects of intermediate lags $1\ldots k-1$. A simple way to compute PACF is to fit the linear regression

Xt=β0+β1Xt−1+⋯+βkXt−k+εtX\_t = \beta\_0 + \beta\_1 X\_{t-1} + \dots + \beta\_k X\_{t-k} + \varepsilon\_tXt​=β0​+β1​Xt−1​+⋯+βk​Xt−k​+εt​

and take the coefficient on Xt−kX\_{t-k}Xt−k​. This uses Linear Regression skills directly. Numeric example: for an AR(1) with coefficient ϕ=0.6\phi=0.6ϕ=0.6, PACF at lag 1 is $0.6$ and at higher lags it is (theoretically) 0.

Model types (intuition):

- •AR(p) (autoregressive of order p): Xt=ϕ1Xt−1+⋯+ϕpXt−p+εtX\_t = \phi\_1 X\_{t-1} + \dots + \phi\_p X\_{t-p} + \varepsilon\_tXt​=ϕ1​Xt−1​+⋯+ϕp​Xt−p​+εt​. Like regressing current value on p past values. If p=1, AR(1) as above.
- •MA(q) (moving average of order q): Xt=εt+θ1εt−1+⋯+θqεt−qX\_t = \varepsilon\_t + \theta\_1 \varepsilon\_{t-1} + \dots + \theta\_q \varepsilon\_{t-q}Xt​=εt​+θ1​εt−1​+⋯+θq​εt−q​. This is a linear filter of white noise and has dependence that dies after q lags in the PACF/ACF in characteristic ways.
- •ARMA(p,q): combination of both.
- •ARIMA(p,d,q): integrate non-stationary series d times (differences) then fit ARMA(p,q).

These building blocks let you represent many time series parsimoniously and prepare for forecasting. The rest of the lesson develops the main mechanical tools: ACF/PACF, estimation via Yule–Walker and least squares, and the Box–Jenkins cycle for practical modeling.

## Core Mechanic 1: Autocorrelation and Partial Autocorrelation (ACF & PACF)

ACF and PACF are the primary diagnostic tools for identifying the dependence structure in a stationary time series. They are analogous to the correlation and partial correlation concepts from Covariance and Correlation and use Linear Regression for PACF computations.

Definitions and sample formulas

- •The theoretical autocovariance function (ACVF) is γk=Cov(Xt,Xt−k)\gamma\_k = \mathrm{Cov}(X\_t,X\_{t-k})γk​=Cov(Xt​,Xt−k​). The theoretical autocorrelation function (ACF) is ρk=γk/γ0\rho\_k = \gamma\_k/\gamma\_0ρk​=γk​/γ0​.
- •For an observed series x1,…,xnx\_1,\dots,x\_nx1​,…,xn​, the sample autocovariance at lag kkk is often taken as

γ^k=1n∑t=k+1n(xt−xˉ)(xt−k−xˉ).\hat\gamma\_k = \frac{1}{n}\sum\_{t=k+1}^{n} (x\_t-\bar x)(x\_{t-k}-\bar x).γ^​k​=n1​t=k+1∑n​(xt​−xˉ)(xt−k​−xˉ).

Example: with [2,4,6,8][2,4,6,8][2,4,6,8] we computed γ^1=1.25\hat\gamma\_1=1.25γ^​1​=1.25 and γ^0=5\hat\gamma\_0=5γ^​0​=5, so ρ^1=0.25\hat\rho\_1=0.25ρ^​1​=0.25 (see Section 1). If you prefer the unbiased denominator n−kn-kn−k replace $1/n$ with $1/(n-k)$; both are used in practice.

Properties of ACF for simple models (critical identification clues)

- •AR(1): Xt=ϕXt−1+εtX\_t=\phi X\_{t-1}+\varepsilon\_tXt​=ϕXt−1​+εt​ with ∣ϕ∣<1|\phi|<1∣ϕ∣<1 has theoretical autocorrelation ρk=ϕk\rho\_k = \phi^kρk​=ϕk. Numeric example: ϕ=0.6\phi=0.6ϕ=0.6 gives ρ1=0.6\rho\_1=0.6ρ1​=0.6, ρ2=0.36\rho\_2=0.36ρ2​=0.36, ρ3=0.216\rho\_3=0.216ρ3​=0.216, etc.
- •MA(1): Xt=εt+θεt−1X\_t=\varepsilon\_t+\theta\varepsilon\_{t-1}Xt​=εt​+θεt−1​ has ρ1=θ/(1+θ2)\rho\_1=\theta/(1+\theta^2)ρ1​=θ/(1+θ2) and ρk=0\rho\_k=0ρk​=0 for k>1k>1k>1. Numeric example: θ=0.5\theta=0.5θ=0.5 gives ρ1=0.5/(1+0.25)=0.5/1.25=0.4\rho\_1=0.5/(1+0.25)=0.5/1.25=0.4ρ1​=0.5/(1+0.25)=0.5/1.25=0.4, and ρ2=0\rho\_2=0ρ2​=0.

Thus the ACF of AR(1) decays exponentially, while the ACF of MA(1) cuts off after lag 1. This distinction is foundational for identification.

Partial Autocorrelation Function (PACF)

- •PACF at lag kkk, denoted αk\alpha\_kαk​ or ϕkk\phi\_{kk}ϕkk​, is the coefficient on Xt−kX\_{t-k}Xt−k​ in the best linear predictor of XtX\_tXt​ using Xt−1,…,Xt−kX\_{t-1},\dots,X\_{t-k}Xt−1​,…,Xt−k​:

Xt=β0+β1Xt−1+⋯+βkXt−k+ut,X\_t = \beta\_0 + \beta\_1 X\_{t-1} + \dots + \beta\_k X\_{t-k} + u\_t,Xt​=β0​+β1​Xt−1​+⋯+βk​Xt−k​+ut​,

then αk=βk\alpha\_k = \beta\_kαk​=βk​ from that regression. For stationary AR(p), the PACF cuts off after lag ppp (i.e., αk=0\alpha\_k=0αk​=0 for k>pk>pk>p). For MA(q), the PACF decays gradually.

Computational methods

- •Sample ACF is computed directly from γ^k\hat\gamma\_kγ^​k​ as ρ^k=γ^k/γ^0\hat\rho\_k = \hat\gamma\_k/\hat\gamma\_0ρ^​k​=γ^​k​/γ^​0​.
- •Sample PACF can be estimated by fitting the regression above for each kkk (this uses Linear Regression knowledge). Another route uses the Durbin–Levinson recursion or solving Yule–Walker linear systems; both rely on sample autocovariances.

Small numeric demonstration of PACF via regression: Data: x=[1.2,0.9,1.1,1.4,1.3]x=[1.2, 0.9, 1.1, 1.4, 1.3]x=[1.2,0.9,1.1,1.4,1.3]. Compute xˉ=1.18\bar x=1.18xˉ=1.18. To estimate PACF at lag 2 (i.e., coefficient on Xt−2X\_{t-2}Xt−2​ when regressing on lags 1 and 2), form the design matrix for t=3..5:

X = [[x\_2,x\_1],[x\_3,x\_2],[x\_4,x\_3]] = [[0.9,1.2],[1.1,0.9],[1.4,1.1]].

Response y = [x\_3,x\_4,x\_5] = [1.1,1.4,1.3].

Run a small OLS: β=(XTX)−1XTy\beta=(X^TX)^{-1}X^T yβ=(XTX)−1XTy. Numeric calculation (sketch): XTX=(0.92+1.12+1.420.9⋅1.2+1.1⋅0.9+1.4⋅1.1same1.22+0.92+1.12)X^TX = \begin{pmatrix}0.9^2+1.1^2+1.4^2 & 0.9\cdot1.2+1.1\cdot0.9+1.4\cdot1.1 \\ same & 1.2^2+0.9^2+1.1^2\end{pmatrix}XTX=(0.92+1.12+1.42same​0.9⋅1.2+1.1⋅0.9+1.4⋅1.11.22+0.92+1.12​). Compute numbers: $0.81+1.21+1.96=3.98$, off-diagonal $1.08+0.99+1.54=3.61$, lower-right $1.44+0.81+1.21=3.46$. Solve to obtain coefficients; the lag-2 coefficient is the PACF estimate. This step explicitly uses Linear Regression.

Interpreting ACF/PACF plots

- •If ACF decays slowly and PACF cuts off after p lags: suggest AR(p).
- •If ACF cuts off after q lags and PACF decays: suggest MA(q).
- •Mixed decay patterns suggest ARMA models.

Statistical significance: For large n, sample autocorrelations under white noise are approximately N(0,1/n)N(0,1/n)N(0,1/n). A rough 95% confidence band is ±1.96/n\pm 1.96/\sqrt{n}±1.96/n​. Example: if n=100n=100n=100, the band is ±0.196\pm 0.196±0.196. Any sample ACF outside that band suggests significant autocorrelation.

Thus ACF and PACF, combined with numerical rules and plots, are your first discovery tools in the Box–Jenkins cycle (coming later). They depend directly on Covariance and Correlation ideas and on Linear Regression for PACF estimation.

## Core Mechanic 2: AR, MA, ARMA, ARIMA Models and Estimation

We now define the principal parametric families and show core formulas and estimation strategies. These models are linear in either past values or past shocks and are the workhorses of time series forecasting.

Autoregressive (AR) models

- •AR(p) model:

Xt=ϕ1Xt−1+ϕ2Xt−2+⋯+ϕpXt−p+εt,X\_t = \phi\_1 X\_{t-1} + \phi\_2 X\_{t-2} + \dots + \phi\_p X\_{t-p} + \varepsilon\_t,Xt​=ϕ1​Xt−1​+ϕ2​Xt−2​+⋯+ϕp​Xt−p​+εt​,

where εt\varepsilon\_tεt​ is white noise with mean 0 and variance σ2\sigma^2σ2. This is analogous to regressing XtX\_tXt​ on its past p values (Linear Regression). To fit AR(p), one can use OLS on lagged regressors when the series is mean zero or include an intercept if needed. Another method uses the Yule–Walker equations derived from autocovariances.

Yule–Walker equations (for AR(p))

The theoretical autocovariances satisfy:

(γ0γ1⋮γp−1)=(1ϕ1…ϕp−1ϕ11…ϕp−2⋮⋱ϕp−1…ϕ11)(σ2 0 ⋮)\begin{pmatrix}\gamma\_0 \\ \gamma\_1 \\ \vdots \\ \gamma\_{p-1}\end{pmatrix} = \begin{pmatrix}1 & \phi\_1 & \dots & \phi\_{p-1} \\\phi\_1 & 1 & \dots & \phi\_{p-2} \\\vdots & & \ddots & \\\phi\_{p-1} & \dots & \phi\_1 & 1\end{pmatrix} \begin{pmatrix}\sigma^2 \\\ 0 \\\ \vdots\end{pmatrix}​γ0​γ1​⋮γp−1​​​=​1ϕ1​⋮ϕp−1​​ϕ1​1…​……⋱ϕ1​​ϕp−1​ϕp−2​1​​​σ2 0 ⋮​​

A practical way is to solve the linear system

(γ1γ2 ⋮γp)=(γ0γ1…γp−1γ1γ0…γp−2⋮⋱γp−1…γ0)(ϕ1ϕ2 ⋮ϕp).\begin{pmatrix}\gamma\_1 \\\gamma\_2 \\\ \vdots \\\gamma\_p\end{pmatrix} = \begin{pmatrix}\gamma\_0 & \gamma\_1 & \dots & \gamma\_{p-1} \\\gamma\_1 & \gamma\_0 & \dots & \gamma\_{p-2} \\\vdots & & \ddots & \\\gamma\_{p-1} & \dots & \gamma\_0\end{pmatrix} \begin{pmatrix}\phi\_1 \\\phi\_2 \\\ \vdots \\\phi\_p\end{pmatrix}.​γ1​γ2​ ⋮γp​​​=​γ0​γ1​⋮γp−1​​γ1​γ0​…​……⋱γ0​​γp−1​γp−2​​​​ϕ1​ϕ2​ ⋮ϕp​​​.

Use sample autocovariances to get Yule–Walker estimators. Example: AR(1) Yule–Walker reduces to γ1=ϕγ0\gamma\_1 = \phi \gamma\_0γ1​=ϕγ0​, so ϕ=γ1/γ0\phi = \gamma\_1/\gamma\_0ϕ=γ1​/γ0​. Numerically, using the sample values from Section 1 where γ^1=1.25\hat\gamma\_1=1.25γ^​1​=1.25 and γ^0=5\hat\gamma\_0=5γ^​0​=5, the Yule–Walker estimate is ϕ^=1.25/5=0.25\hat\phi = 1.25/5 = 0.25ϕ^​=1.25/5=0.25.

Moving Average (MA) models

- •MA(q) model:

Xt=εt+θ1εt−1+⋯+θqεt−q.X\_t = \varepsilon\_t + \theta\_1 \varepsilon\_{t-1} + \dots + \theta\_q \varepsilon\_{t-q}.Xt​=εt​+θ1​εt−1​+⋯+θq​εt−q​.

The parameters θj\theta\_jθj​ multiply the unobserved past shocks εt−j\varepsilon\_{t-j}εt−j​, making direct linear regression impossible. Estimation typically proceeds via maximum likelihood or nonlinear least squares. However, the MA autocovariance has closed-form expressions in terms of θ\thetaθ and σ2\sigma^2σ2, which you can equate to sample autocovariances for method-of-moments estimation in small orders. Example: for MA(1) ρ1=θ/(1+θ2)\rho\_1 = \theta/(1+\theta^2)ρ1​=θ/(1+θ2). If sample ρ^1=0.4\hat\rho\_1=0.4ρ^​1​=0.4, solving $0.4 = \theta/(1+\theta^2)$ yields $0.4+0.4\theta^2=\theta \Rightarrow 0.4\theta^2 - \theta + 0.4=0.Solvenumerically:discriminant. Solve numerically: discriminant .Solvenumerically:discriminant=1-4\cdot0.4^2=1-0.64=0.36,so, so ,so\theta=(1\pm 0.6)/(0.8).Positiveroot. Positive root .Positiveroot(1-0.6)/0.8=0.4/0.8=0.5or or or(1+0.6)/0.8=1.6/0.8=2;invertibilityconstraintusuallyselects; invertibility constraint usually selects ;invertibilityconstraintusuallyselects|\theta|<1,so, so ,so\theta=0.5$.

ARMA(p,q) models

- •ARMA(p,q): combines AR and MA parts:

Xt=ϕ1Xt−1+⋯+ϕpXt−p+εt+θ1εt−1+⋯+θqεt−q.X\_t = \phi\_1 X\_{t-1} + \dots + \phi\_p X\_{t-p} + \varepsilon\_t + \theta\_1 \varepsilon\_{t-1} + \dots + \theta\_q \varepsilon\_{t-q}.Xt​=ϕ1​Xt−1​+⋯+ϕp​Xt−p​+εt​+θ1​εt−1​+⋯+θq​εt−q​.

Estimation is typically via maximum likelihood (often numerically executed) or conditional least squares.

ARIMA(p,d,q): dealing with nonstationarity

- •If the series is non-stationary, differencing can remove trends. A first difference is Yt=Xt−Xt−1Y\_t = X\_t - X\_{t-1}Yt​=Xt​−Xt−1​. The ARIMA(p,d,q) model means the d-th difference of XtX\_tXt​ follows an ARMA(p,q). For example, a random walk Xt=Xt−1+εtX\_t = X\_{t-1} + \varepsilon\_tXt​=Xt−1​+εt​ is ARIMA(0,1,0).

Forecasting with AR models (closed-form)

- •For AR(1) with mean zero: Xt=ϕXt−1+εtX\_t = \phi X\_{t-1} + \varepsilon\_tXt​=ϕXt−1​+εt​, the h-step ahead forecast from time t is

\hat X\_{t+h|t} = \phi^h X\_t.$$ Numeric example: $\phi=0.6$, $X\_t=10$, the 3-step forecast is $0.6^3\cdot 10 = 0.216\cdot 10 = 2.16.$
- With a nonzero mean $\mu$, the forecast becomes
$$\hat X\_{t+h|t} = \mu + \phi^h (X\_t-\mu).

Estimation practicalities and model selection

- •Fit candidate models (identified via ACF/PACF), estimate parameters (Yule–Walker/OLS/ML), check diagnostics (residuals should resemble white noise), and compare models with AIC/BIC. Use overfitting caution: more parameters reduce residual variance but can harm out-of-sample forecasts.

Identifiability and invertibility

- •AR models require roots of the characteristic polynomial $1-\phi\_1 z - \dots - \phi\_p z^p$ lie outside the unit circle for stationarity. MA models require the invertibility condition (roots of $1+\theta\_1 z + \dots$ outside unit circle). Checking these ensures unique parameterizations.

Concrete example illustrating estimation difference: Suppose sample ACF shows strong decay and PACF cuts after 2 lags: this suggests AR(2). Using sample autocovariances γ^1,γ^2\hat\gamma\_1,\hat\gamma\_2γ^​1​,γ^​2​ we solve Yule–Walker linear system to get ϕ^1,ϕ^2\hat\phi\_1,\hat\phi\_2ϕ^​1​,ϕ^​2​ and compute residuals ε^t\hat\varepsilon\_tε^t​ then estimate σ^2\hat\sigma^2σ^2 as mean squared residual. This combines Covariance and Correlation (autocovariances) and Linear Regression (residual analysis).

In short, AR/MA/ARMA/ARIMA provide interpretable, mathematically tractable families; Yule–Walker and OLS give simple estimation for AR models, while MA parameters often need likelihood-based methods.

## Applications and Connections: Box–Jenkins Methodology and Real-World Use

The Box–Jenkins (BJ) methodology is a structured four-step practical workflow for building ARIMA-class models. It turns the theoretical tools (ACF/PACF, AR/MA definitions, stationarity tests) into an applied recipe. Each step references ideas you've seen in previous sections and relies on Covariance and Correlation and Linear Regression for computations.

Box–Jenkins steps

1) Identification: Use plots of the time series, ACF, and PACF to decide whether differencing is needed and to propose model orders p and q. Look for patterns: slow ACF decay suggests nonstationarity or AR behavior; ACF cutoffs help detect MA terms. Example: If ACF decays slowly and first differences look stationary, set d=1 and then examine the ACF/PACF of differenced series.

2) Estimation: Fit candidate ARIMA(p,d,q) models via maximum likelihood or conditional least squares; estimate parameters ϕ,θ,σ2\phi,\theta,\sigma^2ϕ,θ,σ2. For AR parts you might use Yule–Walker to get initial estimates (a closed-form start) and then refine via ML. Example: Fit ARIMA(1,1,1) to data; the differencing makes the series stationary before estimation.

3) Diagnostic checking: Analyze residuals ε^t\hat\varepsilon\_tε^t​ from the fitted model. Residual ACF should show no significant autocorrelation (randomness). Perform Ljung–Box test for joint autocorrelation up to lag m. Residuals should be approximately uncorrelated with constant variance and mean zero. If diagnostics fail, go back to step 1 and refine model orders.

4) Forecasting: With a validated model, compute forecasts and forecast intervals. ARIMA models allow iterative computation of point forecasts and mean squared error estimates for prediction intervals.

Concrete real-world examples and use cases

- •Economics: GDP and inflation series often modeled with ARIMA for medium-term forecasting. Example: GDP growth series are often stationary after first differencing (d=1), motivating ARIMA( p,1,q ) fits.
- •Finance: Daily returns are often roughly stationary and may require ARMA to capture serial dependence; however, volatility clustering is typically modeled with GARCH, which builds on AR foundations.
- •Energy: Electricity load often displays strong daily/weekly seasonality. Seasonal ARIMA (SARIMA) extends ARIMA with seasonal differencing and seasonal AR/MA terms: SARIMA(p,d,q)(P,D,Q)\_s. Example: hourly load with daily seasonality s=24 might need D=1 or SAR terms.

Seasonality and SARIMA: When periodic patterns exist, include seasonal terms. For seasonal period s, a SARIMA model includes factors like (1−Φ1Bs−… )(1 - \Phi\_1 B^s - \dots )(1−Φ1​Bs−…) for seasonal AR and seasonal differencing (1−Bs)D(1-B^s)^D(1−Bs)D. Numeric example: for monthly data with annual seasonality s=12, seasonal differencing with D=1 is Yt=(1−B12)Xt=Xt−Xt−12Y\_t = (1-B^{12})X\_t = X\_t - X\_{t-12}Yt​=(1−B12)Xt​=Xt​−Xt−12​.

Model evaluation and selection

- •Use information criteria: AIC = −2log⁡L+2k-2\log L + 2k−2logL+2k, BIC = −2log⁡L+klog⁡n-2\log L + k\log n−2logL+klogn, where kkk is number of parameters. Lower values are preferred. Example: Compare AR(1) (k small) vs ARMA(1,1) (k larger); pick model minimizing AIC with parsimony in mind.

Connections to machine learning and further topics

- •State-space models and the Kalman filter generalize ARIMA and provide efficient likelihood computation and handling of missing data; they underpin many time-series ML methods. Recurrent neural networks and sequence models are flexible alternatives but lack statistical interpretability.

Practical pitfalls and tips

- •Over-differencing can destroy structure and induce invertibility issues: only difference to achieve stationarity (use tests like the augmented Dickey–Fuller test).
- •Inspect residuals visually and with tests; small sample sizes make ACF/PACF noisy.
- •Start with simple models (parsimony) and gradually increase complexity.

A short end-to-end numeric illustration

Suppose you have monthly sales series and see a linear upward trend. First difference to remove trend (d=1). The differenced series shows ACF cutting off at lag 1 and PACF decaying: candidate ARIMA(0,1,1). Fit MA(1) on differenced data; estimate θ≈0.5\theta\approx0.5θ≈0.5 and residuals look white. Forecast by integrating predicted differences forward to recover level forecasts. This is the Box–Jenkins loop in action.

In summary, Box–Jenkins ties together stationarity tests, ACF/PACF-guided identification, estimation (Yule–Walker, OLS, ML), and diagnostic checking to produce reliable forecasts. The concrete algebra and numerical examples throughout this lesson show how concepts from Covariance and Correlation and Linear Regression are repurposed to handle temporal dependence and forecasting tasks.

## Worked Examples (3)

### Compute sample ACF for a small series

You observe the series x = [2, 4, 6, 8]. Compute the sample mean, sample autocovariance at lags 0 and 1 using denominator n=4, and the sample autocorrelation at lag 1.

1. Compute sample mean: xˉ=(2+4+6+8)/4=20/4=5\bar x = (2+4+6+8)/4 = 20/4 = 5xˉ=(2+4+6+8)/4=20/4=5.
2. Compute sample autocovariance at lag 0: γ^0=14∑t=14(xt−xˉ)2\hat\gamma\_0 = \frac{1}{4}\sum\_{t=1}^4 (x\_t-\bar x)^2γ^​0​=41​∑t=14​(xt​−xˉ)2. Differences squared: (2-5)^2=9, (4-5)^2=1, (6-5)^2=1, (8-5)^2=9. Sum = 20. So γ^0=20/4=5\hat\gamma\_0 = 20/4 = 5γ^​0​=20/4=5.
3. Compute sample autocovariance at lag 1: γ^1=14∑t=24(xt−xˉ)(xt−1−xˉ)\hat\gamma\_1 = \frac{1}{4}\sum\_{t=2}^4 (x\_t-\bar x)(x\_{t-1}-\bar x)γ^​1​=41​∑t=24​(xt​−xˉ)(xt−1​−xˉ). Terms: (4-5)(2-5)=(-1)(-3)=3, (6-5)(4-5)=(1)(-1)=-1, (8-5)(6-5)=(3)(1)=3. Sum = 5. So γ^1=5/4=1.25\hat\gamma\_1 = 5/4 = 1.25γ^​1​=5/4=1.25.
4. Compute sample autocorrelation at lag 1: ρ^1=γ^1/γ^0=1.25/5=0.25\hat\rho\_1 = \hat\gamma\_1 / \hat\gamma\_0 = 1.25/5 = 0.25ρ^​1​=γ^​1​/γ^​0​=1.25/5=0.25.
5. Summarize: xˉ=5\bar x=5xˉ=5, γ^0=5\hat\gamma\_0=5γ^​0​=5, γ^1=1.25\hat\gamma\_1=1.25γ^​1​=1.25, ρ^1=0.25\hat\rho\_1=0.25ρ^​1​=0.25.

**Insight:** This example shows directly how the sample autocovariance and autocorrelation are computed from data and connects to the Covariance and Correlation prerequisite: lagged pairs play the same role as paired variables in a standard correlation computation.

### Identify AR(1) vs MA(1) from theoretical ACF

Consider two processes: (A) AR(1) with ϕ=0.6\phi=0.6ϕ=0.6 and noise variance σ2=1\sigma^2=1σ2=1, (B) MA(1) with θ=0.5\theta=0.5θ=0.5 and noise variance σ2=1\sigma^2=1σ2=1. Compute theoretical ACF at lags 1,2,3 for both and use these to argue which pattern each would show on an ACF plot.

1. AR(1) theoretical ACF: ρk=ϕk\rho\_k = \phi^kρk​=ϕk.

   Compute numeric values with ϕ=0.6\phi=0.6ϕ=0.6: ρ1=0.6\rho\_1=0.6ρ1​=0.6, ρ2=0.62=0.36\rho\_2=0.6^2=0.36ρ2​=0.62=0.36, ρ3=0.63=0.216\rho\_3=0.6^3=0.216ρ3​=0.63=0.216.
2. MA(1) theoretical ACF: ρ1=θ/(1+θ2)\rho\_1 = \theta/(1+\theta^2)ρ1​=θ/(1+θ2) and ρk=0\rho\_k=0ρk​=0 for k>1k>1k>1.

   Compute numeric values with θ=0.5\theta=0.5θ=0.5: ρ1=0.5/(1+0.25)=0.5/1.25=0.4\rho\_1=0.5/(1+0.25)=0.5/1.25=0.4ρ1​=0.5/(1+0.25)=0.5/1.25=0.4, ρ2=0\rho\_2=0ρ2​=0, ρ3=0\rho\_3=0ρ3​=0.
3. Interpretation: AR(1) ACF decays exponentially (0.6, 0.36, 0.216, ...). MA(1) ACF has a single non-zero lag (0.4 at lag 1) then zeros. So on a sample ACF plot, AR(1) would show gradually decreasing bars while MA(1) would show a significant bar at lag 1 and non-significant bars beyond.
4. Thus, if you observe ACF cutting off after lag 1, MA(1) is likely; if it decays, AR(1) is likely. PACF patterns provide complementary evidence.

**Insight:** This demonstrates the identification rule-of-thumb used in Box–Jenkins: ACF decay vs cut-off helps distinguish AR vs MA behavior. The numeric computations show concrete numbers you would expect in plots.

### Yule–Walker estimation for AR(1)

Using the sample autocovariances from worked example 1 (γ^0=5\hat\gamma\_0=5γ^​0​=5, γ^1=1.25\hat\gamma\_1=1.25γ^​1​=1.25), estimate the AR(1) coefficient ϕ\phiϕ via Yule–Walker and compute the implied variance σ2\sigma^2σ2 of residuals (using σ^2=γ^0−ϕ^γ^1\hat\sigma^2 = \hat\gamma\_0 - \hat\phi\hat\gamma\_1σ^2=γ^​0​−ϕ^​γ^​1​).

1. Yule–Walker for AR(1) gives ϕ=γ1/γ0\phi = \gamma\_1 / \gamma\_0ϕ=γ1​/γ0​. Substitute sample values: ϕ^=1.25/5=0.25\hat\phi = 1.25 / 5 = 0.25ϕ^​=1.25/5=0.25.
2. Compute residual variance estimate: σ^2=γ^0−ϕ^γ^1\hat\sigma^2 = \hat\gamma\_0 - \hat\phi \hat\gamma\_1σ^2=γ^​0​−ϕ^​γ^​1​ (this follows from decomposition of variance for AR(1)). Plug numbers: σ^2=5−0.25⋅1.25\hat\sigma^2 = 5 - 0.25 \cdot 1.25σ^2=5−0.25⋅1.25.
3. Compute $0.25\cdot 1.25 = 0.3125,so, so ,so\hat\sigma^2 = 5 - 0.3125 = 4.6875$.
4. Thus estimated AR(1) model is Xt=0.25Xt−1+εtX\_t = 0.25 X\_{t-1} + \varepsilon\_tXt​=0.25Xt−1​+εt​ with estimated noise variance $4.6875$.
5. Check interpretation: the relatively small sample and short series make estimates noisy; in practice we use longer series and refine via maximum likelihood.

**Insight:** This example shows how Yule–Walker turns autocovariances into AR coefficients. It leverages the link between autocovariance structure and AR parameters and provides a direct, algebraic estimator without optimization.

## Key Takeaways

- ✓

  Stationarity (especially weak stationarity) means constant mean and autocovariance depends only on lag; AR(1) is stationary iff |φ|<1, while a random walk is not.
- ✓

  Autocorrelation (ACF) and partial autocorrelation (PACF) are diagnostic tools: ACF measures linear dependence at lags; PACF measures direct dependence removing intermediates and is computed via regressions (use Linear Regression).
- ✓

  AR(p) models regress current value on past p values; MA(q) models are linear filters of past shocks; ARMA combines them; ARIMA adds differencing to handle nonstationarity.
- ✓

  Identification: AR models imply PACF cuts off after p and ACF decays; MA models imply ACF cuts off after q and PACF decays—use these rules in the Box–Jenkins identification step.
- ✓

  Yule–Walker and OLS give closed-form or simple linear-system estimators for AR parameters; MA and ARMA often require likelihood-based numerical optimization.
- ✓

  Box–Jenkins cycle (identify, estimate, diagnose, forecast) is a practical, iterative approach for building ARIMA-class models with checks via residual analysis and information criteria.
- ✓

  Every computational step builds on Covariance and Correlation (autocovariances) and Linear Regression (estimating lagged relationships or residuals).

## Common Mistakes

- ✗

  Confusing stationarity with no trend: stationarity requires constant variance and autocovariances dependent only on lag, not merely detrending. Example: a process with stable seasonal variance but drifting mean is non-stationary unless differenced.
- ✗

  Using ACF/PACF rules mechanically with very small samples: sample ACF/PACF are noisy for small n; false cutoffs or apparent decays can mislead identification.
- ✗

  Treating MA parameters via OLS directly: MA models involve unobserved shocks εt\varepsilon\_tεt​ so you cannot regress XtX\_tXt​ on past shocks; estimation requires likelihood or specialized methods.
- ✗

  Over-differencing a series: differencing more times than needed can introduce moving-average-like structure and degrade forecasts. Use tests (e.g., ADF) and visual inspection before differencing.

## Practice

easy

Easy: Given a stationary AR(1) process X\_t = 0.8 X\_{t-1} + ε\_t with Var(ε\_t)=1, compute the theoretical autocorrelation ρ\_1 and ρ\_3, and the stationary variance Var(X\_t).

**Hint:** Use ρ\_k = φ^k and Var(X\_t)=σ^2/(1-φ^2).

Show solution

ρ\_1 = 0.8, ρ\_3 = 0.8^3 = 0.512. Var(X\_t) = 1/(1-0.8^2)=1/(1-0.64)=1/0.36 ≈ 2.7778.

medium

Medium: You observe sample autocorrelations \hatρ1=0.45 and \hatρ2=0.2 from a long series (n large). Using the Yule–Walker equations for AR(2), solve approximately for φ1 and φ2 by solving the linear system [\hatρ1,\hatρ2]^T = [[1,\hatρ1],[\hatρ1,1]][φ1,φ2]^T.

**Hint:** Solve the 2×2 linear system: invert the matrix [[1,\hatρ1],[\hatρ1,1]] and multiply by [\hatρ1,\hatρ2].

Show solution

Matrix A = [[1,0.45],[0.45,1]]. Determinant = 1-0.45^2 = 1-0.2025 = 0.7975. Inverse = (1/0.7975)*[[1,-0.45],[-0.45,1]]. Multiply by vector r=[0.45,0.2]: φ = (1/0.7975)*[1*0.45 -0.45*0.2 , -0.45*0.45 +1*0.2] = (1/0.7975)*[0.45-0.09, -0.2025+0.2] = (1/0.7975)*[0.36, -0.0025] ≈ [0.4517, -0.0031]. So φ1≈0.452, φ2≈-0.003.

hard

Hard: Suppose you have monthly data with a strong annual seasonality (period s=12) and a linear upward trend. Outline and justify a Box–Jenkins modeling plan: preprocessing steps, identification choices (including possible seasonal orders), and how you would check residuals. Be explicit about differencing and SARIMA components.

**Hint:** Remove trend via differencing (first difference). Consider seasonal differencing (1-B^12). After differencing, examine ACF/PACF at seasonal lags (12,24) and nonseasonal lags to propose (p,d,q)(P,D,Q)\_12. Use residual ACF/Ljung–Box to check.

Show solution

Plan: 1) Take first difference to remove linear trend: Y\_t = X\_t - X\_{t-1} (d=1). 2) Check seasonality: compute ACF of Y\_t; if strong spikes at lags 12,24,... take seasonal difference (D=1): Z\_t=(1-B^12)Y\_t = (1-B)(1-B^{12})X\_t with total differencing d=1,D=1. 3) On stationary Z\_t, plot ACF/PACF. If ACF shows spike at lag 12 and PACF decays, consider seasonal MA term Q=1; if PACF spikes at lag 12 and ACF decays, consider seasonal AR P=1. For nonseasonal structure, use ACF/PACF at low lags to suggest p and q. For example candidate SARIMA(p,1,q)(P,1,Q)\_12. 4) Fit candidate models (e.g., SARIMA(0,1,1)(0,1,1)\_12), estimate parameters via ML, and inspect residuals: plot residual ACF (should be within ±1.96/√n), perform Ljung–Box test up to lag 24 or more to test joint correlation, check residual histogram/QQ-plot for normality assumption if needed. 5) If diagnostics fail, iterate: try different p,q,P,Q or additional differencing cautiously. 6) Validate via out-of-sample forecast performance. This plan explicitly uses seasonal differencing and SARIMA components and relies on ACF/PACF identification and diagnostic checks.

## Connections

Looking back: This lesson reuses core ideas from your prerequisites. From Covariance and Correlation we extended covariance to autocovariance γk=Cov(Xt,Xt−k)\gamma\_k=\mathrm{Cov}(X\_t,X\_{t-k})γk​=Cov(Xt​,Xt−k​) and defined autocorrelation ρk\rho\_kρk​, which are the numerical heart of the ACF. From Linear Regression we borrowed the idea of projecting onto explanatory variables: PACF at lag k is the coefficient on Xt−kX\_{t-k}Xt−k​ when regressing XtX\_tXt​ on lags 1..k, and OLS/residual calculations underpin AR estimation and diagnostics. Looking forward: mastering these foundations enables work on forecasting (point and interval forecasts), state-space models and the Kalman filter (used in engineering and econometrics), volatility modeling (GARCH models in finance), seasonal modeling (SARIMA), and modern probabilistic sequence models. Many machine learning sequence methods (RNNs, LSTMs) often require careful feature engineering and stationarity-aware preprocessing that derive from the ideas covered here. Specific downstream concepts that require this foundation include: Kalman filtering for state-space inference, GARCH for volatility clustering (which presumes understanding of serial dependence), and structural time series for decomposing trend/seasonality — all use ACF/PACF intuition, differencing/ARMA parametrizations, and residual diagnostics taught in this lesson.

Quality: pending (0.0/5)

[← back to tree](/tech-tree/)[browse all →](/tech-tree/inventory/)
