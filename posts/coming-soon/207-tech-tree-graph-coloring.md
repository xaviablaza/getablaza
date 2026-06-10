---
title: Graph Coloring
description: Assigning colors so adjacent vertices differ. Chromatic number.
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
permalink: /tech-tree/graph-coloring/
---

[←Back to Tech Tree](/tech-tree/)

[inventory](/tech-tree/inventory/)[coverage](/tech-tree/coverage/)

# Graph Coloring

Graph TheoryDifficulty: ★★★★☆Depth: 5Unlocks: 0

Assigning colors so adjacent vertices differ. Chromatic number.

## Interactive Visualization

⏮◀◀▶▶STEP0.25x1xZOOM

t=0s

## Core Concepts

- -Proper vertex coloring: assigning a color to each vertex so every edge connects differently colored vertices.
- -Chromatic number: the smallest number of colors required for a proper vertex coloring of a graph.
- -Color class (independent-set) view: a coloring is a partition of the vertex set into independent sets (no edges inside a class).

## Key Symbols & Notation

chi(G) - notation for the chromatic number of graph G

## Essential Relationships

- -chi(G) equals the minimum k such that G has a proper k-coloring (equivalently, G can be partitioned into k independent sets).

## Prerequisites (2)

[NP-Completeness6 atoms](/tech-tree/np-completeness/)[Graph Traversal5 atoms](/tech-tree/graph-traversal/)

Advanced Learning Details

### Graph Position

97

Depth Cost

0

Fan-Out (ROI)

0

Bottleneck Score

5

Chain Length

### Cognitive Load

5

Atomic Elements

26

Total Elements

L0

Percentile Level

L3

Atomic Level

### All Concepts (9)

- - Proper vertex coloring: an assignment of colors to vertices such that every pair of adjacent vertices have different colors
- - k-coloring: a proper coloring that uses at most k distinct colors
- - Chromatic number χ(G): the minimum k for which G admits a k-coloring
- - Color class: the set of vertices that all receive the same color in a coloring
- - Independent set (stable set): a set of vertices with no edges among them (used as color classes)
- - k-colorability decision problem: the decision problem 'does G admit a k-coloring?'
- - Proper coloring as a mapping: viewing a coloring as a function from vertices to a finite palette of color labels (formal functional viewpoint)
- - Clique and clique number ω(G): a clique is a complete subgraph; ω(G) is the size of the largest clique (used as a lower bound for χ(G))
- - Complete graph K\_n as an extremal example for coloring (every pair adjacent)

### Teaching Strategy

Quick unlock - significant prerequisite investment but simple final step. Verify prerequisites first.

Graph coloring looks like a simple puzzle—paint vertices so neighbors clash—but it quietly connects scheduling, register allocation, planar maps, and the boundary between what we can solve efficiently and what’s NP-complete.

TL;DR:

A proper vertex coloring assigns colors to vertices so adjacent vertices differ. The chromatic number χ(G) is the minimum number of colors needed. A coloring is equivalently a partition of V into independent sets. Finding χ(G) is NP-hard in general, but there are strong bounds, special graph classes with efficient algorithms, and practical heuristics that often work well.

## What Is Graph Coloring?

### Why this concept exists

Many real problems have the same underlying constraint: **some pairs of items cannot share the same resource**.

- •Exams that share students can’t be scheduled in the same time slot.
- •Variables that are simultaneously “live” in a program can’t use the same CPU register.
- •Frequencies assigned to nearby radio towers can’t interfere.

Graph coloring turns “cannot share” constraints into edges, and “resources” into colors.

### Core definition: proper vertex coloring

Let G = (V, E) be an undirected graph.

A **proper vertex coloring** is a function

c : V → {1, 2, …, k}

such that for every edge (u, v) ∈ E,

c(u) ≠ c(v).

If such a c exists, we say **G is k-colorable**.

### Chromatic number χ(G)

The **chromatic number** χ(G) is the smallest k for which G is k-colorable:

χ(G) = min { k : G is k-colorable }.

This is an optimization version of a decision problem:

- •**k-COLORING (decision):** “Is χ(G) ≤ k?”
- •**CHROMATIC NUMBER (optimization):** “What is χ(G)?”

You already know NP-completeness; graph coloring is a classic member of that family.

### A grounding intuition: colors are “time slots”

Thinking of color i as “time slot i,” the constraint c(u) ≠ c(v) says: if two vertices conflict (edge), they can’t occupy the same slot.

This viewpoint will matter later when we talk about reductions and why coloring is hard.

### Two small but important edge cases

1) **Edgeless graph** (E = ∅): no constraints. Every vertex can share the same color.

χ(G) = 1 (unless V is empty; conventions vary, but typically χ(∅) = 0).

2) **Complete graph** Kₙ: every pair conflicts.

χ(Kₙ) = n.

Those are extremes: from “everything compatible” to “nothing compatible.” Most graphs live in between.

### Vocabulary: color classes

Given a coloring c with k colors, define the set of vertices with each color:

Cᵢ = { v ∈ V : c(v) = i }.

Each Cᵢ is called a **color class**.

We’ll soon see that each color class must be an **independent set** (no edges inside it), which gives a powerful alternate lens.

## Core Mechanic 1: The Independent-Set (Partition) View

### Why this view is useful

The function definition c : V → {1..k} is clean, but it hides structure.

A k-coloring doesn’t just label vertices—it **groups** them into k buckets. The key is that each bucket must be internally conflict-free.

This turns coloring into a partition problem:

> **Coloring = partition V into independent sets.**

This perspective is often the quickest route to:

- •proving lower bounds on χ(G)
- •understanding reductions (coloring ↔ clique/independent set)
- •designing heuristics (build large independent sets as color classes)

### Independent sets and color classes

A set S ⊂ V is an **independent set** if ∀u, v ∈ S, (u, v) ∉ E.

Now connect that to coloring.

**Claim:** In any proper coloring, each color class Cᵢ is an independent set.

**Reason:** Suppose there is an edge (u, v) with u, v ∈ Cᵢ. Then c(u) = c(v) = i, violating properness.

So properness ⇔ “no edges inside any color class.”

### Equivalence statement (bidirectional)

We can make the equivalence explicit.

**Proposition:** G is k-colorable iff V can be partitioned into k independent sets.

**(⇒)** Given a k-coloring, sets C₁, …, C\_k partition V, and each Cᵢ is independent (as shown).

**(⇐)** Given a partition V = I₁ ⊔ I₂ ⊔ … ⊔ I\_k into independent sets, define c(v) = i for v ∈ Iᵢ. Any edge (u, v) cannot lie within the same Iᵢ (independence), so c(u) ≠ c(v). Proper coloring.

This equivalence is simple, but it unlocks many bounds.

### Lower bounds from cliques

A **clique** is a set of vertices all mutually adjacent.

If a graph contains a clique of size ω(G), then all those vertices must receive different colors.

So:

χ(G) ≥ ω(G).

This is often the first lower bound you try.

### Lower bounds from vertex count and independent set size

Let α(G) be the size of a maximum independent set.

If each color class is an independent set of size at most α(G), then k color classes cover at most k·α(G) vertices.

To cover all |V| vertices, we need:

k·α(G) ≥ |V| ⇒ k ≥ |V| / α(G).

Thus:

χ(G) ≥ ⌈ |V| / α(G) ⌉.

This bound is sometimes stronger than the clique bound (especially in sparse graphs).

### Upper bounds from greedy coloring

A simple way to build a coloring is to order vertices and assign each vertex the smallest available color not used by its colored neighbors. This is **greedy coloring**.

Greedy always succeeds with at most Δ(G) + 1 colors, where Δ(G) is maximum degree.

Reason (local constraint): when coloring a vertex v, at most Δ(G) neighbors are already colored, so at most Δ(G) colors are “blocked.” With Δ(G) + 1 colors, some color is free.

So:

χ(G) ≤ Δ(G) + 1.

This bound is not always tight, but it’s universal and constructive.

### A big theorem you should know (without proof)

**Brooks’ theorem (informal):** For a connected graph that is neither a complete graph nor an odd cycle,

χ(G) ≤ Δ(G).

This is a deep strengthening of the greedy Δ + 1 bound.

You don’t need the proof yet, but you should remember the shape: only two families (cliques, odd cycles) force Δ + 1 colors.

### Complement graphs: coloring ↔ clique

Let Ḡ be the complement graph: same vertices, edges are exactly the non-edges of G.

In Ḡ, a clique corresponds to an independent set in G, and vice versa.

That means:

- •independent set in G ⇔ clique in Ḡ
- •partition into independent sets in G ⇔ cover by cliques in Ḡ

This is part of why coloring is entangled with other NP-hard problems: clique and independent set are also NP-hard.

### Takeaway from this mechanic

The partition view helps you reason about coloring without “colors” at all:

- •A **k-coloring** is k independent sets that cover V.
- •A **lower bound** often comes from “some set of vertices can’t share a color.”
- •An **upper bound** often comes from “here is a constructive procedure.”

## Core Mechanic 2: Complexity, Decision vs Optimization, and Reductions

### Why complexity matters here

In practice, you’ll often want:

- •the fewest time slots
- •the fewest registers
- •the smallest number of frequencies

That is exactly χ(G). Unfortunately, **computing χ(G) is NP-hard**. So the learning goal is twofold:

1) know what can be solved efficiently (special cases, approximations, bounds)

2) know how to reason about hardness and reductions

### The decision problem: k-COLORING

Given (G, k), ask whether χ(G) ≤ k.

- •For k = 1: easy (only possible if E = ∅)
- •For k = 2: easy (bipartite test via BFS/DFS)
- •For k ≥ 3: NP-complete

The shift from 2 to 3 is one of the most important “phase transitions” in graph algorithms.

### 2-coloring as a warm-up: bipartite graphs

A graph is 2-colorable iff it is bipartite iff it has no odd cycle.

BFS-based 2-coloring algorithm:

- •pick a start vertex, color it 0
- •BFS outward, alternate colors by distance parity
- •if you ever see an edge (u, v) with the same color, you found an odd cycle → not bipartite

This is polynomial-time and illustrates a theme: **adding just one more color destroys tractability**.

### Why 3-coloring is hard (high-level reduction story)

You already know reductions from SAT / 3-SAT. The typical plan for showing 3-COLORING NP-complete is:

- •Build a graph gadget for each variable and clause
- •Force each variable to choose between two “truth” colors
- •Force each clause to be satisfied, otherwise a conflict prevents proper coloring

We won’t re-derive the full gadget construction in detail here, but you should internalize the *shape*:

- •Graph structure encodes logic constraints.
- •A proper coloring corresponds to a satisfying assignment.

This “encoding constraints as edges” idea mirrors real applications.

### Optimization is at least as hard

If you can compute χ(G), you can answer k-COLORING by checking whether χ(G) ≤ k.

So CHROMATIC NUMBER is NP-hard.

Also, k-COLORING is NP-complete for k ≥ 3, so unless P = NP, we should not expect a general efficient algorithm.

### Approximation landscape (what is and isn’t feasible)

Even approximating χ(G) is difficult.

Some key facts (stated informally):

- •There is no known polynomial-time algorithm that always colors with exactly χ(G) colors.
- •For general graphs, strong inapproximability results exist: achieving a good approximation factor is NP-hard (and under stronger assumptions, even harder).

So in practice you combine:

- •easy bounds (clique, Δ + 1)
- •exact algorithms on small graphs (branch-and-bound)
- •heuristics (greedy with smart ordering, DSATUR)
- •exploit special structure (planar, interval, chordal)

### A practical bridge: certificates

Even though finding χ(G) is hard, **verifying a given coloring uses O(|E|)** checks:

For each edge (u, v) ∈ E, confirm c(u) ≠ c(v).

So “G is k-colorable” is in NP: the certificate is the coloring itself.

This is the usual NP pattern: hard to find, easy to check.

### Parameter k as a lever

You can also treat k as a parameter.

- •When k is fixed small (like 3), decision remains NP-complete.
- •But in parameterized complexity, some algorithms are efficient in n for fixed k on certain graph families.

Even without full parameterized theory, the intuition is useful:

- •If you only ever need k = 2, you’re safe (polynomial).
- •If you might need k = 3, you’re in NP-complete territory.

### Takeaway from this mechanic

Graph coloring is a “complexity landmark.”

- •2-coloring is efficiently solvable via BFS/DFS.
- •3-coloring and beyond encode SAT-like constraint logic.
- •Exact solutions exist, but typically require exponential-time search in the worst case.

## Applications and Connections: Scheduling, Register Allocation, and Special Graph Classes

### Why applications look different but reduce to coloring

In applications you rarely see “color this graph.” You see:

- •“minimize the number of time slots”
- •“minimize register pressure”
- •“avoid frequency interference”

The reduction recipe:

1) Make a vertex for each item to be assigned a resource.

2) Add an edge between items that cannot share a resource.

3) A color is a resource bucket.

Then χ(G) is the minimum number of resource buckets.

### Example application patterns

#### 1) Exam / meeting scheduling

Vertices = exams.

Edge between exams that share at least one student.

Color = time slot.

Proper coloring ensures no student has two exams at the same time.

#### 2) Register allocation (compiler)

Vertices = program variables.

Edge if two variables are simultaneously live.

Color = CPU register.

If χ(G) exceeds available registers, compilers may “spill” variables to memory.

#### 3) Frequency assignment

Vertices = transmitters.

Edge if too close in space/spectrum to share frequency.

Color = frequency channel.

### Heuristics you’ll actually use

Because χ(G) is hard, real systems use heuristics.

#### Greedy coloring with smart ordering

Greedy depends heavily on vertex order.

Common orderings:

| Ordering | Idea | When it helps |
| --- | --- | --- |
| Largest degree first | color high-degree constraints early | dense graphs |
| Smallest degree first | keep options open (sometimes) | sparse graphs |
| Degeneracy ordering | guarantees ≤ d + 1 colors where d is degeneracy | many real sparse graphs |
| DSATUR | choose vertex with highest “saturation” (distinct neighbor colors) | often near-optimal in practice |

#### DSATUR intuition

A vertex with many differently colored neighbors has fewer remaining choices. Coloring it next reduces the chance of getting stuck and often reduces total colors.

DSATUR is also used in exact branch-and-bound solvers as a strong branching heuristic.

### Special graph classes where χ(G) is tractable

The general problem is hard, but structure can make it easy.

#### Bipartite graphs

χ(G) is 1 or 2, found by BFS/DFS.

#### Interval graphs

Graphs where vertices are intervals on a line, edges mean overlap.

χ(G) equals the size of the maximum clique ω(G), and optimal coloring can be found greedily by sorting intervals by start/end times.

Why: overlaps behave like “simultaneous resource usage,” and cliques capture peak overlap.

#### Chordal graphs

Graphs with no induced cycles of length ≥ 4.

They have a perfect elimination ordering. Using that ordering, greedy coloring is optimal, and again χ(G) = ω(G).

#### Planar graphs

Planar graphs satisfy the **Four Color Theorem**:

χ(G) ≤ 4.

- •Determining whether a planar graph is 3-colorable is still NP-complete.
- •But 4-colorability is guaranteed, which gives a constant upper bound.

This matters when your conflict graph comes from geographic adjacency.

### Bounds you should combine in practice

When you face a graph instance, useful quick diagnostics:

- •Lower bound: ω(G)
- •Lower bound: ⌈|V| / α(G)⌉ (if you can estimate α(G))
- •Upper bound: greedy colors used (with good ordering)
- •Upper bound: Δ(G) + 1 (always)

If lower and upper meet, you have χ(G) exactly.

### Connection to traversal prerequisites

Your BFS/DFS knowledge matters because:

- •2-coloring is essentially BFS parity labeling.
- •Many heuristics and exact algorithms rely on repeated neighborhood queries and exploring subproblems, where traversal concepts help.

### Connection to NP-completeness prerequisites

Reductions are the language for explaining why k-coloring is hard:

- •SAT constraints become graph gadgets.
- •A graph coloring becomes a satisfying assignment.

This is one of the cleanest places to practice reduction thinking.

## Worked Examples (3)

### Example 1: Compute χ(G) for a cycle and see the odd/even split

Let G be the cycle C₆ (6 vertices in a loop) and H be the cycle C₅ (5 vertices in a loop). Determine χ(C₆) and χ(C₅).

1. Step 1: Try 2-coloring C₆.

   Label vertices v₁…v₆ in order around the cycle.

   Assign c(v₁)=1.

   Then to satisfy edges:

   c(v₂)=2, c(v₃)=1, c(v₄)=2, c(v₅)=1, c(v₆)=2.

   Now check the closing edge (v₆, v₁): c(v₆)=2 and c(v₁)=1, OK.
2. Step 2: Conclude χ(C₆)=2.

   C₆ has edges, so χ(C₆) ≠ 1.

   We exhibited a proper 2-coloring, so χ(C₆) ≤ 2.

   Therefore χ(C₆)=2.
3. Step 3: Try the same on C₅.

   Label v₁…v₅.

   Set c(v₁)=1.

   Then forced alternation gives:

   c(v₂)=2, c(v₃)=1, c(v₄)=2, c(v₅)=1.

   Now check the closing edge (v₅, v₁): c(v₅)=1 and c(v₁)=1, conflict.
4. Step 4: Conclude C₅ is not 2-colorable ⇒ χ(C₅) ≥ 3.

   The conflict is unavoidable because the parity alternation around an odd cycle forces the last vertex to match the first.
5. Step 5: Show χ(C₅)=3 by constructing a 3-coloring.

   For instance:

   c(v₁)=1, c(v₂)=2, c(v₃)=1, c(v₄)=2, c(v₅)=3.

   Now every edge has different colors, so χ(C₅) ≤ 3.

   Thus χ(C₅)=3.

**Insight:** Cycles perfectly illustrate the jump from 2-colorable to needing 3: even cycles are bipartite (χ=2), odd cycles are not (χ=3). This is the simplest manifestation of “odd cycle obstruction.”

### Example 2: Use bounds (clique, Δ+1, greedy) to pin down χ(G)

Consider a graph G with vertices {a,b,c,d,e} and edges forming a triangle on {a,b,c} plus edges (c,d), (d,e), (e,c). So {c,d,e} also forms a triangle except missing (c,e)? Actually edges include (c,d), (d,e), (e,c), so it is a triangle. The graph is two triangles sharing vertex c: triangle abc and triangle cde.

1. Step 1: Find a clique lower bound.

   Vertices {a,b,c} form a clique of size 3.

   Vertices {c,d,e} also form a clique of size 3.

   So ω(G)=3 ⇒ χ(G) ≥ 3.
2. Step 2: Compute maximum degree Δ(G).

   Deg(a)=2 (b,c)

   Deg(b)=2 (a,c)

   Deg(c)=4 (a,b,d,e)

   Deg(d)=2 (c,e)

   Deg(e)=2 (c,d)

   So Δ(G)=4 ⇒ χ(G) ≤ Δ(G)+1=5 (universal bound).
3. Step 3: Try a greedy coloring to improve the upper bound.

   Choose an order that starts with high degree: c, a, b, d, e.

   Color c with 1.

   Color a (adjacent to c) with 2.

   Color b (adjacent to c and a): cannot use 1 (c), cannot use 2 (a) ⇒ use 3.

   Color d (adjacent to c): cannot use 1 ⇒ can use 2.

   Color e (adjacent to c and d): cannot use 1 (c), cannot use 2 (d) ⇒ can use 3.
4. Step 4: Conclude χ(G)=3.

   We constructed a proper 3-coloring ⇒ χ(G) ≤ 3.

   Combined with χ(G) ≥ 3 from the clique bound, we get χ(G)=3 exactly.

**Insight:** In many graphs, simple lower bounds (ω(G)) and a decent greedy upper bound meet quickly. When they do, you’ve solved an NP-hard problem instance without heavy machinery.

### Example 3: Translate scheduling into coloring, then interpret color classes

You have 6 exams: {M, P, C, H, B, E}. Conflicts (shared students) are:

(M,P), (M,C), (P,C), (P,H), (C,H), (H,B), (B,E).

Model as a graph and find a coloring with few time slots; interpret each color class as a set of exams that can be scheduled together.

1. Step 1: Build the conflict graph G.

   Vertices are the exams.

   Edges are exactly the listed conflict pairs.

   A time slot assignment is a proper coloring c: V → {1..k}.
2. Step 2: Identify an obvious clique lower bound.

   {M,P,C} form a triangle because edges (M,P), (M,C), (P,C) all exist.

   So ω(G) ≥ 3 ⇒ χ(G) ≥ 3.

   At least 3 time slots are necessary.
3. Step 3: Construct a 3-coloring.

   Let’s try:

   Color 1: P

   Then M cannot be 1 (edge M–P) ⇒ set M=2.

   C conflicts with P and M ⇒ cannot be 1 or 2 ⇒ set C=3.

   H conflicts with P and C ⇒ cannot be 1 or 3 ⇒ set H=2.

   B conflicts with H ⇒ cannot be 2 ⇒ set B=1.

   E conflicts with B ⇒ cannot be 1 ⇒ set E=2 (or 3).

   So one valid coloring is:

   P=1, M=2, C=3, H=2, B=1, E=2.
4. Step 4: Read off the time slots as color classes.

   Slot 1: {P, B}

   Slot 2: {M, H, E}

   Slot 3: {C}

   Verify quickly: no conflicts within each slot because edges only connect different colors.

**Insight:** The independent-set view is exactly the scheduling interpretation: each time slot is an independent set of exams (no pair in conflict). Coloring is not just labeling—it’s partitioning into compatible batches.

## Key Takeaways

- ✓

  A proper vertex coloring assigns colors so every edge connects differently colored vertices.
- ✓

  The chromatic number χ(G) is the minimum number of colors needed; it’s easy to verify a coloring, hard to find the minimum in general.
- ✓

  A k-coloring is equivalent to partitioning V into k independent sets (color classes).
- ✓

  Lower bounds: χ(G) ≥ ω(G) (clique number) and χ(G) ≥ ⌈|V| / α(G)⌉ (independent-set size bound).
- ✓

  Upper bounds: greedy coloring gives a constructive bound; universally χ(G) ≤ Δ(G) + 1, and often χ(G) ≤ Δ(G) (Brooks’ theorem exceptions aside).
- ✓

  2-coloring is exactly bipartiteness and is solvable via BFS/DFS; 3-coloring is NP-complete.
- ✓

  Practical coloring relies on heuristics (good orderings, DSATUR) and exploiting special graph structure (interval/chordal/planar).

## Common Mistakes

- ✗

  Confusing χ(G) (minimum colors) with “colors used by my greedy run” (an upper bound that can be non-optimal).
- ✗

  Assuming χ(G) = Δ(G) + 1 always; many graphs need far fewer colors (even when Δ is large).
- ✗

  Forgetting the partition view: a color class must be an independent set; if you see an edge inside a class, the coloring is invalid.
- ✗

  Mixing up vertex coloring with edge coloring (a different problem with different theorems and bounds).

## Practice

easy

Show that for any graph G, χ(G) ≥ ω(G). Then give a graph where the inequality is strict (χ(G) > ω(G)).

**Hint:** In a clique, every pair of vertices is adjacent. For strictness, think of an odd cycle.

Show solution

Proof: Let K be a clique of size ω(G). In a proper coloring, adjacent vertices must have different colors. Since every pair in K is adjacent, all vertices in K must have distinct colors, requiring at least ω(G) colors. Hence χ(G) ≥ ω(G).

Strict example: G = C₅. Then ω(C₅)=2 (no triangle), but χ(C₅)=3 because odd cycles are not 2-colorable.

medium

Let G be a graph with |V| = 20 and α(G) = 5. Prove that χ(G) ≥ 4 using the independent-set bound. Is it possible that χ(G) = 4? Briefly justify.

**Hint:** Use k·α(G) ≥ |V| for k color classes that are independent sets.

Show solution

Each color class is an independent set, so it has size ≤ α(G)=5. If G is k-colored, then the k color classes cover all vertices:

|V| ≤ ∑ᵢ |Cᵢ| ≤ ∑ᵢ α(G) = k·α(G).

So k ≥ |V|/α(G) = 20/5 = 4.

Thus χ(G) ≥ ⌈4⌉ = 4.

Yes, χ(G) could equal 4 if there exists a partition of V into 4 independent sets of size 5 (or smaller). The bound does not guarantee existence; it only rules out needing fewer than 4 colors.

hard

You are given a graph G and an integer k = 2. Design an algorithm using BFS/DFS that either returns a valid 2-coloring or returns an odd cycle as a certificate that 2-coloring is impossible.

**Hint:** Use BFS layers (distance parity). When you find an edge connecting same-parity vertices, trace parents to extract a cycle.

Show solution

Algorithm sketch:

1) Initialize color[v] = UNCOLORED and parent[v] = NIL.

2) For each component: pick an uncolored start s, set color[s]=0, run BFS.

3) When exploring edge (u,v):

- •If v uncolored: set color[v]=1−color[u], parent[v]=u, enqueue v.
- •Else if color[v]=color[u]: report an odd cycle.

Odd cycle extraction:

If color[u]=color[v], then u and v have the same parity distance from s in the BFS tree. Let P(u) be the path from u to the root via parent pointers, and P(v) similarly. Find their lowest common ancestor x by marking ancestors of u and walking up from v until you hit a mark. Then the cycle is:

(u → … → x) + (x → … → v) + edge (v,u).

Because both tree paths from x to u and x to v have the same parity, their lengths have the same parity, so the total cycle length is odd.

If BFS finishes with no conflict edges, the coloring is valid and is a proper 2-coloring.

## Connections

Prereqs you’re using here: [NP-Completeness](/tech-tree/np-completeness/), [Graph Traversal: BFS and DFS](/tech-tree/graph-traversal/)

Next nodes that commonly follow coloring:

- •[Independent Set](/tech-tree/independent-set/)
- •[Clique](/tech-tree/clique/)
- •[Planar Graphs](/tech-tree/planar-graphs/)
- •[Graph Coloring Heuristics (DSATUR, greedy orderings)](/tech-tree/graph-coloring-heuristics/)
- •[Constraint Satisfaction Problems](/tech-tree/csp/)

Quality: A (4.5/5)

[← back to tree](/tech-tree/)[browse all →](/tech-tree/inventory/)
