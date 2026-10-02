# Advanced RAG Patterns

> **Mạch đọc:** [README](./README.md) là bản đồ owner của **Advanced RAG patterns**. Route đi từ query rewriting/expansion → multi-query or decomposition → routing/iterative retrieval → context compression → failure recovery, để pattern nâng cao được gắn với lỗi retrieval cụ thể.

Basic RAG uses one truy vấn (query / 쿼리), one retrieval pass and one generation step. Real workloads often need more cấu trúc (structure / 구조): ambiguous questions, multi-hop bằng chứng (evidence / 증거), heterogeneous dữ liệu (data / 데이터), changing documents and high độ tin cậy (reliability / 신뢰성). **Advanced RAG** is not one thuật toán (algorithm / 알고리즘); it is a collection of architectural patterns for improving retrieval, bằng chứng (evidence / 증거) selection and generation điều khiển (control / 제어).

## Truy vấn (query / 쿼리) Rewriting

Conversational đầu vào (input / 입력) may be underspecified:

```text
"còn phí của gói kia thì sao?"
```

A rewrite mô hình (model / 모델) resolves lịch sử (history / 이력) into standalone truy vấn (query / 쿼리). Good hệ thống (system / 시스템) preserves original intent and logs both forms.

A rewrite should not silently add facts not present in conversation.

> **Chuyển mạch:** Trong **Advanced RAG Patterns**, **Truy vấn (query / 쿼리) Expansion** tiếp nhận điểm tựa từ **Truy vấn (query / 쿼리) Rewriting** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Multi-Query Retrieval** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Truy vấn (query / 쿼리) Expansion

Generate synonyms/aliases or multiple ngữ nghĩa (semantic / 의미적) formulations to increase recall.

Example:

```text
"hủy hợp đồng"
→ cancellation
→ contract termination
→ 해지
```

Merge results from expanded queries. rủi ro (risk / 위험) is topic drift, so expansion should be constrained by lĩnh vực (domain / 도메인) dictionaries or reranking.

> **Chuyển mạch:** Ở chặng này của **Advanced RAG Patterns**, **Multi-Query Retrieval** tiếp nhận điểm tựa từ **Truy vấn (query / 쿼리) Expansion** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **HyDE** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Multi-Query Retrieval

For complex question, generate several related queries and fuse results. This is useful when one embedding cannot represent all aspects equally.

```text
user question
→ query A
→ query B
→ query C
→ retrieve each
→ fusion/rerank
```

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Advanced RAG Patterns**, **HyDE** tiếp nhận điểm tựa từ **Multi-Query Retrieval** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Parent-Child Retrieval** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## HyDE

**Hypothetical Document Embeddings (HyDE)** creates a hypothetical answer/document from truy vấn (query / 쿼리), embeds that generated văn bản (text / 텍스트), then retrieves real documents close to it.

Intuition: long hypothetical văn bản (text / 텍스트) may land nearer relevant documents than short truy vấn (query / 쿼리).

Rủi ro (risk / 위험): hypothetical generation may inject wrong các giả định (assumptions / 가정들) and drift retrieval.

HyDE should be evaluated, not treated as default.

> **Chuyển mạch:** Trong **Advanced RAG Patterns**, **Parent-Child Retrieval** tiếp nhận điểm tựa từ **HyDE** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Multi-Vector Retrieval** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Parent-Child Retrieval

Chỉ mục (index / 인덱스) small child chunks for precise tìm kiếm (search / 검색), then return larger parent ngữ cảnh (context / 맥락) for generation.

```text
small chunk finds needle
→ parent section supplies surrounding conditions
```

This is especially effective for manuals/policies.

> **Chuyển mạch:** Ở chặng này của **Advanced RAG Patterns**, **Multi-Vector Retrieval** tiếp nhận điểm tựa từ **Parent-Child Retrieval** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Summary chỉ mục (index / 인덱스)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Multi-Vector Retrieval

One document may have multiple representations:

```text
raw chunk embedding
summary embedding
title embedding
questions-the-chunk-can-answer embeddings
```

Retrieve by any biểu diễn (representation / 표현) but return original nguồn (source / 소스) văn bản (text / 텍스트).

This separates **tìm kiếm (search / 검색) biểu diễn (representation / 표현)** from **bằng chứng (evidence / 증거) biểu diễn (representation / 표현)**.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Advanced RAG Patterns**, **Summary chỉ mục (index / 인덱스)** gom các mảnh từ **Multi-Vector Retrieval** thành một kết luận có thể mang sang phần kế tiếp. Từ đây, **Hierarchical Retrieval** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Summary chỉ mục (index / 인덱스)

For very long documents, bản dựng (build / 빌드) hierarchical summaries:

```text
document summary
section summaries
leaf chunks
```

Retriever first routes to relevant document/section, then searches locally.

This reduces tìm kiếm (search / 검색) không gian (space / 공간) and supports broad questions.

> **Chuyển mạch:** Trong **Advanced RAG Patterns**, **Hierarchical Retrieval** gom các mảnh từ **Summary chỉ mục (index / 인덱스)** thành một kết luận có thể mang sang phần kế tiếp. Từ đây, **Siêu dữ liệu (metadata / 메타데이터) Routing** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Hierarchical Retrieval

Corpus can be organized:

```text
organization
→ product
→ document
→ section
→ chunk
```

Truy vấn (query / 쿼리) first predicts higher-level tuyến (route / 경로) then retrieves lower-level units.

Routing errors become new dạng thất bại (failure mode / 실패 모드), so fallback toàn cục (global / 전역) tìm kiếm (search / 검색) is useful.

> **Chuyển mạch:** Ở chặng này của **Advanced RAG Patterns**, **Hierarchical Retrieval** nêu điều cần giải thích; **Siêu dữ liệu (metadata / 메타데이터) Routing** đối chiếu nó với bằng chứng hoặc nguồn kiểm chứng. Từ đây, **Multi-Hop Retrieval** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Siêu dữ liệu (metadata / 메타데이터) Routing

Before ngữ nghĩa (semantic / 의미적) tìm kiếm (search / 검색), detect structured các ràng buộc (constraints / 제약조건들):

```text
language=ko
product=eKYC
country=KR
version=current
```

Tuyến (route / 경로) to matching không gian tên (namespace / 네임스페이스)/chỉ mục (index / 인덱스). LLM may extract filters, but ứng dụng (application / 애플리케이션) validates allowed values.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Advanced RAG Patterns**, **Siêu dữ liệu (metadata / 메타데이터) Routing** nêu điều cần giải thích; **Multi-Hop Retrieval** đối chiếu nó với bằng chứng hoặc nguồn kiểm chứng. Từ đây, **Đồ thị (graph / 그래프) RAG** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Multi-Hop Retrieval

Some answers require chuỗi (chain / 사슬) of sources. Example:

```text
Which policy applies to product X?
→ retrieve product definition
→ discover policy ID
→ retrieve policy clauses
```

An iterative controller can use intermediate bằng chứng (evidence / 증거) to formulate next truy vấn (query / 쿼리).

This begins to overlap tác nhân (agent / 에이전트) kiến trúc (architecture / 아키텍처).

> **Chuyển mạch:** Trong **Advanced RAG Patterns**, **Đồ thị (graph / 그래프) RAG** tiếp nhận điểm tựa từ **Multi-Hop Retrieval** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **SQL + RAG** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Đồ thị (graph / 그래프) RAG

When relationships between entities matter, bản dựng (build / 빌드) đồ thị (graph / 그래프) or kiến thức (knowledge / 지식) đồ thị (graph / 그래프) and combine đồ thị (graph / 그래프) traversal with văn bản (text / 텍스트) retrieval.

Useful for:

```text
organization relationships
dependency chains
regulations and clauses
entity networks
```

Đồ thị (graph / 그래프) RAG is valuable when relational cấu trúc (structure / 구조) is tường minh (explicit / 명시적), not because đồ thị (graph / 그래프) is automatically superior to vectors.

> **Chuyển mạch:** Ở chặng này của **Advanced RAG Patterns**, **SQL + RAG** tiếp nhận điểm tựa từ **Đồ thị (graph / 그래프) RAG** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Tool-Augmented RAG** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## SQL + RAG

Structured dữ liệu (data / 데이터) should often be queried with SQL, while unstructured explanation comes from văn bản (text / 텍스트) retrieval.

Example:

```text
SQL → current transaction values
RAG → policy/explanation
LLM → synthesize
```

Do not embed tables and expect véc-tơ (vector / 벡터) tìm kiếm (search / 검색) to perform accurate aggregation.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Advanced RAG Patterns**, **Tool-Augmented RAG** tiếp nhận điểm tựa từ **SQL + RAG** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Corrective RAG** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Tool-Augmented RAG

Retriever itself can be one công cụ (tool / 도구) among many:

```text
web search
internal docs
SQL
API
code search
```

Router chooses dữ liệu (data / 데이터) nguồn (source / 소스) based on question.

This is more robust than one universal véc-tơ (vector / 벡터) chỉ mục (index / 인덱스).

> **Chuyển mạch:** Trong **Advanced RAG Patterns**, **Corrective RAG** tiếp nhận điểm tựa từ **Tool-Augmented RAG** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Self-RAG-like Patterns** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Corrective RAG

After retrieval, hệ thống (system / 시스템) evaluates whether bằng chứng (evidence / 증거) is sufficient/relevant. If not:

```text
rewrite query
broaden search
switch retriever
search web
ask clarification
abstain
```

Correction vòng lặp (loop / 루프) prevents forced answer on weak bằng chứng (evidence / 증거).

> **Chuyển mạch:** Ở chặng này của **Advanced RAG Patterns**, **Self-RAG-like Patterns** tiếp nhận điểm tựa từ **Corrective RAG** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Adaptive Retrieval** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Self-RAG-like Patterns

Mô hình (model / 모델) may decide when retrieval is needed and critique whether generated statements are supported.

But self-evaluation is probabilistic; bên ngoài (external / 외부) bằng chứng (evidence / 증거) checks still valuable.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Advanced RAG Patterns**, **Adaptive Retrieval** tiếp nhận điểm tựa từ **Self-RAG-like Patterns** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Truy vấn (query / 쿼리) Classification** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Adaptive Retrieval

Not every truy vấn (query / 쿼리) needs retrieval. Simple greetings or pure transformation tasks may skip tìm kiếm (search / 검색).

Router predicts:

```text
retrieve?
which source?
how many results?
```

This saves độ trễ (latency / 지연 시간)/chi phí (cost / 비용) but routing errors can miss necessary kiến thức (knowledge / 지식).

> **Chuyển mạch:** Trong **Advanced RAG Patterns**, **Truy vấn (query / 쿼리) Classification** tiếp nhận điểm tựa từ **Adaptive Retrieval** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Ngữ cảnh (context / 맥락) Compression** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Truy vấn (query / 쿼리) Classification

Classify truy vấn (query / 쿼리) into patterns:

```text
exact lookup
policy QA
comparison
multi-hop
calculation
current data
```

Each lớp (class / 클래스) gets specialized retrieval chiến lược (strategy / 전략).

> **Chuyển mạch:** Ở chặng này của **Advanced RAG Patterns**, **Ngữ cảnh (context / 맥락) Compression** tiếp nhận điểm tựa từ **Truy vấn (query / 쿼리) Classification** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Bằng chứng (evidence / 증거) đồ thị (graph / 그래프)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Ngữ cảnh (context / 맥락) Compression

Reranked chunks can be compressed into query-relevant excerpts. This lowers tokens but introduces extractor rủi ro (risk / 위험).

Keep nguồn (source / 소스) references so người dùng (user / 사용자) can inspect full ngữ cảnh (context / 맥락).

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Advanced RAG Patterns**, **Ngữ cảnh (context / 맥락) Compression** nêu điều cần giải thích; **Bằng chứng (evidence / 증거) đồ thị (graph / 그래프)** đối chiếu nó với bằng chứng hoặc nguồn kiểm chứng. Từ đây, **Giải quyết xung đột (conflict resolution / 충돌 해결)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Bằng chứng (evidence / 증거) đồ thị (graph / 그래프)

For multi-source answer, create tường minh (explicit / 명시적) ánh xạ (mapping / 매핑):

```text
claim A ← source 1
claim B ← source 2 + source 3
```

This improves citation chất lượng (quality / 품질) and makes xác minh (verification / 확인) easier.

> **Chuyển mạch:** Trong **Advanced RAG Patterns**, **Bằng chứng (evidence / 증거) đồ thị (graph / 그래프)** nêu điều cần giải thích; **Giải quyết xung đột (conflict resolution / 충돌 해결)** đối chiếu nó với bằng chứng hoặc nguồn kiểm chứng. Từ đây, **Temporal RAG** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Giải quyết xung đột (conflict resolution / 충돌 해결)

If two sources disagree, mô hình (model / 모델) should not silently average. Use siêu dữ liệu (metadata / 메타데이터):

```text
version
date
authority
status
jurisdiction
```

Hệ thống (system / 시스템) may present xung đột (conflict / 충돌) rather than fabricate single answer.

> **Chuyển mạch:** Ở chặng này của **Advanced RAG Patterns**, **Temporal RAG** tiếp nhận điểm tựa từ **Giải quyết xung đột (conflict resolution / 충돌 해결)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Personalized RAG** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Temporal RAG

Time-sensitive corpora need effective-date filtering. truy vấn (query / 쿼리) should retrieve nguồn (source / 소스) valid at requested thời gian (time / 시간), not simply newest.

Example:

```text
"policy as of 2025-12-01"
```

requires temporal validity intervals.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Advanced RAG Patterns**, **Personalized RAG** tiếp nhận điểm tựa từ **Temporal RAG** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Caching** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Personalized RAG

Retrieval can consider người dùng (user / 사용자) profile/permissions/preferences. But personalization must not leak sensitive cross-user dữ liệu (data / 데이터).

Separate personalization tín hiệu (signal / 신호) from authorization lô-gic (logic / 논리).

> **Chuyển mạch:** Trong **Advanced RAG Patterns**, **Caching** tiếp nhận điểm tựa từ **Personalized RAG** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Khả năng quan sát (observability / 관측 가능성)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Caching

Bộ nhớ đệm (cache / 캐시) truy vấn (query / 쿼리) embedding, retrieval results or final answers. bộ nhớ đệm (cache / 캐시) key must include:

```text
query
user/tenant scope
index version
source version
model/prompt version
```

Otherwise stale or cross-user leakage can occur.

> **Chuyển mạch:** Ở chặng này của **Advanced RAG Patterns**, **Khả năng quan sát (observability / 관측 가능성)** tiếp nhận điểm tựa từ **Caching** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Mô hình tư duy (mental model / 사고 모델)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Khả năng quan sát (observability / 관측 가능성)

Advanced RAG needs traces:

```text
original query
rewritten queries
filters
retrieved IDs/scores
reranker scores
selected context
citations
final output
```

Without dấu vết (trace / 추적), debugging “LLM trả lời sai” becomes guesswork.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Advanced RAG Patterns**, **Mô hình tư duy (mental model / 사고 모델)** gom các mảnh từ **Khả năng quan sát (observability / 관측 가능성)** thành một kết luận có thể mang sang phần kế tiếp. Từ đây, **Dùng chung (common / 공통) Misconceptions** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Mô hình tư duy (mental model / 사고 모델)

> Advanced RAG is **retrieval orchestration under bất định (uncertainty / 불확실성)**. độ phức tạp (complexity / 복잡도) should be added only when a measured dạng thất bại (failure mode / 실패 모드) justifies it.

> **Chuyển mạch:** Trong **Advanced RAG Patterns**, **Dùng chung (common / 공통) Misconceptions** gom các mảnh từ **Mô hình tư duy (mental model / 사고 모델)** thành một kết luận có thể mang sang phần kế tiếp. Từ đây, **Liên kết kiến thức (knowledge connection / 지식 연결)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Dùng chung (common / 공통) Misconceptions

### “Advanced RAG means add an tác nhân (agent / 에이전트) khung phần mềm (framework / 프레임워크)”

Không. Many improvements are deterministic retrieval/ranking kiến trúc (architecture / 아키텍처).

### “đồ thị (graph / 그래프) RAG always beats véc-tơ (vector / 벡터) RAG”

Không. It depends on relational cấu trúc (structure / 구조) and truy vấn (query / 쿼리) kiểu (type / 타입).

### “More retrieval loops always improve answer”

No. More calls increase độ trễ (latency / 지연 시간), drift and chi phí (cost / 비용).

> **Chuyển mạch:** Ở chặng này của **Advanced RAG Patterns**, sau nội dung của **Dùng chung (common / 공통) Misconceptions**, **Liên kết kiến thức (knowledge connection / 지식 연결)** chỉ rõ tài liệu chuẩn và vị trí sở hữu để người học biết phần nào cần quay lại khi muốn đào sâu. Phần còn lại của file dùng kết quả này để khép lại mạch giải thích.

## Liên kết kiến thức (knowledge connection / 지식 연결)

Advanced RAG is the cầu nối (bridge / 브리지) from retrieval chuỗi xử lý (pipeline / 파이프라인) to [Agents](../10_agents_and_ai_systems/00_from_llm_to_agent.md).

Xem tiếp: [RAG Evaluation](./09_rag_evaluation.md).

> **Bàn giao:** Sau **Liên kết kiến thức (knowledge connection / 지식 연결)**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](./README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
