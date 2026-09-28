# Tác nhân (agent / 에이전트) bộ nhớ (memory / 메모리)

> **Mạch đọc:** Đặt **tác nhân (agent / 에이전트) bộ nhớ (memory / 메모리)** trong bản đồ [README](./README.md) để thấy đơn vị sở hữu (owner / 오너) và vị trí của nó. Nội dung đi từ **Working bộ nhớ (memory / 메모리)** sang **Episodic bộ nhớ (memory / 메모리)**; điểm nối này chuẩn bị câu hỏi cho các mục sau thay vì dừng ở định nghĩa đầu tiên.


Tác nhân (agent / 에이전트) làm tác vụ (task / 작업) dài hoặc quay lại nhiều session cần một cơ chế nhớ có cấu trúc. **bộ nhớ (memory / 메모리)** trong tác nhân (agent / 에이전트) không phải một tính năng (feature / 기능) duy nhất và cũng không đồng nghĩa véc-tơ (vector / 벡터) cơ sở dữ liệu (database / 데이터베이스). Nó là family của lưu trữ (storage / 저장소) + retrieval + cập nhật (update / 업데이트) policies giúp tác nhân (agent / 에이전트) giữ thông tin hữu ích qua thời gian (time / 시간).

Một taxonomy thực dụng:

```text
Working memory       → thông tin đang dùng cho task hiện tại
Episodic memory      → lịch sử sự kiện / trải nghiệm
Semantic memory      → facts/knowledge đã tổng hợp
Procedural memory    → cách làm, policy, workflow
External artifacts   → files, DB rows, tickets, code, documents
```

## Working bộ nhớ (memory / 메모리)

Working bộ nhớ (memory / 메모리) là trạng thái (state / 상태) ngắn hạn đang cần cho lập luận (reasoning / 추론) hiện tại:

```text
current goal
current plan
latest tool results
pending subtasks
constraints
```

Nó thường được inject vào ngữ cảnh (context / 맥락) cửa sổ (window / 윈도우), nhưng nguồn chuẩn (source of truth / 정본) nên có thể nằm trong structured trạng thái (state / 상태) store.

Ngữ cảnh (context / 맥락) cửa sổ (window / 윈도우) không phải durable bộ nhớ (memory / 메모리). Khi ngữ cảnh (context / 맥락) bị truncate, thông tin biến mất nếu không persisted.

## Episodic bộ nhớ (memory / 메모리)

Episodic bộ nhớ (memory / 메모리) lưu “đã xảy ra gì”. Ví dụ:

```text
2026-09-20: deploy attempt failed because migration lock timed out
```

Nó hữu ích cho học tập (learning / 학습) from previous attempts, kiểm tra (audit / 감사) và personalization.

Nhưng raw sự kiện (event / 이벤트) log có thể rất lớn, nên retrieval/summarization chính sách (policy / 정책) cần chọn episode relevant.

## Ngữ nghĩa (semantic / 의미적) bộ nhớ (memory / 메모리)

Ngữ nghĩa (semantic / 의미적) bộ nhớ (memory / 메모리) lưu facts đã lớp trừu tượng (abstraction / 추상화) khỏi sự kiện (event / 이벤트) cụ thể:

```text
Service A requires Java 21
User prefers concise Korean explanations
API X rate limit is 100 requests/minute
```

Fact nên có provenance/phiên bản (version / 버전)/thời gian (time / 시간) validity nếu có thể. kiến thức (knowledge / 지식) stale là một bộ nhớ (memory / 메모리) dạng thất bại (failure mode / 실패 모드).

## Procedural bộ nhớ (memory / 메모리)

Procedural bộ nhớ (memory / 메모리) mô tả “cách làm”. Có thể là:

- runbook;
- workflow definition;
- công cụ (tool / 도구) usage mẫu (pattern / 패턴);
- chính sách (policy / 정책);
- reusable checklist.

Trong enterprise tác nhân (agent / 에이전트), procedural kiến thức (knowledge / 지식) thường nên ở tường minh (explicit / 명시적) docs/workflows thay vì chỉ “ẩn” trong prompt.

## Bộ nhớ (memory / 메모리) ghi (write / 쓰기) chính sách (policy / 정책)

Không nên lưu mọi thứ.

Bộ nhớ (memory / 메모리) ghi (write / 쓰기) cần hỏi:

- thông tin này có ích lâu dài không?
- có sensitive/private không?
- đã có fact tương đương chưa?
- confidence/provenance đủ không?
- retention chính sách (policy / 정책) cho phép không?

Nếu mô hình (model / 모델) tự lưu mọi câu người dùng (user / 사용자) nói thành permanent fact, bộ nhớ (memory / 메모리) nhanh chóng ô nhiễm.

## Bộ nhớ (memory / 메모리) Retrieval chính sách (policy / 정책)

Khi cần ngữ cảnh (context / 맥락), retrieve dựa trên:

```text
relevance
recency
importance
authority
scope
permission
```

Véc-tơ (vector / 벡터) similarity chỉ giải quyết relevance theo embedding không gian (space / 공간), không tự giải quyết freshness hoặc authorization.

## Véc-tơ (vector / 벡터) bộ nhớ (memory / 메모리)

Embedding bộ nhớ (memory / 메모리) hỗ trợ ngữ nghĩa (semantic / 의미적) retrieval:

\[
q = embed(query),\quad score_i = sim(q,m_i)
\]

Nhưng cần siêu dữ liệu (metadata / 메타데이터) filter:

```text
user_id
time range
workspace
memory type
access level
```

Không nên cross-user retrieval ngoài permission phạm vi (scope / 범위).

## Summarization bộ nhớ (memory / 메모리)

Long lịch sử (history / 이력) có thể được compress thành summary. Nhưng summary là lossy transformation.

Rủi ro (risk / 위험):

```text
raw events → model summary → future agent treats summary as truth
```

Nếu summary sai, lỗi (error / 오류) persistent. Vì vậy trọng yếu (critical / 중요) facts nên lưu structured records hoặc link provenance.

## Forgetting là tính năng (feature / 기능)

Bộ nhớ (memory / 메모리) không nên grow forever. Forgetting/expiration giúp:

- giảm noise;
- loại stale facts;
- comply retention/privacy;
- giảm retrieval chi phí (cost / 비용).

TTL có thể khác nhau theo bộ nhớ (memory / 메모리) kiểu (type / 타입).

## Giải quyết xung đột (conflict resolution / 충돌 해결)

Bộ nhớ (memory / 메모리) có thể mâu thuẫn:

```text
old: customer timezone = UTC
new: customer timezone = Asia/Seoul
```

Hệ thống (system / 시스템) cần phiên bản (version / 버전)/thời gian (time / 시간) ngữ nghĩa (semantics / 의미론). Không nên đơn giản retrieve cả hai rồi mong LLM tự đoán.

## Bộ nhớ (memory / 메모리) và cơ sở dữ liệu (database / 데이터베이스)

Cơ sở dữ liệu (database / 데이터베이스) đã là bộ nhớ (memory / 메모리) hệ thống (system / 시스템) theo nghĩa broad. Một tác nhân (agent / 에이전트) không cần duplicate structured facts vào véc-tơ (vector / 벡터) DB nếu relational lookup chính xác hơn.

Chọn lưu trữ (storage / 저장소) theo truy vấn (query / 쿼리) mẫu (pattern / 패턴):

```text
exact state      → relational/KV DB
semantic text    → vector/search index
large artifacts  → object/document store
event history    → log/event store
```

## Bộ nhớ (memory / 메모리) và RAG

RAG thường retrieve bên ngoài (external / 외부) kiến thức (knowledge / 지식) documents. tác nhân (agent / 에이전트) bộ nhớ (memory / 메모리) retrieve tác vụ (task / 작업)/người dùng (user / 사용자)/hệ thống (system / 시스템) lịch sử (history / 이력). cơ chế (mechanism / 메커니즘) có thể giống nhau, ngữ nghĩa (semantics / 의미론) khác nhau.

## Người dùng (user / 사용자) bộ nhớ (memory / 메모리) vs tác vụ (task / 작업) bộ nhớ (memory / 메모리)

Tách phạm vi (scope / 범위):

```text
Task memory  → chỉ cho execution hiện tại
User memory  → preferences/facts across sessions
Team memory  → shared domain knowledge
System memory→ policies/runbooks
```

Phạm vi (scope / 범위) ranh giới (boundary / 경계) là ranh giới bảo mật (security boundary / 보안 경계).

## Bộ nhớ (memory / 메모리) Poisoning

Nếu attacker khiến malicious content được lưu lâu dài, future tasks có thể bị ảnh hưởng. Đây là persistence phiên bản (version / 버전) của prompt injection.

Ghi (write / 쓰기) đường dẫn (path / 경로) cần kiểm tra hợp lệ (validation / 검증)/trust mức (level / 수준); retrieval đường dẫn (path / 경로) cần treat bộ nhớ (memory / 메모리) as dữ liệu (data / 데이터), không authority tuyệt đối.

## Example: coding tác nhân (agent / 에이전트)

Một coding tác nhân (agent / 에이전트) có thể lưu:

```text
working: files đang sửa + test failures
episodic: previous failed approach
semantic: repo uses Java 21 + Gradle
procedural: contribution workflow
artifact: actual diff/commit
```

Actual codebase vẫn là nguồn chuẩn (source of truth / 정본); bộ nhớ (memory / 메모리) chỉ hỗ trợ điều hướng (navigation / 내비게이션)/lập luận (reasoning / 추론).

## Bộ nhớ (memory / 메모리) chất lượng (quality / 품질) Metrics

Có thể đánh giá:

- retrieval precision/recall;
- stale-memory tỷ lệ (rate / 비율);
- contradiction tỷ lệ (rate / 비율);
- useful-memory tỷ lệ (rate / 비율);
- unauthorized retrieval incidents;
- ngữ cảnh (context / 맥락) tokens consumed.

“tác nhân (agent / 에이전트) nhớ nhiều” không phải chỉ số (metric / 지표) tốt.

## Mô hình tư duy (mental model / 사고 모델)

> **bộ nhớ (memory / 메모리) là managed bên ngoài (external / 외부) trạng thái (state / 상태), không phải một transcript vô hạn.**

Good bộ nhớ (memory / 메모리) kiến trúc (architecture / 아키텍처) quyết định cái gì cần lưu, ở đâu, bao lâu, ai được đọc và khi nào retrieve.

## Dùng chung (common / 공통) Misconceptions

### “véc-tơ (vector / 벡터) DB = tác nhân (agent / 에이전트) bộ nhớ (memory / 메모리)”

Véc-tơ (vector / 벡터) DB chỉ là một lưu trữ (storage / 저장소)/retrieval technique cho một số bộ nhớ (memory / 메모리) types.

### “Long ngữ cảnh (context / 맥락) thay thế bộ nhớ (memory / 메모리)”

Long ngữ cảnh (context / 맥락) vẫn finite, costly và không giải quyết persistence/truy vấn (query / 쿼리)/versioning.

### “bộ nhớ (memory / 메모리) càng nhiều tác nhân (agent / 에이전트) càng thông minh”

Noise, stale facts và xung đột (conflict / 충돌) có thể làm hiệu năng (performance / 성능) tệ hơn.

## Liên kết kiến thức (knowledge connection / 지식 연결)

Bộ nhớ (memory / 메모리) nối databases, thông tin (information / 정보) retrieval, privacy, sự kiện (event / 이벤트) sourcing và ngữ cảnh (context / 맥락) kỹ thuật (engineering / 엔지니어링). Phần tiếp theo phân biệt bộ nhớ (memory / 메모리) với trạng thái (state / 상태) và ngữ cảnh (context / 맥락).

Xem tiếp: [Agent State and Context](./05_agent_state_and_context.md).

> **Bàn giao:** Sau **liên kết kiến thức (knowledge connection / 지식 연결)**, hãy chốt bất biến (invariant / 불변식) và giới hạn của mục này trước khi nối sang kiến thức kế tiếp. Có thể đọc tiếp [00 from llm to agent](./00_from_llm_to_agent.md) để đối chiếu ranh giới (boundary / 경계) gần nhất.
