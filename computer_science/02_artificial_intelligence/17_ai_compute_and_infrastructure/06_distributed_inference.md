# Distributed Inference

**Suy luận phân tán (distributed inference / 분산 추론)** dùng nhiều device hoặc node để phục vụ một model hoặc cả request workload. Khác distributed training, mục tiêu thường là latency, throughput, concurrency và cost thay vì gradient synchronization.

## Hai hướng Scale chính

```text
Scale out request → nhiều replica
Scale một model   → shard model qua nhiều device
```

Nếu model fit trên một GPU, request-level replication thường đơn giản và scale throughput tốt. Nếu model không fit hoặc latency target yêu cầu nhiều device cùng xử lý, cần model-parallel inference.

## Replica Parallelism

Mỗi replica giữ một bản đầy đủ của model.

```text
Load Balancer
├─ Replica A
├─ Replica B
└─ Replica C
```

Ưu điểm:

- isolation tốt;
- horizontal scaling đơn giản;
- failure của một replica không phá toàn bộ model group.

Nhược điểm: weight memory bị duplicate trên mỗi replica.

## Tensor Parallel Inference

Một layer được chia qua nhiều GPU. Mỗi token decode cần collective communication giữa các shard.

Tensor parallel phù hợp khi:

- model quá lớn cho một device;
- interconnect rất nhanh;
- batch hoặc concurrency đủ lớn để bù communication overhead.

Cross-node tensor parallel thường đắt hơn đáng kể do network latency và bandwidth thấp hơn.

## Pipeline Parallel Inference

Các layer được chia thành nhiều stage. Activation của request đi xuyên qua các stage này.

Pipeline có thể tăng capacity cho model rất lớn nhưng latency của mỗi request tăng do stage communication và scheduling.

## Expert Parallelism

MoE inference route token tới các expert shard khác nhau. Thách thức lớn là all-to-all communication, hot expert và load imbalance.

## Prefill và Decode

LLM inference có hai phase:

```text
Prefill → xử lý prompt token song song
Decode  → sinh token autoregressive theo chuỗi
```

Prefill thường có arithmetic intensity cao; decode thường nhạy với memory bandwidth và KV cache hơn.

Một cluster có thể **tách resource pool (disaggregate)** cho prefill và decode để dùng hardware phù hợp hơn cho từng phase.

## Vị trí của KV Cache

KV cache gắn với sequence state. Nếu request bị chuyển worker giữa các decode step, state phải migrate hoặc được truy cập từ xa, rất tốn.

Scheduler thường duy trì **session affinity** hoặc quản lý distributed KV cache một cách tường minh.

## Continuous Batching

Scheduler trên mỗi worker liên tục thêm và loại sequence theo từng token step. Trong môi trường phân tán cần cân bằng:

- batch efficiency;
- KV memory;
- fairness giữa tenant;
- priority;
- cancellation.

## Routing

Load balancer truyền thống thường chỉ nhìn request count. LLM router nên cân nhắc thêm:

```text
estimated prompt length
current KV memory
active sequences
model shard availability
priority / SLO
```

Một request có long context có thể nặng hơn hàng chục request ngắn.

## Model Routing

Hệ thống có thể route giữa nhiều model size:

```text
task dễ → small model
task khó hoặc giá trị cao → large model
domain đặc thù → specialist model
```

Routing model hoặc routing policy phải được evaluation như một component riêng.

## Autoscaling

Signal để scale có thể gồm:

- queue depth;
- pending token;
- GPU memory;
- request rate;
- TTFT;
- active sequence.

CPU metric thường không phản ánh đúng áp lực trên accelerator serving.

Cold start làm autoscaling LLM chậm vì model loading nặng. Warm pool hoặc predictive scaling có thể cần thiết.

## Multi-Tenancy

Nhiều tenant có thể dùng chung accelerator. Cần quota, priority và isolation.

Các rủi ro gồm:

- noisy neighbor;
- một tenant tiêu thụ quá nhiều long-context memory;
- cross-tenant data leakage do bug hoặc cache key sai.

## Speculative Decoding

Một draft model nhỏ đề xuất nhiều token; target model xác minh chúng. Nếu nhiều token được chấp nhận, số bước decode tuần tự đắt tiền giảm xuống.

Lợi ích phụ thuộc vào draft quality và hiệu quả của verification.

## Fault Tolerance

Nếu một shard trong tensor-parallel group fail, cả group thường fail theo. Replica group kết hợp health-aware routing giúp phục hồi tốt hơn.

Stateful generation làm retry khó hơn: hệ thống có thể phải regenerate prefix và KV cache hoặc resume từ persisted state.

## Streaming và Backpressure

Client đọc streamed token chậm có thể giữ tài nguyên lâu. Hệ thống cần buffer, backpressure và cancellation policy rõ.

## Tail Latency

Latency của distributed request bị chi phối bởi shard hoặc stage chậm nhất. Network jitter có thể làm p99 xấu dù average vẫn tốt.

## Cross-Region Serving

User toàn cầu có network latency khác nhau. Các chiến lược gồm:

- replicate model gần từng region;
- route theo geography hoặc compliance;
- centralize largest model và dùng regional smaller model.

Data residency rule có thể giới hạn placement.

## Cost-Aware Scheduling

Scheduler có thể tối ưu đồng thời:

```text
SLO satisfaction
GPU utilization
energy / cost
fairness
```

Không có một objective duy nhất phù hợp mọi workload.

## Mô hình tư duy

```text
Distributed inference = phân bố model state và request state trên hardware trong khi giảm communication và queueing.
```

## Những nhầm lẫn thường gặp

### “Dùng N GPU cho một model luôn giảm latency”

Không. Communication overhead có thể làm latency tăng ngược lại.

### “Load balancing theo request count là đủ”

Không. Token length và KV memory khiến trọng lượng của mỗi request rất khác nhau.

### “Inference stateless nên retry dễ”

Không phải lúc nào cũng đúng. Autoregressive generation, agent state và side effect có thể tạo stateful workflow.

## Liên kết kiến thức

Xem [Model Serving](../15_ai_engineering/03_model_serving.md), [Caching & Batching](../15_ai_engineering/05_caching_and_batching.md), [Parallel Computing](./04_parallel_computing.md), [Cluster Scheduling](./07_cluster_scheduling_and_interconnect.md).