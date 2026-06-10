---
title: Proof Techniques
description: Direct proof, proof by contradiction, proof by induction.
date: '2026-07-01'
scheduled: '2026-08-28'
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
inspiration_url: https://templeton.host/tech-tree/proof-techniques/
inspiration_category: tech-tree
---

> Source-copy draft imported from [https://templeton.host/tech-tree/proof-techniques/](https://templeton.host/tech-tree/proof-techniques/). Names, domain references, and local media paths were adapted for Xavi Ablaza / getablaza.com.

[←Back to Tech Tree](/tech-tree/)

[inventory](/tech-tree/inventory/)[coverage](/tech-tree/coverage/)

# Proof Techniques

Discrete MathDifficulty: ★★☆☆☆Depth: 1Unlocks: 22

Direct proof, proof by contradiction, proof by induction.

## Interactive Visualization

⏮◀◀▶▶STEP0.25x1xZOOM

t=0s

## Core Concepts

- -Direct proof: derive the conclusion from given premises by a finite sequence of valid logical deductions (establishing an implication).
- -Proof by contradiction: assume the negation of the target statement, derive a contradiction with known facts or assumptions, and conclude the original statement holds.
- -Mathematical induction: prove a universally quantified statement over the natural numbers by verifying a base case and proving that truth for an arbitrary n implies truth for n+1.

## Key Symbols & Notation

Universal quantifier ("for all")

## Essential Relationships

- -Each technique transforms the proof goal into a specific logical task: direct proof -> build a chain of implications; contradiction -> derive an explicit contradiction from the negated goal; induction -> reduce a "for all n" claim to base case plus inductive step, yielding the universal claim.

## Prerequisites (1)

[Boolean Logic5 atoms](/tech-tree/logic-basic/)

## Unlocks (6)

[Recurrence Relationslvl 3](/tech-tree/recurrence-relations/)[Propositional Logiclvl 3](/tech-tree/propositional-logic/)[NP-Completenesslvl 4](/tech-tree/np-completeness/)[Greedy Algorithmslvl 3](/tech-tree/greedy-algorithms/)[Modular Arithmeticlvl 2](/tech-tree/modular-arithmetic/)[Pigeonhole Principlelvl 3](/tech-tree/pigeonhole-principle/)

## Referenced by (2)

Where this concept shows up in the operating-finance and personal-finance graphs.

### From Business (2)

[First PrinciplesBusiness

Proof techniques (direct proof, contradiction, induction) are the formalization of first-principles reasoning - start from axioms, derive conclusions through logical steps rather than analogy or authority](/business/first-principles/)[base caseBusiness

Proof by induction is exactly this pattern: establish the base case, then show each generalization (inductive step) preserves the property](/business/base-case/)

Advanced Learning Details

### Graph Position

10

Depth Cost

22

Fan-Out (ROI)

13

Bottleneck Score

1

Chain Length

### Cognitive Load

5

Atomic Elements

28

Total Elements

L1

Percentile Level

L3

Atomic Level

### All Concepts (12)

- - Mathematical proof: a sequence of justified logical deductions from assumptions/axioms to establish a statement's truth
- - Direct proof: proving an implication P → Q by assuming P and deriving Q
- - Proof by contradiction (reductio ad absurdum): proving a statement S by assuming ¬S and deriving a contradiction, hence concluding S
- - Principle of mathematical induction: proving a property for all natural numbers by proving a base case and an induction step
- - Base case (induction): verifying the property for an initial natural number (e.g., n = 0 or n = 1)
- - Induction hypothesis: the assumption that the property holds for an arbitrary but fixed n = k used in the induction step
- - Induction step: deducing the property for k+1 from the induction hypothesis for k
- - Strong (complete) induction: proving P(k+1) by assuming the property holds for all values ≤ k (a stronger form of the induction hypothesis)
- - Well-ordering principle for ℕ: every nonempty subset of the natural numbers has a least element (often presented as equivalent to induction)
- - Predicate/property notation P(n): expressing a statement that depends on an integer parameter n
- - Witness method for existential statements: proving ∃x P(x) by exhibiting a specific x and verifying P(x)
- - Arbitrary-element method for universal statements: to prove ∀x P(x), choose an arbitrary x and show P(x) (foundation for direct proofs and induction)

### Teaching Strategy

Self-serve tutorial - low prerequisites, straightforward concepts.

In discrete math and CS, you’re rarely asked to “compute” something—you’re asked to justify why something is always true. Proof techniques are the reusable tools that turn an intuition (“this should work”) into a guarantee (“this must work”).

TL;DR:

Direct proof builds the conclusion from assumptions step by step. Contradiction proves a statement by showing its negation would force an impossibility. Induction proves ∀n ∈ ℕ statements by (1) a base case and (2) showing n ⇒ n+1.

## What Is Proof Techniques?

A **proof** is a finite sequence of logically valid steps that establishes a statement is true. In this node, “proof techniques” means a small toolkit of common patterns you can apply again and again:

- •**Direct proof**: start from the premises (assumptions) and deduce the conclusion.
- •**Proof by contradiction**: assume the conclusion is false, deduce a contradiction, then conclude the original statement must be true.
- •**Mathematical induction**: prove a statement about all natural numbers (∀n ∈ ℕ) by proving a base case and a step that propagates truth from n to n+1.

Why do we need “techniques” at all? Because most statements you prove in discrete math and CS have recurring logical shapes. If you recognize the shape, you can choose a proof method that matches it.

### The logical backbone: implications and ∀

Many statements you’ll prove look like one of these:

1) **Implication**: P ⇒ Q ("If P, then Q")

2) **Universal claim**: ∀x, S(x) ("For all x, S(x) holds")

Often these combine: ∀n ∈ ℕ, P(n) ⇒ Q(n).

A direct proof is usually the default for implications: assume P and derive Q.

A contradiction proof is useful when the statement is hard to build directly but easy to refute: assume ¬S and show that cannot happen.

Induction is specialized to universal claims over ℕ (or any well-ordered set where “next” makes sense).

### “Show your work” as a discipline

In programming, the compiler checks correctness rules. In proofs, *you* must make each step justified. A good habit:

- •State what you assume.
- •State what you want.
- •Move in small, checkable steps.
- •Name facts you use (definitions, algebra, earlier theorems).

This pacing matters: it keeps proofs readable and prevents you from accidentally assuming what you’re trying to prove.

### A quick map of when each technique shines

| Statement style | Typical goal | Good technique | Why |
| --- | --- | --- | --- |
| P ⇒ Q | Derive Q from P | Direct proof | Matches the structure |
| “No such x exists” / impossibility | Show contradiction emerges | Contradiction | Negation introduces an existence claim |
| ∀n ∈ ℕ, S(n) | Prove all n | Induction | Propagates truth along ℕ |

You can always force a statement into any technique (e.g., prove P ⇒ Q by contradiction), but choosing the “natural” one usually yields a cleaner proof.

## Core Mechanic 1: Direct Proof (Build the Conclusion)

### Why direct proof is the default

Direct proof mirrors how we reason in code: if the input satisfies some precondition P, we show the output satisfies postcondition Q. This is exactly proving P ⇒ Q.

The key move is:

- •**Assume P** (or take an arbitrary element satisfying P).
- •Use definitions and known facts to **deduce new facts**.
- •Continue until you reach **Q**.

### Template

To prove: P ⇒ Q

1) Assume P.

2) Derive...

3) Therefore Q.

When proving a universal implication, you add one extra step:

To prove: ∀x, (P(x) ⇒ Q(x))

1) Let x be arbitrary.

2) Assume P(x).

3) Derive Q(x).

4) Conclude ∀x, (P(x) ⇒ Q(x)).

That “let x be arbitrary” is crucial: it prevents you from accidentally proving the statement only for a special case.

### Example pattern: even/odd, divisibility

Definitions drive many direct proofs.

- •n is **even** ⇔ ∃k ∈ ℤ such that n = 2k
- •n is **odd** ⇔ ∃k ∈ ℤ such that n = 2k + 1
- •a divides b (a ∣ b) ⇔ ∃k ∈ ℤ such that b = ak

Direct proofs often look like: assume a definition, substitute, and simplify.

### A careful multi-step derivation (typical style)

Claim: If n is even, then n² is even.

Assume n is even.

Then ∃k ∈ ℤ such that n = 2k.

Now compute:

n² = (2k)²

= 4k²

= 2(2k²)

Since 2k² ∈ ℤ, we have written n² as 2(integer), so n² is even.

Notice the structure:

- •Use the **definition** of even.
- •Perform algebra.
- •Re-match the **definition** at the end.

### When direct proof feels hard

Sometimes P ⇒ Q is true, but going forward from P doesn’t give you traction. Two common reasons:

1) **Q is an impossibility / non-existence** statement (e.g., “there is no integer solution”). Directly proving non-existence can be awkward.

2) The statement’s contrapositive is easier.

A useful related move (still “direct” in spirit) is proving the **contrapositive**:

P ⇒ Q is logically equivalent to ¬Q ⇒ ¬P.

So if ¬Q is more concrete, prove ¬Q ⇒ ¬P directly.

Example: “If n² is even, then n is even.”

Directly from “n² is even” to “n is even” is possible, but a clean approach is contrapositive:

¬(n is even) ⇒ ¬(n² is even)

That is: if n is odd, then n² is odd (easy by substitution n = 2k+1).

Contrapositive proofs are extremely common in CS correctness and number theory.

## Core Mechanic 2: Proof by Contradiction (Assume the Negation)

### Why contradiction is powerful

Contradiction is a technique for when the statement is difficult to construct directly, but the opposite assumption quickly breaks the rules.

The logic idea is:

- •To prove S, assume ¬S.
- •Derive a contradiction (something of the form T ∧ ¬T, or “0 = 1”, or a violation of a known fact).
- •Conclude the assumption ¬S is impossible, so S must be true.

Formally, it uses that (¬S ⇒ False) implies S.

### Template

To prove: S

1) Assume ¬S.

2) Derive a contradiction.

3) Therefore S.

### What counts as a contradiction?

A contradiction can be:

- •A direct logical form: P and ¬P
- •An algebraic impossibility: 1 = 0
- •A violation of a known theorem/definition
- •A violation of constraints (e.g., you derive an integer must be both even and odd)

### Why contradiction is especially good for “no such thing exists”

Statements like “There is no integer x such that …” are negations of existential statements.

- •Original: “No x exists such that A(x)”
- •Equivalent: ¬(∃x, A(x))

To prove ¬(∃x, A(x)) by contradiction, you assume the opposite:

Assume ∃x, A(x)

Then pick such an x and derive an impossibility.

That’s often much easier than trying to directly show non-existence.

### Classic example: √2 is irrational (structure you should recognize)

The claim “√2 is irrational” means:

¬(∃a, b ∈ ℤ with b ≠ 0 such that √2 = a/b in lowest terms)

The contradiction proof assumes there *is* such a fraction in lowest terms and then shows both a and b must be even, contradicting “lowest terms.”

You don’t need to memorize every detail now, but recognize the pattern:

- •Assume a minimal/canonical counterexample exists.
- •Show it implies an even smaller one (or violates minimality).
- •Contradiction.

### Contradiction vs contrapositive

Both are related but not identical in practice.

| Method | What you assume | What you aim to show | Common feel |
| --- | --- | --- | --- |
| Contrapositive | ¬Q | ¬P | Still “forward” reasoning |
| Contradiction | ¬S | False | “Assume opposite, crash” |

If the statement is an implication P ⇒ Q, then a contradiction proof often looks like:

Assume P ∧ ¬Q, derive contradiction.

This is equivalent to proving (P ⇒ Q) because (P ∧ ¬Q) is exactly the negation of (P ⇒ Q).

### A pacing tip: isolate the “negation” carefully

Most mistakes in contradiction proofs come from negating the target incorrectly.

Example: Negate “∀n ∈ ℕ, S(n)” correctly:

¬(∀n ∈ ℕ, S(n)) ⇔ ∃n ∈ ℕ such that ¬S(n)

So a contradiction proof against a universal statement often begins:

Assume there exists n with ¬S(n).

Let n be such a counterexample.

...

contradiction.

That step (turning ∀ into ∃) is not cosmetic—it changes the whole structure of the proof.

## Core Mechanic 3: Mathematical Induction (Prove ∀n ∈ ℕ)

### Why induction matches computation

Many CS objects are defined “by size”: lists of length n, trees with n nodes, loops that run n times, sequences defined by recurrence relations.

If a property is true for size 0 (or 1), and if truth for size n forces truth for size n+1, then it’s true for all sizes. That’s the heart of induction.

Induction is not “hand-wavy dominoes”; it’s a rigorous way to prove:

∀n ∈ ℕ, S(n)

### The standard induction scheme

To prove ∀n ≥ n₀, S(n):

1) **Base case**: Prove S(n₀).

2) **Inductive step**:

- •Assume S(n) for an arbitrary n ≥ n₀ (this is the **inductive hypothesis**).
- •Using that assumption, prove S(n+1).

3) Conclude ∀n ≥ n₀, S(n).

The “assume S(n)” is not circular because you assume it only for a generic n and use it to prove the next case.

### A typical algebraic induction: sum of first n integers

Claim: ∀n ∈ ℕ, 1 + 2 + ⋯ + n = n(n+1)/2.

This is a perfect induction target because:

- •It’s explicitly about “all n.”
- •The statement for n+1 naturally relates to the statement for n.

You’ll see the full worked version in the examples below.

### Strong induction (brief preview)

Sometimes S(n+1) depends not just on S(n), but on multiple earlier cases. Then you can use **strong induction**:

Inductive hypothesis: assume S(k) is true for all k with n₀ ≤ k ≤ n.

Prove S(n+1).

At difficulty 2, the key is: strong induction is still induction—it just gives you a stronger hypothesis.

### Common “induction hygiene”

1) **State the domain**: n ∈ ℕ, n ≥ 1, etc.

2) **Write the inductive hypothesis explicitly** (don’t keep it implicit).

3) In the inductive step, start from what you want:

Want: S(n+1)

Use: S(n)

4) Don’t confuse n (arbitrary) with a specific number.

### Why induction matters later

Induction underlies:

- •proofs of correctness for loops and recursive functions
- •bounds on recurrences (like in [Recurrence Relations](/tech-tree/recurrence-relations/))
- •graph/tree properties proved by size

It’s one of the most “CS-native” proof techniques because it aligns with how programs are structured.

## Application/Connection: How These Techniques Power Discrete Math and CS

### Proof techniques as “interfaces” between intuition and guarantees

In CS, many advanced topics are about proving some transformation preserves truth:

- •a reduction transforms instances of problem A into instances of problem B
- •a greedy algorithm makes a local choice and you must prove it can be extended to an optimal global solution
- •modular arithmetic manipulates congruences while preserving equivalence

Each of those ultimately becomes a statement like:

- •∀x, P(x) ⇒ Q(f(x)) (direct proof)
- •“No counterexample exists” (contradiction)
- •∀n, algorithm works for size n (induction)

### Concrete connections

1) **Modular Arithmetic**

You often prove things like:

If a ≡ b (mod m), then a + c ≡ b + c (mod m).

That is a direct proof using the definition:

a ≡ b (mod m) ⇔ m ∣ (a − b).

2) **Greedy Algorithms**

A common proof pattern is an “exchange argument,” often structured as contradiction:

Assume an optimal solution exists that disagrees with the greedy choice.

Modify (“exchange”) it to agree without hurting optimality.

Contradiction to the assumption that greedy was not part of some optimal solution.

3) **NP-Completeness**

Reductions are implication statements:

x ∈ A ⇒ f(x) ∈ B

x ∉ A ⇒ f(x) ∉ B

You prove these with direct proofs (sometimes via contrapositive).

4) **Propositional Logic**

Proof techniques train you to manipulate:

- •implications
- •negations
- •quantifiers like ∀ and ∃

This helps when you later formalize satisfiability arguments.

### Choosing a technique: a small checklist

| If your statement looks like… | Try… | Because… |
| --- | --- | --- |
| P ⇒ Q | Direct proof | Most straightforward |
| “For all n…” | Induction | Natural number structure |
| “No such thing exists” | Contradiction | Negation introduces ∃ |
| “If not Q then not P” is easy | Contrapositive | Equivalent to implication |

### A final meta-skill: write proofs like readable programs

Good proofs:

- •declare inputs (assumptions)
- •use named lemmas (helper results)
- •maintain invariants (especially in induction)
- •end with the exact goal statement

That habit will transfer directly to algorithm correctness, complexity arguments, and rigorous ML derivations later (e.g., showing an objective decreases each step).

## Worked Examples (3)

### Direct proof: The sum of two even integers is even

Prove: If a and b are even integers, then a + b is even.

1. Assume a and b are even.

   By definition of even, ∃k ∈ ℤ such that a = 2k, and ∃m ∈ ℤ such that b = 2m.
2. Compute the sum:

   a + b = 2k + 2m
3. Factor out 2:

   a + b = 2(k + m)
4. Since k + m ∈ ℤ, we have written a + b as 2·(integer).

   Therefore, by the definition of even, a + b is even.

**Insight:** Direct proofs often follow a “definition → algebra → definition” loop. You unpack the assumption into an existence form, simplify, then repack it into the target definition.

### Contradiction: There is no smallest positive rational number

Prove: There is no smallest positive rational number.

1. Let S be the set of positive rational numbers.

   We want to prove: there does not exist r ∈ S such that r ≤ q for all q ∈ S.
2. Assume for contradiction that there is a smallest positive rational number r.

   So r > 0 and for all q > 0 (q rational), we have r ≤ q.
3. Consider the rational number r/2.

   Since r is rational, r/2 is rational. Since r > 0, we also have r/2 > 0.

   Therefore r/2 ∈ S.
4. By “r is the smallest element,” we must have r ≤ r/2.
5. But r ≤ r/2 implies (multiplying both sides by 2 > 0):

   2r ≤ r

   So r ≤ 0, which contradicts r > 0.
6. Therefore our assumption was false, and there is no smallest positive rational number.

**Insight:** A good contradiction proof constructs a specific object that violates the assumed extremal property (here: if r is “smallest,” r/2 is smaller). This pattern repeats in many CS proofs (minimal counterexample arguments).

### Induction: Sum of the first n odd numbers equals n²

Prove: ∀n ∈ ℕ, 1 + 3 + 5 + ⋯ + (2n − 1) = n².

1. Define S(n): 1 + 3 + 5 + ⋯ + (2n − 1) = n².

   We will prove ∀n ∈ ℕ, S(n) by induction.
2. Base case (n = 1):

   Left side = 1.

   Right side = 1² = 1.

   So S(1) holds.
3. Inductive hypothesis: Assume S(n) holds for an arbitrary n ≥ 1.

   That is, assume:

   1 + 3 + 5 + ⋯ + (2n − 1) = n².
4. Inductive step: Prove S(n+1).

   Start with the left side for n+1:

   1 + 3 + ⋯ + (2n − 1) + (2(n+1) − 1)
5. Use the inductive hypothesis to replace the partial sum:

   = n² + (2(n+1) − 1)
6. Simplify the new term:

   2(n+1) − 1 = 2n + 2 − 1 = 2n + 1
7. So the expression becomes:

   = n² + (2n + 1)

   = n² + 2n + 1

   = (n + 1)²
8. Thus S(n+1) holds.

   By induction, ∀n ∈ ℕ, 1 + 3 + ⋯ + (2n − 1) = n².

**Insight:** Induction works because the (n+1) case contains the n case plus one extra piece. The inductive hypothesis is like a reusable “macro” you’re allowed to substitute once per step.

## Key Takeaways

- ✓

  Most discrete math proofs reduce to a small set of reusable patterns: direct, contradiction, induction.
- ✓

  Direct proof matches implications P ⇒ Q: assume P and derive Q using definitions and known facts.
- ✓

  Contradiction proves S by assuming ¬S and deriving an impossibility; it’s especially effective for non-existence claims.
- ✓

  Be careful negating quantified statements: ¬(∀x, S(x)) ⇔ ∃x such that ¬S(x).
- ✓

  Induction proves ∀n ∈ ℕ statements via a base case and an inductive step (assume S(n) to prove S(n+1)).
- ✓

  Writing the inductive hypothesis explicitly prevents circular reasoning and keeps the proof checkable.
- ✓

  Choosing the right technique is often about recognizing the statement’s logical shape (implication, universal, non-existence).

## Common Mistakes

- ✗

  Negating a statement incorrectly, especially with quantifiers (mixing up ∀ and ∃).
- ✗

  In induction, forgetting to specify the starting index (n ≥ 0 vs n ≥ 1) or proving the wrong base case.
- ✗

  Using the inductive hypothesis for n+1 (what you’re trying to prove) instead of only for n (what you’re allowed to assume).
- ✗

  In direct proofs, skipping the defining step (e.g., claiming “n even” implies “n = 2k” without stating existence of k ∈ ℤ).

## Practice

easy

Direct proof: Prove that if a is an odd integer and b is an odd integer, then a + b is even.

**Hint:** Use the definition: odd means a = 2k + 1 for some k ∈ ℤ. Add and simplify into 2·(integer).

Show solution

Assume a and b are odd.

Then ∃k, m ∈ ℤ such that a = 2k + 1 and b = 2m + 1.

Add:

a + b = (2k + 1) + (2m + 1)

= 2k + 2m + 2

= 2(k + m + 1).

Since k + m + 1 ∈ ℤ, a + b is even by definition.

easy

Contradiction: Prove that there is no integer n such that n is both even and odd.

**Hint:** Assume n is even and odd. Then n = 2k and n = 2m + 1 for integers k, m. Compare parity.

Show solution

Assume for contradiction there exists an integer n that is both even and odd.

Then ∃k ∈ ℤ with n = 2k, and ∃m ∈ ℤ with n = 2m + 1.

Set them equal: 2k = 2m + 1.

Then 2k − 2m = 1 ⇒ 2(k − m) = 1.

But the left side is even (a multiple of 2), while the right side is odd. This is impossible.

Therefore no integer is both even and odd.

medium

Induction: Prove that ∀n ∈ ℕ, 1 + 2 + ⋯ + n = n(n + 1)/2.

**Hint:** Base case n = 1. For the step, write the (n+1) sum as (1+…+n) + (n+1) and substitute the hypothesis.

Show solution

Let S(n) be the statement 1 + 2 + ⋯ + n = n(n + 1)/2.

Base case (n = 1): left side = 1, right side = 1·2/2 = 1, so S(1) holds.

Inductive hypothesis: assume S(n) holds for some arbitrary n ≥ 1:

1 + 2 + ⋯ + n = n(n + 1)/2.

Inductive step: consider the sum to n+1:

1 + 2 + ⋯ + n + (n + 1)

= (1 + 2 + ⋯ + n) + (n + 1)

= n(n + 1)/2 + (n + 1)

= n(n + 1)/2 + 2(n + 1)/2

= (n(n + 1) + 2(n + 1))/2

= (n + 1)(n + 2)/2

= (n + 1)((n + 1) + 1)/2.

Thus S(n+1) holds. By induction, ∀n ∈ ℕ, 1 + 2 + ⋯ + n = n(n + 1)/2.

## Connections

Next nodes that heavily rely on these patterns:

- •[Propositional Logic](/tech-tree/propositional-logic/) — formalizing implication, negation, and equivalence used in every proof.
- •[Modular Arithmetic](/tech-tree/modular-arithmetic/) — many results are direct proofs using the definition of congruence.
- •[Recurrence Relations](/tech-tree/recurrence-relations/) — induction is the standard way to verify closed forms.
- •[Greedy Algorithms](/tech-tree/greedy-algorithms/) — correctness proofs often use contradiction or exchange arguments.
- •[NP-Completeness](/tech-tree/np-completeness/) — reductions are implication proofs (often with contrapositives).

Quality: A (4.4/5)

[← back to tree](/tech-tree/)[browse all →](/tech-tree/inventory/)
