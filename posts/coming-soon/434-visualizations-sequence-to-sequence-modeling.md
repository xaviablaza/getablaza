---
title: sequence-to-sequence-modeling
description: Visualizes an encoder-decoder seq2seq model where the encoder produces hidden states H=(h1..hS). At each decoder step t (cycling automatically), attention weights α_t are computed over source positions, forming a context vector c_t=Σ_s α_{t,s} h_s. The active decoder box uses c_t (and prior outputs) to shape an illustrated output distribution P(y_t | y_<t, x).
date: '2026-07-01'
scheduled: '2026-06-10'
tags:
- p-and-l-engineering
- coming-soon
- visualizations
layout: layouts/post.njk
templateEngineOverride: md
image: /img/xavi-linkedin-profile.jpg
draft: false
generated_by: templeton-deep-copy-import
source_format: html
inspiration_url: https://templeton.host/visualizations/sequence-to-sequence-modeling/
inspiration_category: visualizations
---

> Source-copy draft imported from [https://templeton.host/visualizations/sequence-to-sequence-modeling/](https://templeton.host/visualizations/sequence-to-sequence-modeling/). Names, domain references, and local media paths were adapted for Xavi Ablaza / getablaza.com.

[← ~/visualizations](/visualizations/)

# sequence-to-sequence-modeling

Visualizes an encoder-decoder seq2seq model where the encoder produces hidden states H=(h1..hS). At each decoder step t (cycling automatically), attention weights α\_t are computed over source positions, forming a context vector c\_t=Σ\_s α\_{t,s} h\_s. The active decoder box uses c\_t (and prior outputs) to shape an illustrated output distribution P(y\_t | y\_<t, x).

canvasclick to interact

⏮◀◀▶▶STEP0.25x1xZOOM

t=0s

## practical uses

- 01.Machine translation (source sentence → target sentence)
- 02.Abstractive summarization (document → summary)
- 03.Speech-to-text / transcription (audio frames → tokens)

## technical notes

Time-cycled decode steps (3.6s loop). Attention weights are generated from a drifting peak and normalized via softmax, then rendered as weighted connections + a bar chart. Context magnitude is shown as a context bar and modulates a small output-probability panel. Uses snapped pixel grid, green-on-black palette, and only Canvas 2D API.

[← common-distributions](/visualizations/common-distributions/)[logistic-regression →](/visualizations/logistic-regression/)
