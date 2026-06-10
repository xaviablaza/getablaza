---
title: reinforcement-learning-introduction
description: Visualizes a small Markov Decision Process (MDP) where an agent repeatedly samples actions from a stochastic policy pi(a|s), transitions to next states via P(s'|s,a), receives rewards, and incrementally updates value estimates V^pi(s) and action-values Q^pi(s,a). The animation shows the policy probabilities per state, the stochastic transition, reward signals, and the value backup target r + γ V(s').
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
permalink: /visualizations/rl-intro/
---

[← ~/visualizations](/visualizations/)

# reinforcement-learning-introduction

Visualizes a small Markov Decision Process (MDP) where an agent repeatedly samples actions from a stochastic policy pi(a|s), transitions to next states via P(s'|s,a), receives rewards, and incrementally updates value estimates V^pi(s) and action-values Q^pi(s,a). The animation shows the policy probabilities per state, the stochastic transition, reward signals, and the value backup target r + γ V(s').

canvasclick to interact

⏮◀◀▶▶STEP0.25x1xZOOM

t=0s

## practical uses

- 01.Build intuition for how an MDP generates experience (s,a,r,s')
- 02.Understand what a stochastic policy pi(a|s) means and how it affects behavior
- 03.See how value functions V^pi and Q^pi relate to long-run reward via bootstrapped backups

## technical notes

Self-contained Canvas2D draw function with persistent closure state. Uses a 4-state line-world MDP, stochastic transitions (intended vs slip), and simple TD(0)-style incremental updates for V and Q. Blocky 4px-snapped layout, green-on-black palette, and a ~0.9s step animation cycle with easing.

[← token-embeddings](/visualizations/token-embeddings/)[automatic-differentiation →](/visualizations/automatic-differentiation/)
