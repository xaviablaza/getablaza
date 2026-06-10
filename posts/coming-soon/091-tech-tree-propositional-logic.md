---
title: Propositional Logic
description: Formal system with propositions, connectives. Satisfiability.
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
permalink: /tech-tree/propositional-logic/
---

[←Back to Tech Tree](/tech-tree/)

[inventory](/tech-tree/inventory/)[coverage](/tech-tree/coverage/)

# Propositional Logic

Formal MethodsDifficulty: ★★★☆☆Depth: 2Unlocks: 6

Formal system with propositions, connectives. Satisfiability.

## Interactive Visualization

⏮◀◀▶▶STEP0.25x1xZOOM

t=0s

## Core Concepts

- -Atomic proposition (propositional variable: an indivisible statement with a truth value)
- -Well-formed formula (syntactic composition of propositions using connectives)
- -Truth-functional semantics (truth assignments to variables and evaluation of formulas)

## Key Symbols & Notation

Propositional variable symbol (e.g., p, q)Negation symbol (NOT, written as '¬' or 'not')Implication symbol (material implication, written as '->')

## Essential Relationships

- -Connectives are truth-functional: the truth of a compound formula is determined solely by the truth values of its immediate subformulas
- -Satisfiability: a formula is satisfiable iff there exists a truth assignment that makes it true
- -Semantic consequence/validity: a formula is valid (or a conclusion is entailed) iff its truth is preserved across all truth assignments (or all assignments that make the premises true)

## Prerequisites (2)

[Boolean Logic5 atoms](/tech-tree/logic-basic/)[Proof Techniques5 atoms](/tech-tree/proof-techniques/)

## Unlocks (2)

[Complexity Classeslvl 4](/tech-tree/complexity-classes/)[Predicate Logiclvl 3](/tech-tree/predicate-logic/)

Advanced Learning Details

### Graph Position

19

Depth Cost

6

Fan-Out (ROI)

4

Bottleneck Score

2

Chain Length

### Cognitive Load

9

Atomic Elements

46

Total Elements

L3

Percentile Level

L4

Atomic Level

### All Concepts (20)

- - propositional variable (atomic proposition) - a basic, indivisible statement symbol (e.g., p, q, r)
- - well‑formed formula (WFF) / propositional formula - syntactic expressions built from variables and connectives according to formation rules
- - syntax vs semantics - distinction between the formal string structure of formulas and their truth/value interpretation
- - valuation (truth assignment) - a function mapping each propositional variable to true or false
- - model - a valuation that makes a formula (or every formula in a set) true
- - satisfiable - a formula that has at least one model (there exists a valuation that makes it true)
- - unsatisfiable / contradiction - a formula that has no model (false under every valuation)
- - tautology / valid formula - a formula true under every valuation (every valuation is a model)
- - satisfiability decision problem (SAT) - the decision problem of determining whether a given propositional formula is satisfiable
- - material implication (conditional connective) - the connective commonly written A → B (truth defined by truth table, distinct conceptual status from meta‑level entailment)
- - biconditional connective - A ↔ B, true exactly when A and B have the same truth value
- - literal - an occurrence of either a propositional variable or its negation (p or ¬p)
- - clause - a disjunction of literals (possibly a single literal)
- - conjunctive normal form (CNF) - a formula that is a conjunction of clauses
- - disjunctive normal form (DNF) - a formula that is a disjunction of conjunctions of literals
- - empty clause - a clause containing no literals used to represent explicit contradiction/unsatisfiability in refutation
- - resolution rule (propositional resolution) - an inference rule operating on clauses to derive new clauses (used for refutation)
- - syntactic derivability / proof relation - formal proof notion (Γ ⊢ φ) expressing that φ can be derived from axioms/rules syntactically
- - semantic entailment / logical consequence - semantic relation (Γ ⊨ φ) meaning every model of Γ is a model of φ
- - soundness and completeness (for a proof system) - soundness: all syntactic derivations are semantically valid; completeness: all semantic entailments are syntactically derivable

### Teaching Strategy

Deep-dive lesson - accessible entry point but dense material. Use worked examples and spaced repetition.

Propositional logic is the smallest “formal language” where you can clearly separate two worlds: (1) syntax—what strings of symbols are well-formed—and (2) semantics—what those strings mean under a truth assignment. That split is the foundation of formal verification, SAT solving, and (eventually) NP-completeness and predicate logic.

TL;DR:

Propositional logic builds formulas from atomic propositions (p, q, r) using connectives (¬, ∧, ∨, →, ↔). A valuation v assigns each atom T/F; semantics evaluates a formula to T/F under v. Key tasks: evaluate a formula under v, decide satisfiable/unsatisfiable, check validity, and reduce entailment Γ ⊨ φ to an unsatisfiability check of Γ ∧ ¬φ.

## What Is Propositional Logic?

### Why this concept exists (motivation)

In everyday reasoning you mix **language** (“If it rains, the ground is wet”) with **meaning** (is it true today?). Propositional logic exists to make that separation precise:

- •**Syntax**: rules for building *well-formed formulas* (WFFs) from symbols.
- •**Semantics**: rules for assigning truth values to formulas given truth values of atoms.

This separation lets you do three powerful things:

1. 1)**Evaluate** a statement given facts (a truth assignment).
2. 2)**Search** for a counterexample model when a claim is not always true.
3. 3)**Reduce reasoning to computation**: satisfiability (SAT) becomes a central problem.

You already know Boolean operators and truth tables. Propositional logic adds:

- •a formal grammar for what counts as a formula,
- •standard semantic definitions (not just ad-hoc truth tables),
- •meta-questions like satisfiable/valid/entailed.

### Core objects

**Atomic propositions** (aka propositional variables): symbols like p, q, r. Each represents an indivisible statement with a truth value (T/F). Propositional logic does **not** look inside p to see structure like “rains(today)”. That is what predicate logic will do later.

**Connectives** (common set):

| Name | Symbol(s) | Reads as | Intuition |
| --- | --- | --- | --- |
| Negation | ¬φ | not φ | flips truth |
| Conjunction | φ ∧ ψ | φ and ψ | both true |
| Disjunction | φ ∨ ψ | φ or ψ | at least one true |
| Implication | φ → ψ | if φ then ψ | false only when φ true and ψ false |
| Biconditional | φ ↔ ψ | φ iff ψ | same truth value |

**Well-formed formula (WFF)**: a string built by rules, e.g.

- •p is a WFF
- •if φ is a WFF then ¬φ is a WFF
- •if φ, ψ are WFFs then (φ ∧ ψ), (φ ∨ ψ), (φ → ψ), (φ ↔ ψ) are WFFs

Parentheses (or operator precedence) remove ambiguity.

### Semantics: truth-functional meaning

A **valuation** (truth assignment) v maps atoms to {T, F}. For example:

- •v(p) = T
- •v(q) = F
- •v(r) = T

Then each connective is defined truth-functionally. For implication:

⟦φ→ψ⟧v=F iff ⟦φ⟧v=T and ⟦ψ⟧v=F.\llbracket \varphi \to \psi \rrbracket\_v = \text{F} \text{ iff } \llbracket \varphi \rrbracket\_v=\text{T and } \llbracket \psi \rrbracket\_v=\text{F}.[[φ→ψ]]v​=F iff [[φ]]v​=T and [[ψ]]v​=F.

Everything else is defined similarly. The important meta-point: **meaning is computed structurally from syntax**.

### Three big semantic properties

Given a formula φ:

- •**Satisfiable**: there exists v with ⟦φ⟧ᵥ = T. (∃ model)
- •**Unsatisfiable**: for all v, ⟦φ⟧ᵥ = F. (no models)
- •**Valid** (tautology): for all v, ⟦φ⟧ᵥ = T. (true in every model)

These are different questions. For example, p ∨ ¬p is valid. p ∧ ¬p is unsatisfiable. p → q is satisfiable but not valid.

### A first “model-thinking” picture

A valuation v is like a point in a space of possible worlds. With two atoms p and q there are 4 valuations:

```
           q=T                q=F
        +--------+         +--------+
 p=T    |  (T,T) |         |  (T,F) |
        +--------+         +--------+
 p=F    |  (F,T) |         |  (F,F) |
        +--------+         +--------+
```

A formula φ corresponds to a **set of valuations** (its models):

Mod(φ)={v∣⟦φ⟧v=T}.\text{Mod}(\varphi) = \{ v \mid \llbracket \varphi \rrbracket\_v = \text{T} \}.Mod(φ)={v∣[[φ]]v​=T}.

Thinking this way makes satisfiable/valid/unsatisfiable feel like set properties:

- •satisfiable ⇔ Mod(φ) ≠ ∅
- •valid ⇔ Mod(φ) is the whole space
- •unsatisfiable ⇔ Mod(φ) = ∅

## Syntax: Building and Parsing Well-Formed Formulas

### Why syntax matters

If you want computation or proof, you need to know what the input language is. “p → q → r” is ambiguous unless you specify parsing rules. Syntax gives you:

- •what strings are legal,
- •a unique structure for evaluation and transformation,
- •a path to algorithms (parsers, ASTs, CNF conversion).

### Grammar (one standard version)

Let PropVar be a set of atoms: p, q, r, …

Define formulas recursively:

1. 1)Every atom p ∈ PropVar is a formula.
2. 2)If φ is a formula, then ¬φ is a formula.
3. 3)If φ and ψ are formulas, then (φ ∧ ψ), (φ ∨ ψ), (φ → ψ), (φ ↔ ψ) are formulas.

This is a typical inductive definition: it both defines the set of formulas and enables proofs by structural induction.

### Operator precedence and associativity (practical parsing)

Many texts adopt precedence like:

1. 1)¬ (highest)
2. 2)∧
3. 3)∨
4. 4)→
5. 5)↔ (lowest)

And often take → as right-associative: φ → ψ → χ means φ → (ψ → χ).

When in doubt, parenthesize.

### Inline diagram: parse tree (syntax becomes structure)

Consider the formula:

φ=¬(p∧q)→r.\varphi = \neg(p \wedge q) \to r.φ=¬(p∧q)→r.

Its parse tree (abstract syntax tree) makes the structure explicit:

```
             (→)
            /   \
          (¬)    r
           |
          (∧)
         /   \
        p     q
```

Read it bottom-up: p and q combine with ∧, then negated, then implies r.

This matters because evaluation follows the tree. Also, transformations (like pushing negations inward) are tree rewrites.

### Well-formed vs not well-formed

- •WFF: (p ∧ (¬q → r))
- •Not WFF (missing operand): (p ∧ → q)
- •Not WFF (bad nesting): p ∧ (q →)

In an interactive canvas, a good “syntax mode” task is:

- •highlight matching parentheses,
- •show the parse tree live,
- •show where the grammar rule fails if it’s not a WFF.

### A note about different symbol choices

You may see:

- •NOT: ¬, ~, !
- •AND: ∧, &, ·
- •OR: ∨, |
- •implies: →, =>

The logic is the same; syntax is a surface layer. What matters is the connective’s truth function.

## Semantics: Valuations, Models, and Evaluating Formulas

### Why semantics deserves its own section

A common learner mistake is to treat formulas as if they are “just” Boolean expressions without appreciating the meta-questions: **which valuations make it true?** That is the semantics lens.

### Valuations (truth assignments)

A valuation v assigns each atom a truth value:

v:PropVar→{T,F}.v: \text{PropVar} \to \{\text{T},\text{F}\}.v:PropVar→{T,F}.

Given v, extend it to all formulas by recursion on structure:

- •⟦p⟧ᵥ = v(p)
- •⟦¬φ⟧ᵥ = not ⟦φ⟧ᵥ
- •⟦φ ∧ ψ⟧ᵥ = (⟦φ⟧ᵥ and ⟦ψ⟧ᵥ)
- •⟦φ ∨ ψ⟧ᵥ = (⟦φ⟧ᵥ or ⟦ψ⟧ᵥ)
- •⟦φ → ψ⟧ᵥ = (not ⟦φ⟧ᵥ) or ⟦ψ⟧ᵥ
- •⟦φ ↔ ψ⟧ᵥ = (⟦φ⟧ᵥ = ⟦ψ⟧ᵥ)

Notice implication’s definition:

⟦φ→ψ⟧v≡(¬⟦φ⟧v)∨⟦ψ⟧v.\llbracket \varphi \to \psi \rrbracket\_v \equiv (\neg \llbracket \varphi \rrbracket\_v) \lor \llbracket \psi \rrbracket\_v.[[φ→ψ]]v​≡(¬[[φ]]v​)∨[[ψ]]v​.

This equivalence is extremely useful for transformations.

### Material implication: the “surprising” cases

Because φ → ψ is defined as ¬φ ∨ ψ:

- •If φ is false, then φ → ψ is true (no matter ψ).
- •The only falsifying case is: φ true and ψ false.

This matches the idea: “the only way to violate a promise ‘if φ then ψ’ is to have φ happen but ψ fail.”

### Models and model sets

A valuation v is a **model** of φ if ⟦φ⟧ᵥ = T, written v ⊨ φ.

The set of all models:

Mod(φ)={v∣v⊨φ}.\mathrm{Mod}(\varphi) = \{v \mid v \vDash \varphi\}.Mod(φ)={v∣v⊨φ}.

This is where the Venn-style picture becomes concrete.

#### Inline diagram: small model-set view (two variables)

Let the universe U be all valuations over {p, q}. Define:

- •A = Mod(p)
- •B = Mod(q)

Then:

- •Mod(p ∧ q) = A ∩ B
- •Mod(p ∨ q) = A ∪ B
- •Mod(¬p) = U \ A

A tiny “set” sketch (not to scale) helps:

```
Universe U (all valuations over p,q)

   +---------------------------+
   |        ________           |
   |       /        \          |
   |      /   A=p    \         |
   |     |    ______  |        |
   |     |   /  B  \  |        |
   |     |   \_____/  |        |
   |      \          /         |
   |       \________/          |
   +---------------------------+

A ∩ B corresponds to p ∧ q
U \ A corresponds to ¬p
```

Even if the drawing is abstract, the mapping “connectives ↔ set operations” is real and is a powerful intuition pump.

### Truth tables vs structural evaluation

Truth tables enumerate all valuations. Structural evaluation computes ⟦φ⟧ᵥ for one v.

In an interactive canvas, you want both workflows:

1. 1)**Evaluate under v**: pick v(p)=T/F toggles, compute formula value live (following the parse tree).
2. 2)**Find a counterexample**: search for a v making the formula false (for non-validity) or true (for satisfiability).

### Key semantic relations

1) **Satisfiable**: ∃v, v ⊨ φ

2) **Valid**: ∀v, v ⊨ φ

3) **Entailment**: Γ ⊨ φ means every valuation that satisfies all formulas in Γ also satisfies φ.

Formally, for a finite set Γ = {γ₁, …, γₖ}:

Γ⊨φiff∀v:(⋀i=1kv⊨γi)⇒(v⊨φ).\Gamma \vDash \varphi \quad\text{iff}\quad \forall v: \Big( \bigwedge\_{i=1}^k v \vDash \gamma\_i \Big) \Rightarrow (v \vDash \varphi).Γ⊨φiff∀v:(i=1⋀k​v⊨γi​)⇒(v⊨φ).

Model-set view:

Mod(Γ)⊆Mod(φ).\mathrm{Mod}(\Gamma) \subseteq \mathrm{Mod}(\varphi).Mod(Γ)⊆Mod(φ).

That single subset statement is often the cleanest way to think.

## Satisfiability, Validity, and Entailment via UNSAT Reductions

### Why SAT is the center of gravity

Many reasoning questions can be converted into SAT/UNSAT checks. This is a big deal because:

- •SAT has extremely optimized solvers in practice.
- •SAT is the gateway to complexity theory (NP-completeness).
- •Formal methods (model checking, verification) rely on reducing problems to SAT.

So you want a mental toolkit of reductions.

### Satisfiable vs valid: duality with negation

A formula φ is valid exactly when ¬φ is unsatisfiable:

⊨φiff¬φ is UNSAT.\vDash \varphi \quad\text{iff}\quad \neg\varphi \text{ is UNSAT}.⊨φiff¬φ is UNSAT.

**Show the work (both directions):**

(⇒) If φ is valid, then for all v, ⟦φ⟧ᵥ=T. So for all v, ⟦¬φ⟧ᵥ=F. Hence ¬φ has no model, so it’s UNSAT.

(⇐) If ¬φ is UNSAT, then there is no v with ⟦¬φ⟧ᵥ=T. So for all v, ⟦¬φ⟧ᵥ=F, hence ⟦φ⟧ᵥ=T. So φ is valid.

This “prove validity by showing UNSAT of the negation” is a standard solver workflow.

### Entailment as an UNSAT check

For a set of premises Γ (think: assumptions) and conclusion φ:

Γ⊨φiffΓ∧¬φ is UNSAT.\Gamma \vDash \varphi \quad\text{iff}\quad \Gamma \wedge \neg\varphi \text{ is UNSAT}.Γ⊨φiffΓ∧¬φ is UNSAT.

Where “Γ ∧ ¬φ” means conjoining all premises with ¬φ:

(⋀γ∈Γγ)∧¬φ.\Big(\bigwedge\_{\gamma \in \Gamma} \gamma\Big) \wedge \neg\varphi.(γ∈Γ⋀​γ)∧¬φ.

**Derivation (step-by-step):**

Start from definition:

Γ⊨φ  ⟺  ∀v:(v⊨Γ)⇒(v⊨φ).\Gamma \vDash \varphi \iff \forall v: (v \vDash \Gamma) \Rightarrow (v \vDash \varphi).Γ⊨φ⟺∀v:(v⊨Γ)⇒(v⊨φ).

Replace implication with a forbidden counterexample:

∀v:¬((v⊨Γ)∧¬(v⊨φ)).\forall v: \neg\big( (v \vDash \Gamma) \wedge \neg(v \vDash \varphi) \big).∀v:¬((v⊨Γ)∧¬(v⊨φ)).

But “v ⊨ Γ and not(v ⊨ φ)” is exactly “v ⊨ (Γ ∧ ¬φ)”. So:

Γ⊨φ  ⟺  ∄v:v⊨(Γ∧¬φ).\Gamma \vDash \varphi \iff \nexists v: v \vDash (\Gamma \wedge \neg\varphi).Γ⊨φ⟺∄v:v⊨(Γ∧¬φ).

And “there does not exist a satisfying valuation” is precisely UNSAT.

### Counterexamples become tangible objects

If Γ ⊭ φ, then Γ ∧ ¬φ is satisfiable, and any satisfying valuation is a **countermodel**:

- •it makes all premises true,
- •it makes the conclusion false.

In an interactive canvas, “show counterexample for non-validity” should literally output a valuation v (e.g., p=T, q=F, r=F) and highlight which subformulas evaluate to what.

### Mini comparison table: which question becomes which SAT task?

| Reasoning goal | Convert to | What solver returns |
| --- | --- | --- |
| Is φ satisfiable? | SAT(φ) | a model v if yes |
| Is φ valid? | UNSAT(¬φ) | UNSAT proof or no model |
| Does Γ entail φ? | UNSAT(Γ ∧ ¬φ) | UNSAT or countermodel |
| Are φ and ψ equivalent? | UNSAT((φ ∧ ¬ψ) ∨ (¬φ ∧ ψ)) or UNSAT(¬(φ ↔ ψ)) | UNSAT or countermodel |

This is the “reduction mindset” you’ll reuse in complexity and formal methods.

## Application/Connection: From Propositional Logic to SAT Solvers, Complexity, and Predicate Logic

### Why this connects outward

Propositional logic looks small, but it is the substrate for:

- •**SAT-based verification** (hardware circuits, constraints, planning)
- •**NP-completeness** (SAT is the canonical NP-complete problem)
- •**Predicate logic** (adds quantifiers and structure, but keeps the syntax/semantics split)

### Propositional logic as a circuit language

Every formula corresponds to a Boolean circuit:

- •atoms are inputs,
- •connectives are gates.

Evaluation under v is circuit evaluation. Satisfiability is “is there an input making the output 1?” Validity is “does the circuit output 1 for all inputs?”

This is why SAT solvers are so effective: they are optimized engines for exploring huge input spaces using pruning and learned clauses.

### CNF and SAT (high-level preview)

A standard solver interface expects **CNF** (conjunctive normal form):

⋀i(⋁jℓij)\bigwedge\_i \big(\bigvee\_j \ell\_{ij}\big)i⋀​(j⋁​ℓij​)

where each literal ℓ is either p or ¬p.

You do not need full CNF conversion details yet, but conceptually:

- •syntax trees get rewritten,
- •semantics stays the same (equivalent formulas have the same model set).

### Entailment and verification workflow

Suppose a system must satisfy a safety property Safe under assumptions A.

You want: A ⊨ Safe.

Reduce to UNSAT:

A∧¬Safe is UNSAT.A \wedge \neg Safe \text{ is UNSAT}.A∧¬Safe is UNSAT.

If SAT, the model is a counterexample scenario (a bug trace in richer logics).

### Bridge to complexity classes

SAT is central because:

- •SAT ∈ NP (a proposed valuation is a certificate verifiable in polynomial time).
- •SAT is NP-complete (every NP problem reduces to SAT).

So the satisfiability question you learned here becomes the landmark problem behind P vs NP discussions.

### Bridge to predicate logic

Predicate logic keeps the same pattern:

- •syntax: terms, predicates, quantifiers
- •semantics: structures/interpretations + variable assignments

But satisfiability becomes much harder (even undecidable in full first-order logic). Propositional logic is the “controlled environment” where the key ideas are clean.

### Interactive canvas tasks (explicit)

A good interactive environment for this node should support three concrete learner actions:

1. 1)**Evaluate under v**

- •UI: toggles for p, q, r…
- •Output: ⟦φ⟧ᵥ plus per-subformula values (tree annotation)

2. 2)**Show counterexample for non-validity**

- •Action: user asks “Is φ valid?”
- •System: check UNSAT(¬φ). If SAT, return a valuation v falsifying φ.

3. 3)**Reduce entailment to UNSAT**

- •Inputs: premises Γ and conclusion φ
- •System: build (Γ ∧ ¬φ), attempt SAT
- •If SAT: show countermodel; if UNSAT: mark entailment holds

These tasks force the syntax/semantics split and make “models” tangible rather than abstract.

## Worked Examples (3)

### Evaluate a formula under a valuation (syntax-guided evaluation)

Let φ = ¬(p ∧ q) → r. Use valuation v with v(p)=T, v(q)=F, v(r)=F. Compute ⟦φ⟧ᵥ step-by-step following the parse tree.

1. Start with the innermost connective: (p ∧ q).

   We have ⟦p⟧ᵥ = T and ⟦q⟧ᵥ = F.

   So ⟦p ∧ q⟧ᵥ = T ∧ F = F.
2. Negate that subformula:

   ⟦¬(p ∧ q)⟧ᵥ = ¬F = T.
3. Evaluate the implication:

   φ = ¬(p ∧ q) → r.

   We have left side = T and ⟦r⟧ᵥ = F.

   So ⟦φ⟧ᵥ = T → F = F (this is the one falsifying case for implication).

**Insight:** Evaluation is structural: compute leaves (atoms), combine upward using connective definitions. The parse tree is an evaluation plan. Implication is only false when antecedent is true and consequent is false.

### Show non-validity by finding a counterexample valuation

Consider ψ = (p → q) → (¬q → ¬p). Decide whether ψ is valid. If not, give a counterexample valuation; if yes, argue via UNSAT of its negation or direct reasoning.

1. Recognize the pattern: (p → q) → (¬q → ¬p) is the law of contraposition, which should be valid in propositional logic (material implication).
2. Confirm by reasoning with truth-functional equivalences.

   First rewrite implications:

   (p → q) ≡ (¬p ∨ q)

   (¬q → ¬p) ≡ (q ∨ ¬p)
3. So ψ becomes:

   (¬p ∨ q) → (q ∨ ¬p).
4. But the antecedent and consequent are syntactically the same up to commutativity of ∨:

   (¬p ∨ q) and (q ∨ ¬p) are equivalent.

   So we have a form: A → A, which is always true.
5. Therefore ψ is valid: for all valuations v, ⟦ψ⟧ᵥ = T.

   Equivalently, ¬ψ is UNSAT, so no counterexample valuation exists.

**Insight:** A practical way to test validity is to (1) rewrite → as ¬· ∨ ·, then (2) simplify. Validity means there is no valuation that makes the formula false; solver-style, that’s UNSAT(¬ψ).

### Reduce entailment to UNSAT and extract a countermodel when entailment fails

Let Γ = { p → q, q → r } and let conclusion be φ = p → r. Decide whether Γ ⊨ φ by reducing to UNSAT of (Γ ∧ ¬φ).

1. Write the entailment-to-UNSAT reduction:

   Γ ⊨ φ iff ( (p → q) ∧ (q → r) ∧ ¬(p → r) ) is UNSAT.
2. Rewrite implications using (a → b) ≡ (¬a ∨ b):

   (p → q) ≡ (¬p ∨ q)

   (q → r) ≡ (¬q ∨ r)

   (p → r) ≡ (¬p ∨ r)
3. So the conjunction becomes:

   (¬p ∨ q) ∧ (¬q ∨ r) ∧ ¬(¬p ∨ r).
4. Simplify the negation:

   ¬(¬p ∨ r) ≡ (p ∧ ¬r) by De Morgan’s law.
5. Now we have:

   (¬p ∨ q) ∧ (¬q ∨ r) ∧ (p ∧ ¬r).
6. Use (p ∧ ¬r) as strong constraints.

   From p=true, the clause (¬p ∨ q) forces q=true.

   From ¬r (so r=false), the clause (¬q ∨ r) becomes (¬q ∨ false) which forces ¬q=true, i.e., q=false.
7. We derived q=true and q=false, a contradiction.

   Therefore the conjunction is UNSAT, hence Γ ⊨ (p → r).

**Insight:** Entailment checks become satisfiability checks. If the reduced formula were SAT, the satisfying valuation would be a concrete counterexample where all premises hold but the conclusion fails.

## Key Takeaways

- ✓

  Propositional logic separates **syntax** (well-formed formulas) from **semantics** (truth under a valuation v).
- ✓

  A valuation v assigns each atomic proposition a truth value; semantics extends v to all formulas by structural recursion.
- ✓

  A model of φ is a valuation v with v ⊨ φ; the model set Mod(φ) is the set of all such valuations.
- ✓

  Satisfiable means Mod(φ) ≠ ∅; valid means Mod(φ) is all valuations; unsatisfiable means Mod(φ)=∅.
- ✓

  Material implication satisfies (φ → ψ) ≡ (¬φ ∨ ψ) and is false only when φ is true and ψ is false.
- ✓

  Validity reduces to UNSAT: φ is valid iff ¬φ is unsatisfiable.
- ✓

  Entailment reduces to UNSAT: Γ ⊨ φ iff (Γ ∧ ¬φ) is unsatisfiable; otherwise a satisfying valuation is a countermodel.
- ✓

  Parse trees make formula structure explicit and guide evaluation and rewriting.

## Common Mistakes

- ✗

  Treating implication as causal implication rather than **material implication**; forgetting that if the antecedent is false, φ → ψ evaluates to true.
- ✗

  Confusing satisfiable with valid: a formula can be satisfiable (true in some valuations) but not valid (not true in all).
- ✗

  Mixing syntax and semantics: thinking “φ contains p” implies anything about its truth, without specifying a valuation.
- ✗

  Checking entailment by testing random valuations, instead of constructing (Γ ∧ ¬φ) and searching for a countermodel systematically.

## Practice

easy

Let φ = (p ∨ q) ∧ ¬p. (a) Find one valuation v that satisfies φ. (b) Is φ satisfiable, valid, or unsatisfiable?

**Hint:** To satisfy a conjunction, satisfy both parts. ¬p forces p=F; then make (p ∨ q) true by choosing q.

Show solution

(a) Choose v(p)=F, v(q)=T. Then (p ∨ q)=T and ¬p=T, so φ=T.

(b) φ is satisfiable (we found a model). It is not valid because if p=T and q=F then (p ∨ q)=T but ¬p=F so φ=F. Therefore it is satisfiable but not valid.

medium

Decide whether the formula ψ = (p → q) ∧ p ∧ ¬q is satisfiable. If it is unsatisfiable, explain why in a few steps.

**Hint:** Use the definition of implication: (p → q) is false only when p=T and q=F. Compare with p and ¬q constraints.

Show solution

From p ∧ ¬q we get p=T and q=F. But then (p → q) evaluates to T → F = F. So the conjunction (p → q) ∧ p ∧ ¬q is false under any valuation satisfying p ∧ ¬q, and there is no other way to satisfy the conjunction. Hence ψ is UNSAT.

hard

Entailment practice: Let Γ = { p ∨ q, ¬p } and conclusion be φ = q. Determine whether Γ ⊨ φ by reducing to UNSAT of (Γ ∧ ¬φ).

**Hint:** Build (p ∨ q) ∧ ¬p ∧ ¬q and see if any valuation satisfies it.

Show solution

Reduce:

Γ ⊨ q iff ( (p ∨ q) ∧ ¬p ∧ ¬q ) is UNSAT.

But ¬p ∧ ¬q forces p=F and q=F, which makes (p ∨ q)=F. So the conjunction cannot be satisfied by any valuation. Therefore it is UNSAT and Γ ⊨ q.

## Connections

Next nodes:

- •[Complexity Classes](/tech-tree/complexity-classes/) — SAT as a central NP-complete problem; how reductions formalize “hardness.”
- •[Predicate Logic](/tech-tree/predicate-logic/) — extend propositional logic with predicates and quantifiers while keeping the syntax/semantics discipline.

Related reinforcement:

- •Boolean equivalences and normal forms (CNF/DNF) are the practical bridge from formulas to SAT solver inputs.

Quality: A (4.4/5)

[← back to tree](/tech-tree/)[browse all →](/tech-tree/inventory/)
