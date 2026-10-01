# Kiến trúc GPU cho AI

> **Mạch đọc:** [README](./README.md) là bản đồ owner của **Kiến trúc GPU cho AI**; nhìn vào vị trí đó trước để biết file này đang phục vụ nhánh kiến thức nào. **Streaming Multiprocessor** cho thấy đối tượng vận hành qua những bước nào và tạo ra hệ quả gì; sau đó sang **Luồng thực thi (thread / 스레드), khối (block / 블록) và Grid** để mở rộng đối tượng sang phạm vi kế cận. Cách đi này giữ lại điểm tựa của section đầu và cho biết kết luận sẽ được dùng ở đâu, thay vì dừng ở định nghĩa đầu tiên.

Để hiểu vì sao neural mạng (network / 네트워크) chạy nhanh hay chậm trên GPU, cần một mô hình tư duy về cách GPU tổ chức compute và bộ nhớ (memory / 메모리). Không cần trở thành CUDA expert, nhưng các khái niệm như luồng thực thi (thread / 스레드) group, warp hoặc wavefront, SM, register, dùng chung (shared / 공유) bộ nhớ (memory / 메모리) và HBM giúp giải thích hành vi (behavior / 동작) về hiệu năng.

## Streaming Multiprocessor

GPU gồm nhiều **Streaming Multiprocessor (SM)** hoặc đơn vị tương đương. Mỗi SM chứa đơn vị thực thi (execution unit / 실행 유닛), register, scheduling tài nguyên (resource / 자원) và dùng chung (shared / 공유) bộ nhớ (memory / 메모리)/bộ nhớ đệm (cache / 캐시).

Khi kernel được launch, rất nhiều luồng thực thi (thread / 스레드) được tạo ra. Scheduler phân phối các luồng thực thi (thread / 스레드) khối (block / 블록) lên các SM.

> **Chuyển mạch:** Trong **Kiến trúc GPU cho AI**, **Streaming Multiprocessor** xác định đầu vào; **Luồng thực thi (thread / 스레드), khối (block / 블록) và Grid** giải thích bước vận hành tạo ra kết quả kế tiếp. Từ đây, **Warp** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Luồng thực thi (thread / 스레드), khối (block / 블록) và Grid

Phân cấp khái niệm:

```text
Grid
└── Block
    └── Thread
```

Các luồng thực thi (thread / 스레드) trong cùng khối (block / 블록) có thể phối hợp qua dùng chung (shared / 공유) bộ nhớ (memory / 메모리) và synchronization.

Người dùng khung phần mềm (framework / 프레임워크) thường không viết kernel trực tiếp, nhưng optimized thư viện (library / 라이브러리) vẫn ánh xạ tensor thao tác (operation / 연산) xuống cấu trúc này.

> **Chuyển mạch:** Ở chặng này của **Kiến trúc GPU cho AI**, **Warp** tiếp nhận điểm tựa từ **Luồng thực thi (thread / 스레드), khối (block / 블록) và Grid** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Occupancy** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

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

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Kiến trúc GPU cho AI**, **Occupancy** tiếp nhận điểm tựa từ **Warp** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Register** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Occupancy

Occupancy mô tả số warp hoạt động so với sức chứa (capacity / 용량) phần cứng. Occupancy thấp có thể do:

- dùng quá nhiều register;
- dùng chung (shared / 공유) bộ nhớ (memory / 메모리) trên mỗi khối (block / 블록) quá lớn;
- khối (block / 블록) shape không phù hợp.

Nhưng occupancy 100% không tự động nghĩa nhanh nhất; balance giữa bộ nhớ (memory / 메모리) và compute vẫn quan trọng.

> **Chuyển mạch:** Trong **Kiến trúc GPU cho AI**, **Register** tiếp nhận điểm tựa từ **Occupancy** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Dùng chung (shared / 공유) bộ nhớ (memory / 메모리)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Register

Register là vùng lưu trữ rất nhanh theo từng luồng thực thi (thread / 스레드). Nếu kernel cần quá nhiều register, số luồng thực thi (thread / 스레드) hoạt động đồng thời có thể giảm hoặc một phần dữ liệu phải spill sang bộ nhớ (memory / 메모리) chậm hơn.

Trình biên dịch (compiler / 컴파일러) và kernel thiết kế (design / 설계) cố giữ các giá trị được dùng thường xuyên gần compute nhất có thể.

> **Chuyển mạch:** Ở chặng này của **Kiến trúc GPU cho AI**, **Dùng chung (shared / 공유) bộ nhớ (memory / 메모리)** tiếp nhận điểm tựa từ **Register** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Toàn cục (global / 전역) bộ nhớ (memory / 메모리) và HBM** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Dùng chung (shared / 공유) bộ nhớ (memory / 메모리)

Dùng chung (shared / 공유) bộ nhớ (memory / 메모리) là vùng nhớ nhỏ trên chip mà các luồng thực thi (thread / 스레드) trong cùng khối (block / 블록) có thể truy cập. Nó thường được dùng để tile ma trận (matrix / 행렬) thao tác (operation / 연산) và reuse dữ liệu, qua đó giảm traffic tới toàn cục (global / 전역) bộ nhớ (memory / 메모리).

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Kiến trúc GPU cho AI**, **Toàn cục (global / 전역) bộ nhớ (memory / 메모리) và HBM** tiếp nhận điểm tựa từ **Dùng chung (shared / 공유) bộ nhớ (memory / 메모리)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Coalesced truy cập (access / 접근)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Toàn cục (global / 전역) bộ nhớ (memory / 메모리) và HBM

VRAM hoặc HBM có sức chứa (capacity / 용량) lớn hơn nhưng truy cập (access / 접근) chậm hơn on-chip lưu trữ (storage / 저장소). AI hiệu năng (performance / 성능) thường phụ thuộc khả năng tận dụng bộ nhớ (memory / 메모리) truy cập (access / 접근) tuần tự/coalesced và reuse dữ liệu.

> **Chuyển mạch:** Trong **Kiến trúc GPU cho AI**, **Coalesced truy cập (access / 접근)** tiếp nhận điểm tựa từ **Toàn cục (global / 전역) bộ nhớ (memory / 메모리) và HBM** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Tensor cốt lõi (core / 핵심)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Coalesced truy cập (access / 접근)

Nếu các luồng thực thi (thread / 스레드) lân cận truy cập địa chỉ bộ nhớ (memory / 메모리) gần nhau, hardware có thể gộp giao dịch (transaction / 트랜잭션) hiệu quả. Random hoặc scattered truy cập (access / 접근) làm lãng phí bandwidth.

Dense tensor tải công việc (workload / 워크로드) thường được bố cục (layout / 레이아웃) hoặc khối (block / 블록) để tăng locality.

> **Chuyển mạch:** Ở chặng này của **Kiến trúc GPU cho AI**, **Tensor cốt lõi (core / 핵심)** tiếp nhận điểm tựa từ **Coalesced truy cập (access / 접근)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **GEMM là Kernel trung tâm** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Tensor cốt lõi (core / 핵심)

Các ma trận (matrix / 행렬) đơn vị (unit / 단위) chuyên dụng có thể thực hiện multiply-accumulate trên những tile nhỏ với thông lượng (throughput / 처리량) cao. thư viện (library / 라이브러리) ghép các tile đó thành GEMM lớn.

Việc dimension có căn chỉnh phù hợp hay không có thể ảnh hưởng kernel efficiency, đặc biệt ở low precision.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Kiến trúc GPU cho AI**, **GEMM là Kernel trung tâm** tiếp nhận điểm tựa từ **Tensor cốt lõi (core / 핵심)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Kernel Fusion** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## GEMM là Kernel trung tâm

Transformer và MLP chứa rất nhiều phép toán:

\[
C=AB
\]

**General ma trận (matrix / 행렬) Multiply (GEMM)** là một trong những kernel được tối ưu mạnh nhất.

Attention còn có softmax, masking và nhiều mẫu (pattern / 패턴) nhạy bộ nhớ (memory / 메모리); fused kernel giúp giảm số lần read/ghi (write / 쓰기) intermediate tensor.

> **Chuyển mạch:** Trong **Kiến trúc GPU cho AI**, **Kernel Fusion** tiếp nhận điểm tựa từ **GEMM là Kernel trung tâm** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Launch Overhead** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

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

> **Chuyển mạch:** Ở chặng này của **Kiến trúc GPU cho AI**, **Launch Overhead** tiếp nhận điểm tựa từ **Kernel Fusion** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Synchronization** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Launch Overhead

Nhiều kernel rất nhỏ có thể bị launch overhead chi phối. đồ thị (graph / 그래프) capture, fusion hoặc trình biên dịch (compiler / 컴파일러) tối ưu hóa (optimization / 최적화) giúp giảm idle gap giữa các kernel.

Small-batch suy luận (inference / 추론) thường bị overhead ảnh hưởng nhiều hơn large-batch huấn luyện (training / 학습).

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Kiến trúc GPU cho AI**, **Synchronization** tiếp nhận điểm tựa từ **Launch Overhead** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Profiler Timeline** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Synchronization

GPU parallelism hiệu quả nhất khi nhiều tác vụ (task / 작업) độc lập. toàn cục (global / 전역) synchronization buộc luồng thực thi (thread / 스레드) hoặc thiết bị (device / 장치) chờ nhau và tạo idle thời gian (time / 시간).

Phân tán (distributed / 분산) huấn luyện (training / 학습) còn thêm collective synchronization giữa nhiều GPU.

> **Chuyển mạch:** Trong **Kiến trúc GPU cho AI**, **Profiler Timeline** tiếp nhận điểm tựa từ **Synchronization** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Memory-Bound và Compute-Bound** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

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

> **Chuyển mạch:** Ở chặng này của **Kiến trúc GPU cho AI**, **Memory-Bound và Compute-Bound** tiếp nhận điểm tựa từ **Profiler Timeline** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Trực giác về Attention Kernel** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Memory-Bound và Compute-Bound

GEMM lớn thường thiên về compute. Elementwise thao tác (operation / 연산) có arithmetic intensity thấp và thường memory-bound.

Fusing elementwise thao tác (operation / 연산) có thể đem lại lợi ích lớn dù FLOP count nhỏ.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Kiến trúc GPU cho AI**, **Trực giác về Attention Kernel** tiếp nhận điểm tựa từ **Memory-Bound và Compute-Bound** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Động (dynamic / 동적) Shape** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Trực giác về Attention Kernel

Naive attention materialize score ma trận (matrix / 행렬) `QK^T`, làm bộ nhớ (memory / 메모리) chi phí (cost / 비용) tăng mạnh theo chuỗi (sequence / 시퀀스) length. Memory-efficient attention thuật toán (algorithm / 알고리즘) chia computation thành tile để tránh materialize toàn bộ ma trận (matrix / 행렬) trong HBM.

Toán học không đổi, nhưng thực thi (execution / 실행) schedule thay đổi.

> **Chuyển mạch:** Trong **Kiến trúc GPU cho AI**, **Động (dynamic / 동적) Shape** tiếp nhận điểm tựa từ **Trực giác về Attention Kernel** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **GPU bộ nhớ (memory / 메모리) Fragmentation** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Động (dynamic / 동적) Shape

Chuỗi (sequence / 시퀀스) length biến đổi làm kernel specialization và batching khó hơn. Padding, bucketing và compilation chiến lược (strategy / 전략) ảnh hưởng utilization.

> **Chuyển mạch:** Ở chặng này của **Kiến trúc GPU cho AI**, **GPU bộ nhớ (memory / 메모리) Fragmentation** tiếp nhận điểm tựa từ **Động (dynamic / 동적) Shape** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Multi-GPU Topology** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## GPU bộ nhớ (memory / 메모리) Fragmentation

Allocator quản lý nhiều khối (block / 블록) kích thước khác nhau có thể gây fragmentation. Paged-memory chiến lược (strategy / 전략) đặc biệt hữu ích cho KV bộ nhớ đệm (cache / 캐시) có chuỗi (sequence / 시퀀스) length biến động.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Kiến trúc GPU cho AI**, **Multi-GPU Topology** tiếp nhận điểm tựa từ **GPU bộ nhớ (memory / 메모리) Fragmentation** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Mô hình tư duy** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Multi-GPU Topology

Bandwidth giữa các GPU khác nhau tùy chúng nằm cùng nút (node / 노드), có direct interconnect hay phải đi qua đường dẫn (path / 경로) chậm hơn. Placement và sharding cần nhận thức topology.

> **Chuyển mạch:** Trong **Kiến trúc GPU cho AI**, **Mô hình tư duy** gom các mảnh từ **Multi-GPU Topology** thành một kết luận có thể mang sang phần kế tiếp. Từ đây, **Những nhầm lẫn thường gặp** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Mô hình tư duy

Phần này chốt mental model thành một chuỗi có thể dùng lại: bối cảnh → cơ chế → quan sát → giới hạn → quyết định. Hãy đọc sơ đồ như công cụ suy luận, không như một khẩu hiệu tách khỏi chapter.

```text
GPU code nhanh = đủ parallel work + data reuse cao + memory access hiệu quả + ít khoảng chờ đồng bộ
```

> **Chuyển mạch:** Ở chặng này của **Kiến trúc GPU cho AI**, **Mô hình tư duy** đã nêu tiêu chí phân biệt, còn **Những nhầm lẫn thường gặp** dùng tiêu chí đó để soi ranh giới và điểm dễ nhầm. Từ đây, **Liên kết kiến thức** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Những nhầm lẫn thường gặp

### “GPU có nhiều cốt lõi (core / 핵심) nên mọi parallel mã (code / 코드) đều nhanh”

Không. Irregular điều khiển (control / 제어) luồng (flow / 흐름) hoặc bộ nhớ (memory / 메모리) truy cập (access / 접근) có thể không phù hợp với GPU.

### “100% utilization nghĩa kernel đã tối ưu”

Không. thiết bị (device / 장치) có thể đang bận nhưng bị bộ nhớ (memory / 메모리) stall hoặc chạy kernel kém hiệu quả.

### “khung phần mềm (framework / 프레임워크) che hardware nên không cần hiểu GPU”

Không hoàn toàn. Khi mô hình (model / 모델) lớn hoặc độ trễ (latency / 지연 시간)/chi phí (cost / 비용) quan trọng, hardware intuition giúp chọn batch, precision, tensor shape và kiến trúc (architecture / 아키텍처) tốt hơn.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Kiến trúc GPU cho AI**, **Những nhầm lẫn thường gặp** đã nêu tiêu chí phân biệt, còn **Liên kết kiến thức** dùng tiêu chí đó để soi ranh giới và điểm dễ nhầm. Phần còn lại của file dùng kết quả này để khép lại mạch giải thích.

## Liên kết kiến thức

Xem [Memory & Bandwidth](./03_memory_and_bandwidth.md), [Parallel Computing](./04_parallel_computing.md), [Quantization](../15_ai_engineering/06_quantization.md) và [Transformer](../06_deep_learning_architectures/05_transformer.md).

> **Bàn giao:** Sau **Liên kết kiến thức**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](./README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
