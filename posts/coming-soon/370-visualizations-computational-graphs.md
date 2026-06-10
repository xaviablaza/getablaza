---
title: computational-graphs
description: Visualizes a small computational graph where each node is an operation f(…) and each directed edge carries a tensor/value. The animation alternates between a forward pass (values move left→right through the graph) and a backward pass (gradients d/dx propagate right→left along the same dependencies), illustrating reverse-mode autodiff (backprop) via the chain rule.
date: '2026-07-01'
scheduled: '2027-07-05'
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
inspiration_url: https://templeton.host/visualizations/computational-graphs/
inspiration_category: visualizations
---

> Source-copy draft imported from [https://templeton.host/visualizations/computational-graphs/](https://templeton.host/visualizations/computational-graphs/). Names, domain references, and local media paths were adapted for Xavi Ablaza / getablaza.com.

[← ~/visualizations](/visualizations/)

# computational-graphs

Visualizes a small computational graph where each node is an operation f(…) and each directed edge carries a tensor/value. The animation alternates between a forward pass (values move left→right through the graph) and a backward pass (gradients d/dx propagate right→left along the same dependencies), illustrating reverse-mode autodiff (backprop) via the chain rule.

canvasclick to interact

⏮◀◀▶▶STEP0.25x1xZOOM

t=0s

## practical uses

- 01.Understanding how neural network layers compose and how intermediate activations feed downstream operations
- 02.Debugging model implementations by locating where values/gradients should flow in forward/backward passes
- 03.Explaining automatic differentiation systems (PyTorch/TF/JAX) and how parameter gradients dL/dw, dL/db are produced

## technical notes

Pure Canvas2D drawing with a snapped grid for a blocky aesthetic. Edges are drawn as elbow arrows; value-flow uses solid arrows and gradient-flow uses dashed arrows. A timed 4.2s cycle highlights one edge at a time and animates a square packet along it; the active pass changes text/opacity to emphasize forward vs backward propagation.

[← tries](/visualizations/tries/)[meta-learning →](/visualizations/meta-learning/)
