---
title: tries
description: Shows a trie (prefix tree) where each node represents the prefix formed by edge labels from the root. An animated cursor performs searches one character at a time by following child_map[char] edges, highlighting the active path and checking the terminal marker to decide whether the traversed prefix is a complete stored key.
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
permalink: /visualizations/tries/
---

[← ~/visualizations](/visualizations/)

# tries

Shows a trie (prefix tree) where each node represents the prefix formed by edge labels from the root. An animated cursor performs searches one character at a time by following child\_map[char] edges, highlighting the active path and checking the terminal marker to decide whether the traversed prefix is a complete stored key.

canvasclick to interact

⏮◀◀▶▶STEP0.25x1xZOOM

t=0s

## practical uses

- 01.Fast prefix lookups (autocomplete, typeahead)
- 02.Dictionary/word-set storage with O(k) search/insert for k-length strings
- 03.Routing/command parsing by incremental character traversal

## technical notes

Uses a prebuilt example trie (to/tea/ted/ten/in/inn). Layout is computed once via leaf ordering and averaging to place internal nodes. Animation cycles every 4s across several search queries; the cursor interpolates between nodes with cubic easing, and traversed edges/nodes are highlighted in GREEN with terminal nodes marked by a small square.

[← continuity](/visualizations/continuity/)[computational-graphs →](/visualizations/computational-graphs/)
