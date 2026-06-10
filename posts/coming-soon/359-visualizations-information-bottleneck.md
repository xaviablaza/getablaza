---
title: information-bottleneck
description: Visualizes the Information Bottleneck trade-off by animating a Markov chain Y → X → T with a cycling β parameter. As β increases, the bottleneck T expands its effective capacity (more filled slots) and more “relevant” information packets flow from T to Y; as β decreases, fewer packets and a tighter T emphasize compression. Side meters show the changing balance between I(X;T) (capacity/complexity) and I(T;Y) (relevance/predictiveness).
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
source_format: html
inspiration_url: https://templeton.host/visualizations/information-bottleneck/
inspiration_category: visualizations
---

> Source-copy draft imported from [https://templeton.host/visualizations/information-bottleneck/](https://templeton.host/visualizations/information-bottleneck/). Names, domain references, and local media paths were adapted for Xavi Ablaza / getablaza.com.

[← ~/visualizations](/visualizations/)

# information-bottleneck

Visualizes the Information Bottleneck trade-off by animating a Markov chain Y → X → T with a cycling β parameter. As β increases, the bottleneck T expands its effective capacity (more filled slots) and more “relevant” information packets flow from T to Y; as β decreases, fewer packets and a tighter T emphasize compression. Side meters show the changing balance between I(X;T) (capacity/complexity) and I(T;Y) (relevance/predictiveness).

canvasclick to interact

⏮◀◀▶▶STEP0.25x1xZOOM

t=0s

## practical uses

- 01.Designing representation learning objectives that trade off compression and prediction (e.g., IB, variational IB)
- 02.Explaining why larger latent capacity can improve downstream task performance when relevance is prioritized
- 03.Teaching the Markov constraint Y–X–T and how β tunes the compression–relevance balance

## technical notes

Uses time-based cycling (3.6s) to animate β with provided cubic ease(). Packets are simple snapped rectangles moving along two paths; T’s capacity is shown as a 3×2 slot grid with fill count driven by β. All geometry is responsive via scale=Math.min(w,h)/240 with 4–8px snapping for a blocky aesthetic.

[← vector-spaces](/visualizations/vector-spaces/)[graph-coloring →](/visualizations/graph-coloring/)
