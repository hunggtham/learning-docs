# Machine Learning là gì?

**Machine Learning (ML / 기계학습 / học máy)** nghiên cứu cách xây dựng systems cải thiện performance trên một task bằng data hoặc experience thay vì developer phải encode toàn bộ behavior bằng rules cố định.

Điểm cốt lõi không phải “máy tự học như con người”. Một ML system thường có một model family, parameters, objective, data và optimization procedure. Training thay đổi parameters để model fit statistical structure trong data; deployment dùng learned parameters để tạo prediction hoặc representation cho examples mới.

Machine Learning là một major approach bên trong Artificial Intelligence, không phải synonym của AI. Search, logic, planning và constraint solving vẫn là AI dù không nhất thiết học parameters từ data.

Xem trước: [AI vs ML vs DL vs Generative AI](../00_foundations/05_ai_vs_ml_vs_dl_vs_generative_ai.md).

## Từ explicit rules tới learned mapping

Traditional programming thường có dạng:

```text
Rules + Input → Output
```

Supervised ML:

```text
Training Inputs + Desired Outputs
            ↓
        Learning Algorithm
            ↓
        Learned Model
            ↓
New Input → Prediction
```

Ví dụ spam filter. Viết rule `contains "free" → spam` rất brittle. Một classifier có thể học pattern kết hợp từ sender, token distribution, links, metadata và history.

Nhưng learned model vẫn là software. Developer vẫn quyết định data collection, target, features/representation, model class, objective, evaluation và deployment policy.

## Một formal learning problem

Supervised setting có dataset:

\[
D=\{(x_i,y_i)\}_{i=1}^{n}
\]

Model:

\[
f_\theta:X\rightarrow Y
\]

Prediction:

\[
\hat y=f_\theta(x)
\]

Training tìm parameters:

\[
\theta^*=\arg\min_\theta \hat R(\theta)
\]

với empirical risk:

\[
\hat R(\theta)=\frac{1}{n}\sum_i L(f_\theta(x_i),y_i)
\]

Nhưng objective thật không phải memorize training set. Ta muốn low expected risk trên future data:

\[
R(\theta)=\mathbb{E}_{(X,Y)\sim P_{target}}[L(f_\theta(X),Y)]
\]

Gap giữa empirical performance và future performance là heart of **generalization**.

## Task, Experience, Performance

Một classical definition framing nói program learns from experience `E` with respect to task `T` and performance measure `P` nếu performance tại T, measured by P, improves with E.

Framing này hữu ích vì buộc ta specify:

```text
Task       → model phải làm gì?
Experience → học từ data/interaction nào?
Performance→ đo tốt/xấu bằng gì?
```

Nếu ba thứ mơ hồ, “dùng ML” chưa phải problem definition.

## Supervised Learning

Data có target labels.

Regression:

\[
y\in\mathbb{R}
\]

Ví dụ dự đoán price, demand, latency.

Classification:

\[
y\in\{1,...,K\}
\]

Ví dụ fraud/not-fraud, document category.

Model learns relation between input and target.

## Unsupervised Learning

Không có explicit target label theo supervised sense.

Goals include:

- clustering;
- dimensionality reduction;
- density estimation;
- representation learning;
- anomaly structure discovery.

“Unsupervised” không nghĩa system không có objective; algorithm vẫn optimize criterion such as reconstruction error, likelihood or clustering objective.

## Self-Supervised Learning

Labels được tạo từ data itself.

Language modeling:

```text
context tokens → predict next token
```

Masked modeling:

```text
corrupted input → reconstruct missing content
```

Contrastive learning creates positive/negative pairs from transformations or co-occurrence.

Self-supervision lets model learn from massive unlabeled raw data. Modern foundation models rely heavily on this paradigm.

## Semi-Supervised Learning

Có ít labeled data và nhiều unlabeled data.

Methods may use pseudo-labels, consistency regularization, generative models or representation pretraining.

Goal exploit unlabeled structure without trusting noisy pseudo-labels blindly.

## Reinforcement Learning

Agent interacts with environment and receives reward, not direct correct label for each action.

```text
state → action → transition → reward
```

Challenge includes delayed reward, exploration and policy-dependent data.

RL is learning paradigm distinct from standard supervised learning and will have dedicated folder later.

## Online Learning

Model updates continuously/sequentially as examples arrive.

Useful when distribution changes or data stream large.

Need handle:

- concept drift;
- catastrophic adaptation;
- delayed labels;
- feedback loops.

Online learning is not same as online inference. Model can serve requests online while training offline.

## Batch Learning

Train on fixed dataset snapshot, deploy model, retrain periodically.

Operationally simpler and reproducible.

Many production systems use batch retraining even if inference real-time.

## Instance-Based vs Model-Based Learning

**Instance-based** methods keep training examples and compare new input to stored instances, e.g. k-NN.

**Model-based** methods fit parameters summarizing data, e.g. linear regression.

Trade-off:

```text
store/compute at inference
vs
compress structure into parameters during training
```

## Parametric vs Non-Parametric

Parametric model has fixed-dimensional parameterization independent of dataset size, e.g. linear regression.

Non-parametric methods can grow effective complexity with data, e.g. k-NN, some kernel methods.

“Non-parametric” does not mean “has no parameters”. It means model complexity is not fixed by a finite parameter vector in the same way.

## Generative vs Discriminative

Discriminative model learns:

\[
P(Y\mid X)
\]

or direct decision boundary.

Generative model learns joint/data distribution:

\[
P(X,Y)
\]

or `P(X)`.

Generative modeling can sample data and handle missing/latent structure, but may solve a harder problem than classification needs.

Modern generative AI is broader than old “generative classifier” terminology.

## Representation is part of learning

Raw world must become representation.

Traditional ML:

```text
raw data → hand-engineered features → model
```

Deep Learning:

```text
raw-ish data → learned representations → prediction
```

Feature engineering has not disappeared; system still makes representation choices in tokenization, normalization, aggregation, metadata and architecture.

## Parameters và Hyperparameters

Parameters learned from training data:

```text
weights, coefficients, tree split values...
```

Hyperparameters configured outside inner fitting:

```text
learning rate
regularization strength
tree depth
number of neighbors
architecture choices
```

Hyperparameters may be tuned using validation data. If repeatedly tune against test set, test becomes contaminated.

## Hypothesis Space

Model family defines set of functions algorithm can choose:

\[
\mathcal H=\{f_\theta:\theta\in\Theta\}
\]

Linear model chooses from linear/affine decision surfaces. Deep network defines much richer function class.

Learning algorithm does not search “all possible intelligence”; it searches within model/parameterization and optimization biases.

## Inductive Bias

Finite data can be explained by many hypotheses. To generalize, learner must prefer some solutions.

**Inductive bias (귀납 편향)** includes:

- model architecture;
- regularization;
- optimization;
- data augmentation;
- feature representation;
- pretraining.

There is no learning without assumptions. More detail: [Learning Problem and Inductive Bias](./01_learning_problem_and_inductive_bias.md).

## Generalization

Training performance can be perfect while future performance poor.

Overfitting occurs when model captures sample-specific noise/idiosyncrasies instead of reusable structure.

Underfitting occurs when model/optimization cannot capture relevant structure.

Generalization depends on much more than parameter count: data scale/diversity, inductive bias, optimization, regularization and distribution match all matter.

## Distribution matters

Training examples typically assumed sampled from distribution `P_train`. Deployment target `P_deploy` may differ.

If:

\[
P_{train}\neq P_{deploy}
\]

evaluation can break.

Model “accuracy” is never universal; it is performance over a specified population/time/domain.

## Data is generated by systems

Dataset is not neutral snapshot of reality. It reflects collection policy.

Examples:

- only approved loans have repayment labels;
- recommender only sees feedback on shown items;
- fraud labels depend investigation process;
- medical data reflects who seeks care.

This creates selection bias and feedback loops.

## Loss is not the real-world goal

Training needs tractable mathematical signal such as cross-entropy.

Business goal may be:

```text
reduce fraud loss
while preserving customer experience
```

Loss, metric and decision policy must be connected carefully.

A classifier probability model may be good while chosen threshold makes product bad.

## Prediction vs Decision

Model output:

\[
P(fraud\mid x)=0.72
\]

Decision layer chooses:

```text
approve
manual review
block
```

based on costs, capacity and policy.

Do not encode all business logic implicitly inside model if explicit policy is clearer/auditable.

## Correlation vs Causation

ML predicts associations in observed data. A feature predictive of outcome does not mean intervening on feature changes outcome.

If goal is decision policy that changes world, causal reasoning may be needed.

Example users who contact support may churn more; forcing users to contact support does not imply churn increases.

## Leakage

Model may accidentally access future/target information.

Then training/test metrics look excellent but deployment fails.

Leakage is often more dangerous than choosing “wrong algorithm”.

See [Data, Features and Labels](./02_data_features_and_labels.md).

## Evaluation is part of model definition in practice

A system is not “good” without specified metric and test population.

For imbalanced fraud:

```text
99.9% accuracy
```

could mean trivial always-negative model.

Precision, recall, PR-AUC, expected cost and calibration may matter more.

## Baseline

Before sophisticated model, create simple baseline:

- majority class;
- mean predictor;
- simple rule;
- linear/logistic regression.

If complex system barely beats baseline, added complexity may not justify operational cost.

Baseline also catches pipeline bugs: if model worse than trivial baseline, inspect data and target first.

## No Free Lunch intuition

No algorithm universally best for every possible data-generating process.

Algorithm succeeds because its biases match structure of actual task.

Thus model selection asks:

> What assumptions about data and decision boundary are reasonable here?

not simply “which algorithm is strongest?”.

## ML as compression of experience

Training compresses statistical structure from dataset into parameters/representations.

But compression loses detail and encodes biases. A model does not store a perfect database of training examples even if memorization can occur.

This mental model helps distinguish parameterized knowledge from retrieval databases.

## Model lifecycle

Production ML:

```text
problem definition
→ data collection
→ validation/splitting
→ feature/representation
→ train
→ evaluate
→ decision policy
→ deploy
→ monitor
→ collect feedback
→ retrain/revise
```

Training is one stage, not entire ML system.

## When NOT to use ML

Prefer deterministic software when:

- rules are exact and stable;
- output must be provably correct;
- little/no representative data;
- simple threshold solves task;
- failure cost too high without verification.

Example tax formula should be code/rules. ML may predict missing categories or detect anomalies around it, not replace exact arithmetic.

## Mental Model

```text
Data       = observed experience
Model      = family of possible mappings
Parameters = learned state of model
Loss       = training signal
Optimizer  = mechanism adjusting parameters
Bias       = assumptions selecting among possible explanations
Generalization = useful behavior on unseen target data
Evaluation = evidence that system generalizes for intended use
```

## Common Misconceptions

### “ML tự tìm quy luật nên không cần domain knowledge”

Domain knowledge affects target definition, sampling, features, constraints and evaluation. Bad problem formulation cannot be fixed by stronger model alone.

### “More training accuracy = better model”

Training fit can improve while generalization worsens.

### “Deep Learning thay thế classical ML”

Tabular/small-data/latency-constrained tasks often favor trees, linear models or hybrids.

### “Unsupervised learning has no labels nên model tự hiểu data”

Algorithm still has objective/inductive bias defining what structure counts as useful.

## Knowledge Connection

Machine Learning is where [Statistics](../01_mathematical_foundations/03_statistics_for_ai.md), [Optimization](../01_mathematical_foundations/06_optimization.md) and representation meet. The next chapters will make the learning problem precise before introducing specific algorithms.

Xem tiếp: [Learning Problem and Inductive Bias](./01_learning_problem_and_inductive_bias.md).