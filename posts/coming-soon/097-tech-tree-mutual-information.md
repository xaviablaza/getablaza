---
title: Mutual Information
description: Shared information between two variables. I(X;Y) = H(X) - H(X|Y).
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
permalink: /tech-tree/mutual-information/
---

[←Back to Tech Tree](/tech-tree/)

[inventory](/tech-tree/inventory/)[coverage](/tech-tree/coverage/)

# Mutual Information

Information TheoryDifficulty: ★★★☆☆Depth: 7Unlocks: 3

Shared information between two variables. I(X;Y) = H(X) - H(X|Y).

## Interactive Visualization

⏮◀◀▶▶STEP0.25x1xZOOM

t=0s

## Core Concepts

- -Mutual information: the amount by which knowledge of one variable reduces uncertainty about the other.
- -Nonnegativity and independence: mutual information is >= 0 and equals 0 exactly when the variables are independent.

## Key Symbols & Notation

I(X;Y) - mutual information

## Essential Relationships

- -I(X;Y) = H(X) - H(X|Y) (equivalently H(Y) - H(Y|X) = H(X)+H(Y)-H(X,Y)).
- -I(X;Y) equals the Kullback-Leibler divergence between the joint distribution and the product of marginals: I(X;Y) = KL( P(X,Y) || P(X)P(Y) ).

## Prerequisites (2)

[Entropy5 atoms](/tech-tree/entropy/)[Joint Distributions6 atoms](/tech-tree/joint-distributions/)

## Unlocks (3)

[Information Bottlenecklvl 4](/tech-tree/information-bottleneck/)[Rate-Distortion Theorylvl 5](/tech-tree/rate-distortion/)[Channel Capacitylvl 5](/tech-tree/channel-capacity/)

## Referenced by (1)

Where this concept shows up in the operating-finance and personal-finance graphs.

### From Business (1)

[Data MoatBusiness

A data moat formally exists when I(proprietary\_data; Y | public\_data) > 0 - your data shares information with the target that public data does not, which is the mathematical condition justifying custom model investment](/business/data-moat/)

Advanced Learning Details

### Graph Position

95

Depth Cost

3

Fan-Out (ROI)

3

Bottleneck Score

7

Chain Length

### Cognitive Load

5

Atomic Elements

21

Total Elements

L0

Percentile Level

L3

Atomic Level

### All Concepts (7)

- - Mutual information: I(X;Y) - the amount of information shared between X and Y, i.e., how much observing Y on average reduces uncertainty about X (and vice versa)
- - Conditional entropy H(X|Y) as the expected remaining uncertainty in X after observing Y (used in the I=H(X)-H(X|Y) expression)
- - Pointwise mutual information (PMI) pmi(x;y) = log p(x,y) / (p(x)p(y)): the information contribution of a specific outcome pair (x,y)
- - Mutual information as an average/aggregate of PMI over the joint distribution
- - Mutual information as a measure of statistical dependence that captures any (not only linear) association between variables
- - Interpretation of mutual information in operational terms: expected reduction in bits/nats of uncertainty about one variable from knowing the other
- - Units of mutual information depend on the logarithm base (bits for log base 2, nats for natural log)

### Teaching Strategy

Quick unlock - significant prerequisite investment but simple final step. Verify prerequisites first.

Mutual information answers a deceptively simple question: “How many bits do X and Y actually share?” It’s the quantity that turns vague notions like “correlated”, “predictive”, and “dependent” into a precise, operational measure in bits (or nats).

TL;DR:

Mutual information measures how much knowing one random variable reduces uncertainty about the other:

I(X;Y) = H(X) − H(X|Y) = H(Y) − H(Y|X) = H(X)+H(Y)−H(X,Y).

It is always ≥ 0, equals 0 iff X and Y are independent, and can be viewed as a KL divergence: I(X;Y) = D\_KL(p(x,y) ‖ p(x)p(y)).

## What Is Mutual Information?

### Why we need it (motivation)

Entropy H(X) tells you how uncertain X is *by itself*. But many problems are about *relationships*:

- •Does sensor Y tell us anything about the true state X?
- •Does label Y contain information about feature X?
- •How many bits can a channel input X reliably transmit to output Y?

Correlation is not enough: it’s linear, scale-dependent, and can miss nonlinear dependence. We want a measure that:

1. 1)Works for any (discrete) distributions, not just Gaussian.
2. 2)Is measured in **bits** (or nats), so it composes with entropy.
3. 3)Has a crisp meaning: reduction in uncertainty.

Mutual information does exactly this.

### Definition (core idea)

Let X and Y be discrete random variables with joint distribution p(x,y). The **mutual information** between X and Y is

I(X;Y) = H(X) − H(X|Y).

Interpretation:

- •H(X) = uncertainty in X before seeing Y.
- •H(X|Y) = remaining uncertainty in X after seeing Y.
- •Their difference is the **expected reduction** in uncertainty about X gained by observing Y.

Because the definition is symmetric (as we’ll prove), I(X;Y) is also how much X tells you about Y.

### Units and log base

If you use log₂, I(X;Y) is in **bits**. If you use natural log, it’s in **nats**. The math is identical; only the scale changes.

### A concrete mental picture

Think of X as a hidden message and Y as a noisy observation.

- •If Y perfectly determines X, then H(X|Y)=0 ⇒ I(X;Y)=H(X).
- •If Y is unrelated to X, then H(X|Y)=H(X) ⇒ I(X;Y)=0.

So mutual information is a knob between 0 and “all of H(X)” depending on how informative Y is.

### Equivalent forms (you should recognize all of these)

We can rewrite I(X;Y) in several equivalent ways:

1) **Symmetric conditional-entropy form**

I(X;Y) = H(X) − H(X|Y) = H(Y) − H(Y|X).

2) **Joint-entropy form**

I(X;Y) = H(X) + H(Y) − H(X,Y).

3) **Expectation of a log-likelihood ratio**

I(X;Y) = ∑ₓ ∑ᵧ p(x,y) log( p(x,y) / (p(x)p(y)) ).

4) **KL divergence form**

I(X;Y) = D\_KL( p(x,y) ‖ p(x)p(y) ).

Each form emphasizes something different:

- •H(X) − H(X|Y): “how much uncertainty is reduced?”
- •H(X)+H(Y)−H(X,Y): “how much overlap between two entropies?”
- •KL form: “how far from independence is the joint distribution?”

### A small table of interpretations

| Expression | What it highlights | Useful when |
| --- | --- | --- |
| I(X;Y)=H(X)−H(X | Y) | information gain about X from Y | prediction, feature usefulness |
| I(X;Y)=H(X)+H(Y)−H(X,Y) | overlap/shared randomness | Venn-style intuition, algebra |
| I(X;Y)=∑ p log(p/(pp)) | average log ratio | manual computation from tables |
| I(X;Y)=D\_KL(p(x,y)‖p(x)p(y)) | deviation from independence | proving ≥0, theory |

Mutual information will become a central “currency” later in channel capacity and information bottleneck.

## Core Mechanic 1: Algebraic Identities and “Shared Bits”

### Why identities matter

Mutual information shows up inside larger derivations (channel capacity, rate–distortion, variational bounds). If you can fluidly switch between its equivalent forms, many proofs become “one line” instead of opaque.

We’ll derive the key identities carefully.

### Derivation: I(X;Y) = H(X) + H(Y) − H(X,Y)

Start from the definition:

I(X;Y) = H(X) − H(X|Y).

Use the chain rule for entropy:

H(X,Y) = H(Y) + H(X|Y).

Solve this for H(X|Y):

H(X|Y) = H(X,Y) − H(Y).

Substitute back:

I(X;Y)

= H(X) − (H(X,Y) − H(Y))

= H(X) − H(X,Y) + H(Y)

= H(X) + H(Y) − H(X,Y).

That’s the “overlap” form.

### Symmetry: I(X;Y) = H(Y) − H(Y|X)

The overlap form is symmetric in X and Y:

I(X;Y) = H(X) + H(Y) − H(X,Y) = I(Y;X).

So mutual information doesn’t care which variable you call “input” vs “output”.

### Interpreting the overlap form

- •H(X)+H(Y) counts uncertainty in each variable separately.
- •H(X,Y) counts uncertainty in the pair together.

If X and Y share some randomness, then the pair is “less uncertain” than the sum, and the difference is the shared part.

This is where the common Venn-diagram intuition comes from. (Be cautious: entropy isn’t literally a set measure, but the algebra matches.)

### Bounds you should know

From I(X;Y) = H(X) − H(X|Y):

- •Since conditional entropy is nonnegative, H(X|Y) ≥ 0 ⇒

I(X;Y) ≤ H(X).

Similarly, I(X;Y) ≤ H(Y).

So:

0 ≤ I(X;Y) ≤ min{H(X), H(Y)}.

The upper bound is achievable when one variable is a deterministic function of the other (e.g., Y=f(X) with no collisions). Then knowing one fully determines the other, up to the smaller entropy.

### Mutual information as “expected surprise reduction”

Another way to read the definition is pointwise.

Define pointwise mutual information (PMI):

pmi(x,y) = log( p(x,y) / (p(x)p(y)) ).

Then

I(X;Y) = E[ pmi(X,Y) ] = ∑ₓ ∑ᵧ p(x,y) pmi(x,y).

So mutual information is the *average* log factor by which the joint probability differs from what independence would predict.

- •If (x,y) occurs more often than independence suggests, pmi(x,y) > 0.
- •If it occurs less often, pmi(x,y) < 0.
- •The average across the true joint distribution is always ≥ 0 (we’ll show why next).

### A quick intuition check

- •Perfectly informative: If Y=X for a fair bit, then H(X)=1, H(X|Y)=0 ⇒ I=1 bit.
- •Totally uninformative: If Y is an independent coin flip, then H(X|Y)=H(X) ⇒ I=0.

This is the “shared bits” story: mutual information counts how many bits about X are carried by Y, on average.

## Core Mechanic 2: Nonnegativity, Independence, and the KL View

### Why this matters

Two foundational facts make mutual information reliable:

1. 1)**Nonnegativity:** I(X;Y) ≥ 0 always.
2. 2)**Independence criterion:** I(X;Y)=0 iff X and Y are independent.

These properties are not obvious from H(X) − H(X|Y) alone, because conditional entropy can behave in unintuitive ways (especially in continuous settings). The cleanest explanation comes from KL divergence.

### Derivation: I(X;Y) as KL divergence

Start from the overlap form:

I(X;Y) = H(X) + H(Y) − H(X,Y).

Write each entropy as an expectation:

H(X) = −∑ₓ p(x) log p(x)

H(Y) = −∑ᵧ p(y) log p(y)

H(X,Y) = −∑ₓ∑ᵧ p(x,y) log p(x,y).

Plug in:

I(X;Y)

= −∑ₓ p(x) log p(x) − ∑ᵧ p(y) log p(y) + ∑ₓ∑ᵧ p(x,y) log p(x,y).

Convert the marginal sums into joint sums (since ∑ᵧ p(x,y)=p(x), ∑ₓ p(x,y)=p(y)):

−∑ₓ p(x) log p(x)

= −∑ₓ∑ᵧ p(x,y) log p(x)

−∑ᵧ p(y) log p(y)

= −∑ₓ∑ᵧ p(x,y) log p(y)

So

I(X;Y)

= ∑ₓ∑ᵧ p(x,y) log p(x,y)

− ∑ₓ∑ᵧ p(x,y) log p(x)

− ∑ₓ∑ᵧ p(x,y) log p(y)

Combine logs:

I(X;Y)

= ∑ₓ∑ᵧ p(x,y) log( p(x,y) / (p(x)p(y)) ).

Now recognize this as a KL divergence:

D\_KL( p(x,y) ‖ p(x)p(y) )

= ∑ₓ∑ᵧ p(x,y) log( p(x,y) / (p(x)p(y)) ).

Therefore:

I(X;Y) = D\_KL( p(x,y) ‖ p(x)p(y) ).

### Nonnegativity

KL divergence is always nonnegative:

D\_KL(P ‖ Q) ≥ 0,

with equality iff P=Q almost everywhere.

So immediately:

I(X;Y) ≥ 0.

This is a major reason the KL form is beloved: it packages a deep inequality into a known theorem (Gibbs’ inequality).

### Independence criterion

Equality holds iff

p(x,y) = p(x)p(y) for all x,y with p(x,y)>0.

But that is exactly the definition of independence. Hence:

I(X;Y) = 0 ⇔ X ⟂ Y.

This gives mutual information a crisp meaning as a *dependence measure*.

### How to interpret the KL view

- •p(x)p(y) is the “best guess” joint distribution if you assume independence.
- •p(x,y) is reality.
- •Mutual information is the penalty (in expected log-loss) for using the independence model when the true data are dependent.

In bits (log₂), it tells you how many extra bits per sample you pay, on average, by pretending the variables are independent.

### A dependence measure with nuance

Mutual information detects any dependence, not just linear.

- •If Y = X² and X is symmetric around 0, correlation can be 0, but I(X;Y) > 0.

That makes it especially useful in machine learning for feature selection and representation learning, where dependencies are often nonlinear.

### Conditional mutual information (preview)

A closely related quantity you’ll likely meet soon is:

I(X;Y|Z) = H(X|Z) − H(X|Y,Z).

It measures how much X and Y share *after accounting for* Z. It appears in graphical models and in information bottleneck derivations. You don’t need it yet, but it’s helpful to see that mutual information fits into a larger family of “information differences.”

## Application/Connection: Why Mutual Information Powers Compression and Communication

### Why mutual information is a “currency”

In many systems you:

- •**compress** something (keep fewer bits)
- •but want to **preserve relevant information**
- •or **transmit** information through a noisy channel

Mutual information becomes the natural objective/constraint because it counts how many bits about one variable survive into another.

### 1) Channel capacity (communication)

A channel takes an input X and produces an output Y according to p(y|x). If you choose an input distribution p(x), the channel induces a joint p(x,y)=p(x)p(y|x).

The quantity I(X;Y) measures how much information the output reveals about the input under that choice of p(x).

Shannon capacity is:

C = max\_{p(x)} I(X;Y).

Interpretation:

- •You can pick how often you use each input symbol.
- •Different choices yield different amounts of reliably transferable information.
- •Capacity is the best achievable rate (bits per channel use) with vanishing error.

Mutual information is the objective because it precisely measures “how many bits made it through.”

### 2) Rate–distortion (lossy compression)

Suppose X is a source and you compress it into a representation Ŷ (often written X̂) that is allowed to be imperfect, controlled by a distortion measure d(x, x̂).

Rate–distortion theory studies:

minimize I(X;X̂)

subject to E[d(X,X̂)] ≤ D.

Meaning:

- •I(X;X̂) is the number of bits your compressed representation must retain about X.
- •The constraint controls how much quality you lose.

Again, I(·;·) is the *rate*.

### 3) Information bottleneck (learning useful representations)

In supervised learning, you often want a representation T that compresses X but keeps what matters for Y.

The information bottleneck formalizes this tradeoff:

minimize I(X;T) − β I(T;Y).

Interpretation:

- •I(X;T): how much of X is stored in the representation (compression pressure).
- •I(T;Y): how much label-relevant information is preserved (prediction pressure).

This objective is built entirely out of mutual information terms.

### 4) Feature selection and dependence testing

If you are deciding which feature Xᵢ to keep for predicting Y, a common heuristic is to prefer larger I(Xᵢ;Y). Unlike correlation, this works for arbitrary discrete relationships.

Caution: estimating mutual information from finite data can be tricky (bias, binning choices), but conceptually it’s a powerful criterion.

### Summary of where it plugs in

| Domain | Variables | Role of mutual information |
| --- | --- | --- |
| Communication | input X, output Y | maximize I(X;Y) to get capacity |
| Lossy compression | source X, reconstruction X̂ | minimize I(X;X̂) under distortion |
| Representation learning | data X, rep T, target Y | trade off I(X;T) vs I(T;Y) |
| Statistics | two measurements X,Y | test dependence via I(X;Y) |

Mutual information is the bridge between probability models and operational goals: how many bits you can transmit, store, or preserve.

## Worked Examples (3)

### Compute I(X;Y) for a Binary Symmetric Channel (BSC)

Let X ∈ {0,1} be a fair bit: p(x=0)=p(x=1)=1/2. Let Y be X flipped with probability ε (0 ≤ ε ≤ 1/2):

- •p(y=x) = 1−ε
- •p(y≠x) = ε

Compute I(X;Y) in bits (log₂).

1. Step 1: Compute H(X).

   X is fair ⇒ H(X)=1 bit.
2. Step 2: Compute H(X|Y).

   For a BSC with a fair input, the posterior p(x|y) has the same error rate ε:

   - •p(x=y | y)=1−ε
   - •p(x≠y | y)=ε

   So H(X|Y=y) = H₂(ε), where H₂(ε)= −ε log₂ ε − (1−ε) log₂(1−ε).
3. Step 3: Average over y.

   Because H(X|Y=y) is the same for y=0 and y=1,

   H(X|Y)=∑ᵧ p(y) H(X|Y=y)=H₂(ε).
4. Step 4: Use I(X;Y)=H(X)−H(X|Y).

   I(X;Y)=1 − H₂(ε).

**Insight:** A BSC destroys information exactly according to the binary entropy of its flip probability. When ε=0, H₂(0)=0 ⇒ I=1 bit (perfect). When ε=1/2, H₂(1/2)=1 ⇒ I=0 bits (pure noise).

### Mutual Information is Zero Exactly for Independence (via KL)

Show that I(X;Y)=0 if and only if X and Y are independent, using the identity I(X;Y)=D\_KL(p(x,y) ‖ p(x)p(y)).

1. Step 1: Start from the KL form.

   I(X;Y)=D\_KL(p(x,y) ‖ p(x)p(y)).
2. Step 2: Use the fundamental property of KL divergence.

   For any distributions P,Q on the same support:

   D\_KL(P ‖ Q) ≥ 0,

   with equality iff P=Q (for all outcomes where P>0).
3. Step 3: Apply it to the joint vs product-of-marginals.

   I(X;Y)=0 ⇔ D\_KL(p(x,y) ‖ p(x)p(y))=0 ⇔ p(x,y)=p(x)p(y) for all relevant (x,y).
4. Step 4: Recognize independence.

   The condition p(x,y)=p(x)p(y) is exactly the definition of X ⟂ Y.

**Insight:** Mutual information is the “distance from independence” measured in KL divergence. This makes nonnegativity and the independence criterion immediate.

### Compute I(X;Y) from a Small Joint Table

Let X,Y ∈ {0,1} with joint distribution:

- •p(0,0)=0.4
- •p(0,1)=0.1
- •p(1,0)=0.1
- •p(1,1)=0.4

Compute I(X;Y) in bits.

1. Step 1: Compute marginals.

   p(x=0)=0.4+0.1=0.5, p(x=1)=0.1+0.4=0.5.

   p(y=0)=0.4+0.1=0.5, p(y=1)=0.1+0.4=0.5.
2. Step 2: Use the log-ratio formula.

   I(X;Y)=∑ₓ∑ᵧ p(x,y) log₂( p(x,y) / (p(x)p(y)) ).

   Here p(x)p(y)=0.5·0.5=0.25 for all pairs.
3. Step 3: Compute each term.

   For (0,0): 0.4 · log₂(0.4/0.25)=0.4 · log₂(1.6).

   For (0,1): 0.1 · log₂(0.1/0.25)=0.1 · log₂(0.4).

   For (1,0): 0.1 · log₂(0.1/0.25)=0.1 · log₂(0.4).

   For (1,1): 0.4 · log₂(0.4/0.25)=0.4 · log₂(1.6).
4. Step 4: Combine.

   I = 0.8 · log₂(1.6) + 0.2 · log₂(0.4).

   Use log₂(1.6)≈0.6781 and log₂(0.4)≈−1.3219.

   So I ≈ 0.8·0.6781 + 0.2·(−1.3219)

   ≈ 0.5425 − 0.2644

   ≈ 0.2781 bits.

**Insight:** Even with uniform marginals, dependence appears as probability mass concentrating on (0,0) and (1,1). Mutual information quantifies that dependence at ≈0.278 bits—not huge, but clearly nonzero.

## Key Takeaways

- ✓

  Mutual information measures shared information: I(X;Y)=H(X)−H(X|Y).
- ✓

  It is symmetric: I(X;Y)=I(Y;X)=H(X)+H(Y)−H(X,Y).
- ✓

  I(X;Y) can be written as an expectation: I(X;Y)=∑ p(x,y) log( p(x,y)/(p(x)p(y)) ).
- ✓

  KL view: I(X;Y)=D\_KL(p(x,y) ‖ p(x)p(y)) makes key properties immediate.
- ✓

  Nonnegativity: I(X;Y) ≥ 0 always (Gibbs’ inequality).
- ✓

  Independence: I(X;Y)=0 ⇔ p(x,y)=p(x)p(y) ⇔ X ⟂ Y.
- ✓

  Bounds: 0 ≤ I(X;Y) ≤ min{H(X), H(Y)}; equality on the right when one variable determines the other.
- ✓

  Mutual information is the core objective/constraint in channel capacity, rate–distortion, and information bottleneck.

## Common Mistakes

- ✗

  Thinking “I(X;Y)=0 means uncorrelated.” Zero correlation is weaker than independence; mutual information detects nonlinear dependence.
- ✗

  Mixing log bases mid-problem (log₂ vs ln), leading to inconsistent units (bits vs nats).
- ✗

  Forgetting to compute marginals correctly when using I(X;Y)=∑ p log(p/(pp)).
- ✗

  Assuming I(X;Y)=H(X)+H(Y) (it’s H(X)+H(Y)−H(X,Y)); the joint entropy matters.

## Practice

easy

Let X be a fair bit and let Y=X (deterministic copy). Compute I(X;Y).

**Hint:** Use I(X;Y)=H(X)−H(X|Y). What is H(X|Y) when Y determines X?

Show solution

Since Y=X, knowing Y reveals X exactly ⇒ H(X|Y)=0. Also H(X)=1 bit (fair). Therefore I(X;Y)=1−0=1 bit.

medium

Let X,Y ∈ {0,1} with joint distribution p(0,0)=0.25, p(0,1)=0.25, p(1,0)=0.25, p(1,1)=0.25. Compute I(X;Y).

**Hint:** Check whether p(x,y)=p(x)p(y). If yes, mutual information is zero.

Show solution

The distribution is uniform, so p(x)=0.5 and p(y)=0.5. Then p(x)p(y)=0.25 for each pair, matching p(x,y). Thus X and Y are independent and I(X;Y)=0 bits.

hard

Suppose X has entropy H(X)=3 bits. A representation T satisfies H(X|T)=1.2 bits. (a) Compute I(X;T). (b) Give one sentence interpreting the result.

**Hint:** Mutual information is the reduction in uncertainty: I(X;T)=H(X)−H(X|T).

Show solution

(a) I(X;T)=H(X)−H(X|T)=3−1.2=1.8 bits.

(b) Observing T reduces uncertainty about X by 1.8 bits on average; equivalently, T retains 1.8 bits of information about X.

## Connections

Next nodes you can unlock with this concept:

- •[Information Bottleneck](/tech-tree/information-bottleneck/) — formalizes representation learning as a tradeoff between I(X;T) and I(T;Y).
- •[Rate-Distortion Theory](/tech-tree/rate-distortion/) — uses I(X;X̂) as the rate needed for lossy compression at distortion D.
- •[Channel Capacity](/tech-tree/channel-capacity/) — defines capacity as maxₚ(x) I(X;Y), the maximum reliable communication rate.

Related background:

- •[Entropy](/tech-tree/entropy/) — H(X) and H(X|Y) are the building blocks of I(X;Y).
- •[Joint Distributions](/tech-tree/joint-distributions/) — computing p(x,y), p(x), p(y), and p(x|y) is required to evaluate mutual information.

Quality: A (4.5/5)

[← back to tree](/tech-tree/)[browse all →](/tech-tree/inventory/)
