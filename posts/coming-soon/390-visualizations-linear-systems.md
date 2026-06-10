---
title: systems-of-linear-equations
description: Visualizes a system of linear equations as an augmented matrix [A | b] and animates Gaussian elimination via elementary row operations (swap/scale/add). The current pivot and affected row are highlighted, while a side panel explains the active row operation and a rank(A) vs rank([A|b]) test indicates whether the system is consistent (has solutions) and whether the solution is unique or infinite.
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
inspiration_url: https://templeton.host/visualizations/linear-systems/
inspiration_category: visualizations
---

> Source-copy draft imported from [https://templeton.host/visualizations/linear-systems/](https://templeton.host/visualizations/linear-systems/). Names, domain references, and local media paths were adapted for Xavi Ablaza / getablaza.com.

[← ~/visualizations](/visualizations/)

# systems-of-linear-equations

Visualizes a system of linear equations as an augmented matrix [A | b] and animates Gaussian elimination via elementary row operations (swap/scale/add). The current pivot and affected row are highlighted, while a side panel explains the active row operation and a rank(A) vs rank([A|b]) test indicates whether the system is consistent (has solutions) and whether the solution is unique or infinite.

canvasclick to interact

⏮◀◀▶▶STEP0.25x1xZOOM

t=0s

## practical uses

- 01.Solving circuit equations (Kirchhoff’s laws) by converting to Ax=b and eliminating
- 02.Fitting models / least-squares setups where linear constraints are solved or analyzed for consistency
- 03.Detecting whether constraints in engineering/optimization are compatible (consistent) and whether a solution is unique

## technical notes

Uses a small built-in set of 3×3 example systems (unique/infinite/none), computes a row-echelon sequence with recorded row operations, then interpolates between consecutive steps for smooth animation. Blocky aesthetic uses grid snapping and green-on-black palette; rank is inferred from echelon-form nonzero rows to demonstrate rank(A)=rank([A|b]) consistency.

[← conditional-probability](/visualizations/conditional-probability/)[mcmc →](/visualizations/mcmc/)
