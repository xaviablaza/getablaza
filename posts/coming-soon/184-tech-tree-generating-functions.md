---
title: Generating Functions
description: Power series encoding sequences. Solving counting problems.
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
generated_by: templeton-deep-copy-import
permalink: /tech-tree/generating-functions/
---

[←Back to Tech Tree](/tech-tree/)

[inventory](/tech-tree/inventory/)[coverage](/tech-tree/coverage/)

# Generating Functions

Discrete MathDifficulty: ★★★☆☆Depth: 4Unlocks: 0

Power series encoding sequences. Solving counting problems.

## Interactive Visualization

⏮◀◀▶▶STEP0.25x1xZOOM

t=0s

## Core Concepts

- -Ordinary generating function: represent a sequence (a\_n) as the formal power series A(x) = sum\_{n>=0} a\_n x^n.
- -Coefficient extraction: recover sequence terms from the series via the coefficient-of-x^n operation (a\_n = coefficient\_of\_x^n(A(x))).
- -Algebraic reduction: convert counting problems or recurrence relations into algebraic equations for generating functions to solve for closed forms or sequence values.

## Key Symbols & Notation

A(x) = sum\_{n>=0} a\_n x^n (ordinary generating function)

## Essential Relationships

- -Algebra <-> sequence: algebraic operations on generating functions correspond to sequence operations (Cauchy product = convolution; multiplication by x^k = index shift) and rational generating functions correspond to linear recurrences with constant coefficients.

## Prerequisites (2)

[Sequences5 atoms](/tech-tree/sequences/)[Recurrence Relations5 atoms](/tech-tree/recurrence-relations/)

Advanced Learning Details

### Graph Position

52

Depth Cost

0

Fan-Out (ROI)

0

Bottleneck Score

4

Chain Length

### Cognitive Load

5

Atomic Elements

27

Total Elements

L1

Percentile Level

L3

Atomic Level

### All Concepts (11)

- - Ordinary generating function (OGF): representing a sequence (a\_n) by the formal power series A(x)=∑\_{n≥0} a\_n x^n
- - Formal power series viewpoint: treat generating functions algebraically (manipulate coefficients) without requiring analytic convergence or radius of convergence
- - Coefficient extraction: the operation of retrieving a\_n as the coefficient of x^n in A(x), often written [x^n]A(x)
- - Cauchy product (convolution) of sequences: coefficients of the product of two GFs given by discrete convolution of the sequences
- - Index shift by multiplication: multiplying a GF by x^k shifts the sequence indices (x^k A(x) corresponds to inserting k leading zeros / shifting a\_n→a\_{n-k})
- - Geometric-series GF: 1/(1-x) as the generating function for the constant sequence 1, and related closed forms for simple sequences (e.g., 1/(1-x)^2 for the sequence n+1)
- - Algebraic manipulation of GFs to solve problems: formulating an algebraic equation for a GF from a recurrence or combinatorial description and solving that equation for A(x)
- - Rational generating functions: GFs that are ratios of polynomials, typically arising from linear recurrences with constant coefficients
- - Partial-fraction (and related) coefficient-extraction techniques: decomposing a rational GF to obtain an explicit formula for a\_n
- - Translation of basic combinatorial constructions into GF operations (disjoint union → sum of GFs; ordered product → product of GFs; sequence/zero-or-more → 1/(1−A(x)))
- - Using GFs to model counting problems: encoding combinatorial counting constraints as algebraic operations on series to derive counts

### Teaching Strategy

Quick unlock - significant prerequisite investment but simple final step. Verify prerequisites first.

A generating function is a “sequence in disguise”: you pack the entire list (a₀, a₁, a₂, …) into a single algebraic object A(x). Then you solve counting problems by doing algebra on A(x) and reading answers back out as coefficients.

TL;DR:

An ordinary generating function (OGF) encodes a sequence (aₙ) as A(x) = ∑ₙ≥0 aₙxⁿ. The operator [xⁿ]A(x) extracts the coefficient aₙ. The main power move: algebra on series corresponds to combinatorics on sequences—especially shifts and products (convolution). This turns recurrences and counting constructions into solvable equations for A(x).

## What Is a Generating Function?

### Why we bother (motivation before formulas)

You already know two common ways to describe a sequence:

1. 1)**Explicitly**: “an=3⋅2naₙ = 3·2ⁿan​=3⋅2n.”
2. 2)**Recursively**: “an=2an−1aₙ = 2a\_{n-1}an​=2an−1​ with a0=3a₀=3a0​=3.”

Generating functions add a third option: describe the sequence as a **single formal power series** and then use algebra to manipulate it. The surprise is that many sequence operations (shifting, summing, combining choices) become *simple algebra*.

This is especially useful for **counting**: when you build objects out of parts, generating functions let you multiply the “part choices” and automatically produce counts for each size.

### Definition: ordinary generating function (OGF)

Given a sequence (an)n≥0(aₙ)\_{n≥0}(an​)n≥0​, its **ordinary generating function** is

A(x)=∑n≥0anxn.A(x) = \sum\_{n\ge 0} a\_n x^n.A(x)=n≥0∑​an​xn.

- •Think of xxx as a bookkeeping variable that tracks “size” (like number of steps, total sum, total length).
- •Think of anaₙan​ as “how many objects have size nnn.”

Important: in discrete math we often treat A(x)A(x)A(x) as a **formal power series**. That means we’re not worried (at first) about whether the series converges for a numeric value of xxx. We’re using it as an algebraic container for coefficients.

### Coefficient extraction

To recover the original sequence, we use the coefficient operator:

an=[xn]A(x).a\_n = [x^n]A(x).an​=[xn]A(x).

Read [xn]A(x)[x^n]A(x)[xn]A(x) as: “the coefficient of xnxⁿxn in the series A(x)A(x)A(x).”

Example:

If A(x)=2+0x+5x2+7x3+⋯A(x)=2 + 0x + 5x^2 + 7x^3 + \cdotsA(x)=2+0x+5x2+7x3+⋯, then

- •[x0]A(x)=2[x^0]A(x)=2[x0]A(x)=2
- •[x1]A(x)=0[x^1]A(x)=0[x1]A(x)=0
- •[x2]A(x)=5[x^2]A(x)=5[x2]A(x)=5
- •[x3]A(x)=7[x^3]A(x)=7[x3]A(x)=7

### One minute of intuition: why a power series encodes a sequence

Because powers of xxx act like “bins” labeled by nnn:

- •The x0x^0x0 bin stores a0a₀a0​.
- •The x1x^1x1 bin stores a1a₁a1​.
- •The x2x^2x2 bin stores a2a₂a2​.

When you add or multiply series, the bins combine in structured ways—and those structures match common combinatorial constructions.

### Quick examples of OGFs you should recognize

1) Constant 1’s:

∑n≥0xn=1+x+x2+x3+⋯=11−x.\sum\_{n\ge0} x^n = 1 + x + x^2 + x^3 + \cdots = \frac{1}{1-x}.n≥0∑​xn=1+x+x2+x3+⋯=1−x1​.

So the sequence (1,1,1,1,… )(1,1,1,1,\dots)(1,1,1,1,…) has OGF 11−x\frac{1}{1-x}1−x1​.

2) Geometric weights (cn)(c^n)(cn):

∑n≥0cnxn=11−cx.\sum\_{n\ge0} c^n x^n = \frac{1}{1-cx}.n≥0∑​cnxn=1−cx1​.

So (1,c,c2,… )(1,c,c^2,\dots)(1,c,c2,…) has OGF 11−cx\frac{1}{1-cx}1−cx1​.

3) A shifted sequence:

If A(x)=∑n≥0anxnA(x)=\sum\_{n\ge0}aₙxⁿA(x)=∑n≥0​an​xn, then

xA(x)=∑n≥0anxn+1=∑n≥1an−1xn.xA(x)=\sum\_{n\ge0}a\_n x^{n+1}=\sum\_{n\ge1}a\_{n-1}x^n.xA(x)=n≥0∑​an​xn+1=n≥1∑​an−1​xn.

So multiplying by xxx shifts coefficients to the right.

That “shift = multiply by xxx” fact will be one of our core tools.

## Core Mechanic 1: Coefficient Extraction, Shifts, and Simple Algebra

### Why this matters

Most generating-function solutions follow a pattern:

1. 1)Express a recurrence or a counting construction as an equation involving A(x)A(x)A(x).
2. 2)Solve that equation with algebra.
3. 3)Extract [xn][x^n][xn] from the result.

To do step 1 correctly, you need fluency with coefficient extraction and shifts.

### The coefficient operator behaves like a “read-off” function

The operator [xn][x^n][xn] is linear:

[xn](F(x)+G(x))=[xn]F(x)+[xn]G(x),[x^n](F(x)+G(x)) = [x^n]F(x) + [x^n]G(x),[xn](F(x)+G(x))=[xn]F(x)+[xn]G(x),

and constants pull out:

[xn](cF(x))=c [xn]F(x).[x^n](cF(x)) = c\,[x^n]F(x).[xn](cF(x))=c[xn]F(x).

These properties let you extract terms after you do algebra.

### Shifts: multiplying by x moves the sequence

Let

A(x)=∑n≥0anxn.A(x)=\sum\_{n\ge0}a\_nx^n.A(x)=n≥0∑​an​xn.

Then:

- •**Right shift** (delay by 1):

xA(x)=∑n≥0anxn+1=∑n≥1an−1xn.xA(x)=\sum\_{n\ge0}a\_nx^{n+1}=\sum\_{n\ge1}a\_{n-1}x^n.xA(x)=n≥0∑​an​xn+1=n≥1∑​an−1​xn.

So

[xn](xA(x))=an−1(n≥1).[x^n](xA(x)) = a\_{n-1}\quad (n\ge1).[xn](xA(x))=an−1​(n≥1).

- •**Right shift by k**:

xkA(x)=∑n≥kan−kxn.x^kA(x)=\sum\_{n\ge k} a\_{n-k}x^n.xkA(x)=n≥k∑​an−k​xn.

So

[xn](xkA(x))=an−k(n≥k).[x^n](x^kA(x)) = a\_{n-k}\quad (n\ge k).[xn](xkA(x))=an−k​(n≥k).

- •**Left shift** is slightly trickier because you lose initial terms. Observe:

A(x)−a0x=∑n≥1anxn−1=∑n≥0an+1xn.\frac{A(x)-a\_0}{x} = \sum\_{n\ge1}a\_n x^{n-1} = \sum\_{n\ge0} a\_{n+1} x^n.xA(x)−a0​​=n≥1∑​an​xn−1=n≥0∑​an+1​xn.

So

[xn]A(x)−a0x=an+1.[x^n]\frac{A(x)-a\_0}{x} = a\_{n+1}.[xn]xA(x)−a0​​=an+1​.

This is the algebraic way to represent “drop the first term and shift left.”

### A small but crucial identity: summing a recurrence becomes multiplying by a power series

Suppose you have a recurrence like

an=an−1+1(n≥1),a0=0.a\_n = a\_{n-1} + 1 \quad (n\ge1),\qquad a\_0 = 0.an​=an−1​+1(n≥1),a0​=0.

If you multiply both sides by xnx^nxn and sum over n≥1n\ge1n≥1, you get

Left side:

∑n≥1anxn=A(x)−a0=A(x).\sum\_{n\ge1} a\_n x^n = A(x) - a\_0 = A(x).n≥1∑​an​xn=A(x)−a0​=A(x).

Right side:

∑n≥1an−1xn+∑n≥11⋅xn=x∑n≥1an−1xn−1+x1−x.\sum\_{n\ge1} a\_{n-1}x^n + \sum\_{n\ge1}1\cdot x^n = x\sum\_{n\ge1}a\_{n-1}x^{n-1} + \frac{x}{1-x}.n≥1∑​an−1​xn+n≥1∑​1⋅xn=xn≥1∑​an−1​xn−1+1−xx​.

But

∑n≥1an−1xn−1=∑m≥0amxm=A(x).\sum\_{n\ge1}a\_{n-1}x^{n-1} = \sum\_{m\ge0}a\_m x^m = A(x).n≥1∑​an−1​xn−1=m≥0∑​am​xm=A(x).

So the equation becomes

A(x)=xA(x)+x1−x.A(x) = xA(x) + \frac{x}{1-x}.A(x)=xA(x)+1−xx​.

Now solve:

A(x)(1−x)=x1−x⇒A(x)=x(1−x)2.A(x)(1-x) = \frac{x}{1-x}\quad\Rightarrow\quad A(x)=\frac{x}{(1-x)^2}.A(x)(1−x)=1−xx​⇒A(x)=(1−x)2x​.

Finally extract coefficients. A known expansion is

1(1−x)2=∑n≥0(n+1)xn,\frac{1}{(1-x)^2} = \sum\_{n\ge0}(n+1)x^n,(1−x)21​=n≥0∑​(n+1)xn,

so

A(x)=x∑n≥0(n+1)xn=∑n≥1nxn.A(x)=x\sum\_{n\ge0}(n+1)x^n = \sum\_{n\ge1} n x^n.A(x)=xn≥0∑​(n+1)xn=n≥1∑​nxn.

Thus an=na\_n = nan​=n (with a0=0a\_0=0a0​=0), matching the recurrence.

The point isn’t this easy recurrence—the point is the workflow:

- •turn shift terms into xA(x)xA(x)xA(x),
- •use a geometric series for simple sums,
- •solve algebraically,
- •read off coefficients.

### Partial fractions: how we often get closed forms

When A(x)A(x)A(x) is a rational function like

A(x)=P(x)Q(x),A(x)=\frac{P(x)}{Q(x)},A(x)=Q(x)P(x)​,

you can often decompose it into sums of terms like

C1−αx,C(1−αx)2,etc.\frac{C}{1-\alpha x},\quad \frac{C}{(1-\alpha x)^2},\quad\text{etc.}1−αxC​,(1−αx)2C​,etc.

Then coefficient extraction is straightforward because

11−αx=∑n≥0αnxn,\frac{1}{1-\alpha x} = \sum\_{n\ge0} \alpha^n x^n,1−αx1​=n≥0∑​αnxn,

and

1(1−αx)2=∑n≥0(n+1)αnxn.\frac{1}{(1-\alpha x)^2} = \sum\_{n\ge0} (n+1)\alpha^n x^n.(1−αx)21​=n≥0∑​(n+1)αnxn.

You don’t need to master every algebra trick yet; you do need to recognize that “rational generating function” usually means “closed form exists and can be extracted with algebra.”

## Core Mechanic 2: Products as Convolution (and a Visualization You Can Hold Onto)

### Why products show up in counting

When you build a combinatorial object by choosing **Part A** and **Part B** independently, the total size is usually the sum of sizes. Generating functions model exactly that: multiplying series adds exponents.

Let

A(x)=∑n≥0anxn,B(x)=∑n≥0bnxn.A(x)=\sum\_{n\ge0} a\_n x^n,\qquad B(x)=\sum\_{n\ge0} b\_n x^n.A(x)=n≥0∑​an​xn,B(x)=n≥0∑​bn​xn.

Then

A(x)B(x)=(∑i≥0aixi)(∑j≥0bjxj)=∑i≥0∑j≥0aibjxi+j.A(x)B(x)=\left(\sum\_{i\ge0} a\_i x^i\right)\left(\sum\_{j\ge0} b\_j x^j\right)
=\sum\_{i\ge0}\sum\_{j\ge0} a\_i b\_j x^{i+j}.A(x)B(x)=(i≥0∑​ai​xi)(j≥0∑​bj​xj)=i≥0∑​j≥0∑​ai​bj​xi+j.

Group terms by total exponent n=i+jn=i+jn=i+j:

A(x)B(x)=∑n≥0(∑i=0naibn−i)xn.A(x)B(x)=\sum\_{n\ge0}\left(\sum\_{i=0}^n a\_i b\_{n-i}\right)x^n.A(x)B(x)=n≥0∑​(i=0∑n​ai​bn−i​)xn.

So the coefficient rule is:

[xn](A(x)B(x))=∑i=0naibn−i.[x^n](A(x)B(x)) = \sum\_{i=0}^n a\_i b\_{n-i}.[xn](A(x)B(x))=i=0∑n​ai​bn−i​.

That inner sum is the **convolution** of sequences (an)(aₙ)(an​) and (bn)(bₙ)(bn​).

### Static visualization: coefficient extraction in a product

Think of a grid where rows are iii (from AAA) and columns are jjj (from BBB). Each cell contributes to exponent i+ji+ji+j.

```
            j=0      1       2       3       4
          ----------------------------------------
 i=0 |     a0b0    a0b1    a0b2    a0b3    a0b4
 i=1 |     a1b0    a1b1    a1b2    a1b3    a1b4
 i=2 |     a2b0    a2b1    a2b2    a2b3    a2b4
 i=3 |     a3b0    a3b1    a3b2    a3b3    a3b4
 i=4 |     a4b0    a4b1    a4b2    a4b3    a4b4
```

Cells on the same diagonal have the same sum i+ji+ji+j.

- •The diagonal for n=3n=3n=3 is:
- •(i,j)=(0,3)(i,j)=(0,3)(i,j)=(0,3) contributes a0b3a₀b₃a0​b3​
- •(1,2)(1,2)(1,2) contributes a1b2a₁b₂a1​b2​
- •(2,1)(2,1)(2,1) contributes a2b1a₂b₁a2​b1​
- •(3,0)(3,0)(3,0) contributes a3b0a₃b₀a3​b0​

So

[x3](A(x)B(x))=a0b3+a1b2+a2b1+a3b0.[x^3](A(x)B(x)) = a\_0b\_3 + a\_1b\_2 + a\_2b\_1 + a\_3b\_0.[x3](A(x)B(x))=a0​b3​+a1​b2​+a2​b1​+a3​b0​.

This diagonal-summing picture is the most important visualization for OGFs.

### Interpreting convolution combinatorially

If aia\_iai​ counts ways to build something of size iii (Part A), and bjb\_jbj​ counts ways to build something of size jjj (Part B), then:

- •Choose a split n=i+(n−i)n=i+(n-i)n=i+(n−i).
- •Choose Part A in aia\_iai​ ways.
- •Choose Part B in bn−ib\_{n-i}bn−i​ ways.
- •Multiply for independent choices, then sum over all splits.

That is exactly

∑i=0naibn−i.\sum\_{i=0}^n a\_i b\_{n-i}.i=0∑n​ai​bn−i​.

### A concrete “canvas-style” mental animation (shifts + product + read-off)

Even without an actual interactive widget, you can rehearse the same moves:

**Example goal:** compute [x4] (1+x+x2)(1+2x+3x2+4x3+⋯ )[x^4] \,(1 + x + x^2)(1 + 2x + 3x^2 + 4x^3 + \cdots)[x4](1+x+x2)(1+2x+3x2+4x3+⋯).

1) **Shift/limit idea:** the polynomial (1+x+x2)(1+x+x^2)(1+x+x2) says: take one copy of the second series, plus a copy shifted right by 1, plus a copy shifted right by 2.

2) Write that algebraically:

(1+x+x2)B(x)=B(x)+xB(x)+x2B(x).(1+x+x^2)B(x) = B(x) + xB(x) + x^2B(x).(1+x+x2)B(x)=B(x)+xB(x)+x2B(x).

3) Now “read off” coefficient of x4x^4x4:

- •From B(x)B(x)B(x) you need [x4]B(x)=5[x^4]B(x)=5[x4]B(x)=5 (since coefficients are 1,2,3,4,5,...)
- •From xB(x)xB(x)xB(x) you need [x3]B(x)=4[x^3]B(x)=4[x3]B(x)=4
- •From x2B(x)x^2B(x)x2B(x) you need [x2]B(x)=3[x^2]B(x)=3[x2]B(x)=3

So

[x4](1+x+x2)B(x)=5+4+3=12.[x^4](1+x+x^2)B(x) = 5 + 4 + 3 = 12.[x4](1+x+x2)B(x)=5+4+3=12.

This is the same as diagonal summing, but it highlights **shifts** explicitly: multiplication by xkx^kxk delays coefficients by kkk.

### Summary of the mechanics

- •Addition of generating functions: add counts for each size.
- •Multiplication: combine independent parts; coefficient becomes a convolution/diagonal sum.
- •Multiplying by xkx^kxk: shift sizes by kkk.

Once these feel natural, counting problems become “write the right product, then extract the coefficient.”

## Application/Connection: Solving Counting Problems and Recurrences with OGFs

### Two main use cases

Generating functions shine in two common scenarios:

1) **Counting via construction**: you build objects from components and want a formula for “# of objects of size n.”

2) **Solving recurrences**: you have anaₙan​ defined in terms of previous terms, and want a closed form.

We’ll do one of each, and point out the shared pattern.

---

## A) Counting by construction: compositions with restricted parts

A classic problem:

> How many ways are there to write nnn as an ordered sum of 1s and 2s?

This is the “stairs” problem: number of ways to climb nnn steps taking 1 or 2 at a time. You might know the answer is Fibonacci-like.

### Build the generating function

A single step can contribute size 1 or 2. So the OGF for “one step” is

S(x)=x+x2.S(x) = x + x^2.S(x)=x+x2.

A whole walk is **a sequence of steps** of any length: 0 steps, 1 step, 2 steps, …

- •0 steps contributes size 0, counted by 1.
- •1 step contributes S(x)S(x)S(x).
- •2 steps contributes S(x)2S(x)^2S(x)2.

So the total generating function is a geometric series in S(x)S(x)S(x):

W(x)=1+S(x)+S(x)2+S(x)3+⋯=11−S(x)=11−(x+x2).W(x) = 1 + S(x) + S(x)^2 + S(x)^3 + \cdots = \frac{1}{1 - S(x)} = \frac{1}{1 - (x+x^2)}.W(x)=1+S(x)+S(x)2+S(x)3+⋯=1−S(x)1​=1−(x+x2)1​.

Thus

W(x)=11−x−x2.W(x) = \frac{1}{1 - x - x^2}.W(x)=1−x−x21​.

Now [xn]W(x)[x^n]W(x)[xn]W(x) is the number of walks summing to nnn.

### Connection to recurrence automatically

If

W(x)=∑n≥0wnxn,W(x)=\sum\_{n\ge0} w\_n x^n,W(x)=n≥0∑​wn​xn,

then the identity

(1−x−x2)W(x)=1(1 - x - x^2)W(x)=1(1−x−x2)W(x)=1

implies, by matching coefficients, that for n≥2n\ge2n≥2:

wn−wn−1−wn−2=0⇒wn=wn−1+wn−2.w\_n - w\_{n-1} - w\_{n-2} = 0\quad\Rightarrow\quad w\_n = w\_{n-1} + w\_{n-2}.wn​−wn−1​−wn−2​=0⇒wn​=wn−1​+wn−2​.

So the recurrence drops out of the algebra.

This is a key theme: **a rational OGF often corresponds to a linear recurrence with constant coefficients**, and vice versa.

---

## B) Solving a recurrence directly with OGFs

Suppose you have a recurrence:

an=3an−1+2(n≥1),a0=1.a\_n = 3a\_{n-1} + 2\quad(n\ge1),\qquad a\_0=1.an​=3an−1​+2(n≥1),a0​=1.

You can solve this with characteristic equations, but let’s practice the OGF method because it generalizes well.

Let

A(x)=∑n≥0anxn.A(x)=\sum\_{n\ge0}a\_n x^n.A(x)=n≥0∑​an​xn.

Multiply the recurrence by xnx^nxn and sum over n≥1n\ge1n≥1:

Left:

∑n≥1anxn=A(x)−a0=A(x)−1.\sum\_{n\ge1} a\_n x^n = A(x)-a\_0 = A(x)-1.n≥1∑​an​xn=A(x)−a0​=A(x)−1.

Right:

∑n≥13an−1xn+∑n≥12xn.\sum\_{n\ge1} 3a\_{n-1}x^n + \sum\_{n\ge1} 2x^n.n≥1∑​3an−1​xn+n≥1∑​2xn.

Handle each term:

- •For the shifted term:

∑n≥13an−1xn=3x∑n≥1an−1xn−1=3xA(x).\sum\_{n\ge1} 3a\_{n-1}x^n = 3x\sum\_{n\ge1} a\_{n-1}x^{n-1} = 3xA(x).n≥1∑​3an−1​xn=3xn≥1∑​an−1​xn−1=3xA(x).

- •For the constant forcing term:

∑n≥12xn=2⋅x1−x.\sum\_{n\ge1}2x^n = 2\cdot \frac{x}{1-x}.n≥1∑​2xn=2⋅1−xx​.

So we get an algebraic equation:

A(x)−1=3xA(x)+2x1−x.A(x)-1 = 3xA(x) + 2\frac{x}{1-x}.A(x)−1=3xA(x)+21−xx​.

Solve for A(x)A(x)A(x):

A(x)(1−3x)=1+2x1−x.A(x)(1-3x) = 1 + \frac{2x}{1-x}.A(x)(1−3x)=1+1−x2x​.

Put the right side over a common denominator:

1+2x1−x=1−x1−x+2x1−x=1+x1−x.1 + \frac{2x}{1-x} = \frac{1-x}{1-x} + \frac{2x}{1-x} = \frac{1+x}{1-x}.1+1−x2x​=1−x1−x​+1−x2x​=1−x1+x​.

So

A(x)=1+x(1−x)(1−3x).A(x)= \frac{1+x}{(1-x)(1-3x)}.A(x)=(1−x)(1−3x)1+x​.

Now do partial fractions:

Assume

1+x(1−x)(1−3x)=C1−x+D1−3x.\frac{1+x}{(1-x)(1-3x)} = \frac{C}{1-x} + \frac{D}{1-3x}.(1−x)(1−3x)1+x​=1−xC​+1−3xD​.

Then

1+x=C(1−3x)+D(1−x)=(C+D)+(−3C−D)x.1+x = C(1-3x) + D(1-x) = (C+D) + (-3C-D)x.1+x=C(1−3x)+D(1−x)=(C+D)+(−3C−D)x.

Match coefficients:

- •Constant: C+D=1C+D = 1C+D=1
- •xxx coefficient: −3C−D=1-3C - D = 1−3C−D=1

Solve:

From D=1−CD=1-CD=1−C:

−3C−(1−C)=1⇒−2C−1=1⇒C=−1.-3C-(1-C)=1 \Rightarrow -2C - 1 = 1 \Rightarrow C=-1.−3C−(1−C)=1⇒−2C−1=1⇒C=−1.

Then D=1−(−1)=2D=1-(-1)=2D=1−(−1)=2.

So

A(x)=−11−x+21−3x.A(x)=\frac{-1}{1-x} + \frac{2}{1-3x}.A(x)=1−x−1​+1−3x2​.

Extract coefficients using geometric expansions:

11−x=∑n≥0xn,11−3x=∑n≥03nxn.\frac{1}{1-x}=\sum\_{n\ge0}x^n,\qquad \frac{1}{1-3x}=\sum\_{n\ge0}3^n x^n.1−x1​=n≥0∑​xn,1−3x1​=n≥0∑​3nxn.

Thus

A(x)=∑n≥0(−1) xn+∑n≥02⋅3nxn=∑n≥0(−1+2⋅3n)xn.A(x)=\sum\_{n\ge0}(-1)\,x^n + \sum\_{n\ge0} 2\cdot 3^n x^n = \sum\_{n\ge0} ( -1 + 2\cdot 3^n )x^n.A(x)=n≥0∑​(−1)xn+n≥0∑​2⋅3nxn=n≥0∑​(−1+2⋅3n)xn.

So

an=−1+2⋅3n.a\_n = -1 + 2\cdot 3^n.an​=−1+2⋅3n.

Check: a0=−1+2=1a₀=-1+2=1a0​=−1+2=1 ok; and a1=−1+6=5a₁=-1+6=5a1​=−1+6=5, while recurrence gives $3·1+2=5$.

---

## What to remember about the “reduction” step

The core skill is converting “sequence language” into “A(x)A(x)A(x) algebra.” A helpful cheat sheet:

| Sequence statement | Generating-function translation |
| --- | --- |
| ∑n≥0anxn\sum\_{n\ge0} a\_n x^n∑n≥0​an​xn | A(x)A(x)A(x) |
| ∑n≥1anxn\sum\_{n\ge1} a\_n x^n∑n≥1​an​xn | A(x)−a0A(x) - a\_0A(x)−a0​ |
| ∑n≥1an−1xn\sum\_{n\ge1} a\_{n-1} x^n∑n≥1​an−1​xn | xA(x)xA(x)xA(x) |
| Add independent options | add OGFs |
| Concatenate independent parts | multiply OGFs (convolution) |
| Any number of repeats of a component with OGF C(x)C(x)C(x) | $1 + C + C^2+\cdots = 1/(1-C)$ |

If you can do these translations slowly and correctly, you can solve a wide range of counting and recurrence problems.

---

## Connections you’re about to unlock

From here, generating functions connect naturally to:

- •solving more complex linear recurrences (including Fibonacci closed forms),
- •more expressive generating functions (exponential generating functions),
- •analytic techniques (asymptotics) when you *do* care about convergence.

But the foundation is what you’ve learned here: **encode → manipulate → extract**.

## Worked Examples (3)

### Coefficient extraction in a product (convolution by diagonals)

Let A(x) = 1 + 2x + 3x² and B(x) = 1 + x + x² + x³ + … = 1/(1−x). Find [x⁴] A(x)B(x).

1. Write the coefficient rule:

   [x⁴](A·B) = ∑\_{i=0}^4 a\_i b\_{4−i}, where a\_i=[x^i]A and b\_j=[x^j]B.
2. List coefficients:

   A(x)=1+2x+3x² so a₀=1, a₁=2, a₂=3, and a₃=a₄=0.

   B(x)=1/(1−x)=∑\_{n≥0}x^n so b\_j=1 for all j≥0.
3. Compute the convolution sum:

   [x⁴](A·B)=a₀b₄ + a₁b₃ + a₂b₂ + a₃b₁ + a₄b₀

   = 1·1 + 2·1 + 3·1 + 0·1 + 0·1

   = 6.
4. Optional “shift” viewpoint:

   A(x)B(x) = (1+2x+3x²)B(x) = B(x) + 2xB(x) + 3x²B(x).

   Now [x⁴] of that is b₄ + 2b₃ + 3b₂ = 1 + 2 + 3 = 6.

**Insight:** Products of OGFs turn into diagonal sums: to make x⁴, you can split 4 as i+(4−i). This is the algebraic mirror of “choose a size i from A and the rest from B.”

### Solve a recurrence with an OGF (linear, constant coefficients, non-homogeneous)

Solve aₙ = 2aₙ₋₁ + 3 for n≥1 with a₀ = 0 using generating functions.

1. Define the generating function:

   A(x)=∑\_{n≥0} aₙ xⁿ.
2. Multiply the recurrence by xⁿ and sum for n≥1:

   ∑\_{n≥1} aₙ xⁿ = ∑\_{n≥1} (2aₙ₋₁ + 3)xⁿ.
3. Translate each sum into A(x):

   Left: ∑\_{n≥1} aₙ xⁿ = A(x) − a₀ = A(x).

   Right first term: ∑\_{n≥1} 2aₙ₋₁ xⁿ = 2x∑\_{n≥1} aₙ₋₁ xⁿ⁻¹ = 2xA(x).

   Right second term: ∑\_{n≥1} 3xⁿ = 3·x/(1−x).
4. Obtain an algebraic equation:

   A(x) = 2xA(x) + 3x/(1−x).
5. Solve for A(x):

   A(x)(1−2x) = 3x/(1−x)

   ⇒ A(x) = 3x / ((1−x)(1−2x)).
6. Partial fractions:

   Assume 3x/((1−x)(1−2x)) = C/(1−x) + D/(1−2x).

   Then 3x = C(1−2x) + D(1−x) = (C+D) + (−2C−D)x.

   Match coefficients:

   C + D = 0

   −2C − D = 3

   Solve: from D=−C, −2C + C = 3 ⇒ −C=3 ⇒ C=−3, D=3.
7. Expand and extract coefficients:

   A(x)= −3/(1−x) + 3/(1−2x)

   = −3∑\_{n≥0} xⁿ + 3∑\_{n≥0} 2ⁿ xⁿ

   = ∑\_{n≥0} (3·2ⁿ − 3)xⁿ.

   So aₙ = 3·2ⁿ − 3.

**Insight:** The recurrence becomes a solvable algebra problem because shifts like aₙ₋₁ translate to xA(x). Non-homogeneous terms (like +3) translate to simple known series (like x/(1−x)).

### Counting with a construction: number of solutions to i + j = n with bounds

Count the number of integer pairs (i,j) with i≥0, j≥0, i≤2, and i+j=n. Use generating functions to derive a formula for the count as a function of n.

1. Translate choices into OGFs:

   The variable i can be 0,1,2. So its OGF is I(x)=1 + x + x².

   The variable j can be any nonnegative integer. So its OGF is J(x)=1 + x + x² + … = 1/(1−x).
2. Combine independent choices by multiplication:

   Total OGF is T(x)=I(x)J(x) = (1+x+x²)/(1−x).
3. Extract coefficient:

   The count we want is tₙ = [xⁿ]T(x).
4. Use the “shifted copies” view:

   T(x) = (1+x+x²)J(x) = J(x) + xJ(x) + x²J(x).
5. Read off coefficients:

   Since [xⁿ]J(x)=1 for all n≥0,

   [xⁿ]J(x)=1,

   [xⁿ]xJ(x)=[xⁿ⁻¹]J(x)=1 for n≥1 (and 0 for n=0),

   [xⁿ]x²J(x)=[xⁿ⁻²]J(x)=1 for n≥2 (and 0 for n=0,1).
6. Combine cases:

   If n=0: t₀ = 1.

   If n=1: t₁ = 1+1 = 2.

   If n≥2: tₙ = 1+1+1 = 3.
7. State the result:

   There are 1 solution for n=0, 2 solutions for n=1, and 3 solutions for all n≥2.

**Insight:** The product encodes all splits n=i+j, but the bounded i means only three diagonals contribute—visually: only i=0,1,2 rows exist, so each diagonal has at most three cells.

## Key Takeaways

- ✓

  An ordinary generating function encodes a sequence as A(x)=∑ₙ≥0 aₙxⁿ; it’s a formal container for coefficients.
- ✓

  Coefficient extraction is written aₙ = [xⁿ]A(x). The operator [xⁿ] is linear and is how you “read answers.”
- ✓

  Multiplying by x^k shifts the sequence: [xⁿ](x^kA(x)) = aₙ₋ₖ (for n≥k).
- ✓

  Products correspond to convolution: [xⁿ](A·B)=∑\_{i=0}^n a\_i b\_{n−i}. This matches “split n into i+(n−i).”
- ✓

  Counting via construction often becomes “write a product/series, then extract [xⁿ].”
- ✓

  Recurrences become algebraic equations in A(x) once you multiply by xⁿ and sum over n; shift terms turn into xA(x)-style expressions.
- ✓

  Rational generating functions typically lead to closed forms via partial fractions and geometric-series expansions.

## Common Mistakes

- ✗

  Forgetting to subtract initial terms when converting ∑\_{n≥1} aₙxⁿ into A(x)−a₀ (or more generally handling offsets).
- ✗

  Mixing up the shift direction: xA(x) shifts coefficients right (delays indices), while (A(x)−a₀)/x shifts left.
- ✗

  Treating a formal power series as a numeric function too early (worrying about convergence instead of coefficient algebra).
- ✗

  When multiplying series, forgetting that coefficients convolve (diagonal sums) and incorrectly multiplying term-by-term.

## Practice

easy

Let A(x)=∑ₙ≥0 aₙxⁿ. Express the generating function for the shifted sequence bₙ=aₙ₊₂ in terms of A(x), a₀, and a₁.

**Hint:** First remove the first two terms from A(x), then divide by x² to shift left by 2.

Show solution

We have A(x)=a₀ + a₁x + ∑\_{n≥2} aₙxⁿ.

So A(x)−a₀−a₁x = ∑\_{n≥2} aₙxⁿ.

Divide by x²:

(A(x)−a₀−a₁x)/x² = ∑\_{n≥2} aₙ x^{n−2} = ∑\_{m≥0} a\_{m+2} x^m.

Thus B(x)=∑\_{n≥0} bₙxⁿ = (A(x)−a₀−a₁x)/x².

medium

Compute [x⁵] (1 + x + x² + x³) · 1/(1−x). Interpret your answer as a counting statement.

**Hint:** Use the shift idea: (1+x+x²+x³)J(x)=J + xJ + x²J + x³J where J=1/(1−x).

Show solution

Let J(x)=1/(1−x)=∑\_{n≥0}xⁿ so [x^k]J(x)=1 for k≥0.

Then T(x)=(1+x+x²+x³)J(x)=J + xJ + x²J + x³J.

[x⁵]T = [x⁵]J + [x⁴]J + [x³]J + [x²]J = 1+1+1+1=4.

Counting interpretation: number of pairs (i,j) with i∈{0,1,2,3}, j≥0, and i+j=5. There are 4 such pairs: (0,5),(1,4),(2,3),(3,2).

hard

Let a₀=1 and for n≥1, aₙ = aₙ₋₁ + 2aₙ₋₂ (assume this holds for n≥2). Use OGFs to find a closed form for aₙ.

**Hint:** Multiply by xⁿ and sum; you’ll get an equation involving A(x), xA(x), and x²A(x). Solve for A(x) and use partial fractions by factoring the denominator 1−x−2x².

Show solution

Let A(x)=∑\_{n≥0} aₙxⁿ. The recurrence for n≥2 is aₙ − aₙ₋₁ − 2aₙ₋₂ = 0.

Sum from n=2 to ∞ after multiplying by xⁿ:

∑\_{n≥2} aₙxⁿ − ∑\_{n≥2} aₙ₋₁xⁿ − 2∑\_{n≥2} aₙ₋₂xⁿ = 0.

Translate:

∑\_{n≥2} aₙxⁿ = A(x) − a₀ − a₁x.

∑\_{n≥2} aₙ₋₁xⁿ = x∑\_{n≥2} aₙ₋₁x^{n−1} = x(A(x) − a₀).

∑\_{n≥2} aₙ₋₂xⁿ = x²∑\_{n≥2} aₙ₋₂x^{n−2} = x²A(x).

So:

(A − a₀ − a₁x) − x(A − a₀) − 2x²A = 0.

Plug a₀=1. Also compute a₁ from the recurrence base; using a₁ = a₀ + 2a\_{−1} is not valid, so we need a₁ given or inferable. If we interpret the problem as also giving a₁=1 (common default), then proceed; otherwise the closed form depends on a₁.

Assuming a₁=1:

A − 1 − x − xA + x − 2x²A = 0

⇒ A(1 − x − 2x²) = 1

⇒ A(x)=1/(1 − x − 2x²).

Factor: 1 − x − 2x² = (1 − 2x)(1 + x).

Partial fractions:

1/((1−2x)(1+x)) = C/(1−2x) + D/(1+x).

1 = C(1+x) + D(1−2x) = (C+D) + (C−2D)x.

So C+D=1 and C−2D=0 ⇒ C=2D ⇒ 2D + D = 1 ⇒ D=1/3, C=2/3.

Thus A(x)= (2/3)/(1−2x) + (1/3)/(1+x).

Expand:

(2/3)∑\_{n≥0}2^n x^n + (1/3)∑\_{n≥0} (−1)^n x^n

So aₙ = (2/3)·2^n + (1/3)(−1)^n.

If a₁ is different, the same method works but constants C,D change.

## Connections

Next nodes you might study:

- •[Convolutions and Polynomial Multiplication](/tech-tree/convolution-polynomials/)
- •[Linear Recurrences via Generating Functions](/tech-tree/linear-recurrences-gf/)
- •[Fibonacci Numbers](/tech-tree/fibonacci/)
- •[Exponential Generating Functions](/tech-tree/exponential-generating-functions/)
- •[Counting with Formal Power Series](/tech-tree/formal-power-series-counting/)

Quality: A (4.4/5)

[← back to tree](/tech-tree/)[browse all →](/tech-tree/inventory/)
