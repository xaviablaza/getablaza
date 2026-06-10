---
title: Derivative Rules
description: Power rule, product rule, quotient rule, chain rule.
date: '2026-07-01'
scheduled: '2026-08-15'
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
inspiration_url: https://templeton.host/tech-tree/derivative-rules/
inspiration_category: tech-tree
---

> Source-copy draft imported from [https://templeton.host/tech-tree/derivative-rules/](https://templeton.host/tech-tree/derivative-rules/). Names, domain references, and local media paths were adapted for Xavi Ablaza / getablaza.com.

[←Back to Tech Tree](/tech-tree/)

[inventory](/tech-tree/inventory/)[coverage](/tech-tree/coverage/)

# Derivative Rules

CalculusDifficulty: ★★☆☆☆Depth: 3Unlocks: 77

Power rule, product rule, quotient rule, chain rule.

## Interactive Visualization

⏮◀◀▶▶STEP0.25x1xZOOM

t=0s

## Core Concepts

- -Power rule: derivative of x^n is n \* x^(n-1) (for real n where defined)
- -Product rule: derivative of f(x)\*g(x) is f'(x)\*g(x) + f(x)\*g'(x)
- -Chain rule: derivative of a composition f(g(x)) is f'(g(x)) \* g'(x)

## Key Symbols & Notation

d/dx (derivative operator)

## Essential Relationships

- -Quotient rule is obtained by applying the product rule to f(x) \* (1/g(x)) (i.e., division = multiplication by reciprocal)

## Prerequisites (1)

[Derivatives6 atoms](/tech-tree/derivatives-basic/)

## Unlocks (3)

[Multivariable Calculuslvl 3](/tech-tree/multivariable-calculus/)[Multivariable Chain Rulelvl 3](/tech-tree/chain-rule-multivar/)[Taylor Serieslvl 3](/tech-tree/taylor-series/)

Advanced Learning Details

### Graph Position

33

Depth Cost

77

Fan-Out (ROI)

28

Bottleneck Score

3

Chain Length

### Cognitive Load

5

Atomic Elements

25

Total Elements

L0

Percentile Level

L3

Atomic Level

### All Concepts (10)

- - Power rule: for a function x^n (or more generally [g(x)]^n) the derivative is n x^{n-1} (or n[g(x)]^{n-1}·g'(x))
- - Product rule: derivative of a product u(x)·v(x) is u'(x)·v(x) + u(x)·v'(x)
- - Quotient rule: derivative of u(x)/v(x) is (u'(x)·v(x) - u(x)·v'(x)) / [v(x)]^2, with v(x) ≠ 0
- - Chain rule: derivative of a composite f(g(x)) is f'(g(x))·g'(x)
- - Identification of inner and outer functions: recognizing components of a composite so the chain rule applies
- - Conditions for applying rules: component functions must be differentiable where used; quotient rule additionally requires denominator ≠ 0
- - Linearity of the derivative (sum and constant multiple rules) as a practical tool when combining the other rules: (f+g)' = f' + g' and (c·f)' = c·f'
- - Corollaries / common derived formulas: derivative of a reciprocal 1/v = -v'/v^2 and derivative of a quotient obtained via product+reciprocal
- - Higher-order derivatives by repeated application of the rules (e.g., taking the derivative of a derivative)
- - Strategy/decision skill: recognizing which rule or combination of rules to apply (e.g., product vs. chain vs. nested combinations) and when to simplify algebraically first

### Teaching Strategy

Self-serve tutorial - low prerequisites, straightforward concepts.

Most real-world functions aren’t “single-piece” expressions like x². They’re built by multiplying pieces, nesting pieces inside other pieces, and dividing pieces. Derivative rules are the small toolkit that lets you differentiate those built-up functions reliably—without re-deriving limits every time.

TL;DR:

Derivative rules turn differentiation into pattern-matching:

- •Power rule: d/dx (xⁿ) = n·xⁿ⁻¹ (where defined)
- •Product rule: d/dx (f·g) = f′g + fg′
- •Quotient rule: d/dx (f/g) = (f′g − fg′)/g² (g ≠ 0)
- •Chain rule: d/dx f(g(x)) = f′(g(x))·g′(x)

Used together, they differentiate most algebraic expressions you’ll meet in early calculus.

## What Is Derivative Rules?

### Why we need “rules”

You already know what a derivative *means*: the instantaneous rate of change, or the slope of the tangent line. The definition is

f′(x) = lim\_{h→0} (f(x+h) − f(x)) / h.

That definition is the foundation—but using it from scratch for every function is slow. In practice, functions are built from simpler ones, and we want a fast way to translate “how the function is built” into “how its slope behaves.”

Derivative rules are exactly that translation layer.

### What counts as a “rule”?

A derivative rule is a statement of the form

If a function has structure X, then its derivative has structure Y.

For example:

- •If the function is a power xⁿ, its derivative is n·xⁿ⁻¹.
- •If the function is a product f(x)g(x), its derivative is f′g + fg′.
- •If the function is a composition f(g(x)), its derivative is f′(g(x))·g′(x).

### Operator viewpoint (useful habit)

Write the derivative as an operator:

D = d/dx.

Then rules can be read as “how D interacts with algebra.” For instance:

- •D[xⁿ] = n·xⁿ⁻¹
- •D[f·g] = (Df)·g + f·(Dg)

This operator view helps you avoid a common mistake: differentiating “piece by piece” incorrectly when multiplication or composition is involved.

### Domain and “where defined”

Some rules mention conditions like “where defined.” Example: xⁿ with real n isn’t always defined for negative x (e.g., x^{1/2}). When we say

d/dx (xⁿ) = n·xⁿ⁻¹,

we mean: on any interval where xⁿ is defined as a real-valued differentiable function, this derivative formula holds.

### Big picture

In early calculus, the workflow is:

1. 1)**Parse the structure** (power, product, quotient, composition).
2. 2)**Apply the matching derivative rule**.
3. 3)**Simplify**.

The rest of this lesson builds that skill carefully, one structure at a time.

## Core mechanic 1: Power Rule (and constant multiple)

### Why the power rule matters

Polynomials are the “atoms” of algebraic functions. If you can differentiate xⁿ quickly, you can differentiate any polynomial, and then many more functions after combining with other rules.

### Power rule statement

For real n (where xⁿ is differentiable),

d/dx (xⁿ) = n·xⁿ⁻¹.

Examples:

- •d/dx (x⁵) = 5x⁴
- •d/dx (x) = d/dx (x¹) = 1·x⁰ = 1
- •d/dx (1) = d/dx (x⁰) = 0·x⁻¹ = 0 (consistent: derivative of a constant is 0)

### Constant multiple rule (used constantly)

If c is a constant and f is differentiable, then

d/dx (c·f(x)) = c·f′(x).

This means you can “pull constants out” before differentiating.

### Linear combinations (bonus that you’ll use implicitly)

If f and g are differentiable, then

d/dx (f(x) + g(x)) = f′(x) + g′(x),

d/dx (f(x) − g(x)) = f′(x) − g′(x).

These combine with the power rule to make polynomials immediate.

### Power rule for negative and fractional powers

The formula still works, but you must respect domains.

1) Negative powers (x ≠ 0):

f(x) = x^{−3} = 1/x³

f′(x) = −3·x^{−4} = −3/x⁴.

2) Fractional powers (domain depends):

f(x) = x^{1/2} = √x (domain x ≥ 0)

f′(x) = (1/2)·x^{−1/2} = 1/(2√x),

valid for x > 0 (note: derivative blows up at x = 0).

### A short “show your work” derivation (intuition)

A key reason the power rule is believable is how it behaves for integer n. For n = 2:

Let f(x) = x².

f′(x) = lim\_{h→0} ((x+h)² − x²)/h

= lim\_{h→0} (x² + 2xh + h² − x²)/h

= lim\_{h→0} (2xh + h²)/h

= lim\_{h→0} (2x + h)

= 2x.

That matches 2·x¹.

### When the power rule is *not* enough

If you see something like (3x² + 1)⁵, the outside is a power, but the inside is not just x. That is a *composition*, and you’ll need the **chain rule** later in this lesson.

For now, power rule handles expressions where the variable is directly the base (xⁿ), plus sums and constant multiples.

## Core mechanic 2: Product Rule and Quotient Rule

### Why products and quotients need special care

A tempting (but wrong) idea is:

(d/dx)(f·g) ?= f′·g′.

That fails because when x changes a little, **both** factors change, and their interaction matters. The product rule accounts for that interaction.

---

## Product rule

### Statement

If f and g are differentiable, then

d/dx (f(x)g(x)) = f′(x)g(x) + f(x)g′(x).

### Why it looks like that (tiny-change intuition)

Let x increase by a small amount Δx. Then:

- •f changes by about f′(x)Δx
- •g changes by about g′(x)Δx

The product changes like:

(f + Δf)(g + Δg) − fg

= fΔg + gΔf + ΔfΔg.

Divide by Δx:

(fΔg)/Δx + (gΔf)/Δx + (ΔfΔg)/Δx.

As Δx → 0:

- •Δg/Δx → g′
- •Δf/Δx → f′
- •(ΔfΔg)/Δx → 0 (it’s “second order small”)

So the derivative becomes f·g′ + g·f′.

### Practical pattern

For (something)·(something), write:

(fg)′ = f′g + fg′.

Differentiate the first factor, keep the second the same, then swap.

---

## Quotient rule

### Statement

If f and g are differentiable and g(x) ≠ 0, then

d/dx (f(x)/g(x)) = (f′(x)g(x) − f(x)g′(x)) / (g(x))².

### Why it’s true (derive from product + chain)

Instead of memorizing, you can rebuild it:

f/g = f · (g^{−1}).

Differentiate using product rule:

d/dx [f·g^{−1}] = f′·g^{−1} + f·d/dx[g^{−1}].

Now use chain rule on g^{−1} (we’ll formalize chain rule soon, but we can still track structure):

d/dx[g^{−1}] = (−1)·g^{−2}·g′.

So:

(f/g)′ = f′·g^{−1} + f·(−1)·g^{−2}·g′

= f′/g − f g′/g²

= (f′g)/g² − (f g′)/g²

= (f′g − f g′)/g².

### Product vs quotient: when to use which?

If you see a division bar, quotient rule works. But often it’s simpler to rewrite as a product with a power:

(3x² + 1)/(x⁴) = (3x² + 1)·x^{−4}.

Then use product rule + power rule.

Here’s a quick comparison:

| Situation | Good first move | Why |
| --- | --- | --- |
| f(x)g(x) | Product rule | Direct structure |
| f(x)/g(x) with simple g | Rewrite as g^{−1} | Avoid big fraction algebra |
| f(x)/g(x) complicated | Quotient rule | Cleaner than expanding |

### Breathing room: a reality check

- •Product rule adds two terms.
- •Quotient rule creates a numerator difference and a squared denominator.

This “expression growth” is normal. After differentiating, simplify carefully (factor common pieces, combine like terms). Don’t try to simplify *during* differentiation unless it’s obviously helpful.

## Core mechanic 3: Chain Rule (composition)

### Why the chain rule is the most important rule

Many functions are nested: you don’t just compute something from x, you compute something from something-from-x.

Examples:

- •(3x + 1)⁵
- •√(1 + x²)
- •(sin(x))² (if you already know trig derivatives later)

In all of these, there is an **outside function** applied to an **inside function**.

### Composition language

If y = f(u) and u = g(x), then y = f(g(x)).

The chain rule connects their rates of change:

If x changes, u changes; if u changes, y changes.

### Statement

If y = f(g(x)) and both functions are differentiable (where needed), then

d/dx f(g(x)) = f′(g(x)) · g′(x).

Read it as:

- •Differentiate the outside function (as if its input were “a blank”).
- •Then multiply by the derivative of the inside.

### Why it works (rate-of-change viewpoint)

Think of derivatives as “rates”:

dy/dx = (dy/du)·(du/dx).

This is not just a mnemonic; it reflects that small changes propagate:

- •x changes by dx
- •that causes u to change by du ≈ (du/dx)dx
- •that causes y to change by dy ≈ (dy/du)du

Combine:

dy ≈ (dy/du)·(du/dx)·dx,

so dy/dx ≈ (dy/du)(du/dx), and in the limit it becomes exact.

### The most common chain-rule forms

1) Power of a function:

d/dx (g(x))ⁿ = n·(g(x))ⁿ⁻¹ · g′(x).

2) Root of a function:

d/dx √(g(x)) = d/dx (g(x))^{1/2}

= (1/2)(g(x))^{−1/2}·g′(x)

= g′(x)/(2√(g(x))).

### Identifying “inside” and “outside”

Practice saying it out loud:

- •For (3x + 1)⁵: outside is u⁵, inside is u = 3x + 1.
- •For √(1 + x²): outside is √u, inside is u = 1 + x².

### Multi-layer nesting

Sometimes you have multiple layers:

h(x) = (1 + (2x − 3)²)^{5}.

You can name layers:

- •a(x) = 2x − 3
- •b(x) = 1 + (a(x))²
- •h(x) = (b(x))⁵

Then apply chain rule repeatedly:

h′(x) = 5(b(x))⁴ · b′(x)

b′(x) = 2a(x) · a′(x)

a′(x) = 2.

Finally substitute back.

### Product/quotient plus chain is the “real world” mix

Most nontrivial derivatives are combinations. A good strategy is:

1. 1)Find the outermost operation (sum, product, quotient, composition).
2. 2)Apply its rule.
3. 3)Recursively differentiate the pieces.

Take a breath when expressions get big: the rules are local and mechanical, even when the algebra looks messy.

## Application/Connection: Using rules together + what this unlocks

### Putting the rules together (workflow)

Most functions you’ll differentiate now are built from:

- •sums and constants,
- •powers,
- •products,
- •quotients,
- •compositions.

A reliable workflow:

1) **Rewrite** to clarify structure.

- •Replace √(…) with (…)^{1/2}
- •Replace 1/(…) with (…)^{−1}

2) **Mark the top-level structure**.

- •Is it A + B? A·B? A/B? f(g(x))?

3) **Differentiate using the matching rule**.

- •Apply product/quotient/chain at the top.

4) **Simplify**.

- •Factor common terms.
- •Combine fractions.
- •Reduce powers.

### Why simplification is not just “cosmetic”

Simplifying can reveal:

- •where the derivative is undefined,
- •zeros of the derivative (critical points),
- •cancellations that prevent numerical blow-ups.

### How this connects to later topics

These rules are prerequisites because they scale.

1) **Multivariable calculus**

When functions depend on multiple variables, you’ll use partial derivatives like ∂/∂x. The algebraic structure rules (product rule, chain rule) still apply, but with partials.

Connection: [Multivariable Calculus](/tech-tree/multivariable-calculus/)

2) **Multivariable chain rule**

In multiple dimensions, compositions become richer (e.g., y = f(**g**(x)) where **g** outputs a vector). The idea “outside derivative times inside derivative” becomes Jacobians and matrix multiplication.

Connection: [Multivariable Chain Rule](/tech-tree/chain-rule-multivar/)

3) **Taylor series**

Taylor series uses higher derivatives f″(x), f‴(x), etc. Computing those efficiently depends on being fluent with these first-derivative rules; otherwise higher derivatives become impossible to manage.

Connection: [Taylor Series](/tech-tree/taylor-series/)

### A quick comparison table (what each rule reacts to)

| Rule | Trigger structure | Output form | Common use |
| --- | --- | --- | --- |
| Power | xⁿ or (g(x))ⁿ | n·(base)ⁿ⁻¹·(base)′ | Polynomials, roots, rational powers |
| Product | f·g | f′g + fg′ | Multiplying expressions |
| Quotient | f/g | (f′g − fg′)/g² | Ratios, rational expressions |
| Chain | f(g(x)) | f′(g(x))·g′ | Nested functions |

### Final mindset

Derivative rules are not a bag of tricks—they’re a language. Once you can “read” an expression’s structure, differentiation becomes systematic and predictable.

## Worked Examples (3)

### Differentiate a polynomial with negative powers

Compute d/dx [ 4x³ − 7x + 2 + 5x^{−2} ].

1. Differentiate term-by-term using linearity:

   D[4x³ − 7x + 2 + 5x^{−2}] = D[4x³] − D[7x] + D[2] + D[5x^{−2}].
2. Use constant multiple + power rule:

   D[4x³] = 4·D[x³] = 4·(3x²) = 12x².
3. D[7x] = 7·D[x] = 7·1 = 7, so −D[7x] = −7.
4. D[2] = 0.
5. D[5x^{−2}] = 5·D[x^{−2}] = 5·(−2x^{−3}) = −10x^{−3}.
6. Combine results:

   f′(x) = 12x² − 7 − 10x^{−3} = 12x² − 7 − 10/x³.

**Insight:** Polynomials and “almost polynomials” (with negative powers) are straightforward because they’re just sums of power-rule terms. Keep domain in mind: x^{−3} implies x ≠ 0.

### Product rule with a nested power (product + chain)

Compute d/dx [ x²(3x + 1)⁵ ].

1. Identify structure: it’s a product f(x)g(x) with

   f(x) = x²,

   g(x) = (3x + 1)⁵.
2. Apply product rule:

   D[f·g] = f′g + fg′

   ⇒ D[x²(3x + 1)⁵] = D[x²]·(3x + 1)⁵ + x²·D[(3x + 1)⁵].
3. Differentiate f(x) = x²:

   D[x²] = 2x.
4. Differentiate g(x) = (3x + 1)⁵ using chain rule:

   Let u = 3x + 1, so g(x) = u⁵.

   D[u⁵] = 5u⁴·u′.

   Here u′ = D[3x + 1] = 3.

   So D[(3x + 1)⁵] = 5(3x + 1)⁴·3 = 15(3x + 1)⁴.
5. Substitute back:

   f′(x) = (2x)(3x + 1)⁵ + x²·15(3x + 1)⁴.
6. Optional simplification by factoring common terms:

   Both terms share x(3x + 1)⁴:

   (2x)(3x + 1)⁵ = 2x(3x + 1)⁴(3x + 1)

   15x²(3x + 1)⁴ = 15x²(3x + 1)⁴

   So

   f′(x) = x(3x + 1)⁴[2(3x + 1) + 15x]

   = x(3x + 1)⁴[6x + 2 + 15x]

   = x(3x + 1)⁴(21x + 2).

**Insight:** When product rule creates two terms, factoring afterward often makes the result cleaner and more informative (e.g., for finding zeros of the derivative).

### Quotient rule (and careful algebra)

Compute d/dx [ (x² + 1)/(x − 2) ].

1. Identify f(x) = x² + 1 and g(x) = x − 2 (with x ≠ 2).
2. Compute derivatives:

   f′(x) = D[x² + 1] = 2x,

   g′(x) = D[x − 2] = 1.
3. Apply quotient rule:

   D[f/g] = (f′g − fg′)/g²

   ⇒ D[(x² + 1)/(x − 2)] = ( (2x)(x − 2) − (x² + 1)(1) )/(x − 2)².
4. Expand numerator carefully:

   (2x)(x − 2) = 2x² − 4x

   So numerator = (2x² − 4x) − (x² + 1)

   = 2x² − 4x − x² − 1

   = x² − 4x − 1.
5. Final result:

   (x² + 1)/(x − 2) ⇒ derivative = (x² − 4x − 1)/(x − 2)².

**Insight:** Quotient rule is often less about calculus and more about disciplined parentheses. Write the full (f′g − fg′) before expanding.

## Key Takeaways

- ✓

  Power rule: d/dx (xⁿ) = n·xⁿ⁻¹, valid on intervals where xⁿ is differentiable and real-valued (watch domains for fractional/negative powers).
- ✓

  Linearity: d/dx (af + bg) = a f′ + b g′ lets you differentiate sums term-by-term.
- ✓

  Product rule: (fg)′ = f′g + fg′; do not multiply derivatives.
- ✓

  Quotient rule: (f/g)′ = (f′g − fg′)/g² with g ≠ 0; parentheses prevent algebra errors.
- ✓

  Chain rule: d/dx f(g(x)) = f′(g(x))·g′(x); it’s the rule for nesting.
- ✓

  Many derivatives require combining rules: product + chain is especially common.
- ✓

  Simplify after differentiating: factoring can reveal structure (zeros, undefined points) and reduce clutter.

## Common Mistakes

- ✗

  Treating (fg)′ as f′g′ instead of f′g + fg′.
- ✗

  Forgetting the inside derivative in the chain rule (e.g., differentiating (3x+1)⁵ as 5(3x+1)⁴ instead of 15(3x+1)⁴).
- ✗

  Dropping parentheses in the quotient rule numerator: writing f′g − fg′ without grouping, then expanding incorrectly.
- ✗

  Ignoring domain restrictions from negative/fractional powers (e.g., x^{−1} requires x ≠ 0; √x typically requires x ≥ 0).

## Practice

easy

Differentiate: f(x) = 6x^{5/2} − 3x^{−1} + 8.

**Hint:** Use power rule term-by-term. Rewrite x^{−1} as a power and keep domains in mind (x > 0 for x^{5/2} if interpreted as real).

Show solution

f′(x) = 6·(5/2)x^{3/2} − 3·(−1)x^{−2} + 0

= 15x^{3/2} + 3x^{−2}

= 15x^{3/2} + 3/x².

medium

Differentiate: y = (x² − 1)(x³ + 2x).

**Hint:** Product rule with f(x)=x²−1 and g(x)=x³+2x. Differentiate each using power rule.

Show solution

Let f(x)=x²−1 ⇒ f′(x)=2x.

Let g(x)=x³+2x ⇒ g′(x)=3x²+2.

Product rule:

y′ = f′g + fg′

= (2x)(x³+2x) + (x²−1)(3x²+2).

Optionally expand:

(2x)(x³+2x)=2x⁴+4x².

(x²−1)(3x²+2)=3x⁴+2x²−3x²−2=3x⁴−x²−2.

So y′ = (2x⁴+4x²) + (3x⁴−x²−2) = 5x⁴+3x²−2.

hard

Differentiate: y = √(1 + x²) / (2x − 1).

**Hint:** Use quotient rule with f(x)=√(1+x²) and g(x)=2x−1. For f′, rewrite √(1+x²) as (1+x²)^{1/2} and apply chain rule.

Show solution

Let f(x)=(1+x²)^{1/2}.

Then f′(x) = (1/2)(1+x²)^{−1/2}·(2x) = x/√(1+x²).

Let g(x)=2x−1 ⇒ g′(x)=2.

Quotient rule:

y′ = (f′g − fg′)/g²

= \big( (x/√(1+x²))(2x−1) − (√(1+x²))·2 \big)/(2x−1)².

You may leave it like this, or combine terms over √(1+x²):

Numerator = \frac{x(2x−1) − 2(1+x²)}{√(1+x²)}

= \frac{2x²−x −2 −2x²}{√(1+x²)}

= \frac{−x−2}{√(1+x²)}.

So

y′ = \frac{−x−2}{√(1+x²)(2x−1)²}.

## Connections

Next nodes you can unlock and why they rely on these rules:

- •[Multivariable Calculus](/tech-tree/multivariable-calculus/): partial derivatives reuse product/chain rules with ∂/∂x and ∂/∂y.
- •[Multivariable Chain Rule](/tech-tree/chain-rule-multivar/): generalizes “outside derivative × inside derivative” to Jacobians and matrix products (often with bold vectors like **x**).
- •[Taylor Series](/tech-tree/taylor-series/): repeated differentiation depends on fluent use of power/product/chain rules to compute f′, f″, f‴, …

Quality: A (4.3/5)

[← back to tree](/tech-tree/)[browse all →](/tech-tree/inventory/)
