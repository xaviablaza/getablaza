---
title: Counting Principles
description: Addition and multiplication rules for counting possibilities.
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
permalink: /tech-tree/counting-basic/
---

[←Back to Tech Tree](/tech-tree/)

[inventory](/tech-tree/inventory/)[coverage](/tech-tree/coverage/)

# Counting Principles

Discrete MathDifficulty: ★☆☆☆☆Depth: 0Unlocks: 83

Addition and multiplication rules for counting possibilities.

## Interactive Visualization

⏮◀◀▶▶STEP0.25x1xZOOM

t=0s

## Core Concepts

- -Finite set cardinality (count of distinct outcomes)
- -Addition (sum) rule for counting disjoint alternatives
- -Multiplication (product) rule for counting independent sequential choices (Cartesian product)

## Key Symbols & Notation

|S| to denote the cardinality (number of elements) of set S

## Essential Relationships

- -|A ∪ B| = |A| + |B| when A and B are disjoint (addition rule)
- -|A × B| = |A| \* |B| (product rule for independent/ordered choices)

## Unlocks (2)

[Basic Probabilitylvl 1](/tech-tree/probability-basic/)[Permutationslvl 2](/tech-tree/permutations/)

Advanced Learning Details

### Graph Position

6

Depth Cost

83

Fan-Out (ROI)

31

Bottleneck Score

0

Chain Length

### Cognitive Load

6

Atomic Elements

25

Total Elements

L0

Percentile Level

L4

Atomic Level

### All Concepts (10)

- - Sum rule (addition rule): when two or more choices/cases are mutually exclusive, the total number of possibilities is the sum of the counts for each case
- - Product rule (multiplication rule): when a process consists of sequential stages with a fixed number of options at each stage, the total number of ordered outcomes is the product of the numbers of options at each stage
- - Fundamental Counting Principle: generalization of the product rule to any finite number of stages - multiply the counts for all stages to get the total number of ordered outcomes
- - Mutually exclusive (disjoint) cases: definitions and recognition of scenarios that cannot happen at the same time, enabling use of the sum rule
- - Independent stages/choices (in counting): the notion that the number of options at one stage does not depend on choices made at other stages, enabling straightforward multiplication
- - Cartesian product as a model for sequential choices: representing outcomes as ordered tuples formed by taking the Cartesian product of option-sets for each stage
- - Tree-diagram representation: using branching diagrams to enumerate sequential choices and visualize multiplication along branches and addition across alternative branches
- - Partitioning into cases: technique of breaking a counting problem into a set of disjoint cases to which the sum rule can be applied
- - Avoiding double counting: the requirement that cases must be disjoint (or corrected) before summing counts
- - Order matters vs order doesn't matter: recognition that product-rule counts correspond to ordered outcomes and that unordered counting requires different treatment

### Teaching Strategy

Deep-dive lesson - accessible entry point but dense material. Use worked examples and spaced repetition.

When problems ask “How many ways?”, you usually don’t need to list everything. You need the two counting principles that let you count outcomes safely: add when choices are alternatives, multiply when choices are steps.

TL;DR:

Use |S| to mean “how many outcomes are in set S.”

- •**Addition rule**: if choices are disjoint alternatives, total ways add.
- •**Multiplication rule**: if you make choices in sequence (a Cartesian product), total ways multiply.

The main skill is recognizing whether the situation is “either/or” (add) or “and then” (multiply), and checking overlap to avoid double-counting.

## What Is Counting Principles?

Counting principles are the basic rules that let you compute the size of a set of outcomes without listing them one by one.

### Why we care (motivation before formulas)

In computer science and math, you constantly face “space of possibilities” questions:

- •How many possible passwords are there?
- •How many test cases could an input have?
- •How many different outcomes does a random experiment have?

Listing every outcome is often impossible. Counting principles are a shortcut: they let you compute the **cardinality** of a finite set.

### Cardinality: the count of distinct outcomes

A **set** S is a collection of distinct elements (outcomes). The notation

- •|S| = the number of elements in S

Examples:

- •S = {a, b, c} ⇒ |S| = 3
- •T = {heads, tails} ⇒ |T| = 2
- •D = {1, 2, 3, 4, 5, 6} ⇒ |D| = 6

The word **distinct** matters: sets do not count duplicates.

### The two big ideas

Almost all “how many ways” problems at this level reduce to one of two patterns:

1) **Alternatives (either/or)** → **Addition rule**

2) **Sequential choices (and then)** → **Multiplication rule**

A good mental model is: outcomes are points in a space.

- •Alternatives correspond to a **union** of sets.
- •Sequential choices correspond to a **Cartesian product** of sets.

We will build both rules carefully, with examples, and we’ll practice diagnosing which rule applies.

### A quick preview (no pressure)

If A and B are sets of outcomes:

- •**Addition rule (disjoint union)**: if A ∩ B = ∅, then |A ∪ B| = |A| + |B|
- •**Multiplication rule (product)**: for choices A then B, the outcome set is A × B and |A × B| = |A| · |B|

Don’t worry if ∩, ∪, and × look unfamiliar: we’ll explain them as we go.

## Core Mechanic 1: The Addition (Sum) Rule for Disjoint Alternatives

### Why addition appears

Addition is the right operation when you have **alternatives**:

- •You choose **one** option from group A **or** one option from group B.

If the groups do not overlap (no outcome is counted in both), then total outcomes are just the combined count.

### Sets viewpoint: union and disjointness

Let A and B be sets of outcomes.

- •A ∪ B means “in A or in B (or both).”
- •A ∩ B means “in both A and B.”
- •A and B are **disjoint** if A ∩ B = ∅ (empty set).

When A and B are disjoint, there is no overlap, so nothing gets double-counted.

### The addition rule (disjoint union)

If A ∩ B = ∅, then:

This extends to more than two sets: if A₁, A₂, …, Aₖ are pairwise disjoint (no overlaps), then

### Example intuition: menu alternatives

Suppose you can choose:

- •a sandwich: 5 types
- •a salad: 3 types

If you must choose **exactly one** of these (sandwich or salad), and no item is both a sandwich and a salad, then

Total lunches = 5 + 3 = 8

The key phrase is “choose one of these categories.”

### The big danger: overlap (double-counting)

If A and B overlap (A ∩ B ≠ ∅), then |A| + |B| counts elements in the overlap twice.

At this node, your main task is to learn to **check disjointness**. If alternatives are not disjoint, you must either:

- •redesign the categories so they become disjoint, or
- •subtract the overlap (this becomes the inclusion–exclusion idea; you can keep it as a warning for now).

### Diagnosing addition vs multiplication

A useful checklist:

- •Are you selecting **one** option from several **categories**? (either/or) → likely addition.
- •Does choosing an option in category A prevent choosing an option in category B? → suggests alternatives.
- •Are the categories non-overlapping by definition? → disjoint.

### Disjointness is often “baked into the wording”

If a problem says:

- •“Choose a **weekday** or a **weekend day**”

Those are disjoint sets. But if it says:

- •“Choose a day that is **sunny** or **warm**”

A day can be both sunny and warm, so sets overlap.

### A small set-based derivation (why the formula is true)

If A and B are disjoint, every element of A ∪ B is either:

- •in A (counted once), or
- •in B (counted once)

So the total is the sum:

= (number of elements in A) + (number of elements in B)

= |A| + |B|

This is simple, but it’s the pattern you will reuse constantly.

### Quick comparison table

| Situation | What you’re doing | Set operation | Counting rule |
| --- | --- | --- | --- |
| Choose one from category A **or** one from category B | Alternatives | A ∪ B | If disjoint: | A ∪ B | = | A | + | B |  |
| Choose one from A **and then** one from B | Sequence of choices | A × B |  | A × B | = | A | · | B |  |

We’ll now build the multiplication rule, which is the workhorse for multi-step constructions like passwords, IDs, and experiment outcomes.

## Core Mechanic 2: The Multiplication (Product) Rule and Cartesian Products

### Why multiplication appears

Multiplication is the right operation when an outcome is built by making **several choices in sequence**:

- •pick something from A, **then** pick something from B, **then** pick something from C, …

Each complete outcome is a **combination of one choice from each step**.

### Sets viewpoint: ordered pairs and Cartesian product

If A is a set of first-step choices and B is a set of second-step choices, then the set of all two-step outcomes is

A × B = { (a, b) : a ∈ A and b ∈ B }

Important details:

- •(a, b) is an **ordered pair**: (a, b) ≠ (b, a) in general.
- •Even if A and B have overlapping labels, the pair keeps track of “first choice” vs “second choice.”

Example:

A = {R, G} (2 colors)

B = {S, M, L} (3 sizes)

A × B has 2·3 = 6 pairs:

(R,S), (R,M), (R,L), (G,S), (G,M), (G,L)

### The multiplication rule (product rule)

For finite sets A and B:

And for k steps with sets A₁, A₂, …, Aₖ:

### Why this is true (a careful counting argument)

Think of a table:

- •Rows correspond to choices a ∈ A (there are |A| rows)
- •Columns correspond to choices b ∈ B (there are |B| columns)

Each cell corresponds to exactly one pair (a, b). The number of cells is:

(number of rows) · (number of columns)

= |A| · |B|

So |A × B| = |A| · |B|.

### “Independent” in counting means “any can pair with any”

People often say “independent choices,” but in counting problems this usually means:

- •Every first-step option can be paired with every second-step option.

If some combinations are forbidden (constraints), then you can’t blindly multiply; you must adjust.

### Multiplication with constraints: still possible, but be explicit

Example: a 3-character code where the first character is a letter (26 choices) and the next two are digits (10 choices each).

Let

- •A₁ = letters, |A₁| = 26
- •A₂ = digits, |A₂| = 10
- •A₃ = digits, |A₃| = 10

Total codes:

= |A₁|·|A₂|·|A₃|

= 26 · 10 · 10

= 2600

Constraints example: “no repeated digits” would change the later step counts (10 then 9, etc.). You can still multiply, but the factors change because the set of allowed choices at step 3 depends on step 2.

### Addition + multiplication together (the common real case)

Many problems combine both rules:

- •you pick one of several formats (addition)
- •within a format, you pick pieces in sequence (multiplication)

You’ll practice this blend in worked examples.

### Another comparison table: what wording suggests what rule?

| Wording clue | Likely structure | Rule |
| --- | --- | --- |
| “either … or …” | alternatives (union) | add (if disjoint) |
| “choose one of the following types” | disjoint categories | add |
| “and then” / “followed by” / “for each” | sequential steps (product) | multiply |
| “format A or format B, then fill in details” | add outside, multiply inside | both |

At this point you have the two tools. Next we connect them to probability and permutations, where these rules become the backbone of larger formulas.

## Application/Connection: Building Sample Spaces (and Why This Unlocks Probability & Permutations)

### Why counting principles matter in probability

In basic probability (with equally likely outcomes), you often compute:

P(event E) = |E| / |Ω|

where Ω is the **sample space** (set of all possible outcomes).

Counting principles are how you find |Ω| and |E|.

#### Example: two coin flips

Let a coin flip outcome be in C = {H, T} with |C| = 2.

Two flips corresponds to C × C.

|C × C| = |C|·|C| = 2·2 = 4 outcomes:

(H,H), (H,T), (T,H), (T,T)

Now events like “exactly one head” can be counted as a subset.

### Why counting principles matter for permutations

Permutations are about **arrangements** (order matters). The multiplication rule is what builds factorial and permutation counts.

For example, how many ways to arrange 3 distinct items {a, b, c}?

You choose:

- •first position: 3 choices
- •second position: 2 choices (one item used)
- •third position: 1 choice

By multiplication:

3 · 2 · 1 = 6

That becomes 3!.

### A unifying picture: outcomes as structured objects

Many CS objects are built from smaller pieces:

- •strings of length n over an alphabet
- •IDs with a prefix and a number
- •choosing a path with stages

The multiplication rule counts “structured objects” when the structure is sequential. The addition rule counts “choose a type of structure” when there are multiple disjoint types.

### Counting as a design skill

If you can rewrite the problem as:

- •a union of disjoint sets (add), and/or
- •a Cartesian product of sets (multiply),

you can count it.

A helpful approach:

1) Define the outcome set precisely.

2) Split it into disjoint cases if needed.

3) Count each case with multiplication.

4) Add the case counts.

This is the same decomposition mindset used in algorithms: break a big problem into pieces that don’t overlap, count or compute each piece, combine results.

### Looking ahead

These principles unlock:

- •[Basic Probability](/tech-tree/probability-basic/): you’ll count sample spaces and events.
- •[Permutations](/tech-tree/permutations/): you’ll count ordered arrangements and derive n! and nPr.

Even when later topics become more complex (combinations, inclusion–exclusion), the mental habit you build here—**add for alternatives, multiply for stages**—remains the foundation.

## Worked Examples (3)

### Meal choice: add for alternatives, multiply for components

A cafeteria offers:

- •4 sandwiches
- •3 salads

If you choose exactly one main (sandwich or salad) and also choose 1 drink from 5 options, how many total meals are possible?

1. Define sets of mains:

   Let S be the set of sandwiches, |S| = 4.

   Let A be the set of salads, |A| = 3.
2. Because you choose a sandwich or a salad (and these categories do not overlap), treat as a disjoint union:

   Number of possible mains = |S ∪ A| = |S| + |A| = 4 + 3 = 7.
3. Define set of drinks:

   Let D be the set of drinks, |D| = 5.
4. A full meal is (main, drink), so outcomes correspond to (S ∪ A) × D.
5. Apply multiplication rule:

   = 7 · 5

   = 35.

**Insight:** Use addition to count disjoint main-course alternatives, then multiply because you make an additional drink choice for each main.

### License plate formats: add across formats, multiply within each

A system allows two disjoint license plate formats:

- •Format 1: 2 letters followed by 2 digits (LLDD)
- •Format 2: 3 letters followed by 1 digit (LLLD)

Assume 26 letters (A–Z) and 10 digits (0–9), repetition allowed. How many plates are possible total?

1. Count Format 1 using multiplication:

   Choices: 26 · 26 · 10 · 10

   So N₁ = 26² · 10².
2. Compute N₁:

   26² = 676

   10² = 100

   So N₁ = 676 · 100 = 67,600.
3. Count Format 2 using multiplication:

   Choices: 26 · 26 · 26 · 10

   So N₂ = 26³ · 10.
4. Compute N₂:

   26³ = 26 · 26² = 26 · 676 = 17,576

   So N₂ = 17,576 · 10 = 175,760.
5. Formats are disjoint (a plate cannot be both LLDD and LLLD), so add:

   Total = N₁ + N₂

   = 67,600 + 175,760

   = 243,360.

**Insight:** When there are multiple allowed “shapes” for outcomes, count each shape with multiplication, then add because the shapes are disjoint cases.

### Two-step experiment: counting outcomes with a Cartesian product

You roll a standard 6-sided die, then flip a coin. How many outcomes are in the sample space Ω?

1. Define the die outcome set:

   Let D = {1,2,3,4,5,6}, so |D| = 6.
2. Define the coin outcome set:

   Let C = {H,T}, so |C| = 2.
3. A full outcome is an ordered pair (d, c) where d ∈ D and c ∈ C.

   So Ω = D × C.
4. Apply multiplication rule:

   |Ω| = |D × C| = |D| · |C| = 6 · 2 = 12.

**Insight:** Sequential experiments multiply because each first-stage result can be paired with each second-stage result.

## Key Takeaways

- ✓

  |S| denotes the cardinality of a finite set S: the number of distinct outcomes in S.
- ✓

  Use the **addition rule** when outcomes come from disjoint alternatives: if A ∩ B = ∅, then |A ∪ B| = |A| + |B|.
- ✓

  Use the **multiplication rule** for sequential choices: |A × B| = |A| · |B|, and similarly for more steps.
- ✓

  “Either/or” language usually indicates addition; “and then / followed by / for each” usually indicates multiplication.
- ✓

  Many real problems require both: add across disjoint formats (cases), multiply within a format (steps).
- ✓

  Check for overlap before adding; overlap causes double-counting.
- ✓

  If constraints make later choices depend on earlier ones, you can still multiply, but the counts per step may change.

## Common Mistakes

- ✗

  Adding counts for alternatives that are not disjoint (overlap), which double-counts shared outcomes.
- ✗

  Multiplying when the problem is actually “choose one category,” not “do both steps.”
- ✗

  Forgetting order in sequential outcomes: (a, b) and (b, a) are different when steps have roles.
- ✗

  Ignoring constraints (like “no repeats”) and using the same factor for each step when the allowed set shrinks.

## Practice

easy

A website password must be either:

- •6 digits, or
- •4 letters followed by 2 digits.

Assume 10 digits and 26 letters, repetition allowed. How many passwords are possible?

**Hint:** Count each format with multiplication, then add because the formats are disjoint.

Show solution

Let Format A be 6 digits: N₁ = 10⁶.

Let Format B be 4 letters then 2 digits: N₂ = 26⁴ · 10².

Total = N₁ + N₂ = 10⁶ + 26⁴ · 10².

Compute if desired: 10⁶ = 1,000,000. 26⁴ = (26²)² = 676² = 456,976.

So N₂ = 456,976 · 100 = 45,697,600.

Total = 1,000,000 + 45,697,600 = 46,697,600.

easy

How many outcomes are possible when you flip 3 coins (in order)?

**Hint:** Each coin has 2 outcomes; use a 3-step product C × C × C.

Show solution

Let C = {H, T}, |C| = 2.

Sample space Ω = C × C × C.

|Ω| = |C|³ = 2³ = 8.

medium

A student can choose one elective from:

- •5 art electives
- •4 music electives
- •3 theater electives

How many choices are there if the student must pick exactly one elective?

**Hint:** These are disjoint categories (you choose one course total).

Show solution

Let A, M, T be the sets of art, music, and theater electives.

Assuming they are disjoint categories, total choices are

|A ∪ M ∪ T| = |A| + |M| + |T| = 5 + 4 + 3 = 12.

## Connections

Next nodes you can study:

- •[Basic Probability](/tech-tree/probability-basic/)
- •[Permutations](/tech-tree/permutations/)

Related ideas (later in discrete math):

- •Inclusion–exclusion (handles non-disjoint unions)
- •Combinations (counting selections where order doesn’t matter)
- •Product spaces and counting arguments in algorithm analysis

Quality: A (4.4/5)

[← back to tree](/tech-tree/)[browse all →](/tech-tree/inventory/)
