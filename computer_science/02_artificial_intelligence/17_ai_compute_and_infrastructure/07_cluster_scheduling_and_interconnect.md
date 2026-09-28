# Cluster Scheduling và Interconnect cho AI

> **Mạch đọc:** Đặt **Cluster Scheduling và Interconnect cho AI** trong bản đồ [README](./README.md) để thấy đơn vị sở hữu (owner / 오너) và vị trí của nó. Nội dung đi từ **vật lý (physical / 물리적) Topology** sang **Interconnect**; điểm nối này chuẩn bị câu hỏi cho các mục sau thay vì dừng ở định nghĩa đầu tiên.


Khi AI tải công việc (workload / 워크로드) chạy trên nhiều accelerator, **cluster scheduler** và **interconnect** trở thành một phần của hiệu năng (performance / 성능) mô hình (model / 모델). Một job được đặt sai topology có thể có communication chậm hơn nhiều dù dùng cùng số GPU.

## Vật lý (physical / 물리적) Topology

Không phải mọi cặp GPU đều kết nối giống nhau.

```text
GPU ↔ GPU trong cùng node / high-speed link
GPU ↔ GPU qua PCIe
Node ↔ Node qua network fabric
```

Bandwidth và độ trễ (latency / 지연 시간) thay đổi theo từng đường dẫn (path / 경로).

Tensor parallelism có communication thường xuyên nên thường cần fast cục bộ (local / 로컬) link nhất. dữ liệu (data / 데이터) parallelism thường chịu được cross-node tốt hơn.

## Interconnect

Các thuộc tính quan trọng:

```text
bandwidth
latency
oversubscription
collective support
topology
failure rate
```

Aggregate bandwidth cao không bảo đảm pairwise hoặc collective hiệu năng (performance / 성능) tốt nếu mạng (network / 네트워크) bị oversubscribe.

## Topology-Aware Placement

Scheduler nên đặt các worker của cùng một parallel group gần nhau theo vật lý (physical / 물리적) topology.

Ví dụ:

```text
tensor-parallel group → cùng node / fast domain
data-parallel replicas → có thể trải qua nhiều node
```

Topology-aware ánh xạ (mapping / 매핑) giúp giảm communication thời gian (time / 시간) bị lộ ra ngoài.

## Gang Scheduling

Phân tán (distributed / 분산) huấn luyện (training / 학습) cần nhiều GPU cùng lúc. Nếu chỉ allocate được một phần thì job thường không thể chạy hữu ích.

**Gang scheduling** cấp toàn bộ tài nguyên (resource / 자원) cần thiết theo kiểu atomic.

Nhược điểm: large job có thể chờ lâu vì tài nguyên (resource / 자원) fragmentation.

## Tài nguyên (resource / 자원) Fragmentation

Cluster có thể báo tổng cộng 32 GPU rảnh nhưng chúng bị phân tán 1–2 GPU mỗi nút (node / 노드), trong khi job cần 8 GPU cùng một high-speed island. Logical free sức chứa (capacity / 용량) không đồng nghĩa schedulable sức chứa (capacity / 용량).

## Hàng đợi (queue / 큐) và Priority

Cluster thường có nhiều hàng đợi (queue / 큐):

- interactive/gỡ lỗi (debug / 디버그);
- môi trường vận hành (production / 운영 환경) suy luận (inference / 추론);
- huấn luyện (training / 학습);
- batch embedding;
- low-priority experiment.

Priority chính sách (policy / 정책) cần tránh starvation nhưng đồng thời bảo vệ môi trường vận hành (production / 운영 환경) SLO.

## Preemption

Low-priority huấn luyện (training / 학습) có thể bị preempt để giải phóng tài nguyên (resource / 자원). Job phải checkpoint và resume hiệu quả.

Preemption phù hợp hơn với batch huấn luyện (training / 학습) so với stateful low-latency serving.

## Elasticity

Một số tải công việc (workload / 워크로드) có thể thay world kích thước (size / 크기) trong thời gian chạy (runtime / 런타임). Elastic huấn luyện (training / 학습) giúp chịu thất bại (failure / 실패) tốt hơn hoặc tận dụng sức chứa (capacity / 용량) biến động, nhưng tối ưu hóa (optimization / 최적화) ngữ nghĩa (semantics / 의미론) và checkpointing phức tạp hơn.

## Bin Packing

Scheduler cố pack tải công việc (workload / 워크로드) để giảm fragmentation và tăng utilization. Nhưng packing quá mạnh có thể tạo thermal, power hoặc noisy-neighbor tác động (effect / 효과).

## Multi-Instance hoặc Partitioned GPU

Một accelerator lớn có thể được partition cho nhiều tải công việc (workload / 워크로드) nhỏ hơn nếu hardware và thời gian chạy (runtime / 런타임) hỗ trợ.

Lợi ích: tăng utilization cho small suy luận (inference / 추론).

Rủi ro: contention trên dùng chung (shared / 공유) tài nguyên (resource / 자원) và khó dự đoán hiệu năng (performance / 성능).

## Mạng (network / 네트워크) Collective

Collective thư viện (library / 라이브러리) triển khai all-reduce, all-gather hoặc all-to-all có nhận thức topology.

Hiệu năng (performance / 성능) phụ thuộc:

```text
message size
number of ranks
topology
algorithm như ring / tree
link contention
```

## Lưu trữ (storage / 저장소) Topology

Huấn luyện (training / 학습) cluster còn cần dữ liệu (data / 데이터) và checkpoint lưu trữ (storage / 저장소). Nếu hàng nghìn worker cùng đọc central lưu trữ (storage / 저장소), I/O bottleneck xuất hiện.

Có thể dùng phân tán (distributed / 분산) bộ nhớ đệm (cache / 캐시), sharded dataset, prefetch và parallel checkpoint I/O.

## CPU và RAM Allocation

GPU job vẫn cần CPU cho dữ liệu (data / 데이터) loader, tokenization và mạng (network / 네트워크) orchestration. Cấp thiếu CPU có thể làm GPU idle.

Host RAM cũng phải đủ cho buffering và preprocessing.

## Scheduling cho suy luận (inference / 추론)

Serving scheduler cần model-aware tài nguyên (resource / 자원) allocation:

- mô hình (model / 모델) residency;
- KV bộ nhớ đệm (cache / 캐시) sức chứa (capacity / 용량);
- batch tính tương thích (compatibility / 호환성);
- yêu cầu (request / 요청) priority;
- SLO.

Generic bộ chứa (container / 컨테이너) scheduler thường cần thêm specialized suy luận (inference / 추론) tầng (layer / 계층) phía trên.

## Mô hình (model / 모델) Affinity

Nếu mô hình (model / 모델) đã resident trên GPU, tuyến (route / 경로) yêu cầu (request / 요청) tới GPU đó giúp tránh reload weights.

Multi-model serving phải cân bằng affinity với tải (load / 로드) balancing.

## Miền lỗi (failure domain / 장애 도메인)

Rack, power hoặc mạng (network / 네트워크) thất bại (failure / 실패) có thể ảnh hưởng nhiều nút (node / 노드) cùng lúc. dịch vụ trọng yếu (critical service / 핵심 서비스) cần replica trải qua nhiều miền lỗi (failure domain / 장애 도메인).

Checkpoint lưu trữ (storage / 저장소) cũng cần tránh single miền lỗi (failure domain / 장애 도메인).

## Sức chứa (capacity / 용량) Planning

Không nên sizing cluster theo average tải công việc (workload / 워크로드). Cần tính tới:

```text
peak inference
training campaign
maintenance / failure headroom
model growth
seasonality
queue tolerance
```

## Utilization và Responsiveness

Batch cluster thường muốn utilization cao. Online serving lại cần spare sức chứa (capacity / 용량) để hấp thụ burst. Dùng cùng một utilization mục tiêu (target / 대상) cho cả hai là không phù hợp.

## Mô hình tư duy

```text
Cluster performance = compute placement × communication topology × scheduler policy × workload shape
```

## Những nhầm lẫn thường gặp

### “Chỉ cần đếm GPU rảnh để schedule job”

Không. Topology và tính liền mạch của tài nguyên (resource / 자원) có thể khiến job vẫn không fit.

### “mạng (network / 네트워크) chỉ quan trọng khi cross-node”

Không. Link trong cùng nút (node / 노드) cũng khác nhau và ảnh hưởng tensor parallelism.

### “GPU job chỉ cần GPU”

Không. CPU, RAM, lưu trữ (storage / 저장소) và mạng (network / 네트워크) đều phải cấp dữ liệu và điều phối cho accelerator.

## Liên kết kiến thức

Xem [Distributed Training](./05_distributed_training.md), [Distributed Inference](./06_distributed_inference.md), [Memory/Bandwidth](./03_memory_and_bandwidth.md), [MLOps Incident Lifecycle](../16_mlops_and_llmops/09_incident_response_and_lifecycle.md).

> **Bàn giao:** Sau **Liên kết kiến thức**, hãy chốt bất biến (invariant / 불변식) và giới hạn của mục này trước khi nối sang kiến thức kế tiếp. Có thể đọc tiếp [00 compute foundations](./00_compute_foundations.md) để đối chiếu ranh giới (boundary / 경계) gần nhất.
