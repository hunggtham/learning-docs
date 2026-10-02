# SIMD, véc-tơ (vector / 벡터) ISA và mô hình thực thi GPU

> **Mạch đọc:** [README](./README.md) là bản đồ owner của **SIMD, véc-tơ (vector / 벡터) ISA và mô hình thực thi GPU**; nhìn vào vị trí đó trước để biết file này đang phục vụ nhánh kiến thức nào. **1. Scalar thực thi (execution / 실행) và dữ liệu (data / 데이터) parallelism** gom dữ liệu hoặc nguồn để kiểm tra một nhận định cụ thể; sau đó sang **2. véc-tơ (vector / 벡터) register và lane** để mở rộng đối tượng sang phạm vi kế cận. Mạch này nối SIMD, vector ISA và GPU execution, để dữ liệu song song được đọc qua lane, memory access và throughput.

Một CPU có thể tăng hiệu năng không chỉ bằng cách tăng tần số hay chạy nhiều luồng thực thi (thread / 스레드). Nếu cùng một phép toán phải áp dụng lên rất nhiều phần tử độc lập — cộng hai mảng số, biến đổi điểm ảnh (pixel / 픽셀), nhân ma trận — việc giải mã và điều phối một instruction riêng cho từng phần tử tạo ra overhead không cần thiết. **SIMD (Single Instruction, Multiple Data / một lệnh trên nhiều dữ liệu)** và kiến trúc GPU khai thác chính tính song song dữ liệu này.

Chapter này nối [pipeline và out-of-order execution](./01_out_of_order_execution_register_renaming_and_rob.md), [cache hierarchy](./03_advanced_cache_hierarchy_prefetching_and_replacement.md) với thời gian chạy (runtime / 런타임)/trình biên dịch (compiler / 컴파일러): mã (code / 코드) chỉ nhanh khi trình biên dịch (compiler / 컴파일러) có thể tạo instruction phù hợp và dữ liệu có bố cục (layout / 레이아웃) giúp phần cứng cấp dữ liệu đủ nhanh.

## 1. Scalar thực thi (execution / 실행) và dữ liệu (data / 데이터) parallelism

Trong thực thi vô hướng (scalar), một phép cộng thường xử lý một cặp giá trị:

```text
c[0] = a[0] + b[0]
c[1] = a[1] + b[1]
...
```

Nếu véc-tơ (vector / 벡터) register rộng 256 bit chứa tám số `float32`, một véc-tơ (vector / 벡터) instruction về mặt khái niệm có thể thực hiện tám phép cộng cùng lúc.

Điều này không có nghĩa CPU hoàn thành mọi thứ nhanh hơn đúng tám lần. tải (load / 로드)/store, phụ thuộc (dependency / 의존성), trượt bộ nhớ đệm (cache miss / 캐시 미스), instruction thông lượng (throughput / 처리량) và số thực thi (execution / 실행) cổng (port / 포트) vẫn giới hạn tốc độ.

> **Chuyển mạch:** Scalar xử lý từng phần tử, data parallelism xử lý nhiều phần tử cùng instruction; vector register/lane hiện thực SIMD, còn GPU threads là mô hình khác với SIMD lanes.

## 2. véc-tơ (vector / 벡터) register và lane

Véc-tơ (vector / 벡터) register là thanh ghi phần cứng đủ rộng để chứa nhiều phần tử. Mỗi vị trí lô-gic (logic / 논리) thường được gọi là **lane (làn xử lý)**.

```text
A = [a0 a1 a2 a3]
B = [b0 b1 b2 b3]
        vector add
C = [c0 c1 c2 c3]
```

Các ISA như SSE/AVX trên x86, NEON/SVE trên Arm cung cấp instruction véc-tơ (vector / 벡터) với width và ngữ nghĩa (semantics / 의미론) khác nhau. ISA là hợp đồng kiến trúc; số đơn vị thực thi (execution unit / 실행 유닛) vật lý bên dưới là vấn đề vi kiến trúc (microarchitecture).

> **Chuyển mạch:** Ở chặng này của **SIMD, véc-tơ (vector / 벡터) ISA và mô hình thực thi GPU**, **3. SIMD không đồng nghĩa nhiều luồng thực thi (thread / 스레드)** tiếp nhận điểm tựa từ **2. véc-tơ (vector / 벡터) register và lane** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **4. Auto-vectorization và phụ thuộc (dependency / 의존성)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 3. SIMD không đồng nghĩa nhiều luồng thực thi (thread / 스레드)

Một luồng thực thi (thread / 스레드) có thể phát SIMD instruction. Nhiều luồng thực thi (thread / 스레드) là nhiều luồng điều khiển có trạng thái scheduling riêng; SIMD là một instruction áp dụng lên nhiều dữ liệu (data / 데이터) lane.

Hai dạng song song có thể kết hợp:

```text
nhiều CPU core
  -> mỗi core chạy nhiều thread
     -> mỗi thread dùng vector instruction
```

Vì vậy hiệu năng (performance / 성능) lập luận (reasoning / 추론) phải phân biệt thread-level parallelism với data-level parallelism.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **SIMD, véc-tơ (vector / 벡터) ISA và mô hình thực thi GPU**, **4. Auto-vectorization và phụ thuộc (dependency / 의존성)** tiếp nhận điểm tựa từ **3. SIMD không đồng nghĩa nhiều luồng thực thi (thread / 스레드)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **5. bộ nhớ (memory / 메모리) bố cục (layout / 레이아웃) quyết định khả năng cấp dữ liệu** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 4. Auto-vectorization và phụ thuộc (dependency / 의존성)

Trình biên dịch (compiler / 컴파일러) có thể tự véc-tơ (vector / 벡터) hóa vòng lặp (loop / 루프) nếu chứng minh các iteration đủ độc lập.

```c
for (int i = 0; i < n; i++) {
    c[i] = a[i] + b[i];
}
```

Vòng lặp (loop / 루프) này thuận lợi vì iteration `i` không phụ thuộc kết quả `i-1`.

Ngược lại:

```c
for (int i = 1; i < n; i++) {
    a[i] = a[i - 1] + x[i];
}
```

Iteration sau phụ thuộc iteration trước. Vectorization trực tiếp có thể thay đổi ngữ nghĩa (semantics / 의미론).

Do đó trình biên dịch (compiler / 컴파일러) tối ưu hóa (optimization / 최적화) phụ thuộc vào alias phân tích (analysis / 분석), phụ thuộc (dependency / 의존성) phân tích (analysis / 분석), alignment và mục tiêu (target / 대상) ISA chứ không đơn giản là “vòng lặp (loop / 루프) lớn thì dùng SIMD”.

> **Chuyển mạch:** Trong **SIMD, véc-tơ (vector / 벡터) ISA và mô hình thực thi GPU**, **4. Auto-vectorization và phụ thuộc (dependency / 의존성)** nêu điều cần giải thích; **5. bộ nhớ (memory / 메모리) bố cục (layout / 레이아웃) quyết định khả năng cấp dữ liệu** đối chiếu nó với bằng chứng hoặc nguồn kiểm chứng. Từ đây, **6. Alignment, gather và scatter** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 5. bộ nhớ (memory / 메모리) bố cục (layout / 레이아웃) quyết định khả năng cấp dữ liệu

Giả sử chương trình xử lý hàng triệu đối tượng (object / 객체):

```text
Array of Structures:
[x y z][x y z][x y z]...
```

Nếu chỉ cần `x`, bộ nhớ đệm (cache / 캐시) line còn chứa `y`, `z` không cần thiết. **cấu trúc (structure / 구조) of Arrays (SoA)**:

```text
x: [x x x x ...]
y: [y y y y ...]
z: [z z z z ...]
```

có thể phù hợp hơn cho véc-tơ (vector / 벡터) tải (load / 로드) liên tục.

Đây là liên kết (connection / 연결) quan trọng giữa cấu trúc dữ liệu (data structure / 자료구조) và hardware: cùng một thuật toán Big-O nhưng bố cục (layout / 레이아웃) khác nhau có thể tạo bộ nhớ đệm (cache / 캐시) hành vi (behavior / 동작) và SIMD efficiency rất khác.

> **Chuyển mạch:** Ở chặng này của **SIMD, véc-tơ (vector / 벡터) ISA và mô hình thực thi GPU**, **5. bộ nhớ (memory / 메모리) bố cục (layout / 레이아웃) quyết định khả năng cấp dữ liệu** nêu điều cần giải thích; **6. Alignment, gather và scatter** đối chiếu nó với bằng chứng hoặc nguồn kiểm chứng. Từ đây, **7. Masked thực thi (execution / 실행)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 6. Alignment, gather và scatter

Dữ liệu liên tục thường dễ vectorize nhất. Khi các phần tử nằm rải rác, một số ISA hỗ trợ **gather** để đọc nhiều địa chỉ và **scatter** để ghi nhiều địa chỉ. Nhưng gather/scatter thường đắt hơn contiguous truy cập (access / 접근) vì bộ nhớ (memory / 메모리) subsystem phải xử lý nhiều location.

Alignment từng quan trọng hơn trên ISA cũ; CPU hiện đại thường hỗ trợ unaligned truy cập (access / 접근) tốt hơn, nhưng truy cập (access / 접근) vượt cache-line/page ranh giới (boundary / 경계) vẫn có thể tăng chi phí.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **SIMD, véc-tơ (vector / 벡터) ISA và mô hình thực thi GPU**, **7. Masked thực thi (execution / 실행)** tiếp nhận điểm tựa từ **6. Alignment, gather và scatter** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **8. GPU mở rộng dữ liệu (data / 데이터) parallelism** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 7. Masked thực thi (execution / 실행)

Không phải mọi lane luôn cần thực hiện thao tác (operation / 연산). véc-tơ (vector / 벡터) ISA hiện đại có mask/predicate:

```text
values: [10, -2, 7, -1]
mask:   [ 1,  0, 1,  0]
```

Instruction chỉ cập nhật lane được mask chọn. Điều này giúp xử lý điều kiện (condition / 조건) mà không cần scalar branch cho từng phần tử.

Nhưng masked thực thi (execution / 실행) không làm công việc (work / 작업) miễn phí: lane không hoạt động có thể làm giảm mức sử dụng phần cứng.

> **Chuyển mạch:** Trong **SIMD, véc-tơ (vector / 벡터) ISA và mô hình thực thi GPU**, **7. Masked thực thi (execution / 실행)** nêu điều cần giải thích; **8. GPU mở rộng dữ liệu (data / 데이터) parallelism** đối chiếu nó với bằng chứng hoặc nguồn kiểm chứng. Từ đây, **9. SIMT, warp và wavefront** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 8. GPU mở rộng dữ liệu (data / 데이터) parallelism

GPU được thiết kế để duy trì số lượng rất lớn công việc (work / 작업) item và che độ trễ (latency / 지연 시간) bằng cách chuyển giữa các nhóm công việc sẵn sàng. CPU thường đầu tư nhiều transistor vào branch prediction, large bộ nhớ đệm (cache / 캐시) và out-of-order machinery để giảm độ trễ (latency / 지연 시간) của một số luồng thực thi (thread / 스레드); GPU dành nhiều tài nguyên hơn cho thông lượng (throughput / 처리량) song song.

Mô hình tư duy (mental model / 사고 모델) đơn giản:

```text
CPU: tối ưu latency của luồng điều khiển phức tạp
GPU: tối ưu throughput của lượng lớn công việc tương tự
```

Đây là xu hướng kiến trúc, không phải ranh giới tuyệt đối.

> **Chuyển mạch:** Ở chặng này của **SIMD, véc-tơ (vector / 벡터) ISA và mô hình thực thi GPU**, **8. GPU mở rộng dữ liệu (data / 데이터) parallelism** nêu điều cần giải thích; **9. SIMT, warp và wavefront** đối chiếu nó với bằng chứng hoặc nguồn kiểm chứng. Từ đây, **10. GPU bộ nhớ (memory / 메모리) hierarchy** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 9. SIMT, warp và wavefront

GPU thường được mô tả bằng **SIMT (Single Instruction, Multiple Threads)**. Nhiều logical luồng thực thi (thread / 스레드) được nhóm thành warp/wavefront và thực thi instruction theo nhóm.

Nếu các luồng thực thi (thread / 스레드) trong cùng nhóm đi theo branch khác nhau:

```text
if condition:
    path A
else:
    path B
```

GPU có thể phải chạy đường dẫn (path / 경로) A cho một tập lane rồi đường dẫn (path / 경로) B cho tập còn lại. Hiện tượng này gọi là **branch divergence (phân kỳ nhánh)** và làm giảm utilization.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **SIMD, véc-tơ (vector / 벡터) ISA và mô hình thực thi GPU**, **10. GPU bộ nhớ (memory / 메모리) hierarchy** tiếp nhận điểm tựa từ **9. SIMT, warp và wavefront** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **11. Arithmetic intensity** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 10. GPU bộ nhớ (memory / 메모리) hierarchy

GPU cũng có bộ nhớ (memory / 메모리) hierarchy: register, cục bộ (local / 로컬)/dùng chung (shared / 공유) bộ nhớ (memory / 메모리), bộ nhớ đệm (cache / 캐시) và toàn cục (global / 전역)/thiết bị (device / 장치) bộ nhớ (memory / 메모리). Tên cụ thể phụ thuộc nền tảng (platform / 플랫폼).

Toàn cục (global / 전역) bộ nhớ (memory / 메모리) có bandwidth lớn nhưng độ trễ (latency / 지연 시간) cao. Kernel nhanh thường cần truy cập (access / 접근) mẫu (pattern / 패턴) cho phép **coalescing**: các luồng thực thi (thread / 스레드) lân cận truy cập địa chỉ có thể gom thành giao dịch (transaction / 트랜잭션) hiệu quả.

Nếu mỗi luồng thực thi (thread / 스레드) đọc địa chỉ ngẫu nhiên, bandwidth thực tế có thể thấp dù thông số phần cứng rất cao.

> **Chuyển mạch:** Trong **SIMD, véc-tơ (vector / 벡터) ISA và mô hình thực thi GPU**, **11. Arithmetic intensity** tiếp nhận điểm tựa từ **10. GPU bộ nhớ (memory / 메모리) hierarchy** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **12. Transfer chi phí (cost / 비용) và accelerator ranh giới (boundary / 경계)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 11. Arithmetic intensity

Một tải công việc (workload / 워크로드) chỉ hưởng lợi từ compute thông lượng (throughput / 처리량) lớn nếu có đủ phép tính trên mỗi byte dữ liệu di chuyển. Tỷ lệ này gọi là **arithmetic intensity (cường độ tính toán)**.

```text
arithmetic intensity = số phép tính / số byte chuyển qua memory hierarchy
```

Véc-tơ (vector / 벡터)/GPU tối ưu hóa (optimization / 최적화) vì vậy liên hệ trực tiếp với roofline mô hình (model / 모델): tải công việc (workload / 워크로드) memory-bound không tự nhiên nhanh hơn chỉ vì ALU mạnh hơn.

> **Chuyển mạch:** Ở chặng này của **SIMD, véc-tơ (vector / 벡터) ISA và mô hình thực thi GPU**, **11. Arithmetic intensity** đã nêu tiêu chí phân biệt, còn **12. Transfer chi phí (cost / 비용) và accelerator ranh giới (boundary / 경계)** dùng tiêu chí đó để soi ranh giới và điểm dễ nhầm. Từ đây, **13. Floating-point và reproducibility** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 12. Transfer chi phí (cost / 비용) và accelerator ranh giới (boundary / 경계)

GPU rời có bộ nhớ (memory / 메모리) riêng. Chuyển dữ liệu CPU → GPU → CPU có chi phí. Một kernel rất nhanh có thể không tạo speedup end-to-end nếu transfer và synchronization chiếm phần lớn thời gian.

Đây là cùng nguyên tắc xuất hiện trong phân tán (distributed / 분산) các hệ thống (systems / 시스템들): tối ưu thành phần (component / 컴포넌트) không đảm bảo tối ưu toàn đường dẫn (path / 경로) nếu ranh giới (boundary / 경계) crossing đắt.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **SIMD, véc-tơ (vector / 벡터) ISA và mô hình thực thi GPU**, **12. Transfer chi phí (cost / 비용) và accelerator ranh giới (boundary / 경계)** đã nêu tiêu chí phân biệt, còn **13. Floating-point và reproducibility** dùng tiêu chí đó để soi ranh giới và điểm dễ nhầm. Từ đây, **14. Khi vectorization không giúp** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 13. Floating-point và reproducibility

Parallel reduction có thể cộng số theo thứ tự khác scalar vòng lặp (loop / 루프). Floating-point addition không associative tuyệt đối:

```text
(a + b) + c != a + (b + c)
```

với một số giá trị do rounding. Vì vậy vectorization/GPU có thể tạo sai khác số học nhỏ dù thuật toán (algorithm / 알고리즘) lô-gic (logic / 논리) giống nhau. Scientific computing và ML cần hiểu tolerance thay vì mặc định bit-identical kết quả (result / 결과).

> **Chuyển mạch:** Trong **SIMD, véc-tơ (vector / 벡터) ISA và mô hình thực thi GPU**, **14. Khi vectorization không giúp** tiếp nhận điểm tựa từ **13. Floating-point và reproducibility** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Dùng chung (common / 공통) Misconceptions** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 14. Khi vectorization không giúp

SIMD/GPU kém hiệu quả khi tải công việc (workload / 워크로드) có phụ thuộc (dependency / 의존성) tuần tự mạnh, branch divergence lớn, dữ liệu (data / 데이터) set quá nhỏ, bộ nhớ (memory / 메모리) truy cập (access / 접근) ngẫu nhiên, synchronization dày hoặc transfer overhead lớn.

Tối ưu hóa (optimization / 최적화) phải bắt đầu từ đo lường (measurement / 측정). “GPU nhanh hơn CPU” hay “AVX nhanh hơn scalar” không phải định luật độc lập với tải công việc (workload / 워크로드).

> **Chuyển mạch:** Ở chặng này của **SIMD, véc-tơ (vector / 벡터) ISA và mô hình thực thi GPU**, **Dùng chung (common / 공통) Misconceptions** tiếp nhận điểm tựa từ **14. Khi vectorization không giúp** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Mô hình tư duy (mental model / 사고 모델)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Dùng chung (common / 공통) Misconceptions

**“SIMD là multithreading.”** Không. SIMD là dữ liệu (data / 데이터) parallelism trong một instruction stream.

**“véc-tơ (vector / 벡터) width 8 nghĩa là nhanh gấp 8.”** thông lượng (throughput / 처리량) còn phụ thuộc bộ nhớ (memory / 메모리), phụ thuộc (dependency / 의존성) và thực thi (execution / 실행) resources.

**“GPU có nhiều cốt lõi (core / 핵심) nên mọi chương trình đều nhanh hơn.”** GPU hiệu quả khi tải công việc (workload / 워크로드) có đủ parallelism và truy cập (access / 접근) mẫu (pattern / 패턴) phù hợp.

**“Big-O giống nhau thì hiệu năng (performance / 성능) gần nhau.”** Big-O bỏ qua bộ nhớ đệm (cache / 캐시) locality, vectorization và bộ nhớ (memory / 메모리) bandwidth — những yếu tố quyết định ở quy mô thực tế.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **SIMD, véc-tơ (vector / 벡터) ISA và mô hình thực thi GPU**, **Mô hình tư duy (mental model / 사고 모델)** gom các mảnh từ **Dùng chung (common / 공통) Misconceptions** thành một kết luận có thể mang sang phần kế tiếp. Phần còn lại của file dùng kết quả này để khép lại mạch giải thích.

## Mô hình tư duy (mental model / 사고 모델)

> SIMD và GPU không tạo ra công việc ít hơn. Chúng thay đổi cách **đóng gói và cung cấp** nhiều công việc độc lập cho phần cứng để amortize điều khiển (control / 제어) overhead và khai thác nhiều thực thi (execution / 실행) lane cùng lúc.

Khi lập luận (reasoning / 추론) về hiệu năng (performance / 성능), hãy đi theo chuỗi: phụ thuộc (dependency / 의존성) của thuật toán → dữ liệu (data / 데이터) bố cục (layout / 레이아웃) → trình biên dịch (compiler / 컴파일러) vectorization → instruction thông lượng (throughput / 처리량) → bộ nhớ đệm (cache / 캐시)/bandwidth → synchronization → end-to-end độ trễ (latency / 지연 시간).

Xem thêm: [Cache hierarchy](./03_advanced_cache_hierarchy_prefetching_and_replacement.md), [NUMA](./04_numa_interconnects_and_scalable_coherence.md), [Compiler IR/optimization](../../04_programming_languages/advanced/04_compiler_ir_ssa_dataflow_and_optimization.md).

> **Bàn giao:** Sau **Mô hình tư duy (mental model / 사고 모델)**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](./README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
