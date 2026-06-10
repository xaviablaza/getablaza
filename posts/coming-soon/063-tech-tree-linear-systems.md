---
title: Systems of Linear Equations
description: Multiple equations with multiple unknowns. Gaussian elimination.
date: '2026-07-01'
scheduled: '2026-09-01'
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
inspiration_url: https://templeton.host/tech-tree/linear-systems/
inspiration_category: tech-tree
---

> Source-copy draft imported from [https://templeton.host/tech-tree/linear-systems/](https://templeton.host/tech-tree/linear-systems/). Names, domain references, and local media paths were adapted for Xavi Ablaza / getablaza.com.

[←Back to Tech Tree](/tech-tree/)

[inventory](/tech-tree/inventory/)[coverage](/tech-tree/coverage/)

# Systems of Linear Equations

Linear AlgebraDifficulty: ★★☆☆☆Depth: 3Unlocks: 24

Multiple equations with multiple unknowns. Gaussian elimination.

## Interactive Visualization

⏮◀◀▶▶STEP0.25x1xZOOM

t=0s

## Core Concepts

- -System represented as a matrix equation Ax = b
- -Solution set of a system (types: unique, infinite, none)
- -Gaussian elimination: use elementary row operations to convert the augmented matrix to row-echelon form to find solutions

## Key Symbols & Notation

Augmented matrix notation: [A | b] (represents the system Ax = b)

## Essential Relationships

- -Elementary row operations produce an equivalent system (they preserve the solution set)
- -Consistency criterion: the system has a solution exactly when rank(A) equals rank([A | b])

## Prerequisites (2)

[Matrix Operations6 atoms](/tech-tree/matrix-operations/)[Linear Equations5 atoms](/tech-tree/linear-equations/)

## Unlocks (4)

[Eigenvalues and Eigenvectorslvl 3](/tech-tree/eigenvalues/)[Linear Programminglvl 4](/tech-tree/linear-programming/)[Matrix Decompositionlvl 3](/tech-tree/matrix-decomposition/)[Conjugate Gradient Methodslvl 5](/tech-tree/conjugate-gradients/)

Advanced Learning Details

### Graph Position

34

Depth Cost

24

Fan-Out (ROI)

11

Bottleneck Score

3

Chain Length

### Cognitive Load

6

Atomic Elements

47

Total Elements

L3

Percentile Level

L4

Atomic Level

### All Concepts (23)

- - system of linear equations: a set of linear equations in multiple unknowns considered together
- - solution of a system: an ordered tuple (x1,...,xn) that satisfies every equation
- - types of solutions: unique solution, no solution (inconsistent), infinitely many solutions
- - coefficient matrix: matrix A collecting the coefficients of the variables
- - augmented matrix: matrix [A | b] that combines the coefficient matrix A and the right-hand side vector b
- - elementary row operations: (1) swap two rows, (2) multiply a row by a nonzero scalar, (3) add a scalar multiple of one row to another
- - Gaussian elimination (forward elimination): systematic use of row operations to produce an upper-triangular / row‑echelon form
- - back substitution: solving for variables after forward elimination produces an upper-triangular system
- - row‑echelon form (REF): triangular-like matrix form with leading entries stepping to the right on lower rows
- - reduced row‑echelon form (RREF): row‑echelon form refined so each pivot is 1 and is the only nonzero entry in its column
- - pivot / leading entry: the first nonzero entry in a nonzero row of REF/RREF
- - pivot column: a column containing a pivot (used to identify basic variables)
- - basic (leading) variables: variables corresponding to pivot columns
- - free variables: non-pivot variables that can be set as parameters when infinitely many solutions exist
- - parametric description of solution sets: expressing solutions using parameters for free variables
- - row‑equivalence: matrices reachable from one another by elementary row operations (they have the same solution set)
- - consistency condition via augmented matrix: a row [0 ... 0 | c] with c ≠ 0 indicates inconsistency (no solution)
- - rank of a matrix (as used for systems): number of pivots / dimension of row or column space relevant to solution existence/uniqueness
- - homogeneous system Ax = 0: special case always consistent; distinguishes trivial vs. nontrivial solutions
- - nullspace / kernel (as solution space of Ax = 0): the set of all solutions to the homogeneous system
- - particular solution + nullspace decomposition: general solution of Ax = b = one particular solution plus all homogeneous solutions
- - overdetermined vs underdetermined systems: more equations than unknowns vs fewer equations than unknowns
- - elementary matrices (optional): matrices that perform a single elementary row operation when left-multiplied

### Teaching Strategy

Deep-dive lesson - accessible entry point but dense material. Use worked examples and spaced repetition.

When you have many unknowns and many equations, “solve for x” stops being a single trick and becomes a reusable procedure. Systems of linear equations are where algebra turns into a reliable algorithm: represent the system as Ax = b, then use Gaussian elimination to systematically simplify it until the answers are visible.

TL;DR:

A system of linear equations can be written as a matrix equation A**x** = **b**. To solve it, build the augmented matrix [A | **b**] and apply elementary row operations to reach (reduced) row‑echelon form. Then read off whether the system has a unique solution, infinitely many solutions, or no solution.

## What Is a System of Linear Equations?

### Why this concept exists (motivation)

A single linear equation like y = mx + b describes a line. Two linear equations in two unknowns describe the intersection of two lines. But real problems often look like:

- •balancing flows through a network (many constraints)
- •fitting a linear model (many parameters)
- •computing currents in a circuit (Kirchhoff’s laws)

In all these, you have **multiple linear constraints** and you want values of the unknowns that satisfy all of them simultaneously.

### Definition

A **system of linear equations** is a set of equations where each equation is linear in the unknowns. For unknowns x₁, x₂, …, xₙ, a typical system is:

a₁₁x₁ + a₁₂x₂ + … + a₁ₙxₙ = b₁

a₂₁x₁ + a₂₂x₂ + … + a₂ₙxₙ = b₂

…

aₘ₁x₁ + aₘ₂x₂ + … + aₘₙxₙ = bₘ

Here:

- •the aᵢⱼ are coefficients (known numbers)
- •the bᵢ are constants (known numbers)
- •the xⱼ are unknowns

### Matrix equation form: A**x** = **b**

This system is compactly written as:

A**x** = **b**

where:

- •A ∈ ℝᵐˣⁿ is the coefficient matrix
- •**x** ∈ ℝⁿ is the vector of unknowns
- •**b** ∈ ℝᵐ is the right-hand side vector

Using bold for vectors:

**x** = (x₁, x₂, …, xₙ)ᵀ

**b** = (b₁, b₂, …, bₘ)ᵀ

### Solution set (what “solving” means)

A **solution** is any vector **x** such that A**x** = **b**.

There are three high-level possibilities:

| Situation | What it means geometrically (in 2D/3D) | What you see algebraically |
| --- | --- | --- |
| Unique solution | lines/planes intersect at exactly one point | one pivot per variable, no contradictions |
| Infinitely many solutions | lines coincide; planes intersect in a line/plane | at least one free variable |
| No solution | parallel inconsistent lines/planes | a contradiction like 0 = 1 |

### Augmented matrix notation [A | **b**]

Instead of writing all equations, we “pack” them into one matrix by appending **b** as an extra column:

[A | **b**]

This is called the **augmented matrix**. It represents the same system, just more conveniently for computations.

For example, the system:

2x + y = 5

x − 3y = −4

becomes:

A = [ [2, 1], [1, −3] ]

**b** = [5, −4]ᵀ

[A | **b**] = [ [2, 1 | 5], [1, −3 | −4] ]

The entire point of the next sections is: **operate on rows of [A | b] to simplify the system without changing its solution set.**

## Core Mechanic 1: Elementary Row Operations (Why They Preserve Solutions)

### Why row operations are allowed

If you take an equation and:

1) swap it with another equation,

2) multiply it by a nonzero number,

3) add a multiple of another equation,

you do not change the set of **common solutions**. You’re just rewriting the same constraints in an equivalent form.

Gaussian elimination is the process of doing these rewrites systematically until the system is easy to solve.

### The three elementary row operations

When working with the augmented matrix [A | **b**], we treat each row as one equation.

| Row operation | Notation | Meaning in equation form |
| --- | --- | --- |
| Swap two rows | Rᵢ ↔ Rⱼ | reorder equations |
| Scale a row | Rᵢ ← cRᵢ (c ≠ 0) | multiply an equation by nonzero c |
| Replace a row by itself plus a multiple of another | Rᵢ ← Rᵢ + cRⱼ | add c·(equation j) to equation i |

### Why they preserve the solution set (quick reasoning)

- •**Swap:** If **x** satisfies all equations, it still satisfies them after reordering.
- •**Scale by nonzero c:** If aᵀ**x** = b, then (caᵀ)**x** = cb has exactly the same solutions when c ≠ 0.
- •**Row replacement:** If **x** satisfies both equations:
- •(row i): aᵀ**x** = b
- •(row j): dᵀ**x** = e

then it satisfies their combination:

- •(aᵀ + c dᵀ)**x** = b + c e

So these operations create an **equivalent system**.

### Pivots, leading entries, and echelon forms

Row operations aim to create zeros below (and sometimes above) a chosen “leading” coefficient.

Key vocabulary:

- •**Leading entry** in a row: the first nonzero number from the left.
- •**Pivot position:** location of a leading entry.
- •**Pivot variable:** the variable corresponding to a pivot column.
- •**Free variable:** a variable that is not a pivot variable.

Two common targets:

1) **Row-echelon form (REF)**

- •all nonzero rows above any all-zero rows
- •leading entries move right as you go down
- •zeros below each leading entry

2) **Reduced row-echelon form (RREF)** (Gauss–Jordan)

- •same as REF, plus:
- •each pivot is 1
- •zeros above each pivot as well

REF is enough to solve by back-substitution; RREF makes solutions easiest to read directly.

### The “shape” tells you the solution type

Once you reach REF/RREF, you can diagnose:

- •**Contradiction row:** [0 0 … 0 | c] with c ≠ 0
- •means 0 = c (impossible) ⇒ **no solution**

- •**At least one free variable:** fewer pivots than variables
- •means a family of solutions ⇒ **infinitely many solutions**

- •**Pivot in every variable column (for a square n×n system):**
- •typically ⇒ **unique solution**

(There are edge cases with non-square systems, but the pivot/free-variable logic still classifies solution sets correctly.)

## Core Mechanic 2: Gaussian Elimination on the Augmented Matrix [A | b]

### Why Gaussian elimination works (strategy)

Solving a system directly can be messy because variables are entangled across equations. Gaussian elimination creates a simpler, equivalent system where variables are gradually “separated.”

The high-level plan:

1) Put [A | **b**] into REF (forward elimination)

2) Solve from bottom to top (back-substitution)

Optionally:

3) Continue to RREF (Gauss–Jordan) to read solutions immediately

### Forward elimination (creating REF)

Suppose we have m equations and n unknowns. The elimination loop conceptually does:

For each column (variable) from left to right:

- •pick a pivot row that has a nonzero entry in that column
- •swap it into place (if needed)
- •eliminate entries below the pivot by row replacement

A practical note: when computing with floating point, people often use **partial pivoting** (choose the largest magnitude entry as pivot). For difficulty 2, you mainly need the symbolic/hand method: pick a nonzero pivot.

### Back-substitution (solving after REF)

After forward elimination, the last row typically involves the last pivot variable, then you substitute upward.

### Reading solutions in RREF (optional but powerful)

RREF gives equations of the form:

x₁ = (number) + (coefficients)·(free variables)

which makes parametric solution sets very clear.

### How free variables create infinitely many solutions

If n variables but only r pivots (r < n), then there are n − r free variables. You can choose those freely (parameters), and the pivot variables become determined by them.

Example template in RREF:

[1 0 2 | 3]

[0 1 −1 | 4]

Here x₃ is free.

Equations:

- •x₁ + 2x₃ = 3 ⇒ x₁ = 3 − 2x₃
- •x₂ − x₃ = 4 ⇒ x₂ = 4 + x₃

Let x₃ = t. Then:

**x** = (x₁, x₂, x₃)ᵀ = (3 − 2t, 4 + t, t)ᵀ

This is an infinite set (a line in ℝ³).

### Detecting no solution

If elimination produces:

[0 0 0 | 1]

that corresponds to 0 = 1, so the system is inconsistent.

### Unique solution case

When every variable is a pivot variable (no free variables) and there is no contradiction row, you get a unique solution.

In RREF for a square n×n system, it looks like:

[I | **x**]

where I is the identity matrix, and the right side is the unique solution vector.

## Application/Connection: Why Ax = b Shows Up Everywhere

### Linear algebra viewpoint: A as a transformation

You already know a matrix as a linear transformation. In A**x** = **b**:

- •**x** is an input vector
- •A transforms it into an output
- •**b** is the desired output

So “solving the system” means: **find an input that maps to a particular output**.

If you think of A as a function, solving A**x** = **b** is like inverting that function on a particular value **b**.

### Geometry: intersections and consistency

- •In 2D, each equation is a line; solving means finding intersection(s).
- •In 3D, each equation is a plane; solving means common intersection of planes.

Gaussian elimination is the algebraic method that scales beyond what you can visualize.

### Computational significance

Gaussian elimination is the foundation under many higher-level tools:

- •**LU decomposition:** Gaussian elimination reorganized into matrix factors (A = LU) for efficient solving with many different **b**.
- •**Least squares (when system is overdetermined):** if there is no exact solution, you solve a related system that minimizes ‖A**x** − **b**‖.
- •**Optimization and constraints:** linear programming constraints are linear equations/inequalities; elimination is a core primitive behind simplex and feasibility checks.

### A small roadmap of what this unlocks

- •Eigenvalues/eigenvectors: solving (A − λI)**v** = **0** is a linear system whose solutions **v** are eigenvectors.
- •Decompositions (LU/QR): structured versions of elimination.
- •Conjugate gradients: iterative method for large symmetric positive definite systems A**x** = **b** where elimination is too expensive.

### When not to use hand elimination

By hand, Gaussian elimination is great for understanding and small systems (2×2, 3×3). For large systems, computers use optimized variants (pivoting, sparse methods) to control round-off and complexity.

## Worked Examples (3)

### Unique solution (2×2) via Gaussian elimination

Solve the system:

2x + y = 5

x − 3y = −4

Write it as [A | b] and use row operations to reach RREF.

1. Form the augmented matrix:

   [ 2 1 | 5 ]

   [ 1 −3 | −4 ]
2. Swap rows to get a 1 in the top-left pivot position (optional but convenient):

   R₁ ↔ R₂

   [ 1 −3 | −4 ]

   [ 2 1 | 5 ]
3. Eliminate the entry below the pivot (make the (2,1) entry zero):

   R₂ ← R₂ − 2R₁

   Compute 2R₁:

   2R₁ = [ 2 −6 | −8 ]

   Now subtract:

   R₂ = [ 2 1 | 5 ] − [ 2 −6 | −8 ] = [ 0 7 | 13 ]

   So:

   [ 1 −3 | −4 ]

   [ 0 7 | 13 ]
4. Scale the second row to make the pivot 1:

   R₂ ← (1/7)R₂

   [ 1 −3 | −4 ]

   [ 0 1 | 13/7 ]
5. Eliminate the entry above the pivot to reach RREF:

   R₁ ← R₁ + 3R₂

   Compute 3R₂:

   3R₂ = [ 0 3 | 39/7 ]

   Add to R₁:

   R₁ = [ 1 −3 | −4 ] + [ 0 3 | 39/7 ] = [ 1 0 | −4 + 39/7 ]

   Convert −4 = −28/7:

   −28/7 + 39/7 = 11/7

   So:

   [ 1 0 | 11/7 ]

   [ 0 1 | 13/7 ]
6. Read the solution:

   x = 11/7

   y = 13/7

**Insight:** Row operations turned two entangled equations into x = constant and y = constant. In RREF, the left side becomes I, making the unique solution immediate.

### Infinitely many solutions (free variable) and parametric form

Solve:

x + y + z = 2

2x + 2y + 2z = 4

x − y + z = 0

Use Gaussian elimination and express the solution set with a parameter.

1. Write the augmented matrix:

   [ 1 1 1 | 2 ]

   [ 2 2 2 | 4 ]

   [ 1 −1 1 | 0 ]
2. Eliminate below the first pivot (in column 1):

   R₂ ← R₂ − 2R₁

   R₃ ← R₃ − R₁

   Compute:

   R₂: [2 2 2 | 4] − 2·[1 1 1 | 2] = [0 0 0 | 0]

   R₃: [1 −1 1 | 0] − [1 1 1 | 2] = [0 −2 0 | −2]

   Matrix becomes:

   [ 1 1 1 | 2 ]

   [ 0 0 0 | 0 ]

   [ 0 −2 0 | −2 ]
3. Swap rows to keep nonzero rows on top (REF convention):

   R₂ ↔ R₃

   [ 1 1 1 | 2 ]

   [ 0 −2 0 | −2 ]

   [ 0 0 0 | 0 ]
4. Scale row 2 to make the pivot 1:

   R₂ ← (−1/2)R₂

   [ 1 1 1 | 2 ]

   [ 0 1 0 | 1 ]

   [ 0 0 0 | 0 ]
5. Eliminate the y term from row 1:

   R₁ ← R₁ − R₂

   [ 1 0 1 | 1 ]

   [ 0 1 0 | 1 ]

   [ 0 0 0 | 0 ]
6. Interpret the RREF equations:

   Row 1: x + z = 1

   Row 2: y = 1

   Row 3: 0 = 0 (no new information)

   Let z be free: set z = t.

   Then:

   x = 1 − t

   y = 1

   z = t

   So:

   **x** = (x, y, z)ᵀ = (1 − t, 1, t)ᵀ

**Insight:** The second equation was redundant (a multiple of the first), so there weren’t enough independent constraints to pin down all variables. One free variable ⇒ infinitely many solutions.

### No solution (inconsistency) detected by a contradiction row

Solve (or show no solution):

x + y = 1

2x + 2y = 3

Use elimination on [A | b].

1. Augmented matrix:

   [ 1 1 | 1 ]

   [ 2 2 | 3 ]
2. Eliminate below the pivot:

   R₂ ← R₂ − 2R₁

   Compute:

   [2 2 | 3] − 2·[1 1 | 1] = [0 0 | 1]

   So we get:

   [ 1 1 | 1 ]

   [ 0 0 | 1 ]
3. Interpret row 2:

   0x + 0y = 1

   This is 0 = 1, which is impossible.
4. Conclude:

   No solution (the system is inconsistent).

**Insight:** Elimination doesn’t just find solutions; it also proves impossibility. A row of zeros on the left with a nonzero right side is the unmistakable inconsistency signal.

## Key Takeaways

- ✓

  A system of linear equations can be written compactly as A**x** = **b**.
- ✓

  The augmented matrix [A | **b**] is a bookkeeping tool that lets you apply row operations to coefficients and constants together.
- ✓

  Elementary row operations (swap, scale by nonzero, row replacement) produce an equivalent system with the same solution set.
- ✓

  Gaussian elimination (forward elimination + back-substitution) converts [A | **b**] to row-echelon form to make solving systematic.
- ✓

  RREF makes solutions easiest to read: pivot variables are determined; free variables become parameters.
- ✓

  A contradiction row [0 0 … 0 | c] with c ≠ 0 means no solution.
- ✓

  Fewer pivots than variables means infinitely many solutions (at least one free variable).

## Common Mistakes

- ✗

  Forgetting to apply a row operation to the entire augmented row (including the **b** column).
- ✗

  Treating scaling by 0 as a valid row operation (it is not; it destroys equivalence).
- ✗

  Stopping at REF but mis-reading which variables are free vs pivot variables, leading to an incorrect parameterization.
- ✗

  Arithmetic slips during elimination (especially sign errors) that create fake contradictions or fake free variables.

## Practice

easy

Solve using Gaussian elimination:

3x − y = 7

6x − 2y = 14

**Hint:** Notice the second equation is a multiple of the first. What does that imply about pivots/free variables?

Show solution

Augmented matrix:

[ 3 −1 | 7 ]

[ 6 −2 | 14 ]

Eliminate:

R₂ ← R₂ − 2R₁

[6 −2 | 14] − 2·[3 −1 | 7] = [0 0 | 0]

So the system reduces to one equation: 3x − y = 7.

Let y = t (free).

Then 3x − t = 7 ⇒ x = (7 + t)/3.

Infinitely many solutions: (x, y) = ((7 + t)/3, t).

medium

Solve and classify (unique/infinite/none):

x + 2y − z = 1

2x + 4y − 2z = 2

−x − 2y + z = 0

**Hint:** After elimination, check whether you get a contradiction row or a free variable. Watch for dependent equations.

Show solution

Augmented matrix:

[ 1 2 −1 | 1 ]

[ 2 4 −2 | 2 ]

[−1 −2 1 | 0 ]

Eliminate using R₁ as pivot:

R₂ ← R₂ − 2R₁:

[2 4 −2 | 2] − 2·[1 2 −1 | 1] = [0 0 0 | 0]

R₃ ← R₃ + R₁:

[−1 −2 1 | 0] + [1 2 −1 | 1] = [0 0 0 | 1]

Now we have a contradiction row [0 0 0 | 1] ⇒ 0 = 1.

Therefore the system has no solution (inconsistent).

hard

Find the solution set in parametric vector form for:

x + y + z + w = 2

2x + y + 3z + w = 5

**Hint:** You have 2 equations and 4 unknowns, so expect 2 free variables. Use elimination to express pivot variables in terms of the free ones.

Show solution

Augmented matrix:

[ 1 1 1 1 | 2 ]

[ 2 1 3 1 | 5 ]

Eliminate below pivot in column 1:

R₂ ← R₂ − 2R₁

R₂ = [2 1 3 1 | 5] − 2·[1 1 1 1 | 2] = [0 −1 1 −1 | 1]

So:

[ 1 1 1 1 | 2 ]

[ 0 −1 1 −1 | 1 ]

Scale row 2:

R₂ ← −R₂:

[ 1 1 1 1 | 2 ]

[ 0 1 −1 1 | −1 ]

Eliminate y from row 1:

R₁ ← R₁ − R₂:

[1 1 1 1 | 2] − [0 1 −1 1 | −1] = [1 0 2 0 | 3]

RREF-like system:

Row 1: x + 2z = 3

Row 2: y − z + w = −1

Let z = s and w = t (free variables).

Then:

x = 3 − 2s

y = −1 + s − t

Parametric vector form:

**x** = (x, y, z, w)ᵀ

= (3 − 2s, −1 + s − t, s, t)ᵀ

= (3, −1, 0, 0)ᵀ + s(−2, 1, 1, 0)ᵀ + t(0, −1, 0, 1)ᵀ.

## Connections

- •Next: [Eigenvalues and Eigenvectors](/tech-tree/eigenvalues/) (you’ll solve (A − λI)**v** = **0**)
- •Next: [Matrix Decomposition](/tech-tree/matrix-decomposition/) (LU factors come directly from elimination)
- •Next: [Linear Programming](/tech-tree/linear-programming/) (systems define constraint boundaries)
- •Next: [Conjugate Gradient Methods](/tech-tree/conjugate-gradients/) (iterative solving of large A**x** = **b**)
- •Review: [Matrix Operations](/tech-tree/matrix-operations/)
- •Review: [Linear Equations](/tech-tree/linear-equations/)

Quality: A (4.5/5)

[← back to tree](/tech-tree/)[browse all →](/tech-tree/inventory/)
