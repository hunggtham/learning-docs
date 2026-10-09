# Pipelining, multicore, SIMD và GPU

> **Mạch đọc:** [README](./README.md) là bản đồ owner của **Pipelining, multicore, SIMD và GPU**. Route đi từ pipeline hazards → superscalar/out-of-order → multicore/cache coherence → SIMD/GPU throughput và synchronization, để parallelism được đánh giá cùng overhead và memory behavior.

Hiệu năng (performance / 성능) không thể tăng mãi chỉ bằng clock frequency vì power/thermal limits và bộ nhớ (memory / 메모리) độ trễ (latency / 지연 시간). hiện đại (modern / 현대적) computers khai thác parallelism ở nhiều levels: overlap stages trong một cốt lõi (core / 핵심), execute multiple instructions, nhiều cores, véc-tơ (vector / 벡터) lanes và thousands of GPU threads.

## Pipelining

Thay vì chờ instruction A đi hết fetch→decode→execute→bộ nhớ (memory / 메모리)→writeback rồi mới bắt đầu B, chuỗi xử lý (pipeline / 파이프라인) overlap stages. Giống dây chuyền: độ trễ (latency / 지연 시간) một item có thể không giảm, nhưng thông lượng (throughput / 처리량) tăng khi chuỗi xử lý (pipeline / 파이프라인) đầy.

Hazards xuất hiện khi instructions phụ thuộc dữ liệu (data / 데이터), branch chưa biết direction hoặc cùng tranh tài nguyên (resource / 자원). Forwarding, stalling và branch prediction xử lý hazards.

Pipelining tạo song song bên trong một instruction stream. Superscalar và out-of-order mở rộng song song đó ở mỗi cycle; khi thêm multicore, chi phí coherence và coordination trở thành một phần của bài toán.

## Superscalar và out-of-order

Superscalar CPU có thể issue nhiều operations mỗi cycle. Out-of-order thực thi (execution / 실행) tìm independent instructions sẵn sàng, trong khi retirement giữ architectural thứ tự (order / 순서)/precise exceptions.

Instruction-level parallelism bị giới hạn bởi phụ thuộc (dependency / 의존성) chains. mã (code / 코드) có nhiều independent công việc (work / 작업) dễ tận dụng hơn.

Superscalar và out-of-order khai thác các instruction độc lập trong một core. Multicore nhân số luồng thực thi, nhưng speedup lúc này còn bị giới hạn bởi serial fraction và sự tranh chấp bộ nhớ.

## Multicore

Nhiều cores chạy instruction streams song song. Parallel speedup bị giới hạn bởi sequential portion. Amdahl's Law:

\[
S(N)=\frac{1}{(1-P)+P/N}
\]

với P là fraction parallelizable, N processors. Nếu 10% tải công việc (workload / 워크로드) bắt buộc sequential, vô hạn cores cũng giới hạn speedup khoảng 10x.

Formula nhắc rằng tối ưu hóa (optimization / 최적화) phải tìm actual serial bottleneck, không chỉ thêm threads.

Multicore tách công việc giữa các instruction streams. SIMD giữ một instruction nhưng áp dụng nó lên nhiều phần tử dữ liệu, nên hiệu quả phụ thuộc vào layout và khả năng bỏ rẽ nhánh.

## SIMD/vectorization

Single Instruction Multiple dữ liệu (data / 데이터) thực hiện cùng thao tác (operation / 연산) trên nhiều lanes dữ liệu. xử lý ảnh (image processing / 이미지 처리), numeric loops, ML kernels và codecs hưởng lợi mạnh nếu dữ liệu (data / 데이터) bố cục (layout / 레이아웃) contiguous và điều khiển (control / 제어) luồng (flow / 흐름) đều.

Auto-vectorization của trình biên dịch (compiler / 컴파일러) phụ thuộc aliasing, alignment và phụ thuộc (dependency / 의존성) phân tích (analysis / 분석). SoA bố cục (layout / 레이아웃) thường thân thiện hơn AoS cho operations theo trường dữ liệu (field / 필드).

SIMD khai thác các lanes gần nhau trong một core. GPU đẩy ý tưởng data-parallel lên hàng nghìn threads và một memory hierarchy riêng; vì vậy hiệu quả phải được đọc cùng bandwidth và chi phí chuyển dữ liệu.

## GPU

GPU có massive throughput-oriented parallelism, nhiều lightweight thực thi (execution / 실행) lanes và bộ nhớ (memory / 메모리) hierarchy riêng. Nó phù hợp data-parallel workloads với arithmetic intensity cao. CPU tối ưu độ trễ (latency / 지연 시간) và complex điều khiển (control / 제어); GPU tối ưu thông lượng (throughput / 처리량).

Transfer dữ liệu (data / 데이터) CPU↔GPU có chi phí (cost / 비용), nên offload tiny thao tác (operation / 연산) có thể chậm hơn CPU.

GPU và CPU đều có thể bị giới hạn bởi tốc độ đưa dữ liệu đến execution units. Roofline đặt compute và bandwidth trên cùng một khung; với nhiều socket, khoảng cách tới vùng memory cũng trở thành giới hạn cần tính.

## Bộ nhớ (memory / 메모리) bandwidth và roofline intuition

Kernel có thể compute-bound hoặc memory-bound. Nếu mỗi byte tải (load / 로드) chỉ làm rất ít arithmetic, thêm ALUs không giúp vì bandwidth là bottleneck. Arithmetic intensity — operations per byte — giúp lập luận (reasoning / 추론).

Roofline mô tả giới hạn bandwidth như một con số của kernel, còn NUMA thêm vị trí của vùng nhớ vào con số đó. Một access remote có thể làm cùng một kiểu song song trở nên đắt hơn đáng kể.

## NUMA

Multi-socket/large các hệ thống (systems / 시스템들) có Non-Uniform bộ nhớ (memory / 메모리) truy cập (access / 접근): cốt lõi (core / 핵심) truy cập (access / 접근) cục bộ (local / 로컬) bộ nhớ (memory / 메모리) nhanh hơn remote nút (node / 노드). OS scheduling và allocation locality ảnh hưởng hiệu năng (performance / 성능). “RAM là dùng chung (shared / 공유) uniform pool” lại là lớp trừu tượng (abstraction / 추상화) không hoàn toàn đúng.

NUMA cho thấy “chạy nhiều việc” chưa nói rõ các việc có thực sự chạy đồng thời hay chỉ cùng tiến triển theo thời gian. Phân biệt concurrency với parallelism giúp đọc đúng các số đo và chi phí synchronization.

## Parallelism khác tính đồng thời (concurrency / 동시성)

Tính đồng thời (concurrency / 동시성) là nhiều tasks có progress overlapping về logical thời gian (time / 시간); parallelism là thực sự execute đồng thời. Single-core vòng lặp sự kiện (event loop / 이벤트 루프) concurrent nhưng không necessarily parallel. Multi-core workers có thể both.

Parallelism chỉ tạo speedup khi có công việc độc lập, dữ liệu đến kịp và chi phí phối hợp đủ nhỏ. Mô hình này là tiêu chuẩn để kiểm tra các ngộ nhận về core, GPU và concurrency.

## Mô hình tư duy (mental model / 사고 모델)

> Hardware cố **giữ nhiều thực thi (execution / 실행) resources bận cùng lúc**. Speedup chỉ xuất hiện nếu tải công việc (workload / 워크로드) có independent công việc (work / 작업) và dữ liệu (data / 데이터) đến đủ nhanh; phụ thuộc (dependency / 의존성), synchronization và bộ nhớ (memory / 메모리) bandwidth là giới hạn.

## Dùng chung (common / 공통) Misconceptions

**“8 cores làm chương trình nhanh 8x.”** Chỉ phần parallelizable hưởng lợi, còn overhead/synchronization/bộ nhớ (memory / 메모리) contention có thể giảm speedup.

**“GPU luôn nhanh hơn CPU.”** Chỉ với workloads phù hợp và đủ lớn để amortize transfer/setup.

**“tính đồng thời (concurrency / 동시성) và parallelism là một.”** tính đồng thời (concurrency / 동시성) là cấu trúc (structure / 구조) của overlapping tasks; parallelism là simultaneous vật lý (physical / 물리적) thực thi (execution / 실행).

Các ngộ nhận trên đều bỏ qua một loại overhead hoặc một giới hạn của dữ liệu. Kết nối cuối file đưa mô hình này về scheduling, synchronization, scalability và data layout.

## Kết nối

Hardware parallelism đặt nền cho [process/thread scheduling](../03_operating_systems/01_processes_threads_and_scheduling.md), [synchronization](../03_operating_systems/02_concurrency_synchronization_and_deadlock.md) và [performance scalability](../08_software_systems/02_performance_capacity_and_scalability.md). [Data layout](../01_algorithms_data_structures/02_memory_models_and_data_layout.md) quyết định SIMD/bộ nhớ đệm (cache / 캐시) efficiency.

> **Bàn giao:** Sau **Kết nối**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](./README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
