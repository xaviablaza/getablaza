---
title: What is an Algorithm
description: Step-by-step procedure to solve a problem. Input, process, output.
date: '2026-07-01'
scheduled: '2026-09-03'
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
inspiration_url: https://templeton.host/tech-tree/algorithm-concept/
inspiration_category: tech-tree
---

> Source-copy draft imported from [https://templeton.host/tech-tree/algorithm-concept/](https://templeton.host/tech-tree/algorithm-concept/). Names, domain references, and local media paths were adapted for Xavi Ablaza / getablaza.com.

[←Back to Tech Tree](/tech-tree/)

[inventory](/tech-tree/inventory/)[coverage](/tech-tree/coverage/)

# What is an Algorithm

AlgorithmsDifficulty: ★☆☆☆☆Depth: 0Unlocks: 15

Step-by-step procedure to solve a problem. Input, process, output.

## Interactive Visualization

⏮◀◀▶▶STEP0.25x1xZOOM

t=0s

## Core Concepts

- -Procedure (ordered steps)
- -Input (initial data)
- -Output (result)

## Key Symbols & Notation

-> (maps/transforms into)

## Essential Relationships

- -An algorithm is a finite, well-defined procedure that transforms Input -> Output

## Unlocks (1)

[Big O Notationlvl 2](/tech-tree/big-o/)

Advanced Learning Details

### Graph Position

5

Depth Cost

15

Fan-Out (ROI)

10

Bottleneck Score

0

Chain Length

### Cognitive Load

5

Atomic Elements

10

Total Elements

L0

Percentile Level

L3

Atomic Level

### All Concepts (7)

- - Algorithm - a step-by-step procedure to solve a problem
- - Step - a single, discrete action or instruction within an algorithm
- - Ordered sequence of steps - the notion that steps are executed in a specific order
- - Input - the data or instance provided to an algorithm
- - Process (transformation) - the operations performed on input during execution
- - Output - the result produced by executing the algorithm on the input
- - Problem instance - a specific case of the problem that the algorithm addresses

### Teaching Strategy

Self-serve tutorial - low prerequisites, straightforward concepts.

Every program you’ve ever run—sorting photos, searching a contact, recommending a video—depends on an algorithm: a clear procedure that turns inputs into outputs.

TL;DR:

An algorithm is a step-by-step procedure for solving a problem: it takes **input**, performs a **process** (ordered steps), and produces **output**. Good algorithms are precise, finite (they terminate), and correct (they produce the right output for every valid input).

## What Is an Algorithm?

### Why this concept matters

When people first learn programming, it can feel like the computer “just does things.” But computers don’t understand goals like “find the best route” or “put these numbers in order.” They only follow instructions.

An **algorithm** is the bridge between a human goal and mechanical execution.

- •You have a **problem** (e.g., “find the largest number in this list”).
- •You write a **procedure** (a sequence of steps) that always works.
- •A computer (or a person) can follow those steps exactly.

Learning what an algorithm is gives you a vocabulary for everything that comes later: correctness, efficiency, data structures, and eventually Big O notation.

### Definition (with the key idea)

An **algorithm** is a **finite, ordered sequence of unambiguous steps** that **transforms input into output**.

We can summarize it as a mapping:

**input** → **process** → **output**

Using the key symbol:

input → output (via a well-defined procedure)

### Intuition: a recipe, but stricter

Algorithms are often compared to recipes. That’s helpful, but algorithms are stricter than most recipes:

- •**No ambiguity**: “Cook until done” is ambiguous; an algorithm must say what “done” means.
- •**No missing steps**: every step must be explicit enough to follow.
- •**Works for all valid inputs**: not just one example.

### The three atomic concepts

This node is built from three atomic ideas:

1. 1)**Procedure (ordered steps)**

- •There is a first step, then a second, etc.
- •Order matters.

2. 2)**Input (initial data)**

- •The “stuff you start with.”
- •Could be numbers, text, images, a graph of roads, or even a stream of sensor readings.

3. 3)**Output (result)**

- •The “stuff you want at the end.”
- •Could be a number, a decision (yes/no), a sorted list, a route, or a compressed file.

### What an algorithm is not

It helps to separate “algorithm” from nearby ideas:

| Term | What it is | How it relates to algorithms |
| --- | --- | --- |
| Problem | A goal, stated in words | Algorithms solve problems |
| Program | Code written in a programming language | A program can implement an algorithm |
| Function | A reusable piece of code | Often implements an algorithm for a specific task |
| Heuristic | A rule of thumb that often works | Not guaranteed to be correct for all inputs |

A single algorithm can be implemented by many different programs (Python, Java, C++). And one program might contain multiple algorithms.

### Key properties you should expect from an algorithm

Most of the time in computer science, when we say “algorithm,” we expect these properties:

1. 1)**Definiteness (unambiguous steps)**

- •Each step is precisely stated.

2. 2)**Finiteness (termination)**

- •It finishes after a finite number of steps.

3. 3)**Correctness**

- •For every valid input, it produces the intended output.

4. 4)**Effectiveness (doable steps)**

- •Each step is basic enough to be carried out (by a computer or by a person with the right tools).

You don’t need to prove all of these formally yet—but you should know what you’re aiming for.

## Core Mechanic 1: Input → Process → Output (the algorithm “shape”)

### Why focus on this “shape”?

If you can reliably identify **input**, **process**, and **output**, you can:

- •translate word problems into precise tasks,
- •test whether your solution makes sense,
- •compare two different approaches to the same problem.

This is the backbone of algorithmic thinking.

### Input: what counts?

Input is any information the algorithm uses to do its job.

Examples:

- •A list of numbers: [3, 1, 4]
- •A name to search for: "Aisha"
- •A map (roads and distances)
- •A string: "racecar"

Sometimes input is empty (an algorithm might generate something, like the first 100 primes). Even then, you can think of the input as “the number 100” or “a stopping rule.”

### Output: the contract

Output is the result you promise to deliver.

Examples:

- •The maximum number in a list
- •The position (index) where a name occurs, or “not found”
- •A route with minimal total distance
- •True/False for whether a string is a palindrome

A good habit: define output as a **contract**.

> If the input satisfies X, the algorithm will output Y.

This mindset will later help you reason about correctness.

### Process: steps that transform

The process is the ordered list of operations that turns input into output.

At a beginner level, most algorithm steps come from a small toolkit:

- •**Assignment**: set a variable (e.g., best ← 0)
- •**Comparison**: is a < b?
- •**Iteration (loops)**: repeat steps for each item
- •**Selection (if/else)**: choose a branch based on a condition

### Example: “find the maximum” as input → output

Problem: Given a non-empty list of numbers, return the largest number.

- •Input: list L of length n ≥ 1
- •Output: max value in L
- •Process idea: scan through L, tracking the best seen so far

You can describe it in plain steps:

1. 1)Set best to the first element of L.
2. 2)For each remaining element x in L:

- •If x > best, set best ← x.

3. 3)Output best.

That is already an algorithm.

### Why order matters

An algorithm is not just “a set of steps,” it’s an **ordered** sequence.

Consider these two instructions:

- •“Pour batter into pan”
- •“Preheat oven”

The order affects what happens. In computing, order is even stricter: doing something before a variable is initialized might crash a program or produce nonsense.

### Algorithms can be deterministic or not

Many beginner algorithms are **deterministic**:

- •Same input → same output, every time.

Some algorithms use randomness (later you may see randomized algorithms), where:

- •Same input → output may vary, but still meets a goal (e.g., fast on average).

At this node, focus on deterministic algorithms; the input → output mapping is the cleanest.

### A gentle mathematical view: algorithms as functions

You can think of an algorithm like a function f that maps inputs to outputs:

f(input) → output

For example, if input is a number n and output is n²:

f(n) = n²

But be careful: not every algorithm is “just a formula.” Many algorithms define f through a sequence of steps (like scanning a list) rather than a closed-form expression.

### The arrow symbol →

You’ll see → used to mean “maps to” or “transforms into.”

- •Input → Output
- •State\_before → State\_after

Example: if we keep a variable best, one step might be:

(best, x) → (max(best, x))

You don’t need to write it this way all the time, but it captures the idea that each step transforms the current state into a new state.

## Core Mechanic 2: Precision, Termination, and Correctness

### Why these three?

Many “almost algorithms” fail because they are:

- •vague (not precise),
- •endless (don’t terminate), or
- •wrong on some inputs (not correct).

Learning to check these early saves a lot of time later.

## 1) Precision (unambiguous steps)

An algorithm must be clear enough that two different people (or computers) do the same thing.

Ambiguous instruction:

- •“Pick a large number from the list.”

Precise instruction:

- •“Return the maximum element of the list.”

Even more precise (when needed):

- •“If the list contains multiple equal maxima, returning that value is sufficient.”

Notice how precision often means defining edge cases.

## 2) Termination (it stops)

An algorithm should finish in a finite number of steps.

A loop like:

- •“Repeat forever”

is not an algorithm for a typical problem (unless the output is meant to be an ongoing stream).

A common way to ensure termination is to have a loop that makes measurable progress:

- •For each element in a finite list (you will eventually run out)
- •While i ≤ n, increase i by 1 each time

### Example of a terminating loop

If i starts at 1 and you do i ← i + 1 until i = n, you will stop after n − 1 increments.

## 3) Correctness (it gives the right answer)

Correctness means: for **every valid input**, the output matches the problem’s definition.

At this stage, you can reason informally by asking:

- •Does it work on typical cases?
- •Does it work on edge cases?
- •Can I explain why it always works?

### A mini “proof idea” using invariants (informal)

An **invariant** is a statement that stays true as your algorithm runs.

For the maximum-finding algorithm, an invariant could be:

- •After scanning the first k elements, best is the maximum of those k elements.

Why that helps:

- •Initially (k = 1), best is the maximum of the first element (trivially true).
- •Each step updates best to keep the statement true.
- •At the end (k = n), best is the maximum of the whole list.

You don’t need formal proof syntax yet. But this style of reasoning—maintaining a true statement while progressing—will become extremely powerful.

### Algorithms vs. solutions that “seem to work”

If you test only a few inputs, you might miss failures.

Example: an incorrect algorithm for maximum might start with best ← 0. It works for lists of positive numbers but fails for lists like [-5, -2].

Correctness requires thinking beyond a few examples.

### A note about data types (numbers vs. vectors)

Later you’ll see algorithms that operate on vectors like **v** ∈ ℝⁿ. For instance, an algorithm might take **v** as input and output ‖**v**‖ (its length).

Even though this node is foundational, the same input → process → output framing applies:

- •Input: **v**
- •Process: compute ∑ᵢ vᵢ², then take √
- •Output: ‖**v**‖ = √(∑ᵢ vᵢ²)

You don’t need vector math to understand what an algorithm is, but it shows that algorithms generalize far beyond lists of integers.

## Application/Connection: From “Algorithm” to Big O Notation

### Why this connection matters

Once you can clearly describe an algorithm, the next natural question is:

> How efficient is it?

Two algorithms can solve the same problem but take very different amounts of time as input size grows. Big O notation is the standard language for talking about that growth.

This node “unlocks” Big O because Big O is about algorithms specifically—their step counts, memory usage, and scaling behavior.

### Step counting: the seed of complexity

Consider the maximum-finding algorithm on a list of length n.

- •It compares each element (after the first) once.
- •Number of comparisons is (n − 1).

So the work grows roughly proportionally to n.

That idea becomes:

- •Time complexity ≈ O(n)

Another example: checking if two lists are identical element-by-element also takes work proportional to n in the worst case.

### Comparing two approaches (preview)

Suppose you want to find whether a number x is in a list of n numbers.

Approach A: scan from the beginning until you find x.

- •Worst case: x is not there → you check all n elements → O(n)

Approach B (if the list is sorted): use binary search.

- •Each step halves the remaining search space
- •Steps ≈ log₂(n) → O(log n)

At this node, you don’t need to master these algorithms yet; the key point is:

- •Big O compares algorithms based on how their step counts grow with input size.

### What you need before Big O

To understand Big O well, you need the habits from this lesson:

- •Define **input size** (often n)
- •Describe the **process** (what operations repeat?)
- •Identify **termination** (how many steps until it stops?)

Once you can do that, you can translate “steps” into growth rates.

### Where algorithms show up everywhere

Algorithms aren’t only for “classic CS problems.” They appear in:

- •Web search (ranking pages)
- •Maps (route planning)
- •Machine learning (training procedures)
- •Security (encryption and hashing)
- •Graphics (rendering and compression)

In all cases, the structure remains:

input → process → output

That’s why this node is foundational.

## Worked Examples (3)

### Example 1: Algorithm to compute the sum of a list

Problem: Given a list of numbers L = [ℓ₁, ℓ₂, …, ℓₙ], compute the sum S = ∑ᵢ ℓᵢ.

Input: list L of length n (possibly n = 0).

Output: number S (0 if the list is empty).

1. Define the goal precisely:

   We want output S such that

   S = ∑ᵢ ℓᵢ.

   If n = 0, then S = 0.
2. Write a clear procedure:

   1) Set total ← 0.

   2) For each element x in L:

   total ← total + x

   3) Output total.
3. Trace it on a concrete input L = [3, 1, 4]:

   Start: total = 0

   Read 3: total = 0 + 3 = 3

   Read 1: total = 3 + 1 = 4

   Read 4: total = 4 + 4 = 8

   Output: 8
4. Check termination:

   The loop runs once per element.

   If the list has n elements, there are exactly n iterations, so it stops.
5. Check correctness (informal invariant):

   Invariant: after processing the first k elements, total = ∑\_{i=1..k} ℓᵢ.

   - •Base case k = 0: total = 0 matches the empty sum.
   - •Step: when adding the next element, the invariant remains true.
   - •End: when k = n, total = ∑\_{i=1..n} ℓᵢ, which is exactly the desired output.

**Insight:** Many algorithms are “accumulators”: maintain a running value (total, best, count) that summarizes what you’ve seen so far. The key is choosing an invariant that explains why the accumulator is always correct.

### Example 2: Algorithm to find the maximum element in a list

Problem: Given a non-empty list L = [ℓ₁, ℓ₂, …, ℓₙ] with n ≥ 1, return max(L).

Input: non-empty list of numbers.

Output: the largest number in the list.

1. Be precise about input constraints:

   The list must be non-empty (n ≥ 1) so that a maximum exists as one of the elements.
2. Procedure (step-by-step):

   1) Set best ← ℓ₁.

   2) For i = 2 to n:

   If ℓᵢ > best, set best ← ℓᵢ.

   3) Output best.
3. Trace it on L = [2, 9, 5, 9]:

   Start: best = 2

   Compare 9 > 2 → yes, best = 9

   Compare 5 > 9 → no, best = 9

   Compare 9 > 9 → no (not greater), best = 9

   Output: 9
4. Termination:

   The loop runs from i = 2 to n, which is (n − 1) iterations, so it must finish.
5. Correctness reasoning (invariant):

   Invariant: after processing ℓ₁..ℓ\_k, best = max(ℓ₁..ℓ\_k).

   - •Initially k = 1: best = ℓ₁ = max(ℓ₁).
   - •Update step: when seeing ℓ\_{k+1}, setting best ← max(best, ℓ\_{k+1}) preserves the invariant.
   - •At k = n: best = max(ℓ₁..ℓₙ) = max(L), which is the required output.

**Insight:** A good algorithm often keeps a small summary of what matters (here: the best seen so far) instead of storing everything again. This is both conceptually clean and efficient.

### Example 3: Algorithm to check whether a string is a palindrome

Problem: Given a string s of length n, return True if it reads the same forward and backward, else False.

Input: string s (possibly empty).

Output: Boolean (True/False).

1. Clarify what it means:

   A string s is a palindrome if

   ∀ i, s[i] = s[n − 1 − i]

   for indices i in the first half of the string.
2. Procedure:

   1) Let n be the length of s.

   2) For i = 0 to ⌊(n − 1)/2⌋:

   If s[i] ≠ s[n − 1 − i], output False.

   3) Output True.
3. Trace on s = "racecar" (n = 7):

   i=0: s[0]=r, s[6]=r → equal

   i=1: s[1]=a, s[5]=a → equal

   i=2: s[2]=c, s[4]=c → equal

   i=3 is the middle; loop ends

   Output True
4. Trace on s = "hello" (n = 5):

   i=0: h vs o → not equal

   Output False immediately
5. Termination:

   The loop runs at most ⌊n/2⌋ iterations, so it always stops.
6. Correctness intuition:

   The algorithm checks exactly the pairs of characters that must match. If any pair fails, the definition is violated, so False is correct. If all pairs match, the definition holds, so True is correct.

**Insight:** Many algorithms work by reducing the problem to a set of required checks. Here, the definition itself suggests the algorithm: compare symmetric pairs until you reach the middle.

## Key Takeaways

- ✓

  An algorithm is a finite, ordered sequence of unambiguous steps that transforms **input** → **output**.
- ✓

  Algorithms are about procedures, not programming languages: the same algorithm can be implemented in many languages.
- ✓

  Always identify the algorithm “shape”: input, process (steps), output (contract).
- ✓

  Good algorithms are precise (no vague steps), terminate (finish), and are correct (work for all valid inputs).
- ✓

  Informal invariants (“what stays true after each step”) are a powerful way to reason about correctness.
- ✓

  Order matters: changing step order can change results or break the procedure.
- ✓

  This node prepares you for analyzing efficiency and scaling, which leads directly to Big O notation.

## Common Mistakes

- ✗

  Confusing an algorithm with a program: code is one implementation; the algorithm is the underlying procedure.
- ✗

  Leaving steps ambiguous (e.g., “repeat until done”) without defining what “done” means or how to detect it.
- ✗

  Forgetting edge cases (empty list, negative numbers, duplicates), leading to algorithms that work only sometimes.
- ✗

  Writing loops that don’t make progress toward stopping, risking non-termination.

## Practice

easy

Write an algorithm (plain English steps) that counts how many even numbers are in a list L of integers.

**Hint:** Use an accumulator variable that starts at 0, and increase it when you see an even number (x mod 2 = 0).

Show solution

Input: list L.

Output: count of elements x ∈ L such that x is even.

Algorithm:

1) Set count ← 0.

2) For each element x in L:

If x mod 2 = 0, set count ← count + 1.

3) Output count.

Termination: the loop runs once per element.

Correctness idea: after processing k elements, count equals the number of even elements among the first k elements.

easy

Design an algorithm that returns True if a list L contains the number 0, otherwise returns False.

**Hint:** Scan the list and stop early if you find 0.

Show solution

Input: list L of numbers.

Output: Boolean.

Algorithm:

1) For each element x in L:

If x = 0, output True.

2) After the loop ends, output False.

Termination: finite list → loop ends.

Correctness: if 0 appears, the algorithm finds it and returns True; if it never appears, returning False matches the definition.

medium

A student proposes this algorithm to find the maximum: “Set best ← 0. For each x in L, if x > best then best ← x. Output best.” Give a counterexample input where it fails, and fix the algorithm.

**Hint:** Think about lists with all negative numbers. The fix is usually to initialize best using the first element of the list (assuming non-empty).

Show solution

Counterexample: L = [−5, −2].

Student algorithm:

best = 0

Check −5 > 0? no

Check −2 > 0? no

Outputs 0, but 0 is not in the list and max(L) = −2.

Fix (for non-empty L):

1) Set best ← first element of L.

2) For each remaining element x in L:

If x > best, best ← x.

3) Output best.

This works for negative numbers because best starts as an actual element of L.

## Connections

Next node: [Big O Notation](/tech-tree/big-o/)

Related future ideas you’ll meet soon:

- •Searching algorithms (linear search, binary search)
- •Sorting algorithms (selection sort, merge sort)
- •Correctness reasoning (invariants)

This node is the foundation: Big O, data structures, and algorithm design all assume you can clearly state input → process → output.

Quality: A (4.6/5)

[← back to tree](/tech-tree/)[browse all →](/tech-tree/inventory/)
