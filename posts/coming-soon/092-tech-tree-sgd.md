---
title: Stochastic Gradient Descent
description: Gradient descent with random sample estimates. Mini-batches.
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
permalink: /tech-tree/sgd/
---

[←Back to Tech Tree](/tech-tree/)

[inventory](/tech-tree/inventory/)[coverage](/tech-tree/coverage/)

# Stochastic Gradient Descent

OptimizationDifficulty: ★★★★☆Depth: 8Unlocks: 7

Gradient descent with random sample estimates. Mini-batches.

## Interactive Visualization

⏮◀◀▶▶STEP0.25x1xZOOM

t=0s

## Core Concepts

- -Stochastic gradient estimator: compute the gradient using a random single example or a mini-batch instead of the full dataset
- -SGD iteration: perform repeated parameter updates using that noisy/random gradient estimator with a step size (same update form as gradient descent)

## Key Symbols & Notation

g\_hat\_t : stochastic gradient estimate at iteration t (computed from the sampled example or mini-batch)

## Essential Relationships

- -Expectation: E[g\_hat\_t] = full (true) gradient at the current parameters (unbiased estimator)
- -Update rule: theta\_{t+1} = theta\_t - (learning rate) \* g\_hat\_t (iterative stochastic update)

## Prerequisites (2)

[Gradient Descent6 atoms](/tech-tree/gradient-descent/)[Expected Value5 atoms](/tech-tree/expected-value/)

## Unlocks (4)

[Deep Learninglvl 5](/tech-tree/deep-learning/)[Policy Gradient Methodslvl 5](/tech-tree/policy-gradient/)[Diffusion Modelslvl 5](/tech-tree/diffusion-models/)[Meta-Learninglvl 5](/tech-tree/meta-learning/)

Advanced Learning Details

### Graph Position

89

Depth Cost

7

Fan-Out (ROI)

4

Bottleneck Score

8

Chain Length

### Cognitive Load

5

Atomic Elements

44

Total Elements

L3

Percentile Level

L3

Atomic Level

### All Concepts (19)

- - stochastic gradient: using a gradient estimate computed from a random sample (one example) instead of the full dataset
- - mini-batch: computing the gradient estimate as the average gradient over a small subset (batch) of training examples
- - stochastic gradient estimator: the random vector used in place of the true gradient (often denoted hat-g)
- - unbiased estimator (of the gradient): the property that the expectation of the stochastic gradient equals the true/full gradient
- - variance of the gradient estimator: the variability/noise in the stochastic gradient around its expectation
- - noise in parameter updates: randomness in successive parameter updates caused by estimator variance
- - batch size: the number of examples used to form a single mini-batch gradient estimate
- - iteration vs epoch: iteration = one parameter update (one mini-batch); epoch = one full pass over the dataset
- - sampling scheme: how examples are chosen for batches (with/without replacement, shuffling) and its effect on independence
- - trade-off between per-iteration computational cost and estimator variance (small batches are cheap but noisy)
- - learning rate schedule for SGD: possibly time-varying step sizes (e.g., decreasing) required for convergence guarantees
- - convergence in expectation / probabilistic convergence: SGD convergence is typically stated in expectation or with high probability rather than deterministically
- - empirical risk approximation by mini-batch: mini-batch average approximates the full empirical loss gradient
- - variance reduction by averaging: averaging gradients across batch examples reduces estimator variance
- - effect of batch size on variance: variance decreases roughly proportionally to 1/(batch size) for iid samples
- - stochasticity-induced exploration: noise can help escape shallow/local minima or saddle points
- - number of iterations per epoch = dataset\_size / batch\_size (relation between epoch count and iteration count)
- - practical considerations: shuffling data between epochs, choosing batch size and learning rate, using momentum/Adam to mitigate noise
- - terminology: 'SGD' sometimes refers to single-sample updates and sometimes to mini-batch updates

### Teaching Strategy

Quick unlock - significant prerequisite investment but simple final step. Verify prerequisites first.

Full-batch gradient descent is like steering a ship using the average of all ocean currents you can measure—accurate, but slow and expensive. Stochastic Gradient Descent (SGD) steers using a small, randomly sampled set of measurements each step—noisier, but dramatically faster per update, and often better at finding solutions that generalize.

TL;DR:

Stochastic Gradient Descent minimizes an empirical risk by repeatedly updating parameters using a *random* (single-example or mini-batch) estimate of the true gradient: **θ**ₜ₊₁ = **θ**ₜ − ηₜ **ĝ**ₜ, where **ĝ**ₜ is computed from a randomly sampled example/mini-batch. The noise makes updates cheap and can help escape poor regions, but requires careful choices of learning rate and batch size for stable convergence.

## What Is Stochastic Gradient Descent?

### Why we need something beyond full gradient descent

Suppose you are minimizing a loss over a dataset of N examples:

- •Data: {(**x**ᵢ, yᵢ)}ᵢ₌₁ᴺ
- •Model parameters: **θ** (can be a vector of weights, or millions of neural network parameters)
- •Per-example loss: ℓᵢ(**θ**) = ℓ(**θ**; **x**ᵢ, yᵢ)

A standard objective in supervised learning is the *empirical risk* (average loss):

L(**θ**) = (1/N) ∑ᵢ₌₁ᴺ ℓᵢ(**θ**)

Full-batch gradient descent computes the exact gradient of L:

∇L(**θ**) = (1/N) ∑ᵢ₌₁ᴺ ∇ℓᵢ(**θ**)

and then updates:

**θ**ₜ₊₁ = **θ**ₜ − ηₜ ∇L(**θ**ₜ)

This is conceptually simple, but computationally expensive when N is large, because each step requires scanning the whole dataset.

### Definition: SGD in one sentence

**Stochastic Gradient Descent (SGD)** is gradient descent where the gradient ∇L(**θ**) is replaced by a *stochastic (random) estimator* **ĝ**ₜ computed from a randomly sampled single example or a mini-batch.

The SGD update is:

**θ**ₜ₊₁ = **θ**ₜ − ηₜ **ĝ**ₜ

where **ĝ**ₜ ≈ ∇L(**θ**ₜ) but is computed cheaply.

### The stochastic gradient estimator **ĝ**ₜ

At iteration t, we sample:

- •**Single-example SGD**: pick iₜ uniformly from {1,…,N}
- •**ĝ**ₜ = ∇ℓᵢₜ(**θ**ₜ)

- •**Mini-batch SGD**: pick a batch Bₜ ⊂ {1,…,N} of size |Bₜ| = m
- •**ĝ**ₜ = (1/m) ∑\_{i ∈ Bₜ} ∇ℓᵢ(**θ**ₜ)

Mini-batches are the modern default.

### Why this is even “correct”: unbiasedness via expectation

A key idea is that **ĝ**ₜ is often an *unbiased* estimator of the true gradient.

Assume iₜ is uniform. Then:

E[**ĝ**ₜ | **θ**ₜ] = E[∇ℓᵢₜ(**θ**ₜ) | **θ**ₜ]

Because iₜ is uniform:

E[∇ℓᵢₜ(**θ**ₜ) | **θ**ₜ]

= (1/N) ∑ᵢ₌₁ᴺ ∇ℓᵢ(**θ**ₜ)

= ∇L(**θ**ₜ)

So, on average, SGD points in the same direction as full gradient descent.

For a mini-batch sampled uniformly (with or without replacement), you similarly get:

E[**ĝ**ₜ | **θ**ₜ] = ∇L(**θ**ₜ)

### What prerequisites does SGD really depend on?

You listed that the learner already knows Gradient Descent and Expected Value. To understand SGD deeply, it also helps to have:

- •Derivatives and partial derivatives (∂/∂θⱼ)
- •Gradients ∇L(**θ**) (vector of partial derivatives)
- •Loss functions ℓ(**θ**; **x**, y)
- •Basic probability language (random sampling, variance)

SGD is not a different *kind* of optimization step; it’s the same step using a randomized gradient estimate.

### Intuition: the “noise” is a feature, not only a bug

SGD introduces *gradient noise*:

**ĝ**ₜ = ∇L(**θ**ₜ) + **ξ**ₜ

where E[**ξ**ₜ | **θ**ₜ] = **0**.

This noise has two major effects:

1. 1)**Cheaper steps**: each update is far less expensive than summing over N examples.
2. 2)**Exploration**: noise can help move through flat regions or escape shallow/poor minima in nonconvex landscapes (common in deep learning).

But noise also causes:

- •Less smooth progress
- •Need for careful learning-rate selection
- •Different convergence behavior (often to a neighborhood unless ηₜ decreases)

That tension—cheap noisy steps vs stable accurate steps—is the heart of SGD.

## Core Mechanic 1: Mini-batches, Noise, and the Stochastic Gradient

### Why mini-batches exist (not just “because GPUs”)

Single-example SGD is maximally noisy: one example can be atypical, leading to a gradient that points away from the true average direction.

Mini-batches reduce noise by averaging several example gradients.

Let Bₜ be a mini-batch of size m. Define:

**ĝ**ₜ = (1/m) ∑\_{i ∈ Bₜ} ∇ℓᵢ(**θ**ₜ)

This is still stochastic (depends on which batch you drew), but typically has smaller variance than a single-example gradient.

### A variance viewpoint (the key conceptual lever)

Think of per-example gradients as random vectors:

**G** = ∇ℓᵢ(**θ**)

where i is a random index uniform over {1,…,N}. Then:

E[**G**] = ∇L(**θ**)

The mini-batch gradient is an average of m i.i.d. (approximately i.i.d.) samples:

**ĝ** = (1/m) ∑\_{k=1}^m **G**ₖ

A core statistical fact: averaging reduces variance.

Very informally (scalar intuition), if Var(G) = σ², then:

Var(ĝ) = σ² / m

For vectors, you can think in terms of covariance matrices; the same “divide by m” scaling appears under independence assumptions.

**Practical meaning**:

- •Larger batch → less noisy updates → more stable training
- •Smaller batch → noisier updates → cheaper per step + sometimes better generalization

### Why the noise can *help* (conceptual clarity)

It’s tempting to view noise as purely harmful. But in large nonconvex problems (deep nets), the objective surface has:

- •many flat regions (small ‖∇L‖)
- •saddle points (directions of both upward and downward curvature)
- •many local minima of varying “sharpness”

Noise can:

- •kick the iterate out of saddle points
- •prevent over-committing to sharp minima
- •act like a kind of implicit regularization (not guaranteed, but often observed)

A useful mental model is that SGD behaves like gradient descent plus random perturbations.

### Epochs, iterations, and data order

Terminology you will see constantly:

- •**Iteration / step**: one parameter update (one mini-batch processed)
- •**Epoch**: one full pass through the dataset (N examples), often by shuffling and then batching

If batch size is m, then steps per epoch ≈ N/m.

A common training loop:

1. 1)Shuffle data (to avoid correlated batches)
2. 2)Split into mini-batches
3. 3)For each mini-batch B:

- •compute **ĝ**
- •update **θ** ← **θ** − η **ĝ**

The shuffle matters: if data are ordered (e.g., all cats then all dogs), batches become biased and SGD can behave poorly.

### Comparing full-batch, mini-batch, and single-example

| Method | Gradient used | Cost per step | Noise level | Typical use |
| --- | --- | --- | --- | --- |
| Full-batch GD | ∇L = (1/N)∑∇ℓᵢ | High | None | Small datasets, convex problems |
| Mini-batch SGD | (1/m)∑\_{i∈B}∇ℓᵢ | Medium | Medium (↓ with m) | Default in deep learning |
| Single-example SGD | ∇ℓᵢ | Low | High | Rare alone; sometimes online learning |

### A subtle but important point: “SGD” often means “mini-batch SGD”

In modern ML, people say “SGD” even when m = 128 or 1024. The defining feature is still the same: **ĝ**ₜ is computed from a random subset, not the full dataset.

### Measuring noise with the gradient norm

A quick diagnostic idea:

- •If ‖**ĝ**ₜ‖ fluctuates wildly across batches, you likely have high gradient noise.
- •Increasing batch size, using momentum, or lowering η can stabilize.

But there is no universal best setting: compute budget, model size, and data complexity all interact.

## Core Mechanic 2: Learning Rate, Convergence Behavior, and Practical Stability

### Why learning rate matters more in SGD than in full-batch GD

In full-batch GD, the gradient is deterministic for a given **θ**. In SGD, the update direction changes randomly each step.

If η is too large, noise can cause the iterates to bounce around or diverge.

If η is too small, progress becomes extremely slow.

So in SGD, η is not just “step size”; it controls the trade-off between:

- •moving quickly toward low loss
- •averaging out gradient noise

### A useful decomposition: drift + noise

Write:

**ĝ**ₜ = ∇L(**θ**ₜ) + **ξ**ₜ, with E[**ξ**ₜ|**θ**ₜ] = **0**.

Then the update is:

**θ**ₜ₊₁

= **θ**ₜ − ηₜ ∇L(**θ**ₜ) − ηₜ **ξ**ₜ

You can read this as:

- •−ηₜ ∇L(**θ**ₜ): the “drift” toward lower loss
- •−ηₜ **ξ**ₜ: the random walk component (scaled by ηₜ)

If ηₜ stays constant, the random component never truly disappears; you often converge to a *neighborhood* around a minimizer.

If ηₜ decays (ηₜ ↓ 0), noise influence shrinks and you can converge more tightly.

### Classical convergence intuition (high level)

Under convexity and smoothness assumptions (and unbiased gradients with bounded variance), SGD can achieve convergence rates like:

- •with diminishing ηₜ, convergence in expectation to the optimum
- •with constant η, convergence to a ball whose radius depends on η and gradient variance

You don’t need the full proofs to use SGD, but the intuition is essential:

- •**Constant η** is good for fast training and tracking nonstationarity, but leaves residual noise.
- •**Decaying ηₜ** improves final convergence but can slow late-stage training.

### Learning-rate schedules (what people do)

Common schedules:

1. 1)**Step decay**: η drops by a factor (e.g., ×0.1) at fixed epochs.
2. 2)**Cosine decay**: smooth decay from η₀ to near 0.
3. 3)**Warmup**: start with a small η and increase over the first few epochs.

Warmup helps when early gradients are unstable (common in deep nets).

### Batch size and learning rate are linked

Bigger batches reduce gradient variance, so you can often use larger η.

A rough heuristic sometimes used is “linear scaling”:

η ∝ m

when increasing batch size m, at least within some range.

But this is not a law; it depends on model, optimizer (momentum/Adam), and data.

### Momentum (brief, because it often comes with SGD)

Many practitioners mean “SGD with momentum.” Momentum reduces variance by averaging gradients over time.

A standard momentum form:

**v**ₜ₊₁ = β **v**ₜ + **ĝ**ₜ

**θ**ₜ₊₁ = **θ**ₜ − η **v**ₜ₊₁

with β ∈ [0,1). Typical β is 0.9.

Conceptually:

- •If gradients point consistently in one direction, momentum accelerates.
- •If gradients oscillate due to noise, momentum damps oscillation.

Even if you don’t use momentum in a first implementation, you should recognize it as a key stabilization tool.

### Convergence “look and feel” in practice

When you plot training loss vs steps:

- •Full-batch GD: smoother curve; each step expensive
- •SGD: noisy curve; each step cheap

Often you care about *loss vs wall-clock time*, not loss vs number of steps.

SGD wins because it can take many more steps per second.

### When SGD is especially appropriate

SGD shines when:

- •N is large (millions of examples)
- •model is large (deep nets)
- •you need frequent updates (online/streaming)
- •exact gradients are too costly

When full-batch methods may be fine:

- •small N
- •strongly convex objective with cheap exact gradients
- •you want very stable deterministic progress

### A practical checklist for stability

If training diverges or is wildly unstable:

- •Reduce η (most common fix)
- •Increase batch size m
- •Add momentum (or reduce β if already using it)
- •Normalize inputs / use batch norm (modeling choice)
- •Check for exploding gradients (clip ‖**g**‖)

SGD is simple, but its behavior is tightly coupled to these choices.

## Application/Connection: SGD in Linear Regression and in Deep Learning Workflows

### Why linear regression is the perfect “glass box” example

Linear regression lets you see SGD without distractions:

- •the loss is convex
- •gradients have a closed form
- •you can compute both full and stochastic gradients

Yet the training loop is structurally the same as in deep learning.

### Empirical risk minimization template

Most ML training loops fit this template:

L(**θ**) = (1/N) ∑ᵢ ℓᵢ(**θ**)

SGD uses the per-example (or per-batch) gradient to approximate ∇L.

This same structure appears in:

- •classification with cross-entropy
- •matrix factorization
- •neural networks (backprop computes ∇ℓᵢ)

So once SGD is clear, “training deep networks” becomes less mysterious: the core loop is the same, only the gradient computation is more complex.

### Practical hyperparameters: what you actually tune

The big three:

1. 1)**Learning rate η**
2. 2)**Batch size m**
3. 3)**Number of epochs / steps**

Secondary but common:

- •shuffle strategy
- •momentum β
- •weight decay (ℓ² regularization)

A compact comparison of trade-offs:

| Knob | Increase it → | Benefits | Costs/Risks |
| --- | --- | --- | --- |
| Learning rate η | bigger steps | faster initial progress | divergence, overshooting |
| Batch size m | lower noise | smoother training, better hardware utilization | less regularization effect, more memory |
| Epochs | more passes | better fit | overfitting, time |

### Interpreting “generalization” effects

Empirically, small-batch SGD often finds solutions that generalize better than large-batch training for the same compute.

One intuitive story: noise biases the optimizer toward flatter minima (regions where small parameter changes don’t increase loss much). Flatter minima often correlate with better generalization.

This is not a universal theorem, but it’s a useful working intuition.

### Connections to the nodes you unlock

SGD is the workhorse behind many advanced methods:

- •**Deep Learning**: training neural networks is essentially repeated mini-batch SGD updates using backprop gradients.
- •**Policy Gradient Methods**: gradients are estimated from sampled trajectories; the stochasticity is fundamental (you can’t enumerate all futures).
- •**Diffusion Models**: training score networks uses mini-batch SGD over noisy samples and time steps.
- •**Meta-Learning**: algorithms like MAML involve differentiating through SGD steps; the SGD update itself becomes part of the computation graph.

### A final conceptual anchor

If you remember only one thing:

SGD is not “a different update rule.” It is **gradient descent using a random estimate of the gradient**.

Everything else—mini-batches, schedules, momentum, stability tricks—is about managing the consequences of that randomness.

## Worked Examples (3)

### Single-example SGD on 1D linear regression (fully computed by hand)

We fit a 1D linear model ŷ = w x (no bias) using squared error. Dataset has two points: (x₁=1, y₁=2), (x₂=2, y₂=0). Per-example loss: ℓᵢ(w) = (1/2)(w xᵢ − yᵢ)². Empirical loss: L(w) = (1/2)·(1/2)∑ᵢ (w xᵢ − yᵢ)² = (1/4)∑ᵢ (w xᵢ − yᵢ)². We will do SGD with learning rate η = 0.1, starting at w₀ = 0. We sample one example per step.

1. Compute the per-example gradient.

   ℓᵢ(w) = (1/2)(w xᵢ − yᵢ)²

   dℓᵢ/dw = (1/2)·2(w xᵢ − yᵢ)·xᵢ

   = (w xᵢ − yᵢ) xᵢ
2. Step t=0: sample example 1 (i₀=1).

   At w₀=0:

   ĝ₀ = dℓ₁/dw = (w₀ x₁ − y₁) x₁

   = (0·1 − 2)·1

   = −2

   Update:

   w₁ = w₀ − η ĝ₀ = 0 − 0.1(−2) = 0.2
3. Step t=1: sample example 2 (i₁=2).

   At w₁=0.2:

   ĝ₁ = dℓ₂/dw = (w₁ x₂ − y₂) x₂

   = (0.2·2 − 0)·2

   = (0.4)·2

   = 0.8

   Update:

   w₂ = w₁ − η ĝ₁ = 0.2 − 0.1(0.8) = 0.12
4. Step t=2: sample example 1 again (i₂=1).

   At w₂=0.12:

   ĝ₂ = (w₂·1 − 2)·1 = (0.12 − 2) = −1.88

   Update:

   w₃ = 0.12 − 0.1(−1.88) = 0.308
5. Compare with the full gradient direction at w₂=0.12.

   Full gradient of empirical loss L(w) = (1/4)∑(w xᵢ − yᵢ)²:

   First compute d/dw of (w xᵢ − yᵢ)² = 2(w xᵢ − yᵢ)xᵢ.

   So:

   dL/dw = (1/4)∑ 2(w xᵢ − yᵢ)xᵢ

   = (1/2)∑ (w xᵢ − yᵢ)xᵢ

   At w=0.12:

   For i=1: (0.12·1 − 2)·1 = −1.88

   For i=2: (0.12·2 − 0)·2 = (0.24)·2 = 0.48

   Sum = −1.88 + 0.48 = −1.40

   So dL/dw = (1/2)(−1.40) = −0.70

   A full-batch GD step would move w upward by 0.1·0.70 = 0.07 (to 0.19).

   SGD’s step depended on which example we sampled; it moved more (to 0.308) when it saw the high-error example 1.

**Insight:** SGD makes progress using gradients from individual examples. Each step is cheap but noisy: the update direction can differ substantially from the full gradient. Over time, the randomness averages out, but the trajectory is jagged.

### Mini-batch SGD for logistic regression (vector form, showing the stochastic gradient estimator)

Binary classification with logistic regression. For each example (**x**ᵢ, yᵢ) with yᵢ ∈ {0,1}, model pᵢ = σ(**w**ᵀ**x**ᵢ) where σ(z)=1/(1+e^(−z)). Per-example loss (cross-entropy): ℓᵢ(**w**) = −yᵢ log pᵢ − (1−yᵢ) log(1−pᵢ). We use a mini-batch Bₜ of size m to compute **ĝ**ₜ and update **w**.

1. Compute gradient of per-example loss.

   Let zᵢ = **w**ᵀ**x**ᵢ, pᵢ = σ(zᵢ).

   A standard result:

   ∇ℓᵢ(**w**) = (pᵢ − yᵢ) **x**ᵢ

   Derivation sketch (showing the key chain rule steps):

   ∂ℓᵢ/∂zᵢ = pᵢ − yᵢ

   and ∂zᵢ/∂**w** = **x**ᵢ

   So ∇ℓᵢ(**w**) = (∂ℓᵢ/∂zᵢ)(∂zᵢ/∂**w**) = (pᵢ − yᵢ)**x**ᵢ
2. Define the empirical objective:

   L(**w**) = (1/N) ∑ᵢ ℓᵢ(**w**)

   Full gradient:

   ∇L(**w**) = (1/N) ∑ᵢ (pᵢ − yᵢ)**x**ᵢ
3. Mini-batch stochastic gradient estimator at step t:

   Sample Bₜ uniformly, |Bₜ| = m.

   **ĝ**ₜ = (1/m) ∑\_{i∈Bₜ} ∇ℓᵢ(**w**ₜ)

   = (1/m) ∑\_{i∈Bₜ} (pᵢ − yᵢ) **x**ᵢ
4. SGD update:

   **w**ₜ₊₁ = **w**ₜ − ηₜ **ĝ**ₜ

   = **w**ₜ − ηₜ (1/m) ∑\_{i∈Bₜ} (pᵢ − yᵢ) **x**ᵢ
5. Unbiasedness check (conceptual):

   If Bₜ is sampled uniformly, then

   E[**ĝ**ₜ | **w**ₜ] = ∇L(**w**ₜ)

   So in expectation, the update is a descent direction for the full objective.

**Insight:** In deep learning, backprop computes ∇ℓᵢ(**θ**) for each sample in a mini-batch. Mini-batch SGD is simply the average of those per-sample gradients, used as **ĝ**ₜ in the same update rule.

### Seeing batch size reduce noise (a tiny numeric thought experiment)

Assume at some **θ**, per-example gradients along one coordinate behave like a random variable G with mean μ and variance σ². We compare a single-example gradient estimate ĝ₁ = G to a mini-batch estimate ĝₘ = (1/m)∑\_{k=1}^m Gₖ (independent samples).

1. Compute expectation:

   E[ĝₘ] = E[(1/m)∑ Gₖ] = (1/m)∑ E[Gₖ] = (1/m)·m·μ = μ
2. Compute variance:

   Var(ĝₘ) = Var((1/m)∑ Gₖ)

   = (1/m²) Var(∑ Gₖ)

   Assuming independence:

   Var(∑ Gₖ) = ∑ Var(Gₖ) = m σ²

   So:

   Var(ĝₘ) = (1/m²)(m σ²) = σ²/m
3. Interpretation:

   If you quadruple batch size (m → 4m), the variance halves twice:

   σ²/(4m) = (1/4)(σ²/m).

   So the stochastic gradient concentrates around the true gradient as batch size increases.

**Insight:** Mini-batches are a statistical averaging device. They trade extra compute per step for a cleaner gradient direction, often allowing a larger learning rate or more stable optimization.

## Key Takeaways

- ✓

  SGD uses a stochastic gradient estimate **ĝ**ₜ computed from a randomly sampled example or mini-batch: **θ**ₜ₊₁ = **θ**ₜ − ηₜ **ĝ**ₜ.
- ✓

  For uniform sampling, **ĝ**ₜ is typically unbiased: E[**ĝ**ₜ | **θ**ₜ] = ∇L(**θ**ₜ).
- ✓

  Mini-batching reduces gradient noise: averaging over m samples reduces variance roughly like 1/m (under independence assumptions).
- ✓

  SGD’s noise makes training curves jagged; with constant η it often converges to a neighborhood, while decaying ηₜ tightens convergence.
- ✓

  Learning rate η and batch size m are coupled: bigger batches often permit larger η, but may reduce helpful noise/implicit regularization.
- ✓

  Shuffling data each epoch matters; biased or correlated batches can break SGD’s assumptions and harm convergence.
- ✓

  Many practical “SGD” implementations include momentum, which smooths updates and reduces oscillations.

## Common Mistakes

- ✗

  Confusing SGD with a different optimization rule: it’s still gradient descent, just using **ĝ**ₜ instead of ∇L.
- ✗

  Using too large a learning rate because each step is cheap—SGD can diverge quickly when η is not tuned.
- ✗

  Not shuffling data (or batching in a biased order), causing systematically biased gradient estimates and poor training.
- ✗

  Assuming bigger batch is always better: it reduces noise but can hurt generalization and may require schedule changes.

## Practice

easy

You have L(**θ**) = (1/N)∑ᵢ ℓᵢ(**θ**). You sample i uniformly and set **ĝ** = ∇ℓᵢ(**θ**). Show that E[**ĝ**] = ∇L(**θ**).

**Hint:** Write the expectation as a sum over i with probability 1/N.

Show solution

Because P(i=k)=1/N,

E[**ĝ**] = ∑\_{k=1}^N (1/N) ∇ℓ\_k(**θ**)

= (1/N)∑\_{k=1}^N ∇ℓ\_k(**θ**)

= ∇[(1/N)∑\_{k=1}^N ℓ\_k(**θ**)]

= ∇L(**θ**).

medium

Consider 1D linear regression ŷ = w x with per-example loss ℓᵢ(w) = (1/2)(w xᵢ − yᵢ)². For a mini-batch B of size m, write the mini-batch gradient estimator ĝ(w) and the SGD update. Then compute ĝ(w) explicitly for batch B = { (x=1,y=2), (x=3,y=1) } at w=0.

**Hint:** First compute dℓᵢ/dw = (w xᵢ − yᵢ)xᵢ, then average across the batch.

Show solution

Per-example gradient: dℓᵢ/dw = (w xᵢ − yᵢ)xᵢ.

Mini-batch estimator:

ĝ(w) = (1/m)∑\_{i∈B} (w xᵢ − yᵢ)xᵢ.

Update: w⁺ = w − η ĝ(w).

Here m=2 and w=0.

For (1,2): (0·1−2)·1 = −2.

For (3,1): (0·3−1)·3 = −3.

Average: ĝ(0) = (1/2)(−2 + −3) = −2.5.

So w⁺ = 0 − η(−2.5) = 2.5η.

hard

Assume a scalar per-example gradient random variable G has Var(G)=σ². For a mini-batch average ĝₘ = (1/m)∑\_{k=1}^m Gₖ with independent samples, derive Var(ĝₘ). If σ²=16, compare the standard deviation of ĝ₁, ĝ₄, and ĝ₁₆.

**Hint:** Use Var(aX)=a²Var(X) and Var(∑ independent)=∑Var.

Show solution

Var(ĝₘ) = Var((1/m)∑ Gₖ) = (1/m²) Var(∑ Gₖ).

Independence gives Var(∑ Gₖ)=∑Var(Gₖ)=mσ².

So Var(ĝₘ) = (1/m²)(mσ²)=σ²/m.

Standard deviation is √(σ²/m)=σ/√m.

With σ²=16, σ=4.

- •m=1: std = 4/√1 = 4
- •m=4: std = 4/2 = 2
- •m=16: std = 4/4 = 1

## Connections

- •[Gradient Descent](/tech-tree/gradient-descent/)
- •[Expected Value](/tech-tree/expected-value/)
- •[Deep Learning](/tech-tree/deep-learning/)
- •[Policy Gradient Methods](/tech-tree/policy-gradient/)
- •[Diffusion Models](/tech-tree/diffusion-models/)
- •[Meta-Learning](/tech-tree/meta-learning/)
- •[Momentum](/tech-tree/momentum/)
- •[Learning Rate Schedules](/tech-tree/learning-rate-schedules/)

Quality: A (4.4/5)

[← back to tree](/tech-tree/)[browse all →](/tech-tree/inventory/)
