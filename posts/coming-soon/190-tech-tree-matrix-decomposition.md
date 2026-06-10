---
title: Matrix Decomposition
description: LU, QR decomposition. Breaking matrices into factors.
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
permalink: /tech-tree/matrix-decomposition/
---

[←Back to Tech Tree](/tech-tree/)

[inventory](/tech-tree/inventory/)[coverage](/tech-tree/coverage/)

# Matrix Decomposition

Linear AlgebraDifficulty: ★★★☆☆Depth: 4Unlocks: 0

LU, QR decomposition. Breaking matrices into factors.

## Interactive Visualization

⏮◀◀▶▶STEP0.25x1xZOOM

t=0s

## Core Concepts

- -Matrix factorization: representing a matrix as a product of simpler factor matrices
- -LU decomposition: factorization into a lower-triangular (L) and an upper-triangular (U) factor
- -QR decomposition: factorization into an orthogonal/unitary (Q) factor and an upper-triangular (R) factor

## Key Symbols & Notation

L, U, Q, R, P - factor labels: L (lower-triangular), U (upper-triangular), Q (orthogonal/unitary), R (upper-triangular), P (permutation for pivoting)

## Essential Relationships

- -Equality relations: A = L \* U (or P \* A = L \* U with pivoting) and A = Q \* R with Q^T \* Q = I
- -Triangular-solve reduction: triangular factors convert solving A x = b into forward substitution and back substitution (QR gives R x = Q^T b for least-squares)

## Prerequisites (2)

[Systems of Linear Equations6 atoms](/tech-tree/linear-systems/)[Determinants6 atoms](/tech-tree/determinants/)

Advanced Learning Details

### Graph Position

46

Depth Cost

0

Fan-Out (ROI)

0

Bottleneck Score

4

Chain Length

### Cognitive Load

6

Atomic Elements

68

Total Elements

L4

Percentile Level

L4

Atomic Level

### All Concepts (29)

- - LU decomposition: factor a square matrix A into L (lower triangular) and U (upper triangular)
- - Lower-triangular factor L (often unit lower triangular with ones on the diagonal)
- - Upper-triangular factor U
- - Variations of LU algorithms (Doolittle, Crout - different conventions for L and U)
- - Row pivoting (partial pivoting) to avoid zero or small pivots
- - Complete (or full) pivoting
- - Permutation matrix P representing row (or column) permutations
- - Pivoted factorization identity: PA = LU (row permutations applied before factoring)
- - Conditions for existence of LU without pivoting (nonzero leading principal minors / nonzero pivots)
- - Forward substitution to solve Ly = b
- - Back substitution to solve Ux = y
- - Cholesky decomposition for symmetric positive-definite matrices: A = LL^T (or A = U^T U)
- - QR decomposition: factor A into Q (orthogonal/unitary) and R (upper triangular)
- - Orthogonal (real) or unitary (complex) matrices: Q^T Q = I (Q^\* Q = I)
- - Orthonormal columns/basis
- - Gram–Schmidt process (classical and modified) to build an orthonormal basis and produce Q and R
- - Householder reflections as a stable method to introduce zeros and build Q and R
- - Householder reflector vector and construction (reflector that zeros a subvector)
- - Givens rotations: plane rotations to zero individual elements
- - Thin / economy / reduced QR (Q has only orthonormal columns needed, R is smaller)
- - Rank-revealing QR and QR with column pivoting (A P = Q R) for detecting numerical rank
- - Least-squares solution via QR (use Q and R to solve minimization of ||Ax - b||)
- - Orthogonal transformations preserve Euclidean norm and inner product
- - Numerical stability properties: relative stability of LU with pivoting, instability of classical Gram–Schmidt, stability of Householder
- - Uniqueness and sign/phase ambiguity in QR (columns of Q and signs of R diagonals)
- - Using triangular factors to compute determinants efficiently (product of diagonal entries)
- - Treatment of rectangular matrices in factorizations (m×n with m≠n)
- - Rank-deficient cases: zero rows/columns in R or need for pivoting to reveal rank
- - Computational cost considerations (flop counts order-of-growth for LU and QR)

### Teaching Strategy

Deep-dive lesson - accessible entry point but dense material. Use worked examples and spaced repetition.

Matrix decomposition is the idea that a “complicated” matrix can often be rewritten as a product of “structured” matrices (triangular, orthogonal, permutation). That one rewrite turns many hard tasks—solving systems, computing determinants, least squares, and inverses—into sequences of easy steps.

TL;DR:

Matrix decomposition (factorization) rewrites A as a product like P A = L U or A = Q R. LU connects directly to Gaussian elimination for fast solves; QR uses orthogonality for numerical stability and least squares.

## What Is Matrix Decomposition?

### Why this concept exists (motivation)

In linear algebra, many problems repeatedly reduce to operations with the same matrix A:

- •Solve A **x** = **b** for many different right-hand sides **b**
- •Understand whether A is invertible (and how close it is to singular)
- •Compute determinants efficiently
- •Solve least squares when A is rectangular (overdetermined systems)

If you try to do each task “from scratch,” you typically re-run elimination steps or do expensive computations repeatedly. Matrix decomposition avoids that repetition by separating A into factors that are easier to work with.

### Definition (factorization)

A **matrix decomposition** (or factorization) is a representation

A = A₁ A₂ … Aₖ

where the factors Aᵢ have special structure (triangular, orthogonal, permutation, diagonal, etc.). The structure is the entire point: it turns expensive operations into cheap ones.

Two decompositions dominate introductory numerical linear algebra:

1) **LU decomposition** (with pivoting):

P A = L U

- •P is a **permutation matrix** (reorders rows)
- •L is **lower-triangular** (nonzero on and below the diagonal)
- •U is **upper-triangular** (nonzero on and above the diagonal)

2) **QR decomposition**:

A = Q R

- •Q is **orthogonal** (real case) or **unitary** (complex case): Qᵀ Q = I
- •R is **upper-triangular**

### Why triangular and orthogonal factors are “easy”

**Triangular matrices** make solving systems easy by substitution.

- •If U is upper-triangular, solve U **x** = **y** by **back substitution**.
- •If L is lower-triangular, solve L **y** = **b** by **forward substitution**.

These cost about O(n²) operations, much cheaper than O(n³) elimination.

**Orthogonal matrices** preserve lengths and angles:

‖Q **v**‖ = ‖**v**‖, and Q⁻¹ = Qᵀ.

This is valuable for numerical stability: multiplying by Q doesn’t amplify errors the way arbitrary matrices can.

### A quick comparison table

| Decomposition | Form | Typical use | Key strength | Key limitation |
| --- | --- | --- | --- | --- |
| LU (with pivoting) | P A = L U | Many solves A **x** = **b**, determinant | Fast repeated solves | Needs pivoting for robustness; typically square A |
| QR | A = Q R | Least squares, stable solves | Numerically stable | Usually more work than LU for square solves |

The rest of this lesson builds these ideas slowly: first LU as “organized Gaussian elimination,” then QR as “orthogonal elimination.”

## Core Mechanic 1: LU Decomposition (Gaussian Elimination as a Factorization)

### Why LU is the natural next step after Gaussian elimination

You already know Gaussian elimination: use row operations to turn A into an upper-triangular matrix, then solve by back substitution.

LU decomposition answers a natural question:

> Can we save the elimination work so we can solve A **x** = **b** for many **b** without re-eliminating every time?

Yes. LU stores the elimination multipliers in L and the resulting triangular matrix in U.

### The basic idea (no pivoting, conceptually)

Suppose elimination transforms A into U.

Each elimination step subtracts a multiple of a pivot row from rows below.

Those multiples become the subdiagonal entries of L.

The result is:

A = L U

where:

- •L has 1s on its diagonal (a common convention), and elimination multipliers below it
- •U is what you would obtain from elimination

### How solving works once you have A = L U

To solve A **x** = **b**:

A **x** = **b**

L U **x** = **b**

Let **y** = U **x**. Then:

1) L **y** = **b** (forward substitution)

2) U **x** = **y** (back substitution)

This is the payoff: after one O(n³) factorization, each new solve is ~O(n²).

### Pivoting: why P is needed in practice

In exact arithmetic, LU without pivoting can fail if a pivot is zero.

In floating-point arithmetic, it can also be disastrously inaccurate if a pivot is tiny.

Pivoting fixes this by swapping rows so that the pivot is “safe.” The most common form is **partial pivoting**.

We then write:

P A = L U

where P is a permutation matrix representing row swaps.

### Interpreting P

P is an identity matrix with rows permuted.

Multiplying by P on the left permutes rows:

(P A) has the same rows as A, just reordered.

In solving, it means you actually solve:

P A **x** = P **b**

L U **x** = P **b**

### Determinants from LU (with pivoting)

You already know det(A) = 0 iff A is singular. LU gives a fast route to det(A).

From P A = L U:

det(P A) = det(L U)

Use multiplicativity of determinant:

det(P) det(A) = det(L) det(U)

Now note:

- •If L has 1s on the diagonal (unit lower-triangular), then det(L) = 1.
- •For triangular matrices, det(U) is the product of diagonal entries: ∏ᵢ Uᵢᵢ.
- •det(P) is either +1 or −1 depending on whether the permutation is even or odd (number of row swaps).

So:

det(A) = det(P)⁻¹ det(L) det(U) = det(P) det(U)

because det(P)⁻¹ = det(P) (since det(P) = ±1).

### Cost model intuition

- •Factorization P A = L U: ~ (2/3) n³ flops
- •Solve with one **b** after factorization: ~ 2 n² flops

If you have many right-hand sides **b**₁, **b**₂, …, LU is a huge win.

### Geometric / conceptual view

Elimination is applying a sequence of elementary lower-triangular matrices E₁, E₂, … such that:

Eₖ … E₂ E₁ A = U

Those Eᵢ encode row operations. The inverse of a product of lower-triangular matrices is lower-triangular, so:

A = (E₁⁻¹ E₂⁻¹ … Eₖ⁻¹) U

and that product becomes L.

You don’t usually compute Eᵢ explicitly; LU is the compact record of what elimination did.

## Core Mechanic 2: QR Decomposition (Orthogonality as a Tool)

### Why QR exists (a different problem than LU)

LU shines for square systems A **x** = **b**.

But many real problems are **rectangular**:

- •Overdetermined: m > n (more equations than unknowns)
- •You usually can’t satisfy all equations exactly

So you solve a **least squares** problem:

minimize over **x**: ‖A **x** − **b**‖²

QR is designed for this. It also provides a numerically stable way to solve square systems.

### What QR says

For an m×n matrix A (typically m ≥ n), QR decomposition gives:

A = Q R

where:

- •Q is m×m orthogonal (full QR) or m×n with orthonormal columns (thin QR)
- •R is m×n (full) or n×n upper-triangular (thin)

The key property is orthogonality:

Qᵀ Q = I

and for thin QR:

Q has columns **q**₁, …, **q**ₙ with **q**ᵢᵀ **q**ⱼ = 0 for i ≠ j and ‖**q**ᵢ‖ = 1.

### Why orthogonality helps (stability and simplification)

Orthogonal transformations preserve norms:

‖Q **v**‖ = ‖**v**‖

and they don’t magnify relative errors much. That makes QR a workhorse in numerical linear algebra.

Also, orthogonality lets you “remove” Q easily since Q⁻¹ = Qᵀ.

### Least squares via QR (the key derivation)

We want:

min **x** ‖A **x** − **b**‖²

Substitute A = Q R:

‖A **x** − **b**‖²

= ‖Q R **x** − **b**‖²

Insert I = Q Qᵀ (since Q is orthogonal):

= ‖Q R **x** − Q Qᵀ **b**‖²

= ‖Q (R **x** − Qᵀ **b**)‖²

Now use norm preservation:

= ‖R **x** − Qᵀ **b**‖²

So the least squares problem reduces to minimizing a norm involving R, which is triangular.

In the common case m ≥ n with thin QR, R is n×n upper-triangular, and we solve:

R **x** = Qᵀ **b**

by back substitution (or solve the top n equations if using full QR).

### How QR is computed (high-level)

There are multiple algorithms; two important ones:

1) **Gram–Schmidt** (conceptual, but can be numerically fragile)

- •Builds orthonormal columns **q**ᵢ from the columns of A.

2) **Householder reflections** (standard in practice)

- •Applies orthogonal reflections to zero out subdiagonal entries column by column.
- •Very stable.

You don’t need to memorize the full Householder procedure yet, but you should understand the idea: QR uses orthogonal operations to make A triangular without the instability of naive elimination.

### QR for square systems

If A is square and nonsingular:

A **x** = **b**

Q R **x** = **b**

Multiply by Qᵀ:

R **x** = Qᵀ **b**

Then back substitution solves it.

Compared to LU, QR is often more stable (especially for ill-conditioned problems), but typically more expensive for square systems.

## Application/Connection: Choosing LU vs QR (and What They Enable)

### The decision: what problem are you solving?

Matrix decomposition is not one tool but a toolbox. The decomposition you choose matches the structure of the task.

| Task | Best default | Why |
| --- | --- | --- |
| Solve A **x** = **b** (square), many **b** | LU with pivoting | Fast repeated solves after factorization |
| Compute det(A) | LU with pivoting | det(A) = det(P) ∏ᵢ Uᵢᵢ |
| Least squares min ‖A **x** − **b**‖² | QR | Orthogonality gives stable reduction to triangular solve |
| Solve A **x** = **b** (square), high stability needed | QR | Orthogonal transforms are numerically gentle |

### What decompositions unlock in broader CS/ML workflows

1) **Efficient linear solves in optimization**

- •Many optimization algorithms (Newton, interior-point methods) repeatedly solve linear systems with related matrices.
- •LU becomes the “engine” behind each iteration.

2) **Least squares in data fitting**

- •Linear regression is fundamentally a least squares problem.
- •QR provides a stable alternative to solving normal equations (Aᵀ A **x** = Aᵀ **b**), which can square the condition number.

3) **Understanding singularity and rank behavior**

- •If U has a near-zero diagonal entry, LU signals numerical singularity.
- •In QR, small diagonal entries of R can indicate near rank-deficiency.

### A brief note on permutation matrices and practical implementations

In code libraries, you may see variants:

- •P A = L U (row pivoting)
- •A P = L U (column pivoting)
- •P A Q = L U (complete pivoting; rarer)

The purpose is the same: reorder rows/columns to find good pivots.

### A mental model you can reuse

- •LU: “Elimination with bookkeeping.” Stores multipliers in L.
- •QR: “Elimination using rotations/reflections.” Uses orthogonality to stay stable.

If you remember just that, you’ll choose correctly most of the time—and you’ll understand what the library function is doing when it returns L, U, P or Q, R.

## Worked Examples (3)

### LU decomposition (no pivoting) and solving A \*\*x\*\* = \*\*b\*\*

Let A = [[2, 1], [4, 3]] and **b** = [1, 2]ᵀ. Find L and U such that A = L U, then solve A **x** = **b**.

1. We eliminate the (2,1) entry (the 4) using pivot 2.

   Multiplier m = 4/2 = 2.
2. After elimination, row2 ← row2 − m·row1:

   row2: [4, 3] − 2·[2, 1] = [4, 3] − [4, 2] = [0, 1].

   So U = [[2, 1], [0, 1]].
3. Form L using the multiplier m below the diagonal and 1s on the diagonal:

   L = [[1, 0], [m, 1]] = [[1, 0], [2, 1]].
4. Check A = L U:

   L U = [[1, 0], [2, 1]] · [[2, 1], [0, 1]]

   = [

   [1·2 + 0·0, 1·1 + 0·1],

   [2·2 + 1·0, 2·1 + 1·1]

   ]

   = [[2, 1], [4, 3]] = A.
5. Solve A **x** = **b** via L U **x** = **b**.

   Let **y** = U **x**. First solve L **y** = **b** (forward substitution):

   [[1, 0], [2, 1]] · [y₁, y₂]ᵀ = [1, 2]ᵀ.

   Equation 1: y₁ = 1.

   Equation 2: 2y₁ + y₂ = 2 ⇒ 2·1 + y₂ = 2 ⇒ y₂ = 0.
6. Now solve U **x** = **y** (back substitution):

   [[2, 1], [0, 1]] · [x₁, x₂]ᵀ = [1, 0]ᵀ.

   Equation 2: x₂ = 0.

   Equation 1: 2x₁ + x₂ = 1 ⇒ 2x₁ = 1 ⇒ x₁ = 1/2.

**Insight:** LU turns one elimination into a reusable factorization: each new **b** only needs forward + back substitution.

### LU with pivoting: when a zero pivot forces a permutation

Let A = [[0, 1], [2, 3]]. Show that LU without pivoting fails, then find P, L, U such that P A = L U.

1. Attempt LU without pivoting: the first pivot would be A₁₁ = 0.

   We cannot eliminate below using pivot 0 (division by zero), so LU (without pivoting) fails.
2. Use a row swap to bring a nonzero pivot to the top.

   Swap row1 and row2. The permutation matrix is:

   P = [[0, 1], [1, 0]].
3. Compute P A:

   P A = [[0, 1], [1, 0]] · [[0, 1], [2, 3]]

   = [[2, 3], [0, 1]].
4. Now P A is already upper-triangular, so we can take:

   U = [[2, 3], [0, 1]].
5. Because no elimination was needed (no subdiagonal to eliminate), L is just the identity:

   L = [[1, 0], [0, 1]].
6. Verify:

   L U = I · U = U = P A.

**Insight:** Pivoting isn’t an optional detail: it makes LU exist (and behave well) by ensuring usable pivots.

### QR decomposition (conceptual) and least squares reduction

Suppose A is m×n with m ≥ n and A = Q R (thin QR, so Q is m×n with orthonormal columns and R is n×n upper-triangular). Show how min ‖A **x** − **b**‖ reduces to a triangular system.

1. Start with the least squares objective:

   min **x** ‖A **x** − **b**‖².
2. Substitute A = Q R:

   ‖A **x** − **b**‖² = ‖Q R **x** − **b**‖².
3. Use the fact that Q has orthonormal columns. Decompose **b** into components in the column space of Q and orthogonal to it:

   **b** = Q(Qᵀ **b**) + (**b** − Q(Qᵀ **b**)).

   Here Q(Qᵀ **b**) is the projection onto Col(Q) = Col(A).
4. Rewrite the residual:

   Q R **x** − **b**

   = Q R **x** − Q(Qᵀ **b**) − (**b** − Q(Qᵀ **b**))

   = Q(R **x** − Qᵀ **b**) − (**b** − Q(Qᵀ **b**)).
5. Now take norms. The two terms are orthogonal (one lies in Col(Q), the other in its orthogonal complement), so by the Pythagorean theorem:

   ‖Q(R **x** − Qᵀ **b**) − (**b** − Q(Qᵀ **b**))‖²

   = ‖Q(R **x** − Qᵀ **b**)‖² + ‖**b** − Q(Qᵀ **b**)‖².
6. Use norm preservation on the first term (since Q is orthonormal on its columns):

   ‖Q(R **x** − Qᵀ **b**)‖ = ‖R **x** − Qᵀ **b**‖.
7. The second term ‖**b** − Q(Qᵀ **b**)‖² does not depend on **x**, so minimizing the whole expression is equivalent to minimizing:

   ‖R **x** − Qᵀ **b**‖².
8. Thus the least squares minimizer **x** solves the triangular least squares problem, and when R is nonsingular (full column rank):

   R **x** = Qᵀ **b**

   which is solved by back substitution.

**Insight:** QR converts “fit a vector in a subspace” into a stable triangular solve, avoiding the error amplification of normal equations.

## Key Takeaways

- ✓

  Matrix decomposition rewrites A as a product of structured factors to make downstream computations easier.
- ✓

  LU (with pivoting) factors as P A = L U, where L is lower-triangular (often unit diagonal) and U is upper-triangular.
- ✓

  Once LU is computed, solving A **x** = **b** becomes two cheap steps: L **y** = P **b**, then U **x** = **y**.
- ✓

  Pivoting (P) is essential for avoiding zero or tiny pivots and improving numerical robustness.
- ✓

  For triangular matrices, determinants are easy: det(U) = ∏ᵢ Uᵢᵢ, and with LU, det(A) = det(P) det(U) (if L is unit lower-triangular).
- ✓

  QR factors A = Q R with Q orthogonal/unitary and R upper-triangular; Qᵀ = Q⁻¹ makes it algebraically convenient.
- ✓

  QR is the standard stable method for least squares: min ‖A **x** − **b**‖ reduces to solving R **x** = Qᵀ **b** (when full rank).

## Common Mistakes

- ✗

  Forgetting pivoting in LU and being surprised when a zero (or tiny) pivot breaks the factorization or causes large numerical error.
- ✗

  Mixing up where the permutation matrix goes: common conventions are P A = L U (row pivoting) or A = Pᵀ L U; libraries may return a pivot vector instead of P.
- ✗

  Assuming Q is always square m×m; in thin QR, Q is m×n with orthonormal columns, and R is n×n.
- ✗

  Using normal equations Aᵀ A **x** = Aᵀ **b** by default for least squares without realizing it can be less stable than QR (because it can worsen conditioning).

## Practice

easy

Compute an LU decomposition (no pivoting) of A = [[1, 2], [3, 8]] into A = L U with L unit lower-triangular. Then solve A **x** = **b** for **b** = [5, 15]ᵀ using the factors.

**Hint:** Eliminate the 3 under the pivot 1. The multiplier is m = 3/1. Put m into L₂₁, and the resulting upper-triangular matrix is U.

Show solution

Eliminate: m = 3.

U comes from row2 ← row2 − 3·row1:

row2: [3, 8] − 3·[1, 2] = [0, 2].

So U = [[1, 2], [0, 2]].

L = [[1, 0], [3, 1]].

Solve L **y** = **b**:

y₁ = 5.

3y₁ + y₂ = 15 ⇒ 15 + y₂ = 15 ⇒ y₂ = 0.

Solve U **x** = **y**:

2x₂ = 0 ⇒ x₂ = 0.

x₁ + 2x₂ = 5 ⇒ x₁ = 5.

So **x** = [5, 0]ᵀ.

medium

Let P A = L U be an LU decomposition with L unit lower-triangular. Suppose U has diagonal entries (2, −1, 5) and P corresponds to exactly one row swap. Compute det(A).

**Hint:** Use det(P) det(A) = det(L) det(U). For unit lower-triangular L, det(L) = 1. One row swap means det(P) = −1.

Show solution

det(U) = 2 · (−1) · 5 = −10.

With one row swap, det(P) = −1.

From det(P) det(A) = det(L) det(U) = 1 · (−10) = −10,

(−1) det(A) = −10 ⇒ det(A) = 10.

hard

Assume A = Q R is a thin QR decomposition with Qᵀ Q = I and R upper-triangular and invertible. Show that the unique minimizer of min ‖A **x** − **b**‖ is the solution to R **x** = Qᵀ **b**.

**Hint:** Start from ‖A **x** − **b**‖ = ‖Q R **x** − **b**‖. Add and subtract Q(Qᵀ **b**) and use orthogonality to split the norm into two parts, one depending on **x** and one not.

Show solution

We minimize f(**x**) = ‖A **x** − **b**‖² = ‖Q R **x** − **b**‖².

Write **b** = Q(Qᵀ **b**) + (**b** − Q(Qᵀ **b**)).

Then:

Q R **x** − **b** = Q(R **x** − Qᵀ **b**) − (**b** − Q(Qᵀ **b**)).

The two terms are orthogonal, so:

‖Q(R **x** − Qᵀ **b**) − (**b** − Q(Qᵀ **b**))‖²

= ‖Q(R **x** − Qᵀ **b**)‖² + ‖**b** − Q(Qᵀ **b**)‖².

Because Q has orthonormal columns, ‖Q **v**‖ = ‖**v**‖ for **v** ∈ ℝⁿ, hence:

= ‖R **x** − Qᵀ **b**‖² + constant.

Therefore minimizing f(**x**) is equivalent to minimizing ‖R **x** − Qᵀ **b**‖².

Since R is invertible, the unique minimizer satisfies R **x** = Qᵀ **b**, giving **x** = R⁻¹ Qᵀ **b**.

## Connections

[Systems of Linear Equations](/tech-tree/systems-linear-equations/)

[Gaussian Elimination](/tech-tree/gaussian-elimination/)

[Determinants](/tech-tree/determinants/)

[Orthogonal Matrices](/tech-tree/orthogonal-matrices/)

[Least Squares Regression](/tech-tree/least-squares-regression/)

[Condition Number and Numerical Stability](/tech-tree/condition-number/)

Quality: B (4.1/5)

[← back to tree](/tech-tree/)[browse all →](/tech-tree/inventory/)
