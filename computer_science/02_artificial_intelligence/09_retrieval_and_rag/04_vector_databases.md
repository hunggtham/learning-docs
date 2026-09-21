# Cơ sở dữ liệu vector trong RAG

**Cơ sở dữ liệu vector (Vector Database / 벡터 데이터베이스)** là hệ thống dữ liệu được thiết kế để lưu, lập chỉ mục và truy vấn vector cùng metadata ở quy mô production. Nó không chỉ là một thuật toán ANN. Một vector database production thường phải đồng thời giải quyết lưu trữ bền vững, filtering, cập nhật, multi-tenancy, replication, access control và observability.

## Mô hình bản ghi

Một bản ghi đã được index thường có dạng:

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

Trong nhiều hệ thống, raw text có thể nằm ở object store hoặc database khác, còn vector database chỉ lưu pointer và metadata cần thiết.

## Nguồn dữ liệu gốc

Vector database không nên mặc định là nguồn có thẩm quyền (source of truth). Nguồn gốc thường là document store, CMS, relational database hoặc object storage.

Pipeline thường là:

```text
Nguồn dữ liệu gốc
→ ingestion
→ parse / chunk
→ embedding
→ vector index
```

Nếu vector record bị hỏng hoặc mất, hệ thống nên có khả năng rebuild từ source.

## CRUD và tái lập chỉ mục

Tạo hoặc cập nhật một document không chỉ là update một row. Một document có thể sinh nhiều chunk, và khi nội dung đổi thì ranh giới chunk cũng có thể thay đổi.

Một pattern an toàn là dùng chunk bất biến có version:

```text
version document mới
→ tạo chunk và index mới
→ chuyển trạng thái active sang version mới một cách nguyên tử
→ ngừng version cũ
```

Cách này giảm khoảng thời gian search có thể trộn chunk cũ và mới.

## Metadata filter

Metadata hỗ trợ các constraint mà vector similarity không thể biểu diễn đáng tin:

```text
product
version
region
language
created_at
security_scope
tenant
```

Semantics của filter nên được thiết kế như truy vấn database, không phải một gợi ý tùy chọn trong prompt.

## Multi-Tenancy

Nếu nhiều khách hàng dùng chung hạ tầng vector, cách ly tenant rất quan trọng.

Hai thiết kế phổ biến:

```text
index dùng chung + tenant filter nghiêm ngặt
namespace / index tách riêng theo tenant
```

Index dùng chung tiết kiệm tài nguyên nhưng bug filter có thể rò dữ liệu chéo tenant. Index riêng cách ly tốt hơn nhưng tăng chi phí vận hành.

## Authorization

Quyền truy cập của người dùng có thể phụ thuộc group hoặc ACL của document. Retrieval layer phải filter trước khi evidence được đưa vào LLM.

Không được retrieve secret chunk rồi chỉ yêu cầu LLM “đừng tiết lộ”. Khi secret đã vào context, ranh giới bảo mật đã bị phá vỡ.

## Tính nhất quán

Update vector database có thể bất đồng bộ. Sau khi write, query ngay có thể chưa nhìn thấy record tùy consistency model.

Ứng dụng cần biết rõ:

```text
có read-after-write mạnh không?
hay eventual consistency?
index refresh interval là bao lâu?
```

Điều này đặc biệt quan trọng với cập nhật tri thức và xóa dữ liệu.

## Semantics của xóa dữ liệu

Khi xóa source document, thao tác phải lan tới chunk, index và cache. Nếu chỉ xóa text còn vector vẫn searchable, mô hình vẫn có thể đưa nội dung đã xóa hoặc lỗi thời vào context.

Data lineage nên theo được:

```text
source_id → chunk_ids → embedding version → index records
```

## Versioning cho index

Khi nâng cấp embedding model, vector mới thường không tương thích với không gian cũ. Kiến trúc tốt tạo index version mới:

```text
index_v1 = embedding_model_A
index_v2 = embedding_model_B
```

Sau đó backfill, shadow evaluation, chuyển traffic rồi mới retire index cũ.

## Tìm kiếm lai

Nhiều vector database hỗ trợ sparse/BM25 cùng dense vector query. Nếu không, ứng dụng có thể query lexical engine và vector engine riêng rồi hợp nhất thứ hạng.

“Vector database” không có nghĩa hệ thống chỉ nên dùng vector.

## Bố cục lưu trữ

Raw float vector có kích thước lớn. Hệ thống có thể lưu representation nén trong index và giữ full vector ở storage khác để rerank hoặc phục vụ tác vụ cần độ chính xác cao hơn.

Đánh đổi phụ thuộc:

- kích thước corpus;
- tần suất query;
- ngân sách memory;
- tần suất cập nhật;
- yêu cầu recall.

## Replication và tính sẵn sàng cao

Search production cần replica và shard. Replica lag, leader failover và thời gian rebuild index ảnh hưởng availability.

Kiến trúc RAG nên có fallback khi vector service không hoạt động: lexical search, cached answer, lỗi rõ ràng hoặc no-answer; không nên bịa câu trả lời để che lỗi hạ tầng.

## Backup

Nếu index có thể rebuild từ source, chiến lược backup có thể tập trung vào source và pipeline configuration. Tuy nhiên rebuild index hàng tỷ vector có thể tốn thời gian lớn, nên snapshot index vẫn có giá trị vận hành.

## Observability

Không chỉ theo dõi CPU/RAM. Metric retrieval quan trọng gồm:

```text
query latency p50 / p95 / p99
zero-result rate
filter selectivity
index size
freshness lag
ANN recall trên mẫu
top-k score distribution
embedding/version mix
```

Sự thay đổi phân bố score có thể báo query distribution thay đổi hoặc model/index không tương thích.

## Mô hình chi phí

Chi phí vector database gồm memory, storage, compute, network và chi phí embedding khi ingestion.

Số chiều lớn, quá nhiều chunk và replication cao có thể làm chi phí tăng rất nhanh.

Do đó chunking strategy có ảnh hưởng trực tiếp tới kinh tế hạ tầng.

## Managed và Self-Hosted

Dịch vụ managed giảm công sức vận hành nhưng có thể tạo vấn đề data residency hoặc vendor lock-in. Self-hosted tăng quyền kiểm soát nhưng đội ngũ phải tự xử lý tuning index, scaling, backup và upgrade.

Quyết định nên dựa trên security, SLA và năng lực vận hành, không dựa trên xu hướng.

## Cơ sở dữ liệu SQL có vector extension

Relational database ngày càng hỗ trợ vector column và vector index. Với corpus vừa phải và metadata join quan trọng, giữ vector trong database hiện có có thể làm kiến trúc đơn giản hơn.

Dedicated vector database phù hợp khi scale, latency hoặc tính năng vector search là điểm nghẽn chính.

Không cần thêm một database mới chỉ vì tutorial RAG sử dụng nó.

## Cache

Embedding cache tránh tính lại vector cho query trùng. Cache kết quả retrieval hữu ích với query lặp và knowledge ổn định, nhưng invalidation khó khi source thay đổi.

Cache key nên chứa model version, index version và filter version cần thiết.

## Sự cố trộn embedding version

Nếu ingestion job nâng cấp embedding model nhưng query service vẫn dùng model cũ, vector có thể cùng dimension nhưng thuộc hai semantic space khác nhau. Search có thể âm thầm giảm chất lượng mà không báo lỗi shape.

Metadata và validation theo version phải ngăn việc trộn vector không tương thích.

## Mô hình tư duy

> Vector database là **hạ tầng dữ liệu định hướng tìm kiếm** dành cho biểu diễn học được. Semantic relevance đến từ embedding/retrieval model; correctness, security và freshness đến từ kiến trúc dữ liệu và hệ thống xung quanh.

## Những hiểu lầm thường gặp

### “Mọi RAG đều bắt buộc cần vector database”

Không. Corpus nhỏ có thể brute-force; SQL hoặc Elasticsearch cũng có thể đủ.

### “Lưu vector rồi không cần source document nữa”

Sai. Vector là biểu diễn mất mát và không phải nguồn provenance.

### “Tenant filter trong prompt là đủ”

Không. Authorization phải được cưỡng chế trước retrieval và context assembly.

## Liên kết kiến thức

Vector database kết nối ANN search, database systems, security và data engineering.

Xem tiếp: [RAG Fundamentals](./05_rag_fundamentals.md).