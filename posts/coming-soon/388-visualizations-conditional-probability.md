---
title: conditional-probability
description: 'Shows conditional probability as restricting the sample space to event B on a grid of equally likely outcomes. The animation cycles through: the full universe, highlighting B, highlighting the overlap A∩B, and then reading P(A|B) as the fraction of B that lies in A. A final beat emphasizes the requirement P(B) > 0 by shrinking the visual B region.'
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
permalink: /visualizations/conditional-probability/
---

[← ~/visualizations](/visualizations/)

# conditional-probability

Shows conditional probability as restricting the sample space to event B on a grid of equally likely outcomes. The animation cycles through: the full universe, highlighting B, highlighting the overlap A∩B, and then reading P(A|B) as the fraction of B that lies in A. A final beat emphasizes the requirement P(B) > 0 by shrinking the visual B region.

canvasclick to interact

⏮◀◀▶▶STEP0.25x1xZOOM

t=0s

## practical uses

- 01.Medical testing: probability of disease given a positive test (P(D|+))
- 02.Spam filtering: probability an email is spam given certain features (P(Spam|words))
- 03.Reliability/monitoring: probability of failure given an alert condition (P(Failure|Alarm))

## technical notes

Renders a snapped grid of outcomes; A is a diagonal band, B is a rectangle, overlap is emphasized with a left-to-right sweep. Right panel shows formula and probability bars. Uses a 4.2s phase cycle with eased crossfades; includes an animated shrinking mask to illustrate the P(B)>0 condition.

[← linear-equations](/visualizations/linear-equations/)[systems-of-linear-equations →](/visualizations/linear-systems/)
