---
title: clustering
description: 'Side-by-side visualization of two unsupervised clustering approaches. Left panel animates K-means: points are assigned to the nearest centroid (mu_j), then centroids move to the mean of their assigned points, reducing within-cluster sum of squared errors (SSE) shown as bars. Right panel animates hierarchical agglomerative clustering: a dendrogram is built by repeatedly merging the closest clusters under single-linkage, with the currently selected merge highlighted both in the dendrogram and on the point scatter plot.'
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
permalink: /visualizations/clustering/
---

[← ~/visualizations](/visualizations/)

# clustering

Side-by-side visualization of two unsupervised clustering approaches. Left panel animates K-means: points are assigned to the nearest centroid (mu\_j), then centroids move to the mean of their assigned points, reducing within-cluster sum of squared errors (SSE) shown as bars. Right panel animates hierarchical agglomerative clustering: a dendrogram is built by repeatedly merging the closest clusters under single-linkage, with the currently selected merge highlighted both in the dendrogram and on the point scatter plot.

canvasclick to interact

⏮◀◀▶▶STEP0.25x1xZOOM

t=0s

## practical uses

- 01.Customer/user segmentation from behavioral embeddings
- 02.Image/document grouping for exploration and search (unsupervised organization)
- 03.Anomaly detection by finding points far from any cluster centroid or that merge late in a dendrogram

## technical notes

Deterministic synthetic dataset and animations. K-means uses alternating assignment (nearest centroid) and centroid update (mean) with eased interpolation; SSE bars update each cycle (4.2s). Hierarchical clustering precomputes single-linkage agglomerative merges and draws them incrementally as a dendrogram; current merge is highlighted and also shown as a nearest cross-cluster point pair. Blocky aesthetic uses grid snapping (4px base) and a tiny 3x5 pixel font for labels.

[← support-vector-machines](/visualizations/svm/)[disjoint-sets →](/visualizations/disjoint-sets/)
