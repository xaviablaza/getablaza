---
title: law-of-large-numbers
description: Streams iid samples X_i from a fixed distribution (a fair die), computes the running sample mean X̄_n, and shows how X̄_n stabilizes near the expected value E[X] as n grows. A shrinking green band around E[X] visually suggests convergence in probability.
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
permalink: /visualizations/law-large-numbers/
---

[← ~/visualizations](/visualizations/)

# law-of-large-numbers

Streams iid samples X\_i from a fixed distribution (a fair die), computes the running sample mean X̄\_n, and shows how X̄\_n stabilizes near the expected value E[X] as n grows. A shrinking green band around E[X] visually suggests convergence in probability.

canvasclick to interact

⏮◀◀▶▶STEP0.25x1xZOOM

t=0s

## practical uses

- 01.Estimating an unknown mean from repeated measurements (A/B tests, surveys)
- 02.Monte Carlo estimation (approximating expectations with simulated samples)
- 03.Quality control and process monitoring (averages stabilize with more observations)

## technical notes

Uses a closure to maintain state (n, sum, recent samples, mean history). Sampling rate ramps within a ~4.2s cycle to emphasize behavior as n increases; state softly resets after large n. Rendering is grid-snapped for a blocky aesthetic; expectation line and a ~1/√n band illustrate tightening concentration around E[X].

[← principal-component-analysis](/visualizations/pca/)[taylor-series →](/visualizations/taylor-series/)
