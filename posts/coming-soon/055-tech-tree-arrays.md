---
title: Arrays
description: Contiguous memory storing elements by index. O(1) access, O(n) search.
date: '2026-07-01'
scheduled: '2026-08-24'
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
inspiration_url: https://templeton.host/tech-tree/arrays/
inspiration_category: tech-tree
---

> Source-copy draft imported from [https://templeton.host/tech-tree/arrays/](https://templeton.host/tech-tree/arrays/). Names, domain references, and local media paths were adapted for Xavi Ablaza / getablaza.com.

[←Back to Tech Tree](/tech-tree/)

[inventory](/tech-tree/inventory/)[coverage](/tech-tree/coverage/)

# Arrays

Data StructuresDifficulty: ★☆☆☆☆Depth: 0Unlocks: 29

Contiguous memory storing elements by index. O(1) access, O(n) search.

## Interactive Visualization

⏮◀◀▶▶STEP0.25x1xZOOM

t=0s

## Core Concepts

- -Contiguous block of memory storing elements sequentially
- -Elements identified by an integer index (position)
- -Direct (random) access to an element by computing its memory location from its index (constant-time)

## Key Symbols & Notation

A[i] (array element access: array name with integer index)

## Essential Relationships

- -element\_address = base\_address + index \* element\_size (index maps to memory offset; enables O(1) access)

## Unlocks (7)

[Graph Representationslvl 2](/tech-tree/graph-representations/)[Stackslvl 2](/tech-tree/stacks/)[Hash Tableslvl 2](/tech-tree/hash-tables/)[Heapslvl 2](/tech-tree/heaps/)[Queueslvl 2](/tech-tree/queues/)[Basic Sortinglvl 2](/tech-tree/sorting-basic/)[Binary Searchlvl 2](/tech-tree/binary-search/)

Advanced Learning Details

### Graph Position

5

Depth Cost

29

Fan-Out (ROI)

16

Bottleneck Score

0

Chain Length

### Cognitive Load

5

Atomic Elements

27

Total Elements

L1

Percentile Level

L3

Atomic Level

### All Concepts (13)

- - Array: a collection of elements stored in one contiguous block of memory
- - Contiguous memory: elements are laid out adjacent to each other with no gaps
- - Index: an integer position used to name or locate a particular element in the array
- - Element: an individual value stored at one index in the array
- - Base address: the memory address of the first element of the array
- - Offset: the distance from the base address to an element determined by its index
- - Element size: the number of bytes used to store a single array element (affects offset calculation)
- - Address calculation for access: computing an element's address from base, index, and element size
- - Valid index range (array bounds): the set of indices that correspond to actual stored elements
- - Constant-time access (O(1)) by index: retrieving an element via direct address computation
- - Linear search (O(n)): finding an element by checking elements one-by-one
- - Random access: ability to access any element directly by index without traversing preceding elements
- - Memory locality (locality of reference) as a consequence of contiguity: consecutive elements are near each other in memory

### Teaching Strategy

Self-serve tutorial - low prerequisites, straightforward concepts.

You’re writing a tiny image editor. The user clicks at pixel (x=120, y=45) and expects the color to change instantly—no waiting, no “searching” through the whole image. The reason this can feel instantaneous is that the pixels are typically stored in an array (or something array-like), so the program can jump straight to “pixel #k” in O(1) time.

Curiosity challenge (keep this in mind as you read): If arrays are so fast, why is inserting a new element at the very front of an array usually slow?

TL;DR:

An array stores elements in a contiguous block of memory and uses an integer index i to access A[i] in constant time by computing its address. This makes reading/writing by index O(1), but operations that require shifting many elements (like inserting at the front) take O(n).

## What Is an Array?

## The idea

An **array** is a data structure that stores a fixed number of elements **next to each other in memory** (contiguously), and lets you refer to each element using an **integer index**.

If we name an array **A**, then:

- •**A[0]** is the first element (in many languages)
- •**A[1]** is the second element
- •…
- •**A[i]** is the element at position *i*

That simple indexing idea—**A[i]**—is the signature move of arrays.

## Why we care (before details)

Arrays are foundational because they give you something incredibly powerful:

- •**Direct (random) access**: “Go to element 120 right now.”

Many other data structures either build on arrays (stacks, heaps) or are compared against arrays (linked lists, hash tables).

## A concrete mental model: numbered lockers

Imagine a hallway of lockers, each locker the same size, in a single line. Locker #0, #1, #2, … Each locker holds exactly one value.

If you want locker #120, you don’t start at #0 and walk 120 steps checking each locker. You go straight there because the lockers are in order.

That is the feeling arrays provide: **jumping directly** to a position.

## What “contiguous memory” really means

“Contiguous” means the elements are stored back-to-back in memory addresses:

- •A[0] at address `base`
- •A[1] at address `base + elementSize`
- •A[2] at address `base + 2*elementSize`

This layout is the entire reason arrays can do O(1) indexing.

## Indices and bounds

Indices are integers. Common conventions:

- •0-based indexing (C, Java, Python lists behave like 0-based arrays)
- •1-based indexing (MATLAB, some math notation)

Important: indices must be in range.

If the array length is n, valid indices are typically 0…n−1.

Accessing outside that range is called **out-of-bounds**. Some languages catch it with an error; lower-level languages might do something worse (like reading random memory).

## Arrays vs “array-like”

In everyday programming, you’ll see:

- •**Static arrays**: fixed size (common in low-level languages)
- •**Dynamic arrays**: grow as needed (e.g., Python’s list, Java’s ArrayList). These *still* store elements contiguously most of the time, but may occasionally resize and move.

In this lesson, the core mechanics are the same: **contiguous storage + integer index**.

## Core Mechanic 1: O(1) Indexing via Address Computation

## Why indexing can be constant time

When you write **A[i]**, the computer doesn’t “look for” the i-th element.

Instead, it computes the memory address directly.

### Address formula

Let:

- •`base(A)` be the memory address where A[0] starts
- •`s` be the size (in bytes) of one element (e.g., 4 bytes for a 32-bit integer)
- •`i` be the index

Then the address of A[i] is:

addr(A[i])=base(A)+i⋅s\text{addr}(A[i]) = \text{base}(A) + i \cdot saddr(A[i])=base(A)+i⋅s

That’s just multiplication and addition—constant-time arithmetic—so indexing is **O(1)**.

### Why equal-sized elements matter

This formula relies on each element having the same size.

- •If every locker is the same width, you can compute “locker #i” easily.
- •If lockers had random widths, you’d need to sum widths to find the start of locker #i, which could take O(n).

That’s why classic arrays store uniform element sizes.

## Read and write are both O(1)

Once the address is computed:

- •Reading A[i] is O(1)
- •Writing A[i] = value is O(1)

So arrays are excellent for:

- •pixel buffers (image editing)
- •audio samples
- •game grids / tile maps
- •lookup tables
- •any workload that frequently accesses “the i-th thing”

## A 2D example: grids (still arrays underneath)

Suppose you have a 2D grid with `rows` and `cols`. Many systems store it as a 1D array in **row-major order**.

Let grid[y][x] be the cell at row y, column x.

Then the 1D index is:

i=y⋅cols+xi = y \cdot \text{cols} + xi=y⋅cols+x

So:

- •grid[0][0] → i = 0
- •grid[0][1] → i = 1
- •grid[1][0] → i = cols

This is the same O(1) indexing idea, just with an extra step to compute i.

## A note on caching (a hidden superpower)

Because arrays are contiguous, iterating through them tends to be fast in practice.

Modern CPUs fetch memory in chunks (cache lines). If you access A[0], A[1], A[2], … sequentially, the CPU often already has the next values nearby.

So arrays are not just theoretically efficient—**they’re often practically fast**.

## Core Mechanic 2: The Real Costs—Searching, Inserting, and Deleting

Arrays are fast at one thing: **index-based access**.

But many tasks aren’t “give me A[i]”. They’re:

- •“Find the value 42.”
- •“Insert a new element at the beginning.”
- •“Delete the element in the middle.”

This is where the tradeoffs show up.

## Searching: why it’s often O(n)

If the array is unsorted and you want to find a particular value x, you usually must scan:

- •check A[0]
- •check A[1]
- •…
- •check A[n−1]

In the worst case, x is at the end or not present, so you check n elements.

That’s **O(n)**.

### Sorted arrays change the story

If the array is sorted, you can use **binary search**, which is O(log n).

But sorting has its own costs (and maintaining sorted order makes insertions harder). This lesson’s baseline claim “O(n) search” assumes **no additional structure**.

## Inserting: the curiosity challenge

Recall the question: *Why is inserting at the front slow?*

Consider inserting a new element at index 0.

If you need to keep the existing order, everything must shift right:

- •old A[0] moves to A[1]
- •old A[1] moves to A[2]
- •…

That’s potentially moving **n elements**, so insertion at the front is **O(n)**.

### Inserting in the middle is also O(n)

If you insert at index k, then elements k…n−1 shift right.

Worst case k=0 → shift all n.

So insertion is O(n) in the worst case.

### Appending can be O(1) (sometimes)

If you insert at the end (append), you might not need to shift anything.

- •Static array: can’t append if it’s full.
- •Dynamic array: can append in **amortized O(1)**, but occasionally it resizes.

We’ll keep the basic mental model: order-preserving insertions generally require shifting → O(n).

## Deleting: also involves shifting

Deleting A[k] while preserving order means:

- •A[k+1] shifts left to fill the gap
- •…

Worst case: delete near the front → shift almost all elements.

So deletion is typically **O(n)**.

## Summary table: typical time costs

| Operation (unsorted array) | Typical Time | Why |
| --- | --- | --- |
| Read A[i] | O(1) | direct address computation |
| Write A[i] | O(1) | direct address computation |
| Search for value x | O(n) | may need full scan |
| Insert at front/middle | O(n) | shift elements to make room |
| Delete at front/middle | O(n) | shift elements to close gap |
| Iterate through all elements | O(n) | visit each element once |

## Space: compact and predictable

Arrays store elements with little overhead:

- •no extra “next pointer” fields
- •no per-element object metadata (in low-level representations)

This compactness is why arrays are often used as the underlying storage for many other structures.

## Application/Connection: Why Arrays Power So Many Data Structures

Arrays show up everywhere because they provide:

1) **fast indexing**

2) **cache-friendly iteration**

3) **simple memory layout**

Here are key connections to what you’ll learn next.

## Stacks and queues

A **stack** (LIFO) often uses a dynamic array underneath:

- •push: write to the next free index
- •pop: decrease size counter

Most operations become O(1) because you only modify the end.

A **queue** (FIFO) can also be built on an array using a **circular buffer**:

- •head and tail indices wrap around
- •avoids shifting on dequeue

This is an important trick: arrays are bad at removing from the front *if you shift*, but great if you redesign the indexing.

## Heaps (priority queues)

A binary heap is typically stored in an array.

For 0-based indexing:

- •parent(i) = ⌊(i−1)/2⌋
- •left(i) = 2i + 1
- •right(i) = 2i + 2

This is a beautiful example of arrays enabling a tree-like structure without pointers.

## Hash tables

Many hash table designs use arrays internally:

- •an array of buckets
- •or an array of entries

The hash function maps a key to an integer index.

That index is used to jump to a location quickly (again, array indexing).

## Graph representations

Graphs can be represented with an **adjacency matrix**, which is basically a 2D array:

- •matrix[u][v] tells whether there is an edge u→v
- •O(1) edge query
- •but space is O(n²)

Arrays make that matrix representation possible and efficient to access.

## When arrays are the wrong tool

Arrays struggle when you need lots of:

- •insertions/deletions in the middle
- •growth without occasional resizing costs (for dynamic arrays)

In those cases, other structures (linked lists, balanced trees) can help—at the cost of losing O(1) random access.

Arrays are not “best.” They are **specific**.

And that specificity—fast direct access—makes them the foundation for much of practical computing.

## Worked Examples (3)

### Compute the Address of A[i] (and see why it’s O(1))

Suppose an integer array A starts at base address 1000 (in bytes). Each integer takes s = 4 bytes. Compute the address of A[7], and explain why this does not depend on the array length n.

1. Write the indexing address formula:

   addr(A[i])=base(A)+i⋅s\text{addr}(A[i]) = \text{base}(A) + i \cdot saddr(A[i])=base(A)+i⋅s
2. Substitute the known values: base(A)=1000, i=7, s=4:

   addr(A[7])=1000+7⋅4\text{addr}(A[7]) = 1000 + 7 \cdot 4addr(A[7])=1000+7⋅4
3. Compute the multiplication:

   7⋅4=287 \cdot 4 = 287⋅4=28
4. Add to the base:

   addr(A[7])=1000+28=1028\text{addr}(A[7]) = 1000 + 28 = 1028addr(A[7])=1000+28=1028
5. Reason about runtime: this required a constant number of arithmetic operations (one multiply, one add), regardless of whether the array has 10 elements or 10 million.

**Insight:** Array indexing is fast because it’s address computation, not searching. The computer “jumps” directly to the right memory location.

### Why Inserting at the Front Takes O(n)

You have an array A of length 5: A = [10, 20, 30, 40, 50]. You want to insert 5 at index 0 and keep the order of existing elements.

1. Identify what must happen to preserve order: every existing element must move one position to the right.
2. Show the shift from the back to avoid overwriting values:

   - •Move A[4] → A[5] (50 shifts right)
   - •Move A[3] → A[4] (40 shifts right)
   - •Move A[2] → A[3] (30 shifts right)
   - •Move A[1] → A[2] (20 shifts right)
   - •Move A[0] → A[1] (10 shifts right)
3. Now index 0 is free. Write the new value:

   - •Set A[0] = 5
4. Resulting array:

   A = [5, 10, 20, 30, 40, 50]
5. Count the work: you performed 5 shifts (proportional to n). In general, inserting at the front may require shifting n elements → O(n).

**Insight:** The array’s contiguity is both the superpower (O(1) indexing) and the limitation (order-preserving inserts/deletes force shifting many elements).

### 2D Grid Stored in a 1D Array (Row-Major Indexing)

You have a grid with rows = 3 and cols = 4. It’s stored as a 1D array data[] of length 12 in row-major order. Find the 1D index for the cell at (y=2, x=1), and describe the access.

1. Use the row-major mapping from (y, x) to 1D index i:

   i=y⋅cols+xi = y \cdot \text{cols} + xi=y⋅cols+x
2. Substitute y=2, cols=4, x=1:

   i=2⋅4+1i = 2 \cdot 4 + 1i=2⋅4+1
3. Compute:

   i=8+1=9i = 8 + 1 = 9i=8+1=9
4. So grid[2][1] is stored at data[9]. Access is O(1) because it becomes a single array index operation.

**Insight:** Many “2D arrays” are implemented as 1D arrays with an indexing formula. Arrays plus arithmetic can represent rich structures efficiently.

## Key Takeaways

- ✓

  An array stores elements contiguously in memory, enabling fast sequential and random access patterns.
- ✓

  The core operation A[i] is O(1) because the address is computed as base(A) + i·elementSize.
- ✓

  Arrays excel when you frequently read/write by index (tables, pixel buffers, sample arrays, grids).
- ✓

  Unsorted search is typically O(n) because you may need to scan every element.
- ✓

  Order-preserving insertion/deletion in the front or middle is O(n) due to shifting elements.
- ✓

  Appending to a dynamic array is often amortized O(1), but occasional resizing can be costly.
- ✓

  Arrays are commonly used as the underlying storage for stacks, heaps, hash tables, and adjacency matrices.

## Common Mistakes

- ✗

  Assuming arrays are fast for every operation: O(1) access does not mean O(1) insertion or deletion in the middle.
- ✗

  Off-by-one indexing errors (especially mixing 0-based and 1-based thinking).
- ✗

  Out-of-bounds access: using an index < 0 or ≥ n (can crash or corrupt memory in some languages).
- ✗

  Confusing “search by value” with “access by index”: A[i] is O(1), but finding which i contains x is often O(n).

## Practice

easy

An array B starts at base address 2000. Each element is 8 bytes. What is the address of B[13]?

**Hint:** Use addr(B[i]) = base(B) + i·s.

Show solution

Using $addr(B[i])=base(B)+i⋅s\text{addr}(B[i]) = \text{base}(B) + i \cdot saddr(B[i])=base(B)+i⋅s$ with base=2000, i=13, s=8:

addr(B[13])=2000+13⋅8=2000+104=2104.\text{addr}(B[13]) = 2000 + 13 \cdot 8 = 2000 + 104 = 2104.addr(B[13])=2000+13⋅8=2000+104=2104.

easy

You have an array of length n. What is the worst-case time complexity to delete the element at index 0 while preserving order? Explain in one or two sentences.

**Hint:** Think about what happens to all remaining elements after the deletion.

Show solution

O(n). After removing index 0, every element A[1]…A[n−1] must shift one position left to fill the gap, which is proportional to n.

medium

A 5×6 grid is stored in a 1D array in row-major order. What index i corresponds to (y=3, x=4)? Also, what is the range of valid indices?

**Hint:** Row-major uses i = y·cols + x. The total length is rows·cols.

Show solution

cols=6, so $i=y⋅cols+x=3⋅6+4=18+4=22.i = y \cdot \text{cols} + x = 3 \cdot 6 + 4 = 18 + 4 = 22.i=y⋅cols+x=3⋅6+4=18+4=22.$ The total length is 5·6=30, so valid indices are 0…29.

## Connections

- •Next: [Stacks](/tech-tree/stacks/) — often implemented with an array and a “top” index.
- •Next: [Queues](/tech-tree/queues/) — arrays can implement queues efficiently using a circular buffer.
- •Next: [Heaps](/tech-tree/heaps/) — stored compactly in an array using index math (parent/children formulas).
- •Next: [Hash Tables](/tech-tree/hash-tables/) — typically use arrays internally for buckets/slots.
- •Next: [Graph Representations](/tech-tree/graph-representations/) — adjacency matrices are 2D arrays with O(1) edge checks.

Quality: A (4.5/5)

[← back to tree](/tech-tree/)[browse all →](/tech-tree/inventory/)
