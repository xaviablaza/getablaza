---
title: Combinations
description: Unordered selections. nCr (binomial coefficients).
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
inspiration_url: https://templeton.host/tech-tree/combinations/
inspiration_category: tech-tree
---

> Source-copy draft imported from [https://templeton.host/tech-tree/combinations/](https://templeton.host/tech-tree/combinations/). Names, domain references, and local media paths were adapted for Xavi Ablaza / getablaza.com.

[←Back to Tech Tree](/tech-tree/)

[inventory](/tech-tree/inventory/)[coverage](/tech-tree/coverage/)

# Combinations

Discrete MathDifficulty: ★★☆☆☆Depth: 2Unlocks: 0

Unordered selections. nCr (binomial coefficients).

## Interactive Visualization

⏮◀◀▶▶STEP0.25x1xZOOM

t=0s

## Core Concepts

- -Unordered selection (order irrelevant)
- -Selection without repetition (each item used at most once)
- -k-subset of an n-element set (choose exactly k distinct elements from n)

## Key Symbols & Notation

C(n,k) - the "n choose k" binomial coefficient

## Essential Relationships

- -Binomial coefficient formula: C(n,k) = n! / (k! (n-k)!)
- -Relation to permutations: C(n,k) = P(n,k) / k! (combinations = k-permutations divided by k!)

## Prerequisites (1)

[Permutations6 atoms](/tech-tree/permutations/)

Advanced Learning Details

### Graph Position

18

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

16

Total Elements

L0

Percentile Level

L4

Atomic Level

### All Concepts (6)

- - Unordered selection (combination): selecting r items from n where order does not matter
- - Combination as an r-element subset of an n-element set (combinatorial interpretation)
- - Combination formula (closed form): nCr = n! / (r! (n - r)!)
- - Counting by equivalence classes: each combination corresponds to r! ordered permutations, so orderings are collapsed
- - Domain and edge cases for combinations: defined for integer 0 ≤ r ≤ n (C(n,0)=C(n,n)=1) and convention C(n,r)=0 for r>n
- - Binomial coefficient values are nonnegative integers (integrality of combinations)

### Teaching Strategy

Deep-dive lesson - accessible entry point but dense material. Use worked examples and spaced repetition.

How many different 3-person teams can you make from 10 people? If you list “A, B, C” and later list “C, B, A”, did you count a new team—or the same team again? Combinations are the math of “teams, not lineups.”

TL;DR:

A combination counts unordered selections of k distinct items from n distinct items. The binomial coefficient is

C(n,k) = n! / (k!(n−k)!).

It connects directly to permutations by “divide out the internal order”: C(n,k) = nP k / k!. Also, C(n,k) = C(n,n−k).

## What Is a Combination?

### Why you need a new counting tool (motivation)

In permutations, order matters. If you arrange books on a shelf, “A then B” is different from “B then A.” But many real questions aren’t about order:

- •picking a committee
- •choosing toppings on a pizza
- •selecting which features to include in a release
- •choosing k cards from a deck (ignoring the order you drew them)

In these situations, **the selection is what matters**, not the sequence.

A classic symptom that you need combinations: you can easily list multiple “different” answers that are actually the same outcome because they contain the same elements.

### Definition

A **combination** is an **unordered selection** of **k distinct** elements from a set of **n distinct** elements.

- •“unordered” means {A, B, C} is the same as {C, B, A}
- •“distinct” means no repetition (each item used at most once)
- •“exactly k” means you choose a subset of size k

We denote the number of such selections by the binomial coefficient:

- •**C(n,k)** or **(n choose k)**

Read as: “n choose k.”

### Intuition: combinations are k-subsets

If S is a set with |S| = n, then a combination corresponds to picking a **k-subset** T ⊂ S such that |T| = k.

So the counting question becomes:

> How many k-subsets does an n-element set have?

That number is C(n,k).

### Boundary cases (sanity checks)

These help you detect mistakes later.

- •C(n,0) = 1 (there’s exactly one way to choose nothing: the empty set ∅)
- •C(n,n) = 1 (choose everything)
- •C(n,1) = n (choose any one element)
- •C(n,k) = 0 if k > n (you can’t choose 5 distinct items from 3 items)

These are not special tricks—they fall naturally out of the definition.

## Core Mechanic 1: From Permutations to Combinations (Divide by k!)

### Why this works (the key idea)

You already know permutations: the number of ordered selections of k distinct items from n is

- •nP k = n! / (n−k)!

But for combinations, **order is irrelevant**. A single team of k people can be arranged internally in k! different orders.

So if you:

1) count ordered selections (permutations)

2) then collapse all sequences that represent the same set

…you should divide by the number of internal reorderings, which is k!.

That’s the whole bridge:

> combinations = permutations ÷ (ways to reorder the chosen items)

### Derivation (showing the work)

Start with permutations:

nP k = n! / (n−k)!

Each unique k-element set corresponds to exactly k! permutations (all possible orderings of those k items). Therefore:

C(n,k) = (nP k) / k!

Now substitute the formula for nP k:

C(n,k) = (n! / (n−k)!) / k!

Rewrite as a single fraction:

C(n,k) = n! / (k!(n−k)!)

This is the standard closed form.

### What the factorials are “doing”

It’s easy to memorize the formula and still misunderstand it. Here’s the meaning:

- •n! counts all orderings of all n items
- •dividing by (n−k)! removes orderings of the items you did **not** pick
- •dividing by k! removes orderings among the items you **did** pick (because order doesn’t matter)

### Quick comparison table

| Question type | Sample question | Order matters? | Repetition allowed? | Formula |
| --- | --- | --- | --- | --- |
| Permutation (k from n) | “Who gets gold/silver/bronze?” | Yes | No | nP k = n!/(n−k)! |
| Combination (k from n) | “Which 3 people are on the team?” | No | No | C(n,k) = n!/(k!(n−k)!) |

### When *not* to use this formula

This node is about **selection without repetition** (each item used at most once). If repetition is allowed (“choose 3 scoops, flavors may repeat”), that’s a different tool (often called combinations with repetition / stars and bars).

Staying disciplined about the assumptions is half of discrete math.

## Core Mechanic 2: Properties You Can Use to Think Faster

### Why properties matter

Even if you can compute C(n,k) with a calculator, properties help you:

- •simplify expressions without huge factorials
- •check if an answer is plausible
- •connect combinations to probability and algebra later

We’ll focus on three high-value properties.

---

## 1) Symmetry: C(n,k) = C(n,n−k)

### Intuition

Choosing k items to include is equivalent to choosing n−k items to exclude.

Example: “Choose 2 students to be captains” out of 10 is the same as “choose 8 students to not be captains.”

### Algebraic proof (showing the work)

Start with the formula:

C(n,k) = n! / (k!(n−k)!)

Swap k with n−k:

C(n,n−k) = n! / ((n−k)! (n−(n−k))!)

Simplify the last factorial:

n−(n−k) = k

So:

C(n,n−k) = n! / ((n−k)! k!)

That equals C(n,k) since multiplication is commutative:

C(n,k) = C(n,n−k)

---

## 2) Multiplicative ratio (useful for simplification)

A very practical identity is:

C(n,k) = n(n−1)…(n−k+1) / k!

This comes from expanding n!/(n−k)!:

n!/(n−k)! = n(n−1)(n−2)…(n−k+1)

So:

C(n,k) = [n(n−1)…(n−k+1)] / k!

Why you care: it avoids gigantic factorials and makes cancellation easier.

Example pattern: compute C(100,3) without writing 100!.

---

## 3) Pascal’s Identity: C(n,k) = C(n−1,k) + C(n−1,k−1)

### Why it’s true (combinatorial reasoning)

Take an n-element set and pick a particular “special” element x.

Count k-subsets in two disjoint cases:

1) subsets that **do not include** x

- •then you must choose all k elements from the remaining n−1
- •count: C(n−1,k)

2) subsets that **do include** x

- •you already took x, so choose the remaining k−1 elements from the remaining n−1
- •count: C(n−1,k−1)

Add the cases:

C(n,k) = C(n−1,k) + C(n−1,k−1)

### What it gives you

This identity generates Pascal’s Triangle and is the backbone of many proofs in probability and algebra.

---

### Mini-sanity checks using these properties

- •Symmetry implies C(10,2) = C(10,8). If your computations don’t match, something is wrong.
- •Pascal’s identity implies C(5,2) should equal C(4,2)+C(4,1) = 6+4 = 10.

These are quick “unit tests” for your counting.

## Application/Connection: Where Combinations Show Up (and Why You’ll Keep Seeing Them)

### 1) Counting subsets and search spaces

In CS, combinations appear whenever you have to consider subsets:

- •feature selection (choose k features out of n)
- •choosing a set of servers for a shard
- •selecting k test cases out of a suite

The number of possibilities often grows quickly. Knowing that the count is C(n,k) helps you reason about feasibility.

Example: even with moderate n, C(n,k) can be huge, which hints that brute force might be impossible.

### 2) Probability (preview)

Many probabilities are “favorable combinations ÷ total combinations.”

For instance, in card problems, the *order of the hand doesn’t matter*, so combinations are the natural denominator.

You’ll later see expressions like:

P(event) = C(favorable, k) / C(total, k)

### 3) Binomial coefficients and algebra (preview)

The name “binomial coefficient” comes from the Binomial Theorem, where coefficients are combinations:

(x + y)ⁿ = ∑ₖ₌₀ⁿ C(n,k) xᵏ yⁿ⁻ᵏ

You don’t need to master this now, but it explains why C(n,k) is so central: it connects counting to polynomial expansion.

### 4) Relationship to vectors (light connection)

In linear algebra and ML, you’ll sometimes represent a chosen subset using a 0–1 indicator vector **v** ∈ {0,1}ⁿ with exactly k ones.

Each such **v** corresponds to a k-subset, and the number of these vectors is exactly C(n,k).

This is a quiet but powerful bridge: combinations count the number of “k-hot” binary vectors.

### A decision checklist

Before you compute anything, ask:

1) Am I selecting items or arranging them?

- •arranging ⇒ permutations
- •selecting ⇒ keep going

2) Does order matter in the final outcome?

- •yes ⇒ permutations
- •no ⇒ combinations

3) Is repetition allowed?

- •no ⇒ this node’s C(n,k)
- •yes ⇒ different tool (combinations with repetition)

Getting these questions right is more important than memorizing the formula.

## Worked Examples (3)

### Committees: Choose 3 people from 10

A club has 10 members. How many distinct 3-person committees can be formed (no roles, just a set of people)?

1. Recognize this is a selection problem, not an arrangement: committee membership is unordered.
2. Identify n = 10 and k = 3.
3. Use the combinations formula:

   C(10,3) = 10! / (3!(10−3)!)
4. Compute step by step:

   10!/(7!) = 10·9·8

   So C(10,3) = (10·9·8) / 3!
5. Compute 3! = 6.
6. Divide:

   (10·9·8)/6 = 720/6 = 120
7. Final answer: 120 committees.

**Insight:** If you mistakenly used permutations 10P3 = 720, you’d be counting each committee 3! = 6 times (all internal reorderings). Dividing by 6 fixes it.

### Symmetry: Choose 8 out of 10 without heavy arithmetic

How many ways are there to choose 8 distinct items from 10 distinct items?

1. Direct computation would be:

   C(10,8) = 10! / (8!2!)
2. Use symmetry:

   C(10,8) = C(10,10−8) = C(10,2)
3. Now compute the smaller one:

   C(10,2) = 10! / (2!8!)
4. Simplify:

   10!/8! = 10·9
5. So:

   C(10,2) = (10·9)/2 = 90/2 = 45
6. Final answer: 45 ways.

**Insight:** When k is close to n, symmetry turns a hard-looking factorial into a small calculation. Always check whether k or n−k is smaller.

### Counting hands: Choose 5 cards from a 52-card deck

How many distinct 5-card hands can be dealt from a standard 52-card deck (order irrelevant)?

1. A hand is an unordered set of cards, so use combinations with n = 52, k = 5.
2. Write the formula:

   C(52,5) = 52! / (5!47!)
3. Avoid huge factorials by canceling:

   52!/47! = 52·51·50·49·48
4. So:

   C(52,5) = (52·51·50·49·48) / 5!
5. Compute 5! = 120.
6. Compute numerator in manageable steps:

   52·51 = 2652

   50·49·48 = 50·2352 = 117600

   So numerator = 2652·117600
7. Multiply:

   2652·117600 = 311,875,200
8. Divide by 120:

   311,875,200 / 120 = 2,598,960
9. Final answer: 2,598,960 distinct 5-card hands.

**Insight:** This number becomes the denominator in many card probabilities. The combination is the natural count because the order of cards in a hand doesn’t matter.

## Key Takeaways

- ✓

  Combinations count unordered selections of k distinct items from n distinct items: k-subsets of an n-element set.
- ✓

  Main formula: C(n,k) = n! / (k!(n−k)!).
- ✓

  Connection to permutations: C(n,k) = (nP k) / k! (divide out internal order).
- ✓

  Symmetry: C(n,k) = C(n,n−k) often makes calculations easier.
- ✓

  Pascal’s identity: C(n,k) = C(n−1,k) + C(n−1,k−1) comes from splitting by whether a special element is included.
- ✓

  Boundary checks help prevent errors: C(n,0)=1, C(n,n)=1, and C(n,k)=0 for k>n.
- ✓

  In CS and probability, combinations often measure the size of subset search spaces and appear as “favorable ÷ total” counts.

## Common Mistakes

- ✗

  Using permutations when order doesn’t matter (forgetting to divide by k!).
- ✗

  Mixing up k and n−k, especially when k is close to n; failing to use symmetry.
- ✗

  Applying C(n,k) when repetition is allowed (this node assumes no repetition).
- ✗

  Computing gigantic factorials directly instead of canceling (e.g., expanding 52!); this increases arithmetic errors.

## Practice

easy

A class has 18 students. How many ways can you choose 4 students to present (order irrelevant)?

**Hint:** This is C(18,4). Use cancellation: 18!/14! = 18·17·16·15, then divide by 4!.

Show solution

C(18,4) = 18!/(4!14!) = (18·17·16·15)/24.

Compute numerator: 18·17=306, 16·15=240, so 306·240=73440.

73440/24 = 3060.

Answer: 3060.

medium

Compute C(12,9) without large factorials.

**Hint:** Use symmetry: C(12,9) = C(12,3). Then use (12·11·10)/3!.

Show solution

C(12,9) = C(12,3) = 12!/(3!9!) = (12·11·10)/6 = 1320/6 = 220.

hard

Show that C(n,k) = C(n,k−1) · (n−k+1)/k for 1 ≤ k ≤ n, and use it to compute C(20,5) from C(20,4).

**Hint:** Write both C(n,k) and C(n,k−1) using factorials and divide them. For the numeric part, compute C(20,4) first, then multiply by (20−5+1)/5 = 16/5.

Show solution

Derivation:

C(n,k) / C(n,k−1)

= [n!/(k!(n−k)!)] / [n!/((k−1)!(n−(k−1))!)]

= [n!/(k!(n−k)!)] · [((k−1)!(n−k+1)!)/n!]

= (k−1)!/k! · (n−k+1)!/(n−k)!

= (1/k) · (n−k+1)

So C(n,k) = C(n,k−1) · (n−k+1)/k.

Now compute:

C(20,4) = (20·19·18·17)/4! = (20·19·18·17)/24.

Compute 20·19=380, 18·17=306, product 380·306=116280.

116280/24 = 4845.

Then:

C(20,5) = C(20,4) · 16/5 = 4845·16/5.

4845/5 = 969, so 969·16 = 15504.

Answer: C(20,5) = 15504.

## Connections

- •Next up: [Probability Basics](/tech-tree/probability-basics/) (combinations become denominators for counting outcomes)
- •Related: [Binomial Theorem](/tech-tree/binomial-theorem/) (C(n,k) appears as coefficients in (x + y)ⁿ)
- •Review: [Permutations](/tech-tree/permutations/) (ordered selections; combinations are permutations ÷ k!)
- •Future: [Combinations with Repetition (Stars and Bars)](/tech-tree/stars-and-bars/) (when repeats are allowed)

Quality: A (4.6/5)

[← back to tree](/tech-tree/)[browse all →](/tech-tree/inventory/)
