---
title: KL Divergence
description: Relative entropy. Measuring difference between distributions.
date: '2026-07-01'
scheduled: '2026-10-03'
tags:
- p-and-l-engineering
- coming-soon
- tech-tree
layout: layouts/post.njk
templateEngineOverride: md
image: /img/xavi-linkedin-profile.jpg
draft: true
generated_by: templeton-deep-copy-import
source_format: html
inspiration_url: https://templeton.host/tech-tree/kl-divergence/
inspiration_category: tech-tree
---

> Source-copy draft imported from [https://templeton.host/tech-tree/kl-divergence/](https://templeton.host/tech-tree/kl-divergence/). Names, domain references, and local media paths were adapted for Xavi Ablaza / getablaza.com.

[←Back to Tech Tree](/tech-tree/)

[inventory](/tech-tree/inventory/)[coverage](/tech-tree/coverage/)

# KL Divergence

Information TheoryDifficulty: ★★★★☆Depth: 7Unlocks: 7

Relative entropy. Measuring difference between distributions.

## Interactive Visualization

⏮◀◀▶▶STEP0.25x1xZOOM

t=0s

## Core Concepts

- -KL divergence as a scalar measure of how one probability distribution diverges from another (relative entropy).
- -It is defined via an expectation taken with respect to the true distribution (the divergence is expectation-based).
- -Operational interpretation: the KL gives the average extra log-loss (information) per sample when using Q instead of the true P.

## Key Symbols & Notation

D\_KL(P || Q)

## Essential Relationships

- -D\_KL(P || Q) = E\_{X ~ P}[ log( P(X) / Q(X) ) ]
- -D\_KL(P || Q) >= 0, with equality iff P = Q almost everywhere

## Prerequisites (2)

[Entropy5 atoms](/tech-tree/entropy/)[Maximum Likelihood Estimation6 atoms](/tech-tree/mle/)

## Unlocks (3)

[Cross-Entropylvl 4](/tech-tree/cross-entropy/)[Variational Autoencoderslvl 5](/tech-tree/vae/)[Information Bottlenecklvl 4](/tech-tree/information-bottleneck/)

Advanced Learning Details

### Graph Position

79

Depth Cost

7

Fan-Out (ROI)

4

Bottleneck Score

7

Chain Length

### Cognitive Load

6

Atomic Elements

36

Total Elements

L2

Percentile Level

L4

Atomic Level

### All Concepts (15)

- - Definition of KL divergence for discrete distributions: D\_KL(P || Q) = sum over x of P(x) \* log( P(x) / Q(x) ).
- - Continuous (density) version: KL divergence as integral of p(x) \* log(p(x)/q(x)) dx.
- - Interpretation as expected log-likelihood ratio: KL is the expectation under P of the log of the probability ratio log(P(x)/Q(x)).
- - Interpretation as extra expected code length (extra bits or nats) when encoding samples from P using a code optimized for Q instead of P.
- - Non-negativity (Gibbs inequality): KL divergence is always >= 0, with equality only when P and Q are equal almost everywhere.
- - Asymmetry: D\_KL(P || Q) is not equal to D\_KL(Q || P); KL is not a metric.
- - Support requirement and infinity behavior: if there exists x with P(x)>0 but Q(x)=0, then D\_KL(P||Q) = infinity.
- - Cross-entropy concept as a distinct quantity: H(P,Q) = - sum P(x) log Q(x) (or integral), used as a separate loss.
- - Relationship between KL and cross-entropy: D\_KL(P||Q) = H(P,Q) - H(P).
- - Relation to maximum likelihood: minimizing KL(P\_empirical || Q\_theta) over theta (or equivalently minimizing expected negative log-likelihood under P\_empirical) yields MLE; MLE can be viewed as KL minimization to the empirical distribution.
- - Units depend on log base: log base 2 gives bits, natural log gives nats; choice affects numerical value and interpretation.
- - Chain rule / conditional decomposition: KL for joint distributions can be decomposed into marginal KL plus expected conditional KL: D\_KL(P(X,Y)||Q(X,Y)) = D\_KL(P(X)||Q(X)) + E\_{P(X)}[ D\_KL(P(Y|X)||Q(Y|X)) ].
- - Additivity for independent product distributions: D\_KL(P1 x P2 || Q1 x Q2) = D\_KL(P1||Q1) + D\_KL(P2||Q2).
- - Relation to mutual information: mutual information I(X;Y) = D\_KL( P(X,Y) || P(X) P(Y) ).
- - Optimization properties used in ML: convexity in the model distribution Q (for fixed P) making KL a convenient loss for parameter estimation in many cases.

### Teaching Strategy

Multi-session curriculum - substantial prior knowledge and complex material. Use mastery gates and deliberate practice.

Two probability distributions can look “close” on a plot but behave very differently when you use one to make predictions under the other. KL divergence is the tool that turns that mismatch into a single number—with a clear operational meaning: how many extra bits (or nats) you pay, on average, per sample when you code or predict using Q while the world is actually P.

TL;DR:

KL divergence DKL(P∥∥Q)=Ex∼P[log⁡P(x)Q(x)]D\_{\mathrm{KL}}(P\|\|Q)=\mathbb{E}\_{x\sim P}[\log \frac{P(x)}{Q(x)}]DKL​(P∥∥Q)=Ex∼P​[logQ(x)P(x)​] measures the average extra log-loss incurred by using QQQ instead of the true PPP. It is nonnegative, asymmetric, and becomes infinite when QQQ assigns zero probability where PPP does not.

## What Is KL Divergence?

### Why we need a special “distance” for distributions

When you compare two vectors, Euclidean distance is natural. For probability distributions, Euclidean distance often hides what actually matters for learning and decision-making:

- •If your model assigns *tiny* probability to events that happen under the true distribution, your log-loss explodes.
- •If your model assigns probability mass to impossible events, you waste capacity—but you might not be punished as severely.

So we want a measure that is **prediction-aware**: it should tell us how costly it is to pretend the world follows QQQ when it actually follows PPP.

KL divergence (Kullback–Leibler divergence), also called **relative entropy**, does exactly that.

### Definition (discrete)

Let PPP and QQQ be distributions over the same discrete set \(\mathcal{X}\). The KL divergence from QQQ to PPP is

DKL(P∥∥Q)=∑x∈XP(x) log⁡P(x)Q(x).D\_{\mathrm{KL}}(P\|\|Q)=\sum\_{x\in\mathcal{X}} P(x)\,\log\frac{P(x)}{Q(x)}.DKL​(P∥∥Q)=x∈X∑​P(x)logQ(x)P(x)​.

A few immediate notes:

- •The expectation is with respect to **$P$** (the “true” distribution in the common interpretation).
- •The log base sets units: base 2 → **bits**, base eee → **nats**.
- •If there exists an xxx with P(x)>0P(x)>0P(x)>0 but Q(x)=0Q(x)=0Q(x)=0, then log⁡P(x)Q(x)=∞\log \frac{P(x)}{Q(x)}=\inftylogQ(x)P(x)​=∞ and KL becomes **infinite**.

### Definition (continuous)

For densities p(x)p(x)p(x) and q(x)q(x)q(x) (with respect to the same base measure),

DKL(P∥∥Q)=∫p(x) log⁡p(x)q(x) dx.D\_{\mathrm{KL}}(P\|\|Q)=\int p(x)\,\log\frac{p(x)}{q(x)}\,dx.DKL​(P∥∥Q)=∫p(x)logq(x)p(x)​dx.

The same “support mismatch” rule applies: if p(x)>0p(x)>0p(x)>0 on a region where q(x)=0q(x)=0q(x)=0, the KL is infinite.

### The most important intuition: a *log ratio* averaged under reality

KL is an average of a log ratio:

- •If QQQ assigns *lower* probability than PPP to likely events, then P(x)/Q(x)P(x)/Q(x)P(x)/Q(x) is large → log is positive → KL grows.
- •If QQQ assigns *higher* probability than PPP to likely events, then the log ratio can be negative for those xxx.

So why isn’t KL sometimes negative overall? Because of a deep inequality (Jensen / Gibbs) that forces the expectation to be ≥ 0.

### Guided visualization on the interactive canvas (do this now)

**Canvas A: Bernoulli slider**

1. 1)Choose a Bernoulli true distribution: P=Bern(p)P=\mathrm{Bern}(p)P=Bern(p).
2. 2)Choose a model distribution: Q=Bern(q)Q=\mathrm{Bern}(q)Q=Bern(q).
3. 3)Slide ppp and qqq independently.

Prompted observations:

- •Hold p=0.2p=0.2p=0.2 fixed. Move qqq toward 0. Watch DKL(P∥∥Q)D\_{\mathrm{KL}}(P\|\|Q)DKL​(P∥∥Q) rise sharply.
- •Now move qqq toward 1. It also rises, but the blow-up is much more dramatic when QQQ places near-zero probability on outcomes that happen under PPP.
- •Set q=0q=0q=0 exactly while p>0p>0p>0. The KL becomes **infinite**.

This is the first “feel” for what KL cares about: **being wrong in the direction of underestimating true events is catastrophic in log-loss terms.**

### Static anchor diagram: support mismatch

Imagine two distributions over the same line:

- •p(x)p(x)p(x) is concentrated on an interval, say [0,1][0,1][0,1].
- •q(x)q(x)q(x) is concentrated on [1,2][1,2][1,2].

They barely overlap. On [0,1][0,1][0,1], p(x)>0p(x)>0p(x)>0 but q(x)=0q(x)=0q(x)=0, so DKL(P∥∥Q)=∞D\_{\mathrm{KL}}(P\|\|Q)=\inftyDKL​(P∥∥Q)=∞.

If you overlay them, the key highlighted region is where **$p(x)$ has mass but $q(x)$ is zero**. KL treats that as an absolute failure, because it corresponds to assigning impossible probability to events that occur.

### What KL is *not*

- •It is **not symmetric**: generally DKL(P∥∥Q)≠DKL(Q∥∥P)D\_{\mathrm{KL}}(P\|\|Q)\neq D\_{\mathrm{KL}}(Q\|\|P)DKL​(P∥∥Q)=DKL​(Q∥∥P).
- •It is **not** a metric: it doesn’t satisfy the triangle inequality.
- •It is not simply “area between curves.” It is an *expectation of log ratios*, weighted by PPP.

Keep those distinctions in mind; they will matter when we interpret mode-seeking vs mode-covering behavior later.

## Core Mechanic 1: KL as Expected Extra Log-Loss (Operational Meaning)

### Why before how: prediction is about log-loss

In probabilistic modeling, a standard way to score a model QQQ on data drawn from PPP is **negative log-likelihood** (log-loss). For an outcome xxx, the log-loss under model QQQ is

ℓQ(x)=−log⁡Q(x).\ell\_Q(x) = -\log Q(x).ℓQ​(x)=−logQ(x).

The *expected* log-loss under the true distribution PPP is

Ex∼P[ℓQ(x)]=−∑xP(x)log⁡Q(x).\mathbb{E}\_{x\sim P}[\ell\_Q(x)] = -\sum\_x P(x)\log Q(x).Ex∼P​[ℓQ​(x)]=−x∑​P(x)logQ(x).

This quantity shows up everywhere:

- •maximum likelihood estimation (MLE)
- •cross-entropy loss in classification
- •coding and compression

So the natural question becomes:

> How much worse is it to use QQQ than to use the true PPP, on average?

### Derivation: KL is the excess expected log-loss

Start from KL:

DKL(P∥∥Q)=∑xP(x)log⁡P(x)Q(x).D\_{\mathrm{KL}}(P\|\|Q)=\sum\_x P(x)\log\frac{P(x)}{Q(x)}.DKL​(P∥∥Q)=x∑​P(x)logQ(x)P(x)​.

Expand the log ratio:

log⁡P(x)Q(x)=log⁡P(x)−log⁡Q(x).\log\frac{P(x)}{Q(x)} = \log P(x) - \log Q(x).logQ(x)P(x)​=logP(x)−logQ(x).

Plug in:

DKL(P∥∥Q)=∑xP(x)(log⁡P(x)−log⁡Q(x))=∑xP(x)log⁡P(x)−∑xP(x)log⁡Q(x).\begin{aligned}
D\_{\mathrm{KL}}(P\|\|Q)
&= \sum\_x P(x)\big(\log P(x)-\log Q(x)\big) \\
&= \sum\_x P(x)\log P(x) - \sum\_x P(x)\log Q(x).
\end{aligned}DKL​(P∥∥Q)​=x∑​P(x)(logP(x)−logQ(x))=x∑​P(x)logP(x)−x∑​P(x)logQ(x).​

Rewrite each term:

- •Entropy: H(P)=−∑xP(x)log⁡P(x)H(P) = -\sum\_x P(x)\log P(x)H(P)=−∑x​P(x)logP(x)
- •Cross-entropy: H(P,Q)=−∑xP(x)log⁡Q(x)H(P,Q) = -\sum\_x P(x)\log Q(x)H(P,Q)=−∑x​P(x)logQ(x)

So

DKL(P∥∥Q)=−H(P)+H(P,Q)=H(P,Q)−H(P).\begin{aligned}
D\_{\mathrm{KL}}(P\|\|Q)
&= -H(P) + H(P,Q) \\
&= H(P,Q) - H(P).
\end{aligned}DKL​(P∥∥Q)​=−H(P)+H(P,Q)=H(P,Q)−H(P).​

**Interpretation:**

- •H(P)H(P)H(P) is the best achievable expected log-loss if you predict with the true PPP.
- •H(P,Q)H(P,Q)H(P,Q) is the expected log-loss if you predict with QQQ while data comes from PPP.
- •Their difference is the penalty: **the average extra log-loss per sample**.

In base 2 logs, it is literally “extra bits per symbol.”

### Nonnegativity: why you can’t beat the truth on average

The statement DKL(P∥∥Q)≥0D\_{\mathrm{KL}}(P\|\|Q)\ge 0DKL​(P∥∥Q)≥0 formalizes: on average, you cannot do better (in expected log-loss) than predicting with the true distribution.

A clean proof uses Jensen’s inequality on the concave log function.

Let’s show the common Gibbs inequality form.

We want to show:

∑xP(x)log⁡P(x)Q(x)≥0.\sum\_x P(x)\log\frac{P(x)}{Q(x)} \ge 0.x∑​P(x)logQ(x)P(x)​≥0.

Equivalently,

∑xP(x)log⁡Q(x)P(x)≤0.\sum\_x P(x)\log\frac{Q(x)}{P(x)} \le 0.x∑​P(x)logP(x)Q(x)​≤0.

Now use Jensen (log is concave):

∑xP(x)log⁡Q(x)P(x)≤log⁡(∑xP(x)Q(x)P(x))=log⁡(∑xQ(x))=log⁡1=0.\sum\_x P(x)\log\frac{Q(x)}{P(x)} \le \log\left(\sum\_x P(x)\frac{Q(x)}{P(x)}\right) = \log\left(\sum\_x Q(x)\right)=\log 1=0.x∑​P(x)logP(x)Q(x)​≤log(x∑​P(x)P(x)Q(x)​)=log(x∑​Q(x))=log1=0.

Therefore,

DKL(P∥∥Q)≥0,D\_{\mathrm{KL}}(P\|\|Q)\ge 0,DKL​(P∥∥Q)≥0,

with equality iff P(x)=Q(x)P(x)=Q(x)P(x)=Q(x) for all xxx where P(x)>0P(x)>0P(x)>0.

### Guided visualization: “extra log-loss” as a bar chart

**Canvas B: per-outcome contribution plot**

For a small discrete space (say 5 outcomes), plot bars of

c(x)=P(x)log⁡P(x)Q(x).c(x)=P(x)\log\frac{P(x)}{Q(x)}.c(x)=P(x)logQ(x)P(x)​.

Prompts:

1. 1)Make one outcome very likely under PPP (e.g., P(x\_1)=0.6P(x\\_1)=0.6P(x\_1)=0.6), but set Q(x\_1)=0.2Q(x\\_1)=0.2Q(x\_1)=0.2.

- •Watch that bar dominate KL.

2. 2)Make QQQ larger than PPP on a rare outcome.

- •You may see a negative contribution there, but it usually doesn’t compensate much because it’s weighted by small P(x)P(x)P(x).

This visually explains why KL focuses on being accurate where PPP puts mass.

### Connection to MLE (prerequisite bridge)

Suppose you have data x1,…,xn∼Px₁,\dots,x\_n \sim Px1​,…,xn​∼P i.i.d., and a parametric model QθQ\_\thetaQθ​.

The average negative log-likelihood is

1n∑i=1n−log⁡Qθ(xi).\frac{1}{n}\sum\_{i=1}^n -\log Q\_\theta(x\_i).n1​i=1∑n​−logQθ​(xi​).

As n→∞n\to\inftyn→∞, this converges to

Ex∼P[−log⁡Qθ(x)]=H(P,Qθ).\mathbb{E}\_{x\sim P}\big[-\log Q\_\theta(x)\big] = H(P,Q\_\theta).Ex∼P​[−logQθ​(x)]=H(P,Qθ​).

Since

H(P,Qθ)=H(P)+DKL(P∥∥Qθ),H(P,Q\_\theta) = H(P) + D\_{\mathrm{KL}}(P\|\|Q\_\theta),H(P,Qθ​)=H(P)+DKL​(P∥∥Qθ​),

minimizing expected NLL over θ\thetaθ is the same as minimizing DKL(P∥∥Qθ)D\_{\mathrm{KL}}(P\|\|Q\_\theta)DKL​(P∥∥Qθ​) (because H(P)H(P)H(P) does not depend on θ\thetaθ).

So MLE is “KL minimization from data distribution to model distribution.”

That phrasing becomes extremely useful later (cross-entropy, VAEs, variational inference).

## Core Mechanic 2: Asymmetry, Support, and Mode-Seeking vs Mode-Covering

### Why asymmetry matters

Because KL is expectation-weighted under the first argument, swapping arguments changes *what errors are emphasized*.

- •Forward KL: DKL(P∥∥Q)D\_{\mathrm{KL}}(P\|\|Q)DKL​(P∥∥Q) weights errors by PPP (truth-weighted).
- •Reverse KL: DKL(Q∥∥P)D\_{\mathrm{KL}}(Q\|\|P)DKL​(Q∥∥P) weights errors by QQQ (model-weighted).

This is not just a mathematical curiosity: it determines whether an approximation spreads out to “cover” all modes or collapses onto one.

### Support and the “infinite wall”

Recall:

- •If P(x)>0P(x)>0P(x)>0 and Q(x)=0Q(x)=0Q(x)=0 anywhere, then DKL(P∥∥Q)=∞D\_{\mathrm{KL}}(P\|\|Q)=\inftyDKL​(P∥∥Q)=∞.
- •If Q(x)>0Q(x)>0Q(x)>0 and P(x)=0P(x)=0P(x)=0 somewhere, then DKL(Q∥∥P)=∞D\_{\mathrm{KL}}(Q\|\|P)=\inftyDKL​(Q∥∥P)=∞.

So each direction imposes a different feasibility constraint:

| Divergence | Catastrophic if… | Intuition |
| --- | --- | --- |
| $D\_{\mathrm{KL}}(P\ | \ | Q)$ | Q=0Q=0Q=0 where P>0P>0P>0 | Model refuses to assign probability to real events |
| $D\_{\mathrm{KL}}(Q\ | \ | P)$ | P=0P=0P=0 where Q>0Q>0Q>0 | Model insists on events the truth says are impossible |

### Guided visualization: toggle forward vs reverse KL on a bimodal target

**Canvas C: mixture of Gaussians vs single Gaussian approximation**

1. 1)Let PPP be a bimodal distribution (two separated Gaussians).
2. 2)Let QQQ be a single Gaussian with adjustable mean/variance.
3. 3)Add a toggle: compute either DKL(P∥∥Q)D\_{\mathrm{KL}}(P\|\|Q)DKL​(P∥∥Q) (forward) or DKL(Q∥∥P)D\_{\mathrm{KL}}(Q\|\|P)DKL​(Q∥∥P) (reverse).

Prompts:

- •In **forward KL** mode, increase Q’s variance. You’ll often see the best fit broaden to cover both modes. Missing one mode is costly because PPP puts mass there.
- •In **reverse KL** mode, the best fit often collapses onto one mode (mode-seeking). Why? Because the expectation is under QQQ: if QQQ puts almost no mass near the other mode, it doesn’t “feel” that region.

This is a central intuition used in variational inference: minimizing reverse KL (common in VI) tends to be mode-seeking.

### A simple discrete example of asymmetry

Let X={a,b}\mathcal{X} = \{a,b\}X={a,b}.

- •P(a)=0.99P(a)=0.99P(a)=0.99, P(b)=0.01P(b)=0.01P(b)=0.01.
- •Consider two candidate models:
- •Q1(a)=0.9Q₁(a)=0.9Q1​(a)=0.9, Q1(b)=0.1Q₁(b)=0.1Q1​(b)=0.1 (covers both outcomes)
- •Q2(a)=0.9999Q₂(a)=0.9999Q2​(a)=0.9999, Q2(b)=0.0001Q₂(b)=0.0001Q2​(b)=0.0001 (very confident)

Forward KL DKL(P∥∥Q)D\_{\mathrm{KL}}(P\|\|Q)DKL​(P∥∥Q) penalizes when QQQ underestimates events that happen under PPP.

- •If Q2Q₂Q2​ makes bbb extremely unlikely but P(b)=0.01P(b)=0.01P(b)=0.01, the term $0.01\log\frac{0.01}{0.0001}$ can be significant.

Reverse KL DKL(Q∥∥P)D\_{\mathrm{KL}}(Q\|\|P)DKL​(Q∥∥P) penalizes when QQQ places mass where PPP does not.

- •Here both support match (no zeros), but the weighting changes what matters: reverse KL is dominated by where QQQ places mass (mostly at aaa), making it less sensitive to a small-probability region unless QQQ also places mass there.

### KL is not symmetric—and not meant to be

Thinking of KL as “how surprised would I be if I used Q in a world of P?” naturally picks a direction: the world is PPP, your model is QQQ.

So asymmetry is actually *part of the meaning*.

### When does asymmetry show up in ML practice?

- •**Supervised classification**: cross-entropy corresponds to forward KL from the data label distribution to the model distribution.
- •**Variational inference (ELBO)**: commonly minimizes reverse KL between an approximate posterior q(z)q(z)q(z) and true posterior p(z∣x)p(z\mid x)p(z∣x).
- •**Distillation**: direction determines whether the student covers teacher’s support broadly or focuses on peak probabilities.

### Practical note: smoothing to avoid infinities

In discrete problems, if you estimate QQQ from limited data, you can accidentally set Q(x)=0Q(x)=0Q(x)=0 for an event that later appears. Forward KL then becomes infinite.

Common fix: **additive smoothing** (Laplace/Dirichlet priors) so Q(x)>0Q(x)>0Q(x)>0 for all xxx.

This is not a hack; it encodes uncertainty and prevents “impossible” predictions from finite data artifacts.

## Applications and Connections: Cross-Entropy, VAEs/ELBO, and Information Bottleneck

### Cross-entropy: the most common place you see KL

You already know entropy H(P)H(P)H(P). Cross-entropy between PPP and QQQ is

H(P,Q)=−Ex∼P[log⁡Q(x)].H(P,Q)=-\mathbb{E}\_{x\sim P}[\log Q(x)].H(P,Q)=−Ex∼P​[logQ(x)].

And the identity

H(P,Q)=H(P)+DKL(P∥∥Q)H(P,Q)=H(P)+D\_{\mathrm{KL}}(P\|\|Q)H(P,Q)=H(P)+DKL​(P∥∥Q)

says: **cross-entropy is entropy plus a mismatch penalty.**

In classification, PPP is often a one-hot (or soft) label distribution and QQQ is the model’s predicted probabilities. Minimizing cross-entropy is minimizing KL (since H(P)H(P)H(P) doesn’t depend on model parameters).

This is why KL is not just a theoretical object—it is embedded in the training objective of most neural classifiers.

### Variational Autoencoders (VAEs): KL as a regularizer via ELBO

In VAEs, we introduce latent variables zzz and want to maximize log⁡pθ(x)\log p\_\theta(x)logpθ​(x), but the posterior pθ(z∣x)p\_\theta(z\mid x)pθ​(z∣x) is intractable.

We choose an approximate posterior qϕ(z∣x)q\_\phi(z\mid x)qϕ​(z∣x) and maximize the ELBO:

L(θ,ϕ;x)=Ez∼qϕ(z∣x)[log⁡pθ(x∣z)]−DKL(qϕ(z∣x)∥∥p(z)).\mathcal{L}(\theta,\phi; x)=\mathbb{E}\_{z\sim q\_\phi(z\mid x)}[\log p\_\theta(x\mid z)] - D\_{\mathrm{KL}}(q\_\phi(z\mid x)\|\|p(z)).L(θ,ϕ;x)=Ez∼qϕ​(z∣x)​[logpθ​(x∣z)]−DKL​(qϕ​(z∣x)∥∥p(z)).

Two important KL-related insights:

1. 1)The KL term is **reverse KL** (approx posterior to prior). It encourages qϕ(z∣x)q\_\phi(z\mid x)qϕ​(z∣x) not to drift too far from p(z)p(z)p(z).
2. 2)The ELBO can be derived by rewriting log⁡pθ(x)\log p\_\theta(x)logpθ​(x) and inserting qϕq\_\phiqϕ​; the gap between log⁡pθ(x)\log p\_\theta(x)logpθ​(x) and ELBO is itself a KL:

log⁡pθ(x)−L(θ,ϕ;x)=DKL(qϕ(z∣x)∥∥pθ(z∣x)).\log p\_\theta(x) - \mathcal{L}(\theta,\phi; x) = D\_{\mathrm{KL}}\big(q\_\phi(z\mid x)\|\|p\_\theta(z\mid x)\big).logpθ​(x)−L(θ,ϕ;x)=DKL​(qϕ​(z∣x)∥∥pθ​(z∣x)).

So maximizing ELBO is minimizing a KL divergence to the true posterior.

This is a major “KL is everywhere” moment: it measures how far your approximation is from an intractable truth.

### Information Bottleneck: KL as a constraint on information

The information bottleneck trades off:

- •how much information a representation TTT retains about XXX
- •vs how much it preserves about target YYY

Mutual information is defined via KL:

I(X;T)=DKL(p(x,t)∥∥p(x)p(t)).I(X;T)=D\_{\mathrm{KL}}(p(x,t)\|\|p(x)p(t)).I(X;T)=DKL​(p(x,t)∥∥p(x)p(t)).

So KL is the primitive object beneath mutual information. The bottleneck objective can be written using KL-based quantities, and many derivations rely on KL manipulations.

### A unifying mental model

Across these applications, KL is playing the same role:

- •There is a “reference truth” distribution (data labels, true posterior, joint distribution).
- •There is a “model/approximation” distribution.
- •KL measures the **average log mismatch**—the penalty you pay for pretending your approximation is real.

### Visualization prompt: KL as a landscape to optimize

**Canvas D: loss surface in parameter space**

Take a simple family QθQ\_\thetaQθ​ (e.g., Bernoulli with parameter qqq) and a fixed target PPP (Bernoulli with parameter ppp).

Plot DKL(P∥∥Qθ)D\_{\mathrm{KL}}(P\|\|Q\_\theta)DKL​(P∥∥Qθ​) as a function of qqq.

Prompts:

- •Notice convexity in qqq for Bernoulli forward KL.
- •Watch how gradients blow up near q→0q\to 0q→0 when p>0p>0p>0.

This links KL to optimization behavior: sometimes the objective is smooth and well-behaved; sometimes it has steep cliffs because of near-zero probabilities.

That optimization intuition is crucial when you later study:

- •numerical stability in softmax/cross-entropy
- •KL annealing in VAEs
- •mode collapse and distribution mismatch in generative models

## Worked Examples (3)

### Compute KL for Bernoulli distributions and see the blow-up

Let P=Bern(p)P=\mathrm{Bern}(p)P=Bern(p) and Q=Bern(q)Q=\mathrm{Bern}(q)Q=Bern(q). Outcomes are x∈{0,1}x\in\{0,1\}x∈{0,1} with P(1)=pP(1)=pP(1)=p, P(0)=1−pP(0)=1-pP(0)=1−p and similarly for QQQ.

1. Write the discrete KL definition:

   DKL(P∥∥Q)=∑x∈{0,1}P(x)log⁡P(x)Q(x).D\_{\mathrm{KL}}(P\|\|Q)=\sum\_{x\in\{0,1\}} P(x)\log\frac{P(x)}{Q(x)}.DKL​(P∥∥Q)=x∈{0,1}∑​P(x)logQ(x)P(x)​.
2. Expand the sum over the two outcomes:

   DKL(P∥∥Q)=P(1)log⁡P(1)Q(1)+P(0)log⁡P(0)Q(0).D\_{\mathrm{KL}}(P\|\|Q)=P(1)\log\frac{P(1)}{Q(1)} + P(0)\log\frac{P(0)}{Q(0)}.DKL​(P∥∥Q)=P(1)logQ(1)P(1)​+P(0)logQ(0)P(0)​.
3. Substitute P(1)=pP(1)=pP(1)=p, Q(1)=qQ(1)=qQ(1)=q, P(0)=1−pP(0)=1-pP(0)=1−p, Q(0)=1−qQ(0)=1-qQ(0)=1−q:

   DKL(Bern(p)∥∥Bern(q))=plog⁡pq+(1−p)log⁡1−p1−q.D\_{\mathrm{KL}}(\mathrm{Bern}(p)\|\|\mathrm{Bern}(q))=p\log\frac{p}{q} + (1-p)\log\frac{1-p}{1-q}.DKL​(Bern(p)∥∥Bern(q))=plogqp​+(1−p)log1−q1−p​.
4. Concrete numbers (nats): let p=0.2p=0.2p=0.2.

   - •If q=0.2q=0.2q=0.2, then each log ratio is 0, so KL = 0.
   - •If q=0.02q=0.02q=0.02:

   D=0.2log⁡0.20.02+0.8log⁡0.80.98.D=0.2\log\frac{0.2}{0.02} + 0.8\log\frac{0.8}{0.98}.D=0.2log0.020.2​+0.8log0.980.8​.

   Compute pieces:

   $0.2\log 10 \approx 0.2\cdot 2.3026=0.4605$.

   $0.8\log(0.8163)\approx 0.8\cdot(-0.203)= -0.1624$.

   So D≈0.2981D\approx 0.2981D≈0.2981 nats.

   - •If q→0q\to 0q→0:

   The term plog⁡pq→∞p\log\frac{p}{q}\to\inftyplogqp​→∞ as log⁡(1/q)→∞\log(1/q)\to\inftylog(1/q)→∞. Hence KL blows up.

**Insight:** Even with only two outcomes, the asymmetry is visible: if the true event probability p>0p>0p>0 but the model sets qqq near 0, the log-loss penalty becomes arbitrarily large. This is the operational meaning of “support mismatch” in miniature.

### Show that cross-entropy decomposes into entropy + KL (with full algebra)

Let PPP be the true distribution over X\mathcal{X}X and QQQ be a model distribution. Define entropy H(P)=−∑xP(x)log⁡P(x)H(P)=-\sum\_x P(x)\log P(x)H(P)=−∑x​P(x)logP(x) and cross-entropy H(P,Q)=−∑xP(x)log⁡Q(x)H(P,Q)=-\sum\_x P(x)\log Q(x)H(P,Q)=−∑x​P(x)logQ(x).

1. Start from KL:

   DKL(P∥∥Q)=∑xP(x)log⁡P(x)Q(x).D\_{\mathrm{KL}}(P\|\|Q)=\sum\_x P(x)\log\frac{P(x)}{Q(x)}.DKL​(P∥∥Q)=x∑​P(x)logQ(x)P(x)​.
2. Split the log ratio:

   log⁡P(x)Q(x)=log⁡P(x)−log⁡Q(x).\log\frac{P(x)}{Q(x)}=\log P(x)-\log Q(x).logQ(x)P(x)​=logP(x)−logQ(x).
3. Distribute P(x)P(x)P(x) and sum:

   DKL(P∥∥Q)=∑xP(x)log⁡P(x)−∑xP(x)log⁡Q(x).\begin{aligned}
   D\_{\mathrm{KL}}(P\|\|Q)
   &=\sum\_x P(x)\log P(x) - \sum\_x P(x)\log Q(x).
   \end{aligned}DKL​(P∥∥Q)​=x∑​P(x)logP(x)−x∑​P(x)logQ(x).​
4. Multiply by -1 inside the definitions:

   ∑xP(x)log⁡P(x)=−H(P),\sum\_x P(x)\log P(x) = -H(P),x∑​P(x)logP(x)=−H(P),

   −∑xP(x)log⁡Q(x)=H(P,Q).-\sum\_x P(x)\log Q(x) = H(P,Q).−x∑​P(x)logQ(x)=H(P,Q).
5. Substitute:

   DKL(P∥∥Q)=−H(P)+H(P,Q).D\_{\mathrm{KL}}(P\|\|Q)= -H(P) + H(P,Q).DKL​(P∥∥Q)=−H(P)+H(P,Q).
6. Rearrange to get the decomposition:

   H(P,Q)=H(P)+DKL(P∥∥Q).H(P,Q)=H(P)+D\_{\mathrm{KL}}(P\|\|Q).H(P,Q)=H(P)+DKL​(P∥∥Q).

**Insight:** Cross-entropy is exactly “irreducible uncertainty” H(P)H(P)H(P) plus “model mismatch” DKL(P∥∥Q)D\_{\mathrm{KL}}(P\|\|Q)DKL​(P∥∥Q). In learning, you can’t reduce H(P)H(P)H(P) by changing your model, so training focuses on driving the KL term down.

### Reverse vs forward KL on a toy ‘two-mode’ discrete distribution

Let X={A,B,C}\mathcal{X}=\{A,B,C\}X={A,B,C}. Let the target be bimodal: P(A)=0.49P(A)=0.49P(A)=0.49, P(B)=0.49P(B)=0.49P(B)=0.49, P(C)=0.02P(C)=0.02P(C)=0.02. Consider two approximations:

- •Qcover(A)=0.45Q\_{\text{cover}}(A)=0.45Qcover​(A)=0.45, Qcover(B)=0.45Q\_{\text{cover}}(B)=0.45Qcover​(B)=0.45, Qcover(C)=0.10Q\_{\text{cover}}(C)=0.10Qcover​(C)=0.10 (covers everything)
- •Qseek(A)=0.98Q\_{\text{seek}}(A)=0.98Qseek​(A)=0.98, Qseek(B)=0.01Q\_{\text{seek}}(B)=0.01Qseek​(B)=0.01, Qseek(C)=0.01Q\_{\text{seek}}(C)=0.01Qseek​(C)=0.01 (seeks one mode)

1. Compute forward KL for QcoverQ\_{\text{cover}}Qcover​:

   D(P∥∥Q)=∑xP(x)log⁡P(x)Q(x).D(P\|\|Q)=\sum\_x P(x)\log\frac{P(x)}{Q(x)}.D(P∥∥Q)=x∑​P(x)logQ(x)P(x)​.
2. Plug in each term (nats):

   - •For A: $0.49\log(0.49/0.45)$
   - •For B: $0.49\log(0.49/0.45)$
   - •For C: $0.02\log(0.02/0.10)$
3. Approximate:

   log⁡(0.49/0.45)=log⁡(1.0889)≈0.0852\log(0.49/0.45)=\log(1.0889)\approx 0.0852log(0.49/0.45)=log(1.0889)≈0.0852.

   So A+B contribute $2\cdot 0.49\cdot 0.0852 \approx 0.0835$.

   log⁡(0.02/0.10)=log⁡(0.2)≈−1.609\log(0.02/0.10)=\log(0.2)\approx -1.609log(0.02/0.10)=log(0.2)≈−1.609.

   So C contributes $0.02\cdot(-1.609)\approx -0.0322$.

   Total forward KL ≈0.0513\approx 0.0513≈0.0513.
4. Compute forward KL for QseekQ\_{\text{seek}}Qseek​:

   Terms:

   - •A: $0.49\log(0.49/0.98)=0.49\log(0.5)\approx 0.49\cdot(-0.693)= -0.3396$
   - •B: $0.49\log(0.49/0.01)=0.49\log(49)\approx 0.49\cdot 3.892=1.907$
   - •C: $0.02\log(0.02/0.01)=0.02\log 2\approx 0.02\cdot 0.693=0.0139$

   Total forward KL ≈1.581\approx 1.581≈1.581 (much larger).
5. Now compute reverse KL for QseekQ\_{\text{seek}}Qseek​:

   D(Q∥∥P)=∑xQ(x)log⁡Q(x)P(x).D(Q\|\|P)=\sum\_x Q(x)\log\frac{Q(x)}{P(x)}.D(Q∥∥P)=x∑​Q(x)logP(x)Q(x)​.
6. Reverse KL terms (nats):

   - •A: $0.98\log(0.98/0.49)=0.98\log 2\approx 0.98\cdot 0.693=0.679$
   - •B: $0.01\log(0.01/0.49)=0.01\log(0.0204)\approx 0.01\cdot(-3.889)= -0.0389$
   - •C: $0.01\log(0.01/0.02)=0.01\log(0.5)\approx 0.01\cdot(-0.693)= -0.00693$

   Total reverse KL ≈0.633\approx 0.633≈0.633.

**Insight:** Forward KL heavily punishes missing a mode that has large PPP mass (the big log⁡(49)\log(49)log(49) term). Reverse KL weights by QQQ, so if QQQ barely allocates mass to B and C, it barely ‘feels’ being wrong there—capturing the mode-seeking tendency.

## Key Takeaways

- ✓

  KL divergence is defined as an expectation under the first distribution: DKL(P∥∥Q)=Ex∼P[log⁡P(x)Q(x)]D\_{\mathrm{KL}}(P\|\|Q)=\mathbb{E}\_{x\sim P}\left[\log\frac{P(x)}{Q(x)}\right]DKL​(P∥∥Q)=Ex∼P​[logQ(x)P(x)​].
- ✓

  Operational meaning: it is the average extra log-loss (extra bits/nats per sample) you incur when using QQQ to predict data generated by PPP.
- ✓

  KL is always nonnegative (Gibbs/Jensen), and equals 0 iff P=QP=QP=Q (almost everywhere / on the support of PPP).
- ✓

  KL is asymmetric; swapping arguments changes which regions matter because the expectation reweights by PPP vs by QQQ.
- ✓

  Support mismatch causes infinite KL: if P>0P>0P>0 where Q=0Q=0Q=0, then DKL(P∥∥Q)=∞D\_{\mathrm{KL}}(P\|\|Q)=\inftyDKL​(P∥∥Q)=∞.
- ✓

  Forward KL (P∥∥QP\|\|QP∥∥Q) tends to be mode-covering; reverse KL (Q∥∥PQ\|\|PQ∥∥P) tends to be mode-seeking in approximations.
- ✓

  Cross-entropy decomposes as H(P,Q)=H(P)+DKL(P∥∥Q)H(P,Q)=H(P)+D\_{\mathrm{KL}}(P\|\|Q)H(P,Q)=H(P)+DKL​(P∥∥Q), making KL the mismatch term behind common training losses.
- ✓

  KL is a foundational building block under ELBOs (VAEs/variational inference) and mutual information (information bottleneck).

## Common Mistakes

- ✗

  Treating KL as a symmetric distance and casually writing DKL(P∥∥Q)=DKL(Q∥∥P)D\_{\mathrm{KL}}(P\|\|Q)=D\_{\mathrm{KL}}(Q\|\|P)DKL​(P∥∥Q)=DKL​(Q∥∥P).
- ✗

  Ignoring support: computing KL numerically without guarding against zeros in QQQ (leading to infinities or NaNs).
- ✗

  Forgetting the expectation is under PPP (or under QQQ for reverse KL), leading to incorrect intuition about which errors matter.
- ✗

  Confusing cross-entropy H(P,Q)H(P,Q)H(P,Q) with entropy H(P)H(P)H(P), or assuming minimizing cross-entropy always implies QQQ matches PPP without considering model capacity and estimation error.

## Practice

easy

Let P=Bern(0.7)P=\mathrm{Bern}(0.7)P=Bern(0.7) and Q=Bern(0.4)Q=\mathrm{Bern}(0.4)Q=Bern(0.4). Compute DKL(P∥∥Q)D\_{\mathrm{KL}}(P\|\|Q)DKL​(P∥∥Q) in nats.

**Hint:** Use D=plog⁡(p/q)+(1−p)log⁡((1−p)/(1−q))D=p\log(p/q)+(1-p)\log((1-p)/(1-q))D=plog(p/q)+(1−p)log((1−p)/(1−q)).

Show solution

Here p=0.7p=0.7p=0.7, q=0.4q=0.4q=0.4.

D=0.7log⁡0.70.4+0.3log⁡0.30.6.D=0.7\log\frac{0.7}{0.4}+0.3\log\frac{0.3}{0.6}.D=0.7log0.40.7​+0.3log0.60.3​.

Compute pieces:

log⁡(0.7/0.4)=log⁡(1.75)≈0.5596\log(0.7/0.4)=\log(1.75)\approx 0.5596log(0.7/0.4)=log(1.75)≈0.5596 so first term ≈0.7⋅0.5596=0.3917\approx 0.7\cdot 0.5596=0.3917≈0.7⋅0.5596=0.3917.

log⁡(0.3/0.6)=log⁡(0.5)≈−0.6931\log(0.3/0.6)=\log(0.5)\approx -0.6931log(0.3/0.6)=log(0.5)≈−0.6931 so second term ≈0.3⋅(−0.6931)=−0.2079\approx 0.3\cdot(-0.6931)=-0.2079≈0.3⋅(−0.6931)=−0.2079.

Total D≈0.1838D\approx 0.1838D≈0.1838 nats.

medium

Prove (using Jensen’s inequality) that DKL(P∥∥Q)≥0D\_{\mathrm{KL}}(P\|\|Q)\ge 0DKL​(P∥∥Q)≥0 for discrete distributions with matching support.

**Hint:** Rewrite KL as −∑xP(x)log⁡(Q(x)/P(x))-\sum\_x P(x)\log(Q(x)/P(x))−∑x​P(x)log(Q(x)/P(x)) and apply Jensen to the concave log⁡\loglog.

Show solution

Start from

DKL(P∥∥Q)=∑xP(x)log⁡P(x)Q(x)=−∑xP(x)log⁡Q(x)P(x).D\_{\mathrm{KL}}(P\|\|Q)=\sum\_x P(x)\log\frac{P(x)}{Q(x)} = -\sum\_x P(x)\log\frac{Q(x)}{P(x)}.DKL​(P∥∥Q)=x∑​P(x)logQ(x)P(x)​=−x∑​P(x)logP(x)Q(x)​.

Since log⁡\loglog is concave, Jensen gives

∑xP(x)log⁡Q(x)P(x)≤log⁡(∑xP(x)Q(x)P(x))=log⁡(∑xQ(x))=log⁡1=0.\sum\_x P(x)\log\frac{Q(x)}{P(x)} \le \log\left(\sum\_x P(x)\frac{Q(x)}{P(x)}\right)=\log\left(\sum\_x Q(x)\right)=\log 1=0.x∑​P(x)logP(x)Q(x)​≤log(x∑​P(x)P(x)Q(x)​)=log(x∑​Q(x))=log1=0.

Therefore −∑xP(x)log⁡Q(x)P(x)≥0-\sum\_x P(x)\log\frac{Q(x)}{P(x)} \ge 0−∑x​P(x)logP(x)Q(x)​≥0, i.e. DKL(P∥∥Q)≥0D\_{\mathrm{KL}}(P\|\|Q)\ge 0DKL​(P∥∥Q)≥0.

Equality holds iff Q(x)/P(x)Q(x)/P(x)Q(x)/P(x) is constant over xxx with P(x)>0P(x)>0P(x)>0, which implies Q=PQ=PQ=P.

hard

Consider a target distribution PPP that is a mixture of two well-separated Gaussians in 1D. You approximate it with a single Gaussian family Qθ=N(μ,σ2)Q\_\theta=\mathcal{N}(\mu,\sigma^2)Qθ​=N(μ,σ2). Qualitatively, which direction (forward KL vs reverse KL) is more likely to yield a large σ\sigmaσ covering both modes, and which is more likely to pick one mode? Explain using the ‘expectation under which distribution?’ idea.

**Hint:** Forward KL weights by PPP (penalizes missing where PPP has mass). Reverse KL weights by QQQ (penalizes placing mass where PPP is small).

Show solution

Forward KL DKL(P∥∥Q)D\_{\mathrm{KL}}(P\|\|Q)DKL​(P∥∥Q) is averaged over x∼Px\sim Px∼P. If QQQ fails to assign decent density to either mode, then for many samples from the missed mode, log⁡(P(x)/Q(x))\log(P(x)/Q(x))log(P(x)/Q(x)) becomes large, heavily penalizing the fit. This tends to push QQQ toward a broader distribution (larger σ\sigmaσ) that covers both modes.

Reverse KL DKL(Q∥∥P)D\_{\mathrm{KL}}(Q\|\|P)DKL​(Q∥∥P) is averaged over x∼Qx\sim Qx∼Q. If QQQ concentrates around one mode, it rarely samples the other mode, so it does not ‘feel’ the penalty of missing it. Instead, it is strongly penalized for placing mass in the low-density valley between modes (where PPP is small), encouraging QQQ to sit on one mode with smaller σ\sigmaσ. This is the classic mode-seeking behavior.

## Connections

- •[Cross-Entropy](/tech-tree/cross-entropy/)
- •[Variational Autoencoders](/tech-tree/vae/)
- •[Information Bottleneck](/tech-tree/information-bottleneck/)

Related next-step ideas you’ll likely want soon:

- •Mutual information I(X;Y)I(X;Y)I(X;Y) as a KL between joint and product of marginals
- •Jensen–Shannon divergence as a symmetrized, smoothed cousin of KL (useful in GANs)
- •f-divergences (KL is one member of a larger family)

Quality: A (4.4/5)

[← back to tree](/tech-tree/)[browse all →](/tech-tree/inventory/)
