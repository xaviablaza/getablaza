---
title: Jacobian
description: Matrix of partial derivatives. Change of variables in integrals.
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
permalink: /tech-tree/jacobian/
---

[←Back to Tech Tree](/tech-tree/)

[inventory](/tech-tree/inventory/)[coverage](/tech-tree/coverage/)

# Jacobian

CalculusDifficulty: ★★★☆☆Depth: 6Unlocks: 14

Matrix of partial derivatives. Change of variables in integrals.

## Interactive Visualization

⏮◀◀▶▶STEP0.25x1xZOOM

t=0s

## Core Concepts

- -Jacobian matrix as the array of first-order partial derivatives (entry = partial f\_i / partial x\_j)
- -Jacobian as the derivative/linearization: the best linear approximation (matrix) of a vector-valued map at a point
- -Jacobian determinant (square case): scalar giving local oriented volume scaling (absolute value used for change of variables)

## Key Symbols & Notation

Df(x) or J\_f(x) for the Jacobian matrix; det(Df(x)) or |J\_f(x)| for its determinant

## Essential Relationships

- -Linearization: f(x+dx) ≈ f(x) + Df(x) · dx (matrix times vector)
- -Change-of-variables/volume-scaling: for y=f(x) (locally invertible), infinitesimal volumes transform by |det(Df(x))|, hence integrals change using that factor

## Prerequisites (2)

[Gradients5 atoms](/tech-tree/gradients/)[Matrix Operations6 atoms](/tech-tree/matrix-operations/)

## Unlocks (1)

[Matrix Calculuslvl 4](/tech-tree/matrix-calculus/)

Advanced Learning Details

### Graph Position

62

Depth Cost

14

Fan-Out (ROI)

6

Bottleneck Score

6

Chain Length

### Cognitive Load

6

Atomic Elements

23

Total Elements

L0

Percentile Level

L4

Atomic Level

### All Concepts (9)

- - Jacobian matrix: for a function f: R^n -> R^m, the m×n matrix whose (i,j) entry is ∂f\_i/∂x\_j
- - Jacobian determinant: determinant of a square Jacobian (when m = n)
- - Jacobian as linear approximation (differential): the Jacobian gives the best linear map approximating f near a point
- - Local volume (area) scaling: the Jacobian determinant measures how infinitesimal volumes are scaled by the map
- - Absolute Jacobian factor in integrals: using the absolute value of the Jacobian determinant when changing variables in integrals
- - Orientation information: the sign of the Jacobian determinant indicates whether the mapping preserves or reverses orientation
- - Local invertibility criterion (inverse function theorem) in terms of Jacobian determinant: nonzero determinant implies local invertibility
- - Rectangular (non-square) Jacobians: Jacobian matrices when m ≠ n have no determinant but still represent the linear differential
- - Column/row interpretation: each column is the partial derivatives of the output(s) with respect to one input variable (or each row is the gradient of one output component)

### Teaching Strategy

Multi-session curriculum - substantial prior knowledge and complex material. Use mastery gates and deliberate practice.

You already know the gradient tells you how a scalar function changes as you nudge inputs. The Jacobian is the next step: it tells you how an entire vector of outputs changes—capturing the local linear behavior of a multivariable transformation and the volume-scaling you need for change of variables in integrals.

TL;DR:

The Jacobian J\_f(**x**) = Df(**x**) is the matrix of first-order partial derivatives of a vector-valued map f. It is the best linear approximation to f near a point. When f maps ℝⁿ → ℝⁿ, det(J\_f) measures local oriented volume scaling; |det(J\_f)| is the factor used in change-of-variables formulas in integrals.

## What Is Jacobian?

### Why you need a new object beyond the gradient

For a scalar function g: ℝⁿ → ℝ, the gradient ∇g(**x**) summarizes first-order change: it’s the vector that best predicts how g changes for a small input step **h**.

But many important maps are **vector-valued**:

- •A coordinate transform f(u, v) = (x, y)
- •A physics map from state to state
- •A neural network layer that maps an input vector to an output vector

When the output is a vector, the “rate of change” can’t be captured by a single vector. Each output component depends on each input component. The Jacobian packages all those partial derivatives into one matrix.

### Definition (matrix of partial derivatives)

Let f: ℝⁿ → ℝᵐ be written in components:

f(**x**) = (f₁(**x**), f₂(**x**), …, f\_m(**x**))

where **x** = (x₁, x₂, …, x\_n).

The **Jacobian matrix** of f at **x** is

J\_f(**x**) = Df(**x**) = [ ∂f\_i / ∂x\_j ]

It is an m×n matrix whose (i, j) entry is:

(J\_f(**x**))\_{ij} = ∂f\_i(**x**) / ∂x\_j.

So:

- •Rows correspond to output components f\_i
- •Columns correspond to input variables x\_j

### Relationship to the gradient (a comforting special case)

If m = 1 (scalar output), then J\_f is 1×n:

J\_f(**x**) = [ ∂f/∂x₁ ∂f/∂x₂ … ∂f/∂x\_n ]

This is exactly the gradient as a **row vector** (convention). Meanwhile ∇f(**x**) is usually a **column vector**. Transpose connects them:

J\_f(**x**) = (∇f(**x**))ᵀ.

So the Jacobian generalizes the gradient.

### A geometric preview: local linear map

The most important intuition is not “array of partials”, but “**best linear approximation**.” Near a point **a**, f behaves like:

f(**a** + **h**) ≈ f(**a**) + J\_f(**a**) **h**

for small **h**.

That expression is the multivariable analogue of the 1D approximation:

f(a + h) ≈ f(a) + f′(a) h.

Here, f′(a) is a number; in many dimensions, the derivative becomes a matrix.

### Square case and determinant

If m = n, then J\_f(**x**) is n×n and you can take its determinant:

det(J\_f(**x**))

This scalar has a deep meaning:

- •sign(det) tells whether the map locally preserves or flips orientation
- •|det| tells how much the map locally scales n-dimensional volume

That volume-scaling is exactly what appears in change-of-variables for integrals.

## Core Mechanic 1: Jacobian as the Derivative (Linearization)

### Why linearization matters

Most nonlinear functions are hard to analyze globally. But if you zoom in enough, smooth functions look linear. This is the core strategy behind:

- •Newton’s method and other root-finding algorithms
- •error propagation and sensitivity analysis
- •optimization and gradient-based learning (locally linear steps)

The Jacobian is the device that turns “zooming in” into a concrete computation.

### The best linear approximation statement

Let f: ℝⁿ → ℝᵐ be differentiable at **a**. Then there exists a linear map L(**h**) such that

f(**a** + **h**) = f(**a**) + L(**h**) + r(**h**)

where the remainder satisfies

‖r(**h**)‖ / ‖**h**‖ → 0 as ‖**h**‖ → 0.

That linear map L is the derivative Df(**a**). When we choose coordinates, L is represented by the Jacobian matrix J\_f(**a**), and we write:

f(**a** + **h**) ≈ f(**a**) + J\_f(**a**) **h**.

### Interpreting columns and rows

Write **e**ⱼ for the j-th standard basis vector in ℝⁿ (a 1 in position j, else 0). Then:

J\_f(**a**) **e**ⱼ = column j of J\_f(**a**).

But **e**ⱼ corresponds to “nudge only x\_j”. So:

column j ≈ how the output vector changes when you increase x\_j a tiny bit.

Equivalently, each row i is:

row i = [ ∂f\_i/∂x₁ … ∂f\_i/∂x\_n ]

which is the gradient of the i-th output component (as a row). So:

- •columns = sensitivity directions in input space
- •rows = gradients of each output component

### Chain rule in Jacobian form (the practical payoff)

If f: ℝⁿ → ℝᵐ and g: ℝᵐ → ℝᵏ, then the composition g ∘ f: ℝⁿ → ℝᵏ has Jacobian:

J\_{g∘f}(**x**) = J\_g(f(**x**)) · J\_f(**x**).

This is the multivariable chain rule, and it looks exactly like matrix multiplication.

It’s worth pausing to connect this to “linear approximation of a composition”:

- •f turns a small input step **h** into an approximate output step J\_f **h**
- •g then turns that step into J\_g (J\_f **h**)
- •overall: (J\_g J\_f) **h**

That is why the chain rule becomes matrix multiplication.

### Directional derivatives via the Jacobian

For a direction **u** ∈ ℝⁿ, the first-order change in f at **a** in direction **u** is:

Df(**a**) **u** = J\_f(**a**) **u**.

This is the vector-valued directional derivative.

In the scalar-output case (m = 1), this reduces to:

J\_f(**a**) **u** = (∇f(**a**))ᵀ **u** = ∇f(**a**) · **u**

which is the familiar directional derivative formula.

### Small-error propagation (a common use)

Suppose your input **x** has a small perturbation **δx** (measurement noise). Then the induced output perturbation is approximately:

**δy** ≈ J\_f(**x**) **δx**.

So the Jacobian acts like a “local gain matrix.” This is the mathematical foundation for sensitivity analysis and for linearizing nonlinear systems in control and estimation.

## Core Mechanic 2: Jacobian Determinant and Change of Variables

### Why determinants show up in integrals

Integration measures “total accumulation.” In multiple dimensions, it’s accumulation over **area** (2D) or **volume** (3D and beyond). If you change coordinates, a small patch in the new coordinates may correspond to a differently sized patch in the old coordinates.

So you need a conversion factor between tiny volume elements:

(d volume in x-space) = (scale factor) · (d volume in u-space)

That scale factor is the absolute value of the Jacobian determinant.

### Local volume scaling intuition

Assume f: ℝⁿ → ℝⁿ is differentiable and J\_f(**a**) is invertible.

Near **a**, f behaves like:

f(**a** + **h**) ≈ f(**a**) + J\_f(**a**) **h**.

So near **a**, f is approximately the linear map **h** ↦ J\_f(**a**) **h**. For a linear map A, the determinant det(A) gives the oriented volume scaling:

- •A maps a tiny n-dimensional parallelepiped to another
- •the volume scales by |det(A)|
- •orientation flips if det(A) < 0

Therefore, for the nonlinear map f, the **local** volume scaling near **a** is approximately |det(J\_f(**a**))|.

### The change-of-variables formula (multivariable substitution)

Let f: U ⊂ ℝⁿ → V ⊂ ℝⁿ be a bijective differentiable map with differentiable inverse (a diffeomorphism), and let g be integrable on V. Then:

∫∫…∫\_V g(**x**) d**x** = ∫∫…∫\_U g(f(**u**)) · |det(J\_f(**u**))| d**u**.

Here:

- •**u** are the new coordinates
- •**x** = f(**u**) are the old coordinates
- •d**x** and d**u** represent n-dimensional volume elements

The key idea is:

d**x** = |det(J\_f(**u**))| d**u**.

### 2D special case: area scaling

In 2D, if f(u, v) = (x(u, v), y(u, v)), then

J\_f(u, v) = [ ∂x/∂u ∂x/∂v

∂y/∂u ∂y/∂v ]

and the area element transforms as:

dx dy = |det(J\_f(u, v))| du dv.

### Common coordinate transforms

#### Polar coordinates

x = r cos θ

y = r sin θ

Compute J\_f(r, θ):

∂x/∂r = cos θ ∂x/∂θ = −r sin θ

∂y/∂r = sin θ ∂y/∂θ = r cos θ

So

J\_f = [ cos θ −r sin θ

sin θ r cos θ ]

and

det(J\_f) = (cos θ)(r cos θ) − (−r sin θ)(sin θ)

= r cos²θ + r sin²θ

= r.

Thus:

dx dy = r dr dθ.

That single factor r is exactly the Jacobian determinant’s magnitude.

#### General lesson

When you see an “extra factor” like r in polar coordinates (or r² sin φ in spherical coordinates), it is not arbitrary—it is the local volume-scaling |det(J\_f)|.

### Orientation vs absolute value

The determinant can be negative. Integrals measure (unsigned) volume/area, so the change-of-variables formula uses:

|det(J\_f)|.

If you’re doing differential geometry or oriented integrals, the sign can matter; for standard multivariable calculus integrals over regions, absolute value is the rule.

## Application/Connection: Jacobians in Optimization, ML, and Matrix Calculus

### Why Jacobians show up constantly in ML

Many ML models are compositions of vector-valued functions:

**x** → f₁(**x**) → f₂(f₁(**x**)) → … → **y**

Training relies on derivatives of a loss with respect to parameters, and those derivatives are built from Jacobians (and their transposes) via the chain rule.

Even when you mostly hear “gradients,” under the hood:

- •a gradient is a Jacobian of a scalar-output function
- •backprop is repeated application of the Jacobian chain rule

### Jacobian vs gradient vs Hessian (positioning)

You already know gradients. The Jacobian sits between gradient and Hessian in complexity:

| Object | Typical function type | Shape | Captures | Notes |
| --- | --- | --- | --- | --- |
| ∇g(**x**) | g: ℝⁿ → ℝ | n×1 | first-order change of scalar | steepest ascent direction |
| J\_f(**x**) | f: ℝⁿ → ℝᵐ | m×n | first-order change of vector | linearization matrix |
| H\_g(**x**) | g: ℝⁿ → ℝ | n×n | second-order change | curvature |

A helpful mental model:

- •gradient: “slope vector”
- •Jacobian: “slope matrix”
- •Hessian: “curvature matrix”

### Jacobian-transpose trick (common in least squares)

Suppose you have residuals **r**(**x**) ∈ ℝᵐ and a scalar loss:

L(**x**) = ½ ‖**r**(**x**)‖².

Then the gradient of L can be written using the Jacobian of **r**:

Let J = J\_r(**x**) (an m×n matrix). Then:

L(**x**) = ½ ∑\_{i=1}^m r\_i(**x**)²

Differentiate component-wise. For j-th component:

∂L/∂x\_j = ½ ∑\_{i=1}^m 2 r\_i(**x**) · ∂r\_i/∂x\_j

= ∑\_{i=1}^m r\_i(**x**) · J\_{ij}

In matrix form:

∇L(**x**) = J\_r(**x**)ᵀ **r**(**x**).

This identity appears in Gauss–Newton, Levenberg–Marquardt, and many optimization routines.

### Jacobian in dynamics and stability

For a dynamical system:

**x**\_{t+1} = f(**x**\_t)

the Jacobian J\_f at a fixed point **x**⋆ characterizes local stability:

**x**\_{t+1} − **x**⋆ ≈ J\_f(**x**⋆) ( **x**\_t − **x**⋆ )

Eigenvalues of J\_f(**x**⋆) determine whether perturbations shrink or grow.

### Bridge to Matrix Calculus

Matrix calculus generalizes these ideas when variables and outputs are vectors/matrices and you want systematic rules.

Key bridge concepts you’ll use next:

- •organizing derivatives consistently (shapes and conventions)
- •Jacobians of common vector operations
- •combining Jacobians with chain rule for complex compositions

This node sets the foundation: once “derivative = linear map = Jacobian matrix” feels natural, matrix calculus becomes mostly careful bookkeeping plus chain rule.

## Worked Examples (3)

### Compute a Jacobian and use it to linearize a vector-valued function

Let f: ℝ² → ℝ² be f(x, y) = (f₁(x, y), f₂(x, y)) where f₁(x, y) = x²y and f₂(x, y) = sin(x + y). Compute J\_f(x, y). Then linearize at (1, 0) to approximate f(1.02, −0.01).

1. Step 1: Compute partial derivatives for f₁(x, y) = x²y.

   ∂f₁/∂x = 2xy

   ∂f₁/∂y = x²
2. Step 2: Compute partial derivatives for f₂(x, y) = sin(x + y).

   ∂f₂/∂x = cos(x + y)

   ∂f₂/∂y = cos(x + y)
3. Step 3: Assemble the Jacobian matrix.

   J\_f(x, y) = [ 2xy x²

   cos(x+y) cos(x+y) ]
4. Step 4: Evaluate the Jacobian at (1, 0).

   J\_f(1, 0) = [ 2·1·0 1²

   cos(1+0) cos(1+0) ]

   = [ 0 1

   cos 1 cos 1 ]
5. Step 5: Compute f(1, 0).

   f(1, 0) = (1²·0, sin(1+0)) = (0, sin 1)
6. Step 6: Form the small displacement **h** from (1, 0) to (1.02, −0.01).

   **h** = (Δx, Δy) = (0.02, −0.01)
7. Step 7: Apply the linearization f(**a**+**h**) ≈ f(**a**) + J\_f(**a**) **h**.

   J\_f(1,0)**h** = [ 0 1

   cos1 cos1 ] [ 0.02

   −0.01 ]

   First component: 0·0.02 + 1·(−0.01) = −0.01

   Second component: cos1·0.02 + cos1·(−0.01) = cos1·(0.01) = 0.01 cos1
8. Step 8: Combine.

   f(1.02, −0.01) ≈ (0, sin1) + (−0.01, 0.01 cos1)

   = (−0.01, sin1 + 0.01 cos1)

**Insight:** The Jacobian turns “small input change” into “approximate output change” via matrix multiplication. Notice how the first output f₁ is most sensitive to y near (1,0) (since ∂f₁/∂x = 0 there), which is immediately visible in J\_f(1,0).

### Derive the polar-coordinate area factor using det(J)

Use the transformation f(r, θ) = (x, y) = (r cos θ, r sin θ). Compute det(J\_f) and show that dx dy = r dr dθ.

1. Step 1: Write the Jacobian matrix.

   J\_f(r, θ) = [ ∂x/∂r ∂x/∂θ

   ∂y/∂r ∂y/∂θ ]
2. Step 2: Compute the partial derivatives.

   ∂x/∂r = cos θ

   ∂x/∂θ = −r sin θ

   ∂y/∂r = sin θ

   ∂y/∂θ = r cos θ
3. Step 3: Substitute into the matrix.

   J\_f(r, θ) = [ cos θ −r sin θ

   sin θ r cos θ ]
4. Step 4: Compute the determinant.

   det(J\_f) = (cos θ)(r cos θ) − (−r sin θ)(sin θ)

   = r cos²θ + r sin²θ

   = r( cos²θ + sin²θ )

   = r
5. Step 5: Convert the area element.

   dx dy = |det(J\_f(r, θ))| dr dθ = |r| dr dθ

   In standard polar coordinates, r ≥ 0, so |r| = r.

   Therefore dx dy = r dr dθ.

**Insight:** The mysterious “extra r” in polar integrals is exactly local area scaling. A tiny rectangle of size dr×dθ in (r,θ)-space maps to a curved wedge-like region in (x,y)-space whose area is approximately r·dr·dθ.

### Use the Jacobian chain rule to differentiate a composition

Let f: ℝ² → ℝ² be f(x, y) = (u, v) = (x + y, x − y). Let g: ℝ² → ℝ² be g(u, v) = (u², uv). Compute J\_{g∘f}(x, y) using the chain rule.

1. Step 1: Compute J\_f(x, y).

   u = x + y ⇒ ∂u/∂x = 1, ∂u/∂y = 1

   v = x − y ⇒ ∂v/∂x = 1, ∂v/∂y = −1

   So J\_f(x, y) = [ 1 1

   1 −1 ]
2. Step 2: Compute J\_g(u, v).

   First component: g₁(u, v) = u²

   ∂g₁/∂u = 2u, ∂g₁/∂v = 0

   Second component: g₂(u, v) = uv

   ∂g₂/∂u = v, ∂g₂/∂v = u

   So J\_g(u, v) = [ 2u 0

   v u ]
3. Step 3: Apply the chain rule.

   J\_{g∘f}(x, y) = J\_g(f(x, y)) · J\_f(x, y)

   Substitute u = x + y and v = x − y:

   J\_g(f(x, y)) = [ 2(x+y) 0

   (x−y) (x+y) ]
4. Step 4: Multiply the matrices.

   J\_{g∘f} = [ 2(x+y) 0

   (x−y) (x+y) ] [ 1 1

   1 −1 ]

   Compute entry-by-entry:

   Top row:

   (1,1): 2(x+y)·1 + 0·1 = 2(x+y)

   (1,2): 2(x+y)·1 + 0·(−1) = 2(x+y)

   Bottom row:

   (2,1): (x−y)·1 + (x+y)·1 = (x−y)+(x+y)=2x

   (2,2): (x−y)·1 + (x+y)·(−1) = (x−y)−(x+y)=−2y

   So J\_{g∘f}(x, y) = [ 2(x+y) 2(x+y)

   2x −2y ]

**Insight:** The Jacobian chain rule is “just” matrix multiplication because derivatives are linear maps. Computing J\_g at (u,v) and then substituting (u,v)=f(x,y) keeps the structure clean and scales to long compositions.

## Key Takeaways

- ✓

  The Jacobian J\_f(**x**) = Df(**x**) is the m×n matrix with entries (∂f\_i/∂x\_j), describing first-order change of f: ℝⁿ → ℝᵐ.
- ✓

  Linearization: for small **h**, f(**a**+**h**) ≈ f(**a**) + J\_f(**a**) **h**; the Jacobian is the best linear approximation near **a**.
- ✓

  Columns of J\_f describe how the output changes when you perturb one input coordinate; rows are gradients of each output component (as row vectors).
- ✓

  Chain rule: J\_{g∘f}(**x**) = J\_g(f(**x**)) · J\_f(**x**)—composition becomes matrix multiplication.
- ✓

  When n = m, det(J\_f(**x**)) measures local oriented volume scaling; |det(J\_f(**x**))| is the local (unsigned) volume scale factor.
- ✓

  Change of variables in integrals uses d**x** = |det(J\_f(**u**))| d**u** for **x** = f(**u**).
- ✓

  Many “extra factors” in coordinate systems (like r in polar) are exactly Jacobian determinants.

## Common Mistakes

- ✗

  Mixing up the shape: for f: ℝⁿ → ℝᵐ, the Jacobian is m×n (outputs by inputs), not n×m.
- ✗

  Confusing ∇f with J\_f: the gradient is for scalar outputs; for vector outputs you need the full Jacobian (or one gradient per component).
- ✗

  Forgetting the absolute value in change-of-variables: integrals over regions use |det(J)|, not det(J) when det could be negative.
- ✗

  Evaluating J\_g at the wrong point in the chain rule: J\_{g∘f}(x) requires J\_g at f(x), not at x.

## Practice

easy

Let f(x, y, z) = (xy, yz). Compute J\_f(x, y, z). What is J\_f(1, 2, 3)?

**Hint:** There are m=2 outputs and n=3 inputs, so J is 2×3. Differentiate each output with respect to x, y, z.

Show solution

f₁=xy ⇒ ∂f₁/∂x=y, ∂f₁/∂y=x, ∂f₁/∂z=0.

f₂=yz ⇒ ∂f₂/∂x=0, ∂f₂/∂y=z, ∂f₂/∂z=y.

So J\_f(x,y,z) = [ y x 0

0 z y ].

At (1,2,3): J\_f(1,2,3) = [ 2 1 0

0 3 2 ].

medium

Let f: ℝ² → ℝ² be f(u, v) = (x, y) = (u² − v², 2uv). (This maps to complex squaring.) Compute det(J\_f(u, v)).

**Hint:** Compute ∂x/∂u, ∂x/∂v, ∂y/∂u, ∂y/∂v, then take a 2×2 determinant.

Show solution

x=u²−v² ⇒ ∂x/∂u=2u, ∂x/∂v=−2v.

y=2uv ⇒ ∂y/∂u=2v, ∂y/∂v=2u.

J\_f(u,v) = [ 2u −2v

2v 2u ].

det(J\_f) = (2u)(2u) − (−2v)(2v)

= 4u² + 4v²

= 4(u²+v²).

hard

Use a Jacobian to perform the substitution in the integral ∬\_R (x + y) dx dy where R is the parallelogram defined by x = u + v, y = u − v with (u, v) ∈ [0,1]×[0,1]. Compute the value.

**Hint:** Compute det(J\_f) for f(u,v)=(x,y). Rewrite x+y in terms of u,v. Then integrate over the unit square and multiply by |det(J\_f)|.

Show solution

Define f(u,v)=(x,y) with x=u+v, y=u−v.

Jacobian:

J\_f = [ ∂x/∂u ∂x/∂v

∂y/∂u ∂y/∂v ]

= [ 1 1

1 −1 ].

det(J\_f) = (1)(−1) − (1)(1) = −2, so |det(J\_f)|=2.

Rewrite integrand:

x+y = (u+v)+(u−v)=2u.

Change variables:

∬\_R (x+y) dx dy = ∬\_{[0,1]²} (2u) · 2 du dv = ∬\_{[0,1]²} 4u du dv.

Compute:

∫\_0^1 ∫\_0^1 4u dv du = ∫\_0^1 (4u·1) du = 4 ∫\_0^1 u du = 4·(1/2)=2.

## Connections

Next: [Matrix Calculus](/tech-tree/matrix-calculus/)

Related reinforcement nodes you may have seen:

- •[Gradients](/tech-tree/gradients/)
- •[Matrix Operations](/tech-tree/matrix-operations/)

Forward links this enables:

- •Jacobian chain rule → backprop-style differentiation in vector form
- •Jacobian determinant → multivariable substitution and probability density transforms

Quality: A (4.5/5)

[← back to tree](/tech-tree/)[browse all →](/tech-tree/inventory/)
