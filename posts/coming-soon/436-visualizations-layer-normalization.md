---
title: layer-normalization
description: 'Shows a batch of activation vectors (rows) being normalized per-sample across feature dimensions: compute μ and σ² for each row, normalize z=(x-μ)/√(σ²+ε), then apply learned per-feature affine parameters γ and β to produce the output y. Animation highlights one sample at a time to emphasize that statistics are not computed across the batch.'
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
permalink: /visualizations/layer-normalization/
---

[← ~/visualizations](/visualizations/)

# layer-normalization

Shows a batch of activation vectors (rows) being normalized per-sample across feature dimensions: compute μ and σ² for each row, normalize z=(x-μ)/√(σ²+ε), then apply learned per-feature affine parameters γ and β to produce the output y. Animation highlights one sample at a time to emphasize that statistics are not computed across the batch.

canvasclick to interact

⏮◀◀▶▶STEP0.25x1xZOOM

t=0s

## practical uses

- 01.Stabilizing training in Transformers/RNNs where batch statistics are inconvenient
- 02.Improving optimization by keeping activations well-scaled per example
- 03.Retaining representational flexibility via learned γ (scale) and β (shift) after normalization

## technical notes

Pure Canvas2D, blocky grid cells with snapped coordinates. 4-stage loop (input → stats → normalize → affine) over ~4.2s; active sample and feature indices cycle independently. Per-sample μ/σ² bars and per-feature γ/β panel reinforce the axes of normalization vs learned affine parameters.

[← convex-optimization](/visualizations/convex-optimization/)[auction-theory →](/visualizations/auction-theory/)
