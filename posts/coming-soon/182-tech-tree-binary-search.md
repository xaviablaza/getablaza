---
title: Binary Search
description: O(log n) search in sorted array. Divide and conquer.
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
permalink: /tech-tree/binary-search/
---

[←Back to Tech Tree](/tech-tree/)

[inventory](/tech-tree/inventory/)[coverage](/tech-tree/coverage/)

# Binary Search

AlgorithmsDifficulty: ★★☆☆☆Depth: 3Unlocks: 0

O(log n) search in sorted array. Divide and conquer.

## Interactive Visualization

⏮◀◀▶▶STEP0.25x1xZOOM

t=0s

## Core Concepts

- -Array is sorted (nondecreasing order).
- -Maintain a search interval [low,high] that, if target exists, always contains its index; stop when interval is empty or target is found.

## Key Symbols & Notation

low (lowest index of current interval)high (highest index of current interval)

## Essential Relationships

- -Compute mid = (low + high) div 2; compare A[mid] to target: if equal -> found; if A[mid] < target -> low = mid + 1; else high = mid - 1 (this halves the interval).

## Prerequisites (2)

[Arrays5 atoms](/tech-tree/arrays/)[Big O Notation6 atoms](/tech-tree/big-o/)

## Referenced by (1)

Where this concept shows up in the operating-finance and personal-finance graphs.

### From Business (1)

[IRRBusiness

Bisection for IRR is literally binary search on a continuous domain - bracket the rate where NPV changes sign, halve the interval, repeat. The O(log n) convergence logic and divide-and-conquer structure are identical.](/business/irr/)

Advanced Learning Details

### Graph Position

38

Depth Cost

0

Fan-Out (ROI)

0

Bottleneck Score

3

Chain Length

### Cognitive Load

5

Atomic Elements

30

Total Elements

L1

Percentile Level

L3

Atomic Level

### All Concepts (13)

- - Sorted array (total order on elements; array must be ordered ascending or descending for binary search to work)
- - Divide-and-conquer application: reduce problem by splitting the search interval in two and discarding one half
- - Search interval representation: maintaining low and high indices that bound the current candidate subarray
- - Midpoint selection: choosing a middle index of the current interval to test
- - Halving property: each comparison reduces the size of the candidate interval by about half
- - Termination conditions: when midpoint equals target (found) or when interval becomes empty (not found)
- - Loop vs recursion control: implementing repeated halving either iteratively or recursively
- - Invariants for correctness: e.g., if target exists in the array then it is always within A[low..high]
- - Inclusive vs exclusive bounds variants (e.g., [low, high] vs [low, high) semantics) and their impact on updates
- - Off-by-one issues: correct index updates (low = mid+1, high = mid-1, or their variants) to avoid skipping elements
- - Integer-midpoint rounding: the need to floor/truncate when computing the middle index
- - Overflow-safe midpoint computation: using low + (high - low) // 2 instead of (low + high) // 2 in fixed-width integer contexts
- - Handling duplicates: distinguishing finding any occurrence versus finding first/last occurrence requires modified update rules

### Teaching Strategy

Self-serve tutorial - low prerequisites, straightforward concepts.

You have a sorted list of a million items and need to know whether a value is present. Scanning from left to right works—but it wastes the fact that the list is sorted. Binary search is the classic way to turn “sorted order” into a dramatic speedup: from O(n) down to O(log n).

TL;DR:

Binary search repeatedly halves a sorted array’s remaining search interval. Maintain an interval [low, high] that always contains the target’s index if it exists. Check mid; if mid is too small, move low up; if too large, move high down. This takes O(log n) time and O(1) extra space.

## What Is Binary Search?

### The problem it solves

You’re given an array `A` and a `target` value. You want to find the index of `target` (or decide it isn’t present).

- •With an unsorted array, the safest approach is linear search: check each element until you find `target` or reach the end. That’s O(n).
- •With a **sorted** array (nondecreasing order), you can do much better by using the ordering information.

Binary search is a **divide-and-conquer** algorithm for searching in a sorted array. The key idea: each comparison lets you discard **half** of the remaining candidates.

### What “sorted” means here

Assume the array is sorted in **nondecreasing** order:

- •For indices i < j, we have A[i] ≤ A[j].

Nondecreasing allows duplicates (e.g., `[1, 2, 2, 2, 5]`). Binary search still works, but you must be clear on what you want when duplicates exist (any occurrence? first? last?). We’ll cover variants later.

### The mental model: shrinking an interval

Binary search maintains a **search interval** of indices where the target could still be.

- •`low` = lowest index still possible
- •`high` = highest index still possible

At all times, you try to preserve this loop invariant:

> **Invariant:** If `target` appears in the array, then its index lies within `[low, high]`.

Each step picks the middle index `mid`, compares `A[mid]` to `target`, and throws away the half that can’t contain the target.

### Prerequisite note (to avoid hidden gaps)

Before you code binary search confidently, you should be comfortable with:

1. 1)**Integer division / floor:** computing `mid` using floor behavior (e.g., `(low + high) // 2`).
2. 2)**Loop invariants:** understanding and maintaining “what is always true” about `[low, high]` each iteration.
3. 3)**Edge cases:** empty arrays, single-element arrays, and duplicate values.
4. 4)*(Optional but useful)* **Comparator-based ordering:** arrays sorted descending or by a custom key require adjusting comparisons.

These aren’t “extra topics”—they are exactly where most binary search bugs come from.

### Why it’s O(log n)

Each iteration cuts the interval size roughly in half.

If the array length is n:

- •after 1 step: ~n/2 candidates remain
- •after 2 steps: ~n/4
- •after k steps: ~n/2ᵏ

We stop when the interval becomes empty or we find the target. The smallest k such that n/2ᵏ ≤ 1 is k ≥ log₂(n). So the number of iterations is O(log n).

## Core Mechanic 1: Maintain the Search Interval [low, high] (Loop Invariant)

### Why the interval matters

Binary search isn’t just “check middle and move left/right.” It’s a careful promise about what indices are still possible.

If you lose that promise (the invariant), you can:

- •skip over the target
- •loop forever
- •read out of bounds

So we’ll be explicit about the invariant and how each update preserves it.

### The standard exact-match version (closed interval)

We’ll use a **closed interval** `[low, high]` inclusive. Initialize:

- •`low = 0`
- •`high = n - 1`

Loop while the interval is non-empty:

- •condition: `low <= high`

Compute middle:

- •`mid = low + (high - low) // 2`

(The `low + (high - low)` form avoids overflow in languages with fixed-size integers; in Python it’s not necessary, but it’s a good habit.)

Compare:

- •If `A[mid] == target`: return `mid`
- •If `A[mid] < target`: discard left half including `mid` → set `low = mid + 1`
- •If `A[mid] > target`: discard right half including `mid` → set `high = mid - 1`

If the loop ends, return “not found” (often `-1`).

### Showing the invariant preservation

Let’s spell out what each case means.

Assume the array is sorted nondecreasing.

#### Case 1: A[mid] < target

Because the array is sorted, for every i ≤ mid, we have A[i] ≤ A[mid] < target.

So **no index ≤ mid can hold target**.

Therefore, if `target` exists, it must be in indices `mid + 1 ... high`. Setting `low = mid + 1` preserves:

> If target exists, it’s still in `[low, high]`.

#### Case 2: A[mid] > target

Similarly, for every i ≥ mid, we have A[i] ≥ A[mid] > target.

So **no index ≥ mid can hold target**.

Therefore, if `target` exists, it must be in indices `low ... mid - 1`. Setting `high = mid - 1` preserves the invariant.

#### Case 3: A[mid] == target

We’re done.

### Termination: why it must end

Each iteration strictly shrinks the interval:

- •`low` increases (to `mid + 1`) or
- •`high` decreases (to `mid - 1`) or
- •we return

Since `low` and `high` are integers and the interval length can’t shrink forever without becoming empty, the loop terminates.

### Concrete pseudocode

```
binary_search(A, target):
    low = 0
    high = len(A) - 1

    while low <= high:
        mid = low + (high - low) // 2

        if A[mid] == target:
            return mid
        else if A[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return -1
```

### Breathing room: trace one run

Suppose `A = [2, 5, 7, 12, 19, 23, 31]`, `target = 19`.

- •Start: low=0, high=6
- •mid=3 → A[3]=12 < 19 → low=4
- •Now low=4, high=6
- •mid=5 → A[5]=23 > 19 → high=4
- •Now low=4, high=4
- •mid=4 → A[4]=19 == 19 → found at 4

Notice how `[low, high]` always contained index 4 until we found it.

## Core Mechanic 2: Getting Boundaries Right (mid, duplicates, and interval conventions)

Binary search is famous for off-by-one errors. Most bugs come from mixing interval conventions or mishandling duplicates.

### 1) Computing mid safely and correctly

The classic formula is:

- •`mid = (low + high) // 2`

In many languages, `low + high` can overflow if indices are large. A safer version is:

- •`mid = low + (high - low) // 2`

Both choose the “lower middle” when there are two middles.

### 2) Closed vs half-open intervals

There are two common interval conventions:

| Convention | Interval | Loop condition | Update when going right | Update when going left |
| --- | --- | --- | --- | --- |
| Closed | `[low, high]` | `low <= high` | `low = mid + 1` | `high = mid - 1` |
| Half-open | `[low, high)` | `low < high` | `low = mid + 1` or `low = mid` (depends) | `high = mid` |

For beginners, **closed intervals** are often easier to reason about for exact-match search.

The most important rule is: **pick one convention and stay consistent**.

### 3) Duplicates: “any occurrence” vs “first/last occurrence”

If duplicates exist, the exact-match binary search above can return **any** index where `A[mid] == target`.

Sometimes you need a stable boundary, like:

- •**lower bound**: first index i where A[i] ≥ target
- •**upper bound**: first index i where A[i] > target

These are incredibly useful in practice (counting occurrences, insertion positions, range queries).

#### Lower bound (first position with A[i] ≥ target)

A common pattern uses a half-open interval `[low, high)`:

- •Initialize: `low = 0`, `high = n`
- •While `low < high`:
- •`mid = low + (high - low) // 2`
- •If `A[mid] < target`, discard left including mid → `low = mid + 1`
- •Else, keep mid (could be answer) → `high = mid`

At the end, `low` is the smallest index with `A[low] ≥ target` (or `n` if none).

Why does `high = mid` (not `mid - 1`)? Because in half-open intervals, `high` is exclusive, and we want to keep `mid` as a candidate.

#### Upper bound (first position with A[i] > target)

Same structure, just change the comparison:

- •If `A[mid] <= target`, move `low = mid + 1`
- •Else, `high = mid`

Then the count of occurrences of `target` is:

count=upper\_bound(A,target)−lower\_bound(A,target)\text{count} = \text{upper\\_bound}(A, target) - \text{lower\\_bound}(A, target)count=upper\_bound(A,target)−lower\_bound(A,target)

### 4) Empty arrays and single-element arrays

Binary search should handle these without special-casing if your loop condition is correct.

- •Empty: n = 0 → `high = -1` → `low <= high` is false immediately → return -1.
- •Single element: low=0, high=0 → one iteration checks that element.

### 5) Custom orderings (optional but important)

If the array is sorted descending, the direction flips:

- •If `A[mid] < target`, you must go **left** (because values decrease to the right).

If the array is sorted by a key (e.g., objects sorted by `age`), compare using that key consistently.

A useful way to stay sane is to think: you need a monotonic predicate (something that switches from false to true once). Lower/upper bound are built exactly on that principle.

## Applications and Connections (Where Binary Search Shows Up)

### 1) Fast lookup in sorted data

Binary search is the core primitive behind many “fast membership” tasks when data is stored sorted:

- •searching in a sorted array
- •searching in a sorted list of timestamps
- •dictionary-like behavior when updates are rare but queries are frequent

Time complexity is O(log n) per query, with O(1) extra space.

### 2) Insertion position and maintaining sorted order

Using lower bound, you can find where to insert an element while maintaining sorted order.

- •Find index i = lower\_bound(A, x)
- •Insert at i (in an array, insertion itself is O(n) due to shifting, but the search for position is O(log n))

This is common in:

- •building sorted lists incrementally
- •coordinate compression (collect values, sort, then binary search indices)

### 3) Range counting and frequency queries

If the array is sorted, you can count how many elements equal `target` or lie in a range [L, R].

- •occurrences of x: `ub(x) - lb(x)`
- •count in [L, R]: `lb(R+ε) - lb(L)` (conceptually), or more directly `ub(R) - lb(L)`

### 4) Binary search on the answer (a bigger idea)

A powerful pattern is **binary searching over a value space** when you have a monotonic condition.

Example shape:

- •You want the smallest value `k` such that `feasible(k)` is true.
- •If `feasible(k)` is true, then `feasible(k+1)` is also true (monotonic).

Then you can binary search `k` even if there is no array.

This is used for:

- •minimum capacity / maximum speed problems
- •scheduling and allocation
- •optimization with monotonic constraints

This lesson node focuses on array search, but learning lower/upper bound sets you up for that broader technique.

## Worked Examples (3)

### Exact match search (closed interval) with a full trace

Array A is sorted: A = [1, 4, 6, 9, 13, 18, 21, 27]. Find target = 13 using binary search with [low, high].

1. Initialize:

   low = 0

   high = 7 (n-1)

   Invariant: if 13 exists, it is in indices [0,7].
2. Iteration 1:

   mid = low + (high - low)//2 = 0 + (7-0)//2 = 3

   A[mid] = A[3] = 9

   Compare: 9 < 13, so discard indices ≤ 3.

   Update: low = mid + 1 = 4

   Now interval is [4,7].
3. Iteration 2:

   mid = 4 + (7-4)//2 = 4 + 3//2 = 5

   A[5] = 18

   Compare: 18 > 13, so discard indices ≥ 5.

   Update: high = mid - 1 = 4

   Now interval is [4,4].
4. Iteration 3:

   mid = 4 + (4-4)//2 = 4

   A[4] = 13

   Compare: 13 == 13 → found.

   Return index 4.

**Insight:** The invariant makes the updates feel inevitable: once A[mid] is too small, everything left of mid is too small because the array is sorted.

### Lower/upper bound to count duplicates

A = [1, 2, 2, 2, 3, 5, 5, 9]. Compute how many times target = 2 appears using lower\_bound and upper\_bound (half-open intervals).

1. Goal:

   count(2) = upper\_bound(2) - lower\_bound(2)

   where:

   - •lower\_bound finds first index with A[i] ≥ 2
   - •upper\_bound finds first index with A[i] > 2
2. Compute lower\_bound(2):

   Initialize low=0, high=8 (n)

   While low < high:

   - •mid = 0 + (8-0)//2 = 4, A[4]=3

   A[mid] < 2? No (3 < 2 is false) → high = mid = 4

   - •mid = 0 + (4-0)//2 = 2, A[2]=2

   A[mid] < 2? No (2 < 2 false) → high = 2

   - •mid = 0 + (2-0)//2 = 1, A[1]=2

   A[mid] < 2? No → high = 1

   - •mid = 0 + (1-0)//2 = 0, A[0]=1

   A[mid] < 2? Yes → low = mid + 1 = 1

   Stop (low == high == 1). So lower\_bound(2) = 1.
3. Compute upper\_bound(2):

   Initialize low=0, high=8

   While low < high:

   - •mid = 4, A[4]=3

   A[mid] <= 2? No → high=4

   - •mid = 2, A[2]=2

   A[mid] <= 2? Yes → low = mid + 1 = 3

   - •mid = 3, A[3]=2

   A[mid] <= 2? Yes → low = 4

   Stop (low == high == 4). So upper\_bound(2) = 4.
4. Compute count:

   count = upper\_bound - lower\_bound = 4 - 1 = 3

**Insight:** Lower/upper bound treat equality differently. That tiny change ( < vs ≤ ) is what turns “find a match” into “find a boundary,” which is often more useful than returning any one index.

### Not found case and why the loop ends correctly

A = [3, 8, 10, 14, 17]. Search for target = 9 using the closed-interval exact-match binary search.

1. Initialize:

   low=0, high=4
2. Iteration 1:

   mid = 0 + (4-0)//2 = 2

   A[2]=10

   10 > 9 → high = mid - 1 = 1

   Interval becomes [0,1]
3. Iteration 2:

   mid = 0 + (1-0)//2 = 0

   A[0]=3

   3 < 9 → low = mid + 1 = 1

   Interval becomes [1,1]
4. Iteration 3:

   mid = 1 + (1-1)//2 = 1

   A[1]=8

   8 < 9 → low = mid + 1 = 2

   Interval becomes [2,1] (empty because low > high)
5. Loop ends because low <= high is false.

   Return -1 (not found).

**Insight:** The empty interval (low > high) is the precise signal that there is no index left where target could be, so “not found” is justified—not just a guess.

## Key Takeaways

- ✓

  Binary search requires a sorted array (nondecreasing is the usual assumption).
- ✓

  Maintain a search interval: with a closed interval, the loop invariant is “if target exists, it’s in [low, high].”
- ✓

  Use `mid = low + (high - low) // 2` to avoid overflow and to get correct integer rounding.
- ✓

  Closed interval exact-match pattern: `while low <= high`, then update with `low = mid + 1` or `high = mid - 1`.
- ✓

  Binary search runs in O(log n) time because each comparison discards about half the remaining candidates.
- ✓

  With duplicates, exact-match may return any occurrence; use lower\_bound / upper\_bound to get first/last positions and counts.
- ✓

  Be consistent about interval conventions ([low, high] vs [low, high)) to avoid off-by-one errors.

## Common Mistakes

- ✗

  Using the wrong loop condition for your interval convention (e.g., using `low < high` with updates meant for `[low, high]`).
- ✗

  Updating to `low = mid` or `high = mid` in a closed-interval exact-match search, which can cause infinite loops when low == mid or high == mid.
- ✗

  Computing `mid = (low + high) // 2` in a language where `low + high` can overflow, leading to negative or incorrect mid.
- ✗

  For duplicates, expecting the exact-match search to return the first (or last) occurrence without implementing the boundary-search variant.

## Practice

easy

Implement the closed-interval binary search that returns the index of target in a sorted array A, or -1 if not found. Then trace it on A = [1, 2, 4, 8, 16] with target = 8.

**Hint:** Use low=0, high=n-1, loop while low <= high, and update low=mid+1 or high=mid-1.

Show solution

Algorithm:

- •low=0, high=n-1
- •while low<=high:

mid=low+(high-low)//2

if A[mid]==target return mid

if A[mid]<target low=mid+1 else high=mid-1

- •return -1

Trace:

A=[1,2,4,8,16], target=8

low=0 high=4 mid=2 A[2]=4<8 → low=3

low=3 high=4 mid=3 A[3]=8==8 → return 3

medium

Given A = [1, 2, 2, 2, 3, 3, 10], find (a) lower\_bound(3) and (b) upper\_bound(3), and use them to compute how many 3s are in A.

**Hint:** Lower bound uses condition A[mid] < target; upper bound uses A[mid] <= target. Use a half-open interval [low, high) with high=n.

Show solution

A length n=7.

- •lower\_bound(3) returns first index with A[i] ≥ 3. The first 3 is at index 4, so lower\_bound(3)=4.
- •upper\_bound(3) returns first index with A[i] > 3. The first element >3 is 10 at index 6, so upper\_bound(3)=6.

Count of 3s = 6 - 4 = 2.

hard

You are given a sorted array A (nondecreasing) and a target. Modify binary search to return the index of the FIRST occurrence of target (or -1 if absent). Describe the rule for updating boundaries when you find equality.

**Hint:** When A[mid] == target, don’t stop immediately; keep searching left while preserving that the first occurrence is still in the interval.

Show solution

One approach (half-open lower\_bound style):

Compute i = lower\_bound(A, target) (first index with A[i] ≥ target). If i < n and A[i] == target, return i else return -1.

If you implement directly with a closed interval:

- •Keep an `ans = -1`.
- •When A[mid] == target: set ans=mid and move left: high = mid - 1.
- •When A[mid] < target: low = mid + 1.
- •When A[mid] > target: high = mid - 1.

Return ans at the end.

Key rule: on equality, shrink toward the side where the first occurrence could be (left), rather than terminating.

## Connections

- •Prerequisite refresh: [Arrays](/tech-tree/arrays/)
- •Complexity perspective: [Big O Notation](/tech-tree/big-o-notation/)
- •Next useful pattern: [Divide and Conquer](/tech-tree/divide-and-conquer/)
- •Boundary searching skill: [Lower Bound / Upper Bound](/tech-tree/lower-upper-bound/)
- •Data structures that use the same idea: [Binary Search Trees](/tech-tree/binary-search-trees/)
- •Optimization pattern: [Binary Search on Answer](/tech-tree/binary-search-on-answer/)

Quality: A (4.5/5)

[← back to tree](/tech-tree/)[browse all →](/tech-tree/inventory/)
