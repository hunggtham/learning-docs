# Memory Hierarchy và Bandwidth trong AI

AI workload xử lý tensor rất lớn. Trong nhiều trường hợp performance không bị giới hạn bởi số phép tính mà bởi việc **đưa dữ liệu tới compute unit nhanh đến đâu**. Vì vậy memory capacity, hierarchy và bandwidth là phần cốt lõi của AI infrastructure.

## Memory Hierarchy

Một hệ thống có nhiều tầng memory:

```text
register
→ on-chip cache / shared memory
→ HBM / VRAM
→ host RAM
→ NVMe / local storage
→ network / object storage
```

Tầng gần compute nhanh hơn nhưng nhỏ hơn và đắt hơn. Tối ưu hiệu năng cố giữ dữ liệu nóng (hot data) ở tầng gần nhất có thể.

## Capacity, Bandwidth và Latency

Ba khái niệm khác nhau:

```text
capacity  = chứa được bao nhiêu dữ liệu
bandwidth = truyền được bao nhiêu dữ liệu mỗi giây
latency   = phải chờ bao lâu cho một lần truy cập
```

GPU có thể đủ VRAM để fit model nhưng vẫn bị bandwidth bottleneck.

## Weight Memory

Với mô hình có `N` parameter, dung lượng xấp xỉ:

```text
FP32 ≈ 4N byte
FP16 ≈ 2N byte
INT8 ≈ 1N byte
INT4 ≈ 0.5N byte
```

Nhưng inference còn buffer, activation và KV cache; training còn gradient và optimizer state.

## Activation Memory

Training cần lưu intermediate activation cho backpropagation.

Activation memory thường tăng theo:

```text
batch size × sequence length × hidden size × layers
```

**Gradient checkpointing** giảm memory bằng cách không lưu toàn bộ activation mà recompute một phần trong backward pass.

Trade-off:

```text
ít memory hơn ↔ nhiều compute hơn
```

## Optimizer State Memory

Adam thường lưu first moment và second moment cho mỗi parameter. Nếu state ở FP32, optimizer memory có thể lớn hơn weight memory nhiều lần.

Optimizer sharding hoặc lower-precision state giúp giảm footprint.

## KV Cache

Autoregressive Transformer cần lưu Key/Value của các token trước cho mỗi layer.

KV cache size xấp xỉ tỉ lệ với:

\[
Layers\times SequenceLength\times KVHeads\times HeadDim\times Precision\times Batch
\]

Vì vậy long context và high concurrency có thể tiêu thụ memory nhanh hơn weights.

## Multi-Query và Grouped-Query Attention

Giảm số K/V head giúp giảm KV cache và memory bandwidth trong inference.

Đây là ví dụ một thay đổi architecture xuất phát trực tiếp từ constraint hardware/runtime.

## Memory Bandwidth

Nếu mỗi token decode phải đọc một phần lớn model weights, throughput có thể bị giới hạn bởi HBM bandwidth.

Quantization giảm số byte cần đọc nên có thể tăng decode throughput ngay cả khi FLOP count gần như không đổi.

## Arithmetic Intensity

\[
AI=\frac{Operations}{Bytes\ moved}
\]

Arithmetic intensity thấp → thường memory-bound.

Arithmetic intensity cao → thường compute-bound.

## Roofline Model

Performance ceiling xấp xỉ:

```text
min(peak compute,
    memory bandwidth × arithmetic intensity)
```

Roofline giúp suy luận xem nên tối ưu compute hay memory traffic.

## Data Reuse

Matrix multiplication hiệu quả vì cùng tile dữ liệu được reuse cho nhiều multiply-accumulate operation.

Tiling giữ submatrix trong on-chip memory để dùng lại trước khi phải fetch dữ liệu mới từ HBM.

## Cache Locality

Sequential hoặc coalesced access tận dụng cache và burst tốt hơn random access.

Embedding lookup có irregular memory access nên behavior khác dense GEMM.

## Truyền dữ liệu giữa CPU RAM và GPU VRAM

PCIe hoặc interconnect có bandwidth hữu hạn. Nếu mỗi request liên tục copy input lớn hoặc model từ host sang GPU, GPU có thể idle để chờ dữ liệu.

Pinning, prefetch và async transfer giúp overlap compute với data transfer.

## Offloading

Khi model không fit GPU memory, có thể offload weights, optimizer state hoặc activation sang CPU hoặc NVMe.

Offloading tăng effective capacity nhưng làm latency cao hơn vì đường truyền chậm hơn.

Phù hợp khi memory capacity là hard constraint và workload chấp nhận overhead.

## Unified Memory

Unified virtual memory giúp lập trình đơn giản hơn, nhưng page migration vẫn có cost. “Unified” không nghĩa mọi memory access có hiệu năng giống nhau.

## Memory Fragmentation

Allocation có kích thước thay đổi tạo các khoảng trống trong memory. LLM serving với nhiều sequence length rất dễ gặp fragmentation.

Paged hoặc block KV cache dùng block kích thước cố định để reuse memory hiệu quả hơn.

## Distributed Memory

Khi model được shard qua nhiều GPU, mỗi device giữ một phần weights hoặc activation. Khi đó communication trở thành một phần của effective memory access path.

Tensor parallelism thường trao đổi partial activation ở mỗi layer, vì vậy interconnect bandwidth cực kỳ quan trọng.

## Storage I/O

Large checkpoint có thể mất nhiều phút để load nếu storage hoặc network chậm. Distributed training cần parallel checkpointing và serialization hiệu quả.

Tần suất checkpoint có trade-off:

```text
thường xuyên hơn → ít mất công khi failure
                 nhưng I/O overhead lớn hơn
```

## Economics của Long Context

Context length tăng không chỉ làm attention compute tăng mà còn làm KV cache lớn hơn. Serving 100 user với context dài có thể memory-bound dù model weights vẫn fit dễ dàng.

## Precision và Memory

BF16/FP16 giảm một nửa số byte của weight hoặc activation so với FP32. INT8 và INT4 giảm thêm nữa.

Tuy nhiên conversion, scale metadata và kernel không được hỗ trợ có thể làm giảm benefit kỳ vọng.

## Batch Sizing có nhận thức về Memory

Maximum batch không phải mục tiêu cuối. Cần chọn batch cân bằng:

- memory headroom;
- throughput;
- tail latency;
- OOM risk.

Dynamic workload cần chừa margin thay vì lấp đầy 100% VRAM.

## OOM Failure

Out-of-memory thường xảy ra vì peak allocation chứ không phải average allocation. Cần profile peak memory ở worst-case sequence length và batch size.

## Memory Leak và Caching

Long-running serving runtime có allocator và cache nên RSS hoặc VRAM có thể giữ high watermark. Không nên nhầm allocator caching với memory leak thật; cần inspect allocation behavior.

## Mô hình tư duy

```text
Compute hỏi: cần bao nhiêu phép toán?
Memory hỏi: dữ liệu ở đâu, phải di chuyển bao nhiêu byte và có thể reuse bao nhiêu lần?
```

Trong AI hiện đại, **data movement cũng là một phần lớn của computation cost**.

## Những nhầm lẫn thường gặp

### “Model fit VRAM nghĩa là serving ổn”

Không. KV cache, activation và concurrency còn cần thêm memory.

### “Nhiều VRAM hơn nghĩa là nhanh hơn”

Không. Capacity và bandwidth là hai đại lượng khác nhau.

### “Unified memory loại bỏ transfer bottleneck”

Không. Physical data movement vẫn tồn tại.

## Liên kết kiến thức

Xem [GPU Architecture](./02_gpu_architecture.md), [Parallel Computing](./04_parallel_computing.md), [Quantization](../15_ai_engineering/06_quantization.md), [Caching/Batching](../15_ai_engineering/05_caching_and_batching.md).