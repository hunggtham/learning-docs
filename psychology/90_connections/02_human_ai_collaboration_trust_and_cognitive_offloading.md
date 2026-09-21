# Human–AI collaboration, trust và giảm tải nhận thức

AI ngày càng tham gia coding, writing, search, diagnosis support, customer service và decision support. Câu hỏi vì vậy không còn chỉ là “model chính xác bao nhiêu?”, mà là **con người sẽ dùng output đó như thế nào trong một workflow cụ thể**.

Một hệ thống có accuracy cao nhưng làm người dùng phụ thuộc quá mức vẫn có thể tạo rủi ro. Ngược lại, một hệ thống hữu ích nhưng bị bỏ qua sau một lỗi cũng làm mất giá trị. Mục tiêu là **sự phụ thuộc phù hợp (appropriate reliance)**, không phải trust càng cao càng tốt.

> **Trạng thái bằng chứng:** research gần đây nhấn mạnh phải tách **trust**, **trustworthiness** và **reliance**. Explainability không tự động tạo appropriate reliance; empirical results về explainability → trust vẫn mixed. Human–AI performance phụ thuộc task, user, interface, incentive và verification process.

## 1. Trust, trustworthiness và reliance là ba construct khác nhau

**Trust** là thái độ/kỳ vọng của người dùng về hệ thống. **Trustworthiness** là mức hệ thống thực sự đáng tin theo tiêu chí như capability, reliability, safety hoặc integrity. **Reliance** là hành vi: người dùng có làm theo recommendation hay không.

Một người có thể nói “tôi không tin AI lắm” nhưng vẫn copy output mọi lần vì tiện. Ngược lại, họ có thể đánh giá system tốt nhưng không dùng recommendation trong high-stakes case.

Review 2025–2026 về trust in AI nhấn mạnh rằng nếu trộn ba construct này, nghiên cứu dễ kết luận sai rằng “trust cao = sử dụng đúng”.

## 2. Appropriate reliance

**Sự phụ thuộc phù hợp (appropriate reliance)** nghĩa là dựa vào AI khi nó đáng dựa và giữ/reclaim human judgment khi model không đáng dựa.

```text
AI đúng + user follow   → reliance phù hợp
AI sai + user reject    → reliance phù hợp
AI sai + user follow    → over-reliance
AI đúng + user reject   → under-reliance
```

Điểm này quan trọng hơn average trust score.

## 3. Calibration phải theo task, không theo “AI nói chung”

Một code assistant có thể tốt ở boilerplate nhưng yếu với undocumented business rule. Một model có thể mạnh ở summarization nhưng kém ở source-grounded factual verification.

Người dùng cần **capability profile theo task**, không phải một niềm tin toàn cục kiểu “AI tốt” hoặc “AI không đáng tin”.

## 4. Automation bias

**Thiên lệch tự động hóa (automation bias)** xảy ra khi người dùng ưu tiên suggestion của automation dù có dấu hiệu nó sai.

Cơ chế có thể gồm perceived authority, giảm vigilance khi automation thường đúng, áp lực thời gian, tiết kiệm effort và diffusion of responsibility.

Trong enterprise system, field được prefill có thể ít bị kiểm tra chỉ vì “system đã điền”.

## 5. Algorithm aversion

Ngược lại, **algorithm aversion** mô tả việc người dùng từ chối algorithm sau khi quan sát lỗi, đôi khi khắt khe hơn với lỗi máy so với lỗi của human expert.

Hai hiện tượng không mâu thuẫn. Cả hai cho thấy reliance phụ thuộc perceived control, consequence, previous experience và social framing chứ không chỉ objective accuracy.

## 6. Explainability không đồng nghĩa trust đúng

“Explainable AI” không phải một feature duy nhất. Explanation có thể phục vụ debugging, expert review, user comprehension, compliance hoặc teaching.

Một explanation dễ hiểu nhưng không faithful có thể **tăng trust sai**. Review 2025 cho thấy relation giữa explainability và trust còn mixed; vì vậy mục tiêu không phải “thêm explanation để user tin hơn”, mà là giúp user quyết định tốt hơn.

Cần hỏi:

```text
explanation có faithful không?
user hiểu được limitation không?
explanation có giúp detect error không?
```

## 7. Uncertainty communication

AI thường trả lời bằng câu hoàn chỉnh ngay cả khi evidence yếu, tạo **ảo giác chắc chắn (illusion of certainty)**.

Interface high-stakes có thể cần source provenance, alternative hypothesis, “insufficient evidence” state, confidence nếu được calibrated và cảnh báo khi input nằm ngoài distribution quen thuộc.

Nhưng thêm quá nhiều uncertainty signal cũng có thể gây cognitive overload. Thiết kế phải match risk.

Xem [[03_risk_uncertainty_and_science_communication]].

## 8. Cognitive offloading

**Giảm tải nhận thức (cognitive offloading)** là chuyển một phần công việc nhận thức sang external tool. Note, calculator, GPS và IDE autocomplete đều là offloading; AI mở rộng nó sang synthesis, drafting, planning và reasoning-like output.

Offloading không mặc định xấu. Câu hỏi là **mục tiêu hiện tại là performance hay learning**, và skill nào vẫn cần giữ nội bộ.

Xem [[../02_learning_and_cognition/10_cognitive_offloading_external_memory_and_extended_cognition]].

## 9. Performance goal và learning goal

Nếu mục tiêu là hoàn thành production task, offloading nhiều có thể hợp lý. Nếu mục tiêu là xây competence, assistance quá sớm có thể làm giảm retrieval, generation và error-driven learning.

Một pattern học hữu ích:

```text
tự làm trước
→ ghi reasoning
→ dùng AI critique
→ kiểm chứng
→ tự tái dựng không nhìn đáp án
```

Đây là learning design heuristic, không phải universal law.

## 10. Deskilling là nhiều hiện tượng khác nhau

**Suy giảm kỹ năng (deskilling)** có thể gồm giảm declarative knowledge, procedural fluency, error detection, situation awareness hoặc calibration.

Không có evidence để nói “dùng AI chắc chắn làm con người kém thông minh”. Outcome phụ thuộc task allocation, training design, frequency of independent practice và cách review.

## 11. Verification debt

AI có thể tạo artifact nhanh hơn con người kiểm chứng. Khoảng cách này tạo **nợ kiểm chứng (verification debt)**.

Risk tăng khi output dài, lỗi khó phát hiện, source không visible, reviewer bị time pressure và wording rất fluent.

Trong software engineering, generate 20 file nhanh nhưng không hiểu assumption có thể tăng maintenance cost dù short-term velocity trông cao.

## 12. Fluency heuristic

LLM viết trôi chảy, và fluency có thể bị nhầm với truth hoặc expertise.

Vì vậy UI/workflow nên tách presentation quality khỏi epistemic status:

```text
câu viết hay ≠ evidence tốt
confidence tone ≠ calibrated probability
chi tiết nhiều ≠ factual accuracy
```

Xem [[../06_applied/17_misinformation_belief_revision_and_inoculation]].

## 13. Anthropomorphism

Chat interface kích hoạt social cognition. Người dùng có thể gán intention, empathy hoặc understanding cho system.

Anthropomorphism có thể giúp interaction tự nhiên nhưng cũng làm boundary mờ và tăng disclosure. Review 2026 về trust in AI nhấn mạnh trust là socially embedded và agent-specific; vì vậy “AI trust” không thể chỉ đo như reaction với một công cụ vô danh.

## 14. Human-in-the-loop phải là oversight thật

Human checkpoint chỉ có ý nghĩa nếu reviewer có thời gian, competence, context, authority và signal để phát hiện lỗi.

Nếu một người phải approve hàng trăm recommendation với accuracy rất cao, họ dễ thành rubber stamp. “Có human review” không tự động là safety mechanism.

## 15. Team cognition với AI

Khi AI trở thành thành phần của workflow, team cần shared convention:

- task nào được phép dùng AI;
- data nào không được đưa vào;
- output nào bắt buộc review;
- ai giữ ownership cuối;
- provenance được ghi thế nào;
- escalation khi system fail.

Nếu mỗi người tự xây trust model riêng, consistency và auditability giảm.

## 16. AI trong decision support

Một framework thực dụng:

```text
rủi ro thấp + dễ kiểm tra   → automation cao hơn
rủi ro cao + khó kiểm tra   → human review mạnh hơn
uncertainty cao              → provenance + alternatives
hậu quả khó đảo ngược        → tăng friction trước action
```

Friction đôi khi là safety feature, không phải UX failure.

## 17. AI và everyday self-regulation

AI có thể hỗ trợ planning, reminder, reflection và journaling prompt. Nhưng nếu mọi decision nhỏ đều outsource, người dùng có thể giảm practice tự quan sát và tự quyết định.

Một cách dùng thận trọng là AI đóng vai **giàn giáo (scaffold)**: hỗ trợ structure problem, để user chọn action, theo dõi outcome rồi giảm support khi skill tăng.

## 18. Ranh giới bằng chứng

**Bằng chứng tương đối vững:** trust, reliance và trustworthiness là construct khác nhau; automation bias/algorithm aversion tồn tại; user reliance chịu ảnh hưởng của interface, context và task risk.

**Lý thuyết/construct hiện đại:** appropriate reliance, calibration, verification debt, joint cognitive system và socially embedded trust.

**Còn tranh luận:** cách đo appropriate reliance tốt nhất, effect dài hạn của AI lên skill, mức explainability tối ưu và cách anthropomorphic design ảnh hưởng judgment theo thời gian.

**Không được nói:** trust càng cao càng tốt, explainability tự động làm AI an toàn, dùng AI chắc chắn deskill, hoặc human review luôn đủ.

## Mô hình tư duy

\[
Outcome = f(Model, User, Interface, Workflow, Incentive, Verification)
\]

> Human–AI system nên được đánh giá như **một hệ thống nhận thức chung (joint cognitive system)**, không chỉ bằng benchmark accuracy của model.

## Kết nối kiến thức

Xem [[../06_applied/02_hci_ai_and_human_decision_support]], [[../02_learning_and_cognition/10_cognitive_offloading_external_memory_and_extended_cognition]], [[01_psychology_biology_statistics_and_ai]], [[../06_applied/16_psychological_safety_team_learning_and_speaking_up]], [[03_risk_uncertainty_and_science_communication]] và [[../06_applied/17_misinformation_belief_revision_and_inoculation]].