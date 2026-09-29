# Tái lập, phân tích tổng hợp và suy luận Bayes

> **Mạch đọc:** Đọc **Tái lập, phân tích tổng hợp và suy luận Bayes** như một mắt xích của lộ trình học (learning path / 학습 경로) hiện tại, không như một ghi chú tách rời. Nội dung đi từ **1. Tái lập là gì?** sang **2. Replication thất bại (failure / 실패) có nhiều nguyên nhân**; điểm nối này chuẩn bị câu hỏi cho các mục sau thay vì dừng ở định nghĩa đầu tiên.


Một nghiên cứu đơn lẻ hiếm khi đủ để xác lập một psychological claim. Khoa học tích lũy cần biết kết quả có tái xuất hiện không, tác động (effect / 효과) lớn đến đâu, đo lường (measurement / 측정) có ổn không, literature có publication độ lệch (bias / 편향) không và bất định (uncertainty / 불확실성) thay đổi thế nào khi có dữ liệu mới.

> **Trạng thái bằng chứng:** replication, effect-size estimation, meta-analysis và tường minh (explicit / 명시적) bất định (uncertainty / 불확실성) là nền phương pháp tương đối vững. Cách chọn mô hình (model / 모델), prior, heterogeneity estimator hoặc bias-correction phương thức (method / 메서드) vẫn là vấn đề phương pháp phụ thuộc ngữ cảnh (context / 맥락).

Xem [[../EVIDENCE_STATUS_GUIDE]].

## 1. Tái lập là gì?

**Tái lập trực tiếp (direct replication)** cố giữ gần operationalization và procedure của study gốc để kiểm tra kết quả (result / 결과) có tái xuất hiện trong điều kiện tương tự hay không.

**Tái lập khái niệm (conceptual replication)** kiểm tra cùng theoretical claim bằng operationalization khác. Nó hữu ích cho generalization nhưng khó phân biệt thất bại (failure / 실패) của lý thuyết (theory / 이론) với thất bại (failure / 실패) do phương thức (method / 메서드) mới.

Replication không phải nhị phân (binary / 이진) pass/thất bại (fail / 실패). Cần so tác động (effect / 효과) estimate, bất định (uncertainty / 불확실성), thiết kế (design / 설계) fidelity, mẫu (sample / 표본), đo lường (measurement / 측정) và ranh giới (boundary / 경계) conditions.

## 2. Replication thất bại (failure / 실패) có nhiều nguyên nhân

Khi replication không tái tạo original tác động (effect / 효과), các possibility gồm:

- original kết quả (result / 결과) là false positive;
- original tác động (effect / 효과) bị phóng đại do mẫu (sample / 표본) nhỏ hoặc publication độ lệch (bias / 편향);
- replication khác ngữ cảnh (context / 맥락)/đo lường (measurement / 측정) đủ để tác động (effect / 효과) thay đổi;
- original hoặc replication có low độ tin cậy (reliability / 신뢰성);
- tác động (effect / 효과) thật sự heterogeneous giữa population hoặc setting;
- cả hai studies đều quá imprecise để kết luận mạnh.

Vì vậy “không replicate” không tự động nghĩa fraud hoặc lý thuyết (theory / 이론) sai hoàn toàn.

## 3. Kích thước hiệu ứng và độ chính xác

**Kích thước hiệu ứng (effect size)** trả lời “difference/association lớn bao nhiêu?”, còn confidence interval hoặc posterior phân phối (distribution / 분포) phản ánh bất định (uncertainty / 불확실성) quanh estimate.

Một tác động (effect / 효과) nhỏ nhưng precise có thể đáng tin hơn tác động (effect / 효과) lớn nhưng interval rất rộng. Practical significance còn phụ thuộc kết quả (outcome / 결과), chi phí (cost / 비용), prevalence và hiện thực (implementation / 구현).

## 4. Giá trị p không phải bằng chứng (evidence / 증거) quy mô (scale / 규모) hoàn chỉnh

Giá trị p có thể useful trong một testing khung phần mềm (framework / 프레임워크) nhưng không đo tác động (effect / 효과) magnitude, không cho xác suất (probability / 확률) hypothesis đúng và không tóm tắt toàn bộ bằng chứng (evidence / 증거).

Dichotomizing `p < .05` thành “real” và `p ≥ .05` thành “no tác động (effect / 효과)” làm mất thông tin. Khoa học tích lũy nên đọc estimate, bất định (uncertainty / 불확실성), thiết kế (design / 설계) và prior bằng chứng (evidence / 증거) cùng nhau.

## 5. Statistical power và winner's curse

Study có low power thường tạo two problems. Thứ nhất, true tác động (effect / 효과) dễ bị bỏ sót. Thứ hai, những kết quả (result / 결과) tình cờ vượt significance threshold thường là estimate lớn hơn true tác động (effect / 효과) — một dạng **winner's curse**.

Điều này góp phần giải thích vì sao original small studies có thể báo tác động (effect / 효과) lớn hơn later replications.

## 6. Multiple testing và researcher degrees of freedom

Nếu researcher thử nhiều outcomes, exclusions, covariates và phân tích (analysis / 분석) pipelines nhưng chỉ báo kết quả (result / 결과) thuận lợi, false-positive rủi ro (risk / 위험) tăng.

Các giải pháp gồm preregistration, registered reports, transparent multiverse/sensitivity phân tích (analysis / 분석) và reporting toàn bộ phân tích (analysis / 분석) không gian (space / 공간) có ý nghĩa.

Xem [[06_open_science_and_evidence_evaluation]].

## 7. Meta-analysis không đơn giản là “lấy trung bình paper”

**Phân tích tổng hợp (meta-analysis)** kết hợp tác động (effect / 효과) estimates từ nhiều studies theo statistical mô hình (model / 모델). Nó có thể ước lượng average tác động (effect / 효과) và heterogeneity, nhưng chất lượng (quality / 품질) của conclusion phụ thuộc chất lượng (quality / 품질) của inputs.

### Fixed-effect và random-effects

Fixed-effect mô hình (model / 모델) giả định studies share một dùng chung (common / 공통) true tác động (effect / 효과) theo mô hình (model / 모델). Random-effects mô hình (model / 모델) cho phép true effects khác nhau giữa studies theo phân phối (distribution / 분포).

Trong psychology, population, đo lường (measurement / 측정) và ngữ cảnh (context / 맥락) thường khác nhau, nên heterogeneity hiếm khi chỉ là nuisance. Nó có thể là scientific tín hiệu (signal / 신호) cho ranh giới (boundary / 경계) điều kiện (condition / 조건).

## 8. Heterogeneity

Statistics như `I²` thường được dùng để mô tả proportion variation beyond sampling lỗi (error / 오류), nhưng không nên đọc máy móc. I² phụ thuộc precision và study set; prediction interval có thể hữu ích hơn khi hỏi future study tác động (effect / 효과) có thể nằm trong phạm vi (range / 범위) nào.

Nếu average tác động (effect / 효과) dương nhưng prediction interval rộng qua zero, conclusion thực tế khác nhiều so với “meta-analysis significant”.

## 9. Publication độ lệch (bias / 편향) và small-study effects

Literature chỉ chứa published studies có thể overrepresent surprising/positive findings. Funnel plot, Egger-type tests, selection các mô hình (models / 모델들) và sensitivity methods cố đánh giá độ lệch (bias / 편향), nhưng không phương thức (method / 메서드) nào chẩn đoán publication độ lệch (bias / 편향) hoàn hảo từ observed studies.

Do đó độ lệch (bias / 편향) phân tích (analysis / 분석) nên được xem là **sensitivity lập luận (reasoning / 추론)**, không phải nút bấm “sửa publication độ lệch (bias / 편향)”.

## 10. Dependence giữa tác động (effect / 효과) sizes

Một paper có thể báo nhiều outcomes, nhiều thời gian (time / 시간) points hoặc nhiều subgroup effects. Nếu meta-analysis coi mọi estimate là independent, tiêu chuẩn (standard / 표준) errors có thể sai.

Multilevel meta-analysis, robust variance estimation hoặc pre-specified tác động (effect / 효과) selection giúp xử lý dependence phù hợp hơn.

## 11. Meta-analysis của đo lường (measurement / 측정) kém vẫn có thể cho answer kém

Nếu studies dùng instruments không comparable, độ tin cậy (reliability / 신뢰성) thấp hoặc construct definition khác nhau, pooled tác động (effect / 효과) có thể khó interpret dù mẫu (sample / 표본) tổng rất lớn.

Đây là lý do [[05_psychometrics_and_test_interpretation]] và meta-analysis phải được đọc cùng nhau.

## 12. Bayesian lập luận (reasoning / 추론)

**Suy luận Bayes (Bayesian inference)** cập nhật prior belief bằng dữ liệu (data / 데이터) để tạo posterior:

\[
p(\theta|D) \propto p(D|\theta)p(\theta)
\]

Trong đó `p(θ)` là prior, `p(D|θ)` là likelihood và `p(θ|D)` là posterior.

Bayesian lập luận (reasoning / 추론) cho phép hỏi trực tiếp về xác suất (probability / 확률) phân phối (distribution / 분포) của parameter dưới mô hình (model / 모델). Nhưng kết quả (result / 결과) không “khách quan tự động”; prior, likelihood và mô hình (model / 모델) các giả định (assumptions / 가정들) phải được công khai và kiểm tra sensitivity.

## 13. Bayes factor

**Bayes factor** so relative predictive bằng chứng (evidence / 증거) của hai các mô hình (models / 모델들)/hypotheses. Nó có thể cung cấp bằng chứng (evidence / 증거) cho null so với alternative, điều mà nonsignificant p-value không tự làm được.

Tuy nhiên Bayes factor có thể rất sensitive với prior specification. “BF = 10” không nên đọc như universal truth threshold mà không xem các mô hình (models / 모델들) đã được định nghĩa thế nào.

## 14. Prior không phải “độ lệch (bias / 편향) xấu” theo mặc định

Prior có thể weakly informative, skeptical hoặc được xây từ previous dữ liệu (data / 데이터). Điều quan trọng là prior transparent và sensitivity phân tích (analysis / 분석) cho thấy conclusion có phụ thuộc lựa chọn prior mạnh không.

Một prior được chọn sau khi nhìn dữ liệu (data / 데이터) để tạo desired kết quả (result / 결과) phá vỡ lô-gic (logic / 논리) pre-data của Bayesian mô hình (model / 모델) tương tự như researcher flexibility ở frequentist phân tích (analysis / 분석).

## 15. Registered Reports và cải cách incentive

**Registered Report** peer-reviews question và phương thức (method / 메서드) trước khi kết quả (outcome / 결과) được biết. Publication quyết định (decision / 결정) được tách phần lớn khỏi direction của kết quả (result / 결과), giảm incentive chỉ publish positive findings.

Preregistration và Registered Reports không đảm bảo study tốt; bad thiết kế (design / 설계) có thể preregister. Nhưng chúng làm distinction giữa confirmatory và exploratory phân tích (analysis / 분석) rõ hơn.

## 16. Replication và đo lường (measurement / 측정) reporting

Một điểm ngày càng được chú ý là replication không thể được đánh giá đầy đủ nếu measure không được mô tả rõ. độ tin cậy (reliability / 신뢰성), scoring, item content, validity bằng chứng (evidence / 증거) và invariance có thể thay đổi giữa labs.

Nếu same label được dùng cho instrument hoạt động khác nhau ở các samples, “tác động (effect / 효과) không replicate” có thể partly là đo lường (measurement / 측정) non-equivalence.

## 17. Meta-analysis không tự động nâng claim thành established bằng chứng (evidence / 증거)

Một meta-analysis lớn vẫn có thể dựa vào:

- observational studies có confounding;
- poor đo lường (measurement / 측정);
- highly heterogeneous definitions;
- selective reporting;
- correlated tác động (effect / 효과) sizes;
- outdated samples.

Bằng chứng (evidence / 증거) status phải dựa vào **toàn bộ suy luận (inference / 추론) chuỗi (chain / 사슬)**, không chỉ vị trí cao của phương thức (method / 메서드) trong một hierarchy.

## 18. Năm mức trạng thái bằng chứng (evidence / 증거) trong thư viện (library / 라이브러리)

### Bằng chứng tương đối vững

Dùng khi nhiều studies/phương pháp hội tụ và ranh giới (boundary / 경계) conditions tương đối rõ.

### Lý thuyết hiện đại

Dùng cho formal/mô hình (model / 모델) frameworks đang active và tạo testable predictions nhưng chưa phải final truth.

### Giả thuyết

Dùng cho explanatory proposal cụ thể còn cần direct testing hoặc replication.

### Vấn đề còn tranh luận

Dùng khi literature hoặc cơ chế (mechanism / 메커니즘) interpretation chưa đủ nhất quán để chọn một account làm default.

### Lý thuyết lịch sử

Dùng cho các hệ thống (systems / 시스템들) như classical Freud, Adler, Jung khi mô tả historical khung phần mềm (framework / 프레임워크), không phải hiện tại (current / 현재) scientific consensus.

## 19. mô hình tư duy (mental model / 사고 모델)

Phần này chốt mental model thành một chuỗi có thể dùng lại: bối cảnh → cơ chế → bằng chứng → giới hạn → ứng dụng. Hãy đọc sơ đồ như công cụ suy luận, không như một nhãn kết luận tự động.

```text
Study riêng lẻ
   ↓ replication
Effect estimates
   ↓ synthesis
Meta-analysis
   ↓ bias / heterogeneity / measurement checks
Cumulative evidence
   ↓ theory comparison
Update confidence, không phải binary proof
```

## Kết nối kiến thức

Đọc cùng [[03_measurement_statistics]], [[05_psychometrics_and_test_interpretation]], [[06_open_science_and_evidence_evaluation]], [[08_causal_inference_and_psychological_evidence]] và [[02_research_methods]].

### Nguồn định hướng

Các mục dưới đây là điểm kiểm tra bằng chứng và hướng đọc tiếp. Hãy ghi rõ claim nào được nguồn hỗ trợ, mức chắc chắn ra sao và phần nào còn cần cập nhật.

- Open Science Collaboration và các replication projects về reproducibility trong psychology.
- Literature về Bayesian re-analysis của replication nhấn mạnh effect-size overestimation, weak bằng chứng (evidence / 증거) và publication độ lệch (bias / 편향) có thể quan trọng hơn nhị phân (binary / 이진) replicated/not-replicated framing.
- Measurement-focused replication công việc (work / 작업) gần đây cho thấy reporting về độ tin cậy (reliability / 신뢰성), validity và invariance vẫn chưa đồng đều, vì vậy reproducibility cần bao gồm reproducibility của đo lường (measurement / 측정).

> **Bàn giao:** Sau **Nguồn định hướng**, hãy chốt bất biến (invariant / 불변식) và giới hạn của mục này trước khi nối sang kiến thức kế tiếp. Có thể đọc tiếp [00 psychology as science](./00_psychology_as_science.md) để đối chiếu ranh giới (boundary / 경계) gần nhất.
