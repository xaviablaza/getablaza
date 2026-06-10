---
title: softmax-and-logits
description: Visualizes logits as raw class scores, then shows how softmax exponentiates and normalizes them into probabilities. The animation cycles through adding a constant shift (showing invariance), a naive exponentiation step that can overflow, and the numerically-stable log-sum-exp trick (subtracting max logit) while keeping the resulting probabilities unchanged.
date: '2026-07-01'
scheduled: '2027-07-19'
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
inspiration_url: https://templeton.host/visualizations/softmax-and-logits/
inspiration_category: visualizations
---

> Source-copy draft imported from [https://templeton.host/visualizations/softmax-and-logits/](https://templeton.host/visualizations/softmax-and-logits/). Names, domain references, and local media paths were adapted for Xavi Ablaza / getablaza.com.

[← ~/visualizations](/visualizations/)

# softmax-and-logits

Visualizes logits as raw class scores, then shows how softmax exponentiates and normalizes them into probabilities. The animation cycles through adding a constant shift (showing invariance), a naive exponentiation step that can overflow, and the numerically-stable log-sum-exp trick (subtracting max logit) while keeping the resulting probabilities unchanged.

canvasclick to interact

⏮◀◀▶▶STEP0.25x1xZOOM

t=0s

## practical uses

- 01.Interpreting classifier outputs: logits vs probabilities (confidence)
- 02.Computing attention weights in transformers via softmax over similarity scores
- 03.Implementing stable cross-entropy / softmax for training without numerical overflow

## technical notes

Three-column blocky panel: logits -> exp & sum -> probabilities. Animation cycles every ~3.6s through 4 conceptual steps; a global shift c(t) demonstrates softmax invariance, and step 4 computes stable softmax via subtracting max. Bars are grid-snapped for a retro aesthetic; exp bars use log scaling to stay drawable.

[← task-discretization](/visualizations/task-discretization/)[positional-encoding →](/visualizations/positional-encoding/)
