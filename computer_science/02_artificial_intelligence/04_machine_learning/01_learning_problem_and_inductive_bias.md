# Learning Problem và Inductive Bias

Machine Learning chỉ có finite observations nhưng phải predict beyond observations. Đây là một logical gap: vô số functions có thể fit cùng finite training set nhưng behavior hoàn toàn khác ở unseen points. Vì vậy **learning luôn cần inductive bias (귀납 편향 / thiên lệch quy nạp)** — assumptions khiến algorithm ưu tiên một số hypotheses hơn số khác.

Inductive bias không phải “bias xấu” như unfairness. Nó là điều kiện cần để generalize. Câu hỏi đúng không phải “làm sao loại bỏ mọi bias?” mà là “bias nào phù hợp structure của problem và deployment environment?”.

## From data to hypothesis

Dataset:

\[
D=\{(x_i,y_i)\}_{i=1}^{n}
\]

Hypothesis space:

\[
\mathcal H=\{f:X\to Y\}
\]

Learning algorithm maps dataset thành hypothesis:

\[
A(D)=\hat f\in\mathcal H
\]

Nếu nhiều hypotheses đều zero training error, algorithm vẫn phải chọn một.

Selection comes from architecture, objective, regularization, optimization, initialization and data representation.

## Why finite data cannot determine everything

Suppose training points:

```text
x: 1 2 3
 y: 2 4 6
```

Natural hypothesis:

\[
y=2x
\]

But infinitely many functions pass exactly through those three points and differ elsewhere.

For example polynomial with extra term that is zero at x=1,2,3:

\[
y=2x+c(x-1)(x-2)(x-3)
\]

Every `c` fits training data perfectly.

Choosing simple linear relation is an inductive preference.

## Hypothesis space as a structural prior

Linear regression:

\[
f(x)=w^Tx+b
\]

assumes target can be approximated by affine structure in chosen features.

Decision tree assumes useful rules can be built from axis-aligned splits.

CNN assumes locality and translation-related structure.

Transformer assumes sequence can be modeled through learned token interactions with shared layers/attention.

Architecture is not neutral container; it encodes what patterns are easy to represent/learn.

## Occam's Razor

A common principle prefers simpler explanation among equally good fits.

But “simple” depends representation.

A sinusoid is simple in Fourier representation but complex as high-degree polynomial; a convolution is simple under spatial locality.

Therefore Occam's Razor becomes meaningful only after defining description/model language.

## Regularization as explicit preference

Objective:

\[
J(\theta)=\hat R(\theta)+\lambda\Omega(\theta)
\]

L2 penalty:

\[
\Omega(\theta)=\|\theta\|_2^2
\]

prefers smaller parameter magnitude.

L1:

\[
\Omega(\theta)=\|\theta\|_1
\]

encourages sparsity in many settings.

Regularization says multiple functions fit; prefer one satisfying extra structural preference.

## Implicit regularization

No explicit penalty does not mean no regularization/bias.

Gradient descent trajectory, initialization, batch noise, early stopping and parameterization can favor certain solutions.

In overparameterized neural networks, optimizer often finds particular interpolating solutions rather than arbitrary zero-training-loss solution.

This implicit bias is active research topic.

## Data augmentation as invariance bias

Suppose image label should not change under small translation/flip.

Training on transformed samples encodes:

\[
f(x)\approx f(T(x))
\]

for transformations `T` believed label-preserving.

Augmentation is domain assumption, not free improvement. Horizontal flip is fine for cats, but can be invalid for text, traffic signs or medical laterality.

## Equivariance vs invariance

Invariant:

\[
f(Tx)=f(x)
\]

output unchanged.

Equivariant:

\[
f(Tx)=T'f(x)
\]

output transforms predictably.

Image classification may desire translation invariance; segmentation requires output mask shift with image, an equivariant relationship.

Architecture can encode these biases.

## Prior knowledge in Bayesian learning

Bayesian prior:

\[
p(\theta)
\]

explicitly encodes preference before data.

Posterior:

\[
p(\theta\mid D)\propto p(D\mid\theta)p(\theta)
\]

Regularization often corresponds to MAP prior interpretation. L2 is related to Gaussian prior in common formulations; L1 to Laplace prior.

This connection shows “bias” can be written as probability or penalty.

## Empirical Risk Minimization

ERM chooses:

\[
\hat f=\arg\min_{f\in\mathcal H}
\frac{1}{n}\sum_i L(f(x_i),y_i)
\]

Training risk is observable. Population risk is not.

Generalization theory asks when low empirical risk implies low expected risk.

Answer depends capacity, data size/distribution, regularization and algorithmic structure.

## Structural Risk Minimization

Instead of one huge hypothesis class, consider nested classes:

\[
\mathcal H_1\subset\mathcal H_2\subset\cdots
\]

Choose trade-off between empirical fit and complexity.

This formalizes idea:

```text
fit data enough
but avoid unnecessary capacity
```

Modern Deep Learning complicates simple capacity story because huge models can generalize despite enough parameters to memorize.

## VC dimension intuition

VC dimension measures ability of hypothesis class to shatter sets of points in binary classification.

Higher VC dimension means richer class.

It supports bounds roughly relating:

```text
sample size
model capacity
generalization gap
```

But VC theory is often too loose to explain practical behavior of massive neural networks quantitatively. It remains important conceptual foundation.

## Bias–variance

A model class too rigid may have high bias; predictions systematically miss structure.

A highly flexible learner can have high variance; small dataset changes produce large model changes.

Classical decomposition under squared-error assumptions:

\[
ExpectedError=Bias^2+Variance+Noise
\]

This is a mental model, not universal full theory.

See [Bias, Variance and Generalization](./14_bias_variance_and_generalization.md).

## Underfitting

Symptoms:

```text
training error high
validation error also high
```

Possible causes:

- features missing useful information;
- model too restrictive;
- excessive regularization;
- optimization not converged.

Adding data alone often does not solve strong underfitting.

## Overfitting

Typical pattern:

```text
training error very low
validation error significantly worse
```

Possible causes:

- flexible model + insufficient data;
- leakage-like artifacts;
- repeated validation tuning;
- spurious correlations;
- weak regularization.

Overfitting is relative to target distribution and evaluation procedure.

## Memorization vs generalization

Models can memorize rare examples while also generalize elsewhere. These are not mutually exclusive binary states.

Large neural networks can interpolate training set but learn useful representations due to data scale and inductive biases.

So “parameter count > sample count ⇒ overfit” is not a reliable modern rule.

## Interpolation and extrapolation

Interpolation predicts within region covered by training distribution.

Extrapolation predicts outside observed range/structure.

Many ML models are much less reliable under extrapolation.

A model trained on incomes 0–100k may behave strangely at 10 million even if formula returns a number.

Confidence should not be inferred from mere ability to compute output.

## Spurious correlation

A feature may correlate with label in training environment but not causally/reliably.

Example image classifier learns hospital watermark instead of disease pattern because watermark correlates with labels.

Training/test random split from same hospitals may not reveal problem. External-site split might.

Inductive bias includes assumptions about which correlations will persist.

## Shortcut learning

Neural models often exploit easiest predictive signal rather than intended concept.

If dataset allows background color to predict class, model may ignore object shape.

This is not model “cheating”; objective rewards prediction, not human-intended reasoning.

Dataset/evaluation must remove or challenge shortcuts.

## Distributional assumptions

Standard supervised learning often assumes train and test are i.i.d. from same distribution.

Reality:

\[
P_{train}(X,Y)\neq P_{deploy}(X,Y)
\]

Under shift, a bias that worked historically may fail.

Robustness requires designing validation splits and monitoring around plausible shifts.

## Domain shift and invariants

If environments vary, seek relationships stable across them.

Examples:

```text
hospital A vs B
country A vs B
winter vs summer
old device vs new device
```

Learning invariant causal-ish structure is harder than fitting pooled correlations. Domain generalization methods attempt this, but guarantees require assumptions.

## Feature representation changes simplicity

A nonlinear problem in raw feature may become linear after transformation.

Example circular boundary can be easier using radius:

\[
r^2=x_1^2+x_2^2
\]

Then threshold on `r` suffices.

Feature engineering alters hypothesis complexity needed downstream.

Deep Learning learns transformations automatically to make target easier for later layers.

## Kernel trick as representational bias

Kernel methods implicitly map inputs to high-dimensional feature space:

\[
\phi(x)
\]

without computing coordinates explicitly, using:

\[
k(x,x')=\langle\phi(x),\phi(x')\rangle
\]

Choice of kernel encodes similarity bias.

RBF kernel assumes nearby points in feature space should behave similarly.

## Locality bias

k-NN assumes nearby examples likely share target.

This only works if distance metric aligns with semantic relevance.

In high dimensions/raw mixed-scale data, Euclidean distance may be meaningless.

Thus even “model-free” method has strong inductive bias.

## Tree bias

Decision trees partition feature space using hierarchical threshold rules.

They naturally model interactions and nonlinearities but axis-aligned partitions can be inefficient for diagonal smooth boundaries.

Ensembles reduce instability while keeping tree-based bias useful for tabular data.

## Pretraining as inductive prior

A pretrained model starts not from random ignorance but parameters shaped by massive prior data.

Fine-tuning with small task dataset uses representation prior:

```text
general patterns from pretraining
+ task-specific evidence
```

This changes sample efficiency dramatically.

Foundation models can be viewed as learned priors/representations reused across tasks.

## Transfer learning assumptions

Transfer works when source pretraining structure useful for target.

Negative transfer can occur when domains/tasks differ or inherited biases harmful.

“Pretrained is always better” is not guaranteed.

## Multi-task learning

Shared model learns several tasks:

\[
L=\sum_t\lambda_t L_t
\]

Shared representations can regularize/help if tasks related. Conflicting gradients may hurt.

Task relatedness is another inductive assumption.

## Human choices as hidden bias

Bias enters before algorithm:

```text
what problem to automate?
who appears in dataset?
what label means "success"?
which metric optimized?
which errors tolerated?
```

Technical model bias and social/fairness bias overlap but are not identical concepts.

## No Free Lunch

Averaged uniformly over all possible target functions, no learner dominates all others in classic No Free Lunch settings.

Practical meaning:

> Learning works because real-world tasks have structure and our models exploit assumptions about that structure.

Do not interpret as “all algorithms equal”. On actual domains, some inductive biases match far better.

## Choosing model family

Ask:

```text
How much data?
What data type?
Expected nonlinearity/interactions?
Need interpretability?
Latency/memory constraints?
Distribution shifts?
Hard monotonic/physical constraints?
```

Model selection should follow problem structure, not popularity.

## Mental Model

```text
Finite data cannot uniquely determine future behavior.
Inductive bias chooses which explanation to prefer.

Architecture     → representational bias
Regularization   → parameter/function preference
Optimization     → solution-selection bias
Data augmentation→ invariance assumptions
Pretraining      → learned prior
Features         → change geometry/simplicity of task
```

## Common Misconceptions

### “Bias là thứ phải loại bỏ”

Inductive bias is necessary for generalization. Unfair societal bias is a different but related concern.

### “More flexible model always better”

Flexibility helps fit but needs data/bias/evaluation to generalize.

### “A model that fits all training data learned the truth”

Many functions can interpolate same observations.

### “Architecture only affects compute”

Architecture encodes strong assumptions about locality, sequence, invariance and composition.

## Knowledge Connection

Inductive bias connects Statistics, Optimization and model architecture. Every algorithm chapter later should be read as: **what assumptions does this method encode, and when are those assumptions useful or dangerous?**

Xem tiếp: [Data, Features and Labels](./02_data_features_and_labels.md).