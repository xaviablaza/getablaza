---
title: Strongly Connected Components
description: Maximal sets where every vertex reaches every other.
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
permalink: /tech-tree/strongly-connected/
---

[←Back to Tech Tree](/tech-tree/)

[inventory](/tech-tree/inventory/)[coverage](/tech-tree/coverage/)

# Strongly Connected Components

Graph TheoryDifficulty: ★★★☆☆Depth: 4Unlocks: 0

Maximal sets where every vertex reaches every other.

## Interactive Visualization

⏮◀◀▶▶STEP0.25x1xZOOM

t=0s

## Core Concepts

- -Directed-path reachability: there exists a directed path from vertex u to vertex v
- -Pairwise strong connectivity: two vertices are strongly connected if each reaches the other (mutual reachability)
- -Strongly connected component (SCC): a maximal set of vertices that are pairwise strongly connected

## Key Symbols & Notation

"u ->\* v" to mean "there exists a directed path from u to v"

## Essential Relationships

- -Mutual reachability (u ->\* v and v ->\* u) is an equivalence relation; its equivalence classes are exactly the SCCs (a partition of the vertex set into maximal strongly connected sets)

## Prerequisites (1)

[Graph Traversal5 atoms](/tech-tree/graph-traversal/)

Advanced Learning Details

### Graph Position

38

Depth Cost

0

Fan-Out (ROI)

0

Bottleneck Score

4

Chain Length

### Cognitive Load

5

Atomic Elements

41

Total Elements

L3

Percentile Level

L3

Atomic Level

### All Concepts (18)

- - Directed mutual reachability: for two vertices u and v, u can reach v and v can reach u (paths in both directions).
- - Strongly connected set: a set of vertices in a directed graph in which every pair of vertices is mutually reachable.
- - Strongly connected component (SCC): a maximal strongly connected set (cannot add any other vertex without breaking mutual reachability).
- - Maximality: the idea that an SCC cannot be strictly contained in a larger strongly connected set.
- - SCC as equivalence class: mutual reachability induces an equivalence relation whose equivalence classes are SCCs.
- - Partitioning by SCCs: the vertex set is partitioned into disjoint SCCs that cover all vertices.
- - Weakly connected vs strongly connected: distinction that undirected connectivity of the underlying graph is different from directed mutual reachability.
- - Condensation (component) graph: the graph formed by collapsing each SCC to a single node and keeping edges between components.
- - Condensation is a DAG: the condensation graph has no directed cycles.
- - Kosaraju’s two-pass method (high-level): use DFS finish-time ordering on G, then DFS on the transpose G^T in that order to extract SCCs.
- - Transpose graph: the graph G^T obtained by reversing every edge of G (used in Kosaraju).
- - Tarjan’s single-pass method (high-level): a DFS using discovery times, lowlink values, and a stack to output SCCs on-the-fly.
- - Lowlink value (informal): for a node u, the minimum discovery time reachable from u by following 0+ tree edges then at most one back edge (used to detect SCC roots).
- - Stack invariant in Tarjan: nodes on the stack are those in the current DFS recursion subtree that have not yet been assigned to an SCC.
- - Root condition in Tarjan: a node u is the root of an SCC when lowlink[u] == disc[u]; pop stack to form that SCC.
- - Role of DFS finish times: finish-time ordering gives an order that respects the partial order of SCCs (used by Kosaraju).
- - Classification of edges (in directed DFS) for SCC reasoning: tree, back, forward/cross edges and their effects on lowlink/reachability.
- - Linear-time solvability: SCCs can be found in O(|V|+|E|) time using Kosaraju or Tarjan.

### Teaching Strategy

Self-serve tutorial - low prerequisites, straightforward concepts.

In a directed graph, “being connected” is asymmetric: u might reach v without v being able to get back. Strongly Connected Components (SCCs) are the clean way to carve a directed graph into maximal “mutual reachability” regions—subgraphs where every vertex can get to every other vertex.

TL;DR:

An SCC is a maximal set of vertices where ∀u, v in the set, u → *v and v →* u. SCCs partition the vertices of a directed graph. You can find them in linear time O(V + E) using Kosaraju’s or Tarjan’s algorithm, and collapsing SCCs produces a DAG (the “condensation graph”).

## What Is Strong Connectivity (and an SCC)?

### Why this concept exists (motivation)

In undirected graphs, “connected” naturally means there’s a path between any two nodes, and that relationship is symmetric. Directed graphs break that symmetry: a link u → v lets you go from u to v, but not necessarily back.

This matters in real systems:

- •**Web links**: Page A links to B, but B might not link back.
- •**Program call graphs**: Function f calls g, but g might not call f.
- •**State machines**: You can move from state u to state v, but not always return.

We often want to find **regions of the graph that behave like undirected connectivity**—places where movement is possible in both directions (via directed paths). SCCs are exactly that.

### Directed-path reachability

We’ll use the notation from the node profile:

- •\*\*u →\* v\*\* means: “there exists a directed path from u to v.”

A directed path is a sequence of vertices:

- •u = x₀, x₁, …, xₖ = v such that each edge xᵢ → xᵢ₊₁ exists.

Reachability is:

- •**Reflexive**: u →\* u (via path length 0).
- •**Transitive**: if u → *v and v →* w, then u →\* w.
- •**Not symmetric** in general.

### Pairwise strong connectivity

Two vertices u and v are **strongly connected** if they can reach each other:

- •u → *v and v →* u

This *is* symmetric by definition. Intuitively, u and v are in a “mutual reachability loop,” possibly through many intermediate vertices.

### Strongly Connected Component (SCC)

An SCC is a **maximal** set C of vertices such that every pair in C is strongly connected:

- •∀u, v ∈ C: u → *v and v →* u

“Maximal” means you can’t add any other vertex to C without breaking the property.

### Key structural facts

1. 1)**SCCs form a partition** of the vertex set V.

- •Every vertex belongs to exactly one SCC.

2. 2)If you **contract** each SCC into a single super-node, the resulting graph is a **DAG** (Directed Acyclic Graph). This is called the **condensation graph**.

We’ll justify these facts carefully in the next section.

### A small example to build intuition

Suppose we have edges:

- •1 → 2, 2 → 3, 3 → 1 (a cycle)
- •3 → 4
- •4 → 5, 5 → 4 (another cycle)

Then:

- •{1, 2, 3} is an SCC (everyone reaches everyone via the 3-cycle).
- •{4, 5} is an SCC.
- •There is an edge from SCC({1,2,3}) to SCC({4,5}) because 3 → 4.
- •There is **no** edge back, so they are distinct SCCs.

That “cycle vs one-way bridge” feeling is the core mental model: SCCs are the maximal “mutual reachability islands,” and edges between islands are one-way.

## Core Mechanic 1: SCCs as an Equivalence Relation (and Why They Partition the Graph)

### Why talk about equivalence?

Partitioning is powerful: if SCCs split V into disjoint groups, you can solve many directed-graph problems by working on the smaller “component graph.” To trust that reduction, we need to know SCCs are well-defined and don’t overlap in messy ways.

### Define a relation ~ on vertices

Define u ~ v (“u is strongly connected to v”) iff:

- •u → *v and v →* u

We’ll show ~ is an **equivalence relation**, meaning it is:

- •Reflexive
- •Symmetric
- •Transitive

Once we prove that, the equivalence classes of ~ are exactly the SCCs.

### Reflexive

For any vertex u, u →\* u via the length-0 path. So:

- •u → *u and u →* u

Therefore u ~ u.

### Symmetric

If u ~ v, then by definition:

- •u → *v and v →* u

Swapping u and v gives:

- •v → *u and u →* v

So v ~ u.

### Transitive (the key step)

Assume:

- •u ~ v and v ~ w

Then:

- •u → *v and v →* u
- •v → *w and w →* v

We want to show u ~ w, i.e. u → *w and w →* u.

Use transitivity of reachability:

- •u → *v and v →* w ⇒ u →\* w
- •w → *v and v →* u ⇒ w →\* u

So u ~ w.

### Consequence: SCCs partition V

Equivalence relations partition a set into disjoint equivalence classes.

- •Each vertex belongs to the class of vertices strongly connected to it.
- •Two classes are either identical or disjoint.

These equivalence classes are precisely SCCs:

- •They satisfy pairwise strong connectivity by definition.
- •They are maximal: if a vertex x is strongly connected to some vertex in the class, then x must be in the same equivalence class.

### The condensation graph is a DAG

Now contract each SCC into a super-node. Add a directed edge between SCC A and SCC B if there exists an edge u → v in the original graph with u ∈ A and v ∈ B, A ≠ B.

Claim: the condensation graph has **no directed cycles**.

Proof sketch (by contradiction):

- •Suppose there is a cycle of SCCs: C₁ → C₂ → … → Cₖ → C₁.
- •Then for any u ∈ C₁ and any v ∈ C₂, we have u →\* v (because there is an edge/path from C₁ to C₂).
- •Following around the cycle, we get u →\* u′ for u′ ∈ C₁ through other components, and similarly every component can reach every other component.
- •In particular, vertices across these SCCs would be mutually reachable.

More explicitly: take vertices a ∈ C₁ and b ∈ C₂.

- •Since C₁ → C₂, a →\* b.
- •Since C₂ → … → C₁, b →\* a.

So a and b are strongly connected, meaning they should be in the **same** SCC—contradiction.

Therefore the condensation graph is a DAG.

### Why this matters in practice

This gives a standard workflow:

1. 1)Compute SCCs.
2. 2)Contract SCCs into a DAG.
3. 3)Solve the problem on a DAG (often simpler: topological order, DP, etc.).

Many tasks—deadlock detection, cycle detection in directed graphs, program analysis (mutually recursive functions), dependency resolution—reduce cleanly once you have SCCs.

## Core Mechanic 2: How to Compute SCCs (Kosaraju and Tarjan)

### Why SCC algorithms need more than plain DFS

You already know BFS/DFS explores reachability from a starting node. But SCCs ask for **mutual** reachability and **maximal** sets. A single DFS tree doesn’t directly reveal where the “return paths” exist.

Efficient SCC algorithms exploit a key idea:

- •The SCC structure becomes visible when you consider **finish times** in DFS and/or **low-link** information.

We’ll focus on two classic linear-time algorithms:

- •**Kosaraju’s algorithm** (two DFS passes, uses the transpose graph)
- •**Tarjan’s algorithm** (one DFS pass, uses a stack and low-link values)

Both run in **O(V + E)** time.

---

## Kosaraju’s algorithm (two-pass DFS)

### Intuition

If you collapse SCCs, you get a DAG. In a DAG, there are “sources” with no incoming edges. Kosaraju’s algorithm uses DFS finishing times to find SCCs in an order that effectively peels off those components.

A key tool is the **transpose graph** Gᵀ, where every edge is reversed.

- •If u → v in G, then v → u in Gᵀ.

SCCs are the same in G and Gᵀ (reversing all edges doesn’t change mutual reachability).

### Algorithm steps

Given a directed graph G = (V, E):

1) Run DFS on G, recording vertices in order of **decreasing finish time**.

- •Common implementation: push each vertex onto a list/stack when its DFS call finishes.

2) Build Gᵀ (reverse all edges).

3) Process vertices in the order from step (1) (largest finish time first). For each unvisited vertex v in Gᵀ:

- •Run DFS from v in Gᵀ.
- •The set of vertices reached in this DFS is **one SCC**.

### Why it works (high-level)

The finish-time order from step (1) tends to place vertices from “upstream” SCCs (in the condensation DAG) later, so they are processed first in step (3). When you reverse edges, DFS from a component can’t leak into components that were “downstream” in the original condensation DAG, so each DFS cleanly captures exactly one SCC.

### Complexity

- •DFS on G: O(V + E)
- •Building transpose: O(V + E)
- •DFS on Gᵀ: O(V + E)

Total: O(V + E)

---

## Tarjan’s algorithm (one-pass DFS)

### Intuition

Tarjan discovers SCCs during a single DFS by tracking how far back in the current DFS recursion you can reach.

It maintains:

- •A stack S of “active” vertices in the current DFS search path.
- •An index for each vertex (discovery time).
- •A low-link value low[u]: the smallest discovery index reachable from u by taking:
- •zero or more tree edges (DFS edges), followed by
- •at most one back edge to a vertex still on the stack.

When low[u] equals index[u], u is the root of an SCC: pop from the stack until u.

### The low-link idea (carefully)

Let index[u] be the time u is first discovered.

Initialize:

- •index[u] = low[u] = currentTime
- •push u onto stack, mark onStack[u] = true

For each neighbor v of u:

- •If v is unvisited: DFS(v), then
- •low[u] = min(low[u], low[v])
- •Else if onStack[v] is true (a back edge to active vertex):
- •low[u] = min(low[u], index[v])

When done exploring u:

- •If low[u] == index[u], pop vertices from stack until u; that set is one SCC.

### Complexity

Each edge is examined a constant number of times.

- •Total O(V + E)
- •Often preferred in practice because it’s one pass and doesn’t build Gᵀ.

---

## Kosaraju vs Tarjan (comparison)

| Feature | Kosaraju | Tarjan |
| --- | --- | --- |
| DFS passes | 2 | 1 |
| Needs transpose graph Gᵀ | Yes | No |
| Implementation complexity | Low–medium | Medium |
| Typical use | Teaching, quick implementation | Production, memory-sensitive |
| Outputs SCCs in | Reverse finish-time order (via pass 2) | Order of completion of SCC roots |

### A note on notation and what we actually compute

Even though SCCs are defined via u →\* v (existence of paths), the algorithms never enumerate all paths. They infer SCC structure using DFS properties—this is the power of graph traversal plus the right invariants.

## Application/Connection: What SCCs Enable (and How to Use Them)

### Why SCCs are a “gateway” concept

SCCs turn a messy directed graph into a DAG of components. DAGs are much easier to reason about: they support topological sorting, dynamic programming, and clear notions of “upstream/downstream.”

Below are common patterns where SCCs are the missing piece.

---

## 1) Cycle detection and “where cycles are”

A directed graph has a directed cycle iff it has an SCC with:

- •at least 2 vertices, or
- •1 vertex with a self-loop

Reason: in an SCC, every vertex reaches itself through others, which implies cyclic structure.

So SCCs do more than answer “is there a cycle?”—they locate the **maximal cyclic regions**.

---

## 2) Condensation graph and topological order

Once you contract SCCs, you get a DAG. Many tasks become:

1. 1)Compute SCCs.
2. 2)Build condensation DAG.
3. 3)Topologically sort components.
4. 4)Do DP / propagation along the DAG.

Examples:

- •**Dependency analysis**: groups of mutually dependent modules are SCCs; the SCC DAG gives a safe build/order structure.
- •**Program optimization**: mutually recursive functions form SCCs in the call graph.

---

## 3) Deadlock and wait-for graphs

In operating systems and databases, a **wait-for graph** is directed: process A → process B if A is waiting for a resource held by B.

- •A deadlock corresponds to a directed cycle.
- •SCCs identify groups involved in mutual waiting dependencies.

---

## 4) 2-SAT (classic reduction)

In 2-SAT, you build an implication graph. SCCs provide the satisfiability test:

- •A formula is unsatisfiable iff some variable x and its negation ¬x are in the same SCC.

(You don’t need the full 2-SAT method here, just note SCCs are the core subroutine.)

---

## 5) Practical workflow for using SCCs

When you solve problems with SCCs, you usually want more than just the sets. You often want:

- •comp[u] = component id of u
- •components list: vertices per SCC
- •condensation edges between components
- •topological order of components

A typical post-processing step:

- •For every original edge u → v:
- •if comp[u] ≠ comp[v], add edge comp[u] → comp[v] to condensation DAG.

Then you can run standard DAG algorithms.

---

### How SCCs connect back to reachability (u →\* v)

SCCs are not “extra structure” beyond reachability—they are the equivalence classes of mutual reachability.

You can think of them as compressing reachability into two layers:

1. 1)**Inside** an SCC: everything reaches everything.
2. 2)**Between** SCCs: reachability is one-way and acyclic.

That mental model is the bridge between definition and algorithm: DFS is a reachability engine, and SCC algorithms are careful ways of running DFS so that these equivalence classes fall out.

## Worked Examples (3)

### Identify SCCs by reasoning about mutual reachability

Consider the directed graph with vertices {1,2,3,4,5,6} and edges:

1 → 2

2 → 3

3 → 1

3 → 4

4 → 5

5 → 4

5 → 6

Find all SCCs and the condensation DAG.

1. Step 1: Find obvious cycles (strong connectivity candidates).

   The edges 1 → 2 → 3 → 1 form a directed cycle.

   So 1 → *2, 2 →* 3, 3 →\* 1, and by chaining, each of {1,2,3} reaches each other.

   Candidate SCC: {1,2,3}.
2. Step 2: Check maximality for {1,2,3}.

   Vertex 4 is reachable from 3 (since 3 → 4), so {1,2,3} can reach 4.

   But can 4 reach back to 1 (or 2 or 3)?

   From 4 we can go 4 → 5 → 6 (and also 4 ↔ 5), but there is no edge leading back to 1,2,3.

   So 4 ↛\* 1.

   Therefore 4 is not strongly connected with 1.

   So SCC {1,2,3} is maximal as is.
3. Step 3: Identify SCC containing 4 and 5.

   We have 4 → 5 and 5 → 4, so 4 → *5 and 5 →* 4.

   Thus 4 ~ 5.

   Check if 6 joins them:

   5 → 6, so 5 →\* 6.

   But 6 has no outgoing edges listed, so 6 ↛\* 5.

   Thus 6 is not strongly connected with 4/5.

   So SCC {4,5} stands.
4. Step 4: Determine SCC for 6.

   6 reaches itself (6 →\* 6) by the length-0 path.

   No other vertex is mutually reachable with 6.

   So SCC {6}.
5. Step 5: Build condensation DAG.

   Contract SCC A = {1,2,3}, SCC B = {4,5}, SCC C = {6}.

   Original edges crossing SCCs:

   - •3 → 4 gives A → B.
   - •5 → 6 gives B → C.

   No edges go backward.

   So the condensation graph is A → B → C, which is a DAG (a simple chain).

**Insight:** SCCs capture “islands of cycles.” Once you compress each island into a node, the remaining structure becomes acyclic and much easier to analyze.

### Run Kosaraju’s algorithm on a small graph

Let G have vertices {A,B,C,D,E,F} and edges:

A → B

B → C

C → A

B → D

D → E

E → D

E → F

Use Kosaraju’s algorithm to find SCCs (show the two passes conceptually).

1. Step 1: DFS on G and record finish times.

   One valid DFS order: start at A.

   Explore A → B → C.

   From C we can go to A (already discovered), so C finishes first.

   Then back to B: explore B → D → E.

   From E explore E → F (F finishes), then E finishes, then D finishes, then B finishes, then A finishes.

   Finish order (first finished to last finished) could be:

   C, F, E, D, B, A.

   So decreasing finish time order is:

   A, B, D, E, F, C.
2. Step 2: Build transpose graph Gᵀ by reversing edges.

   Edges in Gᵀ:

   B → A

   C → B

   A → C

   D → B

   E → D

   D → E

   F → E
3. Step 3: DFS on Gᵀ in decreasing finish time order.

   Process A first (unvisited):

   From A we go to C, from C to B, from B to A.

   So we reach {A,B,C} in this DFS.

   That is SCC₁ = {A,B,C}.
4. Step 4: Continue the order.

   Next B is already visited.

   Next D is unvisited: DFS from D in Gᵀ reaches E (via D → E) and back to D (via E → D).

   It can also reach B via D → B, but B is already assigned to SCC₁ and is visited, so it won’t be included in this new DFS tree.

   So SCC₂ = {D,E}.
5. Step 5: Next E is visited.

   Next F is unvisited: DFS from F reaches only F (since F → E but E is already visited).

   So SCC₃ = {F}.
6. Step 6: C is visited.

   We are done.

   SCCs found: {A,B,C}, {D,E}, {F}.

**Insight:** The first pass computes an order that respects the SCC DAG. The second pass on the reversed graph ensures each DFS “fills up” exactly one SCC without spilling into others.

### Prove (with steps) that SCC contraction produces a DAG

Let G be any directed graph. Let its SCCs be contracted to form the condensation graph G\_SCC. Prove G\_SCC is acyclic.

1. Step 1: Assume for contradiction that G\_SCC contains a directed cycle:

   C₁ → C₂ → … → Cₖ → C₁,

   where each Cᵢ is a distinct SCC.
2. Step 2: Pick vertices u ∈ C₁ and v ∈ C₂.

   Because there is an edge C₁ → C₂ in G\_SCC, there exists an edge (or path) in G from some vertex in C₁ to some vertex in C₂.

   In particular, u →\* v (reachability across components along the condensation edges).
3. Step 3: Because the SCC cycle returns to C₁, there is also a path from C₂ back to C₁ in G\_SCC.

   Therefore, in G there is a directed path from v to u:

   v →\* u.
4. Step 4: Combine the two reachability statements:

   u → *v and v →* u.

   So u and v are strongly connected, meaning u ~ v.
5. Step 5: If u ~ v, then u and v must be in the same SCC (equivalence class).

   But u ∈ C₁ and v ∈ C₂ with C₁ ≠ C₂, contradicting that SCCs are disjoint.
6. Step 6: Therefore, the assumption was false, and G\_SCC has no directed cycles.

   So the condensation graph is a DAG.

**Insight:** Any cycle between components would create mutual reachability across them, forcing them to merge into a single SCC. The only way SCCs stay separate is if the component graph is acyclic.

## Key Takeaways

- ✓

  Reachability u →\* v means there exists a directed path from u to v; it is reflexive and transitive but not symmetric.
- ✓

  Strong connectivity between u and v is mutual reachability: u → *v and v →* u.
- ✓

  An SCC is a maximal set of vertices that are pairwise strongly connected; SCCs are the equivalence classes of the relation u ~ v.
- ✓

  SCCs partition the vertices: every vertex belongs to exactly one SCC.
- ✓

  Contracting SCCs yields the condensation graph, which is always a DAG.
- ✓

  Kosaraju finds SCCs with two DFS passes (on G and Gᵀ) in O(V + E).
- ✓

  Tarjan finds SCCs in one DFS pass using a stack and low-link values, also in O(V + E).
- ✓

  Many directed-graph problems become simpler by solving them on the SCC DAG rather than on the original graph.

## Common Mistakes

- ✗

  Confusing a directed cycle with an SCC: an SCC can contain many cycles and paths; the definition is mutual reachability among all vertices, not just being on one cycle.
- ✗

  Forgetting maximality: a set may have mutual reachability but still not be an SCC if it can be expanded by adding more mutually reachable vertices.
- ✗

  Assuming SCC edges can form cycles in the condensation graph: they cannot; if they did, those SCCs would actually be one SCC.
- ✗

  Implementing Kosaraju but processing vertices in the wrong order on the second pass (it must be decreasing finish time from the first pass).

## Practice

easy

Given vertices {1,2,3,4} and edges 1 → 2, 2 → 3, 3 → 2, 3 → 4. List the SCCs and draw the condensation DAG.

**Hint:** Look for mutual reachability pairs. If 2 → *3 and 3 →* 2, they must be in the same SCC. Check whether 1 can be reached back from that SCC, and whether 4 can reach back.

Show solution

SCCs: {1}, {2,3}, {4}.

Reason: 2 ↔ 3 via edges 2 → 3 and 3 → 2, so they are strongly connected. 1 reaches 2 but 2 cannot reach 1, so 1 is alone. 3 reaches 4 but 4 cannot reach back, so 4 is alone.

Condensation DAG: {1} → {2,3} → {4}.

medium

Prove that if u and v are in the same SCC and v and w are in the same SCC, then u and w are in the same SCC.

**Hint:** Translate “same SCC” into mutual reachability (→*). Use transitivity of reachability to show u →* w and w →\* u.

Show solution

If u and v are in the same SCC, then u → *v and v →* u.

If v and w are in the same SCC, then v → *w and w →* v.

By transitivity: u → *v and v →* w ⇒ u →\* w.

Also w → *v and v →* u ⇒ w →\* u.

So u and w are mutually reachable and thus in the same SCC.

hard

You are given SCC labels comp[u] for every vertex u in a directed graph G. Describe how to build the condensation graph in O(V + E), and explain why the result is a DAG.

**Hint:** Scan each edge u → v. If comp[u] ≠ comp[v], add an edge comp[u] → comp[v]. To argue it’s a DAG, use the fact that a cycle among components would imply mutual reachability across components.

Show solution

Algorithm (O(V + E)):

- •Let K be the number of components.
- •Create K nodes for the condensation graph.
- •For each directed edge (u → v) in E:
- •if comp[u] ≠ comp[v], add an edge (comp[u] → comp[v]) to the component graph (optionally deduplicate with a set per component).

This is O(V + E) because each edge is processed once.

Why it’s a DAG:

- •Suppose the component graph had a directed cycle C₁ → … → C₁.
- •Then for any vertices a ∈ C₁ and b ∈ C₂, we would have a → *b along the component edges, and b →* a by continuing around the cycle.
- •That would make a and b strongly connected, implying C₁ and C₂ should be the same SCC, contradiction.

So no cycles exist; it is a DAG.

## Connections

Prerequisite refreshers: [Depth-First Search (DFS)](/tech-tree/dfs/), [Breadth-First Search (BFS)](/tech-tree/bfs/), [Reachability in Directed Graphs](/tech-tree/directed-reachability/)

Next-step nodes that commonly use SCCs: [Topological Sorting](/tech-tree/toposort/), [Directed Acyclic Graphs (DAGs)](/tech-tree/dag/), [2-SAT via Implication Graph](/tech-tree/2-sat/), [Deadlock Detection](/tech-tree/deadlock/), [Graph Condensation](/tech-tree/condensation-graph/)

Quality: A (4.4/5)

[← back to tree](/tech-tree/)[browse all →](/tech-tree/inventory/)
