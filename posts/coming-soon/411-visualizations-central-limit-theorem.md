---
title: central-limit-theorem
description: Simulates standardized sums Zₙ of many i.i.d. random variables from different base distributions (uniform, ±1, shifted exponential) and shows how the histogram of Zₙ approaches the overlaid standard normal curve N(0,1) as n increases. Side panels emphasize the CLT conditions (independence, finite variance) and the standardization step (centering by nμ and scaling by σ√n).
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
permalink: /visualizations/central-limit-theorem/
---

[← ~/visualizations](/visualizations/)

# central-limit-theorem

Simulates standardized sums Zₙ of many i.i.d. random variables from different base distributions (uniform, ±1, shifted exponential) and shows how the histogram of Zₙ approaches the overlaid standard normal curve N(0,1) as n increases. Side panels emphasize the CLT conditions (independence, finite variance) and the standardization step (centering by nμ and scaling by σ√n).

canvasclick to interact

⏮◀◀▶▶STEP0.25x1xZOOM

t=0s

## practical uses

- 01.Justifying normal approximations for sums/averages in quality control and measurement error
- 02.Building confidence intervals and hypothesis tests for means when n is moderately large
- 03.Explaining why many aggregated signals/noises look Gaussian even when individual components are not

## technical notes

Per-frame Monte Carlo sampling updates a 64-bin histogram over z∈[-4,4] with exponential forgetting and light 1D smoothing. The visualization cycles through n values (1→100) and base distributions, overlaying the analytic N(0,1) density for comparison. All drawing is grid-snapped for a blocky aesthetic and uses only the Canvas 2D API.

[← mutual-information](/visualizations/mutual-information/)[graph-representations →](/visualizations/graph-representations/)
