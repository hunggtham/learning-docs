# 03_graphs

> **Mạch đọc:** Đọc **03graphs** như một mắt xích của lộ trình học (learning path / 학습 경로) hiện tại, không như một ghi chú tách rời. Hãy xác định đối tượng và câu hỏi trung tâm trước, rồi dùng phần này để đối chiếu với mục liên quan sau khi đã nắm mô hình tư duy (mental model / 사고 모델) chính.


Nhóm này đi từ mô hình hóa đồ thị tới traversal, tối ưu đường đi, connectivity và các cấu trúc động.

- `00_graph_modeling_and_representation.md` — xác định nút (node / 노드)/edge/trạng thái (state / 상태) và chọn ma trận (matrix / 행렬)/danh sách (list / 목록)/CSR/implicit đồ thị (graph / 그래프).
- `01_graph_traversal_bfs_dfs.md` — BFS/DFS, frontier, visited trạng thái (state / 상태) và traversal invariants.
- `02_shortest_paths.md` — BFS, Dijkstra, Bellman-Ford, Floyd-Warshall và các giả định về trọng số.
- `03_minimum_spanning_trees.md` — Kruskal/Prim, cut/cycle thuộc tính (property / 속성) và sensitivity.
- `04_dag_topological_sort_and_scc.md` — DAG, topological thứ tự (order / 순서), Tarjan/Kosaraju và condensation đồ thị (graph / 그래프).
- `05_union_find.md` — DSU, đường dẫn (path / 경로) compression, union-by-size, quay lui (rollback / 롤백) và weighted/parity variants.
- `06_bridges_articulation_and_biconnectivity.md` — low-link, cầu nối (bridge / 브리지) cây (tree / 트리) và block-cut cây (tree / 트리).
- `07_eulerian_paths_and_cycles.md` — Hierholzer, parity/balance và Eulerization.
- `08_network_flow_and_matching.md` — residual đồ thị (graph / 그래프), max-flow/min-cut, Dinic, Push–Relabel, matching và circulation.
- `09_dynamic_temporal_and_large_scale_graphs.md` — incremental/decremental/fully động (dynamic / 동적) đồ thị (graph / 그래프), temporal đồ thị (graph / 그래프), động (dynamic / 동적) connectivity/MST, đồ thị (graph / 그래프) streaming, partitioning và large-scale traversal.

`09_dynamic_temporal_and_large_scale_graphs.md` là lớp tiếp theo sau cốt lõi (core / 핵심) đồ thị (graph / 그래프) algorithms: thay vì giả định topology đứng yên, nó xem topology, trọng số và thời gian tồn tại của cạnh như một phần của trạng thái (state / 상태) cần quản lý.

> **Bàn giao:** Sau **03graphs**, hãy chốt bất biến (invariant / 불변식) và giới hạn của mục này trước khi nối sang kiến thức kế tiếp. Có thể đọc tiếp [00 graph modeling and representation](./00_graph_modeling_and_representation.md) để đối chiếu ranh giới (boundary / 경계) gần nhất.
