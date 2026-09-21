# Nền tảng an toàn AI

**An toàn AI (AI Safety / AI 안전)** nghiên cứu và kỹ nghệ cách xây dựng hệ thống AI sao cho hành vi vẫn nằm trong phạm vi được chấp nhận, có thể giám sát, có thể giới hạn hậu quả và có thể phục hồi khi thất bại. An toàn không đồng nghĩa với bảo mật, căn chỉnh hay quản trị, dù các lĩnh vực này liên kết chặt chẽ.

## Kiến thức cần có trước

Nên đọc [Agent Systems](../10_agents_and_ai_systems/README.md), [AI System Design](../15_ai_engineering/10_ai_system_design.md), [Evaluation & Reliability](../18_evaluation_reliability_interpretability/README.md) và [Incident Response](../16_mlops_and_llmops/09_incident_response_and_lifecycle.md).

## Phân biệt Safety, Security, Alignment và Governance

```text
An toàn (safety)
→ hệ thống có thể gây hậu quả nguy hiểm bằng cách nào?

Bảo mật (security)
→ attacker có thể khai thác hệ thống bằng cách nào?

Căn chỉnh (alignment)
→ mục tiêu/hành vi có phù hợp ý định và ràng buộc không?

Quản trị (governance)
→ ai chịu trách nhiệm, ai được phê duyệt, quy trình nào kiểm soát vòng đời?
```

Một prompt injection là vấn đề bảo mật nhưng có thể dẫn tới hậu quả an toàn. Một reward sai có thể tạo rủi ro an toàn dù không có attacker.

## Từ lỗi mô hình tới hậu quả thực tế

Không phải mọi lỗi dự đoán đều tạo cùng mức rủi ro. Một chuỗi gây hại có thể được mô hình hóa:

```text
lỗi mô hình
→ quyết định sai
→ hành động hoặc thông tin sai
→ người dùng/hệ thống tin và sử dụng
→ hậu quả
```

Ví dụ trợ lý y tế:

```text
failure mode: liều lượng bị hallucination
→ hazard: người dùng tin là thật
→ exposure: không có cảnh báo hoặc review
→ harm: dùng thuốc sai
```

Điều này giải thích vì sao UI, verifier, permission và human review có thể giảm risk ngay cả khi model error chưa về 0.

## Risk và residual risk

Một trực giác đơn giản:

\[
Risk\approx P(Harm)\times Severity(Harm)
\]

Nhưng trong hệ thống mở, xác suất thường khó biết chính xác. Production risk assessment nên xem thêm:

- mức phơi nhiễm;
- khả năng phát hiện;
- khả năng đảo ngược;
- phạm vi ảnh hưởng;
- thời gian tồn tại của lỗi;
- khả năng attacker thích nghi;
- độ tin cậy của evidence.

Sau khi áp dụng control vẫn còn **rủi ro còn lại (residual risk)**. Quyết định deploy phải dựa trên residual risk, không phải giả định rằng control đã loại bỏ toàn bộ rủi ro.

## Hazard và failure mode

**Mối nguy (hazard)** là điều kiện có thể dẫn đến harm. **Kiểu thất bại (failure mode)** là cách hệ thống không đáp ứng contract.

Một failure mode có thể không nguy hiểm trong use case này nhưng nguy hiểm trong use case khác. Ví dụ output chậm 3 giây có thể chấp nhận ở công cụ tóm tắt, nhưng nguy hiểm trong hệ thống điều khiển thời gian thực.

## Safety case

Thay vì tuyên bố “mô hình an toàn”, nên xây một **lập luận an toàn (safety case)**:

```text
claim
→ assumption
→ evidence
→ control
→ monitoring
→ residual risk
```

Ví dụ:

```text
claim: agent không được tự chuyển tiền vượt hạn mức
assumption: mọi giao dịch đi qua payment tool chuẩn
control: backend limit + authorization + approval
validation: integration test + adversarial scenario
monitoring: audit log + alert vượt ngưỡng
residual risk: bug ở payment service hoặc credential compromise
```

Safety là thuộc tính của cả hệ thống dưới những điều kiện xác định, không phải nhãn tuyệt đối của một checkpoint.

## Capability, autonomy và attack surface

Khi capability tăng, bề mặt hậu quả cũng tăng. Một chatbot chỉ trả văn bản khác hoàn toàn agent có quyền:

- đọc file;
- gọi database;
- gửi email;
- sửa code;
- tạo giao dịch;
- lưu memory dài hạn.

Mức tự chủ (autonomy) là một lựa chọn kiến trúc. Không nên tăng autonomy chỉ vì model đủ khả năng; phải tăng đồng thời verifier, permission, state management, observability và recovery.

## Tính đảo ngược

Một nguyên tắc production mạnh là ưu tiên hành động có thể đảo ngược khi uncertainty cao.

```text
nháp email → có thể review
xóa file vĩnh viễn → khó đảo ngược
đề xuất lệnh → có thể kiểm tra
thực thi payment → hậu quả cao
```

Hành động càng khó đảo ngược, control trước execution càng cần mạnh.

## Specification problem

Ý định con người thường giàu hơn mục tiêu có thể đo. Nếu hệ thống tối ưu proxy, nó có thể tìm lỗ hổng giữa proxy và mục tiêu thật.

Ví dụ:

```text
mục tiêu thật: người dùng nhận nội dung hữu ích
proxy: watch time tối đa
```

Tối ưu proxy có thể tăng watch time bằng nội dung gây nghiện. Xem sâu hơn ở [Căn chỉnh AI](./01_alignment_and_objective_specification.md) và [Reward Misspecification](./02_reward_misspecification_and_goal_misgeneralization.md).

## Distribution shift

Control được xác minh trên distribution này có thể thất bại khi:

- ngôn ngữ thay đổi;
- user behavior thay đổi;
- tool mới được thêm;
- corpus RAG thay đổi;
- provider model thay đổi;
- attacker học cách thích nghi.

Do đó safety không kết thúc ở pre-release benchmark. Nó cần monitoring và regression evaluation liên tục.

## Defense in depth

Không nên dựa vào một lớp duy nhất:

```text
hành vi mô hình
+ kiểm tra input
+ quyền hạn
+ sandbox
+ schema công cụ
+ verifier
+ human approval
+ monitoring
+ incident response
```

Mỗi lớp giảm một loại failure khác nhau. Nếu một lớp bị bypass, các lớp sau vẫn phải giới hạn hậu quả.

## Fail-safe và fail-closed

Với hành động rủi ro cao:

```text
không xác minh được
→ không thực thi
```

là lựa chọn hợp lý. Nhưng fail-closed làm giảm availability. Use case rủi ro thấp có thể chọn degraded fallback thay vì chặn toàn bộ.

Không có chính sách fail-open/fail-closed đúng cho mọi hệ thống; lựa chọn phải gắn với impact.

## Human factors

Output trôi chảy có thể tạo **thiên lệch tự động hóa (automation bias)**: người dùng tin kết quả hơn mức evidence cho phép.

Safety engineering phải xem cả giao diện và quy trình:

- nguồn có được hiển thị không;
- uncertainty có được truyền đạt không;
- approval có hiển thị action thật không;
- người review có đủ context không;
- warning có bị bỏ qua vì xuất hiện quá nhiều không.

## Evaluation cho an toàn

Bộ test nên gồm:

```text
known harmful scenarios
misuse / abuse
prompt injection
edge cases
long-horizon agent behavior
tool permission failures
recovery / fallback
multilingual/domain slices
```

Không có finite test suite nào chứng minh an toàn tuyệt đối. Mục tiêu là tăng coverage và evidence theo risk model.

## Red teaming

Red teaming chủ động tìm failure thay vì chờ production phát hiện. Kết quả red team có giá trị khi được chuyển thành:

```text
failure taxonomy
→ architecture fix
→ regression test
→ release gate
→ monitoring signal
```

Chỉ lưu “prompt đã jailbreak được” mà không thay đổi control thì chưa hoàn thành vòng học.

## Mô hình triển khai production

Một hệ thống rủi ro vừa/cao có thể theo flow:

```text
request
→ authentication
→ input validation
→ model/retrieval/tool reasoning
→ policy + authorization
→ verifier
→ approval nếu cần
→ execution
→ outcome verification
→ durable state
→ audit / monitoring
```

Mỗi bước nên có owner, failure behavior và trace rõ ràng.

## Trade-off

Safety control thường đánh đổi:

- latency;
- cost;
- autonomy;
- tỷ lệ tự động hóa;
- false positive refusal;
- developer velocity.

Mục tiêu không phải tối đa mọi control, mà là chọn control tương ứng risk class và khả năng phục hồi.

## Failure mode thường gặp

**Safe model, unsafe application.** Tool permission quá rộng hoặc UI khiến user overtrust.

**Benchmark safety overfitting.** Tốt trên test set nhưng yếu với ngôn ngữ hoặc attack mới.

**Fallback không được test.** Chỉ tồn tại trong diagram.

**Approval sau side effect.** Human review đến quá muộn.

**Monitoring chỉ đo HTTP 200.** Không phát hiện silent quality/safety degradation.

**Không có kill switch.** Không thể vô hiệu hóa capability nhanh khi incident xảy ra.

## Mô hình tư duy

> **An toàn AI = nhận diện mối nguy → giới hạn capability → kiểm chứng hành vi → giới hạn hậu quả → quan sát production → phục hồi khi thất bại.**

## Những nhầm lẫn thường gặp

### “Mô hình an toàn = ứng dụng an toàn”

Không. Permission, retrieval, tool, UI và workflow có thể làm ứng dụng nguy hiểm dù model tương đối tốt.

### “Security và safety là một”

Không. Security tập trung vào khai thác có chủ đích; safety bao gồm cả lỗi không có attacker.

### “Một benchmark đủ chứng minh an toàn”

Không. Safety phụ thuộc context, distribution, tool và deployment.

## Liên kết kiến thức

Xem [Căn chỉnh AI](./01_alignment_and_objective_specification.md), [Prompt Injection](./03_prompt_injection_and_jailbreaks.md), [Adversarial ML](./04_adversarial_machine_learning.md), [Reliability](../18_evaluation_reliability_interpretability/07_reliability_engineering.md), [Reliable Agent Design](../10_agents_and_ai_systems/10_reliable_agent_design.md), [AI System Design](../15_ai_engineering/10_ai_system_design.md) và [Incident Response](../16_mlops_and_llmops/09_incident_response_and_lifecycle.md).