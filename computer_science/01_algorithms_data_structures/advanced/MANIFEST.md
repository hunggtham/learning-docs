# Advanced DSA File Manifest

Manifest này theo dõi thư viện `computer_science/01_algorithms_data_structures/advanced/`. Số từ chỉ là **ước lượng để kiểm tra độ phủ**, không phải tiêu chí chất lượng duy nhất.

Một chapter được xem là đủ sâu khi, tùy chủ đề, nó bao phủ chuỗi:

```text
bản chất vấn đề
→ mô hình tư duy
→ cách biểu diễn
→ bất biến / chứng minh
→ độ phức tạp và loại bảo đảm
→ cách triển khai
→ edge cases / failure modes
→ kiểm thử / benchmark
→ liên hệ hệ thống thực tế
```

Phần giải thích dùng tiếng Việt làm ngôn ngữ chính; thuật ngữ Anh/Hàn được giữ như keyword bổ trợ khi hữu ích. Code, API, class/function name và tên thuật toán chuẩn không bị dịch máy móc.

## Độ phủ hiện tại

| File | Approx. words |
|---|---:|
| `00_foundations/00_dsa_as_problem_modeling.md` | ~4,800 |
| `00_foundations/01_algorithm_correctness_and_invariants.md` | ~5,000 |
| `00_foundations/02_complexity_analysis.md` | ~3,300 |
| `00_foundations/03_memory_models_c_java_javascript.md` | ~3,300 |
| `00_foundations/04_mathematical_toolkit_for_dsa.md` | ~4,800 |
| `01_linear_structures/00_arrays_and_dynamic_arrays.md` | ~3,400 |
| `01_linear_structures/01_linked_lists.md` | ~3,200 |
| `01_linear_structures/02_stacks.md` | ~3,100 |
| `01_linear_structures/03_queues_deques_and_priority_queues.md` | ~4,800 |
| `01_linear_structures/04_hash_tables.md` | ~5,300 |
| `02_trees/00_tree_foundations.md` | ~3,200 |
| `02_trees/01_binary_search_trees.md` | ~3,000 |
| `02_trees/02_balanced_search_trees.md` | ~3,600 |
| `02_trees/03_heaps.md` | ~2,700 |
| `02_trees/04_tries.md` | ~3,500 |
| `02_trees/05_b_trees_and_external_memory.md` | ~3,500 |
| `02_trees/06_augmented_trees_and_order_statistics.md` | ~3,100 |
| `02_trees/07_skip_lists.md` | ~3,300 |
| `02_trees/08_advanced_heaps_and_priority_queue_engineering.md` | ~3,300 |
| `03_graphs/00_graph_modeling_and_representation.md` | ~2,700 |
| `03_graphs/01_graph_traversal_bfs_dfs.md` | ~3,200 |
| `03_graphs/02_shortest_paths.md` | ~3,200 |
| `03_graphs/03_minimum_spanning_trees.md` | ~3,100 |
| `03_graphs/04_dag_topological_sort_and_scc.md` | ~2,900 |
| `03_graphs/05_union_find.md` | ~2,800 |
| `03_graphs/06_bridges_articulation_and_biconnectivity.md` | ~3,300 |
| `03_graphs/07_eulerian_paths_and_cycles.md` | ~3,200 |
| `03_graphs/08_network_flow_and_matching.md` | ~3,600 |
| `03_graphs/09_dynamic_temporal_and_large_scale_graphs.md` | ~3,300 |
| `04_algorithmic_paradigms/00_searching.md` | ~3,000 |
| `04_algorithmic_paradigms/01_sorting.md` | ~4,800 |
| `04_algorithmic_paradigms/02_recursion_and_backtracking.md` | ~2,900 |
| `04_algorithmic_paradigms/03_divide_and_conquer.md` | ~3,600 |
| `04_algorithmic_paradigms/04_greedy_algorithms.md` | ~2,700 |
| `04_algorithmic_paradigms/05_dynamic_programming.md` | ~4,500 |
| `04_algorithmic_paradigms/06_selection_and_top_k.md` | ~3,500 |
| `04_algorithmic_paradigms/07_two_pointers_sliding_window_prefix_difference.md` | ~4,000 |
| `04_algorithmic_paradigms/08_intervals_and_sweep_line.md` | ~3,300 |
| `04_algorithmic_paradigms/09_hard_problems_reductions_and_approximation.md` | ~5,000 |
| `04_algorithmic_paradigms/10_greedy_matroids_primal_dual_and_approximation.md` | ~3,200 |
| `04_algorithmic_paradigms/11_constraint_search_branch_and_bound.md` | ~3,900 |
| `05_specialized/00_string_algorithms.md` | ~3,100 |
| `05_specialized/01_range_queries_fenwick_segment_tree.md` | ~3,200 |
| `05_specialized/02_bit_manipulation_and_bitsets.md` | ~3,000 |
| `05_specialized/03_amortized_randomized_and_probabilistic_thinking.md` | ~3,300 |
| `05_specialized/04_suffix_arrays_suffix_trees_and_lcp.md` | ~3,600 |
| `05_specialized/05_sparse_table_and_static_range_queries.md` | ~3,000 |
| `05_specialized/06_probabilistic_data_structures.md` | ~4,600 |
| `80_language_implementations/00_c_dsa_implementation_patterns.md` | ~3,500 |
| `80_language_implementations/01_java_collections_and_dsa.md` | ~3,700 |
| `80_language_implementations/02_javascript_dsa_runtime_patterns.md` | ~4,200 |
| `80_language_implementations/03_cross_language_testing_and_benchmarking.md` | ~4,300 |
| `90_connections/00_choose_the_right_data_structure.md` | ~3,200 |
| `90_connections/01_dsa_in_databases_networks_and_systems.md` | ~4,000 |
| `90_connections/02_problem_solving_workflow.md` | ~3,300 |
| `90_connections/03_case_study_database_indexing.md` | ~2,500 |
| `90_connections/04_case_study_autocomplete_search.md` | ~2,300 |
| `90_connections/05_case_study_routing_graph_system.md` | ~2,200 |
| `90_connections/06_case_study_streaming_analytics.md` | ~2,400 |
| `90_connections/07_case_study_scheduler_backpressure.md` | ~2,300 |
| `README.md` | ~1,700 |

Các `_index.md` cố ý ngắn vì chỉ làm navigation.

**Tổng quy mô ước lượng:** khoảng **204,000+ từ** cho Advanced DSA. Đây là coverage estimate, không phải word count tuyệt đối.

## Trạng thái các pass nội dung

### Pass 1–4 — kiến trúc, độ phủ và core algorithms

Thư viện được chia thành Foundations, Linear Structures, Trees, Graphs, Algorithmic Paradigms, Specialized Structures, Language Implementations và System Connections. Các chủ đề core được mở rộng từ mức ghi chú/cheat sheet thành các chapter độc lập có reasoning, implementation và cross-links.

### Pass 5–6 — reasoning và độ sâu triển khai

Các chapter cốt lõi được nâng theo hướng specification → invariant/proof → complexity → memory/runtime model → testing → production connection. Những vùng được tăng mạnh gồm correctness, mathematical toolkit, memory model, hash table, queue/deque/PQ, graph algorithms, sorting, DP, selection, language/runtime implementation và benchmarking.

### Language-normalization pass

Phần giải thích được chuẩn hóa sang tiếng Việt tự nhiên. Các thuật ngữ như `invariant`, `ownership`, `locality`, `differential testing` chỉ được giữ bên cạnh bản dịch khi có giá trị tra cứu.

### Depth-normalization pass

Các chapter trước đây lệch chiều sâu được nâng thêm: problem modeling, correctness, mathematical toolkit, queue/deque/PQ, hash table, sorting, hard problems, probabilistic structures, intervals/sweep line, amortized/randomized thinking, network flow, suffix structures, data-structure selection, systems connections, problem-solving workflow, Trie, balanced trees và two-pointers/sliding-window/prefix/difference.

Sau pass này, những chapter khoảng 2,700–2,900 từ như `heaps`, `graph_modeling`, `union_find`, `greedy`, `recursion_backtracking` hoặc `DAG/SCC` vẫn được xem là **đủ core depth** vì đã có đầy đủ bản chất, invariants/proof, implementation, caveats và connections. Chúng không cần kéo dài chỉ để đồng đều số từ.

### Systems case-study pass — nối kiến thức thành thiết kế hoàn chỉnh

Năm case study được thêm vào `90_connections`:

- Database Indexing — B+Tree, Hash Index, Buffer Pool, Bloom Filter, LSM, join và crash consistency;
- Autocomplete/Search — Trie/Radix/FST, Top-K, fuzzy search, Unicode, cache, sharding;
- Routing — graph representation, Dijkstra, PQ, dynamic update, longest-prefix match, ECMP/failover;
- Streaming Analytics — exact map, CMS, HLL, heavy hitters, quantile sketch, time windows, distributed merge;
- Scheduler/Backpressure — FIFO/priority/EDF, fairness, aging, batching, work stealing, bounded queue, retry và admission control.

Mỗi case đi theo workload → representation → invariant → composition → failure/update model → testing/benchmarking.

### Advanced-depth pass — mở rộng sau core

Review sau systems pass cho thấy khoảng trống không còn nằm ở core algorithms mà ở lớp **sau core**, nơi người học cần hiểu vì sao cùng một ADT/paradigm có nhiều cấu trúc chuyên biệt và cách chọn chúng theo workload. Bốn chapter mới được bổ sung:

#### `02_trees/08_advanced_heaps_and_priority_queue_engineering.md`

Mở rộng Priority Queue sang Indexed Heap, D-ary Heap, Binomial/Fibonacci/Pairing/Leftist/Skew Heap, monotone PQ, Dial/Radix Heap, calendar queue, stable priority, lazy deletion, median bằng hai heap, concurrent/relaxed PQ và external-memory PQ.

Mục tiêu không phải học thuộc nhiều loại heap, mà hiểu vector thao tác `insert/extract/decrease-key/meld/delete` quyết định cấu trúc nào hợp lý.

#### `03_graphs/09_dynamic_temporal_and_large_scale_graphs.md`

Bổ sung incremental/decremental/fully dynamic graph, offline dynamic connectivity bằng Segment Tree theo thời gian + Rollback DSU, Euler Tour Tree/Link-Cut Tree, dynamic MST/shortest path, temporal graph, sliding-window graph, graph streaming, partitioning, direction-optimizing BFS, landmarks/A* và Contraction Hierarchies.

Chương này làm rõ rằng dynamic graph cần thêm một chiều state: **phiên bản/thời gian của topology**.

#### `04_algorithmic_paradigms/10_greedy_matroids_primal_dual_and_approximation.md`

Đưa greedy từ các rule riêng lẻ lên cấu trúc tổng quát: independence systems, matroid exchange, graphic/partition matroid, primal–dual, Set Cover approximation, submodular diminishing returns, lazy greedy, online competitive analysis, local search và greedy + binary search/heap/DSU.

Mục tiêu là trả lời sâu hơn câu hỏi: **vì sao một local choice có thể được khóa?**

#### `04_algorithmic_paradigms/11_constraint_search_branch_and_bound.md`

Mở rộng Backtracking thành CSP/solver reasoning: forward checking, constraint propagation, arc consistency, MRV/LCV, symmetry breaking, canonical state, Branch-and-Bound, relaxation, best-first search, alpha-beta, transposition table, Zobrist hashing, SAT-style clause learning, iterative deepening, IDA*, dominance/Pareto frontier, reversible/persistent state, parallel và anytime search.

Mục tiêu là chuyển tư duy từ “viết DFS đệ quy” sang **quản lý thông tin để chứng minh càng nhiều branch là không cần mở càng sớm càng tốt**.

## Đánh giá độ sâu hiện tại

Sau advanced-depth pass, thư viện đã đạt ba tầng tương đối đầy đủ:

```text
Tầng 1 — Core
khái niệm, bất biến, proof, complexity, implementation

Tầng 2 — Engineering
runtime/memory behavior, variants, workload trade-offs, testing

Tầng 3 — Composition/System
case studies, dynamic/online/external-memory/concurrent use
```

Ở thời điểm này, **không còn khoảng trống rõ ràng nào cần giải quyết bằng việc tiếp tục kéo dài mọi chapter**. Việc tăng word count cơ học từ đây có nguy cơ làm tài liệu loãng hơn thay vì sâu hơn.

Những hướng nâng cấp tự nhiên tiếp theo nên là:

```text
worked exercises có lời giải từng bước
proof exercises và counterexample exercises
production failure/postmortem nhỏ
cross-links theo invariant thay vì chỉ theo topic
case study cache/allocator/compiler/search engine
notation và terminology consistency toàn library
```

## Tiêu chí “đủ sâu” cho các lần review sau

Một chapter chỉ được xem là hoàn thiện khi người đọc có thể trả lời, nếu các câu hỏi đó liên quan tới chủ đề:

1. Khái niệm giải quyết vấn đề gì và tại sao cần nó?
2. Cách biểu diễn và bất biến là gì?
3. Vì sao thao tác/thuật toán đúng?
4. Complexity đến từ đâu, thuộc worst-case/expected/amortized/high-probability loại nào?
5. Khi nào các giả định hoặc invariant bị phá?
6. Implementation trong C/Java/JavaScript có caveat quan trọng gì?
7. Có thể kiểm thử/validate bằng cách nào?
8. Nó liên hệ với database/network/OS/runtime hoặc cấu trúc nào khác?
9. Khi nào không nên dùng nó?
10. Có biến thể nào đáng chọn khi workload thay đổi?

Nếu chapter thiếu một lớp quan trọng trong số này, nó vẫn là ứng viên cho pass tiếp theo.