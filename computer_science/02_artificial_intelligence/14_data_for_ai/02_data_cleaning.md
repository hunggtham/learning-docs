# Dữ liệu (data / 데이터) Cleaning

> **Mạch đọc:** Đặt **dữ liệu (data / 데이터) Cleaning** trong bản đồ [README](./README.md) để thấy đơn vị sở hữu (owner / 오너) và vị trí của nó. Nội dung đi từ **Cleaning bắt đầu từ lược đồ (schema / 스키마) và ngữ nghĩa (semantics / 의미론)** sang **Missing Values**; điểm nối này chuẩn bị câu hỏi cho các mục sau thay vì dừng ở định nghĩa đầu tiên.


**dữ liệu (data / 데이터) cleaning (데이터 정제 / làm sạch dữ liệu)** không phải thao tác “xóa những hàng xấu” một cách máy móc. Nó là quá trình phát hiện và xử lý inconsistency, corruption, missingness, duplicates và ngữ nghĩa (semantic / 의미적) errors trong khi cố gắng không xóa mất tín hiệu (signal / 신호) thật.

## Cleaning bắt đầu từ lược đồ (schema / 스키마) và ngữ nghĩa (semantics / 의미론)

Một giá trị (value / 값) chỉ có thể được gọi là invalid nếu biết meaning của trường dữ liệu (field / 필드).

```text
age = 250      → invalid nếu age in years
amount = -10   → có thể invalid, hoặc refund hợp lệ
lat = 91       → invalid geographic latitude
```

Do đó dữ liệu (data / 데이터) cleaning cần lĩnh vực (domain / 도메인) đặc tả hợp đồng (contract / 계약), không chỉ generic functions.

## Missing Values

Missing có nhiều nguyên nhân:

- trường dữ liệu (field / 필드) optional;
- sensor thất bại (failure / 실패);
- người dùng (user / 사용자) refused;
- tính năng (feature / 기능) not applicable;
- dữ liệu (data / 데이터) nguồn (source / 소스) unavailable;
- phép nối (join / 조인) mismatch;
- logging bug.

Gộp tất cả thành null rồi impute mean có thể xóa meaning.

Useful mẫu (pattern / 패턴):

```text
value
+ missing indicator
+ missing reason when known
```

## Imputation

Dùng chung (common / 공통) approaches:

- constant/sentinel;
- mean/median/chế độ (mode / 모드);
- group-based;
- model-based;
- forward fill for thời gian (time / 시간) series when valid.

Imputation must fit on dữ liệu huấn luyện (training data / 학습 데이터) only to avoid leakage. Mean calculated using kiểm thử (test / 테스트) dữ liệu (data / 데이터) leaks phân phối (distribution / 분포) thông tin (information / 정보).

## Outliers

Outlier có thể là:

- dữ liệu (data / 데이터) lỗi (error / 오류);
- rare but valid trường hợp (case / 사례);
- fraud/anomaly mục tiêu (target / 대상) itself.

Blindly clipping/removing outliers can destroy exactly the cases mô hình (model / 모델) needs detect.

Use lĩnh vực (domain / 도메인) bounds + phân phối (distribution / 분포) diagnostics + nguồn (source / 소스) inspection.

## Duplicates

Chính xác (exact / 정확한) duplicate rows easy; thực thể (entity / 엔터티)/sự kiện (event / 이벤트) duplicates harder.

Examples:

```text
same transaction retried with different event id
same document mirrored across websites
same image resized/cropped
same patient study exported twice
```

Need define duplicate ngữ nghĩa (semantics / 의미론).

## Thực thể (entity / 엔터티) Resolution

Records may refer same thực thể (entity / 엔터티) with different IDs/names. thực thể (entity / 엔터티) resolution can use deterministic keys, fuzzy matching or probabilistic linkage.

False merges are dangerous because they create artificial combined lịch sử (history / 이력).

## Kiểu (type / 타입) and đơn vị (unit / 단위) Normalization

Examples:

```text
height: cm vs m
currency: KRW vs USD
timezone: local vs UTC
date: DD/MM vs MM/DD
```

A numeric trường dữ liệu (field / 필드) without đơn vị (unit / 단위) is latent bug.

Normalize đơn vị (unit / 단위) while preserving original/raw provenance when useful.

## Categorical Normalization

`Seoul`, `SEOUL`, `서울`, `Seoul-si` may be same or different depending tác vụ (task / 작업). Canonicalization requires ontology/ngữ cảnh (context / 맥락), not lowercase alone.

## Văn bản (text / 텍스트) Cleaning

Traditional NLP often aggressively removed punctuation/stopwords. hiện đại (modern / 현대적) LLM/NLP may need formatting, casing and punctuation.

Cleaning should preserve signals required by mô hình (model / 모델).

Potential operations:

- Unicode normalization;
- control-character removal;
- boilerplate filtering;
- encoding repair;
- ngôn ngữ (language / 언어) detection;
- duplicate paragraph removal.

## Unicode

Visually similar characters may have different mã (code / 코드) points; normalization NFC/NFKC choices can thay đổi (change / 변경) ngữ nghĩa (semantics / 의미론). NFKC tính tương thích (compatibility / 호환성) normalization may alter special symbols, so task-dependent.

## HTML/Web Cleaning

Extract main content, remove điều hướng (navigation / 내비게이션)/ads/scripts. But boilerplate classifier can accidentally remove mã (code / 코드)/bảng (table / 테이블)/citations.

Preserve document cấu trúc (structure / 구조) if RAG or bố cục (layout / 레이아웃) understanding needs it.

## Ảnh (image / 이미지) Cleaning

Check:

- decode errors;
- corrupted files;
- extreme aspect ratio;
- duplicates;
- blank images;
- label/ảnh (image / 이미지) mismatch;
- orientation siêu dữ liệu (metadata / 메타데이터).

Auto-rotation based EXIF can thay đổi (change / 변경) annotation coordinates if not transformed too.

## Audio Cleaning

Check clipping, silence ratio, duration, mẫu (sample / 표본) tỷ lệ (rate / 비율), channel count, transcript alignment, noise. Resampling should be standardized before tính năng (feature / 기능) extraction.

## Time-Series Cleaning

Do not sort/forward-fill carelessly across thực thể (entity / 엔터티) boundaries. Sensor gaps may be meaningful.

Use event-time thứ tự (ordering / 순서) and distinguish missing đo lường (measurement / 측정) from true zero.

## Referential Integrity

Joins can silently drop/duplicate rows. Validate cardinality:

```text
expected one-to-one
actual one-to-many
→ row explosion
```

This is dùng chung (common / 공통) hidden dữ liệu (data / 데이터) bug in tính năng (feature / 기능) kỹ thuật (engineering / 엔지니어링).

## Train/kiểm thử (test / 테스트) Isolation

Cleaning transformations that learn statistics must fit train only:

```text
scaler
imputer
vocabulary
PCA
feature selector
```

Then apply frozen transform to kiểm tra hợp lệ (validation / 검증)/kiểm thử (test / 테스트).

## Automated dữ liệu (data / 데이터) Tests

Treat dataset like mã (code / 코드). Assertions:

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

Tools/frameworks can automate, but concept is dữ liệu (data / 데이터) contracts + tests.

## Repair vs Drop

If lỗi (error / 오류) can be confidently corrected, repair with kiểm tra (audit / 감사) trail. Otherwise drop/quarantine may be safer.

Never silently fabricate unknown giá trị (value / 값) just to satisfy lược đồ (schema / 스키마).

## Quarantine Dataset

Bad/suspicious records can be moved to quarantine for rà soát (review / 검토) rather than permanently deleted. This supports debugging nguồn (source / 소스) issues.

## Cleaning Log

Nhánh học (track / 트랙) counts:

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

Over-cleaning can make dữ liệu huấn luyện (training data / 학습 데이터) unrealistically pristine. mô hình (model / 모델) then fails on messy môi trường vận hành (production / 운영 환경) đầu vào (input / 입력).

Sometimes keeping realistic noise is important for robustness.

## Mô hình tư duy (mental model / 사고 모델)

> **Cleaning không nhằm làm dữ liệu (data / 데이터) “đẹp”; nó nhằm làm biểu diễn (representation / 표현) faithful hơn với phenomenon và đặc tả hợp đồng (contract / 계약) mà mô hình (model / 모델) sẽ gặp.**

## Dùng chung (common / 공통) Misconceptions

### “Outlier nên bị xóa”

Rare valid cases may be most important.

### “Null = zero”

Missingness has different ngữ nghĩa (semantics / 의미론).

### “Cleaning can happen before splitting”

Only stateless deterministic cleaning; learned statistics can leak kiểm thử (test / 테스트) thông tin (information / 정보).

## Liên kết kiến thức (knowledge connection / 지식 연결)

Dữ liệu (data / 데이터) cleaning connects ETL, kiểm tra hợp lệ (validation / 검증), statistical missingness and leakage prevention.

Xem tiếp: [Data Labeling](./03_data_labeling.md).

> **Bàn giao:** Sau **liên kết kiến thức (knowledge connection / 지식 연결)**, hãy chốt bất biến (invariant / 불변식) và giới hạn của mục này trước khi nối sang kiến thức kế tiếp. Có thể đọc tiếp [00 data as the foundation of ai](./00_data_as_the_foundation_of_ai.md) để đối chiếu ranh giới (boundary / 경계) gần nhất.
