---
title: Minimum Spanning Trees
description: Kruskal, Prim algorithms. Connecting all nodes with minimum edge weight.
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
permalink: /tech-tree/minimum-spanning-trees/
---

[←Back to Tech Tree](/tech-tree/)

[inventory](/tech-tree/inventory/)[coverage](/tech-tree/coverage/)

# Minimum Spanning Trees

Graph TheoryDifficulty: ★★★☆☆Depth: 4Unlocks: 0

Kruskal, Prim algorithms. Connecting all nodes with minimum edge weight.

## Interactive Visualization

⏮◀◀▶▶STEP0.25x1xZOOM

t=0s

## Core Concepts

- -Minimum spanning tree: a spanning tree whose total sum of edge weights is minimum among all spanning trees
- -Cut property (safe edge): the lightest edge crossing any vertex partition (cut) can be included in some MST
- -Cycle property: the heaviest edge on any cycle cannot belong to any MST

## Key Symbols & Notation

w(e) = weight of edge e

## Essential Relationships

- -Cut property justifies greedy selection: choosing safe (lightest-across-cut) edges greedily (Kruskal/Prim) yields an MST

## Prerequisites (2)

[Graph Traversal5 atoms](/tech-tree/graph-traversal/)[Trees5 atoms](/tech-tree/trees/)

Advanced Learning Details

### Graph Position

43

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

55

Total Elements

L4

Percentile Level

L3

Atomic Level

### All Concepts (25)

- - weighted graph: edges carry numerical weights (costs, lengths, etc.)
- - spanning tree: a tree that includes all vertices of a connected graph (subset of edges that connects all vertices with no cycles)
- - minimum spanning tree (MST): a spanning tree whose total edge weight is minimal among all spanning trees
- - total weight of a tree: sum of the weights of all edges in that tree
- - minimum spanning forest: for a disconnected graph, a MST for each connected component (collection of spanning trees)
- - cut of a graph: a partition of vertices into two disjoint sets S and V\S
- - edge crossing a cut: an edge with one endpoint in S and the other in V\S
- - light edge for a cut: an edge of minimum weight among those crossing a cut
- - safe edge: an edge that can be added to a growing forest/tree without preventing construction of an MST (typically a light edge across some cut)
- - cycle property (MST): in any cycle, the maximum-weight edge is not in any MST (or equivalently removing the heaviest edge can improve/maintain optimality)
- - cut property (MST): for any cut, some light edge crossing the cut belongs to some MST (used to justify greedy choices)
- - greedy strategy for MSTs: repeatedly add locally optimal (safe/light) edges to build the final MST
- - Kruskal's algorithm: sort all edges by weight and add edges from smallest to largest, skipping those that would form a cycle, producing a forest that becomes an MST
- - Prim's algorithm: grow a single tree starting from an arbitrary vertex, repeatedly adding the minimum-weight edge connecting the tree to an outside vertex
- - forest-building viewpoint (Kruskal): Kruskal constructs a forest that eventually connects into a spanning tree for each component
- - tree-growing viewpoint (Prim): Prim maintains a single connected tree that gradually spans the component
- - disjoint-set (union-find) data structure: a structure to maintain components/sets with operations to find set representative and union two sets
- - cycle-avoidance via union-find: identify whether adding an edge connects two different components (safe) or would create a cycle (unsafe)
- - priority queue keyed by edge weight (or vertex key) in Prim: structure to efficiently select the next minimum connecting edge
- - decrease-key operation: updating a key value in a priority queue when a better (smaller-weight) connecting edge is found
- - tie situations and multiple MSTs: equal-weight edges can lead to more than one valid MST; uniqueness holds when all edge weights are distinct
- - safe-edge selection differs operationally between Kruskal and Prim (global sorted choice vs. local frontier minimum)
- - minimum spanning tree correctness arguments rely on cut and cycle properties
- - handling disconnected graphs: algorithm produces a minimum spanning forest rather than a single tree
- - practical implementation details that affect performance: sorting edges for Kruskal, and choice of heap/priority-queue implementation for Prim

### Teaching Strategy

Self-serve tutorial - low prerequisites, straightforward concepts.

You’re wiring up a campus network. Every building must be connected, cable is expensive, and you’re allowed to choose which paths to dig. How do you guarantee you connect everything with the least total cable length—without trying every possible network layout?

TL;DR:

A **minimum spanning tree (MST)** is a set of edges that connects all vertices with **no cycles** and **minimum total weight**. Two core greedy facts make MSTs tractable: the **cut property** (the lightest edge across a cut is safe) and the **cycle property** (the heaviest edge on a cycle is never needed). **Kruskal** grows a forest by adding the next-lightest safe edge (using DSU/Union-Find). **Prim** grows one tree by repeatedly adding the lightest edge leaving the current tree (using a priority queue).

## What Is a Minimum Spanning Tree?

## The problem we’re solving

You’re given a connected, undirected, weighted graph G=(V,E)G = (V, E)G=(V,E), where each edge e∈Ee \in Ee∈E has a weight w(e)w(e)w(e) (cost, length, time, etc.). You want to pick some edges so that:

1. 1)**Every vertex is connected** (the chosen edges span all vertices).
2. 2)There are **no cycles** (so you’re not paying for redundant loops).
3. 3)The **total weight is as small as possible**.

A spanning tree is exactly a connected, acyclic subgraph that includes all vertices. So an MST is the best (minimum-weight) spanning tree.

## What “tree” implies (and why it matters)

A spanning tree on ∣V∣=n|V| = n∣V∣=n vertices always has exactly n−1n-1n−1 edges. This is a powerful constraint:

- •If you have fewer than n−1n-1n−1 edges, you can’t be connected.
- •If you have nnn or more edges and you’re connected, you must have a cycle.

So an MST is “choose n−1n-1n−1 edges carefully.”

## A small example to ground the idea

Suppose you have 4 vertices and weighted edges:

- •A—B:1A\text{—}B:1A—B:1, B—C:2B\text{—}C:2B—C:2, A—C:3A\text{—}C:3A—C:3, C—D:1C\text{—}D:1C—D:1, B—D:4B\text{—}D:4B—D:4

One spanning tree is (A,B),(B,C),(C,D)(A,B),(B,C),(C,D)(A,B),(B,C),(C,D) with weight $1+2+1=4$.

Another spanning tree is (A,C),(C,D),(A,B)(A,C),(C,D),(A,B)(A,C),(C,D),(A,B) with weight $3+1+1=5$.

The MST would choose the first: total 4.

## What MST is *not*

- •It’s **not** a shortest path tree (that’s rooted at one source and minimizes distances from the root).
- •It’s **not** about minimizing the maximum edge on every path (that’s related, but different objectives exist).

## Existence and uniqueness

- •If the graph is connected, an MST always exists.
- •If all edge weights are distinct, the MST is unique.
- •If there are ties, there can be multiple MSTs with the same total weight.

## Why greedy algorithms work here

Most graph optimization problems don’t allow “just keep taking the cheapest available step.” MST is special: it has **local rules (cut/cycle properties)** that certify a greedy choice won’t block optimality.

That’s the real theme of MST: we need a *proof tool* that justifies greedy growth.

## Core Mechanic 1: The Cut Property (Safe Edges)

## Motivation: how can we “certify” an edge is a good idea?

If we’re building a spanning tree and we add an edge too early, we might later regret it. So we want a condition that says:

> “No matter what the optimal MST looks like, **there exists** an MST that contains this edge.”

Such an edge is called **safe**.

## Cuts: a clean way to reason about connectivity

A **cut** is a partition of vertices into two non-empty sets:

- •S⊂VS \subset VS⊂V
- •V∖SV \setminus SV∖S

An edge **crosses** the cut if it has one endpoint in SSS and the other in V∖SV \setminus SV∖S.

Intuition: if your current partial structure has connected everything in SSS and you want to connect to the outside, you must pick *some* edge that crosses the cut.

## The Cut Property (statement)

Let (S,V∖S)(S, V\setminus S)(S,V∖S) be any cut. Consider all edges that cross the cut. Let e∗e^\*e∗ be a lightest edge among them (minimum weight). Then:

> **Cut property:** The edge e∗e^\*e∗ is safe: there exists an MST that contains e∗e^\*e∗.

If the lightest crossing edge is unique, then it belongs to **every** MST.

## Seeing the cut property (diagram)

Below, SSS is the left group and V∖SV\setminus SV∖S is the right group. The cut-crossing edges are those that go between the groups.

```
<svg width="640" height="220" viewBox="0 0 640 220" xmlns="http://www.w3.org/2000/svg">
  <style>
    .v { fill:#fff; stroke:#111; stroke-width:2; }
    .lbl { font: 14px sans-serif; fill:#111; }
    .cut { stroke:#888; stroke-width:2; stroke-dasharray:6 6; }
    .e { stroke:#999; stroke-width:2; }
    .elight { stroke:#0b6; stroke-width:5; }
    .w { font: 13px sans-serif; fill:#333; }
    .region { fill:#f4f8ff; stroke:#c7d6ff; stroke-width:2; }
  </style>

  <!-- regions -->
  <rect x="20" y="20" width="270" height="180" rx="14" class="region"/>
  <rect x="350" y="20" width="270" height="180" rx="14" class="region"/>
  <text x="35" y="45" class="lbl">S</text>
  <text x="365" y="45" class="lbl">V \ S</text>

  <!-- cut line -->
  <line x1="320" y1="10" x2="320" y2="210" class="cut"/>

  <!-- vertices left -->
  <circle cx="90" cy="80" r="16" class="v"/><text x="85" y="85" class="lbl">A</text>
  <circle cx="200" cy="140" r="16" class="v"/><text x="195" y="145" class="lbl">B</text>

  <!-- vertices right -->
  <circle cx="430" cy="80" r="16" class="v"/><text x="425" y="85" class="lbl">C</text>
  <circle cx="540" cy="140" r="16" class="v"/><text x="535" y="145" class="lbl">D</text>

  <!-- crossing edges -->
  <line x1="90" y1="80" x2="430" y2="80" class="e"/>
  <text x="255" y="70" class="w">w=5</text>

  <line x1="200" y1="140" x2="540" y2="140" class="e"/>
  <text x="360" y="132" class="w">w=4</text>

  <line x1="200" y1="140" x2="430" y2="80" class="elight"/>
  <text x="305" y="110" class="w" fill="#0b6">w=2 (lightest)</text>

</svg>
```

The cut property says: the green edge of weight 2 (the lightest crossing edge) can be included in some MST safely.

## Why the cut property is true (proof sketch with breathing room)

We’ll use an “exchange argument.”

1. 1)Consider any MST TTT.
2. 2)If TTT already contains e∗e^\*e∗, we’re done.
3. 3)If not, add e∗e^\*e∗ to TTT. This creates exactly one cycle (trees + 1 edge → one cycle).
4. 4)That cycle must cross the cut at least twice (to go from SSS to V∖SV\setminus SV∖S and back), so there exists some other edge fff on the cycle that also crosses the cut.
5. 5)Since e∗e^\*e∗ is the lightest edge crossing the cut, w(e∗)≤w(f)w(e^\*) \le w(f)w(e∗)≤w(f).
6. 6)Remove fff from the cycle. The result is still connected (cycle removal keeps connectivity) and has n−1n-1n−1 edges, so it’s a spanning tree.
7. 7)The new tree has weight no greater than TTT, so it’s also an MST and contains e∗e^\*e∗.

The key move is: **swap in a light edge and swap out a heavier-or-equal one** without breaking spanning-tree structure.

## How algorithms use the cut property

- •Kruskal’s algorithm implicitly considers cuts induced by components in a forest.
- •Prim’s algorithm explicitly considers the cut (S,V∖S)(S, V\setminus S)(S,V∖S) where SSS is the set of vertices already in the growing tree.

In both cases, they repeatedly choose a lightest edge crossing a relevant cut.

## Core Mechanic 2: The Cycle Property (What Can Never Be in an MST)

## Motivation: preventing cycles early vs proving an edge is useless

The cut property tells us which edges are safe to add.

The **cycle property** tells us which edges are safe to *discard*.

This becomes especially helpful for understanding Kruskal (where we sort edges and try them in order) and for reasoning about correctness.

## The Cycle Property (statement)

Consider any cycle CCC in the graph. Let emaxe\_{max}emax​ be an edge on that cycle with maximum weight (a heaviest edge).

> **Cycle property:** There exists an MST that does **not** contain emaxe\_{max}emax​. In particular, if emaxe\_{max}emax​ is uniquely the heaviest on the cycle, it is in **no** MST.

Intuition: within a cycle, you already have a redundant route. If one edge is the most expensive, it’s the best candidate to remove.

## Seeing the cycle property (diagram)

Here’s a 4-cycle. The heaviest edge (weight 9) is highlighted in red; the cycle property says it cannot appear in an MST if it’s uniquely heaviest.

```
<svg width="640" height="240" viewBox="0 0 640 240" xmlns="http://www.w3.org/2000/svg">
  <style>
    .v { fill:#fff; stroke:#111; stroke-width:2; }
    .lbl { font: 14px sans-serif; fill:#111; }
    .e { stroke:#777; stroke-width:3; }
    .heavy { stroke:#c00; stroke-width:6; }
    .w { font: 13px sans-serif; fill:#333; }
  </style>

  <!-- vertices -->
  <circle cx="180" cy="70" r="16" class="v"/><text x="175" y="75" class="lbl">A</text>
  <circle cx="460" cy="70" r="16" class="v"/><text x="455" y="75" class="lbl">B</text>
  <circle cx="460" cy="170" r="16" class="v"/><text x="455" y="175" class="lbl">C</text>
  <circle cx="180" cy="170" r="16" class="v"/><text x="175" y="175" class="lbl">D</text>

  <!-- edges -->
  <line x1="180" y1="70" x2="460" y2="70" class="e"/>
  <text x="310" y="58" class="w">w=3</text>

  <line x1="460" y1="70" x2="460" y2="170" class="e"/>
  <text x="472" y="125" class="w">w=4</text>

  <line x1="460" y1="170" x2="180" y2="170" class="e"/>
  <text x="310" y="190" class="w">w=2</text>

  <line x1="180" y1="170" x2="180" y2="70" class="heavy"/>
  <text x="110" y="125" class="w" fill="#c00">w=9 (heaviest)</text>

</svg>
```

## Why the cycle property is true (exchange argument)

Let TTT be an MST. Suppose (for contradiction, or to build an alternative MST) that TTT contains emaxe\_{max}emax​.

- •Remove emaxe\_{max}emax​ from TTT. The tree splits into two components, say SSS and V∖SV\setminus SV∖S.
- •In the original cycle CCC, there is another path connecting those components (because the rest of the cycle still connects the endpoints).
- •Therefore, there exists some other edge fff on the cycle that crosses the cut (S,V∖S)(S, V\setminus S)(S,V∖S).
- •Since emaxe\_{max}emax​ is a heaviest edge on the cycle, w(f)≤w(emax)w(f) \le w(e\_{max})w(f)≤w(emax​).
- •Add fff to reconnect the components, forming a spanning tree with weight no larger.

So we can always replace the heavy cycle edge with a no-heavier alternative.

## How this connects to Kruskal

Kruskal adds edges in increasing weight order, **skipping any edge that would make a cycle**.

When an edge would complete a cycle, it’s necessarily not needed; and if it’s among the heavier edges on that cycle, skipping it is consistent with the cycle property.

## Cut vs cycle: when to use which

- •Use **cut property** to justify adding an edge.
- •Use **cycle property** to justify excluding an edge.

Both are two sides of the same “exchange” idea: MSTs are flexible enough that local replacements preserve optimality.

## Algorithms: Kruskal and Prim (and How They Relate)

## Before algorithms: what greedy growth looks like

An MST has n−1n-1n−1 edges. A natural greedy plan is:

- •Start with no edges.
- •Repeatedly add a cheap edge that doesn’t break the “tree-ness.”

But there are two distinct ways to organize this growth:

1. 1)**Kruskal:** grow many small trees (a forest) and merge them.
2. 2)**Prim:** grow one tree outward from a starting vertex.

Both are correct because each step corresponds to choosing a lightest edge across some cut.

---

## Kruskal’s algorithm

### Idea

Sort all edges by weight. Scan from lightest to heaviest; add an edge if it connects two different components (i.e., doesn’t form a cycle).

### Data structure: Disjoint Set Union (Union-Find)

We need to quickly answer:

- •Are uuu and vvv already connected by chosen edges? (Find)
- •If not, merge their components. (Union)

With path compression + union by rank/size, each operation is effectively constant amortized time.

### Pseudocode

1. 1)Sort edges EEE by increasing w(e)w(e)w(e)
2. 2)Initialize DSU with each vertex alone
3. 3)For each edge (u,v)(u,v)(u,v) in sorted order:

- •If Find(u) ≠ Find(v):
- •Add edge to MST
- •Union(u, v)

4. 4)Stop when MST has ∣V∣−1|V|-1∣V∣−1 edges

### Correctness intuition

At any moment, Kruskal’s chosen edges form a forest. The components define a cut: pick any component as SSS, and consider edges leaving it. The next chosen edge is the lightest edge that connects two components (a lightest edge across some cut), so by the cut property it’s safe.

### Complexity

- •Sorting edges: O(∣E∣log⁡∣E∣)O(|E|\log|E|)O(∣E∣log∣E∣)
- •DSU operations: O(∣E∣ α(∣V∣))O(|E|\,\alpha(|V|))O(∣E∣α(∣V∣)) (inverse Ackermann, tiny)

So overall: O(∣E∣log⁡∣E∣)O(|E|\log|E|)O(∣E∣log∣E∣).

### When Kruskal is a good fit

- •Sparse graphs (few edges): sorting is manageable.
- •When you already have edges in sorted order (or nearly so).
- •When you want the MST but don’t care about a starting vertex.

---

## Prim’s algorithm

### Idea

Start from any vertex. Maintain a set SSS of vertices already in the tree. Repeatedly add the lightest edge that goes from SSS to V∖SV\setminus SV∖S.

This is “like Dijkstra,” but the key is: Prim uses edge weights directly to cross the boundary, not accumulated path distances.

### Data structure: Priority queue over boundary edges (or keys)

Typical implementation tracks for each vertex v∉Sv \notin Sv∈/S the cheapest edge connecting it to SSS (a key), and updates keys as SSS grows.

### Pseudocode (key-based)

1. 1)Pick a start vertex sss
2. 2)Set key[s] = 0; key[others] = +∞
3. 3)Use a min-priority queue keyed by key[v]
4. 4)While queue not empty:

- •Extract vertex uuu with minimum key
- •Add uuu to SSS
- •For each edge (u,v)(u, v)(u,v) with v∉Sv \notin Sv∈/S:
- •If w(u,v)<key[v]w(u,v) < key[v]w(u,v)<key[v]:
- •key[v] = w(u,v)
- •parent[v] = u
- •Decrease-key in the priority queue

5. 5)The edges (parent[v], v) form the MST

### Correctness intuition

At each step, the algorithm considers the cut (S,V∖S)(S, V\setminus S)(S,V∖S) and picks the lightest edge leaving SSS (via the minimum key). By the cut property, that edge is safe.

### Complexity

- •With binary heap: O(∣E∣log⁡∣V∣)O(|E|\log|V|)O(∣E∣log∣V∣)
- •With Fibonacci heap: O(∣E∣+∣V∣log⁡∣V∣)O(|E| + |V|\log|V|)O(∣E∣+∣V∣log∣V∣) (mostly theoretical)

### When Prim is a good fit

- •Dense graphs (many edges): ∣E∣log⁡∣V∣|E|\log|V|∣E∣log∣V∣ can beat sorting all edges.
- •When you want a single connected growth from a start (e.g., incremental visualization, interactive building).

---

## Kruskal vs Prim (comparison)

| Feature | Kruskal | Prim |
| --- | --- | --- |
| Growth style | forest → merges components | one tree expands |
| Key greedy choice | next lightest edge that doesn’t cycle | lightest edge crossing (S,V∖S)(S, V\setminus S)(S,V∖S) |
| Main structure | DSU (Union-Find) | min-priority queue |
| Typical time | $O( | E | \log | E | )$ | $O( | E | \log | V | )$ |
| Works on disconnected graph? | gives minimum spanning **forest** | needs a start per component |

---

## A note on disconnected graphs: minimum spanning forest

If GGG is not connected, an MST doesn’t exist (can’t span all vertices). But both ideas extend:

- •Kruskal naturally returns a **minimum spanning forest** (one MST per component).
- •Prim can do the same by running it from each unvisited vertex.

---

## Important nuance: undirected graphs

Classical MST is defined for **undirected** graphs. If edges are directed, the analogous structure is a **minimum spanning arborescence** (Edmonds’ algorithm), which is a different topic.

## Application/Connection: Where MST Shows Up (and What It Connects To)

## Why MSTs matter beyond “connect things cheaply”

MSTs are a core pattern: **global optimization made greedy** through structural properties (cuts/cycles). Once you internalize that, you’ll recognize similar proof techniques elsewhere.

## Common applications

### 1) Network design and infrastructure

- •Laying fiber between data centers
- •Electrical grid planning (simplified)
- •Road/path planning in terrains (approximate)

MST gives a baseline “no redundancy” network. Real systems add redundancy later, but MST is often the starting scaffold.

### 2) Clustering (single-linkage)

Given points and pairwise distances, compute the MST of the complete graph. If you delete the k−1k-1k−1 largest edges in the MST, you get kkk connected components—this is exactly **single-linkage hierarchical clustering**.

### 3) Approximation and subroutines

MSTs appear inside larger algorithms:

- •As part of approximation schemes (e.g., metric TSP has MST-based lower bounds).
- •In image segmentation / region merging (graph-based methods often rely on MST-like structures).

## Interpreting MST edges as “bottleneck” structure

Even when you don’t care about total weight, MST has a useful minimax flavor:

- •Any MST is a **minimum bottleneck spanning tree**: it minimizes the maximum edge weight in the tree.

This isn’t the same objective as MST, but MST ends up optimal for it too.

## How cut/cycle properties train your proof skills

These properties are classic examples of:

- •**Exchange arguments** (swap edges without hurting feasibility)
- •**Greedy-choice property** (a local step can be part of an optimum)

If you later study matroids, MST becomes a flagship example: the set of acyclic edge sets forms a matroid (graphic matroid), and greedy works.

## Practical implementation tips (what you’d do in code)

- •Use Kruskal when you already have edges listed and can sort them.
- •Use Prim when you have adjacency lists and want to expand from a start, especially if graph is dense.
- •Be explicit about:
- •whether vertices are 0..n-1
- •whether edges are undirected (store both adjacency directions)
- •handling equal weights (ties don’t break correctness)

## A quick mental checklist

When you see an MST problem, ask:

1. 1)Is the graph undirected and connected?
2. 2)Do I need the MST itself or just the weight?
3. 3)Is the graph sparse or dense?
4. 4)Which proof tool is relevant right now: a cut or a cycle?

That last question is the “transferable skill”: reasoning locally about global optimality.

## Worked Examples (3)

### Kruskal’s algorithm step-by-step (with DSU thinking)

Graph with vertices V = {A, B, C, D, E}. Weighted edges:

(A,B)=1, (C,D)=1, (B,C)=2, (A,C)=3, (B,D)=4, (C,E)=5, (D,E)=6.

Find an MST using Kruskal.

1. Sort edges by weight:

   1: (A,B), (C,D)

   2: (B,C)

   3: (A,C)

   4: (B,D)

   5: (C,E)

   6: (D,E)
2. Initialize DSU components:

   {A}, {B}, {C}, {D}, {E}

   MST = ∅
3. Consider (A,B) with w=1:

   Find(A) ≠ Find(B) ⇒ add it.

   Union(A,B)

   Components: {A,B}, {C}, {D}, {E}

   MST edges: {(A,B)}
4. Consider (C,D) with w=1:

   Find(C) ≠ Find(D) ⇒ add it.

   Union(C,D)

   Components: {A,B}, {C,D}, {E}

   MST edges: {(A,B), (C,D)}
5. Consider (B,C) with w=2:

   Find(B) is component {A,B}; Find(C) is component {C,D} ⇒ different ⇒ add it.

   Union({A,B}, {C,D})

   Components: {A,B,C,D}, {E}

   MST edges: {(A,B), (C,D), (B,C)}
6. Consider (A,C) with w=3:

   Now Find(A) = Find(C) (both in {A,B,C,D}) ⇒ adding would create a cycle ⇒ skip.

   MST unchanged.
7. Consider (B,D) with w=4:

   Find(B) = Find(D) (same component) ⇒ would create a cycle ⇒ skip.
8. Consider (C,E) with w=5:

   Find(C) ≠ Find(E) ⇒ add it.

   Union({A,B,C,D}, {E})

   Components: {A,B,C,D,E}

   MST edges: {(A,B), (C,D), (B,C), (C,E)}
9. Stop condition:

   We have |V|-1 = 4 edges ⇒ done.

   Total MST weight = 1 + 1 + 2 + 5 = 9.

**Insight:** Kruskal’s logic is: “take the cheapest edge that connects two different components.” The DSU is what makes “different components?” fast. Every accepted edge is safe via the cut property on the cut induced by components.

### Prim’s algorithm step-by-step (keys and the cut (S, V\S))

Use the same graph as above:

(A,B)=1, (C,D)=1, (B,C)=2, (A,C)=3, (B,D)=4, (C,E)=5, (D,E)=6.

Run Prim starting at A and produce the MST edges.

1. Initialize:

   S = ∅

   key[A]=0; key[B]=key[C]=key[D]=key[E]=+∞

   parent[·]=nil
2. Extract min key: A (key 0). Add A to S.

   Relax neighbors of A:

   - •Edge (A,B)=1 ⇒ key[B]=1, parent[B]=A
   - •Edge (A,C)=3 ⇒ key[C]=3, parent[C]=A
3. Extract min key among not-in-S: B (key 1). Add B to S.

   Relax neighbors of B:

   - •(B,C)=2 improves key[C] from 3 → 2 ⇒ parent[C]=B
   - •(B,D)=4 ⇒ key[D]=4, parent[D]=B
4. Extract min key: C (key 2). Add C to S.

   Relax neighbors of C:

   - •(C,D)=1 improves key[D] from 4 → 1 ⇒ parent[D]=C
   - •(C,E)=5 ⇒ key[E]=5, parent[E]=C
5. Extract min key: D (key 1). Add D to S.

   Relax neighbors of D:

   - •(D,E)=6 does not improve key[E]=5 ⇒ no change
6. Extract min key: E (key 5). Add E to S.

   Done (all vertices included).
7. MST edges come from parents (excluding the start A):

   (B, parent[B]=A) ⇒ (A,B)

   (C, parent[C]=B) ⇒ (B,C)

   (D, parent[D]=C) ⇒ (C,D)

   (E, parent[E]=C) ⇒ (C,E)

   Total weight = 1 + 2 + 1 + 5 = 9

**Insight:** Prim makes the cut explicit: at each step, S is the current tree’s vertex set. The chosen edge is the minimum-weight edge crossing (S, V\S), which is safe by the cut property—so the tree can grow greedily.

### Using the cycle property to exclude an edge immediately

Graph contains a cycle A—B—C—D—A with weights:

(A,B)=2, (B,C)=3, (C,D)=4, (D,A)=10.

There may be other edges elsewhere, but focus on this cycle. Can (D,A) with weight 10 be in any MST?

1. Identify the cycle C = (A,B),(B,C),(C,D),(D,A).
2. Find the heaviest edge on the cycle:

   w(D,A)=10 is larger than 2,3,4 ⇒ it is uniquely heaviest.
3. Apply cycle property:

   The uniquely heaviest edge on a cycle cannot belong to any MST.
4. Conclusion:

   Edge (D,A) will never be chosen by Kruskal (it would be considered last), and even if a naive algorithm picked it early, you could always replace it with a lighter edge from the same cycle without disconnecting the graph.

**Insight:** Cycle property is a powerful pruning rule: spotting a heavy edge on a cycle lets you discard it without computing the full MST.

## Key Takeaways

- ✓

  An MST is a spanning tree (connected, acyclic, includes all vertices) with minimum total edge weight ∑ w(e).
- ✓

  Any spanning tree on n vertices has exactly n−1 edges; cycles represent redundant cost.
- ✓

  Cut property: for any cut (S, V\S), a lightest edge crossing the cut is safe (can appear in some MST).
- ✓

  Cycle property: on any cycle, a heaviest edge can be excluded from some MST; if uniquely heaviest, it is in no MST.
- ✓

  Kruskal: sort edges and add if they connect different components; implement efficiently with DSU/Union-Find.
- ✓

  Prim: grow a single tree; repeatedly add the lightest edge leaving the current vertex set; implement with a min-priority queue.
- ✓

  Kruskal naturally handles disconnected graphs by producing a minimum spanning forest; Prim needs restarting per component.
- ✓

  Cut/cycle properties are classic exchange-argument tools that justify greedy algorithms.

## Common Mistakes

- ✗

  Confusing MST with shortest path trees (Prim is not Dijkstra; it doesn’t minimize distances from a root).
- ✗

  Forgetting MST assumes an undirected graph; directed variants require different algorithms (arborescences).
- ✗

  Implementing Kruskal without DSU (leading to slow cycle checks) or implementing Prim without decrease-key handling (leading to incorrect or inefficient behavior).
- ✗

  Stopping Kruskal too late or too early: an MST must end with exactly |V|−1 accepted edges (for a connected graph).

## Practice

easy

Easy: Prove that any connected graph’s spanning tree has exactly n−1 edges (where n = |V|).

**Hint:** Use induction on n, or use the fact that a tree is connected and acyclic: adding an edge creates exactly one cycle; removing an edge disconnects.

Show solution

One proof by induction:

Base n=1: tree has 0 edges.

Inductive step: assume any tree on n−1 vertices has (n−2) edges. Take a tree T on n vertices. T has at least one leaf v (degree 1). Remove v and its incident edge; the remaining graph is still a tree on n−1 vertices, so it has n−2 edges. Adding back v adds 1 edge, so T has (n−2)+1 = n−1 edges.

medium

Medium: Given vertices {1,2,3,4} and edges with weights: (1,2)=1, (2,3)=1, (3,4)=1, (4,1)=1, (1,3)=2. Find one MST and its total weight. (There are multiple.)

**Hint:** A spanning tree needs 3 edges. Avoid cycles; prefer weight 1 edges first.

Show solution

All four cycle edges have weight 1. Pick any three that connect all vertices without forming a cycle. For example: (1,2),(2,3),(3,4). This connects all vertices and has no cycle. Total weight = 1+1+1 = 3. Any choice of three of the four weight-1 cycle edges yields an MST of weight 3.

hard

Hard: Let S be the set of vertices already chosen by Prim’s algorithm at some step. Show that the next edge Prim adds is safe by directly invoking the cut property.

**Hint:** Define the cut (S, V\S). Argue that Prim selects the minimum-weight edge crossing that cut (via the minimum key).

Show solution

At a given step, Prim maintains S and for every vertex v ∉ S, key[v] is the minimum weight of any edge (u,v) with u ∈ S. Let u *be the extracted vertex with minimum key; let e* = (parent[u*], u*). Then e *crosses the cut (S, V\S) and has weight key[u*]. For any edge crossing the cut, it ends at some vertex v ∉ S, and its weight is ≥ key[v] by definition of key. Since u *minimizes key over all v ∉ S, w(e*) = key[u\*] is the minimum weight among all edges crossing the cut. By the cut property, a lightest cut-crossing edge is safe; therefore Prim’s next edge is safe.

## Connections

Prereqs you’re using:

- •[Graph Traversal: BFS and DFS](/tech-tree/graph-traversal/)
- •[Trees (Connected Acyclic Graphs)](/tech-tree/trees/)

Natural next nodes:

- •[Disjoint Set Union (Union-Find)](/tech-tree/disjoint-set-union/)
- •[Greedy Algorithms: Exchange Arguments](/tech-tree/greedy-exchange-arguments/)
- •[Shortest Paths (Dijkstra)](/tech-tree/dijkstra/) — to contrast with Prim
- •[Clustering via MST (Single-Linkage)](/tech-tree/single-linkage-clustering/)
- •[Matroids and the Graphic Matroid](/tech-tree/matroids-graphic/)

Quality: A (4.5/5)

[← back to tree](/tech-tree/)[browse all →](/tech-tree/inventory/)
