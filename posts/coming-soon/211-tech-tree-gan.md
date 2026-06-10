---
title: Generative Adversarial Networks
description: Generator vs discriminator training. Minimax game.
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
permalink: /tech-tree/gan/
---

[←Back to Tech Tree](/tech-tree/)

[inventory](/tech-tree/inventory/)[coverage](/tech-tree/coverage/)

# Generative Adversarial Networks

Machine LearningDifficulty: ★★★★★Depth: 11Unlocks: 0

Generator vs discriminator training. Minimax game.

## Interactive Visualization

⏮◀◀▶▶STEP0.25x1xZOOM

t=0s

## Core Concepts

- -Generator: a parametric function that transforms a latent noise vector into synthetic data samples
- -Discriminator: a parametric binary classifier that scores inputs for 'realness' (real vs. generated)
- -Adversarial minimax objective: a two-player zero-sum training goal where the discriminator improves distinction and the generator tries to fool the discriminator

## Key Symbols & Notation

G (generator function)D (discriminator function)z (latent noise/input to G)

## Essential Relationships

- -Generation: G maps z -> x\_fake (synthetic data)
- -Discrimination: D(x) outputs probability that x is real, applied to both real x and G(z)
- -Adversarial optimization: D updates to increase its classification score on real vs fake while G updates to decrease D's ability to distinguish (minimax game)

## Prerequisites (2)

[Neural Networks6 atoms](/tech-tree/neural-networks/)[Zero-Sum Games5 atoms](/tech-tree/zero-sum-games/)

## Referenced by (1)

Where this concept shows up in the operating-finance and personal-finance graphs.

### From Business (1)

[auditingBusiness

Automated adversarial generation is the GAN paradigm applied to quality assurance - a generator produces inputs designed to fool or break the system, which is the mathematical foundation of red-teaming and adversarial robustness testing](/business/auditing/)

Advanced Learning Details

### Graph Position

178

Depth Cost

0

Fan-Out (ROI)

0

Bottleneck Score

11

Chain Length

### Cognitive Load

9

Atomic Elements

49

Total Elements

L4

Percentile Level

L4

Atomic Level

### All Concepts (18)

- - Generator network G: a parametric model that maps samples z from a simple latent prior to data-space samples x (x = G(z))
- - Latent prior p\_z(z): a simple known distribution (e.g., Gaussian, uniform) from which latent vectors z are sampled
- - Implicit model distribution p\_g(x): the probability distribution over data-space induced by pushing p\_z through G (p\_g is defined implicitly via sampling)
- - Discriminator D: a parametric model that scores or outputs the probability that an input x is real vs generated
- - Adversarial (minimax) value function V(G,D): the specific objective used in original GANs combining expectations over real and generated samples
- - Alternating adversarial training: the practical optimization procedure that alternates updates that maximize D’s objective and updates that minimize G’s objective
- - Optimal discriminator D\*(x): the closed-form best-response discriminator given p\_data and p\_g (used in theoretical analysis)
- - Divergence minimization interpretation: training G under the original GAN objective corresponds to minimizing a statistical divergence between p\_g and p\_data (specifically linked to Jensen–Shannon divergence)
- - Non-saturating generator loss (heuristic): an alternative loss for G used in practice to avoid vanishing gradients (maximize log D(G(z)) instead of minimizing log(1 - D(G(z))))
- - Mode collapse: a common GAN failure mode where G maps many distinct z to the same/few outputs, reducing diversity
- - Instability and dynamics of adversarial training: oscillatory or divergent training dynamics arising from simultaneous competing objectives
- - Wasserstein (Earth-Mover) GAN idea: replace the original JS-based objective with the Wasserstein distance to provide more meaningful gradients when supports are disjoint
- - Critic vs discriminator distinction: in WGAN-style methods the critic outputs unconstrained real scores (not probabilities) used in the Wasserstein dual
- - 1-Lipschitz constraint on the critic: the requirement that the critic belong to the set of 1-Lipschitz functions (needed to make the Wasserstein dual valid), and practical enforcement methods (weight clipping, gradient penalty)
- - Implicit density modeling (no explicit likelihood): GANs model a generative process via sampling, not an explicit p(x) formula for likelihood evaluation
- - Pushforward mapping concept: the formal notion that G pushes the latent distribution p\_z forward to produce p\_g
- - Nash equilibrium in GANs: the equilibrium condition where p\_g = p\_data and the discriminator cannot distinguish generated from real samples
- - Practical evaluation challenges: metrics and empirical methods (e.g., FID/Inception Score) are needed because explicit likelihoods are not available

### Teaching Strategy

Multi-session curriculum - substantial prior knowledge and complex material. Use mastery gates and deliberate practice.

GANs turn “learning to generate data” into a competitive game: one network forges samples, another network plays detective. The surprising part is that this duel—if balanced—pushes the forger toward the true data distribution without ever explicitly writing down a likelihood.

TL;DR:

A Generative Adversarial Network (GAN) trains a generator G(z) to map latent noise **z** to synthetic samples, and a discriminator D(x) to classify real vs. generated. Training is a two-player zero-sum minimax game:

min\_G max\_D 𝔼\_{x∼p\_data}[log D(x)] + 𝔼\_{z∼p(z)}[log(1 − D(G(z)))]

At the discriminator optimum, GAN training corresponds to minimizing a divergence (Jensen–Shannon) between the data distribution p\_data and the model distribution p\_g induced by G. In practice, stability depends on keeping G and D in balance, using good losses (often non-saturating), regularization (e.g., gradient penalty), architectural constraints, and careful optimization.

## What Is a Generative Adversarial Network (GAN)?

### Why GANs exist (motivation)

Many machine learning tasks are *discriminative*: given x, predict y. But in generation, we want to *sample new x* that look like they came from an unknown data distribution p\_data(x) (images, audio, text embeddings, etc.). One classical approach is to define an explicit probabilistic model p\_θ(x) and maximize likelihood. That can be hard when the data distribution is complex, multi-modal, and high-dimensional.

GANs offer a different route: instead of writing down p\_θ(x) and computing likelihoods, you train a neural network to *produce samples* and another neural network to *judge samples*. The “judge” becomes a learned loss function that adapts to the generator’s current weaknesses.

### The core idea (two networks)

A GAN contains two parametric functions:

- •**Generator** G: takes a latent noise vector **z** (e.g., **z** ∼ 𝓝(0, I)) and outputs a synthetic sample.
- •For images: G(**z**) ∈ ℝ^{H×W×C}
- •Think of G as a *differentiable simulator*.

- •**Discriminator** D: takes a sample x and outputs a scalar score interpreted as the probability the input is real:
- •D(x) ∈ (0, 1)
- •D is a binary classifier: real (label 1) vs fake (label 0)

Intuitively:

- •D becomes good at spotting artifacts in G’s outputs.
- •G updates to remove those artifacts.

### The minimax game (zero-sum objective)

The classic GAN objective is:

V(D, G) = 𝔼\_{x∼p\_data}[log D(x)] + 𝔼\_{z∼p(z)}[log(1 − D(G(z)))]

The game is:

max\_D min\_G V(D, G)

(or commonly written as min\_G max\_D V(D, G))

- •D wants to **maximize** V: assign high D(x) for real data, low D(G(z)) for generated.
- •G wants to **minimize** V: make D(G(z)) large so that log(1 − D(G(z))) becomes small (i.e., D thinks fakes are real).

### What does “success” look like?

If training reaches an equilibrium:

- •The generated distribution p\_g matches p\_data.
- •D cannot tell real vs fake better than chance.

In that ideal case:

- •D(x) = 1/2 for all x in the support.
- •Samples from G are indistinguishable (statistically) from real data.

### A mental model (for pacing)

Think of p\_data as a complicated cloud in a high-dimensional space. G pushes forward a simple latent distribution p(z) through a neural network to produce a new distribution p\_g. The discriminator learns a moving “boundary” between the two clouds. G then moves its cloud to cross that boundary.

This creates an important theme you will see repeatedly:

- •GANs are powerful because the loss is *learned* (D adapts).
- •GANs are hard because the target is *moving* (D keeps changing), and the game can become imbalanced.

By the end of this lesson, you should be able to:

- •derive the optimal discriminator for fixed G,
- •connect the minimax objective to divergence minimization,
- •explain why training is unstable and how modern variants fix it,
- •reason about practical training loops and diagnostics.

## Core Mechanic 1: The Minimax Objective and the Optimal Discriminator

### Why analyze the discriminator first?

GAN training alternates between updating D and updating G. To understand what G is really optimizing, we first ask:

> If G were fixed, what discriminator D is best?

This is the “inner loop” of the minimax problem. Solving it reveals the divergence GANs implicitly minimize.

### Step 1: Write the value function as an integral

Let p\_g be the distribution of samples x = G(**z**) when **z** ∼ p(z). Then:

V(D, G) = 𝔼\_{x∼p\_data}[log D(x)] + 𝔼\_{x∼p\_g}[log(1 − D(x))]

Rewrite as:

V(D, G) = ∫ p\_data(x) log D(x) dx + ∫ p\_g(x) log(1 − D(x)) dx

Combine integrals:

V(D, G) = ∫ [ p\_data(x) log D(x) + p\_g(x) log(1 − D(x)) ] dx

### Step 2: Optimize D pointwise

For a fixed x, define:

f\_x(D(x)) = p\_data(x) log D(x) + p\_g(x) log(1 − D(x))

Since x is fixed, p\_data(x) and p\_g(x) are constants. We maximize f\_x over D(x) ∈ (0, 1).

Differentiate with respect to D(x):

∂f\_x/∂D = p\_data(x)/D(x) − p\_g(x)/(1 − D(x))

Set derivative to 0:

p\_data(x)/D*(x) = p\_g(x)/(1 − D*(x))

Solve for D\*(x):

p\_data(x) (1 − D*(x)) = p\_g(x) D*(x)

p\_data(x) − p\_data(x) D*(x) = p\_g(x) D*(x)

p\_data(x) = (p\_data(x) + p\_g(x)) D\*(x)

D\*(x) = p\_data(x) / (p\_data(x) + p\_g(x))

This is the optimal discriminator for a fixed generator.

### Interpretation

- •If p\_data(x) ≫ p\_g(x), then D\*(x) ≈ 1: x is likely real.
- •If p\_g(x) ≫ p\_data(x), then D\*(x) ≈ 0: x is likely fake.
- •If p\_data(x) = p\_g(x), then D\*(x) = 1/2.

So D is estimating a density ratio.

### Step 3: Plug D\* back in to see what G is minimizing

Compute:

V(D\*, G) = ∫ p\_data(x) log( p\_data(x)/(p\_data(x)+p\_g(x)) ) dx

- •∫ p\_g(x) log( p\_g(x)/(p\_data(x)+p\_g(x)) ) dx

Let m(x) = (1/2)(p\_data(x) + p\_g(x)) be the mixture distribution. Note that:

p\_data(x)/(p\_data(x)+p\_g(x)) = p\_data(x)/(2m(x))

p\_g(x)/(p\_data(x)+p\_g(x)) = p\_g(x)/(2m(x))

Then:

V(D\*, G) = ∫ p\_data(x) log( p\_data(x)/(2m(x)) ) dx + ∫ p\_g(x) log( p\_g(x)/(2m(x)) ) dx

Split out log(1/2):

V(D\*, G) = ∫ p\_data(x) [log(p\_data(x)/m(x)) + log(1/2)] dx

- •∫ p\_g(x) [log(p\_g(x)/m(x)) + log(1/2)] dx

Use that ∫ p\_data(x) dx = 1 and ∫ p\_g(x) dx = 1:

V(D\*, G) = (∫ p\_data(x) log(p\_data(x)/m(x)) dx) + (∫ p\_g(x) log(p\_g(x)/m(x)) dx) + 2 log(1/2)

Recognize KL divergences:

KL(p\_data ‖ m) = ∫ p\_data(x) log(p\_data(x)/m(x)) dx

KL(p\_g ‖ m) = ∫ p\_g(x) log(p\_g(x)/m(x)) dx

Thus:

V(D\*, G) = KL(p\_data ‖ m) + KL(p\_g ‖ m) − 2 log 2

The Jensen–Shannon divergence is:

JSD(p\_data ‖ p\_g) = (1/2) KL(p\_data ‖ m) + (1/2) KL(p\_g ‖ m)

So:

V(D\*, G) = 2·JSD(p\_data ‖ p\_g) − 2 log 2

### Big conclusion

When D is optimal, minimizing V(D\*, G) with respect to G is equivalent to minimizing JSD(p\_data ‖ p\_g). The minimum is achieved when p\_g = p\_data.

### But there’s a practical twist (gradient issues)

The original minimax generator loss is:

L\_G^minimax = 𝔼\_{z∼p(z)}[log(1 − D(G(z)))]

If D becomes too good early, then D(G(z)) ≈ 0, and:

log(1 − D(G(z))) ≈ log(1) = 0

Its gradient can become very small (the generator “stalls”). A common alternative is the **non-saturating** generator loss:

L\_G^NS = − 𝔼\_{z∼p(z)}[log D(G(z))]

This has stronger gradients when D(G(z)) is small.

### Summary table of common GAN losses

| Component | Classic (minimax) | Non-saturating (common in practice) |
| --- | --- | --- |
| Discriminator objective | maximize 𝔼[log D(x)] + 𝔼[log(1−D(G(z)))] | same |
| Generator objective | minimize 𝔼[log(1−D(G(z)))] | minimize −𝔼[log D(G(z))] |
| Main benefit | clean theory | better gradients early |
| Main risk | saturation when D is strong | still unstable without regularization |

## Core Mechanic 2: Training Dynamics, Stability, and Modern Fixes

### Why GANs are tricky (motivation)

In supervised learning, you minimize a fixed loss. In GANs, the loss depends on D, which is being updated too. So optimization is not “rolling downhill” on a static surface; it’s closer to chasing a moving target in a game.

This can create:

- •**Oscillations / cycling** (you improve against the current opponent, then the opponent adapts)
- •**Mode collapse** (G produces limited variety that fools D)
- •**Vanishing gradients** (D becomes too strong)
- •**D overpowering G** or **G overpowering D** (imbalance)

Understanding these issues helps you choose objectives and regularizers.

---

## 1) Mode collapse: what it is and why it happens

### Symptom

G maps many latent vectors **z** to the same (or few) outputs:

G(**z₁**) ≈ G(**z₂**) ≈ …

So p\_g covers only a subset of modes of p\_data.

### Why it can happen (game perspective)

D provides gradients that only punish *current* mistakes. If G finds a small set of outputs that D currently misclassifies as real, G can “exploit” that weakness. If D then adapts, G may hop to another exploit, producing cycling behavior.

### Practical mitigations

- •Make D stronger but regularized (so it generalizes rather than memorizes)
- •Add techniques that encourage diversity (minibatch discrimination, unrolled GANs)
- •Use objectives with better geometry (e.g., Wasserstein)

---

## 2) Why Jensen–Shannon can be problematic

The JSD is well-behaved when distributions overlap, but in high dimensions, supports can be nearly disjoint early in training. Then D can perfectly separate real and fake, making gradients uninformative.

This motivates alternative distances/divergences with more useful gradients when supports don’t overlap much.

---

## 3) Wasserstein GAN (WGAN): a key conceptual fix

### Why Wasserstein distance?

The **Wasserstein-1** (Earth Mover) distance measures how much “mass” must move to turn one distribution into another. It can provide meaningful gradients even when supports are disjoint.

Formally:

W(p\_data, p\_g) = inf\_{γ ∈ Π(p\_data, p\_g)} 𝔼\_{(x,y)∼γ}[‖x − y‖]

This is hard to compute directly. WGAN uses the Kantorovich–Rubinstein duality:

W(p\_data, p\_g) = sup\_{‖f‖\_L ≤ 1} 𝔼\_{x∼p\_data}[f(x)] − 𝔼\_{x∼p\_g}[f(x)]

So instead of a discriminator that outputs probabilities, WGAN uses a **critic** f (often still called D) that outputs real numbers, constrained to be 1-Lipschitz.

### WGAN objectives

- •Critic maximization:

max\_f 𝔼\_{x∼p\_data}[f(x)] − 𝔼\_{z∼p(z)}[f(G(z))]

- •Generator minimization:

min\_G − 𝔼\_{z∼p(z)}[f(G(z))]

### Enforcing Lipschitzness

Original WGAN used weight clipping (crude). A widely used improvement is **WGAN-GP** (gradient penalty):

L\_D = −(𝔼\_{x∼p\_data}[f(x)] − 𝔼\_{z}[f(G(z))]) + λ 𝔼\_{\hat{x}}[(‖∇\_{\hat{x}} f(\hat{x})‖ − 1)²]

where \hat{x} are points interpolated between real and generated samples.

This penalty encourages ‖∇f‖ ≈ 1, approximating the 1-Lipschitz constraint.

---

## 4) Regularization and normalization that often matter

Even for non-WGAN GANs, regularization helps prevent D from becoming too sharp (leading to vanishing gradients).

Common tools:

| Tool | Where applied | Why it helps |
| --- | --- | --- |
| Spectral normalization | Discriminator weights | Controls Lipschitz constant, stabilizes D |
| Gradient penalty (various forms) | Discriminator | Prevents overly confident / spiky decision boundaries |
| Label smoothing / noisy labels | Discriminator targets | Reduces overconfidence, improves gradients |
| Data augmentation (DiffAugment/ADA) | D input | Prevents D from memorizing, improves sample efficiency |

---

## 5) Alternating updates (the training loop) as game solving

### Why not update both simultaneously?

If you do one gradient step on both G and D, you can get rotational dynamics rather than convergence (common in games). Alternating updates approximate solving:

- •D: move toward its best response to current G
- •G: move toward its best response to current D

A typical loop:

1. 1)For k steps: update D using real x and fake G(z)
2. 2)One step: update G to improve D(G(z))

In WGAN, k is often > 1 (e.g., 5 critic steps per generator step) early in training.

### Balance is a first-class design goal

If D is too weak:

- •gradients point in noisy directions; G can exploit quirks

If D is too strong:

- •gradients vanish (classic GAN) or become unhelpful due to overfitting

So “make D perfect” is not the goal; “make D a good teacher” is.

---

## 6) Diagnostics: how you know what’s going on

GANs are notoriously hard to evaluate, but you can still monitor:

- •D accuracy (if it’s ~100% always, D may be too strong; if ~50% always early, D may be too weak)
- •Loss curves (not always correlated with sample quality)
- •Visual inspection (for images)
- •Diversity checks (nearest neighbor comparisons, latent interpolations)
- •Quantitative metrics: FID, IS (imperfect but common)

A helpful habit: fix a set of latent vectors {**zᵢ**} and track G(**zᵢ**) over training. Mode collapse often shows up as many **zᵢ** converging to similar outputs.

## Application/Connection: How GANs Are Used (and When to Prefer Alternatives)

### Why GANs are useful in practice

GANs are most compelling when you need:

- •**High perceptual quality** samples (especially images)
- •**Fast sampling** (one forward pass through G)
- •**Implicit modeling** (no explicit likelihood)

Typical applications:

1) **Image synthesis**

- •unconditional: sample random images
- •conditional: generate a specific class or guided output

2) **Image-to-image translation**

- •change style, domain, or attributes
- •paired (Pix2Pix) vs unpaired (CycleGAN)

3) **Super-resolution and inpainting**

- •GAN loss encourages perceptual realism
- •often combined with pixel/perceptual losses

4) **Data augmentation**

- •generate additional training data (carefully—distribution shift can hurt)

### Conditional GANs (cGANs)

Often you want control: generate x conditioned on y (label, text embedding, another image).

A simple conditional objective feeds y into both G and D:

G(**z**, y) → x̃

D(x, y) → probability real

Then:

max\_D 𝔼\_{(x,y)∼p\_data}[log D(x,y)] + 𝔼\_{z,y}[log(1 − D(G(z,y), y))]

Conditional setups make the mapping easier because y reduces ambiguity (less multi-modality per condition).

### When GANs are *not* the best default

Modern diffusion models often dominate unconditional high-fidelity image generation because they are easier to train and cover modes better (at the cost of slower sampling). Autoregressive models dominate discrete sequences (text) because likelihood-based training is stable.

So a practical selection table:

| Goal | GANs | Diffusion | Autoregressive |
| --- | --- | --- | --- |
| Fast sampling | excellent | slower (many steps) | slow (token-by-token) |
| Training stability | challenging | good | good |
| Mode coverage | can be poor (collapse) | strong | strong |
| Likelihood | implicit | often implicit/approx | explicit |
| Best for | images, translation, perceptual tasks | high-fidelity images/audio | text, discrete sequences |

### Conceptual connections

GANs sit at the intersection of:

- •deep learning (neural nets as function approximators)
- •game theory (minimax equilibrium)
- •divergence minimization (implicit via D)
- •optimal transport (Wasserstein variants)

If you understand GANs deeply, you also understand a general pattern:

> Learn a generator by training an adversary that provides a task-specific discrepancy signal.

That pattern reappears in domain adaptation, imitation learning (GAIL), and robust representation learning.

## Worked Examples (3)

### Derive the optimal discriminator D\*(x) for a fixed generator G

Assume the generator G induces a distribution p\_g over x. Consider the classic GAN value function:

V(D, G) = 𝔼\_{x∼p\_data}[log D(x)] + 𝔼\_{x∼p\_g}[log(1 − D(x))].

We want the discriminator D that maximizes V for fixed G.

1. Rewrite expectations as integrals:

   V(D,G) = ∫ p\_data(x) log D(x) dx + ∫ p\_g(x) log(1 − D(x)) dx

   = ∫ [p\_data(x) log D(x) + p\_g(x) log(1 − D(x))] dx.
2. Observe that the integrand depends on D only through D(x) at each x, so we can maximize pointwise.

   For fixed x define:

   f\_x(u) = p\_data(x) log u + p\_g(x) log(1 − u), where u = D(x).
3. Differentiate with respect to u:

   ∂f\_x/∂u = p\_data(x)/u − p\_g(x)/(1 − u).
4. Set derivative to zero and solve:

   p\_data(x)/u = p\_g(x)/(1 − u)

   ⇒ p\_data(x)(1 − u) = p\_g(x)u

   ⇒ p\_data(x) = (p\_data(x) + p\_g(x))u

   ⇒ u = p\_data(x)/(p\_data(x) + p\_g(x)).
5. Conclude:

   D\*(x) = p\_data(x) / (p\_data(x) + p\_g(x)).

**Insight:** The discriminator is not “mysterious”: at optimum it estimates a density ratio. This is why GANs can be viewed as divergence minimization—D is a learned critic that compares p\_data and p\_g.

### Show that the GAN minimax objective corresponds to minimizing Jensen–Shannon divergence

Using the optimal discriminator from the previous example, compute V(D\*, G) and relate it to JSD(p\_data ‖ p\_g).

1. Start with D\*(x) = p\_data(x)/(p\_data(x)+p\_g(x)). Plug into V:

   V(D\*,G) = ∫ p\_data(x) log( p\_data(x)/(p\_data(x)+p\_g(x)) ) dx

   - •∫ p\_g(x) log( p\_g(x)/(p\_data(x)+p\_g(x)) ) dx.
2. Define the mixture distribution m(x) = (1/2)(p\_data(x)+p\_g(x)). Then:

   p\_data(x)/(p\_data(x)+p\_g(x)) = p\_data(x)/(2m(x))

   p\_g(x)/(p\_data(x)+p\_g(x)) = p\_g(x)/(2m(x)).
3. Rewrite V(D\*,G):

   V(D\*,G) = ∫ p\_data(x) log( p\_data(x)/(2m(x)) ) dx + ∫ p\_g(x) log( p\_g(x)/(2m(x)) ) dx.
4. Split logs:

   log(p\_data/(2m)) = log(p\_data/m) + log(1/2)

   log(p\_g/(2m)) = log(p\_g/m) + log(1/2).
5. Use normalization of distributions:

   ∫ p\_data(x) dx = 1, ∫ p\_g(x) dx = 1.

   So the constant terms contribute 2 log(1/2) = −2 log 2.
6. Recognize KL terms:

   ∫ p\_data(x) log(p\_data(x)/m(x)) dx = KL(p\_data ‖ m)

   ∫ p\_g(x) log(p\_g(x)/m(x)) dx = KL(p\_g ‖ m).
7. Therefore:

   V(D\*,G) = KL(p\_data ‖ m) + KL(p\_g ‖ m) − 2 log 2

   = 2·JSD(p\_data ‖ p\_g) − 2 log 2.

**Insight:** This establishes the idealized story: if D is optimized, then improving G reduces a statistical divergence. The practical story is harder because D is never fully optimized and neural nets/finite data introduce instability.

### Why the minimax generator loss can saturate (vanishing gradient intuition)

Consider the original generator loss L\_G^minimax = 𝔼\_z[log(1 − D(G(z)))]. Suppose early in training the discriminator becomes very confident: D(G(z)) ≈ 0 for most z.

1. If D(G(z)) ≈ 0 then 1 − D(G(z)) ≈ 1.
2. Thus log(1 − D(G(z))) ≈ log(1) = 0, so the loss becomes near-constant for many samples.
3. A near-constant loss implies small gradients with respect to generator parameters θ\_G because:

   ∇\_{θ\_G} log(1 − D(G(z)))

   = (1/(1 − D(G(z)))) · (−∇\_{θ\_G} D(G(z))).
4. When D(G(z)) is extremely close to 0, D often lies in a saturated region of its sigmoid, making ∇ D(G(z)) small as well (depending on discriminator parametrization).
5. Compare to non-saturating loss:

   L\_G^NS = −𝔼\_z[log D(G(z))].

   If D(G(z)) ≈ 0, then log D(G(z)) is very negative, and the gradient signal is typically stronger because the loss strongly penalizes small D(G(z)).

**Insight:** This is one of the simplest reasons GAN training can stall: if D gets too good too fast, the minimax generator objective can provide weak learning signals. Many practical GAN recipes use the non-saturating loss and/or regularize D to remain a useful teacher.

## Key Takeaways

- ✓

  A GAN defines a generator G(**z**) that induces p\_g and a discriminator D(x) that estimates “realness”; training is a two-player zero-sum minimax game.
- ✓

  For fixed G, the optimal discriminator is D\*(x) = p\_data(x)/(p\_data(x)+p\_g(x)), which acts like a density-ratio estimator.
- ✓

  With D = D*, the value function becomes V(D*,G) = 2·JSD(p\_data ‖ p\_g) − 2 log 2, so the ideal equilibrium is p\_g = p\_data and D = 1/2.
- ✓

  The classic minimax generator loss can saturate when D becomes too strong; the non-saturating generator loss −𝔼[log D(G(z))] often yields better gradients.
- ✓

  GAN training is game optimization, not ordinary minimization; oscillations and instability are expected without constraints and regularization.
- ✓

  Mode collapse occurs when G finds a small set of outputs that exploit D; mitigations include stronger-but-regularized discriminators and alternative objectives.
- ✓

  Wasserstein GAN replaces probability discrimination with a 1-Lipschitz critic to obtain more informative gradients; gradient penalties or spectral normalization help enforce constraints.

## Common Mistakes

- ✗

  Treating GAN losses like standard supervised losses and expecting monotonic convergence; in adversarial games, losses can oscillate while samples improve (or vice versa).
- ✗

  Letting the discriminator overfit or become too strong (near-perfect separation) without regularization, leading to vanishing/poor gradients for the generator.
- ✗

  Assuming that “D accuracy ≈ 50%” always means success; it can also mean both networks are weak or that D is confused due to poor training signals.
- ✗

  Ignoring mode collapse by evaluating only sample quality and not diversity (e.g., failing to test latent interpolations or nearest-neighbor comparisons).

## Practice

easy

Suppose p\_data(x) = p\_g(x) for all x. What is D*(x)? What is V(D*, G) in this case?

**Hint:** Use D*(x) = p\_data(x)/(p\_data(x)+p\_g(x)). Then plug into V(D*,G) = 2·JSD(p\_data ‖ p\_g) − 2 log 2.

Show solution

If p\_data = p\_g, then D\*(x) = p\_data(x)/(2p\_data(x)) = 1/2 for all x.

Also JSD(p\_data ‖ p\_g) = 0, so:

V(D\*,G) = 2·0 − 2 log 2 = −2 log 2.

medium

Derive ∂/∂D(x) of the integrand p\_data(x) log D(x) + p\_g(x) log(1 − D(x)), and show it yields the optimal discriminator formula when set to zero.

**Hint:** Differentiate log D(x) and log(1−D(x)) carefully: d/dD log D = 1/D and d/dD log(1−D) = −1/(1−D).

Show solution

Let u = D(x). The derivative is:

∂/∂u [p\_data log u + p\_g log(1−u)]

= p\_data·(1/u) + p\_g·(−1/(1−u))

= p\_data/u − p\_g/(1−u).

Set to 0:

p\_data/u = p\_g/(1−u)

⇒ p\_data(1−u) = p\_g u

⇒ p\_data = (p\_data+p\_g)u

⇒ u = p\_data/(p\_data+p\_g).

So D\*(x) = p\_data(x)/(p\_data(x)+p\_g(x)).

hard

You observe the discriminator achieves ~99% accuracy quickly and the generator outputs barely change over time. Propose two interventions grounded in GAN theory/practice, and explain why each helps.

**Hint:** Think: gradient saturation, overfitting of D, imbalance. Consider non-saturating loss, regularization (spectral norm, gradient penalty), data augmentation, or changing update ratios.

Show solution

Two plausible interventions:

1) Use the non-saturating generator loss L\_G^NS = −𝔼\_z[log D(G(z))] instead of the minimax loss 𝔼\_z[log(1−D(G(z)))].

Reason: when D(G(z)) is near 0, log(1−D(G(z))) is near 0 and can provide weak gradients; −log D(G(z)) penalizes small D(G(z)) more strongly, typically producing larger, more useful gradients.

2) Regularize / constrain the discriminator so it remains a smooth teacher rather than an overconfident separator. Examples: spectral normalization on D, or a gradient penalty (e.g., WGAN-GP style), plus possibly data augmentation.

Reason: an overly sharp or overfit D can produce uninformative gradients for G (and can memorize training data). Regularization improves generalization and keeps gradients meaningful. Data augmentation reduces memorization and makes D learn more robust features.

Optionally, adjust the training balance (e.g., fewer D steps, lower D learning rate) so D does not outpace G.

## Connections

- •[Neural Networks](/tech-tree/neural-networks/)
- •[Backpropagation and Gradient Descent](/tech-tree/backprop/)
- •[Zero-Sum Games and Minimax](/tech-tree/zero-sum-games/)
- •[Divergences (KL, JSD)](/tech-tree/divergences/)
- •[Optimal Transport and Wasserstein Distance](/tech-tree/wasserstein/)
- •[Wasserstein GAN (WGAN)](/tech-tree/wgan/)
- •[Diffusion Models](/tech-tree/diffusion-models/)
- •[Domain Adaptation and Adversarial Learning](/tech-tree/adversarial-domain-adaptation/)

Quality: A (4.5/5)

[← back to tree](/tech-tree/)[browse all →](/tech-tree/inventory/)
