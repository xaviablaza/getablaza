---
title: Pigeonhole Principle
description: If n+1 items in n boxes, at least one box has 2+ items.
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
inspiration_url: https://templeton.host/tech-tree/pigeonhole-principle/
inspiration_category: tech-tree
---

> Source-copy draft imported from [https://templeton.host/tech-tree/pigeonhole-principle/](https://templeton.host/tech-tree/pigeonhole-principle/). Names, domain references, and local media paths were adapted for Xavi Ablaza / getablaza.com.

[←Back to Tech Tree](/tech-tree/)

[inventory](/tech-tree/inventory/)[coverage](/tech-tree/coverage/)

# Pigeonhole Principle

Discrete MathDifficulty: ★★★☆☆Depth: 2Unlocks: 0

If n+1 items in n boxes, at least one box has 2+ items.

## Interactive Visualization

⏮◀◀▶▶STEP0.25x1xZOOM

t=0s

## Core Concepts

- -Finite discrete items and finite discrete boxes
- -Assignment mapping: each item is placed into exactly one box
- -Comparing cardinalities: counting items and counting boxes (integer comparison)

## Key Symbols & Notation

n (number of boxes, positive integer)m (number of items, nonnegative integer)

## Essential Relationships

- -If m > n (more items than boxes) then at least one box contains two or more items (pigeonhole implication)

## Prerequisites (1)

[Proof Techniques5 atoms](/tech-tree/proof-techniques/)

Advanced Learning Details

### Graph Position

16

Depth Cost

0

Fan-Out (ROI)

0

Bottleneck Score

2

Chain Length

### Cognitive Load

6

Atomic Elements

22

Total Elements

L0

Percentile Level

L4

Atomic Level

### All Concepts (9)

- - Basic pigeonhole principle: if n+1 items are placed into n boxes then at least one box contains at least two items
- - Generalized pigeonhole principle: if N items are placed into k boxes then at least one box contains at least ceil(N/k) items
- - Pigeons vs. pigeonholes modeling: treating 'items' as pigeons and 'boxes' as pigeonholes to reason about distributions
- - Collision/duplicate existence: the idea that two distinct items can share the same box (a guaranteed collision when items > boxes)
- - Function/mapping viewpoint: representing a placement as a function f: Items → Boxes
- - Injectivity impossibility for finite sets: when |Items| > |Boxes|, no injective (one-to-one) mapping from Items to Boxes exists
- - Average-occupancy argument: computing mean occupancy (N/k) and using it to infer a lower bound on the maximum occupancy
- - Tightness/optimality of the bound: the lower bound ⌈N/k⌉ is attainable (there exist distributions that achieve it)
- - Contrapositive form of the principle: if no box has ≥2 items, then the number of items ≤ number of boxes

### Teaching Strategy

Deep-dive lesson - accessible entry point but dense material. Use worked examples and spaced repetition.

You don’t need probability, algebra, or heavy machinery to prove some surprisingly strong statements—sometimes a simple counting mismatch forces a guaranteed collision. The pigeonhole principle is the canonical example: if you try to squeeze “too many” items into “too few” boxes, at least one box must get crowded.

TL;DR:

Model a situation as a function f: Items → Boxes where each item goes to exactly one box. If there are more items than boxes, then f cannot be one-to-one, so ∃ a box containing ≥ 2 items. More generally, with m items and n boxes, some box has at least ⌈m/n⌉ items.

## What Is the Pigeonhole Principle?

### Why this idea exists

In discrete math, many problems look complicated because they describe real-world objects (people, socks, birthdays, edges in a graph, remainders mod n) rather than clean numbers. The pigeonhole principle is a **translation tool**: it turns a messy statement into a statement about counting.

The core motivation is simple:

- •If you have **more items than boxes**, and
- •Each item is placed into **exactly one** box,

then crowding is unavoidable.

This is not about “likely” outcomes; it’s a **certainty**.

### Informal statement

> If n + 1 items are placed into n boxes, then at least one box contains at least 2 items.

Here:

- •“items” are the things being assigned (people, numbers, socks, emails, graph vertices, …)
- •“boxes” are the categories/groups you place them into (months, remainders, colors, bins, …)

### The function view (the real engine)

A clean way to express “each item goes to exactly one box” is with a function.

Let:

- •I be a finite set of items, |I| = m
- •B be a finite set of boxes, |B| = n
- •f: I → B be an assignment rule

Then for each item i ∈ I, f(i) is the box it goes into.

If m > n, then f cannot be injective (one-to-one). That means:

∃ i₁, i₂ ∈ I with i₁ ≠ i₂ and f(i₁) = f(i₂)

That equality means two distinct items land in the same box: a collision.

### Formal statement (basic version)

If m > n and f: I → B, then ∃ b ∈ B such that |f⁻¹({b})| ≥ 2.

This reads: there exists a box b whose preimage has at least 2 items.

### Why it’s so useful

Pigeonhole arguments are powerful because they:

1. 1)Replace a complicated structure with a **counting invariant** (how many boxes exist?)
2. 2)Often give you an **existence proof** with minimal detail
3. 3)Combine well with contradiction (assume no box is crowded, then count maximum items)

In many contest and interview settings, the hardest part is not the counting—it’s choosing the right “boxes.” That design choice is the art of pigeonhole proofs.

## Core Mechanic 1: The Basic Pigeonhole Principle (n + 1 into n)

### Why this mechanic matters

The simplest pigeonhole principle is the seed from which most applications grow. If you can recognize a situation where “more than n items are forced into n categories,” you immediately get a guaranteed repetition.

### Statement

If n + 1 items are placed into n boxes, then at least one box contains at least 2 items.

### Proof (by contradiction, counted carefully)

Assume for contradiction that **no** box contains ≥ 2 items. Then every box contains at most 1 item.

If there are n boxes, the **maximum** number of items you could place is:

1 + 1 + … + 1 (n times) = n

But we are told there are n + 1 items. So we get:

n + 1 ≤ n

which is impossible.

Therefore, the assumption was false, so at least one box contains ≥ 2 items.

### The “design step”: what counts as a box?

In practice, the statement “items” and “boxes” is metaphorical. You decide what they are.

Common choices for boxes:

- •**Remainders mod n**: boxes are 0, 1, …, n − 1
- •**Months**: 12 boxes
- •**Days of week**: 7 boxes
- •**Intervals**: split a number line into n disjoint ranges
- •**Graph neighborhoods**: boxes as adjacency patterns

What makes a good box choice?

- •Every item must map to exactly one box
- •Number of boxes should be easy to count
- •Being in the same box should imply the property you want (same remainder ⇒ difference divisible by n)

### A quick comparison of viewpoints

| Viewpoint | What you track | What you conclude | When it helps |
| --- | --- | --- | --- |
| “Physical bins” | literal distribution | some bin has ≥ 2 | intuitive starts |
| Function f: Items → Boxes | injective vs not | collision f(i₁)=f(i₂) | clean proofs |
| Counting upper bound | max items with constraint | contradiction | many olympiad proofs |

### Breathing room: what it does *not* say

It does **not** tell you:

- •which box is crowded
- •how many boxes are crowded
- •whether there are 2 items or 200 items in that box

It only guarantees **existence**.

This is a feature: you often only need “there exists …” to finish a proof.

## Core Mechanic 2: The Generalized Pigeonhole Principle (⌈m/n⌉)

### Why generalize?

The basic version answers: “if m = n + 1, then some box has 2.”

But many problems naturally have:

- •m items
- •n boxes

and you want a guaranteed **minimum crowding level**. The generalized pigeonhole principle gives a tight bound.

### Statement (generalized)

If m items are placed into n boxes, then at least one box contains at least ⌈m/n⌉ items.

Here ⌈x⌉ is the ceiling function: the smallest integer ≥ x.

### Intuition: average forces a maximum

If you spread m items as evenly as possible over n boxes, you aim for about m/n items per box.

- •If m divides n nicely, you can make each box have exactly m/n.
- •If not, some boxes must have one extra.

So the **maximum** load is at least the ceiling of the average.

### Proof (by contradiction using an upper bound)

Assume for contradiction that every box contains at most ⌈m/n⌉ − 1 items.

Then the total number of items is at most:

n(⌈m/n⌉ − 1)

We now show this is < m.

Because ⌈m/n⌉ is the smallest integer ≥ m/n, we know:

⌈m/n⌉ − 1 < m/n

Multiply both sides by n (note n > 0):

n(⌈m/n⌉ − 1) < m

So under our assumption, total items < m, contradicting that there are m items.

Therefore, at least one box has ≥ ⌈m/n⌉ items.

### Tightness (why the ceiling is the best possible)

You can’t generally guarantee more than ⌈m/n⌉.

Example: m = 10, n = 3.

- •⌈10/3⌉ = 4.

You can distribute as 4, 3, 3.

No box has 5, so “≥ 5” would be false as a guarantee. Thus ⌈m/n⌉ is the correct bound.

### A useful rearrangement: if each box has ≤ k, then m ≤ nk

This is the contrapositive style you’ll use constantly:

If every box has at most k items, then total items m is at most nk.

So if you ever have m > nk, you can instantly conclude:

∃ a box with ≥ k + 1 items.

That is often the quickest way to set up a problem.

### Two patterns to internalize

1) **Force a collision**

- •Choose n boxes
- •Show you have n + 1 items
- •Conclude two items share a box

2) **Force a heavy box**

- •Choose n boxes
- •Count m items
- •Conclude some box has at least ⌈m/n⌉ items

Both are the same idea; they just target different conclusions.

## Application/Connection: How to Use It in Proofs (Remainders, Geometry, Graphs, and Existence)

### Why applications feel “magical”

A good pigeonhole proof often looks like a trick because it introduces a category system (the boxes) that wasn’t explicitly in the problem statement. Once you see that category system, the rest is mechanical.

So the practical skill is: **choose boxes so that sharing a box implies the property you want**.

Below are several common application templates.

---

## 1) Remainders mod n (number theory template)

### Why it works

Remainders partition integers into exactly n boxes:

0, 1, 2, …, n − 1

If two integers land in the same remainder box, their difference is divisible by n.

Formally: if a ≡ b (mod n), then n ∣ (a − b).

### Typical use

To prove: “Among many integers, two differ by a multiple of n.”

- •Items: the integers
- •Boxes: their remainders mod n
- •Conclusion: two share a remainder ⇒ difference divisible by n

---

## 2) Intervals (geometry/analysis-flavored template)

### Why it works

If you split a range into n disjoint intervals (“boxes”), any set of n + 1 points must place two points into the same interval.

Then you get a bound on distance.

Example pattern:

- •Range length L
- •Split into n intervals of length L/n
- •Two points in same interval ⇒ distance ≤ L/n

This is a deterministic cousin of “points are dense somewhere.”

---

## 3) Subsets and binary strings (combinatorics template)

### Why it works

A set of size k has 2ᵏ subsets. If you can map objects into these subsets (or into bit patterns), you can count boxes via powers of 2.

Common box counts:

- •binary strings of length k: 2ᵏ
- •subsets of {1,…,k}: 2ᵏ

This is often used to force two objects to share a pattern.

---

## 4) Graphs (discrete structure template)

### Why it works

In graphs, you often classify vertices by some discrete feature:

- •degree
- •neighborhood intersection
- •color in a coloring

Then pigeonhole yields repeated degrees, repeated colors, or a crowded color class.

Classic quick example: In any simple graph on n ≥ 2 vertices, two vertices have the same degree.

- •Possible degrees are 0, 1, …, n − 1 (n possibilities)
- •But degrees 0 and n − 1 cannot both occur (if someone is connected to everyone, nobody is isolated)
- •So there are at most n − 1 possible degrees
- •With n vertices (items) into n − 1 degree-values (boxes), some degree repeats

Notice how the key is not just counting boxes, but sometimes tightening the box count (n − 1 instead of n).

---

## A step-by-step recipe (what to do when stuck)

1) **Identify the objects you can count** (potential items).

2) **Invent a classification** that is:

- •exhaustive (every item fits)
- •exclusive (one item → one box)

3) **Count boxes**.

4) **Compare counts** (m vs n, or m vs nk).

5) **Translate the collision/crowding back** into the problem’s language.

---

## When to suspect pigeonhole

You should reach for pigeonhole when you see phrases like:

- •“At least two … have the same …”
- •“Show there exist i ≠ j such that …”
- •“Prove some difference is divisible by n” (remainders)
- •“No matter how you choose …” (adversarial / worst-case)
- •“Among many objects, show a repetition/overlap”

Pigeonhole is one of the fastest ways to turn “no matter how” into a proof.

## Worked Examples (3)

### Example 1: Two integers differ by a multiple of n (remainders mod n)

Let n be a positive integer. Given n + 1 integers a₁, a₂, …, aₙ₊₁, prove that there exist i ≠ j such that aᵢ − aⱼ is divisible by n.

1. Define the boxes as the possible remainders modulo n:

   B = {0, 1, 2, …, n − 1}.

   There are n boxes.
2. For each integer a\_k, compute its remainder r\_k where

   r\_k ≡ a\_k (mod n) and r\_k ∈ B.

   This assigns each item a\_k to exactly one box r\_k.
3. We have n + 1 items (the integers) and n boxes (remainders). By the pigeonhole principle, ∃ i ≠ j such that r\_i = r\_j.
4. Translate “same remainder” back into divisibility:

   r\_i = r\_j ⇒ a\_i ≡ a\_j (mod n)

   ⇒ n ∣ (a\_i − a\_j).

**Insight:** The entire proof is: many integers → few remainders. The “box design” (remainders) is what makes the collision meaningful, because equal remainders are exactly the condition for a difference to be divisible by n.

### Example 2: Generalized version—some month has many birthdays

In a group of 100 people, prove that there is a month in which at least 9 of them have birthdays (ignore leap day issues).

1. Choose boxes: the 12 months of the year. So n = 12.
2. Choose items: the 100 people. So m = 100.
3. Apply the generalized pigeonhole principle:

   Some month has at least ⌈m/n⌉ = ⌈100/12⌉ people with birthdays in that month.
4. Compute the ceiling carefully:

   100/12 ≈ 8.333...

   ⌈100/12⌉ = 9.
5. Conclude: ∃ a month with ≥ 9 birthdays in the group.

**Insight:** The ceiling ⌈m/n⌉ is the formal version of “at least the average, rounded up.” Even if birthdays were adversarially arranged, you can’t keep every month at 8 or fewer because 12·8 = 96 < 100.

### Example 3: Two points are close (interval pigeonhole)

Pick 11 real numbers in the interval [0, 1]. Prove that there exist two of them whose distance is at most 0.1.

1. Design boxes by partitioning [0, 1] into 10 disjoint subintervals of equal length 0.1:

   [0, 0.1), [0.1, 0.2), …, [0.9, 1].

   There are n = 10 boxes.
2. The 11 real numbers are the items, so m = 11.
3. By the pigeonhole principle (11 items into 10 boxes), two of the chosen numbers, call them x and y, lie in the same subinterval.
4. Any two numbers in the same subinterval of length 0.1 differ by at most 0.1:

   If x, y ∈ [k/10, (k+1)/10), then

   |x − y| ≤ (k+1)/10 − k/10 = 0.1.
5. Conclude ∃ x ≠ y with |x − y| ≤ 0.1.

**Insight:** Intervals act like “continuous-looking” pigeonholes. The key is choosing the number of intervals so that ‘same interval’ implies the distance bound you want.

## Key Takeaways

- ✓

  Pigeonhole principle is a counting inevitability: too many items forced into too few boxes ⇒ a collision or crowding exists.
- ✓

  Model assignments as a function f: Items → Boxes; if |Items| > |Boxes| then f is not injective, so ∃ two items in the same box.
- ✓

  Generalized form: with m items and n boxes, some box has at least ⌈m/n⌉ items.
- ✓

  A common contrapositive style: if every box has ≤ k items, then total items m ≤ nk; therefore if m > nk, some box has ≥ k + 1.
- ✓

  Most of the difficulty is choosing the right boxes so that “same box” implies a useful shared property (same remainder, same interval, same category).
- ✓

  Pigeonhole is deterministic (guaranteed), not probabilistic (likely).
- ✓

  It often pairs naturally with proof by contradiction: assume no box is crowded, compute a maximum total, and contradict the given count.

## Common Mistakes

- ✗

  Choosing boxes that are not mutually exclusive (an item could belong to multiple boxes) or not exhaustive (some item fits no box), breaking the function/assignment model.
- ✗

  Forgetting the ceiling in the generalized principle (using m/n instead of ⌈m/n⌉), which can make the bound wrong by 1.
- ✗

  Counting the number of boxes incorrectly (e.g., using n possible degrees in a graph when one degree value is impossible, or double-counting intervals with overlapping endpoints).
- ✗

  Concluding more than pigeonhole guarantees (e.g., claiming two collisions, or identifying which box is crowded) without additional argument.

## Practice

easy

Show that among any 13 integers, there exist two whose difference is divisible by 12.

**Hint:** Use remainders modulo 12 as boxes.

Show solution

Let the 12 boxes be the remainders {0,1,…,11} modulo 12. Each of the 13 integers has exactly one remainder, so we assign each integer to one box. With 13 items and 12 boxes, pigeonhole implies two integers a and b share a remainder: a ≡ b (mod 12). Therefore 12 ∣ (a − b).

medium

You choose 51 numbers from the set {1, 2, …, 100}. Prove that at least one chosen pair sums to 101.

**Hint:** Design boxes as complementary pairs (1,100), (2,99), …

Show solution

Partition {1,…,100} into 50 boxes, each box a complementary pair that sums to 101:

{1,100}, {2,99}, …, {50,51}.

There are n = 50 boxes. Selecting 51 numbers means m = 51 items. By pigeonhole, some box contains at least 2 chosen numbers. But each box has exactly 2 numbers and they sum to 101, so at least one chosen pair sums to 101.

hard

In any simple graph with 6 vertices, prove that there exist two vertices with the same degree.

**Hint:** Possible degrees are 0 through 5, but not all can occur simultaneously. Tighten the box count.

Show solution

Each vertex has degree in {0,1,2,3,4,5}. However, a graph cannot have both a vertex of degree 0 and a vertex of degree 5: if some vertex is connected to all others (degree 5), then no vertex is isolated (degree 0). So the set of degrees that can appear has size at most 5 (either exclude 0 or exclude 5). Thus we have 6 vertices (items) assigned to at most 5 degree-values (boxes). By pigeonhole, at least two vertices share the same degree.

## Connections

Related nodes:

- •[Proof by Contradiction](/tech-tree/proof-by-contradiction/)
- •[Modular Arithmetic (Congruences)](/tech-tree/modular-arithmetic/)
- •[Counting Principles (Sum/Product Rules)](/tech-tree/counting-principles/)
- •[Graph Basics: Degrees and Handshaking Lemma](/tech-tree/graph-degrees-handshaking/)
- •[Ceiling and Floor Functions](/tech-tree/ceiling-floor/)

Quality: A (4.6/5)

[← back to tree](/tech-tree/)[browse all →](/tech-tree/inventory/)
