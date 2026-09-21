# Kỹ thuật căn chỉnh và cơ chế giám sát

Không có một thuật toán duy nhất giải quyết toàn bộ bài toán căn chỉnh. Hệ thống production thường kết hợp **hậu huấn luyện (post-training)**, dữ liệu preference, policy/rule, verifier, phân quyền, human approval và đánh giá liên tục. Mục tiêu của chapter này là đặt các kỹ thuật đó vào một kiến trúc chung, để phân biệt rõ thứ gì định hình hành vi mô hình và thứ gì thực sự kiểm soát authority của hệ thống.

## Kiến thức cần có trước

Nên đọc [Căn chỉnh AI và đặc tả mục tiêu](./01_alignment_and_objective_specification.md), [Reward Misspecification](./02_reward_misspecification_and_goal_misgeneralization.md), [SFT](../08_large_language_models/07_supervised_fine_tuning.md), [RLHF](../08_large_language_models/08_rlhf.md), [DPO](../08_large_language_models/09_preference_optimization_and_dpo.md), [Agent Evaluation](../10_agents_and_ai_systems/09_agent_evaluation.md) và [Secure AI System Design](./08_secure_ai_system_design.md).

## Vì sao pretraining chưa đủ

Mô hình ngôn ngữ tiền huấn luyện tối ưu xác suất token tiếp theo:

\[
\min_\theta\; -\sum_t \log P_\theta(x_t\mid x_{<t})
\]

Objective này giúp mô hình học cấu trúc ngôn ngữ và nhiều pattern về thế giới, nhưng không trực tiếp yêu cầu nó:

```text
làm đúng instruction
ưu tiên nguồn đáng tin
thừa nhận bất định
tránh hành động nguy hiểm
xuất JSON hợp lệ
dùng tool đúng quyền
```

Post-training biến khả năng nền thành hành vi trợ lý hoặc hành vi tác vụ cụ thể.

## Supervised Fine-Tuning

**Tinh chỉnh có giám sát (Supervised Fine-Tuning — SFT)** học từ cặp instruction–response mẫu:

\[
L_{SFT}=-\sum_t\log P_\theta(y_t\mid x,y_{<t})
\]

SFT hiệu quả khi có demonstration rõ và nhất quán. Nó dạy trực tiếp pattern như:

```text
câu hỏi → câu trả lời phù hợp
input có cấu trúc → output đúng schema
case mơ hồ → hỏi lại
```

Nhưng SFT bị giới hạn bởi coverage và chất lượng demonstration. Những behavior không xuất hiện hoặc xuất hiện sai trong data khó được học đúng.

## Dữ liệu preference

Khi có nhiều output hợp lệ, người đánh giá có thể chọn:

```text
A tốt hơn B
```

Từ đó hệ thống học preference tương đối thay vì một đáp án duy nhất. Tuy nhiên preference data phản ánh rubric, annotator population và distribution của prompt được thu thập.

Các bias thường gặp:

- thích câu dài hơn dù không chính xác hơn;
- ưu tiên phong cách lịch sự hơn nội dung;
- thiên lệch văn hóa/ngôn ngữ;
- chấm theo độ tự tin thay vì bằng chứng.

## RLHF

Pipeline khái niệm phổ biến:

```text
SFT model
→ thu thập cặp preference
→ huấn luyện reward model
→ tối ưu policy theo reward
→ kiểm soát độ lệch khỏi reference model
```

Một objective đơn giản hóa có thể gồm reward và penalty KL:

\[
J(\pi)=\mathbb{E}[r(x,y)]-\beta D_{KL}(\pi\|\pi_{ref})
\]

`β` kiểm soát mức policy được phép đi xa khỏi reference. Nếu optimization quá mạnh trong khi reward model không hoàn hảo, reward có thể tăng nhưng chất lượng thật giảm.

## DPO và tối ưu preference trực tiếp

Các phương pháp kiểu **Direct Preference Optimization (DPO)** dùng cặp chosen/rejected để tối ưu policy trực tiếp, tránh một số complexity của online RL. Operationally, DPO có thể đơn giản hơn nhưng không làm biến mất các vấn đề về chất lượng preference data, distribution shift hay specification.

Vì vậy “không có reward model riêng” không đồng nghĩa “không còn proxy objective”.

## Best-of-N và rejection sampling

Một cách cải thiện inference mà không cập nhật weights:

```text
sinh N candidate
→ chấm bằng verifier / reward model
→ chọn candidate tốt nhất
```

Xác suất tìm được output tốt có thể tăng khi `N` tăng, nhưng chi phí inference cũng tăng gần tương ứng. Nếu verifier có blind spot, search pressure sẽ khai thác chính blind spot đó.

## Critique và revision

Pattern phổ biến:

```text
sinh bản nháp
→ critique theo rubric
→ sửa lại
```

Self-critique có thể giúp khi lỗi dễ nhận diện sau khi đã có candidate. Tuy nhiên cùng một mô hình có thể không phát hiện được lỗi do chính nó tạo ra. Verifier độc lập, công cụ xác định hoặc human review cung cấp tín hiệu độc lập hơn.

## Rule-based và constitutional-style guidance

Có thể biểu diễn principle cấp cao rồi yêu cầu model tự critique/revise theo principle đó. Cách này giúp scale feedback và làm policy dễ đọc hơn.

Nhưng principle bằng ngôn ngữ tự nhiên vẫn được model diễn giải. Nó không thay thế:

```text
authorization
schema validation
rate limit
financial limit
network policy
sandbox
```

## Outcome supervision và process supervision

**Giám sát kết quả (outcome supervision)** đánh giá output cuối. **Giám sát quá trình (process supervision)** đánh giá các bước trung gian hoặc hành động.

Với agent, process-level check đặc biệt quan trọng vì một trajectory có thể chứa bước nguy hiểm dù final answer trông đúng.

Nên ưu tiên trạng thái và hành động có thể quan sát:

```text
tool call
state transition
permission result
external side effect
verifier outcome
```

thay vì giả định rằng textual chain-of-thought phản ánh chính xác cơ chế bên trong.

## Verifier

Verifier mạnh khi correctness có cấu trúc kiểm tra được:

- unit test;
- type checker;
- theorem prover;
- calculator;
- citation support;
- schema validator;
- business rule;
- policy engine.

Pattern production:

```text
mô hình đề xuất
→ verifier kiểm tra
→ policy/authorization xác nhận
→ executor thực thi
→ outcome được kiểm lại
```

Verifier không nhất thiết là AI. Nhiều verifier tốt nhất là deterministic.

## Scalable oversight

Khi số lượng output vượt khả năng review thủ công, oversight phải được phân tầng:

```text
automated validator cho tất cả request
→ sample audit
→ model-based judge cho case trung bình
→ human escalation cho case rủi ro cao
```

Thiết kế này cần đo cả false negative lẫn false positive của từng tầng.

## Human-in-the-Loop không tự động tạo an toàn

Human review có thể thất bại vì:

- alert quá nhiều;
- reviewer thiếu context;
- automation bias;
- deadline quá ngắn;
- UI chỉ hiển thị summary do model tạo;
- người duyệt không có quyền thật để chặn action.

Một approval tốt nên hiển thị structured action và dữ liệu nguồn quan trọng, sau đó backend re-authorize trước khi thực thi.

## Confidence-based escalation

Có thể route case khó sang model mạnh hơn hoặc con người dựa trên uncertainty/risk signal. Tuy nhiên xác suất token thô của LLM không phải thước đo confidence đáng tin cho mọi task.

Escalation signal có thể kết hợp:

- verifier failure;
- retrieval quality;
- policy risk;
- model disagreement;
- calibrated classifier;
- domain-specific uncertainty.

## Over-refusal và harmful compliance

Alignment evaluation phải đo đồng thời hai phía:

```text
harmful compliance thấp
và
over-refusal thấp
```

Nếu chỉ tối ưu refusal rate, hệ thống có thể trở nên vô dụng. Nếu chỉ tối ưu helpfulness, nó có thể thực hiện request không phù hợp.

Đây là bài toán precision–recall dưới policy distribution, không phải chỉ “càng từ chối nhiều càng an toàn”.

## Distribution shift

Behavior được học từ preference data có thể suy giảm khi gặp:

- ngôn ngữ mới;
- domain mới;
- prompt dài hoặc lạ;
- adversarial wording;
- tool mới;
- workflow dài hạn.

Vì vậy alignment cần regression suite và red-team set theo production distribution thật.

## Căn chỉnh mô hình và căn chỉnh hệ thống

Cần phân biệt rõ:

```text
model alignment
→ định hình output và preference của mô hình

system alignment
→ giới hạn quyền, trạng thái, workflow, verifier và human approval
```

Model alignment cải thiện xác suất hành vi đúng. System alignment quyết định mức hậu quả tối đa nếu mô hình vẫn sai.

## Oversight cho agent dài hạn

Một agent có quyền hành động nên có checkpoint rõ:

```text
mục tiêu
→ kế hoạch
→ validation
→ tool call
→ authorization
→ side-effect approval
→ execution
→ outcome verification
→ state update
```

Không nên chỉ dựa vào câu cuối “tôi đã hoàn thành nhiệm vụ”.

## Mô hình triển khai production

Một stack căn chỉnh thực dụng có thể gồm:

```text
base model
→ SFT / preference tuning
→ system/developer policy
→ retrieval grounding
→ tool scope hẹp
→ validator / verifier
→ human approval theo risk
→ monitoring / red-team feedback
→ release gate
```

Mỗi layer giải một loại failure khác nhau; không có layer nào thay thế hoàn toàn các layer còn lại.

## Evaluation và release gate

Bộ đánh giá nên bao gồm:

- helpfulness;
- factuality;
- instruction hierarchy;
- harmful compliance;
- over-refusal;
- jailbreak resistance;
- multilingual/domain slice;
- tool misuse;
- long-horizon agent scenario;
- cost/latency regression;
- security boundary regression.

Một thay đổi alignment không nên được promote chỉ vì một tổng điểm duy nhất tăng.

## Trade-off

Các kỹ thuật alignment có thể làm tăng latency, chi phí, refusal, complexity và operational burden. Verifier nhiều tầng làm hệ thống chậm hơn nhưng tăng khả năng phát hiện lỗi. Human approval giảm autonomy nhưng phù hợp cho action có impact lớn.

Trade-off phải gắn với risk class, không áp một cấu hình cho mọi task.

## Failure mode thường gặp

**Reward overoptimization.** Reward model tăng nhưng human quality giảm.

**Preference bias.** Dataset preference ưu tiên style hơn correctness.

**Over-refusal.** Policy quá rộng chặn nhiều request hợp lệ.

**Verifier đồng sai.** Model và judge cùng chia sẻ blind spot.

**Human rubber-stamp.** Người duyệt không đủ context hoặc thời gian.

**Model alignment bị nhầm với access control.** Model vẫn có tool permission quá rộng.

**Regression ngoài distribution.** Alignment tốt ở tiếng Anh nhưng kém ở ngôn ngữ/domain khác.

## Mô hình tư duy

> **Alignment techniques định hình hành vi; oversight kiểm tra hành vi; security architecture kiểm soát quyền và hậu quả.**

Ba lớp này liên quan nhưng không thể thay thế lẫn nhau.

## Những nhầm lẫn thường gặp

### “RLHF căn chỉnh mô hình với toàn bộ giá trị con người”

Không. RLHF tối ưu theo preference data và reward model trong một distribution hữu hạn.

### “Constitutional rule là hard constraint”

Không nếu rule chỉ được model diễn giải bằng ngôn ngữ tự nhiên.

### “Có human approval là chắc chắn an toàn”

Không. Chất lượng approval phụ thuộc workload, UI, context và authority của reviewer.

## Liên kết kiến thức

Xem [Căn chỉnh AI](./01_alignment_and_objective_specification.md), [Reward Misspecification](./02_reward_misspecification_and_goal_misgeneralization.md), [SFT](../08_large_language_models/07_supervised_fine_tuning.md), [RLHF](../08_large_language_models/08_rlhf.md), [DPO](../08_large_language_models/09_preference_optimization_and_dpo.md), [Agent Evaluation](../10_agents_and_ai_systems/09_agent_evaluation.md), [Reliability](../18_evaluation_reliability_interpretability/07_reliability_engineering.md), [Prompt Injection](./03_prompt_injection_and_jailbreaks.md) và [Secure AI System Design](./08_secure_ai_system_design.md).