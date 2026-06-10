---
title: Diffusion Models
description: Denoising for generation. Score matching, noise schedules.
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
permalink: /tech-tree/diffusion-models/
---

[←Back to Tech Tree](/tech-tree/)

[inventory](/tech-tree/inventory/)[coverage](/tech-tree/coverage/)

# Diffusion Models

Machine LearningDifficulty: ★★★★★Depth: 12Unlocks: 0

Denoising for generation. Score matching, noise schedules.

## Interactive Visualization

⏮◀◀▶▶STEP0.25x1xZOOM

t=0s

## Core Concepts

- -Forward Gaussian noising (time-indexed Markov chain that corrupts data by adding Gaussian noise according to a noise schedule)
- -Learned denoiser/score (a parameterized model that maps a noisy sample at time t to either the added noise or the score = gradient log density)
- -Reverse generative process (iterative denoising / reverse SDE that uses the learned model to transform noise into data)

## Key Symbols & Notation

epsilon\_theta(x\_t,t) - the parameterized model that predicts the added noise (or equivalently represents the score)

## Essential Relationships

- -The forward noise schedule defines the conditional corruption used for training; minimizing a denoising/score-matching loss makes epsilon\_theta approximate the true noise/score, which is then used in the reverse iterative process to generate samples from the learned data distribution.

## Prerequisites (2)

[Variational Autoencoders6 atoms](/tech-tree/vae/)[Stochastic Gradient Descent5 atoms](/tech-tree/sgd/)

Advanced Learning Details

### Graph Position

179

Depth Cost

0

Fan-Out (ROI)

0

Bottleneck Score

12

Chain Length

### Cognitive Load

5

Atomic Elements

61

Total Elements

L4

Percentile Level

L3

Atomic Level

### All Concepts (23)

- - forward diffusion process: discrete-time Markov chain q(x\_t | x\_{t-1}) that progressively adds Gaussian noise to data
- - closed-form marginal q(x\_t | x\_0) expressing x\_t as a linear combination of x\_0 and Gaussian noise
- - noise schedule: sequence beta\_t (and derived alpha\_t, alpha\_bar\_t) that controls per-step noise magnitude
- - variance-preserving (VP) vs variance-exploding (VE) noise schedules and their qualitative differences
- - reverse (denoising) process p\_theta(x\_{t-1} | x\_t): a learned (usually Gaussian) Markov chain that reverses the forward noising
- - score function: s(x,t) = ∇\_x log p\_t(x), the gradient of the log density at noise level t
- - score-based generative modelling: learning s(x,t) to sample by following gradients of log-density (Langevin or reverse SDE)
- - denoising score matching (DSM): training objective that matches the network output to the score of noisy marginals
- - simplified/noise-prediction loss: training the network to predict injected noise epsilon (MSE) as a practical surrogate for score matching
- - parameterization choices for the model output: predict noise (epsilon\_theta), predict x0 (x0\_theta), or predict score (s\_theta), and how these change training and sampling
- - ELBO decomposition for diffusion models: expressing the marginal likelihood bound as a sum of stepwise KLs and a terminal KL
- - reparameterization sampling formula for q(x\_t | x\_0): x\_t = sqrt(alpha\_bar\_t) x\_0 + sqrt(1 - alpha\_bar\_t) epsilon enabling direct sampling of intermediate noised states
- - continuous-time formulation: forward SDE (dx = f(x,t) dt + g(t) dw) and its reverse-time SDE
- - reverse SDE relation: reverse drift = forward drift minus g(t)^2 times the score (f\_rev = f - g^2 ∇\_x log p\_t(x))
- - probability-flow ODE: deterministic ODE with drift f - 0.5 g^2 ∇ log p that yields the same marginal densities as the SDE
- - numerical sampling methods: ancestral (DDPM) sampling, discretized reverse SDE solvers (Euler-Maruyama), and DDIM deterministic/non-Markovian samplers
- - closed-form posterior q(x\_{t-1} | x\_t, x\_0) for Gaussian forward process used in ELBO/derivations
- - per-timestep loss weighting (lambda\_t) and the role of signal-to-noise ratio (SNR) in choosing weights
- - relationship between score estimation and denoising autoencoder formulation (denoising target as score proxy)
- - impact of noise schedule on training dynamics, sample quality, and required number of sampling steps
- - variance parameterization and how predicted mean/variance choices affect sample variance and likelihood evaluation
- - likelihood evaluation for diffusion models via tractable KL terms (ELBO) and its limitations
- - trade-offs between discrete-time DDPMs and continuous-time score-based models (flexibility, samplers, complexity)

### Teaching Strategy

Quick unlock - significant prerequisite investment but simple final step. Verify prerequisites first.

Diffusion models turn the generative modeling problem into something deceptively simple: learn to undo noise. If you can reliably denoise a sample that has been corrupted in a controlled way, you can start from pure noise and iteratively “walk back” to realistic data.

TL;DR:

A diffusion model defines (1) a forward Markov chain that gradually adds Gaussian noise to data using a schedule {βₜ}, and (2) a learned network ε\_θ(**x**ₜ, t) that predicts the added noise (or equivalently the score ∇\_x log p(**x**ₜ)). Generation runs the reverse process: start from **x**\_T ∼ 𝒩(0, I) and repeatedly denoise to sample **x**₀.

## What Is a Diffusion Model?

Diffusion models are generative models built around one central trick: instead of trying to model a complex data distribution p\_data(**x**₀) directly, we define a *destruction process* that is easy to analyze (adding Gaussian noise over many small steps), then learn a *construction process* that reverses it.

Why this helps:

- •Real images, audio, molecules, etc. have complicated, multi-modal distributions.
- •Gaussian noise is extremely well-behaved mathematically.
- •If we corrupt data gradually, each step becomes a small perturbation, and learning to reverse small perturbations is often easier than learning one huge jump.

A diffusion model typically has two coupled processes indexed by discrete time t ∈ {1, …, T} (T can be 1000 in classical DDPMs; modern samplers often use fewer steps with improved solvers):

1) **Forward (noising) process** q:

- •Start with data **x**₀ ∼ p\_data.
- •Add a little Gaussian noise each step to get **x**₁, **x**₂, …, **x**\_T.
- •After enough steps, **x**\_T is approximately standard normal: **x**\_T ≈ 𝒩(0, I).

2) **Reverse (denoising) process** p\_θ:

- •Start from **x**\_T ∼ 𝒩(0, I).
- •Apply a learned denoiser to iteratively produce **x**\_{T−1}, …, **x**₀.
- •The final **x**₀ is a generated sample.

The key learned object is a neural network that depends on the current noisy sample and the time index:

- •ε\_θ(**x**ₜ, t): predicts the noise that was added to obtain **x**ₜ.

From ε\_θ you can derive other equivalent parameterizations:

- •**x**₀-prediction: predict the clean sample directly.
- •v-prediction: a particular linear combination used for stability.
- •Score prediction: s\_θ(**x**ₜ, t) ≈ ∇\_{**x**ₜ} log q(**x**ₜ), i.e., the *score*.

Even if you only remember one sentence: diffusion models work because “denoise step-by-step” is a tractable supervised learning task.

Connection to ideas you already know (VAEs):

- •VAEs define an encoder q\_ϕ(**z**|**x**) and decoder p\_θ(**x**|**z**) and optimize an ELBO.
- •Diffusion models also define a latent-variable-like chain (**x**₁, …, **x**\_T) and can be derived from a variational bound.
- •But in practice, diffusion training often reduces to a simple regression loss (predict noise) rather than explicitly optimizing a tight ELBO.

Throughout this lesson we’ll use bold for vectors (e.g., **x**, **ε**), and assume images are flattened into vectors in ℝ^d (but all formulas hold per-pixel / per-dimension).

## Core Mechanic 1: Forward Gaussian Noising (the diffusion / corruption process)

The forward process is a time-indexed Markov chain that gradually destroys information by adding Gaussian noise according to a *noise schedule*.

## Why define a forward process at all?

Because it gives you a controlled way to generate paired training data:

- •pick a real data point **x**₀
- •sample a time t
- •corrupt it to get **x**ₜ
- •train a network to predict what corruption happened

This turns generative modeling into supervised learning.

## The step-wise noising rule

A common discrete-time forward process (DDPM) is:

q(**x**ₜ | **x**\_{t−1}) = 𝒩( **x**ₜ ; √(αₜ) **x**\_{t−1}, βₜ I )

where:

- •βₜ ∈ (0, 1) is the variance added at step t
- •αₜ = 1 − βₜ

Intuition:

- •multiply by √(αₜ) slightly shrinks the previous state
- •add fresh Gaussian noise with variance βₜ

Over many steps, the signal decays and noise dominates.

## Collapsing many steps into one: q(**x**ₜ | **x**₀)

A crucial simplification is that the composition of Gaussians stays Gaussian, so we can sample **x**ₜ directly from **x**₀ without simulating every intermediate step.

Define the cumulative product:

ᾱₜ = ∏\_{s=1}^t α\_s

Then:

q(**x**ₜ | **x**₀) = 𝒩( **x**ₜ ; √(ᾱₜ) **x**₀, (1 − ᾱₜ) I )

Equivalently, we can reparameterize:

**x**ₜ = √(ᾱₜ) **x**₀ + √(1 − ᾱₜ) **ε**, where **ε** ∼ 𝒩(0, I)

This single equation is the workhorse of diffusion training.

Pause and interpret each term:

- •√(ᾱₜ) controls how much of the original data remains.
- •√(1 − ᾱₜ) controls how much noise is mixed in.
- •For small t: ᾱₜ ≈ 1 ⇒ **x**ₜ ≈ **x**₀.
- •For large t: ᾱₜ ≈ 0 ⇒ **x**ₜ ≈ **ε** (pure noise).

## Noise schedules: choosing βₜ (or ᾱₜ)

The schedule determines *how quickly* you destroy information.

Design goals:

- •Early steps should not destroy too much, or the denoiser can’t learn delicate structure.
- •Late steps should approach near-Gaussian so the “starting distribution” for generation is simple.
- •Training should cover a range of SNRs (signal-to-noise ratios) that is learnable.

Common schedules:

| Schedule | How it behaves | Pros | Cons |
| --- | --- | --- | --- |
| Linear βₜ | βₜ increases linearly | Simple, classic DDPM | Not optimal SNR allocation |
| Cosine ᾱₜ | ᾱₜ follows a cosine curve | Good empirical performance, smooth | Needs careful discretization |
| Learned / piecewise | optimized for sampling steps | can be very fast at inference | adds complexity |

A useful quantity is the SNR at time t:

SNRₜ = ᾱₜ / (1 − ᾱₜ)

- •High SNR (early): mostly signal.
- •Low SNR (late): mostly noise.

Practical consequence: the network must learn to denoise across wildly different regimes. This is why the time embedding (conditioning on t) is essential.

## Time conditioning

The network ε\_θ(**x**ₜ, t) is conditioned on time t (or a continuous time value). In practice:

- •encode t with sinusoidal features
- •pass through an MLP
- •inject into residual blocks (e.g., via FiLM / adaptive normalization)

This enables one shared network to act like a family of denoisers, one for each noise level.

At this point you have a forward process q that is:

- •tractable
- •easy to sample from
- •analytically solvable for q(**x**ₜ|**x**₀)

Next we learn the reverse.

## Core Mechanic 2: Learned Denoiser / Score (ε\_θ and its meanings)

The learned model sits at the center of diffusion: ε\_θ(**x**ₜ, t). Superficially it’s “just” a network that predicts noise, but understanding what it *represents* explains why diffusion models work and how score matching appears.

## Why predict noise?

When we write

**x**ₜ = √(ᾱₜ) **x**₀ + √(1 − ᾱₜ) **ε**

the only randomness (given **x**₀ and t) is **ε** ∼ 𝒩(0, I). If a network can infer the likely **ε** from **x**ₜ, it can recover information about **x**₀.

Noise prediction is attractive because:

- •The target **ε** is known exactly during training (we sampled it).
- •The loss is a simple MSE.
- •The objective aligns with maximizing a variational lower bound under certain parameterizations.

## The standard training objective

Sample:

- •**x**₀ from dataset
- •t uniformly from {1, …, T} (or from a weighted distribution)
- •**ε** ∼ 𝒩(0, I)
- •form **x**ₜ = √(ᾱₜ) **x**₀ + √(1 − ᾱₜ) **ε**

Then minimize:

L(θ) = 𝔼\_{**x**₀,t,**ε**} [ ‖ **ε** − ε\_θ(**x**ₜ, t) ‖² ]

This is the “simple loss” from DDPM.

### Breathing room: what does minimizing this actually do?

At a fixed t, **x**ₜ is a noisy version of real data. There are many possible clean **x**₀ that could have produced a given **x**ₜ, but the network learns the *conditional expectation* of noise given **x**ₜ and t.

For MSE regression,

ε\_θ\*(**x**ₜ,t) = 𝔼[ **ε** | **x**ₜ, t ]

That conditional expectation encodes the structure of the data distribution because the posterior over **x**₀ given **x**ₜ is shaped by p\_data.

## From noise prediction to **x**₀ prediction

Rearrange the reparameterization:

**x**ₜ = √(ᾱₜ) **x**₀ + √(1 − ᾱₜ) **ε**

Solve for **x**₀:

**x**₀ = ( **x**ₜ − √(1 − ᾱₜ) **ε** ) / √(ᾱₜ)

So given ε\_θ, we can define an implicit estimate of the clean sample:

\hat{**x**}₀(**x**ₜ,t) = ( **x**ₜ − √(1 − ᾱₜ) ε\_θ(**x**ₜ,t) ) / √(ᾱₜ)

This is used during sampling and for guidance methods.

## From noise prediction to the score (score matching connection)

The *score* of a density p(**x**) is:

∇\_{**x**} log p(**x**)

Diffusion theory says the optimal denoiser corresponds to the score of the noisy distribution at each noise level.

For the forward process q, one can show a relationship of the form:

s\_θ(**x**ₜ,t) ≈ ∇\_{**x**ₜ} log q(**x**ₜ)

and with noise prediction parameterization:

s\_θ(**x**ₜ,t) = − ε\_θ(**x**ₜ,t) / √(1 − ᾱₜ)

Up to conventions and scaling, predicting noise is equivalent to predicting the score.

### Why the score matters

If you know the score field ∇ log p(**x**), you know in which direction probability increases most steeply. Sampling methods (reverse SDE / Langevin-like dynamics) can use the score to push noise toward data manifold regions.

This gives diffusion a deep conceptual link: it’s not merely denoising; it’s learning a time-indexed family of score functions.

## Weighting across timesteps

Uniformly sampling t often works, but it can overweight uninformative very-noisy steps or underweight crucial mid-SNR steps.

Many systems use weighted losses:

L(θ) = 𝔼[ w(t) ‖ **ε** − ε\_θ(**x**ₜ,t) ‖² ]

Common ideas:

- •choose w(t) to balance SNR
- •emphasize mid-range noise where perceptual structure is learned
- •adopt v-prediction to stabilize scaling across t

At this stage we have a trained ε\_θ. Next we need to turn it into a generative procedure.

## Core Mechanic 3: Reverse Generative Process (from noise to data)

Generation is the reverse of the forward noising chain. The forward chain is easy because it’s Gaussian by construction; the reverse chain is hard because it depends on the unknown data distribution. The learned model ε\_θ supplies the missing information.

## Reverse-time Markov chain (DDPM view)

We want transitions p\_θ(**x**\_{t−1} | **x**ₜ) that approximately invert q(**x**ₜ | **x**\_{t−1}). DDPMs choose Gaussian reverse transitions:

p\_θ(**x**\_{t−1} | **x**ₜ) = 𝒩( **x**\_{t−1} ; μ\_θ(**x**ₜ,t), Σ\_θ(t) )

A standard choice fixes Σ\_θ(t) to a known variance (e.g., β̃ₜ I), and uses the network to compute the mean.

A common form (using noise prediction) is:

μ\_θ(**x**ₜ,t) = 1/√(αₜ) \left( **x**ₜ − \frac{βₜ}{√(1 − ᾱₜ)} ε\_θ(**x**ₜ,t) \right)

Then sampling is:

**x**\_{t−1} = μ\_θ(**x**ₜ,t) + σₜ **z**, **z** ∼ 𝒩(0, I)

with σₜ chosen from the variance schedule.

Pause: what is happening qualitatively?

- •ε\_θ predicts what noise component is present in **x**ₜ.
- •subtracting that component increases the “signal” portion.
- •you still add some noise (σₜ **z**) except possibly at the final step.

This stochasticity helps match the true reverse distribution and avoids collapsing to a single mode.

## Deterministic sampling (DDIM intuition)

If you set the injected noise to zero (or modify the update), you get deterministic trajectories that still land on realistic samples. This is the basis for faster sampling variants.

You can think of DDPM vs DDIM as trading:

- •stochasticity and exactness of the original discrete diffusion model
- •for fewer steps and faster inference

## Continuous-time perspective (SDE view)

In the score-based modeling framework, the diffusion process is described by an SDE:

d**x** = f(**x**, t) dt + g(t) d**w**

where **w** is Brownian motion.

The reverse-time SDE has drift that involves the score:

d**x** = [ f(**x**, t) − g(t)² ∇\_{**x**} log p\_t(**x**) ] dt + g(t) d\bar{**w**}

If you approximate the score with s\_θ(**x**, t), you can numerically solve the reverse SDE to sample.

You do not need to memorize this SDE form to use diffusion models, but it explains:

- •why score estimation is fundamental
- •why different samplers (Euler–Maruyama, Heun, higher-order solvers) exist
- •how “number of steps” corresponds to ODE/SDE solver accuracy

## Starting point and endpoint

- •Start: **x**\_T ∼ 𝒩(0, I)
- •End: **x**₀ should resemble p\_data

If T is large enough and the schedule is designed properly, q(**x**\_T) is close to a standard normal regardless of p\_data (information destroyed). That’s why the model can start from pure noise.

## Classifier-free guidance (briefly, since it’s common)

In conditional generation (text-to-image, class-conditional), you train ε\_θ(**x**ₜ,t, c) with conditioning c, and also sometimes drop c during training to learn an unconditional path.

At sampling time, combine:

ε\_guided = (1 + w) ε\_θ(**x**ₜ,t,c) − w ε\_θ(**x**ₜ,t, ∅)

where w ≥ 0 is guidance scale.

Intuition: push samples toward regions that satisfy the condition more strongly, at the cost of reduced diversity if w is too high.

This is not strictly part of “diffusion basics,” but it’s a major reason diffusion works well in practice.

## Application/Connection: How Diffusion Models Fit into the Generative Modeling Toolkit

Diffusion models became dominant for high-fidelity generation because they combine stable training with flexible conditioning and strong likelihood-related foundations.

## Comparing diffusion to VAEs and GANs

| Model family | Core idea | Strengths | Weaknesses |
| --- | --- | --- | --- |
| VAE | latent variable model trained with ELBO | stable training, explicit encoder | samples can be blurry; trade-off via KL |
| GAN | adversarial game | sharp samples, fast inference | unstable training, mode collapse, hard likelihood |
| Diffusion | learn to reverse noising | very high quality, stable objective, flexible conditioning | slow sampling (mitigated by fast samplers), compute-heavy |

Since you know VAEs: notice the philosophical similarity:

- •VAE: learn p\_θ(**x**|**z**) with a simple prior p(**z**) = 𝒩(0, I)
- •Diffusion: learn p\_θ(**x**\_{t−1}|**x**ₜ) with a simple prior p(**x**\_T) = 𝒩(0, I)

In both cases, “start from something Gaussian” is the trick. Diffusion differs in that the latent is not low-dimensional; it’s the same dimension as **x**.

## Where score matching shows up operationally

Even if you never explicitly compute ∇ log p, the score view guides:

- •sampler design (SDE/ODE solvers)
- •improved objectives (weighted score matching)
- •understanding guidance (conditioning changes the score landscape)

## Practical considerations in real systems

1) Architecture

- •U-Net backbones (images)
- •attention layers to capture global structure
- •time embeddings injected across layers

2) Data scaling and variance

- •pixel scaling to [−1, 1]
- •predicting ε vs v affects stability

3) Speed

- •fewer-step samplers (DDIM, DPM-Solver, EDM-style solvers)
- •distillation (train a student model to sample in fewer steps)

4) Evaluation

- •FID, precision/recall for generative models
- •human preference for conditional generation

## Mental model to keep

Diffusion models are *iterative refinement*. Each step is a small denoise move that, when composed many times, produces a complex global transformation from noise to data.

If you want one unifying picture:

- •forward: **x**₀ → **x**ₜ is easy because we defined it
- •reverse: **x**ₜ → **x**₀ is hard because it requires knowing where the data lives
- •ε\_θ learns that knowledge from data via a supervised denoising task

## Worked Examples (3)

### Compute q(\*\*x\*\*ₜ|\*\*x\*\*₀) and sample \*\*x\*\*ₜ in one step

Let a 1D “data point” be x₀ = 2. Suppose a diffusion schedule gives ᾱₜ = 0.81 at some timestep t. Sample ε ∼ 𝒩(0,1); take ε = −0.5 for this worked example. Compute xₜ.

1. Use the closed form:

   xₜ = √(ᾱₜ) x₀ + √(1 − ᾱₜ) ε
2. Compute √(ᾱₜ):

   √(0.81) = 0.9
3. Compute √(1 − ᾱₜ):

   1 − ᾱₜ = 1 − 0.81 = 0.19

   √(0.19) ≈ 0.43589
4. Plug in values:

   xₜ = 0.9 · 2 + 0.43589 · (−0.5)

   = 1.8 − 0.217945

   = 1.582055
5. Interpretation:

   - •The clean signal contribution is 1.8.
   - •The noise contribution is about −0.218.
   - •At ᾱₜ = 0.81, the sample is still mostly signal (high SNR).

**Insight:** The ability to sample **x**ₜ directly from **x**₀ (without simulating t steps) is what makes diffusion training efficient: you can train on arbitrary noise levels with one formula.

### Recover \hat{\*\*x\*\*}₀ from ε\_θ(\*\*x\*\*ₜ,t) (noise-prediction parameterization)

Assume ᾱₜ = 0.36 and you observe a 2D noisy sample **x**ₜ = (1.2, −0.3). A trained network predicts ε\_θ(**x**ₜ,t) = (0.5, −1.0). Compute \hat{**x**}₀.

1. Use the reconstruction formula:

   \hat{**x**}₀ = ( **x**ₜ − √(1 − ᾱₜ) ε\_θ(**x**ₜ,t) ) / √(ᾱₜ)
2. Compute √(ᾱₜ):

   √(0.36) = 0.6
3. Compute √(1 − ᾱₜ):

   1 − ᾱₜ = 0.64

   √(0.64) = 0.8
4. Compute the noise term:

   √(1 − ᾱₜ) ε\_θ = 0.8 · (0.5, −1.0)

   = (0.4, −0.8)
5. Subtract from **x**ₜ:

   **x**ₜ − √(1 − ᾱₜ) ε\_θ = (1.2, −0.3) − (0.4, −0.8)

   = (0.8, 0.5)
6. Divide by √(ᾱₜ):

   \hat{**x**}₀ = (0.8, 0.5) / 0.6

   = (1.333…, 0.833…)

**Insight:** Noise prediction is not just a training trick: it provides a direct map from a noisy point back to an estimate of the clean data, which then defines the reverse-process mean updates.

### One reverse DDPM-style update (conceptual numeric step)

Consider 1D for simplicity. Suppose at timestep t you have xₜ = 0.7, αₜ = 0.9 (so βₜ = 0.1), ᾱₜ = 0.5, and the model predicts ε\_θ(xₜ,t) = 0.2. Compute the reverse mean μ\_θ(xₜ,t).

1. Use the standard mean (noise-prediction form):

   μ\_θ(xₜ,t) = 1/√(αₜ) · ( xₜ − (βₜ/√(1 − ᾱₜ)) ε\_θ(xₜ,t) )
2. Compute √(αₜ):

   √(0.9) ≈ 0.948683

   So 1/√(αₜ) ≈ 1.054093
3. Compute √(1 − ᾱₜ):

   1 − ᾱₜ = 0.5

   √(0.5) ≈ 0.707107
4. Compute the scaled noise subtraction:

   (βₜ/√(1 − ᾱₜ)) ε\_θ = (0.1 / 0.707107) · 0.2

   ≈ 0.141421 · 0.2

   ≈ 0.028284
5. Compute inside parentheses:

   xₜ − (...) = 0.7 − 0.028284 = 0.671716
6. Multiply by 1/√(αₜ):

   μ\_θ ≈ 1.054093 · 0.671716 ≈ 0.7081
7. Interpretation:

   - •The reverse mean is slightly different from xₜ.
   - •Over many steps, these small corrections accumulate into a large denoising trajectory.

**Insight:** Reverse diffusion is many small, structured moves. Each move uses ε\_θ to decide how to shift the sample toward higher-probability regions at that noise level.

## Key Takeaways

- ✓

  A diffusion model defines a *forward* Gaussian noising Markov chain q and learns a *reverse* denoising chain p\_θ.
- ✓

  The closed form **x**ₜ = √(ᾱₜ)**x**₀ + √(1 − ᾱₜ)**ε** enables efficient training at arbitrary timesteps.
- ✓

  ε\_θ(**x**ₜ,t) is commonly trained with an MSE objective to predict the exact noise **ε** used to create **x**ₜ.
- ✓

  From ε\_θ you can recover an estimate of the clean sample \hat{**x**}₀, which is used to build reverse transition means.
- ✓

  Noise prediction is (up to scaling) equivalent to learning the score ∇\_{**x**} log p\_t(**x**), connecting diffusion to score matching.
- ✓

  The noise schedule {βₜ} (or ᾱₜ) controls SNR over time and has a large impact on learnability and sampling quality.
- ✓

  Sampling starts from **x**\_T ∼ 𝒩(0, I) and iteratively applies reverse updates; improved samplers reduce the number of steps.
- ✓

  Conditioning and guidance methods (e.g., classifier-free guidance) modify the effective denoising direction to satisfy prompts/labels.

## Common Mistakes

- ✗

  Confusing αₜ with ᾱₜ: αₜ = 1 − βₜ is per-step, while ᾱₜ = ∏\_{s≤t} α\_s is cumulative and appears in the direct sampling formula.
- ✗

  Assuming ε\_θ outputs “denoised **x**₀” by default; many implementations predict noise (ε), v, or **x**₀ depending on configuration, and the conversion matters.
- ✗

  Ignoring time conditioning: a network without a good embedding of t will fail because denoising at different SNRs is fundamentally different.
- ✗

  Thinking the forward process is learned: in standard diffusion, the forward noising q is fixed; only the reverse model is learned.

## Practice

easy

You have ᾱₜ = 0.64 and a clean vector **x**₀ = (3, 0). You sample **ε** = (−1, 2). Compute **x**ₜ using **x**ₜ = √(ᾱₜ)**x**₀ + √(1 − ᾱₜ)**ε**.

**Hint:** Compute √(0.64) and √(0.36) first, then scale and add componentwise.

Show solution

√(ᾱₜ) = √(0.64) = 0.8 and √(1 − ᾱₜ) = √(0.36) = 0.6.

**x**ₜ = 0.8(3,0) + 0.6(−1,2)

= (2.4, 0) + (−0.6, 1.2)

= (1.8, 1.2).

medium

Derive the \hat{**x**}₀ reconstruction formula from **x**ₜ = √(ᾱₜ)**x**₀ + √(1 − ᾱₜ)**ε** when you replace **ε** by ε\_θ(**x**ₜ,t).

**Hint:** Rearrange the equation to isolate **x**₀; treat √(ᾱₜ) as a scalar.

Show solution

Start from:

**x**ₜ = √(ᾱₜ)**x**₀ + √(1 − ᾱₜ)**ε**

Subtract the noise term:

**x**ₜ − √(1 − ᾱₜ)**ε** = √(ᾱₜ)**x**₀

Divide by √(ᾱₜ):

**x**₀ = ( **x**ₜ − √(1 − ᾱₜ)**ε** ) / √(ᾱₜ)

Replace **ε** with the model prediction ε\_θ(**x**ₜ,t):

\hat{**x**}₀(**x**ₜ,t) = ( **x**ₜ − √(1 − ᾱₜ) ε\_θ(**x**ₜ,t) ) / √(ᾱₜ).

hard

Show that if ᾱₜ → 0, then q(**x**ₜ|**x**₀) approaches 𝒩(0, I) regardless of **x**₀. Use the mean and covariance of q(**x**ₜ|**x**₀).

**Hint:** Look at the closed form q(**x**ₜ|**x**₀) = 𝒩(√(ᾱₜ)**x**₀, (1 − ᾱₜ)I) and take limits.

Show solution

We have:

q(**x**ₜ|**x**₀) = 𝒩( **μ**ₜ, Σₜ )

with

**μ**ₜ = √(ᾱₜ)**x**₀

Σₜ = (1 − ᾱₜ) I

Take ᾱₜ → 0:

**μ**ₜ → √0 · **x**₀ = **0**

Σₜ → (1 − 0) I = I

Therefore q(**x**ₜ|**x**₀) → 𝒩(0, I), independent of **x**₀. This formalizes the idea that the forward process eventually destroys all information about the original data.

## Connections

[Variational Autoencoders](/tech-tree/variational-autoencoders/)

[Score Matching](/tech-tree/score-matching/)

[Stochastic Differential Equations for ML](/tech-tree/sde-for-ml/)

[Markov Chains](/tech-tree/markov-chains/)

[U-Net Architectures](/tech-tree/u-net/)

[Classifier-Free Guidance](/tech-tree/classifier-free-guidance/)

Quality: A (4.2/5)

[← back to tree](/tech-tree/)[browse all →](/tech-tree/inventory/)
