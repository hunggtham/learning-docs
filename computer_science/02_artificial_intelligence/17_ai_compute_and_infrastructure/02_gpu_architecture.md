# Kiến trúc GPU cho AI

> **Mạch đọc:** Đặt **Kiến trúc GPU cho AI** trong bản đồ [README](./README.md) để thấy đơn vị sở hữu (owner / 오너) và vị trí của nó. Nội dung đi từ **Streaming Multiprocessor** sang **luồng thực thi (thread / 스레드), khối (block / 블록) và Grid**; điểm nối này chuẩn bị câu hỏi cho các mục sau thay vì dừng ở định nghĩa đầu tiên.


Để hiểu vì sao neural mạng (network / 네트워크) chạy nhanh hay chậm trên GPU, cần một mô hình tư duy về cách GPU tổ chức compute và bộ nhớ (memory / 메모리). Không cần trở thành CUDA expert, nhưng các khái niệm như luồng thực thi (thread / 스레드) group, warp hoặc wavefront, SM, register, dùng chung (shared / 공유) bộ nhớ (memory / 메모리) và HBM giúp giải thích hành vi (behavior / 동작) về hiệu năng.

## Streaming Multiprocessor

GPU gồm nhiều **Streaming Multiprocessor (SM)** hoặc đơn vị tương đương. Mỗi SM chứa đơn vị thực thi (execution unit / 실행 유닛), register, scheduling tài nguyên (resource / 자원) và dùng chung (shared / 공유) bộ nhớ (memory / 메모리)/bộ nhớ đệm (cache / 캐시).

Khi kernel được launch, rất nhiều luồng thực thi (thread / 스레드) được tạo ra. Scheduler phân phối các luồng thực thi (thread / 스레드) khối (block / 블록) lên các SM.

## Luồng thực thi (thread / 스레드), khối (block / 블록) và Grid

Phân cấp khái niệm:

```text
Grid
└── Block
    └── Thread
```

Các luồng thực thi (thread / 스레드) trong cùng khối (block / 블록) có thể phối hợp qua dùng chung (shared / 공유) bộ nhớ (memory / 메모리) và synchronization.

Người dùng khung phần mềm (framework / 프레임워크) thường không viết kernel trực tiếp, nhưng optimized thư viện (library / 라이브러리) vẫn ánh xạ tensor thao tác (operation / 연산) xuống cấu trúc này.

## Warp

GPU thực thi luồng thực thi (thread / 스레드) theo các nhóm kích thước cố định thường gọi là **warp**; terminology có thể khác giữa vendor. Các luồng thực thi (thread / 스레드) trong cùng warp thường thực thi cùng instruction.

Nếu xảy ra **branch divergence**:

```text
if condition A:
  một nửa thread đi path 1
else:
  một nửa thread đi path 2
```

hardware phải tuần tự hóa một phần các đường dẫn (path / 경로), làm giảm efficiency.

## Occupancy

Occupancy mô tả số warp hoạt động so với sức chứa (capacity / 용량) phần cứng. Occupancy thấp có thể do:

- dùng quá nhiều register;
- dùng chung (shared / 공유) bộ nhớ (memory / 메모리) trên mỗi khối (block / 블록) quá lớn;
- khối (block / 블록) shape không phù hợp.

Nhưng occupancy 100% không tự động nghĩa nhanh nhất; balance giữa bộ nhớ (memory / 메모리) và compute vẫn quan trọng.

## Register

Register là vùng lưu trữ rất nhanh theo từng luồng thực thi (thread / 스레드). Nếu kernel cần quá nhiều register, số luồng thực thi (thread / 스레드) hoạt động đồng thời có thể giảm hoặc một phần dữ liệu phải spill sang bộ nhớ (memory / 메모리) chậm hơn.

Trình biên dịch (compiler / 컴파일러) và kernel thiết kế (design / 설계) cố giữ các giá trị được dùng thường xuyên gần compute nhất có thể.

## Dùng chung (shared / 공유) bộ nhớ (memory / 메모리)

Dùng chung (shared / 공유) bộ nhớ (memory / 메모리) là vùng nhớ nhỏ trên chip mà các luồng thực thi (thread / 스레드) trong cùng khối (block / 블록) có thể truy cập. Nó thường được dùng để tile ma trận (matrix / 행렬) thao tác (operation / 연산) và reuse dữ liệu, qua đó giảm traffic tới toàn cục (global / 전역) bộ nhớ (memory / 메모리).

## Toàn cục (global / 전역) bộ nhớ (memory / 메모리) và HBM

VRAM hoặc HBM có sức chứa (capacity / 용량) lớn hơn nhưng truy cập (access / 접근) chậm hơn on-chip lưu trữ (storage / 저장소). AI hiệu năng (performance / 성능) thường phụ thuộc khả năng tận dụng bộ nhớ (memory / 메모리) truy cập (access / 접근) tuần tự/coalesced và reuse dữ liệu.

## Coalesced truy cập (access / 접근)

Nếu các luồng thực thi (thread / 스레드) lân cận truy cập địa chỉ bộ nhớ (memory / 메모리) gần nhau, hardware có thể gộp giao dịch (transaction / 트랜잭션) hiệu quả. Random hoặc scattered truy cập (access / 접근) làm lãng phí bandwidth.

Dense tensor tải công việc (workload / 워크로드) thường được bố cục (layout / 레이아웃) hoặc khối (block / 블록) để tăng locality.

## Tensor cốt lõi (core / 핵심)

Các ma trận (matrix / 행렬) đơn vị (unit / 단위) chuyên dụng có thể thực hiện multiply-accumulate trên những tile nhỏ với thông lượng (throughput / 처리량) cao. thư viện (library / 라이브러리) ghép các tile đó thành GEMM lớn.

Việc dimension có căn chỉnh phù hợp hay không có thể ảnh hưởng kernel efficiency, đặc biệt ở low precision.

## GEMM là Kernel trung tâm

Transformer và MLP chứa rất nhiều phép toán:

\[
C=AB
\]

**General ma trận (matrix / 행렬) Multiply (GEMM)** là một trong những kernel được tối ưu mạnh nhất.

Attention còn có softmax, masking và nhiều mẫu (pattern / 패턴) nhạy bộ nhớ (memory / 메모리); fused kernel giúp giảm số lần read/ghi (write / 쓰기) intermediate tensor.

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

Fusion thường cải thiện độ trễ (latency / 지연 시간) và sử dụng bandwidth.

## Launch Overhead

Nhiều kernel rất nhỏ có thể bị launch overhead chi phối. đồ thị (graph / 그래프) capture, fusion hoặc trình biên dịch (compiler / 컴파일러) tối ưu hóa (optimization / 최적화) giúp giảm idle gap giữa các kernel.

Small-batch suy luận (inference / 추론) thường bị overhead ảnh hưởng nhiều hơn large-batch huấn luyện (training / 학습).

## Synchronization

GPU parallelism hiệu quả nhất khi nhiều tác vụ (task / 작업) độc lập. toàn cục (global / 전역) synchronization buộc luồng thực thi (thread / 스레드) hoặc thiết bị (device / 장치) chờ nhau và tạo idle thời gian (time / 시간).

Phân tán (distributed / 분산) huấn luyện (training / 학습) còn thêm collective synchronization giữa nhiều GPU.

## Profiler Timeline

Timeline từ profiler có thể cho thấy:

```text
CPU launch
GPU kernel
memcpy
communication
idle gap
```

Tối ưu hóa (optimization / 최적화) nên tập trung vào thành phần chiếm wall-clock thời gian (time / 시간) lớn nhất.

## Memory-Bound và Compute-Bound

GEMM lớn thường thiên về compute. Elementwise thao tác (operation / 연산) có arithmetic intensity thấp và thường memory-bound.

Fusing elementwise thao tác (operation / 연산) có thể đem lại lợi ích lớn dù FLOP count nhỏ.

## Trực giác về Attention Kernel

Naive attention materialize score ma trận (matrix / 행렬) `QK^T`, làm bộ nhớ (memory / 메모리) chi phí (cost / 비용) tăng mạnh theo chuỗi (sequence / 시퀀스) length. Memory-efficient attention thuật toán (algorithm / 알고리즘) chia computation thành tile để tránh materialize toàn bộ ma trận (matrix / 행렬) trong HBM.

Toán học không đổi, nhưng thực thi (execution / 실행) schedule thay đổi.

## Động (dynamic / 동적) Shape

Chuỗi (sequence / 시퀀스) length biến đổi làm kernel specialization và batching khó hơn. Padding, bucketing và compilation chiến lược (strategy / 전략) ảnh hưởng utilization.

## GPU bộ nhớ (memory / 메모리) Fragmentation

Allocator quản lý nhiều khối (block / 블록) kích thước khác nhau có thể gây fragmentation. Paged-memory chiến lược (strategy / 전략) đặc biệt hữu ích cho KV bộ nhớ đệm (cache / 캐시) có chuỗi (sequence / 시퀀스) length biến động.

## Multi-GPU Topology

Bandwidth giữa các GPU khác nhau tùy chúng nằm cùng nút (node / 노드), có direct interconnect hay phải đi qua đường dẫn (path / 경로) chậm hơn. Placement và sharding cần nhận thức topology.

## Mô hình tư duy

Phần này chốt mental model thành một chuỗi có thể dùng lại: bối cảnh → cơ chế → quan sát → giới hạn → quyết định. Hãy đọc sơ đồ như công cụ suy luận, không như một khẩu hiệu tách khỏi chapter.

```text
GPU code nhanh = đủ parallel work + data reuse cao + memory access hiệu quả + ít khoảng chờ đồng bộ
```

## Những nhầm lẫn thường gặp

### “GPU có nhiều cốt lõi (core / 핵심) nên mọi parallel mã (code / 코드) đều nhanh”

Không. Irregular điều khiển (control / 제어) luồng (flow / 흐름) hoặc bộ nhớ (memory / 메모리) truy cập (access / 접근) có thể không phù hợp với GPU.

### “100% utilization nghĩa kernel đã tối ưu”

Không. thiết bị (device / 장치) có thể đang bận nhưng bị bộ nhớ (memory / 메모리) stall hoặc chạy kernel kém hiệu quả.

### “khung phần mềm (framework / 프레임워크) che hardware nên không cần hiểu GPU”

Không hoàn toàn. Khi mô hình (model / 모델) lớn hoặc độ trễ (latency / 지연 시간)/chi phí (cost / 비용) quan trọng, hardware intuition giúp chọn batch, precision, tensor shape và kiến trúc (architecture / 아키텍처) tốt hơn.

## Liên kết kiến thức

Xem [Memory & Bandwidth](./03_memory_and_bandwidth.md), [Parallel Computing](./04_parallel_computing.md), [Quantization](../15_ai_engineering/06_quantization.md) và [Transformer](../06_deep_learning_architectures/05_transformer.md).
