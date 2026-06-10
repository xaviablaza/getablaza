---
title: Designed Convergence
description: Design the game so that convergence to the desired outcome is a structural guarantee, not a hope. Mechanism design meets Bayesian ratchet search.
date: '2026-07-01'
scheduled: '2026-06-10'
tags:
- p-and-l-engineering
- coming-soon
- frameworks
layout: layouts/post.njk
templateEngineOverride: md
image: /img/xavi-linkedin-profile.jpg
draft: false
permalink: /frameworks/designed-convergence/
---

[← Frameworks](/frameworks/)

# Designed Convergence

[Stage 4Execute](/thesis/#stage-4)

Designed Convergence is the principle that if you design the search process with four properties - a finite search space, hypothesis elimination on each trial, Bayesian-informed trial generation, and a well-defined success predicate - then convergence to the desired outcome is a structural guarantee, not a hope. An individual experiment can fail. A program designed this way cannot. It can only take longer.

near-certainsingle experiment: p = 0.15Number of experiments (n)P(program success)00.250.500.751.0151015202530one success is enough0.150.560.800.960.99n = 10P(success) = 0.803

Download PNGCopy ImageCopy SVGCopy URLEmbed

Drag along the chart to scrub experiment count. After 10 experiments, P(success) = 0.803.

## The Distinction

|  | Experiment | Research Program |
| --- | --- | --- |
| Example | A/B test: does this CTA color increase conversion? | CRO program: systematically increase conversion over 12 months |
| Outcome | Binary: yes/no | Continuous: how much, how fast |
| Failure mode | Wrong hypothesis | None - the program finds the right hypothesis |
| P(success) | p | 1 - (1-p)n |

The key insight: **if you design the system, not the experiment, success becomes a structural guarantee.** The primary variable is time.

## The Math

An individual experiment has probability *p* of success. If p = 0.15, you have an 85% chance of failure. Most experiments fail. This is fine.

A program runs *n* independent experiments. The probability that at least one succeeds:

# Composite program probability

P(at least one success) = 1 - (1 - p)n

# For p = 0.15 (typical non-trivial hypothesis):

n = 1:   P = 0.15   (a gamble)

n = 5:   P = 0.56   (better than even)

n = 10: P = 0.80   (strong)

n = 20: P = 0.96   (near-certain)

n = 30: P = 0.993 (inevitable)

This isn't a trick - it's the complement rule applied to independent trials. But the organizational implication is profound: the program-level probability of success is a **design choice**, not a hope.

With Bayesian updating between trials, the experiments are not truly independent - each one is informed by prior failures. The effective *p* increases over time because you are not randomly sampling the hypothesis space; you are doing informed search. The formula above is a *lower bound* on the true program success probability.

## The Four Conditions

A system exhibits designed convergence when four conditions hold:

Condition 1

The search space is finite

Or can be made finite by reasonable discretization. If the space is unbounded, you need to bound it before you can guarantee convergence.

Condition 2

Each trial eliminates at least one hypothesis

No wasted experiments. Every trial either finds success or narrows the remaining space. Testing blue vs. slightly-different blue teaches you nothing about copy, placement, or timing.

Condition 3

Trial generation is informed by prior results

Bayesian, not random. Each failed trial updates your posterior on the remaining hypothesis space. The next trial is chosen from the updated belief. Informed search is O(log N); random search is O(N).

Condition 4

The success predicate is well-defined

You know it when you see it. Not “improve conversion” but “find configuration C such that conversion(C) > conversion(baseline) with p < 0.05 significance.”

# The convergence argument

Finite search space S, |S| = N

Each trial eliminates >= 1 element

After at most N trials, S is exhausted

Either success was found, or the entire space was searched.

# If success exists in S: guaranteed to find it

# If it does not: guaranteed to prove it does not exist (also valuable)

## The Designer's Seat

The four conditions above describe single-agent convergence - your own systematic search. But most real systems have multiple agents: vendors, operators, models, customers. Each has different objectives.

Every multi-agent system is a game. You can either:

1**Play the game** - optimize your own moves within existing rules

2**Design the game** - choose the rules so that the equilibrium of self-interested behavior is your desired outcome

Most engineering is (1). Mechanism design is (2), and the CTO's job is (2).

Backward mechanism design asks: “What game produces the desired equilibrium?” It produces a **system** - a set of rules under which the desired outcome is the natural resting state. Systems are robust because they do not depend on any particular path. They depend on the incentive structure, which is invariant to the specific sequence of events.

# Forward vs. backward

Forward: “Step 1: upload file. Step 2: map columns. Step 3...”

Breaks when any step fails unexpectedly.

Backward: “Agents who submit clean data get served faster.

Systems that guess wrong create operator work.

Operators who approve carelessly set floors they regret.”

Works regardless of failure mode - incentives push toward recovery.

## The Composition

**Designed Convergence = Mechanism Design + Bayesian Ratchet Search**

If you use mechanism design to construct a multi-agent game, and that game has the four conditions - finite state space, hypothesis elimination, informed search, well-defined success predicate - then convergence is a structural property of the *entire system*, not just your own actions.

Every agent acting in self-interest produces trials. The ratchet locks in improvements. The search space shrinks. The system converges to the desired outcome because the incentive structure typically makes it the stable equilibrium.

The difference between a good CTO and a great one is not making better decisions. It is designing systems where the quality of any individual decision matters less, because the system converges to the right answer regardless of the path.

## Why Organizations Fail at This

Low nRunning 3 tests instead of 30. At n=3 with p=0.15, composite probability is only 0.39. You are more likely to fail than succeed, and you will wrongly conclude the approach does not work.

No info gainRunning tests that don't update the posterior. Testing blue vs. slightly-different-blue teaches nothing about copy, placement, or targeting. Each trial must explore a genuinely different region.

No BayesTreating each test as independent. Random search is O(N); informed search is O(log N). The difference between a 3-month program and a 3-year program.

No ratchetFinding a winner but not locking it in. Running the next test against the original baseline instead of the new best. Without the [quality ratchet](/lexicon/#quality-ratchet), improvements do not compound.

Goal driftChanging what “success” means mid-program. This resets the search and wastes prior trials. Define the predicate once, commit to it.

## Connection to Other Frameworks

[Quality Hillclimb](/frameworks/quality-hillclimb/) is the single-agent instance of Designed Convergence - quality gates create ascent without a plan.

[The Promotion Protocol](/frameworks/promotion-protocol/) is mechanism design applied to AI autonomy - statistical graduation criteria are the incentive structure.

[The Performance Frontier](/frameworks/performance-frontier/) defines the success predicate - where does excellence live in the space you are searching?

The [AI Operations Tools](/tools/) are the evaluation instruments for each trial in the program.

## Worked example: visualization quality system

In practice, this framework shipped as a CI-enforced quality system for 182 interactive visualizations. Designed-convergence means: you don't tell the artist "make it better." You design the game so that each iteration can only land if the composite score isn't worse, and so that at least one dimension must improve. The ratchet does the ascent for you.

- -**The game:** six-dimension rubric (concept fidelity, visual clarity, animation, interaction, pedagogy, performance), six floors, a composite.
- -**The mechanism:** pre-push hook runs the grader; regressions fail the push. Improvements raise the floor. The baseline only moves up.
- -**The result:** after targeted color expansion, concept\_fidelity pass rate moved from 70% to 82% without anyone being asked to improve concept fidelity. The structure produced the outcome.

## When designed convergence fails

The framework makes a *falsifiable prediction*: a correctly designed ratchet will drive monotonic improvement on every dimension with a binding floor. If it does not, the design is wrong. Here are the common failure modes:

- -**Goodhart pressure on the rubric.** If the judge is too legible, contributors optimize the proxy instead of the thing. Counter with held-out dimensions or adversarial scoring passes.
- -**Stuck in a local minimum.** If every local move regresses some floor, the ratchet halts before the frontier. Pair it with periodic full-rewrite trials that are allowed to temporarily degrade dimensions.
- -**No cheap verifier.** The mechanism requires verification to be cheaper than generation. When it is not, build a verifier before installing the ratchet.
- -**Anti-aligned incentives.** If reviewers are rewarded for velocity, they will override the ratchet. The mechanism only converges if its enforcement is the binding constraint.

## Rosetta Stone

Four circles, four readings of the same object. Each role reads the artifact through its own lens.

[Allocator

A design principle that turns variance into structural return. Rather than underwriting "the team will probably hit the number," you underwrite "the system converges to the number by construction." Higher certainty, lower required return.](/positions/allocator/)[Operator

The shift from asking the team to be heroic to engineering the process so the outcome emerges from discipline. Less dependence on specific people, more dependence on the shape of the work.](/positions/operator/)[Builder

Mechanism design for production systems. You don't build a feature and hope it scales; you build the rules so scaling is automatic. State machines, invariants, reconciliation loops.](/positions/builder/)[Scientist

Convergence proofs from the mechanism-design tradition (Hurwicz, Maskin, Myerson). The equilibrium of self-interested play is the desired outcome. Dominant-strategy incentive compatibility where possible; Bayesian-Nash when not.](/positions/scientist/)

See also: [Quality Hillclimb](/frameworks/quality-hillclimb/) · [Quality Ratchet](/lexicon/#quality-ratchet) · [The Designer's Seat](/lexicon/#designers-seat)
