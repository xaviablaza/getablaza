---
title: Relations
description: Subsets of Cartesian products. Reflexive, symmetric, transitive properties.
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
permalink: /tech-tree/relations/
---

[←Back to Tech Tree](/tech-tree/)

[inventory](/tech-tree/inventory/)[coverage](/tech-tree/coverage/)

# Relations

Discrete MathDifficulty: ★★☆☆☆Depth: 1Unlocks: 1

Subsets of Cartesian products. Reflexive, symmetric, transitive properties.

## Interactive Visualization

⏮◀◀▶▶STEP0.25x1xZOOM

t=0s

## Core Concepts

- -Binary relation: a set of ordered pairs (i.e. a subset of A x B)
- -Reflexive property: for all a in A, (a,a) is in R
- -Symmetric property: for all a,b, if (a,b) is in R then (b,a) is in R
- -Transitive property: for all a,b,c, if (a,b) is in R and (b,c) is in R then (a,c) is in R

## Key Symbols & Notation

A x B (Cartesian product)

## Essential Relationships

- -Equivalence relation = a relation that is reflexive AND symmetric AND transitive

## Prerequisites (2)

[Sets6 atoms](/tech-tree/sets-basic/)[Functions6 atoms](/tech-tree/functions-basic/)

## Unlocks (1)

[Equivalence Relationslvl 2](/tech-tree/equivalence-relations/)

## Referenced by (1)

Where this concept shows up in the operating-finance and personal-finance graphs.

### From Business (1)

[GARPBusiness

GARP is defined on the transitive closure of the directly-revealed-preference relation: no cycles in strict revealed preference. Understanding reflexivity, transitivity, and acyclicity of binary relations is required to state the axiom.](/business/garp/)

Advanced Learning Details

### Graph Position

18

Depth Cost

1

Fan-Out (ROI)

1

Bottleneck Score

1

Chain Length

### Cognitive Load

6

Atomic Elements

20

Total Elements

L0

Percentile Level

L4

Atomic Level

### All Concepts (8)

- - Relation: a set of ordered pairs, i.e., a subset R ⊆ A × B (general notion of a relation between elements of A and B)
- - Relation on a set: a relation whose domain and codomain are the same set, R ⊆ A × A
- - Ordered pair (a,b): an element where order matters and (a,b) ≠ (b,a) in general
- - Reflexive property: every element is related to itself (for all a ∈ A, (a,a) ∈ R)
- - Symmetric property: whenever a is related to b then b is related to a (if (a,b) ∈ R then (b,a) ∈ R)
- - Transitive property: relation 'chains' (if (a,b) ∈ R and (b,c) ∈ R then (a,c) ∈ R)
- - Equivalence relation: a relation that is simultaneously reflexive, symmetric and transitive
- - Shorthand relation notation a R b to mean (a,b) ∈ R

### Teaching Strategy

Deep-dive lesson - accessible entry point but dense material. Use worked examples and spaced repetition.

Functions tell you “exactly one output per input.” Relations remove that restriction—so you can model “can be connected to,” “is similar to,” “is a friend of,” “is a divisor of,” and many other real structures in discrete math and CS.

TL;DR:

A (binary) relation R from A to B is any subset R ⊂ A × B. When A = B, we study special properties: reflexive (∀a, (a,a) ∈ R), symmetric (if (a,b) ∈ R then (b,a) ∈ R), and transitive (if (a,b) ∈ R and (b,c) ∈ R then (a,c) ∈ R). These properties describe “self-links,” “two-way links,” and “chain links,” and they lead directly to equivalence relations and partitions.

## What Is a Relation?

### Why you should care (motivation)

You already know **sets** (collections) and **functions** (special mappings). But many situations don’t fit the “exactly one output” rule of functions:

- •A person can have **multiple** friends.
- •A web page can link to **many** pages.
- •A number can be “related” to many numbers by “≤”.
- •In a graph, a node can have edges to many nodes.

A **relation** is the simplest mathematical object that captures this idea: it’s just a set of pairs.

### Definition

Let A and B be sets. The **Cartesian product** A × B is the set of all ordered pairs:

A × B = { (a, b) | a ∈ A and b ∈ B }

A **(binary) relation** R from A to B is any subset of that product:

R ⊂ A × B

So R is a set of ordered pairs (a,b), where the first component comes from A and the second comes from B.

### Intuition: a “filter” on all possible pairs

Think of A × B as **all possible connections** from A to B. A relation R is what you get after keeping only the pairs that satisfy some condition.

Example: Let A = {1,2,3} and B = {a,b}.

A × B = { (1,a), (1,b), (2,a), (2,b), (3,a), (3,b) }

A relation could be:

R = { (1,a), (2,a), (2,b) }

That’s it—no extra structure is required.

### Domain, codomain, and “image” (link to what you know)

When R ⊂ A × B, we often call A the **domain set** and B the **codomain set** (not to be confused with function domain/codomain, but the idea is similar).

Given a relation R:

- •The **domain of R** (sometimes written dom(R)) is the set of a ∈ A that appear in at least one pair in R.
- •The **range / image of R** (sometimes ran(R)) is the set of b ∈ B that appear in at least one pair in R.

For the example above:

- •dom(R) = {1,2}
- •ran(R) = {a,b}

### Relations vs functions

A function f: A → B chooses **exactly one** b ∈ B for every a ∈ A.

A relation R ⊂ A × B can:

- •map one a to **zero** b’s (no pair starts with a)
- •map one a to **one** b
- •map one a to **many** b’s

So: every function is a relation, but not every relation is a function.

Here’s the relationship in set language. A function f: A → B corresponds to the relation:

R\_f = { (a, f(a)) | a ∈ A }

This R\_f has a very specific structure: for each a ∈ A, there is exactly one pair starting with a.

### The special case: relations “on” a set

Many important properties (reflexive, symmetric, transitive) are discussed for relations **on a single set** A, meaning:

R ⊂ A × A

Then pairs look like (a,b) with both elements in the same universe A. You can picture this as a directed graph whose nodes are elements of A and whose directed edges are the pairs in R.

That graph picture will be useful:

- •(a,a) is a self-loop
- •symmetry means edges go both ways
- •transitivity means paths of length 2 imply a direct edge

## Core Mechanic 1: Building and Representing Relations

### Why representation matters

Because a relation is “just a set of ordered pairs,” you might think it’s trivial. But in practice, you constantly need to:

- •construct a relation from a rule
- •check whether a pair is in the relation
- •visualize the structure
- •test properties like reflexive/symmetric/transitive

Good representations make these tasks mechanical.

### Representation 1: Listing ordered pairs

For small finite sets, you can write R explicitly.

Example: A = {1,2,3}. Define R = “≤” restricted to A.

R = { (1,1),(1,2),(1,3), (2,2),(2,3), (3,3) }

Pros: crystal clear.

Cons: scales poorly.

### Representation 2: Rule-based definition

Instead of listing, define R by a predicate P(a,b) that is true exactly when (a,b) ∈ R.

Example: On integers ℤ, define R by:

(a,b) ∈ R ⇔ a divides b

This is compact and works for infinite sets.

### Representation 3: Directed graph (for R ⊂ A × A)

If A is finite, draw a node for each element and a directed edge a → b if (a,b) ∈ R.

- •Reflexive: every node has a self-loop.
- •Symmetric: every edge has a reverse edge.
- •Transitive: whenever there is a path a → b → c, there is also an edge a → c.

This graph intuition will keep you from getting lost in quantifiers.

### Representation 4: Matrix (adjacency matrix)

If A = {a₁, a₂, …, aₙ}, a relation R on A can be represented by an n×n 0–1 matrix M where:

Mᵢⱼ = 1 iff (aᵢ, aⱼ) ∈ R

This turns property-checking into pattern-checking:

- •Reflexive ⇔ all diagonal entries Mᵢᵢ are 1
- •Symmetric ⇔ M is symmetric: Mᵢⱼ = Mⱼᵢ
- •Transitive ⇔ if Mᵢⱼ = 1 and Mⱼₖ = 1 then Mᵢₖ must be 1 (this relates to Boolean matrix multiplication, later)

### Composition (a sneak preview of “relations as computation”)

Relations can be composed similarly to functions.

If R ⊂ A × B and S ⊂ B × C, the composition S ∘ R is a relation in A × C defined by:

(a,c) ∈ (S ∘ R) ⇔ ∃b ∈ B such that (a,b) ∈ R and (b,c) ∈ S

This matters in CS because it models multi-step connections (like “reachable in 2 steps”). It also foreshadows transitivity: transitivity is essentially saying R ∘ R ⊂ R for a relation on A.

We won’t go deep into composition here, but keep the intuition:

- •functions: compose by plugging outputs into inputs
- •relations: compose by “there exists an intermediate element”

### Quick comparison table

| Object | Definition | Can one input map to many outputs? | Can an input map to zero outputs? |
| --- | --- | --- | --- |
| Function f: A → B | rule giving exactly one b per a | No | No |
| Relation R ⊂ A × B | any set of pairs | Yes | Yes |

This flexibility is exactly why relations are the right tool for many discrete structures.

## Core Mechanic 2: Reflexive, Symmetric, and Transitive Properties

### Why properties matter

A random subset of A × A is rarely meaningful. Properties like reflexive, symmetric, and transitive carve out special “shapes” of relations that correspond to common ideas:

- •“every element relates to itself” (reflexive)
- •“relationship is mutual” (symmetric)
- •“relationship respects chains” (transitive)

When these combine in certain ways, you get powerful classifications—most importantly **equivalence relations**, which will unlock partitions and quotient structures.

We assume in this section that R is a relation **on** A, meaning R ⊂ A × A.

---

## Reflexive

### Definition

R is **reflexive** if:

∀a ∈ A, (a,a) ∈ R

### Intuition

Everyone is related to themselves. In a graph: every node has a self-loop.

### Example

On A = {1,2,3}, the relation “≤” is reflexive because 1 ≤ 1, 2 ≤ 2, 3 ≤ 3.

### Non-example

The relation “<” is not reflexive on numbers because a < a is never true.

---

## Symmetric

### Definition

R is **symmetric** if:

∀a,b ∈ A, (a,b) ∈ R ⇒ (b,a) ∈ R

### Intuition

If a is related to b, then b must be related to a. In a graph: edges come in two-way pairs.

### Example

On people, “is siblings with” is symmetric: if Alice is a sibling of Bob, then Bob is a sibling of Alice.

### Non-example

“≤” is not symmetric: 1 ≤ 2 is true, but 2 ≤ 1 is false.

---

## Transitive

### Definition

R is **transitive** if:

∀a,b,c ∈ A,

(a,b) ∈ R ∧ (b,c) ∈ R ⇒ (a,c) ∈ R

### Intuition

Chains collapse: if a relates to b and b relates to c, then a must relate to c. In a graph: every length-2 path a → b → c forces a direct edge a → c.

### Example

“≤” is transitive: if 1 ≤ 2 and 2 ≤ 3, then 1 ≤ 3.

### Non-example

“is a friend of” is often not transitive: Alice can be friends with Bob, Bob with Cara, but Alice not friends with Cara.

---

## Seeing the three properties together

Because each property is a ∀-statement, to **disprove** it you only need one counterexample.

- •Not reflexive: find an a with (a,a) ∉ R
- •Not symmetric: find (a,b) ∈ R but (b,a) ∉ R
- •Not transitive: find (a,b), (b,c) ∈ R but (a,c) ∉ R

To **prove** a property, you must show the statement holds for all required elements.

### A useful “checklist” mindset

When A is finite and you have R listed:

- •Reflexive: check all diagonal pairs (a,a)
- •Symmetric: check each pair has its reverse
- •Transitive: for each (a,b), look at all (b,c) and ensure (a,c)

This can be time-consuming by hand, but for small sets it is manageable.

### Independence: properties don’t imply each other

A common misconception is that these properties “come as a package.” They do not. You can have:

- •reflexive but not symmetric (e.g., ≤)
- •symmetric but not transitive (e.g., “distance is 1” on integers)
- •transitive but not reflexive (e.g., “<”)

This is worth internalizing: each property is a separate constraint.

### Optional note: antisymmetric vs asymmetric (context)

Learners often confuse symmetry with other “directional” ideas.

- •**Antisymmetric**: (a,b) and (b,a) implies a = b (common in partial orders)
- •**Asymmetric**: (a,b) implies not (b,a)

You don’t need these yet for this node, but knowing the names helps prevent mixing them up with “symmetric.”

## Application/Connection: From Relations to Equivalence Relations (and Partitions)

### Why this connection is the point

The main reason we study reflexive, symmetric, and transitive relations early is that the triple combination is extremely powerful.

A relation that is reflexive + symmetric + transitive behaves like “has the same status as” or “is indistinguishable from under some rule.” That leads to grouping elements into **equivalence classes**—a key move across math and CS.

### Equivalence relation (preview)

A relation R on A is an **equivalence relation** if it is:

- •reflexive
- •symmetric
- •transitive

When this holds, you can define the **equivalence class** of a ∈ A:

[a] = { b ∈ A | (a,b) ∈ R }

The miracle is that these classes form a **partition** of A: they are disjoint and cover A.

### Concrete example: congruence mod n

On ℤ, define a ≡ b (mod n) if n divides (a − b).

This relation is reflexive, symmetric, and transitive, so integers fall into n buckets: the remainder classes.

For n = 3, the classes are:

[0] = { …, −6, −3, 0, 3, 6, … }

[1] = { …, −5, −2, 1, 4, 7, … }

[2] = { …, −4, −1, 2, 5, 8, … }

This is not just number theory; it’s foundational for hashing ideas, cyclic structures, and reasoning about periodicity.

### Graph reachability and transitive closure (another connection)

If you define R as “there is a directed edge from a to b,” then transitivity fails in general.

But you can build a new relation R\* (often called a transitive closure) meaning:

(a,b) ∈ R\* ⇔ b is reachable from a by a path of length ≥ 0

Then R\* becomes transitive by construction. This kind of relational thinking shows up in:

- •database queries (joins are like relational composition)
- •program analysis (control-flow reachability)
- •graph algorithms (reachability, strongly connected components)

### Where functions fit back in

Functions often induce equivalence relations:

Given f: A → B, define a ~ b iff f(a) = f(b).

This ~ is an equivalence relation (you’ll prove this soon in the equivalence relations node). The equivalence classes are exactly the “fibers” of f: all inputs that map to the same output.

That explains why relations are a natural next step after functions: they generalize the idea of grouping and structure beyond one-output rules.

## Worked Examples (3)

### Check reflexive/symmetric/transitive for a relation given by pairs

Let A = {1,2,3} and define R ⊂ A × A by:

R = { (1,1), (2,2), (3,3), (1,2), (2,1), (2,3) }.

Determine whether R is reflexive, symmetric, and transitive.

1. Reflexive check:

   We need ∀a ∈ A, (a,a) ∈ R.

   - •(1,1) ∈ R ✓
   - •(2,2) ∈ R ✓
   - •(3,3) ∈ R ✓

   So R is reflexive.
2. Symmetric check:

   We need ∀a,b, (a,b) ∈ R ⇒ (b,a) ∈ R.

   List the non-diagonal pairs and check reverses:

   - •(1,2) ∈ R and (2,1) ∈ R ✓
   - •(2,3) ∈ R, but is (3,2) ∈ R? No.

   So symmetry fails.

   Therefore R is not symmetric.
3. Transitive check:

   We need: if (a,b) ∈ R and (b,c) ∈ R then (a,c) ∈ R.

   Look for a counterexample (one is enough).

   We have (1,2) ∈ R and (2,3) ∈ R.

   Transitivity would require (1,3) ∈ R.

   But (1,3) ∉ R.

   So transitivity fails.

   Therefore R is not transitive.

**Insight:** For finite relations, reflexive is a diagonal checklist, symmetric is a “reverse-pair” checklist, and transitive is about checking length-2 chains (a → b → c). One counterexample disproves the property.

### A rule-defined relation: divisibility on {1,2,3,4,6}

Let A = {1,2,3,4,6}. Define a relation R on A by:

(a,b) ∈ R ⇔ a divides b.

Check whether R is reflexive, symmetric, and transitive.

1. Reflexive:

   Take any a ∈ A.

   We know a divides a because a = a · 1.

   So (a,a) ∈ R for all a.

   Therefore R is reflexive.
2. Symmetric:

   To be symmetric, we would need: if a divides b, then b divides a.

   Counterexample:

   2 divides 4, so (2,4) ∈ R.

   But 4 does not divide 2, so (4,2) ∉ R.

   Therefore R is not symmetric.
3. Transitive:

   Assume (a,b) ∈ R and (b,c) ∈ R.

   That means:

   - •a divides b ⇒ ∃k such that b = a·k
   - •b divides c ⇒ ∃m such that c = b·m

   Substitute b into the second equation:

   c = b·m

   = (a·k)·m

   = a·(k·m)

   So a divides c, meaning (a,c) ∈ R.

   Therefore R is transitive.

**Insight:** Divisibility is a classic example: reflexive and transitive but not symmetric. The transitivity proof is a good template: unpack definitions using ∃, substitute, and re-pack the conclusion.

### A relation induced by a function: “same output”

Let f: A → B be a function. Define a relation ~ on A by:

a ~ b ⇔ f(a) = f(b).

Show that ~ is reflexive and symmetric (and see why transitivity is plausible).

1. Reflexive:

   We need ∀a ∈ A, a ~ a.

   By definition, a ~ a ⇔ f(a) = f(a).

   But f(a) = f(a) is always true.

   So ~ is reflexive.
2. Symmetric:

   We need ∀a,b, a ~ b ⇒ b ~ a.

   Assume a ~ b. Then f(a) = f(b).

   Equality is symmetric, so f(b) = f(a).

   Thus b ~ a.

   So ~ is symmetric.
3. Transitivity (sketch):

   Assume a ~ b and b ~ c.

   Then f(a) = f(b) and f(b) = f(c).

   By transitivity of equality, f(a) = f(c).

   So a ~ c.

   Therefore ~ is transitive as well.

**Insight:** Many equivalence relations come from “observations” or “features” captured by a function f. Two elements are equivalent if you can’t distinguish them using f.

## Key Takeaways

- ✓

  A binary relation from A to B is any subset R ⊂ A × B; it is literally a set of ordered pairs.
- ✓

  Functions are special relations: for each a ∈ A there is exactly one pair (a,b). Relations can map an element to zero, one, or many elements.
- ✓

  For relations on a set A (R ⊂ A × A), you can visualize them as directed graphs or adjacency matrices.
- ✓

  Reflexive means every element relates to itself: ∀a ∈ A, (a,a) ∈ R.
- ✓

  Symmetric means relationships are mutual: (a,b) ∈ R ⇒ (b,a) ∈ R.
- ✓

  Transitive means chains collapse: (a,b) ∈ R and (b,c) ∈ R ⇒ (a,c) ∈ R.
- ✓

  To disprove any of these properties, a single counterexample pair (or triple for transitivity) is enough.
- ✓

  Equivalence relations are exactly those that are reflexive, symmetric, and transitive; they enable partitioning a set into equivalence classes.

## Common Mistakes

- ✗

  Confusing “relation from A to B” with “relation on A.” Reflexive/symmetric/transitive are defined for relations on the same set (R ⊂ A × A).
- ✗

  Forgetting that ordered pairs are ordered: (a,b) ≠ (b,a) in general, so symmetry is a real extra condition.
- ✗

  Checking transitivity incorrectly by looking for (a,c) only when a, b, c are all distinct; transitivity must hold for all triples, including repeated elements.
- ✗

  Assuming that if a relation is reflexive and symmetric then it must be transitive (it doesn’t).

## Practice

easy

Let A = {a,b,c}. Define R = { (a,a), (b,b), (c,c), (a,b), (b,c), (a,c) }.

Is R reflexive? symmetric? transitive?

**Hint:** Reflexive: check the diagonal. Symmetric: check whether (b,a) exists when (a,b) exists. Transitive: test the chain a → b → c.

Show solution

Reflexive: yes, all (a,a),(b,b),(c,c) are in R.

Symmetric: no, because (a,b) ∈ R but (b,a) ∉ R.

Transitive: yes. The main nontrivial chain is (a,b) and (b,c), which requires (a,c); it is included. Other chains either involve diagonals or require pairs that are already present.

medium

On A = ℤ, define R by (a,b) ∈ R ⇔ a − b is even. Determine whether R is reflexive, symmetric, and transitive.

**Hint:** Use algebra: “even” means divisible by 2. For transitivity, add two even numbers.

Show solution

Reflexive: a − a = 0 is even, so (a,a) ∈ R for all a.

Symmetric: if a − b is even, then b − a = −(a − b) is also even.

Transitive: if a − b is even and b − c is even, then (a − b) + (b − c) = a − c is even. So (a,c) ∈ R.

Therefore R is reflexive, symmetric, and transitive (an equivalence relation).

hard

Let A = {1,2,3,4}. Define R on A by (a,b) ∈ R ⇔ a + b is odd. Check which properties hold: reflexive, symmetric, transitive.

**Hint:** Oddness flips with parity. For reflexive, examine a + a. For transitivity, try to find (a,b) and (b,c) that are in R but (a,c) is not.

Show solution

Reflexive: No. For any a, a + a = 2a is even, not odd. So (a,a) ∉ R.

Symmetric: Yes. a + b is odd ⇔ b + a is odd, so (a,b) ∈ R ⇒ (b,a) ∈ R.

Transitive: No. Example: (1,2) ∈ R because 1+2=3 is odd, and (2,3) ∈ R because 2+3=5 is odd. But (1,3) ∉ R because 1+3=4 is even. So transitivity fails.

## Connections

Next up: [Equivalence Relations](/tech-tree/equivalence-relations/)

Related prior knowledge:

- •[Sets](/tech-tree/sets/)
- •[Functions](/tech-tree/functions/)

Where this goes later (typical paths):

- •Partial orders (reflexive + antisymmetric + transitive)
- •Graph reachability and transitive closure
- •Relational databases (relations as tables; joins as relational composition)

Quality: A (4.3/5)

[← back to tree](/tech-tree/)[browse all →](/tech-tree/inventory/)
