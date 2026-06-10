---
title: Neural Networks
description: Layers of nonlinear transformations. Universal approximators.
date: '2026-07-01'
scheduled: '2026-09-24'
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
inspiration_url: https://templeton.host/tech-tree/neural-networks/
inspiration_category: tech-tree
---

> Source-copy draft imported from [https://templeton.host/tech-tree/neural-networks/](https://templeton.host/tech-tree/neural-networks/). Names, domain references, and local media paths were adapted for Xavi Ablaza / getablaza.com.

[←Back to Tech Tree](/tech-tree/)

[inventory](/tech-tree/inventory/)[coverage](/tech-tree/coverage/)

# Neural Networks

Machine LearningDifficulty: ★★★★☆Depth: 10Unlocks: 11

Layers of nonlinear transformations. Universal approximators.

## Interactive Visualization

⏮◀◀▶▶STEP0.25x1xZOOM

t=0s

## Core Concepts

- -Affine transformation (parameterized linear map): x -> W x + b
- -Elementwise nonlinearity (activation function): apply a nonlinear scalar function to each component
- -Layered composition: stacking alternating affine transforms and activations to form a single parametric function

## Key Symbols & Notation

W (weight matrix)b (bias vector)

## Essential Relationships

- -Composition and backpropagation: the network function is the composition of layers, and gradients of a loss w.r.t. W and b are obtained by chaining derivatives backward through that composition (backprop) for parameter optimization

## Prerequisites (2)

[Logistic Regression6 atoms](/tech-tree/logistic-regression/)[Matrix Calculus6 atoms](/tech-tree/matrix-calculus/)

## Unlocks (6)

[Backpropagationlvl 4](/tech-tree/backpropagation/)[Regularizationlvl 4](/tech-tree/regularization/)[Layer Normalizationlvl 4](/tech-tree/layer-normalization/)[Variational Autoencoderslvl 5](/tech-tree/vae/)[Dimensionality Reductionlvl 4](/tech-tree/dimensionality-reduction/)[Generative Adversarial Networkslvl 5](/tech-tree/gan/)

Advanced Learning Details

### Graph Position

136

Depth Cost

11

Fan-Out (ROI)

5

Bottleneck Score

10

Chain Length

### Cognitive Load

6

Atomic Elements

52

Total Elements

L4

Percentile Level

L4

Atomic Level

### All Concepts (20)

- - Feedforward neural network as a sequence of layers (input → hidden(s) → output)
- - Neuron/unit as an affine transform followed by a nonlinear activation
- - Layer as a vector-valued affine transform plus elementwise nonlinearity
- - Pre-activation (linear output of a layer) vs activation (post-nonlinearity output)
- - Activation functions beyond sigmoid (ReLU, tanh, softmax, leaky-ReLU, etc.)
- - Softmax as an output activation for multiclass probability distributions
- - Vector-valued output (logits) and conversion to class probabilities
- - Parameter set of a network (all weights and biases jointly) as model parameters
- - Forward pass: computing network outputs by sequentially applying affine+nonlinear layers
- - Backward pass / backpropagation: algorithm to compute gradients of loss w.r.t. parameters efficiently
- - Layer-wise error signal (delta) used in backpropagation
- - Gradient-based parameter update (e.g., stochastic gradient descent and mini-batches)
- - Learning rate as a hyperparameter controlling update step size
- - Weight initialization and its effects on training dynamics (vanishing/exploding gradients)
- - Nonlinearity requirement: without nonlinear activations, stacked layers collapse to a single linear map
- - Universal Approximation Theorem: a sufficiently wide single hidden-layer network with a suitable nonlinearity can approximate any continuous function on a compact domain (in principle)
- - Expressive power of depth vs width: deeper architectures can represent some functions more compactly than shallow ones
- - Generalization vs approximation: existence of an approximating network does not guarantee successful training or good generalization
- - Regularization methods commonly used with neural networks (L2 weight decay, dropout, early stopping)
- - Batching concepts: batch, mini-batch, epoch

### Teaching Strategy

Multi-session curriculum - substantial prior knowledge and complex material. Use mastery gates and deliberate practice.

A neural network is what you get when you stop asking a model to be “one good formula” and instead let it be “many simple formulas composed together.” Each layer is easy to understand (an affine map plus a nonlinearity), but stacking layers creates a surprisingly rich family of functions—rich enough to approximate almost any smooth pattern you can express with data.

TL;DR:

Neural networks are parametric functions built by alternating affine transformations (**x** ↦ W**x** + **b**) and elementwise nonlinearities. The nonlinearity is essential: without it, many layers collapse into one linear map. With it, depth creates expressive, flexible models that generalize logistic regression to multi-layer feature learning.

## What Is a Neural Network?

### Why this concept exists

Logistic regression is powerful because it turns a *linear* score (W**x** + b) into a *nonlinear* probability using σ(·). But it still fundamentally draws a linear decision boundary in the original feature space: it can only separate classes that are linearly separable (or close to it).

Neural networks extend this idea by repeatedly doing two steps:

1. 1)**Mix features linearly** (affine transformation)
2. 2)**Warp them nonlinearly** (activation)

By composing these steps many times, a network can learn intermediate representations—new “features” that make a difficult task easy for the final layer.

### The core object: a parametric function

A (feedforward) neural network defines a function:

f( **x**; θ ) → **y**

where θ is the set of all parameters, typically weights and biases across layers:

θ = { (W¹, **b**¹), (W², **b**²), …, (Wᴸ, **b**ᴸ) }

A standard L-layer multilayer perceptron (MLP) has hidden states **h**ˡ computed as:

- •**h**⁰ = **x**
- •**z**ˡ = Wˡ **h**ˡ⁻¹ + **b**ˡ (pre-activation)
- •**h**ˡ = φ( **z**ˡ ) (activation, elementwise)

The final layer is sometimes left “linear” (no activation) depending on the task.

### Shapes (so nothing feels mysterious)

If the input has dimension d and layer l has width nˡ:

- •**h**ˡ⁻¹ ∈ ℝⁿˡ⁻¹
- •Wˡ ∈ ℝⁿˡ × ⁿˡ⁻¹
- •**b**ˡ ∈ ℝⁿˡ
- •**z**ˡ, **h**ˡ ∈ ℝⁿˡ

This is just matrix-vector multiplication plus a bias.

### What does “universal approximator” mean (informally)?

A key motivation: neural networks can approximate very complicated functions. Roughly:

- •With enough hidden units (often in a single hidden layer), an MLP can approximate any continuous function on a bounded region, to arbitrary accuracy.

Important nuance:

- •“Can approximate” does not mean “will learn easily.” Optimization, generalization, and architecture matter.

### Neural networks as “learned features”

A helpful mental model is:

- •The first layers learn useful transformations of **x**.
- •The final layer performs a simpler prediction in the transformed space.

This is logistic regression’s idea—applied repeatedly.

### Connection to logistic regression

Binary logistic regression can be written as a 1-layer network:

p(y = 1 | **x**) = σ( W**x** + b )

A deeper network replaces the direct linear score with a learned feature map **h** = g(**x**) and then uses:

p(y = 1 | **x**) = σ( **w**ᵀ **h** + b )

where g(·) is itself a composition of affine maps and nonlinearities.

## Core Mechanic 1: Affine Transformations as Learnable Feature Mixing

### Why affine maps are the workhorse

An affine transformation

**x** ↦ W**x** + **b**

is the simplest learnable operation that can:

- •**Scale** and **rotate** directions in space (via W)
- •**Translate** the origin (via **b**)
- •**Mix** input coordinates into new coordinates

If you have matrix calculus background, you already know how gradients behave for affine maps, which is one reason they are so central.

### Geometry intuition

Think of **x** as a point in ℝᵈ.

- •Multiplying by W maps the entire space by a linear transformation.
- •Adding **b** shifts everything.

A linear layer can:

- •Stretch some directions
- •Compress others
- •Shear
- •Rotate (in a generalized sense)
- •Project into a lower-dimensional subspace (if nˡ < nˡ⁻¹)

But a single affine layer cannot “bend” space. It cannot create curved decision boundaries by itself.

### Affine layers and feature creation

Suppose the first layer is:

**z**¹ = W¹ **x** + **b**¹

Each coordinate z¹ᵢ is:

z¹ᵢ = **w**¹ᵢᵀ **x** + b¹ᵢ

So every neuron computes a linear score of the input—very similar to logistic regression’s logit. The difference comes next: we don’t directly interpret this as a probability; we *feed it forward* as a feature.

### Why the bias matters

Without **b**, every hyperplane zᵢ = 0 must pass through the origin. Adding bias lets each neuron choose its own threshold.

This matters especially when combined with piecewise-linear activations (like ReLU), where the bias controls where the “kink” happens.

### Layer widths: undercomplete vs overcomplete

The hidden dimension nˡ affects what the network can represent.

| Choice | What it enables | What it risks |
| --- | --- | --- |
| nˡ < nˡ⁻¹ (compression) | bottleneck features, dimensionality reduction | information loss |
| nˡ = nˡ⁻¹ | stable capacity | may need depth for expressiveness |
| nˡ > nˡ⁻¹ (expansion) | rich feature mixing, sparse or disentangled features | overfitting, optimization cost |

### Composition of affine maps (a crucial warning)

If you stack affine maps *without* nonlinearities:

**h**¹ = W¹ **x** + **b**¹

**h**² = W² **h**¹ + **b**²

then:

**h**² = W²(W¹ **x** + **b**¹) + **b**²

= (W²W¹)**x** + (W²**b**¹ + **b**²)

This is still just one affine map.

So if we only used affine layers, depth would be pointless. The entire expressive leap of neural networks comes from the nonlinearity.

## Core Mechanic 2: Elementwise Nonlinearities (Activations) Create Expressiveness

### Why nonlinearities are the “magic ingredient”

A nonlinearity φ applied elementwise:

**h** = φ(**z**) meaning hᵢ = φ(zᵢ)

is what prevents the network from collapsing into a single affine transformation.

Nonlinearities let networks represent:

- •Curved decision boundaries
- •Piecewise-linear or smooth nonlinear functions
- •Hierarchical feature detectors

### Common activation functions

You’ll see a small set of activations repeatedly:

| Activation | Formula | Range | Pros | Cons |
| --- | --- | --- | --- | --- |
| Sigmoid | σ(t) = 1/(1+e⁻ᵗ) | (0,1) | probabilistic interpretation | saturates, vanishing gradients |
| Tanh | tanh(t) | (−1,1) | zero-centered | saturates |
| ReLU | max(0, t) | [0, ∞) | simple, sparse, strong gradients for t>0 | “dead” units for t≤0 |
| Leaky ReLU | max(αt, t) | (−∞, ∞) | reduces dead units | extra hyperparameter α |
| GELU | t·Φ(t) (approx) | (−∞, ∞) | smooth, strong in transformers | more compute |

For many modern MLPs, ReLU/GELU variants dominate.

### How ReLU creates piecewise linearity

Consider a 1D input x and a single neuron:

h = ReLU(wx + b)

This is:

- •0 when wx + b ≤ 0
- •wx + b when wx + b > 0

So it is a “hinge” function with a kink at x = −b/w.

If you sum many such hinges, you can approximate complex shapes. In higher dimensions, each ReLU neuron corresponds to a half-space boundary (**w**ᵀ**x** + b = 0), and the network becomes a partition of input space into regions where the overall function is linear.

### Depth vs width (intuition)

- •**Width** (more neurons) gives more “pieces” to build with.
- •**Depth** (more layers) composes pieces, often allowing exponentially many linear regions with modest width.

This is part of why deep networks can represent complex functions more efficiently than shallow ones.

### Output activations depend on the task

The last layer is often chosen to match the meaning of outputs:

| Task | Output | Typical final layer |
| --- | --- | --- |
| Binary classification | p(y=1) | sigmoid |
| Multi-class classification | p(y=k) | softmax |
| Regression | real value | linear (identity) |

For multi-class, with logits **s** ∈ ℝᴷ:

softmax(**s**)ₖ = exp(sₖ) / ∑ⱼ exp(sⱼ)

### Why “elementwise” is a design choice

Elementwise nonlinearities are simple and efficient. But note:

- •They do not mix coordinates; mixing happens in W.
- •They create nonlinearity coordinate-by-coordinate.

Many advanced architectures introduce nonlinearities that depend on multiple coordinates (attention, normalization, gating). But elementwise activations are the core starting point.

## Layered Composition: From Simple Parts to a Single Powerful Function

### Why composition is the right mental model

A neural network is best understood as a composition of functions:

f(**x**) = fᴸ ∘ fᴸ⁻¹ ∘ … ∘ f¹ (**x**)

where each layer function is typically:

fˡ(**h**) = φ( Wˡ **h** + **b**ˡ )

Composition matters because:

- •each layer can build features on top of previous features
- •the model’s complexity grows quickly with depth
- •training relies on chain rule through the composition (this motivates backpropagation)

### Writing an MLP explicitly

For a 2-hidden-layer network:

**h**¹ = φ( W¹ **x** + **b**¹ )

**h**² = φ( W² **h**¹ + **b**² )

**y** = W³ **h**² + **b**³

Even though each step is simple, the final mapping **x** ↦ **y** can be highly nonlinear.

### Interpreting hidden units as detectors

Each neuron computes:

hᵢ = φ(**w**ᵀ **h\_prev** + b)

This can be seen as:

- •measure alignment of **h\_prev** with **w**
- •compare to threshold (via b)
- •output an activated feature

In early layers, features might correspond to simple patterns.

In deeper layers, features become combinations of combinations.

### A practical view: network as a feature map + linear head

Many networks can be decomposed conceptually:

**h** = g(**x**; θ\_g)

**y** = A**h** + **c**

where g is the deep feature extractor and (A, **c**) is a linear “head.”

This view is helpful because:

- •it links directly to logistic regression
- •it explains transfer learning: reuse g and retrain the head

### Loss functions (what training tries to minimize)

A neural network becomes useful when paired with a loss.

Given dataset {( **x**⁽ⁱ⁾, **t**⁽ⁱ⁾ )}ᵢ:

Minimize: (1/N) ∑ᵢ ℓ( f(**x**⁽ⁱ⁾), **t**⁽ⁱ⁾ )

Examples:

- •Regression: ℓ = ‖**y** − **t**‖²
- •Binary classification: cross-entropy with sigmoid
- •Multi-class: cross-entropy with softmax

Because you know matrix calculus, you can view training as gradient-based optimization in a high-dimensional parameter space.

### Parameter counting (capacity intuition)

If layer l has nˡ units and previous layer has nˡ⁻¹:

- •Wˡ has nˡ·nˡ⁻¹ parameters
- •**b**ˡ has nˡ parameters

Total parameters ≈ ∑ˡ (nˡ·nˡ⁻¹ + nˡ)

Large capacity can fit complex functions—but increases overfitting risk, motivating regularization (an unlock node).

### A note on “universal approximation” and practice

Universal approximation results say “there exists parameters.” In practice you must also consider:

- •optimization landscape (local minima, saddle points)
- •initialization and gradient flow
- •data quantity and noise

This is why deep learning is both a theory of function classes and an engineering discipline.

## Application / Connection: Where Neural Networks Fit in Machine Learning

### Neural networks as the default nonlinear model

When feature engineering is hard, neural networks shine because they can *learn* representations.

They appear in many forms:

- •MLPs for tabular data (sometimes, though tree methods can compete)
- •CNNs for images (spatial structure)
- •RNNs/LSTMs for sequences (temporal structure)
- •Transformers for language and general sequence modeling

The common thread is still layers of affine-like transforms plus nonlinearities, often with architectural constraints.

### Decision boundaries: from linear to complex

Logistic regression gives a hyperplane boundary.

An MLP can build boundaries that are unions and compositions of many half-spaces.

A helpful picture (conceptual):

- •first layer creates many “cuts” of the space
- •next layer recombines these regions
- •deeper layers carve intricate regions that match data manifolds

### Why training needs backpropagation

To train, you need gradients ∂ℓ/∂Wˡ and ∂ℓ/∂**b**ˡ for every layer.

Naively computing derivatives separately for each parameter would be expensive.

Backpropagation is the efficient application of chain rule through the layered composition. This is exactly the next node you unlock.

### Regularization and normalization are not optional in deep nets

High-capacity models can memorize. Regularization techniques (L2, dropout, early stopping) and normalization (batch norm, layer norm) help:

- •stabilize optimization
- •improve generalization

These are also unlocked nodes—and they become much easier to appreciate once the basic network mapping is clear.

### Neural nets as building blocks for generative models

Variational autoencoders (VAEs) and many other generative models use neural networks to parameterize distributions:

- •encoder network outputs parameters of q(**z**|**x**)
- •decoder network outputs parameters of p(**x**|**z**)

In this sense, “neural network” is not the whole algorithm; it’s the function approximator inside the algorithm.

### Connection to dimensionality reduction

Autoencoders are neural networks trained to reconstruct inputs through a bottleneck:

**x** → encoder → **z** (low-dim) → decoder → **x̂**

This creates a learned, nonlinear dimensionality reduction—connected to the dimensionality reduction node.

## Worked Examples (3)

### Forward pass through a small MLP (with shapes and numbers)

Compute the output of a 2-layer network with ReLU hidden layer and a linear output. Let **x** ∈ ℝ².

Given:

W¹ = [[1, −2],

[0, 3]] , **b**¹ = [−1, 2]

W² = [[2, −1]] , **b**² = [0.5]

Activation φ = ReLU.

Input **x** = [2, 1].

1. Step 1: Compute pre-activation **z**¹ = W¹**x** + **b**¹.

   W¹**x** = [[1, −2],[0, 3]] [2,1]

   = [1·2 + (−2)·1,

   0·2 + 3·1]

   = [0, 3]

   **z**¹ = [0, 3] + [−1, 2] = [−1, 5]
2. Step 2: Apply ReLU: **h**¹ = ReLU(**z**¹).

   ReLU([−1, 5]) = [0, 5]
3. Step 3: Compute output pre-activation **z**² = W²**h**¹ + **b**².

   W²**h**¹ = [2, −1] [0,5] = 2·0 + (−1)·5 = −5

   **z**² = −5 + 0.5 = −4.5
4. Step 4: Since output is linear, **y** = **z**².

   Final output y = −4.5

**Insight:** Even with tiny matrices, you can see the pattern: affine → ReLU → affine. ReLU zeroed out the first hidden unit, so only the second feature contributed to the final score. This “selective routing” is a core behavior of ReLU networks.

### Why nonlinearities are necessary: collapsing two affine layers into one

Show that stacking affine layers without an activation is still just an affine map.

Let **h**¹ = W¹**x** + **b**¹ and **h**² = W²**h**¹ + **b**².

1. Start with the definition of the second layer:

   **h**² = W²**h**¹ + **b**²
2. Substitute **h**¹ = W¹**x** + **b**¹:

   **h**² = W²(W¹**x** + **b**¹) + **b**²
3. Distribute W²:

   **h**² = W²W¹**x** + W²**b**¹ + **b**²
4. Group terms into a single affine form:

   Let W̃ = W²W¹ and **b**̃ = W²**b**¹ + **b**².

   Then **h**² = W̃**x** + **b**̃

**Insight:** Depth without nonlinearity gives no extra expressive power. Activations prevent this collapse, making layered composition meaningful.

### A tiny universal-approximation intuition in 1D with ReLU “hinges”

Approximate a simple piecewise-linear function on x ∈ [0, 2] using a sum of shifted ReLUs.

Target function:

f(x) = { x for 0 ≤ x ≤ 1

{ 2 − x for 1 < x ≤ 2

This is a triangle peak at x=1. Show it can be written using ReLU(·).

1. Recall ReLU(t) = max(0, t). Consider these three hinge functions:

   h₁(x) = ReLU(x)

   h₂(x) = ReLU(x − 1)

   h₃(x) = ReLU(x − 2)
2. Construct a piecewise-linear function by combining them:

   g(x) = 1·h₁(x) − 2·h₂(x) + 1·h₃(x)
3. Check intervals.

   For 0 ≤ x ≤ 1:

   - •h₁(x)=x
   - •h₂(x)=0
   - •h₃(x)=0

   So g(x)=x (matches f).
4. For 1 ≤ x ≤ 2:

   - •h₁(x)=x
   - •h₂(x)=x−1
   - •h₃(x)=0

   So g(x)= x − 2(x−1) = x − 2x + 2 = 2 − x (matches f).
5. For x ≥ 2:

   - •h₁(x)=x
   - •h₂(x)=x−1
   - •h₃(x)=x−2

   So g(x)= x − 2(x−1) + (x−2) = 0 (triangle returns to 0).

**Insight:** A sum of a few shifted ReLUs can build a nontrivial shape. In higher dimensions and deeper networks, this idea scales: many hinges compose into extremely rich functions.

## Key Takeaways

- ✓

  A feedforward neural network is a composition of layers: **h**ˡ = φ(Wˡ**h**ˡ⁻¹ + **b**ˡ).
- ✓

  Affine layers (W**x** + **b**) mix and shift features but cannot create curvature by themselves.
- ✓

  Elementwise nonlinearities (ReLU, tanh, sigmoid, GELU, …) prevent stacked affine maps from collapsing into one affine map.
- ✓

  Depth matters because composition can create complex functions from simple building blocks; width controls how many features exist per layer.
- ✓

  The last-layer activation should match the task (sigmoid for binary, softmax for multi-class, identity for regression).
- ✓

  Neural networks generalize logistic regression: logistic regression is essentially a 1-layer network with sigmoid output.
- ✓

  Universal approximation is an existence statement: a network *can* represent many functions, but training and generalization require additional tools (backprop, regularization, normalization).

## Common Mistakes

- ✗

  Assuming more layers automatically help, while forgetting that without nonlinearities, multiple layers are equivalent to one affine map.
- ✗

  Mixing up shapes: Wˡ is (nˡ × nˡ⁻¹) and multiplies **h**ˡ⁻¹ on the right; many bugs are silent shape/broadcast errors.
- ✗

  Using sigmoid/tanh everywhere in deep nets without considering saturation and vanishing gradients (often ReLU/GELU are better defaults).
- ✗

  Interpreting “universal approximator” as “guaranteed to train well” rather than “able to represent.”

## Practice

easy

You are given a network **h**¹ = ReLU(W¹**x** + **b**¹), y = σ(**w**ᵀ**h**¹ + b). If ReLU were removed (replaced with identity), show that the model reduces to logistic regression in the original input **x**.

**Hint:** Substitute **h**¹ = W¹**x** + **b**¹ into the output and regroup terms into a single weight vector and bias.

Show solution

Without ReLU, **h**¹ = W¹**x** + **b**¹.

Then the logit is:

s = **w**ᵀ**h**¹ + b

= **w**ᵀ(W¹**x** + **b**¹) + b

= (**w**ᵀW¹)**x** + (**w**ᵀ**b**¹ + b)

Define **w**̃ᵀ = **w**ᵀW¹ and b̃ = **w**ᵀ**b**¹ + b.

So p(y=1|**x**) = σ(s) = σ(**w**̃ᵀ**x** + b̃), which is logistic regression.

medium

Consider an MLP with input dimension d = 10, one hidden layer of width n¹ = 64, and output dimension K = 5 (multi-class). The hidden layer uses ReLU and the output uses softmax. How many parameters are there total (including biases)?

**Hint:** Count parameters per layer: W¹, **b**¹, W², **b**².

Show solution

Layer 1: W¹ ∈ ℝ⁶⁴×¹⁰ has 64·10 = 640 parameters. **b**¹ ∈ ℝ⁶⁴ has 64 parameters.

Layer 2: W² ∈ ℝ⁵×⁶⁴ has 5·64 = 320 parameters. **b**² ∈ ℝ⁵ has 5 parameters.

Total = 640 + 64 + 320 + 5 = 1029 parameters.

hard

Let φ be ReLU. For a 1-hidden-layer network f(x) = ∑ᵢ aᵢ ReLU(wᵢ x + bᵢ) + c in 1D, explain why f(x) is piecewise linear, and where its slope can change.

**Hint:** Each ReLU term changes from 0 to linear at the point where wᵢ x + bᵢ = 0.

Show solution

Each term ReLU(wᵢ x + bᵢ) is either 0 (when wᵢ x + bᵢ ≤ 0) or a linear function (wᵢ x + bᵢ) (when wᵢ x + bᵢ > 0). Therefore, on any interval where the sign of every (wᵢ x + bᵢ) is fixed, every term is linear (either constant 0 or linear), and the sum is linear.

A slope change can only occur when at least one neuron switches regime, i.e., at a breakpoint x where wᵢ x + bᵢ = 0 ⇒ x = −bᵢ / wᵢ (for wᵢ ≠ 0). Thus f(x) is piecewise linear with possible kinks at those breakpoint locations.

## Connections

Next nodes you’re set up for:

- •[Backpropagation](/tech-tree/backpropagation/) — Apply chain rule through layered composition to compute ∂ℓ/∂Wˡ and ∂ℓ/∂**b**ˡ efficiently.
- •[Regularization](/tech-tree/regularization/) — Control capacity and improve generalization (L2, dropout, early stopping).
- •[Layer Normalization](/tech-tree/layer-normalization/) — Stabilize activations and gradients in deep stacks.
- •[Variational Autoencoders](/tech-tree/vae/) — Use neural nets to parameterize probabilistic encoders/decoders.
- •[Dimensionality Reduction](/tech-tree/dimensionality-reduction/) — Understand autoencoders as nonlinear learned reductions.

Related refreshers:

- •[Logistic Regression](/tech-tree/logistic-regression/)
- •[Matrix Calculus](/tech-tree/matrix-calculus/)

Quality: B (4.4/5)

[← back to tree](/tech-tree/)[browse all →](/tech-tree/inventory/)
