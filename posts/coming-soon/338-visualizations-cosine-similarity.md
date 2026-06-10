---
title: cosine-similarity
description: Shows two vectors a and b on a 2D grid. Vector b rotates through negative to positive alignment while its length changes, demonstrating that cosine similarity depends on direction (angle θ) rather than magnitude. The dot product is visualized as b’s projection onto a, and a side panel displays dot(a,b), norms, and the normalized cosine similarity with a live [-1,1] meter.
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
source_format: html
inspiration_url: https://templeton.host/visualizations/cosine-similarity/
inspiration_category: visualizations
---

> Source-copy draft imported from [https://templeton.host/visualizations/cosine-similarity/](https://templeton.host/visualizations/cosine-similarity/). Names, domain references, and local media paths were adapted for Xavi Ablaza / getablaza.com.

[← ~/visualizations](/visualizations/)

# cosine-similarity

Shows two vectors a and b on a 2D grid. Vector b rotates through negative to positive alignment while its length changes, demonstrating that cosine similarity depends on direction (angle θ) rather than magnitude. The dot product is visualized as b’s projection onto a, and a side panel displays dot(a,b), norms, and the normalized cosine similarity with a live [-1,1] meter.

canvasclick to interact

⏮◀◀▶▶STEP0.25x1xZOOM

t=0s

## practical uses

- 01.Attention scoring in transformers (query·key / ||q|| ||k||) as a direction-based match
- 02.Comparing embedding vectors in search/retrieval and recommendation systems
- 03.Measuring document similarity in TF-IDF / bag-of-words vector spaces

## technical notes

Time-based animation rotates b across ±150° and modulates ||b|| to emphasize magnitude-independence. Uses grid snapping for a retro blocky look, polyline arcs for circle/angle, and a projection segment to connect dot product to geometric interpretation.

[← gradients](/visualizations/gradients/)[divide-and-conquer →](/visualizations/divide-conquer/)
