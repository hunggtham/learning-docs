# Tác nhân (agent / 에이전트) vòng lặp (loop / 루프)

> **Mạch đọc:** [README](./README.md) là bản đồ owner của **Agent loop**. Route đi từ observe → decide/plan → tool action → result/state update → stop or retry criteria, để mỗi vòng lặp có tín hiệu vào, hành động và điều kiện kết thúc rõ ràng.

Tác nhân (agent / 에이전트) vòng lặp (loop / 루프) là cơ chế biến một goal lớn thành chuỗi observation–quyết định (decision / 결정)–hành động (action / 동작) lặp lại. Không có vòng lặp (loop / 루프), công cụ (tool / 도구) calling thường chỉ là một lần gọi hàm; có vòng lặp (loop / 루프), hệ thống (system / 시스템) phải quản lý trạng thái (state / 상태), termination, retries, budgets và xác minh (verification / 확인) qua nhiều bước.

Một vòng lặp (loop / 루프) cơ bản:

```text
initialize task state
while not done:
    observe(state)
    decide(next_action)
    validate(action)
    execute(action)
    record(result)
    verify(progress)
```

## Observe

Observation không chỉ là công cụ (tool / 도구) đầu ra (output / 출력) cuối. Nó có thể gồm:

- hiện tại (current / 현재) structured trạng thái (state / 상태);
- latest công cụ (tool / 도구) kết quả (result / 결과);
- outstanding subtasks;
- previous failures;
- ngân sách (budget / 예산) còn lại;
- approval status;
- môi trường (environment / 환경) changes.

Nếu observation thiếu hoặc stale, quyết định (decision / 결정) sau sai dù lập luận (reasoning / 추론) lô-gic (logic / 논리) tốt.

> **Chuyển mạch:** Trong **Tác nhân (agent / 에이전트) vòng lặp (loop / 루프)**, **Decide** tiếp nhận điểm tựa từ **Observe** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Act** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Decide

Mô hình (model / 모델) có thể chọn:

```text
call tool
ask user
revise plan
retry with changed arguments
verify
finish
```

Quyết định (decision / 결정) không gian (space / 공간) nên tường minh (explicit / 명시적). Nếu mô hình (model / 모델) chỉ được prompt “hãy tiếp tục”, stopping hành vi (behavior / 동작) khó kiểm soát.

> **Chuyển mạch:** Ở chặng này của **Tác nhân (agent / 에이전트) vòng lặp (loop / 루프)**, **Act** tiếp nhận điểm tựa từ **Decide** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Verify** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Act

Hành động (action / 동작) thực thi (execution / 실행) phải qua điều khiển (control / 제어) plane. tác nhân (agent / 에이전트) không nên tự bypass chính sách (policy / 정책) bằng cách encode hành động (action / 동작) trong free-form văn bản (text / 텍스트).

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Tác nhân (agent / 에이전트) vòng lặp (loop / 루프)**, **Verify** tiếp nhận điểm tựa từ **Act** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Termination** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Verify

Sau thực thi (execution / 실행), hệ thống (system / 시스템) cần kiểm progress dựa trên bằng chứng (evidence / 증거).

Ví dụ coding tác nhân (agent / 에이전트) không nên dừng vì mô hình (model / 모델) nói “đã sửa xong”; phải chạy kiểm thử (test / 테스트), inspect diff hoặc check acceptance criteria.

```text
claim of success ≠ verified success
```

> **Chuyển mạch:** Trong **Tác nhân (agent / 에이전트) vòng lặp (loop / 루프)**, **Termination** tiếp nhận điểm tựa từ **Verify** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **ReAct mô hình tư duy (mental model / 사고 모델)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Termination

Stop conditions có thể gồm:

- success criterion satisfied;
- max steps reached;
- đơn vị từ (token / 토큰)/chi phí (cost / 비용) ngân sách (budget / 예산) exceeded;
- repeated identical thất bại (failure / 실패);
- unrecoverable lỗi (error / 오류);
- human approval required;
- confidence/bằng chứng (evidence / 증거) insufficient.

Không có stop quy tắc (rule / 규칙), tác nhân (agent / 에이전트) có thể vòng lặp (loop / 루프) indefinitely.

> **Chuyển mạch:** Ở chặng này của **Tác nhân (agent / 에이전트) vòng lặp (loop / 루프)**, **ReAct mô hình tư duy (mental model / 사고 모델)** gom các mảnh từ **Termination** thành một kết luận có thể mang sang phần kế tiếp. Từ đây, **Thử lại (retry / 재시도) chính sách (policy / 정책)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## ReAct mô hình tư duy (mental model / 사고 모델)

Một dùng chung (common / 공통) mẫu (pattern / 패턴) là alternating lập luận (reasoning / 추론)/hành động (action / 동작)/observation. Dù hiện thực (implementation / 구현) không expose chain-of-thought, conceptual cycle vẫn hữu ích:

```text
assess state → choose action → receive observation → reassess
```

Điểm quan trọng không phải format prompt mà là closed-loop điều khiển (control / 제어).

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Tác nhân (agent / 에이전트) vòng lặp (loop / 루프)**, **Thử lại (retry / 재시도) chính sách (policy / 정책)** gom các mảnh từ **ReAct mô hình tư duy (mental model / 사고 모델)** thành một kết luận có thể mang sang phần kế tiếp. Từ đây, **Backoff và jitter** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Thử lại (retry / 재시도) chính sách (policy / 정책)

Thử lại (retry / 재시도) phải phụ thuộc lỗi (error / 오류) lớp (class / 클래스).

```text
TIMEOUT → retry with backoff
RATE_LIMIT → wait/backoff
INVALID_ARGUMENT → revise arguments
PERMISSION_DENIED → stop/escalate
CONFLICT → refetch state then decide
```

Blind thử lại (retry / 재시도) vừa tốn chi phí (cost / 비용) vừa có thể tạo side tác động (effect / 효과) duplicate.

> **Chuyển mạch:** Trong **Tác nhân (agent / 에이전트) vòng lặp (loop / 루프)**, **Backoff và jitter** tiếp nhận điểm tựa từ **Thử lại (retry / 재시도) chính sách (policy / 정책)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Vòng lặp (loop / 루프) detection** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Backoff và jitter

Phân tán (distributed / 분산) tools thường cần exponential backoff:

\[
t_k=\min(t_{max},t_0 2^k)+\epsilon
\]

`ε` là jitter để tránh nhiều workers thử lại (retry / 재시도) đồng thời.

> **Chuyển mạch:** Ở chặng này của **Tác nhân (agent / 에이전트) vòng lặp (loop / 루프)**, **Vòng lặp (loop / 루프) detection** tiếp nhận điểm tựa từ **Backoff và jitter** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Checkpointing** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Vòng lặp (loop / 루프) detection

Tác nhân (agent / 에이전트) có thể lặp cùng thought/hành động (action / 동작) chuỗi (sequence / 시퀀스).

Detection signals:

- same công cụ (tool / 도구) + same args repeated;
- trạng thái (state / 상태) băm (hash / 해시) không đổi;
- same lỗi (error / 오류) lặp lại;
- no improvement in progress chỉ số (metric / 지표).

Thời gian chạy (runtime / 런타임) có thể force replanning hoặc terminate.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Tác nhân (agent / 에이전트) vòng lặp (loop / 루프)**, **Checkpointing** tiếp nhận điểm tựa từ **Vòng lặp (loop / 루프) detection** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Sự kiện (event / 이벤트) sourcing** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Checkpointing

Long tác vụ (task / 작업) cần checkpoint persisted:

```text
completed steps
current artifacts
external resource ids
pending approvals
next intended action
```

Nhờ đó tiến trình (process / 프로세스) restart không cần replay toàn bộ conversation.

> **Chuyển mạch:** Trong **Tác nhân (agent / 에이전트) vòng lặp (loop / 루프)**, **Sự kiện (event / 이벤트) sourcing** tiếp nhận điểm tựa từ **Checkpointing** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Tính đồng thời (concurrency / 동시성)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Sự kiện (event / 이벤트) sourcing

Một robust mẫu (pattern / 패턴) là append immutable events:

```text
TaskCreated
PlanUpdated
ToolCalled
ToolSucceeded
ApprovalRequested
ApprovalGranted
TaskCompleted
```

Trạng thái hiện tại (current state / 현재 상태) có thể derive từ sự kiện (event / 이벤트) log. Điều này hỗ trợ kiểm tra (audit / 감사), replay và debugging.

> **Chuyển mạch:** Ở chặng này của **Tác nhân (agent / 에이전트) vòng lặp (loop / 루프)**, **Tính đồng thời (concurrency / 동시성)** tiếp nhận điểm tựa từ **Sự kiện (event / 이벤트) sourcing** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Ngân sách (budget / 예산) như một điều khiển (control / 제어) variable** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Tính đồng thời (concurrency / 동시성)

Nếu tác nhân (agent / 에이전트) chạy nhiều subtasks song song, trạng thái dùng chung (shared state / 공유 상태) cần consistency chiến lược (strategy / 전략).

Hai workers có thể cùng cập nhật (update / 업데이트) same tài nguyên (resource / 자원). Cần optimistic locking, phiên bản (version / 버전) check hoặc coordinator.

Tác nhân (agent / 에이전트) orchestration không loại bỏ distributed-systems problems.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Tác nhân (agent / 에이전트) vòng lặp (loop / 루프)**, **Ngân sách (budget / 예산) như một điều khiển (control / 제어) variable** tiếp nhận điểm tựa từ **Tính đồng thời (concurrency / 동시성)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Khôi phục (recovery / 복구)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Ngân sách (budget / 예산) như một điều khiển (control / 제어) variable

Ngân sách (budget / 예산) có thể gồm:

```text
max model calls
max tokens
max wall-clock time
max tool cost
max external writes
```

Chính sách (policy / 정책) có thể thay đổi mô hình (model / 모델) hoặc tìm kiếm (search / 검색) độ sâu (depth / 깊이) khi ngân sách (budget / 예산) gần cạn.

> **Chuyển mạch:** Trong **Tác nhân (agent / 에이전트) vòng lặp (loop / 루프)**, **Khôi phục (recovery / 복구)** tiếp nhận điểm tựa từ **Ngân sách (budget / 예산) như một điều khiển (control / 제어) variable** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Deterministic shell quanh probabilistic cốt lõi (core / 핵심)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Khôi phục (recovery / 복구)

Khôi phục (recovery / 복구) không phải luôn “thử lại (retry / 재시도)”. Có thể:

- quay lui (rollback / 롤백);
- compensate;
- switch công cụ (tool / 도구)/provider;
- reduce phạm vi (scope / 범위);
- ask người dùng (user / 사용자);
- continue from partial success.

> **Chuyển mạch:** Ở chặng này của **Tác nhân (agent / 에이전트) vòng lặp (loop / 루프)**, **Deterministic shell quanh probabilistic cốt lõi (core / 핵심)** tiếp nhận điểm tựa từ **Khôi phục (recovery / 복구)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Example: research tác nhân (agent / 에이전트)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Deterministic shell quanh probabilistic cốt lõi (core / 핵심)

Một thiết kế (design / 설계) mạnh:

```text
Deterministic runtime owns:
state
permissions
budgets
retries
logging
termination

LLM owns:
semantic interpretation
planning suggestion
next-action choice within allowed space
```

Đây là separation of concerns quan trọng.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Tác nhân (agent / 에이전트) vòng lặp (loop / 루프)**, **Deterministic shell quanh probabilistic cốt lõi (core / 핵심)** cho ta quy tắc; **Example: research tác nhân (agent / 에이전트)** đặt quy tắc ấy vào tình huống cụ thể để thấy nó hoạt động đến đâu. Từ đây, **Example: coding tác nhân (agent / 에이전트)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Example: research tác nhân (agent / 에이전트)

Tác vụ (task / 작업): so sánh 3 vendors.

Vòng lặp (loop / 루프) có thể:

```text
1. parse evaluation criteria
2. search vendor A/B/C
3. fetch primary sources
4. detect missing criterion
5. search targeted evidence
6. build structured comparison
7. verify citations
8. finalize
```

Nếu step 4 phát hiện thiếu pricing, tác nhân (agent / 에이전트) cần vòng lặp (loop / 루프) retrieval thay vì generate từ bộ nhớ (memory / 메모리).

> **Chuyển mạch:** Trong **Tác nhân (agent / 에이전트) vòng lặp (loop / 루프)**, **Example: research tác nhân (agent / 에이전트)** cho ta quy tắc; **Example: coding tác nhân (agent / 에이전트)** đặt quy tắc ấy vào tình huống cụ thể để thấy nó hoạt động đến đâu. Từ đây, **Mô hình tư duy (mental model / 사고 모델)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Example: coding tác nhân (agent / 에이전트)

Phần này chuyển khái niệm Computer Science thành cấu trúc, ví dụ hoặc quy trình có thể kiểm tra. Hãy xác định câu hỏi mà mục trả lời rồi nối kết luận với phần kế tiếp.

```text
inspect issue
→ search relevant code
→ read tests
→ edit
→ run focused tests
→ inspect failure
→ revise
→ run broader tests
→ inspect diff
→ finish
```

Xác minh (verification / 확인) actions là một phần của vòng lặp (loop / 루프), không phải post-processing tùy chọn.

> **Chuyển mạch:** Ở chặng này của **Tác nhân (agent / 에이전트) vòng lặp (loop / 루프)**, **Example: coding tác nhân (agent / 에이전트)** cho ta quy tắc; **Mô hình tư duy (mental model / 사고 모델)** đặt quy tắc ấy vào tình huống cụ thể để thấy nó hoạt động đến đâu. Từ đây, **Dùng chung (common / 공통) Misconceptions** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Mô hình tư duy (mental model / 사고 모델)

> **tác nhân (agent / 에이전트) vòng lặp (loop / 루프) là phản hồi (feedback / 피드백) controller cho một chính sách (policy / 정책) không hoàn hảo.**

Open-loop plan giả định world diễn ra đúng dự kiến; closed-loop tác nhân (agent / 에이전트) liên tục quan sát và điều chỉnh.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Tác nhân (agent / 에이전트) vòng lặp (loop / 루프)**, **Dùng chung (common / 공통) Misconceptions** gom các mảnh từ **Mô hình tư duy (mental model / 사고 모델)** thành một kết luận có thể mang sang phần kế tiếp. Từ đây, **Liên kết kiến thức (knowledge connection / 지식 연결)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Dùng chung (common / 공통) Misconceptions

### “Plan một lần rồi execute hết là tác nhân (agent / 에이전트) tốt”

Môi trường (environment / 환경) thay đổi và công cụ (tool / 도구) có thể thất bại (fail / 실패). Replanning dựa observation mới thường cần thiết.

### “More steps means more intelligence”

Nhiều bước có thể chỉ là dithering. chất lượng (quality / 품질) nằm ở progress per step và xác minh (verification / 확인).

### “Conversation lịch sử (history / 이력) chính là trạng thái (state / 상태)”

Transcript có thể chứa trạng thái (state / 상태), nhưng structured persisted trạng thái (state / 상태) đáng tin và queryable hơn.

> **Chuyển mạch:** Trong **Tác nhân (agent / 에이전트) vòng lặp (loop / 루프)**, sau nội dung của **Dùng chung (common / 공통) Misconceptions**, **Liên kết kiến thức (knowledge connection / 지식 연결)** chỉ rõ tài liệu chuẩn và vị trí sở hữu để người học biết phần nào cần quay lại khi muốn đào sâu. Phần còn lại của file dùng kết quả này để khép lại mạch giải thích.

## Liên kết kiến thức (knowledge connection / 지식 연결)

Tác nhân (agent / 에이전트) vòng lặp (loop / 루프) nối điều khiển (control / 제어) lý thuyết (theory / 이론) intuition, trạng thái (state / 상태) machines, phân tán (distributed / 분산) các hệ thống (systems / 시스템들) và classical tác nhân (agent / 에이전트) kiến trúc (architecture / 아키텍처). Phần tiếp theo tập trung vào cách phân rã goal thành plan có thể thực thi.

Xem tiếp: [Planning and Task Decomposition](./03_planning_and_task_decomposition.md).

> **Bàn giao:** Sau **Liên kết kiến thức (knowledge connection / 지식 연결)**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](./README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
