---
title: Topological Sort
description: Linear ordering of DAG vertices. Dependencies come before dependents.
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
permalink: /tech-tree/topological-sort/
---

[←Back to Tech Tree](/tech-tree/)

[inventory](/tech-tree/inventory/)[coverage](/tech-tree/coverage/)

# Topological Sort

Graph TheoryDifficulty: ★★★☆☆Depth: 4Unlocks: 2

Linear ordering of DAG vertices. Dependencies come before dependents.

## Interactive Visualization

⏮◀◀▶▶STEP0.25x1xZOOM

t=0s

## Core Concepts

- -Directed Acyclic Graph (DAG): a directed graph that contains no directed cycles
- -Topological ordering: a linear sequence of all vertices in which every directed edge's source precedes its target

## Key Symbols & Notation

ASCII 'u -> v' to denote a directed edge from vertex u to vertex v

## Essential Relationships

- -For every directed edge 'u -> v', u must come before v in any topological ordering
- -A directed graph admits a topological ordering if and only if it is acyclic (has no directed cycles)

## Prerequisites (1)

[Graph Traversal5 atoms](/tech-tree/graph-traversal/)

## Unlocks (2)

[Causal Inferencelvl 5](/tech-tree/causal-inference/)[Task Discretizationlvl 5](/tech-tree/task-discretization/)

## Referenced by (3)

Where this concept shows up in the operating-finance and personal-finance graphs.

### From Business (3)

[ObsolescenceBusiness

Obsolescence cascades through dependency graphs - a single breaking API change forces upgrades in topological order through all downstream dependents, and understanding DAG ordering is essential to grasping why version churn compounds](/business/obsolescence/)[investment sequencingBusiness

Investment dependencies form a DAG - you cannot train a workforce on a system not yet built, cannot ship a cost program before the enabling infrastructure exists. Topological sort is the exact structure: order nodes so dependencies precede dependents](/business/investment-sequencing/)[critical pathBusiness

Critical path algorithm processes DAG nodes in topological order to compute earliest/latest start times; topological sort is the direct prerequisite that makes the linear-time longest-path computation possible](/business/critical-path/)

Advanced Learning Details

### Graph Position

38

Depth Cost

2

Fan-Out (ROI)

2

Bottleneck Score

4

Chain Length

### Cognitive Load

5

Atomic Elements

28

Total Elements

L1

Percentile Level

L3

Atomic Level

### All Concepts (11)

- - Topological ordering: a linear ordering of the vertices of a directed graph that respects edge directions
- - Directed Acyclic Graph (DAG): a directed graph that contains no directed cycles
- - In-degree of a vertex: the count of incoming edges to that vertex
- - Zero in-degree vertex (source): a vertex with in-degree zero usable as a next element in a topological order
- - Source and sink vertices terminology (source: no incoming edges; sink: no outgoing edges)
- - Topological sort as a linear extension of a partial order induced by the DAG
- - Kahn's algorithm: iterative removal of zero in-degree vertices to build a topological order
- - DFS-based topological sort: using reverse postorder (finishing-time order) from DFS to obtain a topological order
- - Cycle detection via topological sort (topological order exists iff no directed cycle)
- - Multiplicity and uniqueness of topological orders (there may be many valid orders; conditions for uniqueness)
- - Representation of a topological order as a position map (an assignment of each vertex to a position in a sequence)

### Teaching Strategy

Self-serve tutorial - low prerequisites, straightforward concepts.

When a project has dependencies—"compile before link", "foundation before walls", "parents before children"—you’re really asking for a linear order that respects directed constraints. Topological sort is the standard way to produce that order, as long as your dependency graph has no cycles.

TL;DR:

A topological sort of a directed graph is a linear ordering of vertices such that for every edge u -> v, u appears before v. It exists iff the graph is a DAG. Two classic algorithms are: (1) Kahn’s algorithm (repeatedly remove indegree-0 nodes) and (2) DFS postorder (reverse finishing times). If you can’t find an indegree-0 node (or DFS finds a back edge), you’ve detected a cycle—meaning no valid dependency order exists.

## What Is Topological Sort?

### Why you need it

Many real problems are phrased as **dependencies**:

- •Course planning: “take Calculus I before Calculus II”
- •Build systems: “compile files before linking”
- •Data pipelines: “clean data before training”
- •Causal graphs: “causes precede effects”

A dependency is naturally modeled as a **directed edge**.

- •Write **u -> v** to mean: “u must happen before v” (u is a prerequisite of v).

If you want to *execute* everything, you need a **single sequence** of all tasks that respects every edge.

That is exactly what topological sorting provides.

---

### Definition (with intuition)

Let G = (V, E) be a directed graph.

A **topological ordering** of G is a linear ordering of all vertices:

v₁, v₂, …, vₙ

such that for every directed edge **u -> v** in E, **u** appears **before** **v** in the ordering.

A **topological sort** is an algorithm that returns such an ordering.

**Key intuition:** edges point “forward in time.” Topological order is a timeline that never violates an arrow.

---

### The DAG requirement: why cycles break everything

A topological ordering exists **if and only if** the graph is a **DAG** (Directed Acyclic Graph).

- •If there is a directed cycle:
- •A -> B -> C -> A

then A must come before B, B before C, and C before A. That last constraint contradicts the first two. No linear order can satisfy all.

- •If the graph is acyclic, you can always find at least one “starting” node with no prerequisites, place it first, remove it, and repeat.

This “starting node exists” fact is not just intuitive—it’s the engine behind Kahn’s algorithm.

---

### Not unique—and that’s a feature

Topological orderings are often **not unique**.

Example:

- •Edges: A -> C, B -> C

Both A and B must precede C, but A and B can be swapped:

- •A, B, C
- •B, A, C

This reflects reality: when tasks are independent, you have scheduling freedom.

---

### What topological sort does *not* guarantee

Topological sort ensures **validity** (dependency constraints), not:

- •minimal total time (that’s scheduling with durations and resources)
- •minimal number of steps (that’s different)
- •uniqueness

Think of it as producing a feasible plan, not necessarily the optimal one.

## Core Mechanic 1: Kahn’s Algorithm (Indegree / “Peel Off Sources”)

### Why this approach works

If the graph is a DAG, there must be at least one vertex with **indegree 0** (no incoming edges). Call these vertices **sources**.

Why must a source exist?

- •Suppose (for contradiction) every vertex has indegree ≥ 1.
- •Pick any vertex v₀. Since indegree ≥ 1, there exists v₁ with v₁ -> v₀.
- •Similarly, there exists v₂ with v₂ -> v₁, and so on.
- •Because the graph is finite, some vertex repeats, creating a directed cycle.
- •That contradicts acyclicity.

So in a DAG, at least one source exists. If you output a source first, you can safely remove it and continue. This yields a valid ordering.

---

### Algorithm idea

Maintain:

- •indegree[v] = number of incoming edges to v
- •a queue (or stack) of all vertices with indegree 0

Repeatedly:

1. 1)pop a vertex u with indegree 0
2. 2)output u
3. 3)for each edge u -> v:

- •decrement indegree[v]
- •if indegree[v] becomes 0, push v

At the end:

- •if you output all vertices, success: you have a topological order
- •otherwise, the remaining vertices are in (or depend on) a directed cycle → no topo order exists

---

### Walkthrough with a concrete graph

Consider tasks:

- •A -> D
- •B -> D
- •C -> E
- •D -> F
- •E -> F

Compute indegrees:

- •indegree[A]=0, indegree[B]=0, indegree[C]=0
- •indegree[D]=2 (A,B)
- •indegree[E]=1 (C)
- •indegree[F]=2 (D,E)

Initialize queue with A,B,C.

One possible run:

- •pop A → output A → D indegree: 2→1
- •pop B → output B → D indegree: 1→0 (push D)
- •pop C → output C → E indegree: 1→0 (push E)
- •pop D → output D → F indegree: 2→1
- •pop E → output E → F indegree: 1→0 (push F)
- •pop F → output F

Result: A, B, C, D, E, F

Another valid result might start with C, then A, etc. Kahn’s algorithm naturally allows multiple answers depending on how you choose among indegree-0 nodes.

---

### Complexity and data structures

Let n = |V|, m = |E|.

- •Computing indegrees: O(m)
- •Each vertex enters/leaves the queue once: O(n)
- •Each edge processed once when its source is output: O(m)

Total: **O(n + m)** time and **O(n + m)** space (for adjacency list, indegrees, queue).

---

### Cycle detection with Kahn’s algorithm

If there is a directed cycle, no vertex in that cycle can ever reach indegree 0 (within the subgraph induced by remaining vertices). So the queue empties early.

A reliable check:

- •If output\_count < n ⇒ cycle exists ⇒ no topological ordering.

This is a practical benefit: Kahn’s algorithm is both a sorter and a cycle detector.

---

### Queue vs stack vs priority queue

The container for indegree-0 vertices affects which valid ordering you get.

| Structure | What you get | Typical use |
| --- | --- | --- |
| Queue (FIFO) | “Earlier discovered first” | simple scheduling |
| Stack (LIFO) | tends to go deep | sometimes convenient |
| Priority queue | smallest label first | deterministic / canonical-ish order |

All produce valid topological orders as long as you always remove a vertex with indegree 0.

## Core Mechanic 2: DFS Finishing Times (Reverse Postorder)

### Why DFS can produce a valid ordering

You already know DFS as a traversal. For topological sort, the key observation is about **finishing time**.

During DFS, a node u “finishes” after exploring all outgoing edges u -> v and fully finishing those descendants v.

In a DAG, if there is an edge u -> v, then v must finish before u finishes (because DFS from u will (directly or indirectly) reach v, or v is explored in another DFS tree but still cannot create a back edge in a DAG).

So if we list nodes in **decreasing finishing time**, u will appear before v whenever u -> v.

That ordering is exactly a topological ordering.

---

### The actual recipe

1. 1)Run DFS on the directed graph (starting from every unvisited vertex to cover disconnected parts).
2. 2)When a vertex u finishes, append it to a list (often called `order`).
3. 3)Reverse `order` at the end.

Equivalently: push u onto a stack at finish-time; popping the stack yields topo order.

---

### Cycle detection via DFS colors (why it matters)

DFS-based topo sort is typically paired with cycle detection using a 3-state visitation scheme:

- •WHITE: unvisited
- •GRAY: in current recursion stack (actively exploring)
- •BLACK: finished

When exploring an edge u -> v:

- •if v is WHITE: recurse
- •if v is GRAY: you found a **back edge**, which implies a directed cycle ⇒ no topo order
- •if v is BLACK: ignore (already finished)

This is conceptually clean: a back edge means “u depends on something currently depending on u,” which is exactly the cycle contradiction.

---

### Example (showing finishing order)

Edges:

- •1 -> 2
- •1 -> 3
- •3 -> 4

One DFS run:

- •start 1
- •go 2 (finish 2)
- •go 3
- •go 4 (finish 4)
- •finish 3
- •finish 1

Finish sequence (append at finish): [2, 4, 3, 1]

Reverse: [1, 3, 4, 2]

Check constraints:

- •1 before 2 ✓
- •1 before 3 ✓
- •3 before 4 ✓

---

### Complexity

Same as Kahn’s algorithm:

- •DFS visits each vertex once, each edge once ⇒ **O(n + m)**
- •space: O(n + m) for adjacency plus O(n) recursion stack (or explicit stack)

---

### Kahn vs DFS: when to choose which

| Aspect | Kahn’s algorithm | DFS reverse postorder |
| --- | --- | --- |
| Main concept | indegree-0 “available tasks” | finishing times / recursion |
| Cycle detection | output\_count < n | detect back edges (GRAY→GRAY) |
| Produces order incrementally | yes (streaming) | order known after DFS completion |
| Good for scheduling/queues | excellent | okay |
| Implementation pitfalls | careful indegree updates | recursion depth / color logic |

If you’re thinking in terms of “what can I do next?”, Kahn’s algorithm matches that mental model.

If you’re already in DFS mode, reverse postorder is elegant and short.

## Applications and Connections (Why Topological Sort Keeps Showing Up)

### 1) Dependency resolution (build systems, packages, compilation)

Nodes are artifacts; edges encode prerequisites.

- •file.c -> file.o (compile)
- •file.o -> program.exe (link)

A topological order is a valid build order.

If a cycle exists (A depends on B depends on A), your build system should fail with a helpful cycle report.

---

### 2) Course planning / curriculum graphs

Nodes are courses; edges are prerequisites.

Topological sorting provides a feasible sequence of courses.

Often you also have constraints like “at most 4 courses per term.” Topological sort is still the backbone, but then you add batching/leveling (a scheduling layer).

---

### 3) Pipeline orchestration (ETL, ML training)

Data and model workflows are DAGs:

- •raw\_data -> cleaned\_data -> features -> model\_train -> model\_eval

Orchestrators (Airflow, Dagster, Prefect) effectively maintain the set of indegree-0 tasks that are ready to run—Kahn’s idea with extra machinery (retries, resources, time).

---

### 4) Dynamic programming on DAGs

A powerful pattern:

1. 1)Topologically sort vertices.
2. 2)Process vertices in that order to compute DP values.

Why it works: when you process v, all prerequisites u with u -> v have already been processed.

Example: longest path in a DAG.

Let dp[v] = length of longest path ending at v.

Then

- •dp[v] = max over (u -> v) of (dp[u] + 1)

Processing in topological order ensures dp[u] is ready when computing dp[v].

---

### 5) Causal graphs and “cause before effect”

In causal inference, DAGs represent directional assumptions (potential causal influence).

Topological ordering is not the full causal story, but it reinforces the key constraint: if u is a cause of v (directly or indirectly), u cannot come after v in a causal ordering.

---

### 6) From partial orders to linear extensions

A DAG defines a **partial order**: u ≤ v if there is a directed path u → … → v.

A topological ordering is a **linear extension** of that partial order.

This viewpoint helps explain non-uniqueness:

- •partial order leaves some pairs incomparable
- •topo sort chooses an arbitrary consistent order among incomparable elements

---

### Practical note: validating an order

Given an ordering pos[·], you can verify it in O(n + m):

- •for every edge u -> v, check pos[u] < pos[v]

This is useful in testing: generate a topo order, then assert it respects all edges.

---

### Summary

Topological sort is a “glue” primitive:

- •it converts a **graph of constraints** into a **timeline**
- •it’s efficient (O(n + m))
- •it naturally detects impossible constraints (cycles)

Once you see dependencies as edges, topo sort becomes the default tool.

## Worked Examples (3)

### Worked Example 1: Kahn’s Algorithm Step-by-Step (Including a Tie)

Vertices: {A, B, C, D, E}

Edges:

A -> D

B -> D

B -> E

C -> E

D -> E

Goal: produce one topological ordering using Kahn’s algorithm.

1. Compute indegrees:

   - •indegree[A] = 0
   - •indegree[B] = 0
   - •indegree[C] = 0
   - •indegree[D] = 2 (A, B)
   - •indegree[E] = 3 (B, C, D)
2. Initialize the set/queue of indegree-0 vertices:

   Q = [A, B, C]

   Output = []
3. Pop A (one of the available sources):

   Output = [A]

   Remove edges out of A:

   - •A -> D so indegree[D]: 2 → 1

   Q now contains [B, C] (D not added because indegree[D] ≠ 0).
4. Pop B:

   Output = [A, B]

   Remove edges out of B:

   - •B -> D so indegree[D]: 1 → 0 (push D)
   - •B -> E so indegree[E]: 3 → 2

   Q becomes [C, D].
5. Pop C:

   Output = [A, B, C]

   Remove edges out of C:

   - •C -> E so indegree[E]: 2 → 1

   Q becomes [D].
6. Pop D:

   Output = [A, B, C, D]

   Remove edges out of D:

   - •D -> E so indegree[E]: 1 → 0 (push E)

   Q becomes [E].
7. Pop E:

   Output = [A, B, C, D, E]

   Done: output\_count = 5 = |V|, so this is a valid topological ordering.

**Insight:** The only rule is: always choose a vertex with indegree 0. The ordering is not unique; different choices among {A, B, C} at the start produce different (still valid) schedules.

### Worked Example 2: Detecting a Cycle (Why No Topological Order Exists)

Vertices: {1, 2, 3, 4}

Edges:

1 -> 2

2 -> 3

3 -> 1

3 -> 4

Try to topologically sort and observe what fails.

1. Compute indegrees:

   - •indegree[1] = 1 (from 3)
   - •indegree[2] = 1 (from 1)
   - •indegree[3] = 1 (from 2)
   - •indegree[4] = 1 (from 3)
2. Initialize indegree-0 set:

   No vertex has indegree 0.

   So Q = [] immediately.
3. Kahn’s algorithm stops with Output = [].

   Since output\_count = 0 < 4, we conclude: a directed cycle exists, so no topological ordering exists.
4. Interpretation:

   The cycle 1 -> 2 -> 3 -> 1 requires 1 before 2 before 3 before 1, which is impossible in a linear order.

   Edge 3 -> 4 additionally forces 3 before 4, but the cycle already makes the constraints inconsistent.

**Insight:** Cycle detection is not an extra feature bolted on—failure to find a new source is exactly the symptom of cyclic dependencies.

### Worked Example 3: DFS Reverse Postorder + Back Edge Detection

Run DFS topo sort on:

Edges:

A -> B

A -> C

C -> D

D -> B

We will compute finishing order and then reverse it.

1. Initialize all vertices WHITE.

   order = []
2. Start DFS at A:

   Mark A GRAY.

   Explore A -> B:

   - •B is WHITE, DFS(B)
   - •Mark B GRAY
   - •B has no outgoing edges (in this example)
   - •Mark B BLACK, append B to order

   order = [B]
3. Back to A, explore A -> C:

   - •C is WHITE, DFS(C)
   - •Mark C GRAY
   - •Explore C -> D:
   - •D is WHITE, DFS(D)
   - •Mark D GRAY
   - •Explore D -> B:
   - •B is BLACK (finished), so no issue
   - •Mark D BLACK, append D

   order = [B, D]

   - •Mark C BLACK, append C

   order = [B, D, C]
4. Finish A:

   Mark A BLACK, append A

   order = [B, D, C, A]
5. Reverse finishing list:

   Topo order = [A, C, D, B]

   Check edges:

   A -> B (A before B) ✓

   A -> C (A before C) ✓

   C -> D (C before D) ✓

   D -> B (D before B) ✓

**Insight:** In a DAG, an edge u -> v implies v finishes before u (in the sense needed for reverse postorder). If DFS ever sees an edge to a GRAY vertex, that’s a back edge and proves a cycle.

## Key Takeaways

- ✓

  Topological ordering is a linear sequence where every edge u -> v has u before v.
- ✓

  A topological ordering exists **iff** the directed graph is a DAG (no directed cycles).
- ✓

  Kahn’s algorithm repeatedly removes indegree-0 vertices; if it can’t remove all vertices, a cycle exists.
- ✓

  DFS-based topo sort outputs vertices in reverse finishing time (reverse postorder); back edges (to GRAY) detect cycles.
- ✓

  Topological sorts are generally not unique; different choices among currently-available nodes yield different valid orders.
- ✓

  Both major algorithms run in O(n + m) time using adjacency lists.
- ✓

  Topo order is a backbone for DAG dynamic programming and real-world dependency scheduling.

## Common Mistakes

- ✗

  Using topological sort on a graph that may contain directed cycles without checking for failure (you must detect/report cycles).
- ✗

  Mixing up edge direction: if u -> v means “u depends on v” vs “u is prerequisite for v,” you’ll reverse the intended order.
- ✗

  Forgetting to decrement indegree for *every* outgoing edge in Kahn’s algorithm (leading to missing nodes).
- ✗

  In DFS topo sort, appending nodes when they are discovered rather than when they finish (you need finishing times).

## Practice

easy

Given edges: A -> C, B -> C, C -> D, B -> E. List **two different** valid topological orderings.

**Hint:** A and B must both come before C; C must come before D; B must come before E. Try starting with A vs starting with B.

Show solution

Two valid orderings are:

1) A, B, C, D, E

2) B, A, E, C, D

Checks:

- •A -> C: A before C ✓
- •B -> C: B before C ✓
- •C -> D: C before D ✓
- •B -> E: B before E ✓

medium

Run Kahn’s algorithm on: 1 -> 3, 2 -> 3, 3 -> 4, 2 -> 5, 5 -> 4. Use a FIFO queue and break ties by smaller number first. Provide the resulting order.

**Hint:** Compute indegrees first. Initialize Q with all indegree-0 vertices in increasing order.

Show solution

Indegrees:

- •indegree[1]=0
- •indegree[2]=0
- •indegree[3]=2 (1,2)
- •indegree[4]=2 (3,5)
- •indegree[5]=1 (2)

Q=[1,2]

Pop 1 → output [1]; update 3:2→1

Pop 2 → output [1,2]; update 3:1→0 (push 3); update 5:1→0 (push 5)

Q=[3,5]

Pop 3 → output [1,2,3]; update 4:2→1

Pop 5 → output [1,2,3,5]; update 4:1→0 (push 4)

Pop 4 → output [1,2,3,5,4]

Final order: 1, 2, 3, 5, 4

hard

A directed graph has vertices {A, B, C, D} and edges A -> B, B -> C, C -> A, C -> D. Using DFS color logic (WHITE/GRAY/BLACK), explain where the cycle is detected.

**Hint:** Start DFS at A. The cycle will appear when you traverse an edge to a GRAY vertex.

Show solution

Start DFS(A): A becomes GRAY.

Follow A -> B: DFS(B), B becomes GRAY.

Follow B -> C: DFS(C), C becomes GRAY.

Now explore C -> A. Vertex A is currently GRAY (still in the recursion stack), so edge C -> A is a back edge.

A back edge in a directed graph implies a directed cycle; here it reveals the cycle A -> B -> C -> A.

Therefore no topological ordering exists.

## Connections

Prerequisites you’re using here:

- •[Graph Traversal (BFS/DFS)](/tech-tree/graph-traversal/)

Next nodes this unlocks:

- •[Causal Inference](/tech-tree/causal-inference/)
- •[Task Discretization](/tech-tree/task-discretization/)

Related concepts to explore next:

- •[Directed Acyclic Graphs (DAGs)](/tech-tree/dag/)
- •[Cycle Detection in Directed Graphs](/tech-tree/directed-cycle-detection/)
- •[Dynamic Programming on DAGs](/tech-tree/dag-dp/)

Quality: A (4.6/5)

[← back to tree](/tech-tree/)[browse all →](/tech-tree/inventory/)
