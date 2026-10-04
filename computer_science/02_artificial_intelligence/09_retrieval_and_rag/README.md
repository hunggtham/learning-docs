# Retrieval & RAG kiến thức (knowledge / 지식) tầng (layer / 계층)

> **Mạch đọc:** [README](./README.md) là bản đồ owner của **Retrieval & RAG kiến thức (knowledge / 지식) tầng (layer / 계층)**; nhìn vào vị trí đó trước để biết file này đang phục vụ nhánh kiến thức nào. **Phụ thuộc (dependency / 의존성) Map** mở đối tượng chính của file và câu hỏi cần theo dõi; sau đó sang **Chapters** để mở rộng đối tượng sang phạm vi kế cận. Mạch này dùng README làm bản đồ owner của retrieval và RAG, rồi nối indexing, retrieval, grounding và generation thành pipeline có thể kiểm tra.

Folder này giải thích Retrieval-Augmented Generation từ nền thông tin (information / 정보) Retrieval tới kiến trúc vận hành (production architecture / 운영 아키텍처). RAG không được coi như recipe `embed → vector DB → LLM`; nó là một **bằng chứng (evidence / 증거) hệ thống (system / 시스템)** gồm ingestion, tìm kiếm (search / 검색), ranking, ngữ cảnh (context / 맥락) construction, provenance, evaluation và bảo mật (security / 보안).

## Phụ thuộc (dependency / 의존성) Map

Sơ đồ hoặc danh sách này mô tả thứ tự phụ thuộc của các khái niệm. Hãy đọc theo mũi tên để biết phần nào là prerequisite, phần nào là ứng dụng và khi nào cần quay lại nền tảng.

```mermaid
flowchart TD
    IR[IR Foundations] --> SD[Sparse & Dense Retrieval]
    SD --> EMB[Embeddings for Retrieval]
    EMB --> VS[Vector Search / ANN]
    VS --> VDB[Vector Databases]
    IR --> RAG[RAG Fundamentals]
    VDB --> RAG
    RAG --> CH[Chunking & Document Processing]
    CH --> RR[Retrieval / Ranking / Reranking]
    RR --> ADV[Advanced RAG]
    ADV --> EVAL[RAG Evaluation]
```

> **Chuyển mạch:** **Dependency Map** đi từ corpus, chunking và retrieval đến generation; **Full mental model** giữ rõ evidence path và nơi hallucination có thể phát sinh.

## Chapters

Sơ đồ hoặc danh sách này mô tả thứ tự phụ thuộc của các khái niệm. Hãy đọc theo mũi tên để biết phần nào là prerequisite, phần nào là ứng dụng và khi nào cần quay lại nền tảng.

```text
00_information_retrieval_foundations.md
01_sparse_and_dense_retrieval.md
02_embeddings_for_retrieval.md
03_vector_search.md
04_vector_databases.md
05_rag_fundamentals.md
06_chunking_and_document_processing.md
07_retrieval_ranking_and_reranking.md
08_advanced_rag.md
09_rag_evaluation.md
```

> **Chuyển mạch:** Ở chặng này của **Retrieval & RAG kiến thức (knowledge / 지식) tầng (layer / 계층)**, **Full mô hình tư duy (mental model / 사고 모델)** gom các mảnh từ **Chapters** thành một kết luận có thể mang sang phần kế tiếp. Từ đây, **Important Distinctions** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Full mô hình tư duy (mental model / 사고 모델)

Phần này chốt mental model thành một chuỗi có thể dùng lại: bối cảnh → cơ chế → quan sát → giới hạn → quyết định. Hãy đọc sơ đồ như công cụ suy luận, không như một khẩu hiệu tách khỏi chapter.

```text
Source of Truth
   ↓
Parse / Clean / Structure
   ↓
Chunk + Metadata + ACL + Version
   ↓
Embedding / Lexical Index
   ↓
Query Processing
   ↓
Sparse + Dense Candidate Retrieval
   ↓
Reranking / Filtering / Diversity
   ↓
Context Selection
   ↓
LLM Generation
   ↓
Citation / Verification / Abstention
   ↓
Evaluation + Monitoring
```

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Retrieval & RAG kiến thức (knowledge / 지식) tầng (layer / 계층)**, **Important Distinctions** gom các mảnh từ **Full mô hình tư duy (mental model / 사고 모델)** thành một kết luận có thể mang sang phần kế tiếp. Từ đây, **Môi trường vận hành (production / 운영 환경) Principle** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Important Distinctions

Phần này kiểm tra ranh giới và failure mode của cơ chế vừa học. Hãy dùng nó để biết khi nào mô hình còn đúng, khi nào cần đổi chiến lược và bằng chứng nào phải thu thập.

```text
retrieval relevance    ≠ factual truth
embedding similarity   ≠ authorization
vector search          ≠ vector database
RAG                     ≠ model weight update
retrieval candidate    ≠ final context
correct answer          ≠ grounded answer
newest source           ≠ authoritative source
long context            ≠ retrieval replacement
```

> **Chuyển mạch:** **Important Distinctions** tách retrieval quality khỏi generation quality; **Production Principle** đặt cả hai vào latency, freshness, access control và observability.

## Môi trường vận hành (production / 운영 환경) Principle

RAG should be debugged by tầng (layer / 계층). Nếu answer sai, không bắt đầu bằng thay prompt. Trước hết hỏi:

```text
source có đúng không?
parse/chunk có giữ information không?
retriever có lấy evidence không?
reranker có giữ evidence ở top không?
context builder có drop evidence không?
LLM có use evidence faithfully không?
citation có map đúng source không?
```

> **Chuyển mạch:** **Production Principle** khép RAG bằng evidence và operational limits; phần tiếp theo quay về owner của search, data platform hoặc model serving khi cần đào sâu.

## Next

RAG là một capability mà Agent có thể gọi như tool. Tiếp theo: [Agents and AI Systems](../10_agents_and_ai_systems/README.md).

> **Bàn giao:** Sau **Next**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](./README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
