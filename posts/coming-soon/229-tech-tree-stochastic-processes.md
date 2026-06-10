---
title: Stochastic Processes
description: Poisson processes, Brownian motion, Wiener process. Continuous-time stochastic models. Ito calculus foundations.
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
permalink: /tech-tree/stochastic-processes/
---

[←Back to Tech Tree](/tech-tree/)

[inventory](/tech-tree/inventory/)[coverage](/tech-tree/coverage/)

# Stochastic Processes

Probability & StatisticsDifficulty: ★★★★☆Depth: 6Unlocks: 0

Poisson processes, Brownian motion, Wiener process. Continuous-time stochastic models. Ito calculus foundations.

## Prerequisites (3)

[Markov Chains6 atoms](/tech-tree/markov-chains/)[Common Distributions6 atoms](/tech-tree/common-distributions/)[Integrals6 atoms](/tech-tree/integrals-basic/)

## Referenced by (3)

Where this concept shows up in the operating-finance and personal-finance graphs.

### From Business (3)

[VolatilityBusiness

Geometric Brownian motion models asset prices with a volatility parameter (sigma in dS = mu\*S\*dt + sigma\*S\*dW). Ito calculus is the mathematical framework for continuous-time volatility modeling](/business/volatility/)[optionsBusiness

Brownian motion and Ito calculus are the literal mathematical foundation of options pricing (Black-Scholes derives from geometric Brownian motion of the underlying asset)](/business/options/)[Option PricingBusiness

Geometric Brownian motion and Ito calculus are the direct mathematical foundation of Black-Scholes; the entire derivation rests on modeling the underlying as a continuous-time stochastic process and applying Ito's lemma to obtain the pricing PDE](/business/option-pricing/)

Advanced Learning Details

### Graph Position

115

Depth Cost

0

Fan-Out (ROI)

0

Bottleneck Score

6

Chain Length

Random events in time and noisy continuous signals are everywhere: from phone-call arrivals to stock prices and particle diffusion — stochastic processes give the precise language and tools to model and analyse them.

TL;DR:

Stochastic processes study time-indexed random phenomena; Poisson processes model random discrete events, Brownian/Wiener processes model continuous Gaussian noise, and Ito calculus provides the integration and chain rule needed to manipulate continuous-time stochastic differential equations (SDEs).

## What Is a Stochastic Process?

A stochastic process is a collection of random variables indexed by time: {Xt}t∈T\{X\_t\}\_{t\in T}{Xt​}t∈T​, where TTT is typically {0,1,2,… }\{0,1,2,\dots\}{0,1,2,…} (discrete time) or an interval [0,∞)[0,\infty)[0,∞) (continuous time). Intuitively, a stochastic process describes the evolution of a random system observed at different times. Two canonical continuous-time families are Poisson processes (jump/counting processes) and Brownian/Wiener processes (continuous-path Gaussian noise).

Why study these two? Poisson processes capture "events" that occur at random times (phone calls, earthquakes), while Brownian motion captures the accumulation of tiny, independent random disturbances (particle diffusion, financial returns at fine time scales). They also form building blocks for more complicated continuous-time models (jump-diffusions, renewal processes, SDEs) used across queueing, finance, physics and engineering.

Connection to prerequisites

- •In Markov Chains, we learned about memoryless dynamics (the Markov property) and transition matrices. Many continuous-time processes inherit a memoryless property (e.g., exponential interarrival times in Poisson processes) and are continuous-time Markov processes.
- •In Common Distributions, we learned the Poisson, exponential and normal laws; these are the marginal/increment distributions for Poisson and Wiener processes.
- •In Integrals, we learned Riemann sums and limits; in continuous-time stochastic calculus we use mean-square limits of Riemann-type sums to define stochastic integrals.

Poisson process — definition and intuition

A counting process N(t)N(t)N(t) is a Poisson process with rate λ>0\lambda>0λ>0 if:

1) N(0)=0N(0)=0N(0)=0.

2) It has independent increments: for $0\le s<t$, $N(t)-N(s)isindependentofthepastuptotime is independent of the past up to time isindependentofthepastuptotimes$ (this is a continuous-time analog of the Markov property learned in Markov Chains).

3) It has stationary increments: distribution depends only on t−st-st−s.

4) P(N(h)=1)=λh+o(h)P(N(h)=1)=\lambda h+o(h)P(N(h)=1)=λh+o(h), P(N(h)≥2)=o(h)P(N(h)\ge2)=o(h)P(N(h)≥2)=o(h) as h↓0h\downarrow0h↓0 (no multiple jumps in infinitesimal time).

The exact distribution: for t>0t>0t>0,

P(N(t)=k)=e−λt(λt)kk!.P(N(t)=k)=e^{-\lambda t}\frac{(\lambda t)^k}{k!}.P(N(t)=k)=e−λtk!(λt)k​.

Concrete numeric example: with λ=3\lambda=3λ=3 events/hour and t=2t=2t=2 hours, N(2)∼Poisson(6)N(2)\sim\mathrm{Poisson}(6)N(2)∼Poisson(6) so

P(N(2)=5)=e−6655!≈0.1606.P(N(2)=5)=e^{-6}\frac{6^5}{5!}\approx 0.1606.P(N(2)=5)=e−65!65​≈0.1606.

Interarrival times T1,T2,…T\_1,T\_2,\dotsT1​,T2​,… are iid exponential(λ)(\lambda)(λ); e.g., with λ=3\lambda=3λ=3, P(T1>1)=e−3⋅1≈0.0498P(T\_1>1) = e^{-3\cdot1}\approx 0.0498P(T1​>1)=e−3⋅1≈0.0498 (probability the first event takes more than 1 hour).

Brownian motion / Wiener process — definition and intuition

A standard Brownian motion (or Wiener process) {Wt}t≥0\{W\_t\}\_{t\ge0}{Wt​}t≥0​ satisfies:

1) W0=0W\_0=0W0​=0.

2) Independent increments.

3) Stationary Gaussian increments: Wt−Ws∼N(0,t−s)W\_t-W\_s\sim N(0, t-s)Wt​−Ws​∼N(0,t−s) for t>st>st>s.

4) Almost surely continuous paths.

This process is the central continuous-time Gaussian model and arises as a scaling limit of random walks (Donsker's invariance principle). Numeric example: W2−W1∼N(0,1)W\_2-W\_1\sim N(0,1)W2​−W1​∼N(0,1), so P(∣W2−W1∣>1.96)≈0.05P(|W\_2-W\_1|>1.96)\approx0.05P(∣W2​−W1​∣>1.96)≈0.05.

Key qualitative facts:

- •Scalability: aWt/a2aW\_{t/a^2}aWt/a2​ is also Brownian motion (diffusive scaling).
- •Paths are a.s. nowhere differentiable, but of finite quadratic variation: the sum of squared increments over a partition of [0,t][0,t][0,t] tends to ttt.

Continuous-time stochastic models

Two canonical classes: pure jump (Poisson) and continuous diffusion (Brownian). Real-world models often combine both (jump-diffusions). The mathematical machinery to manipulate SDEs driven by Brownian motion is Ito calculus, which modifies the ordinary chain rule to account for the quadratic variation of Brownian paths.

This section sets the stage: the next sections derive core formulas for Poisson processes and Brownian/Ito calculus and show worked examples.

## Core Mechanic 1: Poisson Processes — distributions, interarrivals, thinning and superposition

Distribution and derivation (binomial limit)

A standard construction shows the Poisson law as the limit of Binomial(n,pn)(n,p\_n)(n,pn​) with pn=λ/np\_n=\lambda/npn​=λ/n and n→∞n\to\inftyn→∞: for fixed kkk,

(nk)pnk(1−pn)n−k→e−λλkk!.\binom{n}{k}p\_n^k(1-p\_n)^{n-k}\to e^{-\lambda}\frac{\lambda^k}{k!}.(kn​)pnk​(1−pn​)n−k→e−λk!λk​.

Concrete numeric check: take λ=2\lambda=2λ=2, n=1000n=1000n=1000, pn=0.002p\_n=0.002pn​=0.002. The probability of k=0k=0k=0 is approximately (1−0.002)1000≈e−2≈0.1353(1-0.002)^{1000}\approx e^{-2}\approx0.1353(1−0.002)1000≈e−2≈0.1353.

Interarrival times and memoryless property

From the Poisson process with rate λ\lambdaλ the waiting time until the first event T1T\_1T1​ satisfies

P(T1>t)=P(N(t)=0)=e−λt,P(T\_1>t)=P(N(t)=0)=e^{-\lambda t},P(T1​>t)=P(N(t)=0)=e−λt,

so T1∼Exp(λ)T\_1\sim\mathrm{Exp}(\lambda)T1​∼Exp(λ). Exponential distributions are memoryless: P(T1>t+s∣T1>t)=P(T1>s)P(T\_1>t+s\mid T\_1>t)=P(T\_1>s)P(T1​>t+s∣T1​>t)=P(T1​>s). In Markov Chains, we saw discrete memoryless geometric waiting times; exponential is the continuous analogue.

Order statistics representation

Given N(t)=nN(t)=nN(t)=n, the nnn arrival times conditional on N(t)=nN(t)=nN(t)=n are distributed as the order statistics of nnn iid Uniform(0,t)(0,t)(0,t) variables. Example: with λ=3\lambda=3λ=3, t=2t=2t=2 and conditioning on N(2)=2N(2)=2N(2)=2, the two arrival times have joint density equal to $2!/2^2$ on $0< u\_1<u\_2<2$; marginally each arrival is likely near the center.

Superposition and thinning

- •Superposition: if N1,N2N\_1,N\_2N1​,N2​ are independent Poisson processes with rates λ1,λ2\lambda\_1,\lambda\_2λ1​,λ2​, then N=N1+N2N=N\_1+N\_2N=N1​+N2​ is Poisson(λ1+λ2)(\lambda\_1+\lambda\_2)(λ1​+λ2​).

Numeric example: merging two independent streams at rates 2 and 5 per hour yields a Poisson rate 7 per hour.

- •Thinning: each arrival of a Poisson(λ)(\lambda)(λ) process is kept independently with probability ppp to produce a sub-process; the kept events form Poisson(pλ)(p\lambda)(pλ) and the discarded ones Poisson((1−p)λ)((1-p)\lambda)((1−p)λ), independent.

Numeric example: thinning with p=0.3p=0.3p=0.3 a Poisson process with λ=10\lambda=10λ=10 gives a kept process of rate $3$.

Moment generating and PGF

The probability generating function (PGF) for N(t)N(t)N(t) is

GN(s)=E[sN(t)]=exp⁡(λt(s−1)).G\_N(s)=E[s^{N(t)}]=\exp\big(\lambda t(s-1)\big).GN​(s)=E[sN(t)]=exp(λt(s−1)).

Numeric example: with λ=4\lambda=4λ=4, t=0.5t=0.5t=0.5, GN(0.5)=exp⁡(4⋅0.5(0.5−1))=exp⁡(2(−0.5))=e−1≈0.3679G\_N(0.5)=\exp(4\cdot0.5(0.5-1))=\exp(2(-0.5))=e^{-1}\approx0.3679GN​(0.5)=exp(4⋅0.5(0.5−1))=exp(2(−0.5))=e−1≈0.3679.

A simple applied calculation — probability of at least k events

Question: rate λ=2\lambda=2λ=2 per hour, time t=3t=3t=3 hours. What is P(N(3)≥3)P(N(3)\ge3)P(N(3)≥3)?

Solution: N(3)∼Poisson(6)N(3)\sim\mathrm{Poisson}(6)N(3)∼Poisson(6), so

P(N(3)≥3)=1−∑k=02e−66kk!=1−e−6(1+6+362)≈1−e−6(1+6+18)≈1−e−6⋅25≈1−0.002478⋅25≈0.9380.P(N(3)\ge3)=1-\sum\_{k=0}^2 e^{-6}\frac{6^k}{k!}=1- e^{-6}\left(1+6+\frac{36}{2}\right)\approx1- e^{-6}(1+6+18)\approx1- e^{-6}\cdot25\approx 1-0.002478\cdot25\approx 0.9380.P(N(3)≥3)=1−k=0∑2​e−6k!6k​=1−e−6(1+6+236​)≈1−e−6(1+6+18)≈1−e−6⋅25≈1−0.002478⋅25≈0.9380.

Generator viewpoint (continuous-time Markov chains)

For a pure birth Poisson process (counting upward by ones), its forward generator acting on bounded functions f:Z≥0→Rf:\mathbb{Z}\_{\ge0}\to\mathbb{R}f:Z≥0​→R is

(Lf)(n)=λ(f(n+1)−f(n)).(\mathcal{L}f)(n)=\lambda\big(f(n+1)-f(n)\big).(Lf)(n)=λ(f(n+1)−f(n)).

This mirrors the discrete Markov Chains generator learned earlier, now with rate λ\lambdaλ for jumps. For example, choose f(n)=nf(n)=nf(n)=n. Then (Lf)(n)=λ(\mathcal{L}f)(n)=\lambda(Lf)(n)=λ and solves the ODE dE[Nt]/dt=E[(Lf)(Nt)]=λdE[N\_t]/dt=E[(\mathcal{L}f)(N\_t)]=\lambdadE[Nt​]/dt=E[(Lf)(Nt​)]=λ, consistent with E[Nt]=λtE[N\_t]=\lambda tE[Nt​]=λt.

Takeaway from this section: Poisson processes give a clean, tractable model for random discrete events; many useful transformations (conditioning, thinning, superposition) are exact and have simple probabilistic proofs that rely on independent and stationary increments and the exponential memoryless property. All formulas above had concrete numeric instantiations to make computation immediate.

## Core Mechanic 2: Brownian Motion, Quadratic Variation, and Ito Calculus

Brownian motion (Wiener process) recap and basic computations

Recall WtW\_tWt​ is standard Brownian motion with independent stationary Gaussian increments: Wt−Ws∼N(0,t−s)W\_t-W\_s\sim N(0,t-s)Wt​−Ws​∼N(0,t−s). Key moment: E[Wt]=0E[W\_t]=0E[Wt​]=0, Var(Wt)=t\mathrm{Var}(W\_t)=tVar(Wt​)=t. Concrete numeric example: for t=4t=4t=4, W4∼N(0,4)W\_4\sim N(0,4)W4​∼N(0,4) so P(∣W4∣>2)=P(∣N(0,1)∣>1)≈0.3173P(|W\_4|>2) = P(|N(0,1)|>1)\approx0.3173P(∣W4​∣>2)=P(∣N(0,1)∣>1)≈0.3173 because $2/\sqrt{4}=1$.

Quadratic variation — the source of Ito's extra term

Take a partition Πn={0=t0<t1<⋯<tn=t}\Pi\_n=\{0=t\_0<t\_1<\dots<t\_n=t\}Πn​={0=t0​<t1​<⋯<tn​=t} with mesh max⁡(ti+1−ti)→0\max(t\_{i+1}-t\_i)\to0max(ti+1​−ti​)→0. Define the quadratic variation along the partition:

Q(Πn)=∑i=0n−1(Wti+1−Wti)2.Q(\Pi\_n)=\sum\_{i=0}^{n-1}\big(W\_{t\_{i+1}}-W\_{t\_i}\big)^2.Q(Πn​)=i=0∑n−1​(Wti+1​​−Wti​​)2.

Because increments are independent with variance ti+1−tit\_{i+1}-t\_iti+1​−ti​, we have

E[Q(Πn)]=∑i(ti+1−ti)=t.E[Q(\Pi\_n)]=\sum\_{i}(t\_{i+1}-t\_i)=t.E[Q(Πn​)]=i∑​(ti+1​−ti​)=t.

Also Var(Q(Πn))→0\mathrm{Var}(Q(\Pi\_n))\to0Var(Q(Πn​))→0 as mesh shrinks, so Q(Πn)→tQ(\Pi\_n)\to tQ(Πn​)→t in probability and almost surely along appropriate subsequences. Concrete numeric check: take uniform partition into 100 intervals on [0,1][0,1][0,1]; each increment has variance $0.01$, expected sum of squares is 1.

This nonzero quadratic variation (unlike smooth paths where it is 0) causes Ito calculus to acquire an extra term relative to ordinary calculus.

Ito integral — definition sketch

Let {ϕ(t)}\{\phi(t)\}{ϕ(t)} be a predictable process (non-anticipating, i.e., depends only on the past). For simple processes that are piecewise constant on partitions, define

In=∑i=0n−1ϕ(ti)(Wti+1−Wti).I\_n=\sum\_{i=0}^{n-1} \phi(t\_i)\big(W\_{t\_{i+1}}-W\_{t\_i}\big).In​=i=0∑n−1​ϕ(ti​)(Wti+1​​−Wti​​).

The Ito integral is the mean-square limit as the mesh goes to zero:

∫0tϕ(s) dWs:=lim⁡mesh→0In\int\_0^t \phi(s)\,dW\_s := \lim\_{\text{mesh}\to0} I\_n∫0t​ϕ(s)dWs​:=mesh→0lim​In​

with convergence in L^2. Example: if ϕ(s)=1\phi(s)=1ϕ(s)=1 constant, then the integral is WtW\_tWt​ itself: ∫0t1 dWs=Wt\int\_0^t 1\,dW\_s=W\_t∫0t​1dWs​=Wt​.

Isometry and computations

The Ito isometry gives

E[(∫0tϕ(s) dWs)2]=E[∫0tϕ(s)2 ds].E\left[\left(\int\_0^t \phi(s)\,dW\_s\right)^2\right]=E\left[\int\_0^t \phi(s)^2\,ds\right].E[(∫0t​ϕ(s)dWs​)2]=E[∫0t​ϕ(s)2ds].

Numeric example: if ϕ(s)=2\phi(s)=2ϕ(s)=2 constant on [0,1][0,1][0,1], then E[(∫012 dWs)2]=E[∫014 ds]=4E[(\int\_0^1 2\,dW\_s)^2]=E[\int\_0^1 4\,ds]=4E[(∫01​2dWs​)2]=E[∫01​4ds]=4. Indeed ∫012 dWs∼N(0,4)\int\_0^1 2\,dW\_s\sim N(0,4)∫01​2dWs​∼N(0,4).

Ito's formula (stochastic chain rule)

If XtX\_tXt​ solves an SDE

dXt=a(t,Xt) dt+b(t,Xt) dWtdX\_t = a(t,X\_t)\,dt + b(t,X\_t)\,dW\_tdXt​=a(t,Xt​)dt+b(t,Xt​)dWt​

and f(t,x)f(t,x)f(t,x) is C1,2C^{1,2}C1,2 (once differentiable in ttt, twice in xxx), then

df(t,Xt)=(∂tf+a∂xf+12b2∂xxf)(t,Xt) dt+(b∂xf)(t,Xt) dWt.df(t,X\_t) = \left(\partial\_t f + a\partial\_x f + \tfrac12 b^2 \partial\_{xx}f\right)(t,X\_t)\,dt + (b\partial\_x f)(t,X\_t)\,dW\_t.df(t,Xt​)=(∂t​f+a∂x​f+21​b2∂xx​f)(t,Xt​)dt+(b∂x​f)(t,Xt​)dWt​.

Note the 12b2∂xxf\tfrac12 b^2 \partial\_{xx}f21​b2∂xx​f term coming from quadratic variation. Concrete numeric application: let f(x)=x2f(x)=x^2f(x)=x2 and Xt=WtX\_t=W\_tXt​=Wt​ (so a=0,b=1a=0,b=1a=0,b=1). Then Ito's formula yields

d(Wt2)=2Wt dWt+1 dt.d(W\_t^2) = 2W\_t\,dW\_t + 1\,dt.d(Wt2​)=2Wt​dWt​+1dt.

Take expectation to get dE[Wt2]=dtdE[W\_t^2]=dtdE[Wt2​]=dt, so E[Wt2]=tE[W\_t^2]=tE[Wt2​]=t, matching the variance property. Numeric check: at t=3t=3t=3, E[W32]=3E[W\_3^2]=3E[W32​]=3.

Proof sketch of Ito's formula for f(x)f(x)f(x) (time-homogeneous case)

Use Taylor expansion on increments:

f(Xt+Δt)−f(Xt)≈f′(Xt)ΔXt+12f′′(Xt)(ΔXt)2+o((ΔXt)2).f(X\_{t+\Delta t})-f(X\_t) \approx f'(X\_t)\Delta X\_t + \tfrac12 f''(X\_t)(\Delta X\_t)^2 + o((\Delta X\_t)^2).f(Xt+Δt​)−f(Xt​)≈f′(Xt​)ΔXt​+21​f′′(Xt​)(ΔXt​)2+o((ΔXt​)2).

For ΔXt=aΔt+bΔWt\Delta X\_t = a\Delta t + b\Delta W\_tΔXt​=aΔt+bΔWt​, the linear term gives f′(Xt)(aΔt+bΔWt)f'(X\_t)(a\Delta t + b\Delta W\_t)f′(Xt​)(aΔt+bΔWt​); the quadratic term yields 12f′′(Xt)b2(ΔWt)2\tfrac12 f''(X\_t)b^2(\Delta W\_t)^221​f′′(Xt​)b2(ΔWt​)2. But (ΔWt)2≈Δt(\Delta W\_t)^2\approx \Delta t(ΔWt​)2≈Δt (quadratic variation), so the second-order term contributes 12b2f′′(Xt)Δt\tfrac12 b^2 f''(X\_t)\Delta t21​b2f′′(Xt​)Δt. Higher-order terms vanish in the limit because ΔWt=O(Δt)\Delta W\_t = O(\sqrt{\Delta t})ΔWt​=O(Δt​).

Martingales and exponential martingales

A useful family: for constant θ\thetaθ, the process

Mt=exp⁡(θWt−12θ2t)M\_t = \exp\left(\theta W\_t - \tfrac12\theta^2 t\right)Mt​=exp(θWt​−21​θ2t)

is a martingale. Numeric example: with θ=1\theta=1θ=1 and t=2t=2t=2, E[M2]=1E[M\_2]=1E[M2​]=1 and M2=exp⁡(W2−1)M\_2=\exp(W\_2 - 1)M2​=exp(W2​−1).

SDE example and solution technique

Consider the linear SDE (Ornstein-Uhlenbeck variant) for constants θ,σ\theta,\sigmaθ,σ:

dXt=−θXt dt+σ dWt,X0=x0.dX\_t = -\theta X\_t\,dt + \sigma\,dW\_t,\qquad X\_0=x\_0.dXt​=−θXt​dt+σdWt​,X0​=x0​.

The integrating factor solution (variation of constants) yields

Xt=x0e−θt+σ∫0te−θ(t−s) dWs.X\_t = x\_0 e^{-\theta t} + \sigma\int\_0^t e^{-\theta (t-s)}\,dW\_s.Xt​=x0​e−θt+σ∫0t​e−θ(t−s)dWs​.

Numeric example: with θ=1,σ=2,x0=1,t=1\theta=1,\sigma=2,x\_0=1,t=1θ=1,σ=2,x0​=1,t=1, the expectation is E[X1]=e−1≈0.3679E[X\_1]= e^{-1}\approx0.3679E[X1​]=e−1≈0.3679 and variance

Var(X1)=σ2∫01e−2(1−s) ds=4∫01e−2(1−s) ds=4∫01e−2udu=4(1−e−2)/2=2(1−e−2)≈2(1−0.1353)≈1.7294.\mathrm{Var}(X\_1)=\sigma^2\int\_0^1 e^{-2(1-s)}\,ds=4\int\_0^1 e^{-2(1-s)}\,ds=4\int\_0^1 e^{-2u}du=4(1-e^{-2})/2 =2(1-e^{-2})\approx2(1-0.1353)\approx1.7294.Var(X1​)=σ2∫01​e−2(1−s)ds=4∫01​e−2(1−s)ds=4∫01​e−2udu=4(1−e−2)/2=2(1−e−2)≈2(1−0.1353)≈1.7294.

Takeaway: Ito calculus alters the ordinary calculus chain rule by a quadratic-variation term. The Ito integral is a mean-square limit defined for non-anticipating integrands, and Ito's formula is the workhorse for manipulating functions of SDE solutions.

## Applications and Connections: where these tools go and why they matter

Black–Scholes and quantitative finance

One of the clearest applications is option pricing. Model a stock price by the geometric SDE

dSt=μSt dt+σSt dWt,S0=s0.dS\_t = \mu S\_t\,dt + \sigma S\_t\,dW\_t,\qquad S\_0=s\_0.dSt​=μSt​dt+σSt​dWt​,S0​=s0​.

Ito's formula applied to log⁡St\log S\_tlogSt​ gives

dlog⁡St=(μ−12σ2)dt+σ dWt,d\log S\_t = \left(\mu - \tfrac12\sigma^2\right)dt + \sigma\,dW\_t,dlogSt​=(μ−21​σ2)dt+σdWt​,

so the explicit solution is

St=s0exp⁡((μ−12σ2)t+σWt).S\_t = s\_0\exp\left(\left(\mu - \tfrac12\sigma^2\right)t + \sigma W\_t\right).St​=s0​exp((μ−21​σ2)t+σWt​).

Concrete numeric example: take s0=100s\_0=100s0​=100, μ=0.05\mu=0.05μ=0.05, σ=0.2\sigma=0.2σ=0.2, t=1t=1t=1 year. Then

E[S1]=s0eμt=100e0.05≈100⋅1.05127≈105.127.E[S\_1] = s\_0 e^{\mu t} = 100e^{0.05}\approx100\cdot1.05127\approx 105.127.E[S1​]=s0​eμt=100e0.05≈100⋅1.05127≈105.127.

Black–Scholes uses risk-neutral pricing (μ\muμ replaced by risk-free rate rrr) and properties of lognormal distributions to price European options analytically.

Queueing, telecommunications and reliability

Poisson processes are the standard model for arrival processes in queues (e.g., M/M/1 queue). Key performance measures — waiting times and queue lengths — are derived from Poisson/exponential properties. Example numerical calculation: with arrival rate λ=5\lambda=5λ=5/hr and service rate μ=6\mu=6μ=6/hr, utilization ρ=λ/μ≈0.833\rho=\lambda/\mu\approx0.833ρ=λ/μ≈0.833; the stationary average number in system for M/M/1 is ρ/(1−ρ)≈5\rho/(1-\rho)\approx5ρ/(1−ρ)≈5 customers.

Physics and diffusion

Brownian motion models particle diffusion: the heat equation is the forward equation (Fokker–Planck) for the probability density of Brownian motion. The diffusion constant ties Var(Wt)\mathrm{Var}(W\_t)Var(Wt​) to physical diffusivity.

Stochastic control, filtering and estimation

Ito calculus enables stochastic optimal control (Hamilton–Jacobi–Bellman PDEs) and stochastic filtering (Kalman–Bucy filter for linear Gaussian SDEs). For example, the linear SDE + Gaussian noise assumptions produce closed-form filters because all conditional distributions remain Gaussian.

Statistics for stochastic processes

Parameter estimation for rates λ\lambdaλ in Poisson models or drift/diffusion coefficients in SDEs uses likelihoods based on increments and Girsanov transformations. For example, by observing a Poisson process on [0,T][0,T][0,T] with N(T)=nN(T)=nN(T)=n, the MLE for λ\lambdaλ is λ^=n/T\hat{\lambda}=n/Tλ^=n/T.

Machine learning and stochastic optimisation

Stochastic gradient methods can be viewed as discrete-time stochastic processes; diffusion limits lead to SDE approximations describing algorithm behaviour and escape probabilities from basins of attraction.

Hybrid models and jump-diffusions

Real applications often combine Poisson jumps and Brownian diffusion: e.g., financial returns may have continuous Gaussian noise plus occasional large jumps modeled by a compound Poisson process. SDEs with jumps require an extended Ito formula incorporating jump terms.

Practical modeling checklist

- •Decide whether events are discrete (Poisson) or continuous/noisy (Brownian) or both.
- •Check stationarity/independent increments assumptions; these yield exact tractability.
- •Use Ito's formula to convert between SDEs and deterministic PDEs (Fokker–Planck, backward Kolmogorov).

Downstream methods enabled

- •SDE solution techniques and explicit formulas (Black–Scholes, Ornstein–Uhlenbeck).
- •Stochastic stability, large deviations, and exit-time problems.
- •Nonlinear filtering and stochastic control.

Concrete final illustration: pricing expectation under geometric Brownian motion. Using the StS\_tSt​ formula above with s0=100,μ=0.05,σ=0.2,t=1s\_0=100,\mu=0.05,\sigma=0.2,t=1s0​=100,μ=0.05,σ=0.2,t=1, the distribution of S1S\_1S1​ is lognormal, and the probability P(S1>110)=P(σW1>log⁡(1.1)−(μ−12σ2))P(S\_1>110)=P\left(\sigma W\_1 > \log(1.1) - (\mu-\tfrac12\sigma^2)\right)P(S1​>110)=P(σW1​>log(1.1)−(μ−21​σ2)). Numeric compute: log⁡(1.1)≈0.09531\log(1.1)\approx0.09531log(1.1)≈0.09531, (μ−0.5σ2)=0.05−0.02=0.03(\mu-0.5\sigma^2)=0.05-0.02=0.03(μ−0.5σ2)=0.05−0.02=0.03, so threshold for W1W\_1W1​ is (0.09531−0.03)/0.2≈0.32755(0.09531-0.03)/0.2\approx0.32755(0.09531−0.03)/0.2≈0.32755. Thus P(S1>110)=P(W1>0.32755)≈0.3716P(S\_1>110)=P(W\_1>0.32755)\approx0.3716P(S1​>110)=P(W1​>0.32755)≈0.3716.

This section shows how Poisson processes, Brownian motion and Ito calculus are not abstract curiosities but precise tools that produce explicit models, closed-form calculations, and pathwise constructions for a wide range of applications.

## Worked Examples (3)

### Poisson count probability

Rate λ=2\lambda=2λ=2 events/hour; find P(N(3)≥3)P(N(3)\ge3)P(N(3)≥3) for t=3t=3t=3 hours.

1. Recognize N(3)∼Poisson(λt)=Poisson(2⋅3)=Poisson(6)N(3)\sim\mathrm{Poisson}(\lambda t)=\mathrm{Poisson}(2\cdot3)=\mathrm{Poisson}(6)N(3)∼Poisson(λt)=Poisson(2⋅3)=Poisson(6).
2. Compute probabilities for k=0,1,2k=0,1,2k=0,1,2 and subtract from 1: P(N(3)≥3)=1−∑k=02e−66kk!P(N(3)\ge3)=1-\sum\_{k=0}^2 e^{-6}\frac{6^k}{k!}P(N(3)≥3)=1−∑k=02​e−6k!6k​.
3. Calculate term-by-term: e−6600!=e−6≈0.00247875e^{-6}\frac{6^0}{0!}=e^{-6}\approx0.00247875e−60!60​=e−6≈0.00247875.
4. Next: e−6611!=6e−6≈0.0148725e^{-6}\frac{6^1}{1!}=6e^{-6}\approx0.0148725e−61!61​=6e−6≈0.0148725; then e−6622!=18e−6≈0.0446175e^{-6}\frac{6^2}{2!}=18e^{-6}\approx0.0446175e−62!62​=18e−6≈0.0446175.
5. Sum the three: $0.00247875+0.0148725+0.0446175\approx0.06196875.Subtractfrom1toget. Subtract from 1 to get .Subtractfrom1toget\approx0.93803125$.

**Insight:** This example uses the defining Poisson distribution formula and shows how to compute tail probabilities via finite sums. It reinforces intuition that rare low counts are unlikely when the mean is large (mean 6).

### Ito formula on $f(W\_t)=W\_t^2$

Let WtW\_tWt​ be standard Brownian motion. Use Ito's formula to compute d(Wt2)d(W\_t^2)d(Wt2​) and then find E[Wt2]E[W\_t^2]E[Wt2​] for t=3t=3t=3.

1. Set f(x)=x2f(x)=x^2f(x)=x2. Then f′(x)=2xf'(x)=2xf′(x)=2x, f′′(x)=2f''(x)=2f′′(x)=2.
2. Apply Ito's formula (time-homogeneous case): df(Wt)=f′(Wt)dWt+12f′′(Wt)dtdf(W\_t)=f'(W\_t)dW\_t + \tfrac12 f''(W\_t) dtdf(Wt​)=f′(Wt​)dWt​+21​f′′(Wt​)dt.
3. Substitute derivatives: d(Wt2)=2Wt dWt+12⋅2 dt=2Wt dWt+dtd(W\_t^2)=2W\_t\,dW\_t + \tfrac12\cdot2\,dt = 2W\_t\,dW\_t + dtd(Wt2​)=2Wt​dWt​+21​⋅2dt=2Wt​dWt​+dt.
4. Take expectations: E[d(Wt2)]=E[2Wt dWt]+E[dt]E[d(W\_t^2)] = E[2W\_t\,dW\_t] + E[dt]E[d(Wt2​)]=E[2Wt​dWt​]+E[dt]. The stochastic integral has zero expectation, so dE[Wt2]=dtdE[W\_t^2]=dtdE[Wt2​]=dt.
5. Integrate from 0 to 3: E[W32]=∫03ds=3E[W\_3^2]=\int\_0^3 ds = 3E[W32​]=∫03​ds=3.

**Insight:** Ito's formula produces an extra deterministic dtdtdt term absent in classical chain rule; that term exactly accounts for the quadratic variation and yields the known variance of Brownian motion.

### Ornstein–Uhlenbeck moments

Consider dXt=−Xt dt+2 dWtdX\_t = -X\_t\,dt + 2\,dW\_tdXt​=−Xt​dt+2dWt​, X0=1X\_0=1X0​=1. Compute E[X1]E[X\_1]E[X1​] and Var(X1)\mathrm{Var}(X\_1)Var(X1​).

1. Solve via integrating factor: multiply by ete^{t}et to get d(etXt)=et⋅2 dWtd(e^{t}X\_t)= e^{t}\cdot 2\,dW\_td(etXt​)=et⋅2dWt​.
2. Integrate: etXt=X0+2∫0tes dWse^{t}X\_t = X\_0 + 2\int\_0^t e^{s}\,dW\_setXt​=X0​+2∫0t​esdWs​, so Xt=X0e−t+2∫0te−(t−s) dWsX\_t = X\_0 e^{-t} + 2\int\_0^t e^{-(t-s)}\,dW\_sXt​=X0​e−t+2∫0t​e−(t−s)dWs​.
3. Take expectation: E[Xt]=X0e−t=e−tE[X\_t]=X\_0 e^{-t}=e^{-t}E[Xt​]=X0​e−t=e−t. For t=1t=1t=1, E[X1]=e−1≈0.3679E[X\_1]=e^{-1}\approx0.3679E[X1​]=e−1≈0.3679.
4. Compute variance using Ito isometry: Var(Xt)=4∫0te−2(t−s) ds=4∫0te−2u du\mathrm{Var}(X\_t)=4\int\_0^t e^{-2(t-s)}\,ds=4\int\_0^t e^{-2u}\,duVar(Xt​)=4∫0t​e−2(t−s)ds=4∫0t​e−2udu with u=t−su=t-su=t−s.
5. Evaluate for t=1t=1t=1: Var(X1)=4(1−e−2)/2=2(1−e−2)≈2(1−0.1353)≈1.7294\mathrm{Var}(X\_1)=4(1-e^{-2})/2 =2(1-e^{-2})\approx2(1-0.1353)\approx1.7294Var(X1​)=4(1−e−2)/2=2(1−e−2)≈2(1−0.1353)≈1.7294.

**Insight:** Linear SDEs can be solved explicitly; integrals against Brownian motion yield Gaussian random variables whose variance follows from the Ito isometry. The result shows mean reversion (exponential decay) and stationary variance as t→∞t\to\inftyt→∞.

## Key Takeaways

- ✓

  A stochastic process is a time-indexed family of random variables; Poisson processes model discrete random events, while Brownian/Wiener processes model continuous Gaussian noise.
- ✓

  Poisson processes have independent, stationary increments with Poisson marginals; interarrival times are iid exponential (memoryless).
- ✓

  Brownian motion has Gaussian independent increments and nonzero quadratic variation: sums of squared increments over a partition converge to elapsed time.
- ✓

  The Ito integral is defined for non-anticipating integrands as an L^2 limit; the Ito isometry relates second moments of the integral to the integral of the squared integrand.
- ✓

  Ito's formula extends the chain rule by adding a half the second derivative times the diffusion coefficient squared (the quadratic variation term).
- ✓

  Many applied models (Black–Scholes, queuing, diffusion, filtering) follow directly from these building blocks; linear SDEs often admit explicit solutions via integrating factors.
- ✓

  Always check assumptions: independent increments, stationarity, continuity of paths (or presence of jumps) determine which tools apply.

## Common Mistakes

- ✗

  Treating Brownian paths as differentiable: Brownian motion is almost surely nowhere differentiable; attempts to apply ordinary calculus to sample paths produce wrong terms (you need Ito calculus).
- ✗

  Forgetting the Ito correction: applying the classical chain rule to SDEs and omitting the 12b2f′′\tfrac12 b^2 f''21​b2f′′ term leads to incorrect drift terms (a common error in derivations).
- ✗

  Confusing independent increments with independent values at time points: increments over disjoint intervals are independent, but values like WtW\_tWt​ and WsW\_sWs​ are not independent unless t−st-st−s covers the interval from 0 (i.e., unless one is difference from the other).
- ✗

  Misusing memoryless property: exponential interarrival times are memoryless, but conditional distributions such as arrival times given counts are order statistics, not independent exponentials.

## Practice

easy

Easy: A Poisson process has rate λ=4\lambda=4λ=4 per hour. What is the probability of exactly 3 events in a 30-minute interval?

**Hint:** Compute λt\lambda tλt for t=0.5t=0.5t=0.5 hours and use the Poisson pmf.

Show solution

Here λt=4⋅0.5=2\lambda t = 4\cdot0.5=2λt=4⋅0.5=2. So P(N(0.5)=3)=e−2233!=e−286=43e−2≈1.3333⋅0.13534≈0.18045P(N(0.5)=3)=e^{-2}\frac{2^3}{3!}=e^{-2}\frac{8}{6}=\frac{4}{3}e^{-2}\approx1.3333\cdot0.13534\approx0.18045P(N(0.5)=3)=e−23!23​=e−268​=34​e−2≈1.3333⋅0.13534≈0.18045.

medium

Medium: Let WtW\_tWt​ be standard Brownian motion. Use Ito's formula to compute dYtdY\_tdYt​ when Yt=exp⁡(at+bWt)Y\_t=\exp(a t + b W\_t)Yt​=exp(at+bWt​) for constants a,ba,ba,b. Then compute E[Yt]E[Y\_t]E[Yt​] for given a=0.1,b=0.5,t=2a=0.1,b=0.5,t=2a=0.1,b=0.5,t=2.

**Hint:** Apply Ito to f(t,x)=exp⁡(at+bx)f(t,x)=\exp(a t + b x)f(t,x)=exp(at+bx). Remember ∂tf=af\partial\_t f = a f∂t​f=af, ∂xf=bf\partial\_x f = b f∂x​f=bf, ∂xxf=b2f\partial\_{xx}f = b^2 f∂xx​f=b2f.

Show solution

Ito gives

dYt=(af+12b2f) dt+bf dWt=f(a+12b2)dt+bf dWt.dY\_t = (a f + \tfrac12 b^2 f)\,dt + b f\,dW\_t = f\Big(a + \tfrac12 b^2\Big)dt + b f\,dW\_t.dYt​=(af+21​b2f)dt+bfdWt​=f(a+21​b2)dt+bfdWt​.

Taking expectations kills the dWtdW\_tdWt​ term: dE[Yt]=E[f](a+12b2)dtdE[Y\_t]=E[f]\Big(a+\tfrac12 b^2\Big)dtdE[Yt​]=E[f](a+21​b2)dt, so E[Yt]=e(a+12b2)tE[Y0]E[Y\_t]=e^{(a+\tfrac12 b^2)t}E[Y\_0]E[Yt​]=e(a+21​b2)tE[Y0​]. With Y0=1Y\_0=1Y0​=1, a=0.1,b=0.5,t=2a=0.1,b=0.5,t=2a=0.1,b=0.5,t=2, we get exponent (0.1+0.52/2)⋅2=(0.1+0.125)⋅2=0.225⋅2=0.45(0.1+0.5^2/2)\cdot2=(0.1+0.125)\cdot2=0.225\cdot2=0.45(0.1+0.52/2)⋅2=(0.1+0.125)⋅2=0.225⋅2=0.45, so E[Y2]=e0.45≈1.571E[Y\_2]=e^{0.45}\approx1.571E[Y2​]=e0.45≈1.571.

hard

Hard: Consider the SDE dXt=μXt dt+σXt dWtdX\_t = \mu X\_t\,dt + \sigma X\_t\,dW\_tdXt​=μXt​dt+σXt​dWt​ with X0=x0>0X\_0=x\_0>0X0​=x0​>0. (This is geometric Brownian motion.) Derive the explicit solution and compute Var(Xt)\mathrm{Var}(X\_t)Var(Xt​) in terms of x0,μ,σ,tx\_0,\mu,\sigma,tx0​,μ,σ,t.

**Hint:** Apply Ito to log⁡Xt\log X\_tlogXt​ to linearize; then use the known moments of the lognormal distribution.

Show solution

Using Ito on f(x)=log⁡xf(x)=\log xf(x)=logx: dlog⁡Xt=(μ−12σ2)dt+σdWtd\log X\_t = (\mu - \tfrac12\sigma^2)dt + \sigma dW\_tdlogXt​=(μ−21​σ2)dt+σdWt​. Integrate to get

log⁡Xt=log⁡x0+(μ−12σ2)t+σWt.\log X\_t = \log x\_0 + (\mu - \tfrac12\sigma^2)t + \sigma W\_t.logXt​=logx0​+(μ−21​σ2)t+σWt​.

Exponentiate:

Xt=x0exp⁡((μ−12σ2)t+σWt).X\_t = x\_0\exp\left((\mu - \tfrac12\sigma^2)t + \sigma W\_t\right).Xt​=x0​exp((μ−21​σ2)t+σWt​).

Since σWt∼N(0,σ2t)\sigma W\_t\sim N(0,\sigma^2 t)σWt​∼N(0,σ2t), XtX\_tXt​ is lognormal. Its mean is E[Xt]=x0eμtE[X\_t]=x\_0 e^{\mu t}E[Xt​]=x0​eμt. Its second moment is

E[Xt2]=x02e2μt+σ2tE[X\_t^2] = x\_0^2 e^{2\mu t + \sigma^2 t}E[Xt2​]=x02​e2μt+σ2t

(since E[e2σWt]=e22σ2t/2=e2σ2tE[e^{2\sigma W\_t}] = e^{2^2\sigma^2 t/2} = e^{2\sigma^2 t}E[e2σWt​]=e22σ2t/2=e2σ2t, combine with exponent). Therefore

Var(Xt)=E[Xt2]−(E[Xt])2=x02e2μt(eσ2t−1).\mathrm{Var}(X\_t) = E[X\_t^2] - (E[X\_t])^2 = x\_0^2 e^{2\mu t}\left(e^{\sigma^2 t}-1\right).Var(Xt​)=E[Xt2​]−(E[Xt​])2=x02​e2μt(eσ2t−1).

This completes the derivation.

## Connections

Looking back: In Markov Chains we learned memoryless transitions and generators; Poisson processes are continuous-time Markov chains with exponential holding times, and their generator Lf(n)=λ(f(n+1)−f(n))\mathcal{L}f(n)=\lambda(f(n+1)-f(n))Lf(n)=λ(f(n+1)−f(n)) mirrors discrete generators. From Common Distributions we directly use Poisson, exponential and normal laws as the marginals/increments of Poisson and Brownian processes. From Integrals, the idea of Riemann sums and limits underlies the construction of the Ito integral (mean-square limits of adapted Riemann sums).

Looking forward: Mastery of Poisson processes and Ito calculus is essential for studying stochastic differential equations (SDEs), which underpin Black–Scholes option pricing, stochastic control and filtering (e.g., Kalman–Bucy, nonlinear filters), and for linking probabilistic models to PDEs (Fokker–Planck and backward Kolmogorov equations). Advanced topics that rely on these foundations include large deviations for stochastic processes, Malliavin calculus (stochastic calculus of variations), jump-diffusion models, and modern stochastic numerical methods (Euler–Maruyama, Milstein schemes). Specific prerequisite-to-downstream map: Poisson/exponential results -> queueing theory and point-process statistics; Brownian/Ito -> SDE theory, PDE connections, financial mathematics, stochastic filtering and control.

Quality: pending (0.0/5)

[← back to tree](/tech-tree/)[browse all →](/tech-tree/inventory/)
