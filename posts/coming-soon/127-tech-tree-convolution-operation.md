---
title: Convolution Operation
description: The sliding-window dot-product between a kernel and input (1D/2D) used to extract local patterns and build translation-equivariant representations in convolutional networks. Grasping how stride, padding, and kernel size affect output shape and receptive field is key for CNN design.
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
permalink: /tech-tree/convolution-operation/
---

[←Back to Tech Tree](/tech-tree/)

[inventory](/tech-tree/inventory/)[coverage](/tech-tree/coverage/)

# Convolution Operation

Linear AlgebraDifficulty: ★★★☆☆Depth: 0Unlocks: 4

The sliding-window dot-product between a kernel and input (1D/2D) used to extract local patterns and build translation-equivariant representations in convolutional networks. Grasping how stride, padding, and kernel size affect output shape and receptive field is key for CNN design.

## Interactive Visualization

⏮◀◀▶▶STEP0.25x1xZOOM

t=0s

## Core Concepts

- -Convolution as a sliding-window dot-product: apply a small kernel over local input patches (1D/2D) producing one weighted sum per output position.
- -Kernel as a local pattern detector applied identically across positions (weight-sharing) - this yields translation equivariance.
- -Kernel size defines the local receptive field for each output; repeated convolutions and kernel stacking expand the overall receptive field.

## Key Symbols & Notation

asterisk symbol for convolution ("\*")

## Essential Relationships

- -Output(p) = dot\_product(kernel, input\_patch aligned at p) - the sliding-window weighted sum.
- -Kernel size, stride, and padding determine which input indices form each patch, thus setting output spatial size and each output's receptive field.

## Unlocks (1)

[Deep Learninglvl 5](/tech-tree/deep-learning/)

Advanced Learning Details

### Graph Position

6

Depth Cost

4

Fan-Out (ROI)

2

Bottleneck Score

0

Chain Length

### Cognitive Load

6

Atomic Elements

46

Total Elements

L3

Percentile Level

L4

Atomic Level

### All Concepts (18)

- - Convolution as a sliding-window dot product: applying a kernel over local windows of the input and computing a dot product at each spatial position
- - Kernel / filter: a small weight tensor that is moved across the input to detect local patterns
- - Feature map / output activation map: the spatial map of dot-product responses produced by a kernel
- - Local receptive field: the subset (window) of input entries that influence one output position
- - Weight sharing: the same kernel (same weights) applied at every spatial location
- - Translation equivariance: a property where a spatial shift in the input produces the same shift in the output responses
- - Stride: the step size between neighboring kernel placements (controls sampling and downsampling)
- - Padding: adding border values (usually zeros) around the input to control boundary behavior and output size
- - Kernel size: the spatial extent (e.g., k or k\_h x k\_w) of the kernel that determines how much local context is pooled
- - Output shape (spatial dimensions) of a convolutional layer as a function of input size, kernel size, padding, and stride
- - Boundary modes / padding schemes: common modes like 'valid' (no padding), 'same' (pad to preserve size), and 'full' (maximal padding)
- - Downsampling effect of stride: larger strides reduce output spatial resolution
- - Receptive field of an output unit: the region of the original input that can affect that output unit
- - How stacked convolutional layers combine to produce a larger effective receptive field
- - Multi-channel convolution: kernels that span input channels and sum dot-products across channels to produce each output channel
- - Parameter count for a convolutional layer depends on kernel spatial size and number of in/out channels (not on input spatial size)
- - Dot-product response as local pattern detection: the kernel acts as a template and the dot product measures similarity to that template
- - Convolution versus cross-correlation practical distinction: many implementations perform cross-correlation (no kernel flip) though 'convolution' is commonly used

### Teaching Strategy

Deep-dive lesson - accessible entry point but dense material. Use worked examples and spaced repetition.

Convolution is the workhorse operation behind CNNs: a small set of weights (a kernel) slides across an input and produces a new signal/image whose values tell you “how much this local pattern appears here.” The power comes from doing the same computation everywhere (weight sharing), which naturally builds translation-equivariant representations.

TL;DR:

A (discrete) convolution layer computes a sliding-window dot product between a kernel and local patches of the input. Stride, padding, and dilation control where the kernel is applied and therefore determine output shape and receptive field. In deep learning libraries, what’s called “convolution” is usually cross-correlation (no kernel flip), but the shape math and intuition are the same.

## Prerequisites and Conventions (read this to avoid implementation confusion)

This node is designed to be foundational, but a few micro-prereqs and conventions will save you from common shape bugs.

## Micro-prerequisites

You should be comfortable with:

1) **Indices and summations**

- •Reading formulas like ∑ᵢ xᵢ wᵢ and tracking which index means “position.”

2) **Dot product**

- •For vectors **x**, **w** ∈ ℝᵏ:

x⋅w=∑i=0k−1xiwi\mathbf{x} \cdot \mathbf{w} = \sum\_{i=0}^{k-1} x\_i w\_ix⋅w=i=0∑k−1​xi​wi​

3) **Arrays / tensors and shapes**

- •1D signal: length L (shape [L])
- •2D image: height H, width W (shape [H, W])
- •With channels: [C, H, W] or [H, W, C]
- •With batch: [N, C, H, W] or [N, H, W, C]

4) **Basic CNN layer conventions**

- •“Kernel/filter” size (k), stride (s), padding (p), dilation (d)
- •Input channels C\_in, output channels C\_out

## Critical convention: convolution vs cross-correlation

In classical signal processing, discrete **convolution** flips the kernel. In most deep learning libraries, the operation named `conv` is actually **cross-correlation** (no flip). For 1D:

- •Cross-correlation (what CNNs typically compute):

y[n]=∑i=0k−1w[i] x[n+i]y[n] = \sum\_{i=0}^{k-1} w[i]\,x[n + i]y[n]=i=0∑k−1​w[i]x[n+i]

- •Convolution (signal processing definition, flipped kernel):

y[n]=∑i=0k−1w[i] x[n−i]y[n] = \sum\_{i=0}^{k-1} w[i]\,x[n - i]y[n]=i=0∑k−1​w[i]x[n−i]

For learning CNNs, the “pattern detector sliding” intuition works either way; the network can learn flipped weights if needed. What matters most in practice is **shape math** and **which positions are included**.

## Channel order: NCHW vs NHWC

Different frameworks store tensors differently:

| Name | Meaning | Common in |
| --- | --- | --- |
| NCHW | [batch, channels, height, width] | PyTorch (default), many CUDA kernels |
| NHWC | [batch, height, width, channels] | TensorFlow (often), some accelerators |

The convolution math is identical; only the dimension ordering changes.

## “Same” padding is not one universal rule

Libraries define `padding="same"` to mean “output spatial size is approximately input size when stride=1,” but when stride>1 there are multiple choices (rounding up vs down, distributing extra pad left/right). When you care about exact sizes, use the explicit formula with (p\_left, p\_right) rather than relying on a name.

## Dilation exists (we’ll define it later)

Dilation spaces out kernel taps. It changes the **effective kernel size** and receptive field without increasing parameter count.

Keep these in mind; they directly address the most common beginner failure mode: implementing a conv layer and getting an output whose shape doesn’t match your expectation.

## What Is Convolution Operation?

### Why this operation exists

Many data types have a strong notion of **locality**:

- •Audio: nearby samples form local wave patterns.
- •Text (as sequences): nearby tokens form local n-grams.
- •Images: nearby pixels form edges, corners, textures.

A fully connected layer mixes *everything with everything*, which is expensive and ignores locality. Convolution instead says:

1) Look at a **small local patch**.

2) Compute a **dot product** with a kernel (a learned pattern).

3) Slide that kernel across positions, reusing the **same weights**.

This reuse is called **weight sharing**. It gives you an inductive bias: if a feature (like a vertical edge) matters at one location, it likely matters at other locations too.

### Core definition (1D intuition first)

Let x be a 1D input of length L and w be a kernel of length k. We form an output y where each y[n] is a weighted sum of a window of x.

A common deep-learning definition (cross-correlation) is:

y[n]=∑i=0k−1w[i] x[n+i]y[n] = \sum\_{i=0}^{k-1} w[i] \, x[n + i]y[n]=i=0∑k−1​w[i]x[n+i]

Interpretation:

- •At output position n, you grab the input slice (x[n], x[n+1], …, x[n+k-1]).
- •You compute the dot product with weights (w[0], …, w[k-1]).

So each y[n] is:

y[n]=w⋅xpatch at ny[n] = \mathbf{w} \cdot \mathbf{x}\_{\text{patch at }n}y[n]=w⋅xpatch at n​

### Extending to 2D (images)

For an image x with height H and width W, and a 2D kernel w of size k\_h × k\_w, the output at (u, v) is:

y[u,v]=∑i=0kh−1∑j=0kw−1w[i,j] x[u+i,v+j]y[u,v] = \sum\_{i=0}^{k\_h-1} \sum\_{j=0}^{k\_w-1} w[i,j] \, x[u+i, v+j]y[u,v]=i=0∑kh​−1​j=0∑kw​−1​w[i,j]x[u+i,v+j]

Again, it’s a dot product between a flattened patch and the flattened kernel.

### Multi-channel convolution (what CNNs actually use)

Images typically have channels (RGB), and intermediate CNN layers have many channels. A convolution kernel spans **all input channels**.

If input x has C\_in channels and kernel has C\_in channels too, then:

y[u,v]=∑c=0Cin−1∑i=0kh−1∑j=0kw−1w[c,i,j] x[c,u+i,v+j]y[u,v] = \sum\_{c=0}^{C\_{in}-1} \sum\_{i=0}^{k\_h-1} \sum\_{j=0}^{k\_w-1} w[c,i,j] \, x[c, u+i, v+j]y[u,v]=c=0∑Cin​−1​i=0∑kh​−1​j=0∑kw​−1​w[c,i,j]x[c,u+i,v+j]

And if you want **C\_out** output channels, you learn **C\_out different kernels**, one per output channel. The full weight tensor is shaped:

- •(C\_out, C\_in, k\_h, k\_w) in NCHW-style frameworks

### Two big ideas embedded in the definition

1) **Local receptive field**: y[u,v] depends only on a local neighborhood of x.

2) **Translation equivariance**: if you shift the input, the output shifts correspondingly (ignoring boundary effects from padding). This comes from applying the *same* kernel at every location.

Equivariance is not the same as invariance:

- •Equivariant: shift input → shift output.
- •Invariant: shift input → output stays the same (pooling or global averaging can create invariance).

Convolution gives you the equivariant building block that deeper architectures can compose into higher-level behavior.

## Core Mechanic 1: Sliding-Window Dot Product (stride, padding, dilation, output shape)

This section is about the “physics” of convolution in code: where the kernel lands, how many outputs you get, and what stride/padding/dilation actually do.

## 1) Stride: how far you move the window

With stride s (1D), you compute outputs at positions n = 0, s, 2s, … rather than every position.

For 2D, you have stride (s\_h, s\_w). The kernel top-left corner moves by s\_h rows and s\_w columns.

**Effect:** larger stride → smaller output spatial size → more downsampling.

## 2) Padding: what happens at the boundaries

Without padding, you can only place the kernel where it fully fits in the input. That shrinks the output.

Padding adds extra values around the border, commonly zeros.

- •1D: pad p\_left on the left and p\_right on the right
- •2D: pad (p\_top, p\_bottom, p\_left, p\_right)

**Effect:** more padding → larger output spatial size and more border coverage.

Boundary note: padding breaks perfect translation equivariance at the edges because the border now “sees” artificial values.

## 3) Dilation: spacing out kernel taps

Dilation d inserts gaps between kernel elements. In 1D, a kernel with k elements and dilation d covers an **effective size**:

keff=d (k−1)+1k\_{eff} = d\,(k-1) + 1keff​=d(k−1)+1

Example: k=3, d=2 covers positions like [0, 2, 4] → k\_eff=5.

In 2D, apply this per dimension:

- •$kh,eff=dh(kh−1)+1k\_{h,eff} = d\_h (k\_h-1)+1kh,eff​=dh​(kh​−1)+1$
- •$kw,eff=dw(kw−1)+1k\_{w,eff} = d\_w (k\_w-1)+1kw,eff​=dw​(kw​−1)+1$

**Effect:** increases receptive field without increasing parameter count, but can “skip over” fine details.

## 4) Output shape formula (1D)

Let:

- •input length L
- •kernel size k
- •dilation d
- •padding p\_left, p\_right (total p = p\_left + p\_right)
- •stride s

Compute effective kernel size:

keff=d (k−1)+1k\_{eff} = d\,(k-1) + 1keff​=d(k−1)+1

Then output length L\_out is:

Lout=⌊L+p−keffs⌋+1L\_{out} = \left\lfloor \frac{L + p - k\_{eff}}{s} \right\rfloor + 1Lout​=⌊sL+p−keff​​⌋+1

Why the floor? Because you only count kernel placements that fit.

### Quick derivation (showing the logic)

The last valid output position corresponds to the last kernel placement whose rightmost sampled index is within the padded input.

- •Padded input length: L + p
- •If the kernel starts at position n, its rightmost covered index is n + (k\_eff - 1)
- •Valid if: n + (k\_eff - 1) ≤ (L + p) - 1

So:

n≤L+p−keffn \le L + p - k\_{eff}n≤L+p−keff​

With stride s, starts are n = 0, s, 2s, …, m s. Largest m such that m s ≤ L + p - k\_eff is:

m=⌊L+p−keffs⌋m = \left\lfloor \frac{L + p - k\_{eff}}{s} \right\rfloorm=⌊sL+p−keff​​⌋

And the number of outputs is m+1:

Lout=m+1=⌊L+p−keffs⌋+1L\_{out} = m+1 = \left\lfloor \frac{L + p - k\_{eff}}{s} \right\rfloor + 1Lout​=m+1=⌊sL+p−keff​​⌋+1

## 5) Output shape formula (2D)

For input H×W, kernel k\_h×k\_w, dilation d\_h,d\_w, stride s\_h,s\_w, and padding totals p\_h = p\_top+p\_bottom, p\_w = p\_left+p\_right:

Hout=⌊H+ph−kh,effsh⌋+1H\_{out} = \left\lfloor \frac{H + p\_h - k\_{h,eff}}{s\_h} \right\rfloor + 1Hout​=⌊sh​H+ph​−kh,eff​​⌋+1

Wout=⌊W+pw−kw,effsw⌋+1W\_{out} = \left\lfloor \frac{W + p\_w - k\_{w,eff}}{s\_w} \right\rfloor + 1Wout​=⌊sw​W+pw​−kw,eff​​⌋+1

where

kh,eff=dh(kh−1)+1,kw,eff=dw(kw−1)+1k\_{h,eff} = d\_h (k\_h-1)+1, \quad k\_{w,eff} = d\_w (k\_w-1)+1kh,eff​=dh​(kh​−1)+1,kw,eff​=dw​(kw​−1)+1

## 6) “Valid” vs “Same” vs explicit padding

It helps to name common padding schemes, but always ground them in the formula.

| Scheme | Typical meaning | Outcome (stride=1, dilation=1) |
| --- | --- | --- |
| valid | p=0 | output shrinks: L\_out = L-k+1 |
| same | choose p so L\_out = L | preserves length/size |

For stride=1, dilation=1, to get L\_out = L you need:

L=L+p−k1+1⇒p=k−1L = \frac{L + p - k}{1} + 1 \Rightarrow p = k-1L=1L+p−k​+1⇒p=k−1

That means total padding p = k-1. Usually you split it as evenly as possible:

- •p\_left = ⌊(k-1)/2⌋, p\_right = ⌈(k-1)/2⌉

For 2D, do this per dimension.

When stride>1, there is not a single padding that guarantees H\_out = H exactly; libraries choose rules like “output is ceil(H/stride).” If you need exactness, compute padding explicitly.

## 7) Parameter count and compute cost (sanity checks)

For a standard 2D conv with C\_in input channels and C\_out output channels:

- •Weight parameters: C\_out · C\_in · k\_h · k\_w
- •Bias parameters (if used): C\_out

Compute is roughly proportional to:

- •N · H\_out · W\_out · C\_out · (C\_in · k\_h · k\_w)

These simple counts help you reason about model size and performance.

## Core Mechanic 2: Weight Sharing, Translation Equivariance, and Receptive Field Growth

Now that you can compute shapes, the next step is understanding why convolutions are such a good building block.

## 1) Kernel as a local pattern detector

Think of a kernel as encoding a template.

- •In 1D, it can detect rising/falling edges in a signal.
- •In 2D, classic hand-designed kernels detect edges:
- •horizontal edge detector
- •vertical edge detector

At each position, the dot product is high when the local patch aligns with the kernel’s pattern.

### Dot product = similarity (with caveats)

If you normalize vectors, the dot product relates to cosine similarity. CNNs don’t usually normalize patches, so magnitude also matters. But the intuition remains: convolution measures how much a pattern is present locally.

## 2) Weight sharing → translation equivariance

Weight sharing means the same weights w are used for every location. This creates a structured linear map.

Let T\_Δ be a shift operator that shifts the input by Δ (in 1D, Δ is an integer). For interior positions (ignoring boundary padding effects), convolution satisfies:

Conv(TΔx)=TΔ(Conv(x))\text{Conv}(T\_\Delta x) = T\_\Delta (\text{Conv}(x))Conv(TΔ​x)=TΔ​(Conv(x))

That is **equivariance**.

Why you care:

- •If an object moves in the image, its feature map moves in the same way.
- •Downstream layers can then reason about *where* the feature is.

Padding caveat:

- •Zero padding introduces special behavior at borders, so equivariance holds perfectly only away from edges.

## 3) Stacking convolutions expands the receptive field

The **receptive field** of an output unit is the region of the input that can affect it.

For a single conv layer with kernel size k and dilation 1:

- •Each output depends on k input positions (1D) or k\_h×k\_w pixels (2D).

But when you stack layers, receptive fields grow.

### 1D receptive field with stride 1 (simple case)

Suppose you apply two conv layers, both with kernel size k=3, stride=1, dilation=1.

Layer 1:

- •y₁[n] depends on x[n], x[n+1], x[n+2]

Layer 2:

- •y₂[n] depends on y₁[n], y₁[n+1], y₁[n+2]

Substitute dependencies:

- •y₁[n] uses x[n..n+2]
- •y₁[n+1] uses x[n+1..n+3]
- •y₁[n+2] uses x[n+2..n+4]

So y₂[n] depends on x[n..n+4], i.e. 5 input positions.

This shows a pattern: with stride=1 and dilation=1, stacking k=3 layers increases receptive field by 2 each layer.

### General receptive field growth (useful rule of thumb)

For 1D layers ℓ=1..L, with kernel sizes k\_ℓ and strides s\_ℓ (ignore dilation for a moment), define:

- •jump j₀ = 1 (distance in input between adjacent receptive field centers)
- •receptive field r₀ = 1

Update per layer:

jℓ=jℓ−1⋅sℓj\_\ell = j\_{\ell-1} \cdot s\_\elljℓ​=jℓ−1​⋅sℓ​

rℓ=rℓ−1+(kℓ−1)⋅jℓ−1r\_\ell = r\_{\ell-1} + (k\_\ell - 1) \cdot j\_{\ell-1}rℓ​=rℓ−1​+(kℓ​−1)⋅jℓ−1​

This is a standard CNN design tool: stride increases the jump (downsampling), and kernel size increases the field.

If you include dilation d\_ℓ, replace (k\_ℓ − 1) with (k\_{eff,ℓ} − 1) where k\_eff = d(k−1)+1.

## 4) Multiple kernels = multiple learned features

A conv layer usually has many output channels. Each output channel corresponds to a different kernel (feature detector).

So at each spatial location, you don’t just output one number; you output a vector of C\_out numbers. You can think of that vector as a learned local descriptor.

## 5) Convolution is linear (per channel) but CNNs are not

Convolution itself is a linear operation in x:

Conv(ax1+bx2)=a Conv(x1)+b Conv(x2)\text{Conv}(a x\_1 + b x\_2) = a\,\text{Conv}(x\_1) + b\,\text{Conv}(x\_2)Conv(ax1​+bx2​)=aConv(x1​)+bConv(x2​)

CNNs become powerful because you compose:

- •conv (linear)
- •nonlinearity (ReLU, GELU)
- •normalization
- •pooling/downsampling

The conv operation is the structured linear piece that respects locality and translation structure.

## Application / Connection: How Convolution Is Used in CNN Design (and how libraries parameterize it)

This section connects the operation to practical CNN design decisions and implementation details.

## 1) Designing for shapes: a workflow

When you design a CNN block, you typically decide:

1) Desired change in spatial size (keep, half, quarter)

2) Number of channels (C\_in → C\_out)

3) Kernel size (locality) and whether to use dilation

4) Padding to control boundaries

A common pattern:

- •Use k=3, stride=1, padding=1 (for dilation=1) to preserve H×W.
- •Downsample using stride=2 (sometimes with k=3, p=1).

### Example: “same-size” 3×3 conv (stride 1)

For k=3, dilation=1, want H\_out = H.

- •Need total padding p\_h = 2, so p\_top=1, p\_bottom=1.
- •Same for width.

## 2) Dilation vs larger kernels

If you want a larger receptive field, you can:

- •Increase kernel size (e.g., 5×5)
- •Stack multiple 3×3 layers
- •Use dilation (e.g., 3×3 with d=2 gives k\_eff=5)

Trade-offs:

| Method | Pros | Cons |
| --- | --- | --- |
| Larger kernel | Direct, dense coverage | More parameters and compute |
| Stack 3×3 | Often efficient; more nonlinearities | Deeper network, may be harder to optimize |
| Dilation | Big receptive field, same params | Can miss fine detail; gridding artifacts |

## 3) Grouped and depthwise convolution (heads-up)

Even though this node focuses on standard convolution, you’ll see these variants:

- •**Grouped conv**: split channels into G groups; each group convolves independently.
- •Weight shape: (C\_out, C\_in/G, k\_h, k\_w)
- •Used in ResNeXt, some efficient architectures.

- •**Depthwise conv**: special case where G = C\_in (each channel has its own kernel).
- •Used in MobileNet; often followed by a 1×1 “pointwise” conv.

These change parameter count and mixing across channels.

## 4) Library parameters you must map correctly

When you implement `Conv2d` / `tf.nn.conv2d`, you must align:

1) **Tensor layout**

- •PyTorch expects NCHW by default.
- •TensorFlow `conv2d` often uses NHWC unless configured.

2) **Weight layout**

- •PyTorch Conv2d weights: (C\_out, C\_in, k\_h, k\_w)
- •TensorFlow weights typically: (k\_h, k\_w, C\_in, C\_out)

3) **Padding semantics**

- •Explicit padding: you specify exact integers.
- •SAME/VALID: framework-defined. For stride>1, SAME often gives:
- •H\_out = ceil(H / s\_h)
- •W\_out = ceil(W / s\_w)

and pads accordingly.

4) **Dilation parameter**

- •Ensure you understand whether dilation is per spatial dimension.

## 5) The “im2col” mental model (optional but clarifying)

A convolution can be implemented by:

1) Extracting all patches into a big matrix (each row = one patch) → `im2col`

2) Flattening kernels into columns

3) Doing a matrix multiply

This shows convolution is a structured linear operator. It also explains why:

- •It’s differentiable and easy to backprop through
- •It can be accelerated heavily on GPUs

You don’t need to implement `im2col`, but knowing it helps debug shapes: patches correspond to output positions.

## 6) Where this connects next

Once you’re fluent with convolution mechanics, you can understand:

- •CNN architectures (VGG, ResNet)
- •Feature hierarchies (edges → textures → parts → objects)
- •Translation equivariance and how pooling/global average pooling turn it into invariance
- •Why convolutions are a natural fit for images and other grid-like data

This node is the gateway from basic linear algebra (dot products) to deep learning feature extraction.

## Worked Examples (3)

### Worked Example 1 (1D): Compute convolution output values and output length

Input x (length L=6): x = [1, 2, 0, -1, 3, 1]

Kernel w (length k=3): w = [2, -1, 1]

Use cross-correlation convention (no flip), stride s=1, padding p=0, dilation d=1.

1. List the patches of length 3 (since k=3) that fit with p=0:

   - •patch at n=0: [x0, x1, x2] = [1, 2, 0]
   - •patch at n=1: [x1, x2, x3] = [2, 0, -1]
   - •patch at n=2: [x2, x3, x4] = [0, -1, 3]
   - •patch at n=3: [x3, x4, x5] = [-1, 3, 1]
2. Compute output length using the formula:

   Effective kernel size: k\_eff = d(k-1)+1 = 1·(3-1)+1 = 3

   Total padding p = 0

   Lout=⌊L+p−keffs⌋+1=⌊6+0−31⌋+1=3+1=4L\_{out} = \left\lfloor \frac{L + p - k\_{eff}}{s} \right\rfloor + 1 = \left\lfloor \frac{6 + 0 - 3}{1} \right\rfloor + 1 = 3 + 1 = 4Lout​=⌊sL+p−keff​​⌋+1=⌊16+0−3​⌋+1=3+1=4

   So y has length 4 (indices 0..3).
3. Compute each y[n] as a dot product y[n] = ∑\_{i=0}^{2} w[i] x[n+i].

   n=0:

   y[0]=2⋅1+(−1)⋅2+1⋅0=2−2+0=0y[0] = 2·1 + (-1)·2 + 1·0 = 2 - 2 + 0 = 0y[0]=2⋅1+(−1)⋅2+1⋅0=2−2+0=0
4. n=1:

   y[1]=2⋅2+(−1)⋅0+1⋅(−1)=4+0−1=3y[1] = 2·2 + (-1)·0 + 1·(-1) = 4 + 0 - 1 = 3y[1]=2⋅2+(−1)⋅0+1⋅(−1)=4+0−1=3
5. n=2:

   y[2]=2⋅0+(−1)⋅(−1)+1⋅3=0+1+3=4y[2] = 2·0 + (-1)·(-1) + 1·3 = 0 + 1 + 3 = 4y[2]=2⋅0+(−1)⋅(−1)+1⋅3=0+1+3=4
6. n=3:

   y[3]=2⋅(−1)+(−1)⋅3+1⋅1=−2−3+1=−4y[3] = 2·(-1) + (-1)·3 + 1·1 = -2 - 3 + 1 = -4y[3]=2⋅(−1)+(−1)⋅3+1⋅1=−2−3+1=−4
7. Final output:

   y = [0, 3, 4, -4]

**Insight:** Each output is just a dot product between the kernel and a local patch. The output length comes from counting how many valid kernel placements fit; the formula matches the patch list exactly.

### Worked Example 2 (2D): Output shape with stride, padding, and dilation

Input image x has shape H×W = 7×7 (ignore channels for shape math).

Kernel size k\_h×k\_w = 3×3.

Stride s\_h=s\_w=2.

Dilation d\_h=d\_w=1.

Padding: p\_top=p\_bottom=p\_left=p\_right=1 (so totals p\_h=2, p\_w=2).

1. Compute effective kernel sizes:

   kh,eff=dh(kh−1)+1=1⋅(3−1)+1=3k\_{h,eff} = d\_h (k\_h-1)+1 = 1·(3-1)+1 = 3kh,eff​=dh​(kh​−1)+1=1⋅(3−1)+1=3

   kw,eff=dw(kw−1)+1=3k\_{w,eff} = d\_w (k\_w-1)+1 = 3kw,eff​=dw​(kw​−1)+1=3
2. Compute output height:

   Hout=⌊H+ph−kh,effsh⌋+1=⌊7+2−32⌋+1H\_{out} = \left\lfloor \frac{H + p\_h - k\_{h,eff}}{s\_h} \right\rfloor + 1 = \left\lfloor \frac{7 + 2 - 3}{2} \right\rfloor + 1Hout​=⌊sh​H+ph​−kh,eff​​⌋+1=⌊27+2−3​⌋+1

   Simplify:

   7+2-3 = 6

   Hout=⌊62⌋+1=3+1=4H\_{out} = \left\lfloor \frac{6}{2} \right\rfloor + 1 = 3 + 1 = 4Hout​=⌊26​⌋+1=3+1=4
3. Compute output width (same numbers):

   Wout=⌊W+pw−kw,effsw⌋+1=⌊7+2−32⌋+1=4W\_{out} = \left\lfloor \frac{W + p\_w - k\_{w,eff}}{s\_w} \right\rfloor + 1 = \left\lfloor \frac{7 + 2 - 3}{2} \right\rfloor + 1 = 4Wout​=⌊sw​W+pw​−kw,eff​​⌋+1=⌊27+2−3​⌋+1=4
4. So the output spatial shape is 4×4.

   Sanity check by thinking in placements:

   - •With padding 1, the “padded input” is 9×9.
   - •A 3×3 kernel with stride 2 has top-left corners at rows 0,2,4,6 (4 positions) and same for columns → 4×4 outputs.

**Insight:** The shape formula is just counting how many stride-spaced kernel placements fit inside the padded input. Padding made the padded input 9×9, enabling 4 placements along each dimension with stride 2.

### Worked Example 3 (Receptive field): Two stacked 3×3 conv layers

Consider a 2D CNN block with two convolution layers, both with kernel 3×3, stride 1, dilation 1, and padding 1 (so spatial sizes are preserved). We track the receptive field size (in one dimension; it’s symmetric in H and W here).

1. Initialize receptive field and jump:

   - •r₀ = 1 (a single input pixel)
   - •j₀ = 1 (neighboring outputs correspond to neighboring input centers)
2. Layer 1: k=3, s=1

   j1=j0⋅s=1⋅1=1j\_1 = j\_0 · s = 1·1 = 1j1​=j0​⋅s=1⋅1=1

   r1=r0+(k−1)⋅j0=1+2⋅1=3r\_1 = r\_0 + (k-1)·j\_0 = 1 + 2·1 = 3r1​=r0​+(k−1)⋅j0​=1+2⋅1=3

   After the first conv, each output pixel sees a 3-pixel-wide region (in 1D).
3. Layer 2: k=3, s=1

   j2=j1⋅s=1j\_2 = j\_1 · s = 1j2​=j1​⋅s=1

   r2=r1+(k−1)⋅j1=3+2⋅1=5r\_2 = r\_1 + (k-1)·j\_1 = 3 + 2·1 = 5r2​=r1​+(k−1)⋅j1​=3+2⋅1=5
4. Conclusion:

   Two stacked 3×3 stride-1 conv layers yield a receptive field of 5×5 in 2D (since 5 in height and 5 in width).

**Insight:** Stacking small kernels grows receptive field gradually while adding nonlinearities between them—one reason repeated 3×3 convs are so common in CNNs.

## Key Takeaways

- ✓

  A convolution (as used in CNNs) is a sliding-window dot product: each output value is a weighted sum of a local input patch.
- ✓

  Most deep learning libraries implement cross-correlation (no kernel flip) but still call it convolution; the learning behavior is essentially unaffected.
- ✓

  Weight sharing (same kernel at every position) is what gives convolution translation equivariance (away from boundary effects).
- ✓

  Stride controls downsampling: larger stride reduces output spatial size by skipping kernel placements.
- ✓

  Padding controls boundary behavior and output size; explicit padding values are safer than relying on ambiguous “same” rules for stride>1.
- ✓

  Dilation increases effective kernel size k\_eff = d(k−1)+1, expanding receptive field without increasing parameter count.
- ✓

  Output shapes follow floor-based formulas; they come directly from counting how many kernel placements fit in the padded input.
- ✓

  Stacking convolution layers expands receptive field; stride increases the jump between receptive field centers.

## Common Mistakes

- ✗

  Mixing up tensor layouts (NCHW vs NHWC) and weight layouts (PyTorch vs TensorFlow), leading to silent shape mismatches.
- ✗

  Assuming `padding="same"` means identical behavior across libraries or for stride>1; the rounding/distribution of padding can differ.
- ✗

  Forgetting dilation when computing output shape: you must use k\_eff, not k.
- ✗

  Confusing translation equivariance with invariance (equivariance preserves shifts; invariance requires pooling/aggregation).

## Practice

easy

1D shape practice: An input of length L=20 is convolved with kernel size k=5, stride s=2, dilation d=1, and total padding p=4 (e.g., 2 left + 2 right). What is L\_out?

**Hint:** Use k\_eff = d(k−1)+1 and L\_out = floor((L+p−k\_eff)/s)+1.

Show solution

Compute k\_eff:

keff=1⋅(5−1)+1=5k\_{eff} = 1·(5-1)+1 = 5keff​=1⋅(5−1)+1=5

Then:

Lout=⌊20+4−52⌋+1=⌊192⌋+1=9+1=10L\_{out} = \left\lfloor \frac{20 + 4 - 5}{2} \right\rfloor + 1 = \left\lfloor \frac{19}{2} \right\rfloor + 1 = 9 + 1 = 10Lout​=⌊220+4−5​⌋+1=⌊219​⌋+1=9+1=10

So L\_out = 10.

medium

2D shape + channels: You have an input tensor with shape (N=8, C\_in=3, H=32, W=32) in NCHW. You apply a Conv2d with C\_out=16, kernel 3×3, stride 1, dilation 1, padding 1. What is the output shape and how many weight parameters (ignore bias)?

**Hint:** Padding 1 with kernel 3 and stride 1 preserves H and W. Parameters are C\_out·C\_in·k\_h·k\_w.

Show solution

Spatial shape:

- •k\_eff=3, p\_h=2, p\_w=2, s=1

Hout=⌊32+2−31⌋+1=32H\_{out} = \left\lfloor \frac{32 + 2 - 3}{1} \right\rfloor + 1 = 32Hout​=⌊132+2−3​⌋+1=32

Similarly W\_out=32.

So output shape is (8, 16, 32, 32).

Parameter count:

16⋅3⋅3⋅3=43216 · 3 · 3 · 3 = 43216⋅3⋅3⋅3=432

So there are 432 weights (plus 16 biases if bias were included).

hard

Receptive field reasoning: In 1D, stack three conv layers with kernel sizes [3, 3, 3], strides [1, 2, 1], dilations all 1. Compute the receptive field size r₃ using the update rules j\_ℓ = j\_{ℓ−1}s\_ℓ and r\_ℓ = r\_{ℓ−1} + (k\_ℓ−1)j\_{ℓ−1}.

**Hint:** Start with r₀=1, j₀=1 and apply the updates layer by layer. Be careful: stride affects j first, but r uses j\_{ℓ−1}.

Show solution

Initialize:

- •r₀=1, j₀=1

Layer 1: k₁=3, s₁=1

j1=j0s1=1⋅1=1j\_1 = j\_0 s\_1 = 1·1 = 1j1​=j0​s1​=1⋅1=1

r1=r0+(3−1)j0=1+2⋅1=3r\_1 = r\_0 + (3-1)j\_0 = 1 + 2·1 = 3r1​=r0​+(3−1)j0​=1+2⋅1=3

Layer 2: k₂=3, s₂=2

j2=j1s2=1⋅2=2j\_2 = j\_1 s\_2 = 1·2 = 2j2​=j1​s2​=1⋅2=2

r2=r1+(3−1)j1=3+2⋅1=5r\_2 = r\_1 + (3-1)j\_1 = 3 + 2·1 = 5r2​=r1​+(3−1)j1​=3+2⋅1=5

Layer 3: k₃=3, s₃=1

j3=j2s3=2⋅1=2j\_3 = j\_2 s\_3 = 2·1 = 2j3​=j2​s3​=2⋅1=2

r3=r2+(3−1)j2=5+2⋅2=9r\_3 = r\_2 + (3-1)j\_2 = 5 + 2·2 = 9r3​=r2​+(3−1)j2​=5+2⋅2=9

So the final receptive field is 9 input positions wide.

## Connections

Unlocks and next steps:

- •[Deep Learning](/tech-tree/deep-learning/): Convolution is the core linear operator in CNNs; understanding shapes, padding, and receptive field is essential for designing deep architectures.

Related nodes you may want next (if available in your tree):

- •[Dot Product](/tech-tree/dot-product/)
- •[Tensors and Shapes](/tech-tree/tensors-and-shapes/)
- •[CNN Layers: Pooling and Stride](/tech-tree/cnn-pooling-stride/)
- •[Receptive Field](/tech-tree/receptive-field/)
- •[Backpropagation Through Convolutions](/tech-tree/conv-backprop/)

Quality: B (4.1/5)

[← back to tree](/tech-tree/)[browse all →](/tech-tree/inventory/)
