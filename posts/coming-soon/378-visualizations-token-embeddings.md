---
title: token-embeddings
description: Shows how a discrete token id i selects a row from the embedding matrix E (a learnable lookup table). The selected row E[i] is highlighted and displayed as a length-d vector, while an animated “lookup packet” travels from the token list to the corresponding row. A simple training-like update continuously nudges only the selected row’s values to illustrate embeddings as learned parameters.
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
permalink: /visualizations/token-embeddings/
---

[← ~/visualizations](/visualizations/)

# token-embeddings

Shows how a discrete token id i selects a row from the embedding matrix E (a learnable lookup table). The selected row E[i] is highlighted and displayed as a length-d vector, while an animated “lookup packet” travels from the token list to the corresponding row. A simple training-like update continuously nudges only the selected row’s values to illustrate embeddings as learned parameters.

canvasclick to interact

⏮◀◀▶▶STEP0.25x1xZOOM

t=0s

## practical uses

- 01.Turning token IDs into model inputs for transformers/RNNs via embedding lookup
- 02.Understanding why embedding tables scale with vocabulary size × dimensionality (|V|·d)
- 03.Building intuition for how training updates only the rows for tokens seen in a batch (sparse parameter updates)

## technical notes

Pure Canvas2D. Uses a closure to maintain an embedding matrix E and performs a small continuous update on the currently selected row to simulate training. Layout and shapes are grid-snapped for a blocky aesthetic; animation cycles via step-based token selection plus eased packet motion.

[← diffusion-models](/visualizations/diffusion-models/)[reinforcement-learning-introduction →](/visualizations/rl-intro/)
