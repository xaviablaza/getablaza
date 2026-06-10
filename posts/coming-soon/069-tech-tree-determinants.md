---
title: Determinants
description: Scalar value from square matrix. Zero iff singular.
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
permalink: /tech-tree/determinants/
---

[←Back to Tech Tree](/tech-tree/)

[inventory](/tech-tree/inventory/)[coverage](/tech-tree/coverage/)

# Determinants

Linear AlgebraDifficulty: ★★★☆☆Depth: 3Unlocks: 19

Scalar value from square matrix. Zero iff singular.

## Interactive Visualization

⏮◀◀▶▶STEP0.25x1xZOOM

t=0s

## Core Concepts

- -Determinant is a scalar-valued function assigned to every square matrix
- -The determinant is multilinear in the rows (or columns) and alternating (swapping two rows changes sign)
- -determinant equals zero exactly when the matrix is singular (non-invertible)

## Key Symbols & Notation

det(A) - the determinant operator applied to matrix A

## Essential Relationships

- -Multiplicativity: det(AB) = det(A) \* det(B) for square matrices A and B
- -Predictable effect of elementary row operations on det: row-swap flips sign; scaling a row multiplies det by that scalar; adding a multiple of one row to another leaves det unchanged

## Prerequisites (1)

[Matrix Operations6 atoms](/tech-tree/matrix-operations/)

## Unlocks (2)

[Eigenvalues and Eigenvectorslvl 3](/tech-tree/eigenvalues/)[Matrix Decompositionlvl 3](/tech-tree/matrix-decomposition/)

Advanced Learning Details

### Graph Position

24

Depth Cost

19

Fan-Out (ROI)

8

Bottleneck Score

3

Chain Length

### Cognitive Load

6

Atomic Elements

41

Total Elements

L3

Percentile Level

L4

Atomic Level

### All Concepts (12)

- - Determinant: a scalar-valued function defined on square (n×n) matrices
- - Determinant as a criterion for invertibility: matrix is invertible iff its determinant is nonzero (zero iff singular)
- - Determinant as the signed n-volume scaling factor of the associated linear transformation
- - Orientation/sign of a linear map indicated by the determinant (positive preserves orientation, negative reverses it)
- - Explicit 2×2 determinant formula det([[a,b],[c,d]]) = ad − bc as the simplest case
- - Computation by cofactor (Laplace) expansion along a row or column
- - Computation by the permutation (Leibniz) formula summing over S\_n with permutation signs
- - Determinant of a triangular (or diagonal) matrix equals the product of its diagonal entries
- - Effect of elementary row operations on the determinant (row swap, row scaling, row addition)
- - Adjugate (adj(A)) and its role in expressing the inverse via the determinant
- - Determinant as an alternating multilinear function of the rows (or columns)
- - Relationship between determinant and eigenvalues: determinant equals the product of eigenvalues (with algebraic multiplicity)

### Teaching Strategy

Deep-dive lesson - accessible entry point but dense material. Use worked examples and spaced repetition.

A square matrix doesn’t just move vectors around—it can stretch space, flip orientation, or collapse an entire dimension. The determinant is the single number that summarizes all of that.

TL;DR:

det(A) is a scalar attached to a square matrix A that measures signed volume scaling. It is 0 exactly when A collapses space (is singular). It is multiplicative: det(AB) = det(A)det(B), and changes predictably under row operations.

## What Is Determinants?

### Why we care (before the formula)

When you treat a matrix A as a linear transformation, it takes shapes in ℝⁿ and maps them somewhere else. A crucial question is:

- •Does A **preserve dimension** (so the map is invertible), or does it **collapse** some directions (so information is lost)?
- •How much does A **scale area/volume**?
- •Does A **flip orientation** (like a mirror reflection)?

The determinant packages these geometric behaviors into a single scalar.

### Definition (intuition first)

For an n×n matrix A, the determinant det(A) is a real number with three core behaviors (these can be taken as axioms that uniquely characterize it):

1) **Multilinear in rows (or columns)**

- •If you fix all rows except one, det is linear in that row.
- •“Linear” here means scaling and addition distribute.

2) **Alternating**

- •If you swap two rows, the determinant changes sign.
- •If two rows are equal (or one is a multiple of another), det(A) = 0.

3) **Normalization**

- •det(I) = 1 for the identity matrix I.

These properties are not random: they are exactly what you’d want from a “signed volume scaling factor.”

### Geometric meaning: signed volume scaling

Interpret A as acting on vectors in ℝⁿ. Consider the unit square (in 2D) or unit cube (in 3D), or in general the unit n-dimensional parallelepiped.

- •|det(A)| tells you how the n-dimensional volume scales.
- •If |det(A)| = 3, volumes become 3× larger.
- •If |det(A)| = 1/2, volumes shrink by factor 1/2.
- •sign(det(A)) tells you whether orientation is preserved or reversed.
- •det(A) < 0 means there is a flip (like a reflection composed with some stretching).

### The key singularity test

A matrix A is **singular** (non-invertible) exactly when det(A) = 0.

Intuition: if A collapses at least one dimension, the n-dimensional volume must collapse to 0.

Formally we’ll connect this to row dependence:

- •det(A) = 0 ⇔ rows (or columns) are linearly dependent ⇔ A is not invertible.

### Small concrete example (2×2)

For A = [[a, b], [c, d]],

det(A) = ad − bc.

This number is the signed area scaling factor in 2D.

- •If A = [[2, 0], [0, 3]], then det(A) = 6: it stretches x by 2 and y by 3, so areas scale by 2·3.
- •If A = [[1, 0], [0, −1]], then det(A) = −1: it reflects across the x-axis; area magnitude preserved, orientation flipped.

Takeaway: determinants are not merely a computational trick—they are the algebraic encoding of how linear maps scale and orient space.

## Core mechanic 1: How determinants respond to row operations

### Why row operations matter

In practice, you often compute determinants by simplifying a matrix via row operations (the same moves used in Gaussian elimination). The determinant is designed to react predictably to these moves.

This gives you a powerful workflow:

1) Reduce A to an upper triangular form U.

2) Adjust for the row operations you used.

3) Use det(U) = product of diagonal entries.

### The three fundamental row operations

Below is the rule set you should memorize—because it turns determinant computation into bookkeeping.

| Row operation on A | Effect on det(A) | Why (intuition) |
| --- | --- | --- |
| Swap two rows | det changes sign | Alternating: swapping flips orientation |
| Multiply a row by k | det multiplies by k | Multilinear: scaling one row scales volume |
| Add k·(row i) to row j | det unchanged | Shear: doesn’t change volume |

A subtle but important note: “Add a multiple of one row to another” keeps determinant unchanged, but it can drastically change entries—this is the move that makes elimination so useful.

### Triangular matrices: the determinant shortcut

For an upper triangular matrix U (everything below diagonal is 0),

det(U) = ∏ᵢ uᵢᵢ.

Same for lower triangular.

Why this is true (idea): a triangular matrix maps basis vectors in a way that stacks scaling along diagonal directions without mixing that creates additional volume contributions.

### Worked derivation idea (with multilinearity and alternating)

To see why some rules make sense, consider two quick consequences of the axioms:

**(1) If two rows are equal, det = 0**

Swap the two equal rows:

- •By alternating: det(A) becomes −det(A)
- •But the matrix is unchanged (rows equal)

So:

det(A) = −det(A)

⇒ 2 det(A) = 0

⇒ det(A) = 0.

**(2) Adding a multiple of one row to another doesn’t change det**

Let rows be r₁, …, rⱼ, …, rᵢ, …, rₙ. Replace rⱼ with rⱼ + k rᵢ.

By multilinearity in row j:

det(r₁,…, rⱼ + k rᵢ, …, rₙ)

= det(r₁,…, rⱼ, …, rₙ) + k det(r₁,…, rᵢ, …, rₙ)

But the second determinant has rᵢ appearing twice (once as row i and once in row j’s slot). Two equal rows ⇒ determinant 0. Hence:

det(new) = det(old) + k·0 = det(old).

This is the algebraic reason elimination works so cleanly.

### Computing det(A) via elimination (the safe version)

A common reliable method:

- •Use only row-addition operations (don’t change determinant).
- •If you must swap rows, track a sign flip.
- •If you scale a row, track the scaling factor.

At the end, you reach triangular U, then use product of diagonal.

### The determinant and invertibility (connection to elimination)

Gaussian elimination tells you:

- •A is invertible ⇔ you can reduce it to I without ever creating a zero pivot.
- •A is singular ⇔ you hit a zero pivot (a row becomes dependent).

Determinant encodes this in one number:

- •det(A) = 0 ⇔ some elimination step forces a zero pivot (after appropriate swaps) ⇔ rank < n.

So: elimination gives you a *procedural* test; determinant gives you a *scalar certificate*.

## Core mechanic 2: Determinant formulas (2×2, 3×3, and cofactor expansion)

### Why formulas exist at all

The axioms define det(A), but to compute it directly from entries, we need formulas.

For 2×2 and 3×3, explicit closed forms are convenient. For larger n, direct formulas exist (cofactor expansion / Leibniz formula), but computationally they become expensive; elimination is typically preferred.

### 2×2 formula

For A = [[a, b], [c, d]]:

det(A) = ad − bc.

Geometric sanity checks:

- •If rows are multiples (e.g., [a, b] = t[c, d]), then ad − bc = 0.
- •If A is diagonal diag(α, β), det(A) = αβ.

### 3×3 formula (cofactor expansion along a row)

Let

A =

[ [a, b, c],

[d, e, f],

[g, h, i] ].

One common expression is:

det(A) = a(ei − fh) − b(di − fg) + c(dh − eg).

Notice the alternating + − + pattern, which comes from the “alternating” nature of det.

### Cofactors and minors (the general pattern)

To expand det(A) along row r (or column c), you use **minors** and **cofactors**.

- •The minor Mᵣc is the (n−1)×(n−1) matrix you get by deleting row r and column c.
- •The cofactor Cᵣc is:

Cᵣc = (−1)^(r+c) det(Mᵣc).

Then **cofactor expansion** along row r is:

det(A) = ∑\_{c=1 to n} aᵣc Cᵣc.

Similarly, expansion along column c:

det(A) = ∑\_{r=1 to n} aᵣc Cᵣc.

### Why the sign pattern (−1)^(r+c)?

Swapping rows/columns changes sign. When you “move” an element aᵣc to the top-left conceptually, you perform (r−1) row swaps and (c−1) column swaps, totaling (r+c−2) swaps. Parity of swaps controls the sign, producing the checkerboard pattern.

### When cofactor expansion is useful

Cofactor expansion is rarely the fastest general method, but it shines when:

- •A row/column has many zeros (sparse).
- •You’re doing symbolic determinants (with variables) and want structure.

A practical rule:

- •If n ≥ 4 and the matrix isn’t very sparse, prefer elimination.

### Determinant as a sum over permutations (conceptual, not computational)

There is also the Leibniz formula:

det(A) = ∑\_{σ ∈ Sₙ} sgn(σ) ∏\_{i=1 to n} a\_{i, σ(i)}.

This makes the “alternating” behavior explicit: each permutation contributes with a sign depending on whether it’s an even or odd permutation.

Why mention it?

- •It explains why det is multilinear and alternating.
- •It connects determinants to combinatorics and to proofs like det(AB) = det(A)det(B).

But computing with it directly costs O(n!) terms—prohibitively large.

### Multiplicativity (a central property)

A major theorem:

det(AB) = det(A) det(B).

Interpretation:

- •Apply B: volumes scale by det(B).
- •Then apply A: volumes scale by det(A).
- •Net scaling is the product.

A powerful corollary:

- •A invertible ⇔ det(A) ≠ 0.

Because if A is invertible, AA⁻¹ = I.

Take determinants:

det(A) det(A⁻¹) = det(I) = 1

⇒ det(A) ≠ 0.

And conversely, if det(A) ≠ 0, A must be invertible (can be shown via elimination / rank).

### Determinant and transpose

Another helpful identity:

det(Aᵀ) = det(A).

So you can work with rows or columns interchangeably.

## Application/Connection: determinants in eigenvalues, decompositions, and geometry

### Determinants as a geometric “health check”

In applied linear algebra, det(A) answers fast questions:

- •**Near singular?** If det(A) is close to 0, the transformation nearly collapses volume, and solving A**x** = **b** may be ill-conditioned.
- •**Orientation flip?** If det(A) < 0, a handedness flip occurred.

Important nuance: “det close to 0” is not always a reliable numerical indicator of ill-conditioning by itself (scaling matters), but conceptually it’s a key signal.

### Connection to eigenvalues

If λ₁, …, λₙ are the eigenvalues of A (counted with algebraic multiplicity), then:

det(A) = ∏ᵢ λᵢ.

Why this matters:

- •If any eigenvalue is 0, the product is 0 ⇒ det(A) = 0 ⇒ A is singular.
- •The sign/magnitude of det relates to how eigenvalues scale space in their eigen-directions.

A related identity uses the characteristic polynomial:

p(λ) = det(A − λI).

Roots of p(λ) are eigenvalues. Determinants are literally the engine behind the eigenvalue equation.

### Connection to LU / QR decompositions

Many matrix decompositions expose the determinant cheaply.

**LU decomposition** (with possible permutation P):

PA = LU

where L is lower triangular with 1s on diagonal (often), and U is upper triangular.

Taking det:

det(PA) = det(L) det(U)

det(P) det(A) = det(L) det(U)

So:

det(A) = det(P)⁻¹ det(L) det(U).

Since det(L) is usually 1 (if L has unit diagonal), and det(U) is product of U’s diagonal entries, determinants become almost free once LU is computed.

**QR decomposition**:

A = QR

where Q is orthonormal (QᵀQ = I) and R is upper triangular.

Then:

det(A) = det(Q) det(R).

Key facts:

- •det(Q) is ±1 (orthonormal transforms preserve volume; they may flip orientation).
- •det(R) is product of diagonal entries.

### Determinant and change of variables (multivariable calculus)

If a differentiable map has Jacobian matrix J at a point, then |det(J)| gives the local volume scaling factor. This is why determinants appear in integrals under substitution.

Even if you haven’t studied Jacobians yet, keep the mental model:

- •determinant = local “volume magnifier” (signed).

### Determinants in solving systems (Cramer’s Rule)

There is a formula for solving A**x** = **b** using determinants:

xᵢ = det(Aᵢ) / det(A)

where Aᵢ is A with column i replaced by **b**.

This is elegant theoretically, but computationally inefficient for large systems. Still, it reinforces:

- •det(A) ≠ 0 is the condition for a unique solution.

### Big picture summary

Determinants sit at a crossroads:

- •Geometry (volume/orientation)
- •Algebra (invertibility, rank)
- •Computation (elimination, LU/QR)
- •Spectral theory (eigenvalues)

Once you can compute and reason about det(A), the next nodes—eigenvalues/eigenvectors and decompositions—feel much more motivated and connected.

## Worked Examples (3)

### Compute a determinant via elimination (tracking row operations)

Compute det(A) for A = [[2, 1, 0], [4, 3, 1], [−2, 0, 5]]. Use row operations to reach an upper triangular matrix.

1. Start with

   A =

   [ [ 2, 1, 0 ],

   [ 4, 3, 1 ],

   [ −2, 0, 5 ] ]
2. Use row-addition operations (do not change determinant):

   R₂ ← R₂ − 2R₁

   R₃ ← R₃ + R₁
3. Compute the new rows:

   R₂ = [4,3,1] − 2[2,1,0] = [0, 1, 1]

   R₃ = [−2,0,5] + [2,1,0] = [0, 1, 5]
4. Now the matrix is

   [ [2, 1, 0],

   [0, 1, 1],

   [0, 1, 5] ]
5. Eliminate below the pivot in column 2 using row-addition:

   R₃ ← R₃ − R₂
6. Compute:

   R₃ = [0,1,5] − [0,1,1] = [0,0,4]
7. Now we have an upper triangular matrix U:

   U =

   [ [2, 1, 0],

   [0, 1, 1],

   [0, 0, 4] ]
8. Since we used only row-addition operations, det(U) = det(A). For triangular matrices:

   det(U) = 2 · 1 · 4 = 8
9. Therefore det(A) = 8.

**Insight:** Row-addition operations preserve det, so elimination can compute det(A) with minimal bookkeeping. Once triangular, the determinant is just the product of the diagonal.

### Show singularity using determinant (linear dependence in rows)

Let B = [[1, 2, 3], [2, 4, 6], [0, 1, 1]]. Decide if B is invertible by computing det(B) efficiently.

1. Observe the first two rows:

   R₂ = 2R₁.

   This is immediate linear dependence.
2. Because the determinant is alternating and multilinear, if two rows are linearly dependent then det(B) = 0.

   (Reason: scaling one row scales det; if R₂ is a multiple of R₁ then the volume collapses.)
3. Conclude det(B) = 0 without further computation.
4. Therefore B is singular (non-invertible).

**Insight:** You often don’t need full computation: spotting dependent rows/columns gives det = 0 immediately, which is exactly the “collapse of volume” idea.

### Cofactor expansion on a sparse row

Compute det(C) for C = [[3, 0, 2], [0, 1, 0], [4, 0, 5]] using cofactor expansion.

1. Choose the second row for expansion because it has many zeros: [0, 1, 0].
2. Cofactor expansion along row 2:

   det(C) = ∑\_{c=1..3} c₂c C₂c

   Only the middle term survives because c₂1 = 0 and c₂3 = 0:

   det(C) = 1 · C₂2
3. Compute the cofactor:

   C₂2 = (−1)^(2+2) det(M₂2) = (+1) det(M₂2)
4. Form the minor M₂2 by deleting row 2 and column 2:

   M₂2 = [[3, 2], [4, 5]]
5. Compute its determinant:

   det(M₂2) = 3·5 − 2·4 = 15 − 8 = 7
6. Therefore det(C) = 7.

**Insight:** Cofactor expansion is best used strategically: pick a row/column with many zeros to reduce the amount of work.

## Key Takeaways

- ✓

  det(A) is a scalar for square matrices that measures **signed volume scaling** of the linear map **x** ↦ A**x**.
- ✓

  det(A) = 0 ⇔ A is singular ⇔ rows/columns are linearly dependent ⇔ the transformation collapses dimension.
- ✓

  Row operations have predictable effects: swap → sign flip, scale a row by k → det scales by k, add multiple of another row → det unchanged.
- ✓

  For triangular matrices, det is the product of diagonal entries: det(U) = ∏ᵢ uᵢᵢ.
- ✓

  Cofactor expansion computes det(A) via minors and the checkerboard sign (−1)^(r+c); it’s most useful for sparse matrices.
- ✓

  Multiplicativity det(AB) = det(A)det(B) matches the idea that volume scalings compose by multiplication.
- ✓

  det(Aᵀ) = det(A), so you may reason with rows or columns interchangeably.

## Common Mistakes

- ✗

  Forgetting determinant bookkeeping during elimination (especially row swaps, which multiply det by −1).
- ✗

  Using cofactor expansion on a dense 5×5 (or larger) matrix—this becomes computationally explosive compared to elimination/LU.
- ✗

  Thinking det(A) gives the exact condition number or stability; det near 0 suggests collapse, but numerical conditioning also depends on scaling and singular values.
- ✗

  Mixing up sign patterns in cofactor expansion: the (−1)^(r+c) checkerboard is easy to misapply.

## Practice

easy

Compute det(A) for A = [[1, 2], [5, 7]]. Interpret the sign.

**Hint:** Use det([[a,b],[c,d]]) = ad − bc.

Show solution

det(A) = 1·7 − 2·5 = 7 − 10 = −3. Magnitude 3 means areas scale by 3; negative sign means orientation flips.

medium

Compute det(B) for B = [[1, 1, 1], [2, 3, 4], [0, 1, 2]] using elimination (track any row swaps).

**Hint:** Use row-addition operations to make it upper triangular; then multiply the diagonal.

Show solution

Start

B = [[1,1,1],[2,3,4],[0,1,2]].

R₂ ← R₂ − 2R₁ gives R₂ = [0,1,2].

Now rows 2 and 3 are equal: R₂ = [0,1,2], R₃ = [0,1,2]. Two equal rows ⇒ det(B) = 0. So B is singular.

hard

Let A be invertible and 3×3. If det(A) = −2, compute det(5A) and det(A⁻¹).

**Hint:** Scaling: det(kA) = kⁿ det(A) for n×n. Inverse: det(A)det(A⁻¹) = 1.

Show solution

Since A is 3×3, det(5A) = 5³ det(A) = 125 · (−2) = −250. Also det(A⁻¹) = 1/det(A) = −1/2.

## Connections

Next steps:

- •[Eigenvalues and Eigenvectors](/tech-tree/eigenvalues/): eigenvalues satisfy det(A − λI) = 0, and det(A) = ∏ᵢ λᵢ.
- •[Matrix Decomposition](/tech-tree/matrix-decomposition/): LU/QR make det(A) cheap via triangular factors (product of diagonals).

Related reinforcement:

- •[Matrix Operations](/tech-tree/matrix-operations/): elimination and row operations underpin determinant computation.

Quality: A (4.4/5)

[← back to tree](/tech-tree/)[browse all →](/tech-tree/inventory/)
