---
title: Dynamic Programming
description: Optimal substructure and overlapping subproblems. Memoization.
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
permalink: /tech-tree/dynamic-programming/
---

[←Back to Tech Tree](/tech-tree/)

[inventory](/tech-tree/inventory/)[coverage](/tech-tree/coverage/)

# Dynamic Programming

AlgorithmsDifficulty: ★★★☆☆Depth: 4Unlocks: 7

Optimal substructure and overlapping subproblems. Memoization.

## Interactive Visualization

⏮◀◀▶▶STEP0.25x1xZOOM

t=0s

## Core Concepts

- -Optimal substructure: an optimal solution composes from optimal solutions of smaller subproblems
- -Overlapping subproblems: the same subproblems recur multiple times in recursion
- -State definition: a minimal, unique set of parameters that identifies each subproblem

## Key Symbols & Notation

dp[state] (value/result stored for the subproblem identified by 'state')

## Essential Relationships

- -Optimal substructure AND overlapping subproblems => dynamic programming is applicable via defining dp[state]
- -Storing and reusing dp[state] (memoization or tabulation) removes repeated computation of the same subproblems

## Prerequisites (2)

[Recursion5 atoms](/tech-tree/recursion/)[Recurrence Relations5 atoms](/tech-tree/recurrence-relations/)

## Unlocks (3)

[Markov Decision Processeslvl 5](/tech-tree/mdp/)[Repeated Gameslvl 4](/tech-tree/repeated-games/)[Revenue Managementlvl 5](/tech-tree/revenue-management/)

## Referenced by (10)

Where this concept shows up in the operating-finance and personal-finance graphs.

### From Business (7)

[AllocationBusiness

Multi-period allocation (scheduling production, inventory over time) decomposes via Bellman equations. DP handles the temporal dimension that static LP cannot](/business/allocation/)[Inventory ControlBusiness

Multi-period inventory control (order or not each period, how much to order given current stock and uncertain future demand) is a canonical dynamic programming problem - optimal substructure over periods, Bellman equations yield (s,S) policies, and the technique directly solves stochastic inventory models](/business/inventory-control/)[investment sequencingBusiness

Optimal investment sequencing under budget and timeline constraints has classic DP structure - overlapping subproblems (shared infrastructure across programs) and optimal substructure (best 3-year sequence contains best 2-year subsequence)](/business/investment-sequencing/)[critical pathBusiness

Longest path in a DAG is solved by DP over the topological ordering: earliest\_finish[v] = max(earliest\_finish[u] + w(u,v)) for all predecessors u, a textbook DP recurrence with optimal substructure](/business/critical-path/)[tax strategyBusiness

Multi-year tax planning (Roth conversion sequencing, gain recognition timing, depreciation schedules) exhibits optimal substructure - current year decisions depend on future bracket projections](/business/tax-strategy/)[weighted votingBusiness

The polynomial-time algorithms for weighted voting use pseudo-polynomial DP over the weight-sum space to count winning coalitions and compute power indices](/business/weighted-voting/)[institutional knowledgeBusiness

Memoization is the computational analog of institutional knowledge - you solve subproblems once and cache results. Organizations without institutional knowledge re-solve the same problems repeatedly at full cost](/business/institutional-knowledge/)

### From Money (3)

[Student Loan StrategyMoney

IBR vs PSLF vs refinance forms a multi-stage sequential optimization](/money/student-loan-optimization/)[Roth Conversion LadderMoney

Multi-year conversion planning is a sequential decision optimization](/money/roth-conversion-ladder/)[FIRE MathMoney

Sequence-of-returns risk requires dynamic withdrawal strategy](/money/fire-math/)

Advanced Learning Details

### Graph Position

53

Depth Cost

7

Fan-Out (ROI)

4

Bottleneck Score

4

Chain Length

### Cognitive Load

6

Atomic Elements

38

Total Elements

L2

Percentile Level

L4

Atomic Level

### All Concepts (19)

- - Optimal substructure: the property that an optimal solution to a problem can be constructed from optimal solutions to its subproblems
- - Overlapping subproblems: the property that naive recursive decomposition revisits the same subproblem states multiple times
- - Memoization (top-down caching): storing results of solved subproblems in a lookup to avoid recomputation
- - Tabulation (bottom-up DP): iteratively filling a table of subproblem solutions in an order that respects dependencies
- - State: a minimal set of parameters that uniquely identifies a subproblem (e.g., index i, indices i,j, or other tuple)
- - State transition (DP recurrence-as-computation): the rule that computes a state's value from values of other states
- - DP table / memo map: explicit data structure that holds computed values for each state
- - Subproblem identification: the process of choosing states so the problem decomposes usefully into smaller problems
- - Computation order: choosing an order to compute states so all dependencies are available when needed
- - Redundant-computation recognition: understanding when recursion recomputes identical states
- - Initialization of base cases in the DP table (boundary conditions for the algorithm)
- - Space-time tradeoff in DP: using extra memory (cache/table) to reduce computation time
- - State-space size and its effect on complexity: how the number of distinct states determines runtime
- - Multi-dimensional states: representing subproblems with tuples (e.g., dp[i][j] for two parameters)
- - Rolling-array / space-optimization techniques: reducing memory by keeping only required prior states
- - Traceback / reconstruction: storing additional info during DP to recover the actual solution (not just its value)
- - Feasibility criteria for DP: when to apply DP - must have optimal substructure and overlapping subproblems
- - Mapping a mathematical recurrence to an algorithmic DP (translating recurrence relations into code that fills table or memoizes)
- - Cost per-state transitions: that computing a state's value may require iterating over multiple predecessor states (affects constants)

### Teaching Strategy

Multi-session curriculum - substantial prior knowledge and complex material. Use mastery gates and deliberate practice.

Dynamic programming (DP) is what you do when a recursive solution is “almost right”: it expresses the right logic, but it wastes time recomputing the same subproblems. DP keeps the logic and removes the waste by storing and reusing results.

TL;DR:

Use DP when a problem has (1) optimal substructure and (2) overlapping subproblems. Define a **state** that uniquely identifies a subproblem, write a recurrence for its answer, and compute each state once via memoization (top-down) or tabulation (bottom-up).

## Prerequisites and Expectations (Read This First)

This lesson assumes you already know recursion and recurrence relations. Dynamic programming builds directly on those ideas, but adds **state management** and **complexity counting**.

### What you should be comfortable with

1) **Recursion basics**

- •You can write a recursive function with a clear **base case** and **recursive case**.
- •You understand how recursion creates a call tree.

2) **Big-O and state-space counting (lightweight)**

- •You can estimate time by counting how many distinct subproblems exist, and how much work you do per subproblem.
- •You understand that recomputation in recursion can turn linear-looking recurrences into exponential time.

3) **Arrays / maps / dictionaries**

- •You can store values by index (arrays) or by key (hash maps).
- •You can initialize a table like `dp[n+1]` or `dp[n+1][m+1]`.

4) **Indexing and 2D tables**

- •You can reason about `dp[i]` and `dp[i][j]`, and iterate in nested loops.

### Common DP edge cases to watch for (we will revisit these)

- •**Top-down stack depth**: deep recursion can overflow the call stack; bottom-up avoids this.
- •**Integer overflow**: Fibonacci-style growth can exceed 32-bit integers quickly.
- •**Reconstruction**: sometimes you need not just the optimal value but also the choices; you’ll use **backpointers** or re-run decisions.
- •**State definition mistakes**: the #1 cause of broken DP solutions is a state that doesn’t uniquely capture what matters.

If any of these feel shaky, you can still proceed, but expect to pause and practice implementing small DP tables carefully.

## What Is Dynamic Programming?

Dynamic programming is a technique for solving problems by:

1) Breaking the problem into **subproblems**

2) Ensuring each subproblem is solved **once**

3) Combining subproblem solutions to solve larger problems

DP is not “one algorithm.” It’s a pattern.

### Why DP exists (motivation)

Many problems have a natural recursive definition. For example, Fibonacci numbers:

F(n)=F(n−1)+F(n−2),F(0)=0,  F(1)=1F(n) = F(n-1) + F(n-2), \quad F(0)=0,\; F(1)=1F(n)=F(n−1)+F(n−2),F(0)=0,F(1)=1

A direct recursive implementation mirrors the math, but it recomputes the same values repeatedly.

If you draw the recursion tree for F(6)F(6)F(6), you’ll notice the same subcalls appear many times (like F(3)F(3)F(3), F(2)F(2)F(2)). That repeated work is the key inefficiency.

### Two properties that make DP work

#### 1) Overlapping subproblems

The recursion generates the **same subproblems** again and again.

- •Example: Fibonacci repeatedly asks for F(3)F(3)F(3).

#### 2) Optimal substructure

An optimal solution to the whole problem can be formed from optimal solutions to its subproblems.

- •Example: shortest path in a DAG can be built from shortest paths to predecessors.

DP typically appears in **optimization** (min/max) problems, but it also applies to counting (number of ways), decision (is it possible?), and probability.

### The key symbol: dp[state]

We store the answer to a subproblem in a table:

- •`dp[state]` = the computed result for that subproblem

The entire art of DP often reduces to: **choose a good state** and **write a correct recurrence**.

### Two implementation styles

| Approach | Idea | Pros | Cons |
| --- | --- | --- | --- |
| Top-down (memoization) | Write recursion; cache results | Closest to the recursive logic; computes only needed states | Stack depth risk; overhead from recursion |
| Bottom-up (tabulation) | Fill dp table iteratively | No recursion; often faster in practice | Must find correct iteration order; may compute unused states |

You should be able to do both. Real interviews and real systems often benefit from being fluent in switching between them.

## Core Mechanic 1: State Definition (What Exactly Is a Subproblem?)

DP begins with a precise question:

> What information do I need to uniquely identify a subproblem?

That “information” is your **state**.

### What makes a good state?

A good DP state is:

- •**Minimal**: includes only what affects future decisions
- •**Unique**: two different states must not represent the same subproblem
- •**Composable**: you can compute the state’s answer from smaller states

If your state is missing information, your recurrence will “pretend” two different situations are the same. That produces wrong answers.

### State examples

#### Example A: Fibonacci

Subproblem: compute F(n)F(n)F(n).

State: just nnn.

So `dp[n]` is enough.

#### Example B: Grid paths (count ways)

Subproblem: number of ways to reach cell (i,j)(i,j)(i,j).

State: (i,j)(i,j)(i,j).

So `dp[i][j]`.

#### Example C: Knapsack

Subproblem: best value using first iii items with capacity www.

State: (i,w)(i,w)(i,w).

So `dp[i][w]`.

### The “state-space counting” habit

Once you define state, you can estimate complexity by counting how many states exist.

- •If `dp[n]`: you have nnn states → often O(n)O(n)O(n) time if each is O(1)O(1)O(1).
- •If `dp[i][w]` with i∈[0..n]i \in [0..n]i∈[0..n] and w∈[0..W]w \in [0..W]w∈[0..W]: you have (n+1)(W+1)(n+1)(W+1)(n+1)(W+1) states → often O(nW)O(nW)O(nW) time.

This is essential: DP often replaces exponential recursion with polynomial-time via “compute each state once.”

### A common pitfall: state that is too big

If you include unnecessary information in state, the number of states can explode.

Example: using the entire partial solution history as part of state makes DP infeasible.

### Another pitfall: state that is too small

If you leave out necessary information, you merge distinct subproblems.

Example idea: Suppose a path problem where whether you can step on a cell depends on whether you already used a “skip” power-up. Then state must include `usedSkip ∈ {0,1}`; `dp[i][j]` alone is too small.

### Practical guidance

When you’re stuck:

1) Write the recursive function signature you wish you had.

2) The arguments to that function are usually your state.

3) Then ask: can I memoize those arguments?

## Core Mechanic 2: Recurrence + Memoization (Top-Down DP)

Once you have a state, you need a recurrence: how do you compute `dp[state]` from smaller states?

### Why recurrence comes after state

If you don’t know what the subproblem is, you can’t correctly express how it relates to smaller subproblems.

### Template for top-down DP

You write a recursive function `solve(state)`:

1) If state is a base case, return base answer.

2) If answer is already memoized, return it.

3) Otherwise, compute answer by trying choices that reduce the problem.

4) Store in `dp[state]`, return it.

Pseudo-pattern:

```
solve(state):
  if base(state): return baseValue
  if dp has state: return dp[state]
  ans = combine( solve(nextState1), solve(nextState2), ... )
  dp[state] = ans
  return ans
```

### Example: Fibonacci with memoization

The recurrence is:

F(n)=F(n−1)+F(n−2)F(n)=F(n-1)+F(n-2)F(n)=F(n−1)+F(n−2)

A memoized version computes each F(k)F(k)F(k) once, turning exponential recursion into linear time.

Complexity:

- •States: n+1n+1n+1
- •Work per state: O(1)O(1)O(1)
- •Total time: O(n)O(n)O(n)
- •Space: O(n)O(n)O(n) for dp, plus recursion stack up to O(n)O(n)O(n)

### Edge case: stack depth

For large nnn (like $10^6$), recursion may overflow. That’s a reason to prefer bottom-up.

### Edge case: integer overflow

F(n)F(n)F(n) grows roughly like φn/5\varphi^n/\sqrt{5}φn/5​, so it exceeds 32-bit quickly (e.g., F(47)F(47)F(47) > 2³¹−1). Use 64-bit (`long long`) or big integers, or compute modulo.

### Memoization data structures

| State type | Good memo structure | Notes |
| --- | --- | --- |
| Single integer (n) | array/vector | fastest and simplest |
| Pair (i,j) bounded | 2D array | memory may be large: (n·m) |
| Complex/unbounded | hash map keyed by tuple/string | slower but flexible |

Memoization is conceptually simple, but it only works if your **state uniquely identifies** subproblems.

## Core Mechanic 3: Tabulation (Bottom-Up DP) and Ordering

Bottom-up DP computes answers for small states first, then builds up to the target.

### Why bottom-up exists

- •Avoid recursion stack limits
- •Often better constant factors
- •Naturally supports iterative reconstruction (when storing backpointers)

### The key requirement: a valid evaluation order

Your recurrence defines dependencies. You must fill the table so that when computing `dp[state]`, all required smaller states are already computed.

### Example: Fibonacci bottom-up

We can compute:

- •`dp[0]=0`
- •`dp[1]=1`
- •for `i=2..n`: `dp[i]=dp[i-1]+dp[i-2]`

This order works because `dp[i]` depends only on earlier indices.

### Example: grid paths ordering

If `dp[i][j]` depends on `dp[i-1][j]` and `dp[i][j-1]`, then scanning rows top-to-bottom and columns left-to-right works.

### Space optimization

Often you don’t need the whole table.

#### Fibonacci: O(1) space

Since `dp[i]` depends only on last two values:

- •Keep `prev2 = dp[i-2]`, `prev1 = dp[i-1]`.

#### General pattern

If state uses dimension `i` and only depends on `i-1`, you can compress:

- •from 2D `dp[i][w]` to 1D `dp[w]` (careful with iteration direction!)

### Caution: iteration direction matters

For 0/1 knapsack, if you compress `dp[i][w]` → `dp[w]`, you must iterate `w` descending to avoid reusing item `i` multiple times.

This is a classic DP bug: **same recurrence, wrong loop order, wrong meaning**.

## Application/Connection: DP as Bellman Equations (and Why It Unlocks MDPs)

DP isn’t just a coding trick; it’s a general method for sequential decision problems.

### DP as “value of a state”

In many problems, `dp[state]` represents the **best achievable value** from that state onward.

That’s exactly the mindset used in Markov Decision Processes (MDPs): define a value function over states.

### Bellman-style recurrence (intuition)

In optimization DP, a common form is:

dp[s]=min⁡a∈Actions(s)(cost(s,a)+dp[next(s,a)])dp[s] = \min\_{a \in Actions(s)} \big( cost(s,a) + dp[next(s,a)] \big)dp[s]=a∈Actions(s)min​(cost(s,a)+dp[next(s,a)])

or for maximizing rewards:

dp[s]=max⁡a∈Actions(s)(reward(s,a)+dp[next(s,a)])dp[s] = \max\_{a \in Actions(s)} \big( reward(s,a) + dp[next(s,a)] \big)dp[s]=a∈Actions(s)max​(reward(s,a)+dp[next(s,a)])

This is a **Bellman equation** idea: the value of a state equals the best immediate choice plus the value of the next state.

### Why DP prerequisites matter for MDPs

MDPs generalize DP to settings with uncertainty and expectations. Instead of `next(s,a)` being a single next state, it’s a distribution, and you compute expected value:

V(s)=max⁡a∑s′P(s′∣s,a)(R(s,a,s′)+γV(s′))V(s) = \max\_{a} \sum\_{s'} P(s'\mid s,a)\big(R(s,a,s') + \gamma V(s')\big)V(s)=amax​s′∑​P(s′∣s,a)(R(s,a,s′)+γV(s′))

If you understand:

- •defining a good state,
- •writing correct recurrences,
- •and computing them efficiently,

then Bellman equations feel like the same pattern, just with probabilities.

### DP in practice: beyond toy problems

DP appears in:

- •sequence alignment (bioinformatics)
- •edit distance / diff tools
- •parsing (context-free grammars)
- •resource allocation and scheduling
- •shortest paths on structured graphs

The recurring workflow is:

1) model as states

2) define transitions/choices

3) compute values efficiently

4) optionally reconstruct the solution path

## Worked Examples (3)

### Worked Example 1: Fibonacci — from Exponential Recursion to DP

Compute F(n) with F(0)=0, F(1)=1. Show why naive recursion is slow and how memoization/tabulation fix it.

1. Start from the recurrence:

   F(n)=F(n−1)+F(n−2)F(n)=F(n-1)+F(n-2)F(n)=F(n−1)+F(n−2)

   with base cases F(0)=0F(0)=0F(0)=0, F(1)=1F(1)=1F(1)=1.
2. Naive recursion (conceptually) calls:

   - •F(n) calls F(n-1) and F(n-2)
   - •F(n-1) calls F(n-2) and F(n-3)

   So F(n-2) is computed multiple times.

   This repeated computation grows rapidly, leading to about O(φn)O(\varphi^n)O(φn) time.
3. Define the DP state:

   - •State is just nnn
   - •Let `dp[n]` store F(n)F(n)F(n)
4. Top-down memoization derivation:

   - •If n≤1n \le 1n≤1, return nnn
   - •If `dp[n]` already filled, return it
   - •Else compute:

   dp[n]=solve(n−1)+solve(n−2)dp[n] = solve(n-1) + solve(n-2)dp[n]=solve(n−1)+solve(n−2)

   Store and return.
5. Complexity by state counting:

   - •Number of states: n+1n+1n+1
   - •Each state does O(1) work after memo hits

   So time is O(n)O(n)O(n) and space is O(n)O(n)O(n) (plus recursion stack).
6. Bottom-up tabulation:

   Initialize:

   - •`dp[0]=0`
   - •`dp[1]=1`

   Then for `i=2..n`:

   dp[i]=dp[i−1]+dp[i−2]dp[i]=dp[i-1]+dp[i-2]dp[i]=dp[i−1]+dp[i−2]
7. Space optimization:

   Because dp[i] uses only dp[i-1], dp[i-2], keep two variables:

   - •`a = F(i-2)`
   - •`b = F(i-1)`

   Update `c=a+b`, then shift.

**Insight:** DP doesn’t change the math recurrence. It changes the execution strategy: compute each subproblem once by caching (memoization) or ordering (tabulation).

### Worked Example 2: Minimum Cost Climbing Stairs (Classic 1D DP with Choices)

You have an array cost[0..n-1]. You can start at step 0 or 1. To reach the top (step n), you pay the cost of each step you land on, and you can climb 1 or 2 steps at a time. Find the minimum total cost.

1. Why DP?

   A recursive solution tries both move sizes at each step (1 or 2), which creates repeated subcalls for the same step index → overlapping subproblems.

   Also the optimal way to reach the top from step i uses optimal ways from i+1 and i+2 → optimal substructure.
2. Define state:

   Let `dp[i]` = minimum cost to reach step i (where i can be 0..n).

   Interpretation detail:

   - •Steps 0..n-1 have costs
   - •Step n is the "top" with no cost
3. Set base cases carefully:

   You can start at 0 or 1 without paying anything yet (you pay when you land on a step).

   A common clean setup:

   - •`dp[0]=0`
   - •`dp[1]=0`
4. Write the recurrence.

   To arrive at step i (for i ≥ 2), you came from i-1 or i-2.

   If you came from i-1, you must have paid cost[i-1] when stepping on i-1.

   If you came from i-2, you must have paid cost[i-2] when stepping on i-2.

   So:

   dp[i]=min⁡(dp[i−1]+cost[i−1],  dp[i−2]+cost[i−2])dp[i] = \min\big(dp[i-1] + cost[i-1],\; dp[i-2] + cost[i-2]\big)dp[i]=min(dp[i−1]+cost[i−1],dp[i−2]+cost[i−2])
5. Compute bottom-up:

   For i = 2..n:

   - •compute dp[i] from dp[i-1], dp[i-2]

   Return dp[n].
6. Complexity:

   - •States: n+1
   - •Work per state: O(1)

   So time O(n), space O(n), and space can be optimized to O(1) using two variables.

**Insight:** Good DP often comes from defining dp[i] as the best cost to reach position i, then carefully accounting for what cost is paid on the *previous* step. Most bugs are off-by-one or misinterpreting when costs apply.

### Worked Example 3: 0/1 Knapsack (2D DP + Reconstruction Idea)

Given n items, item i has weight wᵢ and value vᵢ. Capacity is W. Choose a subset (each item at most once) to maximize total value without exceeding W.

1. Why DP?

   A brute-force search over subsets is 2ⁿ. But the problem has optimal substructure: an optimal solution using first i items and capacity w depends on optimal solutions with first i-1 items.

   It also has overlapping subproblems because many subsets lead to the same (i, w) situation.
2. Define state:

   Let `dp[i][w]` = maximum value achievable using items 1..i with capacity w.

   State is (i, w). This uniquely identifies the subproblem.
3. Base cases:

   - •`dp[0][w]=0` for all w (no items, no value)
   - •`dp[i][0]=0` for all i (zero capacity, no value)
4. Recurrence (show both choices).

   For item i (weight wᵢ, value vᵢ):

   - •Exclude it: value = dp[i-1][w]
   - •Include it (only if wᵢ ≤ w): value = dp[i-1][w - wᵢ] + vᵢ

   So:

   dp[i][w]={max⁡(dp[i−1][w],  dp[i−1][w−wi]+vi)if wi≤wdp[i−1][w]if wi>wdp[i][w] = \begin{cases}
   \max\big(dp[i-1][w],\; dp[i-1][w-w\_i] + v\_i\big) & \text{if } w\_i \le w\\
   dp[i-1][w] & \text{if } w\_i > w
   \end{cases}dp[i][w]={max(dp[i−1][w],dp[i−1][w−wi​]+vi​)dp[i−1][w]​if wi​≤wif wi​>w​
5. Tabulation order:

   Compute i from 1..n, and for each i compute w from 0..W.

   This ensures dp[i-1][*] is ready before dp[i][*].
6. Complexity:

   - •States: (n+1)(W+1)
   - •Work per state: O(1)

   So time O(nW), space O(nW).
7. Reconstruction (what items were chosen):

   After filling dp, start at (i=n, w=W) and walk backward:

   - •If dp[i][w] == dp[i-1][w], item i was not chosen → i ← i-1
   - •Else item i was chosen → record i, and w ← w - wᵢ, i ← i-1

   This is a backpointer-by-comparison technique; alternatively store explicit `choice[i][w]`.

**Insight:** Knapsack shows the full DP workflow: define a 2D state, write a max recurrence over choices, fill the table in dependency order, and optionally reconstruct the actual optimal subset with backtracking.

## Key Takeaways

- ✓

  Dynamic programming applies when you have **overlapping subproblems** and **optimal substructure**.
- ✓

  The hardest (and most important) step is defining the **state**: the minimal information that uniquely identifies a subproblem.
- ✓

  `dp[state]` stores the answer for that state; DP’s speed comes from computing each state once.
- ✓

  Top-down DP (memoization) keeps recursive structure but can hit recursion depth limits; bottom-up DP (tabulation) avoids recursion and needs a correct fill order.
- ✓

  Estimate DP time/space by **counting states** × **work per state**.
- ✓

  Loop order and indexing define meaning; the same recurrence can become wrong if you fill in the wrong direction (especially in compressed knapsack).
- ✓

  Many DP problems also need **reconstruction**; plan to store backpointers or enable backward tracing through the dp table.
- ✓

  DP is the algorithmic foundation for Bellman equations and helps prepare you for MDPs and reinforcement learning value functions.

## Common Mistakes

- ✗

  Choosing a state that is missing a crucial variable (merging distinct subproblems and producing incorrect results).
- ✗

  Off-by-one errors in base cases and table size (e.g., confusing dp over indices 0..n-1 vs 0..n).
- ✗

  Using top-down recursion for very large depths and crashing due to stack overflow; switching to bottom-up fixes it.
- ✗

  Forgetting numeric limits (integer overflow) or failing to store enough info to reconstruct the optimal solution (no backpointers / no traceback plan).

## Practice

easy

Compute the number of distinct ways to climb n stairs if you can climb 1 or 2 steps at a time. Return the answer for n (assume n ≥ 0). Define a DP state and recurrence, and give the time and space complexity.

**Hint:** Let dp[i] be the number of ways to reach step i. Think about dp[i-1] and dp[i-2]. Be careful with dp[0].

Show solution

State: dp[i] = # ways to reach step i.

Base: dp[0]=1 (one way to be at the start), dp[1]=1.

Recurrence for i≥2:

dp[i]=dp[i−1]+dp[i−2]dp[i]=dp[i-1]+dp[i-2]dp[i]=dp[i−1]+dp[i−2]

Answer: dp[n].

Complexity: O(n) time, O(n) space (or O(1) with two variables).

medium

Given a 2D grid of nonnegative costs cost[i][j], find the minimum cost path from (0,0) to (n-1,m-1) moving only right or down. Write the DP recurrence and describe a valid fill order.

**Hint:** Let dp[i][j] be the minimum cost to reach (i,j). Handle first row/column separately or via sentinel values.

Show solution

State: dp[i][j] = min cost to reach cell (i,j).

Base: dp[0][0] = cost[0][0].

For i>0, j>0:

dp[i][j]=cost[i][j]+min⁡(dp[i−1][j],  dp[i][j−1])dp[i][j] = cost[i][j] + \min\big(dp[i-1][j],\; dp[i][j-1]\big)dp[i][j]=cost[i][j]+min(dp[i−1][j],dp[i][j−1])

First row: dp[0][j] = cost[0][j] + dp[0][j-1].

First column: dp[i][0] = cost[i][0] + dp[i-1][0].

Fill order: i from 0..n-1, j from 0..m-1 (row-major) works because dependencies are top and left.

hard

0/1 Knapsack space optimization: Starting from dp[i][w], compress to 1D dp[w]. Explain why iterating w from W down to wᵢ is necessary, and give the 1D recurrence.

**Hint:** If you iterate w upward, dp[w-wᵢ] may already include item i, turning 0/1 knapsack into unbounded knapsack.

Show solution

Use dp[w] = best value with capacity w using items processed so far.

For each item i, update:

For w = W down to wᵢ:

dp[w]=max⁡(dp[w],  dp[w−wi]+vi)dp[w] = \max\big(dp[w],\; dp[w-w\_i] + v\_i\big)dp[w]=max(dp[w],dp[w−wi​]+vi​)

Descending order ensures dp[w-wᵢ] is from the previous iteration of i (i-1 items), so item i is used at most once. Ascending would allow reusing item i multiple times because dp[w-wᵢ] might have already been updated with item i.

## Connections

Next, DP becomes a *framework* for sequential decision making via Bellman equations:

- •[Markov Decision Processes](/tech-tree/mdp/)

Related algorithmic patterns you’ll likely connect after DP:

- •[Recursion](/tech-tree/recursion/)
- •[Big-O Analysis](/tech-tree/big-o/)
- •[Graph Shortest Paths](/tech-tree/shortest-paths/)
- •[Greedy Algorithms](/tech-tree/greedy/)
- •[Divide and Conquer](/tech-tree/divide-and-conquer/)

Quality: A (4.4/5)

[← back to tree](/tech-tree/)[browse all →](/tech-tree/inventory/)
