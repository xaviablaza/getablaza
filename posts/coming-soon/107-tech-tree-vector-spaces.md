---
title: Vector Spaces
description: Sets with addition and scalar multiplication satisfying axioms.
date: '2026-07-01'
scheduled: '2026-10-15'
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
inspiration_url: https://templeton.host/tech-tree/vector-spaces/
inspiration_category: tech-tree
---

> Source-copy draft imported from [https://templeton.host/tech-tree/vector-spaces/](https://templeton.host/tech-tree/vector-spaces/). Names, domain references, and local media paths were adapted for Xavi Ablaza / getablaza.com.

[←Back to Tech Tree](/tech-tree/)

[inventory](/tech-tree/inventory/)[coverage](/tech-tree/coverage/)

# Vector Spaces

Linear AlgebraDifficulty: ★★☆☆☆Depth: 2Unlocks: 12

Sets with addition and scalar multiplication satisfying axioms.

## Interactive Visualization

⏮◀◀▶▶STEP0.25x1xZOOM

t=0s

## Core Concepts

- -Vectors form an abelian group under vector addition (closure, associativity, commutativity, additive identity and inverses)
- -Scalar multiplication: vectors are multiplied by scalars (elements of a field)
- -Compatibility axioms tying addition and scalar multiplication (distributivity of scalar over vector addition and of field addition over vectors; associativity with field multiplication; scalar 1 acts as identity)

## Key Symbols & Notation

F (the field of scalars)

## Essential Relationships

- -The field F acts on the additive abelian group of vectors via scalar multiplication, satisfying the compatibility axioms

## Prerequisites (2)

[Vectors Introduction6 atoms](/tech-tree/vectors-intro/)[Sets6 atoms](/tech-tree/sets-basic/)

## Unlocks (1)

[Linear Independencelvl 2](/tech-tree/linear-independence/)

Advanced Learning Details

### Graph Position

23

Depth Cost

12

Fan-Out (ROI)

2

Bottleneck Score

2

Chain Length

### Cognitive Load

5

Atomic Elements

35

Total Elements

L2

Percentile Level

L3

Atomic Level

### All Concepts (14)

- - vector space: a set equipped with two operations (vector addition and scalar multiplication) that satisfy a fixed list of axioms
- - field of scalars: the set (e.g., R, C) from which scalars are drawn and whose arithmetic interacts with scalar multiplication
- - closure under addition: sum of any two vectors in the set is again in the set
- - closure under scalar multiplication: scalar multiple of any vector is again in the set
- - associativity of vector addition: (u + v) + w = u + (v + w)
- - commutativity of vector addition: u + v = v + u
- - additive identity (zero vector): existence of 0 in V with v + 0 = v for all v
- - additive inverse: for every v there exists −v with v + (−v) = 0
- - distributivity of scalar multiplication over vector addition: a(u + v) = au + av
- - distributivity of scalar addition over scalar multiplication: (a + b)v = av + bv
- - compatibility of scalar multiplication with field multiplication: a(bv) = (ab)v
- - identity scalar property: 1·v = v (where 1 is multiplicative identity in the field of scalars)
- - uniqueness results that follow from the axioms (uniqueness of zero vector and additive inverses)
- - standard derived zero/signed-scalar rules: 0·v = 0\_vector, a·0\_vector = 0\_vector, (−1)·v = −v

### Teaching Strategy

Self-serve tutorial - low prerequisites, straightforward concepts.

You already know how to add arrows in the plane and scale them. A vector space is the upgrade that says: “Actually, those rules can apply to lots of things that aren’t arrows”—like polynomials, signals, images, and functions—so long as addition and scaling behave consistently.

TL;DR:

A vector space over a field F is a set V with (1) vector addition making V an abelian group and (2) scalar multiplication by elements of F, linked by distributive/associative axioms. The payoff is that “linear combinations” make sense, unlocking linear independence, bases, and linear maps.

## What Is a Vector Space?

### Why we need a definition (not just examples)

In geometry, vectors look like arrows. But in linear algebra, “vector” really means: *an object you can add and scale in a way that behaves like ordinary arithmetic.*

That’s powerful because it lets us treat many different domains with one toolkit:

- •polynomials (for curve fitting),
- •functions (for differential equations),
- •matrices (for data and transformations),
- •signals (for audio/image processing).

The key is not the *shape* of objects—it’s the *rules*.

---

### The official definition

A **vector space** is a set VVV together with:

1) **Vector addition**: a function +:V×V→V+ : V \times V \to V+:V×V→V

2) **Scalar multiplication**: a function ⋅:F×V→V\cdot : F \times V \to V⋅:F×V→V (often written just as avavav)

where FFF is a **field** (the scalars). Typical choices are R\mathbb{R}R or C\mathbb{C}C. The field matters because we need to add/multiply scalars and have identities/inverses in the scalar world.

We say: “VVV is a vector space **over** FFF.”

---

### The axioms, grouped by meaning

You can memorize 8–10 axioms, but it’s better to group them into two clusters plus “compatibility.”

#### A) Addition behaves like normal addition (abelian group)

For all **u**, **v**, **w** ∈ V:

1. 1)**Closure under addition**: **u** + **v** ∈ V
2. 2)**Associativity**: (**u** + **v**) + **w** = **u** + (**v** + **w**)
3. 3)**Commutativity**: **u** + **v** = **v** + **u**
4. 4)**Additive identity**: there exists **0** ∈ V such that **v** + **0** = **v**
5. 5)**Additive inverse**: for each **v**, there exists −**v** with **v** + (−**v**) = **0**

This is exactly: “(V, +) is an abelian group.”

#### B) Scaling is allowed

For all a∈Fa \in Fa∈F and **v** ∈ V:

- •a v∈Va\,\mathbf{v} \in Vav∈V (closure under scalar multiplication)

#### C) Scaling and addition interact consistently (compatibility)

For all a,b∈Fa,b \in Fa,b∈F and **u**, **v** ∈ V:

1. 1)**Distribute scalar over vector addition**:

a(u+v)=au+ava(\mathbf{u}+\mathbf{v}) = a\mathbf{u} + a\mathbf{v}a(u+v)=au+av

2. 2)**Distribute field addition over vectors**:

(a+b)v=av+bv(a+b)\mathbf{v} = a\mathbf{v} + b\mathbf{v}(a+b)v=av+bv

3. 3)**Associativity of scalar multiplication**:

(ab)v=a(bv)(ab)\mathbf{v} = a(b\mathbf{v})(ab)v=a(bv)

4. 4)**Scalar identity acts as identity**:

1v=v1\mathbf{v} = \mathbf{v}1v=v

---

### A quick “feel” check

If you can:

- •add two objects of the set and stay inside the set,
- •scale any object by any scalar and stay inside the set,
- •and the distributive/identity rules keep working,

then linear algebra becomes available.

In this lesson, we’ll keep returning to the same habit: **test closure + distributivity** early—those are frequent failure points, especially in non-geometric examples.

## Core Mechanic 1: Addition as an Abelian Group (Closure, Zero, Negatives)

### Why focus on addition first?

Scalar multiplication is only meaningful if “adding vectors” already forms a stable arithmetic world. The abelian-group requirements guarantee you can:

- •combine multiple vectors without ambiguity (associativity),
- •reorder sums (commutativity),
- •subtract vectors via inverses,
- •and have a neutral element (**0**).

These are what make expressions like

v1+v2+⋯+vk\mathbf{v}\_1 + \mathbf{v}\_2 + \cdots + \mathbf{v}\_kv1​+v2​+⋯+vk​

well-defined.

---

## Concrete check: does the set contain its own sums?

Closure under addition is often the first axiom that fails.

### Example A (geometric): R2\mathbb{R}^2R2

Take **u** = (1, 2), **v** = (3, −5). Then

(1, 2) + (3, −5) = (4, −3) ∈ R2\mathbb{R}^2R2.

So closure holds.

### Example B (non-geometry): polynomials of degree ≤ 2

Let

- •p(x)=1+xp(x)=1+xp(x)=1+x
- •q(x)=x2−3q(x)=x^2-3q(x)=x2−3

Then

p(x)+q(x)=(1+x)+(x2−3)=x2+x−2p(x)+q(x) = (1+x) + (x^2-3) = x^2 + x - 2p(x)+q(x)=(1+x)+(x2−3)=x2+x−2

This is still a polynomial of degree ≤ 2. So closure holds.

### Example C (common fail): “polynomials of degree exactly 2”

Let p(x)=x2p(x)=x^2p(x)=x2 and q(x)=−x2q(x)=-x^2q(x)=−x2. Then

p(x)+q(x)=0p(x)+q(x)=0p(x)+q(x)=0

But 0 is not degree exactly 2, so the set is not closed under addition.

The lesson: **degree ≤ n works; degree exactly n usually fails**.

---

## The zero vector is not always (0,0)

The additive identity depends on what the objects are.

- •In Rn\mathbb{R}^nRn, **0** is (0, 0, …, 0).
- •In polynomial spaces, **0** is the **zero polynomial** $0$ (all coefficients 0).
- •In function spaces, **0** is the **zero function** f(x)=0f(x)=0f(x)=0 for all x.

You should think: “the zero object under addition.”

---

## Additive inverses: subtraction must stay inside

If **v** is in the set, then −**v** must also be in the set.

### Polynomial example

If p(x)=x2+xp(x)=x^2+xp(x)=x2+x, then −p(x)=−(x2+x)=−x2−xp(x)=-(x^2+x)=-x^2-xp(x)=−(x2+x)=−x2−x, which is still a polynomial (and still degree ≤ 2 if we’re in that set).

### Function example

If f(x)=sin⁡xf(x)=\sin xf(x)=sinx, then −f(x)=−sin⁡xf(x)=-\sin xf(x)=−sinx is still a function of the same type.

But beware: if your set is restricted (e.g., “functions that are always nonnegative”), additive inverses typically fail.

---

## Tiny visualization: closure under addition in a function space

Think of functions as “curves.” Adding functions adds their y-values pointwise.

Take two functions fff and ggg. Their sum is:

(f+g)(x)=f(x)+g(x)(f+g)(x) = f(x) + g(x)(f+g)(x)=f(x)+g(x)

Here’s a simple ASCII snapshot at a few x-values:

| x | f(x) | g(x) | (f+g)(x) |
| --- | --- | --- | --- |
| 0 | 1 | 2 | 3 |
| 1 | 0 | 4 | 4 |
| 2 | -1 | 1 | 0 |

If your set is “all real-valued functions,” the sum is still real-valued at every x, so closure holds.

**Interactive canvas idea (guided):** Plot two curves (e.g., f(x)=sin⁡xf(x)=\sin xf(x)=sinx, g(x)=0.5xg(x)=0.5xg(x)=0.5x). Add a toggle “show f+g.” Let learners drag a point x₀ and observe the vertical addition of y-values. The closure message becomes: “the result is still a function in the same set.”

## Core Mechanic 2: Scalar Multiplication + Compatibility (Distributivity, Identity, Associativity)

### Why scalar multiplication matters

Scalar multiplication is what lets you talk about *size* and *direction* (or more abstractly: intensity, amplitude, coefficient scaling). It’s also what makes **linear combinations** possible:

a1v1+⋯+akvka\_1\mathbf{v}\_1 + \cdots + a\_k\mathbf{v}\_ka1​v1​+⋯+ak​vk​

But scalar multiplication must be consistent with addition; otherwise linear combinations become ambiguous and algebra breaks.

---

## Scalar multiplication closure

For every a∈Fa \in Fa∈F and **v** ∈ V, we need av∈Va\mathbf{v} \in Vav∈V.

### Non-geometry closure example: polynomials

Let F=RF=\mathbb{R}F=R and V={polynomials of degree ≤ 2}V=\{\text{polynomials of degree ≤ 2}\}V={polynomials of degree ≤ 2}.

If a=3a=3a=3 and p(x)=x2−1p(x)=x^2-1p(x)=x2−1, then

3p(x)=3(x2−1)=3x2−33p(x)=3(x^2-1)=3x^2-33p(x)=3(x2−1)=3x2−3

Still degree ≤ 2. Closure holds.

### Common fail: integer-only scalars with real vectors

If you try to treat R2\mathbb{R}^2R2 as a vector space over Z\mathbb{Z}Z, you run into a deeper issue: Z\mathbb{Z}Z is not a field (no multiplicative inverses for most integers). Many theorems break, and it’s not a vector space by definition.

So the “F (field)” requirement is not decoration—it’s structural.

---

## Distributivity: the rule that keeps scaling honest

There are two distributive laws and they fail in many “almost vector spaces.”

### 1) Scalar over vector sum

a(u+v)=au+ava(\mathbf{u}+\mathbf{v}) = a\mathbf{u} + a\mathbf{v}a(u+v)=au+av

**Function visualization (pointwise):**

Let a=2a=2a=2, f(x)=xf(x)=xf(x)=x, g(x)=1g(x)=1g(x)=1.

- •Left: $2(f+g)(x)=2(x+1)=2x+2$
- •Right: (2f+2g)(x)=2x+2(2f+2g)(x)=2x+2(2f+2g)(x)=2x+2

Same function.

### 2) Field addition over vectors

(a+b)v=av+bv(a+b)\mathbf{v} = a\mathbf{v} + b\mathbf{v}(a+b)v=av+bv

**Polynomial visualization (coefficient scaling):**

Let p(x)=x2+xp(x)=x^2+xp(x)=x2+x and a=2a=2a=2, b=−5b=-5b=−5.

Compute the left side:

(a+b)p=(2−5)p=(−3)p=−3x2−3x(a+b)p = (2-5)p = (-3)p = -3x^2-3x(a+b)p=(2−5)p=(−3)p=−3x2−3x

Compute the right side:

ap+bp=2(x2+x)+(−5)(x2+x)ap + bp = 2(x^2+x) + (-5)(x^2+x)ap+bp=2(x2+x)+(−5)(x2+x)

=(2x2+2x)+(−5x2−5x)= (2x^2+2x) + (-5x^2-5x)=(2x2+2x)+(−5x2−5x)

=−3x2−3x= -3x^2 - 3x=−3x2−3x

They match.

---

## Associativity with field multiplication

(ab)v=a(bv)(ab)\mathbf{v} = a(b\mathbf{v})(ab)v=a(bv)

This says: it doesn’t matter whether you scale by bbb then aaa, or scale once by ababab.

In Rn\mathbb{R}^nRn this is obvious; in function spaces it is still pointwise obvious:

If (bv)(x)=b⋅v(x)(b\mathbf{v})(x) = b\cdot v(x)(bv)(x)=b⋅v(x), then

a(bv)(x)=a(bv(x))=(ab)v(x)=((ab)v)(x).a(b\mathbf{v})(x) = a(bv(x)) = (ab)v(x) = ((ab)\mathbf{v})(x).a(bv)(x)=a(bv(x))=(ab)v(x)=((ab)v)(x).

---

## Identity scalar

1v=v1\mathbf{v} = \mathbf{v}1v=v

This is the “do nothing” scale factor.

In polynomials: $1\cdot p(x)=p(x)$.

In matrices: $1\cdot A=A$.

---

## Mini-checklist animation (guided pass/fail)

When testing “is this a vector space?”, use a consistent order:

1) **What is V?** (the set)

2) **What is F?** (the scalars)

3) **How are + and scalar multiplication defined?**

4) **Closure tests** (fast failure):

- •**u**+**v** ∈ V?
- •ava\mathbf{v}av ∈ V?

5) **Zero and inverse** (often fails in restricted sets):

- •Is there a zero object in V?
- •Is −**v** always in V?

6) **Distributivity + identity** (consistency)

**Interactive canvas idea:** Provide toggles for each axiom. For a candidate set (e.g., “nonnegative functions”), clicking “additive inverse” highlights a counterexample: pick f(x)=1f(x)=1f(x)=1 then show −f(x)=−1 not in the set.

This gives learners a reliable mental procedure instead of a memorized list.

## Application/Connection: Why Vector Spaces Unlock Linear Independence

### Why vector spaces are the stage for linear algebra

Most linear algebra concepts are really about *linear combinations*:

a1v1+⋯+akvka\_1\mathbf{v}\_1 + \cdots + a\_k\mathbf{v}\_ka1​v1​+⋯+ak​vk​

To even talk about this expression, you need:

- •addition to combine vectors,
- •scalar multiplication to apply coefficients,
- •closure so the result stays in your world,
- •distributivity so algebraic manipulation is valid.

That’s exactly what the vector space axioms guarantee.

---

## Linear combinations are “mixing recipes”

Think of **v**₁, **v**₂ as ingredients and scalars as amounts.

If V is a vector space, then every recipe output is still a valid element of V.

### Example: polynomial mixing

Let V=P2V=P\_2V=P2​ (polynomials degree ≤ 2 over R\mathbb{R}R). Take

p1(x)=1p\_1(x)=1p1​(x)=1, p2(x)=xp\_2(x)=xp2​(x)=x, p3(x)=x2p\_3(x)=x^2p3​(x)=x2.

A linear combination is

a⋅1+b⋅x+c⋅x2a\cdot 1 + b\cdot x + c\cdot x^2a⋅1+b⋅x+c⋅x2

which is exactly “an arbitrary quadratic.”

So the vector space structure explains why $

\{1, x, x^2\}cangenerateallof can generate all of cangenerateallofP\_2$.

---

## Connection to linear independence (the next node)

The next concept—**linear independence**—asks whether a set of vectors contains redundancy.

A set {v1,…,vk}\{\mathbf{v}\_1,\dots,\mathbf{v}\_k\}{v1​,…,vk​} is linearly independent if the only way to get the zero vector from a linear combination is the trivial way.

Formally (over field F):

a1v1+⋯+akvk=0⇒a1=⋯=ak=0.a\_1\mathbf{v}\_1 + \cdots + a\_k\mathbf{v}\_k = \mathbf{0} \Rightarrow a\_1=\cdots=a\_k=0.a1​v1​+⋯+ak​vk​=0⇒a1​=⋯=ak​=0.

This definition relies on:

- •the existence of **0**,
- •the ability to add and scale vectors,
- •distributive properties to rearrange equations.

So: **vector spaces are the rules of the game; linear independence is one of the key strategies.**

---

## Two non-geometry spaces you’ll see again

### 1) Function space (signals)

Let VVV be the set of continuous functions on [0,1], scalars F=RF=\mathbb{R}F=R.

- •Adding signals adds amplitudes.
- •Scaling changes volume/brightness.

Vector-space thinking leads directly to Fourier series, least squares, and projections.

### 2) Matrix space (data)

Let VVV be the set of all m×nm\times nm×n real matrices, scalars R\mathbb{R}R.

- •Addition combines datasets.
- •Scaling changes units.

This becomes central in machine learning: datasets, parameter matrices, and gradients live in vector spaces.

---

### A final habit to carry forward

Whenever you meet a new “vector-like” object (polynomials, functions, sequences, matrices), ask:

- •What is the zero element?
- •What does it mean to negate something?
- •Is closure obvious or subtle?

That habit will make the next nodes (linear independence, span, basis) feel natural instead of magical.

## Worked Examples (3)

### Worked Example 1: Is P₂ (polynomials of degree ≤ 2) a vector space over ℝ?

Let V = { p(x) : p is a real polynomial with degree ≤ 2 }. Let F = ℝ. Define addition and scalar multiplication in the usual way: (p+q)(x)=p(x)+q(x), and (ap)(x)=a·p(x). Decide whether V is a vector space over F.

1. Step 1: Identify what must be shown.

   We must verify:

   (1) (V,+) is an abelian group, and

   (2) scalar multiplication by ℝ satisfies closure and compatibility axioms.
2. Step 2: Check closure under addition.

   Take arbitrary p,q ∈ V.

   Write p(x)=a₂x²+a₁x+a₀ and q(x)=b₂x²+b₁x+b₀.

   Then

   (p+q)(x)=(a₂+b₂)x²+(a₁+b₁)x+(a₀+b₀).

   This is still degree ≤ 2, so p+q ∈ V.
3. Step 3: Check associativity and commutativity of addition.

   For any polynomials p,q,r, we have pointwise:

   ((p+q)+r)(x)=(p(x)+q(x))+r(x)=p(x)+(q(x)+r(x))=(p+(q+r))(x).

   Similarly p(x)+q(x)=q(x)+p(x) implies p+q=q+p.

   So associativity and commutativity hold.
4. Step 4: Find the additive identity.

   Let 0(x)=0 for all x (the zero polynomial).

   Then (p+0)(x)=p(x)+0=p(x), so p+0=p.

   Thus the additive identity exists and is in V.
5. Step 5: Check additive inverses.

   For p(x)=a₂x²+a₁x+a₀, define (−p)(x)=−a₂x²−a₁x−a₀.

   Then (p+(−p))(x)=0 for all x, so p+(−p)=0.

   Also −p still has degree ≤ 2, so −p ∈ V.
6. Step 6: Check closure under scalar multiplication.

   Take a ∈ ℝ and p(x)=a₂x²+a₁x+a₀.

   Then (ap)(x)=a·a₂x²+a·a₁x+a·a₀, still degree ≤ 2.

   So ap ∈ V.
7. Step 7: Check distributivity and scalar rules.

   For any a,b ∈ ℝ and p,q ∈ V, pointwise:

   (a(p+q))(x)=a(p(x)+q(x))=ap(x)+aq(x)=((ap)+(aq))(x).

   ((a+b)p)(x)=(a+b)p(x)=ap(x)+bp(x)=((ap)+(bp))(x).

   (ab)p(x)=a(bp(x)) and 1·p(x)=p(x).

   Therefore all compatibility axioms hold.

**Insight:** P₂ works because “degree ≤ 2” is stable under addition and scaling. Many near-misses fail only because the set isn’t closed (e.g., degree exactly 2, or monic polynomials).

### Worked Example 2: Is the set of nonnegative continuous functions a vector space?

Let V = { f : [0,1] → ℝ | f is continuous and f(x) ≥ 0 for all x }. Let F = ℝ. Operations are pointwise: (f+g)(x)=f(x)+g(x) and (af)(x)=a·f(x). Determine if V is a vector space over ℝ.

1. Step 1: Try the fastest failure checks (closure + inverses).

   Because V has an inequality restriction (f(x) ≥ 0), additive inverses are suspicious.
2. Step 2: Check closure under addition.

   Take f,g ∈ V.

   For each x, f(x) ≥ 0 and g(x) ≥ 0, so f(x)+g(x) ≥ 0.

   Also f+g is continuous.

   Thus f+g ∈ V. So addition closure passes.
3. Step 3: Check closure under scalar multiplication.

   Take a ∈ ℝ and f ∈ V.

   If a ≥ 0, then af(x) ≥ 0, so af ∈ V.

   But the axiom requires closure for all scalars a ∈ ℝ, including negative scalars.
4. Step 4: Produce a counterexample with a negative scalar.

   Let f(x)=1 (constant function). Then f ∈ V.

   Take a=−1.

   Then (af)(x)=−1 for all x, which is not ≥ 0.

   So af ∉ V.

   Scalar multiplication closure fails.
5. Step 5: (Optional) Note the additive inverse failure as well.

   If f(x)=1 ∈ V, then −f(x)=−1 is not in V.

   So additive inverses fail too.

**Insight:** Sets defined by “≥ 0” constraints usually fail to be vector spaces over ℝ because you can’t multiply by negative scalars and stay inside the set.

### Worked Example 3: Is ℝ² with a weird addition a vector space?

Let V = ℝ² and F = ℝ. Define scalar multiplication as usual: a(x,y)=(ax,ay). But define addition by (x₁,y₁) ⊕ (x₂,y₂) = (x₁+x₂+1, y₁+y₂). Is (V, ⊕, ·) a vector space over ℝ?

1. Step 1: Check closure under ⊕.

   For any (x₁,y₁),(x₂,y₂) ∈ ℝ², we get (x₁+x₂+1, y₁+y₂) ∈ ℝ².

   So closure under addition holds.
2. Step 2: Find the additive identity with respect to ⊕.

   We need an element **e**=(e₁,e₂) such that (x,y) ⊕ (e₁,e₂) = (x,y).

   Compute:

   (x,y) ⊕ (e₁,e₂) = (x+e₁+1, y+e₂).

   Set equal to (x,y):

   x+e₁+1=x ⇒ e₁=−1,

   y+e₂=y ⇒ e₂=0.

   So the identity would be **e**=(−1,0), which exists in V.
3. Step 3: Check compatibility with scalar multiplication (likely failure).

   A key axiom is distributivity:

   a( **u** ⊕ **v** ) should equal a**u** ⊕ a**v**.

   Let **u**=(0,0), **v**=(0,0), a=2.

   Compute left side:

   **u** ⊕ **v** = (0+0+1,0+0)=(1,0).

   Then a(**u** ⊕ **v**) = 2(1,0)=(2,0).

   Compute right side:

   a**u**=(0,0), a**v**=(0,0).

   Then a**u** ⊕ a**v** = (0+0+1,0+0)=(1,0).

   Left ≠ right, since (2,0) ≠ (1,0).
4. Step 4: Conclude.

   Distributivity fails, so this structure is not a vector space.

**Insight:** You can invent an “addition” that’s closed and even has an identity, but the moment distributivity fails, linear combinations stop behaving predictably. Distributivity is a core integrity check.

## Key Takeaways

- ✓

  A vector space is a set V with addition and scalar multiplication over a field F that satisfy specific axioms.
- ✓

  Addition must make V an abelian group: closure, associativity, commutativity, zero element, and additive inverses.
- ✓

  Scalar multiplication must be closed and must interact with addition via distributivity and associativity: a(u+v)=au+av, (a+b)v=av+bv, (ab)v=a(bv), 1v=v.
- ✓

  The “zero vector” depends on the space (zero polynomial, zero function, zero matrix), not just (0,0).
- ✓

  Many non-geometry sets are vector spaces (polynomials ≤ n, all functions of a certain type), and many almost-examples fail due to closure or inverses.
- ✓

  Inequality-restricted sets (like nonnegative functions) typically fail because negative scaling breaks closure.
- ✓

  A reliable checklist (define V, F, operations; test closure, zero/inverses, distributivity) beats memorizing axioms in isolation.
- ✓

  Vector spaces are the foundation that makes linear combinations—and thus linear independence—well-defined.

## Common Mistakes

- ✗

  Forgetting to specify the field F (scalars) and assuming it’s always ℝ; the choice of F matters.
- ✗

  Assuming the zero vector is always (0,0) instead of identifying the additive identity in the given space.
- ✗

  Checking a couple axioms (like closure) but skipping distributivity/identity, where many custom operations fail.
- ✗

  Using sets that are not closed (e.g., degree exactly 2 polynomials, positive-length vectors, invertible matrices under usual addition) and missing the closure failure.

## Practice

easy

Let V be the set of all real 2×2 matrices. With usual matrix addition and scalar multiplication over ℝ, is V a vector space?

**Hint:** Ask: is the sum of two 2×2 matrices still 2×2? Is scalar multiple still 2×2? Do usual arithmetic properties hold entrywise?

Show solution

Yes. Closure holds because adding/scaling entrywise keeps you in 2×2 matrices. The zero vector is the zero matrix. Additive inverses are negatives of matrices. Distributivity and scalar associativity hold entrywise, inherited from ℝ.

medium

Let V = { (x,y) ∈ ℝ² : x + y = 1 } with usual addition and scalar multiplication over ℝ. Is V a vector space?

**Hint:** Test closure under addition using two generic points satisfying x+y=1.

Show solution

No. Take **u**=(1,0) and **v**=(0,1). Both satisfy x+y=1. But **u**+**v**=(1,1), and 1+1=2 ≠ 1, so closure under addition fails.

medium

Let V be the set of all polynomials with real coefficients that satisfy p(0)=0. With usual addition and scalar multiplication over ℝ, is V a vector space?

**Hint:** Check closure by evaluating (p+q)(0) and (ap)(0). Identify the zero element and additive inverses.

Show solution

Yes. If p(0)=0 and q(0)=0, then (p+q)(0)=p(0)+q(0)=0, so closed under addition. If a∈ℝ, then (ap)(0)=a·p(0)=0, so closed under scalar multiplication. Zero polynomial satisfies p(0)=0 and serves as identity; inverses −p also satisfy (−p)(0)=−p(0)=0. Other axioms follow from usual polynomial arithmetic.

## Connections

Next up: [Linear Independence](/tech-tree/linear-independence/)

Related future nodes you’ll likely encounter:

- •Span and Basis (built from linear combinations)
- •Subspaces (sets inside a vector space that are themselves vector spaces)
- •Linear Transformations (functions that preserve addition and scaling)

Quality: A (4.4/5)

[← back to tree](/tech-tree/)[browse all →](/tech-tree/inventory/)
