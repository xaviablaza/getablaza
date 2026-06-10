---
title: maximum-likelihood-estimation
description: 'Visualizes maximum likelihood estimation with fixed Bernoulli data: θ moves along a slider while the likelihood L(θ) and log-likelihood ℓ(θ)=log L(θ) curves are plotted. The MLE θ̂ is highlighted as the argmax of both L(θ) and ℓ(θ), and a score indicator shows the first-order condition dℓ/dθ=0 at the maximizer.'
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
permalink: /visualizations/mle/
---

[← ~/visualizations](/visualizations/)

# maximum-likelihood-estimation

Visualizes maximum likelihood estimation with fixed Bernoulli data: θ moves along a slider while the likelihood L(θ) and log-likelihood ℓ(θ)=log L(θ) curves are plotted. The MLE θ̂ is highlighted as the argmax of both L(θ) and ℓ(θ), and a score indicator shows the first-order condition dℓ/dθ=0 at the maximizer.

canvasclick to interact

⏮◀◀▶▶STEP0.25x1xZOOM

t=0s

## practical uses

- 01.Estimating a coin’s bias (Bernoulli/binomial parameter) from observed flips
- 02.Fitting model parameters in classification/regression via maximum likelihood (e.g., logistic regression)
- 03.Parameter estimation for probabilistic models in signal processing and A/B testing

## technical notes

Self-contained Canvas2D rendering. Uses responsive scaling via scale=min(w,h)/240, grid-snapped rectangles for a retro blocky look, and time-based ping-pong animation for θ. Likelihood is computed from Bernoulli sufficient statistics (k,n) and normalized for plotting; log-likelihood is min/max normalized. Score sign is derived from d/dθ logL = k/θ − (n−k)/(1−θ).

[← independence](/visualizations/independence/)[what-is-an-algorithm →](/visualizations/algorithm-concept/)
