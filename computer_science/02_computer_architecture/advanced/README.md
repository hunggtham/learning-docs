# Advanced Computer Architecture

Bắt đầu từ [Computer Architecture foundation](../../basic/02_computer_architecture/README.md).

Roadmap:

1. [Memory consistency, cache coherence và ordering](./00_memory_consistency_cache_coherence_and_ordering.md)
2. [Out-of-order execution, register renaming và reorder buffer](./01_out_of_order_execution_register_renaming_and_rob.md)
3. [Branch prediction, speculation và pipeline recovery](./02_branch_prediction_speculation_and_pipeline_recovery.md)
4. Advanced cache hierarchy, prefetching và replacement
5. NUMA, interconnects và scalable coherence
6. TLB, page walkers, huge pages và virtualization extensions
7. SIMD/vector ISA và GPU execution model
8. Performance counters, roofline và bottleneck attribution
9. Microarchitectural side channels: Spectre/Meltdown-class reasoning
10. Persistent memory và crash-consistency implications

Ba chapter đầu tạo một chuỗi liên tục từ memory ordering → instruction scheduling → speculative control flow. Các chapter tiếp theo sẽ mở rộng sang memory hierarchy, NUMA, translation, vector/GPU và performance diagnosis.