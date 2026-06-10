---
title: complexity-classes
description: 'Visualizes the set relationships P ⊆ NP, plus the definitions of NP-hard and NP-complete using an animated reduction “funnel” (<=_p) that shows many NP problems reducing to a highlighted NP-complete target. Steps cycle through: P inside NP, certificate verification for NP, reductions defining NP-completeness, and NP-hardness extending beyond NP.'
date: '2026-07-01'
scheduled: '2027-08-27'
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
inspiration_url: https://templeton.host/visualizations/complexity-classes/
inspiration_category: visualizations
---

> Source-copy draft imported from [https://templeton.host/visualizations/complexity-classes/](https://templeton.host/visualizations/complexity-classes/). Names, domain references, and local media paths were adapted for Xavi Ablaza / getablaza.com.

[← ~/visualizations](/visualizations/)

# complexity-classes

Visualizes the set relationships P ⊆ NP, plus the definitions of NP-hard and NP-complete using an animated reduction “funnel” (<=\_p) that shows many NP problems reducing to a highlighted NP-complete target. Steps cycle through: P inside NP, certificate verification for NP, reductions defining NP-completeness, and NP-hardness extending beyond NP.

canvasclick to interact

⏮◀◀▶▶STEP0.25x1xZOOM

t=0s

## practical uses

- 01.Explaining why NP-complete problems are considered “representative hardest” problems in NP
- 02.Teaching polynomial-time reductions (<=\_p) as a way to compare problem difficulty
- 03.Clarifying the difference between NP-hard and NP-complete (outside vs inside NP)

## technical notes

Uses a 4-step timed narrative (1.2s per step) with cubic easing for highlights. Particles animate along a central reduction arrow to reinforce the “every NP problem reduces to it” idea. All geometry is snapped to a grid for a blocky aesthetic and scales with scale = min(w,h)/baseSize.

[← embeddings-(dense-representations)](/visualizations/embeddings-dense-representations/)[measure-theory →](/visualizations/measure-theory/)
