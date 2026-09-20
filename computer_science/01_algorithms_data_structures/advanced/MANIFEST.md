# Advanced DSA File Manifest

Manifest này thuộc thư mục `computer_science/01_algorithms_data_structures/advanced/`. Word count là số gần đúng, dùng để kiểm tra độ phủ và phát hiện chapter quá mỏng; nó không phải tiêu chí chất lượng duy nhất. Sau năm content pass, library được nâng theo hướng **concept → mental model → invariant/proof → complexity → implementation → edge cases → language/runtime semantics → system connections** thay vì note tóm tắt.

| File | Approx. words |
|---|---:|
| `00_foundations/00_dsa_as_problem_modeling.md` | ~3,200 |
| `00_foundations/01_algorithm_correctness_and_invariants.md` | ~3,300 |
| `00_foundations/02_complexity_analysis.md` | 895 |
| `00_foundations/03_memory_models_c_java_javascript.md` | ~2,300 |
| `00_foundations/04_mathematical_toolkit_for_dsa.md` | ~3,500 |
| `00_foundations/_index.md` | 28 |
| `01_linear_structures/00_arrays_and_dynamic_arrays.md` | 1,051 |
| `01_linear_structures/01_linked_lists.md` | 988 |
| `01_linear_structures/02_stacks.md` | 739 |
| `01_linear_structures/03_queues_deques_and_priority_queues.md` | ~3,600 |
| `01_linear_structures/04_hash_tables.md` | ~4,100 |
| `01_linear_structures/_index.md` | 14 |
| `02_trees/00_tree_foundations.md` | ~2,700 |
| `02_trees/01_binary_search_trees.md` | ~3,000 |
| `02_trees/02_balanced_search_trees.md` | ~2,500 |
| `02_trees/03_heaps.md` | ~2,700 |
| `02_trees/04_tries.md` | ~2,200 |
| `02_trees/05_b_trees_and_external_memory.md` | ~3,500 |
| `02_trees/06_augmented_trees_and_order_statistics.md` | ~3,100 |
| `02_trees/07_skip_lists.md` | ~3,300 |
| `02_trees/_index.md` | 40 |
| `03_graphs/00_graph_modeling_and_representation.md` | ~2,700 |
| `03_graphs/01_graph_traversal_bfs_dfs.md` | ~3,200 |
| `03_graphs/02_shortest_paths.md` | ~3,200 |
| `03_graphs/03_minimum_spanning_trees.md` | ~2,100 |
| `03_graphs/04_dag_topological_sort_and_scc.md` | ~2,900 |
| `03_graphs/05_union_find.md` | ~2,800 |
| `03_graphs/06_bridges_articulation_and_biconnectivity.md` | ~1,900 |
| `03_graphs/07_eulerian_paths_and_cycles.md` | ~1,700 |
| `03_graphs/08_network_flow_and_matching.md` | ~2,300 |
| `03_graphs/_index.md` | 29 |
| `04_algorithmic_paradigms/00_searching.md` | ~3,000 |
| `04_algorithmic_paradigms/01_sorting.md` | ~3,700 |
| `04_algorithmic_paradigms/02_recursion_and_backtracking.md` | ~2,900 |
| `04_algorithmic_paradigms/03_divide_and_conquer.md` | ~1,800 |
| `04_algorithmic_paradigms/04_greedy_algorithms.md` | ~2,700 |
| `04_algorithmic_paradigms/05_dynamic_programming.md` | ~4,500 |
| `04_algorithmic_paradigms/06_selection_and_top_k.md` | ~1,900 |
| `04_algorithmic_paradigms/07_two_pointers_sliding_window_prefix_difference.md` | ~2,400 |
| `04_algorithmic_paradigms/08_intervals_and_sweep_line.md` | ~1,900 |
| `04_algorithmic_paradigms/09_hard_problems_reductions_and_approximation.md` | ~3,600 |
| `04_algorithmic_paradigms/_index.md` | 38 |
| `05_specialized/00_string_algorithms.md` | ~3,100 |
| `05_specialized/01_range_queries_fenwick_segment_tree.md` | ~3,200 |
| `05_specialized/02_bit_manipulation_and_bitsets.md` | ~3,000 |
| `05_specialized/03_amortized_randomized_and_probabilistic_thinking.md` | ~2,100 |
| `05_specialized/04_suffix_arrays_suffix_trees_and_lcp.md` | ~2,300 |
| `05_specialized/05_sparse_table_and_static_range_queries.md` | ~3,000 |
| `05_specialized/06_probabilistic_data_structures.md` | ~3,700 |
| `05_specialized/_index.md` | 34 |
| `80_language_implementations/00_c_dsa_implementation_patterns.md` | ~3,700 |
| `80_language_implementations/01_java_collections_and_dsa.md` | ~4,000 |
| `80_language_implementations/02_javascript_dsa_runtime_patterns.md` | ~4,200 |
| `80_language_implementations/03_cross_language_testing_and_benchmarking.md` | ~1,800 |
| `80_language_implementations/_index.md` | 37 |
| `90_connections/00_choose_the_right_data_structure.md` | ~1,500 |
| `90_connections/01_dsa_in_databases_networks_and_systems.md` | ~2,200 |
| `90_connections/02_problem_solving_workflow.md` | ~1,600 |
| `90_connections/_index.md` | 12 |
| `README.md` | ~1,350 |

**Total approximate words:** ~134,000+

Các foundation chapters ở thư mục cha không được tính vào tổng này; manifest chỉ đo Advanced DSA Knowledge Library. Các số có dấu `~` là estimate phục vụ coverage QA, không phải word count tuyệt đối.

## Content-pass status

### Pass 1 — kiến trúc và độ phủ

Library được tách thành foundations, linear structures, trees, graphs, algorithmic paradigms, specialized structures, language implementations và system connections. Các chủ đề nâng cao như B/B+Tree, augmented tree, skip list, flow/matching, suffix structures, sparse table, probabilistic structures và reductions/NP được bổ sung để library vượt khỏi phạm vi “DSA interview notes”.

### Pass 2 — xử lý các chapter mỏng nhất

`memory_models`, `tries`, `MST`, `bridges/articulation`, `Eulerian`, `network flow`, `divide and conquer`, `selection/top-k`, `two pointers/sliding window/prefix`, `interval/sweep line`, `amortized/randomized`, `suffix structures`, `testing/benchmarking` và toàn bộ nhóm `90_connections` được nâng thành các chapter dài có reasoning và production context.

### Pass 3 — củng cố các mental model cốt lõi

Pass 3 nâng `balanced_search_trees`, `heaps`, `shortest_paths`, `DAG/topological sort/SCC`, `union_find`, `recursion/backtracking`, `greedy`, `string algorithms`, `Fenwick/Segment Tree` và `bit manipulation/bitsets` lên mức chapter chuyên sâu với proof intuition, implementation trade-offs và runtime caveats.

### Pass 4 — hoàn thiện các dependency còn lệch độ sâu

Pass 4 nâng `tree_foundations`, `binary_search_trees`, `b_trees_and_external_memory`, `graph_modeling_and_representation`, `graph_traversal_bfs_dfs`, `searching`, `dynamic_programming`, `sparse_table` và ba chapter C/Java/JavaScript runtime implementation. Sau pass này, phần lớn algorithm-specific core chapters đã ở mức vài nghìn từ.

### Pass 5 — hoàn thiện reasoning foundation và các cấu trúc còn mỏng

Pass 5 tập trung các chapter còn là điểm lõm cuối cùng của core library:

- `dsa_as_problem_modeling`: chuyển từ giới thiệu ADT thành framework modeling đầy đủ gồm workload, state equivalence, static/dynamic, online/offline, exact/approximate, deterministic/expected guarantees, preprocessing, composition và runtime cost model;
- `algorithm_correctness_and_invariants`: bổ sung specification, partial/total correctness, loop/representation invariants, structural/strong induction, exchange/cut/contradiction proofs, executable validators, differential/property testing, overflow và concurrency correctness;
- `mathematical_toolkit_for_dsa`: mở rộng logarithm/sums/recurrences sang combinatorics, algebraic properties, modular arithmetic, probability/expectation, graph identities, aggregate/accounting/potential amortized analysis và information-theoretic lower bounds;
- `queues_deques_and_priority_queues`: bổ sung ring-buffer invariants, bounded queues/backpressure, monotonic deque proof, 0–1 BFS, indexed/lazy/bucket priority queues, scheduling fairness, blocking/work-stealing/concurrent queues và testing;
- `hash_tables`: mở rộng chaining/open addressing, probing/tombstones/Robin Hood, hash quality/security, perfect/consistent/rendezvous hashing, incremental resize, database hash join/aggregation, concurrent maps, memory/cache model và adversarial testing;
- `augmented_trees_and_order_statistics`: mở rộng rank/select, weighted statistics, interval pruning, multiple augmentations, implicit/persistent/lazy trees, multidimensional summaries, concurrency và invariant validation;
- `skip_lists`: bổ sung complete search/insert/delete contracts, indexed spans, probability/memory trade-offs, storage-engine use, concurrent logical deletion/reclamation, deterministic testing và comparison với tree/B+Tree;
- `sorting`: nâng từ survey lên chapter về comparator/stability/inversions, quick/merge/heap/hybrid/adaptive/non-comparison sorting, external/database/parallel sorting, partial sorting, hardware locality và correctness benchmarking;
- `hard_problems_reductions_and_approximation`: bổ sung P/NP distinction sâu hơn, reduction proof discipline, SAT/2-SAT, pseudo-polynomial/FPT/kernel/treewidth, meet-in-the-middle, branch-and-bound, LP relaxation, approximation/PTAS/FPTAS, solver và anytime-gap thinking;
- `probabilistic_data_structures`: bổ sung parameter sizing/error models, Counting/Cuckoo/XOR filters, CMS/HLL details, MinHash/KMV/LSH, mergeability, temporal windows, adversarial hashing, serialization/monitoring và statistical validation.

## Remaining natural targets

Sau pass 5, không còn chapter core nào ở mức chỉ vài trăm từ ngoài các `_index.md` cố ý ngắn. Các file ngắn hơn tương đối còn lại — như `complexity_analysis`, `arrays`, `linked_lists`, `stacks`, `probabilistic/amortized thinking` hoặc một số graph subchapters — đã đủ làm chapter độc lập nhưng có thể được nâng tiếp nếu muốn đưa **mọi** chapter về ngưỡng 2,000–3,000 từ.

Hướng mở rộng hợp lý tiếp theo không còn là “vá lỗ hổng cơ bản”, mà là một content pass theo chiều ngang: đồng bộ terminology, thêm cross-links, thêm worked examples lớn xuyên nhiều chapter, hoặc nâng các file 700–1,500 từ còn lại lên cùng độ sâu với nhóm 3,000+ từ.
