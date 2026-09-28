# Caching và Batching trong hệ thống AI

> **Mạch đọc:** Đặt **Caching và Batching trong hệ thống AI** trong bản đồ [README](./README.md) để thấy đơn vị sở hữu (owner / 오너) và vị trí của nó. Nội dung đi từ **Caching ở nhiều lớp** sang **bộ nhớ đệm (cache / 캐시) Key**; điểm nối này chuẩn bị câu hỏi cho các mục sau thay vì dừng ở định nghĩa đầu tiên.


Caching và batching đều là kỹ thuật giúp giảm chi phí hoặc độ trễ, nhưng chúng giải quyết hai vấn đề khác nhau. **Bộ nhớ đệm (caching / 캐싱)** tái sử dụng kết quả tính toán đã có. **Gom lô (batching / 배칭)** gom nhiều phép tính mới để phần cứng xử lý hiệu quả hơn.

## Caching ở nhiều lớp

Một hệ thống AI có thể bộ nhớ đệm (cache / 캐시):

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

Không tồn tại một “AI bộ nhớ đệm (cache / 캐시)” duy nhất. Mỗi lớp có bộ nhớ đệm (cache / 캐시) key, TTL và consistency ngữ nghĩa (semantics / 의미론) riêng.

## Bộ nhớ đệm (cache / 캐시) Key

Bộ nhớ đệm (cache / 캐시) chỉ đúng khi key phản ánh đầy đủ mọi đầu vào (input / 입력) có thể ảnh hưởng đầu ra (output / 출력).

Ví dụ một bộ nhớ đệm (cache / 캐시) cho phản hồi LLM có thể cần:

```text
model version
system prompt
user prompt
context documents
sampling parameters
tool state
```

Nếu bỏ `model version`, sau khi rollout mô hình (model / 모델) mới hệ thống vẫn có thể trả kết quả cũ từ bộ nhớ đệm (cache / 캐시).

## Chính xác (exact / 정확한) bộ nhớ đệm (cache / 캐시) và ngữ nghĩa (semantic / 의미적) bộ nhớ đệm (cache / 캐시)

**chính xác (exact / 정확한) bộ nhớ đệm (cache / 캐시)** chỉ reuse khi key khớp chính xác.

**ngữ nghĩa (semantic / 의미적) bộ nhớ đệm (cache / 캐시)** dùng embedding similarity để reuse câu trả lời cho truy vấn (query / 쿼리) “gần nghĩa”. Cách này giảm chi phí (cost / 비용) nhưng có rủi ro cao hơn vì similarity không đồng nghĩa ngữ nghĩa (semantic / 의미적) equivalence.

Với tác vụ rủi ro cao, ngữ nghĩa (semantic / 의미적) bộ nhớ đệm (cache / 캐시) cần threshold, lĩnh vực (domain / 도메인) ràng buộc (constraint / 제약조건) và kiểm tra hợp lệ (validation / 검증) rõ ràng.

## TTL và vô hiệu hóa (invalidation / 무효화)

Bộ nhớ đệm (cache / 캐시) vô hiệu hóa (invalidation / 무효화) khó vì kiến thức bên ngoài luôn thay đổi. RAG retrieval bộ nhớ đệm (cache / 캐시) cần được invalidate khi corpus hoặc chỉ mục (index / 인덱스) cập nhật (update / 업데이트). công cụ (tool / 도구)/API bộ nhớ đệm (cache / 캐시) cũng cần freshness chính sách (policy / 정책) riêng.

TTL nên phụ thuộc độ biến động của dữ liệu, không nên dùng một con số chung cho toàn hệ thống.

## KV bộ nhớ đệm (cache / 캐시)

Trong autoregressive Transformer, đơn vị từ (token / 토큰) mới cần attention tới các đơn vị từ (token / 토큰) trước. **KV bộ nhớ đệm (cache / 캐시)** lưu Key/giá trị (value / 값) của các tầng (layer / 계층)/đơn vị từ (token / 토큰) đã xử lý để tránh tính lại toàn bộ prefix.

Chi phí bộ nhớ (memory / 메모리) xấp xỉ tăng theo:

```text
layers × sequence length × hidden/head dimensions × precision × concurrent sequences
```

Long ngữ cảnh (context / 맥락) có thể làm KV bộ nhớ đệm (cache / 캐시) trở thành bottleneck bộ nhớ (memory / 메모리) chính.

Paged hoặc block-based KV management giúp giảm fragmentation và hỗ trợ continuous batching hiệu quả hơn.

## Prefix Caching

Nếu nhiều yêu cầu (request / 요청) dùng chung một prefix lớn, ví dụ hệ thống (system / 시스템) prompt hoặc document ngữ cảnh (context / 맥락) giống nhau, computation ở bước prefill có thể tái sử dụng.

Lợi ích lớn nhất khi dùng chung (shared / 공유) prefix dài. Tuy nhiên bộ nhớ đệm (cache / 캐시) key phải khớp mô hình (model / 모델), tokenizer và positional ngữ nghĩa (semantics / 의미론).

## Batching

Các dense accelerator kernel hoạt động hiệu quả hơn với ma trận (matrix / 행렬) lớn. Batch kích thước (size / 크기) lớn giúp tăng hardware utilization nhưng đồng thời tăng hàng đợi (queue / 큐) wait và bộ nhớ (memory / 메모리) usage.

Offline huấn luyện (training / 학습) có thể dùng batch lớn. Online suy luận (inference / 추론) thường cần động (dynamic / 동적) batching.

## Động (dynamic / 동적) Batching

Máy chủ (server / 서버) có thể chờ một khoảng rất ngắn để gom nhiều yêu cầu (request / 요청) thành một batch. sự đánh đổi (trade-off / 트레이드오프):

```text
chờ lâu hơn → batch lớn hơn → throughput tốt hơn
chờ ngắn hơn → latency tốt hơn → utilization thấp hơn
```

Không có một batch kích thước (size / 크기) tối ưu cho mọi hệ thống.

## Continuous Batching cho LLM

Batching truyền thống thường yêu cầu các chuỗi (sequence / 시퀀스) tiến cùng nhịp. LLM có đầu ra (output / 출력) length khác nhau nên dễ lãng phí padding và idle slot.

**Continuous batching** cho phép chuỗi (sequence / 시퀀스) hoàn thành rời khỏi batch và yêu cầu (request / 요청) mới được đưa vào scheduler ngay khi có chỗ.

Scheduler cần quản lý:

- prefill và decode;
- KV bộ nhớ (memory / 메모리);
- priority;
- fairness;
- max đơn vị từ (token / 토큰);
- cancellation.

## Microbatching trong huấn luyện (training / 학습)

Khi GPU bộ nhớ (memory / 메모리) không đủ cho một batch lớn, độ dốc (gradient / 기울기) accumulation chia logical batch thành nhiều microbatch:

```text
microbatch 1 → accumulate gradient
microbatch 2 → accumulate gradient
...
optimizer step
```

Effective batch kích thước (size / 크기) lớn hơn vật lý (physical / 물리적) batch kích thước (size / 크기).

## Yêu cầu (request / 요청) Coalescing

Nếu nhiều máy khách (client / 클라이언트) cùng yêu cầu một phép tính đắt tiền giống hệt nhau trong cùng thời điểm, hệ thống có thể gộp thành một in-flight yêu cầu (request / 요청) thay vì chạy nhiều bản trùng lặp.

## Rủi ro chất lượng do bộ nhớ đệm (cache / 캐시)

Caching có thể giữ nguyên lỗi cũ. Một câu trả lời hallucination nếu bị bộ nhớ đệm (cache / 캐시) có thể trở thành hallucination lặp lại nhiều lần. Vì vậy bộ nhớ đệm (cache / 캐시) chính sách (policy / 정책) nên phân biệt đầu ra (output / 출력) xác định và ổn định với đầu ra (output / 출력) cần freshness hoặc xác minh (verification / 확인).

## Khả năng quan sát (observability / 관측 가능성)

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

Hit tỷ lệ (rate / 비율) cao nhưng stale kết quả (result / 결과) nhiều không phải là thành công.

## Mô hình tư duy

```text
Caching  = tránh lặp lại công việc đã làm
Batching = làm công việc bắt buộc phải làm hiệu quả hơn
```

## Những nhầm lẫn thường gặp

### “bộ nhớ đệm (cache / 캐시) càng nhiều càng tốt”

Không. bộ nhớ đệm (cache / 캐시) làm tăng độ phức tạp (complexity / 복잡도), vô hiệu hóa (invalidation / 무효화) rủi ro (risk / 위험) và bộ nhớ (memory / 메모리) footprint.

### “Batch kích thước (size / 크기) càng lớn thì càng nhanh”

Không. thông lượng (throughput / 처리량) có thể tăng nhưng online độ trễ (latency / 지연 시간) và tail độ trễ (latency / 지연 시간) có thể xấu đi.

### “ngữ nghĩa (semantic / 의미적) bộ nhớ đệm (cache / 캐시) giống chính xác (exact / 정확한) bộ nhớ đệm (cache / 캐시)”

Không. ngữ nghĩa (semantic / 의미적) bộ nhớ đệm (cache / 캐시) thêm một bước learned similarity judgment nên có rủi ro chất lượng riêng.

## Liên kết kiến thức

Xem [Model Serving](./03_model_serving.md), [Latency, Throughput and Cost](./09_latency_throughput_and_cost.md), [RAG](../09_retrieval_and_rag/README.md) và [Transformer trong LLM](../08_large_language_models/03_transformer_inside_llms.md).

> **Bàn giao:** Sau **Liên kết kiến thức**, hãy chốt bất biến (invariant / 불변식) và giới hạn của mục này trước khi nối sang kiến thức kế tiếp. Có thể đọc tiếp [00 ai engineering](./00_ai_engineering.md) để đối chiếu ranh giới (boundary / 경계) gần nhất.
