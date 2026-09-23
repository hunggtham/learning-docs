# Transformer internals, attention, KV cache và inference cost

Transformer quan trọng không chỉ vì model quality mà vì computation graph ánh xạ tốt lên parallel hardware trong training. Autoregressive inference lại có cost profile rất khác: prompt được xử lý theo batch lớn hơn, còn decode phải sinh token nối tiếp và liên tục đọc model state/KV state.

Mental model của chương này là: **AI inference serving là một memory-and-scheduling system có model semantics ở trên**. Correctness cần request nào dùng đúng model/KV state; performance phụ thuộc arithmetic intensity, memory bandwidth, batching, queueing, fragmentation và scheduler policy.

## 1. Bài toán ban đầu: model math không tự nói serving behavior

Cùng model weights có thể cho throughput/latency rất khác tùy:

```text
prompt/context length
output length
concurrent sequences
batching policy
precision/quantization
KV-cache layout
accelerator memory capacity/bandwidth
interconnect
tensor/model parallelism
```

Vì vậy “model có N parameters” không đủ để capacity plan. Cần map workload distribution vào resource consumption theo serving phase.

## 2. Transformer block và state flow

Input tokens được ánh xạ thành vectors. Một transformer block điển hình có attention, feed-forward network, residual paths và normalization.

Attention cho mỗi position tổng hợp information từ positions khác. Nhưng serving system quan tâm thêm:

```text
weights: mostly read-only model state
activations: temporary computation state
KV cache: per-sequence persistent decode state
scheduler metadata: ownership/lifetime of each sequence
```

Tách các state classes này giúp hiểu memory pressure.

## 3. Query, Key, Value và attention invariant

Mỗi token representation được project thành Q, K, V. Query của position hiện tại so với keys tạo scores/weights; weighted values tạo attention output.

Multi-head attention dùng nhiều projections/subspaces. Kiến trúc không hứa một head luôn map tới một human-interpretable concept cụ thể.

Correctness ở serving layer cần giữ **sequence association**: K/V của request A không được nhầm với request B, và positions/order phải map đúng logical prefix của sequence.

## 4. Full self-attention có quadratic interaction theo sequence length

Với sequence length `n`, full attention biểu diễn interactions giữa nhiều pairs positions, tạo component `n × n` trong naïve formulation.

Optimized kernels như tiled/flash-style attention có thể tránh materialize toàn matrix và giảm HBM traffic nhờ tiling/fusion, nhưng không thay mathematical dependency của exact full attention.

Đây là pattern performance quan trọng:

> Cùng algorithmic semantics, data movement strategy có thể thay dominant bottleneck.

## 5. Prefill và decode là hai execution phases khác nhau

**Prefill** xử lý toàn prompt/context mới. Nhiều tokens có thể được tính song song nên accelerator có cơ hội đạt high compute utilization.

**Decode** sinh token từng bước. Token `t+1` phụ thuộc state/result trước, nên một sequence có ít parallelism theo time dimension.

Metrics cần tách:

```text
TTFT — time to first token
prefill throughput
inter-token latency / time per output token
decode throughput
end-to-end request latency
```

Average tokens/s có thể che UX xấu nếu queue/TTFT cao.

## 6. KV cache đổi recomputation lấy memory

Nếu decode mỗi bước tính lại K/V cho toàn prefix, work lặp rất lớn. **KV cache** giữ K/V của prior tokens cho mỗi layer để token mới reuse.

Trade-off:

```text
recompute ↓
↔
per-sequence persistent memory ↑
```

KV memory tăng với context length, active sequences, layers và KV dimensions/precision. Context “được hỗ trợ” không đồng nghĩa có thể phục vụ nhiều long-context requests đồng thời.

## 7. KV cache có ownership/lifetime invariant

Serving scheduler có thể batch, preempt, swap hoặc free sequence state. Invariant là:

> KV blocks chỉ được reuse sau khi sequence sở hữu chúng thật sự kết thúc/evict theo protocol; page table/block mapping của sequence phải trỏ đúng logical token positions.

Một bug allocator/scheduler có thể tạo corruption cross-request dù model math hoàn hảo. Đây là connection trực tiếp giữa AI serving và OS-style memory management.

## 8. Paged KV cache giảm fragmentation bằng indirection

Nếu mỗi sequence cần một contiguous buffer theo maximum context, memory waste lớn và resizing khó. Paged/block-based KV quản cache theo chunks và dùng mapping logical token range → physical block.

Lợi ích:

```text
less external fragmentation
share/reuse blocks easier when semantics allow
allocate incrementally with sequence growth
```

Đổi lại có metadata/indirection cost và allocator pressure. “Paged” không miễn phí; nó chuyển memory-contiguity problem thành mapping/lifetime problem.

## 9. Decode thường memory-bandwidth-bound

Mỗi decode step của một sequence cần đọc lượng lớn weights và KV state để tạo tương đối ít new output. Arithmetic intensity có thể thấp hơn prefill, làm HBM/memory bandwidth dominate.

Roofline-style reasoning hữu ích:

```text
compute demand / bytes moved thấp
→ bandwidth-bound

batching increases reuse/amortization
→ arithmetic intensity/utilization improve
```

Đây là lý do theoretical FLOPS cao không tự bảo đảm low token latency.

## 10. Batching đổi latency lấy throughput

Batch nhiều sequences giúp amortize weight reads và tăng accelerator utilization. Nhưng scheduler có thể giữ request chờ để tạo batch lớn hơn.

Trade-off:

```text
larger batch
→ throughput ↑ đến một mức
→ queue + per-step latency/memory ↑
```

Continuous batching chèn/rút sequences động để tận dụng slots tốt hơn fixed batch, nhưng tạo scheduling complexity: sequences có lengths khác nhau, finish khác nhau và memory footprint thay đổi mỗi decode step.

## 11. Scheduler là admission controller cho GPU memory + compute

Một request long-context có thể tiêu KV memory gấp nhiều lần request ngắn. Nếu scheduler admit chỉ theo request count, một vài long requests có thể OOM hoặc làm concurrency collapse.

Useful admission cost model cần consider:

```text
prompt tokens
max/expected output tokens
KV bytes per token
batch/parallelism mode
current free blocks
latency class / priority / tenant quota
```

Đây là weighted admission, giống general software systems nhưng resource unit là tokens/KV/GPU capacity.

## 12. Head-of-line blocking có thể xuất hiện trong batch

Nếu batch policy ép requests cùng bước theo slowest/longest member, một long sequence có thể làm short requests chờ. Continuous scheduling giảm một số form nhưng không xóa all interference.

Multi-tenant serving cần fairness: throughput tối đa toàn GPU có thể conflict với p99 SLO của interactive requests.

Separate pools/classes hoặc weighted scheduling có thể cần khi workloads khác mạnh.

## 13. Context length làm giảm effective capacity theo nhiều chiều

Context dài:

```text
KV memory ↑
attention work ↑
prefill compute ↑
possible batch size ↓
number of concurrent sequences fit in memory ↓
```

Capacity planning phải dùng **distribution** context/output length, không chỉ maximum context advertised.

Một p99 100k-token workload khác hoàn toàn workload median 1k dù cùng model/context limit.

## 14. Quantization giảm bytes nhưng tạo accuracy/kernel trade-off

Giảm precision weights/activations/KV có thể giảm footprint/bandwidth và tăng throughput nếu hardware/kernel path hỗ trợ tốt.

Nhưng:

```text
quality/calibration can change
conversion/dequant cost exists
unsupported kernel may be slower
some tensors are more sensitive than others
```

“4-bit” không tự động nhanh hoặc đủ quality. Phải benchmark end-to-end workload + quality metrics.

## 15. Tensor/model parallelism đổi local memory problem thành communication problem

Nếu model không fit một device hoặc muốn tăng compute capacity, weights/operations có thể shard qua accelerators.

Mỗi layer có thể cần collective communication. Decode latency lúc đó gồm:

```text
kernel compute
+
interconnect collective
+
synchronization/skew
```

Thêm GPU có thể chậm hơn nếu per-step work nhỏ nhưng communication dominates. Topology/locality trở thành lower abstraction quyết định behavior.

## 16. Prefix reuse/cache chỉ đúng khi semantic identity đúng

Nếu serving system reuse KV cho common prefix, key phải bind đúng model version, tokenizer, prompt bytes/tokens, positional semantics và any adapter/context affecting computation.

Cache hit với wrong semantic key là correctness bug, không phải stale-performance issue.

Đây là same family với cache invalidation: reuse chỉ an toàn khi identity/invalidation contract đúng.

## 17. Model rollout phải version cả serving state

Nếu model weights/config/adapters đổi, existing KV cache được tạo từ version cũ thường không thể tùy ý reuse với version mới.

Deployment cần boundary:

```text
request pinned to model version
KV state belongs to same version
new requests route gradually
old in-flight requests drain or migrate only if explicitly supported
```

Canary model serving vì vậy là protocol/state rollout, không chỉ load new file.

## 18. OOM không phải failure duy nhất của memory pressure

Trước OOM, allocator fragmentation, KV eviction/swap, lower batch size và queue growth có thể làm p99 xấu.

Phase model:

```text
ample memory → batch efficiently
near capacity → fragmentation/admission tighter
pressure → preemption/eviction/swap/recompute
overload → queue/timeout/retry/OOM
```

Monitor free memory alone không đủ; cần block fragmentation, active tokens/sequences và queue age.

## 19. Retry inference có thể gây duplicate expensive work

Client timeout không chứng minh generation đã dừng. Retry long prompt có thể chạy prefill lần nữa và consume expensive GPU time.

If streaming response, partial output complicates semantics further. Serving gateway cần deadline/cancellation propagation và retry budget; deterministic bad request không nên retry như transient transport failure.

AI serving obey same retry→overload feedback loop as other distributed systems, nhưng work unit đắt hơn nhiều.

## 20. Production evidence

Evidence nên tách scheduler/model/hardware:

```text
Workload:
- prompt/output length distributions
- active sequences/tokens
- tenant/priority mix

Scheduler:
- queue wait / TTFT
- batch size over time
- admitted/rejected/preempted requests
- KV blocks used/free/fragmentation

Model phases:
- prefill latency/throughput
- decode token latency/throughput

Hardware:
- accelerator utilization
- HBM bandwidth/memory occupancy
- interconnect collective time
- kernel occupancy/stalls where tooling supports

Reliability:
- OOM/retry/cancellation/late completion
- model-version/KV ownership
```

Một GPU-utilization 100% graph không nói throughput useful hay queue health.

## 21. Performance experiment phải giữ quality + workload semantics

Optimization inference không chỉ “tokens/s cao hơn”. Compare phải giữ:

```text
same model/task or documented model change
same quality/evaluation threshold
same context/output distribution
same TTFT/token-latency SLO
same concurrency/tenant mix
```

Nếu quantization tăng throughput nhưng quality vượt error budget, optimization không đạt business invariant.

## 22. Abstraction nào thực sự quyết định behavior?

Nếu TTFT cao nhưng decode nhanh, look queue/prefill. Nếu token latency cao ở large batch, inspect bandwidth/interconnect/scheduler. Nếu OOM dưới long context, KV capacity/admission quyết định. Nếu one tenant hurts all, fairness is missing. Nếu same model different hardware behaves oddly, data movement/kernel support may dominate theoretical FLOPS.

## 23. Mô hình tư duy

> Transformer inference là interaction giữa **model dependency graph, per-sequence KV state, scheduler và memory hierarchy**. KV cache đổi recomputation lấy persistent memory; batching đổi latency lấy throughput; quantization đổi precision/quality lấy bytes; parallelism đổi local compute lấy communication. **Serving correctness cần giữ request/model/KV ownership; serving performance cần quản queue, memory bandwidth và admission như một systems problem.**

## Kết nối

Ôn [AI neural/transformer foundation](../../basic/10_ai_foundations/03_neural_networks_and_representation_learning.md), đọc [training/inference lifecycle](./00_training_inference_systems_and_model_lifecycle.md), [distributed training](./02_distributed_training_data_model_and_pipeline_parallelism.md), [GPU execution model](../../02_computer_architecture/advanced/06_simd_vector_isa_and_gpu_execution_model.md), [queueing/backpressure](../../08_software_systems/advanced/00_queueing_tail_latency_and_backpressure.md) và specialized AI library tại [`../../02_artificial_intelligence/`](../../02_artificial_intelligence/README.md).
