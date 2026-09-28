# 02_trees

> **Mạch đọc:** Đọc **02trees** như một mắt xích của lộ trình học (learning path / 학습 경로) hiện tại, không như một ghi chú tách rời. Hãy xác định đối tượng và câu hỏi trung tâm trước, rồi dùng phần này để đối chiếu với mục liên quan sau khi đã nắm mô hình tư duy (mental model / 사고 모델) chính.


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

> **Bàn giao:** Sau **02trees**, hãy chốt bất biến (invariant / 불변식) và giới hạn của mục này trước khi nối sang kiến thức kế tiếp. Có thể đọc tiếp [00 tree foundations](./00_tree_foundations.md) để đối chiếu ranh giới (boundary / 경계) gần nhất.
