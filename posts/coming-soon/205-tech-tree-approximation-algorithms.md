---
title: Approximation Algorithms
description: Finding near-optimal solutions for hard problems.
date: '2026-07-01'
scheduled: '2027-01-21'
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
inspiration_url: https://templeton.host/tech-tree/approximation-algorithms/
inspiration_category: tech-tree
---

> Source-copy draft imported from [https://templeton.host/tech-tree/approximation-algorithms/](https://templeton.host/tech-tree/approximation-algorithms/). Names, domain references, and local media paths were adapted for Xavi Ablaza / getablaza.com.

[←Back to Tech Tree](/tech-tree/)

[inventory](/tech-tree/inventory/)[coverage](/tech-tree/coverage/)

# Approximation Algorithms

AlgorithmsDifficulty: ★★★★☆Depth: 5Unlocks: 0

Finding near-optimal solutions for hard problems.

## Interactive Visualization

⏮◀◀▶▶STEP0.25x1xZOOM

t=0s

## Core Concepts

- -Approximation ratio (multiplicative performance guarantee on solution quality)
- -Polynomial-time approximation algorithm (an algorithm running in polynomial time that returns feasible solutions for NP-hard optimization problems)

## Key Symbols & Notation

OPT (cost or value of an optimal solution)rho (approximation factor, a multiplicative constant >= 1)

## Essential Relationships

- -For every instance, algorithm\_cost / OPT <= rho (this inequality formally defines a rho-approximation)

## Prerequisites (2)

[NP-Completeness6 atoms](/tech-tree/np-completeness/)[Greedy Algorithms6 atoms](/tech-tree/greedy-algorithms/)

Advanced Learning Details

### Graph Position

70

Depth Cost

0

Fan-Out (ROI)

0

Bottleneck Score

5

Chain Length

### Cognitive Load

5

Atomic Elements

57

Total Elements

L4

Percentile Level

L3

Atomic Level

### All Concepts (25)

- - Approximation algorithm: an algorithm that runs in polynomial time and returns a feasible (not necessarily optimal) solution with a provable guarantee on closeness to optimal
- - Approximation ratio / approximation factor: a multiplicative guarantee comparing algorithm output to OPT
- - Performance guarantee (worst-case guarantee): the approximation ratio holds for every instance, not just on average
- - Additive vs multiplicative error: difference between guaranteeing |ALG - OPT| ≤ c (additive) and ALG ≤ α·OPT or ALG ≥ OPT/α (multiplicative)
- - Definitions specialized by objective type: distinct formalizations for minimization problems and maximization problems
- - Polynomial-Time Approximation Scheme (PTAS): family of algorithms that for any ε>0 produce a (1+ε)-approximate solution in polynomial time for fixed ε
- - Fully Polynomial-Time Approximation Scheme (FPTAS): PTAS whose running time is polynomial in both input size and 1/ε
- - Approximation class APX: class of problems that admit constant-factor polynomial-time approximations
- - APX-hardness and APX-completeness: hardness notions in the approximation context (problems as hard as the hardest in APX under approximation-preserving reductions)
- - Inapproximability: formal lower bounds showing no polynomial-time algorithm can achieve a given approximation ratio unless complexity assumptions fail (e.g., P=NP)
- - Approximation-preserving reductions (gap-preserving, L-reduction, PTAS-reduction, etc.): reductions that transfer approximation ratios or impossibility results between problems
- - Approximation scheme trade-offs: the runtime vs accuracy trade-off parameterized by ε
- - Integrality gap: worst-case ratio between integer optimum and relaxation optimum (e.g., LP relaxation)
- - Linear-program (LP) relaxation for combinatorial optimization: replacing integrality constraints with continuous ones to obtain a bound and a fractional solution
- - Rounding techniques: methods to convert fractional relaxation solutions into integer solutions with bounded loss (deterministic rounding, randomized rounding)
- - Randomized approximation algorithms and probabilistic guarantees: algorithms that use randomness and provide expected/with-high-probability approximation bounds
- - Primal-dual method for approximation: deriving feasible integral solutions and performance bounds by simultaneous consideration of primal and dual LPs
- - Local search as an approximation technique: iteratively improving a solution within a neighborhood until local optimum with provable approximation ratio
- - Specific canonical approximation results as exemplars: e.g., 2-approx for Vertex Cover (via maximal matching), H\_n-approx for Set Cover (via greedy), 1.5-approx for metric TSP (Christofides)
- - Approximation threshold: the boundary ratio separating achievable approximation from impossible ones under complexity assumptions
- - Gap amplification / PCP-based techniques for hardness of approximation: methods showing tight inapproximability factors via probabilistically checkable proofs
- - Pseudo-polynomial algorithms and scaling approaches used to obtain FPTAS for problems like Knapsack
- - Worst-case instance / hard instance construction used to prove lower bounds on approximability
- - Integrality gap instance: a concrete instance demonstrating the gap between relaxation and integer optimum
- - Approximation-preserving hardness proofs: how to build reductions that maintain approximation ratios (constructing gap instances explicitly)

### Teaching Strategy

Quick unlock - significant prerequisite investment but simple final step. Verify prerequisites first.

Many real optimization problems are NP-hard: you likely can’t get the exact optimum in polynomial time (unless P = NP). Approximation algorithms embrace this reality and ask a different question: can we guarantee a solution that is provably close to optimal—every time—fast?

TL;DR:

An approximation algorithm is a polynomial-time algorithm for an NP-hard optimization problem that always returns a feasible solution with a provable bound vs. OPT. For minimization, an ρ-approximation guarantees cost(A) ≤ ρ·OPT; for maximization, value(A) ≥ OPT/ρ. Core tools include greedy with exchange arguments, LP relaxations + rounding, and primal–dual methods. You also learn how to reason about what is (and isn’t) approximable.

## What Is an Approximation Algorithm?

### Why we need approximation

In NP-completeness, the central story is often *decision* problems: “Is there a solution of size ≤ k?” But in practice, we usually care about *optimization*: “What is the smallest cost?” or “What is the largest value?”

Many optimization problems are NP-hard. If we insist on exact optimality, we’re often stuck with exponential time. Approximation algorithms change the success criterion:

- •**Goal**: run in **polynomial time**
- •**Output**: a **feasible** solution (it must satisfy constraints)
- •**Guarantee**: its quality is within a known factor of **OPT** (the optimal objective value)

This is not “it seems good on average.” The defining feature is a **worst-case, provable** performance guarantee.

### Optimization problems: minimization vs. maximization

Let an instance be x, and let OPT(x) be the objective value of an optimal solution.

- •**Minimization** (e.g., shortest tour): smaller is better.
- •**Maximization** (e.g., maximum coverage): larger is better.

The approximation ratio must respect this direction.

### Approximation ratio (multiplicative guarantee)

We use **ρ ≥ 1** as the approximation factor.

**Minimization**: Algorithm A is a **ρ-approximation** if for every instance x,

cost(A(x)) ≤ ρ · OPT(x)

**Maximization**: Algorithm A is a **ρ-approximation** if for every instance x,

value(A(x)) ≥ OPT(x) / ρ

These are equivalent to:

- •Minimization: cost(A)/OPT ≤ ρ
- •Maximization: OPT/value(A) ≤ ρ

The important feature is **multiplicative** comparison. If OPT is huge, we allow proportionally larger absolute error.

### What the guarantee does—and doesn’t—say

A 2-approximation for a minimization problem does **not** mean “within 2 units.” It means “within a factor of 2.”

If OPT = 10, you guarantee ≤ 20.

If OPT = 10⁶, you guarantee ≤ 2·10⁶.

That can feel weak, but for NP-hard problems it’s often the right currency: factors are stable across scales.

### Polynomial-time approximation algorithm

A **polynomial-time approximation algorithm** is simply an approximation algorithm whose running time is poly(n), where n is the input size.

There is a family of stronger notions you may encounter:

| Name | Guarantee form | Typical meaning |
| --- | --- | --- |
| Constant-factor approximation | ρ is a fixed constant (e.g., 2, 3/2) | Best you can do for some problems |
| PTAS | For any ε > 0, returns (1+ε)-approx (min) in poly(n) time for fixed ε | Very accurate, but can be slow as ε → 0 |
| FPTAS | Like PTAS but poly(n, 1/ε) | Efficient even for small ε |

This lesson focuses on the core constant-factor mindset and the techniques that produce it.

### A mental model: “Relax, solve, repair”

A repeating pattern in approximation:

1. 1)**Relax** the hard problem into an easier one (often linear programming)
2. 2)**Solve** the relaxed problem optimally (poly-time)
3. 3)**Repair** the relaxed solution into a feasible integral solution (rounding, pruning, greedy)
4. 4)**Prove** the repair step loses at most a factor ρ

The “prove” step is the heart: you must compare your output to OPT even though you never computed OPT.

### Why approximation is different from heuristics

Heuristics can work well empirically, but without a worst-case guarantee they can fail arbitrarily badly. Approximation algorithms sit in between exact algorithms and heuristics:

- •Like heuristics: practical and polynomial-time
- •Like exact algorithms: come with correctness-style proofs (feasibility + bound)

The guarantee is what makes approximation a rigorous subfield of algorithms.

## Core Mechanic 1: Proving Approximation Ratios (Charging, Exchange, and Certificates)

### Why proofs matter here

For NP-hard optimization, you don’t have an efficient way to check “how close” you are to OPT. So approximation analysis needs a substitute: a *certificate* that your solution cannot be too far from OPT.

A typical proof has two ingredients:

1. 1)**Upper bound your algorithm’s cost/value** in terms of something you can track.
2. 2)**Lower/upper bound OPT** using a structural argument (or LP relaxation), then relate the two.

This section builds the proof toolbox.

---

## 1) Lower bounds on OPT

To show cost(A) ≤ ρ·OPT (minimization), it’s enough to show:

- •cost(A) ≤ ρ·LB
- •and LB ≤ OPT

Then cost(A) ≤ ρ·OPT.

Common lower bounds LB:

- •**Packing/covering arguments**: any feasible solution must “pay” at least X.
- •**Disjointness**: if you can identify k disjoint requirements, each costs ≥ 1, then OPT ≥ k.
- •**LP relaxation value**: LP\* ≤ OPT for minimization? Careful—direction depends on formulation.
- •For minimization: relaxed feasible set is larger → optimum can only get *smaller*, so LP\* ≤ OPT.
- •Thus OPT is ≥ LP *(LP* is a lower bound).

For maximization, it flips:

- •Relaxation gives LP\* ≥ OPT (an upper bound on OPT).

---

## 2) Charging arguments

A charging argument “pays for” your solution using the lower bound’s budget.

Example template (minimization):

- •Break your algorithm’s cost into pieces.
- •Map each piece to a distinct piece of the lower bound.
- •Show no LB piece is charged more than ρ times.

This yields cost(A) ≤ ρ·LB ≤ ρ·OPT.

Charging is common for covering problems (Vertex Cover, Set Cover) and clustering.

---

## 3) Exchange arguments (greedy analysis)

Greedy algorithms often come with **exchange arguments**:

- •Consider an optimal solution S\*.
- •Show how to transform S\* step-by-step to match the greedy solution S, without making it much worse.

Even when greedy is not optimal, you can often show it is “not too bad.”

An exchange argument usually needs a *local improvement inequality* like:

cost(greedy choice) ≤ cost(what OPT would do instead)

or a bound that each greedy step can be “charged” to a limited number of OPT elements.

---

## 4) A careful note on ρ and problem direction

It’s easy to mix up minimization vs. maximization.

- •Minimization guarantee: cost(A) / OPT ≤ ρ
- •Maximization guarantee: OPT / value(A) ≤ ρ

When writing a proof, keep the inequality direction explicit at every step.

---

## 5) Worked proof skeleton: turning a lemma into an approximation ratio

Suppose you can prove these two lemmas (minimization):

1. 1)(**Algorithm bound**) cost(A) ≤ 2·M
2. 2)(**OPT bound**) OPT ≥ M

Then:

cost(A) ≤ 2·M

≤ 2·OPT

So A is a 2-approximation.

This “M” could be:

- •size of a matching
- •value of an LP relaxation
- •number of disjoint constraints
- •a dual variable sum in primal–dual methods

The rest of approximation design is often about inventing the right M and proving both lemmas.

## Core Mechanic 2: Design Patterns (Greedy, LP Rounding, Primal–Dual)

Approximation algorithms are not a single technique; they are a collection of *design patterns* that repeatedly work across problem families. We’ll focus on three big ones.

---

## Pattern A: Greedy + structure (classic constant factors)

### Why greedy sometimes approximates well

Greedy is tempting because it’s simple. For NP-hard problems, greedy rarely hits OPT, but it can still be provably close when:

- •each greedy choice can be related to a lower bound on OPT
- •or each greedy choice “covers” requirements efficiently

**Vertex Cover** is a canonical example: a simple greedy algorithm based on matching yields a 2-approximation.

Key idea: find a structure that OPT must pay for (like a matching), then show greedy pays at most a constant multiple.

---

## Pattern B: LP relaxation + rounding

### Why linear programming helps

Many NP-hard problems can be written as integer programs:

- •variables are 0/1 (choose item or not)
- •constraints encode feasibility
- •objective encodes cost/value

If we relax integrality (allow variables in [0, 1]), we get an LP solvable in polynomial time.

This helps because:

1. 1)The LP optimum provides a bound on OPT.
2. 2)The fractional solution suggests where “mass” should go.
3. 3)Rounding converts fractional to integral with controlled loss.

### The rounding step is where approximation lives

A common rounding rule is thresholding:

- •if xᵢ ≥ 1/2, set xᵢ = 1
- •else set xᵢ = 0

Then prove feasibility and cost inflation ≤ 2.

There are more advanced forms:

| Rounding type | Idea | Where it appears |
| --- | --- | --- |
| Deterministic threshold | Choose if xᵢ ≥ τ | Vertex cover, facility location variants |
| Randomized rounding | Choose i with probability xᵢ | Set cover, max satisfiability |
| Dependent rounding | Preserve sums/constraints correlations | Matroids, scheduling |

### Integrality gap

The **integrality gap** is:

(Integral OPT) / (LP OPT) for minimization (≥ 1)

If the gap is large, no rounding can beat it *for that LP*.

So approximation design is partly about choosing a relaxation with a small integrality gap.

---

## Pattern C: Primal–dual methods

### Why primal–dual works

Primal–dual is a technique for *covering* problems where you can write:

- •a primal LP (minimization)
- •a dual LP (maximization)

The dual optimum is a lower bound on the primal optimum by weak duality:

Dual *≤ Primal*

Because for minimization:

LP\* (primal) ≤ OPT (integral)

If we build a feasible dual solution along the way, we get a **certified lower bound** we can compare against.

### Intuition

Primal–dual algorithms grow dual variables until some primal constraint becomes “tight,” then they add the corresponding primal variable.

Think of it as:

- •dual variables are “prices” paid by constraints
- •once enough price accumulates to justify buying a primal element, you buy it

The approximation ratio comes from bounding how many times any dual dollar is used to pay for primal purchases.

This is a cousin of charging arguments, but organized via LP duality.

---

## A note about hardness of approximation

Approximation algorithms also have limits: for some problems, getting a factor better than ρ is NP-hard.

This is the topic of **hardness of approximation** (PCP theorem, gap reductions). You don’t need the full theory to benefit from approximation algorithms, but it’s important context:

- •Some problems admit PTAS (e.g., Euclidean TSP under certain metrics).
- •Some admit constant-factor but not PTAS (under standard complexity assumptions).
- •Some are hard to approximate within any constant factor.

In practice, you often choose a target ρ that is known to be achievable and meaningful.

## Application/Connection: Canonical Approximation Algorithms (Vertex Cover, Metric TSP) and How to Use the Mindset

This section anchors the ideas in two landmark results: a clean greedy 2-approximation for **Vertex Cover**, and a 3/2-approximation for **Metric TSP** (Christofides). The goal is not just to memorize algorithms, but to see how approximation thinking connects to structure and lower bounds.

---

## 1) Vertex Cover: a 2-approximation via matching

### Problem

Given graph G = (V, E), find the smallest set C ⊂ V such that every edge has at least one endpoint in C.

This is NP-hard, but approximable.

### Algorithm (maximal matching)

1. 1)Compute a **maximal matching** M (a set of disjoint edges such that you can’t add another edge without breaking disjointness).
2. 2)Output C = all endpoints of edges in M.

### Why it works

- •**Feasibility**: If an edge e were uncovered, neither endpoint is in C. Then e is disjoint from all edges in M and could be added, contradicting maximality. Therefore C covers all edges.

- •**Approximation ratio**: Any vertex cover must include at least one endpoint of each matching edge, and matching edges are disjoint. Thus:

OPT ≥ |M|

Our solution includes **two** vertices per matching edge:

Therefore:

|C| = 2|M| ≤ 2·OPT

This is a perfect illustration of the pattern:

- •M is the lower bound certificate
- •the algorithm’s cost is at most 2× that certificate

---

## 2) Metric TSP: Christofides’ 3/2-approximation

### Problem

Given complete graph with distances d(u, v) satisfying the triangle inequality:

d(u, w) ≤ d(u, v) + d(v, w)

Find a minimum-length Hamiltonian cycle.

General TSP is very hard to approximate, but **metric** TSP allows strong structure.

### Why triangle inequality changes everything

In metric spaces, “shortcuts” don’t hurt:

If a tour visits … → a → b → c → … then replacing a → b → c by a → c does not increase length because:

d(a, c) ≤ d(a, b) + d(b, c)

This enables many approximation proofs.

### Christofides algorithm (high level)

1. 1)Compute a **minimum spanning tree** (MST) T.
2. 2)Let O be the set of vertices of odd degree in T.
3. 3)Compute a **minimum-weight perfect matching** on O (call it M).
4. 4)Combine edges T ∪ M to form an Eulerian multigraph (all degrees even).
5. 5)Find an Eulerian tour and shortcut repeated vertices to get a Hamiltonian cycle.

### The guarantee idea: bound against OPT using MST and matching

Two key facts (sketch-level but standard):

1) MST is a lower bound on OPT:

Let OPT be the optimal tour length. Removing one edge from the optimal tour gives a spanning tree, so:

w(MST) ≤ OPT

2) The minimum perfect matching on odd-degree vertices is not too large:

Using the optimal tour, consider the odd-degree set O. In any cycle, the vertices of O appear in some order; you can pair them along the tour edges to form a perfect matching whose total weight is ≤ OPT/2. Since M is minimum,

w(M) ≤ OPT/2

Now add them:

w(T ∪ M) = w(T) + w(M)

≤ OPT + OPT/2

= 3OPT/2

Shortcutting does not increase length (triangle inequality), so the final Hamiltonian tour has length ≤ 3OPT/2.

This is a more complex version of the same pattern:

- •Find lower bounds (MST ≤ OPT)
- •Find a complementary structure (matching ≤ OPT/2)
- •Combine them and use triangle inequality to preserve the bound

---

## 3) Using the approximation mindset in new problems

When you face an NP-hard optimization problem, ask:

1. 1)**What is OPT forced to pay for?** (a lower bound: matching, MST, LP value, disjoint constraints)
2. 2)**Can I build a solution whose cost is a small multiple of that forced payment?**
3. 3)**What structure is present?** (metric, submodular, bipartite, bounded degree)
4. 4)**Is there an LP/dual that can serve as a certificate?**

Often, you don’t need a fancy algorithm—just the right lower bound and a proof that your construction doesn’t overpay.

## Worked Examples (3)

### 2-Approximation for Vertex Cover via Maximal Matching

You are given a graph G = (V, E). Run the maximal matching algorithm: build a matching M by repeatedly picking any uncovered edge and adding it to M, deleting all edges incident to its endpoints. Output C as all endpoints of edges in M. Prove feasibility and the 2-approximation ratio.

1. Construct M by the greedy matching process. By construction, M is a matching (edges are disjoint). It is also maximal: once the process stops, every edge shares an endpoint with some edge in M.
2. Define C = { all endpoints of edges in M }. Then |C| = 2|M| because matching edges have disjoint endpoints.
3. Feasibility proof:

   Assume for contradiction there exists an uncovered edge e = (u, v) ∈ E with u ∉ C and v ∉ C.

   Then neither u nor v is an endpoint of any edge in M.

   So e is disjoint from all edges in M, meaning we could add e to M, contradicting maximality.

   Therefore C covers every edge and is a valid vertex cover.
4. Lower bound on OPT:

   Let M = {e₁, e₂, …, e\_k}.

   Any vertex cover must cover each eᵢ.

   Because the eᵢ are disjoint, covering e₁ uses at least 1 vertex, covering e₂ uses at least 1 *different* vertex, etc.

   So any vertex cover has size ≥ k.

   Thus OPT ≥ |M|.
5. Approximation ratio:

   ≤ 2·OPT

   So the algorithm is a 2-approximation for minimum vertex cover.

**Insight:** The matching provides a clean, instance-specific lower bound on OPT. The algorithm never needs to guess OPT; it only needs to ensure it pays at most 2 per unit of that bound.

### LP Relaxation + 1/2-Threshold Rounding for Vertex Cover (2-Approx)

Formulate Vertex Cover as an integer program, relax it to an LP, then round: choose every vertex with xᵥ ≥ 1/2. Prove the rounded solution is feasible and costs at most 2 times OPT.

1. Integer program (minimization):

   Variables: xᵥ ∈ {0, 1} for each vertex v (1 means chosen).

   Objective: minimize ∑\_{v∈V} xᵥ.

   Constraints: for each edge (u, v) ∈ E,

   xᵤ + xᵥ ≥ 1 (at least one endpoint chosen).
2. LP relaxation:

   Replace xᵥ ∈ {0, 1} with 0 ≤ xᵥ ≤ 1.

   Let LP\* be the optimal LP value.

   Because the LP feasible set includes all integral solutions,

   LP\* ≤ OPT.

   So LP\* is a lower bound on OPT.
3. Rounding rule:

   Construct C = { v ∈ V : xᵥ ≥ 1/2 }, where x is an optimal LP solution.
4. Feasibility:

   Take any edge (u, v).

   The LP constraint says xᵤ + xᵥ ≥ 1.

   If both xᵤ < 1/2 and xᵥ < 1/2, then xᵤ + xᵥ < 1, contradiction.

   So at least one endpoint has x ≥ 1/2 and is included in C.

   Therefore C is a valid vertex cover.
5. Cost bound:

   Let 1\_C(v) be the indicator that v ∈ C.

   By rounding, if v ∈ C then xᵥ ≥ 1/2, so:

   1\_C(v) ≤ 2xᵥ.

   Sum over all v:

   |C| = ∑\_{v∈V} 1\_C(v)

   ≤ ∑\_{v∈V} 2xᵥ

   = 2 ∑\_{v∈V} xᵥ

   = 2·LP\*.
6. Relate to OPT:

   |C| ≤ 2·LP\*

   ≤ 2·OPT.

   Thus the algorithm is a 2-approximation.

**Insight:** LP gives a numerical lower bound (LP\*) on OPT. Rounding converts fractional membership into an integral set while inflating cost by at most a factor of 2, exactly because every chosen vertex had at least half a unit of LP mass.

### Christofides’ 3/2-Approximation Bound (Key Inequalities)

Assume a complete graph with metric distances d(·,·) satisfying triangle inequality. Let T be an MST, O the odd-degree vertices in T, and M a minimum-weight perfect matching on O. Show the resulting tour length is ≤ 3OPT/2.

1. Lower bound via MST:

   Let OPT be the length of an optimal TSP tour.

   Remove any one edge from the optimal tour; the remaining edges form a spanning tree.

   Since MST has minimum weight among all spanning trees:

   w(T) = w(MST) ≤ OPT.
2. Odd-degree set and matching idea:

   In the MST T, the set O of odd-degree vertices has even cardinality (handshaking lemma: ∑ degrees is even, so number of odd degrees is even).

   So a perfect matching on O exists.
3. Bound w(M) ≤ OPT/2:

   Consider the optimal tour restricted to the vertices in O in the order they appear on the tour.

   Pair consecutive vertices along that order to form a perfect matching M′.

   The tour edges between each pair define a path; by triangle inequality, the direct edge between the pair is no longer than that path.

   Summing over the disjoint paired segments covers at most the entire tour length.

   Hence w(M′) ≤ OPT/2.

   Since M is minimum:

   w(M) ≤ w(M′) ≤ OPT/2.
4. Combine:

   w(T ∪ M) = w(T) + w(M)

   ≤ OPT + OPT/2

   = 3OPT/2.
5. Euler tour and shortcutting:

   All vertices in T ∪ M have even degree (odd + 1 from matching becomes even), so an Eulerian tour exists.

   Convert the Eulerian tour into a Hamiltonian cycle by shortcutting repeated vertices.

   By triangle inequality, shortcutting does not increase total length.

   Therefore final tour length ≤ w(T ∪ M) ≤ 3OPT/2.

**Insight:** Christofides is a ‘two-lower-bounds’ story: MST ≤ OPT and matching-on-odds ≤ OPT/2. Triangle inequality is the glue that makes shortcutting safe, preventing the repair step from increasing cost.

## Key Takeaways

- ✓

  Approximation algorithms give polynomial-time **feasible** solutions with **worst-case multiplicative** guarantees relative to OPT.
- ✓

  For minimization: cost(A) ≤ ρ·OPT; for maximization: value(A) ≥ OPT/ρ. Keep directions explicit.
- ✓

  A strong analysis often hinges on a computable **lower bound** on OPT (matching size, MST weight, LP relaxation value, dual objective).
- ✓

  Charging and exchange arguments are the basic proof tools for constant-factor bounds.
- ✓

  LP relaxation + rounding turns NP-hard integer structure into solvable fractional structure, then carefully “repairs” it with bounded loss.
- ✓

  Primal–dual methods build a dual certificate alongside the solution; weak duality provides the OPT comparison.
- ✓

  Problem structure (e.g., triangle inequality in metric TSP) can dramatically improve approximability.

## Common Mistakes

- ✗

  Mixing up minimization and maximization inequalities (writing cost(A) ≥ OPT/ρ for a minimization problem, etc.).
- ✗

  Forgetting feasibility: an approximation ratio is meaningless if the algorithm can output an infeasible solution.
- ✗

  Using an LP relaxation bound in the wrong direction (e.g., claiming LP\* ≥ OPT for a minimization relaxation).
- ✗

  Assuming a heuristic’s empirical performance implies an approximation guarantee without a worst-case proof.

## Practice

easy

Minimization vs. maximization: Suppose A is claimed to be a ρ-approximation for a maximization problem. Write the correct inequality relating value(A) and OPT, and rewrite it as a bound on OPT/value(A).

**Hint:** Maximization guarantees the algorithm’s value is not too small compared to OPT.

Show solution

For maximization, a ρ-approximation satisfies:

value(A) ≥ OPT/ρ.

Equivalently, divide both sides by value(A)·ρ (positive):

OPT/value(A) ≤ ρ.

medium

Vertex Cover lower bound: Let M be any matching in G. Prove that OPT ≥ |M| for minimum vertex cover.

**Hint:** A vertex cover must cover each edge in M, and matching edges don’t share endpoints.

Show solution

Let M = {e₁, …, e\_k} be a matching. Any vertex cover C must include at least one endpoint of each edge eᵢ. Since edges in a matching are disjoint, the endpoints needed to cover different eᵢ cannot be reused across edges via a shared endpoint. Therefore C must contain at least k vertices, so |C| ≥ k. Since OPT is the minimum possible |C|, OPT ≥ |M|.

hard

LP rounding bound: In the LP-rounding 2-approx for Vertex Cover with threshold 1/2, justify carefully why 1\_C(v) ≤ 2xᵥ holds for every vertex v, then sum to conclude |C| ≤ 2·LP\*.

**Hint:** Consider separately the cases v ∈ C and v ∉ C; use that 0 ≤ xᵥ ≤ 1 in the LP.

Show solution

Let 1\_C(v) be 1 if v ∈ C, else 0. There are two cases:

1) If v ∈ C, then xᵥ ≥ 1/2 by definition of C. So 1\_C(v) = 1 ≤ 2xᵥ.

2) If v ∉ C, then 1\_C(v) = 0 ≤ 2xᵥ because xᵥ ≥ 0 in the LP.

Thus for all v, 1\_C(v) ≤ 2xᵥ.

Summing over v:

|C| = ∑\_{v∈V} 1\_C(v) ≤ ∑\_{v∈V} 2xᵥ = 2∑\_{v∈V} xᵥ = 2·LP\*.

## Connections

- •[NP-Completeness](/tech-tree/np-completeness/)
- •[Reductions](/tech-tree/reductions/)
- •[Greedy Algorithms](/tech-tree/greedy-algorithms/)
- •[Linear Programming Relaxations](/tech-tree/linear-programming-relaxations/)
- •[Duality and Primal–Dual Methods](/tech-tree/primal-dual-methods/)
- •[Hardness of Approximation (PCP / Gap Reductions)](/tech-tree/hardness-of-approximation/)

Quality: A (4.3/5)

[← back to tree](/tech-tree/)[browse all →](/tech-tree/inventory/)
