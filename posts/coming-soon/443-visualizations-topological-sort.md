---
title: topological-sort
description: 'Visualizes topological sorting on a DAG using Kahn’s algorithm: nodes with indegree 0 light up as the current frontier, one is selected each step and appended to the growing linear order. A second panel shows a directed cycle where the frontier becomes empty, illustrating that a topological ordering exists iff the graph is acyclic.'
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
permalink: /visualizations/topological-sort/
---

[← ~/visualizations](/visualizations/)

# topological-sort

Visualizes topological sorting on a DAG using Kahn’s algorithm: nodes with indegree 0 light up as the current frontier, one is selected each step and appended to the growing linear order. A second panel shows a directed cycle where the frontier becomes empty, illustrating that a topological ordering exists iff the graph is acyclic.

canvasclick to interact

⏮◀◀▶▶STEP0.25x1xZOOM

t=0s

## practical uses

- 01.Build systems / task scheduling (compile steps before dependents)
- 02.Course prerequisite planning
- 03.Dependency resolution in package managers and pipelines

## technical notes

Two side-by-side panels. Left panel simulates Kahn’s algorithm with discrete steps (~650ms) and smooth easing for highlights; edges fade when their source is removed. Right panel draws a cyclic graph with a moving token along the cycle and shows that no indegree-0 frontier exists. All drawing uses a snapped 4px grid for a blocky aesthetic and GREEN/GREEN\_DIM on black.

[← mechanism-design](/visualizations/mechanism-design/)[jacobian →](/visualizations/jacobian/)
