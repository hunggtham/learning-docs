# 90_connections

> **Mạch đọc:** [README](../README.md) là bản đồ owner của **90connections**; nhìn vào vị trí đó trước để biết file này đang phục vụ nhánh kiến thức nào. **Các chương tổng hợp** gom các mảnh thành mental model có thể mang sang nhánh khác; sau đó sang **Trường hợp (case / 사례) study xuyên nhiều chapter** để đem mô hình vào tình huống cụ thể. Mạch này dùng index của advanced connections làm bản đồ owner, rồi nối từng case với cấu trúc, thuật toán và hệ thống sử dụng nó.

Nhóm này nối các khái niệm DSA riêng lẻ thành quyết định thiết kế và hệ thống hoàn chỉnh. Nên đọc sau khi đã có nền tảng về cấu trúc tuyến tính, cây, đồ thị và các mô hình thuật toán chính.

## Các chương tổng hợp

Phần này chuyển khái niệm Computer Science thành cấu trúc, ví dụ hoặc quy trình có thể kiểm tra. Hãy xác định câu hỏi mà mục trả lời rồi nối kết luận với phần kế tiếp.

- [Chọn cấu trúc dữ liệu phù hợp](./00_choose_the_right_data_structure.md) — chuyển workload thành tiêu chí lựa chọn representation, invariant và cost model.
- [DSA trong cơ sở dữ liệu, mạng và hệ thống](./01_dsa_in_databases_networks_and_systems.md) — cách B+Tree, Hash Table, Heap, Graph, Trie và sketch xuất hiện trong hệ thống thực tế.
- [Workflow giải bài và thiết kế thuật toán](./02_problem_solving_workflow.md) — specification → modeling → invariant → baseline → optimization → proof → testing → production hardening.

Phần này chuyển khái niệm Computer Science thành cấu trúc, ví dụ hoặc quy trình có thể kiểm tra. Hãy xác định câu hỏi mà mục trả lời rồi nối kết luận với phần kế tiếp.

- [Database Indexing](./03_case_study_database_indexing.md) — Hash Index, B+Tree, Buffer Pool, Bloom Filter, LSM, Join và crash consistency.
- [Autocomplete & Search Suggestions](./04_case_study_autocomplete_search.md) — Trie/FST, Top-K Heap, ranking, Unicode, fuzzy search, cache và distributed merge.
- [Routing System](./05_case_study_routing_graph_system.md) — Graph representation, Dijkstra, Priority Queue, dynamic topology, longest-prefix match, ECMP và failover.
- [Streaming Analytics](./06_case_study_streaming_analytics.md) — Hash Map, Count-Min Sketch, HyperLogLog, heavy hitters, quantile sketch, windows và distributed state.
- [Scheduler & Backpressure](./07_case_study_scheduler_backpressure.md) — Queue/Deque/Priority Queue, fairness, aging, work stealing, bounded queue, retry và admission control.

> **Chuyển mạch:** Trong **90connections**, **Các chương tổng hợp** cho ta quy tắc; **Trường hợp (case / 사례) study xuyên nhiều chapter** đặt quy tắc ấy vào tình huống cụ thể để thấy nó hoạt động đến đâu. Từ đây, **Cách dùng các trường hợp (case / 사례) study** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Trường hợp (case / 사례) study xuyên nhiều chapter

- [Database Indexing](./03_case_study_database_indexing.md) — băm (hash / 해시) chỉ mục (index / 인덱스), B+cây (tree / 트리), Buffer Pool, Bloom Filter, LSM, phép nối (join / 조인) và crash consistency.
- [Autocomplete & Search Suggestions](./04_case_study_autocomplete_search.md) — Trie/FST, Top-K vùng nhớ động (heap / 힙), ranking, Unicode, fuzzy tìm kiếm (search / 검색), bộ nhớ đệm (cache / 캐시) và phân tán (distributed / 분산) merge.
- [Routing System](./05_case_study_routing_graph_system.md) — đồ thị (graph / 그래프) biểu diễn (representation / 표현), Dijkstra, Priority hàng đợi (queue / 큐), động (dynamic / 동적) topology, longest-prefix match, ECMP và failover.
- [Streaming Analytics](./06_case_study_streaming_analytics.md) — băm (hash / 해시) Map, Count-Min Sketch, HyperLogLog, heavy hitters, quantile sketch, windows và phân tán (distributed / 분산) trạng thái (state / 상태).
- [Scheduler & Backpressure](./07_case_study_scheduler_backpressure.md) — hàng đợi (queue / 큐)/Deque/Priority hàng đợi (queue / 큐), fairness, aging, công việc (work / 작업) stealing, bounded hàng đợi (queue / 큐), thử lại (retry / 재시도) và admission điều khiển (control / 제어).

> **Chuyển mạch:** Ở chặng này của **90connections**, **Trường hợp (case / 사례) study xuyên nhiều chapter** cho ta quy tắc; **Cách dùng các trường hợp (case / 사례) study** đặt quy tắc ấy vào tình huống cụ thể để thấy nó hoạt động đến đâu. Phần còn lại của file dùng kết quả này để khép lại mạch giải thích.

## Cách dùng các trường hợp (case / 사례) study

Mỗi trường hợp (case / 사례) study nên được đọc theo hai lượt. Lượt đầu tập trung vào câu hỏi **“vì sao hệ thống cần nhiều cấu trúc cùng lúc?”**. Lượt sau quay lại các chapter được liên kết để kiểm tra từng bất biến, độ phức tạp (complexity / 복잡도) và dạng thất bại (failure mode / 실패 모드) chi tiết.

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

> **Bàn giao:** Sau **Cách dùng các trường hợp (case / 사례) study**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](../README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
