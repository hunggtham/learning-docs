# Căn chỉnh AI và đặc tả mục tiêu

> **Mạch đọc:** [README](./README.md) là bản đồ owner của **Căn chỉnh AI và đặc tả mục tiêu**; nhìn vào vị trí đó trước để biết file này đang phục vụ nhánh kiến thức nào. **Kiến thức cần có trước** mở đối tượng chính của file và câu hỏi cần theo dõi; sau đó sang **Khoảng cách giữa ý định và mục tiêu tối ưu hóa** để mở câu hỏi trung tâm cho phần kế tiếp. Cách đi này giữ lại điểm tựa của section đầu và cho biết kết luận sẽ được dùng ở đâu, thay vì dừng ở định nghĩa đầu tiên.

**Căn chỉnh AI (AI alignment / AI 정렬)** nghiên cứu và kỹ nghệ cách làm cho hành vi của hệ thống AI phù hợp với mục tiêu, ý định, ràng buộc và quyền hạn mà con người thực sự mong muốn. Vấn đề cốt lõi là mục tiêu thật thường giàu ngữ cảnh, khó đo trực tiếp và thay đổi theo tình huống, trong khi hệ thống chỉ tối ưu những tín hiệu có thể biểu diễn bằng dữ liệu, hàm mất mát, phần thưởng, lời nhắc hoặc bộ đánh giá.

## Kiến thức cần có trước

Nên đọc [LLM Post-Training](../08_large_language_models/README.md), [Agent Planning](../10_agents_and_ai_systems/03_planning_and_task_decomposition.md), [Evaluation](../18_evaluation_reliability_interpretability/00_evaluation_foundations.md) và [Safety Foundations](./00_ai_safety_foundations.md).

> **Chuyển mạch:** Trong **Căn chỉnh AI và đặc tả mục tiêu**, **Khoảng cách giữa ý định và mục tiêu tối ưu hóa** tiếp nhận điểm tựa từ **Kiến thức cần có trước** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Căn chỉnh bên ngoài và căn chỉnh bên trong** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

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

> **Chuyển mạch:** Ở chặng này của **Căn chỉnh AI và đặc tả mục tiêu**, **Căn chỉnh bên ngoài và căn chỉnh bên trong** tiếp nhận điểm tựa từ **Khoảng cách giữa ý định và mục tiêu tối ưu hóa** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Đặc tả mục tiêu như một bài toán nhiều mục tiêu** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Căn chỉnh bên ngoài và căn chỉnh bên trong

Một cách phân biệt hữu ích:

```text
căn chỉnh bên ngoài (outer alignment)
→ reward/objective có đại diện đúng điều ta muốn không?

căn chỉnh bên trong (inner alignment)
→ mô hình học được chiến lược nào và chiến lược đó có tiếp tục đúng khi khái quát hóa không?
```

Trong kỹ nghệ môi trường vận hành (production / 운영 환경), có thể chuyển thành hai câu hỏi:

```text
1. Ta đã đặc tả đúng mục tiêu chưa?
2. Hệ thống có tiếp tục theo mục tiêu đó ngoài phân phối huấn luyện không?
```

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Căn chỉnh AI và đặc tả mục tiêu**, **Đặc tả mục tiêu như một bài toán nhiều mục tiêu** tiếp nhận điểm tựa từ **Căn chỉnh bên ngoài và căn chỉnh bên trong** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Goodhart và áp lực tối ưu hóa** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Đặc tả mục tiêu như một bài toán nhiều mục tiêu

Một hệ thống môi trường vận hành (production / 운영 환경) hiếm khi chỉ có một mục tiêu. Nó thường đồng thời cần:

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

thì các trọng số `w_i` chính là chính sách sự đánh đổi (trade-off / 트레이드오프). Chúng không phải chân lý khách quan và có thể tạo hành vi cực đoan khi một thành phần chiếm ưu thế.

Một số yêu cầu nên là **ràng buộc cứng (hard constraint)** thay vì chỉ là thành phần mềm trong mục tiêu (objective / 목표):

```text
quyền truy cập
hạn mức tài chính
schema hợp lệ
quy định pháp lý
phạm vi công cụ được phép dùng
```

> **Chuyển mạch:** Trong **Căn chỉnh AI và đặc tả mục tiêu**, **Goodhart và áp lực tối ưu hóa** tiếp nhận điểm tựa từ **Đặc tả mục tiêu như một bài toán nhiều mục tiêu** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Mục tiêu không chỉ nằm trong reward** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Goodhart và áp lực tối ưu hóa

Khi một thước đo trở thành mục tiêu tối ưu hóa, hệ thống có động lực khai thác những trường hợp mà thước đo không còn đại diện tốt cho mục tiêu thật. Đây là trực giác của **Định luật Goodhart (Goodhart's Law)**.

Trong AI, hiện tượng này xuất hiện dưới nhiều dạng:

- tối ưu click nhưng giảm chất lượng trải nghiệm;
- tối ưu reward mô hình (model / 모델) nhưng làm chất lượng thật giảm;
- vượt benchmark bằng shortcut;
- tác nhân (agent / 에이전트) tuyên bố “đã hoàn thành” vì success tín hiệu (signal / 신호) yếu.

> **Chuyển mạch:** Ở chặng này của **Căn chỉnh AI và đặc tả mục tiêu**, **Mục tiêu không chỉ nằm trong reward** tiếp nhận điểm tựa từ **Goodhart và áp lực tối ưu hóa** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Mơ hồ và xung đột mục tiêu** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Mục tiêu không chỉ nằm trong reward

Với LLM và tác nhân (agent / 에이전트), mục tiêu thực tế có thể được mã hóa đồng thời ở nhiều tầng:

```text
trọng số mô hình
system/developer instruction
workflow graph
quyền công cụ
policy engine
success verifier
human approval
```

Vì vậy không nên coi alignment chỉ là một bài toán huấn luyện mô hình. Nhiều bảo đảm môi trường vận hành (production / 운영 환경) mạnh nhất đến từ thiết kế hệ thống bên ngoài mô hình.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Căn chỉnh AI và đặc tả mục tiêu**, **Mơ hồ và xung đột mục tiêu** tiếp nhận điểm tựa từ **Mục tiêu không chỉ nằm trong reward** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Phân cấp quyền hạn** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Mơ hồ và xung đột mục tiêu

Yêu cầu của người dùng có thể thiếu thông tin hoặc xung đột với chính sách cấp cao hơn. Một hệ thống được căn chỉnh tốt không nên luôn “đoán và làm tiếp”. Tùy rủi ro, nó có thể:

```text
hỏi lại
chọn hành động có thể đảo ngược
hạ mức tự chủ
chuyển sang human review
fail closed với hành động có đặc quyền
```

> **Chuyển mạch:** Trong **Căn chỉnh AI và đặc tả mục tiêu**, **Phân cấp quyền hạn** tiếp nhận điểm tựa từ **Mơ hồ và xung đột mục tiêu** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Căn chỉnh trong tác vụ dài hạn** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Phân cấp quyền hạn

Trong ứng dụng LLM, một mô hình tư duy hữu ích là:

```text
chính sách hệ thống / nhà cung cấp
→ chỉ dẫn của ứng dụng
→ yêu cầu người dùng
→ nội dung bên ngoài không đáng tin
```

Nhưng phân cấp này chỉ giúp định hình hành vi mô hình. Với hành động có quyền, backend vẫn phải tự kiểm tra authorization. [Prompt Injection](./03_prompt_injection_and_jailbreaks.md) giải thích vì sao natural-language hierarchy không phải ranh giới bảo mật đủ mạnh.

> **Chuyển mạch:** Ở chặng này của **Căn chỉnh AI và đặc tả mục tiêu**, **Căn chỉnh trong tác vụ dài hạn** tiếp nhận điểm tựa từ **Phân cấp quyền hạn** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Khả năng sửa sai và kiểm soát** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Căn chỉnh trong tác vụ dài hạn

Tác nhân (agent / 에이전트) dài hạn có thể trôi khỏi mục tiêu dù từng bước riêng lẻ trông hợp lý. môi trường vận hành (production / 운영 환경) workflow nên duy trì:

```text
mục tiêu có cấu trúc
trạng thái hiện tại
điều kiện thành công
điều kiện dừng
ngân sách bước / chi phí
các hành động cấm
checkpoint phê duyệt
```

Không nên dùng transcript tự nhiên làm nguồn trạng thái duy nhất nếu workflow phải resume, thử lại (retry / 재시도) hoặc kiểm tra (audit / 감사).

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Căn chỉnh AI và đặc tả mục tiêu**, **Khả năng sửa sai và kiểm soát** tiếp nhận điểm tựa từ **Căn chỉnh trong tác vụ dài hạn** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Mô hình triển khai môi trường vận hành (production / 운영 환경)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Khả năng sửa sai và kiểm soát

Một hệ thống có thể kiểm soát tốt cần hỗ trợ:

- dừng tác vụ;
- thu hồi quyền;
- sửa mục tiêu;
- quay lui (rollback / 롤백);
- quan sát trạng thái (state / 상태);
- thay đổi chính sách (policy / 정책) mà không phải huấn luyện lại toàn bộ mô hình.

Đây là trực giác kỹ nghệ của **khả năng sửa sai (corrigibility)**: hệ thống không được “mắc kẹt” trong một tối ưu cũ đến mức chống lại sự can thiệp hợp lệ.

> **Chuyển mạch:** Trong **Căn chỉnh AI và đặc tả mục tiêu**, **Mô hình triển khai môi trường vận hành (production / 운영 환경)** tiếp nhận điểm tựa từ **Khả năng sửa sai và kiểm soát** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Đánh giá alignment** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Mô hình triển khai môi trường vận hành (production / 운영 환경)

Một mẫu (pattern / 패턴) đáng tin cậy:

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

> **Chuyển mạch:** Ở chặng này của **Căn chỉnh AI và đặc tả mục tiêu**, **Đánh giá alignment** tiếp nhận điểm tựa từ **Mô hình triển khai môi trường vận hành (production / 운영 환경)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Sự đánh đổi (trade-off / 트레이드오프)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Đánh giá alignment

Không nên chỉ đo “mô hình (model / 모델) có nghe lời không”. Bộ đánh giá cần bao gồm:

- chỉ dẫn xung đột;
- mục tiêu mơ hồ;
- trường hợp có proxy dễ khai thác;
- phân phối mới;
- tác vụ dài hạn;
- công cụ (tool / 도구) use;
- over-refusal;
- harmful compliance;
- khả năng dừng/sửa giữa chừng;
- đa ngôn ngữ và lĩnh vực (domain / 도메인) slice.

Alignment evaluation phải nối với [Behavioral Evaluation](../18_evaluation_reliability_interpretability/05_ai_testing_and_behavioral_evaluation.md) và [Red Teaming](../18_evaluation_reliability_interpretability/06_red_teaming_and_adversarial_evaluation.md).

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Căn chỉnh AI và đặc tả mục tiêu**, **Sự đánh đổi (trade-off / 트레이드오프)** tiếp nhận điểm tựa từ **Đánh giá alignment** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Dạng thất bại (failure mode / 실패 모드) thường gặp** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Sự đánh đổi (trade-off / 트레이드오프)

Tăng kiểm soát thường làm giảm ít nhất một trong các yếu tố: tốc độ, mức tự chủ, tỷ lệ tự động hóa, trải nghiệm liền mạch hoặc chi phí vận hành. môi trường vận hành (production / 운영 환경) thiết kế (design / 설계) phải chọn mức autonomy tương ứng với impact của lỗi.

Một trợ lý tìm tài liệu có thể được phép thử lại tự động. Một tác nhân (agent / 에이전트) tạo giao dịch tài chính nên có chính sách (policy / 정책), hạn mức và approval nghiêm ngặt hơn.

> **Chuyển mạch:** Trong **Căn chỉnh AI và đặc tả mục tiêu**, **Dạng thất bại (failure mode / 실패 모드) thường gặp** tiếp nhận điểm tựa từ **Sự đánh đổi (trade-off / 트레이드오프)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Mô hình tư duy** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Dạng thất bại (failure mode / 실패 모드) thường gặp

**Proxy quá hẹp.** chỉ số (metric / 지표) tăng nhưng kết quả (outcome / 결과) người dùng giảm.

**Soft ràng buộc (constraint / 제약조건) thay cho hard điều khiển (control / 제어).** Permission hoặc giới hạn tiền chỉ được ghi trong prompt/reward.

**Mục tiêu thay đổi nhưng trạng thái (state / 상태) cũ vẫn tiếp tục.** Long-running tác nhân (agent / 에이전트) không nhận hoặc không phản ánh cập nhật mới.

**Mô hình tự đánh giá thành công của chính nó.** Không có verifier độc lập.

**Human approval mang tính hình thức.** Người duyệt thiếu thời gian hoặc ngữ cảnh (context / 맥락) và chỉ bấm đồng ý.

**Tối ưu một slice rồi gây regression slice khác.** Alignment dữ liệu (data / 데이터) quá hẹp so với môi trường vận hành (production / 운영 환경) phân phối (distribution / 분포).

> **Chuyển mạch:** Ở chặng này của **Căn chỉnh AI và đặc tả mục tiêu**, **Mô hình tư duy** gom các mảnh từ **Dạng thất bại (failure mode / 실패 모드) thường gặp** thành một kết luận có thể mang sang phần kế tiếp. Từ đây, **Những nhầm lẫn thường gặp** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Mô hình tư duy

> **Alignment là giảm khoảng cách giữa điều hệ thống đang tối ưu và điều con người thực sự muốn, dưới những ràng buộc và quyền hạn có thể kiểm chứng.**

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Căn chỉnh AI và đặc tả mục tiêu**, **Mô hình tư duy** đã nêu tiêu chí phân biệt, còn **Những nhầm lẫn thường gặp** dùng tiêu chí đó để soi ranh giới và điểm dễ nhầm. Từ đây, **Liên kết kiến thức** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Những nhầm lẫn thường gặp

### “Alignment = mô hình lịch sự”

Không. Giọng điệu chỉ là bề mặt; alignment liên quan mục tiêu, ràng buộc, generalization và quyền hành động.

### “RLHF giải quyết alignment”

Không. RLHF chỉ là một kỹ thuật định hình preference và vẫn phụ thuộc reward mô hình (model / 모델), dữ liệu (data / 데이터) và evaluation.

### “Viết mục tiêu rõ trong prompt là đủ”

Không. Prompt là ngôn ngữ tự nhiên và không thay thế verifier, chính sách (policy / 정책) engine hay authorization.

> **Chuyển mạch:** Trong **Căn chỉnh AI và đặc tả mục tiêu**, **Những nhầm lẫn thường gặp** đã nêu tiêu chí phân biệt, còn **Liên kết kiến thức** dùng tiêu chí đó để soi ranh giới và điểm dễ nhầm. Phần còn lại của file dùng kết quả này để khép lại mạch giải thích.

## Liên kết kiến thức

Xem [Reward Misspecification và Goal Misgeneralization](./02_reward_misspecification_and_goal_misgeneralization.md), [SFT](../08_large_language_models/07_supervised_fine_tuning.md), [RLHF](../08_large_language_models/08_rlhf.md), [DPO](../08_large_language_models/09_preference_optimization_and_dpo.md), [Agent Evaluation](../10_agents_and_ai_systems/09_agent_evaluation.md), [Reliability](../18_evaluation_reliability_interpretability/07_reliability_engineering.md) và [Secure AI System Design](./08_secure_ai_system_design.md).

> **Bàn giao:** Sau **Liên kết kiến thức**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](./README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
