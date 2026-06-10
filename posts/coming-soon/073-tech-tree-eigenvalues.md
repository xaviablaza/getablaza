---
title: Eigenvalues and Eigenvectors
description: Av = λv. Vectors that only scale under transformation.
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
permalink: /tech-tree/eigenvalues/
---

[←Back to Tech Tree](/tech-tree/)

[inventory](/tech-tree/inventory/)[coverage](/tech-tree/coverage/)

# Eigenvalues and Eigenvectors

Linear AlgebraDifficulty: ★★★☆☆Depth: 4Unlocks: 17

Av = λv. Vectors that only scale under transformation.

## Interactive Visualization

⏮◀◀▶▶STEP0.25x1xZOOM

t=0s

## Core Concepts

- -Invariant direction: a nonzero vector whose direction is unchanged by a linear transformation (it is only scaled)
- -Eigenvalue: the scalar factor by which an eigenvector is scaled

## Key Symbols & Notation

lambda (scalar eigenvalue)

## Essential Relationships

- -A v = lambda v : the defining equation linking matrix A, eigenvector v, and eigenvalue lambda
- -det(A - lambda I) = 0 : the characteristic equation whose roots are the eigenvalues
- -Eigenspace for lambda = nullspace of (A - lambda I) : all eigenvectors for a given lambda (plus the zero vector) form a linear subspace

## Prerequisites (2)

[Determinants6 atoms](/tech-tree/determinants/)[Systems of Linear Equations6 atoms](/tech-tree/linear-systems/)

## Unlocks (3)

[Markov Chainslvl 4](/tech-tree/markov-chains/)[Singular Value Decompositionlvl 4](/tech-tree/svd/)[Spectral Graph Theorylvl 4](/tech-tree/spectral-graph-theory/)

Advanced Learning Details

### Graph Position

46

Depth Cost

17

Fan-Out (ROI)

7

Bottleneck Score

4

Chain Length

### Cognitive Load

6

Atomic Elements

35

Total Elements

L2

Percentile Level

L4

Atomic Level

### All Concepts (12)

- - Eigenvalue: a scalar λ for which there exists a nonzero vector v with Av = λv
- - Eigenvector: a nonzero vector v that satisfies Av = λv
- - Eigenspace: the set of all vectors v (including 0) satisfying (A - λI)v = 0 for a given λ
- - Characteristic polynomial: the polynomial p(λ) = det(A - λI)
- - Characteristic equation: det(A - λI) = 0, whose roots are the eigenvalues
- - Algebraic multiplicity: the multiplicity of λ as a root of the characteristic polynomial
- - Geometric multiplicity: the dimension of the eigenspace for λ (i.e., nullity of A - λI)
- - Diagonalization: representing A as A = P D P^{-1} with D diagonal and P invertible
- - Eigenbasis: a basis for the vector space consisting entirely of eigenvectors of A
- - Spectrum: the set of all eigenvalues of A (often written σ(A))
- - Eigendirection: the direction (line through origin) determined by an eigenvector (scales but does not change direction)
- - Zero eigenvalue indicates singularity: λ = 0 is an eigenvalue exactly when A is singular

### Teaching Strategy

Deep-dive lesson - accessible entry point but dense material. Use worked examples and spaced repetition.

A matrix can rotate, stretch, shear, and reflect space. Yet for many transformations there are special directions that behave unusually simply: vectors that don’t “turn” at all—they only scale. Those directions (eigenvectors) and their scale factors (eigenvalues) are the key to understanding long‑term dynamics, stability, and diagonalization.

TL;DR:

Eigenvectors are nonzero vectors **v** such that A**v** = λ**v**. They point in directions left unchanged by A (only scaled). Eigenvalues λ are found by solving det(A − λI) = 0. Once you have them, you can analyze repeated application of A, decouple coupled systems, and connect linear algebra to Markov chains, SVD, and graphs.

## What Is Eigenvalues and Eigenvectors?

### Why this concept exists (motivation)

Linear transformations can be complicated. A general 2D transformation might rotate vectors, stretch them unequally, and shear them so that angles change. If you want to predict what happens after applying the transformation many times—A², A³, …—the complexity compounds.

Eigenvectors and eigenvalues give you **simple “coordinate axes”** (when they exist) in which the transformation behaves like independent scaling along special directions. This is the central idea behind diagonalization, stability analysis, and many algorithms.

### The definition (with intuition)

Let A be an n×n matrix (a linear transformation). An **eigenvector** of A is a **nonzero** vector **v** such that

A**v** = λ**v**

where λ is a scalar. The scalar λ is the **eigenvalue** corresponding to **v**.

Interpretation:

- •**v** is an “invariant direction”: A does not change the direction of **v**.
- •λ tells you how the transformation scales that direction.

If λ > 1, vectors along that eigenvector direction grow.

If 0 < λ < 1, they shrink.

If λ = 0, that direction is sent to the zero vector.

If λ < 0, the direction is flipped and scaled.

### Why **v ≠ 0**?

If **v** = **0**, then A**v** = **0** for any A, and you could write A**0** = λ**0** for any λ. That would make the definition meaningless. Requiring **v** ≠ **0** forces the relationship to describe a genuine property of the transformation.

### A geometric picture (mental model)

Think of A acting on the unit circle in 2D:

- •Many vectors change direction.
- •Eigenvectors are the directions where the image remains on the same line through the origin.

If you draw the line through the origin along **v**, then A maps that entire line back onto itself (possibly reversed). The action on that line is simply “multiply by λ.”

### A first important caution

Not every matrix has enough eigenvectors to form a basis. Some matrices have:

- •no real eigenvectors (e.g., pure rotations in 2D), or
- •too few eigenvectors (defective matrices), even though eigenvalues exist.

This lesson focuses on: (1) how to compute eigenvalues/eigenvectors, (2) what they mean, and (3) why they matter for applications.

## Core Mechanic 1: Finding Eigenvalues via det(A − λI) = 0

### Why the determinant shows up

The eigenvector equation is:

A**v** = λ**v**

Bring everything to one side:

A**v** − λ**v** = **0**

Factor **v** using the identity matrix I (since λ**v** = (λI)**v**):

(A − λI)**v** = **0**

This is a **homogeneous linear system**. You already know a key fact about such systems:

- •(A − λI)**v** = **0** has a **nontrivial solution** (**v** ≠ **0**) iff (A − λI) is **singular**.
- •A matrix is singular iff its determinant is 0.

So λ must satisfy:

det(A − λI) = 0

This equation is called the **characteristic equation**, and det(A − λI) is the **characteristic polynomial**.

### Step-by-step derivation (showing the logic)

Start:

A**v** = λ**v**

Subtract λ**v**:

A**v** − λ**v** = **0**

Rewrite λ**v** as (λI)**v**:

A**v** − (λI)**v** = **0**

Factor out **v**:

(A − λI)**v** = **0**

For **v** ≠ **0** to exist, we need:

(A − λI) is singular

Equivalent to:

det(A − λI) = 0

### What you do in practice

1) Form A − λI

2) Compute det(A − λI)

3) Solve det(A − λI) = 0 for λ

For 2×2 matrices, this is quick. For 3×3 it’s manageable. For larger matrices, you typically use numerical algorithms.

### 2×2 formula as a useful pattern

Let

A = [ a b ]

[ c d ]

Then

A − λI = [ a−λ b ]

[ c d−λ ]

Compute determinant:

det(A − λI) = (a−λ)(d−λ) − bc

= λ² − (a + d)λ + (ad − bc)

So eigenvalues satisfy a quadratic.

### Interpreting coefficients: trace and determinant

For 2×2:

- •Sum of eigenvalues = a + d = tr(A)
- •Product of eigenvalues = ad − bc = det(A)

This is not just a coincidence—it generalizes (with more algebra) to higher dimensions via the characteristic polynomial.

### When eigenvalues might be complex

det(A − λI) = 0 may have complex roots.

Example: a pure rotation in 2D has no real invariant directions, so it has complex eigenvalues/eigenvectors (over ℂ).

For many applications in ML and graphs, the matrices are symmetric (or related to symmetric), and then all eigenvalues are real and eigenvectors can be chosen orthonormal. But you should know that in general eigenvalues can be complex.

## Core Mechanic 2: Finding Eigenvectors by Solving (A − λI)\*\*v\*\* = \*\*0\*\*

### Why solving a linear system gives eigenvectors

Once you have an eigenvalue λ, the eigenvector equation becomes:

(A − λI)**v** = **0**

This is a homogeneous system. The set of all solutions is the **null space** (kernel) of (A − λI). Any nonzero vector in that null space is an eigenvector.

Because you already know Gaussian elimination, the workflow is familiar:

1) Plug in λ

2) Row-reduce (A − λI)

3) Express solutions with free variables

4) Pick any nonzero solution vector

### Eigenvectors come in whole lines (and subspaces)

If **v** is an eigenvector, then any nonzero scalar multiple α**v** is also an eigenvector with the same eigenvalue:

A(α**v**) = αA**v** = α(λ**v**) = λ(α**v**)

So eigenvectors are not “unique”; they represent a direction. More generally, if an eigenvalue has multiple independent eigenvectors, they form an **eigenspace**, which is a subspace.

### Algebraic multiplicity vs geometric multiplicity (gentle intro)

When det(A − λI) = 0, an eigenvalue might repeat.

- •**Algebraic multiplicity**: how many times λ appears as a root of the characteristic polynomial.
- •**Geometric multiplicity**: dimension of the null space of (A − λI), i.e., how many independent eigenvectors you get.

You always have:

1 ≤ geometric multiplicity ≤ algebraic multiplicity

If geometric multiplicity is smaller, the matrix may not have enough eigenvectors to diagonalize.

### Diagonalization preview (why eigenvectors are powerful)

If A has n linearly independent eigenvectors **v**₁,…,**v**ₙ with eigenvalues λ₁,…,λₙ, form the matrix:

V = [ **v**₁ **v**₂ … **v**ₙ ]

Then:

AV = A[**v**₁ … **v**ₙ]

= [A**v**₁ … A**v**ₙ]

= [λ₁**v**₁ … λₙ**v**ₙ]

= [**v**₁ … **v**ₙ] diag(λ₁,…,λₙ)

= VΛ

So:

AV = VΛ

If V is invertible (i.e., eigenvectors are independent), multiply by V⁻¹:

A = VΛV⁻¹

This is diagonalization: in the eigenvector basis, A acts like independent scaling.

### Why repeated powers become easy

If A = VΛV⁻¹, then

A² = (VΛV⁻¹)(VΛV⁻¹) = VΛ²V⁻¹

Aᵏ = VΛᵏV⁻¹

Since Λ is diagonal, Λᵏ just raises each eigenvalue:

Λᵏ = diag(λ₁ᵏ, …, λₙᵏ)

This is the core reason eigenvalues matter for long-term behavior.

## Application/Connection: Dynamics, Markov Chains, SVD, and Graphs

### Why eigenvalues show up everywhere

Many systems update a state by multiplying by a matrix:

**x**ₖ₊₁ = A**x**ₖ

If you can express **x**₀ in an eigenvector basis, you can see which components grow, shrink, oscillate, or remain fixed.

### 1) Markov chains (transition matrices)

A Markov chain with n states often uses a transition matrix P where (depending on convention) columns or rows sum to 1. A **stationary distribution** π satisfies:

Pπ = π

That is exactly an eigenvector equation with eigenvalue λ = 1:

Pπ = 1·π

So π is an eigenvector of P corresponding to eigenvalue 1.

Why λ = 1 matters:

- •It represents a distribution unchanged by the transition.
- •Other eigenvalues (typically with |λ| < 1 for a nice ergodic chain) control how fast the chain converges to π (mixing rate).

### 2) SVD (foreshadowing)

SVD is A = UΣVᵀ. While eigenvalues are not the same as singular values, there is a deep link:

- •Eigenvectors of AᵀA give you the right singular vectors (columns of V).
- •Eigenvalues of AᵀA are the squared singular values:

AᵀA **v** = σ² **v**

So learning eigenvalues now sets you up to understand SVD later.

### 3) Spectral graph theory (adjacency/Laplacian)

Graphs can be encoded by matrices:

- •Adjacency matrix
- •Graph Laplacian L = D − A (degree matrix minus adjacency)

Eigenvalues of L tell you about:

- •connectivity (the number of 0 eigenvalues)
- •clustering (small eigenvalues and their eigenvectors)
- •diffusion on graphs

The reason: many graph processes are linear updates (random walks, diffusion), and eigen-decompositions reveal the “modes” of the network.

### 4) Stability and differential equations (bonus connection)

In continuous-time linear systems:

d**x**/dt = A**x**

Solutions involve e^{tA}. Eigenvalues of A determine whether trajectories grow or decay. Roughly:

- •Re(λ) < 0 ⇒ decay (stable)
- •Re(λ) > 0 ⇒ growth (unstable)

Even if you don’t compute e^{tA} directly, eigenvalues summarize stability.

### A small comparison table (where eigenvalues help)

| Problem type | Matrix equation | Eigenvalue role | What you learn |
| --- | --- | --- | --- |
| Long-run discrete dynamics | **x**ₖ₊₁ = A**x**ₖ | magnitudes | growth/decay per mode |
| Stationary distributions | Pπ = π | λ = 1 | invariant distribution |
| PCA/SVD prep | AᵀA **v** = σ² **v** | σ² are eigenvalues | variance directions |
| Graph connectivity | L**v** = λ**v** | small λ | components/clusters |

The common thread: eigenvectors give “modes,” eigenvalues give their strength.

## Worked Examples (3)

### Example 1: Compute eigenvalues and eigenvectors of a 2×2 matrix

Let A = [[2, 1], [1, 2]]. Find eigenvalues λ and eigenvectors **v**.

1. Start from det(A − λI) = 0.

   A − λI = [[2−λ, 1], [1, 2−λ]].
2. Compute determinant:

   det(A − λI) = (2−λ)(2−λ) − 1·1

   = (2−λ)² − 1

   = (4 − 4λ + λ²) − 1

   = λ² − 4λ + 3.
3. Solve λ² − 4λ + 3 = 0:

   (λ − 1)(λ − 3) = 0

   So eigenvalues are λ₁ = 1 and λ₂ = 3.
4. Find eigenvectors for λ = 3:

   A − 3I = [[2−3, 1], [1, 2−3]] = [[−1, 1], [1, −1]].

   Solve (A − 3I)**v** = **0**.

   Let **v** = (x, y)ᵀ.

   Equations: −x + y = 0 ⇒ y = x.

   So eigenvectors are all nonzero multiples of (1, 1)ᵀ.
5. Find eigenvectors for λ = 1:

   A − I = [[1, 1], [1, 1]].

   Solve (A − I)**v** = **0**.

   Equations: x + y = 0 ⇒ y = −x.

   So eigenvectors are all nonzero multiples of (1, −1)ᵀ.

**Insight:** This symmetric matrix stretches space by 3 along the (1,1) direction and by 1 along the (1,−1) direction. In the eigenvector basis, the transformation becomes diagonal: independent scaling along two perpendicular directions.

### Example 2: Use diagonalization to compute Aᵏ efficiently

Using the same A = [[2,1],[1,2]], compute Aᵏ acting on **x**₀ = (1,0)ᵀ, i.e., **x**ₖ = Aᵏ**x**₀.

1. From Example 1, eigenpairs are:

   λ₁ = 3 with eigenvector **v**₁ = (1,1)ᵀ,

   λ₂ = 1 with eigenvector **v**₂ = (1,−1)ᵀ.
2. Form V and Λ:

   V = [**v**₁ **v**₂] = [[1, 1], [1, −1]].

   Λ = diag(3, 1).
3. Express **x**₀ in the eigenvector basis:

   We want coefficients a, b such that

   **x**₀ = a**v**₁ + b**v**₂.

   So (1,0)ᵀ = a(1,1)ᵀ + b(1,−1)ᵀ

   = (a+b, a−b)ᵀ.
4. Solve for a, b:

   a + b = 1

   a − b = 0

   Add equations: 2a = 1 ⇒ a = 1/2.

   Then b = 1 − a = 1/2.
5. Apply Aᵏ using eigenvalues:

   Aᵏ**x**₀ = aλ₁ᵏ**v**₁ + bλ₂ᵏ**v**₂

   = (1/2)·3ᵏ(1,1)ᵀ + (1/2)·1ᵏ(1,−1)ᵀ.
6. Write components explicitly:

   **x**ₖ = ( (1/2)(3ᵏ + 1), (1/2)(3ᵏ − 1) )ᵀ.

**Insight:** Repeated application of A amplifies the component along the dominant eigenvector (1,1) by 3ᵏ, while the component along (1,−1) stays unchanged (since λ = 1). This is the basic ‘dominant eigenvalue’ phenomenon behind power iteration and Markov chain convergence behavior.

### Example 3: A matrix with a repeated eigenvalue and an eigenspace

Let A = [[4, 0], [0, 4]]. Find eigenvalues/eigenvectors and interpret.

1. Compute A − λI = [[4−λ, 0], [0, 4−λ]].
2. det(A − λI) = (4−λ)(4−λ) = (4−λ)².

   So the only eigenvalue is λ = 4 with algebraic multiplicity 2.
3. Solve (A − 4I)**v** = **0**:

   A − 4I = [[0, 0], [0, 0]].

   So 0·x + 0·y = 0 gives no constraints.
4. Therefore every nonzero vector **v** ∈ ℝ² is an eigenvector:

   A**v** = 4**v** for all **v**.

**Insight:** When A is 4I, the transformation is uniform scaling by 4 in every direction. The eigenspace for λ = 4 is the entire plane (geometric multiplicity 2). This contrasts with matrices that have a repeated eigenvalue but not enough independent eigenvectors.

## Key Takeaways

- ✓

  Eigenvectors **v** satisfy A**v** = λ**v** with **v** ≠ **0**; they represent invariant directions of a linear transformation.
- ✓

  Eigenvalues λ are found by turning the eigenvector condition into a singularity condition: (A − λI)**v** = **0** has nontrivial solutions iff det(A − λI) = 0.
- ✓

  After finding λ, eigenvectors come from solving the homogeneous system (A − λI)**v** = **0** via Gaussian elimination.
- ✓

  Eigenvectors are not unique: any nonzero scalar multiple of an eigenvector is also an eigenvector; eigenvectors for a given λ form an eigenspace (a subspace).
- ✓

  If A has n independent eigenvectors, it diagonalizes as A = VΛV⁻¹, making Aᵏ = VΛᵏV⁻¹ easy to compute.
- ✓

  In Markov chains, stationary distributions are eigenvectors with eigenvalue 1 (Pπ = π).
- ✓

  Eigenvalues summarize long-term behavior: large |λ| modes dominate; |λ| < 1 modes decay; negative or complex eigenvalues introduce sign flips or oscillations.

## Common Mistakes

- ✗

  Forgetting the identity matrix: writing A − λ instead of A − λI, which breaks dimensions and the algebra.
- ✗

  Including **v** = **0** as an eigenvector (it is never allowed).
- ✗

  Solving det(A − λI) = 0 correctly but then plugging λ back into A**v** = λ**v** without rearranging to a solvable system (A − λI)**v** = **0**.
- ✗

  Assuming every matrix is diagonalizable or has real eigenvalues; rotations and defective matrices are important counterexamples.

## Practice

easy

Find the eigenvalues of A = [[5, 2], [0, 1]].

**Hint:** Compute det(A − λI). For an upper triangular matrix, the determinant is the product of diagonal entries.

Show solution

A − λI = [[5−λ, 2], [0, 1−λ]].

det(A − λI) = (5−λ)(1−λ).

Set equal to 0:

(5−λ)(1−λ) = 0 ⇒ λ ∈ {5, 1}.

medium

For A = [[5, 2], [0, 1]], find an eigenvector for each eigenvalue.

**Hint:** Solve (A − λI)**v** = **0** separately for λ = 5 and λ = 1. Use a free variable.

Show solution

For λ = 5:

A − 5I = [[0, 2], [0, −4]].

Solve [[0,2],[0,−4]] (x,y)ᵀ = (0,0)ᵀ.

Equations: 2y = 0 ⇒ y = 0. x is free.

Pick x = 1 ⇒ **v** = (1,0)ᵀ.

For λ = 1:

A − I = [[4, 2], [0, 0]].

Solve 4x + 2y = 0 ⇒ 2x + y = 0 ⇒ y = −2x.

Pick x = 1 ⇒ **v** = (1,−2)ᵀ.

hard

Let A = [[2, 1], [0, 2]]. (a) Find its eigenvalues. (b) Find the eigenspace for λ = 2. (c) Does A have two independent eigenvectors?

**Hint:** You will get a repeated eigenvalue. The key is the null space of (A − 2I). Compare algebraic vs geometric multiplicity.

Show solution

(a) A − λI = [[2−λ, 1], [0, 2−λ]].

Determinant: det(A − λI) = (2−λ)(2−λ) = (2−λ)².

So λ = 2 with algebraic multiplicity 2.

(b) For λ = 2:

A − 2I = [[0, 1], [0, 0]].

Solve [[0,1],[0,0]](x,y)ᵀ = (0,0)ᵀ ⇒ y = 0, x free.

So eigenspace = { (x,0)ᵀ : x ∈ ℝ } = span{(1,0)ᵀ}.

(c) No. The eigenspace is 1-dimensional, so there is only 1 independent eigenvector even though the eigenvalue repeats. Therefore A is not diagonalizable over ℝ.

## Connections

Next nodes you can unlock and why they depend on eigenvalues:

- •[Markov Chains](/tech-tree/markov-chains/): stationary distributions satisfy Pπ = π (eigenvalue 1), and other eigenvalues control convergence rates.
- •[Singular Value Decomposition](/tech-tree/svd/): right singular vectors are eigenvectors of AᵀA; singular values relate via σ² = eigenvalues(AᵀA).
- •[Spectral Graph Theory](/tech-tree/spectral-graph-theory/): eigenvalues/eigenvectors of adjacency or Laplacian matrices reveal connectivity, clustering, and diffusion modes.

Helpful supporting knowledge:

- •[Determinants](/tech-tree/determinants/): det(A − λI) = 0 is the characteristic equation.
- •[Systems of Linear Equations](/tech-tree/systems-linear-equations/): eigenvectors are found by solving homogeneous systems (A − λI)**v** = **0**.

Quality: A (4.4/5)

[← back to tree](/tech-tree/)[browse all →](/tech-tree/inventory/)
