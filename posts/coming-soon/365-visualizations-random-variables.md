---
title: random-variables
description: 'Shows a random variable X as a mapping from outcomes ω in a sample space to numbers, then compares discrete vs continuous distributions. The bottom panels animate an interval (a,b] and demonstrate that P(a<X≤b)=F_X(b)-F_X(a): as a sum of PMF bars for a discrete RV and as an area under the PDF (integral) for a continuous RV, with the corresponding CDF step-curve vs smooth curve.'
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
permalink: /visualizations/random-variables/
---

[← ~/visualizations](/visualizations/)

# random-variables

Shows a random variable X as a mapping from outcomes ω in a sample space to numbers, then compares discrete vs continuous distributions. The bottom panels animate an interval (a,b] and demonstrate that P(a<X≤b)=F\_X(b)-F\_X(a): as a sum of PMF bars for a discrete RV and as an area under the PDF (integral) for a continuous RV, with the corresponding CDF step-curve vs smooth curve.

canvasclick to interact

⏮◀◀▶▶STEP0.25x1xZOOM

t=0s

## practical uses

- 01.Computing interval probabilities using the CDF difference F(b)-F(a)
- 02.Understanding why discrete distributions use a PMF (probability mass at points) while continuous distributions use a PDF (area over intervals)
- 03.Interpreting CDF plots as a complete distribution summary for modeling and simulation

## technical notes

Self-contained canvas draw function with retro grid-snapped rendering and green-on-black palette. Includes a small mouse interaction (mousemove) attached once to the canvas: x controls interval center, y controls interval width; otherwise it auto-animates. Uses simple normal PDF/CDF approximations (erf approximation) and a fixed discrete PMF to illustrate step vs smooth CDF behavior.

[← cross-validation](/visualizations/cross-validation/)[hypothesis-testing →](/visualizations/hypothesis-testing/)
