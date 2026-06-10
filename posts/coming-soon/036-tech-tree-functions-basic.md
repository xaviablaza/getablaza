---
title: Functions
description: Mappings from inputs to outputs. Domain, range, and function notation.
date: '2026-07-01'
scheduled: '2026-08-05'
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
inspiration_url: https://templeton.host/tech-tree/functions-basic/
inspiration_category: tech-tree
---

> Source-copy draft imported from [https://templeton.host/tech-tree/functions-basic/](https://templeton.host/tech-tree/functions-basic/). Names, domain references, and local media paths were adapted for Xavi Ablaza / getablaza.com.

[←Back to Tech Tree](/tech-tree/)

[inventory](/tech-tree/inventory/)[coverage](/tech-tree/coverage/)

# Functions

Discrete MathDifficulty: ★☆☆☆☆Depth: 0Unlocks: 132

Mappings from inputs to outputs. Domain, range, and function notation.

## Interactive Visualization

⏮◀◀▶▶STEP0.25x1xZOOM

t=0s

## Core Concepts

- -Mapping: each input is assigned exactly one output
- -Domain: the set of allowable inputs
- -Range (image): the set of outputs actually produced by the mapping

## Key Symbols & Notation

f: A -> B (function f from set A to set B)f(x) (value of f at input x)

## Essential Relationships

- -For every x in the Domain A, f(x) is a single element of B; the set of all such f(x) values equals the Range (a subset of B)

## Unlocks (5)

[Limitslvl 2](/tech-tree/limits/)[Random Variableslvl 2](/tech-tree/random-variables/)[Recursionlvl 2](/tech-tree/recursion/)[Relationslvl 2](/tech-tree/relations/)[Hash Tableslvl 2](/tech-tree/hash-tables/)

Advanced Learning Details

### Graph Position

6

Depth Cost

132

Fan-Out (ROI)

51

Bottleneck Score

0

Chain Length

### Cognitive Load

6

Atomic Elements

23

Total Elements

L0

Percentile Level

L4

Atomic Level

### All Concepts (10)

- - Function as a mapping: a rule that associates each allowed input with exactly one output
- - Input (independent variable): the value given to the function
- - Output (dependent variable): the value produced by the function for a given input
- - Domain: the set of allowable inputs for the function
- - Range (image): the set of outputs that actually occur from applying the function to the domain
- - Function notation and naming: using a symbol (e.g., f) to denote a particular mapping
- - Evaluation of a function: computing the output corresponding to a specific input (finding f(x))
- - Ordered-pair view: representing a function as a set of ordered pairs (x, f(x))
- - Multiple representations: the same function can be given by an algebraic rule, a table, a mapping diagram, or a graph
- - Determinism/uniqueness property: for each input in the domain there is one and only one output

### Teaching Strategy

Deep-dive lesson - accessible entry point but dense material. Use worked examples and spaced repetition.

A “function” is the idea behind almost everything in math and computing: you give a rule an input, and it gives you an output. Once you can name inputs, name outputs, and write the rule down clearly, you can build calculus, probability, recursion, and data structures on top of it.

TL;DR:

A function is a mapping that assigns **each allowed input exactly one output**. The **domain** is the set of allowed inputs. The **range** (also called the image) is the set of outputs the function actually produces. We write a function as f(x)f(x)f(x) (“f of x”).

## What Is a Function?

### Why we care

In both math and programming, we constantly model a situation where one thing depends on another:

- •Your total cost depends on how many items you buy.
- •A password checker returns “accept” or “reject” based on the password.
- •A conversion rule turns Celsius into Fahrenheit.

A **function** is the cleanest way to describe that dependency.

### Core idea (informal)

A function is a **rule** that takes an input and returns an output.

But math is picky about one key property:

> **A function must give exactly one output for each input in its domain.**

That means:

- •If the input is allowed, the output is determined (no ambiguity).
- •The same input cannot map to two different outputs.

### First examples

1) **Doubling**: input a number, output twice that number.

- •Input: 3 → Output: 6
- •Input: 0 → Output: 0

2) **Square**: input a number, output its square.

- •Input: −2 → Output: 4
- •Input: 5 → Output: 25

### A non-example (not a function)

Suppose we claim a “rule” that maps 1 to both 2 and 3.

- •Input: 1 → Output: 2
- •Input: 1 → Output: 3

This violates the “exactly one output” requirement. So it is **not** a function.

### Function notation

We often name a function with a letter like fff.

- •f(x)f(x)f(x) means “the output of function fff when the input is xxx.”

Example:

Let f(x)=2xf(x) = 2xf(x)=2x.

- •f(3)=2⋅3=6f(3) = 2·3 = 6f(3)=2⋅3=6
- •f(0)=0f(0) = 0f(0)=0

Notice the pattern: the parentheses are **not multiplication**. f(3)f(3)f(3) is “evaluate fff at 3.”

### A gentle checkpoint (before formalism)

To decide if something is a function, ask:

1) What are the allowed inputs?

2) For each allowed input, is there exactly one output?

If yes, it’s a function.

## Domain and Range (Image): Naming Inputs and Outputs

### Why these sets matter

A big source of confusion is that a “rule” is not complete until you know what inputs it is willing to accept.

Example: f(x)=1xf(x) = \frac{1}{x}f(x)=x1​.

- •If we try x=0x = 0x=0, we get division by zero, which is not allowed in ordinary arithmetic.

So we need vocabulary for “what inputs are allowed” and “what outputs come out.”

### Domain

The **domain** of a function is the set of inputs you are allowed to plug in.

Examples:

- •For f(x)=2xf(x)=2xf(x)=2x over real numbers, the domain can be all real numbers (ℝ).
- •For f(x)=1xf(x)=\frac{1}{x}f(x)=x1​ over real numbers, the domain is all real numbers except 0.
- •In set notation: domain = {x ∈ ℝ : x ≠ 0}

In discrete math and CS, the domain is often a finite or countable set:

- •domain = {0,1} (bits)
- •domain = strings over an alphabet
- •domain = set of usernames in a database

### Range (also called image)

The **range** is the set of outputs the function actually produces when you feed it every input in the domain.

Example 1:

Let f(x)=x2f(x)=x^2f(x)=x2 with domain ℝ.

- •Outputs are never negative.
- •Range = {y ∈ ℝ : y ≥ 0}

Example 2:

Let the domain be {−1, 0, 2} and define g(x)=x+1g(x)=x+1g(x)=x+1.

- •g(−1)=0
- •g(0)=1
- •g(2)=3
- •Range = {0,1,3}

### Breathing room: domain vs range in one sentence

- •**Domain**: what you can put in.
- •**Range**: what you can get out.

### A common subtlety (kept light): range vs “all possible outputs”

Sometimes people informally say “range” when they mean “all outputs we *intend* the function to land in.” In more formal math, there is also the **codomain** (the target set). To keep difficulty at 1/5, we’ll focus on:

- •Domain (allowed inputs)
- •Range/image (outputs actually produced)

If you later see notation like f:A→Bf: A \to Bf:A→B, the set BBB is often the *codomain*, while the *range* is the subset of BBB that fff actually hits. You don’t need that distinction yet to use functions correctly day-to-day.

### Function tables and mappings (discrete viewpoint)

In discrete math, a function from a small set can be shown as a table.

Example:

Let domain A = {a,b,c}. Define fff by:

| x | f(x) |
| --- | --- |
| a | 2 |
| b | 2 |
| c | 5 |

This is a valid function because each input appears once and has exactly one output.

Note: multiple inputs are allowed to share the same output (a and b both map to 2). That is still a function.

## Function Notation and Evaluation: Reading and Using f(x)

### Why notation matters

Function notation is like a tiny language. If you can read and write it, you can:

- •compute outputs,
- •specify rules precisely,
- •describe algorithms and transformations clearly.

### Defining a function with a formula

A common way to define a function is with an equation like:

- •f(x)=2x+1f(x)=2x+1f(x)=2x+1

This means: take input xxx, multiply by 2, then add 1.

Evaluate at a specific input:

- •f(4)=2⋅4+1=9f(4)=2·4+1=9f(4)=2⋅4+1=9

### Defining a function with a description

You can also define a function in words, especially in CS.

Example:

- •Input: a string s
- •Output: the length of s

In math, we might call it ℓ(s)\ell(s)ℓ(s) and write ℓ("cat")=3\ell(\text{"cat"})=3ℓ("cat")=3.

### Defining a function by cases (piecewise)

Sometimes a single formula doesn’t cover the rule cleanly. Then we use a piecewise definition.

Example:

∣x∣={xif x≥0−xif x<0|x| =
\begin{cases}
x & \text{if } x \ge 0 \\
-x & \text{if } x < 0
\end{cases}∣x∣={x−x​if x≥0if x<0​

Evaluate:

- •|5| = 5 (because 5 ≥ 0)
- •|−5| = −(−5) = 5 (because −5 < 0)

### A quick checkpoint: “exactly one output” with piecewise rules

A piecewise rule is still a function if:

- •every input in the domain matches at least one case, and
- •no input matches two conflicting cases.

Example of a problem:

h(x)={0if x≥01if x≥0h(x)=
\begin{cases}
0 & \text{if } x \ge 0 \\
1 & \text{if } x \ge 0
\end{cases}h(x)={01​if x≥0if x≥0​

If x = 2, which output should it give—0 or 1? Not a function (as written).

### Inputs don’t have to be numbers

In discrete math, inputs and outputs are often objects.

Examples:

- •fff maps people → their birthdays
- •ggg maps files → their sizes (in bytes)
- •hhh maps web pages → their URLs

The function idea is the same: each input has one associated output.

### (Optional mental model) Functions as machines

Imagine a machine labeled fff:

- •You feed in x.
- •The machine returns f(x).

If you feed in the same x again, you must get the same output again (for a deterministic function).

## Applications and Connections: Where Functions Show Up in CS and Math

### Why this node unlocks so much

Once you understand “input → output with a rule,” many topics become simple variations:

- •calculus: what happens as inputs approach a point
- •probability: mapping outcomes to numbers
- •recursion: defining outputs in terms of smaller inputs
- •data structures: mapping keys to values

Below are a few concrete connections.

### Limits (preview)

In calculus, you study what value a function approaches as the input approaches a point.

Even stating a limit requires function language:

- •“As x approaches 0, what does f(x) approach?”

You can’t talk about that without knowing what f(x)f(x)f(x) means and what inputs are allowed.

### Random variables (preview)

A **random variable** is literally a function in the math sense:

- •It maps each outcome of an experiment to a number.

Example:

- •Flip two coins.
- •Outcomes: {HH, HT, TH, TT}
- •Define XXX = number of heads.
- •X(HH)=2, X(HT)=1, X(TH)=1, X(TT)=0

That’s a function from outcomes → {0,1,2}.

### Recursion (preview)

A recursive definition defines a function using itself on smaller inputs.

Example idea:

- •factorial: n! = n·(n−1)! with base case 0! = 1

To read that, you must be comfortable with function evaluation and domain restrictions (e.g., nonnegative integers).

### Relations vs functions (preview)

A **relation** can connect an input to many outputs.

A **function** is a special kind of relation that connects each input to exactly one output.

This is why functions are often introduced early in discrete math: they’re “well-behaved” relations.

### Hash tables (preview)

A hash function maps a key (like a string) to a bucket index (like an integer).

- •input: key
- •output: integer index

Even though collisions exist (different keys can map to the same output), it is still a function because:

- •each key maps to exactly one index.

### Summary table: how to recognize the “function pattern”

| Area | Typical input | Typical output | Function idea |
| --- | --- | --- | --- |
| Algebra | number x | number f(x) | compute a value |
| Probability | outcome ω | number X(ω) | measure an outcome |
| Algorithms | instance | answer | compute a result |
| Data structures | key | bucket/value | lookup mapping |

Notice the repeating theme: define the domain, ensure one output per input, then use the notation to compute and reason.

## Worked Examples (3)

### Evaluate a function and identify domain/range (finite set)

Let the domain be A = {−1, 0, 2, 4}. Define f(x)=x2+1f(x)=x^2+1f(x)=x2+1 for x ∈ A.

1) Compute f(x) for each x in A.

2) State the range (set of outputs).

1. Compute each output:

   - •f(−1) = (−1)² + 1 = 1 + 1 = 2
   - •f(0) = 0² + 1 = 0 + 1 = 1
   - •f(2) = 2² + 1 = 4 + 1 = 5
   - •f(4) = 4² + 1 = 16 + 1 = 17
2. Collect outputs into a set (remove duplicates if any):

   Range = {2, 1, 5, 17} = {1,2,5,17}

**Insight:** On a finite domain, the range is easy: evaluate at every input and list the outputs. The range is a set, so duplicates collapse to one element.

### Decide whether a mapping is a function

Consider the mapping from A = {a,b,c} to numbers defined by the pairs:

(a, 1), (b, 1), (c, 2).

Then consider a second mapping defined by:

(a, 1), (a, 2), (c, 2).

For each mapping, decide if it is a function from A to numbers.

1. Mapping 1: (a,1), (b,1), (c,2)

   Check each input in A:

   - •a appears once → one output (1)
   - •b appears once → one output (1)
   - •c appears once → one output (2)

   So each input has exactly one output ⇒ this IS a function.
2. Mapping 2: (a,1), (a,2), (c,2)

   Check each input in A:

   - •a appears twice with two different outputs (1 and 2) ⇒ violates “exactly one output”

   Therefore this is NOT a function as a mapping from A.

   (Also, b has no output listed, so even “at least one output” fails if we require the whole domain A.)

**Insight:** Two common ways to fail being a function: (1) one input maps to two outputs, or (2) an input in the declared domain has no output at all.

### Domain restriction example: $f(x)=\frac{1}{x}$

Let f(x)=1xf(x)=\frac{1}{x}f(x)=x1​.

1) Explain why x = 0 cannot be in the domain (over real numbers).

2) Compute f(2), f(−4), and describe the range over the domain ℝ \ {0}.

1. Check x = 0:

   f(0) = 1/0 is undefined (division by zero). So 0 must be excluded from the domain.

   Domain (over ℝ) is {x ∈ ℝ : x ≠ 0}.
2. Evaluate:

   - •f(2) = 1/2
   - •f(−4) = −1/4
3. Describe the range:

   Can the output ever be 0?

   If 1/x = 0, then 1 = 0·x = 0, impossible.

   So 0 is never produced.

   Range is {y ∈ ℝ : y ≠ 0}.

**Insight:** Domain restrictions often come from “operations that can break,” like division by zero or square roots of negative numbers (over reals). The range can also exclude values for algebraic reasons.

## Key Takeaways

- ✓

  A function is a mapping that assigns **each input in its domain exactly one output**.
- ✓

  Function notation: f(x)f(x)f(x) means “the output of f at input x,” not multiplication.
- ✓

  The **domain** is the set of allowed inputs.
- ✓

  The **range/image** is the set of outputs actually produced by the function.
- ✓

  Different inputs may share the same output; that does not violate being a function.
- ✓

  A mapping fails to be a function if an input has two different outputs or if some input in the declared domain has no output.
- ✓

  Functions can map non-numeric objects too (strings, people, files, outcomes).

## Common Mistakes

- ✗

  Thinking f(x)f(x)f(x) means f⋅xf·xf⋅x (multiplication) instead of “evaluate f at x.”
- ✗

  Forgetting to state or check the domain, especially when formulas can be undefined (like division by zero).
- ✗

  Assuming a function must have different outputs for different inputs (it doesn’t).
- ✗

  Mixing up domain and range: domain is what goes in; range is what comes out.

## Practice

easy

Let f(x)=3x−2f(x)=3x-2f(x)=3x−2. Compute f(0), f(2), and f(−1).

**Hint:** Substitute each input into 3x−2 and simplify.

Show solution

f(0)=3·0−2=−2

f(2)=3·2−2=6−2=4

f(−1)=3·(−1)−2=−3−2=−5

easy

Domain/range practice: Domain A = {1,2,3,4}. Define g(x)g(x)g(x) by the table: g(1)=2, g(2)=2, g(3)=5, g(4)=5. What is the range of g?

**Hint:** List the outputs and remove duplicates.

Show solution

Outputs are {2,2,5,5}. As a set, the range is {2,5}.

medium

Is it a function? Consider the relation on A = {a,b,c} given by pairs (a,1), (b,2), (b,3), (c,4). Decide whether this is a function from A to numbers.

**Hint:** Check whether any input has more than one output, and whether every input has at least one output.

Show solution

Input b maps to both 2 and 3, so the mapping gives two outputs for the same input. Therefore it is NOT a function from A.

## Connections

- •[Relations](/tech-tree/relations/)
- •[Limits](/tech-tree/limits/)
- •[Random Variables](/tech-tree/random-variables/)
- •[Recursion](/tech-tree/recursion/)
- •[Hash Tables](/tech-tree/hash-tables/)

Quality: B (4.2/5)

[← back to tree](/tech-tree/)[browse all →](/tech-tree/inventory/)
