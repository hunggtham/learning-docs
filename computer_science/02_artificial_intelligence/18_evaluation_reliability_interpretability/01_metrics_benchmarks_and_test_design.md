# Chỉ số (metric / 지표), Benchmark và kiểm thử (test / 테스트) thiết kế (design / 설계)

> **Mạch đọc:** Đặt **chỉ số (metric / 지표), Benchmark và kiểm thử (test / 테스트) thiết kế (design / 설계)** trong bản đồ [README](./README.md) để thấy đơn vị sở hữu (owner / 오너) và vị trí của nó. Nội dung đi từ **Phân rã chỉ số (metric / 지표)** sang **chỉ số (metric / 지표) cho Classification**; điểm nối này chuẩn bị câu hỏi cho các mục sau thay vì dừng ở định nghĩa đầu tiên.


Chỉ số (metric / 지표) biến hành vi (behavior / 동작) thành số, nhưng con số chỉ có ý nghĩa khi **thiết kế phép đo (measurement design)** đúng. AI evaluation thường thất bại không phải vì thiếu chỉ số (metric / 지표) mà vì chỉ số (metric / 지표) đo sai population, benchmark bị contamination hoặc trường hợp kiểm thử (test case / 테스트 케이스) không phản ánh đặc tả hợp đồng (contract / 계약) thật.

## Phân rã chỉ số (metric / 지표)

Một evaluation tốt thường có nhiều tầng:

```text
chất lượng task
calibration / uncertainty
latency
cost
robustness
safety
chất lượng theo subgroup / slice
```

Một mô hình (model / 모델) có accuracy cao nhưng chi phí (cost / 비용) quá lớn vẫn có thể không phù hợp để deploy.

## Chỉ số (metric / 지표) cho Classification

Confusion ma trận (matrix / 행렬):

```text
TP FP
FN TN
```

Precision:

\[
\frac{TP}{TP+FP}
\]

Recall:

\[
\frac{TP}{TP+FN}
\]

F1:

\[
2\frac{Precision\cdot Recall}{Precision+Recall}
\]

Việc chọn chỉ số (metric / 지표) phụ thuộc chi phí của từng loại lỗi (error / 오류) và prevalence của lớp (class / 클래스).

## ROC-AUC và PR-AUC

ROC-AUC đo khả năng ranking qua nhiều threshold nhưng có thể trông quá tốt khi positive lớp (class / 클래스) rất hiếm.

PR-AUC tập trung vào precision và recall của positive lớp (class / 클래스), thường cung cấp nhiều thông tin hơn cho highly imbalanced tác vụ (task / 작업).

## Regression

MAE ít nhạy với outlier hơn MSE; MSE phạt large lỗi (error / 오류) mạnh hơn.

Nếu mục tiêu (target / 대상) phân phối (distribution / 분포) bị lệch, nên báo cáo thêm quantile hoặc slice thay vì chỉ average chỉ số (metric / 지표).

## Ranking

Recall@k đo xem relevant item có xuất hiện trong top-k hay không.

MRR tập trung vào rank của relevant kết quả (result / 결과) đầu tiên.

nDCG hỗ trợ graded relevance và giảm trọng số cho position thấp.

RAG retrieval cần chỉ số (metric / 지표) phù hợp với câu hỏi đang đo: candidate recall khác với final ranking chất lượng (quality / 품질).

## Chỉ số (metric / 지표) cho Generation

BLEU hoặc ROUGE hữu ích trong một số tác vụ (task / 작업) nhưng đơn vị từ (token / 토큰) overlap không đủ để đo factual tính đúng đắn (correctness / 정확성) hay ngữ nghĩa (semantic / 의미적) chất lượng (quality / 품질).

LLM tác vụ (task / 작업) thường cần kết hợp:

- chính xác (exact / 정확한) hoặc deterministic validator;
- ngữ nghĩa (semantic / 의미적) judge;
- factual hỗ trợ (support / 지원);
- human evaluation;
- task-specific thực thi (execution / 실행) kiểm thử (test / 테스트).

## Chỉ số (metric / 지표) cho Structured đầu ra (output / 출력)

JSON validity chỉ đo cú pháp. Cần tách:

```text
schema có hợp lệ không?
required field có đúng không?
value có đúng semantics không?
action có an toàn không?
```

## Chỉ số (metric / 지표) cho tác nhân (agent / 에이전트)

Tác nhân (agent / 에이전트) success không chỉ là final answer. Nên theo dõi:

- completion đã được verify;
- số step;
- công cụ (tool / 도구) lời gọi (call / 호출);
- thử lại (retry / 재시도);
- độ đúng của side tác động (effect / 효과);
- chi phí (cost / 비용) và thời gian (time / 시간);
- chính sách (policy / 정책) violation.

## Benchmark Contamination

Nếu dữ liệu huấn luyện (training data / 학습 데이터) của mô hình (model / 모델) chứa benchmark, score không còn là phép đo sạch về generalization.

Với large web-trained mô hình (model / 모델), contamination khó loại trừ hoàn toàn; benchmark nên có tác vụ (task / 작업) mới hơn, private/held-out tác vụ (task / 작업) hoặc động (dynamic / 동적) evaluation để giảm rủi ro này.

## Benchmark Saturation

Khi score gần ceiling, difference nhỏ trở nên khó diễn giải và benchmark không còn phân biệt tốt các hệ thống (system / 시스템) mạnh. Khi đó cần tác vụ (task / 작업) khó hơn hoặc coverage rộng hơn.

## Static và động (dynamic / 동적) Benchmark

Static benchmark dễ tái lập nhưng dễ bị overfit. động (dynamic / 동적), rotating hoặc private benchmark giảm gaming nhưng khó so sánh lịch sử hơn.

Có thể kết hợp cả hai.

## Taxonomy của trường hợp kiểm thử (test case / 테스트 케이스)

Một suite tốt nên gồm:

```text
happy path
edge case
long-tail case
known regression
adversarial case
invalid input
out-of-distribution case
high-impact scenario
```

## Golden Set

Golden set nên được tuyển chọn có chủ đích, phiên bản (version / 버전) hóa và có rationale cho từng trường hợp (case / 사례). Không nên để suite biến thành collection ngẫu nhiên không biết coverage.

## Hidden Holdout

Nếu nhà phát triển (developer / 개발자) xem kiểm thử (test / 테스트) đầu ra (output / 출력) mỗi ngày, bộ kiểm thử (test suite / 테스트 스위트) không còn unbiased. Một hidden set giúp phát hiện overfitting của chính quy trình phát hành (release process / 릴리스 프로세스).

## Dữ liệu (data / 데이터) Split Leakage

Thực thể (entity / 엔터티) hoặc temporal duplicate giữa train và kiểm thử (test / 테스트) làm chỉ số (metric / 지표) bị phóng đại. Split chiến lược (strategy / 전략) phải phản ánh triển khai (deployment / 배포) thật.

Temporal ứng dụng (application / 애플리케이션) thường cần future holdout.

## Mẫu (sample / 표본) Weighting

Nếu môi trường vận hành (production / 운영 환경) population khác raw kiểm thử (test / 테스트) mẫu (sample / 표본), có thể cần weighting để ước lượng expected chỉ số (metric / 지표) khi deploy.

Tuy nhiên weighting dựa trên giả định rằng mục tiêu (target / 대상) phân phối (distribution / 분포) đã được biết đủ tốt.

## Statistical Significance và Practical Significance

P-value nhỏ không bảo đảm improvement có giá trị thực tiễn. Với mẫu (sample / 표본) rất lớn, tác động (effect / 효과) cực nhỏ vẫn có thể statistically significant nhưng nghiệp vụ (business / 비즈니스) giá trị (value / 값) không đáng kể.

Nên báo cáo tác động (effect / 효과) kích thước (size / 크기), confidence interval và operational chi phí (cost / 비용) cùng nhau.

## Paired Evaluation

Khi so sánh nhiều mô hình (model / 모델) trên cùng trường hợp kiểm thử (test case / 테스트 케이스), paired bootstrap hoặc paired kiểm thử (test / 테스트) thường có statistical power tốt hơn independent comparison vì kiểm soát độ khó của từng trường hợp (case / 사례).

## Benchmark quản trị (governance / 거버넌스)

Cần theo dõi:

```text
version
owner
source / license
contamination risk
refresh cadence
retirement policy
```

Evaluation dataset cũng là một dữ liệu (data / 데이터) asset cần quản trị (governance / 거버넌스).

## Mô hình tư duy

```text
Metric là một cảm biến.
Benchmark là một thiết lập thí nghiệm.
Cả hai đều không phải bản thân reality.
```

## Những nhầm lẫn thường gặp

### “AUC cao nên threshold 0.5 chắc ổn”

Không. AUC không chọn quyết định (decision / 결정) threshold.

### “LLM judge score là khách quan tuyệt đối”

Không. Judge cũng có độ lệch (bias / 편향) và lỗi (error / 오류), cần được kiểm tra hợp lệ (validation / 검증).

### “Cùng benchmark score nghĩa là hai hệ thống (system / 시스템) tương đương”

Không. độ trễ (latency / 지연 시간), calibration, an toàn (safety / 안전), slice hiệu năng (performance / 성능) và chi phí (cost / 비용) có thể khác rất lớn.

## Liên kết kiến thức

Xem [Evaluation Foundations](./00_evaluation_foundations.md), [Uncertainty/Calibration](./02_uncertainty_and_calibration.md), [AI Testing](./05_ai_testing_and_behavioral_evaluation.md) và [Monitoring](../16_mlops_and_llmops/06_monitoring_and_observability.md).

> **Bàn giao:** Sau **Liên kết kiến thức**, hãy chốt bất biến (invariant / 불변식) và giới hạn của mục này trước khi nối sang kiến thức kế tiếp. Có thể đọc tiếp [00 evaluation foundations](./00_evaluation_foundations.md) để đối chiếu ranh giới (boundary / 경계) gần nhất.
