---
title: residual-(skip)-connections
description: 'Shows a residual block where the input x splits into two paths: an identity shortcut (x) and a residual branch F(x). The branches merge at an elementwise addition node to produce y = F(x) + x. Animated “signal packets” travel forward along both paths and flash at the + node to emphasize summation, while a small backprop panel illustrates stronger gradient flow with the skip connection versus attenuation without it. A hint reinforces the residual-mapping view: the block learns the delta (y − x), making identity solutions easy.'
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
inspiration_url: https://templeton.host/visualizations/residual-connections/
inspiration_category: visualizations
---

> Source-copy draft imported from [https://templeton.host/visualizations/residual-connections/](https://templeton.host/visualizations/residual-connections/). Names, domain references, and local media paths were adapted for Xavi Ablaza / getablaza.com.

[← ~/visualizations](/visualizations/)

# residual-(skip)-connections

Shows a residual block where the input x splits into two paths: an identity shortcut (x) and a residual branch F(x). The branches merge at an elementwise addition node to produce y = F(x) + x. Animated “signal packets” travel forward along both paths and flash at the + node to emphasize summation, while a small backprop panel illustrates stronger gradient flow with the skip connection versus attenuation without it. A hint reinforces the residual-mapping view: the block learns the delta (y − x), making identity solutions easy.

canvasclick to interact

⏮◀◀▶▶STEP0.25x1xZOOM

t=0s

## practical uses

- 01.Training very deep networks (ResNets) without vanishing gradients
- 02.Transformer blocks: residual streams around attention and MLP sublayers
- 03.Stabilizing optimization and enabling easier identity/near-identity behavior during fine-tuning

## technical notes

Pure Canvas2D; time-based loop (~3.6s) with ease()-shaped phase ramps. Diagram elements are grid-snapped for a blocky aesthetic; animated packets move along piecewise-linear paths. A secondary panel uses simple animated bars to contrast gradient strength with/without a skip connection.

[← meta-learning](/visualizations/meta-learning/)[linear-independence →](/visualizations/linear-independence/)
