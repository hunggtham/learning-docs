# Pipelining, multicore, SIMD và GPU

> **Mạch đọc:** Đọc **Pipelining, multicore, SIMD và GPU** như một mắt xích của lộ trình học (learning path / 학습 경로) hiện tại, không như một ghi chú tách rời. Nội dung đi từ **Pipelining** sang **Superscalar và out-of-order**; điểm nối này chuẩn bị câu hỏi cho các mục sau thay vì dừng ở định nghĩa đầu tiên.


Hiệu năng (performance / 성능) không thể tăng mãi chỉ bằng clock frequency vì power/thermal limits và bộ nhớ (memory / 메모리) độ trễ (latency / 지연 시간). hiện đại (modern / 현대적) computers khai thác parallelism ở nhiều levels: overlap stages trong một cốt lõi (core / 핵심), execute multiple instructions, nhiều cores, véc-tơ (vector / 벡터) lanes và thousands of GPU threads.

## Pipelining

Thay vì chờ instruction A đi hết fetch→decode→execute→bộ nhớ (memory / 메모리)→writeback rồi mới bắt đầu B, chuỗi xử lý (pipeline / 파이프라인) overlap stages. Giống dây chuyền: độ trễ (latency / 지연 시간) một item có thể không giảm, nhưng thông lượng (throughput / 처리량) tăng khi chuỗi xử lý (pipeline / 파이프라인) đầy.

Hazards xuất hiện khi instructions phụ thuộc dữ liệu (data / 데이터), branch chưa biết direction hoặc cùng tranh tài nguyên (resource / 자원). Forwarding, stalling và branch prediction xử lý hazards.


> **Chuyển mạch:** Từ **Pipelining**, ta sang **Superscalar và out-of-order** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## Superscalar và out-of-order

Superscalar CPU có thể issue nhiều operations mỗi cycle. Out-of-order thực thi (execution / 실행) tìm independent instructions sẵn sàng, trong khi retirement giữ architectural thứ tự (order / 순서)/precise exceptions.

Instruction-level parallelism bị giới hạn bởi phụ thuộc (dependency / 의존성) chains. mã (code / 코드) có nhiều independent công việc (work / 작업) dễ tận dụng hơn.


> **Chuyển mạch:** Từ **Superscalar và out-of-order**, ta sang **Multicore** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## Multicore

Nhiều cores chạy instruction streams song song. Parallel speedup bị giới hạn bởi sequential portion. Amdahl's Law:

\[
S(N)=\frac{1}{(1-P)+P/N}
\]

với P là fraction parallelizable, N processors. Nếu 10% tải công việc (workload / 워크로드) bắt buộc sequential, vô hạn cores cũng giới hạn speedup khoảng 10x.

Formula nhắc rằng tối ưu hóa (optimization / 최적화) phải tìm actual serial bottleneck, không chỉ thêm threads.


> **Chuyển mạch:** Từ **Multicore**, ta sang **SIMD/vectorization** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## SIMD/vectorization

Single Instruction Multiple dữ liệu (data / 데이터) thực hiện cùng thao tác (operation / 연산) trên nhiều lanes dữ liệu. xử lý ảnh (image processing / 이미지 처리), numeric loops, ML kernels và codecs hưởng lợi mạnh nếu dữ liệu (data / 데이터) bố cục (layout / 레이아웃) contiguous và điều khiển (control / 제어) luồng (flow / 흐름) đều.

Auto-vectorization của trình biên dịch (compiler / 컴파일러) phụ thuộc aliasing, alignment và phụ thuộc (dependency / 의존성) phân tích (analysis / 분석). SoA bố cục (layout / 레이아웃) thường thân thiện hơn AoS cho operations theo trường dữ liệu (field / 필드).


> **Chuyển mạch:** Từ **SIMD/vectorization**, ta sang **GPU** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## GPU

GPU có massive throughput-oriented parallelism, nhiều lightweight thực thi (execution / 실행) lanes và bộ nhớ (memory / 메모리) hierarchy riêng. Nó phù hợp data-parallel workloads với arithmetic intensity cao. CPU tối ưu độ trễ (latency / 지연 시간) và complex điều khiển (control / 제어); GPU tối ưu thông lượng (throughput / 처리량).

Transfer dữ liệu (data / 데이터) CPU↔GPU có chi phí (cost / 비용), nên offload tiny thao tác (operation / 연산) có thể chậm hơn CPU.


> **Chuyển mạch:** Từ **GPU**, ta sang **bộ nhớ (memory / 메모리) bandwidth và roofline intuition** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## Bộ nhớ (memory / 메모리) bandwidth và roofline intuition

Kernel có thể compute-bound hoặc memory-bound. Nếu mỗi byte tải (load / 로드) chỉ làm rất ít arithmetic, thêm ALUs không giúp vì bandwidth là bottleneck. Arithmetic intensity — operations per byte — giúp lập luận (reasoning / 추론).


> **Chuyển mạch:** Từ **bộ nhớ (memory / 메모리) bandwidth và roofline intuition**, ta sang **NUMA** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## NUMA

Multi-socket/large các hệ thống (systems / 시스템들) có Non-Uniform bộ nhớ (memory / 메모리) truy cập (access / 접근): cốt lõi (core / 핵심) truy cập (access / 접근) cục bộ (local / 로컬) bộ nhớ (memory / 메모리) nhanh hơn remote nút (node / 노드). OS scheduling và allocation locality ảnh hưởng hiệu năng (performance / 성능). “RAM là dùng chung (shared / 공유) uniform pool” lại là lớp trừu tượng (abstraction / 추상화) không hoàn toàn đúng.


> **Chuyển mạch:** Từ **NUMA**, ta sang **Parallelism khác tính đồng thời (concurrency / 동시성)** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## Parallelism khác tính đồng thời (concurrency / 동시성)

Tính đồng thời (concurrency / 동시성) là nhiều tasks có progress overlapping về logical thời gian (time / 시간); parallelism là thực sự execute đồng thời. Single-core vòng lặp sự kiện (event loop / 이벤트 루프) concurrent nhưng không necessarily parallel. Multi-core workers có thể both.


> **Chuyển mạch:** Từ **Parallelism khác tính đồng thời (concurrency / 동시성)**, ta sang **mô hình tư duy (mental model / 사고 모델)** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## Mô hình tư duy (mental model / 사고 모델)

> Hardware cố **giữ nhiều thực thi (execution / 실행) resources bận cùng lúc**. Speedup chỉ xuất hiện nếu tải công việc (workload / 워크로드) có independent công việc (work / 작업) và dữ liệu (data / 데이터) đến đủ nhanh; phụ thuộc (dependency / 의존성), synchronization và bộ nhớ (memory / 메모리) bandwidth là giới hạn.


> **Chuyển mạch:** Từ **mô hình tư duy (mental model / 사고 모델)**, ta sang **dùng chung (common / 공통) Misconceptions** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## Dùng chung (common / 공통) Misconceptions

**“8 cores làm chương trình nhanh 8x.”** Chỉ phần parallelizable hưởng lợi, còn overhead/synchronization/bộ nhớ (memory / 메모리) contention có thể giảm speedup.

**“GPU luôn nhanh hơn CPU.”** Chỉ với workloads phù hợp và đủ lớn để amortize transfer/setup.

**“tính đồng thời (concurrency / 동시성) và parallelism là một.”** tính đồng thời (concurrency / 동시성) là cấu trúc (structure / 구조) của overlapping tasks; parallelism là simultaneous vật lý (physical / 물리적) thực thi (execution / 실행).


> **Chuyển mạch:** Từ **dùng chung (common / 공통) Misconceptions**, ta sang **Kết nối** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## Kết nối

Hardware parallelism đặt nền cho [process/thread scheduling](../03_operating_systems/01_processes_threads_and_scheduling.md), [synchronization](../03_operating_systems/02_concurrency_synchronization_and_deadlock.md) và [performance scalability](../08_software_systems/02_performance_capacity_and_scalability.md). [Data layout](../01_algorithms_data_structures/02_memory_models_and_data_layout.md) quyết định SIMD/bộ nhớ đệm (cache / 캐시) efficiency.

> **Bàn giao:** Sau **Kết nối**, hãy chốt bất biến (invariant / 불변식) và giới hạn của mục này trước khi nối sang kiến thức kế tiếp. Có thể đọc tiếp [00 digital logic and circuits](./00_digital_logic_and_circuits.md) để đối chiếu ranh giới (boundary / 경계) gần nhất.
