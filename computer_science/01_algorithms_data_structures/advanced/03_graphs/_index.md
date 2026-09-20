# 03_graphs

Nhóm này đi từ mô hình hóa đồ thị tới traversal, tối ưu đường đi, connectivity và các cấu trúc động.

- `00_graph_modeling_and_representation.md` — xác định node/edge/state và chọn matrix/list/CSR/implicit graph.
- `01_graph_traversal_bfs_dfs.md` — BFS/DFS, frontier, visited state và traversal invariants.
- `02_shortest_paths.md` — BFS, Dijkstra, Bellman-Ford, Floyd-Warshall và các giả định về trọng số.
- `03_minimum_spanning_trees.md` — Kruskal/Prim, cut/cycle property và sensitivity.
- `04_dag_topological_sort_and_scc.md` — DAG, topological order, Tarjan/Kosaraju và condensation graph.
- `05_union_find.md` — DSU, path compression, union-by-size, rollback và weighted/parity variants.
- `06_bridges_articulation_and_biconnectivity.md` — low-link, bridge tree và block-cut tree.
- `07_eulerian_paths_and_cycles.md` — Hierholzer, parity/balance và Eulerization.
- `08_network_flow_and_matching.md` — residual graph, max-flow/min-cut, Dinic, Push–Relabel, matching và circulation.
- `09_dynamic_temporal_and_large_scale_graphs.md` — incremental/decremental/fully dynamic graph, temporal graph, dynamic connectivity/MST, graph streaming, partitioning và large-scale traversal.

`09_dynamic_temporal_and_large_scale_graphs.md` là lớp tiếp theo sau core graph algorithms: thay vì giả định topology đứng yên, nó xem topology, trọng số và thời gian tồn tại của cạnh như một phần của state cần quản lý.