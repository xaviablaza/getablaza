---
title: meta-learning
description: 'Visualizes MAML-style meta-learning as a repeating cycle: sample a task from a task distribution, perform a few inner-loop gradient steps that adapt θ to θ′ using only a small task dataset (few-shot), then run an outer-loop meta-update that nudges shared meta-parameters θ to minimize the post-adaptation loss L_T(θ′) across tasks.'
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
permalink: /visualizations/meta-learning/
---

[← ~/visualizations](/visualizations/)

# meta-learning

Visualizes MAML-style meta-learning as a repeating cycle: sample a task from a task distribution, perform a few inner-loop gradient steps that adapt θ to θ′ using only a small task dataset (few-shot), then run an outer-loop meta-update that nudges shared meta-parameters θ to minimize the post-adaptation loss L\_T(θ′) across tasks.

canvasclick to interact

⏮◀◀▶▶STEP0.25x1xZOOM

t=0s

## practical uses

- 01.Few-shot personalization (adapt quickly to a new user/device with little data)
- 02.Fast adaptation for robotics/control tasks with varying dynamics
- 03.Hyperparameter/initialization learning for rapid fine-tuning across many domains

## technical notes

Blocky green-on-black panels show (left) task distribution, (center) parameter space with θ→θ′ step trail, and (right) loss before/after adaptation. Animation cycles every ~4.2s with discrete inner steps and a smooth outer meta-update; θ is stored in a closure and updated only during the outer-loop segment.

[← computational-graphs](/visualizations/computational-graphs/)[residual-(skip)-connections →](/visualizations/residual-connections/)
