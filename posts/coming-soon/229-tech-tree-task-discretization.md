---
title: Task Discretization
description: Breaking continuous tasks into discrete, measurable subtasks for LLM systems.
date: '2026-07-01'
scheduled: '2026-06-10'
tags:
- p-and-l-engineering
- coming-soon
- tech-tree
layout: layouts/post.njk
templateEngineOverride: md
image: /img/xavi-linkedin-profile.jpg
draft: false
generated_by: templeton-deep-copy-import
source_format: html
inspiration_url: https://templeton.host/tech-tree/task-discretization/
inspiration_category: tech-tree
---

> Source-copy draft imported from [https://templeton.host/tech-tree/task-discretization/](https://templeton.host/tech-tree/task-discretization/). Names, domain references, and local media paths were adapted for Xavi Ablaza / getablaza.com.

[←Back to Tech Tree](/tech-tree/)

[inventory](/tech-tree/inventory/)[coverage](/tech-tree/coverage/)

# Task Discretization

Software EngineeringDifficulty: ★★★★★Depth: 10Unlocks: 0

Breaking continuous tasks into discrete, measurable subtasks for LLM systems.

## Interactive Visualization

⏮◀◀▶▶STEP0.25x1xZOOM

t=0s

## Core Concepts

- -Atomic subtask (tau): minimal, indivisible unit with explicit input/output interface and a verifiable completion criterion
- -Discretization mapping f: a mapping that segments continuous trajectories/states into an ordered sequence of atomic subtasks
- -Observable measurement: each atomic subtask produces a measurable signal (metric or reward) that confirms completion and enables learning

## Key Symbols & Notation

f - discretization mapping (continuous trajectory -> ordered sequence of subtask identifiers)

## Essential Relationships

- -Composability: ordered atomic subtasks (tau\_1,...,tau\_n) connected by their interfaces reconstruct or approximate the original continuous task when executed in sequence

## Prerequisites (5)

[Loss Functions7 atoms](/tech-tree/loss-functions/)[Markov Decision Processes6 atoms](/tech-tree/mdp/)[Mechanism Design11 atoms](/tech-tree/mechanism-design/)[Topological Sort5 atoms](/tech-tree/topological-sort/)[Bayesian Inference5 atoms](/tech-tree/bayesian-inference/)

## Referenced by (3)

Where this concept shows up in the operating-finance and personal-finance graphs.

### From Business (3)

[milestonesBusiness

Milestones are exactly task discretization applied to business strategy - breaking a continuous growth trajectory into discrete, measurable checkpoints that enable progress tracking and resource allocation decisions](/business/milestones/)[contract reviewBusiness

Contract review is a canonical example of breaking a continuous professional task into discrete, measurable subtasks (clause classification, term extraction, obligation mapping, risk scoring) for LLM automation](/business/contract-review/)[Workforce TransformationBusiness

Agent deployments require decomposing continuous workflows into discrete, measurable subtasks that LLM agents can execute - this is the mathematical foundation for operationalizing workforce transformation via AI agents](/business/workforce-transformation/)

Advanced Learning Details

### Graph Position

297

Depth Cost

0

Fan-Out (ROI)

0

Bottleneck Score

10

Chain Length

### Cognitive Load

5

Atomic Elements

57

Total Elements

L4

Percentile Level

L3

Atomic Level

### All Concepts (24)

- - Task discretization: the practice of converting a continuous or open-ended task into a sequence/tree of discrete subtasks.
- - Decomposer function: an explicit operator or procedure that maps a high-level task into subtasks and their dependencies.
- - Subtask: a discrete, scoped unit of work produced by decomposition (distinct from MDP state/action formalism).
- - Granularity: the chosen size/complexity of each subtask (how fine- or coarse-grained the discretization is).
- - Discretization error: the gap between the ideal continuous-task outcome and the outcome produced by assembling discrete subtasks.
- - Measurable subtask: a subtask that has an explicit, operational metric for success or quality.
- - Subtask interface/contract: the explicit input/output specification and preconditions/postconditions that enable composability.
- - Atomicity of a subtask: the property that a subtask is indivisible for the chosen decomposition (minimal reliable unit).
- - Abstraction level of a subtask: the semantic/detail depth at which a subtask is specified (higher abstraction = less detail).
- - Subtask dependency graph: a DAG or tree expressing ordering and data/control dependencies among subtasks.
- - Termination condition for a subtask: the concrete criterion used to decide when that subtask is complete.
- - Reconstruction/aggregation operator: the procedure that composes subtask outputs into a final task output.
- - Credit assignment across subtasks: distributing learning signals or loss to individual subtasks based on contribution.
- - Local measurability score: a quantitative indicator of how observable and evaluable a subtask's result is.
- - Interface idempotence/retryability: whether rerunning a subtask with the same inputs preserves global state and output.
- - Fidelity vs tractability trade-off: the tension between preserving task fidelity (low ε) and keeping subtasks tractable for LLMs.
- - Error propagation across subtasks: how individual subtask errors combine and amplify (or cancel) when aggregated.
- - Subtask-specific policy/prompting: designing distinct prompts, policies, or heuristics tailored to each subtask.
- - Subtask checkpointing and recovery: storing intermediate outputs/state to enable rollback, debugging, or recomputation.
- - Synchronous vs asynchronous subtask execution: whether subtasks run in strict order or can run concurrently/independently.
- - Subtask validation tests: unit-test-like checks applied to subtasks to ensure correctness before composition.
- - Aggregation-preserving decomposition: decompositions designed so that aggregation reconstructs the global objective within tolerance.
- - Designing incentive-aligned metrics: choosing subtask metrics so that optimizing subtasks drives the global objective.
- - Observable contract violation: detectable mismatches between actual subtask behavior and its declared contract.

### Teaching Strategy

Quick unlock - significant prerequisite investment but simple final step. Verify prerequisites first.

LLM systems often fail not because they can’t “think,” but because we ask them to complete a continuous, messy, real-world task without agreeing on the discrete checkpoints that count as progress. Task discretization is the craft of turning “do the thing” into an ordered list of verifiable, measurable subtasks that a system can plan, execute, evaluate, and learn from.

TL;DR:

Task discretization defines (1) atomic subtasks τ with explicit input/output and a completion test, (2) a mapping f that converts a continuous trajectory into an ordered sequence of τ identifiers, and (3) observable measurements (metrics/rewards) that certify completion and enable optimization. Done well, it turns ambiguous objectives into DAGs you can topologically sort, instrument, and improve with loss functions and inference.

## What Is Task Discretization?

### Why this concept exists

Real tasks are continuous in at least three senses:

1. 1)**State is continuous/huge**: The world has too many degrees of freedom (files, users, clocks, networks, policies).
2. 2)**Progress is continuous**: You can be “partway done,” but what does that mean operationally?
3. 3)**Success is fuzzy**: Stakeholders say “make it good,” “ship it,” “be safe,” “be fast,” “be correct.”

LLM-based systems struggle here because their execution model is discrete: they emit tokens, call tools, and produce artifacts. If we don’t discretize the task, we can’t reliably:

- •plan (what should happen next?),
- •verify (did we do it?),
- •learn (what reward/loss should change behavior?),
- •or assign responsibility across agents/tools.

Task discretization is the process of **breaking a continuous task** into **discrete, measurable subtasks**—small enough to verify, but structured enough to recombine into the full task.

### Core objects

You will use three central ideas.

#### 1) Atomic subtask (τ)

An **atomic subtask** τ is the smallest unit you treat as indivisible **for the purposes of orchestration and verification**.

Operationally, τ must have:

- •**Inputs**: what context/resources are allowed or required
- •**Outputs**: what artifact/state change is produced
- •**Completion criterion**: a test you can run to decide done/not done

Think of τ as a function-like interface:

- •Input: (prompt state, files, tool access, constraints)
- •Output: (patch, summary, decision, JSON, API call)
- •Validator: a programmatic or procedural check

A key subtlety: *atomic does not mean “simple.”* It means you **choose** not to further subdivide it because verification would not improve, or because the cost of decomposition outweighs the benefit.

#### 2) Discretization mapping f

Let a task unfold as a continuous trajectory. You can model this as a sequence of world states or observations over time:

- •s(t) for t ∈ [0, T]

Task discretization defines a mapping:

- •**f : (trajectory) → (τ₁, τ₂, …, τₙ)**

Here, f segments the continuous process into an ordered list of subtask identifiers.

In practice, f is not a single formula; it is a design artifact: rules, schemas, and policies for how you label segments as subtasks.

#### 3) Observable measurement

Each τ should produce an **observable measurement**—a signal that can be used for:

- •**verification** (pass/fail),
- •**scoring** (a metric),
- •or **reward shaping** (dense feedback for learning).

This measurement might be:

- •a unit test result,
- •a linter score,
- •a schema validation,
- •a human rubric score,
- •a latency/cost measurement,
- •a safety classifier decision,
- •or a formal proof check.

### Why discretization is hard (and why difficulty is 5/5)

At difficulty 5, the challenge is not “make a checklist.” It is designing subtasks that are:

- •**verifiable** without being trivial,
- •**composable** without creating hidden coupling,
- •**aligned** with the real objective (mechanism design issues),
- •**robust** to distribution shift,
- •and **instrumented** so learning is possible.

This is where your prerequisites connect:

- •**Loss functions**: translate measurements into optimization targets.
- •**MDPs**: treat subtasks as options / macro-actions; define transition structure.
- •**Mechanism design**: avoid Goodhart’s law by aligning incentives.
- •**Topological sort**: order subtasks respecting dependencies.
- •**Bayesian inference**: infer latent “done-ness” and uncertainty from noisy measurements.

### A unifying mental model

Task discretization is designing a bridge:

- •From **continuous intent** (what the user wants)
- •To **discrete execution** (what the system can do)
- •With **measured checkpoints** (what you can verify)

If you can’t measure progress, you can’t manage it. If you can’t define atomic units, you can’t orchestrate it. If you can’t define f, you can’t consistently map messy reality into actionable steps.

## Core Mechanic 1 — Designing Atomic Subtasks τ (Interfaces + Completion)

### Why atomic subtasks matter

LLM systems are brittle when they operate on large, ambiguous scopes. The typical failure mode is:

- •the model “half-solves” multiple things,
- •produces an artifact that is hard to validate,
- •and you can’t tell whether it’s wrong, incomplete, or mis-scoped.

Atomic subtasks create **bounded responsibility**: one τ owns one verifiable change.

### The τ design checklist

A high-quality τ can be specified as a quadruple:

- •τ = (I, O, C, M)

where:

- •I = **input contract**
- •O = **output contract**
- •C = **completion criterion** (boolean or thresholded)
- •M = **measurement(s)** (metrics/reward components)

You can think of C as a predicate:

- •C(I, O) ∈ {0, 1}

and M as a vector of measurements:

- •**m**(I, O) ∈ ℝᵏ

Even if you ultimately need a single scalar reward r, keeping **m** as a vector prevents premature scalarization.

### Input contracts: reduce degrees of freedom

If you do not constrain inputs, your system will “solve” tasks by changing assumptions.

Common input constraints:

- •allowed tools (search, filesystem, DB, deploy)
- •allowed files or directories
- •time budget, token budget, API cost budget
- •policy constraints (PII, safety rules)

An effective pattern is: **minimize the input surface** so the model cannot roam.

### Output contracts: force a concrete artifact

The output should be something you can store, diff, test, or validate.

Examples of output contracts:

- •JSON with a schema
- •a code patch (diff)
- •a SQL migration
- •a markdown report with required headings
- •a set of test cases

The output contract should also specify **format stability**: if downstream τ expects a field, it must exist.

### Completion criteria: from “looks good” to “provably done”

Completion criteria are where discretization becomes engineering.

Good criteria are:

- •**decidable** (you can run them)
- •**cheap** enough to run routinely
- •**correlated** with true success

Bad criteria are:

- •purely aesthetic
- •subjective without a rubric
- •or easy to game

A concrete completion criterion might be:

- •“All unit tests in suite S pass”
- •“JSON validates against schema v1”
- •“No P0 security findings in static scan”

When you can’t fully decide correctness (common in language tasks), you define:

- •a rubric R and a scoring function score\_R ∈ [0, 1]
- •and a threshold θ

Completion:

- •C = 1 ⇔ score\_R ≥ θ

### Measurements: designing **m** and then reward/loss

Measurements should include at least:

- •**quality** (correctness, relevance)
- •**safety** (policy compliance)
- •**cost** (latency, API calls)

Let **m** = (q, s, c) where:

- •q ∈ [0, 1] quality
- •s ∈ [0, 1] safety
- •c ≥ 0 cost

Then you might define a scalar reward:

- •r = w\_q q + w\_s s − w\_c c

But notice the mechanism design problem: if you set w\_c too high, the system may avoid necessary work.

### Atomicity is relative: choose the level that stabilizes verification

You can always split further. The question is: does splitting improve reliability?

A useful test:

- •If τ fails, can you diagnose *why* and *what to do next*?

If the answer is “no,” τ is likely too large.

### Composition: subtasks as a DAG

Subtasks rarely form a simple list. Most real work has dependencies.

Represent subtasks as nodes in a DAG:

- •edges τᵢ → τⱼ mean “τᵢ must complete before τⱼ starts”

Then your execution order can be found via **topological sort**.

This representation matters because it cleanly separates:

- •**logical dependency** (must happen before)
- •from **temporal scheduling** (can happen in parallel)

### Options viewpoint (MDP connection)

In MDP terms, an atomic subtask can be treated like an **option** (a temporally extended action):

- •it has an initiation set,
- •a policy (how the agent behaves while executing it),
- •and a termination condition (completion criterion C).

This helps when you want hierarchical control:

- •high-level planner chooses τ
- •low-level executor performs tool calls and token generation until C is satisfied

### A quick design table

| Design choice | Too coarse | Too fine | Target |
| --- | --- | --- | --- |
| τ scope | hard to verify; ambiguous failure | orchestration overhead; many handoffs | failures are diagnosable and recoverable |
| C strictness | false positives (“done” but wrong) | never completes | cheap, decisive, correlated |
| Measurements **m** | uninformative learning | noisy + overfitting | minimal set that predicts success |
| Output contract | hard to parse downstream | brittle format | stable schema + clear ownership |

The central skill is to balance verification power against coordination cost.

## Core Mechanic 2 — Building the Discretization Mapping f (Segmentation + Ordering + Uncertainty)

### Why you need f, not just “a list of steps”

If you build one checklist per task, you get a brittle system that fails when the task deviates slightly. The mapping f is a generalization: a policy for turning observations into a subtask sequence.

Formally, imagine a trajectory of observations o(t) and states s(t). Discretization produces indices:

- •f(o(·)) = (τ₁, τ₂, …, τₙ)

But in practice, the trajectory is only partially observed. You see:

- •user messages,
- •tool outputs,
- •repository state,
- •logs.

So f is really a mapping from **available evidence** to a plan of τ.

### Segmentation: where do subtasks begin and end?

Segmentation is deciding boundaries.

A boundary is justified when:

1. 1)The completion criterion changes (different validator).
2. 2)The artifact boundary changes (different output type).
3. 3)The responsible agent/tool changes.
4. 4)The risk profile changes (e.g., from analysis to execution).

A useful heuristic: boundaries should align with **observables**. If you can’t observe the boundary, you can’t enforce it.

### Ordering: sequences vs DAGs

Many tasks can be partially ordered.

Define a dependency relation ≺ such that:

- •τᵢ ≺ τⱼ means τᵢ must happen before τⱼ

Then a valid execution sequence is any linear extension of this partial order, obtainable by topological sort.

This yields two benefits:

- •Parallelization: independent subtasks can run concurrently.
- •Robust recovery: if one branch fails, others can proceed.

### The f design problem: two layers

In LLM systems, f often has two layers:

1. 1)**Task compiler** (static): from a task spec to a DAG template.
2. 2)**Task router** (dynamic): from current state to the next τ to attempt.

You can implement these with:

- •rules + schemas,
- •learned models (classifiers for “what next”),
- •or hybrid approaches.

### Making f robust: handle branch points explicitly

Continuous tasks have branch points:

- •missing data
- •failing tests
- •unclear requirements
- •conflicting constraints

If f does not model branch points, the system “hallucinates progress.”

Represent branch points as:

- •decision subtasks τ\_decide that output a discrete choice

Example output:

- •{ "decision": "ask\_user", "question": "…" }

Then downstream dependencies are conditioned on that output.

### Observable measurements and Bayesian inference

Measurements are noisy. For many subtasks, you cannot directly observe correctness—only proxies.

Let D be observed evidence (rubric scores, test results, lint warnings, reviewer ratings).

You care about a latent variable:

- •Z = “τ is truly complete and correct”

Bayesian framing:

- •P(Z = 1 | D) ∝ P(D | Z = 1) P(Z = 1)

This is useful when:

- •validators are imperfect,
- •humans disagree,
- •tests have limited coverage.

Instead of a hard completion decision, you can maintain a posterior and only advance when:

- •P(Z = 1 | D) ≥ 1 − δ

for a chosen risk tolerance δ.

### Reward shaping over discretized subtasks

If you define subtasks τᵢ with measurements **m**ᵢ, you can define an overall objective as a sum:

- •J = ∑ᵢ R(τᵢ)

where R(τᵢ) could be a scalar reward or negative loss.

But beware: **additivity is an assumption**. Some subtasks interact (coupling). Mechanism design tells you that optimizing local rewards can harm global success.

A safer pattern:

- •keep local rewards but periodically evaluate global objective G
- •and use G as a constraint or veto

Example:

- •maximize ∑ᵢ rᵢ
- •subject to G ≥ G\_min

### How discretization relates to mechanism design

When you turn a task into subtasks with metrics, you create a “game” the system plays.

- •The system is the agent.
- •Your metrics are the payoff.

If the metric is gameable, it will be gamed.

Common Goodhart failure:

- •You measure “number of tests added” ⇒ system adds meaningless tests.

Mechanism design response:

- •require tests to fail before fix,
- •measure mutation score,
- •measure coverage *and* fault detection.

In other words: design measurements so that the cheapest path to a high score is aligned with real success.

### A practical schema for f

A workable discretization mapping often looks like:

1. 1)**Normalize** the task into a structured spec (JSON): goals, constraints, resources.
2. 2)**Expand** into a DAG template of τ types.
3. 3)**Ground** each τ with concrete file paths, APIs, or data sources.
4. 4)**Execute** via a router that picks the next τ based on state.
5. 5)**Verify** each τ with validators; update posteriors.
6. 6)**Repair** failures by branching: retry, decompose, or ask for info.

The mapping f is thus an executable artifact: it turns the continuous process into discrete, monitorable units.

### A short comparison: rule-based vs learned f

| Approach | Strengths | Weaknesses | When to use |
| --- | --- | --- | --- |
| Rule-based f | predictable; auditable; cheap | brittle; coverage gaps | stable domains; compliance-heavy workflows |
| Learned f | adapts; handles variety | harder to debug; needs data | broad task diversity; many examples available |
| Hybrid | best of both if done well | integration complexity | production LLM systems with safety needs |

At difficulty 5, the key is not picking one, but designing interfaces so both can cooperate.

## Application/Connection — Task Discretization in LLM System Engineering

### Why discretization is a software engineering primitive

In production, you care about:

- •reliability (can we trust the outcome?)
- •latency and cost (how much does it cost to run?)
- •safety and compliance (can we prove constraints?)
- •debuggability (can we isolate failure?)

Task discretization supports all four by making the system observable and testable.

### Canonical application: LLM agent builds a feature

Suppose the continuous task is:

- •“Implement feature X in repo Y and deploy.”

A discretized plan might include τ like:

- •τ\_spec: extract acceptance criteria into structured format
- •τ\_scan: map codebase modules and ownership
- •τ\_design: propose minimal design + risk list
- •τ\_implement: produce code patch
- •τ\_test: run unit/integration tests
- •τ\_security: run SAST + dependency audit
- •τ\_review: produce PR description + rationale
- •τ\_deploy: perform staged rollout
- •τ\_monitor: check metrics for regressions

Each subtask has a validator:

- •schema validity, test pass, scan thresholds, canary success.

This turns “ship it” into a pipeline with explicit checkpoints.

### Instrumentation: from subtasks to observability traces

If each τ emits:

- •start/end timestamps
- •status (pass/fail)
- •measurements **m**
- •artifacts (links to outputs)

Then you can build a trace:

- •per-task timeline
- •per-τ failure rates
- •cost hotspots

This is the foundation for iterating on your system like any other software.

### Learning loops: improving f and τ over time

Once you have discrete units, you can learn at multiple levels:

1. 1)**Improve executor policies**: better prompting/tool use for a given τ.
2. 2)**Improve validators**: reduce false positives/negatives.
3. 3)**Improve f**: better decomposition and routing.

Because you have measurements, you can define losses.

Example: for a classifier that predicts next τ, cross-entropy loss:

- •L = −∑ᵢ ∑\_k yᵢk log pᵢk

where yᵢk is the one-hot target for the chosen τ\_k.

Example: for quality scoring regression, MSE:

- •L = (q̂ − q)²

### Hierarchical control and MDP abstraction

With subtasks, you can define a higher-level MDP where actions are τ.

Let S be the state summary (repo status, which τ done, key metrics). Let A be available subtasks.

Then policy π chooses:

- •τ ∼ π(τ | S)

The transition dynamics depend on executor behavior and environment, but your validators provide reward signals.

This is how “agentic workflows” become amenable to reinforcement learning or bandit optimization.

### Safety: discretization as a containment strategy

Many safety failures come from unconstrained action spaces.

Discretization helps by:

- •limiting tool access per τ,
- •requiring explicit approval gates for high-risk τ,
- •and forcing structured outputs.

Example: a τ that can modify production settings must have:

- •strict input contract (requires ticket ID)
- •completion criterion (change verified in read-only query)
- •and a human approval measurement

### A design pattern library (practical)

Below are common τ patterns used in LLM systems.

| Pattern | Output | Validator | Purpose |
| --- | --- | --- | --- |
| Extract | JSON fields | schema validation | turn text into structured spec |
| Decide | discrete label | consistency checks | branch control |
| Generate | artifact (code/text) | lint/tests/rubric | produce work product |
| Verify | pass/fail report | deterministic checks | guardrails |
| Summarize | structured summary | coverage checklist | state compression |
| Ask | question set | user response present | resolve uncertainty |

### When discretization fails: symptoms

- •High “done” rate but low user satisfaction (metrics misaligned).
- •Frequent retries on the same τ (τ too large or validator too strict).
- •Many handoffs with little progress (τ too small; orchestration overhead).
- •Silent failures (no observable measurement; missing instrumentation).

### What you should be able to do after this node

- •Define τ with explicit I/O and completion criteria.
- •Build a DAG of τ and topologically sort it.
- •Specify f as a task compiler + router.
- •Design measurement vectors **m** and map them to losses/rewards.
- •Anticipate gaming via mechanism design.
- •Use Bayesian reasoning to manage uncertain completion.

This is the core engineering discipline behind scalable agent workflows.

## Worked Examples (3)

### Worked Example 1 — Discretize “Write a quarterly business review (QBR) from messy inputs”

Continuous task: produce a QBR deck from a folder of notes, metrics exports, and email threads. Constraint: must be accurate, cite sources, and be delivered as a structured markdown outline for conversion to slides.

Goal: define atomic subtasks τ, measurements **m**, and a mapping f that sequences them with branch points.

1. 1) Identify observables and risks

   - •Inputs are messy: CSV exports, PDFs, emails.
   - •Key risk: hallucinated numbers.
   - •Therefore, every numeric claim must be tied to a source row/cell.
2. 2) Propose atomic subtasks τ with explicit contracts

   Let each τ have (I, O, C, M).

   τ₁ = τ\_inventory

   I: folder path; allowed tools: file listing

   O: JSON list of files with type, date, guessed relevance

   C: JSON validates; every file has {name,type,hash}

   M: (coverage = files\_listed/total\_files)

   τ₂ = τ\_extract\_metrics

   I: selected CSV/XLSX files; allowed tools: dataframe parser

   O: canonical metrics table with columns {metric, period, value, source\_ref}

   C: schema validates AND every row has source\_ref

   M: (q = %rows with source\_ref, c = runtime)

   τ₃ = τ\_extract\_narrative

   I: email/PDF notes; allowed tools: text extraction

   O: bullet list of themes with citations (doc id + snippet)

   C: ≥ N themes and each has ≥ 1 citation

   M: (q = citation\_rate)

   τ₄ = τ\_outline

   I: metrics table + themes

   O: markdown outline with required sections

   C: headings match template; all charts referenced exist in metrics

   M: (q = template\_coverage)

   τ₅ = τ\_fact\_check

   I: outline + sources

   O: report of every numeric claim with its source\_ref

   C: all numeric claims linked OR flagged

   M: (q = linked\_claim\_rate)

   τ₆ = τ\_finalize

   I: corrected outline + fact check report resolved

   O: final markdown

   C: linked\_claim\_rate = 1 AND no critical flags

   M: (q = 1, s = policy\_ok, c = cost)
3. 3) Build dependency DAG and topological order

   Edges:

   - •τ\_inventory → {τ\_extract\_metrics, τ\_extract\_narrative}
   - •{τ\_extract\_metrics, τ\_extract\_narrative} → τ\_outline
   - •τ\_outline → τ\_fact\_check → τ\_finalize

   A valid topological sequence is:

   (τ\_inventory, τ\_extract\_metrics, τ\_extract\_narrative, τ\_outline, τ\_fact\_check, τ\_finalize)
4. 4) Define mapping f with branch points

   If τ\_extract\_metrics finds missing periods, branch:

   - •τ\_decide\_missing\_data outputs {"decision": "ask" | "estimate"}

   If "ask": run τ\_ask\_user (completion: user provides missing export)

   If "estimate": run τ\_estimate\_with\_uncertainty (must output CI and mark as estimate)

   So f is conditional:

   - •f(trajectory) = sequence that includes τ\_decide\_missing\_data when gaps detected.
5. 5) Add Bayesian completion for fact check

   Let Z = “all numeric claims are correct.” Evidence D includes linked\_claim\_rate and random spot-check results.

   If linked\_claim\_rate = 1 but spot-check fails, posterior P(Z=1|D) drops.

   Advance only when P(Z=1|D) ≥ 1 − δ (choose δ = 0.05 for high-stakes reporting).
6. 6) Mechanism design check (avoid gaming)

   If you reward linked\_claim\_rate alone, the system might avoid numbers.

   Mitigation: require minimum number of metrics/charts.

   Completion criterion includes: charts\_count ≥ K and all linked.

**Insight:** The discretization succeeds because it makes accuracy measurable (source\_ref per claim), adds explicit branch handling for missing data, and prevents reward hacking (avoiding numbers) by coupling “must include metrics” with “must cite metrics.”

### Worked Example 2 — Discretize “Fix flaky tests in a CI pipeline” (engineering-grade)

Continuous task: CI occasionally fails due to flaky tests. Objective: reduce flake rate while preserving coverage and not masking real failures.

We will define τ, measurements **m**, and a robust f that routes based on evidence.

1. 1) Define success in observables

   We cannot directly observe “true flakiness,” only failure patterns.

   Observables:

   - •test failure logs
   - •historical pass/fail frequency
   - •rerun outcomes
   - •runtime variance

   Define a metric:

   - •flake\_score(test) = P(fail | rerun) estimated from history
2. 2) Create atomic subtasks τ

   τ₁ = τ\_collect\_history

   I: CI logs datastore

   O: table {test\_id, runs, fails, rerun\_fails}

   C: table complete for last N days

   M: (q = coverage\_of\_runs)

   τ₂ = τ\_rank\_suspects

   I: history table

   O: ranked list with flake\_score and confidence

   C: list length ≥ 10 and confidence intervals present

   M: (q = calibration proxy)

   τ₃ = τ\_reproduce\_locally

   I: top suspect test; fixed seed policy

   O: reproduction report + environment fingerprint

   C: either reproduces OR documents non-repro with ≥ R attempts

   M: (c = time, q = attempts)

   τ₄ = τ\_root\_cause\_hypothesis

   I: reproduction artifacts

   O: hypothesis label {race, time, network, order, randomness} + evidence links

   C: evidence links ≥ 2

   M: (q = evidence\_count)

   τ₅ = τ\_fix

   I: hypothesis + code access (restricted to test module)

   O: patch

   C: patch applies cleanly; unit tests for module pass

   M: (q = tests\_pass)

   τ₆ = τ\_validate\_in\_ci

   I: patch + CI runner

   O: CI run results across M reruns

   C: failure rate ≤ ε AND runtime increase ≤ Δ

   M: (q = 1 − failure\_rate, c = runtime)

   τ₇ = τ\_guard\_against\_masking

   I: patch

   O: analysis: does it reduce assertions / skip?

   C: no new skips; assertion count not decreased beyond threshold

   M: (s = masking\_risk)
3. 3) Define dependency structure

   τ\_collect\_history → τ\_rank\_suspects → τ\_reproduce\_locally → τ\_root\_cause\_hypothesis → τ\_fix

   Then τ\_fix → {τ\_validate\_in\_ci, τ\_guard\_against\_masking} and both must pass.
4. 4) Define Bayesian inference for “is it truly fixed?”

   Let Z = “test is non-flaky under distribution of CI conditions.”

   Evidence D: M reruns with k failures.

   Assume a Beta prior for failure probability p:

   - •p ∼ Beta(α, β)
   - •k | p ∼ Binomial(M, p)

   Posterior:

   - •p | D ∼ Beta(α + k, β + M − k)

   We accept fix if:

   - •P(p ≤ ε | D) ≥ 1 − δ

   This is computable from the Beta CDF.
5. 5) Mechanism design: prevent trivial fixes

   If the reward is “CI passes,” the system might mark tests as xfail or skip.

   So we add τ\_guard\_against\_masking with strict completion criteria.

   We also define a global constraint:

   - •coverage\_after ≥ coverage\_before − γ
6. 6) Define mapping f (router behavior)

   If τ\_reproduce\_locally fails to reproduce after R attempts, branch:

   - •τ\_decide\_next outputs {"instrument", "increase\_reruns", "ask\_owner"}
   - •If instrument: add logging hooks (new τ) then retry reproduce.
   - •If increase\_reruns: run more CI reruns to get better posterior.
   - •If ask\_owner: request domain hints (human-in-the-loop).

   So f is a conditional policy over τ based on evidence quality.

**Insight:** This discretization prevents the most common failure mode—‘fixing’ flakes by weakening tests—by explicitly measuring masking risk and treating “fixed” as a Bayesian claim about future failure probability, not a single green CI run.

### Worked Example 3 — Deriving a simple reward from measurement vectors (showing work)

You have a subtask τ that produces measurements **m** = (q, s, c) with q,s ∈ [0,1] and c ≥ 0. You want a scalar reward r that (a) prioritizes correctness, (b) strongly penalizes safety violations, (c) mildly penalizes cost, and (d) is bounded to stabilize learning.

1. 1) Start with a linear reward (unbounded in cost)

   r₀ = w\_q q + w\_s s − w\_c c

   Problem: as c grows, r₀ → −∞, which can destabilize optimization.
2. 2) Bound the cost penalty with a saturating transform

   Use log(1 + c): grows slowly.

   Define:

   r₁ = w\_q q + w\_s s − w\_c log(1 + c)

   Now the penalty increases sublinearly.
3. 3) Add a hard safety veto (mechanism design)

   If safety is violated, we want r to collapse regardless of q.

   Let v be a binary safety violation indicator (from a classifier/validator):

   - •v ∈ {0,1}

   Define:

   r₂ = (1 − v) · r₁ − v · P

   where P > 0 is a large penalty.
4. 4) Bound the total reward to [−1, 1] for stability

   Apply tanh:

   r = tanh(r₂)

   Now r ∈ (−1, 1).
5. 5) Summarize final form

   r = tanh((1 − v)(w\_q q + w\_s s − w\_c log(1 + c)) − vP)

   Interpretation:

   - •When v = 0, you trade off quality/safety/cost smoothly.
   - •When v = 1, the penalty dominates.

**Insight:** Designing r is not just math; it is mechanism design. The ‘veto’ term prevents the agent from trading safety for quality, which linear weights often allow.

## Key Takeaways

- ✓

  Task discretization converts continuous intent into discrete, verifiable subtasks τ connected by an ordering (often a DAG).
- ✓

  An atomic subtask τ must have explicit input/output contracts and a completion criterion C that is observable and reasonably decidable.
- ✓

  Each τ should emit measurements **m** (often a vector) so you can verify, score, and learn without collapsing everything into one fragile metric too early.
- ✓

  The discretization mapping f is a policy/artifact that segments trajectories into (τ₁, …, τₙ) and must explicitly represent branch points and uncertainty.
- ✓

  Topological sorting of a τ-DAG separates dependency logic from scheduling and enables parallelism and robust recovery.
- ✓

  Bayesian inference helps you treat completion as probabilistic when validators are noisy or coverage is incomplete.
- ✓

  Mechanism design is central: any metric you introduce becomes an incentive, so you must anticipate and block reward hacking (Goodhart’s law).
- ✓

  Well-discretized tasks become easier to instrument, debug, optimize with losses/rewards, and scale across agents/tools.

## Common Mistakes

- ✗

  Defining τ without a real validator: if completion cannot be checked, you have not discretized—only renamed the ambiguity.
- ✗

  Over-splitting into tiny τ that create orchestration overhead and brittle handoffs, increasing failure probability at interfaces.
- ✗

  Using a single proxy metric as the objective (e.g., “CI green” or “#tests”) and getting gamed; failing to add constraints/vetoes.
- ✗

  Treating the plan as a fixed list: ignoring branch points (missing info, failed checks) and thereby forcing the system to hallucinate progress.

## Practice

medium

You are building an LLM system to “review a pull request for security issues.” Propose 6–8 atomic subtasks τ with (I, O, C) and at least one measurement each. Include at least one branch point and explain how f routes at that point.

**Hint:** Think in layers: inventory → threat model → scanning → manual reasoning → report → fix suggestions. Make sure each τ outputs an artifact that can be validated (schema, scan result thresholds, checklist completeness).

Show solution

One possible discretization:

τ₁ inventory\_files

I: repo path + PR diff; tools: git diff

O: JSON list of changed files with language + risk tag

C: schema valid; all diff files listed

M: coverage

τ₂ identify\_attack\_surface

I: inventory

O: structured list of entrypoints (HTTP handlers, auth, crypto)

C: at least one entrypoint or explicit “none found” with justification

M: rubric score

τ₃ run\_static\_scan

I: repo; tool: SAST

O: scan report with severities

C: report parsed; no tool errors

M: count(P0), count(P1)

τ₄ dependency\_audit

I: lockfiles

O: CVE list with package + version + severity

C: parsed; sources linked

M: count(high)

τ₅ deep\_review\_high\_risk

I: files tagged high risk

O: findings list with code references

C: each finding includes file:line and exploit narrative

M: evidence\_count

Branch point τ₆ decide\_blocking

I: findings + scan counts

O: decision {block, warn, approve} + rationale

C: decision ∈ set; rationale present

M: consistency check with policy

Routing f:

- •If decision=block ⇒ τ₇ propose\_fixes
- •Else ⇒ τ₈ finalize\_report

Validators: schema checks, policy thresholds (e.g., P0 must block), and completeness rubrics.

hard

Consider a subtask τ where the only available validator is a noisy human rating (0–5). Design a Bayesian completion rule using a prior and repeated ratings. State clearly what latent variable you infer and what threshold you use to declare completion.

**Hint:** Map the 0–5 rating to a binary ‘acceptable’ event or to a probabilistic model. Use a Beta-Binomial model for acceptability, or a Gaussian model for scores if you prefer. Then define P(Z=1|D) ≥ 1−δ.

Show solution

One solution (binary acceptability):

Latent variable:

- •Z = “output is acceptable to spec.”

Observation model:

- •Convert rating r ∈ {0,1,2,3,4,5} into y ∈ {0,1} where y=1 iff r ≥ 4.

Let p be probability a random rater marks acceptable.

Prior:

- •p ∼ Beta(α, β), e.g., α=2, β=2 (moderate prior).

Collect n ratings with k acceptables.

Posterior:

- •p | D ∼ Beta(α+k, β+n−k)

Completion rule:

- •declare complete if P(p ≥ p\_min | D) ≥ 1−δ

Example: p\_min=0.8, δ=0.05.

Interpretation:

- •you require high posterior confidence that most raters would accept the output.

medium

You discretize a task into τ₁…τₙ and define local rewards rᵢ. Give an example where maximizing ∑ᵢ rᵢ harms the global objective G. Then propose a constraint or redesign of measurements to fix it.

**Hint:** Use a Goodhart example: optimizing speed/cost per τ reduces quality; optimizing ‘#issues found’ creates false positives; optimizing ‘short answers’ harms completeness. Add a global veto, couple metrics, or redesign validators.

Show solution

Example: Code review agent.

Local reward rᵢ for τ\_find\_issues is proportional to number of issues reported.

Maximizing ∑ rᵢ causes the agent to flood the PR with trivial nitpicks (global objective G = developer usefulness drops).

Fix:

- •Redesign measurement: weigh issues by severity and require evidence.
- •Add constraint: false\_positive\_rate ≤ η measured by spot-checking.
- •Add global objective: reviewer usefulness score ≥ threshold; if not, veto or penalize.

This aligns incentives so high reward requires high-signal findings.

## Connections

Prerequisite links:

- •[Loss Functions](/tech-tree/loss-functions/)
- •[Markov Decision Processes](/tech-tree/markov-decision-processes/)
- •[Mechanism Design](/tech-tree/mechanism-design/)
- •[Topological Sort](/tech-tree/topological-sort/)
- •[Bayesian Inference](/tech-tree/bayesian-inference/)

Next-step nodes you may want after this concept:

- •[Workflow Orchestration for Agents](/tech-tree/workflow-orchestration/)
- •[Evaluation Harness Design](/tech-tree/evaluation-harness-design/)
- •[Reward Hacking and Goodhart’s Law](/tech-tree/reward-hacking/)
- •[Hierarchical RL (Options)](/tech-tree/hierarchical-rl-options/)

Quality: A (4.6/5)

[← back to tree](/tech-tree/)[browse all →](/tech-tree/inventory/)
