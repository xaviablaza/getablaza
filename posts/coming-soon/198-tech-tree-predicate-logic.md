---
title: Predicate Logic
description: First-order logic. Quantifiers, predicates, relations.
date: '2026-07-01'
scheduled: '2027-01-14'
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
inspiration_url: https://templeton.host/tech-tree/predicate-logic/
inspiration_category: tech-tree
---

> Source-copy draft imported from [https://templeton.host/tech-tree/predicate-logic/](https://templeton.host/tech-tree/predicate-logic/). Names, domain references, and local media paths were adapted for Xavi Ablaza / getablaza.com.

[←Back to Tech Tree](/tech-tree/)

[inventory](/tech-tree/inventory/)[coverage](/tech-tree/coverage/)

# Predicate Logic

Formal MethodsDifficulty: ★★★☆☆Depth: 3Unlocks: 0

First-order logic. Quantifiers, predicates, relations.

## Interactive Visualization

⏮◀◀▶▶STEP0.25x1xZOOM

t=0s

## Core Concepts

- -Domain of discourse (the nonempty set over which variables range)
- -Terms (variables, constants, and function applications that denote elements of the domain)
- -Predicates/atomic formulas (n-ary relations; applying a predicate to terms yields an atomic formula)

## Key Symbols & Notation

quantifier symbols: 'forall' and 'exists' (universal and existential quantifiers)

## Essential Relationships

- -Interpretation and satisfaction: an interpretation maps constants/functions/predicates to domain elements/functions/relations; given a variable assignment, terms denote domain elements, atomic formulas are true iff the tuple of denotations is in the predicate relation, and quantifiers range over the domain to determine truth of quantified formulas

## Prerequisites (1)

[Propositional Logic9 atoms](/tech-tree/propositional-logic/)

## Referenced by (1)

Where this concept shows up in the operating-finance and personal-finance graphs.

### From Business (1)

[contract reviewBusiness

Contract clauses are conditional predicate structures ('If Party A fails to deliver within 30 days, then Party B may terminate') - formalizing review rules as quantified predicates is how you specify what each discrete check evaluates](/business/contract-review/)

Advanced Learning Details

### Graph Position

24

Depth Cost

0

Fan-Out (ROI)

0

Bottleneck Score

3

Chain Length

### Cognitive Load

5

Atomic Elements

52

Total Elements

L4

Percentile Level

L3

Atomic Level

### All Concepts (23)

- - Predicates: symbol P of arity n denoting an n-ary property/relation that becomes a formula when applied to terms (e.g., P(x), R(x,y))
- - Terms: syntactic objects that denote elements of the domain - variables, constant symbols, and function applications (e.g., x, c, f(x,y))
- - Function symbols: f, g, … of fixed arity used to build complex terms
- - Constant symbols: nullary function symbols naming specific domain elements (e.g., a, c)
- - Atomic formulas: the simplest formulas formed by applying a predicate symbol to terms (e.g., P(t1,…,tn))
- - Quantifiers: universal quantifier (∀) and existential quantifier (∃) binding variables in formulas
- - Free vs bound variable occurrences: distinction between variable occurrences subject to a quantifier and those not bound
- - Scope of a quantifier: the subformula over which a quantifier binds its variable
- - Sentences (closed formulas) vs open formulas: sentences have no free variables and have a truth value in a structure
- - Substitution of a term for a variable in a formula (and the capture problem when substituting into scopes with binders)
- - α‑equivalence / renaming of bound variables: changing bound variable names without changing meaning
- - Structures / interpretations (models): a domain plus interpretation mapping constants→elements, functions→operations, predicates→relations
- - Variable assignment: mapping from variables to domain elements used together with an interpretation to evaluate open formulas
- - Satisfaction relation: what it means for a structure and (possibly) assignment to satisfy a formula (semantic truth)
- - Truth of a sentence in a model: sentence truth independent of variable assignment
- - Existential witness: in a model, existence is witnessed by at least one domain element that makes the predicate true
- - Universal generality: ∀ means the formula must hold for every domain element
- - Equality as a logical relation (if included): = as a binary predicate with substitutivity properties
- - Quantifier alternation: interleaving of ∀ and ∃ changes expressiveness and meaning
- - Open/closed term distinction: when a term contains variables it is not a closed term
- - Prenex form (concept): moving all quantifiers to the front of a formula (basic normal-form idea)
- - Skolemization (conceptual): eliminating existential quantifiers by introducing Skolem functions (as a transformation technique)
- - Decidability/undecidability facts about FOL (conceptual): validity/satisfiability are not decidable in general (contrast with propositional SAT)

### Teaching Strategy

Self-serve tutorial - low prerequisites, straightforward concepts.

Propositional logic can say “(P ∧ Q) → R”, but it can’t say “for every user, if they reset their password then they can log in” without inventing a separate proposition for each user. Predicate logic (first-order logic) is the upgrade that lets you talk about objects, their properties, and relationships—at scale—using variables and quantifiers.

TL;DR:

Predicate logic extends propositional logic with (1) a domain of discourse (objects), (2) terms that name objects (variables/constants/functions), (3) predicates/relations that make statements about objects, and (4) quantifiers ∀ and ∃ that range over the domain. You build formulas like ∀x (Human(x) → Mortal(x)) and reason by translating English carefully, tracking scope, and using sound inference patterns (e.g., universal instantiation, existential generalization) while avoiding common quantifier traps.

## What Is Predicate Logic?

### Why we need more than propositional logic

Propositional logic treats whole statements as indivisible atoms: **P**, **Q**, **R**. That’s great for reasoning about fixed, named facts, but it doesn’t let you *open up* a statement and talk about its internal structure.

Consider the English statement:

- •“Every student in this class submitted an assignment.”

In propositional logic, you’d need one proposition per student (“Alice submitted”, “Bob submitted”, …) and then conjoin them all. That’s not scalable and it misses the structure that these are all instances of the same pattern.

Predicate logic (often called **first-order logic**, FOL) solves this by introducing:

1. 1)A **domain of discourse**: a nonempty set of objects we’re talking about.
2. 2)**Variables** that range over that domain.
3. 3)**Predicates** (relations) that say something about objects.
4. 4)**Quantifiers** to express “for all” (∀) and “there exists” (∃).

This is the language used by mathematics (“∀ε > 0 ∃N …”), by program specification (“∀i: 0 ≤ i < n → a[i] ≥ 0”), and by many formal methods tools.

### The basic ingredients

Predicate logic is built from a small set of syntactic building blocks.

#### Domain of discourse

The **domain** (also called the universe) is the set over which variables range. It must be **nonempty**.

Examples:

- •Domain = all integers ℤ
- •Domain = all people in a database
- •Domain = all nodes in a graph

The same formula can mean different things under different domains.

#### Terms (naming objects)

A **term** denotes an element of the domain.

Terms come from:

- •**Variables**: x, y, z (range over the domain)
- •**Constants**: a, b, c (fixed named elements of the domain)
- •**Function symbols**: f(·), g(·,·) applied to terms

Examples of terms:

- •x
- •alice
- •parentOf(x)
- •add(x, 1)

Intuition: a term is like an expression that evaluates to “an object”.

#### Predicates / atomic formulas (stating facts)

A **predicate** is an n-ary relation symbol, like:

- •Human(·) (unary predicate)
- •Likes(·,·) (binary predicate)
- •LessThan(·,·)

When you apply a predicate to terms, you get an **atomic formula**:

- •Human(x)
- •Likes(alice, bob)
- •LessThan(x, add(y, 1))

An atomic formula evaluates to True/False once you know what the symbols mean in your domain.

### Building complex formulas

From atomic formulas, you build larger formulas using the same connectives as propositional logic:

- •¬ (not)
- •∧ (and)
- •∨ (or)
- •→ (implies)
- •↔ (iff)

And you add quantifiers:

- •∀x φ (for all x, φ)
- •∃x φ (there exists an x such that φ)

Crucially, **quantifiers bind variables** (like how parentheses bind subexpressions). The part of the formula a quantifier controls is its **scope**.

### Free vs bound variables

A variable occurrence is:

- •**Bound** if it is under a quantifier for that variable.
- •**Free** if it is not.

Example:

- •∀x (Human(x) → Mortal(x))
- •all occurrences of x are bound.
- •Human(x) → Mortal(x)
- •x is free.

A formula with no free variables is called a **sentence**. Sentences are what we typically evaluate as True/False in a model.

### A quick semantics snapshot (what makes formulas “true”)

To interpret a predicate-logic language, you need:

- •A domain D (nonempty)
- •An interpretation of each constant as an element of D
- •An interpretation of each function symbol as a function on D
- •An interpretation of each predicate as a relation on D

Then:

- •∀x φ is True iff φ is True for **every** assignment of x ∈ D
- •∃x φ is True iff φ is True for **some** assignment of x ∈ D

This “assignment of variables” idea is why quantifiers are powerful: they quantify over *all objects* in the domain, not just those you named.

### Table: how predicate logic extends propositional logic

| Feature | Propositional Logic | Predicate Logic (FOL) |
| --- | --- | --- |
| Atomic units | Propositions P, Q, R | Predicates applied to terms, e.g., P(x), R(x,y) |
| Can talk about objects? | No | Yes (domain + terms) |
| Can express “all / some”? | Only by enumerating | Yes via ∀ and ∃ |
| Typical use | Circuit reasoning, SAT | Math, specs, verification, databases |

Predicate logic keeps propositional logic’s connectives, but gives you a language to express *structure* and *patterns* over a domain.

## Core Mechanic 1: Quantifiers and Scope

### Why quantifiers matter

Most statements we care about in math and software are inherently quantified:

- •“Every array index is in bounds.”
- •“There exists an input that triggers an error.”
- •“For every request, there exists a response.”

Quantifiers let you express these patterns directly. But they also introduce subtlety: **the order and scope of quantifiers can change meaning dramatically**.

### Universal quantifier ∀ (for all)

The formula:

- •∀x φ(x)

means: “for every x in the domain, φ(x) is true.”

Example:

- •∀x (Student(x) → HasID(x))

This does **not** claim that every object is a student. It says: if an object is a student, then it has an ID.

A common pattern:

- •∀x (A(x) → B(x))

reads as: “All A’s are B’s.”

### Existential quantifier ∃ (there exists)

The formula:

- •∃x φ(x)

means: “there exists some x in the domain such that φ(x) is true.”

Example:

- •∃x (Student(x) ∧ Late(x))

This asserts at least one student is late.

### Scope: where a quantifier applies

Scope is usually controlled by parentheses.

Compare:

1) ∀x (P(x) → Q(x))

2) (∀x P(x)) → Q(x)

These are not the same.

- •In (1), x is local to the implication.
- •In (2), the antecedent says “P(x) holds for all x”, but Q(x) has x **free** (so (2) isn’t even a sentence unless Q doesn’t mention x). Many mistakes come from losing track of scope.

### Quantifier order (∃∀ vs ∀∃)

This is one of the biggest conceptual leaps from propositional logic.

Consider:

- •∀x ∃y Loves(x, y)
- •∃y ∀x Loves(x, y)

Assume the domain is people.

1) ∀x ∃y Loves(x, y)

- •“Everyone loves someone.”
- •Each person can have their own y.

2) ∃y ∀x Loves(x, y)

- •“There exists someone whom everyone loves.”
- •One special y loved by all.

These are **very different**. The second is much stronger.

### A careful translation pipeline (English → logic)

When translating, go slowly:

1. 1)**Choose the domain** explicitly.
2. 2)**Define predicates** with clear meaning.
3. 3)**Identify quantifier words**: “every”, “all”, “any” → ∀; “some”, “there exists” → ∃.
4. 4)**Attach conditions** using → or ∧.

Example: “Every user who reset their password can log in.”

- •Domain: users
- •Predicates:
- •Reset(x): “x reset their password”
- •CanLogin(x): “x can log in”

Translation:

- •∀x (Reset(x) → CanLogin(x))

Notice why it’s → and not ∧: we’re not claiming everyone reset their password.

### Negating quantified statements (De Morgan’s for quantifiers)

Negation interacts with quantifiers in a structured way:

- •¬∀x φ ≡ ∃x ¬φ
- •¬∃x φ ≡ ∀x ¬φ

Intuition:

- •“Not everyone passed” means “someone did not pass.”
- •“No one passed” means “everyone did not pass.”

Do the algebra carefully. For example:

¬(∀x (P(x) → Q(x)))

Step-by-step:

1. 1)¬∀x ψ(x) ≡ ∃x ¬ψ(x)

where ψ(x) = (P(x) → Q(x))

So:

2. 2)¬(∀x (P(x) → Q(x)))

≡ ∃x ¬(P(x) → Q(x))

Now expand implication:

3. 3)(P → Q) ≡ (¬P ∨ Q)

so ¬(P → Q) ≡ ¬(¬P ∨ Q)

Apply De Morgan:

4. 4)¬(¬P ∨ Q) ≡ (P ∧ ¬Q)

Final:

5. 5)¬(∀x (P(x) → Q(x)))

≡ ∃x (P(x) ∧ ¬Q(x))

Reading: “It is not true that all P’s are Q’s” means “There exists a P that is not Q.”

### Table: common English patterns

| English | Typical logic form |
| --- | --- |
| “All A are B” | ∀x (A(x) → B(x)) |
| “Some A are B” | ∃x (A(x) ∧ B(x)) |
| “No A are B” | ∀x (A(x) → ¬B(x)) (equiv. ¬∃x (A(x) ∧ B(x))) |
| “Not all A are B” | ∃x (A(x) ∧ ¬B(x)) |

Quantifiers are simple symbols with big consequences. Most real errors are scope/order errors, not symbol errors.

## Core Mechanic 2: Predicates, Relations, and Terms (and why functions matter)

### Why terms and predicates are separate ideas

Predicate logic splits the world into two roles:

- •**Terms** denote objects (elements of the domain).
- •**Formulas** denote truth values (True/False).

Predicates are what *turn* objects into truth claims.

This separation is why you can’t, for example, treat a predicate like an object unless your logic explicitly supports that (standard first-order logic does not—this is a doorway to higher-order logic).

### Arity: how many inputs a symbol takes

Predicates and functions have an **arity**:

- •Unary predicate: P(x)
- •Binary predicate: R(x, y)
- •Ternary predicate: T(x, y, z)

Similarly for functions:

- •Unary function: f(x)
- •Binary function: g(x, y)

Arity matters because it encodes what kind of relationship you’re expressing.

### Relations as sets (a useful mental model)

If your domain is D, then:

- •A unary predicate P(·) corresponds to a subset P ⊂ D.
- •A binary predicate R(·,·) corresponds to a set of pairs R ⊂ D × D.
- •An n-ary predicate corresponds to a set R ⊂ Dⁿ.

So the atomic formula R(a, b) is true exactly when (a, b) ∈ R.

This viewpoint connects predicate logic to:

- •database tables (relations)
- •graph edges (binary relations)
- •constraints in CSP/SAT modulo theories

### Equality

Most first-order settings include equality “=”.

Equality lets you state things like:

- •∃x (x = alice)
- •∀x (f(x) = x)

Be careful: equality is a logical symbol with its own meaning (identity), not just another predicate you can interpret arbitrarily (in standard FOL with equality).

### Function symbols (building more complex terms)

Function symbols let you talk about structured objects *without* introducing extra quantifiers.

Example domain: integers.

- •succ(x) means x + 1

Then you can write:

- •∀x (LessThan(x, succ(x)))

Without functions, you’d need a relation Plus(x, 1, y) to express y = x + 1, and then quantify y.

#### Functions vs relations: two equivalent styles (often)

You can encode a function f(x) using a relation F(x, y) meaning “y = f(x)” plus axioms:

- •∀x ∃y F(x, y) (totality)
- •∀x ∀y₁ ∀y₂ ((F(x, y₁) ∧ F(x, y₂)) → y₁ = y₂) (uniqueness)

But using function symbols is typically cleaner.

### Binding and substitution (the safe way)

A fundamental operation is substituting a term into a formula.

If φ(x) is a formula with x free, and t is a term, then φ(t) is the result of substituting t for x.

Example:

- •φ(x) := Human(x) → Mortal(x)
- •t := socrates
- •φ(t) = Human(socrates) → Mortal(socrates)

But you must avoid **variable capture**: substituting a term containing a variable that becomes accidentally bound.

Example of what can go wrong:

- •φ(x) := ∀y Loves(x, y)
- •substitute t := y

Naively you get ∀y Loves(y, y), where the y inside t became bound by ∀y.

The safe approach is:

- •rename bound variables first (α-renaming)
- •then substitute

So you’d rename:

- •∀y Loves(x, y) ≡ ∀z Loves(x, z)

Then substitute x := y:

- •∀z Loves(y, z)

### Quantifiers as “big AND / big OR” (finite intuition)

If the domain is finite D = {d₁, …, dₙ}, then:

- •∀x φ(x) ≡ φ(d₁) ∧ φ(d₂) ∧ … ∧ φ(dₙ)
- •∃x φ(x) ≡ φ(d₁) ∨ φ(d₂) ∨ … ∨ φ(dₙ)

This is not how we compute it in general (domains can be infinite), but it’s an excellent intuition-builder.

### Summary of the “typing” discipline

Keep these categories separate:

- •Terms: x, alice, f(x), g(a, b)
- •Atomic formulas: P(x), R(f(x), a)
- •Formulas: build from atomic formulas using ¬, ∧, ∨, →, ↔, plus ∀, ∃

If you can reliably tell “object expressions” from “truth expressions”, you’ll write correct formulas much faster.

## Application/Connection: Using Predicate Logic in CS and Formal Methods

### Why this matters in formal methods

Formal methods is about specifying and proving properties of systems. Predicate logic is the backbone for:

- •**Specifications**: describing what a program *should* do.
- •**Verification conditions**: logical formulas whose validity implies correctness.
- •**Model checking and theorem proving interfaces**: even when tools go beyond FOL, FOL is the starting point.

Predicate logic is the first language where you can naturally express invariants like:

- •“All elements are nonnegative.”
- •∀i (0 ≤ i ∧ i < n → a[i] ≥ 0)

or existence claims like:

- •“There exists a counterexample input.”
- •∃x BadInput(x)

### Typical CS domains and predicate meanings

Predicate logic is flexible because you choose the domain and interpretation.

Examples:

1) **Data structures**

- •Domain: nodes in a linked list
- •Predicates:
- •Next(x, y): “y is the next node after x”
- •Reachable(x, y): “y is reachable from x”

2) **Security policies**

- •Domain: principals/users
- •Predicates:
- •CanRead(u, f)
- •Owns(u, f)
- •Admin(u)

Then a policy might be:

- •∀u ∀f (CanRead(u, f) → (Owns(u, f) ∨ Admin(u)))

3) **Databases (relational model)**

A table like Enrolled(student, course) is literally a binary predicate Enrolled(·,·).

Queries often correspond to existential formulas.

Example: “Find students enrolled in CS101” corresponds to:

- •∃c (c = CS101 ∧ Enrolled(s, c))

### Proof patterns you’ll reuse

Even if you don’t do full theorem-prover work yet, you should recognize the standard moves.

#### Universal instantiation (UI)

From ∀x φ(x), you may conclude φ(t) for any term t.

Example:

1. 1)∀x (Human(x) → Mortal(x))
2. 2)Human(socrates)

UI on (1) with t = socrates gives:

3. 3)Human(socrates) → Mortal(socrates)

Then by modus ponens with (2):

4. 4)Mortal(socrates)

#### Existential instantiation (EI) (with care)

From ∃x φ(x), you can introduce a fresh symbol k such that φ(k) holds, **but k must be new** (it can’t carry hidden assumptions).

This is subtle: you don’t get to pick a specific known constant unless you can prove it works.

#### Existential generalization (EG)

From φ(t), infer ∃x φ(x) (replace t by a variable).

Example:

- •Human(socrates) implies ∃x Human(x)

#### Universal generalization (UG) (with care)

From φ(x) for an arbitrary x (with no special assumptions about x), infer ∀x φ(x).

This “arbitrary” requirement is exactly where many informal proofs go wrong.

### Satisfiability, validity, and models (a quick bridge from propositional logic)

You already know satisfiability in propositional logic. In FOL:

- •A **model** is a domain plus interpretations making formulas true.
- •A sentence is **satisfiable** if it’s true in at least one model.
- •A sentence is **valid** if it’s true in all models.

Example (valid):

- •∀x P(x) → ∃x P(x)

This is valid because if P holds for all x in a nonempty domain, then certainly there exists an x where P holds.

Non-valid (not always true):

- •∃x P(x) → ∀x P(x)

True in some models, false in others.

### Why tooling often restricts or extends FOL

Pure FOL is expressive, but automated reasoning is harder than for propositional logic.

- •SAT is decidable and heavily optimized.
- •FOL validity is (in general) **undecidable**.

So real tools often:

- •restrict to decidable fragments (e.g., certain theories), or
- •use semi-decision procedures (can find proofs/countermodels sometimes), or
- •combine SAT with theories (SMT: satisfiability modulo theories), where formulas often look like FOL with arithmetic, arrays, etc.

The key takeaway: learning predicate logic is the gateway to reading specifications, understanding solver input languages, and following proofs about programs.

## Worked Examples (3)

### Translate English to predicate logic (and see why → matters)

Domain: all animals in a shelter.

Predicates:

- •Dog(x): x is a dog
- •Vaccinated(x): x is vaccinated
- •Adoptable(x): x is adoptable

Translate:

1) “Every dog is vaccinated.”

2) “Some dog is adoptable.”

3) “Not every dog is adoptable.”

1. 1) “Every dog is vaccinated.”

   We want: for all x, if x is a dog then x is vaccinated.

   ∀x (Dog(x) → Vaccinated(x))

   2) “Some dog is adoptable.”

   We want: there exists an x that is a dog and is adoptable.

   ∃x (Dog(x) ∧ Adoptable(x))

   3) “Not every dog is adoptable.”

   Start from “Every dog is adoptable”: ∀x (Dog(x) → Adoptable(x))

   Negate it:

   ¬∀x (Dog(x) → Adoptable(x))
2. Now push negation inward using ¬∀x φ ≡ ∃x ¬φ.

   Let φ(x) = (Dog(x) → Adoptable(x)).

   ¬∀x φ(x) ≡ ∃x ¬φ(x)

   So:

   ¬∀x (Dog(x) → Adoptable(x))

   ≡ ∃x ¬(Dog(x) → Adoptable(x))
3. Eliminate implication:

   (Dog(x) → Adoptable(x)) ≡ (¬Dog(x) ∨ Adoptable(x))

   So:

   ¬(Dog(x) → Adoptable(x))

   ≡ ¬(¬Dog(x) ∨ Adoptable(x))

   ≡ Dog(x) ∧ ¬Adoptable(x)

   Final:

   ∃x (Dog(x) ∧ ¬Adoptable(x))

**Insight:** “All dogs are adoptable” is an implication because it’s conditional on being a dog. Negating a universal statement almost always turns into an existential counterexample: “there exists a dog that is not adoptable.”

### Quantifier order changes meaning (everyone has a password vs one shared password)

Domain: users.

Predicate Knows(u, p): user u knows password p.

We want to compare two statements:

A) ∀u ∃p Knows(u, p)

B) ∃p ∀u Knows(u, p)

1. Statement A:

   ∀u ∃p Knows(u, p)

   Read carefully: for each user u, there exists some password p such that u knows p.

   Different users may have different passwords.

   This is typically true in a realistic system (each user knows at least one password).
2. Statement B:

   ∃p ∀u Knows(u, p)

   Read carefully: there exists a single password p such that every user knows p.

   This is far stronger: it implies a shared universal password.
3. Show non-equivalence by countermodel thinking.

   Suppose there are two users: alice and bob.

   Suppose alice knows password "a1" and bob knows password "b1".

   Then:

   - •A is True (alice has a password she knows; bob has a password he knows).
   - •B is False (there is no single password known by both).

**Insight:** Mentally underline which variables must be the same across all choices. In ∃p ∀u, the password is chosen once and reused for every user; in ∀u ∃p, each user gets their own choice.

### A small proof using universal instantiation and modus ponens

Given:

1) ∀x (Student(x) → HasEmail(x))

2) Student(alex)

Prove: HasEmail(alex)

1. Start with the universal statement:

   1) ∀x (Student(x) → HasEmail(x))
2. Apply universal instantiation with t = alex:

   From ∀x φ(x), infer φ(alex).

   So we get:

   3) Student(alex) → HasEmail(alex)
3. Use the fact:

   2) Student(alex)
4. Apply modus ponens to (3) and (2):

   If Student(alex) → HasEmail(alex) and Student(alex), then HasEmail(alex).

   Therefore:

   4) HasEmail(alex)

**Insight:** Universal facts are like templates. Instantiation turns the template into a concrete implication you can fire with propositional reasoning.

## Key Takeaways

- ✓

  Predicate logic = propositional logic + a domain of objects + terms + predicates + quantifiers ∀ and ∃.
- ✓

  Terms denote objects; formulas denote truth. Predicates turn terms into atomic formulas.
- ✓

  Scope and quantifier order matter: ∀x ∃y R(x,y) is generally not equivalent to ∃y ∀x R(x,y).
- ✓

  Translate “All A are B” as ∀x (A(x) → B(x)), not ∀x (A(x) ∧ B(x)).
- ✓

  Negating quantifiers flips them: ¬∀x φ ≡ ∃x ¬φ and ¬∃x φ ≡ ∀x ¬φ.
- ✓

  A formula with no free variables is a sentence; sentences are what become True/False in a model.
- ✓

  Core inference patterns include universal instantiation, existential generalization, and careful existential instantiation with fresh witnesses.

## Common Mistakes

- ✗

  Using ∧ instead of → when translating statements like “All A are B”, accidentally asserting everything is A.
- ✗

  Losing track of scope/parentheses, producing formulas with free variables or unintended bindings.
- ✗

  Assuming ∀x ∃y and ∃y ∀x mean the same thing; swapping quantifiers without checking meaning.
- ✗

  Negating quantified statements incorrectly (e.g., thinking ¬∀x P(x) means ∀x ¬P(x) instead of ∃x ¬P(x)).

## Practice

easy

Translate into predicate logic. Domain: all integers ℤ. Predicates/relations: Even(x), Odd(x), Less(x,y). Use arithmetic terms like x+1 if you want.

A) “Every even integer is not odd.”

B) “There exists an integer that is less than every integer.”

**Hint:** A uses implication. B is about a single special integer that compares to all others; watch quantifier order.

Show solution

A) ∀x (Even(x) → ¬Odd(x))

B) ∃x ∀y Less(x, y)

medium

Negate the sentence and simplify:

∀x (P(x) → ∃y (Q(y) ∧ R(x, y)))

**Hint:** Push ¬ inward step by step: ¬∀ → ∃¬, ¬∃ → ∀¬, and ¬(A → B) ≡ A ∧ ¬B. Then use De Morgan on ¬(Q ∧ R).

Show solution

Start:

¬∀x (P(x) → ∃y (Q(y) ∧ R(x, y)))

≡ ∃x ¬(P(x) → ∃y (Q(y) ∧ R(x, y)))

≡ ∃x (P(x) ∧ ¬∃y (Q(y) ∧ R(x, y)))

≡ ∃x (P(x) ∧ ∀y ¬(Q(y) ∧ R(x, y)))

≡ ∃x (P(x) ∧ ∀y (¬Q(y) ∨ ¬R(x, y)))

hard

Are these two formulas equivalent? If not, give a counterexample model (a small finite domain and an interpretation of R).

1) ∀x ∃y R(x, y)

2) ∃y ∀x R(x, y)

**Hint:** Try a domain with two elements {a,b}. Make R relate each element to itself only.

Show solution

They are not equivalent.

Counterexample:

- •Domain D = {a, b}
- •Interpret R as {(a,a), (b,b)}.

Then:

1) ∀x ∃y R(x,y) is True (for x=a choose y=a; for x=b choose y=b).

2) ∃y ∀x R(x,y) is False (no single y works for both x=a and x=b).

## Connections

Next nodes you’re ready for:

- •[Proof Rules for First-Order Logic](/tech-tree/fol-proof-rules/)
- •[Skolemization and Prenex Normal Form](/tech-tree/skolemization-prenex/)
- •[Unification and Resolution](/tech-tree/unification-resolution/)
- •[SMT Basics (SAT Modulo Theories)](/tech-tree/smt-basics/)

Background refreshers:

- •[Propositional Logic](/tech-tree/propositional-logic/)
- •[Sets and Relations](/tech-tree/sets-relations/)

Quality: A (4.2/5)

[← back to tree](/tech-tree/)[browse all →](/tech-tree/inventory/)
