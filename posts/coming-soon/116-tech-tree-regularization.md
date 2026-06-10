---
title: Regularization
description: Preventing overfitting. L1, L2 penalties. Dropout.
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
permalink: /tech-tree/regularization/
---

[←Back to Tech Tree](/tech-tree/)

[inventory](/tech-tree/inventory/)[coverage](/tech-tree/coverage/)

# Regularization

Machine LearningDifficulty: ★★★★☆Depth: 11Unlocks: 4

Preventing overfitting. L1, L2 penalties. Dropout.

## Interactive Visualization

⏮◀◀▶▶STEP0.25x1xZOOM

t=0s

## Core Concepts

- -Regularization as augmenting the training loss with a penalty term to control model complexity (loss + penalty)
- -Penalty norms as direct parameter constraints: L2 (weight decay) causes weight shrinkage; L1 induces sparsity
- -Dropout: stochastic masking of units during training that reduces co-adaptation and acts like implicit model averaging

## Key Symbols & Notation

lambda (regularization strength, scalar multiplier on penalty)L2 norm squared written as ||w||\_2^2L1 norm written as ||w||\_1

## Essential Relationships

- -Adding lambda \* (norm penalty) to the loss lowers effective capacity and thus reduces overfitting
- -L2 penalty -> smooth shrinkage of weights (small nonzero values); L1 penalty -> drives exact zeros (sparse parameters)
- -Dropout training with random unit masks approximates averaging many thinned networks at test time, improving generalization by reducing co-adaptation

## Prerequisites (2)

[Neural Networks6 atoms](/tech-tree/neural-networks/)[Convex Optimization5 atoms](/tech-tree/convex-optimization/)

## Unlocks (1)

[Deep Learninglvl 5](/tech-tree/deep-learning/)

Advanced Learning Details

### Graph Position

154

Depth Cost

4

Fan-Out (ROI)

2

Bottleneck Score

11

Chain Length

### Cognitive Load

9

Atomic Elements

41

Total Elements

L3

Percentile Level

L4

Atomic Level

### All Concepts (16)

- - Overfitting vs generalization: model fits training data well but performs poorly on unseen data
- - Regularization as an explicit penalty added to the training loss to discourage complex/large-weight solutions
- - Regularization coefficient (λ): a scalar hyperparameter that controls strength of the penalty
- - L2 regularization (ridge): penalty proportional to the squared L2 norm of weights (||w||\_2^2)
- - L1 regularization (lasso): penalty proportional to the L1 norm of weights (||w||\_1)
- - Sparsity: L1 tends to produce exact zero weights (feature selection) whereas L2 does not
- - Weight decay: view of L2 regularization as multiplicative shrinkage of weights during gradient-based updates
- - Non-differentiability of L1 at zero and its practical consequences for optimization (kink -> sparse solutions / need for subgradient or proximal methods)
- - Bayesian/MAP interpretation: L2 corresponds to a Gaussian prior on weights; L1 corresponds to a Laplace prior
- - Capacity control via norms: using weight norms (L1/L2) to bound or control model capacity
- - Dropout: stochastic training technique that multiplies units/activations by random binary masks (thinning) each minibatch
- - Keep probability (q) and dropout probability (p = 1 - q): hyperparameters controlling how many units are kept/dropped
- - Inverted dropout scaling: scaling activations so expected activation at train time equals test time (or alternatively scaling at test time)
- - Dropout as model averaging / ensemble approximation: training many thinned sub-networks and implicitly averaging them at test time
- - Dropout reduces co-adaptation of neurons by injecting multiplicative noise during training
- - Regularization changes the optimization objective and therefore the gradients used during training (penalty term contributes to gradient)

### Teaching Strategy

Multi-session curriculum - substantial prior knowledge and complex material. Use mastery gates and deliberate practice.

Training loss going down while validation loss goes up is one of the most common “surprises” in machine learning. Regularization is the toolkit for preventing that surprise: you deliberately restrict (or noise up) your model so it can’t memorize quirks of the training set and is forced to learn patterns that generalize.

TL;DR:

Regularization modifies learning to prefer simpler, more robust solutions. The most common form is adding a penalty to the objective: minimize L(θ) + λ·Ω(θ). L2 (‖**w**‖₂²) shrinks weights smoothly (“weight decay”), L1 (‖**w**‖₁) promotes sparsity (many weights become exactly 0), and dropout randomly masks units during training to reduce co-adaptation and behaves like implicit ensembling.

## What Is Regularization?

### The problem: overfitting is an optimization success but a modeling failure

In supervised learning, you pick parameters θ to minimize an empirical (training) loss:

- •Data: {(**x**ᵢ, yᵢ)}ᵢ₌₁ⁿ
- •Model: f(**x**; θ)
- •Loss per example: ℓ(f(**x**ᵢ; θ), yᵢ)
- •Training objective:

J\_train(θ) = (1/n) ∑ᵢ ℓ(f(**x**ᵢ; θ), yᵢ)

If the model is flexible enough (especially deep nets), J\_train can often be pushed very low. But “low training loss” is not the goal. The goal is low *generalization error* on unseen data.

Overfitting happens when the model uses its capacity to fit idiosyncrasies: noise, rare coincidences, spurious correlations. The optimization succeeds (training loss drops), but the representation learned is brittle.

### The idea: constrain complexity so learning can’t memorize

Regularization is any technique that changes the learning problem so that the solution is biased toward simpler / smoother / more stable models.

The most canonical framing is: **augment the loss with a penalty term**.

J\_reg(θ) = J\_train(θ) + λ·Ω(θ)

- •Ω(θ) measures “complexity” (often via parameter norms).
- •λ ≥ 0 controls the tradeoff.

This is the atomic concept to keep returning to:

> Regularization = minimize loss + penalty.

It’s not merely a trick; it’s a deliberate statement of preference: among many parameter settings that fit the data similarly well, prefer the one with smaller norm, fewer nonzero parameters, or better robustness.

### Why regularization helps generalization

There are several complementary lenses:

1) **Bias–variance tradeoff (classical)**

- •High-capacity models have low bias but high variance: they adapt strongly to the sample.
- •Regularization increases bias slightly but reduces variance, often improving test error.

2) **Stability / robustness (modern intuition)**

- •Small changes to the training data shouldn’t radically change predictions.
- •Penalties like L2 discourage extreme parameter values that can make the model sensitive.

3) **Constrained optimization equivalence**

Minimizing loss + penalty is often equivalent to minimizing loss subject to a constraint.

For L2:

minimize J\_train(**w**) + λ‖**w**‖₂²

is closely related to

minimize J\_train(**w**) subject to ‖**w**‖₂² ≤ c

The penalty formulation is convenient for gradient methods; the constraint formulation is useful for geometric intuition.

### Regularization in deep learning

Deep networks complicate the story because “complexity” is not perfectly captured by parameter count alone. Still, regularization remains essential.

Three cornerstone tools you’ll use constantly:

| Technique | What it modifies | Primary effect |
| --- | --- | --- |
| L2 penalty (weight decay) | Objective (adds λ‖**w**‖₂²) | Shrinks weights smoothly; improves stability |
| L1 penalty | Objective (adds λ‖**w**‖₁) | Drives many weights to 0 (sparsity) |
| Dropout | Training procedure (random masking) | Reduces co-adaptation; implicit model averaging |

In the next sections, we’ll build each one from motivation → math → behavior → practical use.

## Core Mechanic 1: L2 Regularization (‖w‖₂²) and Weight Decay

### Why L2 is the default

If you want a regularizer that:

- •plays nicely with gradient-based optimization,
- •discourages large weights without forcing exact zeros,
- •tends to improve stability and calibration,

…then L2 is usually the first choice.

In neural nets, you’ll often see it called **weight decay**, because the update rule literally decays weights a bit each step.

### The objective

Let **w** denote the vector of weights you want to penalize (often all weights, sometimes excluding biases and normalization parameters).

J(**w**) = J\_train(**w**) + λ‖**w**‖₂²

Recall:

‖**w**‖₂² = ∑ⱼ wⱼ²

So the penalty grows quadratically with magnitude.

### Show the work: gradient of the L2 penalty

We’ll derive the gradient term you add during backprop.

Ω(**w**) = ‖**w**‖₂² = ∑ⱼ wⱼ²

Take partial derivative for coordinate j:

∂Ω/∂wⱼ = ∂/∂wⱼ (∑ₖ wₖ²)

= 2wⱼ

So

∇Ω(**w**) = 2**w**

Therefore the gradient of the regularized objective is:

∇J(**w**) = ∇J\_train(**w**) + λ∇Ω(**w**)

= ∇J\_train(**w**) + 2λ**w**

### Weight decay update (SGD)

With learning rate η, SGD updates are:

**w** ← **w** − η(∇J\_train(**w**) + 2λ**w**)

Rearrange:

**w** ← **w** − η∇J\_train(**w**) − 2ηλ**w**

Factor **w**:

**w** ← (1 − 2ηλ)**w** − η∇J\_train(**w**)

That factor (1 − 2ηλ) is the “decay”: every step pulls weights toward 0.

### Geometric intuition: why L2 gives smooth shrinkage

Consider the constrained form:

minimize J\_train(**w**) subject to ‖**w**‖₂² ≤ c

The L2 ball is a circle (in 2D) or sphere (in higher dimensions). When you intersect a smooth loss surface with a round constraint set, the optimum typically lies on the boundary but not at axes corners. This leads to **many small weights** rather than **a few exactly zero** weights.

### Bayesian view (useful intuition, not required)

L2 regularization corresponds to a Gaussian prior on weights:

p(**w**) ∝ exp(−(λ)‖**w**‖₂²)

Minimizing J\_train + λ‖**w**‖₂² is like MAP estimation: fit the data while preferring weights near 0.

### Practical notes in deep nets

1) **What to regularize**

- •Common: penalize weights in linear/conv layers.
- •Often *exclude*: bias terms, and sometimes BatchNorm parameters (γ, β), because penalizing them can hurt optimization.

2) **Choosing λ**

- •Too small: little effect, overfitting persists.
- •Too large: underfitting, slow learning, overly damped features.
- •Typically tuned on validation; often log-scale search (e.g., 1e−6, 1e−5, …, 1e−2).

3) **Weight decay vs L2 penalty in adaptive optimizers**

In SGD, “L2 regularization” and “weight decay” are effectively the same. In Adam/RMSProp, naïvely adding λ‖**w**‖₂² to the loss is *not identical* to decoupled weight decay.

- •**L2 penalty**: adds 2λ**w** into the gradient that then gets rescaled by Adam’s adaptive terms.
- •**Decoupled weight decay (AdamW)**: applies decay directly: **w** ← (1 − ηλ)**w** − η·(Adam gradient)

In practice, for Adam-family optimizers, **AdamW** is often preferred because the regularization effect is more predictable.

### What L2 does to the learned function

Even though L2 acts on parameters, its functional effect is:

- •smoother mappings,
- •less sensitivity to input perturbations (often),
- •reduced reliance on rare features,
- •better behaved decision boundaries.

Keep one mental picture: **L2 spreads influence across many features with small coefficients**, rather than betting everything on a few huge weights.

## Core Mechanic 2: L1 Regularization (‖w‖₁) and Sparsity

### Why L1 is different from L2

L1 regularization is used when you want:

- •a model that uses only a subset of features,
- •interpretability (feature selection),
- •compression (many parameters exactly zero),

or when you suspect many true effects are actually irrelevant.

Where L2 shrinks everything smoothly, **L1 tends to create exact zeros**.

### The objective

J(**w**) = J\_train(**w**) + λ‖**w**‖₁

where

‖**w**‖₁ = ∑ⱼ |wⱼ|

### Why L1 induces sparsity (geometric intuition)

Consider the constrained form:

minimize J\_train(**w**) subject to ‖**w**‖₁ ≤ c

In 2D, the L1 ball is a diamond (a rotated square). Its corners lie on the coordinate axes.

When a smooth loss contour first touches this diamond, it often touches at a corner.

Touching at a corner means one coordinate is exactly 0.

This “corners encourage zeros” intuition is the key:

- •L2 ball: round → solutions rarely land exactly on axes.
- •L1 ball: pointy corners → solutions often hit axes → sparsity.

### Show the work: (sub)gradient of L1

The absolute value is not differentiable at 0, so we use a subgradient.

For a single coordinate:

d|w|/dw =

- •+1 if w > 0
- •−1 if w < 0
- •any value in [−1, +1] if w = 0

So a subgradient of ‖**w**‖₁ is:

∂‖**w**‖₁/∂wⱼ = sign(wⱼ) (with sign(0) ∈ [−1, +1])

Thus a subgradient update looks like:

**w** ← **w** − η(∇J\_train(**w**) + λ·sign(**w**))

### Soft-thresholding (important behavior)

For some losses (notably squared loss in linear regression), L1 leads to a closed-form coordinate update called **soft-thresholding**.

Even if you don’t use the closed form in deep learning, the behavior is worth understanding: L1 applies a constant pull toward 0, not proportional to w.

Compare pulls:

- •L2: gradient term is 2λwⱼ → small weights get tiny pull.
- •L1: gradient term is λ·sign(wⱼ) → small weights get the same-size pull as large weights.

That’s why small weights get “snapped” to zero under L1.

### L1 in modern deep learning practice

Pure L1 on all network weights is less common than L2/weight decay, because:

- •optimization can be less smooth,
- •deep nets often benefit from distributed representations rather than strict sparsity,
- •structured sparsity (entire channels/filters) is often more useful than individual-weight sparsity.

But L1 still matters a lot in:

- •linear models and generalized linear models,
- •sparse feature settings (e.g., bag-of-words),
- •feature selection pipelines,
- •inducing sparsity for compression/pruning,
- •variants like elastic net (L1 + L2).

### Elastic net (bridge between L1 and L2)

Sometimes you want sparsity *and* stability:

J(**w**) = J\_train(**w**) + λ₁‖**w**‖₁ + λ₂‖**w**‖₂²

L1 alone can be unstable when features are strongly correlated; L2 helps group correlated features and improves conditioning.

### Summary comparison: L1 vs L2

| Property | L1 (‖**w**‖₁) | L2 (‖**w**‖₂²) |
| --- | --- | --- |
| Pull toward 0 | constant magnitude (λ) | proportional to size (2λw) |
| Exact zeros? | yes, often | rarely |
| Optimization smoothness | nonsmooth at 0 | smooth |
| Typical effect | sparsity / feature selection | shrinkage / stability |
| Common in deep nets | less common (unstructured) | very common |

If L2 is “make everything smaller,” L1 is “make many things vanish.”

## Core Mechanic 3: Dropout as Stochastic Regularization and Implicit Ensembling

### Why dropout exists

Neural networks can overfit by forming **co-adaptations**: a hidden unit becomes useful only because some other unit reliably provides a complementary signal. This can produce fragile internal representations.

Dropout regularizes by injecting structured noise during training:

- •Randomly remove (mask) units or activations.
- •Force the network to perform well under many thinned variants.

The motivation is simple: if any unit might disappear, the network must distribute information and learn redundant, robust features.

### The mechanism (inverted dropout)

Let **h** be a vector of activations at some layer. Sample a mask **m** with independent Bernoulli entries:

mⱼ ∼ Bernoulli(p)

- •p is the **keep probability** (commonly 0.5 for hidden layers historically; often higher in modern nets).

Apply mask:

**h̃** = (**m** ⊙ **h**) / p

- •⊙ is elementwise multiplication.
- •Division by p is **inverted dropout**, ensuring E[**h̃**] = **h**.

**Show the work:**

For one coordinate:

h̃ⱼ = (mⱼ hⱼ)/p

E[h̃ⱼ] = E[mⱼ]·hⱼ/p

= p·hⱼ/p

= hⱼ

So at test time you typically do nothing special (no dropout, no scaling), because the scaling was already handled during training.

### Dropout as implicit model averaging

Each dropout mask corresponds to a sub-network. Training with dropout is like training a huge ensemble of thinned networks that share weights.

You do not explicitly average predictions over all masks at test time (that would be expensive). Instead, using the full network without dropout approximates that ensemble average.

This is why dropout often improves generalization even when it increases training loss: it optimizes performance across many perturbations, not one fixed computation graph.

### Where dropout works well (and where it doesn’t)

Dropout is most effective when:

- •the network is prone to co-adaptation,
- •data is limited relative to model size,
- •you’re using large fully-connected layers.

It can be less helpful (or need careful tuning) when:

- •BatchNorm is used heavily (both add noise; sometimes redundant),
- •convolutional features are already strongly regularized by weight sharing and data augmentation,
- •you apply high dropout early in conv stacks (can harm feature extraction).

Modern practice often uses:

- •lower dropout rates,
- •dropout mainly in classifier heads,
- •alternatives like stochastic depth (for residual networks) or drop-path.

### Dropout vs L1/L2: what’s being “penalized”?

Dropout usually isn’t written as loss + λ·Ω(θ) explicitly. It’s a **procedural regularizer**.

Still, conceptually it:

- •adds noise to activations,
- •encourages smaller effective reliance on any single path,
- •acts like a capacity control mechanism.

A useful comparison:

| Method | How it regularizes | Typical symptom it fixes |
| --- | --- | --- |
| L2 | discourages large weights | overly sharp decision boundaries |
| L1 | enforces sparsity | too many irrelevant features |
| Dropout | disrupts co-adaptation with stochastic masks | brittle internal representations |

### Practical tuning parameters

- •Keep probability p (or dropout rate q = 1 − p)
- •Which layers to apply it to
- •Interaction with BatchNorm (often reduce dropout if BatchNorm is present)

A common approach is to start with small dropout (e.g., q = 0.1–0.3 in dense layers) and increase only if overfitting persists after using weight decay and data augmentation.

## Application/Connection: Using Regularization in Real Training Loops

### Regularization is a design choice, not an afterthought

A practical workflow is:

1) Pick an architecture capable of fitting the task.

2) Use monitoring: training vs validation curves.

3) Add regularization to address observed gaps.

If training and validation losses are both high → underfitting: reduce regularization or increase capacity.

If training loss is low but validation loss is high → overfitting: increase regularization.

### How to choose among L2, L1, and dropout

Think in terms of what kind of “simplicity” you want:

- •Want **smooth shrinkage** and stable optimization? Use L2 / weight decay.
- •Want **feature selection / sparsity**? Use L1 (or elastic net).
- •Want **robust representations** in dense nets? Use dropout.

Often you combine them:

- •L2 + dropout is common.
- •L1 + L2 (elastic net) is common for linear models.

### Interactions with optimization

Regularization changes gradients and thus training dynamics.

- •With SGD + momentum: L2 is straightforward and often very effective.
- •With Adam: prefer AdamW (decoupled weight decay) if your goal is true weight decay behavior.

### Interactions with data augmentation and early stopping

Regularization is part of a larger family of generalization controls:

- •**Data augmentation** increases effective dataset size (regularizes by invariances).
- •**Early stopping** regularizes by limiting how far parameters move toward a potentially overfit minimum.

You’ll often see these combined:

| Tool | What it controls | Notes |
| --- | --- | --- |
| Weight decay | parameter magnitude | cheap, widely applicable |
| Dropout | internal co-adaptation | helps more in dense parts |
| Data augmentation | invariance & sample diversity | often the biggest win in vision |
| Early stopping | effective capacity via training time | requires validation monitoring |

### A concrete mental model for λ

λ is not “a little extra term.” It is a knob that sets the *relative scale* between fitting the data and shrinking complexity.

If the loss term is scaled (e.g., average vs sum over batch), the same numeric λ can behave differently.

So when you tune λ, do it in context:

- •batch size,
- •loss reduction (mean vs sum),
- •learning rate,
- •optimizer.

### Regularization and deep learning readiness

Deep learning systems are powerful partly because they can fit almost anything—so they will happily fit the wrong thing unless you apply constraints.

Understanding regularization prepares you for:

- •training deeper networks without collapse into overfit solutions,
- •using modern optimizers (AdamW),
- •selecting architectural components (dropout placement),
- •diagnosing generalization failures systematically.

This is why regularization is a core “unlock” for the broader [Deep Learning](/tech-tree/deep-learning/) node: it turns raw capacity into reliable performance.

## Worked Examples (3)

### L2 Regularization Changes the Gradient (and Causes Weight Decay)

Assume a model with parameter vector **w** and training objective J\_train(**w**). We define the regularized objective:

J(**w**) = J\_train(**w**) + λ‖**w**‖₂²

We want to derive the SGD update and interpret it as weight decay.

1. Start with the penalty term:

   Ω(**w**) = ‖**w**‖₂² = ∑ⱼ wⱼ²
2. Differentiate coordinate-wise:

   ∂Ω/∂wⱼ = 2wⱼ

   So ∇Ω(**w**) = 2**w**
3. Differentiate the full objective:

   ∇J(**w**) = ∇J\_train(**w**) + λ∇Ω(**w**)

   = ∇J\_train(**w**) + 2λ**w**
4. Write the SGD step with learning rate η:

   **w** ← **w** − η(∇J\_train(**w**) + 2λ**w**)
5. Rearrange to expose decay:

   **w** ← **w** − η∇J\_train(**w**) − 2ηλ**w**

   **w** ← (1 − 2ηλ)**w** − η∇J\_train(**w**)

**Insight:** The factor (1 − 2ηλ) multiplies the current weights every step, shrinking them toward 0 even if the data gradient were zero. This is why L2 is called weight decay: it continuously damps parameter magnitude, which tends to reduce variance and improve generalization.

### Why L1 Produces Exact Zeros (Constant Pull Toward 0)

Consider the regularized objective:

J(**w**) = J\_train(**w**) + λ‖**w**‖₁

We’ll examine the (sub)gradient contributed by the L1 term and compare it to L2.

1. Write the L1 norm:

   ‖**w**‖₁ = ∑ⱼ |wⱼ|
2. For one coordinate wⱼ, the derivative of |wⱼ| is not defined at 0, so use a subgradient:

   ∂|wⱼ|/∂wⱼ =

   +1 if wⱼ > 0

   −1 if wⱼ < 0

   any value in [−1, +1] if wⱼ = 0
3. Thus a valid subgradient of the full L1 norm is:

   ∂‖**w**‖₁/∂wⱼ = sign(wⱼ), where sign(0) ∈ [−1, +1]
4. Gradient-style update (conceptually):

   **w** ← **w** − η(∇J\_train(**w**) + λ·sign(**w**))
5. Compare with L2’s contribution (2λ**w**):

   - •L2 pull shrinks as wⱼ → 0
   - •L1 pull stays roughly constant magnitude λ until the weight hits 0

**Insight:** Because L1 applies a constant-magnitude force toward 0, small weights don’t get “protected” the way they do under L2. They are driven to exactly 0, yielding sparsity (feature selection).

### Dropout Keeps the Expected Activation the Same (Inverted Dropout)

Let **h** be a layer’s activation vector during training. We apply inverted dropout with keep probability p. We want to show E[**h̃**] = **h**.

1. Sample a Bernoulli mask **m** with independent entries:

   mⱼ ∼ Bernoulli(p)
2. Apply inverted dropout:

   **h̃** = (**m** ⊙ **h**) / p
3. Take expectation coordinate-wise:

   h̃ⱼ = (mⱼ hⱼ)/p

   E[h̃ⱼ] = E[mⱼ]·hⱼ/p
4. Use E[mⱼ] = p for a Bernoulli(p):

   E[h̃ⱼ] = p·hⱼ/p = hⱼ
5. Therefore E[**h̃**] = **h**

**Insight:** Inverted dropout preserves the mean activation during training, so at inference you can turn dropout off without additional scaling. The regularization comes from the randomness (variance), not from a shifted mean.

## Key Takeaways

- ✓

  Regularization is best thought of as optimizing a modified objective: J(θ) = J\_train(θ) + λ·Ω(θ), where Ω encodes a preference for simpler solutions.
- ✓

  L2 regularization uses Ω(**w**) = ‖**w**‖₂² and adds gradient 2λ**w**, producing weight decay: **w** ← (1 − 2ηλ)**w** − η∇J\_train(**w**).
- ✓

  L2 typically yields many small weights (smooth shrinkage) and often improves stability and generalization in deep nets.
- ✓

  L1 regularization uses Ω(**w**) = ‖**w**‖₁ and has a sign-based (sub)gradient; its constant pull toward 0 tends to create exact zeros (sparsity).
- ✓

  Geometrically, L1 constraints have corners that encourage axis-aligned (sparse) solutions; L2 constraints are round and rarely produce exact zeros.
- ✓

  Dropout regularizes by randomly masking units/activations during training, reducing co-adaptation and approximating an ensemble of thinned networks.
- ✓

  λ is a true tradeoff parameter; its effective strength depends on loss scaling, batch size, learning rate, and optimizer choice (especially Adam vs AdamW).

## Common Mistakes

- ✗

  Treating λ as universal: the same numeric λ can behave very differently when you change batch size, loss reduction (mean vs sum), or learning rate.
- ✗

  Applying dropout everywhere (especially early convolutional layers) without checking if it hurts representation learning; dropout placement matters.
- ✗

  Assuming “L2 regularization” equals “weight decay” under all optimizers—under Adam, decoupled weight decay (AdamW) is often the intended behavior.
- ✗

  Regularizing all parameters indiscriminately (e.g., including BatchNorm parameters or biases) without verifying whether that helps; sometimes it degrades training.

## Practice

easy

You are training with SGD and L2 regularization. Suppose η = 0.1 and λ = 0.01. Ignoring the data gradient (assume ∇J\_train(**w**) = **0** for this step), what happens to **w** after one update? Write the multiplicative factor applied to **w**.

**Hint:** Use **w** ← (1 − 2ηλ)**w** when the data gradient is zero.

Show solution

With L2: **w** ← **w** − η(2λ**w**) = (1 − 2ηλ)**w**.

Compute 2ηλ = 2·0.1·0.01 = 0.002.

So **w** is multiplied by (1 − 0.002) = 0.998 after one step.

medium

Explain, using the constrained-optimization geometry, why L1 regularization tends to produce sparse solutions while L2 does not. Focus on the shape of the constraint sets in 2D and where smooth loss contours typically touch them.

**Hint:** Compare the L1 ball (diamond) vs the L2 ball (circle) and think about corners vs smooth boundaries.

Show solution

In 2D, the constraint ‖**w**‖₁ ≤ c is a diamond with sharp corners on the axes, while ‖**w**‖₂² ≤ c is a circle with a smooth boundary. A smooth loss contour (e.g., an ellipse) expanded outward from its minimum will typically first touch the feasible set at a point of tangency. Because the L1 feasible set has corners, tangency often occurs at a corner, which lies on an axis, implying one coordinate is exactly 0 (sparsity). The L2 feasible set is round, so tangency usually happens at a point with both coordinates nonzero, producing shrinkage but not exact zeros.

medium

You apply inverted dropout to an activation h with keep probability p. Let h = 3 (a scalar activation). Compute the distribution of h̃ and verify E[h̃] = 3 for p = 0.6.

**Hint:** With probability p you keep the unit and scale by 1/p; otherwise it becomes 0.

Show solution

Mask m ∼ Bernoulli(p) with p = 0.6. Inverted dropout gives h̃ = (m·h)/p.

So:

- •with probability 0.6: m = 1 ⇒ h̃ = 3/0.6 = 5
- •with probability 0.4: m = 0 ⇒ h̃ = 0

Expectation:

E[h̃] = 0.6·5 + 0.4·0 = 3

So E[h̃] = 3, matching the original activation.

## Connections

Next steps and related nodes:

- •[Deep Learning](/tech-tree/deep-learning/): regularization becomes more important as depth and capacity increase; you’ll combine weight decay, dropout-like methods, augmentation, and early stopping.

Related concepts you may want nearby in the tech tree:

- •[Optimization & Gradient Descent](/tech-tree/gradient-descent/): regularization changes gradients and interacts with learning rate.
- •[Bias–Variance Tradeoff](/tech-tree/bias-variance/): a classic lens for why regularization helps.
- •[Data Augmentation](/tech-tree/data-augmentation/): another major regularization family that complements L2/dropout.
- •[Early Stopping](/tech-tree/early-stopping/): an implicit regularizer via training time.

Quality: A (4.2/5)

[← back to tree](/tech-tree/)[browse all →](/tech-tree/inventory/)
