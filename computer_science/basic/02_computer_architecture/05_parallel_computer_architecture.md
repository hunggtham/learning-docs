# Pipelining, multicore, SIMD và GPU

Performance không thể tăng mãi chỉ bằng clock frequency vì power/thermal limits và memory latency. Modern computers khai thác parallelism ở nhiều levels: overlap stages trong một core, execute multiple instructions, nhiều cores, vector lanes và thousands of GPU threads.

## Pipelining

Thay vì chờ instruction A đi hết fetch→decode→execute→memory→writeback rồi mới bắt đầu B, pipeline overlap stages. Giống dây chuyền: latency một item có thể không giảm, nhưng throughput tăng khi pipeline đầy.

Hazards xuất hiện khi instructions phụ thuộc data, branch chưa biết direction hoặc cùng tranh resource. Forwarding, stalling và branch prediction xử lý hazards.

## Superscalar và out-of-order

Superscalar CPU có thể issue nhiều operations mỗi cycle. Out-of-order execution tìm independent instructions sẵn sàng, trong khi retirement giữ architectural order/precise exceptions.

Instruction-level parallelism bị giới hạn bởi dependency chains. Code có nhiều independent work dễ tận dụng hơn.

## Multicore

Nhiều cores chạy instruction streams song song. Parallel speedup bị giới hạn bởi sequential portion. Amdahl's Law:

\[
S(N)=\frac{1}{(1-P)+P/N}
\]

với P là fraction parallelizable, N processors. Nếu 10% workload bắt buộc sequential, vô hạn cores cũng giới hạn speedup khoảng 10x.

Formula nhắc rằng optimization phải tìm actual serial bottleneck, không chỉ thêm threads.

## SIMD/vectorization

Single Instruction Multiple Data thực hiện cùng operation trên nhiều lanes dữ liệu. Image processing, numeric loops, ML kernels và codecs hưởng lợi mạnh nếu data layout contiguous và control flow đều.

Auto-vectorization của compiler phụ thuộc aliasing, alignment và dependency analysis. SoA layout thường thân thiện hơn AoS cho operations theo field.

## GPU

GPU có massive throughput-oriented parallelism, nhiều lightweight execution lanes và memory hierarchy riêng. Nó phù hợp data-parallel workloads với arithmetic intensity cao. CPU tối ưu latency và complex control; GPU tối ưu throughput.

Transfer data CPU↔GPU có cost, nên offload tiny operation có thể chậm hơn CPU.

## Memory bandwidth và roofline intuition

Kernel có thể compute-bound hoặc memory-bound. Nếu mỗi byte load chỉ làm rất ít arithmetic, thêm ALUs không giúp vì bandwidth là bottleneck. Arithmetic intensity — operations per byte — giúp reasoning.

## NUMA

Multi-socket/large systems có Non-Uniform Memory Access: core access local memory nhanh hơn remote node. OS scheduling và allocation locality ảnh hưởng performance. “RAM là shared uniform pool” lại là abstraction không hoàn toàn đúng.

## Parallelism khác concurrency

Concurrency là nhiều tasks có progress overlapping về logical time; parallelism là thực sự execute đồng thời. Single-core event loop concurrent nhưng không necessarily parallel. Multi-core workers có thể both.

## Mental Model

> Hardware cố **giữ nhiều execution resources bận cùng lúc**. Speedup chỉ xuất hiện nếu workload có independent work và data đến đủ nhanh; dependency, synchronization và memory bandwidth là giới hạn.

## Common Misconceptions

**“8 cores làm chương trình nhanh 8x.”** Chỉ phần parallelizable hưởng lợi, còn overhead/synchronization/memory contention có thể giảm speedup.

**“GPU luôn nhanh hơn CPU.”** Chỉ với workloads phù hợp và đủ lớn để amortize transfer/setup.

**“Concurrency và parallelism là một.”** Concurrency là structure của overlapping tasks; parallelism là simultaneous physical execution.

## Kết nối

Hardware parallelism đặt nền cho [process/thread scheduling](../03_operating_systems/01_processes_threads_and_scheduling.md), [synchronization](../03_operating_systems/02_concurrency_synchronization_and_deadlock.md) và [performance scalability](../08_software_systems/02_performance_capacity_and_scalability.md). [Data layout](../01_algorithms_data_structures/02_memory_models_and_data_layout.md) quyết định SIMD/cache efficiency.
