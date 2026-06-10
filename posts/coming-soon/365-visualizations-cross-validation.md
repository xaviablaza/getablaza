---
title: cross-validation
description: 'Visualizes held-out evaluation with k-fold cross-validation: the dataset is partitioned into k disjoint folds; each step highlights one fold as the validation (held-out) set while the others are used for training; the per-fold validation loss L(y, ŷ) is recorded and then aggregated (averaged) into a single cross-validation estimate of expected generalization error. A blinking note indicates LOOCV as the special case k = N.'
date: '2026-07-01'
scheduled: '2027-06-30'
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
inspiration_url: https://templeton.host/visualizations/cross-validation/
inspiration_category: visualizations
---

> Source-copy draft imported from [https://templeton.host/visualizations/cross-validation/](https://templeton.host/visualizations/cross-validation/). Names, domain references, and local media paths were adapted for Xavi Ablaza / getablaza.com.

[← ~/visualizations](/visualizations/)

# cross-validation

Visualizes held-out evaluation with k-fold cross-validation: the dataset is partitioned into k disjoint folds; each step highlights one fold as the validation (held-out) set while the others are used for training; the per-fold validation loss L(y, ŷ) is recorded and then aggregated (averaged) into a single cross-validation estimate of expected generalization error. A blinking note indicates LOOCV as the special case k = N.

canvasclick to interact

⏮◀◀▶▶STEP0.25x1xZOOM

t=0s

## practical uses

- 01.Estimate generalization error when you have limited data (no separate test set available)
- 02.Select hyperparameters/models by comparing mean cross-validation loss across candidates
- 03.Diagnose instability/variance by observing how much validation loss varies across folds (e.g., high variance suggests sensitivity to data splits)

## technical notes

Pure Canvas2D with a 4px-snapped blocky aesthetic on black. Animation cycles through folds in discrete steps (~520ms each) using ease() for within-step progression, then transitions into an aggregation phase that eases the running mean toward the full k-fold mean. No randomness: per-fold losses are deterministic sinusoidal values for repeatable playback.

[← kl-divergence](/visualizations/kl-divergence/)[random-variables →](/visualizations/random-variables/)
