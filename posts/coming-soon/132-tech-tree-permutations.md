---
title: Permutations
description: Ordered arrangements. n! and nPr formulas.
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
inspiration_url: https://templeton.host/tech-tree/permutations/
inspiration_category: tech-tree
---

> Source-copy draft imported from [https://templeton.host/tech-tree/permutations/](https://templeton.host/tech-tree/permutations/). Names, domain references, and local media paths were adapted for Xavi Ablaza / getablaza.com.

[←Back to Tech Tree](/tech-tree/)

[inventory](/tech-tree/inventory/)[coverage](/tech-tree/coverage/)

# Permutations

Discrete MathDifficulty: ★★☆☆☆Depth: 1Unlocks: 1

Ordered arrangements. n! and nPr formulas.

## Interactive Visualization

⏮◀◀▶▶STEP0.25x1xZOOM

t=0s

## Core Concepts

- -Order sensitivity: arrangements are counted differently when item order changes (order matters).
- -k-permutation as ordered selection without replacement: choosing k distinct items from n where sequence position matters.
- -Full permutation: arranging all n distinct items uses the factorial count (product of integers 1 through n).

## Key Symbols & Notation

factorial symbol '!' (n! = 1\*2\*...\*n)permutation operator 'n P k' (also written P(n,k))

## Essential Relationships

- -n P k = n\*(n-1)\*...\*(n-k+1), equivalently n P k = n! / (n-k)!

## Prerequisites (1)

[Counting Principles6 atoms](/tech-tree/counting-basic/)

## Unlocks (1)

[Combinationslvl 2](/tech-tree/combinations/)

## Referenced by (1)

Where this concept shows up in the operating-finance and personal-finance graphs.

### From Business (1)

[Shapley valueBusiness

Shapley value is defined as an average marginal contribution over all n! orderings of players, requiring understanding of permutation counting and enumeration](/business/shapley-value/)

Advanced Learning Details

### Graph Position

12

Depth Cost

1

Fan-Out (ROI)

1

Bottleneck Score

1

Chain Length

### Cognitive Load

6

Atomic Elements

16

Total Elements

L0

Percentile Level

L4

Atomic Level

### All Concepts (5)

- - Permutation: an ordered arrangement of distinct items (order matters)
- - Full permutation: arranging all n distinct items (counts of complete orderings)
- - Partial permutation (r-permutation): arranging r ordered positions chosen from n distinct items
- - Factorial operation (n!): product of all positive integers from 1 to n
- - Special factorial value: 0! = 1 (convention for empty product)

### Teaching Strategy

Deep-dive lesson - accessible entry point but dense material. Use worked examples and spaced repetition.

If you’re assigning 1st/2nd/3rd place, building a password, or seating people in labeled chairs, you’re not just choosing items—you’re arranging them. That “order matters” twist is exactly what permutations count.

TL;DR:

A permutation is an ordered arrangement. Arranging all n distinct items gives n!. Choosing and ordering k distinct items from n (no repeats) gives n P k = n!/(n−k)!. Use permutations when positions are distinct and swapping items creates a new outcome.

## What Is a Permutation?

### The idea: same items, different order ⇒ different outcome

A **permutation** is an **ordered arrangement** of items. The central question permutations answer is:

> How many outcomes are there when the **positions matter**?

You already know the multiplication rule: if you make a sequence of choices and each step has a certain number of options, you multiply those counts.

Permutations are what you get when those choices are:

- •**Without replacement** (you don’t reuse items), and
- •**Order-sensitive** (different orders count as different outcomes).

### Why “order matters” is a big deal

Consider the two-letter sequence made from {A, B, C} without repeats.

- •AB and BA use the same letters.
- •But they are different sequences.
- •So they must be counted separately.

That is the signature of permutations.

### Three common “permutation contexts”

1. 1)**Ranking / podiums**: 1st, 2nd, 3rd are different positions.
2. 2)**Seating in labeled seats**: seat #1 vs seat #2 are different.
3. 3)**Codes / strings** (without repetition): first character vs second character are different.

### Vocabulary you’ll see

- •**Full permutation**: arrange all n distinct items.
- •**k-permutation**: choose and arrange k distinct items from n (no repeats).

We’ll build both from the same counting principle: multiply the number of choices available at each position.

### Notation

- •**Factorial**: n! = 1 · 2 · 3 · … · n (with 0! = 1 by convention).
- •**Permutation operator**: n P k (also written P(n, k)) counts ordered selections of length k from n without replacement.

We’ll derive the formulas rather than memorizing them.

## Core Mechanic 1: Full Permutations and Factorials (n!)

### Why factorials appear

Suppose you have n distinct items and you want to arrange **all of them** in a line.

Think in positions:

- •Position 1: n choices
- •Position 2: n − 1 choices (one item is used)
- •Position 3: n − 2 choices
- •…
- •Position n: 1 choice

By the multiplication rule, the total number of arrangements is:

n · (n − 1) · (n − 2) · … · 2 · 1

That product is called **n factorial**, written **n!**.

### Definition

For integer n ≥ 1:

n! = ∏ᵢ₌₁ⁿ i = 1 · 2 · 3 · … · n

And by convention:

0! = 1

### Why 0! = 1 (intuition, not just a rule)

A “full permutation of 0 items” means: how many ways to arrange nothing? There is exactly **one** empty arrangement.

Also, the recursion for factorials works cleanly:

n! = n · (n − 1)!

If we set n = 1:

1! = 1 · 0!

But 1! = 1, so 0! must be 1.

### Small examples (build intuition)

- •3! = 3 · 2 · 1 = 6

The 6 arrangements of (A, B, C) are:

ABC, ACB, BAC, BCA, CAB, CBA.

- •4! = 24

This already grows fast; factorial growth is one reason permutation counts get large quickly.

### A useful pattern: factorial cancellation

Factorials often simplify when you divide them:

\( \frac{n!}{(n−1)!} \)

Work it out by expansion:

n! = n · (n − 1) · (n − 2) · … · 1

(n − 1)! = (n − 1) · (n − 2) · … · 1

So:

n! / (n − 1)! = n

This “cancellation idea” is the backbone of the n P k formula you’ll meet next.

### When to use n!

Use n! when:

- •You arrange **all** n distinct items.
- •Every position is part of the outcome.
- •Items are not repeated.

If you’re not using all items (only k of them), you need k-permutations instead.

## Core Mechanic 2: k-Permutations (n P k) and the n!/(n−k)! Formula

### The question k-permutations answer

> How many ordered sequences of length k can you form from n distinct items, **without replacement**?

Example contexts:

- •Gold/silver/bronze chosen from n runners (k = 3)
- •A 4-character code from n symbols without repeats (k = 4)
- •Choosing a president, vice president, and treasurer from n people (k = 3)

### Build it from the multiplication rule (the “why”)

Imagine filling k positions one by one.

- •Position 1: n choices
- •Position 2: n − 1 choices
- •Position 3: n − 2 choices
- •…
- •Position k: n − (k − 1) choices

Multiply them:

n P k = n · (n − 1) · (n − 2) · … · (n − k + 1)

This is already a perfectly good formula.

### Convert to factorial form (the “how”)

Factorials let us write that product compactly.

Start with n!:

n! = n · (n − 1) · (n − 2) · … · (n − k + 1) · (n − k) · (n − k − 1) · … · 2 · 1

Notice the part we *want* (the first k factors) is:

n · (n − 1) · … · (n − k + 1)

The “extra tail” we don’t want is:

(n − k) · (n − k − 1) · … · 1 = (n − k)!

So divide to cancel the tail:

n P k = \( \frac{n!}{(n − k)!} \)

### Check with a concrete example

Suppose n = 5 and k = 3.

Direct product:

5 P 3 = 5 · 4 · 3 = 60

Factorial form:

5!/(5 − 3)! = 5!/2! = (120)/2 = 60

Matches.

### Boundary cases and sanity checks

- •If k = n, then:

n P n = n!/(n − n)! = n!/0! = n!/1 = n!

So k-permutation generalizes full permutation.

- •If k = 0, then:

n P 0 = n!/(n − 0)! = n!/n! = 1

There is exactly one sequence of length 0: the empty sequence.

- •If k > n, then there are 0 ways (you can’t pick more distinct items than exist). In formula form, (n − k)! isn’t defined for negative integers in this counting context, so treat it as “not allowed.”

### A decision table: permutations vs other counts

Use this to avoid the most common confusion.

| Situation | Replacement? | Order matters? | Tool |
| --- | --- | --- | --- |
| Arrange all n distinct items | No | Yes | n! |
| Choose and order k from n | No | Yes | n P k = n!/(n−k)! |
| Choose k from n (order irrelevant) | No | No | (This is combinations; unlocked next) |
| Choose with repeats allowed | Yes | Depends | Different formulas (not this node) |

### Interpreting n P k as “pick then arrange”

Another way to see the structure:

- •First you select which k items you’ll use.
- •Then you arrange them.

That viewpoint leads naturally to combinations later:

n P k = (number of k-element sets) · (number of ways to order k items)

And “number of ways to order k items” is k!.

So you’ll soon see the relationship:

n P k = (n C k) · k!

Don’t worry about n C k yet—just remember: permutations count **ordered** outcomes; combinations will count **unordered** ones.

## Application/Connection: Modeling Real Problems and Linking to Combinations

### Turning words into n, k, and “order?”

Most permutation mistakes come from translating the story incorrectly. A reliable workflow:

1. 1)**Identify positions**: Are there labeled roles (1st/2nd/3rd, seat 1/2/3, President/Vice/etc.)?
2. 2)**Check uniqueness**: Can an item/person be used more than once?
3. 3)**Extract n and k**:

- •n = size of available pool
- •k = number of positions filled

4. 4)If no repeats and order matters → use n P k.

### Example application types

#### 1) Rankings and awards

If 10 runners compete and you award gold/silver/bronze, you’re filling 3 distinct ranks:

10 P 3 = 10 · 9 · 8

#### 2) Assigning distinct roles

If you pick a chair, secretary, and treasurer from 12 people:

12 P 3

#### 3) Seating in a row

If 7 people sit in a row of 7 seats:

7!

If only 4 of them sit (4 seats to fill) from 7 people:

7 P 4

### A key conceptual bridge to combinations

Often the only difference between a permutation problem and a combination problem is whether we care about the order.

Take the same three winners from 10 runners:

- •If we only care **which 3** runners win medals (no order): that’s a combinations question.
- •If we care who is gold vs silver vs bronze: that’s permutations.

The relationship:

n P k = (n C k) · k!

Interpretation:

- •n C k chooses the group.
- •k! orders the chosen group into k distinct positions.

### Why permutations are foundational in discrete math and CS

Permutations aren’t just a counting trick.

- •In algorithms, a brute-force search over all arrangements is often “try all permutations,” which can mean n! possibilities—explaining why some problems become infeasible quickly.
- •In probability, many probabilities are “favorable permutations / total permutations.”
- •In data structures, sorting can be seen as transforming one permutation of items into another.

### Quick growth intuition (why pacing matters)

Factorials explode:

| n | n! |
| --- | --- |
| 5 | 120 |
| 8 | 40,320 |
| 10 | 3,628,800 |
| 15 | 1,307,674,368,000 |

So, whenever you see n! or n P k, it’s worth pausing to ask: is the model correct? Are repeats allowed? Are we accidentally counting the same outcome multiple times?

That careful translation skill is the main thing this node is training.

## Worked Examples (3)

### Example 1: Podium finishes (order matters)

A race has 9 runners. How many ways can gold, silver, and bronze be awarded (no ties)?

1. Identify positions: gold, silver, bronze are 3 distinct ranks ⇒ order matters.
2. No runner can take two medals ⇒ without replacement.
3. Set n = 9, k = 3.
4. Use k-permutations: 9 P 3 = 9 · 8 · 7.
5. Compute:

   9 · 8 · 7 = 72 · 7 = 504.

**Insight:** Any time roles are labeled (1st/2nd/3rd), you’re arranging people into positions, so permutations apply.

### Example 2: Arrange all items (factorial)

How many different orders can 6 distinct books be placed on a shelf?

1. All 6 books are used, and left-to-right order matters.
2. This is a full permutation of n = 6 distinct items.
3. Use factorial: 6! = 6 · 5 · 4 · 3 · 2 · 1.
4. Compute stepwise:

   6 · 5 = 30

   30 · 4 = 120

   120 · 3 = 360

   360 · 2 = 720

   720 · 1 = 720.

**Insight:** When you arrange all n distinct items, the count is exactly the product of remaining choices at each position: n!.

### Example 3: Using the factorial form to compute quickly

Compute 12 P 5 and simplify using factorial cancellation.

1. Use the formula: 12 P 5 = 12!/(12 − 5)! = 12!/7!.
2. Expand only what’s needed:

   12! = 12 · 11 · 10 · 9 · 8 · 7!

   7! = 7!
3. Cancel 7!:

   12!/7! = 12 · 11 · 10 · 9 · 8.
4. Multiply:

   12 · 11 = 132

   132 · 10 = 1320

   1320 · 9 = 11880

   11880 · 8 = 95040.

**Insight:** Factorial form is less about computing gigantic factorials and more about cancellation—expand just enough to cancel (n−k)!.

## Key Takeaways

- ✓

  A permutation counts **ordered** outcomes: swapping items creates a new result.
- ✓

  Full permutations of n distinct items: n! = 1 · 2 · … · n, with 0! = 1.
- ✓

  k-permutations (ordered selections without replacement): n P k = n · (n − 1) · … · (n − k + 1).
- ✓

  Equivalent compact form: n P k = n!/(n − k)! (use cancellation to compute).
- ✓

  Sanity checks: n P n = n!, and n P 0 = 1.
- ✓

  Translate word problems by identifying labeled positions (roles/ranks/seats) and whether repeats are allowed.
- ✓

  Permutations connect to combinations via: n P k = (n C k) · k! (order = group × arrangements).

## Common Mistakes

- ✗

  Treating an unordered selection as ordered (using n P k when order doesn’t matter).
- ✗

  Forgetting “without replacement” and accidentally allowing repeats in the count.
- ✗

  Computing n! and (n−k)! separately instead of canceling first, leading to huge numbers or arithmetic errors.
- ✗

  Mixing up k and n (e.g., using k P n) or allowing k > n without noticing the model is impossible.

## Practice

easy

A club has 11 members. In how many ways can it choose a president, vice president, and secretary (three different people)?

**Hint:** These are 3 distinct roles, so order matters. No person can hold two roles.

Show solution

n = 11, k = 3.

11 P 3 = 11 · 10 · 9 = 990.

medium

How many 4-letter sequences can you form from the letters {A, B, C, D, E, F} if no letter can repeat?

**Hint:** You are filling 4 positions from 6 distinct letters without replacement.

Show solution

n = 6, k = 4.

6 P 4 = 6 · 5 · 4 · 3 = 360.

(Equivalently, 6!/2! = 720/2 = 360.)

hard

Simplify and compute: 15 P 6.

**Hint:** Write 15 P 6 = 15!/9! and expand only down to 10.

Show solution

15 P 6 = 15!/9!.

15! = 15 · 14 · 13 · 12 · 11 · 10 · 9!

So 15!/9! = 15 · 14 · 13 · 12 · 11 · 10.

Compute:

15 · 14 = 210

210 · 13 = 2730

2730 · 12 = 32760

32760 · 11 = 360360

360360 · 10 = 3,603,600.

## Connections

Next node: [Combinations](/tech-tree/combinations/)

Related ideas you’ll likely use soon:

- •Relationship: n P k = (n C k) · k!
- •Probability setups often use permutations for ordered sample spaces.
- •Algorithmic complexity: iterating over all permutations can be O(n!).

Quality: A (4.5/5)

[← back to tree](/tech-tree/)[browse all →](/tech-tree/inventory/)
