---
title: Numerical Stability and Conditioning
description: Principles for avoiding floating-point issues (overflow/underflow, catastrophic cancellation) and understanding problem conditioning; includes common fixes like log-sum-exp, normalization, and careful initialization. These concerns are crucial for reliable training of deep models.
date: '2026-07-01'
scheduled: '2026-11-06'
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
inspiration_url: https://templeton.host/tech-tree/numerical-stability/
inspiration_category: tech-tree
---

> Source-copy draft imported from [https://templeton.host/tech-tree/numerical-stability/](https://templeton.host/tech-tree/numerical-stability/). Names, domain references, and local media paths were adapted for Xavi Ablaza / getablaza.com.

[←Back to Tech Tree](/tech-tree/)

[inventory](/tech-tree/inventory/)[coverage](/tech-tree/coverage/)

# Numerical Stability and Conditioning

AlgorithmsDifficulty: ★★★★☆Depth: 1Unlocks: 4

Principles for avoiding floating-point issues (overflow/underflow, catastrophic cancellation) and understanding problem conditioning; includes common fixes like log-sum-exp, normalization, and careful initialization. These concerns are crucial for reliable training of deep models.

## Interactive Visualization

⏮◀◀▶▶STEP0.25x1xZOOM

t=0s

## Core Concepts

- -Finite-precision arithmetic: rounding error and limited dynamic range causing overflow/underflow

## Key Symbols & Notation

epsilon\_machine (machine epsilon, unit roundoff)

## Essential Relationships

- -Ill-conditioned problems (high condition number) amplify rounding errors and catastrophic cancellation into large relative errors
- -Algebraic reformulation and scaling (e.g., log-domain, normalization, careful scaling/initialization) mitigate overflow/underflow and reduce cancellation effects

## Prerequisites (2)

[Activation Functions6 atoms](/tech-tree/activation-functions/)[Computational Graphs6 atoms](/tech-tree/computational-graphs/)

## Unlocks (1)

[Deep Learninglvl 5](/tech-tree/deep-learning/)

Advanced Learning Details

### Graph Position

16

Depth Cost

4

Fan-Out (ROI)

2

Bottleneck Score

1

Chain Length

### Cognitive Load

4

Atomic Elements

43

Total Elements

L3

Percentile Level

L2

Atomic Level

### All Concepts (21)

- - Floating-point representation and finite precision: numbers are represented with limited mantissa and exponent leading to quantization of real values
- - Machine epsilon (unit roundoff): the basic bound on relative rounding error for a floating-point operation
- - Rounding error: error introduced by replacing real arithmetic with finite-precision arithmetic
- - Absolute error vs relative error: two ways to quantify discrepancy between true and computed values
- - Overflow: computed magnitude too large to represent in the floating-point format
- - Underflow: computed magnitude too small to represent in the normalized floating-point format
- - Subnormal (denormal) numbers and flush-to-zero behaviors: representation/handling of tiny magnitudes and their performance/accuracy implications
- - Catastrophic cancellation (loss of significance): large relative error produced when subtracting nearly equal floating-point numbers
- - Condition number of a problem (κ or cond): a scalar quantifying how sensitive the output is to small changes in input
- - Well-conditioned vs ill-conditioned problems: qualitative labels based on condition number magnitude
- - Numerical stability of algorithms: whether an algorithm amplifies or controls rounding errors during computation
- - Forward error vs backward error: two ways to measure algorithmic error (difference in outputs vs input perturbation that explains output)
- - Backward/forward stability definitions: backward-stable algorithm yields exact solution to a slightly perturbed problem; forward-stable implies small forward error
- - Loss of associativity in floating-point arithmetic and its consequences (order of operations matters)
- - Log-domain computations (e.g., log-sum-exp) as a general technique to avoid overflow/underflow for exponentials/products
- - Numerically stable implementations of common primitives (e.g., stable softmax/log-sum-exp)
- - Compensated summation (e.g., Kahan summation): an algorithmic technique to reduce accumulated rounding error in sums
- - Normalization and scaling as numerical fixes: rescaling inputs/weights/activations to keep numeric ranges safe
- - Careful initialization to control numeric ranges of activations/gradients (beyond activation gradient properties)
- - Gradient clipping as a practical fix to prevent numeric explosion of gradients in training
- - Algorithmic vs problem-level remedies: choosing numerically stable algorithms vs reformulating the problem to improve conditioning

### Teaching Strategy

Self-serve tutorial - low prerequisites, straightforward concepts.

Training deep models is often less about “the math is wrong” and more about “the math was computed in a fragile way.” Numerical stability is the craft of making mathematically correct formulas behave reliably under finite-precision floating-point arithmetic—so your softmax doesn’t overflow, your variance doesn’t go negative, and your gradients don’t silently drift due to reduction order.

TL;DR:

Finite-precision arithmetic introduces rounding and a limited dynamic range. Numerical stability is about choosing *algorithms* that control rounding error and avoid overflow/underflow; conditioning is about how sensitive the *problem itself* is to small input perturbations. In deep learning, common fixes include log-sum-exp for softmax/log-likelihoods, stable variance/normalization formulas, careful reduction (pairwise/Kahan), and scale-aware initialization/normalization—especially in float16/float32 training.

## What Is Numerical Stability and Conditioning?

### Why you should care (before any formulas)

You can write down a correct mathematical expression and still get nonsense on a real computer.

- •A softmax that should produce probabilities returns **NaN** because e1000e^{1000}e1000 overflowed.
- •A variance that should be nonnegative becomes **slightly negative**, and then a square root yields **NaN**.
- •The same sum of numbers gives different answers depending on the order you add them.

These aren’t “bugs” in deep learning libraries—they’re consequences of *finite-precision arithmetic*.

Numerical analysis separates two ideas:

1. 1)**Conditioning (problem sensitivity)**: if we slightly perturb the input, how much can the *true answer* change?
2. 2)**Stability (algorithm robustness)**: given rounding errors and finite precision, does our *computed answer* stay close to the true answer of a nearby input?

A well-conditioned problem can be solved poorly by an unstable algorithm. A well-designed stable algorithm cannot fully rescue an *ill-conditioned* problem—but it can avoid making things worse.

---

### Floating-point reality: rounding + limited dynamic range

Computers represent real numbers in floating-point format (float16/float32/float64). Two consequences matter constantly:

- •**Rounding error**: most real numbers cannot be represented exactly, so operations are rounded.
- •**Limited dynamic range**: numbers that are too large overflow to ∞; too small underflow toward 0 (sometimes with subnormals).

A standard model of floating-point arithmetic is:

fl(a∘b)=(a∘b)(1+δ),∣δ∣≤u\mathrm{fl}(a \circ b) = (a \circ b)(1 + \delta), \quad |\delta| \le ufl(a∘b)=(a∘b)(1+δ),∣δ∣≤u

where:

- •∘\circ∘ is +++, −-−, ×\times×, or ///,
- •uuu is the **unit roundoff**, often roughly half of machine epsilon.

We’ll use **machine epsilon** (often denoted εmachine\varepsilon\_{\text{machine}}εmachine​) as the “scale” of relative rounding error.

Typical values (approximate):

| type | significand bits | εmachine\varepsilon\_{\text{machine}}εmachine​ (≈) | dynamic range (rough) |
| --- | --- | --- | --- |
| float16 | 11 (incl. hidden bit) | 9.77e-4 | ~1e−5 to ~6e4 |
| bfloat16 | 8 (incl. hidden bit) | 7.81e-3 | ~1e−38 to ~3e38 |
| float32 | 24 | 1.19e-7 | ~1e−38 to ~3e38 |
| float64 | 53 | 2.22e-16 | ~1e−308 to ~1e308 |

Two important takeaways:

- •float16 has much *worse precision* and a *much smaller max value* than float32.
- •bfloat16 has low precision like float16 but a large exponent range like float32.

---

### Conditioning: “how sensitive is the math problem?”

Consider computing f(x)f(x)f(x). If a tiny perturbation Δx\Delta xΔx can cause a large change in f(x)f(x)f(x), the problem is ill-conditioned near xxx.

A classic measure is the **relative condition number**:

κf(x)≈∣xf′(x)f(x)∣\kappa\_f(x) \approx \left|\frac{x f'(x)}{f(x)}\right|κf​(x)≈​f(x)xf′(x)​​

Interpretation:

- •If κf(x)\kappa\_f(x)κf​(x) is large, then a small relative error in xxx can produce a large relative error in f(x)f(x)f(x).

Example intuition:

- •f(x)=xf(x) = xf(x)=x has κ≈1\kappa \approx 1κ≈1 (well-conditioned).
- •f(x)=1/xf(x) = 1/xf(x)=1/x near x=0x=0x=0 is ill-conditioned (tiny changes in xxx blow up the output).

In deep learning, conditioning shows up as:

- •nearly singular matrices (e.g., Hessians, Jacobians)
- •poorly scaled features/activations
- •exploding/vanishing gradients

---

### Stability: “does the algorithm amplify rounding errors?”

An algorithm is (backward) stable if the computed result equals the exact result for a slightly perturbed input:

y^=f(x+Δx),with ∥Δx∥ small (on the order of rounding).\hat{y} = f(x + \Delta x), \quad \text{with } \|\Delta x\| \text{ small (on the order of rounding).}y^​=f(x+Δx),with ∥Δx∥ small (on the order of rounding).

This is the gold standard: rounding happens anyway; stability means your algorithm behaves like it just saw a tiny bit of noise.

**Key mental model**:

- •Conditioning is about the landscape you’re standing on.
- •Stability is about whether you’re walking carefully or running with untied shoelaces.

---

### Supporting static diagram (conceptual): float spacing vs magnitude

A core stability intuition is that floats are *denser near 0* and *sparser at large magnitudes*.

```
value magnitude:   0 ---- 1 ---- 10 ---- 1e3 ---- 1e6 ---- 1e9
float spacing:     tiny  small  bigger   larger   huge     enormous
```

At large magnitudes, the next representable number can be far away, so adding a small number can do *nothing* (it rounds away). This drives reduction-order issues and “small updates disappear” problems.

## Core Mechanic 1: Failure Modes in Finite-Precision Arithmetic

This section builds a concrete catalog of failure modes you will repeatedly see in ML code. The goal is to recognize them quickly, then reach for the right stable pattern.

---

## 1) Overflow and underflow

### What it is

- •**Overflow**: a value exceeds the largest representable finite float → becomes ∞.
- •**Underflow**: a value is too small in magnitude → becomes 0 (or subnormal, then 0).

### Why ML triggers it

Exponentials, products over many terms, and repeated multiplications are common.

- •Softmax uses ezie^{z\_i}ezi​.
- •Likelihoods multiply probabilities.
- •Deep nets multiply Jacobians across layers.

### Classic example: softmax overflow

Naive softmax:

softmax(z)i=ezi∑jezj\mathrm{softmax}(\mathbf{z})\_i = \frac{e^{z\_i}}{\sum\_j e^{z\_j}}softmax(z)i​=∑j​ezj​ezi​​

If some ziz\_izi​ is large (say 1000 in float32), ezie^{z\_i}ezi​ overflows to ∞, and you get ∞/∞ → NaN.

---

## 2) Catastrophic cancellation

### What it is

Subtracting two nearly equal numbers destroys significant digits.

If a≈ba \approx ba≈b, then a−ba - ba−b is small, but the floating-point representation of aaa and bbb each has rounding error. The subtraction exposes that error.

### Why ML triggers it

- •variance computations
- •normalization
- •loss differences
- •some distance computations

### Example: variance via “E[x²] − (E[x])²”

The identity is correct:

Var(x)=E[x2]−(E[x])2\mathrm{Var}(x) = \mathbb{E}[x^2] - (\mathbb{E}[x])^2Var(x)=E[x2]−(E[x])2

But numerically, if xxx has large mean and small variance, both terms are large and close, so subtraction cancels digits. You may get a small negative result.

---

## 3) Reduction-order (summation) error

### What it is

Floating-point addition is not associative:

(a+b)+c≠a+(b+c)(a + b) + c \ne a + (b + c)(a+b)+c=a+(b+c)

because each intermediate sum is rounded.

### Why ML triggers it

Training is full of reductions:

- •summing losses over a batch
- •summing gradients
- •dot products and matrix multiplies

On GPU/TPU, parallel reductions change order depending on hardware and scheduling. That can change results—usually slightly, sometimes significantly.

### A helpful intuition

If you add a tiny number to a huge number, the tiny number may not change the sum at all (it gets rounded away). So order matters: adding small numbers together first can preserve more information.

---

## 4) Division by tiny numbers / unstable normalization

Normalization often has the form:

x^=x−μσ\hat{x} = \frac{x - \mu}{\sigma}x^=σx−μ​

If σ\sigmaσ is near 0, this blows up. Many algorithms add an ε\varepsilonε term:

x^=x−μσ2+ε\hat{x} = \frac{x - \mu}{\sqrt{\sigma^2 + \varepsilon}}x^=σ2+ε​x−μ​

The ε\varepsilonε here is a *stability constant*, not machine epsilon (though it’s motivated by it). In float16, ε\varepsilonε often must be larger.

---

## 5) Gradients that vanish due to underflow or saturation

Even if your forward pass is stable, gradients can underflow or become 0 in low precision.

Examples:

- •sigmoid/tanh saturation: for large |x|, derivatives are near 0.
- •multiplying many small factors across layers.

This interacts with floating-point: values smaller than ~1e−8 may become subnormals or 0 in float16.

---

## 6) Infs/NaNs that propagate through a computational graph

Given prerequisites about computational graphs, here’s the key operational point:

- •One NaN in forward → many NaNs in backward.
- •One overflow in an activation (e.g., exp) → NaNs in loss → NaN gradients.

This is why stable local formulas (softmax, log-softmax, normalization) matter so much: they sit early in the graph and affect everything.

---

## Interactive canvas specification (explicitly maps to 3 failure modes)

To address these issues systematically, your interactive canvas should have **three mini-labs**, each with:

- •a toggle for precision: float16 / float32 / float64
- •side-by-side traces: **naive** vs **stable**
- •a plot of intermediate values (including detection of inf/nan)

### Mini-lab A: Softmax overflow

**Controls**:

- •slider: max logit magnitude (e.g., from 0 to 2000)
- •toggle: stable shift (subtract max) on/off
- •precision selector

**Display**:

- •naive exp(logits), sum exp, softmax output
- •stable exp(logits − max), sum exp, softmax output
- •highlight when overflow happens

### Mini-lab B: Cancellation in variance

**Controls**:

- •slider: mean magnitude μ (e.g., 0 to 1e6)
- •slider: true std σ (e.g., 1e−2 to 10)
- •toggle: one-pass (E[x²]−E[x]²) vs Welford
- •precision selector

**Display**:

- •computed variance (naive vs stable)
- •difference from ground truth
- •highlight negative variance events

### Mini-lab C: Reduction-order error

**Controls**:

- •choose data distribution: (many small + few large), alternating signs, random
- •toggle: left-to-right sum vs pairwise sum vs Kahan
- •precision selector

**Display**:

- •final sum
- •absolute/relative error vs high-precision reference
- •step-by-step accumulation trace to show where small terms get lost

This canvas ties directly to: overflow in softmax, cancellation in variance, and reduction-order error—the three most common “why did my model blow up?” numerics in practice.

## Core Mechanic 2: Stable Patterns and Derivations You’ll Reuse Constantly

Now we turn the failure modes into stable, reusable techniques.

---

## 1) Log-sum-exp (LSE): the workhorse for stable exponentials

### Motivation

You want to compute:

log⁡∑i=1nezi\log \sum\_{i=1}^n e^{z\_i}logi=1∑n​ezi​

Directly computing ezie^{z\_i}ezi​ is risky if any ziz\_izi​ is large.

### Trick: factor out the maximum

Let m=max⁡izim = \max\_i z\_im=maxi​zi​. Then:

∑iezi=∑iemezi−m=em∑iezi−m\sum\_i e^{z\_i} = \sum\_i e^{m} e^{z\_i - m} = e^{m} \sum\_i e^{z\_i - m}i∑​ezi​=i∑​emezi​−m=emi∑​ezi​−m

Taking log:

log⁡∑iezi=m+log⁡∑iezi−m\log \sum\_i e^{z\_i} = m + \log \sum\_i e^{z\_i - m}logi∑​ezi​=m+logi∑​ezi​−m

Key benefits:

- •all exponents zi−m≤0z\_i - m \le 0zi​−m≤0, so ezi−m∈(0,1]e^{z\_i - m} \in (0, 1]ezi​−m∈(0,1]
- •prevents overflow
- •reduces risk of underflow dominating the sum (though very negative values may still underflow safely to 0)

### Connection to softmax and log-softmax

Stable softmax:

softmax(z)i=ezi−m∑jezj−m\mathrm{softmax}(\mathbf{z})\_i = \frac{e^{z\_i - m}}{\sum\_j e^{z\_j - m}}softmax(z)i​=∑j​ezj​−mezi​−m​

Stable log-softmax:

log⁡softmax(z)i=zi−(m+log⁡∑jezj−m)\log \mathrm{softmax}(\mathbf{z})\_i = z\_i - \left(m + \log \sum\_j e^{z\_j - m}\right)logsoftmax(z)i​=zi​−(m+logj∑​ezj​−m)

In practice you compute log-softmax directly (stable) and then NLL loss, rather than softmax then log.

---

## 2) Stable variance: Welford’s algorithm

### Motivation

Variance is everywhere: batch norm, layer norm, feature scaling, monitoring.

The naive formula is prone to cancellation:

Var=E[x2]−(E[x])2\mathrm{Var} = \mathbb{E}[x^2] - (\mathbb{E}[x])^2Var=E[x2]−(E[x])2

### Welford’s one-pass stable update

Given samples x1,x2,…,xnx\_1, x\_2, \dots, x\_nx1​,x2​,…,xn​, maintain:

- •running mean μk\mu\_kμk​
- •running sum of squares of deviations M2kM2\_kM2k​

Initialize:

- •μ1=x1\mu\_1 = x\_1μ1​=x1​
- •M21=0M2\_1 = 0M21​=0

For k≥2k \ge 2k≥2:

δ=xk−μk−1\delta = x\_k - \mu\_{k-1}δ=xk​−μk−1​

μk=μk−1+δk\mu\_k = \mu\_{k-1} + \frac{\delta}{k}μk​=μk−1​+kδ​

δ2=xk−μk\delta\_2 = x\_k - \mu\_kδ2​=xk​−μk​

M2k=M2k−1+δ⋅δ2M2\_k = M2\_{k-1} + \delta \cdot \delta\_2M2k​=M2k−1​+δ⋅δ2​

Then:

Var=M2nn(population)orM2nn−1(sample)\mathrm{Var} = \frac{M2\_n}{n} \quad (\text{population}) \qquad \text{or} \qquad \frac{M2\_n}{n-1} \quad (\text{sample})Var=nM2n​​(population)orn−1M2n​​(sample)

### Why it helps

It avoids subtracting two nearly equal large numbers. It tracks deviations relative to an evolving mean, keeping intermediate quantities closer to the scale of the variance.

---

## 3) Stable summation: pairwise and Kahan

### Motivation

Summing many numbers is ubiquitous: losses, gradient accumulation, dot products.

### Pairwise summation

Instead of summing linearly, sum in a tree (balanced) structure. This tends to reduce error growth from O(nu)O(nu)O(nu) to closer to O(log⁡n⋅u)O(\log n \cdot u)O(logn⋅u) in many practical settings.

### Kahan compensated summation

Maintain a compensation term ccc for lost low-order bits.

Algorithm (for summing values xix\_ixi​):

- •s=0s = 0s=0, c=0c = 0c=0
- •For each xxx:
- •y=x−cy = x - cy=x−c
- •t=s+yt = s + yt=s+y
- •c=(t−s)−yc = (t - s) - yc=(t−s)−y
- •s=ts = ts=t

Interpretation: ccc estimates what was lost to rounding.

### Practical note for ML

- •Many BLAS/GEMM kernels already use strategies to reduce error, but you still see reduction issues in custom kernels, metrics, and loss aggregation.
- •Mixed precision often accumulates in float32 even if operands are float16 (a major stability improvement).

---

## 4) Normalization and scaling as stability tools

Normalization isn’t only about optimization speed; it’s also about preventing overflow/underflow and controlling conditioning.

### Feature scaling

If one feature has magnitude ~1e6 and another ~1e−3, dot products and gradients become ill-scaled. Scaling features can reduce condition numbers and improve numerical behavior.

### Activation scaling and initialization

Careful initialization (e.g., Xavier/He) aims to keep variance of activations/gradients roughly stable across depth. That’s partly a conditioning story (keeping Jacobian singular values reasonable) and partly a numerical range story (avoid overflow/underflow).

---

## 5) Conditioning vs stability: a quadrant you should internalize

A useful mental diagram:

|  | Stable algorithm | Unstable algorithm |
| --- | --- | --- |
| **Well-conditioned problem** | Great: accurate results | Often fixable by changing algorithm |
| **Ill-conditioned problem** | Best you can do: results sensitive to noise | Worst case: meaningless results |

Deep learning often has *locally ill-conditioned* regions (e.g., during early training or near sharp minima). Your job is to avoid compounding that with unstable computations.

---

## 6) Mixed precision stability patterns

Modern training often uses float16/bfloat16 for speed, with float32 master weights or accumulators.

Common stability patterns:

- •**Loss scaling**: multiply loss by a scale factor to prevent gradient underflow in float16; then unscale before the optimizer step.
- •**FP32 accumulation**: accumulate sums/products in float32 (especially reductions).
- •**Keep sensitive ops in FP32**: softmax/log-softmax, normalization stats, some reductions.

These are not “cheats”—they’re explicit numerics engineering.

## Applications/Connections: Reliable Deep Learning Training in Practice

This section connects the numerics toolbox to everyday deep learning components.

---

## 1) Softmax + cross-entropy: do not compute them separately (naively)

In classification, the loss is often:

L=−log⁡softmax(z)y\mathcal{L} = -\log \mathrm{softmax}(\mathbf{z})\_yL=−logsoftmax(z)y​

Naively:

1) compute softmax

2) take log

This is numerically fragile because:

- •softmax can overflow
- •probabilities can underflow to 0, then log(0) → −∞

Stable approach:

- •compute **log-softmax** via log-sum-exp
- •index the correct class

This avoids both overflow and log(0) underflow.

---

## 2) BatchNorm/LayerNorm: stable mean/variance and safe eps

Normalization layers compute statistics over batches/features.

Key stability decisions:

- •Use stable variance computation (often a two-pass or Welford-like approach internally).
- •Choose ε\varepsilonε appropriate to dtype and scale.

Important nuance:

- •ε\varepsilonε is not a universal constant; it depends on typical activation magnitudes and precision.
- •In float16, using too-small ε\varepsilonε can fail to prevent division blow-ups.

---

## 3) Attention and Transformers: “scaled dot-product” is a numerics fix

Attention uses logits:

zij=qi⋅kjdz\_{ij} = \frac{\mathbf{q}\_i \cdot \mathbf{k}\_j}{\sqrt{d}}zij​=d​qi​⋅kj​​

Then softmax over jjj.

The $1/\sqrt{d}$ scaling is partly about gradients/optimization, but also about numerics:

- •without scaling, dot products can grow with ddd, producing large logits
- •large logits make softmax overflow more likely and cause saturation (one-hot attention)

FlashAttention and similar kernels implement careful stabilization (blockwise softmax with max-subtraction) explicitly to keep values in safe ranges.

---

## 4) Log-likelihoods, HMMs, CRFs: stay in log space

Whenever you multiply many probabilities, underflow is inevitable:

∏tpt→0\prod\_t p\_t \to 0t∏​pt​→0

Use logs:

log⁡∏tpt=∑tlog⁡pt\log \prod\_t p\_t = \sum\_t \log p\_tlogt∏​pt​=t∑​logpt​

And whenever you need to sum probabilities in log space, use log-sum-exp.

This pattern generalizes far beyond softmax.

---

## 5) Gradient clipping and normalization as overflow control

Exploding gradients can cause:

- •weight updates that overflow
- •activations that overflow next step

Gradient clipping (by norm) can be viewed as enforcing a bound on magnitude to keep values in range.

---

## 6) Debugging numerics systematically (a checklist)

When training becomes NaN/Inf:

1. 1)**Locate first NaN/Inf** in the forward pass (hooks / anomaly detection).
2. 2)Check common culprits:

- •softmax/log-softmax
- •normalization variance / division by small numbers
- •exp, log, sqrt
- •mixed precision overflow/underflow

3. 3)Try interventions:

- •replace softmax+log with log-softmax
- •increase normalization eps
- •enable FP32 accumulation
- •use loss scaling
- •clamp logits or activations (carefully)

A key mindset: you’re not only debugging code—you’re debugging a numeric process under rounding.

---

## 7) Connecting conditioning to optimization behavior

Conditioning appears as “how hard the optimizer must work.”

- •If the Hessian has a wide spread of eigenvalues, gradient descent zig-zags.
- •Normalization, adaptive optimizers, and preconditioning methods try to reduce effective condition number.

While this lesson focuses on floating-point issues, it’s important to see that:

- •better conditioning → often fewer extreme values → fewer numeric failures
- •stable numerics → fewer NaNs → more reliable optimization signals

## Worked Examples (3)

### Worked Example 1: Stable Softmax and Log-Softmax via Log-Sum-Exp

Let logits be **z** = [1000, 1001, 999]. Compute softmax and log-softmax stably (in exact math), and explain what goes wrong with the naive computation in float32.

1. Naive softmax uses exp(zᵢ). But exp(1000) and exp(1001) overflow in float32, producing ∞.

   So the naive numerator/denominator become ∞/∞, which is undefined → NaN.
2. Use the stability shift m = max(z) = 1001.

   Compute shifted logits: z' = z − m = [−1, 0, −2].
3. Compute exponentials of shifted logits:

   exp(z') = [e^{−1}, e^{0}, e^{−2}] = [0.367879..., 1, 0.135335...].

   These are all in (0, 1], safe in float16/32/64.
4. Compute denominator:

   S = 0.367879... + 1 + 0.135335... = 1.503214...
5. Compute softmax:

   softmax(z) = exp(z') / S

   = [0.367879/1.503214, 1/1.503214, 0.135335/1.503214]

   ≈ [0.244728, 0.665241, 0.090031].
6. Compute log-sum-exp:

   LSE(z) = m + log(∑ exp(zᵢ − m))

   = 1001 + log(1.503214...)

   ≈ 1001 + 0.407606 = 1001.407606.
7. Compute log-softmax:

   log softmax(z)ᵢ = zᵢ − LSE(z)

   So:

   log softmax = [1000 − 1001.407606,

   1001 − 1001.407606,

   999 − 1001.407606]

   = [−1.407606, −0.407606, −2.407606].
8. Sanity check: exponentiating log-softmax returns the softmax probabilities:

   exp(−0.407606) ≈ 0.665241, etc.

**Insight:** Subtracting max(logits) is not a heuristic; it’s an algebraically exact transformation that keeps exponentials in a safe numeric range. Log-sum-exp is the reusable pattern: whenever you see log(sum(exp(·))), you should think “shift by max.”

### Worked Example 2: Catastrophic Cancellation in Variance (Naive vs Welford)

Suppose x values are near 1e8 with tiny spread: x = [100000000.0, 100000001.0, 99999999.0, 100000000.0]. Show why Var = E[x²] − (E[x])² is fragile, and outline Welford’s stable computation.

1. Compute the mean (exact math):

   μ = (100000000 + 100000001 + 99999999 + 100000000) / 4

   = 400000000 / 4 = 100000000.
2. Compute deviations from the mean:

   (x − μ) = [0, 1, −1, 0].

   So the true population variance is:

   Var = (0² + 1² + (−1)² + 0²)/4 = 2/4 = 0.5.
3. Now look at the naive formula components:

   E[x²] is about (1e8)² = 1e16 scale.

   (μ)² is also (1e8)² = 1e16 scale.

   Their difference should be 0.5 — extremely tiny relative to 1e16.
4. In float32, you only have ~7 decimal digits of precision.

   At magnitude 1e16, the spacing between representable floats is huge (much larger than 1).

   So x² and μ² are rounded so coarsely that subtracting them cannot reliably yield 0.5.

   This is catastrophic cancellation: the small result is dominated by rounding error in the large terms.
5. Welford’s algorithm avoids subtracting huge nearly-equal numbers.

   Initialize:

   μ₁ = x₁ = 100000000

   M2₁ = 0
6. k=2, x₂=100000001:

   δ = x₂ − μ₁ = 1

   μ₂ = μ₁ + δ/2 = 100000000 + 0.5 = 100000000.5

   δ₂ = x₂ − μ₂ = 0.5

   M2₂ = M2₁ + δ·δ₂ = 0 + 1·0.5 = 0.5
7. k=3, x₃=99999999:

   δ = x₃ − μ₂ = 99999999 − 100000000.5 = −1.5

   μ₃ = μ₂ + δ/3 = 100000000.5 − 0.5 = 100000000.0

   δ₂ = x₃ − μ₃ = −1

   M2₃ = 0.5 + (−1.5)(−1) = 2.0
8. k=4, x₄=100000000:

   δ = x₄ − μ₃ = 0

   μ₄ = μ₃ + 0/4 = 100000000

   δ₂ = 0

   M2₄ = 2.0
9. Population variance:

   Var = M2₄ / 4 = 2/4 = 0.5 (correct).

**Insight:** The naive identity is mathematically correct but numerically dangerous when mean ≫ std. Welford keeps intermediate values near the scale of deviations, so rounding error doesn’t get amplified by subtracting huge nearly-equal numbers.

### Worked Example 3: Reduction-Order Error in Summation

Sum the numbers: [1e8, 1, −1e8] in float32-like arithmetic to illustrate non-associativity. Compare (a+b)+c vs a+(b+c).

1. Let a = 1e8, b = 1, c = −1e8.
2. Compute (a + b) + c:

   First a + b = 1e8 + 1.

   At magnitude 1e8 in float32, the spacing between representable floats is larger than 1, so 1e8 + 1 rounds to 1e8.

   So (a+b) ≈ 1e8.

   Then (a+b)+c ≈ 1e8 + (−1e8) = 0.
3. Compute a + (b + c):

   First b + c = 1 + (−1e8) = −99999999.

   This is representable near −1e8 and keeps the +1 effect.

   Then a + (b+c) = 1e8 + (−99999999) = 1.
4. So:

   (a+b)+c ≈ 0, but a+(b+c) ≈ 1.

   Same real-number expression, different floating-point result due to rounding in intermediate steps.

**Insight:** Summation order matters because adding a tiny number to a huge one can lose the tiny number entirely. Pairwise summation and compensated summation reduce this loss, which matters for large reductions (loss totals, gradient sums, dot products).

## Key Takeaways

- ✓

  Finite-precision arithmetic means every operation is rounded; machine epsilon (and unit roundoff) sets the scale of relative rounding error.
- ✓

  Overflow/underflow are about limited dynamic range; catastrophic cancellation and reduction-order error are about limited precision.
- ✓

  Conditioning describes sensitivity of the true solution to input perturbations; stability describes whether an algorithm controls rounding error (often via backward stability).
- ✓

  Log-sum-exp (shift by max) is the standard fix for softmax/log-softmax and log-probability computations.
- ✓

  Variance is a classic cancellation trap; prefer Welford or stable two-pass methods over E[x²] − (E[x])² when mean ≫ std.
- ✓

  Floating-point addition is not associative; for large reductions, consider pairwise summation, FP32 accumulation, or compensated summation.
- ✓

  Normalization and scale-aware initialization help both optimization conditioning and numerical range control.
- ✓

  In mixed precision, keep sensitive ops and accumulations in FP32 and use loss scaling to prevent gradient underflow.

## Common Mistakes

- ✗

  Computing softmax then log for cross-entropy instead of using a stable log-softmax (log-sum-exp).
- ✗

  Using Var = E[x²] − (E[x])² in low precision when data have a large mean and small variance, leading to negative variance and NaNs.
- ✗

  Assuming sums/reductions are deterministic and associative across hardware; changing parallel reduction order can change results.
- ✗

  Confusing the stability epsilon added in normalizations (a modeling/engineering constant) with machine epsilon (a property of the dtype).

## Practice

easy

Compute stably: L = log( exp(100) + exp(101) + exp(99) ). Give the exact stable expression and a numerical approximation (to ~4 decimals).

**Hint:** Use m = max = 101 and write L = m + log(∑ exp(zᵢ − m)).

Show solution

Let m = 101.

Then:

L = 101 + log( exp(100−101) + exp(101−101) + exp(99−101) )

= 101 + log( e^{−1} + 1 + e^{−2} ).

Compute: e^{−1}≈0.3679, e^{−2}≈0.1353, sum≈1.5032.

So L ≈ 101 + log(1.5032) ≈ 101 + 0.4076 = 101.4076.

medium

You are summing 10 million float16 values to compute a loss total. Name two strategies to reduce summation error and briefly explain why each helps.

**Hint:** Think about changing the summation order and using higher precision for the accumulator.

Show solution

Two good strategies:

1) Accumulate in float32 (FP32 accumulation): float32 has much smaller ε\_machine than float16, so each addition rounds less, reducing total error.

2) Pairwise/tree reduction (or compensated summation like Kahan): summing numbers of similar magnitude earlier reduces the “tiny added to huge gets lost” effect, lowering rounding error compared to naive left-to-right summation.

hard

Explain (no code required) why computing cross-entropy as −log(softmax(z)[y]) can produce −∞ or NaN even when the true value is finite. Then state the stable alternative formula.

**Hint:** Consider underflow in softmax probabilities and overflow in exp(z). Use log-sum-exp.

Show solution

Naively computing softmax requires exp(z). Large logits can overflow exp(z) to ∞, producing ∞/∞ → NaN. Small probabilities can underflow to 0, and then log(0) → −∞, even if the mathematically correct probability is merely very small but nonzero. The stable approach is to compute log-softmax directly:

log softmax(z)ᵢ = zᵢ − (m + log ∑ⱼ exp(zⱼ − m)), where m = maxⱼ zⱼ.

Then cross-entropy is −log softmax(z)\_y, avoiding overflow and log(0) underflow.

## Connections

- •[Activation Functions](/tech-tree/activation-functions/)
- •[Computational Graphs](/tech-tree/computational-graphs/)
- •[Deep Learning](/tech-tree/deep-learning/)

Related next-step ideas you’ll likely meet in the Deep Learning node:

- •Mixed precision training (loss scaling, FP32 master weights)
- •Stable attention implementations (blockwise softmax / FlashAttention)
- •Gradient clipping and normalization layers as numerics + conditioning tools

Quality: A (4.2/5)

[← back to tree](/tech-tree/)[browse all →](/tech-tree/inventory/)
