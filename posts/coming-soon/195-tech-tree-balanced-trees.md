---
title: Balanced Trees
description: AVL, Red-Black trees. O(log n) operations guaranteed.
date: '2026-07-01'
scheduled: '2027-01-11'
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
inspiration_url: https://templeton.host/tech-tree/balanced-trees/
inspiration_category: tech-tree
---

> Source-copy draft imported from [https://templeton.host/tech-tree/balanced-trees/](https://templeton.host/tech-tree/balanced-trees/). Names, domain references, and local media paths were adapted for Xavi Ablaza / getablaza.com.

[←Back to Tech Tree](/tech-tree/)

[inventory](/tech-tree/inventory/)[coverage](/tech-tree/coverage/)

# Balanced Trees

Data StructuresDifficulty: ★★★☆☆Depth: 5Unlocks: 0

AVL, Red-Black trees. O(log n) operations guaranteed.

## Interactive Visualization

⏮◀◀▶▶STEP0.25x1xZOOM

t=0s

## Core Concepts

- -Tree rotation (left/right): the single local restructuring that preserves BST in-order and changes local subtree heights
- -Local balance invariant: each node satisfies a small constraint that limits how unbalanced its children can be (AVL: balance factor within {-1,0,1}; Red-Black: node colors combined with equal black-height on root-to-leaf paths)
- -Height bound consequence: those local invariants force tree height = O(log n), so basic BST operations run in O(log n)

## Essential Relationships

- -Rotation preserves BST in-order while updating local heights/black-heights so the balance invariant can be restored

## Prerequisites (2)

[Binary Search Trees5 atoms](/tech-tree/bst/)[Big O Notation6 atoms](/tech-tree/big-o/)

Advanced Learning Details

### Graph Position

58

Depth Cost

0

Fan-Out (ROI)

0

Bottleneck Score

5

Chain Length

### Cognitive Load

4

Atomic Elements

37

Total Elements

L2

Percentile Level

L2

Atomic Level

### All Concepts (18)

- - Self‑balancing tree: a BST that maintains an extra structural invariant to bound height
- - Tree height as a key metric to balance (height of a node/subtree)
- - Balance factor (AVL): numeric difference of heights of a node's children used to detect imbalance
- - AVL balance invariant: every node's balance factor ∈ {-1, 0, +1}
- - AVL rotation cases: single and double rotations classified as LL, RR, LR, RL
- - Rotation operation (left/right): local restructure that preserves BST inorder
- - Rebalancing after AVL insert/delete: where and how rotations are applied to restore AVL invariant
- - Minimum‑nodes‑for‑height recurrence (AVL): recurrence relating min #nodes to height (used to prove height = O(log n))
- - AVL deletion behavior: deletions can propagate imbalances up the tree and may require multiple rebalancing steps
- - Red‑Black tree (RB): a BST with a color bit per node and color-based invariants
- - RB node color attribute: each node is red or black
- - RB invariants (standard): (1) root is black, (2) red nodes have black children (no two consecutive reds), (3) every root→leaf path has same # black nodes
- - Black‑height (bh): number of black nodes on any path from a node down to leaves (used in RB invariant)
- - Rebalancing in RB trees: combination of rotations and recoloring to restore color invariants after insert/delete
- - RB insertion fix‑up: local recoloring/rotations to eliminate red‑red violations
- - RB deletion fix‑up: more complex sequence of recoloring/rotations to restore black‑height balance
- - Tradeoff concept: AVL is more strictly balanced (tighter height bound) while RB has weaker invariant but simpler average fixup behavior
- - Invariant preservation principle: rotations and recolorings must restore balancing invariants while preserving BST key order

### Teaching Strategy

Quick unlock - significant prerequisite investment but simple final step. Verify prerequisites first.

A plain Binary Search Tree (BST) is fast only when it *stays* tree-shaped. Balanced trees are the engineering answer to the worst case: they enforce small local rules so the whole tree can’t silently collapse into a linked list.

TL;DR:

Balanced trees (AVL and Red-Black) maintain a BST plus a local balance invariant. When an insert/delete breaks the invariant, they fix it using a small set of local rotations (and sometimes recoloring). Those local rules imply the height is O(log n), so search/insert/delete are guaranteed O(log n).

## What Is Balanced Trees?

A **Balanced Tree** is a Binary Search Tree that actively prevents itself from becoming too tall.

Why this matters: In a regular BST, search/insert/delete follow one root-to-leaf path. If the tree height is h, these operations take O(h). In the best case h ≈ log₂ n, but in the worst case (inserting sorted keys) h = n − 1, so operations degrade to O(n).

Balanced trees enforce a **local invariant** at each node—some small constraint about the relationship between its children. The key idea is:

- •The invariant is **local** (checkable near one node).
- •When the invariant is violated, we perform a **local repair** (rotation, plus metadata updates).
- •These local constraints are strong enough to force a **global height bound**: h = O(log n).

Two classic families:

1) **AVL trees**

- •Stronger invariant: each node’s left and right subtree heights differ by at most 1.
- •Result: very tightly balanced, excellent lookup performance.

2) **Red-Black trees**

- •Slightly weaker invariant: nodes are colored red/black with rules that limit long chains.
- •Result: still O(log n) height, typically fewer rotations on updates.

Both guarantee O(log n) search/insert/delete, but they trade off *how strict* the balancing is and *how much work* they do to maintain it.

A helpful mental model: balancing is not about making the tree perfectly symmetric—it's about ensuring you never get a long skinny path.

### What “guaranteed O(log n)” really means

If n is the number of keys and the height is h, then:

- •Search: O(h)
- •Insert: O(h) to find the place + O(h) to fix up on the way back up
- •Delete: O(h) to find/remove + O(h) to fix up

Balanced trees ensure h ≤ c · log₂(n + 1) for some constant c.

- •For AVL, c is close to 1.44.
- •For Red-Black, c is at most 2.

So you keep predictable performance even under adversarial insertion orders.

## Core Mechanic 1: Tree Rotations (Local Restructuring Without Breaking Order)

Balanced trees rely on a single surgical tool: the **rotation**.

Why rotations exist: When a subtree becomes too tall on one side, we want to “tilt” it to redistribute height—but we must preserve the BST in-order property:

- •All keys in the left subtree < node key < all keys in the right subtree.

A rotation changes the *shape* while keeping the in-order sequence of keys exactly the same.

### Left rotation

Consider a node x with right child y. A left rotation makes y the parent and x the left child.

Before:

- •x is root of this local subtree
- •y = x.right
- •β = y.left (a subtree)

After rotating left at x:

- •y becomes root
- •x becomes y.left
- •β becomes x.right

Key ordering remains valid because:

- •All keys in x.left are still < x
- •All keys in β are between x and y (so they must live as x.right)
- •All keys in y.right remain > y

### Right rotation

Symmetric: rotate right at y when y has left child x.

Before:

- •y is root
- •x = y.left
- •β = x.right

After rotating right at y:

- •x becomes root
- •y becomes x.right
- •β becomes y.left

### In-order preservation (why it works)

Think in terms of in-order traversal:

For the left rotation case, the in-order order of the local nodes/subtrees is:

- •(x.left), x, (β), y, (y.right)

After rotation, in-order becomes:

- •(x.left), x, (β), y, (y.right)

It’s identical.

### Rotations and heights

Rotations are used because they change subtree heights in a controlled way.

If we define height as:

- •height(null) = −1 (common convention)
- •height(leaf) = 0
- •height(node) = 1 + max(height(left), height(right))

A rotation modifies only a constant-sized region, so height updates are local:

- •After rotation, recompute heights for the two nodes involved (and sometimes ancestors during fix-up).

### Double rotations

Sometimes a single rotation is not enough. Two common cases:

- •**Left-Right (LR)** case: heavy on left child’s right side
- •Rotate left on left child
- •Then rotate right on the node

- •**Right-Left (RL)** case: heavy on right child’s left side
- •Rotate right on right child
- •Then rotate left on the node

These “double rotations” still act locally but correct more complex imbalance patterns.

### Summary table: rotations

| Operation | Trigger pattern | Local effect | Preserves BST order? |
| --- | --- | --- | --- |
| Left rotation | right-heavy at x | promotes x.right | Yes |
| Right rotation | left-heavy at y | promotes y.left | Yes |
| LR (double) | left child is right-heavy | two-step rebalance | Yes |
| RL (double) | right child is left-heavy | two-step rebalance | Yes |

Rotations are the backbone of both AVL and Red-Black trees. The difference is the invariant that tells you *when* to rotate (and what extra metadata to update).

## Core Mechanic 2: Local Balance Invariants (AVL vs Red-Black)

A balanced tree is defined less by rotations and more by the **rule** that determines when rotations are required.

### AVL invariant (balance factor)

AVL trees track a height-based constraint at every node.

Define the **balance factor**:

bf(node) = height(left) − height(right)

AVL requires:

bf(node) ∈ {−1, 0, +1} for every node

Why this helps: If every node’s subtrees differ in height by at most 1, then long skewed chains can’t form.

#### AVL insertion repair (intuition)

Insertion is normal BST insertion first. Then, as you walk back up toward the root, you update heights and check balance factors.

If a node becomes unbalanced, bf becomes ±2, and you fix it using one of four cases:

- •**LL case**: inserted into left subtree of left child → Right rotation
- •**RR case**: inserted into right subtree of right child → Left rotation
- •**LR case**: inserted into right subtree of left child → Left rotation on child, then Right rotation
- •**RL case**: inserted into left subtree of right child → Right rotation on child, then Left rotation

A useful feature: for AVL insertion, after you rebalance at the first unbalanced node on the path upward, the subtree height is restored in a way that often stops further fixes.

#### AVL deletion repair (intuition)

Deletion can reduce heights, which may cause multiple ancestors to become unbalanced. AVL deletion may require rebalancing repeatedly up to the root.

### Red-Black invariant (color + black-height)

Red-Black trees store one extra bit per node: color ∈ {red, black}.

They satisfy (one common formulation):

1) Every node is red or black.

2) The root is black.

3) All leaves (nulls) are black.

4) If a node is red, then both its children are black. (No two consecutive reds.)

5) For any node, every path from that node to any descendant leaf has the same number of black nodes. (Equal **black-height**.)

Why this helps:

- •Rule (4) prevents long red chains.
- •Rule (5) forces a form of uniformity: you can’t have one side with many more black nodes than the other.

Red-Black balancing is looser than AVL. It allows more shape variation, but still guarantees logarithmic height.

### Height bound consequence (the big promise)

Balanced trees work because **local constraints imply global height bounds**.

#### Red-Black height sketch

Let bh be the black-height of the root (number of black nodes on any root→leaf path, excluding null leaf depending on convention).

From rule (4), between black nodes you can have at most one red node. So any root→leaf path has length at most:

h ≤ 2 · bh

Also, a subtree with black-height bh has at least 2ᵇʰ − 1 internal nodes (because each black level must branch enough to maintain that black-height; formally, the minimum-node RB tree of black-height bh is a perfect black-only tree).

So if n ≥ 2ᵇʰ − 1, then:

n + 1 ≥ 2ᵇʰ

log₂(n + 1) ≥ bh

Combine with h ≤ 2 · bh:

h ≤ 2 · log₂(n + 1)

Therefore search/insert/delete are O(log n).

#### AVL height sketch

AVL trees are even tighter. Let N(h) be the minimum number of nodes in an AVL tree of height h.

To minimize nodes for height h, you want children heights to be as small as allowed while still making height h:

- •One child has height h − 1
- •The other has height h − 2

So:

N(h) = 1 + N(h − 1) + N(h − 2)

With base cases:

- •N(−1) = 0
- •N(0) = 1

This is Fibonacci-like growth, implying N(h) grows exponentially in h, so h grows logarithmically in n.

A standard bound is:

h ≤ 1.44 · log₂(n + 2) − 1

The exact constant isn’t the key takeaway; the takeaway is: **AVL forces h = O(log n) via a stricter local rule.**

### AVL vs Red-Black: practical comparison

| Feature | AVL | Red-Black |
| --- | --- | --- |
| Local invariant |  | bf | ≤ 1 | color rules + equal black-height |
| Height bound | tighter (shorter trees) | looser (slightly taller) |
| Search performance | typically slightly better | typically slightly worse |
| Insert/delete fix-up | may do more rotations/height updates | often fewer rotations; recoloring common |
| Typical use | read-heavy workloads, indexing | general-purpose maps/sets in many libs |

Both are excellent. The right choice is often about engineering tradeoffs, not asymptotic complexity.

## Application/Connection: Guaranteeing O(log n) Maps/Sets and Beyond

Balanced trees show up whenever you need an *ordered* collection with predictable performance.

### Ordered maps and sets

Balanced trees implement:

- •Set: insert(x), delete(x), contains(x)
- •Map/dictionary: put(key, value), get(key), remove(key)

But unlike hash tables, they also support order-aware operations efficiently:

- •min/max
- •predecessor/successor
- •range queries: all keys in [a, b]
- •in-order traversal in sorted order

Because height is O(log n):

- •predecessor/successor are O(log n)
- •range query costs O(log n + k), where k is the number of reported elements

### Why not just use hashing?

Hash tables are great for average-case O(1) lookups, but:

- •They don’t maintain sorted order.
- •Range queries are awkward.
- •Worst-case can degrade (depending on hashing and adversarial inputs).

Balanced trees give a clean, deterministic guarantee.

### Where AVL vs Red-Black often appears

- •Many standard libraries implement TreeMap/TreeSet-like structures with Red-Black trees (good all-around performance, simpler rebalancing in practice).
- •AVL trees can be chosen when lookup speed is critical and updates are less frequent.

### Rotations as a general technique

Rotations aren’t only for BSTs. The broader pattern is:

- •Maintain a local invariant
- •When it breaks, apply a constant-sized local transformation

You’ll see this in other data structures (e.g., B-trees have splits/merges; heaps have sift-up/down).

### Performance summary

If a balanced tree maintains height h = O(log n), then:

- •Search: O(log n)
- •Insert: O(log n)
- •Delete: O(log n)
- •Space: O(n)

The “magic” is that the balancing work per operation is bounded by a constant number of rotations per violated node, and the number of visited nodes is proportional to the height.

In other words:

Time(operation) = O(height) = O(log n)

That guarantee is exactly why balanced trees are still a core part of CS—even in a world full of hash tables.

## Worked Examples (3)

### AVL insertion requiring a single rotation (LL case)

Insert keys in this order into an AVL tree: 30, 20, 10. Show how the AVL invariant is restored.

1. Start with empty tree.

   Insert 30:

   - •Tree: 30
   - •height(30) = 0
   - •bf(30) = 0
2. Insert 20 (BST rule: 20 < 30 so it goes left of 30):

   30

   /

   20

   Heights:

   - •height(20) = 0
   - •height(30) = 1 + max(0, −1) = 1

   Balance factors:

   - •bf(20) = 0
   - •bf(30) = height(left) − height(right) = 0 − (−1) = +1 (OK)
3. Insert 10 (10 < 30, 10 < 20 → left of 20):

   30

   /

   20

   /

   10

   Heights bottom-up:

   - •height(10) = 0
   - •height(20) = 1 + max(0, −1) = 1
   - •height(30) = 1 + max(1, −1) = 2

   Balance factors:

   - •bf(20) = 0 − (−1) = +1 (OK)
   - •bf(30) = 1 − (−1) = +2 (violates AVL: must be in {−1,0,1})
4. Classify the imbalance at node 30:

   - •Node 30 is left-heavy.
   - •The insertion was in the left subtree of its left child (30 → 20 → 10).

   This is the **LL case**.
5. Fix with a **right rotation** at 30.

   Before (local):

   30

   /

   20

   /

   10

   After right rotation:

   20

   / \

   10 30
6. Update heights:

   - •height(10) = 0
   - •height(30) = 0
   - •height(20) = 1 + max(0, 0) = 1

   Balance factors:

   - •bf(20) = 0 − 0 = 0
   - •bf(10) = 0
   - •bf(30) = 0

   AVL invariant restored.

**Insight:** A single rotation fixed a global-looking problem (the tree got tall) by repairing the first node whose local balance factor became ±2. That’s the core pattern of AVL rebalancing.

### AVL insertion requiring a double rotation (LR case)

Insert keys: 30, 10, 20 into an AVL tree. Show why a single rotation is not enough and how the LR double rotation works.

1. Insert 30:

   - •Tree: 30
2. Insert 10 (goes left of 30):

   30

   /

   10

   bf(30) = +1 (OK)
3. Insert 20:

   - •20 < 30 so go left
   - •20 > 10 so go right of 10

   Tree:

   30

   /

   10

   \

   20

   Compute heights:

   - •height(20) = 0
   - •height(10) = 1 + max(−1, 0) = 1
   - •height(30) = 1 + max(1, −1) = 2

   Balance factors:

   - •bf(10) = (−1) − 0 = −1 (OK)
   - •bf(30) = 1 − (−1) = +2 (violates)
4. Classify imbalance at 30:

   - •30 is left-heavy.
   - •But insertion happened in the right subtree of its left child (30 → 10 → 20).

   This is the **LR case**.
5. Attempting a single right rotation at 30 would produce:

   10

   \

   30

   /

   20

   This still has imbalance because 30 becomes left-heavy (a zig-zag shape).
6. Correct fix: **double rotation**

   Step 1: left rotate at node 10:

   Before:

   10

   \

   20

   After:

   20

   /

   10
7. Step 2: right rotate at node 30 using new left child 20:

   Before (local):

   30

   /

   20

   /

   10

   After:

   20

   / \

   10 30
8. Update heights:

   - •height(10) = 0
   - •height(30) = 0
   - •height(20) = 1

   All balance factors are 0, AVL invariant holds.

**Insight:** Double rotations resolve a zig-zag by first straightening the child subtree, then rotating the parent. Thinking in shapes (straight vs zig-zag) makes the cases easier to remember than memorizing LL/LR/RL/RR.

### Red-Black height guarantee on a concrete tree

Suppose a Red-Black tree has black-height bh = 4 at the root. Bound its height h and lower-bound the number of internal nodes n.

1. Use the Red-Black property: no red node can have a red child.

   Therefore along any root→leaf path, red nodes can only appear between black nodes.

   So the maximum path length happens when you alternate colors:

   black, red, black, red, ...
2. If the black-height is bh = 4, then there are 4 black nodes on each root→leaf path (by definition of black-height).
3. Between consecutive black nodes, there can be at most 1 red node.

   So the number of red nodes on a longest path is at most 4 (or 3 depending on conventions), but the standard safe inequality is:

   h ≤ 2 · bh
4. Plug in bh = 4:

   h ≤ 2 · 4 = 8
5. Now lower-bound n from black-height.

   A subtree of black-height bh has at least 2ᵇʰ − 1 internal nodes.

   Reason: the minimum-node configuration is when all nodes are black and perfectly balanced, giving a perfect binary tree with bh levels of black nodes.
6. Compute:

   2ᵇʰ − 1 = 2⁴ − 1 = 16 − 1 = 15

   So n ≥ 15

**Insight:** Red-Black trees control height indirectly: black-height forces exponential growth in nodes as bh increases, and the no-consecutive-red rule ensures height is at most twice bh.

## Key Takeaways

- ✓

  Balanced trees prevent BST degeneration by enforcing a **local invariant** at every node.
- ✓

  A **rotation** is a constant-sized transformation that preserves BST in-order order while changing local heights.
- ✓

  AVL trees use **balance factor** bf = height(left) − height(right) and require bf ∈ {−1, 0, +1}.
- ✓

  Red-Black trees use **color rules** and **equal black-height** to enforce logarithmic height with fewer strict constraints.
- ✓

  Local invariants imply global bounds: AVL height is tightly O(log n); Red-Black height satisfies h ≤ 2 · log₂(n + 1).
- ✓

  Search/insert/delete time in these trees is O(height) ⇒ guaranteed O(log n).
- ✓

  AVL often gives slightly faster lookups; Red-Black often gives simpler/faster updates in practice.
- ✓

  The core balancing workflow is: BST operation → detect violated local invariant → repair with rotations (and recoloring for RB).

## Common Mistakes

- ✗

  Thinking a rotation “sorts” nodes: rotations don’t change in-order order; they only reshape pointers locally.
- ✗

  Forgetting to update heights (AVL) or parent pointers after rotations, causing later invariant checks to be wrong.
- ✗

  Mixing up zig-zag vs straight cases (LR/RL vs LL/RR), leading to the wrong rotation sequence.
- ✗

  Assuming Red-Black trees are “almost perfectly balanced”; they can be noticeably less strict than AVL while still being O(log n).

## Practice

medium

AVL practice: Insert 10, 20, 30, 25 into an AVL tree (in that order). Draw the tree after each insertion and show which rotation(s) occur.

**Hint:** After inserting 30 you should see an RR imbalance at 10. After inserting 25, check balance factors on the path from 25 back to the root; look for a zig-zag.

Show solution

After 10,20,30:

- •Insert 10 then 20: bf(10)=−1 OK
- •Insert 30 causes bf(10)=−2 (RR case) ⇒ left rotate at 10

Tree becomes:

20

/ \

10 30

Insert 25:

- •Goes left of 30

Tree:

20

/ \

10 30

/

25

Check bf:

- •bf(30)=+1 OK
- •bf(20)=height(left)=0, height(right)=1 ⇒ bf(20)=−1 OK

No rotation needed.

easy

Rotation reasoning: Prove (by listing in-order sequences) that a right rotation preserves the BST in-order order for the involved nodes/subtrees.

**Hint:** Name the local parts: y as root, x = y.left, and β = x.right. Write in-order before and after using (subtree) placeholders.

Show solution

Before right rotation at y:

- •Structure: x is left child of y; β is right subtree of x.

In-order is: (x.left), x, (β), y, (y.right).

After rotation, x becomes root, y becomes x.right, β becomes y.left.

In-order is: (x.left), x, (β), y, (y.right).

The sequences match, so BST order is preserved.

easy

Red-Black bound: If a Red-Black tree has n = 255 internal nodes, show that its height h is at most 16 using h ≤ 2 · log₂(n + 1).

**Hint:** Compute log₂(n + 1) with n + 1 = 256.

Show solution

n + 1 = 256.

log₂(256) = 8.

So h ≤ 2 · log₂(n + 1) = 2 · 8 = 16.

## Connections

Prerequisites: [Binary Search Trees](/tech-tree/binary-search-trees/), [Big O Notation](/tech-tree/big-o-notation/)

Next natural nodes: [Heaps / Priority Queues](/tech-tree/heaps/), [Hash Tables](/tech-tree/hash-tables/), [B-Trees](/tech-tree/b-trees/), [Order Statistics Trees](/tech-tree/order-statistics-trees/)

Quality: A (4.4/5)

[← back to tree](/tech-tree/)[browse all →](/tech-tree/inventory/)
