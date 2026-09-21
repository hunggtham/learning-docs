# Data Collection

**Data collection (데이터 수집 / thu thập dữ liệu)** là quá trình quyết định cái gì được quan sát, từ đâu, với tần suất nào, dưới permission nào và bằng instrumentation gì. Đây là nơi nhiều bias bắt đầu trước khi model tồn tại.

## Collection Goal phải xuất phát từ Decision Goal

Không thu data chỉ vì “có thể”. Hãy bắt đầu:

```text
business / scientific decision
→ target outcome
→ prediction time
→ required signals
→ collection mechanism
```

Nếu target là fraud decision trong 200 ms, feature chỉ available sau 1 ngày không hữu ích online.

## Source Types

Nguồn data có thể:

- transactional databases;
- application logs;
- sensors;
- third-party APIs;
- user-generated content;
- surveys;
- web/public corpora;
- human annotation;
- synthetic/simulation.

Mỗi source có reliability và legal/privacy constraints khác.

## Instrumentation

Logging event phải có semantics rõ:

```text
event_name
entity_id
event_time
properties
producer_version
```

Schema drift hoặc event rename silently có thể phá feature pipeline.

## Observation Bias

Bạn chỉ collect những gì system hiện tại expose. Recommendation logs không chứa reactions với items chưa từng show.

Đây là exposure bias.

## Sampling Strategy

Nếu collect mọi event quá đắt, sampling cần preserve relevant distribution.

Uniform sampling simple nhưng rare events biến mất. Stratified sampling giữ representation của subgroups/classes.

Sampling probability nên được recorded nếu later weighting needed.

## Temporal Coverage

Data cần cover seasonality:

- weekday/weekend;
- holidays;
- campaigns;
- economic cycles;
- software version changes.

Train trên một tuần bình thường có thể fail Black Friday.

## Sensor Calibration

Physical sensor data phụ thuộc calibration. Drift sensor tạo distribution shift mà model có thể interpret như real-world change.

Calibration metadata cần lineage.

## User Consent và Purpose Limitation

Data collection phải phù hợp consent/legal basis và intended purpose. “Đã collect được” không tự động nghĩa được phép dùng để train mọi model.

## Data Minimization

Collect minimum necessary sensitive data. Extra fields increase security/compliance burden và shortcut risk.

## Identifiers

Stable IDs giúp group/split/lineage nhưng cũng sensitive. Hashing không automatically anonymize nếu domain small hoặc linkage possible.

## Web Data

Web crawling cần quan tâm:

- robots/policies;
- licensing/copyright;
- duplicate mirrors;
- language imbalance;
- spam/SEO content;
- personal data;
- temporal freshness.

Curation often harder than crawling itself.

## Human-Generated Feedback

Ratings/clicks are noisy proxies. Click can mean curiosity, not satisfaction. Absence of click can mean item never seen.

Need understand behavior mechanism before use as label.

## Counterfactual Blindness

System logs chosen action outcome, not outcome of alternatives. Bandit/RL/causal methods may be needed to learn optimal decision, not just prediction.

## Experimentation Data

Randomized experiments produce stronger causal evidence. Logging treatment assignment and eligibility is essential.

Do not train later without preserving experiment semantics.

## Data Contracts

Producer-consumer contract should specify:

```text
schema
semantic definition
freshness SLA
nullability
units
ownership
breaking-change policy
```

Data pipeline is API between teams.

## Late-Arriving Data

Events may arrive delayed/out-of-order. Features based on event time need watermarks/window policy.

Ignoring late events can bias historical aggregates.

## Offline vs Online Feature Availability

A feature easily computed in warehouse may not be available at inference latency. Collection architecture should reflect serving requirements.

## Data Retention

Keep raw data forever is costly/risky. Define retention by purpose, legal requirement and reproducibility needs.

Sometimes store aggregate/derived artifact instead of raw sensitive source.

## Quality at Source

Best cleaning is preventing bad data generation. UI validation, typed APIs, sensor checks and transactional constraints reduce downstream repair.

## Monitoring Collection

Track:

- volume;
- missing rate;
- schema changes;
- latency;
- duplicate rate;
- category distribution;
- source outages.

Sudden 90% drop in event volume should alert before next retraining.

## Example: eKYC

For identity verification, collection may include document images, selfie video, metadata and decision outcome.

Important issues:

- camera/device diversity;
- glare/blur;
- document-country coverage;
- fraud attack samples;
- PII/security;
- whether manual-review outcome is reliable label.

Production coverage often matters more than adding another model layer.

## Mental Model

> **Collection defines the window through which model sees the world. A blind spot in instrumentation becomes a blind spot in learning.**

## Common Misconceptions

### “Collect everything now, decide later”

Creates privacy/cost and ambiguous semantics; not a free option.

### “Logs are objective ground truth”

Logs reflect software behavior and user exposure.

### “Third-party data can be trusted as-is”

Need provenance, license, schema and quality validation.

## Knowledge Connection

Collection connects software instrumentation, databases, privacy and experimental design.

Xem tiếp: [Data Cleaning](./02_data_cleaning.md).