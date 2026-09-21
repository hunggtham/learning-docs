# Đo lường và thống kê nền tảng trong tâm lý học

Tâm lý học thường nghiên cứu những hiện tượng không thể quan sát trực tiếp như trí nhớ, lo âu, trí tuệ, động lực, tính cách hay cảm giác thuộc về. Vì vậy, trước khi hỏi “kết quả có ý nghĩa thống kê không?”, cần hỏi một câu cơ bản hơn: **ta đang đo cái gì, bằng dấu hiệu nào, với sai số nào và cho mục đích diễn giải nào?**

> **Trạng thái bằng chứng:** các nguyên tắc về sai số đo lường, độ tin cậy, độ giá trị, kích thước hiệu ứng và sự không chắc chắn là nền phương pháp tương đối vững. Mô hình cụ thể dùng để biểu diễn construct hoặc phân phối dữ liệu vẫn phụ thuộc giả định và bối cảnh.

Xem quy ước chung tại [[../EVIDENCE_STATUS_GUIDE]].

## 1. Từ construct tới biến quan sát

Một **cấu trúc tâm lý (construct)** là khái niệm lý thuyết như lo âu, trí nhớ làm việc hay hướng ngoại. Construct không được quan sát trực tiếp; ta suy luận nó từ **chỉ báo quan sát được (observable indicator)** như câu trả lời bảng hỏi, thời gian phản ứng, lựa chọn hành vi, đánh giá của người quan sát hoặc tín hiệu sinh lý.

Chuỗi suy luận cơ bản là:

```text
Construct
   ↓ thao tác hóa (operationalization)
Task / item / behavior / signal
   ↓ scoring
Observed variable
   ↓ inference
Interpretation about construct
```

Sai ở bất kỳ bước nào cũng có thể tạo kết luận sai dù phép tính thống kê hoàn toàn chính xác. Đây là lý do trong psychology, measurement thường là vấn đề sâu hơn calculation.

## 2. Thao tác hóa không phải “định nghĩa thật” của construct

**Thao tác hóa (operationalization)** biến một khái niệm thành thủ tục đo cụ thể. Nếu nghiên cứu “chú ý” bằng reaction time trong một task, task đó chỉ cung cấp một cửa sổ vào attention, không phải toàn bộ attention.

Một construct có thể có nhiều operationalization. Khi nhiều phương pháp độc lập hội tụ về cùng một pattern, inference thường mạnh hơn. Ngược lại, nếu toàn bộ literature dựa vào một bảng hỏi duy nhất, ta khó biết result phản ánh construct hay idiosyncrasy của instrument.

## 3. Thang đo và loại dữ liệu

Dữ liệu có thể được mô tả theo nhiều kiểu. **Danh nghĩa (nominal)** biểu diễn category không có thứ tự; **thứ bậc (ordinal)** có thứ tự nhưng khoảng cách giữa mức không nhất thiết bằng nhau; **khoảng (interval)** giả định khoảng cách có ý nghĩa; **tỷ lệ (ratio)** có mốc zero có ý nghĩa theo mô hình đo.

Trong thực hành psychology, câu hỏi Likert riêng lẻ thường mang tính ordinal, còn tổng hoặc trung bình của nhiều item đôi khi được mô hình hóa gần continuous nếu giả định phù hợp. Đây không phải quy tắc máy móc; lựa chọn phân tích cần dựa vào measurement model, phân phối và robustness của phương pháp.

## 4. Sai số đo lường

Một score quan sát luôn chứa nhiễu. Trong mô hình cổ điển:

\[
X = T + E
\]

`X` là score quan sát, `T` là true score theo mô hình và `E` là sai số đo lường. “True score” không phải bản chất siêu hình của con người; nó là giá trị kỳ vọng qua những phép đo tương đương dưới giả định của Classical Test Theory.

Sai số có thể đến từ wording, fatigue, rater, thiết bị, day-to-day fluctuation, language, context hoặc sampling item. Sai số đo lường không chỉ làm score cá nhân dao động; nó còn có thể làm tương quan yếu đi, làm effect estimate lệch và giảm khả năng tái lập.

## 5. Độ tin cậy khác độ giá trị

**Độ tin cậy (reliability)** hỏi phép đo có nhất quán ở mức cần thiết cho use case hay không. Các dạng thường gặp gồm test–retest, inter-rater và internal consistency.

**Độ giá trị (validity)** hỏi bằng chứng và lý thuyết có hỗ trợ cách diễn giải score cho một mục đích cụ thể hay không. Vì vậy không nên nói đơn giản “test này có validity cao” mà không nói **interpretation nào, population nào, mục đích nào**.

Một thước đo có thể rất reliable nhưng đo sai construct. Ngược lại, một construct biến động theo thời gian không nên bị kỳ vọng test–retest quá cao nếu bản chất phenomenon thật sự thay đổi.

Phần này được phát triển sâu hơn tại [[05_psychometrics_and_test_interpretation]].

## 6. Phân phối, trung tâm và độ phân tán

Trung bình (mean) là một summary hữu ích nhưng không mô tả toàn bộ distribution. Hai nhóm có cùng mean có thể khác mạnh về variance, skewness hoặc subgroup structure. Hai nhóm có mean khác nhau vẫn có thể overlap rất lớn.

**Độ lệch chuẩn (standard deviation)** mô tả mức phân tán quanh trung bình theo mô hình; **trung vị (median)** hữu ích khi distribution lệch hoặc có outlier mạnh. Khi đọc psychological data, nên nhìn cả center, spread, distribution shape và missingness thay vì chỉ một average.

## 7. Kích thước hiệu ứng quan trọng hơn câu hỏi “có hay không”

**Kích thước hiệu ứng (effect size)** mô tả độ lớn của khác biệt hoặc mối liên hệ. Cohen's d, correlation r, odds ratio và risk ratio là các ví dụ dùng cho thiết kế khác nhau.

Một effect có thể rất nhỏ nhưng statistically detectable trong sample lớn. Ngược lại, effect lớn trong sample nhỏ có thể có khoảng bất định rất rộng. Vì vậy câu hỏi tốt hơn không phải chỉ là “p < .05 không?”, mà là:

```text
Hiệu ứng lớn bao nhiêu?
Độ không chắc chắn bao nhiêu?
Đo lường tốt đến đâu?
Có ý nghĩa thực tiễn không?
Có generalize sang population cần quan tâm không?
```

## 8. Khoảng tin cậy và độ không chắc chắn

**Khoảng tin cậy (confidence interval)** được tạo bởi một procedure có tính chất bao phủ dài hạn dưới những giả định nhất định. Trong thực hành, nó giúp thấy precision của estimate. Khoảng hẹp thường nghĩa estimate chính xác hơn, nhưng không bảo đảm measurement không bias hoặc model đúng.

Độ không chắc chắn không phải khuyết điểm cần giấu. Báo cáo uncertainty rõ là một phần của reasoning khoa học.

## 9. Giá trị p không phải xác suất hypothesis sai

**Giá trị p (p-value)** không cho biết xác suất giả thuyết không đúng. Nó mô tả mức độ dữ liệu hiện tại hoặc dữ liệu cực đoan hơn tương thích với null model dưới các giả định của phép kiểm.

Ngưỡng `.05` là convention, không phải đường biên giữa “truth” và “falsehood”. Result `p=.049` và `p=.051` không phải hai thế giới khoa học khác nhau.

Khi nhiều analysis được thử nhưng chỉ result thuận lợi được báo cáo, false-positive risk tăng. Vì vậy preregistration, transparent reporting và correction for multiple testing quan trọng.

## 10. Công suất thống kê và sample size

**Công suất thống kê (statistical power)** là xác suất procedure phát hiện một effect có kích thước giả định trong những điều kiện cụ thể. Power thấp làm estimate không ổn định và literature dễ bị selection bias: chỉ những estimate tình cờ lớn mới vượt threshold để được công bố.

Sample size lớn hơn thường tăng precision, nhưng “N lớn” không sửa được measurement kém, sampling bias hoặc confounding.

## 11. Correlation và regression không tự tạo causality

Correlation cho biết variables thay đổi cùng nhau theo một pattern nhất định. Regression có thể estimate conditional association khi kiểm soát một số variables, nhưng neither automatically proves causation.

Điều chỉnh sai biến còn có thể làm inference tệ hơn, ví dụ control mediator hoặc collider. Causal reasoning được phát triển riêng tại [[08_causal_inference_and_psychological_evidence]].

## 12. Repeated measures và dữ liệu lồng nhau

Psychological data thường không độc lập: nhiều observation đến từ cùng một người, nhiều học sinh nằm trong cùng lớp, nhiều nhân viên nằm trong cùng team. Nếu coi tất cả rows là independent, uncertainty có thể bị đánh giá quá thấp.

Repeated-measures models và multilevel models cho phép tách variation giữa người với variation trong cùng người hoặc giữa group với trong group. Đây là điểm quan trọng khi dùng experience sampling, longitudinal diary hoặc workplace data.

Xem [[07_ecological_momentary_assessment_and_real_world_measurement]].

## 13. Missing data không chỉ là vấn đề “thiếu vài ô”

Missingness có thể mang thông tin. Người stress nặng có thể bỏ survey nhiều hơn; participant không cải thiện có thể dropout khỏi treatment study. Nếu missingness liên quan outcome hoặc variables không đo được, complete-case analysis có thể bias.

Các khái niệm MCAR, MAR và MNAR là mô hình hóa cơ chế missingness, không phải nhãn chắc chắn quan sát trực tiếp được. Sensitivity analysis thường quan trọng khi conclusion phụ thuộc giả định missing data.

## 14. So sánh nhóm và tính bất biến đo lường

Nếu hai nhóm dùng cùng một scale, chưa chắc cùng score mang cùng meaning. Language, norm, response style hoặc item interpretation có thể khác.

**Tính bất biến đo lường (measurement invariance)** là một nhóm kiểm tra xem measurement model có đủ tương đương để support comparison hay không. Đây đặc biệt quan trọng trong nghiên cứu xuyên văn hóa, giới, tuổi hoặc migration.

Không đạt invariance không có nghĩa “hai nhóm hoàn toàn không so sánh được”; nó báo rằng interpretation cần thận trọng và có thể cần model khác, partial invariance hoặc item-level investigation.

## 15. Mức bằng chứng trong measurement

### Bằng chứng tương đối vững

Measurement error, reliability, validity evidence, sampling uncertainty và effect-size reasoning là nền phương pháp đã được sử dụng rộng rãi và có cơ sở mạnh.

### Lý thuyết/mô hình hiện hành

CTT, factor models, IRT, multilevel models hay Bayesian models là công cụ formal hóa. Chúng hữu ích khi assumptions phù hợp; không model nào là “bản chất thật duy nhất” của construct.

### Vấn đề còn tranh luận

Cách tốt nhất để model Likert data, tiêu chuẩn fit tối ưu, mức invariance cần thiết cho từng loại comparison, hoặc threshold “đủ tốt” cho reliability phụ thuộc mục đích và literature cụ thể. Không nên biến rule-of-thumb thành luật tự nhiên.

## 16. Mental model

```text
Construct
   ↓
Measurement design
   ↓
Observed data
   ↓
Statistical model
   ↓
Estimate + uncertainty
   ↓
Interpretation
   ↓
Decision
```

Statistical sophistication ở phần giữa không thể cứu một construct mơ hồ ở đầu chuỗi hoặc một interpretation vượt quá evidence ở cuối chuỗi.

## Kết nối kiến thức

Đọc tiếp [[05_psychometrics_and_test_interpretation]], [[09_replication_meta_analysis_and_bayesian_reasoning]], [[02_research_methods]], [[06_open_science_and_evidence_evaluation]] và [[08_causal_inference_and_psychological_evidence]].

### Nguồn định hướng

- *Standards for Educational and Psychological Testing* (AERA, APA, NCME): validity được hiểu là evidence và theory hỗ trợ interpretation score cho proposed use.
- Các guideline hiện đại về phát triển thang đo tâm lý nhấn mạnh construct definition, content coverage, structural evidence, reliability, validity và cross-group evaluation thay vì chỉ báo Cronbach's alpha.
