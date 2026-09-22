# Advanced AI & ML Systems

Phần này giữ AI Foundations trong boundary của Computer Science: model lifecycle, training/inference systems, accelerator utilization, distributed execution và production evaluation. Không mở chapter chỉ vì một model family hay framework đang nổi.

## Canonical chapters

1. [Training, inference systems và model lifecycle](./00_training_inference_systems_and_model_lifecycle.md)
2. [Transformer internals, attention, KV cache và inference cost](./01_transformer_attention_kv_cache_and_inference_cost.md)
3. [Distributed training: data, model và pipeline parallelism](./02_distributed_training_data_model_and_pipeline_parallelism.md)
4. [Inference disaggregation, prefill/decode và placement của KV cache](./03_inference_disaggregation_prefill_decode_and_kv_cache_placement.md)

## Mental models cần đạt

AI system phải được đọc như một versioned dataflow có state và resource constraints:

```text
data/version
→ preprocessing/tokenization
→ training state/checkpoint
→ model artifact
→ serving runtime
→ batching/cache/accelerator memory
→ prediction
→ evaluation/feedback
```

Ở inference, cần thêm state path:

```text
admission
→ prefill
→ KV state
→ placement / transfer
→ decode loop
→ token stream
→ cancellation / cleanup
```

Mỗi stage có invariant riêng: artifact lineage phải truy được, train/eval distribution phải được phân biệt, checkpoint phải đủ state để resume theo contract, serving phải tôn trọng latency/capacity budget, KV state phải gắn đúng model/request/version và online behavior phải được đánh giá bằng evidence phù hợp chứ không chỉ offline metric.

## Performance pressure

AI performance không chỉ là FLOPS. Bottleneck có thể nằm ở input pipeline, host-device transfer, accelerator memory, KV cache, communication collective, batching delay hoặc request queue. Vì vậy phải phân biệt compute-bound, memory-bound và communication-bound behavior.

Prefill và decode cũng không có resource profile giống nhau. Prefill thường có parallel compute lớn hơn; decode lặp theo token và dễ bị memory/KV/scheduler pressure. Disaggregation chỉ có lợi khi specialization/independent scaling lớn hơn state-transfer cost, extra queue và failure surface.

Distributed training là distributed system: synchronization, straggler, topology và failure recovery quyết định scaling efficiency. Inference serving cũng là software system: queueing, admission control, cache lifetime, placement, version rollout và cancellation quyết định tail latency/reliability.

## Connection với các domain khác

Không duplicate nội dung system-level đã có. Queue/capacity đọc tại [`08_software_systems/advanced`](../../08_software_systems/advanced/README.md), distributed coordination tại [`06_networks_distributed_systems/advanced`](../../06_networks_distributed_systems/advanced/README.md), deployment/evolution tại [`09_software_engineering/advanced`](../../09_software_engineering/advanced/README.md), hardware/cache/SIMD/GPU/DVFS tại [`02_computer_architecture/advanced`](../../02_computer_architecture/advanced/README.md).

Retrieval, vector search, MLOps hay model security chỉ được mở rộng ở đây nếu cần một mental model foundational mới; nếu đã thuộc AI specialization riêng thì cross-link thay vì duplicate.

## Production evidence

Evidence cần bao phủ cả model và system: dataset/artifact version, training throughput/utilization, checkpoint/recovery state, communication stalls, accelerator memory/KV-cache pressure, prefill/decode queue riêng, TTFT, inter-token latency, KV transfer/placement time, active sequence/token budget, latency percentile, error/timeout/cancellation, model version/cohort, drift/data-quality signal và offline-online metric gap.

Một model “accuracy tốt” nhưng không đạt latency/cost/reliability requirement vẫn là production system không đạt contract. Một accelerator utilization cao cũng chưa chứng minh hệ thống hiệu quả nếu useful-token throughput thấp hoặc queue/tail latency vượt SLO.