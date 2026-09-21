# 90_connections

Nhóm này nối các khái niệm DSA riêng lẻ thành quyết định thiết kế và hệ thống hoàn chỉnh. Nên đọc sau khi đã có nền tảng về cấu trúc tuyến tính, cây, đồ thị và các mô hình thuật toán chính.

## Các chương tổng hợp

- [Chọn cấu trúc dữ liệu phù hợp](./00_choose_the_right_data_structure.md) — chuyển workload thành tiêu chí lựa chọn representation, invariant và cost model.
- [DSA trong cơ sở dữ liệu, mạng và hệ thống](./01_dsa_in_databases_networks_and_systems.md) — cách B+Tree, Hash Table, Heap, Graph, Trie và sketch xuất hiện trong hệ thống thực tế.
- [Workflow giải bài và thiết kế thuật toán](./02_problem_solving_workflow.md) — specification → modeling → invariant → baseline → optimization → proof → testing → production hardening.

## Case study xuyên nhiều chapter

- [Database Indexing](./03_case_study_database_indexing.md) — Hash Index, B+Tree, Buffer Pool, Bloom Filter, LSM, Join và crash consistency.
- [Autocomplete & Search Suggestions](./04_case_study_autocomplete_search.md) — Trie/FST, Top-K Heap, ranking, Unicode, fuzzy search, cache và distributed merge.
- [Routing System](./05_case_study_routing_graph_system.md) — Graph representation, Dijkstra, Priority Queue, dynamic topology, longest-prefix match, ECMP và failover.
- [Streaming Analytics](./06_case_study_streaming_analytics.md) — Hash Map, Count-Min Sketch, HyperLogLog, heavy hitters, quantile sketch, windows và distributed state.
- [Scheduler & Backpressure](./07_case_study_scheduler_backpressure.md) — Queue/Deque/Priority Queue, fairness, aging, work stealing, bounded queue, retry và admission control.

## Cách dùng các case study

Mỗi case study nên được đọc theo hai lượt. Lượt đầu tập trung vào câu hỏi **“vì sao hệ thống cần nhiều cấu trúc cùng lúc?”**. Lượt sau quay lại các chapter được liên kết để kiểm tra từng bất biến, complexity và failure mode chi tiết.

Mục tiêu của nhóm này không phải học thêm tên thuật toán, mà là luyện khả năng:

```text
requirement
→ workload
→ state
→ invariant
→ data structure / algorithm
→ composition
→ system cost
→ testing / observability
```
