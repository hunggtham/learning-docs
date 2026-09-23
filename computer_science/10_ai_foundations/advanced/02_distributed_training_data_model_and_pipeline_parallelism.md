# Huấn luyện phân tán: song song dữ liệu, mô hình và đường ống

Mô hình hiện đại có thể quá lớn hoặc quá chậm để huấn luyện trên một accelerator. **Huấn luyện phân tán (distributed training)** chia computation, parameters, gradients, optimizer state và activations qua nhiều devices/nodes. Nhưng thêm GPU chỉ hữu ích khi communication, synchronization, memory và input pipeline không trở thành bottleneck mới.

Mental model của chương này là: **distributed training là một synchronous/asynchronous state machine của model state**. Correctness cần workers cập nhật từ một logically compatible training step/state; performance phụ thuộc computation-to-communication ratio, topology, straggler behavior, pipeline bubbles và checkpoint/restart debt.

## 1. Bài toán ban đầu: một device không đủ capacity hoặc throughput

Có hai pressures khác nhau:

```text
memory capacity problem:
model + optimizer + activations không fit một device

throughput/time problem:
model fit nhưng training quá chậm
```

Data parallelism thường giải throughput; tensor/model/pipeline/sharded-state approaches giúp cả memory và compute. Chọn parallelism phải bắt đầu từ pressure nào đang dominate.

## 2. Invariant training step: workers phải agree state theo algorithm contract

Với synchronous data parallelism, invariant đơn giản hóa là:

> Mỗi logical optimization step phải aggregate gradients theo rule đã định từ workers dùng compatible parameter version, rồi update model state theo optimizer semantics.

Nếu worker dùng stale parameter version hoặc collective thiếu một subset ngoài protocol, result có thể không còn tương đương algorithm intended.

Distributed runtime vì vậy không chỉ “send tensors”; nó duy trì step membership, ordering và state version.

## 3. Data parallelism nhân batch work, rồi phải reconcile gradients

Mỗi worker giữ model replica và xử lý mini-batch subset. Sau backward pass, gradients được tổng hợp bằng collective như `all-reduce` hoặc reduce-scatter/all-gather composition.

Simplified:

```text
same parameter state
→ each worker forward/backward on local batch
→ aggregate gradients
→ optimizer update
→ next step state
```

Nếu compute per step nhỏ so với gradient bytes, communication dominates và scaling efficiency giảm.

## 4. Global batch size là algorithm parameter, không chỉ systems knob

Tăng data-parallel workers thường tăng global batch nếu per-device batch giữ nguyên. Điều này có thể đổi optimization dynamics, learning-rate schedule và generalization.

Do đó benchmark “8 GPU nhanh hơn 1 GPU” phải phân biệt:

```text
strong scaling: same total problem/batch workload split thinner
weak scaling: work/batch grows with workers
```

Throughput speedup không tự chứng minh same training semantics/quality trajectory.

## 5. Collective communication có topology và critical path

`all-reduce`, `all-gather`, `reduce-scatter`, broadcast không phải primitive zero-cost. Algorithm có thể dùng ring/tree/hierarchical topology.

Within-node interconnect thường nhanh hơn cross-node network. Efficient runtime cố map collectives theo topology:

```text
fast local links first
→ cross-node aggregation
→ local distribution
```

Nếu placement sai, same GPU count có throughput rất khác.

## 6. Overlap compute và communication chỉ hiệu quả khi dependency cho phép

Backward pass tạo gradients layer-by-layer. Runtime có thể bucket và start communication cho earlier gradients trong khi lower layers vẫn compute.

Overlap invariant:

```text
gradient bucket chỉ được transmit/consume khi values ready
optimizer step chỉ dùng aggregate đúng step
```

Bucket quá lớn trì hoãn communication; quá nhỏ tăng launch/protocol overhead. Performance optimization là schedule dependency graph, không chỉ tăng bandwidth.

## 7. Straggler biến synchronous step thành barrier latency

Trong synchronous training, step completes theo slowest required worker/collective participant.

Sources:

```text
GPU thermal/power variation
network congestion/retransmission
input pipeline stall
host CPU contention
memory pressure
one node hardware degradation
imbalanced batch/sequence lengths
```

Một worker chậm 20% có thể làm nhiều workers rảnh chờ. Average GPU utilization không đủ; cần per-rank timeline/skew.

## 8. Tensor/model parallelism chia operation nhưng tăng communication frequency

Khi layer/model không fit một accelerator, matrix/tensors có thể shard. Mỗi forward/backward layer thường cần collective exchange.

Trade-off:

```text
per-device memory ↓
per-device compute split
↔
collective communication + synchronization ↑
```

Granularity quá nhỏ làm compute kernel ngắn nhưng collective overhead gần như giữ nguyên, dẫn efficiency collapse.

## 9. Pipeline parallelism chia layers thành stages

Stages nhận micro-batches theo pipeline:

```text
Stage 1 → Stage 2 → Stage 3 → Stage 4
```

Bottleneck stage quyết định throughput. Fill/drain tạo **pipeline bubbles**.

Partition phải cân compute + activation transfer, không chỉ equal number of layers. Một stage attention/communication-heavy có thể chậm hơn nhiều dù có cùng layer count.

## 10. Pipeline schedule đổi memory-vs-bubble trade-off

Nhiều micro-batches tăng pipeline utilization nhưng giữ nhiều activations in-flight, tăng memory. Activation checkpointing/recomputation có thể giảm memory bằng cách tính lại forward intermediates trong backward.

Trade-off:

```text
memory ↓
↔
extra compute ↑
```

Distributed training thường là optimization multidimensional: memory saved ở one technique có thể tạo compute/network pressure elsewhere.

## 11. Optimizer state lớn hơn parameter file trực giác

Training memory không chỉ parameters. Có thể gồm:

```text
parameters
master/low-precision copies
gradients
optimizer moments/state
activations
communication buckets
temporary kernel workspace
allocator fragmentation
```

Adam-like optimizers có multiple state tensors. “Model weights 20 GB nên 24 GB GPU đủ” là sai capacity model.

## 12. Sharded optimizer/parameter state đổi memory thành collectives

ZeRO/FSDP-like families shard optimizer state, gradients và/hoặc parameters. Mỗi worker không cần giữ full copies mọi state, nhưng forward/backward có thể cần all-gather/reduce-scatter around layers/steps.

Invariant là parameter shard assembled/available đúng version tại point computation cần nó; memory reclamation không được xảy ra trước collective/users hoàn tất.

Again, this is ownership/lifetime protocol giống distributed buffer management.

## 13. Input pipeline có thể làm GPU đói

Nếu data decode/tokenization/augmentation/storage read không feed accelerator đủ nhanh, GPU utilization thấp dù communication tốt.

Data pipeline phải xét:

```text
storage throughput
CPU preprocessing
host-to-device transfer
shuffle/sampling semantics
worker shard assignment
prefetch buffers
```

Scaling GPU without scaling input path chỉ nhân expensive idle capacity.

## 14. Data sharding phải giữ sampling semantics

Mỗi data-parallel worker thường nhận distinct data shard per step/epoch. Duplicate/missing examples do sampler bug có thể thay training distribution.

Determinism không luôn required, nhưng sampling contract phải explicit. Khi restart worker/world size đổi, sharding/reseed semantics có thể đổi trajectory.

Correctness ở đây là **training algorithm/data distribution**, không chỉ tensors không crash.

## 15. Failure detection trong collective dễ biến một node fault thành whole-job stall

Nếu rank chết hoặc network partition, peers có thể block chờ collective completion tới timeout. “GPU utilization 0” trên surviving ranks có root cause là one missing participant.

Distributed runtime cần membership/failure semantics: fail fast job, elastic membership nếu algorithm supports, or restart from checkpoint.

Elasticity không trivial vì changing world size can alter batch/sampler/optimizer assumptions.

## 16. Checkpoint là durability protocol của training state

Checkpoint cần đủ state để restart theo guarantee desired:

```text
model parameters
optimizer state
scheduler/step counters
random/sampler state khi reproducibility cần
mixed-precision scaler/state
metadata describing sharding/world layout
```

Nếu chỉ save weights, có thể resume inference nhưng không thật sự resume optimizer trajectory.

## 17. Distributed checkpoint cần consistent snapshot semantics

Khi state sharded across workers, checkpoint không được mix shard từ step `N` với shard từ step `N+1` nếu format assumes one logical step.

Possible protocol families: barrier/snapshot at safe point, versioned shard files with manifest/commit marker, copy-on-write/background upload from immutable snapshot.

Invariant:

> Published checkpoint manifest chỉ reference a complete logically compatible set of shards.

Đây là same family với filesystem/database crash consistency.

## 18. Checkpoint frequency là RPO-vs-I/O trade-off

Checkpoint quá thường xuyên:

```text
storage/network I/O ↑
training step jitter ↑
object store pressure ↑
```

Quá thưa:

```text
failure → recompute many hours
```

Training RPO là amount of compute/state progression chấp nhận mất, không chỉ data bytes.

## 19. Restart time là RTO và có thể bottleneck ở checkpoint fan-in/out

Loading multi-TB checkpoint từ remote storage cho hundreds workers có thể saturate network/storage and create thundering herd.

Fast checkpoint write but slow restore still gives poor reliability. Measure both save and recovery critical path.

## 20. Scaling efficiency cần tách compute, communication, idle và input

Nếu 8 GPU nhanh 5× 1 GPU, efficiency ~62.5%, nhưng number alone không giải mechanism.

Per-step decomposition:

```text
useful compute
communication
pipeline bubble/idle
input wait
runtime/launch overhead
checkpoint/background work
```

Amdahl's Law gives intuition that non-scaling/coordination fraction limits speedup. At large scale even small serial/collective overhead dominates.

## 21. Network pressure có phase change

At small cluster, intra-node links dominate. Cross-node scale makes NIC/fabric topology important. At larger scale, oversubscription, congestion, collective synchronization and failure probability all increase.

A job can have same average bandwidth but worse step p99 due to transient congestion on one collective participant. Tail matters because barrier waits for slowest required path.

## 22. Mixed workload/cluster contention creates noisy neighbor

Training jobs may share network/storage/CPU control plane. Another job's checkpoint or shuffle can slow collectives/input path.

Resource scheduler that allocates GPUs but ignores fabric/storage bandwidth can overcommit hidden bottleneck.

Cluster capacity unit therefore is not simply “number of GPUs”. It includes topology-local groups, NIC bandwidth, host memory/CPU and storage path.

## 23. Numerical behavior may change with reduction order

Floating-point addition is not perfectly associative. Different collective tree/order/world size can produce small numerical differences. Usually training tolerates this, but reproducibility expectations must account for it.

“Same seed” does not automatically mean bit-identical distributed execution across topology/parallelism changes.

This connects computer arithmetic to distributed algorithm behavior.

## 24. Production evidence

Evidence should align ranks + phases:

```text
Compute:
- kernel/GPU utilization per rank
- forward/backward time
- memory allocated/reserved/fragmentation

Communication:
- collective duration by type/layer/bucket
- bytes and effective bandwidth
- topology/link errors/congestion

Synchronization:
- per-rank step start/end
- straggler skew / idle time

Input:
- data-loader wait/prefetch occupancy
- host-to-device transfer

Reliability:
- checkpoint save/load duration
- checkpoint version/step
- worker failure/timeout/restart timeline
```

Aggregate GPU utilization can hide rank 7 stalling every step while others wait.

## 25. Failure testing must include partial failure and slow failure

Not only kill a worker. Test:

```text
slow one rank
packet loss/latency on one node
input storage slowdown
checkpoint upload partial failure
restart from latest and previous checkpoint
world-size change if elasticity claimed
corrupt/missing shard manifest
```

After recovery verify logical training step/state, optimizer continuity according to contract and no silent data-sampler duplication/skip beyond expected semantics.

## 26. Abstraction nào thực sự quyết định behavior?

If GPU idle, root may be collective/input not compute kernel. If scaling plateaus, inspect compute-to-communication ratio and topology. If OOM after parallelism change, count optimizer/activation/communication workspace. If job hangs, inspect rank-level collective/membership state. If restart diverges, checkpoint/sampler/random state may be incomplete.

## 27. Mô hình tư duy

> Distributed training partitions **compute, memory and state ownership**, then pays communication/synchronization to make those partitions act like one training algorithm. Data parallelism reconciles gradients; tensor/pipeline parallelism moves activations/parameters across devices; sharding trades memory for collectives; checkpointing creates durable training state. **Performance is limited by the slowest synchronized path; correctness depends on step/version/state invariants surviving communication and failure.**

## Kết nối

Ôn [AI foundations](../../basic/10_ai_foundations/03_neural_networks_and_representation_learning.md), đọc [training/inference lifecycle](./00_training_inference_systems_and_model_lifecycle.md), [transformer/KV serving](./01_transformer_attention_kv_cache_and_inference_cost.md), [GPU execution](../../02_computer_architecture/advanced/06_simd_vector_isa_and_gpu_execution_model.md), [queueing/backpressure](../../08_software_systems/advanced/00_queueing_tail_latency_and_backpressure.md), [distributed failure/consensus](../../06_networks_distributed_systems/advanced/03_consensus_log_replication_reconfiguration_and_snapshots.md) và specialized AI library tại [`../../02_artificial_intelligence/`](../../02_artificial_intelligence/README.md).
