---
title: np-completeness
description: 'Shows polynomial-time many-one reductions (<=_p) as moving “instance packets” along arrows: NP problems reduce to SAT (Cook–Levin), SAT reduces to 3-SAT, and NP-completeness as (in NP) + (every NP problem reduces to it). Final phase illustrates the key consequence: if A <=_p B and B is in P, then A would also be in P - polynomial-time solvability propagates backward through reductions.'
date: '2026-07-01'
scheduled: '2027-07-31'
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
inspiration_url: https://templeton.host/visualizations/np-completeness/
inspiration_category: visualizations
---

> Source-copy draft imported from [https://templeton.host/visualizations/np-completeness/](https://templeton.host/visualizations/np-completeness/). Names, domain references, and local media paths were adapted for Xavi Ablaza / getablaza.com.

[← ~/visualizations](/visualizations/)

# np-completeness

Shows polynomial-time many-one reductions (<=\_p) as moving “instance packets” along arrows: NP problems reduce to SAT (Cook–Levin), SAT reduces to 3-SAT, and NP-completeness as (in NP) + (every NP problem reduces to it). Final phase illustrates the key consequence: if A <=\_p B and B is in P, then A would also be in P - polynomial-time solvability propagates backward through reductions.

canvasclick to interact

⏮◀◀▶▶STEP0.25x1xZOOM

t=0s

## practical uses

- 01.Designing hardness proofs by chaining known reductions (e.g., SAT -> 3-SAT -> your problem).
- 02.Reasoning about what it would mean to find a polynomial-time algorithm for an NP-complete problem (it would imply P=NP).
- 03.Classifying new problems as NP-complete by verifying NP membership and proving universal hardness via reductions.

## technical notes

Single 4.2s cycle with 4 stages; eased motion of a blocky “packet” represents the instance transformation. Grid-snapped coordinates create a retro block aesthetic; subtle background grid and panel text are drawn with monospace fonts; all rendering uses the Canvas 2D API with provided GREEN/GREEN\_DIM constants.

[← network-flow](/visualizations/network-flow/)[bayesian-inference →](/visualizations/bayesian-inference/)
