# Tìm kiếm vector: từ láng giềng gần nhất tới chỉ mục ANN

Khi corpus có hàng triệu vector embedding, cách tìm kiếm ngây thơ phải so query với mọi vector và có chi phí:

\[
O(Nd)
\]

với `N` vector và số chiều `d`. Tìm kiếm chính xác bằng brute force có thể phù hợp với corpus nhỏ hoặc batch trên GPU, nhưng ở quy mô lớn thường cần **tìm kiếm láng giềng gần đúng (Approximate Nearest Neighbor — ANN / 근사 최근접 이웃)**.

ANN chấp nhận mất một phần độ chính xác hình học để giảm độ trễ và chi phí bộ nhớ.

## Láng giềng gần nhất chính xác

Với query `q`, ta tìm:

\[
\arg\max_d s(q,d)
\]

Nếu dùng cosine hoặc dot product, exact search phải tính score với toàn bộ corpus.

Exact search rất hữu ích làm baseline vì cho biết kết quả láng giềng chính xác của embedding space. Nếu ANN recall thấp hơn nhiều so với exact search, cấu hình index có vấn đề.

## Vì sao xấp xỉ vẫn hiệu quả?

RAG thường không cần vector gần nhất chính xác tuyệt đối về toán học; điều cần là candidate set chứa bằng chứng liên quan. Nếu index trả về vector gần nhất xấp xỉ với recall cao nhưng nhanh hơn rất nhiều, đánh đổi đó có giá trị lớn.

Cần phân biệt hai loại recall:

```text
ANN recall
= index có tìm lại được các exact nearest neighbor không?

Retrieval recall
= những neighbor được tìm có thật sự chứa evidence relevant không?
```

Đây là hai tầng lỗi khác nhau.

## HNSW

**Hierarchical Navigable Small World (HNSW)** xây graph nhiều tầng. Search bắt đầu ở tầng trên thưa hơn để di chuyển nhanh tới vùng gần query, rồi tinh chỉnh ở tầng dưới dày hơn.

Mô hình tư duy:

```text
tầng cao như đường cao tốc → đi xa nhanh
tầng thấp như đường địa phương → tìm neighbor gần
```

Các tham số thường quan trọng:

- `M`: số kết nối của mỗi node;
- `efConstruction`: độ rộng search khi xây index;
- `efSearch`: độ rộng search khi query.

Giá trị lớn hơn thường tăng recall nhưng cũng tăng bộ nhớ, thời gian build hoặc latency query.

HNSW rất mạnh cho search độ trễ thấp và cập nhật động, nhưng footprint bộ nhớ của graph có thể lớn.

## IVF

**Inverted File Index (IVF)** chia không gian vector thành các cell thô bằng centroid. Query chỉ tìm trong một số cluster gần nhất.

```text
toàn bộ vector
→ cluster thành cell
→ query chọn nprobe cell
→ search chính xác hoặc lượng tử hóa trong các cell đã chọn
```

`nprobe` lớn hơn thường tăng recall nhưng tăng latency.

IVF phù hợp search quy mô lớn và thường được kết hợp với Product Quantization.

## Product Quantization

**Product Quantization (PQ)** nén vector bằng cách chia các chiều thành subspace rồi lượng tử hóa từng subvector bằng codebook.

Thay vì lưu float vector đầy đủ, index lưu mã compact và xấp xỉ distance bằng bảng tra cứu.

Đánh đổi:

```text
bộ nhớ ↓
hiệu quả cache ↑
độ chính xác giảm một phần
```

PQ đặc biệt quan trọng khi số vector lên tới hàng tỷ hoặc chi phí memory là điểm nghẽn.

## Scalar Quantization

Vector float32 có thể được lượng tử sang int8 hoặc float16. Cách này đơn giản hơn PQ và thường giữ chất lượng tốt trong nhiều trường hợp.

Tác động của quantization vẫn phải benchmark trên đúng phân bố embedding thực tế.

## Chọn metric

ANN index phải dùng metric phù hợp với embedding model:

```text
cosine similarity
inner product
L2 distance
```

Nếu vector được normalize, cosine và inner product cho cùng thứ hạng. Nếu không, độ lớn vector ảnh hưởng inner product.

Chọn sai metric có thể làm retrieval giảm nghiêm trọng.

## Bài toán filtering

Enterprise RAG thường cần filter:

```text
tenant_id = X
access_level <= current_user
version = current
language = ko
```

Filter có thể áp dụng trước hoặc sau ANN.

**Post-filter**: retrieve top-k rồi loại item không hợp lệ. Nếu filter rất chọn lọc, số kết quả và recall có thể giảm mạnh.

**Pre-filter**: thu hẹp candidate space trước hoặc trong search. Implementation phức tạp hơn nhưng phù hợp hơn với constraint nghiêm ngặt.

Filter liên quan bảo mật không được thiết kế theo kiểu “best effort”.

## Xây index và cập nhật

Một số index tối ưu cho batch build, số khác hỗ trợ insert/delete động tốt hơn. Knowledge base cập nhật thường xuyên phải cân nhắc semantics cập nhật.

Xóa đôi khi chỉ đánh dấu **tombstone** rồi rebuild nền thay vì loại vật lý ngay. Nếu có yêu cầu pháp lý về xóa dữ liệu, cần hiểu rõ lifecycle lưu trữ và index.

## Độ mới của index

Index có thể chậm hơn source database. Pipeline thường là:

```text
source thay đổi
→ ingestion event
→ parse / chunk
→ embed
→ cập nhật index
```

Khoảng trễ này là **freshness lag**. RAG chỉ “mới nhất” nếu ingestion có SLA phù hợp.

## Sharding

Corpus lớn có thể được shard theo tenant, language, region hoặc hash. Query có thể fan-out qua nhiều shard rồi hợp nhất thứ hạng.

Semantic sharding giảm search space nhưng có nguy cơ route query vào sai shard.

## Replication

Vector search thiên về đọc có thể dùng replica để tăng throughput và high availability. Đồng bộ phiên bản index giữa replica trở thành vấn đề vận hành.

## Top-k và efSearch

Top-k là số kết quả cần trả. `efSearch` hoặc search breadth là số candidate nội bộ mà thuật toán khám phá.

Muốn top-10 không có nghĩa index chỉ cần xem 10 node. Hai tham số cần được tune độc lập.

## Batch Search

Query embedding có thể được batch và engine vector có thể tận dụng SIMD hoặc GPU. Workload throughput cao khác với workload một query cần latency thấp.

Benchmark phải giống traffic production.

## Benchmark recall của index

Một quy trình đơn giản:

```text
lấy mẫu query
→ brute-force exact top-k
→ ANN top-k
→ so độ trùng
```

Nếu ANN recall@10 = 0.98, trung bình 98% exact neighbor được khôi phục. Nhưng vẫn phải đánh giá relevance ngữ nghĩa riêng.

## Hình học chiều cao

Trong không gian nhiều chiều, phân bố khoảng cách có thể dồn lại. Embedding tốt cố tạo local structure hữu ích, nhưng ANN vẫn chịu một phần **curse of dimensionality**.

Cải thiện representation thường có thể tạo lợi ích lớn hơn việc chỉ tiếp tục tune index.

## Vector Search và Vector Database

Vector search là bài toán thuật toán/index. **Vector database** bổ sung persistence, metadata, CRUD, filtering, replication, consistency, API và vận hành.

HNSW tự nó không phải một vector database.

## Mô hình tư duy

> ANN index là **lớp hiệu năng** bao quanh embedding geometry. Nó không tạo ra chất lượng ngữ nghĩa; nó cố tìm nhanh các neighbor mà không gian embedding đã định nghĩa.

## Những hiểu lầm thường gặp

### “Approximate search làm RAG hallucinate”

ANN có thể làm bỏ sót evidence, nhưng phải tách lỗi index recall khỏi lỗi retriever, dữ liệu và generator.

### “HNSW luôn tốt nhất”

Không. Memory, scale, pattern cập nhật và hardware có thể khiến IVF, PQ hoặc brute force phù hợp hơn.

### “Filter sau search luôn ổn”

Không khi filter rất chọn lọc hoặc mang ý nghĩa bảo mật.

## Liên kết kiến thức

Vector search dựa trên [Linear Algebra](../01_mathematical_foundations/01_linear_algebra_for_ai.md) và [Embeddings](./02_embeddings_for_retrieval.md).

Xem tiếp: [Vector Databases](./04_vector_databases.md).