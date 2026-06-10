---
title: The Dollarized Confusion Matrix
description: Replace accuracy with dollars. Calculate optimal AI thresholds from the actual cost of being wrong in each direction. Stop setting thresholds by feel.
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
generated_by: templeton-deep-copy-import
source_format: html
inspiration_url: https://templeton.host/tools/dollarized-confusion-matrix/
inspiration_category: tools
---

> Source-copy draft imported from [https://templeton.host/tools/dollarized-confusion-matrix/](https://templeton.host/tools/dollarized-confusion-matrix/). Names, domain references, and local media paths were adapted for Xavi Ablaza / getablaza.com.

[← AI Operations Tools](/tools/)

# The Dollarized Confusion Matrix

[Stage 2Characterize](/thesis/#stage-2)

Replace accuracy with dollars. The optimal threshold for any AI classifier is not a feeling - it is a calculation, and the inputs are the actual cost of being wrong in each direction.

## The Matrix

A standard confusion matrix counts errors. A dollarized confusion matrix costs them. The two wrong cells drive every decision that follows.

Predicted Neg

Predicted Pos

Actual Neg

True Negative

+$0

False Positive

−$3

Actual Pos

False Negative

−$3k

True Positive

+$3

The insight: the four cells rarely cancel. Value on the diagonal moves the threshold just as much as cost off the diagonal.

## Threshold Calculator

Start with a scenario

Fraud detection

High cost of missed fraud, moderate false alarm cost

Medical screening

Critical to catch, follow-up test if flagged

Spam filter

Blocking real mail hurts more than missed spam

Compliance labeling

False positive = customer escalation

Ad targeting

Symmetric costs, value from precise targeting

Prop 65 LabelingProduct CategorizationFraud DetectionMedical Screening

Customize inputsFP: -$3 | FN: -$3000 | TP: +$3 | TN: +$0▾

Optimal Threshold

θ\* = 0.0010

Asymmetry

1001:1

0 (flag everything)0.5 (default)1 (flag nothing)

The cost of predicting *negative* and being wrong (missed gain + missed catch) is **1001x** the cost of predicting positive and being wrong. Set the threshold low - flag aggressively. At θ\* = 0.0010, you flag anything above 0.1% confidence. The asymmetry is extreme - even a small probability of a positive should trigger a flag.

Download JPEGCopy ImageCopy URLEmbed

## The Formula

# Optimal threshold including value on correct decisions

θ\* = (C\_FP + V\_TN) / (C\_FP + V\_TN + C\_FN + V\_TP)

# When V\_TP = V\_TN = 0 this collapses to C\_FP / (C\_FP + C\_FN)

# Numerator = loss from predicting positive when wrong

# Denominator = total loss across both wrong-prediction arms

A correct prediction has a value too, not just zero. Flagging a true positive is worth V\_TP (caught fraud is revenue retained). Passing on a true negative is worth V\_TN (the frictionless path through the system). The Bayes-optimal threshold balances the expected utility of predicting positive against predicting negative, giving:

θ\* = (C\_FP + V\_TN) / (C\_FP + V\_TN + C\_FN + V\_TP)

The numerator is what you lose when you predict positive and are wrong: you pay C\_FP (the false alarm) and you forfeit V\_TN (the clean pass you would have gotten). The denominator adds the symmetric loss on the other side. When all four are measured in the same units (dollars per decision), the threshold comes out dimensionless, which is what any probability gate requires.

## Worked Examples

Prop 65 Labelingθ\* = 0.001 · 1001:1

Unnecessary label ($3)

Violation fine ($3,000)

Product Categorizationθ\* = 0.50 · 1.0:1

Wrong category ($10)

Missing from category ($10)

Fraud Detectionθ\* = 0.05 · 20:1

Blocked legitimate tx ($50)

Approved fraud ($500)

Medical Screeningθ\* = 0.002 · 488:1

Unnecessary follow-up ($200)

Missed diagnosis ($50,000)

## From Threshold to Autonomy

The threshold tells you *where* to draw the line. The expected cost per item tells you *how much autonomy* the classifier earns.

HARMFUL

Expected cost >$50/item

Classifier is worse than manual - disable it. You're paying for AI and getting negative ROI.

HITL

Expected cost $5-50/item

Classifier assists but humans typically verify every item. AI does the first pass, humans make the call. Illustrative rule: graduate to Autonomous when expected cost drops below $5.

AUTONOMOUS

Expected cost <$5/item

Classifier runs independently with spot-checks only. Illustrative rule: demote back to HITL if cost rises above $10 (hysteresis prevents oscillation).

## Connection to the [Ablaza Ratio](/lexicon/templeton-ratio/)

The [Verification Quadrant](/tools/verification-quadrant/) asks: how hard is it to check? The Dollarized Confusion Matrix asks: **what happens when you check wrong?**

Cost asymmetry modifies the effective Ablaza Ratio. A task with T = 10 (fast verification) but 1,000:1 cost asymmetry needs verification at a *much* higher confidence level. The time to verify stays cheap, but the required thoroughness is driven by the stakes.

# Effective Ablaza Ratio

T\_effective = time\_to\_do / time\_to\_check\_at\_required\_confidence

# Required confidence is set by cost asymmetry

required\_confidence = f(C\_FP, C\_FN, θ\*)

The Verification Quadrant tells you *where* to automate. This matrix tells you *how carefully* to calibrate what you automate.

## When to Use This

### Use when

- +Costs of FP and FN are measurable
- +Asymmetry exists (at least 2:1)
- +You control the decision threshold
- +Volume justifies the optimization

### Skip when

- -Costs are symmetric (just use 0.5)
- -Scores are not calibrated probabilities
- -Regulatory bright-lines override cost math
- -Zero-tolerance domain (infinite FN cost)

## Rosetta Stone

Four circles, four readings of the same object. Each role reads the artifact through its own lens.

[Allocator

The cost of being wrong, direction by direction. Thresholds follow from costs, not from convention. 0.5 is rarely optimal.](/positions/allocator/)[Operator

The answer to "how cautious should the AI be?" - not a feeling, a formula. Plug the cost per false positive and false negative, get the threshold back.](/positions/operator/)[Builder

The calibration knob for any classifier in production. Two dollars, one number. Stop arguing about thresholds in review.](/positions/builder/)[Scientist

Bayes risk minimization with asymmetric loss. The optimal decision boundary is the likelihood ratio equal to the cost ratio. Textbook decision theory, rarely applied in practice.](/positions/scientist/)

## See also

[Lexicon

Proof Layer →](/lexicon/#proof-layer)[Lexicon

Autonomy State Machine →](/lexicon/#autonomy-state-machine)[Lexicon

Dollarized Confusion Matrix →](/lexicon/#dollarized-confusion-matrix)[Tool

What Factory Are You? →](/tools/factory-typology/)[Position

Allocator →

Which bets to make. Capital allocation, M&A due diligence, portfolio construction.](/positions/allocator/)[Position

Operator →

How to execute at scale. Multi-brand portfolio, turnarounds, P&L ownership.](/positions/operator/)

See also: [Verification Quadrant](/tools/verification-quadrant/) · [All Tools](/tools/)
