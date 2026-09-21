# Advanced Software Systems

Roadmap:

1. [Queueing, tail latency và backpressure](./00_queueing_tail_latency_and_backpressure.md)
2. [Capacity planning, utilization knee và admission control](./01_capacity_planning_utilization_knee_and_admission_control.md)
3. [Caching consistency, invalidation, stampede và hot keys](./02_caching_consistency_invalidation_stampede_and_hot_keys.md)
4. [Load balancing algorithms, connection pools và locality](./03_load_balancing_connection_pools_and_locality.md)
5. [Event streams: partitions, watermarks, replay và stateful processing](./04_event_streams_partitions_watermarks_replay_and_state.md)
6. [Idempotency architecture và deduplication at scale](./05_idempotency_and_deduplication_at_scale.md)
7. [Tiến hóa schema, protocol và hợp đồng tương thích](./06_schema_protocol_evolution_and_compatibility_contracts.md)
8. Service boundaries, data ownership và distributed coupling
9. API gateways, sidecars/service mesh và failure propagation
10. Performance profiling across CPU, memory, I/O và network
11. Multi-tenant resource isolation và noisy-neighbor control
12. Graceful degradation, load shedding và overload recovery

Bảy chapter đầu tạo production model từ queue/capacity/cache tới routing, event processing, reliable side effects và khả năng tiến hóa hệ thống khi nhiều version chạy đồng thời. Schema evolution được xem như distributed protocol theo thời gian, không chỉ là thao tác đổi database column hay JSON field.

Phần tiếp theo ưu tiên service/data ownership và coupling trước khi đi sâu topology, profiling và resilience.