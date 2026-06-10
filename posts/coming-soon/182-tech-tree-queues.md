---
title: Queues
description: FIFO structure. Enqueue and dequeue operations.
date: '2026-07-01'
scheduled: '2026-12-29'
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
inspiration_url: https://templeton.host/tech-tree/queues/
inspiration_category: tech-tree
---

> Source-copy draft imported from [https://templeton.host/tech-tree/queues/](https://templeton.host/tech-tree/queues/). Names, domain references, and local media paths were adapted for Xavi Ablaza / getablaza.com.

[←Back to Tech Tree](/tech-tree/)

[inventory](/tech-tree/inventory/)[coverage](/tech-tree/coverage/)

# Queues

Data StructuresDifficulty: ★★☆☆☆Depth: 1Unlocks: 0

FIFO structure. Enqueue and dequeue operations.

## Interactive Visualization

⏮◀◀▶▶STEP0.25x1xZOOM

t=0s

## Core Concepts

- -First-In, First-Out (FIFO) ordering: elements exit in the same order they entered
- -Enqueue: insert an element at the rear of the queue
- -Dequeue: remove and return the element at the front of the queue

## Key Symbols & Notation

enqueue(Q, x) and dequeue(Q)

## Essential Relationships

- -Enqueue updates the rear and Dequeue updates the front; together these operations enforce FIFO order

## Prerequisites (2)

[Arrays5 atoms](/tech-tree/arrays/)[Linked Lists6 atoms](/tech-tree/linked-lists/)

## Referenced by (2)

Where this concept shows up in the operating-finance and personal-finance graphs.

### From Business (2)

[ThroughputBusiness

Throughput is fundamentally a queue-processing concept - items arrive, get serviced, exit - and the FIFO abstraction with enqueue/dequeue rates is the data structure foundation for reasoning about processing volume, backpressure, and the rate at which a system clears its backlog](/business/throughput/)[Pipeline VelocityBusiness

Pipeline stages are queues. Little's Law (L = λW) directly yields pipeline velocity: items in process equals throughput times cycle time. Queue depth at each stage reveals where work accumulates and flow stalls.](/business/pipeline-velocity/)

Advanced Learning Details

### Graph Position

16

Depth Cost

0

Fan-Out (ROI)

0

Bottleneck Score

1

Chain Length

### Cognitive Load

5

Atomic Elements

39

Total Elements

L2

Percentile Level

L3

Atomic Level

### All Concepts (15)

- - Queue as an abstract data type (ADT) - a container with a defined interface separate from implementation
- - FIFO (First-In-First-Out) ordering/discipline
- - Enqueue - operation that inserts/adds an element at the back (rear/tail) of the queue
- - Dequeue - operation that removes an element from the front (head) of the queue
- - Peek/Front - operation that returns the front element without removing it
- - Rear/Back access - operation that returns the element at the tail without removing it
- - Empty condition and isEmpty predicate
- - Full condition and isFull predicate (for bounded queues)
- - Bounded vs unbounded (capacity) queues - capacity as a limiting attribute
- - Circular queue / ring buffer as an array-based implementation that supports wrap-around
- - Head and tail indices (or pointers) specifically used to track front and rear positions in a queue implementation
- - Size attribute of a queue (number of stored elements) distinct from array length or list length
- - Underflow - error/condition when dequeuing from an empty queue
- - Overflow - error/condition when enqueuing into a full bounded queue
- - Constant-time (O(1)) enqueue and dequeue as the intended performance characteristic of queue operations

### Teaching Strategy

Self-serve tutorial - low prerequisites, straightforward concepts.

When tasks must be handled in the exact order they arrive—customers in a line, print jobs, network packets, or events in a UI—queues give you a simple rule that prevents “cutting”: first in, first out.

TL;DR:

A queue is a FIFO data structure: you **enqueue(Q, x)** at the rear and **dequeue(Q)** from the front. With the right implementation (linked list with head+tail, or a circular array), both operations can be O(1).

## What Is a Queue?

## Intuition first (why it exists)

Many problems are not about *finding* the best element—they’re about preserving *arrival order*. If items must be processed in the same order they were received, you want a structure that makes “the oldest item goes next” the default behavior.

That rule is **First-In, First-Out (FIFO)**:

- •The **first** element inserted is the **first** element removed.
- •No element can “jump ahead” of earlier elements.

A queue models a real-world line: you join the back, and you leave from the front.

## Definition

A **queue** is an abstract data type (ADT) supporting (at minimum) these operations:

- •**enqueue(Q, x)**: insert element x at the **rear/back** of Q
- •**dequeue(Q)**: remove and return the element at the **front** of Q

Common additional operations:

- •**front(Q)** (or peek): return the front element without removing it
- •**isEmpty(Q)**: whether Q has no elements
- •**size(Q)**: number of elements

## Core invariants (what must always be true)

If a queue currently stores elements in arrival order:

front → [a, b, c] → rear

then:

- •dequeue(Q) returns **a** (the oldest)
- •after enqueue(Q, x), the order becomes:

front → [a, b, c, x] → rear

This “order preservation” is the whole point.

## Abstract vs implementation

A queue is the *behavior*. You can implement that behavior using:

- •an array (with indices that move)
- •a linked list (with pointers)

The same FIFO rules apply regardless.

## Why you should care about O(1)

Queues are often used in performance-sensitive pipelines (scheduling, buffering, BFS). If every dequeue requires shifting many elements, the queue becomes a bottleneck. So we’ll focus on implementations where enqueue and dequeue are **O(1)** in the usual case.

## Core Mechanic 1: FIFO Ordering and the Enqueue/Dequeue Contract

## Why the contract matters

Data structures are powerful because they *restrict* what you can do. That restriction creates guarantees.

For a queue, the restriction is:

- •you only insert at the **rear**
- •you only remove from the **front**

This gives a guarantee:

- •the next item out is always the earliest item still inside

## Thinking in time

A useful mental model is timestamps.

- •When you enqueue(Q, x), x gets a “time of arrival” tₓ.
- •dequeue(Q) must always return the element with the smallest t among elements still in Q.

So if you enqueue in order x₁, x₂, x₃, then you must dequeue in the same order.

## A tiny correctness proof (informal)

Assume we enqueue items x₁, x₂, …, xₙ.

At any time, the queue stores a suffix of that sequence (some earliest items may have been dequeued already).

- •The **front** is always the earliest remaining item.
- •dequeue removes that item.

So dequeue order is x₁, x₂, …, xₙ.

## Operation semantics

Let Q be a queue.

### enqueue(Q, x)

- •Effect: Q grows by 1
- •x becomes the new rear
- •No existing relative order changes

### dequeue(Q)

- •Effect: Q shrinks by 1
- •Returns the front element
- •The next element becomes the new front

## Underflow: the empty-queue case

If Q is empty, dequeue(Q) has no element to return.

Different APIs handle this differently:

- •throw an error/exception
- •return a special value (like null)
- •return a pair (successFlag, value)

Regardless of API, the key idea is: **dequeue requires Q to be non-empty**.

## Comparing a queue to nearby structures

Queues often get confused with stacks and deques. It helps to compare them directly:

| Structure | Insert | Remove | Order rule | Typical use |
| --- | --- | --- | --- | --- |
| Stack | push at top | pop at top | LIFO | undo, recursion |
| Queue | enqueue at rear | dequeue at front | FIFO | scheduling, buffering |
| Deque | both ends | both ends | flexible | sliding windows |

The FIFO guarantee is what makes a queue ideal for fairness (first come, first served).

## Core Mechanic 2: Implementing Queues Efficiently (Linked List vs Circular Array)

## Why implementation details matter

The ADT says “insert at rear, remove from front,” but you still have to store the elements somewhere.

A common beginner mistake is implementing a queue with a plain array and doing:

- •enqueue: append at end (fine)
- •dequeue: remove at index 0 and shift everything left (expensive)

That shift is O(n) per dequeue. We want O(1).

We’ll look at two standard O(1) implementations.

---

## Option A: Linked list with head and tail pointers

You already know linked lists support O(1) insert/delete *if you have a pointer to the right place*.

### Representation

Maintain:

- •head: pointer to the front node
- •tail: pointer to the rear node

Each node stores (value, next).

Front is head, rear is tail.

### enqueue(Q, x) in O(1)

- •Create new node n with value x
- •Set tail.next = n (if tail exists)
- •Update tail = n
- •If the queue was empty (head is null), set head = tail

### dequeue(Q) in O(1)

- •If head is null, underflow
- •Save head.value to return
- •Move head = head.next
- •If head becomes null (queue is now empty), set tail = null

### Complexity

- •Time: enqueue O(1), dequeue O(1)
- •Space: O(n) nodes, plus pointer overhead

### Pros/cons

| Aspect | Linked-list queue |
| --- | --- |
| Worst-case time per op | O(1) |
| Memory overhead | higher (pointers) |
| Cache friendliness | worse (non-contiguous) |
| Simplicity | very straightforward |

---

## Option B: Circular array (ring buffer)

Arrays are contiguous and cache-friendly, but we must avoid shifting.

### Key idea

Instead of physically moving elements, keep two indices:

- •**front**: where the next dequeue reads
- •**rear**: where the next enqueue writes

Indices “wrap around” using modulo arithmetic.

### Representation

Let A be an array of capacity C.

Maintain:

- •frontIndex (f)
- •rearIndex (r)
- •size (s)

Invariants:

- •0 ≤ f < C
- •0 ≤ r < C
- •0 ≤ s ≤ C

### Enqueue in a ring buffer

To enqueue(Q, x):

1) If s == C, the buffer is full (either error or resize)

2) Write A[r] = x

3) Update r = (r + 1) mod C

4) Update s = s + 1

### Dequeue in a ring buffer

To dequeue(Q):

1) If s == 0, underflow

2) Read x = A[f]

3) (Optional) clear A[f]

4) Update f = (f + 1) mod C

5) Update s = s − 1

6) Return x

### Why modulo gives “wrap-around”

When r reaches C − 1, adding 1 yields C. Taking mod C maps it back to 0:

(r + 1) mod C = 0

So indices cycle through 0, 1, …, C − 1, 0, 1, …

### Complexity

- •Time: enqueue O(1), dequeue O(1)
- •Space: O(C)

### The “full vs empty” ambiguity

If you only store f and r, then f == r could mean:

- •empty (no elements)
- •full (wrapped around)

That’s why we track **size s** (or keep one slot empty as a convention).

### Pros/cons

| Aspect | Circular-array queue |
| --- | --- |
| Worst-case time per op | O(1) (amortized O(1) if resizing) |
| Memory overhead | low |
| Cache friendliness | good |
| Implementation pitfalls | off-by-one, full/empty logic |

---

## Choosing between them

If you need:

- •**fixed maximum capacity** and speed → circular array is great
- •**unbounded growth** with simple logic → linked list is great

In real systems, you’ll often see both depending on constraints.

## Application/Connection: Where Queues Show Up (and Why FIFO Is the Right Tool)

## Why queues are everywhere

Queues appear whenever you have a mismatch between:

- •the **rate of arrival** of work/items
- •the **rate of processing** of work/items

A queue buffers the difference, and FIFO provides a fairness policy that users and systems expect.

## 1) Scheduling and task processing

Imagine a single worker processing jobs:

- •jobs arrive over time
- •the worker can process one at a time

A FIFO queue ensures earlier jobs are not starved by later jobs.

Examples:

- •printer spooler
- •background job runner
- •customer support ticket handling (in its simplest form)

## 2) Buffers in I/O and networking

Network packets arrive; your application consumes them.

- •If packets arrive faster than you can process, you queue them.
- •FIFO matches the typical “arrival order” semantics.

Similar buffering exists in:

- •keyboard input events
- •audio playback buffers

## 3) Breadth-first search (BFS) (preview connection)

BFS explores a graph “layer by layer.”

The reason a queue is the right tool:

- •nodes discovered earlier should be expanded earlier
- •this preserves increasing distance from the start

Even if you haven’t studied graphs yet, the pattern is:

1) enqueue the start

2) repeatedly dequeue the next node to process

3) enqueue newly discovered neighbors

FIFO is what keeps the exploration in layers.

## 4) Producer–consumer pipelines

A classic architecture:

- •Producer creates items
- •Consumer processes items

A queue decouples them so producer and consumer can run at different speeds.

## Practical API behaviors to watch for

When used in real code, queue operations must define what happens when:

- •dequeue on empty (underflow)
- •enqueue on full (if bounded)

This matters for correctness, not just performance.

## Big-picture connection

Queues are a “building block” structure: once you trust FIFO ordering and O(1) operations, you can build larger systems (schedulers, simulations, graph algorithms) with simple, predictable behavior.

## Worked Examples (3)

### Example 1: Trace FIFO Order Through Operations

Start with an empty queue Q. Perform:

1) enqueue(Q, 10)

2) enqueue(Q, 20)

3) enqueue(Q, 30)

4) dequeue(Q)

5) enqueue(Q, 40)

6) dequeue(Q)

7) dequeue(Q)

What values are returned by the dequeues, and what remains in Q at the end?

1. Initial state: Q = [ ] (empty)

   Front = Rear (conceptually), size = 0
2. 1) enqueue(Q, 10)

   Q = [10]

   Front element is 10, rear element is 10
3. 2) enqueue(Q, 20)

   Q = [10, 20]

   Front is 10 (oldest), rear is 20 (newest)
4. 3) enqueue(Q, 30)

   Q = [10, 20, 30]

   Front is 10, rear is 30
5. 4) dequeue(Q)

   By FIFO, return the oldest element: 10

   Now Q = [20, 30]
6. 5) enqueue(Q, 40)

   Insert at rear

   Q = [20, 30, 40]
7. 6) dequeue(Q)

   Return front: 20

   Now Q = [30, 40]
8. 7) dequeue(Q)

   Return front: 30

   Now Q = [40]
9. Final: dequeued values were 10, then 20, then 30

   Remaining queue contents: [40] (front and rear are both 40)

**Insight:** FIFO is easiest to verify by labeling items as “older” vs “newer.” Enqueue never changes the order of older items; dequeue always removes the oldest remaining item.

### Example 2: Circular Array (Ring Buffer) Index Walkthrough

Implement Q using an array A of capacity C = 5 with front index f, rear index r, and size s. Start empty:

f = 0, r = 0, s = 0.

Perform:

enqueue 1, enqueue 2, enqueue 3, dequeue, dequeue, enqueue 4, enqueue 5, enqueue 6.

Track (f, r, s) and the logical queue contents after each step.

1. Start:

   A = [\_, \_, \_, \_, \_]

   f = 0, r = 0, s = 0

   Logical Q = [ ]
2. enqueue 1:

   Write A[r]=A[0]=1

   r = (0+1) mod 5 = 1

   s = 1

   A = [1, \_, \_, \_, \_]

   Logical Q = [1] (front at f=0)
3. enqueue 2:

   A[1]=2

   r = (1+1) mod 5 = 2

   s = 2

   A = [1, 2, \_, \_, \_]

   Logical Q = [1, 2]
4. enqueue 3:

   A[2]=3

   r = 3

   s = 3

   A = [1, 2, 3, \_, \_]

   Logical Q = [1, 2, 3]
5. dequeue:

   Read A[f]=A[0]=1 (return 1)

   f = (0+1) mod 5 = 1

   s = 2

   A = [1, 2, 3, \_, \_] (optional clear A[0])

   Logical Q = [2, 3]
6. dequeue:

   Read A[1]=2 (return 2)

   f = (1+1) mod 5 = 2

   s = 1

   Logical Q = [3]
7. enqueue 4:

   Write A[r]=A[3]=4

   r = (3+1) mod 5 = 4

   s = 2

   A = [1, 2, 3, 4, \_]

   Logical Q = [3, 4] (front at index 2)
8. enqueue 5:

   Write A[4]=5

   r = (4+1) mod 5 = 0 (wrap around)

   s = 3

   A = [1, 2, 3, 4, 5]

   Logical Q = [3, 4, 5]
9. enqueue 6:

   Write A[0]=6 (this slot is free logically because f=2 and s=3)

   r = (0+1) mod 5 = 1

   s = 4

   A = [6, 2, 3, 4, 5]

   Logical Q reading from f=2 for s=4 items:

   Indices: 2,3,4,0 → values [3,4,5,6]

**Insight:** A ring buffer reuses array slots by moving indices, not elements. The physical array may look “out of order,” but the logical order is defined by (f, s) and modular indexing.

### Example 3: Linked-List Queue Pointer Updates (Empty → One → Empty)

You implement a queue using a singly linked list with head and tail pointers. Show what happens to head and tail when you:

1) enqueue(Q, 'A') into an empty queue

2) dequeue(Q)

Focus on the pointer updates and the special empty-case handling.

1. Initial state:

   head = null

   tail = null

   Q is empty
2. 1) enqueue(Q, 'A'):

   Create node n with n.value='A', n.next=null

   Because tail is null (empty queue), set:

   head = n

   tail = n

   Now head and tail both point to the same single node
3. Queue state:

   head → ['A'] → null

   ↑

   tail
4. 2) dequeue(Q):

   Check head != null (ok)

   Return value = head.value = 'A'

   Move head = head.next = null

   Now the queue is empty again, so also set tail = null
5. Final state:

   head = null

   tail = null

   Returned 'A'

**Insight:** In a linked-list queue, the only tricky case is transitioning to or from empty. When the last element is removed, you must update both head and tail to null.

## Key Takeaways

- ✓

  A queue is an ADT defined by FIFO ordering: the earliest enqueued element is the earliest dequeued element.
- ✓

  enqueue(Q, x) inserts at the rear; dequeue(Q) removes and returns the front.
- ✓

  A naive array queue that shifts elements on dequeue costs O(n) per dequeue and should be avoided.
- ✓

  A linked list with both head and tail pointers supports enqueue and dequeue in O(1).
- ✓

  A circular array (ring buffer) supports enqueue and dequeue in O(1) using indices and modulo arithmetic.
- ✓

  To avoid ambiguity between empty and full in an array queue, track size s (or use a “one empty slot” convention).
- ✓

  Queues naturally model fairness and buffering in real systems: schedulers, I/O, networking, and BFS.

## Common Mistakes

- ✗

  Implementing dequeue on an array by removing index 0 and shifting everything left (O(n) per operation).
- ✗

  Forgetting the empty-case updates: after removing the last node in a linked-list queue, not setting tail = null.
- ✗

  In a circular array, confusing the meaning of front and rear indices (e.g., rear pointing at last element instead of next write position).
- ✗

  Not defining behavior for underflow (dequeue on empty) or overflow (enqueue on full) in a bounded queue.

## Practice

easy

You have Q initially empty. Perform: enqueue 5, enqueue 7, dequeue, enqueue 9, dequeue, enqueue 11. What are the dequeued values and what is left in Q (front→rear)?

**Hint:** Write the queue contents after each operation. Dequeue always removes the current front.

Show solution

Start Q=[]

enq 5 → [5]

enq 7 → [5,7]

deq → returns 5, Q=[7]

enq 9 → [7,9]

deq → returns 7, Q=[9]

enq 11 → [9,11]

Dequeued values: 5, 7

Remaining Q (front→rear): [9, 11]

medium

Circular array queue with capacity C=4. Start f=0, r=0, s=0. Do: enqueue A, enqueue B, enqueue C, dequeue, enqueue D, enqueue E. Give final (f, r, s) and the logical queue order. Assume enqueue on full is not allowed—check whether it becomes full.

**Hint:** Update r on enqueue, f on dequeue, and s on both. Wrap with mod 4. Full means s=C.

Show solution

Start f=0,r=0,s=0

Enq A: write at r=0, r=1, s=1

Enq B: write at r=1, r=2, s=2

Enq C: write at r=2, r=3, s=3

Deq: return at f=0, f=1, s=2

Enq D: write at r=3, r=(3+1) mod 4=0, s=3

Enq E: write at r=0, r=1, s=4 (now full)

Final: f=1, r=1, s=4

Logical order from f=1 for 4 items: indices 1,2,3,0 → [B, C, D, E]

hard

Design question: You need a queue for a high-throughput system where memory allocations are expensive and you know an upper bound of 1,000,000 elements. Would you choose a linked-list queue or a circular-array queue? Justify in terms of time and space.

**Hint:** Think about pointer overhead and per-operation allocations vs a fixed contiguous buffer.

Show solution

A circular-array queue is a strong choice here. Because you know a hard upper bound, you can allocate an array of capacity 1,000,000 once, avoiding per-enqueue node allocations. Enqueue/dequeue remain O(1) via index updates, and memory overhead is low (no next pointers). A linked-list queue would also have O(1) operations, but it requires allocating a node per element (allocation overhead) and adds pointer memory overhead plus worse cache locality.

## Connections

- •[Arrays](/tech-tree/arrays/)
- •[Linked Lists](/tech-tree/linked-lists/)
- •[Stacks](/tech-tree/stacks/)
- •[Deques](/tech-tree/deques/)
- •[Breadth-First Search (BFS)](/tech-tree/bfs/)
- •[Amortized Analysis](/tech-tree/amortized-analysis/)

Quality: A (4.7/5)

[← back to tree](/tech-tree/)[browse all →](/tech-tree/inventory/)
