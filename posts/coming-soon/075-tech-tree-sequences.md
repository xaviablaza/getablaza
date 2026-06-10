---
title: Sequences
description: Ordered lists of numbers following patterns. Arithmetic and geometric sequences.
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
inspiration_url: https://templeton.host/tech-tree/sequences/
inspiration_category: tech-tree
---

> Source-copy draft imported from [https://templeton.host/tech-tree/sequences/](https://templeton.host/tech-tree/sequences/). Names, domain references, and local media paths were adapted for Xavi Ablaza / getablaza.com.

[←Back to Tech Tree](/tech-tree/)

[inventory](/tech-tree/inventory/)[coverage](/tech-tree/coverage/)

# Sequences

Discrete MathDifficulty: ★☆☆☆☆Depth: 0Unlocks: 12

Ordered lists of numbers following patterns. Arithmetic and geometric sequences.

## Interactive Visualization

⏮◀◀▶▶STEP0.25x1xZOOM

t=0s

## Core Concepts

- -Sequence as an indexed ordered list: each term has a position n and value a\_n (function from positive integers to numbers)
- -Characterization of patterns by constant change: sequences can follow a constant additive change (difference) or a constant multiplicative change (ratio)

## Key Symbols & Notation

a\_n (term at index n)

## Essential Relationships

- -Arithmetic sequence: recurrence a\_{n+1} = a\_n + d (explicit a\_n = a\_1 + (n-1)d)
- -Geometric sequence: recurrence a\_{n+1} = r \* a\_n (explicit a\_n = a\_1 \* r^(n-1))

## Unlocks (3)

[Recurrence Relationslvl 3](/tech-tree/recurrence-relations/)[Generating Functionslvl 3](/tech-tree/generating-functions/)[Taylor Serieslvl 3](/tech-tree/taylor-series/)

## Referenced by (27)

Where this concept shows up in the operating-finance and personal-finance graphs.

### From Business (22)

[personal financeBusiness

Compound interest, amortization schedules, and the FIRE 4% rule all derive from geometric series formulas - this is the exact mathematical foundation for compound-interest, interest-rate-math, and fire-math](/business/personal-finance/)[savingsBusiness

Fixed monthly savings is an arithmetic sequence of contributions; with interest, the future value formula is a geometric series sum (the annuity formula), making sequences the direct mathematical foundation](/business/savings/)[ReturnsBusiness

Geometric sequences are the direct mathematical model for returns compounding over multiple periods - each period's value is a function of the prior period's, forming the core quantitative structure of multi-period asset returns](/business/returns/)[interest rateBusiness

Geometric sequences are the mathematical model of compounding - balance\_n = balance\_0 \* (1 + r/12)^n is a geometric sequence, and understanding this structure is what makes interest rate math precise rather than intuitive](/business/interest-rate/)[compound interestBusiness

Compound interest is a geometric sequence (A₀·(1+r)^n); understanding arithmetic vs geometric sequences is the direct mathematical formalization of why compounding is exponential, not linear](/business/compound-interest/)[Discount RateBusiness

DCF valuation is a geometric series: sum of CF\_t / (1+r)^t. Understanding geometric sequence convergence and partial sums is the direct mathematical foundation for discounting cash flows.](/business/discount-rate/)[CompoundingBusiness

Compound growth is a geometric sequence A(1+r)^n; understanding arithmetic vs geometric sequences is the mathematical foundation for why small rate differentials produce large terminal wealth gaps over long horizons](/business/compounding/)[Net RateBusiness

Geometric sequences formalize the two regimes: common ratio > 1 produces compounding growth, < 1 produces exponential decay. The net rate determines which regime the sequence follows](/business/net-rate/)[AccumulationBusiness

Geometric sequences are the mathematical model underlying accumulation: V(t) = V(0) \* (1+r)^t. Understanding geometric growth vs arithmetic growth is the formal basis for why accumulation accelerates over time.](/business/accumulation/)[Rule of 72Business

Rule of 72 solves for n in the geometric sequence a·r^n = 2a. Geometric sequences are the discrete math foundation of all compounding.](/business/rule-of-72/)[APRBusiness

Periodic compounding produces geometric sequences - balance after n periods is P\*(1+r/n)^n, and APY = (1+APR/n)^n - 1 is a direct geometric sequence application](/business/apr/)[APYBusiness

Compound interest growth is a geometric sequence: balance after each period is A \* (1 + r/n). Understanding geometric sequences and their closed-form sums is the mathematical prerequisite for deriving APY and amortization schedules.](/business/apy/)[Physical CapitalBusiness

Depreciation schedules are arithmetic sequences (straight-line) or geometric sequences (declining balance) - the pattern-recognition math that makes book value calculations mechanical](/business/physical-capital/)[AmortizationBusiness

An amortization schedule is a geometric sequence - the interest portion decays and the principal portion grows geometrically across payments, following closed-form series formulas](/business/amortization/)[Liability PaydownBusiness

Arithmetic vs geometric sequences formalize the core asymmetry: asset growth follows geometric compounding (multiplicative, returns on returns) while fixed-rate liability paydown follows a different trajectory where the interest saved is linear in the amount repaid](/business/liability-paydown/)[DiscountingBusiness

Discounted return G\_t = Σ γ^k · r\_{t+k} is a geometric series. Convergence condition |γ| < 1 is what makes infinite-horizon value functions finite and well-defined. Understanding geometric sequence summation is the direct mathematical prerequisite.](/business/discounting/)[present valueBusiness

Present value of a reward stream is the partial sum of a geometric series (gamma^0\*r\_0 + gamma^1\*r\_1 + ...). The convergence condition for geometric series (|ratio| < 1) is exactly why the discount factor must satisfy gamma in [0,1).](/business/present-value/)[Discounted Cash FlowBusiness

DCF is a finite geometric series: PV = Σ CF\_t / (1+r)^t. The closed-form for constant cash flows comes directly from the geometric series sum formula.](/business/discounted-cash-flow/)[discounted returnBusiness

Discounted return is an infinite geometric series with common ratio gamma. Convergence requires |gamma| < 1, which is the standard geometric series convergence condition. Understanding why the sum is finite and how gamma controls the horizon is pure sequence theory.](/business/discounted-return/)[Net Present ValueBusiness

Geometric sequences are the mathematical backbone of discounting - each period's discount factor is (1+r)^{-t}, forming a geometric series whose closed-form sum gives the annuity formula used in most NPV shortcuts.](/business/net-present-value/)[Internal Rate of ReturnBusiness

Discount factors form a geometric sequence (1, 1/(1+r), 1/(1+r)^2, ...) and cash flow streams are the sequences being discounted - IRR solves for the common ratio](/business/internal-rate-of-return/)[Payback PeriodBusiness

Discount factors 1/(1+r)^t form a geometric sequence and NPV is the dot product of a cash flow stream with that sequence - geometric series math is the direct foundation for discounting and annuity formulas](/business/payback-period/)

### From Money (5)

[Compound InterestMoney

Compound growth is a geometric sequence: A(1+r)^n](/money/compound-interest/)[Interest Rate MathMoney

Amortization follows a recursive sequence of principal and interest splits](/money/interest-rate-math/)[Mortgage MathMoney

Amortization schedule is a recursive sequence of principal and interest](/money/mortgage-basics/)[15% Savings RateMoney

15% target derives from geometric growth to a retirement multiple](/money/target-savings-rate/)[FIRE MathMoney

The 25x rule derives from the geometric series of portfolio withdrawals](/money/fire-math/)

Advanced Learning Details

### Graph Position

5

Depth Cost

12

Fan-Out (ROI)

7

Bottleneck Score

0

Chain Length

### Cognitive Load

5

Atomic Elements

38

Total Elements

L2

Percentile Level

L3

Atomic Level

### All Concepts (16)

- - Sequence: an ordered list of numbers indexed by position n
- - Index (n): the position number that identifies a term in a sequence
- - Nth-term notation a\_n: symbol meaning ‘the term at position n’
- - Finite vs infinite sequence: whether the list ends or continues indefinitely
- - Explicit (closed-form) nth-term formula: a direct formula for a\_n in terms of n
- - Recursive (recurrent) definition: a\_n defined using previous term(s) (e.g., a\_{n+1} in terms of a\_n)
- - Arithmetic sequence: a sequence where consecutive terms differ by a constant
- - Geometric sequence: a sequence where consecutive terms have a constant ratio
- - First term (a\_1 or a\_0): the initial value that seeds the sequence
- - Common difference (d): the constant increment in an arithmetic sequence
- - Common ratio (r): the constant multiplier in a geometric sequence
- - Consecutive-term relation: expressing how a\_{n+1} is obtained from a\_n
- - Sequence notation {a\_n} or (a\_n)\_{n=1}^∞ and use of ellipsis (…) to indicate continuation
- - Starting-index convention: sequences can be indexed from 1 or from 0
- - Monotonicity of sequences: increasing, decreasing, or constant behavior
- - Sign oscillation in geometric sequences when the common ratio is negative

### Teaching Strategy

Self-serve tutorial - low prerequisites, straightforward concepts.

Many “patterns” in math become clearer the moment you stop thinking of them as a pile of numbers and start thinking of them as a function: you feed in an index n, and out comes the n-th term aₙ. That shift is what sequences are about.

TL;DR:

A sequence is an ordered list of numbers where each term has an index n and a value aₙ. Two foundational families are arithmetic sequences (constant difference d) and geometric sequences (constant ratio r). You can describe sequences explicitly (aₙ as a formula in n) or recursively (each term from previous ones).

## What Is a Sequence?

### Why this matters

In programming, you often handle arrays, lists, streams, and time series. In mathematics, a **sequence** is the clean, precise version of that idea: an ordered list where order is not optional—it is the point.

A big payoff of learning sequences early is that they become the common language for later topics:

- •**Recurrence relations** define aₙ in terms of earlier terms.
- •**Generating functions** package all aₙ into one object.
- •**Taylor series** are sequences of coefficients that approximate functions.

### Definition (with intuition)

A **sequence** is a function whose input is an index and whose output is a number.

Most commonly, indices come from the positive integers:

- •n ∈ {1, 2, 3, …}

We write the value at index n as **aₙ** (read “a sub n”).

So you can think of a sequence as:

- •**a**: ℕ⁺ → ℝ (or → ℤ, or → ℂ, depending on the context)
- •n ↦ aₙ

### Ordered list viewpoint

You’ll also see sequences written as an ordered list:

- •(a₁, a₂, a₃, …)

The parentheses emphasize order: (1, 2) ≠ (2, 1).

### Indexing conventions (don’t get tripped up)

Different fields start counting at different places:

- •In many math texts: start at n = 1.
- •In computer science: arrays often start at index 0.

Both are valid. What matters is that you **declare** your indexing.

Example:

- •If aₙ = 2n, then a₁ = 2, a₂ = 4, a₃ = 6, …
- •If you instead start at n = 0, then a₀ = 0, a₁ = 2, a₂ = 4, …

### A sequence is not necessarily “patterned”

Many sequences follow a simple rule, but a sequence can be any mapping from indices to values. For instance:

- •aₙ = 0 if n is even, and aₙ = 1 if n is odd
- •aₙ = the n-th digit of π

This lesson focuses on two foundational “patterned” types:

- •**Arithmetic sequences**: constant additive change
- •**Geometric sequences**: constant multiplicative change

### Quick vocabulary

| Term | Meaning |
| --- | --- |
| index n | position in the sequence |
| term aₙ | value at position n |
| explicit formula | aₙ written directly as a function of n |
| recursive definition | aₙ defined using earlier terms |

This vocabulary will matter when you later learn recurrence relations and series.

## Core Mechanic 1: Arithmetic Sequences (Constant Difference)

### Why arithmetic sequences are a “first pattern”

If you watch how something changes over time and the change is **constant**, you are in arithmetic-sequence territory.

Examples in the real world:

- •Saving a fixed amount of money each month
- •Moving at constant velocity: position increases by a constant distance per unit time
- •A linear function sampled at equally spaced inputs

The defining idea is: each step adds the same amount.

### Definition

A sequence (aₙ) is **arithmetic** if the difference between consecutive terms is constant:

- •aₙ − aₙ₋₁ = d for all n ≥ 2

Here d is the **common difference**.

### Building intuition with a small table

Suppose a₁ = 5 and d = 3.

| n | aₙ |
| --- | --- |
| 1 | 5 |
| 2 | 8 |
| 3 | 11 |
| 4 | 14 |

Each time n increases by 1, the value increases by 3.

### Explicit formula (the “closed form”)

If you know the first term a₁ and the common difference d, you can compute any term without listing all previous ones.

Start from the pattern:

- •a₂ = a₁ + d
- •a₃ = a₁ + 2d
- •a₄ = a₁ + 3d

So in general:

- •aₙ = a₁ + (n − 1)d

This is worth deriving carefully because it’s the template for many later topics.

**Derivation (showing the work):**

We are adding d repeatedly:

- •from a₁ to a₂: add d once
- •from a₁ to a₃: add d twice
- •from a₁ to aₙ: add d (n − 1) times

So:

- •aₙ = a₁ + d + d + … + d (with (n − 1) copies of d)
- •aₙ = a₁ + (n − 1)d

### Detecting an arithmetic sequence from data

Given terms a₁, a₂, a₃, … compute consecutive differences:

- •Δₙ = aₙ − aₙ₋₁

If all Δₙ are equal, the sequence is arithmetic.

Example:

- •(2, 7, 12, 17, …)

Differences: 5, 5, 5, … ⇒ arithmetic with d = 5.

### Arithmetic sequences connect to linear functions

If aₙ = a₁ + (n − 1)d, that’s linear in n:

- •aₙ = dn + (a₁ − d)

So arithmetic sequences are essentially “linear growth” indexed by integers.

### Sum of the first n terms (a very common task)

You will frequently want:

- •Sₙ = a₁ + a₂ + … + aₙ

For an arithmetic sequence, there is a famous formula:

- •Sₙ = n(a₁ + aₙ)/2

**Why this is true (pairing idea):**

Write the sum forward and backward:

Sₙ = a₁ + a₂ + … + aₙ₋₁ + aₙ

Sₙ = aₙ + aₙ₋₁ + … + a₂ + a₁

Add them termwise:

2Sₙ = (a₁ + aₙ) + (a₂ + aₙ₋₁) + … + (aₙ + a₁)

Each pair equals (a₁ + aₙ), and there are n pairs:

2Sₙ = n(a₁ + aₙ)

Divide by 2:

Sₙ = n(a₁ + aₙ)/2

You can also substitute aₙ = a₁ + (n − 1)d if you want Sₙ in terms of a₁, d, n.

### When arithmetic sequences fail

Not every “nice-looking” sequence is arithmetic.

Example:

- •(1, 2, 4, 7, 11, …)

Differences: 1, 2, 3, 4, … not constant ⇒ not arithmetic.

This is a key habit: **check the differences** rather than guessing.

## Core Mechanic 2: Geometric Sequences (Constant Ratio)

### Why geometric sequences are the “second pattern”

If something changes by a constant **percentage** (or constant factor), you get multiplicative growth or decay.

Examples:

- •Compound interest (multiply by 1.05 each period for 5% growth)
- •Population growth models (simplified)
- •Repeated halving/doubling in algorithms
- •Exponential functions sampled at equally spaced inputs

The defining idea is: each step multiplies by the same factor.

### Definition

A sequence (aₙ) is **geometric** if the ratio between consecutive terms is constant:

- •aₙ / aₙ₋₁ = r for all n ≥ 2 (assuming aₙ₋₁ ≠ 0)

Here r is the **common ratio**.

### Example table

Suppose a₁ = 3 and r = 2.

| n | aₙ |
| --- | --- |
| 1 | 3 |
| 2 | 6 |
| 3 | 12 |
| 4 | 24 |

Each step doubles.

### Explicit formula

From the pattern:

- •a₂ = a₁r
- •a₃ = a₁r²
- •a₄ = a₁r³

So in general:

- •aₙ = a₁ rⁿ⁻¹

**Derivation (showing the work):**

You multiply by r repeatedly:

- •from a₁ to a₂: multiply by r once
- •from a₁ to a₃: multiply by r twice
- •from a₁ to aₙ: multiply by r (n − 1) times

So:

- •aₙ = a₁ · r · r · … · r (with (n − 1) copies of r)
- •aₙ = a₁ rⁿ⁻¹

### Detecting a geometric sequence

Compute ratios:

- •ρₙ = aₙ / aₙ₋₁

If all ρₙ are equal (and denominators aren’t 0), it’s geometric.

Example:

- •(81, 27, 9, 3, …)

Ratios: 1/3, 1/3, 1/3, … ⇒ geometric with r = 1/3.

### Signs and special cases

- •If r is negative, the sequence alternates signs.

Example: a₁ = 2, r = −3 ⇒ (2, −6, 18, −54, …)

- •If 0 < r < 1, the terms shrink toward 0.
- •If r = 1, the sequence is constant: aₙ = a₁.
- •If r = 0, then a₂ = 0 and all later terms are 0.

### Sum of the first n terms

Let:

- •Sₙ = a₁ + a₂ + … + aₙ

For geometric sequences (r ≠ 1):

- •Sₙ = a₁(1 − rⁿ)/(1 − r)

**Derivation (showing the work):**

Start with:

Sₙ = a₁ + a₁r + a₁r² + … + a₁rⁿ⁻¹

Multiply both sides by r:

rSₙ = a₁r + a₁r² + … + a₁rⁿ

Subtract:

Sₙ − rSₙ = (a₁ + a₁r + … + a₁rⁿ⁻¹) − (a₁r + … + a₁rⁿ)

Everything cancels except the first term a₁ and the last term −a₁rⁿ:

(1 − r)Sₙ = a₁ − a₁rⁿ

Factor:

(1 − r)Sₙ = a₁(1 − rⁿ)

Divide:

Sₙ = a₁(1 − rⁿ)/(1 − r)

(If r = 1, then Sₙ = n a₁.)

### Infinite geometric series (a preview)

If |r| < 1, then rⁿ → 0 as n → ∞, and the sums approach a finite limit:

- •a₁ + a₁r + a₁r² + … = a₁/(1 − r)

You’ll revisit this idea later in generating functions and Taylor series.

## Application/Connection: Explicit vs Recursive Definitions (and Why This Node Unlocks More)

### Two ways to define a sequence

Sequences are often described in one of two styles:

1) **Explicit**: aₙ is given directly in terms of n.

- •Example (arithmetic): aₙ = a₁ + (n − 1)d
- •Example (geometric): aₙ = a₁ rⁿ⁻¹

2) **Recursive**: aₙ is given in terms of previous terms.

- •Example (arithmetic): a₁ = 5, and aₙ = aₙ₋₁ + 3 for n ≥ 2
- •Example (geometric): a₁ = 3, and aₙ = 2aₙ₋₁ for n ≥ 2

### Why recursion matters later

Recursive definitions are natural in algorithms (“do the next step from the previous step”) and in discrete math (“build the next object from smaller ones”). This is the doorway to:

- •**Recurrence Relations**: more complex recursion like aₙ = 3aₙ₋₁ − 2aₙ₋₂
- •**Generating Functions**: turning (a₀, a₁, a₂, …) into a power series A(x) = ∑ aₙ xⁿ
- •**Taylor Series**: coefficients (a₀, a₁, a₂, …) approximate a function locally

### A unifying viewpoint: “constant change”

Arithmetic and geometric sequences are special because their “change rule” is constant:

| Type | What stays constant? | Growth feel |
| --- | --- | --- |
| arithmetic | difference aₙ − aₙ₋₁ = d | linear |
| geometric | ratio aₙ / aₙ₋₁ = r | exponential |

This isn’t just classification—it helps you choose tools.

- •Constant differences ⇒ look for linear formulas.
- •Constant ratios ⇒ look for exponential formulas.

### Mini-connection to functions and sampling

If you sample a function at integer points, you get a sequence:

- •Let f(n) be a function; then define aₙ = f(n).

Examples:

- •If f(x) = 2x + 1, then aₙ = 2n + 1 is arithmetic (difference 2).
- •If f(x) = 3·2ˣ, then aₙ = 3·2ⁿ is geometric (ratio 2).

### Mini-connection to vectors (notation practice)

Later, you’ll often package multiple sequences into a vector sequence, like **x**ₙ ∈ ℝᵏ.

For example, a 2D position over time:

- •**x**ₙ = (xₙ, yₙ)

Even here, the same patterns can apply:

- •arithmetic-like: **x**ₙ = **x**₁ + (n − 1)**d** (constant step vector **d**)
- •geometric-like scaling: **x**ₙ = rⁿ⁻¹ **x**₁

You won’t need this vector form yet, but it shows how sequences generalize cleanly.

### What you should be able to do after this node

- •Interpret aₙ as “the value at index n”
- •Identify arithmetic sequences by constant differences
- •Identify geometric sequences by constant ratios
- •Write explicit formulas from a₁ and d or r
- •Compute partial sums Sₙ for arithmetic and geometric sequences

Those abilities are exactly the prerequisites for recurrence relations, generating functions, and series.

## Worked Examples (3)

### Worked Example 1: Identify the type and find an explicit formula

Given the sequence (4, 1, −2, −5, …), determine whether it is arithmetic or geometric, and find a formula for aₙ (assume indexing starts at n = 1).

1. Compute consecutive differences:

   a₂ − a₁ = 1 − 4 = −3

   a₃ − a₂ = (−2) − 1 = −3

   a₄ − a₃ = (−5) − (−2) = −3
2. The differences are constant (all are −3), so the sequence is arithmetic with common difference d = −3.
3. Use the arithmetic explicit formula:

   aₙ = a₁ + (n − 1)d
4. Substitute a₁ = 4 and d = −3:

   aₙ = 4 + (n − 1)(−3)

   aₙ = 4 − 3(n − 1)

   aₙ = 4 − 3n + 3

   aₙ = 7 − 3n
5. Check quickly:

   a₁ = 7 − 3(1) = 4 ✔

   a₂ = 7 − 3(2) = 1 ✔

   a₃ = 7 − 3(3) = −2 ✔

**Insight:** Constant differences signal linear behavior: aₙ ends up being a linear expression in n.

### Worked Example 2: Geometric growth and partial sums

A bacteria culture triples every hour. At hour 1, there are 500 bacteria. Model this as a geometric sequence and compute the total bacteria count added over the first 6 hours (i.e., S₆ = a₁ + … + a₆).

1. Tripling each hour means a constant ratio r = 3. Given a₁ = 500.
2. Write the explicit formula for a geometric sequence:

   aₙ = a₁ rⁿ⁻¹
3. Substitute:

   aₙ = 500 · 3ⁿ⁻¹
4. Compute S₆ using the geometric sum formula (r ≠ 1):

   Sₙ = a₁(1 − rⁿ)/(1 − r)

   So:

   S₆ = 500(1 − 3⁶)/(1 − 3)
5. Compute 3⁶ = 729:

   S₆ = 500(1 − 729)/(−2)

   S₆ = 500(−728)/(−2)

   S₆ = 500 · 364

   S₆ = 182000
6. Sanity check by listing terms:

   a₁ = 500

   a₂ = 1500

   a₃ = 4500

   a₄ = 13500

   a₅ = 40500

   a₆ = 121500

   Sum = 500 + 1500 + 4500 + 13500 + 40500 + 121500 = 182000 ✔

**Insight:** Geometric sums look messy if you add term-by-term, but multiplying by r and subtracting makes almost everything cancel.

### Worked Example 3: Convert between recursive and explicit forms (arithmetic)

A sequence is defined recursively by a₁ = 10 and aₙ = aₙ₋₁ + 4 for n ≥ 2. Find an explicit formula for aₙ and compute a₁₂.

1. Recognize that aₙ = aₙ₋₁ + 4 means the difference is constant: d = 4. So it is arithmetic.
2. Use the arithmetic explicit form:

   aₙ = a₁ + (n − 1)d
3. Substitute a₁ = 10 and d = 4:

   aₙ = 10 + (n − 1)4

   aₙ = 10 + 4n − 4

   aₙ = 4n + 6
4. Compute a₁₂:

   a₁₂ = 4(12) + 6 = 48 + 6 = 54
5. Quick recursive check (optional): each step adds 4, so after 11 steps you added 11·4 = 44; 10 + 44 = 54 ✔

**Insight:** Recursive arithmetic sequences unwrap into “start + (number of steps)·(step size)”, which becomes a₁ + (n − 1)d.

## Key Takeaways

- ✓

  A sequence is a function from indices to values; aₙ means “the term at index n”.
- ✓

  Order matters: (a₁, a₂, a₃, …) is not just a set of numbers.
- ✓

  Arithmetic sequences have constant difference: aₙ − aₙ₋₁ = d, leading to aₙ = a₁ + (n − 1)d.
- ✓

  Geometric sequences have constant ratio: aₙ / aₙ₋₁ = r, leading to aₙ = a₁ rⁿ⁻¹.
- ✓

  To detect arithmetic vs geometric from data: check differences vs ratios.
- ✓

  Sum formulas: arithmetic Sₙ = n(a₁ + aₙ)/2; geometric (r ≠ 1) Sₙ = a₁(1 − rⁿ)/(1 − r).
- ✓

  Explicit forms let you jump to aₙ directly; recursive forms describe step-by-step generation and lead into recurrence relations.

## Common Mistakes

- ✗

  Mixing up indexing (starting at n = 0 vs n = 1), causing off-by-one errors in formulas like aₙ = a₁ rⁿ⁻¹.
- ✗

  Assuming a sequence is arithmetic because the numbers “look linear” without actually checking differences.
- ✗

  Trying to check geometric behavior by differences instead of ratios (or forgetting ratios fail when a term is 0).
- ✗

  Using the geometric sum formula when r = 1 (it would divide by 0); in that case Sₙ = n a₁.

## Practice

easy

Determine whether (−1, 2, −4, 8, −16, …) is arithmetic or geometric. Find aₙ.

**Hint:** Try ratios aₙ/aₙ₋₁. Watch the sign.

Show solution

Compute ratios:

2/(−1) = −2

(−4)/2 = −2

8/(−4) = −2

Constant ratio r = −2 ⇒ geometric.

With a₁ = −1:

aₙ = a₁ rⁿ⁻¹ = (−1)(−2)ⁿ⁻¹.

medium

An arithmetic sequence has a₃ = 12 and a₁₀ = 40. Find a₁ and d, then write aₙ.

**Hint:** Use aₙ = a₁ + (n − 1)d to set up two equations.

Show solution

Use aₙ = a₁ + (n − 1)d.

a₃ = a₁ + 2d = 12

a₁₀ = a₁ + 9d = 40

Subtract the first from the second:

(a₁ + 9d) − (a₁ + 2d) = 40 − 12

7d = 28

d = 4

Then a₁ + 2(4) = 12 ⇒ a₁ + 8 = 12 ⇒ a₁ = 4.

So aₙ = 4 + (n − 1)4 = 4n.

hard

A geometric sequence has a₂ = 6 and a₅ = 48. Find a₁ and r, then compute S₅.

**Hint:** Write a₂ = a₁r and a₅ = a₁r⁴. Divide the equations to eliminate a₁.

Show solution

Given:

a₂ = a₁r = 6

a₅ = a₁r⁴ = 48

Divide the second by the first:

a₅/a₂ = (a₁r⁴)/(a₁r) = r³

So:

48/6 = r³

8 = r³

r = 2

Then a₁r = 6 ⇒ a₁(2) = 6 ⇒ a₁ = 3.

Now compute S₅ (r ≠ 1):

S₅ = a₁(1 − r⁵)/(1 − r)

= 3(1 − 2⁵)/(1 − 2)

= 3(1 − 32)/(−1)

= 3(−31)/(−1)

= 93.

(Checks: terms are 3, 6, 12, 24, 48; sum = 93.)

## Connections

Next nodes you can unlock and why they rely on sequences:

- •[Recurrence Relations](/tech-tree/recurrence-relations/) — A recurrence is a rule like aₙ = f(aₙ₋₁, aₙ₋₂, …). You must be comfortable with indexing and reading aₙ.
- •[Generating Functions](/tech-tree/generating-functions/) — Generating functions encode a sequence (a₀, a₁, …) into A(x) = ∑ aₙxⁿ; arithmetic and geometric sequences are common first examples.
- •[Taylor Series](/tech-tree/taylor-series/) — A Taylor series is built from a sequence of coefficients; understanding what “the n-th coefficient” means is essential.

Related foundational ideas (optional exploration later):

- •[Functions](/tech-tree/functions/) — A sequence is a special kind of function with integer inputs.
- •[Series](/tech-tree/series/) — Summing terms of sequences leads to partial sums and infinite series.

Quality: A (4.3/5)

[← back to tree](/tech-tree/)[browse all →](/tech-tree/inventory/)
