---
title: divide-and-conquer
description: Animated recursion tree showing the Divide→Conquer→Combine workflow. Blocks represent problem sizes shrinking as they split; highlights and moving flow markers show work moving down the tree (divide), leaf solutions being computed (conquer), and partial results flowing upward to merge into the final answer (combine). A panel ties correctness composition and cost composition to the visual tree via a recurrence.
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
inspiration_url: https://templeton.host/visualizations/divide-conquer/
inspiration_category: visualizations
---

> Source-copy draft imported from [https://templeton.host/visualizations/divide-conquer/](https://templeton.host/visualizations/divide-conquer/). Names, domain references, and local media paths were adapted for Xavi Ablaza / getablaza.com.

[← ~/visualizations](/visualizations/)

# divide-and-conquer

Animated recursion tree showing the Divide→Conquer→Combine workflow. Blocks represent problem sizes shrinking as they split; highlights and moving flow markers show work moving down the tree (divide), leaf solutions being computed (conquer), and partial results flowing upward to merge into the final answer (combine). A panel ties correctness composition and cost composition to the visual tree via a recurrence.

canvasclick to interact

⏮◀◀▶▶STEP0.25x1xZOOM

t=0s

## practical uses

- 01.Merge sort: split array, sort halves, merge
- 02.Quicksort: partition (divide), recurse, combine implicitly
- 03.Binary search / recursive search in trees and graphs

## technical notes

Pure Canvas2D, time-based 4.2s loop. Uses snapped grid coordinates for a blocky aesthetic; easing for flow markers; stage-driven highlighting to emphasize correctness (combine) and cost recurrence (divide). Responsive scaling via scale = min(w,h)/220.

[← cosine-similarity](/visualizations/cosine-similarity/)[confidence-intervals →](/visualizations/confidence-intervals/)
