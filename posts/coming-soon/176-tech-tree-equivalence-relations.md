---
title: Equivalence Relations
description: Relations that partition sets into equivalence classes.
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
permalink: /tech-tree/equivalence-relations/
---

[←Back to Tech Tree](/tech-tree/)

[inventory](/tech-tree/inventory/)[coverage](/tech-tree/coverage/)

# Equivalence Relations

Discrete MathDifficulty: ★★☆☆☆Depth: 2Unlocks: 0

Relations that partition sets into equivalence classes.

## Interactive Visualization

⏮◀◀▶▶STEP0.25x1xZOOM

t=0s

## Core Concepts

- -Equivalence relation: a binary relation that is reflexive, symmetric, and transitive
- -Equivalence class and partition: the set of all elements equivalent to a given element; equivalence classes are pairwise disjoint and their union is the whole underlying set

## Key Symbols & Notation

tilde (~) to denote the equivalence relation (a ~ b means a is equivalent to b)

## Essential Relationships

- -Every equivalence relation induces a partition of the underlying set, and every partition defines an equivalence relation (one-to-one correspondence)
- -a ~ b if and only if a and b lie in the same equivalence class

## Prerequisites (1)

[Relations6 atoms](/tech-tree/relations/)

## Referenced by (1)

Where this concept shows up in the operating-finance and personal-finance graphs.

### From Business (1)

[Internal EquityBusiness

Job leveling and pay banding is literally partitioning employees into equivalence classes where members within a class receive consistent treatment - the mathematical foundation for how internal equity structures work](/business/internal-equity/)

Advanced Learning Details

### Graph Position

23

Depth Cost

0

Fan-Out (ROI)

0

Bottleneck Score

2

Chain Length

### Cognitive Load

5

Atomic Elements

21

Total Elements

L0

Percentile Level

L3

Atomic Level

### All Concepts (6)

- - equivalence relation (the name for a relation that is reflexive, symmetric, and transitive)
- - equivalence class (for a given element a, the set of all elements equivalent to a)
- - partition (a collection of nonempty, pairwise disjoint subsets whose union is the whole set)
- - quotient set / set of equivalence classes (the collection of all equivalence classes of a set under an equivalence relation)
- - canonical projection (the map sending each element to its equivalence class)
- - representative (an element chosen to stand for its entire equivalence class)

### Teaching Strategy

Self-serve tutorial - low prerequisites, straightforward concepts.

When you say “these two things are the same,” you rarely mean literally identical. You mean “the same for the purpose I care about.” Equivalence relations formalize that idea and turn it into a powerful organizing tool: they slice a set into non-overlapping groups called equivalence classes.

TL;DR:

An equivalence relation ~ on a set S is a relation that is reflexive, symmetric, and transitive. It partitions S into equivalence classes [a] = {x ∈ S : x ~ a}. Every equivalence relation determines a unique partition of S, and every partition determines a unique equivalence relation.

## What Is an Equivalence Relation?

### Why we need a special kind of “sameness”

In mathematics and computer science, we constantly treat different objects as interchangeable.

- •Two integers might be “the same” if they have the same remainder mod 5.
- •Two strings might be “the same” if they differ only by capitalization.
- •Two graphs might be “the same” if they are isomorphic.

In each case, we’re not claiming the objects are literally equal. We’re defining a *notion of equivalence*.

An **equivalence relation** is the cleanest way to do this because it guarantees that “equivalent” behaves like a consistent grouping rule.

### Definition (with the three rules)

Let S be a set and let ~ be a binary relation on S (so ~ ⊆ S × S). We say ~ is an **equivalence relation** if it satisfies:

1. 1)**Reflexive:** ∀a ∈ S, a ~ a.
2. 2)**Symmetric:** ∀a, b ∈ S, if a ~ b then b ~ a.
3. 3)**Transitive:** ∀a, b, c ∈ S, if a ~ b and b ~ c then a ~ c.

These rules are not arbitrary; they’re exactly what you need for “equivalent” to produce stable groups.

### Intuition: what each property is protecting

Think of drawing a graph where each element of S is a node, and you draw an (undirected) edge between a and b when a ~ b.

- •Reflexive means every node has a “self-connection” (often implicit). It prevents an element from being excluded from its own group.
- •Symmetric means edges have no direction. If a is considered equivalent to b, b must be equivalent to a.
- •Transitive means connectivity “closes”: if a is connected to b and b to c, then a and c must be connected too. This is what forces groups to become cliques/connected components rather than messy overlaps.

### A tiny non-example to see what goes wrong

Let S = {1, 2, 3} and define a relation R = {(1,2), (2,1), (2,3), (3,2)}.

- •Symmetric? Yes.
- •Reflexive? No (missing (1,1), (2,2), (3,3)).
- •Transitive? Not necessarily: we have 1 R 2 and 2 R 3, but not 1 R 3.

If you tried to “group by R,” you’d feel the problem: 1 is grouped with 2, and 2 with 3, but 1 is not grouped with 3. That violates the idea of an equivalence class being a coherent bucket.

### Notation you’ll see constantly

- •Write **a ~ b** to mean “a is equivalent to b.”
- •When ~ is understood, we define the **equivalence class** of a as:

[a]={x∈S:x∼a}[a] = \{x \in S : x \sim a\}[a]={x∈S:x∼a}

This set [a] is “everything that belongs in the same bucket as a.”

## Core Mechanic 1: Equivalence Classes (and the “Disjoint or Identical” Rule)

### Why equivalence classes matter

Equivalence relations are useful because they let you **replace complicated objects with their class label**.

- •In modular arithmetic, you often care only about the remainder, not the exact integer.
- •In compiler optimization, you might identify expressions that are equivalent under rewriting rules.

Equivalence classes are the units you actually manipulate.

### Definition: equivalence class of an element

Given an equivalence relation ~ on S and an element a ∈ S:

[a]={x∈S:x∼a}[a] = \{x \in S : x \sim a\}[a]={x∈S:x∼a}

Two key facts follow from the equivalence properties.

### Fact A: Every element is in its own class

Because ~ is reflexive, a ~ a, so a ∈ [a].

This is small but important: no class is empty, and no element “falls out” of the grouping.

### Fact B: Two classes are either disjoint or identical

This is the central structural rule of equivalence classes.

> For any a, b ∈ S, either [a] = [b] or [a] ∩ [b] = ∅.

#### Proof (showing the work)

Assume [a] ∩ [b] ≠ ∅. Then there exists some x such that x ∈ [a] and x ∈ [b].

By definition of class:

- •x ∈ [a] ⇒ x ~ a
- •x ∈ [b] ⇒ x ~ b

Now use symmetry and transitivity to connect a to b:

1. 1)x ~ a ⇒ (by symmetry) a ~ x
2. 2)a ~ x and x ~ b ⇒ (by transitivity) a ~ b

Now show [a] ⊆ [b]. Take any y ∈ [a]. Then y ~ a.

Since a ~ b, transitivity gives:

- •y ~ a and a ~ b ⇒ y ~ b

So y ∈ [b]. Hence [a] ⊆ [b].

Similarly, show [b] ⊆ [a] (swap roles), so [a] = [b].

So if they overlap at all, they must be the same class.

### Small diagram/table (for when interactive visuals aren’t available)

Imagine S split into “blocks,” each block is a class:

| Element | Its class label | Meaning |
| --- | --- | --- |
| a | [a] | all things equivalent to a |
| b | [b] | all things equivalent to b |

And the structural rule is:

```
[a] and [b] either:
  (1) don’t touch at all, or
  (2) are exactly the same block
```

This is what makes equivalence classes behave like well-defined buckets.

### Example snapshot: integers mod 4

Let S = ℤ and define a ~ b if a and b have the same remainder mod 4 (i.e., 4 | (a − b)).

Then there are exactly four equivalence classes:

- •[0] = {..., -8, -4, 0, 4, 8, ...}
- •[1] = {..., -7, -3, 1, 5, 9, ...}
- •[2] = {..., -6, -2, 2, 6, 10, ...}
- •[3] = {..., -5, -1, 3, 7, 11, ...}

Notice how:

- •every integer belongs to exactly one of these,
- •the classes don’t overlap,
- •but each class has infinitely many elements.

## Core Mechanic 2: Partitions ⇔ Equivalence Relations (Two Views of the Same Structure)

### Why this correspondence is the whole point

Equivalence relations can feel abstract: sets of ordered pairs with three properties.

Partitions are much more concrete: “split the set into non-overlapping groups.”

The key theorem is that these are the same idea expressed in two different languages:

- •An equivalence relation **induces** a partition into equivalence classes.
- •A partition **defines** an equivalence relation by “same block.”

This is the conceptual bridge you want to internalize.

---

## From an equivalence relation to a partition

Let ~ be an equivalence relation on S.

Define the collection of all equivalence classes:

P={[a]:a∈S}\mathcal{P} = \{[a] : a \in S\}P={[a]:a∈S}

(As a set, this automatically removes duplicates, because if [a] = [b] they appear only once in \(\mathcal{P}\).)

### Claim: 𝒫 is a partition of S

A **partition** of S is a collection of nonempty subsets (called blocks) such that:

1. 1)Every block is nonempty.
2. 2)Blocks are pairwise disjoint.
3. 3)The union of all blocks is S.

Check each:

1) Nonempty: For any a, a ∈ [a] (reflexive), so [a] ≠ ∅.

2) Disjointness: For any a, b, either [a] = [b] or [a] ∩ [b] = ∅ (proved earlier). So distinct blocks are disjoint.

3) Covers S: For any x ∈ S, x ∈ [x]. So every element is in some block. Thus ⋃\_{C∈𝒫} C = S.

So equivalence classes form a partition.

---

## From a partition to an equivalence relation

Now go the other way.

Suppose you start with a partition 𝒫 of S. That means 𝒫 is a set of blocks {B₁, B₂, ..., } such that each element of S belongs to exactly one block.

Define a relation ~ by:

> a ~ b iff a and b are in the same block of 𝒫.

### Claim: ~ is an equivalence relation

Check the properties:

- •Reflexive: a is in the same block as itself ⇒ a ~ a.
- •Symmetric: if a and b are in the same block, then b and a are in the same block ⇒ b ~ a.
- •Transitive: if a and b are in the same block, and b and c are in the same block, then all three are in that one block (because b can’t be in two blocks). Hence a and c are in the same block ⇒ a ~ c.

So any partition gives an equivalence relation.

---

## Why this is a bijection (one-to-one correspondence)

These two constructions are inverses:

- •Start with ~, build its classes 𝒫. Then define “same block” from 𝒫. You get back exactly ~.
- •Start with partition 𝒫, define ~ as “same block.” Then take classes [a]. You get back the original blocks.

This is why equivalence relations are best understood visually as partitions.

---

## Visualization guidance (for an interactive canvas)

If you’re building or using a visualization, here’s the mental model to reinforce partition ⇔ relation.

### View A: Partition blocks

- •Show elements as dots.
- •Surround each equivalence class with a shaded region (a block).
- •Clicking an element highlights its entire block.

### View B: Relation edges

- •Same dots, but now draw an undirected edge between any pair (a,b) with a ~ b.
- •In a true equivalence relation, each block becomes a **clique** (all-to-all connections), or at least a clearly separated connected component if you treat self-loops as implicit.

### Crucial interaction: toggle + highlight the theorem

1. 1)Toggle from blocks → edges.
2. 2)Click element a:

- •In block view, highlight block [a].
- •In edge view, highlight all vertices connected within that block.

3. 3)Click element b:

- •If b is in [a], the highlight is identical.
- •Otherwise, the highlight is disjoint.

This directly demonstrates “either disjoint or identical.”

### A concrete micro-demo you can picture

Let S = {1,2,3,4,5,6} and partition it as:

- •B₁ = {1,4}
- •B₂ = {2,3,6}
- •B₃ = {5}

Block view shows three regions.

Edge view would show:

- •edges between 1 and 4,
- •edges among 2,3,6 (a triangle),
- •no edges for 5 besides (5,5) if you include self-loops.

No edges ever connect between blocks. That’s the partition boundary showing up as “no relation.”

## Application/Connection: Using Equivalence Relations in Discrete Math and CS

### 1) Modular arithmetic (grouping integers by remainder)

This is the canonical example because it’s both practical and rigorous.

Define, for a fixed n ≥ 1:

a∼b  ⟺  n∣(a−b)a \sim b \iff n \mid (a-b)a∼b⟺n∣(a−b)

Read it as: “a is equivalent to b if their difference is divisible by n.”

This creates n equivalence classes, often written as:

[0],[1],…,[n−1][0],[1],\dots,[n-1][0],[1],…,[n−1]

These classes are exactly the integers grouped by remainder. This is the foundation of working in ℤₙ.

### 2) Converting “messy equality” into clean computation

In programming, you frequently define a custom equality notion:

- •case-insensitive string equality
- •equality up to whitespace normalization
- •geometric points equal up to rounding tolerance (careful: tolerance-based relations are often not transitive!)

Equivalence relations tell you what properties must hold if you want to safely:

- •deduplicate items (e.g., store one representative per class)
- •use hash-based structures (hashing typically assumes an equivalence relation)

### 3) Data structure connection: Disjoint Set Union (Union-Find)

Union-Find maintains a partition of elements into disjoint sets, supporting:

- •**find(x):** return a representative of x’s class
- •**union(a,b):** merge the classes containing a and b

This is exactly “maintain equivalence classes under merges.”

Even if you don’t yet know Union-Find, equivalence relations explain *what the structure is tracking*: a partition.

### 4) Mathematics connection: quotient sets

Given an equivalence relation ~ on S, the set of equivalence classes is written:

S/∼={[a]:a∈S}S/\sim = \{[a] : a \in S\}S/∼={[a]:a∈S}

Read “S mod ~” or “S quotient ~.”

This is how you build new objects:

- •integers mod n: ℤ/≡ₙ
- •rational numbers as equivalence classes of integer pairs (a,b) with b≠0 under (a,b) ~ (c,d) iff ad = bc

The pattern: define an equivalence relation capturing “same value,” then treat each class as a single new element.

### 5) Design warning: not every ‘similarity’ is equivalence

In ML and graphics, you might say two items are “similar” if distance ≤ ε.

That relation is often:

- •reflexive (distance(a,a)=0)
- •symmetric (distance(a,b)=distance(b,a))
- •**not transitive** (a close to b, b close to c, but a not close to c)

So it does not partition cleanly into equivalence classes. That’s a common reason clustering behaves differently from equivalence-class grouping.

## Worked Examples (3)

### Checking a relation and listing its equivalence classes

Let S = {1,2,3,4,5,6}. Define a ~ b iff a and b have the same parity (both even or both odd). Determine whether ~ is an equivalence relation, and list the equivalence classes.

1. Reflexive check:

   Take any a ∈ S.

   - •a has the same parity as itself.

   So a ~ a. Reflexive holds.
2. Symmetric check:

   Assume a ~ b.

   - •That means a and b have the same parity.

   Then b and a also have the same parity.

   So b ~ a. Symmetric holds.
3. Transitive check:

   Assume a ~ b and b ~ c.

   - •a and b have the same parity.
   - •b and c have the same parity.

   Therefore a and c have the same parity.

   So a ~ c. Transitive holds.
4. Conclusion:

   ~ is reflexive, symmetric, and transitive ⇒ ~ is an equivalence relation.
5. Find the classes:

   Odds in S: {1,3,5}

   Evens in S: {2,4,6}

   So:

   [1] = {1,3,5}

   [2] = {2,4,6}

   (and [3]=[1], [4]=[2], etc.)
6. Sanity check (disjoint-or-identical):

   [1] ∩ [2] = ∅ and [1] ∪ [2] = S.

   So the classes form a partition.

**Insight:** Once you identify the invariant (here: parity), each equivalence class is the set of elements sharing that invariant. The partition viewpoint makes it immediate: odds vs evens.

### Building an equivalence relation from a partition (and reconstructing the partition)

Let S = {a,b,c,d,e,f}. Suppose we partition S into blocks:

B₁ = {a,d}, B₂ = {b,c,e}, B₃ = {f}.

Define a relation ~ by: x ~ y iff x and y are in the same block. (1) List all pairs (x,y) with x ~ y. (2) Compute [b] and [f].

1. Understand what “same block” means:

   - •Elements inside B₁ are all equivalent to each other.
   - •Elements inside B₂ are all equivalent to each other.
   - •f is only equivalent to itself (since B₃ has one element).
2. List pairs from B₁ = {a,d}:

   All ordered pairs within B₁ are:

   (a,a), (a,d), (d,a), (d,d).
3. List pairs from B₂ = {b,c,e}:

   All ordered pairs within B₂ are:

   (b,b), (b,c), (b,e),

   (c,b), (c,c), (c,e),

   (e,b), (e,c), (e,e).
4. List pairs from B₃ = {f}:

   Only (f,f).
5. Combine to get the relation ~:

   ~ is the union of those within-block pairs:

   {(a,a),(a,d),(d,a),(d,d),

   (b,b),(b,c),(b,e),(c,b),(c,c),(c,e),(e,b),(e,c),(e,e),

   (f,f)}
6. Compute the equivalence class [b]:

   [b] = {x ∈ S : x ~ b}

   From B₂, b is equivalent to b, c, e.

   So [b] = {b,c,e}.
7. Compute the equivalence class [f]:

   [f] = {x ∈ S : x ~ f}

   Only f shares f’s block.

   So [f] = {f}.

**Insight:** A partition automatically generates an equivalence relation by adding all within-block pairs. The equivalence classes you get back are exactly the original blocks—this is the partition ⇔ equivalence relation correspondence in action.

### Modular equivalence: prove it’s an equivalence relation and compute a class

On ℤ define a ~ b iff 5 | (a − b). (1) Prove ~ is an equivalence relation. (2) Describe the class [12].

1. Reflexive:

   For any a ∈ ℤ,

   a − a = 0.

   Since 5 | 0, we have a ~ a.

   So reflexive holds.
2. Symmetric:

   Assume a ~ b.

   Then 5 | (a − b), so (a − b) = 5k for some k ∈ ℤ.

   Then (b − a) = −(a − b) = 5(−k).

   So 5 | (b − a), hence b ~ a.

   So symmetric holds.
3. Transitive:

   Assume a ~ b and b ~ c.

   Then 5 | (a − b) and 5 | (b − c).

   So (a − b) = 5k and (b − c) = 5m.

   Add them:

   (a − c) = (a − b) + (b − c) = 5k + 5m = 5(k+m).

   Thus 5 | (a − c), so a ~ c.

   Transitive holds.
4. Conclusion:

   ~ is reflexive, symmetric, transitive ⇒ equivalence relation.
5. Compute [12]:

   [12] = {x ∈ ℤ : x ~ 12}

   Meaning 5 | (x − 12).

   So x = 12 + 5t for some t ∈ ℤ.

   Therefore:

   [12] = {..., 2, 7, 12, 17, 22, ...}
6. Optional simplification:

   Since 12 ≡ 2 (mod 5), we also have [12] = [2].

**Insight:** In modular equivalence, the equivalence class is an arithmetic progression. The “new object” in ℤ/≡ is the remainder class, not an individual integer.

## Key Takeaways

- ✓

  An equivalence relation ~ is exactly a relation that is reflexive, symmetric, and transitive.
- ✓

  The equivalence class [a] = {x ∈ S : x ~ a} is the “bucket” containing a.
- ✓

  Equivalence classes are never empty and always contain their defining element a.
- ✓

  Two equivalence classes are either identical or disjoint—there is no partial overlap.
- ✓

  The set of all equivalence classes forms a partition of S.
- ✓

  Every partition of S defines an equivalence relation by “in the same block.”
- ✓

  Equivalence relations and partitions are two equivalent ways to represent the same structure (partition ⇔ equivalence relation).
- ✓

  Quotient sets S/~ treat each equivalence class as a single new element, enabling constructions like ℤₙ.

## Common Mistakes

- ✗

  Forgetting that transitivity is what prevents “chain overlap” problems (a ~ b and b ~ c must force a ~ c).
- ✗

  Treating similarity-with-threshold (like distance ≤ ε) as an equivalence relation even though it often fails transitivity.
- ✗

  Thinking different representatives imply different classes: if a ~ b then [a] = [b], so the class doesn’t depend on the representative chosen.
- ✗

  Listing equivalence classes as overlapping sets (which cannot happen for a true equivalence relation).

## Practice

easy

On S = {1,2,3,4}, define a relation R by: a R b iff a = b or {a,b} = {1,2}. Is R an equivalence relation? If not, which property fails?

**Hint:** Check transitivity using the chain 1 R 2 and 2 R 1, then involve 1 R 1 and 2 R 2; also verify whether 1 R 2 and 2 R 3 implies 1 R 3 (if 2 R 3 ever holds).

Show solution

R contains all (a,a) (so reflexive holds). It also has (1,2) and (2,1), so symmetry holds.

Transitivity fails: 1 R 2 is true and 2 R 1 is true, so transitivity would require 1 R 1 (which is true). That chain is fine.

But consider 1 R 2 and 2 R 2 (true by reflexivity): transitivity would require 1 R 2 (true). Still fine.

The actual failure is with 2 R 1 and 1 R 2 requiring 2 R 2 (true). Also fine.

So R is in fact an equivalence relation on {1,2,3,4} where {1,2} is one class and {3} and {4} are singleton classes.

Equivalence classes: [1]=[2]={1,2}, [3]={3}, [4]={4}.

medium

Let S = ℤ. Define a ~ b iff a − b is even. (1) Prove ~ is an equivalence relation. (2) Describe ℤ/~ as a set of classes.

**Hint:** Use the facts: 0 is even; if k is even then −k is even; the sum of two even integers is even.

Show solution

(1) Reflexive: a − a = 0 is even ⇒ a ~ a.

Symmetric: if a − b is even, then b − a = −(a − b) is even ⇒ b ~ a.

Transitive: if a − b and b − c are even, then (a − c) = (a − b) + (b − c) is even ⇒ a ~ c.

So ~ is an equivalence relation.

(2) There are two classes: the even integers and the odd integers.

ℤ/~ = { [0], [1] } where

[0] = {...,−4,−2,0,2,4,...} and [1] = {...,−3,−1,1,3,5,...}.

hard

Suppose 𝒫 is a partition of S and ~ is defined by: a ~ b iff a and b are in the same block of 𝒫. Prove that the equivalence class [a] is exactly the block of 𝒫 that contains a.

**Hint:** Show two inclusions: (i) every element in a’s block is equivalent to a, (ii) every element equivalent to a must lie in a’s block. Use the fact that blocks are disjoint and cover S.

Show solution

Let B be the unique block in 𝒫 such that a ∈ B.

(i) If x ∈ B, then x and a are in the same block, so x ~ a. Hence x ∈ [a]. So B ⊆ [a].

(ii) If x ∈ [a], then x ~ a, meaning x and a are in the same block of 𝒫. But a is in B, so x must also be in B (since blocks are disjoint and membership is unique). Hence [a] ⊆ B.

Therefore [a] = B.

## Connections

Related nodes:

- •[Relations](/tech-tree/relations/)
- •[Partitions](/tech-tree/partitions/)
- •[Modular Arithmetic](/tech-tree/modular-arithmetic/)
- •[Quotient Sets](/tech-tree/quotient-sets/)
- •[Union-Find (Disjoint Set Union)](/tech-tree/union-find/)
- •[Congruence Relations](/tech-tree/congruence-relations/)

Quality: A (4.6/5)

[← back to tree](/tech-tree/)[browse all →](/tech-tree/inventory/)
