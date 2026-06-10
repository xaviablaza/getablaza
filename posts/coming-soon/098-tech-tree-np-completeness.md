---
title: NP-Completeness
description: Reductions proving problems equally hard. SAT, 3-SAT.
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
permalink: /tech-tree/np-completeness/
---

[←Back to Tech Tree](/tech-tree/)

[inventory](/tech-tree/inventory/)[coverage](/tech-tree/coverage/)

# NP-Completeness

AlgorithmsDifficulty: ★★★★☆Depth: 4Unlocks: 3

Reductions proving problems equally hard. SAT, 3-SAT.

## Interactive Visualization

⏮◀◀▶▶STEP0.25x1xZOOM

t=0s

## Core Concepts

- -Polynomial-time many-one reduction (Karp reduction): a polynomial-time computable transformation of instances that preserves yes/no answers
- -Definition of NP-complete: a problem that is in NP and is as hard as every problem in NP
- -SAT and 3-SAT as the canonical NP-complete problems (Cook-Levin): the concrete starting point for hardness reductions

## Key Symbols & Notation

<=\_p (polynomial-time many-one reducibility)

## Essential Relationships

- -If A <=\_p B and B is in P then A is in P (reductions preserve polynomial-time solvability)
- -A is NP-complete iff A is in NP and for every problem B in NP, B <=\_p A (completeness = membership + universality of reductions)

## Prerequisites (2)

[Complexity Classes6 atoms](/tech-tree/complexity-classes/)[Proof Techniques5 atoms](/tech-tree/proof-techniques/)

## Unlocks (3)

[Approximation Algorithmslvl 4](/tech-tree/approximation-algorithms/)[Graph Coloringlvl 4](/tech-tree/graph-coloring/)[Computational Complexity Theorylvl 5](/tech-tree/computational-complexity/)

Advanced Learning Details

### Graph Position

59

Depth Cost

3

Fan-Out (ROI)

3

Bottleneck Score

4

Chain Length

### Cognitive Load

6

Atomic Elements

33

Total Elements

L1

Percentile Level

L4

Atomic Level

### All Concepts (15)

- - Polynomial-time many-one (Karp) reduction: a function f computable in polynomial time mapping instances of one decision problem to instances of another so membership is preserved
- - Formal definition of reducibility between decision problems (language A reduces to language B via a polynomial-time mapping)
- - Karp reduction vs Turing reduction distinction (many-one reduction vs oracle/Turing-style reductions)
- - Satisfiability problem (SAT) as the decision problem: does a Boolean formula have a satisfying assignment?
- - Conjunctive Normal Form (CNF): Boolean formula expressed as an AND of OR-clauses
- - 3-CNF and 3-SAT: CNF formulas where each clause has exactly three literals, and the decision problem of their satisfiability
- - Clause, literal, and Boolean variable as formal components of propositional formulas
- - Satisfiability-preserving transformation: a reduction that ensures the original instance is satisfiable iff the transformed instance is satisfiable
- - Introduction of fresh (auxiliary) variables in reductions to adjust formula shape while preserving satisfiability
- - Clause-splitting / padding techniques to convert arbitrary CNF to 3-CNF (how to handle clauses of size <3 and >3)
- - Gadgets in reductions: small constructed components that simulate parts/constraints of the source problem inside the target problem
- - Proof pattern for NP-completeness of a problem: (1) show problem ∈ NP, (2) pick a known NP-complete problem, (3) give a polynomial-time reduction from that problem to the new problem
- - Cook–Levin theorem (role as foundational result): SAT is NP-complete because every NP problem reduces to SAT
- - Satisfiability equivalence vs implication in reductions (ensuring iff, not just one direction)
- - Polynomial-time computability requirement for reductions (ensures reductions preserve tractability relationships)

### Teaching Strategy

Multi-session curriculum - substantial prior knowledge and complex material. Use mastery gates and deliberate practice.

NP-completeness is the craft of explaining, with surgical precision, why a problem is “as hard as” every problem in NP—by converting any NP problem into it using a polynomial-time reduction. Once you can do reductions, you can transfer hardness like a conserved quantity.

TL;DR:

To prove a problem X is NP-complete: (1) show X ∈ NP via a polynomial-time verifier, and (2) show NP-hardness by giving a polynomial-time many-one (Karp) reduction A ≤ₚ X from a known NP-complete problem A (often SAT or 3-SAT). A reduction is a poly-time transformation f such that x ∈ A ⇔ f(x) ∈ X.

## What Is NP-Completeness?

### Why this concept exists (motivation)

When you face a new decision problem—say, a scheduling constraint system or a graph property—you want to know whether it is likely to have a polynomial-time algorithm.

For many problems, we do **not** know how to solve them efficiently, and we also do **not** know how to prove they’re impossible to solve efficiently (because proving lower bounds is hard). NP-completeness gives a pragmatic middle ground:

- •If a problem is NP-complete, then **a polynomial-time algorithm for it would imply P = NP**.
- •Conversely, if you believe P ≠ NP, NP-complete problems are **intractable in the worst case**, so you should consider approximation, heuristics, parameterization, or special cases.

NP-completeness is therefore a **classification tool**: it lets you explain hardness by relating a new problem to a canonical hard problem.

### Decision problems and the “yes/no” framing

NP-completeness is fundamentally about **decision problems**, not optimization problems.

- •Optimization: “What is the smallest number of colors needed?”
- •Decision: “Can this graph be colored with k colors?”

This matters because NP is defined via **verifiers** for yes-instances.

### The definition of NP-complete

Let X be a decision problem.

X is **NP-complete** iff both hold:

1) **Membership:** X ∈ NP

Meaning: there exists a polynomial p(n) and a polynomial-time verifier V such that:

- •If x is a YES instance, then there exists a certificate (witness) y with ‖y‖ ≤ p(‖x‖) and V(x, y) accepts.
- •If x is a NO instance, then for all y with ‖y‖ ≤ p(‖x‖), V(x, y) rejects.

2) **Hardness:** For every A ∈ NP, A ≤ₚ X

Meaning: every NP problem reduces to X under polynomial-time many-one reductions.

This “hardness” clause is why NP-complete problems are considered the hardest problems in NP.

### NP-hard vs NP-complete (quick contrast)

A problem X is **NP-hard** if for every A ∈ NP, A ≤ₚ X, but X may not be in NP.

Examples of why “not in NP” can happen:

- •X could be an optimization problem (not a decision language).
- •X could have certificates that are not polynomially checkable.
- •X could even be undecidable.

NP-complete = NP-hard + in NP.

### SAT and 3-SAT as the canonical starting points

The practical workflow of NP-completeness proofs relies on one key historical theorem:

- •**Cook–Levin Theorem:** SAT is NP-complete.

SAT (Boolean satisfiability) asks: given a Boolean formula φ, is there an assignment to its variables that makes φ true?

From SAT, we get many reductions. Often we use **3-SAT**, a restricted form where φ is in CNF (AND of clauses) and each clause has exactly 3 literals.

- •3-SAT is NP-complete.

Why 3-SAT is so useful:

- •It is structured enough to map cleanly to graphs, set systems, scheduling constraints, etc.
- •It is expressive enough to encode many gadgets.

### The symbol ≤ₚ

We write A ≤ₚ B to mean “A is polynomial-time many-one reducible to B.”

Interpretation:

- •If B is easy (poly-time), then A is easy.
- •If A is hard (NP-complete), and A ≤ₚ B, then B is hard.

So reductions are not just technicalities—they are the **directional arrows** that carry hardness.

## Core Mechanic 1: Polynomial-Time Many-One Reductions (Karp Reductions)

### Why reductions are the right notion

Suppose you have two decision problems A and B. If you can solve B quickly, and you can convert instances of A into instances of B quickly, then you can solve A quickly too.

That is the operational meaning of a reduction: it is a **translator** from A to B.

In NP-completeness, we use this in contrapositive form:

- •If A is known hard, and A reduces to B, then B must be at least as hard as A.

### Formal definition

A ≤ₚ B if there exists a function f computable in polynomial time such that for all instances x:

x ∈ A ⇔ f(x) ∈ B.

Key features:

- •**Many-one**: a single instance x maps to a single instance f(x).
- •**Polynomial-time computable**: f runs in time poly(‖x‖).
- •**Preserves yes/no answers**: equivalence (⇔) is crucial.

Think of f as building a “mirror instance” in B that has a YES answer exactly when the original instance in A has a YES answer.

### Direction matters

The most common mistake in early NP-completeness proofs is reversing the arrow.

If you want to prove B is NP-hard, you must reduce from a known hard problem A to B:

A ≤ₚ B.

Why? Because this shows: if we could solve B efficiently, we could solve A efficiently.

If you instead show B ≤ₚ A, you only show B is **no harder than** A (which does not prove hardness of B).

### Reduction as an algorithmic wrapper

If you have an algorithm ALG\_B for B, and a reduction f from A to B, you get an algorithm for A:

1. 1)On input x, compute y = f(x).
2. 2)Run ALG\_B on y.
3. 3)Output the same YES/NO.

Runtime:

- •computing f is poly(‖x‖)
- •ALG\_B runs in poly(‖y‖)
- •and ‖y‖ is poly(‖x‖)

So the composition is polynomial.

### The “equivalence proof” pattern

To prove correctness of a reduction, you almost always prove two implications:

1) (→) If x is YES for A, then f(x) is YES for B.

2) (←) If f(x) is YES for B, then x is YES for A.

Write them explicitly. Don’t rely on intuition.

### Gadgets: local structures that enforce logic

Many reductions, especially from 3-SAT to graph problems, are built from **gadgets**:

- •variable gadgets represent choosing True/False
- •clause gadgets enforce that at least one literal is satisfied
- •consistency edges prevent contradictions

A gadget is not just a trick: it is the reduction’s way of guaranteeing the equivalence x ∈ A ⇔ f(x) ∈ B.

### SAT vs 3-SAT and why “restricted” doesn’t mean “easy”

It can feel paradoxical that 3-SAT is NP-complete even though it’s a special case of SAT.

The key idea is that SAT ≤ₚ 3-SAT: any formula can be converted to an equisatisfiable 3-CNF formula in polynomial time.

So 3-SAT is at least as hard as SAT.

### Comparing reduction types (clarity table)

| Notion | What it transforms | Output type | Used for | Typical symbol |
| --- | --- | --- | --- | --- |
| Many-one reduction | Single instance | Single instance | NP-completeness proofs | ≤ₚ |
| Turing reduction | Instance with oracle calls | Multiple queries | Finer-grained complexity | ≤ᵀ |
| Cook reduction (older usage) | Oracle-based | Multiple queries | Sometimes for NP-hardness | (varies) |

For standard NP-completeness in algorithms courses, **≤ₚ means Karp (many-one) reduction**.

### A quick “sanity checklist” for your reduction

When you propose f:

- •Is f computable in polynomial time?
- •Is the size ‖f(x)‖ polynomial in ‖x‖?
- •Did you prove both directions (→) and (←)?
- •Does any hidden step require solving the hard problem?

A reduction must be constructive and efficient. You are not allowed to “guess a satisfying assignment” during the reduction.

## Core Mechanic 2: Proving NP-Completeness in Practice (SAT, 3-SAT, and Proof Templates)

### Why proofs have a template

NP-completeness proofs can look creative, but they are remarkably templated. The creativity is mostly in designing the right gadgets; the overall logic is consistent.

To prove a problem X is NP-complete, you usually do:

1) **Show X ∈ NP** (verification)

2) **Show A ≤ₚ X** for some known NP-complete A (hardness)

The second step is where reductions happen.

### Step 1: Show X ∈ NP (verifier thinking)

You must identify:

- •a certificate y of polynomial length
- •a deterministic poly-time verifier V

Examples of certificates:

- •For k-COLORABILITY: a coloring function c: V → {1,…,k}
- •For CLIQUE: a set S of k vertices
- •For Hamiltonian Cycle: an ordering of vertices

Verifier logic: check the claimed structure quickly.

This step is often easy, but it is not optional.

### Step 2: Choose a source problem A

You almost never reduce from “an arbitrary NP problem.” Instead, reduce from something already known NP-complete.

Good sources:

- •SAT / 3-SAT (logic constraints)
- •CLIQUE / INDEPENDENT SET / VERTEX COVER (graph structure)
- •Hamiltonian Cycle / TSP-decision (path/cycle structure)
- •PARTITION / SUBSET SUM (numeric constraints)

Pick a source that “resembles” your target.

### Why SAT is NP-complete (Cook–Levin, at a high level)

You are not required to re-prove Cook–Levin each time, but understanding what it says helps you trust SAT as a starting point.

Cook–Levin idea (conceptual):

- •Any NP computation is a nondeterministic polynomial-time Turing machine.
- •Encode its accepting computation tableau (time × tape cells) as a Boolean formula.
- •The formula is satisfiable iff there exists an accepting computation.

So SAT captures the existence of a polynomially verifiable witness.

### 3-SAT as a reduction hub

A common chain:

SAT ≤ₚ 3-SAT ≤ₚ (your problem)

So you can use 3-SAT directly as the NP-complete source.

3-SAT instance format:

- •Variables x₁,…,xₙ
- •Clauses C₁,…,Cₘ
- •Each clause is (ℓ₁ ∨ ℓ₂ ∨ ℓ₃) where each ℓ is xᵢ or ¬xᵢ
- •Question: does there exist an assignment making all clauses true?

### A practical proof template (write this down)

When proving A ≤ₚ X:

1) **Define f**: Given an instance I of A, construct instance f(I) of X.

2) **Polynomial time**: argue construction is O(poly(size(I))).

3) **Correctness**:

- •(→) If I is YES, show f(I) is YES.
- •(←) If f(I) is YES, show I is YES.

Your correctness argument often relies on mapping:

- •satisfying assignments ↔ valid structures
- •variable choices ↔ gadget selections

### Example-level intuition: “choices” and “constraints”

Most NP-complete problems have this feel:

- •You must make many local choices.
- •Choices must satisfy global constraints.

3-SAT: choose truth values; satisfy all clauses.

Graph coloring: choose colors; satisfy adjacency constraints.

Clique: choose vertices; satisfy pairwise adjacency.

Reductions translate one set of choices/constraints into another.

### Polynomial growth matters

Even if f is conceptually correct, it must not blow up the instance exponentially.

If your input has n variables and m clauses, a typical gadget reduction produces:

- •O(n + m) vertices/edges, or
- •O(poly(n + m)) size

If you produce something like 2ⁿ vertices, you have not built a polynomial-time reduction.

### Certification vs construction

A subtle but important pacing point:

- •Proving X ∈ NP: you assume a candidate solution exists and **verify** it fast.
- •Building f for hardness: you must **construct** the instance deterministically in poly-time.

Hardness reductions cannot “use nondeterminism.” They are ordinary algorithms.

## Application/Connection: Using NP-Completeness Results (and What They Don’t Say)

### What NP-completeness lets you conclude

If X is NP-complete, then:

- •If X ∈ P, then P = NP.
- •If P ≠ NP, then there is no polynomial-time algorithm that solves all instances of X.

In practice, we treat NP-completeness as strong evidence that we should not search for exact poly-time algorithms for the general case.

### What NP-completeness does **not** say

NP-completeness is about worst-case asymptotic complexity. It does not mean:

- •“Every instance is hard.” Many real instances are easy.
- •“You can’t solve it at all.” You can often solve moderate sizes or special cases.
- •“Approximation is impossible.” Some NP-complete problems have excellent approximations; others are hard to approximate.

### Typical responses when you learn a problem is NP-complete

Once you have an NP-completeness classification, you usually pivot to one of these strategies:

| Strategy | Goal | When it works | Example follow-up node |
| --- | --- | --- | --- |
| Approximation algorithms | Near-optimal solutions provably close to best | Optimization versions with structure | [Approximation Algorithms](/tech-tree/approximation-algorithms/) |
| Parameterized algorithms | Exponential in a small parameter k, poly in n | Small treewidth, small k, etc. | (often separate node) |
| Special cases / restrictions | Exact poly-time on restricted inputs | Planar graphs, bounded degree, etc. | [Graph Coloring](/tech-tree/graph-coloring/) |
| Heuristics / SAT solvers / ILP | Fast in practice on many instances | Industrial instances, structured constraints | (SAT/ILP tooling) |

### Why SAT and 3-SAT keep showing up in applications

SAT is not just theoretical. Modern SAT solvers can handle massive instances and are used in:

- •hardware verification
- •scheduling and planning
- •cryptanalysis
- •formal methods

So NP-completeness does not imply “never solvable”—it implies “don’t expect a guaranteed polynomial-time exact algorithm for all instances.”

### Reduction thinking as a transferable skill

Even outside NP-completeness, reductions teach you how to:

- •model problems precisely
- •map one formalism into another
- •preserve meaning under transformation

These are core skills in algorithms, complexity, and even systems (e.g., compiling one representation into another).

### Connection to broader complexity theory

NP-completeness lives inside a bigger ecosystem:

- •Space complexity (PSPACE, Savitch’s theorem)
- •Randomized classes (BPP, RP)
- •Circuit complexity and lower bounds
- •Fine-grained complexity (SETH, 3SUM)

If you continue into [Computational Complexity Theory](/tech-tree/computational-complexity/), you’ll see that the same proof discipline (define reductions carefully; track resources) generalizes to other resources besides time.

## Worked Examples (3)

### Reduction 3-SAT ≤ₚ CLIQUE

Goal: prove CLIQUE is NP-hard by reducing from 3-SAT.

CLIQUE decision problem:

Input: graph G = (V, E) and integer k.

Question: does G contain a clique of size k (a set of k vertices all pairwise adjacent)?

3-SAT instance: φ with m clauses C₁,…,Cₘ, each clause has 3 literals.

We will construct (G, k) such that φ is satisfiable ⇔ G has a clique of size k.

1. Construction f(φ):

   For each clause Cᵢ and each literal ℓ in Cᵢ, create a vertex v(i, ℓ).

   So there are 3m vertices total (one per literal occurrence).
2. Add edges to represent compatibility:

   Connect v(i, ℓ) to v(j, ℓ′) iff:

   - •i ≠ j (they come from different clauses), and
   - •ℓ is not the negation of ℓ′ (they are logically consistent).

   In other words, do NOT connect contradictory literals like x and ¬x.
3. Set k = m (we want to pick one literal from each clause).
4. Polynomial time check:

   We create O(m) vertices and compare pairs across clauses.

   There are O((3m)²) = O(m²) potential edges, each decided by a constant-time consistency check.

   So the construction is polynomial in m (and in the size of φ).
5. Correctness (→): assume φ is satisfiable.

   Then there exists a truth assignment that makes every clause true.

   For each clause Cᵢ, pick one literal ℓᵢ in Cᵢ that is true under the assignment.

   Consider the vertices v(i, ℓᵢ) for i = 1…m.

   Any two chosen literals are simultaneously true, so they cannot be contradictory.

   Thus for i ≠ j, v(i, ℓᵢ) is connected to v(j, ℓⱼ).

   Therefore these m vertices form a clique of size m.
6. Correctness (←): assume G has a clique of size m.

   Because edges only connect vertices from different clauses, the clique can contain at most one vertex per clause.

   Having size m implies it contains exactly one vertex from each clause: v(1, ℓ₁), …, v(m, ℓₘ).

   Because it is a clique, no pair (ℓᵢ, ℓⱼ) is contradictory.

   Now define an assignment by setting variables to satisfy all selected literals (this is consistent because no contradictions appear).

   Then each clause Cᵢ has its selected literal ℓᵢ satisfied, so every clause is satisfied.

   Hence φ is satisfiable.

**Insight:** This reduction turns “choose one true literal per clause, consistently” into “choose one vertex per clause that are all pairwise compatible.” CLIQUE’s pairwise adjacency condition is doing the global consistency work.

### Reduction 3-SAT ≤ₚ VERTEX COVER (via CLIQUE/INDEPENDENT SET identities)

Goal: show VERTEX COVER is NP-complete. We’ll focus on the hardness part using a chain of reductions.

VERTEX COVER decision problem:

Input: graph G = (V, E) and integer k.

Question: is there a set S ⊆ V with |S| ≤ k such that every edge has at least one endpoint in S?

We will use known relationships between:

- •CLIQUE
- •INDEPENDENT SET
- •VERTEX COVER

Key graph facts:

1) S is an independent set in G ⇔ V \ S is a vertex cover in G.

2) S is a clique in G ⇔ S is an independent set in the complement graph G̅.

We’ll start from the previous example: 3-SAT ≤ₚ CLIQUE.

1. Step A: CLIQUE ≤ₚ INDEPENDENT SET

   Given an instance (G, k) of CLIQUE, construct the complement graph G̅.

   Set k′ = k.

   Claim:

   G has a clique of size k ⇔ G̅ has an independent set of size k.
2. Proof of the claim:

   Let S ⊆ V.

   S is a clique in G means:

   ∀u, v ∈ S with u ≠ v, (u, v) ∈ E(G).

   In the complement graph:

   (u, v) ∈ E(G̅) ⇔ (u, v) ∉ E(G).

   So:

   S is a clique in G

   ⇔ ∀u ≠ v in S, (u, v) ∉ E(G̅)

   ⇔ S is an independent set in G̅.
3. Polynomial time:

   Constructing G̅ takes O(|V|²) time if using an adjacency matrix (or similar polynomial time in the input size).
4. Step B: INDEPENDENT SET ≤ₚ VERTEX COVER

   Given (H, k) for INDEPENDENT SET, output (H, |V(H)| − k) for VERTEX COVER.

   Claim:

   H has an independent set of size k ⇔ H has a vertex cover of size |V| − k.
5. Proof of the claim:

   (→) Suppose S is an independent set with |S| = k.

   Consider T = V \ S.

   Any edge cannot have both endpoints in S (since S is independent), so every edge has at least one endpoint in T.

   Thus T is a vertex cover.

   And |T| = |V| − |S| = |V| − k.

   (←) Suppose T is a vertex cover with |T| = |V| − k.

   Let S = V \ T.

   If there were an edge entirely within S, that edge would have neither endpoint in T, contradicting that T covers all edges.

   So S is independent and |S| = k.
6. Chain them:

   3-SAT ≤ₚ CLIQUE ≤ₚ INDEPENDENT SET ≤ₚ VERTEX COVER.

   By transitivity of ≤ₚ:

   3-SAT ≤ₚ VERTEX COVER.

   So VERTEX COVER is NP-hard.
7. Finish NP-completeness with membership:

   VERTEX COVER ∈ NP because a certificate is the set S of vertices, and a verifier checks in O(|E|) time that every edge has an endpoint in S.

**Insight:** Not every NP-completeness proof needs a fresh gadget reduction. Sometimes you can reuse a powerful reduction once (like 3-SAT ≤ₚ CLIQUE) and then move between graph problems using crisp equivalences.

### Reduction SAT ≤ₚ 3-SAT (sketch with correctness structure)

Goal: justify why 3-SAT can be used as a canonical NP-complete source.

We want a polynomial-time transformation that takes an arbitrary Boolean formula φ and outputs a 3-CNF formula ψ such that:

φ is satisfiable ⇔ ψ is satisfiable.

A full construction has multiple stages (e.g., convert to CNF, then to 3-CNF). Here we focus on the core 3-literal clause normalization step that preserves satisfiability.

1. Assume we already have a CNF formula:

   φ = ∧ᵢ Cᵢ

   where each clause Cᵢ is a disjunction of literals and may have length rᵢ different from 3.
2. Case 1: clause length r = 1.

   C = (ℓ)

   Convert to:

   (ℓ ∨ a ∨ b) ∧ (ℓ ∨ a ∨ ¬b) ∧ (ℓ ∨ ¬a ∨ b) ∧ (ℓ ∨ ¬a ∨ ¬b)

   for fresh variables a, b.

   Reason:

   - •If ℓ is true, all four clauses are true.
   - •If ℓ is false, then the four clauses require all combinations of a, b simultaneously, impossible.

   So the conjunction is satisfiable ⇔ ℓ is satisfiable.
3. Case 2: clause length r = 2.

   C = (ℓ₁ ∨ ℓ₂)

   Convert to:

   (ℓ₁ ∨ ℓ₂ ∨ a) ∧ (ℓ₁ ∨ ℓ₂ ∨ ¬a)

   for fresh a.

   Reason:

   - •If (ℓ₁ ∨ ℓ₂) is true, set a arbitrarily and satisfy both.
   - •If (ℓ₁ ∨ ℓ₂) is false, then both clauses become (a) and (¬a), impossible.

   So satisfiable ⇔ satisfiable.
4. Case 3: clause length r > 3.

   C = (ℓ₁ ∨ ℓ₂ ∨ … ∨ ℓᵣ)

   Introduce fresh variables y₁,…,yᵣ₋₃ and replace C by:

   (ℓ₁ ∨ ℓ₂ ∨ y₁) ∧ (¬y₁ ∨ ℓ₃ ∨ y₂) ∧ … ∧ (¬yᵣ₋₄ ∨ ℓᵣ₋₂ ∨ yᵣ₋₃) ∧ (¬yᵣ₋₃ ∨ ℓᵣ₋₁ ∨ ℓᵣ)

   Reason (→):

   If C is true, pick the first true literal among ℓⱼ and set the y’s to satisfy the chain.

   Reason (←):

   If the chain is satisfiable, at least one ℓⱼ must be true; otherwise the chain forces contradictions through y variables.
5. Polynomial size/time:

   Each clause of length r becomes O(r) clauses, using O(r) fresh variables.

   Total blow-up is linear in the total number of literals across all clauses, hence polynomial.

**Insight:** The heart of SAT ≤ₚ 3-SAT is the idea of adding fresh variables to ‘thread’ a long clause into a chain of 3-clauses without changing satisfiability. You preserve the existence of a satisfying assignment, not necessarily the exact same set of satisfying assignments.

## Key Takeaways

- ✓

  NP-complete means: (i) the problem is in NP (poly-time verifiable), and (ii) every NP problem reduces to it via ≤ₚ.
- ✓

  A polynomial-time many-one reduction A ≤ₚ B is a poly-time computable function f with x ∈ A ⇔ f(x) ∈ B.
- ✓

  To prove a new problem X is NP-hard, reduce from a known NP-complete problem A to X (A ≤ₚ X), not the other way around.
- ✓

  Correctness of reductions is almost always proven by two implications: YES(A) → YES(B) and YES(B) → YES(A).
- ✓

  SAT is NP-complete by Cook–Levin; 3-SAT is NP-complete and is a convenient hub for gadget reductions.
- ✓

  Reductions must be efficient: both runtime of f and the size ‖f(x)‖ must be polynomial in ‖x‖.
- ✓

  Once a problem is NP-complete, the usual next steps are approximation, parameterization, special cases, or practical solvers—not expecting a general exact poly-time algorithm.

## Common Mistakes

- ✗

  Reversing the reduction direction: proving X ≤ₚ 3-SAT does not show X is NP-hard; you need 3-SAT ≤ₚ X (or another known NP-complete source).
- ✗

  Forgetting to prove X ∈ NP (verifiability) and only proving NP-hardness, which gives NP-hard but not NP-complete.
- ✗

  Using a reduction that implicitly solves the source problem (e.g., ‘pick a satisfying assignment’ during construction), which violates the polynomial-time construction requirement.
- ✗

  Not proving both directions of correctness (→ and ←), leaving a gap where the constructed instance might introduce or lose solutions.

## Practice

easy

Show that 3-SAT ≤ₚ INDEPENDENT SET by composing known reductions, and state the resulting k parameter in the INDEPENDENT SET instance.

**Hint:** Use the worked example 3-SAT ≤ₚ CLIQUE and the fact that CLIQUE in G corresponds to INDEPENDENT SET in the complement graph G̅ with the same k.

Show solution

From the worked example, build (G, k) from φ with k = m (number of clauses) such that φ satisfiable ⇔ G has a clique of size m.

Now map (G, m) to (G̅, m).

Because S is a clique in G ⇔ S is an independent set in G̅, we get:

φ satisfiable ⇔ G̅ has an independent set of size m.

Thus 3-SAT ≤ₚ INDEPENDENT SET with k = m.

easy

Prove that VERTEX COVER ∈ NP by explicitly describing a certificate and a polynomial-time verifier. Give a runtime bound in terms of |V| and |E|.

**Hint:** The certificate can be the set S of chosen vertices. The verifier checks every edge.

Show solution

Certificate: a list (or bitmask) indicating a set S ⊆ V with |S| ≤ k.

Verifier V(G, k, S):

1) Check |S| ≤ k.

2) For each edge (u, v) ∈ E, check whether u ∈ S or v ∈ S; if any edge fails, reject.

If all edges pass, accept.

Runtime: step (1) is O(|V|) or O(|S|); step (2) checks each edge once, O(|E|), with O(1) membership tests if using a bitmask/boolean array. Total O(|V| + |E|), polynomial.

medium

Let A, B, C be decision problems. Suppose A ≤ₚ B and B ≤ₚ C. Prove that A ≤ₚ C (transitivity) by explicitly constructing the reduction function and showing it is polynomial-time.

**Hint:** Compose the two reduction functions: f from A to B and g from B to C. Use that poly(poly(n)) is poly(n).

Show solution

Given A ≤ₚ B via f and B ≤ₚ C via g.

Define h(x) = g(f(x)).

Correctness:

x ∈ A ⇔ f(x) ∈ B (definition of f)

⇔ g(f(x)) ∈ C (definition of g)

⇔ h(x) ∈ C.

Polynomial time:

If f runs in time p(‖x‖) and outputs size ‖f(x)‖ ≤ q(‖x‖), and g runs in time r(‖y‖) on input y, then g(f(x)) runs in time r(‖f(x)‖) ≤ r(q(‖x‖)).

Total time = p(‖x‖) + r(q(‖x‖)), which is polynomial in ‖x‖ because compositions/sums of polynomials are polynomials. Hence A ≤ₚ C.

## Connections

- •Next: [Approximation Algorithms](/tech-tree/approximation-algorithms/) — what to do when exact optimality is NP-hard.
- •Related application domain: [Graph Coloring](/tech-tree/graph-coloring/) — many coloring variants are NP-complete; reductions often start from 3-SAT.
- •Deeper theory: [Computational Complexity Theory](/tech-tree/computational-complexity/) — extends reduction thinking to other resources (space, randomness, circuits) and richer completeness notions.

Quality: A (4.5/5)

[← back to tree](/tech-tree/)[browse all →](/tech-tree/inventory/)
