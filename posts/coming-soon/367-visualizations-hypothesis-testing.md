---
title: hypothesis-testing
description: 'Visualizes the hypothesis testing pipeline: competing statements (H0 vs Ha), a sample producing an observed test statistic z_obs, the null distribution of the statistic under H0, the p-value as the right-tail probability beyond z_obs, and the decision rule comparing p to a pre-specified significance level α (reject H0 when p ≤ α).'
date: '2026-07-01'
scheduled: '2027-07-02'
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
inspiration_url: https://templeton.host/visualizations/hypothesis-testing/
inspiration_category: visualizations
---

> Source-copy draft imported from [https://templeton.host/visualizations/hypothesis-testing/](https://templeton.host/visualizations/hypothesis-testing/). Names, domain references, and local media paths were adapted for Xavi Ablaza / getablaza.com.

[← ~/visualizations](/visualizations/)

# hypothesis-testing

Visualizes the hypothesis testing pipeline: competing statements (H0 vs Ha), a sample producing an observed test statistic z\_obs, the null distribution of the statistic under H0, the p-value as the right-tail probability beyond z\_obs, and the decision rule comparing p to a pre-specified significance level α (reject H0 when p ≤ α).

canvasclick to interact

⏮◀◀▶▶STEP0.25x1xZOOM

t=0s

## practical uses

- 01.A/B testing: decide if a new variant improves a conversion rate beyond random noise
- 02.Quality control: detect if a manufacturing process mean has drifted above a tolerance
- 03.Scientific experiments: quantify evidence against a null effect using a p-value threshold

## technical notes

Pure Canvas 2D. Uses a 4-stage time cycle (~4.2s) with easing to sequentially reveal sample -> statistic -> p-value shading -> decision. Null distribution is drawn as blocky vertical bars from a standard normal PDF; p-value uses a self-contained normal CDF via an erf approximation. All geometry is grid-snapped for a retro block aesthetic and scaled with scale = min(w,h)/240.

[← random-variables](/visualizations/random-variables/)[continuity →](/visualizations/continuity/)
