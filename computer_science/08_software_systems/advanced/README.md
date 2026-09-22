# Advanced Software Systems

Phần này tập trung vào behavior của hệ thống khi có queue, state, cache, failure, version skew, resource pressure và fleet-level resource economics. Không thêm chapter chỉ để liệt kê pattern hoặc infrastructure product mới.

## Canonical chapters

1. [Queueing, tail latency và backpressure](./00_queueing_tail_latency_and_backpressure.md)
2. [Capacity planning, utilization knee và admission control](./01_capacity_planning_utilization_knee_and_admission_control.md)
3. [Caching consistency, invalidation, stampede và hot keys](./02_caching_consistency_invalidation_stampede_and_hot_keys.md)
4. [Load balancing algorithms, connection pools và locality](./03_load_balancing_connection_pools_and_locality.md)
5. [Event streams: partitions, watermarks, replay và stateful processing](./04_event_streams_partitions_watermarks_replay_and_state.md)
6. [Idempotency architecture và deduplication at scale](./05_idempotency_and_deduplication_at_scale.md)
7. [Tiến hóa schema, protocol và hợp đồng tương thích](./06_schema_protocol_evolution_and_compatibility_contracts.md)
8. [Fleet profiling, cost attribution và multi-tenant efficiency](./07_fleet_profiling_cost_attribution_and_multi_tenant_efficiency.md)

## Mental models cần đạt

Track này phải giúp reasoning được các chuỗi như:

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

Ở fleet scale cần thêm:

```text
useful demand
→ distributed resource consumption
→ placement/skew/headroom
→ SLO outcome
→ cost attribution
→ capacity/architecture decision
```

Mỗi mechanism phải được đọc theo invariant mà nó bảo vệ. Queue bảo vệ bottleneck nào? Cache được phép stale tới mức nào? Idempotency key đại diện business operation nào? Schema evolution giữ compatibility qua overlap window ra sao? Fleet efficiency đang tối ưu resource nào dưới failure reserve và fairness constraint nào?

## System Design nằm trong reasoning này

System Design không được tách thành root library riêng. Service boundary, load balancing, pool sizing, cache topology, event processing, graceful degradation, multi-tenant isolation và fleet economics được học bằng cách nối các canonical chapters hiện có với [`09_software_engineering/advanced`](../../09_software_engineering/advanced/README.md) và [`06_networks_distributed_systems/advanced`](../../06_networks_distributed_systems/advanced/README.md).

Một design tốt bắt đầu từ invariant, workload và failure model; không bắt đầu từ danh sách technology.

## Production evidence

Khi hệ thống chậm hoặc không ổn định, phải đo arrival/completion rate, queue depth/wait, active concurrency, retry attempts, rejection/load shedding, cache hit/miss/hot-key distribution, pool wait, downstream saturation và trace critical path. Ở fleet scale cần giữ cohort theo region/version/hardware/shard/tenant đủ để không bị average che skew, nhưng tránh cardinality vô hạn.

Mục tiêu của observability là trả lời **work đang chờ ở đâu, resource nào giới hạn progress, state nào có thể stale/duplicate, feedback loop nào đang làm failure lan rộng, và cost nào đang tạo useful outcome**.

## Quy tắc mở rộng

Nếu một gap có thể được giải thích bằng cách đào sâu queue/capacity/cache/routing/event/idempotency/compatibility chapter hiện tại, không tạo file mới. Chỉ thêm conceptual unit khi thật sự có invariant và failure model độc lập không thể đặt hợp lý vào canonical boundary hiện có.