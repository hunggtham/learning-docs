# Algorithms & Data Structures — Computer Science Foundations

Thư mục này là phần **kiến thức nền tảng của Computer Science** về Thuật toán và Cấu trúc dữ liệu (Algorithms & Data Structures / 알고리즘과 자료구조). Các chapter ở cấp thư mục hiện tại được viết để xây mental model cốt lõi trước: thuật toán là gì, tính đúng đắn được reasoning như thế nào, độ phức tạp biểu diễn growth ra sao, dữ liệu được tổ chức trong memory thế nào, và những family cấu trúc/thuật toán chính liên hệ với nhau ra sao.

Mục tiêu của phần foundation không phải cover mọi biến thể chuyên sâu. Nó tạo một bản đồ đủ chắc để khi gặp array, hash table, tree, graph, sorting, dynamic programming hoặc randomized algorithm, người đọc hiểu vấn đề mà chúng giải quyết và biết nên đào sâu ở đâu.

## Foundation và Advanced được tách như thế nào?

Các file `.md` nằm trực tiếp trong thư mục này là **foundation chapters**. Chúng ưu tiên bức tranh tổng thể, terminology, first principles và connection giữa các chủ đề Computer Science.

Thư mục [`advanced/`](./advanced/README.md) là **Knowledge Library DSA chuyên sâu**. Phần đó phân rã domain theo conceptual boundary thành nhiều chapter riêng, đi sâu vào invariant, proof, implementation, complexity, edge cases và runtime behavior bằng **C, Java và JavaScript**.

Sự phân chia này không có nghĩa kiến thức foundation là “dễ” còn advanced là một level cố định. Nó mô tả vai trò của hai lớp tài liệu:

```text
Computer Science foundation
        ↓
mental model + vocabulary + big picture
        ↓
Advanced DSA Knowledge Library
        ↓
implementation + proof + specialized structures + system connections
```

## Các chapter nền tảng

| Chapter | Vai trò trong foundation |
|---|---|
| [00 — Algorithmic Thinking & Correctness](./00_algorithmic_thinking_and_correctness.md) | Xây cách nhìn problem → algorithm → invariant → correctness. |
| [01 — Complexity & Asymptotic Analysis](./01_complexity_and_asymptotic_analysis.md) | Hiểu time/space complexity và cách growth thay đổi theo input. |
| [02 — Memory Models & Data Layout](./02_memory_models_and_data_layout.md) | Nối abstraction DSA với memory, locality, references và representation. |
| [03 — Linear Data Structures](./03_linear_data_structures.md) | Array, list, stack, queue và các trade-off tuyến tính cơ bản. |
| [04 — Hashing & Hash Tables](./04_hashing_and_hash_tables.md) | Exact-key lookup, collision và hashing model. |
| [05 — Trees, Heaps & Search Structures](./05_trees_heaps_and_search_structures.md) | Hierarchy, ordered search và priority structures. |
| [06 — Graphs & Graph Algorithms](./06_graphs_and_graph_algorithms.md) | Modeling relationship, traversal, paths và connectivity. |
| [07 — Sorting, Searching & Selection](./07_sorting_searching_and_selection.md) | Order, search-space reduction và selection problems. |
| [08 — Algorithmic Strategies](./08_algorithmic_strategies.md) | Recursion, divide-and-conquer, greedy, dynamic programming và backtracking. |
| [09 — String Algorithms & Text Indexing](./09_string_algorithms_and_text_indexing.md) | Sequence/prefix/pattern ideas trong text processing. |
| [10 — Randomized, Approximation & Online Algorithms](./10_randomized_approximation_and_online_algorithms.md) | Mở rộng deterministic model sang randomness, approximation và streaming/online decisions. |

Foundation nên được đọc như một **bản đồ Computer Science có chiều sâu vừa đủ**. Nếu một chủ đề ở đây trở thành trọng tâm học tập hoặc công việc, hãy chuyển sang chapter chuyên sâu tương ứng trong [`advanced/`](./advanced/README.md).

## Khi nào nên chuyển sang Advanced?

Khi đã hiểu các câu hỏi sau, bạn có thể chuyển sang phần chuyên sâu mà không bị biến thành học thuộc implementation:

```text
Vì sao representation quyết định cost của operation?
Vì sao một invariant có thể làm search nhanh hơn?
Big-O đang đo growth nào và không nói được điều gì?
Array, hash table, tree và graph khác nhau ở mental model nào?
Recursion, greedy và DP khác nhau ở cách tổ chức state/search space ra sao?
```

Nếu một câu hỏi vẫn mơ hồ, hãy quay lại chapter foundation tương ứng. Nếu đã rõ nhưng muốn biết “implementation thực sự hoạt động thế nào, proof ra sao, có biến thể nào, dùng trong production thế nào”, đó chính là phạm vi của Advanced DSA.

## Liên kết sang Knowledge Library chuyên sâu

Bắt đầu tại:

**[Advanced Data Structures & Algorithms Knowledge Library](./advanced/README.md)**

Phần advanced bao gồm không chỉ array/tree/graph/DP mà còn B/B+Tree, augmented tree, skip list, flow/matching, suffix structures, Fenwick/Segment Tree, sparse table, probabilistic data structures, reduction/NP reasoning và các chapter riêng về implementation trong C, Java và JavaScript.
