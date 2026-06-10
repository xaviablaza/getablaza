---
title: embeddings-(dense-representations)
description: 'Shows embeddings as a learned table of parameter vectors: a one-hot index selects a row v_x (lookup), and the chosen vectors live in a geometric space where semantic relatedness is measured by dot products and distances. The animation cycles through tokens, highlighting the selected embedding row and then visualizing similarity to another token in 2D with meters for v_x · v_y and ||v_x−v_y||.'
date: '2026-07-01'
scheduled: '2027-08-26'
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
inspiration_url: https://templeton.host/visualizations/embeddings-dense-representations/
inspiration_category: visualizations
---

> Source-copy draft imported from [https://templeton.host/visualizations/embeddings-dense-representations/](https://templeton.host/visualizations/embeddings-dense-representations/). Names, domain references, and local media paths were adapted for Xavi Ablaza / getablaza.com.

[← ~/visualizations](/visualizations/)

# embeddings-(dense-representations)

Shows embeddings as a learned table of parameter vectors: a one-hot index selects a row v\_x (lookup), and the chosen vectors live in a geometric space where semantic relatedness is measured by dot products and distances. The animation cycles through tokens, highlighting the selected embedding row and then visualizing similarity to another token in 2D with meters for v\_x · v\_y and ||v\_x−v\_y||.

canvasclick to interact

⏮◀◀▶▶STEP0.25x1xZOOM

t=0s

## practical uses

- 01.Token/word embeddings in NLP models (lookup table parameters)
- 02.Measuring semantic similarity via inner products (retrieval, clustering)
- 03.Understanding how attention consumes embedding vectors as inputs

## technical notes

Responsive layout using scale = min(w,h)/240 with 6px-ish grid snapping for a blocky aesthetic. Animation cycle (~3.6s) splits into lookup and similarity phases; the active row is subtly nudged toward a moving target during lookup to imply learning/parameter updates. Similarity uses 2D dot product and Euclidean distance with on-canvas meters.

[← eigenvalues-and-eigenvectors](/visualizations/eigenvalues/)[complexity-classes →](/visualizations/complexity-classes/)
