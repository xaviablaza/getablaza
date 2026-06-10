---
title: Variational Autoencoders
description: Generative models with latent variables. ELBO, reparameterization.
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
permalink: /tech-tree/vae/
---

[←Back to Tech Tree](/tech-tree/)

[inventory](/tech-tree/inventory/)[coverage](/tech-tree/coverage/)

# Variational Autoencoders

Machine LearningDifficulty: ★★★★★Depth: 11Unlocks: 1

Generative models with latent variables. ELBO, reparameterization.

## Interactive Visualization

⏮◀◀▶▶STEP0.25x1xZOOM

t=0s

## Core Concepts

- -Latent-variable generative model: data x is generated from latent z via a decoder p\_theta(x|z) with prior p(z) (joint p\_theta(x,z)=p\_theta(x|z)p(z))
- -Variational posterior (encoder) q\_phi(z|x): a tractable parametric approximation to the true posterior p\_theta(z|x)
- -Evidence Lower Bound (ELBO): the objective E\_{q\_phi(z|x)}[log p\_theta(x,z) - log q\_phi(z|x)] used to fit model and inference parameters
- -Reparameterization trick: express z = g\_phi(epsilon,x) with epsilon drawn from a fixed noise distribution so gradients w.r.t. phi can backpropagate through sampling

## Key Symbols & Notation

q\_phi(z|x) - the variational/encoder distribution (parameters phi)

## Essential Relationships

- -ELBO decomposition: log p\_theta(x) = ELBO + KL[q\_phi(z|x) || p\_theta(z|x)], equivalently ELBO = E\_{q\_phi}[log p\_theta(x|z)] - KL[q\_phi(z|x) || p(z)]

## Prerequisites (3)

[Bayesian Inference5 atoms](/tech-tree/bayesian-inference/)[Neural Networks6 atoms](/tech-tree/neural-networks/)[KL Divergence6 atoms](/tech-tree/kl-divergence/)

## Unlocks (1)

[Diffusion Modelslvl 5](/tech-tree/diffusion-models/)

Advanced Learning Details

### Graph Position

169

Depth Cost

1

Fan-Out (ROI)

1

Bottleneck Score

11

Chain Length

### Cognitive Load

6

Atomic Elements

37

Total Elements

L2

Percentile Level

L4

Atomic Level

### All Concepts (12)

- - Latent-variable generative model: a decoder p\_θ(x|z) with a prior p(z) and marginal likelihood p\_θ(x)=∫ p\_θ(x|z)p(z) dz (usually intractable)
- - Inference network / encoder q\_φ(z|x): a neural-network parameterized approximate posterior that maps x to a distribution over latent z
- - Evidence Lower Bound (ELBO): the objective used in VAEs that lower-bounds log p\_θ(x)
- - ELBO decomposition: ELBO as the sum of a reconstruction (expected log-likelihood) term and a KL regularizer
- - Amortized variational inference: learning a single parametric mapping q\_φ(z|x) shared across data points instead of per-datapoint variational parameters
- - Reparameterization trick: expressing stochastic sampling from q\_φ(z|x) as a deterministic, differentiable transform z = g\_φ(ε, x) of noise ε to enable backpropagation through samples
- - Stochastic gradient variational Bayes / SGVB estimator: using Monte Carlo samples (with reparameterization) to get low-variance unbiased gradient estimates of ELBO
- - Monte Carlo estimation of expectations in the ELBO (using a small number of samples per datapoint during training)
- - Gaussian encoder parameterization: common choice q\_φ(z|x)=N(μ\_φ(x), diag(σ^2\_φ(x))) with the encoder outputting μ and σ
- - Closed-form KL for common pairs (e.g., Gaussian q to standard normal prior) used to avoid sampling for the KL term
- - Trade-off perspective: ELBO optimization trades reconstruction accuracy against closeness of q\_φ to the prior (regularization of latent space)
- - Posterior collapse (degenerate solution): phenomenon where q\_φ(z|x) collapses to the prior p(z) and the decoder ignores z

### Teaching Strategy

Multi-session curriculum - substantial prior knowledge and complex material. Use mastery gates and deliberate practice.

Variational Autoencoders (VAEs) are the bridge between probabilistic latent-variable modeling (Bayes, priors, posteriors) and deep learning (powerful function approximation). They give you a principled way to learn both a generator and an inference procedure—by optimizing a single tractable objective: the ELBO.

TL;DR:

A VAE posits a latent variable **z** that generates data **x** via a decoder p\_θ(x|z) and a prior p(z). Because the true posterior p\_θ(z|x) is intractable, we approximate it with an encoder q\_φ(z|x). Training maximizes the ELBO: 𝔼\_{q\_φ(z|x)}[log p\_θ(x|z)] − KL(q\_φ(z|x) ‖ p(z)). The reparameterization trick (z = μ\_φ(x) + σ\_φ(x) ⊙ ε, ε ∼ 𝒩(0, I)) allows backpropagation through sampling.

## What Is a Variational Autoencoder?

## Why VAEs exist (motivation)

In many problems we want a model that can **generate** realistic data and also **explain** data in terms of hidden factors. Think:

- •Images explained by pose, lighting, identity
- •Audio explained by speaker, phoneme content
- •Text explained by topic, style

A standard (deterministic) autoencoder learns an encoder f(**x**) → **z** and decoder g(**z**) → **x̂**, but **it does not define a probability distribution** over data. You can reconstruct, but “sampling” **z** and decoding often produces arbitrary garbage because the latent space has no probabilistic structure.

A VAE fixes this by making the model explicitly probabilistic. It’s an instance of a **latent-variable generative model**:

- •Sample latent **z** from a prior p(**z**)
- •Sample data **x** from a likelihood/decoder p\_θ(**x**|**z**)

This defines a joint distribution:

p\_θ(**x**, **z**) = p\_θ(**x**|**z**) p(**z**)

If we can learn θ well, then we can generate new data by sampling **z** ∼ p(**z**) and then **x** ∼ p\_θ(**x**|**z**).

## The core obstacle: posterior inference

Given an observed **x**, the Bayesian posterior over latents is

p\_θ(**z**|**x**) = p\_θ(**x**|**z**) p(**z**) / p\_θ(**x**)

where the marginal likelihood (evidence) is

p\_θ(**x**) = ∫ p\_θ(**x**|**z**) p(**z**) d**z**

In deep models, that integral is typically intractable.

But to learn the model, we’d like to maximize log p\_θ(**x**) over θ for the dataset. And to do inference (encode **x**), we want p\_θ(**z**|**x**). Both are blocked by the same intractable evidence integral.

## The VAE idea in one sentence

Introduce a tractable approximation q\_φ(**z**|**x**) (the **variational posterior** / encoder) and optimize a **lower bound** on log p\_θ(**x**) that is differentiable and scalable.

## What makes it an “autoencoder”?

The VAE has two neural networks:

- •**Encoder** q\_φ(**z**|**x**): maps **x** to parameters of a distribution over **z**
- •**Decoder** p\_θ(**x**|**z**): maps **z** to parameters of a distribution over **x**

Unlike a deterministic autoencoder, the encoder outputs **a distribution** (often Gaussian) and the decoder defines a **likelihood** (often Gaussian for real-valued data, Bernoulli for binary pixels, categorical for discrete tokens, etc.).

## Typical choice of distributions

A common (and very useful) baseline is:

- •Prior: p(**z**) = 𝒩(**0**, **I**)
- •Encoder: q\_φ(**z**|**x**) = 𝒩(μ\_φ(**x**), diag(σ²\_φ(**x**)))
- •Decoder:
- •For real-valued **x**: p\_θ(**x**|**z**) = 𝒩(μ\_θ(**z**), σ² **I**) (often fixed σ)
- •For binary pixels: p\_θ(**x**|**z**) = Bernoulli(π\_θ(**z**))

This is not required, but it’s a common starting point because (1) sampling is easy, (2) KL terms often have closed form, and (3) reparameterization is straightforward.

## Mental model

Think of training a VAE as simultaneously:

1. 1)Learning a **generator** that can map simple noise **z** into data space.
2. 2)Learning an **inference network** that can map data **x** back to a distribution over plausible **z**.
3. 3)Ensuring these two agree via a variational objective.

## Core Mechanic 1: The ELBO (Evidence Lower Bound)

## Why we need a bound at all

The quantity we would like to maximize for each datapoint **x** is log p\_θ(**x**). But:

log p\_θ(**x**) = log ∫ p\_θ(**x**|**z**) p(**z**) d**z**

The log of an integral of a neural-network-defined density is generally not tractable.

Variational inference gives a workaround: introduce a distribution q\_φ(**z**|**x**) that we can sample from and evaluate.

## Deriving the ELBO (showing the work)

Start with the log evidence and multiply inside by q\_φ(**z**|**x**) / q\_φ(**z**|**x**):

log p\_θ(**x**)

= log ∫ p\_θ(**x**, **z**) d**z**

= log ∫ q\_φ(**z**|**x**) · [p\_θ(**x**, **z**) / q\_φ(**z**|**x**)] d**z**

Now apply Jensen’s inequality to log 𝔼[·] (log is concave):

log ∫ q\_φ(**z**|**x**) · [p\_θ(**x**, **z**) / q\_φ(**z**|**x**)] d**z**

= log 𝔼\_{q\_φ(**z**|**x**)} [ p\_θ(**x**, **z**) / q\_φ(**z**|**x**) ]

≥ 𝔼\_{q\_φ(**z**|**x**)} [ log p\_θ(**x**, **z**) − log q\_φ(**z**|**x**) ]

Define the ELBO:

ELBO(θ, φ; **x**) = 𝔼\_{q\_φ(**z**|**x**)} [ log p\_θ(**x**, **z**) − log q\_φ(**z**|**x**) ]

So we have the bound:

log p\_θ(**x**) ≥ ELBO(θ, φ; **x**)

## Unpacking the ELBO into “reconstruction − regularization”

Use p\_θ(**x**, **z**) = p\_θ(**x**|**z**) p(**z**):

ELBO

= 𝔼\_{q\_φ(**z**|**x**)}[ log p\_θ(**x**|**z**) + log p(**z**) − log q\_φ(**z**|**x**) ]

Group the last two terms as a KL divergence:

KL(q\_φ(**z**|**x**) ‖ p(**z**))

= 𝔼\_{q\_φ(**z**|**x**)}[ log q\_φ(**z**|**x**) − log p(**z**) ]

So:

ELBO

= 𝔼\_{q\_φ(**z**|**x**)}[ log p\_θ(**x**|**z**) ] − KL(q\_φ(**z**|**x**) ‖ p(**z**))

This is the form you implement.

### Term 1: expected log-likelihood (reconstruction)

𝔼\_{q\_φ(**z**|**x**)}[ log p\_θ(**x**|**z**) ]

- •Encourages **z** sampled from the encoder to decode into something that assigns high probability to the observed **x**.
- •With Gaussian likelihood and fixed variance, this becomes (up to constants) a negative squared error.
- •With Bernoulli likelihood, it becomes cross-entropy.

### Term 2: KL to the prior (regularization)

KL(q\_φ(**z**|**x**) ‖ p(**z**))

- •Encourages the encoded distribution to stay close to the prior.
- •This makes sampling from p(**z**) produce meaningful decodes.
- •Prevents the encoder from using arbitrarily “spiky” posteriors just to reconstruct perfectly.

## The tightness of the bound

A key identity connects ELBO and the true posterior:

log p\_θ(**x**) = ELBO(θ, φ; **x**) + KL(q\_φ(**z**|**x**) ‖ p\_θ(**z**|**x**))

Derivation sketch (showing the work):

KL(q ‖ p\_θ(**z**|**x**))

= 𝔼\_q[ log q(**z**|**x**) − log p\_θ(**z**|**x**) ]

= 𝔼\_q[ log q(**z**|**x**) − log (p\_θ(**x**, **z**) / p\_θ(**x**)) ]

= 𝔼\_q[ log q(**z**|**x**) − log p\_θ(**x**, **z**) + log p\_θ(**x**) ]

= log p\_θ(**x**) − 𝔼\_q[ log p\_θ(**x**, **z**) − log q(**z**|**x**) ]

= log p\_θ(**x**) − ELBO

Rearrange:

log p\_θ(**x**) = ELBO + KL(q ‖ p\_θ(**z**|**x**))

Because KL ≥ 0, ELBO is a lower bound. It becomes tight when q\_φ(**z**|**x**) matches the true posterior.

## Dataset objective

For a dataset {**x**ᵢ}ᵢ₌₁ᴺ, maximize:

∑ᵢ ELBO(θ, φ; **x**ᵢ)

This trains:

- •θ to make the decoder a good likelihood model
- •φ to make the encoder approximate the posterior under the current decoder

## A practical view: what gradients do we need?

We need gradients of

𝔼\_{q\_φ(**z**|**x**)}[ log p\_θ(**x**|**z**) ]

with respect to both θ and φ, plus gradients of the KL term.

- •Gradients w.r.t. θ are usually straightforward: sample **z** and backprop through the decoder.
- •Gradients w.r.t. φ are subtle because **z** is sampled from q\_φ, so the sampling operation depends on φ.

That’s exactly why the reparameterization trick matters.

## Core Mechanic 2: The Reparameterization Trick

## Why reparameterization is needed

Suppose we approximate the expectation with Monte Carlo:

𝔼\_{q\_φ(**z**|**x**)}[ f(**z**) ] ≈ (1/L) ∑\_{ℓ=1}^L f(**z**^{(ℓ)}), where **z**^{(ℓ)} ∼ q\_φ(**z**|**x**)

If **z**^{(ℓ)} is produced by a sampling step that depends on φ, naive backprop gets stuck: the computational graph has a stochastic node.

One option is the score-function (REINFORCE) estimator:

∇\_φ 𝔼\_{q\_φ}[f(**z**)] = 𝔼\_{q\_φ}[ f(**z**) ∇\_φ log q\_φ(**z**) ]

It’s unbiased but typically high-variance.

Reparameterization gives a lower-variance, pathwise gradient by rewriting the random variable as a deterministic function of φ and external noise.

## The key idea

If you can write

**z** = g\_φ(ε, **x**), ε ∼ p(ε)

where p(ε) does not depend on φ, then

𝔼\_{q\_φ(**z**|**x**)}[ f(**z**) ] = 𝔼\_{p(ε)}[ f(g\_φ(ε, **x**)) ]

Now the randomness is in ε, not in the parameters. Gradients can flow through g\_φ.

## Gaussian case (most common)

Let

q\_φ(**z**|**x**) = 𝒩(μ\_φ(**x**), diag(σ²\_φ(**x**)))

Sample ε ∼ 𝒩(**0**, **I**) and define:

**z** = μ\_φ(**x**) + σ\_φ(**x**) ⊙ ε

Here ⊙ is elementwise multiplication.

This produces **z** distributed exactly as q\_φ(**z**|**x**). And μ\_φ, σ\_φ are outputs of a neural net.

## Backprop through the expectation

Consider the reconstruction term for a single **x**:

ℒ\_rec(θ, φ; **x**) = 𝔼\_{q\_φ(**z**|**x**)}[ log p\_θ(**x**|**z**) ]

Using reparameterization:

ℒ\_rec = 𝔼\_{ε∼𝒩(0,I)}[ log p\_θ(**x**| μ\_φ(**x**) + σ\_φ(**x**) ⊙ ε ) ]

Approximate with L samples:

ℒ\_rec ≈ (1/L) ∑\_{ℓ=1}^L log p\_θ(**x**| μ\_φ(**x**) + σ\_φ(**x**) ⊙ ε^{(ℓ)})

Now ∇\_φ is just ordinary backprop through μ\_φ and σ\_φ.

## The KL term and closed form

With a standard normal prior p(**z**) = 𝒩(**0**, **I**) and diagonal Gaussian q\_φ, the KL has a closed form.

Let q = 𝒩(μ, diag(σ²)) and p = 𝒩(0, I). Then:

KL(q ‖ p) = (1/2) ∑ⱼ ( μⱼ² + σⱼ² − log σⱼ² − 1 )

This is extremely useful: it’s exact, differentiable, and cheap.

### Show the structure (intuition)

Each latent dimension j pays a penalty:

- •μⱼ²: pushes means toward 0
- •σⱼ²: pushes variances toward 1 (too large is penalized)
- •−log σⱼ²: penalizes tiny variances (too confident)

So the encoder is encouraged to produce a distribution “not too far” from 𝒩(0,1).

## Practical parameterization: log-variance

To keep σ positive, we usually output log σ² (call it **s**) and compute:

σ² = exp(**s**), σ = exp(0.5 **s**)

This avoids invalid (negative) variances and tends to be numerically stable.

## Summary table: what you compute in a basic VAE

| Piece | Object | Typical choice | Role |
| --- | --- | --- | --- |
| Prior | p(**z**) | 𝒩(**0**, **I**) | Defines “sampling space” |
| Encoder | q\_φ(**z** | **x**) | 𝒩(μ\_φ(**x**), diag(σ²\_φ(**x**))) | Approx posterior |
| Decoder | p\_θ(**x** | **z**) | Bernoulli or Gaussian | Likelihood model |
| Objective | ELBO | 𝔼\_q[log p\_θ(**x** | **z**)] − KL(q ‖ p) | Train θ, φ |
| Trick | **z** = μ + σ ⊙ ε | ε ∼ 𝒩(0,I) | Low-variance gradients |

## A note on discrete latents

Reparameterization is straightforward for continuous distributions like Gaussians. For discrete latents, you need alternatives (Gumbel-Softmax / Concrete distributions, score-function estimators, or other variational relaxations). Many VAE lessons stop at Gaussians because they cover the most common and useful case.

## Application/Connection: How VAEs Are Used (and What to Watch For)

## Generation

After training, generation is simple:

1. 1)Sample **z** ∼ p(**z**) = 𝒩(**0**, **I**)
2. 2)Sample **x** ∼ p\_θ(**x**|**z**) or take the decoder mean as a “typical” sample

Because the KL term kept q\_φ(**z**|**x**) near p(**z**), the decoder has been trained on **z** values that look like prior samples.

## Representation learning

The latent **z** can be used as a learned feature representation. Common uses:

- •Clustering in latent space
- •Interpolation: decode points along (1−t)**z**₁ + t**z**₂
- •Downstream supervised tasks using **z** as input

Caution: VAEs trade off reconstruction fidelity vs. latent regularity. If the KL term dominates, representations can become less informative.

## Conditional VAEs (cVAEs)

If you want generation conditioned on labels or attributes **y**:

- •Prior p(**z**|**y**)
- •Decoder p\_θ(**x**|**z**, **y**)
- •Encoder q\_φ(**z**|**x**, **y**)

This lets you generate samples with a chosen condition.

## Anomaly detection

A common heuristic: points with low ELBO (or high reconstruction error) are considered anomalous. This works best when the model class fits normal data well.

## The “posterior collapse” problem (important failure mode)

In powerful decoders (e.g., autoregressive text decoders), the model may learn to ignore **z** entirely:

- •q\_φ(**z**|**x**) ≈ p(**z**) (KL goes to 0)
- •Decoder models p\_θ(**x**) well without needing **z**

Then **z** carries little information about **x**.

### Common mitigations

| Technique | What it changes | Why it helps |
| --- | --- | --- |
| KL annealing | Slowly increase KL weight from 0 → 1 | Gives encoder time to learn informative latents |
| β-VAE | Use β · KL with β ≠ 1 | β < 1 encourages information; β > 1 encourages disentanglement |
| Free bits | KL term has a per-dim minimum | Prevents KL from collapsing too aggressively |
| Weaker decoder | Reduce decoder capacity | Forces use of **z** |

## β-VAE: a small change with big effects

Objective:

ELBO\_β = 𝔼\_q[log p\_θ(**x**|**z**)] − β KL(q ‖ p)

- •β > 1: stronger pressure to match the prior → often more “disentangled” latents but blurrier samples
- •β < 1: weaker pressure → better reconstructions but latent space may be less smooth for sampling

## Importance-weighted autoencoders (IWAE)

ELBO uses one sample (or few) and is a lower bound. IWAE tightens the bound using multiple samples:

log p\_θ(**x**) ≥ 𝔼\_{**z**₁:K ∼ q}[ log ( (1/K) ∑ₖ p\_θ(**x**, **z**ₖ) / q(**z**ₖ|**x**) ) ]

This can improve generative modeling but changes optimization dynamics.

## Connection to diffusion models (why this node unlocks them)

Diffusion models also involve:

- •Latent/noise variables (a sequence of noisy states)
- •Learning to reverse a corruption process
- •Using tractable training objectives that avoid directly optimizing log p(**x**) in closed form

Conceptually, VAEs train a generator with latent variables via a variational bound; diffusion trains a generator via denoising/score objectives. Understanding:

- •latent-variable modeling
- •KL terms and approximate inference
- •reparameterization and sampling-based gradients

makes diffusion objectives feel much less mysterious.

## Worked Examples (3)

### Derive the ELBO decomposition into reconstruction − KL

Given a latent-variable model p\_θ(**x**, **z**) = p\_θ(**x**|**z**) p(**z**) and an approximate posterior q\_φ(**z**|**x**), show that ELBO = 𝔼\_q[log p\_θ(**x**|**z**)] − KL(q\_φ(**z**|**x**) ‖ p(**z**)).

1. Start from the ELBO definition:

   ELBO = 𝔼\_{q\_φ(**z**|**x**)}[ log p\_θ(**x**, **z**) − log q\_φ(**z**|**x**) ].
2. Substitute the joint factorization:

   log p\_θ(**x**, **z**) = log p\_θ(**x**|**z**) + log p(**z**).
3. Plug in and separate expectations:

   ELBO = 𝔼\_q[ log p\_θ(**x**|**z**) + log p(**z**) − log q(**z**|**x**) ]

   = 𝔼\_q[ log p\_θ(**x**|**z**) ] + 𝔼\_q[ log p(**z**) − log q(**z**|**x**) ].
4. Recognize the KL divergence:

   KL(q(**z**|**x**) ‖ p(**z**)) = 𝔼\_q[ log q(**z**|**x**) − log p(**z**) ].

   Therefore:

   𝔼\_q[ log p(**z**) − log q(**z**|**x**) ] = − KL(q(**z**|**x**) ‖ p(**z**)).
5. Conclude:

   ELBO = 𝔼\_{q\_φ(**z**|**x**)}[ log p\_θ(**x**|**z**) ] − KL(q\_φ(**z**|**x**) ‖ p(**z**)).

**Insight:** The ELBO cleanly separates “fit the data” (expected log-likelihood) from “keep latents well-behaved for sampling” (KL to the prior). This is the central tradeoff in VAEs.

### Compute KL(q ‖ p) for diagonal Gaussians (standard VAE case)

Let q(**z**) = 𝒩(μ, diag(σ²)) and p(**z**) = 𝒩(0, I). Derive KL(q ‖ p) = (1/2) ∑ⱼ ( μⱼ² + σⱼ² − log σⱼ² − 1 ).

1. Write log densities (up to constants) for d dimensions.

   For p:

   log p(**z**) = −(1/2) ∑ⱼ ( zⱼ² + log 2π ).

   For q:

   log q(**z**) = −(1/2) ∑ⱼ ( (zⱼ−μⱼ)²/σⱼ² + log σⱼ² + log 2π ).
2. Start from KL definition:

   KL(q ‖ p) = 𝔼\_q[ log q(**z**) − log p(**z**) ].

   The log 2π constants cancel.
3. Compute the difference inside the expectation:

   log q − log p

   = −(1/2) ∑ⱼ [ (zⱼ−μⱼ)²/σⱼ² + log σⱼ² − zⱼ² ].
4. Take expectation under q. Use facts:

   If zⱼ ∼ 𝒩(μⱼ, σⱼ²), then

   𝔼[(zⱼ−μⱼ)²] = σⱼ²,

   𝔼[zⱼ²] = Var(zⱼ) + (𝔼[zⱼ])² = σⱼ² + μⱼ².
5. Substitute expectations:

   𝔼\_q[(zⱼ−μⱼ)²/σⱼ²] = σⱼ²/σⱼ² = 1,

   𝔼\_q[zⱼ²] = σⱼ² + μⱼ².
6. So for each j:

   𝔼\_q[ (zⱼ−μⱼ)²/σⱼ² + log σⱼ² − zⱼ² ]

   = 1 + log σⱼ² − (σⱼ² + μⱼ²).
7. Therefore:

   KL(q ‖ p)

   = −(1/2) ∑ⱼ [ 1 + log σⱼ² − σⱼ² − μⱼ² ]

   = (1/2) ∑ⱼ [ μⱼ² + σⱼ² − log σⱼ² − 1 ].

**Insight:** This closed-form KL is why the Gaussian VAE is so popular: you get exact regularization without needing Monte Carlo estimates, and gradients are stable.

### Reparameterization in practice: differentiating through a sample

Let q\_φ(**z**|**x**) = 𝒩(μ\_φ(**x**), diag(σ²\_φ(**x**))). Show how to rewrite an expectation 𝔼\_{q\_φ}[f(**z**)] so ∇\_φ can be computed by backprop.

1. Define external noise ε ∼ 𝒩(**0**, **I**), independent of φ.
2. Construct a deterministic transform:

   **z** = g\_φ(ε, **x**) = μ\_φ(**x**) + σ\_φ(**x**) ⊙ ε.
3. Rewrite the expectation:

   𝔼\_{q\_φ(**z**|**x**)}[ f(**z**) ] = 𝔼\_{ε∼𝒩(0,I)}[ f( μ\_φ(**x**) + σ\_φ(**x**) ⊙ ε ) ].
4. Approximate with a Monte Carlo sample ε¹:

   𝔼 ≈ f( μ\_φ(**x**) + σ\_φ(**x**) ⊙ ε¹ ).
5. Differentiate:

   ∇\_φ f( μ\_φ(**x**) + σ\_φ(**x**) ⊙ ε¹ )

   flows through μ\_φ and σ\_φ via the chain rule because ε¹ is treated as a constant during backprop.

**Insight:** Reparameterization moves the randomness to an input node (ε). Once you do that, the sampled **z** is just another differentiable layer in the network.

## Key Takeaways

- ✓

  A VAE is a probabilistic latent-variable model: p\_θ(**x**, **z**) = p\_θ(**x**|**z**) p(**z**), enabling true sampling/generation.
- ✓

  Because p\_θ(**z**|**x**) is usually intractable, we introduce an encoder q\_φ(**z**|**x**) to approximate the posterior.
- ✓

  The ELBO is the tractable training objective: ELBO = 𝔼\_{q\_φ}[log p\_θ(**x**|**z**)] − KL(q\_φ(**z**|**x**) ‖ p(**z**)).
- ✓

  ELBO is a lower bound on log p\_θ(**x**) and becomes tight when q\_φ(**z**|**x**) = p\_θ(**z**|**x**).
- ✓

  The reparameterization trick (Gaussian case: **z** = μ + σ ⊙ ε, ε ∼ 𝒩(0,I)) enables low-variance gradients through sampling.
- ✓

  With Gaussian prior and diagonal Gaussian encoder, KL has a closed form: (1/2)∑ⱼ(μⱼ² + σⱼ² − log σⱼ² − 1).
- ✓

  VAEs can fail via posterior collapse (KL→0, latents ignored), especially with very strong decoders; KL annealing, β-VAE, and capacity control help.
- ✓

  Understanding latent-variable objectives, KL structure, and reparameterization provides conceptual groundwork for later generative models, including diffusion.

## Common Mistakes

- ✗

  Treating the VAE decoder output as a deterministic reconstruction **x̂** without defining a likelihood p\_θ(**x**|**z**); you need a distribution to make the ELBO meaningful.
- ✗

  Forgetting that the reconstruction term is an expectation over **z** ∼ q\_φ(**z**|**x**); using only μ\_φ(**x**) can work as a heuristic but changes the objective.
- ✗

  Implementing σ directly (which can go negative) instead of parameterizing log σ² and exponentiating; this often causes numerical instability.
- ✗

  Assuming the KL term is just a generic regularizer; it specifically matches q\_φ(**z**|**x**) to the chosen prior p(**z**), which determines sampling behavior.

## Practice

medium

Show that log p\_θ(**x**) = ELBO(θ, φ; **x**) + KL(q\_φ(**z**|**x**) ‖ p\_θ(**z**|**x**)).

**Hint:** Start from KL(q ‖ p\_θ(**z**|**x**)) and substitute p\_θ(**z**|**x**) = p\_θ(**x**, **z**) / p\_θ(**x**). Rearrange to isolate log p\_θ(**x**).

Show solution

Let q = q\_φ(**z**|**x**).

KL(q ‖ p\_θ(**z**|**x**))

= 𝔼\_q[ log q(**z**|**x**) − log p\_θ(**z**|**x**) ]

= 𝔼\_q[ log q(**z**|**x**) − log (p\_θ(**x**, **z**) / p\_θ(**x**)) ]

= 𝔼\_q[ log q(**z**|**x**) − log p\_θ(**x**, **z**) + log p\_θ(**x**) ]

= log p\_θ(**x**) − 𝔼\_q[ log p\_θ(**x**, **z**) − log q(**z**|**x**) ]

= log p\_θ(**x**) − ELBO.

Therefore log p\_θ(**x**) = ELBO + KL(q\_φ(**z**|**x**) ‖ p\_θ(**z**|**x**)).

easy

Assume p(**z**) = 𝒩(0, I) and q\_φ(**z**|**x**) = 𝒩(μ, diag(σ²)) for a single datapoint. If μ = (2, 0) and σ² = (0.25, 4), compute KL(q ‖ p).

**Hint:** Use KL = (1/2)∑ⱼ(μⱼ² + σⱼ² − log σⱼ² − 1). Be careful: the formula uses σⱼ², not σⱼ.

Show solution

Compute per dimension.

j=1: μ₁² = 4, σ₁² = 0.25, log σ₁² = log 0.25 = −1.386294...

Term₁ = 4 + 0.25 − (−1.386294) − 1 = 4.636294...

j=2: μ₂² = 0, σ₂² = 4, log σ₂² = log 4 = 1.386294...

Term₂ = 0 + 4 − 1.386294 − 1 = 1.613706...

Sum = 6.25

KL = (1/2) · 6.25 = 3.125.

hard

A VAE uses Gaussian likelihood p\_θ(**x**|**z**) = 𝒩(μ\_θ(**z**), σ\_x² I) with fixed σ\_x². Show that maximizing 𝔼\_q[log p\_θ(**x**|**z**)] is equivalent (up to a constant) to minimizing 𝔼\_q[‖**x** − μ\_θ(**z**)‖²].

**Hint:** Write out the log density of a Gaussian with fixed variance and drop terms that do not depend on θ.

Show solution

For d-dimensional **x**,

log p\_θ(**x**|**z**) = −(d/2) log(2πσ\_x²) − (1/(2σ\_x²)) ‖**x** − μ\_θ(**z**)‖².

Take expectation over q\_φ(**z**|**x**):

𝔼\_q[log p\_θ(**x**|**z**)]

= −(d/2) log(2πσ\_x²) − (1/(2σ\_x²)) 𝔼\_q[ ‖**x** − μ\_θ(**z**)‖² ].

The first term is constant w.r.t. θ. Therefore maximizing 𝔼\_q[log p\_θ(**x**|**z**)] is equivalent to minimizing 𝔼\_q[ ‖**x** − μ\_θ(**z**)‖² ]. (The scaling 1/(2σ\_x²) does not change the optimizer when σ\_x² is fixed.)

## Connections

- •Next: [Diffusion Models](/tech-tree/diffusion-models/)
- •Related foundations: [Bayesian Inference](/tech-tree/bayesian-inference/), [KL Divergence](/tech-tree/kl-divergence/), [Neural Networks](/tech-tree/neural-networks/)
- •Nearby generative modeling ideas: [Normalizing Flows](/tech-tree/normalizing-flows/), [GANs](/tech-tree/gans/)

Quality: A (4.4/5)

[← back to tree](/tech-tree/)[browse all →](/tech-tree/inventory/)
