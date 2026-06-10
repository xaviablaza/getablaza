---
title: Recurrence Relations
description: Defining sequences recursively. Solving with characteristic equations.
date: '2026-07-01'
scheduled: '2026-09-21'
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
inspiration_url: https://templeton.host/tech-tree/recurrence-relations/
inspiration_category: tech-tree
---

> Source-copy draft imported from [https://templeton.host/tech-tree/recurrence-relations/](https://templeton.host/tech-tree/recurrence-relations/). Names, domain references, and local media paths were adapted for Xavi Ablaza / getablaza.com.

[←Back to Tech Tree](/tech-tree/)

[inventory](/tech-tree/inventory/)[coverage](/tech-tree/coverage/)

# Recurrence Relations

Discrete MathDifficulty: ★★★☆☆Depth: 3Unlocks: 10

Defining sequences recursively. Solving with characteristic equations.

## Interactive Visualization

⏮◀◀▶▶STEP0.25x1xZOOM

t=0s

## Core Concepts

- -Linear homogeneous constant-coefficient recurrence of order k
- -Characteristic polynomial of the recurrence (polynomial in r derived from recurrence coefficients)
- -General solution form: linear combination of root-based terms (r^n), with repeated roots giving factors n^j; constants fixed by initial conditions

## Key Symbols & Notation

r (root variable of the characteristic polynomial P(r)=0)

## Essential Relationships

- -Roots of P(r)=0 map directly to terms in the general solution (multiplicity m => factors n^0,...,n^{m-1}); initial conditions determine the linear combination coefficients

## Prerequisites (3)

[Recursion5 atoms](/tech-tree/recursion/)[Sequences5 atoms](/tech-tree/sequences/)[Proof Techniques5 atoms](/tech-tree/proof-techniques/)

## Unlocks (3)

[Dynamic Programminglvl 3](/tech-tree/dynamic-programming/)[Generating Functionslvl 3](/tech-tree/generating-functions/)[Divide and Conquerlvl 3](/tech-tree/divide-conquer/)

Advanced Learning Details

### Graph Position

47

Depth Cost

10

Fan-Out (ROI)

6

Bottleneck Score

3

Chain Length

### Cognitive Load

5

Atomic Elements

35

Total Elements

L2

Percentile Level

L3

Atomic Level

### All Concepts (16)

- - Linear recurrence relation with constant coefficients: a relation that expresses a\_n as a linear combination of a fixed number of previous terms with constant multipliers
- - Order of a recurrence: the number of previous terms the relation depends on (the ’k’ in a\_n defined using a\_{n-1}, ..., a\_{n-k})
- - Homogeneous recurrence: a recurrence with zero nonhomogeneous term (no extra function of n on the right-hand side)
- - Nonhomogeneous (inhomogeneous) recurrence: a recurrence that includes an additional known function of n on the right-hand side
- - Characteristic polynomial/equation: the polynomial equation formed by replacing a\_n by r^n (or using the shift) that determines solution behaviours
- - Root of the characteristic polynomial: a value r that satisfies the characteristic equation
- - Multiplicity of a root: how many times a particular root occurs in the characteristic polynomial
- - General solution of a homogeneous linear recurrence: the linear combination of basic solutions determined by the characteristic roots
- - Basis solution r^n: for each distinct root r of the characteristic polynomial, r^n is a basic solution (for homogeneous case)
- - Effect of repeated roots: if a root r has multiplicity m, the associated part of the solution is a polynomial in n of degree m-1 times r^n (e.g., n r^n for multiplicity 2)
- - Complex roots and real solutions: complex conjugate roots produce real-valued solution terms that can be expressed with r^n cos(nθ) and r^n sin(nθ) or equivalent real linear combinations
- - Particular solution concept: any specific solution of a nonhomogeneous recurrence which, when added to the homogeneous general solution, gives the full general solution
- - Method of undetermined coefficients (sketch level): a technique for guessing a form of the particular solution based on the nonhomogeneous term
- - Initial conditions determine constants: using the first k terms (for order k) to solve for the k arbitrary constants in the general solution
- - Dimension/order correspondence: the order k equals the number of independent arbitrary constants (the dimension of the solution space)
- - Companion-matrix / linear-algebra viewpoint (optional): representing a linear recurrence as a linear transformation on a k-dimensional state vector; solving via eigenvalues corresponds to the characteristic roots

### Teaching Strategy

Self-serve tutorial - low prerequisites, straightforward concepts.

Many sequences in CS and discrete math aren’t given by a closed formula—they’re defined by how each term depends on earlier terms. Recurrence relations are the language for that dependency, and characteristic equations are the workhorse tool for turning “defined recursively” into “solved explicitly.”

TL;DR:

A linear homogeneous constant-coefficient recurrence (like aₙ = c₁aₙ₋₁ + ⋯ + cₖaₙ₋ₖ) can often be solved by guessing aₙ = rⁿ. This produces a characteristic polynomial P(r). If P has distinct roots rᵢ, the general solution is aₙ = ∑ αᵢ rᵢⁿ. Repeated roots of multiplicity m add factors nʲ: (α₀ + α₁n + ⋯ + αₘ₋₁nᵐ⁻¹) rⁿ. Initial conditions determine the constants αᵢ.

## What Is a Recurrence Relation?

A **recurrence relation** defines a sequence by relating later terms to earlier ones. Instead of saying “the n-th term equals some explicit function of n,” we say “the n-th term is computed from previous terms.”

Why this matters in discrete math and CS:

- •Many counting problems naturally “build” solutions from smaller sizes.
- •Many algorithms (especially dynamic programming and divide-and-conquer) have running times described recursively.
- •Recurrences capture **structure**: what information from the past is needed to produce the next value.

### Sequences: explicit vs recursive

An explicit definition might be:

- •aₙ = 3·2ⁿ (geometric)

A recursive (recurrence) definition might be:

- •a₀ = 3
- •aₙ = 2aₙ₋₁ for n ≥ 1

Both define the same sequence, but the recursive version highlights the “local rule.”

### Order and initial conditions

A recurrence can depend on one or more previous terms.

- •**Order 1:** aₙ depends on aₙ₋₁ only.
- •**Order k:** aₙ depends on aₙ₋₁, aₙ₋₂, …, aₙ₋ₖ.

To uniquely define a sequence, you need enough starting values (initial conditions):

- •Order 1 needs 1 initial value (like a₀).
- •Order k needs k initial values (like a₀, a₁, …, aₖ₋₁).

Example (order 2):

- •a₀ = 0, a₁ = 1
- •aₙ = aₙ₋₁ + aₙ₋₂

That’s Fibonacci.

### The class we’ll solve: linear homogeneous constant-coefficient

This lesson focuses on a very solvable and very common family:

A recurrence is **linear** if terms appear in a linear combination (no products like aₙ₋₁·aₙ₋₂ and no squares like aₙ₋₁²).

It is **homogeneous** if there is no “extra” term depending only on n (no added constant or function f(n)).

It has **constant coefficients** if the weights don’t change with n.

So the standard form is:

aₙ = c₁aₙ₋₁ + c₂aₙ₋₂ + ⋯ + cₖaₙ₋ₖ

with fixed constants c₁, …, cₖ.

We’ll learn the main trick for solving these: the **characteristic equation**. The motivation is simple: if the recurrence behaves like repeated multiplication, then exponentials rⁿ are natural building blocks.

## Core Mechanic 1: From Recurrence to Characteristic Polynomial

To solve

aₙ = c₁aₙ₋₁ + c₂aₙ₋₂ + ⋯ + cₖaₙ₋ₖ,

we want a closed form for aₙ.

### Why guess aₙ = rⁿ?

A key observation: exponentials have the property that shifting the index multiplies by a constant:

- •If aₙ = rⁿ, then aₙ₋₁ = rⁿ⁻¹ = r⁻¹·rⁿ, and generally aₙ₋ⱼ = rⁿ⁻ⱼ = r⁻ⱼ·rⁿ.

That means a linear combination of shifted terms becomes a multiple of rⁿ.

### Deriving the characteristic polynomial

Assume a trial solution aₙ = rⁿ (with r ≠ 0). Substitute into the recurrence:

rⁿ = c₁rⁿ⁻¹ + c₂rⁿ⁻² + ⋯ + cₖrⁿ⁻ᵏ

Factor out rⁿ⁻ᵏ (or divide by rⁿ⁻ᵏ) to get a polynomial in r. A clean approach is to divide both sides by rⁿ⁻ᵏ:

rᵏ = c₁rᵏ⁻¹ + c₂rᵏ⁻² + ⋯ + cₖ

Bring everything to one side:

rᵏ − c₁rᵏ⁻¹ − c₂rᵏ⁻² − ⋯ − cₖ = 0

This polynomial

P(r) = rᵏ − c₁rᵏ⁻¹ − c₂rᵏ⁻² − ⋯ − cₖ

is the **characteristic polynomial**, and the equation P(r) = 0 is the **characteristic equation**.

Any root r of P(r) = 0 gives a solution aₙ = rⁿ.

### Example: Fibonacci characteristic polynomial

Fibonacci recurrence:

aₙ = aₙ₋₁ + aₙ₋₂

Here k = 2, c₁ = 1, c₂ = 1.

Characteristic equation:

r² = r + 1

r² − r − 1 = 0

Roots:

r = (1 ± √5)/2

So we already know rⁿ terms will appear in the closed form.

### Why this works (intuition)

The recurrence is a linear transformation that maps a “state” of k previous values to the next one. Exponentials rⁿ behave like eigenvectors of the shift operator: shifting n corresponds to scaling by r. The characteristic equation is essentially the eigenvalue condition.

You don’t need linear algebra to use this method, but it explains why exponentials and polynomials-in-n times exponentials show up.

### What we get from roots

- •Distinct roots → sum of exponentials.
- •Repeated roots → exponential times polynomial factors in n.

We’ll make that precise next.

## Core Mechanic 2: Building the General Solution (Distinct and Repeated Roots)

Once you have the characteristic polynomial P(r), solving the recurrence becomes a “root bookkeeping” problem.

### Case A: Distinct roots

Suppose P(r) has k distinct roots r₁, r₂, …, rₖ.

Then the general solution is

aₙ = α₁r₁ⁿ + α₂r₂ⁿ + ⋯ + αₖrₖⁿ

where α₁, …, αₖ are constants determined by the initial conditions.

Why we can add solutions:

- •The recurrence is linear and homogeneous.
- •If sequences xₙ and yₙ each satisfy it, then (xₙ + yₙ) also satisfies it.
- •Scaling a solution by a constant also preserves being a solution.

So once we have building blocks rᵢⁿ, linear combinations are still solutions.

### Case B: Repeated roots

If r is a root of multiplicity m (meaning (r − r₀)ᵐ divides P(r)), we don’t get m linearly independent solutions by repeating rⁿ.

Instead, the m independent solutions are:

rⁿ, n·rⁿ, n²·rⁿ, …, nᵐ⁻¹·rⁿ

So the contribution of a repeated root r with multiplicity m is:

(β₀ + β₁n + β₂n² + ⋯ + βₘ₋₁nᵐ⁻¹) rⁿ

where βⱼ are constants.

### Quick example of a repeated root

Consider

aₙ = 2aₙ₋₁ − aₙ₋₂

Characteristic equation:

r² = 2r − 1

r² − 2r + 1 = 0

(r − 1)² = 0

So r = 1 is a root of multiplicity 2.

General solution:

aₙ = (α + βn)·1ⁿ = α + βn

So the sequence must be linear in n.

### Solving for constants using initial conditions

You always use the initial values to solve for α’s (and β’s). This is usually a small linear system.

For distinct roots r₁, …, rₖ:

Given a₀, a₁, …, aₖ₋₁,

set up equations:

a₀ = α₁r₁⁰ + ⋯ + αₖrₖ⁰

a₁ = α₁r₁¹ + ⋯ + αₖrₖ¹

…

aₖ₋₁ = α₁r₁ᵏ⁻¹ + ⋯ + αₖrₖᵏ⁻¹

Solve for αᵢ.

For repeated roots, you do the same but with the polynomial factors.

### Reality check: complex roots

Sometimes P(r) has complex roots. That’s not a problem.

If coefficients cᵢ are real, complex roots come in conjugate pairs (a ± bi). Their contributions combine to a real sequence. Often you can rewrite them using cos and sin:

If r = ρe^{iθ}, then rⁿ = ρⁿe^{inθ}

and the real solutions look like:

ρⁿ( A cos(nθ) + B sin(nθ) )

You won’t always need this form, but it’s useful when oscillations appear.

### Summary table: root patterns → solution patterns

| Root type in P(r) | Multiplicity | Independent solution terms | Contribution to aₙ |
| --- | --- | --- | --- |
| Real root r | 1 | rⁿ | αrⁿ |
| Real root r | m | rⁿ, n rⁿ, …, nᵐ⁻¹ rⁿ | (∑ⱼ₌₀^{m−1} βⱼ nʲ) rⁿ |
| Complex pair ρe^{±iθ} | 1 each | ρⁿcos(nθ), ρⁿsin(nθ) | ρⁿ(A cos(nθ) + B sin(nθ)) |

At this point, you can solve a large fraction of recurrence relations that show up in discrete math courses and CS analysis.

## Application/Connection: Why CS Cares (DP, Divide-and-Conquer, Growth Rates)

Recurrence relations are not just a math curiosity—they are a core tool for reasoning about programs.

### 1) Algorithm running times

Many algorithms are defined recursively, so their runtimes are too.

Example: if a function does two recursive calls on size n−1 plus O(1) work, you might get:

T(n) = 2T(n−1) + 1

This one is not homogeneous (there’s a +1), so characteristic polynomials alone don’t finish it—but the homogeneous part still guides the growth. You can often solve the homogeneous part first, then find a particular solution.

Even when you ultimately use the Master Theorem or substitution, having recurrence intuition helps you avoid mistakes.

### 2) Dynamic programming (DP)

DP problems typically define optimal values by recurrences.

Example shape:

DP[n] = min( DP[n−1] + cost₁, DP[n−2] + cost₂, … )

Those aren’t linear recurrences (because of min/max), but the mindset is the same: compute a sequence from earlier values.

Recurrence relations teach you:

- •what “state” is required (order k)
- •why base cases matter
- •how dependency structure controls complexity

This directly unlocks [Dynamic Programming](/tech-tree/dynamic-programming/).

### 3) Closed forms reveal growth rates

Suppose you solve:

aₙ = 3aₙ₋₁ − 2aₙ₋₂

n ≥ 2

Characteristic equation:

r² − 3r + 2 = 0

(r − 1)(r − 2) = 0

Solution:

aₙ = α·1ⁿ + β·2ⁿ = α + β·2ⁿ

As n grows, β·2ⁿ dominates (unless β = 0). This kind of analysis is everywhere in complexity and combinatorics: the largest-magnitude root typically dictates asymptotic behavior.

### 4) Bridge to generating functions

Characteristic polynomials are one way to solve linear recurrences.

Generating functions are another, often more powerful for:

- •non-homogeneous recurrences
- •combinatorial counting with “add one object” logic

Knowing characteristic roots makes generating-function solutions feel less mysterious: both techniques transform a recurrence into an algebraic object (a polynomial or power series) you can manipulate.

This connects to [Generating Functions](/tech-tree/generating-functions/).

### 5) Divide-and-conquer

Divide-and-conquer often yields recurrences like:

T(n) = aT(n/b) + f(n)

Those aren’t constant-coefficient in n, so the characteristic polynomial method doesn’t directly apply, but you’ll reuse the same habits:

- •identify the recurrence structure
- •unroll a few steps
- •infer a closed form or tight bound

That prepares you for [Divide and Conquer](/tech-tree/divide-conquer/).

### Big picture

Characteristic equations give you a “closed form lens.” Even if you later switch to asymptotic methods, you’ll have a mental model of what sequences are capable of doing: exponential growth, oscillation, polynomial factors from repeated roots, and mixtures of these behaviors.

## Worked Examples (3)

### Solve aₙ = 5aₙ₋₁ − 6aₙ₋₂ with a₀ = 1, a₁ = 4

This is a linear homogeneous constant-coefficient recurrence of order 2. We’ll use the characteristic equation, then fit constants using the initial conditions.

1. Write the recurrence:

   aₙ = 5aₙ₋₁ − 6aₙ₋₂
2. Try a solution aₙ = rⁿ and substitute:

   rⁿ = 5rⁿ⁻¹ − 6rⁿ⁻²
3. Divide both sides by rⁿ⁻² (assuming r ≠ 0):

   r² = 5r − 6
4. Bring to one side to get the characteristic polynomial:

   r² − 5r + 6 = 0
5. Factor:

   r² − 5r + 6 = (r − 2)(r − 3) = 0
6. Distinct roots r₁ = 2, r₂ = 3 ⇒ general solution:

   aₙ = α·2ⁿ + β·3ⁿ
7. Use initial condition a₀ = 1:

   a₀ = α·2⁰ + β·3⁰ = α + β = 1
8. Use initial condition a₁ = 4:

   a₁ = α·2¹ + β·3¹ = 2α + 3β = 4
9. Solve the system:

   From α + β = 1 ⇒ α = 1 − β

   Substitute into 2α + 3β = 4:

   2(1 − β) + 3β = 4

   2 − 2β + 3β = 4

   2 + β = 4

   β = 2

   Then α = 1 − 2 = −1
10. Final closed form:

    aₙ = −1·2ⁿ + 2·3ⁿ = 2·3ⁿ − 2ⁿ

**Insight:** Distinct characteristic roots produce a sum of exponentials. The constants come from a small linear system built from initial conditions.

### Solve aₙ = 2aₙ₋₁ − aₙ₋₂ with a₀ = 3, a₁ = 5 (repeated root case)

This recurrence has order 2 and constant coefficients, so we again use aₙ = rⁿ. This time the characteristic polynomial has a repeated root, which changes the solution form.

1. Write the recurrence:

   aₙ = 2aₙ₋₁ − aₙ₋₂
2. Substitute aₙ = rⁿ:

   rⁿ = 2rⁿ⁻¹ − rⁿ⁻²
3. Divide by rⁿ⁻²:

   r² = 2r − 1
4. Characteristic polynomial:

   r² − 2r + 1 = 0
5. Factor:

   r² − 2r + 1 = (r − 1)²
6. Root r = 1 with multiplicity 2 ⇒ general solution:

   aₙ = (α + βn)·1ⁿ = α + βn
7. Use a₀ = 3:

   a₀ = α + β·0 = α = 3
8. Use a₁ = 5:

   a₁ = α + β·1 = 3 + β = 5

   β = 2
9. Final closed form:

   aₙ = 3 + 2n

**Insight:** A repeated root of multiplicity m adds polynomial factors up to degree m−1. Here multiplicity 2 forces solutions to be linear in n.

### Fibonacci closed form structure (roots and constants set-up)

We’ll derive the characteristic roots for Fibonacci and show how the initial conditions determine constants. (The algebra simplifies nicely, but the important part is the method.)

1. Fibonacci recurrence:

   Fₙ = Fₙ₋₁ + Fₙ₋₂ with F₀ = 0, F₁ = 1
2. Try Fₙ = rⁿ:

   rⁿ = rⁿ⁻¹ + rⁿ⁻²
3. Divide by rⁿ⁻²:

   r² = r + 1
4. Characteristic polynomial:

   r² − r − 1 = 0
5. Solve quadratic:

   r = (1 ± √5)/2

   Let φ = (1 + √5)/2 and ψ = (1 − √5)/2
6. General solution (distinct roots):

   Fₙ = α φⁿ + β ψⁿ
7. Use F₀ = 0:

   0 = α φ⁰ + β ψ⁰ = α + β ⇒ β = −α
8. Use F₁ = 1:

   1 = α φ + β ψ = α φ − α ψ = α(φ − ψ)
9. Compute φ − ψ:

   φ − ψ = [(1 + √5) − (1 − √5)]/2 = (2√5)/2 = √5
10. So α = 1/√5 and β = −1/√5
11. Closed form:

    Fₙ = (φⁿ − ψⁿ)/√5

**Insight:** Even famous sequences are just “roots + constants.” The constant-finding step is systematic: write equations for n = 0, 1, … and solve.

## Key Takeaways

- ✓

  A recurrence relation defines a sequence using earlier terms; order k means you need k initial conditions.
- ✓

  For linear homogeneous constant-coefficient recurrences, try aₙ = rⁿ to derive the characteristic polynomial P(r).
- ✓

  Each root r of P(r) contributes a solution term rⁿ; distinct roots add as a linear combination aₙ = ∑ αᵢ rᵢⁿ.
- ✓

  A root of multiplicity m contributes (β₀ + β₁n + ⋯ + βₘ₋₁nᵐ⁻¹) rⁿ, introducing polynomial factors in n.
- ✓

  Initial conditions determine the unknown constants by solving a (usually small) linear system.
- ✓

  Complex roots are allowed; conjugate pairs combine to real sequences, often expressible with cos(nθ) and sin(nθ).
- ✓

  The largest-magnitude characteristic root often dictates asymptotic growth (unless its coefficient becomes 0 from initial conditions).
- ✓

  Recurrence thinking directly supports DP state design, algorithm analysis, and later tools like generating functions.

## Common Mistakes

- ✗

  Forgetting how many initial conditions are needed (order k needs k starting values) and trying to solve with too little information.
- ✗

  Writing the characteristic polynomial incorrectly (sign errors are common when moving terms to one side).
- ✗

  Ignoring repeated roots and incorrectly using aₙ = αrⁿ + βrⁿ instead of (α + βn)rⁿ.
- ✗

  Solving for constants with the wrong indexing (mixing a₀ vs a₁ start) and getting a consistent-looking but incorrect closed form.

## Practice

easy

Solve: aₙ = 4aₙ₋₁ − 4aₙ₋₂ with a₀ = 2, a₁ = 8.

**Hint:** Find the characteristic polynomial and check whether it has a repeated root. If it does, use aₙ = (α + βn)rⁿ.

Show solution

Assume aₙ = rⁿ:

r² = 4r − 4 ⇒ r² − 4r + 4 = 0 ⇒ (r − 2)² = 0.

Repeated root r = 2 with multiplicity 2 ⇒ aₙ = (α + βn)2ⁿ.

Use a₀ = 2:

2 = (α + 0)2⁰ = α ⇒ α = 2.

Use a₁ = 8:

8 = (α + β)2¹ = (2 + β)2 ⇒ 2 + β = 4 ⇒ β = 2.

So aₙ = (2 + 2n)2ⁿ.

medium

Solve: aₙ = 3aₙ₋₁ + 10aₙ₋₂ with a₀ = 0, a₁ = 1.

**Hint:** Factor the characteristic polynomial r² − 3r − 10. Then solve for α, β using n = 0 and n = 1.

Show solution

Characteristic equation:

r² = 3r + 10 ⇒ r² − 3r − 10 = 0 ⇒ (r − 5)(r + 2) = 0.

Roots: r₁ = 5, r₂ = −2.

General solution: aₙ = α·5ⁿ + β·(−2)ⁿ.

Use a₀ = 0:

0 = α + β ⇒ β = −α.

Use a₁ = 1:

1 = 5α + (−2)β = 5α − (−2)α = 7α ⇒ α = 1/7.

Then β = −1/7.

So aₙ = (1/7)·5ⁿ − (1/7)·(−2)ⁿ = (5ⁿ − (−2)ⁿ)/7.

hard

A recurrence has characteristic polynomial P(r) = (r − 1)³(r + 2). Write the most general real-form solution for aₙ (do not solve for constants).

**Hint:** A root r with multiplicity m contributes (β₀ + β₁n + ⋯ + βₘ₋₁nᵐ⁻¹)rⁿ. Combine contributions from each distinct root.

Show solution

Root r = 1 has multiplicity 3 ⇒ contribution: (α + βn + γn²)·1ⁿ = α + βn + γn².

Root r = −2 has multiplicity 1 ⇒ contribution: δ(−2)ⁿ.

General solution:

aₙ = (α + βn + γn²) + δ(−2)ⁿ.

## Connections

Next nodes you can tackle:

- •[Dynamic Programming](/tech-tree/dynamic-programming/) — recurrences define DP transitions; you’ll learn to compute efficiently and reason about state.
- •[Generating Functions](/tech-tree/generating-functions/) — an alternative algebraic method for solving recurrences and counting problems.
- •[Divide and Conquer](/tech-tree/divide-conquer/) — many runtimes form recurrences; you’ll learn systematic solution and bounding techniques.

Quality: B (4.0/5)

[← back to tree](/tech-tree/)[browse all →](/tech-tree/inventory/)
