---
title: Gradient Descent
description: Iteratively moving in negative gradient direction to minimize.
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
permalink: /tech-tree/gradient-descent/
---

[←Back to Tech Tree](/tech-tree/)

[inventory](/tech-tree/inventory/)[coverage](/tech-tree/coverage/)

# Gradient Descent

OptimizationDifficulty: ★★★☆☆Depth: 7Unlocks: 37

Iteratively moving in negative gradient direction to minimize.

## Interactive Visualization

⏮◀◀▶▶STEP0.25x1xZOOM

t=0s

## Core Concepts

- -Negative gradient is the local direction of steepest decrease of the objective function
- -A scalar step size (learning rate) scales how far to move along that direction and controls stability/speed
- -Repeat the scaled negative-gradient move iteratively to produce a sequence of parameter updates

## Key Symbols & Notation

alpha: step size (learning rate), a positive scalarx\_t: parameter vector (value at iteration t)

## Essential Relationships

- -Update rule (fundamental connection): next parameters = current parameters minus step size times gradient at current parameters (x\_{t+1} = x\_t - alpha \* gradient f(x\_t))

## Prerequisites (2)

[Gradients5 atoms](/tech-tree/gradients/)[Optimization Introduction5 atoms](/tech-tree/optimization-intro/)

## Unlocks (5)

[Machine Learning Introductionlvl 3](/tech-tree/ml-intro/)[Convex Optimizationlvl 4](/tech-tree/convex-optimization/)[Logistic Regressionlvl 3](/tech-tree/logistic-regression/)[Stochastic Gradient Descentlvl 4](/tech-tree/sgd/)[Conjugate Gradient Methodslvl 5](/tech-tree/conjugate-gradients/)

## Referenced by (2)

Where this concept shows up in the operating-finance and personal-finance graphs.

### From Business (2)

[Feedback LoopBusiness

The training loop is a feedback loop: compute loss on current parameters → compute gradient → update parameters → recompute loss. Each iteration's output (updated weights) becomes the next iteration's input, iteratively closing the gap to a minimum.](/business/feedback-loop/)[ExecutionBusiness

Demand 'pulling' is a gradient signal on the market loss surface. Orthogonal execution means your step vector has zero projection onto the gradient - effort magnitude is nonzero but progress toward the optimum is zero regardless of step size (execution quality).](/business/execution/)

Advanced Learning Details

### Graph Position

61

Depth Cost

37

Fan-Out (ROI)

16

Bottleneck Score

7

Chain Length

### Cognitive Load

6

Atomic Elements

28

Total Elements

L1

Percentile Level

L4

Atomic Level

### All Concepts (11)

- - Steepest descent as the negative gradient direction (moving opposite the gradient decreases the objective)
- - Iterative update rule: updating parameters repeatedly to approach a minimum
- - Learning rate / step size (single scalar that scales the gradient step)
- - Iteration indexing (discrete time steps t, k for successive updates)
- - Stopping criteria for an iterative algorithm (e.g., gradient norm threshold, change in parameters, max iterations)
- - Convergence to a stationary point (algorithm approaches a point where gradient ≈ 0)
- - Local vs. global minima in the context of iterative descent (GD may converge to local minima or saddle points)
- - Sensitivity of behaviour to step size (small step → slow progress; large step → overshoot/divergence/oscillation)
- - Step-size schedules (constant vs. decreasing step sizes across iterations)
- - Batch gradient descent distinction implicitly implied by using the full gradient at each iteration (as opposed to stochastic variants)
- - Practical termination/diagnostic quantities (objective value decrease per step, gradient norm, or parameter change used to decide when to stop)

### Teaching Strategy

Multi-session curriculum - substantial prior knowledge and complex material. Use mastery gates and deliberate practice.

You already know what a gradient is: it points uphill. Gradient descent is the art of repeatedly stepping downhill—carefully—so your objective function gets smaller and smaller until further improvement is hard or unnecessary.

TL;DR:

Gradient descent minimizes a differentiable function f(**x**) by iterating **x**ₜ₊₁ = **x**ₜ − α ∇f(**x**ₜ). The negative gradient gives the local direction of steepest decrease, and the step size α controls how far you move—too big can diverge, too small can crawl. You stop when progress (or gradient size) is small enough.

## What Is Gradient Descent?

## The problem it solves

In optimization, you often want to choose parameters **x** (a vector) to minimize some objective function:

- •Minimize f(**x**) over **x** ∈ ℝⁿ

In machine learning, f is frequently a *loss function* measuring how wrong your model is on data. In engineering, f might be energy, cost, or error.

Sometimes you can solve ∇f(**x**) = **0** exactly, but often:

- •f is complicated (many variables, messy algebra)
- •f has no closed-form minimizer
- •you only can compute f and ∇f numerically

So we want an *iterative* method: start somewhere, improve step-by-step.

## The key idea: “go downhill”

You already know:

- •∇f(**x**) points in the direction of steepest *increase* of f (locally).

So the direction of steepest *decrease* is:

- •−∇f(**x**)

Gradient descent turns this into an update rule:

- •pick a starting point **x**₀
- •for t = 0, 1, 2, …:
- •compute the gradient **g**ₜ = ∇f(**x**ₜ)
- •update **x**ₜ₊₁ = **x**ₜ − α **g**ₜ

Here α > 0 is the **step size** (learning rate). It is a scalar that controls how far you move along the downhill direction.

## Why it’s called “descent”

Imagine f(**x**) as a height function over a landscape. At your current position **x**ₜ, the gradient is the direction of steepest uphill; stepping in the negative gradient points you down the steepest slope available *using only local information*.

This local nature matters:

- •Gradient descent does not “see” the whole landscape.
- •It makes greedy local steps based on the slope at the current point.

## What gradient descent guarantees (and what it doesn’t)

Gradient descent is simple and powerful, but its behavior depends on the shape of f.

- •If f is **convex** and smooth (nice curvature), gradient descent with an appropriate α converges to the global minimum.
- •If f is **non-convex**, gradient descent can converge to local minima, saddle points, or flat regions.

Even in non-convex settings (like deep learning), it’s still widely used because:

- •it scales to huge parameter spaces
- •it only needs gradients
- •it often finds good solutions in practice

## The canonical formula

You’ll see this update everywhere:

**x**ₜ₊₁ = **x**ₜ − α ∇f(**x**ₜ)

Keep a mental model:

- •direction = −∇f(**x**ₜ)
- •distance = α · ‖∇f(**x**ₜ)‖

So α controls stability and speed, while the gradient magnitude reflects how steep the landscape is at **x**ₜ.

## Core Mechanic 1: Why the Negative Gradient Is the Steepest Decrease Direction

## Why we need a “best local direction”

At **x**, there are infinitely many directions you could move. We want the one that decreases f the fastest *for a tiny step*.

So ask: if we take a small step ε in a unit direction **u** (‖**u**‖ = 1), how does f change?

## Directional derivative connects gradients to change

For differentiable f, the first-order approximation (Taylor expansion) is:

f(**x** + ε**u**) ≈ f(**x**) + ε ∇f(**x**) · **u**

So the *rate of change* in direction **u** is:

D₍**u**₎ f(**x**) = ∇f(**x**) · **u**

We want the direction **u** that minimizes this quantity (most negative), under the constraint ‖**u**‖ = 1.

## Turning it into a clean optimization problem

We want:

minimize over **u**: ∇f(**x**) · **u**

subject to: ‖**u**‖ = 1

Let **g** = ∇f(**x**). Then the objective is **g** · **u**.

By Cauchy–Schwarz:

**g** · **u** ≥ −‖**g**‖ ‖**u**‖ = −‖**g**‖

Since ‖**u**‖ = 1, we get:

**g** · **u** ≥ −‖**g**‖

Equality happens when **u** points exactly opposite to **g**:

**u** = −**g** / ‖**g**‖

So:

- •the best unit direction for decreasing f is **u** = −∇f(**x**) / ‖∇f(**x**)‖
- •the steepest decrease rate is −‖∇f(**x**)‖

## What this means for the algorithm

Gradient descent chooses this direction and then decides **how far** to move with α.

If you rewrote the update using a unit direction:

Let **u**ₜ = −∇f(**x**ₜ) / ‖∇f(**x**ₜ)‖

Then:

**x**ₜ₊₁ = **x**ₜ + (α ‖∇f(**x**ₜ)‖) **u**ₜ

So the step length is α ‖∇f(**x**ₜ)‖.

This explains an important behavior:

- •When gradients are large, steps are larger.
- •When gradients are small (near a stationary point), steps shrink.

## First-order thinking (and its limits)

The “steepest decrease” statement is *local* and *first-order*.

- •It relies on the linear approximation f(**x** + Δ**x**) ≈ f(**x**) + ∇f(**x**)·Δ**x**.
- •If you take too large a step, curvature matters, and the approximation can be misleading.

That’s exactly why the next ingredient—step size α—matters so much.

## Core Mechanic 2: Step Size (Learning Rate) and Stability

## Why α is the make-or-break knob

The update rule has a single explicit hyperparameter:

**x**ₜ₊₁ = **x**ₜ − α ∇f(**x**ₜ)

But α does multiple jobs:

- •controls how fast you move (progress per step)
- •controls stability (whether you overshoot and bounce/diverge)
- •affects final accuracy (small α can “fine tune” better)

If gradient descent feels like “just walk downhill,” α is how big your stride is.

## A concrete 1D picture

Consider 1D f(x). The update is:

xₜ₊₁ = xₜ − α f′(xₜ)

If f is a simple bowl (like a quadratic), then:

- •small α: slow but steady, like taking tiny steps
- •large α: you might jump past the minimum and oscillate
- •too large α: oscillations grow and you diverge

This isn’t a subtle effect—it’s often the difference between learning and exploding.

## Quadratic case: you can see stability algebraically

Quadratics are the “physics sandbox” of optimization. Let:

f(**x**) = 1/2 **x**ᵀ **A** **x** (assume **A** is symmetric positive definite)

Then:

∇f(**x**) = **A** **x**

Gradient descent becomes:

**x**ₜ₊₁ = **x**ₜ − α **A** **x**ₜ

= (**I** − α **A**) **x**ₜ

So the behavior depends on the matrix (**I** − α **A**). If its eigenvalues are within (−1, 1), iterates shrink toward 0.

Let λᵢ be eigenvalues of **A** (all positive). Eigenvalues of (**I** − α **A**) are (1 − α λᵢ). We need:

|1 − α λᵢ| < 1 for all i

Solve it:

−1 < 1 − α λᵢ < 1

Left inequality:

−1 < 1 − α λᵢ

α λᵢ < 2

α < 2/λᵢ

Right inequality:

1 − α λᵢ < 1

−α λᵢ < 0

α > 0

So the condition for all i is:

0 < α < 2/λₘₐₓ

This is a clean statement:

- •α must be below a threshold set by the *largest curvature* direction.

If λₘₐₓ is huge (steep direction), α must be small to avoid instability.

## The speed problem: ill-conditioning

Even if you pick α stable, convergence can still be slow if **A** is ill-conditioned.

Define condition number:

κ = λₘₐₓ / λₘᵢₙ

When κ is large, the bowl is stretched: steep in some directions, flat in others. Then:

- •α limited by λₘₐₓ (stability)
- •but progress along flat directions depends on λₘᵢₙ (slow)

So you may see “zig-zagging” down a narrow valley.

This is a major motivation for:

- •feature scaling / normalization
- •preconditioning
- •momentum methods
- •conjugate gradients (especially for quadratics)

## Fixed α vs adaptive α

There are two common philosophies:

| Approach | What you choose | Pros | Cons |
| --- | --- | --- | --- |
| Fixed learning rate | constant α | simple, cheap | must tune carefully; can stall or diverge |
| Step size schedule | αₜ decreases over time | can be stable + accurate | schedule design matters |
| Line search | choose α each step to reduce f | less tuning; robust | extra computation per step |

In many ML settings, you’ll see schedules like:

- •αₜ = α₀ / (1 + k t)
- •αₜ = α₀ · γᵗ

But the core concept remains: α is a stability-speed trade-off.

## Practical stopping criteria

Gradient descent is iterative, so you must decide when to stop. Common criteria:

- •Gradient small: ‖∇f(**x**ₜ)‖ ≤ ε
- •Step small: ‖**x**ₜ₊₁ − **x**ₜ‖ ≤ ε
- •Objective improvement small: |f(**x**ₜ₊₁) − f(**x**ₜ)| ≤ ε
- •Max iterations reached

Each criterion has a “why”:

- •small gradient means you’re near a stationary point
- •small step means updates aren’t changing parameters much
- •small improvement means you’re not gaining value per compute

In ML, you’ll also stop based on validation performance (generalization), not just training loss.

## Application/Connection: Gradient Descent in Machine Learning Workflows

## Why gradient descent is the default optimizer in ML

Many models are trained by minimizing an average loss:

f(**w**) = (1/n) ∑ᵢ₌₁ⁿ ℓᵢ(**w**)

Here **w** are model parameters (weights), and ℓᵢ measures error on example i.

Two key reasons gradient descent fits ML so well:

1) **Modularity**: If you can compute ∇f, you can train.

2) **Scalability**: Each step costs about “one gradient computation,” which is manageable even in large dimensions.

For linear regression, logistic regression, neural nets—this pattern repeats.

## Batch gradient descent vs stochastic gradient descent

Plain gradient descent (often called *batch* GD in ML) computes the full gradient over all data:

∇f(**w**) = (1/n) ∑ᵢ ∇ℓᵢ(**w**)

This can be expensive when n is large.

SGD (and mini-batch SGD) approximates the gradient using a subset of examples. Conceptually:

- •GD: exact average gradient
- •SGD: noisy estimate of that average

You’ll unlock SGD soon; for now, notice what remains the same:

- •update direction is still “negative gradient” (or an estimate)
- •learning rate still controls stability/speed

## Example: logistic regression connection

Logistic regression minimizes cross-entropy loss. Even if you don’t have the full formula memorized, the training loop is the same:

- •initialize **w**₀
- •repeat:
- •compute gradient of loss wrt **w**
- •update **w** ← **w** − α ∇loss(**w**)

This is why gradient descent is often taught before specific ML models: it’s the shared engine underneath.

## Interpreting “learning” as optimization

In supervised learning, you often hear:

- •“the model learns weights”

Operationally, it means:

- •we run an optimization algorithm that reduces loss

Gradient descent gives you a clean mental map:

- •parameters **x**ₜ evolve over time
- •each iteration nudges parameters toward lower loss
- •training curves (loss vs iteration) visualize this descent

## Geometry you should keep in mind

Even without fancy second-order methods, you can improve GD performance by shaping the landscape:

- •**Feature scaling**: makes curvature more uniform → less zig-zag
- •**Good initialization**: starts you in a better region
- •**Regularization**: adds terms like (λ/2)‖**w**‖², which changes curvature and can help stability/generalization

For example, with L2 regularization:

f(**w**) = data\_loss(**w**) + (λ/2)‖**w**‖²

Then:

∇f(**w**) = ∇data\_loss(**w**) + λ **w**

So gradient descent update becomes:

**w**ₜ₊₁ = **w**ₜ − α (∇data\_loss(**w**ₜ) + λ **w**ₜ)

= (1 − αλ)**w**ₜ − α ∇data\_loss(**w**ₜ)

This shows a neat interpretation:

- •the regularization term shrinks weights toward 0 each step (weight decay).

## When to consider other optimizers

Gradient descent is foundational, but not always the most efficient choice.

A rough comparison:

| Method | Uses | Typical strength | Typical weakness |
| --- | --- | --- | --- |
| Gradient descent | ∇f | simple, general | can be slow on ill-conditioned problems |
| Conjugate gradients | structure of quadratics | very fast for quadratic/linear systems | less direct for non-quadratic, needs careful usage |
| Newton / quasi-Newton | ∇f and (approx) Hessian | fast local convergence | expensive per step in high dimensions |
| SGD / mini-batch | noisy ∇f | scales to huge data | requires more tuning; noisy convergence |

Learning gradient descent well makes all of these easier, because most are variations on “choose direction + choose step size.”

## Worked Examples (3)

### Example 1 (1D): Gradient descent on a quadratic and the effect of α

Minimize f(x) = (x − 3)². Start at x₀ = 0. Compare α = 0.1 vs α = 1.1 for a few steps.

1. Compute derivative:

   f(x) = (x − 3)²

   f′(x) = 2(x − 3)
2. Gradient descent update in 1D:

   xₜ₊₁ = xₜ − α f′(xₜ)

   = xₜ − α · 2(xₜ − 3)

   = xₜ − 2α xₜ + 6α

   = (1 − 2α) xₜ + 6α
3. Case A: α = 0.1

   Update rule: xₜ₊₁ = (1 − 0.2) xₜ + 0.6 = 0.8 xₜ + 0.6

   Compute iterates:

   x₀ = 0

   x₁ = 0.8·0 + 0.6 = 0.6

   x₂ = 0.8·0.6 + 0.6 = 1.08

   x₃ = 0.8·1.08 + 0.6 = 1.464

   x₄ = 0.8·1.464 + 0.6 = 1.7712

   (It moves steadily toward 3.)
4. Case B: α = 1.1

   Update rule: xₜ₊₁ = (1 − 2.2) xₜ + 6.6 = (−1.2) xₜ + 6.6

   Compute iterates:

   x₀ = 0

   x₁ = −1.2·0 + 6.6 = 6.6

   x₂ = −1.2·6.6 + 6.6 = −1.32

   x₃ = −1.2·(−1.32) + 6.6 = 8.184

   x₄ = −1.2·8.184 + 6.6 = −3.2208

   (It oscillates wildly and grows in magnitude.)
5. Interpret stability from the coefficient (1 − 2α):

   For convergence we need |1 − 2α| < 1

   Solve:

   −1 < 1 − 2α < 1

   Left: −1 < 1 − 2α ⇒ 2α < 2 ⇒ α < 1

   Right: 1 − 2α < 1 ⇒ α > 0

   So 0 < α < 1 is stable here.

   α = 1.1 violates it, so divergence makes sense.

**Insight:** Even in the friendliest possible objective (a perfect parabola), α determines whether you converge smoothly, oscillate, or blow up. Stability is not optional tuning—it is part of the algorithm.

### Example 2 (2D): One gradient descent step with full vector math

Minimize f(**x**) = x₁² + 4x₂². Start at **x**₀ = [2, 1]ᵀ. Use α = 0.2. Compute **x**₁ and show that f decreases.

1. Write **x** = [x₁, x₂]ᵀ. Compute the gradient:

   f(**x**) = x₁² + 4x₂²

   ∂f/∂x₁ = 2x₁

   ∂f/∂x₂ = 8x₂

   So:

   ∇f(**x**) = [2x₁, 8x₂]ᵀ
2. Evaluate at **x**₀ = [2, 1]ᵀ:

   ∇f(**x**₀) = [2·2, 8·1]ᵀ = [4, 8]ᵀ
3. Apply gradient descent update:

   **x**₁ = **x**₀ − α ∇f(**x**₀)

   = [2, 1]ᵀ − 0.2[4, 8]ᵀ

   = [2 − 0.8, 1 − 1.6]ᵀ

   = [1.2, −0.6]ᵀ
4. Check objective value decreases:

   f(**x**₀) = 2² + 4·1² = 4 + 4 = 8

   f(**x**₁) = 1.2² + 4·(−0.6)²

   = 1.44 + 4·0.36

   = 1.44 + 1.44

   = 2.88

   So f decreased from 8 to 2.88 in one step.
5. Geometric note:

   The curvature in x₂ direction is larger (coefficient 4), so the gradient component in x₂ is scaled more (8x₂ vs 2x₁). This creates the typical behavior: stronger pull (and stricter stability) in steep directions.

**Insight:** Gradients encode anisotropic steepness: directions with higher curvature produce larger gradient components, which affects both progress and the maximum stable α.

### Example 3 (Quadratic in matrix form): Deriving the GD update and stability bound

Let f(**x**) = 1/2 **x**ᵀ **A** **x** with **A** symmetric positive definite. Show ∇f(**x**) = **A** **x**, derive **x**ₜ₊₁ = (**I** − α**A**)**x**ₜ, and state the stability condition in terms of λₘₐₓ.

1. Compute gradient (known result for symmetric **A**):

   f(**x**) = 1/2 **x**ᵀ **A** **x**

   ∇f(**x**) = **A** **x**
2. Gradient descent update:

   **x**ₜ₊₁ = **x**ₜ − α ∇f(**x**ₜ)

   = **x**ₜ − α **A** **x**ₜ

   = (**I** − α **A**) **x**ₜ
3. Diagonalize **A**:

   Because **A** is symmetric, **A** = **Q**Λ**Q**ᵀ with orthonormal **Q**, diagonal Λ with entries λᵢ > 0.
4. Transform coordinates **z**ₜ = **Q**ᵀ **x**ₜ:

   **x**ₜ = **Q** **z**ₜ

   **x**ₜ₊₁ = (**I** − α **Q**Λ**Q**ᵀ) **Q** **z**ₜ

   = **Q**(**I** − αΛ)**z**ₜ

   So:

   **z**ₜ₊₁ = (**I** − αΛ)**z**ₜ
5. Coordinate-wise behavior:

   zᵢ,ₜ₊₁ = (1 − αλᵢ) zᵢ,ₜ

   For convergence we need |1 − αλᵢ| < 1 for all i.
6. Solve for α:

   |1 − αλᵢ| < 1

   ⇒ −1 < 1 − αλᵢ < 1

   ⇒ 0 < α < 2/λᵢ

   To satisfy all i, require:

   0 < α < 2/λₘₐₓ

**Insight:** The largest eigenvalue λₘₐₓ (steepest curvature direction) sets the global stability limit for a fixed learning rate on a quadratic.

## Key Takeaways

- ✓

  Gradient descent iterates **x**ₜ₊₁ = **x**ₜ − α ∇f(**x**ₜ) to minimize a differentiable objective f(**x**).
- ✓

  The negative gradient −∇f(**x**) is the direction of steepest local decrease because it minimizes the directional derivative under ‖**u**‖ = 1.
- ✓

  The learning rate α controls step length; too small makes progress slow, too large can cause oscillation or divergence.
- ✓

  For quadratics f(**x**) = 1/2 **x**ᵀ**A****x**, stability with fixed α requires 0 < α < 2/λₘₐₓ.
- ✓

  Ill-conditioning (large κ = λₘₐₓ/λₘᵢₙ) explains zig-zagging and slow convergence even when α is stable.
- ✓

  Stopping criteria are typically based on small gradient norm, small parameter changes, small objective improvement, or iteration budget.
- ✓

  Gradient descent is the core training engine behind many ML models; SGD is a scalable noisy variant of the same principle.

## Common Mistakes

- ✗

  Using the wrong sign: updating **x** ← **x** + α∇f(**x**) performs gradient ascent, increasing the objective.
- ✗

  Choosing α without checking stability: a learning rate that is slightly too large can make loss explode or oscillate indefinitely.
- ✗

  Assuming GD always finds the global minimum: for non-convex objectives, it may converge to local minima or saddle points.
- ✗

  Stopping solely because iterations are done, without checking whether ‖∇f(**x**ₜ)‖ or the loss improvement has actually become small.

## Practice

easy

Let f(x) = x². Start at x₀ = 5.

1) Write the gradient descent update.

2) For α = 0.4 compute x₁, x₂, x₃.

3) For which α does this 1D quadratic converge?

**Hint:** Compute f′(x) and simplify xₜ₊₁ in terms of xₜ. Convergence requires |multiplier| < 1.

Show solution

1) f′(x) = 2x, so xₜ₊₁ = xₜ − α·2xₜ = (1 − 2α)xₜ.

2) With α = 0.4, multiplier = 1 − 0.8 = 0.2:

x₁ = 0.2·5 = 1

x₂ = 0.2·1 = 0.2

x₃ = 0.2·0.2 = 0.04

3) Need |1 − 2α| < 1 ⇒ 0 < α < 1.

medium

Minimize f(**x**) = (x₁ − 1)² + (x₂ + 2)².

Start at **x**₀ = [3, 0]ᵀ and use α = 0.5.

Compute ∇f(**x**), then compute **x**₁. What is f(**x**₀) and f(**x**₁)?

**Hint:** Differentiate each squared term: ∂/∂x (x − c)² = 2(x − c).

Show solution

∇f(**x**) = [2(x₁ − 1), 2(x₂ + 2)]ᵀ.

At **x**₀ = [3,0]ᵀ:

∇f(**x**₀) = [2(3−1), 2(0+2)]ᵀ = [4, 4]ᵀ.

Update:

**x**₁ = **x**₀ − 0.5[4,4]ᵀ = [3−2, 0−2]ᵀ = [1, −2]ᵀ.

Objective values:

f(**x**₀) = (3−1)² + (0+2)² = 4 + 4 = 8.

f(**x**₁) = (1−1)² + (−2+2)² = 0 + 0 = 0.

hard

Consider f(**x**) = 1/2 **x**ᵀ**A****x** where **A** has eigenvalues {1, 10}.

1) Give a range of α that guarantees convergence for fixed-step gradient descent.

2) Explain (in one or two sentences) why convergence can still feel slow when eigenvalues are very different.

**Hint:** Use the condition 0 < α < 2/λₘₐₓ. For slowness, think about the condition number κ = λₘₐₓ/λₘᵢₙ and zig-zagging.

Show solution

1) λₘₐₓ = 10, so 0 < α < 2/10 = 0.2 guarantees convergence.

2) When eigenvalues differ greatly (κ large), α must be small enough for the steep direction (λ=10), which makes progress along the flat direction (λ=1) comparatively slow; iterates can zig-zag in a narrow valley, reducing efficiency.

## Connections

- •Next: [Stochastic Gradient Descent](/tech-tree/sgd/) — same update idea, but gradients are estimated from mini-batches.
- •Useful foundation for: [Logistic Regression](/tech-tree/logistic-regression/) — training is typically done with GD/SGD on cross-entropy.
- •Deeper theory: [Convex Optimization](/tech-tree/convex-optimization/) — convergence guarantees, smoothness, strong convexity, and line search.
- •Alternative direction strategies: [Conjugate Gradient Methods](/tech-tree/conjugate-gradients/) — particularly efficient on quadratic objectives.
- •Big picture: [Machine Learning Introduction](/tech-tree/ml-intro/) — framing learning as minimizing loss functions.

Quality: A (4.5/5)

[← back to tree](/tech-tree/)[browse all →](/tech-tree/inventory/)
