---
title: Binary Trees
description: Trees where each node has at most two children.
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
inspiration_url: https://templeton.host/tech-tree/binary-trees/
inspiration_category: tech-tree
---

> Source-copy draft imported from [https://templeton.host/tech-tree/binary-trees/](https://templeton.host/tech-tree/binary-trees/). Names, domain references, and local media paths were adapted for Xavi Ablaza / getablaza.com.

[←Back to Tech Tree](/tech-tree/)

[inventory](/tech-tree/inventory/)[coverage](/tech-tree/coverage/)

# Binary Trees

Graph TheoryDifficulty: ★★☆☆☆Depth: 3Unlocks: 5

Trees where each node has at most two children.

## Interactive Visualization

⏮◀◀▶▶STEP0.25x1xZOOM

t=0s

## Core Concepts

- -At-most-two-children: each node has no more than two child positions
- -Ordered children: the two positions are distinct (left vs right) and their order matters
- -Recursive definition: a binary tree is either empty or a node with a left binary subtree and a right binary subtree

## Key Symbols & Notation

NULL (represents an absent/empty child/subtree)

## Essential Relationships

- -Each node's left and right links independently reference either another binary tree or NULL

## Prerequisites (1)

[Trees5 atoms](/tech-tree/trees/)

## Unlocks (2)

[Heapslvl 2](/tech-tree/heaps/)[Binary Search Treeslvl 2](/tech-tree/bst/)

Advanced Learning Details

### Graph Position

21

Depth Cost

5

Fan-Out (ROI)

2

Bottleneck Score

3

Chain Length

### Cognitive Load

5

Atomic Elements

15

Total Elements

L0

Percentile Level

L3

Atomic Level

### All Concepts (6)

- - Binary tree: a rooted tree in which each node has at most two children (i.e., arity ≤ 2)
- - Ordered child positions: the two child slots are distinguished as 'left' and 'right' (position matters)
- - Left subtree: the subtree rooted at the left child of a node
- - Right subtree: the subtree rooted at the right child of a node
- - Empty child / empty subtree: an explicit missing child (a placeholder/null subtree) occupying a left or right position
- - Node-degree possibilities specific to binary trees: nodes can be unary (one child) or binary (two children) in addition to leaves (zero children)

### Teaching Strategy

Self-serve tutorial - low prerequisites, straightforward concepts.

A tree already gives you “parent/child.” A binary tree adds a surprisingly powerful constraint: every node has exactly two *slots* for children—left and right—and either slot may be empty (NULL). That simple shape rule is the foundation for heaps, binary search trees, expression trees, and many serialization formats.

TL;DR:

A binary tree is defined recursively: it’s either empty (NULL) or a node with a left binary subtree and a right binary subtree. The two child positions are *ordered* (left ≠ right), even if one or both are NULL. This order affects traversals (preorder/inorder/postorder), representations, and algorithms.

## What Is a Binary Tree?

### Motivation (why this concept exists)

When you first learn “trees,” the number of children a node can have is usually unconstrained: a node may have 0, 1, 2, 10… children. Many algorithms and data structures become simpler and faster when you restrict the shape.

A **binary tree** is the most common restriction: each node has *at most two children*. That might seem arbitrary, but it buys you:

- •**Simple recursive structure**: problems split into “solve left subtree” and “solve right subtree.”
- •**Clear, ordered positions**: “left child” and “right child” are distinct roles.
- •**Compact array representations** for special cases (e.g., complete trees → heaps).

### Definition

A **binary tree** is a rooted tree where **each node has at most two children**, and the two child positions are **ordered**.

There are three atomic ideas to keep in your head:

1. 1)**At-most-two-children**: a node can have 0, 1, or 2 children.
2. 2)**Ordered children**: the two slots are distinct: *left* vs *right*. Swapping them generally changes the tree.
3. 3)**Recursive definition**: a binary tree is either empty or a node whose left and right are themselves binary trees.

A common formal recursive definition is:

- •A binary tree is either **empty** (represented by **NULL**), or
- •A node containing a value and two pointers: `left` and `right`, each pointing to a binary tree (or NULL).

In pseudocode, a node is often modeled as:

```
Node {
  value
  left  // Node or NULL
  right // Node or NULL
}
```

### A diagram you should be able to “read”

The key visualization: **each node has two labeled outgoing edges (slots)**, and **NULL is meaningful**.

Here is an inline static SVG diagram labeling left/right pointers and NULL slots:

```
<svg width="650" height="220" viewBox="0 0 650 220" xmlns="http://www.w3.org/2000/svg">
  <style>
    .node { fill: #fff; stroke: #111; stroke-width: 2; }
    .null { fill: #f6f6f6; stroke: #666; stroke-width: 2; stroke-dasharray: 5 4; }
    .lbl { font: 14px sans-serif; fill: #111; }
    .small { font: 12px sans-serif; fill: #333; }
    .edge { stroke: #111; stroke-width: 2; }
    .dedge { stroke: #666; stroke-width: 2; stroke-dasharray: 5 4; }
  </style>

  <!-- root -->
  <circle class="node" cx="325" cy="40" r="22" />
  <text class="lbl" x="325" y="45" text-anchor="middle">A</text>

  <!-- left child -->
  <circle class="node" cx="220" cy="110" r="22" />
  <text class="lbl" x="220" y="115" text-anchor="middle">B</text>

  <!-- right child (NULL) -->
  <rect class="null" x="410" y="88" width="60" height="44" rx="8" />
  <text class="small" x="440" y="115" text-anchor="middle">NULL</text>

  <!-- B's children -->
  <rect class="null" x="155" y="160" width="60" height="44" rx="8" />
  <text class="small" x="185" y="187" text-anchor="middle">NULL</text>

  <circle class="node" cx="285" cy="182" r="22" />
  <text class="lbl" x="285" y="187" text-anchor="middle">C</text>

  <!-- edges -->
  <line class="edge" x1="310" y1="58" x2="236" y2="95" />
  <line class="dedge" x1="340" y1="58" x2="410" y2="95" />

  <line class="dedge" x1="205" y1="128" x2="185" y2="160" />
  <line class="edge" x1="235" y1="128" x2="270" y2="165" />

  <!-- labels for slots -->
  <text class="small" x="265" y="78" text-anchor="middle">left</text>
  <text class="small" x="385" y="78" text-anchor="middle">right</text>

  <text class="small" x="175" y="150" text-anchor="middle">left</text>
  <text class="small" x="260" y="150" text-anchor="middle">right</text>
</svg>
```

Read it like this:

- •Node `A` has:
- •`A.left = B`
- •`A.right = NULL`
- •Node `B` has:
- •`B.left = NULL`
- •`B.right = C`

Notice how “having one child” still means you must decide *which slot* is used. A node with only a right child is different from a node with only a left child.

### Ordered children means swapping changes the tree

If you swap every left and right pointer, you get the tree’s **mirror image**. In general, the original tree and its mirror are *not the same binary tree* (even if they contain the same values).

This is a major difference from some “un-ordered” tree models where children are just a set/list without named positions.

## Core Mechanic 1: Recursive Structure and NULL as a Real Base Case

### Why recursion fits perfectly

Binary trees are defined in terms of smaller binary trees. That means many algorithms naturally look like:

1. 1)Handle the **empty tree** (NULL)
2. 2)Solve for the left subtree
3. 3)Solve for the right subtree
4. 4)Combine results

This is not just programming convenience—it’s a direct consequence of the definition.

### The recursive definition (made explicit)

Let TTT be a binary tree. Then:

- •T=NULLT = \text{NULL}T=NULL (empty), or
- •T=(value,left,right)T = (value, left, right)T=(value,left,right) where `left` and `right` are binary trees.

If you like, you can think of a node as a 3-tuple:

T=(x,TL,TR)T = (x, T\_L, T\_R)T=(x,TL​,TR​)

where TLT\_LTL​ is the left subtree and TRT\_RTR​ is the right subtree, and either may be empty (NULL).

### NULL is not “nothing”; it’s part of the shape

A common beginner mistake is to treat “missing child pointers” as irrelevant. But for binary trees, NULL is what makes the recursive definition work cleanly and what makes many representations unambiguous.

Example: Suppose we want to count nodes.

Let `size(T)` be the number of non-NULL nodes in tree `T`.

We define:

- •If T=NULLT = \text{NULL}T=NULL, then `size(T) = 0`.
- •Otherwise, if TTT has root with left LLL and right RRR:

size(T)=1+size(L)+size(R)\text{size}(T) = 1 + \text{size}(L) + \text{size}(R)size(T)=1+size(L)+size(R)

That “0 for NULL” is the base case that stops recursion.

### Height and depth (and why people mix them up)

Two related measures:

- •**Depth** of a node: number of edges from the root to that node.
- •**Height** of a tree: number of edges on the longest path from the root down to a leaf.

Conventions vary: sometimes height counts nodes instead of edges. Pick one and be consistent.

A recursive height definition (edge-counting) is:

- •`height(NULL) = -1` (so a leaf node has height 0)
- •`height(node) = 1 + max(height(left), height(right))`

This choice is nice because it makes the math clean.

### Interactive-canvas suggestion (visualization focus)

If you’re building or using an interactive canvas for this node, add a toggle that:

- •Shows left/right pointers as **two fixed slots** per node
- •Draws **NULL markers** explicitly (e.g., dashed boxes labeled NULL)
- •Lets learners toggle traversal animations:
- •Preorder (N-L-R)
- •Inorder (L-N-R)
- •Postorder (L-R-N)
- •Lets learners toggle a “**serialize with NULLs**” mode, so they can see output change when NULLs are omitted vs included

A crucial demonstration:

- •Two different trees can produce the **same traversal output** if you omit NULL markers.
- •Adding NULL markers (or parentheses structure) makes the serialization unambiguous.

For example, preorder without NULLs:

- •Tree 1: A with left child B
- •Tree 2: A with right child B

Both produce preorder sequence: `A, B`.

But preorder *with NULL markers* distinguishes them:

- •Tree 1: `A, B, NULL, NULL, NULL`
- •Tree 2: `A, NULL, B, NULL, NULL`

That difference is exactly “ordered child positions + base case.”

## Core Mechanic 2: Traversals (Preorder, Inorder, Postorder) and What They Really Mean

### Why traversals matter

A traversal is a rule for visiting every node exactly once. Traversals are how we:

- •Print or serialize trees
- •Evaluate expression trees
- •Implement many algorithms cleanly

Binary trees have especially standard traversals because “left vs right” gives a built-in order.

### The three depth-first traversals

Assume a node `N` with left subtree `L` and right subtree `R`.

| Traversal | Rule | Mnemonic |
| --- | --- | --- |
| Preorder | Visit N, then L, then R | N-L-R |
| Inorder | Visit L, then N, then R | L-N-R |
| Postorder | Visit L, then R, then N | L-R-N |

You can write them recursively. For preorder:

```
preorder(T):
  if T == NULL: return
  visit(T.root)
  preorder(T.left)
  preorder(T.right)
```

Inorder:

```
inorder(T):
  if T == NULL: return
  inorder(T.left)
  visit(T.root)
  inorder(T.right)
```

Postorder:

```
postorder(T):
  if T == NULL: return
  postorder(T.left)
  postorder(T.right)
  visit(T.root)
```

### Breathing room: what changes between these?

Only one thing: *when* you visit the node relative to its subtrees.

But that one thing changes the meaning:

- •**Preorder**: good for “copying” a tree structure (especially with NULL markers), or prefix notation.
- •**Inorder**: special for **binary search trees** (it yields sorted order). For a general binary tree, it’s just a consistent left-to-right listing.
- •**Postorder**: useful for deleting/freeing nodes, evaluating expression trees in postfix order.

### Traversals + NULL markers = serialization

If your goal is to reconstruct the exact tree shape later, you typically must record NULLs (or use parentheses).

A common preorder-with-NULL serialization scheme:

```
serialize(T):
  if T == NULL: output "NULL"; return
  output T.value
  serialize(T.left)
  serialize(T.right)
```

This produces a sequence that uniquely identifies the tree (given ordered child slots).

### BFS / level-order (bonus, but common)

Level-order traversal visits nodes by depth: root, then all depth-1 nodes left-to-right, then depth-2, etc. This is typically implemented with a queue.

While not part of the classic “three DFS traversals,” level-order is heavily used in heaps and in array representations.

### Visualization note for the interactive canvas

To improve intuition, the canvas should animate a moving “cursor”:

- •Highlight current node
- •Show a call stack panel (or recursion depth) as you traverse
- •In “include NULLs” mode, the animation should also step into missing children and emit a NULL token

Learners should be able to watch preorder vs inorder vs postorder produce different sequences from the same static shape.

## Application / Connection: Representations and Why Binary Trees Enable Heaps and BSTs

### Representation 1: Pointer-based nodes (general binary trees)

The most general representation uses explicit nodes with left/right pointers.

Pros:

- •Supports any shape (sparse trees, skewed trees)
- •Easy to mutate locally

Cons:

- •Memory overhead per node (pointers)
- •Cache locality can be worse than arrays

### Representation 2: Array-based (works best for complete trees)

If a binary tree is **complete** (all levels filled except maybe the last, filled left-to-right), you can store it compactly in an array.

Using 1-based indexing:

- •Node at index iii
- •Left child at $2i$
- •Right child at $2i + 1$
- •Parent at ⌊i/2⌋\lfloor i/2 \rfloor⌊i/2⌋

This is the key trick behind **heaps**.

If the tree is sparse, the array representation wastes space because you’d need many NULL slots.

### Heaps and BSTs: what binary trees unlock

Binary trees are the “host structure.” Additional rules turn them into specialized data structures:

| Structure | Extra rule added | What you get |
| --- | --- | --- |
| Heap | Complete shape + heap-order property | Fast access to min/max, priority queue |
| Binary Search Tree (BST) | For each node, left values < node < right values | Fast search/insert/delete on average |

Binary trees are not automatically fast. A badly shaped (skewed) BST can degrade to a chain with O(n)O(n)O(n) operations. That’s why shape and invariants matter.

### A small but important conceptual bridge

- •**Binary tree** is about **shape + left/right order + NULL base case**.
- •**BST** is about adding a **value ordering invariant** on top of the binary tree.
- •**Heap** is about adding a **shape constraint (complete)** and a **parent/child priority invariant**.

So this node is the “shape vocabulary” you need before learning those invariants.

## Worked Examples (3)

### Compute preorder, inorder, postorder (and see how NULL markers change serialization)

Use the tree from the SVG diagram:

- •A.left = B, A.right = NULL
- •B.left = NULL, B.right = C
- •C.left = NULL, C.right = NULL

1. Preorder (N-L-R):

   Visit A

   → Traverse left subtree (rooted at B)

   Visit B

   → Traverse B.left (NULL) (no output in normal traversal)

   → Traverse B.right (rooted at C)

   Visit C

   → C.left NULL

   → C.right NULL

   → Traverse right subtree of A (NULL)

   Preorder output (without NULLs): A, B, C
2. Inorder (L-N-R):

   Traverse A.left (B):

   Traverse B.left (NULL)

   Visit B

   Traverse B.right (C):

   Traverse C.left (NULL)

   Visit C

   Traverse C.right (NULL)

   Visit A

   Traverse A.right (NULL)

   Inorder output (without NULLs): B, C, A
3. Postorder (L-R-N):

   Traverse A.left (B):

   Traverse B.left (NULL)

   Traverse B.right (C):

   Traverse C.left (NULL)

   Traverse C.right (NULL)

   Visit C

   Visit B

   Traverse A.right (NULL)

   Visit A

   Postorder output (without NULLs): C, B, A
4. Now preorder serialization WITH NULL markers:

   Rule:

   - •If node is NULL: output NULL
   - •Else: output value, then serialize(left), serialize(right)

   Serialize(A):

   Output A

   Serialize(A.left = B):

   Output B

   Serialize(B.left = NULL): output NULL

   Serialize(B.right = C):

   Output C

   Serialize(C.left=NULL): output NULL

   Serialize(C.right=NULL): output NULL

   Serialize(A.right = NULL): output NULL

   Preorder-with-NULL output:

   A, B, NULL, C, NULL, NULL, NULL

**Insight:** Without NULL markers, traversals list values but can lose shape information. Adding NULL makes the recursive structure explicit and makes reconstruction possible.

### Derive a recursive node-count and height on a concrete tree

Consider this binary tree (values don’t matter for counting):

- •Root has two children.
- •Left child is a leaf.
- •Right child has one left child (a leaf) and a NULL right child.

In pointers:

R.left = L

R.right = X

L.left=NULL, L.right=NULL

X.left=Y, X.right=NULL

Y.left=NULL, Y.right=NULL

1. Compute size(T) with:

   size(NULL)=0

   size(node)=1+size(left)+size(right)
2. Compute bottom-up:

   size(L)=1+0+0=1

   size(Y)=1+0+0=1
3. Now size(X)=1+size(Y)+size(NULL)=1+1+0=2
4. Now size(R)=1+size(L)+size(X)=1+1+2=4
5. Compute height(T) (edge-counting) with:

   height(NULL)=-1

   height(node)=1+max(height(left), height(right))
6. Bottom-up:

   height(L)=1+max(-1,-1)=0

   height(Y)=1+max(-1,-1)=0
7. height(X)=1+max(height(Y), height(NULL))=1+max(0,-1)=1
8. height(R)=1+max(height(L), height(X))=1+max(0,1)=2

**Insight:** NULL base cases make recursive definitions precise. Choosing height(NULL) = -1 makes leaves come out to height 0 cleanly under an edge-counting convention.

### Show that left-vs-right matters: two different trees with the same preorder (without NULLs)

Tree T₁: A.left=B, A.right=NULL (B is a leaf)

Tree T₂: A.left=NULL, A.right=B (B is a leaf)

1. Preorder without NULLs for T₁:

   Visit A, then left subtree (B), then right subtree (NULL)

   Output: A, B
2. Preorder without NULLs for T₂:

   Visit A, then left subtree (NULL), then right subtree (B)

   Output: A, B
3. So the same preorder value list does not uniquely identify the tree shape.
4. Preorder WITH NULL markers distinguishes them:

   T₁: A, B, NULL, NULL, NULL

   T₂: A, NULL, B, NULL, NULL

**Insight:** The ordered child slots are real information. If you don’t record NULLs (or equivalent structure markers), you can’t reliably reconstruct the original binary tree.

## Key Takeaways

- ✓

  A binary tree node has at most two child *slots*: left and right; the slots are ordered (left ≠ right).
- ✓

  Binary trees are defined recursively: a tree is either NULL or a node with left and right binary subtrees.
- ✓

  NULL is a meaningful part of the structure and is the base case that powers recursive algorithms.
- ✓

  Preorder, inorder, and postorder differ only in *when* the root is visited, but that changes what the traversal is useful for.
- ✓

  Traversals that omit NULL markers can lose shape information; adding NULL markers (or parentheses) enables unambiguous serialization.
- ✓

  Pointer-based representations handle arbitrary shapes; array-based representations shine for complete trees.
- ✓

  Binary trees are the foundation for heaps (complete + heap property) and BSTs (value ordering invariant).

## Common Mistakes

- ✗

  Treating a node with only a right child as “the same” as a node with only a left child (they are different in an ordered binary tree).
- ✗

  Forgetting to handle NULL in recursive functions, leading to crashes or infinite recursion.
- ✗

  Assuming a traversal list of values uniquely identifies a binary tree without including NULL markers or structure delimiters.
- ✗

  Mixing height conventions (edges vs nodes) without stating which one you’re using.

## Practice

easy

Given a binary tree where root A has left child B and right child C, and B has left child D (all other children are NULL). Write the preorder, inorder, and postorder traversals (without NULL markers).

**Hint:** Draw the shape first. Then apply N-L-R, L-N-R, L-R-N carefully.

Show solution

Tree:

A.left=B, A.right=C

B.left=D, B.right=NULL

C is a leaf

Preorder (N-L-R): A, B, D, C

Inorder (L-N-R): D, B, A, C

Postorder (L-R-N): D, B, C, A

medium

Preorder-serialize the same tree as Exercise 1 using NULL markers, using the rule: output value for a node, and output NULL for empty children, recursing left then right.

**Hint:** Every non-NULL node contributes exactly 1 value token, and every missing child contributes a NULL token. Walk preorder and explicitly emit NULL when you step into an empty subtree.

Show solution

Serialize(A):

A,

Serialize(B):

B,

Serialize(D):

D,

NULL,

NULL,

Serialize(B.right=NULL): NULL,

Serialize(C):

C,

NULL,

NULL

Output:

A, B, D, NULL, NULL, NULL, C, NULL, NULL

medium

Let height(NULL) = -1 and height(node) = 1 + max(height(left), height(right)). Compute the height of a single-node tree (just the root) and of a chain of 3 nodes all linked as left children (a skewed tree).

**Hint:** Work bottom-up: compute the leaf first. A single node has two NULL children.

Show solution

Single-node tree:

Root has left=NULL, right=NULL

height(root)=1+max(-1,-1)=0

3-node left chain: A.left=B, B.left=C, C.left=NULL, C.right=NULL and all rights NULL

height(C)=1+max(-1,-1)=0

height(B)=1+max(height(C)=0, -1)=1

height(A)=1+max(height(B)=1, -1)=2

## Connections

- •Next: [Heaps](/tech-tree/heaps/)
- •Next: [Binary Search Trees](/tech-tree/bst/)
- •Related foundation: [Trees](/tech-tree/trees/)
- •Later: Tree traversals often reappear in [Recursion](/tech-tree/recursion/) and [Stack / Call Stack](/tech-tree/stacks/)

Quality: A (4.4/5)

[← back to tree](/tech-tree/)[browse all →](/tech-tree/inventory/)
