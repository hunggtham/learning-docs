# Data Leakage

**Data leakage (데이터 누수 / rò rỉ dữ liệu)** xảy ra khi training/evaluation pipeline cho model access information mà production inference sẽ không thực sự có, hoặc khi information từ validation/test ảnh hưởng training. Leakage tạo metrics đẹp giả tạo và thường là một trong những failure nghiêm trọng nhất của ML system.

## Target Leakage

Feature chứa trực tiếp hoặc gián tiếp information về target sau thời điểm prediction.

Ví dụ dự đoán fraud tại transaction time nhưng feature chứa:

```text
chargeback_status
manual_investigation_result
post-transaction dispute count
```

Model không “thông minh”; nó nhìn tương lai.

## Temporal Leakage

Feature aggregate vô tình include future events.

Ví dụ muốn predict churn ngày 1/9 nhưng tính “number of support tickets in September” bằng full-month table.

Correct feature cần as-of query:

```text
only events with event_time <= prediction_time
```

## Train/Test Contamination

Same or near-duplicate entity appears both sides:

- frames từ same video;
- records của same patient;
- copied web documents;
- repeated customer transactions;
- augmented versions of same image.

Random row split không đủ khi observations correlated by group.

## Preprocessing Leakage

Fit scaler/PCA/imputer/vocabulary on full dataset trước split:

\[
\mu = mean(train+test)
\]

Test distribution ảnh hưởng transform training. Correct pattern:

```text
fit transform on train
apply frozen transform to val/test
```

## Feature Selection Leakage

Nếu chọn features dựa trên correlation với target computed over entire data including test, test đã influence model design.

Selection/hyperparameter tuning phải nằm trong training/validation process.

## Cross-Validation Leakage

Preprocessing outside CV folds leaks fold information. Pipeline phải refit transforms inside each training fold.

## Label Leakage Through Human Process

Human-created fields may encode outcome indirectly. Example analyst writes note after resolving case; text contains “confirmed fraud”. If model is supposed to triage before analyst resolution, note is illegal feature.

## Proxy Leakage

Feature itself technically available but only because current production process already uses target outcome.

Example `queue=fraud_team` indicates upstream rule already decided case suspicious. Model appears strong but adds no independent predictive power and may fail if routing logic changes.

## Identifier Leakage

IDs can encode time/source/category unintentionally. Model memorizes entity or batch rather than general signal.

High-cardinality IDs should be scrutinized even if not obvious target.

## Duplicate Leakage in Foundation Models

Evaluation benchmark text may exist verbatim or paraphrased in pretraining corpus. Model score then mixes generalization and memorization.

Contamination detection uses exact hashes, n-gram similarity, semantic matching and source provenance, but perfect detection is difficult.

## RAG Evaluation Leakage

If evaluator answer is included in indexed corpus in an artificial way not representative production, RAG may retrieve gold answer directly. Need construct realistic retrieval corpus.

## Time-Based Split

For future prediction systems, train past → validate/test future often best approximates deployment:

```text
train: Jan-Jun
val: Jul
 test: Aug
```

But seasonality/regime shift can make one time split noisy; rolling backtests help.

## Group Split

Group all observations of entity into same split:

```text
patient_id
user_id
company_id
device_id
video_id
```

prevents memorization across correlated records.

## Spatial Leakage

Geospatial data nearby locations correlated. Random points split can overestimate generalization to new regions. Spatial block split may be needed.

## Leakage Audit Questions

For each feature:

1. feature được generated khi nào?
2. source event xảy ra trước prediction time không?
3. production path có compute được cùng logic không?
4. target hoặc downstream decision có ảnh hưởng feature không?
5. same entity/data derivative có xuất hiện test không?

## Feature Store Point-in-Time Join

Correct historical training join selects latest feature value available before event time, not current latest record.

This is core function of temporal feature stores.

## Hidden Leakage Through Aggregates

A monthly aggregate may have timestamp first day of month nhưng calculated after month end. Timestamp field alone cannot prove availability; lineage must record **availability time**.

## Hyperparameter Overfitting

Repeatedly inspect test score and adjust model turns test set into informal validation set. Final metric optimistic.

Need hidden final holdout or nested evaluation discipline.

## Early Stopping

Using validation for early stopping is legitimate because validation is part of model selection. But final test must remain untouched until selection complete.

## Leakage Detection Signals

Suspicious signs:

- unrealistically high metric;
- one feature dominates importance;
- test performance collapses in future split;
- model works offline but not online;
- feature correlation appears after outcome timestamp.

High performance is not proof of leakage, but deserves audit.

## Example: Credit Risk

Feature `days_past_due_current` may be valid for predicting future 12-month default at current date, but invalid if goal is predict default at loan origination. Same field legality depends prediction timestamp.

Thus leakage is task-definition relative.

## Mental Model

> **Leakage means model receives information from outside the information boundary that will exist at the moment of real decision.**

Think like time traveler/auditor, not like dataframe programmer.

## Common Misconceptions

### “Leakage chỉ là target column accidentally included”

Temporal aggregates, duplicates, human workflow and preprocessing are more subtle common forms.

### “Random split prevents leakage”

Not for time/group/spatial correlated data.

### “If feature exists in database, it is fair to use”

It may not exist yet at prediction time.

## Knowledge Connection

Leakage connects temporal databases, causal process understanding and evaluation design.

Xem tiếp: [Dataset Bias](./06_dataset_bias.md).