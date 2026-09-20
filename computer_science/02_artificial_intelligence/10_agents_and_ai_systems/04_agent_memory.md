# Agent Memory

Agent làm task dài hoặc quay lại nhiều session cần một cơ chế nhớ có cấu trúc. **Memory (메모리 / bộ nhớ)** trong agent không phải một feature duy nhất và cũng không đồng nghĩa vector database. Nó là family của storage + retrieval + update policies giúp agent giữ thông tin hữu ích qua time.

Một taxonomy thực dụng:

```text
Working memory       → thông tin đang dùng cho task hiện tại
Episodic memory      → lịch sử sự kiện / trải nghiệm
Semantic memory      → facts/knowledge đã tổng hợp
Procedural memory    → cách làm, policy, workflow
External artifacts   → files, DB rows, tickets, code, documents
```

## Working Memory

Working memory là state ngắn hạn đang cần cho reasoning hiện tại:

```text
current goal
current plan
latest tool results
pending subtasks
constraints
```

Nó thường được inject vào context window, nhưng source of truth nên có thể nằm trong structured state store.

Context window không phải durable memory. Khi context bị truncate, thông tin biến mất nếu không persisted.

## Episodic Memory

Episodic memory lưu “đã xảy ra gì”. Ví dụ:

```text
2026-09-20: deploy attempt failed because migration lock timed out
```

Nó hữu ích cho learning from previous attempts, audit và personalization.

Nhưng raw event log có thể rất lớn, nên retrieval/summarization policy cần chọn episode relevant.

## Semantic Memory

Semantic memory lưu facts đã abstraction khỏi event cụ thể:

```text
Service A requires Java 21
User prefers concise Korean explanations
API X rate limit is 100 requests/minute
```

Fact nên có provenance/version/time validity nếu có thể. Knowledge stale là một memory failure mode.

## Procedural Memory

Procedural memory mô tả “cách làm”. Có thể là:

- runbook;
- workflow definition;
- tool usage pattern;
- policy;
- reusable checklist.

Trong enterprise agent, procedural knowledge thường nên ở explicit docs/workflows thay vì chỉ “ẩn” trong prompt.

## Memory Write Policy

Không nên lưu mọi thứ.

Memory write cần hỏi:

- thông tin này có ích lâu dài không?
- có sensitive/private không?
- đã có fact tương đương chưa?
- confidence/provenance đủ không?
- retention policy cho phép không?

Nếu model tự lưu mọi câu user nói thành permanent fact, memory nhanh chóng ô nhiễm.

## Memory Retrieval Policy

Khi cần context, retrieve dựa trên:

```text
relevance
recency
importance
authority
scope
permission
```

Vector similarity chỉ giải quyết relevance theo embedding space, không tự giải quyết freshness hoặc authorization.

## Vector Memory

Embedding memory hỗ trợ semantic retrieval:

\[
q = embed(query),\quad score_i = sim(q,m_i)
\]

Nhưng cần metadata filter:

```text
user_id
time range
workspace
memory type
access level
```

Không nên cross-user retrieval ngoài permission scope.

## Summarization Memory

Long history có thể được compress thành summary. Nhưng summary là lossy transformation.

Risk:

```text
raw events → model summary → future agent treats summary as truth
```

Nếu summary sai, error persistent. Vì vậy critical facts nên lưu structured records hoặc link provenance.

## Forgetting là feature

Memory không nên grow forever. Forgetting/expiration giúp:

- giảm noise;
- loại stale facts;
- comply retention/privacy;
- giảm retrieval cost.

TTL có thể khác nhau theo memory type.

## Conflict Resolution

Memory có thể mâu thuẫn:

```text
old: customer timezone = UTC
new: customer timezone = Asia/Seoul
```

System cần version/time semantics. Không nên đơn giản retrieve cả hai rồi mong LLM tự đoán.

## Memory và Database

Database đã là memory system theo nghĩa broad. Một agent không cần duplicate structured facts vào vector DB nếu relational lookup chính xác hơn.

Chọn storage theo query pattern:

```text
exact state      → relational/KV DB
semantic text    → vector/search index
large artifacts  → object/document store
event history    → log/event store
```

## Memory và RAG

RAG thường retrieve external knowledge documents. Agent memory retrieve task/user/system history. Mechanism có thể giống nhau, semantics khác nhau.

## User Memory vs Task Memory

Tách scope:

```text
Task memory  → chỉ cho execution hiện tại
User memory  → preferences/facts across sessions
Team memory  → shared domain knowledge
System memory→ policies/runbooks
```

Scope boundary là security boundary.

## Memory Poisoning

Nếu attacker khiến malicious content được lưu lâu dài, future tasks có thể bị ảnh hưởng. Đây là persistence version của prompt injection.

Write path cần validation/trust level; retrieval path cần treat memory as data, không authority tuyệt đối.

## Example: coding agent

Một coding agent có thể lưu:

```text
working: files đang sửa + test failures
episodic: previous failed approach
semantic: repo uses Java 21 + Gradle
procedural: contribution workflow
artifact: actual diff/commit
```

Actual codebase vẫn là source of truth; memory chỉ hỗ trợ navigation/reasoning.

## Memory Quality Metrics

Có thể đánh giá:

- retrieval precision/recall;
- stale-memory rate;
- contradiction rate;
- useful-memory rate;
- unauthorized retrieval incidents;
- context tokens consumed.

“Agent nhớ nhiều” không phải metric tốt.

## Mental Model

> **Memory là managed external state, không phải một transcript vô hạn.**

Good memory architecture quyết định cái gì cần lưu, ở đâu, bao lâu, ai được đọc và khi nào retrieve.

## Common Misconceptions

### “Vector DB = agent memory”

Vector DB chỉ là một storage/retrieval technique cho một số memory types.

### “Long context thay thế memory”

Long context vẫn finite, costly và không giải quyết persistence/query/versioning.

### “Memory càng nhiều agent càng thông minh”

Noise, stale facts và conflict có thể làm performance tệ hơn.

## Knowledge Connection

Memory nối databases, information retrieval, privacy, event sourcing và context engineering. Phần tiếp theo phân biệt memory với state và context.

Xem tiếp: [Agent State and Context](./05_agent_state_and_context.md).