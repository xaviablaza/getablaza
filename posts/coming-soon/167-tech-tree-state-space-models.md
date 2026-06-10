---
title: State-Space Models
description: Kalman filter, hidden Markov models. Latent state estimation via filtering and smoothing. Forward-backward algorithm.
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
permalink: /tech-tree/state-space-models/
---

[←Back to Tech Tree](/tech-tree/)

[inventory](/tech-tree/inventory/)[coverage](/tech-tree/coverage/)

# State-Space Models

Probability & StatisticsDifficulty: ★★★★☆Depth: 11Unlocks: 2

Kalman filter, hidden Markov models. Latent state estimation via filtering and smoothing. Forward-backward algorithm.

## Prerequisites (3)

[Time Series Foundations? atoms](/tech-tree/time-series-foundations/)[Markov Chains6 atoms](/tech-tree/markov-chains/)[Bayesian Inference5 atoms](/tech-tree/bayesian-inference/)

## Unlocks (1)

[Bayesian Forecastinglvl 5](/tech-tree/bayesian-forecasting/)

Advanced Learning Details

### Graph Position

213

Depth Cost

2

Fan-Out (ROI)

1

Bottleneck Score

11

Chain Length

State-space models let you turn messy time-series and latent-process problems into modular, solvable inference tasks — they are the lingua franca of tracking, econometrics, and probabilistic control.

TL;DR:

State-space models formalize a latent (Markov) state driving observed data; Kalman filtering and the forward-backward (smoothing) algorithms give optimal filtering and retrospective estimates for linear-Gaussian and discrete-HMM cases respectively.

## What Is a State-Space Model?

A state-space model (SSM) is a probabilistic framework that explicitly separates an unobserved internal state (the "latent" or "hidden" state) from noisy observations. This gives two advantages: (1) you model dynamics in the hidden, typically lower-dimensional state, and (2) you perform principled inference on that state using the observation stream. Formally, in discrete time, an SSM is specified by a state (transition) model and an observation (emission) model. Two canonical families are:

- •Linear Gaussian state-space model (LGSSM), often called the Kalman model:

xt=Axt−1+wt,wt∼N(0,Q)x\_t = A x\_{t-1} + w\_t, \quad w\_t \sim \mathcal{N}(0,Q)xt​=Axt−1​+wt​,wt​∼N(0,Q)

yt=Cxt+vt,vt∼N(0,R)y\_t = C x\_t + v\_t, \quad v\_t \sim \mathcal{N}(0,R)yt​=Cxt​+vt​,vt​∼N(0,R)

where xt∈Rnx\_t\in\mathbb{R}^nxt​∈Rn is the latent state, yt∈Rmy\_t\in\mathbb{R}^myt​∈Rm is the observation, AAA and CCC are matrices, and Q,RQ,RQ,R are covariance matrices. Example: an AR(1) process from "Time Series Foundations" can be written as a one-dimensional LGSSM with A=ϕA=\phiA=ϕ, C=1C=1C=1, and suitable Q,RQ,RQ,R; e.g., for AR(1) with ϕ=0.9\phi=0.9ϕ=0.9, process noise variance σw2=1\sigma\_w^2=1σw2​=1, and observation noise variance σv2=2\sigma\_v^2=2σv2​=2, set A=0.9A=0.9A=0.9, Q=1Q=1Q=1, C=1C=1C=1, R=2R=2R=2.

- •Hidden Markov model (HMM), discrete state case:

zt∼p(zt∣zt−1)(Markov chain)z\_t \sim p(z\_t\mid z\_{t-1})\quad\text{(Markov chain)}zt​∼p(zt​∣zt−1​)(Markov chain)

yt∼p(yt∣zt)(emissions)y\_t \sim p(y\_t\mid z\_t)\quad\text{(emissions)}yt​∼p(yt​∣zt​)(emissions)

where ztz\_tzt​ takes values in a finite set. Example: a two-state HMM with transition matrix

T=(0.80.20.10.9)T=\begin{pmatrix}0.8 & 0.2\\ 0.1 & 0.9\end{pmatrix}T=(0.80.1​0.20.9​)

and emission probabilities p(yt∣zt)p(y\_t|z\_t)p(yt​∣zt​) (e.g., categorical or Gaussian) is a simple discrete SSM.

Why build SSMs? From a modeling perspective, many time-series phenomena are naturally explained by a latent quantity evolving over time (hidden economy, object position, unobserved volatility). From an algorithmic perspective, the Markov structure (in the latent space) allows recursive, linear-time inference via dynamic programming: filtering (online) and smoothing (offline). In "Markov Chains" we learned how the memoryless property simplifies analysis; SSMs leverage that same idea: the state at time ttt depends on the past only through xt−1x\_{t-1}xt−1​. In "Bayesian Inference" we learned updating beliefs via priors and likelihoods; the Kalman filter and forward-backward algorithm are recursive Bayesian updates tailored to sequential data.

Key inference questions in SSMs:

- •Filtering: compute p(xt∣y1:t)p(x\_t\mid y\_{1:t})p(xt​∣y1:t​) (belief about current state given past observations). This is online.
- •Prediction: compute p(xt+1∣y1:t)p(x\_{t+1}\mid y\_{1:t})p(xt+1​∣y1:t​) or p(yt+k∣y1:t)p(y\_{t+k}\mid y\_{1:t})p(yt+k​∣y1:t​).
- •Smoothing: compute p(xt∣y1:T)p(x\_t\mid y\_{1:T})p(xt​∣y1:T​) for t<Tt<Tt<T; this uses future information and is an offline pass that reduces uncertainty.
- •Parameter learning: estimate A,C,Q,RA,C,Q,RA,C,Q,R (or transition and emission probabilities in HMMs) from data, typically via Expectation-Maximization (EM) where the E-step uses smoothing to compute sufficient statistics.

Concrete small numeric example to anchor the notation: consider a 1D LGSSM with A=0.9A=0.9A=0.9, Q=1Q=1Q=1, C=1C=1C=1, R=2R=2R=2, initial prior x0∼N(0,1)x\_0\sim\mathcal{N}(0,1)x0​∼N(0,1). You observe y1=1.5y\_1=1.5y1​=1.5. The filtering problem asks for p(x1∣y1)p(x\_1\mid y\_1)p(x1​∣y1​); the Kalman filter will give this in closed form (derived in the next section) and will produce a Gaussian with explicit mean and variance computed from the matrices above.

Intuition: the transition matrix AAA controls how much we trust the past state to predict the next; the process noise QQQ injects uncertainty (how much the state can change unpredictably); the observation matrix CCC and noise RRR govern how informative each measurement is. When RRR is large relative to QQQ, measurements are noisy and the filter relies more on predictions; when QQQ is large, the filter trusts new observations more.

## Core Mechanic 1 — Kalman Filter: Derivation and Worked Mini-Example

The Kalman filter is the closed-form optimal Bayesian filter for linear-Gaussian SSMs. It computes for each ttt the Gaussian posterior p(xt∣y1:t)=N(xt∣t,Pt∣t)p(x\_t\mid y\_{1:t})=\mathcal{N}(x\_{t|t}, P\_{t|t})p(xt​∣y1:t​)=N(xt∣t​,Pt∣t​) by alternating a prediction step and an update (correction) step.

Equations (matrix form).

Prediction (time update):

xt∣t−1=Axt−1∣t−1x\_{t|t-1} = A x\_{t-1|t-1}xt∣t−1​=Axt−1∣t−1​

Pt∣t−1=APt−1∣t−1A⊤+QP\_{t|t-1} = A P\_{t-1|t-1} A^\top + QPt∣t−1​=APt−1∣t−1​A⊤+Q

Update (measurement update):

St=CPt∣t−1C⊤+R(innovation covariance)S\_t = C P\_{t|t-1} C^\top + R\quad\text{(innovation covariance)}St​=CPt∣t−1​C⊤+R(innovation covariance)

Kt=Pt∣t−1C⊤St−1(Kalman gain)K\_t = P\_{t|t-1} C^\top S\_t^{-1}\quad\text{(Kalman gain)}Kt​=Pt∣t−1​C⊤St−1​(Kalman gain)

xt∣t=xt∣t−1+Kt(yt−Cxt∣t−1)x\_{t|t} = x\_{t|t-1} + K\_t (y\_t - C x\_{t|t-1})xt∣t​=xt∣t−1​+Kt​(yt​−Cxt∣t−1​)

Pt∣t=(I−KtC)Pt∣t−1P\_{t|t} = (I - K\_t C) P\_{t|t-1}Pt∣t​=(I−Kt​C)Pt∣t−1​

Derivation idea (sketch): the posterior is proportional to prior times likelihood. With Gaussians, multiply two exponentials gives another Gaussian. Completing the square yields the posterior mean and covariance above; the Kalman gain is the coefficient that balances prior uncertainty with observation uncertainty. This is a direct application of "Bayesian Inference" where the prior is the predictive Gaussian and the likelihood is Gaussian centered at CxtC x\_tCxt​.

Numeric 1D worked mini-example (showing every arithmetic step). Keep everything scalar so matrix operations reduce to multiplication.

Model parameters:

- •A=0.9A=0.9A=0.9, Q=1Q=1Q=1, C=1C=1C=1, R=2R=2R=2.
- •Prior at time 0: x0∣0=0x\_{0|0}=0x0∣0​=0, P0∣0=1P\_{0|0}=1P0∣0​=1.
- •Observation: y1=1.5y\_1=1.5y1​=1.5.

Step 1 — Predict to time 1:

- •x1∣0=Ax0∣0=0.9×0=0x\_{1|0} = A x\_{0|0} = 0.9\times 0 = 0x1∣0​=Ax0∣0​=0.9×0=0.
- •P1∣0=AP0∣0A⊤+Q=0.92×1+1=0.81+1=1.81P\_{1|0} = A P\_{0|0} A^\top + Q = 0.9^2\times 1 + 1 = 0.81 + 1 = 1.81P1∣0​=AP0∣0​A⊤+Q=0.92×1+1=0.81+1=1.81.

Step 2 — Compute innovation covariance and Kalman gain:

- •S1=CP1∣0C⊤+R=1×1.81×1+2=3.81S\_1 = C P\_{1|0} C^\top + R = 1\times 1.81 \times 1 + 2 = 3.81S1​=CP1∣0​C⊤+R=1×1.81×1+2=3.81.
- •K1=P1∣0C⊤/S1=1.81/3.81≈0.475K\_1 = P\_{1|0} C^\top / S\_1 = 1.81 / 3.81 \approx 0.475K1​=P1∣0​C⊤/S1​=1.81/3.81≈0.475. (This is a scalar; we used P/SP/ SP/S.)

Step 3 — Update state mean and covariance with observation y1=1.5y\_1=1.5y1​=1.5:

- •Innovation: y1−Cx1∣0=1.5−0=1.5y\_1 - C x\_{1|0} = 1.5 - 0 = 1.5y1​−Cx1∣0​=1.5−0=1.5.
- •x1∣1=x1∣0+K1⋅1.5=0+0.475×1.5≈0.7125x\_{1|1} = x\_{1|0} + K\_1\cdot 1.5 = 0 + 0.475\times 1.5 \approx 0.7125x1∣1​=x1∣0​+K1​⋅1.5=0+0.475×1.5≈0.7125.
- •P1∣1=(1−K1C)P1∣0=(1−0.475)×1.81=0.525×1.81≈0.95025P\_{1|1} = (1 - K\_1 C) P\_{1|0} = (1 - 0.475)\times 1.81 = 0.525\times 1.81 \approx 0.95025P1∣1​=(1−K1​C)P1∣0​=(1−0.475)×1.81=0.525×1.81≈0.95025.

Interpretation: the posterior mean ≈0.71\approx0.71≈0.71 is between the prediction (0) and the observation (1.5), weighted by the Kalman gain which depends on the relative uncertainties. The posterior variance decreased from $1.81$ (predictive) to $0.95$ (updated): adding the observation reduced uncertainty.

Multiple-step operation and relation to "Time Series Foundations": if you write an AR(1) time series yt=ϕyt−1+ϵty\_t=\phi y\_{t-1}+\epsilon\_tyt​=ϕyt−1​+ϵt​, an equivalent LGSSM can represent the hidden state as the AR(1) latent variable; the Kalman filter then provides the optimal linear minimum MSE estimator for missing values or one-step-ahead forecasts. The Kalman filter is thus the dynamic generalization of the Gaussian conjugate update we saw in "Bayesian Inference".

Important practical points:

- •Numerical stability: the covariance update Pt∣t=(I−KtC)Pt∣t−1P\_{t|t}=(I-K\_t C)P\_{t|t-1}Pt∣t​=(I−Kt​C)Pt∣t−1​ can lose symmetry/positive-definiteness due to rounding; implement stabilized forms such as Joseph form

Pt∣t=(I−KtC)Pt∣t−1(I−KtC)⊤+KtRKt⊤.P\_{t|t}=(I-K\_tC)P\_{t|t-1}(I-K\_tC)^\top + K\_t R K\_t^\top.Pt∣t​=(I−Kt​C)Pt∣t−1​(I−Kt​C)⊤+Kt​RKt⊤​.

- •Initialization matters: poor initial P0∣0P\_{0|0}P0∣0​ or wrong Q,RQ,RQ,R will bias early estimates; often use an uninformative large covariance to reflect prior uncertainty.

The Kalman filter cost per time step is O(n^3) dominated by matrix inverses, but for moderate state dimension it's efficient and exact.

## Core Mechanic 2 — Smoothing: RTS and Forward–Backward

Filtering answers "what is the current state given the past?" Smoothing answers "given the entire dataset, what was the state at time t?" Smoothing reduces posterior variance by incorporating future observations. Two complementary algorithms handle the main SSM families.

1) Rauch–Tung–Striebel (RTS) smoother — linear Gaussian case

After running the Kalman filter forward and storing xt∣tx\_{t|t}xt∣t​, Pt∣tP\_{t|t}Pt∣t​ and the predictive xt+1∣tx\_{t+1|t}xt+1∣t​, Pt+1∣tP\_{t+1|t}Pt+1∣t​ for t=0…T−1t=0\ldots T-1t=0…T−1, the RTS smoother performs a backward pass to compute p(xt∣y1:T)=N(xt∣T,Pt∣T)p(x\_t\mid y\_{1:T})=\mathcal{N}(x\_{t|T}, P\_{t|T})p(xt​∣y1:T​)=N(xt∣T​,Pt∣T​) via

Jt=Pt∣tA⊤Pt+1∣t−1J\_t = P\_{t|t} A^\top P\_{t+1|t}^{-1}Jt​=Pt∣t​A⊤Pt+1∣t−1​

xt∣T=xt∣t+Jt(xt+1∣T−xt+1∣t)x\_{t|T} = x\_{t|t} + J\_t (x\_{t+1|T} - x\_{t+1|t})xt∣T​=xt∣t​+Jt​(xt+1∣T​−xt+1∣t​)

Pt∣T=Pt∣t+Jt(Pt+1∣T−Pt+1∣t)Jt⊤P\_{t|T} = P\_{t|t} + J\_t (P\_{t+1|T} - P\_{t+1|t}) J\_t^\topPt∣T​=Pt∣t​+Jt​(Pt+1∣T​−Pt+1∣t​)Jt⊤​

Derivation sketch: the smoothed estimates follow from the conditional Gaussian identity for jointly Gaussian vectors (xt,xt+1)(x\_t,x\_{t+1})(xt​,xt+1​) conditioned on all observations: one expresses p(xt∣y1:T)=∫p(xt∣xt+1,y1:t)p(xt+1∣y1:T)dxt+1p(x\_t\mid y\_{1:T}) =\int p(x\_t\mid x\_{t+1}, y\_{1:t}) p(x\_{t+1}\mid y\_{1:T}) dx\_{t+1}p(xt​∣y1:T​)=∫p(xt​∣xt+1​,y1:t​)p(xt+1​∣y1:T​)dxt+1​ and uses linear-Gaussian conditional formulas. The matrix JtJ\_tJt​ is the smoothing gain, analogous to KtK\_tKt​ but applied backward.

Numeric RTS example (2-step) to illustrate arithmetic. Use the previous 1D example with parameters A=0.9,Q=1,C=1,R=2A=0.9,Q=1,C=1,R=2A=0.9,Q=1,C=1,R=2 and two observations y1=1.5,y2=0.5y\_1=1.5, y\_2=0.5y1​=1.5,y2​=0.5. From Section 2 we computed x1∣1≈0.7125x\_{1|1}\approx0.7125x1∣1​≈0.7125, P1∣1≈0.95025P\_{1|1}\approx0.95025P1∣1​≈0.95025, and x2∣1=Ax1∣1=0.9×0.7125≈0.64125x\_{2|1}=A x\_{1|1}=0.9\times0.7125\approx0.64125x2∣1​=Ax1∣1​=0.9×0.7125≈0.64125, P2∣1=AP1∣1A⊤+Q=0.92×0.95025+1≈0.7697+1=1.7697P\_{2|1}=A P\_{1|1}A^\top + Q = 0.9^2\times0.95025 + 1 \approx 0.7697 + 1 = 1.7697P2∣1​=AP1∣1​A⊤+Q=0.92×0.95025+1≈0.7697+1=1.7697. After running Kalman update at time 2, suppose we compute x2∣2≈0.55x\_{2|2}\approx0.55x2∣2​≈0.55 and P2∣2≈0.9P\_{2|2}\approx0.9P2∣2​≈0.9 (numbers illustrative). Then backward step for t=1t=1t=1:

- •J1=P1∣1A⊤/P2∣1=0.95025×0.9/1.7697≈0.4837J\_1 = P\_{1|1} A^\top / P\_{2|1} = 0.95025\times 0.9 / 1.7697 \approx 0.4837J1​=P1∣1​A⊤/P2∣1​=0.95025×0.9/1.7697≈0.4837.
- •x1∣2=x1∣1+J1(x2∣2−x2∣1)=0.7125+0.4837(0.55−0.64125)≈0.7125−0.0445≈0.6680x\_{1|2} = x\_{1|1} + J\_1 (x\_{2|2} - x\_{2|1}) = 0.7125 + 0.4837 (0.55 - 0.64125) \approx 0.7125 - 0.0445 \approx 0.6680x1∣2​=x1∣1​+J1​(x2∣2​−x2∣1​)=0.7125+0.4837(0.55−0.64125)≈0.7125−0.0445≈0.6680.
- •P1∣2=P1∣1+J1(P2∣2−P2∣1)J1≈0.95025+0.4837(0.9−1.7697)0.4837≈0.95025−0.201≈0.7492P\_{1|2} = P\_{1|1} + J\_1 (P\_{2|2} - P\_{2|1}) J\_1 \approx 0.95025 + 0.4837 (0.9 - 1.7697) 0.4837 \approx 0.95025 - 0.201 \approx 0.7492P1∣2​=P1∣1​+J1​(P2∣2​−P2∣1​)J1​≈0.95025+0.4837(0.9−1.7697)0.4837≈0.95025−0.201≈0.7492.

The smoothed mean moved toward values that explain future data; variance decreased from $0.95025$ to $0.7492$.

2) Forward–Backward algorithm — discrete HMM case

For finite-state HMMs, smoothing is performed by the forward–backward algorithm (a dynamic-programming factorization). Define the forward variable αt(i)=p(y1:t,zt=i)\alpha\_t(i) = p(y\_{1:t}, z\_t=i)αt​(i)=p(y1:t​,zt​=i) and backward variable βt(i)=p(yt+1:T∣zt=i)\beta\_t(i) = p(y\_{t+1:T} \mid z\_t=i)βt​(i)=p(yt+1:T​∣zt​=i). Then the smoothed state posterior is

γt(i):=p(zt=i∣y1:T)=αt(i)βt(i)∑jαt(j)βt(j).\gamma\_t(i) := p(z\_t=i\mid y\_{1:T}) = \frac{\alpha\_t(i)\beta\_t(i)}{\sum\_j \alpha\_t(j)\beta\_t(j)}.γt​(i):=p(zt​=i∣y1:T​)=∑j​αt​(j)βt​(j)αt​(i)βt​(i)​.

Recursions:

α1(i)=πip(y1∣z1=i),αt+1(j)=p(yt+1∣zt+1=j)∑iαt(i)p(zt+1=j∣zt=i).\alpha\_1(i) = \pi\_i p(y\_1\mid z\_1=i),\quad \alpha\_{t+1}(j)= p(y\_{t+1}\mid z\_{t+1}=j)\sum\_i \alpha\_t(i) p(z\_{t+1}=j\mid z\_t=i).α1​(i)=πi​p(y1​∣z1​=i),αt+1​(j)=p(yt+1​∣zt+1​=j)i∑​αt​(i)p(zt+1​=j∣zt​=i).

βT(i)=1,βt(i)=∑jp(zt+1=j∣zt=i)p(yt+1∣zt+1=j)βt+1(j).\beta\_T(i)=1,\quad \beta\_t(i) = \sum\_j p(z\_{t+1}=j\mid z\_t=i) p(y\_{t+1}\mid z\_{t+1}=j) \beta\_{t+1}(j).βT​(i)=1,βt​(i)=j∑​p(zt+1​=j∣zt​=i)p(yt+1​∣zt+1​=j)βt+1​(j).

Concrete discrete example: two-state HMM with transitions

T=(0.80.20.10.9),π=(0.6,0.4)T=\begin{pmatrix}0.8 & 0.2\\ 0.1 & 0.9\end{pmatrix},\quad \pi=(0.6,0.4)T=(0.80.1​0.20.9​),π=(0.6,0.4)

Emissions: p(yt=H∣z=1)=0.7p(y\_t=H\mid z=1)=0.7p(yt​=H∣z=1)=0.7, p(yt=H∣z=2)=0.3p(y\_t=H\mid z=2)=0.3p(yt​=H∣z=2)=0.3 (H = "High"). Observations: [H, L] where L denotes low with complementary probabilities. Compute α\alphaα forward and β\betaβ backward and then γt\gamma\_tγt​; make sure to renormalize at each step to avoid underflow. Include scaling factors ct=∑iαt(i)c\_t = \sum\_i \alpha\_t(i)ct​=∑i​αt​(i) when implementing for long sequences.

Relationship between the two: both RTS and forward–backward perform the same logical operation (compute posterior over states given all data) but are specialized to linear-Gaussian continuous states and discrete finite states respectively. The backward gains JtJ\_tJt​ and the backward variables βt\beta\_tβt​ play analogous roles.

Smoothing is essential for parameter learning (EM): the E-step requires expected sufficient statistics like E[xtxt⊤]\mathbb{E}[x\_t x\_t^\top]E[xt​xt⊤​] or E[1(zt=i,zt+1=j)]\mathbb{E}[\mathbf{1}(z\_t=i, z\_{t+1}=j)]E[1(zt​=i,zt+1​=j)] which are computed from smoothed marginals and pairwise smoothed distributions (for HMMs, ξt(i,j)=p(zt=i,zt+1=j∣y1:T)\xi\_t(i,j)=p(z\_t=i,z\_{t+1}=j\mid y\_{1:T})ξt​(i,j)=p(zt​=i,zt+1​=j∣y1:T​)).

## Applications and Connections

State-space methods are a crossroads connecting "Time Series Foundations", "Markov Chains", and "Bayesian Inference" to many applied domains. Here are concrete applications, practical considerations, and downstream connections that rely on understanding SSMs.

Major application areas with concrete examples:

- •Tracking and navigation (robotics, aerospace): an aircraft's position and velocity are latent states; radar returns are noisy observations. An LGSSM with constant-velocity dynamics (AAA a block with 1s and timestep multipliers) and small process noise models motion; the Kalman filter provides real-time position estimates. Example: for a 2D constant-velocity model with state x=[x,x˙,y,y˙]⊤x=[x,\dot x, y,\dot y]^\topx=[x,x˙,y,y˙​]⊤, AAA and QQQ are chosen from discrete-time kinematic equations and process acceleration variance. Kalman filter runs at sensor rate to fuse GPS and IMU.

- •Econometrics (state-space ARMA and unobserved components): many macro time series are modeled as combinations of trend and seasonal latent states. The Kalman smoother recovers the trend component; parameter estimation via EM or maximum likelihood (via Kalman-filtered log-likelihood) yields interpretable model parameters (trend variance, cycle frequency). In "Time Series Foundations" we learned ARMA; any ARMA model can be written in state-space form (companion form) and handled by the Kalman filter for missing data or likelihood evaluation.

- •Signal processing and communications: Kalman filters provide optimal linear equalizers and adaptive filters; smoothing is used in offline deconvolution.

- •Finance: stochastic volatility models are often written as nonlinear/non-Gaussian SSMs; particle filters or specialized smoothers are used for inference. The EM algorithm using smoothing can estimate latent volatility parameters.

- •Machine learning and probabilistic modeling: HMMs are the building block of speech recognition (Baum–Welch algorithm = forward–backward EM), bioinformatics (gene prediction), and sequence labeling. Linear-Gaussian SSMs are used in Gaussian process state-space models and as differentiable building blocks in deep learning architectures (e.g., KalmanNet).

Downstream algorithms that require SSM understanding:

- •Expectation–Maximization (EM) for parameter estimation: E-step uses smoothing to compute expectations; M-step updates A,Q,C,RA,Q,C,RA,Q,C,R or HMM transition/emission matrices. Concrete: for LGSSM, the expected sufficient statistics are ∑tE[xtxt⊤]\sum\_t \mathbb{E}[x\_t x\_t^\top]∑t​E[xt​xt⊤​], ∑tE[xtxt−1⊤]\sum\_t \mathbb{E}[x\_t x\_{t-1}^\top]∑t​E[xt​xt−1⊤​], and these are computed by smoothing outputs.

- •Particle filters and sequential Monte Carlo: when dynamics or observations are nonlinear/non-Gaussian, the Kalman filter is not optimal; particle filters approximate the filtering distribution by weighted particles. The theoretical underpinning (sequential importance sampling and resampling) builds on the same Markov/Bayesian filtering logic.

- •Control theory (LQG — linear-quadratic-Gaussian): the Kalman filter provides the optimal state estimator that, combined with an LQR regulator, gives the separation principle: estimation and control decouple. A practical example: autopilot design separates state estimation (Kalman) and control (LQR), each designed using SSM parameters.

Practicalities and numerical issues:

- •Underflow in forward–backward: use log-space or per-step scaling (store ct=∑iαt(i)c\_t=\sum\_i \alpha\_t(i)ct​=∑i​αt​(i) and normalize). Example: in a long HMM, raw αt\alpha\_tαt​ values shrink exponentially; the scaled α^t=αt/ct\hat\alpha\_t=\alpha\_t/c\_tα^t​=αt​/ct​ avoids underflow.

- •Observability and identifiability: not every SSM parameter is recoverable from data. Observability (a linear algebra condition on (A,C)(A,C)(A,C)) ensures the state can be inferred from outputs. Example: if C=[0  0  …  0]C=[0\;0\;\dots\;0]C=[00…0], the state is unobservable no matter how many measurements you collect.

- •Model mismatch: wrong noise covariance assumptions (Q,RQ,RQ,R) bias the Kalman gain. In practice, you may treat QQQ as a tuning parameter or estimate it via EM.

- •Complexity: Kalman filter is O(n^3) per time step; HMM forward–backward is O(S^2 T) where S is number of discrete states; particle filters are O(N T) with sample size N.

Concrete numeric tie-in: the log-likelihood of observations under the LGSSM can be computed incrementally from the Kalman filter via

log⁡p(y1:T)=−12∑t=1T[mlog⁡(2π)+log⁡∣St∣+(yt−Cxt∣t−1)⊤St−1(yt−Cxt∣t−1)],\log p(y\_{1:T}) = -\tfrac{1}{2}\sum\_{t=1}^T \left[ m\log(2\pi) + \log|S\_t| + (y\_t - C x\_{t|t-1})^\top S\_t^{-1} (y\_t - C x\_{t|t-1}) \right],logp(y1:T​)=−21​t=1∑T​[mlog(2π)+log∣St​∣+(yt​−Cxt∣t−1​)⊤St−1​(yt​−Cxt∣t−1​)],

where mmm is the observation dimension. In practice this is used in maximum-likelihood parameter estimation; substitute numeric StS\_tSt​ from the filter each step.

Summary: mastering Kalman filtering and forward–backward smoothing gives you powerful, computationally efficient tools to estimate hidden dynamics and to build higher-level algorithms for learning and control. In the next section (worked examples) we will step through concrete instances to cement arithmetic and intuition.

## Worked Examples (3)

### 1D Kalman Filter Single Update

Parameters: A=0.8A=0.8A=0.8, Q=0.5Q=0.5Q=0.5, C=1C=1C=1, R=1.5R=1.5R=1.5. Prior: x0∣0=0x\_{0|0}=0x0∣0​=0, P0∣0=2P\_{0|0}=2P0∣0​=2. Observation: y1=1.2y\_1=1.2y1​=1.2. Compute x1∣1x\_{1|1}x1∣1​ and P1∣1P\_{1|1}P1∣1​.

1. Prediction: x1∣0=Ax0∣0=0.8×0=0x\_{1|0}=A x\_{0|0}=0.8\times0=0x1∣0​=Ax0∣0​=0.8×0=0.
2. Predictive covariance: P1∣0=AP0∣0A⊤+Q=0.82×2+0.5=1.28+0.5=1.78P\_{1|0}=A P\_{0|0} A^\top + Q = 0.8^2\times 2 + 0.5 = 1.28 + 0.5 = 1.78P1∣0​=AP0∣0​A⊤+Q=0.82×2+0.5=1.28+0.5=1.78.
3. Innovation covariance: S1=CP1∣0C⊤+R=1×1.78+1.5=3.28S\_1 = C P\_{1|0} C^\top + R = 1\times 1.78 + 1.5 = 3.28S1​=CP1∣0​C⊤+R=1×1.78+1.5=3.28.
4. Kalman gain: K1=P1∣0C⊤/S1=1.78/3.28≈0.5439K\_1 = P\_{1|0} C^\top / S\_1 = 1.78 / 3.28 \approx 0.5439K1​=P1∣0​C⊤/S1​=1.78/3.28≈0.5439.
5. Innovation: y1−Cx1∣0=1.2−0=1.2y\_1 - C x\_{1|0} = 1.2 - 0 = 1.2y1​−Cx1∣0​=1.2−0=1.2.
6. Updated mean: x1∣1=x1∣0+K1×1.2=0+0.5439×1.2≈0.6527x\_{1|1} = x\_{1|0} + K\_1 \times 1.2 = 0 + 0.5439 \times 1.2 \approx 0.6527x1∣1​=x1∣0​+K1​×1.2=0+0.5439×1.2≈0.6527.
7. Updated covariance: P1∣1=(1−K1C)P1∣0=(1−0.5439)×1.78≈0.8122P\_{1|1} = (1 - K\_1 C) P\_{1|0} = (1 - 0.5439)\times 1.78 \approx 0.8122P1∣1​=(1−K1​C)P1∣0​=(1−0.5439)×1.78≈0.8122.

**Insight:** This example shows how the Kalman gain depends on the relative sizes of predictive uncertainty P1∣0P\_{1|0}P1∣0​ and measurement noise RRR: larger RRR would reduce K1K\_1K1​, pulling the posterior mean closer to the prediction.

### RTS Smoother for 3-step Linear Gaussian

1D model: A=0.9A=0.9A=0.9, Q=1Q=1Q=1, C=1C=1C=1, R=2R=2R=2. Observations: y1=1.5y\_1=1.5y1​=1.5, y2=0.5y\_2=0.5y2​=0.5, y3=1.0y\_3=1.0y3​=1.0. Start with x0∣0=0x\_{0|0}=0x0∣0​=0, P0∣0=1P\_{0|0}=1P0∣0​=1. Compute x2∣3x\_{2|3}x2∣3​ and P2∣3P\_{2|3}P2∣3​ (smoothed estimates for time 2) using a forward Kalman pass and backward RTS smoothing.

1. Forward pass step 1 (t=1): match Section 2 calculations to get x1∣1≈0.7125x\_{1|1}\approx0.7125x1∣1​≈0.7125, P1∣1≈0.95025P\_{1|1}\approx0.95025P1∣1​≈0.95025, x2∣1=Ax1∣1≈0.64125x\_{2|1}=A x\_{1|1}\approx0.64125x2∣1​=Ax1∣1​≈0.64125, P2∣1=0.92×0.95025+1≈1.7697P\_{2|1}=0.9^2\times0.95025 + 1 \approx1.7697P2∣1​=0.92×0.95025+1≈1.7697.
2. Update at t=2 with y2=0.5y\_2=0.5y2​=0.5: S2=P2∣1+R=1.7697+2=3.7697S\_2 = P\_{2|1}+R = 1.7697 + 2 = 3.7697S2​=P2∣1​+R=1.7697+2=3.7697, K2=1.7697/3.7697≈0.4695K\_2 = 1.7697/3.7697 \approx0.4695K2​=1.7697/3.7697≈0.4695, innovation $0.5 - 0.64125 = -0.14125,so, so ,sox\_{2|2}=0.64125 + 0.4695\times(-0.14125) \approx0.5748$, $P\_{2|2}=(1-K\_2)P\_{2|1}\approx 0.9424$.
3. Predict to t=3: x3∣2=Ax2∣2=0.9×0.5748≈0.5173x\_{3|2}=A x\_{2|2}=0.9\times0.5748\approx0.5173x3∣2​=Ax2∣2​=0.9×0.5748≈0.5173, P3∣2=0.92×0.9424+1≈1.7631P\_{3|2}=0.9^2\times0.9424 + 1 \approx 1.7631P3∣2​=0.92×0.9424+1≈1.7631.
4. Update at t=3 with y3=1.0y\_3=1.0y3​=1.0: S3=1.7631+2=3.7631S\_3 = 1.7631 + 2 = 3.7631S3​=1.7631+2=3.7631, K3=1.7631/3.7631≈0.4687K\_3 = 1.7631/3.7631 \approx0.4687K3​=1.7631/3.7631≈0.4687, innovation $1.0 - 0.5173 = 0.4827,so, so ,sox\_{3|3}=0.5173 + 0.4687\times0.4827 \approx 0.7439$, $P\_{3|3}\approx 0.9418$.
5. Backward RTS for t=2: compute J2=P2∣2A⊤/P3∣2=0.9424×0.9/1.7631≈0.4809J\_2 = P\_{2|2} A^\top / P\_{3|2} = 0.9424\times 0.9 / 1.7631 \approx 0.4809J2​=P2∣2​A⊤/P3∣2​=0.9424×0.9/1.7631≈0.4809.
6. Smoothed mean: x2∣3=x2∣2+J2(x3∣3−x3∣2)=0.5748+0.4809(0.7439−0.5173)≈0.6937x\_{2|3} = x\_{2|2} + J\_2 (x\_{3|3} - x\_{3|2}) = 0.5748 + 0.4809 (0.7439 - 0.5173) \approx 0.6937x2∣3​=x2∣2​+J2​(x3∣3​−x3∣2​)=0.5748+0.4809(0.7439−0.5173)≈0.6937.
7. Smoothed covariance: P2∣3=P2∣2+J2(P3∣3−P3∣2)J2≈0.9424+0.4809(0.9418−1.7631)0.4809≈0.7151P\_{2|3} = P\_{2|2} + J\_2 (P\_{3|3} - P\_{3|2}) J\_2 \approx 0.9424 + 0.4809 (0.9418 - 1.7631) 0.4809 \approx 0.7151P2∣3​=P2∣2​+J2​(P3∣3​−P3∣2​)J2​≈0.9424+0.4809(0.9418−1.7631)0.4809≈0.7151.

**Insight:** Smoothing moved the estimate at t=2 towards values that better explain the later observation at t=3 and reduced variance. This illustrates how future data refines past beliefs.

### Forward–Backward on a Two-State HMM

Two states {1,2}, initial distribution π=(0.5,0.5)\pi=(0.5,0.5)π=(0.5,0.5), transition matrix T=(0.70.30.40.6)T=\begin{pmatrix}0.7&0.3\\0.4&0.6\end{pmatrix}T=(0.70.4​0.30.6​). Emission probabilities for observation O ∈ {A,B}: p(A∣1)=0.8,p(B∣1)=0.2p(A|1)=0.8,p(B|1)=0.2p(A∣1)=0.8,p(B∣1)=0.2 and p(A∣2)=0.3,p(B∣2)=0.7p(A|2)=0.3,p(B|2)=0.7p(A∣2)=0.3,p(B∣2)=0.7. Observed sequence: [A,B]. Compute smoothed marginals γ1\gamma\_1γ1​ and γ2\gamma\_2γ2​.

1. Forward t=1: α1(1)=π1p(A∣1)=0.5×0.8=0.4\alpha\_1(1)=\pi\_1 p(A|1)=0.5\times0.8=0.4α1​(1)=π1​p(A∣1)=0.5×0.8=0.4, α1(2)=0.5×0.3=0.15\alpha\_1(2)=0.5\times0.3=0.15α1​(2)=0.5×0.3=0.15. Normalize by c1=0.55c\_1=0.55c1​=0.55 if desired; unnormalized values suffice for ratios.
2. Forward t=2: compute predictive sums: for state 1: ∑iα1(i)Ti→1=0.4×0.7+0.15×0.4=0.28+0.06=0.34\sum\_i \alpha\_1(i) T\_{i\to1}=0.4\times0.7 + 0.15\times0.4 = 0.28 + 0.06 = 0.34∑i​α1​(i)Ti→1​=0.4×0.7+0.15×0.4=0.28+0.06=0.34. Multiply by emission p(B∣1)=0.2p(B|1)=0.2p(B∣1)=0.2 gives α2(1)=0.068\alpha\_2(1)=0.068α2​(1)=0.068. For state 2: ∑iα1(i)Ti→2=0.4×0.3+0.15×0.6=0.12+0.09=0.21\sum\_i \alpha\_1(i) T\_{i\to2}=0.4\times0.3 + 0.15\times0.6 = 0.12 + 0.09 = 0.21∑i​α1​(i)Ti→2​=0.4×0.3+0.15×0.6=0.12+0.09=0.21. Multiply by emission p(B∣2)=0.7p(B|2)=0.7p(B∣2)=0.7 gives α2(2)=0.147\alpha\_2(2)=0.147α2​(2)=0.147.
3. Backward initialization: β2(1)=β2(2)=1\beta\_2(1)=\beta\_2(2)=1β2​(1)=β2​(2)=1.
4. Backward t=1: β1(1)=∑jT1→jp(y2∣j)β2(j)=0.7×0.2+0.3×0.7=0.14+0.21=0.35\beta\_1(1)=\sum\_j T\_{1\to j} p(y\_2|j) \beta\_2(j) = 0.7\times0.2 + 0.3\times0.7 = 0.14 + 0.21 = 0.35β1​(1)=∑j​T1→j​p(y2​∣j)β2​(j)=0.7×0.2+0.3×0.7=0.14+0.21=0.35. Similarly β1(2)=0.4×0.2+0.6×0.7=0.08+0.42=0.5\beta\_1(2) = 0.4\times0.2 + 0.6\times0.7 = 0.08 + 0.42 = 0.5β1​(2)=0.4×0.2+0.6×0.7=0.08+0.42=0.5.
5. Smoothed marginals: γ1(i)∝α1(i)β1(i)\gamma\_1(i) \propto \alpha\_1(i) \beta\_1(i)γ1​(i)∝α1​(i)β1​(i). Compute numerators: for 1: $0.4\times0.35=0.14$; for 2: $0.15\times0.5=0.075$. Normalize sum $0.215gives gives gives\gamma\_1=(0.14/0.215, 0.075/0.215)\approx(0.651,0.349)$.
6. For t=2: γ2(i)∝α2(i)β2(i)=α2(i)\gamma\_2(i) \propto \alpha\_2(i) \beta\_2(i)=\alpha\_2(i)γ2​(i)∝α2​(i)β2​(i)=α2​(i) since β2=1\beta\_2=1β2​=1. Sum $0.068+0.147=0.215.So. So .So\gamma\_2=(0.068/0.215, 0.147/0.215)\approx(0.316,0.684)$.

**Insight:** The forward–backward algorithm computes exact smoothed posteriors for HMMs in O(S^2T). Scaling/normalization is necessary for long sequences; the same dynamic-programming idea underlies continuous-state smoothers like RTS.

## Key Takeaways

- ✓

  A state-space model separates latent dynamics (state equation) from noisy observations (observation equation), enabling efficient recursive inference.
- ✓

  The Kalman filter provides exact closed-form filtering for linear-Gaussian models via predict/update equations; every formula can be implemented as matrix algebra (with scalar examples above).
- ✓

  Smoothing (RTS for LGSSM, forward–backward for HMMs) uses future observations to reduce uncertainty about past states and provides required expectations for EM parameter learning.
- ✓

  Forward (alpha) recursions are numerically complemented by backward (beta) recursions; normalization/scaling is essential in discrete HMMs to avoid underflow.
- ✓

  State-space representations unify ARMA models and Markov chain ideas: ARMA can be written in companion form and handled by Kalman filtering; HMMs are discrete-state SSMs.
- ✓

  Practical implementations must address numerical stability (Joseph form for covariance updates, scaled forward variables) and identifiability/observability of the model.

## Common Mistakes

- ✗

  Using the naive covariance update Pt∣t=(I−KtC)Pt∣t−1P\_{t|t}=(I-K\_tC)P\_{t|t-1}Pt∣t​=(I−Kt​C)Pt∣t−1​ without considering numerical stability: rounding can break symmetry/positive-definiteness; use the Joseph form when necessary.
- ✗

  Mixing filtering and smoothing indices: applying smoothing equations with 'filtered' quantities at the wrong time (e.g., using xt∣t−1x\_{t|t-1}xt∣t−1​ where xt∣tx\_{t|t}xt∣t​ is required) produces incorrect estimates.
- ✗

  Forgetting to include process noise QQQ: setting Q=0Q=0Q=0 (unless truly known zero) often leads to overconfident estimates and filter divergence when the true process is stochastic.
- ✗

  Not scaling forward variables in HMM forward–backward: naive implementation on long sequences leads to numerical underflow and incorrect normalized probabilities.

## Practice

easy

Easy: Consider a 1D LGSSM with A=0.95A=0.95A=0.95, Q=0.2Q=0.2Q=0.2, C=1C=1C=1, R=0.5R=0.5R=0.5, prior x0∣0=1x\_{0|0}=1x0∣0​=1, P0∣0=0.3P\_{0|0}=0.3P0∣0​=0.3, and observation y1=1.4y\_1=1.4y1​=1.4. Compute x1∣1x\_{1|1}x1∣1​ and P1∣1P\_{1|1}P1∣1​.

**Hint:** Perform the prediction step to get x1∣0x\_{1|0}x1∣0​ and P1∣0P\_{1|0}P1∣0​, then compute S1S\_1S1​, K1K\_1K1​, update mean and covariance.

Show solution

Prediction: x1∣0=0.95×1=0.95x\_{1|0}=0.95\times1=0.95x1∣0​=0.95×1=0.95, P1∣0=0.952×0.3+0.2=0.27075+0.2=0.47075P\_{1|0}=0.95^2\times0.3 + 0.2 = 0.27075 + 0.2 = 0.47075P1∣0​=0.952×0.3+0.2=0.27075+0.2=0.47075. Innovation cov: S1=0.47075+0.5=0.97075S\_1 = 0.47075 + 0.5 = 0.97075S1​=0.47075+0.5=0.97075. Kalman gain: K1=0.47075/0.97075≈0.4850K\_1 = 0.47075 / 0.97075 \approx 0.4850K1​=0.47075/0.97075≈0.4850. Innovation: $1.4 - 0.95 = 0.45.Updatedmean:. Updated mean: .Updatedmean:x\_{1|1}=0.95 + 0.4850\times0.45 \approx 1.1658.Updatedcovariance:. Updated covariance: .Updatedcovariance:P\_{1|1}=(1 - 0.4850)\times0.47075 \approx 0.2426$.

medium

Medium: For an LGSSM, show how the E-step of EM leads to sufficient statistics involving ∑tE[xtxt⊤]\sum\_t \mathbb{E}[x\_t x\_t^\top]∑t​E[xt​xt⊤​] and ∑tE[xtxt−1⊤]\sum\_t \mathbb{E}[x\_t x\_{t-1}^\top]∑t​E[xt​xt−1⊤​], and write closed-form M-step updates for AAA and QQQ (assume C known). Given smoothed means xt∣Tx\_{t|T}xt∣T​ and covariances Pt∣TP\_{t|T}Pt∣T​ and cross-covariances Pt,t−1∣TP\_{t,t-1|T}Pt,t−1∣T​, write formulas for the M-step.

**Hint:** Maximize expected complete-data log-likelihood. The quadratic terms lead to normal equations for A and sample covariances for Q.

Show solution

The M-step (maximize w.r.t. A,Q) yields

Anew=(∑t=1TE[xtxt−1⊤])(∑t=1TE[xt−1xt−1⊤])−1A^{\text{new}} = \left(\sum\_{t=1}^T \mathbb{E}[x\_t x\_{t-1}^\top]\right) \left(\sum\_{t=1}^T \mathbb{E}[x\_{t-1} x\_{t-1}^\top]\right)^{-1}Anew=(t=1∑T​E[xt​xt−1⊤​])(t=1∑T​E[xt−1​xt−1⊤​])−1

where E[xtxt−1⊤]=Pt,t−1∣T+xt∣Txt−1∣T⊤\mathbb{E}[x\_t x\_{t-1}^\top]=P\_{t,t-1|T} + x\_{t|T} x\_{t-1|T}^\topE[xt​xt−1⊤​]=Pt,t−1∣T​+xt∣T​xt−1∣T⊤​ and E[xt−1xt−1⊤]=Pt−1∣T+xt−1∣Txt−1∣T⊤\mathbb{E}[x\_{t-1} x\_{t-1}^\top]=P\_{t-1|T} + x\_{t-1|T} x\_{t-1|T}^\topE[xt−1​xt−1⊤​]=Pt−1∣T​+xt−1∣T​xt−1∣T⊤​. The process noise covariance updates to

Qnew=1T∑t=1T(E[xtxt⊤]−AnewE[xtxt−1⊤]⊤)Q^{\text{new}} = \frac{1}{T}\sum\_{t=1}^T \left(\mathbb{E}[x\_t x\_t^\top] - A^{\text{new}} \mathbb{E}[x\_{t} x\_{t-1}^\top]^\top\right)Qnew=T1​t=1∑T​(E[xt​xt⊤​]−AnewE[xt​xt−1⊤​]⊤)

where E[xtxt⊤]=Pt∣T+xt∣Txt∣T⊤\mathbb{E}[x\_t x\_t^\top]=P\_{t|T} + x\_{t|T} x\_{t|T}^\topE[xt​xt⊤​]=Pt∣T​+xt∣T​xt∣T⊤​. These are implemented with the smoothed moments computed from RTS.

hard

Hard: Convert an AR(2) process yt=1.2yt−1−0.32yt−2+ϵty\_t = 1.2 y\_{t-1} - 0.32 y\_{t-2} + \epsilon\_tyt​=1.2yt−1​−0.32yt−2​+ϵt​ with ϵt∼N(0,0.5)\epsilon\_t\sim\mathcal{N}(0,0.5)ϵt​∼N(0,0.5) into a 2D state-space model in companion form with xt=[yt,yt−1]⊤x\_t=[y\_t, y\_{t-1}]^\topxt​=[yt​,yt−1​]⊤, choose A,C,Q,RA,C,Q,RA,C,Q,R accordingly (assume observations are exact yty\_tyt​), and explain whether the system is observable and how you would apply Kalman smoothing if some yty\_tyt​ are missing.

**Hint:** Companion form places AR coefficients in the first row of A. Process noise enters only in the first component. Observability can be tested via the observability matrix [C; CA]. Missing observations: run Kalman prediction at missing steps and skip update.

Show solution

Companion state: xt=(ytyt−1)x\_t=\begin{pmatrix}y\_t\\ y\_{t-1}\end{pmatrix}xt​=(yt​yt−1​​). Then

A=(1.2−0.3210),C=(10).A=\begin{pmatrix}1.2 & -0.32\\ 1 & 0\end{pmatrix},\quad C=\begin{pmatrix}1 & 0\end{pmatrix}.A=(1.21​−0.320​),C=(1​0​).

Process noise: wtw\_twt​ affects yty\_tyt​ only, so set Q=(0.5000)Q=\begin{pmatrix}0.5 & 0\\0 & 0\end{pmatrix}Q=(0.50​00​). Observation noise R=0R=0R=0 for exact observations. Observability: the observability matrix is

O=(CCA)=(101.2−0.32)\mathcal{O}=\begin{pmatrix}C\\ C A\end{pmatrix} = \begin{pmatrix}1 & 0\\ 1.2 & -0.32\end{pmatrix}O=(CCA​)=(11.2​0−0.32​)

which has determinant −0.32≠0-0.32\neq0−0.32=0, so full rank and system is observable. For missing yty\_tyt​ (say at time k), run the prediction step to get xk∣k−1x\_{k|k-1}xk∣k−1​ and Pk∣k−1P\_{k|k-1}Pk∣k−1​, but skip the update (equivalently set R=∞R=\inftyR=∞); continue predictions until an observation appears, then resume updates. For smoothing, run the RTS backward pass using stored predictions and filtered estimates; missing observations simply mean the corresponding filtered step equals the predictive step.

## Connections

Looking backward: this lesson builds directly on "Time Series Foundations" by showing that ARMA and ARIMA models can be cast as state-space systems (companion form) and treated with Kalman filtering for forecasting and missing-data handling; it relies on the Markov property from "Markov Chains" to enable recursive decomposition; and it uses the update logic from "Bayesian Inference" (prior × likelihood -> posterior), specialized in closed-form for Gaussians. Looking forward: mastering Kalman/RTS and forward–backward enables EM-based parameter estimation (Baum–Welch for HMMs, EM for LGSSMs), sequential Monte Carlo and particle filtering for nonlinear/non-Gaussian models, and model-based control (LQG). Concrete downstream topics that require this material include system identification, SLAM in robotics, stochastic optimal control, variational and Monte Carlo inference in time series, and modern state-space neural architectures (e.g., deep state-space models). Understanding observability/identifiability conditions from linear algebra and the numerical stability techniques shown here is essential before deploying these methods in real systems.

Quality: pending (0.0/5)

[← back to tree](/tech-tree/)[browse all →](/tech-tree/inventory/)
