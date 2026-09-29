# Dữ liệu (data / 데이터) as the Foundation of AI

> **Mạch đọc:** Đặt **dữ liệu (data / 데이터) as the Foundation of AI** trong bản đồ [README](./README.md) để thấy đơn vị sở hữu (owner / 오너) và vị trí của nó. Nội dung đi từ **Dataset không phải Reality** sang **dữ liệu (data / 데이터) Generating tiến trình (process / 프로세스)**; điểm nối này chuẩn bị câu hỏi cho các mục sau thay vì dừng ở định nghĩa đầu tiên.


Một AI mô hình (model / 모델) chỉ học được từ thông tin (information / 정보) mà dữ liệu (data / 데이터) chuỗi xử lý (pipeline / 파이프라인) quan sát và giữ lại. Vì vậy **dữ liệu (data / 데이터)** không phải nguyên liệu trung tính; nó là kết quả của đo lường (measurement / 측정), selection, labeling, logging và chính sách (policy / 정책).

Mô hình tư duy (mental model / 사고 모델):

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

Vòng lặp (loop / 루프) cuối quan trọng: deployed AI có thể thay đổi dữ liệu (data / 데이터) tương lai.

## Dataset không phải Reality

Dataset chỉ là mẫu (sample / 표본) từ tiến trình (process / 프로세스) tạo dữ liệu (data / 데이터). Nếu tiến trình (process / 프로세스) đó biased, mô hình (model / 모델) học độ lệch (bias / 편향) của tiến trình (process / 프로세스).

Ví dụ loan dataset chỉ có repayment outcomes cho applicants đã được approve. Ta không observe counterfactual của rejected applicants.

## Dữ liệu (data / 데이터) Generating tiến trình (process / 프로세스)

Một useful question:

> dữ liệu (data / 데이터) này xuất hiện bằng cơ chế nào?

Need understand:

- ai tạo sự kiện (event / 이벤트);
- sensor/log nào capture;
- trường hợp nào bị missing;
- chính sách (policy / 정책) nào quyết định inclusion;
- label được xác định khi nào;
- triển khai (deployment / 배포) khác collection môi trường (environment / 환경) ra sao.

## Observational dữ liệu (data / 데이터)

Most môi trường vận hành (production / 운영 환경) ML dữ liệu (data / 데이터) is observational, not randomized experiment. Correlation may reflect confounding or selection effects.

Prediction may still công việc (work / 작업) if triển khai (deployment / 배포) phân phối (distribution / 분포) similar, nhưng nhân quả (causal / 인과적) interpretation cần caution.

## Dữ liệu (data / 데이터) lược đồ (schema / 스키마)

Lược đồ (schema / 스키마) không chỉ dữ liệu (data / 데이터) types; cần ngữ nghĩa (semantic / 의미적) đặc tả hợp đồng (contract / 계약):

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

`amount=100` vô nghĩa nếu không biết currency/đơn vị (unit / 단위)/thời gian (time / 시간).

## Sự kiện (event / 이벤트) thời gian (time / 시간) vs Processing thời gian (time / 시간)

Streaming/giao dịch (transaction / 트랜잭션) các hệ thống (systems / 시스템들) distinguish:

```text
event_time      → when real-world event happened
processing_time → when pipeline received/processed it
```

ML leakage often occurs when tính năng (feature / 기능) computed using thông tin (information / 정보) available only after prediction thời gian (time / 시간).

## Point-in-Time tính đúng đắn (correctness / 정확성)

Huấn luyện (training / 학습) example at thời gian (time / 시간) `t` chỉ được use thông tin (information / 정보) that would have existed at `t` in môi trường vận hành (production / 운영 환경).

```text
prediction time = 10:00
feature uses chargeback discovered at 14:00
→ leakage
```

Tính năng (feature / 기능) store/lịch sử (history / 이력) queries need as-of ngữ nghĩa (semantics / 의미론).

## Đơn vị (unit / 단위) of Observation

Dataset row may represent:

- người dùng (user / 사용자);
- giao dịch (transaction / 트랜잭션);
- session;
- ảnh (image / 이미지);
- document;
- thời gian (time / 시간) cửa sổ (window / 윈도우).

Incorrect đơn vị (unit / 단위) can create duplicate weighting or leakage. Example splitting multiple images from same patient across train/kiểm thử (test / 테스트).

## Sampling

Huấn luyện (training / 학습) phân phối (distribution / 분포) may intentionally oversample rare positives. This helps học tập (learning / 학습) but changes lớp (class / 클래스) prior.

If triển khai (deployment / 배포) prior differs, xác suất (probability / 확률) calibration/threshold selection must account for sampling.

## Coverage

Dataset should cover intended operational không gian (space / 공간):

```text
languages
devices
regions
lighting/noise
customer segments
rare edge cases
```

No mô hình (model / 모델) can generalize reliably to regions absent from huấn luyện (training / 학습) without các giả định (assumptions / 가정들)/transfer.

## Long Tail

Real-world categories often follow heavy-tailed frequency. dùng chung (common / 공통) cases dominate dữ liệu (data / 데이터); rare but important failures have little supervision.

Long-tail chiến lược (strategy / 전략) may require targeted collection, reweighting, synthetic dữ liệu (data / 데이터) or separate rules.

## Duplicate dữ liệu (data / 데이터)

Duplicates inflate effective mẫu (sample / 표본) count and can leak across splits.

Near-duplicate detection is harder than chính xác (exact / 정확한) hashes: resized/cropped images, copied documents, paraphrases.

## Dữ liệu (data / 데이터) Versioning

Dataset is an sản phẩm tạo ra (artifact / 산출물). Need know:

```text
source snapshots
transform code version
filters
label version
split definition
hash / manifest
```

Without versioning, experiment cannot reproduce.

## Dữ liệu (data / 데이터) Lineage

Lineage tracks where each tính năng (feature / 기능)/dataset comes from:

```text
source DB table
→ ETL job
→ feature transform
→ training dataset
→ model version
```

Trọng yếu (critical / 중요) for debugging, compliance and impact phân tích (analysis / 분석).

## Phản hồi (feedback / 피드백) Loops

Recommendation mô hình (model / 모델) shows items → users interact with shown items → logs become next dữ liệu huấn luyện (training data / 학습 데이터). mô hình (model / 모델) influences what bằng chứng (evidence / 증거) it later sees.

This can amplify popularity độ lệch (bias / 편향) or hide alternatives.

## Selective Labels

We observe kết quả (outcome / 결과) only after specific quyết định (decision / 결정). Examples:

- loan default only for approved loans;
- medical kết quả (result / 결과) only for tested patients;
- fraud confirmed only for investigated transactions.

This violates simple i.i.d. các giả định (assumptions / 가정들) and may require exploration/nhân quả (causal / 인과적) methods.

## Missing dữ liệu (data / 데이터)

Missingness mechanisms matter:

- MCAR: missing unrelated to variables;
- MAR: missing depends observed dữ liệu (data / 데이터);
- MNAR: missing depends unobserved giá trị (value / 값)/tiến trình (process / 프로세스).

Imputation cannot magically recover arbitrary MNAR thông tin (information / 정보).

## Structured vs Unstructured dữ liệu (data / 데이터)

Structured dữ liệu (data / 데이터) has tường minh (explicit / 명시적) lược đồ (schema / 스키마); unstructured văn bản (text / 텍스트)/ảnh (image / 이미지)/audio still has siêu dữ liệu (metadata / 메타데이터), provenance and latent cấu trúc (structure / 구조). “Unstructured” does not mean schema-free chuỗi xử lý (pipeline / 파이프라인).

## Dữ liệu (data / 데이터) for Foundation các mô hình (models / 모델들)

At web quy mô (scale / 규모), curation includes:

- deduplication;
- ngôn ngữ (language / 언어) identification;
- chất lượng (quality / 품질) filtering;
- an toàn (safety / 안전) filtering;
- license/provenance;
- contamination removal;
- mixture weighting.

Dữ liệu (data / 데이터) mixture is effectively part of huấn luyện (training / 학습) mục tiêu (objective / 목표): more tokens from lĩnh vực (domain / 도메인) → more tối ưu hóa (optimization / 최적화) attention to that lĩnh vực (domain / 도메인).

## Benchmark Contamination

If evaluation examples appear in huấn luyện (training / 학습)/pretraining, benchmark no longer estimates generalization cleanly.

Chính xác (exact / 정확한) match insufficient because paraphrases/derived sources may contaminate.

## Dữ liệu (data / 데이터) Quantity vs chất lượng (quality / 품질)

More dữ liệu (data / 데이터) often helps, but low-quality duplicated/noisy dữ liệu (data / 데이터) can waste compute or teach harmful patterns.

Effective dữ liệu (data / 데이터) giá trị (value / 값) depends diversity, relevance, tính đúng đắn (correctness / 정확성) and coverage, not row count alone.

## Active học tập (learning / 학습)

Instead label random examples, mô hình (model / 모델) identifies uncertain/informative examples for annotation. This can improve label efficiency but bất định (uncertainty / 불확실성) heuristic may miss systematic blind spots.

## Data-Centric AI

When chuỗi xử lý (pipeline / 파이프라인)/mô hình (model / 모델) baseline stable, improving labels, coverage and definitions often gives more gain than kiến trúc (architecture / 아키텍처) tweaks.

Data-centric approach does not mean mô hình (model / 모델) unimportant; it means treat dữ liệu (data / 데이터) chất lượng (quality / 품질) as an kỹ thuật (engineering / 엔지니어링) đối tượng (object / 객체).

## Privacy

Dữ liệu huấn luyện (training data / 학습 데이터) may contain personal/sensitive thông tin (information / 정보). Collection needs purpose limitation, minimization, retention and truy cập (access / 접근) controls.

Anonymization is difficult for high-dimensional dữ liệu (data / 데이터); văn bản (text / 텍스트)/images can re-identify indirectly.

## Mô hình tư duy (mental model / 사고 모델)

> **Dataset là một instrumented view của reality, produced by a tiến trình (process / 프로세스). Muốn hiểu mô hình (model / 모델), phải hiểu tiến trình (process / 프로세스) tạo dataset.**

## Dùng chung (common / 공통) Misconceptions

### “dữ liệu (data / 데이터) speaks for itself”

Dữ liệu (data / 데이터) meaning depends đo lường (measurement / 측정), lược đồ (schema / 스키마) and selection.

### “More rows always improve mô hình (model / 모델)”

Duplicates/noise/coverage imbalance reduce marginal giá trị (value / 값).

### “Random train/kiểm thử (test / 테스트) split luôn đúng”

Thời gian (time / 시간)/group/thực thể (entity / 엔터티) dependencies often require different splitting.

## Liên kết kiến thức (knowledge connection / 지식 연결)

Dữ liệu (data / 데이터) tầng (layer / 계층) connects Statistics, Databases, phân tán (distributed / 분산) các hệ thống (systems / 시스템들), Privacy và ML evaluation.

Xem tiếp: [Data Collection](./01_data_collection.md).

> **Bàn giao:** Sau **liên kết kiến thức (knowledge connection / 지식 연결)**, hãy chốt bất biến (invariant / 불변식) và giới hạn của mục này trước khi nối sang kiến thức kế tiếp. Có thể đọc tiếp [01 data collection](./01_data_collection.md) để đối chiếu ranh giới (boundary / 경계) gần nhất.
