---
title: what-is-an-algorithm
description: Visualizes an algorithm as a finite, ordered procedure that transforms INPUT -> OUTPUT. A data token moves through the pipeline while the procedure box highlights steps (READ, PROCESS, WRITE) to show sequencing and transformation.
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
permalink: /visualizations/algorithm-concept/
---

[← ~/visualizations](/visualizations/)

# what-is-an-algorithm

Visualizes an algorithm as a finite, ordered procedure that transforms INPUT -> OUTPUT. A data token moves through the pipeline while the procedure box highlights steps (READ, PROCESS, WRITE) to show sequencing and transformation.

canvasclick to interact

⏮◀◀▶▶STEP0.25x1xZOOM

t=0s

## practical uses

- 01.Explaining the basic Input-Process-Output model to beginners
- 02.Introducing step-by-step reasoning before teaching specific algorithms (sorting/searching)
- 03.Demonstrating how data is transformed through well-defined, finite steps

## technical notes

Pure Canvas2D draw function with time-based loop (~3.6s). Uses responsive scaling, grid snapping for a blocky aesthetic, staged animation (input, procedure, output), and step highlighting synced to token movement. Colors use GREEN/GREEN\_DIM on black.

[← maximum-likelihood-estimation](/visualizations/mle/)[convex-functions →](/visualizations/convexity/)
