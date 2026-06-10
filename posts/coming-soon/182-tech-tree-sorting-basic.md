---
title: Basic Sorting
description: Bubble sort, insertion sort, selection sort. O(n^2) algorithms.
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
permalink: /tech-tree/sorting-basic/
---

[←Back to Tech Tree](/tech-tree/)

[inventory](/tech-tree/inventory/)[coverage](/tech-tree/coverage/)

# Basic Sorting

AlgorithmsDifficulty: ★★☆☆☆Depth: 3Unlocks: 0

Bubble sort, insertion sort, selection sort. O(n^2) algorithms.

## Interactive Visualization

⏮◀◀▶▶STEP0.25x1xZOOM

t=0s

## Core Concepts

- -Compare two elements to decide their order
- -Relocate elements in-place via primitive operations (swap or shift)
- -Maintain a loop invariant: a progressively grown sorted region until the entire array is sorted

## Key Symbols & Notation

swap(i,j) -- primitive operation exchanging elements at indices i and j

## Essential Relationships

- -Repeated comparisons combined with swaps/shifts across n items (nested iteration) produce quadratic time, O(n^2)
- -Each algorithm is defined by how it expands the sorted region (adjacent swapping, shifting to insert, or selecting an extreme then swapping)

## Prerequisites (2)

[Arrays5 atoms](/tech-tree/arrays/)[Big O Notation6 atoms](/tech-tree/big-o/)

Advanced Learning Details

### Graph Position

39

Depth Cost

0

Fan-Out (ROI)

0

Bottleneck Score

3

Chain Length

### Cognitive Load

6

Atomic Elements

30

Total Elements

L1

Percentile Level

L4

Atomic Level

### All Concepts (18)

- - Sorting problem: arranging the elements of an array into a specified order (e.g., non-decreasing) using comparisons and rearrangements
- - Comparison operation as the basic decision: comparing two elements to determine order
- - Compare-and-swap primitive: compare two elements and swap them if they are out of order
- - Swap (exchange) operation: swapping the positions of two array elements
- - Adjacent swap: swapping elements that are next to each other (indices i and i+1)
- - Pass (sweep): one traversal over part or all of the array during which comparisons/swaps are performed
- - Sorted prefix: a contiguous initial segment of the array that is already sorted (used by insertion sort)
- - Sorted suffix: a contiguous final segment of the array that is already sorted (used by bubble/selection sorts)
- - Selection step: locating the minimum (or maximum) element in the unsorted portion and moving it into place
- - Insertion step: taking the next element and inserting it into the correct position within the sorted prefix
- - Shifting versus swapping during insertion: moving elements one position to the right (shift) instead of repeated swaps
- - Early-exit optimization for bubble sort: detecting a pass with no swaps to stop early
- - Stability of a sorting algorithm: whether equal-valued elements preserve their original relative order
- - In-place sorting: performing the sort using only O(1) extra memory (no significant auxiliary arrays)
- - Adaptivity: an algorithm property where running time improves if the input is already partially sorted (insertion sort is adaptive)
- - Cost metrics beyond Big-O runtime: counting comparisons and swaps/assignments as distinct costs useful for comparing these algorithms
- - Loop invariant for sorting algorithms: a formal condition (e.g., 'prefix of length k is sorted') that holds after each iteration and is used to prove correctness
- - Comparison-based sorting class: these algorithms make decisions only by comparing elements (as opposed to non-comparison sorts)

### Teaching Strategy

Deep-dive lesson - accessible entry point but dense material. Use worked examples and spaced repetition.

Sorting is where “algorithm thinking” becomes tangible: you can watch order emerge from repeated, tiny decisions—compare, swap, shift—until the whole array becomes predictable to scan, search, and reason about.

TL;DR:

Basic O(n²) sorting algorithms repeatedly compare elements and move them into place. Bubble sort grows a sorted region by swapping adjacent out-of-order pairs; selection sort grows it by repeatedly selecting the minimum; insertion sort grows it by inserting the next element into an already-sorted prefix via shifts. All rely on clear loop invariants and simple in-place operations like swap(i,j).

## What Is Basic Sorting?

### Why sorting is worth learning (before the how)

Sorting is the simplest setting where you practice three core algorithm skills:

1. 1)**Local decisions → global order**: a single comparison tells you which of two elements should come first, but sorting needs the entire array to agree with those comparisons.
2. 2)**Primitive in-place movement**: most real algorithms are built out of a small set of operations (swap, shift, overwrite). Sorting makes those operations explicit.
3. 3)**Loop invariants**: you prove progress by naming a region that is already sorted (or already “final”), and showing every iteration grows that region.

Even if you later use faster algorithms (merge sort, quicksort, heapsort), these basics give you intuition for:

- •how much work “ordering” inherently requires,
- •how algorithm structure affects constant factors,
- •how to argue correctness with invariants.

### What “sorting an array” means

You have an array A of length n with elements that can be compared. A sorting algorithm rearranges the elements so that:

A[0] ≤ A[1] ≤ … ≤ A[n−1]

We’ll assume **ascending** order and a comparison operator “≤”. The learner already knows arrays and Big-O; here we focus on *mechanics*.

### The primitive operations: swap vs shift

We’ll use the key symbol:

- •**swap(i,j)**: exchange A[i] and A[j]

This is the primitive “relocate in-place” tool in bubble and selection sort.

Insertion sort typically uses **shifts** (copying an element one position right) and then writes one saved element into a gap. Shifting is still in-place, but it’s not symmetric like swap.

### What O(n²) means here (intuitively)

All three algorithms do “many” comparisons. In the average/worst case they do on the order of:

∑ from k=1 to n of k ≈ n(n+1)/2 ≈ n²/2

So time grows roughly with n². Doubling n makes work about 4×.

### A note on stability (a subtle but important property)

If elements have equal keys (say, two records with the same score), a **stable** sort preserves their original relative order.

- •Bubble sort: stable (when implemented with strict “>” swap condition)
- •Insertion sort: stable (when shifting elements that are “> key”)
- •Selection sort: typically **not stable** (because a far-away minimum swaps forward)

Stability matters when sorting by multiple keys (e.g., sort by last name, then stable-sort by first name).

### Big picture: the “sorted region” idea

Each algorithm maintains a loop invariant describing a region that is already sorted and in final position:

- •Bubble: a **sorted suffix** grows at the end.
- •Selection: a **sorted prefix** grows at the start.
- •Insertion: a **sorted prefix** grows at the start.

That invariant is your correctness anchor: if the region is correct and it grows until it covers the whole array, the algorithm works.

## Core Mechanic 1: Comparing + Moving Elements In-Place (swap and shift)

### Why movement strategy matters

Sorting is not only about comparing; it’s about *how you move elements once you know something is out of place*.

Two common strategies:

1. 1)**Swap-based movement**: exchange two elements.

- •Simple
- •Often does extra writes
- •Great for “push the extreme to the end” patterns

2. 2)**Shift-based movement**: slide a block over by 1 to make a hole.

- •More efficient when an element needs to move left a long distance
- •Preserves stability naturally

### swap(i,j) precisely

Given indices i and j:

- •temp ← A[i]
- •A[i] ← A[j]
- •A[j] ← temp

That’s 3 assignments (writes) for one swap.

### Shifting precisely

Suppose you want to insert a key into a sorted prefix A[0..i−1]. You:

- •save key = A[i]
- •while elements are too large, shift them right:
- •A[j+1] ← A[j]
- •then place key:
- •A[j+1] ← key

This can move key far left with many shifts, but avoids repeated swaps.

### Counting work: comparisons vs writes

When analyzing O(n²) sorts, it helps to separate:

- •**Comparisons**: calls to “≤” or “>”
- •**Writes**: assignments into the array (swaps are multiple writes)

Why? Two algorithms can both be O(n²) but behave differently in practice.

| Algorithm | Main movement | Comparisons (worst) | Writes (typical) | Stable? |
| --- | --- | --- | --- | --- |
| Bubble | adjacent swaps | ≈ n²/2 | high (many swaps) | yes |
| Selection | swap min forward | ≈ n²/2 | low (≤ n swaps) | no |
| Insertion | shifts then insert | ≈ n²/2 | moderate; good on nearly sorted | yes |

### A key pacing insight: “sorted region” is not the same as “minimum work”

All three can be proven correct by a growing sorted region. But performance depends on *how much disruption* the remaining unsorted region causes.

- •If the array is nearly sorted, insertion sort does very little shifting.
- •Bubble sort can also short-circuit with an “already sorted” flag.
- •Selection sort does the same comparisons regardless of existing order (it still scans to find the minimum each time).

## Core Mechanic 2: Loop Invariants and the Three O(n²) Sorts

### Why loop invariants come first

A sorting algorithm is repetitive. Without a clear invariant, it’s easy to get lost in indices and off-by-one errors.

A **loop invariant** is a statement that is true:

1) before an iteration,

2) preserved by the iteration,

3) and strong enough that when the loop ends, it implies the array is sorted.

We’ll state a clean invariant for each algorithm.

---

## Bubble Sort

### Idea

Repeatedly compare adjacent elements and swap if out of order. This “bubbles” large elements to the right.

### Invariant

After pass p (0-based), the **last p elements** are in sorted order and are the p largest elements of the array.

So the sorted region is a **suffix** that grows from the right.

### Mechanics (high level)

For i from 0 to n−2:

- •compare A[i] and A[i+1]
- •if A[i] > A[i+1], do swap(i, i+1)

Repeat for shorter and shorter ranges.

### Why it works (sketch)

During a single pass, the maximum element in the unsorted prefix moves right one step at a time until it reaches the end of that prefix. So after one full pass, the maximum is in its final place at the end. Repeat.

### Common optimization

Track whether any swap happened during a pass.

- •If no swaps occur, the array is already sorted → stop early.

---

## Selection Sort

### Idea

Repeatedly select the minimum element from the unsorted region and swap it into the next position in the front.

### Invariant

After iteration k, the **first k elements** are the k smallest elements of the array, in sorted order.

So the sorted region is a **prefix** that grows from the left.

### Mechanics (high level)

For pos from 0 to n−1:

- •find index minIdx of the smallest element in A[pos..n−1]
- •swap(pos, minIdx)

### Why it works (sketch)

At each step, you place the smallest remaining element into position pos, which is exactly where it belongs in the fully sorted array.

### Not stable (important)

If there are equal keys, selecting a minimum far to the right and swapping forward can leapfrog equal elements.

---

## Insertion Sort

### Idea

Grow a sorted prefix one element at a time by inserting the next element into the correct position in the prefix.

### Invariant

Before processing index i, the prefix A[0..i−1] is sorted.

Then you take A[i] (call it key) and insert it so that A[0..i] becomes sorted.

### Mechanics (high level)

For i from 1 to n−1:

- •key ← A[i]
- •j ← i−1
- •while j ≥ 0 and A[j] > key:
- •A[j+1] ← A[j] (shift right)
- •j ← j−1
- •A[j+1] ← key

### Why it works (sketch)

Because A[0..i−1] is sorted, once you find where key belongs (the first position where A[j] ≤ key), everything to the right can be shifted by 1 and key placed in the gap.

### Best-case behavior

If the array is already sorted, the inner while condition fails immediately each time:

- •comparisons ≈ n
- •shifts ≈ 0

So insertion sort is fast on nearly sorted data.

---

## Complexity summary with a little math

All three do nested loops. In the worst case:

Comparisons ≈ ∑ from m=1 to n−1 of m

Compute:

∑ m = 1 + 2 + … + (n−1)

= (n−1)n/2

≈ n²/2

So worst-case time is O(n²).

Writes differ:

- •Bubble: can swap many times (each swap is 3 writes)
- •Selection: at most n swaps → O(n) swaps (but still O(n²) comparisons)
- •Insertion: shifts depend on how far elements move; worst-case O(n²) shifts, but often much less.

## Application/Connection: Choosing a Basic Sort and Using It Well

### Why you still care about O(n²) sorts in real systems

Even though O(n²) sounds “slow,” these algorithms show up in practice because:

- •n is sometimes small (sorting ≤ 20 elements is common in inner loops)
- •data may be nearly sorted (insertion sort excels)
- •they are simple to implement and reason about
- •they can be used as building blocks (hybrid algorithms)

A common pattern: a fast O(n log n) algorithm partitions the problem, and for small subarrays, it switches to insertion sort because constant factors dominate.

### How to choose (quick decision table)

| Situation | Best pick | Why |
| --- | --- | --- |
| Very small arrays | Insertion | low overhead, good cache behavior |
| Nearly sorted input | Insertion | few shifts; close to O(n) |
| Want minimal writes (flash / expensive writes) | Selection | O(n) swaps |
| Need stable sorting by multiple keys | Insertion or Bubble | stability preserved |
| Teaching / visualizing adjacent swaps | Bubble | easiest to “see” |

### Invariants as debugging tools

When your sort fails, invariants tell you where to look.

- •Bubble: after each pass, check the suffix is sorted and contains the largest elements.
- •Selection: after each iteration, check the prefix is sorted and contains the smallest elements.
- •Insertion: before inserting key at i, check A[0..i−1] is sorted.

You can literally assert these conditions in code while learning.

### Connection to later topics

These algorithms build intuition for:

- •**Divide and conquer sorts**: merge sort, quicksort
- •**Heaps**: selecting min/max efficiently
- •**Stability**: sorting records by multiple keys
- •**Inversions**: insertion sort’s cost relates to the number of out-of-order pairs

If you understand how a sorted region grows and why each move is safe, you’re ready to learn faster sorts without treating them as magic.

## Worked Examples (3)

### Bubble Sort by Hand (track the growing sorted suffix)

Sort A = [5, 1, 4, 2, 8] in ascending order using bubble sort. Show passes and swaps(i,i+1).

1. Pass 1 (compare adjacent through index 0..3):

   - •Compare A[0]=5 and A[1]=1 → 5 > 1 ⇒ swap(0,1)

   A = [1, 5, 4, 2, 8]

   - •Compare A[1]=5 and A[2]=4 → 5 > 4 ⇒ swap(1,2)

   A = [1, 4, 5, 2, 8]

   - •Compare A[2]=5 and A[3]=2 → 5 > 2 ⇒ swap(2,3)

   A = [1, 4, 2, 5, 8]

   - •Compare A[3]=5 and A[4]=8 → 5 ≤ 8 ⇒ no swap

   End pass 1: last element is the maximum of the array → suffix [8] is sorted and final.
2. Pass 2 (compare adjacent through index 0..2):

   - •Compare 1 and 4 → ok
   - •Compare 4 and 2 → 4 > 2 ⇒ swap(1,2)

   A = [1, 2, 4, 5, 8]

   - •Compare 4 and 5 → ok

   End pass 2: suffix [5, 8] is sorted and final.
3. Pass 3 (through index 0..1):

   - •Compare 1 and 2 → ok
   - •Compare 2 and 4 → ok

   No swaps occurred in this pass ⇒ array is sorted; can stop early.

**Insight:** Bubble sort’s core correctness story is: one full pass guarantees the current maximum reaches its final position at the end, so the sorted suffix grows by 1 each pass. The “no swaps” optimization turns best case into O(n).

### Insertion Sort by Hand (shifts + insert into a sorted prefix)

Sort A = [7, 3, 5, 2] using insertion sort. Show shifts and the loop invariant that A[0..i−1] is sorted.

1. Start: A = [7, 3, 5, 2]

   Invariant before i=1: prefix A[0..0] = [7] is sorted.
2. i = 1, key = 3, j = 0

   Check A[j] > key? A[0]=7 > 3 yes ⇒ shift:

   - •A[1] ← A[0] ⇒ A = [7, 7, 5, 2]
   - •j ← -1 (stop)

   Insert key at j+1 = 0:

   - •A[0] ← 3 ⇒ A = [3, 7, 5, 2]

   Now A[0..1] = [3,7] is sorted.
3. i = 2, key = 5, j = 1

   A[1]=7 > 5 yes ⇒ shift:

   - •A[2] ← A[1] ⇒ A = [3, 7, 7, 2]
   - •j ← 0

   A[0]=3 > 5? no ⇒ stop shifting

   Insert key at j+1=1:

   - •A[1] ← 5 ⇒ A = [3, 5, 7, 2]

   Now A[0..2] = [3,5,7] is sorted.
4. i = 3, key = 2, j = 2

   A[2]=7 > 2 ⇒ shift → A = [3, 5, 7, 7]

   A[1]=5 > 2 ⇒ shift → A = [3, 5, 5, 7]

   A[0]=3 > 2 ⇒ shift → A = [3, 3, 5, 7]

   j becomes -1

   Insert key at 0:

   A = [2, 3, 5, 7]

   Now entire array sorted.

**Insight:** Insertion sort is “sorting by maintaining a promise”: before each insertion, the left prefix is sorted. Shifts preserve that order, and inserting key in the first valid position restores the invariant for a larger prefix.

### Selection Sort by Hand (min scan + swap forward)

Sort A = [4, 1, 3, 1] using selection sort. Show each min selection and swap(pos, minIdx).

1. pos = 0: scan A[0..3] = [4,1,3,1]

   Minimum is 1 at minIdx = 1 (or 3; standard implementation picks first min found).

   swap(0,1) ⇒ A = [1,4,3,1]

   Invariant: A[0] is the smallest element and fixed.
2. pos = 1: scan A[1..3] = [4,3,1]

   Minimum is 1 at minIdx = 3

   swap(1,3) ⇒ A = [1,1,3,4]

   Invariant: A[0..1] are the 2 smallest elements sorted.
3. pos = 2: scan A[2..3] = [3,4]

   Minimum is 3 at minIdx = 2

   swap(2,2) does nothing ⇒ A unchanged.

   Array sorted.

**Insight:** Selection sort minimizes swaps (≤ n), but it still performs a full min-scan each step. Also notice how swapping can move an element far—this is why selection sort is usually not stable.

## Key Takeaways

- ✓

  Sorting means rearranging array elements so A[0] ≤ A[1] ≤ … ≤ A[n−1].
- ✓

  All three basic sorts are built from local comparisons plus in-place relocation via swap(i,j) or shifts.
- ✓

  A loop invariant (a growing sorted prefix/suffix) is the cleanest way to reason about correctness.
- ✓

  Bubble sort grows a sorted suffix by repeated adjacent swaps; an early-exit flag gives O(n) best case.
- ✓

  Selection sort grows a sorted prefix by selecting the minimum from the unsorted region; it uses few swaps but is typically not stable.
- ✓

  Insertion sort grows a sorted prefix by inserting the next element into position using shifts; it is fast on nearly sorted data and stable.
- ✓

  Worst-case comparisons for all three are about (n−1)n/2 ≈ n²/2 ⇒ O(n²).
- ✓

  Algorithm choice can depend on stability needs, write cost, and how sorted the input already is.

## Common Mistakes

- ✗

  Off-by-one loop bounds (e.g., bubble inner loop going to n−1 instead of stopping at the unsorted boundary).
- ✗

  Breaking stability accidentally (e.g., in bubble sort swapping when A[i] ≥ A[i+1] instead of strictly A[i] > A[i+1]).
- ✗

  In insertion sort, forgetting to save key before shifting, which overwrites the value you’re trying to insert.
- ✗

  In selection sort, scanning the wrong range (should start at pos, not 0), which can undo earlier work.

## Practice

easy

Run one full pass of bubble sort on A = [3, 2, 2, 1]. Show the array after the pass and state what you know is true about the last element.

**Hint:** Bubble pass compares (0,1), (1,2), (2,3). Swap only when left > right.

Show solution

Start: [3,2,2,1]

Compare 3 and 2 → swap ⇒ [2,3,2,1]

Compare 3 and 2 → swap ⇒ [2,2,3,1]

Compare 3 and 1 → swap ⇒ [2,2,1,3]

After one full pass, the last element (3) is the maximum and is in its final position.

medium

Use insertion sort logic to insert key = 6 into the sorted prefix [2, 4, 5, 7] (think of it as A[0..3] sorted and key is A[4]). Show shifts and the final array.

**Hint:** Shift elements that are > 6 one position right until you find an element ≤ 6.

Show solution

Prefix sorted: [2,4,5,7], key=6

Start j at index of 7. Since 7 > 6, shift it right:

[2,4,5,7,7]

Now compare 5 to 6: 5 > 6? no, stop.

Insert key at position after 5:

[2,4,5,6,7]

hard

Selection sort does (n−1) + (n−2) + … + 1 comparisons in the worst case. Derive a closed form and show it is O(n²).

**Hint:** Use the arithmetic series sum 1 + 2 + … + (n−1) = (n−1)n/2.

Show solution

Worst-case comparisons:

C(n) = (n−1) + (n−2) + … + 1

Rewrite in increasing order:

C(n) = 1 + 2 + … + (n−1)

Use arithmetic series formula:

C(n) = (n−1)n/2

Asymptotically, (n−1)n/2 = (n² − n)/2 ≈ n²/2, so C(n) ∈ O(n²).

## Connections

- •Next: [Divide and Conquer Sorting](/tech-tree/sorting-divide-conquer/)
- •Related: [Loop Invariants](/tech-tree/loop-invariants/)
- •Related: [Stability in Sorting](/tech-tree/sorting-stability/)
- •Related: [Asymptotic Analysis Refresher](/tech-tree/big-o-notation/)

Quality: A (4.5/5)

[← back to tree](/tech-tree/)[browse all →](/tech-tree/inventory/)
