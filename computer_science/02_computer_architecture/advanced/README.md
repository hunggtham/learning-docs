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

Track này đi từ ordering/instruction execution xuống speculation, cache/coherence, topology, address translation, data-parallel execution và sustained performance dưới power/thermal constraint. Mỗi chapter cần được đọc cùng câu hỏi: invariant kiến trúc nào software dựa vào, microarchitecture tối ưu bằng cách nào, pressure nào làm latency/throughput đổi phase và counter/evidence nào chứng minh bottleneck.

## Depth priorities

Hardware-prefetch pathology đã được deepen trong chapter cache/prefetch hiện có: khi prefetch sai làm tăng bandwidth pressure, cache pollution, memory-level parallelism hoặc tail latency. Bước tiếp theo là validate bằng controlled comparison và hardware-event evidence, không tạo chapter mới chỉ để có riêng “performance counters”, “side channels” hay “persistent memory”. Performance counters và bottleneck attribution phải được bổ sung vào các chapter nơi mechanism xuất hiện. Spectre-class reasoning thuộc speculation + security boundary; persistence thuộc storage/durability cross-layer.

Cross-layer path bắt buộc: [CPU cache → language memory model → concurrency bug](../../90_connections/advanced/02_correctness_path_language_os_cpu_memory_ordering.md).
