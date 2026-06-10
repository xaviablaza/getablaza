---
title: Basis and Dimension
description: Minimal spanning set. Number of vectors in a basis.
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
permalink: /tech-tree/basis-dimension/
---

[←Back to Tech Tree](/tech-tree/)

[inventory](/tech-tree/inventory/)[coverage](/tech-tree/coverage/)

# Basis and Dimension

Linear AlgebraDifficulty: ★★☆☆☆Depth: 4Unlocks: 10

Minimal spanning set. Number of vectors in a basis.

## Interactive Visualization

⏮◀◀▶▶STEP0.25x1xZOOM

t=0s

## Core Concepts

- -Spanning set: a set whose linear combinations equal the whole vector space
- -Basis: a set that is both spanning and linearly independent (equivalently a minimal spanning set)
- -Dimension (finite): the number of vectors in a basis; a space is finite-dimensional if some basis is finite

## Key Symbols & Notation

span(S) - denotes the set of all linear combinations of S (the span of S)dim(V) - denotes the dimension, the number of vectors in any basis of V

## Essential Relationships

- -All bases of a finite-dimensional vector space have the same number of vectors; that common number is dim(V)

## Prerequisites (1)

[Linear Independence5 atoms](/tech-tree/linear-independence/)

## Unlocks (1)

[Orthogonalitylvl 3](/tech-tree/orthogonality/)

Advanced Learning Details

### Graph Position

34

Depth Cost

10

Fan-Out (ROI)

2

Bottleneck Score

4

Chain Length

### Cognitive Load

6

Atomic Elements

21

Total Elements

L0

Percentile Level

L4

Atomic Level

### All Concepts (7)

- - Spanning set: a set of vectors whose linear combinations produce every vector in the space
- - Minimal spanning set: a spanning set with no redundant vectors (removing any vector destroys the span)
- - Basis: a set that is both linearly independent and spanning
- - Dimension: the number (cardinality) of vectors in a basis; a numeric measure of the size of a vector space
- - Finite-dimensional vs. infinite-dimensional: whether a finite basis exists
- - Coordinate representation relative to a basis: expressing any vector uniquely as a linear combination of basis vectors
- - Empty basis / zero-dimensional space: the zero vector space has the empty set as a basis and dimension zero

### Teaching Strategy

Deep-dive lesson - accessible entry point but dense material. Use worked examples and spaced repetition.

If linear independence tells you “no redundancy,” then a basis answers the next question: “What’s the smallest set of directions I need to build everything in this space?” Dimension is the count of those directions.

TL;DR:

A set S spans a vector space V if every vector in V can be written as a linear combination of vectors in S. A basis is a set that is both spanning and linearly independent (equivalently: a minimal spanning set or a maximal independent set). In a finite-dimensional space, every basis has the same number of vectors; that number is dim(V).

## What Is Basis and Dimension?

### Why we care

When you work with vectors, you often want a **coordinate system**: a way to describe any vector using a list of numbers. A **basis** is exactly the information needed to create such a coordinate system—no more, no less.

- •**No more**: you don’t want redundant vectors that can be built from others.
- •**No less**: you still want to be able to build *every* vector in the space.

These two desires correspond to:

- •**Linear independence** (no redundancy)
- •**Spanning** (enough to reach everything)

A basis is the sweet spot that satisfies both.

### Spanning set (span)

Let S = {**v**₁, **v**₂, …, **v**ₖ} be a set of vectors in a vector space V.

The **span** of S, written span(S), is the set of all linear combinations:

span(S) = { a₁**v**₁ + a₂**v**₂ + … + aₖ**v**ₖ : a₁, …, aₖ are scalars }

If span(S) = V, then S is a **spanning set** of V.

Intuition: you can “mix” the vectors in S (by scaling and adding) to reach any vector in V.

### Basis

A set B ⊂ V is a **basis** of V if:

1) B spans V, and

2) B is linearly independent.

There are two equivalent ways to think about a basis that are often more practical:

- •**Minimal spanning set**: B spans V, and if you remove any vector from B, it no longer spans V.
- •**Maximal independent set**: B is linearly independent, and if you add any new vector from V to B, it becomes dependent.

These equivalences are not just “nice facts”—they explain *why* a basis is the “just right” set.

### Dimension

If V has a finite basis, then V is **finite-dimensional**.

The **dimension** of V, written dim(V), is the number of vectors in any basis of V.

A crucial theorem (we’ll use it as a guiding rule):

> In a finite-dimensional vector space, **every basis has the same number of vectors**.

So dim(V) is well-defined.

Examples you already know intuitively:

- •In ℝ², a typical basis has 2 vectors, so dim(ℝ²) = 2.
- •In ℝ³, a typical basis has 3 vectors, so dim(ℝ³) = 3.

But bases are not unique: ℝ² has infinitely many different bases, all with exactly 2 vectors.

## Core Mechanic 1: Spanning Sets and the Meaning of span(S)

### Why spanning matters before the formalism

Linear independence tells you whether vectors are redundant. But you can have a set with **no redundancy** that still doesn’t reach the whole space.

For example, in ℝ², the single vector (1, 0) is linearly independent (a single nonzero vector always is), but it cannot reach (0, 1). So it does not span ℝ².

Spanning is about **coverage**.

### What does it mean to span?

Let V be a vector space and S = {**v**₁, …, **v**ₖ} ⊂ V.

To say **w** ∈ span(S) means:

∃ scalars a₁, …, aₖ such that

**w** = a₁**v**₁ + a₂**v**₂ + … + aₖ**v**ₖ

So proving span(S) = V usually means:

- •Take an arbitrary vector **w** in V
- •Show you can solve for coefficients aᵢ to represent **w**

### A geometric picture (in ℝ² and ℝ³)

In ℝ²:

- •span({one nonzero vector}) is a **line through the origin**.
- •span({two non-parallel vectors}) is the **whole plane**.

In ℝ³:

- •span({one nonzero vector}) is a line.
- •span({two independent vectors}) is a plane through the origin.
- •span({three independent vectors}) is all of ℝ³.

This suggests a key theme:

> Adding independent vectors tends to increase the “reach” of the span.

### Spanning and solving linear systems

Suppose S = {**v**₁, …, **v**ₖ} in ℝⁿ. Put them as columns of a matrix:

A = [ **v**₁ **v**₂ … **v**ₖ ]

Then asking whether a vector **w** is in span(S) is the same as asking whether the linear system has a solution:

A**x** = **w**

And asking whether S spans ℝⁿ is the same as asking:

For every **w** ∈ ℝⁿ, does A**x** = **w** have a solution?

In ℝⁿ, this is equivalent to A having a pivot in every row (i.e., rank(A) = n). You don’t need full rank theory yet, but it’s useful to recognize the workflow: spanning is a “can we solve for coefficients?” question.

### Minimal spanning idea (preview)

If a spanning set has extra vectors, some are unnecessary. For example, in ℝ²:

S = {(1, 0), (0, 1), (1, 1)}

This spans ℝ², but it is not minimal: (1, 1) = (1, 0) + (0, 1), so removing it doesn’t break spanning.

This naturally motivates the definition of a basis as a **minimal spanning set**.

## Core Mechanic 2: Basis = Spanning + Independence (and Why Dimension Is a Count)

### Why independence must join spanning

A spanning set can be too large.

A linearly independent set can be too small.

A basis avoids both problems.

Let B = {**b**₁, …, **b**ₖ}.

- •If B spans V, then every **v** ∈ V can be expressed using B.
- •If B is independent, that expression is not “wasteful.” In fact, it leads to **uniqueness** of coordinates.

### Coordinates are unique in a basis

Suppose B is a basis of V and

**v** = a₁**b**₁ + … + aₖ**b**ₖ

and also

**v** = c₁**b**₁ + … + cₖ**b**ₖ

Subtract the two equations:

0 = (a₁ − c₁)**b**₁ + … + (aₖ − cₖ)**b**ₖ

Because B is linearly independent, the only linear combination giving 0 is the trivial one:

(a₁ − c₁) = 0, …, (aₖ − cₖ) = 0

So aᵢ = cᵢ for all i.

**Conclusion:** the representation of **v** in a basis is unique.

This is the practical reason bases matter: they give a stable coordinate system.

### Basis as minimal spanning set (why equivalent)

Assume B spans V and is linearly independent.

Take any **b**ⱼ ∈ B. If you remove it and still span V, then **b**ⱼ would be a linear combination of the remaining vectors (because the remaining vectors could build every vector, including **b**ⱼ). That would contradict independence.

So removing any vector breaks spanning.

Hence:

Spanning + independence ⇒ minimal spanning.

Conversely, if a set spans V and is minimal (removing anything breaks spanning), then it must be independent. Otherwise one vector would be a linear combination of the others, and removing it would not change the span—contradiction.

So:

Basis ⇔ minimal spanning set.

### Dimension: why it’s consistent

Dimension is defined as:

dim(V) = number of vectors in any basis of V.

But why does this not depend on which basis you pick?

The key fact is:

> In a finite-dimensional vector space, all bases have the same number of vectors.

A useful intuition (not a full proof):

- •A linearly independent set cannot have “more directions” than a spanning set can support.
- •In ℝⁿ, you cannot have more than n independent vectors.

More generally, there is an important relationship:

> In a finite-dimensional vector space V, every linearly independent set has size ≤ any spanning set.

So if B and C are both bases, then:

- •B is independent, C spans ⇒ |B| ≤ |C|
- •C is independent, B spans ⇒ |C| ≤ |B|

Therefore |B| = |C|.

That shared size is dim(V).

### Quick dimension facts you’ll use constantly

- •dim(ℝⁿ) = n.
- •Any set of more than dim(V) vectors in V is automatically linearly dependent.
- •Any spanning set in V must have at least dim(V) vectors.
- •In a k-dimensional space, a set of k vectors is a basis **iff** it is independent (equivalently: **iff** it spans). This is a powerful shortcut.

We’ll use these in examples and exercises.

## Application/Connection: How Basis and Dimension Power Other Ideas

### Choosing a basis is choosing a coordinate system

Once you pick a basis B = {**b**₁, …, **b**ₖ}, every vector **v** has unique coordinates (a₁, …, aₖ) such that:

**v** = ∑ᵢ aᵢ **b**ᵢ

Those coordinates depend on the basis, but the vector **v** does not.

This viewpoint becomes essential when you:

- •change coordinates (basis change)
- •represent linear transformations as matrices
- •compute projections and decompositions

### Why dimension shows up everywhere

Dimension controls what is possible:

- •In dim 2, two independent vectors are enough to span.
- •In dim 3, you need three independent vectors to span.
- •In higher dimensions, the same pattern holds.

It also tells you when redundancy must exist:

- •In ℝ³, any 4 vectors must be dependent.

This becomes the backbone of many later tools.

### Bridge to orthogonality (what you unlock next)

An **orthonormal basis** is a basis whose vectors are mutually perpendicular (orthogonal) and have length 1.

Why is that special?

- •Coordinates become easy to compute using dot products.
- •Projections and least squares become clean.

But orthogonality only makes sense once you understand what a basis is and why dimension fixes how many basis vectors you need.

So this node sets up the question for the next one:

> “Can we choose a basis with extra geometric structure (perpendicular, unit length) to make computations simpler?”

That is exactly what [Orthogonality](/tech-tree/orthogonality/) addresses.

## Worked Examples (3)

### Find span(S) and decide if S is a basis of ℝ²

Let S = { **v**₁, **v**₂ } with **v**₁ = (1, 2) and **v**₂ = (2, 4) in ℝ². Determine span(S). Is S a basis of ℝ²?

1. Observe that **v**₂ is a multiple of **v**₁:

   **v**₂ = (2, 4) = 2(1, 2) = 2**v**₁.
2. So any linear combination of **v**₁ and **v**₂ looks like:

   a**v**₁ + b**v**₂ = a**v**₁ + b(2**v**₁)

   = (a + 2b)**v**₁.
3. Therefore span(S) = span({**v**₁}). Geometrically, this is a line through the origin in direction (1, 2).
4. Because S is linearly dependent (one vector is a multiple of the other), it cannot be a basis.
5. Also, span(S) is only a line, not all of ℝ², so S does not span ℝ² either.

**Insight:** Two vectors in ℝ² only form a basis if they are not scalar multiples. Dependence collapses the span to a lower-dimensional subspace.

### Show a set spans ℝ³ by solving for coefficients

Let B = { **b**₁, **b**₂, **b**₃ } in ℝ³ where **b**₁ = (1, 0, 1), **b**₂ = (0, 1, 1), **b**₃ = (1, 1, 0). Show B spans ℝ³ by expressing an arbitrary **w** = (x, y, z) as a linear combination of B.

1. We want scalars a, b, c such that:

   a**b**₁ + b**b**₂ + c**b**₃ = (x, y, z).
2. Write the linear combination component-wise:

   a(1,0,1) + b(0,1,1) + c(1,1,0)

   = (a + c, b + c, a + b).
3. Set equal to (x, y, z) to get the system:

   a + c = x

   b + c = y

   a + b = z
4. Solve step-by-step.

   From a + c = x ⇒ a = x − c.

   From b + c = y ⇒ b = y − c.
5. Plug into a + b = z:

   (x − c) + (y − c) = z

   x + y − 2c = z

   −2c = z − x − y

   c = (x + y − z)/2.
6. Back-substitute:

   a = x − (x + y − z)/2 = (2x − x − y + z)/2 = (x − y + z)/2

   b = y − (x + y − z)/2 = (2y − x − y + z)/2 = (−x + y + z)/2.
7. We found a, b, c for an arbitrary (x, y, z). Therefore every vector in ℝ³ lies in span(B), so span(B) = ℝ³.

**Insight:** To prove a set spans, take an arbitrary vector and solve for coefficients. If you can always solve (with no restrictions on x, y, z), the set spans the whole space.

### Use dimension shortcuts in a subspace of ℝ³

Let V = { (x, y, z) ∈ ℝ³ : x + y + z = 0 }. Consider **u**₁ = (1, −1, 0) and **u**₂ = (1, 0, −1). Show {**u**₁, **u**₂} is a basis of V and find dim(V).

1. First check **u**₁ and **u**₂ lie in V:

   For **u**₁: 1 + (−1) + 0 = 0 ⇒ **u**₁ ∈ V.

   For **u**₂: 1 + 0 + (−1) = 0 ⇒ **u**₂ ∈ V.
2. Check linear independence:

   Suppose a**u**₁ + b**u**₂ = **0**.

   Then a(1, −1, 0) + b(1, 0, −1) = (0,0,0).
3. Compute components:

   (a + b, −a, −b) = (0, 0, 0).
4. So −a = 0 ⇒ a = 0, and −b = 0 ⇒ b = 0. Therefore {**u**₁, **u**₂} is linearly independent.
5. Now show they span V:

   Take an arbitrary (x, y, z) ∈ V, so x + y + z = 0.

   We want a, b such that a**u**₁ + b**u**₂ = (x, y, z).
6. Solve:

   (a + b, −a, −b) = (x, y, z).

   From −a = y ⇒ a = −y.

   From −b = z ⇒ b = −z.

   Then a + b = −y − z.
7. But since x + y + z = 0, we have x = −y − z.

   So a + b = x is automatically satisfied.
8. Thus every vector in V can be expressed as a combination of **u**₁ and **u**₂, so they span V.
9. Therefore {**u**₁, **u**₂} is a basis of V, and dim(V) = 2.

**Insight:** Subspaces defined by one linear equation in ℝ³ often have dimension 2 (a plane through the origin). A basis gives you a concrete coordinate system on that plane.

## Key Takeaways

- ✓

  span(S) is the set of all linear combinations of vectors in S; S spans V when span(S) = V.
- ✓

  A basis is a set that is both spanning and linearly independent.
- ✓

  Basis ⇔ minimal spanning set ⇔ maximal linearly independent set (in finite-dimensional spaces).
- ✓

  In a basis, every vector has a unique coordinate representation.
- ✓

  dim(V) is the number of vectors in any basis of V; it is well-defined because all bases have the same size.
- ✓

  In a finite-dimensional space, any set with more than dim(V) vectors is linearly dependent.
- ✓

  In a k-dimensional space, a set of k vectors is a basis iff it is linearly independent (equivalently iff it spans).

## Common Mistakes

- ✗

  Thinking “spanning” means you can reach some vectors—spanning means you can reach **every** vector in the space.
- ✗

  Assuming any spanning set is a basis; spanning sets can have redundancy (dependence).
- ✗

  Forgetting that basis vectors must belong to the space V (especially for subspaces defined by constraints).
- ✗

  Believing different bases can have different sizes; in finite-dimensional spaces, all bases have the same number of vectors.

## Practice

easy

In ℝ², let S = { (1, 1), (1, −1) }. (a) Does S span ℝ²? (b) Is S a basis of ℝ²?

**Hint:** Try to solve a(1,1) + b(1,−1) = (x,y) for arbitrary x,y. Or check whether the vectors are scalar multiples.

Show solution

Solve a(1,1) + b(1,−1) = (x,y).

Component-wise: (a + b, a − b) = (x, y).

Add equations: (a + b) + (a − b) = x + y ⇒ 2a = x + y ⇒ a = (x + y)/2.

Subtract: (a + b) − (a − b) = x − y ⇒ 2b = x − y ⇒ b = (x − y)/2.

A solution exists for all x,y, so S spans ℝ². The two vectors are not multiples, so they are independent. Therefore S is a basis.

medium

Let V be the subspace of ℝ³ given by V = { (x, y, z) : z = 0 }. Find a basis for V and determine dim(V).

**Hint:** Vectors in V look like (x, y, 0). Try to express (x, y, 0) using two simple vectors.

Show solution

Any (x, y, 0) can be written as x(1,0,0) + y(0,1,0). So { (1,0,0), (0,1,0) } spans V. These two vectors are linearly independent, hence they form a basis. Therefore dim(V) = 2.

hard

Let S = { (1,0,0), (0,1,0), (1,1,0) } in ℝ³. (a) Find span(S). (b) Is S a basis of span(S)? (c) Find a basis of span(S) with fewer vectors.

**Hint:** All vectors have z = 0. Also, check whether (1,1,0) is a linear combination of the first two vectors.

Show solution

(a) Every linear combination of S has the form a(1,0,0) + b(0,1,0) + c(1,1,0) = (a + c, b + c, 0). This is any vector (x,y,0), so span(S) = { (x,y,0) } (the z=0 plane).

(b) S is not a basis of span(S) because it is linearly dependent: (1,1,0) = (1,0,0) + (0,1,0).

(c) A basis with fewer vectors is { (1,0,0), (0,1,0) }. It spans the same set and is independent.

## Connections

Next, you’ll use bases with special geometric structure: [Orthogonality](/tech-tree/orthogonality/). Related foundations include linear independence (prerequisite) and upcoming ideas like change of basis and matrix representations of linear maps (future nodes).

- •[Orthogonality](/tech-tree/orthogonality/)
- •[Linear Independence](/tech-tree/linear-independence/)

Quality: B (4.1/5)

[← back to tree](/tech-tree/)[browse all →](/tech-tree/inventory/)
