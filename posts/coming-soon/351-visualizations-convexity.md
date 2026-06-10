---
title: convex-functions
description: 'Shows convexity two ways on a 1D slice: (top) the chord between (x,f(x)) and (y,f(y)) stays above the graph, so f(tx+(1-t)y) <= t f(x)+(1-t) f(y). (bottom) a moving tangent line at x0 supports the function from below, illustrating f(y) >= f(x0) + f''(x0)(y-x0). Animated points and vertical gaps make both inequalities visually explicit, highlighting their equivalence under differentiability.'
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
permalink: /visualizations/convexity/
---

[← ~/visualizations](/visualizations/)

# convex-functions

Shows convexity two ways on a 1D slice: (top) the chord between (x,f(x)) and (y,f(y)) stays above the graph, so f(tx+(1-t)y) <= t f(x)+(1-t) f(y). (bottom) a moving tangent line at x0 supports the function from below, illustrating f(y) >= f(x0) + f'(x0)(y-x0). Animated points and vertical gaps make both inequalities visually explicit, highlighting their equivalence under differentiability.

canvasclick to interact

⏮◀◀▶▶STEP0.25x1xZOOM

t=0s

## practical uses

- 01.Justifying why gradient-based methods work well on convex objectives (global minima)
- 02.Understanding Jensen’s inequality and averaging arguments in ML/statistics
- 03.Building intuition for supporting hyperplanes used in convex optimization and duality

## technical notes

Pure Canvas2D, green-on-black blocky rendering via grid snapping and pixel-stamped lines. Time-based animation cycles endpoints (x,y) and interpolation parameter t (0..1) over ~4s; a second sweep animates the supporting-line test point. Uses a smooth strongly convex polynomial f(x)=0.28x^2+0.10x^4 with analytic derivative for the tangent.

[← what-is-an-algorithm](/visualizations/algorithm-concept/)[principal-component-analysis →](/visualizations/pca/)
