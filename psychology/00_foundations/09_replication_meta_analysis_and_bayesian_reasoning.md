# Tái lập, phân tích tổng hợp và suy luận Bayes

Một nghiên cứu đơn lẻ hiếm khi đủ để xác lập một psychological claim. Khoa học tích lũy cần biết kết quả có tái xuất hiện không, effect lớn đến đâu, measurement có ổn không, literature có publication bias không và uncertainty thay đổi thế nào khi có dữ liệu mới.

> **Trạng thái bằng chứng:** replication, effect-size estimation, meta-analysis và explicit uncertainty là nền phương pháp tương đối vững. Cách chọn model, prior, heterogeneity estimator hoặc bias-correction method vẫn là vấn đề phương pháp phụ thuộc context.

Xem [[../EVIDENCE_STATUS_GUIDE]].

## 1. Tái lập là gì?

**Tái lập trực tiếp (direct replication)** cố giữ gần operationalization và procedure của study gốc để kiểm tra result có tái xuất hiện trong điều kiện tương tự hay không.

**Tái lập khái niệm (conceptual replication)** kiểm tra cùng theoretical claim bằng operationalization khác. Nó hữu ích cho generalization nhưng khó phân biệt failure của theory với failure do method mới.

Replication không phải binary pass/fail. Cần so effect estimate, uncertainty, design fidelity, sample, measurement và boundary conditions.

## 2. Replication failure có nhiều nguyên nhân

Khi replication không tái tạo original effect, các possibility gồm:

- original result là false positive;
- original effect bị phóng đại do sample nhỏ hoặc publication bias;
- replication khác context/measurement đủ để effect thay đổi;
- original hoặc replication có low reliability;
- effect thật sự heterogeneous giữa population hoặc setting;
- cả hai studies đều quá imprecise để kết luận mạnh.

Vì vậy “không replicate” không tự động nghĩa fraud hoặc theory sai hoàn toàn.

## 3. Kích thước hiệu ứng và độ chính xác

**Kích thước hiệu ứng (effect size)** trả lời “difference/association lớn bao nhiêu?”, còn confidence interval hoặc posterior distribution phản ánh uncertainty quanh estimate.

Một effect nhỏ nhưng precise có thể đáng tin hơn effect lớn nhưng interval rất rộng. Practical significance còn phụ thuộc outcome, cost, prevalence và implementation.

## 4. Giá trị p không phải evidence scale hoàn chỉnh

Giá trị p có thể useful trong một testing framework nhưng không đo effect magnitude, không cho probability hypothesis đúng và không tóm tắt toàn bộ evidence.

Dichotomizing `p < .05` thành “real” và `p ≥ .05` thành “no effect” làm mất thông tin. Khoa học tích lũy nên đọc estimate, uncertainty, design và prior evidence cùng nhau.

## 5. Statistical power và winner's curse

Study có low power thường tạo two problems. Thứ nhất, true effect dễ bị bỏ sót. Thứ hai, những result tình cờ vượt significance threshold thường là estimate lớn hơn true effect — một dạng **winner's curse**.

Điều này góp phần giải thích vì sao original small studies có thể báo effect lớn hơn later replications.

## 6. Multiple testing và researcher degrees of freedom

Nếu researcher thử nhiều outcomes, exclusions, covariates và analysis pipelines nhưng chỉ báo result thuận lợi, false-positive risk tăng.

Các giải pháp gồm preregistration, registered reports, transparent multiverse/sensitivity analysis và reporting toàn bộ analysis space có ý nghĩa.

Xem [[06_open_science_and_evidence_evaluation]].

## 7. Meta-analysis không đơn giản là “lấy trung bình paper”

**Phân tích tổng hợp (meta-analysis)** kết hợp effect estimates từ nhiều studies theo statistical model. Nó có thể ước lượng average effect và heterogeneity, nhưng quality của conclusion phụ thuộc quality của inputs.

### Fixed-effect và random-effects

Fixed-effect model giả định studies share một common true effect theo model. Random-effects model cho phép true effects khác nhau giữa studies theo distribution.

Trong psychology, population, measurement và context thường khác nhau, nên heterogeneity hiếm khi chỉ là nuisance. Nó có thể là scientific signal cho boundary condition.

## 8. Heterogeneity

Statistics như `I²` thường được dùng để mô tả proportion variation beyond sampling error, nhưng không nên đọc máy móc. I² phụ thuộc precision và study set; prediction interval có thể hữu ích hơn khi hỏi future study effect có thể nằm trong range nào.

Nếu average effect dương nhưng prediction interval rộng qua zero, conclusion thực tế khác nhiều so với “meta-analysis significant”.

## 9. Publication bias và small-study effects

Literature chỉ chứa published studies có thể overrepresent surprising/positive findings. Funnel plot, Egger-type tests, selection models và sensitivity methods cố đánh giá bias, nhưng không method nào chẩn đoán publication bias hoàn hảo từ observed studies.

Do đó bias analysis nên được xem là **sensitivity reasoning**, không phải nút bấm “sửa publication bias”.

## 10. Dependence giữa effect sizes

Một paper có thể báo nhiều outcomes, nhiều time points hoặc nhiều subgroup effects. Nếu meta-analysis coi mọi estimate là independent, standard errors có thể sai.

Multilevel meta-analysis, robust variance estimation hoặc pre-specified effect selection giúp xử lý dependence phù hợp hơn.

## 11. Meta-analysis của measurement kém vẫn có thể cho answer kém

Nếu studies dùng instruments không comparable, reliability thấp hoặc construct definition khác nhau, pooled effect có thể khó interpret dù sample tổng rất lớn.

Đây là lý do [[05_psychometrics_and_test_interpretation]] và meta-analysis phải được đọc cùng nhau.

## 12. Bayesian reasoning

**Suy luận Bayes (Bayesian inference)** cập nhật prior belief bằng data để tạo posterior:

\[
p(\theta|D) \propto p(D|\theta)p(\theta)
\]

Trong đó `p(θ)` là prior, `p(D|θ)` là likelihood và `p(θ|D)` là posterior.

Bayesian reasoning cho phép hỏi trực tiếp về probability distribution của parameter dưới model. Nhưng result không “khách quan tự động”; prior, likelihood và model assumptions phải được công khai và kiểm tra sensitivity.

## 13. Bayes factor

**Bayes factor** so relative predictive evidence của hai models/hypotheses. Nó có thể cung cấp evidence cho null so với alternative, điều mà nonsignificant p-value không tự làm được.

Tuy nhiên Bayes factor có thể rất sensitive với prior specification. “BF = 10” không nên đọc như universal truth threshold mà không xem models đã được định nghĩa thế nào.

## 14. Prior không phải “bias xấu” theo mặc định

Prior có thể weakly informative, skeptical hoặc được xây từ previous data. Điều quan trọng là prior transparent và sensitivity analysis cho thấy conclusion có phụ thuộc lựa chọn prior mạnh không.

Một prior được chọn sau khi nhìn data để tạo desired result phá vỡ logic pre-data của Bayesian model tương tự như researcher flexibility ở frequentist analysis.

## 15. Registered Reports và cải cách incentive

**Registered Report** peer-reviews question và method trước khi outcome được biết. Publication decision được tách phần lớn khỏi direction của result, giảm incentive chỉ publish positive findings.

Preregistration và Registered Reports không đảm bảo study tốt; bad design có thể preregister. Nhưng chúng làm distinction giữa confirmatory và exploratory analysis rõ hơn.

## 16. Replication và measurement reporting

Một điểm ngày càng được chú ý là replication không thể được đánh giá đầy đủ nếu measure không được mô tả rõ. Reliability, scoring, item content, validity evidence và invariance có thể thay đổi giữa labs.

Nếu same label được dùng cho instrument hoạt động khác nhau ở các samples, “effect không replicate” có thể partly là measurement non-equivalence.

## 17. Meta-analysis không tự động nâng claim thành established evidence

Một meta-analysis lớn vẫn có thể dựa vào:

- observational studies có confounding;
- poor measurement;
- highly heterogeneous definitions;
- selective reporting;
- correlated effect sizes;
- outdated samples.

Evidence status phải dựa vào **toàn bộ inference chain**, không chỉ vị trí cao của method trong một hierarchy.

## 18. Năm mức trạng thái evidence trong library

### Bằng chứng tương đối vững

Dùng khi nhiều studies/phương pháp hội tụ và boundary conditions tương đối rõ.

### Lý thuyết hiện đại

Dùng cho formal/model frameworks đang active và tạo testable predictions nhưng chưa phải final truth.

### Giả thuyết

Dùng cho explanatory proposal cụ thể còn cần direct testing hoặc replication.

### Vấn đề còn tranh luận

Dùng khi literature hoặc mechanism interpretation chưa đủ nhất quán để chọn một account làm default.

### Lý thuyết lịch sử

Dùng cho systems như classical Freud, Adler, Jung khi mô tả historical framework, không phải current scientific consensus.

## 19. Mental model

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

- Open Science Collaboration và các replication projects về reproducibility trong psychology.
- Literature về Bayesian re-analysis của replication nhấn mạnh effect-size overestimation, weak evidence và publication bias có thể quan trọng hơn binary replicated/not-replicated framing.
- Measurement-focused replication work gần đây cho thấy reporting về reliability, validity và invariance vẫn chưa đồng đều, vì vậy reproducibility cần bao gồm reproducibility của measurement.
