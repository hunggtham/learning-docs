# Véc-tơ (vector / 벡터) Databases trong RAG

> **Mạch đọc:** [README](./README.md) là bản đồ owner của **Vector databases trong RAG**. Route đi từ document/chunk records → embeddings and metadata → ANN index → filtering/updates → durability, isolation, and observability, để database layer nối được với retrieval contract.

**véc-tơ (vector / 벡터) cơ sở dữ liệu (database / 데이터베이스)** là dữ liệu (data / 데이터) hệ thống (system / 시스템) được thiết kế để lưu, chỉ mục (index / 인덱스) và truy vấn vectors cùng siêu dữ liệu (metadata / 메타데이터) ở quy mô (scale / 규모) môi trường vận hành (production / 운영 환경). Nó không chỉ là một ANN thuật toán (algorithm / 알고리즘). môi trường vận hành (production / 운영 환경) véc-tơ (vector / 벡터) DB thường phải giải đồng thời persistence, filtering, updates, multi-tenancy, replication, kiểm soát truy cập (access control / 접근 제어) và khả năng quan sát (observability / 관측 가능성).

## Bản ghi (record / 레코드) mô hình (model / 모델)

Một indexed bản ghi (record / 레코드) thường có dạng:

```json
{
  "id": "chunk_123",
  "vector": [0.01, -0.42, ...],
  "text": "...",
  "metadata": {
    "document_id": "policy_v5",
    "tenant_id": "A",
    "version": 5,
    "language": "ko"
  }
}
```

Trong nhiều các hệ thống (systems / 시스템들), raw văn bản (text / 텍스트) có thể ở đối tượng (object / 객체) store/cơ sở dữ liệu (database / 데이터베이스) khác và véc-tơ (vector / 벡터) DB chỉ lưu pointer + siêu dữ liệu (metadata / 메타데이터).

> **Chuyển mạch:** Trong **Véc-tơ (vector / 벡터) Databases trong RAG**, **Bản ghi (record / 레코드) mô hình (model / 모델)** nêu điều cần giải thích; **Nguồn chuẩn (source of truth / 정본)** đối chiếu nó với bằng chứng hoặc nguồn kiểm chứng. Từ đây, **CRUD và Reindexing** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Nguồn chuẩn (source of truth / 정본)

Véc-tơ (vector / 벡터) DB không nên mặc định là authoritative nguồn (source / 소스). Thường nguồn chuẩn (source of truth / 정본) là document store, CMS, relational DB hoặc đối tượng (object / 객체) lưu trữ (storage / 저장소).

Chuỗi xử lý (pipeline / 파이프라인):

```text
Source of Truth
→ ingestion
→ parse/chunk
→ embedding
→ vector index
```

Nếu véc-tơ (vector / 벡터) bản ghi (record / 레코드) corrupt/lost, hệ thống (system / 시스템) nên có khả năng rebuild từ nguồn (source / 소스).

> **Chuyển mạch:** Ở chặng này của **Véc-tơ (vector / 벡터) Databases trong RAG**, **Nguồn chuẩn (source of truth / 정본)** nêu điều cần giải thích; **CRUD và Reindexing** đối chiếu nó với bằng chứng hoặc nguồn kiểm chứng. Từ đây, **Siêu dữ liệu (metadata / 메타데이터) Filters** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## CRUD và Reindexing

Create/cập nhật (update / 업데이트) document không chỉ là cập nhật (update / 업데이트) một row. Một document có thể tạo nhiều chunks. cập nhật (update / 업데이트) content có thể làm chunk boundaries thay đổi.

Safe mẫu (pattern / 패턴) thường dùng immutable versioned chunks:

```text
new document version
→ generate new chunks/index
→ atomically mark new version active
→ retire old version
```

Điều này giảm cửa sổ (window / 윈도우) nơi tìm kiếm (search / 검색) mix old/new chunks.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Véc-tơ (vector / 벡터) Databases trong RAG**, **CRUD và Reindexing** nêu điều cần giải thích; **Siêu dữ liệu (metadata / 메타데이터) Filters** đối chiếu nó với bằng chứng hoặc nguồn kiểm chứng. Từ đây, **Multi-Tenancy** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Siêu dữ liệu (metadata / 메타데이터) Filters

Siêu dữ liệu (metadata / 메타데이터) hỗ trợ các ràng buộc (constraints / 제약조건들) mà véc-tơ (vector / 벡터) similarity không encode reliable:

```text
product
version
region
language
created_at
security_scope
tenant
```

Filter ngữ nghĩa (semantics / 의미론) nên được thiết kế (design / 설계) như truy vấn cơ sở dữ liệu (database query / 데이터베이스 쿼리), không phải optional prompt hint.

> **Chuyển mạch:** Trong **Véc-tơ (vector / 벡터) Databases trong RAG**, **Siêu dữ liệu (metadata / 메타데이터) Filters** nêu điều cần giải thích; **Multi-Tenancy** đối chiếu nó với bằng chứng hoặc nguồn kiểm chứng. Từ đây, **Authorization** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Multi-Tenancy

Nếu nhiều customers dùng same véc-tơ (vector / 벡터) infra, tenant isolation rất quan trọng.

Hai designs:

```text
shared index + strict tenant filter
separate namespace/index per tenant
```

Dùng chung (shared / 공유) chỉ mục (index / 인덱스) efficient nhưng filter bug có thể leak cross-tenant dữ liệu (data / 데이터). Separate indexes isolate tốt hơn nhưng operational overhead lớn.

> **Chuyển mạch:** Ở chặng này của **Véc-tơ (vector / 벡터) Databases trong RAG**, **Authorization** tiếp nhận điểm tựa từ **Multi-Tenancy** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Consistency** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Authorization

Người dùng (user / 사용자) truy cập (access / 접근) có thể phụ thuộc group/document ACL. Retrieval tầng (layer / 계층) phải filter trước khi bằng chứng (evidence / 증거) tới LLM.

Không được retrieve secret chunk rồi yêu cầu LLM “đừng tiết lộ”. Khi secret đã vào ngữ cảnh (context / 맥락), ranh giới bảo mật (security boundary / 보안 경계) đã bị vi phạm.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Véc-tơ (vector / 벡터) Databases trong RAG**, **Consistency** tiếp nhận điểm tựa từ **Authorization** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Deletion ngữ nghĩa (semantics / 의미론)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Consistency

Véc-tơ (vector / 벡터) DB cập nhật (update / 업데이트) có thể asynchronous. Sau ghi (write / 쓰기), truy vấn (query / 쿼리) ngay có thể chưa thấy bản ghi (record / 레코드) tùy consistency mô hình (model / 모델).

Ứng dụng (application / 애플리케이션) cần biết:

```text
strong/read-after-write?
eventual consistency?
index refresh interval?
```

Đặc biệt important cho kiến thức (knowledge / 지식) updates và deletion.

> **Chuyển mạch:** Trong **Véc-tơ (vector / 벡터) Databases trong RAG**, **Deletion ngữ nghĩa (semantics / 의미론)** tiếp nhận điểm tựa từ **Consistency** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Chỉ mục (index / 인덱스) Versioning** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Deletion ngữ nghĩa (semantics / 의미론)

Delete nguồn (source / 소스) document cần propagate tới chunks/chỉ mục (index / 인덱스)/bộ nhớ đệm (cache / 캐시). Nếu chỉ delete văn bản (text / 텍스트) nhưng véc-tơ (vector / 벡터) vẫn searchable, mô hình (model / 모델) có thể expose stale/deleted content.

Dữ liệu (data / 데이터) lineage cần nhánh học (track / 트랙):

```text
source_id → chunk_ids → embedding version → index records
```

> **Chuyển mạch:** Ở chặng này của **Véc-tơ (vector / 벡터) Databases trong RAG**, **Chỉ mục (index / 인덱스) Versioning** tiếp nhận điểm tựa từ **Deletion ngữ nghĩa (semantics / 의미론)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Hybrid tìm kiếm (search / 검색)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Chỉ mục (index / 인덱스) Versioning

Khi upgrade embedding mô hình (model / 모델), new vectors không compatible với old không gian (space / 공간). Good kiến trúc (architecture / 아키텍처) tạo new chỉ mục (index / 인덱스) phiên bản (version / 버전):

```text
index_v1 = embedding_model_A
index_v2 = embedding_model_B
```

Backfill, shadow evaluate, switch traffic, then retire old chỉ mục (index / 인덱스).

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Véc-tơ (vector / 벡터) Databases trong RAG**, **Hybrid tìm kiếm (search / 검색)** tiếp nhận điểm tựa từ **Chỉ mục (index / 인덱스) Versioning** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Lưu trữ (storage / 저장소) bố cục (layout / 레이아웃)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Hybrid tìm kiếm (search / 검색)

Nhiều véc-tơ (vector / 벡터) databases hỗ trợ (support / 지원) sparse/BM25 + dense véc-tơ (vector / 벡터) truy vấn (query / 쿼리). Nếu không, ứng dụng (application / 애플리케이션) có thể truy vấn (query / 쿼리) separate lexical engine và véc-tơ (vector / 벡터) engine rồi fuse rankings.

“véc-tơ (vector / 벡터) cơ sở dữ liệu (database / 데이터베이스)” không có nghĩa hệ thống (system / 시스템) chỉ nên dùng vectors.

> **Chuyển mạch:** Trong **Véc-tơ (vector / 벡터) Databases trong RAG**, **Lưu trữ (storage / 저장소) bố cục (layout / 레이아웃)** tiếp nhận điểm tựa từ **Hybrid tìm kiếm (search / 검색)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Replication và High Availability** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Lưu trữ (storage / 저장소) bố cục (layout / 레이아웃)

Raw float vectors large. các hệ thống (systems / 시스템들) có thể store compressed representations in chỉ mục (index / 인덱스) và full vectors separately for reranking/reconstruction.

Trade-offs depend on:

- corpus kích thước (size / 크기);
- truy vấn (query / 쿼리) tỷ lệ (rate / 비율);
- bộ nhớ (memory / 메모리) ngân sách (budget / 예산);
- cập nhật (update / 업데이트) frequency;
- recall yêu cầu (requirement / 요구사항).

> **Chuyển mạch:** Ở chặng này của **Véc-tơ (vector / 벡터) Databases trong RAG**, **Lưu trữ (storage / 저장소) bố cục (layout / 레이아웃)** cho ta quy tắc; **Replication và High Availability** đặt quy tắc ấy vào tình huống cụ thể để thấy nó hoạt động đến đâu. Từ đây, **Backups** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Replication và High Availability

Môi trường vận hành (production / 운영 환경) tìm kiếm (search / 검색) needs replicas/shards. Replica lag, leader failover và chỉ mục (index / 인덱스) rebuild thời gian (time / 시간) ảnh hưởng availability.

RAG kiến trúc (architecture / 아키텍처) nên có fallback khi véc-tơ (vector / 벡터) dịch vụ (service / 서비스) unavailable: lexical tìm kiếm (search / 검색), cached answer, graceful lỗi (error / 오류) hoặc no-answer — không fabricate.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Véc-tơ (vector / 벡터) Databases trong RAG**, **Replication và High Availability** cho ta quy tắc; **Backups** đặt quy tắc ấy vào tình huống cụ thể để thấy nó hoạt động đến đâu. Từ đây, **Khả năng quan sát (observability / 관측 가능성)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Backups

Nếu chỉ mục (index / 인덱스) rebuildable from nguồn (source / 소스), backup chiến lược (strategy / 전략) có thể focus nguồn (source / 소스) + chuỗi xử lý (pipeline / 파이프라인) cấu hình (config / 설정). Nhưng rebuild billion-vector chỉ mục (index / 인덱스) có thể mất nhiều thời gian, nên chỉ mục (index / 인덱스) snapshots vẫn valuable.

> **Chuyển mạch:** Trong **Véc-tơ (vector / 벡터) Databases trong RAG**, **Khả năng quan sát (observability / 관측 가능성)** tiếp nhận điểm tựa từ **Backups** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Chi phí (cost / 비용) mô hình (model / 모델)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Khả năng quan sát (observability / 관측 가능성)

Monitor không chỉ CPU/RAM. Retrieval-specific metrics:

```text
query latency p50/p95/p99
zero-result rate
filter selectivity
index size
freshness lag
ANN recall sample
top-k score distribution
embedding/version mix
```

Score phân phối (distribution / 분포) shift có thể tín hiệu (signal / 신호) truy vấn (query / 쿼리) phân phối (distribution / 분포) thay đổi (change / 변경) hoặc mô hình (model / 모델) mismatch.

> **Chuyển mạch:** Ở chặng này của **Véc-tơ (vector / 벡터) Databases trong RAG**, **Chi phí (cost / 비용) mô hình (model / 모델)** tiếp nhận điểm tựa từ **Khả năng quan sát (observability / 관측 가능성)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Managed vs Self-Hosted** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Chi phí (cost / 비용) mô hình (model / 모델)

Véc-tơ (vector / 벡터) DB chi phí (cost / 비용) gồm bộ nhớ (memory / 메모리), lưu trữ (storage / 저장소), compute, mạng (network / 네트워크) và embedding ingestion chi phí (cost / 비용).

Large `d`, many chunks và aggressive replicas tăng chi phí (cost / 비용) nhanh.

Chunking chiến lược (strategy / 전략) therefore has direct hạ tầng (infrastructure / 인프라) economics.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Véc-tơ (vector / 벡터) Databases trong RAG**, **Managed vs Self-Hosted** tiếp nhận điểm tựa từ **Chi phí (cost / 비용) mô hình (model / 모델)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **SQL Databases with véc-tơ (vector / 벡터) Extensions** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Managed vs Self-Hosted

Managed services reduce operations but may introduce dữ liệu (data / 데이터) residency/vendor lock-in. Self-hosted gives điều khiển (control / 제어) but requires chỉ mục (index / 인덱스) tuning, scaling, backups and upgrades.

Quyết định (decision / 결정) should come from bảo mật (security / 보안)/SLA/năng lực nhóm (team capability / 팀 역량), not trend.

> **Chuyển mạch:** Trong **Véc-tơ (vector / 벡터) Databases trong RAG**, **SQL Databases with véc-tơ (vector / 벡터) Extensions** tiếp nhận điểm tựa từ **Managed vs Self-Hosted** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Bộ nhớ đệm (cache / 캐시)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## SQL Databases with véc-tơ (vector / 벡터) Extensions

Relational databases increasingly hỗ trợ (support / 지원) véc-tơ (vector / 벡터) columns/indexes. Với corpus vừa và siêu dữ liệu (metadata / 메타데이터) joins quan trọng, keeping vectors in existing DB can simplify kiến trúc (architecture / 아키텍처).

Dedicated véc-tơ (vector / 벡터) DB hữu ích khi véc-tơ (vector / 벡터) tìm kiếm (search / 검색) quy mô (scale / 규모)/độ trễ (latency / 지연 시간)/features dominate.

Không cần thêm new cơ sở dữ liệu (database / 데이터베이스) chỉ vì RAG tutorial dùng một cái.

> **Chuyển mạch:** Ở chặng này của **Véc-tơ (vector / 벡터) Databases trong RAG**, **Bộ nhớ đệm (cache / 캐시)** tiếp nhận điểm tựa từ **SQL Databases with véc-tơ (vector / 벡터) Extensions** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Disaster Scenario: Mixed Embedding Versions** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Bộ nhớ đệm (cache / 캐시)

Embedding bộ nhớ đệm (cache / 캐시) tránh recompute duplicate truy vấn (query / 쿼리) vectors. Retrieval-result bộ nhớ đệm (cache / 캐시) useful cho repeated stable queries nhưng vô hiệu hóa (invalidation / 무효화) hard when kiến thức (knowledge / 지식) changes.

Bộ nhớ đệm (cache / 캐시) key cần include mô hình (model / 모델)/chỉ mục (index / 인덱스)/filter versions.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Véc-tơ (vector / 벡터) Databases trong RAG**, **Disaster Scenario: Mixed Embedding Versions** tiếp nhận điểm tựa từ **Bộ nhớ đệm (cache / 캐시)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Mô hình tư duy (mental model / 사고 모델)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Disaster Scenario: Mixed Embedding Versions

Nếu ingestion job upgrade embedding mô hình (model / 모델) nhưng truy vấn (query / 쿼리) dịch vụ (service / 서비스) vẫn mô hình (model / 모델) cũ, vectors share dimension maybe same nhưng ngữ nghĩa (semantic / 의미적) không gian (space / 공간) khác. tìm kiếm (search / 검색) silently fails.

Siêu dữ liệu (metadata / 메타데이터)/phiên bản (version / 버전) checks nên prevent mixing incompatible embeddings.

> **Chuyển mạch:** Trong **Véc-tơ (vector / 벡터) Databases trong RAG**, **Mô hình tư duy (mental model / 사고 모델)** gom các mảnh từ **Disaster Scenario: Mixed Embedding Versions** thành một kết luận có thể mang sang phần kế tiếp. Từ đây, **Dùng chung (common / 공통) Misconceptions** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Mô hình tư duy (mental model / 사고 모델)

> véc-tơ (vector / 벡터) DB là **search-oriented dữ liệu (data / 데이터) hạ tầng (infrastructure / 인프라)** cho learned representations. ngữ nghĩa (semantic / 의미적) relevance đến từ embedding/retrieval mô hình (model / 모델); tính đúng đắn (correctness / 정확성), bảo mật (security / 보안) và freshness đến từ dữ liệu (data / 데이터)/hệ thống (system / 시스템) kiến trúc (architecture / 아키텍처) xung quanh.

> **Chuyển mạch:** Ở chặng này của **Véc-tơ (vector / 벡터) Databases trong RAG**, **Dùng chung (common / 공통) Misconceptions** gom các mảnh từ **Mô hình tư duy (mental model / 사고 모델)** thành một kết luận có thể mang sang phần kế tiếp. Từ đây, **Liên kết kiến thức (knowledge connection / 지식 연결)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Dùng chung (common / 공통) Misconceptions

### “véc-tơ (vector / 벡터) DB là yêu cầu (requirement / 요구사항) của mọi RAG”

Không. Small corpus có thể brute-force; SQL/Elasticsearch may suffice.

### “Lưu véc-tơ (vector / 벡터) rồi không cần nguồn (source / 소스) document nữa”

Sai. véc-tơ (vector / 벡터) là lossy biểu diễn (representation / 표현) và không phải provenance nguồn (source / 소스).

### “Tenant filter trong prompt là đủ”

Không. Authorization phải enforced trước retrieval/ngữ cảnh (context / 맥락) assembly.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Véc-tơ (vector / 벡터) Databases trong RAG**, sau nội dung của **Dùng chung (common / 공통) Misconceptions**, **Liên kết kiến thức (knowledge connection / 지식 연결)** chỉ rõ tài liệu chuẩn và vị trí sở hữu để người học biết phần nào cần quay lại khi muốn đào sâu. Phần còn lại của file dùng kết quả này để khép lại mạch giải thích.

## Liên kết kiến thức (knowledge connection / 지식 연결)

Véc-tơ (vector / 벡터) cơ sở dữ liệu (database / 데이터베이스) kết nối ANN tìm kiếm (search / 검색), cơ sở dữ liệu (database / 데이터베이스) các hệ thống (systems / 시스템들), bảo mật (security / 보안) và kỹ thuật dữ liệu (data engineering / 데이터 엔지니어링).

Xem tiếp: [RAG Fundamentals](./05_rag_fundamentals.md).

> **Bàn giao:** Sau **Liên kết kiến thức (knowledge connection / 지식 연결)**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](./README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
