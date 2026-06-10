---
title: affine-transformations-(linear-layers)
description: 'Visualizes an affine transformation in 2D as a two-step process: first a linear map (y = W·x) that mixes and reweights vector components via matrix multiplication, then a bias translation (+b) that shifts the result independent of the input. The animation cycles through the stages and highlights the corresponding parts of the equation y = W·x + b.'
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
permalink: /visualizations/affine-transformations/
---

[← ~/visualizations](/visualizations/)

# affine-transformations-(linear-layers)

Visualizes an affine transformation in 2D as a two-step process: first a linear map (y = W·x) that mixes and reweights vector components via matrix multiplication, then a bias translation (+b) that shifts the result independent of the input. The animation cycles through the stages and highlights the corresponding parts of the equation y = W·x + b.

canvasclick to interact

⏮◀◀▶▶STEP0.25x1xZOOM

t=0s

## practical uses

- 01.Understanding neural network linear layers (dense/projection layers) as W·x + b
- 02.Interpreting attention projections into Q/K/V as learned affine maps
- 03.Debugging/intuition for how weights mix features vs. how biases shift activations

## technical notes

Pure Canvas2D, time-based 3.6s loop. Uses responsive scaling (scale=min(w,h)/240), snapped pixel/grid coordinates for a blocky aesthetic, and staged easing for linear-map then bias-translation. Vectors are drawn in a small 2D axis frame with arrows and labels; panels show numeric W, b, x, y with staged highlights.

[← dynamic-programming](/visualizations/dynamic-programming/)[vector-spaces →](/visualizations/vector-spaces/)
