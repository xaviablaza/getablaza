---
title: Activation Functions
description: Nonlinear functions applied elementwise to neuron outputs (e.g., ReLU, sigmoid, tanh) that enable networks to model complex, non-linear relationships and affect training dynamics. Understanding their properties (saturation, gradient behavior, sparsity) is important for architecture design and optimization.
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
permalink: /tech-tree/activation-functions/
---

[←Back to Tech Tree](/tech-tree/)

[inventory](/tech-tree/inventory/)[coverage](/tech-tree/coverage/)

# Activation Functions

Machine LearningDifficulty: ★★★☆☆Depth: 0Unlocks: 5

Nonlinear functions applied elementwise to neuron outputs (e.g., ReLU, sigmoid, tanh) that enable networks to model complex, non-linear relationships and affect training dynamics. Understanding their properties (saturation, gradient behavior, sparsity) is important for architecture design and optimization.

## Interactive Visualization

⏮◀◀▶▶STEP0.25x1xZOOM

t=0s

## Core Concepts

- -Nonlinearity: activation functions introduce a non-linear transform so stacked layers can model non-linear functions (without them, multiple linear layers reduce to one).
- -Elementwise mapping: each neuron applies the activation to its pre-activation input (a = f(z)), i.e., activation is an elementwise function.
- -Local gradient behavior: the activation's derivative at z determines the local backpropagation signal; regions with near-zero derivative (saturation) or very large slope critically affect training dynamics.

## Key Symbols & Notation

f(z) - activation function mapping pre-activation z to output af'(z) - derivative of the activation (local gradient) used in backpropagation

## Essential Relationships

- -f'(z) directly controls gradient propagation during backpropagation: small f' (saturated regions) causes vanishing gradients and slows/blocks learning, while large/unbounded slopes can amplify/unstabilize gradients.

## Unlocks (2)

[Deep Learninglvl 5](/tech-tree/deep-learning/)[Numerical Stability and Conditioninglvl 4](/tech-tree/numerical-stability/)

Advanced Learning Details

### Graph Position

6

Depth Cost

5

Fan-Out (ROI)

2

Bottleneck Score

0

Chain Length

### Cognitive Load

6

Atomic Elements

35

Total Elements

L2

Percentile Level

L4

Atomic Level

### All Concepts (17)

- - Activation function: a nonlinear function applied to a neuron's pre-activation output to produce its activation
- - Elementwise application: the activation function is applied independently to each component of a vector/tensor of neuron outputs
- - Rectified Linear Unit (ReLU): activation defined by max(0, x) with zero output for negative inputs and linear for positive inputs
- - Sigmoid (logistic) activation: S-shaped function σ(x) = 1 / (1 + e^{-x}) mapping inputs to (0,1)
- - Hyperbolic tangent (tanh) activation: S-shaped function tanh(x) mapping inputs to (-1,1)
- - Nonlinearity enabling representational power: using non-linear activations lets layered networks approximate complex, non-linear functions
- - Saturation: regions of an activation where outputs approach a constant value and responses change very little with input
- - Gradient (local derivative) of an activation: the slope of the activation function that determines how errors backpropagate through that unit
- - Vanishing-gradient tendency: when an activation's derivative is very small in some regions, causing tiny gradients during backpropagation
- - Sparsity of activations: many neurons producing exactly zero (or near-zero) outputs for given inputs
- - Dead neuron phenomenon: a neuron that outputs zero for all inputs (commonly a ReLU that receives only negative pre-activations) and thus stops learning
- - Zero-centeredness of outputs: whether an activation's range is centered around zero (e.g., tanh) or not (e.g., sigmoid)
- - Bounded vs. unbounded outputs: whether an activation's output range is finite (sigmoid, tanh) or unbounded above/below (ReLU)
- - Differentiability / smoothness of the activation: whether the function is continuous and has continuous derivatives (affects gradient-based optimization)
- - Monotonicity of activation functions: whether the function is non-decreasing (many common activations are monotonic)
- - Effect on training dynamics: how an activation's properties influence optimization speed, stability, and convergence
- - Output range / scaling: the numeric interval and typical scale of activation outputs, which affect subsequent layer inputs and gradient magnitudes

### Teaching Strategy

Deep-dive lesson - accessible entry point but dense material. Use worked examples and spaced repetition.

A neural network without activation functions is secretly just one big linear model—no matter how many layers you stack. Activation functions are the small elementwise “twists” that make deep learning expressive, trainable, and (sometimes) numerically fragile.

TL;DR:

An activation function applies an elementwise nonlinearity a=f(z)a = f(z)a=f(z) to each neuron’s pre-activation z=w⊤x+bz = \mathbf{w}^\top \mathbf{x} + bz=w⊤x+b. This breaks linearity so deep networks can model complex functions, and its derivative f′(z)f'(z)f′(z) controls gradient flow in backprop. Key properties: saturation (tiny gradients), sparsity (many zeros for ReLU), and smoothness/scale (affects optimization and stability).

## What Is an Activation Function?

### Why we need them (motivation first)

A single neuron computes a weighted sum and bias, then optionally squashes it:

- •**Pre-activation**: z=w⊤x+bz = \mathbf{w}^\top \mathbf{x} + bz=w⊤x+b
- •**Activation output**: a=f(z)a = f(z)a=f(z)

The function f(⋅)f(\cdot)f(⋅) is the **activation function**. In standard feedforward layers, it is applied **elementwise** to each component of the vector **z** (one value per neuron).

The key reason activation functions matter is **nonlinearity**.

If you remove fff (or choose f(z)=zf(z) = zf(z)=z), then each layer is linear:

h=Wx+b\mathbf{h} = \mathbf{W}\mathbf{x} + \mathbf{b}h=Wx+b

Stack two such layers:

h1=W1x+b1\mathbf{h}\_1 = \mathbf{W}\_1\mathbf{x} + \mathbf{b}\_1h1​=W1​x+b1​

h2=W2h1+b2=W2(W1x+b1)+b2\mathbf{h}\_2 = \mathbf{W}\_2\mathbf{h}\_1 + \mathbf{b}\_2 = \mathbf{W}\_2(\mathbf{W}\_1\mathbf{x} + \mathbf{b}\_1) + \mathbf{b}\_2h2​=W2​h1​+b2​=W2​(W1​x+b1​)+b2​

Now expand:

h2=(W2W1)x+(W2b1+b2)\mathbf{h}\_2 = (\mathbf{W}\_2\mathbf{W}\_1)\mathbf{x} + (\mathbf{W}\_2\mathbf{b}\_1 + \mathbf{b}\_2)h2​=(W2​W1​)x+(W2​b1​+b2​)

That is **still just one linear layer** with new weights and bias:

- •W=W2W1\mathbf{W} = \mathbf{W}\_2\mathbf{W}\_1W=W2​W1​
- •b=W2b1+b2\mathbf{b} = \mathbf{W}\_2\mathbf{b}\_1 + \mathbf{b}\_2b=W2​b1​+b2​

So without nonlinear activations, adding depth does not add expressive power. Activations prevent this “collapse,” allowing networks to represent highly non-linear mappings.

### What “elementwise” really means

For a layer with mmm neurons, you typically compute:

z=Wx+b(z∈Rm)\mathbf{z} = \mathbf{W}\mathbf{x} + \mathbf{b} \quad (\mathbf{z} \in \mathbb{R}^m)z=Wx+b(z∈Rm)

Then apply activation elementwise:

a=f(z)    meaning    ai=f(zi)    ∀i\mathbf{a} = f(\mathbf{z}) \;\;\text{meaning}\;\; a\_i = f(z\_i)\;\;\forall ia=f(z)meaningai​=f(zi​)∀i

There’s no mixing between neurons inside fff; all the mixing is in Wx\mathbf{W}\mathbf{x}Wx.

### Local gradient behavior (why training cares)

Backprop uses the chain rule. For a scalar loss LLL, the gradient with respect to pre-activation zzz includes f′(z)f'(z)f′(z):

If a=f(z)a = f(z)a=f(z), then

∂L∂z=∂L∂a⋅f′(z)\frac{\partial L}{\partial z} = \frac{\partial L}{\partial a}\cdot f'(z)∂z∂L​=∂a∂L​⋅f′(z)

So the **local slope** f′(z)f'(z)f′(z) determines how strongly error signals flow backward.

Two immediate consequences:

1. 1)If f′(z)≈0f'(z) \approx 0f′(z)≈0 in some region (a **saturated** region), gradients vanish and learning slows.
2. 2)If f′(z)f'(z)f′(z) can be very large or unstable, gradients can explode or become numerically brittle.

### A visual “map” of common activations and their derivatives

Below is an inline static SVG overlaying common activation curves and (scaled) derivatives. The shapes make saturation and gradient flow tangible.

<svg width="780" height="310" viewBox="0 0 780 310" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Overlay of activation functions (sigmoid, tanh, ReLU) and their derivatives">

<rect x="0" y="0" width="780" height="310" fill="#ffffff" />

<!-- axes -->

<line x1="40" y1="155" x2="760" y2="155" stroke="#222" stroke-width="2"/>

<line x1="400" y1="20" x2="400" y2="290" stroke="#222" stroke-width="2"/>

<text x="745" y="148" font-size="12" fill="#222">z</text>

<text x="408" y="30" font-size="12" fill="#222">value</text>

<!-- grid ticks -->

<g stroke="#eee" stroke-width="1">

<line x1="40" y1="55" x2="760" y2="55"/>

<line x1="40" y1="255" x2="760" y2="255"/>

<line x1="220" y1="20" x2="220" y2="290"/>

<line x1="580" y1="20" x2="580" y2="290"/>

</g>

<g fill="#666" font-size="11">

<text x="208" y="170">-2</text>

<text x="568" y="170">+2</text>

<text x="392" y="170">0</text>

<text x="15" y="60">+1</text>

<text x="15" y="260">-1</text>

</g>

<!-- sigmoid (approx) -->

<path d="M40 230 C140 225, 220 210, 300 185 C340 170, 360 160, 400 155 C440 150, 460 140, 500 125 C580 100, 660 85, 760 80" fill="none" stroke="#1f77b4" stroke-width="3"/>

<!-- tanh (approx) -->

<path d="M40 255 C140 250, 220 225, 300 185 C340 165, 370 155, 400 155 C430 155, 460 145, 500 125 C580 85, 660 60, 760 55" fill="none" stroke="#ff7f0e" stroke-width="3"/>

<!-- ReLU -->

<path d="M40 155 L400 155 L760 55" fill="none" stroke="#2ca02c" stroke-width="3"/>

<!-- derivatives (scaled to fit): sigmoid' peak 0.25 -> scale x4 to show as 1 -->

<path d="M40 155 C170 155, 300 140, 400 105 C500 140, 630 155, 760 155" fill="none" stroke="#1f77b4" stroke-width="2" stroke-dasharray="6,4"/>

<!-- tanh' = 1 - tanh^2 peak 1 at 0 (already) -->

<path d="M40 155 C170 155, 300 135, 400 55 C500 135, 630 155, 760 155" fill="none" stroke="#ff7f0e" stroke-width="2" stroke-dasharray="6,4"/>

<!-- ReLU' piecewise: 0 for z<0, 1 for z>0 (draw as step) -->

<path d="M40 155 L400 155" fill="none" stroke="#2ca02c" stroke-width="2" stroke-dasharray="6,4"/>

<path d="M400 55 L760 55" fill="none" stroke="#2ca02c" stroke-width="2" stroke-dasharray="6,4"/>

<circle cx="400" cy="55" r="3" fill="#2ca02c"/>

<!-- legend -->

<g font-size="12" fill="#222">

<text x="50" y="25">Solid = activation f(z), dashed = derivative f'(z) (scaled where noted)</text>

<rect x="50" y="35" width="10" height="3" fill="#1f77b4"/><text x="65" y="42">sigmoid</text>

<rect x="140" y="35" width="10" height="3" fill="#ff7f0e"/><text x="155" y="42">tanh</text>

<rect x="210" y="35" width="10" height="3" fill="#2ca02c"/><text x="225" y="42">ReLU</text>

</g>

</svg>

**Reading the figure:**

- •Sigmoid and tanh saturate at large |z| (flat tails), and their derivatives collapse toward 0 there.
- •ReLU is not saturating on the positive side, and its derivative is constant 1 for z>0, but it is exactly 0 for z<0 (dead region).

This single picture captures most of what you’ll care about when choosing activations: where gradients flow, where they die, and what ranges outputs can take.

## Core Mechanic 1: Expressiveness from Nonlinearity (and why ReLU makes piecewise-linear models)

### From “just a line” to complex decision boundaries

A linear classifier in 2D has decision boundary w⊤x+b=0\mathbf{w}^\top \mathbf{x} + b = 0w⊤x+b=0, which is a line. If you compose linear layers only, you still get a line.

When you insert a nonlinearity, the network can “bend” space. Intuitively:

- •linear map: stretch/rotate/translate
- •nonlinearity: warp (but in a structured way)

### ReLU networks create piecewise-linear functions

ReLU is

ReLU⁡(z)=max⁡(0,z)\operatorname{ReLU}(z) = \max(0, z)ReLU(z)=max(0,z)

Consider a 1-hidden-layer network:

y(x)=∑j=1mvj ReLU⁡(wj⊤x+bj)+cy(\mathbf{x}) = \sum\_{j=1}^m v\_j\,\operatorname{ReLU}(\mathbf{w}\_j^\top \mathbf{x} + b\_j) + cy(x)=j=1∑m​vj​ReLU(wj⊤​x+bj​)+c

Each hidden unit splits input space by a hyperplane wj⊤x+bj=0\mathbf{w}\_j^\top \mathbf{x} + b\_j = 0wj⊤​x+bj​=0.

- •On one side, the unit outputs 0.
- •On the other, it outputs a linear function of **x**.

Because different subsets of ReLUs turn “on” in different regions, the whole network becomes **piecewise linear**: linear in each region, but with many regions.

### Visual: ReLU induces partitions in 2D

This SVG illustrates how two ReLU units create a partition of 2D space into regions where different linear pieces apply.

<svg width="780" height="320" viewBox="0 0 780 320" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="2D partition of the plane into regions by two ReLU hyperplanes">

<rect x="0" y="0" width="780" height="320" fill="#ffffff"/>

<text x="20" y="25" font-size="14" fill="#222">Two ReLU pre-activations define two lines (z₁=0 and z₂=0), partitioning the plane into 4 regions.</text>

<!-- coordinate frame -->

<line x1="80" y1="270" x2="360" y2="270" stroke="#222" stroke-width="2"/>

<line x1="220" y1="300" x2="220" y2="60" stroke="#222" stroke-width="2"/>

<text x="345" y="290" font-size="12" fill="#222">x₁</text>

<text x="230" y="70" font-size="12" fill="#222">x₂</text>

<!-- lines z1=0 and z2=0 -->

<line x1="110" y1="80" x2="330" y2="260" stroke="#1f77b4" stroke-width="3"/>

<line x1="110" y1="250" x2="330" y2="90" stroke="#ff7f0e" stroke-width="3"/>

<text x="115" y="75" font-size="12" fill="#1f77b4">z₁=0</text>

<text x="115" y="265" font-size="12" fill="#ff7f0e">z₂=0</text>

<!-- region labels -->

<g font-size="12" fill="#222">

<text x="120" y="140">Region A:</text>

<text x="120" y="158">z₁&lt;0, z₂&gt;0</text>

<text x="250" y="140">Region B:</text>

<text x="250" y="158">z₁&gt;0, z₂&gt;0</text>

<text x="120" y="215">Region C:</text>

<text x="120" y="233">z₁&lt;0, z₂&lt;0</text>

<text x="250" y="215">Region D:</text>

<text x="250" y="233">z₁&gt;0, z₂&lt;0</text>

</g>

<!-- explanation on the right -->

<rect x="410" y="60" width="350" height="220" fill="#fafafa" stroke="#ddd"/>

<text x="430" y="90" font-size="13" fill="#222">In each region, the network is linear:</text>

<text x="430" y="115" font-size="12" fill="#222">- If zⱼ&lt;0 ⇒ ReLU(zⱼ)=0 (unit off)</text>

<text x="430" y="138" font-size="12" fill="#222">- If zⱼ&gt;0 ⇒ ReLU(zⱼ)=zⱼ (unit on)</text>

<text x="430" y="170" font-size="12" fill="#222">So different regions activate different subsets</text>

<text x="430" y="190" font-size="12" fill="#222">of linear pieces, yielding a “bent” boundary</text>

<text x="430" y="210" font-size="12" fill="#222">when you solve y(x)=0.</text>

</svg>

This picture explains why ReLU networks are powerful: with many units, you get many regions, and therefore many linear pieces. Depth increases the number of regions dramatically.

### Smooth activations (sigmoid/tanh) give smooth warps

Sigmoid:

σ(z)=11+e−z\sigma(z) = \frac{1}{1+e^{-z}}σ(z)=1+e−z1​

Tanh:

tanh⁡(z)=ez−e−zez+e−z\tanh(z) = \frac{e^z - e^{-z}}{e^z + e^{-z}}tanh(z)=ez+e−zez−e−z​

These functions don’t create sharp “kinks” like ReLU; they create smooth transitions. That can be beneficial (smooth gradients) but can also cause saturation for large |z|.

### Output range and centering

A practical (often overlooked) design detail is the **range** and **mean** of activations:

| Activation | Range | Zero-centered? | Typical note |
| --- | --- | --- | --- |
| Sigmoid | (0, 1) | No | Good for probabilities; saturates |
| tanh | (-1, 1) | Yes | Often better than sigmoid in hidden layers |
| ReLU | [0, ∞) | No | Sparse activations; simple; risk of dead units |

Zero-centering matters because if activations are mostly positive, the next layer’s gradients can become biased (all weights pushed similarly), sometimes slowing optimization.

## Core Mechanic 2: Gradients, Saturation, and Training Dynamics

### The derivative is the “gate” for backprop

Let one neuron be:

- •z=w⊤x+bz = \mathbf{w}^\top \mathbf{x} + bz=w⊤x+b
- •a=f(z)a = f(z)a=f(z)

During backprop, the gradient that flows into zzz is:

δz≡∂L∂z=∂L∂a f′(z)=δa f′(z)\delta\_z \equiv \frac{\partial L}{\partial z} = \frac{\partial L}{\partial a}\, f'(z) = \delta\_a\, f'(z)δz​≡∂z∂L​=∂a∂L​f′(z)=δa​f′(z)

So f′(z)f'(z)f′(z) is literally a multiplier on the error signal.

If you stack many layers, you multiply many such terms (plus weight matrices). A simplified 1D intuition:

∂L∂z(1)≈∂L∂z(L)∏ℓ=1L−1f′(z(ℓ)) w(ℓ)\frac{\partial L}{\partial z^{(1)}} \approx \frac{\partial L}{\partial z^{(L)}} \prod\_{\ell=1}^{L-1} f'\big(z^{(\ell)}\big)\, w^{(\ell)}∂z(1)∂L​≈∂z(L)∂L​ℓ=1∏L−1​f′(z(ℓ))w(ℓ)

If the product shrinks toward 0, you get **vanishing gradients**. If it grows huge, **exploding gradients**.

### Saturation: when learning stalls

Sigmoid derivative:

First compute it cleanly:

σ(z)=11+e−z\sigma(z) = \frac{1}{1+e^{-z}}σ(z)=1+e−z1​

Differentiate:

σ′(z)=e−z(1+e−z)2\sigma'(z) = \frac{e^{-z}}{(1+e^{-z})^2}σ′(z)=(1+e−z)2e−z​

A more useful identity:

σ′(z)=σ(z)(1−σ(z))\sigma'(z) = \sigma(z)(1-\sigma(z))σ′(z)=σ(z)(1−σ(z))

This peaks at σ(z)=0.5\sigma(z)=0.5σ(z)=0.5 (i.e., z=0z=0z=0):

max⁡σ′(z)=0.25\max \sigma'(z) = 0.25maxσ′(z)=0.25

So even in the best case, each sigmoid layer multiplies gradients by at most 0.25 (before considering weights). In the saturated tails (large |z|), σ′(z)≈0\sigma'(z)\approx 0σ′(z)≈0.

Tanh derivative:

ddztanh⁡(z)=1−tanh⁡2(z)\frac{d}{dz}\tanh(z) = 1 - \tanh^2(z)dzd​tanh(z)=1−tanh2(z)

This peaks at 1 when z=0z=0z=0, but still goes to 0 as |z| grows.

**Interpretation:**

- •Sigmoid/tanh are smooth but can “turn off” gradients when zzz drifts into saturation.
- •This is why modern hidden layers rarely use sigmoid (except special cases like gates in LSTMs).

### ReLU: non-saturating (half the time)

ReLU derivative is:

ReLU⁡′(z)={0z<01z>0\operatorname{ReLU}'(z) = \begin{cases}
0 & z<0\\
1 & z>0
\end{cases}ReLU′(z)={01​z<0z>0​

(Undefined at 0, but implementations pick 0 or 1; it rarely matters in practice.)

So for active units (z>0), gradients pass through unchanged (multiplied by 1). That’s a big reason ReLU enabled very deep networks to train effectively.

But the zero-derivative region causes the **dying ReLU** problem: if a neuron’s inputs make z<0z<0z<0 for most data, it outputs 0 and gets no gradient to recover.

### Common variants and why they exist

Most activation variants are attempts to tune one or more properties:

- •keep gradients alive
- •keep outputs well-scaled
- •avoid numerical issues
- •preserve some sparsity

| Activation | Definition | Derivative behavior | Typical use |
| --- | --- | --- | --- |
| Leaky ReLU | max⁡(αz,z)\max(\alpha z, z)max(αz,z) | small slope α for z<0 | reduces dead ReLUs |
| ELU | zzz if z>0 else α(ez−1)\alpha(e^z-1)α(ez−1) | smooth negative side | sometimes improves convergence |
| GELU | z Φ(z)z\,\Phi(z)zΦ(z) (approx) | smooth, nonzero slope | Transformers/modern NLP |
| Softplus | log⁡(1+ez)\log(1+e^z)log(1+ez) | smooth ReLU; never 0 | when you need smoothness |

Leaky ReLU derivative:

f(z)={αzz<0zz≥0⇒f′(z)={αz<01z>0f(z)=\begin{cases}
\alpha z & z<0\\
z & z\ge 0
\end{cases}\quad\Rightarrow\quad f'(z)=\begin{cases}
\alpha & z<0\\
1 & z>0
\end{cases}f(z)={αzz​z<0z≥0​⇒f′(z)={α1​z<0z>0​

So even when “off,” some gradient passes.

### Sparsity: why zeros can be a feature

ReLU-like activations produce many exact zeros. That implies:

- •**sparse activations** → fewer active paths → sometimes easier optimization
- •implicit regularization: fewer co-adaptations
- •computational benefits in some systems

But sparsity is not free: too many zeros can reduce effective capacity and can stall learning for dead units.

### Numerical stability considerations

Activation functions interact with floating-point behavior.

- •**Sigmoid overflow/underflow**: e−ze^{-z}e−z can overflow for large negative z (since -z becomes large positive). Stable implementations branch:
- •if z ≥ 0 use σ(z)=1/(1+e−z)\sigma(z)=1/(1+e^{-z})σ(z)=1/(1+e−z)
- •else use σ(z)=ez/(1+ez)\sigma(z)=e^z/(1+e^z)σ(z)=ez/(1+ez)

- •**Softplus stability**: log⁡(1+ez)\log(1+e^z)log(1+ez) is stabilized via:

softplus⁡(z)=log⁡(1+ez)=max⁡(0,z)+log⁡(1+e−∣z∣)\operatorname{softplus}(z) = \log(1+e^z) = \max(0,z) + \log(1+e^{-|z|})softplus(z)=log(1+ez)=max(0,z)+log(1+e−∣z∣)

This avoids overflow when z is large.

- •**Saturation as “numerical” issue**: even if you avoid overflow, saturation still produces gradients near machine precision (effectively 0), which is an optimization issue.

These concerns connect directly to careful initialization and normalization methods you’ll meet later.

## Application/Connection: Choosing Activations in Real Networks

### A practical decision process

You rarely choose an activation in isolation. You choose it given:

- •task (classification vs regression)
- •depth
- •normalization (BatchNorm/LayerNorm)
- •expected input scale
- •whether you need probabilities or bounded outputs

A useful rule of thumb:

1. 1)**Hidden layers (general deep nets)**: ReLU / GELU are common defaults.
2. 2)**Output layers**: choose based on the output’s meaning.

### Output activations (match the target)

| Task | Output activation | Output meaning |
| --- | --- | --- |
| Binary classification | sigmoid | p(y=1∣x)p(y=1\mid \mathbf{x})p(y=1∣x) |
| Multi-class (single label) | softmax | categorical distribution |
| Regression (unbounded) | identity | any real value |
| Regression (positive) | softplus or exp | positive real |
| Regression (bounded) | tanh/sigmoid | constrained range |

Softmax is not elementwise (it mixes logits), but it’s commonly discussed alongside activations. Elementwise activations typically happen in hidden layers; softmax is a special output nonlinearity.

### Hidden layers: why ReLU/GELU are popular

**ReLU**:

- •simple and fast
- •non-saturating on positive side
- •encourages sparsity

**GELU** (common in Transformers):

- •smooth version of “keep positive, damp negative”
- •can yield slightly better optimization in some settings

### When sigmoid/tanh are still useful

Even though sigmoid/tanh can saturate, they remain important:

- •**Sigmoid** is ideal for probabilities and gating.
- •**tanh** is useful when you want bounded, zero-centered hidden state (classic RNNs).

### A note on initialization and activation pairing

Activations influence how variance propagates forward/backward. While you’ll study initialization formally later, the intuition is:

- •If fff squashes too hard (sigmoid), signals and gradients shrink.
- •If fff passes with slope ~1 for many inputs (ReLU on positive side), signals survive better.

This is why “He initialization” is often paired with ReLU-like activations, and “Xavier/Glorot” is often paired with tanh.

### Summary: what properties you’re trading off

| Property | Helps with | Often hurts |
| --- | --- | --- |
| Bounded outputs (sigmoid/tanh) | stability, interpretability | saturation → vanishing gradients |
| Unbounded positive (ReLU) | gradient flow, simplicity | dead units, nonzero mean |
| Smoothness (tanh, softplus, GELU) | stable optimization, differentiability | can reduce sparsity; may saturate |
| Sparsity (ReLU) | regularization-like effect | too many inactive units |

Activation functions are not just “a nonlinearity.” They are a design lever that shapes geometry (expressiveness) and learning (gradient flow).

## Worked Examples (3)

### Show that stacking linear layers without activations collapses to one linear layer

Consider a 2-layer network with no activation functions:

\nLayer 1: h=W1x+b1\mathbf{h} = \mathbf{W}\_1\mathbf{x} + \mathbf{b}\_1h=W1​x+b1​

\nLayer 2: y=W2h+b2\mathbf{y} = \mathbf{W}\_2\mathbf{h} + \mathbf{b}\_2y=W2​h+b2​.

\nShow that y\mathbf{y}y is an affine function of x\mathbf{x}x and write the equivalent single-layer parameters.

1. Substitute Layer 1 into Layer 2:

   \ny=W2(W1x+b1)+b2\mathbf{y} = \mathbf{W}\_2(\mathbf{W}\_1\mathbf{x} + \mathbf{b}\_1) + \mathbf{b}\_2y=W2​(W1​x+b1​)+b2​
2. Distribute W2\mathbf{W}\_2W2​:

   \ny=W2W1x+W2b1+b2\mathbf{y} = \mathbf{W}\_2\mathbf{W}\_1\mathbf{x} + \mathbf{W}\_2\mathbf{b}\_1 + \mathbf{b}\_2y=W2​W1​x+W2​b1​+b2​
3. Group terms as a single affine map y=Wx+b\mathbf{y} = \mathbf{W}\mathbf{x} + \mathbf{b}y=Wx+b:

   \nW=W2W1\mathbf{W} = \mathbf{W}\_2\mathbf{W}\_1W=W2​W1​,

   \nb=W2b1+b2\mathbf{b} = \mathbf{W}\_2\mathbf{b}\_1 + \mathbf{b}\_2b=W2​b1​+b2​
4. Conclude: any number of stacked linear layers (no nonlinear activation between them) equals one linear layer, so depth adds no representational power in that case.

**Insight:** This is the core “why before how” for activations: fff prevents this collapse, allowing each layer to change the function class rather than merely re-parameterize a linear map.

### Compute backprop through a single activation and see saturation numerically (sigmoid vs ReLU)

Let a scalar neuron be z=wx+bz = wx + bz=wx+b, a=f(z)a=f(z)a=f(z), and loss L=12(a−y)2L = \tfrac{1}{2}(a - y)^2L=21​(a−y)2.

\nPick x=1x=1x=1, w=1w=1w=1, b=0b=0b=0, y=1y=1y=1.

\nCompare gradients ∂L/∂w\partial L/\partial w∂L/∂w for:

1) sigmoid f(z)=σ(z)f(z)=\sigma(z)f(z)=σ(z) at z=0z=0z=0 and at z=−10z=-10z=−10

2) ReLU f(z)=max⁡(0,z)f(z)=\max(0,z)f(z)=max(0,z) at the same z values.

1. Compute generic derivatives.

   \nSince L=12(a−y)2L=\tfrac{1}{2}(a-y)^2L=21​(a−y)2, we have:

   \n∂L∂a=a−y\frac{\partial L}{\partial a} = a - y∂a∂L​=a−y.

   \nAnd by chain rule:

   \n∂L∂w=∂L∂a⋅∂a∂z⋅∂z∂w=(a−y) f′(z) x\frac{\partial L}{\partial w} = \frac{\partial L}{\partial a}\cdot \frac{\partial a}{\partial z}\cdot \frac{\partial z}{\partial w} = (a-y)\,f'(z)\,x∂w∂L​=∂a∂L​⋅∂z∂a​⋅∂w∂z​=(a−y)f′(z)x.

   \nWith x=1x=1x=1: ∂L/∂w=(a−y)f′(z)\partial L/\partial w = (a-y)f'(z)∂L/∂w=(a−y)f′(z).
2. Case A (sigmoid) at z=0.

   \na=σ(0)=0.5a=\sigma(0)=0.5a=σ(0)=0.5.

   \nf′(0)=σ(0)(1−σ(0))=0.5⋅0.5=0.25f'(0)=\sigma(0)(1-\sigma(0))=0.5\cdot 0.5=0.25f′(0)=σ(0)(1−σ(0))=0.5⋅0.5=0.25.

   \nSo ∂L/∂w=(0.5−1)⋅0.25=(−0.5)⋅0.25=−0.125\partial L/\partial w = (0.5-1)\cdot 0.25 = (-0.5)\cdot 0.25 = -0.125∂L/∂w=(0.5−1)⋅0.25=(−0.5)⋅0.25=−0.125.
3. Case B (sigmoid) at z=-10.

   \na=σ(−10)≈0.0000454a=\sigma(-10)\approx 0.0000454a=σ(−10)≈0.0000454.

   \nf′(−10)=a(1−a)≈0.0000454⋅(0.9999546)≈0.0000454f'(-10)=a(1-a)\approx 0.0000454\cdot (0.9999546)\approx 0.0000454f′(−10)=a(1−a)≈0.0000454⋅(0.9999546)≈0.0000454.

   \nSo ∂L/∂w≈(0.0000454−1)⋅0.0000454≈(−0.9999546)⋅0.0000454≈−0.0000454\partial L/\partial w \approx (0.0000454-1)\cdot 0.0000454 \approx (-0.9999546)\cdot 0.0000454 \approx -0.0000454∂L/∂w≈(0.0000454−1)⋅0.0000454≈(−0.9999546)⋅0.0000454≈−0.0000454.

   \nThe gradient magnitude shrank from 1e-1 to about 1e-5 due to saturation.
4. Case C (ReLU) at z=0.

   \na=max⁡(0,0)=0a=\max(0,0)=0a=max(0,0)=0.

   \nAt exactly 0, ReLU derivative is undefined; implementations pick 0 or 1. Consider a tiny positive z (e.g., z=+ε) to represent “active” behavior: then f′(z)=1f'(z)=1f′(z)=1.

   \nIf z≈0⁺: a≈0a≈0a≈0, so ∂L/∂w=(0−1)⋅1=−1\partial L/\partial w = (0-1)\cdot 1 = -1∂L/∂w=(0−1)⋅1=−1.
5. Case D (ReLU) at z=-10.

   \na=0a=0a=0 and f′(z)=0f'(z)=0f′(z)=0 (inactive).

   \nSo ∂L/∂w=(0−1)⋅0=0\partial L/\partial w = (0-1)\cdot 0 = 0∂L/∂w=(0−1)⋅0=0.

   \nNo gradient flows: this is the dying-ReLU risk if many datapoints keep z<0.

**Insight:** Sigmoid gives you *some* gradient when saturated, but it can be extremely small; ReLU gives you strong gradients when active, but exactly zero when inactive. Training dynamics are dominated by these local derivative regimes.

### Piecewise linearity in 1D: a tiny ReLU network becomes a ‘hinge sum’

Let x∈Rx \in \mathbb{R}x∈R and define a 2-unit ReLU network:

\ny(x)=v1 ReLU⁡(x−1)+v2 ReLU⁡(x+1)+cy(x) = v\_1\,\operatorname{ReLU}(x - 1) + v\_2\,\operatorname{ReLU}(x + 1) + cy(x)=v1​ReLU(x−1)+v2​ReLU(x+1)+c.

\nShow explicitly that y(x)y(x)y(x) is linear on each interval cut by the hinge points x=−1x=-1x=−1 and x=1x=1x=1.

1. Identify hinge points where each ReLU switches.

   \nReLU⁡(x−1)\operatorname{ReLU}(x-1)ReLU(x−1) switches at x=1x=1x=1.

   \nReLU⁡(x+1)\operatorname{ReLU}(x+1)ReLU(x+1) switches at x=−1x=-1x=−1.

   \nSo consider intervals: (−∞,−1)(-\infty,-1)(−∞,−1), [−1,1)[-1,1)[−1,1), [1,∞)[1,\infty)[1,∞).
2. Interval 1: x<−1x<-1x<−1.

   \nThen x−1<0x-1<0x−1<0 and x+1<0x+1<0x+1<0.

   \nSo both ReLUs are 0:

   \ny(x)=cy(x)=cy(x)=c (constant, hence linear).
3. Interval 2: −1≤x<1-1 \le x < 1−1≤x<1.

   \nThen x−1<0x-1<0x−1<0 but x+1≥0x+1\ge 0x+1≥0.

   \nSo:

   \nReLU⁡(x−1)=0\operatorname{ReLU}(x-1)=0ReLU(x−1)=0,

   \nReLU⁡(x+1)=x+1\operatorname{ReLU}(x+1)=x+1ReLU(x+1)=x+1.

   \nThus y(x)=v2(x+1)+c=v2x+(v2+c)y(x)=v\_2(x+1)+c = v\_2 x + (v\_2+c)y(x)=v2​(x+1)+c=v2​x+(v2​+c) (linear).
4. Interval 3: x≥1x\ge 1x≥1.

   \nThen both x−1≥0x-1\ge 0x−1≥0 and x+1≥0x+1\ge 0x+1≥0.

   \nSo:

   \ny(x)=v1(x−1)+v2(x+1)+c=(v1+v2)x+(−v1+v2+c)y(x)=v\_1(x-1)+v\_2(x+1)+c = (v\_1+v\_2)x + (-v\_1+v\_2+c)y(x)=v1​(x−1)+v2​(x+1)+c=(v1​+v2​)x+(−v1​+v2​+c) (linear).
5. Conclude: the network is piecewise linear with ‘kinks’ at x=-1 and x=1; adding more ReLU units adds more hinge points, increasing shape flexibility.

**Insight:** This is the 1D version of the 2D partition picture: ReLUs introduce regions where different linear formulas apply, letting you build complex shapes by stitching simple pieces.

## Key Takeaways

- ✓

  Activation functions apply an elementwise mapping a=f(z)a=f(z)a=f(z) to each neuron’s pre-activation zzz.
- ✓

  Without nonlinear activations, stacked linear layers collapse into a single linear (affine) transformation—depth gives no extra expressiveness.
- ✓

  The derivative f′(z)f'(z)f′(z) directly gates backpropagation: ∂L/∂z=(∂L/∂a) f′(z)\partial L/\partial z = (\partial L/\partial a)\,f'(z)∂L/∂z=(∂L/∂a)f′(z).
- ✓

  Sigmoid and tanh saturate for large |z|, causing vanishing gradients in their tails; sigmoid’s maximum slope is only 0.25.
- ✓

  ReLU is non-saturating for z>0 (good gradient flow) but has zero gradient for z<0 (risk of dead neurons).
- ✓

  ReLU networks represent piecewise-linear functions; in higher dimensions, ReLU hyperplanes partition space into regions with different linear behaviors.
- ✓

  Activation choice affects output range, zero-centering, sparsity, and numerical stability—so it influences both modeling and optimization.

## Common Mistakes

- ✗

  Using sigmoid (or tanh) in many deep hidden layers without understanding saturation, then wondering why gradients vanish and training stalls.
- ✗

  Assuming activations are “just a detail,” ignoring their derivatives—when f′(z)f'(z)f′(z) is the main determinant of gradient flow locally.
- ✗

  Forgetting that ReLU can die: if pre-activations stay negative, the unit outputs 0 and receives zero gradient (especially with large learning rates or biased initialization).
- ✗

  Mismatching output activation to the task (e.g., using ReLU for probabilities, or sigmoid for unbounded regression).

## Practice

easy

Compute derivatives: (a) σ′(z)\sigma'(z)σ′(z) for sigmoid σ(z)=1/(1+e−z)\sigma(z)=1/(1+e^{-z})σ(z)=1/(1+e−z), and (b) tanh⁡′(z)\tanh'(z)tanh′(z). Then evaluate each derivative at z=0 and describe what it implies for gradient flow near the origin.

**Hint:** For sigmoid, try rewriting in terms of σ(z)\sigma(z)σ(z) after differentiating. For tanh, use tanh⁡(z)=ez−e−zez+e−z\tanh(z)=\frac{e^z-e^{-z}}{e^z+e^{-z}}tanh(z)=ez+e−zez−e−z​ or the identity $1-\tanh^2(z)$.

Show solution

Sigmoid:

σ(z)=11+e−z\sigma(z)=\frac{1}{1+e^{-z}}σ(z)=1+e−z1​

Differentiate:

σ′(z)=e−z(1+e−z)2\sigma'(z)=\frac{e^{-z}}{(1+e^{-z})^2}σ′(z)=(1+e−z)2e−z​

And using σ(z)=1/(1+e−z)\sigma(z)=1/(1+e^{-z})σ(z)=1/(1+e−z) gives:

σ′(z)=σ(z)(1−σ(z)).\sigma'(z)=\sigma(z)(1-\sigma(z)).σ′(z)=σ(z)(1−σ(z)).

At z=0: σ(0)=0.5\sigma(0)=0.5σ(0)=0.5 so σ′(0)=0.25\sigma'(0)=0.25σ′(0)=0.25.

Tanh:

tanh⁡′(z)=1−tanh⁡2(z).\tanh'(z)=1-\tanh^2(z).tanh′(z)=1−tanh2(z).

At z=0: tanh⁡(0)=0\tanh(0)=0tanh(0)=0 so tanh⁡′(0)=1\tanh'(0)=1tanh′(0)=1.

Implication: near z=0, tanh passes gradient more strongly than sigmoid; sigmoid’s slope is capped at 0.25 even in its best region.

medium

Consider a 2-layer network with ReLU between layers: h=ReLU⁡(W1x+b1)\mathbf{h}=\operatorname{ReLU}(\mathbf{W}\_1\mathbf{x}+\mathbf{b}\_1)h=ReLU(W1​x+b1​) and y=w2⊤h+b2y=\mathbf{w}\_2^\top\mathbf{h}+b\_2y=w2⊤​h+b2​. Explain (in words) why this network can represent non-linear decision boundaries in x-space, unlike the same architecture without ReLU.

**Hint:** Focus on what happens in regions where each component of W1x+b1\mathbf{W}\_1\mathbf{x}+\mathbf{b}\_1W1​x+b1​ is positive vs negative.

Show solution

With ReLU, each hidden unit outputs either 0 (if its pre-activation is negative) or a linear function of x (if positive). The set of signs of the hidden pre-activations partitions input space into regions; within each region, the network behaves like a linear model, but different regions have different linear formulas because different subsets of hidden units are active. The boundary y=0 can therefore bend across regions, forming a non-linear decision boundary. Without ReLU, the whole network is just one affine map in x, so y=0 is a single hyperplane (linear boundary).

hard

Dying ReLU thought experiment: Suppose a neuron uses ReLU and its pre-activation is z=wx+bz = wx + bz=wx+b. If your dataset has x mostly around 0 and you initialize b = -5 with small w, what happens to this neuron during early training? Propose one fix.

**Hint:** Evaluate the sign of z initially and connect it to ReLU⁡′(z)\operatorname{ReLU}'(z)ReLU′(z).

Show solution

If x≈0 and w is small, then initially z≈b=-5, so z<0 for most examples. The neuron outputs a=ReLU(z)=0 and its derivative is ReLU'(z)=0 in that region. In backprop, ∂L/∂z\partial L/\partial z∂L/∂z gets multiplied by 0, so ∂L/∂w\partial L/\partial w∂L/∂w and ∂L/∂b\partial L/\partial b∂L/∂b for that neuron are ~0; it may not recover and becomes a dead unit. Fixes include: (1) initialize biases closer to 0 (or slightly positive) so some examples activate the unit, (2) use Leaky ReLU so the negative side has slope α>0 and gradients can update w and b, or (3) use normalization (e.g., BatchNorm) to keep z distribution near 0.

## Connections

Next nodes you can explore:

- •[Deep Learning](/tech-tree/deep-learning/) — activations become even more crucial as depth increases (gradient flow, expressiveness, architectural defaults like ReLU/GELU).
- •[Numerical Stability and Conditioning](/tech-tree/numerical-stability/) — stable implementations of sigmoid/softplus, saturation as an optimization/stability issue, and why scaling/normalization matter.

Quality: A (4.4/5)

[← back to tree](/tech-tree/)[browse all →](/tech-tree/inventory/)
