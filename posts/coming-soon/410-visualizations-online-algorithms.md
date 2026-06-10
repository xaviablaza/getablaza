---
title: online-algorithms
description: 'Visualizes the online decision model using a streaming-day scenario (ski rental): input arrives day by day, the online algorithm must commit (rent vs BUY) without future knowledge, while OPT is a clairvoyant offline benchmark that knows the stopping day T. The animation alternates adversarial stopping times to show worst-case behavior and displays the competitive inequality and the resulting cost/OPT ratio against a highlighted competitive bound c.'
date: '2026-07-01'
scheduled: '2027-08-14'
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
inspiration_url: https://templeton.host/visualizations/online-algorithms/
inspiration_category: visualizations
---

> Source-copy draft imported from [https://templeton.host/visualizations/online-algorithms/](https://templeton.host/visualizations/online-algorithms/). Names, domain references, and local media paths were adapted for Xavi Ablaza / getablaza.com.

[← ~/visualizations](/visualizations/)

# online-algorithms

Visualizes the online decision model using a streaming-day scenario (ski rental): input arrives day by day, the online algorithm must commit (rent vs BUY) without future knowledge, while OPT is a clairvoyant offline benchmark that knows the stopping day T. The animation alternates adversarial stopping times to show worst-case behavior and displays the competitive inequality and the resulting cost/OPT ratio against a highlighted competitive bound c.

canvasclick to interact

⏮◀◀▶▶STEP0.25x1xZOOM

t=0s

## practical uses

- 01.Designing caching/paging strategies (LRU/FIFO) under unknown future requests
- 02.Ski-rental style buy-vs-rent decisions (cloud reservations, equipment leasing)
- 03.Analyzing scheduling/queueing policies with adversarial or worst-case arrivals

## technical notes

Implements a deterministic ski-rental instance with buy cost B and online threshold k=B. Each animation cycle reveals the input stream up to an adversarially chosen stop day T, then compares ONLINE cost vs OPT with animated bars and a ratio dial. Uses grid snapping for a blocky aesthetic, green-on-black palette, and time-based easing for smooth transitions.

[← optimization-introduction](/visualizations/optimization-intro/)[mutual-information →](/visualizations/mutual-information/)
