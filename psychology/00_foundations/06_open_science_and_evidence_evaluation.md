# Khoa học mở và cách đánh giá bằng chứng

Một kết quả nghiên cứu chỉ thật sự có giá trị khi người khác có thể hiểu nó được tạo ra như thế nào, kiểm tra giả định, đánh giá độ không chắc chắn và thử tái lập. **Khoa học mở (open science)** là tập hợp các thực hành làm quá trình đó minh bạch hơn: đăng ký trước, báo cáo đã đăng ký, chia sẻ dữ liệu/vật liệu khi phù hợp, công khai mã phân tích và khuyến khích replication.

> **Trạng thái bằng chứng tổng quát:** publication bias, researcher degrees of freedom, selective reporting và low-powered studies có thể làm literature méo là vấn đề đã được ghi nhận rộng. Preregistration, registered reports và sharing cải thiện transparency, nhưng không phải “thuốc chữa” tự động cho design kém, measurement yếu hoặc theory mơ hồ.

Xem [[../EVIDENCE_STATUS_GUIDE]], [[02_research_methods]], [[03_measurement_statistics]] và [[09_replication_meta_analysis_and_bayesian_reasoning]].

## 1. Vì sao hệ thống khoa học có thể tạo kết quả quá đẹp

Researcher thường phải đưa ra nhiều quyết định: loại outlier hay không, dùng transformation nào, thêm covariate nào, dừng thu thập ở đâu, outcome nào là primary và model nào được báo cáo.

Mỗi lựa chọn có thể hợp lý riêng lẻ. Nhưng nếu nhiều lựa chọn được thử sau khi đã nhìn outcome rồi chỉ giữ đường phân tích thuận lợi nhất, xác suất tìm ra pattern ngẫu nhiên tăng.

Vấn đề này thường được gọi chung là **researcher degrees of freedom**.

## 2. Exploratory và confirmatory research phải được phân biệt

**Nghiên cứu xác nhận (confirmatory research)** kiểm tra hypothesis và analysis plan đã định trước. **Nghiên cứu khám phá (exploratory research)** dùng data để tìm pattern hoặc hypothesis mới.

Cả hai đều có giá trị. Lỗi xảy ra khi exploration được kể lại như prediction có sẵn từ trước.

Mental model gần với machine learning:

```text
train / explore
     ≠
independent test / confirm
```

Nếu liên tục tune model trên test set, test set không còn độc lập. Tương tự, nếu hypothesis được hình thành sau khi thấy data, study đó phù hợp để generate hypothesis hơn là xác nhận mạnh hypothesis ấy.

## 3. Preregistration giúp gì — và không giúp gì

**Đăng ký trước (preregistration)** ghi hypothesis, outcome, exclusion rule và analysis plan trước khi biết kết quả.

Nó giúp phân biệt planned analysis với exploratory analysis và giảm một số flexibility hậu nghiệm.

> **Limitation:** preregistration không bảo đảm hypothesis hay, measurement valid hoặc sample representative. Một plan kém được đăng ký trước vẫn là plan kém. Preregistration cũng không cấm exploration; nó chỉ yêu cầu ghi nhãn trung thực.

## 4. Registered reports thay đổi incentive

**Báo cáo đã đăng ký (registered reports)** cho phép journal review research question và method trước khi biết result. Nếu protocol đạt yêu cầu, paper có thể được chấp nhận về nguyên tắc bất kể outcome có “positive” hay không.

Cách này giảm incentive phải đạt p-value đẹp và chuyển trọng tâm từ result sang question/design.

> **Evidence boundary:** registered reports cải thiện một số mặt transparency và publication process, nhưng literature về long-term system-wide impact vẫn tiếp tục phát triển.

## 5. Direct replication và conceptual replication

**Tái lập trực tiếp (direct replication)** cố giữ procedure gần original study để kiểm tra effect cụ thể. **Tái lập khái niệm (conceptual replication)** thay operationalization nhưng kiểm tra cùng theoretical relation.

Direct replication mạnh cho câu hỏi “result này có xuất hiện lại với procedure gần tương tự không?”. Conceptual replication mạnh hơn cho generality nhưng khó interpret hơn khi fail vì manipulation khác.

Một replication thất bại không tự động chứng minh study gốc fraud hoặc theory sai hoàn toàn. Nhưng nếu mọi failure đều được giải thích hậu nghiệm bằng “context khác”, theory mất falsifiability.

## 6. Replication cần effect size và uncertainty

Chỉ so `significant` với `not significant` là sai. Hai studies có thể có effect estimate gần nhau nhưng một study p < .05, study kia p > .05 vì sample size khác.

Cần so effect size, confidence interval, design quality và compatibility của estimates.

Xem [[09_replication_meta_analysis_and_bayesian_reasoning]].

## 7. Publication bias

Nếu positive result dễ publish hơn null result, visible literature sẽ overestimate effect stability hoặc magnitude.

**Publication bias** không chỉ là “paper null bị giấu”. Incentive có thể tác động sớm hơn: hypothesis nào được viết, outcome nào được chọn, analysis nào được report.

Meta-analysis có tool để đánh giá asymmetry, nhưng không thể reconstruct hoàn hảo studies chưa tồn tại hoặc chưa được chia sẻ.

## 8. Winner's curse

Effect đầu tiên trong literature thường đến từ small study hoặc selected positive result. Estimate ban đầu vì vậy có thể lớn hơn true effect.

Replication lớn hơn thường cho estimate nhỏ hơn mà không có nghĩa “effect biến mất hoàn toàn”.

Đây là reason không nên build intervention mạnh từ một dramatic first paper.

## 9. Reproducibility khác replicability

**Khả năng tái tạo (reproducibility)**: cùng data + code có tạo lại reported result không?

**Khả năng tái lập (replicability)**: data mới có cho pattern tương tự không?

Một study có thể reproducible nhưng not replicable. Code hoàn hảo không sửa sampling bias hoặc poor measurement.

## 10. Data/code sharing có boundary đạo đức

Open data hữu ích cho audit, reanalysis và training, nhưng không phải dataset nào cũng nên public.

Mental-health data, genomic data, precise location hoặc small-community data có re-identification risk. Transparency phải cân bằng privacy, consent và legal constraints.

Vì vậy “open science” không đồng nghĩa “upload everything”. Controlled access hoặc synthetic data có thể phù hợp hơn.

Xem [[04_ethics_and_critical_thinking]].

## 11. Measurement reproducibility

Một field có thể replicate same task nhiều lần nhưng vẫn đo sai construct.

Nếu “self-control” được operationalize bằng một task có reliability thấp, replication chỉ cho biết task behavior lặp lại hay không, chưa chắc construct interpretation đúng.

Evidence evaluation luôn cần hỏi:

```text
measurement có ổn không?
↓
design có trả lời đúng câu hỏi không?
↓
analysis có transparent không?
↓
result có replicate không?
↓
theory có predict boundary không?
```

## 12. Không có một hierarchy evidence dùng cho mọi câu hỏi

Randomized trial rất mạnh cho nhiều causal intervention questions nhưng không thích hợp cho mọi hiện tượng. Longitudinal study mạnh cho trajectory; natural experiment có thể hữu ích khi randomization bất khả thi; qualitative research có thể trả lời lived experience hoặc mechanism generation tốt hơn numerical estimate.

Evidence quality phải được đánh giá **relative to question**.

Một meta-analysis của studies yếu không tự động thành strong evidence.

## 13. Meta-analysis cần đọc heterogeneity

Mean effect có thể che variation lớn giữa studies.

**Dị biệt (heterogeneity)** hỏi effect thay đổi ra sao giữa population, measurement và implementation.

Nếu heterogeneity lớn, câu hỏi “effect trung bình là bao nhiêu?” có thể ít hữu ích hơn “trong condition nào effect lớn, nhỏ hoặc đổi hướng?”.

Nhưng moderator analysis hậu nghiệm với ít studies rất dễ false positive.

## 14. Multiverse và specification analysis

Một cách kiểm tra robustness là chạy nhiều reasonable analysis specifications thay vì chọn một model duy nhất.

**Multiverse analysis** hoặc **specification curve** cho thấy conclusion có phụ thuộc mạnh vào analytic choice hay không.

> **Boundary:** nếu tất cả specifications cùng dựa trên same biased sample hoặc invalid measure, robustness analytic không giải quyết bias nền.

## 15. Bayesian evidence không thay uncertainty bằng certainty

Bayesian methods cập nhật prior bằng likelihood để tạo posterior. Chúng có thể quantify support cho competing models hoặc parameter range.

Nhưng result vẫn phụ thuộc model, likelihood và prior choice. Prior sensitivity cần được xem xét khi conclusion nhạy.

Bayesian không phải “cách đúng, frequentist là sai”; chúng trả lời và biểu diễn uncertainty theo framework khác nhau.

## 16. Triangulation

**Tam giác hóa (triangulation)** dùng methods có failure mode khác nhau để kiểm tra cùng phenomenon.

Nếu lab experiment, longitudinal data, natural experiment và physiological measure đều converge, confidence tăng hơn khi chỉ có nhiều studies cùng một design.

Nhưng convergence chỉ mạnh khi bias không shared. Mười studies dùng cùng một self-report scale yếu không phải mười nguồn evidence độc lập hoàn toàn.

## 17. Generalization và WEIRD samples

Một effect replicate ở nhiều university labs phương Tây chưa chắc là universal human psychology.

Cần hỏi population, language, culture, age, socioeconomic context và institutional environment.

**External validity** không phải bonus sau internal validity; với claim về “human nature”, nó là core evidence requirement.

## 18. Evidence taxonomy của library

Library này dùng bốn nhãn chính:

- **Established evidence**: effect/process được support tương đối nhất quán trong phạm vi xác định.
- **Current theory**: model hiện được nghiên cứu và có support nhưng chưa phải consensus cuối cùng.
- **Debated interpretation**: data tồn tại nhưng interpretation hoặc generality còn tranh luận.
- **Historical theory**: quan trọng lịch sử nhưng không được trình bày như modern consensus.

Một chapter tốt phải nói rõ claim nằm ở tầng nào thay vì dùng cùng giọng chắc chắn cho tất cả.

## 19. Cách đọc một paper

Một workflow hữu ích:

```text
construct là gì?
↓
đo bằng gì?
↓
sample là ai?
↓
design cho phép inference nào?
↓
effect size + uncertainty?
↓
alternative explanation?
↓
preregistered hay exploratory?
↓
independent replication?
↓
generalize tới đâu?
```

Không bước nào một mình đủ tạo certainty.

## 20. Những hiểu lầm phổ biến

**“Preregistered = đúng.”** Không. Nó tăng transparency, không bảo đảm validity.

**“Replicate fail = original fraud.”** Không. Có nhiều explanation; cần cumulative evidence.

**“Meta-analysis ở trên mọi evidence.”** Không. Chất lượng phụ thuộc studies đầu vào và synthesis method.

**“Open data luôn tốt.”** Không nếu privacy risk vượt benefit.

**“p < .05 nghĩa theory đúng.”** Không. Nó không cung cấp probability trực tiếp rằng theory đúng.

**“Một paper Nature/Science là đủ.”** Journal prestige không thay cumulative evidence.

## 21. Mô hình tư duy

```text
Câu hỏi rõ
→ measurement phù hợp
→ design đúng inference
→ analysis minh bạch
→ uncertainty được báo cáo
→ replication / triangulation
→ boundary và generalization
```

Science đáng tin là một **process tích lũy**, không phải một paper đơn lẻ.

## Kết nối kiến thức

Đọc cùng [[02_research_methods]], [[03_measurement_statistics]], [[04_ethics_and_critical_thinking]], [[05_psychometrics_and_test_interpretation]], [[08_causal_inference_and_psychological_evidence]] và [[09_replication_meta_analysis_and_bayesian_reasoning]].