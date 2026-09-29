# Tư duy, suy luận và ra quyết định

> **Mạch đọc:** Đọc **Tư duy, suy luận và ra quyết định** như một mắt xích của lộ trình học (learning path / 학습 경로) hiện tại, không như một ghi chú tách rời. Nội dung đi từ **1. Biểu diễn vấn đề quyết định không gian lời giải** sang **2. Khái niệm, category và lược đồ (schema / 스키마)**; điểm nối này chuẩn bị câu hỏi cho các mục sau thay vì dừng ở định nghĩa đầu tiên.


Tư duy không chỉ là “suy nghĩ nhiều”. Nó là quá trình tạo, duy trì và biến đổi **biểu diễn tinh thần (mental representation)** để hiểu vấn đề, suy luận, dự đoán và lựa chọn hành động. Chất lượng của quyết định phụ thuộc không chỉ vào lô-gic (logic / 논리) ở bước cuối mà còn vào cách vấn đề được biểu diễn, dữ liệu nào được chú ý và giả thuyết nào được đưa vào ngay từ đầu.

> **Trạng thái bằng chứng tổng quát:** giới hạn của lập luận (reasoning / 추론), vai trò của biểu diễn vấn đề, heuristic, cơ sở (base / 기반) tỷ lệ (rate / 비율), framing và metacognition có hỗ trợ (support / 지원) thực nghiệm rộng. Các mô hình (model / 모델) cụ thể như dual-process, predictive accounts hay một số decomposition của lập luận (reasoning / 추론) là **hiện tại (current / 현재) theories**, hữu ích nhưng không nên được hiểu như “hai bộ não” hay kiến trúc cuối cùng.

Xem [[../EVIDENCE_STATUS_GUIDE]], [[04_cognitive_biases_and_metacognition]] và [[08_decision_under_risk_uncertainty_and_ambiguity]].

## 1. Biểu diễn vấn đề quyết định không gian lời giải

Một báo cáo lỗi “ứng dụng chậm” tạo không gian tìm kiếm rất rộng. Khi được viết lại thành “độ trễ chỉ tăng ở API X sau khi số bản ghi vượt N, CPU bình thường nhưng I/O cơ sở dữ liệu (database / 데이터베이스) tăng”, tìm kiếm (search / 검색) không gian (space / 공간) thu hẹp rõ.

Trong psychology, thay đổi cách mô tả một bài toán (problem / 문제) để lộ cấu trúc (structure / 구조) mới thường được gọi là **tái cấu trúc (restructuring)**.

Điều này cho thấy đôi khi lập luận (reasoning / 추론) thất bại không phải vì thiếu “thông minh” mà vì biểu diễn (representation / 표현) ban đầu sai hoặc quá mơ hồ.

## 2. Khái niệm, category và lược đồ (schema / 스키마)

Con người nén kinh nghiệm thành **khái niệm (concept)** và **danh mục (category)**. Một **prototype** là ví dụ điển hình; một **lược đồ (schema / 스키마)** là cấu trúc kiến thức giúp dự đoán điều thường xảy ra trong ngữ cảnh (context / 맥락) nhất định.

Lược đồ (schema / 스키마) giảm tải nhận thức nhưng cũng tạo blind spot. nhà phát triển (developer / 개발자) quen relational cơ sở dữ liệu (database / 데이터베이스) có thể tự động frame mọi persistence bài toán (problem / 문제) thành bảng (table / 테이블)/phép nối (join / 조인) bài toán (problem / 문제) dù sự kiện (event / 이벤트) stream hay đồ thị (graph / 그래프) mô hình (model / 모델) phù hợp hơn.

Lược đồ (schema / 스키마) là công cụ nén và dự đoán, không phải định nghĩa tuyệt đối của reality.

## 3. Deduction và induction

**Suy diễn (deduction)** hỏi kết luận có bắt buộc đúng khi premise đúng hay không. **Quy nạp (induction)** đi từ số quan sát hữu hạn tới kết luận rộng hơn, vì vậy luôn chứa bất định (uncertainty / 불확실성).

Phần lớn quyết định (decision / 결정) đời thực là inductive. Ta không có complete thông tin (information / 정보) và phải đánh giá xác suất (probability / 확률), chi phí (cost / 비용) của lỗi (error / 오류) và chất lượng (quality / 품질) của bằng chứng (evidence / 증거).

## 4. cơ sở (base / 기반) tỷ lệ (rate / 비율) và diagnostic bằng chứng (evidence / 증거)

Một bằng chứng (evidence / 증거) nổi bật không có giá trị độc lập với prior xác suất (probability / 확률).

Nếu một kiểm thử (test / 테스트) có false-positive tỷ lệ (rate / 비율) đáng kể trong population nơi điều kiện (condition / 조건) rất hiếm, positive kết quả (result / 결과) chưa chắc đồng nghĩa xác suất mắc điều kiện (condition / 조건) cao.

**Bỏ qua tỷ lệ nền (base-rate neglect)** xảy ra khi người ta overweight case-specific cue và underweight prevalence hoặc prior.

Xem [[../00_foundations/09_replication_meta_analysis_and_bayesian_reasoning]].

## 5. Bayesian lập luận (reasoning / 추론) như mô hình cập nhật

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

Bayesian lập luận (reasoning / 추론) không yêu cầu “tin prior mù quáng”; prior phải được cập nhật (update / 업데이트) khi dữ liệu (data / 데이터) mới xuất hiện.

## 6. Bounded rationality

Con người không có thời gian, attention hay computational tài nguyên (resource / 자원) vô hạn. **Tính duy lý giới hạn (bounded rationality)** mô tả quyết định (decision / 결정) dưới tài nguyên (resource / 자원) ràng buộc (constraint / 제약조건).

Vì vậy heuristic không mặc định là lỗi. Một chiến lược (strategy / 전략) đơn giản có thể rất hiệu quả nếu cue–môi trường (environment / 환경) quan hệ (relation / 관계) ổn định.

Độ lệch (bias / 편향) xuất hiện khi shortcut dùng cue không còn diagnostic cho mục tiêu (target / 대상).

## 7. Heuristics

**Availability** dùng ease of retrieval như cue cho frequency/rủi ro (risk / 위험). **Representativeness** dùng similarity với prototype. **Anchoring** làm estimate bị kéo về giá trị ban đầu.

Các tác động (effect / 효과) này có bằng chứng (evidence / 증거) tốt ở nhiều laboratory setting, nhưng magnitude phụ thuộc tác vụ (task / 작업), wording, experience và ngữ cảnh (context / 맥락).

Không nên dùng label độ lệch (bias / 편향) để giải thích hậu nghiệm mọi quyết định (decision / 결정) mình không đồng ý.

## 8. Dual-process các mô hình (models / 모델들)

Các mô hình (model / 모델) hai quá trình phân biệt processing nhanh/tự động và processing chậm/có kiểm soát.

> **hiện tại (current / 현재) lý thuyết (theory / 이론):** distinction này hữu ích cho nhiều hiện tượng, nhưng “hệ thống (system / 시스템) 1” và “hệ thống (system / 시스템) 2” không phải hai brain mô-đun (module / 모듈) độc lập. Nhiều tiến trình (process / 프로세스) nằm trên continuum và có thể tương tác.

Khi mệt hoặc thời gian (time / 시간) pressure cao, reliance vào default/habit thường tăng, nhưng tác động (effect / 효과) không universal cho mọi tác vụ (task / 작업).

## 9. lập luận (reasoning / 추론) môi trường (environment / 환경) quan trọng hơn lời nhắc “hãy suy nghĩ kỹ”

Quyết định (decision / 결정) chất lượng (quality / 품질) có thể được cải thiện bằng tiến trình (process / 프로세스) thiết kế (design / 설계): independent estimate trước discussion, checklist, tham chiếu (reference / 참조) lớp (class / 클래스), pre-mortem, delay với high-stake choice và yêu cầu (requirement / 요구사항) nêu hypothesis cạnh tranh.

Những công cụ (tool / 도구) này hoạt động bằng cách thay thông tin (information / 정보) luồng (flow / 흐름) và reducing độ lệch (bias / 편향) opportunity, không phải bằng cách làm con người “ít thiên kiến” vĩnh viễn.

## 10. Ngôn ngữ ảnh hưởng cognition nhưng không quyết định toàn bộ thought

Phiên bản mạnh của **tính tương đối ngôn ngữ (linguistic relativity)** cho rằng ngôn ngữ (language / 언어) quyết định hoàn toàn khả năng suy nghĩ không được hiện đại (modern / 현대적) bằng chứng (evidence / 증거) hỗ trợ (support / 지원) rộng.

Phiên bản yếu hơn hợp lý hơn: ngôn ngữ (language / 언어) categories có thể độ lệch (bias / 편향) attention, bộ nhớ (memory / 메모리) hoặc discrimination trong một số tác vụ (task / 작업).

Ngôn ngữ (language / 언어) là cognitive công cụ (tool / 도구) mạnh, nhưng cognition không bị khóa hoàn toàn vào vocabulary hoặc grammar.

## 11. Framing

Cùng một quantitative kết quả (outcome / 결과) có thể tạo preference khác khi được frame dưới dạng gain hoặc mất mát (loss / 손실).

> **Established tác động (effect / 효과) with ranh giới (boundary / 경계):** framing tác động (effect / 효과) được replicate trong nhiều paradigm, nhưng magnitude phụ thuộc population, tác vụ (task / 작업), numeracy và wording. Không phải mọi người luôn “sợ mất mát (loss / 손실) hơn gain” trong mọi lĩnh vực (domain / 도메인).

## 12. Prospect lý thuyết (theory / 이론)

**Lý thuyết triển vọng (prospect theory)** mô tả choice relative to tham chiếu (reference / 참조) điểm (point / 지점), diminishing sensitivity và nonlinear xác suất (probability / 확률) weighting.

Nó là một mô hình (model / 모델) có strong empirical influence, nhưng parameter không phải constants universal của human nature.

Xem [[08_decision_under_risk_uncertainty_and_ambiguity]].

## 13. quyết định (decision / 결정) under ambiguity

**rủi ro (risk / 위험)** thường ngụ ý xác suất (probability / 확률) tương đối xác định; **ambiguity** xuất hiện khi xác suất (probability / 확률) mô hình (model / 모델) itself không rõ.

Con người thường xử lý ambiguity khác rủi ro (risk / 위험), nhưng preference thay đổi theo lĩnh vực (domain / 도메인), expertise và framing.

Trong sản phẩm (product / 제품) planning hoặc investing, nhiều situation là ambiguity hơn rủi ro (risk / 위험) thuần túy vì phân phối (distribution / 분포) tương lai chưa biết tốt.

## 14. Metacognition

**Siêu nhận thức (metacognition)** là khả năng monitor và điều khiển (control / 제어) chính cognition của mình.

Một dimension quan trọng là **calibration** giữa confidence và accuracy. Người có confidence thấp nhưng phân biệt đúng trial nào mình biết/không biết vẫn có metacognitive sensitivity tốt.

Confidence vì vậy không nên được đọc như direct measure của truth.

Xem [[04_cognitive_biases_and_metacognition]].

## 15. Hindsight và kết quả (outcome / 결과) độ lệch (bias / 편향)

Sau khi kết quả (outcome / 결과) đã biết, past bằng chứng (evidence / 증거) trông obvious hơn. **Hindsight độ lệch (bias / 편향)** làm ta underestimate bất định (uncertainty / 불확실성) trước sự kiện (event / 이벤트).

**kết quả (outcome / 결과) độ lệch (bias / 편향)** đánh giá quyết định (decision / 결정) chất lượng (quality / 품질) dựa quá nhiều vào kết quả (result / 결과) cuối. Nhưng good tiến trình (process / 프로세스) có thể unlucky và bad tiến trình (process / 프로세스) có thể lucky.

Quyết định (decision / 결정) log ghi prediction, xác suất (probability / 확률) và rationale trước kết quả (outcome / 결과) giúp giữ historical bất định (uncertainty / 불확실성).

## 16. Creativity và restructuring

Bài toán (problem / 문제) solving đôi khi cần mở tìm kiếm (search / 검색) không gian (space / 공간) trước khi thu hẹp. **Tư duy phân kỳ (divergent thinking)** tạo alternatives; evaluation sau đó dùng ràng buộc (constraint / 제약조건) và bằng chứng (evidence / 증거) để chọn.

Creativity không đối lập lập luận (reasoning / 추론). Good creative solution vẫn cần kiểm tra hợp lệ (validation / 검증).

Xem [[06_expertise_creativity_and_problem_solving]].

## 17. nhóm (team / 팀) quyết định (decision / 결정)

Group có thể aggregate diverse thông tin (information / 정보), nhưng cũng có thể amplify dùng chung (shared / 공유) độ lệch (bias / 편향).

Authority, status và early confident speaker ảnh hưởng discussion. Independent estimate trước meeting và structured dissent có thể giảm informational cascade.

Xem [[../03_human_development_and_person/10_group_dynamics_collective_behavior_and_cooperation]] và [[../06_applied/20_negotiation_conflict_and_joint_decision_making]].

## 18. AI-assisted lập luận (reasoning / 추론)

AI có thể mở rộng option generation, summarize dữ liệu (data / 데이터) và reduce tìm kiếm (search / 검색) chi phí (cost / 비용). Nhưng fluent đầu ra (output / 출력) tạo rủi ro (risk / 위험) **automation độ lệch (bias / 편향)** và **xác minh (verification / 확인) debt**.

Human–AI hệ thống (system / 시스템) tốt cần tách:

```text
generate candidate
→ verify evidence
→ compare alternatives
→ retain human responsibility
```

Short-term hiệu năng (performance / 성능) với công cụ (tool / 도구) không đồng nghĩa nội bộ (internal / 내부) lập luận (reasoning / 추론) skill đã tăng.

Xem [[10_cognitive_offloading_external_memory_and_extended_cognition]] và [[../90_connections/02_human_ai_collaboration_trust_and_cognitive_offloading]].

## 19. dùng chung (common / 공통) misconceptions

**“lô-gic (logic / 논리) tốt là đủ để quyết định tốt.”** Không. đầu vào (input / 입력), biểu diễn (representation / 표현) và bất định (uncertainty / 불확실성) matter.

**“Heuristic = irrational.”** Không. Heuristic có thể adaptive trong môi trường (environment / 환경) phù hợp.

**“hệ thống (system / 시스템) 1/hệ thống (system / 시스템) 2 là hai vùng não.”** Không.

**“Biết độ lệch (bias / 편향) giúp miễn nhiễm độ lệch (bias / 편향).”** Không. Procedure và phản hồi (feedback / 피드백) thường quan trọng hơn awareness.

**“Confidence cao nghĩa xác suất (probability / 확률) đúng cao.”** Chỉ khi confidence được calibrated trong lĩnh vực (domain / 도메인) và procedure phù hợp.

## 20. mô hình tư duy (mental model / 사고 모델)

Phần này chốt mental model thành một chuỗi có thể dùng lại: bối cảnh → cơ chế → bằng chứng → giới hạn → ứng dụng. Hãy đọc sơ đồ như công cụ suy luận, không như một nhãn kết luận tự động.

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

Lập luận (reasoning / 추론) tốt không phải cố loại bỏ mọi heuristic. Nó là biết khi nào shortcut đủ tốt và khi nào stakes/bất định (uncertainty / 불확실성) đòi hỏi procedure chặt hơn.

## Kết nối kiến thức

Đọc cùng [[04_cognitive_biases_and_metacognition]], [[05_language_social_cognition_and_theory_of_mind]], [[06_expertise_creativity_and_problem_solving]], [[08_decision_under_risk_uncertainty_and_ambiguity]], [[../00_foundations/08_causal_inference_and_psychological_evidence]] và [[../06_applied/18_financial_psychology_and_personal_decision_making]].
