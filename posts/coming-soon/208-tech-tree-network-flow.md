---
title: Network Flow
description: Max-flow min-cut theorem. Ford-Fulkerson algorithm.
date: '2026-07-01'
scheduled: '2027-01-24'
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
inspiration_url: https://templeton.host/tech-tree/network-flow/
inspiration_category: tech-tree
---

> Source-copy draft imported from [https://templeton.host/tech-tree/network-flow/](https://templeton.host/tech-tree/network-flow/). Names, domain references, and local media paths were adapted for Xavi Ablaza / getablaza.com.

[←Back to Tech Tree](/tech-tree/)

[inventory](/tech-tree/inventory/)[coverage](/tech-tree/coverage/)

# Network Flow

Graph TheoryDifficulty: ★★★★☆Depth: 8Unlocks: 0

Max-flow min-cut theorem. Ford-Fulkerson algorithm.

## Interactive Visualization

⏮◀◀▶▶STEP0.25x1xZOOM

t=0s

## Core Concepts

- -Feasible s-t flow: assignment f(u,v) satisfying capacity bounds (0 <= f(u,v) <= c(u,v)) and flow conservation at every intermediate vertex
- -Residual network and augmenting path: edges with available (unused or reversible) capacity form a residual graph; an augmenting path is an s->t path in this graph allowing flow increase
- -s-t cut and cut capacity: a partition (S,T) with s in S, t in T; cut capacity is the sum of capacities of edges from S to T

## Key Symbols & Notation

f(u,v) = flow on edge (u,v)c(u,v) = capacity of edge (u,v)

## Essential Relationships

- -Max-flow min-cut and augmenting-path equivalence: the maximum value of any feasible s-t flow equals the minimum s-t cut capacity; equivalently a flow is maximum iff there is no augmenting path in the residual network (which induces a saturated minimum cut)

## Prerequisites (2)

[Shortest Paths6 atoms](/tech-tree/shortest-paths/)[Linear Programming6 atoms](/tech-tree/linear-programming/)

## Referenced by (7)

Where this concept shows up in the operating-finance and personal-finance graphs.

### From Business (7)

[AllocationBusiness

Routing flows in networks is explicitly named as an allocation domain. Max-flow min-cut and minimum cost flow are LP special cases with combinatorial structure](/business/allocation/)[resource allocationBusiness

Explicitly named in the concept description; min-cost network flow is resource allocation on graphs, solved by primal-dual methods](/business/resource-allocation/)[BottleneckBusiness

Bottleneck capacity is defined within max-flow theory; Ford-Fulkerson pushes flow equal to the path bottleneck, and max-flow min-cut theorem shows the global bottleneck equals the minimum cut capacity](/business/bottleneck/)[CommodityBusiness

Commodity flow is exactly the max-flow problem formalized: Ford-Fulkerson algorithm finds maximum s-t flow, and the max-flow min-cut theorem gives the dual characterization of capacity bottlenecks](/business/commodity/)[Pipeline VelocityBusiness

Max-flow min-cut theorem is the direct mathematical formalization of pipeline bottleneck analysis. Pipeline velocity equals max flow; the bottleneck IS the minimum cut. Improving velocity means increasing capacity at the min-cut edges.](/business/pipeline-velocity/)[Process BottlenecksBusiness

Max-flow min-cut theorem is the mathematical formalization of bottleneck analysis - pipeline velocity is bounded by the capacity of its tightest constraint, and identifying the min-cut tells you exactly which process stage to widen](/business/process-bottlenecks/)[Investment PortfolioBusiness

Routing flows in networks maps directly to network flow theory - max-flow min-cut governs capacity-constrained allocation across edges, the dual framing of portfolio as flow routing](/business/investment-portfolio/)

Advanced Learning Details

### Graph Position

138

Depth Cost

0

Fan-Out (ROI)

0

Bottleneck Score

8

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

### All Concepts (20)

- - Flow as an assignment on directed edges: a function f(u,v) giving amount sent on edge (u,v) (feasible flows are those meeting the constraints below)
- - Capacity constraint for each directed edge: a nonnegative upper bound c(u,v) with 0 <= f(u,v) <= c(u,v)
- - Flow conservation at intermediate vertices: for every vertex other than source s and sink t, sum of incoming flow equals sum of outgoing flow
- - Value of a flow: net flow out of the source (equivalently net flow into the sink) as the objective quantity to maximize
- - s-t cut: a partition of vertices into S and T with source s in S and sink t in T
- - Capacity of a cut: the sum of capacities of edges directed from S to T (this is an upper bound on any s-t flow)
- - Residual graph: a derived directed graph G\_f whose edges represent how an existing flow can be changed; it contains forward edges with remaining capacity and backward edges representing possible cancellation
- - Residual capacity of an edge: c\_f(u,v) describing how much more flow can be pushed from u to v in the residual graph (forward residual = c(u,v)-f(u,v); backward residual = f(u,v))
- - Augmenting path: an s-to-t path in the residual graph with all edges having positive residual capacity
- - Bottleneck (augment amount) of a path: the minimum residual capacity along an augmenting path used to increase flow
- - Augmentation step: the operation of increasing flow along a chosen augmenting path by the bottleneck amount and updating the residual graph
- - Ford-Fulkerson method (generic): initialize zero flow, repeatedly find an augmenting path in the residual graph and augment, stop when no augmenting path exists
- - Role of reverse/backward edges in algorithms: explicit reverse edges in the residual graph allow cancellation or rerouting of previously assigned flow
- - Flow decomposition: any feasible flow can be decomposed into a multiset of s-t path flows and cycle flows
- - Max-flow min-cut theorem: the maximum possible value of an s-t flow equals the minimum capacity among all s-t cuts
- - Weak duality relation: the value of any feasible flow is at most the capacity of any s-t cut (used in correctness proofs)
- - Integrality property: if all capacities are integers then there exists a maximum flow that assigns integer flow values on all edges
- - Termination and correctness caveats for Ford-Fulkerson: with integer capacities the basic FF procedure terminates after a finite number of augmentations; with arbitrary real/irrational capacities naive augmentation might not terminate or might require special path-selection policies
- - Algorithmic consequence of path choice: different augmenting-path selection strategies affect runtime (e.g., BFS shortest-augmenting-path leads to Edmonds-Karp with provable polynomial bounds)
- - Optimality certificates: an s-t cut whose capacity equals the current flow value certifies that the flow is maximum

### Teaching Strategy

Multi-session curriculum - substantial prior knowledge and complex material. Use mastery gates and deliberate practice.

If you’ve ever tried to route “as much as possible” through a bottlenecked system—traffic through streets, data through links, jobs through machines—you’ve met network flow. The surprising part is that the answer to “how much can we push?” is exactly equal to a seemingly different object: the capacity of a best “barrier” (a cut) separating source from sink.

TL;DR:

A feasible s–t flow assigns values f(u,v) on directed edges so that 0 ≤ f(u,v) ≤ c(u,v) and every intermediate vertex conserves flow. The Ford–Fulkerson method repeatedly finds an augmenting path in the residual network (edges with remaining capacity, plus backward edges that allow undoing flow) and augments along it. When no augmenting path exists, the flow is maximum and the set of vertices reachable from s in the residual graph defines a minimum s–t cut, proving max-flow = min-cut.

## What Is Network Flow?

### Why this problem exists (motivation)

Many optimization problems on graphs are about **routes** (shortest path), **orderings** (topological constraints), or **structures** (spanning trees). Network flow is different: it is about **simultaneous movement** through many edges at once, where each edge has a limited capacity.

Think of a directed graph as a pipe network:

- •**Vertices** are junctions.
- •**Edges** are pipes.
- •**Capacities** are how much can pass through a pipe per unit time.
- •A **source** sss injects flow; a **sink** ttt absorbs it.

The core question:

> What is the maximum amount of flow that can be sent from sss to ttt without violating edge capacities?

### Formal definition: flow network

A **flow network** is a directed graph G=(V,E)G = (V,E)G=(V,E) with:

- •a source s∈Vs \in Vs∈V
- •a sink t∈Vt \in Vt∈V
- •a **capacity function** c:E→R≥0c: E \to \mathbb{R}\_{\ge 0}c:E→R≥0​, where c(u,v)c(u,v)c(u,v) is the capacity of edge (u,v)(u,v)(u,v)

We allow the convention that if (u,v)∉E(u,v) \notin E(u,v)∈/E, then c(u,v)=0c(u,v)=0c(u,v)=0.

### Feasible sss–ttt flow

A **flow** is a function f:V×V→Rf: V \times V \to \mathbb{R}f:V×V→R (often only nonzero on edges), interpreted as f(u,v)f(u,v)f(u,v) = amount sent on edge (u,v)(u,v)(u,v).

A flow is **feasible** if it satisfies:

1) **Capacity constraints** (can’t exceed the pipe):

- •For every (u,v)(u,v)(u,v),

0≤f(u,v)≤c(u,v).0 \le f(u,v) \le c(u,v).0≤f(u,v)≤c(u,v).

2) **Flow conservation** (what goes in must go out) for every intermediate vertex v∈V∖{s,t}v \in V \setminus \{s,t\}v∈V∖{s,t}:

Let incoming flow to vvv be ∑u∈Vf(u,v)\sum\_{u \in V} f(u,v)∑u∈V​f(u,v) and outgoing be ∑w∈Vf(v,w)\sum\_{w \in V} f(v,w)∑w∈V​f(v,w). Then

∑u∈Vf(u,v)=∑w∈Vf(v,w).\sum\_{u \in V} f(u,v)
= \sum\_{w \in V} f(v,w).u∈V∑​f(u,v)=w∈V∑​f(v,w).

Equivalently, net flow at vvv is zero.

3) **Value of the flow** (objective):

The amount successfully sent from sss to ttt is

∣f∣=∑v∈Vf(s,v)−∑v∈Vf(v,s).|f| = \sum\_{v \in V} f(s,v) - \sum\_{v \in V} f(v,s).∣f∣=v∈V∑​f(s,v)−v∈V∑​f(v,s).

In many treatments we assume no edges enter sss and no edges leave ttt, making this simply ∣f∣=∑vf(s,v)|f| = \sum\_{v} f(s,v)∣f∣=∑v​f(s,v).

### Connection to linear programming (you already know this)

Max flow is a linear program:

- •Variables: f(u,v)f(u,v)f(u,v)
- •Constraints: capacity bounds and conservation
- •Objective: maximize ∣f∣|f|∣f∣

That matters because it hints at:

- •Why a theorem like max-flow min-cut could hold (duality flavor)
- •Why integral capacities often lead to integral optimal flows (totally unimodular structure)

But the network-flow viewpoint gives more than “solve an LP”: it gives a **combinatorial algorithm** and a geometric intuition.

### The other side of the coin: cuts

A cut feels like a “barrier” rather than a “routing.” Yet it pins down the answer.

An **$s$–$t$ cut** is a partition of vertices into two sets (S,T)(S,T)(S,T) such that:

- •s∈Ss \in Ss∈S
- •t∈Tt \in Tt∈T
- •S∪T=VS \cup T = VS∪T=V, S∩T=∅S \cap T = \emptysetS∩T=∅

The **capacity of the cut** is the total capacity of edges going from SSS to TTT:

c(S,T)=∑u∈S, v∈Tc(u,v).c(S,T) = \sum\_{u \in S,\ v \in T} c(u,v).c(S,T)=u∈S, v∈T∑​c(u,v).

Intuition: if you draw a boundary around SSS, the only way flow can go from sss to ttt is to cross from SSS to TTT. Those crossing edges limit the total possible flow.

We will later prove:

max⁡f∣f∣=min⁡(S,T)c(S,T).\max\_f |f| = \min\_{(S,T)} c(S,T).fmax​∣f∣=(S,T)min​c(S,T).

That equality is the Max-Flow Min-Cut Theorem—the central result of this node.

## Core Mechanic 1: Residual Networks and Augmenting Paths

### Why we need residual networks

Suppose you have some feasible flow fff. You want to increase it.

If an edge (u,v)(u,v)(u,v) has unused capacity, you can push more forward.

But you also want the ability to **change your mind**: if later you discover that flow you sent earlier blocks a better routing, you’d like to pull some flow back and reroute it elsewhere.

Residual networks encode **both** possibilities:

- •remaining forward capacity
- •reversible capacity (send flow “backward” to undo)

This is what makes Ford–Fulkerson work.

### Residual capacity

Given a capacity c(u,v)c(u,v)c(u,v) and current flow f(u,v)f(u,v)f(u,v), the **forward residual capacity** is:

cf(u,v)=c(u,v)−f(u,v).c\_f(u,v) = c(u,v) - f(u,v).cf​(u,v)=c(u,v)−f(u,v).

If cf(u,v)>0c\_f(u,v) > 0cf​(u,v)>0, you can increase f(u,v)f(u,v)f(u,v).

Now the crucial twist: if f(u,v)>0f(u,v) > 0f(u,v)>0, you can **decrease** it by sending flow in the reverse direction. That creates a **backward edge** (v,u)(v,u)(v,u) in the residual graph with residual capacity:

cf(v,u)=f(u,v).c\_f(v,u) = f(u,v).cf​(v,u)=f(u,v).

This is not a real physical edge in the original network; it represents “canceling” previously sent flow.

### Residual network GfG\_fGf​

The **residual network** Gf=(V,Ef)G\_f = (V, E\_f)Gf​=(V,Ef​) contains all directed edges with positive residual capacity:

- •include (u,v)(u,v)(u,v) if cf(u,v)>0c\_f(u,v) > 0cf​(u,v)>0

Each such edge has capacity cf(u,v)c\_f(u,v)cf​(u,v).

### Augmenting path

An **augmenting path** is any directed path from sss to ttt in the residual network GfG\_fGf​.

If you can find one, you can increase the total flow value.

Let PPP be an augmenting path. The maximum amount you can push through it is limited by the smallest residual capacity along it:

Δ=min⁡(u,v)∈Pcf(u,v).\Delta = \min\_{(u,v) \in P} c\_f(u,v).Δ=(u,v)∈Pmin​cf​(u,v).

This Δ\DeltaΔ is called the **bottleneck** of the path.

### How augmentation updates the flow

For each edge (u,v)(u,v)(u,v) on the path PPP:

- •If (u,v)(u,v)(u,v) is a **forward** edge of the original direction, do

f(u,v)←f(u,v)+Δ.f(u,v) \leftarrow f(u,v) + \Delta.f(u,v)←f(u,v)+Δ.

- •If (u,v)(u,v)(u,v) is a **backward** residual edge (meaning original had flow from vvv to uuu), do

f(v,u)←f(v,u)−Δ.f(v,u) \leftarrow f(v,u) - \Delta.f(v,u)←f(v,u)−Δ.

This preserves feasibility:

- •Capacity bounds: we never exceed because Δ≤cf(u,v)\Delta \le c\_f(u,v)Δ≤cf​(u,v)
- •Conservation: along the internal vertices of the path, what you add in equals what you add out (a telescoping effect)

### Diagram 1: Residual forward and backward edges (static SVG)

The picture below shows one original edge and the residual edges it induces.

```
<svg xmlns="http://www.w3.org/2000/svg" width="820" height="230" viewBox="0 0 820 230" role="img" aria-label="Residual network illustration showing forward residual capacity and backward residual edge for canceling flow">
  <defs>
    <marker id="arrow" markerWidth="10" markerHeight="10" refX="10" refY="3" orient="auto" markerUnits="strokeWidth">
      <path d="M0,0 L10,3 L0,6 Z" fill="#222" />
    </marker>
    <marker id="arrowBlue" markerWidth="10" markerHeight="10" refX="10" refY="3" orient="auto" markerUnits="strokeWidth">
      <path d="M0,0 L10,3 L0,6 Z" fill="#1f77b4" />
    </marker>
    <marker id="arrowRed" markerWidth="10" markerHeight="10" refX="10" refY="3" orient="auto" markerUnits="strokeWidth">
      <path d="M0,0 L10,3 L0,6 Z" fill="#d62728" />
    </marker>
  </defs>

  <!-- Nodes -->
  <circle cx="170" cy="115" r="28" fill="#fff" stroke="#222" stroke-width="2" />
  <text x="170" y="121" text-anchor="middle" font-family="sans-serif" font-size="16">u</text>

  <circle cx="650" cy="115" r="28" fill="#fff" stroke="#222" stroke-width="2" />
  <text x="650" y="121" text-anchor="middle" font-family="sans-serif" font-size="16">v</text>

  <!-- Original edge -->
  <line x1="198" y1="115" x2="622" y2="115" stroke="#222" stroke-width="3" marker-end="url(#arrow)" />
  <text x="410" y="90" text-anchor="middle" font-family="sans-serif" font-size="14" fill="#222">original edge (u→v)</text>
  <text x="410" y="136" text-anchor="middle" font-family="sans-serif" font-size="14" fill="#222">capacity c(u,v)=10, current flow f(u,v)=6</text>

  <!-- Residual forward -->
  <line x1="210" y1="55" x2="610" y2="55" stroke="#1f77b4" stroke-width="3" marker-end="url(#arrowBlue)" />
  <text x="410" y="40" text-anchor="middle" font-family="sans-serif" font-size="14" fill="#1f77b4">forward residual: c_f(u,v)=c-f=4</text>

  <!-- Residual backward -->
  <line x1="610" y1="175" x2="210" y2="175" stroke="#d62728" stroke-width="3" marker-end="url(#arrowRed)" />
  <text x="410" y="200" text-anchor="middle" font-family="sans-serif" font-size="14" fill="#d62728">backward residual: c_f(v,u)=f=6 (can cancel)</text>

  <text x="410" y="18" text-anchor="middle" font-family="sans-serif" font-size="16" fill="#222">Residual edges represent “can add” and “can undo”</text>
</svg>
```

### A small but important conceptual pause

Residual edges are often the hardest part to internalize. Two reminders help:

1) Backward residual edges do **not** violate the original graph direction. They are bookkeeping that says: “you may reduce the earlier decision.”

2) Augmenting along a residual path may mix forward and backward edges. That corresponds to a **rerouting**: some flow gets pushed into a new corridor, and some earlier corridor gets partially emptied.

### Why augmenting paths increase flow value

Let PPP be an s→ts \to ts→t path and augment by Δ\DeltaΔ.

- •At sss, you increase net outgoing by Δ\DeltaΔ.
- •At ttt, you increase net incoming by Δ\DeltaΔ.
- •At internal vertices, increases cancel (one edge adds Δ\DeltaΔ in, another adds Δ\DeltaΔ out).

So:

∣f∣←∣f∣+Δ.|f| \leftarrow |f| + \Delta.∣f∣←∣f∣+Δ.

That’s the engine of Ford–Fulkerson.

## Core Mechanic 2: Ford–Fulkerson and Why It Eventually Stops

### The algorithm idea (why before how)

We want maximum flow. Instead of guessing a final flow, we:

1) start with zero flow

2) repeatedly find a way to push more (augmenting path)

3) stop when no improvement is possible

This is a classic “local improvement” strategy, except the residual network is designed so that “no local improvement” actually implies “global optimum.”

### Ford–Fulkerson method (high-level)

Initialize f(u,v)=0f(u,v)=0f(u,v)=0 for all edges.

Repeat:

- •Construct residual graph GfG\_fGf​
- •Find any sss–ttt path PPP in GfG\_fGf​
- •Let Δ=min⁡(u,v)∈Pcf(u,v)\Delta = \min\_{(u,v) \in P} c\_f(u,v)Δ=min(u,v)∈P​cf​(u,v)
- •Augment along PPP by Δ\DeltaΔ

Stop when no augmenting path exists.

### Pseudocode (conceptual)

- •While there exists an augmenting path PPP in GfG\_fGf​:
- •Δ←min⁡\Delta \leftarrow \minΔ←min residual capacity on PPP
- •For each edge (u,v)(u,v)(u,v) on PPP:
- •if (u,v)(u,v)(u,v) is a forward residual edge: f(u,v)←f(u,v)+Δf(u,v) \leftarrow f(u,v) + \Deltaf(u,v)←f(u,v)+Δ
- •else (backward): f(v,u)←f(v,u)−Δf(v,u) \leftarrow f(v,u) - \Deltaf(v,u)←f(v,u)−Δ

### Termination: integer capacities vs. real capacities

This is a subtle point, and it’s important at difficulty 4.

- •If all capacities are **integers**, and we always augment by the bottleneck Δ\DeltaΔ, then Δ\DeltaΔ is an integer, and the flow value increases by at least 1 each augmentation. Since the max flow value is at most the total capacity leaving sss, the algorithm must terminate.

- •If capacities are **rational**, scaling them by a common denominator reduces to the integer case.

- •If capacities are **real**, naive Ford–Fulkerson can fail to terminate (it can keep making smaller and smaller improvements).

So, for guaranteed polynomial-time behavior, we specify a strategy for picking augmenting paths.

### Edmonds–Karp (a canonical path strategy)

Edmonds–Karp is Ford–Fulkerson where the augmenting path is chosen as the **shortest path in number of edges** in the residual graph (use BFS).

Key facts:

- •It always terminates.
- •Running time is O(VE2)O(VE^2)O(VE2).

Even if you don’t memorize the proof, the intuition is useful:

- •Shortest augmenting paths tend not to “thrash” back and forth.
- •Distances (layer levels) from sss in the residual graph can only increase a bounded number of times before edges become permanently saturated in a way that prevents them from reappearing on short paths.

### Complexity comparison table

| Approach | How augmenting path is chosen | Termination guarantee | Typical bound |
| --- | --- | --- | --- |
| Ford–Fulkerson (generic) | Any augmenting path | Yes for integer/rational capacities; not guaranteed for arbitrary reals | $O(E \cdot | f^\* | )$ augmentations in integer case (pseudo-polynomial) |
| Edmonds–Karp | BFS shortest (#edges) | Yes | O(VE2)O(VE^2)O(VE2) |
| Dinic (preview) | Level graph + blocking flow | Yes | O(EV2)O(EV^2)O(EV2) general; faster in special cases |

### A careful note about representation

When implementing, you almost always store:

- •adjacency list of residual edges
- •current residual capacities
- •pointers to reverse edges (so updates are O(1)O(1)O(1))

Even if the original graph has only forward edges, the residual graph will contain backward edges during the run.

### Integrality (why flows are often integers)

If all capacities are integers, maximum flow has an optimal solution with integer flows.

Reason (informal but accurate):

- •With Edmonds–Karp, each augmentation pushes an integer bottleneck
- •Starting at 0, all flows remain integers

This is extremely powerful: it turns many “counting” problems into flow problems (matchings, disjoint paths, bipartite assignment variants).

## Application/Connection: Max-Flow Min-Cut Theorem (and How the Cut Appears from the Residual Graph)

### Why the theorem matters

Ford–Fulkerson gives you *a* flow. But how do you know it’s optimal?

Max-Flow Min-Cut gives a crisp certificate:

- •A flow value can never exceed the capacity of any cut.
- •When the algorithm stops, we can build a cut whose capacity equals the current flow value.

So you get both:

- •an optimal value
- •a proof of optimality (the min cut)

### Step 1: Any flow is bounded by any cut

Take any feasible flow fff and any cut (S,T)(S,T)(S,T).

Consider net flow leaving SSS:

∑u∈S,v∈Vf(u,v)−∑u∈V,v∈Sf(u,v).\sum\_{u \in S, v \in V} f(u,v) - \sum\_{u \in V, v \in S} f(u,v).u∈S,v∈V∑​f(u,v)−u∈V,v∈S∑​f(u,v).

Because every vertex in SSS except possibly sss has flow conservation, all internal cancellations happen, and the expression collapses to ∣f∣|f|∣f∣ (the only net source inside SSS is sss).

More directly, one can show:

∣f∣=∑u∈S,v∈Tf(u,v)−∑u∈T,v∈Sf(u,v).|f| = \sum\_{u \in S, v \in T} f(u,v) - \sum\_{u \in T, v \in S} f(u,v).∣f∣=u∈S,v∈T∑​f(u,v)−u∈T,v∈S∑​f(u,v).

Now use bounds:

- •f(u,v)≤c(u,v)f(u,v) \le c(u,v)f(u,v)≤c(u,v) on edges from SSS to TTT
- •f(u,v)≥0f(u,v) \ge 0f(u,v)≥0 on edges from TTT to SSS

So:

∣f∣≤∑u∈S,v∈Tc(u,v)=c(S,T).|f| \le \sum\_{u \in S, v \in T} c(u,v) = c(S,T).∣f∣≤u∈S,v∈T∑​c(u,v)=c(S,T).

This implies:

∣f∣≤min⁡(S,T)c(S,T).|f| \le \min\_{(S,T)} c(S,T).∣f∣≤(S,T)min​c(S,T).

So the max flow is always ≤ min cut capacity.

### Step 2: When no augmenting path exists, a cut “falls out”

Assume Ford–Fulkerson has stopped: there is **no** s→ts \to ts→t path in residual graph GfG\_fGf​.

Let SSS be the set of vertices reachable from sss in GfG\_fGf​ (including sss). Let T=V∖ST = V \setminus ST=V∖S.

Because ttt is not reachable, we have t∈Tt \in Tt∈T. Thus (S,T)(S,T)(S,T) is a valid cut.

Now consider any original edge (u,v)(u,v)(u,v) with u∈Su \in Su∈S and v∈Tv \in Tv∈T.

Claim: this edge must be **saturated**:

f(u,v)=c(u,v).f(u,v) = c(u,v).f(u,v)=c(u,v).

Why? If it were not saturated, then forward residual capacity would be positive:

cf(u,v)=c(u,v)−f(u,v)>0,c\_f(u,v) = c(u,v) - f(u,v) > 0,cf​(u,v)=c(u,v)−f(u,v)>0,

meaning (u,v)(u,v)(u,v) would appear in GfG\_fGf​, and then vvv would be reachable from uuu (and from sss), contradicting v∈Tv \in Tv∈T.

So every edge from SSS to TTT is saturated.

Also consider any original edge (v,u)(v,u)(v,u) from TTT to SSS (opposite direction). Claim: it must carry **zero** flow:

f(v,u)=0.f(v,u) = 0.f(v,u)=0.

Why? If f(v,u)>0f(v,u) > 0f(v,u)>0, then the backward residual edge (u,v)(u,v)(u,v) would have positive residual capacity cf(u,v)=f(v,u)c\_f(u,v)=f(v,u)cf​(u,v)=f(v,u), making vvv reachable from uuu and hence from sss, again contradicting v∈Tv \in Tv∈T.

### Step 3: The cut capacity equals the flow value

Compute ∣f∣|f|∣f∣ using the cut identity:

∣f∣=∑u∈S,v∈Tf(u,v)−∑u∈T,v∈Sf(u,v).|f| = \sum\_{u \in S, v \in T} f(u,v) - \sum\_{u \in T, v \in S} f(u,v).∣f∣=u∈S,v∈T∑​f(u,v)−u∈T,v∈S∑​f(u,v).

But we just established:

- •for S→TS \to TS→T edges: f(u,v)=c(u,v)f(u,v)=c(u,v)f(u,v)=c(u,v)
- •for T→ST \to ST→S edges: f(u,v)=0f(u,v)=0f(u,v)=0

So:

∣f∣=∑u∈S,v∈Tc(u,v)=c(S,T).|f| = \sum\_{u \in S, v \in T} c(u,v) = c(S,T).∣f∣=u∈S,v∈T∑​c(u,v)=c(S,T).

Thus the current flow equals the capacity of this cut.

Combine with Step 1:

- •∣f∣≤min⁡c(S,T)|f| \le \min c(S,T)∣f∣≤minc(S,T) for any flow
- •we found a cut with c(S,T)=∣f∣c(S,T) = |f|c(S,T)=∣f∣

Therefore fff is maximum and (S,T)(S,T)(S,T) is a minimum cut:

max⁡f∣f∣=min⁡(S,T)c(S,T).\max\_f |f| = \min\_{(S,T)} c(S,T).fmax​∣f∣=(S,T)min​c(S,T).

### Diagram 2: Reachable set S vs T defines the min cut (static SVG)

This diagram shows a residual graph situation at termination: vertices reachable from sss are shaded as SSS; ttt is in TTT. All edges from SSS to TTT are saturated (no forward residual capacity), so there is no crossing residual edge.

```
<svg xmlns="http://www.w3.org/2000/svg" width="880" height="320" viewBox="0 0 880 320" role="img" aria-label="Cut from reachable set in residual network: S is reachable from s, T contains t, and edges from S to T are saturated">
  <defs>
    <marker id="arr" markerWidth="10" markerHeight="10" refX="10" refY="3" orient="auto" markerUnits="strokeWidth">
      <path d="M0,0 L10,3 L0,6 Z" fill="#222" />
    </marker>
  </defs>

  <!-- Background regions -->
  <rect x="20" y="40" width="400" height="250" fill="#e8f4ff" stroke="#1f77b4" stroke-width="2"/>
  <rect x="460" y="40" width="400" height="250" fill="#fff0f0" stroke="#d62728" stroke-width="2"/>
  <text x="220" y="30" text-anchor="middle" font-family="sans-serif" font-size="16" fill="#1f77b4">S (reachable from s in residual)</text>
  <text x="660" y="30" text-anchor="middle" font-family="sans-serif" font-size="16" fill="#d62728">T (not reachable)</text>

  <!-- Nodes in S -->
  <circle cx="120" cy="110" r="22" fill="#fff" stroke="#222" stroke-width="2"/>
  <text x="120" y="116" text-anchor="middle" font-family="sans-serif" font-size="14">s</text>

  <circle cx="240" cy="110" r="22" fill="#fff" stroke="#222" stroke-width="2"/>
  <text x="240" y="116" text-anchor="middle" font-family="sans-serif" font-size="14">a</text>

  <circle cx="180" cy="210" r="22" fill="#fff" stroke="#222" stroke-width="2"/>
  <text x="180" y="216" text-anchor="middle" font-family="sans-serif" font-size="14">b</text>

  <!-- Nodes in T -->
  <circle cx="600" cy="110" r="22" fill="#fff" stroke="#222" stroke-width="2"/>
  <text x="600" y="116" text-anchor="middle" font-family="sans-serif" font-size="14">c</text>

  <circle cx="720" cy="210" r="22" fill="#fff" stroke="#222" stroke-width="2"/>
  <text x="720" y="216" text-anchor="middle" font-family="sans-serif" font-size="14">t</text>

  <!-- Residual edges inside S (reachable) -->
  <line x1="142" y1="110" x2="218" y2="110" stroke="#222" stroke-width="2.5" marker-end="url(#arr)"/>
  <text x="180" y="96" text-anchor="middle" font-family="sans-serif" font-size="12">residual&gt;0</text>

  <line x1="130" y1="126" x2="170" y2="190" stroke="#222" stroke-width="2.5" marker-end="url(#arr)"/>

  <line x1="220" y1="126" x2="195" y2="188" stroke="#222" stroke-width="2.5" marker-end="url(#arr)"/>

  <!-- Original edges from S to T are saturated => show as dashed and labeled saturated -->
  <line x1="262" y1="110" x2="578" y2="110" stroke="#222" stroke-width="3" stroke-dasharray="6,6" marker-end="url(#arr)"/>
  <text x="420" y="100" text-anchor="middle" font-family="sans-serif" font-size="12">S→T edge saturated (no residual)</text>

  <line x1="202" y1="210" x2="705" y2="210" stroke="#222" stroke-width="3" stroke-dasharray="6,6" marker-end="url(#arr)"/>
  <text x="455" y="200" text-anchor="middle" font-family="sans-serif" font-size="12">S→T edge saturated (no residual)</text>

  <!-- Edges inside T (may exist, but unreachable from s) -->
  <line x1="620" y1="126" x2="705" y2="194" stroke="#222" stroke-width="2" marker-end="url(#arr)"/>
  <text x="690" y="150" text-anchor="middle" font-family="sans-serif" font-size="12">(unreached)</text>

  <!-- Label: cut boundary -->
  <text x="440" y="285" text-anchor="middle" font-family="sans-serif" font-size="14">Cut boundary between S and T</text>
</svg>
```

### Practical payoff: you get a minimum cut for free

From the final residual graph you can extract:

- •SSS = reachable from sss via residual edges
- •the min-cut edges are exactly original edges (u,v)(u,v)(u,v) with u∈Su \in Su∈S, v∈Tv \in Tv∈T

This is extremely useful in applications (segmentation, clustering, reliability, identifying bottlenecks) because the min cut provides interpretability: “here are the edges that truly limit throughput.”

## Worked Examples (3)

### Example 1: Run Ford–Fulkerson with residual backward edges (rerouting happens)

Consider a flow network with vertices {s, a, b, t} and capacities:

- •c(s,a)=3, c(s,b)=2
- •c(a,b)=2
- •c(a,t)=2
- •c(b,t)=3

We will run Ford–Fulkerson and explicitly observe a backward residual edge enabling rerouting. Start with f=0 everywhere.

1. Step 1: Start with zero flow.

   All residual capacities equal original capacities.

   |f|=0.
2. Step 2: Choose augmenting path P₁: s → a → b → t.

   Residual capacities along edges:

   - •c\_f(s,a)=3
   - •c\_f(a,b)=2
   - •c\_f(b,t)=3

   Bottleneck Δ₁ = min(3,2,3)=2.

   Augment by 2:

   - •f(s,a)=2
   - •f(a,b)=2
   - •f(b,t)=2

   Now |f|=2.
3. Step 3: Build residual edges after augmentation.

   Forward residuals:

   - •c\_f(s,a)=3-2=1
   - •c\_f(a,b)=2-2=0 (saturated)
   - •c\_f(b,t)=3-2=1

   Also backward residuals appear where flow>0:

   - •c\_f(a,s)=f(s,a)=2
   - •c\_f(b,a)=f(a,b)=2
   - •c\_f(t,b)=f(b,t)=2
4. Step 4: If we try path s → a → t, it exists in residual.

   Residual capacities:

   - •c\_f(s,a)=1
   - •c\_f(a,t)=2

   So Δ₂ = 1.

   Augment by 1:

   - •f(s,a)=3
   - •f(a,t)=1

   Now |f|=3.

   (Flow conservation at a: in=3, out=2 to b +1 to t =3.)
5. Step 5: We still have capacity from s to b: c\_f(s,b)=2.

   Try path P₃: s → b → t.

   Residuals:

   - •c\_f(s,b)=2
   - •c\_f(b,t)=1

   So Δ₃=1.

   Augment:

   - •f(s,b)=1
   - •f(b,t)=3

   Now |f|=4.

   (b→t is now saturated.)
6. Step 6: Can we push more? We’d like to use s→b (still has residual 1) but b→t is full.

   Look for an augmenting path that uses a backward edge.

   Consider residual path P₄: s → b → a → t.

   Check each residual edge:

   - •s→b has c\_f=2-1=1 (forward)
   - •b→a exists as a backward residual edge with capacity c\_f(b,a)=f(a,b)=2
   - •a→t has forward residual c\_f(a,t)=2-1=1

   So P₄ is valid and Δ₄=min(1,2,1)=1.
7. Step 7: Augment along P₄ by 1.

   Edge updates:

   - •On s→b (forward): f(s,b)=1+1=2
   - •On b→a (backward): this decreases f(a,b): f(a,b)=2-1=1
   - •On a→t (forward): f(a,t)=1+1=2

   Now |f|=5.
8. Step 8: Verify feasibility and interpret rerouting.

   At vertex b:

   - •inflow from s is 2
   - •outflow to t is 3 and to a is (none in original, but the residual step reduced a→b flow, effectively freeing b)

   More systematically via original edges:

   - •b receives f(s,b)=2 and f(a,b)=1, total 3
   - •b sends f(b,t)=3

   So conservation holds.

   At vertex a:

   - •a receives f(s,a)=3
   - •a sends f(a,b)=1 and f(a,t)=2, total 3

   So conservation holds.
9. Step 9: Argue optimality quickly via cut.

   Consider cut S={s,a,b}, T={t}.

   Cut capacity is c(a,t)+c(b,t)=2+3=5.

   We have found a flow of value 5, so it must be maximum.

**Insight:** Backward residual edges are not a technicality; they encode “undoing” earlier routing choices. In this example, the augmenting path s→b→a→t used the backward edge b→a to reduce flow on a→b, freeing capacity so more could reach t through a→t even though b→t was already saturated.

### Example 2: Extract the min cut from the final residual graph

Use the same network and the final maximum flow from Example 1 (value 5). We will construct the residual graph and compute the reachable set S from s, then read off the minimum cut (S,T).

1. Step 1: Record final flows from Example 1:

   - •f(s,a)=3 (saturated)
   - •f(s,b)=2 (saturated)
   - •f(a,b)=1 (not saturated)
   - •f(a,t)=2 (saturated)
   - •f(b,t)=3 (saturated)

   Flow value |f|=5.
2. Step 2: Compute residual capacities for each original edge.

   For each edge (u,v): c\_f(u,v)=c(u,v)-f(u,v).

   - •c\_f(s,a)=3-3=0
   - •c\_f(s,b)=2-2=0
   - •c\_f(a,b)=2-1=1
   - •c\_f(a,t)=2-2=0
   - •c\_f(b,t)=3-3=0
3. Step 3: Add backward residual edges where f(u,v)>0 with capacity f(u,v).

   - •residual a→s with cap 3
   - •residual b→s with cap 2
   - •residual b→a with cap 1
   - •residual t→a with cap 2
   - •residual t→b with cap 3
4. Step 4: Determine which vertices are reachable from s in the residual graph.

   From s, there are no outgoing residual edges (both s→a and s→b have residual 0).

   So the reachable set is S={s}.

   Thus T={a,b,t}.
5. Step 5: Compute cut capacity c(S,T).

   Edges from S to T are edges leaving s:

   - •c(s,a)=3
   - •c(s,b)=2

   So c(S,T)=3+2=5.
6. Step 6: Conclude minimum cut.

   We already have |f|=5, and we found a cut with capacity 5.

   So (S,T)=({s},{a,b,t}) is a minimum cut and f is a maximum flow.

**Insight:** At optimality, the residual graph can “strand” the source: if s has no outgoing residual edges, then S={s} immediately yields a min cut consisting of the saturated edges leaving s. More generally, S is the set reachable from s; edges crossing S→T are exactly the saturated bottleneck edges defining the min cut.

### Example 3: Max flow as an LP and the cut as its dual (conceptual bridge)

You already know linear programming and simplex. Here we sketch the primal/dual relationship that mirrors max-flow/min-cut. This is not a full dual derivation, but enough to connect the theorem to LP duality intuition.

1. Step 1: Write max flow (primal) as an LP.

   Variables f(u,v) for each edge.

   Maximize |f|, which can be written as maximize ∑\_v f(s,v) - ∑\_v f(v,s).

   Subject to:

   - •0 ≤ f(u,v) ≤ c(u,v)
   - •For all v≠s,t: ∑\_u f(u,v) = ∑\_w f(v,w).
2. Step 2: Interpret conservation constraints as “no net creation” at intermediate vertices.

   Only s can create net +|f| and t can absorb it.
3. Step 3: Dual intuition: assign potentials/labels that separate s from t.

   A cut can be represented by an indicator x\_v ∈ {0,1} with x\_s=0, x\_t=1, where S={v: x\_v=0}.

   Then edges crossing S→T are those with x\_u=0, x\_v=1.
4. Step 4: The min-cut objective ∑\_{(u,v)} c(u,v)·[x\_u=0, x\_v=1] mirrors a dual objective.

   Relaxing x\_v to [0,1] and using constraints like y\_{uv} ≥ x\_v - x\_u creates a linear program whose optimum equals max flow (strong duality).
5. Step 5: Connect to theorem.

   The fact that max flow equals min cut is an instance of strong duality specialized to a network matrix, but Ford–Fulkerson gives a purely graph-theoretic constructive proof and produces the dual certificate (the cut) from residual reachability.

**Insight:** Max-flow/min-cut is not a coincidence: a cut is a dual witness that upper-bounds every feasible flow. The residual-graph stopping condition is the combinatorial analogue of complementary slackness: crossing edges are saturated (tight), and no residual path remains to improve the primal.

## Key Takeaways

- ✓

  A feasible sss–ttt flow satisfies capacity bounds $0 \le f(u,v) \le c(u,v)andflowconservationatallverticesexcept and flow conservation at all vertices except andflowconservationatallverticesexceptsand and andt$.
- ✓

  The residual network GfG\_fGf​ contains edges with positive residual capacity, including backward edges with capacity equal to the current flow (allowing cancellation).
- ✓

  An augmenting path is an s→ts \to ts→t path in GfG\_fGf​; augmenting by the bottleneck Δ\DeltaΔ increases the flow value by exactly Δ\DeltaΔ while preserving feasibility.
- ✓

  Ford–Fulkerson repeats augmentation until no augmenting path exists; with integer capacities it terminates (and yields an integer max flow).
- ✓

  Edmonds–Karp (BFS shortest augmenting paths) guarantees polynomial time: O(VE2)O(VE^2)O(VE2).
- ✓

  For any cut (S,T)(S,T)(S,T), every feasible flow satisfies ∣f∣≤c(S,T)|f| \le c(S,T)∣f∣≤c(S,T) (cuts upper-bound flows).
- ✓

  When no augmenting path exists, letting S be vertices reachable from s in the residual graph produces a cut with capacity equal to the current flow value.
- ✓

  Therefore, maximum flow equals minimum cut capacity: max⁡f∣f∣=min⁡(S,T)c(S,T)\max\_f |f| = \min\_{(S,T)} c(S,T)maxf​∣f∣=min(S,T)​c(S,T).

## Common Mistakes

- ✗

  Forgetting backward residual edges (or giving them the wrong capacity): the correct backward residual capacity is exactly the current flow on the forward edge.
- ✗

  Updating flows incorrectly on backward edges during augmentation (you must subtract Δ\DeltaΔ from the corresponding original forward flow).
- ✗

  Computing cut capacity using edges in both directions; cut capacity is only the sum of capacities of edges directed from S to T.
- ✗

  Assuming generic Ford–Fulkerson always terminates quickly; without a path selection rule it can be pseudo-polynomial (or non-terminating with irrational capacities).

## Practice

easy

Given a network with edges and capacities: c(s,a)=4, c(s,b)=2, c(a,b)=1, c(a,t)=2, c(b,t)=3. Start with zero flow. Perform two Ford–Fulkerson augmentations of your choice and write the resulting flow values on each edge.

**Hint:** Pick an s→t path, compute the bottleneck residual capacity, augment, then rebuild residual capacities before the second augmentation.

Show solution

One possible sequence:

1) Path s→a→t has bottleneck min(4,2)=2. Augment: f(s,a)=2, f(a,t)=2. |f|=2.

2) Residuals now: c\_f(s,a)=2, c\_f(a,t)=0. Pick path s→b→t with bottleneck min(2,3)=2. Augment: f(s,b)=2, f(b,t)=2. |f|=4.

Resulting nonzero flows: f(s,a)=2, f(a,t)=2, f(s,b)=2, f(b,t)=2. (Other edges 0.)

medium

Let f be a feasible flow and (S,T) be any s–t cut. Prove (by algebra using conservation) that ∣f∣=∑u∈S,v∈Tf(u,v)−∑u∈T,v∈Sf(u,v)|f| = \sum\_{u \in S, v \in T} f(u,v) - \sum\_{u \in T, v \in S} f(u,v)∣f∣=∑u∈S,v∈T​f(u,v)−∑u∈T,v∈S​f(u,v).

**Hint:** Sum flow conservation equations over all vertices in S\{s}. The internal edges cancel; only boundary terms and source terms remain.

Show solution

Consider net outflow from S:

N(S)=∑\_{u∈S, v∈V} f(u,v) − ∑\_{u∈V, v∈S} f(u,v).

Split sums into internal (S→S), outgoing (S→T), incoming (T→S).

Internal terms cancel because they appear once with + and once with −.

So N(S)=∑\_{u∈S, v∈T} f(u,v) − ∑\_{u∈T, v∈S} f(u,v).

Now use conservation: for every vertex in S except s, net outflow is 0. Therefore N(S) equals net outflow of s, which is exactly |f|. Hence the identity holds.

hard

At termination (no augmenting path), define S as the set of vertices reachable from s in the residual graph. Prove that every original edge (u,v) with u∈S and v∈T is saturated: f(u,v)=c(u,v).

**Hint:** Argue by contradiction: if f(u,v)<c(u,v), then the forward residual capacity is positive and (u,v) would be a residual edge.

Show solution

Suppose there exists an edge (u,v) with u∈S, v∈T, and f(u,v)<c(u,v). Then c\_f(u,v)=c(u,v)−f(u,v)>0, so (u,v) is an edge in the residual graph. Since u is reachable from s and (u,v) is a residual edge, v would be reachable from s as well, contradicting v∈T=V\S. Therefore no such edge exists, and every edge crossing S→T must satisfy f(u,v)=c(u,v).

## Connections

Prerequisites you can lean on:

- •[Shortest Paths](/tech-tree/shortest-paths/): Edmonds–Karp uses BFS on the residual graph; many intuitions (reachability layers, augmenting along paths) mirror shortest-path thinking.
- •[Linear Programming](/tech-tree/linear-programming/): max-flow is an LP; min-cut is its dual witness in spirit, and the theorem reflects strong duality.

Common next steps (typical unlocks after this node):

- •[Bipartite Matching via Max Flow](/tech-tree/bipartite-matching/)
- •[Min-Cost Max-Flow](/tech-tree/min-cost-flow/)
- •[Dinic’s Algorithm](/tech-tree/dinic/)
- •[Flow with Lower Bounds](/tech-tree/flow-lower-bounds/)

Quality: A (4.4/5)

[← back to tree](/tech-tree/)[browse all →](/tech-tree/inventory/)
