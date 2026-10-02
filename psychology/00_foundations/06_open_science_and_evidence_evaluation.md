# Khoa học mở và cách đánh giá bằng chứng

> **Mạch đọc:** [README](../README.md) là bản đồ owner của **Khoa học mở và cách đánh giá bằng chứng**; nhìn vào vị trí đó trước để biết file này đang phục vụ nhánh kiến thức nào. **1. Vì sao hệ thống khoa học có thể tạo kết quả quá đẹp** mở đối tượng chính của file và câu hỏi cần theo dõi; sau đó sang **2. Exploratory và confirmatory research phải được phân biệt** để mở rộng đối tượng sang phạm vi kế cận. Mạch này nối open science với evidence evaluation, để preregistration, transparency và uncertainty làm rõ mức tin cậy của kết luận.

Một kết quả nghiên cứu chỉ thật sự có giá trị khi người khác có thể hiểu nó được tạo ra như thế nào, kiểm tra giả định, đánh giá độ không chắc chắn và thử tái lập. **Khoa học mở (open science)** là tập hợp các thực hành làm quá trình đó minh bạch hơn: đăng ký trước, báo cáo đã đăng ký, chia sẻ dữ liệu/vật liệu khi phù hợp, công khai mã phân tích và khuyến khích replication.

> **Trạng thái bằng chứng tổng quát:** publication độ lệch (bias / 편향), researcher degrees of freedom, selective reporting và low-powered studies có thể làm literature méo là vấn đề đã được ghi nhận rộng. Preregistration, registered reports và sharing cải thiện transparency, nhưng không phải “thuốc chữa” tự động cho thiết kế (design / 설계) kém, đo lường (measurement / 측정) yếu hoặc lý thuyết (theory / 이론) mơ hồ.

Xem [[../EVIDENCE_STATUS_GUIDE]], [[02_research_methods]], [[03_measurement_statistics]] và [[09_replication_meta_analysis_and_bayesian_reasoning]].

## 1. Vì sao hệ thống khoa học có thể tạo kết quả quá đẹp

Researcher thường phải đưa ra nhiều quyết định: loại outlier hay không, dùng transformation nào, thêm covariate nào, dừng thu thập ở đâu, kết quả (outcome / 결과) nào là primary và mô hình (model / 모델) nào được báo cáo.

Mỗi lựa chọn có thể hợp lý riêng lẻ. Nhưng nếu nhiều lựa chọn được thử sau khi đã nhìn kết quả (outcome / 결과) rồi chỉ giữ đường phân tích thuận lợi nhất, xác suất tìm ra mẫu (pattern / 패턴) ngẫu nhiên tăng.

Vấn đề này thường được gọi chung là **researcher degrees of freedom**.

> **Chuyển mạch:** Trong **Khoa học mở và cách đánh giá bằng chứng**, **2. Exploratory và confirmatory research phải được phân biệt** tiếp nhận điểm tựa từ **1. Vì sao hệ thống khoa học có thể tạo kết quả quá đẹp** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **3. Preregistration giúp gì — và không giúp gì** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 2. Exploratory và confirmatory research phải được phân biệt

**Nghiên cứu xác nhận (confirmatory research)** kiểm tra hypothesis và phân tích (analysis / 분석) plan đã định trước. **Nghiên cứu khám phá (exploratory research)** dùng dữ liệu (data / 데이터) để tìm mẫu (pattern / 패턴) hoặc hypothesis mới.

Cả hai đều có giá trị. Lỗi xảy ra khi exploration được kể lại như prediction có sẵn từ trước.

Mô hình tư duy (mental model / 사고 모델) gần với machine học tập (learning / 학습):

```text
train / explore
     ≠
independent test / confirm
```

Nếu liên tục tune mô hình (model / 모델) trên kiểm thử (test / 테스트) set, kiểm thử (test / 테스트) set không còn độc lập. Tương tự, nếu hypothesis được hình thành sau khi thấy dữ liệu (data / 데이터), study đó phù hợp để generate hypothesis hơn là xác nhận mạnh hypothesis ấy.

> **Chuyển mạch:** Ở chặng này của **Khoa học mở và cách đánh giá bằng chứng**, **3. Preregistration giúp gì — và không giúp gì** tiếp nhận điểm tựa từ **2. Exploratory và confirmatory research phải được phân biệt** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **4. Registered reports thay đổi incentive** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 3. Preregistration giúp gì — và không giúp gì

**Đăng ký trước (preregistration)** ghi hypothesis, kết quả (outcome / 결과), exclusion quy tắc (rule / 규칙) và phân tích (analysis / 분석) plan trước khi biết kết quả.

Nó giúp phân biệt planned phân tích (analysis / 분석) với exploratory phân tích (analysis / 분석) và giảm một số flexibility hậu nghiệm.

> **Limitation:** preregistration không bảo đảm hypothesis hay, đo lường (measurement / 측정) valid hoặc mẫu (sample / 표본) representative. Một plan kém được đăng ký trước vẫn là plan kém. Preregistration cũng không cấm exploration; nó chỉ yêu cầu ghi nhãn trung thực.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Khoa học mở và cách đánh giá bằng chứng**, **4. Registered reports thay đổi incentive** tiếp nhận điểm tựa từ **3. Preregistration giúp gì — và không giúp gì** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **5. Direct replication và conceptual replication** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 4. Registered reports thay đổi incentive

**Báo cáo đã đăng ký (registered reports)** cho phép journal rà soát (review / 검토) research question và phương thức (method / 메서드) trước khi biết kết quả (result / 결과). Nếu giao thức (protocol / 프로토콜) đạt yêu cầu, paper có thể được chấp nhận về nguyên tắc bất kể kết quả (outcome / 결과) có “positive” hay không.

Cách này giảm incentive phải đạt p-value đẹp và chuyển trọng tâm từ kết quả (result / 결과) sang question/thiết kế (design / 설계).

> **bằng chứng (evidence / 증거) ranh giới (boundary / 경계):** registered reports cải thiện một số mặt transparency và publication tiến trình (process / 프로세스), nhưng literature về long-term system-wide impact vẫn tiếp tục phát triển.

> **Chuyển mạch:** Trong **Khoa học mở và cách đánh giá bằng chứng**, **5. Direct replication và conceptual replication** tiếp nhận điểm tựa từ **4. Registered reports thay đổi incentive** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **6. Replication cần tác động (effect / 효과) kích thước (size / 크기) và bất định (uncertainty / 불확실성)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 5. Direct replication và conceptual replication

**Tái lập trực tiếp (direct replication)** cố giữ procedure gần original study để kiểm tra tác động (effect / 효과) cụ thể. **Tái lập khái niệm (conceptual replication)** thay operationalization nhưng kiểm tra cùng theoretical quan hệ (relation / 관계).

Direct replication mạnh cho câu hỏi “kết quả (result / 결과) này có xuất hiện lại với procedure gần tương tự không?”. Conceptual replication mạnh hơn cho generality nhưng khó interpret hơn khi thất bại (fail / 실패) vì manipulation khác.

Một replication thất bại không tự động chứng minh study gốc fraud hoặc lý thuyết (theory / 이론) sai hoàn toàn. Nhưng nếu mọi thất bại (failure / 실패) đều được giải thích hậu nghiệm bằng “ngữ cảnh (context / 맥락) khác”, lý thuyết (theory / 이론) mất falsifiability.

> **Chuyển mạch:** Ở chặng này của **Khoa học mở và cách đánh giá bằng chứng**, **6. Replication cần tác động (effect / 효과) kích thước (size / 크기) và bất định (uncertainty / 불확실성)** tiếp nhận điểm tựa từ **5. Direct replication và conceptual replication** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **7. Publication độ lệch (bias / 편향)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 6. Replication cần tác động (effect / 효과) kích thước (size / 크기) và bất định (uncertainty / 불확실성)

Chỉ so `significant` với `not significant` là sai. Hai studies có thể có tác động (effect / 효과) estimate gần nhau nhưng một study p < .05, study kia p > .05 vì cỡ mẫu (sample size / 표본 크기) khác.

Cần so tác động (effect / 효과) kích thước (size / 크기), confidence interval, thiết kế (design / 설계) chất lượng (quality / 품질) và tính tương thích (compatibility / 호환성) của estimates.

Xem [[09_replication_meta_analysis_and_bayesian_reasoning]].

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Khoa học mở và cách đánh giá bằng chứng**, **7. Publication độ lệch (bias / 편향)** tiếp nhận điểm tựa từ **6. Replication cần tác động (effect / 효과) kích thước (size / 크기) và bất định (uncertainty / 불확실성)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **8. Winner's curse** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 7. Publication độ lệch (bias / 편향)

Nếu positive kết quả (result / 결과) dễ publish hơn null kết quả (result / 결과), visible literature sẽ overestimate tác động (effect / 효과) stability hoặc magnitude.

**Publication độ lệch (bias / 편향)** không chỉ là “paper null bị giấu”. Incentive có thể tác động sớm hơn: hypothesis nào được viết, kết quả (outcome / 결과) nào được chọn, phân tích (analysis / 분석) nào được report.

Meta-analysis có công cụ (tool / 도구) để đánh giá asymmetry, nhưng không thể reconstruct hoàn hảo studies chưa tồn tại hoặc chưa được chia sẻ.

> **Chuyển mạch:** Trong **Khoa học mở và cách đánh giá bằng chứng**, **8. Winner's curse** tiếp nhận điểm tựa từ **7. Publication độ lệch (bias / 편향)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **9. Reproducibility khác replicability** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 8. Winner's curse

Tác động (effect / 효과) đầu tiên trong literature thường đến từ small study hoặc selected positive kết quả (result / 결과). Estimate ban đầu vì vậy có thể lớn hơn true tác động (effect / 효과).

Replication lớn hơn thường cho estimate nhỏ hơn mà không có nghĩa “tác động (effect / 효과) biến mất hoàn toàn”.

Đây là reason không nên bản dựng (build / 빌드) intervention mạnh từ một dramatic first paper.

> **Chuyển mạch:** Ở chặng này của **Khoa học mở và cách đánh giá bằng chứng**, **9. Reproducibility khác replicability** tiếp nhận điểm tựa từ **8. Winner's curse** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **10. dữ liệu (data / 데이터)/mã (code / 코드) sharing có ranh giới (boundary / 경계) đạo đức** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 9. Reproducibility khác replicability

**Khả năng tái tạo (reproducibility)**: cùng dữ liệu (data / 데이터) + mã (code / 코드) có tạo lại reported kết quả (result / 결과) không?

**Khả năng tái lập (replicability)**: dữ liệu (data / 데이터) mới có cho mẫu (pattern / 패턴) tương tự không?

Một study có thể reproducible nhưng not replicable. mã (code / 코드) hoàn hảo không sửa sampling độ lệch (bias / 편향) hoặc poor đo lường (measurement / 측정).

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Khoa học mở và cách đánh giá bằng chứng**, **9. Reproducibility khác replicability** đã nêu tiêu chí phân biệt, còn **10. dữ liệu (data / 데이터)/mã (code / 코드) sharing có ranh giới (boundary / 경계) đạo đức** dùng tiêu chí đó để soi ranh giới và điểm dễ nhầm. Từ đây, **11. đo lường (measurement / 측정) reproducibility** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 10. dữ liệu (data / 데이터)/mã (code / 코드) sharing có ranh giới (boundary / 경계) đạo đức

Open dữ liệu (data / 데이터) hữu ích cho kiểm tra (audit / 감사), reanalysis và huấn luyện (training / 학습), nhưng không phải dataset nào cũng nên công khai (public / 공개).

Mental-health dữ liệu (data / 데이터), genomic dữ liệu (data / 데이터), precise location hoặc small-community dữ liệu (data / 데이터) có re-identification rủi ro (risk / 위험). Transparency phải cân bằng privacy, consent và legal các ràng buộc (constraints / 제약조건들).

Vì vậy “open science” không đồng nghĩa “upload everything”. Controlled truy cập (access / 접근) hoặc synthetic dữ liệu (data / 데이터) có thể phù hợp hơn.

Xem [[04_ethics_and_critical_thinking]].

> **Chuyển mạch:** Trong **Khoa học mở và cách đánh giá bằng chứng**, **10. dữ liệu (data / 데이터)/mã (code / 코드) sharing có ranh giới (boundary / 경계) đạo đức** đã nêu tiêu chí phân biệt, còn **11. đo lường (measurement / 측정) reproducibility** dùng tiêu chí đó để soi ranh giới và điểm dễ nhầm. Từ đây, **12. Không có một hierarchy bằng chứng (evidence / 증거) dùng cho mọi câu hỏi** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 11. đo lường (measurement / 측정) reproducibility

Một trường dữ liệu (field / 필드) có thể replicate same tác vụ (task / 작업) nhiều lần nhưng vẫn đo sai construct.

Nếu “self-control” được operationalize bằng một tác vụ (task / 작업) có độ tin cậy (reliability / 신뢰성) thấp, replication chỉ cho biết tác vụ (task / 작업) hành vi (behavior / 동작) lặp lại hay không, chưa chắc construct interpretation đúng.

Bằng chứng (evidence / 증거) evaluation luôn cần hỏi:

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

> **Chuyển mạch:** Ở chặng này của **Khoa học mở và cách đánh giá bằng chứng**, **11. đo lường (measurement / 측정) reproducibility** nêu điều cần giải thích; **12. Không có một hierarchy bằng chứng (evidence / 증거) dùng cho mọi câu hỏi** đối chiếu nó với bằng chứng hoặc nguồn kiểm chứng. Từ đây, **13. Meta-analysis cần đọc heterogeneity** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 12. Không có một hierarchy bằng chứng (evidence / 증거) dùng cho mọi câu hỏi

Randomized trial rất mạnh cho nhiều nhân quả (causal / 인과적) intervention questions nhưng không thích hợp cho mọi hiện tượng. Longitudinal study mạnh cho trajectory; natural experiment có thể hữu ích khi randomization bất khả thi; qualitative research có thể trả lời lived experience hoặc cơ chế (mechanism / 메커니즘) generation tốt hơn numerical estimate.

Bằng chứng (evidence / 증거) chất lượng (quality / 품질) phải được đánh giá **relative to question**.

Một meta-analysis của studies yếu không tự động thành strong bằng chứng (evidence / 증거).

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Khoa học mở và cách đánh giá bằng chứng**, **12. Không có một hierarchy bằng chứng (evidence / 증거) dùng cho mọi câu hỏi** nêu điều cần giải thích; **13. Meta-analysis cần đọc heterogeneity** đối chiếu nó với bằng chứng hoặc nguồn kiểm chứng. Từ đây, **14. Multiverse và specification phân tích (analysis / 분석)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 13. Meta-analysis cần đọc heterogeneity

Mean tác động (effect / 효과) có thể che variation lớn giữa studies.

**Dị biệt (heterogeneity)** hỏi tác động (effect / 효과) thay đổi ra sao giữa population, đo lường (measurement / 측정) và hiện thực (implementation / 구현).

Nếu heterogeneity lớn, câu hỏi “tác động (effect / 효과) trung bình là bao nhiêu?” có thể ít hữu ích hơn “trong điều kiện (condition / 조건) nào tác động (effect / 효과) lớn, nhỏ hoặc đổi hướng?”.

Nhưng moderator phân tích (analysis / 분석) hậu nghiệm với ít studies rất dễ false positive.

> **Chuyển mạch:** Trong **Khoa học mở và cách đánh giá bằng chứng**, **14. Multiverse và specification phân tích (analysis / 분석)** tiếp nhận điểm tựa từ **13. Meta-analysis cần đọc heterogeneity** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **15. Bayesian bằng chứng (evidence / 증거) không thay bất định (uncertainty / 불확실성) bằng certainty** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 14. Multiverse và specification phân tích (analysis / 분석)

Một cách kiểm tra robustness là chạy nhiều reasonable phân tích (analysis / 분석) specifications thay vì chọn một mô hình (model / 모델) duy nhất.

**Multiverse phân tích (analysis / 분석)** hoặc **specification curve** cho thấy conclusion có phụ thuộc mạnh vào analytic choice hay không.

> **ranh giới (boundary / 경계):** nếu tất cả specifications cùng dựa trên same biased mẫu (sample / 표본) hoặc invalid measure, robustness analytic không giải quyết độ lệch (bias / 편향) nền.

> **Chuyển mạch:** Ở chặng này của **Khoa học mở và cách đánh giá bằng chứng**, **14. Multiverse và specification phân tích (analysis / 분석)** nêu điều cần giải thích; **15. Bayesian bằng chứng (evidence / 증거) không thay bất định (uncertainty / 불확실성) bằng certainty** đối chiếu nó với bằng chứng hoặc nguồn kiểm chứng. Từ đây, **16. Triangulation** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 15. Bayesian bằng chứng (evidence / 증거) không thay bất định (uncertainty / 불확실성) bằng certainty

Bayesian methods cập nhật prior bằng likelihood để tạo posterior. Chúng có thể quantify hỗ trợ (support / 지원) cho competing các mô hình (models / 모델들) hoặc parameter phạm vi (range / 범위).

Nhưng kết quả (result / 결과) vẫn phụ thuộc mô hình (model / 모델), likelihood và prior choice. Prior sensitivity cần được xem xét khi conclusion nhạy.

Bayesian không phải “cách đúng, frequentist là sai”; chúng trả lời và biểu diễn bất định (uncertainty / 불확실성) theo khung phần mềm (framework / 프레임워크) khác nhau.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Khoa học mở và cách đánh giá bằng chứng**, **15. Bayesian bằng chứng (evidence / 증거) không thay bất định (uncertainty / 불확실성) bằng certainty** nêu điều cần giải thích; **16. Triangulation** đối chiếu nó với bằng chứng hoặc nguồn kiểm chứng. Từ đây, **17. Generalization và WEIRD samples** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 16. Triangulation

**Tam giác hóa (triangulation)** dùng methods có dạng thất bại (failure mode / 실패 모드) khác nhau để kiểm tra cùng phenomenon.

Nếu lab experiment, longitudinal dữ liệu (data / 데이터), natural experiment và physiological measure đều converge, confidence tăng hơn khi chỉ có nhiều studies cùng một thiết kế (design / 설계).

Nhưng convergence chỉ mạnh khi độ lệch (bias / 편향) không dùng chung (shared / 공유). Mười studies dùng cùng một self-report quy mô (scale / 규모) yếu không phải mười nguồn bằng chứng (evidence / 증거) độc lập hoàn toàn.

> **Chuyển mạch:** Trong **Khoa học mở và cách đánh giá bằng chứng**, **17. Generalization và WEIRD samples** tiếp nhận điểm tựa từ **16. Triangulation** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **18. bằng chứng (evidence / 증거) taxonomy của thư viện (library / 라이브러리)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 17. Generalization và WEIRD samples

Một tác động (effect / 효과) replicate ở nhiều university labs phương Tây chưa chắc là universal human psychology.

Cần hỏi population, ngôn ngữ (language / 언어), culture, age, socioeconomic ngữ cảnh (context / 맥락) và institutional môi trường (environment / 환경).

**bên ngoài (external / 외부) validity** không phải bonus sau nội bộ (internal / 내부) validity; với claim về “human nature”, nó là cốt lõi (core / 핵심) bằng chứng (evidence / 증거) yêu cầu (requirement / 요구사항).

> **Chuyển mạch:** Ở chặng này của **Khoa học mở và cách đánh giá bằng chứng**, **17. Generalization và WEIRD samples** nêu điều cần giải thích; **18. bằng chứng (evidence / 증거) taxonomy của thư viện (library / 라이브러리)** đối chiếu nó với bằng chứng hoặc nguồn kiểm chứng. Từ đây, **19. Cách đọc một paper** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 18. bằng chứng (evidence / 증거) taxonomy của thư viện (library / 라이브러리)

Thư viện (library / 라이브러리) này dùng bốn nhãn chính:

- **Established bằng chứng (evidence / 증거)**: tác động (effect / 효과)/tiến trình (process / 프로세스) được hỗ trợ (support / 지원) tương đối nhất quán trong phạm vi xác định.
- **hiện tại (current / 현재) lý thuyết (theory / 이론)**: mô hình (model / 모델) hiện được nghiên cứu và có hỗ trợ (support / 지원) nhưng chưa phải consensus cuối cùng.
- **Debated interpretation**: dữ liệu (data / 데이터) tồn tại nhưng interpretation hoặc generality còn tranh luận.
- **Historical lý thuyết (theory / 이론)**: quan trọng lịch sử nhưng không được trình bày như hiện đại (modern / 현대적) consensus.

Một chapter tốt phải nói rõ claim nằm ở tầng nào thay vì dùng cùng giọng chắc chắn cho tất cả.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Khoa học mở và cách đánh giá bằng chứng**, **18. bằng chứng (evidence / 증거) taxonomy của thư viện (library / 라이브러리)** nêu điều cần giải thích; **19. Cách đọc một paper** đối chiếu nó với bằng chứng hoặc nguồn kiểm chứng. Từ đây, **20. Những hiểu lầm phổ biến** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

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

> **Chuyển mạch:** Trong **Khoa học mở và cách đánh giá bằng chứng**, **20. Những hiểu lầm phổ biến** tiếp nhận điểm tựa từ **19. Cách đọc một paper** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **21. Mô hình tư duy** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 20. Những hiểu lầm phổ biến

**“Preregistered = đúng.”** Không. Nó tăng transparency, không bảo đảm validity.

**“Replicate thất bại (fail / 실패) = original fraud.”** Không. Có nhiều explanation; cần cumulative bằng chứng (evidence / 증거).

**“Meta-analysis ở trên mọi bằng chứng (evidence / 증거).”** Không. Chất lượng phụ thuộc studies đầu vào và synthesis phương thức (method / 메서드).

**“Open dữ liệu (data / 데이터) luôn tốt.”** Không nếu privacy rủi ro (risk / 위험) vượt benefit.

**“p < .05 nghĩa lý thuyết (theory / 이론) đúng.”** Không. Nó không cung cấp xác suất (probability / 확률) trực tiếp rằng lý thuyết (theory / 이론) đúng.

**“Một paper Nature/Science là đủ.”** Journal prestige không thay cumulative bằng chứng (evidence / 증거).

> **Chuyển mạch:** Ở chặng này của **Khoa học mở và cách đánh giá bằng chứng**, **21. Mô hình tư duy** gom các mảnh từ **20. Những hiểu lầm phổ biến** thành một kết luận có thể mang sang phần kế tiếp. Từ đây, **Kết nối kiến thức** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 21. Mô hình tư duy

Phần này chốt mental model thành một chuỗi có thể dùng lại: bối cảnh → cơ chế → bằng chứng → giới hạn → ứng dụng. Hãy đọc sơ đồ như công cụ suy luận, không như một nhãn kết luận tự động.

```text
Câu hỏi rõ
→ measurement phù hợp
→ design đúng inference
→ analysis minh bạch
→ uncertainty được báo cáo
→ replication / triangulation
→ boundary và generalization
```

Science đáng tin là một **tiến trình (process / 프로세스) tích lũy**, không phải một paper đơn lẻ.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Khoa học mở và cách đánh giá bằng chứng**, **Kết nối kiến thức** gom các mảnh từ **21. Mô hình tư duy** thành một kết luận có thể mang sang phần kế tiếp. Phần còn lại của file dùng kết quả này để khép lại mạch giải thích.

## Kết nối kiến thức

Đọc cùng [[02_research_methods]], [[03_measurement_statistics]], [[04_ethics_and_critical_thinking]], [[05_psychometrics_and_test_interpretation]], [[08_causal_inference_and_psychological_evidence]] và [[09_replication_meta_analysis_and_bayesian_reasoning]].

> **Bàn giao:** Sau **Kết nối kiến thức**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](../README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
