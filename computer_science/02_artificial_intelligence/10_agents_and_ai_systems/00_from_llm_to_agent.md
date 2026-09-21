# Từ LLM tới AI Agent

Large Language Model tự nó chủ yếu là một conditional sequence model: nhận context và sinh output. **AI Agent (에이전트 / tác nhân AI)** xuất hiện khi model được đặt vào một control loop có goal, state, observations và khả năng chọn action tác động ra bên ngoài model.

Một mental model tối giản:

```text
Goal
 ↓
Observe current state
 ↓
Choose next action
 ↓
Execute action/tool
 ↓
Observe result
 ↓
Update state
 ↓
Continue or stop
```

Điểm quan trọng là **agent không đồng nghĩa LLM**. LLM có thể đóng vai trò policy/decision component, planner hoặc parser; nhưng agent system còn cần runtime, tools, permissions, state management, error handling, termination conditions và observability.

Xem nền classical agent tại [Intelligence, Agents and Environments](../00_foundations/02_intelligence_agents_and_environments.md).

## Agent như một policy có memory và tools

Trong classical AI, agent có thể mô hình hóa action selection như:

\[
\pi(a\mid s)
\]

với `s` là state và `a` là action. Với LLM agent, state không nhất thiết là một vector Markov đầy đủ. Nó thường được biểu diễn bằng structured state + selected context + tool results + conversation history.

LLM có thể nhận:

```text
system policy
+ user goal
+ current state
+ tool schemas
+ previous observations
```

và sinh một trong hai loại output:

```text
final response
hoặc
structured tool/action request
```

Runtime mới là thành phần thực thi action.

## Model capability và agent capability khác nhau

Một model có thể reasoning tốt nhưng agent vẫn thất bại vì:

- tool schema mơ hồ;
- state mất đồng bộ;
- action không idempotent;
- retry tạo duplicate side effect;
- permission quá rộng;
- loop không có stopping rule;
- tool result không được validate;
- context bị overflow hoặc polluted.

Ngược lại, một model không phải mạnh nhất vẫn có thể tạo system đáng tin nếu workflow và action space được thiết kế tốt.

## Agent không phải chatbot có nhiều prompt

Chatbot thường có interaction pattern:

```text
user → model → text
```

Agent:

```text
user goal
→ model decision
→ action
→ environment result
→ model decision
→ ...
```

Sự xuất hiện của **external state transition** là khác biệt quan trọng. Khi agent gửi email, update database hoặc deploy code, output của model trở thành hành động có side effect thực.

## Autonomy là một spectrum

Không nên chia binary “agent / không agent”. Có thể có nhiều mức:

```text
Model chỉ trả text
→ model đề xuất action
→ user approve từng action
→ model tự chọn tool trong whitelist
→ model tự lập kế hoạch nhiều bước
→ model điều hành workflow dài hạn
```

Autonomy càng cao thì yêu cầu về sandboxing, validation, budget, permissions và monitoring càng cao.

## Environment trong LLM Agent

Environment có thể là:

- file system;
- browser/web;
- database;
- source repository;
- enterprise APIs;
- operating system;
- SaaS applications;
- physical robot environment.

Observation là thông tin runtime trả lại từ environment sau action.

Agent quality phụ thuộc mạnh vào observation fidelity. Nếu tool chỉ trả “success” thay vì changed state cụ thể, model khó reasoning bước sau.

## Action Space

Action space là tập hành động system cho phép.

Ví dụ coding agent:

```text
read_file(path)
search_code(query)
edit_file(path, patch)
run_tests()
git_diff()
```

Action space tốt nên:

- nhỏ đủ để reasoning rõ;
- expressive đủ để hoàn thành task;
- typed/structured;
- có semantics ổn định;
- expose error rõ;
- hạn chế dangerous side effect.

Đưa cho model một `shell(command)` toàn quyền rất flexible nhưng làm verification và security khó hơn typed tools.

## Goal và Success Condition

“Fix bug” là goal mơ hồ. Agent cần observable success criteria:

```text
test X passes
no existing test regresses
changed files only within scope
```

Một agent không có clear success condition dễ rơi vào loop hoặc dừng quá sớm.

## Agent loop và control plane

Production agent thường có hai layer:

```text
Reasoning / Policy Plane
    LLM chooses next operation

Control Plane
    validates action
    checks permission/budget
    executes tool
    records state
    enforces stop rules
```

Không nên để model vừa quyết định policy vừa tự quyết security policy của chính nó.

## Agent và Planning

Agent có thể reactive: quan sát rồi chọn bước tiếp.

Agent cũng có thể deliberative: tạo intermediate plan trước khi thực thi.

Nhưng plan chỉ là hypothesis về future state. Sau mỗi action, environment có thể trả kết quả bất ngờ nên agent cần **replanning**.

Xem [Planning](../02_search_reasoning_and_planning/05_planning.md).

## Agent và RAG

RAG giải quyết retrieval/grounding. Agent giải quyết sequential action selection.

Một agent có thể gọi retrieval như tool:

```text
Goal
→ Search knowledge
→ Read documents
→ Decide
→ Call API
```

Vì vậy:

```text
RAG ≠ Agent
Agent can use RAG
```

Xem [RAG Fundamentals](../09_retrieval_and_rag/05_rag_fundamentals.md).

## Agent và Workflow

Workflow có control flow được developer định nghĩa tương đối rõ. Agent cho model quyền quyết định nhiều hơn về next step.

Hybrid design thường tốt nhất:

```text
Deterministic outer workflow
       ↓
Agentic decision at uncertain step
       ↓
Deterministic validation
```

Không nên dùng agent khi branching logic đã biết rõ và có thể code trực tiếp.

## Failure propagation

Agent task dài có multiplicative reliability problem.

Nếu mỗi bước đúng với probability `p`, một approximation đơn giản cho `n` independent critical steps là:

\[
P(success)\approx p^n
\]

Nếu `p=0.95`, 20 bước liên tiếp:

\[
0.95^{20}\approx0.36
\]

Thực tế failures không independent, nhưng intuition quan trọng: long-horizon autonomy cần checkpoints, verification và recovery.

## Cost và latency accumulation

Agent loop có nhiều model/tool calls. Total cost gần như:

\[
C=\sum_t(C_{model,t}+C_{tool,t})
\]

Latency cũng tích lũy. Vì vậy “agent làm được” chưa đủ; phải có budget policy và early stopping.

## Agent as state machine

Một cách implementation robust là coi agent như explicit state machine:

```text
RECEIVED
→ ANALYZING
→ PLANNING
→ EXECUTING
→ VERIFYING
→ DONE / FAILED / NEEDS_APPROVAL
```

State machine giúp resumability, retry và observability tốt hơn việc chỉ lưu conversation transcript.

## Human-in-the-loop

Human approval phù hợp cho irreversible/high-risk actions:

```text
read/search → auto
write draft → auto
send external message → approval
transfer money → strict approval
production deploy → policy-dependent approval
```

Approval boundary nên dựa trên risk, không phải “AI có tự tin hay không”.

## Mental Model

> **LLM cung cấp flexible policy; agent system biến policy đó thành controlled interaction với environment.**

Model là cognitive component. Runtime và engineering quyết định action có an toàn, observable và recoverable hay không.

## Common Misconceptions

### “Có tool calling là agent”

Một single deterministic tool call chưa nhất thiết tạo agent. Agentic behavior rõ hơn khi system có loop quan sát–quyết định–hành động và model có quyền chọn next action.

### “Agent càng autonomous càng tốt”

Autonomy là cost/risk trade-off. Nhiều business systems tốt hơn với workflow giới hạn autonomy.

### “Agent memory chỉ là vector database”

Memory gồm working state, event history, semantic knowledge, user preferences và persisted artifacts. Vector retrieval chỉ là một mechanism.

## Knowledge Connection

Agent systems nối Classical AI agents, [Planning](../02_search_reasoning_and_planning/05_planning.md), [LLMs](../08_large_language_models/00_from_language_models_to_llms.md), [RAG](../09_retrieval_and_rag/05_rag_fundamentals.md) và Software Engineering. Chapter tiếp theo đi vào boundary giữa model decision và executable tools.

Xem tiếp: [Tools and Function Calling](./01_tools_and_function_calling.md).