---
title: Boolean Logic
description: AND, OR, NOT operations. Truth tables and logical equivalence.
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
permalink: /tech-tree/logic-basic/
---

[←Back to Tech Tree](/tech-tree/)

[inventory](/tech-tree/inventory/)[coverage](/tech-tree/coverage/)

# Boolean Logic

Discrete MathDifficulty: ★☆☆☆☆Depth: 0Unlocks: 23

AND, OR, NOT operations. Truth tables and logical equivalence.

## Interactive Visualization

⏮◀◀▶▶STEP0.25x1xZOOM

t=0s

## Core Concepts

- -Binary truth values: TRUE and FALSE
- -Basic logical operations: NOT, AND, OR (each maps input truth values to an output truth value)

## Key Symbols & Notation

'!' for NOT; '&&' for AND; '||' for OR

## Essential Relationships

- -Truth table: a complete mapping from every combination of input truth values to the operation's output
- -Logical equivalence: two expressions are equivalent iff they have identical truth tables for all input combinations

## Unlocks (2)

[Proof Techniqueslvl 2](/tech-tree/proof-techniques/)[Propositional Logiclvl 3](/tech-tree/propositional-logic/)

Advanced Learning Details

### Graph Position

5

Depth Cost

23

Fan-Out (ROI)

13

Bottleneck Score

0

Chain Length

### Cognitive Load

5

Atomic Elements

40

Total Elements

L3

Percentile Level

L3

Atomic Level

### All Concepts (12)

- - Proposition: a declarative statement that has a truth value (True or False)
- - Boolean value: the two possible truth values (True, False)
- - Conjunction (AND): a binary operation that combines two propositions
- - Disjunction (OR): a binary operation that combines two propositions (inclusive OR)
- - Negation (NOT): a unary operation that flips a proposition's truth value
- - Compound proposition: an expression built from propositions using AND/OR/NOT
- - Truth table: a systematic tabular representation of an expression's output for every combination of input truth values
- - Logical equivalence: the notion that two propositions have identical truth values for every possible assignment
- - Tautology: a proposition that is True for every input assignment
- - Contradiction (unsatisfiable): a proposition that is False for every input assignment
- - Satisfiability: the property of a proposition having at least one input assignment that makes it True
- - Operator precedence for Boolean operators (typical convention: NOT before AND before OR)

### Teaching Strategy

Self-serve tutorial - low prerequisites, straightforward concepts.

Every time a program checks a password, a search engine filters results, or a circuit decides whether to light an LED, it’s doing the same thing: combining TRUE/FALSE facts with a small set of rules. Boolean logic is that rulebook.

TL;DR:

Boolean logic works with two truth values (TRUE, FALSE) and three core operations: NOT (!), AND (&&), OR (||). Truth tables list outputs for all possible inputs. Logical equivalence means two expressions always produce the same truth value, so you can simplify or rewrite conditions safely.

## What Is Boolean Logic?

Boolean logic is a way to compute with truth values.

Instead of numbers like 7 or 3.14, the “data type” here is:

- •TRUE
- •FALSE

A *Boolean expression* is anything that evaluates to TRUE or FALSE.

Why care? Because many real questions are naturally yes/no:

- •“Is the user logged in?”
- •“Is the temperature above a threshold?”
- •“Is this number divisible by 2?”

In computing, these yes/no questions drive control flow:

- •`if` statements
- •`while` loops
- •filtering (keep items that satisfy a condition)

In math, the same ideas show up in proofs:

- •You assume something is TRUE and derive consequences.
- •You show something cannot be TRUE (so it must be FALSE).

### Propositions: the things that can be TRUE/FALSE

A *proposition* is a statement that is definitively TRUE or FALSE.

Examples:

- •“2 is even.” (TRUE)
- •“5 < 3.” (FALSE)
- •“This program will terminate.” (depends, but still intended to be either TRUE or FALSE)

Non-examples (not propositions):

- •“Close the door.” (command)
- •“x is greater than 3.” (depends on x; becomes a proposition only after x is fixed)

### From everyday language to logic

Natural language has words like “and”, “or”, “not”, “if”, “only if”, “unless”. Boolean logic begins with the simplest three:

- •NOT
- •AND
- •OR

We’ll use the programming-style symbols specified in this node:

- •`!` for NOT
- •`&&` for AND
- •`||` for OR

You should read them as:

- •`!P` : “not P”
- •`P && Q` : “P and Q”
- •`P || Q` : “P or Q”

### The key idea: an operator is a function on truth values

Each operator takes input truth values and produces an output truth value.

- •NOT takes 1 input (unary operator)
- •AND takes 2 inputs (binary operator)
- •OR takes 2 inputs (binary operator)

A *truth table* is how we define these operators precisely: list all possible inputs, and specify the output for each case.

That’s the foundation: Boolean logic is “functions on {TRUE, FALSE}”.

## Core Mechanic 1: Truth Tables for !, &&, ||

Truth tables matter because they remove ambiguity.

In everyday speech, “or” can be confusing:

- •“You can have soup or salad.” (sometimes means one but not both)
- •“It’s raining or snowing.” (could be one or both)

In Boolean logic, `||` is the *inclusive OR*: it is TRUE when at least one input is TRUE.

We’ll use these conventions:

- •T = TRUE
- •F = FALSE

### NOT (!)

NOT flips the truth value.

| P | !P |
| --- | --- |
| T | F |
| F | T |

Interpretation: if P is TRUE, then “not P” is FALSE, and vice versa.

### AND (&&)

AND is TRUE only when *both* inputs are TRUE.

| P | Q | P && Q |
| --- | --- | --- |
| T | T | T |
| T | F | F |
| F | T | F |
| F | F | F |

Interpretation: `P && Q` means “P and Q are both the case.”

### OR (||)

OR is TRUE when *at least one* input is TRUE.

| P | Q | P |  | Q |
| --- | --- | --- | --- | --- |
| T | T | T |
| T | F | T |
| F | T | T |
| F | F | F |

Interpretation: `P || Q` means “P is the case, or Q is the case, or both.”

### Building larger truth tables (slowly and mechanically)

Real conditions are usually built from smaller ones:

- •`(!P) && Q`
- •`P && (Q || R)`

A good habit: compute *intermediate columns*.

For example, to evaluate `(!P) && Q`, make a column for `!P`, then a column for `(!P) && Q`.

| P | Q | !P | (!P) && Q |
| --- | --- | --- | --- |
| T | T | F | F |
| T | F | F | F |
| F | T | T | T |
| F | F | T | F |

This is “showing your work” in logic.

### Precedence and parentheses (so we don’t accidentally mean something else)

In most programming languages, `!` binds tighter than `&&`, which binds tighter than `||`.

So typically:

- •`!P && Q || R` is read as `((!P) && Q) || R`

But relying on precedence can be risky for learners and teammates.

Use parentheses when learning:

- •Write `((!P) && Q) || R` if that’s what you mean.

### Quick comparison table

Here’s a compact way to remember behavior:

| Operator | Symbol | When result is TRUE | Common English |
| --- | --- | --- | --- |
| NOT | `!` | when input is FALSE | “not” |
| AND | `&&` | when both are TRUE | “and” |
| OR | ` |  | ` | when at least one is TRUE | “or (inclusive)” |

Truth tables are the “ground truth” for all later topics: proofs, algebraic simplification, satisfiability, and circuit design.

## Core Mechanic 2: Logical Equivalence and Rewriting

Once you know what an expression *means* (via truth tables), the next power is to recognize when two different-looking expressions always give the same result.

That idea is called **logical equivalence**.

### Definition: logical equivalence

Two Boolean expressions A and B are *logically equivalent* if they evaluate to the same truth value for **every** assignment of truth values to their variables.

We write:

- •A ≡ B

Why this matters:

- •**Simplification:** make conditions shorter and clearer.
- •**Optimization:** fewer checks in code or fewer gates in circuits.
- •**Proof:** replace an expression with an equivalent one to make reasoning easier.

### How to prove equivalence (at this level)

At Difficulty 1, the main tool is: **compare truth tables**.

Process:

1. 1)List all combinations of input variables.
2. 2)Compute A and B for each row.
3. 3)If the output columns match exactly, then A ≡ B.

### The most important equivalences to know early

These are the “algebra rules” of Boolean logic. You don’t need to memorize all of them immediately, but you should get comfortable using them.

#### 1) Double negation

Negating twice returns the original:

- •!!P ≡ P

Truth table check:

| P | !P | !!P |
| --- | --- | --- |
| T | F | T |
| F | T | F |

The last column equals P.

#### 2) De Morgan’s Laws

These explain how NOT interacts with AND/OR.

- •!(P && Q) ≡ (!P) || (!Q)
- •!(P || Q) ≡ (!P) && (!Q)

Intuition:

- •“Not (P and Q)” means “at least one of them is not true.”
- •“Not (P or Q)” means “neither is true.”

Truth table for the first law:

| P | Q | P && Q | !(P && Q) | !P | !Q | (!P) |  | (!Q) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| T | T | T | F | F | F | F |
| T | F | F | T | F | T | T |
| F | T | F | T | T | F | T |
| F | F | F | T | T | T | T |

The columns `!(P && Q)` and `(!P) || (!Q)` match row-by-row, so they’re equivalent.

#### 3) Identity and domination (helpful for simplification)

Think of TRUE and FALSE as special “absorbing” values.

- •P && TRUE ≡ P
- •P || FALSE ≡ P
- •P && FALSE ≡ FALSE
- •P || TRUE ≡ TRUE

You can confirm each via a 2-row truth table.

#### 4) Idempotence (repeating doesn’t change anything)

- •P && P ≡ P
- •P || P ≡ P

#### 5) Commutativity and associativity (reordering and regrouping)

- •P && Q ≡ Q && P
- •P || Q ≡ Q || P
- •(P && Q) && R ≡ P && (Q && R)
- •(P || Q) || R ≡ P || (Q || R)

These are why we can write `P && Q && R` without worrying about parentheses (conceptually), though you should still be careful in code with mixed operators.

### A note on “exclusive or”

People sometimes mean “one or the other but not both.” That operator is XOR.

This node does not include XOR, but it’s worth knowing that plain `||` is inclusive.

If you ever need XOR using only `!`, `&&`, `||`, one common form is:

- •(P || Q) && !(P && Q)

You can verify it with a truth table when you’re ready.

### Showing work: rewriting with laws

Equivalence laws let you rewrite step-by-step.

Example goal: simplify `!(P || Q) || Q`.

We can rewrite using De Morgan:

- •!(P || Q) || Q
- •≡ ((!P) && (!Q)) || Q

From here, a full simplification would use additional distributive/absorption laws (often taught next). For now, the key skill is: you can *legally replace* `!(P || Q)` with `(!P) && (!Q)` because they are equivalent.

At this stage, truth tables are your safety net: if you’re unsure, compute and compare.

## Application/Connection: Logic in Code, Proofs, and Circuits

Boolean logic is a shared language between programming, math proofs, and hardware.

### 1) Programming: conditions in `if` and `while`

A program constantly evaluates Boolean expressions:

- •`if (isAdmin && !isBanned) { ... }`
- •`while (hasWork || retryCount < 3) { ... }`

Truth tables help you reason about edge cases.

Example: Suppose

- •P = “user is logged in”
- •Q = “user has premium access”

Then:

- •`P && Q` means “logged in AND premium”
- •`P || Q` means “logged in OR premium (or both)”

A common design question is: do you want to allow premium users who are not logged in? If not, `P || Q` is wrong.

### 2) Proof techniques (what this node unlocks)

In proofs, you often transform statements using logic.

- •In a **direct proof**, you start from assumptions (TRUE statements) and chain implications.
- •In **proof by contradiction**, you assume the opposite of what you want, then derive FALSE.

Even though implication (→) isn’t covered in this node, the mindset is already here:

- •Build complex statements from simpler ones.
- •Use equivalences to rewrite.
- •Use contradictions like “P && !P” (can never be TRUE).

### 3) Circuits: logic gates

Digital circuits represent TRUE/FALSE as voltage levels. Gates compute the same operations:

| Logic | Circuit gate | Meaning |
| --- | --- | --- |
| `!` | NOT gate | flips signal |
| `&&` | AND gate | both inputs high ⇒ output high |
| ` |  | ` | OR gate | any input high ⇒ output high |

This is why truth tables are also used in hardware design: they specify exactly what a gate or circuit should do.

### 4) Why equivalence matters in applications

If two expressions are equivalent, you can swap them without changing behavior.

- •In code: rewrite to something clearer.
- •In circuits: reduce gate count.
- •In proofs: rewrite a statement into a form that matches a theorem you can apply.

Example: `!(P && Q)` is sometimes easier to implement or reason about as `(!P) || (!Q)` (De Morgan), depending on what signals are available.

### A practical “debugging” strategy

When a Boolean condition seems wrong:

1. 1)Name subconditions (P, Q, R).
2. 2)Write the intended behavior in words.
3. 3)Create a truth table for the expression.
4. 4)Compare the table to what you intended.

This is slow at first, but it’s extremely reliable—and it scales to more advanced logic later.

## Worked Examples (3)

### Evaluate a Boolean expression with a truth table

Let P and Q be Boolean variables. Build a truth table for the expression E = (!P) || (P && Q).

1. List all possible (P, Q) pairs:

   - •(T, T), (T, F), (F, T), (F, F).
2. Create intermediate columns for !P and (P && Q).
3. Compute row by row:

   | P | Q | !P | P && Q | E = (!P) |  | (P && Q) |
   | --- | --- | --- | --- | --- | --- | --- |
   | T | T | F | T | F |  | T = T |
   | T | F | F | F | F |  | F = F |
   | F | T | T | F | T |  | F = T |
   | F | F | T | F | T |  | F = T |
4. Read the result column: E is FALSE only when P = T and Q = F. In all other cases E is TRUE.

**Insight:** Intermediate columns prevent mistakes. You can see exactly which part of the condition “makes it TRUE” on each row.

### Verify De Morgan’s Law with a truth table

Show that !(P || Q) ≡ (!P) && (!Q) by comparing their truth tables.

1. List all possible (P, Q) pairs:

   - •(T, T), (T, F), (F, T), (F, F).
2. Compute the left-hand side L = !(P || Q):

   First compute (P || Q), then negate.
3. Compute the right-hand side R = (!P) && (!Q):

   First compute !P and !Q, then AND them.
4. Fill the full table:

   | P | Q | P |  | Q | L = !(P |  | Q) | !P | !Q | R = (!P) && (!Q) |
   | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
   | T | T | T | F | F | F | F |
   | T | F | T | F | F | T | F |
   | F | T | T | F | T | F | F |
   | F | F | F | T | T | T | T |
5. Compare columns L and R: they match in every row, so the expressions are equivalent:

   !(P || Q) ≡ (!P) && (!Q).

**Insight:** De Morgan’s Laws are not “tricks”—they are facts defined by the truth tables. Whenever you negate a grouped condition, you flip AND ↔ OR and negate each part.

### Translate an everyday rule into Boolean logic and test it

A website rule says: “A user can access the page if they are an admin OR (they are logged in AND not banned).”

Let:

- •A = “user is admin”
- •L = “user is logged in”
- •B = “user is banned”

Write the Boolean expression and test two scenarios.

1. Translate the sentence carefully:

   - •“admin OR (logged in AND not banned)” becomes:

   E = A || (L && !B)
2. Scenario 1: A = F, L = T, B = F (not admin, logged in, not banned)

   Compute:

   - •!B = T
   - •L && !B = T && T = T
   - •A || (L && !B) = F || T = T

   So access is allowed.
3. Scenario 2: A = F, L = T, B = T (not admin, logged in, banned)

   Compute:

   - •!B = F
   - •L && !B = T && F = F
   - •A || (L && !B) = F || F = F

   So access is denied.

**Insight:** Parentheses encode the policy. Without them, a small change in grouping can create a security bug.

## Key Takeaways

- ✓

  Boolean logic computes with two values: TRUE and FALSE.
- ✓

  NOT `!` flips a truth value; AND `&&` is TRUE only if both inputs are TRUE; OR `||` is TRUE if at least one input is TRUE.
- ✓

  Truth tables precisely define operators and are the most reliable way to check your reasoning.
- ✓

  Use intermediate columns in truth tables to avoid errors in complex expressions.
- ✓

  Two expressions are logically equivalent (A ≡ B) if they match on every row of their truth tables.
- ✓

  De Morgan’s Laws: !(P && Q) ≡ (!P) || (!Q) and !(P || Q) ≡ (!P) && (!Q).
- ✓

  Equivalences let you rewrite conditions safely in code, circuits, and proofs.

## Common Mistakes

- ✗

  Confusing inclusive OR (`||`) with exclusive or (“either but not both”). In Boolean logic, `P || Q` is TRUE when both are TRUE.
- ✗

  Forgetting parentheses and relying on operator precedence, leading to a different meaning than intended.
- ✗

  Negating a grouped condition incorrectly (e.g., writing `!(P && Q)` as `(!P) && (!Q)` instead of `(!P) || (!Q)`).
- ✗

  Skipping intermediate columns in truth tables and making arithmetic-like “mental leaps” that hide errors.

## Practice

easy

Create the truth table for E = P && (!Q).

**Hint:** Make a column for !Q, then AND it with P.

Show solution

Truth table:

| P | Q | !Q | P && (!Q) |
| --- | --- | --- | --- |
| T | T | F | F |
| T | F | T | T |
| F | T | F | F |
| F | F | T | F |

E is TRUE only when P is TRUE and Q is FALSE.

medium

Use a truth table to decide whether these are equivalent: !(P && Q) and (!P) || (!Q).

**Hint:** Compute both expressions for all four (P, Q) rows and compare the final columns.

Show solution

They are equivalent. Truth table:

| P | Q | P && Q | !(P && Q) | !P | !Q | (!P) |  | (!Q) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| T | T | T | F | F | F | F |
| T | F | F | T | F | T | T |
| F | T | F | T | T | F | T |
| F | F | F | T | T | T | T |

The last two columns match.

hard

A rule says: “You can submit the form only if you are logged in and you have either accepted the terms or you are an admin.”

Let L = logged in, T = accepted terms, A = admin. Write a Boolean expression using only !, &&, ||. Then evaluate it for (L, T, A) = (T, F, F) and (T, F, T).

**Hint:** Translate “only if” here as a requirement: the condition must be TRUE to submit. Group “accepted terms or admin” with parentheses.

Show solution

Expression:

E = L && (T || A)

Evaluate (L, T, A) = (T, F, F):

- •(T || A) = (F || F) = F
- •E = L && (T || A) = T && F = F

So cannot submit.

Evaluate (L, T, A) = (T, F, T):

- •(T || A) = (F || T) = T
- •E = T && T = T

So can submit.

## Connections

- •Next: [Proof Techniques](/tech-tree/proof-techniques/) (uses Boolean structure to justify steps and handle contradictions)
- •Next: [Propositional Logic](/tech-tree/propositional-logic/) (adds more connectives like →, ↔, quantifiers later, and studies satisfiability)

Quality: A (4.5/5)

[← back to tree](/tech-tree/)[browse all →](/tech-tree/inventory/)
