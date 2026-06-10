---
title: rlhf
description: 'Visualizes the RLHF pipeline as a looping 3-step process: (1) humans provide preference comparisons (A vs B) that train a reward model r_phi, (2) r_phi converts policy samples into scalar rewards used as the RL return, and (3) the policy pi_theta is updated (PPO-style) while a KL(pi_theta || pi_ref) term keeps it close to the pretrained reference policy pi_ref to reduce drift.'
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
permalink: /visualizations/rlhf/
---

[← ~/visualizations](/visualizations/)

# rlhf

Visualizes the RLHF pipeline as a looping 3-step process: (1) humans provide preference comparisons (A vs B) that train a reward model r\_phi, (2) r\_phi converts policy samples into scalar rewards used as the RL return, and (3) the policy pi\_theta is updated (PPO-style) while a KL(pi\_theta || pi\_ref) term keeps it close to the pretrained reference policy pi\_ref to reduce drift.

canvasclick to interact

⏮◀◀▶▶STEP0.25x1xZOOM

t=0s

## practical uses

- 01.Aligning language model behavior with human preferences
- 02.Stabilizing fine-tuning with a reference policy (KL regularization)
- 03.Explaining why RLHF uses a learned reward model instead of direct human labels at scale

## technical notes

Pure Canvas2D, time-based loop (~4.2s). Blocky green-on-black UI with dashed-flow arrows. PPO objective panel plus a simple discrete distribution overlay to illustrate drift and a KL meter driven by simulated mean-shift. Includes auto-cycling tooltips to mimic interactivity without external input hooks.

[← equivalence-relations](/visualizations/equivalence-relations/)[conjugate-gradient-methods →](/visualizations/conjugate-gradients/)
