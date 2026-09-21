# Kết nối xuyên tầng nâng cao

Roadmap:

1. [Gỡ lỗi xuyên các tầng abstraction](./00_debugging_across_abstraction_layers.md)
2. [Độ trễ end-to-end: browser → edge → service → DB → storage](./01_end_to_end_latency_browser_edge_service_db_storage.md)
3. [Đường correctness: language memory model → OS → CPU ordering](./02_correctness_path_language_os_cpu_memory_ordering.md)
4. [Đường durability: application commit → WAL → filesystem → device](./03_durability_path_application_commit_wal_filesystem_device.md)
5. Đường identity: browser session → gateway → service → database authorization
6. Đường overload: retry → queue → pool → database saturation
7. Đường nhất quán dữ liệu: transaction → event → replica → cache
8. Đường performance: allocation → GC → scheduler → cache/TLB → NUMA
9. Phân tích incident bằng timeline, causal graph và mức tin cậy của evidence
10. Thiết kế observability tại các boundary giữa abstraction

Các chapter cross-domain không lặp lại từng domain. Chúng bắt đầu từ một thuộc tính end-to-end hoặc triệu chứng production rồi đi xuyên hardware, OS, runtime, application, network và storage để xây causal model. Bốn chapter hiện có bao phủ debugging, latency, concurrent correctness và durability.