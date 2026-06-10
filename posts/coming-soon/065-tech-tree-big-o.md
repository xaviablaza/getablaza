---
title: Big O Notation
description: Asymptotic upper bound on algorithm complexity. O(1), O(n), O(n^2), O(log n).
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
permalink: /tech-tree/big-o/
---

[←Back to Tech Tree](/tech-tree/)

[inventory](/tech-tree/inventory/)[coverage](/tech-tree/coverage/)

# Big O Notation

AlgorithmsDifficulty: ★★☆☆☆Depth: 2Unlocks: 14

Asymptotic upper bound on algorithm complexity. O(1), O(n), O(n^2), O(log n).

## Interactive Visualization

⏮◀◀▶▶STEP0.25x1xZOOM

t=0s

## Core Concepts

- -Asymptotic behavior (n -> infinity): Big-O concerns growth of functions for sufficiently large input sizes
- -Upper-bound notion: Big-O expresses that one function grows at most as quickly as another (up to a constant) for large n
- -Dominant-term abstraction: constant factors and lower-order terms are ignored, leaving the dominant growth rate

## Key Symbols & Notation

O(g(n)) - Big-O notation denoting the set of functions asymptotically bounded above by g(n)

## Essential Relationships

- -Formal definition (existential inequality): f(n) is in O(g(n)) iff there exist constants c>0 and n0 such that for all n >= n0, f(n) <= c \* g(n)
- -Transitivity (ordering property): if f = O(g) and g = O(h) then f = O(h)

## Prerequisites (2)

[What is an Algorithm5 atoms](/tech-tree/algorithm-concept/)[Limits5 atoms](/tech-tree/limits/)

## Unlocks (9)

[Complexity Classeslvl 4](/tech-tree/complexity-classes/)[Greedy Algorithmslvl 3](/tech-tree/greedy-algorithms/)[Amortized Analysislvl 3](/tech-tree/amortized-analysis/)[Basic Sortinglvl 2](/tech-tree/sorting-basic/)[Binary Searchlvl 2](/tech-tree/binary-search/)[Balanced Treeslvl 3](/tech-tree/balanced-trees/)[Randomized Algorithmslvl 4](/tech-tree/randomized-algorithms/)[Online Algorithmslvl 4](/tech-tree/online-algorithms/)

+1 more...

Advanced Learning Details

### Graph Position

28

Depth Cost

14

Fan-Out (ROI)

10

Bottleneck Score

2

Chain Length

### Cognitive Load

6

Atomic Elements

21

Total Elements

L0

Percentile Level

L4

Atomic Level

### All Concepts (9)

- - Big O (asymptotic upper bound) as a way to classify algorithm resource usage by growth rate
- - Function f(n) that maps input size n to a resource measure (time or space) used by an algorithm
- - Input size n as the primary independent variable for complexity (distinct from raw inputs)
- - Dominant term (leading-order behavior) of a function determines its asymptotic class
- - Ignoring constant factors and lower-order terms when classifying growth
- - Common named growth classes (constant, logarithmic, linear, linearithmic, quadratic, exponential, factorial) with examples O(1), O(log n), O(n), O(n log n), O(n^2), O(2^n), O(n!)
- - Formal (inequality-based) definition of Big O using existence of positive constants c and n0
- - Big O as a set-theoretic notion (O(g(n)) denotes the set of functions bounded above by g up to constant factor for large n)
- - Interpretation of Big O as usually describing worst-case asymptotic behavior of an algorithm (as opposed to best- or average-case)

### Teaching Strategy

Deep-dive lesson - accessible entry point but dense material. Use worked examples and spaced repetition.

When you pick an algorithm, you’re really picking a growth rate: how the time (or memory) cost scales as the input size n gets large. Big O is the compact language we use to talk about that growth—without getting distracted by machine speed, constant factors, or tiny lower-order details.

TL;DR:

Big O notation, written O(g(n)), describes an asymptotic upper bound on how fast an algorithm’s resource usage can grow with input size n. It ignores constant factors and lower-order terms, keeping only the dominant growth rate (like O(1), O(log n), O(n), O(n²)). To use it, model the work as a function T(n) and keep the term that dominates as n → ∞.

## What Is Big O Notation?

### Why we need a “growth language”

If you time an algorithm on your laptop, the result depends on many accidental details:

- •CPU speed and cache
- •programming language and compiler
- •implementation choices
- •the specific input data

But when we compare algorithms, we want something *portable*: a way to say “this will scale well” or “this will blow up” as the input size n grows.

That’s what Big O does. It describes *asymptotic behavior*: what happens as n → ∞.

### The idea in one sentence

**Big O notation gives an asymptotic upper bound on a function’s growth.**

If an algorithm takes time T(n), saying

T(n) ∈ O(g(n))

means: for sufficiently large n, T(n) grows *no faster than* a constant multiple of g(n).

### Formal definition (upper bound)

We say f(n) ∈ O(g(n)) if there exist constants c > 0 and n₀ such that

∀ n ≥ n₀: 0 ≤ f(n) ≤ c · g(n)

Important parts to notice:

- •**“For sufficiently large n”**: we only care after some threshold n₀.
- •**Constant multiplier c**: we allow scaling by a constant.
- •**Upper bound**: f is eventually not bigger than c · g.

### What Big O is *not*

Big O is often used informally as “the runtime,” but technically:

- •It is a **set of functions** (all functions bounded by g(n) up to constants).
- •It is an **upper bound**, not an exact equality.

So if someone says “this algorithm is O(n),” they mean “its runtime is in O(n)”—an upper bound.

### Why ignoring details is a feature, not a bug

Suppose an algorithm’s time is

T(n) = 3n² + 10n + 50

For small n, the +50 might matter. For large n, the 3n² dominates.

As n → ∞:

- •n² eventually dwarfs n
- •n² eventually dwarfs constants

Big O intentionally ignores:

- •constant factors (like the 3)
- •lower-order terms (like 10n and 50)

and keeps the **dominant term**: O(n²).

### Big O can describe more than time

You can apply the same idea to:

- •**Space usage** S(n)
- •**Network calls**
- •**Disk I/O**

Any resource that can be modeled as a function of input size n.

### A quick intuition: “ceilings”

Think of g(n) as a ceiling shape. Saying f(n) ∈ O(g(n)) means that eventually, f(n) stays under some scaled version of that ceiling.

This is why Big O is an upper bound: it promises the function won’t grow faster than that ceiling (for large n).

## Core Mechanic 1: Asymptotic Upper Bounds and Dominant Terms

### Why upper bounds matter for algorithms

When you run an algorithm, the exact time can vary by input. For example, searching an array:

- •Best case: target is first element
- •Worst case: target is last or missing

Big O is commonly used to express **worst-case asymptotic upper bounds**, because worst-case gives a safety guarantee.

### From a runtime expression to Big O

A common workflow:

1. 1)Write a function T(n) for the amount of work.
2. 2)Simplify it by keeping only the term that dominates as n → ∞.
3. 3)Drop constant factors.

#### Example: nested loops

If you have two loops each running about n times, the total iterations are about n · n = n², giving O(n²).

#### Example: linear loop plus constant work

If you do 7 operations per element, you get T(n) = 7n, which is O(n).

### Dominant-term reasoning (with a limit intuition)

Even though Big O doesn’t require calculus, your prerequisite knowledge of limits gives a clean intuition.

Consider f(n) = 3n² + 10n + 50 and g(n) = n².

Look at the ratio:

f(n) / g(n)

= (3n² + 10n + 50) / n²

= 3 + 10/n + 50/n²

Now take n → ∞:

limₙ→∞ (3 + 10/n + 50/n²)

= 3 + 0 + 0

= 3

So for large n, f(n) behaves like about 3 · n².

That implies f(n) ≤ c · n² for some constant c (for sufficiently large n), hence f(n) ∈ O(n²).

### Common Big O “family” functions

Here are the growth rates you’ll see constantly:

| Name | Big O | Typical pattern | Intuition |
| --- | --- | --- | --- |
| Constant | O(1) | fixed number of steps | doesn’t depend on n |
| Logarithmic | O(log n) | repeatedly halve / double | “how many times can I divide?” |
| Linear | O(n) | single pass | proportional to n |
| Linearithmic | O(n log n) | split + combine | common in efficient sorting |
| Quadratic | O(n²) | double nested loops | pairwise comparisons |
| Cubic | O(n³) | triple loops | many 3-way combinations |
| Exponential | O(2ⁿ) | branching recursion | doubles each step |

At difficulty 2, the “core” set is usually O(1), O(log n), O(n), O(n²).

### A concrete scale comparison

Suppose n = 1,000,000.

- •O(1): ~1 step
- •O(log₂ n): ~20 steps (since 2²⁰ ≈ 1,048,576)
- •O(n): 1,000,000 steps
- •O(n²): 10¹² steps

The *difference between O(n) and O(n²)* is enormous at large n.

### Big O vs “exact steps”

Big O can hide meaningful constants, especially for small n.

Example:

- •Algorithm A: T₁(n) = 100n
- •Algorithm B: T₂(n) = n²

Big O says A is O(n) and B is O(n²), so A scales better.

But for n = 50:

- •100n = 5000
- •n² = 2500

So B is faster at n = 50, even though it scales worse.

That’s why Big O is about long-run scaling, not always about what is fastest for small inputs.

### Quick “rules of thumb” for simplifying to Big O

Let T(n) be a polynomial-like expression:

- •Drop constants: O(7n) → O(n)
- •Keep the highest power: O(n² + n) → O(n²)
- •Different bases of log are equivalent up to a constant: log₂ n vs log₁₀ n

Because:

log\_a n = (log\_b n) / (log\_b a)

and 1/(log\_b a) is just a constant factor.

## Core Mechanic 2: Reading Code Patterns as Big O

### Why pattern recognition matters

In real code, you rarely start with a clean formula. You start with loops, recursion, and data structure operations.

So the practical skill is: **look at the shape of the code and map it to a growth rate.**

Below are the most common patterns.

### O(1): constant-time operations

Typical examples (conceptually):

- •access array element A[i]
- •update a variable
- •swap two values

These do not scale with n.

Caveat: in real systems, some “simple” operations may hide complexity (like hash table worst-cases), but at this level we treat them as O(1) average-case.

### O(n): a single pass

Pattern:

- •one loop from 1 to n
- •visiting each element once

If you do constant work each iteration, total work is proportional to n.

### O(n²): nested loops

Pattern:

- •for i in 1..n:
- •for j in 1..n:

Total iterations: n · n = n².

A common variant is when the inner loop depends on i:

- •for i in 1..n:
- •for j in 1..i:

Total iterations:

∑ᵢ₌₁ⁿ i

= n(n + 1)/2

= (n² + n)/2

Now simplify to Big O:

(n² + n)/2 ∈ O(n²)

because the n² term dominates and 1/2 is a constant.

### O(log n): halving behavior

Pattern:

- •while n > 1:
- •n = n/2

How many times can you halve n before it becomes 1?

If you halve k times:

n / 2ᵏ = 1

⇒ 2ᵏ = n

⇒ k = log₂ n

So the loop runs O(log n) times.

This is the key intuition behind binary search.

### O(n log n): “do log n work for each of n items” (or split + combine)

Two common sources:

1) A loop of n iterations, each doing O(log n) work (like inserting into a balanced tree):

T(n) = n · log n

2) Divide-and-conquer algorithms that split the problem and combine results efficiently.

Classic example: mergesort has runtime O(n log n).

### Combining parts: add vs multiply

When you see pieces of code one after another:

- •Do A, then do B

their costs add:

T(n) = T\_A(n) + T\_B(n)

Big O becomes dominated by the larger term.

When one piece is *inside* another (nested):

- •For each item, do B

their costs multiply:

T(n) = T\_outer(n) · T\_inner(n)

### Best-case, average-case, worst-case

Big O is most often used for worst-case.

But you’ll also see:

- •Best case: e.g., a search finds the item immediately (O(1))
- •Average case: expected runtime under a distribution of inputs

A helpful table:

| Case | Meaning | Why you care |
| --- | --- | --- |
| Best-case | minimum work | optimistic, often not guaranteed |
| Average-case | expected work | realistic if assumptions hold |
| Worst-case | maximum work | guarantees performance ceiling |

### Time vs space Big O

An algorithm can be fast but memory-hungry or vice versa.

Examples:

- •Storing an array of n elements uses O(n) space.
- •A few variables uses O(1) space.

You should always ask: “What resource are we bounding?”

Time: T(n) ∈ O(g(n))

Space: S(n) ∈ O(h(n))

Same notation, different resource.

## Application/Connection: Big O in Real Algorithm Choices

### Why Big O changes what problems are feasible

Big O is the difference between:

- •“This runs in under a second for n = 10⁶”
- •“This will never finish”

Quadratic algorithms (O(n²)) are often fine for n ≈ 10³ to 10⁴, but become painful past that. Linearithmic (O(n log n)) scales to much larger n.

### Choosing between common approaches

Here are common tasks and what Big O suggests.

| Task | Naive approach | Big O | Better approach | Big O |
| --- | --- | --- | --- | --- |
| Find an element in unsorted array | scan | O(n) | (can’t asymptotically beat without assumptions) | O(n) |
| Find in sorted array | scan | O(n) | binary search | O(log n) |
| Sort numbers | bubble/selection | O(n²) | mergesort/heapsort | O(n log n) |
| Check duplicates | compare all pairs | O(n²) | hash set | O(n) average |

Big O doesn’t tell you everything, but it quickly eliminates bad options at scale.

### Connecting Big O to future nodes

This node unlocks several big ideas because Big O is the *entry point* to complexity theory and algorithm design.

- •Complexity Classes: formalizing what “efficient” means (often polynomial time like O(nᵏ)).
- •Greedy Algorithms: evaluating tradeoffs and why a greedy choice can be efficient.
- •Amortized Analysis: when a single operation is expensive but the *average over many* is small (still described with Big O).
- •Basic Sorting and Binary Search: canonical examples of O(n²) vs O(n log n) and O(log n).

### A note about “Big O as a contract”

When you claim an algorithm is O(n log n), you’re making a promise:

- •There exists some constant c and some threshold n₀
- •such that beyond n₀ your algorithm’s runtime is ≤ c · n log n

This is why careful definitions matter: they let you prove performance properties independent of hardware.

### Big O and input size modeling

Choosing n is part of the modeling step:

- •For an array, n might be number of elements.
- •For a graph, n might be vertices and m edges.

You’ll later see multi-parameter Big O like O(n + m). For now, focus on single-parameter n to build solid intuition.

### Final mental model

Big O is a *zoomed-out* view. Zoom out far enough (n large), and only the overall shape matters:

- •constant
- •logarithmic
- •linear
- •quadratic

Learning to see that shape in code is one of the highest-leverage skills in algorithms.

## Worked Examples (3)

### Simplifying a runtime expression to Big O

An algorithm has runtime T(n) = 12n + 3n² + 100. Find its Big O class using dominant-term reasoning.

1. Start with the runtime function:

   T(n) = 12n + 3n² + 100
2. Reorder by degree (highest power first):

   T(n) = 3n² + 12n + 100
3. Identify the dominant term as n → ∞:

   - •n² grows faster than n
   - •n² grows faster than constants
4. Drop lower-order terms and constant factors:

   T(n) ∈ O(n²)

**Insight:** Big O keeps the growth rate that dominates for large n. Any polynomial is dominated by its highest-degree term.

### Counting work in a triangular nested loop

Consider code where i runs from 1 to n, and for each i, j runs from 1 to i. Assume the inner loop body is O(1). Compute T(n) and simplify to Big O.

1. Total work equals the total number of inner-loop iterations:

   T(n) = ∑ᵢ₌₁ⁿ i
2. Use the closed form for the sum of the first n integers:

   ∑ᵢ₌₁ⁿ i = n(n + 1)/2
3. Expand:

   T(n) = (n² + n)/2
4. Simplify to Big O by dropping constants and lower-order terms:

   (n² + n)/2 ∈ O(n²)

**Insight:** Not all nested loops are exactly n² iterations. Summations help you count precisely; Big O then compresses the result.

### Why halving loops are O(log n)

A loop repeatedly halves n until it reaches 1: while n > 1: n = n/2. How many iterations does it run?

1. After k iterations, n becomes:

   n / 2ᵏ
2. Stop condition is when this is ≤ 1:

   n / 2ᵏ ≤ 1
3. Solve for k:

   n ≤ 2ᵏ

   ⇒ log₂ n ≤ k
4. So k grows proportionally to log n:

   iterations ∈ O(log n)

**Insight:** Logarithms appear when you repeatedly multiply/divide by a constant factor (like halving).

## Key Takeaways

- ✓

  Big O, written O(g(n)), is an asymptotic upper bound: for large n, f(n) ≤ c · g(n) for some constants c, n₀.
- ✓

  Big O focuses on growth as n → ∞, ignoring constant factors and lower-order terms.
- ✓

  Common growth rates: O(1), O(log n), O(n), O(n log n), O(n²).
- ✓

  Sequential parts add (T = A + B), nested parts multiply (T = A · B).
- ✓

  O(log n) often comes from repeated halving/doubling; O(n²) often comes from comparing all pairs.
- ✓

  Big O can describe time or space; always state which resource you mean.
- ✓

  Big O is usually a worst-case upper bound, providing a performance guarantee ceiling.

## Common Mistakes

- ✗

  Thinking O(n) means “exactly n steps.” It means “at most proportional to n” for sufficiently large n (up to constants).
- ✗

  Forgetting the difference between sequential vs nested code when combining costs (adding when you should multiply, or vice versa).
- ✗

  Treating Big O as a precise benchmark for small n; constants can dominate at small sizes.
- ✗

  Assuming every nested loop is O(n²); many are triangular (∑ i) or depend on changing bounds. Count carefully.

## Practice

easy

Simplify T(n) = 5n³ + 20n² + 7 to Big O.

**Hint:** Which term dominates as n → ∞? Drop constants and lower powers.

Show solution

The dominant term is 5n³. Dropping constants and lower-order terms gives T(n) ∈ O(n³).

medium

A loop runs i from 1 to n. Inside it, a loop runs j from 1 to 100. The body is O(1). What is the total time complexity in Big O?

**Hint:** The inner loop bound is constant with respect to n.

Show solution

Inner loop does 100 iterations → O(1) per outer iteration. Total T(n) = n · 100 ∈ O(n).

medium

You have an array of length n that is already sorted. You want to check whether a value x is present. Compare the Big O of (1) scanning from start to end and (2) binary search.

**Hint:** Scanning checks items one by one; binary search halves the search interval each step.

Show solution

Scan: O(n). Binary search: O(log n) because each comparison halves the remaining range.

## Connections

Up next, Big O becomes the backbone for nearly every algorithms topic:

- •[Binary Search](/tech-tree/binary-search/)
- •[Basic Sorting](/tech-tree/sorting-basic/)
- •[Amortized Analysis](/tech-tree/amortized-analysis/)
- •[Greedy Algorithms](/tech-tree/greedy-algorithms/)
- •[Complexity Classes](/tech-tree/complexity-classes/)

Quality: A (4.2/5)

[← back to tree](/tech-tree/)[browse all →](/tech-tree/inventory/)
