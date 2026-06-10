---
title: Your Chart of Accounts Is a Directed Graph
description: Every cost and revenue line is a node. Every causal relationship is an edge. Walk the graph and find the mispriced edges where value is leaking.
date: '2026-07-01'
scheduled: '2026-07-19'
tags:
- p-and-l-engineering
- coming-soon
- frameworks
layout: layouts/post.njk
templateEngineOverride: md
image: /img/xavi-linkedin-profile.jpg
draft: true
generated_by: templeton-deep-copy-import
source_format: html
inspiration_url: https://templeton.host/frameworks/directed-graph/
inspiration_category: frameworks
---

> Source-copy draft imported from [https://templeton.host/frameworks/directed-graph/](https://templeton.host/frameworks/directed-graph/). Names, domain references, and local media paths were adapted for Xavi Ablaza / getablaza.com.

[← Frameworks](/frameworks/)

# Your Chart of Accounts Is a Directed Graph

[Stage 1Find](/thesis/#stage-1)

Every business has a chart of accounts. Most people treat it as a flat list of categories. It is not. It is a directed graph - nodes are your cost and revenue lines, edges are causal relationships between business activities and financial outcomes. The goal is to find the **soft spots** - edges where value is leaking that no one has named yet.

3.2 touches/SKUMarketing spend - cost nodeMktg SpendSupport load - cost that erodes CSATSupportVendor data quality - upstream soft spotVendor DataPricing lever - cost driver into marginPricingPipeline volume - mechanismPipeline VolumeWin rate - mechanism driving ARRWin RateInventory - mechanismInventoryFulfillment - mechanism feeding CSATFulfillmentCSAT - mechanism, satisfaction scoreCSATMargin - mechanism feeding ARRMarginRework loop - soft spot mechanismRework LoopTime to market - downstream of reworkTime to MktAnnual recurring revenue - the outcomeARRExpansion revenue - outcomeExpansionChurn - cost outcome, negative feedbackChurnCostMechanismRevenueSoft spotNegative feedbackClick a node

Download PNGCopy ImageCopy SVGCopy URLEmbed

Click any node to trace its downstream causal path.

## The Model

A **node** is any line in your P&L that you can measure: a cost center, a revenue line, a conversion metric, a quality score.

An **edge** is a causal relationship: “onboarding friction delays time to value,” “support load erodes satisfaction,” “pipeline quality drives win rate.” These are not correlations. They are directional causes that propagate through your business.

A [soft spot](/lexicon/soft-spot/) is an edge where value is leaking and no one has named it yet. Every business has them. Most of the time, the people closest to the work already feel them - they just lack the language to surface them to leadership.

## Finding Soft Spots

The people closest to the work already know where the soft spots are. They feel them every day. They just lack the vocabulary to name them as edges in a graph that leadership can act on. Three questions surface them:

Question 1

Where do you lose the most time between receiving an input and producing an output?

Question 2

Which part of your process exists only because another part fails silently?

Question 3

If you had to cut one step and absorb the consequences, which step would cause the least damage?

Feed every response into the graph. Map each answer to a node or edge. The soft spots cluster. The highest-value intervention is usually sitting in the intersection of those answers.

## Why This Works

**Status quo:** A couple of key executives intuitively understand where value leaks in the business. They carry the map in their heads. When they leave, the map leaves with them. Most other people describe problems in their own local vocabulary - “onboarding is slow,” “support is overwhelmed” - without connecting those complaints to financial outcomes.

**The target state:** The graph gives the entire organization a shared language. When anyone - from a frontline rep to a VP - can say “there is a soft spot on the edge between onboarding friction and time to value,” that complaint becomes actionable. It maps to a node. It connects to a dollar amount. It can be prioritized.

The power of the directed graph is not the math. It is the **network effect of shared language**. Every person who learns to name edges and soft spots becomes a sensor for value leakage. The more people speak the language, the more signal leadership gets, and the faster the organization names the leaks that were hiding in plain sight.

## From Graph to Action

Once you find a soft spot, the [AI Operations Tools](/tools/) evaluate what to do about it:

DIAGNOSEPlot the task on the [Verification Quadrant](/tools/verification-quadrant/). Is this automatable? What is the Ablaza Ratio?

CALIBRATEUse the [Dollarized Confusion Matrix](/tools/dollarized-confusion-matrix/) to price the asymmetry. What does it cost to be wrong in each direction?

INVESTUse [Quadrant Shifting](/tools/quadrant-shifting/) to decide which capital investment moves this task to a better position.

VALUECalculate the [Automation NPV](/tools/automation-npv/) to know whether the investment pencils out before writing a line of code.

Thanks to [James Garvey](https://www.linkedin.com/in/jamesgarvey/) for encouraging me to formalize and publish these frameworks.

## Worked example: SKU ingestion at retail scale

In practice, this framework is how you find the mispriced edges. Walk the chart of accounts, look for edges where the implicit per-unit cost is radically higher than it ought to be, and that's where the AI capital is worth deploying.

A concrete example: SKU ingestion in a retail holding company. The edge connecting *vendor-provided-data* to *catalog-ready-SKU* had a tariff of roughly $11 per unit - a human operator touching each SKU, fixing spec sheets, reconciling attributes. The volume flowing over that edge was in the millions. The total implied cost made the edge one of the most expensive non-revenue-producing lines on the graph.

Deployed: an AI pipeline targeted specifically at that edge. Result: per-unit cost dropped to ~$0.90 (about 92%). No other edges touched. The framework predicted this ranking; the deployment confirmed it. That is what falsifiable looks like for a framework - the prediction has to match reality or the framework is wrong.

## When the graph model fails

The framework rests on a *falsifiable claim*: the edge with the largest mispricing is the edge where capital deployment produces the largest return. If that ranking is wrong in an environment, the framework is wrong for that environment.

- -**Path dependence dominates.** If attacking the largest edge requires upstream edges to be fixed first, the ranking lies about true leverage. Walk topologically, not just by magnitude.
- -**The graph is wrong.** If the chart of accounts hides the real causal structure (e.g., an activity-based cost is smeared across three GL lines), the edges are fiction. Rebuild the graph before ranking.
- -**The mispriced edge is mispriced for a reason.** Regulatory, contractual, or political constraints can make an edge untouchable. Kill it from the candidate set rather than ranking it.
- -**Correlated rework.** Fixing one edge can inflate adjacent edges (the classic "squeeze the balloon" problem). Score the neighborhood, not the single edge.

## Rosetta Stone

Four circles, four readings of the same object. Each role reads the artifact through its own lens.

[Allocator

The chart of accounts is a first-order approximation of your portfolio of operating investments. Each edge has a risk-adjusted return you can estimate or compute. The graph is the map of deployable capital.](/positions/allocator/)[Operator

A way to make the team's felt knowledge legible. Everyone knows where the bottlenecks are; the graph gives them names and a place on the wall. An audit trail of where value moves and where it stalls.](/positions/operator/)[Builder

A system diagram for the business. Nodes are services, edges are dependencies. The failing edges are where you should put your next PR.](/positions/builder/)[Scientist

A directed graph G=(V,E) of operating flows. The allocation problem is a vertex-weighted max-flow variant: select the edge improvements that maximize expected value under budget and correlation constraints.](/positions/scientist/)

See also: [Knowledge Work as Capital](/frameworks/knowledge-capital/) · [AI Operations Tools](/tools/) · [Lexicon](/lexicon/)
