---
title: Basic Probability
description: Probability as favorable outcomes over total outcomes. Coin flips, dice rolls.
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
permalink: /tech-tree/probability-basic/
---

[←Back to Tech Tree](/tech-tree/)

[inventory](/tech-tree/inventory/)[coverage](/tech-tree/coverage/)

# Basic Probability

Probability & StatisticsDifficulty: ★☆☆☆☆Depth: 1Unlocks: 80

Probability as favorable outcomes over total outcomes. Coin flips, dice rolls.

## Interactive Visualization

⏮◀◀▶▶STEP0.25x1xZOOM

t=0s

## Core Concepts

- -Sample space (set of all possible outcomes)
- -Event (a subset of the sample space; outcomes of interest)
- -Classical probability (when outcomes are equally likely, probability = favorable count / total count)

## Key Symbols & Notation

P(A) - probability of event A

## Essential Relationships

- -P(A) = (number of favorable outcomes for A) / (number of equally likely outcomes in the sample space)
- -Sum of probabilities of all outcomes in the sample space = 1

## Prerequisites (1)

[Counting Principles6 atoms](/tech-tree/counting-basic/)

## Unlocks (2)

[Random Variableslvl 2](/tech-tree/random-variables/)[Conditional Probabilitylvl 2](/tech-tree/conditional-probability/)

## Referenced by (4)

Where this concept shows up in the operating-finance and personal-finance graphs.

### From Money (4)

[Emergency BufferMoney

Buffer size depends on the probability distribution of adverse events](/money/emergency-buffer/)[Full Emergency FundMoney

3-6 months depends on income replacement probability](/money/full-emergency-fund/)[Insurance BasicsMoney

Risk transfer relies on the probability of loss events](/money/insurance-basics/)[Options BasicsMoney

Option value depends on the probability distribution of the underlying price](/money/options-basics/)

Advanced Learning Details

### Graph Position

12

Depth Cost

80

Fan-Out (ROI)

30

Bottleneck Score

1

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

### All Concepts (11)

- - Probability defined as the ratio of the number of favorable outcomes to the number of total (equally likely) outcomes
- - Sample space: the set of all possible outcomes for an experiment
- - Outcome: a single result in the sample space
- - Event: a subset of the sample space (one or more outcomes) that we are interested in
- - Classical/equally‑likely assumption: the idea that each outcome in the sample space is assumed to have the same chance
- - Probability bounds: probabilities lie between 0 and 1 inclusive
- - Complement of an event: the set of outcomes in the sample space that are not in the event
- - Mutually exclusive (disjoint) events: events that cannot occur at the same time
- - Probability of a single outcome under equally likely outcomes (each single outcome has probability 1/size of sample space)
- - Using counting results (counts of favorable and total outcomes) to compute probabilities
- - Interpretation of probability as a relative frequency or long‑run proportion (classical vs. frequentist viewpoint)

### Teaching Strategy

Deep-dive lesson - accessible entry point but dense material. Use worked examples and spaced repetition.

Mini‑puzzle (predict before reading):

You roll two fair six‑sided dice and add them.

**Question:** Which sum is more likely: **6** or **7**?

Don’t compute yet—just predict.

Now open the interactive canvas for this node:

- •Set the “Die 1” slider to 1…6 and the “Die 2” slider to 1…6.
- •Watch the grid of ordered pairs (d₁, d₂) light up.
- •Then switch the canvas to “Show sums” mode and see how many pairs land on each sum.

Hold onto your prediction. By the end, you’ll be able to justify it using just one idea: **probability = favorable outcomes / total outcomes** (when outcomes are equally likely).

TL;DR:

Basic probability (classical probability) starts with a **sample space** Ω (all possible outcomes) and an **event** A ⊂ Ω (outcomes you care about). If all outcomes in Ω are equally likely, then $P(A)=∣A∣∣Ω∣.P(A)=\frac{|A|}{|\Omega|}.P(A)=∣Ω∣∣A∣​.$

## What Is Basic Probability?

### Why probability exists (motivation)

In many everyday situations you can’t predict the exact outcome, but you can still reason about **how likely** different outcomes are.

- •A coin flip: you can’t control heads vs tails.
- •A die roll: you can’t choose which face lands up.
- •Drawing a card from a shuffled deck: you don’t know which card you’ll get.

Probability gives a precise language for “chance.” In this node we focus on the simplest, most concrete version: **classical probability**.

### The two objects you always start with

1) **Sample space** (usually written Ω)

- •Definition: the **set of all possible outcomes** of an experiment.
- •Example: for one coin flip, Ω = {H, T}.
- •Example: for one die roll, Ω = {1,2,3,4,5,6}.

2) **Event** (often written A)

- •Definition: an **event** is a subset of the sample space, so A ⊂ Ω.
- •Intuition: an event is a “condition you care about.”
- •Example: on a die roll, “roll an even number” is the event A = {2,4,6}.

### Probability of an event (the key symbol)

We write **P(A)** for “the probability that event A happens.”

In this node, we restrict to situations where outcomes are **equally likely** (fair coin, fair die, well‑shuffled cards, etc.). In that setting, the probability of an event is:

P(A)=number of favorable outcomesnumber of total outcomes=∣A∣∣Ω∣.P(A)=\frac{\text{number of favorable outcomes}}{\text{number of total outcomes}}=\frac{|A|}{|\Omega|}.P(A)=number of total outcomesnumber of favorable outcomes​=∣Ω∣∣A∣​.

- •“Favorable” means “in the event A.”
- •|A| means “the number of elements in A.”

### A tiny reality check: probabilities are numbers between 0 and 1

- •If A is impossible, A = ∅, then |A| = 0 and P(A) = 0.
- •If A is certain, A = Ω, then |A| = |Ω| and P(A) = 1.
- •Most events land in between.

### Where the interactive canvas fits

Use the canvas as a *counting tool*:

- •First, decide what Ω is.
- •Then, highlight which outcomes belong to A.
- •Finally, compute P(A) = highlighted / total.

This is not just a visualization—it’s the workflow you’ll use repeatedly.

## Core Mechanic 1: Sample Spaces and Events (Ω and A)

### Why being explicit about Ω matters

A very common beginner mistake is to compute “favorable / total” with the wrong “total.” The total is not “whatever feels like all outcomes”—it’s exactly the size of your sample space Ω.

So we slow down and build a habit:

1) **Name the experiment** (what is being done?)

2) **Write Ω** (all outcomes)

3) **Describe A as a subset** of Ω

4) **Count** |Ω| and |A|

### Example 1: One coin flip

Experiment: flip a fair coin once.

- •Ω = {H, T}
- •Event A = “heads” = {H}
- •|Ω| = 2, |A| = 1
- •P(A) = 1/2

### Example 2: One die roll

Experiment: roll a fair six‑sided die.

- •Ω = {1,2,3,4,5,6}
- •Event A = “roll at least 5” = {5,6}
- •|Ω| = 6, |A| = 2
- •P(A) = 2/6 = 1/3

### Composite outcomes: ordered pairs

When you repeat an experiment, each outcome often becomes a *tuple*.

Experiment: flip a coin twice.

A good sample space is ordered outcomes:

- •Ω = {HH, HT, TH, TT}
- •|Ω| = 4

Event A = “exactly one head”

- •A = {HT, TH}
- •|A| = 2
- •P(A) = 2/4 = 1/2

Notice how order matters: HT ≠ TH as outcomes (even if they both represent “one head”).

### Use the canvas: the grid idea

In the interactive canvas, two dice outcomes are naturally shown as a 6×6 grid.

- •Each cell corresponds to one ordered pair (d₁, d₂).
- •That grid *is* the sample space Ω.
- •If the dice are fair, every cell is equally likely.

So if you can count highlighted cells, you can compute probability.

### Set operations (just enough to be useful)

Because events are sets, you can combine them.

- •Union: A ∪ B = outcomes in A **or** B (or both)
- •Intersection: A ∩ B = outcomes in A **and** B
- •Complement: Aᶜ = outcomes not in A (within Ω)

These lead to quick probability facts in the equally‑likely setting:

- •P(Aᶜ) = 1 − P(A)

And if A and B do not overlap (A ∩ B = ∅), then

- •P(A ∪ B) = P(A) + P(B)

You don’t need more set theory than that for this node—just recognize events can be built and combined.

## Core Mechanic 2: Classical Probability = Counting (Favorable / Total)

### Why counting is the engine

In classical probability, the hardest part is usually not “probability” itself—it’s **counting**.

You already know counting principles (addition and multiplication rules). Here’s how they plug into probability:

- •Multiplication rule often builds |Ω| for multi‑step experiments.
- •Addition rule often builds |A| when an event can happen in multiple distinct ways.

### The classical probability formula

When outcomes are equally likely:

P(A)=∣A∣∣Ω∣.P(A)=\frac{|A|}{|\Omega|}.P(A)=∣Ω∣∣A∣​.

The word “equally likely” is doing a lot of work.

- •Fair coin: each outcome has probability 1/2.
- •Fair die: each face has probability 1/6.
- •Two fair dice: each ordered pair has probability 1/36.

If outcomes are not equally likely, you need more advanced tools (later nodes). For now, we deliberately stay in the equally‑likely world.

### Worked motivation: why 7 is the most likely sum (return to the puzzle)

Experiment: roll two dice and sum them.

Step 1: sample space

- •Each die has 6 outcomes.
- •Ω = {(d₁, d₂) : d₁ ∈ {1,…,6}, d₂ ∈ {1,…,6}}
- •|Ω| = 6×6 = 36

Step 2: event for sum = 6

A₆ = {(d₁,d₂) : d₁+d₂=6}

List them:

- •(1,5), (2,4), (3,3), (4,2), (5,1) → 5 outcomes

So |A₆| = 5 and P(sum=6)=5/36.

Step 3: event for sum = 7

A₇ = {(d₁,d₂) : d₁+d₂=7}

List them:

- •(1,6), (2,5), (3,4), (4,3), (5,2), (6,1) → 6 outcomes

So |A₇| = 6 and P(sum=7)=6/36=1/6.

Conclusion: **7 is more likely than 6** because there are more ordered pairs that add to 7.

### Use the canvas (explicit instruction)

On the interactive canvas:

1) Toggle to “Two dice (grid)” mode.

2) Click “Highlight sum = 7.” Count highlighted cells: 6.

3) Click “Highlight sum = 6.” Count highlighted cells: 5.

4) The fraction highlighted/36 is the probability.

This is the exact same favorable/total rule—just visual.

### A compact table for common experiments

| Experiment | Sample space Ω |  | Ω |  |
| --- | --- | --- | --- | --- |
| 1 fair coin flip | {H,T} | 2 |
| 2 fair coin flips | {HH,HT,TH,TT} | 4 |
| 1 fair die roll | {1,2,3,4,5,6} | 6 |
| 2 fair dice | {(d₁,d₂)} | 36 |

### A note on “equally likely” (don’t skip this)

If a die is loaded, or a coin is biased, you cannot assume P(face) = 1/6.

Classical probability is best viewed as:

- •a starting model for fair random mechanisms, and
- •a training ground for thinking with Ω, events, and counting.

Later, you’ll generalize to probability models where outcomes have different weights.

## Application/Connection: From Basic Probability to Random Variables and Conditional Probability

### 1) Connection to random variables (next unlock)

A **random variable** is a rule that assigns a number to each outcome in Ω.

In the two‑dice example:

- •Outcome is (d₁,d₂) ∈ Ω.
- •Define X(d₁,d₂) = d₁ + d₂.

X is a random variable: it turns outcomes into numbers.

Why this matters:

- •Events can be written using X.
- •Example event: “sum is 7” is {X = 7}.

Then probability becomes:

P(X=7)=∣{ω∈Ω:X(ω)=7}∣∣Ω∣.P(X=7)=\frac{|\{\omega\in\Omega : X(\omega)=7\}|}{|\Omega|}.P(X=7)=∣Ω∣∣{ω∈Ω:X(ω)=7}∣​.

That is the same favorable/total idea, just written in a way that scales.

### 2) Connection to conditional probability (next unlock)

Conditional probability asks: **how does the probability change once you learn something?**

Even in the equally‑likely world, learning information shrinks your sample space.

Example (two dice):

- •Original Ω has 36 equally likely outcomes.
- •Suppose you learn the first die is 6.
- •New sample space: Ω′ = {(6,d₂) : d₂ ∈ {1,…,6}}
- •|Ω′| = 6

Now ask: what is the probability the sum is 7 given die 1 is 6?

Event A = “sum is 7.” Within Ω′, only (6,1) works.

- •favorable = 1, total = 6 → probability = 1/6.

This is the intuition behind P(A∣B)P(A\mid B)P(A∣B):

- •condition on B → restrict to outcomes where B is true
- •then compute favorable/total inside that restricted space

You will formalize this in the Conditional Probability node.

### 3) A practical habit you’ll reuse

Whenever you feel stuck, write:

- •What is Ω?
- •What is A?
- •Are outcomes equally likely?
- •Can I count |Ω| and |A|?

If you can answer those, you can compute P(A) in this basic setting.

## Worked Examples (3)

### Example 1: Probability of drawing a heart from a standard deck

A standard deck has 52 cards, well shuffled. Find P(A) where A = “the card is a heart.” Assume each card is equally likely.

1. Define the sample space: Ω = set of all 52 distinct cards in the deck.

   So |Ω| = 52.
2. Define the event: A = {all hearts}.

   In a standard deck there are 13 hearts, so |A| = 13.
3. Apply classical probability:

   P(A)=∣A∣∣Ω∣=1352.P(A)=\frac{|A|}{|\Omega|}=\frac{13}{52}.P(A)=∣Ω∣∣A∣​=5213​.
4. Simplify the fraction:

   1352=14.\frac{13}{52}=\frac{1}{4}.5213​=41​.

**Insight:** When outcomes are equally likely, probability is just a fraction of the sample space. The hard part is knowing what’s in Ω and counting correctly.

### Example 2: Two coin flips — probability of at least one head

Flip a fair coin twice. Find the probability of the event A = “at least one head.”

1. Write the sample space of ordered outcomes:

   Ω = {HH, HT, TH, TT}.

   So |Ω| = 4.
2. Describe the event A:

   “At least one head” includes HH, HT, TH.

   So A = {HH, HT, TH} and |A| = 3.
3. Compute:

   P(A)=∣A∣∣Ω∣=34.P(A)=\frac{|A|}{|\Omega|}=\frac{3}{4}.P(A)=∣Ω∣∣A∣​=43​.
4. Optional cross-check using complement:

   Let B = “no heads” = {TT}.

   Then P(B) = 1/4, so

   P(A)=1−P(B)=1−14=34.P(A)=1-P(B)=1-\frac{1}{4}=\frac{3}{4}.P(A)=1−P(B)=1−41​=43​.

**Insight:** The complement trick (1 − P(complement)) is often easier when the event is phrased as “at least one…” or “not…”

### Example 3: Two dice — probability the sum is at least 10

Roll two fair six-sided dice. Let A be the event “sum ≥ 10.” Find P(A).

1. Define the sample space:

   Ω = {(d₁,d₂) : d₁,d₂ ∈ {1,…,6}}.

   So |Ω| = 6×6 = 36.
2. List favorable outcomes by sums.

   Sum = 10: (4,6), (5,5), (6,4) → 3 outcomes.

   Sum = 11: (5,6), (6,5) → 2 outcomes.

   Sum = 12: (6,6) → 1 outcome.
3. Count favorable outcomes:

   |A| = 3 + 2 + 1 = 6.
4. Compute:

   P(A)=∣A∣∣Ω∣=636=16.P(A)=\frac{|A|}{|\Omega|}=\frac{6}{36}=\frac{1}{6}.P(A)=∣Ω∣∣A∣​=366​=61​.

**Insight:** For two dice, thinking in ordered pairs prevents undercounting. The canvas grid makes “36 equally likely outcomes” feel concrete.

## Key Takeaways

- ✓

  A **sample space** Ω is the set of all possible outcomes of an experiment.
- ✓

  An **event** A is a subset of the sample space: A ⊂ Ω.
- ✓

  In **classical probability** (equally likely outcomes), $P(A)=∣A∣∣Ω∣P(A)=\frac{|A|}{|\Omega|}P(A)=∣Ω∣∣A∣​$.
- ✓

  For multi-step experiments, outcomes are often **ordered tuples** (like (d₁,d₂) for two dice).
- ✓

  The complement rule is a fast tool: P(Aᶜ) = 1 − P(A).
- ✓

  Union/intersection correspond to “or/and” combinations of events; disjoint unions add probabilities.
- ✓

  The interactive canvas is a counting aid: highlight the event inside Ω, then compute highlighted/total.

## Common Mistakes

- ✗

  Using the wrong sample space (wrong “total outcomes”), especially when order matters (HT vs TH).
- ✗

  Assuming outcomes are equally likely when they aren’t (loaded die, biased coin, non-uniform mechanism).
- ✗

  Counting favorable outcomes correctly but forgetting to divide by |Ω| (or dividing by the wrong number).
- ✗

  Mixing up “at least one” with “exactly one,” or failing to use the complement when it would simplify.

## Practice

easy

Roll a fair six-sided die once. What is the probability of rolling a number greater than 2?

**Hint:** Write Ω = {1,2,3,4,5,6}. Your event is {3,4,5,6}.

Show solution

Ω has 6 outcomes. Event A = {3,4,5,6} has 4 outcomes.

P(A)=46=23.P(A)=\frac{4}{6}=\frac{2}{3}.P(A)=64​=32​.

medium

Flip a fair coin three times. What is the probability of getting exactly two heads?

**Hint:** There are 2³ outcomes total. Count outcomes with exactly two H’s (think of positions for the tails).

Show solution

Sample space size: |Ω| = 2³ = 8.

Exactly two heads means exactly one tail. Choose which flip is T:

- •THH, HTH, HHT → 3 outcomes.

So |A| = 3.

P(A)=38.P(A)=\frac{3}{8}.P(A)=83​.

medium

Roll two fair dice. What is the probability that at least one die shows a 6?

**Hint:** Use the complement: 1 − P(no 6’s). No 6 on one die has probability 5/6, so for two dice it’s (5/6)².

Show solution

Let A = “at least one 6.” Use complement Aᶜ = “no 6’s.”

For one die: P(no 6) = 5/6.

For two independent dice, the sample space is 36 equally likely pairs, and:

P(Ac)=(56)2=2536.P(A^c)=\left(\frac{5}{6}\right)^2=\frac{25}{36}.P(Ac)=(65​)2=3625​.

So

P(A)=1−P(Ac)=1−2536=1136.P(A)=1-P(A^c)=1-\frac{25}{36}=\frac{11}{36}.P(A)=1−P(Ac)=1−3625​=3611​.

## Connections

Unlocks and next steps:

- •[Random Variables](/tech-tree/random-variables/): Treat outcomes ω ∈ Ω as inputs to a function X(ω) (like the sum of two dice).
- •[Conditional Probability](/tech-tree/conditional-probability/): Update probabilities when you learn information (restrict Ω to the outcomes consistent with that information).

Related prior knowledge:

- •Counting Principles (addition/multiplication rules) power the |A| and |Ω| counts that make classical probability work.

Quality: A (4.3/5)

[← back to tree](/tech-tree/)[browse all →](/tech-tree/inventory/)
