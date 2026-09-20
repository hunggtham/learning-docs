# 02_trees

Nhóm này đi từ nền tảng về cây tới các cấu trúc có thứ tự và cấu trúc ưu tiên.

- `00_tree_foundations.md` — cấu trúc cây, traversal, subtree/path, LCA, tree DP, Euler Tour và các kỹ thuật nền.
- `01_binary_search_trees.md` — bất biến thứ tự của BST và các thao tác tìm kiếm/chèn/xóa.
- `02_balanced_search_trees.md` — AVL, Red-Black, Treap, Splay, Scapegoat, split/join, persistence và concurrency.
- `03_heaps.md` — heap nhị phân và hàng đợi ưu tiên từ bất biến cơ bản tới Top-K/Dijkstra/scheduler.
- `04_tries.md` — Trie, Radix/Patricia, FST, double-array/succinct representation và autocomplete.
- `05_b_trees_and_external_memory.md` — B/B+Tree và mô hình chi phí theo page/I/O.
- `06_augmented_trees_and_order_statistics.md` — cây tăng cường, rank, k-th, interval metadata và order statistics.
- `07_skip_lists.md` — cấu trúc có thứ tự dựa trên ngẫu nhiên hóa.
- `08_advanced_heaps_and_priority_queue_engineering.md` — Indexed/D-ary/Binomial/Fibonacci/Pairing/Leftist/Skew/Radix Heap, monotone queue, concurrent và external-memory priority queue.

`05_b_trees_and_external_memory.md` được tách riêng vì lưu trữ theo trang tạo một mô hình chi phí khác BST trong RAM. `08_advanced_heaps_and_priority_queue_engineering.md` được đặt sau phần heap cơ bản để mở rộng từ ADT `PriorityQueue` sang lựa chọn cấu trúc theo workload thực tế.