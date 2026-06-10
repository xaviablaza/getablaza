---
title: derivative-rules
description: Animated 4-panel, green-on-black visualization cycling through power, product, chain, and quotient rules. Each panel shows a function (dim) and its derivative (bright) on a shared graph, with a moving sample point x* and a right-side blocky ‘formula pipeline’ that highlights how each rule is applied. The quotient rule panel explicitly rewrites f/g as f·(1/g) and then applies the product rule to reveal the reciprocal derivative piece.
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
permalink: /visualizations/derivative-rules/
---

[← ~/visualizations](/visualizations/)

# derivative-rules

Animated 4-panel, green-on-black visualization cycling through power, product, chain, and quotient rules. Each panel shows a function (dim) and its derivative (bright) on a shared graph, with a moving sample point x\* and a right-side blocky ‘formula pipeline’ that highlights how each rule is applied. The quotient rule panel explicitly rewrites f/g as f·(1/g) and then applies the product rule to reveal the reciprocal derivative piece.

canvasclick to interact

⏮◀◀▶▶STEP0.25x1xZOOM

t=0s

## practical uses

- 01.Differentiate polynomials and power functions quickly (power rule).
- 02.Differentiate multiplied signals/models in physics/economics (product rule).
- 03.Differentiate nested functions in optimization and machine learning (chain rule).
- 04.Differentiate ratios like efficiency = output/input and rational functions (quotient rule).

## technical notes

Pure Canvas2D TypeScript draw function using time-sliced panels (2–4s each). Uses responsive scaling via scale=min(w,h)/240 and a snapped pixel grid for a blocky aesthetic. Plots functions with polyline sampling and overlays derivatives; animates a sweeping x\* point and per-panel emphasis via smoothstep/ease blending.

[← kernel-methods](/visualizations/kernel-methods/)
