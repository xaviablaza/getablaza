---
title: common-distributions
description: Visualizes the difference between discrete vs continuous support by switching between PMF bars and PDF curves, then shows normalization (sum/integral → 1) and how parameters θ determine moments (mean/variance) for Bernoulli, Binomial, Poisson, Uniform, and Normal families.
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
permalink: /visualizations/common-distributions/
---

[← ~/visualizations](/visualizations/)

# common-distributions

Visualizes the difference between discrete vs continuous support by switching between PMF bars and PDF curves, then shows normalization (sum/integral → 1) and how parameters θ determine moments (mean/variance) for Bernoulli, Binomial, Poisson, Uniform, and Normal families.

canvasclick to interact

⏮◀◀▶▶STEP0.25x1xZOOM

t=0s

## practical uses

- 01.Choosing an appropriate model for counts vs measurements (PMF vs PDF)
- 02.Checking whether a hand-built probability function is valid via normalization
- 03.Understanding how parameters (p, λ, μ, σ, a, b) control mean and variance for simulation and inference

## technical notes

Single self-contained Canvas2D draw function. Cycles through 5 distributions in ~4.2s segments, animates a point-probability (discrete) or interval area (continuous), approximates normalization by summation or midpoint-rule integration, and uses grid-snapped rectangles/lines for a retro blocky green-on-black aesthetic.

[← generative-adversarial-networks](/visualizations/gan/)[sequence-to-sequence-modeling →](/visualizations/sequence-to-sequence-modeling/)
