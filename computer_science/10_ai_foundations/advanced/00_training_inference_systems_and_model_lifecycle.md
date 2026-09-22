# Training, inference systems và model lifecycle

Foundation ML thường tập trung model, loss và generalization. Production AI cần thêm mental model systems: **data, model, optimizer state và serving runtime đi qua một lifecycle versioned**, và mỗi stage có invariant, resource bottleneck, failure mode và evidence riêng.

Model weights chỉ là một artifact. Một production model thực tế phụ thuộc tokenizer/preprocessing, feature/data schema, code, checkpoint state, runtime kernels, hardware, serving config và evaluation contract.

## 1. Invariant đầu tiên: phải biết chính xác artifact nào tạo ra behavior

Nếu production trả output sai, câu “đang dùng model v42” chưa đủ. Cần biết bundle:

```text
training data/version/provenance
preprocessing/tokenizer/feature code
model architecture + weights
optimizer/checkpoint metadata khi resume training
runtime/library/kernel versions
quantization format
serving config + thresholds
prompt/template nếu system có layer đó
```

Reproducibility invariant là: từ artifact identity và provenance, team phải có khả năng giải thích model nào, data nào và runtime nào tạo behavior đang quan sát.

## 2. Training system là dataflow + optimization state

Một training step thường là:

```text
storage
→ read/decode/preprocess
→ shuffle/sample/batch
→ host memory
→ accelerator transfer
→ forward
→ loss
→ backward
→ gradient synchronization
→ optimizer update
→ checkpoint/metrics
```

GPU utilization thấp không tự động nghĩa GPU yếu. Input pipeline, data loader, synchronization hoặc host→device transfer có thể làm accelerator starve.

Performance reasoning phải profile toàn pipeline thay vì chỉ kernel compute.

## 3. Checkpoint không chỉ là weights

Để resume training gần tương đương trajectory trước interruption, thường cần:

```text
model parameters
optimizer state
scheduler state
random/RNG state
gradient scaler nếu mixed precision
training step/epoch/data position
parallelism/sharding metadata
```

Chỉ lưu weights có thể tiếp tục từ cùng model parameters nhưng không phải cùng optimization state.

Invariant recovery cần được định nghĩa rõ: “resume usable model” hay “resume equivalent training state”.

## 4. Data ordering và randomness cũng là state

Shuffle seed, sampler position, data augmentation randomness và distributed worker partitioning có thể thay training trajectory.

Reproducibility tuyệt đối trên accelerators đôi khi khó vì nondeterministic kernels, reduction order hoặc floating-point behavior. Điều quan trọng là phân biệt:

```text
bitwise reproducibility
statistical reproducibility
model-quality reproducibility
```

Không hứa mức mạnh hơn stack thực sự đảm bảo.

## 5. Distributed training thêm communication invariant

Data parallelism replicate model và aggregate gradients. Tensor/model/pipeline parallelism chia computation/state theo dimension khác.

Mỗi strategy cần giữ một invariant tương đương với optimization step mong muốn: gradients/parameters phải được combine theo protocol đúng, không để worker dùng state lệch không được model semantics cho phép.

Failure một worker có thể làm collective communication treo hoặc cả job restart. Distributed training vì thế là distributed-systems problem chứ không chỉ linear algebra.

## 6. Straggler quyết định step time trong synchronous training

Synchronous step thường phải chờ participants cần thiết. Một GPU/node chậm do thermal throttling, network congestion, data-loader stall hoặc hardware error có thể kéo toàn job.

Step latency gần với slowest required participant, tương tự tail amplification trong fan-out service.

Evidence cần per-rank/per-stage timing, không chỉ global tokens/s.

## 7. Communication topology là lower layer quan trọng

All-reduce hoặc tensor-parallel communication phụ thuộc PCIe/NVLink/InfiniBand/Ethernet topology, bandwidth và latency.

Model có arithmetic intensity cao có thể scale tốt; model nhỏ hoặc communication-heavy có thể đạt speedup rất kém khi thêm accelerators.

Performance invariant không phải “GPU count gấp đôi thì throughput gấp đôi”. Speedup bị giới hạn bởi compute/communication ratio, synchronization và load imbalance.

## 8. Mixed precision và numerical stability

FP16/BF16/TF32/low precision tăng throughput và giảm memory bandwidth/footprint nhưng đổi numerical behavior.

Loss scaling, accumulation precision và kernel choice quyết định stability. NaN/Inf có thể xuất hiện khi dynamic range không đủ hoặc optimizer state bất ổn.

Đây là connection giữa numerical representation và systems performance: chọn precision là một correctness-performance trade-off, không chỉ hardware flag.

## 9. Inference có objective khác training

Training thường tối ưu throughput/cost theo samples hoặc tokens processed. Online inference quan tâm:

```text
p50/p95/p99 latency
throughput
time-to-first-token nếu autoregressive
inter-token latency
memory per request
availability
cost per request/token
```

Một optimization tăng total throughput nhưng làm p99 vượt SLO có thể không phù hợp production API.

## 10. Dynamic/continuous batching là queueing decision

Batching tăng accelerator utilization nhưng request phải chờ batch formation. Continuous batching tái sử dụng slots khi sequences hoàn tất khác thời điểm.

Mental model:

```text
batch lớn hơn
→ compute efficiency tăng
→ queue/batching wait có thể tăng
→ memory pressure/concurrency thay đổi
```

Batch scheduler vì vậy là một admission/queueing controller tương tự Software Systems.

## 11. KV cache biến context thành memory-capacity problem

Autoregressive Transformer lưu key/value states của prior tokens để không recompute toàn prefix mỗi token.

KV cache memory tăng theo roughly:

```text
sequence length
× layers
× hidden/head dimensions
× bytes per element
× concurrent sequences
```

Context length dài có thể giảm concurrency mạnh dù weights không đổi. Khi memory gần đầy, allocator fragmentation hoặc cache eviction/offload có thể làm latency phase-change.

Inference bottleneck lúc đó là memory capacity/bandwidth, không phải raw FLOPS.

## 12. Quantization không đồng nghĩa luôn nhanh hơn

INT8/FP8/low-bit weights giảm footprint/bandwidth, nhưng speedup phụ thuộc kernel support, dequantization overhead, packing layout và hardware execution units.

Một model nhỏ fit cache tốt sẵn có thể không được lợi nhiều. Quantization cũng có quality impact khác theo layer/task/data distribution.

Do đó phải evaluate **quality + latency + throughput + memory** cùng nhau trên deployment workload.

## 13. Model loading và cold start là production phase riêng

Large model start có thể gồm download artifact, checksum, deserialize, allocate memory, compile kernels/JIT, warm caches và create KV allocator.

Autoscaling chỉ dựa CPU/GPU utilization có thể phản ứng quá chậm nếu new replica mất nhiều phút mới ready.

Capacity design cần model warm capacity, startup time và deployment headroom.

## 14. Model registry là provenance system, không chỉ file store

Registry cần nối artifact với:

```text
code commit/config
dataset snapshot/provenance
evaluation result
approval/deployment status
runtime compatibility
rollback target
```

Version weights nhưng không version tokenizer/schema có thể tạo silent incompatibility.

“Model” nên được coi là bundle có contract, không phải một `.bin` đơn lẻ.

## 15. Offline metric và online outcome khác nhau

Validation accuracy/F1/loss không tự động dự đoán business outcome do threshold, latency, population shift, user adaptation hoặc feedback loop.

Deployment có thể cần shadow, canary hoặc A/B tùy risk. Nhưng online experiment cũng phải giữ system invariant: cohort assignment ổn định, exposure logged, safety constraints enforce trước model decision nếu cần.

## 16. Data/model drift không có một metric universal

Input distribution thay đổi không luôn làm quality xấu; quality có thể xấu mà simple feature distribution không drift rõ.

Khi labels đến chậm, monitoring thường phải kết hợp:

```text
schema/data-quality violations
input distribution
score/confidence distribution
system latency/error
human/business proxy
late-arriving labeled evaluation
```

Không nên gọi một divergence score là “accuracy real-time” nếu không có ground truth.

## 17. Retraining là state transition có regression risk

Retrain hàng ngày không tự động tốt. Data window, label delay, concept drift, cost và poisoning/bad-data risk cần policy.

Pipeline hợp lý là:

```text
new data
→ train candidate
→ evaluate against fixed + recent slices
→ safety/regression checks
→ approve/canary
→ observe
→ promote hoặc rollback
```

Mỗi retrain tạo artifact mới; auto-promotion càng mạnh thì guardrail/provenance càng phải mạnh.

## 18. Failure modes cần được phân lớp

Training:

```text
input starvation
OOM
NaN/divergence
collective hang
straggler
checkpoint corruption/incompatibility
bad-data regression
```

Inference:

```text
queue overload
OOM/KV exhaustion
cold-start capacity loss
kernel/runtime crash
model/tokenizer mismatch
latency regression
bad model output dưới distribution shift
```

Gom mọi thứ thành “model issue” làm investigation sai layer.

## 19. Production evidence

Training evidence nên có:

```text
samples/tokens per second
GPU/accelerator utilization
input-pipeline wait
per-rank step timing
communication time
memory allocated/reserved
loss/gradient statistics
checkpoint duration/failure
```

Inference evidence nên có:

```text
time-to-first-token / inter-token latency
batching/queue wait
active sequences/concurrency
KV-cache usage/fragmentation
accelerator compute + memory utilization
model/runtime version
OOM/rejection rate
quality/evaluation slices
```

Metrics phải giữ artifact identity để regression có thể correlate với model/runtime/config rollout.

## 20. Lower abstraction nào quyết định behavior?

GPU utilization thấp có thể do storage/data loader/CPU, không phải GPU. Inference p99 tăng có thể do queue/batching, allocator hoặc network. Distributed training hang có thể do interconnect/collective library. Quality regression có thể do tokenizer/data schema chứ không phải weights.

AI systems debugging phải đi xuống đúng abstraction layer như mọi distributed/software system khác.

## 21. Connection với Reliability và System Design

Model serving là service có finite capacity. Retry, admission control, load shedding và graceful degradation vẫn áp dụng.

Ví dụ context quá dài làm KV cache đầy → queue tăng → timeout → gateway retry → duplicate inference work → overload. Fix không nhất thiết là “GPU mạnh hơn”; có thể cần token limit, concurrency admission, retry budget và overload response.

AI không đứng ngoài Computer Science systems principles; nó chỉ có resource shape khác.

## 22. Mô hình tư duy

> Production AI là **versioned dataflow + optimization state + distributed compute + serving queue + evaluation feedback loop**. Invariant về provenance/recovery/correctness phải được giữ qua data/model/runtime versions; performance bị quyết định bởi compute, memory, communication và queueing; evidence phải nối model quality với system behavior thay vì coi weights là toàn bộ hệ thống.

## Kết nối

Đọc cùng [ML foundation](../../basic/10_ai_foundations/02_machine_learning_foundations.md), [Transformer/KV cache](./01_transformer_attention_kv_cache_and_inference_cost.md), [Distributed training](./02_distributed_training_data_model_and_pipeline_parallelism.md), [Capacity/admission control](../../08_software_systems/advanced/01_capacity_planning_utilization_knee_and_admission_control.md) và [Deployment safety](../../09_software_engineering/advanced/05_deployment_safety_canary_blue_green_flags_and_rollback.md).