---
title: Deep Learning
description: Neural networks with many layers. CNNs, RNNs, architectures.
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
permalink: /tech-tree/deep-learning/
---

[←Back to Tech Tree](/tech-tree/)

[inventory](/tech-tree/inventory/)[coverage](/tech-tree/coverage/)

# Deep Learning

Machine LearningDifficulty: ★★★★★Depth: 12Unlocks: 3

Neural networks with many layers. CNNs, RNNs, architectures.

## Interactive Visualization

⏮◀◀▶▶STEP0.25x1xZOOM

t=0s

## Core Concepts

- -Layered function composition: a model is a nested composition of parameterized transformations (layers)
- -Distributed hierarchical representations: each layer computes feature representations that combine lower-level features into higher-level abstractions
- -Architectural inductive biases: structural constraints (e.g., locality, weight sharing, recurrence, attention) that restrict the function family and encode useful invariances

## Key Symbols & Notation

f\_theta(x) = f\_L(... f\_2(f\_1(x))) (composed network function)h^l (activation / representation vector at layer l)

## Essential Relationships

- -The composed function f\_theta produces the layerwise representations h^l (hierarchical, distributed features), and architectural inductive biases determine which compositions are parameter-efficient and generalize from data

## Prerequisites (9)

[Backpropagation5 atoms](/tech-tree/backpropagation/)[Stochastic Gradient Descent5 atoms](/tech-tree/sgd/)[Regularization9 atoms](/tech-tree/regularization/)[Activation Functions6 atoms](/tech-tree/activation-functions/)[Computational Graphs6 atoms](/tech-tree/computational-graphs/)[Automatic Differentiation5 atoms](/tech-tree/automatic-differentiation/)[Curse of Dimensionality6 atoms](/tech-tree/curse-of-dimensionality/)[Convolution Operation6 atoms](/tech-tree/convolution-operation/)[Numerical Stability and Conditioning4 atoms](/tech-tree/numerical-stability/)

## Unlocks (2)

[Attention Mechanismslvl 5](/tech-tree/attention-mechanisms/)[Meta-Learninglvl 5](/tech-tree/meta-learning/)

Advanced Learning Details

### Graph Position

209

Depth Cost

3

Fan-Out (ROI)

2

Bottleneck Score

12

Chain Length

### Cognitive Load

6

Atomic Elements

53

Total Elements

L4

Percentile Level

L4

Atomic Level

### All Concepts (20)

- - Depth and hierarchical feature learning (many stacked layers produce progressively higher-level representations)
- - Convolutional network architecture elements beyond the convolution operation (pooling, strided convolution for downsampling, transposed/upsampling convolution)
- - Architectural efficiency tricks for CNNs (depthwise-separable convolutions, bottleneck layers)
- - Dilated (atrous) convolution (increase receptive field without increasing parameter count)
- - Effective receptive field vs. theoretical receptive field (actual influence of input pixels on deeper activations)
- - Residual and skip connections (identity/shortcut paths between non-adjacent layers)
- - Normalization layers specific to deep architectures (BatchNorm, LayerNorm, GroupNorm) and their use
- - Recurrent neural networks (RNNs) as sequence models: recurrence, hidden state, timestep indexing
- - Backpropagation Through Time (BPTT) - applying backpropagation to unfolded recurrent computations
- - Gated recurrent units and memory cells (LSTM and GRU): gate vectors and cell state to control information flow
- - Gradient issues specific to deep and recurrent architectures (vanishing and exploding gradients in very deep nets / long sequences) and practical fixes
- - Gradient clipping (rescaling or truncating gradients to stabilize training)
- - Attention mechanisms (query/key/value formulation) and self-attention
- - Transformer-style architectures: replacing recurrence with multi-head self-attention plus positional encodings
- - Softmax output layer and cross-entropy loss (converting logits to a probability distribution and measuring mismatch)
- - Advanced optimization algorithms commonly used in deep learning (Adam, RMSProp, AdamW and their per-parameter adaptive learning rates / moment estimates)
- - Initialization schemes tuned for deep nets (Xavier/Glorot, He/Kaiming) to control variance propagation
- - Training at scale: pretraining, transfer learning, fine-tuning, and checkpointing
- - Design trade-offs in architecture depth vs width, and compute/parameter-efficiency strategies
- - Regularization and augmentation strategies commonly used with deep architectures (data augmentation, early stopping, label smoothing - beyond L1/L2 and dropout)

### Teaching Strategy

Multi-session curriculum - substantial prior knowledge and complex material. Use mastery gates and deliberate practice.

Deep learning is the art of building a *useful family of functions* by stacking simple transformations into a long composition—and then making that composition trainable and stable at scale.

TL;DR:

A deep network is a composed function fθ(x)=fL(⋯f2(f1(x)))f\_\theta(x)=f\_L(\cdots f\_2(f\_1(x)))fθ​(x)=fL​(⋯f2​(f1​(x))). Depth creates *hierarchical representations* (each layer builds features from earlier features). Architecture is about *inductive bias*: choosing structure (convolutions, recurrence, attention, normalization, residual paths) that makes learning feasible and generalization likely. Training success depends as much on conditioning (initialization, normalization, residuals) as on optimization (SGD variants).

## What Is Deep Learning? (And a Minimal Working Mental Model)

### Why before how

Deep learning is not “just bigger neural nets.” It’s a strategy for **representing complicated functions** using many simple, reusable parts (layers), and for **learning representations** that make downstream prediction easy.

The core object is a **composed function**:

fθ(x)=fL(fL−1(⋯f2(f1(x))))f\_\theta(x)=f\_L\big( f\_{L-1}(\cdots f\_2(f\_1(x)) )\big)fθ​(x)=fL​(fL−1​(⋯f2​(f1​(x))))

At each layer ℓ\ellℓ, we maintain an activation / representation vector hℓ\mathbf{h}^{\ell}hℓ (often written hℓh^\ellhℓ when shape is clear):

- •h0=x\mathbf{h}^{0} = \mathbf{x}h0=x (the input)
- •hℓ=fℓ(hℓ−1;θℓ)\mathbf{h}^{\ell} = f\_{\ell}(\mathbf{h}^{\ell-1};\theta\_{\ell})hℓ=fℓ​(hℓ−1;θℓ​)
- •output y^=hL\hat{\mathbf{y}} = \mathbf{h}^{L}y^​=hL

A very common concrete layer is **affine + nonlinearity**:

zℓ=Wℓhℓ−1+bℓ,hℓ=ϕ(zℓ)\mathbf{z}^{\ell} = \mathbf{W}^{\ell}\mathbf{h}^{\ell-1} + \mathbf{b}^{\ell}, \qquad \mathbf{h}^{\ell} = \phi(\mathbf{z}^{\ell})zℓ=Wℓhℓ−1+bℓ,hℓ=ϕ(zℓ)

Depth matters because it changes *what is easy to represent* and *what is easy to learn*.

### Minimal working mental model: a 2-layer network on a simple task

You already know backprop and SGD; let’s anchor deep learning in one concrete “small but real” example.

**Task:** binary classification in 2D. Input x∈R2\mathbf{x} \in \mathbb{R}^2x∈R2, label y∈{0,1}y\in\{0,1\}y∈{0,1}. Suppose the decision boundary is not linearly separable (e.g., two moons).

A **2-layer MLP** (one hidden layer) is:

h1=ReLU(W1x+b1)\mathbf{h}^1 = \mathrm{ReLU}(\mathbf{W}^1\mathbf{x}+\mathbf{b}^1)h1=ReLU(W1x+b1)

y^=σ(w2⋅h1+b2)\hat{y} = \sigma(\mathbf{w}^2 \cdot \mathbf{h}^1 + b^2)y^​=σ(w2⋅h1+b2)

Interpretation:

- •Layer 1 creates a set of learned “features” (half-spaces gated by ReLU).
- •Layer 2 mixes those features into a probability via logistic regression.

Even here, you can see the deep learning pattern:

1) **Representation**: h1\mathbf{h}^1h1 is not hand-designed—it’s learned.

2) **Composition**: the model builds a nonlinear function from simple parts.

3) **Trainability**: success depends on gradients flowing from y^\hat{y}y^​ back to W1\mathbf{W}^1W1.

Now scale that idea: more layers, richer inductive biases (convolution, attention), and careful conditioning (normalization/residuals) to make training stable.

### Checkpoint: what “deep” adds

Before going further, keep these three questions in mind:

1) **What family of functions** does this architecture represent?

2) **What representations** will intermediate layers tend to discover?

3) **Will gradients and signals** propagate stably through depth?

Deep learning is largely the practice of answering those three questions well.

## Core Mechanic 1: Layered Function Composition → Representations

### Why depth is not just “more parameters”

You could increase width (more units per layer) or increase depth (more layers). Both add parameters, but they add *different* representational structure.

A useful mental model:

- •**Width** adds “parallel feature templates.”
- •**Depth** adds “feature reuse and hierarchy.”

Depth encourages **distributed hierarchical representations**:

- •Early layers: local/simple patterns.
- •Middle layers: combinations of patterns.
- •Late layers: task-level abstractions.

In images, this often looks like edges → textures → parts → objects. In language, characters/subwords → local syntax → semantics.

### The forward pass as representation building

Write the network as repeated transformations:

hℓ=fℓ(hℓ−1)\mathbf{h}^{\ell} = f\_{\ell}(\mathbf{h}^{\ell-1})hℓ=fℓ​(hℓ−1)

Think of hℓ\mathbf{h}^{\ell}hℓ as a *coordinate system* the network invents. Learning aims to make the final layer’s problem “simple” (often linearly separable).

A very common pattern is:

fℓ(h)=ϕ(Norm(Wh+b))f\_{\ell}(\mathbf{h}) = \phi\big(\mathrm{Norm}(\mathbf{W}\mathbf{h}+\mathbf{b})\big)fℓ​(h)=ϕ(Norm(Wh+b))

where Norm might be BatchNorm, LayerNorm, RMSNorm, etc.

### A little math: how composition shapes sensitivity

Deep nets are compositions, so their derivatives are products (chains) of Jacobians.

Let hℓ∈Rdℓ\mathbf{h}^{\ell} \in \mathbb{R}^{d\_\ell}hℓ∈Rdℓ​. Define the Jacobian

Jℓ=∂hℓ∂hℓ−1∈Rdℓ×dℓ−1\mathbf{J}^{\ell} = \frac{\partial \mathbf{h}^{\ell}}{\partial \mathbf{h}^{\ell-1}} \in \mathbb{R}^{d\_\ell \times d\_{\ell-1}}Jℓ=∂hℓ−1∂hℓ​∈Rdℓ​×dℓ−1​

Then:

∂hL∂x=JL JL−1⋯J1\frac{\partial \mathbf{h}^{L}}{\partial \mathbf{x}} = \mathbf{J}^{L}\,\mathbf{J}^{L-1}\cdots \mathbf{J}^{1}∂x∂hL​=JLJL−1⋯J1

This single equation explains a lot:

- •If typical singular values of Jℓ\mathbf{J}^\ellJℓ are > 1, gradients can **explode**.
- •If they are < 1, gradients can **vanish**.
- •If they cluster near 1, training tends to be stable.

You don’t need to compute these Jacobians explicitly to benefit from this mental model; it motivates **initialization**, **normalization**, and **residual connections**.

### Checkpoint: what you should carry forward

- •Representations hℓ\mathbf{h}^\ellhℓ are the real “product” of deep learning.
- •The chain-of-Jacobians view predicts optimization pathologies.
- •Architecture is about shaping both representations and Jacobians.

## Core Mechanic 2: Architectural Inductive Biases (CNNs, RNNs, Attention, MLPs)

### Why inductive bias is the point of architecture

Without assumptions, learning in high dimensions is sample-inefficient (curse of dimensionality). Architectural choices encode assumptions like:

- •locality
- •translation equivariance
- •temporal recurrence
- •permutation invariance/equivariance
- •long-range interactions

These biases restrict the function class to something that matches the world.

### A comparison table of major deep learning architectures

| Architecture | Core operation | Inductive bias | Strengths | Common failure mode |
| --- | --- | --- | --- | --- |
| MLP (feedforward) | dense affine + nonlinearity | weak (mostly none) | flexible; works on tabular/embeddings | data-hungry; ignores structure |
| CNN | convolution (weight sharing, locality) | translation equivariance; local patterns | vision, audio; parameter efficient | struggles with global context unless deep/augmented |
| RNN / LSTM / GRU | recurrence ht=f(ht−1,xt)\mathbf{h}\_t=f(\mathbf{h}\_{t-1},\mathbf{x}\_t)ht​=f(ht−1​,xt​) | sequential state; temporal locality | streaming, variable-length sequences | long-range dependencies; parallelization limits |
| Attention / Transformer | content-based mixing (self-attn) | flexible pairwise interactions; permutation equivariance with positional encoding | long-range dependencies; parallelizable | quadratic cost in sequence length; needs lots of data |
| GNN | message passing on graphs | graph equivariance/invariance | molecules, networks, relational data | oversmoothing; limited expressivity for some tasks |

We’ll focus on CNNs and sequence models (RNNs/attention), since they are canonical deep learning building blocks.

---

## CNNs: locality + weight sharing

A 2D convolution layer applies a kernel over local neighborhoods. If you already know the convolution operation, the key deep-learning additions are:

1) **Channels**: kernels map CinC\_{in}Cin​ input channels to CoutC\_{out}Cout​ output channels.

2) **Stacking**: repeated convs grow the **receptive field**.

A simplified expression (single output channel) is:

y[i,j]=∑u,vk[u,v]  x[i+u,j+v]y[i,j] = \sum\_{u,v} k[u,v] \; x[i+u, j+v]y[i,j]=u,v∑​k[u,v]x[i+u,j+v]

With multiple channels:

yc[i,j]=∑c′∑u,vkc,c′[u,v]  xc′[i+u,j+v]y\_c[i,j] = \sum\_{c'}\sum\_{u,v} k\_{c,c'}[u,v] \; x\_{c'}[i+u, j+v]yc​[i,j]=c′∑​u,v∑​kc,c′​[u,v]xc′​[i+u,j+v]

**Why it helps:** weight sharing means you learn “edge detector” once and reuse it across the image. Locality reduces parameters and encourages features to be local.

Common CNN design motifs:

- •small kernels (3×3) stacked
- •pooling or strided conv for downsampling
- •residual blocks (ResNet)

---

## RNNs: recurrence for sequences

An RNN maintains a state ht\mathbf{h}\_tht​ updated over time:

ht=ϕ(Whht−1+Wxxt+b)\mathbf{h}\_t = \phi(\mathbf{W}\_h\mathbf{h}\_{t-1} + \mathbf{W}\_x\mathbf{x}\_t + \mathbf{b})ht​=ϕ(Wh​ht−1​+Wx​xt​+b)

This encodes an inductive bias: “the present depends on a compressed summary of the past.”

**Training issue:** backprop through time multiplies many Jacobians across timesteps, causing vanishing/exploding gradients. LSTMs/GRUs mitigate this with gating, roughly creating more stable paths for gradient flow.

---

## Attention/Transformers: content-based routing

Self-attention computes a weighted average of value vectors using query-key similarity.

Given matrices Q,K,V\mathbf{Q},\mathbf{K},\mathbf{V}Q,K,V:

Attn(Q,K,V)=softmax(QK⊤d)V\mathrm{Attn}(\mathbf{Q},\mathbf{K},\mathbf{V}) = \mathrm{softmax}\Big(\frac{\mathbf{Q}\mathbf{K}^\top}{\sqrt{d}}\Big)\mathbf{V}Attn(Q,K,V)=softmax(d​QK⊤​)V

The inductive bias shifts from locality/recurrent state to **learned interactions** between all positions.

Transformers add:

- •positional information (positional encodings)
- •residual connections
- •normalization
- •MLP blocks

---

### Checkpoint: choosing an architecture

A practical decision rule:

- •If your data has **grid locality** (images, spectrograms): start with CNNs.
- •If your data is **sequential** and you need streaming/low latency: consider RNNs.
- •If you need **long-range dependencies** and can afford batch processing: attention/Transformers.

Architecture is not just accuracy—it’s compute, latency, memory, and data efficiency.

## Making Deep Nets Trainable: Initialization, Normalization, Residual Paths

### Why this section exists

In shallow models, SGD “just works” surprisingly often. In deep models, optimization can fail even when the model is expressive enough.

The chain-of-Jacobians view tells you why: signals and gradients must propagate through many transformations. If their magnitudes drift, training becomes unstable.

We’ll build a stable mental model in three steps:

1) initialization tries to keep variance roughly constant across layers

2) normalization actively stabilizes distributions during training

3) residual connections provide easy paths for gradient flow

---

## 1) Initialization as variance control

Consider a layer:

z=Wh\mathbf{z} = \mathbf{W}\mathbf{h}z=Wh

Assume hih\_ihi​ are i.i.d. with mean 0 and variance Var(hi)=σh2\mathrm{Var}(h\_i)=\sigma\_h^2Var(hi​)=σh2​. If weights have mean 0 and variance Var(Wij)=σw2\mathrm{Var}(W\_{ij})=\sigma\_w^2Var(Wij​)=σw2​, then (roughly):

Var(zj)≈n σw2 σh2\mathrm{Var}(z\_j) \approx n\,\sigma\_w^2\,\sigma\_h^2Var(zj​)≈nσw2​σh2​

where nnn is fan-in.

To keep Var(zj)\mathrm{Var}(z\_j)Var(zj​) from blowing up with depth, choose σw2∝1/n\sigma\_w^2 \propto 1/nσw2​∝1/n.

Two famous schemes:

- •**Xavier/Glorot** (good for tanh-like activations): σw2≈2fan-in+fan-out\sigma\_w^2 \approx \frac{2}{\text{fan-in}+\text{fan-out}}σw2​≈fan-in+fan-out2​
- •**He/Kaiming** (good for ReLU): σw2≈2fan-in\sigma\_w^2 \approx \frac{2}{\text{fan-in}}σw2​≈fan-in2​

These are not magic constants; they are attempts to keep forward activations and backward gradients in a reasonable range.

---

## 2) Normalization as conditioning control

Even with good initialization, distributions drift as parameters update. Normalization layers reduce internal covariate shift and improve conditioning.

### BatchNorm (BN)

For a mini-batch, BN normalizes pre-activations per feature:

z^=z−μBσB2+ϵ,y=γz^+β\hat{z} = \frac{z-\mu\_B}{\sqrt{\sigma\_B^2+\epsilon}}, \qquad y = \gamma\hat{z}+\betaz^=σB2​+ϵ​z−μB​​,y=γz^+β

- •μB,σB2\mu\_B, \sigma\_B^2μB​,σB2​ computed over the batch
- •γ,β\gamma,\betaγ,β are learned scale/shift

**Pros:** strong stabilizer, often speeds up CNN training.

**Cons:** batch-size dependence; tricky for RNNs/online/very small batches.

### LayerNorm (LN)

LN normalizes across features within a single example:

z^=z−μσ2+ϵ\hat{\mathbf{z}} = \frac{\mathbf{z}-\mu}{\sqrt{\sigma^2+\epsilon}}z^=σ2+ϵ​z−μ​

**Pros:** works well in Transformers; independent of batch size.

### RMSNorm

RMSNorm scales by root-mean-square without subtracting the mean:

RMS=1d∑izi2+ϵ,z^=zRMS\mathrm{RMS} = \sqrt{\frac{1}{d}\sum\_i z\_i^2 + \epsilon}, \qquad \hat{\mathbf{z}} = \frac{\mathbf{z}}{\mathrm{RMS}}RMS=d1​i∑​zi2​+ϵ​,z^=RMSz​

Often used in modern LLM stacks for simplicity and stability.

---

## 3) Residual connections as gradient highways

A residual block computes:

hℓ+1=hℓ+F(hℓ)\mathbf{h}^{\ell+1} = \mathbf{h}^{\ell} + F(\mathbf{h}^{\ell})hℓ+1=hℓ+F(hℓ)

Differentiate w.r.t. hℓ\mathbf{h}^{\ell}hℓ:

∂hℓ+1∂hℓ=I+∂F∂hℓ\frac{\partial \mathbf{h}^{\ell+1}}{\partial \mathbf{h}^{\ell}} = \mathbf{I} + \frac{\partial F}{\partial \mathbf{h}^{\ell}}∂hℓ∂hℓ+1​=I+∂hℓ∂F​

The identity term I\mathbf{I}I ensures there is always a path with derivative near 1, which combats vanishing gradients.

This is a key reason very deep networks (ResNets, deep Transformers) are trainable.

---

### Checkpoint: the stability toolkit

When a deep model won’t train, ask:

- •Are activations exploding/vanishing? (initialization, normalization)
- •Are gradients unstable? (residuals, normalization, learning rate)
- •Is the loss numerically unstable? (log-sum-exp tricks, mixed precision care)

These are not “details”—they are often the difference between success and failure.

## Application/Connection: Designing and Training Deep Models in Practice

### Why practice looks different from theory

In theory, you can specify fθf\_\thetafθ​ and run SGD. In practice, deep learning is an engineering loop:

1) pick an architecture with the right inductive bias

2) ensure optimization is stable (normalization, residuals, schedules)

3) regularize and validate (to generalize)

4) scale data/compute appropriately

Let’s connect the concepts to concrete workflows.

---

## A practical blueprint: from data to model

### Step 1: Represent input and output

- •Images: tensors ∈RC×H×W\in \mathbb{R}^{C\times H\times W}∈RC×H×W
- •Text: token IDs → embeddings ∈RT×d\in \mathbb{R}^{T\times d}∈RT×d
- •Tabular: normalized numeric + embeddings for categoricals

Decide output:

- •classification: softmax / sigmoid
- •regression: linear head (maybe with bounded activation)
- •sequence-to-sequence: autoregressive decoder or encoder-decoder

### Step 2: Choose an inductive bias

- •Spatial locality? Use CNN or vision transformer with patches.
- •Long-range dependencies? Use attention.
- •Need streaming? Consider RNNs or efficient attention variants.

### Step 3: Choose a loss and ensure numerical stability

For classification with logits s\mathbf{s}s and label yyy:

CE(s,y)=−log⁡esy∑kesk\mathrm{CE}(\mathbf{s},y) = -\log \frac{e^{s\_y}}{\sum\_k e^{s\_k}}CE(s,y)=−log∑k​esk​esy​​

Compute with stable log-sum-exp:

log⁡∑kesk=m+log⁡∑kesk−m,m=max⁡ksk\log \sum\_k e^{s\_k} = m + \log \sum\_k e^{s\_k-m}, \quad m=\max\_k s\_klogk∑​esk​=m+logk∑​esk​−m,m=kmax​sk​

This prevents overflow in eske^{s\_k}esk​.

### Step 4: Optimization choices (SGD family)

Even if you know SGD, deep learning often uses schedules and adaptive methods.

| Optimizer | Typical use | Notes |
| --- | --- | --- |
| SGD + momentum | CNNs, large-scale vision | often best generalization; needs tuning + LR schedule |
| Adam/AdamW | Transformers, NLP | fast convergence; AdamW decouples weight decay |

Learning rate schedules (cosine decay, step decay, warmup) can be as important as the optimizer.

### Step 5: Regularize for generalization

You already know L1/L2/dropout. In deep learning, common additional regularizers include:

- •data augmentation (especially vision)
- •early stopping
- •label smoothing
- •stochastic depth / drop-path (deep residual nets)

---

## Worked mental model: “depth creates features, architecture chooses which features are easy”

Tie back to our earlier 2-layer classifier:

- •adding layers lets the model build intermediate representations that progressively linearize the task
- •CNN bias makes “edge-like” features easy to learn everywhere
- •attention bias makes “copy/align” behavior easy to learn across positions

Deep learning succeeds when your architecture makes the right representations *cheap* to discover with gradient descent.

---

## Connections forward: why this node unlocks attention and meta-learning

- •**Attention mechanisms** refine the idea of learned representations by letting the model decide *where to read from* in its own activations.
- •**Meta-learning** treats the learning process itself as an object: deep nets can learn representations that adapt quickly, or learn optimizers/updates.

### Final checkpoint

If you can explain:

1) fθf\_\thetafθ​ as a composition of layers,

2) hℓ\mathbf{h}^\ellhℓ as learned representations,

3) inductive bias as the reason architectures differ,

4) trainability as controlling Jacobian products,

…then you have a working deep learning “tech tree” model that scales to modern architectures.

## Worked Examples (3)

### Example 1: Forward pass as feature building in a 2-layer ReLU network

Let x=[1−2]\mathbf{x} = \begin{bmatrix}1\\-2\end{bmatrix}x=[1−2​]. Define a 2-layer network:

Layer 1: h1=ReLU(W1x+b1)\mathbf{h}^1 = \mathrm{ReLU}(\mathbf{W}^1\mathbf{x}+\mathbf{b}^1)h1=ReLU(W1x+b1) with

W1=[11−120−1]\mathbf{W}^1 = \begin{bmatrix}1 & 1\\ -1 & 2\\ 0 & -1\end{bmatrix}W1=​1−10​12−1​​, b1=[01−1]\mathbf{b}^1=\begin{bmatrix}0\\1\\-1\end{bmatrix}b1=​01−1​​.

Layer 2 (logit): s=w2⋅h1+b2s = \mathbf{w}^2\cdot \mathbf{h}^1 + b^2s=w2⋅h1+b2 with w2=[2−11]\mathbf{w}^2=\begin{bmatrix}2\\-1\\1\end{bmatrix}w2=​2−11​​ and b2=0b^2=0b2=0. Output probability y^=σ(s)\hat{y}=\sigma(s)y^​=σ(s).

1. Compute pre-activation z1=W1x+b1\mathbf{z}^1 = \mathbf{W}^1\mathbf{x}+\mathbf{b}^1z1=W1x+b1:

   $\mathbf{W}^1\mathbf{x} = \begin{bmatrix}1 & 1\\ -1 & 2\\ 0 & -1\end{bmatrix}\begin{bmatrix}1\\-2\end{bmatrix}

   = \begin{bmatrix}1\cdot1 + 1\cdot(-2)\\ (-1)\cdot1 + 2\cdot(-2)\\ 0\cdot1 + (-1)\cdot(-2)\end{bmatrix}

   = \begin{bmatrix}-1\\ -5\\ 2\end{bmatrix}$.

   Add bias:

   z1=[−1−52]+[01−1]=[−1−41]\mathbf{z}^1 = \begin{bmatrix}-1\\ -5\\ 2\end{bmatrix} + \begin{bmatrix}0\\1\\-1\end{bmatrix} = \begin{bmatrix}-1\\ -4\\ 1\end{bmatrix}z1=​−1−52​​+​01−1​​=​−1−41​​.
2. Apply ReLU elementwise:

   h1=ReLU(z1)=[max⁡(0,−1)max⁡(0,−4)max⁡(0,1)]=[001]\mathbf{h}^1 = \mathrm{ReLU}(\mathbf{z}^1)=\begin{bmatrix}\max(0,-1)\\\max(0,-4)\\\max(0,1)\end{bmatrix} = \begin{bmatrix}0\\0\\1\end{bmatrix}h1=ReLU(z1)=​max(0,−1)max(0,−4)max(0,1)​​=​001​​.
3. Compute the logit:

   s=w2⋅h1=[2−11]⋅[001]=2⋅0+(−1)⋅0+1⋅1=1s = \mathbf{w}^2\cdot \mathbf{h}^1 = \begin{bmatrix}2\\-1\\1\end{bmatrix}\cdot\begin{bmatrix}0\\0\\1\end{bmatrix} = 2\cdot0 + (-1)\cdot0 + 1\cdot1 = 1s=w2⋅h1=​2−11​​⋅​001​​=2⋅0+(−1)⋅0+1⋅1=1.
4. Convert to probability with sigmoid:

   y^=σ(1)=11+e−1≈0.731\hat{y} = \sigma(1)=\frac{1}{1+e^{-1}} \approx 0.731y^​=σ(1)=1+e−11​≈0.731.

**Insight:** Even this tiny deep net builds a representation h1\mathbf{h}^1h1 where the final decision is simple (a dot product). ReLU created a sparse feature vector: only the third feature is active for this input. Scaling depth increases the space of learned features and their compositional reuse.

### Example 2: Why gradients can vanish/explode (a Jacobian product toy calculation)

Consider a depth-LLL scalar network (for intuition):

h0=xh^0=xh0=x, and for ℓ=1,…,L\ell=1,\dots,Lℓ=1,…,L:

hℓ=a hℓ−1h^{\ell} = a\, h^{\ell-1}hℓ=ahℓ−1 (a linear layer with scalar weight aaa).

Output is hL=aLxh^L = a^L xhL=aLx. We examine ∂hL∂x\frac{\partial h^L}{\partial x}∂x∂hL​ and how it scales with depth.

1. Write the closed form:

   h1=axh^1 = a xh1=ax

   h2=ah1=a(ax)=a2xh^2 = a h^1 = a(ax)=a^2 xh2=ah1=a(ax)=a2x

   By induction:

   hL=aLxh^L = a^L xhL=aLx.
2. Differentiate w.r.t. input:

   ∂hL∂x=∂(aLx)∂x=aL\frac{\partial h^L}{\partial x} = \frac{\partial (a^L x)}{\partial x} = a^L∂x∂hL​=∂x∂(aLx)​=aL.
3. Analyze cases:

   If ∣a∣<1|a|<1∣a∣<1, then ∣a∣L→0|a|^L \to 0∣a∣L→0 as LLL grows ⇒ gradients vanish.

   If ∣a∣>1|a|>1∣a∣>1, then ∣a∣L→∞|a|^L \to \infty∣a∣L→∞ ⇒ gradients explode.

   If ∣a∣≈1|a|\approx 1∣a∣≈1, gradients stay in a workable range.

**Insight:** Real networks are not scalar, but the principle survives: deep learning stability depends on keeping the effective Jacobian product near an isometry (singular values near 1). Initialization, normalization, and residual connections are practical tools to approximate this behavior.

### Example 3: CNN parameter efficiency vs dense layers (quick comparison)

Compare two ways to process a 32×32 RGB image (C=3C=3C=3). Option A: a dense layer to 100 hidden units. Option B: a conv layer with 64 kernels of size 3×3.

We count parameters (ignoring biases for simplicity).

1. Dense layer: flatten input size is $32\cdot32\cdot3 = 3072$.

   Parameters = $3072 \times 100 = 307,200$.
2. Convolution: each kernel has size $3\times3\times C\_{in} = 3\times3\times3 = 27$.

   With 64 output channels:

   Parameters = $27 \times 64 = 1,728$.
3. Compare:

   Dense: 307,200 parameters

   Conv: 1,728 parameters

   The conv layer uses about $307,200 / 1,728 \approx 178$× fewer parameters.

**Insight:** Weight sharing and locality massively reduce parameters while matching image structure. This is inductive bias made concrete: CNNs restrict the function family to translation-equivariant local pattern detectors, improving sample efficiency.

## Key Takeaways

- ✓

  A deep network is a nested composition: fθ(x)=fL(⋯f2(f1(x)))f\_\theta(x)=f\_L(\cdots f\_2(f\_1(x)))fθ​(x)=fL​(⋯f2​(f1​(x))), producing intermediate representations hℓ\mathbf{h}^\ellhℓ.
- ✓

  Depth primarily helps by enabling **hierarchical feature composition** and feature reuse—not merely by adding parameters.
- ✓

  Training stability is governed by products of Jacobians; vanishing/exploding gradients are expected failure modes without careful design.
- ✓

  Architectures are defined by **inductive biases** (locality, weight sharing, recurrence, attention) that improve sample efficiency and generalization.
- ✓

  CNNs encode translation equivariance and locality; RNNs encode sequential state; attention enables flexible long-range interactions.
- ✓

  Initialization schemes (Xavier/He) aim to keep activation/gradient scales reasonable across layers.
- ✓

  Normalization (BatchNorm/LayerNorm/RMSNorm) improves conditioning and stability; residual connections provide gradient highways.
- ✓

  Deep learning practice is an engineering loop balancing architecture, optimization, regularization, and compute constraints.

## Common Mistakes

- ✗

  Treating depth as automatically beneficial: deeper models can be harder to optimize and may overfit without the right stabilizers and regularization.
- ✗

  Ignoring conditioning: using arbitrary initialization or omitting normalization/residuals often causes silent training failure (loss plateaus or NaNs).
- ✗

  Choosing architecture by trend rather than inductive bias: e.g., using an MLP on images without exploiting locality, or using attention when streaming constraints require recurrence.
- ✗

  Debugging only the optimizer: many issues blamed on SGD/Adam are actually numerical stability, normalization placement, or learning-rate schedule problems.

## Practice

easy

You have a depth-10 network where each layer (locally) has an average Jacobian spectral norm of about 0.9. Roughly how will gradient magnitudes scale from output back to the input? What qualitative behavior do you expect during training?

**Hint:** Use the idea that gradient scales like a product of per-layer factors.

Show solution

If each layer contributes a factor ≈ 0.9, then over 10 layers the scale is about $0.9^{10} \approx 0.35$. Gradients shrink as they propagate backward (vanishing tendency). Training may be slower for early layers and may require residual connections, normalization, or different initialization to keep effective scales closer to 1.

medium

Design choice: You need to classify 1-second audio clips sampled at 16 kHz. You can represent them as a spectrogram (time × frequency grid) or as raw waveform. Which inductive bias suggests a CNN is a strong baseline, and what structure is the CNN exploiting?

**Hint:** Think locality and weight sharing on a grid.

Show solution

A CNN is a strong baseline because audio (especially as a spectrogram) has local time-frequency structure: nearby time frames and frequencies form local patterns (harmonics, onsets). Convolutions exploit locality (small receptive fields) and weight sharing (same detector across time/frequency shifts), giving translation-equivariant feature extraction and parameter efficiency.

hard

Suppose you remove residual connections from a 48-layer Transformer block stack but keep everything else the same. Using the chain-of-Jacobians viewpoint, explain why optimization becomes much harder. Propose two architectural/training modifications that could partially compensate (even if imperfect).

**Hint:** Residuals add an identity term to the layer-to-layer derivative; without it the product of Jacobians must stay well-conditioned by itself.

Show solution

Without residuals, the layer-to-layer derivative is dominated by ∂F/∂h\partial F/\partial \mathbf{h}∂F/∂h rather than I+∂F/∂h\mathbf{I}+\partial F/\partial \mathbf{h}I+∂F/∂h. The gradient becomes a product of many non-identity Jacobians, making vanishing/exploding gradients much more likely (singular values drift away from 1). Two partial compensations: (1) stronger/appropriate normalization (e.g., careful LayerNorm/RMSNorm placement, possibly pre-norm) to stabilize activation distributions and Jacobian spectra; (2) adjust initialization and learning-rate schedule (smaller LR, warmup, scaled init) to keep updates small and maintain conditioning. Other possible aids include gradient clipping and reducing depth.

## Connections

[Attention Mechanisms](/tech-tree/attention-mechanisms/)

[Meta-Learning](/tech-tree/meta-learning/)

Quality: A (4.3/5)

[← back to tree](/tech-tree/)[browse all →](/tech-tree/inventory/)
