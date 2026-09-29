# Human–AI collaboration, trust và giảm tải nhận thức

> **Mạch đọc:** Đọc **Human–AI collaboration, trust và giảm tải nhận thức** như một mắt xích của lộ trình học (learning path / 학습 경로) hiện tại, không như một ghi chú tách rời. Nội dung đi từ **1. Trust, trustworthiness và reliance là ba construct khác nhau** sang **2. Appropriate reliance**; điểm nối này chuẩn bị câu hỏi cho các mục sau thay vì dừng ở định nghĩa đầu tiên.


AI ngày càng tham gia coding, writing, tìm kiếm (search / 검색), diagnosis hỗ trợ (support / 지원), customer dịch vụ (service / 서비스) và quyết định (decision / 결정) hỗ trợ (support / 지원). Câu hỏi vì vậy không còn chỉ là “mô hình (model / 모델) chính xác bao nhiêu?”, mà là **con người sẽ dùng đầu ra (output / 출력) đó như thế nào trong một workflow cụ thể**.

Một hệ thống có accuracy cao nhưng làm người dùng phụ thuộc quá mức vẫn có thể tạo rủi ro. Ngược lại, một hệ thống hữu ích nhưng bị bỏ qua sau một lỗi cũng làm mất giá trị. Mục tiêu là **sự phụ thuộc phù hợp (appropriate reliance)**, không phải trust càng cao càng tốt.

> **Trạng thái bằng chứng:** research gần đây nhấn mạnh phải tách **trust**, **trustworthiness** và **reliance**. Explainability không tự động tạo appropriate reliance; empirical results về explainability → trust vẫn mixed. Human–AI hiệu năng (performance / 성능) phụ thuộc tác vụ (task / 작업), người dùng (user / 사용자), giao diện (interface / 인터페이스), incentive và xác minh (verification / 확인) tiến trình (process / 프로세스).

## 1. Trust, trustworthiness và reliance là ba construct khác nhau

**Trust** là thái độ/kỳ vọng của người dùng về hệ thống. **Trustworthiness** là mức hệ thống thực sự đáng tin theo tiêu chí như năng lực (capability / 역량), độ tin cậy (reliability / 신뢰성), an toàn (safety / 안전) hoặc integrity. **Reliance** là hành vi: người dùng có làm theo recommendation hay không.

Một người có thể nói “tôi không tin AI lắm” nhưng vẫn bản sao (copy / 복사) đầu ra (output / 출력) mọi lần vì tiện. Ngược lại, họ có thể đánh giá hệ thống (system / 시스템) tốt nhưng không dùng recommendation trong high-stakes trường hợp (case / 사례).

Rà soát (review / 검토) 2025–2026 về trust in AI nhấn mạnh rằng nếu trộn ba construct này, nghiên cứu dễ kết luận sai rằng “trust cao = sử dụng đúng”.

## 2. Appropriate reliance

**Sự phụ thuộc phù hợp (appropriate reliance)** nghĩa là dựa vào AI khi nó đáng dựa và giữ/reclaim human judgment khi mô hình (model / 모델) không đáng dựa.

```text
AI đúng + user follow   → reliance phù hợp
AI sai + user reject    → reliance phù hợp
AI sai + user follow    → over-reliance
AI đúng + user reject   → under-reliance
```

Điểm này quan trọng hơn average trust score.

## 3. Calibration phải theo tác vụ (task / 작업), không theo “AI nói chung”

Một mã (code / 코드) assistant có thể tốt ở boilerplate nhưng yếu với undocumented nghiệp vụ (business / 비즈니스) quy tắc (rule / 규칙). Một mô hình (model / 모델) có thể mạnh ở summarization nhưng kém ở source-grounded factual xác minh (verification / 확인).

Người dùng cần **năng lực (capability / 역량) profile theo tác vụ (task / 작업)**, không phải một niềm tin toàn cục kiểu “AI tốt” hoặc “AI không đáng tin”.

## 4. Automation độ lệch (bias / 편향)

**Thiên lệch tự động hóa (automation bias)** xảy ra khi người dùng ưu tiên suggestion của automation dù có dấu hiệu nó sai.

Cơ chế có thể gồm perceived authority, giảm vigilance khi automation thường đúng, áp lực thời gian, tiết kiệm effort và diffusion of responsibility.

Trong enterprise hệ thống (system / 시스템), trường dữ liệu (field / 필드) được prefill có thể ít bị kiểm tra chỉ vì “hệ thống (system / 시스템) đã điền”.

## 5. thuật toán (algorithm / 알고리즘) aversion

Ngược lại, **thuật toán (algorithm / 알고리즘) aversion** mô tả việc người dùng từ chối thuật toán (algorithm / 알고리즘) sau khi quan sát lỗi, đôi khi khắt khe hơn với lỗi máy so với lỗi của human expert.

Hai hiện tượng không mâu thuẫn. Cả hai cho thấy reliance phụ thuộc perceived điều khiển (control / 제어), consequence, previous experience và xã hội (social / 사회적) framing chứ không chỉ mục tiêu (objective / 목표) accuracy.

## 6. Explainability không đồng nghĩa trust đúng

“Explainable AI” không phải một tính năng (feature / 기능) duy nhất. Explanation có thể phục vụ debugging, expert rà soát (review / 검토), người dùng (user / 사용자) comprehension, compliance hoặc teaching.

Một explanation dễ hiểu nhưng không faithful có thể **tăng trust sai**. rà soát (review / 검토) 2025 cho thấy quan hệ (relation / 관계) giữa explainability và trust còn mixed; vì vậy mục tiêu không phải “thêm explanation để người dùng (user / 사용자) tin hơn”, mà là giúp người dùng (user / 사용자) quyết định tốt hơn.

Cần hỏi:

```text
explanation có faithful không?
user hiểu được limitation không?
explanation có giúp detect error không?
```

## 7. bất định (uncertainty / 불확실성) communication

AI thường trả lời bằng câu hoàn chỉnh ngay cả khi bằng chứng (evidence / 증거) yếu, tạo **ảo giác chắc chắn (illusion of certainty)**.

Giao diện (interface / 인터페이스) high-stakes có thể cần nguồn (source / 소스) provenance, alternative hypothesis, “insufficient bằng chứng (evidence / 증거)” trạng thái (state / 상태), confidence nếu được calibrated và cảnh báo khi đầu vào (input / 입력) nằm ngoài phân phối (distribution / 분포) quen thuộc.

Nhưng thêm quá nhiều bất định (uncertainty / 불확실성) tín hiệu (signal / 신호) cũng có thể gây cognitive overload. Thiết kế phải match rủi ro (risk / 위험).

Xem [[03_risk_uncertainty_and_science_communication]].

## 8. Cognitive offloading

**Giảm tải nhận thức (cognitive offloading)** là chuyển một phần công việc nhận thức sang bên ngoài (external / 외부) công cụ (tool / 도구). ghi chú (note / 노트), calculator, GPS và IDE autocomplete đều là offloading; AI mở rộng nó sang synthesis, drafting, planning và reasoning-like đầu ra (output / 출력).

Offloading không mặc định xấu. Câu hỏi là **mục tiêu hiện tại là hiệu năng (performance / 성능) hay học tập (learning / 학습)**, và skill nào vẫn cần giữ nội bộ.

Xem [[../02_learning_and_cognition/10_cognitive_offloading_external_memory_and_extended_cognition]].

## 9. hiệu năng (performance / 성능) goal và học tập (learning / 학습) goal

Nếu mục tiêu là hoàn thành môi trường vận hành (production / 운영 환경) tác vụ (task / 작업), offloading nhiều có thể hợp lý. Nếu mục tiêu là xây competence, assistance quá sớm có thể làm giảm retrieval, generation và error-driven học tập (learning / 학습).

Một mẫu (pattern / 패턴) học hữu ích:

```text
tự làm trước
→ ghi reasoning
→ dùng AI critique
→ kiểm chứng
→ tự tái dựng không nhìn đáp án
```

Đây là học tập (learning / 학습) thiết kế (design / 설계) heuristic, không phải universal law.

## 10. Deskilling là nhiều hiện tượng khác nhau

**Suy giảm kỹ năng (deskilling)** có thể gồm giảm declarative kiến thức (knowledge / 지식), procedural fluency, lỗi (error / 오류) detection, situation awareness hoặc calibration.

Không có bằng chứng (evidence / 증거) để nói “dùng AI chắc chắn làm con người kém thông minh”. kết quả (outcome / 결과) phụ thuộc tác vụ (task / 작업) allocation, huấn luyện (training / 학습) thiết kế (design / 설계), frequency of independent practice và cách rà soát (review / 검토).

## 11. xác minh (verification / 확인) debt

AI có thể tạo sản phẩm tạo ra (artifact / 산출물) nhanh hơn con người kiểm chứng. Khoảng cách này tạo **nợ kiểm chứng (verification debt)**.

Rủi ro (risk / 위험) tăng khi đầu ra (output / 출력) dài, lỗi khó phát hiện, nguồn (source / 소스) không visible, reviewer bị thời gian (time / 시간) pressure và wording rất fluent.

Trong kỹ nghệ phần mềm (software engineering / 소프트웨어 공학), generate 20 tệp (file / 파일) nhanh nhưng không hiểu giả định (assumption / 가정) có thể tăng maintenance chi phí (cost / 비용) dù short-term velocity trông cao.

## 12. Fluency heuristic

LLM viết trôi chảy, và fluency có thể bị nhầm với truth hoặc expertise.

Vì vậy UI/workflow nên tách presentation chất lượng (quality / 품질) khỏi epistemic status:

```text
câu viết hay ≠ evidence tốt
confidence tone ≠ calibrated probability
chi tiết nhiều ≠ factual accuracy
```

Xem [[../06_applied/17_misinformation_belief_revision_and_inoculation]].

## 13. Anthropomorphism

Chat giao diện (interface / 인터페이스) kích hoạt xã hội (social / 사회적) cognition. Người dùng có thể gán intention, empathy hoặc understanding cho hệ thống (system / 시스템).

Anthropomorphism có thể giúp tương tác (interaction / 상호작용) tự nhiên nhưng cũng làm ranh giới (boundary / 경계) mờ và tăng disclosure. rà soát (review / 검토) 2026 về trust in AI nhấn mạnh trust là socially embedded và agent-specific; vì vậy “AI trust” không thể chỉ đo như reaction với một công cụ vô danh.

## 14. Human-in-the-loop phải là oversight thật

Human checkpoint chỉ có ý nghĩa nếu reviewer có thời gian, competence, ngữ cảnh (context / 맥락), authority và tín hiệu (signal / 신호) để phát hiện lỗi.

Nếu một người phải approve hàng trăm recommendation với accuracy rất cao, họ dễ thành rubber stamp. “Có human rà soát (review / 검토)” không tự động là an toàn (safety / 안전) cơ chế (mechanism / 메커니즘).

## 15. nhóm (team / 팀) cognition với AI

Khi AI trở thành thành phần của workflow, nhóm (team / 팀) cần dùng chung (shared / 공유) convention:

- tác vụ (task / 작업) nào được phép dùng AI;
- dữ liệu (data / 데이터) nào không được đưa vào;
- đầu ra (output / 출력) nào bắt buộc rà soát (review / 검토);
- ai giữ quyền sở hữu (ownership / 소유권) cuối;
- provenance được ghi thế nào;
- escalation khi hệ thống (system / 시스템) thất bại (fail / 실패).

Nếu mỗi người tự xây trust mô hình (model / 모델) riêng, consistency và auditability giảm.

## 16. AI trong quyết định (decision / 결정) hỗ trợ (support / 지원)

Một khung phần mềm (framework / 프레임워크) thực dụng:

```text
rủi ro thấp + dễ kiểm tra   → automation cao hơn
rủi ro cao + khó kiểm tra   → human review mạnh hơn
uncertainty cao              → provenance + alternatives
hậu quả khó đảo ngược        → tăng friction trước action
```

Friction đôi khi là an toàn (safety / 안전) tính năng (feature / 기능), không phải UX thất bại (failure / 실패).

## 17. AI và everyday self-regulation

AI có thể hỗ trợ planning, reminder, reflection và journaling prompt. Nhưng nếu mọi quyết định (decision / 결정) nhỏ đều outsource, người dùng có thể giảm practice tự quan sát và tự quyết định.

Một cách dùng thận trọng là AI đóng vai **giàn giáo (scaffold)**: hỗ trợ cấu trúc (structure / 구조) bài toán (problem / 문제), để người dùng (user / 사용자) chọn hành động (action / 동작), theo dõi kết quả (outcome / 결과) rồi giảm hỗ trợ (support / 지원) khi skill tăng.

## 18. Ranh giới bằng chứng

**Bằng chứng tương đối vững:** trust, reliance và trustworthiness là construct khác nhau; automation độ lệch (bias / 편향)/thuật toán (algorithm / 알고리즘) aversion tồn tại; người dùng (user / 사용자) reliance chịu ảnh hưởng của giao diện (interface / 인터페이스), ngữ cảnh (context / 맥락) và tác vụ (task / 작업) rủi ro (risk / 위험).

**Lý thuyết/construct hiện đại:** appropriate reliance, calibration, xác minh (verification / 확인) debt, joint cognitive hệ thống (system / 시스템) và socially embedded trust.

**Còn tranh luận:** cách đo appropriate reliance tốt nhất, tác động (effect / 효과) dài hạn của AI lên skill, mức explainability tối ưu và cách anthropomorphic thiết kế (design / 설계) ảnh hưởng judgment theo thời gian.

**Không được nói:** trust càng cao càng tốt, explainability tự động làm AI an toàn, dùng AI chắc chắn deskill, hoặc human rà soát (review / 검토) luôn đủ.

## Mô hình tư duy

\[
kết quả (outcome / 결과) = f(model, user, interface, Workflow, Incentive, verification)
\]

> Human–AI hệ thống (system / 시스템) nên được đánh giá như **một hệ thống nhận thức chung (joint cognitive system)**, không chỉ bằng benchmark accuracy của mô hình (model / 모델).

## Kết nối kiến thức

Xem [[../06_applied/02_hci_ai_and_human_decision_support]], [[../02_learning_and_cognition/10_cognitive_offloading_external_memory_and_extended_cognition]], [[01_psychology_biology_statistics_and_ai]], [[../06_applied/16_psychological_safety_team_learning_and_speaking_up]], [[03_risk_uncertainty_and_science_communication]] và [[../06_applied/17_misinformation_belief_revision_and_inoculation]].

> **Bàn giao:** Sau **Kết nối kiến thức**, hãy chốt bất biến (invariant / 불변식) và giới hạn của mục này trước khi nối sang kiến thức kế tiếp. Có thể đọc tiếp [00 freud jung and depth psychology in context](./00_freud_jung_and_depth_psychology_in_context.md) để đối chiếu ranh giới (boundary / 경계) gần nhất.
