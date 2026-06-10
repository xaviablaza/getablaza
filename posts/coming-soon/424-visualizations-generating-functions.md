---
title: generating-functions
description: 'Cycles through three linked views: (1) encoding a sequence a_n as an ordinary generating function A(x)=∑a_n x^n, (2) extracting a specific coefficient [x^n]A(x)=a_n with an animated scanner, and (3) showing how algebra on generating functions corresponds to sequence operations (index shift via x^k and convolution via the Cauchy product).'
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
permalink: /visualizations/generating-functions/
---

[← ~/visualizations](/visualizations/)

# generating-functions

Cycles through three linked views: (1) encoding a sequence a\_n as an ordinary generating function A(x)=∑a\_n x^n, (2) extracting a specific coefficient [x^n]A(x)=a\_n with an animated scanner, and (3) showing how algebra on generating functions corresponds to sequence operations (index shift via x^k and convolution via the Cauchy product).

canvasclick to interact

⏮◀◀▶▶STEP0.25x1xZOOM

t=0s

## practical uses

- 01.Solve counting problems by translating combinatorial constructions into algebraic equations in A(x).
- 02.Derive and solve linear recurrences with constant coefficients using rational generating functions.
- 03.Compute sequence convolutions (e.g., ways to combine independent choices) via multiplication of generating functions.

## technical notes

Uses a 3-scene time loop (~3.2s each). All geometry snaps to a 4px grid for a blocky aesthetic. Animations use time-based phases and the provided cubic ease(). No external state; pure Canvas 2D drawing with lightweight shapes and monospace text.

[← regularization](/visualizations/regularization/)[joint-distributions →](/visualizations/joint-distributions/)
