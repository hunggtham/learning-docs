# Hiệu năng (performance / 성능), power và đo lường hardware

> **Mạch đọc:** Đặt **hiệu năng (performance / 성능), power và đo lường hardware** trong bản đồ [README](./README.md) để thấy đơn vị sở hữu (owner / 오너) và vị trí của nó. Nội dung đi từ **CPU thời gian (time / 시간) và ba thành phần cơ bản** sang **độ trễ (latency / 지연 시간) và thông lượng (throughput / 처리량)**; điểm nối này chuẩn bị câu hỏi cho các mục sau thay vì dừng ở định nghĩa đầu tiên.


Một CPU “3.5 GHz” không thể tự nói nó nhanh hơn CPU “3.0 GHz”. hiệu năng (performance / 성능) xuất hiện từ tương tác (interaction / 상호작용) giữa instruction count, cycles per instruction, bộ nhớ (memory / 메모리) stalls, parallelism, branch hành vi (behavior / 동작), trình biên dịch (compiler / 컴파일러) và tải công việc (workload / 워크로드). Vì vậy kiến trúc (architecture / 아키텍처) cần một chi phí (cost / 비용) mô hình (model / 모델) định lượng thay vì suy luận từ một specification riêng lẻ.

## CPU thời gian (time / 시간) và ba thành phần cơ bản

Một mô hình (model / 모델) kinh điển:

\[
CPU\ thời gian (time / 시간) = Instruction\ Count \times CPI \times Clock\ Cycle\ thời gian (time / 시간)
\]

hoặc tương đương

\[
CPU\ thời gian (time / 시간) = \frac{Instruction\ Count \times CPI}{Clock\ tỷ lệ (rate / 비율)}
\]

Instruction Count phụ thuộc thuật toán (algorithm / 알고리즘), trình biên dịch (compiler / 컴파일러) và ISA. CPI (cycles per instruction) là average, phụ thuộc instruction mix, bộ nhớ đệm (cache / 캐시) misses, branch mispredictions và chuỗi xử lý (pipeline / 파이프라인) hành vi (behavior / 동작). Clock tỷ lệ (rate / 비율) chỉ là một factor.

Một tối ưu hóa (optimization / 최적화) có thể giảm instruction count nhưng tăng bộ nhớ đệm (cache / 캐시) misses; kết quả cuối chỉ biết qua total thực thi (execution / 실행) thời gian (time / 시간) trên tải công việc (workload / 워크로드) đại diện.


> **Chuyển mạch:** Từ **CPU thời gian (time / 시간) và ba thành phần cơ bản**, ta sang **độ trễ (latency / 지연 시간) và thông lượng (throughput / 처리량)** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## Độ trễ (latency / 지연 시간) và thông lượng (throughput / 처리량)

Độ trễ (latency / 지연 시간) là thời gian hoàn thành một thao tác (operation / 연산); thông lượng (throughput / 처리량) là số operations trong một đơn vị thời gian. Pipelining có thể tăng thông lượng (throughput / 처리량) mà không giảm độ trễ (latency / 지연 시간) của từng instruction tương ứng.

Máy chủ (server / 서버) kiến trúc (architecture / 아키텍처) thường tối ưu thông lượng (throughput / 처리량)/tính đồng thời (concurrency / 동시성), trong khi interactive UI nhạy với tail độ trễ (latency / 지연 시간). Không có một chỉ số (metric / 지표) hiệu năng (performance / 성능) duy nhất phù hợp mọi hệ thống (system / 시스템).


> **Chuyển mạch:** Từ **độ trễ (latency / 지연 시간) và thông lượng (throughput / 처리량)**, ta sang **IPC, CPI và chuỗi xử lý (pipeline / 파이프라인) stalls** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## IPC, CPI và chuỗi xử lý (pipeline / 파이프라인) stalls

Instructions per cycle (IPC) là inverse-style chỉ số (metric / 지표) của CPI trong một số ngữ cảnh (context / 맥락). Superscalar CPU có thể retire nhiều instructions mỗi cycle nếu dependencies và resources cho phép.

Trượt bộ nhớ đệm (cache miss / 캐시 미스), branch misprediction và dữ liệu (data / 데이터) phụ thuộc (dependency / 의존성) tạo stalls. Out-of-order thực thi (execution / 실행) cố lấp bubbles bằng independent instructions, nhưng không thể vượt true dependencies hoặc độ trễ (latency / 지연 시간) chuỗi (chain / 사슬) vô hạn.


> **Chuyển mạch:** Từ **IPC, CPI và chuỗi xử lý (pipeline / 파이프라인) stalls**, ta sang **Amdahl và giới hạn speedup** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## Amdahl và giới hạn speedup

Nếu fraction `p` của tải công việc (workload / 워크로드) có thể speed up `s` lần, total speedup theo Amdahl:

\[
Speedup = \frac{1}{(1-p)+p/s}
\]

Nếu chỉ 20% thời gian chạy (runtime / 런타임) được tối ưu vô hạn, speedup tối đa vẫn chỉ `1/0.8 = 1.25×`.

Ý nghĩa kỹ thuật (engineering / 엔지니어링): profile trước khi tối ưu. Tối ưu phần hiếm không cứu total độ trễ (latency / 지연 시간).


> **Chuyển mạch:** Từ **Amdahl và giới hạn speedup**, ta sang **Power, năng lượng (energy / 에너지) và thermal các ràng buộc (constraints / 제약조건들)** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## Power, năng lượng (energy / 에너지) và thermal các ràng buộc (constraints / 제약조건들)

Động (dynamic / 동적) power của CMOS thường được mô hình hóa gần:

\[
P \propto C V^2 f
\]

với capacitance `C`, voltage `V`, frequency `f`. Tăng frequency thường đòi voltage cao hơn, nên power tăng nhanh hơn tuyến tính.

Thermal thiết kế (design / 설계) Power không phải chính xác (exact / 정확한) power consumption mọi lúc, nhưng thermal các ràng buộc (constraints / 제약조건들) giải thích vì sao CPU boost ngắn hạn rồi giảm clock, và vì sao mobile devices ưu tiên năng lượng (energy / 에너지) efficiency.

Hiệu năng (performance / 성능) per watt trở thành chỉ số (metric / 지표) quan trọng trong datacenter và battery-powered các hệ thống (systems / 시스템들).


> **Chuyển mạch:** Từ **Power, năng lượng (energy / 에너지) và thermal các ràng buộc (constraints / 제약조건들)**, ta sang **Benchmarking đúng nghĩa** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## Benchmarking đúng nghĩa

Benchmark phải đại diện tải công việc (workload / 워크로드) thật. Microbenchmark đo một cơ chế (mechanism / 메커니즘) nhỏ nhưng dễ bị trình biên dịch (compiler / 컴파일러) tối ưu hóa (optimization / 최적화), warm caches, branch prediction hoặc đo lường (measurement / 측정) overhead làm sai.

Các nguyên tắc quan trọng gồm warm-up khi thời gian chạy (runtime / 런타임) có JIT, chạy đủ repetitions, đo phân phối (distribution / 분포) thay vì chỉ average, pin/điều khiển (control / 제어) môi trường (environment / 환경) khi cần và tránh benchmark mã (code / 코드) bị trình biên dịch (compiler / 컴파일러) dead-code eliminate.

Tail percentiles như p95/p99 quan trọng cho máy chủ (server / 서버) độ trễ (latency / 지연 시간) vì average có thể che long tail.


> **Chuyển mạch:** Từ **Benchmarking đúng nghĩa**, ta sang **Roofline intuition** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## Roofline intuition

Một computation có thể compute-bound hoặc memory-bandwidth-bound. Arithmetic intensity đo lượng computation trên mỗi byte bộ nhớ (memory / 메모리) traffic. Nếu intensity thấp, tăng FLOPS peak không giúp nhiều; bộ nhớ (memory / 메모리) bandwidth là ceiling.

Mô hình tư duy (mental model / 사고 모델) này giải thích tại sao ma trận (matrix / 행렬) kernels, vectorization và dữ liệu (data / 데이터) bố cục (layout / 레이아웃) quan trọng trong numerical workloads.


> **Chuyển mạch:** Từ **Roofline intuition**, ta sang **dùng chung (common / 공통) Misconceptions** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## Dùng chung (common / 공통) Misconceptions

**“Clock cao hơn = CPU nhanh hơn.”** Chỉ đúng nếu các factors còn lại tương đương, điều hiếm khi hoàn toàn đúng.

**“Benchmark score là thuộc tính (property / 속성) tuyệt đối của chip.”** Score thuộc chip + trình biên dịch (compiler / 컴파일러) + OS + tải công việc (workload / 워크로드) + cấu hình (configuration / 구성).

**“Parallelize càng nhiều càng tốt.”** Synchronization, communication và serial fraction giới hạn speedup.


> **Chuyển mạch:** Từ **dùng chung (common / 공통) Misconceptions**, ta sang **mô hình tư duy (mental model / 사고 모델)** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## Mô hình tư duy (mental model / 사고 모델)

> hiệu năng (performance / 성능) là thuộc tính (property / 속성) của một đường dẫn (path / 경로) qua nhiều bottlenecks. Đừng hỏi “thành phần (component / 컴포넌트) nào nhanh”, hãy hỏi “tải công việc (workload / 워크로드) nào, chỉ số (metric / 지표) nào, bottleneck ở đâu, và tối ưu hóa (optimization / 최적화) chuyển bottleneck sang đâu”.


> **Chuyển mạch:** Từ **mô hình tư duy (mental model / 사고 모델)**, ta sang **Kết nối** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## Kết nối

Xem [parallel architecture](./05_parallel_computer_architecture.md), [cache hierarchy](./02_memory_hierarchy_and_cache.md), [software performance/capacity](../08_software_systems/02_performance_capacity_and_scalability.md) và [cross-cutting trade-offs](../90_connections/03_cross_cutting_tradeoffs.md).

> **Bàn giao:** Sau **Kết nối**, hãy chốt bất biến (invariant / 불변식) và giới hạn của mục này trước khi nối sang kiến thức kế tiếp. Có thể đọc tiếp [00 digital logic and circuits](./00_digital_logic_and_circuits.md) để đối chiếu ranh giới (boundary / 경계) gần nhất.
