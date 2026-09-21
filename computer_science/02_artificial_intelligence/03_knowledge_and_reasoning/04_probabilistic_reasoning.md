# Probabilistic Reasoning trong Artificial Intelligence

Classical logic asks whether proposition follows or not. Real AI often cannot work with binary certainty. Sensor noisy, diagnosis ambiguous, user intent uncertain và knowledge incomplete. **Probabilistic Reasoning (확률적 추론)** extends reasoning by assigning and updating degrees of belief under a probability model.

The core question changes from:

> Is hypothesis H logically entailed?

to:

> Given evidence E, how should belief `P(H|E)` change?

Xem trước: [Probability for AI](../01_mathematical_foundations/02_probability_for_ai.md) và [Inference and Reasoning](./03_inference_and_reasoning.md).

## Uncertainty is not ignorance alone

Uncertainty can come from:

- inherent randomness;
- measurement noise;
- hidden variables;
- incomplete knowledge;
- limited data;
- model approximation.

A single probability number may mix several sources. Good system design tries separate what can be reduced by more information from what is irreducible.

## Bayesian update

Bayes' rule:

\[
P(H\mid E)=\frac{P(E\mid H)P(H)}{P(E)}
\]

Interpretation:

```text
prior belief
   ×
likelihood of evidence under hypothesis
   ↓
posterior belief
```

Normalization `P(E)` makes probabilities sum to 1.

## Odds form

Bayes can be expressed with odds:

\[
\frac{P(H\mid E)}{P(\neg H\mid E)}
=
\frac{P(H)}{P(\neg H)}
\times
\frac{P(E\mid H)}{P(E\mid\neg H)}
\]

Likelihood ratio tells how strongly evidence shifts odds.

This is useful in medical testing and evidence accumulation.

## Base rate matters

Rare-event detection often suffers base-rate neglect.

Even high sensitivity/specificity may yield low posterior positive probability when prevalence very low.

Fraud, anomaly detection and security alerts require careful base rates; otherwise false positives dominate.

## Multiple evidence

If evidence `E1,E2` conditionally independent given H:

\[
P(E_1,E_2\mid H)=P(E_1\mid H)P(E_2\mid H)
\]

Then likelihoods multiply.

But naive independence assumptions can double-count correlated evidence.

Example two fraud signals derived from same IP reputation source are not independent just because represented as separate features.

## Naive Bayes

Naive Bayes assumes features conditionally independent given class:

\[
P(x_1,...,x_d\mid y)=\prod_i P(x_i\mid y)
\]

Then:

\[
P(y\mid x)\propto P(y)\prod_i P(x_i\mid y)
\]

Assumption often false, yet classifier can work surprisingly well because decision boundary may still be useful and estimation easy.

This is lesson: model assumptions can be wrong literally but useful operationally.

## Generative vs discriminative modeling

Generative classifier models joint structure:

\[
P(X,Y)=P(Y)P(X\mid Y)
\]

Discriminative model directly models:

\[
P(Y\mid X)
\]

Naive Bayes generative; logistic regression discriminative.

Generative model can sample/model input conditional on class; discriminative focuses decision boundary.

## Latent variables

A latent variable `Z` is not directly observed but helps explain observed data `X`.

\[
P(X)=\sum_z P(X,Z)
\]

or continuous integral.

Examples:

- hidden topic causing word distribution;
- hidden disease causing symptoms;
- hidden state causing sensor observations.

Latent variables compress explanatory structure but introduce inference challenge.

## Marginalization

To reason about observed variables while hidden variable unknown:

\[
P(X)=\sum_z P(X,Z)
\]

This “sum over possibilities” can be computationally expensive when many hidden variables.

Probabilistic inference complexity often comes from exponential number joint assignments.

## Conditioning

When observe evidence `E=e`, posterior restricts/renormalizes distribution:

\[
P(X\mid E=e)
\]

In graphical models, evidence can propagate belief through network.

Observation can make previously independent variables dependent — phenomenon called **explaining away**.

## Explaining away

Suppose burglary `B` and earthquake `E` can both cause alarm `A`:

```text
B → A ← E
```

Before observing alarm, B and E may be independent.

After observe `A=true`, learning `B=true` reduces need to believe earthquake caused alarm, so B and E become dependent conditioned on A.

Collider structure is central in probabilistic/causal graphs.

## Conditional independence

Notation:

\[
X\perp Y\mid Z
\]

means X and Y independent when conditioned on Z.

Graphical Models encode many conditional independence relations compactly, allowing factorization of huge joint distribution.

Without factorization, joint table over `n` binary variables requires:

\[
2^n
\]

entries.

## Factorization

Instead of full joint:

\[
P(X_1,...,X_n)
\]

use product local factors:

\[
\prod_i \phi_i(X_{S_i})
\]

Bayesian Network factors conditional distributions; Markov Random Field uses undirected potentials.

Factorization is the probabilistic equivalent of exploiting structure instead of brute force enumeration.

## Exact inference

Exact methods compute posterior exactly under model:

- variable elimination;
- belief propagation on trees/polytrees;
- junction tree.

Complexity depends graph structure/treewidth, not just number variables.

Dense dependencies can make exact inference exponential.

## Variable elimination

Suppose want:

\[
P(A\mid E=e)
\]

We multiply relevant factors and sum hidden variables in chosen order.

Elimination order strongly affects size of intermediate factors.

This resembles database join-order optimization: mathematically same result, computational cost can vary dramatically.

## Approximate inference

When exact inference too expensive, use approximation:

- Monte Carlo sampling;
- importance sampling;
- MCMC;
- variational inference;
- loopy belief propagation.

Approximation trades correctness exactness for tractability.

Need monitor convergence/error; “algorithm returned number” does not mean posterior accurate.

## Monte Carlo

Sample hidden configurations:

\[
z^{(1)},...,z^{(N)}\sim P
\]

estimate expectation:

\[
\mathbb{E}[f(Z)]\approx\frac1N\sum_i f(z^{(i)})
\]

Error typically shrinks around `O(1/√N)` under standard independent sampling, making high precision expensive.

## Importance sampling

If target distribution hard sample but proposal `q` easy:

\[
\mathbb{E}_p[f(X)]
=
\mathbb{E}_q\left[f(X)\frac{p(X)}{q(X)}\right]
\]

Importance weights explode if `q` poorly covers regions where `p` has mass, causing high variance.

This theme appears again in off-policy RL.

## Markov Chain Monte Carlo

MCMC constructs Markov chain whose stationary distribution is target.

Methods include Metropolis–Hastings, Gibbs Sampling.

Samples correlated; burn-in/mixing/convergence diagnostic matter.

High-dimensional multimodal distributions can mix slowly.

## Variational inference

Choose tractable distribution family `q_φ(z)` approximate posterior `p(z|x)` by optimization.

Often minimize:

\[
D_{KL}(q_\phi(z)\|p(z\mid x))
\]

Equivalent maximize ELBO:

\[
\log p(x)\ge
\mathbb{E}_{q}[\log p(x,z)-\log q(z)]
\]

Variational inference turns inference into optimization, usually faster but introduces approximation bias.

## Maximum likelihood and Bayesian inference

MLE chooses point estimate:

\[
\theta_{MLE}=\arg\max_\theta P(D\mid\theta)
\]

Bayesian inference keeps posterior distribution:

\[
P(\theta\mid D)
\]

Full posterior expresses parameter uncertainty but is often computationally expensive in neural networks.

Approximate Bayesian deep learning uses ensembles, variational methods or other uncertainty approximations.

## Predictive distribution

Bayesian prediction integrates parameters:

\[
P(y\mid x,D)=\int P(y\mid x,\theta)P(\theta\mid D)d\theta
\]

Rather than commit to one `θ`, average predictions weighted by posterior plausibility.

Deep ensembles approximate model uncertainty differently by training multiple models.

## Calibration

Probabilistic reasoner should not only rank correctly but probabilities should match empirical frequencies when interpretation requires.

Calibration can degrade under distribution shift.

A model calibrated on US customers may be miscalibrated on Korean customers if conditional relationships differ.

## Evidence and likelihood are model-dependent

Posterior is only as good as likelihood/prior assumptions.

Bayes theorem itself is mathematically exact, but wrong model gives wrong posterior.

This mirrors formal logic: valid inference from false premises is still formal-valid but real-world wrong.

## Prior sensitivity

With little data, prior strongly influences posterior. With abundant informative data, likelihood often dominates under regular conditions.

In high-dimensional models, “uninformative prior” is not simple; parameterization matters.

Prior encodes inductive bias, not something to hide.

## Bayesian decision theory

Posterior alone not action. Choose action minimize posterior expected loss:

\[
a^*=\arg\min_a\mathbb{E}_{\theta\mid D}[L(a,\theta)]
\]

This connects probabilistic inference to [Decision Making Under Uncertainty](../02_search_reasoning_and_planning/06_decision_making_under_uncertainty.md).

## Probabilistic graphical models

Two major forms:

**Bayesian Network** — directed acyclic graph; local conditional probabilities.

**Markov Random Field** — undirected graph; potentials/factors.

Factor Graph explicitly separates variable and factor nodes.

These representations expose conditional structure for inference.

## HMM

Hidden Markov Model has latent state sequence:

```text
Z1 → Z2 → Z3 → ...
↓    ↓    ↓
X1   X2   X3
```

Assumptions:

\[
P(Z_t\mid Z_{<t})=P(Z_t\mid Z_{t-1})
\]

and observations conditionally dependent on current state.

Algorithms:

- Forward algorithm → likelihood/filtering;
- Viterbi → most likely state sequence;
- Forward–Backward → posterior marginals.

HMM historically central in speech/NLP before Deep Learning.

## Kalman Filter

Linear-Gaussian state-space model permits exact recursive Bayesian filtering with Gaussian beliefs.

It predicts next state then corrects using observation.

Kalman gain balances model uncertainty and measurement uncertainty.

This is probabilistic reasoning deployed in navigation/tracking/control.

## Probabilistic programming

Languages like Stan, PyMC-like ecosystems let user specify generative model and perform inference via MCMC/VI.

This separates model specification from inference engine similarly to declarative logic.

But inference quality/computation still depend model geometry and algorithm.

## Uncertainty in LLMs

LLM next-token probabilities are conditional sequence probabilities, not directly “truth probabilities”.

A token can have high probability because it is linguistically likely despite claim being false.

Therefore:

```text
P(token | context)
≠
P(statement is true | world evidence)
```

This distinction is fundamental to hallucination/grounding.

## Self-reported confidence

Asking LLM “How confident are you?” produces text generated from same model, not automatically calibrated posterior about correctness.

Confidence estimation requires explicit evaluation/calibration methods, ensembles, consistency signals, external verification or task-specific models.

## Probabilistic RAG

Retrieval introduces uncertainty:

```text
query intent uncertain
retriever ranking uncertain
document truth/freshness uncertain
LLM interpretation uncertain
```

Reliable RAG should treat retrieval score as ranking signal, not guaranteed relevance/truth.

Reranking, citations and source validation reduce uncertainty at different stages.

## Mental Model

```text
Logic         → what must follow if premises true
Probability   → how belief is distributed under uncertainty
Bayes         → update belief with evidence
Factorization → exploit conditional structure
Inference     → compute posterior/marginals/expectations
Approximation → trade exactness for tractability
Decision      → combine posterior with utility/cost
```

## Common Misconceptions

### “Bayesian means probabilities are always correct”

Posterior depends model, prior, likelihood and data quality.

### “LLM probability = factual confidence”

Next-token likelihood is not calibrated truth probability.

### “Exact inference is always preferable”

Exact may be infeasible; approximate inference can be only practical option.

### “Conditional independence means variables unrelated”

They can be dependent marginally but independent given a third variable.

## Knowledge Connection

Probabilistic Reasoning bridges Probability, Knowledge Representation and Decision Theory. [Bayesian Networks](./05_bayesian_networks.md) will make the conditional-dependency structure concrete, while later Machine Learning chapters will show how models estimate these distributions from data.