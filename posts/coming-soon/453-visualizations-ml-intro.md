---
title: machine-learning-introduction
description: 'Shows the ML pipeline as three blocky panels: a dataset (with labels y in supervised mode, no labels in unsupervised), a parameterized model f(x; θ) with learnable parameters, and an empirical risk R(θ) that training minimizes. Animation cycles between supervised and unsupervised, and within each mode it shows θ updating over time while the risk decreases.'
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
permalink: /visualizations/ml-intro/
---

[← ~/visualizations](/visualizations/)

# machine-learning-introduction

Shows the ML pipeline as three blocky panels: a dataset (with labels y in supervised mode, no labels in unsupervised), a parameterized model f(x; θ) with learnable parameters, and an empirical risk R(θ) that training minimizes. Animation cycles between supervised and unsupervised, and within each mode it shows θ updating over time while the risk decreases.

canvasclick to interact

⏮◀◀▶▶STEP0.25x1xZOOM

t=0s

## practical uses

- 01.Explain what a parameterized hypothesis f(x;θ) means before introducing specific model families (linear models, neural nets).
- 02.Motivate training as optimization by visualizing empirical risk decreasing with parameter updates.
- 03.Clarify the core distinction between supervised and unsupervised learning by showing how labels y change the objective.

## technical notes

Pure Canvas2D, green-on-black retro grid with snapped coordinates for a blocky feel. Time-based animation uses (t/duration)%1 cycles: mode toggles every 3.6s and training progress runs on a 2.6s loop with cubic easing via ease(). Deterministic pseudo-random point placement uses a sine hash for stable visuals without external state.

[← linear-regression](/visualizations/linear-regression/)[minimum-spanning-trees →](/visualizations/minimum-spanning-trees/)
