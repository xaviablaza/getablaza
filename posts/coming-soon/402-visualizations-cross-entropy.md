---
title: cross-entropy
description: Animated green-on-black visualization of cross-entropy as the average surprise of a model q on samples from a true distribution p. The left panel shows evolving class probabilities for p (true) and q (model). The right panel alternates between (1) the decomposition H(p,q)=H(p)+KL(p||q) with a stacked bar, and (2) the one-hot classification case where H(p,q) reduces to the negative log-likelihood -log q(y) of the correct class.
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
permalink: /visualizations/cross-entropy/
---

[← ~/visualizations](/visualizations/)

# cross-entropy

Animated green-on-black visualization of cross-entropy as the average surprise of a model q on samples from a true distribution p. The left panel shows evolving class probabilities for p (true) and q (model). The right panel alternates between (1) the decomposition H(p,q)=H(p)+KL(p||q) with a stacked bar, and (2) the one-hot classification case where H(p,q) reduces to the negative log-likelihood -log q(y) of the correct class.

canvasclick to interact

⏮◀◀▶▶STEP0.25x1xZOOM

t=0s

## practical uses

- 01.Classification loss for neural networks (softmax + cross-entropy)
- 02.Measuring how well a probabilistic model q matches observed data p
- 03.Deriving and interpreting KL divergence as the gap between entropy and cross-entropy

## technical notes

Uses deterministic time-based morphing of 3-class distributions p and q (q lags and wobbles to create KL). Computes entropy, cross-entropy, and KL in nats (natural log). Renders block-snapped bars and labels on a scanlined black background; cycles between decomposition and one-hot views every ~3.8s using provided cubic ease().

[← rate-distortion-theory](/visualizations/rate-distortion/)[fundamental-theorem-of-calculus →](/visualizations/fundamental-theorem/)
