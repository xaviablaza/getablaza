---
title: Bayesian Decision Theory
description: Loss functions L(action, state). Bayes risk, posterior expected loss minimization. Admissibility, minimax estimators. Decision rules as functions from data to actions.
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
permalink: /tech-tree/bayesian-decision-theory/
---

[←Back to Tech Tree](/tech-tree/)

[inventory](/tech-tree/inventory/)[coverage](/tech-tree/coverage/)

# Bayesian Decision Theory

Probability & StatisticsDifficulty: ★★★★☆Depth: 8Unlocks: 2

Loss functions L(action, state). Bayes risk, posterior expected loss minimization. Admissibility, minimax estimators. Decision rules as functions from data to actions.

## Prerequisites (3)

[Bayesian Inference5 atoms](/tech-tree/bayesian-inference/)[Expected Value5 atoms](/tech-tree/expected-value/)[Optimization Introduction5 atoms](/tech-tree/optimization-intro/)

## Unlocks (2)

[Revenue Managementlvl 5](/tech-tree/revenue-management/)[Dynamic Pricinglvl 5](/tech-tree/dynamic-pricing/)

## Referenced by (18)

Where this concept shows up in the operating-finance and personal-finance graphs.

### From Business (18)

[Utility FunctionBusiness

Extends utility to decision-making under uncertainty - loss functions are negative utility, and Bayes risk minimization is choosing actions that maximize expected utility given beliefs](/business/utility-function/)[Error CostBusiness

Bayesian decision theory is the formal mathematical framework for error cost estimation - loss functions L(action, state), Bayes risk as expected loss over the posterior, and choosing actions that minimize posterior expected loss are exactly the machinery needed to make error costs estimable](/business/error-cost/)[personal financeBusiness

The moderate-debt-strategy decision under uncertainty (invest vs repay at ambiguous rates) is posterior expected loss minimization with uncertain future returns as the prior](/business/personal-finance/)[Scoring ModelBusiness

A scoring model that ranks AI bets and selects which to pursue is a Bayesian decision rule: define a utility/loss over outcomes, compute posterior expected utility for each candidate bet given current evidence, and choose the action that maximizes it](/business/scoring-model/)[Service RecoveryBusiness

The $47 directly parameterizes the loss function L(predict\_ok, actual\_problem) = 47 in a Bayes-optimal decision rule, where the threshold that minimizes posterior expected loss shifts to avoid costly false negatives](/business/service-recovery/)[Value of InformationBusiness

VOI (EVPI, EVSI) is formally defined within Bayesian decision theory as the expected reduction in Bayes risk from observing data before choosing an action. Loss functions, posterior expected loss minimization, and the decision rule framework give VOI its mathematical foundation.](/business/value-of-information/)[investment decisionBusiness

The formal framework for choosing actions under uncertainty by minimizing posterior expected loss - the rigorous version of evaluating operating decisions as investments](/business/investment-decision/)[UnderwritingBusiness

Formalizes the underwriting decision as minimizing posterior expected loss over invest/pass actions given uncertain deal parameters - the mathematical backbone of due diligence updating beliefs with each new data point](/business/underwriting/)[Enterprise ValueBusiness

Posterior expected loss minimization is the formal mathematical framework for 'systematic identification of mispriced edges' - choosing actions that minimize Bayes risk given beliefs about true state. Every mispriced edge is a decision where expected payoff exceeds price under your posterior.](/business/enterprise-value/)[ROI underwritingBusiness

Formal framework for capital allocation under uncertainty - posterior expected loss minimization maps directly to go/no-go investment decisions given evolving due diligence evidence](/business/roi-underwriting/)[M&A due diligenceBusiness

M&A due diligence is choosing actions (acquire, pass, renegotiate) under uncertainty about target value, with asymmetric loss functions (overpaying destroys returns, missing a good deal has opportunity cost) - exactly posterior expected loss minimization](/business/m-a-due-diligence/)[Approved FraudBusiness

The approve/reject threshold is a Bayes-optimal decision rule: given posterior P(fraud|signals), choose the action minimizing expected loss L(approve,fraud)=$500 vs L(investigate,fraud)=staff\_cost+friction. The $500 cutoff falls out of the loss function.](/business/approved-fraud/)[Expected Total CostBusiness

Comparing expected total cost across options is posterior expected loss minimization - choose the consolidation option (action) that minimizes E[L(a, state)] under uncertainty about future costs](/business/expected-total-cost/)[M&A Technical Due DiligenceBusiness

Due diligence is decision-making under uncertainty with asymmetric loss functions - the cost of funding a dud (wasted capital, distraction) differs from the cost of killing a winner (foregone upside). Posterior expected loss minimization over fund/kill actions given noisy technical signals is the formal structure of the problem.](/business/m-a-technical-due-diligence/)[capital disciplineBusiness

Capital discipline under uncertainty requires choosing actions (fund, cut, defer) that minimize posterior expected loss given noisy signals about technology ROI - the formal framework for 'invest or not' under incomplete information](/business/capital-discipline/)[AllocatorBusiness

Fund-or-kill decisions under uncertainty are Bayes risk minimization - choose the action (fund, kill, restructure) that minimizes posterior expected loss given due diligence evidence](/business/allocator/)[PE operatorsBusiness

Investment committee decisions are posterior expected loss minimization under uncertainty - PE operators update beliefs on portfolio company performance with new data and choose actions (hold, inject capital, exit) that minimize expected loss given current posteriors](/business/pe-operators/)[Portfolio AlphaBusiness

The mathematical foundation for allocation decisions under uncertainty. The allocator minimizes posterior expected loss when choosing where to deploy capital, updating beliefs about business quality with operational evidence. Loss functions L(action, state) map directly to capital deployment decisions.](/business/portfolio-alpha/)

Advanced Learning Details

### Graph Position

111

Depth Cost

2

Fan-Out (ROI)

2

Bottleneck Score

8

Chain Length

Decisions under uncertainty are everywhere: choosing a medical treatment, setting a spam filter threshold, or estimating a parameter for a model. Bayesian Decision Theory turns posterior probabilities into concrete actions that minimize expected harm.

TL;DR:

Bayesian Decision Theory chooses actions to minimize expected loss: compute posterior expected loss for each action and pick the minimizer; Bayes rules, Bayes risk, admissibility and minimaxity formalize optimality under uncertainty.

## What Is Bayesian Decision Theory?

Bayesian Decision Theory is the formal framework that turns probabilistic beliefs (posteriors) into concrete actions by minimizing expected loss. In a decision problem you specify:

- •A state (parameter) space \(\Theta\) representing unknowns (e.g., a disease presence, a parameter value).
- •An action space \(\mathcal{A}\) (e.g., treatment choices, point estimates, classification labels).
- •A loss function \(L(a,\theta)\) quantifying how bad action \(a\) is when the true state is \(\theta\).
- •A data-generating model (likelihood) and a prior over \(\Theta\). From these we obtain a posterior distribution, using Bayesian Inference (In Bayesian Inference, we learned how to update priors to posteriors via the likelihood).

A decision rule (or decision function) is a measurable function \(\delta: \mathcal{X} \to \mathcal{A}\) mapping observed data \(X\) to an action. If we allow randomization, \(\delta\) can be a Markov kernel from \(\mathcal{X}\) to \(\mathcal{A}\). The performance of a decision rule is measured by the risk function

R(δ,θ)=EX∼Pθ[L(δ(X),θ)],R(\delta,\theta)=\mathbb{E}\_{X\sim P\_\theta}[L(\delta(X),\theta)],R(δ,θ)=EX∼Pθ​​[L(δ(X),θ)],

which is the expected loss when the true state is \(\theta\). (Numeric example: if \(L(a,\theta)=(a-\theta)^2\) and \(X\sim N(\theta,1)\) with decision \(\delta(X)=X\), then \(R(\delta,\theta)=\mathbb{E}[(X-\theta)^2]=1\); here the risk equals the variance 1.)

A Bayesian (or Bayes) rule minimizes the Bayes risk relative to a prior \(\pi(\theta)\):

r(δ)=Eθ∼π[R(δ,θ)]=Eθ,X[L(δ(X),θ)].r(\delta)=\mathbb{E}\_{\theta\sim\pi}[R(\delta,\theta)]=\mathbb{E}\_{\theta,X}[L(\delta(X),\theta)].r(δ)=Eθ∼π​[R(δ,θ)]=Eθ,X​[L(δ(X),θ)].

The Bayes rule minimizes \(r(\delta)\) over decision rules. There's a crucial simplification: minimizing the Bayes risk decomposes pointwise in data by minimizing the posterior expected loss (also called the posterior risk). For each observed \(x\) one computes

ρ(a∣x)=E[L(a,Θ)∣X=x],\rho(a\mid x)=\mathbb{E}[L(a,\Theta)\mid X=x],ρ(a∣x)=E[L(a,Θ)∣X=x],

then chooses an action \(a^*(x)\) that minimizes \(\rho(a\mid x)\). This yields a Bayes rule \(\delta^*(x)=a^*(x)\). (Numeric example: Suppose the posterior for \(\Theta\) given \(x\) is \(N(2,0.5^2)\) and \(L(a,\theta)=(a-\theta)^2\). Then \(\rho(a\mid x)=\mathbb{E}[(a-\Theta)^2]= (a-2)^2+0.5^2\). Minimizing in \(a\) gives \(a^*=2\): the posterior mean.)

Why care? This approach converts the qualitative posterior into an action automatically accounting for asymmetric losses, different units, and decision costs. It unifies point estimation, hypothesis testing, and classification: they differ only by the loss function and action space. Because the method depends on the loss, it forces explicit statement of utility/penalty — a strength in applied decision-making.

In summary, Bayesian Decision Theory: (1) defines performance by loss, (2) evaluates rules by risk, and (3) picks actions via minimizing posterior expected loss. It connects directly to Bayesian Inference (posterior), Expected Value (posterior expectation), and Optimization Introduction (minimization of expected loss).

## Core Mechanic 1: Posterior Expected Loss Minimization and Common Losses

The central constructive rule is: for each observed data \(x\), choose action

a∗(x)=arg⁡min⁡a∈A  ρ(a∣x),ρ(a∣x)=E[L(a,Θ)∣X=x].a^\*(x)=\arg\min\_{a\in\mathcal{A}}\;\rho(a\mid x),\qquad \rho(a\mid x)=\mathbb{E}[L(a,\Theta)\mid X=x].a∗(x)=arga∈Amin​ρ(a∣x),ρ(a∣x)=E[L(a,Θ)∣X=x].

This converts a potentially infinite-dimensional global minimization (over rules) to a pointwise minimization in the action space for each \(x\). This is where Bayesian Inference (posterior) and Expected Value (taking expectation of the loss) come together with Optimization Introduction (solving the minimization).

Important canonical loss functions and their Bayes actions:

1) Squared error loss: \(L(a,\theta)=(a-\theta)^2\).

- •Posterior expected loss: \(\rho(a\mid x) = \mathbb{E}[(a-\Theta)^2|x] = (a-\mu\_{post})^2 + \sigma\_{post}^2\), where \(\mu\_{post}=\mathbb{E}[\Theta\mid x]\) and \(\sigma\_{post}^2=\mathrm{Var}(\Theta\mid x)\).
- •Minimizer: \(a^\*(x)=\mu\_{post}\) (the posterior mean).
- •Numeric example: If posterior is \(N(3,0.25)\) then \(\mu\_{post}=3\), \(\sigma\_{post}^2=0.25\). The posterior expected loss at \(a=2.5\) is \((2.5-3)^2+0.25=0.25+0.25=0.5\). Minimizer is \(a=3\).

2) Absolute error loss: \(L(a,\theta)=|a-\theta|\).

- •Posterior expected loss: \(\rho(a\mid x)=\mathbb{E}[|a-\Theta||x]\).
- •Minimizer: any median of the posterior. If the posterior is continuous and unimodal, the unique minimizer is the posterior median.
- •Numeric example: If posterior is \(N(0,1)\), the median is 0, so \(a^\*=0\). The posterior expected loss at \(a=1\) is \(\mathbb{E}[|1-\Theta|]=\int |1-\theta|\phi(\theta)d\theta\approx 1.0\) (numerical integration) while at \(a=0\) it's smaller, about 0.7979.

3) 0–1 loss (classification): For action set \(\mathcal{A}=\{0,1\}\) and state in \(\{0,1\}\),

L(a,θ)=1{a≠θ}.L(a,\theta)=\mathbf{1}\{a\neq\theta\}.L(a,θ)=1{a=θ}.

- •Posterior expected loss when choosing \(a=1\) is \(1-\mathbb{P}(\Theta=1\mid x)\); choosing \(a=0\) gives \(1-\mathbb{P}(\Theta=0\mid x)\).
- •Minimizer: choose the class with the highest posterior probability (the posterior mode, or MAP rule).
- •Numeric example: If \(\mathbb{P}(\Theta=1\mid x)=0.7\) then choosing 1 has posterior expected loss 0.3, choosing 0 has loss 0.7, so choose 1.

4) Asymmetric linear loss (linex or weighted absolute): \(L(a,\theta)=c\_1(\theta-a)\_++c\_2(a-\theta)\_+\) with different penalties for under- vs over-estimation.

- •Minimizer: a posterior quantile determined by the ratio of weights. Specifically choose the \(\alpha= c\_1/(c\_1+c\_2)\) posterior quantile.
- •Numeric example: Suppose \(c\_1=2\), \(c\_2=1\), so \(\alpha=2/3\). If posterior is \(N(0,1)\), the 2/3 quantile is approx 0.43. Thus the Bayes action clips toward higher values.

Derivation sketch (squared loss): write

ρ(a∣x)=E[(a−Θ)2∣x]=a2−2aμpost+E[Θ2∣x]\rho(a\mid x)=\mathbb{E}[ (a-\Theta)^2\mid x ] = a^2 -2a\mu\_{post} + \mathbb{E}[\Theta^2|x]ρ(a∣x)=E[(a−Θ)2∣x]=a2−2aμpost​+E[Θ2∣x]

Differentiate: \(\partial/\partial a\,\rho(a\mid x)=2a-2\mu\_{post}\); solve to get \(a=\mu\_{post}\). Numeric instantiation: if \(\mu\_{post}=1.5\), set \(a=1.5\). This is a simple calculus-based optimization, invoking the Optimization Introduction prerequisite.

This pointwise minimization is the key computational rule: after computing the full posterior (In Bayesian Inference, we learned how to compute \(\pi(\theta\mid x)\)), reduce decisions to a small optimization in the action space, typically tractable analytically for standard losses or numerically otherwise.

## Core Mechanic 2: Bayes Risk, Admissibility, and Minimaxity

The Bayes rule is a decision rule minimizing the average risk under a prior, but in frequentist evaluation we often care about performance across possible true values \(\theta\). Two foundational frequentist optimality notions are admissibility and minimaxity.

Definitions:

- •Risk: \(R(\delta,\theta)=\mathbb{E}\_{\theta}[L(\delta(X),\theta)]\).
- •Bayes risk for rule \(\delta\) w.r.t. prior \(\pi\): \(r\_\pi(\delta)=\int R(\delta,\theta)\,\pi(d\theta)\).
- •An estimator \(\delta\_1\) dominates \(\delta\_2\) if \(R(\delta\_1,\theta)\le R(\delta\_2,\theta)\) for all \(\theta\) and strictly less for some \(\theta\). \(\delta\) is admissible if no rule dominates it.
- •\(\delta\) is minimax if it minimizes the maximum (supremum) risk across \(\Theta\):

δMM=arg⁡min⁡δ sup⁡θ∈ΘR(δ,θ).\delta\_{MM}=\arg\min\_{\delta}\,\sup\_{\theta\in\Theta} R(\delta,\theta).δMM​=argδmin​θ∈Θsup​R(δ,θ).

Numeric example (simple): For the normal location problem with known variance, \(X\sim N(\theta,\sigma^2)\) and decision \(\delta(X)=X\), squared error loss gives \(R(\delta,\theta)=\sigma^2\) independent of \(\theta\). So \(\sup\_\theta R=\sigma^2\). This constant-risk property is strong: any rule with risk uniformly at most \(\sigma^2\) must have risk equal to \(\sigma^2\) and \(\delta(X)=X\) is minimax. Concretely, if \(\sigma^2=1\) and \(n=1\), then \(R=1\).

Relationships between Bayes and minimax solutions:

- •If a Bayes rule has constant risk in \(\theta\), it is minimax because its maximum risk equals the Bayes risk. Numeric example: For a prior that makes the posterior mean equal to the sample mean (improper flat prior), the sample mean can be both Bayes and minimax in some Gaussian problems — with risk equal to variance/n.

- •Least favorable prior: If a prior \(\pi^*\) maximizes the Bayes risk achieved by its Bayes rule (i.e., \(r\_{\pi^*}(\delta\_{\pi^*})=\sup\_\pi \inf\_\delta r\_\pi(\delta)\)), then the Bayes rule for \(\pi^*\) is minimax. The prior is 'least favorable' because it makes the decision problem hardest on average.

- •Wald's complete class theorem (sketch): Under mild regularity, the set of Bayes rules (and limits of Bayes rules) is essentially complete — any admissible rule is a Bayes rule or a limit of Bayes rules. Thus focusing on Bayes rules is not as restrictive as it may sound. This theorem uses advanced measure-theoretic arguments; here we note the implication: many admissible procedures are obtainable via Bayesian formulations.

Admissibility facts and pitfalls:

- •A Bayes rule with respect to a proper prior is often admissible under regularity; counterexamples exist (e.g., Stein's paradox). For instance, in multivariate normal mean estimation with squared error and dimension at least 3, the usual estimator (sample mean) is inadmissible: James–Stein shrinkage estimators dominate it. This is a striking result showing that being unbiased or intuitive doesn't guarantee admissibility.

Numeric demonstration of minimax via constant risk: Consider estimating \(\theta\) from \(X\sim N(\theta,\sigma^2/n)\) using \(\delta(X)=X\) (sample mean from \(n\) observations). With squared loss, \(R(\delta,\theta)=\sigma^2/n\) for all \(\theta\). If \(\sigma^2=4\) and \(n=4\), then \(R=1\) uniformly, so \(\delta\) is minimax with worst-case MSE 1.

Constructing least favorable priors: In many finite-parameter settings, the least favorable prior is discrete and concentrates mass on parameter values that make distinguishing difficult. In continuous problems, least favorable priors may be improper or limits of discrete priors. Finding a least favorable prior often involves a saddle-point (minimax) optimization: maximize over priors the minimal Bayes risk.

Practical takeaways: Bayes rules provide a principled way to find good decision rules; admissibility and minimaxity give frequentist guarantees. When risks depend on \(\theta\), consider whether a Bayes rule under a sensible prior yields acceptable sup-risk; if you need worst-case guarantees, solve the minimax problem or seek a least favorable prior.

## Applications and Connections

Bayesian Decision Theory underlies many applied tasks. Because it tells you how to convert posterior distributions into actions, it is the bridge between probabilistic modeling and practical decisions.

Concrete applied examples:

1) Medical decision-making (treatment selection): Suppose \(\Theta\) is a binary indicator for disease severity and actions are treatment intensities. Losses combine treatment cost and mis-treatment harm. Using patient data, compute the posterior probability of severity (In Bayesian Inference, we learned to compute this) and pick the treatment minimizing posterior expected loss. Numeric example: If posterior probability of severe disease is 0.2, and losses are 10 for undertreatment and 3 for overtreatment, weighted expected losses are computed and action chosen accordingly.

2) Point estimation with asymmetric penalties (forecasting): In inventory management, understocking is more costly than overstocking. Represent this via asymmetric linear loss and pick the corresponding posterior quantile as the order quantity. Numeric example: If understock cost is twice overstock cost (ratio 2:1), order the 2/3 posterior quantile of demand.

3) Classification and binary decisions: 0–1 loss yields the MAP rule; with cost-sensitive classification, use weighted 0–1 loss to tilt the decision threshold according to posterior odds and cost ratio. Numeric example: If false negative costs 5 times a false positive, choose the label 1 whenever posterior odds exceed 1/5.

4) Hypothesis testing framed as decision: Treat accepting/rejecting as actions and specify losses for Type I and II errors. Minimization of posterior expected loss often yields familiar threshold rules when combined with likelihood ratios and priors.

Connections to other fields and techniques:

- •Machine learning and classification: Loss-based training (cross-entropy, hinge loss) is decision-theoretically motivated. In probabilistic classifiers, Bayes decision rule is the Bayes optimal classifier under 0–1 loss. Link to expected value: classifier chooses class that minimizes the expected 0–1 loss given the posterior.

- •Reinforcement learning: The action-value function is an expected cumulative loss (or negative reward). Bayesian decision principles apply to model-based RL where posterior over dynamics guides planning under uncertainty.

- •Robust statistics: Minimaxity connects to robust estimation — a minimax estimator is robust against worst-case parameters. Least favorable priors interpret robustness from a Bayesian viewpoint.

- •Empirical Bayes and hierarchical modeling: Often you estimate priors from data to get practical Bayes rules (In Bayesian Inference, we learned hierarchical priors). Empirical Bayes can produce rules with good frequentist properties.

- •PAC-Bayes and learning theory: Bayesian priors and posterior generalization bounds use Bayes risk and expected losses to control generalization.

Numerical/algorithmic aspects:

- •For complex posteriors, compute posterior expectations via MCMC or variational inference, then minimize \(\rho(a\mid x)\) numerically. For continuous action spaces, perform gradient-based optimization on \(\rho(a\mid x)\). Numeric example: If posterior samples of \(\Theta\) are {0.5,1.2,0.8}, for squared loss compute sample mean 0.833 as approximate Bayes action; for absolute loss compute sample median 0.8.

- •For model selection and utility-aware model comparison, compute expected utility (negative expected loss) of actions induced by each model and choose the model maximizing expected utility.

Final note: Bayesian Decision Theory formalizes the natural way to make decisions under uncertainty by combining Bayesian Inference (posteriors), Expected Value (posterior expectations), and Optimization Introduction (minimization). It gives both prescriptive rules (choose minimizer of posterior expected loss) and prescriptive-frequentist guarantees (via admissibility/minimaxity) that guide practical decision-making in statistics, machine learning, and applied domains.

## Worked Examples (3)

### Gaussian Posterior, Squared Loss — Posterior Mean as Bayes Action

Data: Single observation X=5 from model X|\theta \sim N(\theta,1). Prior: \theta\sim N(3,4). Loss: squared error L(a,\theta)=(a-\theta)^2. Compute the posterior, the Bayes action a^*(x), and the Bayes risk r(\delta) of the Bayes rule \delta(X)=a^*(X).

1. 1) Compute posterior parameters. Prior N(3,4) has mean 3 and variance 4. Likelihood is N(\theta,1) viewed as function of \theta. Posterior for \theta|X=x is Normal with mean \mu\_post = (\sigma\_l^{-2} x + \sigma\_p^{-2} \mu\_p)/(\sigma\_l^{-2}+\sigma\_p^{-2}) and variance \sigma\_post^2 = 1/(\sigma\_l^{-2}+\sigma\_p^{-2}). Here \sigma\_l^2=1 (likelihood variance) and \sigma\_p^2=4 (prior variance).
2. 2) Plug numbers: precision (inverse variance) of likelihood is 1, of prior is 1/4 = 0.25. Sum precision = 1 + 0.25 = 1.25. So posterior variance = 1/1.25 = 0.8. Posterior mean = (1*5 + 0.25*3)/1.25 = (5 + 0.75)/1.25 = 5.75/1.25 = 4.6.
3. 3) Bayes action under squared error is the posterior mean, so a^\*(5)=4.6. Numeric check: if we had chosen a=4.6, the posterior expected loss is Var + (bias)^2 = 0.8 + 0 = 0.8. For a=5, posterior expected loss is (5-4.6)^2 + 0.8 = 0.16 + 0.8 = 0.96, larger.
4. 4) The Bayes rule is \delta(x)=\mu\_{post}(x) (posterior mean as a function of x). To compute the Bayes risk r(\delta)=E\_\theta E\_{X|\theta}[(\delta(X)-\theta)^2], use the decomposition r = E[Var(\theta|X)] + E[(E[\theta|X] - \theta)^2]. But for a Bayes rule minimizing r, there's an identity r(\delta) = E[Var(\Theta|X)] + E[ (\Theta - E[\Theta|X])^2 ] = E[Var(\Theta|X)] + 0 = E[Var(\Theta|X)]. Actually the Bayes risk equals the prior variance minus the expected posterior variance; simpler to compute directly here.
5. 5) Compute Bayes risk directly: For squared loss, r(\delta) = E\_{X}[ Var(\Theta|X) ] + E\_{X}[ (E[\Theta|X] - \Theta)^2 ] but the second term equals 0 if expectation is over prior and posterior — more directly r(\delta) = E\_{\theta,X}[(\delta(X)-\theta)^2]. Using conjugacy one can show r(\delta)=prior variance - E[variance reduction] = prior variance - E[posterior variance]. Given conjugacy with one observation, posterior variance is constant 0.8 for any x, so E[posterior variance]=0.8. Prior variance=4, so Bayes risk = 4 - 0.8 = 3.2.
6. 6) Numeric summary: Posterior is N(4.6, 0.8). Bayes action for X=5 is 4.6. Bayes risk of the rule (averaged over prior and X) is 3.2.

**Insight:** This example shows the full workflow: compute posterior (Bayesian Inference), obtain the posterior mean (Expected Value) and use calculus/optimization to argue it minimizes posterior expected squared loss (Optimization Introduction), then compute the Bayes risk. It demonstrates how a single data point pulls the prior mean toward the data in the posterior and how Bayes risk accounts for prior uncertainty.

### Binary Classification with Asymmetric Costs

Two classes: \Theta\in\{0,1\}. Posterior probabilities given x: P(\Theta=1|x)=0.3. Loss: false negative cost c\_FN=10 (predict 0 when true=1), false positive cost c\_FP=1 (predict 1 when true=0). Actions: predict 0 or 1. Decide the Bayes action and compute posterior expected losses.

1. 1) Write posterior expected loss for predicting 1: choose a=1 gives loss = c\_FP  *P(\Theta=0|x) = 1*  (1 - 0.3) = 0.7.
2. 2) Posterior expected loss for predicting 0: choose a=0 gives loss = c\_FN  *P(\Theta=1|x) = 10*  0.3 = 3.0.
3. 3) Compare losses: loss(a=1)=0.7, loss(a=0)=3.0. The Bayes action minimizes posterior expected loss, so choose a=1 despite the posterior favoring 0, because false negatives are much more costly.
4. 4) Compute the breakpoint posterior probability p *where actions tie: c\_FP*(1-p)=c\_FN*p => c\_FP - c\_FP p = c\_FN p => p*(c\_FN + c\_FP) = c\_FP => p\* = c\_FP/(c\_FP + c\_FN) = 1/(1+10) = 1/11 ≈ 0.0909. So if P(Θ=1|x)>0.0909 we predict 1. Here p=0.3>0.0909 so predict 1.
5. 5) Interpret: even though class 1 is less likely, larger cost of missing it forces predicting 1; this shows how Bayesian Decision Theory formalizes cost-sensitive decisions.

**Insight:** This example shows a cost-sensitive classification rule: the Bayes decision depends on both posterior probabilities (In Bayesian Inference) and the loss matrix. It highlights the role of asymmetric costs and the simple algebra that yields decision thresholds.

### Asymmetric Linear Loss — Posterior Quantile as Bayes Action

Model: posterior for \Theta|x is N(2,1). Loss: L(a,\theta)=c\_1(\theta-a)\_+ + c\_2(a-\theta)\_+ with c\_1=3 (underestimate penalty), c\_2=1 (overestimate penalty). Find the Bayes action.

1. 1) For weighted absolute loss of this form, Bayes action is the posterior quantile at level \alpha = c\_1/(c\_1 + c\_2) = 3/(3+1) = 3/4 = 0.75.
2. 2) Compute the 0.75 quantile of N(2,1): the standard normal 0.75 quantile z\_{0.75} ≈ 0.6745. So the posterior 0.75-quantile is 2 + 1 \* 0.6745 = 2.6745.
3. 3) Thus the Bayes action is a^\*(x) ≈ 2.6745. Check numerically: compute posterior expected loss at a=2.6745 via numerical integration or note property that a quantile minimizes the weighted absolute expected loss.
4. 4) Compare to posterior mean 2: if we used squared loss we'd choose 2, but because underestimation is more costly we pick a higher value (2.6745). Numeric compare: if we picked a=2, expected weighted absolute loss = c\_1 E[(Θ-2)\_+] + c\_2 E[(2-Θ)\_+] which will be larger than at the 0.75 quantile.
5. 5) Interpretation: The Bayes action reflects risk asymmetry — by shifting to the 75th percentile we trade a small increase in overprediction loss for a larger decrease in underprediction loss, lowering total expected loss.

**Insight:** This example demonstrates that different loss choices lead to qualitatively different Bayes actions (mean vs median vs quantile), emphasizing the necessity to specify losses to align actions with application goals.

## Key Takeaways

- ✓

  A decision rule maps data to actions; its performance is measured by the risk function R(δ,θ)=E\_X[L(δ(X),θ)].
- ✓

  Bayes rules minimize Bayes risk r\_π(δ)=E\_π[R(δ,θ)] and are found by minimizing posterior expected loss pointwise: a\*(x)=argmin\_a E[L(a,Θ)|X=x].
- ✓

  Under common losses: squared error → posterior mean; absolute error → posterior median; 0–1 loss → posterior mode (MAP); asymmetric linear loss → posterior quantile.
- ✓

  Admissibility and minimaxity are frequentist optimality criteria: admissible rules are not dominated; minimax rules minimize the worst-case risk. Bayes rules can be minimax, especially via least favorable priors.
- ✓

  Computationally, Bayes decision-making reduces to posterior computation (Bayesian Inference) and small-scale optimization (Expected Value + Optimization Introduction), often solvable analytically for conjugate models or numerically with posterior samples.
- ✓

  Choosing the loss function is crucial: it encodes application priorities and changes the optimal action, so decision theory forces explicit utility specification.
- ✓

  Many practical algorithms (classification thresholds, forecast quantiles, shrinkage estimators) are immediate consequences of decision-theoretic choices of loss and prior.

## Common Mistakes

- ✗

  Confusing posterior mode with posterior mean: for squared loss the optimal action is the posterior mean, not the mode; choosing the mode gives suboptimal posterior expected squared loss in general.
- ✗

  Using improper priors without checking consequences: an improper prior may lead to a formal Bayes rule but the Bayes risk or admissibility properties may fail or require limit arguments.
- ✗

  Equating Bayes optimality with minimaxity: a Bayes rule is not automatically minimax unless additional conditions (e.g., constant risk or existence of a least favorable prior) hold.
- ✗

  Ignoring asymmetric costs: using symmetric losses (MSE) by default can produce actions that are grossly suboptimal when under- and over-estimation have different real-world costs.

## Practice

easy

Given posterior \Theta|x \sim N(1.5, 0.36), compute the Bayes action under (a) squared error loss, (b) absolute error loss, and (c) asymmetric linear loss with c1=2 for underestimation and c2=1 for overestimation.

**Hint:** Use results: squared loss → posterior mean; absolute loss → median; asymmetric linear → posterior quantile at c1/(c1+c2). For Normal, mean = median and quantiles use standard normal z-values.

Show solution

Posterior mean = 1.5; posterior median = 1.5. For asymmetric linear loss, alpha = c1/(c1+c2)=2/3≈0.6667; z\_{0.6667}≈0.4307. Posterior 2/3-quantile = 1.5 + sqrt(0.36)*0.4307 = 1.5 + 0.6*0.4307 = 1.5 + 0.2584 = 1.7584. So (a) 1.5, (b) 1.5, (c) ≈1.7584.

medium

Consider classification with two classes and 0–1 loss but with unequal false negative cost c\_FN and false positive cost c\_FP. Given posterior P(Θ=1|x)=p, derive the Bayes rule and compute the threshold p *in terms of c\_FN and c\_FP. Then evaluate p* when c\_FN=4 and c\_FP=1.

**Hint:** Write posterior expected loss for predicting 1 and 0, set them equal to find threshold.

Show solution

Loss when choosing 1: c\_FP*(1-p). Loss when choosing 0: c\_FN*p. Choose 1 when c\_FP*(1-p) ≤ c\_FN*p → c\_FP ≤ p(c\_FN + c\_FP) → p ≥ c\_FP/(c\_FN + c\_FP). Thus p *= c\_FP/(c\_FN + c\_FP). For c\_FN=4, c\_FP=1, p* = 1/(4+1)=0.2. So predict 1 if p≥0.2.

hard

Let X\_1,...,X\_n iid N(θ,σ^2) with known σ^2. Consider estimator δ(X)=\bar X (sample mean). (a) Compute R(δ,θ) under squared error loss and show it is constant in θ. (b) Prove δ is minimax among all measurable estimators by showing no estimator can have sup\_θ R smaller than this constant. (Outline a rigorous argument.)

**Hint:** Use that Var(\bar X)=σ^2/n and bias is zero so MSE=σ^2/n. For part (b), use the fact that for any estimator, Bayes risk under a prior converges to the sup risk for a sequence of priors concentrating mass at the worst-case θ; use least favorable prior or a lower bound via averaging over parameters.

Show solution

a) For δ=\bar X, R(δ,θ)=E[(\bar X-θ)^2]=Var(\bar X)+[E(\bar X)-θ]^2=σ^2/n + 0 = σ^2/n, which is constant in θ. b) Let c=σ^2/n. For any estimator δ', sup\_θ R(δ',θ) ≥ ∫ R(δ',θ) π\_m(dθ) for any prior π\_m. Choose priors π\_m that put mass uniformly on an expanding finite grid and then concentrate mass at parameter values where R(δ',θ) is near its supremum; taking limit yields sup\_θ R(δ',θ) ≥ lim r\_{π\_m}(δ') ≥ inf\_δ r\_{π\_m}(δ) and for the sequence the right-hand side approaches c because the Bayes risk cannot be below c. More concretely, use the fact that inf\_δ sup\_θ R(δ,θ) = sup\_π inf\_δ r\_π(δ) (minimax theorem) and note that for the sample mean the max risk equals c, so no estimator can have sup risk < c. Hence δ is minimax.

## Connections

Backward connections: This lesson builds directly on Bayesian Inference (In Bayesian Inference, we learned how to compute priors, likelihoods, and posteriors to represent uncertainty), Expected Value (we repeatedly take expectations of losses to compute posterior expected loss), and Optimization Introduction (we minimize posterior expected loss to obtain actions). Forward connections: Bayesian Decision Theory is foundational for statistical learning (it yields Bayes optimal classifiers and motivates loss functions used in training), for hypothesis testing framed as decisions with asymmetric costs, for reinforcement learning (planning under posterior uncertainty), and for robust statistics and minimax theory (least favorable priors, saddle-point formulations). Specific downstream topics that require this material include: James–Stein shrinkage and admissibility proofs, empirical Bayes decision rules for hierarchical models, PAC-Bayes bounds in learning theory, cost-sensitive classification algorithms, and Bayesian experimental design (which optimizes expected utility/loss). Understanding Bayes risk, admissibility, and minimaxity is essential for advanced work in theoretical statistics and machine learning where both Bayesian and frequentist guarantees matter.

Quality: pending (0.0/5)

[← back to tree](/tech-tree/)[browse all →](/tech-tree/inventory/)
