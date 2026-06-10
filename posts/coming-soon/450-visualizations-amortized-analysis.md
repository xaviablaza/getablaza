---
title: amortized-analysis
description: Visualizes amortized cost via the potential method using a dynamic array push sequence. Actual costs (including occasional resize-copy spikes) are shown alongside constant-ish amortized costs, while a potential “credit tank” Phi(S) stores and releases credit so that a_i = c_i + Phi(S_i) − Phi(S_{i−1}). The bottom panel shows the telescoping sum Σa_i = Σc_i + Phi(S_n) − Phi(S_0), illustrating how nonnegative potential bounds total actual work over the whole sequence.
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
permalink: /visualizations/amortized-analysis/
---

[← ~/visualizations](/visualizations/)

# amortized-analysis

Visualizes amortized cost via the potential method using a dynamic array push sequence. Actual costs (including occasional resize-copy spikes) are shown alongside constant-ish amortized costs, while a potential “credit tank” Phi(S) stores and releases credit so that a\_i = c\_i + Phi(S\_i) − Phi(S\_{i−1}). The bottom panel shows the telescoping sum Σa\_i = Σc\_i + Phi(S\_n) − Phi(S\_0), illustrating how nonnegative potential bounds total actual work over the whole sequence.

canvasclick to interact

⏮◀◀▶▶STEP0.25x1xZOOM

t=0s

## practical uses

- 01.Proving O(1) amortized push in dynamic arrays (vector/ArrayList growth)
- 02.Analyzing amortized bounds in stacks/queues (e.g., multipop, two-stack queue)
- 03.Reasoning about splay trees, union-find, and other data structures with occasional expensive operations

## technical notes

Time-driven 3.6s operation cycles; persistent closure state simulates a sequence of pushes with doubling resizes. Bars plot recent actual vs amortized costs; a blocky token animation illustrates paying c\_i and storing/spending ΔPhi. Uses snap-to-grid sizing for a retro aesthetic and ease() for smooth transitions.

[← norms](/visualizations/norms/)[linear-regression →](/visualizations/linear-regression/)
