---
title: Shortest Paths
description: Dijkstra, Bellman-Ford algorithms. Minimum cost paths.
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
source_format: html
inspiration_url: https://templeton.host/tech-tree/shortest-paths/
inspiration_category: tech-tree
---

> Source-copy draft imported from [https://templeton.host/tech-tree/shortest-paths/](https://templeton.host/tech-tree/shortest-paths/). Names, domain references, and local media paths were adapted for Xavi Ablaza / getablaza.com.

[←Back to Tech Tree](/tech-tree/)

[inventory](/tech-tree/inventory/)[coverage](/tech-tree/coverage/)

# Shortest Paths

Graph TheoryDifficulty: ★★★☆☆Depth: 5Unlocks: 1

Dijkstra, Bellman-Ford algorithms. Minimum cost paths.

## Interactive Visualization

⏮◀◀▶▶STEP0.25x1xZOOM

t=0s

## Core Concepts

- -Shortest-path distance: for a source s and vertex v, the shortest-path value is the minimum sum of edge weights over all s->v paths.
- -Edge relaxation: a local operation that tests and improves a vertex's distance estimate by considering a single incoming edge.
- -Weight-sign applicability: nonnegative edge weights allow a greedy extract-min finalization (Dijkstra); negative edges without negative cycles require iterative full-edge relaxations until convergence (Bellman-Ford).

## Key Symbols & Notation

d[v] (current shortest-path estimate for vertex v)w(u,v) (weight/cost of edge from u to v)

## Essential Relationships

- -Relaxation rule (operational): if d[v] > d[u] + w(u,v) then set d[v] = d[u] + w(u,v) (and update predecessor).

## Prerequisites (2)

[Graph Traversal5 atoms](/tech-tree/graph-traversal/)[Heaps5 atoms](/tech-tree/heaps/)

## Unlocks (1)

[Network Flowlvl 4](/tech-tree/network-flow/)

Advanced Learning Details

### Graph Position

54

Depth Cost

1

Fan-Out (ROI)

1

Bottleneck Score

5

Chain Length

### Cognitive Load

6

Atomic Elements

42

Total Elements

L3

Percentile Level

L4

Atomic Level

### All Concepts (19)

- - weighted graph: edges carry numeric weights (costs)
- - path weight: total cost of a path = sum of its edge weights
- - single-source shortest path problem: find minimum-cost paths from one source to all vertices
- - shortest-path tree: tree of predecessors encoding shortest paths from source
- - distance estimate (d[v]): mutable estimate of shortest-path cost from source to v
- - predecessor / parent pointer (π[v] or pred[v]): pointer to previous vertex on current best path
- - initialization of distances: d[source] = 0, d[other] = ∞
- - relaxation operation: local update that tries to improve d[v] via an edge (u,v)
- - decrease-key operation on a priority queue to reflect improved distance estimates
- - greedy selection in Dijkstra: extracting the vertex with minimum d[] and finalizing it
- - requirement of nonnegative edge weights for Dijkstra's correctness
- - Bellman–Ford iterative relaxation: repeated passes over edges to propagate improvements
- - iteration bound for Bellman–Ford: at most |V|-1 rounds to stabilize distances
- - negative edge weight handling: Bellman–Ford can handle negative edges (but Dijkstra cannot)
- - negative-weight cycle detection: existence of a cycle whose total weight < 0 implies no well-defined finite shortest paths
- - optimal substructure of shortest paths: any subpath of a shortest path is itself shortest
- - convergence notion: repeated relaxations move estimates monotonically toward true shortest distances
- - reachability vs unreachable: unreachable vertices retain distance ∞
- - finalization concept: a vertex whose d[] will no longer change (e.g., when extracted by Dijkstra)

### Teaching Strategy

Multi-session curriculum - substantial prior knowledge and complex material. Use mastery gates and deliberate practice.

When you ask “what’s the cheapest way to get from s to every other node?”, you’re really asking for a *proof-backed algorithm* that turns local edge information into globally optimal paths. Shortest paths is where greedy choices sometimes work (Dijkstra) and sometimes fail (negative edges), forcing a different strategy (Bellman–Ford).

TL;DR:

Shortest-path distance from a source s to v is the minimum total weight among all s→v paths. The core operation is **edge relaxation**: try to improve d[v] using d[u] + w(u,v). With **nonnegative** weights, Dijkstra uses a priority queue and a greedy “finalize the smallest estimate” rule. With **negative** edges (but no reachable negative cycles), Bellman–Ford repeatedly relaxes all edges until convergence (or detects a negative cycle).

## What Is Shortest Paths?

### The question we’re solving

You’re given a weighted graph and a starting vertex (the **source**) s. Each edge (u,v) has a cost/weight w(u,v). You want, for every vertex v, the **shortest-path distance** δ(s,v): the minimum total cost of any path from s to v.

A path is a sequence of edges:

s = v₀ → v₁ → … → vₖ = v

Its total cost is the sum of its edge weights:

cost(v0→v1→⋯→vk)=∑i=0k−1w(vi,vi+1)\text{cost}(v\_0\to v\_1\to \dots \to v\_k) = \sum\_{i=0}^{k-1} w(v\_i, v\_{i+1})cost(v0​→v1​→⋯→vk​)=i=0∑k−1​w(vi​,vi+1​)

Then the shortest-path distance is:

δ(s,v)=min⁡paths p:s→v ∑(x,y)∈pw(x,y)\delta(s,v) = \min\_{\text{paths } p: s\to v} \ \sum\_{(x,y)\in p} w(x,y)δ(s,v)=paths p:s→vmin​ (x,y)∈p∑​w(x,y)

If v is unreachable from s, we define δ(s,v) = ∞.

### Why shortest paths is more than “like BFS but weighted”

BFS works for **unweighted** graphs (or all edges cost 1), because “fewest edges” equals “minimum cost.” With weights, a path with more edges can be cheaper.

Example: s→a (cost 100), s→b (1), b→a (1). BFS might pick the 1-edge path s→a, but the cheapest path is s→b→a with cost 2.

So we need algorithms that reason about costs.

### Two outputs: distances and predecessors

Most shortest-path algorithms maintain:

- •d[v]: a **current estimate** of δ(s,v)
- •π[v]: a **predecessor** pointer used to reconstruct an actual shortest path (a tree rooted at s)

Distances answer “how far,” predecessors answer “how to get there.”

### Explicit prerequisite / assumptions block (read this once)

To avoid hidden confusion, here are the working assumptions for the lesson:

1. 1)**Directed vs undirected graphs**

- •For an **undirected** edge {u,v} with weight w, treat it as *two directed edges* (u,v) and (v,u) with the same weight.
- •All algorithms below work on directed graphs; undirected graphs are handled via that conversion.

2. 2)**Graph representation**

- •We assume an **adjacency list** representation: for each u, a list of outgoing edges (u,v,w(u,v)).
- •Time bounds are typically written in terms of |V| and |E| using adjacency lists.

3. 3)**Edge-weight requirements**

- •**Dijkstra’s algorithm requires w(u,v) ≥ 0 for every edge reachable from s** (practically: assume all edges are nonnegative).
- •**Bellman–Ford allows negative edges**, but requires **no negative-weight cycle reachable from s** for distances to be well-defined.

4. 4)**Nearby special cases (situating the tools)**

- •If the graph is a **DAG**, shortest paths can be solved in linear time by topological order + relaxation (even with negative edges).
- •If weights are only 0 or 1, **0–1 BFS** (deque-based) beats Dijkstra.

These assumptions are the difference between an algorithm that is correct vs. one that silently gives wrong answers.

### The “triangle inequality” viewpoint

Shortest paths rests on a basic necessary condition: for any edge (u,v), the true shortest distances must satisfy

δ(s,v)≤δ(s,u)+w(u,v)\delta(s,v) \le \delta(s,u) + w(u,v)δ(s,v)≤δ(s,u)+w(u,v)

Because you can always go to u optimally, then take (u,v). Algorithms exploit this by repeatedly enforcing that inequality via relaxation.

## Core Mechanic 1: Edge Relaxation (the atomic step)

### Why relaxation is the heart of shortest paths

Shortest paths feels global (“consider all paths”), but the algorithms work by applying a local rule repeatedly until it forces the global optimum.

That local rule is **edge relaxation**.

Suppose we currently believe d[u] is a good estimate of δ(s,u). Then taking edge (u,v) suggests a candidate distance to v:

candidate=d[u]+w(u,v)\text{candidate} = d[u] + w(u,v)candidate=d[u]+w(u,v)

Relaxation says: if this candidate improves d[v], update it.

### The relaxation rule (with predecessor)

For a directed edge (u,v):

- •If d[u] + w(u,v) < d[v], then
- •d[v] ← d[u] + w(u,v)
- •π[v] ← u

In pseudocode:

```
RELAX(u, v):
  if d[u] + w(u,v) < d[v]:
      d[v] = d[u] + w(u,v)
      π[v] = u
```

### Why relaxation makes sense

Relaxation is just enforcing the inequality:

d[v]≤d[u]+w(u,v)d[v] \le d[u] + w(u,v)d[v]≤d[u]+w(u,v)

If your current d violates it, you fix d[v].

If eventually you reach a point where **no edge can relax**, then you have a stable set of estimates. Under the right conditions (depends on algorithm + weights), that stable point equals the true shortest distances.

### Initialization matters

Almost all shortest-path methods begin with:

- •d[s] = 0
- •d[v] = ∞ for v ≠ s
- •π[v] = NIL

This encodes: “we know how to reach s at cost 0; everything else unknown.”

### A small relaxation walk-through

Take s→a (5), s→b (2), b→a (1). Initialize:

- •d[s]=0, d[a]=∞, d[b]=∞

Relax edges out of s:

- •Relax(s,a): candidate = 0+5=5 < ∞ ⇒ d[a]=5, π[a]=s
- •Relax(s,b): candidate = 0+2=2 < ∞ ⇒ d[b]=2, π[b]=s

Now relax (b,a): candidate = d[b]+1 = 2+1=3 < d[a]=5 ⇒ update d[a]=3, π[a]=b

We discovered a cheaper 2-edge route beating a more direct expensive edge.

### Key idea: algorithms differ in *how they schedule relaxations*

Relaxation is always the operation.

- •**Dijkstra** is selective: it uses a priority queue to choose the next “most promising” vertex and relaxes outgoing edges from it, relying on nonnegative weights to finalize distances.
- •**Bellman–Ford** is exhaustive: it repeats relaxing *all edges*, because negative edges can invalidate greedy finalization.

So when learning shortest paths, keep asking:

1) What relaxations are performed?

2) In what order?

3) When can we stop?

4) When are we allowed to “finalize” a distance?

## Core Mechanic 2: Dijkstra’s Algorithm (nonnegative weights and greedy finalization)

### Why Dijkstra can be greedy

If all edge weights are nonnegative, paths only get more expensive as you extend them. That single fact enables a powerful claim:

> When the vertex with smallest current estimate d[·] is selected next, that estimate is already optimal.

This is the **extract-min finalization** principle.

Intuition: if v currently has the smallest tentative distance, any alternative path to v must go through some not-yet-finalized vertex x with d[x] ≥ d[v]. Adding a nonnegative edge from x onward can’t make a cheaper route to v.

### The algorithm shape

Maintain a min-priority queue keyed by d[v]. Often we keep a set S of “finalized” vertices.

1. 1)Initialize d[s]=0, others ∞.
2. 2)Put all vertices into a min-priority queue Q.
3. 3)While Q not empty:

- •u = EXTRACT-MIN(Q) (u has smallest d among not finalized)
- •For each outgoing edge (u,v): RELAX(u,v)
- •If d[v] decreases, perform DECREASE-KEY(Q,v)

Pseudocode sketch:

```
DIJKSTRA(G, s):
  for v in V:
    d[v] = ∞
    π[v] = NIL
  d[s] = 0

  Q = min-priority-queue over V keyed by d[·]

  while Q not empty:
    u = extract-min(Q)
    for each edge (u,v) in Adj[u]:
      if d[u] + w(u,v) < d[v]:
        d[v] = d[u] + w(u,v)
        π[v] = u
        decrease-key(Q, v)
```

### Correctness idea (why the greedy step is safe)

Let S be the set of extracted vertices so far. Dijkstra maintains the invariant:

- •For every u ∈ S, d[u] = δ(s,u) (final, correct)
- •For every v ∉ S, d[v] is the length of the shortest s→v path that uses only vertices in S internally (frontier estimate)

When we extract-min u, we claim no cheaper path to u exists via vertices not in S. Suppose for contradiction there is a cheaper path P to u that goes through some vertex x ∉ S. Consider the first vertex y on P that is not in S; its predecessor z is in S. When z was finalized, relaxation would set d[y] ≤ d[z]+w(z,y). Because weights are nonnegative, the remainder of the path from y to u can’t reduce the cost below d[y]. This would imply u shouldn’t have been the minimum. Contradiction.

The nonnegativity is used precisely when we say “continuing along the path cannot make it cheaper.” With negative edges, it absolutely can.

### Complexity (with adjacency lists)

Let |V| = n, |E| = m.

- •Using a **binary heap** priority queue:
- •extract-min: O(log n) done n times
- •decrease-key: O(log n) done up to m times
- •Total: O((n + m) log n)

- •Using a Fibonacci heap (advanced): O(n log n + m)

Given the prerequisite includes heaps, the binary heap bound is the one to internalize.

### What Dijkstra returns

- •Distances d[v]
- •Predecessors π[v] forming a shortest-path tree for reachable vertices

To reconstruct path to t:

- •follow π[t] backwards until s
- •reverse the sequence

### When Dijkstra fails

If there’s a reachable negative edge, the extract-min “finalization” can lock in a distance too early.

Tiny counterexample:

- •s→a (2)
- •s→b (5)
- •b→a (-10)

Dijkstra extracts a first (d[a]=2) and finalizes it. Later, when b is processed, it discovers a cheaper route to a of cost -5, but a is already finalized, so the algorithm (in its standard form) will not correct it. The greedy proof breaks because weights aren’t nonnegative.

So: **Dijkstra is fast, but only under the correct weight assumptions.**

## Core Mechanic 3: Bellman–Ford (negative edges and cycle detection)

### Why Bellman–Ford exists

Negative edges break greedy finalization, but shortest paths can still be well-defined as long as there is **no negative-weight cycle reachable from s**.

A negative cycle means you can loop to reduce path cost without bound:

cycle cost<0⇒δ(s,v)=−∞ for vertices reachable after that cycle\text{cycle cost} < 0 \Rightarrow \delta(s,v) = -\infty \text{ for vertices reachable after that cycle}cycle cost<0⇒δ(s,v)=−∞ for vertices reachable after that cycle

So a correct algorithm must either:

- •compute distances when no negative cycle is reachable, or
- •report that a negative cycle exists

Bellman–Ford does exactly that.

### The key fact: shortest paths use at most |V|−1 edges

If there are no negative cycles reachable from s, then an optimal shortest path to any vertex can be chosen to be **simple** (no repeated vertices). A simple path in a graph with n vertices has at most n−1 edges.

This gives a natural plan:

- •After 1 full pass of relaxing all edges, you know shortest paths using ≤1 edge.
- •After 2 passes, you know shortest paths using ≤2 edges.
- •…
- •After n−1 passes, you know shortest paths using ≤n−1 edges, which is enough.

### Bellman–Ford algorithm

Initialize d[s]=0, others ∞.

Repeat n−1 times:

- •for each edge (u,v) in E:
- •RELAX(u,v)

Then do one more pass to detect negative cycles:

- •if any edge can still relax, a negative cycle is reachable.

Pseudocode:

```
BELLMAN-FORD(G, s):
  for v in V:
    d[v] = ∞
    π[v] = NIL
  d[s] = 0

  for i = 1 to |V|-1:
    for each edge (u,v) in E:
      RELAX(u,v)

  for each edge (u,v) in E:
    if d[u] + w(u,v) < d[v]:
      return "negative cycle reachable"

  return d, π
```

### Why the repeated passes work (a paced invariant)

Define δᵢ(s,v) = the shortest path from s to v using at most i edges.

Claim: after i full passes of relaxing all edges, d[v] = δᵢ(s,v).

- •Base i=0: d[s]=0 and others ∞ matches “0-edge paths.”
- •Step: any ≤(i+1)-edge path to v ends with some edge (u,v), where the prefix to u uses ≤i edges. If after i passes d[u]=δᵢ(s,u), then relaxing (u,v) can set d[v] ≤ d[u]+w(u,v) = cost of that candidate ≤(i+1)-edge path. Taking min over all incoming edges gives δᵢ₊₁(s,v).

After n−1 passes, δₙ₋₁(s,v)=δ(s,v) when no negative cycles are reachable.

### Complexity

Bellman–Ford is slower:

- •Outer loop: n−1
- •Inner loop: m edge relaxations

Total time: O(nm)

But it buys you two capabilities Dijkstra doesn’t have:

1. 1)handles negative edges
2. 2)detects negative cycles

### Practical improvement: early stopping

In many graphs, distances converge before n−1 passes. You can track whether any relaxation happened in a pass; if none happened, stop early.

This doesn’t change worst-case big-O, but helps in practice.

### What about unreachable vertices?

If v is unreachable, d[v] stays ∞ forever.

In the negative-cycle detection pass, edges out of unreachable vertices do not matter because their d[u]=∞, and ∞ + w won’t relax anything.

### Summary comparison (at the decision level)

Bellman–Ford is the “safe general tool” for signed weights (no negative cycles). Dijkstra is the fast specialized tool for nonnegative weights.

The skill is choosing based on weight signs and required guarantees.

## Application/Connection: Choosing the Right Tool and Why It Unlocks Network Flow

### Algorithm selection guide (with nearby special cases)

Picking the right shortest-path method is mostly about graph structure and edge weights.

| Setting | Recommended tool | Why |
| --- | --- | --- |
| Unweighted (or all weights equal) | BFS | Layer-by-layer equals minimal cost |
| Weights are 0 or 1 | 0–1 BFS | Deque gives O( | V | + | E | ) |
| All weights ≥ 0 | Dijkstra + heap | Greedy finalization is correct and fast |
| Some weights negative, no negative cycle reachable | Bellman–Ford | Repeated relaxation converges |
| DAG (can have negative weights) | Topological DP + relax | No cycles, linear-time |

Even if you only implement Dijkstra and Bellman–Ford now, keeping the table in mind prevents misapplication.

### Path reconstruction (a common “real deliverable”)

Distances are useful, but applications often need the actual route.

Given π[v], reconstruct s→t:

1. 1)Start at t.
2. 2)Repeatedly set t ← π[t] until NIL.
3. 3)Reverse the collected vertices.

If you hit NIL before reaching s, then t was unreachable.

### Connection to Network Flow (why shortest paths matters later)

Shortest paths shows up inside flow algorithms in two major ways:

1. 1)**Residual graphs and finding augmenting paths**

Basic max-flow (like Ford–Fulkerson) repeatedly finds an s→t path in a residual graph. If you choose augmenting paths carefully, you can improve runtime.

2. 2)**Min-Cost Max-Flow (advanced but motivating)**

A common extension of flow problems is minimizing total cost while sending as much flow as possible. Those algorithms repeatedly compute shortest paths in a residual network where edge costs can be negative due to reverse edges.

That’s where understanding **weight-sign applicability** becomes essential:

- •Residual networks can introduce negative edges.
- •You may need Bellman–Ford (or Johnson’s reweighting, later) to keep shortest-path computations correct.

So shortest paths is not just a graph topic; it’s a core subroutine that powers more complex optimization.

### Mental model to keep

- •Relaxation is enforcing local constraints.
- •Dijkstra works when nonnegativity makes “smallest tentative is final” true.
- •Bellman–Ford works when repeated enforcement up to n−1 edges is enough.

This mental model transfers cleanly into flow, dynamic programming on graphs, and many ML/OR optimization formulations.

## Worked Examples (3)

### Dijkstra on a small nonnegative graph (compute d[·] and π[·])

Directed graph with source s and edges:

- •s→a (4)
- •s→b (1)
- •b→a (2)
- •a→c (1)
- •b→c (5)
- •c→d (3)
- •a→d (7)

All weights are ≥ 0, so Dijkstra applies.

Goal: compute shortest distances from s to all vertices and one shortest path to d.

1. Initialize:

   - •d[s]=0
   - •d[a]=d[b]=d[c]=d[d]=∞
   - •π[·]=NIL

   Priority queue contains all vertices keyed by d.
2. Extract-min: u = s (d=0). Relax outgoing edges:

   - •Relax(s,a): 0+4 < ∞ ⇒ d[a]=4, π[a]=s
   - •Relax(s,b): 0+1 < ∞ ⇒ d[b]=1, π[b]=s

   Now tentative distances: d[b]=1, d[a]=4, others ∞.
3. Extract-min: u = b (d=1). Relax outgoing edges:

   - •Relax(b,a): 1+2=3 < d[a]=4 ⇒ d[a]=3, π[a]=b
   - •Relax(b,c): 1+5=6 < ∞ ⇒ d[c]=6, π[c]=b

   Now d[a]=3, d[c]=6, d[d]=∞.
4. Extract-min: u = a (d=3). Relax outgoing edges:

   - •Relax(a,c): 3+1=4 < d[c]=6 ⇒ d[c]=4, π[c]=a
   - •Relax(a,d): 3+7=10 < ∞ ⇒ d[d]=10, π[d]=a

   Now d[c]=4, d[d]=10.
5. Extract-min: u = c (d=4). Relax outgoing edges:

   - •Relax(c,d): 4+3=7 < d[d]=10 ⇒ d[d]=7, π[d]=c

   Now d[d]=7.
6. Extract-min: u = d (d=7). No outgoing edges to improve anything. Done.
7. Final distances:

   - •d[s]=0
   - •d[b]=1
   - •d[a]=3
   - •d[c]=4
   - •d[d]=7

   Reconstruct path to d using π:

   - •π[d]=c, π[c]=a, π[a]=b, π[b]=s

   So path is s→b→a→c→d with total cost 1+2+1+3=7.

**Insight:** Notice how the best route to a was not the direct edge (cost 4) but via b (cost 3). Dijkstra discovers this through relaxation, and nonnegative weights ensure once a vertex is extracted, its distance never needs revision.

### Bellman–Ford with a negative edge (and no negative cycle)

Directed graph with source s and edges:

- •s→a (1)
- •s→b (10)
- •a→c (2)
- •b→c (-10)
- •c→d (3)

There is a negative edge b→c, so Dijkstra is not safe. Use Bellman–Ford to compute shortest distances and show convergence.

1. Initialize:

   - •d[s]=0
   - •d[a]=d[b]=d[c]=d[d]=∞
   - •π[·]=NIL

   We will do |V|-1 = 4 passes (vertices: s,a,b,c,d ⇒ |V|=5).
2. Pass 1 (relax all edges in any order; we’ll list them):

   1) Relax(s,a): d[a] = min(∞, 0+1)=1, π[a]=s

   2) Relax(s,b): d[b] = min(∞, 0+10)=10, π[b]=s

   3) Relax(a,c): d[c] = min(∞, 1+2)=3, π[c]=a

   4) Relax(b,c): candidate = 10 + (-10) = 0 < d[c]=3 ⇒ d[c]=0, π[c]=b

   5) Relax(c,d): d[d] = min(∞, 0+3)=3, π[d]=c

   End of pass 1: d[a]=1, d[b]=10, d[c]=0, d[d]=3.
3. Pass 2:

   1) Relax(s,a): candidate 0+1=1 (no change)

   2) Relax(s,b): candidate 10 (no change)

   3) Relax(a,c): candidate 1+2=3 (no change; d[c]=0 is better)

   4) Relax(b,c): candidate 10-10=0 (no change)

   5) Relax(c,d): candidate 0+3=3 (no change)

   No changes occurred in this pass ⇒ we can stop early (optional optimization).
4. Negative-cycle check (one extra scan):

   For each edge (u,v), verify d[u] + w(u,v) < d[v] is false.

   - •All checks fail to relax ⇒ no reachable negative cycle.
5. Final distances:

   - •d[a]=1 via s→a
   - •d[b]=10 via s→b
   - •d[c]=0 via s→b→c (10 + -10)
   - •d[d]=3 via s→b→c→d

   Reconstruct d: π[d]=c, π[c]=b, π[b]=s ⇒ s→b→c→d.

**Insight:** Bellman–Ford succeeds because it does not finalize vertices early. The negative edge b→c can improve c even after c was already assigned a tentative value (3 via a). Repeated full-edge relaxations ensure these late improvements propagate.

### Negative cycle detection (why distances can be undefined)

Directed graph with source s and edges:

- •s→a (1)
- •a→b (1)
- •b→a (-3)

This creates a cycle a→b→a with total weight 1 + (-3) = -2, reachable from s.

Run the Bellman–Ford logic conceptually to see detection.

1. Initialize d[s]=0, others ∞.
2. After relaxing enough times, d[a] and d[b] keep decreasing:

   - •s→a sets d[a]=1
   - •a→b sets d[b]=2
   - •b→a sets d[a]=-1

   Then again:

   - •a→b sets d[b]=0
   - •b→a sets d[a]=-3

   This can repeat indefinitely, lowering costs without bound.
3. Bellman–Ford after |V|-1 passes performs one more edge scan.

   Because the cycle is negative, at least one edge on the cycle will still be able to relax:

   For example, if currently d[b]=0, then b→a gives candidate -3 < current d[a], so a relaxation is still possible.
4. Algorithm reports a reachable negative cycle, meaning shortest-path distances are not well-defined (they are effectively −∞ for vertices reachable after looping).

**Insight:** The extra pass is not a technicality: it’s the mathematical line between “there exists a minimum” and “you can always do better by looping.”

## Key Takeaways

- ✓

  The shortest-path distance δ(s,v) is the minimum total weight over all s→v paths; unreachable vertices have distance ∞.
- ✓

  Relaxation is the core operation: if d[u] + w(u,v) improves d[v], update d[v] and set π[v]=u.
- ✓

  Dijkstra’s algorithm is correct only when all reachable edge weights are nonnegative; then extract-min finalizes a vertex’s distance.
- ✓

  With a binary heap and adjacency lists, Dijkstra runs in O((|V|+|E|) log |V|).
- ✓

  Bellman–Ford handles negative edges by relaxing all edges |V|−1 times, giving O(|V||E|) time.
- ✓

  If any edge can still relax after |V|−1 passes, a negative cycle reachable from s exists and shortest paths are undefined (−∞).
- ✓

  Predecessor pointers π[·] let you reconstruct actual shortest paths, not just distances.
- ✓

  Special cases matter: DAG shortest paths (topological order) and 0–1 BFS can outperform the general algorithms in their niches.

## Common Mistakes

- ✗

  Running Dijkstra on graphs with negative edges (even a single reachable negative edge can invalidate the greedy finalization).
- ✗

  Forgetting that undirected edges must be treated as two directed edges; mixing representations can lead to missing relaxations.
- ✗

  Not using decrease-key (or an equivalent approach) with Dijkstra’s priority queue, leading to incorrect or slower implementations.
- ✗

  Misinterpreting Bellman–Ford’s negative-cycle result: it only guarantees detection of cycles *reachable from s* (unreachable negative cycles don’t affect δ(s,·)).

## Practice

easy

You have a directed graph with weights all ≥ 0 and you run Dijkstra from s. After extracting some set S of vertices, a vertex u is extracted next with smallest key d[u]. Explain (in 2–4 sentences) why d[u] cannot later be improved by a path that goes through any vertex outside S.

**Hint:** Use the idea: any alternative path to u must cross from S to V\S somewhere; weights are nonnegative so costs can’t drop after that crossing.

Show solution

Consider any path P from s to u that uses a vertex outside S. Let (x,y) be the first edge on P with x ∈ S and y ∉ S. When x was extracted, d[x]=δ(s,x), and relaxing (x,y) would ensure d[y] ≤ d[x]+w(x,y). Since all weights are ≥ 0, the remaining suffix from y to u cannot make the total cost smaller than d[y], so u could not have a smaller true distance than the current minimum key d[u]. Thus d[u] is final when extracted.

medium

Run Bellman–Ford for 3 passes on this graph (source s). Vertices: s,a,b,c. Edges: s→a (4), s→b (5), a→b (-2), b→c (3), a→c (10). Compute d[a], d[b], d[c] after each pass.

**Hint:** Initialize d[s]=0, others ∞. In each pass, relax edges in the listed order. Track updates carefully, especially from a→b (-2).

Show solution

Initialization: d[a]=∞, d[b]=∞, d[c]=∞.

Pass 1:

- •s→a: d[a]=4
- •s→b: d[b]=5
- •a→b: candidate 4-2=2 < 5 ⇒ d[b]=2
- •b→c: candidate 2+3=5 ⇒ d[c]=5
- •a→c: candidate 4+10=14 (no change)

After pass 1: d[a]=4, d[b]=2, d[c]=5.

Pass 2:

- •s→a: 4 (no change)
- •s→b: candidate 5 (no change; d[b]=2)
- •a→b: candidate 2 (no change)
- •b→c: candidate 5 (no change)
- •a→c: 14 (no change)

After pass 2: d[a]=4, d[b]=2, d[c]=5.

Pass 3: identical, no changes.

So distances converge after pass 1.

easy

Decide which algorithm to use (and why) for each case:

1) weights are {0,1}

2) DAG with some negative edges

3) general graph with a negative edge but you also need to detect negative cycles

4) road network with all distances positive

**Hint:** Match each case to the selection table: 0–1 BFS, DAG shortest paths, Bellman–Ford, Dijkstra.

Show solution

1) 0–1 BFS, because weights are only 0/1 and you can use a deque for O(|V|+|E|).

2) DAG shortest paths via topological order + relaxation, because acyclicity guarantees correctness even with negative edges.

3) Bellman–Ford, because it supports negative edges and includes a negative-cycle detection pass.

4) Dijkstra, because all weights are nonnegative and it’s typically faster (O((|V|+|E|) log |V|) with a heap).

## Connections

Next nodes you can tackle:

- •[Network Flow](/tech-tree/network-flow/) — shortest paths often appear inside min-cost flow methods and residual-graph reasoning.

Related/background nodes to review if needed:

- •[Graph Traversal](/tech-tree/graph-traversal/) — BFS is the shortest-path algorithm for unweighted graphs.
- •[Heaps](/tech-tree/heaps/) — priority queues enable Dijkstra’s efficiency.

Nearby special-case extensions (good follow-ups):

- •[DAG Shortest Paths](/tech-tree/dag-shortest-paths/)
- •[0–1 BFS](/tech-tree/zero-one-bfs/)

Quality: A (4.5/5)

[← back to tree](/tech-tree/)[browse all →](/tech-tree/inventory/)
