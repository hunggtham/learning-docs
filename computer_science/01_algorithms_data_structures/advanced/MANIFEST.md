# Advanced DSA tệp (file / 파일) Manifest

> **Mạch đọc:** [README](./README.md) là bản đồ owner của **Advanced DSA tệp (file / 파일) Manifest**; nhìn vào vị trí đó trước để biết file này đang phục vụ nhánh kiến thức nào. **Độ phủ hiện tại** mở đối tượng chính của file và câu hỏi cần theo dõi; sau đó sang **Trạng thái các pass nội dung** để mở rộng đối tượng sang phạm vi kế cận. Cách đi này giữ lại điểm tựa của section đầu và cho biết kết luận sẽ được dùng ở đâu, thay vì dừng ở định nghĩa đầu tiên.

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

Phần giải thích dùng tiếng Việt làm ngôn ngữ chính; thuật ngữ Anh/Hàn được giữ như từ khóa (keyword / 키워드) bổ trợ khi hữu ích. mã (code / 코드), API, lớp (class / 클래스)/hàm (function / 함수) name và tên thuật toán chuẩn không bị dịch máy móc.

## Độ phủ hiện tại

Phần này chuyển khái niệm Computer Science thành cấu trúc, ví dụ hoặc quy trình có thể kiểm tra. Hãy xác định câu hỏi mà mục trả lời rồi nối kết luận với phần kế tiếp.

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

Các `_index.md` cố ý ngắn vì chỉ làm điều hướng (navigation / 내비게이션).

**Tổng quy mô ước lượng:** khoảng **204,000+ từ** cho Advanced DSA. Đây là coverage estimate, không phải word count tuyệt đối.

> **Chuyển mạch:** Trong **Advanced DSA tệp (file / 파일) Manifest**, **Trạng thái các pass nội dung** tiếp nhận điểm tựa từ **Độ phủ hiện tại** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Đánh giá độ sâu hiện tại** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Trạng thái các pass nội dung

### Pass 1–4 — kiến trúc, độ phủ và cốt lõi (core / 핵심) algorithms

Thư viện được chia thành Foundations, tuyến tính (linear / 선형) Structures, Trees, Graphs, Algorithmic Paradigms, Specialized Structures, ngôn ngữ (language / 언어) Implementations và hệ thống (system / 시스템) Connections. Các chủ đề cốt lõi (core / 핵심) được mở rộng từ mức ghi chú/cheat sheet thành các chapter độc lập có lập luận (reasoning / 추론), hiện thực (implementation / 구현) và cross-links.

### Pass 5–6 — lập luận (reasoning / 추론) và độ sâu triển khai

Các chapter cốt lõi được nâng theo hướng specification → bất biến (invariant / 불변식)/proof → độ phức tạp (complexity / 복잡도) → bộ nhớ (memory / 메모리)/thời gian chạy (runtime / 런타임) mô hình (model / 모델) → testing → môi trường vận hành (production / 운영 환경) liên kết (connection / 연결). Những vùng được tăng mạnh gồm tính đúng đắn (correctness / 정확성), mathematical toolkit, bộ nhớ (memory / 메모리) mô hình (model / 모델), bảng băm (hash table / 해시 테이블), hàng đợi (queue / 큐)/deque/PQ, đồ thị (graph / 그래프) algorithms, sorting, DP, selection, ngôn ngữ (language / 언어)/thời gian chạy (runtime / 런타임) hiện thực (implementation / 구현) và benchmarking.

### Language-normalization pass

Phần giải thích được chuẩn hóa sang tiếng Việt tự nhiên. Các thuật ngữ như `invariant`, `ownership`, `locality`, `differential testing` chỉ được giữ bên cạnh bản dịch khi có giá trị tra cứu.

### Depth-normalization pass

Các chapter trước đây lệch chiều sâu được nâng thêm: bài toán (problem / 문제) modeling, tính đúng đắn (correctness / 정확성), mathematical toolkit, hàng đợi (queue / 큐)/deque/PQ, bảng băm (hash table / 해시 테이블), sorting, hard problems, probabilistic structures, intervals/sweep line, amortized/randomized thinking, mạng (network / 네트워크) luồng (flow / 흐름), suffix structures, data-structure selection, các hệ thống (systems / 시스템들) connections, problem-solving workflow, Trie, balanced trees và two-pointers/sliding-window/prefix/difference.

Sau pass này, những chapter khoảng 2,700–2,900 từ như `heaps`, `graph_modeling`, `union_find`, `greedy`, `recursion_backtracking` hoặc `DAG/SCC` vẫn được xem là **đủ cốt lõi (core / 핵심) độ sâu (depth / 깊이)** vì đã có đầy đủ bản chất, invariants/proof, hiện thực (implementation / 구현), caveats và connections. Chúng không cần kéo dài chỉ để đồng đều số từ.

### Các hệ thống (systems / 시스템들) case-study pass — nối kiến thức thành thiết kế hoàn chỉnh

Năm trường hợp (case / 사례) study được thêm vào `90_connections`:

- cơ sở dữ liệu (database / 데이터베이스) Indexing — B+cây (tree / 트리), băm (hash / 해시) chỉ mục (index / 인덱스), Buffer Pool, Bloom Filter, LSM, phép nối (join / 조인) và crash consistency;
- Autocomplete/tìm kiếm (search / 검색) — Trie/Radix/FST, Top-K, fuzzy tìm kiếm (search / 검색), Unicode, bộ nhớ đệm (cache / 캐시), sharding;
- Routing — đồ thị (graph / 그래프) biểu diễn (representation / 표현), Dijkstra, PQ, động (dynamic / 동적) cập nhật (update / 업데이트), longest-prefix match, ECMP/failover;
- Streaming Analytics — chính xác (exact / 정확한) map, CMS, HLL, heavy hitters, quantile sketch, thời gian (time / 시간) windows, phân tán (distributed / 분산) merge;
- Scheduler/Backpressure — FIFO/priority/EDF, fairness, aging, batching, công việc (work / 작업) stealing, bounded hàng đợi (queue / 큐), thử lại (retry / 재시도) và admission điều khiển (control / 제어).

Mỗi trường hợp (case / 사례) đi theo tải công việc (workload / 워크로드) → biểu diễn (representation / 표현) → bất biến (invariant / 불변식) → composition → thất bại (failure / 실패)/cập nhật (update / 업데이트) mô hình (model / 모델) → testing/benchmarking.

### Advanced-depth pass — mở rộng sau cốt lõi (core / 핵심)

Rà soát (review / 검토) sau các hệ thống (systems / 시스템들) pass cho thấy khoảng trống không còn nằm ở cốt lõi (core / 핵심) algorithms mà ở lớp **sau cốt lõi (core / 핵심)**, nơi người học cần hiểu vì sao cùng một ADT/paradigm có nhiều cấu trúc chuyên biệt và cách chọn chúng theo tải công việc (workload / 워크로드). Bốn chapter mới được bổ sung:

#### `02_trees/08_advanced_heaps_and_priority_queue_engineering.md`

Mở rộng Priority hàng đợi (queue / 큐) sang Indexed vùng nhớ động (heap / 힙), D-ary vùng nhớ động (heap / 힙), Binomial/Fibonacci/Pairing/Leftist/Skew vùng nhớ động (heap / 힙), monotone PQ, Dial/Radix vùng nhớ động (heap / 힙), calendar hàng đợi (queue / 큐), stable priority, lazy deletion, median bằng hai vùng nhớ động (heap / 힙), concurrent/relaxed PQ và external-memory PQ.

Mục tiêu không phải học thuộc nhiều loại vùng nhớ động (heap / 힙), mà hiểu véc-tơ (vector / 벡터) thao tác `insert/extract/decrease-key/meld/delete` quyết định cấu trúc nào hợp lý.

#### `03_graphs/09_dynamic_temporal_and_large_scale_graphs.md`

Bổ sung incremental/decremental/fully động (dynamic / 동적) đồ thị (graph / 그래프), offline động (dynamic / 동적) connectivity bằng Segment cây (tree / 트리) theo thời gian + quay lui (rollback / 롤백) DSU, Euler Tour cây (tree / 트리)/Link-Cut cây (tree / 트리), động (dynamic / 동적) MST/shortest đường dẫn (path / 경로), temporal đồ thị (graph / 그래프), sliding-window đồ thị (graph / 그래프), đồ thị (graph / 그래프) streaming, partitioning, direction-optimizing BFS, landmarks/A* và Contraction Hierarchies.

Chương này làm rõ rằng động (dynamic / 동적) đồ thị (graph / 그래프) cần thêm một chiều trạng thái (state / 상태): **phiên bản/thời gian của topology**.

#### `04_algorithmic_paradigms/10_greedy_matroids_primal_dual_and_approximation.md`

Đưa greedy từ các quy tắc (rule / 규칙) riêng lẻ lên cấu trúc tổng quát: independence các hệ thống (systems / 시스템들), matroid exchange, graphic/partition matroid, primal–dual, Set Cover approximation, submodular diminishing returns, lazy greedy, online competitive phân tích (analysis / 분석), cục bộ (local / 로컬) tìm kiếm (search / 검색) và greedy + tìm kiếm nhị phân (binary search / 이진 탐색)/vùng nhớ động (heap / 힙)/DSU.

Mục tiêu là trả lời sâu hơn câu hỏi: **vì sao một cục bộ (local / 로컬) choice có thể được khóa?**

#### `04_algorithmic_paradigms/11_constraint_search_branch_and_bound.md`

Mở rộng Backtracking thành CSP/solver lập luận (reasoning / 추론): forward checking, ràng buộc (constraint / 제약조건) propagation, arc consistency, MRV/LCV, symmetry breaking, chuẩn gốc (canonical / 정본) trạng thái (state / 상태), Branch-and-Bound, relaxation, best-first tìm kiếm (search / 검색), alpha-beta, transposition bảng (table / 테이블), Zobrist hashing, SAT-style clause học tập (learning / 학습), iterative deepening, IDA*, dominance/Pareto frontier, reversible/persistent trạng thái (state / 상태), parallel và anytime tìm kiếm (search / 검색).

Mục tiêu là chuyển tư duy từ “viết DFS đệ quy” sang **quản lý thông tin để chứng minh càng nhiều branch là không cần mở càng sớm càng tốt**.

> **Chuyển mạch:** Ở chặng này của **Advanced DSA tệp (file / 파일) Manifest**, **Đánh giá độ sâu hiện tại** tiếp nhận điểm tựa từ **Trạng thái các pass nội dung** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Tiêu chí “đủ sâu” cho các lần rà soát (review / 검토) sau** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

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

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Advanced DSA tệp (file / 파일) Manifest**, **Tiêu chí “đủ sâu” cho các lần rà soát (review / 검토) sau** tiếp nhận điểm tựa từ **Đánh giá độ sâu hiện tại** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Phần còn lại của file dùng kết quả này để khép lại mạch giải thích.

## Tiêu chí “đủ sâu” cho các lần rà soát (review / 검토) sau

Một chapter chỉ được xem là hoàn thiện khi người đọc có thể trả lời, nếu các câu hỏi đó liên quan tới chủ đề:

1. Khái niệm giải quyết vấn đề gì và tại sao cần nó?
2. Cách biểu diễn và bất biến là gì?
3. Vì sao thao tác/thuật toán đúng?
4. độ phức tạp (complexity / 복잡도) đến từ đâu, thuộc worst-case/expected/amortized/high-probability loại nào?
5. Khi nào các giả định hoặc bất biến (invariant / 불변식) bị phá?
6. hiện thực (implementation / 구현) trong C/Java/JavaScript có caveat quan trọng gì?
7. Có thể kiểm thử/validate bằng cách nào?
8. Nó liên hệ với cơ sở dữ liệu (database / 데이터베이스)/mạng (network / 네트워크)/OS/thời gian chạy (runtime / 런타임) hoặc cấu trúc nào khác?
9. Khi nào không nên dùng nó?
10. Có biến thể nào đáng chọn khi tải công việc (workload / 워크로드) thay đổi?

Nếu chapter thiếu một lớp quan trọng trong số này, nó vẫn là ứng viên cho pass tiếp theo.

> **Bàn giao:** Sau **Tiêu chí “đủ sâu” cho các lần rà soát (review / 검토) sau**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](./README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
