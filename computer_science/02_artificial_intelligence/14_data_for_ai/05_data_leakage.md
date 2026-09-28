# Dữ liệu (data / 데이터) Leakage

> **Mạch đọc:** Đặt **dữ liệu (data / 데이터) Leakage** trong bản đồ [README](./README.md) để thấy đơn vị sở hữu (owner / 오너) và vị trí của nó. Nội dung đi từ **mục tiêu (target / 대상) Leakage** sang **Temporal Leakage**; điểm nối này chuẩn bị câu hỏi cho các mục sau thay vì dừng ở định nghĩa đầu tiên.


**dữ liệu (data / 데이터) leakage (데이터 누수 / rò rỉ dữ liệu)** xảy ra khi huấn luyện (training / 학습)/evaluation chuỗi xử lý (pipeline / 파이프라인) cho mô hình (model / 모델) truy cập (access / 접근) thông tin (information / 정보) mà môi trường vận hành (production / 운영 환경) suy luận (inference / 추론) sẽ không thực sự có, hoặc khi thông tin (information / 정보) từ kiểm tra hợp lệ (validation / 검증)/kiểm thử (test / 테스트) ảnh hưởng huấn luyện (training / 학습). Leakage tạo metrics đẹp giả tạo và thường là một trong những thất bại (failure / 실패) nghiêm trọng nhất của ML hệ thống (system / 시스템).

## Mục tiêu (target / 대상) Leakage

Tính năng (feature / 기능) chứa trực tiếp hoặc gián tiếp thông tin (information / 정보) về mục tiêu (target / 대상) sau thời điểm prediction.

Ví dụ dự đoán fraud tại giao dịch (transaction / 트랜잭션) thời gian (time / 시간) nhưng tính năng (feature / 기능) chứa:

```text
chargeback_status
manual_investigation_result
post-transaction dispute count
```

Mô hình (model / 모델) không “thông minh”; nó nhìn tương lai.

## Temporal Leakage

Tính năng (feature / 기능) aggregate vô tình include future events.

Ví dụ muốn predict churn ngày 1/9 nhưng tính “number of hỗ trợ (support / 지원) tickets in September” bằng full-month bảng (table / 테이블).

Correct tính năng (feature / 기능) cần as-of truy vấn (query / 쿼리):

```text
only events with event_time <= prediction_time
```

## Train/kiểm thử (test / 테스트) Contamination

Same or near-duplicate thực thể (entity / 엔터티) appears both sides:

- frames từ same video;
- records của same patient;
- copied web documents;
- repeated customer transactions;
- augmented versions of same ảnh (image / 이미지).

Random row split không đủ khi observations correlated by group.

## Preprocessing Leakage

Fit scaler/PCA/imputer/vocabulary on full dataset trước split:

\[
\mu = mean(train+test)
\]

Kiểm thử (test / 테스트) phân phối (distribution / 분포) ảnh hưởng transform huấn luyện (training / 학습). Correct mẫu (pattern / 패턴):

```text
fit transform on train
apply frozen transform to val/test
```

## Tính năng (feature / 기능) Selection Leakage

Nếu chọn features dựa trên correlation với mục tiêu (target / 대상) computed over entire dữ liệu (data / 데이터) including kiểm thử (test / 테스트), kiểm thử (test / 테스트) đã influence mô hình (model / 모델) thiết kế (design / 설계).

Selection/hyperparameter tuning phải nằm trong huấn luyện (training / 학습)/kiểm tra hợp lệ (validation / 검증) tiến trình (process / 프로세스).

## Cross-Validation Leakage

Preprocessing outside CV folds leaks fold thông tin (information / 정보). chuỗi xử lý (pipeline / 파이프라인) phải refit transforms inside each huấn luyện (training / 학습) fold.

## Label Leakage Through Human tiến trình (process / 프로세스)

Human-created fields may encode kết quả (outcome / 결과) indirectly. Example analyst writes ghi chú (note / 노트) after resolving trường hợp (case / 사례); văn bản (text / 텍스트) contains “confirmed fraud”. If mô hình (model / 모델) is supposed to triage before analyst resolution, ghi chú (note / 노트) is illegal tính năng (feature / 기능).

## Proxy Leakage

Tính năng (feature / 기능) itself technically available but only because hiện tại (current / 현재) môi trường vận hành (production / 운영 환경) tiến trình (process / 프로세스) already uses mục tiêu (target / 대상) kết quả (outcome / 결과).

Example `queue=fraud_team` indicates upstream quy tắc (rule / 규칙) already decided trường hợp (case / 사례) suspicious. mô hình (model / 모델) appears strong but adds no independent predictive power and may thất bại (fail / 실패) if routing lô-gic (logic / 논리) changes.

## Identifier Leakage

IDs can encode thời gian (time / 시간)/nguồn (source / 소스)/category unintentionally. mô hình (model / 모델) memorizes thực thể (entity / 엔터티) or batch rather than general tín hiệu (signal / 신호).

High-cardinality IDs should be scrutinized even if not obvious mục tiêu (target / 대상).

## Duplicate Leakage in Foundation các mô hình (models / 모델들)

Evaluation benchmark văn bản (text / 텍스트) may exist verbatim or paraphrased in pretraining corpus. mô hình (model / 모델) score then mixes generalization and memorization.

Contamination detection uses chính xác (exact / 정확한) hashes, n-gram similarity, ngữ nghĩa (semantic / 의미적) matching and nguồn (source / 소스) provenance, but perfect detection is difficult.

## RAG Evaluation Leakage

If evaluator answer is included in indexed corpus in an artificial way not representative môi trường vận hành (production / 운영 환경), RAG may retrieve gold answer directly. Need construct realistic retrieval corpus.

## Time-Based Split

For future prediction các hệ thống (systems / 시스템들), train past → validate/kiểm thử (test / 테스트) future often best approximates triển khai (deployment / 배포):

```text
train: Jan-Jun
val: Jul
 test: Aug
```

But seasonality/regime shift can make one thời gian (time / 시간) split noisy; rolling backtests help.

## Group Split

Group all observations of thực thể (entity / 엔터티) into same split:

```text
patient_id
user_id
company_id
device_id
video_id
```

prevents memorization across correlated records.

## Spatial Leakage

Geospatial dữ liệu (data / 데이터) nearby locations correlated. Random points split can overestimate generalization to new regions. Spatial khối (block / 블록) split may be needed.

## Leakage kiểm tra (audit / 감사) Questions

For each tính năng (feature / 기능):

1. tính năng (feature / 기능) được generated khi nào?
2. nguồn (source / 소스) sự kiện (event / 이벤트) xảy ra trước prediction thời gian (time / 시간) không?
3. môi trường vận hành (production / 운영 환경) đường dẫn (path / 경로) có compute được cùng lô-gic (logic / 논리) không?
4. mục tiêu (target / 대상) hoặc downstream quyết định (decision / 결정) có ảnh hưởng tính năng (feature / 기능) không?
5. same thực thể (entity / 엔터티)/dữ liệu (data / 데이터) derivative có xuất hiện kiểm thử (test / 테스트) không?

## Tính năng (feature / 기능) Store Point-in-Time phép nối (join / 조인)

Correct historical huấn luyện (training / 학습) phép nối (join / 조인) selects latest tính năng (feature / 기능) giá trị (value / 값) available before sự kiện (event / 이벤트) thời gian (time / 시간), not hiện tại (current / 현재) latest bản ghi (record / 레코드).

This is cốt lõi (core / 핵심) hàm (function / 함수) of temporal tính năng (feature / 기능) stores.

## Hidden Leakage Through Aggregates

A monthly aggregate may have timestamp first day of month nhưng calculated after month end. Timestamp trường dữ liệu (field / 필드) alone cannot prove availability; lineage must bản ghi (record / 레코드) **availability thời gian (time / 시간)**.

## Hyperparameter Overfitting

Repeatedly inspect kiểm thử (test / 테스트) score and adjust mô hình (model / 모델) turns kiểm thử (test / 테스트) set into informal kiểm tra hợp lệ (validation / 검증) set. Final chỉ số (metric / 지표) optimistic.

Need hidden final holdout or nested evaluation discipline.

## Early Stopping

Using kiểm tra hợp lệ (validation / 검증) for early stopping is legitimate because kiểm tra hợp lệ (validation / 검증) is part of mô hình (model / 모델) selection. But final kiểm thử (test / 테스트) must remain untouched until selection complete.

## Leakage Detection Signals

Suspicious signs:

- unrealistically high chỉ số (metric / 지표);
- one tính năng (feature / 기능) dominates importance;
- kiểm thử (test / 테스트) hiệu năng (performance / 성능) collapses in future split;
- mô hình (model / 모델) works offline but not online;
- tính năng (feature / 기능) correlation appears after kết quả (outcome / 결과) timestamp.

High hiệu năng (performance / 성능) is not proof of leakage, but deserves kiểm tra (audit / 감사).

## Example: Credit rủi ro (risk / 위험)

Tính năng (feature / 기능) `days_past_due_current` may be valid for predicting future 12-month default at hiện tại (current / 현재) date, but invalid if goal is predict default at loan origination. Same trường dữ liệu (field / 필드) legality depends prediction timestamp.

Thus leakage is task-definition relative.

## Mô hình tư duy (mental model / 사고 모델)

> **Leakage means mô hình (model / 모델) receives thông tin (information / 정보) from outside the thông tin (information / 정보) ranh giới (boundary / 경계) that will exist at the moment of real quyết định (decision / 결정).**

Think like thời gian (time / 시간) traveler/auditor, not like dataframe programmer.

## Dùng chung (common / 공통) Misconceptions

### “Leakage chỉ là mục tiêu (target / 대상) column accidentally included”

Temporal aggregates, duplicates, human workflow and preprocessing are more subtle dùng chung (common / 공통) forms.

### “Random split prevents leakage”

Not for thời gian (time / 시간)/group/spatial correlated dữ liệu (data / 데이터).

### “If tính năng (feature / 기능) exists in cơ sở dữ liệu (database / 데이터베이스), it is fair to use”

It may not exist yet at prediction thời gian (time / 시간).

## Liên kết kiến thức (knowledge connection / 지식 연결)

Leakage connects temporal databases, nhân quả (causal / 인과적) tiến trình (process / 프로세스) understanding and evaluation thiết kế (design / 설계).

Xem tiếp: [Dataset Bias](./06_dataset_bias.md).

> **Bàn giao:** Sau **liên kết kiến thức (knowledge connection / 지식 연결)**, hãy chốt bất biến (invariant / 불변식) và giới hạn của mục này trước khi nối sang kiến thức kế tiếp. Có thể đọc tiếp [00 data as the foundation of ai](./00_data_as_the_foundation_of_ai.md) để đối chiếu ranh giới (boundary / 경계) gần nhất.
