---
title: Graphs Introduction
description: Nodes (vertices) and edges connecting them. Directed vs undirected.
date: '2026-07-01'
scheduled: '2026-09-02'
tags:
- p-and-l-engineering
- coming-soon
- tech-tree
layout: layouts/post.njk
templateEngineOverride: md
image: /img/xavi-linkedin-profile.jpg
draft: true
generated_by: templeton-deep-copy-import
source_format: html
inspiration_url: https://templeton.host/tech-tree/graphs-basic/
inspiration_category: tech-tree
---

> Source-copy draft imported from [https://templeton.host/tech-tree/graphs-basic/](https://templeton.host/tech-tree/graphs-basic/). Names, domain references, and local media paths were adapted for Xavi Ablaza / getablaza.com.

[←Back to Tech Tree](/tech-tree/)

[inventory](/tech-tree/inventory/)[coverage](/tech-tree/coverage/)

# Graphs Introduction

Graph TheoryDifficulty: ★☆☆☆☆Depth: 1Unlocks: 18

Nodes (vertices) and edges connecting them. Directed vs undirected.

## Interactive Visualization

⏮◀◀▶▶STEP0.25x1xZOOM

t=0s

## Core Concepts

- -Vertex (node): a single element of a graph
- -Edge: a connection between vertices
- -Directed vs undirected: whether an edge has orientation (ordered) or not (unordered)

## Key Symbols & Notation

G = (V, E): graph specified by vertex set V and edge set E

## Essential Relationships

- -An edge connects two vertices: edges are pairs of vertices (ordered pair for directed edges, unordered pair for undirected edges)

## Prerequisites (1)

[Sets6 atoms](/tech-tree/sets-basic/)

## Unlocks (2)

[Graph Representationslvl 2](/tech-tree/graph-representations/)[Treeslvl 2](/tech-tree/trees/)

## Referenced by (1)

Where this concept shows up in the operating-finance and personal-finance graphs.

### From Business (1)

[Chart of AccountsBusiness

The concept explicitly frames the chart of accounts as a directed graph - parent accounts point to children, value flows along edges - making graph theory the precise mathematical foundation for the 'walk the edges' analysis it prescribes](/business/chart-of-accounts/)

Advanced Learning Details

### Graph Position

11

Depth Cost

18

Fan-Out (ROI)

10

Bottleneck Score

1

Chain Length

### Cognitive Load

5

Atomic Elements

26

Total Elements

L0

Percentile Level

L3

Atomic Level

### All Concepts (10)

- - graph: a mathematical object consisting of a set of vertices and a set of edges
- - vertex (node): an individual element/point in a graph
- - edge: an object that connects two vertices
- - undirected edge: an edge with no orientation (connection is symmetric)
- - directed edge (arc): an edge with orientation from one vertex to another
- - edge endpoints (incidence): the one or two vertices that an edge connects
- - adjacency: the notion that two vertices are connected by an edge
- - source and target (or tail and head): the roles of vertices in a directed edge
- - self-loop: an edge that connects a vertex to itself
- - ordered pair as a representation for directed edges

### Teaching Strategy

Self-serve tutorial - low prerequisites, straightforward concepts.

When you model “things and relationships”—friends in a social network, pages linked on the web, cities connected by roads—you’re already thinking in graphs. Graphs give a simple language for turning real-world connections into something you can reason about and compute on.

TL;DR:

A graph is a pair G = (V, E) where V is a set of vertices (nodes) and E is a set of edges (connections). In an undirected graph, edges are unordered pairs {u, v}. In a directed graph, edges are ordered pairs (u, v) that point from u to v. This lesson builds the basic vocabulary so you can describe and analyze network-like structures precisely.

## What Is a Graph?

### Why graphs matter

Many problems aren’t about a single object—they’re about **relationships** between objects.

- •In a **social network**, people are objects; friendships are relationships.
- •In a **map**, intersections are objects; roads are relationships.
- •In a **program dependency graph**, files/modules are objects; “imports” are relationships.

Graphs are the mathematical tool for expressing these situations with minimal assumptions.

### Formal definition

A **graph** is written as:

**G = (V, E)**

- •**V** is a set of **vertices** (also called **nodes**).
- •**E** is a set of **edges** that connect vertices.

Since you already know sets, you can think of a graph as “two sets packaged together”: a set of things (V) and a set of connections (E).

### A first concrete example

Let

- •V = {A, B, C, D}
- •E = {{A, B}, {B, C}, {A, D}}

Then G = (V, E) describes 4 vertices, with three undirected connections.

You can already ask meaningful questions:

- •Is there a connection between A and C? (Not directly.)
- •Can A reach C by hopping across edges? (Yes: A–B–C.)

Notice what we did not need:

- •No coordinates like in geometry
- •No equations like in algebra
- •Just sets and membership (∈)

### Terminology: “node” vs “vertex”, “edge” vs “link”

Different fields prefer different words:

| Common term | Graph theory term | Meaning |
| --- | --- | --- |
| node | vertex | an element of V |
| link/connection | edge | an element of E |

In this node, we’ll use **vertex** and **edge**, but remember the synonyms.

### What graphs do *not* automatically include

A basic graph definition doesn’t automatically assume:

- •weights (like distance or cost)
- •labels beyond vertex names
- •directions
- •multiple edges between the same two vertices

Those are all extensions. Here, we’ll focus on the most standard intro: **simple directed and undirected graphs**.

## Vertices and Edges (The Building Blocks)

### Vertices: the “things”

A **vertex** is a single entity. Formally, it’s just an element v ∈ V.

Because V is a set, vertices are **distinct** objects. That means you don’t have two different vertices that are both literally “A” inside the same set.

Example:

- •V = {0, 1, 2, 3} could represent four computers.
- •V = {Paris, Tokyo, Nairobi} could represent cities.

The symbols don’t matter; the structure comes from edges.

### Edges: the “relationships”

An **edge** says that two vertices are connected in some way.

But “connected” depends on the graph type:

- •In an **undirected** graph, an edge is an **unordered pair** of vertices.
- •In a **directed** graph, an edge is an **ordered pair** of vertices.

We’ll unpack that carefully, because it’s the core distinction in this lesson.

### Undirected edges as unordered pairs

In an **undirected graph**, an edge between u and v is written:

- •{u, v}

Because sets are unordered:

- •{u, v} = {v, u}

So the edge does not “point” anywhere. It just says “u and v are connected.”

If G is an undirected graph:

- •E ⊂ {{u, v} : u ∈ V, v ∈ V, u ≠ v}

That expression reads: E is a subset of all possible two-vertex sets from V (excluding self-loops for a simple graph).

### Directed edges as ordered pairs

In a **directed graph** (often called a **digraph**), an edge is written:

- •(u, v)

Now order matters:

- •(u, v) ≠ (v, u) in general

Interpretation: the edge goes **from u to v**.

Formally, if G is directed, we typically have:

- •E ⊂ V × V

where V × V is the Cartesian product (all ordered pairs).

### A quick comparison table

| Feature | Undirected graph | Directed graph |
| --- | --- | --- |
| Edge notation | {u, v} | (u, v) |
| Order matters? | no | yes |
| Symmetry implied? | yes: u connected to v implies v connected to u | no: (u, v) does not imply (v, u) |
| Common examples | friendship, roads (two-way) | follows on social media, one-way streets, prerequisites |

### Neighbors and adjacency (informal but essential)

Two vertices are **adjacent** (or **neighbors**) if they share an edge.

- •Undirected: u and v are adjacent if {u, v} ∈ E.
- •Directed: u is adjacent to v if (u, v) ∈ E (sometimes we specify “out-neighbor”).

This simple idea—who is adjacent to whom—will later become the basis for graph representations like adjacency lists and adjacency matrices.

### Degree: how many edges touch a vertex

Graphs invite “local counting” questions.

**Undirected degree**

The **degree** of a vertex v, written deg(v), is the number of edges incident to v (edges that touch v).

Example: If E = {{A, B}, {A, C}, {A, D}}, then deg(A) = 3.

**Directed degree**

In directed graphs, edges have direction, so we split degree into:

- •**out-degree** deg⁺(v): number of edges leaving v
- •**in-degree** deg⁻(v): number of edges entering v

Example: If E = {(A, B), (A, C), (D, A)}, then:

- •deg⁺(A) = 2 (A → B, A → C)
- •deg⁻(A) = 1 (D → A)

Degree is not just vocabulary: it’s often a first signal of “important” nodes (high degree) or bottlenecks (nodes with special in/out patterns).

### A small but important boundary: self-loops and multi-edges

In many introductory settings, we assume a **simple graph**:

- •no self-loop edges like {v, v} or (v, v)
- •no multiple identical edges between the same vertices

But in real systems you might allow them:

- •a webpage linking to itself (self-loop)
- •multiple flights between the same cities (multi-edges)

Those lead to **multigraphs**. For this node, keep the simple case in mind unless stated otherwise.

## Directed vs Undirected: The Core Mechanic

### Why this distinction is fundamental

The biggest modeling choice you make with graphs is whether relationships are mutual.

- •Friendship is usually mutual: if A is friends with B, B is friends with A.
- •“Follows” on many platforms is not mutual: A can follow B without B following A.

This choice changes what questions make sense.

- •In undirected graphs, “Can I get from u to v?” is symmetric.
- •In directed graphs, reachability can be one-way.

### Same vertices, two different meanings

Suppose V = {A, B}.

- •Undirected: E = {{A, B}} means A connected to B and B connected to A (the same statement).
- •Directed: E = {(A, B)} means A → B, but not necessarily B → A.

If you want mutual connection in a directed graph, you must include both edges:

- •E = {(A, B), (B, A)}

### Thinking in sets: what exactly is E?

It helps to explicitly name what kind of elements E contains.

**Undirected:**

- •Elements of E look like {u, v}
- •These are 2-element sets (unordered)

**Directed:**

- •Elements of E look like (u, v)
- •These are ordered pairs

So the same symbol “edge” hides two different underlying data types.

### Paths (a gentle preview)

Even before full algorithms, you can define a **path** informally:

- •A path is a sequence of vertices where each consecutive pair is connected by an edge.

Undirected example:

- •A–B–C is a path if {A, B} ∈ E and {B, C} ∈ E.

Directed example:

- •A → B → C is a directed path if (A, B) ∈ E and (B, C) ∈ E.

This is where direction matters:

- •In an undirected graph, A–B–C implies C–B–A is also a path.
- •In a directed graph, A → B → C does *not* imply C → B → A.

### Converting between directed and undirected models

Sometimes you’re given one type but want the other.

1) **Forget direction** (make an undirected version)

Given a directed graph G = (V, E), define an undirected edge {u, v} whenever at least one of (u, v) or (v, u) is in E.

This is useful when direction is noise or when you care only about whether there is any connection.

2) **Add direction** (make a directed version)

Given an undirected graph, you can replace each {u, v} with two directed edges (u, v) and (v, u).

This is useful when your algorithms are written for digraphs but the relationship is mutual.

### A note on notation with vectors

In this lesson, you might see vectors like **v** in later graph topics (e.g., representing vertices as indices, or adjacency vectors). Here, vertices are usually symbols like u, v, w (scalars in notation), not vectors. We’ll reserve **v** for actual vectors in later nodes.

## Applications and Connections (How Graphs Show Up in CS)

### Why computer science loves graphs

Graphs are a universal “data structure for relationships.” Once you can describe something as G = (V, E), many standard tools become available:

- •traversal (visit nodes systematically)
- •connectivity and components
- •shortest paths
- •dependency ordering

This node is about vocabulary, but it’s worth seeing where it leads.

### Common modeling patterns

| Scenario | Vertices (V) | Edges (E) | Directed? |
| --- | --- | --- | --- |
| Social network friendships | people | friendships | usually undirected |
| Social media “follows” | accounts | follow links | directed |
| Road network | intersections/cities | roads | depends (two-way vs one-way) |
| Web graph | web pages | hyperlinks | directed |
| Course prerequisites | courses | “is prerequisite of” | directed |
| Computer network | devices | cables/connections | often undirected; can be directed for routing policies |

### How this enables representations

To run algorithms, you must store a graph in memory.

Two classic representations are:

- •**Adjacency list**: for each vertex, list its neighbors
- •**Adjacency matrix**: a 2D table indicating whether an edge exists between i and j

Those are the focus of the next node: [Graph Representations](/tech-tree/graph-representations/).

### How this connects to trees

A **tree** is a special kind of graph (informally: connected and without cycles). If you understand vertices and edges, you can define trees precisely and see why they’re useful for hierarchy and recursion.

That’s the next major structure unlocked by this node: [Trees](/tech-tree/trees/).

### Mental checklist when someone says “graph”

Before you do anything else, ask:

1) What are the vertices, exactly?

2) What does an edge mean in the real world?

3) Is the relationship directed or undirected?

4) Are self-loops or multiple edges allowed?

5) Do edges have weights or labels? (not in this node, but often later)

Getting these answers early prevents confusion later.

## Worked Examples (3)

### Build G = (V, E) from a story (Undirected)

Four people {Ava, Ben, Chen, Dia}. Friendships: Ava is friends with Ben and Dia. Ben is friends with Chen. (Friendship is mutual.) Write the graph G = (V, E) and compute deg(Ava), deg(Ben).

1. Identify the vertex set:

   V = {Ava, Ben, Chen, Dia}
2. Translate each friendship into an undirected edge (unordered pair):

   Ava–Ben becomes {Ava, Ben}

   Ava–Dia becomes {Ava, Dia}

   Ben–Chen becomes {Ben, Chen}
3. Collect edges into the edge set:

   E = {{Ava, Ben}, {Ava, Dia}, {Ben, Chen}}
4. Write the graph as a pair:

   G = (V, E)
5. Compute degrees by counting incident edges:

   - •deg(Ava) = 2 because {Ava, Ben} and {Ava, Dia} touch Ava
   - •deg(Ben) = 2 because {Ava, Ben} and {Ben, Chen} touch Ben

**Insight:** The graph definition is just careful bookkeeping with sets. The modeling choice “friendship is mutual” forces undirected edges.

### Directed vs undirected edges change reachability

Let V = {A, B, C}. Consider two graphs on the same vertices:

G₁ (undirected): E₁ = {{A, B}, {B, C}}

G₂ (directed): E₂ = {(A, B), (B, C)}

In each graph, is there a path from C to A?

1. For G₁ (undirected), edges are unordered:

   {A, B} means A—B and B—A are effectively the same connection.

   {B, C} means B—C and C—B are also connected.
2. Check C to A in G₁:

   C—B is allowed because {B, C} ∈ E₁.

   B—A is allowed because {A, B} ∈ E₁.

   So a path exists: C–B–A.
3. For G₂ (directed), edges are ordered:

   (A, B) is A → B.

   (B, C) is B → C.
4. Check C to A in G₂:

   From C, there are no outgoing edges listed (no edge of the form (C, ·)).

   So you cannot start a directed path leaving C.

   Therefore, no directed path exists from C to A.
5. Optionally, note the reverse direction:

   In G₂ there is a directed path from A to C: A → B → C.

**Insight:** Direction turns “connectedness” into a one-way notion. In directed graphs, you must follow arrow orientation; in undirected graphs, every edge is traversable both ways.

### Compute in-degree and out-degree in a digraph

Let V = {1, 2, 3, 4} and E = {(1, 2), (1, 3), (3, 2), (4, 1)}. Compute deg⁺(1), deg⁻(1), deg⁺(2), deg⁻(2).

1. List outgoing edges from each requested vertex:

   Edges leaving 1 are (1, 2) and (1, 3).

   So deg⁺(1) = 2.
2. List incoming edges to 1:

   The only edge entering 1 is (4, 1).

   So deg⁻(1) = 1.
3. Outgoing edges from 2:

   Look for edges of the form (2, x). None appear.

   So deg⁺(2) = 0.
4. Incoming edges to 2:

   Edges entering 2 are (1, 2) and (3, 2).

   So deg⁻(2) = 2.

**Insight:** In directed graphs, “how connected” splits into two different questions: how many edges leave vs how many arrive. Many algorithms (like ranking or flow) depend on this split.

## Key Takeaways

- ✓

  A graph is defined as G = (V, E) with V a set of vertices and E a set of edges.
- ✓

  Undirected edges are unordered pairs {u, v}, so {u, v} = {v, u}.
- ✓

  Directed edges are ordered pairs (u, v), so (u, v) ≠ (v, u) in general.
- ✓

  Adjacency means “connected by an edge”; in directed graphs you often distinguish out-neighbors vs in-neighbors.
- ✓

  Degree counts incident edges; in directed graphs it splits into out-degree deg⁺(v) and in-degree deg⁻(v).
- ✓

  Most early graph questions (paths, reachability, connectivity) depend critically on whether edges are directed.
- ✓

  Before solving a graph problem, clarify what vertices represent, what edges represent, and whether the graph is directed.

## Common Mistakes

- ✗

  Treating directed edges as if they were undirected (assuming (u, v) implies (v, u)).
- ✗

  Mixing up edge notation: writing {u, v} for a directed edge or (u, v) for an undirected one without stating intent.
- ✗

  Forgetting that in a simple graph you typically exclude self-loops (v, v) and duplicate edges unless explicitly allowed.
- ✗

  Confusing degree in a directed graph: using a single deg(v) without specifying in-degree vs out-degree.

## Practice

easy

Let V = {a, b, c, d} and E = {{a, b}, {b, c}, {c, d}} (undirected). (1) Write G = (V, E). (2) Compute deg(b) and deg(d). (3) Is there a path from a to d?

**Hint:** Degree counts edges touching the vertex. A path can hop along consecutive edges.

Show solution

(1) G = (V, E) with V = {a, b, c, d} and E = {{a, b}, {b, c}, {c, d}}.

(2) deg(b) = 2 because {a, b} and {b, c} touch b. deg(d) = 1 because only {c, d} touches d.

(3) Yes: a–b–c–d is a path since each consecutive pair is an edge.

medium

Let V = {A, B, C}. Consider the directed graph with E = {(A, B), (B, A), (B, C)}. (1) Compute deg⁺(B) and deg⁻(B). (2) Is there a directed path from C to A?

**Hint:** Out-degree: edges starting at B. In-degree: edges ending at B. For a path from C, you need an edge leaving C.

Show solution

(1) Edges leaving B: (B, A), (B, C), so deg⁺(B) = 2. Edges entering B: (A, B), so deg⁻(B) = 1.

(2) No. There are no edges of the form (C, x), so C has out-degree 0 and cannot start a directed path to A.

easy

You are modeling airline flights between cities. For each pair of cities u and v, there may be a flight u → v without necessarily having v → u. Should your graph be directed or undirected? Write a one-sentence justification, then describe what V and E represent.

**Hint:** Ask whether the relationship is inherently one-way or two-way.

Show solution

Directed. A flight from u to v does not imply a flight from v to u.

V is the set of cities, and E is the set of directed edges (u, v) representing an available flight from city u to city v.

## Connections

- •Next: [Graph Representations](/tech-tree/graph-representations/) (how to store E efficiently as adjacency lists/matrices)
- •Next: [Trees](/tech-tree/trees/) (a special class of graphs with strong structure)
- •Related foundation: Sets and Cartesian products (V × V) for understanding directed edge sets

Quality: A (4.6/5)

[← back to tree](/tech-tree/)[browse all →](/tech-tree/inventory/)
