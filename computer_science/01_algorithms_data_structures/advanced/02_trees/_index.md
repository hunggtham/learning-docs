# 02_trees

> **Mạch đọc:** [README](../README.md) là bản đồ owner của **02trees**; nhìn vào vị trí đó trước để biết file này đang phục vụ nhánh kiến thức nào. Bắt đầu ở **02trees** để mở đối tượng chính của file và câu hỏi cần theo dõi, rồi dùng kết luận đó khi quay về lộ trình rộng hơn.

Nhóm này đi từ nền tảng về cây tới các cấu trúc có thứ tự và cấu trúc ưu tiên.

- `00_tree_foundations.md` — cấu trúc cây, traversal, subtree/đường dẫn (path / 경로), LCA, cây (tree / 트리) DP, Euler Tour và các kỹ thuật nền.
- `01_binary_search_trees.md` — bất biến thứ tự của BST và các thao tác tìm kiếm/chèn/xóa.
- `02_balanced_search_trees.md` — AVL, Red-Black, Treap, Splay, Scapegoat, split/phép nối (join / 조인), persistence và tính đồng thời (concurrency / 동시성).
- `03_heaps.md` — vùng nhớ động (heap / 힙) nhị phân và hàng đợi ưu tiên từ bất biến cơ bản tới Top-K/Dijkstra/scheduler.
- `04_tries.md` — Trie, Radix/Patricia, FST, double-array/succinct biểu diễn (representation / 표현) và autocomplete.
- `05_b_trees_and_external_memory.md` — B/B+cây (tree / 트리) và mô hình chi phí theo page/I/O.
- `06_augmented_trees_and_order_statistics.md` — cây tăng cường, rank, k-th, interval siêu dữ liệu (metadata / 메타데이터) và thứ tự (order / 순서) statistics.
- `07_skip_lists.md` — cấu trúc có thứ tự dựa trên ngẫu nhiên hóa.
- `08_advanced_heaps_and_priority_queue_engineering.md` — Indexed/D-ary/Binomial/Fibonacci/Pairing/Leftist/Skew/Radix vùng nhớ động (heap / 힙), monotone hàng đợi (queue / 큐), concurrent và external-memory priority hàng đợi (queue / 큐).

`05_b_trees_and_external_memory.md` được tách riêng vì lưu trữ theo trang tạo một mô hình chi phí khác BST trong RAM. `08_advanced_heaps_and_priority_queue_engineering.md` được đặt sau phần vùng nhớ động (heap / 힙) cơ bản để mở rộng từ ADT `PriorityQueue` sang lựa chọn cấu trúc theo tải công việc (workload / 워크로드) thực tế.

> **Bàn giao:** Sau **02trees**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](../README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
