---
title: Graph Traversal
description: BFS and DFS. Exploring all reachable nodes systematically.
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
permalink: /tech-tree/graph-traversal/
---

[←Back to Tech Tree](/tech-tree/)

[inventory](/tech-tree/inventory/)[coverage](/tech-tree/coverage/)

# Graph Traversal

Graph TheoryDifficulty: ★★☆☆☆Depth: 3Unlocks: 8

BFS and DFS. Exploring all reachable nodes systematically.

## Interactive Visualization

⏮◀◀▶▶STEP0.25x1xZOOM

t=0s

## Core Concepts

- -Reachability: traversal explores all nodes reachable from a given start node
- -Frontier/extraction policy: the order nodes are removed from the frontier determines traversal order (FIFO vs LIFO)
- -Visited marking: record nodes as visited when discovered to avoid revisiting and ensure termination

## Key Symbols & Notation

visited[v] (boolean marker indicating node v has been discovered)

## Essential Relationships

- -When a node is extracted from the frontier, its unvisited neighbors are marked (visited[v]=true) and inserted into the frontier; FIFO extraction yields breadth-first behavior, LIFO extraction yields depth-first behavior

## Prerequisites (2)

[Graph Representations6 atoms](/tech-tree/graph-representations/)[Linked Lists6 atoms](/tech-tree/linked-lists/)

## Unlocks (5)

[Topological Sortlvl 3](/tech-tree/topological-sort/)[Shortest Pathslvl 3](/tech-tree/shortest-paths/)[Minimum Spanning Treeslvl 3](/tech-tree/minimum-spanning-trees/)[Strongly Connected Componentslvl 3](/tech-tree/strongly-connected/)[Graph Coloringlvl 4](/tech-tree/graph-coloring/)

Advanced Learning Details

### Graph Position

33

Depth Cost

8

Fan-Out (ROI)

6

Bottleneck Score

3

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

### All Concepts (17)

- - Breadth-First Search (BFS): systematic level-by-level exploration from a start node
- - Depth-First Search (DFS): systematic depth-first exploration that follows a path as far as possible before backtracking
- - Queue (FIFO) as the frontier data structure used by BFS (enqueue / dequeue operations)
- - Stack (LIFO) or recursion as the frontier mechanism used by DFS (push / pop or recursive calls)
- - Visited marking / visited set to record which nodes have already been discovered and avoid revisiting
- - Frontier (the set/structure of discovered but not-yet-fully-explored nodes)
- - Parent / predecessor pointers (parent[v]) that record the traversal tree and allow path reconstruction
- - Distance / level array (dist[v] or level[v]) recording number of edges from the source (used in BFS)
- - Path reconstruction: recover an explicit path from source to a node by following parent pointers
- - Backtracking: the act of returning from deeper exploration in DFS and continuing with other branches
- - Reachability (whether a node is reachable from a given source via traversal)
- - Connected components discovery by running traversal(s) from unvisited nodes (each run yields one component)
- - Cycle detection via traversal (detecting edges that indicate a cycle)
- - Traversal order and DFS timestamps (discovery and finish times used to order/examine visit sequence)
- - Traversal produces a spanning tree or spanning forest of the reachable nodes (via parent pointers)
- - Time complexity of graph traversal algorithms (BFS/DFS) expressed as O(V + E) for adjacency-list graphs
- - Space complexity considerations for traversal: O(V) storage for visited/parent/dist and additional frontier/recursion stack

### Teaching Strategy

Self-serve tutorial - low prerequisites, straightforward concepts.

Graphs show up whenever “things connect to other things”: friends in a social network, pages linked on the web, roads between cities, function calls in code. Graph traversal is the basic skill that lets you explore what’s reachable from a starting point—systematically, without getting stuck in cycles, and with predictable order.

TL;DR:

Graph traversal means visiting every vertex reachable from a start vertex using a frontier (data structure of “discovered but not fully processed” vertices) plus a visited[v] marker to avoid revisits. BFS uses a FIFO queue (good for unweighted shortest paths in edges); DFS uses a LIFO stack/recursion (good for exploring deep structure and enabling algorithms like topological sort and SCCs).

## Prerequisites (stated up front) + important edge cases

Before you learn BFS/DFS, make sure these are solid:

1) **Graph representations** (you already know this)

- •**Adjacency list**: for each vertex u, store list of neighbors N(u). Great when the graph is sparse.
- •**Adjacency matrix**: an n×n table where entry (u,v) indicates if an edge exists. Great for dense graphs or O(1) edge queries.

2) **Queue/Stack basics** (quick refresh)

- •**Queue (FIFO)**: first in, first out. Operations: enqueue, dequeue.
- •**Stack (LIFO)**: last in, first out. Operations: push, pop.

3) **What “unweighted shortest path” means**

- •In an **unweighted** graph, every edge counts as cost 1.
- •The “shortest path” from s to v is the path with the **fewest edges**.
- •BFS (not DFS) gives shortest-path distances in this sense.

4) **Edge cases you must handle** (important for correctness)

- •**Self-loop** (u → u): If you mark visited[u] when discovered, then when you later scan neighbors and see u again, you ignore it. No infinite loop.
- •**Parallel edges** (multiple edges u → v): You may see v repeated in adjacency lists. visited[v] prevents adding v to the frontier multiple times.
- •**Disconnected graph**: Starting from s only reaches its connected component (or reachable set in directed graphs). To traverse the entire graph, you run traversal from every unvisited vertex.
- •**Directed vs undirected**: In directed graphs, reachability follows edge direction.

One key theme across everything you’re about to do: traversal is not “visit each vertex once by magic.” It’s a careful combination of:

- •a **frontier** that stores discovered vertices you still need to process
- •a **policy** for which frontier element to extract next (FIFO vs LIFO)
- •a **visited[v]** marker to guarantee termination and keep work bounded

## What Is Graph Traversal?

A **graph traversal** is a procedure that explores all vertices **reachable** from a given start vertex s, in a systematic order.

### Why do we need a traversal at all?

In a tree, you can “just” walk children pointers and never worry about coming back around. In a general graph, you can have:

- •**cycles** (A → B → C → A)
- •**multiple ways to reach the same vertex** (A → D and A → B → D)

Without a rule to avoid revisiting, you can loop forever.

### The three atomic concepts

#### 1) Reachability

Given a graph G = (V, E) and start vertex s, traversal explores:

- •All v ∈ V such that there exists a path from s to v.

If there is no path from s to v, traversal from s will never visit v.

#### 2) Frontier / extraction policy

Traversal maintains a **frontier**: vertices that have been discovered but not fully processed.

- •If you extract vertices in **FIFO order**, you get **Breadth-First Search (BFS)**.
- •If you extract vertices in **LIFO order**, you get **Depth-First Search (DFS)**.

This single design choice drastically changes the order of exploration and the properties you can prove.

#### 3) Visited marking

We maintain a boolean marker:

- •visited[v] = true means “v has been discovered already.”

This prevents:

- •infinite loops (cycles)
- •repeated work (multiple edges pointing to same vertex)

A subtle but crucial detail is **when** you set visited[v]. The standard and safest approach is:

- •Mark visited[v] **when you discover v** (i.e., when you push/enqueue it into the frontier), not when you pop/dequeue it.

If you delay marking until extraction, then parallel edges (or converging paths) can insert the same vertex many times, bloating runtime.

### Traversal skeleton (shared idea)

Here’s the shared structure both BFS and DFS follow:

1) Initialize all visited[v] = false

2) Create an empty frontier

3) Add s to frontier, set visited[s] = true

4) While frontier not empty:

- •remove a vertex u according to some policy
- •for each neighbor v of u:
- •if not visited[v]: set visited[v] = true and add v to frontier

The only difference is the frontier policy (queue vs stack).

## Core Mechanic 1: BFS (Breadth-First Search) with a FIFO Queue

### Why BFS exists (motivation)

Suppose you’re in a social network graph and want to find people closest to you:

- •distance 1: direct friends
- •distance 2: friends-of-friends
- •distance 3: three hops away

You want to explore in “layers” of increasing hop count. That is exactly what BFS does.

### Key idea: FIFO creates layers

BFS uses a **queue**, so vertices discovered earlier are processed earlier.

That enforces a level-by-level expansion from the start vertex s.

We often track a distance array (optional but common):

- •dist[v] = number of edges in the shortest path from s to v (in an unweighted graph)

Initialize:

- •dist[s] = 0
- •when you discover v from u, set dist[v] = dist[u] + 1

### BFS pseudocode (adjacency list)

Assume the graph is stored as adjacency lists Adj[u].

```
BFS(G, s):
  for each vertex v in V:
    visited[v] = false
    dist[v] = +∞
    parent[v] = NIL

  visited[s] = true
  dist[s] = 0
  Q = empty queue
  enqueue(Q, s)

  while Q not empty:
    u = dequeue(Q)
    for each v in Adj[u]:
      if visited[v] == false:
        visited[v] = true
        dist[v] = dist[u] + 1
        parent[v] = u
        enqueue(Q, v)
```

### What BFS guarantees (and why)

**Claim (unweighted shortest paths):** When BFS first discovers a vertex v, dist[v] is the length (in edges) of the shortest path from s to v.

Intuition:

- •The queue ensures all vertices at distance 0 are processed, then all at distance 1, then distance 2, etc.
- •So the first time you reach v, it must be via the smallest possible number of edges.

A useful view is “BFS tree”:

- •parent[v] pointers form a tree (or forest) of shortest paths from s.

### Complexity

Let n = |V| and m = |E|.

- •With adjacency lists: BFS runs in O(n + m).
- •Each vertex is enqueued at most once.
- •Each edge is scanned at most once (directed) or twice (undirected).
- •With adjacency matrix: scanning neighbors costs O(n) per vertex, so O(n²).

### Edge cases revisited under BFS

- •Self-loop u→u: when scanning neighbors of u, you see u but visited[u] is already true.
- •Parallel edges u→v repeated: the first time you see v you enqueue it; subsequent times visited[v] blocks duplicates.
- •Directed graphs: BFS respects direction; reachability and distances apply along directed paths.

## Core Mechanic 2: DFS (Depth-First Search) with a LIFO Stack (or Recursion)

### Why DFS exists (motivation)

Sometimes you don’t care about shortest hop count. You care about structure:

- •Is there a path from s to some target t? (DFS can find one quickly in practice)
- •Does the graph have cycles?
- •Can we order tasks with dependencies? (topological sort uses DFS)
- •What are strongly connected components? (DFS is a key ingredient)

DFS explores “as deep as possible” before backtracking.

### Two equivalent implementations

1) **Recursive DFS** (uses the call stack implicitly)

2) **Iterative DFS** (uses an explicit stack)

They behave similarly, but iterative DFS avoids recursion depth limits.

### Recursive DFS pseudocode

```
DFS(G, s):
  for each vertex v in V:
    visited[v] = false
    parent[v] = NIL

  dfsVisit(s)

  dfsVisit(u):
    visited[u] = true
    for each v in Adj[u]:
      if visited[v] == false:
        parent[v] = u
        dfsVisit(v)
```

### Iterative DFS (explicit stack) pseudocode

To match the “mark when discovered” rule:

```
DFS_iter(G, s):
  for each vertex v in V:
    visited[v] = false
    parent[v] = NIL

  S = empty stack
  visited[s] = true
  push(S, s)

  while S not empty:
    u = pop(S)
    for each v in Adj[u]:
      if visited[v] == false:
        visited[v] = true
        parent[v] = u
        push(S, v)
```

Note: This iterative version’s exact visitation order depends on neighbor ordering in Adj[u]. That’s normal.

### What DFS guarantees (and what it doesn’t)

DFS guarantees:

- •It visits all vertices reachable from s.
- •It produces a DFS tree via parent pointers.

DFS does **not** guarantee shortest paths.

Example intuition:

- •DFS might go s→a→b→c… (very deep) even if there is a direct edge s→c.

### Complexity

Same as BFS:

- •Adjacency list: O(n + m)
- •Adjacency matrix: O(n²)

### Edge cases under DFS

Identical handling as BFS with visited marking:

- •Self-loops and parallel edges are harmless.
- •Cycles do not cause infinite recursion/loop because visited stops revisits.

### A small but important note: “discovered” vs “finished”

Some DFS-based algorithms (topological sort, SCC) track timestamps:

- •discovery time (when visited becomes true)
- •finish time (when you return from recursion)

You don’t need timestamps to traverse, but it’s helpful to know DFS has a natural notion of “finishing” a node after exploring its descendants.

## Application / Connection: Choosing BFS vs DFS, and what traversal enables

### BFS vs DFS: how to choose

They solve different kinds of problems. The frontier policy is the whole story.

| Goal | Prefer | Why |
| --- | --- | --- |
| Explore in increasing number of edges from s | BFS | FIFO creates distance layers |
| Find shortest paths in an unweighted graph | BFS | First discovery gives shortest dist[v] |
| Detect cycles / reason about backtracking structure | DFS | Natural recursion stack / finish times |
| Topological sort (DAG ordering) | DFS | Uses finish times |
| Strongly connected components | DFS | Key building block (Kosaraju/Tarjan) |
| Just check reachability s → t | Either | Both are O(n+m); DFS may find a path quickly |

### Traversal as a “subroutine”

Many bigger algorithms start with “run BFS/DFS from …”

- •**Topological Sort**: DFS finishing order gives a valid linear ordering in DAGs.
- •**Shortest Paths**: BFS is the shortest-path algorithm for unweighted graphs; Dijkstra generalizes to weighted.
- •**Minimum Spanning Trees**: Not the same as traversal, but MST algorithms rely on graph structure and edge scanning; being comfortable with adjacency lists and visited concepts transfers directly.
- •**Strongly Connected Components**: DFS explores reachability; SCCs are about mutual reachability.
- •**Graph Coloring**: Traversal helps you color connected components and perform checks (though optimal coloring is harder).

### Traversing the entire graph (graph may be disconnected)

So far we assumed a start node s. If you want to visit every vertex in the graph:

```
for each vertex v in V:
  if visited[v] == false:
    BFS(G, v)   // or DFS(G, v)
```

This produces a **forest** of BFS/DFS trees—one per connected component (undirected) or per reachable region (directed).

### One more practical detail: adjacency list + duplicates

Because adjacency lists can contain repeated neighbors (parallel edges), you should always structure the neighbor scan as:

- •check visited[v] before pushing/enqueueing

This keeps runtime tight: each vertex enters the frontier once.

## Worked Examples (3)

### Worked Example 1: BFS layers + shortest path reconstruction

Graph (undirected) with vertices {A,B,C,D,E,F}. Edges: A-B, A-C, B-D, C-D, C-E, D-F, E-F. Start s = A. Use BFS to compute dist[·] and parent[·], then reconstruct a shortest path from A to F.

1. Initialize:

   visited[*]=false, dist[*]=∞, parent[\*]=NIL

   visited[A]=true, dist[A]=0

   Q=[A]
2. Dequeue A. Neighbors: B, C.

   B unvisited ⇒ visited[B]=true, dist[B]=1, parent[B]=A, enqueue B

   C unvisited ⇒ visited[C]=true, dist[C]=1, parent[C]=A, enqueue C

   Now Q=[B,C]
3. Dequeue B. Neighbors: A, D.

   A already visited ⇒ ignore

   D unvisited ⇒ visited[D]=true, dist[D]=2, parent[D]=B, enqueue D

   Now Q=[C,D]
4. Dequeue C. Neighbors: A, D, E.

   A visited ⇒ ignore

   D is already visited (discovered via B) ⇒ ignore (important!)

   E unvisited ⇒ visited[E]=true, dist[E]=2, parent[E]=C, enqueue E

   Now Q=[D,E]
5. Dequeue D. Neighbors: B, C, F.

   B visited ⇒ ignore

   C visited ⇒ ignore

   F unvisited ⇒ visited[F]=true, dist[F]=3, parent[F]=D, enqueue F

   Now Q=[E,F]
6. Dequeue E. Neighbors: C, F.

   C visited ⇒ ignore

   F already visited ⇒ ignore

   Q=[F]
7. Dequeue F. Neighbors: D, E (both visited). Done. Q=[]
8. Distances found:

   dist[A]=0

   dist[B]=1, dist[C]=1

   dist[D]=2, dist[E]=2

   dist[F]=3
9. Reconstruct shortest path A→F using parent pointers:

   F has parent D

   D has parent B

   B has parent A

   So path (reverse) is F←D←B←A ⇒ A→B→D→F

   This path has 3 edges, matching dist[F]=3.

**Insight:** The moment F is first discovered, BFS has already guaranteed it used the fewest edges possible. Notice how the edge C-D did not change dist[D] after D was discovered; visited marking at discovery time prevents duplicates and preserves the first (shortest) discovery.

### Worked Example 2: DFS exploration order and why it’s not shortest

Directed graph with vertices {S, A, B, C, T}. Edges: S→A, S→T, A→B, B→C, C→T. Start at S. Run DFS (recursive) scanning neighbors in alphabetical order. Compare the path found to the shortest path in edges.

1. Adjacency lists (alphabetical):

   Adj[S]=[A,T]

   Adj[A]=[B]

   Adj[B]=[C]

   Adj[C]=[T]

   Adj[T]=[]
2. Start dfsVisit(S):

   visited[S]=true
3. From S, first neighbor is A (unvisited):

   parent[A]=S

   call dfsVisit(A)
4. At A:

   visited[A]=true

   neighbor B unvisited ⇒ parent[B]=A, dfsVisit(B)
5. At B:

   visited[B]=true

   neighbor C unvisited ⇒ parent[C]=B, dfsVisit(C)
6. At C:

   visited[C]=true

   neighbor T unvisited ⇒ parent[T]=C, dfsVisit(T)
7. At T:

   visited[T]=true

   Adj[T] empty ⇒ return
8. Unwind returns back to C, B, A, S.

   Back at S, next neighbor is T, but visited[T]=true so it is skipped.

**Insight:** DFS found a path S→A→B→C→T (4 edges), even though there is a direct edge S→T (1 edge). DFS is about deep exploration, not shortest paths. Neighbor order can strongly influence what DFS finds first.

### Worked Example 3: Handling self-loops and parallel edges with visited[v]

Directed graph with vertices {1,2,3}. Edges: 1→1 (self-loop), 1→2 (two parallel edges), 2→3. Start BFS at 1. Show the queue evolution and explain why it terminates cleanly.

1. Adj[1]=[1,2,2]

   Adj[2]=[3]

   Adj[3]=[]

   Initialize visited[\*]=false

   visited[1]=true, Q=[1]
2. Dequeue 1. Scan neighbors:

   - •v=1 (self-loop): visited[1] already true ⇒ do nothing
   - •v=2: unvisited ⇒ visited[2]=true, enqueue 2
   - •v=2 again (parallel edge): visited[2] already true ⇒ do nothing

   Now Q=[2]
3. Dequeue 2. Neighbor v=3 unvisited ⇒ visited[3]=true, enqueue 3

   Q=[3]
4. Dequeue 3. No neighbors. Q=[] stop.

**Insight:** Marking visited at discovery time ensures each vertex enters the frontier at most once, even if adjacency lists contain duplicates (parallel edges) or cycles (including self-loops).

## Key Takeaways

- ✓

  Traversal explores all vertices **reachable** from a start vertex s; unreachable vertices require separate starts.
- ✓

  The **frontier** is the set of discovered-but-not-processed vertices; its extraction policy defines BFS vs DFS.
- ✓

  BFS uses a **FIFO queue** and explores in distance layers; it yields **unweighted shortest-path distances** in number of edges.
- ✓

  DFS uses a **LIFO stack/recursion** and explores deep before backtracking; it’s foundational for structural algorithms (topological sort, SCC).
- ✓

  Use a boolean marker **visited[v]** and (usually) set it **when you discover v** to avoid duplicates and guarantee termination.
- ✓

  With adjacency lists, both BFS and DFS run in O(|V| + |E|); with adjacency matrices, neighbor scanning often costs O(|V|²).
- ✓

  Self-loops and parallel edges do not break traversal if visited marking is done correctly—they just add redundant neighbor checks.

## Common Mistakes

- ✗

  Marking visited[v] only when you pop/dequeue v, which can cause the same vertex to be added many times (especially with parallel edges).
- ✗

  Expecting DFS to produce shortest paths; only BFS guarantees shortest paths in unweighted graphs.
- ✗

  Forgetting that traversal from a single start vertex won’t visit disconnected parts of the graph (or unreachable regions in directed graphs).
- ✗

  Using an adjacency matrix but still assuming O(|V|+|E|) runtime; with a matrix you typically scan O(|V|) neighbors per vertex.

## Practice

easy

Run BFS on the undirected graph with vertices {0,1,2,3,4} and edges: 0-1, 0-2, 1-3, 2-3, 3-4. Start at 0. Compute dist[·] and one shortest path from 0 to 4 using parent pointers.

**Hint:** Initialize dist[0]=0. When you discover a neighbor v from u, set dist[v]=dist[u]+1 and parent[v]=u.

Show solution

BFS layers:

Start: dist[0]=0

Discover 1 and 2 ⇒ dist[1]=1 parent[1]=0; dist[2]=1 parent[2]=0

Process 1 ⇒ discover 3 ⇒ dist[3]=2 parent[3]=1

Process 2 ⇒ 3 already visited

Process 3 ⇒ discover 4 ⇒ dist[4]=3 parent[4]=3

Shortest path 0→4: follow parents 4←3←1←0 ⇒ 0→1→3→4 (length 3).

medium

Give a small directed graph where DFS from S visits T, but the DFS parent path from S to T is longer (more edges) than the shortest path. Explain briefly why BFS would avoid this.

**Hint:** Include both a direct edge S→T and a longer chain S→A→B→…→T, and order neighbors so DFS explores the chain first.

Show solution

Example: vertices {S,A,B,T}. Edges: S→A, A→B, B→T, and S→T. If Adj[S]=[A,T], DFS explores S→A→B→T (3 edges) and marks T visited before returning to consider S→T. BFS would discover T from S immediately with dist[T]=1, which is the unweighted shortest path.

medium

You want to traverse an entire graph that may be disconnected. Describe (in pseudocode-level English) how to use BFS or DFS to ensure every vertex is visited exactly once, even with self-loops and parallel edges.

**Hint:** Use an outer loop over all vertices; start a new traversal whenever you find an unvisited vertex; mark visited on discovery.

Show solution

Set visited[v]=false for all v. For each vertex v in V: if visited[v]==false, start BFS/DFS from v. In the traversal, when scanning neighbors u of a popped vertex, only enqueue/push u if visited[u]==false, and immediately set visited[u]=true. This prevents repeats from cycles, self-loops, or parallel edges and guarantees each vertex is added to the frontier at most once.

## Connections

- •[Topological Sort](/tech-tree/topological-sort/)
- •[Shortest Paths](/tech-tree/shortest-paths/)
- •[Minimum Spanning Trees](/tech-tree/minimum-spanning-trees/)
- •[Strongly Connected Components](/tech-tree/strongly-connected/)
- •[Graph Coloring](/tech-tree/graph-coloring/)

Related refreshers:

- •[Graph Representations](/tech-tree/graph-representations/)
- •[Stacks and Queues](/tech-tree/stacks-queues/)

Quality: A (4.5/5)

[← back to tree](/tech-tree/)[browse all →](/tech-tree/inventory/)
