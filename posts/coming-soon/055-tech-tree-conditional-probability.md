---
title: Conditional Probability
description: P(A|B) - probability of A given B has occurred.
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
permalink: /tech-tree/conditional-probability/
---

[←Back to Tech Tree](/tech-tree/)

[inventory](/tech-tree/inventory/)[coverage](/tech-tree/coverage/)

# Conditional Probability

Probability & StatisticsDifficulty: ★★☆☆☆Depth: 2Unlocks: 28

P(A|B) - probability of A given B has occurred.

## Interactive Visualization

⏮◀◀▶▶STEP0.25x1xZOOM

t=0s

## Core Concepts

- -Conditional probability represents the probability of event A given that B has occurred (we are evaluating A under the condition B).
- -Conditioning restricts the sample space to B; probabilities are measured relative to B rather than the original universe.
- -Definition requires the condition event to have nonzero probability: P(B) > 0.

## Key Symbols & Notation

P(A|B)

## Essential Relationships

- -P(A|B) = P(A and B) / P(B) (valid only if P(B) > 0)
- -P(A and B) = P(A|B) \* P(B)

## Prerequisites (1)

[Basic Probability6 atoms](/tech-tree/probability-basic/)

## Unlocks (3)

[Bayes Theoremlvl 2](/tech-tree/bayes-theorem/)[Markov Chainslvl 4](/tech-tree/markov-chains/)[Independencelvl 2](/tech-tree/independence/)

## Referenced by (7)

Where this concept shows up in the operating-finance and personal-finance graphs.

### From Business (6)

[Close RateBusiness

Close rate is literally P(placement | interview); data-driven recruiting means identifying which observable candidate signals maximize this conditional probability, and the 4:1 ratio is a direct expression of the conditional conversion rate through the funnel](/business/close-rate/)[CollateralBusiness

Collateral fundamentally changes P(loss severity | default) - the conditional distribution of lender losses given borrower default is dramatically different with vs without pledged assets, which is the mathematical mechanism by which collateral reduces loan pricing](/business/collateral/)[Interview-to-Placement RatioBusiness

The 4:1 ratio is literally P(placement | interview) = 0.25. Data-driven recruiting means decomposing this conditional probability through the funnel - P(pass screen | apply), P(pass interview | pass screen), etc. - and measuring which signals improve each stage's conversion rate.](/business/interview-to-placement-ratio/)[Time-to-FillBusiness

Close rates and interview-stage ratios are conditional probabilities - P(accept|offer), P(onsite|phone screen) - and the entire hiring funnel is a chain of conditional transitions whose product gives P(hire|sourced)](/business/time-to-fill/)[Contingent LiabilitiesBusiness

A contingent liability is literally a conditional obligation - it only materializes if a triggering event occurs, making P(loss | trigger event) the core quantity to estimate](/business/contingent-liabilities/)[Churn RateBusiness

Churn rate is P(leave | active customer in period t). Computing it correctly requires conditioning on the right population and time window - cohort-based churn vs blended rates are conditional probability problems.](/business/churn-rate/)

### From Money (1)

[Disability InsuranceMoney

Disability probability is conditioned on occupation, age, and health](/money/disability-insurance/)

Advanced Learning Details

### Graph Position

18

Depth Cost

28

Fan-Out (ROI)

14

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

- - Conditional probability: the probability of event A when it is known that event B has occurred (updating probabilities given new information)
- - Conditional (restricted) sample space: when conditioning on B, consider only outcomes in B as the effective sample space
- - Joint event (intersection) A ∩ B: the event that both A and B occur
- - Requirement for conditioning: P(B) > 0 is necessary for P(A|B) to be defined
- - Counting/interpreting conditional probability for equally likely outcomes: count favorable outcomes within B and divide by total outcomes in B
- - Renormalization viewpoint: probabilities are rescaled (renormalized) so total mass over B equals 1 when conditioning on B

### Teaching Strategy

Deep-dive lesson - accessible entry point but dense material. Use worked examples and spaced repetition.

A fair coin has P(H) = 1/2. But if you’re told “the coin landed heads,” the probability of heads becomes 1. Conditional probability is the formal way to express this idea: once you learn B happened, you measure everything inside the world where B is true.

TL;DR:

Conditional probability is the probability of event A given event B: P(A|B). It means you restrict your attention to outcomes in B, and then ask what fraction of those outcomes also lie in A. Formally (when P(B) > 0): P(A|B) = P(A ∩ B) / P(B).

## What Is Conditional Probability?

### Why we need it

In basic probability, you pick a sample space Ω (all possible outcomes) and assign probabilities to events (subsets of Ω). That’s great when you have no extra information.

But real reasoning almost always comes with **information**:

- •“Given that it rained, what’s the chance traffic is bad?”
- •“Given that the die roll is even, what’s the chance it’s a 6?”
- •“Given that a test is positive, what’s the chance the patient actually has the disease?”

That phrase “given that …” is exactly what conditional probability captures.

### Intuition: shrinking the universe

Think of an event B as a filter. Once you learn B occurred, outcomes not in B are impossible, so you throw them away.

- •Original world: Ω
- •After learning B: your new world is B

Conditional probability asks: **inside this new world B, how likely is A?**

So P(A|B) is not “A and B” (that’s intersection). It’s “A measured **within** B.”

### Formal definition

If P(B) > 0, the conditional probability of A given B is

P(A|B) = P(A ∩ B) / P(B)

Read it slowly:

- •A ∩ B: outcomes where **both** A and B happen
- •Divide by P(B): because we’re renormalizing probabilities so that the total probability of the new universe (B) becomes 1

### A picture in words

Imagine 100 equally likely outcomes.

- •40 outcomes are in B
- •10 outcomes are in A ∩ B

Then:

- •P(B) = 40/100
- •P(A ∩ B) = 10/100
- •P(A|B) = (10/100) / (40/100) = 10/40 = 1/4

The key idea: you don’t compare A ∩ B to Ω anymore; you compare it to B.

### The nonzero condition

The definition requires P(B) > 0.

Why? Because if P(B) = 0, then “given B happened” is conditioning on something that never happens (in your probability model). The fraction P(A ∩ B)/P(B) would divide by zero.

At difficulty level 2, the important takeaway is: **only condition on events with positive probability** (for basic discrete problems).

## Core Mechanic 1: Conditioning Restricts the Sample Space

### Why this matters

Most mistakes with conditional probability come from not fully committing to the new sample space. Learners often keep using the original denominator (Ω) instead of the conditioned denominator (B).

### Sample-space rewrite rule

Once you know B happened:

- •Possible outcomes become: B
- •Your question becomes: “What fraction of B also lies in A?”

In equally likely discrete settings:

P(A|B) = |A ∩ B| / |B|

This is the same as the earlier formula, just using counts instead of probabilities.

### Example: die roll with a condition

Let Ω = {1,2,3,4,5,6}.

- •A = “roll is 6” = {6}
- •B = “roll is even” = {2,4,6}

After conditioning on B, the new universe is {2,4,6}.

Within B:

- •Outcomes that satisfy A are just {6}

So:

P(A|B) = 1/3

Notice how different this is from P(A) = 1/6. The evidence “even” made 6 more plausible.

### Two complementary views (and when each is useful)

Conditional probability can be approached in two equivalent ways:

| View | What you do | When it’s easiest |
| --- | --- | --- |
| Restrict-and-count | Rewrite the sample space as B, then count A within it | Equally likely outcomes (dice, cards) |
| Use the formula | Compute P(A ∩ B) and P(B) from given probabilities | Non-uniform probabilities, word problems |

### Relationship to complements

If you are inside B, the complement of A becomes “not A, but still inside B.”

P(Aᶜ|B) = 1 − P(A|B)

This is often an easy way to compute a conditional probability when the direct event is awkward.

### A common mental model: “re-normalize”

Conditioning on B does two things:

1) Deletes outcomes not in B

2) Scales the remaining probabilities so they sum to 1

If the outcomes in B were originally equally likely, they remain equally likely *relative to each other* after conditioning.

If outcomes in B were not equally likely, you can still condition, but you must keep their original weights and then re-normalize.

### Mini-derivation: why the formula makes sense

Suppose we want a new probability measure P(·|B) that lives on the restricted universe B.

We want:

- •P(B|B) = 1
- •P(A|B) should be proportional to P(A ∩ B) (because only overlap with B matters)

So we set

P(A|B) = c · P(A ∩ B)

Choose c so that P(B|B) = 1:

1 = P(B|B) = c · P(B ∩ B) = c · P(B)

So c = 1 / P(B).

Therefore:

P(A|B) = P(A ∩ B) / P(B)

This is the cleanest justification for the definition: it’s the unique way to “renormalize” probabilities inside B.

## Core Mechanic 2: Multiplication Rule (Turning Conditionals into Intersections)

### Why we need a second mechanic

Sometimes you don’t want P(A|B). Instead, you want the probability that **both** events happen, P(A ∩ B). Conditional probability gives a direct bridge between these.

Starting from the definition:

P(A|B) = P(A ∩ B) / P(B)

Multiply both sides by P(B):

P(A ∩ B) = P(A|B) · P(B)

This is called the **multiplication rule**.

### Two equivalent forms

Be careful with order: both are true (when denominators are nonzero).

P(A ∩ B) = P(A|B)P(B)

P(A ∩ B) = P(B|A)P(A)

They describe the same intersection, just conditioning in different directions.

### Why this is powerful

The intersection P(A ∩ B) is often hard to estimate directly, but conditional probabilities are natural in real situations.

Example narrative:

- •P(B) = probability it rains
- •P(A|B) = probability of traffic given rain

Then P(A ∩ B) = probability it rains **and** traffic is bad.

### Chaining more than two events

Conditional probability lets you build probabilities step-by-step. For three events A, B, C with appropriate nonzero probabilities:

P(A ∩ B ∩ C) = P(A|B ∩ C) · P(B|C) · P(C)

Interpretation: start from C, then within C consider B, then within (B ∩ C) consider A.

At this node’s level, you don’t need to memorize the general chain rule, but it’s useful to see that conditional probability is the building block for multi-step reasoning.

### A note on symmetry (and why “given” is not symmetric)

Intersection is symmetric:

A ∩ B = B ∩ A

But conditional probability generally is not:

P(A|B) ≠ P(B|A)

Example:

- •A = “number is divisible by 2”
- •B = “number is divisible by 6” (in {1,…,12})

If a number is divisible by 6, it must be divisible by 2, so P(A|B) = 1.

But if a number is divisible by 2, it is not necessarily divisible by 6, so P(B|A) < 1.

This non-symmetry is the entire reason Bayes’ Theorem is interesting later: it provides a way to relate the two directions.

## Application/Connection: Reading Real Problems (Tests, Updates, and “Given” Language)

### Translating English to events

A lot of conditional probability skill is language parsing.

- •“Probability of A given B” → P(A|B)
- •“Probability of A and B” → P(A ∩ B)
- •“Probability of A or B” → P(A ∪ B)
- •“Only look at cases where B happened” → restrict sample space to B

A practical technique: rewrite the question as

“Among outcomes where B is true, what fraction have A true?”

### Diagnostic tests (setup for Bayes)

Consider medical testing language:

- •D = person has disease
- •T = test is positive

Two different conditionals:

- •P(T|D): sensitivity (test detects disease when disease is present)
- •P(D|T): probability of disease given a positive test (what you actually care about)

These are not the same. Conditional probability makes that distinction precise.

Even before Bayes’ Theorem, you can see the structure:

- •P(D|T) depends on how common the disease is (base rate P(D))
- •P(T|D) is about the test’s behavior

This node equips you to keep the symbols straight so Bayes later feels like algebra, not magic.

### Independence as a special case

Independence will be unlocked soon. Conditional probability is the quickest way to express it.

A and B are independent exactly when

P(A|B) = P(A)

(assuming P(B) > 0)

Interpretation: learning B doesn’t change your belief about A.

Equivalently:

P(A ∩ B) = P(A)P(B)

But conceptually, the conditional form is often more intuitive: **no update**.

### Markov chains preview

A Markov chain is about transitions like

P(Xₜ₊₁ = j | Xₜ = i)

That is literally conditional probability: the next state given the current state.

So this node is foundational: without comfort reading and manipulating P(·|·), transition matrices and “memoryless” properties will feel opaque.

### Quick checklist for solving conditional probability problems

1) Identify events A and B clearly.

2) Confirm P(B) > 0 (in discrete problems, B must have at least one outcome).

3) Decide approach:

- •Restrict-and-count if equally likely
- •Use P(A|B) = P(A ∩ B)/P(B) if probabilities are given

4) Be explicit about the denominator: after conditioning, your denominator is B.

5) Sanity-check: 0 ≤ P(A|B) ≤ 1, and if A ⊂ B then P(A|B) = P(A)/P(B) and should be ≤ 1.

That last point is a great self-check: if you compute something bigger than 1, your denominator or event interpretation is wrong.

## Worked Examples (3)

### Worked Example 1: Conditioning by restricting the sample space (cards)

A standard 52-card deck. Let A = “card is an Ace”. Let B = “card is a Spade”. Find P(A|B).

1. Step 1: Translate the meaning.

   P(A|B) means: among the spades, what fraction are aces?
2. Step 2: Count the conditioned universe.

   B = “Spade” → there are 13 spades.

   So |B| = 13.
3. Step 3: Count the overlap.

   A ∩ B = “Ace and Spade” → only the Ace of Spades.

   So |A ∩ B| = 1.
4. Step 4: Compute the conditional probability using counts.

   P(A|B) = |A ∩ B| / |B| = 1 / 13.

**Insight:** Conditioning turned a 52-outcome space into a 13-outcome space. The denominator must match the condition.

### Worked Example 2: Using the formula and the multiplication rule

Suppose P(B) = 0.30 and P(A|B) = 0.20. Find (1) P(A ∩ B) and (2) P(Aᶜ|B).

1. Part (1): Use the multiplication rule.

   We know:

   P(A ∩ B) = P(A|B)P(B)
2. Compute:

   P(A ∩ B) = 0.20 · 0.30 = 0.06
3. Part (2): Use the complement rule inside the condition.

   P(Aᶜ|B) = 1 − P(A|B)
4. Compute:

   P(Aᶜ|B) = 1 − 0.20 = 0.80

**Insight:** Once you know one conditional probability, you can often get several others quickly using algebraic identities (multiplication and complements).

### Worked Example 3: “Given” changes the denominator (dice)

Roll a fair six-sided die. Let A = “roll is greater than 3” and B = “roll is odd”. Compute P(A|B) and compare to P(A).

1. Step 1: List outcomes.

   Ω = {1,2,3,4,5,6}

   A = {4,5,6}

   B = {1,3,5}
2. Step 2: Restrict to B.

   Given B occurred, possible outcomes are {1,3,5}. So |B| = 3.
3. Step 3: Find overlap A ∩ B.

   A ∩ B = {5}. So |A ∩ B| = 1.
4. Step 4: Compute conditional.

   P(A|B) = |A ∩ B| / |B| = 1/3.
5. Step 5: Compute unconditional for comparison.

   P(A) = |A| / |Ω| = 3/6 = 1/2.

**Insight:** Learning “odd” made outcomes {4,6} impossible, which reduced the chance of being > 3 from 1/2 down to 1/3.

## Key Takeaways

- ✓

  Conditional probability measures A **within** the world where B is known to occur.
- ✓

  Definition (requires P(B) > 0): P(A|B) = P(A ∩ B) / P(B).
- ✓

  Conditioning restricts the sample space to B; the denominator becomes B, not Ω.
- ✓

  Multiplication rule: P(A ∩ B) = P(A|B)P(B) (and also = P(B|A)P(A)).
- ✓

  Conditional probability is generally not symmetric: P(A|B) ≠ P(B|A).
- ✓

  Complement works inside conditions: P(Aᶜ|B) = 1 − P(A|B).
- ✓

  Independence can be expressed as “no update”: P(A|B) = P(A) (when P(B) > 0).

## Common Mistakes

- ✗

  Using the original sample space Ω as the denominator instead of using the conditioned event B.
- ✗

  Confusing P(A|B) with P(A ∩ B): “given” vs “and”.
- ✗

  Assuming P(A|B) = P(B|A) just because the same letters appear.
- ✗

  Conditioning on an impossible event (forgetting the requirement P(B) > 0).

## Practice

easy

A fair die is rolled. Let A = “the roll is 2 or 3” and B = “the roll is less than 4”. Compute P(A|B).

**Hint:** Restrict the sample space to B first, then count outcomes in A within that restricted set.

Show solution

Ω = {1,2,3,4,5,6}

A = {2,3}

B = {1,2,3}

A ∩ B = {2,3}

P(A|B) = |A ∩ B| / |B| = 2/3.

medium

You are told that P(B) = 0.4 and P(A ∩ B) = 0.1. Compute P(A|B).

**Hint:** Use the definition P(A|B) = P(A ∩ B)/P(B).

Show solution

Given P(B) = 0.4 and P(A ∩ B) = 0.1,

P(A|B) = 0.1 / 0.4 = 0.25.

hard

A bag has 3 red balls and 2 blue balls. Two balls are drawn without replacement. Let A = “the second ball is red” and B = “the first ball is red”. Compute P(A|B).

**Hint:** After conditioning on B, update the bag’s composition before computing the probability of A.

Show solution

Initially: 3R, 2B (5 total).

Condition on B: the first ball is red, so remove one red.

Remaining bag: 2R, 2B (4 total).

Event A: second ball is red.

So P(A|B) = 2/4 = 1/2.

## Connections

Next nodes:

- •[Bayes Theorem](/tech-tree/bayes-theorem/) — relates P(A|B) and P(B|A) using P(A ∩ B).
- •[Independence](/tech-tree/independence/) — independence means conditioning on B doesn’t change A: P(A|B) = P(A).
- •[Markov Chains](/tech-tree/markov-chains/) — transitions are conditional probabilities like P(Xₜ₊₁|Xₜ).

Quality: A (4.5/5)

[← back to tree](/tech-tree/)[browse all →](/tech-tree/inventory/)
