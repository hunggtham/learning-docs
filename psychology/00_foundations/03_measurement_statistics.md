# Đo lường và thống kê nền tảng trong tâm lý học

> **Mạch đọc:** Đọc **Đo lường và thống kê nền tảng trong tâm lý học** như một mắt xích của lộ trình học (learning path / 학습 경로) hiện tại, không như một ghi chú tách rời. Nội dung đi từ **1. Từ construct tới biến quan sát** sang **2. Thao tác hóa không phải “định nghĩa thật” của construct**; điểm nối này chuẩn bị câu hỏi cho các mục sau thay vì dừng ở định nghĩa đầu tiên.


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

Sai ở bất kỳ bước nào cũng có thể tạo kết luận sai dù phép tính thống kê hoàn toàn chính xác. Đây là lý do trong psychology, đo lường (measurement / 측정) thường là vấn đề sâu hơn calculation.

## 2. Thao tác hóa không phải “định nghĩa thật” của construct

**Thao tác hóa (operationalization)** biến một khái niệm thành thủ tục đo cụ thể. Nếu nghiên cứu “chú ý” bằng reaction thời gian (time / 시간) trong một tác vụ (task / 작업), tác vụ (task / 작업) đó chỉ cung cấp một cửa sổ vào attention, không phải toàn bộ attention.

Một construct có thể có nhiều operationalization. Khi nhiều phương pháp độc lập hội tụ về cùng một mẫu (pattern / 패턴), suy luận (inference / 추론) thường mạnh hơn. Ngược lại, nếu toàn bộ literature dựa vào một bảng hỏi duy nhất, ta khó biết kết quả (result / 결과) phản ánh construct hay idiosyncrasy của instrument.

## 3. Thang đo và loại dữ liệu

Dữ liệu có thể được mô tả theo nhiều kiểu. **Danh nghĩa (nominal)** biểu diễn category không có thứ tự; **thứ bậc (ordinal)** có thứ tự nhưng khoảng cách giữa mức không nhất thiết bằng nhau; **khoảng (interval)** giả định khoảng cách có ý nghĩa; **tỷ lệ (ratio)** có mốc zero có ý nghĩa theo mô hình đo.

Trong thực hành psychology, câu hỏi Likert riêng lẻ thường mang tính ordinal, còn tổng hoặc trung bình của nhiều item đôi khi được mô hình hóa gần continuous nếu giả định phù hợp. Đây không phải quy tắc máy móc; lựa chọn phân tích cần dựa vào đo lường (measurement / 측정) mô hình (model / 모델), phân phối và robustness của phương pháp.

## 4. Sai số đo lường

Một score quan sát luôn chứa nhiễu. Trong mô hình cổ điển:

\[
X = T + E
\]

`X` là score quan sát, `T` là true score theo mô hình và `E` là sai số đo lường. “True score” không phải bản chất siêu hình của con người; nó là giá trị kỳ vọng qua những phép đo tương đương dưới giả định của Classical kiểm thử (test / 테스트) lý thuyết (theory / 이론).

Sai số có thể đến từ wording, fatigue, rater, thiết bị, day-to-day fluctuation, ngôn ngữ (language / 언어), ngữ cảnh (context / 맥락) hoặc sampling item. Sai số đo lường không chỉ làm score cá nhân dao động; nó còn có thể làm tương quan yếu đi, làm tác động (effect / 효과) estimate lệch và giảm khả năng tái lập.

## 5. Độ tin cậy khác độ giá trị

**độ tin cậy (reliability / 신뢰성)** hỏi phép đo có nhất quán ở mức cần thiết cho use trường hợp (case / 사례) hay không. Các dạng thường gặp gồm kiểm thử (test / 테스트)–retest, inter-rater và nội bộ (internal / 내부) consistency.

**Độ giá trị (validity)** hỏi bằng chứng và lý thuyết có hỗ trợ cách diễn giải score cho một mục đích cụ thể hay không. Vì vậy không nên nói đơn giản “kiểm thử (test / 테스트) này có validity cao” mà không nói **interpretation nào, population nào, mục đích nào**.

Một thước đo có thể rất reliable nhưng đo sai construct. Ngược lại, một construct biến động theo thời gian không nên bị kỳ vọng kiểm thử (test / 테스트)–retest quá cao nếu bản chất phenomenon thật sự thay đổi.

Phần này được phát triển sâu hơn tại [[05_psychometrics_and_test_interpretation]].

## 6. Phân phối, trung tâm và độ phân tán

Trung bình (mean) là một summary hữu ích nhưng không mô tả toàn bộ phân phối (distribution / 분포). Hai nhóm có cùng mean có thể khác mạnh về variance, skewness hoặc subgroup cấu trúc (structure / 구조). Hai nhóm có mean khác nhau vẫn có thể overlap rất lớn.

**Độ lệch chuẩn (standard deviation)** mô tả mức phân tán quanh trung bình theo mô hình; **trung vị (median)** hữu ích khi phân phối (distribution / 분포) lệch hoặc có outlier mạnh. Khi đọc psychological dữ liệu (data / 데이터), nên nhìn cả center, spread, phân phối (distribution / 분포) shape và missingness thay vì chỉ một average.

## 7. Kích thước hiệu ứng quan trọng hơn câu hỏi “có hay không”

**Kích thước hiệu ứng (effect size)** mô tả độ lớn của khác biệt hoặc mối liên hệ. Cohen's d, correlation r, odds ratio và rủi ro (risk / 위험) ratio là các ví dụ dùng cho thiết kế khác nhau.

Một tác động (effect / 효과) có thể rất nhỏ nhưng statistically detectable trong mẫu (sample / 표본) lớn. Ngược lại, tác động (effect / 효과) lớn trong mẫu (sample / 표본) nhỏ có thể có khoảng bất định rất rộng. Vì vậy câu hỏi tốt hơn không phải chỉ là “p < .05 không?”, mà là:

```text
Hiệu ứng lớn bao nhiêu?
Độ không chắc chắn bao nhiêu?
Đo lường tốt đến đâu?
Có ý nghĩa thực tiễn không?
Có generalize sang population cần quan tâm không?
```

## 8. Khoảng tin cậy và độ không chắc chắn

**Khoảng tin cậy (confidence interval)** được tạo bởi một procedure có tính chất bao phủ dài hạn dưới những giả định nhất định. Trong thực hành, nó giúp thấy precision của estimate. Khoảng hẹp thường nghĩa estimate chính xác hơn, nhưng không bảo đảm đo lường (measurement / 측정) không độ lệch (bias / 편향) hoặc mô hình (model / 모델) đúng.

Độ không chắc chắn không phải khuyết điểm cần giấu. Báo cáo bất định (uncertainty / 불확실성) rõ là một phần của lập luận (reasoning / 추론) khoa học.

## 9. Giá trị p không phải xác suất hypothesis sai

**Giá trị p (p-value)** không cho biết xác suất giả thuyết không đúng. Nó mô tả mức độ dữ liệu hiện tại hoặc dữ liệu cực đoan hơn tương thích với null mô hình (model / 모델) dưới các giả định của phép kiểm.

Ngưỡng `.05` là convention, không phải đường biên giữa “truth” và “falsehood”. kết quả (result / 결과) `p=.049` và `p=.051` không phải hai thế giới khoa học khác nhau.

Khi nhiều phân tích (analysis / 분석) được thử nhưng chỉ kết quả (result / 결과) thuận lợi được báo cáo, false-positive rủi ro (risk / 위험) tăng. Vì vậy preregistration, transparent reporting và correction for multiple testing quan trọng.

## 10. Công suất thống kê và cỡ mẫu (sample size / 표본 크기)

**Công suất thống kê (statistical power)** là xác suất procedure phát hiện một tác động (effect / 효과) có kích thước giả định trong những điều kiện cụ thể. Power thấp làm estimate không ổn định và literature dễ bị selection độ lệch (bias / 편향): chỉ những estimate tình cờ lớn mới vượt threshold để được công bố.

Cỡ mẫu (sample size / 표본 크기) lớn hơn thường tăng precision, nhưng “N lớn” không sửa được đo lường (measurement / 측정) kém, sampling độ lệch (bias / 편향) hoặc confounding.

## 11. Correlation và regression không tự tạo causality

Correlation cho biết variables thay đổi cùng nhau theo một mẫu (pattern / 패턴) nhất định. Regression có thể estimate conditional association khi kiểm soát một số variables, nhưng neither automatically proves causation.

Điều chỉnh sai biến còn có thể làm suy luận (inference / 추론) tệ hơn, ví dụ điều khiển (control / 제어) mediator hoặc collider. lập luận nhân quả (causal reasoning / 인과적 추론) được phát triển riêng tại [[08_causal_inference_and_psychological_evidence]].

## 12. Repeated measures và dữ liệu lồng nhau

Psychological dữ liệu (data / 데이터) thường không độc lập: nhiều observation đến từ cùng một người, nhiều học sinh nằm trong cùng lớp, nhiều nhân viên nằm trong cùng nhóm (team / 팀). Nếu coi tất cả rows là independent, bất định (uncertainty / 불확실성) có thể bị đánh giá quá thấp.

Repeated-measures các mô hình (models / 모델들) và multilevel các mô hình (models / 모델들) cho phép tách variation giữa người với variation trong cùng người hoặc giữa group với trong group. Đây là điểm quan trọng khi dùng experience sampling, longitudinal diary hoặc workplace dữ liệu (data / 데이터).

Xem [[07_ecological_momentary_assessment_and_real_world_measurement]].

## 13. Missing dữ liệu (data / 데이터) không chỉ là vấn đề “thiếu vài ô”

Missingness có thể mang thông tin. Người stress nặng có thể bỏ survey nhiều hơn; participant không cải thiện có thể dropout khỏi treatment study. Nếu missingness liên quan kết quả (outcome / 결과) hoặc variables không đo được, complete-case phân tích (analysis / 분석) có thể độ lệch (bias / 편향).

Các khái niệm MCAR, MAR và MNAR là mô hình hóa cơ chế missingness, không phải nhãn chắc chắn quan sát trực tiếp được. Sensitivity phân tích (analysis / 분석) thường quan trọng khi conclusion phụ thuộc giả định missing dữ liệu (data / 데이터).

## 14. So sánh nhóm và tính bất biến đo lường

Nếu hai nhóm dùng cùng một quy mô (scale / 규모), chưa chắc cùng score mang cùng meaning. ngôn ngữ (language / 언어), norm, phản hồi (response / 응답) style hoặc item interpretation có thể khác.

**Tính bất biến đo lường (measurement invariance)** là một nhóm kiểm tra xem đo lường (measurement / 측정) mô hình (model / 모델) có đủ tương đương để hỗ trợ (support / 지원) comparison hay không. Đây đặc biệt quan trọng trong nghiên cứu xuyên văn hóa, giới, tuổi hoặc di chuyển (migration / 마이그레이션).

Không đạt invariance không có nghĩa “hai nhóm hoàn toàn không so sánh được”; nó báo rằng interpretation cần thận trọng và có thể cần mô hình (model / 모델) khác, partial invariance hoặc item-level investigation.

## 15. Mức bằng chứng trong đo lường (measurement / 측정)

### Bằng chứng tương đối vững

Sai số đo lường (measurement error / 측정 오차), độ tin cậy (reliability / 신뢰성), validity bằng chứng (evidence / 증거), sampling bất định (uncertainty / 불확실성) và effect-size lập luận (reasoning / 추론) là nền phương pháp đã được sử dụng rộng rãi và có cơ sở mạnh.

### Lý thuyết/mô hình hiện hành

CTT, factor các mô hình (models / 모델들), IRT, multilevel các mô hình (models / 모델들) hay Bayesian các mô hình (models / 모델들) là công cụ formal hóa. Chúng hữu ích khi các giả định (assumptions / 가정들) phù hợp; không mô hình (model / 모델) nào là “bản chất thật duy nhất” của construct.

### Vấn đề còn tranh luận

Cách tốt nhất để mô hình (model / 모델) Likert dữ liệu (data / 데이터), tiêu chuẩn fit tối ưu, mức invariance cần thiết cho từng loại comparison, hoặc threshold “đủ tốt” cho độ tin cậy (reliability / 신뢰성) phụ thuộc mục đích và literature cụ thể. Không nên biến rule-of-thumb thành luật tự nhiên.

## 16. mô hình tư duy (mental model / 사고 모델)

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

Statistical sophistication ở phần giữa không thể cứu một construct mơ hồ ở đầu chuỗi hoặc một interpretation vượt quá bằng chứng (evidence / 증거) ở cuối chuỗi.

## Kết nối kiến thức

Đọc tiếp [[05_psychometrics_and_test_interpretation]], [[09_replication_meta_analysis_and_bayesian_reasoning]], [[02_research_methods]], [[06_open_science_and_evidence_evaluation]] và [[08_causal_inference_and_psychological_evidence]].

### Nguồn định hướng

- *Standards for Educational and Psychological Testing* (AERA, APA, NCME): validity được hiểu là bằng chứng (evidence / 증거) và lý thuyết (theory / 이론) hỗ trợ interpretation score cho proposed use.
- Các guideline hiện đại về phát triển thang đo tâm lý nhấn mạnh construct definition, content coverage, structural bằng chứng (evidence / 증거), độ tin cậy (reliability / 신뢰성), validity và cross-group evaluation thay vì chỉ báo Cronbach's alpha.

> **Bàn giao:** Sau **Nguồn định hướng**, hãy chốt bất biến (invariant / 불변식) và giới hạn của mục này trước khi nối sang kiến thức kế tiếp. Có thể đọc tiếp [00 psychology as science](./00_psychology_as_science.md) để đối chiếu ranh giới (boundary / 경계) gần nhất.
