---
title: Vectors Introduction
description: Directed quantities with magnitude and direction. Addition and scalar multiplication.
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
source_format: html
inspiration_url: https://templeton.host/tech-tree/vectors-intro/
inspiration_category: tech-tree
---

> Source-copy draft imported from [https://templeton.host/tech-tree/vectors-intro/](https://templeton.host/tech-tree/vectors-intro/). Names, domain references, and local media paths were adapted for Xavi Ablaza / getablaza.com.

[←Back to Tech Tree](/tech-tree/)

[inventory](/tech-tree/inventory/)[coverage](/tech-tree/coverage/)

# Vectors Introduction

Linear AlgebraDifficulty: ★☆☆☆☆Depth: 1Unlocks: 99

Directed quantities with magnitude and direction. Addition and scalar multiplication.

## Interactive Visualization

⏮◀◀▶▶STEP0.25x1xZOOM

t=0s

## Core Concepts

- -Vector: a directed quantity characterized by magnitude (length) and direction
- -Vector addition: combining two vectors yields a third vector (geometric head-to-tail/parallelogram rule)
- -Scalar multiplication: multiplying a vector by a real number scales its magnitude and reverses direction if the scalar is negative

## Key Symbols & Notation

Vector notation: a letter designated as a vector (e.g., 'v' indicated by an arrow over the letter or boldface 'v')Magnitude notation: vertical bars around a vector, written as '|v|', denote its length

## Essential Relationships

- -Coordinate correspondence: in a chosen coordinate system, vector addition and scalar multiplication are performed componentwise on the vectors' coordinates

## Prerequisites (1)

[Coordinate Systems6 atoms](/tech-tree/coordinate-plane/)

## Unlocks (5)

[Multivariable Calculuslvl 3](/tech-tree/multivariable-calculus/)[Gradientslvl 3](/tech-tree/gradients/)[Matrix Operationslvl 2](/tech-tree/matrix-operations/)[Dot Productlvl 2](/tech-tree/dot-product/)[Vector Spaceslvl 2](/tech-tree/vector-spaces/)

Advanced Learning Details

### Graph Position

12

Depth Cost

99

Fan-Out (ROI)

32

Bottleneck Score

1

Chain Length

### Cognitive Load

6

Atomic Elements

40

Total Elements

L3

Percentile Level

L4

Atomic Level

### All Concepts (15)

- - Vector as a directed quantity (arrow) distinct from a point
- - Free vector notion: same vector independent of its position in the plane/space
- - Representation of a vector by components (ordered tuple of numbers)
- - Position (or position) vector: vector from the origin to a point
- - Magnitude (length, norm) of a vector
- - Direction of a vector (orientation, e.g., angle relative to an axis)
- - Vector addition (geometric: head-to-tail construction)
- - Vector addition (algebraic: component-wise addition)
- - Scalar multiplication (scaling a vector by a real number)
- - Zero vector (additive identity)
- - Negative (opposite) vector (additive inverse)
- - Unit vector (vector with length 1)
- - Normalization (process: dividing by magnitude to get a unit vector)
- - Vector subtraction as adding the negative (displacement between points)
- - Standard basis vectors (e.g., i, j or e1, e2) and expressing vectors as linear combinations of them

### Teaching Strategy

Deep-dive lesson - accessible entry point but dense material. Use worked examples and spaced repetition.

When GPS tells you to drive 'north for 2 miles,' it's giving you a vector - a quantity with both size and direction. This seemingly simple idea turns out to be one of the most powerful concepts in mathematics, underlying everything from physics to machine learning.

TL;DR:

A vector is a quantity with both magnitude (how much) and direction (which way). You can represent vectors as ordered pairs of numbers, add them component-wise, and scale them by multiplying each component.

## What Is a Vector?

![A vector shown as an arrow with magnitude (length) and direction labeled](/img/templeton/lessons/vectors/vector-as-arrow.svg)

Let's start with the core idea: a **vector** is a mathematical object that captures two pieces of information simultaneously:

1. 1)**Magnitude** - how big or strong something is (a number)
2. 2)**Direction** - which way it points (an orientation in space)

The most natural way to visualize a vector is as an **arrow**. The arrow's length represents the magnitude - a longer arrow means a bigger value. The arrow's orientation tells you the direction - where it's pointing.

This is fundamentally different from regular numbers. A regular number like "5" just tells you "how much" - it answers questions like "how far?" or "how heavy?" We call these regular numbers **scalars** because they only have scale (size), not direction.

A vector answers a richer question: "how much *in which direction*?"

**Example:** Saying "the wind is blowing at 20 mph" gives you a scalar - just the speed. But saying "the wind is blowing at 20 mph from the northwest" gives you a vector - both speed and direction. The second is more useful if you're sailing a boat!

**A crucial property:** Two arrows that have the same length and point the same direction represent the *same* vector, regardless of where they're drawn. You could draw an arrow from point A to point B, or an identical arrow from point C to point D - if they have the same length and direction, they're the same vector. We say vectors are "free" - they don't have a fixed position in space.

This might seem abstract, but it's actually what makes vectors so useful: we can move them around, add them together, and manipulate them without worrying about where they're located.

## Components: The Coordinate View

![Vector (4,2) broken into x-component of 4 and y-component of 2](/img/templeton/lessons/vectors/vector-components.svg)

Drawing arrows is great for intuition, but we need a way to work with vectors using numbers. That's where **components** come in.

Place your vector in a coordinate system - the familiar x-y plane from algebra. Now, any vector from the origin can be described by two numbers:

- •How far it goes horizontally (the **x-component**)
- •How far it goes vertically (the **y-component**)

We write these as an ordered pair. For example:

**v** = (4, 2)

This notation means: "start at the origin, go 4 units to the right, then go 2 units up." The tip of the arrow lands at the point (4, 2).

Let's be very clear about what these numbers mean:

- •The first number (4) is the x-component - the horizontal displacement
- •The second number (2) is the y-component - the vertical displacement
- •Together, they completely specify the vector

**Different notations you'll encounter:**

Mathematicians and physicists use several equivalent ways to write the same vector:

| Notation | Example | Common in |
| --- | --- | --- |
| Parentheses | (4, 2) | Most textbooks |
| Angle brackets | ⟨4, 2⟩ | Physics, some calc texts |
| Column vector | [4; 2] vertically | Linear algebra |
| Unit vector form | 4**î** + 2**ĵ** | Physics (we'll cover this later) |

All of these mean exactly the same thing: a vector with x-component 4 and y-component 2. Don't let the notation confuse you - it's just different ways of writing the same object.

**Why components are powerful:** Once you have components, you can do arithmetic with vectors using ordinary algebra. No more drawing - just calculate with the numbers.

## Magnitude: How Long Is the Arrow?

![Right triangle showing how magnitude relates to components via Pythagorean theorem](/img/templeton/lessons/vectors/magnitude-pythagorean.svg)

Sometimes you need to know how "big" a vector is without caring about its direction. The **magnitude** (also called the **length** or **norm**) of a vector measures exactly this.

But wait - if a vector is written as (4, 2), is its magnitude 4? Or 2? Or something else entirely?

Here's where geometry helps us. Draw a vector from the origin to point (4, 2). Now draw a horizontal line from the origin to (4, 0), and a vertical line from (4, 0) up to (4, 2).

You've just created a **right triangle** where:

- •One leg has length 4 (the x-component)
- •One leg has length 2 (the y-component)
- •The hypotenuse is the vector itself

The Pythagorean theorem tells us the hypotenuse length! For any right triangle:

a² + b² = c²

where c is the hypotenuse.

So for our vector **v** = (4, 2):

magnitude² = 4² + 2² = 16 + 4 = 20

magnitude = √20 ≈ 4.47

**The general formula:** For any 2D vector **v** = (x, y), the magnitude is:

‖**v**‖ = √(x² + y²)

Those double vertical bars ‖ ‖ are the standard notation for magnitude. Some texts use single bars |**v**|, but ‖**v**‖ is more precise (single bars often mean absolute value, which is a related but different concept).

**A classic example:** Consider **v** = (3, 4).

‖**v**‖ = √(3² + 4²) = √(9 + 16) = √25 = 5

This is the famous 3-4-5 right triangle. The vector (3, 4) has magnitude exactly 5. Notice that 5 is not equal to either component - the magnitude is the *diagonal* distance, not a horizontal or vertical distance.

**Key insight:** Magnitude is always non-negative (zero or positive). The only vector with magnitude zero is the **zero vector** (0, 0), which has no direction because it doesn't point anywhere.

## Vector Addition: Head-to-Tail

![Two vectors added head-to-tail, with the sum vector shown](/img/templeton/lessons/vectors/vector-addition.svg)

Now we get to one of the most useful operations: adding vectors together. When would you want to do this? Any time two vector quantities combine.

**Physical example:** You walk 3 blocks east, then 2 blocks north. Where are you relative to where you started? You need to add your two displacement vectors.

**The geometric method (head-to-tail):**

To add vector **a** and vector **b** geometrically:

1. 1)Draw vector **a** starting from any point
2. 2)Draw vector **b** starting from the *head* (tip) of **a**
3. 3)The sum **a** + **b** is the vector from the *tail* of **a** to the *head* of **b**

Why does this work? Think about it: **a** gets you from the start to some intermediate point. Then **b** takes you from that intermediate point to the final destination. The sum is the "shortcut" - the direct path from start to finish.

**The algebraic method (component-wise addition):**

Even simpler: just add the corresponding components!

If **a** = (3, 1) and **b** = (2, 3), then:

**a** + **b** = (3 + 2, 1 + 3) = (5, 4)

That's it. Add the x-components together, add the y-components together.

Why does this work? Think about the x-direction and y-direction separately:

- •In the x-direction, **a** moves you 3 units and **b** moves you 2 more. Total: 5 units.
- •In the y-direction, **a** moves you 1 unit and **b** moves you 3 more. Total: 4 units.

**Properties of vector addition:**

Vector addition behaves nicely, just like addition of regular numbers:

1. 1)**Commutative:** **a** + **b** = **b** + **a**

(Order doesn't matter - you end up at the same place)

2. 2)**Associative:** (**a** + **b**) + **c** = **a** + (**b** + **c**)

(Grouping doesn't matter)

3. 3)**Identity:** **v** + **0** = **v**

(Adding the zero vector (0, 0) changes nothing)

These properties might seem obvious, but not all mathematical operations have them. It's worth noting when they hold.

## Scalar Multiplication: Scaling Vectors

![Same vector scaled by 2, 0.5, and -1](/img/templeton/lessons/vectors/scalar-multiplication.svg)

What if you want to make a vector longer or shorter without changing its direction? That's **scalar multiplication** - multiplying a vector by a regular number (a scalar).

**The basic operation:**

To multiply vector **v** = (3, 1) by the scalar 2:

2 · **v** = 2 · (3, 1) = (2 · 3, 2 · 1) = (6, 2)

Just multiply each component by the scalar. The result is a vector that points in the same direction but is twice as long.

**What different scalars do:**

| Scalar c | Effect on **v** |
| --- | --- |
| c > 1 | Longer, same direction |
| c = 1 | No change |
| 0 < c < 1 | Shorter, same direction |
| c = 0 | Zero vector (0, 0) |
| c < 0 | Flipped direction! |

Let's see negative scalars in action. If **v** = (3, 1):

−1 · **v** = (−3, −1)

This vector has the same magnitude as **v** but points in the *exactly opposite* direction. Multiplying by -1 is like doing a 180° turn.

What about −2 · **v**?

−2 · **v** = (−6, −2)

This vector is twice as long as **v** and points in the opposite direction. The negative sign flips it; the 2 stretches it.

**Why this is useful:**

Scalar multiplication lets you express related vectors compactly. For example:

- •"A force three times as strong in the same direction" → 3**F**
- •"Half the velocity" → 0.5**v**
- •"The opposite direction" → −**v**

**The algebraic rule:**

For any scalar c and vector **v** = (x, y):

c · **v** = (c · x, c · y)

Multiply the scalar through to each component. That's all there is to it.

## Unit Vectors: Pure Direction

![Unit vectors i and j, and how any vector decomposes into them](/img/templeton/lessons/vectors/unit-vectors.svg)

A **unit vector** is a vector with magnitude exactly equal to 1. It represents pure direction, with no "size" attached.

Why would you want such a thing? Because sometimes you want to talk about direction independently of magnitude. "Which way is it pointing?" is a different question from "How strong is it?"

**The standard basis vectors:**

In 2D, two unit vectors are so important they get their own names:

**î** = (1, 0) - points in the positive x-direction

**ĵ** = (0, 1) - points in the positive y-direction

(The little hat symbol ˆ indicates a unit vector. You'll see **î** pronounced "i-hat" and **ĵ** pronounced "j-hat".)

These two vectors form the **standard basis** for 2D space. Why "basis"? Because any 2D vector can be built from them.

**Decomposing any vector:**

Take the vector (3, 2). Using unit vectors:

(3, 2) = 3**î** + 2**ĵ**

This says: "go 3 units in the **î** direction, then 2 units in the **ĵ** direction."

Let's verify this makes sense:

- •3**î** = 3 · (1, 0) = (3, 0) - three steps right
- •2**ĵ** = 2 · (0, 1) = (0, 2) - two steps up
- •(3, 0) + (0, 2) = (3, 2) ✓

So the notation 3**î** + 2**ĵ** is just another way of writing (3, 2). It emphasizes that the vector is a combination of horizontal and vertical components.

**Creating a unit vector from any vector:**

Given any non-zero vector **v**, you can create a unit vector **û** that points in the same direction by dividing by the magnitude:

**û** = **v** / ‖**v**‖

This process is called **normalizing** the vector.

**Example:** Normalize **v** = (3, 4).

Step 1: Find the magnitude.

‖**v**‖ = √(3² + 4²) = √(9 + 16) = √25 = 5

Step 2: Divide each component by the magnitude.

**û** = (3/5, 4/5) = (0.6, 0.8)

Step 3: Verify the result has magnitude 1.

‖**û**‖ = √(0.6² + 0.8²) = √(0.36 + 0.64) = √1 = 1 ✓

The vector (0.6, 0.8) points in the same direction as (3, 4) but has magnitude exactly 1.

## Vector Subtraction and the Zero Vector

**Vector subtraction** is defined in terms of addition and scalar multiplication:

**a** − **b** = **a** + (−1 · **b**) = **a** + (−**b**)

In other words, subtracting **b** is the same as adding the opposite of **b**.

**Example:** If **a** = (5, 3) and **b** = (2, 1):

**a** − **b** = (5, 3) − (2, 1)

= (5 − 2, 3 − 1)

= (3, 2)

Just subtract component by component, just like addition adds component by component.

**Geometric interpretation:** The vector **a** − **b** points from the tip of **b** to the tip of **a** (when both are drawn from the origin). It answers: "what vector do I add to **b** to get **a**?"

**The zero vector:**

The **zero vector**, written **0** or (0, 0), is special:

- •It has magnitude 0
- •It has no defined direction (there's no "way" a zero-length arrow points)
- •It's the **additive identity**: **v** + **0** = **v** for any vector **v**

Every vector has an **additive inverse** - a vector that "cancels it out":

**v** + (−**v**) = **0**

For **v** = (3, 4), the additive inverse is −**v** = (−3, −4), and:

(3, 4) + (−3, −4) = (0, 0) = **0**

**Physical interpretation:** If you walk 3 blocks east and then 3 blocks west, you're back where you started. Your net displacement is zero - the zero vector.

## Worked Examples (4)

### Displacement vs. Distance

A hiker walks 4 km east, then 3 km north. Find: (a) their displacement from the starting point, and (b) the total distance they walked.

1. Model each leg as a vector:

   • East leg: **d₁** = (4, 0) km (4 units in x-direction, 0 in y)

   • North leg: **d₂** = (0, 3) km (0 units in x, 3 in y)
2. Add the vectors to find displacement:

   **d** = **d₁** + **d₂** = (4, 0) + (0, 3) = (4, 3) km
3. Find the magnitude of the displacement:

   ‖**d**‖ = √(4² + 3²) = √(16 + 9) = √25 = 5 km

   This is how far they are from the start, as the crow flies.
4. Find total distance walked:

   Distance = 4 km + 3 km = 7 km

   This is the length of the path they actually traveled.

**Insight:** Distance walked (7 km) and displacement magnitude (5 km) are different! Displacement is a vector - it cares about the net change in position. Distance is a scalar - it accumulates every step regardless of direction. A round trip has zero displacement but positive distance.

### Combining Forces

Two forces act on an object: **F₁** = (6, 8) N and **F₂** = (−2, 4) N. Find the net force and its magnitude.

1. Understand what the forces mean:

   • **F₁** pushes 6 N to the right and 8 N upward

   • **F₂** pushes 2 N to the left (negative x) and 4 N upward
2. Add the force vectors component by component:

   **F\_net** = **F₁** + **F₂**

   = (6 + (−2), 8 + 4)

   = (4, 12) N
3. Find the magnitude of the net force:

   ‖**F\_net**‖ = √(4² + 12²)

   = √(16 + 144)

   = √160

   ≈ 12.65 N

**Insight:** You can't just add magnitudes! ‖**F₁**‖ = √(36+64) = 10 N and ‖**F₂**‖ = √(4+16) ≈ 4.5 N, but the net force is about 12.65 N, not 14.5 N. The x-components partially canceled (6 − 2 = 4), while the y-components reinforced (8 + 4 = 12). Direction matters.

### Normalizing a Vector

Find a unit vector pointing in the same direction as **w** = (5, 12).

1. First, find the magnitude of **w**:

   ‖**w**‖ = √(5² + 12²) = √(25 + 144) = √169 = 13

   (This is the 5-12-13 Pythagorean triple.)
2. Divide each component by the magnitude:

   **ŵ** = **w** / ‖**w**‖

   = (5/13, 12/13)

   ≈ (0.385, 0.923)
3. Verify the result has magnitude 1:

   ‖**ŵ**‖ = √((5/13)² + (12/13)²)

   = √(25/169 + 144/169)

   = √(169/169)

   = √1 = 1 ✓

**Insight:** Normalization preserves direction while setting magnitude to 1. This is useful when you only care about which way something is pointing, not how strong it is. For example, in computer graphics, surface normals are always normalized.

### Scalar Multiplication with Negatives

Given **v** = (−3, 7), write it in unit vector notation. Then find a vector that is twice as long and points in the opposite direction.

1. Express **v** using unit vectors **î** and **ĵ**:

   **v** = (−3, 7) = −3**î** + 7**ĵ**

   (The x-component multiplies **î**, the y-component multiplies **ĵ**.)
2. To flip direction and double length, multiply by −2:

   −2**v** = −2 · (−3, 7)

   = (−2 · −3, −2 · 7)

   = (6, −14)
3. Verify the result:

   • Original magnitude: ‖**v**‖ = √(9 + 49) = √58 ≈ 7.62

   • New magnitude: ‖−2**v**‖ = √(36 + 196) = √232 ≈ 15.23

   • Ratio: 15.23 / 7.62 ≈ 2 ✓ (twice as long)

   • Direction: (6, −14) vs (−3, 7) - signs are opposite ✓

**Insight:** Scalar multiplication by a negative number does two things at once: it flips the direction (the negative part) and scales the magnitude (the absolute value part). The factor −2 means: flip it around, then stretch it to twice the length.

## Key Takeaways

- ✓

  A vector has both **magnitude** (length) and **direction** - think of it as an arrow, not just a number
- ✓

  **Components** (x, y) describe a vector by how far it goes horizontally and vertically
- ✓

  **Magnitude** uses the Pythagorean theorem: ‖(x, y)‖ = √(x² + y²)
- ✓

  **Vector addition** is component-wise: (a, b) + (c, d) = (a+c, b+d)
- ✓

  **Scalar multiplication** scales each component: c · (x, y) = (cx, cy)
- ✓

  **Negative scalars** flip direction; positive scalars preserve it
- ✓

  **Unit vectors** have magnitude 1; the standard basis is **î** = (1,0) and **ĵ** = (0,1)
- ✓

  Any vector can be written as x**î** + y**ĵ** - a weighted combination of the basis vectors

## Common Mistakes

- ✗

  **Adding magnitudes instead of vectors:** If two perpendicular forces have magnitudes 3 and 4, the combined magnitude is 5 (not 7). You must add the vectors, not the magnitudes. Direction matters!
- ✗

  **Confusing magnitude with a component:** The vector (3, 4) has magnitude 5, not 3 or 4. The magnitude is the diagonal distance; components are horizontal and vertical steps.
- ✗

  **Thinking vectors are fixed in place:** Two arrows with the same length and direction are the SAME vector, even if drawn at different positions. Vectors are 'free' - they don't have a home location.
- ✗

  **Treating î and ĵ as special:** They're just convenient names for (1, 0) and (0, 1). Any vector of magnitude 1 is a unit vector. The î-ĵ notation is just another way to write components.

## Practice

easy

Given **u** = (2, −5) and **v** = (−3, 4), compute:

(a) **u** + **v**

(b) **u** − **v**

(c) 3**u**

(d) 2**u** − **v**

**Hint:** For (d), first compute 2**u** = (4, −10), then subtract **v** component by component.

Show solution

(a) (−1, −1)

(b) (5, −9)

(c) (6, −15)

(d) (4−(−3), −10−4) = (7, −14)

medium

Find the magnitude of **w** = (7, 24) and create a unit vector in its direction.

**Hint:** Check if 7² + 24² is a perfect square. Then divide each component by the magnitude.

Show solution

‖**w**‖ = √(49 + 576) = √625 = 25. Unit vector: **ŵ** = (7/25, 24/25) = (0.28, 0.96)

hard

A plane aims north at 200 mph airspeed, but a 50 mph wind blows from the west (pushing it eastward). Find the plane's actual velocity over the ground: both speed and direction.

**Hint:** Plane's heading: (0, 200). Wind's effect: (50, 0). Add them. Find magnitude for speed and use arctan for angle.

Show solution

**v** = (0, 200) + (50, 0) = (50, 200).

Speed = √(2500 + 40000) = √42500 ≈ 206 mph.

Direction: arctan(50/200) ≈ 14° east of north.

## Connections

Vectors build directly on the [Coordinate Plane](/tech-tree/coordinate-plane/) - without coordinates, we couldn't write vectors as components.

From here, vectors unlock:

• [Dot Product](/tech-tree/dot-product/) - measuring alignment between vectors (are they pointing the same way?)

• [Matrix Operations](/tech-tree/matrix-operations/) - matrices transform vectors via multiplication

• [Gradients](/tech-tree/gradients/) - the derivative as a vector in multivariable calculus

• [Neural Networks](/tech-tree/neural-networks/) - layers are just matrix-vector multiplications

• [Vector Embeddings](/tech-tree/vector-embeddings/) - representing words and concepts as vectors

In physics: force, velocity, and acceleration are all vectors. In ML: feature vectors, weight matrices, gradient descent - vectors everywhere.

Mastering vectors now pays compound interest across everything technical.

Quality: A (4.5/5)

[← back to tree](/tech-tree/)[browse all →](/tech-tree/inventory/)
