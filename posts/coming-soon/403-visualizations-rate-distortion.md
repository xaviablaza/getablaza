---
title: rate-distortion-theory
description: Visualizes the variational definition of the rate–distortion function. The animation sweeps a distortion target D, updates an R(D) curve (minimal bits per symbol), and shows a discrete test-channel p(x̂|x) that becomes sharper at low distortion (more informative, higher mutual information) and flatter at high distortion (less informative, lower mutual information).
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
source_format: html
inspiration_url: https://templeton.host/visualizations/rate-distortion/
inspiration_category: visualizations
---

> Source-copy draft imported from [https://templeton.host/visualizations/rate-distortion/](https://templeton.host/visualizations/rate-distortion/). Names, domain references, and local media paths were adapted for Xavi Ablaza / getablaza.com.

[← ~/visualizations](/visualizations/)

# rate-distortion-theory

Visualizes the variational definition of the rate–distortion function. The animation sweeps a distortion target D, updates an R(D) curve (minimal bits per symbol), and shows a discrete test-channel p(x̂|x) that becomes sharper at low distortion (more informative, higher mutual information) and flatter at high distortion (less informative, lower mutual information).

canvasclick to interact

⏮◀◀▶▶STEP0.25x1xZOOM

t=0s

## practical uses

- 01.Tuning video/audio/image codecs by selecting a bitrate–quality operating point
- 02.Designing quantizers and reconstruction rules under an average distortion constraint
- 03.Understanding ML compression and bottlenecks (information constraints vs. fidelity)

## technical notes

Pure Canvas2D, green-on-black, grid-snapped geometry. D cycles smoothly (ease(tri)). R(D) is a stylized convex decreasing curve; p(x̂|x) is a 3x3 softmax over negative squared-error distortion with temperature tied to D; mutual information I(X;X̂) is computed from the discrete distributions and displayed alongside the variational equation.

[← strongly-connected-components](/visualizations/strongly-connected/)[cross-entropy →](/visualizations/cross-entropy/)
