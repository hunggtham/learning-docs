# 90_connections

> **Mạch đọc:** Đọc **90connections** như một mắt xích của lộ trình học (learning path / 학습 경로) hiện tại, không như một ghi chú tách rời. Nội dung đi từ **Các chương tổng hợp** sang **trường hợp (case / 사례) study xuyên nhiều chapter**; điểm nối này chuẩn bị câu hỏi cho các mục sau thay vì dừng ở định nghĩa đầu tiên.


Nhóm này nối các khái niệm DSA riêng lẻ thành quyết định thiết kế và hệ thống hoàn chỉnh. Nên đọc sau khi đã có nền tảng về cấu trúc tuyến tính, cây, đồ thị và các mô hình thuật toán chính.

## Các chương tổng hợp

- [Chọn cấu trúc dữ liệu phù hợp](./00_choose_the_right_data_structure.md) — chuyển tải công việc (workload / 워크로드) thành tiêu chí lựa chọn biểu diễn (representation / 표현), bất biến (invariant / 불변식) và chi phí (cost / 비용) mô hình (model / 모델).
- [DSA trong cơ sở dữ liệu, mạng và hệ thống](./01_dsa_in_databases_networks_and_systems.md) — cách B+cây (tree / 트리), bảng băm (hash table / 해시 테이블), vùng nhớ động (heap / 힙), đồ thị (graph / 그래프), Trie và sketch xuất hiện trong hệ thống thực tế.
- [Workflow giải bài và thiết kế thuật toán](./02_problem_solving_workflow.md) — specification → modeling → bất biến (invariant / 불변식) → baseline → tối ưu hóa (optimization / 최적화) → proof → testing → môi trường vận hành (production / 운영 환경) hardening.


> **Chuyển mạch:** Từ **Các chương tổng hợp**, ta sang **trường hợp (case / 사례) study xuyên nhiều chapter** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## Trường hợp (case / 사례) study xuyên nhiều chapter

- [Database Indexing](./03_case_study_database_indexing.md) — băm (hash / 해시) chỉ mục (index / 인덱스), B+cây (tree / 트리), Buffer Pool, Bloom Filter, LSM, phép nối (join / 조인) và crash consistency.
- [Autocomplete & Search Suggestions](./04_case_study_autocomplete_search.md) — Trie/FST, Top-K vùng nhớ động (heap / 힙), ranking, Unicode, fuzzy tìm kiếm (search / 검색), bộ nhớ đệm (cache / 캐시) và phân tán (distributed / 분산) merge.
- [Routing System](./05_case_study_routing_graph_system.md) — đồ thị (graph / 그래프) biểu diễn (representation / 표현), Dijkstra, Priority hàng đợi (queue / 큐), động (dynamic / 동적) topology, longest-prefix match, ECMP và failover.
- [Streaming Analytics](./06_case_study_streaming_analytics.md) — băm (hash / 해시) Map, Count-Min Sketch, HyperLogLog, heavy hitters, quantile sketch, windows và phân tán (distributed / 분산) trạng thái (state / 상태).
- [Scheduler & Backpressure](./07_case_study_scheduler_backpressure.md) — hàng đợi (queue / 큐)/Deque/Priority hàng đợi (queue / 큐), fairness, aging, công việc (work / 작업) stealing, bounded hàng đợi (queue / 큐), thử lại (retry / 재시도) và admission điều khiển (control / 제어).


> **Chuyển mạch:** Từ **trường hợp (case / 사례) study xuyên nhiều chapter**, ta sang **Cách dùng các trường hợp (case / 사례) study** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

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

> **Bàn giao:** Sau **Cách dùng các trường hợp (case / 사례) study**, hãy chốt bất biến (invariant / 불변식) và giới hạn của mục này trước khi nối sang kiến thức kế tiếp. Có thể đọc tiếp [00 choose the right data structure](./00_choose_the_right_data_structure.md) để đối chiếu ranh giới (boundary / 경계) gần nhất.
