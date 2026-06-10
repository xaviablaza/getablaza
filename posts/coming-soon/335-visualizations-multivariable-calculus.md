---
title: multivariable-calculus
description: Visualizes a multivariable function z=f(x,y) as a gridded surface. Then it animates partial derivatives by taking x- and y-slices through a moving point and shrinking the step h in the difference quotient (holding the other variable fixed). Finally it shows the gradient vector ∇f, a rotating displacement Δx, and the first-order change approximation Δf ≈ ∇f·Δx, comparing linear prediction to the actual surface step.
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
permalink: /visualizations/multivariable-calculus/
---

[← ~/visualizations](/visualizations/)

# multivariable-calculus

Visualizes a multivariable function z=f(x,y) as a gridded surface. Then it animates partial derivatives by taking x- and y-slices through a moving point and shrinking the step h in the difference quotient (holding the other variable fixed). Finally it shows the gradient vector ∇f, a rotating displacement Δx, and the first-order change approximation Δf ≈ ∇f·Δx, comparing linear prediction to the actual surface step.

canvasclick to interact

⏮◀◀▶▶STEP0.25x1xZOOM

t=0s

## practical uses

- 01.Optimization in machine learning (gradients for training)
- 02.Physics and engineering fields (temperature/pressure fields, flux)
- 03.Computer graphics and geometry (normals, shading from gradients)

## technical notes

Pure Canvas2D; blocky aesthetic via 4px snapping and squared markers. Surface uses a lightweight projected grid (no fills) for speed. Animation cycles through 4 stages (~3.8s) and uses easing to shrink h toward 0 for the limit interpretation. Gradient/dot-product shown in a 2D inset plus a predicted-vs-actual step on the surface.

[← variance](/visualizations/variance/)[gradients →](/visualizations/gradients/)
