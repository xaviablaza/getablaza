---
title: gradients
description: Shows a scalar field f(x,y) with animated contour lines (level sets). A movable sample point displays the gradient vector ∇f as the direction of steepest ascent, a tangent segment to the nearby contour (demonstrating ∇f ⟂ level sets), and a rotating unit direction u to illustrate the directional derivative D_u f = ∇f·u via a live dot-product bar.
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
permalink: /visualizations/gradients/
---

[← ~/visualizations](/visualizations/)

# gradients

Shows a scalar field f(x,y) with animated contour lines (level sets). A movable sample point displays the gradient vector ∇f as the direction of steepest ascent, a tangent segment to the nearby contour (demonstrating ∇f ⟂ level sets), and a rotating unit direction u to illustrate the directional derivative D\_u f = ∇f·u via a live dot-product bar.

canvasclick to interact

⏮◀◀▶▶STEP0.25x1xZOOM

t=0s

## practical uses

- 01.Gradient descent/ascent in machine learning optimization
- 02.Finding steepest slope directions in terrain/heightmap analysis
- 03.Computing directional rates of change in physics (e.g., temperature/pressure fields)

## technical notes

Contours are approximated by sampling a grid and drawing crossing segments per level (marching-squares style). The sample point is pointer-controlled when available; otherwise it follows a smooth loop. All geometry is snapped to a small pixel grid for a retro blocky aesthetic; animations are time-based (2–4s cycles).

[← multivariable-calculus](/visualizations/multivariable-calculus/)[cosine-similarity →](/visualizations/cosine-similarity/)
