# Chọn cấu trúc dữ liệu phù hợp
**Data Structure Selection / 자료구조 선택**

Đừng chọn theo tên cấu trúc quen thuộc. Chọn từ operations, invariants và mutation pattern.

| Nhu cầu chính | Cấu trúc thường phù hợp |
|---|---|
| random access theo index | array / dynamic array |
| exact lookup theo key | hash map / hash set |
| sorted dynamic keys | balanced BST |
| min/max liên tục | heap / priority queue |
| LIFO | stack |
| FIFO | queue |
| thao tác hai đầu | deque |
| prefix string | trie |
| graph reachability | adjacency list + BFS/DFS |
| merge-only connectivity | DSU |
| static range sum | prefix sum |
| point update + range sum | Fenwick tree |
| general range aggregate/update | segment tree |

## Không chỉ nhìn Big-O

Linked list có insert `O(1)` tại node đã biết, nhưng tìm node có thể `O(n)` và locality kém. Hash map expected `O(1)` nhưng không tự giữ sorted order. Tree map `O(log n)` nhưng cung cấp predecessor/successor/range semantics.

## Composition mới là thực tế

Nhiều hệ thống ghép structures. LRU cache = hash map + doubly linked list. Dijkstra = graph adjacency list + priority queue. Kruskal = edge list sorting + DSU. Autocomplete có thể = trie + ranking heap/cache.

## Mental Model

> Không hỏi “cấu trúc nào nhanh nhất?”. Hỏi “operation nào phải rẻ, invariant nào phải giữ, dữ liệu mutate theo cách nào, và cost model của runtime/hardware là gì?”.
