---
title: Trees
description: Connected acyclic graphs. Root, leaves, parent-child relationships.
date: '2026-07-01'
scheduled: '2026-09-22'
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
inspiration_url: https://templeton.host/tech-tree/trees/
inspiration_category: tech-tree
---

> Source-copy draft imported from [https://templeton.host/tech-tree/trees/](https://templeton.host/tech-tree/trees/). Names, domain references, and local media paths were adapted for Xavi Ablaza / getablaza.com.

[←Back to Tech Tree](/tech-tree/)

[inventory](/tech-tree/inventory/)[coverage](/tech-tree/coverage/)

# Trees

Graph TheoryDifficulty: ★★☆☆☆Depth: 2Unlocks: 9

Connected acyclic graphs. Root, leaves, parent-child relationships.

## Interactive Visualization

⏮◀◀▶▶STEP0.25x1xZOOM

t=0s

## Core Concepts

- -Tree: a connected acyclic graph
- -Rooted tree: a tree with one distinguished root that orients nodes into parent-child directions
- -Leaf: a node with no children (a terminal node)

## Key Symbols & Notation

parent(x) - the parent of node x (undefined for the root)

## Essential Relationships

- -Every non-root node has exactly one parent (parent(x) is unique for each non-root node)

## Prerequisites (1)

[Graphs Introduction5 atoms](/tech-tree/graphs-basic/)

## Unlocks (4)

[Binary Treeslvl 2](/tech-tree/binary-trees/)[Minimum Spanning Treeslvl 3](/tech-tree/minimum-spanning-trees/)[Disjoint Setslvl 3](/tech-tree/disjoint-sets/)[Trieslvl 3](/tech-tree/tries/)

Advanced Learning Details

### Graph Position

16

Depth Cost

9

Fan-Out (ROI)

5

Bottleneck Score

2

Chain Length

### Cognitive Load

5

Atomic Elements

40

Total Elements

L3

Percentile Level

L3

Atomic Level

### All Concepts (14)

- - Tree: a graph that is connected and contains no cycles (connected + acyclic)
- - Root: a distinguished vertex chosen as the top of a rooted tree
- - Rooted tree: a tree with a designated root that induces parent-child orientation
- - Parent: the immediate predecessor of a node toward the root
- - Child: an immediate successor of a node away from the root
- - Leaf (external node): a node with no children (in undirected view: typically degree 1, with a special-case for single-vertex tree)
- - Internal node: a node that is not a leaf (has at least one child)
- - Ancestor: any node on the path from the root to a given node (inclusive/exclusive as defined)
- - Descendant: any node for which the given node is an ancestor
- - Siblings: distinct nodes that share the same parent
- - Subtree (rooted at v): the node v together with all of its descendants, forming a tree
- - Unique simple path: between any two vertices in a tree there is exactly one simple path
- - Depth (level) of a node: the number of edges on the path from the root to that node
- - Height of a node: the length (in edges) of the longest path from that node down to a leaf; height of a tree: height of its root

### Teaching Strategy

Self-serve tutorial - low prerequisites, straightforward concepts.

Trees are the “just enough edges” graphs: they connect everything without ever looping back. That simple idea powers file systems, organization charts, search structures, network design, and many algorithms.

TL;DR:

A **tree** is a connected, acyclic (cycle-free) undirected graph. This is equivalent to saying there is a **unique simple path** between any two vertices, and also equivalent to having exactly **|E| = |V| − 1** edges. If you pick a **root**, the tree becomes a **rooted tree** with parent/child relationships; **leaves** are nodes with no children.

## What Is a Tree?

### Why trees matter

In graphs, you often face a tension:

- •You want **connectivity** (everything can reach everything).
- •But extra edges can create **cycles**, which can cause redundancy, ambiguity in “the path,” and algorithmic overhead.

A **tree** hits a sweet spot: it’s connected, but it has *no cycles*. That means it has exactly the minimum number of edges needed to stay connected.

### Definition (undirected)

A **tree** is an undirected graph G=(V,E)G = (V, E)G=(V,E) such that:

1) **Connected**: for any vertices u,v∈Vu, v \in Vu,v∈V, there exists a path between them.

2) **Acyclic**: there is no cycle (no closed loop of distinct vertices/edges).

You can think of a tree as a structure where edges form “branches” that never loop back.

### A quick intuition

Imagine building a network by adding edges one at a time:

- •If you start with nnn isolated vertices, you have nnn connected components.
- •Each time you add an edge **between two different components**, you reduce the component count by 1.
- •If you ever add an edge **within the same component**, you create a cycle.

A tree is exactly the state where:

- •you’ve reduced components down to 1 (connected),
- •and you never created a cycle.

### Key equivalences (the “triangle” to remember)

For a finite undirected graph G=(V,E)G = (V, E)G=(V,E), the following are equivalent:

1) GGG is a **tree** (connected + acyclic)

2) There is a **unique simple path** between any two vertices

3) GGG is connected and has exactly $∣E∣=∣V∣−1|E| = |V| - 1∣E∣=∣V∣−1$

These equivalences are not trivia—they’re the fastest way to *recognize* and *reason about* trees.

### Visualization idea for an interactive canvas (recommended)

Use toggles/buttons:

- •**Add edge** (choose endpoints)
- •**Remove edge**

And live indicators:

- •**|V|, |E|**
- •**Component count**
- •**Cycle detector** (highlight cycle edges in red)
- •**Unique path check** (click two nodes → highlight the path; if multiple paths exist, show both)

This setup reinforces the key equivalences:

- •Adding an edge in a connected tree forces a cycle.
- •Removing any edge in a tree disconnects it.
- •As long as you have connected + ∣E∣=∣V∣−1|E|=|V|-1∣E∣=∣V∣−1, you must have no cycles.

## Core Mechanic 1: Connected + Acyclic ⇔ Unique Path ⇔ |E| = |V| − 1

This section is the backbone. Trees are simple because three different “views” all describe the same object.

## A. Why “no cycles” gives unique paths

Assume GGG is connected and acyclic.

Take any two vertices uuu and vvv.

- •Because the graph is connected, **at least one** path exists.
- •Suppose there were **two different simple paths** from uuu to vvv.

Then those two paths must diverge at some point and rejoin later, forming a loop—i.e., a **cycle**. That contradicts acyclic.

So in a connected acyclic graph, the path between any two vertices is **unique**.

**Key intuition:**

- •*Multiple routes between the same two nodes* implies there’s a way to go out along one route and come back along another → a cycle.

## B. Why unique paths forbid cycles

Now assume between any two vertices there is a **unique** simple path.

- •If a cycle existed, pick two vertices on that cycle.
- •Going around the cycle clockwise vs counterclockwise gives **two different simple paths** between the same vertices.

Contradiction. So there can be no cycles.

## C. Where does |E| = |V| − 1 come from?

This is the “edge counting” signature of trees.

### Claim

If GGG is a tree with n=∣V∣n = |V|n=∣V∣ vertices, then it has exactly ∣E∣=n−1|E| = n - 1∣E∣=n−1 edges.

### Proof idea (slow and intuitive)

Start from a single vertex:

- •With $1$ vertex, a tree has $0$ edges.

Now imagine building any tree by adding one new vertex at a time.

- •To keep the graph connected, each new vertex must be connected by **at least one** edge.
- •To avoid creating a cycle, that new vertex cannot connect with **two** edges into the existing connected structure.

So each time you add a vertex, you add **exactly one** edge.

After adding up to nnn vertices:

- •edges = (n−1)(n - 1)(n−1)

### A more “component count” perspective

Let’s start with nnn isolated vertices. Components = nnn.

Each edge that connects two different components reduces components by 1.

To reach 1 component, you must reduce by (n−1)(n - 1)(n−1), requiring at least (n−1)(n - 1)(n−1) edges.

A tree is cycle-free, meaning you *never* waste an edge inside a component. So it uses exactly (n−1)(n - 1)(n−1) edges.

## D. Two “surgery” facts (great for visualization)

These are extremely useful and very testable in an interactive canvas.

### Fact 1: Add an edge to a tree ⇒ exactly one cycle appears

Let TTT be a tree. Pick any two vertices u,vu, vu,v.

- •In a tree there is a **unique** path from uuu to vvv.
- •If you add the edge (u,v)(u, v)(u,v), you create a loop: that path plus the new edge.

So one extra edge over ∣V∣−1|V|-1∣V∣−1 forces a cycle.

### Fact 2: Remove any edge from a tree ⇒ it disconnects

Take any edge eee in a tree.

- •Because paths are unique, that edge lies on the unique path between its endpoints.
- •Removing it destroys that only route.

So every edge is a **bridge** (a cut edge) in a tree.

## E. A compact equivalence summary

For a finite undirected graph, any two of the following imply the third:

- •connected
- •acyclic
- •∣E∣=∣V∣−1|E| = |V| - 1∣E∣=∣V∣−1

This is a powerful “tree detector.”

### Mini-table: how to use the equivalences

| What you know | Fast conclusion |
| --- | --- |
| connected + acyclic | it’s a tree; unique paths; $ | E | = | V | -1$ |
| connected + $ | E | = | V | -1$ | must be acyclic → tree |
| acyclic + $ | E | = | V | -1$ | must be connected → tree |

(That last row surprises people: if you have no cycles and still have n−1n-1n−1 edges, you can’t afford to be disconnected.)

## Core Mechanic 2: Rooted Trees (Parent/Child) and Leaves

So far, trees were **undirected**: edges have no orientation. Many applications (hierarchies, parsing, search) need direction—so we pick a **root**.

## A. Rooted tree: turning an undirected tree into a hierarchy

A **rooted tree** is a tree with one distinguished vertex called the **root** (often written rrr).

Once you choose a root, every other vertex xxx has:

- •a unique path from rrr to xxx (because the underlying graph is a tree)
- •therefore a unique **previous** vertex on that path

That previous vertex is the **parent**.

### Parent function

For a rooted tree with root rrr:

- •parent(r)\text{parent}(r)parent(r) is **undefined** (or sometimes set to null)
- •for any x≠rx \neq rx=r, parent(x)\text{parent}(x)parent(x) is the neighbor of xxx on the unique path from rrr to xxx

You can define it formally:

- •Let the unique path from rrr to xxx be (r=v0,v1,…,vk=x)(r = v\_0, v\_1, \dots, v\_k = x)(r=v0​,v1​,…,vk​=x).
- •Then $parent(x)=vk−1.\text{parent}(x) = v\_{k-1}.parent(x)=vk−1​.$

## B. Children, ancestors, descendants

Once parent is defined:

- •yyy is a **child** of xxx if parent(y)=x\text{parent}(y) = xparent(y)=x.
- •xxx is an **ancestor** of yyy if xxx lies on the path from rrr to yyy.
- •yyy is a **descendant** of xxx if xxx is an ancestor of yyy.

These relationships are not extra edges—they are *interpretations* of the same undirected structure after choosing a root.

## C. Leaves

A **leaf** (in a rooted tree) is a node with **no children**.

Important subtlety:

- •In an **undirected** tree, a leaf is usually defined as a vertex of degree 1 (when ∣V∣>1|V|>1∣V∣>1).
- •In a **rooted** tree, “leaf” depends on orientation: it means no children.

These align nicely when the root is not isolated:

- •A vertex of degree 1 in the undirected sense will be a leaf for any root not equal to that vertex.
- •The root can be a leaf only in the degenerate 1-vertex tree.

## D. Depth and height (useful derived notions)

With a root, you can measure “how far down” nodes are.

- •**Depth** of a node xxx: number of edges on the path from rrr to xxx.
- •**Height** of the rooted tree: maximum depth of any node.

These quantities matter in algorithmic runtime (e.g., searching a deep tree can be costly).

## E. Visualization hooks for rooted trees

On an interactive canvas:

- •Add a “Choose root” tool: click a vertex to mark it as root.
- •Automatically orient edges away from root (draw arrows or place parent pointers).
- •When you click a node xxx, display:
- •parent(x)\text{parent}(x)parent(x)
- •list of children
- •depth
- •Highlight leaves in a distinct style.

This makes the idea of “parent(x) is defined by the unique path to root” concrete.

## Applications and Connections

Trees show up whenever you want **structure without ambiguity**.

## A. Modeling hierarchies

- •File systems: folders contain subfolders/files (a rooted tree if you ignore links).
- •Organization charts: manager (parent) → reports (children).
- •Taxonomies: category/subcategory relationships.

Root choice is natural here (CEO, root directory, etc.).

## B. Algorithm design on trees

Trees are friendly because:

- •Unique paths simplify reasoning.
- •Many problems become solvable with DFS/BFS in linear time O(∣V∣)O(|V|)O(∣V∣).

Typical tasks:

- •compute depths, parents
- •find lowest common ancestor (later topic)
- •dynamic programming on trees (later topic)

## C. Relationship to spanning trees (preview)

Given a connected graph with cycles, a **spanning tree** is a subgraph that:

- •includes all vertices
- •is a tree (so it has ∣V∣−1|V|-1∣V∣−1 edges)

So a spanning tree is what you get when you “remove enough edges to break all cycles but keep connectivity.”

This connects directly to **Minimum Spanning Trees** (MST): among all spanning trees, choose minimum total weight.

## D. Relationship to Disjoint Sets (Union-Find) (preview)

Union-Find helps track connected components as you add edges.

That aligns perfectly with the “tree building” view:

- •Each edge connecting two components reduces component count.
- •An edge within a component creates a cycle.

That’s exactly what Kruskal’s MST algorithm uses Union-Find to detect.

## E. Trees as data structures (preview)

When you restrict the shape or labeling of a rooted tree, you get powerful data structures:

- •**Binary Trees**: each node has ≤ 2 children.
- •**Tries**: edges labeled by characters; paths represent strings.

These will reuse the parent/child/leaf vocabulary heavily.

## Worked Examples (3)

### Example 1: Is this graph a tree? (Edge/vertex count + cycle/connected check)

Consider the undirected graph with vertices V = {A, B, C, D, E, F} and edges:

E = { (A,B), (B,C), (C,D), (D,E), (E,F) }.

We will verify it is a tree using multiple equivalent characterizations and show how a single edge addition breaks it.

1. Step 1: Count vertices and edges.

   |V| = 6 (A through F)

   |E| = 5
2. Step 2: Check the edge-count signature.

   Compute |V| − 1 = 6 − 1 = 5.

   We have |E| = 5 = |V| − 1.

   This is consistent with being a tree, but not sufficient alone unless we also know connected (or acyclic).
3. Step 3: Check connectedness.

   From A you can reach B, then C, then D, then E, then F.

   So every vertex is reachable from A → graph is connected.
4. Step 4: Conclude it’s a tree.

   We have connected + |E| = |V| − 1 ⇒ it must be acyclic.

   Therefore the graph is a tree.
5. Step 5: Demonstrate the “add an edge ⇒ cycle” fact.

   Add one new edge (B,E).

   Because the original graph is a tree, there is a unique path from B to E:

   B → C → D → E.

   Adding (B,E) creates a cycle:

   B → C → D → E → B.

   Now it is no longer a tree.

**Insight:** The fastest practical test for a finite graph is: if it’s connected and has |E| = |V| − 1, it’s a tree. The interactive takeaway: adding any extra edge to a tree creates exactly one cycle, which you can highlight as “unique path between endpoints + new edge.”

### Example 2: Rooting a tree and computing parent(x), children, and leaves (with diagram)

We have this undirected tree (edges shown). We will choose a root and compute parent(x) for all nodes.

Inline diagram:

A

B

/ \

C D

/ \

E F

Edges: (A,B), (B,C), (B,D), (D,E), (D,F).

Choose root r = A.

1. Step 1: Identify the root.

   Root r = A.

   By definition, parent(A) is undefined.
2. Step 2: Find parent of B.

   The unique path from A to B is A → B.

   So parent(B) = A.
3. Step 3: Find parent of C.

   Unique path A → B → C.

   So parent(C) = B.
4. Step 4: Find parent of D.

   Unique path A → B → D.

   So parent(D) = B.
5. Step 5: Find parent of E and F.

   Unique path A → B → D → E ⇒ parent(E) = D.

   Unique path A → B → D → F ⇒ parent(F) = D.
6. Step 6: List children of each node.

   Children(A) = {B}

   Children(B) = {C, D}

   Children(D) = {E, F}

   Children(C) = ∅, Children(E) = ∅, Children(F) = ∅
7. Step 7: Identify leaves (rooted definition: nodes with no children).

   Leaves are C, E, F.

   (They are also degree-1 nodes in the undirected sense.)

**Insight:** Choosing a root doesn’t change the underlying edges—it changes your viewpoint. parent(x) is not arbitrary: it is forced by the unique path to the root. Leaves become visually obvious when you orient edges away from the root and look for nodes with no outgoing child edges.

### Example 3: Using “remove an edge ⇒ disconnect” to reason about connectivity

Take the rooted tree from Example 2. Remove edge (B,D). What happens to the graph? Which nodes become unreachable from the root A?

1. Step 1: Recall the structure.

   A—B connects to C and D; D connects to E and F.
2. Step 2: Remove edge (B,D).

   This deletes the only connection between the set {D,E,F} and the set {A,B,C}.
3. Step 3: Use the tree property (unique paths / bridges).

   In a tree every edge is a bridge: removing it disconnects the graph into exactly two components.
4. Step 4: Identify components after removal.

   Component 1: {A, B, C}

   Component 2: {D, E, F}
5. Step 5: Reachability from root A.

   From A you can reach B and C.

   You can no longer reach D, E, or F.

**Insight:** In general graphs, removing an edge might not matter (there could be alternate routes). In trees, edges are never redundant: remove one edge and you always lose connectivity.

## Key Takeaways

- ✓

  A **tree** is an undirected graph that is **connected** and **acyclic** (has no cycles).
- ✓

  For finite graphs, these are equivalent: connected+acyclic ⇔ **unique simple path** between any two vertices ⇔ **|E| = |V| − 1** (with connectedness).
- ✓

  A tree has the minimum number of edges needed to stay connected: with nnn vertices it has exactly n−1n−1n−1 edges.
- ✓

  Adding one edge to a tree creates **exactly one** cycle; removing any edge from a tree **disconnects** it.
- ✓

  A **rooted tree** is a tree with a distinguished root; the root induces parent/child directions without changing the underlying edges.
- ✓

  For x≠rx \ne rx=r, parent(x)\text{parent}(x)parent(x) is the neighbor just above xxx on the unique path from the root to xxx; parent(r)\text{parent}(r)parent(r) is undefined.
- ✓

  A **leaf** in a rooted tree is a node with **no children** (often matching degree-1 vertices in the undirected view).

## Common Mistakes

- ✗

  Thinking a tree must be drawn like a botanical tree (with a top and bottom). Trees are graphs; layout is arbitrary.
- ✗

  Assuming ∣E∣=∣V∣−1|E| = |V| − 1∣E∣=∣V∣−1 alone guarantees a tree. You also need connectedness (or acyclicity).
- ✗

  Confusing undirected-degree leaves (degree 1) with rooted leaves (no children) without checking which definition is being used.
- ✗

  Treating parent(x) as an extra label you can choose freely; in a rooted tree, parent(x) is determined by the unique path to the root.

## Practice

easy

You have an undirected graph with |V| = 8 and |E| = 7. You also know it is acyclic. Must it be a tree? Explain.

**Hint:** Use the equivalence: acyclic + |E| = |V| − 1 ⇒ connected.

Show solution

Yes. Since |E| = |V| − 1 (7 = 8 − 1) and the graph is acyclic, it cannot be disconnected. If it were disconnected into k ≥ 2 components, each component being acyclic would be a tree/forest component with at most (|Vᵢ| − 1) edges, giving total edges ≤ (|V| − k) ≤ |V| − 2, contradiction. Therefore it is connected and acyclic, hence a tree.

medium

In a tree with 10 vertices, how many edges are there? If you add 3 new edges (between existing vertices), what is the minimum number of cycles created?

**Hint:** Trees have |E| = |V| − 1. Also, each added edge to a tree creates exactly one cycle (though cycles can share edges).

Show solution

A tree with 10 vertices has 9 edges. Adding 3 edges creates at least 3 cycles: each added edge closes a unique cycle with the pre-existing unique path between its endpoints. So the minimum number of cycles created is 3.

medium

Given the rooted tree below, compute parent(x) for all nodes and list the leaves.

R

/ \

A B

/ \

C D

\

E

Edges: (R,A), (R,B), (B,C), (B,D), (D,E). Root is R.

**Hint:** parent(x) is the previous node on the unique path from R to x. Leaves have no children.

Show solution

parent(R) undefined.

parent(A)=R.

parent(B)=R.

parent(C)=B.

parent(D)=B.

parent(E)=D.

Children: R→{A,B}, B→{C,D}, D→{E}.

Leaves (no children): A, C, E.

## Connections

Unlocks and next steps:

- •[Binary Trees](/tech-tree/binary-trees/)
- •[Minimum Spanning Trees](/tech-tree/minimum-spanning-trees/)
- •[Disjoint Sets](/tech-tree/disjoint-sets/)
- •[Tries](/tech-tree/tries/)

Related prerequisite:

- •Graph basics (vertices/edges, directed vs undirected) from your earlier node.

Quality: A (4.4/5)

[← back to tree](/tech-tree/)[browse all →](/tech-tree/inventory/)
