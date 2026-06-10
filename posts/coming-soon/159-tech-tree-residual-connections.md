---
title: Residual (Skip) Connections
description: Architecture pattern that adds the input of a layer to its output to enable training of very deep networks and ease gradient flow; understand the motivation, basic implementation, and effect on optimization. Residual connections are a structural backbone of Transformer layers.
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
permalink: /tech-tree/residual-connections/
---

[←Back to Tech Tree](/tech-tree/)

[inventory](/tech-tree/inventory/)[coverage](/tech-tree/coverage/)

# Residual (Skip) Connections

Machine LearningDifficulty: ★★★☆☆Depth: 0Unlocks: 1

Architecture pattern that adds the input of a layer to its output to enable training of very deep networks and ease gradient flow; understand the motivation, basic implementation, and effect on optimization. Residual connections are a structural backbone of Transformer layers.

## Interactive Visualization

⏮◀◀▶▶STEP0.25x1xZOOM

t=0s

## Core Concepts

- -Identity shortcut: add a layer's input to its output (elementwise)
- -Residual mapping F(x): the block learns the difference from the input rather than the full mapping
- -Optimization benefit: enables training much deeper networks by improving gradient flow and making identity solutions easy

## Key Symbols & Notation

x, F(x), and + (elementwise addition)

## Essential Relationships

- -Output relation: output = F(x) + x, where the identity term x provides a direct gradient path to earlier layers

## Unlocks (1)

[Transformerslvl 5](/tech-tree/transformers/)

Advanced Learning Details

### Graph Position

5

Depth Cost

1

Fan-Out (ROI)

1

Bottleneck Score

0

Chain Length

### Cognitive Load

5

Atomic Elements

32

Total Elements

L1

Percentile Level

L3

Atomic Level

### All Concepts (13)

- - skip (residual) connection: routing a layer's input around the layer and adding it to the layer's output
- - residual block: a local pattern combining one or more layers that produce F(x) and an identity shortcut that adds x
- - residual function F(x): the function computed by the layer(s) inside a residual block that models change from input
- - identity (shortcut) mapping: the unchanged input passed forward and added to the layer output
- - projection (shortcut) for dimension mismatch: a learned linear projection (e.g., W\_s x) applied to x when shapes differ
- - element-wise addition as the merge operation for shortcut + layer output
- - residual parameterization view: the network learns H(x) by learning F(x) where H(x)=F(x)+x (learn residuals, not full mapping)
- - residual initialization/zero-residual intuition: if F is zero (or near zero) the block implements identity, making deep nets easier to initialize and train
- - forward signal preservation: residuals keep input information available to deeper layers
- - backward gradient bypass: residuals provide direct gradient paths that ease gradient propagation
- - effect on optimization: residuals reduce difficulty of training very deep networks by turning learning into small perturbations around identity
- - pre-activation vs post-activation residual block variants (ordering of normalization/activation relative to the addition)
- - Add & Norm pattern in Transformers: each sublayer's output is added to its input then normalized (x + Sublayer(x) followed by LayerNorm)

### Teaching Strategy

Self-serve tutorial - low prerequisites, straightforward concepts.

Deep networks can be powerful, but they’re often hard to train: as you stack more layers, optimization can stall or become unstable. Residual (skip) connections fix a surprisingly big part of this with a tiny structural change: let information (and gradients) flow around a layer by adding the input back to the output.

TL;DR:

A residual block outputs y = x + F(x). Instead of forcing a stack of layers to learn a full mapping H(x), you let it learn a residual F(x) = H(x) − x. This makes the identity mapping easy to represent, improves gradient flow, and enables training much deeper networks. Residual connections are core to modern architectures, including Transformers (via Add & Norm).

## What Is a Residual (Skip) Connection?

### The problem it addresses

When you build a deep neural network, you typically compose many transformations:

- •input **x** goes through layer 1 → output
- •then through layer 2 → output
- •… repeated dozens or hundreds of times

In principle, deeper networks can represent more complex functions. In practice, very deep stacks can become **hard to optimize**: training loss stops improving, gradients become unhelpful, and the model struggles to learn even “simple” behaviors.

Residual (skip) connections are a structural pattern designed to make deep stacks trainable.

### The core definition

A residual connection means a layer (or block) computes:

- •**Residual block output**:

**y** = **x** + **F(x)**

where:

- •**x** is the block input (a vector or tensor)
- •**F(x)** is a learned transformation (often several layers)
- •“+” is **elementwise addition** (so shapes must match)

This is why it’s also called a **skip connection**: **x** “skips” around the transform **F** and is added back in.

### Intuition: “don’t overwrite—edit”

Without a residual connection, a block must output **H(x)** directly:

- •plain block: **y** = **H(x)**

With residual connections, the block outputs:

- •residual block: **y** = **x** + **F(x)**

So the block isn’t forced to generate the whole signal from scratch. It can instead learn an *edit* to the input.

If the best thing to do is “do nothing,” the residual block can set **F(x) ≈ 0**, giving **y ≈ x**. That “identity solution” turns out to be extremely helpful for optimization.

### Residual mapping viewpoint

You can rewrite the residual form as:

- •want: **H(x)**
- •learn: **F(x) = H(x) − x**
- •output: **x + F(x) = x + (H(x) − x) = H(x)**

The representational power is not reduced—**H** can still be learned—but the parameterization makes certain useful functions (especially identity) much easier to reach during training.

### Where you’ll see it

Residual connections show up in many places:

- •ResNet-style CNN blocks (where the term became famous)
- •MLP blocks in deep feedforward nets
- •**Transformer layers**, where each sublayer is wrapped with “Add” (residual) and then “Norm” (LayerNorm)

In Transformers, you’ll repeatedly see patterns like:

- •**y** = **x** + Sublayer(**x**)

That single plus sign is a big part of why very deep Transformer stacks can train at all.

## Core Mechanic 1: Identity Shortcuts and Gradient Flow

### Why gradient flow matters

Training uses gradient-based optimization. If the gradient of the loss with respect to early layers becomes extremely small or chaotic, learning stalls.

Residual connections help by providing a **direct path** from later layers back to earlier layers.

### A minimal gradient derivation (scalar intuition)

To see the key idea without getting lost in tensor notation, consider a single residual block with scalar input x:

- •y = x + F(x)

Let L be the loss depending on y. By the chain rule:

∂L/∂x = ∂L/∂y · ∂y/∂x

Now compute ∂y/∂x:

y = x + F(x)

∂y/∂x = 1 + ∂F/∂x

So:

∂L/∂x = ∂L/∂y · (1 + ∂F/∂x)

The critical term is the **“1”** coming from the skip connection.

- •In a plain block y = F(x), you’d have ∂y/∂x = ∂F/∂x.
- •In a residual block, you always have a baseline pathway with derivative 1.

This doesn’t magically eliminate vanishing/exploding gradients in every setting, but it **adds a stable component** to gradient propagation.

### Vector/tensor form (same idea)

Let **x** ∈ ℝᵈ, and **F** maps ℝᵈ → ℝᵈ. Then:

**y** = **x** + **F(x)**

The Jacobian is:

∂**y**/∂**x** = **I** + ∂**F**/∂**x**

So the gradient to earlier layers includes an identity term **I**. Across many stacked blocks, this means there exists a path where the gradient multiplies by (approximately) identity instead of repeatedly multiplying by potentially small/large Jacobians.

### Composition across many layers

Consider a deep stack of residual blocks:

**x₀** = input

For k = 0…N−1:

**xₖ₊₁** = **xₖ** + **Fₖ(xₖ)**

If all **Fₖ** are near 0 early in training, then:

**xₖ₊₁ ≈ xₖ**

So the entire deep network initially behaves close to the identity mapping—meaning signals don’t get destroyed just because you made the network deep.

This is one of the most important practical effects:

- •**Depth becomes less risky**.

You can add more layers to gain capacity, and training remains feasible because the network can default to “almost identity” until each block learns useful residual corrections.

### Residual connections as an optimization “safety net”

A helpful mental model:

- •Plain deep network: each layer must get things right, because any mistake compounds.
- •Residual deep network: each layer can make small improvements, because the baseline is to pass information through.

This shifts the optimization landscape toward something easier to navigate.

### A quick comparison table

| Property | Plain stack (no skip) | Residual stack |
| --- | --- | --- |
| Block form | **y** = **F(x)** | **y** = **x** + **F(x)** |
| Identity mapping | Must be learned by parameters | Achieved by **F(x) = 0** |
| Gradient term | ∂**F**/∂**x** | **I** + ∂**F**/∂**x** |
| Deep behavior early in training | Can distort signals | Often close to identity |
| Practical depth | Limited | Much larger |

Residual connections don’t replace good initialization, normalization, and learning-rate choices—but they make deep learning dramatically more robust.

## Core Mechanic 2: Residual Mapping F(x) Learns “the Difference”

### Why learn a difference instead of the whole function?

Suppose the function you ultimately want is **H(x)**. In many deep models, especially when stacking many similar blocks, **H(x)** may be close to **x** much of the time.

Examples of “close to identity” needs:

- •A block might refine features slightly rather than rewrite them.
- •A Transformer layer might adjust token representations based on context, but preserve much of the original embedding.

If **H(x) ≈ x**, then the difference **H(x) − x** is small.

Residual blocks make the model explicitly represent that difference:

**F(x) = H(x) − x**

This can be easier to learn because:

1. 1)Small corrections can be represented with small weights.
2. 2)Many blocks can each contribute a modest update.
3. 3)If a block is not needed, it can “opt out” by learning **F(x) ≈ 0**.

### The “easy identity” argument, with a bit more structure

Imagine a block **F** is implemented as a small network, like:

**F(x)** = W₂ σ(W₁ **x**)

If you want the overall mapping to be identity (**y = x**), then in a plain network you would need:

W₂ σ(W₁ **x**) = **x**

That’s a strong constraint; depending on σ, it might be awkward or require special parameter values.

In a residual network, identity is just:

**y** = **x** + W₂ σ(W₁ **x**) = **x**

which is achieved whenever:

W₂ σ(W₁ **x**) = **0**

A sufficient condition is simply:

W₂ = 0 (or very small)

This shows why “do nothing” is naturally available to the model.

### Residual blocks as incremental updates (an optimization lens)

Rearrange the residual update:

**xₖ₊₁** = **xₖ** + **Fₖ(xₖ)**

This looks like an iterative refinement method:

- •start with **x₀**
- •repeatedly add updates

If you squint, it resembles a discretized dynamical system:

**xₖ₊₁ − xₖ** = **Fₖ(xₖ)**

This perspective helps explain why very deep residual networks behave like many small steps rather than a few huge jumps.

### Implementation details that matter

Residual connections are conceptually simple, but practical implementations need two details:

#### 1) Shape matching

Elementwise addition requires the same shape:

- •**x** and **F(x)** must have identical dimensions.

If shapes differ, common strategies include:

- •**Projection shortcut**: apply a linear map P to **x**, then add:

**y** = P(**x**) + **F(x)**

- •In CNNs, P is often a 1×1 convolution.
- •In Transformers, dimensions are usually kept constant within a block, so plain addition works.

#### 2) Where normalization goes (important in Transformers)

In Transformer literature you’ll see:

- •Post-norm: **y** = LayerNorm(**x** + Sublayer(**x**))
- •Pre-norm: **y** = **x** + Sublayer(LayerNorm(**x**))

Both use residual addition; they differ in optimization behavior and stability for very deep stacks. The key idea for this node is the residual path itself: the “+ **x**” that preserves a direct route for information.

### Residual connections are not (just) “more capacity”

It’s tempting to think residual connections add representational power. But the main win is **reparameterization**:

- •They change how the same function class is reached during training.

That’s why residual connections are discussed primarily as an **optimization** technique—even though they also interact with generalization and training dynamics in interesting ways.

## Application/Connection: Residuals in Transformer Layers (Add & Norm)

### Why Transformers lean on residual connections

A Transformer layer has multiple complex subcomponents:

- •multi-head self-attention
- •a position-wise feedforward network (MLP)
- •normalization and dropout

Training would be much harder if each layer had to fully rewrite token representations. Residual connections make each sublayer behave like a controlled update to the current representation.

### Canonical Transformer sublayer pattern

For a token representation vector **x** (really a matrix of token vectors), a typical sublayer wrapper is:

**y** = **x** + Sublayer(**x**)

Then normalization is applied either before or after depending on design.

A simplified (pre-norm) Transformer block looks like:

1) Attention sublayer

**x₁** = **x** + Attention(LayerNorm(**x**))

2) MLP sublayer

**x₂** = **x₁** + MLP(LayerNorm(**x₁**))

Each residual addition means:

- •the model can preserve **x** if the sublayer output is small
- •gradients can flow along the skip pathway
- •each sublayer learns an increment rather than a rewrite

### Interpreting attention as a residual update

Self-attention produces context-aware mixtures of token information. But residual addition ensures:

- •the original token features remain available
- •attention contributes “context corrections” instead of replacing the representation

This is especially important early in training, when attention weights may be noisy.

### Practical effects you can observe

In real training runs, residual connections often enable:

- •deeper models without catastrophic optimization failure
- •faster convergence (fewer epochs/steps to reach a given loss)
- •better final performance due to the ability to scale depth

Residuals are not sufficient alone—Transformers also rely heavily on normalization, learning-rate schedules, and careful initialization. But the skip connection is a structural backbone.

### When residual connections can be tricky

Residuals are usually beneficial, but you still must manage:

- •**scale**: if ‖**F(x)**‖ is too large, the residual update can destabilize activations
- •**shape**: addition demands matching dimensions
- •**interaction with normalization**: pre-norm vs post-norm impacts stability

A common engineering tactic is to ensure the residual branch starts small (e.g., initialization choices), so early training behaves close to identity and gradually learns stronger updates.

### Big picture connection

Residual connections are a pattern you’ll see across architectures because they solve a general problem:

- •how to compose many learned transformations while keeping optimization stable.

Transformers are one of the most important modern examples, but the core math is the same: **y = x + F(x)**.

## Worked Examples (3)

### Example 1: Residual vs plain block—compute gradients (scalar case)

Let F(x) = a·x (a is a scalar parameter). Compare a plain block y = F(x) to a residual block y = x + F(x). Suppose the loss is L = ½·(y − t)² for target t. Compute ∂L/∂x for both cases.

1. Plain block:

   y = F(x) = a·x

   L = ½·(a·x − t)²
2. Compute ∂L/∂y:

   ∂L/∂y = (y − t)
3. Compute ∂y/∂x:

   y = a·x ⇒ ∂y/∂x = a
4. Chain rule:

   ∂L/∂x = ∂L/∂y · ∂y/∂x

   = (y − t) · a

   = (a·x − t) · a
5. Residual block:

   y = x + F(x) = x + a·x = (1 + a)·x

   L = ½·((1 + a)·x − t)²
6. Compute ∂y/∂x:

   y = (1 + a)·x ⇒ ∂y/∂x = (1 + a)

   (Equivalently: y = x + a·x ⇒ ∂y/∂x = 1 + a.)
7. Chain rule:

   ∂L/∂x = (y − t) · (1 + a)

   = (((1 + a)·x) − t) · (1 + a)

**Insight:** In the plain case, the backprop multiplier is a. If a is small, gradients shrink. In the residual case, the multiplier is (1 + a), which includes a built-in 1 from the skip path—making it harder for gradients to vanish purely because the learned transform is weak early in training.

### Example 2: Residual mapping view—convert between H(x) and F(x)

Assume the desired function is H(x) = 3x + 2 (scalar). If we implement a residual block y = x + F(x), what residual function F(x) must be learned? Verify that the residual formulation reproduces H(x).

1. Start from the relationship:

   H(x) = x + F(x)

   So:

   F(x) = H(x) − x
2. Plug in H(x) = 3x + 2:

   F(x) = (3x + 2) − x

   = 2x + 2
3. Verify by substitution:

   y = x + F(x)

   = x + (2x + 2)

   = 3x + 2

   = H(x)

**Insight:** Residual learning doesn’t restrict what you can represent; it changes what the block is asked to model. If H(x) is close to x, then F(x) is small—often easier to learn robustly with gradient-based optimization.

### Example 3: Shape matching—when you need a projection shortcut

Let **x** ∈ ℝ³, but suppose your transform produces **F(x)** ∈ ℝ² (e.g., you changed hidden size). You cannot add **x** + **F(x)** directly. Show how a projection P fixes this, and write the new residual form.

1. Problem: elementwise addition requires matching shapes.

   **x** ∈ ℝ³

   **F(x)** ∈ ℝ²

   So **x** + **F(x)** is undefined.
2. Introduce a learned projection P: ℝ³ → ℝ², often linear:

   P(**x**) = W **x** + **b**

   where W is 2×3 and **b** ∈ ℝ².
3. Define the residual output:

   **y** = P(**x**) + **F(x)**

   Now both terms are in ℝ², so the sum is valid.
4. Interpretation:

   - •the skip path still exists, but it now passes through a simple projection
   - •the main branch learns a correction in the new space

**Insight:** Residual connections fundamentally require an additive merge. If dimensions change, you can keep the residual idea by making the shortcut path match dimensions via a cheap projection.

## Key Takeaways

- ✓

  A residual (skip) connection outputs **y** = **x** + **F(x)** using elementwise addition.
- ✓

  Residual learning reframes the target mapping **H(x)** as a residual **F(x) = H(x) − x**, often making optimization easier.
- ✓

  The skip path contributes an identity term to backprop: ∂**y**/∂**x** = **I** + ∂**F**/∂**x**, improving gradient flow in deep stacks.
- ✓

  Residual blocks make the identity mapping easy: set **F(x) ≈ 0** ⇒ **y ≈ x**.
- ✓

  Deep residual stacks behave like iterative refinement: **xₖ₊₁ = xₖ + Fₖ(xₖ)** (many small updates).
- ✓

  Elementwise addition requires matching shapes; if dimensions differ, use a projection shortcut **y** = P(**x**) + **F(x)**.
- ✓

  Transformers rely on residual connections around attention and MLP sublayers (Add & Norm), enabling stable training at depth.

## Common Mistakes

- ✗

  Forgetting that “+” is elementwise: trying to add tensors with mismatched shapes without a projection shortcut.
- ✗

  Thinking residual connections mainly increase expressivity; their primary benefit is optimization via easier identity solutions and improved gradient flow.
- ✗

  Assuming residuals guarantee no vanishing/exploding gradients in any circumstance; they help a lot, but normalization, initialization, and learning rates still matter.
- ✗

  Mixing up where normalization happens in Transformers (pre-norm vs post-norm) and attributing all stability differences solely to the residual connection.

## Practice

easy

Let **x** ∈ ℝᵈ and a residual block be **y** = **x** + **F(x)**. Show (using Jacobians) that ∂**y**/∂**x** = **I** + ∂**F**/∂**x**.

**Hint:** Differentiate **y** componentwise: yᵢ = xᵢ + Fᵢ(**x**). What is ∂xᵢ/∂xⱼ?

Show solution

Write yᵢ = xᵢ + Fᵢ(**x**).

Then for each i, j:

∂yᵢ/∂xⱼ = ∂xᵢ/∂xⱼ + ∂Fᵢ/∂xⱼ

But ∂xᵢ/∂xⱼ = 1 if i = j, else 0, which is exactly the identity matrix **I**.

So the Jacobian is:

∂**y**/∂**x** = **I** + ∂**F**/∂**x**.

medium

Suppose a deep network is a stack of N residual blocks: **xₖ₊₁ = xₖ + Fₖ(xₖ)**. If all Fₖ are exactly 0, what function does the whole network compute? What does this imply about adding more layers?

**Hint:** If Fₖ = 0, then xₖ₊₁ = xₖ. Unroll the recurrence.

Show solution

If Fₖ ≡ 0 for every k, then:

**x₁ = x₀ + 0 = x₀**

**x₂ = x₁ + 0 = x₁ = x₀**

...

**x\_N = x₀**

So the whole network computes the identity function.

Implication: adding layers does not force the network to change behavior; the model can default to identity and only learn nonzero residuals where useful. This makes very deep architectures easier to optimize.

hard

You have a residual block where **x** ∈ ℝ⁶, but the transform produces **F(x)** ∈ ℝ⁴. Propose two ways to make a valid residual connection, and write the resulting equations.

**Hint:** Either change the transform to output ℝ⁶, or project the skip path into ℝ⁴ (or project the transform into ℝ⁶).

Show solution

Two valid approaches:

1) Keep the skip path unchanged and make the transform match ℝ⁶:

- •Redesign **F** so that **F(x)** ∈ ℝ⁶.
- •Then: **y** = **x** + **F(x)**.

2) Use a projection shortcut from ℝ⁶ → ℝ⁴:

- •Define P(**x**) = W **x** + **b**, with W ∈ ℝ⁴×⁶.
- •Then: **y** = P(**x**) + **F(x)**, where both terms are in ℝ⁴.

(Variants: you could also project **F(x)** up to ℝ⁶ and add to **x**, but typically you project the shortcut when changing widths.)

## Connections

[Transformers](/tech-tree/transformers/)

Related next nodes you’ll often want after this:

- •[Layer Normalization](/tech-tree/layer-normalization/)
- •[Backpropagation](/tech-tree/backpropagation/)
- •[Vanishing and Exploding Gradients](/tech-tree/vanishing-exploding-gradients/)

Quality: A (4.4/5)

[← back to tree](/tech-tree/)[browse all →](/tech-tree/inventory/)
