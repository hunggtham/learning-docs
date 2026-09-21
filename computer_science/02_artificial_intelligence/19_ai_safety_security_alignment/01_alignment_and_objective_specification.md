# Căn chỉnh AI và đặc tả mục tiêu

**Căn chỉnh AI (AI alignment / AI 정렬)** nghiên cứu và kỹ nghệ cách làm cho hành vi của hệ thống AI phù hợp với mục tiêu, ý định, ràng buộc và quyền hạn mà con người thực sự mong muốn. Vấn đề cốt lõi là mục tiêu thật thường giàu ngữ cảnh, khó đo trực tiếp và thay đổi theo tình huống, trong khi hệ thống chỉ tối ưu những tín hiệu có thể biểu diễn bằng dữ liệu, hàm mất mát, phần thưởng, lời nhắc hoặc bộ đánh giá.

## Kiến thức cần có trước

Nên đọc [LLM Post-Training](../08_large_language_models/README.md), [Agent Planning](../10_agents_and_ai_systems/03_planning_and_task_decomposition.md), [Evaluation](../18_evaluation_reliability_interpretability/00_evaluation_foundations.md) và [Safety Foundations](./00_ai_safety_foundations.md).

## Khoảng cách giữa ý định và mục tiêu tối ưu hóa

Một hệ thống thực tế thường có chuỗi:

```text
ý định của con người
→ mục tiêu có thể đo
→ dữ liệu / reward / policy
→ tối ưu hóa
→ hành vi đã học
→ hành vi trong production
```

Sai lệch có thể xuất hiện ở bất kỳ mũi tên nào. Nếu mục tiêu đo được chỉ là một đại diện (proxy) cho mục tiêu thật, áp lực tối ưu hóa có thể khai thác khoảng trống giữa hai thứ.

Ví dụ:

```text
mục tiêu thật: người dùng giải quyết được vấn đề
proxy: thời lượng phiên càng dài càng tốt
```

Một hệ thống tối ưu proxy có thể vô tình làm người dùng mất nhiều thời gian hơn thay vì giúp họ hoàn thành nhiệm vụ nhanh hơn.

## Căn chỉnh bên ngoài và căn chỉnh bên trong

Một cách phân biệt hữu ích:

```text
căn chỉnh bên ngoài (outer alignment)
→ reward/objective có đại diện đúng điều ta muốn không?

căn chỉnh bên trong (inner alignment)
→ mô hình học được chiến lược nào và chiến lược đó có tiếp tục đúng khi khái quát hóa không?
```

Trong kỹ nghệ production, có thể chuyển thành hai câu hỏi:

```text
1. Ta đã đặc tả đúng mục tiêu chưa?
2. Hệ thống có tiếp tục theo mục tiêu đó ngoài phân phối huấn luyện không?
```

## Đặc tả mục tiêu như một bài toán nhiều mục tiêu

Một hệ thống production hiếm khi chỉ có một mục tiêu. Nó thường đồng thời cần:

```text
độ hữu ích
độ đúng
an toàn
quyền riêng tư
độ trễ
chi phí
công bằng
khả năng giải thích
khả năng tuân thủ
```

Nếu gộp tất cả thành một số duy nhất:

\[
J(\theta)=\sum_i w_iJ_i(\theta)
\]

thì các trọng số `w_i` chính là chính sách trade-off. Chúng không phải chân lý khách quan và có thể tạo hành vi cực đoan khi một thành phần chiếm ưu thế.

Một số yêu cầu nên là **ràng buộc cứng (hard constraint)** thay vì chỉ là thành phần mềm trong objective:

```text
quyền truy cập
hạn mức tài chính
schema hợp lệ
quy định pháp lý
phạm vi công cụ được phép dùng
```

## Goodhart và áp lực tối ưu hóa

Khi một thước đo trở thành mục tiêu tối ưu hóa, hệ thống có động lực khai thác những trường hợp mà thước đo không còn đại diện tốt cho mục tiêu thật. Đây là trực giác của **Định luật Goodhart (Goodhart's Law)**.

Trong AI, hiện tượng này xuất hiện dưới nhiều dạng:

- tối ưu click nhưng giảm chất lượng trải nghiệm;
- tối ưu reward model nhưng làm chất lượng thật giảm;
- vượt benchmark bằng shortcut;
- agent tuyên bố “đã hoàn thành” vì success signal yếu.

## Mục tiêu không chỉ nằm trong reward

Với LLM và agent, mục tiêu thực tế có thể được mã hóa đồng thời ở nhiều tầng:

```text
trọng số mô hình
system/developer instruction
workflow graph
quyền công cụ
policy engine
success verifier
human approval
```

Vì vậy không nên coi alignment chỉ là một bài toán huấn luyện mô hình. Nhiều bảo đảm production mạnh nhất đến từ thiết kế hệ thống bên ngoài mô hình.

## Mơ hồ và xung đột mục tiêu

Yêu cầu của người dùng có thể thiếu thông tin hoặc xung đột với chính sách cấp cao hơn. Một hệ thống được căn chỉnh tốt không nên luôn “đoán và làm tiếp”. Tùy rủi ro, nó có thể:

```text
hỏi lại
chọn hành động có thể đảo ngược
hạ mức tự chủ
chuyển sang human review
fail closed với hành động có đặc quyền
```

## Phân cấp quyền hạn

Trong ứng dụng LLM, một mô hình tư duy hữu ích là:

```text
chính sách hệ thống / nhà cung cấp
→ chỉ dẫn của ứng dụng
→ yêu cầu người dùng
→ nội dung bên ngoài không đáng tin
```

Nhưng phân cấp này chỉ giúp định hình hành vi mô hình. Với hành động có quyền, backend vẫn phải tự kiểm tra authorization. [Prompt Injection](./03_prompt_injection_and_jailbreaks.md) giải thích vì sao natural-language hierarchy không phải ranh giới bảo mật đủ mạnh.

## Căn chỉnh trong tác vụ dài hạn

Agent dài hạn có thể trôi khỏi mục tiêu dù từng bước riêng lẻ trông hợp lý. Production workflow nên duy trì:

```text
mục tiêu có cấu trúc
trạng thái hiện tại
điều kiện thành công
điều kiện dừng
ngân sách bước / chi phí
các hành động cấm
checkpoint phê duyệt
```

Không nên dùng transcript tự nhiên làm nguồn trạng thái duy nhất nếu workflow phải resume, retry hoặc audit.

## Khả năng sửa sai và kiểm soát

Một hệ thống có thể kiểm soát tốt cần hỗ trợ:

- dừng tác vụ;
- thu hồi quyền;
- sửa mục tiêu;
- rollback;
- quan sát state;
- thay đổi policy mà không phải huấn luyện lại toàn bộ mô hình.

Đây là trực giác kỹ nghệ của **khả năng sửa sai (corrigibility)**: hệ thống không được “mắc kẹt” trong một tối ưu cũ đến mức chống lại sự can thiệp hợp lệ.

## Mô hình triển khai production

Một pattern đáng tin cậy:

```text
ý định / yêu cầu
→ chuẩn hóa task contract
→ mô hình đề xuất kế hoạch hoặc output
→ verifier / policy kiểm tra
→ authorization
→ approval khi cần
→ thực thi
→ xác minh kết quả
→ cập nhật state
→ ghi trace / feedback
```

Mô hình đóng vai trò tạo phương án; authority và kiểm soát hậu quả nằm ở các lớp có tính xác định hơn.

## Đánh giá alignment

Không nên chỉ đo “model có nghe lời không”. Bộ đánh giá cần bao gồm:

- chỉ dẫn xung đột;
- mục tiêu mơ hồ;
- trường hợp có proxy dễ khai thác;
- phân phối mới;
- tác vụ dài hạn;
- tool use;
- over-refusal;
- harmful compliance;
- khả năng dừng/sửa giữa chừng;
- đa ngôn ngữ và domain slice.

Alignment evaluation phải nối với [Behavioral Evaluation](../18_evaluation_reliability_interpretability/05_ai_testing_and_behavioral_evaluation.md) và [Red Teaming](../18_evaluation_reliability_interpretability/06_red_teaming_and_adversarial_evaluation.md).

## Trade-off

Tăng kiểm soát thường làm giảm ít nhất một trong các yếu tố: tốc độ, mức tự chủ, tỷ lệ tự động hóa, trải nghiệm liền mạch hoặc chi phí vận hành. Production design phải chọn mức autonomy tương ứng với impact của lỗi.

Một trợ lý tìm tài liệu có thể được phép thử lại tự động. Một agent tạo giao dịch tài chính nên có policy, hạn mức và approval nghiêm ngặt hơn.

## Failure mode thường gặp

**Proxy quá hẹp.** Metric tăng nhưng outcome người dùng giảm.

**Soft constraint thay cho hard control.** Permission hoặc giới hạn tiền chỉ được ghi trong prompt/reward.

**Mục tiêu thay đổi nhưng state cũ vẫn tiếp tục.** Long-running agent không nhận hoặc không phản ánh cập nhật mới.

**Mô hình tự đánh giá thành công của chính nó.** Không có verifier độc lập.

**Human approval mang tính hình thức.** Người duyệt thiếu thời gian hoặc context và chỉ bấm đồng ý.

**Tối ưu một slice rồi gây regression slice khác.** Alignment data quá hẹp so với production distribution.

## Mô hình tư duy

> **Alignment là giảm khoảng cách giữa điều hệ thống đang tối ưu và điều con người thực sự muốn, dưới những ràng buộc và quyền hạn có thể kiểm chứng.**

## Những nhầm lẫn thường gặp

### “Alignment = mô hình lịch sự”

Không. Giọng điệu chỉ là bề mặt; alignment liên quan mục tiêu, ràng buộc, generalization và quyền hành động.

### “RLHF giải quyết alignment”

Không. RLHF chỉ là một kỹ thuật định hình preference và vẫn phụ thuộc reward model, data và evaluation.

### “Viết mục tiêu rõ trong prompt là đủ”

Không. Prompt là ngôn ngữ tự nhiên và không thay thế verifier, policy engine hay authorization.

## Liên kết kiến thức

Xem [Reward Misspecification và Goal Misgeneralization](./02_reward_misspecification_and_goal_misgeneralization.md), [SFT](../08_large_language_models/07_supervised_fine_tuning.md), [RLHF](../08_large_language_models/08_rlhf.md), [DPO](../08_large_language_models/09_preference_optimization_and_dpo.md), [Agent Evaluation](../10_agents_and_ai_systems/09_agent_evaluation.md), [Reliability](../18_evaluation_reliability_interpretability/07_reliability_engineering.md) và [Secure AI System Design](./08_secure_ai_system_design.md).