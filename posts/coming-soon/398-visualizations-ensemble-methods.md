---
title: ensemble-methods
description: Visualizes how an ensemble combines multiple base learners hᵢ(x) into a single prediction H(x) using voting or averaging. The animation cycles through Bagging (bootstrap resampling and parallel learners), Boosting (sequential learners with increasing weights focusing on errors), and Aggregation (majority vote vs average), showing how H(x)=Σ wᵢ·hᵢ(x) emerges from the learners’ outputs.
date: '2026-07-01'
scheduled: '2027-08-02'
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
inspiration_url: https://templeton.host/visualizations/ensemble-methods/
inspiration_category: visualizations
---

> Source-copy draft imported from [https://templeton.host/visualizations/ensemble-methods/](https://templeton.host/visualizations/ensemble-methods/). Names, domain references, and local media paths were adapted for Xavi Ablaza / getablaza.com.

[← ~/visualizations](/visualizations/)

# ensemble-methods

Visualizes how an ensemble combines multiple base learners hᵢ(x) into a single prediction H(x) using voting or averaging. The animation cycles through Bagging (bootstrap resampling and parallel learners), Boosting (sequential learners with increasing weights focusing on errors), and Aggregation (majority vote vs average), showing how H(x)=Σ wᵢ·hᵢ(x) emerges from the learners’ outputs.

canvasclick to interact

⏮◀◀▶▶STEP0.25x1xZOOM

t=0s

## practical uses

- 01.Random forests: bagging + feature subsampling to reduce variance and improve robustness
- 02.Gradient boosting (XGBoost/LightGBM/CatBoost): sequentially reduce residual errors for strong predictive performance
- 03.Model ensembling in production/competitions: average/vote across diverse models for better generalization

## technical notes

Pure Canvas2D, green-on-black blocky UI with grid snapping. Uses time-based 3-stage cycle (4.5s) with ease() for smooth transitions. Learner predictions are deterministic via a small hash() for stable per-learner diversity; boosting uses normalized weights and a staged highlight to convey sequential training.

[← bayesian-inference](/visualizations/bayesian-inference/)[bias-variance-tradeoff →](/visualizations/bias-variance/)
