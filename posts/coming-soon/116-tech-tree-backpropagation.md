---
title: Backpropagation
description: Computing gradients efficiently via chain rule through network.
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
permalink: /tech-tree/backpropagation/
---

[←Back to Tech Tree](/tech-tree/)

[inventory](/tech-tree/inventory/)[coverage](/tech-tree/coverage/)

# Backpropagation

Machine LearningDifficulty: ★★★★☆Depth: 11Unlocks: 4

Computing gradients efficiently via chain rule through network.

## Interactive Visualization

⏮◀◀▶▶STEP0.25x1xZOOM

t=0s

## Core Concepts

- -Node-local backward rule: a node converts an incoming loss gradient into gradients for its inputs using only its local partial derivatives.
- -Reverse traversal of the computation graph: apply the node-local backward rules in reverse topological order, summing contributions where multiple forward paths meet.

## Key Symbols & Notation

delta\_j := dL/dz\_j (node upstream gradient / sensitivity)

## Essential Relationships

- -Local chain-rule transform: dL/dx = (dL/dy) \* (dy/dx) (apply the chain rule at each node).
- -Parameter gradient relation: dL/dtheta = delta\_node \* (d node output / dtheta) (upstream sensitivity times local parameter derivative).

## Prerequisites (2)

[Neural Networks6 atoms](/tech-tree/neural-networks/)[Multivariable Chain Rule6 atoms](/tech-tree/chain-rule-multivar/)

## Unlocks (1)

[Deep Learninglvl 5](/tech-tree/deep-learning/)

Advanced Learning Details

### Graph Position

147

Depth Cost

4

Fan-Out (ROI)

2

Bottleneck Score

11

Chain Length

### Cognitive Load

5

Atomic Elements

39

Total Elements

L2

Percentile Level

L3

Atomic Level

### All Concepts (15)

- - computational graph: representing the network and loss as a directed acyclic graph of elementary operations
- - forward pass vs backward pass: computing outputs/activations first, then propagating gradients backward
- - loss as a scalar function of network parameters via network outputs (L(θ) or L(y, ŷ))
- - gradient of the loss with respect to parameters (weights and biases) as the target quantity
- - layer-local quantities: pre-activation (z^l) and activation (a^l) as intermediates needed for gradients
- - local gradient of a layer: derivative of the layer's activation function evaluated at its pre-activation
- - layerwise error signal (δ^l): the sensitivity of the loss to the pre-activation of a layer
- - recursive/backpropagation rule: compute layerwise error signals by propagating downstream errors upstream
- - efficient reuse of stored intermediate values (activations, pre-activations) to avoid redundant derivative work
- - vectorized (matrix) formulation of backpropagation using weight matrices and batch vectors
- - Hadamard/elementwise combination of upstream error and local derivative when computing deltas
- - backprop as reverse-mode automatic differentiation: computing Jacobian-transpose-vector (sensitivity) products without forming full Jacobians
- - computational/memory trade-off: need to store activations during the forward pass to compute backward pass
- - vanishing and exploding gradients as phenomena arising from repeated application of layer Jacobians/weight multiplications across many layers
- - parameter update step using computed gradients (e.g., gradient descent: update rule W <- W - η ∂L/∂W)

### Teaching Strategy

Quick unlock - significant prerequisite investment but simple final step. Verify prerequisites first.

Training a neural network is mostly one question repeated millions of times: “If I nudge this weight a tiny bit, how does the loss change?” Backpropagation is the algorithmic answer—an efficient way to compute all those derivatives without redoing work for every parameter.

TL;DR:

Backpropagation computes ∂L/∂(parameters) efficiently by (1) viewing the network as a computation graph, (2) running a forward pass to cache intermediate values, then (3) running a backward pass that propagates sensitivities δⱼ := ∂L/∂zⱼ from outputs to inputs using node-local partial derivatives, summing gradient contributions where paths merge.

## What Is Backpropagation?

### The goal: gradients for learning

A neural network learns by adjusting parameters (weights and biases) to reduce a loss L. Gradient-based optimization methods (like SGD, Momentum, Adam) need derivatives such as ∂L/∂W and ∂L/∂b.

If you tried to compute these derivatives “from scratch” for each parameter independently, you would do a huge amount of repeated work. A modern network can have millions or billions of parameters, and the forward computation reuses intermediate activations across many parameters. We want the same kind of reuse when differentiating.

Backpropagation is exactly that: **a systematic reuse of intermediate derivative calculations**.

### The key viewpoint: computation graphs

Any forward computation can be represented as a directed acyclic graph (DAG) where:

- •Nodes are intermediate values (scalars, vectors, tensors).
- •Edges represent functional dependencies.

Example (conceptually):

- •z = Wx + b
- •a = σ(z)
- •L = ℓ(a, y)

Even if you write this as “layers,” it’s still a composition of functions, which is what the chain rule is about.

### Sensitivities (upstream gradients)

A central symbol in backprop is the **sensitivity** of the loss to a node’s pre-activation (or any intermediate variable). For a scalar loss L and a node value zⱼ, define:

δⱼ := ∂L/∂zⱼ

Think of δ as answering: “If zⱼ changes a tiny bit, how much does the loss change?”

### Two atomic ideas (the whole algorithm)

Backpropagation is built from two atomic concepts:

1) **Node-local backward rule**

A node converts an incoming loss gradient (upstream gradient) into gradients for its inputs using only its **local** partial derivatives.

If a node computes:

z = f(x)

and you know the upstream gradient ∂L/∂z, then the chain rule gives:

∂L/∂x = ∂L/∂z · ∂z/∂x

This is “local”: it only needs the node’s own derivative ∂z/∂x and the incoming gradient.

2) **Reverse traversal + summation at merges**

You apply these node-local rules in **reverse topological order** (from outputs back to inputs). If multiple forward paths feed into the same variable, their gradient contributions **add**.

This “add at merges” is not a special trick—it is exactly the multivariable chain rule.

### Why it’s efficient

Suppose your network computes L in O(C) time (C is the cost of the forward pass). Backprop computes all parameter gradients in about O(C) additional time (often a small constant multiple).

In contrast, computing a gradient for each parameter via finite differences would take O(P·C) where P is the number of parameters. That’s infeasible.

### What backprop is not

- •It is **not** a specific optimizer.
- •It is **not** restricted to neural networks; it applies to any differentiable computation graph.
- •It does **not** magically avoid the chain rule; it is the chain rule organized to reuse work.

The big idea to keep in your head: **Forward pass computes values. Backward pass computes sensitivities, reusing cached values and local derivatives.**

## Core Mechanic 1: The Node-Local Backward Rule (Chain Rule in “Message Passing” Form)

### Why start local?

A neural network is built from small operations: add, multiply, matrix multiply, activation functions, normalization, etc. If we can differentiate each operation locally, we can differentiate the whole network by composition.

This makes backprop feel like **message passing**:

- •Each node receives an upstream gradient (a “message” about how L changes with respect to that node).
- •It sends downstream gradients to its inputs.

### Single-input case

Let a node compute:

z = f(x)

Loss is L(z). By the chain rule:

∂L/∂x = ∂L/∂z · ∂z/∂x

Written as a backward rule:

- •Input: upstream gradient gₙ = ∂L/∂z
- •Local derivative: f′(x) = ∂z/∂x
- •Output: ∂L/∂x = gₙ · f′(x)

This is the simplest “local rule.”

### Multi-input case: the true neural-network setting

Most nodes have multiple inputs. Suppose:

z = f(x, y)

Then:

∂L/∂x = ∂L/∂z · ∂z/∂x

∂L/∂y = ∂L/∂z · ∂z/∂y

Same upstream gradient ∂L/∂z fans out to each input, multiplied by the appropriate local partial.

### Merge case: when multiple paths contribute

Now suppose a variable x influences L through two different children nodes, z₁ and z₂:

z₁ = f₁(x)

z₂ = f₂(x)

L = g(z₁, z₂)

Then x affects L through both routes. Multivariable chain rule gives:

∂L/∂x = (∂L/∂z₁)(∂z₁/∂x) + (∂L/∂z₂)(∂z₂/∂x)

This is the “sum contributions at merges” rule.

### A tiny computation-graph example (scalar)

Let:

- •u = x · y
- •v = u + y
- •L = v²

Forward:

- •u = xy
- •v = u + y
- •L = v²

Backward (local rules):

1) L = v² ⇒ ∂L/∂v = 2v

2) v = u + y ⇒ ∂v/∂u = 1, ∂v/∂y = 1

So ∂L/∂u = ∂L/∂v · 1

And contribution to ∂L/∂y from this path is ∂L/∂v · 1

3) u = x · y ⇒ ∂u/∂x = y, ∂u/∂y = x

So ∂L/∂x = ∂L/∂u · y

And contribution to ∂L/∂y from this path is ∂L/∂u · x

Finally, add the two contributions to ∂L/∂y:

∂L/∂y = (from v) + (from u)

= (∂L/∂v · 1) + (∂L/∂u · x)

Notice how “sum at merge” naturally appears because y is used in two places.

### Vector/matrix shapes: the practical reality

Neural nets use vector-valued activations and matrix multiplies. The same local-rule logic holds, but you must respect shapes.

A very common pattern:

**z** = W**x** + **b**

Where:

- •W ∈ ℝ^{m×n}
- •**x** ∈ ℝ^{n}
- •**b** ∈ ℝ^{m}
- •**z** ∈ ℝ^{m}

Given upstream gradient **g** = ∂L/∂**z** (same shape as **z**), the local backward rules are:

∂L/∂**b** = **g**

∂L/∂W = **g** **x**ᵀ

∂L/∂**x** = Wᵀ **g**

These formulas are not “memorize-only.” They come from componentwise chain rule. For example, for W:

Let zᵢ = ∑ⱼ Wᵢⱼ xⱼ + bᵢ

Then:

∂L/∂Wᵢⱼ = ∑ₖ (∂L/∂zₖ)(∂zₖ/∂Wᵢⱼ)

But zₖ depends on Wᵢⱼ only when k = i, so:

∂zₖ/∂Wᵢⱼ = xⱼ if k = i, else 0

So:

∂L/∂Wᵢⱼ = (∂L/∂zᵢ) xⱼ

In matrix form that is **g** **x**ᵀ.

### What to cache from the forward pass

Node-local derivatives typically depend on forward values (like x for σ′(x), or **x** for **g****x**ᵀ).

So the forward pass doesn’t just compute outputs; it **stores** the needed intermediates (often called “activations” and sometimes “pre-activations”). Backprop then uses them.

A useful mental rule:

- •If an operation’s derivative depends on its input, you will need that input saved (or recomputed).

This is why training uses more memory than inference.

### Summary table: common node-local backward rules

| Forward op | Forward definition | Upstream gradient | Backward outputs |
| --- | --- | --- | --- |
| Add | z = x + y | ∂L/∂z | ∂L/∂x = ∂L/∂z, ∂L/∂y = ∂L/∂z |
| Multiply | z = x·y | ∂L/∂z | ∂L/∂x = (∂L/∂z)·y, ∂L/∂y = (∂L/∂z)·x |
| Affine | **z** = W**x** + **b** | **g** = ∂L/∂**z** | ∂L/∂W = **g****x**ᵀ, ∂L/∂**b** = **g**, ∂L/∂**x** = Wᵀ**g** |
| ReLU | a = max(0, z) | ∂L/∂a | ∂L/∂z = (∂L/∂a) ⊙ 𝟙[z>0] |
| Sigmoid | a = σ(z) | ∂L/∂a | ∂L/∂z = (∂L/∂a) ⊙ a ⊙ (1−a) |
| Tanh | a = tanh(z) | ∂L/∂a | ∂L/∂z = (∂L/∂a) ⊙ (1−a²) |

(⊙ is elementwise product.)

These are “node-local rules”: upstream gradient in, multiply by local derivative, produce gradients out.

## Core Mechanic 2: Reverse Traversal of the Computation Graph (and Why We Sum at Merges)

### Why reverse order?

In the forward pass, you compute prerequisites first: inputs → intermediate values → loss.

In the backward pass, you need ∂L/∂(something). But ∂L/∂(something) depends on how that “something” affects later computations. So you must start at L and propagate backward: loss → outputs → earlier intermediates → parameters.

This is exactly reverse topological order on the computation graph.

### A clean statement of the algorithm

Given a computation graph that produces scalar loss L:

1) **Forward pass**

- •Compute every node value.
- •Cache required intermediates.

2) **Initialize the backward pass**

- •Set ∂L/∂L = 1.

3) **Reverse traversal**

- •For each node z, assume you have accumulated its upstream gradient ∂L/∂z.
- •Apply the node’s local backward rule to compute contributions to each parent/input.
- •If a parent receives multiple contributions, **add** them.

4) **Read off parameter gradients**

- •The gradients with respect to W, **b**, etc. are now available.

### Why do gradients add at merges? (A derivation)

Suppose x feeds into two children nodes z₁ and z₂, and both influence L.

Let:

z₁ = f₁(x)

z₂ = f₂(x)

L = g(z₁, z₂)

We can derive ∂L/∂x explicitly:

∂L/∂x = (∂L/∂z₁)(∂z₁/∂x) + (∂L/∂z₂)(∂z₂/∂x)

Steps:

- •L = g(z₁, z₂) with z₁ and z₂ depending on x.
- •Differentiate L with respect to x via multivariable chain rule:

∂L/∂x = ∂g/∂z₁ · ∂z₁/∂x + ∂g/∂z₂ · ∂z₂/∂x

Recognize ∂g/∂z₁ = ∂L/∂z₁ and ∂g/∂z₂ = ∂L/∂z₂.

So if x has multiple outgoing edges in the forward graph, it has multiple incoming gradient contributions in the backward graph, which must be summed.

### “δ” notation and layerwise backprop

In neural networks, it’s common to distinguish:

- •Pre-activation **z**ˡ (before nonlinearity)
- •Activation **a**ˡ (after nonlinearity)

For layer ℓ:

**z**ˡ = Wˡ **a**ˡ⁻¹ + **b**ˡ

**a**ˡ = φ(**z**ˡ)

Define the layer sensitivity:

**δ**ˡ := ∂L/∂**z**ˡ

This is exactly your node-local symbol δⱼ := ∂L/∂zⱼ, but grouped by layer and vectorized.

Now derive the standard backprop identities.

#### Step 1: Backprop through the activation

We have **a**ˡ = φ(**z**ˡ). So elementwise:

∂L/∂**z**ˡ = ∂L/∂**a**ˡ ⊙ φ′(**z**ˡ)

So:

**δ**ˡ = (∂L/∂**a**ˡ) ⊙ φ′(**z**ˡ)

#### Step 2: Backprop through the affine transform

**z**ˡ = Wˡ **a**ˡ⁻¹ + **b**ˡ.

Given **δ**ˡ = ∂L/∂**z**ˡ, we get:

∂L/∂Wˡ = **δ**ˡ (**a**ˡ⁻¹)ᵀ

∂L/∂**b**ˡ = **δ**ˡ

∂L/∂**a**ˡ⁻¹ = (Wˡ)ᵀ **δ**ˡ

Now plug Step 2 into Step 1 for the previous layer:

**δ**ˡ⁻¹ = (∂L/∂**a**ˡ⁻¹) ⊙ φ′(**z**ˡ⁻¹)

= ((Wˡ)ᵀ **δ**ˡ) ⊙ φ′(**z**ˡ⁻¹)

That is the classic recurrence.

### Where the loss gradient starts

The backward pass starts from the loss. Two common cases:

1) **Regression with MSE**

If L = ½‖**a**ᴸ − **y**‖², then:

∂L/∂**a**ᴸ = **a**ᴸ − **y**

Then **δ**ᴸ = (∂L/∂**a**ᴸ) ⊙ φ′(**z**ᴸ).

2) **Classification with softmax + cross-entropy**

A very common final layer is:

**p** = softmax(**z**)

L = −∑ᵢ yᵢ log pᵢ

A key simplification (worth remembering) is:

∂L/∂**z** = **p** − **y**

So the starting sensitivity at the logits is just prediction minus label.

### Computational story: forward is evaluation, backward is accumulation

A useful way to imagine backprop in code:

- •Each node stores:
- •its forward value
- •pointers to its parents
- •a function that maps upstream gradient → parent gradients
- •Backward initializes grad[L] = 1
- •Then repeatedly:
- •take a node whose gradient is known
- •apply its backward rule
- •add contributions into its parents’ gradient slots

This is reverse-mode automatic differentiation (reverse-mode AD). Backpropagation is reverse-mode AD specialized to neural nets.

### Quick comparison: forward-mode vs reverse-mode

| Mode | Computes | Best when | Cost intuition |
| --- | --- | --- | --- |
| Forward-mode AD | directional derivatives (Jacobian-vector products) | few inputs, many outputs | roughly scales with #inputs |
| Reverse-mode AD (backprop) | gradients of scalar loss (vector-Jacobian products) | many parameters, scalar loss | roughly scales with #outputs (≈1) |

Neural nets have huge input dimension in parameter space (millions of weights) and a single scalar loss, so reverse-mode is ideal.

## Application/Connection: Backprop in Real Neural Networks (Batches, Modules, and Practical Gotchas)

### From single example to minibatches

In practice, we rarely train on one example at a time. With a minibatch of size B:

- •Activations become matrices (or higher tensors).
- •Gradients must aggregate over the batch.

Suppose **X** ∈ ℝ^{n×B} and **Z** = W**X** + **b**, where **b** is broadcast across columns.

Let **G** = ∂L/∂**Z** ∈ ℝ^{m×B}.

Then the batched gradients are:

∂L/∂W = **G** **X**ᵀ

∂L/∂**b** = ∑\_{k=1}^{B} **G**[:, k]

∂L/∂**X** = Wᵀ **G**

Notice:

- •The W gradient looks like “sum of outer products” across the batch.
- •The bias gradient sums along the batch dimension.

### Modular backprop: layers as reusable nodes

Deep learning frameworks implement layers/modules that each provide:

- •forward(input) → output
- •backward(upstream\_grad) → input\_grad and parameter\_grads

This is exactly the node-local backward rule, just grouped into a bigger node.

Common modules:

- •Linear / Dense
- •Convolution
- •BatchNorm / LayerNorm
- •Attention blocks

Even when the module is complicated, its backward pass follows the same idea:

- •accept upstream gradient
- •multiply by local derivatives (often involving cached forward stats)
- •return gradients to its inputs and parameters

### Why caching matters (time vs memory)

Backprop needs forward intermediates. For deep nets, storing every activation can be expensive.

Two practical strategies:

1) **Store everything (standard)**

- •Faster backward
- •More memory

2) **Checkpointing / recomputation**

- •Save only some activations
- •Recompute missing ones during backward
- •Trades extra compute for reduced memory

### Exploding/vanishing gradients: a backprop perspective

Backprop multiplies many Jacobians together. For a deep chain:

∂L/∂**x** = (J₁ᵀ J₂ᵀ … Jₖᵀ) ∂L/∂**z**

If the norms of these Jacobians are often < 1, gradients shrink (vanish). If often > 1, they grow (explode).

This is why choices like:

- •careful initialization
- •normalization layers
- •residual connections
- •activation choice

matter so much. They change the effective Jacobians that backprop multiplies.

### Residual connections and “sum at merges”

A residual block often looks like:

**h** = **x** + F(**x**)

In backprop:

∂L/∂**x** = ∂L/∂**h** · ∂**h**/∂**x**

But **h** depends on **x** through two paths: identity and F.

So:

∂L/∂**x** = ∂L/∂**h** · I + (∂L/∂**h**) · ∂F/∂**x**

Meaning:

∂L/∂**x** = ∂L/∂**h** + (∂L/∂**h**)·∂F/∂**x**

The identity path contributes a clean gradient term, which helps gradients flow even if ∂F/∂**x** becomes small.

### Backprop as the engine behind “Deep Learning”

Deep architectures (CNNs, RNNs, Transformers) are essentially large computation graphs with repeated motifs.

Backprop is what makes them trainable at scale:

- •Efficient gradients for millions/billions of parameters
- •Clear modular implementation (local backward rules)
- •Compatibility with GPU/TPU linear algebra

Once you are comfortable with δ propagation and reverse traversal, you’re ready to reason about:

- •why certain architectures are stable
- •why certain losses simplify gradients (e.g., softmax + cross-entropy)
- •how to debug shape mistakes in backward passes

That is the bridge to the next node: deeper architectures and the systems that train them.

## Worked Examples (3)

### Example 1: Scalar computation graph with a merge (explicit δ propagation)

Let x and y be scalars. Define:

1) u = x·y

2) v = u + y

3) L = v²

Compute ∂L/∂x and ∂L/∂y using backprop (node-local rules + reverse traversal).

1. Forward pass:

   - •u = x·y
   - •v = u + y
   - •L = v²
2. Initialize backward:

   - •∂L/∂L = 1

   Work from L backward.
3. Backprop through L = v²:

   - •∂L/∂v = 2v
4. Backprop through v = u + y:

   Local partials: ∂v/∂u = 1, ∂v/∂y = 1

   So:

   - •∂L/∂u = ∂L/∂v · 1 = 2v
   - •Contribution to ∂L/∂y (path via v) is: (∂L/∂v)·1 = 2v
5. Backprop through u = x·y:

   Local partials: ∂u/∂x = y, ∂u/∂y = x

   So:

   - •∂L/∂x = ∂L/∂u · y = (2v)·y
   - •Contribution to ∂L/∂y (path via u) is: ∂L/∂u · x = (2v)·x
6. Sum contributions at the merge for y:

   - •∂L/∂y = (2v) + (2v·x)

   = 2v(1 + x)

   And ∂L/∂x = 2v·y, where v = u + y = xy + y = y(x+1).

**Insight:** The only global coordination is the reverse traversal and the “add at merges” rule. Everything else is local: multiply the upstream gradient by a local derivative.

### Example 2: One hidden-layer network (vectorized) and the classic δ recurrence

Consider a 2-layer (one hidden layer) network for a single example:

- •**z**¹ = W¹**x** + **b**¹
- •**a**¹ = φ(**z**¹)
- •**z**² = W²**a**¹ + **b**²
- •**a**² = **z**² (identity output)

Loss: L = ½‖**a**² − **y**‖²

Derive ∂L/∂W², ∂L/∂**b**², ∂L/∂W¹, ∂L/∂**b**¹ using δ notation.

1. Start at the loss:

   L = ½‖**a**² − **y**‖²

   So:

   ∂L/∂**a**² = **a**² − **y**
2. Output is identity: **a**² = **z**²

   Therefore:

   **δ**² := ∂L/∂**z**² = ∂L/∂**a**² = **a**² − **y**
3. Backprop through **z**² = W²**a**¹ + **b**² using the affine rules with upstream gradient **δ**²:

   ∂L/∂W² = **δ**² (**a**¹)ᵀ

   ∂L/∂**b**² = **δ**²

   ∂L/∂**a**¹ = (W²)ᵀ **δ**²
4. Backprop through **a**¹ = φ(**z**¹):

   **δ**¹ := ∂L/∂**z**¹ = (∂L/∂**a**¹) ⊙ φ′(**z**¹)

   So:

   **δ**¹ = ((W²)ᵀ **δ**²) ⊙ φ′(**z**¹)
5. Backprop through **z**¹ = W¹**x** + **b**¹:

   ∂L/∂W¹ = **δ**¹ **x**ᵀ

   ∂L/∂**b**¹ = **δ**¹

   And (if needed) ∂L/∂**x** = (W¹)ᵀ **δ**¹

**Insight:** Backprop for layered networks is just repeated application of two templates: (1) affine backward, (2) activation backward. The δ vectors store exactly the sensitivities you need to reuse.

### Example 3: Softmax + cross-entropy gives δ = \*\*p\*\* − \*\*y\*\*

Let logits **z** ∈ ℝ^K. Softmax probabilities: pᵢ = exp(zᵢ) / ∑ⱼ exp(zⱼ).

Cross-entropy loss with one-hot **y**: L = −∑ᵢ yᵢ log pᵢ.

Show that ∂L/∂**z** = **p** − **y**.

1. Rewrite the loss in a convenient form.

   Since log pᵢ = zᵢ − log(∑ⱼ exp(zⱼ)), we have:

   L = −∑ᵢ yᵢ[zᵢ − log(∑ⱼ exp(zⱼ))]

   = −∑ᵢ yᵢ zᵢ + (∑ᵢ yᵢ) log(∑ⱼ exp(zⱼ))
2. For one-hot (or any distribution label), ∑ᵢ yᵢ = 1, so:

   L = −∑ᵢ yᵢ zᵢ + log(∑ⱼ exp(zⱼ))
3. Differentiate w.r.t. z\_k:

   ∂/∂z\_k [−∑ᵢ yᵢ zᵢ] = −y\_k
4. Differentiate the log-sum-exp term:

   Let S = ∑ⱼ exp(zⱼ)

   Then:

   ∂/∂z\_k [log S] = (1/S) · ∂S/∂z\_k

   And:

   ∂S/∂z\_k = exp(z\_k)

   So:

   ∂/∂z\_k [log(∑ⱼ exp(zⱼ))] = exp(z\_k) / ∑ⱼ exp(zⱼ) = p\_k
5. Combine terms:

   ∂L/∂z\_k = p\_k − y\_k

   Stacking all k gives:

   ∂L/∂**z** = **p** − **y**

**Insight:** This simplification is why softmax + cross-entropy is so popular: it produces a clean starting sensitivity at the logits, avoiding an extra Jacobian factor.

## Key Takeaways

- ✓

  Backpropagation is reverse-mode differentiation on a computation graph: forward computes values; backward computes gradients.
- ✓

  The atomic operation is the node-local backward rule: given ∂L/∂z, compute ∂L/∂(inputs) using local partial derivatives.
- ✓

  Reverse traversal (reverse topological order) ensures every node’s upstream gradient is available before using it.
- ✓

  When a variable influences the loss through multiple forward paths, its gradients from each path add: ∂L/∂x = ∑ paths (contribution).
- ✓

  Sensitivities δⱼ := ∂L/∂zⱼ (and layerwise **δ**ˡ) are the reusable quantities that make gradient computation efficient.
- ✓

  For affine layers **z** = W**x** + **b**, the core backward identities are ∂L/∂W = **g****x**ᵀ, ∂L/∂**b** = **g**, ∂L/∂**x** = Wᵀ**g**.
- ✓

  Softmax + cross-entropy yields a particularly simple gradient: ∂L/∂**z** = **p** − **y**.
- ✓

  Backprop’s efficiency (≈ one extra forward pass worth of compute) is what makes deep learning practical.

## Common Mistakes

- ✗

  Forgetting to sum gradient contributions at merges (e.g., residual connections or reused tensors), leading to gradients that are too small.
- ✗

  Mismatching tensor shapes/transposes in affine backward rules (common bug: using **x****g**ᵀ instead of **g****x**ᵀ).
- ✗

  Confusing pre-activation **z** and activation **a** when applying φ′: you need φ′(**z**) (or an equivalent expression using cached **a**).
- ✗

  Dropping batch reductions: bias gradients typically require summing over the batch dimension (and sometimes spatial dimensions in CNNs).

## Practice

easy

Scalar backprop practice: Let a = x + y, b = x·a, L = b². Compute ∂L/∂x and ∂L/∂y in terms of x and y.

**Hint:** Work backward: L→b→(x,a) and a→(x,y). Remember that x influences b both directly and through a, so you must add contributions for ∂L/∂x.

Show solution

Forward:

a = x + y

b = x·a = x(x+y)

L = b²

Backward:

∂L/∂b = 2b

For b = x·a:

∂b/∂x = a, ∂b/∂a = x

So contributions:

∂L/∂x (via b direct) = (2b)·a

∂L/∂a = (2b)·x

For a = x + y:

∂a/∂x = 1, ∂a/∂y = 1

So:

Contribution to ∂L/∂x (via a) = ∂L/∂a · 1 = (2b)x

∂L/∂y = ∂L/∂a · 1 = (2b)x

Add for x:

∂L/∂x = 2b·a + 2b·x = 2b(a + x)

Substitute a = x+y and b = x(x+y):

∂L/∂x = 2x(x+y)[(x+y)+x] = 2x(x+y)(2x+y)

∂L/∂y = 2x·b = 2x·x(x+y) = 2x²(x+y)

medium

Affine + ReLU layer: **z** = W**x** + **b**, **a** = ReLU(**z**). Suppose the upstream gradient is **g** = ∂L/∂**a**. Derive expressions for ∂L/∂W, ∂L/∂**b**, and ∂L/∂**x** using **g** and cached **z**.

**Hint:** First convert **g** into **δ** = ∂L/∂**z** by multiplying by the ReLU mask 𝟙[z>0]. Then use affine backward rules.

Show solution

ReLU backward (elementwise):

**δ** := ∂L/∂**z** = **g** ⊙ 𝟙[**z**>0]

Affine backward with upstream **δ**:

∂L/∂W = **δ** **x**ᵀ

∂L/∂**b** = **δ**

∂L/∂**x** = Wᵀ **δ**

hard

Show the merge-sum rule in vector form: Let **h** = **x** + F(**x**) where F: ℝ^n → ℝ^n is differentiable. Given upstream gradient **u** = ∂L/∂**h**, express ∂L/∂**x** in terms of **u** and the Jacobian J\_F = ∂F/∂**x**.

**Hint:** Treat **h** as two paths from **x**: identity and F. The derivative of identity is I. Use vector-Jacobian products appropriate for reverse-mode.

Show solution

We have **h**(**x**) = **x** + F(**x**).

The Jacobian is:

∂**h**/∂**x** = I + J\_F

Reverse-mode uses a vector-Jacobian product:

∂L/∂**x** = (∂**h**/∂**x**)ᵀ **u**

= (I + J\_F)ᵀ **u**

= Iᵀ **u** + J\_Fᵀ **u**

= **u** + J\_Fᵀ **u**

This is exactly “sum contributions at the merge”: the identity path contributes **u**, and the F path contributes J\_Fᵀ **u**.

## Connections

Unlocks: [Deep Learning](/tech-tree/deep-learning/)

Related prerequisite refreshers:

- •[Neural Networks](/tech-tree/neural-networks/)
- •[Multivariable Chain Rule](/tech-tree/multivariable-chain-rule/)

Next good companions (often adjacent in a tech tree):

- •[Automatic Differentiation](/tech-tree/automatic-differentiation/)
- •[Optimization (SGD/Adam)](/tech-tree/optimization/)
- •[Initialization and Gradient Flow](/tech-tree/initialization-gradient-flow/)

Quality: A (4.5/5)

[← back to tree](/tech-tree/)[browse all →](/tech-tree/inventory/)
