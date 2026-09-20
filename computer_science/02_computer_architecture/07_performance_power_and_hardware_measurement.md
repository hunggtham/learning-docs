# Performance, power và đo lường hardware

Một CPU “3.5 GHz” không thể tự nói nó nhanh hơn CPU “3.0 GHz”. Performance xuất hiện từ interaction giữa instruction count, cycles per instruction, memory stalls, parallelism, branch behavior, compiler và workload. Vì vậy architecture cần một cost model định lượng thay vì suy luận từ một specification riêng lẻ.

## CPU time và ba thành phần cơ bản

Một model kinh điển:

\[
CPU\ Time = Instruction\ Count \times CPI \times Clock\ Cycle\ Time
\]

hoặc tương đương

\[
CPU\ Time = \frac{Instruction\ Count \times CPI}{Clock\ Rate}
\]

Instruction Count phụ thuộc algorithm, compiler và ISA. CPI (cycles per instruction) là average, phụ thuộc instruction mix, cache misses, branch mispredictions và pipeline behavior. Clock Rate chỉ là một factor.

Một optimization có thể giảm instruction count nhưng tăng cache misses; kết quả cuối chỉ biết qua total execution time trên workload đại diện.

## Latency và throughput

Latency là thời gian hoàn thành một operation; throughput là số operations trong một đơn vị thời gian. Pipelining có thể tăng throughput mà không giảm latency của từng instruction tương ứng.

Server architecture thường tối ưu throughput/concurrency, trong khi interactive UI nhạy với tail latency. Không có một metric performance duy nhất phù hợp mọi system.

## IPC, CPI và pipeline stalls

Instructions per cycle (IPC) là inverse-style metric của CPI trong một số context. Superscalar CPU có thể retire nhiều instructions mỗi cycle nếu dependencies và resources cho phép.

Cache miss, branch misprediction và data dependency tạo stalls. Out-of-order execution cố lấp bubbles bằng independent instructions, nhưng không thể vượt true dependencies hoặc latency chain vô hạn.

## Amdahl và giới hạn speedup

Nếu fraction `p` của workload có thể speed up `s` lần, total speedup theo Amdahl:

\[
Speedup = \frac{1}{(1-p)+p/s}
\]

Nếu chỉ 20% runtime được tối ưu vô hạn, speedup tối đa vẫn chỉ `1/0.8 = 1.25×`.

Ý nghĩa engineering: profile trước khi tối ưu. Tối ưu phần hiếm không cứu total latency.

## Power, energy và thermal constraints

Dynamic power của CMOS thường được mô hình hóa gần:

\[
P \propto C V^2 f
\]

với capacitance `C`, voltage `V`, frequency `f`. Tăng frequency thường đòi voltage cao hơn, nên power tăng nhanh hơn tuyến tính.

Thermal Design Power không phải exact power consumption mọi lúc, nhưng thermal constraints giải thích vì sao CPU boost ngắn hạn rồi giảm clock, và vì sao mobile devices ưu tiên energy efficiency.

Performance per watt trở thành metric quan trọng trong datacenter và battery-powered systems.

## Benchmarking đúng nghĩa

Benchmark phải đại diện workload thật. Microbenchmark đo một mechanism nhỏ nhưng dễ bị compiler optimization, warm caches, branch prediction hoặc measurement overhead làm sai.

Các nguyên tắc quan trọng gồm warm-up khi runtime có JIT, chạy đủ repetitions, đo distribution thay vì chỉ average, pin/control environment khi cần và tránh benchmark code bị compiler dead-code eliminate.

Tail percentiles như p95/p99 quan trọng cho server latency vì average có thể che long tail.

## Roofline intuition

Một computation có thể compute-bound hoặc memory-bandwidth-bound. Arithmetic intensity đo lượng computation trên mỗi byte memory traffic. Nếu intensity thấp, tăng FLOPS peak không giúp nhiều; memory bandwidth là ceiling.

Mental model này giải thích tại sao matrix kernels, vectorization và data layout quan trọng trong numerical workloads.

## Common Misconceptions

**“Clock cao hơn = CPU nhanh hơn.”** Chỉ đúng nếu các factors còn lại tương đương, điều hiếm khi hoàn toàn đúng.

**“Benchmark score là property tuyệt đối của chip.”** Score thuộc chip + compiler + OS + workload + configuration.

**“Parallelize càng nhiều càng tốt.”** Synchronization, communication và serial fraction giới hạn speedup.

## Mental Model

> Performance là property của một path qua nhiều bottlenecks. Đừng hỏi “component nào nhanh”, hãy hỏi “workload nào, metric nào, bottleneck ở đâu, và optimization chuyển bottleneck sang đâu”.

## Kết nối

Xem [parallel architecture](./05_parallel_computer_architecture.md), [cache hierarchy](./02_memory_hierarchy_and_cache.md), [software performance/capacity](../08_software_systems/02_performance_capacity_and_scalability.md) và [cross-cutting trade-offs](../90_connections/03_cross_cutting_tradeoffs.md).