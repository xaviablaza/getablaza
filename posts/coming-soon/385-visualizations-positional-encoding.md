---
title: positional-encoding
description: Shows how position index p is mapped to a positional encoding vector PE(p) and injected into token representations (via add/concat) so parallel processing can still use order; contrasts with relative schemes that use offsets (p_i − p_j) as attention biases in an i×j attention grid.
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
inspiration_url: https://templeton.host/visualizations/positional-encoding/
inspiration_category: visualizations
---

> Source-copy draft imported from [https://templeton.host/visualizations/positional-encoding/](https://templeton.host/visualizations/positional-encoding/). Names, domain references, and local media paths were adapted for Xavi Ablaza / getablaza.com.

[← ~/visualizations](/visualizations/)

# positional-encoding

Shows how position index p is mapped to a positional encoding vector PE(p) and injected into token representations (via add/concat) so parallel processing can still use order; contrasts with relative schemes that use offsets (p\_i − p\_j) as attention biases in an i×j attention grid.

canvasclick to interact

⏮◀◀▶▶STEP0.25x1xZOOM

t=0s

## practical uses

- 01.Enable Transformers to represent word order without recurrence/convolutions
- 02.Improve long-context generalization (e.g., sinusoidal/rotary or other structured encodings)
- 03.Model relative relationships like distance-based attention bias for tasks such as retrieval, code, and time series

## technical notes

Three-panel loop (absolute → relative → integration) over ~3.6s. Left column renders token positions and vector bars for E(token), PE(p), and their combination; right column renders an attention matrix where cell intensity depends on |i−j| and a highlighted (i,j) shows Δ=p\_i−p\_j. All geometry is grid-snapped for a blocky aesthetic; animation is time-based using ease() and cycling indices.

[← softmax-and-logits](/visualizations/softmax-and-logits/)[game-theory-introduction →](/visualizations/game-theory-intro/)
