# Phân tán (distributed / 분산) suy luận (inference / 추론)

> **Mạch đọc:** [README](./README.md) là bản đồ owner của **Distributed inference**. Route đi từ replica/tensor/pipeline parallelism → request routing → batching and queueing → consistency/fault handling → latency and utilization, để scale inference nối với SLO phục vụ.

**Suy luận phân tán (distributed inference / 분산 추론)** dùng nhiều thiết bị (device / 장치) hoặc nút (node / 노드) để phục vụ một mô hình (model / 모델) hoặc cả yêu cầu (request / 요청) tải công việc (workload / 워크로드). Khác phân tán (distributed / 분산) huấn luyện (training / 학습), mục tiêu thường là độ trễ (latency / 지연 시간), thông lượng (throughput / 처리량), tính đồng thời (concurrency / 동시성) và chi phí (cost / 비용) thay vì độ dốc (gradient / 기울기) synchronization.

## Hai hướng quy mô (scale / 규모) chính

Phần này chuyển khái niệm Computer Science thành cấu trúc, ví dụ hoặc quy trình có thể kiểm tra. Hãy xác định câu hỏi mà mục trả lời rồi nối kết luận với phần kế tiếp.

```text
Scale out request → nhiều replica
Scale một model   → shard model qua nhiều device
```

Nếu mô hình (model / 모델) fit trên một GPU, request-level replication thường đơn giản và quy mô (scale / 규모) thông lượng (throughput / 처리량) tốt. Nếu mô hình (model / 모델) không fit hoặc độ trễ (latency / 지연 시간) mục tiêu (target / 대상) yêu cầu nhiều thiết bị (device / 장치) cùng xử lý, cần model-parallel suy luận (inference / 추론).

> **Chuyển mạch:** Trong **Phân tán (distributed / 분산) suy luận (inference / 추론)**, **Replica Parallelism** tiếp nhận điểm tựa từ **Hai hướng quy mô (scale / 규모) chính** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Tensor Parallel suy luận (inference / 추론)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

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

> **Chuyển mạch:** Ở chặng này của **Phân tán (distributed / 분산) suy luận (inference / 추론)**, **Tensor Parallel suy luận (inference / 추론)** tiếp nhận điểm tựa từ **Replica Parallelism** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Chuỗi xử lý (pipeline / 파이프라인) Parallel suy luận (inference / 추론)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Tensor Parallel suy luận (inference / 추론)

Một tầng (layer / 계층) được chia qua nhiều GPU. Mỗi đơn vị từ (token / 토큰) decode cần collective communication giữa các shard.

Tensor parallel phù hợp khi:

- mô hình (model / 모델) quá lớn cho một thiết bị (device / 장치);
- interconnect rất nhanh;
- batch hoặc tính đồng thời (concurrency / 동시성) đủ lớn để bù communication overhead.

Cross-node tensor parallel thường đắt hơn đáng kể do mạng (network / 네트워크) độ trễ (latency / 지연 시간) và bandwidth thấp hơn.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Phân tán (distributed / 분산) suy luận (inference / 추론)**, **Tensor Parallel suy luận (inference / 추론)** xác định đầu vào; **Chuỗi xử lý (pipeline / 파이프라인) Parallel suy luận (inference / 추론)** giải thích bước vận hành tạo ra kết quả kế tiếp. Từ đây, **Expert Parallelism** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Chuỗi xử lý (pipeline / 파이프라인) Parallel suy luận (inference / 추론)

Các tầng (layer / 계층) được chia thành nhiều stage. Activation của yêu cầu (request / 요청) đi xuyên qua các stage này.

Chuỗi xử lý (pipeline / 파이프라인) có thể tăng sức chứa (capacity / 용량) cho mô hình (model / 모델) rất lớn nhưng độ trễ (latency / 지연 시간) của mỗi yêu cầu (request / 요청) tăng do stage communication và scheduling.

> **Chuyển mạch:** Trong **Phân tán (distributed / 분산) suy luận (inference / 추론)**, **Chuỗi xử lý (pipeline / 파이프라인) Parallel suy luận (inference / 추론)** xác định đầu vào; **Expert Parallelism** giải thích bước vận hành tạo ra kết quả kế tiếp. Từ đây, **Prefill và Decode** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Expert Parallelism

MoE suy luận (inference / 추론) tuyến (route / 경로) đơn vị từ (token / 토큰) tới các expert shard khác nhau. Thách thức lớn là all-to-all communication, hot expert và tải (load / 로드) imbalance.

> **Chuyển mạch:** Ở chặng này của **Phân tán (distributed / 분산) suy luận (inference / 추론)**, **Prefill và Decode** tiếp nhận điểm tựa từ **Expert Parallelism** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Vị trí của KV bộ nhớ đệm (cache / 캐시)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Prefill và Decode

LLM suy luận (inference / 추론) có hai phase:

```text
Prefill → xử lý prompt token song song
Decode  → sinh token autoregressive theo chuỗi
```

Prefill thường có arithmetic intensity cao; decode thường nhạy với bộ nhớ (memory / 메모리) bandwidth và KV bộ nhớ đệm (cache / 캐시) hơn.

Một cluster có thể **tách tài nguyên (resource / 자원) pool (disaggregate)** cho prefill và decode để dùng hardware phù hợp hơn cho từng phase.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Phân tán (distributed / 분산) suy luận (inference / 추론)**, **Vị trí của KV bộ nhớ đệm (cache / 캐시)** tiếp nhận điểm tựa từ **Prefill và Decode** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Continuous Batching** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Vị trí của KV bộ nhớ đệm (cache / 캐시)

KV bộ nhớ đệm (cache / 캐시) gắn với chuỗi (sequence / 시퀀스) trạng thái (state / 상태). Nếu yêu cầu (request / 요청) bị chuyển worker giữa các decode step, trạng thái (state / 상태) phải migrate hoặc được truy cập từ xa, rất tốn.

Scheduler thường duy trì **session affinity** hoặc quản lý phân tán (distributed / 분산) KV bộ nhớ đệm (cache / 캐시) một cách tường minh.

> **Chuyển mạch:** Trong **Phân tán (distributed / 분산) suy luận (inference / 추론)**, **Continuous Batching** tiếp nhận điểm tựa từ **Vị trí của KV bộ nhớ đệm (cache / 캐시)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Routing** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Continuous Batching

Scheduler trên mỗi worker liên tục thêm và loại chuỗi (sequence / 시퀀스) theo từng đơn vị từ (token / 토큰) step. Trong môi trường phân tán cần cân bằng:

- batch efficiency;
- KV bộ nhớ (memory / 메모리);
- fairness giữa tenant;
- priority;
- cancellation.

> **Chuyển mạch:** Ở chặng này của **Phân tán (distributed / 분산) suy luận (inference / 추론)**, **Routing** tiếp nhận điểm tựa từ **Continuous Batching** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Mô hình (model / 모델) Routing** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

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

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Phân tán (distributed / 분산) suy luận (inference / 추론)**, **Mô hình (model / 모델) Routing** tiếp nhận điểm tựa từ **Routing** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Autoscaling** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Mô hình (model / 모델) Routing

Hệ thống có thể tuyến (route / 경로) giữa nhiều mô hình (model / 모델) kích thước (size / 크기):

```text
task dễ → small model
task khó hoặc giá trị cao → large model
domain đặc thù → specialist model
```

Routing mô hình (model / 모델) hoặc routing chính sách (policy / 정책) phải được evaluation như một thành phần (component / 컴포넌트) riêng.

> **Chuyển mạch:** Trong **Phân tán (distributed / 분산) suy luận (inference / 추론)**, **Autoscaling** tiếp nhận điểm tựa từ **Mô hình (model / 모델) Routing** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Multi-Tenancy** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

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

> **Chuyển mạch:** Ở chặng này của **Phân tán (distributed / 분산) suy luận (inference / 추론)**, **Multi-Tenancy** tiếp nhận điểm tựa từ **Autoscaling** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Speculative Decoding** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Multi-Tenancy

Nhiều tenant có thể dùng chung accelerator. Cần quota, priority và isolation.

Các rủi ro gồm:

- noisy neighbor;
- một tenant tiêu thụ quá nhiều long-context bộ nhớ (memory / 메모리);
- cross-tenant dữ liệu (data / 데이터) leakage do bug hoặc bộ nhớ đệm (cache / 캐시) key sai.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Phân tán (distributed / 분산) suy luận (inference / 추론)**, **Speculative Decoding** tiếp nhận điểm tựa từ **Multi-Tenancy** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Fault Tolerance** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Speculative Decoding

Một draft mô hình (model / 모델) nhỏ đề xuất nhiều đơn vị từ (token / 토큰); mục tiêu (target / 대상) mô hình (model / 모델) xác minh chúng. Nếu nhiều đơn vị từ (token / 토큰) được chấp nhận, số bước decode tuần tự đắt tiền giảm xuống.

Lợi ích phụ thuộc vào draft chất lượng (quality / 품질) và hiệu quả của xác minh (verification / 확인).

> **Chuyển mạch:** Trong **Phân tán (distributed / 분산) suy luận (inference / 추론)**, **Fault Tolerance** tiếp nhận điểm tựa từ **Speculative Decoding** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Streaming và Backpressure** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Fault Tolerance

Nếu một shard trong tensor-parallel group thất bại (fail / 실패), cả group thường thất bại (fail / 실패) theo. Replica group kết hợp health-aware routing giúp phục hồi tốt hơn.

Stateful generation làm thử lại (retry / 재시도) khó hơn: hệ thống có thể phải regenerate prefix và KV bộ nhớ đệm (cache / 캐시) hoặc resume từ persisted trạng thái (state / 상태).

> **Chuyển mạch:** Ở chặng này của **Phân tán (distributed / 분산) suy luận (inference / 추론)**, **Streaming và Backpressure** tiếp nhận điểm tựa từ **Fault Tolerance** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Tail độ trễ (latency / 지연 시간)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Streaming và Backpressure

Máy khách (client / 클라이언트) đọc streamed đơn vị từ (token / 토큰) chậm có thể giữ tài nguyên lâu. Hệ thống cần buffer, backpressure và cancellation chính sách (policy / 정책) rõ.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Phân tán (distributed / 분산) suy luận (inference / 추론)**, **Tail độ trễ (latency / 지연 시간)** tiếp nhận điểm tựa từ **Streaming và Backpressure** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Cross-Region Serving** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Tail độ trễ (latency / 지연 시간)

Độ trễ (latency / 지연 시간) của phân tán (distributed / 분산) yêu cầu (request / 요청) bị chi phối bởi shard hoặc stage chậm nhất. mạng (network / 네트워크) jitter có thể làm p99 xấu dù average vẫn tốt.

> **Chuyển mạch:** Trong **Phân tán (distributed / 분산) suy luận (inference / 추론)**, **Cross-Region Serving** tiếp nhận điểm tựa từ **Tail độ trễ (latency / 지연 시간)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Cost-Aware Scheduling** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Cross-Region Serving

Người dùng (user / 사용자) toàn cầu có mạng (network / 네트워크) độ trễ (latency / 지연 시간) khác nhau. Các chiến lược gồm:

- replicate mô hình (model / 모델) gần từng region;
- tuyến (route / 경로) theo geography hoặc compliance;
- centralize largest mô hình (model / 모델) và dùng regional smaller mô hình (model / 모델).

Dữ liệu (data / 데이터) residency quy tắc (rule / 규칙) có thể giới hạn placement.

> **Chuyển mạch:** Ở chặng này của **Phân tán (distributed / 분산) suy luận (inference / 추론)**, **Cost-Aware Scheduling** tiếp nhận điểm tựa từ **Cross-Region Serving** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Mô hình tư duy** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Cost-Aware Scheduling

Scheduler có thể tối ưu đồng thời:

```text
SLO satisfaction
GPU utilization
energy / cost
fairness
```

Không có một mục tiêu (objective / 목표) duy nhất phù hợp mọi tải công việc (workload / 워크로드).

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Phân tán (distributed / 분산) suy luận (inference / 추론)**, **Mô hình tư duy** gom các mảnh từ **Cost-Aware Scheduling** thành một kết luận có thể mang sang phần kế tiếp. Từ đây, **Những nhầm lẫn thường gặp** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Mô hình tư duy

Phần này chốt mental model thành một chuỗi có thể dùng lại: bối cảnh → cơ chế → quan sát → giới hạn → quyết định. Hãy đọc sơ đồ như công cụ suy luận, không như một khẩu hiệu tách khỏi chapter.

```text
Distributed inference = phân bố model state và request state trên hardware trong khi giảm communication và queueing.
```

> **Chuyển mạch:** Trong **Phân tán (distributed / 분산) suy luận (inference / 추론)**, **Mô hình tư duy** đã nêu tiêu chí phân biệt, còn **Những nhầm lẫn thường gặp** dùng tiêu chí đó để soi ranh giới và điểm dễ nhầm. Từ đây, **Liên kết kiến thức** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Những nhầm lẫn thường gặp

### “Dùng N GPU cho một mô hình (model / 모델) luôn giảm độ trễ (latency / 지연 시간)”

Không. Communication overhead có thể làm độ trễ (latency / 지연 시간) tăng ngược lại.

### “tải (load / 로드) balancing theo yêu cầu (request / 요청) count là đủ”

Không. đơn vị từ (token / 토큰) length và KV bộ nhớ (memory / 메모리) khiến trọng lượng của mỗi yêu cầu (request / 요청) rất khác nhau.

### “suy luận (inference / 추론) stateless nên thử lại (retry / 재시도) dễ”

Không phải lúc nào cũng đúng. Autoregressive generation, tác nhân (agent / 에이전트) trạng thái (state / 상태) và side tác động (effect / 효과) có thể tạo stateful workflow.

> **Chuyển mạch:** Ở chặng này của **Phân tán (distributed / 분산) suy luận (inference / 추론)**, **Những nhầm lẫn thường gặp** đã nêu tiêu chí phân biệt, còn **Liên kết kiến thức** dùng tiêu chí đó để soi ranh giới và điểm dễ nhầm. Phần còn lại của file dùng kết quả này để khép lại mạch giải thích.

## Liên kết kiến thức

Xem [Model Serving](../15_ai_engineering/03_model_serving.md), [Caching & Batching](../15_ai_engineering/05_caching_and_batching.md), [Parallel Computing](./04_parallel_computing.md), [Cluster Scheduling](./07_cluster_scheduling_and_interconnect.md).

> **Bàn giao:** Sau **Liên kết kiến thức**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](./README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
