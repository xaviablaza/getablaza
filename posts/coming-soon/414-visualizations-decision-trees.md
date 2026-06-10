---
title: decision-trees
description: Visualizes a decision tree node evaluating multiple candidate splits by computing node impurity I(node) (Gini or Entropy), selecting the split with maximum impurity reduction ΔI, then routing sample “packets” down the chosen branch to leaf nodes that predict the majority class.
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
permalink: /visualizations/decision-trees/
---

[← ~/visualizations](/visualizations/)

# decision-trees

Visualizes a decision tree node evaluating multiple candidate splits by computing node impurity I(node) (Gini or Entropy), selecting the split with maximum impurity reduction ΔI, then routing sample “packets” down the chosen branch to leaf nodes that predict the majority class.

canvasclick to interact

⏮◀◀▶▶STEP0.25x1xZOOM

t=0s

## practical uses

- 01.Explaining how CART/ID3-style trees choose splits (information gain / Gini reduction)
- 02.Debugging/teaching why a particular split is preferred at a node
- 03.Building intuition for recursive partitioning and leaf majority-class prediction

## technical notes

3.6s animation cycle: (1) scan/evaluate split candidates, (2) highlight argmax ΔI, (3) animate sample packets flowing to children proportional to wL, (4) emphasize leaf prediction. Responsive scaling via scale=Math.min(w,h)/240, grid-snapped drawing for a retro blocky look, no external deps; impurity toggles between Gini and Entropy every two cycles.

[← balanced-trees](/visualizations/balanced-trees/)[equivalence-relations →](/visualizations/equivalence-relations/)
