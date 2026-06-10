---
title: Support Vector Machines
description: Maximum margin classifiers. Kernel trick for nonlinearity.
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
permalink: /tech-tree/svm/
---

[←Back to Tech Tree](/tech-tree/)

[inventory](/tech-tree/inventory/)[coverage](/tech-tree/coverage/)

# Support Vector Machines

Machine LearningDifficulty: ★★★★☆Depth: 9Unlocks: 1

Maximum margin classifiers. Kernel trick for nonlinearity.

## Interactive Visualization

⏮◀◀▶▶STEP0.25x1xZOOM

t=0s

## Core Concepts

- -Maximum-margin separating hyperplane (decision boundary w·x+b=0 with canonical scaling so margin = 1/||w||)
- -Support vectors and sparsity (only training points with active constraints determine the classifier)
- -Kernel trick (use of a positive-definite kernel as an implicit inner product to enable nonlinear separation)

## Key Symbols & Notation

alpha\_i (dual coefficient / Lagrange multiplier for training example i)K(x,x') (positive-definite kernel function = inner product in feature space)

## Essential Relationships

- -Primal-dual and kernelized decision function: w = sum\_i alpha\_i y\_i x\_i, so f(x)=sign(sum\_i alpha\_i y\_i K(x\_i,x)+b); only alpha\_i>0 (support vectors) contribute and margin = 1/||w|| under canonical scaling

## Prerequisites (2)

[Convex Optimization5 atoms](/tech-tree/convex-optimization/)[Lagrange Multipliers5 atoms](/tech-tree/lagrange-multipliers/)

## Unlocks (1)

[Kernel Methodslvl 4](/tech-tree/kernel-methods/)

Advanced Learning Details

### Graph Position

81

Depth Cost

1

Fan-Out (ROI)

1

Bottleneck Score

9

Chain Length

### Cognitive Load

6

Atomic Elements

61

Total Elements

L4

Percentile Level

L4

Atomic Level

### All Concepts (26)

- - Linear separating hyperplane as classifier: decision boundary defined by w·x + b = 0
- - Geometric margin: signed distance from a point to the separating hyperplane
- - Maximum-margin principle: choose hyperplane that maximizes the minimum (geometric) margin
- - Support vectors: training examples that lie on or inside the margin and determine the solution
- - Hard-margin SVM: maximum-margin classifier when data are linearly separable (no errors allowed)
- - Soft-margin SVM: margin maximization allowing classification errors via slack variables
- - Slack variables (ξ\_i): nonnegative variables measuring margin violations for each training point
- - Regularization parameter C: trade-off parameter between margin size and slack (misclassification) penalty
- - Hinge loss: loss function max(0, 1 - y f(x)) that underlies soft-margin SVM
- - Primal SVM optimization problem: objective and constraints in w, b, and ξ (quadratic objective plus linear constraints)
- - Dual SVM optimization problem: quadratic program in dual variables (α\_i) involving only inner products of training points
- - Representation theorem for SVMs: primal weight vector w expressed as a linear combination of training points weighted by α\_i y\_i
- - Kernel function K(x, x'): a function that computes an inner product in some (possibly high- or infinite-dimensional) feature space
- - Kernel trick: replace inner products ⟨φ(x), φ(x')⟩ with K(x,x') to train non-linear SVMs without explicit feature mapping
- - Kernel (Gram) matrix: matrix of pairwise kernel evaluations K\_ij = K(x\_i, x\_j)
- - Positive semi-definiteness / Mercer condition for kernels: condition that a function be a valid inner-product kernel
- - Common kernel families and their qualitative effects (linear, polynomial, Gaussian/RBF, sigmoid)
- - Dual-to-primal link: bias term b and decision function recovered from dual solution (α\_i)
- - Sparsity of dual solution: only support vectors have nonzero α\_i, leading to sparse decision function
- - KKT conditions specialized to SVM: complementary slackness implications relating α\_i, ξ\_i, and classification margin
- - Bounds on dual variables in soft-margin: 0 ≤ α\_i ≤ C and equality constraint sum\_i α\_i y\_i = 0
- - Decision function in kernelized form: f(x) = sign( sum\_i α\_i y\_i K(x\_i, x) + b )
- - Interpretation of C as inverse regularization strength and its effect on margin/generalization
- - Equivalence/relationship between minimizing ||w|| (or ||w||^2) and maximizing margin
- - Influence of kernel choice on implicit feature space dimensionality (e.g., RBF → infinite-dimensional)
- - Computational implications: training scales with number of training examples (quadratic/greater for dense kernels); prediction cost scales with number of support vectors

### Teaching Strategy

Multi-session curriculum - substantial prior knowledge and complex material. Use mastery gates and deliberate practice.

Support Vector Machines (SVMs) are one of the cleanest examples of how geometry, convex optimization, and linear algebra combine into a powerful ML algorithm: pick the separating hyperplane that leaves the *widest* safety buffer (margin) between classes—and if the data isn’t linearly separable, quietly switch to a richer feature space using a kernel, without ever computing those features explicitly.

TL;DR:

An SVM chooses a decision boundary w⋅x+b=0\mathbf{w}\cdot\mathbf{x}+b=0w⋅x+b=0 that maximizes the margin (roughly, the distance to the closest training points). Only the closest points—*support vectors*—determine the solution, producing a sparse model in the dual form. With the kernel trick, inner products ϕ(x)⋅ϕ(x′)\phi(\mathbf{x})\cdot\phi(\mathbf{x}')ϕ(x)⋅ϕ(x′) are replaced by a positive-definite kernel K(x,x′)K(\mathbf{x},\mathbf{x}')K(x,x′), enabling nonlinear decision boundaries while solving a convex optimization problem.

## What Is a Support Vector Machine?

### The problem SVMs are trying to solve (why before how)

In binary classification you often want a rule that separates two classes as reliably as possible. If the data are roughly linearly separable, many hyperplanes can separate them—but some are *fragile*: a tiny perturbation in the data could flip predictions.

SVMs add a strong geometric preference:

- •Don’t just separate the classes.
- •Separate them with the **largest possible margin**.

That “margin” is a built-in robustness buffer. Intuitively, if the boundary is far from the training points, small noise in the inputs is less likely to cross the boundary.

### The decision boundary

A linear classifier uses a hyperplane:

w⋅x+b=0\mathbf{w}\cdot\mathbf{x}+b=0w⋅x+b=0

- •**w** is the normal vector (perpendicular to the boundary)
- •bbb is the offset (bias)
- •prediction is typically y^=sign⁡(w⋅x+b)\hat{y}=\operatorname{sign}(\mathbf{w}\cdot\mathbf{x}+b)y^​=sign(w⋅x+b) with labels y∈{+1,−1}y\in\{+1,-1\}y∈{+1,−1}

### What “margin” means (geometrically)

For a point **x**, its signed distance to the hyperplane is:

dist(x,w,b)=w⋅x+b∥w∥\text{dist}(\mathbf{x}, \mathbf{w}, b)=\frac{\mathbf{w}\cdot\mathbf{x}+b}{\|\mathbf{w}\|}dist(x,w,b)=∥w∥w⋅x+b​

So the distance scales like $1/\|\mathbf{w}\|.Totalkaboutmarginsinaconsistentway,SVMsuse∗∗canonicalscaling∗∗:choosethescaleof∗∗w∗∗and. To talk about margins in a consistent way, SVMs use \*\*canonical scaling\*\*: choose the scale of \*\*w\*\* and .Totalkaboutmarginsinaconsistentway,SVMsuse∗∗canonicalscaling∗∗:choosethescaleof∗∗w∗∗andb$ so that the *closest* points satisfy

yi(w⋅xi+b)=1y\_i(\mathbf{w}\cdot\mathbf{x}\_i+b)=1yi​(w⋅xi​+b)=1

Under that choice:

- •the two “margin” hyperplanes are

w⋅x+b=+1andw⋅x+b=−1\mathbf{w}\cdot\mathbf{x}+b=+1 \quad\text{and}\quad \mathbf{w}\cdot\mathbf{x}+b=-1w⋅x+b=+1andw⋅x+b=−1

- •the distance between them is

2∥w∥\frac{2}{\|\mathbf{w}\|}∥w∥2​

Many texts call the margin 1∥w∥\frac{1}{\|\mathbf{w}\|}∥w∥1​ (distance from boundary to the closest points), while others emphasize the full band width 2∥w∥\frac{2}{\|\mathbf{w}\|}∥w∥2​. Either way, maximizing the margin is equivalent to minimizing ∥w∥\|\mathbf{w}\|∥w∥.

### The “maximum margin” optimization (hard-margin)

If the data are perfectly separable, we want:

- •correct classification with margin constraints:

yi(w⋅xi+b)≥1∀iy\_i(\mathbf{w}\cdot\mathbf{x}\_i+b)\ge 1 \quad \forall iyi​(w⋅xi​+b)≥1∀i

- •maximum margin, i.e. minimize ∥w∥\|\mathbf{w}\|∥w∥.

This gives the classic **hard-margin SVM** primal problem:

min⁡w,b  12∥w∥2s.t.yi(w⋅xi+b)≥1  ∀i\min\_{\mathbf{w},b}\; \frac{1}{2}\|\mathbf{w}\|^2 \quad \text{s.t.}\quad y\_i(\mathbf{w}\cdot\mathbf{x}\_i+b)\ge 1\;\forall iw,bmin​21​∥w∥2s.t.yi​(w⋅xi​+b)≥1∀i

Why 12∥w∥2\frac{1}{2}\|\mathbf{w}\|^221​∥w∥2? It’s convex and differentiable, and the factor $1/2$ cancels nicely in derivatives.

### Visualization focus: margin vs decision boundary

**Interactive canvas idea (1):** show a 2D dataset with two classes. Provide sliders to rotate/translate a candidate hyperplane and display:

- •the decision boundary w⋅x+b=0\mathbf{w}\cdot\mathbf{x}+b=0w⋅x+b=0
- •the two margin lines w⋅x+b=±1\mathbf{w}\cdot\mathbf{x}+b=\pm 1w⋅x+b=±1
- •the current margin width $2/\|\mathbf{w}\|$

Let the user move the boundary and watch the margin shrink/grow, with a live readout of ∥w∥\|\mathbf{w}\|∥w∥.

**Static diagram (for non-canvas readers):**

```
<svg xmlns="http://www.w3.org/2000/svg" width="720" height="260" viewBox="0 0 720 260" role="img" aria-label="SVM margin: decision boundary and two margin lines with support vectors">
  <rect x="0" y="0" width="720" height="260" fill="#ffffff"/>
  <!-- axes -->
  <line x1="60" y1="220" x2="680" y2="220" stroke="#333" stroke-width="2"/>
  <line x1="60" y1="220" x2="60" y2="30" stroke="#333" stroke-width="2"/>
  <!-- decision boundary and margins -->
  <line x1="170" y1="220" x2="510" y2="30" stroke="#1f77b4" stroke-width="3"/>
  <line x1="140" y1="220" x2="480" y2="30" stroke="#1f77b4" stroke-width="2" stroke-dasharray="8,6"/>
  <line x1="200" y1="220" x2="540" y2="30" stroke="#1f77b4" stroke-width="2" stroke-dasharray="8,6"/>
  <text x="520" y="60" font-family="sans-serif" font-size="14" fill="#1f77b4">w·x+b=0</text>
  <text x="545" y="80" font-family="sans-serif" font-size="12" fill="#1f77b4">w·x+b=+1</text>
  <text x="455" y="90" font-family="sans-serif" font-size="12" fill="#1f77b4">w·x+b=-1</text>
  <!-- points (class +1) -->
  <circle cx="520" cy="70" r="7" fill="#2ca02c"/>
  <circle cx="600" cy="110" r="7" fill="#2ca02c"/>
  <circle cx="610" cy="60" r="7" fill="#2ca02c"/>
  <!-- points (class -1) -->
  <circle cx="150" cy="185" r="7" fill="#d62728"/>
  <circle cx="210" cy="170" r="7" fill="#d62728"/>
  <circle cx="250" cy="205" r="7" fill="#d62728"/>
  <!-- support vectors (highlighted) -->
  <circle cx="520" cy="70" r="12" fill="none" stroke="#000" stroke-width="2"/>
  <circle cx="210" cy="170" r="12" fill="none" stroke="#000" stroke-width="2"/>
  <text x="90" y="45" font-family="sans-serif" font-size="14" fill="#000">Support vectors lie on the dashed margin lines</text>
</svg>
```

This diagram emphasizes a key idea you’ll return to: the boundary is “pinned” by the closest points.

## Core Mechanic 1: Maximum-Margin Optimization and the Soft Margin

### Why the hard-margin version is not enough

Perfect separability is rare. Noise, overlap, and mislabeled points are common.

If you insist on yi(w⋅xi+b)≥1y\_i(\mathbf{w}\cdot\mathbf{x}\_i+b)\ge 1yi​(w⋅xi​+b)≥1 for *every* point, you may get:

- •infeasibility (no solution)
- •or an overly complex boundary in feature space (when kernels are used)

SVMs handle this with **slack variables** ξi≥0\xi\_i\ge 0ξi​≥0 that allow violations:

yi(w⋅xi+b)≥1−ξiy\_i(\mathbf{w}\cdot\mathbf{x}\_i+b)\ge 1-\xi\_iyi​(w⋅xi​+b)≥1−ξi​

Interpretation:

- •ξi=0\xi\_i=0ξi​=0: point is correctly classified and outside/on the margin.
- •$0<\xi\_i<1$: correctly classified but inside the margin.
- •ξi≥1\xi\_i\ge 1ξi​≥1: misclassified.

### The soft-margin primal objective

We now trade off large margin vs. violations:

min⁡w,b,ξ  12∥w∥2+C∑i=1nξis.t.yi(w⋅xi+b)≥1−ξi,  ξi≥0\min\_{\mathbf{w},b,\boldsymbol{\xi}}\; \frac{1}{2}\|\mathbf{w}\|^2 + C\sum\_{i=1}^n \xi\_i \quad\text{s.t.}\quad y\_i(\mathbf{w}\cdot\mathbf{x}\_i+b)\ge 1-\xi\_i,\;\xi\_i\ge 0w,b,ξmin​21​∥w∥2+Ci=1∑n​ξi​s.t.yi​(w⋅xi​+b)≥1−ξi​,ξi​≥0

C>0C>0C>0 controls the trade-off:

- •large CCC: violations are expensive → narrower margin, fewer training errors
- •small CCC: violations are tolerated → wider margin, possibly more training errors

A helpful way to remember this:

- •12∥w∥2\frac{1}{2}\|\mathbf{w}\|^221​∥w∥2 is a *capacity/complexity* penalty
- •∑ξi\sum \xi\_i∑ξi​ is a *training loss* (linear penalty on margin violations)

### Connecting to hinge loss

You can rewrite the constrained soft-margin problem into an unconstrained form using the hinge loss

ℓhinge(y,f)=max⁡(0,1−yf)\ell\_{\text{hinge}}(y, f)=\max(0, 1-y f)ℓhinge​(y,f)=max(0,1−yf)

where f(x)=w⋅x+bf(\mathbf{x})=\mathbf{w}\cdot\mathbf{x}+bf(x)=w⋅x+b.

At optimum, ξi\xi\_iξi​ becomes exactly the hinge loss:

ξi=max⁡(0,1−yi(w⋅xi+b))\xi\_i = \max\big(0, 1-y\_i(\mathbf{w}\cdot\mathbf{x}\_i+b)\big)ξi​=max(0,1−yi​(w⋅xi​+b))

So the primal is equivalent to:

min⁡w,b  12∥w∥2+C∑i=1nmax⁡(0,1−yi(w⋅xi+b))\min\_{\mathbf{w},b}\; \frac{1}{2}\|\mathbf{w}\|^2 + C\sum\_{i=1}^n \max\big(0, 1-y\_i(\mathbf{w}\cdot\mathbf{x}\_i+b)\big)w,bmin​21​∥w∥2+Ci=1∑n​max(0,1−yi​(w⋅xi​+b))

This is a useful lens because it makes SVMs feel like “regularized empirical risk minimization,” just with hinge loss instead of logistic loss.

### Visualization focus: how C changes the solution

**Interactive canvas idea:** a slider for CCC that recomputes the separating line (in 2D linear case) and updates:

- •margin width $2/\|\mathbf{w}\|$
- •number of margin violations
- •which points are support vectors

Learners should see that increasing CCC often pulls the boundary toward outliers to fix them, shrinking the margin.

### A careful note about scaling

Because SVMs depend on inner products and distances, feature scaling matters.

If one feature has values in thousands and another in tenths, the large-scale feature dominates w⋅x\mathbf{w}\cdot\mathbf{x}w⋅x and ∥w∥\|\mathbf{w}\|∥w∥. Standard practice:

- •standardize features (zero mean, unit variance) or similar normalization
- •tune CCC (and kernel params) after scaling

### Where convex optimization shows up

Both hard- and soft-margin SVMs are **convex** problems:

- •quadratic objective in **w**
- •linear constraints in (**w**, bbb, ξ\xiξ)

That convexity is why SVMs historically earned a reputation for reliability: there is a single global optimum (up to degeneracies).

But the most elegant part is what happens when we transform the problem into its **dual**: it will reveal support vectors and the kernel trick naturally.

## Core Mechanic 2: Support Vectors, the Dual Problem, and Sparsity

### Why we go to the dual

You already know Lagrange multipliers for equality constraints. For SVMs we have inequality constraints, so we use the Karush–Kuhn–Tucker (KKT) framework.

The payoff for deriving the dual is big:

1. 1)The classifier can be written entirely in terms of dot products xi⋅xj\mathbf{x}\_i\cdot\mathbf{x}\_jxi​⋅xj​.
2. 2)The solution becomes **sparse**: only some points have nonzero coefficients.
3. 3)That dot-product-only form is exactly what kernels replace.

We’ll derive the soft-margin dual (hard-margin is a special case).

### Step 1: Set up constraints and multipliers

Primal (soft-margin) again:

min⁡w,b,ξ  12∥w∥2+C∑iξi\min\_{\mathbf{w},b,\boldsymbol{\xi}}\; \frac{1}{2}\|\mathbf{w}\|^2 + C\sum\_i \xi\_iw,b,ξmin​21​∥w∥2+Ci∑​ξi​

subject to

yi(w⋅xi+b)≥1−ξi,ξi≥0y\_i(\mathbf{w}\cdot\mathbf{x}\_i+b)\ge 1-\xi\_i, \quad \xi\_i\ge 0yi​(w⋅xi​+b)≥1−ξi​,ξi​≥0

Introduce Lagrange multipliers:

- •αi≥0\alpha\_i\ge 0αi​≥0 for the margin constraints
- •μi≥0\mu\_i\ge 0μi​≥0 for the slack nonnegativity constraints ξi≥0\xi\_i\ge 0ξi​≥0

The Lagrangian is:

L(w,b,ξ,α,μ)=12∥w∥2+C∑iξi−∑iαi(yi(w⋅xi+b)−1+ξi)−∑iμiξi\mathcal{L}(\mathbf{w},b,\boldsymbol{\xi},\boldsymbol{\alpha},\boldsymbol{\mu})
= \frac{1}{2}\|\mathbf{w}\|^2 + C\sum\_i \xi\_i
- \sum\_i \alpha\_i\big(y\_i(\mathbf{w}\cdot\mathbf{x}\_i+b)-1+\xi\_i\big)
- \sum\_i \mu\_i\xi\_iL(w,b,ξ,α,μ)=21​∥w∥2+Ci∑​ξi​−i∑​αi​(yi​(w⋅xi​+b)−1+ξi​)−i∑​μi​ξi​

### Step 2: Stationarity conditions (minimize over primal variables)

Take partial derivatives and set to zero.

**With respect to** **w**:

∂L∂w=w−∑iαiyixi=0  ⇒  w=∑iαiyixi\frac{\partial \mathcal{L}}{\partial \mathbf{w}} = \mathbf{w} - \sum\_i \alpha\_i y\_i \mathbf{x}\_i = 0
\;\Rightarrow\; \mathbf{w} = \sum\_i \alpha\_i y\_i \mathbf{x}\_i∂w∂L​=w−i∑​αi​yi​xi​=0⇒w=i∑​αi​yi​xi​

This is the first major result: **w** is a linear combination of training points.

**With respect to** bbb:

∂L∂b=−∑iαiyi=0  ⇒  ∑iαiyi=0\frac{\partial \mathcal{L}}{\partial b} = -\sum\_i \alpha\_i y\_i = 0
\;\Rightarrow\; \sum\_i \alpha\_i y\_i = 0∂b∂L​=−i∑​αi​yi​=0⇒i∑​αi​yi​=0

**With respect to** ξi\xi\_iξi​:

∂L∂ξi=C−αi−μi=0  ⇒  αi+μi=C\frac{\partial \mathcal{L}}{\partial \xi\_i} = C - \alpha\_i - \mu\_i = 0
\;\Rightarrow\; \alpha\_i + \mu\_i = C∂ξi​∂L​=C−αi​−μi​=0⇒αi​+μi​=C

Since μi≥0\mu\_i\ge 0μi​≥0, we get the box constraint:

0≤αi≤C0 \le \alpha\_i \le C0≤αi​≤C

### Step 3: Plug back in → the dual objective

Substitute w=∑iαiyixi\mathbf{w}=\sum\_i \alpha\_i y\_i \mathbf{x}\_iw=∑i​αi​yi​xi​ into the Lagrangian and eliminate ξ\boldsymbol{\xi}ξ using stationarity. After simplification, the dual becomes:

max⁡α  ∑i=1nαi−12∑i=1n∑j=1nαiαjyiyj(xi⋅xj)\max\_{\boldsymbol{\alpha}}\; \sum\_{i=1}^n \alpha\_i - \frac{1}{2}\sum\_{i=1}^n\sum\_{j=1}^n \alpha\_i\alpha\_j y\_i y\_j (\mathbf{x}\_i\cdot\mathbf{x}\_j)αmax​i=1∑n​αi​−21​i=1∑n​j=1∑n​αi​αj​yi​yj​(xi​⋅xj​)

subject to

0≤αi≤C,∑iαiyi=00\le \alpha\_i\le C, \quad \sum\_i \alpha\_i y\_i=00≤αi​≤C,i∑​αi​yi​=0

This is a convex quadratic program in α\boldsymbol{\alpha}α (maximize a concave quadratic).

### Step 4: The classifier in terms of α

Once you solve for αi\alpha\_iαi​, the decision function is:

f(x)=w⋅x+b=(∑iαiyixi)⋅x+b=∑iαiyi(xi⋅x)+bf(\mathbf{x})=\mathbf{w}\cdot\mathbf{x}+b
=\Big(\sum\_i \alpha\_i y\_i \mathbf{x}\_i\Big)\cdot\mathbf{x}+b
=\sum\_i \alpha\_i y\_i (\mathbf{x}\_i\cdot\mathbf{x}) + bf(x)=w⋅x+b=(i∑​αi​yi​xi​)⋅x+b=i∑​αi​yi​(xi​⋅x)+b

Only points with αi≠0\alpha\_i\ne 0αi​=0 contribute. These are the **support vectors**.

### What exactly are “support vectors”?

From KKT complementary slackness:

αi(yi(w⋅xi+b)−1+ξi)=0\alpha\_i\big(y\_i(\mathbf{w}\cdot\mathbf{x}\_i+b)-1+\xi\_i\big)=0αi​(yi​(w⋅xi​+b)−1+ξi​)=0

So:

- •If a point is comfortably outside the margin: yi(w⋅xi+b)>1y\_i(\mathbf{w}\cdot\mathbf{x}\_i+b)>1yi​(w⋅xi​+b)>1 and ξi=0\xi\_i=0ξi​=0 → typically αi=0\alpha\_i=0αi​=0.
- •If a point lies exactly on the margin: yi(w⋅xi+b)=1y\_i(\mathbf{w}\cdot\mathbf{x}\_i+b)=1yi​(w⋅xi​+b)=1 and ξi=0\xi\_i=0ξi​=0 → $0<\alpha\_i<C$.
- •If a point violates the margin: yi(w⋅xi+b)<1y\_i(\mathbf{w}\cdot\mathbf{x}\_i+b)<1yi​(w⋅xi​+b)<1 → usually αi=C\alpha\_i=Cαi​=C (at the upper bound) when it’s a “hard” violator.

This yields a practical taxonomy:

| Point location | Condition | Typical α | Role |
| --- | --- | --- | --- |
| Outside margin | yf(x)>1y f(\mathbf{x})>1yf(x)>1 | 0 | irrelevant to boundary |
| On margin | yf(x)=1y f(\mathbf{x})=1yf(x)=1 | (0, C) | “geometric” support vector |
| Inside margin / misclassified | yf(x)<1y f(\mathbf{x})<1yf(x)<1 | C | “error” support vector |

### Visualization focus: support vectors control the boundary

**Interactive canvas idea (2):** show a solved linear SVM in 2D with support vectors highlighted. Allow the user to:

1. 1)drag any *non-support* point a moderate amount
2. 2)drag a support vector a moderate amount

and recompute the SVM.

Expected visual lesson:

- •moving non-support points often **does not change** the boundary (or changes it very little)
- •moving a support vector **noticeably moves/rotates** the boundary

To make this explicit, display:

- •list/count of support vectors
- •α values next to points (e.g., tiny labels)
- •“boundary change” metric (angle shift, bias shift)

This turns “only support vectors matter” from a slogan into an observed fact.

### How do we find b?

Once you have α\alphaα, you can compute bbb using any support vector with $0<\alpha\_i<C(i.e.,on−margin,notattheboxconstraint).Forsuchapoint, (i.e., on-margin, not at the box constraint). For such a point, (i.e.,on−margin,notattheboxconstraint).Forsuchapoint,\xi\_i=0$ and

yi(w⋅xi+b)=1y\_i(\mathbf{w}\cdot\mathbf{x}\_i+b)=1yi​(w⋅xi​+b)=1

So

b=yi−w⋅xib = y\_i - \mathbf{w}\cdot\mathbf{x}\_ib=yi​−w⋅xi​

In practice you average bbb over all margin support vectors to reduce numerical noise.

### Sparsity and prediction cost

Prediction evaluates

f(x)=∑i∈SVαiyi(xi⋅x)+bf(\mathbf{x})=\sum\_{i\in SV} \alpha\_i y\_i (\mathbf{x}\_i\cdot\mathbf{x}) + bf(x)=i∈SV∑​αi​yi​(xi​⋅x)+b

If the number of support vectors is small, this is fast. This sparsity is a real advantage over methods that require all points at prediction time.

But note the caveat: with some kernels and some CCC choices, the number of support vectors can become large (even close to nnn), making prediction slower.

## Application/Connection: The Kernel Trick (Nonlinear SVMs)

### Why kernels

A linear separator in the original input space might be impossible even if the data are “simple” in a different representation.

Classic example: concentric circles. No line separates inner vs outer ring.

Idea: map inputs through a feature map ϕ(x)\phi(\mathbf{x})ϕ(x) so that classes become linearly separable in feature space:

f(x)=w⋅ϕ(x)+bf(\mathbf{x}) = \mathbf{w}\cdot\phi(\mathbf{x}) + bf(x)=w⋅ϕ(x)+b

But explicitly constructing ϕ(x)\phi(\mathbf{x})ϕ(x) could be expensive or infinite-dimensional.

### The key observation

In the dual, data only appear inside dot products:

xi⋅xj\mathbf{x}\_i\cdot\mathbf{x}\_jxi​⋅xj​

If we instead operate in feature space, we would need:

ϕ(xi)⋅ϕ(xj)\phi(\mathbf{x}\_i)\cdot\phi(\mathbf{x}\_j)ϕ(xi​)⋅ϕ(xj​)

A **kernel** is a function

K(x,x′)=ϕ(x)⋅ϕ(x′)K(\mathbf{x},\mathbf{x}') = \phi(\mathbf{x})\cdot\phi(\mathbf{x}')K(x,x′)=ϕ(x)⋅ϕ(x′)

for some (possibly implicit) feature map ϕ\phiϕ, provided KKK is positive-definite (Mercer condition).

Then the dual becomes:

max⁡α  ∑iαi−12∑i∑jαiαjyiyjK(xi,xj)\max\_{\boldsymbol{\alpha}}\; \sum\_i \alpha\_i - \frac{1}{2}\sum\_i\sum\_j \alpha\_i\alpha\_j y\_i y\_j K(\mathbf{x}\_i,\mathbf{x}\_j)αmax​i∑​αi​−21​i∑​j∑​αi​αj​yi​yj​K(xi​,xj​)

and prediction becomes:

f(x)=∑i∈SVαiyiK(xi,x)+bf(\mathbf{x})=\sum\_{i\in SV} \alpha\_i y\_i K(\mathbf{x}\_i,\mathbf{x}) + bf(x)=i∈SV∑​αi​yi​K(xi​,x)+b

That’s the **kernel trick**: you get nonlinear decision boundaries in input space while solving a convex problem that only needs kernel evaluations.

### Common kernels and what they “feel like”

| Kernel | Formula | Main parameter(s) | What it implies |
| --- | --- | --- | --- |
| Linear | K(x,x′)=x⋅x′K(\mathbf{x},\mathbf{x}')=\mathbf{x}\cdot\mathbf{x}'K(x,x′)=x⋅x′ | none | linear boundary in input space |
| Polynomial | K=(γ x⋅x′+r)dK=(\gamma\,\mathbf{x}\cdot\mathbf{x}'+r)^dK=(γx⋅x′+r)d | d,γ,rd,\gamma,rd,γ,r | interactions up to degree ddd |
| RBF / Gaussian | $K=\exp(-\gamma\ | \mathbf{x}-\mathbf{x}'\ | ^2)$ | γ\gammaγ | local similarity; flexible smooth boundaries |
| Sigmoid (less common) | K=tanh⁡(γ x⋅x′+r)K=\tanh(\gamma\,\mathbf{x}\cdot\mathbf{x}'+r)K=tanh(γx⋅x′+r) | γ,r\gamma,rγ,r | related to neural nets; not always PD |

A practical intuition for RBF:

- •small γ\gammaγ → wide Gaussian → smoother, more global influence → simpler boundary
- •large γ\gammaγ → narrow Gaussian → very local influence → potentially wiggly boundary

And remember: CCC and kernel parameters interact. High CCC + high γ\gammaγ can easily overfit.

### Visualization focus: concentric circles and feature space linearity

**Interactive canvas idea (3):** present a concentric-circles dataset.

Panel A (input space): show points and the learned nonlinear boundary for an RBF SVM.

Panel B (a chosen feature space view): show an illustrative mapping where the same points become linearly separable.

For circles, an instructive explicit mapping is to use a radial feature like r2=x12+x22r^2=x\_1^2+x\_2^2r2=x12​+x22​. In a 1D feature space of r2r^2r2, the classes may separate by a threshold (a “linear” separator in that 1D feature). More generally, you can visualize a 3D feature map:

ϕ(x1,x2)=(x1,x2,x12+x22)\phi(x\_1,x\_2) = (x\_1, x\_2, x\_1^2+x\_2^2)ϕ(x1​,x2​)=(x1​,x2​,x12​+x22​)

Then a plane in this 3D space can correspond to a circle-like boundary when projected back to 2D.

Important honesty: the RBF kernel’s actual feature space is infinite-dimensional, so Panel B is an *illustration* of the concept, not literally the RBF feature map.

**Static diagram (for non-canvas readers):**

```
<svg xmlns="http://www.w3.org/2000/svg" width="720" height="300" viewBox="0 0 720 300" role="img" aria-label="Kernel idea: circles not separable in 2D become separable after mapping using radius-squared feature">
  <rect x="0" y="0" width="720" height="300" fill="#fff"/>
  <text x="60" y="30" font-family="sans-serif" font-size="16" fill="#000">Input space (x₁,x₂): concentric circles</text>
  <text x="420" y="30" font-family="sans-serif" font-size="16" fill="#000">Feature (r²): linear threshold</text>
  <!-- left axes -->
  <line x1="60" y1="250" x2="330" y2="250" stroke="#333" stroke-width="2"/>
  <line x1="60" y1="250" x2="60" y2="60" stroke="#333" stroke-width="2"/>
  <!-- circles of points -->
  <circle cx="195" cy="155" r="35" fill="none" stroke="#d62728" stroke-width="2"/>
  <circle cx="195" cy="155" r="80" fill="none" stroke="#2ca02c" stroke-width="2"/>
  <!-- sample points -->
  <circle cx="195" cy="120" r="5" fill="#d62728"/>
  <circle cx="230" cy="155" r="5" fill="#d62728"/>
  <circle cx="195" cy="190" r="5" fill="#d62728"/>
  <circle cx="165" cy="155" r="5" fill="#d62728"/>
  <circle cx="195" cy="75" r="5" fill="#2ca02c"/>
  <circle cx="275" cy="155" r="5" fill="#2ca02c"/>
  <circle cx="195" cy="235" r="5" fill="#2ca02c"/>
  <circle cx="115" cy="155" r="5" fill="#2ca02c"/>
  <!-- right axes for r^2 -->
  <line x1="420" y1="250" x2="690" y2="250" stroke="#333" stroke-width="2"/>
  <line x1="420" y1="250" x2="420" y2="60" stroke="#333" stroke-width="2"/>
  <text x="560" y="275" font-family="sans-serif" font-size="12">r²</text>
  <!-- threshold -->
  <line x1="560" y1="250" x2="560" y2="60" stroke="#1f77b4" stroke-width="2" stroke-dasharray="6,5"/>
  <text x="565" y="80" font-family="sans-serif" font-size="12" fill="#1f77b4">threshold</text>
  <!-- points on line (r^2) -->
  <circle cx="500" cy="170" r="6" fill="#d62728"/>
  <circle cx="510" cy="140" r="6" fill="#d62728"/>
  <circle cx="520" cy="200" r="6" fill="#d62728"/>
  <circle cx="620" cy="120" r="6" fill="#2ca02c"/>
  <circle cx="640" cy="180" r="6" fill="#2ca02c"/>
  <circle cx="650" cy="150" r="6" fill="#2ca02c"/>
  <text x="430" y="55" font-family="sans-serif" font-size="12" fill="#000">(conceptual) mapping: (x₁,x₂) → r²=x₁²+x₂²</text>
</svg>
```

### Model selection: tuning C and kernel parameters

In practice, an SVM’s performance depends heavily on hyperparameters:

- •CCC (regularization vs margin violations)
- •kernel parameters (e.g., γ\gammaγ for RBF, degree ddd for polynomial)

A typical approach:

- •standardize features
- •perform cross-validation over a grid (often log-spaced)
- •choose parameters that optimize validation performance

### Practical pros/cons (when to use SVMs)

**Strengths**

- •Convex optimization → no bad local minima
- •Effective in moderate dimensions
- •Kernel trick enables flexible nonlinear boundaries
- •Often strong performance on small-to-medium datasets

**Limitations**

- •Training can be expensive for very large nnn (kernel matrix is n×nn\times nn×n)
- •Prediction can be expensive if many support vectors
- •Less natural probabilistic outputs (though you can calibrate)
- •Kernel and hyperparameter choices matter a lot

### Bridge to what you’ll unlock next

Everything about “kernel methods” generalizes beyond SVMs: ridge regression, PCA variants, Gaussian processes, etc. The SVM is your first major encounter with the idea that *inner products are the computational interface* to a possibly huge feature space.

You’re now ready for: [Kernel Methods](/tech-tree/kernel-methods/).

## Worked Examples (3)

### Example 1: Compute the margin from a given hyperplane (and see why scaling matters)

Suppose a linear classifier is given by w=(3,4)\mathbf{w}=(3,4)w=(3,4) and b=−10b=-10b=−10. Consider the point x=(2,2)\mathbf{x}=(2,2)x=(2,2). (1) Compute its signed distance to the decision boundary. (2) Compute the geometric margin band width $2/\|\mathbf{w}\|$. (3) Explain why you can’t read off the SVM margin unless the classifier is in canonical scaling.

1. Compute the norm of **w**:

   \n∥w∥=32+42=9+16=5\|\mathbf{w}\|=\sqrt{3^2+4^2}=\sqrt{9+16}=5∥w∥=32+42​=9+16​=5.
2. Compute the signed value of the decision function:

   \nw⋅x+b=(3,4)⋅(2,2)−10=(6+8)−10=4\mathbf{w}\cdot\mathbf{x}+b = (3,4)\cdot(2,2) -10 = (6+8)-10 = 4w⋅x+b=(3,4)⋅(2,2)−10=(6+8)−10=4.
3. Convert to signed distance:

   \n$dist(x,w,b)=w⋅x+b∥w∥=45=0.8\text{dist}(\mathbf{x},\mathbf{w},b)=\frac{\mathbf{w}\cdot\mathbf{x}+b}{\|\mathbf{w}\|}=\frac{4}{5}=0.8dist(x,w,b)=∥w∥w⋅x+b​=54​=0.8$

   \nSo the point lies on the positive side of the hyperplane, 0.8 units away (in Euclidean distance).
4. Compute the margin band width (distance between w⋅x+b=+1\mathbf{w}\cdot\mathbf{x}+b=+1w⋅x+b=+1 and =−1=-1=−1):

   \n$2∥w∥=25=0.4\frac{2}{\|\mathbf{w}\|} = \frac{2}{5}=0.4∥w∥2​=52​=0.4$
5. Explain scaling:

   \nIf we scale (w,b)(\mathbf{w},b)(w,b) by any constant k>0k>0k>0, the decision boundary w⋅x+b=0\mathbf{w}\cdot\mathbf{x}+b=0w⋅x+b=0 is unchanged because

   \nkw⋅x+kb=0k\mathbf{w}\cdot\mathbf{x}+kb=0kw⋅x+kb=0 is equivalent.

   \nBut ∥kw∥=k∥w∥\|k\mathbf{w}\|=k\|\mathbf{w}\|∥kw∥=k∥w∥, so $2/\|\mathbf{w}\|$ would change even though the boundary is the same.

   \nSVM’s canonical scaling fixes this ambiguity by enforcing that the closest points satisfy yi(w⋅xi+b)=1y\_i(\mathbf{w}\cdot\mathbf{x}\_i+b)=1yi​(w⋅xi​+b)=1, making the margin a well-defined geometric quantity.

**Insight:** The “margin” isn’t just about the boundary line; it’s about the boundary *plus a chosen scale*. SVM selects the scale by pinning the closest points to functional value ±1, turning $1/\|\mathbf{w}\|$ into a true geometric distance.

### Example 2: From dual coefficients to a classifier (support vectors only)

You trained a (linear) soft-margin SVM and obtained nonzero dual coefficients for only two training points:

- •x1=(1,0)\mathbf{x}\_1=(1,0)x1​=(1,0) with y1=+1y\_1=+1y1​=+1, α1=0.5\alpha\_1=0.5α1​=0.5
- •x2=(0,1)\mathbf{x}\_2=(0,1)x2​=(0,1) with y2=−1y\_2=-1y2​=−1, α2=0.5\alpha\_2=0.5α2​=0.5

Assume b=0b=0b=0. (1) Compute **w**. (2) Write the decision function f(x)f(\mathbf{x})f(x). (3) Classify x=(2,1)\mathbf{x}=(2,1)x=(2,1).

1. Compute **w** using w=∑iαiyixi\mathbf{w}=\sum\_i \alpha\_i y\_i \mathbf{x}\_iw=∑i​αi​yi​xi​:

   \nw=0.5⋅(+1)⋅(1,0)+0.5⋅(−1)⋅(0,1)\mathbf{w}=0.5\cdot(+1)\cdot(1,0) + 0.5\cdot(-1)\cdot(0,1)w=0.5⋅(+1)⋅(1,0)+0.5⋅(−1)⋅(0,1)

   \nw=(0.5,0)+(0,−0.5)=(0.5,−0.5)\mathbf{w}=(0.5,0) + (0,-0.5) = (0.5,-0.5)w=(0.5,0)+(0,−0.5)=(0.5,−0.5).
2. Write the decision function:

   \nf(x)=w⋅x+b=(0.5,−0.5)⋅(x1,x2)f(\mathbf{x})=\mathbf{w}\cdot\mathbf{x}+b = (0.5,-0.5)\cdot(x\_1,x\_2)f(x)=w⋅x+b=(0.5,−0.5)⋅(x1​,x2​)

   \nSo

   \n$f(x)=0.5x1−0.5x2f(\mathbf{x})=0.5x\_1 - 0.5x\_2f(x)=0.5x1​−0.5x2​$
3. Evaluate at x=(2,1)\mathbf{x}=(2,1)x=(2,1):

   \nf(2,1)=0.5⋅2−0.5⋅1=1−0.5=0.5f(2,1)=0.5\cdot 2 - 0.5\cdot 1 = 1 - 0.5 = 0.5f(2,1)=0.5⋅2−0.5⋅1=1−0.5=0.5.
4. Classify using sign:

   \ny^=sign⁡(0.5)=+1\hat{y}=\operatorname{sign}(0.5)=+1y^​=sign(0.5)=+1.

**Insight:** Even if you had 10,000 training points, if only two have nonzero α, prediction depends only on those two points. That’s the operational meaning of “support vectors determine the classifier.”

### Example 3: Kernelized prediction with an RBF kernel (showing the mechanics)

You have a kernel SVM with two support vectors:

- •x1=(0,0)\mathbf{x}\_1=(0,0)x1​=(0,0) with y1=+1y\_1=+1y1​=+1, α1=0.8\alpha\_1=0.8α1​=0.8
- •x2=(1,0)\mathbf{x}\_2=(1,0)x2​=(1,0) with y2=−1y\_2=-1y2​=−1, α2=0.6\alpha\_2=0.6α2​=0.6

Bias b=0.1b=0.1b=0.1. Use an RBF kernel K(x,x′)=exp⁡(−γ∥x−x′∥2)K(\mathbf{x},\mathbf{x}')=\exp(-\gamma\|\mathbf{x}-\mathbf{x}'\|^2)K(x,x′)=exp(−γ∥x−x′∥2) with γ=1\gamma=1γ=1.

Compute f(x)f(\mathbf{x})f(x) and the predicted label for x=(0.5,0)\mathbf{x}=(0.5,0)x=(0.5,0).

1. Write the kernel decision function:

   \n$f(x)=∑i∈SVαiyiK(xi,x)+bf(\mathbf{x})=\sum\_{i\in SV} \alpha\_i y\_i K(\mathbf{x}\_i,\mathbf{x}) + bf(x)=∑i∈SV​αi​yi​K(xi​,x)+b$
2. Compute K(x1,x)K(\mathbf{x}\_1,\mathbf{x})K(x1​,x):

   \n∥x1−x∥2=∥(0,0)−(0.5,0)∥2=0.52+02=0.25\|\mathbf{x}\_1-\mathbf{x}\|^2 = \|(0,0)-(0.5,0)\|^2 = 0.5^2+0^2=0.25∥x1​−x∥2=∥(0,0)−(0.5,0)∥2=0.52+02=0.25

   \nSo

   \nK(x1,x)=exp⁡(−1⋅0.25)=e−0.25K(\mathbf{x}\_1,\mathbf{x})=\exp(-1\cdot 0.25)=e^{-0.25}K(x1​,x)=exp(−1⋅0.25)=e−0.25.
3. Compute K(x2,x)K(\mathbf{x}\_2,\mathbf{x})K(x2​,x):

   \n∥x2−x∥2=∥(1,0)−(0.5,0)∥2=0.52=0.25\|\mathbf{x}\_2-\mathbf{x}\|^2 = \|(1,0)-(0.5,0)\|^2 = 0.5^2=0.25∥x2​−x∥2=∥(1,0)−(0.5,0)∥2=0.52=0.25

   \nSo

   \nK(x2,x)=e−0.25K(\mathbf{x}\_2,\mathbf{x})=e^{-0.25}K(x2​,x)=e−0.25 as well.
4. Assemble the score:

   \nf(x)=0.8⋅(+1)⋅e−0.25+0.6⋅(−1)⋅e−0.25+0.1f(\mathbf{x})=0.8\cdot(+1)\cdot e^{-0.25} + 0.6\cdot(-1)\cdot e^{-0.25} + 0.1f(x)=0.8⋅(+1)⋅e−0.25+0.6⋅(−1)⋅e−0.25+0.1

   \n=(0.8−0.6)e−0.25+0.1=(0.8-0.6)e^{-0.25}+0.1=(0.8−0.6)e−0.25+0.1

   \n=0.2e−0.25+0.1=0.2e^{-0.25}+0.1=0.2e−0.25+0.1.
5. Numerical approximation: e−0.25≈0.7788e^{-0.25}\approx 0.7788e−0.25≈0.7788.

   \nSo f(x)≈0.2⋅0.7788+0.1=0.1558+0.1=0.2558f(\mathbf{x})\approx 0.2\cdot 0.7788 + 0.1 = 0.1558 + 0.1 = 0.2558f(x)≈0.2⋅0.7788+0.1=0.1558+0.1=0.2558.
6. Predict label:

   \ny^=sign⁡(0.2558)=+1\hat{y}=\operatorname{sign}(0.2558)=+1y^​=sign(0.2558)=+1.

**Insight:** Kernel SVM prediction looks like a weighted vote of similarities to support vectors. With RBF, each support vector contributes most to nearby points and fades with distance.

## Key Takeaways

- ✓

  SVMs choose the separating hyperplane that maximizes the margin; under canonical scaling, margin is proportional to $1/\|\mathbf{w}\|$ (band width $2/\|\mathbf{w}\|$).
- ✓

  Hard-margin SVM requires perfect separability; soft-margin SVM introduces slack variables ξi\xi\_iξi​ and trade-off parameter CCC.
- ✓

  The soft-margin objective corresponds to minimizing 12∥w∥2+C∑imax⁡(0,1−yif(xi))\frac{1}{2}\|\mathbf{w}\|^2 + C\sum\_i \max(0, 1-y\_if(\mathbf{x}\_i))21​∥w∥2+C∑i​max(0,1−yi​f(xi​)) (hinge loss + L2 regularization).
- ✓

  In the dual, the solution is expressed by coefficients αi\alpha\_iαi​ with constraints $0\le \alpha\_i\le Cand and and\sum\_i \alpha\_i y\_i=0$.
- ✓

  Only points with αi>0\alpha\_i>0αi​>0 matter at prediction time; these are the support vectors, which “pin” the optimal boundary.
- ✓

  The kernel trick replaces dot products with a positive-definite kernel K(x,x′)K(\mathbf{x},\mathbf{x}')K(x,x′), enabling nonlinear decision boundaries while keeping convex optimization.
- ✓

  Hyperparameters (CCC, kernel parameters like RBF γ\gammaγ) strongly affect bias/variance and the number of support vectors; scaling features is essential.
- ✓

  SVMs are powerful for small-to-medium datasets and can be very robust, but kernel SVMs can be costly for very large nnn due to the n×nn\times nn×n kernel matrix.

## Common Mistakes

- ✗

  Confusing the decision boundary scale ambiguity: scaling (**w**, b) changes ∥w∥\|\mathbf{w}\|∥w∥ but not the boundary; the SVM margin definition relies on canonical scaling.
- ✗

  Forgetting to standardize features before training, causing one feature to dominate inner products and distorting margins and kernel behavior.
- ✗

  Assuming all training points influence the solution equally; in SVMs, non-support vectors often have α = 0 and do not affect the classifier.
- ✗

  Overfitting with RBF kernels by choosing both large CCC and large γ\gammaγ, producing very wiggly boundaries and many support vectors.

## Practice

easy

You are given a hyperplane w=(1,2)\mathbf{w}=(1,2)w=(1,2), b=−3b=-3b=−3. (a) Compute the distance from x=(3,1)\mathbf{x}=(3,1)x=(3,1) to the hyperplane. (b) What is the margin band width $2/\|\mathbf{w}\|$? (c) If you scale (**w**, b) by 10, do (a) and (b) change?

**Hint:** Use dist=(w⋅x+b)/∥w∥\text{dist}=(\mathbf{w}\cdot\mathbf{x}+b)/\|\mathbf{w}\|dist=(w⋅x+b)/∥w∥ and remember ∥w∥=w12+w22\|\mathbf{w}\|=\sqrt{w\_1^2+w\_2^2}∥w∥=w12​+w22​​.

Show solution

(a) ∥w∥=12+22=5\|\mathbf{w}\|=\sqrt{1^2+2^2}=\sqrt{5}∥w∥=12+22​=5​. Compute w⋅x+b=(1,2)⋅(3,1)−3=(3+2)−3=2\mathbf{w}\cdot\mathbf{x}+b=(1,2)\cdot(3,1)-3=(3+2)-3=2w⋅x+b=(1,2)⋅(3,1)−3=(3+2)−3=2. Distance =2/5=2/\sqrt{5}=2/5​.\n\n(b) Band width $2/\|\mathbf{w}\|=2/\sqrt{5}$.\n\n(c) Scaling (**w**, b) by 10 leaves the boundary unchanged. The signed distance to the boundary is unchanged because numerator and denominator both scale by 10. But the expression $2/\|\mathbf{w}\|$ computed from the scaled **w** becomes $2/(10\sqrt{5})$, which shows why margin is only meaningful once canonical scaling is fixed.

medium

A soft-margin SVM solution has three points with coefficients: α1=0\alpha\_1=0α1​=0, α2=0.3\alpha\_2=0.3α2​=0.3, α3=C\alpha\_3=Cα3​=C. (a) Which points are support vectors? (b) Which point is likely violating the margin? (c) What condition must hold among labels yiy\_iyi​ and coefficients αi\alpha\_iαi​?

**Hint:** Support vectors have αi>0\alpha\_i>0αi​>0. Points with αi=C\alpha\_i=Cαi​=C are often inside the margin or misclassified. The dual equality constraint is ∑iαiyi=0\sum\_i \alpha\_i y\_i=0∑i​αi​yi​=0.

Show solution

(a) Points 2 and 3 are support vectors because they have α>0\alpha>0α>0.\n\n(b) Point 3 (with α3=C\alpha\_3=Cα3​=C) is likely a margin violator (inside the margin and/or misclassified).\n\n(c) The coefficients must satisfy the dual constraint ∑iαiyi=0\sum\_i \alpha\_i y\_i=0∑i​αi​yi​=0, i.e., α1y1+α2y2+α3y3=0\alpha\_1 y\_1 + \alpha\_2 y\_2 + \alpha\_3 y\_3 = 0α1​y1​+α2​y2​+α3​y3​=0.

hard

Consider an RBF kernel K(x,x′)=exp⁡(−γ∥x−x′∥2)K(\mathbf{x},\mathbf{x}')=\exp(-\gamma\|\mathbf{x}-\mathbf{x}'\|^2)K(x,x′)=exp(−γ∥x−x′∥2). (a) What happens to K(x,x′)K(\mathbf{x},\mathbf{x}')K(x,x′) as γ→0\gamma\to 0γ→0? (b) What happens as γ→∞\gamma\to\inftyγ→∞ for x≠x′\mathbf{x}\ne\mathbf{x}'x=x′? (c) How would these extremes affect the flexibility of an SVM decision boundary?

**Hint:** Use limits of exp⁡(−γd2)\exp(-\gamma d^2)exp(−γd2) as γ\gammaγ changes; interpret kernel value as similarity/influence.

Show solution

(a) As γ→0\gamma\to 0γ→0, K(x,x′)=exp⁡(−γ∥x−x′∥2)→exp⁡(0)=1K(\mathbf{x},\mathbf{x}')=\exp(-\gamma\|\mathbf{x}-\mathbf{x}'\|^2)\to \exp(0)=1K(x,x′)=exp(−γ∥x−x′∥2)→exp(0)=1 for all pairs. The kernel matrix becomes approximately all ones (very low effective complexity).\n\n(b) As γ→∞\gamma\to\inftyγ→∞ and x≠x′\mathbf{x}\ne\mathbf{x}'x=x′, ∥x−x′∥2>0\|\mathbf{x}-\mathbf{x}'\|^2>0∥x−x′∥2>0 so −γ∥x−x′∥2→−∞-\gamma\|\mathbf{x}-\mathbf{x}'\|^2\to -\infty−γ∥x−x′∥2→−∞ and K→0K\to 0K→0. Also, K(x,x)=1K(\mathbf{x},\mathbf{x})=1K(x,x)=1 always. The kernel matrix approaches the identity.\n\n(c) Small γ\gammaγ makes all points look similar, encouraging very smooth/simple boundaries (can underfit). Very large γ\gammaγ makes similarity extremely local, allowing highly flexible boundaries that can interpolate noise (risk of overfitting), especially with large CCC.

## Connections

Next: [Kernel Methods](/tech-tree/kernel-methods/)

Related nodes you may also connect in your mental map:

- •Linear classifiers (hyperplanes, margins)
- •Convex optimization (quadratic programs)
- •Regularization and loss functions (hinge loss vs logistic)
- •Feature scaling and preprocessing

Quality: A (4.4/5)

[← back to tree](/tech-tree/)[browse all →](/tech-tree/inventory/)
