# Advanced Software Systems

Roadmap:

1. [Queueing, tail latency và backpressure](./00_queueing_tail_latency_and_backpressure.md)
2. [Capacity planning, utilization knee và admission control](./01_capacity_planning_utilization_knee_and_admission_control.md)
3. [Caching consistency, invalidation, stampede và hot keys](./02_caching_consistency_invalidation_stampede_and_hot_keys.md)
4. Load balancing algorithms, connection pools và locality
5. Event streams: partitions, watermarks, replay và stateful processing
6. Idempotency architecture và deduplication at scale
7. Schema/protocol evolution và compatibility contracts
8. Service boundaries, data ownership và distributed coupling
9. API gateways, sidecars/service mesh và failure propagation
10. Performance profiling across CPU, memory, I/O và network
11. Multi-tenant resource isolation và noisy-neighbor control
12. Graceful degradation, load shedding và overload recovery

Ba chapter đầu hình thành một cụm production-performance: queueing giải thích latency, capacity/admission giữ system trong safe envelope, cache thay đổi load path nhưng thêm consistency và failure modes mới.