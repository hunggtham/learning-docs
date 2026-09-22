# Advanced Computer Architecture

Bắt đầu từ [Computer Architecture foundation](../../basic/02_computer_architecture/00_digital_logic_and_circuits.md).

## Canonical chapters

1. [Memory consistency, cache coherence và ordering](./00_memory_consistency_cache_coherence_and_ordering.md)
2. [Out-of-order execution, register renaming và reorder buffer](./01_out_of_order_execution_register_renaming_and_rob.md)
3. [Branch prediction, speculation và pipeline recovery](./02_branch_prediction_speculation_and_pipeline_recovery.md)
4. [Advanced cache hierarchy, prefetching và replacement](./03_advanced_cache_hierarchy_prefetching_and_replacement.md)
5. [NUMA, interconnects và scalable coherence](./04_numa_interconnects_and_scalable_coherence.md)
6. [TLB, page walkers, huge pages và virtualization extensions](./05_tlb_page_walkers_huge_pages_and_virtualization.md)
7. [SIMD, vector ISA và GPU execution model](./06_simd_vector_isa_and_gpu_execution_model.md)
8. [Power, thermal, DVFS và sustained performance](./07_power_thermal_dvfs_and_sustained_performance.md)

Track này đi từ ordering/instruction execution xuống speculation, cache/coherence, topology, address translation, data-parallel execution và cuối cùng là physical operating envelope quyết định performance có thể duy trì. Mỗi chapter cần được đọc cùng câu hỏi: invariant kiến trúc nào software dựa vào, microarchitecture tối ưu bằng cách nào, pressure nào làm latency/throughput đổi phase và counter/evidence nào chứng minh bottleneck.

Chapter power/thermal bổ sung một distinction quan trọng: peak clock/benchmark ngắn không đồng nghĩa sustained capacity. Workload activity, voltage/frequency operating point, thermal inertia, package power budget và cooling path có thể làm cùng binary có throughput khác theo thời gian. Vì vậy performance diagnosis phải phân biệt instruction/memory bottleneck với controller chủ động giảm operating point để giữ physical safety invariant.

## Depth priorities

Không tạo chapter mới chỉ để có riêng “performance counters”, “side channels” hay một tên accelerator mới nếu mental model có thể được đặt đúng boundary hiện có. Performance counters và bottleneck attribution phải nằm trong chapter nơi mechanism xuất hiện. Spectre-class reasoning thuộc speculation + security boundary; persistence thuộc storage/durability cross-layer.

Hardware-prefetch pathology tiếp tục được deepen trong cache hierarchy trừ khi sau này xuất hiện một reasoning path đủ độc lập về predictor state, bandwidth pollution và cross-core interference. Power/thermal đã được tách vì nó có control loop, time constant và sustained-performance invariant riêng.

Cross-layer paths bắt buộc: [CPU cache → language memory model → concurrency bug](../../90_connections/advanced/02_correctness_path_language_os_cpu_memory_ordering.md) và các performance path nối architecture với [fleet profiling/cost attribution](../../08_software_systems/advanced/07_fleet_profiling_cost_attribution_and_multi_tenant_efficiency.md).