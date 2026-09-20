# Advanced DSA File Manifest

Manifest này thuộc thư mục `computer_science/01_algorithms_data_structures/advanced/`. Word count là số gần đúng, dùng để kiểm tra độ phủ và phát hiện chapter quá mỏng; nó không phải tiêu chí chất lượng duy nhất. Sau ba content pass, các chapter trọng tâm được nâng theo hướng **concept → mental model → invariant/proof → complexity → implementation → edge cases → language/runtime semantics → system connections** thay vì note tóm tắt.

| File | Approx. words |
|---|---:|
| `00_foundations/00_dsa_as_problem_modeling.md` | 606 |
| `00_foundations/01_algorithm_correctness_and_invariants.md` | 534 |
| `00_foundations/02_complexity_analysis.md` | 895 |
| `00_foundations/03_memory_models_c_java_javascript.md` | ~2,300 |
| `00_foundations/04_mathematical_toolkit_for_dsa.md` | 762 |
| `00_foundations/_index.md` | 28 |
| `01_linear_structures/00_arrays_and_dynamic_arrays.md` | 1,051 |
| `01_linear_structures/01_linked_lists.md` | 988 |
| `01_linear_structures/02_stacks.md` | 739 |
| `01_linear_structures/03_queues_deques_and_priority_queues.md` | 645 |
| `01_linear_structures/04_hash_tables.md` | 681 |
| `01_linear_structures/_index.md` | 14 |
| `02_trees/00_tree_foundations.md` | 563 |
| `02_trees/01_binary_search_trees.md` | 563 |
| `02_trees/02_balanced_search_trees.md` | ~2,500 |
| `02_trees/03_heaps.md` | ~2,700 |
| `02_trees/04_tries.md` | ~2,200 |
| `02_trees/05_b_trees_and_external_memory.md` | 542 |
| `02_trees/06_augmented_trees_and_order_statistics.md` | 736 |
| `02_trees/07_skip_lists.md` | 721 |
| `02_trees/_index.md` | 40 |
| `03_graphs/00_graph_modeling_and_representation.md` | 546 |
| `03_graphs/01_graph_traversal_bfs_dfs.md` | 543 |
| `03_graphs/02_shortest_paths.md` | ~3,200 |
| `03_graphs/03_minimum_spanning_trees.md` | ~2,100 |
| `03_graphs/04_dag_topological_sort_and_scc.md` | ~2,900 |
| `03_graphs/05_union_find.md` | ~2,800 |
| `03_graphs/06_bridges_articulation_and_biconnectivity.md` | ~1,900 |
| `03_graphs/07_eulerian_paths_and_cycles.md` | ~1,700 |
| `03_graphs/08_network_flow_and_matching.md` | ~2,300 |
| `03_graphs/_index.md` | 29 |
| `04_algorithmic_paradigms/00_searching.md` | 630 |
| `04_algorithmic_paradigms/01_sorting.md` | 979 |
| `04_algorithmic_paradigms/02_recursion_and_backtracking.md` | ~2,900 |
| `04_algorithmic_paradigms/03_divide_and_conquer.md` | ~1,800 |
| `04_algorithmic_paradigms/04_greedy_algorithms.md` | ~2,700 |
| `04_algorithmic_paradigms/05_dynamic_programming.md` | 990 |
| `04_algorithmic_paradigms/06_selection_and_top_k.md` | ~1,900 |
| `04_algorithmic_paradigms/07_two_pointers_sliding_window_prefix_difference.md` | ~2,400 |
| `04_algorithmic_paradigms/08_intervals_and_sweep_line.md` | ~1,900 |
| `04_algorithmic_paradigms/09_hard_problems_reductions_and_approximation.md` | 898 |
| `04_algorithmic_paradigms/_index.md` | 38 |
| `05_specialized/00_string_algorithms.md` | ~3,100 |
| `05_specialized/01_range_queries_fenwick_segment_tree.md` | ~3,200 |
| `05_specialized/02_bit_manipulation_and_bitsets.md` | ~3,000 |
| `05_specialized/03_amortized_randomized_and_probabilistic_thinking.md` | ~2,100 |
| `05_specialized/04_suffix_arrays_suffix_trees_and_lcp.md` | ~2,300 |
| `05_specialized/05_sparse_table_and_static_range_queries.md` | 643 |
| `05_specialized/06_probabilistic_data_structures.md` | 880 |
| `05_specialized/_index.md` | 34 |
| `80_language_implementations/00_c_dsa_implementation_patterns.md` | 738 |
| `80_language_implementations/01_java_collections_and_dsa.md` | 689 |
| `80_language_implementations/02_javascript_dsa_runtime_patterns.md` | 769 |
| `80_language_implementations/03_cross_language_testing_and_benchmarking.md` | ~1,800 |
| `80_language_implementations/_index.md` | 37 |
| `90_connections/00_choose_the_right_data_structure.md` | ~1,500 |
| `90_connections/01_dsa_in_databases_networks_and_systems.md` | ~2,200 |
| `90_connections/02_problem_solving_workflow.md` | ~1,600 |
| `90_connections/_index.md` | 12 |
| `README.md` | ~1,350 |

**Total approximate words:** ~78,000+

Các foundation chapters ở thư mục cha không được tính vào tổng này; manifest chỉ đo Advanced DSA Knowledge Library.

## Content-pass status

### Pass 1 — kiến trúc và độ phủ

Library được tách thành foundations, linear structures, trees, graphs, algorithmic paradigms, specialized structures, language implementations và system connections. Các chủ đề nâng cao như B/B+Tree, augmented tree, skip list, flow/matching, suffix structures, sparse table, probabilistic structures và reductions/NP được bổ sung để library vượt khỏi phạm vi “DSA interview notes”.

### Pass 2 — xử lý các chapter mỏng nhất

`memory_models`, `tries`, `MST`, `bridges/articulation`, `Eulerian`, `network flow`, `divide and conquer`, `selection/top-k`, `two pointers/sliding window/prefix`, `interval/sweep line`, `amortized/randomized`, `suffix structures`, `testing/benchmarking` và toàn bộ nhóm `90_connections` được nâng thành các chapter dài có reasoning và production context.

### Pass 3 — củng cố các mental model cốt lõi

Pass hiện tại đã nâng tiếp:

- `balanced_search_trees`: AVL/Red-Black invariants, rotation proof, deletion, comparator contract, augmentation, locality và B-Tree connection;
- `heaps`: partial order, build-heap proof, priority-queue abstraction, indexed heap/decrease-key, top-k, k-way merge, online median, d-ary heaps và mutable-priority pitfalls;
- `shortest_paths`: BFS, 0-1 BFS, Dijkstra, Bellman-Ford, DAG shortest path, Floyd-Warshall, Johnson, A*, bidirectional reasoning, negative-cycle semantics và overflow;
- `dag_topological_sort_and_scc`: Kahn/DFS topo, DAG DP, critical path, Kosaraju, Tarjan, condensation DAG, 2-SAT connection và transitive concepts;
- `union_find`: union-by-size proof, path compression, offline threshold queries, rollback DSU, potential/parity DSU và offline dynamic connectivity;
- `recursion_and_backtracking`: recursive contracts, induction, search-space modeling, pruning, MRV, branch-and-bound, memoization transition và state ownership;
- `greedy_algorithms`: exchange argument, cut property, Huffman, fractional-vs-0/1 knapsack, scheduling, approximation/heuristic distinction và brute-force counterexample workflow;
- `string_algorithms`: encoding model, KMP/prefix-function, Z, rolling hash, Aho-Corasick, Manacher, periodicity, suffix connections và Unicode/runtime caveats;
- `range_queries_fenwick_segment_tree`: prefix/difference algebra, Fenwick block model, order statistics, two-BIT range updates, monoid segment tree, lazy composition, persistence và implicit trees;
- `bit_manipulation_and_bitsets`: two's complement reasoning, subset/submask algebra, SOS DP, Java/JS/C semantics, bitset acceleration, bitboards, bitset DP và production representation concerns.

## Remaining natural targets

Library hiện đã có nhiều chapter ở mức vài nghìn từ, nhưng một số file vẫn chỉ khoảng 500–900 từ. Các content pass sau nên ưu tiên `tree_foundations`, `binary_search_trees`, `b_trees_and_external_memory`, `graph_modeling_and_representation`, `graph_traversal_bfs_dfs`, `searching`, `dynamic_programming` nếu cần sâu hơn nữa, `sparse_table`, cùng ba chapter language implementations C/Java/JavaScript để toàn library có độ sâu đồng đều hơn.