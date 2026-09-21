# Thiên kiến nhận thức và siêu nhận thức

**Thiên kiến nhận thức (cognitive bias)** không có nghĩa con người luôn phi lý. Nó mô tả một pattern sai lệch có hệ thống so với một benchmark như logic, probability, unbiased estimation hoặc long-term goal. Một heuristic có thể tạo bias trong laboratory task nhưng vẫn adaptive trong môi trường khác nếu nó giảm search cost hoặc phản ứng nhanh trước threat.

**Siêu nhận thức (metacognition)** là khả năng theo dõi và điều chỉnh chính quá trình nhận thức của mình: mình biết gì, không biết gì, confidence bao nhiêu, strategy nào đang hiệu quả và khi nào cần đổi strategy.

> **Trạng thái bằng chứng:** con người có systematic biases và confidence có thể lệch khỏi objective performance là bằng chứng tương đối vững. Các computational/neural models giải thích confidence và metacognition là current theories; mechanism cụ thể vẫn đang active research.

Xem [[../EVIDENCE_STATUS_GUIDE]].

## 1. Heuristic: lối tắt có trade-off

**Heuristic** là strategy đơn giản hóa decision khi time, information hoặc computational resource bị giới hạn. Heuristic không tự động “xấu”.

Ví dụ, dùng familiarity để đoán “thứ này có lẽ đúng” thường hiệu quả trong môi trường nơi repeated exposure correlate với validity, nhưng trở nên nguy hiểm khi misinformation được lặp lại có chủ đích.

Cách học bias hữu ích hơn memorizing hundreds of names là hỏi:

```text
Resource limit nào tồn tại?
Cue nào được dùng thay cho target?
Environment nào làm heuristic useful?
Khi nào cue-target relation bị phá?
```

## 2. Confirmation bias

**Thiên kiến xác nhận (confirmation bias)** mô tả tendency tìm, ưu tiên hoặc diễn giải evidence theo belief hiện có.

Một developer tin database là bottleneck có thể chỉ đọc slow-query log và bỏ qua network trace. Mechanism không chỉ là “muốn mình đúng”; current hypothesis làm supporting cues dễ được retrieve hơn và testing strategy có thể asymmetric.

Antidote tốt là **tư duy phản chứng (falsification mindset)**: hỏi observation nào nếu xuất hiện sẽ làm hypothesis yếu đi.

## 3. Hindsight bias

**Thiên kiến nhìn lại (hindsight bias)** làm outcome sau khi xảy ra trông predictable hơn mức nó thực sự từng có.

Trong incident postmortem, biết service đã crash khiến signal trước crash trông “obvious”, dẫn đến unfair blame. Decision log ghi prediction và uncertainty trước outcome giúp chống hindsight reconstruction.

## 4. Availability heuristic

**Heuristic sẵn có (availability heuristic)** dùng ease of retrieval như cue cho probability hoặc frequency.

Một dramatic plane accident dễ nhớ hơn ordinary car crash, khiến subjective risk lệch. Trong work, một production incident mới xảy ra có thể làm team overestimate probability của same failure và neglect less salient risks.

## 5. Representativeness và base-rate neglect

**Representativeness** dùng similarity với prototype để judge probability. Nếu description “rất logic, ít nói, thích debugging” giống stereotype developer, người ta có thể ignore base rate của occupations trong population.

**Bỏ qua tần suất nền (base-rate neglect)** là fail to incorporate prior probability. Bayesian reasoning giúp formalize tại sao evidence strength phải được đọc cùng prior prevalence.

Xem [[../00_foundations/09_replication_meta_analysis_and_bayesian_reasoning]].

## 6. Anchoring

**Hiệu ứng neo (anchoring)** xảy ra khi initial number/value ảnh hưởng estimate sau đó, kể cả khi anchor arbitrary hoặc weakly relevant.

Salary negotiation, property price và effort estimation đều có thể bị anchor. Debias không đơn giản là “biết anchor tồn tại”; cần independent estimate, reference class hoặc range trước khi exposure nếu possible.

## 7. Framing effect

Cùng outcome có thể tạo preference khác khi frame bằng gain hay loss. Framing không chứng minh con người “không rational” theo mọi definition; nó cho thấy representation của choice influence value construction.

Application phải thận trọng vì framing effect magnitude phụ thuộc domain, wording, stakes và population.

## 8. Loss aversion và prospect theory

**Prospect theory** mô tả decision relative to reference point, diminishing sensitivity và loss aversion trong nhiều risky-choice settings.

> **Trạng thái bằng chứng:** reference-dependent choice và nonlinear probability weighting có substantial empirical support; exact parameters và universality across domains/individuals là model-dependent, không phải fixed psychological constants.

Xem [[08_decision_under_risk_uncertainty_and_ambiguity]].

## 9. Sunk cost

**Hiệu ứng chi phí chìm (sunk-cost effect)** là tendency tiếp tục vì đã đầu tư trước đó dù future expected value không support tiếp tục.

Không phải mọi persistence sau investment là bias; past investment có thể chứa information về hidden benefit hoặc switching cost. Chỉ gọi sunk-cost bias khi past irrecoverable cost influence decision beyond relevant future consequences.

## 10. Overconfidence có nhiều dạng

“Overconfidence” không phải một phenomenon duy nhất.

- **Overestimation**: nghĩ performance mình cao hơn thực tế.
- **Overplacement**: nghĩ mình tốt hơn others quá mức.
- **Overprecision**: confidence interval quá hẹp.

Tách các dạng này quan trọng vì mechanism và intervention khác nhau.

## 11. Metacognitive monitoring

**Metacognitive monitoring** đánh giá state hiện tại: “tôi có nhớ không?”, “confidence bao nhiêu?”, “tôi có hiểu explanation này không?”.

Research hiện đại thường đo **metacognitive sensitivity**: confidence có phân biệt correct vs incorrect trials tốt đến đâu. Một người có overall confidence thấp nhưng sensitivity tốt vẫn có insight; ngược lại, confidence cao không đồng nghĩa monitoring tốt.

> **Current theory:** confidence được xem như inference từ evidence về task, uncertainty và self-model. Các computational models khác nhau tranh luận signal nào được dùng và ở stage nào.

## 12. Calibration

**Hiệu chỉnh (calibration)** hỏi confidence có match empirical accuracy không.

Nếu người học nói “90% chắc” cho 100 answers nhưng chỉ 60 đúng, confidence bị miscalibrated. Calibration useful trong medicine, investing, software estimates và eyewitness judgments.

Calibration cần repeated feedback; một single decision không đủ để estimate stable metacognitive ability.

## 13. Metacognitive control

Monitoring chỉ có ích nếu dẫn tới **metacognitive control**: allocate study time, request help, verify source, switch strategy hoặc stop searching.

A common failure:

```text
Familiarity ↑
→ Confidence ↑
→ Verification ↓
→ Error persists
```

Trong AI use, fluent output có thể tăng subjective confidence mà không tăng factual accuracy. Vì vậy workflow nên separate generation from verification.

## 14. Fluency và illusion of knowledge

Information dễ đọc, repeated hoặc well-formatted thường feels more familiar. Processing fluency có thể influence truth judgment, liking và confidence.

Fluency không luôn misleading; familiar information đôi khi thật sự reliable. Problem xảy ra khi environment manipulate fluency independently of truth.

Xem [[../06_applied/17_misinformation_belief_revision_and_inoculation]].

## 15. Dunning–Kruger: cần hiểu cẩn thận

Popular version nói “người kém luôn nghĩ mình giỏi”. Evidence thực tế phức tạp hơn. Poor performers often misestimate, nhưng statistical artifacts, regression to mean, measurement reliability và reference information influence observed pattern.

> **Trạng thái bằng chứng:** performance–self-assessment mismatch là real research topic; internet slogan “càng ngu càng tự tin” là overstatement và không nên dùng như diagnosis người khác.

## 16. Bias blind spot

Con người dễ nhận bias ở others hơn ở mình. Awareness of bias names không tự tạo immunity; expert debiasing cần procedure, external check và feedback.

Checklist hữu ích vì nó externalize control thay vì trông chờ introspection hoàn hảo.

## 17. Debiasing theo cơ chế

Không có một “debiasing trick” sửa mọi bias. Strategy nên target source:

- confirmation bias → seek disconfirming evidence;
- anchoring → independent estimate/reference class;
- overconfidence → calibration feedback;
- availability → base-rate data;
- sunk cost → write future-only decision rule;
- misinformation → source check + correction + alternative explanation.

## 18. Decision hygiene

**Decision hygiene** giảm noise và bias bằng process design:

1. define criterion trước;
2. collect independent estimates trước discussion;
3. separate evidence from interpretation;
4. log uncertainty;
5. review outcome later;
6. distinguish process quality from outcome luck.

Một good decision có thể cho bad outcome vì uncertainty; một bad decision có thể lucky.

## 19. Metacognition và learning

Learners thường overvalue rereading vì fluency cao và undervalue retrieval vì retrieval feels difficult.

**Desirable difficulty** không nghĩa “càng khó càng tốt”; difficulty chỉ valuable nếu nó activate mechanism relevant cho later performance.

Calibration tốt cần delayed test, retrieval without notes và transfer task, không chỉ feeling immediately after study.

Xem [[09_learning_transfer_forgetting_and_durable_knowledge]].

## 20. Metacognition xã hội

Confidence không chỉ ảnh hưởng self. Trong group, confident speaker có thể được weighted more even when accuracy không cao. Shared confidence can coordinate team nhưng cũng amplify error.

Good team process nên hỏi both `who is confident?` và `whose confidence is calibrated in this domain?`.

Xem [[../03_human_development_and_person/10_group_dynamics_collective_behavior_and_cooperation]].

## 21. Neuroscience của metacognition

Neuroimaging và lesion studies tìm networks liên quan monitoring/confidence, thường gồm prefrontal và parietal regions tùy task.

> **Trạng thái bằng chứng:** neural correlates có evidence, nhưng mapping “một region = metacognition” là oversimplification. Computation likely distributed và task-dependent.

## 22. Common misconceptions

### “Biết tên bias giúp hết bias”

Không. Knowledge without procedure/feedback có limited effect.

### “Bias nghĩa là irrational”

Không nhất thiết. Heuristic có thể ecologically rational trong environment phù hợp.

### “Confidence cao nghĩa accuracy cao”

Không universally. Relationship phụ thuộc calibration, domain và procedure.

### “Expert không bị bias”

Expertise giảm một số errors nhưng tạo domain-specific blind spots và overgeneralization risk.

## 23. Mental model

```text
Evidence
   ↓
First-order decision
   ↓
Confidence / self-evaluation
   ↓
Metacognitive control
   ↓
Verify / persist / stop / seek help
```

Bias thường xuất hiện khi cue thuận tiện thay target thật; metacognition tốt là biết cue nào đáng trust và khi nào cần external correction.

## Kết nối kiến thức

Đọc cùng [[02_thinking_language_and_decision]], [[08_decision_under_risk_uncertainty_and_ambiguity]], [[01_memory]], [[../06_applied/17_misinformation_belief_revision_and_inoculation]], [[../06_applied/18_financial_psychology_and_personal_decision_making]] và [[../90_connections/02_human_ai_collaboration_trust_and_cognitive_offloading]].
