---
title: policy-gradient-methods
description: Visualizes a parameterized stochastic policy πθ(a|s) as action-probability bars for two states, then repeatedly samples a short trajectory under πθ. A moving cursor shows the current timestep’s score-function factor ∇θ log πθ(a|s) multiplied by return/advantage (baseline V), illustrating the policy gradient theorem as a sample-based estimator that drives updates and improves the running objective J(θ).
date: '2026-07-01'
scheduled: '2027-10-07'
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
inspiration_url: https://templeton.host/visualizations/policy-gradient/
inspiration_category: visualizations
---

> Source-copy draft imported from [https://templeton.host/visualizations/policy-gradient/](https://templeton.host/visualizations/policy-gradient/). Names, domain references, and local media paths were adapted for Xavi Ablaza / getablaza.com.

[← ~/visualizations](/visualizations/)

# policy-gradient-methods

Visualizes a parameterized stochastic policy πθ(a|s) as action-probability bars for two states, then repeatedly samples a short trajectory under πθ. A moving cursor shows the current timestep’s score-function factor ∇θ log πθ(a|s) multiplied by return/advantage (baseline V), illustrating the policy gradient theorem as a sample-based estimator that drives updates and improves the running objective J(θ).

canvasclick to interact

⏮◀◀▶▶STEP0.25x1xZOOM

t=0s

## practical uses

- 01.Training stochastic policies with REINFORCE when you only have sampled episodes
- 02.Actor-critic methods (using a learned baseline/value to reduce variance)
- 03.Optimizing continuous or discrete action policies directly without a differentiable environment model

## technical notes

Implements a tiny 2-state/2-action MDP and a toy softmax policy with persistent parameters (W logits) plus a baseline V(s). Every ~520ms it samples a horizon-6 trajectory, computes discounted returns with γ=0.95, forms advantages (G−V), applies a REINFORCE-style update to W and an MSE update to V. Rendering uses pixel-snapped rectangles on a black background with GREEN/GREEN\_DIM and eased cursor motion for smooth, educational animation.

[← dimensionality-reduction](/visualizations/dimensionality-reduction/)[basis-and-dimension →](/visualizations/basis-dimension/)
