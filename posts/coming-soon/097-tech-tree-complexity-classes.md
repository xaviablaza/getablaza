---
title: Complexity Classes
description: P, NP, NP-complete, NP-hard. Computational tractability.
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
permalink: /tech-tree/complexity-classes/
---

[←Back to Tech Tree](/tech-tree/)

[inventory](/tech-tree/inventory/)[coverage](/tech-tree/coverage/)

# Complexity Classes

AlgorithmsDifficulty: ★★★★☆Depth: 3Unlocks: 4

P, NP, NP-complete, NP-hard. Computational tractability.

## Interactive Visualization

⏮◀◀▶▶STEP0.25x1xZOOM

t=0s

## Core Concepts

- -Polynomial-time solvability (class P): decision problems with algorithms running in time polynomial in input size
- -Polynomial-time verifiability (class NP): decision problems where 'yes' instances have polynomial-size certificates verifiable in polynomial time
- -Hardness and completeness: NP-hard means at least as hard as every problem in NP; NP-complete means both in NP and NP-hard

## Key Symbols & Notation

<=\_p (polynomial-time many-one reduction: transform instances of A to instances of B in polynomial time preserving yes/no)

## Essential Relationships

- -P is a subset of NP
- -NP-complete iff (in NP) AND (every problem in NP reduces to it via <=\_p)

## Prerequisites (2)

[Big O Notation6 atoms](/tech-tree/big-o/)[Propositional Logic9 atoms](/tech-tree/propositional-logic/)

## Unlocks (2)

[NP-Completenesslvl 4](/tech-tree/np-completeness/)[Computational Complexity Theorylvl 5](/tech-tree/computational-complexity/)

## Referenced by (1)

Where this concept shows up in the operating-finance and personal-finance graphs.

### From Business (1)

[weighted votingBusiness

The entire framing is about tractability - these problems are #P-hard for general cooperative games but fall into P for the special structure of weighted voting games](/business/weighted-voting/)

Advanced Learning Details

### Graph Position

53

Depth Cost

4

Fan-Out (ROI)

3

Bottleneck Score

3

Chain Length

### Cognitive Load

6

Atomic Elements

45

Total Elements

L3

Percentile Level

L4

Atomic Level

### All Concepts (19)

- - Decision problem (yes/no question about inputs) and formalization as a language (set of strings)
- - Deterministic polynomial-time algorithms as the basis of class P
- - Non-deterministic polynomial-time computation (nondeterministic Turing machine notion)
- - Polynomial-time verifier plus certificate formulation of NP (verifier V(x,c) that runs in poly time and certificate c of polynomial length)
- - Class P: set of decision problems decidable by a deterministic algorithm in polynomial time
- - Class NP: set of decision problems for which a proposed solution (certificate) can be verified in polynomial time
- - NP-hardness: notion of being at least as hard as every problem in NP (via polynomial-time reductions)
- - NP-completeness: problems that are both in NP and NP-hard
- - Polynomial-time many-one reduction (Karp reduction): mapping instances of problem A to instances of problem B in polynomial time such that answers are preserved
- - Certificate (witness): a short (polynomial-length) object that enables verification of membership for NP problems
- - Verifier model (deterministic algorithm that checks certificates) as an alternate definition of NP
- - Completeness vs hardness distinction: completeness = in class + hardest in class; hardness = at least as hard as class
- - Canonical NP-complete problems (e.g., SAT, 3-SAT, CLIQUE, Hamiltonian cycle) as benchmarks for hardness
- - Cook–Levin theorem (SAT is NP-complete) as the foundational NP-completeness result
- - Decision version vs optimization version of problems and how they relate
- - Computational tractability convention: polynomial-time as tractable/feasible and superpolynomial (e.g., exponential) as intractable/unfeasible in practice
- - Worst-case complexity focus (class definitions are about worst-case running time)
- - Polynomial bound on certificate length (certificate length is polynomial in input size)
- - Transitivity of polynomial-time many-one reductions (if A ≤\_p B and B ≤\_p C then A ≤\_p C)

### Teaching Strategy

Multi-session curriculum - substantial prior knowledge and complex material. Use mastery gates and deliberate practice.

Some problems feel “easy” because we can solve them quickly for large inputs. Others feel “hard” because every known approach blows up. Complexity classes are the vocabulary for saying, precisely, which side a problem seems to live on—and for proving that two very different-looking problems are equally hard by building reductions between them.

TL;DR:

Class **P** = decision problems solvable in polynomial time. **NP** = decision problems whose “yes” answers have certificates verifiable in polynomial time (equivalently: solvable by a nondeterministic polynomial-time machine). **NP-hard** = at least as hard as every problem in NP under polynomial-time reductions. **NP-complete** = both NP-hard and in NP. Reductions (≤p\le\_p≤p​) are the main tool: if A≤pBA \le\_p BA≤p​B and BBB is easy, then AAA is easy; if AAA is hard and A≤pBA \le\_p BA≤p​B, then BBB is hard.

## What Is a Complexity Class?

### Why we need a *class* (not just a runtime)

When you analyze an algorithm, you can say it runs in O(n2)O(n^2)O(n2) time, or O(nlog⁡n)O(n\log n)O(nlogn) time, etc. That’s useful—but it’s attached to a *particular algorithm*. Complexity theory asks a different question:

> Is the *problem itself* efficiently solvable?

A **complexity class** is a set of problems grouped by the resources needed by the *best possible* algorithms (time, space, randomness, etc.). In this lesson we focus on **time** and on four names you’ll see constantly:

- •**P** (polynomial-time solvable)
- •**NP** (polynomial-time verifiable)
- •**NP-hard** (at least as hard as NP)
- •**NP-complete** (the “hardest” problems *inside* NP)

### Decision problems: the standard “unit”

Complexity classes are usually defined for **decision problems**: the answer is **YES** or **NO**.

Examples:

- •**PATH**: Given a graph GGG and two vertices s,ts,ts,t, is there a path from sss to ttt?
- •**PRIME**: Given an integer nnn, is nnn prime?
- •**SAT**: Given a propositional formula φ\varphiφ, is there an assignment that makes it true?

Why decision problems?

1. 1)They simplify definitions and reductions.
2. 2)Many optimization problems can be converted to decision versions (e.g., “Is there a tour of length ≤ K?”).

### Input size: what does “polynomial” mean?

To talk about time, we need a notion of **input length**, typically denoted ∣x∣|x|∣x∣.

- •For a graph with nnn vertices and mmm edges, an adjacency-list encoding has size Θ(n+m)\Theta(n+m)Θ(n+m) (up to log factors depending on how vertices are labeled).
- •For an integer NNN, the input size is the number of bits, ∣N∣=⌊log⁡2N⌋+1|N| = \lfloor \log\_2 N \rfloor + 1∣N∣=⌊log2​N⌋+1.

This matters: an algorithm that is polynomial in the *value* of NNN may be exponential in the *bit-length* of NNN.

### Tractability (computational feasibility)

In practice, “efficient” is nuanced. But complexity theory uses a robust proxy:

> **Polynomial time** is considered *tractable*.

Why? Because polynomials compose well, are stable under reasonable machine models, and scale far better than exponentials.

A mental comparison (not a proof): if n=106n = 10^6n=106, then n2=1012n^2 = 10^{12}n2=1012 might be heavy but imaginable; $2^n$ is completely impossible.

### Visualization: the containment map we’ll keep returning to

Below is the conceptual picture we’re building toward (interactive in the tech tree canvas):

1. 1)A big region for “all decision problems.”
2. 2)A subset **NP**.
3. 3)Inside NP, a subset **P** (we know P⊆NPP \subseteq NPP⊆NP).
4. 4)A subset **NP-complete** inside NP.
5. 5)A region **NP-hard** that contains NP-complete and can extend outside NP.

We do **not** know whether P=NPP = NPP=NP.

This diagram isn’t decoration—it encodes the definitions. In later sections, we’ll use it as a correctness checklist when doing reductions.

## Core Mechanic 1: P and NP (Solving vs Verifying)

### Class P: polynomial-time solvable

**Definition (P).** A decision problem LLL is in **P** if there exists a deterministic algorithm that decides LLL in time polynomial in the input size.

Formally: L∈PL \in PL∈P if there exists an algorithm AAA and a polynomial p(⋅)p(\cdot)p(⋅) such that for every input xxx, A(x)A(x)A(x) halts in at most p(∣x∣)p(|x|)p(∣x∣) steps and outputs YES iff x∈Lx \in Lx∈L.

**Intuition:** problems in P are the ones we can *solve* efficiently.

Examples commonly in P:

- •Graph reachability (PATH) via BFS/DFS
- •Minimum spanning tree (as an optimization problem) and its decision variant
- •Maximum flow (and decision variants)
- •Primality testing (PRIME)

### NP: polynomial-time verifiable

**Definition (NP) via certificates.** A decision problem LLL is in **NP** if there exists:

- •a polynomial-time verifier V(x,c)V(x, c)V(x,c), and
- •a polynomial bound on certificate size ∣c∣≤p(∣x∣)|c| \le p(|x|)∣c∣≤p(∣x∣),

such that:

- •If x∈Lx \in Lx∈L (YES instance), then there exists a certificate ccc making V(x,c)=YESV(x,c) = \text{YES}V(x,c)=YES.
- •If x∉Lx \notin Lx∈/L (NO instance), then for all certificates ccc, V(x,c)=NOV(x,c) = \text{NO}V(x,c)=NO.

In logic form:

x∈L  ⟺  ∃c    V(x,c)=YESx \in L \iff \exists c \;\; V(x,c)=\text{YES}x∈L⟺∃cV(x,c)=YES

with VVV running in polytime and ∣c∣|c|∣c∣ polynomially bounded.

**Intuition:** NP problems are those where a proposed solution can be checked quickly.

Examples:

- •**SAT**: certificate = a truth assignment; verifier evaluates the formula.
- •**Hamiltonian Cycle (HC)**: certificate = a cycle listing vertices; verifier checks it is a cycle and uses edges in the graph.
- •**Clique**: certificate = set of kkk vertices; verifier checks all pairs are edges.

### Why “verifiable” is the right lens

It’s tempting to say NP means “hard.” That’s not the definition.

NP contains problems that might be easy or hard; it’s about the existence of short proofs of “YES.”

- •If a problem is in P, it’s automatically in NP:
- •To verify, just ignore the certificate and solve the problem yourself in polynomial time.

So we know:

P⊆NP.P \subseteq NP.P⊆NP.

Whether the containment is strict is the famous open question.

### Equivalent viewpoint: nondeterminism

Another equivalent definition: NP is the class of problems solvable by a **nondeterministic** Turing machine in polynomial time.

Interpretation:

- •The machine “guesses” a certificate ccc (nondeterministically).
- •It then verifies deterministically in polynomial time.

This equivalence is conceptually helpful, but in reductions we usually work with the *certificate* viewpoint.

### A key mental move: decision vs search

Many NP problems are naturally **search** problems (“find an assignment,” “find a tour”). Complexity classes are defined for decision versions.

For SAT:

- •Decision: “Does a satisfying assignment exist?”
- •Search: “Find a satisfying assignment.”

In many settings (including SAT under standard assumptions), decision and search are polynomial-time interreducible, but that’s an extra theorem. For this node, focus on decision formulations.

### Visualization: clickable certificate checker

In the canvas, imagine SAT as a card with:

- •Input: formula φ\varphiφ
- •Certificate: assignment **a** (vector of bits)
- •Verifier: evaluate φ(∗∗a∗∗)\varphi(\*\*a\*\*)φ(∗∗a∗∗) in O(∣φ∣)O(|\varphi|)O(∣φ∣)

The point is to make NP feel *mechanical*: you can literally plug in a candidate and check it.

## Core Mechanic 2: Reductions and Hardness (≤ₚ as a Pipeline)

### Why reductions are the engine of NP-completeness

Suppose you’re given a new problem BBB and you suspect it’s hard. Proving “no polynomial algorithm exists” is beyond current techniques for most natural problems.

Instead, complexity theory uses a powerful relative statement:

> If BBB were easy, then a known-hard problem AAA would also be easy.

That implication is established by a **polynomial-time reduction**.

### Polynomial-time many-one reduction (Karp reduction)

We write:

A≤pBA \le\_p BA≤p​B

to mean: there exists a polynomial-time computable function fff that maps instances xxx of AAA to instances f(x)f(x)f(x) of BBB such that:

x∈A  ⟺  f(x)∈B.x \in A \iff f(x) \in B.x∈A⟺f(x)∈B.

This “iff” is the *invariant* you must protect.

#### Reduction pipeline visualization (the one you should picture)

A reduction is not magic. It’s a program with a contract:

- •**Input:** instance xxx of AAA
- •**Transform:** compute y=f(x)y = f(x)y=f(x) in polytime
- •**Output:** instance yyy of BBB
- •**Correctness invariant:** YES in AAA iff YES in BBB

In the canvas, this should be a clickable pipeline:

A  →  f    BA \;\xrightarrow{\;f\; }\; BAf​B

with a live displayed invariant: “YES(xxx) ⇔ YES(f(x)f(x)f(x)).”

### How reductions transfer algorithms (easy direction)

If A≤pBA \le\_p BA≤p​B and B∈PB \in PB∈P, then A∈PA \in PA∈P.

**Reason:** to decide AAA on input xxx:

1. 1)Compute y=f(x)y = f(x)y=f(x) in polynomial time.
2. 2)Run the polytime decider for BBB on yyy.

Polynomial + polynomial = polynomial.

This is why we say:

- •If A≤pBA \le\_p BA≤p​B, then BBB is **at least as hard as** AAA.

### NP-hard and NP-complete

Now we can define hardness precisely.

**Definition (NP-hard).** A problem HHH is **NP-hard** if for every problem A∈NPA \in NPA∈NP, we have A≤pHA \le\_p HA≤p​H.

Interpretation: HHH is at least as hard as *every* NP problem.

**Definition (NP-complete).** A problem CCC is **NP-complete** if:

1. 1)C∈NPC \in NPC∈NP, and
2. 2)CCC is NP-hard.

Interpretation: NP-complete problems are the “hardest problems in NP.”

### The containment picture (explicitly tied to definitions)

- •**P** sits inside **NP** because solving implies verifying.
- •**NP-complete** sits inside **NP** by definition.
- •**NP-hard** contains all NP-complete problems, but may include problems *outside* NP (e.g., certain optimization problems or even undecidable problems).

A concrete reminder:

- •The optimization version of TSP (“find the shortest tour”) is NP-hard, but it is not a decision problem in NP as stated.
- •The decision version (“Is there a tour of length ≤ K?”) *is* in NP and is NP-complete.

### The standard NP-completeness proof recipe

To prove a new decision problem BBB is NP-complete:

1. 1)**Membership:** show B∈NPB \in NPB∈NP by describing a polynomial-size certificate and a polynomial-time verifier.
2. 2)**Hardness:** pick a known NP-complete problem AAA and show A≤pBA \le\_p BA≤p​B.

Notice the direction: reduce **from** a known-hard problem **to** your target problem.

A common mistake is to reverse it. If you show B≤pAB \le\_p AB≤p​A, that only says BBB is *no harder than* AAA.

### What if P = NP?

If P=NPP = NPP=NP, then every NP problem (including NP-complete ones) has a polynomial-time algorithm. The reduction machinery still works, but the interpretation of “hard” changes.

If P≠NPP \ne NPP=NP, then NP-complete problems are not in P.

We don’t know which world we live in.

## Application/Connection: Computational Tractability and a Full NP-Completeness Reduction (3SAT → CLIQUE)

### Why this matters in practice

Once you can classify problems as P, NP, NP-complete, or NP-hard, you gain a practical workflow:

- •If a problem is in **P**, invest in better implementations, constants, and data structures.
- •If a problem is **NP-complete/NP-hard**, stop hoping for a generic fast exact algorithm and pivot to:
- •approximation algorithms,
- •heuristics,
- •fixed-parameter tractability (FPT),
- •special-case structure (planarity, bounded treewidth, etc.),
- •or problem relaxations.

Complexity classes become a decision-making tool.

### A complete end-to-end reduction: 3SAT ≤ₚ CLIQUE

We’ll do a full reduction with the reduction pipeline mindset.

#### Step 0: define the two problems

**3SAT**

- •Input: a 3-CNF formula φ\varphiφ with clauses C1,…,CmC\_1,\dots,C\_mC1​,…,Cm​, each clause has exactly 3 literals.
- •Question: does there exist an assignment that satisfies all clauses?

**CLIQUE**

- •Input: an undirected graph G=(V,E)G=(V,E)G=(V,E) and integer kkk.
- •Question: does GGG have a clique of size at least kkk?

A set S⊆VS \subseteq VS⊆V is a **clique** if for all distinct u,v∈Su,v \in Su,v∈S, (u,v)∈E(u,v) \in E(u,v)∈E.

#### Step 1: the high-level idea (why this reduction should exist)

A satisfying assignment for 3SAT picks, for each clause, at least one literal that is made true. That resembles selecting one “compatible” choice per clause.

A clique enforces pairwise compatibility: every chosen literal must be consistent with every other chosen literal.

So we’ll build a graph where:

- •vertices correspond to *literals inside clauses*, and
- •edges connect literals from different clauses **unless** they conflict.

Then a clique of size mmm corresponds to picking one non-conflicting literal from each clause—exactly what we need for satisfiability.

#### Step 2: define the reduction function f

Input: φ\varphiφ with clauses C1,…,CmC\_1,\dots,C\_mC1​,…,Cm​.

Construct a graph GGG as follows:

- •For each clause CiC\_iCi​ and each literal ℓ in CiC\_iCi​, create a vertex labeled (i,ℓ)(i,\ell)(i,ℓ).
- •So there are $3m$ vertices.
- •Add an edge between two vertices (i,ℓ)(i,\ell)(i,ℓ) and (j,ℓ′)(j,\ell')(j,ℓ′) if:

1. 1)i≠ji \ne ji=j (different clauses), and
2. 2)ℓ and ℓ′ are **not contradictory** (i.e., it is not the case that ℓ is xxx and ℓ′ is ¬x\neg x¬x for the same variable xxx).

Set k=mk = mk=m.

Output: (G,k)(G,k)(G,k).

This is clearly polynomial-time to build: O(m2)O(m^2)O(m2) literal-pair checks, each check constant-time with a suitable encoding.

#### Step 3: prove the correctness invariant (YES iff YES)

We must prove:

φ is satisfiable   ⟺  G has a clique of size m.\varphi \text{ is satisfiable } \iff G \text{ has a clique of size } m.φ is satisfiable ⟺G has a clique of size m.

We’ll do both directions carefully.

##### (⇒) If ϕ is satisfiable, then G has a clique of size m

Assume φ\varphiφ is satisfiable. Then there exists an assignment that makes every clause true.

For each clause CiC\_iCi​, pick one literal ℓᵢ in CiC\_iCi​ that is true under this assignment.

Now consider the set of vertices:

S={(i,ℓi):i=1,…,m}.S = \{(i,\ell\_i) : i=1,\dots,m\}.S={(i,ℓi​):i=1,…,m}.

We claim SSS is a clique of size mmm.

Take any two distinct vertices (i,ℓi)(i,\ell\_i)(i,ℓi​) and (j,ℓj)(j,\ell\_j)(j,ℓj​) with i≠ji\ne ji=j.

- •They are from different clauses, so condition (1) for an edge is satisfied.
- •Can they be contradictory? If ℓᵢ is xxx and ℓⱼ is ¬x\neg x¬x, then xxx would have to be simultaneously true and false under the assignment—impossible.

So ℓᵢ and ℓⱼ are not contradictory, therefore condition (2) holds and the edge exists.

Thus every pair in SSS is connected: SSS is a clique. And ∣S∣=m|S| = m∣S∣=m, so GGG has a clique of size k=mk=mk=m.

##### (⇐) If G has a clique of size m, then ϕ is satisfiable

Assume GGG has a clique SSS with ∣S∣=m|S|=m∣S∣=m.

Key observation: edges only connect vertices from different clauses. That means:

- •In any clique, you can include **at most one** vertex from a given clause, because two vertices from the same clause have i=ji=ji=j and thus no edge.

Since SSS has size mmm and there are mmm clauses, SSS must contain **exactly one** vertex from each clause.

So we can write:

S={(1,ℓ1),(2,ℓ2),…,(m,ℓm)}.S = \{(1,\ell\_1), (2,\ell\_2), \dots, (m,\ell\_m)\}.S={(1,ℓ1​),(2,ℓ2​),…,(m,ℓm​)}.

Because SSS is a clique, every pair is connected by an edge, so no two literals among ℓ1,…,ℓm\ell\_1,\dots,\ell\_mℓ1​,…,ℓm​ are contradictory.

Now we build an assignment:

- •For each variable xxx:
- •if any chosen literal equals xxx, set x=truex=\text{true}x=true
- •else if any chosen literal equals ¬x\neg x¬x, set x=falsex=\text{false}x=false
- •otherwise set xxx arbitrarily.

This assignment is **well-defined**: we never choose both xxx and ¬x\neg x¬x among the ℓi\ell\_iℓi​ because that would create a contradiction, and contradictory literals are not connected by an edge—so they cannot both appear in the clique.

Finally, does this assignment satisfy φ\varphiφ?

- •In each clause CiC\_iCi​, the clique selected a literal ℓi\ell\_iℓi​ from that clause.
- •Our assignment sets ℓi\ell\_iℓi​ to true (by construction).
- •Therefore each clause has at least one true literal, hence all clauses are satisfied.

So φ\varphiφ is satisfiable.

We have proven the invariant, so 3SAT ≤ₚ CLIQUE.

### Connecting back to NP-completeness and the diagram

- •CLIQUE is in NP: certificate = set of kkk vertices; verifier checks all pairs are edges.
- •Since 3SAT is NP-complete and 3SAT ≤ₚ CLIQUE, CLIQUE is NP-hard.
- •Combining NP-hardness with membership gives: CLIQUE is NP-complete.

In the containment visualization:

- •3SAT sits in NP-complete.
- •The arrow (reduction pipeline) points to CLIQUE, pulling CLIQUE into NP-hard.
- •The certificate checker puts CLIQUE into NP.
- •So CLIQUE lands inside NP-complete.

This is what “reduction machinery” looks like when you run it end-to-end.

## Worked Examples (3)

### Classify problems as P vs NP using certificates

For each decision problem, identify whether it is in P, in NP (via a certificate), or both.

1) PATH: Given a graph G and vertices s,t, is there a path from s to t?

2) CLIQUE: Given G and k, is there a clique of size ≥ k?

3) SAT: Given formula φ, is it satisfiable?

1. 1) PATH

   - •Algorithmic view: run BFS/DFS from s and check whether t is reached.
   - •Runtime: O(n+m) for adjacency lists.
   - •Conclusion: PATH ∈ P.
   - •Since P ⊆ NP, also PATH ∈ NP.

   2) CLIQUE

   - •Certificate idea: a set S of k vertices.
   - •Verifier: check |S|=k and for every pair u,v ∈ S verify (u,v) ∈ E.
   - •Pair checking takes O(k²) adjacency queries; with adjacency matrix, O(1) per query; with hashing, expected O(1).
   - •Overall polynomial in input size.
   - •Conclusion: CLIQUE ∈ NP (membership). Whether CLIQUE ∈ P is unknown; it is NP-complete (from reductions).

   3) SAT

   - •Certificate idea: a truth assignment a (a bit-vector).
   - •Verifier: evaluate φ(a) in time O(|φ|).
   - •Conclusion: SAT ∈ NP. SAT is NP-complete, so SAT is believed not in P.

**Insight:** NP membership is often straightforward: propose the natural ‘witness’ object and show you can check it quickly. The hard part is usually NP-hardness, which comes from reductions.

### Use a reduction to transfer an algorithm: if CLIQUE were in P then 3SAT would be in P

Assume hypothetically there exists a polynomial-time algorithm CliqueSolve(G,k) that decides CLIQUE. Use the reduction 3SAT ≤ₚ CLIQUE to build a polynomial-time algorithm for 3SAT.

1. Goal: build SatSolve(φ) that decides whether a 3CNF formula φ is satisfiable.

   1) Reduction step (transform)

   - •Given φ with m clauses, construct (G,k) = f(φ) using the reduction:
   - •vertices (i,ℓ) for each literal ℓ in clause i
   - •edges between non-contradictory literals from different clauses
   - •set k = m
   - •This runs in polynomial time in |φ|.

   2) Solve step

   - •Run CliqueSolve(G,k).
   - •If CliqueSolve outputs YES, output YES; else output NO.

   3) Correctness argument

   - •By the reduction invariant: φ satisfiable ⇔ f(φ) has a clique of size m.
   - •CliqueSolve decides whether f(φ) has such a clique.
   - •Therefore SatSolve decides 3SAT correctly.

   4) Runtime

   - •polytime(f) + polytime(CliqueSolve) = polytime overall.

   Conclusion: If CLIQUE ∈ P, then 3SAT ∈ P. Since 3SAT is NP-complete, this would imply P = NP.

**Insight:** Reductions are like ‘plug adapters’: they let you route instances of A through a solver for B. The direction A ≤ₚ B matters because it determines which way algorithms and hardness transfer.

### Full mini-instance walkthrough of 3SAT → CLIQUE

Reduce the 3SAT instance φ = (x ∨ y ∨ z) ∧ (¬x ∨ y ∨ ¬z) ∧ (x ∨ ¬y ∨ w) to a CLIQUE instance (G,k), and exhibit a clique if φ is satisfiable.

1. 1) Identify clauses

   C₁ = (x ∨ y ∨ z)

   C₂ = (¬x ∨ y ∨ ¬z)

   C₃ = (x ∨ ¬y ∨ w)

   So m = 3, hence k = 3.

   2) Create vertices (i,ℓ)

   Clause 1: (1,x), (1,y), (1,z)

   Clause 2: (2,¬x), (2,y), (2,¬z)

   Clause 3: (3,x), (3,¬y), (3,w)

   Total 9 vertices.

   3) Add edges between different clauses unless contradictory

   - •Between clause 1 and clause 2:
   - •(1,x) is contradictory with (2,¬x): no edge.
   - •(1,z) is contradictory with (2,¬z): no edge.
   - •All other cross-pairs get edges.
   - •Between clause 1 and clause 3:
   - •(1,y) is contradictory with (3,¬y): no edge.
   - •Otherwise edges exist.
   - •Between clause 2 and clause 3:
   - •(2,¬x) contradictory with (3,x): no edge.
   - •(2,y) contradictory with (3,¬y): no edge.
   - •(2,¬z) has no contradiction among literals in clause 3, so it connects to (3,x),(3,¬y),(3,w).

   4) Find a satisfying assignment (one example)

   Try x=true, y=true, z=false, w=false.

   - •C₁: x ∨ y ∨ z = true
   - •C₂: ¬x ∨ y ∨ ¬z = false ∨ true ∨ true = true
   - •C₃: x ∨ ¬y ∨ w = true ∨ false ∨ false = true

   So φ is satisfiable.

   5) Map that to a clique of size 3

   Pick one true literal per clause:

   - •From C₁ pick x → vertex (1,x)
   - •From C₂ pick y → vertex (2,y)
   - •From C₃ pick x → vertex (3,x)

   6) Check pairwise compatibility (edges)

   - •(1,x) with (2,y): not contradictory → edge exists.
   - •(1,x) with (3,x): not contradictory (same literal) → edge exists (different clauses).
   - •(2,y) with (3,x): not contradictory → edge exists.

   So these 3 vertices form a 3-clique, hence (G,k) is a YES instance.

**Insight:** The reduction doesn’t just claim existence—it constructs a graph whose cliques literally encode consistent choices of literals across clauses.

## Key Takeaways

- ✓

  Complexity classes classify *problems* by the best possible resource bounds, not a particular algorithm’s runtime.
- ✓

  P = decision problems solvable in polynomial time; NP = decision problems whose YES instances have polynomial-size certificates verifiable in polynomial time.
- ✓

  We know P ⊆ NP; whether P = NP is open.
- ✓

  A polynomial-time many-one reduction A ≤ₚ B is a polytime transform f such that x ∈ A ⇔ f(x) ∈ B.
- ✓

  If A ≤ₚ B and B ∈ P, then A ∈ P (algorithms transfer along reductions).
- ✓

  NP-hard means every NP problem reduces to it; NP-complete means NP-hard and also in NP.
- ✓

  To prove NP-completeness: (1) show the problem is in NP (certificate + verifier), (2) reduce from a known NP-complete problem to it.

## Common Mistakes

- ✗

  Reversing reduction direction: proving B ≤ₚ A does not show B is NP-hard if A is known hard; you usually need A ≤ₚ B.
- ✗

  Forgetting the ‘iff’ invariant in reductions: you must prove both YES ⇒ YES and NO ⇒ NO (equivalently YES ⇔ YES).
- ✗

  Confusing NP with ‘not polynomial’: NP is about verifiability, and it includes all of P.
- ✗

  Mixing optimization and decision versions without care: NP is defined over decision problems; optimization problems are often handled via decision variants or NP-hardness statements.

## Practice

easy

Show that P ⊆ NP using the certificate/verifier definition of NP.

**Hint:** Given a polytime decider for a problem L, design a verifier that ignores (or uses a trivial) certificate.

Show solution

Let L ∈ P. Then there exists a deterministic polynomial-time decider A(x) for L.

Define verifier V(x,c) as: run A(x) and output its answer; ignore c (or require c to be empty).

- •If x ∈ L, then V(x,ε)=YES.
- •If x ∉ L, then for all c, V(x,c)=NO.

V runs in polynomial time, and the certificate length is 0 (which is polynomial). Hence L ∈ NP. Therefore P ⊆ NP.

medium

Prove CLIQUE ∈ NP by explicitly describing a certificate and a polynomial-time verifier, including a runtime bound in terms of |V| and k.

**Hint:** Certificate can be a list of k vertices. The verifier checks every pair is an edge.

Show solution

Certificate: a list S = (v₁,…,v\_k) of k vertices.

Verifier V(G,k,S):

1) Check that all v\_i are valid vertices and distinct.

2) For every pair (v\_i,v\_j) with i<j, check whether (v\_i,v\_j) ∈ E.

3) Accept iff all checks pass.

Runtime: step (2) performs C(k,2)=k(k−1)/2 edge checks. With an adjacency matrix, each check is O(1), so total O(k²). Even with adjacency lists, you can preprocess or hash adjacency for expected O(1) checks; in any standard encoding the total is polynomial in the input size. Therefore CLIQUE ∈ NP.

hard

Let A ≤ₚ B and B ≤ₚ C. Prove that A ≤ₚ C (transitivity).

**Hint:** Compose the two reduction functions and argue polynomial time is preserved.

Show solution

Assume A ≤ₚ B via f and B ≤ₚ C via g.

Define h(x) = g(f(x)).

Correctness:

- •x ∈ A ⇔ f(x) ∈ B (by definition of f)
- •f(x) ∈ B ⇔ g(f(x)) ∈ C (by definition of g)

Thus x ∈ A ⇔ h(x) ∈ C.

Runtime:

- •f is polynomial-time in |x|, so |f(x)| is at most polynomial in |x| for any reasonable encoding.
- •g runs in polynomial time in |f(x)|, hence also polynomial in |x|.

Therefore h is polynomial-time computable, and A ≤ₚ C.

## Connections

- •Next: [NP-Completeness](/tech-tree/np-completeness/)
- •Deeper theory: [Computational Complexity Theory](/tech-tree/computational-complexity/)

Suggested parallel review nodes (if available in your tech tree):

- •[Reductions and Problem Transformations](/tech-tree/reductions/)
- •[Graph Problems: Clique and Independent Set](/tech-tree/graph-clique-independent-set/)
- •[SAT and CNF](/tech-tree/sat-cnf/)

Quality: A (4.4/5)

[← back to tree](/tech-tree/)[browse all →](/tech-tree/inventory/)
