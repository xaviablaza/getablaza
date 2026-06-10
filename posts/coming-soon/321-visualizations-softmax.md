---
title: softmax-function
description: Raw logits converted to probabilities via softmax. Shows how relative differences become probability distribution.
date: '2026-07-01'
scheduled: '2027-05-17'
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
inspiration_url: https://templeton.host/visualizations/softmax/
inspiration_category: visualizations
---

> Source-copy draft imported from [https://templeton.host/visualizations/softmax/](https://templeton.host/visualizations/softmax/). Names, domain references, and local media paths were adapted for Xavi Ablaza / getablaza.com.

[← ~/visualizations](/visualizations/)

# softmax-function

Raw logits converted to probabilities via softmax. Shows how relative differences become probability distribution.

canvasclick to interact

⏮◀◀▶▶STEP0.25x1xZOOM

t=0s

## practical uses

- 01.Teaching classification outputs
- 02.Explaining probability normalization
- 03.Visualizing temperature effects
- 04.Demonstrating attention weights

## technical notes

4-element logit vector. Softmax computed with max subtraction for stability. Probabilities shown as percentages.

[← entropy](/visualizations/entropy/)[dot-product →](/visualizations/dot-product/)
