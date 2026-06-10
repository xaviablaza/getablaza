---
title: Singular Value Decomposition
description: A = UΣV^T. Fundamental matrix factorization.
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
source_format: html
inspiration_url: https://templeton.host/tech-tree/svd/
inspiration_category: tech-tree
---

> Source-copy draft imported from [https://templeton.host/tech-tree/svd/](https://templeton.host/tech-tree/svd/). Names, domain references, and local media paths were adapted for Xavi Ablaza / getablaza.com.

[←Back to Tech Tree](/tech-tree/)

[inventory](/tech-tree/inventory/)[coverage](/tech-tree/coverage/)

# Singular Value Decomposition

Linear AlgebraDifficulty: ★★★★☆Depth: 6Unlocks: 2

A = UΣV^T. Fundamental matrix factorization.

## Interactive Visualization

⏮◀◀▶▶STEP0.25x1xZOOM

t=0s

## Core Concepts

- -Existence of orthonormal factorization: any real m-by-n matrix can be represented using orthonormal bases for domain and codomain plus nonnegative scale factors
- -Geometric interpretation: singular values are the nonnegative scale factors that map orthogonal directions to orthogonal directions (unit sphere maps to an ellipsoid)

## Key Symbols & Notation

U and V (orthonormal matrices whose columns are left and right singular vectors)Sigma (rectangular diagonal matrix of nonnegative entries called singular values)

## Essential Relationships

- -A = U \* Sigma \* V^T (the singular value decomposition)
- -Columns of U are eigenvectors of A \* A^T; columns of V are eigenvectors of A^T \* A; singular values = square roots of the corresponding eigenvalues

## Prerequisites (2)

[Eigenvalues and Eigenvectors6 atoms](/tech-tree/eigenvalues/)[Orthogonality5 atoms](/tech-tree/orthogonality/)

## Unlocks (1)

[Principal Component Analysislvl 4](/tech-tree/pca/)

Advanced Learning Details

### Graph Position

84

Depth Cost

2

Fan-Out (ROI)

1

Bottleneck Score

6

Chain Length

### Cognitive Load

6

Atomic Elements

46

Total Elements

L3

Percentile Level

L4

Atomic Level

### All Concepts (16)

- - Singular value: a nonnegative scalar σ\_i that measures how much A stretches (or compresses) along a particular orthonormal direction.
- - Right singular vector: v\_i (column of V) - an orthonormal input direction in the domain associated with σ\_i.
- - Left singular vector: u\_i (column of U) - an orthonormal output direction in the codomain associated with σ\_i.
- - Σ (Sigma) matrix: a diagonal matrix whose diagonal entries are the singular values σ\_i, usually arranged in nonincreasing order.
- - Full SVD factorization: any real m×n matrix A can be written A = U Σ V^T with U and V orthogonal and Σ rectangular-diagonal.
- - Rotation–scaling–rotation view: SVD decomposes A into (i) an orthonormal change of input basis (V^T), (ii) axis-aligned scaling (Σ), and (iii) an orthonormal change of output basis (U).
- - Geometric interpretation: A maps the unit sphere in the domain to an ellipsoid in the codomain whose principal axes lengths are the singular values and directions are the left singular vectors.
- - Rank via singular values: the rank of A equals the number of nonzero singular values.
- - Nullspace relation: right singular vectors with σ\_i = 0 form a basis for the nullspace (kernel) of A.
- - Column-space relation: left singular vectors corresponding to nonzero σ\_i span the column space (range) of A.
- - Pseudoinverse via SVD: a stabilized inverse built by reciprocals of nonzero singular values (Σ^+), yielding A^+ = V Σ^+ U^T.
- - Truncated (low-rank) SVD: keeping only the largest k singular values/vectors yields a rank-k approximation of A.
- - Existence without diagonalizability: SVD exists for any (possibly non-square, non-diagonalizable) real matrix - no eigen-decomposition requirement.
- - Compact/economy SVD: a reduced-size SVD that omits zero singular values and corresponding columns of U and V to save space.
- - Nonuniqueness/degeneracy: SVD is unique up to sign (or orthogonal transforms in subspaces when singular values are repeated).
- - Operator-norm and Frobenius interpretations: singular values quantify standard matrix norms and energy (see relationships).

### Teaching Strategy

Multi-session curriculum - substantial prior knowledge and complex material. Use mastery gates and deliberate practice.

Most linear algebra tools tell you what a matrix does to special vectors. Eigenvectors work beautifully—when the matrix is square and behaves nicely. The Singular Value Decomposition (SVD) is the “works anyway” factorization: it describes how any real m×n matrix transforms space by rotating (or reflecting), scaling along orthogonal directions, then rotating again.

TL;DR:

For any real matrix A ∈ ℝ^{m×n}, there exist orthonormal matrices U ∈ ℝ^{m×m}, V ∈ ℝ^{n×n}, and a diagonal (rectangular) matrix Σ ∈ ℝ^{m×n} with nonnegative diagonal entries σ₁ ≥ σ₂ ≥ … ≥ 0 such that A = UΣVᵀ. Geometrically: Vᵀ rotates the input, Σ scales along orthogonal axes, U rotates the output. The σᵢ are singular values; columns of V are right singular vectors; columns of U are left singular vectors. SVD underlies best low-rank approximation and PCA.

## What Is Singular Value Decomposition?

### Why we need something beyond eigenvalues

Eigenvalues and eigenvectors answer: “Are there directions **v** that A maps onto themselves up to scaling?”

- •For a square matrix A ∈ ℝ^{n×n}, we look for **v** ≠ **0** such that A**v** = λ**v**.
- •This is powerful, but it has limitations:
- •Many matrices are not diagonalizable over ℝ.
- •Many problems involve rectangular matrices (m×n), where eigenvalues are not even defined in the usual sense.
- •Even when eigenvectors exist, they may not be orthogonal, which makes geometric and numerical reasoning harder.

SVD fixes these issues by giving an orthonormal coordinate system in the input and output spaces.

### Definition

For any real matrix A ∈ ℝ^{m×n}, the **Singular Value Decomposition** is

A = UΣVᵀ

where:

- •U ∈ ℝ^{m×m} is **orthonormal** (UᵀU = Iₘ)
- •V ∈ ℝ^{n×n} is **orthonormal** (VᵀV = Iₙ)
- •Σ ∈ ℝ^{m×n} is **diagonal (rectangular)**:
- •Σ\_{ii} = σᵢ ≥ 0 (singular values)
- •all off-diagonal entries are 0
- •typically ordered σ₁ ≥ σ₂ ≥ … ≥ σ\_r > 0, where r = rank(A)

Concretely, Σ looks like

Σ = [ diag(σ₁,…,σ\_r) 0 ]

[ 0 0 ]

with the diagonal sitting in the top-left.

### The “three-step” story

SVD says A can be viewed as three simple transformations composed:

1) **Vᵀ**: rotate/reflect input space (ℝⁿ) into a special orthonormal basis (the right singular vectors)

2) **Σ**: scale along coordinate axes by nonnegative factors σᵢ

3) **U**: rotate/reflect output space (ℝᵐ) into the standard basis

Because U and V are orthonormal, they preserve lengths and angles:

‖Vᵀ**x**‖ = ‖**x**‖, ‖U**y**‖ = ‖**y**‖.

So all stretching/squashing is completely captured by Σ.

### Geometric intuition: sphere → ellipsoid

Consider the unit sphere in ℝⁿ:

S = { **x** ∈ ℝⁿ : ‖**x**‖ = 1 }.

Under A, the set A(S) is generally an ellipsoid (possibly flattened into lower dimensions). SVD explains why:

- •Vᵀ rotates the sphere (still a sphere)
- •Σ scales orthogonal axes by σᵢ (sphere becomes axis-aligned ellipsoid)
- •U rotates the ellipsoid in ℝᵐ

The singular values σᵢ are the lengths of the ellipsoid’s semi-axes.

### The cast of characters

Let V = [**v**₁ … **v**ₙ] and U = [**u**₁ … **u**ₘ]. Then:

- •**Right singular vectors**: columns **v**ᵢ of V
- •**Left singular vectors**: columns **u**ᵢ of U
- •Singular values: σᵢ (diagonal entries of Σ)

And the defining relationships are:

A**v**ᵢ = σᵢ **u**ᵢ

Aᵀ**u**ᵢ = σᵢ **v**ᵢ

These say: A maps orthonormal directions **v**ᵢ to orthonormal directions **u**ᵢ, scaled by σᵢ.

### Existence (why you can trust it)

A key promise of SVD: **every real matrix has an SVD**.

This is not just a convenience—it is the reason SVD becomes a universal tool in numerical linear algebra, data analysis, and machine learning.

A common route to existence uses the fact that AᵀA is symmetric positive semidefinite, hence has an orthonormal eigenbasis. From that eigenbasis we build V and Σ, then define U accordingly. We’ll do this carefully in the next section.

## Core Mechanic 1: Constructing SVD from AᵀA (and What Singular Values Really Are)

### Why start with AᵀA?

We want orthonormal directions in the input space that A treats “nicely.” AᵀA is the right object because:

- •AᵀA is always n×n (square), even if A is rectangular.
- •AᵀA is symmetric: (AᵀA)ᵀ = AᵀA.
- •AᵀA is positive semidefinite:

**x**ᵀ(AᵀA)**x** = (A**x**)ᵀ(A**x**) = ‖A**x**‖² ≥ 0.

So AᵀA has real eigenvalues and orthonormal eigenvectors.

### Step 1: Eigen-decompose AᵀA

Because AᵀA is symmetric, there exists an orthonormal matrix V and diagonal Λ such that:

AᵀA = VΛVᵀ

where Λ = diag(λ₁,…,λₙ) with λᵢ ≥ 0.

Let the eigenpairs be:

(AᵀA)**v**ᵢ = λᵢ **v**ᵢ

with ‖**v**ᵢ‖ = 1 and **v**ᵢ ⟂ **v**ⱼ for i ≠ j.

### Step 2: Define singular values

Singular values are defined as

σᵢ = √λᵢ (nonnegative)

and arranged in decreasing order σ₁ ≥ σ₂ ≥ … ≥ 0.

So singular values are literally the square-roots of eigenvalues of AᵀA.

### Step 3: Define left singular vectors

For any λᵢ > 0 (equivalently σᵢ > 0), define

**u**ᵢ = (1/σᵢ) A**v**ᵢ.

Then **u**ᵢ is a unit vector, and distinct **u**ᵢ are orthogonal. Let’s show the unit-length claim carefully.

Compute ‖**u**ᵢ‖²:

‖**u**ᵢ‖² = **u**ᵢᵀ**u**ᵢ

= ((1/σᵢ)A**v**ᵢ)ᵀ ((1/σᵢ)A**v**ᵢ)

= (1/σᵢ²) **v**ᵢᵀ AᵀA **v**ᵢ

= (1/σᵢ²) **v**ᵢᵀ (λᵢ **v**ᵢ)

= (1/σᵢ²) λᵢ (**v**ᵢᵀ**v**ᵢ)

= (1/σᵢ²) λᵢ

= (1/(√λᵢ)²) λᵢ

= 1.

So ‖**u**ᵢ‖ = 1.

Now check orthogonality for i ≠ j (assuming σᵢ,σⱼ > 0):

**u**ᵢᵀ**u**ⱼ

= ((1/σᵢ)A**v**ᵢ)ᵀ ((1/σⱼ)A**v**ⱼ)

= (1/(σᵢσⱼ)) **v**ᵢᵀ AᵀA **v**ⱼ

= (1/(σᵢσⱼ)) **v**ᵢᵀ (λⱼ **v**ⱼ)

= (λⱼ/(σᵢσⱼ)) **v**ᵢᵀ**v**ⱼ

= 0.

Thus {**u**ᵢ} are orthonormal over the nonzero singular values.

For the remaining columns of U (if m > r), we choose any orthonormal vectors that complete a basis of ℝᵐ. This completion is not unique.

### Step 4: Assemble Σ, U, V

Let r = rank(A) = number of positive singular values.

- •Put σ₁,…,σ\_r on the diagonal of Σ.
- •Let V contain the eigenvectors **v**ᵢ of AᵀA.
- •Let U contain **u**ᵢ = A**v**ᵢ/σᵢ for i ≤ r, plus any orthonormal completion.

Then we can show A = UΣVᵀ.

One clean way is to check what A does to each **v**ᵢ:

A**v**ᵢ = σᵢ **u**ᵢ.

Now consider the matrix UΣVᵀ applied to **v**ᵢ:

(UΣVᵀ)**v**ᵢ

= UΣ (Vᵀ**v**ᵢ)

= UΣ **e**ᵢ

= U (σᵢ **e**ᵢ)

= σᵢ **u**ᵢ.

So A and UΣVᵀ agree on the basis vectors **v**ᵢ, hence they are the same linear map.

### What singular values mean: operator norm and energy

The largest singular value σ₁ tells you the maximum stretching factor of A:

σ₁ = max\_{‖**x**‖=1} ‖A**x**‖.

You can see this from

‖A**x**‖² = **x**ᵀAᵀA**x**.

For symmetric matrices, the maximum of **x**ᵀM**x** over ‖**x**‖=1 is the largest eigenvalue. Here M = AᵀA, so the maximum is λ₁, and thus max ‖A**x**‖ = √λ₁ = σ₁.

More generally, the sum of squared singular values equals the squared Frobenius norm:

‖A‖\_F² = ∑\_{i=1}^{r} σᵢ².

This becomes useful for measuring how much “energy” is captured by keeping only the top k singular values.

### Relationship to eigenvalues (what carries over, what doesn’t)

If A is symmetric positive semidefinite, then its eigen-decomposition A = QΛQᵀ looks SVD-like.

In that case:

- •U = V = Q
- •Σ = Λ (with nonnegative eigenvalues)

But in general:

- •Eigenvalues of A can be negative or complex.
- •Singular values of A are always real and nonnegative.
- •SVD always exists over ℝ.

This is why SVD is the robust “geometric backbone” behind many algorithms.

## Core Mechanic 2: Geometry, Rank, and the Outer-Product (Sum of Rank-1) View

### Why a rank-1 sum matters

Matrices can be complicated globally, but rank-1 matrices are simple:

- •A rank-1 matrix has the form **a****b**ᵀ.
- •It maps any **x** to **a**(**b**ᵀ**x**):
- •first take a dot product with **b** (a scalar)
- •then scale **a** by that scalar

So if we can write A as a sum of rank-1 pieces, we get an interpretable and computable structure.

SVD gives exactly that.

### The outer-product expansion of SVD

Write the (thin) SVD using r = rank(A):

A = U\_r Σ\_r V\_rᵀ

where:

- •U\_r ∈ ℝ^{m×r} has columns **u**₁,…,**u**\_r
- •V\_r ∈ ℝ^{n×r} has columns **v**₁,…,**v**\_r
- •Σ\_r = diag(σ₁,…,σ\_r)

Then:

A = ∑\_{i=1}^{r} σᵢ **u**ᵢ **v**ᵢᵀ.

This is worth pausing on:

- •Each term σᵢ **u**ᵢ **v**ᵢᵀ is rank 1.
- •The singular values act like weights.
- •The left/right singular vectors give orthonormal directions on output/input sides.

### Derivation (showing the work)

Start from thin SVD:

A = U\_r Σ\_r V\_rᵀ.

Let Σ\_r have diagonal entries σᵢ. We can write Σ\_r as a sum of diagonal basis matrices:

Σ\_r = ∑\_{i=1}^{r} σᵢ (**e**ᵢ **e**ᵢᵀ).

Then

A = U\_r (∑\_{i=1}^{r} σᵢ **e**ᵢ **e**ᵢᵀ) V\_rᵀ

= ∑\_{i=1}^{r} σᵢ (U\_r **e**ᵢ) (V\_r **e**ᵢ)ᵀ

= ∑\_{i=1}^{r} σᵢ **u**ᵢ **v**ᵢᵀ.

That’s the outer-product form.

### Geometry: orthogonal directions map to orthogonal directions

The defining relation A**v**ᵢ = σᵢ **u**ᵢ means:

- •The input direction **v**ᵢ (unit length) maps to the output direction **u**ᵢ (unit length)
- •The length is scaled by σᵢ

If you take an arbitrary input vector **x** and express it in the V-basis:

**x** = ∑\_{i=1}^{n} αᵢ **v**ᵢ

where αᵢ = **v**ᵢᵀ**x**.

Then

A**x**

= A(∑\_{i} αᵢ **v**ᵢ)

= ∑\_{i} αᵢ A**v**ᵢ

= ∑\_{i} αᵢ σᵢ **u**ᵢ.

So the components along **v**ᵢ get scaled by σᵢ and re-expressed along **u**ᵢ.

This is the ellipsoid story in coordinates.

### Rank and null spaces through Σ

Because Σ has σ₁,…,σ\_r > 0 and the rest 0:

- •rank(A) = r
- •dim(null(A)) = n − r
- •dim(null(Aᵀ)) = m − r

The right singular vectors associated with σᵢ = 0 span null(A):

If σᵢ = 0, then A**v**ᵢ = 0.

Similarly, left singular vectors with σᵢ = 0 span null(Aᵀ).

This makes SVD a “coordinate system” where the fundamental subspaces (row space, column space, null space) become clean blocks.

### Full SVD vs thin SVD (practical distinction)

You will see two common SVD shapes:

| Name | Factorization | Shapes | When used |
| --- | --- | --- | --- |
| Full SVD | A = UΣVᵀ | U: m×m, Σ: m×n, V: n×n | Theory, explicit bases for all spaces |
| Thin/compact SVD | A = U\_r Σ\_r V\_rᵀ | U\_r: m×r, Σ\_r: r×r, V\_r: n×r | Computation, low-rank approximation |

The thin SVD discards the “zero singular value” directions and keeps only what A actually uses.

### Best rank-k approximation (why SVD dominates compression)

A remarkable theorem (Eckart–Young–Mirsky) says:

If you want a rank-k matrix B that best approximates A, then truncating the SVD is optimal.

Define

A\_k = ∑\_{i=1}^{k} σᵢ **u**ᵢ **v**ᵢᵀ.

Then A\_k solves:

min\_{rank(B)=k} ‖A − B‖\_F

and also

min\_{rank(B)=k} ‖A − B‖₂.

Intuition:

- •The first singular directions capture the largest stretches (largest “energy”).
- •Any rank-k matrix can only capture k independent input-output directions.
- •SVD orders directions from most to least influential.

Quantitatively, the truncation error is clean:

‖A − A\_k‖\_F² = ∑\_{i=k+1}^{r} σᵢ²

‖A − A\_k‖₂ = σ\_{k+1}.

These formulas are incredibly useful in practice: they tell you exactly what you lose by compressing.

## Application/Connection: PCA, Least Squares, and Why SVD Is a Workhorse

### PCA connection (what SVD unlocks)

Principal Component Analysis (PCA) finds directions of maximal variance in data.

Suppose you have a centered data matrix X ∈ ℝ^{N×d}:

- •rows are data points
- •columns are features
- •“centered” means each feature has mean 0

The sample covariance is

C = (1/(N−1)) XᵀX.

PCA traditionally says: compute eigenvectors of C.

Now notice:

- •XᵀX is exactly the AᵀA object from SVD.
- •If X = UΣVᵀ, then

XᵀX = VΣᵀUᵀUΣVᵀ = V(ΣᵀΣ)Vᵀ.

Since UᵀU = I, we get an eigen-decomposition:

C = (1/(N−1)) V(ΣᵀΣ)Vᵀ.

So:

- •PCA directions (principal axes) are the right singular vectors **v**ᵢ of X
- •PCA variances are (σᵢ²/(N−1))

This is why numerical PCA is often implemented via SVD of X directly.

### Least squares and the pseudoinverse

Given an overdetermined system A**x** ≈ **b** (m > n), the least squares solution minimizes

min\_{**x**} ‖A**x** − **b**‖².

SVD provides a stable way to solve it using the Moore–Penrose pseudoinverse A⁺.

If A = UΣVᵀ, then

A⁺ = V Σ⁺ Uᵀ

where Σ⁺ is formed by inverting nonzero singular values:

Σ⁺\_{ii} = 1/σᵢ for i ≤ r, and 0 otherwise.

Then one least-squares solution is

**x̂** = A⁺ **b**.

Why this is good:

- •Small singular values correspond to directions where A barely changes the output.
- •Inverting tiny σᵢ can amplify noise (ill-conditioning).
- •SVD exposes this explicitly, enabling regularization (e.g., truncated SVD or ridge regression).

### Conditioning and numerical stability

The condition number (in 2-norm) of a full-rank matrix is

κ₂(A) = σ₁ / σ\_n

(or σ₁/σ\_r if rank-deficient).

Interpretation:

- •If κ₂(A) is large, A squashes some directions much more than others.
- •Solving A**x** = **b** becomes sensitive to noise.

SVD makes this sensitivity visible and measurable.

### A practical mental model

When you see A = UΣVᵀ, think:

- •V gives “input axes that matter”
- •Σ tells you “how much each axis matters”
- •U tells you “where those axes land in output space”

And when you truncate at k:

A ≈ A\_k = U\_k Σ\_k V\_kᵀ

you are choosing to keep only the k most influential input-output modes.

### Where SVD appears (a few common places)

- •**PCA / dimensionality reduction**: compress features while preserving variance
- •**Recommender systems**: matrix factorization (low-rank structure)
- •**Compression**: images, embeddings, model weights
- •**Signal processing**: denoising via truncation
- •**Machine learning**: analyzing linear layers, conditioning, and rank

SVD is not just a theorem—it is a lens for understanding what a matrix does, and a toolkit for acting on that understanding.

## Worked Examples (3)

### Compute an SVD of a simple diagonal matrix (and see the geometry)

Let A = [[3, 0], [0, 1]]. Find an SVD and interpret σ₁, σ₂ geometrically.

1. Recognize A is already diagonal with nonnegative diagonal entries.

   We suspect V = I and U = I might work.
2. Compute AᵀA:

   AᵀA = A² = [[9, 0], [0, 1]].
3. Find eigenvalues/eigenvectors of AᵀA.

   Eigenvalues: λ₁ = 9, λ₂ = 1.

   Eigenvectors are the standard basis:

   **v**₁ = [1,0]ᵀ, **v**₂ = [0,1]ᵀ.

   Thus V = I.
4. Convert eigenvalues to singular values:

   σ₁ = √9 = 3

   σ₂ = √1 = 1

   So Σ = [[3,0],[0,1]].
5. Compute left singular vectors:

   **u**ᵢ = (1/σᵢ)A**v**ᵢ.

   For i=1:

   A**v**₁ = [3,0]ᵀ ⇒ **u**₁ = (1/3)[3,0]ᵀ = [1,0]ᵀ.

   For i=2:

   A**v**₂ = [0,1]ᵀ ⇒ **u**₂ = (1/1)[0,1]ᵀ = [0,1]ᵀ.

   Thus U = I.
6. Verify:

   UΣVᵀ = I · Σ · I = A.

**Insight:** This matrix scales the x-axis by 3 and the y-axis by 1. The unit circle maps to an axis-aligned ellipse with semi-axes 3 and 1. SVD reduces to “rotate (none), scale, rotate (none)”—a clean case that matches the general geometric story.

### SVD of a rank-1 matrix via AᵀA

Let A = [[1, 1], [1, 1]]. Compute its singular values and one valid SVD.

1. Compute AᵀA:

   AᵀA = [[1,1],[1,1]]ᵀ[[1,1],[1,1]] = [[2,2],[2,2]].
2. Find eigenvalues of AᵀA.

   Matrix [[2,2],[2,2]] has:

   - •eigenvector **v**₁ ∥ [1,1]ᵀ with eigenvalue λ₁ = 4
   - •eigenvector **v**₂ ∥ [1,−1]ᵀ with eigenvalue λ₂ = 0

   Normalize:

   **v**₁ = (1/√2)[1,1]ᵀ

   **v**₂ = (1/√2)[1,−1]ᵀ

   Set V = [**v**₁ **v**₂].
3. Singular values:

   σ₁ = √λ₁ = 2

   σ₂ = √λ₂ = 0

   So rank r = 1.
4. Compute **u**₁ = (1/σ₁)A**v**₁:

   A**v**₁ = [[1,1],[1,1]] (1/√2)[1,1]ᵀ

   = (1/√2)[2,2]ᵀ

   = √2 [1,1]ᵀ

   Thus **u**₁ = (1/2) √2 [1,1]ᵀ = (1/√2)[1,1]ᵀ.
5. Complete U to an orthonormal basis.

   Choose **u**₂ = (1/√2)[1,−1]ᵀ.

   Then U = [**u**₁ **u**₂] is orthonormal.
6. Assemble Σ = [[2,0],[0,0]].

   Then A = UΣVᵀ holds (one valid SVD).

**Insight:** A has rank 1: it only acts nontrivially along the direction **v**₁ = (1/√2)[1,1]. Everything orthogonal to that direction is sent to 0 (σ₂ = 0). The unit circle is squashed into a line segment (a degenerate ellipsoid).

### Best rank-1 approximation error from singular values

Suppose A has singular values σ₁ = 10, σ₂ = 3, σ₃ = 1 (and no others). Compute ‖A − A₁‖\_F and ‖A − A₁‖₂.

1. Recall truncation errors:

   ‖A − A\_k‖\_F² = ∑\_{i=k+1}^{r} σᵢ²

   ‖A − A\_k‖₂ = σ\_{k+1}.
2. Here r = 3 and k = 1.

   So:

   ‖A − A₁‖\_F² = σ₂² + σ₃² = 3² + 1² = 9 + 1 = 10.
3. Therefore:

   ‖A − A₁‖\_F = √10.
4. Spectral norm error:

   ‖A − A₁‖₂ = σ₂ = 3.

**Insight:** SVD doesn’t just give a method—it gives exact guarantees. The leftover singular values quantify precisely what information you discard when compressing.

## Key Takeaways

- ✓

  SVD factorizes any real matrix A ∈ ℝ^{m×n} as A = UΣVᵀ with U, V orthonormal and Σ diagonal with nonnegative entries.
- ✓

  Geometrically: Vᵀ rotates/reflects the input, Σ scales along orthogonal axes (σᵢ), and U rotates/reflects the output; the unit sphere maps to an ellipsoid.
- ✓

  Singular values satisfy σᵢ = √λᵢ where λᵢ are eigenvalues of AᵀA (or AAᵀ).
- ✓

  Right singular vectors (**v**ᵢ) are eigenvectors of AᵀA; left singular vectors (**u**ᵢ) are eigenvectors of AAᵀ.
- ✓

  The relationships A**v**ᵢ = σᵢ**u**ᵢ and Aᵀ**u**ᵢ = σᵢ**v**ᵢ encode how A acts on special orthonormal directions.
- ✓

  SVD gives an outer-product expansion: A = ∑ σᵢ **u**ᵢ **v**ᵢᵀ, a sum of rank-1 components.
- ✓

  Truncating the SVD yields the best rank-k approximation: A\_k = ∑\_{i=1}^{k} σᵢ **u**ᵢ **v**ᵢᵀ, with clean error formulas.
- ✓

  PCA is closely connected: for centered data X, the principal directions are right singular vectors of X, and variances are proportional to σᵢ².

## Common Mistakes

- ✗

  Confusing eigenvalues with singular values: eigenvalues can be negative/complex; singular values are always real and ≥ 0, derived from AᵀA.
- ✗

  Assuming U = V always: that holds for special cases (e.g., symmetric positive semidefinite), but not for general matrices.
- ✗

  Forgetting the rectangular shape of Σ in the full SVD: Σ is m×n, not necessarily square; only its diagonal entries matter.
- ✗

  Thinking the SVD is unique: singular vectors are not unique when singular values repeat, and sign flips (**u**ᵢ, **v**ᵢ) → (−**u**ᵢ, −**v**ᵢ) leave A unchanged.

## Practice

medium

Let A ∈ ℝ^{m×n} have SVD A = UΣVᵀ. Show that ‖A**x**‖ ≤ σ₁‖**x**‖ for all **x** ∈ ℝⁿ.

**Hint:** Write **x** = V**z** with **z** = Vᵀ**x**. Use orthonormality to relate ‖**z**‖ and ‖**x**‖, then bound ‖Σ**z**‖ by σ₁‖**z**‖.

Show solution

Let **z** = Vᵀ**x**, so **x** = V**z** and ‖**z**‖ = ‖**x**‖ since V is orthonormal.

Then:

A**x** = UΣVᵀ**x** = UΣ**z**.

Taking norms and using orthonormality of U:

‖A**x**‖ = ‖UΣ**z**‖ = ‖Σ**z**‖.

Since Σ scales coordinates by at most σ₁,

‖Σ**z**‖² = ∑ σᵢ² zᵢ² ≤ σ₁² ∑ zᵢ² = σ₁²‖**z**‖².

Thus ‖A**x**‖ ≤ σ₁‖**z**‖ = σ₁‖**x**‖.

easy

Compute the singular values of A = [[2, 0], [0, −1]] and give one valid SVD.

**Hint:** Compute AᵀA and take square-roots of its eigenvalues. Remember singular values are nonnegative; signs can be absorbed into U or V.

Show solution

AᵀA = [[4,0],[0,1]]. Its eigenvalues are 4 and 1, so singular values are σ₁=2, σ₂=1.

One SVD: take V = I, Σ = [[2,0],[0,1]].

We need U such that UΣ = A. Since A differs by a sign on the second axis, choose U = diag(1, −1).

Then UΣVᵀ = diag(1,−1) diag(2,1) I = diag(2, −1) = A.

medium

Suppose A has singular values 5, 2, 2, 0. What are rank(A), dim(null(A)), and the best rank-2 Frobenius error ‖A − A₂‖\_F?

**Hint:** Rank is the number of positive singular values. Use ‖A − A\_k‖\_F² = ∑\_{i>k} σᵢ².

Show solution

Positive singular values: 5,2,2 → rank(A)=3.

If A is m×n, then dim(null(A)) = n − rank(A) = n − 3.

For k=2:

‖A − A₂‖\_F² = σ₃² + σ₄² = 2² + 0² = 4.

So ‖A − A₂‖\_F = 2.

## Connections

[Eigenvalues and Eigenvectors](/tech-tree/eigen/)

[Orthogonality](/tech-tree/orthogonality/)

[Principal Component Analysis](/tech-tree/pca/)

Quality: A (4.3/5)

[← back to tree](/tech-tree/)[browse all →](/tech-tree/inventory/)
