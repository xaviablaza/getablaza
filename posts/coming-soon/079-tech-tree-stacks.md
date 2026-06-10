---
title: Stacks
description: LIFO structure. Push and pop operations.
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
permalink: /tech-tree/stacks/
---

[←Back to Tech Tree](/tech-tree/)

[inventory](/tech-tree/inventory/)[coverage](/tech-tree/coverage/)

# Stacks

Data StructuresDifficulty: ★★☆☆☆Depth: 1Unlocks: 12

LIFO structure. Push and pop operations.

## Interactive Visualization

⏮◀◀▶▶STEP0.25x1xZOOM

t=0s

## Core Concepts

- -Last-In, First-Out (LIFO) ordering
- -Push: add an element to the top of the stack
- -Pop: remove and return the top element from the stack

## Key Symbols & Notation

push(S, x) and pop(S) (standard operation notation)

## Essential Relationships

- -pop returns the most recently pushed element not yet popped; push and pop operate only at the top (this enforces LIFO)

## Prerequisites (2)

[Arrays5 atoms](/tech-tree/arrays/)[Linked Lists6 atoms](/tech-tree/linked-lists/)

## Unlocks (1)

[Recursionlvl 2](/tech-tree/recursion/)

Advanced Learning Details

### Graph Position

16

Depth Cost

12

Fan-Out (ROI)

6

Bottleneck Score

1

Chain Length

### Cognitive Load

5

Atomic Elements

33

Total Elements

L1

Percentile Level

L3

Atomic Level

### All Concepts (14)

- - Stack as an abstract data type (ADT) with restricted access (only top accessible)
- - LIFO ordering (Last-In-First-Out): most recently pushed element is first popped
- - push operation: add an element to the top of the stack
- - pop operation: remove and return the element at the top of the stack
- - peek / top operation: read the top element without removing it
- - isEmpty predicate: check whether the stack contains no elements
- - isFull predicate (for fixed-capacity stacks): check whether stack has reached capacity
- - size operation / maintaining the current element count
- - top pointer / top index concept: a single reference or index indicating the stack's top
- - stack underflow: error/state when pop is attempted on an empty stack
- - stack overflow: error/state when push is attempted on a full fixed-capacity stack
- - array-backed stack implementation pattern: use an index (top) into an array to represent the stack
- - linked-list-backed stack implementation pattern: use head pointer as the top, push/pop by inserting/removing head node
- - dynamic-resizing behavior for array-backed stacks: doubling (or similar) growth causing amortized O(1) push

### Teaching Strategy

Self-serve tutorial - low prerequisites, straightforward concepts.

A stack is the simplest “do one thing, then undo it” data structure. If you can push work onto a stack and later pop it back off, you can build function calls (recursion), undo/redo, backtracking, and depth-first search.

TL;DR:

A stack stores items in Last-In, First-Out (LIFO) order. The two core operations are push(S, x) (add x to the top) and pop(S) (remove and return the top). With an array-backed stack, push/pop are O(1) amortized (but push may be O(n) on a resize). With a linked-list-backed stack, push/pop are O(1) worst-case.

## What Is a Stack?

## Definition (and why you should care)

A **stack** is a collection with a strict access rule:

- •You can only add items to one end, called the **top**.
- •You can only remove items from that same end.

This creates **Last-In, First-Out (LIFO)** ordering: the most recently added item is the first one to be removed.

A good mental model is a stack of plates:

- •You place a plate on top.
- •You remove the top plate.
- •You *don’t* pull a plate from the middle.

## Core operations

Stacks are defined by a tiny API:

- •**Push**: add an element to the top
- •Notation: push(S, x)
- •**Pop**: remove and return the top element
- •Notation: pop(S)

Most stack interfaces also include:

- •**Peek/Top**: return the top element without removing it
- •Notation often: top(S) or peek(S)
- •**IsEmpty**: check whether the stack has no elements

## Explicit prerequisites (so complexity claims are accurate)

You already know arrays and linked lists, but for stacks we need a few extra details to be precise:

1. 1)**Big-O notation**

- •You should be comfortable with claims like O(1), O(n), and what they mean for growing input sizes.

2. 2)**Arrays with resizing (dynamic arrays) + amortized analysis basics**

- •A “push to the end of an array” is often said to be O(1), but that’s only **amortized**.
- •Occasionally, the array must resize (allocate a larger block and copy items), which is **O(n)** for that push.

3. 3)**Pointers / references for linked lists**

- •Linked-list stacks rely on changing a head pointer and storing next pointers.

### Worst-case vs amortized (brief but important)

- •**Worst-case time**: the maximum time a single operation can take.
- •**Amortized time**: the average time per operation over a long sequence.

For an array-backed stack, most pushes are cheap, but some pushes trigger a resize.

Example idea: If capacity doubles when full, then after many pushes, the total copying work spreads out, and the average cost per push becomes constant.

We’ll revisit this when we implement stacks with arrays.

## Core Mechanic 1: LIFO Ordering (the rule that makes stacks useful)

## Why LIFO is a *feature*, not a limitation

At first, “you can only access the top” sounds restrictive. But LIFO matches many real computation patterns:

- •**Nested structure**: parentheses, HTML tags, scopes, function calls
- •**Undo behavior**: most recent action undone first
- •**Backtracking**: explore a path, then retreat in reverse order

LIFO is exactly what you want when later work depends on earlier work finishing.

## LIFO as a formal property

Suppose we start with an empty stack S and do:

1. 1)push(S, a)
2. 2)push(S, b)
3. 3)push(S, c)

Now the top-to-bottom order is: c, b, a.

Then:

- •pop(S) returns c
- •pop(S) returns b
- •pop(S) returns a

So the pop sequence is the reverse of the push sequence.

### A small derivation: pop reverses push

If we represent the sequence of pushes as a list [x₁, x₂, …, xₙ] (in chronological order), then after all pushes:

- •top(S) = xₙ

After one pop:

- •returned value = xₙ
- •remaining stack corresponds to [x₁, …, xₙ₋₁]

After k pops:

- •returned values (in order) = xₙ, xₙ₋₁, …, xₙ₋k+1

This “reverse order” behavior is the heart of stacks.

## Stack state: top pointer / index intuition

Even without code, it helps to picture what the stack must remember:

- •The elements
- •Where the **top** is

That “where the top is” becomes:

- •an integer index (array-based)
- •a pointer to a node (linked-list-based)

This is why stacks can be so fast: operations only touch the top.

## Underflow: what if you pop from empty?

A stack needs a defined behavior for pop(S) when S is empty:

- •Throw an error/exception
- •Return a sentinel value (less common in strongly typed designs)
- •Provide a pre-check isEmpty(S)

Conceptually, **pop on empty** is an invalid operation and must be handled.

## Core Mechanic 2: Implementing push(S, x) and pop(S) Efficiently

## Two common implementations

Stacks are an **abstract data type (ADT)**: the behavior is defined (LIFO), not the storage.

The two classic implementations build on your prerequisites:

| Implementation | “Top” stored as | push | pop | Notes |
| --- | --- | --- | --- | --- |
| Array-backed (dynamic array) | integer index n (size) | O(1) amortized, O(n) worst-case on resize | O(1) | cache-friendly, simple |
| Linked-list-backed | pointer to head node | O(1) worst-case | O(1) worst-case | no resizing cost, extra pointer overhead |

We’ll walk through both, carefully stating complexity.

---

## Array-backed stack

### Representation

Use an array A and an integer n = number of elements.

- •Valid elements are in A[0..n−1]
- •The top element is A[n−1]

### push(S, x)

To push x:

1. 1)If n == capacity(A), resize to a bigger array (typically double capacity).
2. 2)Set A[n] = x
3. 3)Increment n

In pseudocode:

- •push(S, x):
- •if n == capacity: resize
- •A[n] ← x
- •n ← n + 1

### pop(S)

To pop:

1. 1)If n == 0, error (underflow)
2. 2)Decrement n
3. 3)Return A[n] (which was the previous top)

- •pop(S):
- •if n == 0: error
- •n ← n − 1
- •return A[n]

### Time complexity (being precise)

- •pop is **O(1) worst-case** (no resizing needed just to remove).
- •push is:
- •**O(1) amortized** if you use geometric resizing (like doubling)
- •**O(n) worst-case** for a push that triggers a resize and copies n elements

#### Why push is amortized O(1) (intuition)

When you double capacity, the expensive copies happen rarely.

Example: start with capacity 1.

- •Push 1 element: copy 0
- •Push 2nd: resize, copy 1
- •Push 3rd: resize, copy 2
- •Push 5th: resize, copy 4

Total copies after growing to size N is roughly:

1 + 2 + 4 + … + N/2 < N

So the total copying work is O(N) over N pushes, giving O(1) *amortized* per push.

---

## Linked-list-backed stack

### Representation

Store a pointer head that points to the top node.

Each node stores:

- •value
- •next pointer

Top element is head.value.

### push(S, x)

To push x:

1. 1)Create new node p holding x
2. 2)Set p.next = head
3. 3)Set head = p

Only a constant number of pointer updates.

### pop(S)

To pop:

1. 1)If head is null, error
2. 2)Store x = head.value
3. 3)Set head = head.next
4. 4)Return x

Again, constant pointer updates.

### Time complexity

- •push: **O(1) worst-case**
- •pop: **O(1) worst-case**

### Tradeoffs vs array-backed

Linked lists avoid resize spikes, but:

- •extra memory per node (the next pointer)
- •worse cache locality (nodes scattered in memory)

In many practical systems, array-backed stacks are faster in practice due to locality, even with occasional resizes.

---

## Space complexity

Both are O(n) for n elements.

- •Array-backed: might allocate extra unused capacity (e.g., capacity up to ~2n)
- •Linked-list-backed: exactly n nodes, but each node has pointer overhead

---

## Peek/top operation

peek(S):

- •If empty, error
- •Return top element without modifying the stack

Array-backed: return A[n−1]

Linked-list: return head.value

Both are O(1).

## Application/Connection: Why Stacks Enable Recursion (and more)

## The big connection: stacks and function calls

When a function calls another function, the program must remember where to return, plus local variables and parameters. That “remembering” is managed by a **call stack**.

Each call frame is pushed when a function begins and popped when it returns.

This is why recursion naturally maps to stacks:

- •Each recursive call pushes a new frame.
- •When a base case returns, frames pop in reverse order.

So LIFO order matches “last call finishes first.”

## Example: nested tasks

Consider evaluating a nested expression like: ((2 + 3) \* (4 + 5))

When you parse or evaluate nested structure, you often:

- •push markers when you enter a nested region
- •pop when you exit it

This is the same “open something, then close it later” logic.

## Classic uses of stacks

Even before recursion, stacks show up everywhere:

1. 1)**Balanced parentheses / bracket matching**

- •Push opening symbols
- •Pop when you see a closing symbol

2. 2)**Undo/redo**

- •Push user actions onto an undo stack
- •Pop to undo

3. 3)**Depth-first search (DFS)**

- •A stack stores the frontier of nodes to visit

4. 4)**Backtracking**

- •Push choices
- •Pop when a choice fails

## A note on “stack overflow”

Because call stacks are finite, deep recursion can exhaust available memory.

That’s not a problem with the stack *idea*, but with limited resources.

Practical mitigation:

- •convert recursion to an explicit stack (iterative)
- •ensure recursion depth stays safe

## Connecting the node you unlock

This node unlocks: [Recursion](/tech-tree/recursion/)

A key learning goal for recursion will be: every recursive solution has an equivalent iterative solution using an explicit stack, because recursion is (conceptually) stack-driven.

## Worked Examples (3)

### Example 1: Simulate push/pop and track the top

Start with an empty stack S. Perform operations in order:

1) push(S, 10)

2) push(S, 20)

3) pop(S)

4) push(S, 30)

5) pop(S)

6) pop(S)

Track what each pop returns and the final stack contents.

1. Initial: S = [ ] (empty)
2. 1) push(S, 10)

   S = [10]

   Top is 10
3. 2) push(S, 20)

   S = [10, 20]

   Top is 20
4. 3) pop(S)

   Pop returns 20 (last pushed)

   S becomes [10]
5. 4) push(S, 30)

   S = [10, 30]

   Top is 30
6. 5) pop(S)

   Pop returns 30

   S becomes [10]
7. 6) pop(S)

   Pop returns 10

   S becomes [ ]
8. Final: stack is empty; pop outputs were 20, 30, 10

**Insight:** Stacks reverse the order of the most recent pushes: the last item pushed is always the first item popped.

### Example 2: Parentheses matching with a stack

Determine whether the string is balanced: s = "( [ ( ) ] )" (spaces only for readability). Use a stack that stores opening brackets. Rules: push on '(', '[', '{'. On ')', ']', '}', the top must be the matching opener; pop it. At the end, stack must be empty.

1. Initialize stack S = [ ]
2. Read '(': opener → push

   S = ['(']
3. Read '[': opener → push

   S = ['(', '[']
4. Read '(': opener → push

   S = ['(', '[', '(']
5. Read ')': closer → top must be '('

   Top is '(' → pop

   S = ['(', '[']
6. Read ']': closer → top must be '['

   Top is '[' → pop

   S = ['(']
7. Read ')': closer → top must be '('

   Top is '(' → pop

   S = [ ]
8. End of input: S is empty → balanced

**Insight:** The stack naturally handles nested structure because the most recent unmatched opener is exactly the one that must be closed next (LIFO).

### Example 3: Amortized vs worst-case push in an array-backed stack

You have an array-backed stack that doubles capacity when full. Start with capacity = 1 and push 8 elements. Count how many total element copies happen due to resizing (ignore the O(1) write into the new slot; only count copies performed during resize).

1. Capacity 1: push #1 fits, copies = 0. Size=1, cap=1.
2. push #2 triggers resize 1→2: copy 1 element. copies += 1. Size=2, cap=2.
3. push #3 triggers resize 2→4: copy 2 elements. copies += 2. Size=3, cap=4.
4. push #4 fits, copies += 0. Size=4, cap=4.
5. push #5 triggers resize 4→8: copy 4 elements. copies += 4. Size=5, cap=8.
6. push #6 fits, copies += 0. Size=6, cap=8.
7. push #7 fits, copies += 0. Size=7, cap=8.
8. push #8 fits, copies += 0. Size=8, cap=8.
9. Total copies due to resizing = 1 + 2 + 4 = 7

**Insight:** Even though some pushes are expensive (O(n) copy on resize), the total copying over many pushes grows linearly with the number of pushes. That’s the core idea behind amortized O(1) push.

## Key Takeaways

- ✓

  A stack is an ADT with LIFO ordering: the last element pushed is the first popped.
- ✓

  The core operations are push(S, x) and pop(S); peek/top is a common O(1) addition.
- ✓

  Array-backed stacks use a top index n; pop is O(1) worst-case, push is O(1) amortized but can be O(n) on a resize.
- ✓

  Linked-list-backed stacks use a head pointer; push and pop are O(1) worst-case with no resizing spikes.
- ✓

  Worst-case and amortized time are different: amortized averages across a sequence of operations; worst-case is for a single operation.
- ✓

  Stacks are ideal for nested/last-opened-first-closed problems: parentheses matching, backtracking, and DFS.
- ✓

  Recursion is deeply connected to stacks via the call stack: each call pushes a frame; returns pop frames in reverse order.

## Common Mistakes

- ✗

  Claiming array-backed push is always O(1) without mentioning amortized analysis and the O(n) resize worst-case.
- ✗

  Forgetting to handle stack underflow: calling pop(S) or peek(S) on an empty stack.
- ✗

  Implementing an array-backed stack but pushing/popping from the front (index 0), accidentally turning operations into O(n) due to shifting.
- ✗

  Confusing a stack with a queue: stacks are LIFO, queues are FIFO.

## Practice

easy

You perform these operations on an empty stack S: push(S, 'a'), push(S, 'b'), push(S, 'c'), pop(S), push(S, 'd'), pop(S), pop(S). What sequence of values is returned by the pops?

**Hint:** Write the stack contents after each operation; remember LIFO.

Show solution

After pushes: [a, b, c]. First pop returns c → stack [a, b]. Push d → [a, b, d]. Next pop returns d → [a, b]. Next pop returns b → [a]. Pop outputs: c, d, b.

medium

Design an array-backed stack with variables A (array) and n (size). Write the exact steps (in words or pseudocode) for peek(S), including error handling. State the time complexity.

**Hint:** The top element is at index n−1 when n>0.

Show solution

Algorithm: if n == 0, error/throw underflow; else return A[n−1]. Time: O(1) worst-case.

hard

An array-backed stack doubles capacity when full, starting from capacity 2. You push 9 elements. How many total element copies occur due to resizing (count only copies done during resize)?

**Hint:** Resizes happen when pushing into a full array. Track capacities: 2→4→8→16 and sum copies at each resize.

Show solution

Start cap=2. Push #1-2 fit (0 copies). Push #3 triggers 2→4: copy 2. Push #4 fits. Push #5 triggers 4→8: copy 4. Push #6-8 fit. Push #9 triggers 8→16: copy 8. Total copies = 2 + 4 + 8 = 14.

## Connections

- •Next: [Recursion](/tech-tree/recursion/)
- •Compare: Queues (FIFO) are the “opposite ordering” cousin of stacks.
- •Related patterns: Depth-first search typically uses a stack; breadth-first search typically uses a queue.

Quality: A (4.6/5)

[← back to tree](/tech-tree/)[browse all →](/tech-tree/inventory/)
