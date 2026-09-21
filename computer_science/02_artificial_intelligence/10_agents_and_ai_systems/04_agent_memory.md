# Bộ nhớ của Agent

Agent thực hiện task dài hoặc quay lại qua nhiều session cần cơ chế nhớ có cấu trúc. **Bộ nhớ (memory / 메모리)** trong agent không phải một feature duy nhất và cũng không đồng nghĩa với vector database. Nó là tập hợp các cơ chế lưu trữ, truy xuất và cập nhật giúp agent giữ thông tin hữu ích theo thời gian.

Một taxonomy thực dụng:

```text
Working memory       → thông tin đang dùng cho task hiện tại
Episodic memory      → lịch sử sự kiện / trải nghiệm
Semantic memory      → fact / tri thức đã tổng hợp
Procedural memory    → cách làm, policy, workflow
External artifacts   → file, DB row, ticket, code, document
```

## Working Memory

Working memory là trạng thái ngắn hạn cần cho reasoning hiện tại:

```text
mục tiêu hiện tại
plan hiện tại
kết quả tool mới nhất
subtask đang chờ
constraint
```

Nó thường được đưa vào context window, nhưng source of truth nên có thể nằm trong structured state store.

Context window không phải durable memory. Khi context bị cắt, thông tin biến mất nếu chưa được persist.

## Episodic Memory

Episodic memory lưu “đã xảy ra gì”. Ví dụ:

```text
2026-09-20: lần deploy thất bại vì migration lock bị timeout
```

Nó hữu ích để học từ lần thử trước, audit và personalization.

Tuy nhiên raw event log có thể rất lớn, nên retrieval hoặc summarization policy cần chọn episode relevant.

## Semantic Memory

Semantic memory lưu fact đã được trừu tượng hóa khỏi event cụ thể:

```text
Service A yêu cầu Java 21
User thích giải thích tiếng Hàn ngắn gọn
API X giới hạn 100 request/phút
```

Fact nên có provenance, version và khoảng hiệu lực thời gian khi có thể. Tri thức lỗi thời là một failure mode của memory.

## Procedural Memory

Procedural memory mô tả “cách thực hiện”. Có thể là:

- runbook;
- workflow definition;
- pattern dùng tool;
- policy;
- checklist tái sử dụng.

Trong enterprise agent, tri thức thủ tục thường nên nằm trong document hoặc workflow tường minh thay vì chỉ “ẩn” trong prompt.

## Chính sách ghi Memory

Không nên lưu mọi thứ.

Trước khi ghi memory cần hỏi:

- thông tin này có ích dài hạn không?
- có nhạy cảm hoặc riêng tư không?
- đã có fact tương đương chưa?
- confidence và provenance có đủ không?
- retention policy có cho phép không?

Nếu mô hình tự lưu mọi câu user nói thành fact vĩnh viễn, memory sẽ nhanh chóng bị ô nhiễm.

## Chính sách truy xuất Memory

Khi đưa memory vào context, có thể xếp hạng theo:

```text
relevance
recency
importance
authority
scope
permission
```

Vector similarity chỉ giải quyết relevance theo embedding space, không tự xử lý freshness hoặc authorization.

## Vector Memory

Embedding memory hỗ trợ semantic retrieval:

\[
q = embed(query),\quad score_i = sim(q,m_i)
\]

Nhưng vẫn cần metadata filter:

```text
user_id
time range
workspace
memory type
access level
```

Không được truy xuất chéo user ngoài permission scope.

## Memory bằng tóm tắt

Lịch sử dài có thể được nén thành summary. Tuy nhiên tóm tắt là phép biến đổi mất mát.

Rủi ro:

```text
raw events → model summary → future agent coi summary là sự thật
```

Nếu summary sai, lỗi trở thành trạng thái bền vững. Fact quan trọng nên lưu thành structured record hoặc kèm link provenance.

## Quên cũng là một Feature

Memory không nên tăng vô hạn. Expiration và forgetting giúp:

- giảm nhiễu;
- loại fact lỗi thời;
- tuân thủ retention và privacy;
- giảm chi phí retrieval.

TTL có thể khác nhau theo loại memory.

## Giải quyết xung đột

Memory có thể mâu thuẫn:

```text
cũ: customer timezone = UTC
mới: customer timezone = Asia/Seoul
```

Hệ thống cần semantics về version và thời gian. Không nên chỉ retrieve cả hai rồi để LLM tự đoán.

## Memory và Database

Database vốn đã là hệ thống nhớ theo nghĩa rộng. Agent không cần copy structured fact vào vector database nếu relational lookup chính xác hơn.

Chọn storage theo kiểu truy vấn:

```text
state chính xác      → relational / KV DB
text ngữ nghĩa       → vector / search index
artifact lớn         → object / document store
lịch sử event        → log / event store
```

## Memory và RAG

RAG thường retrieve tri thức từ document bên ngoài. Agent memory retrieve lịch sử task, user hoặc system. Cơ chế có thể giống nhau nhưng semantics khác nhau.

## User Memory và Task Memory

Cần tách scope:

```text
Task memory   → chỉ phục vụ execution hiện tại
User memory   → preference / fact qua nhiều session
Team memory   → tri thức domain dùng chung
System memory → policy / runbook
```

Ranh giới scope cũng là ranh giới bảo mật.

## Memory Poisoning

Nếu attacker khiến nội dung độc hại được lưu lâu dài, các task tương lai có thể bị ảnh hưởng. Đây là phiên bản bền vững của prompt injection.

Write path cần validation và trust level; retrieval path phải coi memory là dữ liệu, không phải authority tuyệt đối.

## Ví dụ: Coding Agent

Một coding agent có thể lưu:

```text
working: file đang sửa + test failure
episodic: cách thử trước đã thất bại
semantic: repo dùng Java 21 + Gradle
procedural: contribution workflow
artifact: diff / commit thật
```

Codebase vẫn là source of truth; memory chỉ hỗ trợ navigation và reasoning.

## Metric chất lượng Memory

Có thể đánh giá:

- retrieval precision/recall;
- stale-memory rate;
- contradiction rate;
- useful-memory rate;
- unauthorized retrieval incident;
- số token context bị tiêu thụ.

“Agent nhớ nhiều” không phải metric chất lượng.

## Mô hình tư duy

> **Memory là trạng thái bên ngoài được quản lý, không phải transcript vô hạn.**

Kiến trúc memory tốt quyết định cái gì cần lưu, lưu ở đâu, bao lâu, ai được đọc và khi nào retrieve.

## Những hiểu lầm thường gặp

### “Vector DB = agent memory”

Không. Vector DB chỉ là một kỹ thuật lưu và retrieval phù hợp với một số loại memory.

### “Long context thay thế memory”

Không. Context vẫn hữu hạn, tốn chi phí và không giải quyết persistence, query hay versioning.

### “Memory càng nhiều agent càng thông minh”

Không. Nhiễu, fact cũ và xung đột có thể làm hiệu năng kém hơn.

## Liên kết kiến thức

Memory nối database, information retrieval, privacy, event sourcing và context engineering.

Xem tiếp: [Agent State and Context](./05_agent_state_and_context.md).