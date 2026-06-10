---
title: Meta-Learning
description: Learning to learn. Few-shot learning, MAML.
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
inspiration_url: https://templeton.host/tech-tree/meta-learning/
inspiration_category: tech-tree
---

> Source-copy draft imported from [https://templeton.host/tech-tree/meta-learning/](https://templeton.host/tech-tree/meta-learning/). Names, domain references, and local media paths were adapted for Xavi Ablaza / getablaza.com.

[←Back to Tech Tree](/tech-tree/)

[inventory](/tech-tree/inventory/)[coverage](/tech-tree/coverage/)

# Meta-Learning

Machine LearningDifficulty: ★★★★★Depth: 13Unlocks: 0

Learning to learn. Few-shot learning, MAML.

## Interactive Visualization

⏮◀◀▶▶STEP0.25x1xZOOM

t=0s

## Core Concepts

- -Task distribution: model-of-learning is defined over a distribution of tasks; learning uses many tasks to transfer across tasks.
- -Fast adaptation (inner loop): given a small dataset from one task, produce task-specific parameters quickly (few-shot update).
- -Meta-objective (outer loop): optimize shared meta-parameters so that after fast adaptation on a task they yield low task loss.

## Key Symbols & Notation

theta (meta-parameters / initialization)theta\_prime (adapted task-specific parameters after inner update)

## Essential Relationships

- -Meta-learning alternates: (1) inner-loop adaptation mapping theta + small task data -> theta\_prime via a few optimization steps, and (2) outer-loop meta-optimization that updates theta to minimize the expected post-adaptation loss of theta\_prime across tasks sampled from the task distribution.

## Prerequisites (2)

[Deep Learning6 atoms](/tech-tree/deep-learning/)[Stochastic Gradient Descent5 atoms](/tech-tree/sgd/)

Advanced Learning Details

### Graph Position

215

Depth Cost

0

Fan-Out (ROI)

0

Bottleneck Score

13

Chain Length

### Cognitive Load

6

Atomic Elements

51

Total Elements

L4

Percentile Level

L4

Atomic Level

### All Concepts (22)

- - Meta-learning (learning-to-learn): optimizing a procedure so models can adapt quickly to new tasks
- - Task (T) as a unit of experience: a distinct problem sampled from a distribution of tasks
- - Task distribution p(T): the probabilistic source of tasks used for meta-training and evaluation
- - Episode (episode-based training): a single meta-training instance consisting of one task with its split into support and query sets
- - Support set (also called 'shot' or training split of an episode): the small labeled set used for fast adaptation on a task
- - Query set (also called test split of an episode): the held-out examples used to evaluate post-adaptation performance for that task
- - K-shot / N-way terminology: K = number of examples per class in the support set; N = number of classes in classification episodes
- - Meta-parameters (θ): the shared parameters learned across tasks (often called initialization or slow weights)
- - Task-specific / adapted parameters (θ' or φ): parameters obtained after adapting meta-parameters to a particular task (fast weights)
- - Inner loop (task adaptation): the adaptation procedure (often a few SGD steps) applied to θ on the support set to produce θ'
- - Outer loop (meta-update): the optimization step that updates θ to improve post-adaptation performance across tasks
- - Meta-objective (expected post-adaptation loss): the objective minimized by meta-learning, typically the expected loss on query sets after adaptation
- - MAML (Model-Agnostic Meta-Learning): a specific meta-learning algorithm that learns an initialization θ such that few gradient steps on a task's support set produce good task performance
- - Gradient-based adaptation (fast adaptation): using gradient descent (or a small number of SGD steps) as the inner-loop adaptation mechanism
- - Higher-order gradients / backpropagating through optimization: computing gradients of the meta-objective that require differentiating through the inner-loop update(s)
- - First-order MAML (FOMAML): approximation of MAML that ignores second-order derivative terms to reduce computation
- - Support/query split as a training strategy that mimics few-shot test conditions during meta-training
- - Learning the inner learning rate or per-parameter learning rates (α) as part of the meta-parameters
- - Initialization-as-prior: interpreting the learned θ as a prior that makes task-specific fine-tuning efficient
- - Fast weights vs slow weights: distinction between quickly-updated task-specific parameters and slowly-learned meta-parameters
- - Meta-training vs meta-testing: training phase where θ is optimized over tasks vs test phase where θ is adapted to new tasks with few examples
- - Episode sampling and batch of tasks: meta-update computed over a batch of sampled tasks (episodes) rather than over individual datapoints

### Teaching Strategy

Multi-session curriculum - substantial prior knowledge and complex material. Use mastery gates and deliberate practice.

A normal ML pipeline learns one task at a time: it starts random (or pretrained), sees lots of data, and slowly becomes good. Meta-learning flips the question: can we train a system so that seeing just a few examples from a brand-new task is enough to adapt immediately?

TL;DR:

Meta-learning (“learning to learn”) trains over a distribution of tasks. In gradient-based meta-learning (e.g., MAML), we learn meta-parameters θ (often an initialization) so that a small inner-loop update on a new task produces adapted parameters θ′ with low task loss. The outer loop optimizes θ by differentiating through the inner-loop adaptation across many tasks.

## What Is Meta-Learning?

### Why meta-learning exists (motivation)

In standard supervised learning, we assume a single task: one input space, one label space, one dataset, and one loss. If you want to solve a *new* but related task, you often retrain or fine-tune. That works, but it’s wasteful and slow when:

- •Each new task has very little labeled data (few-shot).
- •Tasks arrive continuously and you must adapt quickly.
- •You care about *learning speed* as much as final performance.

Humans seem to have a prior over tasks: you can learn a new character in a foreign alphabet from a couple examples because you’ve learned *how learning tends to work* in that domain. Meta-learning aims to build that capability into ML systems.

### The key shift: from “one dataset” to “a distribution of tasks”

Meta-learning is not defined by a specific model class (you can meta-learn neural nets, linear models, optimizers). It’s defined by the *training setup*:

- •There is a distribution over tasks, written p(𝒯).
- •Each task 𝒯 has its own dataset and loss.

A common formalization:

- •Sample a task: 𝒯 ∼ p(𝒯)
- •Sample a *support set* (few-shot training data): Dₛ(𝒯)
- •Sample a *query set* (evaluation data): D\_q(𝒯)

The meta-learner uses Dₛ(𝒯) to adapt quickly, then is evaluated on D\_q(𝒯). Meta-training adjusts shared structure so that this procedure works well for tasks drawn from p(𝒯).

### What does “learning to learn” mean concretely?

A useful way to think about it is as a *two-level optimization*:

1. 1)**Inner loop (fast adaptation):** For a specific task 𝒯, update task-specific parameters using a small amount of data.
2. 2)**Outer loop (meta-learning):** Update shared meta-parameters so that the inner-loop adaptation yields low loss on new data for that task.

In gradient-based meta-learning, the shared parameters are often an initialization θ. Given a new task, you start from θ and take one or a few gradient steps to obtain θ′ (task-adapted parameters).

### When meta-learning is the right tool

Meta-learning is strongest when tasks are related but not identical.

Examples:

- •Few-shot classification across many classes (e.g., 5-way 1-shot episodes).
- •Reinforcement learning across environments with shared structure (different mazes, different dynamics).
- •Regression across functions (e.g., tasks are different sine waves or polynomials).

If tasks are unrelated, no method can reliably transfer. If tasks are identical, ordinary training already works.

### A small vocabulary (to keep us aligned)

| Term | Meaning | Typical symbol |
| --- | --- | --- |
| Task distribution | How tasks are generated | p(𝒯) |
| Task | A specific problem instance with its own loss | 𝒯 |
| Support set | Few-shot data used for adaptation | Dₛ(𝒯) |
| Query set | Data used to evaluate meta-objective | D\_q(𝒯) |
| Meta-parameters | Shared parameters across tasks | θ |
| Adapted parameters | Parameters after inner update for task 𝒯 | θ′ |

The rest of the lesson focuses on a canonical approach: **MAML (Model-Agnostic Meta-Learning)**, which cleanly illustrates the inner/outer loop idea and the role of θ and θ′.

## Core Mechanic 1: Task Distributions and Episodic Training

### Why episodic training matters

If the goal is: “perform well after seeing only a few examples from a new task,” then the training procedure should match that goal.

Episodic (a.k.a. meta-training) simulates test-time conditions repeatedly:

- •Pick a task 𝒯
- •Pretend you only get K examples per class (or a tiny dataset)
- •Adapt using those examples
- •Measure performance on held-out examples

This forces the model to practice adapting under data scarcity.

### A more formal view: what is a task?

A task 𝒯 typically specifies:

- •A data-generating process: (x, y) ∼ p\_𝒯(x, y)
- •A loss function: ℒ\_𝒯(θ; D)

For supervised learning, a common choice is cross-entropy over D.

The meta-learning assumption is:

- •𝒯 is random: 𝒯 ∼ p(𝒯)
- •Tasks share latent structure that can be exploited

You can imagine a hidden variable **z** controlling each task, e.g., “which classes are chosen,” “which sinusoid parameters,” or “which environment layout.” Even if we don’t explicitly model **z**, meta-learning tries to learn parameters that work well across the induced distribution.

### Support vs query: the train/eval split inside each task

Within each task 𝒯, we split data into:

- •**Support set** Dₛ(𝒯): used for inner-loop adaptation
- •**Query set** D\_q(𝒯): used to compute the meta-loss

This is subtle but crucial:

- •If you meta-optimize on the same data you adapt on, you can reward memorization.
- •By evaluating on D\_q(𝒯), you reward *generalization after adaptation*.

This resembles cross-validation, but nested inside a task distribution.

### The meta-objective in words

We want θ such that:

- •When we adapt θ using Dₛ(𝒯), we obtain θ′(𝒯)
- •Then θ′(𝒯) performs well on D\_q(𝒯)

So the outer objective is an expectation over tasks:

MetaLoss(θ) = 𝔼\_{𝒯 ∼ p(𝒯)} [ ℒ\_𝒯(θ′(𝒯); D\_q(𝒯)) ]

But θ′(𝒯) is itself produced by a learning rule (inner loop), usually gradient descent.

### Typical few-shot classification episode

A standard benchmark structure is N-way K-shot:

- •Choose N classes for the task
- •Support: K labeled examples per class (N·K total)
- •Query: Q labeled examples per class (N·Q total)

You run many episodes, each with different class subsets.

### What changes compared to “normal” training?

Normal training:

- •One dataset, minimize training loss.

Meta-training (episodic):

- •Many mini-problems.
- •Each mini-problem includes its own train/eval split.
- •The objective is performance after adaptation.

A practical comparison:

| Aspect | Standard supervised learning | Meta-learning (episodic) |
| --- | --- | --- |
| Unit of sampling | Example (x, y) | Task 𝒯 (support + query) |
| Objective | Low loss on dataset | Low loss after adaptation |
| Generalization target | New examples from same task | New tasks from p(𝒯) |
| Overfitting risk | Overfit dataset | Overfit task distribution |

### The “model of learning” perspective

Meta-learning is sometimes described as learning a *model of learning*: the algorithm itself is trained.

Concretely, you are no longer just learning a function f\_θ(x) → y.

You are learning parameters θ such that the *procedure*

θ → (adapt using Dₛ(𝒯)) → θ′(𝒯) → predictions on D\_q(𝒯)

works well across tasks.

This sets up the next mechanic: the fast inner loop and how θ′ is computed.

## Core Mechanic 2: Fast Adaptation (Inner Loop) and MAML’s Outer Loop

### Why gradient-based meta-learning is appealing

If you already know SGD and backprop, a natural idea is: “Can we meta-learn an initialization that fine-tunes quickly?”

This is the core of **MAML**:

- •It is *model-agnostic*: any differentiable model trained with gradient descent can be used.
- •It uses a very small number of inner steps (often 1–5).

### Inner loop: from θ to θ′

For a task 𝒯 with support set Dₛ, define the support loss:

ℒₛ(θ) = ℒ\_𝒯(θ; Dₛ(𝒯))

A single gradient step with step size α gives:

θ′ = θ − α ∇\_θ ℒₛ(θ)

This is the **fast adaptation** step. With multiple inner steps, you iterate:

θ⁽⁰⁾ = θ

θ⁽i+1⁾ = θ⁽i⁾ − α ∇\_{θ⁽i⁾} ℒ\_𝒯(θ⁽i⁾; Dₛ)

and set θ′ = θ⁽m⁾.

### Outer loop: optimize θ for post-adaptation performance

Now evaluate on the query set:

ℒ\_q(θ′) = ℒ\_𝒯(θ′; D\_q(𝒯))

The meta-objective across tasks is:

min\_θ 𝔼\_{𝒯 ∼ p(𝒯)} [ ℒ\_𝒯(θ′(θ, 𝒯); D\_q(𝒯)) ]

The key is that θ′ depends on θ. Therefore, when we compute the meta-gradient ∇\_θ ℒ\_q(θ′), we must differentiate *through the inner update*.

### The chain rule moment (where MAML becomes “meta”)

For one inner step:

θ′(θ) = θ − α ∇\_θ ℒₛ(θ)

The meta-gradient is:

∇\_θ ℒ\_q(θ′(θ))

Using the chain rule:

∇\_θ ℒ\_q(θ′) = (∂θ′/∂θ)ᵀ ∇\_{θ′} ℒ\_q(θ′)

Compute ∂θ′/∂θ:

θ′ = θ − α ∇\_θ ℒₛ(θ)

Differentiate w.r.t. θ:

∂θ′/∂θ = I − α ∂(∇\_θ ℒₛ(θ))/∂θ

But ∂(∇\_θ ℒₛ)/∂θ is the Hessian:

∂(∇\_θ ℒₛ(θ))/∂θ = ∇²\_θ ℒₛ(θ)

So:

∂θ′/∂θ = I − α ∇²\_θ ℒₛ(θ)

Therefore:

∇\_θ ℒ\_q(θ′)

= (I − α ∇²\_θ ℒₛ(θ))ᵀ ∇\_{θ′} ℒ\_q(θ′)

If the Hessian is symmetric (common), transpose doesn’t change it:

∇\_θ ℒ\_q(θ′)

= (I − α ∇²\_θ ℒₛ(θ)) ∇\_{θ′} ℒ\_q(θ′)

This is why MAML is considered “second-order”: it involves Hessian-vector products.

### First-Order MAML (FOMAML) and why people use it

Computing the exact meta-gradient can be expensive. A common approximation is to ignore the Hessian term:

∂θ′/∂θ ≈ I

Then:

∇\_θ ℒ\_q(θ′) ≈ ∇\_{θ′} ℒ\_q(θ′)

This is **FOMAML**. It often works surprisingly well, trading some accuracy for speed and memory.

### Reptile (related intuition)

Another popular first-order method is Reptile, which repeatedly:

- •Samples a task
- •Runs a few inner steps to get θ′
- •Moves θ toward θ′

Update:

θ ← θ + ε(θ′ − θ)

Reptile can be derived as optimizing a meta-objective that encourages within-task generalization. It’s simpler (no second-order terms) and sometimes competitive.

### What is actually being learned?

It’s tempting to say: “MAML learns an initialization.” That’s true, but incomplete.

MAML learns θ such that:

- •The gradients ∇\_θ ℒₛ(θ) are informative from very few examples.
- •One or a few steps land you in a good region for that task.

In geometric terms, θ is placed in parameter space near many task-specific optima, in a way that a small step can reach each optimum.

### Inner-loop hyperparameters are part of the story

The adaptation rule includes choices:

- •α (inner learning rate)
- •number of inner steps m
- •which parameters adapt (all layers vs last layer)

These strongly affect performance. Sometimes α is itself meta-learned.

### Practical training loop (conceptual)

For each meta-iteration:

1. 1)Sample batch of tasks {𝒯ᵢ}.
2. 2)For each 𝒯ᵢ:

- •Compute θ′ᵢ via inner updates on Dₛ(𝒯ᵢ).
- •Compute query loss ℒᵢ = ℒ\_𝒯ᵢ(θ′ᵢ; D\_q(𝒯ᵢ)).

3. 3)Meta-update:

- •θ ← θ − β ∇\_θ ∑ᵢ ℒᵢ

Here β is the outer learning rate.

At meta-test time:

- •Freeze θ (no outer updates).
- •Given a new task, adapt from θ using its support set to get θ′.
- •Evaluate on query/test examples.

This completes the central mechanism: θ is trained so that θ → θ′ quickly yields good performance.

## Application/Connection: Few-Shot Learning, Meta-Overfitting, and Practical Variants

### Few-shot learning: where MAML is often introduced

In few-shot classification, the model must build a classifier for novel classes from very few labeled examples.

Two broad families of approaches:

| Family | Core idea | Examples |
| --- | --- | --- |
| Metric-based | Learn an embedding where nearest-neighbor works | Prototypical Networks, Matching Networks |
| Optimization-based | Learn parameters/initialization to optimize quickly | MAML, FOMAML, Reptile |

MAML’s advantage is flexibility: it can adapt the whole network, not just a linear head. Its disadvantage is computational cost.

### Regression and RL: why “model-agnostic” matters

Because MAML only assumes differentiability, it applies to:

- •Regression tasks (predict y ∈ ℝ)
- •Classification tasks
- •Reinforcement learning (with policy gradients)

In RL, tasks might be different environments. The inner loop becomes one or a few policy-gradient updates; the query loss is expected return after adaptation.

### The hidden danger: meta-overfitting

Meta-learning can overfit in two ways:

1. 1)**Within-task overfitting:** adapting too strongly to the small support set.
2. 2)**Across-task overfitting (meta-overfitting):** learning θ that works well on meta-training tasks but not on meta-test tasks.

Meta-overfitting is especially likely if:

- •The number of meta-training tasks is small.
- •Tasks are not diverse.
- •The model is very expressive.

Practical mitigations:

- •Hold out meta-validation tasks for early stopping.
- •Regularize inner updates (fewer steps, smaller α, weight decay).
- •Increase task diversity; better sampling of episodes.

### Computation and memory: why second-order is hard

Exact MAML requires differentiating through inner-loop computation graphs.

Costs:

- •Memory grows with number of inner steps (need to backprop through them).
- •Second-order terms require Hessian-vector products.

Common workarounds:

- •FOMAML (ignore second-order).
- •Reduce inner steps.
- •Use implicit gradients (advanced) to avoid unrolling.

### What you get from meta-learning (and what you don’t)

Meta-learning is not magic. It leverages task similarity. You should expect:

- •Strong gains when tasks share structure.
- •Weak gains when tasks are unrelated.
- •Potential instability when the inner loop is poorly tuned.

### Interpreting θ and θ′ in practice

It helps to make θ and θ′ concrete:

- •θ: parameters after meta-training—your “learning-ready” model.
- •θ′: parameters after a few gradient steps on a specific new task.

The quality of meta-learning is measured by how good θ′ becomes given a tiny Dₛ.

### Connections to other ideas

- •**Transfer learning / fine-tuning:** Fine-tuning starts from pretrained θ but is not explicitly trained for fast adaptation; meta-learning is.
- •**Hyperparameter optimization:** Outer loop resembles optimizing hyperparameters (θ) with validation performance after inner training.
- •**Bilevel optimization:** MAML is a bilevel optimization problem (inner minimize support loss, outer minimize query loss).

### A simple mental model

If you imagine each task has its own optimal parameters θ\*(𝒯), then MAML tries to find θ such that:

- •θ is near many θ\*(𝒯) simultaneously
- •A small gradient step using few samples moves toward the appropriate θ\*(𝒯)

This is why, during meta-training, you must repeatedly practice: adapt on support, evaluate on query.

### When to choose MAML vs metric-based methods

| Criterion | Metric-based (Prototypical) | MAML |
| --- | --- | --- |
| Speed at meta-test | Very fast | Requires inner optimization |
| Flexibility | Often assumes class structure | Works for many losses/settings |
| Implementation complexity | Moderate | High (unrolling, stability) |
| Best when | Embedding is sufficient | Task requires deeper adaptation |

If your tasks differ mainly in labels/classes but share representation, metric methods are strong. If tasks require changing internal features or dynamics, optimization-based meta-learning can shine.

This closes the loop: meta-learning is a training paradigm over tasks, with a fast inner adaptation and a meta-objective optimizing θ so that θ′ performs well after few-shot updates.

## Worked Examples (3)

### Worked Example 1: One-Step MAML Meta-Gradient in 1D (Scalar θ)

Consider a simple 1D parameter θ ∈ ℝ. For a sampled task 𝒯, define the support loss ℒₛ(θ) and query loss ℒ\_q(θ). We do one inner step: θ′ = θ − α dℒₛ/dθ. We want dℒ\_q(θ′)/dθ.

1. Inner update (one step):

   θ′(θ) = θ − α (dℒₛ(θ)/dθ)
2. Differentiate θ′ w.r.t. θ:

   dθ′/dθ = 1 − α d/dθ (dℒₛ/dθ)

   = 1 − α (d²ℒₛ/dθ²)
3. Apply chain rule to the meta-objective:

   d/dθ ℒ\_q(θ′(θ)) = (dℒ\_q/dθ′) · (dθ′/dθ)
4. Substitute the expression for dθ′/dθ:

   dℒ\_q(θ′)/dθ = (dℒ\_q/dθ′) · (1 − α d²ℒₛ/dθ²)

**Insight:** Even in 1D, the meta-gradient includes a curvature term from the support loss. MAML is optimizing θ not just for low loss, but for producing useful gradients from few examples.

### Worked Example 2: Linear Regression Task Family and “Good Initialization” Geometry

Suppose tasks are 1D linear regression with parameter a (task-specific slope). For each task 𝒯, data is y = a x with small noise. The model is f\_θ(x) = θ x. Support set has a few (x, y) pairs. Show how one gradient step moves θ toward a.

1. Define mean-squared error on support set Dₛ:

   ℒₛ(θ) = (1/|Dₛ|) ∑(θ xᵢ − yᵢ)²
2. Use yᵢ = a xᵢ (ignore noise for clarity):

   θ xᵢ − yᵢ = θ xᵢ − a xᵢ = (θ − a) xᵢ
3. Rewrite the loss:

   ℒₛ(θ) = (1/|Dₛ|) ∑ ((θ − a) xᵢ)²

   = (θ − a)² · (1/|Dₛ|) ∑ xᵢ²
4. Compute the gradient:

   dℒₛ/dθ = 2(θ − a) · (1/|Dₛ|) ∑ xᵢ²
5. One inner gradient step:

   θ′ = θ − α · 2(θ − a) · (1/|Dₛ|) ∑ xᵢ²
6. Factor the update:

   θ′ = θ − c(θ − a) where c = 2α(1/|Dₛ|) ∑ xᵢ²

   So:

   θ′ = (1 − c) θ + c a

**Insight:** For this family, one step is a convex combination of θ and the task slope a (if 0 < c < 1). Meta-learning θ amounts to choosing an initialization that is close (on average) to task-specific optima so that one step lands near a.

### Worked Example 3: FOMAML Approximation vs Full MAML (What You Drop)

For one inner step: θ′ = θ − α ∇\_θ ℒₛ(θ). Full MAML uses ∇\_θ ℒ\_q(θ′(θ)). FOMAML approximates this gradient. Write both explicitly to see the difference.

1. Full MAML meta-gradient:

   ∇\_θ ℒ\_q(θ′) = (∂θ′/∂θ)ᵀ ∇\_{θ′} ℒ\_q(θ′)
2. Compute the Jacobian:

   ∂θ′/∂θ = I − α ∇²\_θ ℒₛ(θ)
3. So full MAML is:

   ∇\_θ ℒ\_q(θ′) = (I − α ∇²\_θ ℒₛ(θ))ᵀ ∇\_{θ′} ℒ\_q(θ′)
4. FOMAML approximation sets:

   ∂θ′/∂θ ≈ I

   Therefore:

   ∇\_θ ℒ\_q(θ′) ≈ ∇\_{θ′} ℒ\_q(θ′)

**Insight:** FOMAML treats θ′ as if it were independent of θ when computing the gradient. You keep the benefit of adapting in the inner loop, but you ignore how changing θ changes the adaptation trajectory.

## Key Takeaways

- ✓

  Meta-learning trains over a distribution of tasks p(𝒯), not a single dataset.
- ✓

  Each task splits into support Dₛ (for adaptation) and query D\_q (for meta-objective), rewarding generalization after adaptation.
- ✓

  In MAML, θ are meta-parameters (often an initialization), and θ′ are task-adapted parameters after inner-loop updates.
- ✓

  The outer objective minimizes expected query loss after adaptation: 𝔼\_{𝒯}[ℒ\_𝒯(θ′; D\_q)].
- ✓

  Full MAML differentiates through the inner update, introducing second-order terms involving ∇²\_θ ℒₛ.
- ✓

  FOMAML and Reptile are popular first-order alternatives that reduce computation and memory cost.
- ✓

  Meta-learning can meta-overfit: you must validate on held-out tasks and control inner-loop capacity and step sizes.
- ✓

  Meta-learning is most effective when tasks share structure such that fast adaptation from a shared θ is possible.

## Common Mistakes

- ✗

  Using the same data for adaptation and meta-evaluation (no support/query split), which rewards memorization rather than adaptation.
- ✗

  Assuming meta-learning will help when tasks are unrelated; without shared structure in p(𝒯), transfer cannot work.
- ✗

  Treating α (inner learning rate) and the number of inner steps as minor details—these can make MAML unstable or ineffective.
- ✗

  Reporting only meta-training performance; the real test is performance on unseen meta-test tasks after adaptation.

## Practice

easy

You have tasks 𝒯 ∼ p(𝒯). For each task you compute θ′ = θ − α ∇\_θ ℒ\_𝒯(θ; Dₛ). Write the meta-objective using a query set D\_q and describe (in one sentence) what it encourages.

**Hint:** Use an expectation over tasks and evaluate loss at θ′ on D\_q.

Show solution

MetaLoss(θ) = 𝔼\_{𝒯 ∼ p(𝒯)} [ ℒ\_𝒯(θ′; D\_q(𝒯)) ], where θ′ = θ − α ∇\_θ ℒ\_𝒯(θ; Dₛ(𝒯)). It encourages choosing θ so that a small gradient-based adaptation using Dₛ yields parameters that generalize well to new data D\_q from the same task.

medium

Derive ∂θ′/∂θ for one inner step θ′ = θ − α ∇\_θ ℒₛ(θ), and identify where the Hessian appears.

**Hint:** Differentiate both sides w.r.t. θ; derivative of a gradient is a Hessian.

Show solution

Differentiate: ∂θ′/∂θ = ∂/∂θ [θ − α ∇\_θ ℒₛ(θ)] = I − α ∂(∇\_θ ℒₛ(θ))/∂θ = I − α ∇²\_θ ℒₛ(θ). The Hessian appears as the Jacobian of the gradient.

hard

In the linear regression family y = a x (task slope a), suppose one inner step yields θ′ = (1 − c)θ + c a for some 0 < c < 1 (as derived in the lesson). If tasks have slopes a with mean 𝔼[a] = μ, what initialization θ minimizes expected squared error 𝔼[(θ − a)²] before adaptation? What does that suggest about a reasonable meta-initialization when only one small step is allowed?

**Hint:** Minimizing 𝔼[(θ − a)²] over θ gives θ = 𝔼[a].

Show solution

We minimize J(θ) = 𝔼[(θ − a)²]. Differentiate: dJ/dθ = 𝔼[2(θ − a)] = 2(θ − 𝔼[a]). Setting to 0 gives θ\* = 𝔼[a] = μ. This suggests that when only a limited adaptation is possible, a good meta-initialization is near the average task optimum; the inner step then nudges θ toward each specific a.

## Connections

Related nodes:

- •[Stochastic Gradient Descent](/tech-tree/stochastic-gradient-descent/) — inner-loop and outer-loop updates both rely on gradient estimators.
- •[Transfer Learning and Fine-Tuning](/tech-tree/transfer-learning/) — meta-learning can be seen as training explicitly for fast fine-tuning.
- •[Bilevel Optimization](/tech-tree/bilevel-optimization/) — MAML is a classic bilevel problem: inner adapts, outer evaluates.
- •[Few-Shot Learning](/tech-tree/few-shot-learning/) — meta-learning is one of the main paradigms for few-shot generalization.
- •[Automatic Differentiation](/tech-tree/automatic-differentiation/) — differentiating through inner loops requires careful autodiff and often Hessian-vector products.

Quality: A (4.4/5)

[← back to tree](/tech-tree/)[browse all →](/tech-tree/inventory/)
