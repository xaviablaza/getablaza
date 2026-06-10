---
title: Disjoint Sets
description: Union-Find structure. Near-constant time union and find.
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
permalink: /tech-tree/disjoint-sets/
---

[←Back to Tech Tree](/tech-tree/)

[inventory](/tech-tree/inventory/)[coverage](/tech-tree/coverage/)

# Disjoint Sets

Data StructuresDifficulty: ★★★☆☆Depth: 4Unlocks: 0

Union-Find structure. Near-constant time union and find.

## Interactive Visualization

⏮◀◀▶▶STEP0.25x1xZOOM

t=0s

## Core Concepts

- -Disjoint partition: every element belongs to exactly one non-overlapping set
- -Representative (root): each set has a canonical representative (a root node) that identifies membership
- -Efficiency heuristics: path compression and union by rank/size keep trees shallow, giving near-constant amortized time

## Key Symbols & Notation

parent[x] - pointer/index of x's parent (equals x if x is a root)rank[x] - heuristic measure (approximate tree height) used to decide which root becomes parent

## Essential Relationships

- -find(x) follows parent pointers to the root (optionally compressing the path); union(a,b) uses find to get roots and links one root's parent to the other, updating rank to preserve shallow trees

## Prerequisites (2)

[Trees5 atoms](/tech-tree/trees/)[Amortized Analysis5 atoms](/tech-tree/amortized-analysis/)

Advanced Learning Details

### Graph Position

55

Depth Cost

0

Fan-Out (ROI)

0

Bottleneck Score

4

Chain Length

### Cognitive Load

6

Atomic Elements

34

Total Elements

L2

Percentile Level

L4

Atomic Level

### All Concepts (14)

- - Disjoint-set (union-find) as a data structure representing a partition of a universe into disjoint sets (equivalence classes)
- - Representative (leader, canonical element) of a set: one distinguished element that identifies the whole set
- - makeSet(x): operation that creates a new singleton set containing x
- - find(x): operation that returns the representative (root) of the set containing x
- - union(x, y): operation that merges the sets containing x and y into a single set
- - Representation of each set as a rooted tree and the whole structure as a forest of such trees
- - Parent-pointer representation: each node stores a pointer to its parent; the root is its own parent (or has a null parent)
- - Union-by-rank heuristic: when linking two roots, attach the root with smaller rank under the root with larger rank to keep trees shallow
- - Union-by-size heuristic (alternative): when linking, attach the smaller tree under the larger tree (stores sizes instead of ranks)
- - Rank: an auxiliary integer stored at a root that acts as an upper bound/approximation of tree height (not necessarily exact height)
- - Path compression heuristic: during find, update visited nodes' parent pointers to point directly to the root, flattening the tree
- - Idempotence/no-op union: union of two elements already in the same set leaves the partition unchanged
- - Invariant: each tree's root uniquely identifies its entire tree (all descendants belong to the same set)
- - Connectivity test via find: determining whether two elements are in the same set by comparing their representatives

### Teaching Strategy

Multi-session curriculum - substantial prior knowledge and complex material. Use mastery gates and deliberate practice.

You’re repeatedly asked questions like “Are a and b in the same group?” while also merging groups over time. Disjoint Sets (Union-Find) is the classic structure that makes those queries fast—so fast that in practice it feels constant-time even for huge inputs.

TL;DR:

Disjoint Sets (Union-Find) maintains a partition of elements into non-overlapping sets. It supports

- •find(x): return a representative (root) of x’s set
- •union(a, b): merge the sets containing a and b

With **path compression** + **union by rank/size**, a sequence of m operations on n elements runs in O(m α(n)) time (α is inverse Ackermann), which is “near-constant” amortized.

## What Is Disjoint Sets? (Union-Find)

### Why this data structure exists

Many problems evolve by **merging** groups and asking **connectivity** questions:

- •Social networks: do two users belong to the same community after a sequence of friend links?
- •Graph algorithms: does adding an edge create a cycle?
- •Clustering: merge clusters and query membership.

A naive approach stores each set explicitly (like a list). Then:

- •**Union** might require relabeling many elements (slow).
- •**Find** might require searching (slow).

Union-Find is designed for exactly this pattern: **lots of operations**, interleaving unions and queries, where we want each operation to be almost constant time.

### The core abstraction: a disjoint partition

We maintain a collection of sets S₁, S₂, … such that:

- •Every element belongs to **exactly one** set.
- •Sets are **non-overlapping**: Sᵢ ∩ Sⱼ = ∅ for i ≠ j.
- •Their union is the whole universe U: ⋃ᵢ Sᵢ = U.

This is a **partition** of U.

### The key idea: each set has a representative (root)

Instead of storing full sets, we store **parent pointers** that form a forest of rooted trees.

- •Each element x has a pointer parent[x].
- •If parent[x] = x, then x is a **root**.
- •Each root represents one set.

The representative (root) is a canonical “name” for the set. Two elements are in the same set iff they have the same root.

Formally, define:

- •find(x) = the root you reach by following parent pointers from x.
- •x and y are connected ⇔ find(x) = find(y).

### What operations we support

We typically implement three operations:

1) **make-set(x)**

- •Create a new singleton set {x}.
- •parent[x] = x.

2) **find(x)**

- •Return the representative root of x’s set.

3) **union(a, b)**

- •Merge the sets containing a and b.
- •After union, all elements that were in either set are now in one set.

### Data stored (common variant)

We’ll use these arrays:

- •parent[x]: index/pointer to x’s parent; root points to itself.
- •rank[x] (or size[x]): heuristic info to keep trees shallow.

Rank is an **estimate** of tree height; size is exact set size. Either supports good performance when used correctly.

### A small picture in words

Suppose we have elements 1..7. Initially each is its own root.

After unions, we might have:

- •parent[1]=2, parent[2]=2 (2 is root)
- •parent[3]=2
- •parent[4]=5, parent[5]=5 (5 is root)
- •parent[6]=5
- •parent[7]=7 (alone)

Then:

- •find(1)=2, find(3)=2 ⇒ same set
- •find(4)=5, find(7)=7 ⇒ different sets

Union-Find’s entire job is to maintain this forest efficiently as it changes.

## Core Mechanic 1: Trees of Parent Pointers and the Find Operation

### Why find() is the heart of Union-Find

Every union needs to know which sets it is merging, and every connectivity query needs to know whether two elements share a set. Both tasks reduce to a single primitive:

> **Find the representative root**.

Without optimizations, find(x) just walks up parent pointers:

- •x → parent[x] → parent[parent[x]] → … until a root r where parent[r] = r.

That is correct—but could be slow if trees get tall.

### Correctness invariant

Union-Find maintains this invariant:

- •The parent pointers form a forest of directed edges toward roots.
- •Each connected component (tree) has exactly one root r with parent[r] = r.
- •The set represented by r is exactly the nodes in that tree.

As long as union() only links **root to root**, and never creates cycles, the forest remains valid.

### Baseline find implementation

Pseudocode (conceptually):

- •find(x):
- •while parent[x] ≠ x:
- •x = parent[x]
- •return x

This runs in O(h), where h is the height of x’s tree. If h becomes O(n), find becomes O(n) and everything collapses.

### Path compression: the “secret sauce” for find

**Motivation:** If we frequently call find(x), it’s wasteful to traverse the same long path over and over.

**Path compression** flattens the tree during find:

- •After computing the root r, we rewire every node visited to point directly to r.

In a recursive form:

find(x):

- •if parent[x] = x: return x
- •parent[x] = find(parent[x])
- •return parent[x]

Now, the next time we call find on any of those nodes, it returns quickly.

### What path compression does (and does not do)

- •It does **not** change which elements are in which set.
- •It **does** change the internal shape of the tree, usually making it much shallower.

Important subtlety: path compression alone already helps a lot, but to get the famous near-constant bound we pair it with a good union rule (next section).

### A step-by-step mental model

Suppose we have a chain:

- •1 → 2 → 3 → 4 → 5 (root)

Calling find(1) without compression visits 1,2,3,4,5.

With path compression, after find(1):

- •1 → 5
- •2 → 5
- •3 → 5
- •4 → 5
- •5 → 5

Now find(2) is essentially O(1).

### Complexity intuition (amortized)

Path compression can make one find operation do extra work (rewiring pointers), but that work pays off later.

Over a long sequence of operations, the total cost is tiny per operation. The formal result (when combined with union by rank/size) is:

- •m operations on n elements cost O(m α(n))

where α(n) is the inverse Ackermann function.

For any realistic n (even n ≈ 10²⁰), α(n) ≤ 5. So in practice, Union-Find behaves like constant time.

### Implementation detail: iterative path compression

Some environments avoid recursion. You can still compress paths iteratively in two passes:

1) Walk up to find the root.

2) Walk again and set each visited node’s parent to the root.

Both are common; recursive is compact, iterative avoids stack depth issues.

## Core Mechanic 2: Union by Rank/Size (Keeping Trees Shallow)

### Why union() needs a strategy

A union operation merges two sets. Internally, that means we take two roots r₁ and r₂ and make one the parent of the other.

If we do this carelessly (e.g., always parent[r₂] = r₁), we can create tall trees:

- •union(1,2), union(2,3), union(3,4), … can form a chain.

Tall trees make find slow.

So union must be **disciplined**: always attach the “smaller” or “shallower” tree under the “bigger” or “deeper” one.

### Union by size

Store size[root] = number of nodes in that root’s tree.

Algorithm:

1) r₁ = find(a), r₂ = find(b)

2) if r₁ = r₂: already same set

3) attach smaller to larger:

- •if size[r₁] < size[r₂]: swap
- •parent[r₂] = r₁
- •size[r₁] += size[r₂]

**Why it helps:** each time a node’s tree is attached under another, the size of the resulting tree at least doubles. A node can only be “moved upward” O(log n) times.

### Union by rank

Store rank[root], which approximates tree height.

Algorithm:

1) r₁ = find(a), r₂ = find(b)

2) if r₁ = r₂: return

3) compare ranks:

- •if rank[r₁] < rank[r₂]: swap
- •parent[r₂] = r₁
- •if rank[r₁] = rank[r₂]: rank[r₁] += 1

**Why rank works:** ranks only increase when two equal-rank trees are merged, which is rare per node, and creates a provable bound when combined with path compression.

### Rank vs size: which should you use?

Both are excellent. Rank is slightly more common in textbooks; size can be easier to reason about and gives you set sizes for free.

| Heuristic | Stored value | Union rule | Extra capability | Typical use |
| --- | --- | --- | --- | --- |
| Union by rank | rank[root] ≈ height | attach lower-rank under higher-rank; tie ⇒ increment | none directly | classic DSU |
| Union by size | size[root] = set size | attach smaller size under larger size | can answer component sizes | many contest implementations |

Either one + path compression ⇒ near-constant amortized time.

### The famous time bound (what it really means)

With both heuristics:

- •Total time for m operations on n elements is O(m α(n)).

This is an **amortized** statement:

- •Some single operations might still take longer (especially early on).
- •Averaged across the whole sequence, operations are extremely fast.

### “Near-constant” is not marketing—it's math

α(n) grows so slowly that it’s ≤ 4 for values of n far beyond what you can store in memory.

That’s why Union-Find is one of the few structures where theoretical and practical performance line up remarkably well.

### A careful invariant to keep

Union must connect **roots** to **roots**.

That means union(a,b) should do:

- •r₁ = find(a)
- •r₂ = find(b)
- •parent[r₂] = r₁ (or vice versa)

If you accidentally do parent[a] = b without finding roots, you can break the forest structure and even create cycles, making find incorrect or non-terminating.

## Application/Connection: When and How Disjoint Sets Gets Used

### The pattern: dynamic connectivity under unions

Union-Find shines when:

- •Connections are only **added** (monotonic growth).
- •You need to query whether two elements are connected.

It does *not* directly support efficiently removing connections (dynamic connectivity with deletions is harder).

### Kruskal’s algorithm (Minimum Spanning Tree)

In Kruskal’s algorithm, you sort edges by weight and add them if they don’t create a cycle.

The cycle check is exactly:

- •edge (u,v) is safe iff find(u) ≠ find(v)
- •then union(u,v)

So DSU provides cycle detection quickly, making Kruskal efficient.

### Cycle detection in an undirected graph

As you scan edges:

- •If find(u) = find(v), then u and v are already connected ⇒ adding (u,v) creates a cycle.
- •Otherwise union(u,v).

This is a lightweight way to detect cycles without full DFS each time.

### Connected components as they evolve

Suppose you’re building components from interactions:

- •Each interaction merges components.
- •You can ask at any time whether two nodes are in the same component.

With union by size, you can also answer:

- •“How big is the component containing x?”
- •root = find(x)
- •size[root]

### Percolation / grid connectivity

In an N×N grid, you may open cells and union adjacent open cells.

Queries like “is there a path from top to bottom?” become connectivity checks between virtual nodes representing borders.

### DSU and equivalence relations

Union-Find is a practical way to maintain an equivalence relation ~ over elements:

- •Reflexive: x ~ x (same root)
- •Symmetric: x ~ y ⇒ y ~ x
- •Transitive: x ~ y and y ~ z ⇒ x ~ z

Union operations add equivalences; find queries membership in equivalence classes.

### How it connects to what you already know

You already know:

- •**Trees**: DSU stores a forest of rooted trees.
- •**Amortized analysis**: DSU’s speed guarantee is amortized; single operations can vary, but the sequence is fast.

Think of DSU as a case study where an extremely simple structure (parent pointers) becomes powerful when paired with the right heuristics.

### Implementation checklist (practical)

When writing DSU in code:

- •Initialize: parent[x] = x for all x.
- •Choose one heuristic: rank or size.
- •Always call find() inside union().
- •Use path compression in find().

The resulting code is short, reliable, and performance-friendly.

### A note on vectors and math notation

Union-Find is less about vector math (no **v** or ‖**v**‖ needed here), and more about combinatorial structure. Still, it’s grounded in precise invariants and amortized bounds, which is why it belongs in a core data structures track.

## Worked Examples (3)

### Worked Example 1: Run DSU by hand (with union by rank + path compression)

Elements: {1,2,3,4,5,6}. Start with make-set on all.

We perform operations:

1) union(1,2)

2) union(2,3)

3) union(4,5)

4) find(3)

5) union(3,4)

Track parent[·] and rank[·].

1. Initialization:

   parent[x]=x for x=1..6

   rank[x]=0 for x=1..6
2. 1) union(1,2)

   find(1)=1, find(2)=2 (both roots)

   ranks equal (0 and 0) ⇒ choose 1 as new root

   parent[2]=1

   rank[1]=rank[1]+1=1

   Now: 1 is root of {1,2}
3. 2) union(2,3)

   First find(2):

   - •parent[2]=1, parent[1]=1 ⇒ find(2)=1

   (With path compression, parent[2] already points to 1, so no change.)

   find(3)=3

   Union roots 1 and 3:

   rank[1]=1 > rank[3]=0 ⇒ parent[3]=1

   Now: root 1 represents {1,2,3}
4. 3) union(4,5)

   find(4)=4, find(5)=5

   ranks equal ⇒ parent[5]=4 and rank[4]=1

   Now: root 4 represents {4,5}
5. 4) find(3)

   parent[3]=1, parent[1]=1 ⇒ root is 1

   Path compression step sets parent[3]=1 (already 1)

   So find(3)=1
6. 5) union(3,4)

   find(3)=1

   find(4)=4

   Compare ranks: rank[1]=1, rank[4]=1 (tie)

   Attach one under the other; pick 1 as root:

   parent[4]=1

   Increment rank[1]: rank[1]=2

   Note: node 5 still has parent[5]=4, but 4 now points to 1.

   After this, a future find(5) will compress 5 → 1.

**Insight:** Two ideas are visible here: (1) union by rank prevents systematic growth of height; (2) path compression doesn’t need to run on every node immediately—future find calls gradually flatten the structure, yielding the amortized near-constant cost.

### Worked Example 2: Cycle detection while scanning edges

Undirected graph with vertices {A,B,C,D}. Edges arrive in this order:

( A,B ), ( B,C ), ( C,D ), ( D,A )

Use DSU to detect when a cycle first appears.

1. Initialize:

   parent[A]=A, parent[B]=B, parent[C]=C, parent[D]=D
2. Edge (A,B):

   find(A)=A, find(B)=B ⇒ different

   union(A,B)

   Now A and B are in same set.
3. Edge (B,C):

   find(B)=find(A)=A (after compression)

   find(C)=C ⇒ different

   union(B,C) merges C into {A,B,C}
4. Edge (C,D):

   find(C)=A

   find(D)=D ⇒ different

   union(C,D) merges D into {A,B,C,D}
5. Edge (D,A):

   find(D)=A

   find(A)=A ⇒ same representative

   Therefore adding (D,A) creates a cycle.

   We can report: the first cycle is detected at edge (D,A).

**Insight:** Cycle detection is just a same-set query: an undirected edge (u,v) forms a cycle exactly when u and v are already connected. DSU turns that global graph property into two near-constant-time finds.

### Worked Example 3: Union by size and component size queries

Elements {1,2,3,4,5,6,7}. Use union by size + path compression.

Operations:

union(1,2), union(2,3), union(4,5), union(6,7), union(5,6)

Then query: size of component containing 7.

1. Initialization:

   parent[x]=x

   size[x]=1 for all x
2. union(1,2):

   find(1)=1, find(2)=2

   sizes tie ⇒ choose 1 as root

   parent[2]=1

   size[1]=2
3. union(2,3):

   find(2)=find(1)=1

   find(3)=3

   Attach smaller to larger:

   parent[3]=1

   size[1]=3
4. union(4,5):

   parent[5]=4

   size[4]=2
5. union(6,7):

   parent[7]=6

   size[6]=2
6. union(5,6):

   find(5): parent[5]=4 ⇒ root 4

   find(6)=6

   sizes: size[4]=2, size[6]=2 tie ⇒ pick 4

   parent[6]=4

   size[4]=4

   Now 7 still points to 6, and 6 points to 4.
7. Query size of component containing 7:

   find(7): 7 → 6 → 4 (root)

   Path compression updates parent[7]=4 (and possibly parent[6]=4 already)

   Answer = size[4] = 4

**Insight:** Union by size gives you component sizes essentially for free. Path compression ensures that repeated size queries become extremely fast because nodes quickly learn their true root.

## Key Takeaways

- ✓

  Disjoint Sets maintains a **partition**: each element belongs to exactly one non-overlapping set.
- ✓

  Internally it stores a **forest of rooted trees** using parent[x] pointers; each root is a set representative.
- ✓

  find(x) returns the root representative; two elements are in the same set iff their roots are equal.
- ✓

  Path compression rewires nodes during find to point closer to the root, flattening trees over time.
- ✓

  Union must link **root to root**; otherwise you can break invariants or create cycles.
- ✓

  Union by rank or union by size prevents tall trees by attaching the shallower/smaller tree under the deeper/larger one.
- ✓

  With both heuristics, m operations on n elements take O(m α(n)) time amortized, which is effectively constant in practice.

## Common Mistakes

- ✗

  Forgetting to call find() inside union(), and instead linking a and b directly (can create incorrect structures or cycles).
- ✗

  Updating rank/size on non-root nodes, or failing to update it only on the new root after a merge.
- ✗

  Implementing path compression incorrectly (e.g., compressing to parent[parent[x]] inconsistently) and accidentally skipping necessary updates.
- ✗

  Assuming DSU supports deletions efficiently; standard Union-Find is for merges (unions) and queries, not edge removals.

## Practice

easy

You have elements {1..8}. Perform: union(1,2), union(3,4), union(2,3), union(5,6), union(7,8), union(6,7). After these operations, are 1 and 4 connected? Are 5 and 8 connected?

**Hint:** Connectivity is determined entirely by representatives: check whether find(x) = find(y). You don’t need the exact parent array if you track which components got merged.

Show solution

union(1,2) ⇒ {1,2}

union(3,4) ⇒ {3,4}

union(2,3) merges {1,2} with {3,4} ⇒ {1,2,3,4}

So 1 and 4 are connected.

union(5,6) ⇒ {5,6}

union(7,8) ⇒ {7,8}

union(6,7) merges {5,6} with {7,8} ⇒ {5,6,7,8}

So 5 and 8 are connected.

medium

Consider a DSU using union by rank (no path compression). Prove that the rank of any node is at most ⌊log₂ n⌋, where n is the number of elements.

**Hint:** Rank increases only when two roots of equal rank are merged. Track a lower bound on the size of a tree as a function of its rank.

Show solution

Claim: a root of rank r has at least 2ʳ nodes in its tree.

Base: r=0 ⇒ singleton tree has size 1 = 2⁰.

Inductive step: rank increases from r to r+1 only when two trees of rank r are merged. By induction each has size ≥ 2ʳ, so merged size ≥ 2ʳ + 2ʳ = 2ʳ⁺¹.

Thus size ≥ 2ʳ for rank r. Since size ≤ n, we have 2ʳ ≤ n ⇒ r ≤ log₂ n, so rank ≤ ⌊log₂ n⌋.

medium

In an undirected graph with vertices 1..n, edges arrive one by one. Describe an algorithm using DSU to output the first edge that creates a cycle, or report that no cycle is created after all edges arrive. Give the time complexity in terms of m edges and n vertices.

**Hint:** The cycle condition for an undirected edge (u,v) is that u and v are already connected before adding the edge.

Show solution

Algorithm:

Initialize DSU with make-set(1..n).

For each edge (u,v) in arrival order:

- •if find(u) = find(v): output (u,v) as the first cycle-creating edge and stop.
- •else union(u,v).

If finished without finding such an edge, report “no cycle.”

Time: Each edge does up to two finds and possibly one union. With path compression + union by rank/size, total time is O(m α(n)).

## Connections

Related nodes:

- •[Trees](/tech-tree/trees/)
- •[Amortized Analysis](/tech-tree/amortized-analysis/)
- •[Graph Connected Components](/tech-tree/graph-connected-components/)
- •[Kruskal’s Algorithm (MST)](/tech-tree/kruskals-algorithm/)

Quality: A (4.6/5)

[← back to tree](/tech-tree/)[browse all →](/tech-tree/inventory/)
