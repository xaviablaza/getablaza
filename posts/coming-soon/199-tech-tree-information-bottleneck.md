---
title: Information Bottleneck
description: Compression that preserves relevant information.
date: '2026-07-01'
scheduled: '2027-01-15'
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
inspiration_url: https://templeton.host/tech-tree/information-bottleneck/
inspiration_category: tech-tree
---

> Source-copy draft imported from [https://templeton.host/tech-tree/information-bottleneck/](https://templeton.host/tech-tree/information-bottleneck/). Names, domain references, and local media paths were adapted for Xavi Ablaza / getablaza.com.

[←Back to Tech Tree](/tech-tree/)

[inventory](/tech-tree/inventory/)[coverage](/tech-tree/coverage/)

# Information Bottleneck

Information TheoryDifficulty: ★★★★☆Depth: 8Unlocks: 0

Compression that preserves relevant information.

## Interactive Visualization

⏮◀◀▶▶STEP0.25x1xZOOM

t=0s

## Core Concepts

- -Compression-relevance trade-off: compress X while preserving information about Y
- -Bottleneck variable T: a compressed/latent representation of X that should retain relevant information about Y

## Key Symbols & Notation

T (bottleneck / compressed latent variable)beta (positive trade-off / Lagrange multiplier)

## Essential Relationships

- -Markov chain Y - X - T (T is produced from X; no direct dependence of T on Y)
- -IB objective: minimize I(X;T) - beta \* I(T;Y) (equivalently maximize I(T;Y) - beta \* I(X;T)) to balance compression and relevance

## Prerequisites (2)

[Mutual Information5 atoms](/tech-tree/mutual-information/)[KL Divergence6 atoms](/tech-tree/kl-divergence/)

## Referenced by (2)

Where this concept shows up in the operating-finance and personal-finance graphs.

### From Business (2)

[Informational AdvantageBusiness

A CTO who doesn't build receives system state through an information bottleneck (reports, dashboards, team summaries) that compresses away relevant detail; building directly bypasses this lossy channel](/business/informational-advantage/)[executive summaryBusiness

An executive summary is lossy compression of a full document under the constraint that all flagged clauses (relevant information) are preserved. The information bottleneck formalizes exactly this tradeoff: minimize description length while retaining specified mutual information with the source.](/business/executive-summary/)

Advanced Learning Details

### Graph Position

113

Depth Cost

0

Fan-Out (ROI)

0

Bottleneck Score

8

Chain Length

### Cognitive Load

6

Atomic Elements

32

Total Elements

L1

Percentile Level

L4

Atomic Level

### All Concepts (12)

- - Compressed representation T: a new random variable that encodes X with reduced information
- - Information preservation/relevance: the idea of preserving information in T that is specifically relevant to predicting Y
- - IB objective (trade-off) as a design goal: compress X while keeping predictive information about Y
- - Lagrangian and constrained formulations: optimizing a trade-off via a Lagrange multiplier or via a constrained optimization
- - Trade-off parameter beta (β): a scalar that controls the emphasis on relevance versus compression
- - Stochastic encoder/decoder viewpoint: using probabilistic mappings p(t|x) and p(y|t) rather than deterministic mappings
- - Distortion-as-KL interpretation: measuring representational distortion by the KL divergence between conditional predictive distributions
- - Predictive clustering: representing X by clustering inputs that have similar conditional distributions p(y|x)
- - Information Bottleneck (IB) curve / information plane: the frontier of achievable pairs (I(X;T), I(T;Y))
- - Sufficiency and minimal sufficient representation: T is sufficient for Y if it preserves I(T;Y)=I(X;Y); minimal sufficiency minimizes I(X;T) among sufficient T
- - Markov chain constraint for encoders: the encoder must satisfy the conditional-independence structure Y - X - T (T depends only on X)
- - Phase/structural transitions in optimal representations as β varies (changes in number/shape of clusters or support of p(t|x))

### Teaching Strategy

Multi-session curriculum - substantial prior knowledge and complex material. Use mastery gates and deliberate practice.

You have data X that contains “everything,” but your downstream task only cares about Y. The Information Bottleneck principle asks: can we compress X into a smaller representation T that forgets irrelevant details, while keeping what matters for predicting Y?

TL;DR:

Information Bottleneck (IB) formalizes representation learning as a trade-off: minimize I(X;T) (compression) while maximizing I(T;Y) (relevance). With a Lagrange multiplier β>0, IB solves for a stochastic encoder p(t|x) that produces a bottleneck variable T, under the Markov chain T–X–Y. The discrete IB has fixed-point updates; the practical “Variational IB” (VIB) replaces intractable mutual informations with variational bounds, yielding a loss that looks like prediction loss + β·KL regularization—closely related to β-VAEs and regularized neural classifiers.

## What Is Information Bottleneck?

### The problem IB is trying to solve (why before how)

In many learning settings, your input variable XXX contains a mix of:

- •**Signal**: aspects of XXX that help predict a target YYY (labels, future outcomes, etc.).
- •**Nuisance**: aspects of XXX that are unrelated to YYY (noise, style, background, idiosyncrasies).

If you let a model store *everything* about XXX, it can overfit, memorize, or learn brittle features. If you compress too aggressively, you lose predictive power.

The Information Bottleneck (IB) framework turns this into a clean information-theoretic optimization:

- •Create a compressed representation TTT of XXX.
- •Ensure TTT retains information about YYY.

Here TTT is called the **bottleneck variable** because it limits how much information from XXX can flow downstream.

### The IB story in one line

Find a stochastic mapping p(t∣x)p(t|x)p(t∣x) such that:

- •TTT is **as independent of $X$ as possible** (compression)
- •while TTT is **as informative about $Y$ as possible** (relevance)

The standard IB Lagrangian is:

min⁡p(t∣x)  LIB=I(X;T)−β I(T;Y),β>0.\min\_{p(t|x)} \; \mathcal{L}\_{IB} = I(X;T) - \beta \, I(T;Y), \quad \beta>0.p(t∣x)min​LIB​=I(X;T)−βI(T;Y),β>0.

Interpretation:

- •I(X;T)I(X;T)I(X;T): how many bits TTT “remembers” about XXX. Smaller means stronger compression.
- •I(T;Y)I(T;Y)I(T;Y): how many bits TTT carries about YYY. Larger means better relevance.
- •β\betaβ: trade-off knob.
- •Small β\betaβ → prioritize compression (small I(X;T)I(X;T)I(X;T)), risk losing predictive info.
- •Large β\betaβ → prioritize relevance (large I(T;Y)I(T;Y)I(T;Y)), allow more capacity.

### A key modeling assumption: the Markov chain

IB usually assumes the representation is formed from XXX alone:

T  −  X  −  YT \; - \; X \; - \; YT−X−Y

This means: given XXX, TTT is independent of YYY (because you compute TTT from XXX).

Formally:

p(t∣x,y)=p(t∣x).p(t|x,y) = p(t|x).p(t∣x,y)=p(t∣x).

This assumption is not just a technicality—it encodes the idea that **you don’t get to peek at the label $Y$ when forming the representation** (at test time, you only see XXX).

### “Compression” vs “relevance” as two competing forces

It helps to visualize two extremes:

| Setting | What happens | Risk |
| --- | --- | --- |
| Very strong compression (force I(X;T)I(X;T)I(X;T) small) | TTT discards many details of XXX | TTT may lose predictive info about YYY |
| Very strong relevance (force I(T;Y)I(T;Y)I(T;Y) large) | TTT keeps whatever helps predict YYY | TTT may retain lots of XXX (less robust/generalizable) |

IB doesn’t assume you know which parts of XXX are relevant. It discovers them by optimizing these two pressures.

---

### Pause and check 1 (sanity questions)

Before going further, make sure these answers feel clear:

1. 1)If TTT is a copy of XXX, what is I(X;T)I(X;T)I(X;T) likely to be? (Large—approximately H(X)H(X)H(X).)
2. 2)If TTT is constant (always the same value), what are I(X;T)I(X;T)I(X;T) and I(T;Y)I(T;Y)I(T;Y)? (Both 0.)
3. 3)Why is β\betaβ needed? (Because you can’t generally minimize I(X;T)I(X;T)I(X;T) and maximize I(T;Y)I(T;Y)I(T;Y) simultaneously without trading them off.)

If those are intuitive, you’re ready for the mechanics.

## Core Mechanic 1: The IB Objective and What It Really Measures

### Step 1: Start from what we control

We do not choose p(x,y)p(x,y)p(x,y); it comes from the world/data. What we *can* choose is an encoder (possibly stochastic):

p(t∣x).p(t|x).p(t∣x).

Together with p(x,y)p(x,y)p(x,y), this induces:

- •p(t)=∑xp(x)p(t∣x)p(t) = \sum\_x p(x) p(t|x)p(t)=∑x​p(x)p(t∣x)
- •p(y∣t)=∑xp(y∣x)p(x∣t)p(y|t) = \sum\_x p(y|x) p(x|t)p(y∣t)=∑x​p(y∣x)p(x∣t)

### Step 2: Expand the two mutual informations

Recall the mutual information identities:

I(X;T)=∑x,tp(x,t)log⁡p(t∣x)p(t).I(X;T) = \sum\_{x,t} p(x,t) \log \frac{p(t|x)}{p(t)}.I(X;T)=x,t∑​p(x,t)logp(t)p(t∣x)​.

And

I(T;Y)=∑t,yp(t,y)log⁡p(y∣t)p(y).I(T;Y) = \sum\_{t,y} p(t,y) \log \frac{p(y|t)}{p(y)}.I(T;Y)=t,y∑​p(t,y)logp(y)p(y∣t)​.

The IB Lagrangian:

LIB=I(X;T)−βI(T;Y)\mathcal{L}\_{IB} = I(X;T) - \beta I(T;Y)LIB​=I(X;T)−βI(T;Y)

is therefore a functional of the entire conditional distribution p(t∣x)p(t|x)p(t∣x).

### What I(X;T)I(X;T)I(X;T) means operationally

Think of transmitting TTT given XXX. If TTT contains many distinguishable states for different xxx, then TTT carries many bits about XXX. If many different xxx map to similar distributions over ttt, then TTT forgets details.

A useful equivalent form is:

I(X;T)=H(T)−H(T∣X).I(X;T) = H(T) - H(T|X).I(X;T)=H(T)−H(T∣X).

- •Increasing stochasticity in the encoder (larger H(T∣X)H(T|X)H(T∣X)) can reduce I(X;T)I(X;T)I(X;T).
- •But if you make the encoder too noisy, you may also reduce I(T;Y)I(T;Y)I(T;Y).

### What I(T;Y)I(T;Y)I(T;Y) means operationally

TTT is “good” if it makes YYY predictable. Another identity:

I(T;Y)=H(Y)−H(Y∣T).I(T;Y) = H(Y) - H(Y|T).I(T;Y)=H(Y)−H(Y∣T).

Since H(Y)H(Y)H(Y) is fixed by data, maximizing I(T;Y)I(T;Y)I(T;Y) is equivalent to minimizing the conditional entropy H(Y∣T)H(Y|T)H(Y∣T): make YYY as predictable from TTT as possible.

### The IB curve (rate–distortion flavor)

If you fix a compression budget I(X;T)≤RI(X;T) \le RI(X;T)≤R and maximize relevance, you get a curve of optimal trade-offs. Equivalently, the Lagrangian with β\betaβ traces that curve.

This parallels rate–distortion theory:

- •Rate ↔ I(X;T)I(X;T)I(X;T)
- •Distortion ↔ a loss of predictive info about YYY

IB can be seen as a *task-aware* compression method.

---

### Pause and check 2 (micro-summary)

At this point:

- •We choose **an encoder** p(t∣x)p(t|x)p(t∣x).
- •I(X;T)I(X;T)I(X;T) penalizes how much TTT remembers about XXX.
- •I(T;Y)I(T;Y)I(T;Y) rewards how much TTT helps predict YYY.

Quick self-test:

- •If you increase β\betaβ, do you expect I(T;Y)I(T;Y)I(T;Y) to go up or down at the optimum? (Up.)
- •If you decrease β\betaβ, do you expect I(X;T)I(X;T)I(X;T) to go up or down? (Down.)

Now we’ll derive the *structure* of the optimal p(t∣x)p(t|x)p(t∣x) in the discrete case.

## Core Mechanic 2: Discrete IB and the Fixed-Point Equations

### Why fixed-point equations appear

The IB optimization is over distributions, not over a few parameters. In the discrete setting (finite XXX, YYY, TTT), the classic IB solution gives self-consistent update rules for:

- •the encoder p(t∣x)p(t|x)p(t∣x)
- •the cluster prior p(t)p(t)p(t)
- •the decoder p(y∣t)p(y|t)p(y∣t)

This resembles a “soft clustering” procedure where each xxx is assigned probabilistically to bottleneck states ttt.

### Set up the constrained optimization

We minimize

LIB=I(X;T)−βI(T;Y)\mathcal{L}\_{IB} = I(X;T) - \beta I(T;Y)LIB​=I(X;T)−βI(T;Y)

subject to the normalization constraints:

∑tp(t∣x)=1∀x.\sum\_t p(t|x)=1 \quad \forall x.t∑​p(t∣x)=1∀x.

We also rely on the Markov chain T−X−YT-X-YT−X−Y.

### Key identity: relevance term becomes a KL to class-conditionals

A central result in IB is that the optimal encoder depends on how different p(y∣x)p(y|x)p(y∣x) is from p(y∣t)p(y|t)p(y∣t). The natural measure of “difference between predictive distributions” is KL divergence.

Define the KL:

DKL(p(y∣x)∥p(y∣t))=∑yp(y∣x)log⁡p(y∣x)p(y∣t).D\_{KL}(p(y|x) \| p(y|t)) = \sum\_y p(y|x)\log\frac{p(y|x)}{p(y|t)}.DKL​(p(y∣x)∥p(y∣t))=y∑​p(y∣x)logp(y∣t)p(y∣x)​.

Intuition: if xxx and bottleneck state ttt imply similar label distributions, then assigning xxx to ttt costs little relevance.

### The fixed-point form (the classic IB equations)

The discrete IB solution satisfies:

1) **Encoder update**

p(t∣x)=p(t)Z(x,β)exp⁡(−β DKL(p(y∣x)∥p(y∣t)))p(t|x) = \frac{p(t)}{Z(x,\beta)} \exp\Big(-\beta\, D\_{KL}(p(y|x)\|p(y|t))\Big)p(t∣x)=Z(x,β)p(t)​exp(−βDKL​(p(y∣x)∥p(y∣t)))

where Z(x,β)Z(x,\beta)Z(x,β) is a normalizer:

Z(x,β)=∑tp(t)exp⁡(−β DKL(p(y∣x)∥p(y∣t))).Z(x,\beta)=\sum\_t p(t)\exp\Big(-\beta\, D\_{KL}(p(y|x)\|p(y|t))\Big).Z(x,β)=t∑​p(t)exp(−βDKL​(p(y∣x)∥p(y∣t))).

2) **Cluster prior update**

p(t)=∑xp(x)p(t∣x).p(t) = \sum\_x p(x) p(t|x).p(t)=x∑​p(x)p(t∣x).

3) **Decoder (label distribution per cluster)**

p(y∣t)=∑xp(y∣x)p(x∣t)p(y|t) = \sum\_x p(y|x) p(x|t)p(y∣t)=x∑​p(y∣x)p(x∣t)

and using Bayes:

p(x∣t)=p(x)p(t∣x)p(t).p(x|t)=\frac{p(x)p(t|x)}{p(t)}.p(x∣t)=p(t)p(x)p(t∣x)​.

Putting it together, (3) is often written as:

p(y∣t)=1p(t)∑xp(x)p(t∣x)p(y∣x).p(y|t) = \frac{1}{p(t)}\sum\_x p(x)p(t|x)p(y|x).p(y∣t)=p(t)1​x∑​p(x)p(t∣x)p(y∣x).

### Show-your-work sketch: where does the exponential form come from?

We’ll outline the logic (not every calculus-of-variations detail, but the key steps).

Start with:

I(X;T)=∑x,tp(x)p(t∣x)log⁡p(t∣x)p(t).I(X;T)=\sum\_{x,t} p(x)p(t|x)\log\frac{p(t|x)}{p(t)}.I(X;T)=x,t∑​p(x)p(t∣x)logp(t)p(t∣x)​.

For the relevance term, using I(T;Y)=∑tp(t)∑yp(y∣t)log⁡p(y∣t)p(y)I(T;Y)=\sum\_{t}p(t)\sum\_y p(y|t)\log\frac{p(y|t)}{p(y)}I(T;Y)=∑t​p(t)∑y​p(y∣t)logp(y)p(y∣t)​.

When you take the functional derivative of LIB\mathcal{L}\_{IB}LIB​ with respect to p(t∣x)p(t|x)p(t∣x) and enforce ∑tp(t∣x)=1\sum\_t p(t|x)=1∑t​p(t∣x)=1 using Lagrange multipliers λ(x)\lambda(x)λ(x), the stationary condition yields something of the form:

log⁡p(t∣x)=log⁡p(t)−β DKL(p(y∣x)∥p(y∣t))−λ(x).\log p(t|x) = \log p(t) - \beta\, D\_{KL}(p(y|x)\|p(y|t)) - \lambda(x).logp(t∣x)=logp(t)−βDKL​(p(y∣x)∥p(y∣t))−λ(x).

Exponentiate both sides:

p(t∣x)∝p(t)exp⁡(−βDKL(p(y∣x)∥p(y∣t)))p(t|x) \propto p(t)\exp\big(-\beta D\_{KL}(p(y|x)\|p(y|t))\big)p(t∣x)∝p(t)exp(−βDKL​(p(y∣x)∥p(y∣t)))

and the proportionality constant is exactly $1/Z(x,\beta)$.

### Intuition: IB as soft clustering of inputs by label-meaning

The encoder update says:

- •p(t)p(t)p(t) favors common clusters.
- •The exponential penalizes assigning xxx to clusters whose label-distribution p(y∣t)p(y|t)p(y∣t) mismatches p(y∣x)p(y|x)p(y∣x).
- •β\betaβ controls how “hard” the assignments become.

As β→0\beta \to 0β→0, the KL term is downweighted and assignments become dominated by p(t)p(t)p(t) (compression wins).

As β→∞\beta \to \inftyβ→∞, the encoder strongly prefers clusters that match p(y∣x)p(y|x)p(y∣x) (relevance wins), potentially making TTT preserve nearly all predictive structure.

---

### Pause and check 3 (sanity and pacing)

Answer these before moving on:

1. 1)In the encoder update, what happens if p(y∣x)=p(y∣t)p(y|x)=p(y|t)p(y∣x)=p(y∣t) exactly? (KL=0, so xxx can be assigned to ttt with no relevance penalty.)
2. 2)Why does a KL divergence appear rather than, say, squared error? (Because we compare *distributions* over YYY; KL is the natural information-theoretic discrepancy.)
3. 3)What makes these equations “fixed-point”? (Each update uses the others; iterating them seeks a self-consistent solution.)

Next we’ll shift from theory (discrete exact IB) to practice (continuous/high-dimensional settings).

## Application/Connection: From Exact IB to Variational Information Bottleneck (VIB) and Deep Learning

### Flagging the shift: why we need a variational approximation

The discrete IB fixed-point equations are elegant, but they assume we can:

- •Sum over all xxx, ttt, and yyy.
- •Represent p(t∣x)p(t|x)p(t∣x) as a full table.
- •Compute p(y∣x)p(y|x)p(y∣x) from the data distribution.

In modern ML:

- •XXX is high-dimensional (images, text).
- •TTT is continuous (latent vectors).
- •p(y∣x)p(y|x)p(y∣x) is unknown; we only have samples.

So we use **Variational Information Bottleneck (VIB)**: an optimization that *resembles* IB but is tractable with neural networks and minibatches.

### The VIB setup

We parameterize:

- •Encoder qϕ(t∣x)q\_\phi(t|x)qϕ​(t∣x) (neural net producing a distribution, often Gaussian)
- •Decoder/predictor pθ(y∣t)p\_\theta(y|t)pθ​(y∣t) (classifier/regressor)
- •A prior over latents p(t)p(t)p(t) (often standard normal)

Goal: keep TTT predictive of YYY while limiting information from XXX into TTT.

### Replace the intractable terms with bounds

#### Relevance term

We want to maximize I(T;Y)=H(Y)−H(Y∣T)I(T;Y)=H(Y)-H(Y|T)I(T;Y)=H(Y)−H(Y∣T). Since H(Y)H(Y)H(Y) is constant, we minimize H(Y∣T)H(Y|T)H(Y∣T).

In practice, we minimize negative log-likelihood under a decoder:

Ep(x,y) Eqϕ(t∣x)[−log⁡pθ(y∣t)].\mathbb{E}\_{p(x,y)}\,\mathbb{E}\_{q\_\phi(t|x)}[-\log p\_\theta(y|t)].Ep(x,y)​Eqϕ​(t∣x)​[−logpθ​(y∣t)].

This is a standard prediction loss.

#### Compression term

The IB compression term is I(X;T)I(X;T)I(X;T). In VIB, a common upper bound is:

I(X;T)≤Ep(x)[DKL(qϕ(t∣x)∥p(t))].I(X;T) \le \mathbb{E}\_{p(x)}\left[D\_{KL}(q\_\phi(t|x)\|p(t))\right].I(X;T)≤Ep(x)​[DKL​(qϕ​(t∣x)∥p(t))].

Why this makes sense (sketch):

- •I(X;T)=Ep(x)DKL(q(t∣x)∥q(t))I(X;T)=\mathbb{E}\_{p(x)} D\_{KL}(q(t|x)\|q(t))I(X;T)=Ep(x)​DKL​(q(t∣x)∥q(t)).
- •q(t)q(t)q(t) is the aggregated posterior, hard to compute.
- •Replacing q(t)q(t)q(t) with a chosen prior p(t)p(t)p(t) yields an upper bound.

### The VIB objective (the practical loss)

Putting these together gives a common VIB training objective:

min⁡ϕ,θ  LVIB=Ep(x,y) Eqϕ(t∣x)[−log⁡pθ(y∣t)]+β Ep(x)[DKL(qϕ(t∣x)∥p(t))].\min\_{\phi,\theta}\; \mathcal{L}\_{VIB} = \mathbb{E}\_{p(x,y)}\,\mathbb{E}\_{q\_\phi(t|x)}[-\log p\_\theta(y|t)] + \beta\, \mathbb{E}\_{p(x)}\left[D\_{KL}(q\_\phi(t|x)\|p(t))\right].ϕ,θmin​LVIB​=Ep(x,y)​Eqϕ​(t∣x)​[−logpθ​(y∣t)]+βEp(x)​[DKL​(qϕ​(t∣x)∥p(t))].

Compare to IB:

- •Prediction loss corresponds to maximizing relevance.
- •KL regularizer corresponds to compression.
- •β\betaβ again controls the trade-off.

### Connection map: IB, β-VAE, and regularization

VIB looks structurally similar to other objectives:

| Method | Objective shape | What it’s for |
| --- | --- | --- |
| IB | I(X;T)−βI(T;Y)I(X;T) - \beta I(T;Y)I(X;T)−βI(T;Y) | theory of optimal representations |
| VIB | NLL($y | t)+) + )+\betaKL( KL(KL(q(t | x)\ | p(t)$) | supervised representation learning |
| β-VAE | reconstruction + β\betaβ KL($q(z | x)\ | p(z)$) | unsupervised disentangling/regularization |

Key difference: VIB uses YYY in the decoder; β-VAE reconstructs XXX.

### Practical encoder choice: Gaussian + reparameterization

A common choice is:

qϕ(t∣x)=N(μϕ(x),diag(σϕ2(x))).q\_\phi(t|x) = \mathcal{N}(\mu\_\phi(x), \mathrm{diag}(\sigma^2\_\phi(x))).qϕ​(t∣x)=N(μϕ​(x),diag(σϕ2​(x))).

Sampling is done via the reparameterization trick:

t=μϕ(x)+σϕ(x)⊙ϵ,ϵ∼N(0,I).t = \mu\_\phi(x) + \sigma\_\phi(x) \odot \epsilon, \quad \epsilon\sim\mathcal{N}(0,I).t=μϕ​(x)+σϕ​(x)⊙ϵ,ϵ∼N(0,I).

This makes gradients flow through stochastic sampling.

### Why VIB can improve robustness and generalization

The KL term pushes qϕ(t∣x)q\_\phi(t|x)qϕ​(t∣x) toward a simple prior (like N(0,I)\mathcal{N}(0,I)N(0,I)). That tends to:

- •limit memorization (capacity control)
- •encourage smoother representations
- •reduce sensitivity to nuisance variation in XXX

But if β\betaβ is too large, you get **posterior collapse** (the encoder ignores XXX and TTT carries little information), harming prediction.

---

### Pause and check 4 (explicit bridge from theory to practice)

Make sure you can articulate these two transitions:

1. 1)**Exact IB → VIB**: We can’t compute I(X;T)I(X;T)I(X;T) and I(T;Y)I(T;Y)I(T;Y) exactly in deep settings, so we optimize a surrogate using NLL and a KL-to-prior.
2. 2)**$p(t|x)$ → $q\_\phi(t|x)$**: We move from an unconstrained distribution to a parameterized family (neural network).

If that’s clear, the worked examples will feel grounded rather than magical.

## Worked Examples (3)

### Discrete IB: One encoder update step on a tiny problem

Let X∈{x₁,x₂}, Y∈{0,1}, T∈{t₁,t₂}. Suppose p(x₁)=p(x₂)=0.5.

Assume the label conditionals are:

- •p(y=1|x₁)=0.9, p(y=0|x₁)=0.1
- •p(y=1|x₂)=0.2, p(y=0|x₂)=0.8

Initialize p(t₁)=p(t₂)=0.5 and choose decoder distributions:

- •p(y=1|t₁)=0.8, p(y=0|t₁)=0.2
- •p(y=1|t₂)=0.3, p(y=0|t₂)=0.7

Let β=2. Compute p(t|x) using the IB encoder update.

1. Write the encoder update:

   p(t|x) = [p(t)/Z(x,β)] · exp(-β · D\_KL(p(y|x) || p(y|t))).
2. Compute D\_KL for x₁ vs each t.

   For t₁:

   D₁ = 0.9·log(0.9/0.8) + 0.1·log(0.1/0.2)

   = 0.9·log(1.125) + 0.1·log(0.5)

   ≈ 0.9·0.1173 + 0.1·(-0.6931)

   ≈ 0.1056 - 0.0693

   ≈ 0.0363.

   For t₂:

   D₂ = 0.9·log(0.9/0.3) + 0.1·log(0.1/0.7)

   = 0.9·log(3) + 0.1·log(1/7)

   ≈ 0.9·1.0986 + 0.1·(-1.9459)

   ≈ 0.9887 - 0.1946

   ≈ 0.7941.
3. Compute unnormalized weights for x₁:

   w(t₁|x₁)=p(t₁)·exp(-βD₁)=0.5·exp(-2·0.0363)

   =0.5·exp(-0.0726)≈0.5·0.9300≈0.4650.

   w(t₂|x₁)=0.5·exp(-2·0.7941)=0.5·exp(-1.5882)

   ≈0.5·0.2043≈0.1021.
4. Normalize:

   Z(x₁,β)=0.4650+0.1021=0.5671.

   p(t₁|x₁)=0.4650/0.5671≈0.820.

   p(t₂|x₁)=0.1021/0.5671≈0.180.
5. Repeat for x₂.

   Compute KLs:

   For t₁:

   D₃ = 0.2·log(0.2/0.8) + 0.8·log(0.8/0.2)

   = 0.2·log(0.25) + 0.8·log(4)

   ≈ 0.2·(-1.3863) + 0.8·(1.3863)

   ≈ -0.2773 + 1.1090

   ≈ 0.8317.

   For t₂:

   D₄ = 0.2·log(0.2/0.3) + 0.8·log(0.8/0.7)

   ≈ 0.2·(-0.4055) + 0.8·(0.1335)

   ≈ -0.0811 + 0.1068

   ≈ 0.0257.
6. Weights for x₂:

   w(t₁|x₂)=0.5·exp(-2·0.8317)=0.5·exp(-1.6634)

   ≈0.5·0.1893≈0.0946.

   w(t₂|x₂)=0.5·exp(-2·0.0257)=0.5·exp(-0.0514)

   ≈0.5·0.9499≈0.4750.

   Normalize:

   Z(x₂,β)=0.0946+0.4750=0.5696.

   p(t₁|x₂)=0.0946/0.5696≈0.166.

   p(t₂|x₂)=0.4750/0.5696≈0.834.

**Insight:** The encoder assigns x₁ mostly to t₁ and x₂ mostly to t₂ because those clusters have similar label distributions. β controls how sharply the KL mismatch turns into near-hard assignments.

### VIB loss on a single datapoint with a Gaussian bottleneck

Binary classification with y∈{0,1}. Let the bottleneck T be 1D.

Assume encoder qϕ(t|x)=N(μ,σ²) outputs μ=1.0 and σ=0.5 for this x.

Use prior p(t)=N(0,1).

Decoder pθ(y=1|t)=sigmoid(wt+b) with w=2, b=0. Suppose the true label is y=1.

Let β=0.1. Compute the per-example VIB loss approximately using one Monte Carlo sample ε=0 (so t=μ).

1. Sample t using reparameterization:

   t = μ + σ·ε. With ε=0:

   t = 1.0 + 0.5·0 = 1.0.
2. Compute prediction probability:

   pθ(y=1|t)=sigmoid(2·1+0)=sigmoid(2)=1/(1+e^{-2})≈0.8808.
3. Compute negative log-likelihood for y=1:

   NLL = -log pθ(y=1|t) = -log(0.8808) ≈ 0.1269.
4. Compute KL(q||p) for 1D Gaussians:

   If q=N(μ,σ²), p=N(0,1), then

   D\_KL(q||p) = 0.5·(μ² + σ² - 1 - log σ²).

   Plug in μ=1.0, σ²=0.25:

   D\_KL = 0.5·(1.0 + 0.25 - 1 - log 0.25)

   = 0.5·(0.25 - (-1.3863))

   = 0.5·(1.6363)

   ≈ 0.8182.
5. Combine into VIB loss:

   L = NLL + β·KL ≈ 0.1269 + 0.1·0.8182

   ≈ 0.1269 + 0.0818

   ≈ 0.2087.

**Insight:** Even when prediction is confident (small NLL), the model pays a compression cost if qϕ(t|x) drifts away from the prior. Increasing β would push μ toward 0 and σ toward 1 (more compressed), potentially hurting accuracy if overdone.

### Effect of β: two limiting behaviors you can compute mentally

Consider the VIB objective L = E[-log pθ(y|t)] + β·KL(qϕ(t|x)||p(t)). Think about what happens as β→0 and β→∞, without doing full training.

1. Case 1: β→0.

   The loss becomes dominated by the prediction term:

   L ≈ E[-log pθ(y|t)].

   So the encoder is free to choose qϕ(t|x) to make prediction easiest, even if it memorizes x in t.

   In the extreme, qϕ(t|x) could become nearly deterministic with tiny σ and highly varying μ(x).
2. Case 2: β→∞.

   The KL term dominates:

   L ≈ β·KL(qϕ(t|x)||p(t)).

   The easiest way to minimize KL for all x is to set qϕ(t|x)=p(t) regardless of x.

   Then t becomes independent of x, implying I(X;T)≈0.

   But then y is hard to predict from t, so the NLL term increases.

**Insight:** β sets an information budget. β too small risks overfitting; β too large forces T to ignore X, collapsing predictive power. Practical work is largely about finding the right regime.

## Key Takeaways

- ✓

  Information Bottleneck learns a representation T of X that preserves information relevant to Y while discarding the rest.
- ✓

  The canonical trade-off is $min⁡p(t∣x)I(X;T)−βI(T;Y)\min\_{p(t|x)} I(X;T) - \beta I(T;Y)minp(t∣x)​I(X;T)−βI(T;Y)$ with β>0 controlling compression vs relevance.
- ✓

  The Markov chain T–X–Y encodes that T is computed from X (no label leakage).
- ✓

  In discrete IB, the optimal encoder has a Gibbs/exponential form using a KL divergence between p(y|x) and p(y|t).
- ✓

  The discrete IB equations are fixed-point updates for p(t|x), p(t), and p(y|t), interpretable as soft clustering by label-meaning.
- ✓

  Variational IB (VIB) replaces intractable mutual informations with tractable surrogates: prediction NLL + β·KL(q(t|x)||p(t)).
- ✓

  β governs representation capacity: too low can memorize; too high can cause posterior collapse and hurt accuracy.

## Common Mistakes

- ✗

  Confusing the roles of the two mutual informations: I(X;T) is the compression penalty, I(T;Y) is the relevance reward.
- ✗

  Dropping the Markov assumption T–X–Y implicitly (e.g., designing T using Y at test time), which breaks the intended meaning of the objective.
- ✗

  Assuming VIB’s KL(q(t|x)||p(t)) equals I(X;T) exactly; it is typically an upper bound depending on the chosen prior.
- ✗

  Interpreting β as a learning rate-like nuisance parameter; it is a meaningful trade-off that changes what information the representation retains.

## Practice

easy

Discrete IB intuition: Suppose two inputs x₁ and x₂ have identical label distributions p(y|x₁)=p(y|x₂). In the discrete IB fixed-point encoder update, what does this suggest about how x₁ and x₂ should be assigned to bottleneck states t? Explain using the KL term.

**Hint:** Look at D\_KL(p(y|x)||p(y|t)). What happens if the two p(y|x) are the same?

Show solution

If p(y|x₁)=p(y|x₂), then for any cluster t the KL divergences D\_KL(p(y|x₁)||p(y|t)) and D\_KL(p(y|x₂)||p(y|t)) are equal. Therefore the encoder update produces the same relative preferences over t for x₁ and x₂ (up to the same normalizer Z). This suggests x₁ and x₂ are information-theoretically indistinguishable with respect to Y and can be compressed together (assigned similarly in T) without loss of relevance.

medium

Compute a KL regularizer: Let q(t|x)=N(μ,σ²) with μ=0.2 and σ=2.0, and prior p(t)=N(0,1). Compute D\_KL(q||p).

**Hint:** Use D\_KL = 0.5·(μ² + σ² − 1 − log σ²).

Show solution

Here μ²=0.04 and σ²=4. So

D\_KL = 0.5·(0.04 + 4 − 1 − log 4)

= 0.5·(3.04 − 1.3863)

= 0.5·(1.6537)

≈ 0.8269.

hard

Reasoning about β: In VIB, you observe posterior collapse (the encoder outputs q(t|x)≈p(t) for all x and accuracy drops). Name two concrete adjustments you could try, and explain the direction each changes the trade-off.

**Hint:** Think: which term is overpowering the other? How can you reduce that pressure or increase the usefulness of T?

Show solution

Posterior collapse indicates the KL/compression pressure is too strong relative to the prediction benefit. Two adjustments: (1) Decrease β, directly reducing the weight on KL(q(t|x)||p(t)), allowing T to carry more information about X (and thus about Y). (2) Increase decoder strength or training signal so using T becomes beneficial (e.g., a more expressive pθ(y|t), better optimization, or annealing β from 0 upward), which increases the relative gain from encoding predictive information, counteracting the incentive to ignore X.

## Connections

Prereqs you’re using here:

- •[Mutual Information](/tech-tree/mutual-information/)
- •[KL Divergence](/tech-tree/kl-divergence/)

Natural next nodes to unlock/relate:

- •[Rate–Distortion Theory](/tech-tree/rate-distortion/)
- •[Variational Inference](/tech-tree/variational-inference/)
- •[β-VAE and Latent Variable Models](/tech-tree/beta-vae/)
- •[Representation Learning](/tech-tree/representation-learning/)
- •[Regularization and Generalization](/tech-tree/generalization-regularization/)

Quality: A (4.2/5)

[← back to tree](/tech-tree/)[browse all →](/tech-tree/inventory/)
