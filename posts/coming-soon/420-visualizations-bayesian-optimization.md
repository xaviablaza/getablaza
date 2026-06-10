---
title: bayesian-optimization
description: 'Animated closed-loop Bayesian Optimization: a hidden objective f(x) (faint), a probabilistic surrogate summarized by μ(x) and an uncertainty band (σ), and an acquisition function a(x) that trades exploitation (-μ) and exploration (κσ). Each cycle highlights x_next = argmax a(x), evaluates f(x_next) (falling sample), then updates the surrogate.'
date: '2026-07-01'
scheduled: '2027-08-24'
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
inspiration_url: https://templeton.host/visualizations/bayesian-optimization/
inspiration_category: visualizations
---

> Source-copy draft imported from [https://templeton.host/visualizations/bayesian-optimization/](https://templeton.host/visualizations/bayesian-optimization/). Names, domain references, and local media paths were adapted for Xavi Ablaza / getablaza.com.

[← ~/visualizations](/visualizations/)

# bayesian-optimization

Animated closed-loop Bayesian Optimization: a hidden objective f(x) (faint), a probabilistic surrogate summarized by μ(x) and an uncertainty band (σ), and an acquisition function a(x) that trades exploitation (-μ) and exploration (κσ). Each cycle highlights x\_next = argmax a(x), evaluates f(x\_next) (falling sample), then updates the surrogate.

canvasclick to interact

⏮◀◀▶▶STEP0.25x1xZOOM

t=0s

## practical uses

- 01.Hyperparameter tuning of ML models with expensive training runs
- 02.Optimizing engineering design parameters using costly simulations (CFD/FEA)
- 03.Calibrating experiments or A/B settings when each evaluation is expensive

## technical notes

Self-contained canvas 2D animation with a simple RBF-kernel surrogate (kernel regression + heuristic uncertainty) and UCB acquisition. Time is segmented into phases (update → acquire → evaluate) over a 3s loop. Blocky grid-snapped rendering with green-on-black palette.

[← activation-functions](/visualizations/activation-functions/)[eigenvalues-and-eigenvectors →](/visualizations/eigenvalues/)
