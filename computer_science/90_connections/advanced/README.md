# Advanced Cross-domain Connections

Roadmap:

1. [Debugging xuyên abstraction layers](./00_debugging_across_abstraction_layers.md)
2. [End-to-end latency: browser → edge → service → DB → storage](./01_end_to_end_latency_browser_edge_service_db_storage.md)
3. Correctness path: language memory model → OS → CPU ordering
4. Durability path: application commit → WAL → filesystem → device
5. Identity path: browser session → gateway → service → database authorization
6. Overload path: retries → queues → pools → database saturation
7. Data consistency path: transaction → event → replica → cache
8. Performance path: allocation → GC → scheduler → cache/TLB → NUMA
9. Incident reasoning with timelines, causal graphs và evidence confidence
10. Designing observability at abstraction boundaries

Cross-domain chapters không lặp lại từng domain. Chúng dùng một production symptom hoặc correctness path để nối các abstraction layers thành causal model.