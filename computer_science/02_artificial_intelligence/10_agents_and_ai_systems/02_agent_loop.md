# Vòng lặp Agent

**Vòng lặp Agent (agent loop)** là cơ chế biến một mục tiêu lớn thành chuỗi quan sát–quyết định–hành động lặp lại. Không có loop, tool calling thường chỉ là một lần gọi hàm; khi có loop, hệ thống phải quản lý state, điều kiện dừng, retry, budget và verification qua nhiều bước.

Một loop cơ bản:

```text
khởi tạo trạng thái tác vụ
while chưa hoàn thành:
    quan sát(state)
    quyết định(next_action)
    kiểm tra(action)
    thực thi(action)
    ghi lại(result)
    xác minh tiến độ
```

## Quan sát

Observation không chỉ là output cuối từ tool. Nó có thể gồm:

- structured state hiện tại;
- kết quả tool mới nhất;
- subtask chưa hoàn thành;
- failure trước đó;
- budget còn lại;
- trạng thái approval;
- thay đổi của environment.

Nếu observation thiếu hoặc lỗi thời, quyết định tiếp theo có thể sai dù logic reasoning của model tốt.

## Quyết định

Mô hình có thể chọn:

```text
gọi tool
hỏi người dùng
sửa plan
retry với argument khác
verify
kết thúc
```

Không gian quyết định nên rõ. Nếu chỉ prompt “hãy tiếp tục”, stopping behavior sẽ khó kiểm soát.

## Hành động

Việc thực thi action phải đi qua control plane. Agent không nên có khả năng vượt policy chỉ bằng cách encode hành động trong free-form text.

## Xác minh

Sau khi thực thi, hệ thống cần kiểm tra tiến độ bằng evidence.

Ví dụ coding agent không nên dừng chỉ vì model nói “đã sửa xong”; nó phải chạy test, kiểm diff hoặc đối chiếu acceptance criteria.

```text
claim thành công ≠ thành công đã được xác minh
```

## Điều kiện dừng

Stop condition có thể gồm:

- success criterion đã thỏa;
- đạt số bước tối đa;
- vượt token hoặc cost budget;
- cùng một failure lặp lại;
- lỗi không thể phục hồi;
- cần human approval;
- bằng chứng không đủ.

Không có stop rule, agent có thể loop vô hạn.

## Mô hình ReAct

Một pattern phổ biến là xen kẽ reasoning, action và observation. Dù implementation không cần hiển thị chain-of-thought, chu kỳ khái niệm vẫn hữu ích:

```text
đánh giá state → chọn action → nhận observation → đánh giá lại
```

Điểm cốt lõi không nằm ở format prompt mà ở **điều khiển vòng kín (closed-loop control)**.

## Chính sách Retry

Retry phải phụ thuộc loại lỗi:

```text
TIMEOUT → retry với backoff
RATE_LIMIT → chờ / backoff
INVALID_ARGUMENT → sửa arguments
PERMISSION_DENIED → dừng / escalate
CONFLICT → đọc lại state rồi quyết định
```

Retry mù vừa tốn chi phí vừa có thể tạo side effect trùng.

## Backoff và Jitter

Tool phân tán thường cần exponential backoff:

\[
t_k=\min(t_{max},t_0 2^k)+\epsilon
\]

`ε` là jitter để tránh nhiều worker retry cùng lúc.

## Phát hiện Loop

Agent có thể lặp cùng chuỗi action.

Các tín hiệu gồm:

- cùng tool + cùng argument lặp lại;
- state hash không đổi;
- cùng error xuất hiện nhiều lần;
- progress metric không cải thiện.

Runtime có thể buộc replanning hoặc terminate.

## Checkpoint

Task dài cần checkpoint được lưu bền vững:

```text
các bước đã hoàn thành
artifact hiện tại
ID tài nguyên bên ngoài
approval đang chờ
hành động dự định tiếp theo
```

Nhờ đó process restart không cần replay toàn bộ conversation.

## Event Sourcing

Một pattern robust là ghi event bất biến theo thứ tự:

```text
TaskCreated
PlanUpdated
ToolCalled
ToolSucceeded
ApprovalRequested
ApprovalGranted
TaskCompleted
```

State hiện tại có thể được dựng lại từ event log, hỗ trợ audit, replay và debugging.

## Concurrency

Nếu agent chạy nhiều subtask song song, shared state cần chiến lược consistency.

Hai worker có thể cùng sửa một resource. Cần optimistic locking, version check hoặc coordinator.

Agent orchestration không làm biến mất các bài toán distributed systems.

## Budget như biến điều khiển

Budget có thể gồm:

```text
số model call tối đa
số token tối đa
thời gian tối đa
chi phí tool tối đa
số write action tối đa
```

Policy có thể đổi model hoặc giảm search depth khi budget gần cạn.

## Phục hồi

Recovery không phải lúc nào cũng là retry. Có thể:

- rollback;
- chạy compensating action;
- đổi tool/provider;
- giảm scope;
- hỏi user;
- tiếp tục từ phần đã thành công.

## Lớp xác định bao quanh lõi xác suất

Một thiết kế mạnh là:

```text
Runtime xác định quản lý:
state
permission
budget
retry
logging
termination

LLM quản lý:
hiểu ngữ nghĩa
đề xuất plan
chọn next action trong không gian được phép
```

Đây là cách tách trách nhiệm quan trọng.

## Ví dụ: Research Agent

Task: so sánh ba vendor.

Loop có thể là:

```text
1. phân tích tiêu chí
2. search vendor A / B / C
3. lấy primary source
4. phát hiện tiêu chí còn thiếu
5. search evidence cụ thể
6. tạo bảng so sánh có cấu trúc
7. verify citation
8. hoàn thành
```

Nếu bước 4 phát hiện thiếu pricing, agent nên quay lại retrieval thay vì bịa từ memory.

## Ví dụ: Coding Agent

```text
đọc issue
→ search code liên quan
→ đọc test
→ sửa code
→ chạy focused test
→ đọc failure
→ sửa tiếp
→ chạy broader test
→ kiểm diff
→ kết thúc
```

Verification là một phần của loop, không phải post-processing tùy chọn.

## Mô hình tư duy

> **Agent loop là bộ điều khiển phản hồi cho một policy không hoàn hảo.**

Plan vòng hở giả định thế giới diễn ra đúng dự kiến; agent vòng kín liên tục quan sát và điều chỉnh.

## Những hiểu lầm thường gặp

### “Lập plan một lần rồi chạy hết là agent tốt”

Không. Environment thay đổi và tool có thể lỗi; replanning theo observation mới thường cần thiết.

### “Nhiều bước hơn nghĩa thông minh hơn”

Không. Nhiều bước có thể chỉ là đi vòng. Chất lượng nằm ở progress mỗi bước và verification.

### “Conversation history chính là state”

Transcript có thể chứa state nhưng structured persisted state đáng tin và dễ query hơn.

## Liên kết kiến thức

Agent loop nối trực giác control theory, state machine, distributed systems và classical agent architecture.

Xem tiếp: [Planning and Task Decomposition](./03_planning_and_task_decomposition.md).