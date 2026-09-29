# Tâm trắc học và diễn giải bài đo tâm lý

> **Mạch đọc:** Đọc **Tâm trắc học và diễn giải bài đo tâm lý** như một mắt xích của lộ trình học (learning path / 학습 경로) hiện tại, không như một ghi chú tách rời. Nội dung đi từ **1. Score không phải construct** sang **2. Construct definition và content coverage**; điểm nối này chuẩn bị câu hỏi cho các mục sau thay vì dừng ở định nghĩa đầu tiên.


Tâm lý học nghiên cứu nhiều construct không thể quan sát trực tiếp: trí tuệ, lo âu, trầm cảm, tính cách, động lực, burnout, attachment hay cảm giác thuộc về. **Tâm trắc học (psychometrics)** nghiên cứu cách biến những construct này thành score có thể sử dụng một cách hợp lý, đồng thời đánh giá sai số và giới hạn của suy luận (inference / 추론).

> **Trạng thái bằng chứng:** nguyên tắc `score ≠ construct`, độ tin cậy (reliability / 신뢰성) ≠ validity, validity gắn với interpretation/use và đo lường (measurement / 측정) equivalence cần được kiểm tra khi so sánh group là nền phương pháp tương đối vững. CTT, factor phân tích (analysis / 분석), IRT và các đo lường (measurement / 측정) các mô hình (models / 모델들) là những mô hình hiện hành, không phải ontology duy nhất của tâm trí.

Xem quy ước chung tại [[../EVIDENCE_STATUS_GUIDE]].

## 1. Score không phải construct

Một bảng hỏi tạo ra con số; con số chỉ có ý nghĩa nếu có argument rằng phản hồi (response / 응답) thực sự phản ánh construct cần đo trong population và mục đích cụ thể.

Ví dụ, một quy mô (scale / 규모) tên “xã hội (social / 사회적) anxiety” nhưng chủ yếu hỏi mức thích đi party có thể lẫn lo âu xã hội với hướng nội. Một instrument có giao diện chuyên nghiệp không tự trở thành psychological measure tốt.

Chuỗi suy luận (inference / 추론) là:

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

Trước khi viết item, cần xác định construct gồm gì và không gồm gì. **Độ giá trị nội dung (content validity)** hỏi các indicator có phủ đủ lĩnh vực (domain / 도메인) hay không.

Nếu đo burnout nhưng chỉ hỏi tiredness, instrument có thể bỏ cynicism hoặc occupational ngữ cảnh (context / 맥락). Nếu đo intelligence nhưng chỉ dùng vocabulary, score có thể phản ánh schooling và ngôn ngữ (language / 언어) exposure nhiều hơn lĩnh vực (domain / 도메인) mong muốn.

Content ánh xạ (mapping / 매핑), expert rà soát (review / 검토) và cognitive interviewing thường hữu ích để kiểm tra item có được hiểu đúng như dự định hay không.

## 3. Classical kiểm thử (test / 테스트) lý thuyết (theory / 이론)

Trong **Classical kiểm thử (test / 테스트) lý thuyết (theory / 이론) (CTT)**:

\[
X = T + E
\]

`X` là observed score, `T` là true score theo mô hình (model / 모델) và `E` là sai số đo lường (measurement error / 측정 오차). True score ở đây là expected score qua repeated equivalent đo lường (measurement / 측정), không phải “giá trị thật tuyệt đối” của person.

CTT hữu ích để lập luận (reasoning / 추론) về độ tin cậy (reliability / 신뢰성) ở kiểm thử (test / 테스트) mức (level / 수준), nhưng precision có thể khác nhau giữa trait levels và item sets; đây là một lý do IRT được phát triển.

## 4. độ tin cậy (reliability / 신뢰성) là consistency cho một use trường hợp (case / 사례)

### Nội bộ (internal / 내부) consistency

Nội bộ (internal / 내부) consistency hỏi các item có covary đủ để hỗ trợ (support / 지원) interpretation composite score không. Cronbach's alpha phổ biến nhưng **alpha cao không chứng minh unidimensionality**. Alpha còn tăng khi item redundant.

Trong nhiều trường hợp, omega hoặc model-based độ tin cậy (reliability / 신뢰성) có các giả định (assumptions / 가정들) phù hợp hơn, nhưng không có một coefficient “tốt nhất cho mọi kiểm thử (test / 테스트)”. độ tin cậy (reliability / 신뢰성) phải gắn với mô hình (model / 모델) và mục đích sử dụng.

### Kiểm thử (test / 테스트)–retest

Kiểm thử (test / 테스트)–retest độ tin cậy (reliability / 신뢰성) hỏi score có ổn định qua thời gian khi construct được kỳ vọng ổn định hay không. Với trạng thái (state / 상태) thay đổi nhanh như mood trong ngày, kiểm thử (test / 테스트)–retest thấp không nhất thiết là lỗi đo lường (measurement / 측정).

### Inter-rater độ tin cậy (reliability / 신뢰성)

Khi clinician hoặc coder đánh giá hành vi (behavior / 동작), agreement giữa raters quan trọng. Rubric, huấn luyện (training / 학습) và blinding có thể giảm drift nhưng không loại bỏ hoàn toàn subjectivity.

## 5. Validity là argument về interpretation và use

Không nên nói “kiểm thử (test / 테스트) này valid” như một thuộc tính bất biến. Cách diễn đạt tốt hơn là: **bằng chứng (evidence / 증거) hiện có hỗ trợ tới mức nào cho interpretation score này, trong population này, cho use này?**

Validity bằng chứng (evidence / 증거) thường bao gồm:

- content;
- phản hồi (response / 응답) tiến trình (process / 프로세스);
- nội bộ (internal / 내부) cấu trúc (structure / 구조);
- quan hệ (relation / 관계) with other variables;
- consequences và fairness của use.

**Convergent bằng chứng (evidence / 증거)** hỏi measure có quan hệ hợp lý với construct gần không. **Discriminant bằng chứng (evidence / 증거)** hỏi nó có đủ khác construct lân cận không. **Predictive/criterion bằng chứng (evidence / 증거)** hỏi score có liên hệ với kết quả (outcome / 결과) hoặc criterion liên quan không.

Structural validity chỉ là một phần. Factor mô hình (model / 모델) đẹp không tự chứng minh bên ngoài (external / 외부) validity.

## 6. Factor phân tích (analysis / 분석) không “phát hiện các phần của não”

**Exploratory Factor phân tích (analysis / 분석) (EFA)** tìm latent cấu trúc (structure / 구조) có thể giải thích covariance giữa items. **Confirmatory Factor phân tích (analysis / 분석) (CFA)** kiểm tra cấu trúc (structure / 구조) được hypothesize trước.

Factors là statistical constructs. Chúng không tự động là natural kinds hoặc distinct neural các hệ thống (systems / 시스템들). kết quả (result / 결과) phụ thuộc item pool, estimator, rotation, mẫu (sample / 표본) và mô hình (model / 모델) specification.

Một quy mô (scale / 규모) có thể fit one-factor mô hình (model / 모델) trong mẫu (sample / 표본) này nhưng two-factor mô hình (model / 모델) trong mẫu (sample / 표본) khác. Điều đó không nên bị che bằng một chỉ số fit duy nhất.

## 7. đo lường (measurement / 측정) invariance và so sánh group

Khi so sánh Vietnamese, Korean và English samples, literal translation chưa đủ. **Tính bất biến đo lường (measurement invariance)** kiểm tra đo lường (measurement / 측정) relations có đủ tương đương để hỗ trợ (support / 지원) comparison hay không.

Các bước thường được mô tả như:

- configural invariance: cấu trúc (structure / 구조) cơ bản tương tự;
- chỉ số (metric / 지표) invariance: factor loadings đủ tương đương để so quan hệ;
- scalar invariance: intercept/threshold đủ tương đương để so latent means theo mô hình (model / 모델).

Đây là modeling khung phần mềm (framework / 프레임워크), không phải checklist tuyệt đối. Partial invariance, alignment hoặc item-level investigation có thể phù hợp tùy dữ liệu và mục tiêu.

## 8. Differential Item Functioning

**Hoạt động khác biệt của item (Differential Item Functioning — DIF)** xảy ra khi people có cùng latent trait nhưng xác suất trả lời item khác nhau theo group.

Ví dụ item “tôi thường nói thẳng khi không đồng ý với cấp trên” có thể phản ánh assertiveness nhưng cũng chịu power-distance norm. Nếu DIF mạnh, group difference có thể đến từ item functioning chứ không hoàn toàn từ latent construct.

## 9. Item phản hồi (response / 응답) lý thuyết (theory / 이론)

**Item phản hồi (response / 응답) lý thuyết (theory / 이론) (IRT)** mô hình (model / 모델) xác suất (probability / 확률) của phản hồi (response / 응답) dựa trên latent trait và item parameters. Trong mô hình (model / 모델) phổ biến, item có thể khác về difficulty và discrimination; một số mô hình (model / 모델) còn thêm guessing hoặc threshold parameters.

IRT cho phép precision thay đổi theo trait mức (level / 수준). Computerized adaptive testing có thể chọn item informative hơn quanh hiện tại (current / 현재) estimate, giảm số item cần dùng.

> **hiện tại (current / 현재) lý thuyết (theory / 이론)/mô hình (model / 모델):** IRT là họ đo lường (measurement / 측정) các mô hình (models / 모델들) rất mạnh, nhưng suy luận (inference / 추론) phụ thuộc unidimensionality/local-independence các giả định (assumptions / 가정들) và mô hình (model / 모델) fit. Không nên dùng “IRT-based” như nhãn chất lượng nếu các giả định (assumptions / 가정들) không được kiểm tra.

## 10. Norms và tham chiếu (reference / 참조) group

Raw score thường không tự có nghĩa. Percentile hoặc standardized score phụ thuộc **nhóm chuẩn (normative sample)**.

Percentile 90 nghĩa person đứng khoảng 90th percentile so với tham chiếu (reference / 참조) group, không có nghĩa “90% khả năng” hay “đúng 90%”. Norm cũ, population khác hoặc sampling không đại diện có thể làm interpretation sai.

## 11. Screening khác diagnosis

Screening thường ưu tiên phát hiện người có khả năng cần assessment thêm. Nó không thay clinical interview, lịch sử (history / 이력), impairment, differential diagnosis và medical evaluation.

### Sensitivity và specificity

**Độ nhạy (sensitivity)** là tỷ lệ cases thật được phát hiện. **Độ đặc hiệu (specificity)** là tỷ lệ non-cases được loại đúng.

Threshold thường tạo sự đánh đổi (trade-off / 트레이드오프): tăng sensitivity có thể làm false positives tăng.

### Predictive giá trị (value / 값) và cơ sở (base / 기반) tỷ lệ (rate / 비율)

**Positive predictive giá trị (value / 값)** và **negative predictive giá trị (value / 값)** phụ thuộc prevalence/cơ sở (base / 기반) tỷ lệ (rate / 비율). Một kiểm thử (test / 테스트) có sensitivity và specificity cao vẫn có thể tạo nhiều false positive khi điều kiện (condition / 조건) rất hiếm.

Đây là ứng dụng trực tiếp của Bayesian lập luận (reasoning / 추론).

## 12. Fairness không chỉ là “cùng một kiểm thử (test / 테스트) cho mọi người”

Fairness liên quan truy cập (access / 접근), ngôn ngữ (language / 언어), disability accommodation, item độ lệch (bias / 편향), norming, consequences và whether score interpretation is comparable.

Cùng procedure cho mọi người có thể không công bằng nếu một group bị đo lường (measurement / 측정) barrier không liên quan construct, ví dụ hearing impairment khi kiểm thử (test / 테스트) không có accommodation phù hợp.

## 13. Cross-cultural adaptation

Dịch quy mô (scale / 규모) tốt thường gồm nhiều bước: forward translation, reconciliation, back translation, expert rà soát (review / 검토), cognitive interviewing và psychometric evaluation ở population đích.

Một câu literal-equivalent vẫn có thể cultural-non-equivalent. “Family obligation”, “assertiveness” hay “independence” có meaning khác nhau giữa ngữ cảnh (context / 맥락).

## 14. kiểm thử (test / 테스트) classification và internet psychology

Online personality quiz thường biến continuous traits thành nhị phân (binary / 이진) categories để dễ hiểu. Điều này có thể có entertainment giá trị (value / 값) nhưng không tự mang psychometric validity.

MBTI chịu ảnh hưởng historical từ Jung nhưng không phải bằng chứng cho Jungian typology; hiện đại (modern / 현대적) personality science thường ưu tiên dimensional trait các mô hình (models / 모델들). Xem [[../03_human_development_and_person/03_personality]] và [[../90_connections/06_historical_theories_and_modern_evidence_matrix]].

## 15. đo lường (measurement / 측정) reporting và replication

Replication chỉ hữu ích nếu measure được mô tả đủ rõ và hoạt động tương tự trong mẫu (sample / 표본) mới. Nếu original study không báo độ tin cậy (reliability / 신뢰성), scoring, item wording hoặc validity bằng chứng (evidence / 증거), apparent replication thất bại (failure / 실패) có thể partly là đo lường (measurement / 측정) thất bại (failure / 실패).

Do đó transparency về instrument là một phần của reproducibility, không phải appendix kỹ thuật.

Xem [[09_replication_meta_analysis_and_bayesian_reasoning]].

## 16. Mức bằng chứng

### Established bằng chứng (evidence / 증거)

Phần này gom các nguyên tắc đo lường đã có nền tảng tương đối chắc: reliability, validity, norms và measurement error. Hãy đọc chúng như điều kiện để diễn giải score, không như bảo đảm test luôn đúng.

- observed score luôn cần được hiểu qua measurement error;
- reliability không đồng nghĩa validity;
- validity support phải gắn interpretation/use;
- base rate ảnh hưởng predictive value;
- group comparison cần evidence về comparability của measurement.

### Hiện tại (current / 현재) các mô hình (models / 모델들)

CTT, CFA/SEM, IRT, generalizability lý thuyết (theory / 이론) và Bayesian psychometrics là mô hình (model / 모델) families hiện hành. Chúng không phải competing religions; mỗi mô hình (model / 모델) trả lời questions khác nhau dưới các giả định (assumptions / 가정들) khác nhau.

### Debated/conditional issues

Cutoff “độ tin cậy (reliability / 신뢰성) đủ tốt”, fit-index thresholds, mức invariance tối thiểu, choice giữa factor các mô hình (models / 모델들) và treatment của ordinal dữ liệu (data / 데이터) đều phụ thuộc ngữ cảnh (context / 맥락). Rule-of-thumb không nên được dùng như scientific law.

## 17. Những hiểu lầm phổ biến

**“Cronbach's alpha > .90 nghĩa kiểm thử (test / 테스트) rất tốt.”** Sai. Alpha có thể cao vì item redundant và không chứng minh construct validity.

**“Factor phân tích (analysis / 분석) tìm ra các loại người tự nhiên.”** Không nhất thiết. Factor mô hình (model / 모델) mô tả covariance cấu trúc (structure / 구조).

**“Một cutoff tạo ra hai nhóm thật trong tự nhiên.”** Nhiều traits continuous; threshold thường phục vụ quyết định (decision / 결정) quy tắc (rule / 규칙).

**“Một kiểm thử (test / 테스트) đã được publish thì dùng ở population nào cũng được.”** Không đúng. Interpretation cần bằng chứng (evidence / 증거) ở ngữ cảnh (context / 맥락) liên quan.

## 18. mô hình tư duy (mental model / 사고 모델)

Mental model này đi từ construct tới item, score, uncertainty và quyết định. Nó giúp người đọc hỏi đúng: test đang đo gì, sai số ở đâu và kết luận nào vượt quá dữ liệu.

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

Một score chỉ mạnh bằng weakest link trong suy luận (inference / 추론) chuỗi (chain / 사슬).

## Kết nối kiến thức

Đọc cùng [[03_measurement_statistics]], [[06_open_science_and_evidence_evaluation]], [[09_replication_meta_analysis_and_bayesian_reasoning]], [[../02_learning_and_cognition/03_intelligence_and_cognitive_differences]], [[../03_human_development_and_person/03_personality]] và [[../04_mental_health/01_assessment_and_diagnosis]].

### Nguồn định hướng

Các nguồn định hướng giúp đối chiếu psychometric claim, fairness và cách diễn giải test. Hãy ưu tiên tài liệu nêu rõ population, reliability và validity evidence.

- *Standards for Educational and Psychological Testing* — AERA, APA, NCME.
- Best-practice guidelines hiện đại về quy mô (scale / 규모) development/kiểm tra hợp lệ (validation / 검증) trong psychological và behavioral sciences.
- Nghiên cứu replication gần đây nhấn mạnh đo lường (measurement / 측정) reporting, độ tin cậy (reliability / 신뢰성), validity và invariance là một phần của reproducibility.

> **Bàn giao:** Sau **Nguồn định hướng**, hãy chốt bất biến (invariant / 불변식) và giới hạn của mục này trước khi nối sang kiến thức kế tiếp. Có thể đọc tiếp [00 psychology as science](./00_psychology_as_science.md) để đối chiếu ranh giới (boundary / 경계) gần nhất.
