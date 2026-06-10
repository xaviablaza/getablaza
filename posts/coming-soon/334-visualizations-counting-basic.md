---
title: counting-principles
description: Two side-by-side animated panels show how counting works for (1) disjoint alternatives using the addition rule |A ∪ B| = |A| + |B| by revealing elements in sets A and B, and (2) sequential independent choices using the product rule |A × B| = |A| * |B| by filling a Cartesian-product grid of ordered pairs.
date: '2026-07-01'
scheduled: '2027-05-30'
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
inspiration_url: https://templeton.host/visualizations/counting-basic/
inspiration_category: visualizations
---

> Source-copy draft imported from [https://templeton.host/visualizations/counting-basic/](https://templeton.host/visualizations/counting-basic/). Names, domain references, and local media paths were adapted for Xavi Ablaza / getablaza.com.

[← ~/visualizations](/visualizations/)

# counting-principles

Two side-by-side animated panels show how counting works for (1) disjoint alternatives using the addition rule |A ∪ B| = |A| + |B| by revealing elements in sets A and B, and (2) sequential independent choices using the product rule |A × B| = |A| \* |B| by filling a Cartesian-product grid of ordered pairs.

canvasclick to interact

⏮◀◀▶▶STEP0.25x1xZOOM

t=0s

## practical uses

- 01.Counting outcomes with either/or choices (e.g., choose soup OR salad options)
- 02.Counting multi-step configurations (e.g., password format: 3 digits then 2 letters)
- 03.Estimating combinations in UI flows (e.g., A/B test variants across multiple independent toggles)

## technical notes

Uses time-based stepping to reveal elements (discrete counting) and a scanning fill to build the Cartesian product grid. Blocky look comes from snapped coordinates and square “dot” markers; colors follow GREEN/GREEN\_DIM on black with a subtle grid. Mode alternates every 4s to focus attention on one rule at a time.

[← expected-value](/visualizations/expected-value/)[variance →](/visualizations/variance/)
