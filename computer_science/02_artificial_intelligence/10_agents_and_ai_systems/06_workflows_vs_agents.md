# Workflow và tác nhân (agent / 에이전트) khác nhau như thế nào?

> **Mạch đọc:** [README](./README.md) là bản đồ owner của **Workflow và tác nhân (agent / 에이전트) khác nhau như thế nào?**; nhìn vào vị trí đó trước để biết file này đang phục vụ nhánh kiến thức nào. **Determinism vs Flexibility** mở đối tượng chính của file và câu hỏi cần theo dõi; sau đó sang **Hybrid kiến trúc (architecture / 아키텍처)** để mở rộng đối tượng sang phạm vi kế cận. Cách đi này giữ lại điểm tựa của section đầu và cho biết kết luận sẽ được dùng ở đâu, thay vì dừng ở định nghĩa đầu tiên.

Hai từ này thường bị dùng như synonym nhưng chúng đại diện hai cách phân bổ quyền quyết định khác nhau.

**Workflow (워크플로 / quy trình)** có điều khiển (control / 제어) luồng (flow / 흐름) chủ yếu được nhà phát triển (developer / 개발자) định nghĩa trước. **tác nhân (agent / 에이전트)** cho mô hình (model / 모델) quyết định nhiều hơn về next step dựa trên trạng thái (state / 상태)/observation hiện tại.

```text
Workflow:
step A → if X then B else C → D

Agent:
observe state → choose among allowed actions → observe result → repeat
```

## Determinism vs Flexibility

Workflow mạnh khi tiến trình (process / 프로세스) ổn định, auditability cao và branching lô-gic (logic / 논리) biết trước.

Tác nhân (agent / 에이전트) mạnh khi:

- đầu vào (input / 입력) không có lược đồ (schema / 스키마) cố định;
- tác vụ (task / 작업) có nhiều đường giải;
- cần interpret natural ngôn ngữ (language / 언어);
- môi trường (environment / 환경) không predictable;
- hành động (action / 동작) chuỗi (sequence / 시퀀스) khó encode hết bằng rules.

Không nên dùng tác nhân (agent / 에이전트) chỉ vì “AI mới hơn”.

> **Chuyển mạch:** Trong **Workflow và tác nhân (agent / 에이전트) khác nhau như thế nào?**, **Hybrid kiến trúc (architecture / 아키텍처)** tiếp nhận điểm tựa từ **Determinism vs Flexibility** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Why Workflow is Easier to kiểm thử (test / 테스트)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Hybrid kiến trúc (architecture / 아키텍처)

Thiết kế môi trường vận hành (production / 운영 환경) thường tốt nhất:

```text
Deterministic workflow shell
      ↓
Agentic decision at ambiguous node
      ↓
Deterministic validation / execution
```

Ví dụ claims processing:

```text
receive claim
→ validate required fields [deterministic]
→ classify unusual narrative [LLM]
→ retrieve policy [deterministic/RAG]
→ decide whether human review needed [policy + model]
→ payment execution [deterministic + approval]
```

> **Chuyển mạch:** Ở chặng này của **Workflow và tác nhân (agent / 에이전트) khác nhau như thế nào?**, **Hybrid kiến trúc (architecture / 아키텍처)** xác định đầu vào; **Why Workflow is Easier to kiểm thử (test / 테스트)** giải thích bước vận hành tạo ra kết quả kế tiếp. Từ đây, **Độ tin cậy (reliability / 신뢰성) Composition** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Why Workflow is Easier to kiểm thử (test / 테스트)

Vì transitions known trước, đơn vị (unit / 단위)/tích hợp (integration / 통합) tests có thể cover branches rõ hơn.

Tác nhân (agent / 에이전트) hành vi (behavior / 동작) stochastic hơn; evaluation cần scenario suites và trajectory phân tích (analysis / 분석).

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Workflow và tác nhân (agent / 에이전트) khác nhau như thế nào?**, **Why Workflow is Easier to kiểm thử (test / 테스트)** xác định đầu vào; **Độ tin cậy (reliability / 신뢰성) Composition** giải thích bước vận hành tạo ra kết quả kế tiếp. Từ đây, **Chi phí (cost / 비용)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Độ tin cậy (reliability / 신뢰성) Composition

Workflow có fewer mô hình (model / 모델) decisions nên giảm compounded bất định (uncertainty / 불확실성). Nếu deterministic step có tính đúng đắn (correctness / 정확성) gần 1 và chỉ 2 agentic decisions thay vì 10, end-to-end độ tin cậy (reliability / 신뢰성) thường tốt hơn.

> **Chuyển mạch:** Trong **Workflow và tác nhân (agent / 에이전트) khác nhau như thế nào?**, **Chi phí (cost / 비용)** tiếp nhận điểm tựa từ **Độ tin cậy (reliability / 신뢰성) Composition** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Explainability và kiểm tra (audit / 감사)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Chi phí (cost / 비용)

Tác nhân (agent / 에이전트) vòng lặp (loop / 루프) gọi mô hình (model / 모델) nhiều lần. Workflow có thể gọi mô hình (model / 모델) đúng nơi cần ngữ nghĩa (semantic / 의미적) intelligence.

Tối ưu hóa (optimization / 최적화) principle:

> **Dùng deterministic mã (code / 코드) cho phần deterministic; dùng mô hình (model / 모델) cho phần bất định (uncertainty / 불확실성)/ngữ nghĩa (semantics / 의미론).**

> **Chuyển mạch:** Ở chặng này của **Workflow và tác nhân (agent / 에이전트) khác nhau như thế nào?**, **Explainability và kiểm tra (audit / 감사)** tiếp nhận điểm tựa từ **Chi phí (cost / 비용)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Thất bại (failure / 실패) Isolation** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Explainability và kiểm tra (audit / 감사)

Workflow branch rõ giúp explain “vì sao hành động (action / 동작) xảy ra”. tác nhân (agent / 에이전트) cần log trạng thái (state / 상태), công cụ (tool / 도구) calls, selected bằng chứng (evidence / 증거) và xác minh (verification / 확인) results để reconstruct trajectory.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Workflow và tác nhân (agent / 에이전트) khác nhau như thế nào?**, **Thất bại (failure / 실패) Isolation** tiếp nhận điểm tựa từ **Explainability và kiểm tra (audit / 감사)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **When to Prefer Workflow** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Thất bại (failure / 실패) Isolation

Hybrid hệ thống (system / 시스템) có thể isolate AI thất bại (failure / 실패):

```text
model output invalid
→ fallback deterministic/manual route
```

Nếu toàn bộ ứng dụng (application / 애플리케이션) là one giant tác nhân (agent / 에이전트) vòng lặp (loop / 루프), blast radius lớn hơn.

> **Chuyển mạch:** Trong **Workflow và tác nhân (agent / 에이전트) khác nhau như thế nào?**, **Thất bại (failure / 실패) Isolation** xác định đầu vào; **When to Prefer Workflow** giải thích bước vận hành tạo ra kết quả kế tiếp. Từ đây, **When tác nhân (agent / 에이전트) Adds giá trị (value / 값)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## When to Prefer Workflow

Phần này chuyển khái niệm Computer Science thành cấu trúc, ví dụ hoặc quy trình có thể kiểm tra. Hãy xác định câu hỏi mà mục trả lời rồi nối kết luận với phần kế tiếp.

- compliance-heavy process;
- exact financial calculation;
- fixed approval chain;
- repeated ETL/data pipeline;
- known API orchestration;
- trạng thái (state / 상태) transitions defined by nghiệp vụ (business / 비즈니스) rules.

> **Chuyển mạch:** Ở chặng này của **Workflow và tác nhân (agent / 에이전트) khác nhau như thế nào?**, **When to Prefer Workflow** xác định đầu vào; **When tác nhân (agent / 에이전트) Adds giá trị (value / 값)** giải thích bước vận hành tạo ra kết quả kế tiếp. Từ đây, **Agent-in-Workflow mẫu (pattern / 패턴)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## When tác nhân (agent / 에이전트) Adds giá trị (value / 값)

Phần này chuyển khái niệm Computer Science thành cấu trúc, ví dụ hoặc quy trình có thể kiểm tra. Hãy xác định câu hỏi mà mục trả lời rồi nối kết luận với phần kế tiếp.

- open-ended research;
- debugging unknown codebase;
- heterogeneous công cụ (tool / 도구) discovery;
- document-heavy trường hợp (case / 사례) phân tích (analysis / 분석);
- planning under changing observations.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Workflow và tác nhân (agent / 에이전트) khác nhau như thế nào?**, **When tác nhân (agent / 에이전트) Adds giá trị (value / 값)** xác định đầu vào; **Agent-in-Workflow mẫu (pattern / 패턴)** giải thích bước vận hành tạo ra kết quả kế tiếp. Từ đây, **Workflow-in-Agent mẫu (pattern / 패턴)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Agent-in-Workflow mẫu (pattern / 패턴)

Một nút (node / 노드) `AnalyzeCase` có thể internally chạy tác nhân (agent / 에이전트), nhưng outer workflow owns:

```text
timeout
retry
approval
state
SLA
next deterministic step
```

> **Chuyển mạch:** Trong **Workflow và tác nhân (agent / 에이전트) khác nhau như thế nào?**, **Agent-in-Workflow mẫu (pattern / 패턴)** xác định đầu vào; **Workflow-in-Agent mẫu (pattern / 패턴)** giải thích bước vận hành tạo ra kết quả kế tiếp. Từ đây, **Quyền sở hữu trạng thái (state ownership / 상태 소유권)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Workflow-in-Agent mẫu (pattern / 패턴)

Tác nhân (agent / 에이전트) có thể invoke a known workflow as one high-level công cụ (tool / 도구):

```text
agent decides “run onboarding workflow”
→ workflow engine executes 12 deterministic steps
→ returns result
```

Đây thường tốt hơn để tác nhân (agent / 에이전트) gọi 12 low-level APIs riêng.

> **Chuyển mạch:** Ở chặng này của **Workflow và tác nhân (agent / 에이전트) khác nhau như thế nào?**, **Workflow-in-Agent mẫu (pattern / 패턴)** xác định đầu vào; **Quyền sở hữu trạng thái (state ownership / 상태 소유권)** giải thích bước vận hành tạo ra kết quả kế tiếp. Từ đây, **Mô hình tư duy (mental model / 사고 모델)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Quyền sở hữu trạng thái (state ownership / 상태 소유권)

Workflow engine nên own durable tiến trình (process / 프로세스) trạng thái (state / 상태). tác nhân (agent / 에이전트) ngữ cảnh (context / 맥락) chỉ nhận relevant view.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Workflow và tác nhân (agent / 에이전트) khác nhau như thế nào?**, **Mô hình tư duy (mental model / 사고 모델)** gom các mảnh từ **Quyền sở hữu trạng thái (state ownership / 상태 소유권)** thành một kết luận có thể mang sang phần kế tiếp. Từ đây, **Dùng chung (common / 공통) Misconceptions** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Mô hình tư duy (mental model / 사고 모델)

> **Workflow quyết định đường đi trước; tác nhân (agent / 에이전트) quyết định đường đi trong lúc chạy. Hybrid hệ thống (system / 시스템) chọn đúng mức autonomy cho từng đoạn.**

> **Chuyển mạch:** Trong **Workflow và tác nhân (agent / 에이전트) khác nhau như thế nào?**, **Dùng chung (common / 공통) Misconceptions** gom các mảnh từ **Mô hình tư duy (mental model / 사고 모델)** thành một kết luận có thể mang sang phần kế tiếp. Từ đây, **Liên kết kiến thức (knowledge connection / 지식 연결)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Dùng chung (common / 공통) Misconceptions

### “tác nhân (agent / 에이전트) thay thế workflow engine”

Không. Scheduling, persistence, thử lại (retry / 재시도) và transactional orchestration vẫn là các hệ thống (systems / 시스템들) problems.

### “Workflow không phải AI”

Workflow có thể chứa ML/LLM nodes. AI vs workflow là khác axis.

### “More agentic = more capable”

More autonomy cũng nghĩa more variance, chi phí (cost / 비용) và rủi ro (risk / 위험).

> **Chuyển mạch:** Ở chặng này của **Workflow và tác nhân (agent / 에이전트) khác nhau như thế nào?**, sau nội dung của **Dùng chung (common / 공통) Misconceptions**, **Liên kết kiến thức (knowledge connection / 지식 연결)** chỉ rõ tài liệu chuẩn và vị trí sở hữu để người học biết phần nào cần quay lại khi muốn đào sâu. Phần còn lại của file dùng kết quả này để khép lại mạch giải thích.

## Liên kết kiến thức (knowledge connection / 지식 연결)

Phân biệt này là nền cho hệ thống (system / 시스템) thiết kế (design / 설계) ở các chapter orchestration và độ tin cậy (reliability / 신뢰성).

Xem tiếp: [Multi-Agent Systems](./07_multi_agent_systems.md).

> **Bàn giao:** Sau **Liên kết kiến thức (knowledge connection / 지식 연결)**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](./README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
