---
title: Multiple Integrals
description: Double and triple integrals. Volume under surfaces.
date: '2026-07-01'
scheduled: '2027-01-04'
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
inspiration_url: https://templeton.host/tech-tree/multiple-integrals/
inspiration_category: tech-tree
---

> Source-copy draft imported from [https://templeton.host/tech-tree/multiple-integrals/](https://templeton.host/tech-tree/multiple-integrals/). Names, domain references, and local media paths were adapted for Xavi Ablaza / getablaza.com.

[←Back to Tech Tree](/tech-tree/)

[inventory](/tech-tree/inventory/)[coverage](/tech-tree/coverage/)

# Multiple Integrals

CalculusDifficulty: ★★★☆☆Depth: 5Unlocks: 0

Double and triple integrals. Volume under surfaces.

## Interactive Visualization

⏮◀◀▶▶STEP0.25x1xZOOM

t=0s

## Core Concepts

- -Multiple integral as a single number measuring signed volume/hypervolume over a region (extension of definite integral)
- -Integration region (domain) in R^2 or R^3 whose shape/boundaries determine limits of integration
- -Infinitesimal area/volume element representing how integrand is accumulated (the differential element)

## Key Symbols & Notation

dA / dV (differential area or volume element, written in practice as 'dx dy' or 'dx dy dz')

## Essential Relationships

- -Multiple integral equals the limit of Riemann sums over a partition of the region (gives the volume interpretation)
- -Fubini's theorem: when integrable, the multiple integral equals the corresponding iterated single-variable integrals with limits determined by the region (permits computation by nesting)

## Prerequisites (2)

[Integrals6 atoms](/tech-tree/integrals-basic/)[Multivariable Calculus6 atoms](/tech-tree/multivariable-calculus/)

Advanced Learning Details

### Graph Position

57

Depth Cost

0

Fan-Out (ROI)

0

Bottleneck Score

5

Chain Length

### Cognitive Load

6

Atomic Elements

50

Total Elements

L4

Percentile Level

L4

Atomic Level

### All Concepts (20)

- - double integral defined as the limit of Riemann sums over a planar region (definition of ∬\_D f dA)
- - triple integral defined as the limit of Riemann sums over a 3D region (definition of ∭\_E f dV)
- - volume under a surface z = f(x,y) over a region D computed by ∬\_D f(x,y) dA
- - iterated integrals: evaluating multiple integrals as nested single-variable integrals (∫(∫ f dy) dx etc.)
- - Fubini's theorem: conditions under which a multiple integral equals the corresponding iterated integrals and order can be exchanged
- - classification of planar regions for integration (rectangular regions, Type I where y between functions of x, Type II where x between functions of y, and more general bounded regions)
- - setting integration limits as functions of the other variable(s) to describe non-rectangular regions
- - order of integration: how the sequence of inner/outer integrals affects limits and evaluation
- - change of variables in multiple integrals: substituting new coordinates and transforming the integral
- - Jacobian determinant as the local area/volume scaling factor in a change of variables
- - polar coordinates for double integrals (x = r cosθ, y = r sinθ) and using dA = r dr dθ
- - cylindrical coordinates for triple integrals (x = r cosθ, y = r sinθ, z = z) and dV = r dz dr dθ
- - spherical coordinates for triple integrals (x = ρ sinφ cosθ, y = ρ sinφ sinθ, z = ρ cosφ) and dV = ρ^2 sinφ dρ dφ dθ
- - using symmetry of the region or integrand to simplify multiple integrals
- - properties of multiple integrals: linearity, additivity over non-overlapping regions, monotonicity
- - improper multiple integrals: handling unbounded regions or unbounded integrands and criteria for convergence
- - average value of a function over a region via (1/Area(D)) ∬\_D f dA
- - mass and center-of-mass computations via multiple integrals using a density function (mass = ∬\_D ρ(x,y) dA, moments = ∬ xρ dA, etc.)
- - special-case: computing volume of a 3D solid by evaluating a triple integral of 1 over the solid (∭\_E 1 dV = Volume(E))
- - describing regions using inequalities and set-builder notation appropriate for multiple integration (e.g., D = { (x,y): a ≤ x ≤ b, g1(x) ≤ y ≤ g2(x) })

### Teaching Strategy

Multi-session curriculum - substantial prior knowledge and complex material. Use mastery gates and deliberate practice.

A single integral adds up “infinitesimal strips” to measure area. Multiple integrals do the same thing in higher dimensions: they add up “infinitesimal patches” (dA) or “infinitesimal boxes” (dV) to measure volume, mass, probability, and more—over regions whose shapes can be rectangles, disks, triangles, or curved solids.

TL;DR:

A double integral ∬\_D f(x,y) dA accumulates f over a 2D region D; a triple integral ∭\_E f(x,y,z) dV accumulates f over a 3D region E. You compute them by choosing an order (dx dy, dy dx, …), translating the region’s boundaries into limits, and integrating iteratively. When f = 1, the integral returns area (2D) or volume (3D); when f is density, it returns mass.

## What Is Multiple Integrals?

### Why this concept exists

A definite integral

∫ₐᵇ g(x) dx

is best understood as an accumulation process: you slice the x-interval into tiny widths Δx, evaluate g on each slice, and add up g(xᵢ)Δx. In the limit as Δx → 0, that sum becomes a single number: the **signed area** under g.

In many real problems, “one coordinate isn’t enough.” You might want:

- •The volume under a surface z = f(x,y) above some region D in the xy-plane
- •The total mass of a thin plate with varying density ρ(x,y)
- •The amount of heat in a 3D object with density ρ(x,y,z)

In each case, you’re adding up contributions over a **region** in 2D or 3D, not just an interval.

### The big idea (extension of Riemann sums)

A **double integral** is the limit of sums over tiny rectangles (or more general shapes) in a region D ⊂ ℝ².

Partition D into small pieces with area ΔAᵢ. Pick a sample point (xᵢ, yᵢ) in each piece. Then form a sum:

∑ f(xᵢ, yᵢ) ΔAᵢ

If the limit exists as the partition is refined (max ΔAᵢ → 0), we define

∬\_D f(x,y) dA = lim ∑ f(xᵢ, yᵢ) ΔAᵢ.

Similarly, a **triple integral** adds over tiny boxes in a region E ⊂ ℝ³:

∭\_E f(x,y,z) dV = lim ∑ f(xᵢ, yᵢ, zᵢ) ΔVᵢ.

### What “dA” and “dV” really mean

The symbols **dA** and **dV** are reminders of the “infinitesimal piece” you’re summing.

- •In Cartesian coordinates, **dA** is written as dx dy (or dy dx).
- •In 3D Cartesian coordinates, **dV** is written as dx dy dz (in some order).

It is tempting to treat dx dy as algebraic factors—and in computations it often behaves that way—but conceptually it stands for the limiting area of a tiny patch.

### Signed accumulation (not always geometric volume)

In one variable, ∫ can be negative if the function is below the axis. The same is true here:

- •∬\_D f(x,y) dA is **signed**: positive where f > 0, negative where f < 0.
- •If you want physical volume under z = f above D, you typically assume f ≥ 0.

### A key sanity check

If f(x,y) = 1, then

⎧ ∬\_D 1 dA = Area(D)

⎨

⎩ ∭\_E 1 dV = Volume(E)

This is a powerful check: if your limits describe the wrong region, your “area/volume of 1” will come out wrong.

### Two ways to think about the output

A multiple integral returns **one number**. You can interpret it as:

1) **Geometric accumulation**: volume under a surface (2D region) or hypervolume (higher dimensions)

2) **Total quantity**: if f is a density (mass/area, mass/volume, probability density, etc.), the integral gives the total amount.

In many applications, the main challenge is not the integration itself—it’s correctly describing the region D or E and choosing a convenient differential element.

## Core Mechanic 1: Regions and Limits (How Geometry Becomes Bounds)

### Why limits are the real problem

In single-variable integrals, the interval [a,b] is straightforward. In multiple integrals, the region can be:

- •A rectangle: easy
- •A triangle: piecewise bounds
- •A disk: curved boundary
- •A region between curves: requires careful reading

Your goal is to translate a geometric description of D (or E) into limits of integration.

### Type I and Type II regions in ℝ²

Many 2D regions can be described in two common ways.

**Type I (x-simple):**

D = { (x,y) : a ≤ x ≤ b, g₁(x) ≤ y ≤ g₂(x) }

Then

∬\_D f(x,y) dA = ∫ₓ=aᵇ ∫ᵧ=g₁(x)^{g₂(x)} f(x,y) dy dx.

**Type II (y-simple):**

D = { (x,y) : c ≤ y ≤ d, h₁(y) ≤ x ≤ h₂(y) }

Then

∬\_D f(x,y) dA = ∫ᵧ=cᵈ ∫ₓ=h₁(y)^{h₂(y)} f(x,y) dx dy.

Same region, different descriptions. The choice can make the integral easy or miserable.

### Reading boundaries from a picture (the method)

A reliable workflow:

1) **Sketch D** (even roughly).

2) Decide an order (dy dx or dx dy).

3) For the inner variable, draw a vertical or horizontal line through the region.

4) Find where that line enters and exits the region: those are the inner bounds.

5) The outer bounds are the range over which that line actually intersects D.

### Example of why order matters

Suppose D is the region between y = x² and y = 2x for x ≥ 0. Intersections:

x² = 2x

x² − 2x = 0

x(x − 2) = 0 ⇒ x = 0, 2

If you integrate with dy first (vertical slices):

0 ≤ x ≤ 2,

x² ≤ y ≤ 2x.

So

∬\_D f dA = ∫₀² ∫\_{x²}^{2x} f(x,y) dy dx.

If you reverse order (horizontal slices), you must solve for x in terms of y:

y = x² ⇒ x = √y (since x ≥ 0)

y = 2x ⇒ x = y/2

But the left/right boundary switches depending on y. You’d need to split into ranges where y/2 ≤ √y (and check where they meet).

That’s the typical pattern: reversing order can require **piecewise integrals**.

### Differential area element as geometry

In Cartesian coordinates:

- •A tiny rectangle has side lengths dx and dy
- •Its area is approximately dx·dy

So dA = dx dy.

This becomes especially meaningful later in other coordinate systems (polar, cylindrical, spherical), where the “tiny patch” is not a rectangle. Even in Cartesian coordinates, it helps to remember that dA represents *shape and scale* of the local patch.

### A table: choosing an order

| Goal | Prefer dy dx when… | Prefer dx dy when… |
| --- | --- | --- |
| Simpler bounds | Region is easily described by vertical slices | Region is easily described by horizontal slices |
| Integrand easier | Integrating f with respect to y is simple | Integrating f with respect to x is simple |
| Avoid splitting | One order yields single-range bounds | The other order forces piecewise bounds |

### In ℝ³: describing solids with bounds

For triple integrals, the same ideas extend, but you now have **three** variables and nested bounds.

A common pattern is a “z-simple” solid:

E = { (x,y,z) : (x,y) ∈ D, z₁(x,y) ≤ z ≤ z₂(x,y) }

Then

∭\_E f(x,y,z) dV = ∬\_D

\left( ∫\_{z=z₁(x,y)}^{z₂(x,y)} f(x,y,z) dz \right) dA.

In Cartesian coordinates, dV = dx dy dz (in some order). Geometrically, you’re summing tiny boxes with volume dx·dy·dz.

### A key mental model: “stacking”

If E is between two surfaces z = z₂(x,y) (top) and z = z₁(x,y) (bottom), then for each (x,y) in the base region D you have a vertical segment of height z₂ − z₁. You can think:

Volume(E) = ∬\_D (z₂(x,y) − z₁(x,y)) dA

because that’s exactly ∭\_E 1 dV with dz integrated out first:

∭\_E 1 dV

= ∬\_D \left( ∫\_{z₁}^{z₂} 1 dz \right) dA

= ∬\_D (z₂ − z₁) dA.

That identity is one of the most useful bridges between 2D and 3D integration.

## Core Mechanic 2: Iterated Integrals (Compute by Integrating One Variable at a Time)

### Why iterated integrals work

The double integral is defined via a 2D limiting process, but in practice we compute it using **iterated integrals** (one integral inside another). Under mild conditions (e.g., f continuous on a nice region), Fubini’s Theorem tells us we can compute

∬\_D f(x,y) dA

by integrating in one variable and then the other, provided the bounds correctly describe D.

So computation becomes familiar: it’s just repeated single-variable integration.

### Anatomy of an iterated integral

Take

∬\_D f(x,y) dA = ∫ₓ=aᵇ ∫ᵧ=g₁(x)^{g₂(x)} f(x,y) dy dx.

Read it as:

1) For a fixed x, integrate f(x,y) with respect to y from y = g₁(x) to y = g₂(x).

2) The result is a function of x.

3) Integrate that result from x = a to x = b.

The inner integral treats the “outer variable” as a constant.

### Worked algebra pattern (keep constants straight)

If f(x,y) = x y² + 3x, then when integrating with respect to y:

∫ (x y² + 3x) dy

= x ∫ y² dy + 3x ∫ 1 dy

= x \left( y³/3 \right) + 3x(y)

= (x/3) y³ + 3xy.

The key move is recognizing x is constant during dy integration.

### Double integrals as volume under a surface

If f(x,y) ≥ 0 and D is a region in the plane, then

Volume under z = f(x,y) above D = ∬\_D f(x,y) dA.

Why? Because above each small patch ΔA, the “column” has base area ΔA and height f(xᵢ,yᵢ), so volume contribution is approximately f(xᵢ,yᵢ)ΔA.

### Triple integrals as accumulation in 3D

In 3D, if ρ(x,y,z) is a density (mass per unit volume), then total mass is

Mass = ∭\_E ρ(x,y,z) dV.

Again, each tiny box has mass approximately ρ(xᵢ,yᵢ,zᵢ)ΔV.

### Changing order: not just algebra, geometry

Changing dx dy to dy dx is not a symbolic swap. It means:

- •You are slicing the region differently.
- •The inner bounds must represent the “enter/exit” points of the slice.

This is where many mistakes happen: the integrand stays the same, but the bounds must be rewritten to describe the **same** region.

### A practical test: integrate 1

If you’re unsure whether your bounds match the region, compute ∬\_D 1 dA.

- •If D is a triangle of area 3, you must get 3.
- •If D is a disk of radius 2, you must get 4π.

This is the fastest debugging tool for region setup.

### Common region templates (Cartesian)

1) **Rectangle:** a ≤ x ≤ b, c ≤ y ≤ d

∬\_D f dA = ∫ₐᵇ ∫\_c^d f(x,y) dy dx

2) **Between curves y = g₁(x) and y = g₂(x):**

∬\_D f dA = ∫ₐᵇ ∫\_{g₁(x)}^{g₂(x)} f(x,y) dy dx

3) **Between surfaces z = z₁(x,y) and z = z₂(x,y):**

∭\_E f dV = ∬\_D ∫\_{z₁(x,y)}^{z₂(x,y)} f(x,y,z) dz dA

### Differential element as bookkeeping

In an iterated integral, the differential at the end is a reminder of the order:

- •dx dy means “integrate in x first (inner), then y (outer)” only if written as ∫∫ … dx dy.
- •dy dx means “integrate in y first, then x.”

So the pair (bounds, differential order) must match.

A helpful habit: when you write

∫ₓ=aᵇ ∫ᵧ=g₁(x)^{g₂(x)} f(x,y) dy dx

say out loud: “dy then dx.” This prevents accidental mismatches like writing y-bounds that depend on y (nonsense) or forgetting which variable is currently being integrated.

## Application/Connection: What Multiple Integrals Let You Do

### 1) Area and volume as special cases

As noted earlier:

Area(D) = ∬\_D 1 dA

Volume(E) = ∭\_E 1 dV

And for a solid under z = f(x,y) above base D (with f ≥ 0):

Volume = ∬\_D f(x,y) dA.

This is the “volume under surfaces” story that motivates double integrals.

### 2) Mass with variable density

If a lamina (thin plate) occupies D and has density ρ(x,y) (mass per unit area), then

Mass = ∬\_D ρ(x,y) dA.

If a 3D object occupies E with density ρ(x,y,z) (mass per unit volume), then

Mass = ∭\_E ρ(x,y,z) dV.

These formulas are identical in structure to area/volume, but the integrand now encodes material variation.

### 3) Averages in 2D and 3D

In 1D, the average value of g on [a,b] is (1/(b−a))∫ₐᵇ g(x) dx.

In 2D, the average value of f on region D is

f\_avg = (1/Area(D)) ∬\_D f(x,y) dA.

In 3D, the average value of f on region E is

f\_avg = (1/Volume(E)) ∭\_E f(x,y,z) dV.

This is a common use in physics (average temperature, average density) and probability (expected values with densities).

### 4) Probability (continuous random variables)

If (X,Y) has joint density p(x,y) over D, then

P((X,Y) ∈ D) = ∬\_D p(x,y) dA.

And for expectations, you integrate the quantity of interest times density:

E[g(X,Y)] = ∬ g(x,y) p(x,y) dA.

Even if you haven’t studied probability yet, it’s helpful to recognize that the same accumulation logic powers it.

### 5) Where this node leads next (coordinate systems)

Many regions (disks, cylinders, spheres) are awkward in Cartesian bounds but simple in polar/cylindrical/spherical coordinates. In those systems, the differential element changes (e.g., dA = r dr dθ), which is fundamentally the same “infinitesimal patch” idea.

So mastering regions + iterated integrals in Cartesian coordinates sets you up to understand **Jacobian factors** later: the scaling needed when your tiny patch is a wedge or shell rather than a rectangle.

### 6) Connection to vector calculus

Multiple integrals are also the foundation for:

- •Line integrals and surface integrals (integrating along curves or over surfaces)
- •Divergence and curl theorems (turning complicated flux integrals into volume integrals)

Those topics reuse the same mental pattern: define a region, identify the correct differential element, and accumulate.

## Worked Examples (3)

### Double integral over a non-rectangular region (between curves)

Compute ∬\_D (x + y) dA where D is the region bounded by y = x² and y = 2x for 0 ≤ x ≤ 2.

1. Step 1: Describe the region D.

   We are told D is between y = x² (lower curve for 0≤x≤2) and y = 2x (upper curve).

   So a convenient Type I description is:

   0 ≤ x ≤ 2,

   x² ≤ y ≤ 2x.
2. Step 2: Write the iterated integral (dy then dx).

   ∬\_D (x + y) dA

   = ∫₀² ∫\_{y=x²}^{2x} (x + y) dy dx.
3. Step 3: Compute the inner integral with respect to y.

   Treat x as constant:

   ∫ (x + y) dy

   = ∫ x dy + ∫ y dy

   = xy + y²/2.

   Evaluate from y = x² to y = 2x:

   [xy + y²/2]\_{x²}^{2x}

   = (x(2x) + (2x)²/2) − (x(x²) + (x²)²/2)

   = (2x² + 4x²/2) − (x³ + x⁴/2)

   = (2x² + 2x²) − x³ − x⁴/2

   = 4x² − x³ − x⁴/2.
4. Step 4: Integrate the result over x from 0 to 2.

   ∫₀² (4x² − x³ − x⁴/2) dx

   = ∫₀² 4x² dx − ∫₀² x³ dx − (1/2)∫₀² x⁴ dx

   Compute each:

   ∫ 4x² dx = 4·(x³/3)

   ∫ x³ dx = x⁴/4

   ∫ x⁴ dx = x⁵/5

   So

   = [4x³/3 − x⁴/4 − (1/2)(x⁵/5)]₀²

   = [4x³/3 − x⁴/4 − x⁵/10]₀².
5. Step 5: Evaluate at x = 2.

   4x³/3 = 4·8/3 = 32/3

   x⁴/4 = 16/4 = 4

   x⁵/10 = 32/10 = 16/5

   So value = 32/3 − 4 − 16/5.

   Put over common denominator 15:

   32/3 = 160/15

   4 = 60/15

   16/5 = 48/15

   Result = (160 − 60 − 48)/15 = 52/15.

**Insight:** Most of the work was not “integration tricks”—it was correctly encoding the region as x² ≤ y ≤ 2x. Once the bounds match the geometry, the computation becomes routine.

### Volume of a solid between two surfaces (triple integral via stacking)

Find the volume of the solid E over the rectangle D = { (x,y): 0 ≤ x ≤ 1, 0 ≤ y ≤ 2 } between z = 0 and z = 3 + x + y.

1. Step 1: Recognize this is a stacked solid.

   For each (x,y) in the base D, z runs from bottom z₁ = 0 to top z₂ = 3 + x + y.
2. Step 2: Write volume as ∭\_E 1 dV and integrate dz first.

   Volume = ∭\_E 1 dV

   = ∬\_D \left( ∫\_{z=0}^{3+x+y} 1 dz \right) dA.
3. Step 3: Compute the inner integral.

   ∫₀^{3+x+y} 1 dz = (3 + x + y) − 0 = 3 + x + y.
4. Step 4: Convert to a double integral over the rectangle.

   Since D is rectangular, dA = dx dy is simple:

   Volume = ∬\_D (3 + x + y) dA

   = ∫ₓ=0^1 ∫ᵧ=0^2 (3 + x + y) dy dx.
5. Step 5: Integrate with respect to y.

   Treat x as constant:

   ∫₀² (3 + x + y) dy

   = [ (3 + x)y + y²/2 ]₀²

   = (3 + x)·2 + 4/2

   = 2(3 + x) + 2

   = 6 + 2x + 2

   = 8 + 2x.
6. Step 6: Integrate with respect to x.

   ∫₀¹ (8 + 2x) dx

   = [8x + x²]₀¹

   = 8 + 1

   = 9.

**Insight:** A triple integral can collapse quickly if you choose the natural order. Here, integrating dz first turns the 3D volume problem into a 2D area accumulation of the height (3 + x + y).

### Mass of a lamina with variable density over a rectangle

A plate occupies D = { (x,y): 0 ≤ x ≤ 2, 1 ≤ y ≤ 3 } with density ρ(x,y) = x y. Find the mass.

1. Step 1: Set up mass as a double integral.

   Mass = ∬\_D ρ(x,y) dA = ∬\_D x y dA.
2. Step 2: Use the rectangular bounds.

   Mass = ∫₀² ∫₁³ x y dy dx.
3. Step 3: Integrate with respect to y.

   x is constant with respect to y:

   ∫₁³ x y dy = x ∫₁³ y dy = x [y²/2]₁³ = x(9/2 − 1/2) = x·(8/2) = 4x.
4. Step 4: Integrate with respect to x.

   ∫₀² 4x dx = [2x²]₀² = 2·4 = 8.

**Insight:** When the region is a rectangle, the main conceptual step is interpreting ρ as “mass per unit area.” The integral adds up tiny masses ρ(x,y) dA.

## Key Takeaways

- ✓

  A multiple integral is a single number representing accumulation of a function over a region in ℝ² (dA) or ℝ³ (dV).
- ✓

  The differential element dA or dV encodes the “infinitesimal patch/box” being summed; in Cartesian coordinates dA = dx dy and dV = dx dy dz.
- ✓

  Setting up correct bounds (describing the region) is often harder than performing the integrations.
- ✓

  Iterated integrals compute multiple integrals by integrating one variable at a time; the inner integral treats outer variables as constants.
- ✓

  Order matters for setup: the same region can require one integral or a piecewise split depending on whether you use dy dx or dx dy.
- ✓

  Area and volume are special cases: ∬\_D 1 dA = Area(D) and ∭\_E 1 dV = Volume(E).
- ✓

  For solids between z = z₁(x,y) and z = z₂(x,y), volume can be computed as ∬\_D (z₂ − z₁) dA.

## Common Mistakes

- ✗

  Writing bounds that don’t match the region (e.g., using constant limits when the boundary is curved, or forgetting to restrict the outer variable’s range).
- ✗

  Swapping the order (dx dy ↔ dy dx) without rewriting the bounds to describe the same region, often leading to incorrect answers.
- ✗

  Forgetting that the inner integral treats the outer variable(s) as constants (e.g., incorrectly integrating x as if it depended on y).
- ✗

  Confusing geometric volume with signed integral when f changes sign; ∬\_D f dA can be negative even if the region is positive area.

## Practice

easy

Compute ∬\_D (2x) dA over the rectangle D = { (x,y): 0 ≤ x ≤ 3, −1 ≤ y ≤ 2 }.

**Hint:** Integrate in y first: ∫\_{−1}^2 2x dy = 2x(2−(−1)).

Show solution

Set up:

∬\_D 2x dA = ∫₀³ ∫\_{−1}^2 2x dy dx.

Inner integral:

∫\_{−1}^2 2x dy = 2x[y]\_{−1}^2 = 2x(3) = 6x.

Outer:

∫₀³ 6x dx = [3x²]₀³ = 27.

medium

Let D be the triangle with vertices (0,0), (2,0), (2,3). Compute ∬\_D 1 dA (the area) using an iterated integral.

**Hint:** Describe the slanted edge as a line from (0,0) to (2,3): y = (3/2)x. Use 0 ≤ x ≤ 2 and 0 ≤ y ≤ (3/2)x.

Show solution

The line through (0,0) and (2,3) is y = (3/2)x.

A Type I description is:

0 ≤ x ≤ 2,

0 ≤ y ≤ (3/2)x.

Then

Area(D) = ∬\_D 1 dA = ∫₀² ∫₀^{(3/2)x} 1 dy dx.

Inner:

∫₀^{(3/2)x} 1 dy = (3/2)x.

Outer:

∫₀² (3/2)x dx = (3/2)[x²/2]₀² = (3/2)·(4/2) = (3/2)·2 = 3.

hard

Compute the volume of E = { (x,y,z): 0 ≤ x ≤ 1, 0 ≤ y ≤ 1, 0 ≤ z ≤ x + y }.

**Hint:** Use ∭\_E 1 dV and integrate dz first, then over the unit square in (x,y).

Show solution

Volume = ∭\_E 1 dV = ∫₀¹ ∫₀¹ ∫₀^{x+y} 1 dz dy dx.

Inner:

∫₀^{x+y} 1 dz = x + y.

So

Volume = ∫₀¹ ∫₀¹ (x + y) dy dx.

Integrate in y:

∫₀¹ (x + y) dy = [xy + y²/2]₀¹ = x + 1/2.

Integrate in x:

∫₀¹ (x + 1/2) dx = [x²/2 + x/2]₀¹ = 1/2 + 1/2 = 1.

## Connections

- •Next: [Polar Coordinates and Jacobians](/tech-tree/polar-coordinates/)
- •Related: [Riemann Sums](/tech-tree/riemann-sums/)
- •Related: [Partial Derivatives](/tech-tree/partial-derivatives/)
- •Next: [Line Integrals](/tech-tree/line-integrals/)
- •Next: [Surface Integrals](/tech-tree/surface-integrals/)

Quality: A (4.3/5)

[← back to tree](/tech-tree/)[browse all →](/tech-tree/inventory/)
