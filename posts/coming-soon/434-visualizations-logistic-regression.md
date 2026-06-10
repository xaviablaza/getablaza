---
title: logistic-regression
description: 'Visualizes the logistic regression pipeline for a single example: a linear score z = w·x is accumulated term-by-term (including bias), mapped through the sigmoid curve to a probability p, then converted into a per-example binary cross-entropy loss. A bottom panel shows the 2D decision boundary (z=0) and a coarse probability field that updates as weights and the example point change over time.'
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
permalink: /visualizations/logistic-regression/
---

[← ~/visualizations](/visualizations/)

# logistic-regression

Visualizes the logistic regression pipeline for a single example: a linear score z = w·x is accumulated term-by-term (including bias), mapped through the sigmoid curve to a probability p, then converted into a per-example binary cross-entropy loss. A bottom panel shows the 2D decision boundary (z=0) and a coarse probability field that updates as weights and the example point change over time.

canvasclick to interact

⏮◀◀▶▶STEP0.25x1xZOOM

t=0s

## practical uses

- 01.Spam vs. not-spam classification from email features
- 02.Medical risk prediction (e.g., disease present vs. absent)
- 03.Click-through rate prediction (clicked vs. not clicked)

## technical notes

Pure Canvas2D, green-on-black blocky style using grid snapping. Time-based cycling: weights and the displayed sample interpolate every ~0.9s; full cycle ~3.6s. Sigmoid and cross-entropy are plotted with stable clamped logs; decision boundary is drawn from z=0 in feature space; probability field rendered as coarse cells for a retro aesthetic.

[← sequence-to-sequence-modeling](/visualizations/sequence-to-sequence-modeling/)[singular-value-decomposition →](/visualizations/svd/)
