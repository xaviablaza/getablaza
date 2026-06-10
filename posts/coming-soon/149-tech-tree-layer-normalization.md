---
title: Layer Normalization
description: Normalizing activations for stable training. Batch norm, layer norm.
date: '2026-07-01'
scheduled: '2026-11-26'
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
inspiration_url: https://templeton.host/tech-tree/layer-normalization/
inspiration_category: tech-tree
---

> Source-copy draft imported from [https://templeton.host/tech-tree/layer-normalization/](https://templeton.host/tech-tree/layer-normalization/). Names, domain references, and local media paths were adapted for Xavi Ablaza / getablaza.com.

[←Back to Tech Tree](/tech-tree/)

[inventory](/tech-tree/inventory/)[coverage](/tech-tree/coverage/)

# Layer Normalization

Machine LearningDifficulty: ★★★★☆Depth: 11Unlocks: 1

Normalizing activations for stable training. Batch norm, layer norm.

## Interactive Visualization

⏮◀◀▶▶STEP0.25x1xZOOM

t=0s

## Core Concepts

- -Per-sample normalization across the layer's feature dimensions (statistics computed per example, not across the batch)
- -Normalize activations using mean and variance (subtract mean, divide by sqrt(variance + eps))
- -Apply learned affine parameters after normalization to retain representational flexibility

## Key Symbols & Notation

gamma (learned per-feature scale parameter)beta (learned per-feature shift parameter)

## Essential Relationships

- -output = gamma \* (input - mu) / sqrt(variance + eps) + beta - where mu and variance are computed over the features of the same sample

## Prerequisites (2)

[Neural Networks6 atoms](/tech-tree/neural-networks/)[Variance5 atoms](/tech-tree/variance/)

## Unlocks (1)

[Transformerslvl 5](/tech-tree/transformers/)

Advanced Learning Details

### Graph Position

142

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

25

Total Elements

L0

Percentile Level

L4

Atomic Level

### All Concepts (8)

- - Per-sample (feature-wise) normalization: compute normalization statistics across the features/hidden units of a single example (not across the batch).
- - Computation pipeline of LayerNorm as a sequence of steps: compute per-sample mean, compute per-sample variance, normalize each activation, then apply an affine transform.
- - Learnable affine transform after normalization: per-feature scale (γ) and shift (β) parameters that are trained with the model.
- - Numerical-stability constant (ε) used inside the denominator to avoid division by zero when normalizing.
- - LayerNorm operator: a functional unit (often written LayerNorm(x; γ, β) or LN(x)) that maps an activation vector to a normalized-and-affine-transformed output.
- - Per-feature parameters: γ and β are vectors whose length equals the number of features (not global scalars), i.e., scaling/shift is done per hidden unit.
- - Batch-size independence: because statistics are computed per sample, LayerNorm's behavior does not depend on the minibatch size and works with batch size = 1 or variable sizes.
- - Typical use-cases and advantages: suitable for RNNs and architectures (e.g., Transformers) where batch statistics are impractical; it stabilizes and speeds training by making layer inputs have controlled mean/variance.

### Teaching Strategy

Multi-session curriculum - substantial prior knowledge and complex material. Use mastery gates and deliberate practice.

Deep nets don’t usually fail because they can’t represent a function—they fail because training becomes numerically and statistically unstable. Layer Normalization is a simple, per-example stabilizer: it keeps activations in a predictable range without depending on batch statistics, which is exactly why it became a default building block for Transformers.

TL;DR:

Layer Normalization (LayerNorm) normalizes each example’s activation vector across its feature dimensions: subtract the per-example mean and divide by the per-example standard deviation (with ε for safety), then apply learned per-feature scale γ and shift β. Unlike BatchNorm, it does not use batch statistics, so it works well with small batches, variable sequence lengths, and autoregressive inference.

## What Is Layer Normalization?

### The problem it solves (why before how)

Training a deep network means repeatedly composing nonlinear layers. Even if each layer is “reasonable,” their composition can drift into regimes where:

- •activations become very large or very small (numerical issues, saturation),
- •gradients become ill-conditioned (harder optimization),
- •different features in a layer live on very different scales (some features dominate updates),
- •training behavior changes when batch size changes.

Normalization layers attack these issues by **standardizing** activations so that the next computation sees inputs with a stable distribution.

Batch Normalization (BatchNorm) does this by computing statistics over the batch. That can be powerful, but it also means:

- •behavior depends on batch size,
- •training and inference behave differently (moving averages),
- •it’s awkward for variable-length sequences and autoregressive decoding,
- •it can be unstable for very small or micro-batches.

Layer Normalization (LayerNorm) is the alternative that makes normalization **per example**.

### Intuition: “normalize the vector you have, not the batch you wish you had”

Take one training example flowing through a layer. At some point you have a feature vector **x** (for a single token, or a single hidden state, or a single fully-connected layer output). LayerNorm treats that vector as the object to normalize.

For an activation vector **x** ∈ ℝᵈ (d features), LayerNorm computes:

- •the mean across features (within that one example),
- •the variance across features (within that one example),
- •uses those to standardize each feature,
- •then restores flexibility by applying learned scale and shift.

### The core definition

Let **x** = (x₁, x₂, …, x\_d) be one example’s activation vector.

Per-example mean:

μ = (1/d) ∑ᵢ xᵢ

Per-example variance:

σ² = (1/d) ∑ᵢ (xᵢ − μ)²

Normalized activations:

x̂ᵢ = (xᵢ − μ) / √(σ² + ε)

Then an affine transform (learned per-feature):

yᵢ = γᵢ x̂ᵢ + βᵢ

Where:

- •γ (gamma) is a learned scale vector in ℝᵈ
- •β (beta) is a learned shift vector in ℝᵈ
- •ε is a small constant (e.g. 1e−5) to avoid division by 0

### What it guarantees (and what it doesn’t)

If γ = 1 and β = 0, then for each example, the normalized vector x̂ has:

- •mean ≈ 0 across features
- •variance ≈ 1 across features

But LayerNorm **does not** make the distribution across the batch standardized, and it **does not** guarantee anything about each individual feature across the dataset. It’s “within-vector” normalization, not “within-feature-across-batch” normalization.

### Where it’s applied

LayerNorm is used in:

- •Transformers (almost always)
- •RNNs / LSTMs (often)
- •MLP blocks in many modern architectures

A typical Transformer block normalizes hidden vectors of shape (batch, seq, d\_model) across the last dimension d\_model.

That last detail matters: **LayerNorm normalizes across the feature dimension(s) you choose**, usually the hidden size.

## Core Mechanic 1: Per-sample mean/variance normalization across features

### What exactly is being normalized?

Suppose you have a mini-batch of hidden states:

X ∈ ℝ^(B × d)

Row b is one example:

**x**^(b) ∈ ℝᵈ

LayerNorm computes statistics separately for each b.

For each example b:

μ^(b) = (1/d) ∑ᵢ xᵢ^(b)

σ²^(b) = (1/d) ∑ᵢ (xᵢ^(b) − μ^(b))²

Then:

x̂ᵢ^(b) = (xᵢ^(b) − μ^(b)) / √(σ²^(b) + ε)

### Why normalize across features?

Think of a single layer output as a “feature descriptor” of the current example. If the overall magnitude and offset of that descriptor drift, subsequent layers must continuously re-adapt their weights to changing input scales.

LayerNorm reduces that burden by keeping each example’s feature vector in a normalized range.

A useful geometric view:

- •Subtracting μ removes the component along the all-ones direction (centering).
- •Dividing by √(σ² + ε) rescales so the average squared deviation is ~1.

This makes optimization more stable because the next layer sees inputs that are less sensitive to upstream shifts.

### A careful note about variance definition

You may see variance computed with 1/d or 1/(d−1). In deep learning implementations, LayerNorm virtually always uses:

σ² = (1/d) ∑ᵢ (xᵢ − μ)²

This is not about unbiased estimation; it’s about a deterministic scaling that behaves consistently.

### Multi-dimensional LayerNorm (common in practice)

In NLP / Transformers, your tensor might be:

X ∈ ℝ^(B × T × d)

You apply LayerNorm over the last dimension d:

For each (b, t), treat **x**^(b,t) ∈ ℝᵈ and normalize across i = 1…d.

In vision, you might have:

X ∈ ℝ^(B × C × H × W)

Depending on the variant, you might normalize across channels C only, or across C×H×W. “LayerNorm” in its original sense typically normalizes across the feature dimensions of a layer’s output; in convnets, that notion can blur into GroupNorm / InstanceNorm.

### Numerical stability: why ε exists

If a vector’s features are all equal, then σ² = 0. Without ε you’d divide by 0.

More generally, if σ² is tiny, division can amplify noise. ε prevents extreme scaling:

√(σ² + ε) ≥ √ε

Typical ε values are 1e−5 or 1e−6.

### BatchNorm vs LayerNorm: a comparison table

BatchNorm and LayerNorm are often confused because the formulas look similar. The key difference is **which axes you average over**.

| Property | BatchNorm | LayerNorm |
| --- | --- | --- |
| Stats computed over | batch (and often spatial dims) | features within one example |
| Depends on batch size | yes | no |
| Training vs inference behavior | different (running stats) | same |
| Works well with tiny batches | often no | yes |
| Common in | CNNs, large-batch training | Transformers, RNNs, small/variable batch |
| Noise as regularization | yes (batch noise) | minimal |

### Subtle but important: LayerNorm is deterministic given the example

BatchNorm introduces stochasticity because batch composition changes. LayerNorm’s stats for an example depend only on that example.

This is one reason LayerNorm plays nicely with autoregressive Transformers: during inference you often have batch size 1. BatchNorm would either be undefined or require stored running averages; LayerNorm just works.

### What LayerNorm does to gradients (high-level)

You don’t need the full derivative to benefit from LayerNorm, but it helps to know what it changes:

- •It rescales gradients flowing into earlier layers because outputs are divided by √(σ² + ε).
- •It couples features: μ and σ² depend on all xᵢ, so each output yᵢ depends on all inputs xⱼ.

That coupling is intentional: the normalization is a property of the whole vector.

A conceptual takeaway:

- •Without normalization, one feature can explode and dominate the layer.
- •With LayerNorm, an exploding feature increases σ², which increases the denominator and dampens the standardized values.

Not a perfect “clamp,” but a stabilizing feedback.

## Core Mechanic 2: Learned affine parameters (γ, β) and representational flexibility

### Why normalize at all if it might remove useful information?

If we only output x̂, we force every example’s representation to be mean 0 and variance 1 across features. That sounds restrictive: what if a layer wants a particular feature to be systematically larger, or wants a nonzero mean for downstream computation?

This is why LayerNorm includes a learned per-feature affine transform:

**y** = γ ⊙ **x̂** + β

Where:

- •γ, β ∈ ℝᵈ
- •⊙ is elementwise multiplication

### The key idea: normalize for stability, then let the model “undo it” when beneficial

LayerNorm gives optimization stability, but γ and β let the network recover expressive power.

Two important facts:

1) If the best thing is “do nothing,” LayerNorm can learn that.

If γᵢ = √(σ² + ε) and βᵢ = μ (not exactly per-example, but conceptually), you can approximate reversing normalization. More practically: with learned γ and β, the network can set outputs to whatever scale and offset is useful.

2) γ can gate features.

If γᵢ becomes small, feature i’s normalized value contributes less. If γᵢ becomes large, that feature is amplified.

### Why γ and β are per-feature (not scalars)

A single scalar γ would rescale the whole vector uniformly. But different features often need different typical magnitudes.

Per-feature γ, β allow:

- •one feature dimension to carry “large” signals,
- •another to stay small and precise,
- •shifting individual dimensions to match the distribution expected by subsequent weights.

### Initialization choices

Common initializations:

- •γ initialized to 1 (so initial LayerNorm is close to pure normalization)
- •β initialized to 0

This makes the network start in a stable regime.

### Where LayerNorm sits relative to residual connections (Pre-LN vs Post-LN)

In Transformers, you’ll see two popular placements:

- •**Post-LN** (original Transformer):
- •sublayer output is added to residual, then LayerNorm
- •pattern: **h** ← LN(**h** + Sublayer(**h**))

- •**Pre-LN** (common modern variant):
- •LayerNorm before the sublayer, residual added after
- •pattern: **h** ← **h** + Sublayer(LN(**h**))

Why this matters:

- •Pre-LN often improves gradient flow in very deep Transformers.
- •Post-LN makes the residual path go through a normalization, which can sometimes make optimization trickier for depth.

Either way, LayerNorm is still doing the same per-example feature normalization; the placement changes training dynamics.

### A short derivation: verifying the normalized mean is 0 (when ε = 0)

Let x̂ᵢ = (xᵢ − μ)/σ with σ = √σ².

Compute mean across features:

(1/d) ∑ᵢ x̂ᵢ

= (1/d) ∑ᵢ (xᵢ − μ)/σ

= (1/σ) · (1/d) ∑ᵢ (xᵢ − μ)

= (1/σ) · ( (1/d) ∑ᵢ xᵢ − (1/d) ∑ᵢ μ )

= (1/σ) · ( μ − μ )

= 0

With ε > 0, the same algebra holds with σ = √(σ² + ε) (still a constant w.r.t. i), so the mean is still exactly 0.

### Another derivation: normalized variance is ~1 (ε complicates slightly)

Variance across features:

(1/d) ∑ᵢ x̂ᵢ²

= (1/d) ∑ᵢ (xᵢ − μ)² / (σ² + ε)

= (1/(σ² + ε)) · (1/d) ∑ᵢ (xᵢ − μ)²

= (1/(σ² + ε)) · σ²

= σ² / (σ² + ε)

So if ε is tiny compared to σ², this is close to 1.

This explains why ε slightly reduces the achieved variance when σ² is small, which is exactly what we want for stability.

### Practical shapes and parameter counts

If hidden size is d\_model, then:

- •γ has d\_model parameters
- •β has d\_model parameters

LayerNorm adds 2d\_model parameters per normalized vector space—usually negligible compared to attention/MLP weights.

### Summary intuition

- •Normalization improves conditioning.
- •γ and β prevent the normalization from becoming a representational bottleneck.
- •Placement (pre/post) affects optimization but not the mathematical definition of LayerNorm.

## Application/Connection: Why LayerNorm is central to Transformers (and when to choose BatchNorm vs LayerNorm)

### Transformers: why LayerNorm fits the setting

Transformers process sequences with variable lengths, and often train with:

- •small effective batches (due to memory limits),
- •gradient accumulation (micro-batches),
- •distributed setups where per-device batch is tiny,
- •autoregressive inference with batch size 1.

BatchNorm depends on stable batch statistics. In these settings, batch statistics are noisy or unusable.

LayerNorm, by contrast:

- •uses per-example stats (independent of batch size),
- •behaves identically in training and inference,
- •naturally applies to each token’s hidden state vector.

### Typical Transformer block usage

Let hidden states be **H** ∈ ℝ^(B × T × d).

A common (Pre-LN) block is:

1) **U** = LN(**H**)

2) **A** = Attention(**U**)

3) **H** ← **H** + Dropout(**A**)

4) **V** = LN(**H**)

5) **M** = MLP(**V**)

6) **H** ← **H** + Dropout(**M**)

LayerNorm is the “stabilizer” before each major transformation.

### BatchNorm vs LayerNorm: choosing in practice

A simplified rule of thumb:

| Scenario | Often best choice | Why |
| --- | --- | --- |
| CNNs with large batches | BatchNorm | exploits batch stats; strong performance historically |
| NLP / Transformers | LayerNorm | batch size often small; inference needs determinism |
| Very small batches / micro-batches | LayerNorm / GroupNorm | BatchNorm statistics become noisy |
| Autoregressive generation | LayerNorm | BatchNorm problematic with batch=1 |

### Important nuance: BatchNorm can act as regularization

BatchNorm’s batch-to-batch noise sometimes improves generalization.

LayerNorm is more “clean” and deterministic. If you lose that regularization benefit, you might rely more on:

- •dropout,
- •data augmentation,
- •weight decay,
- •stochastic depth.

### LayerNorm and optimization stability (connection to conditioning)

Consider a linear layer:

**z** = W **x** + **b**

If **x** varies wildly in magnitude, then gradients w.r.t. W scale with **x**:

∂L/∂W includes terms proportional to **x**

So controlling the scale of **x** can stabilize updates. LayerNorm indirectly limits the variability of scales seen by downstream layers, improving the optimizer’s job.

### When LayerNorm can be less ideal

LayerNorm is not universally best. Some considerations:

- •In convnets, normalizing across channels only (or groups) may better respect spatial structure.
- •In some reinforcement learning settings, normalization choices can interact with nonstationary data.
- •If you want batch-level noise benefits and have large batches, BatchNorm might still win.

### Implementation mental model (no code, just steps)

For each example (and token position if sequence):

1) compute μ over the chosen feature axes

2) compute σ² over the same axes

3) normalize: (**x** − μ)/√(σ² + ε)

4) scale/shift: γ ⊙ (…) + β

Because the computation is local to each example, it parallelizes well and doesn’t require synchronization across devices the way BatchNorm can.

### Connection forward: Transformers

Transformers rely on stable deep residual stacks of attention + MLP blocks. LayerNorm is one of the key pieces that makes those stacks trainable.

If you understand LayerNorm, you’re ready to reason about:

- •why “Pre-LN Transformers” train deeper,
- •why inference-time behavior is stable,
- •why normalization interacts with residual connections and learning rates.

## Worked Examples (3)

### Compute LayerNorm by hand on a 4D activation vector

You have one example with activation vector **x** ∈ ℝ⁴:

**x** = (2, 0, 4, 4)

Use ε = 0 for simplicity. Assume γ = (1, 1, 1, 1) and β = (0, 0, 0, 0). Compute x̂.

1. Compute the mean across features:

   μ = (1/4)(2 + 0 + 4 + 4)

   = (1/4)(10)

   = 2.5
2. Compute deviations from the mean:

   **x** − μ = (2 − 2.5, 0 − 2.5, 4 − 2.5, 4 − 2.5)

   = (−0.5, −2.5, 1.5, 1.5)
3. Compute variance:

   σ² = (1/4)[(−0.5)² + (−2.5)² + (1.5)² + (1.5)²]

   = (1/4)[0.25 + 6.25 + 2.25 + 2.25]

   = (1/4)(11)

   = 2.75
4. Compute standard deviation:

   σ = √(2.75)

   ≈ 1.6583
5. Normalize each component:

   x̂ = (1/σ)(**x** − μ)

   ≈ (1/1.6583)(−0.5, −2.5, 1.5, 1.5)

   ≈ (−0.3015, −1.5076, 0.9045, 0.9045)

**Insight:** LayerNorm turned a vector with mean 2.5 and variance 2.75 into a standardized vector with mean 0 and variance 1 (up to rounding). This happens per example, independent of any other examples in the batch.

### Effect of learned γ and β (restoring flexibility)

Continue from the previous example where:

x̂ ≈ (−0.3015, −1.5076, 0.9045, 0.9045)

Now use learned parameters:

γ = (2, 0.5, 1, 3)

β = (1, −1, 0, 0.5)

Compute **y** = γ ⊙ x̂ + β.

1. Apply elementwise scaling γ ⊙ x̂:

   γ ⊙ x̂ ≈ (2·(−0.3015), 0.5·(−1.5076), 1·0.9045, 3·0.9045)

   ≈ (−0.6030, −0.7538, 0.9045, 2.7135)
2. Add β elementwise:

   **y** ≈ (−0.6030 + 1,

   −0.7538 − 1,

   0.9045 + 0,

   2.7135 + 0.5)

   ≈ (0.3970, −1.7538, 0.9045, 3.2135)

**Insight:** Normalization stabilizes optimization, but γ and β let each feature dimension adopt the scale and offset that the network finds useful. In practice, γ and β are crucial—LayerNorm is not just standardization; it’s standardization plus learnable reparameterization.

### LayerNorm vs BatchNorm on a tiny batch (why batch dependence matters)

Consider a batch of B = 2 examples, each with d = 3 features:

**x**^(1) = (0, 0, 6)

**x**^(2) = (3, 3, 3)

Compare:

1) LayerNorm applied per example across features

2) BatchNorm-like normalization per feature across the batch (conceptual; ignoring running averages)

Use ε = 0 and no γ/β for simplicity.

1. LayerNorm on example 1:

   μ^(1) = (1/3)(0 + 0 + 6) = 2

   Deviations: (−2, −2, 4)

   σ²^(1) = (1/3)(4 + 4 + 16) = 8

   σ^(1) = √8 ≈ 2.828

   x̂^(1) ≈ (−0.707, −0.707, 1.414)
2. LayerNorm on example 2:

   μ^(2) = (1/3)(3 + 3 + 3) = 3

   Deviations: (0, 0, 0)

   σ²^(2) = 0 ⇒ σ^(2) = 0 (this is why ε is needed in practice)

   With ε > 0, x̂^(2) becomes (0, 0, 0).
3. BatchNorm-like per-feature stats across the batch:

   Feature 1 values: (0, 3) ⇒ mean = 1.5

   Feature 2 values: (0, 3) ⇒ mean = 1.5

   Feature 3 values: (6, 3) ⇒ mean = 4.5
4. Per-feature variance across the batch (using 1/B):

   Feature 1: (1/2)[(0−1.5)² + (3−1.5)²] = (1/2)(2.25 + 2.25) = 2.25

   Feature 2: same ⇒ 2.25

   Feature 3: (1/2)[(6−4.5)² + (3−4.5)²] = (1/2)(2.25 + 2.25) = 2.25
5. BatchNorm-like normalized outputs:

   Example 1: ((0−1.5)/1.5, (0−1.5)/1.5, (6−4.5)/1.5) = (−1, −1, 1)

   Example 2: ((3−1.5)/1.5, (3−1.5)/1.5, (3−4.5)/1.5) = (1, 1, −1)

**Insight:** With B = 2, BatchNorm-like statistics are extremely sensitive to which examples are paired. LayerNorm’s statistics don’t change if you shuffle batch composition; they’re per example. That invariance is a major reason LayerNorm is preferred in sequence models and small-batch regimes.

## Key Takeaways

- ✓

  LayerNorm normalizes activations **per example**, across the feature dimensions of a layer’s output.
- ✓

  The normalization step is: x̂ᵢ = (xᵢ − μ)/√(σ² + ε), with μ and σ² computed over features within the same example.
- ✓

  Learned γ (scale) and β (shift) are applied per feature: yᵢ = γᵢ x̂ᵢ + βᵢ, restoring representational flexibility.
- ✓

  Unlike BatchNorm, LayerNorm does not depend on batch size and behaves the same during training and inference.
- ✓

  ε is essential for numerical stability, especially when an example’s feature variance is near 0.
- ✓

  LayerNorm couples features because μ and σ² depend on all features; each output depends on the whole input vector.
- ✓

  Transformers heavily rely on LayerNorm (often Pre-LN) to stabilize deep residual stacks and enable reliable inference with batch size 1.

## Common Mistakes

- ✗

  Normalizing over the wrong axis (e.g., across the batch dimension instead of the feature dimension), which silently changes the algorithm into something else.
- ✗

  Forgetting ε or using an ε that is too small for low-variance activations, causing numerical blow-ups or NaNs.
- ✗

  Assuming LayerNorm provides the same regularization effect as BatchNorm; LayerNorm is largely deterministic and may require other regularizers.
- ✗

  Confusing γ/β with global scalars; in standard LayerNorm they are per-feature vectors, not single numbers.

## Practice

easy

Given **x** = (1, 2, 3, 4) with ε = 0, compute the LayerNorm normalized vector x̂ (no γ/β).

**Hint:** Compute μ, then σ² = (1/4)∑(xᵢ−μ)², then divide deviations by √σ².

Show solution

μ = (1/4)(1+2+3+4) = 2.5

Deviations: (−1.5, −0.5, 0.5, 1.5)

σ² = (1/4)(2.25 + 0.25 + 0.25 + 2.25) = (1/4)(5) = 1.25

σ = √1.25 ≈ 1.1180

x̂ ≈ (−1.5/1.1180, −0.5/1.1180, 0.5/1.1180, 1.5/1.1180)

≈ (−1.3416, −0.4472, 0.4472, 1.3416)

medium

You apply LayerNorm to a token embedding vector **x** ∈ ℝᵈ and then apply γ, β. If γ = **0** (all zeros) and β is nonzero, what is the output **y** for any input **x**? What does this mean representationally?

**Hint:** Use **y** = γ ⊙ x̂ + β and note what happens when γ is the zero vector.

Show solution

If γ = **0**, then γ ⊙ x̂ = **0** for any x̂. Therefore **y** = **0** + β = β for any input **x**.

Representationally, the layer outputs a constant vector (per position), ignoring the input. This shows γ can act like a gate that can completely suppress normalized features.

hard

Suppose a LayerNorm input **x** ∈ ℝᵈ has all components equal: xᵢ = c. Show what happens to x̂ when ε > 0, and explain why ε prevents numerical issues.

**Hint:** Compute μ and σ² explicitly when all values are identical.

Show solution

If xᵢ = c for all i, then:

μ = (1/d)∑ᵢ c = c

Each deviation xᵢ − μ = c − c = 0

So σ² = (1/d)∑ᵢ 0² = 0

With ε > 0:

x̂ᵢ = (xᵢ − μ)/√(σ² + ε) = 0/√(0 + ε) = 0

So x̂ is the zero vector.

ε prevents division by 0 because √(σ² + ε) = √ε > 0 even when σ² = 0.

## Connections

Next, see how LayerNorm is used inside Transformer blocks and why its placement matters:

- •[Transformers](/tech-tree/transformers/)

Related normalization ideas you may encounter later (not necessarily nodes here): BatchNorm, GroupNorm, RMSNorm (a LayerNorm variant that normalizes by RMS without subtracting μ).

Quality: A (4.4/5)

[← back to tree](/tech-tree/)[browse all →](/tech-tree/inventory/)
