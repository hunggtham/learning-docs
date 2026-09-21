# Workflow và Agent khác nhau như thế nào?

Hai thuật ngữ này thường bị dùng như từ đồng nghĩa, nhưng chúng đại diện cho hai cách phân bổ **quyền quyết định (decision authority)** khác nhau trong một hệ thống.

**Quy trình (workflow / 워크플로)** có luồng điều khiển (control flow) chủ yếu được developer định nghĩa trước. **Agent** trao cho mô hình nhiều quyền hơn để quyết định bước tiếp theo dựa trên state và observation hiện tại.

```text
Workflow:
step A → nếu X thì B, nếu không thì C → D

Agent:
quan sát state → chọn action được phép → nhận kết quả → lặp lại
```

## Tính xác định và tính linh hoạt

Workflow mạnh khi quy trình ổn định, yêu cầu audit cao và logic phân nhánh đã biết trước.

Agent hữu ích hơn khi:

- input không có schema cố định;
- task có nhiều đường giải hợp lệ;
- cần diễn giải natural language;
- environment khó dự đoán;
- chuỗi action khó mã hóa đầy đủ bằng rule.

Không nên dùng agent chỉ vì nó là kiến trúc mới hơn hoặc nghe “thông minh” hơn.

## Kiến trúc Hybrid

Trong production, kiến trúc lai (hybrid architecture) thường đáng tin cậy nhất:

```text
Lớp workflow có tính xác định
      ↓
Quyết định agentic tại node mơ hồ
      ↓
Validation / execution có tính xác định
```

Ví dụ xử lý claim:

```text
nhận claim
→ kiểm tra field bắt buộc [deterministic]
→ phân loại narrative bất thường [LLM]
→ retrieve policy [deterministic / RAG]
→ quyết định có cần human review hay không [policy + model]
→ thực thi payment [deterministic + approval]
```

Trong thiết kế này, LLM chỉ được dùng tại những điểm cần hiểu ngữ nghĩa hoặc xử lý không chắc chắn.

## Vì sao Workflow dễ kiểm thử hơn?

Do transition đã biết trước, unit test và integration test có thể cover branch rõ ràng hơn.

Agent có hành vi xác suất hơn; evaluation cần scenario suite, trajectory analysis và end-to-end task test thay vì chỉ kiểm output của một hàm.

## Reliability Composition

Workflow có ít quyết định do mô hình đưa ra hơn nên giảm **uncertainty tích lũy**. Nếu phần lớn step là deterministic và hệ thống chỉ có hai agentic decision thay vì mười quyết định nối tiếp, độ tin cậy end-to-end thường dễ kiểm soát hơn.

Đây là lý do “giảm số bước cần AI” đôi khi cải thiện hệ thống nhiều hơn đổi sang model lớn hơn.

## Chi phí

Agent loop có thể gọi model nhiều lần. Workflow có thể giới hạn việc gọi model đúng vào những điểm cần semantic intelligence.

Nguyên tắc tối ưu quan trọng:

> **Dùng code có tính xác định cho phần có thể xác định; dùng mô hình cho phần chứa mơ hồ, ngữ nghĩa hoặc uncertainty.**

## Khả năng giải thích và Audit

Workflow có branch rõ nên dễ giải thích “vì sao action này xảy ra”. Agent cần log đầy đủ:

```text
state trước quyết định
evidence đã dùng
tool call
arguments
observation
verification result
state sau quyết định
```

Nếu không có trajectory log, việc điều tra lỗi agent rất dễ biến thành suy đoán.

## Cô lập lỗi

Hybrid system có thể cô lập lỗi từ mô hình:

```text
model output không hợp lệ
→ fallback sang route deterministic hoặc manual review
```

Nếu toàn bộ application là một giant agent loop, **phạm vi ảnh hưởng khi lỗi xảy ra (blast radius)** thường lớn hơn.

## Khi nào nên ưu tiên Workflow?

Workflow thường phù hợp với:

- quy trình chịu ràng buộc compliance;
- phép tính tài chính chính xác;
- approval chain cố định;
- ETL hoặc data pipeline lặp lại;
- orchestration API đã biết;
- state transition được business rule định nghĩa rõ.

Trong những trường hợp này, việc để LLM tự quyết định đường đi thường tạo thêm variance mà không đem lại giá trị tương xứng.

## Khi nào Agent tạo thêm giá trị?

Agent thường hữu ích với:

- nghiên cứu mở;
- debugging codebase chưa biết trước;
- lựa chọn giữa nhiều heterogeneous tool;
- phân tích hồ sơ hoặc tài liệu phức tạp;
- planning khi observation mới liên tục thay đổi next step.

## Pattern Agent-in-Workflow

Một node như `AnalyzeCase` có thể chạy một agent nội bộ, nhưng outer workflow vẫn sở hữu:

```text
timeout
retry
approval
durable state
SLA
next deterministic step
```

Agent được giới hạn trong phạm vi một node thay vì sở hữu toàn bộ quy trình nghiệp vụ.

## Pattern Workflow-in-Agent

Ngược lại, agent có thể gọi một workflow đã biết như một high-level tool:

```text
agent quyết định “run onboarding workflow”
→ workflow engine thực hiện 12 bước deterministic
→ trả structured result về agent
```

Cách này thường an toàn hơn việc cho agent gọi 12 low-level API riêng lẻ và tự quản lý toàn bộ transaction semantics.

## Quyền sở hữu State

Workflow engine nên sở hữu **durable process state**. Agent context chỉ nhận phần state liên quan tới quyết định hiện tại.

Nếu cả workflow engine và LLM cùng tự sửa một bản state không có versioning, hệ thống dễ phát sinh drift và race condition.

## Autonomy Budget

Có thể xem autonomy như một tài nguyên cần phân bổ:

```text
0% autonomy  → workflow hoàn toàn deterministic
20%          → LLM phân loại / trích xuất tại một vài node
50%          → agent chọn tool nhưng không tự write
80%          → agent planning nhiều bước với approval boundary
100%         → agent tự quyết phần lớn action
```

Không có mức càng cao càng tốt. Mức phù hợp phụ thuộc độ không chắc chắn của task, khả năng verify và chi phí khi sai.

## Mô hình tư duy

> **Workflow quyết định đường đi trước khi chạy; agent quyết định một phần đường đi trong lúc chạy. Hybrid system chọn đúng mức autonomy cho từng đoạn của quy trình.**

## Những nhầm lẫn thường gặp

### “Agent thay thế workflow engine”

Không. Scheduling, persistence, retry, transaction và orchestration vẫn là bài toán systems engineering.

### “Workflow thì không phải AI”

Không đúng. Workflow có thể chứa ML hoặc LLM node. “Có AI hay không” và “workflow hay agent” là hai trục khác nhau.

### “Càng agentic thì càng mạnh”

Autonomy cao hơn cũng đồng nghĩa variance, chi phí, attack surface và risk cao hơn.

## Liên kết kiến thức

Phân biệt workflow và agent là nền cho các phần orchestration, multi-agent và reliability ở phía sau. Nó cũng nối trực tiếp với software architecture, distributed systems và business process management.

Xem tiếp: [Hệ thống Multi-Agent](./07_multi_agent_systems.md).