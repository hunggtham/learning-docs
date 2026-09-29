# Advanced Software các hệ thống (systems / 시스템들)

> **Mạch đọc:** Đọc **Advanced Software các hệ thống (systems / 시스템들)** như một mắt xích của lộ trình học (learning path / 학습 경로) hiện tại, không như một ghi chú tách rời. Nội dung đi từ **chuẩn gốc (canonical / 정본) chapters** sang **mô hình tư duy (mental models / 사고 모델들) cần đạt**; điểm nối này chuẩn bị câu hỏi cho các mục sau thay vì dừng ở định nghĩa đầu tiên.


Phần này tập trung vào hành vi (behavior / 동작) của hệ thống khi có hàng đợi (queue / 큐), trạng thái (state / 상태), bộ nhớ đệm (cache / 캐시), thất bại (failure / 실패), phiên bản (version / 버전) skew, tài nguyên (resource / 자원) pressure và fleet-level tài nguyên (resource / 자원) economics. Không thêm chapter chỉ để liệt kê mẫu (pattern / 패턴) hoặc hạ tầng (infrastructure / 인프라) sản phẩm (product / 제품) mới.

## Chuẩn gốc (canonical / 정본) chapters

1. [Queueing, tail latency và backpressure](./00_queueing_tail_latency_and_backpressure.md)
2. [Capacity planning, utilization knee và admission control](./01_capacity_planning_utilization_knee_and_admission_control.md)
3. [Caching consistency, invalidation, stampede và hot keys](./02_caching_consistency_invalidation_stampede_and_hot_keys.md)
4. [Load balancing algorithms, connection pools và locality](./03_load_balancing_connection_pools_and_locality.md)
5. [Event streams: partitions, watermarks, replay và stateful processing](./04_event_streams_partitions_watermarks_replay_and_state.md)
6. [Idempotency architecture và deduplication at scale](./05_idempotency_and_deduplication_at_scale.md)
7. [Tiến hóa schema, protocol và hợp đồng tương thích](./06_schema_protocol_evolution_and_compatibility_contracts.md)
8. [Fleet profiling, cost attribution và multi-tenant efficiency](./07_fleet_profiling_cost_attribution_and_multi_tenant_efficiency.md)


> **Chuyển mạch:** Từ **chuẩn gốc (canonical / 정본) chapters**, ta sang **mô hình tư duy (mental models / 사고 모델들) cần đạt** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## Mô hình tư duy (mental models / 사고 모델들) cần đạt

Nhánh học (track / 트랙) này phải giúp lập luận (reasoning / 추론) được các chuỗi như:

```text
arrival rate
→ queue
→ saturation
→ timeout
→ retry
→ overload amplification
```

và:

```text
state/cache/event
→ version visibility
→ invalidation/replay
→ duplicate/reordering
→ consistency failure
```

Ở fleet quy mô (scale / 규모) cần thêm:

```text
useful demand
→ distributed resource consumption
→ placement/skew/headroom
→ SLO outcome
→ cost attribution
→ capacity/architecture decision
```

Mỗi cơ chế (mechanism / 메커니즘) phải được đọc theo bất biến (invariant / 불변식) mà nó bảo vệ. hàng đợi (queue / 큐) bảo vệ bottleneck nào? bộ nhớ đệm (cache / 캐시) được phép stale tới mức nào? Idempotency key đại diện nghiệp vụ (business / 비즈니스) thao tác (operation / 연산) nào? lược đồ (schema / 스키마) evolution giữ tính tương thích (compatibility / 호환성) qua overlap cửa sổ (window / 윈도우) ra sao? Fleet efficiency đang tối ưu tài nguyên (resource / 자원) nào dưới thất bại (failure / 실패) reserve và fairness ràng buộc (constraint / 제약조건) nào?


> **Chuyển mạch:** Từ **mô hình tư duy (mental models / 사고 모델들) cần đạt**, ta sang **hệ thống (system / 시스템) thiết kế (design / 설계) nằm trong lập luận (reasoning / 추론) này** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## Hệ thống (system / 시스템) thiết kế (design / 설계) nằm trong lập luận (reasoning / 추론) này

Hệ thống (system / 시스템) thiết kế (design / 설계) không được tách thành gốc (root / 루트) thư viện (library / 라이브러리) riêng. dịch vụ (service / 서비스) ranh giới (boundary / 경계), tải (load / 로드) balancing, pool sizing, bộ nhớ đệm (cache / 캐시) topology, sự kiện (event / 이벤트) processing, graceful degradation, multi-tenant isolation và fleet economics được học bằng cách nối các chuẩn gốc (canonical / 정본) chapters hiện có với [`09_software_engineering/advanced`](../../09_software_engineering/advanced/README.md) và [`06_networks_distributed_systems/advanced`](../../06_networks_distributed_systems/advanced/README.md).

Một thiết kế (design / 설계) tốt bắt đầu từ bất biến (invariant / 불변식), tải công việc (workload / 워크로드) và thất bại (failure / 실패) mô hình (model / 모델); không bắt đầu từ danh sách technology.


> **Chuyển mạch:** Từ **hệ thống (system / 시스템) thiết kế (design / 설계) nằm trong lập luận (reasoning / 추론) này**, ta sang **bằng chứng vận hành (production evidence / 운영 증거)** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## Bằng chứng vận hành (production evidence / 운영 증거)

Khi hệ thống chậm hoặc không ổn định, phải đo arrival/completion tỷ lệ (rate / 비율), hàng đợi (queue / 큐) độ sâu (depth / 깊이)/wait, active tính đồng thời (concurrency / 동시성), thử lại (retry / 재시도) attempts, rejection/tải (load / 로드) shedding, bộ nhớ đệm (cache / 캐시) hit/miss/hot-key phân phối (distribution / 분포), pool wait, downstream saturation và dấu vết (trace / 추적) đường găng (critical path / 임계 경로). Ở fleet quy mô (scale / 규모) cần giữ cohort theo region/phiên bản (version / 버전)/hardware/shard/tenant đủ để không bị average che skew, nhưng tránh cardinality vô hạn.

Mục tiêu của khả năng quan sát (observability / 관측 가능성) là trả lời **công việc (work / 작업) đang chờ ở đâu, tài nguyên (resource / 자원) nào giới hạn progress, trạng thái (state / 상태) nào có thể stale/duplicate, vòng phản hồi (feedback loop / 피드백 루프) nào đang làm thất bại (failure / 실패) lan rộng, và chi phí (cost / 비용) nào đang tạo useful kết quả (outcome / 결과)**.


> **Chuyển mạch:** Từ **bằng chứng vận hành (production evidence / 운영 증거)**, ta sang **Quy tắc mở rộng** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## Quy tắc mở rộng

Nếu một gap có thể được giải thích bằng cách đào sâu hàng đợi (queue / 큐)/sức chứa (capacity / 용량)/bộ nhớ đệm (cache / 캐시)/routing/sự kiện (event / 이벤트)/idempotency/tính tương thích (compatibility / 호환성) chapter hiện tại, không tạo tệp (file / 파일) mới. Chỉ thêm conceptual đơn vị (unit / 단위) khi thật sự có bất biến (invariant / 불변식) và thất bại (failure / 실패) mô hình (model / 모델) độc lập không thể đặt hợp lý vào chuẩn gốc (canonical / 정본) ranh giới (boundary / 경계) hiện có.

> **Bàn giao:** Sau **Quy tắc mở rộng**, hãy chốt bất biến (invariant / 불변식) và giới hạn của mục này trước khi nối sang kiến thức kế tiếp. Có thể đọc tiếp [00 queueing tail latency and backpressure](./00_queueing_tail_latency_and_backpressure.md) để đối chiếu ranh giới (boundary / 경계) gần nhất.
