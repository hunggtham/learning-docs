# Data Cleaning

**Data cleaning (데이터 정제 / làm sạch dữ liệu)** không phải thao tác “xóa những hàng xấu” một cách máy móc. Nó là quá trình phát hiện và xử lý inconsistency, corruption, missingness, duplicates và semantic errors trong khi cố gắng không xóa mất signal thật.

## Cleaning bắt đầu từ Schema và Semantics

Một value chỉ có thể được gọi là invalid nếu biết meaning của field.

```text
age = 250      → invalid nếu age in years
amount = -10   → có thể invalid, hoặc refund hợp lệ
lat = 91       → invalid geographic latitude
```

Do đó data cleaning cần domain contract, không chỉ generic functions.

## Missing Values

Missing có nhiều nguyên nhân:

- field optional;
- sensor failure;
- user refused;
- feature not applicable;
- data source unavailable;
- join mismatch;
- logging bug.

Gộp tất cả thành null rồi impute mean có thể xóa meaning.

Useful pattern:

```text
value
+ missing indicator
+ missing reason when known
```

## Imputation

Common approaches:

- constant/sentinel;
- mean/median/mode;
- group-based;
- model-based;
- forward fill for time series when valid.

Imputation must fit on training data only to avoid leakage. Mean calculated using test data leaks distribution information.

## Outliers

Outlier có thể là:

- data error;
- rare but valid case;
- fraud/anomaly target itself.

Blindly clipping/removing outliers can destroy exactly the cases model needs detect.

Use domain bounds + distribution diagnostics + source inspection.

## Duplicates

Exact duplicate rows easy; entity/event duplicates harder.

Examples:

```text
same transaction retried with different event id
same document mirrored across websites
same image resized/cropped
same patient study exported twice
```

Need define duplicate semantics.

## Entity Resolution

Records may refer same entity with different IDs/names. Entity resolution can use deterministic keys, fuzzy matching or probabilistic linkage.

False merges are dangerous because they create artificial combined history.

## Type and Unit Normalization

Examples:

```text
height: cm vs m
currency: KRW vs USD
timezone: local vs UTC
date: DD/MM vs MM/DD
```

A numeric field without unit is latent bug.

Normalize unit while preserving original/raw provenance when useful.

## Categorical Normalization

`Seoul`, `SEOUL`, `서울`, `Seoul-si` may be same or different depending task. Canonicalization requires ontology/context, not lowercase alone.

## Text Cleaning

Traditional NLP often aggressively removed punctuation/stopwords. Modern LLM/NLP may need formatting, casing and punctuation.

Cleaning should preserve signals required by model.

Potential operations:

- Unicode normalization;
- control-character removal;
- boilerplate filtering;
- encoding repair;
- language detection;
- duplicate paragraph removal.

## Unicode

Visually similar characters may have different code points; normalization NFC/NFKC choices can change semantics. NFKC compatibility normalization may alter special symbols, so task-dependent.

## HTML/Web Cleaning

Extract main content, remove navigation/ads/scripts. But boilerplate classifier can accidentally remove code/table/citations.

Preserve document structure if RAG or layout understanding needs it.

## Image Cleaning

Check:

- decode errors;
- corrupted files;
- extreme aspect ratio;
- duplicates;
- blank images;
- label/image mismatch;
- orientation metadata.

Auto-rotation based EXIF can change annotation coordinates if not transformed too.

## Audio Cleaning

Check clipping, silence ratio, duration, sample rate, channel count, transcript alignment, noise. Resampling should be standardized before feature extraction.

## Time-Series Cleaning

Do not sort/forward-fill carelessly across entity boundaries. Sensor gaps may be meaningful.

Use event-time ordering and distinguish missing measurement from true zero.

## Referential Integrity

Joins can silently drop/duplicate rows. Validate cardinality:

```text
expected one-to-one
actual one-to-many
→ row explosion
```

This is common hidden data bug in feature engineering.

## Train/Test Isolation

Cleaning transformations that learn statistics must fit train only:

```text
scaler
imputer
vocabulary
PCA
feature selector
```

Then apply frozen transform to validation/test.

## Automated Data Tests

Treat dataset like code. Assertions:

```text
row count range
null percentage
unique key
category domain
numeric bounds
monotonic timestamps
join cardinality
schema version
```

Tools/frameworks can automate, but concept is data contracts + tests.

## Repair vs Drop

If error can be confidently corrected, repair with audit trail. Otherwise drop/quarantine may be safer.

Never silently fabricate unknown value just to satisfy schema.

## Quarantine Dataset

Bad/suspicious records can be moved to quarantine for review rather than permanently deleted. This supports debugging source issues.

## Cleaning Log

Track counts:

```text
raw rows
removed duplicates
invalid schema
imputed values
filtered languages
final rows
```

Large changes between versions should be explainable.

## Reproducibility

Cleaning must be deterministic/versioned where possible. Manual edits to CSV without recorded script destroy lineage.

## Over-Cleaning

Over-cleaning can make training data unrealistically pristine. Model then fails on messy production input.

Sometimes keeping realistic noise is important for robustness.

## Mental Model

> **Cleaning không nhằm làm data “đẹp”; nó nhằm làm representation faithful hơn với phenomenon và contract mà model sẽ gặp.**

## Common Misconceptions

### “Outlier nên bị xóa”

Rare valid cases may be most important.

### “Null = zero”

Missingness has different semantics.

### “Cleaning can happen before splitting”

Only stateless deterministic cleaning; learned statistics can leak test information.

## Knowledge Connection

Data cleaning connects ETL, validation, statistical missingness and leakage prevention.

Xem tiếp: [Data Labeling](./03_data_labeling.md).