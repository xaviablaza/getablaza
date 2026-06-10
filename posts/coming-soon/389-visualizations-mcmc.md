---
title: mcmc
description: 'Visualizes Metropolis–Hastings MCMC on a 1D bimodal target density pi(x). The animation shows repeated propose-and-correct steps (a candidate x'' is proposed, then accepted/rejected with probability alpha to keep pi invariant). The bottom panel accumulates the empirical histogram and a running time-average g(x)=x, illustrating ergodicity: long-run averages along a single chain converge to expectations under pi.'
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
permalink: /visualizations/mcmc/
---

[← ~/visualizations](/visualizations/)

# mcmc

Visualizes Metropolis–Hastings MCMC on a 1D bimodal target density pi(x). The animation shows repeated propose-and-correct steps (a candidate x' is proposed, then accepted/rejected with probability alpha to keep pi invariant). The bottom panel accumulates the empirical histogram and a running time-average g(x)=x, illustrating ergodicity: long-run averages along a single chain converge to expectations under pi.

canvasclick to interact

⏮◀◀▶▶STEP0.25x1xZOOM

t=0s

## practical uses

- 01.Bayesian inference when the posterior is not analytically sampleable (e.g., hierarchical models)
- 02.Sampling high-dimensional distributions for uncertainty quantification in ML/statistics
- 03.Estimating expectations/normalizing constants via Monte Carlo when only an unnormalized density is available

## technical notes

Uses a persistent closure to simulate a single MH random-walk chain. Target pi(x) is an unnormalized bimodal mixture; symmetric Gaussian proposals make the MH ratio alpha = min(1, pi(x')/pi(x)). Animation interpolates the proposal motion with ease(), while the histogram/mean update only on step completion for clarity. Rendering uses a snapped grid for a blocky green-on-black aesthetic and scales with Math.min(w,h)/baseSize.

[← systems-of-linear-equations](/visualizations/linear-systems/)[computational-complexity-theory →](/visualizations/computational-complexity/)
