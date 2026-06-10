---
title: joint-distributions
description: Shows a discrete joint distribution p_{X,Y}(x,y) as a 5×5 probability grid. The animation cycles through (1) summing a highlighted row to form the marginal p_Y(y), (2) summing a highlighted column to form p_X(x), and (3) fixing a y* row and normalizing by p_Y(y*) to produce the conditional p_{X|Y}(x|y*). The right panel reinforces the identities p_{X,Y}=p_{X|Y}·p_Y and Bayes’ rule as an algebraic rearrangement.
date: '2026-07-01'
scheduled: '2027-08-31'
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
inspiration_url: https://templeton.host/visualizations/joint-distributions/
inspiration_category: visualizations
---

> Source-copy draft imported from [https://templeton.host/visualizations/joint-distributions/](https://templeton.host/visualizations/joint-distributions/). Names, domain references, and local media paths were adapted for Xavi Ablaza / getablaza.com.

[← ~/visualizations](/visualizations/)

# joint-distributions

Shows a discrete joint distribution p\_{X,Y}(x,y) as a 5×5 probability grid. The animation cycles through (1) summing a highlighted row to form the marginal p\_Y(y), (2) summing a highlighted column to form p\_X(x), and (3) fixing a y\* row and normalizing by p\_Y(y\*) to produce the conditional p\_{X|Y}(x|y\*). The right panel reinforces the identities p\_{X,Y}=p\_{X|Y}·p\_Y and Bayes’ rule as an algebraic rearrangement.

canvasclick to interact

⏮◀◀▶▶STEP0.25x1xZOOM

t=0s

## practical uses

- 01.Computing marginals from a learned or measured joint distribution (e.g., sensor fusion tables)
- 02.Turning joint models into conditional predictors p(Y|X) for classification/diagnosis
- 03.Understanding independence/correlation structure by comparing joint vs marginals and conditionals

## technical notes

Renders a blocky heatmap on a snapped grid (4px\*scale). Joint probabilities are generated from a small correlated discrete model that smoothly morphs over time, then normalized. Marginals and conditionals are computed each frame and visualized as bar charts and normalized strips; narrative segments are timed over a 4s cycle using smoothstep/ease for emphasis.

[← generating-functions](/visualizations/generating-functions/)[recurrence-relations →](/visualizations/recurrence-relations/)
