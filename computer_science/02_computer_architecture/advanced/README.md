# Advanced Computer Kiến trúc (architecture / 아키텍처)

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

Nhánh học (track / 트랙) này đi từ thứ tự (ordering / 순서)/instruction thực thi (execution / 실행) xuống speculation, bộ nhớ đệm (cache / 캐시)/coherence, topology, address translation, data-parallel thực thi (execution / 실행) và cuối cùng là vật lý (physical / 물리적) operating envelope quyết định hiệu năng (performance / 성능) có thể duy trì. Mỗi chapter cần được đọc cùng câu hỏi: bất biến (invariant / 불변식) kiến trúc nào software dựa vào, microarchitecture tối ưu bằng cách nào, pressure nào làm độ trễ (latency / 지연 시간)/thông lượng (throughput / 처리량) đổi phase và counter/bằng chứng (evidence / 증거) nào chứng minh bottleneck.

Chapter power/thermal bổ sung một distinction quan trọng: peak clock/benchmark ngắn không đồng nghĩa sustained sức chứa (capacity / 용량). Tải công việc (workload / 워크로드) activity, voltage/frequency operating điểm (point / 지점), thermal inertia, gói (package / 패키지) power ngân sách (budget / 예산) và cooling đường dẫn (path / 경로) có thể làm cùng nhị phân (binary / 이진) có thông lượng (throughput / 처리량) khác theo thời gian. Vì vậy hiệu năng (performance / 성능) diagnosis phải phân biệt instruction/bộ nhớ (memory / 메모리) bottleneck với controller chủ động giảm operating điểm (point / 지점) để giữ vật lý (physical / 물리적) an toàn (safety / 안전) bất biến (invariant / 불변식).

## Độ sâu (depth / 깊이) priorities

Không tạo chapter mới chỉ để có riêng “hiệu năng (performance / 성능) counters”, “side channels” hay một tên accelerator mới nếu mô hình tư duy (mental model / 사고 모델) có thể được đặt đúng ranh giới (boundary / 경계) hiện có. Hiệu năng (performance / 성능) counters và bottleneck attribution phải nằm trong chapter nơi cơ chế (mechanism / 메커니즘) xuất hiện. Spectre-class lập luận (reasoning / 추론) thuộc speculation + ranh giới bảo mật (security boundary / 보안 경계); persistence thuộc lưu trữ (storage / 저장소)/durability cross-layer.

Hardware-prefetch pathology tiếp tục được deepen trong bộ nhớ đệm (cache / 캐시) hierarchy trừ khi sau này xuất hiện một lập luận (reasoning / 추론) đường dẫn (path / 경로) đủ độc lập về predictor trạng thái (state / 상태), bandwidth pollution và cross-core interference. Power/thermal đã được tách vì nó có vòng điều khiển (control loop / 제어 루프), thời gian (time / 시간) constant và sustained-performance bất biến (invariant / 불변식) riêng.

Cross-layer paths bắt buộc: [CPU cache → language memory model → concurrency bug](../../90_connections/advanced/02_correctness_path_language_os_cpu_memory_ordering.md) và các hiệu năng (performance / 성능) đường dẫn (path / 경로) nối kiến trúc (architecture / 아키텍처) với [fleet profiling/cost attribution](../../08_software_systems/advanced/07_fleet_profiling_cost_attribution_and_multi_tenant_efficiency.md).