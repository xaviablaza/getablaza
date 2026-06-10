---
title: Multivariable Chain Rule
description: Derivatives of composed functions with multiple variables.
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
permalink: /tech-tree/chain-rule-multivar/
---

[←Back to Tech Tree](/tech-tree/)

[inventory](/tech-tree/inventory/)[coverage](/tech-tree/coverage/)

# Multivariable Chain Rule

CalculusDifficulty: ★★★☆☆Depth: 6Unlocks: 5

Derivatives of composed functions with multiple variables.

## Interactive Visualization

⏮◀◀▶▶STEP0.25x1xZOOM

t=0s

## Core Concepts

- -Structure of composition: an inner map from R^n to R^m and an outer map from R^m to R^p (track which variables feed into which function)
- -Derivative as the best linear approximation at a point, represented by the Jacobian matrix (matrix of partial derivatives)
- -Composition of linear maps is given by matrix multiplication (linear maps compose by multiplying their matrices)

## Key Symbols & Notation

D f (the Jacobian matrix / derivative of f)o (function composition)

## Essential Relationships

- -Chain rule (core formula): D(g o f)(x) = Dg(f(x)) \* Df(x) (matrix product; evaluate outer derivative at f(x))

## Prerequisites (2)

[Gradients5 atoms](/tech-tree/gradients/)[Derivative Rules5 atoms](/tech-tree/derivative-rules/)

## Unlocks (1)

[Backpropagationlvl 4](/tech-tree/backpropagation/)

Advanced Learning Details

### Graph Position

56

Depth Cost

5

Fan-Out (ROI)

2

Bottleneck Score

6

Chain Length

### Cognitive Load

6

Atomic Elements

24

Total Elements

L0

Percentile Level

L4

Atomic Level

### All Concepts (9)

- - Composition of multivariable maps: inner map g: R^k -> R^n and outer map f: R^n -> R^m (so f∘g: R^k -> R^m)
- - Total derivative (or differential) as a linear map at a point (best linear approximation of a multivariable function)
- - Jacobian matrix: the matrix representation of the total derivative for vector-valued functions
- - Derivative of vector-valued functions (componentwise partial derivatives assembled into a Jacobian)
- - Multivariable chain rule as a rule for composing total derivatives (not just scalar chain rule)
- - Component/summation form of the chain rule: expressing partials of a composition as sums over intermediate variables
- - Chain rule along a parameterized curve (rate of change of f along r(t): df/dt = ∇f(r(t)) · r'(t))
- - Evaluation-location dependence: derivatives of outer function must be evaluated at the inner function value (e.g., Df(g(x)))
- - Interpretation of the chain rule as composition of linear approximations (compose best linear approximations to get best linear approximation of composition)

### Teaching Strategy

Multi-session curriculum - substantial prior knowledge and complex material. Use mastery gates and deliberate practice.

In single-variable calculus, the chain rule is a one-line formula. In multivariable calculus, it’s the same idea—“derivatives multiply along a composition”—but the objects are linear maps, so the multiplication becomes matrix multiplication. Once you truly see that, backpropagation stops feeling like magic.

TL;DR:

For a composition h=f∘gh = f \circ gh=f∘g where g:Rn→Rmg: \mathbb{R}^n \to \mathbb{R}^mg:Rn→Rm and f:Rm→Rpf: \mathbb{R}^m \to \mathbb{R}^pf:Rm→Rp, the multivariable chain rule is

D(f∘g)(x)=Df(g(x)) Dg(x).D(f \circ g)(\mathbf{x}) = Df(g(\mathbf{x}))\, Dg(\mathbf{x}).D(f∘g)(x)=Df(g(x))Dg(x).

Interpretation: a small input perturbation Δx\Delta \mathbf{x}Δx is pushed forward by DgDgDg into Δu\Delta \mathbf{u}Δu, then pushed forward by DfDfDf into Δy\Delta \mathbf{y}Δy. For scalar output p=1p=1p=1, gradients pull back via transpose: ∇h(x)=Dg(x)⊤∇f(g(x))\nabla h(\mathbf{x}) = Dg(\mathbf{x})^\top \nabla f(g(\mathbf{x}))∇h(x)=Dg(x)⊤∇f(g(x)).

## What Is the Multivariable Chain Rule?

### Why you need a new-looking chain rule

In 1D, composition looks like h(x)=f(g(x))h(x) = f(g(x))h(x)=f(g(x)) and the chain rule says h′(x)=f′(g(x)) g′(x)h'(x) = f'(g(x))\, g'(x)h′(x)=f′(g(x))g′(x).

In multiple dimensions, you still compose functions, but now each function can take *multiple inputs* and produce *multiple outputs*. The “derivative” is no longer a single number; it’s a *linear map* that best approximates the function near a point. Linear maps are represented by matrices, so “multiply the derivatives” becomes “multiply the Jacobian matrices.”

This is the conceptual core:

- •**Derivative = best linear approximation** near a point.
- •**Jacobian matrix** = the matrix of partial derivatives that represents that linear approximation.
- •**Composition of linear maps** corresponds to **matrix multiplication**.

### The composition structure (track shapes)

The cleanest multivariable chain rule is written with a clear inner/outer structure:

- •Inner map: g:Rn→Rmg: \mathbb{R}^n \to \mathbb{R}^mg:Rn→Rm
- •Outer map: f:Rm→Rpf: \mathbb{R}^m \to \mathbb{R}^pf:Rm→Rp
- •Composition: h=f∘g:Rn→Rph = f \circ g: \mathbb{R}^n \to \mathbb{R}^ph=f∘g:Rn→Rp

Let:

- •input vector **x** ∈ ℝⁿ
- •intermediate vector **u** = g(**x**) ∈ ℝᵐ
- •output vector **y** = f(**u**) ∈ ℝᵖ

A quick “shape table” you should get used to:

| Object | Meaning | Shape |
| --- | --- | --- |
| **x** | input | n×1 |
| **u** = g(**x**) | intermediate | m×1 |
| **y** = f(**u**) | output | p×1 |
| Dg(x)Dg(\mathbf{x})Dg(x) | Jacobian of g at **x** | m×n |
| Df(u)Df(\mathbf{u})Df(u) | Jacobian of f at **u** | p×m |
| D(f∘g)(x)D(f\circ g)(\mathbf{x})D(f∘g)(x) | Jacobian of composition | p×n |

Notice the only multiplication that makes sense dimensionally is:

(p×m) (m×n)=(p×n).(p\times m)\,(m\times n) = (p\times n).(p×m)(m×n)=(p×n).

That is already a big part of the multivariable chain rule: the shapes *force* the correct order.

### The chain rule (matrix form)

The multivariable chain rule states:

D(f∘g)(x)=Df(g(x)) Dg(x).D(f \circ g)(\mathbf{x}) = Df(g(\mathbf{x}))\, Dg(\mathbf{x}).D(f∘g)(x)=Df(g(x))Dg(x).

Read it as: “first apply the derivative of ggg at **x**, then apply the derivative of fff at the resulting point g(x)g(\mathbf{x})g(x).”

### What it means geometrically (tiny perturbations)

If you perturb the input by a small vector Δx\Delta \mathbf{x}Δx, then:

1) **Push forward through g**:

Δu≈Dg(x) Δx.\Delta \mathbf{u} \approx Dg(\mathbf{x})\, \Delta \mathbf{x}.Δu≈Dg(x)Δx.

2) **Push forward through f**:

Δy≈Df(u) Δu.\Delta \mathbf{y} \approx Df(\mathbf{u})\, \Delta \mathbf{u}.Δy≈Df(u)Δu.

Combine them:

Δy≈Df(g(x)) Dg(x) Δx.\Delta \mathbf{y} \approx Df(g(\mathbf{x}))\, Dg(\mathbf{x})\, \Delta \mathbf{x}.Δy≈Df(g(x))Dg(x)Δx.

So the Jacobian of the composition is the matrix that takes Δx\Delta \mathbf{x}Δx directly to Δy\Delta \mathbf{y}Δy. That matrix is the product Df DgDf\,DgDfDg.

### A note on notation: Df vs ∇f

You said you know gradients already. The key is to keep these distinct:

- •DfDfDf is the **Jacobian** (a matrix, in general).
- •∇f\nabla f∇f is the **gradient** (a vector) and is defined when fff is scalar-valued: f:Rn→Rf: \mathbb{R}^n \to \mathbb{R}f:Rn→R.

When p=1p=1p=1, the Jacobian of fff is a 1×m row vector; the gradient is usually written as an m×1 column vector. They are transposes of each other (depending on convention):

Df(u) is 1×m,∇f(u) is m×1.Df(\mathbf{u}) \text{ is } 1\times m, \qquad \nabla f(\mathbf{u}) \text{ is } m\times 1.Df(u) is 1×m,∇f(u) is m×1.

This transpose issue matters a lot in backprop, so we’ll be explicit about it later.

## Core Mechanic 1: Derivative as Best Linear Approximation (and the Jacobian)

### Why this viewpoint

If you treat multivariable derivatives as “a bunch of partial derivatives,” you can still compute things, but it’s easy to lose track of structure.

If you treat the derivative as “the best linear map near a point,” everything becomes systematic:

- •You can *push forward* small changes.
- •You can *compose* derivatives by composing linear maps.
- •You can *check correctness* by verifying matrix shapes.

### The linear approximation definition

Let g:Rn→Rmg: \mathbb{R}^n \to \mathbb{R}^mg:Rn→Rm. We say ggg is differentiable at **x** if there exists a linear map L:Rn→RmL: \mathbb{R}^n \to \mathbb{R}^mL:Rn→Rm such that

g(x+Δx)≈g(x)+L Δxg(\mathbf{x} + \Delta \mathbf{x}) \approx g(\mathbf{x}) + L\,\Delta \mathbf{x}g(x+Δx)≈g(x)+LΔx

with an error that becomes negligible compared to ∥Δx∥\|\Delta \mathbf{x}\|∥Δx∥ as Δx→0\Delta \mathbf{x} \to 0Δx→0.

That linear map is the derivative Dg(x)Dg(\mathbf{x})Dg(x).

### Jacobian matrix: how the linear map is represented

Write g(x)=[g1(x)⋮gm(x)]g(\mathbf{x}) = \begin{bmatrix} g\_1(\mathbf{x}) \\ \vdots \\ g\_m(\mathbf{x}) \end{bmatrix}g(x)=​g1​(x)⋮gm​(x)​​.

Then the Jacobian Dg(x)Dg(\mathbf{x})Dg(x) is the m×n matrix:

Dg(x)=[∂g1∂x1⋯∂g1∂xn⋮⋱⋮∂gm∂x1⋯∂gm∂xn].Dg(\mathbf{x}) = \begin{bmatrix}
\frac{\partial g\_1}{\partial x\_1} & \cdots & \frac{\partial g\_1}{\partial x\_n} \\
\vdots & \ddots & \vdots \\
\frac{\partial g\_m}{\partial x\_1} & \cdots & \frac{\partial g\_m}{\partial x\_n}
\end{bmatrix}.Dg(x)=​∂x1​∂g1​​⋮∂x1​∂gm​​​⋯⋱⋯​∂xn​∂g1​​⋮∂xn​∂gm​​​​.

This is exactly the matrix that maps a small input perturbation to an approximate output perturbation:

Δu≈Dg(x) Δx.\Delta \mathbf{u} \approx Dg(\mathbf{x})\, \Delta \mathbf{x}.Δu≈Dg(x)Δx.

### Interactive-canvas mental model (shape-tracking + arrows)

Imagine an “interactive canvas” with three boxes:

1) **x-box**: **x** ∈ ℝⁿ

2) **u-box**: **u** = g(**x**) ∈ ℝᵐ

3) **y-box**: **y** = f(**u**) ∈ ℝᵖ

Now add two kinds of arrows:

#### Arrow type A: pushforward of perturbations (forward mode)

You draw a little arrow Δx\Delta \mathbf{x}Δx at the input.

- •It transforms to Δu=Dg Δx\Delta \mathbf{u} = Dg\, \Delta \mathbf{x}Δu=DgΔx.
- •Then transforms to Δy=Df Δu\Delta \mathbf{y} = Df\, \Delta \mathbf{u}Δy=DfΔu.

So perturbations flow **with** the function direction.

#### Arrow type B: pullback of sensitivities / gradients (reverse mode)

If the final output is scalar (p=1), you draw a gradient arrow at the output: ∇yℓ\nabla\_{\mathbf{y}} \ell∇y​ℓ (often just 1 if the scalar is the loss itself).

Then gradients flow **backwards** through transposes:

- •sensitivity at **u**: ∇uℓ=Df(u)⊤∇yℓ\nabla\_{\mathbf{u}} \ell = Df(\mathbf{u})^\top \nabla\_{\mathbf{y}} \ell∇u​ℓ=Df(u)⊤∇y​ℓ
- •sensitivity at **x**: ∇xℓ=Dg(x)⊤∇uℓ\nabla\_{\mathbf{x}} \ell = Dg(\mathbf{x})^\top \nabla\_{\mathbf{u}} \ell∇x​ℓ=Dg(x)⊤∇u​ℓ

This is the heart of backprop. In this lesson, we’re building the “transpose reflex”:

- •**Perturbations push forward with $J$**.
- •**Gradients pull back with $J^\top$**.

### A small but crucial convention check

There are two common conventions:

1) Jacobian is m×n (outputs by inputs). Gradients are column vectors.

2) Jacobian is n×m (inputs by outputs). Gradients are row vectors.

We’ll use the most common ML convention:

- •**Jacobian $Dg$ is m×n**.
- •**Gradient $\nabla f$ is n×1** for scalar f.

With that convention, the chain rule for scalar output becomes a clean transpose pullback (we’ll derive it soon).

## Core Mechanic 2: Chain Rule = Composition of Linear Maps (Matrix Multiplication)

### Why matrix multiplication appears

The multivariable chain rule is not a new rule you memorize. It is a consequence of one fact:

> If you approximate each function by a linear map near the relevant point, then approximating the composition means composing those linear maps.

And linear maps compose by matrix multiplication.

### Derivation (showing the work)

Let g:Rn→Rmg: \mathbb{R}^n \to \mathbb{R}^mg:Rn→Rm and f:Rm→Rpf: \mathbb{R}^m \to \mathbb{R}^pf:Rm→Rp.

Define:

- •**u** = g(**x**)
- •**y** = f(**u**) = (f\circ g)(**x**)

Start with a small perturbation Δx\Delta \mathbf{x}Δx.

**Step 1: Linearize g at x**

g(x+Δx)≈g(x)+Dg(x) Δx.g(\mathbf{x}+\Delta\mathbf{x}) \approx g(\mathbf{x}) + Dg(\mathbf{x})\,\Delta\mathbf{x}.g(x+Δx)≈g(x)+Dg(x)Δx.

Let Δu=Dg(x) Δx\Delta \mathbf{u} = Dg(\mathbf{x})\,\Delta\mathbf{x}Δu=Dg(x)Δx, so

g(x+Δx)≈u+Δu.g(\mathbf{x}+\Delta\mathbf{x}) \approx \mathbf{u} + \Delta\mathbf{u}.g(x+Δx)≈u+Δu.

**Step 2: Linearize f at u**

f(u+Δu)≈f(u)+Df(u) Δu.f(\mathbf{u}+\Delta\mathbf{u}) \approx f(\mathbf{u}) + Df(\mathbf{u})\,\Delta\mathbf{u}.f(u+Δu)≈f(u)+Df(u)Δu.

Substitute Δu=Dg(x) Δx\Delta \mathbf{u} = Dg(\mathbf{x})\,\Delta\mathbf{x}Δu=Dg(x)Δx:

f(u+Δu)≈f(u)+Df(u) Dg(x) Δx.f(\mathbf{u}+\Delta\mathbf{u}) \approx f(\mathbf{u}) + Df(\mathbf{u})\,Dg(\mathbf{x})\,\Delta\mathbf{x}.f(u+Δu)≈f(u)+Df(u)Dg(x)Δx.

But the left side is approximately

f(g(x+Δx))=(f∘g)(x+Δx).f(g(\mathbf{x}+\Delta\mathbf{x})) = (f\circ g)(\mathbf{x}+\Delta\mathbf{x}).f(g(x+Δx))=(f∘g)(x+Δx).

So we have the linear approximation:

(f∘g)(x+Δx)≈(f∘g)(x)+(Df(g(x)) Dg(x)) Δx.(f\circ g)(\mathbf{x}+\Delta\mathbf{x}) \approx (f\circ g)(\mathbf{x}) + \bigl(Df(g(\mathbf{x}))\,Dg(\mathbf{x})\bigr)\,\Delta\mathbf{x}.(f∘g)(x+Δx)≈(f∘g)(x)+(Df(g(x))Dg(x))Δx.

By uniqueness of the best linear approximation, the derivative must be:

D(f∘g)(x)=Df(g(x)) Dg(x).D(f \circ g)(\mathbf{x}) = Df(g(\mathbf{x}))\,Dg(\mathbf{x}).D(f∘g)(x)=Df(g(x))Dg(x).

That’s the multivariable chain rule.

### Element-wise chain rule (path-tracing through indices)

Sometimes you want the version that looks like “sum over paths.”

Let h=f∘gh = f \circ gh=f∘g with components:

- •gk(x)g\_k(\mathbf{x})gk​(x) for k = 1..m
- •fi(u)f\_i(\mathbf{u})fi​(u) for i = 1..p
- •hi(x)=fi(g(x))h\_i(\mathbf{x}) = f\_i(g(\mathbf{x}))hi​(x)=fi​(g(x))

Then for each output component i and input component j:

∂hi∂xj(x)=∑k=1m∂fi∂uk(u) ∂gk∂xj(x),u=g(x).\frac{\partial h\_i}{\partial x\_j}(\mathbf{x}) = \sum\_{k=1}^{m} \frac{\partial f\_i}{\partial u\_k}(\mathbf{u})\,\frac{\partial g\_k}{\partial x\_j}(\mathbf{x}),\quad \mathbf{u}=g(\mathbf{x}).∂xj​∂hi​​(x)=k=1∑m​∂uk​∂fi​​(u)∂xj​∂gk​​(x),u=g(x).

This is literally matrix multiplication in coordinates.

**Path-tracing interpretation:**

- •Each term ∂fi∂uk ∂gk∂xj\frac{\partial f\_i}{\partial u\_k}\,\frac{\partial g\_k}{\partial x\_j}∂uk​∂fi​​∂xj​∂gk​​ corresponds to a path xj→uk→yix\_j \to u\_k \to y\_ixj​→uk​→yi​.
- •You add contributions from all intermediate coordinates uku\_kuk​.

### “Computational graph” view (interactive canvas)

Think of a small graph:

- •Nodes are variables (scalars or vectors).
- •Edges are functions.

For our two-layer composition:

**x** →(g)→ **u** →(f)→ **y**

On an interactive canvas, you can show two overlays:

#### Overlay 1: Jacobians on edges

- •edge **x**→**u** labeled Dg(x)Dg(\mathbf{x})Dg(x) (m×n)
- •edge **u**→**y** labeled Df(u)Df(\mathbf{u})Df(u) (p×m)

To get total derivative **x**→**y**, multiply along the path:

Dxy=Df Dg.D\_{\mathbf{x}}\mathbf{y} = Df\,Dg.Dx​y=DfDg.

#### Overlay 2: live perturbations and gradients

Pick a concrete point **x**₀.

- •Drag **x** by a tiny Δx\Delta \mathbf{x}Δx. The canvas updates **u** and **y** and also shows the predicted linear response Df Dg ΔxDf\,Dg\,\Delta \mathbf{x}DfDgΔx.
- •Alternatively, set a scalar loss ℓ=ϕ(y)\ell = \phi(\mathbf{y})ℓ=ϕ(y) (or just take p=1). Show a gradient vector at **y** and animate it flowing backward:

∇xℓ=Dg(x)⊤ Df(u)⊤ ∇yℓ.\nabla\_{\mathbf{x}}\ell = Dg(\mathbf{x})^\top\,Df(\mathbf{u})^\top\,\nabla\_{\mathbf{y}}\ell.∇x​ℓ=Dg(x)⊤Df(u)⊤∇y​ℓ.

This “two-way animation” is the visualization you want to internalize:

- •**Forward:** Δ\DeltaΔ vectors multiply by Jacobians.
- •**Backward:** gradients multiply by Jacobian transposes.

### Scalar output special case (gradient form)

Now suppose f:Rm→Rf: \mathbb{R}^m \to \mathbb{R}f:Rm→R is scalar. Then Df(u)Df(\mathbf{u})Df(u) is 1×m.

From the Jacobian chain rule:

D(f∘g)(x)=Df(u) Dg(x).D(f\circ g)(\mathbf{x}) = Df(\mathbf{u})\,Dg(\mathbf{x}).D(f∘g)(x)=Df(u)Dg(x).

This left side is a 1×n row vector. If we want the gradient as an n×1 column vector, transpose:

\begin{align\*}

\nabla (f\circ g)(\mathbf{x})

&= D(f\circ g)(\mathbf{x})^\top \\

&= \bigl(Df(\mathbf{u})\,Dg(\mathbf{x})\bigr)^\top \\

&= Dg(\mathbf{x})^\top\,Df(\mathbf{u})^\top \\

&= Dg(\mathbf{x})^\top\,\nabla f(\mathbf{u}).

\end{align\*}

That last line is the standard “gradient chain rule” used everywhere in ML.

### One more composition (three layers)

If you have x→gu→fv→ry\mathbf{x} \xrightarrow{g} \mathbf{u} \xrightarrow{f} \mathbf{v} \xrightarrow{r} \mathbf{y}xg​uf​vr​y, then:

D(r∘f∘g)(x)=Dr(v) Df(u) Dg(x).D(r\circ f\circ g)(\mathbf{x}) = Dr(\mathbf{v})\,Df(\mathbf{u})\,Dg(\mathbf{x}).D(r∘f∘g)(x)=Dr(v)Df(u)Dg(x).

Forward-mode perturbations multiply left-to-right in the same order as the functions apply (inner to outer).

Reverse-mode gradients multiply by transposes right-to-left:

∇xℓ=Dg(x)⊤ Df(u)⊤ Dr(v)⊤ ∇yℓ.\nabla\_{\mathbf{x}}\ell = Dg(\mathbf{x})^\top\,Df(\mathbf{u})^\top\,Dr(\mathbf{v})^\top\,\nabla\_{\mathbf{y}}\ell.∇x​ℓ=Dg(x)⊤Df(u)⊤Dr(v)⊤∇y​ℓ.

This is backprop in one line—just applied repeatedly.

## Application/Connection: From Multivariable Chain Rule to Backprop Intuition

### Why this matters for ML

Neural networks are compositions of many vector-valued functions:

x→h(1)→h(2)→⋯→y^→ℓ.\mathbf{x} \to \mathbf{h}^{(1)} \to \mathbf{h}^{(2)} \to \cdots \to \hat{\mathbf{y}} \to \ell.x→h(1)→h(2)→⋯→y^​→ℓ.

Training requires ∇θℓ\nabla\_{\theta}\ell∇θ​ℓ, gradients with respect to parameters. The only tool you need conceptually is the multivariable chain rule, but applied efficiently.

The hard part is not the calculus; it’s **bookkeeping**:

- •What depends on what?
- •What is the shape of each Jacobian?
- •Are we pushing perturbations forward or pulling gradients back?

### A concrete computational graph (with explicit shapes)

Let’s build a tiny “network” with one hidden layer and a scalar loss. Define:

- •**x** ∈ ℝ²
- •Parameters:
- •WWW ∈ ℝ^{3×2}, **b** ∈ ℝ³
- •**c** ∈ ℝ³ (a vector used to reduce to scalar)

Forward computation:

1) **a** = Wx+bW\mathbf{x} + \mathbf{b}Wx+b (so **a** ∈ ℝ³)

2) **h** = σ(a)\sigma(\mathbf{a})σ(a) elementwise (so **h** ∈ ℝ³)

3) ℓ=c⊤h\ell = \mathbf{c}^\top \mathbf{h}ℓ=c⊤h (so ℓ\ellℓ ∈ ℝ)

This is a composition:

**x** →(affine)→ **a** →(nonlinearity)→ **h** →(dot)→ ℓ

On an interactive canvas, you can attach:

| Edge | Local derivative | Shape |
| --- | --- | --- |
| **x**→**a** | Dxa=WD\_{\mathbf{x}}\mathbf{a} = WDx​a=W | 3×2 |
| **a**→**h** | Dah=Diag⁡(σ′(a))D\_{\mathbf{a}}\mathbf{h} = \operatorname{Diag}(\sigma'(\mathbf{a}))Da​h=Diag(σ′(a)) | 3×3 |
| **h**→ℓ | Dhℓ=c⊤D\_{\mathbf{h}}\ell = \mathbf{c}^\topDh​ℓ=c⊤ | 1×3 |

#### Forward-mode (push a perturbation)

A perturbation Δx\Delta \mathbf{x}Δx produces:

\begin{align\*}

\Delta \mathbf{a} &\approx W\,\Delta \mathbf{x} \\

\Delta \mathbf{h} &\approx \operatorname{Diag}(\sigma'(\mathbf{a}))\,\Delta \mathbf{a} \\

\Delta \ell &\approx \mathbf{c}^\top\,\Delta \mathbf{h}.

\end{align\*}

Combine:

Δℓ≈c⊤ Diag⁡(σ′(a)) W Δx.\Delta \ell \approx \mathbf{c}^\top\,\operatorname{Diag}(\sigma'(\mathbf{a}))\,W\,\Delta \mathbf{x}.Δℓ≈c⊤Diag(σ′(a))WΔx.

So the total Jacobian (1×2 row vector) is:

Dxℓ=c⊤ Diag⁡(σ′(a)) W.D\_{\mathbf{x}}\ell = \mathbf{c}^\top\,\operatorname{Diag}(\sigma'(\mathbf{a}))\,W.Dx​ℓ=c⊤Diag(σ′(a))W.

#### Reverse-mode (pull back a gradient)

Because ℓ is scalar, we typically want ∇xℓ\nabla\_{\mathbf{x}}\ell∇x​ℓ as a 2×1 column vector.

Start with ∇ℓℓ=1\nabla\_{\ell}\ell = 1∇ℓ​ℓ=1.

- •From ℓ = **c**ᵀ**h**:

∇hℓ=c.\nabla\_{\mathbf{h}}\ell = \mathbf{c}.∇h​ℓ=c.

- •Through **h** = σ(**a**) elementwise:

∇aℓ=Diag⁡(σ′(a)) ∇hℓ=Diag⁡(σ′(a)) c.\nabla\_{\mathbf{a}}\ell = \operatorname{Diag}(\sigma'(\mathbf{a}))\,\nabla\_{\mathbf{h}}\ell = \operatorname{Diag}(\sigma'(\mathbf{a}))\,\mathbf{c}.∇a​ℓ=Diag(σ′(a))∇h​ℓ=Diag(σ′(a))c.

- •Through **a** = Wx+bW\mathbf{x}+\mathbf{b}Wx+b:

∇xℓ=W⊤ ∇aℓ=W⊤ Diag⁡(σ′(a)) c.\nabla\_{\mathbf{x}}\ell = W^\top\,\nabla\_{\mathbf{a}}\ell = W^\top\,\operatorname{Diag}(\sigma'(\mathbf{a}))\,\mathbf{c}.∇x​ℓ=W⊤∇a​ℓ=W⊤Diag(σ′(a))c.

Compare with the forward-mode Jacobian expression above:

- •DxℓD\_{\mathbf{x}}\ellDx​ℓ (row) = **c**ᵀ Diag(σ′) W
- •∇xℓ\nabla\_{\mathbf{x}}\ell∇x​ℓ (column) = W⊤W^\topW⊤ Diag(σ′) **c**

They are transposes, consistent with ∇ℓ=(Dℓ)⊤\nabla \ell = (D\ell)^\top∇ℓ=(Dℓ)⊤.

### Visual intuition: pushforward vs pullback

To address visualization explicitly, here’s the picture you should rehearse:

1) Pick a point **x**₀.

2) Draw a tiny arrow Δx\Delta \mathbf{x}Δx at **x**.

3) Multiply by local Jacobians to watch the arrow morph:

- •it rotates/scales/shears in **a**-space,
- •then again in **h**-space,
- •finally collapses to a scalar change Δℓ\Delta \ellΔℓ.

Now reverse:

1) Draw a gradient arrow at **h**: it points in the direction that increases ℓ fastest in **h**-space.

2) Pull it back to **a** using the transpose of the local Jacobian: Diag⁡(σ′)\operatorname{Diag}(\sigma')Diag(σ′) (symmetric here, so transpose doesn’t change it).

3) Pull it back to **x** using W⊤W^\topW⊤.

This is not two unrelated processes. It’s the same linear maps viewed from two dual perspectives:

- •perturbations: Δ\DeltaΔ vectors (tangent vectors)
- •gradients: covectors, pulled back by transpose

You don’t need the formal differential-geometry language to use it correctly, but you *do* need the operational rule:

> If forward uses JJJ, backward uses J⊤J^\topJ⊤.

### Connection you’ll use next

Backpropagation is essentially the repeated application of:

∇inputℓ=J⊤ ∇outputℓ.\nabla\_{\text{input}}\ell = J^\top\,\nabla\_{\text{output}}\ell.∇input​ℓ=J⊤∇output​ℓ.

where JJJ is the Jacobian of a local block in the computational graph.

Once you’re comfortable multiplying Jacobians (forward) and multiplying by transposes (backward), you’re ready to study backprop as an algorithmic optimization: reuse intermediate results so you don’t form huge Jacobian matrices explicitly.

## Worked Examples (3)

### Matrix-form chain rule with a 2→2→1 composition (shape-check + gradient)

Let g:R2→R2g: \mathbb{R}^2 \to \mathbb{R}^2g:R2→R2 and f:R2→Rf: \mathbb{R}^2 \to \mathbb{R}f:R2→R be

g(x1,x2)=[u1u2]=[x12+x2x1x2],f(u1,u2)=u1+u22.g(x\_1,x\_2) = \begin{bmatrix} u\_1 \\ u\_2 \end{bmatrix} = \begin{bmatrix} x\_1^2 + x\_2 \\ x\_1x\_2 \end{bmatrix}, \qquad f(u\_1,u\_2)= u\_1 + u\_2^2.g(x1​,x2​)=[u1​u2​​]=[x12​+x2​x1​x2​​],f(u1​,u2​)=u1​+u22​.

Define h=f∘gh = f\circ gh=f∘g. Compute Dh(x)Dh(\mathbf{x})Dh(x) and ∇h(x)\nabla h(\mathbf{x})∇h(x) at a general point, then evaluate at (x1,x2)=(1,2)(x\_1,x\_2)=(1,2)(x1​,x2​)=(1,2).

1. Step 1: Compute Dg(x)Dg(\mathbf{x})Dg(x) (2×2).

   We have

   - •u1=x12+x2u\_1 = x\_1^2 + x\_2u1​=x12​+x2​ so ∂u1/∂x1=2x1\partial u\_1/\partial x\_1 = 2x\_1∂u1​/∂x1​=2x1​, ∂u1/∂x2=1\partial u\_1/\partial x\_2 = 1∂u1​/∂x2​=1.
   - •u2=x1x2u\_2 = x\_1x\_2u2​=x1​x2​ so ∂u2/∂x1=x2\partial u\_2/\partial x\_1 = x\_2∂u2​/∂x1​=x2​, ∂u2/∂x2=x1\partial u\_2/\partial x\_2 = x\_1∂u2​/∂x2​=x1​.

   Thus

   Dg(x)=[2x11x2x1].Dg(\mathbf{x}) = \begin{bmatrix} 2x\_1 & 1 \\ x\_2 & x\_1 \end{bmatrix}.Dg(x)=[2x1​x2​​1x1​​].
2. Step 2: Compute Df(u)Df(\mathbf{u})Df(u) (1×2).

   f(u1,u2)=u1+u22f(u\_1,u\_2)=u\_1 + u\_2^2f(u1​,u2​)=u1​+u22​ so

   Df(u)=[∂f/∂u1∂f/∂u2]=[12u2].Df(\mathbf{u}) = \begin{bmatrix} \partial f/\partial u\_1 & \partial f/\partial u\_2 \end{bmatrix} = \begin{bmatrix} 1 & 2u\_2 \end{bmatrix}.Df(u)=[∂f/∂u1​​∂f/∂u2​​]=[1​2u2​​].
3. Step 3: Apply the Jacobian chain rule.

   Dh(x)=Df(g(x)) Dg(x).Dh(\mathbf{x}) = Df(g(\mathbf{x}))\,Dg(\mathbf{x}).Dh(x)=Df(g(x))Dg(x).

   Substitute u2=x1x2u\_2 = x\_1x\_2u2​=x1​x2​:

   Df(g(x))=[12x1x2].Df(g(\mathbf{x})) = \begin{bmatrix} 1 & 2x\_1x\_2 \end{bmatrix}.Df(g(x))=[1​2x1​x2​​].

   Now multiply:

   \begin{align\*}

   Dh(\mathbf{x})

   &= \begin{bmatrix} 1 & 2x\_1x\_2 \end{bmatrix}

   \begin{bmatrix} 2x\_1 & 1 \\ x\_2 & x\_1 \end{bmatrix} \\

   &= \begin{bmatrix}

   1\cdot 2x\_1 + (2x\_1x\_2)\cdot x\_2 \; , \; 1\cdot 1 + (2x\_1x\_2)\cdot x\_1

   \end{bmatrix} \\

   &= \begin{bmatrix}

   2x\_1 + 2x\_1x\_2^2 \; , \; 1 + 2x\_1^2x\_2

   \end{bmatrix}.

   \end{align\*}
4. Step 4: Convert to gradient (column vector).

   Since hhh is scalar, DhDhDh is 1×2 and

   ∇h(x)=Dh(x)⊤=[2x1+2x1x221+2x12x2].\nabla h(\mathbf{x}) = Dh(\mathbf{x})^\top = \begin{bmatrix} 2x\_1 + 2x\_1x\_2^2 \\ 1 + 2x\_1^2x\_2 \end{bmatrix}.∇h(x)=Dh(x)⊤=[2x1​+2x1​x22​1+2x12​x2​​].
5. Step 5: Evaluate at (1,2).

   ∇h(1,2)=[2⋅1+2⋅1⋅221+2⋅12⋅2]=[2+81+4]=[105].\nabla h(1,2)=\begin{bmatrix}2\cdot 1 + 2\cdot 1\cdot 2^2 \\ 1 + 2\cdot 1^2\cdot 2\end{bmatrix}=
   \begin{bmatrix}2+8\\1+4\end{bmatrix}=
   \begin{bmatrix}10\\5\end{bmatrix}.∇h(1,2)=[2⋅1+2⋅1⋅221+2⋅12⋅2​]=[2+81+4​]=[105​].

**Insight:** The computation stayed organized because we never mixed ‘partial derivative rules’ randomly. We computed two local Jacobians with clear shapes (2×2 and 1×2), multiplied them in the only shape-consistent order, then transposed to get the gradient vector.

### Pushforward vs pullback on a small computational graph (explicit J and Jᵀ)

Let **x** ∈ ℝ². Define

1) **u** = g(**x**) where g(x1,x2)=[u1u2]=[x1+2x2x1−x2]g(x\_1,x\_2) = \begin{bmatrix} u\_1 \\ u\_2 \end{bmatrix} = \begin{bmatrix} x\_1 + 2x\_2 \\ x\_1 - x\_2 \end{bmatrix}g(x1​,x2​)=[u1​u2​​]=[x1​+2x2​x1​−x2​​]

2) scalar output ℓ=f(u)\ell = f(\mathbf{u})ℓ=f(u) where f(u1,u2)=u12+3u2f(u\_1,u\_2)= u\_1^2 + 3u\_2f(u1​,u2​)=u12​+3u2​

At **x**₀ = (1,1), compute:

- •(A) the predicted scalar change Δℓ\Delta \ellΔℓ for a small perturbation Δx=(0.01,−0.02)\Delta \mathbf{x} = (0.01, -0.02)Δx=(0.01,−0.02) using pushforward
- •(B) the gradient ∇xℓ\nabla\_{\mathbf{x}}\ell∇x​ℓ using pullback

1. Step 1: Compute the forward values at **x**₀.

   At (1,1):

   - •u=g(1,1)=[1+2⋅11−1]=[30]\mathbf{u} = g(1,1) = \begin{bmatrix} 1+2\cdot 1 \\ 1-1 \end{bmatrix} = \begin{bmatrix} 3 \\ 0 \end{bmatrix}u=g(1,1)=[1+2⋅11−1​]=[30​].
   - •ℓ=f(3,0)=32+3⋅0=9\ell = f(3,0)= 3^2 + 3\cdot 0 = 9ℓ=f(3,0)=32+3⋅0=9.
2. Step 2: Pushforward (perturbations use Jacobians).

   Compute Dg(x)Dg(\mathbf{x})Dg(x) (2×2). Since g is linear,

   Dg=[∂u1/∂x1∂u1/∂x2∂u2/∂x1∂u2/∂x2]=[121−1].Dg = \begin{bmatrix} \partial u\_1/\partial x\_1 & \partial u\_1/\partial x\_2 \\ \partial u\_2/\partial x\_1 & \partial u\_2/\partial x\_2 \end{bmatrix} = \begin{bmatrix} 1 & 2 \\ 1 & -1 \end{bmatrix}.Dg=[∂u1​/∂x1​∂u2​/∂x1​​∂u1​/∂x2​∂u2​/∂x2​​]=[11​2−1​].

   Compute Df(u)Df(\mathbf{u})Df(u) (1×2):

   Df(u)=[2u13].Df(\mathbf{u})=\begin{bmatrix}2u\_1 & 3\end{bmatrix}.Df(u)=[2u1​​3​].

   At **u** = (3,0):

   Df(u)=[63].Df(\mathbf{u}) = \begin{bmatrix} 6 & 3 \end{bmatrix}.Df(u)=[6​3​].

   Now push Δx\Delta \mathbf{x}Δx forward:

   Δu≈Dg Δx=[121−1][0.01−0.02]=[0.01−0.040.01+0.02]=[−0.030.03].\Delta \mathbf{u} \approx Dg\,\Delta \mathbf{x} = \begin{bmatrix} 1 & 2 \\ 1 & -1 \end{bmatrix}\begin{bmatrix} 0.01 \\ -0.02 \end{bmatrix} = \begin{bmatrix} 0.01-0.04 \\ 0.01+0.02 \end{bmatrix} = \begin{bmatrix} -0.03 \\ 0.03 \end{bmatrix}.Δu≈DgΔx=[11​2−1​][0.01−0.02​]=[0.01−0.040.01+0.02​]=[−0.030.03​].

   Then

   Δℓ≈Df Δu=[63][−0.030.03]=6(−0.03)+3(0.03)=−0.18+0.09=−0.09.\Delta \ell \approx Df\,\Delta \mathbf{u} = \begin{bmatrix}6 & 3\end{bmatrix}\begin{bmatrix}-0.03\\0.03\end{bmatrix} = 6(-0.03)+3(0.03) = -0.18+0.09 = -0.09.Δℓ≈DfΔu=[6​3​][−0.030.03​]=6(−0.03)+3(0.03)=−0.18+0.09=−0.09.
3. Step 3: Pullback (gradients use transposes).

   Because ℓ\ellℓ is scalar, start with ∇uℓ\nabla\_{\mathbf{u}}\ell∇u​ℓ:

   ∇uℓ=[∂ℓ/∂u1∂ℓ/∂u2]=[2u13].\nabla\_{\mathbf{u}}\ell = \begin{bmatrix} \partial \ell/\partial u\_1 \\ \partial \ell/\partial u\_2 \end{bmatrix} = \begin{bmatrix}2u\_1\\3\end{bmatrix}.∇u​ℓ=[∂ℓ/∂u1​∂ℓ/∂u2​​]=[2u1​3​].

   At **u**=(3,0):

   ∇uℓ=[63].\nabla\_{\mathbf{u}}\ell = \begin{bmatrix}6\\3\end{bmatrix}.∇u​ℓ=[63​].

   Now pull back through g using Dg⊤Dg^\topDg⊤:

   ∇xℓ=Dg⊤ ∇uℓ=[112−1][63]=[912−3]=[99].\nabla\_{\mathbf{x}}\ell = Dg^\top\,\nabla\_{\mathbf{u}}\ell = \begin{bmatrix} 1 & 1 \\ 2 & -1 \end{bmatrix}\begin{bmatrix}6\\3\end{bmatrix} = \begin{bmatrix}9\\12-3\end{bmatrix} = \begin{bmatrix}9\\9\end{bmatrix}.∇x​ℓ=Dg⊤∇u​ℓ=[12​1−1​][63​]=[912−3​]=[99​].
4. Step 4: Consistency check via dot product.

   The linear prediction should satisfy

   Δℓ≈∇xℓ⋅Δx.\Delta \ell \approx \nabla\_{\mathbf{x}}\ell \cdot \Delta \mathbf{x}.Δℓ≈∇x​ℓ⋅Δx.

   Compute:

   [99]⋅[0.01−0.02]=9(0.01)+9(−0.02)=0.09−0.18=−0.09,\begin{bmatrix}9\\9\end{bmatrix}\cdot\begin{bmatrix}0.01\\-0.02\end{bmatrix} = 9(0.01)+9(-0.02)=0.09-0.18=-0.09,[99​]⋅[0.01−0.02​]=9(0.01)+9(−0.02)=0.09−0.18=−0.09,

   matching the pushforward result.

**Insight:** This example makes the duality visible: forward-mode computes the effect of a small move Δx\Delta \mathbf{x}Δx; reverse-mode computes the gradient that, when dotted with Δx\Delta \mathbf{x}Δx, predicts the same Δℓ\Delta \ellΔℓ. The transpose is exactly what makes those two views consistent.

### Element-wise chain rule as “sum over intermediate coordinates”

Let g:R3→R2g: \mathbb{R}^3\to\mathbb{R}^2g:R3→R2 and f:R2→R2f: \mathbb{R}^2\to\mathbb{R}^2f:R2→R2 be

g(x1,x2,x3)=[u1u2]=[x1x2x2+x32],f(u1,u2)=[y1y2]=[u1+u2u1u2].g(x\_1,x\_2,x\_3)=\begin{bmatrix}u\_1\\u\_2\end{bmatrix}=\begin{bmatrix}x\_1x\_2\\x\_2+x\_3^2\end{bmatrix},\qquad f(u\_1,u\_2)=\begin{bmatrix}y\_1\\y\_2\end{bmatrix}=\begin{bmatrix}u\_1+u\_2\\u\_1u\_2\end{bmatrix}.g(x1​,x2​,x3​)=[u1​u2​​]=[x1​x2​x2​+x32​​],f(u1​,u2​)=[y1​y2​​]=[u1​+u2​u1​u2​​].

Compute ∂y2∂x3\frac{\partial y\_2}{\partial x\_3}∂x3​∂y2​​ at a general point using path-tracing.

1. Step 1: Identify the dependency paths.

   We want y2=u1u2y\_2 = u\_1u\_2y2​=u1​u2​.

   - •u1=x1x2u\_1 = x\_1x\_2u1​=x1​x2​ does NOT depend on x3x\_3x3​.
   - •u2=x2+x32u\_2 = x\_2 + x\_3^2u2​=x2​+x32​ DOES depend on x3x\_3x3​.

   So only paths through u2u\_2u2​ matter for ∂y2/∂x3\partial y\_2/\partial x\_3∂y2​/∂x3​.
2. Step 2: Apply the coordinate chain rule.

   Use

   ∂y2∂x3=∑k=12∂y2∂uk∂uk∂x3.\frac{\partial y\_2}{\partial x\_3} = \sum\_{k=1}^{2}\frac{\partial y\_2}{\partial u\_k}\frac{\partial u\_k}{\partial x\_3}.∂x3​∂y2​​=k=1∑2​∂uk​∂y2​​∂x3​∂uk​​.

   Compute each factor:

   - •∂y2∂u1=∂(u1u2)∂u1=u2\frac{\partial y\_2}{\partial u\_1} = \frac{\partial (u\_1u\_2)}{\partial u\_1} = u\_2∂u1​∂y2​​=∂u1​∂(u1​u2​)​=u2​
   - •∂y2∂u2=∂(u1u2)∂u2=u1\frac{\partial y\_2}{\partial u\_2} = \frac{\partial (u\_1u\_2)}{\partial u\_2} = u\_1∂u2​∂y2​​=∂u2​∂(u1​u2​)​=u1​
   - •∂u1∂x3=0\frac{\partial u\_1}{\partial x\_3} = 0∂x3​∂u1​​=0
   - •∂u2∂x3=2x3\frac{\partial u\_2}{\partial x\_3} = 2x\_3∂x3​∂u2​​=2x3​
3. Step 3: Sum over k.

   \begin{align\*}

   \frac{\partial y\_2}{\partial x\_3}

   &= \left(\frac{\partial y\_2}{\partial u\_1}\right)\left(\frac{\partial u\_1}{\partial x\_3}\right) + \left(\frac{\partial y\_2}{\partial u\_2}\right)\left(\frac{\partial u\_2}{\partial x\_3}\right) \\

   &= (u\_2)(0) + (u\_1)(2x\_3) \\

   &= 2x\_3\,u\_1 \\

   &= 2x\_3\,(x\_1x\_2).

   \end{align\*}

**Insight:** The summation form is ‘matrix multiplication with indices.’ It forces you to enumerate intermediate coordinates uku\_kuk​ and add their contributions—exactly like summing over all paths in a computational graph.

## Key Takeaways

- ✓

  A multivariable derivative is best understood as a linear map; its matrix representation is the Jacobian.
- ✓

  For g:Rn→Rmg: \mathbb{R}^n\to\mathbb{R}^mg:Rn→Rm and f:Rm→Rpf: \mathbb{R}^m\to\mathbb{R}^pf:Rm→Rp, the chain rule is $D(f∘g)(x)=Df(g(x)) Dg(x).D(f\circ g)(\mathbf{x}) = Df(g(\mathbf{x}))\,Dg(\mathbf{x}).D(f∘g)(x)=Df(g(x))Dg(x).$
- ✓

  Shape-tracking is a correctness tool: (p×m)(m×n)=(p×n)(p\times m)(m\times n)=(p\times n)(p×m)(m×n)=(p×n) is the only order that composes.
- ✓

  Perturbations push forward: Δu≈J Δx\Delta \mathbf{u} \approx J\,\Delta \mathbf{x}Δu≈JΔx.
- ✓

  Gradients pull back: for scalar output, ∇xℓ=J⊤ ∇uℓ\nabla\_{\mathbf{x}}\ell = J^\top\,\nabla\_{\mathbf{u}}\ell∇x​ℓ=J⊤∇u​ℓ.
- ✓

  The coordinate form $∂hi∂xj=∑k∂fi∂uk∂gk∂xj\frac{\partial h\_i}{\partial x\_j} = \sum\_k \frac{\partial f\_i}{\partial u\_k}\frac{\partial g\_k}{\partial x\_j}∂xj​∂hi​​=∑k​∂uk​∂fi​​∂xj​∂gk​​$ is the same rule as matrix multiplication, interpreted as ‘sum over intermediate coordinates.’
- ✓

  Backpropagation is repeated application of the pullback rule (multiply by local Jacobian transposes) along a computational graph.

## Common Mistakes

- ✗

  Multiplying Jacobians in the wrong order (forgetting that composition order reverses: outer derivative on the left).
- ✗

  Mixing up Jacobians (matrices) and gradients (vectors), especially the row-vs-column convention; forgetting the transpose when converting DℓD\ellDℓ to ∇ℓ\nabla \ell∇ℓ.
- ✗

  Trying to build the full Jacobian for a large network when you only need Jacobian-vector products (forward mode) or Jacobianᵀ-vector products (reverse mode).
- ✗

  Losing track of which variables each function actually depends on; missing or adding dependency paths in the summation form.

## Practice

easy

Let g:R2→R3g: \mathbb{R}^2\to\mathbb{R}^3g:R2→R3 be g(x1,x2)=(x1,  x1x2,  x22)g(x\_1,x\_2)=(x\_1,\; x\_1x\_2,\; x\_2^2)g(x1​,x2​)=(x1​,x1​x2​,x22​) and let f:R3→Rf: \mathbb{R}^3\to\mathbb{R}f:R3→R be f(u1,u2,u3)=2u1−u2+u3f(u\_1,u\_2,u\_3)=2u\_1-u\_2+u\_3f(u1​,u2​,u3​)=2u1​−u2​+u3​. Compute ∇(f∘g)(x)\nabla (f\circ g)(\mathbf{x})∇(f∘g)(x).

**Hint:** Compute Dg(x)Dg(\mathbf{x})Dg(x) (3×2) and ∇f(u)\nabla f(\mathbf{u})∇f(u) (3×1). Then use ∇(f∘g)=Dg⊤∇f\nabla (f\circ g)=Dg^\top\nabla f∇(f∘g)=Dg⊤∇f.

Show solution

We have ∇f(u)=[2−11]\nabla f(\mathbf{u}) = \begin{bmatrix}2\\-1\\1\end{bmatrix}∇f(u)=​2−11​​.

Compute

Dg(x)=[∂u1/∂x1∂u1/∂x2∂u2/∂x1∂u2/∂x2∂u3/∂x1∂u3/∂x2]=[10x2x102x2].Dg(\mathbf{x})=\begin{bmatrix}
\partial u\_1/\partial x\_1 & \partial u\_1/\partial x\_2 \\
\partial u\_2/\partial x\_1 & \partial u\_2/\partial x\_2 \\
\partial u\_3/\partial x\_1 & \partial u\_3/\partial x\_2
\end{bmatrix}
=
\begin{bmatrix}
1 & 0 \\
x\_2 & x\_1 \\
0 & 2x\_2
\end{bmatrix}.Dg(x)=​∂u1​/∂x1​∂u2​/∂x1​∂u3​/∂x1​​∂u1​/∂x2​∂u2​/∂x2​∂u3​/∂x2​​​=​1x2​0​0x1​2x2​​​.

Then

∇(f∘g)(x)=Dg(x)⊤ ∇f=[1x200x12x2][2−11]=[2−x2−x1+2x2].\nabla (f\circ g)(\mathbf{x}) = Dg(\mathbf{x})^\top\,\nabla f = \begin{bmatrix}1 & x\_2 & 0\\0 & x\_1 & 2x\_2\end{bmatrix}\begin{bmatrix}2\\-1\\1\end{bmatrix} = \begin{bmatrix}2-x\_2\\-x\_1+2x\_2\end{bmatrix}.∇(f∘g)(x)=Dg(x)⊤∇f=[10​x2​x1​​02x2​​]​2−11​​=[2−x2​−x1​+2x2​​].

medium

Suppose g:Rn→Rmg: \mathbb{R}^n\to\mathbb{R}^mg:Rn→Rm and f:Rm→Rpf: \mathbb{R}^m\to\mathbb{R}^pf:Rm→Rp. You are told Dg(x)Dg(\mathbf{x})Dg(x) is m×n and Df(u)Df(\mathbf{u})Df(u) is p×m. What is the shape of D(f∘g)(x)D(f\circ g)(\mathbf{x})D(f∘g)(x)? Also, if p=1p=1p=1, what is the shape of ∇(f∘g)(x)\nabla (f\circ g)(\mathbf{x})∇(f∘g)(x) (as a column vector)?

**Hint:** Use matrix multiplication shapes. For p=1p=1p=1, the Jacobian is 1×n and the gradient is its transpose.

Show solution

D(f∘g)(x)=Df(g(x)) Dg(x)D(f\circ g)(\mathbf{x}) = Df(g(\mathbf{x}))\,Dg(\mathbf{x})D(f∘g)(x)=Df(g(x))Dg(x) has shape (p×m)(m×n) = p×n.

If p=1p=1p=1, then D(f∘g)D(f\circ g)D(f∘g) is 1×n, so the gradient ∇(f∘g)\nabla (f\circ g)∇(f∘g) (column) has shape n×1.

hard

Let **u** = g(**x**) with g:R2→R2g: \mathbb{R}^2\to\mathbb{R}^2g:R2→R2 given by u1=x12u\_1=x\_1^2u1​=x12​, u2=sin⁡(x2)u\_2=\sin(x\_2)u2​=sin(x2​). Let scalar ℓ=f(u)\ell=f(\mathbf{u})ℓ=f(u) with f(u1,u2)=u1u2f(u\_1,u\_2)=u\_1u\_2f(u1​,u2​)=u1​u2​. Compute ∇xℓ\nabla\_{\mathbf{x}}\ell∇x​ℓ.

**Hint:** Compute ∇uℓ\nabla\_{\mathbf{u}}\ell∇u​ℓ first, then multiply by Dg(x)⊤Dg(\mathbf{x})^\topDg(x)⊤. Remember DgDgDg is 2×2 and diagonal here.

Show solution

First, ℓ=u1u2\ell=u\_1u\_2ℓ=u1​u2​ so

∇uℓ=[∂ℓ/∂u1∂ℓ/∂u2]=[u2u1].\nabla\_{\mathbf{u}}\ell = \begin{bmatrix}\partial \ell/\partial u\_1\\\partial \ell/\partial u\_2\end{bmatrix} = \begin{bmatrix}u\_2\\u\_1\end{bmatrix}.∇u​ℓ=[∂ℓ/∂u1​∂ℓ/∂u2​​]=[u2​u1​​].

Next, Dg(x)Dg(\mathbf{x})Dg(x):

- •u1=x12u\_1=x\_1^2u1​=x12​ so ∂u1/∂x1=2x1\partial u\_1/\partial x\_1=2x\_1∂u1​/∂x1​=2x1​, ∂u1/∂x2=0\partial u\_1/\partial x\_2=0∂u1​/∂x2​=0
- •u2=sin⁡(x2)u\_2=\sin(x\_2)u2​=sin(x2​) so ∂u2/∂x1=0\partial u\_2/\partial x\_1=0∂u2​/∂x1​=0, ∂u2/∂x2=cos⁡(x2)\partial u\_2/\partial x\_2=\cos(x\_2)∂u2​/∂x2​=cos(x2​)

Thus

Dg(x)=[2x100cos⁡(x2)].Dg(\mathbf{x})=\begin{bmatrix}2x\_1 & 0\\0 & \cos(x\_2)\end{bmatrix}.Dg(x)=[2x1​0​0cos(x2​)​].

So

∇xℓ=Dg(x)⊤ ∇uℓ=[2x100cos⁡(x2)][u2u1]=[2x1sin⁡(x2)x12cos⁡(x2)].\nabla\_{\mathbf{x}}\ell = Dg(\mathbf{x})^\top\,\nabla\_{\mathbf{u}}\ell = \begin{bmatrix}2x\_1 & 0\\0 & \cos(x\_2)\end{bmatrix}\begin{bmatrix}u\_2\\u\_1\end{bmatrix} = \begin{bmatrix}2x\_1\sin(x\_2)\\x\_1^2\cos(x\_2)\end{bmatrix}.∇x​ℓ=Dg(x)⊤∇u​ℓ=[2x1​0​0cos(x2​)​][u2​u1​​]=[2x1​sin(x2​)x12​cos(x2​)​].

## Connections

Next up: apply this rule repeatedly and efficiently in neural networks.

- •[Backpropagation](/tech-tree/backpropagation/)

Related supporting nodes you may also want:

- •[Gradients](/tech-tree/gradients/)
- •[Jacobians](/tech-tree/jacobians/)
- •[Computational Graphs](/tech-tree/computational-graphs/)

Quality: A (4.5/5)

[← back to tree](/tech-tree/)[browse all →](/tech-tree/inventory/)
