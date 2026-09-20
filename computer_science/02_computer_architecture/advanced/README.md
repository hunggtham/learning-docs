# Advanced Computer Architecture

Bắt đầu từ [Computer Architecture foundation](../../basic/02_computer_architecture/README.md).

Roadmap:

1. [Memory consistency, cache coherence và ordering](./00_memory_consistency_cache_coherence_and_ordering.md)
2. [Out-of-order execution, register renaming và reorder buffer](./01_out_of_order_execution_register_renaming_and_rob.md)
3. [Branch prediction, speculation và pipeline recovery](./02_branch_prediction_speculation_and_pipeline_recovery.md)
4. [Advanced cache hierarchy, prefetching và replacement](./03_advanced_cache_hierarchy_prefetching_and_replacement.md)
5. [NUMA, interconnects và scalable coherence](./04_numa_interconnects_and_scalable_coherence.md)
6. [TLB, page walkers, huge pages và virtualization extensions](./05_tlb_page_walkers_huge_pages_and_virtualization.md)
7. SIMD/vector ISA và GPU execution model
8. Performance counters, roofline và bottleneck attribution
9. Microarchitectural side channels: Spectre/Meltdown-class reasoning
10. Persistent memory và crash-consistency implications

Sáu chapter hiện tại tạo đường reasoning liên tục từ instruction execution → speculation → cache/coherence → machine topology → address translation. Phần tiếp theo sẽ đi vào vector/GPU execution, measurement và security/performance consequences.