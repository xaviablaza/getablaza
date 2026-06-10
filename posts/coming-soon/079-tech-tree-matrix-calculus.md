---
title: Matrix Calculus
description: Derivatives with respect to matrices and vectors. Jacobians, Hessians.
date: '2026-07-01'
scheduled: '2026-09-17'
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
inspiration_url: https://templeton.host/tech-tree/matrix-calculus/
inspiration_category: tech-tree
---

> Source-copy draft imported from [https://templeton.host/tech-tree/matrix-calculus/](https://templeton.host/tech-tree/matrix-calculus/). Names, domain references, and local media paths were adapted for Xavi Ablaza / getablaza.com.

[←Back to Tech Tree](/tech-tree/)

[inventory](/tech-tree/inventory/)[coverage](/tech-tree/coverage/)

# Matrix Calculus

Linear AlgebraDifficulty: ★★★★☆Depth: 7Unlocks: 13

Derivatives with respect to matrices and vectors. Jacobians, Hessians.

## Interactive Visualization

⏮◀◀▶▶STEP0.25x1xZOOM

t=0s

## Core Concepts

- -Derivative as linear map (differential): the derivative at X is the linear operator Df(X) that gives the first-order change, i.e. df approx Df(X)[dX].
- -Storage conventions for derivatives: scalar-output -> gradient (represented to match input via the trace/inner product); vector-output -> Jacobian (matrix of partials); matrix-output -> handled by vectorization into a Jacobian.
- -Second derivative as a symmetric bilinear form (Hessian): the second differential is a bilinear map on perturbations, commonly represented as the Hessian matrix after vectorization.

## Key Symbols & Notation

D f(X) (derivative operator / linear map)vec(X) (vectorization of a matrix: stack columns into a vector)

## Essential Relationships

- -Chain rule in operator/Jacobian form: D(g∘f)(x) = Dg(f(x)) ∘ Df(x) (equivalently, using Jacobians and vec: vec(dY) = J \* vec(dX)).

## Prerequisites (3)

[Gradients5 atoms](/tech-tree/gradients/)[Jacobian6 atoms](/tech-tree/jacobian/)[Matrix Operations6 atoms](/tech-tree/matrix-operations/)

## Unlocks (3)

[Neural Networkslvl 4](/tech-tree/neural-networks/)[Attention Mechanismslvl 5](/tech-tree/attention-mechanisms/)[Second-Order Optimizationlvl 5](/tech-tree/second-order-methods/)

Advanced Learning Details

### Graph Position

68

Depth Cost

13

Fan-Out (ROI)

6

Bottleneck Score

7

Chain Length

### Cognitive Load

6

Atomic Elements

43

Total Elements

L3

Percentile Level

L4

Atomic Level

### All Concepts (18)

- - Matrix differential (dX): using differentials to linearize matrix-valued functions and express total derivative
- - Derivative with respect to a matrix: definition, interpretation and the fact that the derivative's shape depends on flattening convention
- - Derivative with respect to a matrix entry-wise: scalar-of-matrix partials arranged into a matrix of the same shape
- - Hessian for vector arguments: second derivative of a scalar w.r.t. a vector (∇^2 f) and its interpretation as a bilinear form
- - Higher-order derivatives for matrix-valued inputs: notion that second derivatives of matrix functions are fourth-order tensors
- - Avoidance/representation of higher-order tensors: using matrix differentials, trace identities, vec and Kronecker tools to represent higher-order derivatives without explicit fourth-order tensors
- - vec operator: vectorization of a matrix by stacking columns (vec(X)) as a tool to convert matrix derivatives into vector derivatives
- - Kronecker product (⊗) as a tool for expressing linear maps on vec(X) and for representing derivatives of matrix products
- - Trace operator and trace identities used as a bridge between scalar differentials and inner products on matrices
- - Inner product on matrices: ⟨A,B⟩ = tr(A^T B) and its role in defining gradients for matrix arguments
- - Layout conventions for matrix derivatives (numerator-layout vs denominator-layout, row-major vs column-major Jacobian conventions) and their effect on transposes and shapes
- - Matrix product/chain/product-rule adaptations: matrix-specific forms of product rule and chain rule for derivatives
- - Common matrix derivative formulas as canonical results to learn (e.g., derivative of inverse, determinant, log-det, trace, quadratic forms)
- - Gradient expressions for quadratic forms: e.g., gradient of x^T A x equals (A + A^T) x and Hessian equals (A + A^T)
- - Differential identities for matrix inverse: d(X^{-1}) = -X^{-1} (dX) X^{-1} and related derived gradient formulas
- - Differential identities for determinant & log-determinant: d det(X) = det(X) tr(X^{-1} dX) and d log det(X) = tr(X^{-1} dX)
- - Conversion between trace forms and vector inner-products: rewriting scalar expressions as tr(A^T B) to read off gradients
- - Representing Jacobians of matrix-valued functions via vec and Kronecker identities to get explicit Jacobian matrices

### Teaching Strategy

Multi-session curriculum - substantial prior knowledge and complex material. Use mastery gates and deliberate practice.

Backprop, attention, and second-order methods all depend on one quiet idea: when your input is a vector or matrix, “the derivative” is best understood as a linear map that eats a perturbation and returns the first-order change. Matrix calculus is the toolkit for writing that idea cleanly and computing it reliably.

TL;DR:

Treat derivatives as linear maps (differentials): df ≈ Df(X)[dX]. For scalars, store the derivative as a gradient so that df = ⟨∇f, dX⟩ = tr((∇f)ᵀ dX). For vector outputs, store it as a Jacobian J so that d**y** = J d**x**. For matrices, use the same idea with tr and/or vec(·) to reduce everything to vector calculus. Second derivatives are bilinear maps; after vectorization they become Hessian matrices.

## What Is Matrix Calculus?

### The motivation: why “partial derivatives” get messy

In single-variable calculus, a derivative is a number. In multivariable calculus, a derivative is not “just a bunch of partial derivatives” (though it can be stored that way). Conceptually, it is a *linear approximation*.

Matrix calculus keeps that conceptual core while letting the input be a vector or a matrix.

When you do machine learning, your parameters might be a matrix W, your activations might be a matrix X, and your loss is often a scalar L. You want rules that feel like:

- •If L depends on W, compute ∂L/∂W.
- •If **y** = f(**x**), compute the Jacobian.
- •If you want curvature information, compute the Hessian.

But matrices have shapes, transposes, and multiplication order, so naive elementwise partial derivatives quickly become unreadable.

### The core definition: derivative as a linear map (differential)

Let f map matrices to scalars: f: ℝ^{m×n} → ℝ.

The derivative at X is the linear operator Df(X) that maps a perturbation dX to the first-order change in f:

- •**First-order approximation**:

f(X + dX) ≈ f(X) + Df(X)[dX]

- •**Differential notation** (same idea):

df ≈ Df(X)[dX]

Here, Df(X)[·] is *linear* in dX.

This is the cleanest way to reason about derivatives with matrix inputs, because it avoids getting stuck in index notation too early.

### How do we “store” Df(X)? Enter inner products

A linear functional on matrices (a linear map ℝ^{m×n} → ℝ) can be represented using an inner product.

We use the Frobenius inner product:

⟨A, B⟩ = tr(Aᵀ B) = ∑ᵢ∑ⱼ Aᵢⱼ Bᵢⱼ

So if Df(X)[dX] is a scalar linear in dX, there exists a matrix G (same shape as X) such that:

Df(X)[dX] = ⟨G, dX⟩ = tr(Gᵀ dX)

That matrix G is what we call the **gradient** with respect to X, written ∇\_X f (or sometimes ∂f/∂X depending on convention).

So for scalar-output functions of a matrix input, the most common storage convention is:

df = tr((∇\_X f)ᵀ dX)

This single equation is the “Rosetta stone” of practical matrix calculus.

### Vector outputs: Jacobians are the storage for linear maps

If f maps vectors to vectors, f: ℝ^n → ℝ^k, then the derivative at **x** is a linear map ℝ^n → ℝ^k. We store it as a k×n matrix J so that:

d**y** = J d**x**

where **y** = f(**x**).

Again, the point is: *the Jacobian is a representation of a linear map*.

### Matrix outputs: it’s still linear maps, but we often vec(·)

If F maps matrices to matrices, F: ℝ^{m×n} → ℝ^{p×q}, then DF(X) is a linear map from ℝ^{m×n} to ℝ^{p×q}. To store it as a matrix, we often vectorize:

vec(X) stacks the columns of X into a long vector.

Then DF(X) becomes an ordinary Jacobian:

vec(dF) = J vec(dX)

where J has shape (pq)×(mn).

This seems big, but you rarely form J explicitly; it’s mainly a conceptual tool to make chain rules precise.

### Second derivatives: Hessians as bilinear forms

The second derivative is not just “the derivative of the gradient” (though it can be computed that way). Conceptually, it is a *bilinear map*:

D²f(X)[dX₁, dX₂]

For scalar-output f, the second differential d²f is quadratic in dX:

d²f = D²f(X)[dX, dX]

After vectorization, you can represent this bilinear form using a Hessian matrix H:

Let x = vec(X). Then:

d²f = (dx)ᵀ H dx

When f is sufficiently smooth, H is symmetric (Hᵀ = H), matching the idea of “curvature.”

### A quick conventions table (so you don’t get whiplash)

Different books choose different layouts. We’ll stick to a consistent “differential-first” approach.

| Situation | Function type | Derivative as linear map | Common storage | Key identity |
| --- | --- | --- | --- | --- |
| Scalar output, vector input | f: ℝ^n → ℝ | Df(**x**)[d**x**] | gradient ∇f ∈ ℝ^n | df = (∇f)ᵀ d**x** |
| Scalar output, matrix input | f: ℝ^{m×n} → ℝ | Df(X)[dX] | gradient ∇\_X f ∈ ℝ^{m×n} | df = tr((∇\_X f)ᵀ dX) |
| Vector output, vector input | f: ℝ^n → ℝ^k | Df(**x**)[d**x**] | Jacobian J ∈ ℝ^{k×n} | d**y** = J d**x** |
| Matrix output, matrix input | F: ℝ^{m×n} → ℝ^{p×q} | DF(X)[dX] | Jacobian of vec(F) vs vec(X) | vec(dF) = J vec(dX) |

The rest of this lesson is about using these identities to compute derivatives cleanly, with the right shapes, and with a chain rule that works in matrix form.

## Core Mechanic 1: Differentials + Trace Trick (Gradients for Scalar Losses)

### Why this mechanic matters

In ML, the loss L is almost always a scalar, but it depends on matrices: weights W, data X, covariances Σ, attention score matrices, etc.

So the most common task is:

- •Given a scalar f(X), compute ∇\_X f.

Trying to do this entry-by-entry works, but it is slow and error-prone. The differential method keeps you aligned with linear algebra operations.

### The method in one sentence

1) Compute df in terms of dX using algebra (product rule, transpose rule, trace identities).

2) Rewrite df into the canonical form df = tr(Gᵀ dX).

3) Read off ∇\_X f = G.

### Rules you’ll use constantly

We’ll list the rules, then show how they play together.

**(1) Linearity**

If f = a f₁ + b f₂, then df = a df₁ + b df₂.

**(2) Product rule (matrix form)**

If M(X) and N(X) are matrix-valued functions, then

d(MN) = (dM)N + M(dN)

Same as scalar calculus, but preserve order.

**(3) Transpose rule**

d(Xᵀ) = (dX)ᵀ

**(4) Trace cyclic property**

tr(ABC) = tr(BCA) = tr(CAB) as long as the products are defined.

This is how you “move” matrices around to place dX at the end.

**(5) Frobenius inner product identification**

If df = tr(Gᵀ dX), then ∇\_X f = G.

### Canonical patterns worth memorizing

These are not magic; they’re just the differential method applied once, and then remembered.

#### Pattern A: f(X) = tr(Aᵀ X)

Let A be constant.

- •f = tr(Aᵀ X)
- •df = tr(Aᵀ dX)

So ∇\_X f = A.

This is the matrix analog of “derivative of a dot product.”

#### Pattern B: f(X) = tr(Xᵀ A X)

Assume A is constant and X is variable. Shapes: X ∈ ℝ^{n×k}, A ∈ ℝ^{n×n}.

Start:

f = tr(Xᵀ A X)

df = tr(d(Xᵀ) A X) + tr(Xᵀ A dX)

Use d(Xᵀ) = (dX)ᵀ:

df = tr((dX)ᵀ A X) + tr(Xᵀ A dX)

Now rewrite the first term to have dX (not (dX)ᵀ). Use tr((dX)ᵀ M) = tr(Mᵀ dX):

tr((dX)ᵀ A X) = tr((A X)ᵀ dX) = tr(Xᵀ Aᵀ dX)

So:

df = tr(Xᵀ Aᵀ dX) + tr(Xᵀ A dX)

= tr(Xᵀ (Aᵀ + A) dX)

Match df = tr(Gᵀ dX). Here Gᵀ = Xᵀ (Aᵀ + A), so

G = (Aᵀ + A) X

Therefore:

∇\_X tr(Xᵀ A X) = (Aᵀ + A) X

If A is symmetric (Aᵀ = A), this simplifies to 2AX.

#### Pattern C: f(X) = ‖X‖\_F²

Recall ‖X‖\_F² = tr(Xᵀ X).

Using Pattern B with A = I:

∇\_X ‖X‖\_F² = 2X

#### Pattern D: f(X) = ‖AX − B‖\_F² (least squares)

Let f = tr((AX − B)ᵀ (AX − B)).

Define E = AX − B.

Then f = tr(Eᵀ E) and df = 2 tr(Eᵀ dE).

But dE = A dX (since B is constant).

So:

df = 2 tr(Eᵀ A dX)

Move to canonical form:

2 tr(Eᵀ A dX) = 2 tr((Aᵀ E)ᵀ dX)

Thus:

∇\_X ‖AX − B‖\_F² = 2 Aᵀ (AX − B)

This is the workhorse gradient behind linear regression and many layers’ backprop steps.

### The “shape check” habit

A reliable way to avoid transpose mistakes: always verify shapes.

- •If X is m×n, then ∇\_X f must also be m×n.
- •In the canonical form df = tr(Gᵀ dX), both G and dX are m×n.

If your G comes out transposed, you’ll catch it immediately.

### Scalars built from vectors and matrices

A lot of ML scalars look like:

- •**b**ᵀ **x**
- •**x**ᵀ A **x**
- •tr(A X)
- •log det(X)

The differential method extends to these, but you need a few extra identities.

#### Identity: d log det(X)

For an invertible square matrix X:

d(log det X) = tr(X⁻¹ dX)

So in canonical form df = tr((X⁻ᵀ)ᵀ dX) (since X⁻¹ may not be symmetric), hence:

∇\_X log det X = X⁻ᵀ

This shows up in Gaussian log-likelihoods and normalization constants.

#### Identity: d(X⁻¹)

For invertible X:

d(X⁻¹) = −X⁻¹ (dX) X⁻¹

This is essential when differentiating through solves, covariances, and some attention normalizations.

### Why trace is the right language

You might wonder: why do we insist on writing df as tr(Gᵀ dX)?

Because it is exactly the statement “Df(X) is a linear functional and the Frobenius inner product identifies linear functionals with matrices.”

It’s the matrix version of: df = (∇f)ᵀ d**x**.

Once you internalize that, most derivative problems become:

- •compute df algebraically
- •rearrange
- •read off the gradient

rather than “take partial derivative with respect to every element.”

## Core Mechanic 2: Jacobians, vec(·), and the Chain Rule (Plus Hessians)

### Why this mechanic matters

Gradients are enough for basic backprop, but modern ML quickly forces you into more structured derivatives:

- •vector outputs (activations) and their Jacobians
- •matrix outputs (attention score matrices, covariance matrices)
- •second-order info (Newton / Gauss–Newton / Fisher)

To make these rigorous, you need two tools:

1) A chain rule stated for linear maps.

2) A way to store/represent matrix-to-matrix linear maps (often vec(·)).

### Jacobians as linear map storage

Let **y** = f(**x**) with **x** ∈ ℝ^n and **y** ∈ ℝ^k.

Derivative as linear map:

D f(**x**)[d**x**] = d**y**

Storage as Jacobian J:

d**y** = J d**x**, where J ∈ ℝ^{k×n}

Entry definition:

Jᵢⱼ = ∂yᵢ/∂xⱼ

This matches what you already know, but the linear-map viewpoint is what makes composition painless.

### Chain rule (most general, most useful form)

If **y** = f(**x**) and z = g(**y**) (z can be scalar or vector), then:

D(g ∘ f)(**x**) = Dg(**y**) ∘ Df(**x**)

Meaning: apply Df to the perturbation first, then apply Dg.

In differentials:

d**y** = Df(**x**)[d**x**]

dz = Dg(**y**)[d**y**]

Substitute:

dz = Dg(**y**)[ Df(**x**)[d**x**] ]

If you store Df and Dg as matrices (Jacobians), you get ordinary matrix multiplication:

dz = (J\_g J\_f) d**x**

This is the clean mathematical heart of backprop.

### Matrix inputs/outputs and vec(·)

Suppose F: ℝ^{m×n} → ℝ^{p×q}.

DF(X) is a linear map:

DF(X)[dX] = dF

To store it as a matrix, vectorize both sides:

vec(dF) = J vec(dX)

where J is (pq)×(mn). This is the Jacobian of vec(F) with respect to vec(X).

You can now apply the usual vector chain rule to big, flattened vectors.

In practice, you rarely build J. You use it conceptually to justify operations like:

- •“the gradient is the adjoint of the Jacobian” (vector-Jacobian products)
- •efficient backprop without constructing huge matrices

### Vector-Jacobian and Jacobian-vector products

Two extremely practical computational patterns:

- •**JVP**: given d**x**, compute d**y** = J d**x**
- •**VJP**: given upstream **v** (same shape as **y**), compute **v**ᵀ J (or Jᵀ **v** depending on convention)

Autodiff systems exploit these to compute gradients efficiently.

For scalar loss L(**y**), the gradient ∇\_**x** L can be seen as a VJP:

If **y** = f(**x**), then

∇\_**x** L = J\_f(**x**)ᵀ ∇\_**y** L

This is the algebraic form of backprop through f.

### Hessians: the second differential as a bilinear map

Let f: ℝ^n → ℝ be scalar.

First differential:

df = (∇f)ᵀ d**x**

Differentiate again:

d(df) = d( (∇f)ᵀ d**x** )

Treat d**x** as the perturbation (not a variable), so the variability is in ∇f:

d²f = (d(∇f))ᵀ d**x**

But d(∇f) is linear in d**x** and is given by the Hessian H:

d(∇f) = H d**x**

So:

d²f = (H d**x**)ᵀ d**x** = (d**x**)ᵀ Hᵀ d**x**

For smooth f, H is symmetric, so Hᵀ = H:

d²f = (d**x**)ᵀ H d**x**

#### Matrix-input Hessians

If f(X) is scalar with X ∈ ℝ^{m×n}, let x = vec(X).

Then define H = ∂²f/∂x² (an (mn)×(mn) matrix) so that:

d²f = (dx)ᵀ H dx

This is the formal way to store the second derivative. It’s often too large to form explicitly, so practical methods use:

- •Hessian-vector products H v
- •structure (e.g., Kronecker products) when available

### When Hessians simplify: quadratic forms

If f(**x**) = ½ **x**ᵀ A **x** with A symmetric, then:

∇f = A **x**

H = A

For f(X) = ½ ‖AX − B‖\_F², the Hessian (with respect to vec(X)) is:

H = (I ⊗ Aᵀ A)

where ⊗ is the Kronecker product, and I matches the output dimension of columns of X.

You don’t need to memorize this, but it hints at why second-order methods can be expensive: the Hessian lives in a much bigger space.

### A conventions sanity table (Jacobian layout)

Different sources disagree on whether Jacobians are ∂yᵢ/∂xⱼ or ∂xⱼ/∂yᵢ in rows/cols. We’ll use the standard “rows are outputs” convention.

| Object | Shape | Meaning |
| --- | --- | --- |
| J = ∂**y**/∂**x** | k×n | d**y** = J d**x** |
| ∇\_**x** L | n×1 | df = (∇L)ᵀ d**x** |
| Hessian H | n×n | d²f = (d**x**)ᵀ H d**x** |

If you ever switch conventions, the safest fallback is the differential definition: if your stored object reproduces the correct df or d**y**, it’s consistent.

## Application/Connection: Backprop, Attention, and Second-Order Optimization

### Why matrix calculus shows up everywhere in ML

Most ML systems are compositions of linear maps and elementwise nonlinearities applied to vectors/matrices. The training objective is a scalar.

So you repeatedly need:

- •gradients with respect to matrices
- •chain rule through many layers
- •sometimes curvature information (or approximations)

Matrix calculus provides a language that stays readable even when the model is large.

### Backprop through a linear layer (matrix form)

Consider a batch of inputs X ∈ ℝ^{d×b} (b examples as columns), weights W ∈ ℝ^{m×d}, and outputs Z:

Z = W X

Suppose the loss L depends on Z (through later layers): L = ℓ(Z).

The differential:

dZ = d(WX) = (dW)X + W(dX)

Upstream, you have ∇\_Z L (same shape as Z). For scalar L:

dL = tr((∇\_Z L)ᵀ dZ)

Substitute dZ:

dL = tr((∇\_Z L)ᵀ ( (dW)X + W(dX) ))

= tr((∇\_Z L)ᵀ (dW)X) + tr((∇\_Z L)ᵀ W(dX))

Now rearrange each term into tr(Gᵀ dW) and tr(Hᵀ dX).

First term:

tr((∇\_Z L)ᵀ (dW)X)

= tr(X (∇\_Z L)ᵀ dW) (cyclic)

= tr(( (∇\_Z L) Xᵀ )ᵀ dW)

So:

∇\_W L = (∇\_Z L) Xᵀ

Second term:

tr((∇\_Z L)ᵀ W(dX))

= tr( (Wᵀ ∇\_Z L)ᵀ dX )

So:

∇\_X L = Wᵀ (∇\_Z L)

These are exactly the standard backprop equations, derived without indices.

### Attention as a matrix-calculus playground

A simplified attention block contains operations like:

S = Q Kᵀ / √d (scores)

P = softmax(S) (row-wise)

O = P V

Even if you don’t derive full softmax Jacobians by hand in practice, the dependency structure is entirely matrix-based. The linear-map view keeps you grounded:

- •O depends linearly on V given P
- •O depends linearly on P given V
- •P depends nonlinearly on S (softmax Jacobian per row)
- •S depends bilinearly on Q and K

For the bilinear score S = QKᵀ, the differential is:

dS = (dQ)Kᵀ + Q(dK)ᵀ

This is the same product rule pattern you saw earlier, and it’s the starting point for gradients with respect to Q and K.

### Second-order optimization: where Hessians enter

Newton’s method for minimizing scalar f(**x**) uses:

**x**\_{new} = **x** − H⁻¹ ∇f

For huge parameter vectors, H is too large to form or invert, but second-order methods rely on:

- •approximations (BFGS/L-BFGS)
- •Hessian-vector products (for conjugate gradient)
- •structured curvature (Gauss–Newton, Fisher)

Matrix calculus provides:

- •the definition of H via second differentials
- •the ability to compute H v without forming H explicitly (via differentiating a gradient in direction v)

### A practical mental model: what autodiff is doing

Reverse-mode autodiff can be understood as repeatedly applying VJPs (vector-Jacobian products) through a computational graph.

When your variable is a matrix, the “vector” in VJP is really an object of the same shape, and the inner product is Frobenius:

dL = tr((∇\_X L)ᵀ dX)

So the backpropagated quantity is precisely the gradient that makes this identity true.

### Connections to the rest of the tech tree

- •Neural networks: gradients of matrix multiplications and elementwise nonlinearities.
- •Attention: gradients through bilinear forms QKᵀ and normalization.
- •Second-order methods: Hessians, Hessian-vector products, curvature approximations.

If you can fluently turn “how does this output change if I perturb X?” into df = tr(Gᵀ dX), you can derive most gradients you’ll ever need.

## Worked Examples (3)

### Gradient of a quadratic matrix form: f(X) = tr(Xᵀ A X)

Let X ∈ ℝ^{n×k} be the variable and A ∈ ℝ^{n×n} be constant. Compute ∇\_X f for f(X) = tr(Xᵀ A X).

1. Start with the differential:

   f = tr(Xᵀ A X)

   df = tr(d(Xᵀ) A X) + tr(Xᵀ A dX)
2. Use d(Xᵀ) = (dX)ᵀ:

   df = tr((dX)ᵀ A X) + tr(Xᵀ A dX)
3. Rewrite the first term to have dX (not (dX)ᵀ):

   tr((dX)ᵀ A X) = tr((A X)ᵀ dX) = tr(Xᵀ Aᵀ dX)
4. Combine terms:

   df = tr(Xᵀ Aᵀ dX) + tr(Xᵀ A dX)

   = tr(Xᵀ (Aᵀ + A) dX)
5. Match canonical form df = tr(Gᵀ dX):

   Gᵀ = Xᵀ (Aᵀ + A)

   ⇒ G = (Aᵀ + A) X

   Therefore:

   ∇\_X tr(Xᵀ A X) = (Aᵀ + A) X

**Insight:** The gradient depends on the symmetric part of A: (A + Aᵀ). If A is symmetric, the result collapses to 2AX. This is the matrix version of ∇(**x**ᵀA**x**) = (A + Aᵀ)**x**.

### Least squares gradient: f(X) = ‖AX − B‖\_F²

Let A ∈ ℝ^{p×m}, X ∈ ℝ^{m×n} (variable), B ∈ ℝ^{p×n}. Compute ∇\_X f where f(X) = ‖AX − B‖\_F².

1. Introduce E = AX − B so that f = tr(Eᵀ E).
2. Differentiate f:

   df = d tr(Eᵀ E)

   = tr(d(Eᵀ) E) + tr(Eᵀ dE)

   = tr((dE)ᵀ E) + tr(Eᵀ dE)
3. Use tr((dE)ᵀ E) = tr(Eᵀ dE):

   df = 2 tr(Eᵀ dE)
4. Differentiate E = AX − B:

   dE = A dX
5. Substitute:

   df = 2 tr(Eᵀ A dX)
6. Put into canonical form:

   2 tr(Eᵀ A dX) = 2 tr((Aᵀ E)ᵀ dX)
7. Read off the gradient:

   ∇\_X f = 2 Aᵀ E = 2 Aᵀ(AX − B)

**Insight:** This derivation is a template: (1) name the residual, (2) use df = 2⟨E, dE⟩, (3) push dX to the end via trace, (4) read off the gradient. It’s the backbone of many ML gradients.

### Backprop through a linear map: Z = W X, compute ∇\_W L and ∇\_X L

Let W ∈ ℝ^{m×d}, X ∈ ℝ^{d×b}, Z = W X ∈ ℝ^{m×b}. Let L be a scalar loss that depends on Z, and assume you know ∇\_Z L. Compute ∇\_W L and ∇\_X L.

1. Differentiate Z = WX:

   dZ = d(WX) = (dW)X + W(dX)
2. Write the scalar differential using the Frobenius pairing:

   dL = tr((∇\_Z L)ᵀ dZ)
3. Substitute for dZ:

   dL = tr((∇\_Z L)ᵀ ( (dW)X + W(dX) ))

   = tr((∇\_Z L)ᵀ (dW)X) + tr((∇\_Z L)ᵀ W(dX))
4. Rearrange the first term to isolate dW:

   tr((∇\_Z L)ᵀ (dW)X)

   = tr(X(∇\_Z L)ᵀ dW)

   = tr(((∇\_Z L)Xᵀ)ᵀ dW)

   ⇒ ∇\_W L = (∇\_Z L)Xᵀ
5. Rearrange the second term to isolate dX:

   tr((∇\_Z L)ᵀ W(dX))

   = tr((Wᵀ∇\_Z L)ᵀ dX)

   ⇒ ∇\_X L = Wᵀ(∇\_Z L)

**Insight:** This is backprop in its most compact form: the upstream gradient ∇\_Z L gets multiplied by Xᵀ to produce ∇\_W L, and by Wᵀ to produce ∇\_X L. The only trick is writing dL = tr((∇\_Z L)ᵀ dZ).

## Key Takeaways

- ✓

  The derivative is best understood as a linear map: df ≈ Df(X)[dX].
- ✓

  For scalar-output f(X), store the derivative as a gradient ∇\_X f such that df = tr((∇\_X f)ᵀ dX).
- ✓

  Trace identities (especially cyclic permutation) are the main tool to rearrange df into canonical form and read off gradients.
- ✓

  For vector outputs, the Jacobian J stores the linear map so that d**y** = J d**x**.
- ✓

  Matrix-to-matrix derivatives can be represented via vectorization: vec(dF) = J vec(dX), even if J is never formed explicitly.
- ✓

  Second derivatives are bilinear forms; after vec(·) they become Hessian matrices via d²f = (dx)ᵀ H dx.
- ✓

  Backprop is repeated application of the chain rule in linear-map form, implemented efficiently as VJPs and JVPs.

## Common Mistakes

- ✗

  Dropping matrix multiplication order in product rules (writing d(MN) as dM dN or swapping factors).
- ✗

  Forgetting the storage convention: a correct Df(X)[dX] but an incorrectly transposed gradient because df wasn’t matched to tr(Gᵀ dX).
- ✗

  Mixing Jacobian layout conventions (rows-as-outputs vs columns-as-outputs) without checking which one matches d**y** = J d**x**.
- ✗

  Treating the Hessian as “just the gradient of the gradient” without respecting that the second derivative is a bilinear form (and often too large to form explicitly).

## Practice

easy

Compute ∇\_X f for f(X) = tr(A X B), where A and B are constants and shapes are compatible.

**Hint:** Use df = tr(A dX B) and then use cyclic trace to put dX at the end: tr(A dX B) = tr((Aᵀ ? )ᵀ dX).

Show solution

df = tr(A dX B) = tr(B A dX) (cyclic).

Now match df = tr(Gᵀ dX).

We have Gᵀ = B A, so G = (B A)ᵀ = Aᵀ Bᵀ.

Therefore ∇\_X tr(A X B) = Aᵀ Bᵀ.

medium

Let f(**x**) = ½‖C**x** − **d**‖² with C ∈ ℝ^{m×n}. Compute ∇\_**x** f and the Hessian H.

**Hint:** Write f = ½(C**x** − **d**)ᵀ(C**x** − **d**). Differentiate once to get ∇, then differentiate again (or recognize it is quadratic).

Show solution

Let **r** = C**x** − **d**.

Then f = ½ **r**ᵀ **r**.

Differential: df = **r**ᵀ d**r**.

But d**r** = C d**x**.

So df = **r**ᵀ C d**x** = (Cᵀ **r**)ᵀ d**x**.

Thus ∇\_**x** f = Cᵀ(C**x** − **d**).

Because ∇\_**x** f = Cᵀ C **x** − Cᵀ **d**, the Hessian is constant:

H = Cᵀ C.

hard

For invertible X ∈ ℝ^{n×n}, compute ∇\_X f for f(X) = −log det(X) + tr(S X), where S is constant.

**Hint:** Use d log det(X) = tr(X⁻¹ dX). Then put df into df = tr(Gᵀ dX).

Show solution

f(X) = −log det(X) + tr(S X).

Differential:

df = −d(log det X) + d tr(SX)

= −tr(X⁻¹ dX) + tr(S dX).

Write as df = tr((S − X⁻¹) dX).

Match df = tr(Gᵀ dX) ⇒ Gᵀ = S − X⁻¹ ⇒ G = (S − X⁻¹)ᵀ = Sᵀ − X⁻ᵀ.

Therefore ∇\_X f = Sᵀ − X⁻ᵀ.

(If S is symmetric, this simplifies to S − X⁻ᵀ.)

## Connections

Next nodes you can unlock/apply this to:

- •[Neural Networks](/tech-tree/neural-networks/)
- •[Attention Mechanisms](/tech-tree/attention-mechanisms/)
- •[Second-Order Optimization](/tech-tree/second-order-methods/)

Related refreshers:

- •[Gradients](/tech-tree/gradients/)
- •[Jacobian](/tech-tree/jacobian/)
- •[Matrix Operations](/tech-tree/matrix-operations/)

Quality: B (4.2/5)

[← back to tree](/tech-tree/)[browse all →](/tech-tree/inventory/)
