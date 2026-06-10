---
title: Modular Arithmetic
description: Arithmetic with remainders. Congruence, modular inverse.
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
permalink: /tech-tree/modular-arithmetic/
---

[←Back to Tech Tree](/tech-tree/)

[inventory](/tech-tree/inventory/)[coverage](/tech-tree/coverage/)

# Modular Arithmetic

Discrete MathDifficulty: ★★☆☆☆Depth: 2Unlocks: 0

Arithmetic with remainders. Congruence, modular inverse.

## Interactive Visualization

⏮◀◀▶▶STEP0.25x1xZOOM

t=0s

## Core Concepts

- -Congruence modulo n (definition: integers grouped when their difference is divisible by n)
- -Residue classes and reduction to canonical representatives (remainders 0..n-1)
- -Modular multiplicative inverse (an element that multiplies to the multiplicative identity modulo n)

## Key Symbols & Notation

congruence notation: 'a == b (mod n)' (read: a is congruent to b modulo n)multiplicative inverse notation: 'a^-1' (read: the inverse of a modulo n)

## Essential Relationships

- -Congruence iff divisibility: a == b (mod n) exactly when n divides (a - b) (so congruence partitions Z into n residue classes)
- -Inverse existence/property: gcd(a,n)=1 iff there exists a^-1 with a \* a^-1 == 1 (mod n); if gcd(a,n)>1 no multiplicative inverse exists

## Prerequisites (1)

[Proof Techniques5 atoms](/tech-tree/proof-techniques/)

Advanced Learning Details

### Graph Position

17

Depth Cost

0

Fan-Out (ROI)

0

Bottleneck Score

2

Chain Length

### Cognitive Load

7

Atomic Elements

30

Total Elements

L1

Percentile Level

L4

Atomic Level

### All Concepts (15)

- - Modulus: the fixed positive integer n that defines 'mod n' arithmetic
- - Remainder and the 'mod' operation: mapping any integer a to its remainder in {0,...,n-1}
- - Congruence relation: definition 'a congruent-to b modulo n' means n divides (a - b)
- - Residue class: the set of all integers congruent to a modulo n (the equivalence class of a)
- - Representative of a residue class and canonical representative (e.g., least nonnegative remainder)
- - Equivalence-relation properties of congruence: reflexive, symmetric, transitive
- - Well-definedness of operations on residue classes (operation result independent of representative chosen)
- - Modular addition, subtraction, and multiplication: performing arithmetic on residue classes
- - Modular exponentiation: raising elements to powers modulo n
- - Modular inverse (multiplicative inverse modulo n): element x such that a \* x is congruent-to 1 modulo n
- - Units modulo n: the set of elements that have modular inverses (multiplicative group of invertible classes)
- - Relationship of invertibility to greatest common divisor: inverse exists exactly when gcd(a,n)=1
- - Solving linear congruences ax congruent-to b (mod n): solvability condition and number of solutions
- - Cancellation rule in modular arithmetic and its restriction to units only
- - Extended Euclidean algorithm as a constructive method to compute modular inverses and express gcd as a linear combination

### Teaching Strategy

Deep-dive lesson - accessible entry point but dense material. Use worked examples and spaced repetition.

Clock arithmetic is the easiest place to meet modular arithmetic: 23:00 plus 4 hours is 03:00, not 27:00. Modular arithmetic formalizes this “wrap-around” behavior and turns it into a powerful tool for reasoning about integers, solving equations, and building systems like checksums and cryptography.

TL;DR:

Modular arithmetic groups integers into residue classes modulo n. We write a ≡ b (mod n) when n divides (a − b). You can add/multiply congruences and reduce numbers to canonical remainders 0…n−1. A modular inverse a⁻¹ (mod n) exists exactly when gcd(a, n) = 1, and it lets you “divide” modulo n.

## What Is Modular Arithmetic?

### Why this concept exists (motivation)

In ordinary arithmetic, numbers grow without bound. But many real situations only care about **remainders** after division by some fixed number n:

- •Time on a 12-hour or 24-hour clock
- •Days of the week (mod 7)
- •Hashing and checksums
- •Repeating patterns in algorithms and data structures

Modular arithmetic is the mathematics of **working with remainders in a consistent way**.

### The core idea: “same remainder” as an equivalence

Fix an integer n ≥ 2 (the **modulus**). We say two integers a and b are **congruent modulo n** if they differ by a multiple of n.

**Definition (congruence).**

a ≡ b (mod n) ⇔ n ∣ (a − b)

Read this as: “a is congruent to b modulo n.”

This is not an equation about being literally equal; it is a statement that a and b land in the **same remainder class** when divided by n.

### Residue classes

All integers can be partitioned into n groups (for modulus n), where each group corresponds to a remainder.

For example, modulo 5:

- •…, −10, −5, 0, 5, 10, … are all congruent (remainder 0)
- •…, −9, −4, 1, 6, 11, … are all congruent (remainder 1)
- •… and so on up to remainder 4

Each group is called a **residue class**.

### Canonical representatives (the “standard remainder”)

To compute and communicate easily, we usually represent each residue class by a **canonical representative** in {0, 1, 2, …, n − 1}.

If a is any integer, its canonical representative mod n is:

r = a mod n, where 0 ≤ r ≤ n − 1 and a ≡ r (mod n)

This “reduce to a remainder” step is what most people first recognize as modular arithmetic.

### Quick intuition check

- •17 ≡ 2 (mod 5) because 17 − 2 = 15 and 5 ∣ 15
- •−1 ≡ 6 (mod 7) because −1 − 6 = −7 and 7 ∣ −7

Notice negative numbers fit naturally: they still have a remainder class.

### Congruence behaves like equality in many ways

Congruence is an **equivalence relation** (you don’t need heavy theory here, but the properties guide reasoning):

- •Reflexive: a ≡ a (mod n)
- •Symmetric: if a ≡ b (mod n) then b ≡ a (mod n)
- •Transitive: if a ≡ b (mod n) and b ≡ c (mod n) then a ≡ c (mod n)

This is why we can safely “replace” numbers with congruent ones when computing modulo n.

## Core Mechanic 1: Computing with Congruences (Reduction, Addition, Multiplication)

### Why rules are needed

If modular arithmetic is going to be useful, we need to know what operations are allowed. The guiding principle is:

> If two numbers are congruent, they behave the same under addition and multiplication (mod n).

This lets you simplify big computations by replacing numbers with smaller congruent ones.

### Reduction rule (replace by a remainder)

If a ≡ r (mod n), then you can replace a with r in any modular computation.

Example idea: Instead of computing 987654321 mod 9 directly, repeatedly reduce.

### Addition and subtraction are well-behaved

If

a ≡ b (mod n) and c ≡ d (mod n)

then

a + c ≡ b + d (mod n)

a − c ≡ b − d (mod n)

**Reason (showing the divisibility structure).**

If a ≡ b (mod n), then n ∣ (a − b).

If c ≡ d (mod n), then n ∣ (c − d).

Then

(a + c) − (b + d)

= (a − b) + (c − d)

Since each term is divisible by n, the sum is divisible by n, so:

n ∣ ((a + c) − (b + d))

⇒ a + c ≡ b + d (mod n)

The subtraction case is the same idea.

### Multiplication is also well-behaved

If

a ≡ b (mod n)

then for any integer c,

a·c ≡ b·c (mod n)

More generally, if a ≡ b (mod n) and c ≡ d (mod n), then:

a·c ≡ b·d (mod n)

**Reason (one clean derivation).**

Assume a ≡ b (mod n) and c ≡ d (mod n).

We want n ∣ (ac − bd). Write:

ac − bd

= ac − bc + bc − bd

= c(a − b) + b(c − d)

Now:

- •n ∣ (a − b), so n ∣ c(a − b)
- •n ∣ (c − d), so n ∣ b(c − d)

Therefore n divides their sum, so ac ≡ bd (mod n).

### Exponentiation: reduce early, reduce often

Because multiplication respects congruence, exponentiation does too:

If a ≡ b (mod n), then aᵏ ≡ bᵏ (mod n) for k ≥ 0.

This is extremely practical. When computing a large power mod n:

1) reduce the base mod n

2) multiply while reducing at every step

### A compact “allowed operations” table

| Operation | If a ≡ b (mod n) and c ≡ d (mod n) then… | Safe? |
| --- | --- | --- |
| Addition | a + c ≡ b + d (mod n) | Yes |
| Subtraction | a − c ≡ b − d (mod n) | Yes |
| Multiplication | a·c ≡ b·d (mod n) | Yes |
| Exponentiation | aᵏ ≡ bᵏ (mod n) | Yes |
| Division | a/c ≡ b/d (mod n) | Not always (needs inverses) |

That last row is the subtle one: **division is not automatically valid**. That leads to modular inverses.

### A note on notation: “mod” vs “≡ (mod n)”

- •“a mod n” often means the **remainder** (a number in 0…n−1).
- •“a ≡ b (mod n)” is a **relationship** between integers.

They are connected but not identical. You can say:

a mod n = r ⇔ a ≡ r (mod n) and 0 ≤ r ≤ n − 1

## Core Mechanic 2: Modular Multiplicative Inverses (When “Division” Works)

### Why inverses matter

In ordinary arithmetic, division by a (nonzero) number a is multiplication by 1/a.

In modular arithmetic, we want an analogous operation: given a and modulus n, we’d like to solve equations like:

a·x ≡ 1 (mod n)

If such an x exists, it plays the role of “1/a” modulo n.

### Definition: modular multiplicative inverse

Let n ≥ 2. An integer x is a **multiplicative inverse** of a modulo n if:

a·x ≡ 1 (mod n)

We write x ≡ a⁻¹ (mod n) when x is an inverse of a modulo n.

Important: a⁻¹ here is **not** the real-number reciprocal 1/a. It is an integer residue class mod n.

### Existence: exactly when gcd(a, n) = 1

A modular inverse exists iff a and n are **coprime**.

**Theorem.** a has an inverse mod n ⇔ gcd(a, n) = 1.

#### Why (direction 1): if inverse exists, gcd must be 1

Assume there exists x such that:

a·x ≡ 1 (mod n)

By definition, that means:

n ∣ (a·x − 1)

So there exists an integer k such that:

a·x − 1 = k·n

Rearrange:

a·x + n·(−k) = 1

This shows 1 is an integer linear combination of a and n. Any common divisor of a and n must divide the left-hand side, hence must divide 1. Therefore gcd(a, n) = 1.

#### Why (direction 2): if gcd is 1, an inverse exists

If gcd(a, n) = 1, then by Bézout’s identity there exist integers x and y such that:

a·x + n·y = 1

Reduce both sides mod n:

a·x + n·y ≡ 1 (mod n)

But n·y ≡ 0 (mod n), so:

a·x ≡ 1 (mod n)

So x is an inverse of a mod n (perhaps after reducing x to 0…n−1).

### Uniqueness (mod n)

If an inverse exists, it is unique modulo n: if x and x′ both satisfy a·x ≡ 1 (mod n), then x ≡ x′ (mod n).

### How to find inverses (practical approach)

At difficulty 2, the most useful method is: **solve a·x + n·y = 1** by inspection for small numbers or by the Extended Euclidean Algorithm for larger ones.

Even without the full algorithm, you can often reason quickly.

Example of “inspection + adjustment”:

Find the inverse of 3 mod 7.

We want 3x ≡ 1 (mod 7). Try multiples of 3:

3·1 = 3

3·2 = 6

3·3 = 9 ≡ 2

3·4 = 12 ≡ 5

3·5 = 15 ≡ 1 ✅

So 3⁻¹ ≡ 5 (mod 7).

### Using inverses to solve linear congruences

If gcd(a, n) = 1, then the congruence:

a·x ≡ b (mod n)

has a unique solution modulo n, found by multiplying both sides by a⁻¹:

x ≡ a⁻¹·b (mod n)

This is the modular version of “divide both sides by a,” but it only works when a is invertible mod n.

### When division fails

If gcd(a, n) ≠ 1, then a has no inverse mod n.

Example: 2 mod 6.

Possible products 2x mod 6 are only {0, 2, 4}. You can never get 1, so no inverse exists.

This also explains why you cannot cancel factors freely.

For instance, even if:

2·x ≡ 2·y (mod 6)

you cannot conclude x ≡ y (mod 6), because multiplying by 2 “collapses” multiple residues together when 2 is not invertible.

## Application/Connection: Checks, Cycles, and Solving Problems Efficiently

### Why modular arithmetic shows up everywhere

Modular arithmetic turns “remainder reasoning” into a clean algebraic system. That gives you two big powers:

1) **Cycle detection and periodic behavior**: many processes repeat modulo n.

2) **Fast computation**: reduce numbers early to keep them small.

### Application 1: quick divisibility and checksum-style reasoning

A classic example is mod 9 (digit sums). Because 10 ≡ 1 (mod 9), we have:

10ᵏ ≡ 1ᵏ ≡ 1 (mod 9)

So a decimal number like:

N = d₀ + d₁·10 + d₂·10² + … + dₖ·10ᵏ

satisfies:

N ≡ d₀ + d₁ + d₂ + … + dₖ (mod 9)

That’s why the sum of digits determines N mod 9.

This same idea generalizes: represent numbers in a base, reduce the base modulo n, and simplify.

### Application 2: solving “clock” equations

Scheduling, cyclic buffers, and time calculations are naturally modular.

If it’s 22:00 and you add 9 hours:

22 + 9 = 31

31 mod 24 = 7

So the time is 07:00.

The key is that the underlying variable (hour) lives in the residue classes mod 24.

### Application 3: linear congruences in puzzles and programming

Suppose you want x such that:

5x ≡ 3 (mod 17)

If you can find 5⁻¹ (mod 17), you can solve immediately:

x ≡ 5⁻¹·3 (mod 17)

This pattern appears in:

- •hashing schemes
- •randomized algorithms
- •modular indexing (e.g., circular arrays)

### Application 4 (preview): cryptography and finite fields

A large part of modern public-key cryptography uses modular arithmetic with huge numbers.

Two ideas you now have the vocabulary for:

- •working with congruences to keep computations bounded
- •using modular inverses (division) when gcd conditions are right

If n is prime, then every nonzero residue has an inverse mod n, and the system behaves like a “field.” That’s a major gateway concept for later nodes.

### A quick comparison: integer arithmetic vs modular arithmetic

| Feature | Integers (ℤ) | Modulo n (ℤ/nℤ) |
| --- | --- | --- |
| Size | infinite | finite (n residues) |
| Addition/multiplication | always defined | always defined (then reduce) |
| Division | not always in ℤ | only when an inverse exists |
| Inverses | only ±1 in ℤ | depends on gcd(a, n) |

The key mental shift: modulo n you are working with **classes of integers**, not a single integer.

## Worked Examples (3)

### Reduce large and negative numbers to canonical representatives

Compute: (a) 137 mod 12, (b) −29 mod 8, and express each as a congruence.

1. (a) Divide 137 by 12:

   137 = 12·11 + 5

   So the remainder is 5.
2. Therefore:

   137 ≡ 5 (mod 12)

   and 137 mod 12 = 5.
3. (b) We want r ∈ {0,1,2,3,4,5,6,7} such that −29 ≡ r (mod 8).
4. Compute a nearby multiple of 8:

   −29 = 8·(−4) + 3

   because 8·(−4) = −32 and −32 + 3 = −29.
5. So the remainder is 3, and:

   −29 ≡ 3 (mod 8)

   −29 mod 8 = 3.

**Insight:** For negatives, don’t guess—rewrite a = n·q + r with 0 ≤ r ≤ n−1. That automatically produces the canonical remainder.

### Fast modular computation using reduction at each step

Compute 23²⁷ mod 7 without ever computing 23²⁷ explicitly.

1. First reduce the base:

   23 ≡ 2 (mod 7) because 23 = 7·3 + 2.
2. So:

   23²⁷ ≡ 2²⁷ (mod 7).
3. Notice a small cycle:

   2¹ ≡ 2 (mod 7)

   2² = 4 ≡ 4 (mod 7)

   2³ = 8 ≡ 1 (mod 7)
4. Once 2³ ≡ 1, powers repeat every 3:

   2²⁷ = (2³)⁹.
5. So:

   2²⁷ ≡ (2³)⁹ ≡ 1⁹ ≡ 1 (mod 7).
6. Therefore:

   23²⁷ mod 7 = 1.

**Insight:** Modular exponentiation often becomes easy after you find a small repeating pattern (a cycle). Reducing early keeps numbers tiny.

### Find a modular inverse and solve a linear congruence

Solve 5x ≡ 3 (mod 17).

1. Because 17 is prime and 5 ≠ 0 (mod 17), gcd(5,17) = 1, so 5 has an inverse mod 17.
2. Find 5⁻¹ (mod 17) by trying multiples of 5:

   5·1 = 5

   5·2 = 10

   5·3 = 15

   5·4 = 20 ≡ 3

   5·5 = 25 ≡ 8

   5·6 = 30 ≡ 13

   5·7 = 35 ≡ 1 ✅
3. So 5⁻¹ ≡ 7 (mod 17).
4. Multiply both sides of 5x ≡ 3 (mod 17) by 7:

   7·5x ≡ 7·3 (mod 17).
5. Left side simplifies:

   7·5x ≡ 1·x ≡ x (mod 17).
6. Right side:

   7·3 = 21 ≡ 4 (mod 17).
7. Therefore:

   x ≡ 4 (mod 17).

   Canonical solution: x = 4.

**Insight:** “Division” modulo n means multiplying by an inverse. The inverse exists exactly when gcd(a, n) = 1.

## Key Takeaways

- ✓

  a ≡ b (mod n) means n ∣ (a − b): they differ by a multiple of n, so they have the same remainder mod n.
- ✓

  Every integer has a canonical representative modulo n in {0, 1, …, n − 1}.
- ✓

  You can add, subtract, multiply, and exponentiate congruences safely; always reduce along the way to keep numbers small.
- ✓

  Congruence is not the same as equality; it is an equivalence relation grouping integers into residue classes.
- ✓

  A modular inverse a⁻¹ (mod n) is an x such that a·x ≡ 1 (mod n).
- ✓

  An inverse exists iff gcd(a, n) = 1; if it exists, it is unique modulo n.
- ✓

  To solve a·x ≡ b (mod n) with gcd(a, n) = 1, compute x ≡ a⁻¹·b (mod n).

## Common Mistakes

- ✗

  Treating “≡” like “=” and forgetting the “(mod n)” context (e.g., concluding 17 ≡ 2 implies 17 = 2).
- ✗

  Assuming you can always divide/cancel factors in congruences; cancellation requires the factor to be invertible mod n.
- ✗

  Mixing up “a mod n” (a remainder) with “a ≡ b (mod n)” (a relationship).
- ✗

  Forgetting to convert negative residues to canonical form (e.g., leaving an answer as −1 mod 7 instead of 6).

## Practice

easy

Reduce each to a canonical representative: (a) 1001 mod 9, (b) −45 mod 11.

**Hint:** Write a = n·q + r with 0 ≤ r ≤ n−1. For 1001 mod 9, note 9·111 = 999.

Show solution

(a) 1001 = 9·111 + 2, so 1001 mod 9 = 2 and 1001 ≡ 2 (mod 9).

(b) −45 = 11·(−5) + 10 (since −55 + 10 = −45), so −45 mod 11 = 10 and −45 ≡ 10 (mod 11).

medium

Compute 3⁴⁰ mod 10.

**Hint:** Look for a repeating cycle in powers of 3 modulo 10. Once you find the period, reduce 40 by that period.

Show solution

Compute a few powers mod 10:

3¹ ≡ 3

3² = 9 ≡ 9

3³ = 27 ≡ 7

3⁴ = 21 ≡ 1 (mod 10)

So the pattern repeats every 4 because 3⁴ ≡ 1.

Then 3⁴⁰ = (3⁴)¹⁰ ≡ 1¹⁰ ≡ 1 (mod 10).

hard

Find the inverse of 7 modulo 26 if it exists, and use it to solve 7x ≡ 5 (mod 26).

**Hint:** First check gcd(7, 26). Then find x such that 7x ≡ 1 (mod 26) by trying small multiples or by solving 7x + 26y = 1.

Show solution

gcd(7, 26) = 1, so an inverse exists.

Try multiples of 7 mod 26:

7·1 = 7

7·2 = 14

7·3 = 21

7·4 = 28 ≡ 2

7·5 = 35 ≡ 9

7·6 = 42 ≡ 16

7·7 = 49 ≡ 23

7·8 = 56 ≡ 4

7·9 = 63 ≡ 11

7·10 = 70 ≡ 18

7·11 = 77 ≡ 25

7·12 = 84 ≡ 6

7·13 = 91 ≡ 13

7·14 = 98 ≡ 20

7·15 = 105 ≡ 1 ✅

So 7⁻¹ ≡ 15 (mod 26).

Now solve 7x ≡ 5 (mod 26) by multiplying both sides by 15:

x ≡ 15·5 ≡ 75 (mod 26).

Reduce: 75 = 26·2 + 23, so x ≡ 23 (mod 26).

## Connections

Next steps and related nodes:

- •[Greatest Common Divisor (GCD)](/tech-tree/gcd/) — needed for the condition gcd(a, n) = 1 and for computing inverses.
- •[Extended Euclidean Algorithm](/tech-tree/extended-euclid/) — efficient way to find a⁻¹ (mod n) by solving a·x + n·y = 1.
- •[Chinese Remainder Theorem](/tech-tree/chinese-remainder-theorem/) — solving systems of congruences.
- •[Finite Fields (mod p)](/tech-tree/finite-fields/) — when p is prime, every nonzero element has an inverse.
- •[Modular Exponentiation](/tech-tree/modular-exponentiation/) — efficient computation of aᵏ mod n for large k.

Quality: A (4.4/5)

[← back to tree](/tech-tree/)[browse all →](/tech-tree/inventory/)
