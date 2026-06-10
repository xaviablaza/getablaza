---
title: Sequence-to-Sequence Modeling
description: The paradigm of mapping input sequences to output sequences (e.g., translation or summarization), including encoder-decoder architectures and alignment concepts; attention mechanisms are often introduced to improve information flow between encoder and decoder. Familiarity with seq2seq setups clarifies why and how attention is applied.
date: '2026-07-01'
scheduled: '2026-12-02'
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
inspiration_url: https://templeton.host/tech-tree/sequence-to-sequence-modeling/
inspiration_category: tech-tree
---

> Source-copy draft imported from [https://templeton.host/tech-tree/sequence-to-sequence-modeling/](https://templeton.host/tech-tree/sequence-to-sequence-modeling/). Names, domain references, and local media paths were adapted for Xavi Ablaza / getablaza.com.

[←Back to Tech Tree](/tech-tree/)

[inventory](/tech-tree/inventory/)[coverage](/tech-tree/coverage/)

# Sequence-to-Sequence Modeling

Machine LearningDifficulty: ★★★★☆Depth: 1Unlocks: 2

The paradigm of mapping input sequences to output sequences (e.g., translation or summarization), including encoder-decoder architectures and alignment concepts; attention mechanisms are often introduced to improve information flow between encoder and decoder. Familiarity with seq2seq setups clarifies why and how attention is applied.

## Interactive Visualization

⏮◀◀▶▶STEP0.25x1xZOOM

t=0s

## Core Concepts

- -Seq2seq as conditional mapping: model P(y\_1..y\_T | x\_1..x\_S) with an encoder-decoder that encodes the input sequence and generates the output sequence autoregressively.
- -Attention/alignment: a per-output-step mechanism that produces a context by weighting encoder representations so the decoder can read input positions dynamically.

## Key Symbols & Notation

H = (h\_1,...,h\_S) : sequence of encoder hidden states (one vector per source position).alpha\_t = (alpha\_{t,1},...,alpha\_{t,S}) : attention weight vector at decoder step t (softmax-normalized).

## Essential Relationships

- -At each decode step t the decoder conditions on previous outputs and a context c\_t = sum\_s alpha\_{t,s} \* h\_s, where alpha\_t is computed by a softmax over compatibility scores between the decoder state and each h\_s, and uses c\_t (plus the decoder state) to produce the output distribution P(y\_t | y\_<t, x).

## Prerequisites (1)

[Softmax Function6 atoms](/tech-tree/softmax-function/)

## Unlocks (1)

[Attention Mechanismslvl 5](/tech-tree/attention-mechanisms/)

Advanced Learning Details

### Graph Position

11

Depth Cost

2

Fan-Out (ROI)

1

Bottleneck Score

1

Chain Length

### Cognitive Load

5

Atomic Elements

38

Total Elements

L2

Percentile Level

L3

Atomic Level

### All Concepts (16)

- - Sequence-to-sequence (seq2seq) paradigm: learning a mapping from a variable-length input sequence x1..xn to a variable-length output sequence y1..ym
- - Encoder: a model (often RNN/CNN/Transformer block) that processes the input sequence and emits a sequence of hidden representations
- - Decoder: an autoregressive model that produces output tokens one step at a time, conditioned on prior outputs and encoder information
- - Encoder–decoder architecture: the structured composition that connects an encoder and a decoder to implement seq2seq
- - Hidden state sequence: the ordered set of encoder vectors (h1, h2, ..., hn) representing input positions/contents
- - Fixed context vector (context bottleneck): the single-vector summary of the entire input produced by some enc–dec designs
- - Alignment: the conceptual notion of linking particular output positions to particular input positions (which input the decoder should 'focus' on when producing a given output)
- - Attention mechanism: a differentiable mechanism that computes dynamic, per-decoder-step focus over encoder hidden states (replaces or supplements a fixed context vector)
- - Attention score function: a parametric function that produces unnormalized compatibility scores between a decoder state and each encoder state
- - Attention weights (soft alignment): normalized, nonnegative weights over encoder positions (a probability distribution per decoder step) used to combine encoder states
- - Context vector from attention: a decoder-step-specific vector computed as the weighted sum of encoder hidden states using attention weights
- - Soft vs. hard alignment distinction: soft = differentiable weighted combination; hard = discrete choice of input position(s)
- - Global vs. local attention: attending over all encoder positions vs attending over a restricted window/subset
- - Autoregressive decoding: the decoder conditions on previously generated outputs (y<t) when producing y\_t
- - End-to-end training with attention: learning encoder, decoder, and attention parameters jointly by backpropagation (for soft attention)
- - Encoder-decoder coupling strategies: ways of initializing or passing encoder information into the decoder (e.g., initializing decoder state from encoder final state vs. using attention at every step)

### Teaching Strategy

Self-serve tutorial - low prerequisites, straightforward concepts.

Mini-scenario (we’ll keep using it):

You’re building a tiny English→French translator for a five-word sentence.

Source (English, length S=5):

1. 1)I
2. 2)eat
3. 3)green
4. 4)apples
5. 5)today

Target (French, length T=5):

1. 1)Je
2. 2)mange
3. 3)des
4. 4)pommes
5. 5)vertes

If you translate word-by-word, you’ll get stuck: in French, “green” (vertes) often comes after “apples” (pommes). So when the decoder is producing the last word “vertes”, it must “look back” to the English word “green” at position 3—even though it already produced “pommes” at position 4.

This lesson is about the modeling paradigm that makes that possible: sequence-to-sequence (seq2seq) modeling. We’ll build up from the probability objective P(y₁..y\_T | x₁..x\_S), then see why plain encoder→decoder has an information bottleneck, and how alignment/attention uses αₜ to let the decoder read from the encoder states H=(h₁,…,h\_S) at every output step.

Quick schematic (we’ll refer back to it):

x₁ x₂ x₃ x₄ x₅

v v v v v

[h₁][h₂][h₃][h₄][h₅] = H (encoder states)

\ | /

\ | /

αₜ (softmax over 1..S)

v

cₜ (context)

v

decoder state sₜ → yₜ

TL;DR:

Seq2seq models learn a conditional distribution over output sequences given an input sequence: P(y₁..y\_T | x₁..x\_S). An encoder maps the source tokens to hidden states H=(h₁,…,h\_S). A decoder generates tokens autoregressively, using previously generated tokens and (optionally) a context vector. Attention/alignment computes a per-step weight vector αₜ over encoder positions, forming a context cₜ=∑ᵢ αₜ,ᵢ hᵢ so the decoder can dynamically “read” the right parts of the input while generating each output token.

## What Is Sequence-to-Sequence (Seq2seq) Modeling?

### Why this paradigm exists

Many real problems are not “predict a single label” but “produce a whole sequence whose length may differ from the input.” Examples:

- •Machine translation: English sentence → French sentence
- •Summarization: article → short summary
- •Speech recognition: audio frames → text tokens
- •Code generation: docstring → function

The defining feature is **variable-length in, variable-length out**, and output tokens depend on each other.

In our running example:

- •Source sequence **x** has length S=5S=5S=5 (English tokens)
- •Target sequence **y** has length T=5T=5T=5 (French tokens)

The goal is to model the conditional probability of the entire output sequence given the input sequence:

P(y1,…,yT∣x1,…,xS).P(y\_1,\ldots,y\_T \mid x\_1,\ldots,x\_S).P(y1​,…,yT​∣x1​,…,xS​).

### Autoregressive factorization (the key probabilistic move)

We don’t predict the whole sequence at once. We factorize it using the chain rule:

P(y1,…,yT∣x1:S)=∏t=1TP(yt∣y<t,x1:S).P(y\_1,\ldots,y\_T \mid x\_{1:S}) = \prod\_{t=1}^{T} P(y\_t \mid y\_{<t}, x\_{1:S}).P(y1​,…,yT​∣x1:S​)=t=1∏T​P(yt​∣y<t​,x1:S​).

Here y<ty\_{<t}y<t​ means (y1,…,yt−1)(y\_1,\ldots,y\_{t-1})(y1​,…,yt−1​).

This single equation captures the **seq2seq contract**:

- •At step ttt, the model has seen the entire input x1:Sx\_{1:S}x1:S​.
- •It also conditions on the outputs it already produced.
- •It outputs a distribution over the next token yty\_tyt​.

### Encoder–decoder: turning the contract into an architecture

To implement this, we split responsibilities:

1. 1)**Encoder** reads the input sequence and produces internal representations.
2. 2)**Decoder** generates the output sequence one token at a time.

Historically, the encoder and decoder were RNNs (LSTM/GRU). Today, they are often Transformers—but the encoder/decoder *roles* persist.

A classic mental model:

- •The encoder produces a “memory” of the source.
- •The decoder is a “writer” that consults that memory to decide what to write next.

### The bottleneck that motivates attention

Early seq2seq used a single vector (often the final encoder hidden state) as a summary of the entire source. This works for very short sentences but degrades on longer ones: the decoder must squeeze everything about x1:Sx\_{1:S}x1:S​ through a fixed-size bottleneck.

Our five-word example is short, but it already hints at a deeper need: when the decoder generates “vertes” (green), it should access information from source position 3. If all information is compressed into a single vector, the decoder has to remember precise token-level details across steps.

This is why alignment/attention matters: it provides a **direct path** from each output step back to the relevant encoder states.

### What you should be able to say after this section

- •Seq2seq is about P(y∣x)P(\mathbf{y} \mid \mathbf{x})P(y∣x) where both sides are sequences.
- •Decoding is autoregressive: predict yty\_tyt​ given y<ty\_{<t}y<t​ and the input.
- •Encoder–decoder splits the job into reading and writing.
- •A single-vector summary can be an information bottleneck, motivating attention.

## Core Mechanic 1: Encoder–Decoder Modeling (Without Attention)

### Why understand the no-attention version first?

Attention can feel like “extra machinery.” But it’s easier to appreciate once you’ve seen what the encoder–decoder is trying to do on its own—and where it struggles.

We’ll describe a standard formulation using hidden states and probability distributions. Even if you later use a Transformer, the ideas map cleanly:

- •Encoder produces a sequence of representations (or a final summary).
- •Decoder maintains a state and emits tokens via softmax.

### Step 1: Represent tokens as vectors

Tokens are discrete symbols. Models convert them into continuous vectors.

- •Input embedding for token xix\_ixi​: **e**(xᵢ) ∈ ℝᵈ
- •Output embedding for token yt−1y\_{t-1}yt−1​ (previous token): **e**(y\_{t-1})

### Step 2: Encoder produces hidden states

Let the encoder produce hidden states **h**ᵢ (one per source position):

- •H=(h1,…,hS)H = (h\_1,\ldots,h\_S)H=(h1​,…,hS​) where each hi∈Rdhh\_i \in \mathbb{R}^{d\_h}hi​∈Rdh​

In an RNN encoder, a typical recurrence is:

hi=fenc(hi−1,e(xi)).h\_i = f\_{enc}(h\_{i-1}, e(x\_i)).hi​=fenc​(hi−1​,e(xi​)).

Intuition:

- •hih\_ihi​ is a contextual representation of the prefix x1:ix\_{1:i}x1:i​.
- •In a bidirectional encoder, hih\_ihi​ can represent both left and right context.

Even in a Transformer encoder, you still end up with one vector per token position; you can still call them hih\_ihi​.

### Step 3: The simplest bottleneck: a single context vector

A classic early approach defines a single vector **c** summarizing the source, for example the last hidden state:

c=hS.c = h\_S.c=hS​.

(There are other choices: pooling over HHH, or concatenating last states of a bidirectional RNN. But the core idea is “fixed-size summary.”)

### Step 4: Decoder state and token generation

The decoder maintains a hidden state **s**ₜ and emits a distribution over the next token:

1) Update decoder state:

st=fdec(st−1,e(yt−1),c).s\_t = f\_{dec}(s\_{t-1}, e(y\_{t-1}), c).st​=fdec​(st−1​,e(yt−1​),c).

2) Produce logits and probabilities:

ot=Wost+boo\_t = W\_o s\_t + b\_oot​=Wo​st​+bo​

P(yt∣y<t,x1:S)=softmax(ot).P(y\_t \mid y\_{<t}, x\_{1:S}) = \text{softmax}(o\_t).P(yt​∣y<t​,x1:S​)=softmax(ot​).

The softmax is your prerequisite: it turns logits into a probability distribution over the vocabulary.

### Training objective: teacher forcing + cross-entropy

During training, we usually feed the *true* previous token rather than the model’s sampled token (teacher forcing). The loss is negative log-likelihood:

L=−∑t=1Tlog⁡P(yt\\*∣y<t\\*,x1:S).\mathcal{L} = -\sum\_{t=1}^{T} \log P(y\_t^{\\*} \mid y\_{<t}^{\\*}, x\_{1:S}).L=−t=1∑T​logP(yt\\*​∣y<t\\*​,x1:S​).

Where yt\\*y\_t^{\\*}yt\\*​ is the ground-truth token.

### Inference: start/end tokens and decoding strategies

At inference time:

- •Start with a special token: y0=⟨BOS⟩y\_0 = \langle BOS \rangley0​=⟨BOS⟩
- •Repeatedly sample/choose tokens until ⟨EOS⟩\langle EOS \rangle⟨EOS⟩ or a max length.

Decoding choices:

| Strategy | How it chooses yty\_tyt​ | Pros | Cons |
| --- | --- | --- | --- |
| Greedy | arg⁡max⁡\arg\maxargmax over softmax | Fast | Can miss better global sequences |
| Beam search | Keep top-K partial sequences | Better translations often | Slower; can prefer generic outputs |
| Sampling | Sample from distribution | Diverse outputs | Can be unstable without controls |

### Why the bottleneck is a real problem

If ccc is fixed, then every output token must be generated from the same compressed summary.

Imagine generating “vertes” at the end. The decoder must:

- •Remember that “green” occurred in the input.
- •Remember that it modifies “apples” and thus should agree in gender/number.
- •Place it at the correct point in the output.

With a single ccc, the model can learn this sometimes, but it scales poorly with longer sequences and complex reorderings.

### A “breathing room” intuition

Think of the encoder summary vector ccc as trying to be a whole paragraph’s worth of meaning squeezed into one sticky note.

You *can* write a good sticky note.

But if the decoder could instead flip through the original paragraph whenever needed, it would make fewer mistakes.

That “flipping through” is exactly what attention adds.

### What you should be able to do after this section

- •Write the factorization ∏tP(yt∣y<t,x)\prod\_t P(y\_t \mid y\_{<t}, x)∏t​P(yt​∣y<t​,x).
- •Describe how an encoder produces hidden states and (optionally) a single context vector.
- •Explain training with teacher forcing and cross-entropy.
- •Articulate the fixed-size bottleneck problem as the main motivation for attention.

## Core Mechanic 2: Attention/Alignment (Dynamic Reading with αₜ and H)

### Why attention: the decoder needs *target-step-specific* context

When producing yty\_tyt​, the decoder doesn’t need the entire source equally.

- •To generate “Je”, focus on “I”.
- •To generate “mange”, focus on “eat”.
- •To generate “pommes”, focus on “apples”.
- •To generate “vertes”, focus back on “green”.

So instead of a single fixed ccc, we want a **different context vector $c\_t$ at each decoding step**.

### The objects (anchored to the node’s symbols)

You are given:

- •Encoder states: H=(h1,…,hS)H=(h\_1,\ldots,h\_S)H=(h1​,…,hS​), one vector per source position.
- •Attention weights at step ttt: αt=(αt,1,…,αt,S)\alpha\_t = (\alpha\_{t,1},\ldots,\alpha\_{t,S})αt​=(αt,1​,…,αt,S​).

Constraints:

- •αt,i≥0\alpha\_{t,i} \ge 0αt,i​≥0
- •∑i=1Sαt,i=1\sum\_{i=1}^{S} \alpha\_{t,i} = 1∑i=1S​αt,i​=1 (because it’s softmax-normalized)

Interpretation:

- •αt,i\alpha\_{t,i}αt,i​ is “how much the decoder at time ttt attends to source position iii.”

### Step 1: Compute attention scores (alignment scores)

We first compute an unnormalized score for each source position iii.

A common pattern:

et,i=score(st−1,hi).e\_{t,i} = \text{score}(s\_{t-1}, h\_i).et,i​=score(st−1​,hi​).

Where:

- •st−1s\_{t-1}st−1​ is the decoder’s previous hidden state (a summary of what has been generated so far).
- •hih\_ihi​ is the encoder representation of source token xix\_ixi​.

Typical scoring functions (you’ll see these in literature):

| Name | Score function | Notes |
| --- | --- | --- |
| Dot product | et,i=st−1⊤hie\_{t,i} = s\_{t-1}^\top h\_iet,i​=st−1⊤​hi​ | Simple; requires same dimension |
| General | et,i=st−1⊤Whie\_{t,i} = s\_{t-1}^\top W h\_iet,i​=st−1⊤​Whi​ | Learnable linear map |
| Additive (Bahdanau) | et,i=v⊤tanh⁡(Wsst−1+Whhi)e\_{t,i} = v^\top \tanh(W\_s s\_{t-1} + W\_h h\_i)et,i​=v⊤tanh(Ws​st−1​+Wh​hi​) | Works well with different dims |

You don’t need to memorize them all right now—the pattern is what matters: **compare the decoder’s needs to each encoder state**.

### Step 2: Softmax into attention weights αₜ

Convert scores into a distribution over positions:

αt,i=exp⁡(et,i)∑j=1Sexp⁡(et,j).\alpha\_{t,i} = \frac{\exp(e\_{t,i})}{\sum\_{j=1}^{S} \exp(e\_{t,j})}.αt,i​=∑j=1S​exp(et,j​)exp(et,i​)​.

This is exactly where your softmax prerequisite shows up.

Numerical stability reminder (important in real implementations):

αt,i=exp⁡(et,i−m)∑jexp⁡(et,j−m),m=max⁡jet,j.\alpha\_{t,i} = \frac{\exp(e\_{t,i} - m)}{\sum\_{j} \exp(e\_{t,j}-m)},\quad m=\max\_j e\_{t,j}.αt,i​=∑j​exp(et,j​−m)exp(et,i​−m)​,m=jmax​et,j​.

### Step 3: Build the context vector cₜ as a weighted sum of encoder states

Now we compute:

ct=∑i=1Sαt,i hi.c\_t = \sum\_{i=1}^{S} \alpha\_{t,i} \, h\_i.ct​=i=1∑S​αt,i​hi​.

Interpretation:

- •ctc\_tct​ lives in the same vector space as hih\_ihi​.
- •If αt,3\alpha\_{t,3}αt,3​ is large, ctc\_tct​ is pulled toward h3h\_3h3​.

This makes attention feel like a **soft pointer** into the source.

### Step 4: Use cₜ to update the decoder and produce yₜ

A common formulation:

st=fdec(st−1,e(yt−1),ct).s\_t = f\_{dec}(s\_{t-1}, e(y\_{t-1}), c\_t).st​=fdec​(st−1​,e(yt−1​),ct​).

Then output distribution:

P(yt∣y<t,x1:S)=softmax(Wost+bo).P(y\_t \mid y\_{<t}, x\_{1:S}) = \text{softmax}(W\_o s\_t + b\_o).P(yt​∣y<t​,x1:S​)=softmax(Wo​st​+bo​).

Sometimes the context is also fed directly into the output layer, e.g. concatenate [st;ct][s\_t; c\_t][st​;ct​].

### Anchoring back to our 5-word example: what αₜ should look like

Let’s label source positions:

1:I, 2:eat, 3:green, 4:apples, 5:today

A plausible alignment pattern:

- •When y1=Jey\_1=\text{Je}y1​=Je, attention peaks on source 1.
- •When y2=mangey\_2=\text{mange}y2​=mange, attention peaks on source 2.
- •When y4=pommesy\_4=\text{pommes}y4​=pommes, attention peaks on source 4.
- •When y5=vertesy\_5=\text{vertes}y5​=vertes, attention peaks on source 3.

So α5\alpha\_5α5​ might heavily weight position 3.

### Inline “alignment table” diagram

Below is a rough alignment matrix (rows are target steps t, columns are source positions i). Darker means larger α.

| t / i | 1 (I) | 2 (eat) | 3 (green) | 4 (apples) | 5 (today) |
| --- | --- | --- | --- | --- | --- |
| 1 (Je) | ████ | ░ | ░ | ░ | ░ |
| 2 (mange) | ░ | ████ | ░ | ░ | ░ |
| 3 (des) | ░ | ░ | ░ | ███ | ░ |
| 4 (pommes) | ░ | ░ | ░ | ████ | ░ |
| 5 (vertes) | ░ | ░ | ████ | ░ | ░ |

This is the *alignment concept*: for each output step, the model forms a distribution over input positions.

### Why attention improves information flow (conceptually)

Without attention, the only path from input token xix\_ixi​ to output decision at time ttt is:

xi→x\_i \toxi​→ encoder computations →\to→ single summary c→c \toc→ decoder state st→yts\_t \to y\_tst​→yt​

With attention:

xi→hi→ct→st→ytx\_i \to h\_i \to c\_t \to s\_t \to y\_txi​→hi​→ct​→st​→yt​

Now each output step has a direct, learnable channel to **any** encoder state.

### A careful note: attention weights are not always “true explanations”

It’s tempting to say “αₜ tells you exactly which input word caused the output.” Often it correlates with alignment, but:

- •The decoder state st−1s\_{t-1}st−1​ also carries information.
- •Multiple layers and nonlinearities can mix information.

So treat attention as:

- •A useful *alignment-like* mechanism
- •Sometimes an interpretability aid
- •Not a perfect causal explanation by default

### What you should be able to do after this section

- •Define H=(h1,…,hS)H=(h\_1,\ldots,h\_S)H=(h1​,…,hS​) and αt\alpha\_tαt​.
- •Write αt,i=softmax(et,i)\alpha\_{t,i}=\text{softmax}(e\_{t,i})αt,i​=softmax(et,i​) and ct=∑iαt,ihic\_t=\sum\_i \alpha\_{t,i}h\_ict​=∑i​αt,i​hi​.
- •Explain attention as a per-output-step soft selection over source positions.
- •Connect attention back to reorderings like placing “vertes” after “pommes”.

## Application/Connection: How Seq2seq + Attention Shows Up in Practice (and Why It Unlocks Cross-Attention)

### From “alignment” to modern architectures

The attention we described is often called **encoder–decoder attention** or **cross-attention**:

- •Queries come from the decoder state (what we need now)
- •Keys/values come from encoder states HHH (what the source contains)

Even if you haven’t learned Transformer math yet, the conceptual mapping is straightforward:

- •Our score function score(st−1,hi)\text{score}(s\_{t-1}, h\_i)score(st−1​,hi​) becomes “query–key compatibility.”
- •Our weighted sum ct=∑iαt,ihic\_t=\sum\_i \alpha\_{t,i}h\_ict​=∑i​αt,i​hi​ becomes “weighted sum of values.”

This is exactly why understanding seq2seq clarifies attention: it tells you *what problem attention is solving*.

### Real tasks and what changes

Seq2seq setups vary mainly in:

1) What counts as the “sequence” on the input side

2) What output vocabulary/tokenization looks like

3) How decoding is constrained

Examples:

| Task | Input sequence x | Output sequence y | Special concerns |
| --- | --- | --- | --- |
| Translation | tokens | tokens | reordering, morphology |
| Summarization | long tokens | shorter tokens | content selection, hallucination |
| Speech recognition | audio frames | tokens | long inputs, monotonic alignment |
| Image captioning | region features | tokens | attention over image regions |

The encoder can be anything that outputs a sequence of vectors HHH:

- •RNN/Transformer over tokens
- •CNN/ViT over image patches
- •Acoustic model over spectrogram frames

As long as you have HHH, the decoder can attend over it.

### Decoding details that matter in applications

Even with a good model, the way you decode changes behavior:

- •**Beam search** often improves translation quality, but can produce bland outputs.
- •**Length normalization** is common because log-probabilities favor short sequences.

A typical beam objective may look like:

arg⁡max⁡y1∣y∣γ∑t=1∣y∣log⁡P(yt∣y<t,x)\arg\max\_{y} \frac{1}{|y|^\gamma} \sum\_{t=1}^{|y|} \log P(y\_t \mid y\_{<t}, x)argymax​∣y∣γ1​t=1∑∣y∣​logP(yt​∣y<t​,x)

where γ\gammaγ controls length penalty.

### Exposure bias (a practical training vs inference gap)

Training uses teacher forcing: decoder sees true yt−1\\*y\_{t-1}^{\\*}yt−1\\*​.

Inference uses its own previous prediction y^t−1\hat{y}\_{t-1}y^​t−1​.

So the model may drift if it makes an early mistake. This issue is called **exposure bias**.

Mitigations you may hear about:

- •Scheduled sampling
- •Sequence-level training objectives (e.g., policy gradient)
- •Stronger models + better decoding

You don’t need to solve exposure bias now, but you should recognize it as a recurring theme in seq2seq.

### Why attention is a stepping stone to Transformers

In Transformers:

- •The encoder uses **self-attention** to build HHH.
- •The decoder uses **masked self-attention** to model P(yt∣y<t)P(y\_t \mid y\_{<t})P(yt​∣y<t​).
- •The decoder uses **cross-attention** to incorporate the source (our αt\alpha\_tαt​ idea).

So the conceptual flow becomes:

1) Encode source into HHH

2) For each decoding step t, compute attention distribution αt\alpha\_tαt​ over HHH

3) Use the resulting context to predict yty\_tyt​

If you understand that, the jump to “multi-head attention” is mostly an engineering/generalization step: do it several times in parallel with different learned projections.

### Returning one last time to the mini-scenario

Our translator succeeded not because it memorized the entire input in one vector, but because at each step it can ask:

- •“What part of the source is relevant *right now*?”

When producing “vertes”, it can attend back to “green” even though that occurred earlier and has already influenced other outputs.

That dynamic reading behavior is the essence of seq2seq alignment.

### What you should be able to do after this section

- •Recognize encoder–decoder attention as cross-attention.
- •Name common seq2seq applications and what differs.
- •Explain exposure bias and why decoding strategy matters.
- •See how this node unlocks the more general [Attention Mechanisms](/tech-tree/attention-mechanisms/) node.

## Worked Examples (3)

### Compute one attention step (αₜ and cₜ) from given scores and encoder states

Suppose the encoder produced S=5 hidden states h₁..h₅ (each 2D for simplicity):

h₁ = [1, 0]

h₂ = [0, 1]

h₃ = [1, 1]

h₄ = [2, 0]

h₅ = [0, 2]

At decoder step t=5 (trying to produce “vertes”), assume the alignment scores (unnormalized) are:

e₅ = [e₅,₁..e₅,₅] = [-1, 0, 2, 0, -2].

Compute α₅ via softmax and then compute the context vector c₅ = ∑ᵢ α₅,ᵢ hᵢ.

1. Compute stabilized softmax.

   Let m = max(e₅) = 2.

   Compute shifted scores:

   e' = e₅ - m = [-3, -2, 0, -2, -4].
2. Exponentiate the shifted scores:

   exp(e') = [exp(-3), exp(-2), exp(0), exp(-2), exp(-4)].

   Numerically (approx):

   exp(-3)≈0.0498

   exp(-2)≈0.1353

   exp(0)=1

   exp(-4)≈0.0183

   So:

   exp(e') ≈ [0.0498, 0.1353, 1, 0.1353, 0.0183].
3. Normalize to get α₅.

   Sum Z = 0.0498 + 0.1353 + 1 + 0.1353 + 0.0183 = 1.3387 (approx).

   Therefore:

   α₅,₁ ≈ 0.0498 / 1.3387 = 0.0372

   α₅,₂ ≈ 0.1353 / 1.3387 = 0.1011

   α₅,₃ ≈ 1 / 1.3387 = 0.7470

   α₅,₄ ≈ 0.1353 / 1.3387 = 0.1011

   α₅,₅ ≈ 0.0183 / 1.3387 = 0.0137

   Check: they sum to ~1.0001 (rounding error).
4. Compute context c₅ = ∑ᵢ α₅,ᵢ hᵢ.

   Write it out:

   c₅ = α₅,₁ h₁ + α₅,₂ h₂ + α₅,₃ h₃ + α₅,₄ h₄ + α₅,₅ h₅

   = 0.0372[1,0] + 0.1011[0,1] + 0.7470[1,1] + 0.1011[2,0] + 0.0137[0,2].
5. Add component-wise.

   x-component:

   = 0.0372(1) + 0.1011(0) + 0.7470(1) + 0.1011(2) + 0.0137(0)

   = 0.0372 + 0 + 0.7470 + 0.2022 + 0

   = 0.9864.

   y-component:

   = 0.0372(0) + 0.1011(1) + 0.7470(1) + 0.1011(0) + 0.0137(2)

   = 0 + 0.1011 + 0.7470 + 0 + 0.0274

   = 0.8755.

   So c₅ ≈ [0.986, 0.876].

**Insight:** Because e₅,₃ is much larger than the rest, α₅ puts ~75% of its mass on source position 3. The context vector c₅ becomes close to h₃ (with smaller contributions from other positions). This is the “soft pointer” idea in numbers: attention is a learned weighted average over encoder states.

### From seq2seq probability to training loss (a concrete negative log-likelihood calculation)

Assume a tiny vocabulary of 4 tokens for the decoder: {Je, mange, pommes, vertes}. For one training example, the target sequence is y = [Je, mange].

Suppose the model outputs these probabilities:

At t=1 (predicting y₁):

P(y₁=Je | x) = 0.70

At t=2 (predicting y₂ with teacher forcing on y₁=Je):

P(y₂=mange | y₁=Je, x) = 0.20

Compute the negative log-likelihood loss for this example (natural log).

1. Write the seq2seq factorization for this short target:

   P(y₁,y₂ | x) = P(y₁|x) · P(y₂|y₁,x).
2. Plug in the given probabilities:

   P(y|x) = 0.70 · 0.20 = 0.14.
3. Negative log-likelihood (NLL) is:

   L = -log P(y|x) = -log(0.14).
4. Compute using log rules:

   -log(0.14) = -(log(14) - log(100))

   = log(100) - log(14).

   Numerically:

   log(100)=4.6052

   log(14)=2.6391

   So L ≈ 4.6052 - 2.6391 = 1.9661.
5. Equivalently, sum token-level losses:

   L = -log 0.70 + -log 0.20

   ≈ 0.3567 + 1.6094

   = 1.9661.

**Insight:** Training loss decomposes across time steps: you can see exactly which step is hurting you. Here, the second token is much less probable (0.20), dominating the loss. This per-step view is also how gradients flow back through the decoder and (with attention) into the encoder states that were used to build cₜ.

### Why fixed-size context can fail: a toy “compression” argument with two different sources

Consider two different English inputs that share the same last word:

A: [I, eat, green, apples, today]

B: [I, eat, red, apples, today]

Suppose a no-attention encoder summarizes the entire source as c = h\_S (the final state). The decoder must produce the correct last French adjective: vertes (green) vs rouges (red).

Explain, at a mechanistic level, why relying only on c makes this harder than using attention over H=(h₁..h₅).

1. In the no-attention setup, every decision y\_t depends on the same fixed context c.

   Formally, s\_t = f\_dec(s\_{t-1}, e(y\_{t-1}), c).
2. The difference between inputs A and B occurs at position 3 (green vs red).

   But by the time the encoder reaches position 5, the final state h\_S must contain:

   - •the subject and verb information (I/eat)
   - •the object (apples)
   - •the time adverb (today)
   - •and the color attribute (green vs red)

   all in one vector of fixed dimension d\_h.
3. During decoding, when generating the final adjective (vertes/rouges), the model must extract from c the specific attribute that was present at input position 3, potentially many steps earlier in the encoder computation.
4. With attention, the decoder at the adjective step can compute αₜ that peaks at i=3.

   Then c\_t = ∑ᵢ αₜ,ᵢ hᵢ is dominated by h₃, which is directly tied to the color token’s representation.
5. So the decision boundary between “vertes” and “rouges” can depend more directly on h₃ rather than on whatever compressed trace of “green vs red” survived into h\_S.

**Insight:** Attention reduces the need for perfect long-range compression. Instead of hoping the final encoder state retains every detail, the decoder can retrieve the relevant detail from the specific encoder state where it was encoded. This is especially important when the decisive information is not near the end of the source, or when the output needs to revisit earlier source tokens later in decoding.

## Key Takeaways

- ✓

  Seq2seq models learn conditional sequence distributions: P(y1:T∣x1:S)P(y\_{1:T} \mid x\_{1:S})P(y1:T​∣x1:S​).
- ✓

  Autoregressive decoding uses the chain rule: P(y1:T∣x)=∏tP(yt∣y<t,x)P(y\_{1:T}|x)=\prod\_t P(y\_t|y\_{<t},x)P(y1:T​∣x)=∏t​P(yt​∣y<t​,x).
- ✓

  An encoder produces token-level representations H=(h1,…,hS)H=(h\_1,\ldots,h\_S)H=(h1​,…,hS​); a decoder generates outputs step-by-step using a hidden state sts\_tst​.
- ✓

  A fixed-size encoder summary vector creates an information bottleneck, especially for long inputs and reordering.
- ✓

  Attention/alignment computes scores et,ie\_{t,i}et,i​, softmaxes them into αt,i\alpha\_{t,i}αt,i​, and forms a context ct=∑iαt,ihic\_t=\sum\_i \alpha\_{t,i}h\_ict​=∑i​αt,i​hi​.
- ✓

  The attention vector αt\alpha\_tαt​ is a distribution over source positions and can be read as a soft alignment for each output step.
- ✓

  Training typically uses teacher forcing with cross-entropy loss; inference uses greedy/beam/sampling and can suffer from exposure bias.
- ✓

  Encoder–decoder attention is conceptually the same idea as cross-attention in Transformers, which is why this node unlocks modern attention mechanisms.

## Common Mistakes

- ✗

  Forgetting the conditional structure and writing P(y1:T)P(y\_{1:T})P(y1:T​) instead of P(y1:T∣x1:S)P(y\_{1:T}|x\_{1:S})P(y1:T​∣x1:S​) when describing translation/summarization.
- ✗

  Mixing up attention scores et,ie\_{t,i}et,i​ (unnormalized) with attention weights αt,i\alpha\_{t,i}αt,i​ (softmax-normalized and summing to 1).
- ✗

  Treating attention weights as guaranteed causal explanations for model outputs; they are often alignment-like but not definitive explanations.
- ✗

  Ignoring the training–inference mismatch: teacher forcing during training does not reflect autoregressive generation at inference, leading to exposure bias.

## Practice

easy

You have S=3 encoder states h₁,h₂,h₃ (vectors). At some decoder step t, the attention scores are eₜ = [0, 0, 0]. What are the attention weights αₜ? What is cₜ in terms of h₁,h₂,h₃?

**Hint:** Softmax of equal numbers is uniform. Then cₜ is the average of the vectors.

Show solution

If eₜ = [0,0,0], then softmax gives αₜ = [1/3, 1/3, 1/3].

So:

ct=∑i=13αt,ihi=13h1+13h2+13h3.c\_t = \sum\_{i=1}^{3} \alpha\_{t,i} h\_i = \tfrac{1}{3}h\_1 + \tfrac{1}{3}h\_2 + \tfrac{1}{3}h\_3.ct​=i=1∑3​αt,i​hi​=31​h1​+31​h2​+31​h3​.

This is the simple mean of the encoder states.

medium

Show the chain-rule factorization for P(y₁,y₂,y₃ | x₁..x\_S). Then write the negative log-likelihood loss for a single training pair (x, y) using teacher forcing.

**Hint:** Use ∏ over t for the probability and ∑ over t for the loss; each term conditions on y\_<t and x.

Show solution

Factorization:

P(y1,y2,y3∣x1:S)=P(y1∣x1:S) P(y2∣y1,x1:S) P(y3∣y1:2,x1:S).P(y\_1,y\_2,y\_3 \mid x\_{1:S}) = P(y\_1 \mid x\_{1:S})\,P(y\_2 \mid y\_1, x\_{1:S})\,P(y\_3 \mid y\_{1:2}, x\_{1:S}).P(y1​,y2​,y3​∣x1:S​)=P(y1​∣x1:S​)P(y2​∣y1​,x1:S​)P(y3​∣y1:2​,x1:S​).

Teacher-forcing NLL loss for one pair (x,y) of length T=3:

L=−∑t=13log⁡P(yt\\*∣y<t\\*,x1:S).\mathcal{L} = -\sum\_{t=1}^{3} \log P(y\_t^{\\*} \mid y\_{<t}^{\\*}, x\_{1:S}).L=−t=1∑3​logP(yt\\*​∣y<t\\*​,x1:S​).

medium

At decoder step t, you have attention weights αₜ = [0.1, 0.2, 0.7] over three encoder states h₁=[1,0], h₂=[0,1], h₃=[2,2]. Compute cₜ.

**Hint:** Compute cₜ = 0.1h₁ + 0.2h₂ + 0.7h₃ component-wise.

Show solution

Compute the weighted sum:

cₜ = 0.1[1,0] + 0.2[0,1] + 0.7[2,2]

First component:

= 0.1·1 + 0.2·0 + 0.7·2 = 0.1 + 0 + 1.4 = 1.5

Second component:

= 0.1·0 + 0.2·1 + 0.7·2 = 0 + 0.2 + 1.4 = 1.6

So cₜ = [1.5, 1.6].

## Connections

Unlocks and next steps:

- •[Attention Mechanisms](/tech-tree/attention-mechanisms/) — generalizes the alignment idea into cross-attention and self-attention (including multi-head attention).

Related conceptual neighbors you may want in a tech tree:

- •Autoregressive language modeling (decoder-only view of ∏tP(yt∣y<t)\prod\_t P(y\_t|y\_{<t})∏t​P(yt​∣y<t​))
- •Beam search and decoding heuristics
- •RNNs/LSTMs vs Transformer encoder–decoder architectures
- •Tokenization (BPE/WordPiece) and how it changes “alignment” granularity

Quality: A (4.4/5)

[← back to tree](/tech-tree/)[browse all →](/tech-tree/inventory/)
