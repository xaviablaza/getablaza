---
title: deep-learning
description: Visualizes a deep network as a layered composition f_θ(x)=f_L(...f_2(f_1(x))). Animated packets flow left-to-right through layer blocks, while each layer’s representation vector h^l lights up as features are transformed into higher-level abstractions. A cycling “inductive bias” panel switches between CNN (locality + weight sharing), RNN (recurrence), and Attention (global mixing), showing how architecture constrains which connections exist and thus which function families are parameter-efficient and generalize well.
date: '2026-07-01'
scheduled: '2027-07-17'
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
inspiration_url: https://templeton.host/visualizations/deep-learning/
inspiration_category: visualizations
---

> Source-copy draft imported from [https://templeton.host/visualizations/deep-learning/](https://templeton.host/visualizations/deep-learning/). Names, domain references, and local media paths were adapted for Xavi Ablaza / getablaza.com.

[← ~/visualizations](/visualizations/)

# deep-learning

Visualizes a deep network as a layered composition f\_θ(x)=f\_L(...f\_2(f\_1(x))). Animated packets flow left-to-right through layer blocks, while each layer’s representation vector h^l lights up as features are transformed into higher-level abstractions. A cycling “inductive bias” panel switches between CNN (locality + weight sharing), RNN (recurrence), and Attention (global mixing), showing how architecture constrains which connections exist and thus which function families are parameter-efficient and generalize well.

canvasclick to interact

⏮◀◀▶▶STEP0.25x1xZOOM

t=0s

## practical uses

- 01.Explaining why depth creates hierarchical feature representations (edges→parts→objects, etc.)
- 02.Comparing architectural inductive biases (CNN vs RNN vs Attention) at a conceptual level
- 03.Teaching forward-pass composition and intermediate activations h^l in deep models

## technical notes

Uses a 3.2s forward-pass phase for smooth highlighting across layers; packets are lightweight stateful elements updated with dt. Blocky aesthetic is enforced via grid snapping and strokeRect/fillRect primitives; bias modes change the rendered connection topology (local+shared kernels, recurrence loop, or global fan connections).

[← automatic-differentiation](/visualizations/automatic-differentiation/)[task-discretization →](/visualizations/task-discretization/)
