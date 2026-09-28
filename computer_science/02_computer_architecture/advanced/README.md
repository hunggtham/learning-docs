# Advanced Computer kiến trúc (architecture / 아키텍처)

> **Mạch đọc:** Đọc **Advanced Computer kiến trúc (architecture / 아키텍처)** như một mắt xích của lộ trình học (learning path / 학습 경로) hiện tại, không như một ghi chú tách rời. Nội dung đi từ **chuẩn gốc (canonical / 정본) chapters** sang **độ sâu (depth / 깊이) priorities**; điểm nối này chuẩn bị câu hỏi cho các mục sau thay vì dừng ở định nghĩa đầu tiên.


Bắt đầu từ [Computer Architecture foundation](../../basic/02_computer_architecture/00_digital_logic_and_circuits.md).

## Chuẩn gốc (canonical / 정본) chapters

1. [Memory consistency, cache coherence và ordering](./00_memory_consistency_cache_coherence_and_ordering.md)
2. [Out-of-order execution, register renaming và reorder buffer](./01_out_of_order_execution_register_renaming_and_rob.md)
3. [Branch prediction, speculation và pipeline recovery](./02_branch_prediction_speculation_and_pipeline_recovery.md)
4. [Advanced cache hierarchy, prefetching và replacement](./03_advanced_cache_hierarchy_prefetching_and_replacement.md)
5. [NUMA, interconnects và scalable coherence](./04_numa_interconnects_and_scalable_coherence.md)
6. [TLB, page walkers, huge pages và virtualization extensions](./05_tlb_page_walkers_huge_pages_and_virtualization.md)
7. [SIMD, vector ISA và GPU execution model](./06_simd_vector_isa_and_gpu_execution_model.md)
8. [Power, thermal, DVFS và sustained performance](./07_power_thermal_dvfs_and_sustained_performance.md)

Nhánh học (track / 트랙) này đi từ thứ tự (ordering / 순서)/instruction thực thi (execution / 실행) xuống speculation, bộ nhớ đệm (cache / 캐시)/coherence, topology, address translation, data-parallel thực thi (execution / 실행) và sustained hiệu năng (performance / 성능) dưới power/thermal ràng buộc (constraint / 제약조건). Mỗi chapter cần được đọc cùng câu hỏi: bất biến (invariant / 불변식) kiến trúc nào software dựa vào, microarchitecture tối ưu bằng cách nào, pressure nào làm độ trễ (latency / 지연 시간)/thông lượng (throughput / 처리량) đổi phase và counter/bằng chứng (evidence / 증거) nào chứng minh bottleneck.


> **Chuyển mạch:** Từ **chuẩn gốc (canonical / 정본) chapters**, ta sang **độ sâu (depth / 깊이) priorities** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## Độ sâu (depth / 깊이) priorities

Hardware-prefetch pathology đã được deepen trong chapter bộ nhớ đệm (cache / 캐시)/prefetch hiện có: khi prefetch sai làm tăng bandwidth pressure, bộ nhớ đệm (cache / 캐시) pollution, memory-level parallelism hoặc tail độ trễ (latency / 지연 시간). Bước tiếp theo là validate bằng controlled comparison và hardware-event bằng chứng (evidence / 증거), không tạo chapter mới chỉ để có riêng “hiệu năng (performance / 성능) counters”, “side channels” hay “persistent bộ nhớ (memory / 메모리)”. hiệu năng (performance / 성능) counters và bottleneck attribution phải được bổ sung vào các chapter nơi cơ chế (mechanism / 메커니즘) xuất hiện. Spectre-class lập luận (reasoning / 추론) thuộc speculation + ranh giới bảo mật (security boundary / 보안 경계); persistence thuộc lưu trữ (storage / 저장소)/durability cross-layer.

Cross-layer đường dẫn (path / 경로) bắt buộc: [CPU cache → language memory model → concurrency bug](../../90_connections/advanced/02_correctness_path_language_os_cpu_memory_ordering.md).

> **Bàn giao:** Sau **độ sâu (depth / 깊이) priorities**, hãy chốt bất biến (invariant / 불변식) và giới hạn của mục này trước khi nối sang kiến thức kế tiếp. Có thể đọc tiếp [00 memory consistency cache coherence and ordering](./00_memory_consistency_cache_coherence_and_ordering.md) để đối chiếu ranh giới (boundary / 경계) gần nhất.
