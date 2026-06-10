---
title: Greedy Algorithms
description: Making locally optimal choices. Optimal substructure without overlapping.
date: '2026-07-01'
scheduled: '2026-10-22'
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
inspiration_url: https://templeton.host/tech-tree/greedy-algorithms/
inspiration_category: tech-tree
---

> Source-copy draft imported from [https://templeton.host/tech-tree/greedy-algorithms/](https://templeton.host/tech-tree/greedy-algorithms/). Names, domain references, and local media paths were adapted for Xavi Ablaza / getablaza.com.

[←Back to Tech Tree](/tech-tree/)

[inventory](/tech-tree/inventory/)[coverage](/tech-tree/coverage/)

# Greedy Algorithms

AlgorithmsDifficulty: ★★★☆☆Depth: 3Unlocks: 2

Making locally optimal choices. Optimal substructure without overlapping.

## Interactive Visualization

⏮◀◀▶▶STEP0.25x1xZOOM

t=0s

## Core Concepts

- -Greedy-choice property: a single locally optimal choice can be extended to a global optimum
- -Optimal substructure: an optimal solution contains optimal solutions to subinstances
- -Feasibility invariant: each greedy choice must preserve a valid (feasible) partial solution

## Key Symbols & Notation

argmax / argmin (the argument that maximizes or minimizes a selection criterion)

## Essential Relationships

- -Greedy-choice property depends on optimal substructure (local optimality implies global optimality only when optimal substructure holds)
- -Every greedy choice must preserve feasibility so that optimal substructure can be applied to the remaining instance

## Prerequisites (2)

[Proof Techniques5 atoms](/tech-tree/proof-techniques/)[Big O Notation6 atoms](/tech-tree/big-o/)

## Unlocks (2)

[Approximation Algorithmslvl 4](/tech-tree/approximation-algorithms/)[Online Algorithmslvl 4](/tech-tree/online-algorithms/)

## Referenced by (11)

Where this concept shows up in the operating-finance and personal-finance graphs.

### From Business (9)

[Implementation CostBusiness

Greedy algorithms are the canonical paradigm of low implementation cost: simple local-choice logic, O(1) auxiliary state per step, and provably optimal when the problem has the matroid/greedy-choice property](/business/implementation-cost/)[personal financeBusiness

Debt avalanche (pay highest rate first) is a textbook greedy algorithm - locally optimal choice at each step yields globally optimal total interest paid](/business/personal-finance/)[decision treeBusiness

The canonical personal finance flowchart is a greedy algorithm - at each step it allocates the next dollar to the locally optimal use (highest guaranteed return), and the ordering works because the subproblems have optimal substructure](/business/decision-tree/)[Cost OptimizationBusiness

Prioritizing cuts by ROI is a greedy algorithm: always execute the highest-return cut next, exploiting optimal substructure where cuts are approximately independent](/business/cost-optimization/)[Total Interest PaidBusiness

Debt avalanche is a textbook greedy algorithm: always allocate the next marginal dollar to the highest-rate debt, and the greedy choice is provably globally optimal because interest costs are separable across balances](/business/total-interest-paid/)[Debt AvalancheBusiness

Debt avalanche is a textbook greedy algorithm: at each step allocate the extra dollar to the locally optimal choice (highest rate). Provably globally optimal here because the interest savings from each dollar are independent and additive - no overlapping subproblems, just optimal substructure.](/business/debt-avalanche/)[Debt SnowballBusiness

Debt snowball is a greedy algorithm - sort debts by balance, always attack the locally smallest. It doesn't minimize the global objective (total interest) but optimizes a different objective (motivation via quick wins). Avalanche is also greedy but on a different sort key (rate). Comparing the two illustrates how greedy criterion selection changes outcomes.](/business/debt-snowball/)[EBITDA OptimizationBusiness

Ranking cost programs by ROI and executing in descending order is a greedy algorithm - optimal when programs are independent, requires dynamic programming when they have dependencies](/business/ebitda-optimization/)[Exit SequencingBusiness

Sequencing cost programs by ROI is a greedy algorithm - select highest marginal return first given capacity constraints. Works when programs are roughly independent; breaks down when there are dependencies between initiatives.](/business/exit-sequencing/)

### From Money (2)

[Debt AvalancheMoney

Highest-rate-first is a greedy optimization strategy](/money/debt-avalanche/)[Debt SnowballMoney

Smallest-balance-first is a different greedy heuristic prioritizing behavioral wins over mathematical optimality](/money/debt-snowball/)

Advanced Learning Details

### Graph Position

44

Depth Cost

2

Fan-Out (ROI)

2

Bottleneck Score

3

Chain Length

### Cognitive Load

6

Atomic Elements

32

Total Elements

L1

Percentile Level

L4

Atomic Level

### All Concepts (15)

- - Greedy choice: the strategy of picking the best available option according to a local criterion at each step
- - Locally optimal choice (local optimum): a choice that is best among current feasible options without considering future choices
- - Greedy algorithm template/pattern: initialize an empty partial solution, repeatedly select a candidate by a selection rule, update the remaining instance, terminate with a complete solution
- - Feasible partial solution: a partial selection that can be extended to a complete valid solution
- - Candidate set (remaining options): the set of items/elements still available for selection at a given step
- - Greedy-choice property (formal): there exists an optimal solution that begins with the greedy choice for the instance
- - Optimal substructure in greedy context: after making the greedy choice, the remaining problem admits an optimal solution that combines with that choice to form a global optimum
- - Non-overlapping subproblems requirement for greedy: the subproblems produced after a greedy choice do not require recomputation of overlapping subproblems (contrast with dynamic programming)
- - Selection criterion / priority rule: the specific measurable key (e.g., earliest finish time, highest value/weight ratio) used to rank candidates
- - Tie-breaking policy: a deterministic rule for handling equal-selection-criterion candidates which can affect correctness
- - Exchange argument (greedy correctness proof technique): proof by showing any optimal solution can be transformed, via swaps, into one that starts with the greedy choice without worsening objective
- - Greedy-stays-ahead argument (alternative proof technique): prove the greedy partial solution is at least as good as any optimal partial solution at each step
- - Invariant-based correctness reasoning for greedy: identifying and proving a property preserved across steps that implies optimality at termination
- - Conditions under which greedy fails: examples or situations where local optimality does not imply global optimality (necessity of the greedy-choice property/structure)
- - Matroid/independence-system characterization (theoretical condition): a structural criterion on the feasible sets under which a simple greedy rule yields an optimal solution (advanced theoretical condition)

### Teaching Strategy

Deep-dive lesson - accessible entry point but dense material. Use worked examples and spaced repetition.

Greedy algorithms feel almost too simple: at each step, pick the best-looking option right now. Sometimes that intuition is disastrously wrong. But for an important class of problems, it’s exactly right—and we can prove it.

TL;DR:

A greedy algorithm builds a solution step-by-step, choosing an argmin/argmax option that preserves feasibility. It works when (1) a greedy-choice property holds (a locally optimal choice can be extended to a global optimum) and (2) the problem has optimal substructure. Proofs typically use an exchange argument or contradiction. Classic examples: interval scheduling, Huffman coding, and minimum spanning trees.

## What Is a Greedy Algorithm?

### Why this idea exists

Many algorithmic problems ask you to choose a *set* or *sequence* of items under constraints:

- •Choose activities that don’t overlap.
- •Build a cheapest network connecting cities.
- •Encode symbols with shortest average code length.

A brute-force approach considers all combinations—usually exponential. Dynamic programming (DP) can help when the problem has optimal substructure *and* overlapping subproblems. But not every problem has helpful overlap, and DP can still be heavier than necessary.

Greedy algorithms are the “lightweight” alternative: they commit early and never backtrack.

### Definition

A **greedy algorithm** constructs a solution incrementally. At each step it chooses the option that optimizes some local criterion, typically written using argmin/argmax:

- •**argmin** selects the *choice* that minimizes a score.
- •**argmax** selects the *choice* that maximizes a score.

For a set of candidate choices C and a scoring function score(c),

- •c⋆ = argmin\_{c ∈ C} score(c)
- •c⋆ = argmax\_{c ∈ C} score(c)

The key is that the algorithm commits to c⋆ and continues with the reduced subproblem.

### Three atomic concepts you must track

Greedy correctness is not magic; it rests on three pillars:

1) **Feasibility invariant**

At every step, your partial solution must remain valid. Greedy choices are only allowed if they keep the partial solution feasible.

2) **Greedy-choice property**

There exists an optimal solution that begins with the greedy choice. In other words, making the locally optimal choice does not “paint you into a corner.”

3) **Optimal substructure**

After making a choice, what remains is a smaller instance of the same problem, and an optimal solution to the whole contains an optimal solution to that remainder.

Greedy algorithms often apply when the problem has optimal substructure **without overlapping subproblems** (so DP offers less advantage), but that’s a heuristic, not a strict rule.

### The common greedy template

You’ll see this structure repeatedly:

1. 1)Define a local criterion (a score) to optimize.
2. 2)Initialize an empty partial solution S.
3. 3)While not done:

- •Pick c⋆ = argmin/argmax among feasible choices.
- •Add c⋆ to S.
- •Update the remaining candidates / constraints.

The hard part is not writing steps 2–3; it is justifying *why that local score implies global optimality*.

### A quick comparison table

| Approach | Core move | Typical use-case | Risk |
| --- | --- | --- | --- |
| Greedy | Commit to best local choice | Problems with greedy-choice property | Wrong criterion → wrong answer |
| Dynamic Programming | Explore choices, reuse subresults | Optimal substructure + overlapping subproblems | More time/memory |
| Brute force / backtracking | Explore all combinations | Small n or pruning | Exponential blowup |

The rest of this lesson is about recognizing the three pillars and proving correctness with standard proof patterns.

## Core Mechanic 1: Feasibility Invariants and Greedy Selection (argmin/argmax)

### Why feasibility comes first

A greedy algorithm *builds* a solution; if you ever make an infeasible move, you may not be able to recover because you don’t backtrack. So you should consciously separate two ideas:

- •**Feasibility**: “Is this partial solution allowed?”
- •**Optimality**: “Among feasible partial solutions, is this one best?”

A good greedy algorithm is designed so that each local decision is chosen from a set of *feasible* next moves.

### Feasibility invariant (formal-ish)

Let S\_k be the partial solution after k steps. A feasibility invariant is a statement P(S\_k) such that:

- •Base: P(S\_0) holds.
- •Step: If P(S\_k) holds and you choose a greedy step that is allowed, then P(S\_{k+1}) holds.

This is essentially an induction proof skeleton: you guarantee you never leave the feasible region.

### What argmin/argmax really means in greedy algorithms

Greedy choice is typically expressed as:

- •Choose c⋆ = argmax\_{c ∈ F(S)} gain(c, S)

where F(S) is the set of feasible next choices given current partial solution S.

Two important clarifications:

1) **argmax returns an argument, not a value**

If gain is maximized at c = 7 with gain(7) = 12, then argmax is 7, not 12.

2) **Ties are part of the algorithm**

If multiple choices tie, you must specify tie-breaking or prove any tie works. Many greedy proofs implicitly show “there exists an optimal solution consistent with *some* greedy tie.”

### Example of feasibility: Interval scheduling

Problem: Given intervals (start, finish), choose as many non-overlapping intervals as possible.

A feasibility invariant is:

- •S is a set of pairwise non-overlapping intervals.

A feasible next move is any interval that starts after (or at) the finish of the last chosen interval.

### Designing the local score: beware “obvious” criteria

A core skill is picking the right score. For interval scheduling, several plausible criteria exist:

| Greedy criterion | score | Works? | Why/why not |
| --- | --- | --- | --- |
| Earliest start time | min start | No | Can block many short intervals later |
| Shortest duration | min (finish − start) | No | Might pick a short interval that ends late |
| Earliest finish time | min finish | Yes | Leaves maximum room for future intervals |

Feasibility alone doesn’t guarantee optimality. The *choice rule* must align with the structure of optimal solutions.

### A reusable mental checklist

Before attempting a proof, ask:

1) What is the feasible set F(S) after partial solution S?

2) What invariant P(S) keeps the solution valid?

3) What score makes sense to optimize locally?

4) Can I imagine an exchange argument that replaces some optimal solution’s first step with the greedy step without getting worse?

If you can’t answer (4), your criterion may be wrong (or you need a different proof technique).

### Complexity notes (since you know Big-O)

Most greedy algorithms are dominated by:

- •Sorting: O(n log n)
- •Priority queue operations: O(n log n)
- •Linear scan: O(n)

So a common pattern is: sort once, then do a linear pass making greedy choices.

## Core Mechanic 2: Proving Greedy Correctness (Greedy-choice Property + Optimal Substructure)

### Why proofs matter more for greedy than for DP

DP is often correct because it considers all choices (then memoizes). Greedy commits to one choice, so the entire algorithm hinges on a statement like:

> “There exists an optimal solution that starts with the greedy choice.”

That is the **greedy-choice property**.

Once you have that, **optimal substructure** finishes the job: after making the greedy first choice, the remaining part must be solved optimally as a subproblem.

### The standard proof pattern: exchange arguments

An **exchange argument** proves that if you take any optimal solution OPT, you can transform it into another optimal solution OPT′ that agrees with the greedy choice, without worsening the objective.

The structure looks like:

1) Let g be the greedy choice (e.g., interval with earliest finish).

2) Consider an optimal solution OPT.

3) If OPT already contains g in the right place, great.

4) Otherwise, swap some element o in OPT with g.

5) Prove feasibility is preserved and objective value is not worse.

6) Conclude there exists an optimal solution starting with g.

This is usually a proof by contradiction in disguise: if greedy were wrong, you could produce an optimal solution that contradicts “optimal”.

### Worked mini-derivation: what “exchange” looks like

Suppose you maximize a count (like interval scheduling). Let OPT contain interval o as its first interval (by finish time ordering). Greedy picks g with the smallest finish time.

Because finish(g) ≤ finish(o), and both are feasible as first picks, then replacing o with g cannot reduce the number of intervals you can schedule after it (it only leaves *more* time).

That’s the intuition. The proof formalizes “leaves more time” as a subset relation between feasible remainders.

### Optimal substructure (how it appears in greedy proofs)

After selecting g, you form a subproblem on the remaining items consistent with g.

If the overall solution is optimal and starts with g, then what remains must be optimal for that subproblem. Otherwise you could improve the remainder and improve the whole.

This is often a short contradiction argument:

- •Assume remainder R is not optimal.
- •Then there exists R′ better than R.
- •Combine g + R′ to get a better full solution.
- •Contradiction.

### A second proof pattern: cut / prefix properties

Some greedy algorithms (notably minimum spanning trees) are proven via **cut properties**:

- •Consider a partition (cut) of the vertices.
- •The lightest edge crossing the cut is “safe” to add.

The underlying structure is still exchange-like: if an optimal solution doesn’t include that safe edge, you can swap it in.

### When greedy fails: a cautionary example

**0/1 Knapsack**: maximize value under weight limit W.

Greedy by value/weight ratio works for *fractional* knapsack, but fails for 0/1.

Example:

- •W = 50
- •Item A: w=10, v=60 (ratio 6)
- •Item B: w=20, v=100 (ratio 5)
- •Item C: w=30, v=120 (ratio 4)

Greedy by ratio picks A then B (w=30, v=160), remaining capacity 20, can’t take C.

But B + C fits exactly (w=50) with v=220, which is better.

What broke? The greedy-choice property: the locally best ratio item (A) is not guaranteed to be part of some global optimum.

### Practical takeaway

A greedy algorithm is not “a heuristic that often works.” In this node, “greedy algorithm” means:

- •You can state the feasibility invariant.
- •You can state the greedy choice rule as an argmin/argmax over feasible next moves.
- •You can prove greedy-choice property (usually via exchange).
- •You can invoke optimal substructure to finish.

If any of those pieces are missing, treat it as an unproven heuristic.

## Applications and Connections: Classic Greedy Problems (and What They Teach)

This section ties the mechanics to three canonical applications. The goal is not memorizing algorithms—it’s recognizing *why* the greedy step is safe.

## 1) Interval Scheduling (maximize number of non-overlapping intervals)

**Greedy rule:** pick the interval with earliest finish time among those compatible with what you’ve already chosen.

- •Selection: g = argmin\_{i feasible} finish(i)
- •Feasibility invariant: chosen intervals do not overlap.
- •Why it works: earliest finish leaves the largest feasible set for the future.

Complexity: sort by finish time O(n log n), then one pass O(n).

## 2) Huffman Coding (minimize expected code length)

Given symbol probabilities p(x), build a prefix code minimizing expected length ∑ p(x) ℓ(x).

**Greedy rule:** repeatedly merge the two least-probable symbols/subtrees.

- •Selection: pick a,b = two minima of p among current nodes.
- •{a,b} = argmin over pairs? Practically: use a min-heap.
- •Feasibility invariant: the code remains a valid prefix code (represented as a binary tree).
- •Why it works: in an optimal prefix code, the two least frequent symbols are siblings at maximum depth. Merging them reduces to an optimal subproblem.

Complexity: building with a heap is O(n log n).

## 3) Minimum Spanning Tree (MST)

Given an undirected weighted graph, connect all vertices with minimum total weight.

Two greedy algorithms:

| Algorithm | Greedy step | Data structure | Typical complexity |
| --- | --- | --- | --- |
| Kruskal | add the lightest edge that doesn’t form a cycle | sorting + DSU | O(m log m) |
| Prim | grow a tree by adding the lightest edge leaving the tree | priority queue | O(m log n) |

Feasibility invariant:

- •Kruskal: selected edges form an acyclic forest.
- •Prim: selected edges form a tree on a growing vertex set.

Why it works:

- •**Cut property**: For any cut, the lightest edge crossing it is safe.

## What these examples have in common

They all have a notion of “safe” local decisions:

- •Interval scheduling: earliest finishing is safe.
- •Huffman: merging two least-probable is safe.
- •MST: lightest edge across a cut is safe.

Each safety statement is proved by exchange: if an optimal solution doesn’t use the safe choice, swap it in.

## How this connects to what you unlock

1) **Approximation Algorithms**

For NP-hard problems, greedy often becomes an approximation method: even when greedy-choice property fails, you can bound how far from optimal you are.

2) **Online Algorithms**

Online decision-making is greedy-like by nature (no future info). Competitive analysis often evaluates greedy strategies against an optimal offline algorithm.

The mindset you built here—feasibility invariants + exchange-style reasoning—transfers directly to those areas.

## Worked Examples (3)

### Interval Scheduling via Earliest Finish Time (with an exchange argument)

You are given intervals: A(1,4), B(3,5), C(0,6), D(5,7), E(3,9), F(5,9), G(6,10), H(8,11), I(8,12), J(2,14), K(12,16). Goal: pick a maximum-size set of non-overlapping intervals.

1. Step 1: Define feasibility and the greedy rule.

   Feasible means no overlaps.

   Greedy choice at each step:

   g = argmin\_{i feasible} finish(i)

   (earliest finishing among those starting after the last finish).
2. Step 2: Sort intervals by finish time.

   A ends 4

   B ends 5

   C ends 6

   D ends 7

   E ends 9

   F ends 9

   G ends 10

   H ends 11

   I ends 12

   J ends 14

   K ends 16
3. Step 3: Greedy selection by scanning.

   Pick A(1,4). LastFinish=4.

   Next feasible start ≥ 4.

   Pick D(5,7). LastFinish=7.

   Next feasible start ≥ 7.

   Pick H(8,11). LastFinish=11.

   Next feasible start ≥ 11.

   Pick K(12,16). LastFinish=16.

   Solution S = {A, D, H, K} with |S|=4.
4. Step 4: Prove greedy-choice property (exchange sketch).

   Let g be the interval with minimum finish time among all intervals.

   Claim: There exists an optimal schedule OPT that includes g as its first chosen interval.

   Proof idea:

   - •Let o be the first interval in OPT (the one that finishes earliest among OPT’s chosen intervals).
   - •Since g has the globally minimum finish time, finish(g) ≤ finish(o).
   - •Replace o with g: OPT′ = (OPT \ {o}) ∪ {g}.

   Feasibility:

   - •g finishes no later than o, so every interval that started after finish(o) also starts after finish(g) (or at least remains feasible).

   Objective:

   - •OPT′ has the same number of intervals as OPT.

   Thus OPT′ is also optimal and starts with g.
5. Step 5: Invoke optimal substructure.

   After picking g, the remaining problem is: schedule intervals that start ≥ finish(g).

   If the remainder were not optimal, swapping in a better remainder would improve the whole schedule, contradicting optimality.

**Insight:** The key safety fact is: picking an interval that ends earlier can only enlarge the set of intervals still feasible later. That monotonicity makes the exchange argument work.

### Kruskal’s MST: Using the Cut Property to Justify a Greedy Edge

Graph with vertices {1,2,3,4} and weighted edges: (1,2)=1, (2,3)=2, (1,3)=3, (3,4)=4, (2,4)=5. Find an MST with Kruskal’s algorithm and justify one greedy step.

1. Step 1: Greedy rule + feasibility invariant.

   Greedy rule:

   pick e = argmin\_{edge not yet considered} weight(e)

   add e if it does not create a cycle.

   Invariant: selected edges form an acyclic forest (so always feasible to extend toward a spanning tree).
2. Step 2: Sort edges by weight.

   (1,2):1

   (2,3):2

   (1,3):3

   (3,4):4

   (2,4):5
3. Step 3: Run Kruskal.

   Start S = ∅.

   Add (1,2) (no cycle). S={(1,2)}.

   Add (2,3) (no cycle). S={(1,2),(2,3)}.

   Consider (1,3): adding would create a cycle 1-2-3-1, so skip.

   Add (3,4). S={(1,2),(2,3),(3,4)}.

   Now S has 3 edges connecting 4 vertices → spanning tree. Total weight = 1+2+4 = 7.
4. Step 4: Justify adding (1,2) via cut property (exchange-style).

   Consider cut: U={1}, V\U={2,3,4}.

   Edges crossing this cut: (1,2) weight 1, (1,3) weight 3.

   The lightest crossing edge is (1,2).

   Claim: There exists an MST that contains (1,2).

   Reason (exchange):

   - •Take any MST T.
   - •If T already contains (1,2), done.
   - •Otherwise, T must contain some edge crossing the cut to connect vertex 1 to others; call it e′.
   - •Since weight(1,2) ≤ weight(e′), replacing e′ with (1,2) keeps the graph connected and does not increase total weight.

   So we can transform T into an MST containing (1,2).
5. Step 5: Connect to the greedy-choice property.

   The argument shows the greedy edge (lightest safe edge) is “safe”: it can be part of some optimal solution, so committing to it does not prevent optimality.

**Insight:** MST greedy proofs often rely on a structural statement about optimal solutions across cuts: the lightest edge across a cut can be swapped into an MST. This is the exchange argument in graph form.

### A Greedy Failure: 0/1 Knapsack by Value/Weight Ratio

Capacity W=50. Items: A(w=10,v=60), B(w=20,v=100), C(w=30,v=120). Consider greedy by ratio v/w.

1. Step 1: Compute ratios.

   A: 60/10 = 6

   B: 100/20 = 5

   C: 120/30 = 4
2. Step 2: Apply greedy.

   Pick A first. Remaining capacity = 40, value=60.

   Pick B next. Remaining capacity = 20, value=160.

   Cannot pick C (needs 30). Greedy result value=160.
3. Step 3: Compare with optimal.

   Pick B + C:

   Total weight = 20 + 30 = 50 ≤ 50

   Total value = 100 + 120 = 220

   So 220 > 160.
4. Step 4: Identify what property failed.

   The greedy-choice property is false here:

   Even though A is locally best by ratio, there is no guarantee an optimal 0/1 solution includes A.

   Committing early can exclude the true best combination.

**Insight:** Greedy is not about a clever score; it’s about a score that matches the structure of optimal solutions. When item indivisibility matters, the exchange argument breaks.

## Key Takeaways

- ✓

  A greedy algorithm repeatedly picks a locally optimal feasible move: c⋆ = argmin/argmax\_{c ∈ F(S)} score(c, S).
- ✓

  Feasibility invariants ensure every prefix of the algorithm’s output remains a valid partial solution (crucial because greedy doesn’t backtrack).
- ✓

  Greedy is correct only when the greedy-choice property holds: some optimal solution begins with the greedy choice.
- ✓

  Optimal substructure completes correctness: after the greedy choice, the remainder must be solved optimally for the reduced instance.
- ✓

  Exchange arguments are the most common proof technique: transform an optimal solution to one that agrees with the greedy choice without worsening it.
- ✓

  Many greedy algorithms are O(n log n) due to sorting or priority queues, followed by a linear scan.
- ✓

  Classic correct greedy problems: interval scheduling (earliest finish), Huffman coding (merge least probabilities), MST (cut property).
- ✓

  Classic pitfall: plausible local scores (e.g., ratio for 0/1 knapsack) can fail because they don’t align with global structure.

## Common Mistakes

- ✗

  Choosing a local criterion because it sounds intuitive, without proving the greedy-choice property (result: a fast wrong algorithm).
- ✗

  Forgetting to state (and maintain) a feasibility invariant—especially in graph problems where cycles or disconnected components can silently appear.
- ✗

  Assuming “optimal substructure” alone implies greedy works; optimal substructure is necessary but not sufficient.
- ✗

  Ignoring tie-breaking: if multiple choices share the same score, you may need to show any tie works or specify how to break ties.

## Practice

easy

Interval scheduling: Give a counterexample showing that choosing the interval with the earliest start time can be suboptimal for maximizing the number of non-overlapping intervals.

**Hint:** Construct one long interval that starts earliest and overlaps many short intervals that start later.

Show solution

Example: intervals X(0,10), A(1,2), B(2,3), C(3,4), D(4,5).

Earliest-start greedy picks X first, yielding 1 interval.

Optimal picks A,B,C,D for 4 intervals.

medium

Prove (by exchange argument) that in interval scheduling, there exists an optimal solution whose first chosen interval is the one with minimum finish time among all intervals.

**Hint:** Let g be the min-finish interval. Compare it to the first interval o in an optimal solution OPT; swap o → g and show feasibility is preserved.

Show solution

Let g be an interval with minimum finish time. Let OPT be an optimal schedule, and let o be the interval in OPT that finishes first (so all other intervals in OPT start ≥ finish(o)).

Since finish(g) ≤ finish(o), replacing o with g keeps the schedule feasible: every interval that starts after finish(o) also starts after finish(g) (because finish(g) is earlier or equal).

The number of intervals stays the same, so the modified schedule is still optimal and starts with g.

hard

MST cut property practice: Let G be a connected weighted undirected graph, and let (S, V\S) be any cut. Prove that any minimum-weight edge e crossing the cut is safe (i.e., belongs to some MST).

**Hint:** Take an MST T. If T already contains e, done. Otherwise, add e to T to form a cycle; identify an edge e′ on the cycle that also crosses the cut, and swap it out.

Show solution

Let e be a minimum-weight edge crossing the cut (S, V\S). Take any MST T.

If e ∈ T, done.

Otherwise, add e to T. This creates a unique cycle C. Because e crosses the cut, the cycle must cross the cut at least twice, so there exists an edge e′ in C (e′ ≠ e) that also crosses the cut.

Remove e′ from T ∪ {e}. The graph remains connected (removing an edge from a cycle keeps connectivity), so we obtain a spanning tree T′.

Since e is minimum-weight among cut-crossing edges, w(e) ≤ w(e′). Therefore:

w(T′) = w(T) + w(e) − w(e′) ≤ w(T)

But T is an MST, so w(T′) = w(T) and T′ is also an MST containing e. Hence e is safe.

## Connections

[Approximation Algorithms](/tech-tree/approximation-algorithms/)

[Online Algorithms](/tech-tree/online-algorithms/)

[Dynamic Programming](/tech-tree/dynamic-programming/)

[Minimum Spanning Trees](/tech-tree/minimum-spanning-tree/)

[Huffman Coding](/tech-tree/huffman-coding/)

[Proof by Induction](/tech-tree/proof-by-induction/)

Quality: A (4.5/5)

[← back to tree](/tech-tree/)[browse all →](/tech-tree/inventory/)
