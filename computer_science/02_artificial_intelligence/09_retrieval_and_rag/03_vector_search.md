# Véc-tơ (vector / 벡터) tìm kiếm (search / 검색): từ Nearest Neighbor tới ANN chỉ mục (index / 인덱스)

> **Mạch đọc:** Đặt **véc-tơ (vector / 벡터) tìm kiếm (search / 검색): từ Nearest Neighbor tới ANN chỉ mục (index / 인덱스)** trong bản đồ [README](./README.md) để thấy đơn vị sở hữu (owner / 오너) và vị trí của nó. Nội dung đi từ **chính xác (exact / 정확한) Nearest Neighbor** sang **Why Approximation Works**; điểm nối này chuẩn bị câu hỏi cho các mục sau thay vì dừng ở định nghĩa đầu tiên.


Khi corpus có hàng triệu embedding vectors, naive tìm kiếm (search / 검색) so sánh truy vấn (query / 쿼리) với mọi véc-tơ (vector / 벡터) có chi phí (cost / 비용):

\[
O(Nd)
\]

với `N` vectors và dimension `d`. chính xác (exact / 정확한) brute-force có thể ổn với corpus nhỏ hoặc GPU batch, nhưng quy mô (scale / 규모) lớn thường cần **Approximate Nearest Neighbor (ANN / 근사 최근접 이웃)**.

ANN hy sinh một phần exactness để giảm độ trễ (latency / 지연 시간)/bộ nhớ (memory / 메모리) chi phí (cost / 비용).

## Chính xác (exact / 정확한) Nearest Neighbor

Given truy vấn (query / 쿼리) `q`, tìm:

\[
\arg\max_d s(q,d)
\]

Nếu dùng cosine/dot sản phẩm (product / 제품), chính xác (exact / 정확한) tìm kiếm (search / 검색) compute score với toàn bộ corpus.

Chính xác (exact / 정확한) tìm kiếm (search / 검색) useful cho baseline vì cho upper bound recall của chỉ mục (index / 인덱스). Nếu ANN recall thấp hơn nhiều chính xác (exact / 정확한) tìm kiếm (search / 검색), chỉ mục (index / 인덱스) cấu hình (config / 설정) có vấn đề.

## Why Approximation Works

RAG thường không cần chính xác (exact / 정확한) mathematically nearest véc-tơ (vector / 벡터); cần candidate set relevant. Nếu chỉ mục (index / 인덱스) trả almost-nearest vectors với recall cao nhưng nhanh hơn 100x, sự đánh đổi (trade-off / 트레이드오프) rất đáng giá.

Chất lượng (quality / 품질) chỉ số (metric / 지표) của ANN thường là **recall against chính xác (exact / 정확한) nearest neighbors**, khác retrieval relevance recall. Hai layers cần phân biệt:

```text
ANN recall: index có tìm được vector neighbors exact không?
Retrieval recall: những neighbors đó có chứa relevant evidence không?
```

## HNSW

**Hierarchical Navigable Small World (HNSW)** xây đồ thị (graph / 그래프) nhiều tầng. tìm kiếm (search / 검색) bắt đầu ở sparse upper layers để move nhanh gần truy vấn (query / 쿼리) region, sau đó refine ở dense lower tầng (layer / 계층).

Mô hình tư duy (mental model / 사고 모델):

```text
highway layer → đi xa nhanh
local roads   → tìm neighbor gần
```

Important parameters thường gồm:

- `M`: số connections per nút (node / 노드);
- `efConstruction`: tìm kiếm (search / 검색) breadth khi bản dựng (build / 빌드);
- `efSearch`: tìm kiếm (search / 검색) breadth khi truy vấn (query / 쿼리).

Higher values thường improve recall nhưng tăng bộ nhớ (memory / 메모리)/bản dựng (build / 빌드)/truy vấn (query / 쿼리) chi phí (cost / 비용).

HNSW mạnh cho low-latency động (dynamic / 동적) tìm kiếm (search / 검색) nhưng chỉ mục (index / 인덱스) bộ nhớ (memory / 메모리) có thể lớn.

## IVF

**Inverted tệp (file / 파일) chỉ mục (index / 인덱스) (IVF)** cluster véc-tơ (vector / 벡터) không gian (space / 공간) thành coarse cells bằng centroids. truy vấn (query / 쿼리) chỉ tìm kiếm (search / 검색) một số nearest clusters.

```text
all vectors
→ cluster into cells
→ query selects nprobe cells
→ exact/quantized search within selected cells
```

`nprobe` lớn → recall cao hơn, độ trễ (latency / 지연 시간) lớn hơn.

IVF phù hợp large-scale tìm kiếm (search / 검색) và thường kết hợp sản phẩm (product / 제품) Quantization.

## Sản phẩm (product / 제품) Quantization

**PQ** compress véc-tơ (vector / 벡터) bằng chia dimensions thành subspaces và quantize mỗi subvector bằng codebook.

Thay lưu float véc-tơ (vector / 벡터) đầy đủ, chỉ mục (index / 인덱스) lưu compact codes. Distance được approximate từ lookup tables.

Sự đánh đổi (trade-off / 트레이드오프):

```text
memory ↓
cache efficiency ↑
accuracy ↓ somewhat
```

PQ rất quan trọng khi billions vectors hoặc bộ nhớ (memory / 메모리) chi phí (cost / 비용) dominate.

## Scalar Quantization

Float32 véc-tơ (vector / 벡터) có thể quantize sang int8/float16. Simpler hơn PQ và giữ accuracy tốt trong many settings.

Nhưng quantization tác động (effect / 효과) cần benchmark trên actual embedding phân phối (distribution / 분포).

## Chỉ số (metric / 지표) Choice

ANN chỉ mục (index / 인덱스) phải match similarity used by embedding mô hình (model / 모델):

```text
cosine similarity
inner product
L2 distance
```

Nếu vectors normalized, cosine và inner sản phẩm (product / 제품) ranking equivalent. Nếu không, magnitude affects inner sản phẩm (product / 제품).

Sai chỉ số (metric / 지표) có thể degrade retrieval nghiêm trọng.

## Filtering bài toán (problem / 문제)

Enterprise RAG cần filters:

```text
tenant_id = X
access_level <= current_user
version = current
language = ko
```

Filter có thể apply pre-filter hoặc post-filter.

**Post-filter**: ANN retrieve top-k rồi remove unauthorized/nonmatching items. Nếu nhiều items bị remove, kết quả (result / 결과) count/recall giảm.

**Pre-filter**: restrict candidate không gian (space / 공간) trước/within tìm kiếm (search / 검색). hiện thực (implementation / 구현) phức tạp hơn nhưng tính đúng đắn (correctness / 정확성) tốt hơn.

Bảo mật (security / 보안) filters không được best-effort.

## Chỉ mục (index / 인덱스) bản dựng (build / 빌드) vs cập nhật (update / 업데이트)

Một số indexes optimized batch bản dựng (build / 빌드), others động (dynamic / 동적) insert/delete tốt hơn. kiến thức (knowledge / 지식) cơ sở (base / 기반) có frequent updates cần consider cập nhật (update / 업데이트) ngữ nghĩa (semantics / 의미론).

Deletion đôi khi là tombstone + background rebuild, không immediate vật lý (physical / 물리적) removal.

Nếu legal deletion yêu cầu (requirement / 요구사항) nghiêm ngặt, cần hiểu lưu trữ (storage / 저장소)/chỉ mục (index / 인덱스) vòng đời (lifecycle / 생명주기).

## Freshness

Chỉ mục (index / 인덱스) có thể lag nguồn (source / 소스) cơ sở dữ liệu (database / 데이터베이스). chuỗi xử lý (pipeline / 파이프라인):

```text
source update
→ ingestion event
→ parse/chunk
→ embed
→ index update
```

Độ trễ (latency / 지연 시간) giữa nguồn (source / 소스) và tìm kiếm (search / 검색) là **freshness lag**. RAG “latest” chỉ tốt nếu ingestion SLA tốt.

## Sharding

Large corpus có thể shard by tenant, ngôn ngữ (language / 언어), region hoặc băm (hash / 해시). truy vấn (query / 쿼리) fan-out across shards rồi merge rankings.

Ngữ nghĩa (semantic / 의미적) sharding giảm tìm kiếm (search / 검색) không gian (space / 공간) nhưng rủi ro (risk / 위험) tuyến (route / 경로) sai truy vấn (query / 쿼리).

## Replication

Read-heavy véc-tơ (vector / 벡터) tìm kiếm (search / 검색) cần replicas để quy mô (scale / 규모) thông lượng (throughput / 처리량)/high availability. chỉ mục (index / 인덱스) phiên bản (version / 버전) synchronization trở thành operational concern.

## Top-k và efSearch

Top-k là số results người dùng (user / 사용자) wants. `efSearch`/tìm kiếm (search / 검색) breadth là nội bộ (internal / 내부) candidate exploration. Muốn top-10 không có nghĩa nội bộ (internal / 내부) tìm kiếm (search / 검색) chỉ inspect 10 nodes.

Recall tuning cần separate these knobs.

## Batch tìm kiếm (search / 검색)

Embedding queries có thể batch, và véc-tơ (vector / 벡터) engines có SIMD/GPU acceleration. thông lượng (throughput / 처리량) tải công việc (workload / 워크로드) khác low-latency single-query tải công việc (workload / 워크로드).

Benchmark phải match traffic mẫu (pattern / 패턴).

## Chỉ mục (index / 인덱스) Recall Benchmark

Procedure:

```text
sample queries
→ brute-force exact top-k
→ ANN top-k
→ compare overlap
```

Nếu ANN recall@10 = 0.98, 98% chính xác (exact / 정확한) neighbors recovered on average. Nhưng still need ngữ nghĩa (semantic / 의미적) relevance evaluation.

## High-Dimensional hình học (geometry / 기하학)

In high dimensions, distance distributions can concentrate. Good learned embeddings try create useful cục bộ (local / 로컬) cấu trúc (structure / 구조), but ANN algorithms still face curse of dimensionality.

Better biểu diễn (representation / 표현) often improves tìm kiếm (search / 검색) more than endlessly tuning chỉ mục (index / 인덱스).

## Véc-tơ (vector / 벡터) tìm kiếm (search / 검색) vs véc-tơ (vector / 벡터) cơ sở dữ liệu (database / 데이터베이스)

Véc-tơ (vector / 벡터) tìm kiếm (search / 검색) là thuật toán (algorithm / 알고리즘)/chỉ mục (index / 인덱스) bài toán (problem / 문제). **véc-tơ (vector / 벡터) cơ sở dữ liệu (database / 데이터베이스)** adds persistence, siêu dữ liệu (metadata / 메타데이터), CRUD, filtering, replication, transactions/consistency, APIs và operations.

Không nên coi HNSW = véc-tơ (vector / 벡터) cơ sở dữ liệu (database / 데이터베이스).

## Mô hình tư duy (mental model / 사고 모델)

> ANN chỉ mục (index / 인덱스) là **hiệu năng (performance / 성능) tầng (layer / 계층)** quanh embedding hình học (geometry / 기하학). Nó không tạo ngữ nghĩa (semantic / 의미적) chất lượng (quality / 품질); nó cố tìm gần đúng những neighbors mà embedding không gian (space / 공간) đã định nghĩa.

## Dùng chung (common / 공통) Misconceptions

### “Approximate tìm kiếm (search / 검색) làm RAG hallucinate”

ANN approximation có thể miss bằng chứng (evidence / 증거), nhưng nguyên nhân gốc (root cause / 근본 원인) phải tách ANN recall khỏi retriever/mô hình (model / 모델) chất lượng (quality / 품질).

### “HNSW luôn tốt nhất”

Không. bộ nhớ (memory / 메모리), quy mô (scale / 규모), cập nhật (update / 업데이트) mẫu (pattern / 패턴) và hardware khác nhau làm IVF/PQ/brute-force đôi khi tốt hơn.

### “Filter sau tìm kiếm (search / 검색) luôn ổn”

Không nếu filter selective hoặc security-critical.

## Liên kết kiến thức (knowledge connection / 지식 연결)

Véc-tơ (vector / 벡터) tìm kiếm (search / 검색) dựa [High-dimensional Linear Algebra](../01_mathematical_foundations/01_linear_algebra_for_ai.md) và [Embeddings](./02_embeddings_for_retrieval.md).

Xem tiếp: [Vector Databases](./04_vector_databases.md).

> **Bàn giao:** Sau **liên kết kiến thức (knowledge connection / 지식 연결)**, hãy chốt bất biến (invariant / 불변식) và giới hạn của mục này trước khi nối sang kiến thức kế tiếp. Có thể đọc tiếp [00 information retrieval foundations](./00_information_retrieval_foundations.md) để đối chiếu ranh giới (boundary / 경계) gần nhất.
