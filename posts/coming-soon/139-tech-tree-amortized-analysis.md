---
title: Amortized Analysis
description: Average cost over sequence of operations. Aggregate, accounting methods.
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
permalink: /tech-tree/amortized-analysis/
---

[←Back to Tech Tree](/tech-tree/)

[inventory](/tech-tree/inventory/)[coverage](/tech-tree/coverage/)

# Amortized Analysis

AlgorithmsDifficulty: ★★★☆☆Depth: 3Unlocks: 1

Average cost over sequence of operations. Aggregate, accounting methods.

## Interactive Visualization

⏮◀◀▶▶STEP0.25x1xZOOM

t=0s

## Core Concepts

- -Amortized cost: the average cost per operation over a sequence (worst-case sequence view, not probabilistic).
- -Potential/accounting method: assign stored credit via a potential function on states to move cost between operations.

## Key Symbols & Notation

Phi(S) - potential function mapping a state S to a real (stored credit)

## Essential Relationships

- -Per-operation potential relation: a\_i = c\_i + Phi(S\_i) - Phi(S\_{i-1}) (a\_i = amortized cost, c\_i = actual cost).
- -Telescoping/aggregate: sum\_{i=1..n} a\_i = sum\_{i=1..n} c\_i + Phi(S\_n) - Phi(S\_0); if Phi(S\_0)=0 and Phi(S) >= 0 then sum a\_i >= sum c\_i, so amortized costs bound total actual cost.

## Prerequisites (1)

[Big O Notation6 atoms](/tech-tree/big-o/)

## Unlocks (1)

[Disjoint Setslvl 3](/tech-tree/disjoint-sets/)

## Referenced by (2)

Where this concept shows up in the operating-finance and personal-finance graphs.

### From Business (2)

[Amortized CostBusiness

Same core principle applied to algorithm complexity - averaging the cost of a sequence of operations rather than evaluating each individually, directly paralleling how business amortized cost smooths uneven actual costs into uniform periodic amounts](/business/amortized-cost/)[amortized costsBusiness

Direct mathematical formalization: amortized analysis computes average cost over a sequence of operations (aggregate and accounting methods), which is the same core idea as spreading uneven actual costs into a uniform per-period figure](/business/amortized-costs/)

Advanced Learning Details

### Graph Position

33

Depth Cost

1

Fan-Out (ROI)

1

Bottleneck Score

3

Chain Length

### Cognitive Load

5

Atomic Elements

23

Total Elements

L0

Percentile Level

L3

Atomic Level

### All Concepts (10)

- - Amortized cost: the average cost per operation when averaged over a sequence of operations (as a worst-case guarantee over sequences, not a probabilistic average)
- - Sequence-of-operations perspective: analyze a whole sequence of m operations on a data structure rather than a single operation in isolation
- - Aggregate method: compute total actual cost of a sequence then divide by number of operations to get amortized cost
- - Accounting (banker's) method: assign an amortized charge to each operation, deposit excess as 'credits' and use credits to pay expensive operations later
- - Potential method: define a potential function that maps the data structure state to a scalar 'stored energy' used to pay future costs
- - Credits / stored value: abstract resource (credits or potential) accumulated by cheaper operations and consumed by expensive ones
- - Invariants for amortized proofs: nonnegativity of stored credits or potential and an initial potential value (often zero)
- - Amortized bound notation and meaning: saying an operation is O(1) amortized means total cost of any sequence of m operations is O(m)
- - Distinction between amortized guarantee and worst-case-per-operation guarantee: amortized allows occasional expensive ops as long as average over sequence is bounded
- - Design of charging schemes / potential functions: selecting an amortized charge or potential function to make bookkeeping/invariant hold

### Teaching Strategy

Self-serve tutorial - low prerequisites, straightforward concepts.

Some operations are occasionally expensive, but only because they “pay back” a lot of cheap work you did earlier. Amortized analysis is the toolkit for proving that kind of performance—without assuming randomness and without pretending worst-case spikes don’t happen.

TL;DR:

Amortized analysis bounds the average cost per operation over any sequence of operations (worst-case sequence, not probabilistic). You can prove an O(1) amortized cost even if some individual operations cost O(n), using either (1) aggregate analysis, (2) the accounting (banker’s) method, or (3) the potential method with a potential function Φ(S) over states S.

## What Is Amortized Analysis?

### Why we need it

Big-O worst-case analysis answers: “How bad can *one* operation be?” That’s important, but it can be misleading for data structures where rare expensive operations are balanced by many cheap ones.

Classic example: dynamic arrays.

- •Most `push` operations are O(1).
- •Occasionally, the array grows and you copy n elements: O(n).

Worst-case per operation is O(n), but in practice we feel “constant-ish” time. Amortized analysis is the formal proof of that feeling.

### The key idea: worst-case over sequences

Amortized analysis is **not** average-case probability. There is no distribution over inputs.

Instead we fix *any* sequence of m operations (even an adversarially chosen one), and we show:

∑ (actual cost of op i) ≤ (amortized cost bound) · m + constant

Then the amortized cost per operation is the average upper bound over that sequence.

Formally, if operation i has actual cost cᵢ, we want a bound like:

(1/m) ∑ᵢ cᵢ ≤ O(f(n))

for all sequences of length m, where n is a relevant size parameter (often current number of elements).

### Three common proof styles

Amortized analysis usually comes in three equivalent “voices”:

| Method | Core move | What you track | When it feels natural |
| --- | --- | --- | --- |
| Aggregate | Bound total cost of m ops directly | Total work across the whole run | Resizing arrays, periodic rebuilds |
| Accounting (banker’s) | Overcharge some ops, store “credits” | Credits attached to items/structure | Stack with multipop, splay-ish intuitions |
| Potential | Define Φ(S) on state S; amortized = actual + ΔΦ | A single numeric potential | Systematic, composable proofs |

You’ll often start with aggregate to get intuition, then write a clean potential function to make the proof reusable.

### What makes a good amortized argument

Two ingredients:

1. 1)**A clear model of cost** (what counts as 1 unit? comparisons, pointer updates, element moves?)
2. 2)**A stored-value story**: expensive operations spend work that was “saved up” by previous cheap operations.

That stored value can be literal credits (accounting) or a potential Φ(S) (potential method).

### Introducing the potential function Φ(S)

A potential function maps a **state** S of the data structure to a real number:

Φ(S) ∈ ℝ

Intuition: Φ(S) is “stored credit” or “energy.” If Φ increases, we’re saving credit for later. If Φ decreases, we’re spending credit to subsidize a costly operation.

A standard requirement is:

- •Φ(S) ≥ 0 for all reachable states S
- •Φ(S₀) is usually 0 (or bounded) for the initial empty state S₀

Then we define amortized cost:

ĉᵢ = cᵢ + (Φ(Sᵢ) − Φ(Sᵢ₋₁))

and show that ĉᵢ ≤ some bound for every operation.

Finally, the magic telescopes:

∑ᵢ ĉᵢ = ∑ᵢ cᵢ + (Φ(S\_m) − Φ(S₀))

So if Φ(S\_m) ≥ 0 and Φ(S₀) ≥ 0, then:

∑ᵢ cᵢ ≤ ∑ᵢ ĉᵢ + Φ(S₀)

Meaning: bounding amortized costs bounds total actual cost.

This is the formal reason amortized analysis is worst-case over sequences: the inequality holds for every sequence, not “on average.”

## Core Mechanic 1: Aggregate Analysis (Total Cost Over m Operations)

### Why aggregate analysis comes first

Aggregate analysis is the quickest path to intuition: instead of bounding each operation, you bound the *total* work across a whole sequence, then divide by m.

This is perfect when expensive events are structured and countable (like “how many resizes can happen?”).

### Example pattern: occasional rebuilds

Suppose we have a structure that is cheap most of the time, but sometimes does a rebuild costing proportional to its size.

To use aggregate analysis:

1. 1)Identify the expensive events.
2. 2)Bound how many times they can happen in m operations.
3. 3)Sum their costs.

### Dynamic array resizing: total copies are linear in m

Consider a dynamic array that doubles capacity when full.

- •`push(x)` writes x into the next slot: cost 1.
- •If full, allocate new array of size 2k and copy k elements: cost k (plus the write).

Let’s count element copies over m pushes starting from empty.

Capacities go 1, 2, 4, 8, …

When capacity is k and we grow, we copy k elements.

So total copy cost over all grows up to size m is:

1 + 2 + 4 + … + ⌊m/2⌋ < 2m

because geometric series:

∑\_{j=0}^{t} 2ʲ = 2^{t+1} − 1

Thus total actual cost over m pushes is:

- •m writes
- •< 2m copies

So total < 3m, hence amortized cost is < 3 = O(1).

### What aggregate analysis gives you (and what it doesn’t)

Aggregate analysis shows:

(1/m) ∑ᵢ cᵢ ≤ constant

But it doesn’t produce a per-operation “bank balance” that composes well with other operations. If you later add `pop`, `shrink`, or other behavior, aggregate analysis can become messy.

That’s why we often upgrade to accounting or potential methods: they track stored credit in a way that’s easier to extend.

### A second aggregate pattern: bounded number of expensive steps

A surprisingly common amortized trick is:

- •Each operation can do many “small steps” (like while-loops).
- •But each small step can be charged to a unique event (like “this element gets popped once”).

Then total steps over m operations is O(m).

This is the philosophical bridge to the next methods: you’re already doing “charging,” just informally.

### Aggregate analysis as a proof template

When you can identify a monotone progress measure (size, capacity, number of items that can be moved), aggregate bounds often become a one-liner:

Total cost ≤ O(total progress)

But when progress can go up and down, you’ll want explicit stored credit (accounting) or explicit Φ(S) (potential).

## Core Mechanic 2: Accounting and Potential Methods (Moving Cost Between Operations)

### Why we need “stored credit”

Aggregate analysis is great when behavior is monotone. But many data structures have operations that undo each other (`push` vs `pop`) or have multiple interacting costs.

Accounting and potential methods let you say:

- •“This cheap operation will overpay a bit.”
- •“That overpayment is saved.”
- •“Later, a costly operation spends what was saved.”

The result is a uniform amortized bound even if the sequence alternates adversarially.

---

## The accounting (banker’s) method

### The rules

You assign each operation i an **amortized charge** ĉᵢ.

- •You must ensure ĉᵢ ≥ cᵢ − (credits spent on op i)
- •You maintain that the “bank balance” (credits stored) never goes negative.

If the bank never goes negative, then the total amortized charge upper-bounds total actual cost:

∑ᵢ cᵢ ≤ ∑ᵢ ĉᵢ

Intuition: if you always have enough saved credit to pay for extra work, you can’t “cheat.”

### A classic example: stack with multipop

Operations on a stack:

- •`push(x)`: cost 1
- •`pop()`: cost 1 (if nonempty)
- •`multipop(k)`: pop up to k items; cost = number popped

Worst-case `multipop(k)` is O(n). But amortized, it’s O(1).

Accounting proof idea:

- •Charge `push` an amortized cost of 2.
- •Use 1 to pay for the push.
- •Store 1 credit on the pushed item.

When an item is popped (by `pop` or by `multipop`), spend its stored credit to pay the pop.

Each item is popped at most once, so the credits always suffice.

Thus each operation has amortized O(1).

---

## The potential method

### Why potential is more systematic

Accounting attaches credits to “places” (items, nodes, edges). That’s intuitive, but can be ad hoc.

The potential method compresses the entire credit state into a single function:

Φ(S): state → ℝ

Then define amortized cost:

ĉᵢ = cᵢ + (Φ(Sᵢ) − Φ(Sᵢ₋₁))

If you can prove ĉᵢ ≤ K for every operation (for some constant K), then:

∑ᵢ cᵢ

= ∑ᵢ (ĉᵢ − (Φ(Sᵢ) − Φ(Sᵢ₋₁)))

= ∑ᵢ ĉᵢ − (Φ(S\_m) − Φ(S₀))

≤ ∑ᵢ ĉᵢ + Φ(S₀)

And if Φ(S₀) = 0 and Φ(S\_m) ≥ 0, then:

∑ᵢ cᵢ ≤ ∑ᵢ ĉᵢ

So bounding amortized costs bounds actual total cost.

### How to choose Φ(S)

A good Φ(S) should:

1. 1)Be easy to compute conceptually (even if not computed at runtime).
2. 2)Increase when you do “preparatory work” that will help later.
3. 3)Decrease when an operation is expensive.

Common patterns:

| Situation | Potential often depends on |
| --- | --- |
| Resizable arrays | difference between capacity and size |
| Balanced rebuilding | distance from “ideal balance” |
| Union-Find (later) | ranks / sizes / structural complexity |
| Splay trees | weighted path lengths (advanced) |

### Relating accounting and potential

If accounting stores credits on items, potential is often:

Φ(S) = total stored credits in the structure

So potential can be viewed as “the banker’s balance,” but expressed as a function of state rather than as an explicit ledger.

### A small but crucial constraint

Potential functions are typically chosen to be **nonnegative** on all reachable states:

∀S reachable: Φ(S) ≥ 0

This ensures the telescoping argument yields an upper bound on actual cost.

Sometimes Φ(S) can be negative if you can still bound Φ(S\_m) − Φ(S₀), but for most learning-level proofs, keep Φ ≥ 0 to avoid subtle pitfalls.

### A note on notation

You’ll often see potential written as Φ, and state as S.

We’ll use:

- •Sᵢ = state after i-th operation
- •ΔΦᵢ = Φ(Sᵢ) − Φ(Sᵢ₋₁)

Then:

ĉᵢ = cᵢ + ΔΦᵢ

Think: amortized = actual + change in stored credit.

If ΔΦᵢ is positive, you’re “saving” credit (amortized > actual).

If ΔΦᵢ is negative, you’re “spending” credit (amortized < actual).

## Application/Connection: From Amortized Analysis to Union-Find and Real Data Structures

### Why this matters beyond toy examples

Amortized analysis shows up whenever a data structure occasionally does heavy maintenance:

- •rebuilding, rebalancing, resizing
- •path compression (Union-Find)
- •garbage collection / compaction strategies

The point is not that worst-case spikes disappear—they don’t. The point is that **spikes are paid for** by many cheap operations.

### How amortized proofs guide design

When you design an algorithm, amortized thinking helps you decide:

- •How aggressive should resizing be? (double vs +constant)
- •When should you rebuild a structure? (every k operations, or when imbalance exceeds a threshold)
- •What invariant should you maintain? (choose one that yields a clean potential)

If you pick the right invariant, you can often get:

- •simple implementation
- •strong worst-case-over-sequences guarantees

### Connection to Disjoint Sets (Union-Find)

Union-Find with union by rank/size and path compression has famously fast operations: “near constant.”

That result is typically stated as:

- •A sequence of m operations on n elements costs O(m α(n))
- •where α(n) is the inverse Ackermann function (≤ 4 for all practical n)

This is an amortized statement: single operations can be more expensive, but across the whole sequence the average is tiny.

To understand that proof later, you need comfort with:

- •reasoning about sequences (not single worst cases)
- •charging work to structural progress
- •potential-like arguments (or equivalent accounting)

This node is the prerequisite mindset.

### Choosing between methods in practice

Here’s a pragmatic guide:

| If you see… | Try… |
| --- | --- |
| A simple growth pattern (doubling, geometric) | Aggregate analysis first |
| A while-loop that deletes items (each item removed once) | Accounting (“each item prepaid”) |
| Multiple interacting operations and non-monotone state | Potential function Φ(S) |

### Mental model you should keep

Amortized analysis is a guarantee about *any* sequence:

- •Not “typical inputs”
- •Not “random operations”
- •Not “expected value”

It’s deterministic: an adversary can pick the worst possible sequence, and the total cost bound still holds.

That’s why it’s so valuable for core data structures used everywhere.

### Checklist for writing your own amortized proof

1. 1)State the operations and cost model.
2. 2)Pick a method (aggregate / accounting / potential).
3. 3)Define what credit means (explicitly or via Φ(S)).
4. 4)Prove credits never go negative (or Φ(S) ≥ 0).
5. 5)Derive the total-cost bound by summing over operations.

Once you can do that reliably, you’re ready to read and trust “near constant amortized time” claims in advanced structures like Union-Find.

## Worked Examples (3)

### Dynamic Array Push with Doubling (Aggregate + Potential)

A dynamic array supports push(x). If the array has size n and capacity cap:

- •If n < cap: write x (cost 1)
- •If n = cap: allocate new array of size 2·cap, copy cap elements, then write x.

Assume starting from empty with cap = 1.

Goal: prove amortized O(1) per push.

1. Aggregate view (total copies):

   Let m be the number of pushes.

   Resizes occur at sizes 1, 2, 4, 8, …

   When resizing from capacity k to 2k, we copy k elements.

   Total copies ≤ 1 + 2 + 4 + … + ⌊m/2⌋ < 2m.

   Total writes = m.

   So total cost < 3m ⇒ amortized cost < 3 = O(1).
2. Potential view (define Φ):

   Let state S be (n, cap).

   Choose Φ(S) = 2n − cap.

   Check nonnegativity on reachable states:

   Because cap is always a power of 2 and n ≤ cap, we have 2n − cap ≥ 0 only when n ≥ cap/2.

   So Φ is not always ≥ 0.

   Fix by clamping: Φ(S) = max(0, 2n − cap).

   This keeps Φ(S) ≥ 0 for all states.
3. Amortized cost when no resize (n < cap):

   Actual cost c = 1.

   If n < cap/2 then Φ = 0 before and after push until you cross cap/2.

   So ΔΦ = 0 and ĉ = 1.

   If n ≥ cap/2 then Φ = 2n − cap.

   After push, n increases by 1 so Φ increases by 2.

   Thus ΔΦ = 2 and ĉ = 1 + 2 = 3.
4. Amortized cost when resize happens (n = cap):

   Before: n = cap so Φ\_before = max(0, 2cap − cap) = cap.

   Actual cost: copy cap items (cap) + write (1) ⇒ c = cap + 1.

   After resize: new cap' = 2cap, new n' = cap + 1.

   Φ\_after = max(0, 2(cap + 1) − 2cap) = max(0, 2) = 2.

   So ΔΦ = 2 − cap.

   Amortized cost:

   ĉ = c + ΔΦ = (cap + 1) + (2 − cap) = 3.
5. Conclusion:

   Every push has amortized cost ≤ 3, so any sequence of m pushes costs ≤ 3m + Φ(S₀).

   With empty start Φ(S₀) = 0, total is O(m) ⇒ O(1) amortized per push.

**Insight:** The resize operation is expensive (cap copies), but the potential drops by about cap at the same moment, “paying for” the copies. Choosing Φ(S) so that it rises during cheap pushes and falls during a resize is the whole art.

### Stack with multipop(k) (Accounting Method)

Operations on a stack:

- •push(x): actual cost 1
- •pop(): actual cost 1 if stack nonempty
- •multipop(k): pop up to k items; actual cost = number of pops performed

Goal: prove O(1) amortized time per operation for any sequence.

1. Define the accounting scheme:

   Charge each push an amortized cost ĉ = 2.

   Charge each pop and multipop an amortized cost ĉ = 0.

   Interpretation:

   - •When pushing an item, spend 1 credit to pay the actual push.
   - •Store 1 credit on the item itself.
2. Show credits never go negative:

   Each item receives 1 stored credit when it is pushed.

   An item can be removed (popped) at most once across the entire sequence.

   Whenever pop/multipop removes an item, it spends that item’s stored credit to pay its actual cost 1.

   Thus every actual pop is paid by a credit that definitely exists.

   So the bank balance (total stored credits) is never negative.
3. Bound total actual cost by total amortized charge:

   Let there be P pushes in the sequence.

   Total amortized charge is ∑ ĉ = 2P.

   Total actual cost is:

   - •pushes: P
   - •pops via pop/multipop: at most P (cannot pop more than pushed)

   So total actual ≤ 2P = total amortized.
4. Convert to per-operation bound:

   If the total number of operations is m, then P ≤ m.

   Total actual cost ≤ 2m ⇒ amortized O(1) per operation.

**Insight:** The expensive-looking operation is multipop(k), but its work is capped by a lifetime rule: each pushed item can only be popped once. Accounting makes that rule explicit by attaching a prepaid coin to each item.

### Binary Counter Increment (Potential Method)

A binary counter supports increment(): add 1 to a k-bit binary number.

Cost model: flipping one bit costs 1.

In the worst case (e.g., 111…111 + 1), increment flips k bits ⇒ O(k).

Goal: show amortized O(1) cost per increment over any sequence.

1. Observe what happens in increment:

   - •Some number t ≥ 0 of trailing 1 bits flip from 1 → 0.
   - •Then one 0 bit flips from 0 → 1.

   So actual cost c = t + 1.
2. Define potential Φ(S):

   Let S be the current bitstring.

   Let Φ(S) = (# of 1 bits in S).

   Clearly Φ(S) ≥ 0 always.
3. Compute ΔΦ for one increment:

   Trailing t ones become zeros: decreases Φ by t.

   One zero becomes one: increases Φ by 1.

   So ΔΦ = 1 − t.
4. Compute amortized cost:

   ĉ = c + ΔΦ

   = (t + 1) + (1 − t)

   = 2.
5. Conclude:

   Every increment has amortized cost 2, so any sequence of m increments performs at most 2m bit flips in total (up to an additive constant from Φ(S₀)).

**Insight:** A long carry chain is expensive exactly when you erase many 1s—so the potential (number of 1s) drops sharply and reimburses the work.

## Key Takeaways

- ✓

  Amortized analysis bounds average cost per operation over any sequence, not an expected value over random inputs.
- ✓

  To prove amortized bounds, you either bound total cost directly (aggregate) or shift cost across operations (accounting/potential).
- ✓

  Accounting method: overcharge some operations and store credits; the invariant is that stored credits never go negative.
- ✓

  Potential method: choose Φ(S) ≥ 0 and define ĉᵢ = cᵢ + (Φ(Sᵢ) − Φ(Sᵢ₋₁)); telescoping sums convert amortized bounds to total cost bounds.
- ✓

  A good Φ(S) increases during cheap operations (saving credit) and decreases during expensive ones (spending credit).
- ✓

  Many “worst-case O(n)” operations (resize, multipop, carries) are O(1) amortized because expensive work can happen only when enough credit has accumulated.
- ✓

  Amortized reasoning is foundational for advanced data structures, including Union-Find’s near-constant time guarantees.

## Common Mistakes

- ✗

  Confusing amortized analysis with average-case (probabilistic) analysis; amortized is deterministic over worst-case sequences.
- ✗

  Picking a potential function Φ(S) that can go negative without carefully bounding Φ(S\_m) − Φ(S₀), causing the telescoping argument to fail.
- ✗

  Charging credits in the accounting method without proving the bank balance never goes negative (i.e., silently borrowing from the future).
- ✗

  Bounding each operation’s amortized cost but forgetting to state the cost model precisely (what counts as 1 unit of work).

## Practice

medium

Dynamic array with growth factor 3/2: capacity multiplies by 3/2 (round up) when full. Show that push(x) is still O(1) amortized. Give an aggregate analysis bound on total copies over m pushes.

**Hint:** Sum the capacities copied at each resize as a geometric series: k + (3/2)k + (3/2)²k + … up to O(m). The ratio is > 1 but constant.

Show solution

Let capacities be c₀, c₁, c₂, … where c\_{j+1} = ⌈(3/2) c\_j⌉. When resizing from c\_j to c\_{j+1}, you copy c\_j elements.

After enough pushes to reach size m, the largest capacity is O(m).

Total copies = ∑\_{j} c\_j.

Since c\_j grows geometrically with ratio about 3/2, the sum of all previous capacities is dominated by the last:

∑\_{j=0}^{t} c\_j ≤ c\_t · (1 + 2/3 + (2/3)² + …) = 3c\_t.

With c\_t = O(m), total copies = O(m).

Adding m writes gives total cost O(m), hence amortized O(1) per push.

hard

Binary counter variant: define cost as the number of bits inspected (read) during increment, not just flipped. Suppose your increment scans trailing 1s until it finds a 0, then flips. Show the amortized cost is still O(1) using a potential function.

**Hint:** Use the same Φ(S) = number of 1s. Relate “inspected bits” to trailing 1s + the first 0. The scan length is t + 1.

Show solution

Let t be the number of trailing 1s. The algorithm inspects t trailing 1 bits plus the first 0 bit, so actual cost c = t + 1 (inspections). It may also flip bits, but if flips are included they are also O(t + 1).

Choose Φ(S) = (# of 1 bits). Then ΔΦ = 1 − t as in the standard proof.

Amortized cost:

ĉ = c + ΔΦ = (t + 1) + (1 − t) = 2.

Thus amortized O(1) per increment for inspections (and also for flips if counted similarly).

easy

A stack supports push and pop, and also an operation clear() that removes all items currently in the stack. Actual cost of clear() is the number of removed items. Prove O(1) amortized per operation with an accounting argument.

**Hint:** Same idea as multipop: each pushed item can be removed at most once, whether by pop or clear.

Show solution

Charge each push amortized cost 2: pay 1 for the actual push and store 1 credit on the item. Charge pop and clear amortized cost 0. When pop removes an item, spend its stored credit to pay cost 1. When clear removes r items, spend each item’s stored credit to pay its unit removal cost; total credits spent = r. Since each item is removed at most once, credits never go negative. Therefore total actual cost is at most total amortized charge, which is 2·(#pushes) ≤ 2m for m operations, giving O(1) amortized.

## Connections

Unlocks: [Disjoint Sets](/tech-tree/disjoint-sets/)

Related nodes you may want next:

- •[Big O Notation](/tech-tree/big-o-notation/)
- •[Dynamic Arrays](/tech-tree/dynamic-arrays/)
- •[Data Structure Invariants](/tech-tree/data-structure-invariants/)

Quality: A (4.6/5)

[← back to tree](/tech-tree/)[browse all →](/tech-tree/inventory/)
