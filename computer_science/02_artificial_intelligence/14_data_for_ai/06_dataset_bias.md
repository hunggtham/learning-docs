# Dataset Bias

**Dataset bias (데이터 편향 / thiên lệch dữ liệu)** là systematic mismatch giữa data được quan sát và phenomenon/population mà model intended serve. Bias không chỉ là “class imbalance”; nó có thể đến từ sampling, measurement, labels, historical decisions và deployment feedback loops.

## Selection Bias

Examples được include không random relative target population.

Ví dụ hospital dataset chỉ chứa people who sought care. Model trained to estimate disease prevalence từ dataset đó may overestimate relative general population.

## Sampling Bias

Some subgroups underrepresented:

```text
camera devices
languages
regions
age groups
rare classes
```

Model may have high aggregate performance but weak subgroup reliability.

## Measurement Bias

Feature/label measurement quality differs across groups. Example image quality lower on certain devices, or diagnostic test sensitivity differs.

Same model may appear “biased” partly because sensor quality differs.

## Historical Bias

Data reflects historical human/system decisions. Hiring records encode who was hired under previous policy, not objective “true talent”.

Learning historical outcome can reproduce past inequity.

## Label Bias

Human labels may systematically differ by subgroup. Moderation/toxicity judgments can reflect dialect/cultural bias.

Need audit annotator agreement by subgroup, not only global.

## Representation Bias

Common groups dominate feature learning. Rare language/accent may have poorer embeddings/ASR even if labels themselves correct.

## Aggregation Bias

One global model assumes same mapping for heterogeneous populations. If mechanisms differ, pooled model can hurt some groups.

Separate models or group-aware features may help, but must consider fairness/privacy/legal constraints.

## Evaluation Bias

Benchmark itself unrepresentative. Model optimized to benchmark becomes good at measured slice, not intended world.

## Survivorship Bias

Only successful/remaining entities observed. Churned or failed cases disappear from later data, distorting conclusions.

## Feedback Loops

Model decisions affect future data:

```text
rank popular item higher
→ gets more clicks
→ appears even more popular
```

Popularity reinforcement can reduce exposure diversity.

## Proxy Variables

Even if protected attribute removed, other features (postcode, school, language) may strongly proxy it.

“Fairness through unawareness” is insufficient.

## Simpson’s Paradox

Aggregate relationship can reverse within subgroups. Always inspect relevant conditional slices before causal/fairness conclusions.

## Fairness Metrics Trade-offs

Different fairness definitions can conflict when base rates differ:

- demographic parity;
- equal opportunity/TPR parity;
- equalized odds;
- calibration.

No metric universally correct; choice depends social/legal decision context.

## Bias vs Variance

Dataset bias here is social/statistical sampling concept, distinct from ML **bias–variance trade-off**. Same word, different meanings.

## Reweighting

If target population distribution known, importance weights:

\[
w(x)=\frac{P_{target}(x)}{P_{train}(x)}
\]

can adjust training/evaluation under covariate shift assumptions.

But high weights increase variance and cannot fix missing support where `P_train(x)=0`.

## Resampling

Oversampling minority groups/classes increases training exposure. Undersampling majority reduces imbalance but discards data.

Synthetic oversampling may interpolate examples but can amplify artifacts.

## Targeted Data Collection

Often best fix is collect more real data in weak slices rather than complex reweighting.

Model error analysis should drive collection priorities.

## Slice-Based Evaluation

Define metrics per subgroup/context:

```text
language
region
skin tone (when ethically/legally appropriate)
device
lighting
transaction amount band
new vs existing users
```

Slices should correspond real risk, not endless arbitrary combinations.

## Intersectionality

Bias can appear only at intersection of groups, e.g. language + age + device. Data sparsity makes intersection analysis statistically hard.

Need confidence intervals/minimum sample rules.

## Counterfactual Fairness Intuition

Ask whether decision would change if protected characteristic changed while relevant underlying factors held appropriately constant. Formal causal definitions require causal model and strong assumptions.

## Bias in Foundation Models

Web-scale text/image data reflects societal stereotypes and uneven language/geographic representation.

Filtering can reduce harmful content but also erase minority dialects/topics if classifiers biased.

## Synthetic Data and Bias

Generating synthetic data from biased model can reproduce or amplify bias. Synthetic balancing only helps if generator accurately represents target subgroup.

## Label Policy as Value Choice

Moderation/helpfulness/safety labels encode normative choices. Dataset documentation should make these policies explicit.

## Dataset Documentation

Datasheets/model cards style documentation can include:

- motivation;
- composition;
- collection process;
- preprocessing;
- uses/limitations;
- demographic/geographic coverage;
- licensing;
- known biases.

Documentation does not remove bias but makes assumptions inspectable.

## Bias Mitigation Layers

Mitigation can happen:

```text
pre-processing → data collection/reweighting
in-processing  → constraints/loss
post-processing→ thresholds/calibration/policy
```

Fixing dataset/process source is often more durable than post-hoc threshold hacks.

## Mental Model

> **Bias asks whose reality dataset represents, whose it misses, và cơ chế selection/measurement nào tạo ra mismatch đó.**

## Common Misconceptions

### “Balanced class counts = unbiased dataset”

Bias can remain in subgroup coverage, measurement and labels.

### “Remove protected attribute = fair model”

Proxy features and historical outcomes still encode it.

### “Fairness has one correct mathematical metric”

Metrics encode different normative criteria and can conflict.

## Knowledge Connection

Dataset bias connects sampling theory, causal inference, fairness, social systems and deployment feedback.

Xem tiếp: [Synthetic Data](./07_synthetic_data.md).