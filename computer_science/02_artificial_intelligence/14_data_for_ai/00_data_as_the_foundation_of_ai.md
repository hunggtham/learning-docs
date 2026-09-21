# Data as the Foundation of AI

Một AI model chỉ học được từ information mà data pipeline quan sát và giữ lại. Vì vậy **data (데이터)** không phải nguyên liệu trung tính; nó là kết quả của measurement, selection, labeling, logging và policy.

Mental model:

```text
Real world
→ measurement / event logging
→ raw data
→ filtering / labeling / transformation
→ training dataset
→ model
→ decisions
→ new real-world behavior/data
```

Loop cuối quan trọng: deployed AI có thể thay đổi data tương lai.

## Dataset không phải Reality

Dataset chỉ là sample từ process tạo data. Nếu process đó biased, model học bias của process.

Ví dụ loan dataset chỉ có repayment outcomes cho applicants đã được approve. Ta không observe counterfactual của rejected applicants.

## Data Generating Process

Một useful question:

> Data này xuất hiện bằng cơ chế nào?

Need understand:

- ai tạo event;
- sensor/log nào capture;
- trường hợp nào bị missing;
- policy nào quyết định inclusion;
- label được xác định khi nào;
- deployment khác collection environment ra sao.

## Observational Data

Most production ML data is observational, not randomized experiment. Correlation may reflect confounding or selection effects.

Prediction may still work if deployment distribution similar, nhưng causal interpretation cần caution.

## Data Schema

Schema không chỉ data types; cần semantic contract:

```text
field meaning
unit
time semantics
nullable rules
source
version
allowed range
privacy class
```

`amount=100` vô nghĩa nếu không biết currency/unit/time.

## Event Time vs Processing Time

Streaming/transaction systems distinguish:

```text
event_time      → when real-world event happened
processing_time → when pipeline received/processed it
```

ML leakage often occurs when feature computed using information available only after prediction time.

## Point-in-Time Correctness

Training example at time `t` chỉ được use information that would have existed at `t` in production.

```text
prediction time = 10:00
feature uses chargeback discovered at 14:00
→ leakage
```

Feature store/history queries need as-of semantics.

## Unit of Observation

Dataset row may represent:

- user;
- transaction;
- session;
- image;
- document;
- time window.

Incorrect unit can create duplicate weighting or leakage. Example splitting multiple images from same patient across train/test.

## Sampling

Training distribution may intentionally oversample rare positives. This helps learning but changes class prior.

If deployment prior differs, probability calibration/threshold selection must account for sampling.

## Coverage

Dataset should cover intended operational space:

```text
languages
devices
regions
lighting/noise
customer segments
rare edge cases
```

No model can generalize reliably to regions absent from training without assumptions/transfer.

## Long Tail

Real-world categories often follow heavy-tailed frequency. Common cases dominate data; rare but important failures have little supervision.

Long-tail strategy may require targeted collection, reweighting, synthetic data or separate rules.

## Duplicate Data

Duplicates inflate effective sample count and can leak across splits.

Near-duplicate detection is harder than exact hashes: resized/cropped images, copied documents, paraphrases.

## Data Versioning

Dataset is an artifact. Need know:

```text
source snapshots
transform code version
filters
label version
split definition
hash / manifest
```

Without versioning, experiment cannot reproduce.

## Data Lineage

Lineage tracks where each feature/dataset comes from:

```text
source DB table
→ ETL job
→ feature transform
→ training dataset
→ model version
```

Critical for debugging, compliance and impact analysis.

## Feedback Loops

Recommendation model shows items → users interact with shown items → logs become next training data. Model influences what evidence it later sees.

This can amplify popularity bias or hide alternatives.

## Selective Labels

We observe outcome only after specific decision. Examples:

- loan default only for approved loans;
- medical result only for tested patients;
- fraud confirmed only for investigated transactions.

This violates simple i.i.d. assumptions and may require exploration/causal methods.

## Missing Data

Missingness mechanisms matter:

- MCAR: missing unrelated to variables;
- MAR: missing depends observed data;
- MNAR: missing depends unobserved value/process.

Imputation cannot magically recover arbitrary MNAR information.

## Structured vs Unstructured Data

Structured data has explicit schema; unstructured text/image/audio still has metadata, provenance and latent structure. “Unstructured” does not mean schema-free pipeline.

## Data for Foundation Models

At web scale, curation includes:

- deduplication;
- language identification;
- quality filtering;
- safety filtering;
- license/provenance;
- contamination removal;
- mixture weighting.

Data mixture is effectively part of training objective: more tokens from domain → more optimization attention to that domain.

## Benchmark Contamination

If evaluation examples appear in training/pretraining, benchmark no longer estimates generalization cleanly.

Exact match insufficient because paraphrases/derived sources may contaminate.

## Data Quantity vs Quality

More data often helps, but low-quality duplicated/noisy data can waste compute or teach harmful patterns.

Effective data value depends diversity, relevance, correctness and coverage, not row count alone.

## Active Learning

Instead label random examples, model identifies uncertain/informative examples for annotation. This can improve label efficiency but uncertainty heuristic may miss systematic blind spots.

## Data-Centric AI

When pipeline/model baseline stable, improving labels, coverage and definitions often gives more gain than architecture tweaks.

Data-centric approach does not mean model unimportant; it means treat data quality as an engineering object.

## Privacy

Training data may contain personal/sensitive information. Collection needs purpose limitation, minimization, retention and access controls.

Anonymization is difficult for high-dimensional data; text/images can re-identify indirectly.

## Mental Model

> **Dataset là một instrumented view của reality, produced by a process. Muốn hiểu model, phải hiểu process tạo dataset.**

## Common Misconceptions

### “Data speaks for itself”

Data meaning depends measurement, schema and selection.

### “More rows always improve model”

Duplicates/noise/coverage imbalance reduce marginal value.

### “Random train/test split luôn đúng”

Time/group/entity dependencies often require different splitting.

## Knowledge Connection

Data layer connects Statistics, Databases, Distributed Systems, Privacy và ML evaluation.

Xem tiếp: [Data Collection](./01_data_collection.md).