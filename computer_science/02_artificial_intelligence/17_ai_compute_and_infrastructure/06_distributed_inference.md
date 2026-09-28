# Phân tán (distributed / 분산) suy luận (inference / 추론)

> **Mạch đọc:** Đặt **phân tán (distributed / 분산) suy luận (inference / 추론)** trong bản đồ [README](./README.md) để thấy đơn vị sở hữu (owner / 오너) và vị trí của nó. Nội dung đi từ **Hai hướng quy mô (scale / 규모) chính** sang **Replica Parallelism**; điểm nối này chuẩn bị câu hỏi cho các mục sau thay vì dừng ở định nghĩa đầu tiên.


**Suy luận phân tán (distributed inference / 분산 추론)** dùng nhiều thiết bị (device / 장치) hoặc nút (node / 노드) để phục vụ một mô hình (model / 모델) hoặc cả yêu cầu (request / 요청) tải công việc (workload / 워크로드). Khác phân tán (distributed / 분산) huấn luyện (training / 학습), mục tiêu thường là độ trễ (latency / 지연 시간), thông lượng (throughput / 처리량), tính đồng thời (concurrency / 동시성) và chi phí (cost / 비용) thay vì độ dốc (gradient / 기울기) synchronization.

## Hai hướng quy mô (scale / 규모) chính

```text
Scale out request → nhiều replica
Scale một model   → shard model qua nhiều device
```

Nếu mô hình (model / 모델) fit trên một GPU, request-level replication thường đơn giản và quy mô (scale / 규모) thông lượng (throughput / 처리량) tốt. Nếu mô hình (model / 모델) không fit hoặc độ trễ (latency / 지연 시간) mục tiêu (target / 대상) yêu cầu nhiều thiết bị (device / 장치) cùng xử lý, cần model-parallel suy luận (inference / 추론).

## Replica Parallelism

Mỗi replica giữ một bản đầy đủ của mô hình (model / 모델).

```text
Load Balancer
├─ Replica A
├─ Replica B
└─ Replica C
```

Ưu điểm:

- isolation tốt;
- horizontal scaling đơn giản;
- thất bại (failure / 실패) của một replica không phá toàn bộ mô hình (model / 모델) group.

Nhược điểm: weight bộ nhớ (memory / 메모리) bị duplicate trên mỗi replica.

## Tensor Parallel suy luận (inference / 추론)

Một tầng (layer / 계층) được chia qua nhiều GPU. Mỗi đơn vị từ (token / 토큰) decode cần collective communication giữa các shard.

Tensor parallel phù hợp khi:

- mô hình (model / 모델) quá lớn cho một thiết bị (device / 장치);
- interconnect rất nhanh;
- batch hoặc tính đồng thời (concurrency / 동시성) đủ lớn để bù communication overhead.

Cross-node tensor parallel thường đắt hơn đáng kể do mạng (network / 네트워크) độ trễ (latency / 지연 시간) và bandwidth thấp hơn.

## Chuỗi xử lý (pipeline / 파이프라인) Parallel suy luận (inference / 추론)

Các tầng (layer / 계층) được chia thành nhiều stage. Activation của yêu cầu (request / 요청) đi xuyên qua các stage này.

Chuỗi xử lý (pipeline / 파이프라인) có thể tăng sức chứa (capacity / 용량) cho mô hình (model / 모델) rất lớn nhưng độ trễ (latency / 지연 시간) của mỗi yêu cầu (request / 요청) tăng do stage communication và scheduling.

## Expert Parallelism

MoE suy luận (inference / 추론) tuyến (route / 경로) đơn vị từ (token / 토큰) tới các expert shard khác nhau. Thách thức lớn là all-to-all communication, hot expert và tải (load / 로드) imbalance.

## Prefill và Decode

LLM suy luận (inference / 추론) có hai phase:

```text
Prefill → xử lý prompt token song song
Decode  → sinh token autoregressive theo chuỗi
```

Prefill thường có arithmetic intensity cao; decode thường nhạy với bộ nhớ (memory / 메모리) bandwidth và KV bộ nhớ đệm (cache / 캐시) hơn.

Một cluster có thể **tách tài nguyên (resource / 자원) pool (disaggregate)** cho prefill và decode để dùng hardware phù hợp hơn cho từng phase.

## Vị trí của KV bộ nhớ đệm (cache / 캐시)

KV bộ nhớ đệm (cache / 캐시) gắn với chuỗi (sequence / 시퀀스) trạng thái (state / 상태). Nếu yêu cầu (request / 요청) bị chuyển worker giữa các decode step, trạng thái (state / 상태) phải migrate hoặc được truy cập từ xa, rất tốn.

Scheduler thường duy trì **session affinity** hoặc quản lý phân tán (distributed / 분산) KV bộ nhớ đệm (cache / 캐시) một cách tường minh.

## Continuous Batching

Scheduler trên mỗi worker liên tục thêm và loại chuỗi (sequence / 시퀀스) theo từng đơn vị từ (token / 토큰) step. Trong môi trường phân tán cần cân bằng:

- batch efficiency;
- KV bộ nhớ (memory / 메모리);
- fairness giữa tenant;
- priority;
- cancellation.

## Routing

Bộ cân bằng tải (load balancer / 로드 밸런서) truyền thống thường chỉ nhìn yêu cầu (request / 요청) count. LLM router nên cân nhắc thêm:

```text
estimated prompt length
current KV memory
active sequences
model shard availability
priority / SLO
```

Một yêu cầu (request / 요청) có long ngữ cảnh (context / 맥락) có thể nặng hơn hàng chục yêu cầu (request / 요청) ngắn.

## Mô hình (model / 모델) Routing

Hệ thống có thể tuyến (route / 경로) giữa nhiều mô hình (model / 모델) kích thước (size / 크기):

```text
task dễ → small model
task khó hoặc giá trị cao → large model
domain đặc thù → specialist model
```

Routing mô hình (model / 모델) hoặc routing chính sách (policy / 정책) phải được evaluation như một thành phần (component / 컴포넌트) riêng.

## Autoscaling

Tín hiệu (signal / 신호) để quy mô (scale / 규모) có thể gồm:

- hàng đợi (queue / 큐) độ sâu (depth / 깊이);
- pending đơn vị từ (token / 토큰);
- GPU bộ nhớ (memory / 메모리);
- yêu cầu (request / 요청) tỷ lệ (rate / 비율);
- TTFT;
- active chuỗi (sequence / 시퀀스).

CPU chỉ số (metric / 지표) thường không phản ánh đúng áp lực trên accelerator serving.

Cold start làm autoscaling LLM chậm vì mô hình (model / 모델) loading nặng. Warm pool hoặc predictive scaling có thể cần thiết.

## Multi-Tenancy

Nhiều tenant có thể dùng chung accelerator. Cần quota, priority và isolation.

Các rủi ro gồm:

- noisy neighbor;
- một tenant tiêu thụ quá nhiều long-context bộ nhớ (memory / 메모리);
- cross-tenant dữ liệu (data / 데이터) leakage do bug hoặc bộ nhớ đệm (cache / 캐시) key sai.

## Speculative Decoding

Một draft mô hình (model / 모델) nhỏ đề xuất nhiều đơn vị từ (token / 토큰); mục tiêu (target / 대상) mô hình (model / 모델) xác minh chúng. Nếu nhiều đơn vị từ (token / 토큰) được chấp nhận, số bước decode tuần tự đắt tiền giảm xuống.

Lợi ích phụ thuộc vào draft chất lượng (quality / 품질) và hiệu quả của xác minh (verification / 확인).

## Fault Tolerance

Nếu một shard trong tensor-parallel group thất bại (fail / 실패), cả group thường thất bại (fail / 실패) theo. Replica group kết hợp health-aware routing giúp phục hồi tốt hơn.

Stateful generation làm thử lại (retry / 재시도) khó hơn: hệ thống có thể phải regenerate prefix và KV bộ nhớ đệm (cache / 캐시) hoặc resume từ persisted trạng thái (state / 상태).

## Streaming và Backpressure

Máy khách (client / 클라이언트) đọc streamed đơn vị từ (token / 토큰) chậm có thể giữ tài nguyên lâu. Hệ thống cần buffer, backpressure và cancellation chính sách (policy / 정책) rõ.

## Tail độ trễ (latency / 지연 시간)

Độ trễ (latency / 지연 시간) của phân tán (distributed / 분산) yêu cầu (request / 요청) bị chi phối bởi shard hoặc stage chậm nhất. mạng (network / 네트워크) jitter có thể làm p99 xấu dù average vẫn tốt.

## Cross-Region Serving

Người dùng (user / 사용자) toàn cầu có mạng (network / 네트워크) độ trễ (latency / 지연 시간) khác nhau. Các chiến lược gồm:

- replicate mô hình (model / 모델) gần từng region;
- tuyến (route / 경로) theo geography hoặc compliance;
- centralize largest mô hình (model / 모델) và dùng regional smaller mô hình (model / 모델).

Dữ liệu (data / 데이터) residency quy tắc (rule / 규칙) có thể giới hạn placement.

## Cost-Aware Scheduling

Scheduler có thể tối ưu đồng thời:

```text
SLO satisfaction
GPU utilization
energy / cost
fairness
```

Không có một mục tiêu (objective / 목표) duy nhất phù hợp mọi tải công việc (workload / 워크로드).

## Mô hình tư duy

```text
Distributed inference = phân bố model state và request state trên hardware trong khi giảm communication và queueing.
```

## Những nhầm lẫn thường gặp

### “Dùng N GPU cho một mô hình (model / 모델) luôn giảm độ trễ (latency / 지연 시간)”

Không. Communication overhead có thể làm độ trễ (latency / 지연 시간) tăng ngược lại.

### “tải (load / 로드) balancing theo yêu cầu (request / 요청) count là đủ”

Không. đơn vị từ (token / 토큰) length và KV bộ nhớ (memory / 메모리) khiến trọng lượng của mỗi yêu cầu (request / 요청) rất khác nhau.

### “suy luận (inference / 추론) stateless nên thử lại (retry / 재시도) dễ”

Không phải lúc nào cũng đúng. Autoregressive generation, tác nhân (agent / 에이전트) trạng thái (state / 상태) và side tác động (effect / 효과) có thể tạo stateful workflow.

## Liên kết kiến thức

Xem [Model Serving](../15_ai_engineering/03_model_serving.md), [Caching & Batching](../15_ai_engineering/05_caching_and_batching.md), [Parallel Computing](./04_parallel_computing.md), [Cluster Scheduling](./07_cluster_scheduling_and_interconnect.md).

> **Bàn giao:** Sau **Liên kết kiến thức**, hãy chốt bất biến (invariant / 불변식) và giới hạn của mục này trước khi nối sang kiến thức kế tiếp. Có thể đọc tiếp [00 compute foundations](./00_compute_foundations.md) để đối chiếu ranh giới (boundary / 경계) gần nhất.
