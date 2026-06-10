---
title: Projections
description: Projecting vectors onto subspaces. Least squares.
date: '2026-07-01'
scheduled: '2026-11-15'
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
inspiration_url: https://templeton.host/tech-tree/projections/
inspiration_category: tech-tree
---

> Source-copy draft imported from [https://templeton.host/tech-tree/projections/](https://templeton.host/tech-tree/projections/). Names, domain references, and local media paths were adapted for Xavi Ablaza / getablaza.com.

[←Back to Tech Tree](/tech-tree/)

[inventory](/tech-tree/inventory/)[coverage](/tech-tree/coverage/)

# Projections

Linear AlgebraDifficulty: ★★★☆☆Depth: 6Unlocks: 5

Projecting vectors onto subspaces. Least squares.

## Interactive Visualization

⏮◀◀▶▶STEP0.25x1xZOOM

t=0s

## Core Concepts

- -Orthogonal projection: for vector v and subspace S, proj\_S(v) is the unique element u in S that minimizes ||v - u||.
- -Projection operator as a linear map: for a fixed subspace S there is a matrix P that maps any vector to its projection in S; for orthogonal projections P is idempotent (P^2 = P) and symmetric (P^T = P).

## Key Symbols & Notation

Projection matrix P = A (A^T A)^{-1} A^T (when A has full column rank and S = Col(A)).Normal equations: A^T A x\_hat = A^T b (the linear system whose solution x\_hat gives the least-squares fit).

## Essential Relationships

- -Residual orthogonality: v - proj\_S(v) is orthogonal to every vector in S (this condition characterizes the orthogonal projection).
- -Least-squares equivalence: the minimizer x\_hat of ||Ax - b|| satisfies Ax\_hat = proj\_{Col(A)}(b), and x\_hat is obtained by solving the normal equations.

## Prerequisites (2)

[Orthogonality5 atoms](/tech-tree/orthogonality/)[Dot Product5 atoms](/tech-tree/dot-product/)

## Unlocks (1)

[Linear Regressionlvl 3](/tech-tree/linear-regression/)

Advanced Learning Details

### Graph Position

50

Depth Cost

5

Fan-Out (ROI)

1

Bottleneck Score

6

Chain Length

### Cognitive Load

6

Atomic Elements

39

Total Elements

L2

Percentile Level

L4

Atomic Level

### All Concepts (15)

- - Projection of a vector onto another vector (vector component parallel to a given vector and the perpendicular component)
- - Orthogonal projection of a vector onto a subspace (line, plane, or general subspace)
- - Projection matrix (linear operator that maps any vector to its orthogonal projection onto a subspace)
- - Orthogonal decomposition theorem: unique decomposition of a vector as projection plus orthogonal residual
- - Residual vector (difference between original vector and its projection) and its properties
- - Least-squares problem: finding x that minimizes ||Ax - b||^2 for an overdetermined linear system
- - Normal equations as the algebraic condition for least-squares solutions
- - Closed-form least-squares solution when A^T A is invertible: x\_hat = (A^T A)^{-1} A^T b
- - Expression for the orthogonal projection onto Col(A): p = A(A^T A)^{-1} A^T b (projection via A)
- - Interpretation of least squares as projecting b onto the column space Col(A) (geometric best-fit)
- - Moore–Penrose pseudoinverse as a general tool to compute least-squares solutions when A^T A is not invertible
- - Full-column-rank condition (rank(A)=n) and its role in uniqueness of least-squares solution
- - Closest-point (best-approximation) property: the projection is the point in the subspace minimizing Euclidean distance to the original vector
- - Simplification when using an orthonormal basis Q for the subspace (projection becomes Q Q^T b and coordinate extraction Q^T b)
- - Algebraic properties of orthogonal projection operators: linearity, idempotence (P^2 = P), and symmetry for orthogonal projections (P^T = P)

### Teaching Strategy

Multi-session curriculum - substantial prior knowledge and complex material. Use mastery gates and deliberate practice.

When data doesn’t fit your model perfectly, you don’t “solve” A**x** = **b**—you choose the best approximation. Projections are the geometric rule that turns “best approximation” into a precise, computable object.

TL;DR:

Projecting a vector **v** onto a subspace S means finding the unique **u** ∈ S that minimizes ‖**v** − **u**‖. For S = Col(A) with full column rank, the orthogonal projection is **p** = P**b**, where P = A(AᵀA)⁻¹Aᵀ. Least squares chooses **x̂** that makes A**x̂** the projection of **b** onto Col(A), leading to the normal equations AᵀA**x̂** = Aᵀ**b**.

## What Is a Projection?

### Why projections matter (motivation)

In linear algebra, a subspace S is a “legal set of directions.” Often, the vector you have—call it **v**—doesn’t lie inside S. That mismatch happens constantly:

- •A measurement **b** doesn’t lie exactly in the column space of a model matrix A.
- •A noisy signal doesn’t lie exactly in the subspace spanned by your chosen basis functions.
- •A complicated vector is approximated using a lower-dimensional subspace for compression.

In all these cases, you want a principled way to replace **v** with a nearby vector **u** that *does* lie in S. The key idea is: choose the closest one.

### Definition (orthogonal projection)

Let S ⊂ ℝⁿ be a subspace, and let **v** ∈ ℝⁿ. The **orthogonal projection** of **v** onto S, written proj\_S(**v**), is the unique vector **u** ∈ S that minimizes the distance to **v**:

- •**u** = proj\_S(**v**) is the unique minimizer of

minimize over **u** ∈ S: ‖**v** − **u**‖.

This is a geometric “drop a perpendicular” idea generalized from 2D/3D to ℝⁿ.

### The orthogonality condition (what makes it “orthogonal”)

The minimizer isn’t just any closest point. It satisfies a very specific condition:

Let **p** = proj\_S(**v**). Define the **residual** (error) **r** = **v** − **p**.

Then:

- •**r** ⟂ S

Meaning **r** is orthogonal to *every* vector in S:

- •∀ **s** ∈ S, **s**ᵀ(**v** − **p**) = 0.

This is the characterization that makes projections computable.

### Uniqueness (why there is exactly one best point)

Because S is a subspace (hence closed and convex) and the objective ‖**v** − **u**‖² is strictly convex in **u**, there is exactly one minimizer.

Geometrically: the set of points in S is “flat,” and the distance function has a single lowest point when you look from **v** toward that flat set.

### Decomposing a vector into parallel + perpendicular parts

Orthogonal projection gives a clean decomposition:

- •**v** = **p** + **r**
- •**p** ∈ S
- •**r** ∈ S⊥
- •**p** ⟂ **r**

So projection is not merely “closest point.” It is a structured split into a component inside the subspace and a component orthogonal to it.

### A quick sanity check: 1D subspace (a line)

If S is the span of a nonzero vector **a**, then the projection is the familiar formula:

- •proj\_S(**v**) = ((**a**ᵀ**v**) / (**a**ᵀ**a**)) **a**.

If **a** is unit length (‖**a**‖ = 1), this simplifies to:

- •proj\_S(**v**) = (**a**ᵀ**v**) **a**.

The general subspace case is this idea repeated, but with multiple basis directions at once.

## Core Mechanic 1: Orthogonal Projections via Geometry and Conditions

### Why we need a computable rule

The definition “pick the closest **u** ∈ S” is conceptually perfect, but it doesn’t yet tell you how to compute **u**. The trick is to translate “closest” into an equation.

Instead of minimizing ‖**v** − **u**‖ directly, minimize the squared norm (same minimizer, easier algebra):

- •minimize over **u** ∈ S: f(**u**) = ‖**v** − **u**‖².

### The key idea: the residual is orthogonal to the subspace

Let **p** ∈ S be the minimizer. Consider any direction **s** ∈ S (a feasible direction to move within the subspace). If you nudge **p** inside the subspace by t**s**, the distance to **v** cannot decrease at t = 0 (otherwise **p** wasn’t minimal).

Compute the derivative:

f(**p** + t**s**) = ‖**v** − (**p** + t**s**)‖²

= ‖(**v** − **p**) − t**s**‖²

= ((**v** − **p**) − t**s**)ᵀ((**v** − **p**) − t**s**)

= ‖**v** − **p**‖² − 2t **s**ᵀ(**v** − **p**) + t²‖**s**‖².

At a minimum, derivative at t = 0 is 0:

d/dt f(**p** + t**s**) |\_{t=0} = −2 **s**ᵀ(**v** − **p**) = 0.

So:

- •**s**ᵀ(**v** − **p**) = 0 for all **s** ∈ S,

which is exactly:

- •**v** − **p** ∈ S⊥.

This is the most important practical fact: *the residual is orthogonal to the model subspace.*

### Using a basis: turning “orthogonal to S” into linear equations

Suppose S is spanned by k linearly independent vectors **a**₁, …, **a**ₖ. Put them into a matrix A ∈ ℝⁿˣᵏ as columns:

- •A = [**a**₁ … **a**ₖ]
- •S = Col(A).

Any vector in S looks like A**x** for some **x** ∈ ℝᵏ.

We want **p** = A**x** that makes **r** = **v** − A**x** orthogonal to S.

Being orthogonal to S is equivalent to being orthogonal to every column of A:

- •**a**ᵢᵀ(**v** − A**x**) = 0 for i = 1..k.

Stack these k equations:

- •Aᵀ(**v** − A**x**) = **0**

⇒ AᵀA**x** = Aᵀ**v**.

These are the **normal equations** in the language of least squares (we’ll return to that). For projection, they are simply the orthogonality conditions written in matrix form.

### Orthonormal basis special case (fast mental model)

If the columns of Q ∈ ℝⁿˣᵏ are orthonormal (QᵀQ = I), then projection is especially simple.

Let S = Col(Q). We want **p** ∈ S of the form **p** = Q**c**.

Use the orthogonality condition:

Qᵀ(**v** − Q**c**) = **0**

⇒ Qᵀ**v** − QᵀQ**c** = **0**

⇒ Qᵀ**v** − I**c** = **0**

⇒ **c** = Qᵀ**v**.

So:

- •proj\_S(**v**) = Q(Qᵀ**v**).

Interpretation:

1) Compute coordinates **c** = Qᵀ**v** (dot products against basis vectors).

2) Rebuild the vector in the subspace: Q**c**.

This is the cleanest picture of what projection does.

### Pythagorean identity (what you gain from orthogonality)

With **v** = **p** + **r** and **p** ⟂ **r**:

‖**v**‖² = ‖**p**‖² + ‖**r**‖².

This is often used to reason about error. Projection chooses **p** to make ‖**r**‖ as small as possible, so it also makes ‖**p**‖ as large as possible among all vectors in S that could approximate **v**.

## Core Mechanic 2: Projection as a Linear Map (Projection Matrices)

### Why introduce a projection matrix?

If you will project many different vectors onto the same subspace S, you want a reusable operator. Projections are not just geometric constructions; they are linear transformations.

For a fixed subspace S ⊂ ℝⁿ, the orthogonal projection is a function P: ℝⁿ → ℝⁿ such that:

- •P(**v**) = proj\_S(**v**).

When written in standard coordinates, this function is multiplication by an n×n matrix, also called P.

### Column-space projection: P = A(AᵀA)⁻¹Aᵀ

Assume A ∈ ℝⁿˣᵏ has full column rank (its columns are independent). Then AᵀA is invertible.

Given **b** ∈ ℝⁿ, the projection of **b** onto Col(A) is **p** = A**x̂** where **x̂** solves the normal equations:

AᵀA**x̂** = Aᵀ**b**

⇒ **x̂** = (AᵀA)⁻¹Aᵀ**b**.

Plug back into **p**:

**p** = A**x̂**

= A((AᵀA)⁻¹Aᵀ**b**)

= (A(AᵀA)⁻¹Aᵀ)**b**.

So the projection matrix is:

- •P = A(AᵀA)⁻¹Aᵀ
- •proj\_Col(A)(**b**) = P**b**.

### What P does (and why it’s special)

For an orthogonal projection matrix P onto S:

1) **Idempotent:** P² = P

Apply the projection twice: once you’re in the subspace, projecting again does nothing.

2) **Symmetric:** Pᵀ = P

This encodes “orthogonal” in matrix form.

3) **Range and null space:**

- •Range(P) = S
- •Null(P) = S⊥

So P keeps the S component and kills the orthogonal component.

### Verifying idempotence (show the work)

Let P = A(AᵀA)⁻¹Aᵀ. Then:

P² = [A(AᵀA)⁻¹Aᵀ][A(AᵀA)⁻¹Aᵀ]

= A(AᵀA)⁻¹(AᵀA)(AᵀA)⁻¹Aᵀ

= A(I)(AᵀA)⁻¹Aᵀ

= A(AᵀA)⁻¹Aᵀ

= P.

The step (AᵀA)⁻¹(AᵀA) = I works because A has full column rank.

### Verifying symmetry (show the work)

Pᵀ = [A(AᵀA)⁻¹Aᵀ]ᵀ

= (Aᵀ)ᵀ[(AᵀA)⁻¹]ᵀAᵀ

= A[(AᵀA)⁻¹]Aᵀ

= P,

because AᵀA is symmetric, so (AᵀA)⁻¹ is also symmetric.

### Orthonormal columns shortcut: P = QQᵀ

If Q has orthonormal columns (QᵀQ = I), then:

P = Q(QᵀQ)⁻¹Qᵀ = QIQᵀ = QQᵀ.

This is why orthonormal bases are so valuable: they make projection formulas simpler and numerically more stable.

### Eigenvalues intuition (optional but useful)

From P² = P, any eigenvalue λ satisfies λ² = λ, so λ ∈ {0, 1}.

- •Eigenvalue 1 directions are vectors in S (they stay unchanged).
- •Eigenvalue 0 directions are vectors in S⊥ (they get projected to 0).

So P is literally a “keep these directions, erase those directions” operator.

## Application/Connection: Least Squares and the Normal Equations

### Why least squares is projection in disguise

Consider a system A**x** = **b**. If **b** ∈ Col(A), there is an exact solution. But if **b** is not in Col(A), there is no **x** that makes A**x** equal to **b**.

Least squares replaces “solve exactly” with “get as close as possible”:

- •minimize over **x**: ‖A**x** − **b**‖.

This is the same geometry as projection:

- •The set {A**x** : **x** ∈ ℝᵏ} is exactly Col(A).
- •You are choosing the closest point in Col(A) to **b**.

So the least-squares fitted vector A**x̂** is:

- •A**x̂** = proj\_Col(A)(**b**) = P**b**.

### Deriving the normal equations (show the work)

Minimize the squared error:

f(**x**) = ‖A**x** − **b**‖²

= (A**x** − **b**)ᵀ(A**x** − **b**).

Expand:

f(**x**) = **x**ᵀAᵀA**x** − 2**x**ᵀAᵀ**b** + **b**ᵀ**b**.

Take gradient and set to zero:

∇f(**x**) = 2AᵀA**x** − 2Aᵀ**b** = **0**

⇒ AᵀA**x̂** = Aᵀ**b**.

These are the **normal equations**.

Geometric meaning: the residual **r** = **b** − A**x̂** is orthogonal to Col(A):

Aᵀ(**b** − A**x̂**) = **0**.

That is exactly the orthogonality condition for projection.

### When does the formula (AᵀA)⁻¹Aᵀ work?

If A has full column rank, AᵀA is invertible and:

- •**x̂** = (AᵀA)⁻¹Aᵀ**b**
- •A**x̂** = A(AᵀA)⁻¹Aᵀ**b** = P**b**.

If A does *not* have full column rank, there are infinitely many least-squares minimizers; then one typically uses the pseudoinverse A⁺ (outside this node’s core scope, but good to know).

### Residual properties you can rely on

Let **p** = A**x̂** and **r** = **b** − **p**.

- •**p** ∈ Col(A)
- •**r** ⟂ Col(A)
- •**b** = **p** + **r**
- •‖**b**‖² = ‖**p**‖² + ‖**r**‖² (Pythagorean)

This gives a stable mental model: least squares chooses the decomposition of **b** into “explained by the model subspace” plus “leftover orthogonal noise.”

### Connection to linear regression

In linear regression, A is the design matrix, **x** is the parameter vector, and **b** (often written **y**) is the target output. The fitted predictions A**x̂** are the projection of **y** onto Col(A).

That single sentence unifies:

- •why residuals are orthogonal to features,
- •why the normal equations appear,
- •why adding more columns to A can only reduce training error (you enlarge the subspace, so the closest point can only get closer).

## Worked Examples (3)

### Project \*\*v\*\* onto a line span(\*\*a\*\*)

Let **a** = (2, 1) and **v** = (1, 3). Let S = span(**a**) ⊂ ℝ². Compute proj\_S(**v**) and the residual **r**.

1. Use the line projection formula:

   proj\_S(**v**) = ((**a**ᵀ**v**) / (**a**ᵀ**a**)) **a**.
2. Compute dot products:

   **a**ᵀ**v** = (2, 1)·(1, 3) = 2·1 + 1·3 = 5.

   **a**ᵀ**a** = (2, 1)·(2, 1) = 2² + 1² = 5.
3. Compute the scalar coefficient:

   (**a**ᵀ**v**) / (**a**ᵀ**a**) = 5/5 = 1.
4. Compute the projection:

   proj\_S(**v**) = 1·**a** = (2, 1).
5. Compute the residual:

   **r** = **v** − proj\_S(**v**) = (1, 3) − (2, 1) = (−1, 2).
6. Check orthogonality to the subspace (it suffices to check ⟂ to **a**):

   **a**ᵀ**r** = (2, 1)·(−1, 2) = 2(−1) + 1(2) = 0.

   So **r** ⟂ span(**a**), as required.

**Insight:** The closest point on a line is found by matching the component of **v** along the line direction and discarding the perpendicular component. The residual must be orthogonal to the line—this condition is what generalizes to higher-dimensional subspaces.

### Projection onto Col(A) using P = A(AᵀA)⁻¹Aᵀ

Let A = [[1],[1],[0]] (a 3×1 matrix) and **b** = (2, 0, 1). Compute the projection of **b** onto Col(A) and verify P² = P.

1. Interpretation:

   Col(A) is the line in ℝ³ spanned by **a** = (1, 1, 0). We will compute P explicitly.
2. Compute AᵀA:

   AᵀA = [1 1 0]·[1; 1; 0] = 1² + 1² + 0² = 2.

   So (AᵀA)⁻¹ = 1/2.
3. Compute P:

   P = A(AᵀA)⁻¹Aᵀ

   = [1; 1; 0](1/2)[1 1 0]

   = (1/2)

   [[1·1, 1·1, 1·0],

   [1·1, 1·1, 1·0],

   [0·1, 0·1, 0·0]]

   = (1/2)

   [[1, 1, 0],

   [1, 1, 0],

   [0, 0, 0]].
4. Project **b**:

   **p** = P**b**

   = (1/2)

   [[1, 1, 0],

   [1, 1, 0],

   [0, 0, 0]]

   [2; 0; 1]

   = (1/2)

   [1·2 + 1·0 + 0·1;

   1·2 + 1·0 + 0·1;

   0]

   = (1/2)[2; 2; 0]

   = (1, 1, 0).
5. Residual:

   **r** = **b** − **p** = (2, 0, 1) − (1, 1, 0) = (1, −1, 1).

   Check orthogonality to Col(A):

   **a**ᵀ**r** = (1, 1, 0)·(1, −1, 1) = 1 − 1 + 0 = 0.
6. Verify idempotence (compute P²):

   First note P = (1/2)M with M = [[1,1,0],[1,1,0],[0,0,0]].

   Compute M²:

   M² = [[1,1,0],[1,1,0],[0,0,0]]·[[1,1,0],[1,1,0],[0,0,0]]

   = [[2,2,0],[2,2,0],[0,0,0]]

   = 2M.

   So P² = (1/2)² M² = (1/4)(2M) = (1/2)M = P.

**Insight:** The matrix P acts as a reusable operator: any **b** is decomposed into **p** ∈ Col(A) and **r** ⟂ Col(A). The algebraic identities P² = P and Pᵀ = P encode the geometric facts “projecting twice changes nothing” and “the residual is orthogonal.”

### Least squares fit as a projection (normal equations)

Fit **b** = (1, 2, 2) with a model A**x** where A has two columns:

A = [[1,0],[1,1],[1,2]].

Compute the least-squares solution **x̂** and the fitted vector **p** = A**x̂**.

1. Set up the normal equations:

   AᵀA**x̂** = Aᵀ**b**.
2. Compute AᵀA.

   Aᵀ = [[1,1,1],[0,1,2]].

   So:

   AᵀA = [[1,1,1],[0,1,2]]·[[1,0],[1,1],[1,2]]

   = [[1+1+1, 0+1+2],

   [0+1+2, 0²+1²+2²]]

   = [[3, 3],

   [3, 5]].
3. Compute Aᵀ**b**:

   Aᵀ**b** = [[1,1,1],[0,1,2]]·[1;2;2]

   = [1+2+2;

   0·1 + 1·2 + 2·2]

   = [5;

   6].
4. Solve [[3,3],[3,5]] **x̂** = [5,6].

   Let **x̂** = (x₁, x₂).

   Equations:

   3x₁ + 3x₂ = 5

   3x₁ + 5x₂ = 6

   Subtract first from second:

   (3x₁ + 5x₂) − (3x₁ + 3x₂) = 6 − 5

   2x₂ = 1 ⇒ x₂ = 1/2.

   Plug back:

   3x₁ + 3(1/2) = 5

   3x₁ + 3/2 = 5

   3x₁ = 5 − 3/2 = 10/2 − 3/2 = 7/2

   x₁ = 7/6.
5. Compute fitted vector **p** = A**x̂**:

   A**x̂** = [[1,0],[1,1],[1,2]]·[7/6; 1/2]

   = [7/6 + 0;

   7/6 + 1/2;

   7/6 + 2·(1/2)]

   = [7/6;

   7/6 + 3/6;

   7/6 + 6/6]

   = [7/6;

   10/6;

   13/6]

   = (7/6, 5/3, 13/6).
6. Compute residual **r** = **b** − **p**:

   **r** = (1,2,2) − (7/6, 5/3, 13/6)

   = (6/6−7/6, 6/3−5/3, 12/6−13/6)

   = (−1/6, 1/3, −1/6).

   Check orthogonality to Col(A) by verifying Aᵀ**r** = **0**:

   Aᵀ**r** = [[1,1,1],[0,1,2]]·[−1/6; 1/3; −1/6]

   = [−1/6 + 1/3 − 1/6;

   0·(−1/6) + 1·(1/3) + 2·(−1/6)]

   = [0;

   1/3 − 2/6]

   = [0;

   0].

**Insight:** Least squares chooses **x̂** so that the residual is orthogonal to every column of A. That orthogonality is exactly the geometric condition for projection onto Col(A).

## Key Takeaways

- ✓

  proj\_S(**v**) is the unique **u** ∈ S minimizing ‖**v** − **u**‖; equivalently, the residual **v** − **u** lies in S⊥.
- ✓

  Projection decomposes **v** as **v** = **p** + **r** with **p** ∈ S, **r** ∈ S⊥, and **p** ⟂ **r**.
- ✓

  If S = Col(A) and A has full column rank, the projection matrix is P = A(AᵀA)⁻¹Aᵀ and proj\_S(**b**) = P**b**.
- ✓

  Orthogonal projection matrices satisfy P² = P (idempotent) and Pᵀ = P (symmetric).
- ✓

  With an orthonormal basis Q for S, projection simplifies to proj\_S(**v**) = Q(Qᵀ**v**) and P = QQᵀ.
- ✓

  Least squares min ‖A**x** − **b**‖ produces A**x̂** = proj\_Col(A)(**b**) and leads to the normal equations AᵀA**x̂** = Aᵀ**b**.
- ✓

  Geometrically, least squares finds the closest point in Col(A) to **b**; algebraically, it enforces Aᵀ(**b** − A**x̂**) = **0**.

## Common Mistakes

- ✗

  Forgetting the orthogonality condition: the residual must be orthogonal to the *entire subspace* (all columns of A), not just to the projected vector.
- ✗

  Using P = A(AᵀA)⁻¹Aᵀ when A is not full column rank (AᵀA not invertible). In that case you need a different tool (e.g., pseudoinverse).
- ✗

  Confusing projection onto Col(A) with projection onto the row space; the formulas involve Aᵀ differently and live in different ambient spaces.
- ✗

  Assuming every idempotent matrix is an orthogonal projection: orthogonal projections require both P² = P and Pᵀ = P.

## Practice

easy

Let **a** = (1, −2, 2) and **v** = (2, 1, 0). Compute proj\_span(**a**)(**v**) and the residual **r**. Verify **a**ᵀ**r** = 0.

**Hint:** Use proj\_span(**a**)(**v**) = ((**a**ᵀ**v**) / (**a**ᵀ**a**)) **a**.

Show solution

**a**ᵀ**v** = (1,−2,2)·(2,1,0) = 2 − 2 + 0 = 0.

**a**ᵀ**a** = 1² + (−2)² + 2² = 1 + 4 + 4 = 9.

Coefficient = 0/9 = 0.

Projection = 0·**a** = (0,0,0).

Residual **r** = **v** − **0** = (2,1,0).

Check: **a**ᵀ**r** = **a**ᵀ**v** = 0, so orthogonality holds.

medium

Let A = [[1,1],[1,0],[0,1]] and **b** = (1,2,3). (i) Compute **x̂** solving AᵀA**x̂** = Aᵀ**b**. (ii) Compute **p** = A**x̂**. (iii) Compute **r** = **b** − **p** and verify Aᵀ**r** = **0**.

**Hint:** Compute AᵀA (2×2) and Aᵀ**b** (2×1), solve the 2×2 system, then form **p** and **r**.

Show solution

Aᵀ = [[1,1,0],[1,0,1]].

AᵀA = [[1,1,0],[1,0,1]]·[[1,1],[1,0],[0,1]]

= [[1²+1²+0², 1·1+1·0+0·1],

[1·1+0·1+1·0, 1²+0²+1²]]

= [[2, 1],

[1, 2]].

Aᵀ**b** = [[1,1,0],[1,0,1]]·[1;2;3] = [1+2+0; 1+0+3] = [3;4].

Solve [[2,1],[1,2]] [x₁;x₂] = [3;4].

From 2x₁ + x₂ = 3 ⇒ x₂ = 3 − 2x₁.

Plug into x₁ + 2x₂ = 4:

x₁ + 2(3 − 2x₁) = 4 ⇒ x₁ + 6 − 4x₁ = 4 ⇒ −3x₁ = −2 ⇒ x₁ = 2/3.

Then x₂ = 3 − 2(2/3) = 3 − 4/3 = 5/3.

So **x̂** = (2/3, 5/3).

Compute **p** = A**x̂**:

A**x̂** = [[1,1],[1,0],[0,1]]·[2/3; 5/3]

= [2/3+5/3; 2/3; 5/3]

= [7/3; 2/3; 5/3].

Residual **r** = **b** − **p** = [1;2;3] − [7/3;2/3;5/3]

= [3/3−7/3; 6/3−2/3; 9/3−5/3]

= [−4/3; 4/3; 4/3].

Verify Aᵀ**r**:

Aᵀ**r** = [[1,1,0],[1,0,1]]·[−4/3; 4/3; 4/3]

= [−4/3 + 4/3 + 0; −4/3 + 0 + 4/3] = [0;0].

hard

Suppose P is an orthogonal projection matrix in ℝⁿ (so P² = P and Pᵀ = P). Show that for any **v**, the residual **r** = **v** − P**v** is orthogonal to every vector in Range(P).

**Hint:** Take an arbitrary **y** in Range(P). Write **y** = P**x** for some **x**. Compute **y**ᵀ**r** and use symmetry/idempotence.

Show solution

Let **y** ∈ Range(P). Then ∃ **x** such that **y** = P**x**.

Let **r** = **v** − P**v**.

Compute:

**y**ᵀ**r** = (P**x**)ᵀ(**v** − P**v**)

= **x**ᵀPᵀ(**v** − P**v**) (move P using transpose)

= **x**ᵀP(**v** − P**v**) (since Pᵀ = P)

= **x**ᵀ(P**v** − P²**v**)

= **x**ᵀ(P**v** − P**v**) (since P² = P)

= **x**ᵀ**0**

= 0.

So **y**ᵀ**r** = 0 for all **y** ∈ Range(P), meaning **r** ⟂ Range(P).

## Connections

Next up: projections are the geometric backbone of least squares regression.

- •[Linear Regression](/tech-tree/linear-regression/)

Related reinforcement nodes you may have seen:

- •[Orthogonality](/tech-tree/orthogonality/)
- •[Dot Product](/tech-tree/dot-product/)

Quality: A (4.6/5)

[← back to tree](/tech-tree/)[browse all →](/tech-tree/inventory/)
