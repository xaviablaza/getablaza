---
title: markov-decision-processes
description: 'Visualizes an MDP decision epoch: a highlighted state selects an action via a (stochastic) policy π(a|s), transitions to next states according to P(s''|s,a) with immediate rewards r, then performs a Bellman backup Q(s,a)=E[r]+γE[V(s'')]. The final stage morphs from policy evaluation (expectation under π) to Bellman optimality (max over actions).'
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
permalink: /visualizations/mdp/
---

[← ~/visualizations](/visualizations/)

# markov-decision-processes

Visualizes an MDP decision epoch: a highlighted state selects an action via a (stochastic) policy π(a|s), transitions to next states according to P(s'|s,a) with immediate rewards r, then performs a Bellman backup Q(s,a)=E[r]+γE[V(s')]. The final stage morphs from policy evaluation (expectation under π) to Bellman optimality (max over actions).

canvasclick to interact

⏮◀◀▶▶STEP0.25x1xZOOM

t=0s

## practical uses

- 01.Reinforcement learning (policy evaluation and value iteration)
- 02.Robotics/control: planning under uncertainty with discounted rewards
- 03.Operations research: sequential decisions like inventory, routing, scheduling

## technical notes

Time-based 3.8s loop with eased segments (decision→transition→backup→optimality). Blocky grid-snapped drawing (4px\*scale) on black with GREEN/GREEN\_DIM. γ is shown as a pulsing bar; transitions display P and r labels; backup panel shows expected terms and an animated target value; optimality panel compares action-values and highlights argmax.

[← second-order-optimization](/visualizations/second-order-methods/)[concentration-inequalities →](/visualizations/concentration-inequalities/)
