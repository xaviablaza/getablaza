---
title: channel-capacity
description: 'Visualizes a noisy channel as a probabilistic mapping p(y|x) (shown as a 2×2 transition matrix for a binary symmetric channel) and the channel capacity C as the maximum mutual information over input distributions: C = sup_{p(x)} I(X;Y). The lower plot animates I(X;Y) vs p(X=1) for the current noise level ε, highlighting the maximizing distribution and the capacity. A rate strip illustrates Shannon’s theorem: rates R<C are achievable while R>C are not reliably achievable.'
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
inspiration_url: https://templeton.host/visualizations/channel-capacity/
inspiration_category: visualizations
---

> Source-copy draft imported from [https://templeton.host/visualizations/channel-capacity/](https://templeton.host/visualizations/channel-capacity/). Names, domain references, and local media paths were adapted for Xavi Ablaza / getablaza.com.

[← ~/visualizations](/visualizations/)

# channel-capacity

Visualizes a noisy channel as a probabilistic mapping p(y|x) (shown as a 2×2 transition matrix for a binary symmetric channel) and the channel capacity C as the maximum mutual information over input distributions: C = sup\_{p(x)} I(X;Y). The lower plot animates I(X;Y) vs p(X=1) for the current noise level ε, highlighting the maximizing distribution and the capacity. A rate strip illustrates Shannon’s theorem: rates R<C are achievable while R>C are not reliably achievable.

canvasclick to interact

⏮◀◀▶▶STEP0.25x1xZOOM

t=0s

## practical uses

- 01.Choosing modulation/coding rates that remain below channel capacity for reliable links
- 02.Understanding why increasing SNR (lower ε) increases maximum throughput
- 03.Designing/benchmarking error-correcting codes against theoretical limits

## technical notes

Implements a Binary Symmetric Channel (BSC) so p(y|x) is easy to display and capacity is C=1−H2(ε). Mutual information is computed as I=H2(P(Y=1))−H2(ε) with P(Y=1)=ε+q(1−2ε). Animations sweep ε and the input bias q; blocky rendering uses grid snapping and simple chunky glyphs on a green-on-black palette.

[← combinations](/visualizations/combinations/)[sequence-masking-(causal-and-padding-masks) →](/visualizations/sequence-masking/)
