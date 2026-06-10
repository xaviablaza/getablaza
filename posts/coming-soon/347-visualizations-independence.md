---
title: independence
description: 'Shows independence as a geometric/product rule: event A is a vertical strip and event B is a horizontal strip inside a sample-space rectangle, so the overlap area (A∩B) equals P(A)·P(B). A second panel compares P(A) to P(A|B) (and P(A|not B)) to emphasize that conditioning gives no new information when A and B are independent.'
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
permalink: /visualizations/independence/
---

[← ~/visualizations](/visualizations/)

# independence

Shows independence as a geometric/product rule: event A is a vertical strip and event B is a horizontal strip inside a sample-space rectangle, so the overlap area (A∩B) equals P(A)·P(B). A second panel compares P(A) to P(A|B) (and P(A|not B)) to emphasize that conditioning gives no new information when A and B are independent.

canvasclick to interact

⏮◀◀▶▶STEP0.25x1xZOOM

t=0s

## practical uses

- 01.Checking whether two sensors/errors can be modeled independently in a system model
- 02.Simplifying calculations in probability by replacing joint probabilities with products of marginals
- 03.Validating assumptions in A/B testing or randomized experiments (treatment independent of assignment)

## technical notes

Responsive two-panel layout using scale=Math.min(w,h)/baseSize with 4px snapping for a blocky aesthetic. Time-based 4.2s cycle reveals marginals, then joint-as-product, then conditional equality; uses the provided ease(t) for smooth phase transitions. Pure Canvas2D drawing (rectangles, stroke/fill, monospace labels) on black with GREEN/GREEN\_DIM accents.

[← greedy-algorithms](/visualizations/greedy-algorithms/)[maximum-likelihood-estimation →](/visualizations/mle/)
