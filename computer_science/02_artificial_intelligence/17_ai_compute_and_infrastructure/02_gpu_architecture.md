# Kiến trúc GPU cho AI

Để hiểu vì sao neural network chạy nhanh hay chậm trên GPU, cần một mô hình tư duy về cách GPU tổ chức compute và memory. Không cần trở thành CUDA expert, nhưng các khái niệm như thread group, warp hoặc wavefront, SM, register, shared memory và HBM giúp giải thích behavior về hiệu năng.

## Streaming Multiprocessor

GPU gồm nhiều **Streaming Multiprocessor (SM)** hoặc đơn vị tương đương. Mỗi SM chứa execution unit, register, scheduling resource và shared memory/cache.

Khi kernel được launch, rất nhiều thread được tạo ra. Scheduler phân phối các thread block lên các SM.

## Thread, Block và Grid

Phân cấp khái niệm:

```text
Grid
└── Block
    └── Thread
```

Các thread trong cùng block có thể phối hợp qua shared memory và synchronization.

Người dùng framework thường không viết kernel trực tiếp, nhưng optimized library vẫn ánh xạ tensor operation xuống cấu trúc này.

## Warp

GPU thực thi thread theo các nhóm kích thước cố định thường gọi là **warp**; terminology có thể khác giữa vendor. Các thread trong cùng warp thường thực thi cùng instruction.

Nếu xảy ra **branch divergence**:

```text
if condition A:
  một nửa thread đi path 1
else:
  một nửa thread đi path 2
```

hardware phải tuần tự hóa một phần các path, làm giảm efficiency.

## Occupancy

Occupancy mô tả số warp hoạt động so với capacity phần cứng. Occupancy thấp có thể do:

- dùng quá nhiều register;
- shared memory trên mỗi block quá lớn;
- block shape không phù hợp.

Nhưng occupancy 100% không tự động nghĩa nhanh nhất; balance giữa memory và compute vẫn quan trọng.

## Register

Register là vùng lưu trữ rất nhanh theo từng thread. Nếu kernel cần quá nhiều register, số thread hoạt động đồng thời có thể giảm hoặc một phần dữ liệu phải spill sang memory chậm hơn.

Compiler và kernel design cố giữ các giá trị được dùng thường xuyên gần compute nhất có thể.

## Shared Memory

Shared memory là vùng nhớ nhỏ trên chip mà các thread trong cùng block có thể truy cập. Nó thường được dùng để tile matrix operation và reuse dữ liệu, qua đó giảm traffic tới global memory.

## Global Memory và HBM

VRAM hoặc HBM có capacity lớn hơn nhưng access chậm hơn on-chip storage. AI performance thường phụ thuộc khả năng tận dụng memory access tuần tự/coalesced và reuse dữ liệu.

## Coalesced Access

Nếu các thread lân cận truy cập địa chỉ memory gần nhau, hardware có thể gộp transaction hiệu quả. Random hoặc scattered access làm lãng phí bandwidth.

Dense tensor workload thường được layout hoặc block để tăng locality.

## Tensor Core

Các matrix unit chuyên dụng có thể thực hiện multiply-accumulate trên những tile nhỏ với throughput cao. Library ghép các tile đó thành GEMM lớn.

Việc dimension có căn chỉnh phù hợp hay không có thể ảnh hưởng kernel efficiency, đặc biệt ở low precision.

## GEMM là Kernel trung tâm

Transformer và MLP chứa rất nhiều phép toán:

\[
C=AB
\]

**General Matrix Multiply (GEMM)** là một trong những kernel được tối ưu mạnh nhất.

Attention còn có softmax, masking và nhiều pattern nhạy memory; fused kernel giúp giảm số lần read/write intermediate tensor.

## Kernel Fusion

Thực thi ngây thơ:

```text
op1 → ghi HBM
op2 → đọc HBM → ghi HBM
op3 → đọc HBM
```

Fused kernel giữ intermediate gần compute hơn:

```text
op1 + op2 + op3 → ít chuyến đi tới memory hơn
```

Fusion thường cải thiện latency và sử dụng bandwidth.

## Launch Overhead

Nhiều kernel rất nhỏ có thể bị launch overhead chi phối. Graph capture, fusion hoặc compiler optimization giúp giảm idle gap giữa các kernel.

Small-batch inference thường bị overhead ảnh hưởng nhiều hơn large-batch training.

## Synchronization

GPU parallelism hiệu quả nhất khi nhiều task độc lập. Global synchronization buộc thread hoặc device chờ nhau và tạo idle time.

Distributed training còn thêm collective synchronization giữa nhiều GPU.

## Profiler Timeline

Timeline từ profiler có thể cho thấy:

```text
CPU launch
GPU kernel
memcpy
communication
idle gap
```

Optimization nên tập trung vào thành phần chiếm wall-clock time lớn nhất.

## Memory-Bound và Compute-Bound

GEMM lớn thường thiên về compute. Elementwise operation có arithmetic intensity thấp và thường memory-bound.

Fusing elementwise operation có thể đem lại lợi ích lớn dù FLOP count nhỏ.

## Trực giác về Attention Kernel

Naive attention materialize score matrix `QK^T`, làm memory cost tăng mạnh theo sequence length. Memory-efficient attention algorithm chia computation thành tile để tránh materialize toàn bộ matrix trong HBM.

Toán học không đổi, nhưng execution schedule thay đổi.

## Dynamic Shape

Sequence length biến đổi làm kernel specialization và batching khó hơn. Padding, bucketing và compilation strategy ảnh hưởng utilization.

## GPU Memory Fragmentation

Allocator quản lý nhiều block kích thước khác nhau có thể gây fragmentation. Paged-memory strategy đặc biệt hữu ích cho KV cache có sequence length biến động.

## Multi-GPU Topology

Bandwidth giữa các GPU khác nhau tùy chúng nằm cùng node, có direct interconnect hay phải đi qua path chậm hơn. Placement và sharding cần nhận thức topology.

## Mô hình tư duy

```text
GPU code nhanh = đủ parallel work + data reuse cao + memory access hiệu quả + ít khoảng chờ đồng bộ
```

## Những nhầm lẫn thường gặp

### “GPU có nhiều core nên mọi parallel code đều nhanh”

Không. Irregular control flow hoặc memory access có thể không phù hợp với GPU.

### “100% utilization nghĩa kernel đã tối ưu”

Không. Device có thể đang bận nhưng bị memory stall hoặc chạy kernel kém hiệu quả.

### “Framework che hardware nên không cần hiểu GPU”

Không hoàn toàn. Khi model lớn hoặc latency/cost quan trọng, hardware intuition giúp chọn batch, precision, tensor shape và architecture tốt hơn.

## Liên kết kiến thức

Xem [Memory & Bandwidth](./03_memory_and_bandwidth.md), [Parallel Computing](./04_parallel_computing.md), [Quantization](../15_ai_engineering/06_quantization.md) và [Transformer](../06_deep_learning_architectures/05_transformer.md).