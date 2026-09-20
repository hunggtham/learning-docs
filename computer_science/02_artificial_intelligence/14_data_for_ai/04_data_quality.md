# Data Quality

**Data quality (데이터 품질 / chất lượng dữ liệu)** không phải một score duy nhất. Dataset có thể sạch về format nhưng vẫn kém vì coverage thiếu, labels sai, timestamps stale hoặc distribution lệch deployment.

Một framework thực dụng gồm nhiều dimensions:

```text
correctness
completeness
consistency
uniqueness
freshness
coverage
representativeness
label quality
lineage
availability
```

## Correctness

Value có phản ánh phenomenon thật không? `country=KR` có thể syntactically valid nhưng wrong for user.

Correctness thường cần reference source hoặc domain audit.

## Completeness

Bao nhiêu required information bị missing? Nhưng 100% completeness không guarantee utility; field có thể filled bằng default meaningless value.

## Consistency

Cùng concept có thống nhất across sources/time không?

```text
currency KRW in table A
USD in table B
same field name
```

Semantic inconsistency nguy hiểm hơn schema mismatch rõ ràng.

## Uniqueness

Duplicate examples alter effective weighting. Need entity/event-specific duplicate definition.

## Freshness

Feature/data có update đủ nhanh cho use case? User profile từ 6 tháng trước có thể valid format nhưng stale.

Define freshness SLA per feature/source.

## Coverage

Dataset có chứa cases system sẽ gặp không? Coverage phải analyze theo meaningful dimensions:

- geography;
- device;
- language;
- class;
- time;
- sensor;
- subgroup;
- edge cases.

## Representativeness

Training distribution có tương đồng target deployment distribution? Oversampling có thể intentional, nhưng evaluation/calibration phải account.

## Label Quality

Metrics:

- disagreement;
- adjudication rate;
- known-answer accuracy;
- class-specific noise;
- label latency/maturity.

## Lineage Quality

Nếu không biết data đến từ đâu và transform nào, debug impossible dù values nhìn hợp lý.

## Dataset Health Dashboard

Monitor trends, not just one-time checks:

```text
row/event count
null rate
unique entities
class prior
feature quantiles
category cardinality
freshness
label delay
join failure
```

## Distribution Tests

Compare training/reference vs current data using statistical distances:

- PSI;
- KS statistic;
- Wasserstein distance;
- Jensen-Shannon divergence;
- categorical chi-square-like checks.

No threshold universal; statistical significance can trigger on huge datasets for tiny irrelevant differences. Need business effect size.

## Schema Drift vs Semantic Drift

Schema drift: field type/name changes.

Semantic drift: schema same but meaning changes. Example `status=1` used to mean active, new service version means verified.

Semantic drift harder to detect automatically; versioned contracts help.

## Feature Drift

Input distribution changes:

\[
P_t(X) \neq P_{ref}(X)
\]

Not every drift harms model. Need relate drift to performance/decision.

## Label / Concept Drift

Relationship changes:

\[
P_t(Y|X) \neq P_{ref}(Y|X)
\]

This is more directly harmful but labels often delayed, so detection harder.

## Data Slices

Aggregate quality hides issues. Define critical slices:

```text
new users
rare language
mobile camera model
nighttime
high-value transactions
```

Each slice needs minimum sample size and quality metrics.

## Quality Gates

Before training/deploy data snapshot, enforce gates:

```text
schema passes
no critical feature missing > threshold
label maturity complete
leakage audit passed
coverage minimum met
lineage recorded
```

A failed gate should block pipeline rather than just dashboard red.

## Golden Records

Small curated records with expected transformations help test ETL/feature pipeline end-to-end.

## Data Quality vs Model Metrics

A model may temporarily perform well despite bad data due to redundancy. Data-quality monitoring detects upstream problem before model metric collapses.

## Quality Debt

Teams can accumulate “data debt”: undocumented fields, fragile joins, silently changing sources. This resembles technical debt and slows every later model improvement.

## Quality for Unstructured Data

Text quality:

- encoding;
- spam;
- boilerplate;
- language;
- truncation;
- factual/source reliability.

Image/audio quality:

- corruption;
- resolution;
- blur/noise;
- clipping;
- metadata mismatch.

## Foundation Model Data Quality

Scale introduces mixture-level concerns:

```text
source quality distribution
deduplication
contamination
language balance
repetition
synthetic-content fraction
```

Low-quality repeated data may receive disproportionate optimization weight.

## Data Quality Incident

Example feature pipeline accidentally fills missing risk score with `0` after upstream outage. Schema, null checks all pass because `0` valid. Distribution dashboard reveals sudden spike at zero. This shows quality needs statistical semantics, not only types.

## Mental Model

> **Data quality asks: can this dataset faithfully support the inference/decision we intend, at the time and population where we will use it?**

## Common Misconceptions

### “No nulls = high quality”

Defaults can hide missingness.

### “Data drift = model failure”

Some drift irrelevant; need performance linkage.

### “Quality is preprocessing team responsibility”

Producer, data engineer, ML engineer and domain owner share semantic responsibility.

## Knowledge Connection

Data quality connects observability, contracts, statistics and MLOps monitoring.

Xem tiếp: [Data Leakage](./05_data_leakage.md).