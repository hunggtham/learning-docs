# Tâm trắc học và diễn giải bài đo tâm lý

Tâm lý học nghiên cứu nhiều construct không thể quan sát trực tiếp: trí tuệ, lo âu, trầm cảm, tính cách, động lực, burnout, attachment hay cảm giác thuộc về. **Tâm trắc học (psychometrics)** nghiên cứu cách biến những construct này thành score có thể sử dụng một cách hợp lý, đồng thời đánh giá sai số và giới hạn của inference.

> **Trạng thái bằng chứng:** nguyên tắc `score ≠ construct`, reliability ≠ validity, validity gắn với interpretation/use và measurement equivalence cần được kiểm tra khi so sánh group là nền phương pháp tương đối vững. CTT, factor analysis, IRT và các measurement models là những mô hình hiện hành, không phải ontology duy nhất của tâm trí.

Xem quy ước chung tại [[../EVIDENCE_STATUS_GUIDE]].

## 1. Score không phải construct

Một bảng hỏi tạo ra con số; con số chỉ có ý nghĩa nếu có argument rằng response thực sự phản ánh construct cần đo trong population và mục đích cụ thể.

Ví dụ, một scale tên “social anxiety” nhưng chủ yếu hỏi mức thích đi party có thể lẫn lo âu xã hội với hướng nội. Một instrument có giao diện chuyên nghiệp không tự trở thành psychological measure tốt.

Chuỗi inference là:

```text
Construct
   ↓ xác định domain
Items / tasks / observations
   ↓ response process
Observed responses
   ↓ scoring model
Score
   ↓ validity evidence
Interpretation
   ↓ decision context
Use
```

Mỗi mũi tên đều cần justification.

## 2. Construct definition và content coverage

Trước khi viết item, cần xác định construct gồm gì và không gồm gì. **Độ giá trị nội dung (content validity)** hỏi các indicator có phủ đủ domain hay không.

Nếu đo burnout nhưng chỉ hỏi tiredness, instrument có thể bỏ cynicism hoặc occupational context. Nếu đo intelligence nhưng chỉ dùng vocabulary, score có thể phản ánh schooling và language exposure nhiều hơn domain mong muốn.

Content mapping, expert review và cognitive interviewing thường hữu ích để kiểm tra item có được hiểu đúng như dự định hay không.

## 3. Classical Test Theory

Trong **Classical Test Theory (CTT)**:

\[
X = T + E
\]

`X` là observed score, `T` là true score theo model và `E` là measurement error. True score ở đây là expected score qua repeated equivalent measurement, không phải “giá trị thật tuyệt đối” của person.

CTT hữu ích để reasoning về reliability ở test level, nhưng precision có thể khác nhau giữa trait levels và item sets; đây là một lý do IRT được phát triển.

## 4. Reliability là consistency cho một use case

### Internal consistency

Internal consistency hỏi các item có covary đủ để support interpretation composite score không. Cronbach's alpha phổ biến nhưng **alpha cao không chứng minh unidimensionality**. Alpha còn tăng khi item redundant.

Trong nhiều trường hợp, omega hoặc model-based reliability có assumptions phù hợp hơn, nhưng không có một coefficient “tốt nhất cho mọi test”. Reliability phải gắn với model và mục đích sử dụng.

### Test–retest

Test–retest reliability hỏi score có ổn định qua thời gian khi construct được kỳ vọng ổn định hay không. Với state thay đổi nhanh như mood trong ngày, test–retest thấp không nhất thiết là lỗi measurement.

### Inter-rater reliability

Khi clinician hoặc coder đánh giá behavior, agreement giữa raters quan trọng. Rubric, training và blinding có thể giảm drift nhưng không loại bỏ hoàn toàn subjectivity.

## 5. Validity là argument về interpretation và use

Không nên nói “test này valid” như một thuộc tính bất biến. Cách diễn đạt tốt hơn là: **evidence hiện có hỗ trợ tới mức nào cho interpretation score này, trong population này, cho use này?**

Validity evidence thường bao gồm:

- content;
- response process;
- internal structure;
- relation with other variables;
- consequences và fairness của use.

**Convergent evidence** hỏi measure có quan hệ hợp lý với construct gần không. **Discriminant evidence** hỏi nó có đủ khác construct lân cận không. **Predictive/criterion evidence** hỏi score có liên hệ với outcome hoặc criterion liên quan không.

Structural validity chỉ là một phần. Factor model đẹp không tự chứng minh external validity.

## 6. Factor analysis không “phát hiện các phần của não”

**Exploratory Factor Analysis (EFA)** tìm latent structure có thể giải thích covariance giữa items. **Confirmatory Factor Analysis (CFA)** kiểm tra structure được hypothesize trước.

Factors là statistical constructs. Chúng không tự động là natural kinds hoặc distinct neural systems. Result phụ thuộc item pool, estimator, rotation, sample và model specification.

Một scale có thể fit one-factor model trong sample này nhưng two-factor model trong sample khác. Điều đó không nên bị che bằng một chỉ số fit duy nhất.

## 7. Measurement invariance và so sánh group

Khi so sánh Vietnamese, Korean và English samples, literal translation chưa đủ. **Tính bất biến đo lường (measurement invariance)** kiểm tra measurement relations có đủ tương đương để support comparison hay không.

Các bước thường được mô tả như:

- configural invariance: structure cơ bản tương tự;
- metric invariance: factor loadings đủ tương đương để so quan hệ;
- scalar invariance: intercept/threshold đủ tương đương để so latent means theo model.

Đây là modeling framework, không phải checklist tuyệt đối. Partial invariance, alignment hoặc item-level investigation có thể phù hợp tùy dữ liệu và mục tiêu.

## 8. Differential Item Functioning

**Hoạt động khác biệt của item (Differential Item Functioning — DIF)** xảy ra khi people có cùng latent trait nhưng xác suất trả lời item khác nhau theo group.

Ví dụ item “tôi thường nói thẳng khi không đồng ý với cấp trên” có thể phản ánh assertiveness nhưng cũng chịu power-distance norm. Nếu DIF mạnh, group difference có thể đến từ item functioning chứ không hoàn toàn từ latent construct.

## 9. Item Response Theory

**Item Response Theory (IRT)** model probability của response dựa trên latent trait và item parameters. Trong model phổ biến, item có thể khác về difficulty và discrimination; một số model còn thêm guessing hoặc threshold parameters.

IRT cho phép precision thay đổi theo trait level. Computerized adaptive testing có thể chọn item informative hơn quanh current estimate, giảm số item cần dùng.

> **Current theory/model:** IRT là họ measurement models rất mạnh, nhưng inference phụ thuộc unidimensionality/local-independence assumptions và model fit. Không nên dùng “IRT-based” như nhãn chất lượng nếu assumptions không được kiểm tra.

## 10. Norms và reference group

Raw score thường không tự có nghĩa. Percentile hoặc standardized score phụ thuộc **nhóm chuẩn (normative sample)**.

Percentile 90 nghĩa person đứng khoảng 90th percentile so với reference group, không có nghĩa “90% khả năng” hay “đúng 90%”. Norm cũ, population khác hoặc sampling không đại diện có thể làm interpretation sai.

## 11. Screening khác diagnosis

Screening thường ưu tiên phát hiện người có khả năng cần assessment thêm. Nó không thay clinical interview, history, impairment, differential diagnosis và medical evaluation.

### Sensitivity và specificity

**Độ nhạy (sensitivity)** là tỷ lệ cases thật được phát hiện. **Độ đặc hiệu (specificity)** là tỷ lệ non-cases được loại đúng.

Threshold thường tạo trade-off: tăng sensitivity có thể làm false positives tăng.

### Predictive value và base rate

**Positive predictive value** và **negative predictive value** phụ thuộc prevalence/base rate. Một test có sensitivity và specificity cao vẫn có thể tạo nhiều false positive khi condition rất hiếm.

Đây là ứng dụng trực tiếp của Bayesian reasoning.

## 12. Fairness không chỉ là “cùng một test cho mọi người”

Fairness liên quan access, language, disability accommodation, item bias, norming, consequences và whether score interpretation is comparable.

Cùng procedure cho mọi người có thể không công bằng nếu một group bị measurement barrier không liên quan construct, ví dụ hearing impairment khi test không có accommodation phù hợp.

## 13. Cross-cultural adaptation

Dịch scale tốt thường gồm nhiều bước: forward translation, reconciliation, back translation, expert review, cognitive interviewing và psychometric evaluation ở population đích.

Một câu literal-equivalent vẫn có thể cultural-non-equivalent. “Family obligation”, “assertiveness” hay “independence” có meaning khác nhau giữa context.

## 14. Test classification và internet psychology

Online personality quiz thường biến continuous traits thành binary categories để dễ hiểu. Điều này có thể có entertainment value nhưng không tự mang psychometric validity.

MBTI chịu ảnh hưởng historical từ Jung nhưng không phải bằng chứng cho Jungian typology; modern personality science thường ưu tiên dimensional trait models. Xem [[../03_human_development_and_person/03_personality]] và [[../90_connections/06_historical_theories_and_modern_evidence_matrix]].

## 15. Measurement reporting và replication

Replication chỉ hữu ích nếu measure được mô tả đủ rõ và hoạt động tương tự trong sample mới. Nếu original study không báo reliability, scoring, item wording hoặc validity evidence, apparent replication failure có thể partly là measurement failure.

Do đó transparency về instrument là một phần của reproducibility, không phải appendix kỹ thuật.

Xem [[09_replication_meta_analysis_and_bayesian_reasoning]].

## 16. Mức bằng chứng

### Established evidence

- observed score luôn cần được hiểu qua measurement error;
- reliability không đồng nghĩa validity;
- validity support phải gắn interpretation/use;
- base rate ảnh hưởng predictive value;
- group comparison cần evidence về comparability của measurement.

### Current models

CTT, CFA/SEM, IRT, generalizability theory và Bayesian psychometrics là model families hiện hành. Chúng không phải competing religions; mỗi model trả lời questions khác nhau dưới assumptions khác nhau.

### Debated/conditional issues

Cutoff “reliability đủ tốt”, fit-index thresholds, mức invariance tối thiểu, choice giữa factor models và treatment của ordinal data đều phụ thuộc context. Rule-of-thumb không nên được dùng như scientific law.

## 17. Những hiểu lầm phổ biến

**“Cronbach's alpha > .90 nghĩa test rất tốt.”** Sai. Alpha có thể cao vì item redundant và không chứng minh construct validity.

**“Factor analysis tìm ra các loại người tự nhiên.”** Không nhất thiết. Factor model mô tả covariance structure.

**“Một cutoff tạo ra hai nhóm thật trong tự nhiên.”** Nhiều traits continuous; threshold thường phục vụ decision rule.

**“Một test đã được publish thì dùng ở population nào cũng được.”** Không đúng. Interpretation cần evidence ở context liên quan.

## 18. Mental model

```text
Construct definition
      ↓
Content & response process
      ↓
Measurement model
      ↓
Reliability / error
      ↓
Validity evidence
      ↓
Population & fairness
      ↓
Interpretation
      ↓
Decision
```

Một score chỉ mạnh bằng weakest link trong inference chain.

## Kết nối kiến thức

Đọc cùng [[03_measurement_statistics]], [[06_open_science_and_evidence_evaluation]], [[09_replication_meta_analysis_and_bayesian_reasoning]], [[../02_learning_and_cognition/03_intelligence_and_cognitive_differences]], [[../03_human_development_and_person/03_personality]] và [[../04_mental_health/01_assessment_and_diagnosis]].

### Nguồn định hướng

- *Standards for Educational and Psychological Testing* — AERA, APA, NCME.
- Best-practice guidelines hiện đại về scale development/validation trong psychological và behavioral sciences.
- Nghiên cứu replication gần đây nhấn mạnh measurement reporting, reliability, validity và invariance là một phần của reproducibility.
