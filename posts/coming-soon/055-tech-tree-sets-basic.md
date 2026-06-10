---
title: Sets
description: Collections of distinct objects. Union, intersection, complement operations.
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
permalink: /tech-tree/sets-basic/
---

[←Back to Tech Tree](/tech-tree/)

[inventory](/tech-tree/inventory/)[coverage](/tech-tree/coverage/)

# Sets

Discrete MathDifficulty: ★☆☆☆☆Depth: 0Unlocks: 35

Collections of distinct objects. Union, intersection, complement operations.

## Interactive Visualization

⏮◀◀▶▶STEP0.25x1xZOOM

t=0s

## Core Concepts

- -Set: a collection of distinct objects (called elements)
- -Membership: an object either belongs to a set or does not (the idea of 'being an element of')
- -Set operations as core constructors: forming new sets from old ones (union, intersection, complement)

## Key Symbols & Notation

element-of (written as 'in')subset-or-equal (written as 'subseteq')

## Essential Relationships

- -Membership-based definitions: membership determines operations and inclusion - x is in A union B iff x is in A or in B; x is in A intersect B iff x is in A and in B; A subseteq B iff every element of A is an element of B; the complement of A consists of elements (in a specified universe) that are not in A.

## Unlocks (4)

[Graphs Introductionlvl 1](/tech-tree/graphs-basic/)[Vector Spaceslvl 2](/tech-tree/vector-spaces/)[Relationslvl 2](/tech-tree/relations/)[Measure Theorylvl 5](/tech-tree/measure-theory/)

Advanced Learning Details

### Graph Position

6

Depth Cost

35

Fan-Out (ROI)

14

Bottleneck Score

0

Chain Length

### Cognitive Load

6

Atomic Elements

56

Total Elements

L4

Percentile Level

L4

Atomic Level

### All Concepts (20)

- - set - an unordered collection of distinct elements
- - element/member - an individual object that may belong to a set
- - distinctness/uniqueness - duplicates are ignored (multisets differ from sets)
- - order irrelevance - the order of listing elements does not change the set
- - empty set - the set containing no elements
- - singleton - a set with exactly one element
- - finite vs infinite set - whether the set has a finite number of elements
- - subset - a set all of whose elements are also elements of another set
- - proper subset - a subset that is strictly smaller (not equal) to the other set
- - universal set - the implicit domain of discourse used when taking complements
- - set equality - two sets are equal when they contain exactly the same elements
- - membership vs subset distinction - difference between 'x ∈ A' and 'X ⊆ A' (where X is a set)
- - union operation - forming a set containing elements that are in either set
- - intersection operation - forming a set containing elements common to both sets
- - complement operation - elements of the universal set not in the given set
- - set difference - elements of one set that are not in another
- - power set - the set of all subsets of a given set
- - cardinality - the number of elements in a (finite) set
- - disjoint sets - sets whose intersection is the empty set
- - roster/list notation vs set-builder notation - ways to describe sets

### Teaching Strategy

Deep-dive lesson - accessible entry point but dense material. Use worked examples and spaced repetition.

Sets are the language of “which things are we talking about?” In discrete math, computer science, and probability, you constantly build, compare, and combine collections—and sets give you precise tools to do that without ambiguity.

TL;DR:

A set is a collection of distinct objects called elements. Use x ∈ A to mean “x is in A”, A ⊆ B to mean “A is a subset of B”. Core operations build new sets from old ones: union (A ∪ B), intersection (A ∩ B), and complement (Aᶜ, relative to a universe U).

## What Is a Set?

### Why sets exist (motivation)

In everyday language we often talk about groups of things:

- •“The students in this class”
- •“All prime numbers”
- •“The files in this folder”

But everyday language can be vague. Sets give a **clean, mathematical way** to specify *exactly* what belongs and what does not.

A big idea here is that sets are about **membership**—a yes/no question:

- •Either an object is in the set, or it isn’t.

### Definition

A **set** is a collection of **distinct** objects called **elements**.

If an object x is an element of set A, we write:

- •x ∈ A

If x is not an element of A:

- •x ∉ A

### Distinct elements (no duplicates)

A set does **not** track multiplicity. So:

- •{1, 1, 2} is the same set as {1, 2}

This is different from structures like **lists/arrays** (which can have repeats and order).

### Order does not matter

For sets, order is irrelevant:

- •{a, b, c} = {c, b, a}

### Common ways to describe sets

1) **Roster notation** (explicit elements):

- •A = {2, 4, 6, 8}

2) **Set-builder notation** (a rule):

- •E = {x ∈ ℤ : x is even}

Read “:” as “such that”.

3) **By description** (informal, but you should be able to translate it):

- •“The set of vowels in English” = {a, e, i, o, u}

### The universe U and why it matters

Many operations (especially complement) depend on what “all possible elements” are. We often declare a **universe** U.

Example:

- •Let U = {1, 2, 3, 4, 5}
- •Let A = {2, 5}

Now the complement of A depends on U (we’ll define complement soon).

### Comparing sets vs. other CS objects

| Structure | Allows duplicates? | Order matters? | Typical use |
| --- | --- | --- | --- |
| Set | No | No | Membership queries, combining collections |
| List/Array | Yes | Yes | Sequences, indexing |
| Multiset/Bag | Yes | No | Counting items without order |

This node focuses on **sets** and their basic operations.

## Membership and Subsets (⊆): Saying “Contained In” Precisely

### Why this matters

Before you combine sets, you need a way to:

1) Ask whether a specific element belongs (membership)

2) Compare whole sets (subset)

These are the backbone of definitions in later topics:

- •Graphs: edge set E is a set of pairs
- •Relations: a relation is a subset of a Cartesian product
- •Vector spaces: a vector space is a set with extra structure

### Membership

Membership is a statement like:

- •3 ∈ {1, 2, 3}
- •0 ∉ ℕ (if ℕ is defined as {1, 2, 3, …})

Notice the small but important point: you must know the intended meaning of ℕ, ℤ, ℚ, ℝ in your course or text.

### Subset

We write:

- •A ⊆ B

and read it as:

- •“A is a subset of B” or “A is contained in B”.

Meaning:

- •Every element of A is also an element of B.

Formally:

- •A ⊆ B ⇔ ∀x (x ∈ A ⇒ x ∈ B)

This definition is worth slowing down for. It says: *take any x; if x is in A, then it must be in B.*

### Equality of sets

Two sets are equal when they contain exactly the same elements:

- •A = B ⇔ (A ⊆ B) ∧ (B ⊆ A)

This is a common proof pattern: to show sets are equal, prove **two subset relations**.

### Proper subset

Sometimes we want “A is contained in B, but not equal.” This is a **proper subset**:

- •A ⊂ B

Meaning:

- •A ⊆ B and A ≠ B

(Notation varies: some books use ⊊ for proper subset and reserve ⊂ for subset-or-equal. In this lesson, ⊆ is subset-or-equal as requested.)

### The empty set ∅

The empty set has no elements:

- •∅ = { }

A key fact:

- •∅ ⊆ A for every set A

Why? Use the definition:

- •∅ ⊆ A ⇔ ∀x (x ∈ ∅ ⇒ x ∈ A)

But x ∈ ∅ is never true, so the implication “false ⇒ anything” is true. So the statement holds.

This can feel slippery at first, but it becomes very useful later.

### Common set symbols you’ll see

| Symbol | Meaning | Example |
| --- | --- | --- |
| ∈ | element of | 2 ∈ {1,2,3} |
| ∉ | not an element of | 4 ∉ {1,2,3} |
| ⊆ | subset or equal | {1,2} ⊆ {1,2,3} |
| ∅ | empty set | ∅ ⊆ A |

### A gentle “logic bridge”

Sets and logic are tightly related. Notice how subset uses ⇒ and ∀. This is your first hint that discrete math is often “logic + structures”.

## Core Set Operations (∪, ∩, Complement): Building New Sets from Old Ones

### Why operations matter

Once you can describe sets, you want to **construct** new ones:

- •Combine permissions: users with role A **or** role B
- •Filter data: items that satisfy condition 1 **and** condition 2
- •Exclude cases: everything **except** the invalid values

Set operations are the math version of these moves.

We’ll assume a fixed universe U when talking about complements.

---

## Union: A ∪ B

**Union** collects elements that are in A or in B (or both).

Definition:

- •A ∪ B = {x : x ∈ A ∨ x ∈ B}

Example:

- •A = {1, 2, 3}
- •B = {3, 4}
- •A ∪ B = {1, 2, 3, 4}

Notice: 3 appears once (sets don’t duplicate).

---

## Intersection: A ∩ B

**Intersection** collects elements that are in both A and B.

Definition:

- •A ∩ B = {x : x ∈ A ∧ x ∈ B}

Example:

- •A = {1, 2, 3}
- •B = {3, 4}
- •A ∩ B = {3}

If there is no overlap:

- •A ∩ B = ∅

---

## Complement: Aᶜ (relative to U)

The **complement** means “everything in the universe that is not in A.”

Definition (relative complement in U):

- •Aᶜ = U \ A = {x ∈ U : x ∉ A}

Example:

- •U = {1, 2, 3, 4, 5}
- •A = {2, 5}
- •Aᶜ = {1, 3, 4}

This is why the universe matters: if U changes, Aᶜ changes.

---

## Difference: A \ B (often used with complements)

Not required by the node description, but it’s a common companion.

Definition:

- •A \ B = {x : x ∈ A ∧ x ∉ B}

Example:

- •{1,2,3} \ {3,4} = {1,2}

And note:

- •A \ B = A ∩ Bᶜ (when complements are relative to the same U)

---

## Key laws (you don’t need to memorize all yet, but recognize them)

These are “algebra rules” for sets.

### Commutative

- •A ∪ B = B ∪ A
- •A ∩ B = B ∩ A

### Associative

- •(A ∪ B) ∪ C = A ∪ (B ∪ C)
- •(A ∩ B) ∩ C = A ∩ (B ∩ C)

### Distributive

- •A ∩ (B ∪ C) = (A ∩ B) ∪ (A ∩ C)
- •A ∪ (B ∩ C) = (A ∪ B) ∩ (A ∪ C)

### Identity / domination

- •A ∪ ∅ = A
- •A ∩ ∅ = ∅

If you later study Boolean algebra, these will feel very familiar.

---

## Visual intuition: Venn diagrams

Even without drawing, it helps to imagine two overlapping circles:

- •Union = everything in either circle
- •Intersection = the overlap
- •Complement = everything outside a circle (but still inside the rectangle U)

Venn diagrams are great for intuition, but definitions using ∈, ∨, ∧ are what make arguments precise.

---

## Sets in linear algebra (quick note about **v**)

You may soon see sets whose elements are vectors like **v** ∈ ℝⁿ. The set ideas are identical:

- •A set can contain numbers, strings, pairs, or vectors **v**.
- •Membership still means “is this object one of the allowed ones?”

## Application/Connection: How Sets Show Up in CS, Graphs, Relations, and Probability

### Why connect now?

Sets can feel abstract until you see them in the wild. This section shows how the same few ideas (∈, ⊆, ∪, ∩, Aᶜ) appear across fields.

---

## Computer science: data and constraints

### 1) Filtering with intersection

Suppose:

- •A = users who are active
- •B = users who have paid

Then:

- •A ∩ B = users who are both active and paid

### 2) Combining with union

If:

- •C = users who get access via subscription
- •D = users who get access via a free trial

Then:

- •C ∪ D = users who have access

### 3) Excluding invalid cases with complement

If:

- •U = all possible inputs
- •Bad = inputs that fail validation

Then valid inputs are:

- •Badᶜ

---

## Graphs: vertices and edges are sets

A (simple) graph is often described as:

- •G = (V, E)

where:

- •V is a set of vertices (nodes)
- •E is a set of edges

In an undirected graph, edges can be represented as sets {u, v} with u, v ∈ V.

So you’ll write things like:

- •v ∈ V
- •{u, v} ∈ E

This is the set language of graphs.

---

## Relations: subsets of a Cartesian product

A relation R between sets A and B is a subset of A × B.

Even before learning Cartesian products in detail, note the pattern:

- •R ⊆ A × B

Elements of R are typically ordered pairs (a, b). Membership means:

- •(a, b) ∈ R

Properties like “reflexive” and “transitive” are built from membership statements about such pairs.

---

## Vector spaces: start with a set, then add rules

A vector space begins as a set V whose elements are vectors **v**, together with operations like addition and scalar multiplication.

The set part still matters:

- •**v** ∈ V

And closure properties are set statements:

- •if **u** ∈ V and **v** ∈ V then **u** + **v** ∈ V

So sets are the container that later structure lives inside.

---

## Probability and measure theory: events are sets

In probability, an **event** is a set of outcomes.

If Ω is the sample space (a universe of outcomes), then events are subsets:

- •A ⊆ Ω

Operations match intuitive language:

- •“A or B happens” → A ∪ B
- •“A and B happens” → A ∩ B
- •“A does not happen” → Aᶜ

Measure theory will later formalize which sets are allowed to be events (σ-algebras), but the basic operations are the same.

---

### A unifying perspective

Set operations are like logical operations on membership:

- •x ∈ (A ∪ B) ⇔ (x ∈ A) ∨ (x ∈ B)
- •x ∈ (A ∩ B) ⇔ (x ∈ A) ∧ (x ∈ B)
- •x ∈ Aᶜ ⇔ ¬(x ∈ A)

This “translate to logic” trick is one of the most powerful habits you can build early.

## Worked Examples (3)

### Compute union, intersection, and complement (with an explicit universe)

Let U = {1, 2, 3, 4, 5, 6}. Let A = {1, 2, 4, 6} and B = {2, 3, 6}. Find A ∪ B, A ∩ B, Aᶜ, and Bᶜ (all complements relative to U).

1. Union means “in A or in B”.

   A ∪ B = {x : x ∈ A ∨ x ∈ B}

   Start from A = {1,2,4,6} and add any elements from B not already included.

   So A ∪ B = {1, 2, 3, 4, 6}.
2. Intersection means “in both”.

   A ∩ B = {x : x ∈ A ∧ x ∈ B}

   Check elements of B against A:

   - •2 ∈ A and 2 ∈ B ⇒ include 2
   - •3 ∉ A ⇒ exclude 3
   - •6 ∈ A and 6 ∈ B ⇒ include 6

   So A ∩ B = {2, 6}.
3. Complement means “in U but not in the set”.

   Aᶜ = U \ A = {x ∈ U : x ∉ A}

   U = {1,2,3,4,5,6} and A = {1,2,4,6}

   Remove 1,2,4,6 from U ⇒ Aᶜ = {3, 5}.
4. Similarly,

   Bᶜ = U \ B

   Remove 2,3,6 from U ⇒ Bᶜ = {1, 4, 5}.

**Insight:** Always state (or infer) the universe U before taking complements. Union/intersection don’t need U, but complements do.

### Prove a basic identity by element-chasing (A \ B = A ∩ Bᶜ)

Let U be a universe, and let A, B ⊆ U. Prove that A \ B = A ∩ Bᶜ.

1. Why this proof style works:

   To prove two sets are equal, show they have the same elements.

   That is, show:

   (1) A \ B ⊆ A ∩ Bᶜ

   (2) A ∩ Bᶜ ⊆ A \ B
2. (1) Show A \ B ⊆ A ∩ Bᶜ.

   Take an arbitrary element x.

   Assume x ∈ A \ B.

   By definition of set difference:

   - •x ∈ A \ B ⇔ (x ∈ A) ∧ (x ∉ B)

   From (x ∉ B) and the definition of complement:

   - •x ∉ B ⇔ x ∈ Bᶜ

   So we have (x ∈ A) ∧ (x ∈ Bᶜ), which means:

   - •x ∈ A ∩ Bᶜ

   Therefore every x in A \ B is in A ∩ Bᶜ, so A \ B ⊆ A ∩ Bᶜ.
3. (2) Show A ∩ Bᶜ ⊆ A \ B.

   Take an arbitrary element x.

   Assume x ∈ A ∩ Bᶜ.

   By definition of intersection:

   - •x ∈ A ∩ Bᶜ ⇔ (x ∈ A) ∧ (x ∈ Bᶜ)

   By definition of complement:

   - •x ∈ Bᶜ ⇔ x ∉ B

   So (x ∈ A) ∧ (x ∉ B), which is exactly the definition of x ∈ A \ B.

   Therefore A ∩ Bᶜ ⊆ A \ B.
4. Since we proved both subset directions, we conclude:

   A \ B = A ∩ Bᶜ.

**Insight:** Many set proofs are really logic proofs in disguise. Translate set membership into ∧, ∨, and ¬ statements and the result becomes straightforward.

### Use subset definitions to check equality of sets

Let A = {1, 2, 3} and B = {x ∈ ℕ : x ≤ 3}. Decide whether A = B, and justify using subset reasoning.

1. First interpret B.

   B = {x ∈ ℕ : x ≤ 3} means “natural numbers less than or equal to 3”.

   Assuming ℕ = {1,2,3,…}, this gives B = {1, 2, 3}.
2. Now show A ⊆ B.

   Take any x ∈ A. Then x is one of {1,2,3}.

   Each of these is a natural number and ≤ 3, so x ∈ B.

   Therefore A ⊆ B.
3. Show B ⊆ A.

   Take any x ∈ B. Then x ∈ ℕ and x ≤ 3.

   So x must be 1, 2, or 3.

   Hence x ∈ A.

   Therefore B ⊆ A.
4. Conclude equality.

   Since A ⊆ B and B ⊆ A, we have A = B.

**Insight:** Set-builder notation often defines a set indirectly. Converting it to a roster (when finite) makes comparisons easier, but the real justification still comes from subset logic.

## Key Takeaways

- ✓

  A set is a collection of distinct elements; order and duplicates do not matter.
- ✓

  Membership is written x ∈ A (or x ∉ A) and is a yes/no statement.
- ✓

  Subset is written A ⊆ B and means ∀x (x ∈ A ⇒ x ∈ B).
- ✓

  Set equality can be proven via two inclusions: A = B ⇔ (A ⊆ B) ∧ (B ⊆ A).
- ✓

  Union and intersection are defined by logic: x ∈ A ∪ B ⇔ (x ∈ A) ∨ (x ∈ B), and x ∈ A ∩ B ⇔ (x ∈ A) ∧ (x ∈ B).
- ✓

  Complement Aᶜ depends on a universe U: Aᶜ = {x ∈ U : x ∉ A}.
- ✓

  Many set identities are best proven by “element-chasing”: assume x is in one set and show it must be in the other.

## Common Mistakes

- ✗

  Forgetting to specify the universe U when taking complements, leading to ambiguous answers.
- ✗

  Treating sets like lists: thinking {1,2,2} is different from {1,2} or that {a,b} ≠ {b,a}.
- ✗

  Confusing ∈ (element-of) with ⊆ (subset-of), e.g., writing 2 ⊆ A instead of 2 ∈ A.
- ✗

  Assuming A ⊆ B means A is “smaller” in size; subset is about containment, not cardinality (though containment often implies size constraints for finite sets).

## Practice

easy

Let U = {a, b, c, d, e}. Let A = {a, c, e} and B = {b, c, d}. Compute A ∪ B, A ∩ B, Aᶜ, and (A ∩ B)ᶜ.

**Hint:** Union = in either set; intersection = in both; complements are relative to U.

Show solution

A ∪ B = {a, b, c, d, e}.

A ∩ B = {c}.

Aᶜ = U \ A = {b, d}.

(A ∩ B)ᶜ = U \ {c} = {a, b, d, e}.

medium

Prove using element-chasing that A ∩ (B ∪ C) = (A ∩ B) ∪ (A ∩ C).

**Hint:** Show both subset directions. Start with x ∈ A ∩ (B ∪ C) and translate membership into logic using ∧ and ∨.

Show solution

Take arbitrary x.

(⊆) Assume x ∈ A ∩ (B ∪ C).

Then x ∈ A and x ∈ (B ∪ C).

So x ∈ A and (x ∈ B or x ∈ C).

Thus (x ∈ A and x ∈ B) or (x ∈ A and x ∈ C).

So x ∈ (A ∩ B) or x ∈ (A ∩ C).

Hence x ∈ (A ∩ B) ∪ (A ∩ C).

(⊇) Assume x ∈ (A ∩ B) ∪ (A ∩ C).

Then (x ∈ A and x ∈ B) or (x ∈ A and x ∈ C).

In either case x ∈ A, and also (x ∈ B or x ∈ C), meaning x ∈ (B ∪ C).

Therefore x ∈ A ∩ (B ∪ C).

So A ∩ (B ∪ C) = (A ∩ B) ∪ (A ∩ C).

medium

Let A and B be sets. Is it always true that A ⊆ A ∪ B? Is it always true that A ∩ B ⊆ A? Prove your answers.

**Hint:** Use the definition of ⊆: pick an arbitrary x in the left-hand set and show it must be in the right-hand set.

Show solution

Yes, both are always true.

1) A ⊆ A ∪ B:

Take x ∈ A. Then x ∈ A or x ∈ B is true (because x ∈ A). Hence x ∈ A ∪ B. So A ⊆ A ∪ B.

2) A ∩ B ⊆ A:

Take x ∈ A ∩ B. Then x ∈ A and x ∈ B, in particular x ∈ A. So A ∩ B ⊆ A.

## Connections

- •Next: [Graphs Introduction](/tech-tree/graphs-basic/) — graphs are built from a vertex set V and edge set E.
- •Next: [Relations](/tech-tree/relations/) — relations are sets of pairs, written as subsets of A × B.
- •Next: [Vector Spaces](/tech-tree/vector-spaces/) — start with a set V of vectors **v**, then add operations and axioms.
- •Later: [Measure Theory](/tech-tree/measure-theory/) — events are sets; complements/unions/intersections become the foundation of probability.

Quality: A (4.5/5)

[← back to tree](/tech-tree/)[browse all →](/tech-tree/inventory/)
