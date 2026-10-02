# Tác nhân (agent / 에이전트) bộ nhớ (memory / 메모리)

> **Mạch đọc:** [README](./README.md) là bản đồ owner của **Agent memory**. Route đi từ working context → episodic traces → semantic/user memory → retrieval/write policy → forgetting, privacy, and staleness, để memory được thiết kế theo nhu cầu và rủi ro.

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

> **Chuyển mạch:** Trong **Tác nhân (agent / 에이전트) bộ nhớ (memory / 메모리)**, **Episodic bộ nhớ (memory / 메모리)** tiếp nhận điểm tựa từ **Working bộ nhớ (memory / 메모리)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Ngữ nghĩa (semantic / 의미적) bộ nhớ (memory / 메모리)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Episodic bộ nhớ (memory / 메모리)

Episodic bộ nhớ (memory / 메모리) lưu “đã xảy ra gì”. Ví dụ:

```text
2026-09-20: deploy attempt failed because migration lock timed out
```

Nó hữu ích cho học tập (learning / 학습) from previous attempts, kiểm tra (audit / 감사) và personalization.

Nhưng raw sự kiện (event / 이벤트) log có thể rất lớn, nên retrieval/summarization chính sách (policy / 정책) cần chọn episode relevant.

> **Chuyển mạch:** Ở chặng này của **Tác nhân (agent / 에이전트) bộ nhớ (memory / 메모리)**, **Ngữ nghĩa (semantic / 의미적) bộ nhớ (memory / 메모리)** tiếp nhận điểm tựa từ **Episodic bộ nhớ (memory / 메모리)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Procedural bộ nhớ (memory / 메모리)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Ngữ nghĩa (semantic / 의미적) bộ nhớ (memory / 메모리)

Ngữ nghĩa (semantic / 의미적) bộ nhớ (memory / 메모리) lưu facts đã lớp trừu tượng (abstraction / 추상화) khỏi sự kiện (event / 이벤트) cụ thể:

```text
Service A requires Java 21
User prefers concise Korean explanations
API X rate limit is 100 requests/minute
```

Fact nên có provenance/phiên bản (version / 버전)/thời gian (time / 시간) validity nếu có thể. kiến thức (knowledge / 지식) stale là một bộ nhớ (memory / 메모리) dạng thất bại (failure mode / 실패 모드).

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Tác nhân (agent / 에이전트) bộ nhớ (memory / 메모리)**, **Procedural bộ nhớ (memory / 메모리)** tiếp nhận điểm tựa từ **Ngữ nghĩa (semantic / 의미적) bộ nhớ (memory / 메모리)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Bộ nhớ (memory / 메모리) ghi (write / 쓰기) chính sách (policy / 정책)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Procedural bộ nhớ (memory / 메모리)

Procedural bộ nhớ (memory / 메모리) mô tả “cách làm”. Có thể là:

- runbook;
- workflow definition;
- công cụ (tool / 도구) usage mẫu (pattern / 패턴);
- chính sách (policy / 정책);
- reusable checklist.

Trong enterprise tác nhân (agent / 에이전트), procedural kiến thức (knowledge / 지식) thường nên ở tường minh (explicit / 명시적) docs/workflows thay vì chỉ “ẩn” trong prompt.

> **Chuyển mạch:** Trong **Tác nhân (agent / 에이전트) bộ nhớ (memory / 메모리)**, **Bộ nhớ (memory / 메모리) ghi (write / 쓰기) chính sách (policy / 정책)** tiếp nhận điểm tựa từ **Procedural bộ nhớ (memory / 메모리)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Bộ nhớ (memory / 메모리) Retrieval chính sách (policy / 정책)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Bộ nhớ (memory / 메모리) ghi (write / 쓰기) chính sách (policy / 정책)

Không nên lưu mọi thứ.

Bộ nhớ (memory / 메모리) ghi (write / 쓰기) cần hỏi:

- thông tin này có ích lâu dài không?
- có sensitive/private không?
- đã có fact tương đương chưa?
- confidence/provenance đủ không?
- retention chính sách (policy / 정책) cho phép không?

Nếu mô hình (model / 모델) tự lưu mọi câu người dùng (user / 사용자) nói thành permanent fact, bộ nhớ (memory / 메모리) nhanh chóng ô nhiễm.

> **Chuyển mạch:** Ở chặng này của **Tác nhân (agent / 에이전트) bộ nhớ (memory / 메모리)**, **Bộ nhớ (memory / 메모리) Retrieval chính sách (policy / 정책)** tiếp nhận điểm tựa từ **Bộ nhớ (memory / 메모리) ghi (write / 쓰기) chính sách (policy / 정책)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Véc-tơ (vector / 벡터) bộ nhớ (memory / 메모리)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

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

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Tác nhân (agent / 에이전트) bộ nhớ (memory / 메모리)**, **Véc-tơ (vector / 벡터) bộ nhớ (memory / 메모리)** tiếp nhận điểm tựa từ **Bộ nhớ (memory / 메모리) Retrieval chính sách (policy / 정책)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Summarization bộ nhớ (memory / 메모리)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

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

> **Chuyển mạch:** Trong **Tác nhân (agent / 에이전트) bộ nhớ (memory / 메모리)**, **Summarization bộ nhớ (memory / 메모리)** tiếp nhận điểm tựa từ **Véc-tơ (vector / 벡터) bộ nhớ (memory / 메모리)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Forgetting là tính năng (feature / 기능)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Summarization bộ nhớ (memory / 메모리)

Long lịch sử (history / 이력) có thể được compress thành summary. Nhưng summary là lossy transformation.

Rủi ro (risk / 위험):

```text
raw events → model summary → future agent treats summary as truth
```

Nếu summary sai, lỗi (error / 오류) persistent. Vì vậy trọng yếu (critical / 중요) facts nên lưu structured records hoặc link provenance.

> **Chuyển mạch:** Ở chặng này của **Tác nhân (agent / 에이전트) bộ nhớ (memory / 메모리)**, **Forgetting là tính năng (feature / 기능)** tiếp nhận điểm tựa từ **Summarization bộ nhớ (memory / 메모리)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Giải quyết xung đột (conflict resolution / 충돌 해결)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Forgetting là tính năng (feature / 기능)

Bộ nhớ (memory / 메모리) không nên grow forever. Forgetting/expiration giúp:

- giảm noise;
- loại stale facts;
- comply retention/privacy;
- giảm retrieval chi phí (cost / 비용).

TTL có thể khác nhau theo bộ nhớ (memory / 메모리) kiểu (type / 타입).

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Tác nhân (agent / 에이전트) bộ nhớ (memory / 메모리)**, **Giải quyết xung đột (conflict resolution / 충돌 해결)** tiếp nhận điểm tựa từ **Forgetting là tính năng (feature / 기능)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Bộ nhớ (memory / 메모리) và cơ sở dữ liệu (database / 데이터베이스)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Giải quyết xung đột (conflict resolution / 충돌 해결)

Bộ nhớ (memory / 메모리) có thể mâu thuẫn:

```text
old: customer timezone = UTC
new: customer timezone = Asia/Seoul
```

Hệ thống (system / 시스템) cần phiên bản (version / 버전)/thời gian (time / 시간) ngữ nghĩa (semantics / 의미론). Không nên đơn giản retrieve cả hai rồi mong LLM tự đoán.

> **Chuyển mạch:** Trong **Tác nhân (agent / 에이전트) bộ nhớ (memory / 메모리)**, **Giải quyết xung đột (conflict resolution / 충돌 해결)** nêu điều cần giải thích; **Bộ nhớ (memory / 메모리) và cơ sở dữ liệu (database / 데이터베이스)** đối chiếu nó với bằng chứng hoặc nguồn kiểm chứng. Từ đây, **Bộ nhớ (memory / 메모리) và RAG** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Bộ nhớ (memory / 메모리) và cơ sở dữ liệu (database / 데이터베이스)

Cơ sở dữ liệu (database / 데이터베이스) đã là bộ nhớ (memory / 메모리) hệ thống (system / 시스템) theo nghĩa broad. Một tác nhân (agent / 에이전트) không cần duplicate structured facts vào véc-tơ (vector / 벡터) DB nếu relational lookup chính xác hơn.

Chọn lưu trữ (storage / 저장소) theo truy vấn (query / 쿼리) mẫu (pattern / 패턴):

```text
exact state      → relational/KV DB
semantic text    → vector/search index
large artifacts  → object/document store
event history    → log/event store
```

> **Chuyển mạch:** Ở chặng này của **Tác nhân (agent / 에이전트) bộ nhớ (memory / 메모리)**, **Bộ nhớ (memory / 메모리) và cơ sở dữ liệu (database / 데이터베이스)** nêu điều cần giải thích; **Bộ nhớ (memory / 메모리) và RAG** đối chiếu nó với bằng chứng hoặc nguồn kiểm chứng. Từ đây, **Người dùng (user / 사용자) bộ nhớ (memory / 메모리) vs tác vụ (task / 작업) bộ nhớ (memory / 메모리)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Bộ nhớ (memory / 메모리) và RAG

RAG thường retrieve bên ngoài (external / 외부) kiến thức (knowledge / 지식) documents. tác nhân (agent / 에이전트) bộ nhớ (memory / 메모리) retrieve tác vụ (task / 작업)/người dùng (user / 사용자)/hệ thống (system / 시스템) lịch sử (history / 이력). cơ chế (mechanism / 메커니즘) có thể giống nhau, ngữ nghĩa (semantics / 의미론) khác nhau.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Tác nhân (agent / 에이전트) bộ nhớ (memory / 메모리)**, **Người dùng (user / 사용자) bộ nhớ (memory / 메모리) vs tác vụ (task / 작업) bộ nhớ (memory / 메모리)** tiếp nhận điểm tựa từ **Bộ nhớ (memory / 메모리) và RAG** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Bộ nhớ (memory / 메모리) Poisoning** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Người dùng (user / 사용자) bộ nhớ (memory / 메모리) vs tác vụ (task / 작업) bộ nhớ (memory / 메모리)

Tách phạm vi (scope / 범위):

```text
Task memory  → chỉ cho execution hiện tại
User memory  → preferences/facts across sessions
Team memory  → shared domain knowledge
System memory→ policies/runbooks
```

Phạm vi (scope / 범위) ranh giới (boundary / 경계) là ranh giới bảo mật (security boundary / 보안 경계).

> **Chuyển mạch:** Trong **Tác nhân (agent / 에이전트) bộ nhớ (memory / 메모리)**, **Bộ nhớ (memory / 메모리) Poisoning** tiếp nhận điểm tựa từ **Người dùng (user / 사용자) bộ nhớ (memory / 메모리) vs tác vụ (task / 작업) bộ nhớ (memory / 메모리)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Example: coding tác nhân (agent / 에이전트)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Bộ nhớ (memory / 메모리) Poisoning

Nếu attacker khiến malicious content được lưu lâu dài, future tasks có thể bị ảnh hưởng. Đây là persistence phiên bản (version / 버전) của prompt injection.

Ghi (write / 쓰기) đường dẫn (path / 경로) cần kiểm tra hợp lệ (validation / 검증)/trust mức (level / 수준); retrieval đường dẫn (path / 경로) cần treat bộ nhớ (memory / 메모리) as dữ liệu (data / 데이터), không authority tuyệt đối.

> **Chuyển mạch:** Ở chặng này của **Tác nhân (agent / 에이전트) bộ nhớ (memory / 메모리)**, **Bộ nhớ (memory / 메모리) Poisoning** cho ta quy tắc; **Example: coding tác nhân (agent / 에이전트)** đặt quy tắc ấy vào tình huống cụ thể để thấy nó hoạt động đến đâu. Từ đây, **Bộ nhớ (memory / 메모리) chất lượng (quality / 품질) Metrics** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

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

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Tác nhân (agent / 에이전트) bộ nhớ (memory / 메모리)**, **Example: coding tác nhân (agent / 에이전트)** cho ta quy tắc; **Bộ nhớ (memory / 메모리) chất lượng (quality / 품질) Metrics** đặt quy tắc ấy vào tình huống cụ thể để thấy nó hoạt động đến đâu. Từ đây, **Mô hình tư duy (mental model / 사고 모델)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Bộ nhớ (memory / 메모리) chất lượng (quality / 품질) Metrics

Có thể đánh giá:

- retrieval precision/recall;
- stale-memory tỷ lệ (rate / 비율);
- contradiction tỷ lệ (rate / 비율);
- useful-memory tỷ lệ (rate / 비율);
- unauthorized retrieval incidents;
- ngữ cảnh (context / 맥락) tokens consumed.

“tác nhân (agent / 에이전트) nhớ nhiều” không phải chỉ số (metric / 지표) tốt.

> **Chuyển mạch:** Trong **Tác nhân (agent / 에이전트) bộ nhớ (memory / 메모리)**, **Mô hình tư duy (mental model / 사고 모델)** gom các mảnh từ **Bộ nhớ (memory / 메모리) chất lượng (quality / 품질) Metrics** thành một kết luận có thể mang sang phần kế tiếp. Từ đây, **Dùng chung (common / 공통) Misconceptions** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Mô hình tư duy (mental model / 사고 모델)

> **bộ nhớ (memory / 메모리) là managed bên ngoài (external / 외부) trạng thái (state / 상태), không phải một transcript vô hạn.**

Good bộ nhớ (memory / 메모리) kiến trúc (architecture / 아키텍처) quyết định cái gì cần lưu, ở đâu, bao lâu, ai được đọc và khi nào retrieve.

> **Chuyển mạch:** Ở chặng này của **Tác nhân (agent / 에이전트) bộ nhớ (memory / 메모리)**, **Dùng chung (common / 공통) Misconceptions** gom các mảnh từ **Mô hình tư duy (mental model / 사고 모델)** thành một kết luận có thể mang sang phần kế tiếp. Từ đây, **Liên kết kiến thức (knowledge connection / 지식 연결)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Dùng chung (common / 공통) Misconceptions

### “véc-tơ (vector / 벡터) DB = tác nhân (agent / 에이전트) bộ nhớ (memory / 메모리)”

Véc-tơ (vector / 벡터) DB chỉ là một lưu trữ (storage / 저장소)/retrieval technique cho một số bộ nhớ (memory / 메모리) types.

### “Long ngữ cảnh (context / 맥락) thay thế bộ nhớ (memory / 메모리)”

Long ngữ cảnh (context / 맥락) vẫn finite, costly và không giải quyết persistence/truy vấn (query / 쿼리)/versioning.

### “bộ nhớ (memory / 메모리) càng nhiều tác nhân (agent / 에이전트) càng thông minh”

Noise, stale facts và xung đột (conflict / 충돌) có thể làm hiệu năng (performance / 성능) tệ hơn.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Tác nhân (agent / 에이전트) bộ nhớ (memory / 메모리)**, sau nội dung của **Dùng chung (common / 공통) Misconceptions**, **Liên kết kiến thức (knowledge connection / 지식 연결)** chỉ rõ tài liệu chuẩn và vị trí sở hữu để người học biết phần nào cần quay lại khi muốn đào sâu. Phần còn lại của file dùng kết quả này để khép lại mạch giải thích.

## Liên kết kiến thức (knowledge connection / 지식 연결)

Bộ nhớ (memory / 메모리) nối databases, thông tin (information / 정보) retrieval, privacy, sự kiện (event / 이벤트) sourcing và ngữ cảnh (context / 맥락) kỹ thuật (engineering / 엔지니어링). Phần tiếp theo phân biệt bộ nhớ (memory / 메모리) với trạng thái (state / 상태) và ngữ cảnh (context / 맥락).

Xem tiếp: [Agent State and Context](./05_agent_state_and_context.md).

> **Bàn giao:** Sau **Liên kết kiến thức (knowledge connection / 지식 연결)**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](./README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
