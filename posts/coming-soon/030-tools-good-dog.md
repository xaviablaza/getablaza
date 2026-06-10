---
title: The DoG Test
description: 'A 60-second Claude prompt that audits an AI roadmap idea on three checks: strength of finding, surprise, and utility. Built on Popper, Shannon, Lindley, and Raiffa.'
date: '2026-07-01'
scheduled: '2026-06-10'
tags:
- p-and-l-engineering
- coming-soon
- tools
layout: layouts/post.njk
templateEngineOverride: md
image: /img/xavi-linkedin-profile.jpg
draft: false
permalink: /tools/good-dog/
---

[← AI Operations Tools](/tools/)

# The DoG Test

Is your AI roadmap a good DoG or a bad DoG?

A 60-second Claude prompt that tells you whether your AI roadmap idea is ready to ship, needs more work, or shouldn’t be pursued at all. Built on Popper, Shannon, Lindley, and Raiffa; packaged as a paste-into-Claude operator audit.

Copy the prompt

Paste into Claude (or any frontier model) with any AI roadmap idea you want to audit. The model will refuse to evaluate it until you have answered three questions about how you would *know* the idea is good. Takes about 60 seconds; rejects most bad ideas in the first check.

When to use it

Any AI roadmap idea, feature bet, or model-improvement proposal you are about to spend calendar and budget on. The audit is cheapest at the moment of proposal, before sunk cost accrues and before the idea has political momentum behind it.

When not to use it

A decision that is already reversible-cheap (just try it), a pure-research exploration where the point is to learn rather than to ship, or a call that turns on taste or values rather than a dollarized bet. Forcing those through a Backing / Bite / Bet audit measures the wrong thing.

## The Full Prompt

Show promptCopy prompt

Paste this into Claude (or any frontier model) and feed it the idea you want to audit. It will refuse to evaluate the idea on its merits until you have answered three questions about how you would *know* the idea is good. Use **Copy prompt** to grab the whole thing without expanding it; use **Show prompt** if you want to read it inline first.

81 lines · BACKING · BITE · BET checks · verdict + recursive sharpening step. Click **Show prompt** to expand.

## Three Checks at a Glance

1. Backing

How do you know?

The specific claim, the evidence behind it, and an observation that would change your mind. No change-my-mind condition = no backing yet.

2. Bite

Are you learning anything?

The single belief this updates for a smart, informed person in your domain. Restatement of common wisdom has no bite.

3. Bet

Who would bet money on it?

What metric this moves, in dollars. Order-of-magnitude delta if true vs false. Who in the org would sign their name to that estimate.

Backing × Bite × Bet. An idea has to clear all three to be worth doing - otherwise you are spending calendar, budget, and reputation on something that cannot fail informatively.

## Same three checks, different lenses

The carousel uses Backing × Bite × Bet because the words are short, alliterative, and stick. Underneath, these are the three factors of Expected Value of Sample Information (Lindley, 1956). If your team prefers different vocabulary, here are equivalent slates the prompt’s structural behavior is identical under.

| Carousel | Plain operator | Boardroom | Math / EVSI |
| --- | --- | --- | --- |
| Backing | Evidence | Rigor | Strength of finding / Falsifiability |
| Bite | Insight | Novelty | Surprise / Information gain |
| Bet | Stakes | Impact | Utility / Expected dollar weight |

The prompt always uses Backing / Bite / Bet so that the published carousel, the open-source transcripts, and the tool output stay in sync. The other slates are translation layers for different rooms.

## When YELLOW is actually STOP: the EV-hurdle

The audit’s natural failure mode is to engage rather than terminate. When an idea has thin evidence but could-in-principle be supported, the audit returns NEEDS TRAINING with a “go gather X first” next action. That is the right move *most* of the time. It is the wrong move when X is too expensive to gather.

The fourth check the audit does *not* apply automatically - and that you should apply yourself before accepting a YELLOW verdict:

EV(having the data) vs. Cost(acquiring it)

if Cost > EV: this YELLOW is a 🔴 STOP-UNOBTAINABLE.

A YELLOW verdict assumes the missing data is *economically obtainable*. If gathering it would take a quarter of operations time on a pitch the board would only fund at thirty percent confidence, the right call is to stop. The audit cannot price your team’s time or the strategic value of the answer. You can.

Concrete shape: before accepting a YELLOW, write down (a) the specific data the audit said you needed, (b) the all-in cost to gather it (headcount-hours, vendor cost, opportunity cost), and (c) the expected dollar improvement in the decision from having it. If (c) clears (b) - YELLOW is real and worth deferring on. If (b) clears (c) - YELLOW is a STOP wearing yellow clothing.

## What It Produces

🟢GOOD DoG

All three checks clear. The claim is falsifiable, the update is non-obvious, the utility is dollarized with ownership. Next action: ship the smallest version that could falsify it.

🟡NEEDS TRAINING

One or more checks come back UNDERSPECIFIED. The idea could be good but isn’t in shape to commit resources against yet. Next action: name the specific missing piece and fill it before iterating.

🔴BAD DoG

A check returns BAD PROXY - the metric is outside your control, lagging when leading exists, or activity standing in for value. Next action: stop. Pursuing this would be motion without information.

## Run It Yourself

Two paths, depending on whether you want a one-off audit or a repeatable harness.

Path A

Paste into Claude

Copy the prompt above. Paste it into Claude. Describe the idea you want to audit. Sixty seconds, no setup.

Path B

Clone the repo

The full test harness is open-source on GitHub: [andrew-templeton/dog-test](https://github.com/xaviablaza/dog-test). TypeScript, provider-agnostic (Anthropic / OpenAI / Gemini), runs against five committed worked examples so you can replay them locally.

## Prior Art

The three checks are not new. **Backing** is Popper - a claim that cannot be falsified is not a claim. **Bite** is Shannon - information is the reduction of uncertainty, and a restatement of common wisdom reduces none. **Bet** is Lindley and Raiffa - the value of a decision is the expected dollar delta against the next-best alternative, owned by someone who can sign for it. The DoG Test packages those three filters into a single 60-second operator audit. [TESTS.md](https://github.com/xaviablaza/dog-test/blob/main/TESTS.md) in the repo is the deeper reference, including how the calibration set was assembled.

## The LinkedIn Launch Deck

The 15-slide carousel walks through the three checks with worked examples and a structural-experiment frame. Built with the same zinc aesthetic as the rest of the site.

[Download the carousel (PDF)](/carousels/good-dog.pdf)[See the LinkedIn post](https://www.linkedin.com/posts/xaviablaza_the-dog-test-ugcPost-7465040403466006529-Q7Ob)

Xavi Ablaza

AI ops, P&L engineering, allocation thinking.

[Subscribe](/#newsletter)[Writing](/writing/)[LinkedIn](https://www.linkedin.com/in/andrew-templeton/)[All tools](/tools/)
