---
title: Binary Search Trees
description: Ordered binary trees. O(log n) search, insert, delete.
date: '2026-07-01'
scheduled: '2026-11-14'
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
inspiration_url: https://templeton.host/tech-tree/bst/
inspiration_category: tech-tree
---

> Source-copy draft imported from [https://templeton.host/tech-tree/bst/](https://templeton.host/tech-tree/bst/). Names, domain references, and local media paths were adapted for Xavi Ablaza / getablaza.com.

[←Back to Tech Tree](/tech-tree/)

[inventory](/tech-tree/inventory/)[coverage](/tech-tree/coverage/)

# Binary Search Trees

Data StructuresDifficulty: ★★☆☆☆Depth: 4Unlocks: 1

Ordered binary trees. O(log n) search, insert, delete.

## Interactive Visualization

⏮◀◀▶▶STEP0.25x1xZOOM

t=0s

## Core Concepts

- -Ordering invariant: for every node n, every key in the left subtree < key(n) < every key in the right subtree.
- -Search by comparison: to locate a target key k, compare k with key(n) and recurse left if k < key(n), right if k > key(n), stop if equal or reach null.
- -Local updates preserve the invariant: insertion and deletion are done by local link changes (attach/remove/replace nodes) that maintain the ordering invariant.

## Key Symbols & Notation

key(node) - the key stored in a node

## Essential Relationships

- -The ordering invariant enables comparison-guided traversal: comparisons between a target key and key(node) determine which subtree contains the key and ensure correctness of local insert/delete.

## Prerequisites (1)

[Binary Trees5 atoms](/tech-tree/binary-trees/)

## Unlocks (1)

[Balanced Treeslvl 3](/tech-tree/balanced-trees/)

Advanced Learning Details

### Graph Position

26

Depth Cost

1

Fan-Out (ROI)

1

Bottleneck Score

4

Chain Length

### Cognitive Load

5

Atomic Elements

36

Total Elements

L2

Percentile Level

L3

Atomic Level

### All Concepts (14)

- - Binary Search Tree (BST) invariant: nodes are arranged so that keys in the left subtree are less than the node's key and keys in the right subtree are greater than the node's key
- - Key versus value distinction: each node carries a key used for ordering (and optionally an associated value)
- - Ordered-key comparisons as the basis for navigation and modification (compare target key to node.key to decide direction)
- - BST search algorithm: iterative or recursive compare-and-descend procedure (compare key, go left if smaller, right if larger, stop if equal or null)
- - BST insertion algorithm: locate leaf position using BST search rules and attach new node while preserving the BST invariant
- - BST deletion algorithm: three-case strategy (remove leaf; remove node with one child by replacing it with its child; remove node with two children by replacing key with successor or predecessor and deleting that node)
- - In-order successor and predecessor: the next-larger (successor) and next-smaller (predecessor) keys relative to a node
- - Finding minimum and maximum: min is leftmost node; max is rightmost node
- - Transplant (subtree replacement) helper operation: replace one subtree with another by updating parent/child links (used in deletion implementations)
- - Handling duplicate keys: design choices/policies (disallow duplicates, store duplicates at one side, maintain counts or lists, or use tie-breaker rules)
- - Tree height and its role in performance: definition of tree height as longest root-to-leaf path
- - Balanced vs. degenerate (unbalanced) BST shapes: balanced trees keep height low; degenerate trees behave like linked lists
- - Average-case versus worst-case performance behaviors for BST operations
- - In-order traversal property for BSTs: in-order yields keys in non-decreasing (sorted) order

### Teaching Strategy

Self-serve tutorial - low prerequisites, straightforward concepts.

A binary tree becomes dramatically more useful the moment you add one rule: everything smaller goes left, everything larger goes right. That single ordering invariant is what turns “walk the tree” into fast search, insert, and delete—often in O(log n) time.

TL;DR:

A Binary Search Tree (BST) is a binary tree where, for every node n, all keys in its left subtree are < key(n) and all keys in its right subtree are > key(n). This invariant lets you search by comparing the target with key(n) and choosing exactly one subtree each step. Insertion and deletion are local pointer updates that preserve the invariant; performance is O(h) where h is the tree height (≈ log₂ n when reasonably balanced, but can degrade to O(n) if the tree becomes a chain).

## What Is a Binary Search Tree?

### Why BSTs exist (motivation)

A plain binary tree gives you structure, but not speed: to find a value, you might have to visit many nodes because there’s no guiding rule about where values live.

A **Binary Search Tree (BST)** adds a *global promise* about ordering. With that promise, every comparison tells you which half of the remaining search space to ignore—similar in spirit to binary search on an array, but in a pointer-based tree.

### Definition (the invariant)

Each node stores a key, written as **key(node)**.

A binary tree is a BST if **for every node n**:

- •Every key in the left subtree of n is **< key(n)**
- •Every key in the right subtree of n is **> key(n)**

This is the **ordering invariant**.

A common way to say it more formally:

For all nodes n:

- •∀x ∈ LeftSubtree(n): key(x) < key(n)
- •∀y ∈ RightSubtree(n): key(n) < key(y)

### Local view vs global truth

It’s tempting to think the rule is only about the direct children (left child < parent < right child). But the BST invariant is stronger: it’s about **entire subtrees**.

Example: if key(n) = 10, then every key anywhere in the left subtree (left child, left-left grandchild, etc.) must be < 10.

### What you get “for free”

If the invariant holds, then:

- •Searching is guided: each step discards one whole subtree.
- •In-order traversal visits keys in sorted order.
- •Insert and delete can be done by changing a few links while preserving the invariant.

### Height drives performance

BST operations take time proportional to the height **h** (the longest root-to-leaf path):

- •Search: O(h)
- •Insert: O(h)
- •Delete: O(h)

If the tree is balanced-ish, h ≈ log₂ n, giving O(log n). If it becomes skewed (like a linked list), h ≈ n, giving O(n).

So BSTs are “fast when shaped well,” and this is the main reason balanced BST variants (AVL / Red-Black) exist.

## Core Mechanic 1: Search by Comparison (Guided Descent)

### Why search is efficient

The invariant allows a decision at each node: after comparing the target key k with key(n), you know which subtree could possibly contain k.

If k < key(n), then k cannot be in the right subtree (all keys there are > key(n)).

If k > key(n), then k cannot be in the left subtree (all keys there are < key(n)).

So you follow exactly **one** pointer per level.

### Search algorithm (recursive idea)

Given a node n (starting at the root) and target k:

1. 1)If n is null → not found
2. 2)If k = key(n) → found
3. 3)If k < key(n) → search left subtree
4. 4)If k > key(n) → search right subtree

### Search algorithm (iterative idea)

Iterative search is often preferred in practice to avoid deep recursion:

- •current ← root
- •while current ≠ null:
- •if k = key(current) return current
- •else if k < key(current) current ← current.left
- •else current ← current.right
- •return null

### Complexity reasoning

Let h be the tree height.

- •Each loop/recursive call moves down exactly one level.
- •You can do at most h + 1 node visits.

So search cost is O(h).

When the BST is balanced, h ≈ log₂ n, so search is O(log n).

### A note on duplicates

The strict form of the invariant uses < and >, implying no duplicates.

Real implementations must decide what to do with equal keys. Common policies:

| Duplicate Policy | Invariant tweak | Resulting behavior |
| --- | --- | --- |
| Disallow duplicates | keep strict < and > | insert may reject if key exists |
| Put equals on right | left < node ≤ right | duplicates cluster in right subtree |
| Count duplicates | store (key, count) | structure unchanged; counts tracked |

Whatever you choose, the key is consistency: the search rule must match the insertion rule, or you’ll “lose” keys.

### In-order traversal yields sorted order

The BST invariant implies that an in-order traversal (Left, Node, Right) visits keys in increasing order.

Why? Because:

- •Everything in left subtree is < key(n)
- •Then you visit n
- •Then everything in right subtree is > key(n)

This property is a big reason BSTs are used for ordered sets/maps.

## Core Mechanic 2: Local Updates Preserve the Invariant (Insert & Delete)

### Why local updates matter

BST operations feel “global” (you’re maintaining a sorted structure), but the magic is that you can preserve the global invariant with **local pointer changes**.

You do not reshuffle the entire tree on every insert/delete. You:

- •Walk down via comparisons to find a specific location.
- •Change a small number of links.

That’s the key atomic concept: **local updates preserve the invariant**.

---

## Insertion

### Why insertion is simple

To insert key k, you search for where k *would* be found. When the search hits a null child pointer, that null is the correct place to attach a new node.

Because you followed the BST search rule the whole way down, the final position automatically respects all ancestor constraints.

### Insertion procedure

1. 1)If tree is empty, new node becomes root.
2. 2)Otherwise, start at root.
3. 3)Compare k with key(current):

- •if k < key(current): go left
- •if k > key(current): go right
- •if equal: follow your duplicate policy

4. 4)When the chosen child pointer is null, attach new node there.

### Insertion cost

Insertion walks a root-to-leaf path: O(h).

---

## Deletion

Deletion is the “hard” BST operation because removing a node can disconnect subtrees. The trick is to replace the deleted node with a nearby key that keeps the ordering invariant.

### The three deletion cases

Suppose we want to delete a node n with key(n) = k.

#### Case 1: n has no children (leaf)

- •Just remove it: set the parent’s pointer to null.
- •Invariant remains true because no subtree needs reattachment.

#### Case 2: n has exactly one child

- •Splice n out: link n’s parent directly to n’s only child.
- •The child’s subtree already satisfies the constraints that n satisfied (with respect to ancestors), so the invariant is preserved.

#### Case 3: n has two children

This is the interesting case. If you remove n outright, you’d have two subtrees to reconnect.

Standard solution: replace key(n) with either:

- •the **in-order successor**: the smallest key in n’s right subtree
- •or the **in-order predecessor**: the largest key in n’s left subtree

Then delete that successor/predecessor node (which will fall into Case 1 or Case 2).

### Why successor/predecessor works

Let s be the in-order successor of n. Then:

- •s is in the right subtree of n ⇒ key(s) > key(n)
- •s is the smallest in that right subtree ⇒ there is no key between key(n) and key(s) inside the BST order

So if you replace key(n) with key(s), you maintain:

- •all left-subtree keys are still < new key(n)
- •all right-subtree keys are still > new key(n)

And since s is the **leftmost** node in the right subtree, s has **no left child** (it might have a right child). That makes deleting s easy (Case 1 or Case 2).

### Successor-finding detail

To find successor of node n:

1. 1)Go to n.right
2. 2)Then go left as far as possible

This is O(h) in the worst case, but it’s bounded by the height of the tree.

### Delete cost

Delete does:

- •search to find node: O(h)
- •possibly find successor: O(h)
- •local link updates: O(1)

Overall: O(h).

---

## A brief note on “BST property checks”

A common debugging tool is to verify the invariant by tracking allowable key ranges.

At node n, maintain an interval (low, high) such that:

- •low < key(n) < high

When recursing:

- •left child must be in (low, key(n))
- •right child must be in (key(n), high)

This catches subtle violations that child-only checks miss.

## Applications & Connections (Why BSTs Matter in Real Systems)

### Ordered maps and sets

BSTs naturally implement:

- •**Set**: store unique keys, support contains/insert/delete
- •**Map / dictionary**: store (key → value) pairs, ordered by key

Compared to hash tables:

- •BSTs maintain keys in sorted order (hash tables do not).
- •BSTs support order-based queries efficiently:
- •find minimum/maximum
- •find predecessor/successor
- •iterate in sorted order
- •range query (all keys between a and b)

### Range queries (the “BST superpower”)

Suppose you want all keys in [a, b]. A BST can do this by:

- •descending to where a would be,
- •then doing an in-order traversal but pruning subtrees that fall entirely outside [a, b].

A hash table can’t do this without scanning everything.

### Why balancing is the next node

BSTs promise O(log n) only when height h ≈ log₂ n.

But if you insert already-sorted keys into a plain BST, you get a chain:

- •1, 2, 3, 4, 5 inserted in order
- •every new key goes to the right
- •height becomes h = n

Then search/insert/delete degrade to O(n).

This is exactly what **balanced trees** solve: they add rules (and rotations) to keep h bounded by O(log n) regardless of insertion order.

### Practical take

Plain BSTs are still worth learning because:

- •the invariant is foundational
- •the search path logic is the same in balanced trees
- •delete’s successor/predecessor idea appears everywhere
- •many interview and systems problems reduce to BST reasoning

## Worked Examples (3)

### Search and Insert in a BST (Tracing Comparisons)

Start with a BST containing keys: 8 (root), left child 3, right child 10, and 3 has children 1 and 6. Node 6 has children 4 and 7. (This is a classic example BST.)

Tasks:

1) Search for k = 7.

2) Insert k = 5 using the standard BST insertion rule (no duplicates).

1. 1) Search for k = 7

   - •Start at root: key(root) = 8
   - •Compare: 7 < 8 ⇒ go left to node 3
   - •Compare: 7 > 3 ⇒ go right to node 6
   - •Compare: 7 > 6 ⇒ go right to node 7
   - •Compare: 7 = 7 ⇒ found
2. 2) Insert k = 5

   - •Start at root 8: 5 < 8 ⇒ go left to 3
   - •At 3: 5 > 3 ⇒ go right to 6
   - •At 6: 5 < 6 ⇒ go left to 4
   - •At 4: 5 > 4 ⇒ go right
   - •Right child of 4 is null ⇒ attach new node with key 5 as 4.right
3. Check the invariant locally

   - •New node 5 is in the right subtree of 4, and 5 > 4 (OK)
   - •It is also in the left subtree of 6, and 5 < 6 (OK)
   - •It is in the right subtree of 3, and 5 > 3 (OK)
   - •It is in the left subtree of 8, and 5 < 8 (OK)

   So the global invariant is preserved.

**Insight:** Insertion doesn’t require rearranging existing nodes. The search path itself encodes all the constraints from ancestors, so attaching at the first null pointer automatically preserves the BST ordering invariant.

### Delete a Node with Two Children (Using In-Order Successor)

Use the same BST as before (including the inserted key 5). Delete the node with key 3, which has two children (1 and 6). Use the in-order successor method.

1. Find the node to delete

   - •Start at 8: 3 < 8 ⇒ go left
   - •At 3: found node n with key(n) = 3
2. Identify deletion case

   - •Node 3 has two children: left = 1, right = 6 ⇒ Case 3
3. Find in-order successor s of node 3

   - •Go to right subtree: start at 6
   - •Go left as far as possible:
   - •6.left = 4 ⇒ go to 4
   - •4.left is null ⇒ stop

   So successor s has key(s) = 4
4. Replace key(n) with key(s)

   - •Overwrite node 3’s key with 4
   - •Now the node formerly labeled 3 is labeled 4
   - •The tree still has another node with key 4 (the successor node), which we must delete next
5. Delete the successor node (original key 4)

   - •Successor node 4 has:
   - •left child = null
   - •right child = 5 (because we inserted 5 as 4.right)

   So successor deletion is Case 2 (one child)

   - •Splice it out: set 6.left to 5
6. Sanity check of ordering around the edited area

   - •The node now labeled 4 has left subtree containing 1 (and only 1): 1 < 4 (OK)
   - •Its right subtree root is 6, and 6 > 4 (OK)
   - •Under 6, left child is now 5: 5 < 6 and also 5 > 4 (OK)

   Invariant preserved.

**Insight:** Deleting a two-child node is reduced to deleting a one-child/leaf node by swapping with the in-order successor (or predecessor). The successor is chosen specifically because it sits at the boundary between “still bigger than the node” and “as small as possible,” keeping the BST invariant intact.

### Why Height Matters: Same Keys, Different Runtime

Consider inserting the same keys {1, 2, 3, 4, 5} into a plain BST in two different orders:

A) 1, 2, 3, 4, 5

B) 3, 1, 4, 2, 5

Compare resulting height h and search cost for key 5.

1. A) Insert in sorted order: 1,2,3,4,5

   - •1 becomes root
   - •2 goes right of 1
   - •3 goes right of 2
   - •4 goes right of 3
   - •5 goes right of 4

   Result: a chain leaning right

   Height h = 4 (edges) or 5 levels (nodes), depending on definition

   Search for 5 visits every node: 1 → 2 → 3 → 4 → 5 ⇒ Θ(n)
2. B) Insert in mixed order: 3,1,4,2,5

   - •3 root
   - •1 left of 3
   - •4 right of 3
   - •2 right of 1
   - •5 right of 4

   Result: roughly balanced

   Longest path: 3 → 1 → 2 or 3 → 4 → 5

   Height h = 2 (edges) or 3 levels

   Search for 5 visits: 3 → 4 → 5 ⇒ Θ(log n) here

**Insight:** BST time is O(h), not automatically O(log n). The same set of keys can produce either a fast tree or a slow chain depending on insertion order—this is the motivation for self-balancing BSTs.

## Key Takeaways

- ✓

  A BST is a binary tree with the invariant: ∀n, keys(left subtree) < key(n) < keys(right subtree).
- ✓

  Search follows one path determined by comparisons: k < key(n) ⇒ left, k > key(n) ⇒ right.
- ✓

  Search, insert, and delete are O(h), where h is the tree height; this is ≈ log₂ n only when the tree is balanced-ish.
- ✓

  Insertion attaches a new node at the first null pointer encountered along the search path, preserving the invariant automatically.
- ✓

  Deletion has three cases: leaf (remove), one child (splice), two children (swap with in-order successor/predecessor, then delete that node).
- ✓

  In-order traversal of a BST outputs keys in sorted order.
- ✓

  Handling duplicates requires a consistent policy (reject, route equals to one side, or count duplicates).
- ✓

  Poor insertion order can skew a BST into a chain, motivating balanced BSTs (AVL/Red-Black).

## Common Mistakes

- ✗

  Checking only parent-child ordering (left child < node < right child) instead of enforcing the invariant over entire subtrees.
- ✗

  Implementing duplicates inconsistently (e.g., insertion puts equals left but search assumes equals right), causing failed lookups.
- ✗

  Forgetting to handle the “delete root” case carefully (updating the root pointer when the deleted node is the root).
- ✗

  During two-child deletion, copying the successor key but forgetting to actually delete the successor node (creating a duplicate key).

## Practice

easy

Given a BST with keys inserted in this order: 10, 5, 15, 3, 7, 12, 18. Trace the search path (list visited keys) for k = 12 and for k = 6.

**Hint:** At each node, compare k with key(node) and choose exactly one direction. Stop at null if not found.

Show solution

For k = 12:

- •Visit 10 (12 > 10 ⇒ right)
- •Visit 15 (12 < 15 ⇒ left)
- •Visit 12 (equal ⇒ found)

Path: 10 → 15 → 12

For k = 6:

- •Visit 10 (6 < 10 ⇒ left)
- •Visit 5 (6 > 5 ⇒ right)
- •Visit 7 (6 < 7 ⇒ left)
- •Next is null ⇒ not found

Path: 10 → 5 → 7 → null

medium

Delete key 10 (the root) from the BST built by inserting: 10, 5, 15, 3, 7, 12, 18. Use the in-order successor method. What key becomes the new root key, and which node is physically removed in the final step?

**Hint:** The in-order successor of the root is the leftmost node in the root’s right subtree.

Show solution

Root key is 10 with two children ⇒ use successor.

Successor is the smallest in right subtree (root.right is 15; leftmost under 15 is 12).

Replace root key 10 with 12. Then delete the successor node (the original node containing key 12).

That successor node is a leaf in this tree, so it is physically removed by setting 15.left = null.

New root key: 12. Physically removed node in final step: the original node with key 12.

hard

Prove (informally) that an in-order traversal of a BST outputs keys in increasing order.

**Hint:** Use the invariant at a node n: all left keys < key(n) and all right keys > key(n). Then apply the same idea recursively to subtrees.

Show solution

Consider any node n.

By the BST invariant, every key in the left subtree is < key(n), and every key in the right subtree is > key(n).

An in-order traversal visits: (in-order of left subtree), then n, then (in-order of right subtree).

By recursion, the left subtree’s in-order output is sorted and consists only of keys < key(n).

Similarly, the right subtree’s in-order output is sorted and consists only of keys > key(n).

Concatenating these three sequences yields a globally increasing sequence: all left keys (sorted) < key(n) < all right keys (sorted).

## Connections

- •Next: [Balanced Trees](/tech-tree/balanced-trees/) — adds rotations and extra invariants to guarantee h = O(log n).
- •Review: [Binary Trees](/tech-tree/binary-trees/) — structure and terminology (root/leaf/child/subtree) used throughout BSTs.
- •Related: [Hash Tables](/tech-tree/hash-tables/) — faster average lookup, but lacks sorted order and range-query support.

Quality: A (4.3/5)

[← back to tree](/tech-tree/)[browse all →](/tech-tree/inventory/)
