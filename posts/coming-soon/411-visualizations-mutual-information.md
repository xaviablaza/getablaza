---
title: mutual-information
description: Shows a joint distribution P(X,Y) as a blocky 8×8 heatmap, with marginals P(X), P(Y). The animation cycles between independence (P(X,Y)=P(X)P(Y), diff grid near zero, I(X;Y)≈0) and dependence (diagonal structure, diff grid lights up, I(X;Y)>0). A decomposition bar visualizes I(X;Y)=H(X)−H(X|Y) by splitting H(X) into the shared part (mutual information) and the remaining uncertainty (conditional entropy).
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
inspiration_url: https://templeton.host/visualizations/mutual-information/
inspiration_category: visualizations
---

> Source-copy draft imported from [https://templeton.host/visualizations/mutual-information/](https://templeton.host/visualizations/mutual-information/). Names, domain references, and local media paths were adapted for Xavi Ablaza / getablaza.com.

[← ~/visualizations](/visualizations/)

# mutual-information

Shows a joint distribution P(X,Y) as a blocky 8×8 heatmap, with marginals P(X), P(Y). The animation cycles between independence (P(X,Y)=P(X)P(Y), diff grid near zero, I(X;Y)≈0) and dependence (diagonal structure, diff grid lights up, I(X;Y)>0). A decomposition bar visualizes I(X;Y)=H(X)−H(X|Y) by splitting H(X) into the shared part (mutual information) and the remaining uncertainty (conditional entropy).

canvasclick to interact

⏮◀◀▶▶STEP0.25x1xZOOM

t=0s

## practical uses

- 01.Feature selection: measure how informative a feature is about a label
- 02.Detecting dependence/correlation beyond linear correlation (nonlinear relationships)
- 03.Clustering and representation learning (e.g., mutual information-based objectives)

## technical notes

Computes entropies and mutual information in bits from an 8×8 synthetic joint distribution that smoothly blends between an independent product-of-marginals model and a diagonal-biased dependent model. Uses time-based easing to linger at endpoints, renders blocky snapped rectangles, and includes an animated scanline to illustrate how conditioning on Y narrows uncertainty in X.

[← online-algorithms](/visualizations/online-algorithms/)[central-limit-theorem →](/visualizations/central-limit-theorem/)
