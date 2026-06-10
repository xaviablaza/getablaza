---
title: expected-value
description: 'Shows expected value as a probability-weighted average (highlighting one term x·P(x) at a time) and as the long-run average: a running sample mean from repeated draws converges toward the theoretical E[X]. A bottom panel animates linearity by varying constants a and b and displaying E[aX+b] = aE[X]+b.'
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
permalink: /visualizations/expected-value/
---

[← ~/visualizations](/visualizations/)

# expected-value

Shows expected value as a probability-weighted average (highlighting one term x·P(x) at a time) and as the long-run average: a running sample mean from repeated draws converges toward the theoretical E[X]. A bottom panel animates linearity by varying constants a and b and displaying E[aX+b] = aE[X]+b.

canvasclick to interact

⏮◀◀▶▶STEP0.25x1xZOOM

t=0s

## practical uses

- 01.Evaluating games of chance and making fair-bet decisions
- 02.Estimating average outcomes in A/B tests or simulations (Monte Carlo)
- 03.Computing expected cost/latency in systems with probabilistic behavior

## technical notes

Deterministic per-cycle sampling uses a simple xorshift32 PRNG so the animation is stable. The right panel plots the running mean approaching a fixed E[X] line; the left panel cycles a highlighted x·P(x) term. Layout scales with canvas size using scale=Math.min(w,h)/240 and snap-to-grid rounding for a blocky aesthetic.

[← functions](/visualizations/functions-basic/)[counting-principles →](/visualizations/counting-basic/)
