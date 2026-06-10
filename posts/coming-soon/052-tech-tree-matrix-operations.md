---
title: Matrix Operations
description: Addition, multiplication, transpose. Matrix as linear transformation.
date: '2026-07-01'
scheduled: '2026-08-21'
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
inspiration_url: https://templeton.host/tech-tree/matrix-operations/
inspiration_category: tech-tree
---

> Source-copy draft imported from [https://templeton.host/tech-tree/matrix-operations/](https://templeton.host/tech-tree/matrix-operations/). Names, domain references, and local media paths were adapted for Xavi Ablaza / getablaza.com.

[←Back to Tech Tree](/tech-tree/)

[inventory](/tech-tree/inventory/)[coverage](/tech-tree/coverage/)

# Matrix Operations

Linear AlgebraDifficulty: ★★☆☆☆Depth: 2Unlocks: 51

Addition, multiplication, transpose. Matrix as linear transformation.

## Interactive Visualization

⏮◀◀▶▶STEP0.25x1xZOOM

t=0s

## Core Concepts

- -Matrix as a linear transformation: a rectangular array whose columns (or entries) specify a linear map from R^n to R^m
- -Matrix addition and scalar multiplication: componentwise addition and scalar scaling making matrices into a vector space
- -Matrix multiplication: binary operation producing a matrix that represents composing linear maps (defined by the row-by-column entry rule)
- -Transpose: operation that swaps rows and columns, with (A^T)\_{ij} = a\_{ji}

## Key Symbols & Notation

a\_ij (entry at row i, column j)

## Essential Relationships

- -Matrix multiplication corresponds to composition of linear transformations: AB means apply B then A, with entries computed by summing products of corresponding row and column entries

## Prerequisites (1)

[Vectors Introduction6 atoms](/tech-tree/vectors-intro/)

## Unlocks (6)

[Systems of Linear Equationslvl 2](/tech-tree/linear-systems/)[Determinantslvl 3](/tech-tree/determinants/)[Game Theory Introductionlvl 3](/tech-tree/game-theory-intro/)[Jacobianlvl 3](/tech-tree/jacobian/)[Matrix Calculuslvl 4](/tech-tree/matrix-calculus/)[Markov Chainslvl 4](/tech-tree/markov-chains/)

Advanced Learning Details

### Graph Position

18

Depth Cost

51

Fan-Out (ROI)

21

Bottleneck Score

2

Chain Length

### Cognitive Load

6

Atomic Elements

49

Total Elements

L4

Percentile Level

L4

Atomic Level

### All Concepts (19)

- - Matrix: a rectangular array of numbers with m rows and n columns (entries denoted a\_{ij})
- - Matrix dimensions: the size m×n, row vs column, row count and column count
- - Matrix entry notation a\_{ij}: element in i-th row and j-th column
- - Matrix equality: two matrices equal iff same dimensions and all corresponding entries equal
- - Zero matrix 0\_{m×n}: the matrix of all zeros for given dimensions
- - Identity matrix I\_n: the n×n matrix with 1s on the diagonal and 0s elsewhere
- - Matrix addition: elementwise addition defined only for same-dimension matrices
- - Scalar multiplication of a matrix: multiply each entry by a scalar
- - Matrix transpose A^T: flip rows and columns (i.e., (A^T)\_{ij}=A\_{ji})
- - Matrix multiplication (definition): product AB defined by row-by-column rule (or equivalently columns of AB are linear combinations of columns of A)
- - Dimension compatibility for multiplication: AB defined only when A is m×n and B is n×p
- - Resulting size of a product: an m×p matrix when multiplying m×n by n×p
- - Matrix-vector product Ax: multiplying an m×n matrix by an n-vector to produce an m-vector
- - Matrices as linear transformations: an m×n matrix represents a linear map from R^n to R^m
- - Columns as images of basis vectors: the j-th column of A equals A applied to the j-th standard basis vector
- - Kernel/nullspace of A: set of vectors x with Ax = 0
- - Column space / image of A: span of the columns of A, i.e., the set of all Ax
- - Associative and distributive properties of matrix multiplication with respect to addition (structural properties)
- - Non-commutativity of matrix multiplication: AB generally differs from BA

### Teaching Strategy

Deep-dive lesson - accessible entry point but dense material. Use worked examples and spaced repetition.

Matrices look like “just tables of numbers,” but their real power is that they *do something*: they represent linear transformations—rules that move, rotate, stretch, and mix vectors in a consistent way.

TL;DR:

A matrix is a linear map from ℝⁿ to ℝᵐ. You can add matrices and scale them entry-by-entry. You multiply matrices to compose linear maps (apply one, then the other). The transpose swaps rows and columns and often converts “row” viewpoints into “column” viewpoints.

## What Is Matrix Operations? (And What Is a Matrix?)

### Why we care

You already know vectors: you can add them and scale them, and those operations have geometric meaning (combine directions, change magnitude). Matrices extend this idea: they describe *linear rules* that take an input vector and produce an output vector.

If vectors are “arrows,” then matrices are “machines that transform arrows.” Understanding addition, multiplication, and transpose is mostly about understanding how these machines combine.

### The object: a matrix

A matrix **A** is a rectangular array of numbers with **m rows** and **n columns**. We write **A** ∈ ℝᵐˣⁿ.

- •Entry notation: aᵢⱼ means “row i, column j.”
- •Shape matters: a 2×3 matrix is a different kind of object than a 3×2 matrix.

Example:

**A** = [ [1, 2, 0],

[−1, 3, 4] ] is 2×3

### Matrix as a linear transformation (the main intuition)

A matrix **A** ∈ ℝᵐˣⁿ represents a linear map

**A**: ℝⁿ → ℝᵐ

Given an input vector **x** ∈ ℝⁿ, the output is **y** = **A****x** ∈ ℝᵐ.

The most important way to “see” **A** is via its **columns**.

Let **A** have columns **a₁**, **a₂**, …, **aₙ**, where each **aⱼ** ∈ ℝᵐ. Write

**A** = [ **a₁** **a₂** … **aₙ** ]

If **x** = [x₁, x₂, …, xₙ]ᵀ, then

**A****x** = x₁**a₁** + x₂**a₂** + … + xₙ**aₙ**

That is: **A****x** is a linear combination of the columns of **A**, using the entries of **x** as weights.

### Linearity (what makes matrices special)

A transformation T is linear if for all vectors **u**, **v** and scalars c:

T(**u** + **v**) = T(**u**) + T(**v**)

T(c**u**) = cT(**u**)

Matrix multiplication **A****x** always defines a linear transformation, and (in finite-dimensional real vector spaces) every linear transformation can be represented by some matrix.

This node is about operations that correspond to natural ways of combining these linear machines:

- •**Addition / scalar multiplication**: combine machines “in parallel” (add their outputs).
- •**Multiplication**: combine machines “in series” (compose transformations).
- •**Transpose**: flip the matrix, swapping the roles of inputs/outputs in many identities.

## Core Mechanic 1: Matrix Addition and Scalar Multiplication

### Why these operations exist

When you add vectors, you get another vector that represents the combined effect. For matrices, addition and scaling let you build new linear transformations from old ones.

If **A** and **B** both take ℝⁿ → ℝᵐ, then you can define a new transformation:

(**A** + **B**)(**x**) = **A****x** + **B****x**

This is “add the outputs” for the same input.

### Definition: addition (componentwise)

You may add matrices only when they have the **same shape**.

If **A**, **B** ∈ ℝᵐˣⁿ, then **C** = **A** + **B** ∈ ℝᵐˣⁿ is defined by

cᵢⱼ = aᵢⱼ + bᵢⱼ

So it’s entry-by-entry.

### Definition: scalar multiplication

For scalar c ∈ ℝ and matrix **A** ∈ ℝᵐˣⁿ:

(c**A**)ᵢⱼ = c·aᵢⱼ

Again, entry-by-entry.

### Geometric / transformation viewpoint

If **A** and **B** represent linear maps ℝⁿ → ℝᵐ, then:

- •**A** + **B** is the map that sends **x** to **A****x** + **B****x**.
- •c**A** is the map that sends **x** to c(**A****x**) (it scales every output by c).

A useful identity to connect “entry rules” to “transformation rules”:

(**A** + **B**)**x** = **A****x** + **B****x**

Proof (by columns; a good mental model):

Let **A** = [**a₁** … **aₙ**], **B** = [**b₁** … **bₙ**]. Then **A** + **B** = [**a₁**+**b₁** … **aₙ**+**bₙ**].

So for **x** = [x₁,…,xₙ]ᵀ:

(**A**+**B**)**x**

= x₁(**a₁**+**b₁**) + … + xₙ(**aₙ**+**bₙ**)

= (x₁**a₁** + … + xₙ**aₙ**) + (x₁**b₁** + … + xₙ**bₙ**)

= **A****x** + **B****x**

### Matrices form a vector space

Because addition and scalar multiplication behave like vector operations, the set ℝᵐˣⁿ is a vector space.

Here are the most used properties (they mirror vector properties):

- •**Commutativity**: **A** + **B** = **B** + **A**
- •**Associativity**: (**A** + **B**) + **C** = **A** + (**B** + **C**)
- •**Distributivity**: c(**A** + **B**) = c**A** + c**B**
- •**Zero matrix** **0**: **A** + **0** = **A**
- •**Additive inverse**: **A** + (−**A**) = **0**

### Practical shape checklist

Before adding or scaling, check:

- •**A** + **B**: requires same m and n.
- •c**A**: always OK; shape unchanged.

You’ll rely on this habit when you start solving linear systems and doing matrix calculus.

## Core Mechanic 2: Matrix Multiplication (Composition of Linear Maps)

### Why multiplication is defined the way it is

Matrix multiplication is not “entry-by-entry.” It is designed so that multiplying matrices corresponds to **composing linear transformations**.

If **B** maps ℝᵖ → ℝⁿ and **A** maps ℝⁿ → ℝᵐ, then doing **B** first and then **A** is a map

ℝᵖ → ℝᵐ

Matrix multiplication encodes exactly that:

(**A****B**)**x** = **A**(**B****x**)

So the order matters: **A****B** means “apply **B**, then apply **A**.”

### Shape rule (the first gate)

If **A** ∈ ℝᵐˣⁿ and **B** ∈ ℝⁿˣᵖ, then the product **A****B** is defined and has shape ℝᵐˣᵖ.

The “inner” dimensions must match (n).

A quick mnemonic:

(m×n)·(n×p) = (m×p)

### Entry rule (row-by-column)

For **C** = **A****B**, the entry cᵢⱼ is

cᵢⱼ = ∑ₖ₌₁ⁿ aᵢₖ bₖⱼ

Interpretation: take row i of **A** and column j of **B**, multiply matching entries, and sum.

### Same rule, but with vectors (often clearer)

Let **bⱼ** be the j-th column of **B**. Then the j-th column of **C** = **A****B** is

(**A****B**)ⱼ = **A****bⱼ**

So multiplying on the left by **A** means: apply **A** to each column of **B**.

This is a powerful viewpoint:

- •Columns of **B** are inputs.
- •**A** transforms each input into an output.
- •The outputs become columns of **A****B**.

### Multiplication is not commutative

In general:

**A****B** ≠ **B****A**

Because composition of functions is not commutative.

Even when both products exist (both are square of same size), they can differ.

### Associativity (composition works in chains)

If shapes match so everything is defined:

(**A****B**)**C** = **A**(**B****C**)

This matters because it lets you write **A****B****C** without parentheses (the product is unambiguous).

### Distributivity over addition

If shapes match:

**A**(**B** + **C**) = **A****B** + **A****C**

(**A** + **B**)**C** = **A****C** + **B****C**

### Identity matrix (the “do nothing” transformation)

The identity matrix **I**ₙ ∈ ℝⁿˣⁿ satisfies

**I**ₙ **x** = **x** for all **x** ∈ ℝⁿ

And for any compatible matrix **A**:

**I**ₘ **A** = **A**, **A****I**ₙ = **A**

### A small transformation picture (ℝ² → ℝ²)

Suppose **A** scales x by 2 and y by 1:

**A** = [ [2, 0],

[0, 1] ]

Suppose **B** swaps x and y:

**B** = [ [0, 1],

[1, 0] ]

Then **A****B** means “swap, then scale.” **B****A** means “scale, then swap.” Those are different operations, so the matrices differ.

### Summary table: addition vs multiplication

| Operation | When defined? | Rule | Transformation meaning |
| --- | --- | --- | --- |
| **A** + **B** | same shape m×n | (aᵢⱼ + bᵢⱼ) | add outputs: (**A**+**B**)**x** = **A****x** + **B****x** |
| c**A** | always | (c·aᵢⱼ) | scale outputs: (c**A**)**x** = c(**A****x**) |
| **A****B** | (m×n)(n×p) | cᵢⱼ = ∑ aᵢₖbₖⱼ | compose maps: (**A****B**)**x** = **A**(**B****x**) |

## Core Mechanic 3: Transpose (Swap Rows and Columns)

### Why transpose matters

Transpose looks simple—flip across the diagonal—but it appears everywhere:

- •It converts between row and column perspectives.
- •It is essential for dot products in matrix form (e.g., **x**ᵀ**y**).
- •It’s used constantly in optimization, least squares, and machine learning.

### Definition

If **A** ∈ ℝᵐˣⁿ, then **A**ᵀ ∈ ℝⁿˣᵐ and

(**A**ᵀ)ᵢⱼ = aⱼᵢ

So rows become columns.

Example:

**A** = [ [1, 2, 3],

[4, 5, 6] ] (2×3)

**A**ᵀ = [ [1, 4],

[2, 5],

[3, 6] ] (3×2)

### Key identities (worth memorizing)

These are not just algebra tricks; they encode how “flipping” interacts with other operations.

1) Double transpose returns the original:

(**A**ᵀ)ᵀ = **A**

2) Transpose distributes over addition and scalar multiplication:

(**A** + **B**)ᵀ = **A**ᵀ + **B**ᵀ

(c**A**)ᵀ = c**A**ᵀ

3) Transpose reverses multiplication order:

(**A****B**)ᵀ = **B**ᵀ **A**ᵀ

This one is extremely important.

### Showing the work for (**A****B**)ᵀ = **B**ᵀ**A**ᵀ

Let **A** ∈ ℝᵐˣⁿ, **B** ∈ ℝⁿˣᵖ.

Consider entry (i, j) of (**A****B**)ᵀ.

((**A****B**)ᵀ)ᵢⱼ

= (**A****B**)ⱼᵢ

= ∑ₖ₌₁ⁿ aⱼₖ bₖᵢ

Now look at (**B**ᵀ**A**ᵀ)ᵢⱼ. Here **B**ᵀ ∈ ℝᵖˣⁿ and **A**ᵀ ∈ ℝⁿˣᵐ, so the product is ℝᵖˣᵐ, matching.

(**B**ᵀ**A**ᵀ)ᵢⱼ

= ∑ₖ₌₁ⁿ (bᵀ)ᵢₖ (aᵀ)ₖⱼ

= ∑ₖ₌₁ⁿ bₖᵢ aⱼₖ

= ∑ₖ₌₁ⁿ aⱼₖ bₖᵢ

So the entries match for all i, j ⇒ the matrices are equal.

### Transpose and vectors

For a column vector **x** ∈ ℝⁿ, **x**ᵀ is a 1×n row vector.

Dot product in matrix notation:

**x**ᵀ**y** = ∑ᵢ xᵢ yᵢ

This is a bridge between “vector algebra” and “matrix algebra.”

## Application/Connection: Matrices as Tools for Systems, Geometry, and Data

### 1) Systems of linear equations

A system like

2x + y = 5

−x + 3y = 1

can be written as **A****x** = **b** with

**A** = [ [2, 1],

[−1, 3] ], **x** = [x, y]ᵀ, **b** = [5, 1]ᵀ

Then solving the system means finding **x** such that **A****x** matches **b**.

This node prepares you for Gaussian elimination and matrix methods in [Systems of Linear Equations](/tech-tree/linear-systems/).

### 2) Geometry: transforming space

In ℝ², a matrix can represent:

- •scaling (stretch/compress)
- •reflection
- •shear
- •rotation (with special matrices)

The column view is especially geometric: the columns of **A** are where the basis vectors go.

If **e₁** = [1,0]ᵀ and **e₂** = [0,1]ᵀ, then

**A****e₁** = first column of **A**

**A****e₂** = second column of **A**

So **A** is fully determined by where it sends the basis.

### 3) Composition = pipelines

If **B** does “normalize then mix features” and **A** does “project to a smaller space,” then **A****B** is the combined pipeline.

This viewpoint shows up in ML models and in the [Jacobian](/tech-tree/jacobian/), where derivatives themselves form matrices and are multiplied via chain rule (composition).

### 4) Transpose in data problems

If a data matrix **X** stores examples in rows (common) versus columns (also common), transpose switches conventions.

- •Rows-as-examples: **X** ∈ ℝᴺˣᵈ (N examples, d features)
- •Columns-as-examples: **X**ᵀ ∈ ℝᵈˣᴺ

Transpose lets formulas remain consistent even when you change how you store data.

### 5) Where this node leads

Once you’re fluent in these operations, many “next” ideas become more natural:

- •[Determinants](/tech-tree/determinants/): understand singular vs invertible transformations.
- •[Matrix Calculus](/tech-tree/matrix-calculus/): gradients/Jacobians use transpose constantly.
- •[Game Theory Introduction](/tech-tree/game-theory-intro/): payoff matrices and mixed strategies rely on matrix-vector multiplication.

Matrices are not just notation; they are a compact language for linear structure.

## Worked Examples (3)

### Add and scale matrices (componentwise) and interpret as transformations

Let **A** = [[1, −2], [0, 3]] and **B** = [[4, 1], [−1, 2]]. Compute **C** = 2**A** + **B**. Then verify on a vector **x** = [1, 2]ᵀ that **C****x** = 2(**A****x**) + **B****x**.

1. Compute 2**A** entrywise:

   2**A** = [[2·1, 2·(−2)], [2·0, 2·3]] = [[2, −4], [0, 6]].
2. Add **B** entrywise:

   **C** = 2**A** + **B**

   = [[2+4, −4+1], [0+(−1), 6+2]]

   = [[6, −3], [−1, 8]].
3. Compute **A****x**:

   **A****x** = [[1, −2], [0, 3]] [1, 2]ᵀ

   = [1·1 + (−2)·2, 0·1 + 3·2]ᵀ

   = [1 − 4, 6]ᵀ

   = [−3, 6]ᵀ.
4. Compute 2(**A****x**) = 2[−3, 6]ᵀ = [−6, 12]ᵀ.
5. Compute **B****x**:

   **B****x** = [[4, 1], [−1, 2]] [1, 2]ᵀ

   = [4·1 + 1·2, (−1)·1 + 2·2]ᵀ

   = [6, 3]ᵀ.
6. Add outputs:

   2(**A****x**) + **B****x** = [−6, 12]ᵀ + [6, 3]ᵀ = [0, 15]ᵀ.
7. Compute **C****x** directly:

   **C****x** = [[6, −3], [−1, 8]] [1, 2]ᵀ

   = [6·1 + (−3)·2, (−1)·1 + 8·2]ᵀ

   = [6 − 6, −1 + 16]ᵀ

   = [0, 15]ᵀ.
8. Conclude **C****x** = 2(**A****x**) + **B****x**, matching the transformation interpretation.

**Insight:** Matrix addition/scaling are designed so that adding/scaling matrices corresponds exactly to adding/scaling the outputs of the linear transformations they represent.

### Matrix multiplication as composition (and why order matters)

Let **A** = [[2, 0], [0, 1]] (scale x by 2) and **B** = [[0, 1], [1, 0]] (swap coordinates). Compute **A****B** and **B****A**, and test on **x** = [3, 5]ᵀ.

1. Compute **A****B** using row-by-column:

   **A****B** = [[2, 0], [0, 1]] [[0, 1], [1, 0]]

   First row vs columns:

   c₁₁ = 2·0 + 0·1 = 0

   c₁₂ = 2·1 + 0·0 = 2

   Second row vs columns:

   c₂₁ = 0·0 + 1·1 = 1

   c₂₂ = 0·1 + 1·0 = 0

   So **A****B** = [[0, 2], [1, 0]].
2. Compute **B****A**:

   **B****A** = [[0, 1], [1, 0]] [[2, 0], [0, 1]]

   First row:

   d₁₁ = 0·2 + 1·0 = 0

   d₁₂ = 0·0 + 1·1 = 1

   Second row:

   d₂₁ = 1·2 + 0·0 = 2

   d₂₂ = 1·0 + 0·1 = 0

   So **B****A** = [[0, 1], [2, 0]].
3. Observe **A****B** ≠ **B****A**.
4. Test on **x** = [3, 5]ᵀ:

   **B****x** = [5, 3]ᵀ (swap)

   **A**(**B****x**) = **A**[5, 3]ᵀ = [10, 3]ᵀ

   So (**A****B**)**x** = [10, 3]ᵀ.
5. Other order:

   **A****x** = [6, 5]ᵀ (scale x)

   **B**(**A****x**) = **B**[6, 5]ᵀ = [5, 6]ᵀ

   So (**B****A**)**x** = [5, 6]ᵀ.

**Insight:** Matrix multiplication encodes composition: **A****B** means “do **B** first, then **A**.” Different order ⇒ different transformation.

### Transpose properties, including reversing multiplication order

Let **A** = [[1, 2, 0], [−1, 3, 4]] (2×3) and **B** = [[2, 1], [0, −1], [5, 2]] (3×2). Compute (**A****B**)ᵀ and compare with **B**ᵀ**A**ᵀ.

1. Check shapes:

   **A** is 2×3 and **B** is 3×2, so **A****B** is 2×2 and transpose will be 2×2.
2. Compute **A****B**:

   **A****B** = [[1, 2, 0], [−1, 3, 4]] [[2, 1], [0, −1], [5, 2]]

   Entry (1,1): 1·2 + 2·0 + 0·5 = 2

   Entry (1,2): 1·1 + 2·(−1) + 0·2 = 1 − 2 = −1

   Entry (2,1): (−1)·2 + 3·0 + 4·5 = −2 + 20 = 18

   Entry (2,2): (−1)·1 + 3·(−1) + 4·2 = −1 − 3 + 8 = 4

   So **A****B** = [[2, −1], [18, 4]].
3. Transpose it:

   (**A****B**)ᵀ = [[2, 18], [−1, 4]].
4. Compute **B**ᵀ and **A**ᵀ:

   **B**ᵀ = [[2, 0, 5], [1, −1, 2]] (2×3)

   **A**ᵀ = [[1, −1], [2, 3], [0, 4]] (3×2).
5. Multiply **B**ᵀ**A**ᵀ (2×3)(3×2) = 2×2:

   Entry (1,1): [2,0,5]·[1,2,0]ᵀ = 2·1 + 0·2 + 5·0 = 2

   Entry (1,2): [2,0,5]·[−1,3,4]ᵀ = 2·(−1) + 0·3 + 5·4 = −2 + 20 = 18

   Entry (2,1): [1,−1,2]·[1,2,0]ᵀ = 1·1 + (−1)·2 + 2·0 = −1

   Entry (2,2): [1,−1,2]·[−1,3,4]ᵀ = 1·(−1) + (−1)·3 + 2·4 = −1 − 3 + 8 = 4

   So **B**ᵀ**A**ᵀ = [[2, 18], [−1, 4]].
6. Compare:

   (**A****B**)ᵀ = **B**ᵀ**A**ᵀ.

**Insight:** Transpose flips multiplication order because it swaps the roles of rows and columns; the entrywise sum ∑ aᵢₖbₖⱼ becomes the same sum but viewed from the other side.

## Key Takeaways

- ✓

  A matrix **A** ∈ ℝᵐˣⁿ represents a linear transformation ℝⁿ → ℝᵐ via **x** ↦ **A****x**.
- ✓

  Column view: **A****x** = x₁**a₁** + … + xₙ**aₙ** (a linear combination of columns of **A**).
- ✓

  Matrix addition and scalar multiplication are componentwise and correspond to adding/scaling transformation outputs.
- ✓

  Matrix multiplication is defined to match composition: (**A****B**)**x** = **A**(**B****x**).
- ✓

  Shape rule for multiplication: (m×n)(n×p) = (m×p); inner dimensions must match.
- ✓

  Multiplication is generally not commutative: **A****B** ≠ **B****A**.
- ✓

  Transpose swaps rows and columns: (**A**ᵀ)ᵢⱼ = aⱼᵢ, and (**A****B**)ᵀ = **B**ᵀ**A**ᵀ.

## Common Mistakes

- ✗

  Trying to add matrices of different shapes (e.g., 2×3 plus 3×2).
- ✗

  Assuming matrix multiplication is commutative because scalar multiplication is (it usually isn’t).
- ✗

  Forgetting the shape rule and multiplying in an invalid order (or expecting the wrong output size).
- ✗

  Thinking multiplication is entrywise (it’s row-by-column sums, designed for composition).

## Practice

easy

Let **A** = [[3, −1], [2, 4]] and **B** = [[0, 5], [−2, 1]]. Compute **A** + **B** and 3**A** − 2**B**.

**Hint:** Addition/subtraction and scalar multiplication are componentwise. Do 3**A** and 2**B** first, then subtract.

Show solution

**A** + **B** = [[3+0, −1+5], [2+(−2), 4+1]] = [[3, 4], [0, 5]].

3**A** = [[9, −3], [6, 12]]

2**B** = [[0, 10], [−4, 2]]

3**A** − 2**B** = [[9−0, −3−10], [6−(−4), 12−2]] = [[9, −13], [10, 10]].

medium

Let **A** be 2×3 and **B** be 3×4. (a) What is the shape of **A****B**? (b) Is **B****A** defined? If it is, what would its shape be?

**Hint:** Use (m×n)(n×p) = (m×p). For **B****A**, the inner dimensions would be 4 and 2—do they match?

Show solution

(a) **A****B** has shape (2×3)(3×4) = 2×4.

(b) **B****A** would require (3×4)(2×3), but the inner dimensions 4 and 2 do not match, so **B****A** is not defined.

hard

Given **A** = [[1, 2], [3, 4]] and **B** = [[2, 0], [1, −1]], compute (**A****B**)ᵀ and **B**ᵀ**A**ᵀ to verify (**A****B**)ᵀ = **B**ᵀ**A**ᵀ.

**Hint:** First compute **A****B** (2×2). Then transpose. Separately compute **B**ᵀ and **A**ᵀ and multiply in that order.

Show solution

**A****B** = [[1,2],[3,4]] [[2,0],[1,−1]]

= [[1·2+2·1, 1·0+2·(−1)], [3·2+4·1, 3·0+4·(−1)]]

= [[4, −2], [10, −4]].

(**A****B**)ᵀ = [[4, 10], [−2, −4]].

**B**ᵀ = [[2,1],[0,−1]], **A**ᵀ = [[1,3],[2,4]].

**B**ᵀ**A**ᵀ = [[2,1],[0,−1]] [[1,3],[2,4]]

= [[2·1+1·2, 2·3+1·4], [0·1+(−1)·2, 0·3+(−1)·4]]

= [[4, 10], [−2, −4]].

They match, so (**A****B**)ᵀ = **B**ᵀ**A**ᵀ.

## Connections

Next nodes you’re ready for:

- •[Systems of Linear Equations](/tech-tree/linear-systems/): rewrite systems as **A****x** = **b** and solve.
- •[Determinants](/tech-tree/determinants/): understand when a square transformation is invertible (det ≠ 0).
- •[Jacobian](/tech-tree/jacobian/): matrices of partial derivatives; chain rule becomes matrix multiplication.
- •[Matrix Calculus](/tech-tree/matrix-calculus/): gradients, Jacobians, Hessians; transpose appears constantly.
- •[Game Theory Introduction](/tech-tree/game-theory-intro/): payoff matrices and expected utilities via matrix-vector products.

Quality: B (4.2/5)

[← back to tree](/tech-tree/)[browse all →](/tech-tree/inventory/)
