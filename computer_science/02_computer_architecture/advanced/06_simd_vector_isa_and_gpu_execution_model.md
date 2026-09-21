# SIMD, Vector ISA và mô hình thực thi GPU

Một CPU có thể tăng hiệu năng không chỉ bằng cách tăng tần số hay chạy nhiều thread. Nếu cùng một phép toán phải áp dụng lên rất nhiều phần tử độc lập — cộng hai mảng số, biến đổi pixel, nhân ma trận — việc giải mã và điều phối một instruction riêng cho từng phần tử tạo ra overhead không cần thiết. **SIMD (Single Instruction, Multiple Data / một lệnh trên nhiều dữ liệu)** và kiến trúc GPU khai thác chính tính song song dữ liệu này.

Chapter này nối [pipeline và out-of-order execution](./01_out_of_order_execution_register_renaming_and_rob.md), [cache hierarchy](./03_advanced_cache_hierarchy_prefetching_and_replacement.md) với runtime/compiler: code chỉ nhanh khi compiler có thể tạo instruction phù hợp và dữ liệu có layout giúp phần cứng cấp dữ liệu đủ nhanh.

## 1. Scalar execution và data parallelism

Trong thực thi vô hướng (scalar), một phép cộng thường xử lý một cặp giá trị:

```text
c[0] = a[0] + b[0]
c[1] = a[1] + b[1]
...
```

Nếu vector register rộng 256 bit chứa tám số `float32`, một vector instruction về mặt khái niệm có thể thực hiện tám phép cộng cùng lúc.

Điều này không có nghĩa CPU hoàn thành mọi thứ nhanh hơn đúng tám lần. Load/store, dependency, cache miss, instruction throughput và số execution port vẫn giới hạn tốc độ.

## 2. Vector register và lane

Vector register là thanh ghi phần cứng đủ rộng để chứa nhiều phần tử. Mỗi vị trí logic thường được gọi là **lane (làn xử lý)**.

```text
A = [a0 a1 a2 a3]
B = [b0 b1 b2 b3]
        vector add
C = [c0 c1 c2 c3]
```

Các ISA như SSE/AVX trên x86, NEON/SVE trên Arm cung cấp instruction vector với width và semantics khác nhau. ISA là hợp đồng kiến trúc; số execution unit vật lý bên dưới là vấn đề vi kiến trúc (microarchitecture).

## 3. SIMD không đồng nghĩa nhiều thread

Một thread có thể phát SIMD instruction. Nhiều thread là nhiều luồng điều khiển có trạng thái scheduling riêng; SIMD là một instruction áp dụng lên nhiều data lane.

Hai dạng song song có thể kết hợp:

```text
nhiều CPU core
  -> mỗi core chạy nhiều thread
     -> mỗi thread dùng vector instruction
```

Vì vậy performance reasoning phải phân biệt thread-level parallelism với data-level parallelism.

## 4. Auto-vectorization và dependency

Compiler có thể tự vector hóa loop nếu chứng minh các iteration đủ độc lập.

```c
for (int i = 0; i < n; i++) {
    c[i] = a[i] + b[i];
}
```

Loop này thuận lợi vì iteration `i` không phụ thuộc kết quả `i-1`.

Ngược lại:

```c
for (int i = 1; i < n; i++) {
    a[i] = a[i - 1] + x[i];
}
```

Iteration sau phụ thuộc iteration trước. Vectorization trực tiếp có thể thay đổi semantics.

Do đó compiler optimization phụ thuộc vào alias analysis, dependency analysis, alignment và target ISA chứ không đơn giản là “loop lớn thì dùng SIMD”.

## 5. Memory layout quyết định khả năng cấp dữ liệu

Giả sử chương trình xử lý hàng triệu object:

```text
Array of Structures:
[x y z][x y z][x y z]...
```

Nếu chỉ cần `x`, cache line còn chứa `y`, `z` không cần thiết. **Structure of Arrays (SoA)**:

```text
x: [x x x x ...]
y: [y y y y ...]
z: [z z z z ...]
```

có thể phù hợp hơn cho vector load liên tục.

Đây là connection quan trọng giữa data structure và hardware: cùng một thuật toán Big-O nhưng layout khác nhau có thể tạo cache behavior và SIMD efficiency rất khác.

## 6. Alignment, gather và scatter

Dữ liệu liên tục thường dễ vectorize nhất. Khi các phần tử nằm rải rác, một số ISA hỗ trợ **gather** để đọc nhiều địa chỉ và **scatter** để ghi nhiều địa chỉ. Nhưng gather/scatter thường đắt hơn contiguous access vì memory subsystem phải xử lý nhiều location.

Alignment từng quan trọng hơn trên ISA cũ; CPU hiện đại thường hỗ trợ unaligned access tốt hơn, nhưng access vượt cache-line/page boundary vẫn có thể tăng chi phí.

## 7. Masked execution

Không phải mọi lane luôn cần thực hiện operation. Vector ISA hiện đại có mask/predicate:

```text
values: [10, -2, 7, -1]
mask:   [ 1,  0, 1,  0]
```

Instruction chỉ cập nhật lane được mask chọn. Điều này giúp xử lý condition mà không cần scalar branch cho từng phần tử.

Nhưng masked execution không làm work miễn phí: lane không hoạt động có thể làm giảm mức sử dụng phần cứng.

## 8. GPU mở rộng data parallelism

GPU được thiết kế để duy trì số lượng rất lớn work item và che latency bằng cách chuyển giữa các nhóm công việc sẵn sàng. CPU thường đầu tư nhiều transistor vào branch prediction, large cache và out-of-order machinery để giảm latency của một số thread; GPU dành nhiều tài nguyên hơn cho throughput song song.

Mental model đơn giản:

```text
CPU: tối ưu latency của luồng điều khiển phức tạp
GPU: tối ưu throughput của lượng lớn công việc tương tự
```

Đây là xu hướng kiến trúc, không phải ranh giới tuyệt đối.

## 9. SIMT, warp và wavefront

GPU thường được mô tả bằng **SIMT (Single Instruction, Multiple Threads)**. Nhiều logical thread được nhóm thành warp/wavefront và thực thi instruction theo nhóm.

Nếu các thread trong cùng nhóm đi theo branch khác nhau:

```text
if condition:
    path A
else:
    path B
```

GPU có thể phải chạy path A cho một tập lane rồi path B cho tập còn lại. Hiện tượng này gọi là **branch divergence (phân kỳ nhánh)** và làm giảm utilization.

## 10. GPU memory hierarchy

GPU cũng có memory hierarchy: register, local/shared memory, cache và global/device memory. Tên cụ thể phụ thuộc platform.

Global memory có bandwidth lớn nhưng latency cao. Kernel nhanh thường cần access pattern cho phép **coalescing**: các thread lân cận truy cập địa chỉ có thể gom thành transaction hiệu quả.

Nếu mỗi thread đọc địa chỉ ngẫu nhiên, bandwidth thực tế có thể thấp dù thông số phần cứng rất cao.

## 11. Arithmetic intensity

Một workload chỉ hưởng lợi từ compute throughput lớn nếu có đủ phép tính trên mỗi byte dữ liệu di chuyển. Tỷ lệ này gọi là **arithmetic intensity (cường độ tính toán)**.

```text
arithmetic intensity = số phép tính / số byte chuyển qua memory hierarchy
```

Vector/GPU optimization vì vậy liên hệ trực tiếp với roofline model: workload memory-bound không tự nhiên nhanh hơn chỉ vì ALU mạnh hơn.

## 12. Transfer cost và accelerator boundary

GPU rời có memory riêng. Chuyển dữ liệu CPU → GPU → CPU có chi phí. Một kernel rất nhanh có thể không tạo speedup end-to-end nếu transfer và synchronization chiếm phần lớn thời gian.

Đây là cùng nguyên tắc xuất hiện trong distributed systems: tối ưu component không đảm bảo tối ưu toàn path nếu boundary crossing đắt.

## 13. Floating-point và reproducibility

Parallel reduction có thể cộng số theo thứ tự khác scalar loop. Floating-point addition không associative tuyệt đối:

```text
(a + b) + c != a + (b + c)
```

với một số giá trị do rounding. Vì vậy vectorization/GPU có thể tạo sai khác số học nhỏ dù algorithm logic giống nhau. Scientific computing và ML cần hiểu tolerance thay vì mặc định bit-identical result.

## 14. Khi vectorization không giúp

SIMD/GPU kém hiệu quả khi workload có dependency tuần tự mạnh, branch divergence lớn, data set quá nhỏ, memory access ngẫu nhiên, synchronization dày hoặc transfer overhead lớn.

Optimization phải bắt đầu từ measurement. “GPU nhanh hơn CPU” hay “AVX nhanh hơn scalar” không phải định luật độc lập với workload.

## Common Misconceptions

**“SIMD là multithreading.”** Không. SIMD là data parallelism trong một instruction stream.

**“Vector width 8 nghĩa là nhanh gấp 8.”** Throughput còn phụ thuộc memory, dependency và execution resources.

**“GPU có nhiều core nên mọi chương trình đều nhanh hơn.”** GPU hiệu quả khi workload có đủ parallelism và access pattern phù hợp.

**“Big-O giống nhau thì performance gần nhau.”** Big-O bỏ qua cache locality, vectorization và memory bandwidth — những yếu tố quyết định ở quy mô thực tế.

## Mental Model

> SIMD và GPU không tạo ra công việc ít hơn. Chúng thay đổi cách **đóng gói và cung cấp** nhiều công việc độc lập cho phần cứng để amortize control overhead và khai thác nhiều execution lane cùng lúc.

Khi reasoning về performance, hãy đi theo chuỗi: dependency của thuật toán → data layout → compiler vectorization → instruction throughput → cache/bandwidth → synchronization → end-to-end latency.

Xem thêm: [Cache hierarchy](./03_advanced_cache_hierarchy_prefetching_and_replacement.md), [NUMA](./04_numa_interconnects_and_scalable_coherence.md), [Compiler IR/optimization](../../04_programming_languages/advanced/04_compiler_ir_ssa_dataflow_and_optimization.md).