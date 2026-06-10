---
title: Lexicon
description: The operating vocabulary. Ablaza Ratio, Quality Ratchet, Oracle Gradient, and the language for treating knowledge work as a capital asset.
date: '2026-07-01'
scheduled: '2026-07-07'
tags:
- p-and-l-engineering
- coming-soon
- lexicon
layout: layouts/post.njk
templateEngineOverride: md
image: /img/xavi-linkedin-profile.jpg
draft: true
generated_by: templeton-deep-copy-import
source_format: html
inspiration_url: https://templeton.host/lexicon/
inspiration_category: lexicon
---

> Source-copy draft imported from [https://templeton.host/lexicon/](https://templeton.host/lexicon/). Names, domain references, and local media paths were adapted for Xavi Ablaza / getablaza.com.

[← Home](/)

# Lexicon

The operating vocabulary. Every term here was invented to name something that existed but didn't have a word for it. Grouped by stage of the allocation cycle - see the [thesis](/thesis/) for the full lattice.

Stage 1

## Find

· Where are the mispriced edges in the operating graph?

[### Soft Spot →

An edge in the directed graph of your business where value is leaking that no one has named yet. Identified by walking the graph and listening to the people closest to the work.

Directed GraphOperational AlphaDemand Gravity](/lexicon/soft-spot/)[### Operational Alpha →

Excess return on enterprise value generated through systematic identification and capture of mispriced edges in business operations. The operational equivalent of alpha in financial markets.

Directed GraphAI Operations ToolsSoft SpotConstruction Spread](/lexicon/operational-alpha/)[### Oracle Gradient →

The computed vector from your current performance toward the unobservable optimum in a domain's performance space. You never reach the oracle. You approach it. Each measurement sharpens your estimate of where it is.

The Performance FrontierQuality Ratchet](/lexicon/oracle-gradient/)[### Demand Gravity →

The inescapable pull of real demand on product trajectories. Demand is always there, always pulling, and you can't negotiate with it. Map it or crash into it.

The Demand FieldSoft SpotOperational Alpha](/lexicon/demand-gravity/)

Stage 2

## Characterize

· What is the return distribution of this opportunity?

[### Ablaza Ratio →

T = time\_to\_do / time\_to\_check. The ratio of generation difficulty to verification difficulty for any task. Determines whether AI automation creates leverage or doubles the work.

Verification QuadrantVerification TrapAI Sweet SpotProof Layer](/lexicon/templeton-ratio/)[### Verification Trap →

A task that is easy to generate but hard to verify. The AI produces output effortlessly, but checking whether it is correct takes as long as doing it manually. T approaches 1.

Verification QuadrantAblaza RatioAI Sweet SpotQuadrant Shifting](/lexicon/verification-trap/)[### AI Sweet Spot →

A task where generation is hard but verification is cheap. T >> 1. You can review 50 AI outputs in the time it takes to manually produce one. This is the P vs NP intuition applied to operations.

Verification QuadrantAblaza RatioVerification TrapQuadrant Shifting](/lexicon/ai-sweet-spot/)[### Dollarized Confusion Matrix →

A confusion matrix where counts are replaced with costs. The optimal threshold follows: theta\* = C\_FP / (C\_FP + C\_FN). Costs drive thresholds, thresholds drive autonomy levels.

Dollarized Confusion Matrix ToolVerification TrapAutonomy State Machine](/lexicon/dollarized-confusion-matrix/)[### Construction Spread →

S = (annual\_value x P(success)) / build\_cost. The risk-adjusted return on the capital deployed to build a knowledge asset. Rank opportunities by spread descending. Deploy capital top-down until budget is exhausted.

Automation NPVKnowledge CapitalCompile TimeDual CurveOperational Alpha](/lexicon/construction-spread/)[### Dual Curve →

The simultaneous depreciation of AI models (distribution shift, competitive erosion) and appreciation of knowledge assets (verifiers, labeled corpora, institutional rubrics) - where the appreciating side gets better through operating use, not in spite of it. The net rate determines whether an automation is a wasting asset or a compounder.

Knowledge CapitalVerifier CapitalAutomation NPVConstruction SpreadCompile Time](/lexicon/dual-curve/)

Stage 4

## Execute

· How do you realize the returns?

[### Proof Layer →

The verification rubric, asymmetry profile, and verification cost analysis built BEFORE the capability. Every AI system needs one. No exceptions.

Knowledge CapitalDollarized Confusion MatrixGold StandardAblaza Ratio](/lexicon/proof-layer/)[### Autonomy State Machine →

A graduated trust system for AI deployments with three states: Disabled, HITL (human verifies every output), and Autonomous (spot-check only). Transitions are driven by statistical evidence with hysteresis to prevent oscillation. See: The Promotion Protocol.

The Promotion ProtocolDollarized Confusion MatrixDrift DetectorGold Standard](/lexicon/autonomy-state-machine/)[### Quality Ratchet →

A CI-enforced floor that only moves up. Once a quality metric hits a threshold, the system blocks any change that drops below it. Each improvement becomes the new minimum. The sequence of baselines is monotonically non-decreasing. Formally: a monotonic ratchet.

Quality HillclimbDesigned ConvergenceGold StandardOracle Gradient](/lexicon/quality-ratchet/)[### Structured Elicitation →

A controlled experiment designed to learn the operator's preferences. Pairwise comparisons, best-worst scaling, or adaptive conjoint analysis. Highest information per query of the three Deity Problem channels, but requires operator attention.

The Deity ProblemRevealed PreferenceDirect QueryDrift Detector](/lexicon/structured-elicitation/)[### Revealed Preference →

Inferring the operator's preferences by watching what they actually do - not what they say they want. Based on revealed preference theory (Afriat's theorem, GARP). Cheapest evidence channel because the operator is doing what they would do anyway.

The Deity ProblemStructured ElicitationDirect Query](/lexicon/revealed-preference/)[### Direct Query →

A question posed to the operator, used only when the expected value of the answer exceeds the cost of the operator's attention. An agent that asks too many questions isn't diligent - it's poorly calibrated.

The Deity ProblemStructured ElicitationRevealed Preference](/lexicon/direct-query/)[### Drift Detector →

A posterior predictive check that detects when the operator's preferences have drifted from the learned model. Computed as the fraction of recent decisions the model predicted incorrectly. When the drift score exceeds a threshold, the agent triggers re-elicitation.

The Deity ProblemAutonomy State MachineStructured Elicitation](/lexicon/drift-detector/)[### The Designer's Seat →

The position of designing the game rather than playing it. Every multi-agent system is a game. You can optimize your moves within existing rules (playing), or you can choose the rules so that the equilibrium of self-interested behavior is your desired outcome (designing). The CTO's job is the second one.

Designed ConvergenceAutonomy State Machine](/lexicon/designers-seat/)

Stage 5

## Compound

· How do you build the appreciating asset?

[### Gold Standard →

A set of human-verified, ground-truth examples used to calibrate and evaluate AI output. The gold standard IS the verification instrument. Without it, you are measuring with a broken ruler.

Knowledge CapitalProof LayerQuality RatchetAutonomy State Machine](/lexicon/gold-standard/)[### Compile Time →

Time spent building systems, frameworks, rubrics, and processes that produce returns across many future periods. The ROI is multiplicative.

Knowledge CapitalRuntimeConstruction Spread](/lexicon/compile-time/)[### Runtime →

Time spent executing tasks, fighting fires, reviewing outputs, and attending meetings. Produces returns in a single period. Necessary but should not dominate a leader's schedule.

Knowledge CapitalCompile Time](/lexicon/runtime/)[### Quadrant Shifting →

Capital investments that move a task to a better position on the Verification Quadrant. Five moves: build a verifier, decompose the task, enrich inputs, constrain outputs, build a rubric.

Quadrant Shifting ToolVerification QuadrantAI Sweet SpotVerification TrapConstruction Spread](/lexicon/quadrant-shifting/)[### Verifier Capital →

A verifier is one of the only capital assets that appreciates through operating use. Every failure it catches gets encoded as a new rule, test, or rubric line, and the next run inherits the catch. Use raises the floor instead of lowering it.

The Capital Value of VerifiersKnowledge CapitalDual CurveAblaza RatioQuadrant ShiftingProof Layer](/lexicon/verifier-capital/)

See also: [Frameworks](/frameworks/) · [AI Operations Tools](/tools/)
