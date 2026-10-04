# Thiên kiến nhận thức và siêu nhận thức

> **Mạch đọc:** [README](../README.md) là bản đồ owner của **Thiên kiến nhận thức và siêu nhận thức**. Route đi từ heuristics và trade-offs → confirmation/availability/anchoring biases → metacognition, confidence và calibration → debiasing/intervention limits → quyết định có bằng chứng.

**Thiên kiến nhận thức (cognitive bias)** không có nghĩa con người luôn phi lý. Nó mô tả một mẫu (pattern / 패턴) sai lệch có hệ thống so với một benchmark như lô-gic (logic / 논리), xác suất (probability / 확률), unbiased estimation hoặc long-term goal. Một heuristic có thể tạo độ lệch (bias / 편향) trong laboratory tác vụ (task / 작업) nhưng vẫn adaptive trong môi trường khác nếu nó giảm tìm kiếm (search / 검색) chi phí (cost / 비용) hoặc phản ứng nhanh trước threat.

**Siêu nhận thức (metacognition)** là khả năng theo dõi và điều chỉnh chính quá trình nhận thức của mình: mình biết gì, không biết gì, confidence bao nhiêu, chiến lược (strategy / 전략) nào đang hiệu quả và khi nào cần đổi chiến lược (strategy / 전략).

> **Trạng thái bằng chứng:** con người có systematic biases và confidence có thể lệch khỏi mục tiêu (objective / 목표) hiệu năng (performance / 성능) là bằng chứng tương đối vững. Các computational/neural các mô hình (models / 모델들) giải thích confidence và metacognition là hiện tại (current / 현재) theories; cơ chế (mechanism / 메커니즘) cụ thể vẫn đang active research.

Xem [[../EVIDENCE_STATUS_GUIDE]].

## 1. Heuristic: lối tắt có sự đánh đổi (trade-off / 트레이드오프)

**Heuristic** là chiến lược (strategy / 전략) đơn giản hóa quyết định (decision / 결정) khi thời gian (time / 시간), thông tin (information / 정보) hoặc computational tài nguyên (resource / 자원) bị giới hạn. Heuristic không tự động “xấu”.

Ví dụ, dùng familiarity để đoán “thứ này có lẽ đúng” thường hiệu quả trong môi trường nơi repeated exposure correlate với validity, nhưng trở nên nguy hiểm khi misinformation được lặp lại có chủ đích.

Cách học độ lệch (bias / 편향) hữu ích hơn memorizing hundreds of names là hỏi:

```text
Resource limit nào tồn tại?
Cue nào được dùng thay cho target?
Environment nào làm heuristic useful?
Khi nào cue-target relation bị phá?
```

> **Nối mạch:** **Heuristic** giúp xử lý nhanh nhưng mang trade-off về độ chính xác; **confirmation bias** chỉ ra cách ta ưu tiên dữ kiện hợp với niềm tin sẵn có. **Hindsight bias** tiếp theo cho thấy sau khi biết kết quả, ta dễ tưởng mình đã dự đoán đúng từ đầu.

## 2. Confirmation độ lệch (bias / 편향)

**Thiên kiến xác nhận (confirmation bias)** mô tả tendency tìm, ưu tiên hoặc diễn giải bằng chứng (evidence / 증거) theo belief hiện có.

Một nhà phát triển (developer / 개발자) tin cơ sở dữ liệu (database / 데이터베이스) là bottleneck có thể chỉ đọc slow-query log và bỏ qua mạng (network / 네트워크) dấu vết (trace / 추적). cơ chế (mechanism / 메커니즘) không chỉ là “muốn mình đúng”; hiện tại (current / 현재) hypothesis làm supporting cues dễ được retrieve hơn và testing chiến lược (strategy / 전략) có thể asymmetric.

Antidote tốt là **tư duy phản chứng (falsification mindset)**: hỏi observation nào nếu xuất hiện sẽ làm hypothesis yếu đi.

> **Nối mạch:** Confirmation bias làm lệch việc chọn bằng chứng trước quyết định; hindsight bias làm lệch cách nhớ lại sau quyết định. **Availability heuristic** nối hai thời điểm bằng cách dùng ký ức dễ gọi ra làm đại diện cho tần suất.

## 3. Hindsight độ lệch (bias / 편향)

**Thiên kiến nhìn lại (hindsight bias)** làm kết quả (outcome / 결과) sau khi xảy ra trông predictable hơn mức nó thực sự từng có.

Trong sự cố (incident / 인시던트) postmortem, biết dịch vụ (service / 서비스) đã crash khiến tín hiệu (signal / 신호) trước crash trông “obvious”, dẫn đến unfair blame. quyết định (decision / 결정) log ghi prediction và bất định (uncertainty / 불확실성) trước kết quả (outcome / 결과) giúp chống hindsight reconstruction.

> **Nối mạch:** Hindsight bias cho thấy trí nhớ tái dựng chứ không phải bản ghi nguyên vẹn; availability biến cơ chế đó thành phán đoán xác suất tức thời. **Representativeness và base-rate neglect** tiếp tục hỏi khi nào sự giống nhau lấn át tần suất nền.

## 4. Availability heuristic

**Heuristic sẵn có (availability heuristic)** dùng ease of retrieval như cue cho xác suất (probability / 확률) hoặc frequency.

Một dramatic plane accident dễ nhớ hơn ordinary car crash, khiến subjective rủi ro (risk / 위험) lệch. Trong công việc (work / 작업), một môi trường vận hành (production / 운영 환경) sự cố (incident / 인시던트) mới xảy ra có thể làm nhóm (team / 팀) overestimate xác suất (probability / 확률) của same thất bại (failure / 실패) và neglect less salient risks.

> **Nối mạch:** Availability lấy độ dễ nhớ làm tín hiệu, còn **representativeness** lấy độ giống mẫu; cả hai có thể bỏ qua base rate. **Anchoring** mở rộng vấn đề sang việc một con số ban đầu kéo lệch các ước lượng sau đó.

## 5. Representativeness và base-rate neglect

**Representativeness** dùng similarity với prototype để judge xác suất (probability / 확률). Nếu description “rất lô-gic (logic / 논리), ít nói, thích debugging” giống stereotype nhà phát triển (developer / 개발자), người ta có thể ignore cơ sở (base / 기반) tỷ lệ (rate / 비율) của occupations trong population.

**Bỏ qua tần suất nền (base-rate neglect)** là thất bại (fail / 실패) to incorporate prior xác suất (probability / 확률). Bayesian lập luận (reasoning / 추론) giúp formalize tại sao bằng chứng (evidence / 증거) strength phải được đọc cùng prior prevalence.

Xem [[../00_foundations/09_replication_meta_analysis_and_bayesian_reasoning]].

> **Nối mạch:** Khi representativeness bỏ qua phân bố nền, **anchoring** cho thấy điểm khởi đầu cũng có thể chi phối cập nhật. **Framing effect** tiếp theo kiểm tra cách cùng một lựa chọn đổi giá trị chỉ vì cách mô tả.

## 6. Anchoring

**Hiệu ứng neo (anchoring)** xảy ra khi initial number/giá trị (value / 값) ảnh hưởng estimate sau đó, kể cả khi anchor arbitrary hoặc weakly relevant.

Salary negotiation, thuộc tính (property / 속성) price và effort estimation đều có thể bị anchor. Debias không đơn giản là “biết anchor tồn tại”; cần independent estimate, tham chiếu (reference / 참조) lớp (class / 클래스) hoặc phạm vi (range / 범위) trước khi exposure nếu possible.

> **Nối mạch:** Anchoring đặt một mốc tham chiếu, còn framing chọn khung diễn giải quanh mốc đó. **Loss aversion và prospect theory** giải thích vì sao khung lời được–mất làm thay đổi trọng số tâm lý của cùng một kết quả.

## 7. Framing tác động (effect / 효과)

Cùng kết quả (outcome / 결과) có thể tạo preference khác khi frame bằng gain hay mất mát (loss / 손실). Framing không chứng minh con người “không rational” theo mọi definition; nó cho thấy biểu diễn (representation / 표현) của choice influence giá trị (value / 값) construction.

Ứng dụng (application / 애플리케이션) phải thận trọng vì framing tác động (effect / 효과) magnitude phụ thuộc lĩnh vực (domain / 도메인), wording, stakes và population.

> **Nối mạch:** Framing làm nổi bật miền lời hoặc miền mất; **loss aversion** khiến tổn thất được cảm nhận nặng hơn lợi ích tương đương. **Sunk cost** là hệ quả theo thời gian: khoản đã mất kéo quyết định tiếp tục dù không còn phù hợp.

## 8. mất mát (loss / 손실) aversion và prospect lý thuyết (theory / 이론)

**Prospect lý thuyết (theory / 이론)** mô tả quyết định (decision / 결정) relative to tham chiếu (reference / 참조) điểm (point / 지점), diminishing sensitivity và mất mát (loss / 손실) aversion trong nhiều risky-choice settings.

> **Trạng thái bằng chứng:** reference-dependent choice và nonlinear xác suất (probability / 확률) weighting có substantial empirical hỗ trợ (support / 지원); chính xác (exact / 정확한) parameters và universality across domains/individuals là model-dependent, không phải fixed psychological constants.

Xem [[08_decision_under_risk_uncertainty_and_ambiguity]].

> **Nối mạch:** Sunk cost cho thấy loss aversion làm ta bảo vệ quá khứ thay vì tối ưu từ hiện tại. **Overconfidence** chuyển trọng tâm sang độ tin cậy của người ra quyết định đối với phán đoán của chính mình.

## 9. Sunk chi phí (cost / 비용)

**Hiệu ứng chi phí chìm (sunk-cost effect)** là tendency tiếp tục vì đã đầu tư trước đó dù future expected giá trị (value / 값) không hỗ trợ (support / 지원) tiếp tục.

Không phải mọi persistence sau investment là độ lệch (bias / 편향); past investment có thể chứa thông tin (information / 정보) về hidden benefit hoặc switching chi phí (cost / 비용). Chỉ gọi sunk-cost độ lệch (bias / 편향) khi past irrecoverable chi phí (cost / 비용) influence quyết định (decision / 결정) beyond relevant future consequences.

> **Nối mạch:** Overconfidence có thể là đánh giá quá cao năng lực, độ chính xác hoặc khả năng kiểm soát; nó làm sunk-cost escalation khó nhận ra hơn. **Metacognitive monitoring** cung cấp cơ chế theo dõi để so sánh dự đoán với kết quả.

## 10. Overconfidence có nhiều dạng

“Overconfidence” không phải một phenomenon duy nhất.

- **Overestimation**: nghĩ hiệu năng (performance / 성능) mình cao hơn thực tế.
- **Overplacement**: nghĩ mình tốt hơn others quá mức.
- **Overprecision**: confidence interval quá hẹp.

Tách các dạng này quan trọng vì cơ chế (mechanism / 메커니즘) và intervention khác nhau.

> **Nối mạch:** **Metacognitive monitoring** hỏi “mình biết chắc đến đâu?” thay vì chấp nhận confidence. **Calibration** biến câu hỏi đó thành quan hệ đo được giữa xác suất dự báo và tần suất đúng.

## 11. Metacognitive monitoring

**Metacognitive monitoring** đánh giá trạng thái (state / 상태) hiện tại: “tôi có nhớ không?”, “confidence bao nhiêu?”, “tôi có hiểu explanation này không?”.

Research hiện đại thường đo **metacognitive sensitivity**: confidence có phân biệt correct vs incorrect trials tốt đến đâu. Một người có overall confidence thấp nhưng sensitivity tốt vẫn có insight; ngược lại, confidence cao không đồng nghĩa monitoring tốt.

> **hiện tại (current / 현재) lý thuyết (theory / 이론):** confidence được xem như suy luận (inference / 추론) từ bằng chứng (evidence / 증거) về tác vụ (task / 작업), bất định (uncertainty / 불확실성) và self-model. Các computational các mô hình (models / 모델들) khác nhau tranh luận tín hiệu (signal / 신호) nào được dùng và ở stage nào.

> **Nối mạch:** Monitoring phát hiện chênh lệch giữa tin tưởng và đúng sai; **calibration** định lượng chênh lệch đó. **Metacognitive control** dùng tín hiệu đã hiệu chuẩn để đổi chiến lược, thời gian hoặc mức trợ giúp.

## 12. Calibration

**Hiệu chỉnh (calibration)** hỏi confidence có match empirical accuracy không.

Nếu người học nói “90% chắc” cho 100 answers nhưng chỉ 60 đúng, confidence bị miscalibrated. Calibration useful trong medicine, investing, software estimates và eyewitness judgments.

Calibration cần repeated phản hồi (feedback / 피드백); một single quyết định (decision / 결정) không đủ để estimate stable metacognitive ability.

> **Nối mạch:** **Metacognitive control** chỉ hiệu quả khi tín hiệu đánh giá đáng tin; cảm giác trôi chảy có thể phá hỏng nó. **Fluency và illusion of knowledge** giải thích vì sao dễ đọc hoặc dễ nhớ không đồng nghĩa hiểu sâu.

## 13. Metacognitive điều khiển (control / 제어)

Monitoring chỉ có ích nếu dẫn tới **metacognitive điều khiển (control / 제어)**: allocate study thời gian (time / 시간), yêu cầu (request / 요청) help, verify nguồn (source / 소스), switch chiến lược (strategy / 전략) hoặc stop searching.

A dùng chung (common / 공통) thất bại (failure / 실패):

```text
Familiarity ↑
→ Confidence ↑
→ Verification ↓
→ Error persists
```

Trong AI use, fluent đầu ra (output / 출력) có thể tăng subjective confidence mà không tăng factual accuracy. Vì vậy workflow nên separate generation from xác minh (verification / 확인).

> **Nối mạch:** Fluency tạo cảm giác đúng và đủ, khiến người học điều khiển nỗ lực sai hướng. **Dunning–Kruger** cần được đọc cẩn thận như vấn đề thiếu tiêu chuẩn tự đánh giá, không phải nhãn cố định cho một nhóm người.

## 14. Fluency và illusion of kiến thức (knowledge / 지식)

Thông tin (information / 정보) dễ đọc, repeated hoặc well-formatted thường feels more familiar. Processing fluency có thể influence truth judgment, liking và confidence.

Fluency không luôn misleading; familiar thông tin (information / 정보) đôi khi thật sự reliable. bài toán (problem / 문제) xảy ra khi môi trường (environment / 환경) manipulate fluency independently of truth.

Xem [[../06_applied/17_misinformation_belief_revision_and_inoculation]].

> **Nối mạch:** Dunning–Kruger nhấn mạnh khoảng cách giữa năng lực và khả năng đánh giá năng lực; fluency chỉ là một nguồn gây nhiễu. **Blind spot bias** mở rộng sang việc nhận ra lỗi của người khác dễ hơn lỗi của mình.

## 15. Dunning–Kruger: cần hiểu cẩn thận

Popular phiên bản (version / 버전) nói “người kém luôn nghĩ mình giỏi”. bằng chứng (evidence / 증거) thực tế phức tạp hơn. Poor performers often misestimate, nhưng statistical artifacts, regression to mean, đo lường (measurement / 측정) độ tin cậy (reliability / 신뢰성) và tham chiếu (reference / 참조) thông tin (information / 정보) influence observed mẫu (pattern / 패턴).

> **Trạng thái bằng chứng:** hiệu năng (performance / 성능)–self-assessment mismatch là real research topic; internet slogan “càng ngu càng tự tin” là overstatement và không nên dùng như diagnosis người khác.

> **Nối mạch:** Blind spot cho thấy tự nhận biết không tự xuất hiện chỉ vì biết tên các bias. **Debiasing theo cơ chế** phải thay đổi điểm thu thập dữ liệu, quy trình so sánh hoặc feedback tương ứng với từng lỗi.

## 16. độ lệch (bias / 편향) blind spot

Con người dễ nhận độ lệch (bias / 편향) ở others hơn ở mình. Awareness of độ lệch (bias / 편향) names không tự tạo immunity; expert debiasing cần procedure, bên ngoài (external / 외부) check và phản hồi (feedback / 피드백).

Checklist hữu ích vì nó externalize điều khiển (control / 제어) thay vì trông chờ introspection hoàn hảo.

> **Nối mạch:** Từ blind spot, **debiasing** xác định cơ chế can thiệp thay vì khuyên “suy nghĩ lý trí hơn”. **Decision hygiene** đóng gói các can thiệp thành quy trình lặp lại, độc lập với người ra quyết định cụ thể.

## 17. Debiasing theo cơ chế

Không có một “debiasing trick” sửa mọi độ lệch (bias / 편향). chiến lược (strategy / 전략) nên mục tiêu (target / 대상) nguồn (source / 소스):

- confirmation độ lệch (bias / 편향) → seek disconfirming bằng chứng (evidence / 증거);
- anchoring → independent estimate/tham chiếu (reference / 참조) lớp (class / 클래스);
- overconfidence → calibration phản hồi (feedback / 피드백);
- availability → base-rate dữ liệu (data / 데이터);
- sunk chi phí (cost / 비용) → ghi (write / 쓰기) future-only quyết định (decision / 결정) quy tắc (rule / 규칙);
- misinformation → nguồn (source / 소스) check + correction + alternative explanation.

> **Nối mạch:** **Decision hygiene** dùng checklist, tách dự báo khỏi lựa chọn và ghi lại base rate để giảm bias có hệ thống. **Metacognition và học tập** đưa cùng nguyên tắc vào việc chọn chiến lược học, không chỉ quyết định ngoài đời.

## 18. quyết định (decision / 결정) hygiene

**quyết định (decision / 결정) hygiene** giảm noise và độ lệch (bias / 편향) bằng tiến trình (process / 프로세스) thiết kế (design / 설계):

1. define criterion trước;
2. collect independent estimates trước discussion;
3. separate bằng chứng (evidence / 증거) from interpretation;
4. log bất định (uncertainty / 불확실성);
5. rà soát (review / 검토) kết quả (outcome / 결과) later;
6. distinguish tiến trình (process / 프로세스) chất lượng (quality / 품질) from kết quả (outcome / 결과) luck.

Một good quyết định (decision / 결정) có thể cho bad kết quả (outcome / 결과) vì bất định (uncertainty / 불확실성); một bad quyết định (decision / 결정) có thể lucky.

> **Nối mạch:** Học tập tốt cần hygiene trong việc dự đoán mức nhớ, chọn bài và kiểm tra lại kết quả; đó là metacognition có dữ liệu. **Metacognition xã hội** mở rộng tự theo dõi sang cách ta đọc ý định và hiểu biết của người khác.

## 19. Metacognition và học tập (learning / 학습)

Learners thường overvalue rereading vì fluency cao và undervalue retrieval vì retrieval feels difficult.

**Desirable difficulty** không nghĩa “càng khó càng tốt”; difficulty chỉ valuable nếu nó activate cơ chế (mechanism / 메커니즘) relevant cho later hiệu năng (performance / 성능).

Calibration tốt cần delayed kiểm thử (test / 테스트), retrieval without notes và transfer tác vụ (task / 작업), không chỉ feeling immediately after study.

Xem [[09_learning_transfer_forgetting_and_durable_knowledge]].

> **Nối mạch:** **Metacognition xã hội** dùng tín hiệu từ tương tác, chuẩn nhóm và phản hồi, nên dễ chịu ảnh hưởng của conformity và mind-reading bias. **Neuroscience của metacognition** hỏi các quá trình đánh giá này được thực hiện ở mức hệ thần kinh ra sao.

## 20. Metacognition xã hội

Confidence không chỉ ảnh hưởng self. Trong group, confident speaker có thể được weighted more even when accuracy không cao. dùng chung (shared / 공유) confidence can coordinate nhóm (team / 팀) nhưng cũng amplify lỗi (error / 오류).

Good nhóm (team / 팀) tiến trình (process / 프로세스) nên hỏi both `who is confident?` và `whose confidence is calibrated in this domain?`.

Xem [[../03_human_development_and_person/10_group_dynamics_collective_behavior_and_cooperation]].

> **Nối mạch:** Não bộ cung cấp cơ chế cho confidence, error monitoring và cập nhật, nhưng không biến các bias thành định mệnh sinh học. **Common misconceptions** tiếp theo kiểm tra các diễn giải quá đơn giản về bias và expertise.

## 21. Neuroscience của metacognition

Neuroimaging và lesion studies tìm networks liên quan monitoring/confidence, thường gồm prefrontal và parietal regions tùy tác vụ (task / 작업).

> **Trạng thái bằng chứng:** neural correlates có bằng chứng (evidence / 증거), nhưng ánh xạ (mapping / 매핑) “một region = metacognition” là oversimplification. Computation likely phân tán (distributed / 분산) và task-dependent.

> **Nối mạch:** Các misconception được sửa bằng cách phân biệt cơ chế, điều kiện và bằng chứng thay vì gán “bias = irrational”. **Mental model** sẽ gom các tầng từ heuristic đến feedback và thiết kế môi trường quyết định.

## 22. dùng chung (common / 공통) misconceptions

### “Biết tên độ lệch (bias / 편향) giúp hết độ lệch (bias / 편향)”

Không. kiến thức (knowledge / 지식) without procedure/phản hồi (feedback / 피드백) có limited tác động (effect / 효과).

### “độ lệch (bias / 편향) nghĩa là irrational”

Không nhất thiết. Heuristic có thể ecologically rational trong môi trường (environment / 환경) phù hợp.

### “Confidence cao nghĩa accuracy cao”

Không universally. Relationship phụ thuộc calibration, lĩnh vực (domain / 도메인) và procedure.

### “Expert không bị độ lệch (bias / 편향)”

Expertise giảm một số errors nhưng tạo domain-specific blind spots và overgeneralization rủi ro (risk / 위험).

> **Nối mạch:** **Mental model** của chapter là chuỗi: lối tắt tạo tín hiệu nhanh → bias làm lệch cập nhật → metacognition đo sai số → hygiene và feedback sửa quy trình. **Kết nối kiến thức** đưa chuỗi này sang học tập, quyết định và tương tác xã hội.

## 23. mô hình tư duy (mental model / 사고 모델)

Phần này chốt mental model thành một chuỗi có thể dùng lại: bối cảnh → cơ chế → bằng chứng → giới hạn → ứng dụng. Hãy đọc sơ đồ như công cụ suy luận, không như một nhãn kết luận tự động.

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

Độ lệch (bias / 편향) thường xuất hiện khi cue thuận tiện thay mục tiêu (target / 대상) thật; metacognition tốt là biết cue nào đáng trust và khi nào cần bên ngoài (external / 외부) correction.

> **Nối mạch:** **Kết nối kiến thức** khép bài bằng cách giữ nguyên cơ chế nhưng đổi bối cảnh: học tập cần calibration, quyết định cần hygiene, còn nhóm cần feedback và kiểm tra base rate. Đây là điểm bàn giao cho các chapter cognition và social psychology trong owner Psychology.

## Kết nối kiến thức

Đọc cùng [[02_thinking_language_and_decision]], [[08_decision_under_risk_uncertainty_and_ambiguity]], [[01_memory]], [[../06_applied/17_misinformation_belief_revision_and_inoculation]], [[../06_applied/18_financial_psychology_and_personal_decision_making]] và [[../90_connections/02_human_ai_collaboration_trust_and_cognitive_offloading]].

> **Bàn giao:** Sau **Kết nối kiến thức**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](../README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
