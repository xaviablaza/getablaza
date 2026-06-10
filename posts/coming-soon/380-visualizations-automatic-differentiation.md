---
title: automatic-differentiation
description: Visualizes a tiny program trace (mul → sin → add) as a computational graph and shows how automatic differentiation applies the chain rule by composing local Jacobians. The animation alternates between forward-mode (pushing value+tangent left-to-right) and reverse-mode (pulling adjoints right-to-left) to highlight their different propagation directions and cost scaling.
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
permalink: /visualizations/automatic-differentiation/
---

[← ~/visualizations](/visualizations/)

# automatic-differentiation

Visualizes a tiny program trace (mul → sin → add) as a computational graph and shows how automatic differentiation applies the chain rule by composing local Jacobians. The animation alternates between forward-mode (pushing value+tangent left-to-right) and reverse-mode (pulling adjoints right-to-left) to highlight their different propagation directions and cost scaling.

canvasclick to interact

⏮◀◀▶▶STEP0.25x1xZOOM

t=0s

## practical uses

- 01.Understanding backpropagation as reverse-mode AD in deep learning
- 02.Estimating gradient computation cost tradeoffs (forward vs reverse) when choosing implementations
- 03.Debugging/implementing custom differentiable ops by reasoning about local derivatives and their composition

## technical notes

Single self-contained Canvas2D draw function. Uses a 4–8px snapped grid for a retro blocky look, GREEN/GREEN\_DIM on black, and a 4.2s cycle that alternates forward and reverse sweeps with cubic easing (ease). The visualization is symbolic (local Jacobians labeled) to emphasize chain-rule composition over numeric evaluation.

[← reinforcement-learning-introduction](/visualizations/rl-intro/)[deep-learning →](/visualizations/deep-learning/)
