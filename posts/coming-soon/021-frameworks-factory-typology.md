---
title: The Factory Typology
description: The physical-factory archetype a knowledge-work line should borrow from is not a constant - it is a function of the line's input, process, and output signature. The triple signature, the archetype zoo, the smile curve, and the make-vs-buy boundary. Work in progress, building in public.
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
generated_by: templeton-deep-copy-import
source_format: html
inspiration_url: https://templeton.host/frameworks/factory-typology/
inspiration_category: frameworks
---

> Source-copy draft imported from [https://templeton.host/frameworks/factory-typology/](https://templeton.host/frameworks/factory-typology/). Names, domain references, and local media paths were adapted for Xavi Ablaza / getablaza.com.

[← Frameworks](/frameworks/)

# The Factory Typology

[Stage 1Find](/thesis/#stage-1)

A repeatable knowledge-work line - one stable enough to define inputs, transforms, outputs, and defects - can be operated like a factory. The comparison only earns its keep if it tells you *which* kind, because aerospace, an oil refinery, and a high-throughput drug screen have very different dominant operating levers (they share reliability, process control, and quality documentation, but optimize for entirely different things). The working claim:

candidate archetype ≈ f(coarse input, output, value-shape signature; process only proxied)

Not injective and not calibrated - the signature proposes analogies; it does not determine an archetype.

Name your line's signature and a mature industry's operations playbook becomes a head start you can **borrow selectively** - never wholesale, and only where the constraints match (assayability, defect observability, stationarity, marginal cost, queueing, regulatory burden). The richer the set of archetypes you can recognize, the more candidate practice is available. Try the [interactive classifier](/tools/factory-typology/) to place your own line. Low-repeatability work - exploratory research, negotiation, bespoke strategy, incident response - is where the analogy fits worst: the diagnostic should abstain, and the right move is to stabilize or decompose the work into a repeatable line first (or use a different lens), not to force an archetype onto it.

## The signature

The diagnostic asks **six primitive coordinates** - input (I), output kind, and the shape of the value out (U). The process (Σ) is only *proxied* by risk curvature and otherwise checked by follow-up questions, not directly asked. These are exactly the questions the [tool](/tools/factory-typology/) asks - one canonical schema. They underdetermine the operational form, so the output is a candidate, not a verdict: two lines can share all six and still differ on regulation, defect latency, or human-review cost.

I

Input grade

Your raw material. Scarce expert input often needs little concentration; free low-grade exhaust usually wants an assay/triage station if downstream processing is costly.

I

Input variance (signal-to-ore)

How much of the feed is waste. Extreme variance - a tailings pile with rare seams - usually wants exhaustive screening plus a cheap pre-filter; uniform feed reduces but does not eliminate screening (safety, drift, contamination).

Σ→U

Output kind

What the line emits: an artifact, a function/policy, a data slate, or a reusable type/process. It co-varies with the archetype.

U

Risk curvature

Usually the strongest single signal. Convex (breadth of attempts pays), concave (downside control pays; can be high-volume), or mixed (discovery feeds production).

U

Transferability

A reusable recipe/platform, or a one-off? A reusable platform can still emit one-off units - keep platform-reuse and unit-reuse distinct.

U

Volume / scale

High-volume / scaled, or low-volume / bespoke? (Volume and marginal cost are separate: a high-volume line with real per-unit model/API/review cost is still capacity-bound, not just yield-bound.)

### Derived consequences (implied, not asked)

⤷

Stage-difficulty locus

Where the irreducible acumen sits. In scalable, commoditized-middle lines it is often U-shaped (hard at design and distribution); some lines are front-, back-, or middle-heavy instead.

⤷

Coordination intensity

How hard the line is to coordinate (often driven by how hard your inputs are to join). It raises the make-vs-buy question but does not answer it: that boundary is a separate decision turning on asset specificity, hold-up, IP leakage, regulation, and supplier markets - not read off the value curve.

⤷

Defect-cost asymmetry

Often cheap at the per-unit instance (re-stampable) and catastrophic at the recipe (it fans out to every unit). QC belongs where the fan-out is - frequently, not always, at the recipe.

## Worked example (illustrative)

Take a line that turns scanned vendor invoices into structured fields. Name its six coordinates: low-grade abundant input (free incoming PDFs), extreme input variance (most of each page is irrelevant, a few fields are load-bearing), a data-slate output, concave risk curvature (a wrong field is costly and breadth of attempts does not help), a reusable extraction recipe, high volume.

That signature points at a **refinery**: continuous processing of a low-grade feed into a purified stream. So the playbook to borrow is statistical process control on the output fields plus a cheap pre-filter on the feed - not the breadth-of-attempts screening a convex discovery line would want. The point is the method, not this particular line: name your six coordinates, read off a candidate, then verify it against where your defects actually land.

## When the middle is commoditized, value often migrates to the ends

Use this only if cheapening the middle does not degrade *risk-adjusted, end-to-end* quality - which includes latent defect rates, compliance/audit exposure, security, model drift, reversibility, and accumulated learning, not just externally-visible metrics (those lag, and the middle is exactly where hidden liabilities surface later). If cheapening it hurts any of those, the middle is your moat - invest there instead.

Design / recipe (often own this)Distribution / demand capture (often own this)commodity middle - minimize ownership IF doing so does not hurt end-to-end qualityvalue added per stage

In many scalable, content- or software-like lines, value added per stage traces a smile once the middle is commoditized: high at the design end (the reusable recipe, the schema, the judged template) and the distribution end (the published surface, the demand-capture page), low in a commodity middle engineered cheap so the line scales. The conditional matters - in plenty of lines the middle *is* the moat (regulated processing, proprietary data cleaning, latency-sensitive infrastructure, expert review). The diagnostic question is whether your *risk-adjusted, end-to-end* quality - including latent and delayed liabilities (defect rate, compliance/audit debt, security, drift, reversibility, learning loss), not just externally-visible output - stays stable when the middle is cheap; if it does not, invest in the middle.

**Make-vs-buy is a separate decision**, not something that falls out of the curve. Buying commodity perception (extraction, model inference, raster generation) is often the first hypothesis to test, but the boundary turns on transaction cost, asset specificity, hold-up risk, IP leakage, latency, reliability, and whether the component compounds learning - and markets *can* sometimes sell you the join via integrators or managed services. When the middle is genuinely commoditized, the allocation read is **own the left-end recipe and the right-end surface, minimize ownership of the middle** - and the operator who owns both ends is better positioned to capture the rent, subject to bargaining power, switching costs, rights, and channel dependency.

## The archetype zoo

This is the current working set of archetypes - the ones that have covered the small, internal sample of lines analyzed so far (the sample is biased toward the kinds of lines I have built, and the negative cases are not yet catalogued). The falsifiable bet is that the set stays small as the sample grows; the honest invitation is for counterexamples. A line resembling professional services, marketplace governance, education, clinical care, or trust-and-safety may not fit cleanly - if yours does not, that is a new-archetype candidate, not a forced label. Tap one to read what its playbook transfers, and what does not.

Vertically Integrated Process ChainHigh-Throughput Screening / Directed EvolutionOre Reclamation / Froth Flotation (Salvage)Oil Refinery / Continuous ProcessFloat Glass / Commodity MaterialsPharma Process Scale-Up / Pilot PlantMass Customization / Configure-to-OrderShared-Capital Platform / FoundryAerospace / Job-Shop

### Vertically Integrated Process Chain

Physical exemplar: a specialty-chemicals firm running discovery, pilot, and production under one roof

Not one factory but several wired in series, with a risk-curvature sign-flip mid-line: convex discovery searches for a recipe, then concave production runs it at scale.

QC regime

Apply the right QC regime per layer, not per line. Screening metrics on the convex discovery layers; statistical process control plus cost-weighted thresholds on the concave production layers. A uniform posture across a chain is the common mistake.

Playbook it transfers

- →Theory of Constraints across the whole chain - the irreducible-judgement review tier is often (not always) the drum; instrument throughput where the bottleneck actually is.
- →Consider an inter-stage buffer at the curvature sign-flip (the joint between discovery and production), where queueing variance tends to concentrate.
- →Run the full ops stack per layer, not uniformly: screening economics upstream, SPC and poka-yoke downstream.
- →Treat the discovery half and the production half as separately fundable subsystems with an explicit handoff contract.

Transfers

Stage-specific QC, inter-stage buffering, and constraint analysis across a multi-stage line.

Does not transfer

Buffer/gate/firm-boundary placement is not mechanically fixed by the sign-flip; observability and defect cost can move them.

## When the line is a chain, apply QC per layer

In the lines I have analyzed, the most common pattern is not one factory but a chain with a **risk-curvature sign-flip** in the middle: a convex discovery stage that searches for a winning recipe, feeding a concave production stage that runs it at scale. (Pure-convex search lines and pure-concave execution lines exist too - the tool classifies those without forcing a chain.) The discovery half wants screening economics - many cheap shots, gold-plate only the confirmation, measure cost-per-confirmed-hit. The production half wants the opposite - statistical process control, cost-weighted thresholds, poka-yoke interlocks.

Where a line *is* a chain, a uniform QC posture across it is the common mistake. The most useful move is to **find the sign-flip** - the stage where you stop screening for upside and start defending against downside. It is a strong *candidate* location for your inter-stage buffer, your strictest gate, and your make-vs-buy boundary - but verify against where defects are actually cheapest to detect, where irreversible cost lands, and where queueing concentrates; any of those can pull a gate or boundary off the joint. When your curvature is mixed the [classifier](/tools/factory-typology/) proposes a chain decomposition - but only after you confirm both halves are genuinely load-bearing; if one stage dominates with a light prelude, it points you to classify the dominant stage instead. A sign-flip exists is not the same as the chain is the dominant archetype.

[Going deeper →

## The Formalism (work in progress)

Is the analogy a theorem or a metaphor? The dense page treats the structural functor honestly: what an adversary forced us to walk back, where the category theory is decorative, and the one open program - a computable obstruction invariant - that would make it predictive. Read it for the rigor, not for the playbook.](/frameworks/factory-typology/formalism/)

Changelog6 entries · building in publicshow ↓hide ↑

1. 2026-06-03Adversary round 8 (gpt-5.5). Removed the self-contradiction in the smile-curve gate (the diagnostic test is now risk-adjusted end-to-end quality, not "externally-observable quality"); aligned the non-repeatable-work guidance with the tool (abstain and stabilize/decompose, do not generate a hypothesis result); annotated the formula that the process coordinate is only proxied; softened "buying commodity perception is usually right" to "often the first hypothesis."
2. 2026-06-03Adversary round 5 (gpt-5.5). Broadened the smile-curve gate from "externally-observed quality" to risk-adjusted end-to-end quality (latent defects, compliance, security, drift, reversibility, learning - lagging metrics are insufficient). Made the chain copy conditional: mixed curvature proposes a chain only after both halves are confirmed load-bearing.
3. 2026-06-03Adversary round 4 (gpt-5.5). Softened the last universals (risk curvature is "usually" the strongest signal); sharpened the foundry exemplar to a semiconductor fab and removed turbine-blade machining from the bespoke aerospace row (it is a qualified repeatable process). The classifier now resolves the six-coordinate collisions via an answerable follow-up rather than disclosing them as dead-ends.
4. 2026-06-03Adversary round 3 (gpt-5.5). Made the smile curve conditional in the heading and the diagram (with a "use only if cheapening the middle does not hurt quality" gate); softened universal input-screening claims to conditionals; "very different operating levers" rather than "almost nothing in common"; tied playbook transfer to matching constraints; annotated the formula as non-injective (proposes analogies, does not determine); reworked the make-vs-buy derived row.
5. 2026-06-02Adversary round 2 (gpt-5.5). Scoped "knowledge work is manufacturing" to repeatable lines; reconciled the signature to one canonical six-coordinate schema (primitives vs derived consequences); made the smile curve and "starve the middle" conditional (the middle can be the moat); separated make-vs-buy from the curve; relabelled the zoo a "current working set" inviting counterexamples; made the sign-flip a candidate location, not a law.
6. 2026-06-02First public draft of the conceptual explainer: triple signature, archetype zoo, smile curve, make-vs-buy boundary, per-layer QC doctrine.

## Rosetta Stone

Four circles, four readings of the same object. Each role reads the artifact through its own lens.

[Allocator

The recipe for which physical industry to underwrite your knowledge-work line as. Own the left-end recipe and the right-end demand surface; starve the commodity middle. That is the allocation thesis stated as a value-add fact.](/positions/allocator/)[Operator

A way to stop running every line the same way. Most lines are chains with a curvature sign-flip; apply screening economics upstream and statistical process control downstream, never one posture across the whole thing.](/positions/operator/)[Builder

The system-design prior. The signature tells you whether you are building a screen, a refinery, a configurator, or a shared substrate - and therefore which failure modes to engineer against first.](/positions/builder/)[Scientist

A typology archetype = f(I, Σ, U) with a falsifiable compression claim and a separate, honestly second-class categorical track (a structural functor with an open obstruction-invariant program).](/positions/scientist/)

## See also

[Tool

What Factory Are You? →](/tools/factory-typology/)[Framework

Knowledge Work as Capital →](/frameworks/knowledge-capital/)

See also: [What Factory Are You?](/tools/factory-typology/) · [Knowledge Work as Capital](/frameworks/knowledge-capital/) · [Frameworks](/frameworks/)
