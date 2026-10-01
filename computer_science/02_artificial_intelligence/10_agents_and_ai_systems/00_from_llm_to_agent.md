# Từ LLM tới AI tác nhân (agent / 에이전트)

> **Mạch đọc:** [README](./README.md) là bản đồ owner của **Từ LLM tới AI tác nhân (agent / 에이전트)**; nhìn vào vị trí đó trước để biết file này đang phục vụ nhánh kiến thức nào. **Tác nhân (agent / 에이전트) như một chính sách (policy / 정책) có bộ nhớ (memory / 메모리) và tools** mở đối tượng chính của file và câu hỏi cần theo dõi; sau đó sang **Mô hình (model / 모델) năng lực (capability / 역량) và tác nhân (agent / 에이전트) năng lực (capability / 역량) khác nhau** để mở rộng đối tượng sang phạm vi kế cận. Cách đi này giữ lại điểm tựa của section đầu và cho biết kết luận sẽ được dùng ở đâu, thay vì dừng ở định nghĩa đầu tiên.

Large ngôn ngữ (language / 언어) mô hình (model / 모델) tự nó chủ yếu là một conditional chuỗi (sequence / 시퀀스) mô hình (model / 모델): nhận ngữ cảnh (context / 맥락) và sinh đầu ra (output / 출력). **AI tác nhân (agent / 에이전트)** xuất hiện khi mô hình (model / 모델) được đặt vào một vòng điều khiển (control loop / 제어 루프) có goal, trạng thái (state / 상태), observations và khả năng chọn hành động (action / 동작) tác động ra bên ngoài mô hình (model / 모델).

Một mô hình tư duy (mental model / 사고 모델) tối giản:

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

Điểm quan trọng là **tác nhân (agent / 에이전트) không đồng nghĩa LLM**. LLM có thể đóng vai trò chính sách (policy / 정책)/quyết định (decision / 결정) thành phần (component / 컴포넌트), planner hoặc parser; nhưng hệ tác nhân (agent system / 에이전트 시스템) còn cần thời gian chạy (runtime / 런타임), tools, permissions, trạng thái (state / 상태) management, lỗi (error / 오류) handling, termination conditions và khả năng quan sát (observability / 관측 가능성).

Xem nền classical tác nhân (agent / 에이전트) tại [Intelligence, Agents and Environments](../00_foundations/02_intelligence_agents_and_environments.md).

## Tác nhân (agent / 에이전트) như một chính sách (policy / 정책) có bộ nhớ (memory / 메모리) và tools

Trong classical AI, tác nhân (agent / 에이전트) có thể mô hình hóa hành động (action / 동작) selection như:

\[
\pi(a\mid s)
\]

với `s` là trạng thái (state / 상태) và `a` là hành động (action / 동작). Với LLM tác nhân (agent / 에이전트), trạng thái (state / 상태) không nhất thiết là một véc-tơ (vector / 벡터) Markov đầy đủ. Nó thường được biểu diễn bằng structured trạng thái (state / 상태) + selected ngữ cảnh (context / 맥락) + công cụ (tool / 도구) results + conversation lịch sử (history / 이력).

LLM có thể nhận:

```text
system policy
+ user goal
+ current state
+ tool schemas
+ previous observations
```

và sinh một trong hai loại đầu ra (output / 출력):

```text
final response
hoặc
structured tool/action request
```

Thời gian chạy (runtime / 런타임) mới là thành phần thực thi hành động (action / 동작).

> **Chuyển mạch:** Trong **Từ LLM tới AI tác nhân (agent / 에이전트)**, **Mô hình (model / 모델) năng lực (capability / 역량) và tác nhân (agent / 에이전트) năng lực (capability / 역량) khác nhau** tiếp nhận điểm tựa từ **Tác nhân (agent / 에이전트) như một chính sách (policy / 정책) có bộ nhớ (memory / 메모리) và tools** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Tác nhân (agent / 에이전트) không phải chatbot có nhiều prompt** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Mô hình (model / 모델) năng lực (capability / 역량) và tác nhân (agent / 에이전트) năng lực (capability / 역량) khác nhau

Một mô hình (model / 모델) có thể lập luận (reasoning / 추론) tốt nhưng tác nhân (agent / 에이전트) vẫn thất bại vì:

- công cụ (tool / 도구) lược đồ (schema / 스키마) mơ hồ;
- trạng thái (state / 상태) mất đồng bộ;
- hành động (action / 동작) không idempotent;
- thử lại (retry / 재시도) tạo duplicate side tác động (effect / 효과);
- permission quá rộng;
- vòng lặp (loop / 루프) không có stopping quy tắc (rule / 규칙);
- công cụ (tool / 도구) kết quả (result / 결과) không được validate;
- ngữ cảnh (context / 맥락) bị overflow hoặc polluted.

Ngược lại, một mô hình (model / 모델) không phải mạnh nhất vẫn có thể tạo hệ thống (system / 시스템) đáng tin nếu workflow và hành động (action / 동작) không gian (space / 공간) được thiết kế tốt.

> **Chuyển mạch:** Ở chặng này của **Từ LLM tới AI tác nhân (agent / 에이전트)**, **Tác nhân (agent / 에이전트) không phải chatbot có nhiều prompt** tiếp nhận điểm tựa từ **Mô hình (model / 모델) năng lực (capability / 역량) và tác nhân (agent / 에이전트) năng lực (capability / 역량) khác nhau** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Autonomy là một spectrum** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Tác nhân (agent / 에이전트) không phải chatbot có nhiều prompt

Chatbot thường có tương tác (interaction / 상호작용) mẫu (pattern / 패턴):

```text
user → model → text
```

Tác nhân (agent / 에이전트):

```text
user goal
→ model decision
→ action
→ environment result
→ model decision
→ ...
```

Sự xuất hiện của **bên ngoài (external / 외부) chuyển tiếp trạng thái (state transition / 상태 전이)** là khác biệt quan trọng. Khi tác nhân (agent / 에이전트) gửi email, cập nhật (update / 업데이트) cơ sở dữ liệu (database / 데이터베이스) hoặc deploy mã (code / 코드), đầu ra (output / 출력) của mô hình (model / 모델) trở thành hành động có side tác động (effect / 효과) thực.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Từ LLM tới AI tác nhân (agent / 에이전트)**, **Autonomy là một spectrum** tiếp nhận điểm tựa từ **Tác nhân (agent / 에이전트) không phải chatbot có nhiều prompt** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Môi trường (environment / 환경) trong LLM tác nhân (agent / 에이전트)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Autonomy là một spectrum

Không nên chia nhị phân (binary / 이진) “tác nhân (agent / 에이전트) / không tác nhân (agent / 에이전트)”. Có thể có nhiều mức:

```text
Model chỉ trả text
→ model đề xuất action
→ user approve từng action
→ model tự chọn tool trong whitelist
→ model tự lập kế hoạch nhiều bước
→ model điều hành workflow dài hạn
```

Autonomy càng cao thì yêu cầu về sandboxing, kiểm tra hợp lệ (validation / 검증), ngân sách (budget / 예산), permissions và monitoring càng cao.

> **Chuyển mạch:** Trong **Từ LLM tới AI tác nhân (agent / 에이전트)**, **Môi trường (environment / 환경) trong LLM tác nhân (agent / 에이전트)** tiếp nhận điểm tựa từ **Autonomy là một spectrum** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Hành động (action / 동작) không gian (space / 공간)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Môi trường (environment / 환경) trong LLM tác nhân (agent / 에이전트)

Môi trường (environment / 환경) có thể là:

- tệp (file / 파일) hệ thống (system / 시스템);
- trình duyệt (browser / 브라우저)/web;
- cơ sở dữ liệu (database / 데이터베이스);
- nguồn (source / 소스) repository;
- enterprise APIs;
- operating hệ thống (system / 시스템);
- SaaS applications;
- vật lý (physical / 물리적) robot môi trường (environment / 환경).

Observation là thông tin thời gian chạy (runtime / 런타임) trả lại từ môi trường (environment / 환경) sau hành động (action / 동작).

Tác nhân (agent / 에이전트) chất lượng (quality / 품질) phụ thuộc mạnh vào observation fidelity. Nếu công cụ (tool / 도구) chỉ trả “success” thay vì changed trạng thái (state / 상태) cụ thể, mô hình (model / 모델) khó lập luận (reasoning / 추론) bước sau.

> **Chuyển mạch:** Ở chặng này của **Từ LLM tới AI tác nhân (agent / 에이전트)**, **Hành động (action / 동작) không gian (space / 공간)** tiếp nhận điểm tựa từ **Môi trường (environment / 환경) trong LLM tác nhân (agent / 에이전트)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Goal và Success điều kiện (condition / 조건)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Hành động (action / 동작) không gian (space / 공간)

Hành động (action / 동작) không gian (space / 공간) là tập hành động hệ thống (system / 시스템) cho phép.

Ví dụ coding tác nhân (agent / 에이전트):

```text
read_file(path)
search_code(query)
edit_file(path, patch)
run_tests()
git_diff()
```

Hành động (action / 동작) không gian (space / 공간) tốt nên:

- nhỏ đủ để lập luận (reasoning / 추론) rõ;
- expressive đủ để hoàn thành tác vụ (task / 작업);
- typed/structured;
- có ngữ nghĩa (semantics / 의미론) ổn định;
- expose lỗi (error / 오류) rõ;
- hạn chế dangerous side tác động (effect / 효과).

Đưa cho mô hình (model / 모델) một `shell(command)` toàn quyền rất flexible nhưng làm xác minh (verification / 확인) và bảo mật (security / 보안) khó hơn typed tools.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Từ LLM tới AI tác nhân (agent / 에이전트)**, **Goal và Success điều kiện (condition / 조건)** tiếp nhận điểm tựa từ **Hành động (action / 동작) không gian (space / 공간)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Tác nhân (agent / 에이전트) vòng lặp (loop / 루프) và điều khiển (control / 제어) plane** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Goal và Success điều kiện (condition / 조건)

“Fix bug” là goal mơ hồ. tác nhân (agent / 에이전트) cần observable success criteria:

```text
test X passes
no existing test regresses
changed files only within scope
```

Một tác nhân (agent / 에이전트) không có clear success điều kiện (condition / 조건) dễ rơi vào vòng lặp (loop / 루프) hoặc dừng quá sớm.

> **Chuyển mạch:** Trong **Từ LLM tới AI tác nhân (agent / 에이전트)**, **Tác nhân (agent / 에이전트) vòng lặp (loop / 루프) và điều khiển (control / 제어) plane** tiếp nhận điểm tựa từ **Goal và Success điều kiện (condition / 조건)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Tác nhân (agent / 에이전트) và Planning** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Tác nhân (agent / 에이전트) vòng lặp (loop / 루프) và điều khiển (control / 제어) plane

Môi trường vận hành (production / 운영 환경) tác nhân (agent / 에이전트) thường có hai tầng (layer / 계층):

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

Không nên để mô hình (model / 모델) vừa quyết định chính sách (policy / 정책) vừa tự quyết bảo mật (security / 보안) chính sách (policy / 정책) của chính nó.

> **Chuyển mạch:** Ở chặng này của **Từ LLM tới AI tác nhân (agent / 에이전트)**, **Tác nhân (agent / 에이전트) và Planning** tiếp nhận điểm tựa từ **Tác nhân (agent / 에이전트) vòng lặp (loop / 루프) và điều khiển (control / 제어) plane** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Tác nhân (agent / 에이전트) và RAG** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Tác nhân (agent / 에이전트) và Planning

Tác nhân (agent / 에이전트) có thể reactive: quan sát rồi chọn bước tiếp.

Tác nhân (agent / 에이전트) cũng có thể deliberative: tạo intermediate plan trước khi thực thi.

Nhưng plan chỉ là hypothesis về future trạng thái (state / 상태). Sau mỗi hành động (action / 동작), môi trường (environment / 환경) có thể trả kết quả bất ngờ nên tác nhân (agent / 에이전트) cần **replanning**.

Xem [Planning](../02_search_reasoning_and_planning/05_planning.md).

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Từ LLM tới AI tác nhân (agent / 에이전트)**, **Tác nhân (agent / 에이전트) và RAG** tiếp nhận điểm tựa từ **Tác nhân (agent / 에이전트) và Planning** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Tác nhân (agent / 에이전트) và Workflow** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Tác nhân (agent / 에이전트) và RAG

RAG giải quyết retrieval/grounding. tác nhân (agent / 에이전트) giải quyết sequential hành động (action / 동작) selection.

Một tác nhân (agent / 에이전트) có thể gọi retrieval như công cụ (tool / 도구):

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

> **Chuyển mạch:** Trong **Từ LLM tới AI tác nhân (agent / 에이전트)**, **Tác nhân (agent / 에이전트) và RAG** xác định đầu vào; **Tác nhân (agent / 에이전트) và Workflow** giải thích bước vận hành tạo ra kết quả kế tiếp. Từ đây, **Thất bại (failure / 실패) propagation** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Tác nhân (agent / 에이전트) và Workflow

Workflow có điều khiển (control / 제어) luồng (flow / 흐름) được nhà phát triển (developer / 개발자) định nghĩa tương đối rõ. tác nhân (agent / 에이전트) cho mô hình (model / 모델) quyền quyết định nhiều hơn về next step.

Hybrid thiết kế (design / 설계) thường tốt nhất:

```text
Deterministic outer workflow
       ↓
Agentic decision at uncertain step
       ↓
Deterministic validation
```

Không nên dùng tác nhân (agent / 에이전트) khi branching lô-gic (logic / 논리) đã biết rõ và có thể mã (code / 코드) trực tiếp.

> **Chuyển mạch:** Ở chặng này của **Từ LLM tới AI tác nhân (agent / 에이전트)**, **Tác nhân (agent / 에이전트) và Workflow** xác định đầu vào; **Thất bại (failure / 실패) propagation** giải thích bước vận hành tạo ra kết quả kế tiếp. Từ đây, **Chi phí (cost / 비용) và độ trễ (latency / 지연 시간) accumulation** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Thất bại (failure / 실패) propagation

Tác nhân (agent / 에이전트) tác vụ (task / 작업) dài có multiplicative độ tin cậy (reliability / 신뢰성) bài toán (problem / 문제).

Nếu mỗi bước đúng với xác suất (probability / 확률) `p`, một approximation đơn giản cho `n` independent trọng yếu (critical / 중요) steps là:

\[
P(success)\approx p^n
\]

Nếu `p=0.95`, 20 bước liên tiếp:

\[
0.95^{20}\approx0.36
\]

Thực tế failures không independent, nhưng intuition quan trọng: long-horizon autonomy cần checkpoints, xác minh (verification / 확인) và khôi phục (recovery / 복구).

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Từ LLM tới AI tác nhân (agent / 에이전트)**, **Chi phí (cost / 비용) và độ trễ (latency / 지연 시간) accumulation** tiếp nhận điểm tựa từ **Thất bại (failure / 실패) propagation** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Tác nhân (agent / 에이전트) as máy trạng thái (state machine / 상태 머신)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Chi phí (cost / 비용) và độ trễ (latency / 지연 시간) accumulation

Tác nhân (agent / 에이전트) vòng lặp (loop / 루프) có nhiều mô hình (model / 모델)/công cụ (tool / 도구) calls. Total chi phí (cost / 비용) gần như:

\[
C=\sum_t(C_{model,t}+C_{tool,t})
\]

Độ trễ (latency / 지연 시간) cũng tích lũy. Vì vậy “tác nhân (agent / 에이전트) làm được” chưa đủ; phải có ngân sách (budget / 예산) chính sách (policy / 정책) và early stopping.

> **Chuyển mạch:** Trong **Từ LLM tới AI tác nhân (agent / 에이전트)**, **Tác nhân (agent / 에이전트) as máy trạng thái (state machine / 상태 머신)** tiếp nhận điểm tựa từ **Chi phí (cost / 비용) và độ trễ (latency / 지연 시간) accumulation** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Human-in-the-loop** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Tác nhân (agent / 에이전트) as máy trạng thái (state machine / 상태 머신)

Một cách hiện thực (implementation / 구현) robust là coi tác nhân (agent / 에이전트) như tường minh (explicit / 명시적) máy trạng thái (state machine / 상태 머신):

```text
RECEIVED
→ ANALYZING
→ PLANNING
→ EXECUTING
→ VERIFYING
→ DONE / FAILED / NEEDS_APPROVAL
```

Máy trạng thái (state machine / 상태 머신) giúp resumability, thử lại (retry / 재시도) và khả năng quan sát (observability / 관측 가능성) tốt hơn việc chỉ lưu conversation transcript.

> **Chuyển mạch:** Ở chặng này của **Từ LLM tới AI tác nhân (agent / 에이전트)**, **Human-in-the-loop** tiếp nhận điểm tựa từ **Tác nhân (agent / 에이전트) as máy trạng thái (state machine / 상태 머신)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Mô hình tư duy (mental model / 사고 모델)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Human-in-the-loop

Human approval phù hợp cho irreversible/high-risk actions:

```text
read/search → auto
write draft → auto
send external message → approval
transfer money → strict approval
production deploy → policy-dependent approval
```

Approval ranh giới (boundary / 경계) nên dựa trên rủi ro (risk / 위험), không phải “AI có tự tin hay không”.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Từ LLM tới AI tác nhân (agent / 에이전트)**, **Mô hình tư duy (mental model / 사고 모델)** gom các mảnh từ **Human-in-the-loop** thành một kết luận có thể mang sang phần kế tiếp. Từ đây, **Dùng chung (common / 공통) Misconceptions** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Mô hình tư duy (mental model / 사고 모델)

> **LLM cung cấp flexible chính sách (policy / 정책); hệ tác nhân (agent system / 에이전트 시스템) biến chính sách (policy / 정책) đó thành controlled tương tác (interaction / 상호작용) với môi trường (environment / 환경).**

Mô hình (model / 모델) là cognitive thành phần (component / 컴포넌트). thời gian chạy (runtime / 런타임) và kỹ thuật (engineering / 엔지니어링) quyết định hành động (action / 동작) có an toàn, observable và recoverable hay không.

> **Chuyển mạch:** Trong **Từ LLM tới AI tác nhân (agent / 에이전트)**, **Dùng chung (common / 공통) Misconceptions** gom các mảnh từ **Mô hình tư duy (mental model / 사고 모델)** thành một kết luận có thể mang sang phần kế tiếp. Từ đây, **Liên kết kiến thức (knowledge connection / 지식 연결)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Dùng chung (common / 공통) Misconceptions

### “Có công cụ (tool / 도구) calling là tác nhân (agent / 에이전트)”

Một single deterministic công cụ (tool / 도구) lời gọi (call / 호출) chưa nhất thiết tạo tác nhân (agent / 에이전트). Agentic hành vi (behavior / 동작) rõ hơn khi hệ thống (system / 시스템) có vòng lặp (loop / 루프) quan sát–quyết định–hành động và mô hình (model / 모델) có quyền chọn next hành động (action / 동작).

### “tác nhân (agent / 에이전트) càng autonomous càng tốt”

Autonomy là chi phí (cost / 비용)/rủi ro (risk / 위험) sự đánh đổi (trade-off / 트레이드오프). Nhiều nghiệp vụ (business / 비즈니스) các hệ thống (systems / 시스템들) tốt hơn với workflow giới hạn autonomy.

### “tác nhân (agent / 에이전트) bộ nhớ (memory / 메모리) chỉ là véc-tơ (vector / 벡터) cơ sở dữ liệu (database / 데이터베이스)”

Bộ nhớ (memory / 메모리) gồm working trạng thái (state / 상태), sự kiện (event / 이벤트) lịch sử (history / 이력), ngữ nghĩa (semantic / 의미적) kiến thức (knowledge / 지식), người dùng (user / 사용자) preferences và persisted artifacts. véc-tơ (vector / 벡터) retrieval chỉ là một cơ chế (mechanism / 메커니즘).

> **Chuyển mạch:** Ở chặng này của **Từ LLM tới AI tác nhân (agent / 에이전트)**, sau nội dung của **Dùng chung (common / 공통) Misconceptions**, **Liên kết kiến thức (knowledge connection / 지식 연결)** chỉ rõ tài liệu chuẩn và vị trí sở hữu để người học biết phần nào cần quay lại khi muốn đào sâu. Phần còn lại của file dùng kết quả này để khép lại mạch giải thích.

## Liên kết kiến thức (knowledge connection / 지식 연결)

Tác nhân (agent / 에이전트) các hệ thống (systems / 시스템들) nối Classical AI agents, [Planning](../02_search_reasoning_and_planning/05_planning.md), [LLMs](../08_large_language_models/00_from_language_models_to_llms.md), [RAG](../09_retrieval_and_rag/05_rag_fundamentals.md) và Kỹ nghệ phần mềm (software engineering / 소프트웨어 공학). Chapter tiếp theo đi vào ranh giới (boundary / 경계) giữa mô hình (model / 모델) quyết định (decision / 결정) và executable tools.

Xem tiếp: [Tools and Function Calling](./01_tools_and_function_calling.md).

> **Bàn giao:** Sau **Liên kết kiến thức (knowledge connection / 지식 연결)**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](./README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
