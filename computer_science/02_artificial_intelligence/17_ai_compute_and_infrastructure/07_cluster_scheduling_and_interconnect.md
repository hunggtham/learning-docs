# Cluster Scheduling và Interconnect cho AI

Khi AI workload chạy trên nhiều accelerator, **cluster scheduler** và **interconnect** trở thành một phần của performance model. Một job được đặt sai topology có thể có communication chậm hơn nhiều dù dùng cùng số GPU.

## Physical Topology

Không phải mọi cặp GPU đều kết nối giống nhau.

```text
GPU ↔ GPU trong cùng node / high-speed link
GPU ↔ GPU qua PCIe
Node ↔ Node qua network fabric
```

Bandwidth và latency thay đổi theo từng path.

Tensor parallelism có communication thường xuyên nên thường cần fast local link nhất. Data parallelism thường chịu được cross-node tốt hơn.

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

Aggregate bandwidth cao không bảo đảm pairwise hoặc collective performance tốt nếu network bị oversubscribe.

## Topology-Aware Placement

Scheduler nên đặt các worker của cùng một parallel group gần nhau theo physical topology.

Ví dụ:

```text
tensor-parallel group → cùng node / fast domain
data-parallel replicas → có thể trải qua nhiều node
```

Topology-aware mapping giúp giảm communication time bị lộ ra ngoài.

## Gang Scheduling

Distributed training cần nhiều GPU cùng lúc. Nếu chỉ allocate được một phần thì job thường không thể chạy hữu ích.

**Gang scheduling** cấp toàn bộ resource cần thiết theo kiểu atomic.

Nhược điểm: large job có thể chờ lâu vì resource fragmentation.

## Resource Fragmentation

Cluster có thể báo tổng cộng 32 GPU rảnh nhưng chúng bị phân tán 1–2 GPU mỗi node, trong khi job cần 8 GPU cùng một high-speed island. Logical free capacity không đồng nghĩa schedulable capacity.

## Queue và Priority

Cluster thường có nhiều queue:

- interactive/debug;
- production inference;
- training;
- batch embedding;
- low-priority experiment.

Priority policy cần tránh starvation nhưng đồng thời bảo vệ production SLO.

## Preemption

Low-priority training có thể bị preempt để giải phóng resource. Job phải checkpoint và resume hiệu quả.

Preemption phù hợp hơn với batch training so với stateful low-latency serving.

## Elasticity

Một số workload có thể thay world size trong runtime. Elastic training giúp chịu failure tốt hơn hoặc tận dụng capacity biến động, nhưng optimization semantics và checkpointing phức tạp hơn.

## Bin Packing

Scheduler cố pack workload để giảm fragmentation và tăng utilization. Nhưng packing quá mạnh có thể tạo thermal, power hoặc noisy-neighbor effect.

## Multi-Instance hoặc Partitioned GPU

Một accelerator lớn có thể được partition cho nhiều workload nhỏ hơn nếu hardware và runtime hỗ trợ.

Lợi ích: tăng utilization cho small inference.

Rủi ro: contention trên shared resource và khó dự đoán performance.

## Network Collective

Collective library triển khai all-reduce, all-gather hoặc all-to-all có nhận thức topology.

Performance phụ thuộc:

```text
message size
number of ranks
topology
algorithm như ring / tree
link contention
```

## Storage Topology

Training cluster còn cần data và checkpoint storage. Nếu hàng nghìn worker cùng đọc central storage, I/O bottleneck xuất hiện.

Có thể dùng distributed cache, sharded dataset, prefetch và parallel checkpoint I/O.

## CPU và RAM Allocation

GPU job vẫn cần CPU cho data loader, tokenization và network orchestration. Cấp thiếu CPU có thể làm GPU idle.

Host RAM cũng phải đủ cho buffering và preprocessing.

## Scheduling cho Inference

Serving scheduler cần model-aware resource allocation:

- model residency;
- KV cache capacity;
- batch compatibility;
- request priority;
- SLO.

Generic container scheduler thường cần thêm specialized inference layer phía trên.

## Model Affinity

Nếu model đã resident trên GPU, route request tới GPU đó giúp tránh reload weights.

Multi-model serving phải cân bằng affinity với load balancing.

## Failure Domain

Rack, power hoặc network failure có thể ảnh hưởng nhiều node cùng lúc. Critical service cần replica trải qua nhiều failure domain.

Checkpoint storage cũng cần tránh single failure domain.

## Capacity Planning

Không nên sizing cluster theo average workload. Cần tính tới:

```text
peak inference
training campaign
maintenance / failure headroom
model growth
seasonality
queue tolerance
```

## Utilization và Responsiveness

Batch cluster thường muốn utilization cao. Online serving lại cần spare capacity để hấp thụ burst. Dùng cùng một utilization target cho cả hai là không phù hợp.

## Mô hình tư duy

```text
Cluster performance = compute placement × communication topology × scheduler policy × workload shape
```

## Những nhầm lẫn thường gặp

### “Chỉ cần đếm GPU rảnh để schedule job”

Không. Topology và tính liền mạch của resource có thể khiến job vẫn không fit.

### “Network chỉ quan trọng khi cross-node”

Không. Link trong cùng node cũng khác nhau và ảnh hưởng tensor parallelism.

### “GPU job chỉ cần GPU”

Không. CPU, RAM, storage và network đều phải cấp dữ liệu và điều phối cho accelerator.

## Liên kết kiến thức

Xem [Distributed Training](./05_distributed_training.md), [Distributed Inference](./06_distributed_inference.md), [Memory/Bandwidth](./03_memory_and_bandwidth.md), [MLOps Incident Lifecycle](../16_mlops_and_llmops/09_incident_response_and_lifecycle.md).