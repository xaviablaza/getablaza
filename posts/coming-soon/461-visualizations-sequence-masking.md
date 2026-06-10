---
title: sequence-masking-(causal-and-padding-masks)
description: Visualizes the attention mask matrix M (1=allow, 0=block) and how causal masking (upper-triangular blocking of future tokens) and padding masking (blocking PAD key positions) combine. The animation cycles between mask types, then demonstrates integration into attention by adding a large negative value to masked logits so softmax assigns ~0 probability to blocked keys for the active query row.
date: '2026-07-01'
scheduled: '2027-10-04'
tags:
- p-and-l-engineering
- coming-soon
- visualizations
layout: layouts/post.njk
templateEngineOverride: md
image: /img/xavi-linkedin-profile.jpg
draft: true
generated_by: templeton-deep-copy-import
source_format: html
inspiration_url: https://templeton.host/visualizations/sequence-masking/
inspiration_category: visualizations
---

> Source-copy draft imported from [https://templeton.host/visualizations/sequence-masking/](https://templeton.host/visualizations/sequence-masking/). Names, domain references, and local media paths were adapted for Xavi Ablaza / getablaza.com.

[← ~/visualizations](/visualizations/)

# sequence-masking-(causal-and-padding-masks)

Visualizes the attention mask matrix M (1=allow, 0=block) and how causal masking (upper-triangular blocking of future tokens) and padding masking (blocking PAD key positions) combine. The animation cycles between mask types, then demonstrates integration into attention by adding a large negative value to masked logits so softmax assigns ~0 probability to blocked keys for the active query row.

canvasclick to interact

⏮◀◀▶▶STEP0.25x1xZOOM

t=0s

## practical uses

- 01.Autoregressive decoding: prevent attention to future tokens via causal masking
- 02.Training with padded batches: prevent padded key positions from receiving attention via padding masks
- 03.Debugging Transformer implementations: verify mask construction and that masked logits yield near-zero softmax weights

## technical notes

Grid-snapped, green-on-black rendering. Left panel draws M as a blocky Q×K matrix with an animated active query row. Right panel synthesizes logits, applies a combined (causal AND padding) mask using a finite -8 stand-in for -INF, then computes a stable softmax to show probabilities collapsing to ~0 on masked keys. Animation cycles every ~4.2s.

[← channel-capacity](/visualizations/channel-capacity/)[modular-arithmetic →](/visualizations/modular-arithmetic/)
