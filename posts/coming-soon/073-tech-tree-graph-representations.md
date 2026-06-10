---
title: Graph Representations
description: Adjacency matrix vs adjacency list. Space-time tradeoffs.
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
inspiration_url: https://templeton.host/tech-tree/graph-representations/
inspiration_category: tech-tree
---

> Source-copy draft imported from [https://templeton.host/tech-tree/graph-representations/](https://templeton.host/tech-tree/graph-representations/). Names, domain references, and local media paths were adapted for Xavi Ablaza / getablaza.com.

[←Back to Tech Tree](/tech-tree/)

[inventory](/tech-tree/inventory/)[coverage](/tech-tree/coverage/)

# Graph Representations

Graph TheoryDifficulty: ★★☆☆☆Depth: 2Unlocks: 10

Adjacency matrix vs adjacency list. Space-time tradeoffs.

## Interactive Visualization

⏮◀◀▶▶STEP0.25x1xZOOM

t=0s

## Core Concepts

- -Adjacency matrix: a two-dimensional array where entry A[i][j] records whether (or with what weight) there is an edge between vertices i and j.
- -Adjacency list: for each vertex v, a sequence (list/array) of its neighbor vertices; stores only existing edges.

## Key Symbols & Notation

A[i][j] (adjacency matrix entry for vertices i and j)Adj[v] (the list of neighbors of vertex v in an adjacency-list representation)

## Essential Relationships

- -Space tradeoff: adjacency matrix uses Theta(n^2) space; adjacency list uses Theta(n + m) space (n = number of vertices, m = number of edges).
- -Operation tradeoff: edge-existence check is O(1) with a matrix vs O(deg(v)) with a list; iterating neighbors is Theta(n) by scanning a matrix row vs Theta(deg(v)) from a list - choice depends on graph density and needed operations.

## Prerequisites (2)

[Graphs Introduction5 atoms](/tech-tree/graphs-basic/)[Arrays5 atoms](/tech-tree/arrays/)

## Unlocks (2)

[Graph Traversallvl 2](/tech-tree/graph-traversal/)[Spectral Graph Theorylvl 4](/tech-tree/spectral-graph-theory/)

Advanced Learning Details

### Graph Position

22

Depth Cost

10

Fan-Out (ROI)

7

Bottleneck Score

2

Chain Length

### Cognitive Load

6

Atomic Elements

32

Total Elements

L1

Percentile Level

L4

Atomic Level

### All Concepts (13)

- - Adjacency matrix: represent a graph as an n×n matrix A where A[i][j] indicates whether (or with what weight) there is an edge from vertex i to vertex j
- - Adjacency list: represent a graph by storing, for each vertex v, a list (or vector) of its neighbor vertices (and optionally edge weights)
- - Space complexity of adjacency matrix: uses O(n^2) memory (depends only on number of vertices)
- - Space complexity of adjacency list: uses O(n + m) memory (depends on vertices plus edges)
- - Edge-existence query cost: how long it takes to check whether edge (u,v) exists under each representation
- - Neighbor-iteration cost: cost to enumerate all neighbors of a vertex under each representation
- - Edge insertion/removal cost differences between matrix and list representations
- - Graph density notions (sparse vs dense) as a driver for representation choice
- - Vertex degree deg(v): number of edges incident to v (affects adjacency-list costs)
- - Symmetry/redundancy for undirected graphs: adjacency matrix is symmetric and adjacency lists store each undirected edge twice (once per endpoint)
- - Storing weights: adjacency-matrix entries can hold weights; adjacency-list entries become (neighbor, weight) pairs
- - Memory-locality and constant-factor overheads: matrix is contiguous (better cache locality), lists incur pointer/structure overhead
- - Space–time tradeoff principle applied to graph representations: spending more space (matrix) can speed certain operations, using less space (list) can slow them but save memory

### Teaching Strategy

Deep-dive lesson - accessible entry point but dense material. Use worked examples and spaced repetition.

A graph is only as useful as the way you store it. The same graph can feel “fast” or “slow” depending on whether you represent edges as a dense table (matrix) or as sparse neighbor lists.

TL;DR:

Two standard graph representations are:

- •**Adjacency matrix** A where A[i][j] tells you whether (or with what weight) edge i → j exists.
- •**Adjacency list** Adj where Adj[v] is a list of v’s neighbors.

Matrices give O(1) edge-existence queries but cost Θ(V²) space; lists use Θ(V + E) space and make “iterate neighbors” fast, but checking if a specific edge exists may be slower unless you add extra indexing.

## What Is Graph Representations?

### Why representation matters

When you learn graphs, it’s natural to focus on the **mathematical object**: a set of vertices V and edges E. But when you implement algorithms (BFS, DFS, shortest paths, connectivity checks), you must choose a **data structure**. That choice controls:

- •**Space usage**: Do you allocate memory for every possible edge, or only edges that exist?
- •**Time for common operations**:
- •“Does edge (i, j) exist?”
- •“What are the neighbors of v?”
- •“Add/remove an edge.”

Many graph algorithms are dominated by how quickly you can **iterate over neighbors**. Others frequently ask **membership** questions (“is there an edge here?”). Different representations optimize different patterns.

### Two standard ways to store a graph

We’ll focus on two core representations:

1) **Adjacency matrix**

- •A 2D array A where entry A[i][j] records whether there is an edge between vertices i and j.
- •For weighted graphs, A[i][j] can store the **weight** (and some special value to mean “no edge”).

2) **Adjacency list**

- •For each vertex v, store a collection (often a list or dynamic array) of the neighbors of v.
- •Notation: Adj[v] = [neighbors of v].

### What assumptions we’ll make

- •Vertices are labeled 0…V−1 so we can index arrays.
- •Graph can be **directed** or **undirected**.
- •Graph can be **unweighted** or **weighted**.

We’ll use:

- •V = number of vertices
- •E = number of edges

A graph is called **dense** when E is close to V², and **sparse** when E is much smaller than V² (for example E ≈ V, or E ≈ V log V).

A quick density intuition:

- •Maximum directed edges (no self-loops): V(V−1)
- •Maximum undirected edges (no self-loops): V(V−1)/2

So V² is the scale of “all possible edges.”

### The big picture

A matrix spends memory on **all possible edges**. A list spends memory only on **existing edges**. That single idea drives most of the space-time tradeoffs you’ll see in practice.

## Core mechanic 1: Adjacency Matrix (A[i][j])

### Why use a matrix?

An adjacency matrix is conceptually simple: you create a table where rows and columns correspond to vertices. Then:

- •A[i][j] = 1 if edge i → j exists (unweighted)
- •A[i][j] = w if edge i → j has weight w (weighted)

The main motivation is **constant-time edge queries**:

- •“Is there an edge from i to j?” becomes a single array lookup.

### Definition

Let the vertices be {0, 1, …, V−1}. The adjacency matrix A is a V×V array such that:

- •**Directed, unweighted**:
- •A[i][j] ∈ {0, 1}
- •A[i][j] = 1 ⇔ (i, j) ∈ E

- •**Undirected, unweighted**:
- •A[i][j] = A[j][i]
- •The matrix is symmetric.

- •**Weighted**:
- •A[i][j] = weight(i, j) if edge exists
- •Otherwise A[i][j] = 0, or ∞, or null (choose a sentinel carefully)

A common choice for weighted graphs is:

- •A[i][j] = ∞ meaning “no edge”
- •A[i][i] = 0 (distance from a node to itself)

### Space cost

A matrix allocates V² entries.

- •Space: Θ(V²)

This is great if the graph is dense (lots of edges), but wasteful if the graph is sparse.

### Time for common operations

With an adjacency matrix:

- •Check if edge (i, j) exists: Θ(1)
- •Add/remove edge (i, j): Θ(1)
- •Iterate neighbors of v:
- •Must scan row v (or column v) of length V
- •Time: Θ(V)

That last bullet is the key weakness: even if v has only 3 neighbors, you still scan V possible neighbors.

### Directed vs undirected details

- •Directed graph: A[i][j] and A[j][i] are independent.
- •Undirected graph: store both directions; set A[i][j] = A[j][i].

### Small example

Suppose V = 4 with undirected edges:

- •0—1, 0—2, 2—3

Then A is:

- •Row 0: connected to 1 and 2 → [0, 1, 1, 0]
- •Row 1: connected to 0 → [1, 0, 0, 0]
- •Row 2: connected to 0 and 3 → [1, 0, 0, 1]
- •Row 3: connected to 2 → [0, 0, 1, 0]

You can answer “Is there an edge 2—3?” by checking A[2][3] (and A[3][2]).

### When matrices shine

Matrices are especially good when:

- •The graph is dense (E ≈ V²)
- •You do many edge-existence queries
- •You plan to use matrix-based math (e.g., eigenvalues in spectral graph theory)

Even if you don’t do advanced math, matrices can be convenient for small graphs because they’re simple to implement and debug.

## Core mechanic 2: Adjacency List (Adj[v])

### Why use a list?

In many real-world graphs (social networks, web links, road networks), each node connects to a relatively small number of neighbors compared to V. That means the graph is **sparse**.

If you used a matrix, you would allocate V² space even though only E edges exist.

An adjacency list stores only the edges that exist, so it scales with E.

### Definition

Adj is an array (indexed by vertex) where each entry is a collection of neighbors.

- •For an unweighted directed graph:
- •Adj[v] contains all vertices u such that v → u is an edge.

- •For an unweighted undirected graph:
- •If v—u is an edge, then u appears in Adj[v] and v appears in Adj[u].

- •For a weighted graph:
- •Adj[v] contains pairs (u, w) meaning edge v → u has weight w.

So you might see:

- •Adj[v] = [u₁, u₂, …]
- •or Adj[v] = [(u₁, w₁), (u₂, w₂), …]

### Space cost

Adjacency lists store:

- •The list headers for V vertices
- •Plus one list entry per edge (or two per edge in an undirected graph, since each undirected edge is stored twice).

Asymptotically:

- •Space: Θ(V + E)

This is dramatically better than Θ(V²) when E ≪ V².

### Time for common operations

With an adjacency list:

- •Iterate neighbors of v:
- •Time: Θ(deg(v)) where deg(v) is the number of neighbors

This is a huge win for traversal algorithms (BFS/DFS) because they naturally iterate neighbors.

But membership queries can be slower:

- •Check if edge (i, j) exists:
- •You must search within Adj[i]
- •Time: Θ(deg(i)) with a plain list

You can improve this by changing the per-vertex container:

- •If Adj[v] is a **hash set**, membership can be expected Θ(1)
- •If Adj[v] is a **sorted array**, membership can be Θ(log deg(v)) via binary search

However, these choices have their own tradeoffs (overhead, insertion time, ordering).

### Small example

Using the same undirected graph:

- •0—1, 0—2, 2—3

Adj could be:

- •Adj[0] = [1, 2]
- •Adj[1] = [0]
- •Adj[2] = [0, 3]
- •Adj[3] = [2]

Now “iterate neighbors of 2” is just scanning [0, 3], which is Θ(2), not Θ(V).

### When lists shine

Adjacency lists are especially good when:

- •The graph is sparse
- •You frequently traverse neighbors (BFS/DFS, shortest paths, connected components)
- •You want memory proportional to the actual edges

They are the default choice for many algorithmic problems because many classic running times are expressed as Θ(V + E), and adjacency lists make that achievable.

## Application/Connection: Space–Time Tradeoffs and Choosing the Right One

### The two key operations to compare

Most decisions reduce to two questions:

1) How often do you need to ask: “Does (i, j) exist?”

2) How often do you need: “List all neighbors of v.”

Adjacency matrix is best for (1).

Adjacency list is best for (2) on sparse graphs.

### Side-by-side comparison

| Operation / Property | Adjacency matrix A[i][j] | Adjacency list Adj[v] |
| --- | --- | --- |
| Space | Θ(V²) | Θ(V + E) |
| Check edge (i, j) exists | Θ(1) | Θ(deg(i)) (plain list) |
| Add/remove edge | Θ(1) | Θ(1) amortized to append (remove can be Θ(deg(i))) |
| Iterate neighbors of v | Θ(V) | Θ(deg(v)) |
| Best for | Dense graphs, many membership queries, matrix math | Sparse graphs, traversals, scalable storage |
| Undirected storage | symmetric A | store each edge twice |

### Dense vs sparse: a practical rule of thumb

Compare E to V².

- •If E is on the order of V² (dense), matrix space Θ(V²) is not “wasted,” and O(1) edge queries are very attractive.
- •If E is much smaller (sparse), lists reduce memory and usually speed up algorithms that walk edges.

A concrete mental check:

- •If V = 10,000 then V² = 100,000,000 entries.
- •Even if each entry were 1 byte, that’s ~100 MB (and often it’s more, e.g., 4 bytes or 8 bytes).
- •If E = 50,000, then Θ(V + E) is ~60,000 list items (plus overhead), far smaller.

### Traversal complexity preview (why this unlocks BFS/DFS)

BFS/DFS often have a natural bound of Θ(V + E) when using adjacency lists:

- •You visit each vertex once: Θ(V)
- •You scan each edge once (or twice in undirected): Θ(E)

With an adjacency matrix, scanning neighbors costs Θ(V) per vertex, so traversal becomes Θ(V²), regardless of how few edges exist.

This is one of the main reasons adjacency lists are the standard representation for graph traversal lessons.

### Connection to spectral graph theory (why matrices matter)

Spectral methods use linear algebra objects like:

- •the adjacency matrix A
- •the degree matrix D (diagonal)
- •the Laplacian L = D − A

Eigenvalues/eigenvectors are defined for matrices, so matrix representations (or at least matrix-like operators) are the natural language.

Even if the graph is sparse, spectral computations often rely on sparse-matrix data structures—but the core conceptual object remains A.

### Weighted graphs and “no edge” representation

Be careful with weighted graphs:

- •In a matrix, you need a sentinel for “no edge.” Using 0 can be ambiguous if weight 0 is valid.
- •Common choice: A[i][j] = ∞ for no edge (especially in shortest path contexts), and A[i][i] = 0.

In adjacency lists, the absence of an edge is natural: if (j, w) is not in Adj[i], the edge is absent.

### Summary decision guide

- •Choose **adjacency list** by default for algorithmic graph problems and traversals.
- •Choose **adjacency matrix** when you need fast membership queries, have dense graphs, or want direct access to matrix-based math.

If you later find you need both benefits, you can maintain both structures—but that increases code complexity and memory.

## Worked Examples (3)

### Build A and Adj for the same directed graph

Let V = {0,1,2,3}. Directed edges: 0→1, 0→2, 2→1, 3→0. Unweighted. Construct the adjacency matrix A and adjacency list Adj.

1. Step 1: Initialize A as a 4×4 matrix of zeros.

   A =

   [ [0,0,0,0],

   [0,0,0,0],

   [0,0,0,0],

   [0,0,0,0] ]
2. Step 2: Fill in A[i][j] = 1 for each directed edge i→j.

   Edges:

   - •0→1 ⇒ A[0][1] = 1
   - •0→2 ⇒ A[0][2] = 1
   - •2→1 ⇒ A[2][1] = 1
   - •3→0 ⇒ A[3][0] = 1
3. Step 3: Write the final matrix explicitly by rows.

   Row 0 has edges to 1 and 2: [0,1,1,0]

   Row 1 has no outgoing edges: [0,0,0,0]

   Row 2 has edge to 1: [0,1,0,0]

   Row 3 has edge to 0: [1,0,0,0]

   So

   A =

   [ [0,1,1,0],

   [0,0,0,0],

   [0,1,0,0],

   [1,0,0,0] ]
4. Step 4: Build Adj as an array of 4 lists, initially empty.

   Adj[0]=[ ]

   Adj[1]=[ ]

   Adj[2]=[ ]

   Adj[3]=[ ]
5. Step 5: Append each edge i→j to Adj[i].

   - •0→1 ⇒ Adj[0]=[1]
   - •0→2 ⇒ Adj[0]=[1,2]
   - •2→1 ⇒ Adj[2]=[1]
   - •3→0 ⇒ Adj[3]=[0]

   Final:

   Adj[0]=[1,2]

   Adj[1]=[ ]

   Adj[2]=[1]

   Adj[3]=[0]

**Insight:** A and Adj store the same information, but support different fast operations: A gives O(1) edge checks like “is 2→1 present?”, while Adj makes it cheap to enumerate outgoing neighbors like “who can 0 reach in one step?”

### Compare memory and traversal cost on a sparse graph

Suppose V = 1000 and E = 3000 (directed). Estimate the number of stored entries for an adjacency matrix vs an adjacency list, and compare the cost of iterating neighbors across all vertices (as in BFS/DFS).

1. Step 1: Adjacency matrix storage.

   A has V² entries.

   V² = 1000² = 1,000,000 entries.

   So storage is Θ(1,000,000) cells (times the size per cell).
2. Step 2: Adjacency list storage.

   Adj stores:

   - •V list headers (1000)
   - •plus one neighbor entry per directed edge (E = 3000)

   Total list items ≈ V + E = 1000 + 3000 = 4000 (ignoring overhead).

   So storage is Θ(4000) items.
3. Step 3: Neighbor iteration cost for a traversal.

   A typical traversal needs to scan neighbors of each vertex.

   With a matrix:

   - •scanning neighbors of one vertex costs Θ(V) = Θ(1000)
   - •for all vertices: Θ(V·V) = Θ(V²) = Θ(1,000,000)

   With a list:

   - •scanning neighbors of v costs Θ(deg(v))
   - •summed over all vertices: ∑ᵥ deg(v) = E

   So total cost is Θ(V + E) = Θ(1000 + 3000) = Θ(4000).
4. Step 4: Interpret the result.

   Matrix neighbor scans touch 1,000,000 potential edges.

   List neighbor scans touch only the 3,000 real edges (plus vertex overhead).

**Insight:** On sparse graphs, adjacency lists turn many graph algorithms into “work proportional to what exists” (V + E), while adjacency matrices force you to repeatedly scan nonexistent edges, pushing you toward V² time.

### Weighted graph: choosing a sentinel in A[i][j] vs storing pairs in Adj[v]

Vertices {0,1,2}. Directed weighted edges: 0→1 with weight 5, 0→2 with weight 0, 2→1 with weight −2. Build both representations and highlight the ‘no edge’ issue.

1. Step 1: Notice weight 0 is a valid edge weight (0→2 has weight 0).

   Therefore, using 0 to mean “no edge” in a matrix would be ambiguous.
2. Step 2: Choose a sentinel for ‘no edge’ in the matrix.

   A common choice is ∞.

   Initialize A as a 3×3 matrix with ∞ everywhere, and set diagonal to 0:

   A =

   [ [0, ∞, ∞],

   [∞, 0, ∞],

   [∞, ∞, 0] ]
3. Step 3: Fill in edge weights.

   - •0→1 weight 5 ⇒ A[0][1] = 5
   - •0→2 weight 0 ⇒ A[0][2] = 0
   - •2→1 weight −2 ⇒ A[2][1] = −2

   So

   A =

   [ [0, 5, 0],

   [∞, 0, ∞],

   [∞, −2, 0] ]
4. Step 4: Build adjacency list with (neighbor, weight) pairs.

   Adj[0] = [(1,5), (2,0)]

   Adj[1] = [ ]

   Adj[2] = [(1,−2)]
5. Step 5: Compare ‘no edge’ meaning.

   In the matrix, A[1][0] = ∞ explicitly stores “no edge.”

   In the list, the absence of 0 from Adj[1] implicitly means “no edge.”

**Insight:** Weighted matrices require a careful choice of sentinel (∞, null) to represent missing edges, especially when 0 or negative weights are allowed. Adjacency lists avoid this ambiguity by storing only real edges.

## Key Takeaways

- ✓

  Adjacency matrix A is a V×V table where A[i][j] records whether/what weight edge i → j exists.
- ✓

  Adjacency list Adj stores, for each vertex v, exactly the neighbors reachable from v (and optionally weights).
- ✓

  Space: matrix is Θ(V²); list is Θ(V + E) (or Θ(V + 2E) for undirected storage, which is still Θ(V + E)).
- ✓

  Edge-existence checks are Θ(1) with matrices but typically Θ(deg(i)) with plain adjacency lists.
- ✓

  Neighbor iteration is Θ(V) per vertex in matrices but Θ(deg(v)) per vertex in lists—crucial for BFS/DFS.
- ✓

  Sparse graphs strongly favor adjacency lists; dense graphs (or heavy edge-query workloads) can favor matrices.
- ✓

  Weighted graphs in matrix form need a well-defined ‘no edge’ sentinel (often ∞) to avoid ambiguity.

## Common Mistakes

- ✗

  Using 0 in a weighted adjacency matrix to mean “no edge” when weight 0 is a valid value; prefer ∞/null or a separate boolean matrix.
- ✗

  Forgetting that undirected graphs require symmetric storage: A[i][j] = A[j][i] and u in Adj[v] implies v in Adj[u].
- ✗

  Assuming adjacency lists always give O(1) edge-existence checks; with a plain list it’s Θ(deg(i)) unless you add a set/hash structure.
- ✗

  Implementing BFS/DFS over an adjacency matrix and expecting Θ(V + E); neighbor scans make it Θ(V²) in general.

## Practice

easy

You have an undirected unweighted graph with V = 6 and edges: 0—1, 0—4, 1—2, 2—3, 3—4. Write (a) its adjacency list Adj and (b) one row of its adjacency matrix A (specifically row 0).

**Hint:** Undirected means each edge appears in both endpoints’ neighbor lists, and A is symmetric. Row 0 marks neighbors of 0 with 1s.

Show solution

Adj:

Adj[0] = [1,4]

Adj[1] = [0,2]

Adj[2] = [1,3]

Adj[3] = [2,4]

Adj[4] = [0,3]

Adj[5] = [ ]

Row 0 of A (columns 0..5):

A[0] = [0,1,0,0,1,0]

medium

For a directed graph, V = 2000 and E = 10,000. Compare Θ(V²) and Θ(V + E) numerically, and explain which representation is likely better for BFS and why.

**Hint:** Compute V² and V + E. BFS mainly needs to iterate neighbors of visited nodes.

Show solution

V² = 2000² = 4,000,000.

V + E = 2000 + 10,000 = 12,000.

For BFS, adjacency lists are likely better because BFS iterates over outgoing neighbors; with lists this costs Θ(V + E) ≈ 12,000 neighbor entries plus overhead, while a matrix-based BFS would scan Θ(V) = 2000 potential neighbors per vertex, pushing toward Θ(V²) ≈ 4,000,000 checks.

hard

You need to support many queries of the form “is there an edge (i, j)?” on a sparse graph. Propose one way to keep the adjacency-list space advantage but speed up edge existence checks.

**Hint:** Change the per-vertex container type or add an auxiliary index structure.

Show solution

One approach is to store Adj[v] as a hash set (or maintain an additional hash set alongside a list). Then checking whether j ∈ Adj[i] can be expected Θ(1), while total space remains proportional to Θ(V + E) (with higher constant factors). Another approach is to keep Adj[v] sorted and use binary search for Θ(log deg(v)) membership queries.

## Connections

Next nodes:

- •[Graph Traversal](/tech-tree/graph-traversal/) — BFS/DFS typically assume adjacency lists to achieve Θ(V + E).
- •[Spectral Graph Theory](/tech-tree/spectral-graph-theory/) — adjacency matrices (and Laplacians) are central objects for eigenvalue-based analysis.

Quality: A (4.7/5)

[← back to tree](/tech-tree/)[browse all →](/tech-tree/inventory/)
