---
title: Computational Complexity Theory
description: Space complexity, circuit complexity, derandomization.
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
permalink: /tech-tree/computational-complexity/
---

[←Back to Tech Tree](/tech-tree/)

[inventory](/tech-tree/inventory/)[coverage](/tech-tree/coverage/)

# Computational Complexity Theory

AlgorithmsDifficulty: ★★★★★Depth: 5Unlocks: 0

Space complexity, circuit complexity, derandomization.

## Interactive Visualization

⏮◀◀▶▶STEP0.25x1xZOOM

t=0s

## Core Concepts

- -Space as a fundamental resource (workspace of a Turing machine; SPACE(f(n)) as the space-bound measure)
- -Non-uniform Boolean circuit families as a computation model with size and depth as irreducible complexity measures
- -Pseudorandomness (pseudorandom generators) as the mechanism by which randomness can be replaced to achieve derandomization

## Key Symbols & Notation

PRG: {0,1}^s -> {0,1}^m (pseudorandom generator, seed-to-output mapping)

## Essential Relationships

- -Existence of a PRG that fools a target class implies deterministic simulation of randomized algorithms for that class (derandomization)

## Prerequisites (2)

[Complexity Classes6 atoms](/tech-tree/complexity-classes/)[NP-Completeness6 atoms](/tech-tree/np-completeness/)

Advanced Learning Details

### Graph Position

64

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

75

Total Elements

L4

Percentile Level

L3

Atomic Level

### All Concepts (30)

- - Space complexity: measuring memory (work-tape cells) used by a Turing machine as a function of input size
- - Deterministic space class SPACE(s(n)) and the class PSPACE (polynomial space)
- - Nondeterministic space class NSPACE(s(n)) and log-space classes L and NL
- - Space-constructible functions (functions s(n) for which a TM can construct s(n) workspace)
- - Configuration graph of a space-bounded Turing machine (nodes = configurations, edges = one-step moves)
- - PSPACE-completeness and canonical PSPACE-complete problems (e.g., TQBF)
- - Savitch's theorem (relating nondeterministic and deterministic space)
- - Immerman–Szelepcsényi theorem (NL is closed under complement: NL = coNL)
- - Space vs time tradeoffs and qualitative differences in closure/robustness
- - Boolean circuits as a computation model (gates, inputs, directed acyclic graph structure)
- - Circuit size (number of gates) as a complexity measure
- - Circuit depth (longest gate-to-output path) as a complexity measure
- - Circuit families {C\_n} (one circuit per input length) and the notion of families as languages' characterization
- - Non-uniformity vs uniformity of circuit families (i.e., requirement for an algorithm to produce C\_n)
- - Uniformity conditions (e.g., DLOGTIME-uniformity, P-uniformity) and their meaning
- - The non-uniform class P/poly (languages with polynomial-size circuit families / polynomial advice)
- - NC (Nick's Class): classes defined by poly-size, polylog-depth uniform circuits, capturing parallelizability
- - AC classes (e.g., AC^0) characterized by unbounded fan-in gates and depth-based hierarchies
- - Circuit lower bounds: proving explicit functions require large/superpolynomial circuit size or depth
- - Advice strings and non-uniform advice (how advice length models non-uniformity, notation L/poly)
- - Randomized complexity classes important to derandomization (BPP, RP, ZPP)
- - Adleman's theorem (non-uniform containment of randomized classes: BPP ⊆ P/poly)
- - Pseudorandom generator (PRG): deterministic function that expands a short random seed to a longer string indistinguishable by a class of algorithms
- - PRG parameters: seed length (r), output stretch, and distinguishing advantage/error
- - Hardness vs randomness paradigm (construct PRGs from functions with high circuit complexity)
- - Nisan–Wigderson and Impagliazzo–Wigderson PRG constructions (idea: use hard functions to build PRGs)
- - Derandomization: goal and techniques to simulate randomized algorithms deterministically using PRGs or extractors
- - Randomness extractors and their role in converting weak randomness into nearly uniform randomness
- - Polynomial identity testing (PIT) as a central example of a randomized problem whose derandomization links to circuit lower bounds
- - Error reduction/amplification for randomized algorithms (repetition, majority, and their cost in time/space)

### Teaching Strategy

Quick unlock - significant prerequisite investment but simple final step. Verify prerequisites first.

Why do some problems resist every clever optimization we try? Complexity theory answers this by changing the question from “what’s the fastest algorithm?” to “what are the fundamental limits of computation under a resource budget?” In this node you’ll treat space as a first-class resource, study non-uniform circuits as an alternative computation model, and see how pseudorandomness enables derandomization—replacing random bits with structure without losing power.

TL;DR:

Computational complexity theory studies what can be computed under resource bounds. This lesson focuses on (1) space complexity and landmark results like Savitch’s theorem and Immerman–Szelepcsényi, (2) circuit complexity via families {Cₙ} with size/depth as intrinsic measures (P/poly, AC⁰, NC¹), and (3) derandomization via pseudorandom generators PRG: {0,1}ˢ → {0,1}ᵐ that “fool” a class so randomness can be eliminated or reduced.

## What Is Computational Complexity Theory?

Computational complexity theory is the study of computation under constraints. Instead of asking “is problem X solvable?”, we ask:

- •**How much time?** (number of steps)
- •**How much space?** (working memory)
- •**How much circuit size/depth?** (non-uniform hardware-like resources)
- •**How much randomness?** (random bits as a resource)

The central idea is that *resources are currencies*. Different models of computation charge you in different currencies, but the goal is to understand which costs are unavoidable.

### Why we need multiple resource measures

If you only measure time, you can miss important structure:

- •Some problems appear to require huge time but only small memory.
- •Some problems have very shallow parallel algorithms (low depth) even if sequential time is large.
- •Some randomized algorithms are dramatically simpler than known deterministic ones—raising the question: is randomness truly a source of power, or just a shortcut we can simulate?

Complexity theory builds a “map” of classes—sets of languages (decision problems) solvable within given resource bounds—and studies containments, separations, and equivalences.

### The three pillars in this node

This node emphasizes three atomic concepts:

1. 1)**Space as a fundamental resource**

Space counts the number of work tape cells a Turing machine uses, as a function of input length n. We write classes like SPACE(f(n)) (and special cases like L, NL, PSPACE).

2. 2)**Circuit complexity as a computation model**

Instead of a single algorithm, we consider a *family* of Boolean circuits {Cₙ}, one circuit per input length n. Complexity is measured via circuit **size** (number of gates) and **depth** (longest path). This leads to classes like P/poly, AC⁰, NC¹.

3. 3)**Pseudorandomness and derandomization**

Randomness can be treated as a resource (BPP, RP, ZPP). A **pseudorandom generator** (PRG) is a function

PRG: {0,1}ˢ → {0,1}ᵐ

that stretches a short *seed* into a longer string that looks random to some computationally bounded observer. If a PRG fools the class that a randomized algorithm uses, we can replace randomness with a loop over seeds, turning randomized computation into deterministic computation.

### A unifying viewpoint

All three pillars ask variations of the same question:

> If I restrict computation (memory, circuit resources, randomness), what power remains—and what tradeoffs exist between resources?

Space can sometimes simulate time (and vice versa) but with nontrivial overhead. Circuits capture non-uniform “advice-like” computation. PRGs connect hardness (things that are difficult for circuits) to randomness elimination.

This lesson will move slowly through these ideas, with the goal of building intuition and a working technical toolkit.

## Core Mechanic 1: Space Complexity (SPACE(f(n)), L/NL, and the Shape of PSPACE)

### Why space deserves its own spotlight

Space is not just “time but smaller.” Memory is a bottleneck in real systems, but more importantly, **space has unique mathematical properties**:

- •Space-bounded machines can be *reused*: you can revisit memory cells.
- •Configurations of a space-bounded machine form a graph of limited size.
- •That graph perspective enables simulation theorems that don’t exist (as cleanly) for time.

### Definitions: SPACE(f(n)) and friends

A deterministic Turing machine M decides a language L in **space f(n)** if on every input x of length n it uses at most O(f(n)) work tape cells. The input tape is read-only and does not count (standard convention).

- •**SPACE(f(n))**: languages decidable in O(f(n)) deterministic space.
- •**NSPACE(f(n))**: languages decidable in O(f(n)) nondeterministic space.

Special named classes:

- •**L** = SPACE(log n)
- •**NL** = NSPACE(log n)
- •**PSPACE** = ⋃ₖ SPACE(nᵏ)

A key detail: for f(n) < log n, you can’t even index the input properly, so most interesting classes start at log n.

### The configuration graph viewpoint

Fix an input x of length n. Suppose M runs in space s(n). A **configuration** encodes:

- •the machine state
- •head positions (input head position needs O(log n) bits)
- •work tape contents (O(s(n)) bits)

So the number of configurations is at most:

|Conf(M, x)| ≤ 2^{O(s(n))} · poly(n)

Often we simplify to:

|Conf(M, x)| ≤ 2^{O(s(n))}

because poly(n) is dominated by 2^{O(s(n))} once s(n) ≥ log n.

Now build a directed graph Gₓ where nodes are configurations, and edges represent one valid transition of M. Then:

- •x ∈ L(M) iff there is a path from the start configuration to an accept configuration.

This reframes space-bounded computation as **graph reachability** in an exponentially large (but implicitly defined) graph.

### Savitch’s Theorem: nondeterministic space is “almost” deterministic space

Savitch’s theorem is one of the crown jewels of space complexity:

> For s(n) ≥ log n,

> NSPACE(s(n)) ⊆ SPACE(s(n)²).

Meaning: nondeterminism does not buy you exponential power in space; it costs only a quadratic blowup.

#### Why this is true (high-level idea)

In the configuration graph, nondeterministic acceptance is reachability. Reachability can be solved by a recursive “meet-in-the-middle” strategy that uses space to store only:

- •two configurations **u**, **v**
- •a recursion depth counter

#### The recursive reachability predicate

Define a predicate:

REACH(u, v, t) = “is there a path from u to v of length ≤ t?”

We want REACH(start, accept, T) where T is the number of configurations (so any path can be assumed to have length ≤ T).

Use the recurrence:

REACH(u, v, t) is true iff ∃ midpoint m such that

REACH(u, m, ⌊t/2⌋) ∧ REACH(m, v, ⌊t/2⌋)

This is a nondeterministic-looking statement, but we can implement it deterministically by looping over all possible midpoints m (all configurations). The recursion depth is O(log t) = O(s(n)). Each level stores O(s(n)) bits for u, v, t. Total space:

O(s(n)) (per level) × O(log t) (levels)

Since t ≤ 2^{O(s(n))}, we have log t = O(s(n)). Thus space is O(s(n)²).

So:

NSPACE(s) ⊆ SPACE(s²).

This is profoundly different from time complexity, where we do not know anything like NTIME(t) ⊆ TIME(t²) in general.

### Immerman–Szelepcsényi: NL is closed under complement

Another striking result:

> NL = coNL.

So if a logspace nondeterministic machine can decide a language, it can decide its complement too.

#### Why this matters

In NP, we do not know whether NP = coNP. The fact that NL *does* equal coNL is a reminder that space behaves differently than time.

#### Intuition (very informal)

NL-completeness of **s-t reachability** (is there a path from s to t in a directed graph) suggests that complement asks “no path exists,” which sounds global.

Immerman–Szelepcsényi shows that in logspace nondeterminism, you can count (modestly) the number of reachable nodes layer by layer, and verify that t is not among them, using only O(log n) space for counters.

The key trick is that nondeterminism can be used to *certify counts* by guessing a set and verifying it consistently, without storing the whole set.

### Where PSPACE sits

PSPACE includes many “game-like” and “quantified” problems (QBF is PSPACE-complete). You can view PSPACE as problems solvable with polynomial memory—even if time might be exponential.

A useful containment chain (all believed strict):

P ⊆ NP ⊆ PSPACE ⊆ EXPTIME

Two meta-intuitions:

- •Polynomial space is powerful because you can do depth-first search of exponential trees using only polynomial stack space.
- •Space-bounded computations correspond to reachability in huge graphs, which can be navigated systematically without storing the whole graph.

### Quick comparison table

| Resource | Typical class | Canonical complete problem | Intuition |
| --- | --- | --- | --- |
| log space | L / NL | s-t reachability (NL) | tiny memory, streaming-like |
| poly space | PSPACE | QBF | explore exponential possibilities with reuse |
| poly time | P | (varies) | efficient sequential computation |

Space complexity provides tools (configuration graphs, reachability, recursion) that will reappear when we talk about circuits and derandomization.

## Core Mechanic 2: Circuit Complexity (Non-Uniform Families, Size, Depth, and P/poly)

### Why circuits?

A Turing machine is *uniform*: one finite description handles all input lengths. Circuits are *non-uniform*: you can have a different circuit for each n.

Why is this useful?

- •Circuits model **hardware**: fixed wiring for a fixed input size.
- •Circuits expose **parallelism**: depth measures time with unbounded parallel gates.
- •Circuits let us talk about **lower bounds**: proving a function needs many gates is a concrete kind of impossibility.
- •Circuits connect directly to **derandomization**: PRGs are often defined by “fooling” circuit classes.

### Circuit families and non-uniformity

A Boolean circuit Cₙ takes n input bits and outputs 0/1. A **circuit family** {Cₙ} decides a language L if for all x ∈ {0,1}ⁿ:

Cₙ(x) = 1 ⇔ x ∈ L.

Non-uniformity means there may be no efficient algorithm that, given n, outputs Cₙ. The family can be arbitrary as long as each Cₙ is finite.

To control this, we often study:

- •**P/poly**: languages decided by polynomial-size circuit families.

Equivalently (important viewpoint): P/poly = poly-time computation with **polynomial advice**. Advice is a string aₙ of length poly(n) that depends only on n, not on the particular input x.

### Size and depth as irreducible measures

Two primary complexity measures for circuits:

- •**Size(C)**: number of gates (sometimes wires).
- •**Depth(C)**: length of the longest path from input to output.

Depth corresponds to parallel time: if all gates at a level compute simultaneously, depth is time steps.

This yields classes like:

- •**NC**: poly-size, polylog-depth circuits (efficient parallelizable problems).
- •**NC¹**: poly-size, O(log n)-depth circuits.
- •**AC⁰**: constant-depth, poly-size circuits with unbounded fan-in AND/OR/NOT.

A central theme: **depth is powerful**. Allowing depth to grow from O(1) to O(log n) dramatically increases what you can compute.

### Uniform vs non-uniform: what you gain and what you lose

| Model | Strength | Weakness |
| --- | --- | --- |
| Turing machine (uniform) | single algorithm, realistic | harder to prove lower bounds |
| Circuits (non-uniform) | captures per-n optimization; lower bounds are concrete | may encode “magic” per input length |

Non-uniformity can be surprisingly strong. For instance, it’s known that if NP ⊆ P/poly then the polynomial hierarchy collapses (a major unlikely event). So proving NP ⊄ P/poly is a prominent goal.

### AC⁰ as a case study: constant depth limitations

AC⁰ circuits are extremely shallow. They can compute many basic operations, but they cannot compute some simple global properties efficiently.

Classic results (you don’t need proofs here, but you should know the statements):

- •PARITY ∉ AC⁰ (requires superpolynomial size at constant depth)
- •MAJORITY ∉ AC⁰ (similarly)

These theorems are examples of **circuit lower bounds**, among the few strong lower bounds we can prove unconditionally.

### Depth vs size tradeoff intuition

Consider computing XOR of n bits.

- •With depth O(log n), you can build a binary tree of XOR gates: size O(n), depth O(log n).
- •With constant depth AND/OR/NOT only (AC⁰), you cannot do it with polynomial size.

This highlights that depth restrictions create qualitative changes.

### Circuits and space: a subtle relationship

Circuits and space are not identical currencies, but there are translations:

- •A logspace uniformity condition on circuits corresponds to certain space bounds.
- •Many space-bounded computations can be simulated by polynomial-size circuits (non-uniformly) because each input length’s configuration graph is finite.

One useful heuristic:

- •**Space bounds often imply circuit bounds (non-uniformly)**.
- •**Circuit lower bounds can imply derandomization** (via hardness vs randomness).

This is why circuits sit in the middle of this node: they connect space and pseudorandomness.

## Core Mechanic 3: Pseudorandomness and Derandomization (PRGs as Randomness Substitutes)

### Why derandomize?

Randomness is a resource. Many algorithms use random bits to simplify design or speed up computation (e.g., randomized primality testing historically, hashing, sampling).

Complexity theory asks:

- •Is randomness *fundamental* (BPP strictly larger than P)?
- •Or can we simulate randomness deterministically with small overhead?

Derandomization is the program of removing or reducing randomness.

### Randomized classes in one picture

- •**BPP**: bounded-error probabilistic polynomial time.
- •**RP**: one-sided error (false negatives allowed).
- •**ZPP**: zero-error expected poly time.

A core belief in complexity theory is:

BPP = P

But this is unproven.

### Pseudorandom generators (PRGs)

A pseudorandom generator is a deterministic function

PRG: {0,1}ˢ → {0,1}ᵐ

where s ≪ m (seed shorter than output). If you pick a uniform seed z ∈ {0,1}ˢ, the output PRG(z) should “look uniform” to a restricted observer.

The observer is typically a circuit or algorithm from some class 𝒞. Then PRG is said to **fool** 𝒞 if no member of 𝒞 can distinguish PRG(z) from a truly uniform m-bit string.

Formally, for a class 𝒞 of distinguishers D: {0,1}ᵐ → {0,1}, PRG ε-fools 𝒞 if for all D ∈ 𝒞:

| Pr[D(Uₘ)=1] − Pr[D(PRG(Uₛ))=1] | ≤ ε

where Uₖ denotes the uniform distribution over {0,1}ᵏ.

### How PRGs imply derandomization (the key mechanism)

Suppose you have a randomized algorithm A(x; r) that runs in poly(n) time and uses m(n) random bits r.

Assume we have a PRG with seed length s(n) that fools the class of computations that A performs on its random tape.

Then we can define a deterministic algorithm:

1. 1)For every seed z ∈ {0,1}ˢ
2. 2)Compute r = PRG(z)
3. 3)Run A(x; r)
4. 4)Take the majority vote (or OR/AND depending on error type)

Runtime blowup: 2ˢ times poly(n).

So if s(n) = O(log n), then 2ˢ = poly(n), and we get a polynomial-time deterministic simulation. In other words:

If we can build PRGs with logarithmic seed that fool BPP computations, then BPP ⊆ P.

This is the core “replace randomness with structure” story.

### Where do PRGs come from? Hardness vs randomness

PRGs are not magic; they are usually built from **hard functions**.

The celebrated intuition (made rigorous in many frameworks):

> If there exists a function that is hard for small circuits, then we can construct PRGs that fool small circuits.

This is called a **hardness vs randomness** connection.

At a high level:

- •A hard function cannot be predicted/compressed by small circuits.
- •Its truth table contains “complex” patterns.
- •Those patterns can be used to generate outputs that small circuits cannot distinguish from uniform.

This is why circuit lower bounds are so valuable: even modest lower bounds can imply derandomization results.

### Space-bounded derandomization (Nisan’s generator intuition)

There are PRGs tailored to **space-bounded** computation (e.g., Nisan’s generator). The key phenomenon:

- •A space-s machine has only 2^{O(s)} configurations.
- •Its computation on random bits can be seen as a walk through configurations.
- •If we generate a pseudorandom stream that “hits” transitions similarly to truly random bits, the machine can’t tell.

One common parameter form you should remember:

- •For space s and m random bits, one can often get seed length roughly O(s · log m) (up to polylog factors), sufficient to derandomize algorithms that use much randomness but small space.

This is conceptually powerful: **small-space algorithms can often be derandomized more directly** than general polynomial-time algorithms.

### Derandomization as resource tradeoff

Derandomization usually trades randomness for one (or more) of:

- •extra time (enumerate seeds)
- •extra space (store more structure)
- •stronger assumptions (hardness assumptions)

The main lesson: randomness is a resource that can sometimes be “compressed” into a short seed—if your computational model is too weak to notice the difference.

## Application/Connection: Putting Space, Circuits, and PRGs Together

### The triangle of ideas

This node’s three topics reinforce each other:

1. 1)**Space complexity** gives a clean graph-based view (configuration reachability).
2. 2)**Circuit complexity** gives a non-uniform lens and concrete lower-bound targets.
3. 3)**PRGs** connect hardness (circuit lower bounds) to derandomization (removing randomness).

A useful mental model is a triangle:

- •Space → (configuration graphs) → reachability problems
- •Circuits → (non-uniform computation) → hardness targets
- •Hardness → (PRGs) → derandomization, often for space-bounded computation

### Example: s-t reachability, NL, and derandomization

The NL-complete problem s-t reachability (directed graph reachability) sits at the intersection of these ideas.

- •It is a space-bounded problem: can be solved in nondeterministic logspace.
- •It can be expressed with small circuits if you allow non-uniformity and enough depth.
- •Randomized algorithms (random walks) can solve some reachability variants; PRGs for space-bounded computation can often derandomize them.

Even if you don’t go deep into specific constructions, the pattern matters:

> Space-bounded computation has a small state space ⇒ it is more susceptible to pseudorandom simulation.

### Example: P/poly and “advice” as a boundary of feasibility

P/poly is important as a “ceiling” for many uniform classes:

- •P ⊆ P/poly (trivially)
- •BPP ⊆ P/poly (randomness can be hardwired as advice per length)

That second containment is worth pausing on. Here is the intuition:

A BPP machine succeeds with probability ≥ 2/3 over random strings r. For each input length n, by averaging, there exists a *fixed* randomness string (or a small set) that works well on many inputs. With polynomial advice, you can store such helpful random strings for each n, yielding non-uniform simulation.

So even without full derandomization (BPP = P), randomness often collapses under non-uniformity.

### Example: Circuit lower bounds as “engines” of PRGs

Many landmark conditional results have the form:

If ∃ explicit f with circuit complexity ≥ 2^{Ω(n)} (or strong enough lower bound)

⇒ strong PRGs exist

⇒ BPP = P (or other derandomization conclusions)

Why this matters pedagogically:

- •Proving lower bounds is hard.
- •Derandomization is hard.
- •Complexity theory links them so progress in one implies progress in the other.

### What you should be able to do after this node

You’re aiming for these capabilities:

- •Comfortably define and reason about SPACE(f(n)) and NSPACE(f(n)) using configuration graphs.
- •Explain Savitch’s theorem at the level of the recursive midpoint reachability method and compute the space bound.
- •Define circuit families, size, depth, and interpret P/poly as “polynomial advice.”
- •State what it means for PRG: {0,1}ˢ → {0,1}ᵐ to fool a class, and show the seed-enumeration derandomization step.

These are foundational tools for advanced nodes on interactive proofs, hardness vs randomness in detail, and fine-grained complexity.

## Worked Examples (3)

### Savitch-style reachability and the s(n)² space bound

Let M be a nondeterministic Turing machine using space s(n) on inputs of length n (with s(n) ≥ log n). Fix an input x. Consider the configuration graph Gₓ of M on x. Show how a deterministic algorithm can decide whether M accepts x using O(s(n)²) space.

1. Model nondeterminism as reachability:

   - •Let c\_start be the start configuration on x.
   - •Let c\_acc range over accept configurations.
   - •Then M accepts x ⇔ ∃ path from c\_start to some c\_acc in Gₓ.
2. Bound the number of configurations:

   A configuration stores:

   - •O(1) bits for state
   - •O(log n) bits for input head position
   - •O(s(n)) bits for work tape contents and work head positions

   So total bits = O(s(n)).

   Thus the number of configurations N satisfies:

   N ≤ 2^{O(s(n))}.
3. Reduce to bounded-length reachability:

   Any accepting path can be taken to have length ≤ N (if a path repeats a configuration, remove the cycle).

   So it suffices to decide REACH(c\_start, c\_acc, N).
4. Define the recursive predicate REACH(u, v, t):

   REACH(u, v, t) = “there exists a path from u to v of length ≤ t”.

   Base cases:

   - •If t = 0: return (u = v).
   - •If t = 1: return (u → v is an edge) or (u = v).
5. Recursive step via midpoint:

   For t > 1, compute:

   REACH(u, v, t) = OR over all midpoints m of

   REACH(u, m, ⌊t/2⌋) AND REACH(m, v, ⌊t/2⌋).

   Implement this deterministically by looping m over all configurations.
6. Space accounting (why it’s s²):

   At any recursion level, store:

   - •u (O(s))
   - •v (O(s))
   - •t (O(log t))

   So per level: O(s + log t).

   Depth of recursion: O(log t).

   Since t ≤ N ≤ 2^{O(s)}, we have:

   log t ≤ O(s).

   Therefore:

   Per level space = O(s)

   Number of levels = O(s)

   Total space = O(s · s) = O(s²).

**Insight:** Savitch’s theorem is really a statement about reachability in an implicitly defined graph with 2^{O(s)} nodes: you can solve reachability with only O(log N) recursion depth and O(log N) bits per stored node, leading to O((log N)²) = O(s²) space.

### From a PRG to a deterministic simulation by seed enumeration

You have a randomized algorithm A(x; r) that runs in time poly(n) and uses m(n) random bits r ∈ {0,1}ᵐ. Assume there is a PRG G: {0,1}ˢ → {0,1}ᵐ that ε-fools the class of distinguishers induced by A’s acceptance predicate, with ε ≤ 1/10. Show how to build a deterministic algorithm and bound its runtime when s(n) = O(log n).

1. Interpret A as a boolean function of randomness:

   For fixed input x, define fₓ(r) = 1 if A(x; r) accepts, else 0.

   Then A’s acceptance probability is Pr[fₓ(Uₘ)=1].
2. Use the PRG guarantee:

   Since G ε-fools the relevant class,

   | Pr[fₓ(Uₘ)=1] − Pr[fₓ(G(Uₛ))=1] | ≤ ε.

   So the acceptance probability under pseudorandom bits is close to acceptance under truly random bits.
3. Define a deterministic simulator D:

   On input x:

   1) For every seed z ∈ {0,1}ˢ:

   - •compute r = G(z)
   - •run A(x; r)
   - •record the output bit

   2) Output the majority value over all seeds.
4. Why majority works:

   Assume A is BPP with error ≤ 1/3, so either:

   - •x ∈ L: Pr[fₓ(Uₘ)=1] ≥ 2/3
   - •x ∉ L: Pr[fₓ(Uₘ)=1] ≤ 1/3

   Under G(Uₛ), probabilities shift by at most ε ≤ 1/10:

   - •x ∈ L: Pr[fₓ(G(Uₛ))=1] ≥ 2/3 − 1/10 = 17/30 > 1/2
   - •x ∉ L: Pr[fₓ(G(Uₛ))=1] ≤ 1/3 + 1/10 = 13/30 < 1/2

   So the majority over seeds matches the correct answer.
5. Runtime bound:

   There are 2ˢ seeds.

   Each seed evaluation runs A plus G in poly(n) time.

   So total time = 2ˢ · poly(n).

   If s(n) = O(log n), then 2ˢ = poly(n), hence total time remains poly(n).

**Insight:** Derandomization often reduces to one move: replace a random choice over {0,1}ᵐ with a pseudorandom choice generated from {0,1}ˢ, then enumerate all seeds. The entire challenge is constructing G with small s that fools the computation you care about.

### P/poly as polynomial advice (a concrete translation)

Show the equivalence between: (1) L ∈ P/poly (polynomial-size circuit family), and (2) L is decidable by a polynomial-time Turing machine with polynomial-length advice strings aₙ depending only on n.

1. Direction (circuits ⇒ advice):

   Assume L has circuits {Cₙ} of size ≤ nᵏ.

   Define advice aₙ to be an encoding of Cₙ (gate list and wiring) of length poly(n).

   On input x of length n, the TM:

   - •reads advice aₙ
   - •evaluates the described circuit Cₙ on x in time poly(n)
   - •outputs Cₙ(x).
2. Direction (advice ⇒ circuits):

   Assume there is a poly-time TM M and advice strings aₙ with |aₙ| ≤ nᵏ such that M(x, aₙ) decides L.

   For each n, build a circuit Cₙ that hardwires aₙ as constants and simulates M’s computation on n-bit inputs.

   Since M runs in poly(n) time, the simulation yields a circuit of poly(n) size.

   Thus {Cₙ} is a polynomial-size circuit family deciding L.

**Insight:** Non-uniformity is “information per input length.” P/poly is exactly polynomial-time computation plus a polynomial-sized hint that depends only on n. This framing is crucial when comparing uniform derandomization (BPP vs P) to non-uniform collapses (BPP ⊆ P/poly).

## Key Takeaways

- ✓

  Space is a distinct computational resource with powerful structural tools (configuration graphs, reachability) that enable theorems unlike those in time complexity.
- ✓

  For s(n) ≥ log n, NSPACE(s(n)) ⊆ SPACE(s(n)²) (Savitch): nondeterministic space can be simulated deterministically with only quadratic space overhead.
- ✓

  NL = coNL (Immerman–Szelepcsényi): logspace nondeterminism is closed under complement, contrasting with the open NP vs coNP question.
- ✓

  Circuit families {Cₙ} provide a non-uniform computation model; size and depth measure intrinsic complexity (hardware cost and parallel time).
- ✓

  P/poly can be understood as polynomial-size circuits or equivalently as polynomial-time algorithms with polynomial advice aₙ.
- ✓

  A PRG G: {0,1}ˢ → {0,1}ᵐ fools a class if bounded distinguishers cannot tell G(Uₛ) from Uₘ; small seed length enables derandomization by enumerating seeds.
- ✓

  Derandomization is a resource tradeoff: you typically exchange randomness for time (seed enumeration) plus either structure (PRGs) or assumptions (hardness).
- ✓

  Hardness vs randomness links circuit lower bounds to PRGs and derandomization, explaining why progress on either side can unlock the other.

## Common Mistakes

- ✗

  Confusing time and space: a poly-time algorithm need not be poly-space and vice versa; PSPACE problems may require exponential time.
- ✗

  Forgetting that circuit families are non-uniform: assuming there must be an efficient procedure to generate Cₙ from n (uniformity is an extra condition).
- ✗

  Assuming “PRG exists” automatically implies P = BPP: the PRG must fool the right class with sufficiently small seed length (typically O(log n)) and small error.
- ✗

  Treating “BPP ⊆ P/poly” as equivalent to “BPP = P”: non-uniform containments can hold even when uniform derandomization is unknown.

## Practice

medium

Let M be a deterministic TM that uses space s(n) on inputs of length n, with s(n) ≥ log n. Argue that on any fixed input x, either M halts within at most 2^{O(s(n))} steps or it loops forever.

**Hint:** Count the number of distinct configurations possible under space s(n). What happens if a configuration repeats?

Show solution

A configuration is determined by (state, head positions, work tape contents). With space s(n), the total description length is O(s(n)), so the number of configurations is N ≤ 2^{O(s(n))}. If M runs longer than N steps without halting, by the pigeonhole principle some configuration repeats. Since M is deterministic, repeating a configuration implies the future evolution repeats as well, so M loops forever. Therefore if it halts, it must do so within at most N = 2^{O(s(n))} steps.

easy

Suppose a randomized algorithm A(x; r) for inputs of length n uses m(n) random bits and runs in time poly(n). You have a PRG G: {0,1}ˢ → {0,1}ᵐ that fools A’s acceptance predicate with error ε = 1/100. Show that enumerating all seeds yields a deterministic algorithm with runtime 2ˢ · poly(n). Under what condition on s(n) is this runtime polynomial?

**Hint:** Write the deterministic algorithm explicitly and count the number of seeds.

Show solution

Deterministic algorithm: for all seeds z ∈ {0,1}ˢ, compute r = G(z), run A(x; r), and output majority. There are 2ˢ seeds, each run costs poly(n), so runtime is 2ˢ · poly(n). This is polynomial when 2ˢ ≤ poly(n), i.e., when s(n) = O(log n).

medium

Prove that if a language L has a polynomial-size circuit family {Cₙ}, then L ∈ P/poly (advice formulation). Explicitly describe what the advice string aₙ contains and how the TM uses it.

**Hint:** Advice can be an encoding of the circuit’s gate list and wiring; evaluation is straightforward.

Show solution

Let size(Cₙ) ≤ nᵏ. Define advice aₙ to be a canonical encoding of Cₙ: for each gate, store its type (AND/OR/NOT), its input wire indices, and identify which wires correspond to the n input bits; also identify the output wire. The encoding length is O(size(Cₙ) · log size(Cₙ)) = poly(n). A polynomial-time TM on input x of length n reads aₙ, reconstructs the circuit description, evaluates gates in topological order, and outputs the value on the output wire. Thus L is decidable in polynomial time with polynomial advice, meaning L ∈ P/poly.

## Connections

Next nodes you can study:

- •[Space-Bounded Computation and Logspace Reductions](/tech-tree/space-bounded-computation/)
- •[Circuit Complexity: AC⁰, NC, and Lower Bounds](/tech-tree/circuit-complexity/)
- •[Randomness, BPP, and Derandomization](/tech-tree/derandomization/)
- •[Hardness vs Randomness](/tech-tree/hardness-vs-randomness/)
- •[Interactive Proofs and PSPACE](/tech-tree/interactive-proofs-pspace/)

Quality: B (4.1/5)

[← back to tree](/tech-tree/)[browse all →](/tech-tree/inventory/)
