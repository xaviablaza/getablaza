---
title: cooperative-games
description: Visualizes coalition formation in a 3-player transferable-utility cooperative game. The animation cycles through all player orderings (permutations). As each player joins the current coalition S, the canvas shows v(S), v(S∪{i}), and the marginal contribution v(S∪{i})−v(S). On the right, each player’s Shapley value φ_i is shown as the average marginal contribution over orderings (exact, plus a running sample average that repeatedly converges).
date: '2026-07-01'
scheduled: '2027-07-11'
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
inspiration_url: https://templeton.host/visualizations/cooperative-games/
inspiration_category: visualizations
---

> Source-copy draft imported from [https://templeton.host/visualizations/cooperative-games/](https://templeton.host/visualizations/cooperative-games/). Names, domain references, and local media paths were adapted for Xavi Ablaza / getablaza.com.

[← ~/visualizations](/visualizations/)

# cooperative-games

Visualizes coalition formation in a 3-player transferable-utility cooperative game. The animation cycles through all player orderings (permutations). As each player joins the current coalition S, the canvas shows v(S), v(S∪{i}), and the marginal contribution v(S∪{i})−v(S). On the right, each player’s Shapley value φ\_i is shown as the average marginal contribution over orderings (exact, plus a running sample average that repeatedly converges).

canvasclick to interact

⏮◀◀▶▶STEP0.25x1xZOOM

t=0s

## practical uses

- 01.Fair profit/cost allocation in joint ventures (who gets how much of v(N))
- 02.Attributing value in ML feature attribution (Shapley-style explanations)
- 03.Revenue sharing and cost splitting for shared infrastructure or collaborations

## technical notes

Uses a fixed 3-player characteristic function v(S)=sum of singleton values + pair synergies + triple synergy (bitmask representation). Cycles through the 6 permutations; within each permutation, joining is eased and shown step-by-step. Exact Shapley values are precomputed by averaging marginal contributions over all permutations; a running average is updated once per permutation to visualize the expectation idea. Grid-snapped rectangles and monospace text create a blocky green-on-black aesthetic; layout scales with canvas size via scale=min(w,h)/240.

[← orthogonality](/visualizations/orthogonality/)[stochastic-gradient-descent →](/visualizations/sgd/)
