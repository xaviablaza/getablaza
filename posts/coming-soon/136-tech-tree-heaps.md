---
title: Heaps
description: Complete binary tree with heap property. Priority queues.
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
inspiration_url: https://templeton.host/tech-tree/heaps/
inspiration_category: tech-tree
---

> Source-copy draft imported from [https://templeton.host/tech-tree/heaps/](https://templeton.host/tech-tree/heaps/). Names, domain references, and local media paths were adapted for Xavi Ablaza / getablaza.com.

[←Back to Tech Tree](/tech-tree/)

[inventory](/tech-tree/inventory/)[coverage](/tech-tree/coverage/)

# Heaps

Data StructuresDifficulty: ★★☆☆☆Depth: 4Unlocks: 2

Complete binary tree with heap property. Priority queues.

## Interactive Visualization

⏮◀◀▶▶STEP0.25x1xZOOM

t=0s

## Core Concepts

- -Heap-order property: every parent compares >= (max-heap) or <= (min-heap) each child (local partial order)
- -Complete binary-tree shape: all levels filled except possibly the last, which is filled left-to-right
- -Heap operations as local-restoration: insert and remove-extreme are implemented by comparing and swapping along a single root-to-leaf or leaf-to-root path (sift-down / sift-up) to restore heap-order while preserving shape

## Key Symbols & Notation

Index functions for array representation: parent(i) = floor((i-1)/2), left(i) = 2\*i+1, right(i) = 2\*i+2 (0-based indices)

## Essential Relationships

- -The complete-tree shape maps directly to a contiguous array via the index functions (parent/left/right), enabling O(1) navigation between node and parent/children

## Prerequisites (2)

[Binary Trees5 atoms](/tech-tree/binary-trees/)[Arrays5 atoms](/tech-tree/arrays/)

## Unlocks (1)

[Shortest Pathslvl 3](/tech-tree/shortest-paths/)

Advanced Learning Details

### Graph Position

31

Depth Cost

2

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

### All Concepts (16)

- - Complete binary tree: every level except possibly the last is completely filled, and the last level is filled left-to-right
- - Array (level-order) representation of a complete binary tree (no gaps) used for heaps
- - Index-mapping formulas for a heap stored in an array (parent/child index relationships)
- - Heap property: relation between a node and its children that defines max-heap vs min-heap
- - Max-heap: every parent >= its children (so maximum is at the root)
- - Min-heap: every parent <= its children (so minimum is at the root)
- - Sift-down (a.k.a. heapify, bubble-down): operation that restores heap property by moving a node downward
- - Sift-up (a.k.a. bubble-up): operation that restores heap property by moving a node upward
- - Build-heap (Floyd's algorithm): bottom-up heap construction by running sift-down from the last non-leaf to the root
- - Insert into heap: append to array then sift-up to restore heap property
- - Extract (remove root) from heap: swap root with last element, remove last, then sift-down the new root
- - Peek/top operation: read the root (extremum) without removing it
- - Heap as an implementation of a priority queue (mapping priority-queue operations to heap ops)
- - Height of a heap (complete binary tree) and its relation to number of nodes (logarithmic height)
- - In-place heap-sort: build a heap over the array, repeatedly swap root with last unsorted element and sift-down to sort in place
- - Comparator/key selection for making a max-heap vs a min-heap (behavior determined by comparison function)

### Teaching Strategy

Self-serve tutorial - low prerequisites, straightforward concepts.

A heap is a data structure that’s “just ordered enough” to always give you the smallest (or largest) element quickly—without paying the full cost of keeping everything perfectly sorted.

TL;DR:

A (binary) heap is a complete binary tree that satisfies a local heap-order property (min-heap or max-heap). Stored in an array, it supports peek-extreme in O(1), insert in O(log n) via sift-up, and remove-extreme in O(log n) via sift-down. It’s the standard implementation of a priority queue and is a key building block for algorithms like Dijkstra (often with an important caveat: many libraries don’t support true decrease-key).

## What Is a Heap?

### Why heaps exist (motivation)

Often you don’t need a fully sorted list—you just need to repeatedly answer questions like:

- •“What’s the smallest item right now?”
- •“Give me the next highest priority task.”
- •“I inserted something new—how does that affect the next thing I should process?”

A heap is designed for exactly this pattern: frequent **insert** and frequent **remove the min/max**.

### Definition (binary heap)

A **binary heap** is a binary tree with two constraints:

1. 1)**Shape constraint (complete binary tree):**

- •Every level is completely filled except possibly the last.
- •The last level is filled **left-to-right**.

2. 2)**Heap-order property (local ordering):**

- •**Min-heap:** every parent is ≤ each of its children.
- •**Max-heap:** every parent is ≥ each of its children.

This ordering is **local**, not global. In a min-heap, the root is the minimum element, but the rest of the tree is not necessarily sorted.

### What you get “for free”

From the heap-order property:

- •In a **min-heap**, the minimum element is at the root.
- •In a **max-heap**, the maximum element is at the root.

So:

- •**peek-min / peek-max** is **O(1)**.

### What you *don’t* get

A heap does **not** support:

- •Fast search for an arbitrary value (still O(n) in general)
- •Sorted iteration without extra work (if you repeatedly remove-min you will get sorted order, but that costs O(n log n) total)

### Difficulty calibration note

This node is **Difficulty 2–3/5**. Core heap operations are approachable (2/5), but using heaps inside graph algorithms (like Dijkstra) introduces subtleties (often closer to 3/5). This lesson keeps Dijkstra-related details **optional/advanced**.

## Core Mechanic 1: The Complete-Tree Shape and Array Representation

### Why the shape matters

The complete-tree shape makes heaps efficient because the tree height stays small.

If nnn is the number of nodes, the height is O(log⁡n)O(\log n)O(logn) (more precisely, about ⌊log⁡2n⌋\lfloor \log\_2 n \rfloor⌊log2​n⌋).

That’s the key reason sift-up and sift-down are fast: they only walk a single path from a leaf to the root (or vice versa), and that path length is at most the height.

### Array representation (0-based indexing)

A binary heap is almost always stored in an **array** rather than explicit node pointers.

Because the tree is complete, nodes can be laid out level-by-level (breadth-first order) with no gaps.

For index iii (0-based), the relationships are:

- •parent(i) = ⌊(i − 1) / 2⌋
- •left(i) = 2i + 1
- •right(i) = 2i + 2

These formulas come from how a complete binary tree packs into an array.

### Example: mapping indices to a tree

Suppose the heap array is:

Index: 0 1 2 3 4 5 6

Value: 2 5 3 9 7 4 8

Tree structure (conceptually):

- •Index 0 is the root (2)
- •Children of 0 are indices 1 and 2 (5 and 3)
- •Children of 1 are indices 3 and 4 (9 and 7)
- •Children of 2 are indices 5 and 6 (4 and 8)

### Quick complexity table

| Operation | Heap (binary) | Unsorted array | Sorted array |
| --- | --- | --- | --- |
| peek-min | O(1) | O(n) | O(1) |
| insert | O(log n) | O(1) | O(n) |
| remove-min | O(log n) | O(n) | O(1) if removing from front, but maintaining sortedness costs insert O(n) |

Heaps sit in the “sweet spot”: they keep just enough structure to make min/max cheap, without making insertion too expensive.

## Core Mechanic 2: Restoring Heap Order Locally (Sift-Up and Sift-Down)

### Why operations are “local repairs”

The heap property is local (parent vs. children). That means when you modify the heap in a controlled way, you typically break the property in only one area.

Heaps exploit this: after an insert or remove, you **repair** the heap by swapping along one path.

There are two fundamental repair operations:

- •**sift-up** (a.k.a. bubble-up, percolate-up)
- •**sift-down** (a.k.a. heapify-down, percolate-down)

We’ll describe everything using a **min-heap**. For a max-heap, flip the comparisons.

---

## Insert(x): append then sift-up

### Why append?

To preserve the **complete-tree shape**, you must add the new node at the next available spot: the end of the array.

This may violate heap order (the new value might be smaller than its parent), but the violation is on the path from that new leaf to the root.

### Sift-up logic

Let i be the index of the newly appended item.

While i > 0 and heap[i] < heap[parent(i)]:

- •swap heap[i] with heap[parent(i)]
- •update i = parent(i)

Each swap moves the element one level closer to its correct place.

### Cost

Each iteration moves up one level. There are at most O(log n) levels.

So insert is O(log n).

---

## removeMin(): move last to root then sift-down

### Why move the last element to the root?

We need to remove the root (the minimum), but if we simply delete it, we would create a hole and break the complete-tree shape.

Instead:

1. 1)Save heap[0] as the answer.
2. 2)Move the last element into heap[0].
3. 3)Pop the last slot.

Now the shape is preserved, but heap order may be violated at the root (the moved element might be too large compared to children).

### Sift-down logic

Starting at i = 0:

- •Compare heap[i] with its children.
- •Swap heap[i] with the smaller child if that child is smaller than heap[i].
- •Continue at the child index.

Stop when:

- •i has no children, or
- •heap[i] ≤ both children.

### Cost

Each swap moves down one level, and there are O(log n) levels.

So removeMin is O(log n).

---

## Peek

peekMin() just returns heap[0] (if non-empty), so O(1).

---

## Build-heap (bonus)

If you’re given an arbitrary array and want to turn it into a heap:

- •**Naive approach:** insert each item one-by-one → O(n log n).
- •**Bottom-up heapify:** run sift-down from the last parent down to root → O(n).

The O(n) result can feel surprising. Intuition: most nodes are near the bottom, and sifting down from them is very cheap.

A standard bottom-up approach for an array of length n:

- •Start i = parent(n − 1)
- •While i ≥ 0: siftDown(i)

This is the core of **heapsort** as well.

## Application/Connection: Priority Queues, Heapsort, and (Optional) Dijkstra Caveats

### Priority queue = heap + interface

A **priority queue** is an abstract data type (ADT) with operations like:

- •push(item, priority)
- •peek() (returns min or max)
- •pop() (removes and returns min or max)

A binary heap is the most common implementation.

### Typical real-world uses

- •Scheduling tasks by urgency
- •Event simulation (next event time)
- •Streaming: keep top-k elements (often using a size-k heap)
- •Graph algorithms: Dijkstra’s algorithm (min-priority queue)

---

## Heapsort connection

If you:

1. 1)Build a max-heap
2. 2)Repeatedly removeMax and place it at the end

You get an in-place sorting algorithm with O(n log n) time and O(1) extra space (ignoring recursion).

Heapsort is not stable, but it has strong worst-case guarantees.

---

## Advanced/Optional: Dijkstra and decrease-key

Dijkstra’s algorithm conceptually needs a priority queue that supports:

- •extract-min
- •decrease-key (lower the priority of an existing node)

A binary heap can support decrease-key efficiently **if** you can find the element’s index in the heap array (often by maintaining a map from node → heap index).

### Common library behavior (important caveat)

Many standard libraries (e.g., Python’s `heapq`, Java’s `PriorityQueue`) do **not** provide a direct decrease-key operation.

Common workaround:

- •When a node’s distance decreases, push a new (better) entry anyway.
- •When popping, ignore stale entries that no longer match the best-known distance.

This keeps the code simple but changes the operational profile:

- •The heap may contain multiple entries per node.
- •Complexity can become closer to O((E + K) log (E + K)) where K is the number of extra pushes (often still acceptable in practice).

If you later unlock the [Shortest Paths](/tech-tree/shortest-paths/) node, you’ll see how this affects correctness and runtime in detail.

## Worked Examples (3)

### Insert into a min-heap (sift-up step by step)

We have a min-heap stored as an array:

heap = [2, 5, 3, 9, 7, 4, 8]

Insert x = 1 and show each swap using parent(i) = ⌊(i−1)/2⌋.

1. Append 1 to the end to preserve complete-tree shape.

   New heap: [2, 5, 3, 9, 7, 4, 8, 1]

   Index of 1 is i = 7.
2. Compute parent(7) = ⌊(7−1)/2⌋ = ⌊6/2⌋ = 3.

   Compare heap[7] = 1 with heap[3] = 9.

   Since 1 < 9, swap.

   Heap becomes: [2, 5, 3, 1, 7, 4, 8, 9]

   Update i = 3.
3. Compute parent(3) = ⌊(3−1)/2⌋ = ⌊2/2⌋ = 1.

   Compare heap[3] = 1 with heap[1] = 5.

   Since 1 < 5, swap.

   Heap becomes: [2, 1, 3, 5, 7, 4, 8, 9]

   Update i = 1.
4. Compute parent(1) = ⌊(1−1)/2⌋ = 0.

   Compare heap[1] = 1 with heap[0] = 2.

   Since 1 < 2, swap.

   Heap becomes: [1, 2, 3, 5, 7, 4, 8, 9]

   Update i = 0.
5. Stop because i = 0 (at the root). The heap-order property is restored.

**Insight:** Insert only disturbed heap order along one leaf-to-root path. Sift-up fixes it with at most O(log n) swaps.

### Remove-min from a min-heap (sift-down step by step)

Start with the min-heap:

heap = [1, 2, 3, 5, 7, 4, 8, 9]

Perform removeMin() and show each swap using left(i)=2i+1 and right(i)=2i+2.

1. The minimum is at the root: min = heap[0] = 1.

   To remove it while preserving shape, move the last element (9) to the root and pop the last slot.

   Intermediate heap: [9, 2, 3, 5, 7, 4, 8]

   Now heap order may be violated at i = 0.
2. At i = 0:

   left(0)=1 → heap[1]=2

   right(0)=2 → heap[2]=3

   Choose the smaller child: index 1 (value 2).

   Since heap[0]=9 > 2, swap.

   Heap becomes: [2, 9, 3, 5, 7, 4, 8]

   Update i = 1.
3. At i = 1:

   left(1)=3 → heap[3]=5

   right(1)=4 → heap[4]=7

   Smaller child is index 3 (value 5).

   Since heap[1]=9 > 5, swap.

   Heap becomes: [2, 5, 3, 9, 7, 4, 8]

   Update i = 3.
4. At i = 3:

   left(3)=7 and right(3)=8 are out of bounds (heap size is 7).

   So i=3 has no children.

   Stop. Heap-order property is restored.

**Insight:** removeMin() replaces the root with the last element to keep the complete shape, then repairs order by pushing that element down a single root-to-leaf path.

### Bottom-up build-heap (heapify) on an arbitrary array

Given an arbitrary array A = [7, 2, 6, 3, 9, 1, 5]. Convert it into a min-heap using bottom-up heapify (sift-down from last parent to root). Use 0-based indices.

1. We have n = 7. The last index is 6.

   The last parent is parent(6) = ⌊(6−1)/2⌋ = ⌊5/2⌋ = 2.

   So we will siftDown(i) for i = 2, 1, 0.
2. i = 2:

   A[2]=6. Children:

   left(2)=5 → A[5]=1

   right(2)=6 → A[6]=5

   Smallest child is index 5 (value 1).

   Since 6 > 1, swap indices 2 and 5.

   Array becomes: [7, 2, 1, 3, 9, 6, 5]

   Now i becomes 5, which has no children → stop.
3. i = 1:

   A[1]=2. Children:

   left(1)=3 → A[3]=3

   right(1)=4 → A[4]=9

   Smallest child is index 3 (value 3).

   Since 2 ≤ 3, no swap needed → stop.
4. i = 0:

   A[0]=7. Children:

   left(0)=1 → A[1]=2

   right(0)=2 → A[2]=1

   Smallest child is index 2 (value 1).

   Since 7 > 1, swap indices 0 and 2.

   Array becomes: [1, 2, 7, 3, 9, 6, 5]

   Continue sifting down at i = 2.
5. i = 2:

   A[2]=7. Children:

   left(2)=5 → A[5]=6

   right(2)=6 → A[6]=5

   Smallest child is index 6 (value 5).

   Since 7 > 5, swap indices 2 and 6.

   Array becomes: [1, 2, 5, 3, 9, 6, 7]

   Now i = 6 has no children → stop.
6. Result: [1, 2, 5, 3, 9, 6, 7] is a valid min-heap (each parent ≤ its children).

**Insight:** Bottom-up heapify works because subtrees near the bottom are already tiny heaps after at most a couple comparisons. Doing sift-down from the last parent to the root yields O(n) total work.

## Key Takeaways

- ✓

  A binary heap is a complete binary tree + a local heap-order property (min-heap or max-heap).
- ✓

  The complete-tree shape keeps height at O(log n), enabling fast updates.
- ✓

  Array representation is standard; with 0-based indexing: parent(i)=⌊(i−1)/2⌋, left(i)=2i+1, right(i)=2i+2.
- ✓

  peek-min/peek-max is O(1) because the extreme element is at the root.
- ✓

  insert = append then sift-up; removeMin/removeMax = swap root with last, pop, then sift-down; both are O(log n).
- ✓

  Heaps are great for priority queues but do not support fast arbitrary search or maintaining fully sorted order.
- ✓

  Bottom-up build-heap (heapify) runs in O(n), faster than inserting n items (O(n log n)).
- ✓

  In many libraries, priority queues lack decrease-key; common practice is inserting duplicates and skipping stale entries when popped.

## Common Mistakes

- ✗

  Confusing the heap property with a binary search tree: heaps do not guarantee left subtree < right subtree ordering or in-order sortedness.
- ✗

  Breaking the complete-tree shape by inserting/removing from the middle; the shape rule is what makes the array representation work.
- ✗

  Implementing sift-down but swapping with an arbitrary child instead of the smaller (min-heap) / larger (max-heap) child, which can leave violations behind.
- ✗

  Assuming decrease-key exists in standard library heaps; many require a workaround (duplicates + stale pop skipping) or a custom indexed heap.

## Practice

easy

Given a min-heap array H = [2, 6, 3, 9, 8, 5]. Insert x = 4 and write the resulting heap array.

**Hint:** Append 4, then repeatedly compare it with its parent and swap while it’s smaller.

Show solution

Append: [2, 6, 3, 9, 8, 5, 4] (i=6)

parent(6)=⌊(6−1)/2⌋=2. Compare 4 with H[2]=3 → 4 is not smaller, so stop.

Result: [2, 6, 3, 9, 8, 5, 4].

medium

Perform removeMin() on the min-heap H = [1, 4, 2, 9, 7, 3]. Show the final heap array.

**Hint:** Move last element to root, pop last, then sift down by swapping with the smaller child until order is restored.

Show solution

Remove min=1. Move last element 3 to root and pop last:

[3, 4, 2, 9, 7]

Sift-down at i=0: children are 4 and 2 → smaller is 2 at index 2. Swap:

[2, 4, 3, 9, 7]

Now i=2 has no children (left(2)=5 out of bounds). Stop.

Final heap: [2, 4, 3, 9, 7].

hard

You have an array A = [10, 1, 8, 3, 2]. Build a min-heap using bottom-up heapify and give the resulting array.

**Hint:** Start at i = parent(n−1) and sift down for i = 1 then i = 0.

Show solution

n=5 → last index 4 → last parent parent(4)=⌊(4−1)/2⌋=1.

Start A=[10,1,8,3,2]

i=1: A[1]=1, children: left=3→3, right=4→2. Since 1 ≤ 2 and 1 ≤ 3, no swap.

i=0: A[0]=10, children: left=1→1, right=2→8. Smaller child is 1 at index 1. Swap:

A=[1,10,8,3,2]

Continue at i=1: A[1]=10, children: left=3→3, right=4→2. Smaller child is 2 at index 4. Swap:

A=[1,2,8,3,10]

Index 4 has no children. Done.

Result: [1,2,8,3,10].

## Connections

Next, heaps become a critical tool in graph algorithms where you repeatedly select the smallest tentative distance:

- •[Shortest Paths](/tech-tree/shortest-paths/)

Related nodes you may have already used implicitly:

- •Binary Trees (structure intuition)
- •Arrays (indexing + O(1) access enabling parent/child formulas)

Quality: A (4.4/5)

[← back to tree](/tech-tree/)[browse all →](/tech-tree/inventory/)
