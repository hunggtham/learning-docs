# Từ LLM tới AI Agent

Mô hình ngôn ngữ lớn tự nó chủ yếu là một mô hình chuỗi có điều kiện: nhận context và sinh đầu ra. **Tác nhân AI (AI Agent / 에이전트)** xuất hiện khi mô hình được đặt vào một vòng điều khiển có mục tiêu, trạng thái, quan sát và khả năng chọn hành động tác động ra bên ngoài mô hình.

Một mô hình tư duy tối giản:

```text
Mục tiêu
 ↓
Quan sát trạng thái hiện tại
 ↓
Chọn hành động tiếp theo
 ↓
Thực thi hành động / tool
 ↓
Quan sát kết quả
 ↓
Cập nhật trạng thái
 ↓
Tiếp tục hoặc dừng
```

Điểm quan trọng là **agent không đồng nghĩa LLM**. LLM có thể đóng vai policy, thành phần quyết định, planner hoặc parser; nhưng agent system còn cần runtime, tool, quyền, quản lý trạng thái, xử lý lỗi, điều kiện dừng và observability.

Xem nền về agent cổ điển tại [Intelligence, Agents and Environments](../00_foundations/02_intelligence_agents_and_environments.md).

## Agent như một policy có bộ nhớ và công cụ

Trong AI cổ điển, việc chọn hành động có thể mô hình hóa bằng:

\[
\pi(a\mid s)
\]

với `s` là trạng thái và `a` là hành động. Với LLM agent, trạng thái thường không phải một vector Markov đầy đủ. Nó có thể gồm structured state + selected context + tool result + history hội thoại.

LLM có thể nhận:

```text
system policy
+ mục tiêu người dùng
+ trạng thái hiện tại
+ tool schema
+ các observation trước
```

và tạo một trong hai loại đầu ra:

```text
phản hồi cuối
hoặc
request tool / action có cấu trúc
```

Runtime mới là thành phần thực sự thực thi hành động.

## Năng lực model và năng lực agent khác nhau

Một model có thể reasoning tốt nhưng agent vẫn thất bại vì:

- tool schema mơ hồ;
- state mất đồng bộ;
- action không idempotent;
- retry tạo side effect trùng;
- quyền quá rộng;
- vòng lặp không có stopping rule;
- kết quả tool không được validate;
- context overflow hoặc bị nhiễm.

Ngược lại, một model không phải mạnh nhất vẫn có thể tạo hệ thống đáng tin nếu workflow và action space được thiết kế tốt.

## Agent không chỉ là chatbot có nhiều prompt

Chatbot thường có pattern:

```text
user → model → text
```

Agent có vòng tương tác:

```text
mục tiêu user
→ model quyết định
→ hành động
→ kết quả môi trường
→ model quyết định
→ ...
```

Sự xuất hiện của **chuyển trạng thái bên ngoài (external state transition)** là khác biệt lớn. Khi agent gửi email, update database hoặc deploy code, đầu ra mô hình trở thành hành động có side effect thật.

## Tính tự chủ là một phổ liên tục

Không nên chia cứng “agent / không agent”. Có thể có nhiều mức:

```text
model chỉ trả text
→ model đề xuất action
→ user duyệt từng action
→ model tự chọn tool trong whitelist
→ model tự lập kế hoạch nhiều bước
→ model điều hành workflow dài hạn
```

Tự chủ càng cao thì yêu cầu về sandboxing, validation, budget, permission và monitoring càng cao.

## Môi trường của LLM Agent

Environment có thể là:

- hệ thống file;
- browser/web;
- database;
- source repository;
- enterprise API;
- operating system;
- SaaS application;
- môi trường robot vật lý.

**Quan sát (observation)** là thông tin runtime trả về sau một action.

Chất lượng agent phụ thuộc mạnh vào độ trung thực của observation. Nếu tool chỉ trả `success` thay vì trạng thái đã thay đổi cụ thể, mô hình khó quyết định bước sau.

## Không gian hành động

**Không gian hành động (action space)** là tập hành động hệ thống cho phép.

Ví dụ coding agent:

```text
read_file(path)
search_code(query)
edit_file(path, patch)
run_tests()
git_diff()
```

Action space tốt nên:

- đủ nhỏ để reasoning rõ;
- đủ biểu đạt để hoàn thành task;
- có kiểu và cấu trúc;
- có semantics ổn định;
- trả error rõ ràng;
- giới hạn side effect nguy hiểm.

Một `shell(command)` toàn quyền rất linh hoạt nhưng làm verification và security khó hơn nhiều so với typed tool.

## Mục tiêu và điều kiện thành công

“Fix bug” là mục tiêu mơ hồ. Agent cần điều kiện thành công có thể quan sát:

```text
test X chạy qua
không regression test nào hỏng
chỉ thay đổi file trong phạm vi cho phép
```

Agent không có success condition rõ dễ rơi vào loop hoặc dừng quá sớm.

## Agent loop và control plane

Agent production thường có hai lớp:

```text
Reasoning / Policy Plane
    LLM chọn thao tác tiếp theo

Control Plane
    validate action
    kiểm tra permission / budget
    thực thi tool
    ghi trạng thái
    cưỡng chế điều kiện dừng
```

Không nên để model vừa quyết định task policy vừa tự quyết security policy cho chính nó.

## Agent và Planning

Agent có thể phản ứng trực tiếp: quan sát rồi chọn bước tiếp.

Agent cũng có thể lập kế hoạch trước khi thực thi. Tuy nhiên plan chỉ là giả thuyết về trạng thái tương lai. Sau mỗi action, environment có thể trả kết quả khác dự đoán nên agent cần **lập kế hoạch lại (replanning)**.

Xem [Planning](../02_search_reasoning_and_planning/05_planning.md).

## Agent và RAG

RAG giải quyết retrieval và grounding; Agent giải quyết chọn hành động tuần tự.

Một agent có thể dùng retrieval như tool:

```text
Mục tiêu
→ tìm tri thức
→ đọc tài liệu
→ quyết định
→ gọi API
```

Do đó:

```text
RAG ≠ Agent
Agent có thể dùng RAG
```

Xem [RAG Fundamentals](../09_retrieval_and_rag/05_rag_fundamentals.md).

## Agent và Workflow

Workflow có control flow được developer định nghĩa tương đối rõ. Agent trao cho model nhiều quyền hơn trong việc chọn bước tiếp theo.

Thiết kế lai thường hiệu quả:

```text
workflow xác định ở lớp ngoài
       ↓
quyết định agentic tại bước không chắc chắn
       ↓
validation xác định
```

Không nên dùng agent nếu branching logic đã rõ và có thể code trực tiếp.

## Lỗi lan truyền qua nhiều bước

Task agent dài có vấn đề độ tin cậy nhân dồn.

Nếu mỗi bước đúng với xác suất `p`, một xấp xỉ đơn giản cho `n` bước quan trọng độc lập là:

\[
P(success)\approx p^n
\]

Nếu `p=0.95`, 20 bước liên tiếp:

\[
0.95^{20}\approx0.36
\]

Trong thực tế failure không độc lập, nhưng trực giác quan trọng: tự chủ dài hạn cần checkpoint, verification và recovery.

## Chi phí và độ trễ tích lũy

Agent loop có nhiều model call và tool call. Tổng chi phí gần đúng:

\[
C=\sum_t(C_{model,t}+C_{tool,t})
\]

Latency cũng tích lũy. Vì vậy “agent làm được” chưa đủ; cần budget policy và early stopping.

## Agent như một state machine

Một cách triển khai robust là coi agent như state machine rõ ràng:

```text
RECEIVED
→ ANALYZING
→ PLANNING
→ EXECUTING
→ VERIFYING
→ DONE / FAILED / NEEDS_APPROVAL
```

State machine giúp resume, retry và observability tốt hơn việc chỉ lưu transcript hội thoại.

## Human-in-the-loop

Human approval phù hợp với hành động không thể đảo ngược hoặc rủi ro cao:

```text
read / search → tự động
write draft → tự động
send external message → cần duyệt
transfer money → duyệt nghiêm ngặt
production deploy → tùy policy
```

Ranh giới approval nên dựa trên rủi ro, không dựa vào “mức tự tin” do AI tự báo.

## Mô hình tư duy

> **LLM cung cấp policy linh hoạt; agent system biến policy đó thành tương tác có kiểm soát với environment.**

Model là một thành phần nhận thức. Runtime và engineering quyết định action có an toàn, quan sát được và phục hồi được hay không.

## Những hiểu lầm thường gặp

### “Có tool calling là agent”

Một lời gọi tool đơn lẻ có control flow xác định chưa chắc là agent. Hành vi agentic rõ hơn khi có vòng observe–decide–act và model được quyền chọn next action.

### “Agent càng tự chủ càng tốt”

Không. Autonomy là đánh đổi giữa giá trị, chi phí và rủi ro. Nhiều business system phù hợp hơn với workflow giới hạn tự chủ.

### “Agent memory chỉ là vector database”

Memory còn gồm working state, event history, semantic knowledge, preference của user và artifact đã lưu. Vector retrieval chỉ là một cơ chế.

## Liên kết kiến thức

Agent system nối agent cổ điển, [Planning](../02_search_reasoning_and_planning/05_planning.md), [LLMs](../08_large_language_models/00_from_language_models_to_llms.md), [RAG](../09_retrieval_and_rag/05_rag_fundamentals.md) và Software Engineering.

Xem tiếp: [Tools and Function Calling](./01_tools_and_function_calling.md).