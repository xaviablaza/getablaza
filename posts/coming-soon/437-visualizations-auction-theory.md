---
title: auction-theory
description: 'Shows an auction mechanism as a mapping from bid profiles b to allocation x(b) and payments p(b), then animates the incentive-compatibility (envelope) link: a monotone allocation rule x(v) pins payments p(v) up to a constant. The final stage highlights Revenue Equivalence: with the same allocation rule and a shared normalization p(0), different IC auction formats yield the same expected payments (seller revenue).'
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
permalink: /visualizations/auction-theory/
---

[← ~/visualizations](/visualizations/)

# auction-theory

Shows an auction mechanism as a mapping from bid profiles b to allocation x(b) and payments p(b), then animates the incentive-compatibility (envelope) link: a monotone allocation rule x(v) pins payments p(v) up to a constant. The final stage highlights Revenue Equivalence: with the same allocation rule and a shared normalization p(0), different IC auction formats yield the same expected payments (seller revenue).

canvasclick to interact

⏮◀◀▶▶STEP0.25x1xZOOM

t=0s

## practical uses

- 01.Explaining why second-price and (properly normalized) alternative IC mechanisms can have identical expected revenue under IPV assumptions
- 02.Teaching the envelope theorem intuition: payments are determined by allocation monotonicity in single-parameter environments
- 03.Comparing auction designs by focusing on allocation rules (efficiency vs. reserve prices) rather than payment details

## technical notes

Pure Canvas2D, green-on-black blocky UI with snapped coordinates. A 3-stage 4.2s cycle: (1) mechanism outputs x,p, (2) envelope visualization with shaded ∫x and v·x rectangle, (3) revenue equivalence callout. Allocation curve is a quantized monotone S-shape for a retro step-plot aesthetic.

[← layer-normalization](/visualizations/layer-normalization/)[projections →](/visualizations/projections/)
