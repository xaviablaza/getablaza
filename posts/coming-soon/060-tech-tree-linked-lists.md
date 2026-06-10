---
title: Linked Lists
description: Nodes connected by pointers. O(1) insert/delete, O(n) access.
date: '2026-07-01'
scheduled: '2026-08-29'
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
inspiration_url: https://templeton.host/tech-tree/linked-lists/
inspiration_category: tech-tree
---

> Source-copy draft imported from [https://templeton.host/tech-tree/linked-lists/](https://templeton.host/tech-tree/linked-lists/). Names, domain references, and local media paths were adapted for Xavi Ablaza / getablaza.com.

[←Back to Tech Tree](/tech-tree/)

[inventory](/tech-tree/inventory/)[coverage](/tech-tree/coverage/)

# Linked Lists

Data StructuresDifficulty: ★☆☆☆☆Depth: 0Unlocks: 22

Nodes connected by pointers. O(1) insert/delete, O(n) access.

## Interactive Visualization

⏮◀◀▶▶STEP0.25x1xZOOM

t=0s

## Core Concepts

- -Node: stores a value and a single pointer field ('next')
- -Head: a reference serving as the list's entry point
- -Null terminator: a special null value indicating no further node

## Key Symbols & Notation

next (pointer field in a node)head (reference to the first node)

## Essential Relationships

- -Following next pointers from head visits nodes in order; reassigning a node's next links or unlinks neighbors (basis for insertion/deletion)

## Unlocks (3)

[Graph Traversallvl 2](/tech-tree/graph-traversal/)[Stackslvl 2](/tech-tree/stacks/)[Queueslvl 2](/tech-tree/queues/)

Advanced Learning Details

### Graph Position

6

Depth Cost

22

Fan-Out (ROI)

12

Bottleneck Score

0

Chain Length

### Cognitive Load

6

Atomic Elements

40

Total Elements

L3

Percentile Level

L4

Atomic Level

### All Concepts (19)

- - Node: a container with a stored value and a pointer field that references another node
- - Pointer/reference: a variable whose value is the address or reference of a node rather than a simple data value
- - Head pointer: a variable that references the first node of the list
- - Tail pointer: a variable that references the last node of the list (optional but common)
- - Null terminator: a special pointer value meaning "no node" or end of list
- - Singly linked list: node structure with a single "next" pointer linking nodes in one direction
- - Doubly linked list: node structure with both "next" and "prev" pointers linking nodes in both directions (variant)
- - Insertion at head: creating or reassigning pointers so a new node becomes the first node
- - Insertion after a given node: linking a new node into the chain immediately after a specified node
- - Deletion of a node given a pointer to it: unlinking a node by updating neighbor pointers
- - Predecessor requirement for deletion in singly lists: to remove a node you normally need a reference to its previous node
- - Traversal/iteration: moving through the list by repeatedly following the next pointer from head
- - Access by index requires traversal: there is no direct index-to-node mapping, so reaching the i-th element requires i steps on average
- - Empty list and single-element list edge cases: special conditions when head is null or head==tail
- - Aliasing and shared references: multiple pointers can reference the same node so changes via one reference affect all aliases
- - Dynamic allocation and deallocation of nodes at runtime (list size changes as nodes are added/removed)
- - Sentinel or dummy node technique: using a non-data node at head to simplify boundary operations
- - Updates to head or tail on insert/delete: operations must maintain correct head/tail references
- - Locality and memory layout implication: nodes are typically heap-allocated and not stored contiguously, affecting cache behavior

### Teaching Strategy

Deep-dive lesson - accessible entry point but dense material. Use worked examples and spaced repetition.

Arrays feel like books with numbered pages: jump straight to page 57. Linked lists feel like a treasure hunt: each clue points to the next clue. That “next clue” idea is simple, but it unlocks many core CS structures like stacks, queues, and graph traversal.

TL;DR:

A linked list is a chain of nodes. Each node stores (1) a value and (2) a pointer/reference called next to the next node. The list starts at head and ends when next is null. You can insert/delete near a known node in O(1), but accessing the k-th element requires walking from head, which is O(n).

## What Is a Linked List?

## The idea

A **linked list** is a linear data structure made of **nodes**, where each node knows how to reach the next node.

A *singly linked list* node contains:

- •**value**: the data you care about (number, string, object, etc.)
- •**next**: a pointer/reference to another node (the “next” node in the chain)

A list also has a special reference:

- •**head**: a pointer/reference to the first node (the entry point)

And it uses a special terminator:

- •**null**: a special “points to nothing” value meaning “there is no next node.”

So the shape is:

head → [value | next] → [value | next] → [value | null]

## Why this exists (motivation)

Arrays are great when you need fast random access: element i is reachable in O(1). But arrays typically assume elements are stored in a contiguous block of memory, which makes some operations expensive:

- •inserting at the front requires shifting everything right
- •deleting in the middle requires shifting elements left

Linked lists trade away random access to gain a different power: **local rewiring**.

If you have a pointer to a node, you can often insert or delete next to it by changing a small number of pointers—no shifting required.

## Mini-primer: the few prerequisites we’ll use (so this can stay beginner-friendly)

Even if you’ve never used C/C++ pointers, you can understand linked lists with these minimal ideas:

1) **Reference / pointer**: a variable that “points to” an object/node.

- •Think: “this variable holds the location of the node.”

2) **null**: a special value meaning “no object here.”

- •If node.next is null, the list ends there.

3) **Big-O**: a rough way to describe how runtime grows with input size n.

- •O(1): constant time (doesn’t grow with n)
- •O(n): linear time (grows proportionally with n)

4) **Basic pseudocode**: we’ll write steps like:

- •set A.next = B
- •head = head.next

That’s it.

## The linked list invariants (rules that must stay true)

To reason safely, keep these mental rules:

- •**head** points to the first node (or is null if the list is empty)
- •each node’s **next** either points to another node or is **null**
- •following next repeatedly from head will eventually reach null (no cycles) in a standard list

## A small example

Suppose we store 3 → 7 → 9.

- •head points to the node containing 3
- •node(3).next points to node(7)
- •node(7).next points to node(9)
- •node(9).next is null

If you want the value 9, you must walk:

- •start at head (3)
- •go to next (7)
- •go to next (9)

That “walk” is the central linked-list operation.

## Time complexity (the headline)

Let n be the number of nodes.

- •Access/search by position (k-th element): **O(n)** because you may traverse many nodes.
- •Insert/delete at the **front** (with head): **O(1)**
- •Insert/delete after a **known node**: **O(1)**
- •Insert/delete at the end: often **O(n)** unless you also store a tail pointer.

We’ll make these precise in the next sections.

## Core Mechanic 1: Traversal (Walking the Chain)

## Why traversal matters

With arrays, “go to index i” is direct. With linked lists, the *default* operation is: **start at head and follow next pointers**.

Traversal is how you:

- •print the list
- •count nodes
- •find a value
- •reach the k-th node
- •reach the node *before* the one you want to delete

Because traversal is common, it’s also the main source of O(n) cost.

## Basic traversal pattern

We use a moving pointer/reference, often called curr.

Pseudocode:

- •curr = head
- •while curr != null:
- •visit curr.value
- •curr = curr.next

This loop ends because eventually curr becomes null (the null terminator).

## Example: count the number of nodes

We keep a counter.

- •count = 0
- •curr = head
- •while curr != null:
- •count = count + 1
- •curr = curr.next
- •return count

If there are n nodes, the loop runs n times ⇒ O(n).

## Example: find whether a value exists

We scan until we find it or hit null.

- •curr = head
- •while curr != null:
- •if curr.value == target: return true
- •curr = curr.next
- •return false

Worst case: target is not present (or at the end), so you examine all n nodes ⇒ O(n).

## Getting the k-th element (0-indexed)

To get element k, you move k steps.

- •curr = head
- •i = 0
- •while curr != null and i < k:
- •curr = curr.next
- •i = i + 1
- •if curr == null: error (index out of bounds)
- •return curr.value

Runtime: in the worst case k ≈ n ⇒ O(n).

## A subtle but important idea: tracking previous

Many operations (especially deletion) require knowing not just curr, but also the node **before** it.

Pattern:

- •prev = null
- •curr = head
- •while curr != null:
- •if curr.value == target: break
- •prev = curr
- •curr = curr.next

After the loop:

- •curr is the target node (or null if not found)
- •prev is the node before curr (or null if curr is head)

This “prev/curr” pair shows up everywhere.

## Common traversal pitfalls

- •Forgetting to advance: if you never do curr = curr.next, you create an infinite loop.
- •Dereferencing null: if curr is null, curr.next is invalid.
- •Off-by-one: mixing up “stop when i == k” vs “move k times.”

Traversal is the price you pay for the benefits you’ll see next: simple pointer rewiring.

## Core Mechanic 2: Insertion and Deletion (Pointer Rewiring)

## Why insertion/deletion are the linked list’s superpower

In an array, inserting at the front requires shifting all n elements (O(n)).

In a linked list, inserting at the front is usually just:

1) create a new node

2) point it at the old head

3) move head to the new node

That’s a constant number of operations ⇒ O(1).

The key insight: **you don’t move the nodes; you change the links**.

## Inserting at the front (push front)

Assume we have:

- •head → A → B → null

We want to insert X at the front.

Steps:

1) X.next = head

2) head = X

Result:

- •head → X → A → B → null

This is O(1).

## Inserting after a given node

Suppose you already have a reference to node A, and you want to insert X right after it.

Before:

- •A → B

Steps:

1) X.next = A.next (so X points to B)

2) A.next = X (so A points to X)

After:

- •A → X → B

Also O(1) (because it’s a constant number of pointer changes).

### Why the order matters

If you do A.next = X first, you lose the original link to B unless you saved it.

Correct safe order:

- •X.next = A.next
- •A.next = X

## Deleting after a given node

If you have node A, and you want to delete the node right after it (call that node B), you can bypass B.

Before:

- •A → B → C

Steps:

1) A.next = B.next (A points directly to C)

2) (optionally) free/delete B in languages that require it

After:

- •A → C

Again O(1).

## Deleting the head node

Deleting the first node is special because it changes head.

Before:

- •head → A → B → ...

Steps:

1) head = head.next

2) (optionally) free/delete old A

After:

- •head → B → ...

O(1).

## Deleting a node by value (needs traversal)

Now combine traversal with rewiring.

Goal: delete the first node whose value == target.

We need prev/curr:

- •prev tracks the node before curr

Cases:

1) target is at head: update head

2) target is in middle/end: set prev.next = curr.next

3) target not found: do nothing

This is O(n) because you may scan the list.

Pseudocode:

- •prev = null
- •curr = head
- •while curr != null and curr.value != target:
- •prev = curr
- •curr = curr.next
- •if curr == null: return (not found)
- •if prev == null:
- •head = curr.next (deleted head)
- •else:
- •prev.next = curr.next (bypass curr)
- •(optionally) free/delete curr

## Summary table: operations and costs

| Operation | What you need | Time | Why |
| --- | --- | --- | --- |
| Traverse/print | head | O(n) | must follow next links |
| Search by value | head | O(n) | may inspect all nodes |
| Access k-th | head, k | O(n) | move step-by-step |
| Insert at head | head | O(1) | constant rewiring |
| Delete at head | head | O(1) | constant rewiring |
| Insert after node A | pointer to A | O(1) | constant rewiring |
| Delete after node A | pointer to A | O(1) | constant rewiring |

## Memory and layout intuition

Nodes typically live separately in memory. Each node stores extra “overhead” (the next pointer). That overhead is part of the trade-off:

- •Pros: easy local insert/delete
- •Cons: extra memory, and traversals can be slower in practice due to poor cache locality (advanced detail; not required, but good to know)

At this level, the essential skill is: **draw the pointers and perform pointer rewiring carefully**.

## Applications and Connections: Why Linked Lists Show Up Everywhere

## Linked lists as the foundation for other structures

Linked lists are a “building block” data structure. Once you can:

- •traverse
- •insert at head
- •delete at head

…you can implement several important abstractions.

## Connection 1: Stacks (LIFO)

A stack supports:

- •push(x)
- •pop()

Using a linked list:

- •push(x): insert at head (O(1))
- •pop(): delete head (O(1))

Why it fits: the top of the stack can be the head of the list.

## Connection 2: Queues (FIFO)

A queue supports:

- •enqueue(x) at the back
- •dequeue() from the front

Linked list approach:

- •keep head for front
- •optionally keep tail for back

If you maintain both head and tail pointers:

- •enqueue at tail: O(1)
- •dequeue at head: O(1)

Without a tail pointer, enqueue requires walking to the end ⇒ O(n). This is a nice example of how **one extra reference** can change performance.

## Connection 3: Graph traversal intuition

Graphs are “nodes connected by references” too. Linked lists are the simplest version: each node has only one outgoing edge (next). When you later learn BFS/DFS, you’ll still be following pointers/references—just with branching.

## When to use a linked list (and when not to)

Use a linked list when:

- •you do many insertions/deletions near the front or near known nodes
- •you don’t need frequent random access by index

Prefer an array/dynamic array when:

- •you need fast indexing (get/set by i)
- •you frequently iterate and want good cache performance
- •you rarely insert/delete in the middle

## A final mental model

Linked list skills are mostly about *maintaining correct structure*:

- •keep head correct
- •make sure the last node’s next is null
- •update pointers in the right order

If you can do that, you’re ready to build stacks, queues, and start thinking in terms of pointer-based structures like trees and graphs.

## Worked Examples (3)

### Insert a node into the middle (pointer rewiring with order)

You have a list: head → 10 → 20 → 40 → null. You have a reference to the node holding 20. Insert a new node holding 30 right after 20, producing: head → 10 → 20 → 30 → 40 → null.

1. Name the known node A = node(20). Let B = A.next (currently node(40)).

   We want: A → X → B, where X is node(30).
2. Create the new node X with X.value = 30.
3. Set X.next = A.next.

   This makes X.next point to B (node(40)).

   Now the chain conceptually is: A → B and X → B.
4. Set A.next = X.

   Now A points to X, and X points to B.

   The list becomes: head → 10 → 20 → 30 → 40 → null.
5. Verify you did not lose node(40): it is still reachable from head by following next pointers.

**Insight:** The safe insertion pattern is always: (1) new.next = old\_next, then (2) old.next = new. If you reverse the order without saving old\_next, you can disconnect the rest of the list.

### Delete the first node with a given value (prev/curr traversal)

Delete the first node whose value is 7 from: head → 3 → 7 → 7 → 9 → null. Only the first 7 should be removed.

1. Initialize two pointers:

   prev = null

   curr = head (node with value 3)
2. Check curr.value:

   - •curr.value = 3 ≠ 7, so advance.

   Update:

   prev = curr (now prev is 3)

   curr = curr.next (now curr is the first 7)
3. Check curr.value again:

   - •curr.value = 7, so we stop traversal. We found the node to delete (curr).
4. Since prev != null, this is not deleting the head.

   Rewire:

   prev.next = curr.next

   That is: node(3).next now points to the second 7.
5. Optionally free/delete curr depending on the language.

   Now the list is: head → 3 → 7 → 9 → null (where this 7 is the original second 7).
6. Verify by traversal from head: 3, then 7, then 9, then null.

**Insight:** Deletion is usually “bypass the node.” To bypass safely, you often need the node before it (prev). The head case is special because there is no previous node.

### Access the k-th element and explain the O(n) cost

Given: head → 5 → 8 → 2 → 1 → null. Find the element at index k = 3 (0-indexed).

1. Start:

   curr = head (value 5)

   i = 0
2. We need to move forward while i < 3.

   Step 1: i = 0 < 3 ⇒ curr = curr.next (value 8), i = 1
3. Step 2: i = 1 < 3 ⇒ curr = curr.next (value 2), i = 2
4. Step 3: i = 2 < 3 ⇒ curr = curr.next (value 1), i = 3
5. Now i == 3, stop. curr points to the node at index 3.

   Return curr.value = 1.
6. Cost explanation: in the worst case, k is near n-1, so you take about n steps. That’s why indexed access in a linked list is O(n).

**Insight:** Linked lists don’t store an “index → address” map. The only way to reach deeper nodes is to follow next repeatedly from head.

## Key Takeaways

- ✓

  A singly linked list is a chain of nodes; each node stores a value and a next pointer/reference.
- ✓

  head is the entry point; an empty list has head = null.
- ✓

  The list ends when a node’s next is null (the null terminator).
- ✓

  Traversal (following next) is fundamental and costs O(n) in the number of nodes visited.
- ✓

  Insert/delete at the head is O(1) because it changes only a constant number of pointers.
- ✓

  Insert/delete after a known node is O(1); deleting/searching by value is usually O(n) because you must find the spot first.
- ✓

  Pointer update order matters: set new.next before redirecting old.next to avoid losing the remainder of the list.
- ✓

  Linked lists naturally implement stacks (head as top) and queues (head/tail as ends).

## Common Mistakes

- ✗

  Forgetting the head special case when deleting: if the target is at head, you must update head (there is no prev).
- ✗

  Updating pointers in the wrong order during insertion, accidentally disconnecting the rest of the list.
- ✗

  Null dereference: accessing curr.next when curr is null (always check termination conditions).
- ✗

  Assuming linked lists have O(1) indexing like arrays; reaching the k-th element requires O(k) traversal.

## Practice

easy

Write pseudocode to insert a new value x at the front of a singly linked list. Use head and next. What is the time complexity?

**Hint:** Create a node X. Point X.next to the current head, then move head to X.

Show solution

Pseudocode:

- •X = new Node(x)
- •X.next = head
- •head = X

Time complexity: O(1) because it does a constant amount of work.

medium

Given head → 1 → 2 → 3 → 4 → null, delete the node with value 3 (assume it exists). Show the key pointer update(s).

**Hint:** You must traverse until curr is 3, keeping prev as the node before curr.

Show solution

Traversal:

- •prev = null, curr = head (1)
- •advance until curr.value == 3, updating prev each time

At the moment curr is node(3), prev is node(2).

Delete by bypassing:

- •prev.next = curr.next

So node(2).next now points to node(4).

Result: head → 1 → 2 → 4 → null.

Runtime: O(n) due to traversal.

hard

You maintain both head and tail pointers for a singly linked list. Describe how to enqueue (append) a value x in O(1) time, including how tail changes in the empty-list case.

**Hint:** If the list is empty, head and tail should both point to the new node. Otherwise, link tail.next to the new node and move tail.

Show solution

Let X = new Node(x), with X.next = null.

Case 1: empty list (head == null):

- •head = X
- •tail = X

Case 2: non-empty:

- •tail.next = X
- •tail = X

This is O(1) because it updates a constant number of pointers.

## Connections

[Graph Traversal](/tech-tree/graph-traversal/)

[Stacks](/tech-tree/stacks/)

[Queues](/tech-tree/queues/)

Quality: A (4.4/5)

[← back to tree](/tech-tree/)[browse all →](/tech-tree/inventory/)
