---
title: Recursion
description: Functions that call themselves. Base case and recursive case.
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
inspiration_url: https://templeton.host/tech-tree/recursion/
inspiration_category: tech-tree
---

> Source-copy draft imported from [https://templeton.host/tech-tree/recursion/](https://templeton.host/tech-tree/recursion/). Names, domain references, and local media paths were adapted for Xavi Ablaza / getablaza.com.

[←Back to Tech Tree](/tech-tree/)

[inventory](/tech-tree/inventory/)[coverage](/tech-tree/coverage/)

# Recursion

AlgorithmsDifficulty: ★★☆☆☆Depth: 2Unlocks: 11

Functions that call themselves. Base case and recursive case.

## Interactive Visualization

⏮◀◀▶▶STEP0.25x1xZOOM

t=0s

## Core Concepts

- -Self-reference: a function directly invokes itself
- -Base case: a condition that returns without further recursion
- -Progress (measure): each recursive call reduces a well-founded measure or simplifies the problem

## Essential Relationships

- -Recursive case calls the same function with arguments transformed to make progress toward the base case
- -Base case halts further self-calls so that recursive calls can return (unwind)

## Prerequisites (2)

[Functions6 atoms](/tech-tree/functions-basic/)[Stacks5 atoms](/tech-tree/stacks/)

## Unlocks (3)

[Recurrence Relationslvl 3](/tech-tree/recurrence-relations/)[Dynamic Programminglvl 3](/tech-tree/dynamic-programming/)[Divide and Conquerlvl 3](/tech-tree/divide-conquer/)

## Referenced by (1)

Where this concept shows up in the operating-finance and personal-finance graphs.

### From Business (1)

[base caseBusiness

Recursion is defined by its base case plus recursive step - identical structure to starting from simplest assumptions and incrementally relaxing them](/business/base-case/)

Advanced Learning Details

### Graph Position

27

Depth Cost

11

Fan-Out (ROI)

6

Bottleneck Score

2

Chain Length

### Cognitive Load

5

Atomic Elements

28

Total Elements

L1

Percentile Level

L3

Atomic Level

### All Concepts (12)

- - Recursion: a function defined in terms of calls to itself (self-referential definition)
- - Base case: a non-recursive branch that stops further self-calls and provides a direct answer
- - Recursive case: the branch where the function calls itself on a simpler/smaller instance
- - Recursive call: invocation of the same function from within its own body
- - Activation record / call frame: the per-call local state (parameters, local variables, return address) created for each recursive call
- - Recursion depth: the number of active (not-yet-returned) recursive calls at a point in execution
- - Termination / progress measure: the requirement and mechanism by which each recursive call moves toward a base case (a metric that decreases or simplifies)
- - Unwinding / return-value propagation: how values computed in deeper calls are returned and combined as the call stack pops
- - Call tree (or recursion tree): conceptual tree showing how the original problem decomposes into subcalls
- - Mutual recursion: recursion distributed across two or more functions that call each other
- - Recurrence relation: mathematical expression that defines the value or cost of a function in terms of its values on smaller inputs
- - Stack usage and overflow risk: the fact that each recursive call consumes stack resources and too many calls can exhaust the stack

### Teaching Strategy

Self-serve tutorial - low prerequisites, straightforward concepts.

Recursion is the programming version of a “self-similar” story: to solve a big problem, you describe how to solve a smaller version of the same problem—until you hit a stopping point.

TL;DR:

A recursive function solves a problem by calling itself on smaller inputs. It must have (1) a base case that stops, and (2) a progress measure that strictly decreases each call so it can’t recurse forever. The call stack remembers “where you were” so results can return back up.

## What Is Recursion?

### Why recursion exists (motivation before mechanics)

Some problems are naturally *self-similar*: the overall structure repeats inside smaller parts.

- •A folder contains subfolders, which contain subfolders.
- •A tree has subtrees, each of which is a tree.
- •A sorted array can be searched by looking at half, then half of half, etc.
- •Many mathematical definitions are recursive: factorial, Fibonacci, linked lists.

Recursion is a technique for expressing that self-similarity directly in code: **a function calls itself** to solve a smaller version of the same problem.

### Definition

A function is **recursive** if it (directly or indirectly) invokes itself.

A well-formed recursive function has two essential parts:

1) **Base case**: a condition where the function returns an answer *without* making another recursive call.

2) **Recursive case**: a rule that reduces the problem to one or more *smaller* instances of itself.

### The “progress measure” idea (the secret to termination)

To prevent infinite recursion, each recursive call must make progress toward the base case.

Think of a quantity that always decreases and can’t decrease forever. Common measures:

- •`n` decreases: `n → n − 1` until `n = 0`
- •interval size decreases: `hi − lo` shrinks each call
- •list length decreases: `len(xs)` goes down
- •tree height decreases: move to a child node

Mathematically, you want a **well-founded** measure: there is no infinite strictly-decreasing sequence. The natural numbers ℕ with “>” are well-founded, because you can’t keep subtracting 1 forever without hitting 0.

### A tiny example: factorial

Factorial is often defined recursively:

- •0! = 1 (base case)
- •n! = n · (n − 1)! for n ≥ 1 (recursive case)

In code-like pseudocode:

```
fact(n):
  if n == 0: return 1
  else: return n * fact(n-1)
```

Here:

- •Base case: `n == 0`
- •Progress measure: `n` decreases by 1 each call

### Recursion and the call stack (link to what you already know)

You already know stacks (LIFO). Recursion uses the **call stack** automatically.

When `fact(4)` calls `fact(3)`, the program needs to remember:

- •what `n` was (4)
- •that it should multiply the returned result by 4

That “remembering” is stored in a stack frame on the call stack. Then `fact(3)` calls `fact(2)`, pushing another frame, and so on.

When the base case returns, results flow back upward, popping frames as each call completes.

### Recursion vs. iteration (not rivals, just different expressions)

Many recursive functions can be rewritten as loops. Recursion is often clearer when:

- •the structure is hierarchical (trees, nested objects)
- •divide-and-conquer naturally splits the input
- •you want a direct translation of a recursive definition

But recursion can use more stack space and can overflow if too deep. You’ll learn to choose based on clarity and constraints.

## Core Mechanic 1: Base Case + Recursive Case (and how the stack makes it work)

### Why this mechanic matters

People new to recursion often focus on “the function calls itself” and forget that recursion is really about *two* responsibilities:

- •**Stopping** (base case)
- •**Reducing** (recursive case)

If either part is wrong, you get infinite recursion, wrong answers, or runtime errors.

### A mental model that actually works

When reasoning about recursion, use this disciplined viewpoint:

1) Assume the recursive call works on smaller inputs.

2) Use it to build the solution for the current input.

3) Verify that you eventually reach the base case.

This is basically informal induction.

### Example: sum of first n natural numbers

Define S(n) = 1 + 2 + … + n.

Recursive definition:

- •S(0) = 0
- •S(n) = n + S(n − 1)

Pseudocode:

```
sumTo(n):
  if n == 0: return 0
  else: return n + sumTo(n-1)
```

#### Stack trace intuition (small input)

Call `sumTo(3)`:

- •`sumTo(3)` needs `3 + sumTo(2)`
- •`sumTo(2)` needs `2 + sumTo(1)`
- •`sumTo(1)` needs `1 + sumTo(0)`
- •`sumTo(0)` returns `0`

Now unwind:

- •`sumTo(1)` returns `1 + 0 = 1`
- •`sumTo(2)` returns `2 + 1 = 3`
- •`sumTo(3)` returns `3 + 3 = 6`

Notice the call stack is LIFO:

- •Calls push frames: 3,2,1,0
- •Returns pop frames: 0,1,2,3

### Two common base-case styles

Base cases depend on the problem. Two patterns show up often:

1) **Minimal input** base case

- •`n == 0`
- •empty list `[]`
- •null node / leaf

2) **Small threshold** base case

- •for merge sort: when `len(arr) ≤ 1`
- •for binary search: when `lo > hi`

The key is that the base case is **guaranteed to occur** if the recursive case keeps making progress.

### A table of common recursive shapes

| Shape | Calls per frame | Typical data | Example | Key measure |
| --- | --- | --- | --- | --- |
| Linear recursion | 1 | integers, lists | factorial, list length | n, len |
| Divide-and-conquer | 2+ | arrays, problems split | merge sort | problem size |
| Tree recursion | varies | trees/graphs | DFS on tree | height/remaining nodes |

At difficulty 2, linear recursion is the easiest place to get fluent, but you should recognize the others so recursion doesn’t feel mysterious later.

### Spotting “hidden” recursion: indirect self-calls

A calls B calls A:

```
A(x):
  ... return B(x-1)
B(x):
  ... return A(x-1)
```

This is still recursion (mutual recursion). It still needs:

- •base case somewhere
- •progress measure across the cycle

### Practical caution: recursion depth

Each recursive call adds a stack frame. If the recursion is too deep, you can hit a stack overflow.

For linear recursion on large `n`, a loop is often safer. Later, you’ll learn techniques like tail recursion (and language-specific optimizations), but the first step is simply being aware that recursion consumes stack space proportional to depth.

## Core Mechanic 2: Progress Measures (How to Guarantee Termination and Correctness)

### Why “progress” deserves its own section

Many recursion bugs have a base case, but still never reach it because the recursive step doesn’t move closer.

Example of a broken recursive case:

```
countDown(n):
  if n == 0: return
  else: countDown(n)   # progress measure does not decrease
```

It has a base case (`n == 0`) but never reaches it.

So we need a way to *prove* we’re moving toward termination.

### Progress measures: the idea

A **progress measure** is a value m(input) ∈ ℕ (often) such that:

- •m(input) ≥ 0 for all valid inputs
- •each recursive call strictly decreases the measure

Formally, if `f` calls `f` on inputs x → x′, we want:

m(x′) < m(x)

Since ℕ has no infinite strictly decreasing sequences, recursion must eventually stop.

### Examples of measures

1) **Integer countdown**

- •Input: `n`
- •Measure: m(n) = n
- •Decrease rule: call on `n − 1`

2) **List processing**

- •Input: list `xs`
- •Measure: m(xs) = len(xs)
- •Decrease rule: call on `tail(xs)` (length decreases by 1)

3) **Range shrinking**

- •Input: `(lo, hi)`
- •Measure: m(lo, hi) = max(0, hi − lo + 1)
- •Decrease rule: choose a smaller subrange

### Connecting progress to correctness (informal induction)

Recursion correctness typically follows the same structure:

1) **Base case correctness**: show the function returns the right answer on the base case.

2) **Inductive step**: assume the function works for all smaller measures; prove it works for the current input.

You don’t need formal proofs for every function, but this mindset prevents “wishful recursion.”

### Worked-through reasoning example: list sum

Suppose we define a function `sum(xs)`.

Recursive idea:

- •Base case: empty list sums to 0
- •Recursive case: sum of list is head + sum(tail)

Let xs = [x₀, x₁, …, xₖ].

- •Base: sum([]) = 0
- •Step: sum([x₀] + rest) = x₀ + sum(rest)

Progress measure: m(xs) = len(xs). Each call uses `rest` where len(rest) = len(xs) − 1.

Correctness intuition:

- •If we already know sum(rest) is correct (smaller list), then adding x₀ produces the correct total.

### Another subtle progress issue: off-by-one in the wrong direction

Broken variant:

```
fact(n):
  if n == 0: return 1
  else: return n * fact(n+1)
```

This moves away from the base case: n grows, and you never hit 0.

The progress measure test catches this immediately:

- •m(n) = n does not decrease; it increases.

### When measures aren’t simple numbers

Sometimes the input is a structure (like a tree). You can still measure progress:

- •height of the remaining subtree
- •number of nodes remaining to visit

Even if you never compute the measure explicitly, you should be able to point to it in your reasoning.

### Summary checklist (use this when writing recursion)

Before you run your code, answer:

1) What is the base case?

2) What input(s) does the recursive call use?

3) What is the progress measure?

4) Does the measure strictly decrease on every path?

5) Does the recursive case combine results correctly?

If you can answer these, the recursion is usually correct and terminating.

## Application/Connection: Where Recursion Shows Up (and Why You’ll Want It Later)

### Why recursion becomes a “core tool” in algorithms

Recursion is not just a coding trick; it’s a way to express algorithmic structure.

Many major algorithm families are easiest to understand recursively first, and then (sometimes) optimized into iterative forms.

### 1) Divide and Conquer

Divide-and-conquer means:

1) Split the problem into smaller subproblems

2) Solve each subproblem (often recursively)

3) Combine the results

Example: merge sort

- •Split array into two halves
- •Recursively sort each half
- •Merge the two sorted halves

Progress measure: n = array length; each call handles roughly n/2.

This is the gateway to analyzing runtime with **recurrence relations** like:

T(n) = 2T(n/2) + O(n)

You’re not solving recurrences yet in this node, but recursion is what *creates* them.

### 2) Dynamic Programming (memoization starts as recursion)

Many problems have:

- •**optimal substructure**: the best solution uses best solutions to subproblems
- •**overlapping subproblems**: the same subproblem appears many times

A common path:

1) write a clean recursive solution

2) notice repeated calls

3) add memoization (cache) → dynamic programming

Classic example: Fibonacci.

Naive recursion:

- •F(0)=0, F(1)=1
- •F(n)=F(n−1)+F(n−2)

This is correct but repeats work. Memoization keeps the recursive clarity while improving performance.

### 3) Tree/graph traversals

Depth-first search (DFS) on a tree is naturally recursive:

- •Visit a node
- •Recursively visit each child

Progress measure: remaining nodes / subtree height.

(For general graphs, you must also track visited nodes to avoid cycles—otherwise recursion may not terminate even if depth decreases in some branches.)

### 4) Parsing and nested data

Anything nested—parentheses, JSON-like structures, expression trees—often becomes simpler with recursion.

### Recursion and stacks: the conceptual bridge

Since you already know stacks, here’s the key connection:

- •Recursion is “using the call stack as an implicit stack.”
- •Rewriting recursion iteratively often means “use your own explicit stack.”

This is a powerful translation:

| You have… | Recursive solution uses… | Iterative rewrite uses… |
| --- | --- | --- |
| Nested structure | call stack frames | explicit stack data structure |
| Need to return after subcall | return address stored in frame | store state in stack entries |

Understanding this makes recursion feel less like magic and more like a design choice.

### When not to use recursion

Recursion is great when it matches the problem structure. But you should consider alternatives when:

- •depth can be huge (risk of stack overflow)
- •an iterative solution is much clearer
- •performance requires tight control

Even then, learning recursion first is often the best route to a correct solution.

## Worked Examples (3)

### Worked Example 1: Factorial with a Full Call Stack Unwind

Compute 4! using a recursive definition and show every intermediate step.

Definition:

- •0! = 1
- •n! = n · (n − 1)! for n ≥ 1

1. Start with the goal:

   4! = 4 · 3!
2. Expand 3! using the same rule:

   3! = 3 · 2!

   So:

   4! = 4 · (3 · 2!)
3. Expand 2!:

   2! = 2 · 1!

   So:

   4! = 4 · (3 · (2 · 1!))
4. Expand 1!:

   1! = 1 · 0!

   So:

   4! = 4 · (3 · (2 · (1 · 0!)))
5. Use the base case:

   0! = 1

   So:

   4! = 4 · (3 · (2 · (1 · 1)))
6. Now multiply while unwinding (returning):

   1 · 1 = 1

   2 · 1 = 2

   3 · 2 = 6

   4 · 6 = 24
7. Final answer:

   4! = 24

**Insight:** The recursion “goes down” building a chain of deferred multiplications, and the base case starts the “unwind” where results flow back up. The call stack stores those deferred operations.

### Worked Example 2: Sum of a List via Recursion (Base Case = Empty List)

Let xs = [5, 2, 7]. Define recursively:

- •sum([]) = 0
- •sum([x] + rest) = x + sum(rest)

Compute sum([5, 2, 7]) with explicit substitutions.

1. Start:

   sum([5, 2, 7]) = 5 + sum([2, 7])
2. Apply the rule again:

   sum([2, 7]) = 2 + sum([7])

   So:

   sum([5, 2, 7]) = 5 + (2 + sum([7]))
3. Apply the rule to the last non-empty list:

   sum([7]) = 7 + sum([])

   So:

   sum([5, 2, 7]) = 5 + (2 + (7 + sum([])))
4. Use the base case:

   sum([]) = 0

   So:

   sum([5, 2, 7]) = 5 + (2 + (7 + 0))
5. Compute:

   7 + 0 = 7

   2 + 7 = 9

   5 + 9 = 14
6. Final answer:

   sum([5, 2, 7]) = 14

**Insight:** The progress measure is len(xs). Each call removes one element, guaranteeing termination, and the combination step (x + …) reconstructs the full sum.

### Worked Example 3: Binary Search Termination via a Range Measure

Binary search checks the middle of a sorted range and recurses into a smaller half.

Suppose arr is sorted and we search for target in indices lo..hi.

Progress measure: m(lo, hi) = max(0, hi − lo + 1).

1. Base case idea:

   If lo > hi, the range is empty, so return “not found.”

   This matches m(lo, hi) = 0.
2. Recursive case idea:

   Let mid = ⌊(lo + hi)/2⌋.

   Compare arr[mid] with target.
3. If target < arr[mid], recurse on left half:

   (lo, hi) → (lo, mid − 1)

   New measure:

   m' = (mid − 1) − lo + 1 = mid − lo

   Old measure:

   m = hi − lo + 1

   Since mid ≤ hi, we get:

   mid − lo < hi − lo + 1

   So m' < m.
4. If target > arr[mid], recurse on right half:

   (lo, hi) → (mid + 1, hi)

   New measure:

   m' = hi − (mid + 1) + 1 = hi − mid

   Since mid ≥ lo, we have:

   hi − mid < hi − lo + 1

   So m' < m.
5. Therefore, on every recursive path, the measure strictly decreases until the base case lo > hi occurs.

**Insight:** You don’t have to ‘feel’ that recursion terminates—you can *measure* it. Range size is a clean, reliable progress measure for divide-and-conquer search.

## Key Takeaways

- ✓

  Recursion = solving a problem by calling the same function on smaller instances of the problem.
- ✓

  Every recursive function needs a base case (stop) and a recursive case (reduce).
- ✓

  A progress measure m(input) ensures termination by strictly decreasing on each recursive call (often into ℕ).
- ✓

  The call stack acts like an implicit stack that stores “what to do after the recursive call returns.”
- ✓

  Reasoning about recursion works well with an induction-like mindset: assume smaller cases work, then build the current case.
- ✓

  Many major algorithm families (divide-and-conquer, dynamic programming, tree traversals) are naturally expressed recursively.
- ✓

  Recursion can be rewritten iteratively by managing your own explicit stack, which can help avoid deep call stacks.

## Common Mistakes

- ✗

  Missing or incorrect base case (e.g., forgetting n == 0, or using the wrong stopping condition).
- ✗

  No progress toward the base case (e.g., calling f(n) → f(n) or moving in the wrong direction f(n) → f(n+1)).
- ✗

  Off-by-one errors in the reduced input (e.g., binary search recursing on (lo, mid) instead of (lo, mid − 1), causing non-decreasing ranges).
- ✗

  Assuming recursion is always slower or always better: the right choice depends on depth, clarity, and constraints.

## Practice

easy

Write a recursive definition for power(n) = 2ⁿ for n ∈ ℕ, including a base case. Then compute 2⁵ by expanding your recursion.

**Hint:** Use 2⁰ = 1 as the base case, and reduce n by 1 each step.

Show solution

Recursive definition:

- •pow2(0) = 1
- •pow2(n) = 2 · pow2(n − 1) for n ≥ 1

Expansion:

pow2(5)

= 2 · pow2(4)

= 2 · (2 · pow2(3))

= 2 · (2 · (2 · pow2(2)))

= 2 · (2 · (2 · (2 · pow2(1))))

= 2 · (2 · (2 · (2 · (2 · pow2(0)))))

= 2 · (2 · (2 · (2 · (2 · 1))))

= 32

medium

Consider this function:

sumDown(n):

if n == 0: return 0

else: return n + sumDown(n)

Identify the bug using a progress measure, and fix the function.

**Hint:** What is the intended progress measure? Does it decrease in the recursive call?

Show solution

Intended progress measure is m(n) = n. But the recursive call uses sumDown(n), so m does not decrease (it stays equal), meaning the base case is never reached for n > 0.

Fix:

sumDown(n):

if n == 0: return 0

else: return n + sumDown(n − 1)

Now m(n) decreases by 1 each call until n = 0.

medium

Define a recursive function len(xs) that returns the length of a list xs, using:

- •len([])
- •len([x] + rest)

Then evaluate len([9, 8, 7, 6]) step by step.

**Hint:** Your base case should be the empty list. Your recursive call should use rest (the tail).

Show solution

Definition:

- •len([]) = 0
- •len([x] + rest) = 1 + len(rest)

Evaluation:

len([9, 8, 7, 6])

= 1 + len([8, 7, 6])

= 1 + (1 + len([7, 6]))

= 1 + (1 + (1 + len([6])))

= 1 + (1 + (1 + (1 + len([]))))

= 1 + (1 + (1 + (1 + 0)))

= 4

## Connections

- •Next: [Recurrence Relations](/tech-tree/recurrence-relations/) — recursion often implies a runtime recurrence like T(n) = T(n−1) + O(1) or T(n) = 2T(n/2) + O(n).
- •Next: [Divide and Conquer](/tech-tree/divide-conquer/) — recursion is the natural way to express splitting into subproblems and combining results.
- •Next: [Dynamic Programming](/tech-tree/dynamic-programming/) — start from a recursive definition, then add memoization to remove repeated work.

Quality: A (4.5/5)

[← back to tree](/tech-tree/)[browse all →](/tech-tree/inventory/)
