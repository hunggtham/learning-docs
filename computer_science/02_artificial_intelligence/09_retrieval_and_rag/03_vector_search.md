# Véc-tơ (vector / 벡터) tìm kiếm (search / 검색): từ Nearest Neighbor tới ANN chỉ mục (index / 인덱스)

> **Mạch đọc:** [README](./README.md) là bản đồ owner của **Véc-tơ (vector / 벡터) tìm kiếm (search / 검색): từ Nearest Neighbor tới ANN chỉ mục (index / 인덱스)**; nhìn vào vị trí đó trước để biết file này đang phục vụ nhánh kiến thức nào. **Chính xác (exact / 정확한) Nearest Neighbor** mở đối tượng chính của file và câu hỏi cần theo dõi; sau đó sang **Why Approximation Works** để mở câu hỏi trung tâm cho phần kế tiếp. Cách đi này giữ lại điểm tựa của section đầu và cho biết kết luận sẽ được dùng ở đâu, thay vì dừng ở định nghĩa đầu tiên.

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

> **Chuyển mạch:** Trong **Véc-tơ (vector / 벡터) tìm kiếm (search / 검색): từ Nearest Neighbor tới ANN chỉ mục (index / 인덱스)**, **Why Approximation Works** tiếp nhận điểm tựa từ **Chính xác (exact / 정확한) Nearest Neighbor** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **HNSW** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Why Approximation Works

RAG thường không cần chính xác (exact / 정확한) mathematically nearest véc-tơ (vector / 벡터); cần candidate set relevant. Nếu chỉ mục (index / 인덱스) trả almost-nearest vectors với recall cao nhưng nhanh hơn 100x, sự đánh đổi (trade-off / 트레이드오프) rất đáng giá.

Chất lượng (quality / 품질) chỉ số (metric / 지표) của ANN thường là **recall against chính xác (exact / 정확한) nearest neighbors**, khác retrieval relevance recall. Hai layers cần phân biệt:

```text
ANN recall: index có tìm được vector neighbors exact không?
Retrieval recall: những neighbors đó có chứa relevant evidence không?
```

> **Chuyển mạch:** Ở chặng này của **Véc-tơ (vector / 벡터) tìm kiếm (search / 검색): từ Nearest Neighbor tới ANN chỉ mục (index / 인덱스)**, **HNSW** tiếp nhận điểm tựa từ **Why Approximation Works** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **IVF** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

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

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Véc-tơ (vector / 벡터) tìm kiếm (search / 검색): từ Nearest Neighbor tới ANN chỉ mục (index / 인덱스)**, **IVF** tiếp nhận điểm tựa từ **HNSW** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Sản phẩm (product / 제품) Quantization** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

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

> **Chuyển mạch:** Trong **Véc-tơ (vector / 벡터) tìm kiếm (search / 검색): từ Nearest Neighbor tới ANN chỉ mục (index / 인덱스)**, **Sản phẩm (product / 제품) Quantization** tiếp nhận điểm tựa từ **IVF** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Scalar Quantization** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

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

> **Chuyển mạch:** Ở chặng này của **Véc-tơ (vector / 벡터) tìm kiếm (search / 검색): từ Nearest Neighbor tới ANN chỉ mục (index / 인덱스)**, **Scalar Quantization** tiếp nhận điểm tựa từ **Sản phẩm (product / 제품) Quantization** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Chỉ số (metric / 지표) Choice** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Scalar Quantization

Float32 véc-tơ (vector / 벡터) có thể quantize sang int8/float16. Simpler hơn PQ và giữ accuracy tốt trong many settings.

Nhưng quantization tác động (effect / 효과) cần benchmark trên actual embedding phân phối (distribution / 분포).

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Véc-tơ (vector / 벡터) tìm kiếm (search / 검색): từ Nearest Neighbor tới ANN chỉ mục (index / 인덱스)**, **Chỉ số (metric / 지표) Choice** tiếp nhận điểm tựa từ **Scalar Quantization** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Filtering bài toán (problem / 문제)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Chỉ số (metric / 지표) Choice

ANN chỉ mục (index / 인덱스) phải match similarity used by embedding mô hình (model / 모델):

```text
cosine similarity
inner product
L2 distance
```

Nếu vectors normalized, cosine và inner sản phẩm (product / 제품) ranking equivalent. Nếu không, magnitude affects inner sản phẩm (product / 제품).

Sai chỉ số (metric / 지표) có thể degrade retrieval nghiêm trọng.

> **Chuyển mạch:** Trong **Véc-tơ (vector / 벡터) tìm kiếm (search / 검색): từ Nearest Neighbor tới ANN chỉ mục (index / 인덱스)**, **Filtering bài toán (problem / 문제)** tiếp nhận điểm tựa từ **Chỉ số (metric / 지표) Choice** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Chỉ mục (index / 인덱스) bản dựng (build / 빌드) vs cập nhật (update / 업데이트)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

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

> **Chuyển mạch:** Ở chặng này của **Véc-tơ (vector / 벡터) tìm kiếm (search / 검색): từ Nearest Neighbor tới ANN chỉ mục (index / 인덱스)**, **Chỉ mục (index / 인덱스) bản dựng (build / 빌드) vs cập nhật (update / 업데이트)** tiếp nhận điểm tựa từ **Filtering bài toán (problem / 문제)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Freshness** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Chỉ mục (index / 인덱스) bản dựng (build / 빌드) vs cập nhật (update / 업데이트)

Một số indexes optimized batch bản dựng (build / 빌드), others động (dynamic / 동적) insert/delete tốt hơn. kiến thức (knowledge / 지식) cơ sở (base / 기반) có frequent updates cần consider cập nhật (update / 업데이트) ngữ nghĩa (semantics / 의미론).

Deletion đôi khi là tombstone + background rebuild, không immediate vật lý (physical / 물리적) removal.

Nếu legal deletion yêu cầu (requirement / 요구사항) nghiêm ngặt, cần hiểu lưu trữ (storage / 저장소)/chỉ mục (index / 인덱스) vòng đời (lifecycle / 생명주기).

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Véc-tơ (vector / 벡터) tìm kiếm (search / 검색): từ Nearest Neighbor tới ANN chỉ mục (index / 인덱스)**, **Freshness** tiếp nhận điểm tựa từ **Chỉ mục (index / 인덱스) bản dựng (build / 빌드) vs cập nhật (update / 업데이트)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Sharding** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

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

> **Chuyển mạch:** Trong **Véc-tơ (vector / 벡터) tìm kiếm (search / 검색): từ Nearest Neighbor tới ANN chỉ mục (index / 인덱스)**, **Sharding** tiếp nhận điểm tựa từ **Freshness** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Replication** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Sharding

Large corpus có thể shard by tenant, ngôn ngữ (language / 언어), region hoặc băm (hash / 해시). truy vấn (query / 쿼리) fan-out across shards rồi merge rankings.

Ngữ nghĩa (semantic / 의미적) sharding giảm tìm kiếm (search / 검색) không gian (space / 공간) nhưng rủi ro (risk / 위험) tuyến (route / 경로) sai truy vấn (query / 쿼리).

> **Chuyển mạch:** Ở chặng này của **Véc-tơ (vector / 벡터) tìm kiếm (search / 검색): từ Nearest Neighbor tới ANN chỉ mục (index / 인덱스)**, **Replication** tiếp nhận điểm tựa từ **Sharding** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Top-k và efSearch** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Replication

Read-heavy véc-tơ (vector / 벡터) tìm kiếm (search / 검색) cần replicas để quy mô (scale / 규모) thông lượng (throughput / 처리량)/high availability. chỉ mục (index / 인덱스) phiên bản (version / 버전) synchronization trở thành operational concern.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Véc-tơ (vector / 벡터) tìm kiếm (search / 검색): từ Nearest Neighbor tới ANN chỉ mục (index / 인덱스)**, **Top-k và efSearch** tiếp nhận điểm tựa từ **Replication** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Batch tìm kiếm (search / 검색)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Top-k và efSearch

Top-k là số results người dùng (user / 사용자) wants. `efSearch`/tìm kiếm (search / 검색) breadth là nội bộ (internal / 내부) candidate exploration. Muốn top-10 không có nghĩa nội bộ (internal / 내부) tìm kiếm (search / 검색) chỉ inspect 10 nodes.

Recall tuning cần separate these knobs.

> **Chuyển mạch:** Trong **Véc-tơ (vector / 벡터) tìm kiếm (search / 검색): từ Nearest Neighbor tới ANN chỉ mục (index / 인덱스)**, **Batch tìm kiếm (search / 검색)** tiếp nhận điểm tựa từ **Top-k và efSearch** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Chỉ mục (index / 인덱스) Recall Benchmark** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Batch tìm kiếm (search / 검색)

Embedding queries có thể batch, và véc-tơ (vector / 벡터) engines có SIMD/GPU acceleration. thông lượng (throughput / 처리량) tải công việc (workload / 워크로드) khác low-latency single-query tải công việc (workload / 워크로드).

Benchmark phải match traffic mẫu (pattern / 패턴).

> **Chuyển mạch:** Ở chặng này của **Véc-tơ (vector / 벡터) tìm kiếm (search / 검색): từ Nearest Neighbor tới ANN chỉ mục (index / 인덱스)**, **Chỉ mục (index / 인덱스) Recall Benchmark** tiếp nhận điểm tựa từ **Batch tìm kiếm (search / 검색)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **High-Dimensional hình học (geometry / 기하학)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Chỉ mục (index / 인덱스) Recall Benchmark

Procedure:

```text
sample queries
→ brute-force exact top-k
→ ANN top-k
→ compare overlap
```

Nếu ANN recall@10 = 0.98, 98% chính xác (exact / 정확한) neighbors recovered on average. Nhưng still need ngữ nghĩa (semantic / 의미적) relevance evaluation.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Véc-tơ (vector / 벡터) tìm kiếm (search / 검색): từ Nearest Neighbor tới ANN chỉ mục (index / 인덱스)**, **High-Dimensional hình học (geometry / 기하학)** tiếp nhận điểm tựa từ **Chỉ mục (index / 인덱스) Recall Benchmark** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Véc-tơ (vector / 벡터) tìm kiếm (search / 검색) vs véc-tơ (vector / 벡터) cơ sở dữ liệu (database / 데이터베이스)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## High-Dimensional hình học (geometry / 기하학)

In high dimensions, distance distributions can concentrate. Good learned embeddings try create useful cục bộ (local / 로컬) cấu trúc (structure / 구조), but ANN algorithms still face curse of dimensionality.

Better biểu diễn (representation / 표현) often improves tìm kiếm (search / 검색) more than endlessly tuning chỉ mục (index / 인덱스).

> **Chuyển mạch:** Trong **Véc-tơ (vector / 벡터) tìm kiếm (search / 검색): từ Nearest Neighbor tới ANN chỉ mục (index / 인덱스)**, **High-Dimensional hình học (geometry / 기하학)** nêu điều cần giải thích; **Véc-tơ (vector / 벡터) tìm kiếm (search / 검색) vs véc-tơ (vector / 벡터) cơ sở dữ liệu (database / 데이터베이스)** đối chiếu nó với bằng chứng hoặc nguồn kiểm chứng. Từ đây, **Mô hình tư duy (mental model / 사고 모델)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Véc-tơ (vector / 벡터) tìm kiếm (search / 검색) vs véc-tơ (vector / 벡터) cơ sở dữ liệu (database / 데이터베이스)

Véc-tơ (vector / 벡터) tìm kiếm (search / 검색) là thuật toán (algorithm / 알고리즘)/chỉ mục (index / 인덱스) bài toán (problem / 문제). **véc-tơ (vector / 벡터) cơ sở dữ liệu (database / 데이터베이스)** adds persistence, siêu dữ liệu (metadata / 메타데이터), CRUD, filtering, replication, transactions/consistency, APIs và operations.

Không nên coi HNSW = véc-tơ (vector / 벡터) cơ sở dữ liệu (database / 데이터베이스).

> **Chuyển mạch:** Ở chặng này của **Véc-tơ (vector / 벡터) tìm kiếm (search / 검색): từ Nearest Neighbor tới ANN chỉ mục (index / 인덱스)**, các dấu vết trong **Véc-tơ (vector / 벡터) tìm kiếm (search / 검색) vs véc-tơ (vector / 벡터) cơ sở dữ liệu (database / 데이터베이스)** được đọc cùng nhau ở **Mô hình tư duy (mental model / 사고 모델)** để rút ra mô hình, thay vì giữ chúng như những quan sát rời. Từ đây, **Dùng chung (common / 공통) Misconceptions** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Mô hình tư duy (mental model / 사고 모델)

> ANN chỉ mục (index / 인덱스) là **hiệu năng (performance / 성능) tầng (layer / 계층)** quanh embedding hình học (geometry / 기하학). Nó không tạo ngữ nghĩa (semantic / 의미적) chất lượng (quality / 품질); nó cố tìm gần đúng những neighbors mà embedding không gian (space / 공간) đã định nghĩa.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Véc-tơ (vector / 벡터) tìm kiếm (search / 검색): từ Nearest Neighbor tới ANN chỉ mục (index / 인덱스)**, **Dùng chung (common / 공통) Misconceptions** gom các mảnh từ **Mô hình tư duy (mental model / 사고 모델)** thành một kết luận có thể mang sang phần kế tiếp. Từ đây, **Liên kết kiến thức (knowledge connection / 지식 연결)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Dùng chung (common / 공통) Misconceptions

### “Approximate tìm kiếm (search / 검색) làm RAG hallucinate”

ANN approximation có thể miss bằng chứng (evidence / 증거), nhưng nguyên nhân gốc (root cause / 근본 원인) phải tách ANN recall khỏi retriever/mô hình (model / 모델) chất lượng (quality / 품질).

### “HNSW luôn tốt nhất”

Không. bộ nhớ (memory / 메모리), quy mô (scale / 규모), cập nhật (update / 업데이트) mẫu (pattern / 패턴) và hardware khác nhau làm IVF/PQ/brute-force đôi khi tốt hơn.

### “Filter sau tìm kiếm (search / 검색) luôn ổn”

Không nếu filter selective hoặc security-critical.

> **Chuyển mạch:** Trong **Véc-tơ (vector / 벡터) tìm kiếm (search / 검색): từ Nearest Neighbor tới ANN chỉ mục (index / 인덱스)**, sau nội dung của **Dùng chung (common / 공통) Misconceptions**, **Liên kết kiến thức (knowledge connection / 지식 연결)** chỉ rõ tài liệu chuẩn và vị trí sở hữu để người học biết phần nào cần quay lại khi muốn đào sâu. Phần còn lại của file dùng kết quả này để khép lại mạch giải thích.

## Liên kết kiến thức (knowledge connection / 지식 연결)

Véc-tơ (vector / 벡터) tìm kiếm (search / 검색) dựa [High-dimensional Linear Algebra](../01_mathematical_foundations/01_linear_algebra_for_ai.md) và [Embeddings](./02_embeddings_for_retrieval.md).

Xem tiếp: [Vector Databases](./04_vector_databases.md).

> **Bàn giao:** Sau **Liên kết kiến thức (knowledge connection / 지식 연결)**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](./README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
