---
title: fundamental-theorem-of-calculus
description: 'Shows f(x) on the top panel with a moving upper limit x and blocky Riemann shading for the signed area ∫_a^x f(t)dt. The bottom panel graphs the accumulation function F(x) and draws a tangent whose slope dF/dx numerically matches the current f(x), illustrating FTC Part 1. A center annotation highlights FTC Part 2: ∫_a^b f(x)dx = F(b) − F(a).'
date: '2026-07-01'
scheduled: '2027-08-09'
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
inspiration_url: https://templeton.host/visualizations/fundamental-theorem/
inspiration_category: visualizations
---

> Source-copy draft imported from [https://templeton.host/visualizations/fundamental-theorem/](https://templeton.host/visualizations/fundamental-theorem/). Names, domain references, and local media paths were adapted for Xavi Ablaza / getablaza.com.

[← ~/visualizations](/visualizations/)

# fundamental-theorem-of-calculus

Shows f(x) on the top panel with a moving upper limit x and blocky Riemann shading for the signed area ∫\_a^x f(t)dt. The bottom panel graphs the accumulation function F(x) and draws a tangent whose slope dF/dx numerically matches the current f(x), illustrating FTC Part 1. A center annotation highlights FTC Part 2: ∫\_a^b f(x)dx = F(b) − F(a).

canvasclick to interact

⏮◀◀▶▶STEP0.25x1xZOOM

t=0s

## practical uses

- 01.Compute definite integrals via antiderivatives (evaluation theorem)
- 02.Interpret integrals as accumulated change (area/accumulation models)
- 03.Connect rates (derivatives) to totals (integrals) in physics and engineering

## technical notes

Uses time-based sweep x=a→b with ease() for smooth motion. f(x) is sampled to scale axes; F(x) is computed each frame by a midpoint Riemann sum, and dF/dx is approximated with a centered finite difference. Rendering uses grid-snapped coordinates and Riemann bars for a retro blocky aesthetic on a black background with green highlights.

[← cross-entropy](/visualizations/cross-entropy/)[propositional-logic →](/visualizations/propositional-logic/)
