---
title: spectral-graph-theory
description: Shows a small graph whose adjacency (A) and degree (D) matrices combine into the Laplacian L = D − A. A pulsing “bridge” edge smoothly turns a disconnected graph into a connected one; the Laplacian eigenvalue bars update in real time to demonstrate that the number of near-zero eigenvalues matches the number of connected components, and that the second-smallest eigenvalue (algebraic connectivity λ1) becomes positive exactly when the graph is connected.
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
permalink: /visualizations/spectral-graph-theory/
---

[← ~/visualizations](/visualizations/)

# spectral-graph-theory

Shows a small graph whose adjacency (A) and degree (D) matrices combine into the Laplacian L = D − A. A pulsing “bridge” edge smoothly turns a disconnected graph into a connected one; the Laplacian eigenvalue bars update in real time to demonstrate that the number of near-zero eigenvalues matches the number of connected components, and that the second-smallest eigenvalue (algebraic connectivity λ1) becomes positive exactly when the graph is connected.

canvasclick to interact

⏮◀◀▶▶STEP0.25x1xZOOM

t=0s

## practical uses

- 01.Detecting connected components and connectivity from matrix spectra
- 02.Spectral clustering / graph partitioning via small Laplacian eigenvalues and eigenvectors
- 03.Analyzing diffusion, random walks, and network robustness using Laplacian properties

## technical notes

Uses a small (6×6) Laplacian and a lightweight Jacobi iteration to approximate eigenvalues each frame. The bridge edge is treated as a weighted adjacency entry so λ1 lifts smoothly during the animation. All drawing is grid-snapped for a retro blocky look with green-on-black styling.

[← bias-variance-tradeoff](/visualizations/bias-variance/)[proof-techniques →](/visualizations/proof-techniques/)
