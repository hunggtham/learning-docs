# Dữ liệu (data / 데이터) chất lượng (quality / 품질)

> **Mạch đọc:** Đặt **dữ liệu (data / 데이터) chất lượng (quality / 품질)** trong bản đồ [README](./README.md) để thấy đơn vị sở hữu (owner / 오너) và vị trí của nó. Nội dung đi từ **tính đúng đắn (correctness / 정확성)** sang **Completeness**; điểm nối này chuẩn bị câu hỏi cho các mục sau thay vì dừng ở định nghĩa đầu tiên.


**dữ liệu (data / 데이터) chất lượng (quality / 품질)** không phải một score duy nhất. Dataset có thể sạch về format nhưng vẫn kém vì coverage thiếu, labels sai, timestamps stale hoặc phân phối (distribution / 분포) lệch triển khai (deployment / 배포).

Một khung phần mềm (framework / 프레임워크) thực dụng gồm nhiều dimensions:

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

## Tính đúng đắn (correctness / 정확성)

Giá trị (value / 값) có phản ánh phenomenon thật không? `country=KR` có thể syntactically valid nhưng wrong for người dùng (user / 사용자).

Tính đúng đắn (correctness / 정확성) thường cần tham chiếu (reference / 참조) nguồn (source / 소스) hoặc lĩnh vực (domain / 도메인) kiểm tra (audit / 감사).

## Completeness

Bao nhiêu required thông tin (information / 정보) bị missing? Nhưng 100% completeness không guarantee utility; trường dữ liệu (field / 필드) có thể filled bằng default meaningless giá trị (value / 값).

## Consistency

Cùng concept có thống nhất across sources/thời gian (time / 시간) không?

```text
currency KRW in table A
USD in table B
same field name
```

Ngữ nghĩa (semantic / 의미적) inconsistency nguy hiểm hơn lược đồ (schema / 스키마) mismatch rõ ràng.

## Uniqueness

Duplicate examples alter effective weighting. Need thực thể (entity / 엔터티)/event-specific duplicate definition.

## Freshness

Tính năng (feature / 기능)/dữ liệu (data / 데이터) có cập nhật (update / 업데이트) đủ nhanh cho use trường hợp (case / 사례)? người dùng (user / 사용자) profile từ 6 tháng trước có thể valid format nhưng stale.

Define freshness SLA per tính năng (feature / 기능)/nguồn (source / 소스).

## Coverage

Dataset có chứa cases hệ thống (system / 시스템) sẽ gặp không? Coverage phải analyze theo meaningful dimensions:

- geography;
- thiết bị (device / 장치);
- ngôn ngữ (language / 언어);
- lớp (class / 클래스);
- thời gian (time / 시간);
- sensor;
- subgroup;
- edge cases.

## Representativeness

Huấn luyện (training / 학습) phân phối (distribution / 분포) có tương đồng mục tiêu (target / 대상) triển khai (deployment / 배포) phân phối (distribution / 분포)? Oversampling có thể intentional, nhưng evaluation/calibration phải account.

## Label chất lượng (quality / 품질)

Metrics:

- disagreement;
- adjudication tỷ lệ (rate / 비율);
- known-answer accuracy;
- class-specific noise;
- label độ trễ (latency / 지연 시간)/maturity.

## Lineage chất lượng (quality / 품질)

Nếu không biết dữ liệu (data / 데이터) đến từ đâu và transform nào, gỡ lỗi (debug / 디버그) impossible dù values nhìn hợp lý.

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

## Phân phối (distribution / 분포) Tests

Compare huấn luyện (training / 학습)/tham chiếu (reference / 참조) vs hiện tại (current / 현재) dữ liệu (data / 데이터) using statistical distances:

- PSI;
- KS statistic;
- Wasserstein distance;
- Jensen-Shannon divergence;
- categorical chi-square-like checks.

No threshold universal; statistical significance can trigger on huge datasets for tiny irrelevant differences. Need nghiệp vụ (business / 비즈니스) tác động (effect / 효과) kích thước (size / 크기).

## Lược đồ (schema / 스키마) Drift vs ngữ nghĩa (semantic / 의미적) Drift

Lược đồ (schema / 스키마) drift: trường dữ liệu (field / 필드) kiểu (type / 타입)/name changes.

Ngữ nghĩa (semantic / 의미적) drift: lược đồ (schema / 스키마) same but meaning changes. Example `status=1` used to mean active, new dịch vụ (service / 서비스) phiên bản (version / 버전) means verified.

Ngữ nghĩa (semantic / 의미적) drift harder to detect automatically; versioned contracts help.

## Tính năng (feature / 기능) Drift

Đầu vào (input / 입력) phân phối (distribution / 분포) changes:

\[
P_t(X) \neq P_{ref}(X)
\]

Not every drift harms mô hình (model / 모델). Need relate drift to hiệu năng (performance / 성능)/quyết định (decision / 결정).

## Label / Concept Drift

Relationship changes:

\[
P_t(Y|X) \neq P_{ref}(Y|X)
\]

This is more directly harmful but labels often delayed, so detection harder.

## Dữ liệu (data / 데이터) Slices

Aggregate chất lượng (quality / 품질) hides issues. Define trọng yếu (critical / 중요) slices:

```text
new users
rare language
mobile camera model
nighttime
high-value transactions
```

Each slice needs minimum cỡ mẫu (sample size / 표본 크기) and chất lượng (quality / 품질) metrics.

## Chất lượng (quality / 품질) Gates

Before huấn luyện (training / 학습)/deploy dữ liệu (data / 데이터) snapshot, enforce gates:

```text
schema passes
no critical feature missing > threshold
label maturity complete
leakage audit passed
coverage minimum met
lineage recorded
```

A failed gate should khối (block / 블록) chuỗi xử lý (pipeline / 파이프라인) rather than just dashboard red.

## Golden Records

Small curated records with expected transformations help kiểm thử (test / 테스트) ETL/tính năng (feature / 기능) chuỗi xử lý (pipeline / 파이프라인) end-to-end.

## Dữ liệu (data / 데이터) chất lượng (quality / 품질) vs mô hình (model / 모델) Metrics

A mô hình (model / 모델) may temporarily perform well despite bad dữ liệu (data / 데이터) due to redundancy. Data-quality monitoring detects upstream bài toán (problem / 문제) before mô hình (model / 모델) chỉ số (metric / 지표) collapses.

## Chất lượng (quality / 품질) Debt

Teams can accumulate “dữ liệu (data / 데이터) debt”: undocumented fields, fragile joins, silently changing sources. This resembles technical debt and slows every later mô hình (model / 모델) improvement.

## Chất lượng (quality / 품질) for Unstructured dữ liệu (data / 데이터)

Văn bản (text / 텍스트) chất lượng (quality / 품질):

- encoding;
- spam;
- boilerplate;
- ngôn ngữ (language / 언어);
- truncation;
- factual/nguồn (source / 소스) độ tin cậy (reliability / 신뢰성).

Ảnh (image / 이미지)/audio chất lượng (quality / 품질):

- corruption;
- resolution;
- blur/noise;
- clipping;
- siêu dữ liệu (metadata / 메타데이터) mismatch.

## Foundation mô hình (model / 모델) dữ liệu (data / 데이터) chất lượng (quality / 품질)

Quy mô (scale / 규모) introduces mixture-level concerns:

```text
source quality distribution
deduplication
contamination
language balance
repetition
synthetic-content fraction
```

Low-quality repeated dữ liệu (data / 데이터) may receive disproportionate tối ưu hóa (optimization / 최적화) weight.

## Dữ liệu (data / 데이터) chất lượng (quality / 품질) sự cố (incident / 인시던트)

Example tính năng (feature / 기능) chuỗi xử lý (pipeline / 파이프라인) accidentally fills missing rủi ro (risk / 위험) score with `0` after upstream outage. lược đồ (schema / 스키마), null checks all pass because `0` valid. phân phối (distribution / 분포) dashboard reveals sudden spike at zero. This shows chất lượng (quality / 품질) needs statistical ngữ nghĩa (semantics / 의미론), not only types.

## Mô hình tư duy (mental model / 사고 모델)

> **dữ liệu (data / 데이터) chất lượng (quality / 품질) asks: can this dataset faithfully hỗ trợ (support / 지원) the suy luận (inference / 추론)/quyết định (decision / 결정) we intend, at the thời gian (time / 시간) and population where we will use it?**

## Dùng chung (common / 공통) Misconceptions

### “No nulls = high chất lượng (quality / 품질)”

Defaults can hide missingness.

### “dữ liệu (data / 데이터) drift = mô hình (model / 모델) thất bại (failure / 실패)”

Some drift irrelevant; need hiệu năng (performance / 성능) linkage.

### “chất lượng (quality / 품질) is preprocessing nhóm (team / 팀) responsibility”

Producer, dữ liệu (data / 데이터) engineer, ML engineer and lĩnh vực (domain / 도메인) đơn vị sở hữu (owner / 오너) share ngữ nghĩa (semantic / 의미적) responsibility.

## Liên kết kiến thức (knowledge connection / 지식 연결)

Dữ liệu (data / 데이터) chất lượng (quality / 품질) connects khả năng quan sát (observability / 관측 가능성), contracts, statistics and MLOps monitoring.

Xem tiếp: [Data Leakage](./05_data_leakage.md).

> **Bàn giao:** Sau **liên kết kiến thức (knowledge connection / 지식 연결)**, hãy chốt bất biến (invariant / 불변식) và giới hạn của mục này trước khi nối sang kiến thức kế tiếp. Có thể đọc tiếp [00 data as the foundation of ai](./00_data_as_the_foundation_of_ai.md) để đối chiếu ranh giới (boundary / 경계) gần nhất.
