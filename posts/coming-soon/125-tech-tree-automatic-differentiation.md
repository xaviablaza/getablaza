---
title: Automatic Differentiation
description: An algorithmic technique to compute exact derivatives of functions expressed as programs by applying the chain rule systematically (forward- or reverse-mode), which underlies efficient backpropagation in modern frameworks. Knowing AD helps in understanding gradient computation costs and implementation choices.
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
permalink: /tech-tree/automatic-differentiation/
---

[←Back to Tech Tree](/tech-tree/)

[inventory](/tech-tree/inventory/)[coverage](/tech-tree/coverage/)

# Automatic Differentiation

AlgorithmsDifficulty: ★★★★☆Depth: 1Unlocks: 4

An algorithmic technique to compute exact derivatives of functions expressed as programs by applying the chain rule systematically (forward- or reverse-mode), which underlies efficient backpropagation in modern frameworks. Knowing AD helps in understanding gradient computation costs and implementation choices.

## Interactive Visualization

⏮◀◀▶▶STEP0.25x1xZOOM

t=0s

## Core Concepts

- -Systematic application of the chain rule to a recorded sequence of primitive operations (the program trace).
- -Forward-mode (tangent) propagation: compute directional derivatives by pushing tangents alongside values during evaluation.
- -Reverse-mode (adjoint/backprop) propagation: compute gradients by accumulating output sensitivities backward to inputs after evaluation.

## Key Symbols & Notation

J\_f or D[f] : the Jacobian (matrix of partial derivatives) of function f

## Essential Relationships

- -The global derivative is the composition/product of local Jacobians along the computational graph; forward-mode evaluates this composition left-to-right (cost scales with number of inputs), reverse-mode evaluates sensitivities right-to-left (cost scales with number of outputs).

## Prerequisites (1)

[Computational Graphs6 atoms](/tech-tree/computational-graphs/)

## Unlocks (1)

[Deep Learninglvl 5](/tech-tree/deep-learning/)

Advanced Learning Details

### Graph Position

11

Depth Cost

4

Fan-Out (ROI)

2

Bottleneck Score

1

Chain Length

### Cognitive Load

5

Atomic Elements

30

Total Elements

L1

Percentile Level

L3

Atomic Level

### All Concepts (13)

- - Automatic Differentiation (AD) as an algorithmic technique that computes exact derivatives of programs by systematically applying the chain rule
- - Forward-mode AD (tangent-mode): propagate tangents (directional derivatives) alongside primal values through the program
- - Reverse-mode AD (adjoint-mode): propagate cotangents/adjoints backward to accumulate gradients from outputs to inputs
- - Dual numbers as an implementation idea for forward-mode (representing a value and its tangent together)
- - Tape or Wengert list: recording the sequence of elementary operations and intermediate values during execution for later backpropagation
- - Jacobian-vector product (JVP): the operation that computes J·v efficiently without forming the full Jacobian
- - Vector-Jacobian product (VJP) / pullback / adjoint: the operation that computes v·J or J^T·v efficiently
- - Operator overloading vs source-code transformation as two principal implementation strategies for AD
- - Checkpointing / recomputation strategies to trade memory for extra computation in reverse-mode AD
- - Higher-order derivatives in AD obtained by composing AD modes (e.g., forward-over-reverse, reverse-over-forward)
- - Local Jacobians (derivatives of elementary primitives) are used as building blocks in AD
- - AD’s numerical exactness: derivatives produced are exact up to machine precision (unlike finite differences)
- - Memory/time trade-offs inherent to AD implementations (e.g., storing intermediates for reverse-mode vs recomputing them)

### Teaching Strategy

Self-serve tutorial - low prerequisites, straightforward concepts.

You already know computational graphs show how values flow. Automatic differentiation (AD) is what makes those graphs *actionable*: it turns “a program that computes a number” into “a program that computes that number *and* its exact derivative”, with predictable computational cost. This is the algorithmic heart of backpropagation.

TL;DR:

Automatic differentiation computes exact derivatives of functions written as programs by systematically applying the chain rule to a trace of primitive operations. Forward-mode propagates tangents (directional derivatives) alongside values and is efficient when inputs are few. Reverse-mode propagates adjoints (sensitivities) backward and is efficient when outputs are few (e.g., scalar loss), which is why it powers backprop in deep learning.

## What Is Automatic Differentiation?

### Why AD exists (and why you should care)

When you want derivatives, you have several options:

- •**Symbolic differentiation**: manipulate algebraic expressions (like a CAS). Can produce huge expressions (“expression swell”) and struggles with control flow, loops, and code structure.
- •**Numerical differentiation** (finite differences): approximate derivatives via small perturbations. Easy to write, but introduces truncation + rounding error and can be unstable.
- •**Automatic differentiation (AD)**: *compute derivatives exactly (up to floating-point roundoff)* by applying the chain rule to the **actual sequence of operations your program executed**.

Deep learning depends on fast and reliable gradients. If your loss is a scalar ℓ and your parameters are **θ**, you typically need ∇\_**θ** ℓ. AD gives you those gradients with a cost that you can reason about.

### Definition

Let f be a function implemented as a program:

- •Inputs: **x** ∈ ℝⁿ
- •Outputs: **y** = f(**x**) ∈ ℝᵐ

The **Jacobian** is

J\_f(**x**) = D[f](**x**) = [∂yᵢ/∂xⱼ] ∈ ℝᵐˣⁿ

**Automatic differentiation** is an algorithmic technique to compute J\_f(**x**) (or products with it) by decomposing f into a sequence of primitive operations whose derivatives are known, then applying the chain rule systematically along that sequence.

### Programs, traces, and primitive operations

A key AD idea: your code (or computational graph) induces a sequence of intermediate values:

x → v₁ → v₂ → … → v\_k → y

Each step is a primitive operation like +, ×, sin, exp, matmul, etc.

Example (scalar):

f(x) = sin(x) + x²

A “trace” might look like:

- •v₁ = x
- •v₂ = sin(v₁)
- •v₃ = v₁²
- •v₄ = v₂ + v₃
- •y = v₄

AD differentiates this trace.

### “Exact” but not symbolic

AD is not algebraic simplification. It does not try to build and simplify a symbolic formula for df/dx. Instead, it evaluates derivatives *numerically*, step-by-step, using exact local derivative rules.

So the result is **exact with respect to the executed operations** (subject to floating point), and it naturally supports:

- •loops
- •branches (with caveats around nondifferentiable points)
- •modular code

### Two main modes

AD comes in two main propagation styles:

- •**Forward-mode AD**: propagate **tangents** (directional derivatives) from inputs to outputs.
- •**Reverse-mode AD**: propagate **adjoints** (sensitivities) from outputs back to inputs.

They compute different Jacobian-related objects efficiently:

| Mode | Efficiently computes | Typical use case |
| --- | --- | --- |
| Forward | J\_f(**x**) **v** (Jacobian-vector product, JVP) | Few inputs, many outputs; sensitivity in a direction |
| Reverse | **w**ᵀ J\_f(**x**) (vector-Jacobian product, VJP) | Many inputs, few outputs (often m = 1) |

Deep learning training typically has m = 1 (a scalar loss), and n can be millions of parameters. That asymmetry makes reverse-mode the star.

### AD vs “backprop”

Backpropagation is best understood as **reverse-mode AD applied to a computational graph**. The deep learning context often adds batching, tensor primitives, and GPU kernels, but the underlying algorithm is reverse-mode AD.

The main learning goal for this node: understand *what* is being propagated, *why* the two modes have different cost profiles, and *how* the chain rule is organized algorithmically.

## Core Mechanic 1: Forward-Mode AD (Tangent Propagation)

### Why forward-mode is a good first step

Forward-mode is conceptually straightforward: as you compute each intermediate value v, you also compute how v changes with respect to a chosen input direction.

Think: “If I nudge the input **x** a tiny amount along direction **u**, how does the output change?”

This is a **directional derivative**:

d/dε f(**x** + ε**u**) |\_{ε=0} = J\_f(**x**) **u**

Forward-mode computes exactly this quantity in one pass.

### Dual numbers intuition (scalar case)

A classic way to explain forward-mode is **dual numbers**. Replace a real number x with

x̂ = x + ẋ ε

where ε is a special symbol with ε² = 0 (but ε ≠ 0). Then:

- •The “real part” is the value x
- •The “ε part” carries the derivative ẋ

If you initialize ẋ = 1, then the ε coefficient at the end becomes df/dx.

Example: for multiplication,

(a + ȧ ε)(b + ḃ ε)

= ab + (a ḃ + b ȧ) ε

The ε coefficient exactly matches the product rule.

AD implementations don’t need to literally use ε, but the algebra captures the idea: **push derivative information forward alongside values**.

### Forward-mode on a trace

Suppose a program defines intermediates vᵢ = opᵢ(parents). Forward-mode maintains (vᵢ, v̇ᵢ), where v̇ᵢ is the directional derivative of vᵢ in the chosen input direction.

If vᵢ = g(vⱼ, v\_k), then by chain rule:

v̇ᵢ = (∂g/∂vⱼ) v̇ⱼ + (∂g/∂v\_k) v̇\_k

You can see the pattern: local partial derivatives times incoming tangents.

### Vector inputs: JVPs

For **x** ∈ ℝⁿ, choose a direction **u** ∈ ℝⁿ. Initialize input tangents:

**ẋ** = **u**

Run the program forward; each intermediate carries its tangent. The output tangent is:

**ẏ** = J\_f(**x**) **u**

This is a **Jacobian-vector product (JVP)**.

If you want the full Jacobian J\_f, you could run forward-mode n times with **u** = **e**ⱼ (standard basis vectors). That costs O(n) forward sweeps.

### Cost model (the key reason modes differ)

Forward-mode cost is roughly:

- •One forward evaluation of the primal values
- •Plus extra work to propagate tangents

The big scaling fact:

- •Computing one JVP costs ≈ a small constant factor times evaluating f.
- •Computing the full Jacobian by forward-mode costs ≈ n evaluations (one per input dimension).

So forward-mode is attractive when **n (inputs) is small**, even if m is large.

### Practical benefits of forward-mode

Forward-mode shines in situations like:

- •f: ℝ → ℝᵐ (one input, many outputs)
- •Computing derivatives of ODE solutions w.r.t. a small number of parameters
- •Sensitivity analysis in a particular direction (JVP)

It is also valuable in deep learning systems as a building block (for higher-order derivatives and for efficient JVP computation).

### Example of forward-mode update rules

For common scalar primitives (primal v, tangent v̇):

- •Addition: v = a + b ⇒ v̇ = ȧ + ḃ
- •Multiplication: v = ab ⇒ v̇ = ȧ b + a ḃ
- •sin: v = sin(a) ⇒ v̇ = cos(a) ȧ
- •exp: v = exp(a) ⇒ v̇ = exp(a) ȧ

For vectors/matrices, the same principles apply with appropriate linear algebra. For example, if **y** = A **x**, then ẏ = A ẋ (a linear map).

### Breathing room: what forward-mode is *not*

- •It is not finite differences (no small ε tuning)
- •It does not “differentiate the source code” into a big formula; it differentiates each executed primitive
- •It does not automatically give you the full gradient ∇\_**x** f if f is scalar and **x** is huge (that’s reverse-mode’s job)

Forward-mode sets the stage: it makes the chain rule feel like a local propagation law. Reverse-mode will use the same local derivatives but run the information in the opposite direction.

## Core Mechanic 2: Reverse-Mode AD (Adjoint/Backpropagation)

### Why reverse-mode exists

In machine learning you often have:

- •Many inputs (parameters): **θ** ∈ ℝⁿ with n large
- •One output (loss): ℓ = f(**θ**) ∈ ℝ

You want ∇\_**θ** ℓ, i.e., all ∂ℓ/∂θⱼ.

Forward-mode would require n separate passes (one per θⱼ direction). Reverse-mode computes *all* partials in about the cost of a small constant times one evaluation of f.

### The central object: adjoints

Reverse-mode defines, for each intermediate vᵢ, an **adjoint** (also called sensitivity):

v̄ᵢ = ∂ℓ/∂vᵢ

Read it as: “how much does the final scalar output ℓ change if vᵢ changes?”

This is *exactly* what backprop stores as “gradients with respect to activations.”

### Local chain rule as a pullback

Suppose an intermediate is computed by

vᵢ = g(vⱼ, v\_k)

Given v̄ᵢ, we can distribute it to parents:

v̄ⱼ += v̄ᵢ · ∂vᵢ/∂vⱼ

v̄\_k += v̄ᵢ · ∂vᵢ/∂v\_k

This is the chain rule written in an accumulation form.

Important: the “+=” is not decoration. If a variable feeds into multiple downstream paths, its total sensitivity is the **sum** of contributions from each path.

### Reverse-mode algorithm sketch

1. 1)**Forward pass**: compute and store all intermediates vᵢ needed to evaluate local derivatives later.
2. 2)**Initialize**: set output adjoint ℓ̄ = ∂ℓ/∂ℓ = 1.
3. 3)**Backward pass**: traverse operations in reverse topological order, applying local derivative rules to accumulate adjoints to inputs.

At the end, θ̄ = ∂ℓ/∂**θ** = ∇\_**θ** ℓ.

### Why storage matters

Reverse-mode needs values from the forward pass to compute local derivatives. Example:

If v = sin(a), then ∂v/∂a = cos(a). During backward, you need a (or v) to compute cos(a).

So reverse-mode typically stores (“tapes”) intermediate values.

This leads to a real implementation tradeoff:

| Strategy | Memory | Compute | Notes |
| --- | --- | --- | --- |
| Store all intermediates | High | Low | Standard backprop |
| Recompute some intermediates (checkpointing) | Lower | Higher | Useful for very deep nets |

### Reverse-mode yields VJPs

For general f: ℝⁿ → ℝᵐ, reverse-mode naturally computes

**w**ᵀ J\_f(**x**)

for a chosen output weighting **w** ∈ ℝᵐ.

When m = 1 and ℓ = f(**x**), **w** = 1 and

1ᵀ J\_f(**x**) = ∇\_**x** ℓ

So gradients are a special case of a **vector-Jacobian product (VJP)**.

### Cost model (the other key reason modes differ)

Let C be the cost of evaluating f once.

- •Reverse-mode computes ∇\_**x** ℓ with cost ≈ kC for a small constant k (often around 2–5 depending on primitives).
- •Forward-mode would need n passes to get the full gradient when n is large.

So reverse-mode is efficient when **m (outputs) is small**, especially m = 1.

### A gentle derivation on a tiny graph

Consider:

v₁ = x

v₂ = y

v₃ = v₁ v₂

v₄ = sin(v₁)

v₅ = v₃ + v₄

ℓ = v₅

Adjoints:

- •Initialize: v̄₅ = 1
- •Backprop through v₅ = v₃ + v₄:
- •v̄₃ += v̄₅ · 1 = 1
- •v̄₄ += v̄₅ · 1 = 1
- •Backprop through v₄ = sin(v₁):
- •v̄₁ += v̄₄ · cos(v₁)
- •Backprop through v₃ = v₁ v₂:
- •v̄₁ += v̄₃ · v₂
- •v̄₂ += v̄₃ · v₁

So:

∂ℓ/∂x = v̄₁ = y + cos(x)

∂ℓ/∂y = v̄₂ = x

This is the chain rule, reorganized so you reuse shared subcomputations efficiently.

### Reverse-mode is not “reverse evaluation”

A subtle but important distinction:

- •The backward pass is not trying to “undo” computations.
- •It computes *sensitivities* using local derivatives.

Even if an operation is not invertible (e.g., squaring), reverse-mode still works because it doesn’t need to invert; it needs partial derivatives.

### Nondifferentiabilities and subgradients

Real programs may include primitives like ReLU(x) = max(0, x), which is not differentiable at x = 0.

Frameworks typically define a convention (a subgradient) such as:

d/dx ReLU(x) = 0 if x < 0, 1 if x > 0, and a chosen value at x = 0 (often 0)

AD will propagate according to those primitive rules.

Reverse-mode is the workhorse for deep learning, but remember: it is one mode of a general AD idea. The real power comes from understanding both modes and the Jacobian products they compute.

## Application/Connection: Backprop, Jacobian Products, and Implementation Choices

### Backpropagation = reverse-mode AD on a computational graph

In neural networks, you define a scalar loss:

ℓ = L(model(**x**; **θ**), target)

Training needs ∇\_**θ** ℓ. The computation of ℓ is a composition of many layers, each a primitive (or a bundle of primitives). Reverse-mode AD traverses the graph backward, accumulating adjoints.

So when you see “.backward()” in a framework, it’s executing reverse-mode AD.

### Why Jacobian products matter more than Jacobians

In high dimensions, explicitly building J\_f is often impossible:

- •If n = 10⁷ parameters and m = 1, J is 1 × 10⁷ (already huge but manageable as a gradient vector).
- •If m is also large (say m = 10⁶ outputs), J would have 10¹³ entries: impossible to store.

AD avoids this by computing *products*:

- •Forward-mode: JVP = J\_f(**x**) **v**
- •Reverse-mode: VJP = **w**ᵀ J\_f(**x**)

These are enough for many algorithms:

- •gradients (VJP with **w** = 1 for scalar output)
- •Hessian-vector products (HVPs) via combinations of JVP and VJP
- •implicit differentiation and optimization methods

### Higher-order derivatives (brief but important)

If you want second derivatives, you can apply AD to an AD-produced derivative computation.

For scalar ℓ(**x**):

- •Hessian H = ∇²ℓ(**x**)
- •Often you want H **v** (HVP), not H explicitly.

A common strategy is:

1. 1)Compute g(**x**) = ∇ℓ(**x**) via reverse-mode.
2. 2)Compute J\_g(**x**) **v** via forward-mode on g.

This is “forward-over-reverse” and can compute H **v** efficiently.

### Choosing a mode: a practical rule

Let f: ℝⁿ → ℝᵐ.

- •If you want **one** directional derivative (JVP): forward-mode is natural.
- •If you want gradients of a scalar output (m = 1): reverse-mode is usually best.
- •If you want the full Jacobian:
- •forward-mode costs ~n sweeps
- •reverse-mode costs ~m sweeps

So:

| Goal | Better mode | Why |
| --- | --- | --- |
| Full Jacobian J ∈ ℝᵐˣⁿ | forward if n ≪ m, reverse if m ≪ n | One sweep per “small side” |
| Gradient of scalar ℓ | reverse | m = 1 |
| JVP | forward | computes J **v** directly |
| VJP | reverse | computes **w**ᵀ J directly |

### AD and control flow

Real programs include:

- •if/else branches
- •loops with data-dependent iteration counts

AD works by differentiating the executed trace. That means:

- •The derivative corresponds to the path actually taken.
- •At branch boundaries, the function may be nondifferentiable (like a piecewise function). AD gives the derivative of the executed piece.

This is usually what you want in ML, but it matters for correctness and debugging.

### Operator overloading vs source transformation

Implementations generally fall into two families:

| Approach | How it works | Pros | Cons |
| --- | --- | --- | --- |
| Operator overloading | Run code with special number/tensor types that record a tape | Easy to integrate with dynamic languages | Runtime overhead; tracing can be subtle |
| Source transformation | Transform the program (or IR) into a new program that computes derivatives | Can be faster; more compile-time optimization | Harder to implement; language/IR constraints |

Modern frameworks blend ideas (e.g., tracing to an IR, then compiling).

### Numerical stability: AD isn’t a magic fix

AD avoids finite-difference error, but it cannot fix a numerically unstable primal computation.

Example: if your function involves subtracting nearly equal numbers, the primal has catastrophic cancellation; the derivative will reflect that sensitivity.

So you still need good numerical practices.

### Connecting back to deep learning

Backprop is reverse-mode AD, and its efficiency is why deep learning is feasible at scale.

But understanding AD gives you extra superpowers:

- •You can predict when a gradient computation will be memory-heavy (tape size)
- •You can reason about when JVPs are cheaper than VJPs (and vice versa)
- •You can understand why some frameworks expose `jvp`, `vjp`, `grad`, `jacobian`, `hessian`

Most importantly: you stop treating gradients as “magic,” and start seeing them as a carefully organized application of the chain rule.

## Worked Examples (3)

### Forward-mode AD on a small function (compute a JVP)

Let f: ℝ² → ℝ² be

f(x₁, x₂) = (y₁, y₂)

where

y₁ = x₁ x₂ + sin(x₁)

y₂ = exp(x₂) + x₁²

Compute the Jacobian-vector product J\_f(x) **u** at x = (1, 0) along direction **u** = (2, -1).

1. Write a trace with intermediates:

   v₁ = x₁

   v₂ = x₂

   v₃ = v₁ v₂

   v₄ = sin(v₁)

   v₅ = v₃ + v₄ (this is y₁)

   v₆ = exp(v₂)

   v₇ = v₁²

   v₈ = v₆ + v₇ (this is y₂)

   We will propagate tangents v̇ᵢ.
2. Initialize primals at x = (1, 0):

   v₁ = 1

   v₂ = 0

   Initialize tangents from **u**:

   v̇₁ = 2

   v̇₂ = -1
3. Forward propagate:

   v₃ = v₁ v₂ = 1·0 = 0

   v̇₃ = v̇₁ v₂ + v₁ v̇₂ = 2·0 + 1·(-1) = -1
4. Next:

   v₄ = sin(v₁) = sin(1)

   v̇₄ = cos(v₁) v̇₁ = cos(1)·2 = 2cos(1)
5. Add for y₁:

   v₅ = v₃ + v₄ = 0 + sin(1) = sin(1)

   v̇₅ = v̇₃ + v̇₄ = -1 + 2cos(1)
6. For y₂ part:

   v₆ = exp(v₂) = exp(0) = 1

   v̇₆ = exp(v₂) v̇₂ = 1·(-1) = -1
7. Square:

   v₇ = v₁² = 1² = 1

   v̇₇ = 2 v₁ v̇₁ = 2·1·2 = 4
8. Add for y₂:

   v₈ = v₆ + v₇ = 1 + 1 = 2

   v̇₈ = v̇₆ + v̇₇ = -1 + 4 = 3
9. Collect the JVP:

   **ẏ** = (v̇₅, v̇₈) = ( -1 + 2cos(1), 3 )

**Insight:** Forward-mode naturally returns J\_f(x)**u** in one sweep, without building J\_f. You chose **u**; AD gave the directional derivative of the entire program along that direction.

### Reverse-mode AD on a scalar loss (classic gradient via adjoints)

Let ℓ(x, y) be

ℓ = (x y + sin x)²

Compute ∂ℓ/∂x and ∂ℓ/∂y using reverse-mode AD, and evaluate at (x, y) = (1, 2).

1. Build a trace:

   v₁ = x

   v₂ = y

   v₃ = v₁ v₂

   v₄ = sin(v₁)

   v₅ = v₃ + v₄

   v₆ = v₅²

   ℓ = v₆
2. Forward pass at (1, 2):

   v₁ = 1

   v₂ = 2

   v₃ = 1·2 = 2

   v₄ = sin(1)

   v₅ = 2 + sin(1)

   v₆ = (2 + sin(1))²
3. Initialize adjoints (bars). Since ℓ = v₆:

   v̄₆ = ∂ℓ/∂v₆ = 1
4. Backprop through v₆ = v₅²:

   ∂v₆/∂v₅ = 2 v₅

   v̄₅ += v̄₆ · 2 v₅ = 1 · 2(2 + sin(1)) = 2(2 + sin(1))
5. Backprop through v₅ = v₃ + v₄:

   v̄₃ += v̄₅ · 1 = 2(2 + sin(1))

   v̄₄ += v̄₅ · 1 = 2(2 + sin(1))
6. Backprop through v₄ = sin(v₁):

   ∂v₄/∂v₁ = cos(v₁) = cos(1)

   v̄₁ += v̄₄ · cos(1)

   = 2(2 + sin(1)) cos(1)
7. Backprop through v₃ = v₁ v₂:

   ∂v₃/∂v₁ = v₂ = 2

   ∂v₃/∂v₂ = v₁ = 1

   v̄₁ += v̄₃ · v₂

   = 2(2 + sin(1)) · 2

   = 4(2 + sin(1))

   v̄₂ += v̄₃ · v₁

   = 2(2 + sin(1)) · 1

   = 2(2 + sin(1))
8. Now read off gradients:

   ∂ℓ/∂x = v̄₁ = 4(2 + sin(1)) + 2(2 + sin(1))cos(1)

   ∂ℓ/∂y = v̄₂ = 2(2 + sin(1))

**Insight:** Reverse-mode computes all input partials of a scalar output in one backward sweep by accumulating adjoints. Notice how v̄₁ receives contributions from two downstream paths (through v₃ and v₄), which is why accumulation is essential.

### Mode comparison on the same function: full Jacobian costs

Consider f: ℝ³ → ℝ². You want the full Jacobian J\_f ∈ ℝ²ˣ³ at a point. Compare forward-mode and reverse-mode sweep counts conceptually.

1. Forward-mode computes one JVP J\_f(**x**) **u** per forward sweep.

   To get all 3 columns of J\_f, run 3 sweeps with **u** = **e**₁, **e**₂, **e**₃.

   So: ~3 forward sweeps.
2. Reverse-mode computes one VJP **w**ᵀ J\_f(**x**) per backward sweep (after one forward to record the trace).

   To get all 2 rows of J\_f, run 2 backward sweeps with **w** = **e**₁ and **e**₂.

   So: ~2 backward sweeps (plus the shared forward for values/tape).
3. Conclude: if m < n (2 < 3 here), reverse-mode needs fewer sweeps to form the full Jacobian; if n < m, forward-mode would.

**Insight:** The rule “forward is good when inputs are few; reverse is good when outputs are few” is not folklore—it comes directly from how many basis directions you must seed to recover the full Jacobian.

## Key Takeaways

- ✓

  Automatic differentiation computes derivatives of a program by applying the chain rule to a recorded sequence of primitive operations (the trace).
- ✓

  Forward-mode AD propagates tangents and efficiently computes J\_f(**x**) **v** (a JVP) in one forward sweep.
- ✓

  Reverse-mode AD propagates adjoints and efficiently computes **w**ᵀ J\_f(**x**) (a VJP); gradients of a scalar loss are the special case **w** = 1.
- ✓

  Reverse-mode requires storing (or recomputing) intermediates from the forward pass; memory is often the limiting factor in deep networks.
- ✓

  To form a full Jacobian J ∈ ℝᵐˣⁿ: forward-mode typically needs n sweeps; reverse-mode typically needs m sweeps.
- ✓

  Backpropagation in deep learning is reverse-mode AD on the computational graph of the loss computation.
- ✓

  AD is “exact” relative to the primitives executed (up to floating-point), unlike finite differences which introduce approximation error.

## Common Mistakes

- ✗

  Confusing AD with numerical differentiation: AD does not pick a small ε or suffer truncation error; it uses analytic local derivatives on the executed trace.
- ✗

  Assuming reverse-mode is always better: for functions with small input dimension or when you specifically need JVPs, forward-mode can be cheaper and simpler.
- ✗

  Forgetting accumulation in reverse-mode: when a value feeds multiple downstream operations, its adjoint must sum contributions (using +=).
- ✗

  Ignoring memory cost: reverse-mode may store many intermediates; without checkpointing or careful design, memory can dominate runtime.

## Practice

easy

Let f(x) = exp(x) sin(x). Use forward-mode AD (dual-number style) to compute df/dx at x = 0.

Write the primal and tangent updates step-by-step.

**Hint:** Trace: v₁ = x, v₂ = exp(v₁), v₃ = sin(v₁), v₄ = v₂ v₃. Initialize v̇₁ = 1.

Show solution

Trace and tangents:

v₁ = x, v̇₁ = 1

At x = 0: v₁ = 0

v₂ = exp(v₁) = exp(0) = 1

v̇₂ = exp(v₁) v̇₁ = 1·1 = 1

v₃ = sin(v₁) = sin(0) = 0

v̇₃ = cos(v₁) v̇₁ = cos(0)·1 = 1

v₄ = v₂ v₃ = 1·0 = 0

v̇₄ = v̇₂ v₃ + v₂ v̇₃ = 1·0 + 1·1 = 1

So df/dx at x = 0 equals v̇₄ = 1.

medium

Reverse-mode practice. Define ℓ(x, y, z) = (x y + z) · sin(y).

Compute ∂ℓ/∂x, ∂ℓ/∂y, ∂ℓ/∂z using reverse-mode AD (show the trace, then adjoint propagation).

**Hint:** A good trace: v₁=x, v₂=y, v₃=z, v₄=v₁ v₂, v₅=v₄+v₃, v₆=sin(v₂), v₇=v₅ v₆ = ℓ.

Show solution

Trace:

v₁ = x

v₂ = y

v₃ = z

v₄ = v₁ v₂

v₅ = v₄ + v₃

v₆ = sin(v₂)

v₇ = v₅ v₆

ℓ = v₇

Adjoints (initialize): v̄₇ = 1

Backprop v₇ = v₅ v₆:

v̄₅ += v̄₇ · v₆ = 1·v₆ = v₆

v̄₆ += v̄₇ · v₅ = 1·v₅ = v₅

Backprop v₆ = sin(v₂):

v̄₂ += v̄₆ · cos(v₂) = v₅ cos(v₂)

Backprop v₅ = v₄ + v₃:

v̄₄ += v̄₅ · 1 = v₆

v̄₃ += v̄₅ · 1 = v₆

Backprop v₄ = v₁ v₂:

v̄₁ += v̄₄ · v₂ = v₆ v₂

v̄₂ += v̄₄ · v₁ = v₆ v₁

Collect:

∂ℓ/∂x = v̄₁ = y sin(y)

∂ℓ/∂z = v̄₃ = sin(y)

∂ℓ/∂y = v̄₂ = (x y + z) cos(y) + x sin(y)

(Using v₅ = x y + z and v₆ = sin(y).)

hard

Let f: ℝⁿ → ℝᵐ. You need the full Jacobian J\_f at a point. Suppose one forward evaluation costs C.

1) Estimate the cost (in units of C) to compute J\_f with forward-mode.

2) Estimate the cost to compute J\_f with reverse-mode.

3) For which regimes of (n, m) is each preferable?

**Hint:** Forward-mode gives one column per seeded input basis direction; reverse-mode gives one row per seeded output basis direction (after taping).

Show solution

1) Forward-mode: one sweep gives J\_f(**x**) **u**. To get all columns, run with **u** = **e**₁,…,**e**ₙ. Cost ≈ n·C (up to a small constant factor).

2) Reverse-mode: one backward sweep gives **w**ᵀ J\_f(**x**). To get all rows, run with **w** = **e**₁,…,**e**ₘ. Cost ≈ m·C plus the cost of the forward pass to build/store the trace (often counted once). So ≈ (m+1)·C times constants.

3) Prefer forward-mode when n ≪ m (few inputs, many outputs). Prefer reverse-mode when m ≪ n (few outputs, many inputs). In ML with scalar loss, m = 1 and n is huge, so reverse-mode is strongly preferred.

## Connections

Next steps and related nodes:

- •[Computational Graphs](/tech-tree/computational-graphs/): AD operates on the same graph structure; reverse-mode is a backward pass on that graph.
- •[Deep Learning](/tech-tree/deep-learning/): Training uses reverse-mode AD (backprop) to compute ∇\_**θ** ℓ efficiently for large parameter vectors.
- •[Optimization](/tech-tree/optimization/): Gradient-based methods (SGD, Adam, Newton-style methods) depend on gradients and sometimes Hessian-vector products.
- •[Numerical Linear Algebra](/tech-tree/numerical-linear-algebra/): Understanding Jacobians as linear maps helps interpret JVP/VJP as efficient linear algebra operations.

Quality: A (4.5/5)

[← back to tree](/tech-tree/)[browse all →](/tech-tree/inventory/)
