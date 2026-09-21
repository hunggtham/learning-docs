# Caching và Batching trong hệ thống AI

Caching và batching đều là kỹ thuật giúp giảm chi phí hoặc độ trễ, nhưng chúng giải quyết hai vấn đề khác nhau. **Bộ nhớ đệm (caching / 캐싱)** tái sử dụng kết quả tính toán đã có. **Gom lô (batching / 배칭)** gom nhiều phép tính mới để phần cứng xử lý hiệu quả hơn.

## Caching ở nhiều lớp

Một hệ thống AI có thể cache:

```text
raw API response
preprocessed input
embedding
retrieval result
reranker result
model output
KV cache
tool result
```

Không tồn tại một “AI cache” duy nhất. Mỗi lớp có cache key, TTL và consistency semantics riêng.

## Cache Key

Cache chỉ đúng khi key phản ánh đầy đủ mọi input có thể ảnh hưởng output.

Ví dụ một cache cho phản hồi LLM có thể cần:

```text
model version
system prompt
user prompt
context documents
sampling parameters
tool state
```

Nếu bỏ `model version`, sau khi rollout model mới hệ thống vẫn có thể trả kết quả cũ từ cache.

## Exact Cache và Semantic Cache

**Exact cache** chỉ reuse khi key khớp chính xác.

**Semantic cache** dùng embedding similarity để reuse câu trả lời cho query “gần nghĩa”. Cách này giảm cost nhưng có rủi ro cao hơn vì similarity không đồng nghĩa semantic equivalence.

Với tác vụ rủi ro cao, semantic cache cần threshold, domain constraint và validation rõ ràng.

## TTL và Invalidation

Cache invalidation khó vì kiến thức bên ngoài luôn thay đổi. RAG retrieval cache cần được invalidate khi corpus hoặc index update. Tool/API cache cũng cần freshness policy riêng.

TTL nên phụ thuộc độ biến động của dữ liệu, không nên dùng một con số chung cho toàn hệ thống.

## KV Cache

Trong autoregressive Transformer, token mới cần attention tới các token trước. **KV cache** lưu Key/Value của các layer/token đã xử lý để tránh tính lại toàn bộ prefix.

Chi phí memory xấp xỉ tăng theo:

```text
layers × sequence length × hidden/head dimensions × precision × concurrent sequences
```

Long context có thể làm KV cache trở thành bottleneck memory chính.

Paged hoặc block-based KV management giúp giảm fragmentation và hỗ trợ continuous batching hiệu quả hơn.

## Prefix Caching

Nếu nhiều request dùng chung một prefix lớn, ví dụ system prompt hoặc document context giống nhau, computation ở bước prefill có thể tái sử dụng.

Lợi ích lớn nhất khi shared prefix dài. Tuy nhiên cache key phải khớp model, tokenizer và positional semantics.

## Batching

Các dense accelerator kernel hoạt động hiệu quả hơn với matrix lớn. Batch size lớn giúp tăng hardware utilization nhưng đồng thời tăng queue wait và memory usage.

Offline training có thể dùng batch lớn. Online inference thường cần dynamic batching.

## Dynamic Batching

Server có thể chờ một khoảng rất ngắn để gom nhiều request thành một batch. Trade-off:

```text
chờ lâu hơn → batch lớn hơn → throughput tốt hơn
chờ ngắn hơn → latency tốt hơn → utilization thấp hơn
```

Không có một batch size tối ưu cho mọi hệ thống.

## Continuous Batching cho LLM

Batching truyền thống thường yêu cầu các sequence tiến cùng nhịp. LLM có output length khác nhau nên dễ lãng phí padding và idle slot.

**Continuous batching** cho phép sequence hoàn thành rời khỏi batch và request mới được đưa vào scheduler ngay khi có chỗ.

Scheduler cần quản lý:

- prefill và decode;
- KV memory;
- priority;
- fairness;
- max token;
- cancellation.

## Microbatching trong Training

Khi GPU memory không đủ cho một batch lớn, gradient accumulation chia logical batch thành nhiều microbatch:

```text
microbatch 1 → accumulate gradient
microbatch 2 → accumulate gradient
...
optimizer step
```

Effective batch size lớn hơn physical batch size.

## Request Coalescing

Nếu nhiều client cùng yêu cầu một phép tính đắt tiền giống hệt nhau trong cùng thời điểm, hệ thống có thể gộp thành một in-flight request thay vì chạy nhiều bản trùng lặp.

## Rủi ro chất lượng do Cache

Caching có thể giữ nguyên lỗi cũ. Một câu trả lời hallucination nếu bị cache có thể trở thành hallucination lặp lại nhiều lần. Vì vậy cache policy nên phân biệt output xác định và ổn định với output cần freshness hoặc verification.

## Observability

Nên theo dõi:

```text
cache hit rate
miss rate
eviction
stale hit
batch size distribution
queue wait
tokens/sec
memory utilization
```

Hit rate cao nhưng stale result nhiều không phải là thành công.

## Mô hình tư duy

```text
Caching  = tránh lặp lại công việc đã làm
Batching = làm công việc bắt buộc phải làm hiệu quả hơn
```

## Những nhầm lẫn thường gặp

### “Cache càng nhiều càng tốt”

Không. Cache làm tăng complexity, invalidation risk và memory footprint.

### “Batch size càng lớn thì càng nhanh”

Không. Throughput có thể tăng nhưng online latency và tail latency có thể xấu đi.

### “Semantic cache giống exact cache”

Không. Semantic cache thêm một bước learned similarity judgment nên có rủi ro chất lượng riêng.

## Liên kết kiến thức

Xem [Model Serving](./03_model_serving.md), [Latency, Throughput and Cost](./09_latency_throughput_and_cost.md), [RAG](../09_retrieval_and_rag/README.md) và [Transformer trong LLM](../08_large_language_models/03_transformer_inside_llms.md).