# Tư duy, suy luận và ra quyết định

Tư duy không chỉ là “suy nghĩ nhiều”. Nó là quá trình tạo, duy trì và biến đổi **biểu diễn tinh thần (mental representation)** để hiểu vấn đề, suy luận, dự đoán và lựa chọn hành động. Chất lượng của quyết định phụ thuộc không chỉ vào logic ở bước cuối mà còn vào cách vấn đề được biểu diễn, dữ liệu nào được chú ý và giả thuyết nào được đưa vào ngay từ đầu.

> **Trạng thái bằng chứng tổng quát:** giới hạn của reasoning, vai trò của biểu diễn vấn đề, heuristic, base rate, framing và metacognition có support thực nghiệm rộng. Các model cụ thể như dual-process, predictive accounts hay một số decomposition của reasoning là **current theories**, hữu ích nhưng không nên được hiểu như “hai bộ não” hay kiến trúc cuối cùng.

Xem [[../EVIDENCE_STATUS_GUIDE]], [[04_cognitive_biases_and_metacognition]] và [[08_decision_under_risk_uncertainty_and_ambiguity]].

## 1. Biểu diễn vấn đề quyết định không gian lời giải

Một báo cáo lỗi “ứng dụng chậm” tạo không gian tìm kiếm rất rộng. Khi được viết lại thành “độ trễ chỉ tăng ở API X sau khi số bản ghi vượt N, CPU bình thường nhưng I/O database tăng”, search space thu hẹp rõ.

Trong psychology, thay đổi cách mô tả một problem để lộ structure mới thường được gọi là **tái cấu trúc (restructuring)**.

Điều này cho thấy đôi khi reasoning thất bại không phải vì thiếu “thông minh” mà vì representation ban đầu sai hoặc quá mơ hồ.

## 2. Khái niệm, category và schema

Con người nén kinh nghiệm thành **khái niệm (concept)** và **danh mục (category)**. Một **prototype** là ví dụ điển hình; một **schema** là cấu trúc kiến thức giúp dự đoán điều thường xảy ra trong context nhất định.

Schema giảm tải nhận thức nhưng cũng tạo blind spot. Developer quen relational database có thể tự động frame mọi persistence problem thành table/join problem dù event stream hay graph model phù hợp hơn.

Schema là công cụ nén và dự đoán, không phải định nghĩa tuyệt đối của reality.

## 3. Deduction và induction

**Suy diễn (deduction)** hỏi kết luận có bắt buộc đúng khi premise đúng hay không. **Quy nạp (induction)** đi từ số quan sát hữu hạn tới kết luận rộng hơn, vì vậy luôn chứa uncertainty.

Phần lớn decision đời thực là inductive. Ta không có complete information và phải đánh giá probability, cost của error và quality của evidence.

## 4. Base rate và diagnostic evidence

Một evidence nổi bật không có giá trị độc lập với prior probability.

Nếu một test có false-positive rate đáng kể trong population nơi condition rất hiếm, positive result chưa chắc đồng nghĩa xác suất mắc condition cao.

**Bỏ qua tỷ lệ nền (base-rate neglect)** xảy ra khi người ta overweight case-specific cue và underweight prevalence hoặc prior.

Xem [[../00_foundations/09_replication_meta_analysis_and_bayesian_reasoning]].

## 5. Bayesian reasoning như mô hình cập nhật

Bayes có thể viết:

\[
P(H\mid E)=\frac{P(E\mid H)P(H)}{P(E)}
\]

Ý nghĩa thực hành là:

```text
prior belief
+ diagnostic value of new evidence
→ posterior belief
```

Trong debugging, một cause phổ biến có prior cao, nhưng log có likelihood ratio mạnh cho hypothesis khác có thể đảo ranking.

Bayesian reasoning không yêu cầu “tin prior mù quáng”; prior phải được update khi data mới xuất hiện.

## 6. Bounded rationality

Con người không có thời gian, attention hay computational resource vô hạn. **Tính duy lý giới hạn (bounded rationality)** mô tả decision dưới resource constraint.

Vì vậy heuristic không mặc định là lỗi. Một strategy đơn giản có thể rất hiệu quả nếu cue–environment relation ổn định.

Bias xuất hiện khi shortcut dùng cue không còn diagnostic cho target.

## 7. Heuristics

**Availability** dùng ease of retrieval như cue cho frequency/risk. **Representativeness** dùng similarity với prototype. **Anchoring** làm estimate bị kéo về giá trị ban đầu.

Các effect này có evidence tốt ở nhiều laboratory setting, nhưng magnitude phụ thuộc task, wording, experience và context.

Không nên dùng label bias để giải thích hậu nghiệm mọi decision mình không đồng ý.

## 8. Dual-process models

Các model hai quá trình phân biệt processing nhanh/tự động và processing chậm/có kiểm soát.

> **Current theory:** distinction này hữu ích cho nhiều hiện tượng, nhưng “System 1” và “System 2” không phải hai brain module độc lập. Nhiều process nằm trên continuum và có thể tương tác.

Khi mệt hoặc time pressure cao, reliance vào default/habit thường tăng, nhưng effect không universal cho mọi task.

## 9. Reasoning environment quan trọng hơn lời nhắc “hãy suy nghĩ kỹ”

Decision quality có thể được cải thiện bằng process design: independent estimate trước discussion, checklist, reference class, pre-mortem, delay với high-stake choice và requirement nêu hypothesis cạnh tranh.

Những tool này hoạt động bằng cách thay information flow và reducing bias opportunity, không phải bằng cách làm con người “ít thiên kiến” vĩnh viễn.

## 10. Ngôn ngữ ảnh hưởng cognition nhưng không quyết định toàn bộ thought

Phiên bản mạnh của **tính tương đối ngôn ngữ (linguistic relativity)** cho rằng language quyết định hoàn toàn khả năng suy nghĩ không được modern evidence support rộng.

Phiên bản yếu hơn hợp lý hơn: language categories có thể bias attention, memory hoặc discrimination trong một số task.

Language là cognitive tool mạnh, nhưng cognition không bị khóa hoàn toàn vào vocabulary hoặc grammar.

## 11. Framing

Cùng một quantitative outcome có thể tạo preference khác khi được frame dưới dạng gain hoặc loss.

> **Established effect with boundary:** framing effect được replicate trong nhiều paradigm, nhưng magnitude phụ thuộc population, task, numeracy và wording. Không phải mọi người luôn “sợ loss hơn gain” trong mọi domain.

## 12. Prospect theory

**Lý thuyết triển vọng (prospect theory)** mô tả choice relative to reference point, diminishing sensitivity và nonlinear probability weighting.

Nó là một model có strong empirical influence, nhưng parameter không phải constants universal của human nature.

Xem [[08_decision_under_risk_uncertainty_and_ambiguity]].

## 13. Decision under ambiguity

**Risk** thường ngụ ý probability tương đối xác định; **ambiguity** xuất hiện khi probability model itself không rõ.

Con người thường xử lý ambiguity khác risk, nhưng preference thay đổi theo domain, expertise và framing.

Trong product planning hoặc investing, nhiều situation là ambiguity hơn risk thuần túy vì distribution tương lai chưa biết tốt.

## 14. Metacognition

**Siêu nhận thức (metacognition)** là khả năng monitor và control chính cognition của mình.

Một dimension quan trọng là **calibration** giữa confidence và accuracy. Người có confidence thấp nhưng phân biệt đúng trial nào mình biết/không biết vẫn có metacognitive sensitivity tốt.

Confidence vì vậy không nên được đọc như direct measure của truth.

Xem [[04_cognitive_biases_and_metacognition]].

## 15. Hindsight và outcome bias

Sau khi outcome đã biết, past evidence trông obvious hơn. **Hindsight bias** làm ta underestimate uncertainty trước event.

**Outcome bias** đánh giá decision quality dựa quá nhiều vào result cuối. Nhưng good process có thể unlucky và bad process có thể lucky.

Decision log ghi prediction, probability và rationale trước outcome giúp giữ historical uncertainty.

## 16. Creativity và restructuring

Problem solving đôi khi cần mở search space trước khi thu hẹp. **Tư duy phân kỳ (divergent thinking)** tạo alternatives; evaluation sau đó dùng constraint và evidence để chọn.

Creativity không đối lập reasoning. Good creative solution vẫn cần validation.

Xem [[06_expertise_creativity_and_problem_solving]].

## 17. Team decision

Group có thể aggregate diverse information, nhưng cũng có thể amplify shared bias.

Authority, status và early confident speaker ảnh hưởng discussion. Independent estimate trước meeting và structured dissent có thể giảm informational cascade.

Xem [[../03_human_development_and_person/10_group_dynamics_collective_behavior_and_cooperation]] và [[../06_applied/20_negotiation_conflict_and_joint_decision_making]].

## 18. AI-assisted reasoning

AI có thể mở rộng option generation, summarize data và reduce search cost. Nhưng fluent output tạo risk **automation bias** và **verification debt**.

Human–AI system tốt cần tách:

```text
generate candidate
→ verify evidence
→ compare alternatives
→ retain human responsibility
```

Short-term performance với tool không đồng nghĩa internal reasoning skill đã tăng.

Xem [[10_cognitive_offloading_external_memory_and_extended_cognition]] và [[../90_connections/02_human_ai_collaboration_trust_and_cognitive_offloading]].

## 19. Common misconceptions

**“Logic tốt là đủ để quyết định tốt.”** Không. Input, representation và uncertainty matter.

**“Heuristic = irrational.”** Không. Heuristic có thể adaptive trong environment phù hợp.

**“System 1/System 2 là hai vùng não.”** Không.

**“Biết bias giúp miễn nhiễm bias.”** Không. Procedure và feedback thường quan trọng hơn awareness.

**“Confidence cao nghĩa probability đúng cao.”** Chỉ khi confidence được calibrated trong domain và procedure phù hợp.

## 20. Mental model

```text
Attention
   ↓
Problem representation
   ↓
Hypotheses / options
   ↓
Evidence + prior + constraints
   ↓
Choice
   ↓
Outcome
   ↓
Feedback / model update
```

Reasoning tốt không phải cố loại bỏ mọi heuristic. Nó là biết khi nào shortcut đủ tốt và khi nào stakes/uncertainty đòi hỏi procedure chặt hơn.

## Kết nối kiến thức

Đọc cùng [[04_cognitive_biases_and_metacognition]], [[05_language_social_cognition_and_theory_of_mind]], [[06_expertise_creativity_and_problem_solving]], [[08_decision_under_risk_uncertainty_and_ambiguity]], [[../00_foundations/08_causal_inference_and_psychological_evidence]] và [[../06_applied/18_financial_psychology_and_personal_decision_making]].