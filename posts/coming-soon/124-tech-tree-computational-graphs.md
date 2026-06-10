---
title: Computational Graphs
description: A representation of mathematical expressions as directed graphs where nodes are operations and edges are tensors, used to structure and execute forward and backward passes in neural network computation. They make it clear how values flow and where gradients need to be propagated for training.
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
permalink: /tech-tree/computational-graphs/
---

[←Back to Tech Tree](/tech-tree/)

[inventory](/tech-tree/inventory/)[coverage](/tech-tree/coverage/)

# Computational Graphs

Machine LearningDifficulty: ★★★☆☆Depth: 0Unlocks: 6

A representation of mathematical expressions as directed graphs where nodes are operations and edges are tensors, used to structure and execute forward and backward passes in neural network computation. They make it clear how values flow and where gradients need to be propagated for training.

## Interactive Visualization

⏮◀◀▶▶STEP0.25x1xZOOM

t=0s

## Core Concepts

- -Node-as-operation: a graph node represents a mathematical operation/function that maps input tensors to output tensors (computes values).
- -Edge-as-data: a directed edge carries a tensor/value from one node's output to another node's input and encodes dependency/ordering.
- -Reverse-mode autodiff (backprop): gradients are computed by applying the chain rule along the graph in reverse to propagate partial derivatives to inputs and parameters.

## Key Symbols & Notation

f(...) (operation/node)d/dx (gradient/derivative operator)

## Essential Relationships

- -Outputs of nodes flow forward along directed edges to become inputs of downstream nodes; gradients flow backward along those same edges using d/dx (chain rule) to compute parameter/input derivatives.

## Unlocks (3)

[Deep Learninglvl 5](/tech-tree/deep-learning/)[Automatic Differentiationlvl 4](/tech-tree/automatic-differentiation/)[Numerical Stability and Conditioninglvl 4](/tech-tree/numerical-stability/)

Advanced Learning Details

### Graph Position

6

Depth Cost

6

Fan-Out (ROI)

2

Bottleneck Score

0

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

### All Concepts (15)

- - Computational graph: representing a computation as a directed graph G = (V, E)
- - Node-as-operation: each node in the graph denotes a primitive operation (e.g., add, multiply, matmul, ReLU)
- - Edge-as-tensor: each directed edge carries a tensor (the value output by one node and consumed by another)
- - Tensor: a multidimensional numeric array that flows along edges
- - Forward pass: evaluating the graph in dependency order to produce outputs from inputs
- - Backward pass (reverse-mode automatic differentiation / backpropagation): traversing the graph to compute gradients of a scalar loss w.r.t. intermediate tensors and parameters
- - Local gradient: the derivative(s) of a node's outputs with respect to its inputs (node-level derivative)
- - Gradient accumulation: when a tensor feeds multiple downstream nodes, its incoming gradient contributions are combined (summed) during backprop
- - Parameter node: a node whose value is a learnable parameter (weight) and for which gradients are computed to perform updates
- - Loss node: a distinguished scalar output (the objective) that is the starting point for gradient propagation
- - Topological ordering: an order of nodes consistent with dependencies used to schedule the forward evaluation
- - Reverse ordering: the backward scheduling is the reverse of a topological order
- - Gradient flow vs. value flow: during backward pass gradients propagate opposite the forward dataflow
- - Activation storage requirement: intermediate outputs (activations) must be retained (or recomputed) to compute local gradients during backprop
- - Graph encodes computational dependencies and enables automated, compositional computation of derivatives

### Teaching Strategy

Deep-dive lesson - accessible entry point but dense material. Use worked examples and spaced repetition.

Neural networks look like “layers”, but training them is really about one thing: computing lots of derivatives efficiently and correctly. Computational graphs are the picture (and data structure) that makes both the forward computation and the backward (gradient) computation explicit—so we can automate learning.

TL;DR:

A computational graph represents a function as a directed graph: nodes are operations f(…), edges carry tensors (values). A forward pass evaluates node outputs in dependency order. A backward pass (reverse-mode autodiff / backprop) propagates gradients from outputs to inputs using the chain rule, accumulating contributions when a value fans out to multiple consumers.

## What Is a Computational Graph?

A **computational graph** is a directed graph that represents how a mathematical expression (or program) computes its outputs from its inputs.

Why we need this picture at all:

- •Real ML models aren’t a single formula you write once; they’re **programs** that combine many operations.
- •Training means adjusting parameters to reduce a loss, which requires **gradients** (derivatives).
- •The chain rule tells us how to combine derivatives, but doing it by hand for a big model is impractical.

A computational graph makes two things explicit:

1) **Data flow** (forward computation): how numbers/tensors are produced.

2) **Dependency structure** (for derivatives): which intermediate values influence which outputs.

### The two core roles: nodes and edges

- •**Node-as-operation**: each node is an operation/function f(…) that maps input tensors to output tensors.
- •Examples: add, multiply, matrix multiply, sin, exp, log, reshape, convolution, ReLU.
- •**Edge-as-data**: each directed edge carries a tensor (a value) from an operation’s output to another operation’s input.
- •The direction encodes “must be computed before” and “is needed by.”

This is the key mental model:

- •**Edges are values**.
- •**Nodes transform values**.

### A tiny example (scalar)

Suppose we define

z = (x + y) · y

We can break this into intermediate values:

- •a = x + y
- •z = a · y

Graphically (conceptually): x and y flow into “+” producing a, and then a and y flow into “×” producing z.

Even at this size, the graph is useful because it tells us:

- •Forward order: compute a, then z.
- •For gradients: z depends on x through a; z depends on y both directly (the multiply) and indirectly (through a). That “two paths” idea is exactly where accumulation comes from during backprop.

### Tensors, not just scalars

In ML, edges typically carry vectors/matrices/tensors. We’ll use **v** for vectors and uppercase like W for matrices.

- •Example: **y** = ReLU(W **x** + **b**)
- •Here W **x** is a matrix-vector multiply node.
- •Adding **b** is an add node.
- •ReLU is a nonlinearity node.

The graph doesn’t care whether values are scalars or tensors; it’s the same idea. The only difference is that “derivatives” become vector-Jacobian and Jacobian-vector products under the hood.

### Why graphs are central in deep learning frameworks

Computational graphs are the backbone of systems like PyTorch, JAX, and TensorFlow.

They enable:

- •**Automatic differentiation** (compute gradients automatically)
- •**Scheduling** (execute ops in the right order)
- •**Optimization** (fuse ops, reuse memory, place ops on GPU/TPU)
- •**Debugging** (inspect intermediate tensors)

You can think of a computational graph as the “assembly language” of differentiable programs: explicit enough to analyze, optimize, and differentiate.

## Core Mechanic 1: Forward Pass — Values Flow Along Edges

The forward pass is simply: evaluate every node in an order that respects dependencies.

### Why forward order matters

If node B uses the output of node A, then A must run before B. This is a partial order induced by the directed edges.

Most computational graphs used for standard feed-forward neural networks are **acyclic** (a DAG: directed acyclic graph). For a DAG, a **topological ordering** exists.

- •In practice, frameworks execute nodes in a topological order (or something equivalent).

### Example: a small DAG

Let

u = x · y

w = sin(ν)

z = w + y

Dependencies:

- •ν depends on x, y
- •w depends on ν
- •z depends on w, y

A valid forward order is: compute ν → w → z.

### What is stored during forward?

Here is a subtle but important point: for backprop, you typically need some intermediate values.

- •Example: if w = sin(ν), then ∂w/∂ν = cos(ν). You need ν to evaluate cos(ν).

So most autodiff systems either:

- •**Store** intermediate tensors from forward (a “tape”), or
- •**Recompute** them later (checkpointing) to save memory.

This leads to a core engineering trade-off:

| Strategy | What you store | Memory | Extra compute | Common use |
| --- | --- | --- | --- | --- |
| Store intermediates | ν, w, … | higher | low | default training |
| Recompute (checkpoint) | fewer values | lower | higher | very deep nets |

### Multiple consumers (fan-out)

A single node output may feed many later nodes. That means:

- •In forward: compute once, reuse many times.
- •In backward: gradients flowing “back” from multiple children must be **summed**.

Example:

- •a = x + y
- •z = a · y
- •u = a²
- •L = z + u

Here a is used in two places. During backprop, the gradient ∂L/∂a has two contributions:

- •One from z
- •One from u

You add them because the total derivative is linear in contributions from different paths.

### Shapes are part of the contract

Edges carry tensors with shapes. Each node must obey shape rules.

- •If W is (m×n) and **x** is (n,), then W **x** is (m,).
- •If **b** is (m,), then W **x** + **b** is (m,) (broadcasting rules may apply).

Computational graphs make shape mismatches easier to catch because every edge has a well-defined produced tensor.

### Takeaway

Forward mode is “just computation,” but the graph clarifies:

- •Which values depend on which
- •What intermediate values are needed later
- •Where values are reused
- •Where shapes must match

That clarity becomes crucial when we reverse direction and compute gradients.

## Core Mechanic 2: Backward Pass — Reverse-Mode Autodiff (Backprop) on the Graph

Training needs gradients: if L is a loss and θ are parameters, we want ∂L/∂θ.

### Why reverse-mode?

In deep learning, we usually have:

- •Many parameters θ (millions)
- •A single scalar loss L

Reverse-mode autodiff computes all ∂L/∂θ in about the cost of a small constant multiple of the forward pass. That’s why it’s the default for neural nets.

### Local derivatives + chain rule

Each node performs an operation. Backprop works by combining:

1) An **upstream gradient**: how the loss changes with respect to the node’s output.

2) A **local derivative**: how the node’s output changes with respect to its inputs.

Then it produces **downstream gradients** for each input.

If a node computes

u = f(a)

then by the chain rule:

dL/da = (dL/dν) · (dν/da)

In graph terms:

- •You start with dL/dL = 1 at the loss node.
- •You propagate gradients backward along edges.

### A concrete scalar derivation

Let

a = x + y

z = a · y

Assume L = z (so L = (x + y) · y).

Forward:

- •a = x + y
- •L = z = a · y

Backward:

- •Start: dL/dz = 1
- •For z = a · y:
- •dz/da = y
- •dz/dy = a

So:

- •dL/da = dL/dz · dz/da = 1 · y = y
- •dL/dy (from this node) = dL/dz · dz/dy = 1 · a = a
- •For a = x + y:
- •da/dx = 1
- •da/dy = 1

So:

- •dL/dx = dL/da · da/dx = y · 1 = y
- •dL/dy (additional contribution) = dL/da · da/dy = y · 1 = y

Now combine contributions to y (because y influenced L via two paths):

dL/dy = a + y = (x + y) + y = x + 2y

This “sum the contributions at fan-out” rule is one of the most important operational facts about backprop.

### Gradient accumulation at merges

Whenever an edge’s value is used in multiple places, its gradient is the sum of gradients coming back from each usage.

Operationally, frameworks maintain an accumulator for each node output:

- •Initialize grads to 0
- •As each consumer backpropagates, add into the accumulator
- •When all consumers have contributed, backprop through the node

### Vector/tensor intuition (without heavy Jacobians)

For tensors, the same idea holds but with appropriate linear algebra.

Example: **y** = W **x**

- •**x** ∈ ℝⁿ, W ∈ ℝᵐˣⁿ, **y** ∈ ℝᵐ

If we have upstream gradient **g** = dL/d**y** (a vector in ℝᵐ), then:

- •dL/d**x** = Wᵀ **g**
- •dL/dW = **g** **x**ᵀ

You don’t need to explicitly form Jacobians; backprop uses efficient vector-Jacobian products.

### Reverse traversal order

To compute gradients correctly, you need to process nodes in reverse topological order (from outputs back to inputs). In a DAG, this is well-defined.

### What about branches and shared subgraphs?

Branches are fine; they just introduce multiple gradient contributions that must sum.

Shared subgraphs (reuse) are also fine; they are exactly “fan-out.”

### What about cycles (RNNs)?

Some models have logical cycles (recurrent connections). Training still uses backprop by **unrolling** the cycle over time steps, yielding a larger DAG.

- •This is “backpropagation through time” (BPTT)

### Takeaway

Reverse-mode autodiff is “the chain rule on a graph”:

- •Each node knows how to compute local derivatives.
- •The framework routes and accumulates gradients along edges.
- •The full gradient emerges from many local, composable steps.

## Application/Connection: How Computational Graphs Power Deep Learning Practice

Computational graphs aren’t just a conceptual tool; they determine how training runs on real hardware.

### 1) Defining models as graphs

A neural net layer is a subgraph pattern:

- •Linear layer: **h** = W **x** + **b**
- •Nonlinearity: **y** = ReLU(**h**)

Stacking layers composes graphs.

A whole training step includes:

1) Forward pass to compute predictions and loss L

2) Backward pass to compute gradients ∂L/∂θ

3) Parameter update (e.g., θ ← θ − η ∂L/∂θ)

That’s “forward graph” + “backward graph” + “optimizer graph.”

### 2) Debugging: you can localize problems

If gradients are NaN or 0, a graph helps you ask:

- •Which node first produced NaN?
- •Where do values saturate (e.g., sigmoid) and kill gradients?
- •Where does an overflow occur (e.g., exp)?

This connects directly to numerical stability: many stability tricks (like log-sum-exp) are specific subgraph rewrites.

### 3) Performance: graphs enable optimizations

Once computation is explicit, systems can:

- •Fuse ops: combine several nodes into one kernel
- •Reorder when safe
- •Precompute constants
- •Use mixed precision

The graph is also used for device placement:

- •Put matrix multiplies on GPU
- •Keep small control logic on CPU

### 4) Static vs dynamic graphs (conceptual comparison)

Different frameworks expose graphs differently.

| Style | How graph is built | Pros | Cons | Examples |
| --- | --- | --- | --- | --- |
| Static graph | define graph, then run | global optimization, easier deployment | less flexible debugging, control flow harder | TF 1.x, XLA-compiled graphs |
| Dynamic graph | graph created as code runs | very flexible, Pythonic debugging | fewer global optimizations unless compiled | PyTorch eager, JAX tracing (hybrid) |

Modern systems blur the line (e.g., torch.compile, JAX jit): write dynamic code, then trace/compile into a more static graph for speed.

### 5) Connecting forward/backward to learning

A central reason computational graphs matter is that learning signals (gradients) follow the same dependency paths as values—but reversed.

- •If a parameter θ doesn’t influence L in the forward graph, then ∂L/∂θ = 0.
- •If a parameter influences L through many paths, gradients add.

That provides a practical “sanity check” when designing architectures.

### 6) Where this node unlocks next

- •**Deep Learning**: architectures are just larger computational graphs with repeated motifs.
- •**Automatic Differentiation**: computational graphs are the core data structure behind forward-mode and reverse-mode AD.
- •**Numerical Stability and Conditioning**: stability fixes are often graph-level transformations (rewrite a subgraph to avoid overflow/underflow).

Computational graphs are the map; autodiff is the navigation algorithm; deep learning is the city you can now traverse.

## Worked Examples (3)

### Example 1: Backprop on a Small Scalar Graph with a Branch (Fan-out)

Define a computational graph with

u = x + y

z = u · y

w = u²

L = z + w

Goal: compute dL/dx and dL/dy using the graph + chain rule.

1. Forward compute intermediate values:

   - •u = x + y
   - •z = u · y
   - •w = u²
   - •L = z + w
2. Initialize gradient at the output:

   - •dL/dL = 1

   Because L = z + w, local derivatives are:

   - •dL/dz = 1
   - •dL/dw = 1
3. Backprop through w = u²:

   - •dw/du = 2u

   So contribution to u from this path:

   - •dL/du |\_from\_w = dL/dw · dw/du = 1 · 2u = 2u
4. Backprop through z = u · y:

   Local derivatives:

   - •dz/du = y
   - •dz/dy = u

   So:

   - •dL/du |\_from\_z = dL/dz · dz/du = 1 · y = y
   - •dL/dy |\_from\_z = dL/dz · dz/dy = 1 · u = u
5. Accumulate gradients at u (fan-out merge):

   - •dL/du = (dL/du |\_from\_w) + (dL/du |\_from\_z)
   - •dL/du = 2u + y
6. Backprop through u = x + y:

   Local derivatives:

   - •du/dx = 1
   - •du/dy = 1

   So:

   - •dL/dx = dL/du · du/dx = (2u + y) · 1 = 2u + y
   - •dL/dy |\_from\_u = dL/du · du/dy = (2u + y) · 1 = 2u + y
7. Accumulate total gradient for y (two paths):

   - •dL/dy = (dL/dy |\_from\_z) + (dL/dy |\_from\_u)
   - •dL/dy = u + (2u + y) = 3u + y
8. Substitute u = x + y:

   - •dL/dx = 2(x + y) + y = 2x + 3y
   - •dL/dy = 3(x + y) + y = 3x + 4y

**Insight:** Whenever a value is used by multiple later operations (fan-out), its gradient is the sum of gradients flowing back along each outgoing path. This is the graph version of “collect all chain rule paths and add them.”

### Example 2: Vector Computational Graph for a Linear Layer + Squared Error

Let **x** ∈ ℝⁿ, W ∈ ℝᵐˣⁿ, **b** ∈ ℝᵐ, target **t** ∈ ℝᵐ.

Define:

- •**y** = W **x** + **b**
- •L = 1/2 ‖**y** − **t**‖²

Compute gradients dL/d**y**, dL/dW, dL/d**b**, dL/d**x**.

1. Rewrite loss with an intermediate:

   Let **e** = **y** − **t**.

   Then L = 1/2 ‖**e**‖² = 1/2 ∑ᵢ eᵢ².
2. Compute gradient w.r.t. **e**:

   For each component, ∂L/∂eᵢ = 1/2 · 2eᵢ = eᵢ.

   So in vector form:

   - •dL/d**e** = **e**.
3. Backprop through **e** = **y** − **t**:

   - •∂**e**/∂**y** is identity, and **t** is constant.

   So:

   - •dL/d**y** = dL/d**e** = **e** = (**y** − **t**).
4. Backprop through **y** = W **x** + **b**:

   Split into two nodes: **u** = W **x**, then **y** = **u** + **b**.

   Upstream gradient is **g** = dL/d**y**.

   For **y** = **u** + **b**:

   - •dL/d**u** = **g**
   - •dL/d**b** = **g**

   For **u** = W **x**:

   Using matrix calculus identities:

   - •dL/dW = **g** **x**ᵀ
   - •dL/d**x** = Wᵀ **g**
5. Optionally substitute **g** = (**y** − **t**) and **y** = W **x** + **b**:

   - •dL/d**b** = W **x** + **b** − **t**
   - •dL/dW = (W **x** + **b** − **t**) **x**ᵀ
   - •dL/d**x** = Wᵀ (W **x** + **b** − **t**)

**Insight:** Computational graphs scale because each node only needs a local backward rule (like for + or matmul). Reverse-mode AD stitches those local rules into full gradients without ever building a giant Jacobian explicitly.

### Example 3: A Numerically Sensitive Subgraph and a Stable Rewrite (Softmax + Log)

Consider probabilities from logits **s** ∈ ℝᵏ via softmax:

- •softmax(**s**)ᵢ = exp(sᵢ) / ∑ⱼ exp(sⱼ)

If you then compute log-prob for class c:

- •L = −log(softmax(**s**)꜀)

Show how the computational graph suggests a stable rewrite using log-sum-exp.

1. Start from the definition:

   softmax(**s**)꜀ = exp(s꜀) / ∑ⱼ exp(sⱼ)

   So:

   L = −log(exp(s꜀) / ∑ⱼ exp(sⱼ)).
2. Use log rules:

   L = −(log(exp(s꜀)) − log(∑ⱼ exp(sⱼ)))

   = −(s꜀ − log(∑ⱼ exp(sⱼ)))

   = log(∑ⱼ exp(sⱼ)) − s꜀.
3. Identify numerical issue in the original graph:

   The naive path computes exp(sⱼ) which can overflow if some sⱼ is large.

   Graph insight: the problematic node is exp(·) applied to raw logits.
4. Apply the log-sum-exp trick by subtracting m = maxⱼ sⱼ:

   ∑ⱼ exp(sⱼ) = ∑ⱼ exp((sⱼ − m) + m)

   = exp(m) ∑ⱼ exp(sⱼ − m)

   So:

   log(∑ⱼ exp(sⱼ)) = log(exp(m) ∑ⱼ exp(sⱼ − m))

   = m + log(∑ⱼ exp(sⱼ − m)).
5. Final stable expression:

   Let m = maxⱼ sⱼ.

   Then:

   L = (m + log(∑ⱼ exp(sⱼ − m))) − s꜀.

   All exponentials now see inputs (sⱼ − m) ≤ 0, reducing overflow risk.

**Insight:** Computational graphs aren’t just for gradients; they help you spot unstable subgraphs (like exp feeding into sums and logs) and replace them with equivalent but stable subgraphs.

## Key Takeaways

- ✓

  A computational graph represents a function/program as a directed graph: nodes are operations f(…), edges carry tensors (values) and encode dependencies.
- ✓

  The forward pass evaluates nodes in a dependency-respecting order (often a topological order in a DAG).
- ✓

  Reverse-mode autodiff (backprop) computes gradients by propagating upstream gradients backward through nodes using local derivatives and the chain rule.
- ✓

  When a value fans out to multiple consumers, its gradient is the sum of contributions from each path (gradient accumulation).
- ✓

  For tensor operations, backprop uses efficient vector-Jacobian products (e.g., dL/d**x** = Wᵀ dL/d**y**) rather than forming full Jacobians.
- ✓

  Graphs enable practical system features: saving intermediates, checkpointing, scheduling, kernel fusion, and device placement.
- ✓

  Many numerical stability techniques can be seen as graph rewrites (e.g., log-sum-exp for softmax-related computations).

## Common Mistakes

- ✗

  Forgetting to accumulate gradients at fan-out points (overwriting instead of summing contributions).
- ✗

  Confusing the direction of data flow (forward) with the direction of gradient flow (backward) and mixing up which quantity is “upstream.”
- ✗

  Dropping needed forward intermediates (e.g., ν for cos(ν)) and then being unable to compute local derivatives correctly without recomputation.
- ✗

  Ignoring tensor shapes/broadcasting rules, leading to silent shape errors or incorrect gradient shapes.

## Practice

easy

Let a = x · y, b = a + y, L = b². Compute dL/dx and dL/dy.

**Hint:** Do forward intermediates a, b. Backprop from L to b to (a, y) and then to (x, y). Remember y affects b both directly and via a.

Show solution

Forward:

a = x y

b = a + y = x y + y = y(x + 1)

L = b²

Backward:

dL/db = 2b

For b = a + y:

- •db/da = 1 ⇒ dL/da = 2b
- •db/dy = 1 ⇒ contribution to dL/dy is 2b

For a = x y:

- •da/dx = y ⇒ dL/dx = dL/da · y = (2b) y = 2by
- •da/dy = x ⇒ additional contribution to dL/dy is dL/da · x = (2b)x

Total:

dL/dx = 2by

dL/dy = 2b + 2bx = 2b(1 + x)

Substitute b = y(x + 1):

dL/dx = 2 y(x + 1) · y = 2 y² (x + 1)

dL/dy = 2 y(x + 1) (1 + x) = 2 y (x + 1)²

medium

Consider **y** = ReLU(W **x** + **b**) and loss L = ∑ᵢ yᵢ (sum of outputs). Express dL/dW in terms of **x** and a mask derived from the pre-activation **h** = W **x** + **b**.

**Hint:** Use dL/d**y** = **1** (vector of ones). ReLU’(**h**) is 1 where hᵢ > 0 else 0. Then dL/dW looks like an outer product.

Show solution

Let **h** = W **x** + **b**, **y** = ReLU(**h**).

Given L = ∑ᵢ yᵢ, we have dL/d**y** = **1** (all ones).

Backprop through ReLU:

Define mask **m** where mᵢ = 1 if hᵢ > 0 else 0.

Then dL/d**h** = dL/d**y** ⊙ **m** = **1** ⊙ **m** = **m**.

Backprop through **h** = W **x** + **b**:

For matrix multiply, dL/dW = (dL/d**h**) **x**ᵀ = **m** **x**ᵀ.

So dL/dW is an outer product of the ReLU mask with the input **x**.

hard

A value u feeds into two branches: v = u² and w = 3u. The final output is L = v · w. Compute dL/du by treating it as a computational graph and showing the gradient accumulation clearly.

**Hint:** Compute dL/dv and dL/dw first from L = v w. Then push back to u through each branch and add.

Show solution

Forward:

v = u²

w = 3u

L = v w

Backward:

From L = v w:

- •dL/dv = w
- •dL/dw = v

Backprop through v = u²:

- •dv/du = 2u

So contribution:

dL/du |\_via\_v = dL/dv · dv/du = w · 2u

Backprop through w = 3u:

- •dw/du = 3

So contribution:

dL/du |\_via\_w = dL/dw · dw/du = v · 3

Accumulate at u:

dL/du = (w · 2u) + (v · 3)

Substitute v = u² and w = 3u:

dL/du = (3u · 2u) + (u² · 3)

= 6u² + 3u²

= 9u².

## Connections

Next nodes you can study:

- •[Deep Learning](/tech-tree/deep-learning/)
- •[Automatic Differentiation](/tech-tree/automatic-differentiation/)
- •[Numerical Stability and Conditioning](/tech-tree/numerical-stability/)

Related conceptual building blocks:

- •[Gradient Descent](/tech-tree/gradient-descent/)
- •[Linear Algebra Basics](/tech-tree/linear-algebra-basics/)
- •[Chain Rule](/tech-tree/chain-rule/)

Quality: A (4.6/5)

[← back to tree](/tech-tree/)[browse all →](/tech-tree/inventory/)
