# Cluster Scheduling và Interconnect cho AI

> **Mạch đọc:** [README](./README.md) là bản đồ owner của **Cluster Scheduling và Interconnect cho AI**; nhìn vào vị trí đó trước để biết file này đang phục vụ nhánh kiến thức nào. **Vật lý (physical / 물리적) Topology** mở đối tượng chính của file và câu hỏi cần theo dõi; sau đó sang **Interconnect** để mở rộng đối tượng sang phạm vi kế cận. Cách đi này giữ lại điểm tựa của section đầu và cho biết kết luận sẽ được dùng ở đâu, thay vì dừng ở định nghĩa đầu tiên.

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

> **Chuyển mạch:** Trong **Cluster Scheduling và Interconnect cho AI**, **Interconnect** tiếp nhận điểm tựa từ **Vật lý (physical / 물리적) Topology** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Topology-Aware Placement** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

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

> **Chuyển mạch:** Ở chặng này của **Cluster Scheduling và Interconnect cho AI**, **Topology-Aware Placement** tiếp nhận điểm tựa từ **Interconnect** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Gang Scheduling** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Topology-Aware Placement

Scheduler nên đặt các worker của cùng một parallel group gần nhau theo vật lý (physical / 물리적) topology.

Ví dụ:

```text
tensor-parallel group → cùng node / fast domain
data-parallel replicas → có thể trải qua nhiều node
```

Topology-aware ánh xạ (mapping / 매핑) giúp giảm communication thời gian (time / 시간) bị lộ ra ngoài.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Cluster Scheduling và Interconnect cho AI**, **Gang Scheduling** tiếp nhận điểm tựa từ **Topology-Aware Placement** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Tài nguyên (resource / 자원) Fragmentation** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Gang Scheduling

Phân tán (distributed / 분산) huấn luyện (training / 학습) cần nhiều GPU cùng lúc. Nếu chỉ allocate được một phần thì job thường không thể chạy hữu ích.

**Gang scheduling** cấp toàn bộ tài nguyên (resource / 자원) cần thiết theo kiểu atomic.

Nhược điểm: large job có thể chờ lâu vì tài nguyên (resource / 자원) fragmentation.

> **Chuyển mạch:** Trong **Cluster Scheduling và Interconnect cho AI**, **Gang Scheduling** nêu điều cần giải thích; **Tài nguyên (resource / 자원) Fragmentation** đối chiếu nó với bằng chứng hoặc nguồn kiểm chứng. Từ đây, **Hàng đợi (queue / 큐) và Priority** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Tài nguyên (resource / 자원) Fragmentation

Cluster có thể báo tổng cộng 32 GPU rảnh nhưng chúng bị phân tán 1–2 GPU mỗi nút (node / 노드), trong khi job cần 8 GPU cùng một high-speed island. Logical free sức chứa (capacity / 용량) không đồng nghĩa schedulable sức chứa (capacity / 용량).

> **Chuyển mạch:** Ở chặng này của **Cluster Scheduling và Interconnect cho AI**, **Tài nguyên (resource / 자원) Fragmentation** nêu điều cần giải thích; **Hàng đợi (queue / 큐) và Priority** đối chiếu nó với bằng chứng hoặc nguồn kiểm chứng. Từ đây, **Preemption** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Hàng đợi (queue / 큐) và Priority

Cluster thường có nhiều hàng đợi (queue / 큐):

- interactive/gỡ lỗi (debug / 디버그);
- môi trường vận hành (production / 운영 환경) suy luận (inference / 추론);
- huấn luyện (training / 학습);
- batch embedding;
- low-priority experiment.

Priority chính sách (policy / 정책) cần tránh starvation nhưng đồng thời bảo vệ môi trường vận hành (production / 운영 환경) SLO.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Cluster Scheduling và Interconnect cho AI**, **Preemption** tiếp nhận điểm tựa từ **Hàng đợi (queue / 큐) và Priority** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Elasticity** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Preemption

Low-priority huấn luyện (training / 학습) có thể bị preempt để giải phóng tài nguyên (resource / 자원). Job phải checkpoint và resume hiệu quả.

Preemption phù hợp hơn với batch huấn luyện (training / 학습) so với stateful low-latency serving.

> **Chuyển mạch:** Trong **Cluster Scheduling và Interconnect cho AI**, **Elasticity** tiếp nhận điểm tựa từ **Preemption** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Bin Packing** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Elasticity

Một số tải công việc (workload / 워크로드) có thể thay world kích thước (size / 크기) trong thời gian chạy (runtime / 런타임). Elastic huấn luyện (training / 학습) giúp chịu thất bại (failure / 실패) tốt hơn hoặc tận dụng sức chứa (capacity / 용량) biến động, nhưng tối ưu hóa (optimization / 최적화) ngữ nghĩa (semantics / 의미론) và checkpointing phức tạp hơn.

> **Chuyển mạch:** Ở chặng này của **Cluster Scheduling và Interconnect cho AI**, **Bin Packing** tiếp nhận điểm tựa từ **Elasticity** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Multi-Instance hoặc Partitioned GPU** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Bin Packing

Scheduler cố pack tải công việc (workload / 워크로드) để giảm fragmentation và tăng utilization. Nhưng packing quá mạnh có thể tạo thermal, power hoặc noisy-neighbor tác động (effect / 효과).

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Cluster Scheduling và Interconnect cho AI**, **Multi-Instance hoặc Partitioned GPU** tiếp nhận điểm tựa từ **Bin Packing** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Mạng (network / 네트워크) Collective** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Multi-Instance hoặc Partitioned GPU

Một accelerator lớn có thể được partition cho nhiều tải công việc (workload / 워크로드) nhỏ hơn nếu hardware và thời gian chạy (runtime / 런타임) hỗ trợ.

Lợi ích: tăng utilization cho small suy luận (inference / 추론).

Rủi ro: contention trên dùng chung (shared / 공유) tài nguyên (resource / 자원) và khó dự đoán hiệu năng (performance / 성능).

> **Chuyển mạch:** Trong **Cluster Scheduling và Interconnect cho AI**, **Mạng (network / 네트워크) Collective** tiếp nhận điểm tựa từ **Multi-Instance hoặc Partitioned GPU** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Lưu trữ (storage / 저장소) Topology** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

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

> **Chuyển mạch:** Ở chặng này của **Cluster Scheduling và Interconnect cho AI**, **Lưu trữ (storage / 저장소) Topology** tiếp nhận điểm tựa từ **Mạng (network / 네트워크) Collective** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **CPU và RAM Allocation** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Lưu trữ (storage / 저장소) Topology

Huấn luyện (training / 학습) cluster còn cần dữ liệu (data / 데이터) và checkpoint lưu trữ (storage / 저장소). Nếu hàng nghìn worker cùng đọc central lưu trữ (storage / 저장소), I/O bottleneck xuất hiện.

Có thể dùng phân tán (distributed / 분산) bộ nhớ đệm (cache / 캐시), sharded dataset, prefetch và parallel checkpoint I/O.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Cluster Scheduling và Interconnect cho AI**, **CPU và RAM Allocation** tiếp nhận điểm tựa từ **Lưu trữ (storage / 저장소) Topology** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Scheduling cho suy luận (inference / 추론)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## CPU và RAM Allocation

GPU job vẫn cần CPU cho dữ liệu (data / 데이터) loader, tokenization và mạng (network / 네트워크) orchestration. Cấp thiếu CPU có thể làm GPU idle.

Host RAM cũng phải đủ cho buffering và preprocessing.

> **Chuyển mạch:** Trong **Cluster Scheduling và Interconnect cho AI**, **Scheduling cho suy luận (inference / 추론)** tiếp nhận điểm tựa từ **CPU và RAM Allocation** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Mô hình (model / 모델) Affinity** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Scheduling cho suy luận (inference / 추론)

Serving scheduler cần model-aware tài nguyên (resource / 자원) allocation:

- mô hình (model / 모델) residency;
- KV bộ nhớ đệm (cache / 캐시) sức chứa (capacity / 용량);
- batch tính tương thích (compatibility / 호환성);
- yêu cầu (request / 요청) priority;
- SLO.

Generic bộ chứa (container / 컨테이너) scheduler thường cần thêm specialized suy luận (inference / 추론) tầng (layer / 계층) phía trên.

> **Chuyển mạch:** Ở chặng này của **Cluster Scheduling và Interconnect cho AI**, **Mô hình (model / 모델) Affinity** tiếp nhận điểm tựa từ **Scheduling cho suy luận (inference / 추론)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Miền lỗi (failure domain / 장애 도메인)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Mô hình (model / 모델) Affinity

Nếu mô hình (model / 모델) đã resident trên GPU, tuyến (route / 경로) yêu cầu (request / 요청) tới GPU đó giúp tránh reload weights.

Multi-model serving phải cân bằng affinity với tải (load / 로드) balancing.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Cluster Scheduling và Interconnect cho AI**, **Miền lỗi (failure domain / 장애 도메인)** tiếp nhận điểm tựa từ **Mô hình (model / 모델) Affinity** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Sức chứa (capacity / 용량) Planning** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Miền lỗi (failure domain / 장애 도메인)

Rack, power hoặc mạng (network / 네트워크) thất bại (failure / 실패) có thể ảnh hưởng nhiều nút (node / 노드) cùng lúc. dịch vụ trọng yếu (critical service / 핵심 서비스) cần replica trải qua nhiều miền lỗi (failure domain / 장애 도메인).

Checkpoint lưu trữ (storage / 저장소) cũng cần tránh single miền lỗi (failure domain / 장애 도메인).

> **Chuyển mạch:** Trong **Cluster Scheduling và Interconnect cho AI**, **Sức chứa (capacity / 용량) Planning** tiếp nhận điểm tựa từ **Miền lỗi (failure domain / 장애 도메인)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Utilization và Responsiveness** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

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

> **Chuyển mạch:** Ở chặng này của **Cluster Scheduling và Interconnect cho AI**, **Utilization và Responsiveness** tiếp nhận điểm tựa từ **Sức chứa (capacity / 용량) Planning** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Mô hình tư duy** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Utilization và Responsiveness

Batch cluster thường muốn utilization cao. Online serving lại cần spare sức chứa (capacity / 용량) để hấp thụ burst. Dùng cùng một utilization mục tiêu (target / 대상) cho cả hai là không phù hợp.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Cluster Scheduling và Interconnect cho AI**, **Mô hình tư duy** gom các mảnh từ **Utilization và Responsiveness** thành một kết luận có thể mang sang phần kế tiếp. Từ đây, **Những nhầm lẫn thường gặp** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Mô hình tư duy

Phần này chốt mental model thành một chuỗi có thể dùng lại: bối cảnh → cơ chế → quan sát → giới hạn → quyết định. Hãy đọc sơ đồ như công cụ suy luận, không như một khẩu hiệu tách khỏi chapter.

```text
Cluster performance = compute placement × communication topology × scheduler policy × workload shape
```

> **Chuyển mạch:** Trong **Cluster Scheduling và Interconnect cho AI**, **Mô hình tư duy** đã nêu tiêu chí phân biệt, còn **Những nhầm lẫn thường gặp** dùng tiêu chí đó để soi ranh giới và điểm dễ nhầm. Từ đây, **Liên kết kiến thức** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Những nhầm lẫn thường gặp

### “Chỉ cần đếm GPU rảnh để schedule job”

Không. Topology và tính liền mạch của tài nguyên (resource / 자원) có thể khiến job vẫn không fit.

### “mạng (network / 네트워크) chỉ quan trọng khi cross-node”

Không. Link trong cùng nút (node / 노드) cũng khác nhau và ảnh hưởng tensor parallelism.

### “GPU job chỉ cần GPU”

Không. CPU, RAM, lưu trữ (storage / 저장소) và mạng (network / 네트워크) đều phải cấp dữ liệu và điều phối cho accelerator.

> **Chuyển mạch:** Ở chặng này của **Cluster Scheduling và Interconnect cho AI**, **Những nhầm lẫn thường gặp** đã nêu tiêu chí phân biệt, còn **Liên kết kiến thức** dùng tiêu chí đó để soi ranh giới và điểm dễ nhầm. Phần còn lại của file dùng kết quả này để khép lại mạch giải thích.

## Liên kết kiến thức

Xem [Distributed Training](./05_distributed_training.md), [Distributed Inference](./06_distributed_inference.md), [Memory/Bandwidth](./03_memory_and_bandwidth.md), [MLOps Incident Lifecycle](../16_mlops_and_llmops/09_incident_response_and_lifecycle.md).

> **Bàn giao:** Sau **Liên kết kiến thức**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](./README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
