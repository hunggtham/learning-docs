# Tree, heap và ordered search structures

Tree (트리 / cây) biểu diễn hierarchy và recursive decomposition. Filesystem directories, DOM, AST, database indexes và organizational structures đều có tree-like shape. Nhưng không phải mọi tree phục vụ cùng operation; shape và invariant quyết định performance.

## Tree vocabulary từ structure

Một rooted tree có root, parent/child, leaves, depth và height. Mỗi node trừ root có đúng một parent, và không có cycle. Với n nodes, tree connected có n−1 edges.

Recursive definition tự nhiên: tree là root cộng một tập subtrees. Vì vậy recursion hoặc explicit stack thường dùng traversal.

DFS traversals gồm preorder, inorder, postorder tùy vị trí xử lý node. BFS/level-order dùng queue.

## Binary Search Tree

BST đặt ordering invariant: keys trong left subtree nhỏ hơn node; right lớn hơn, với duplicate policy explicit. Lookup so sánh key và loại bỏ một subtree mỗi step.

Nếu tree balanced, height O(log n). Nếu insert sorted sequence vào naive BST, nó degenerates thành chain height O(n). Vì vậy complexity dựa vào shape.

Self-balancing trees như AVL hoặc Red-Black tree dùng rotations và balance metadata để giữ height O(log n). Standard library ordered map/set thường dùng một dạng balanced tree.

## B-tree và B+ tree

Binary tree tối ưu không nhất thiết phù hợp storage. Disk/page access đắt, nên ta muốn fan-out lớn để giảm height. B-tree nodes chứa nhiều keys/children sao cho một node gần page/cache-block size. B+ tree thường giữ actual records/row pointers ở leaves và link leaves cho range scan.

Database index có thể chỉ cần 3–4 page reads để tìm trong hàng triệu rows nhờ fan-out lớn. Đây là ví dụ data structure được thiết kế theo I/O cost model, không chỉ comparison count.

## Heap và priority queue

Heap là tree-shaped partial order, thường lưu compact trong array. Min-heap invariant: parent ≤ children. Nó không fully sort elements; chỉ bảo đảm root là minimum.

Binary heap array mapping: children của index i thường ở `2i+1`, `2i+2`; parent ở `(i-1)//2`. Không cần pointers, locality tốt.

`peek-min O(1)`, insert và extract-min `O(log n)`. Priority queue dùng heap để scheduler lấy task priority cao nhất, Dijkstra lấy vertex distance nhỏ nhất, event simulation lấy next event.

## Trie: search theo prefix

Trie (prefix tree / 트라이) đi theo symbols của key. Lookup cost phụ thuộc key length hơn number of keys. Autocomplete, routing prefix và dictionaries dùng variants. Đổi lại memory overhead có thể lớn; compressed radix tree gộp chains để tiết kiệm.

## Tree traversal như một pattern computation

Nhiều algorithms trên hierarchical data là fold: tính kết quả node từ kết quả children. Directory size = file sizes + subtree sizes; expression tree evaluation = apply operator vào child results; compiler AST analysis tương tự.

## Balanced không luôn có nghĩa “đẹp”

Balance invariant tồn tại để bound height. Mỗi update phải trả giá rotations/restructuring. Nếu workload append-only rồi scan, một sorted array có thể tốt hơn tree. Nếu range queries nhiều và writes moderate, B+ tree hợp lý. Data structure phải match operations.

## Mental Model

> Tree biến một search space lớn thành hierarchy. Performance đến từ **height × cost per node**, vì vậy branching factor, balance và physical node size đều quan trọng.

## Common Misconceptions

**“Heap là sorted tree.”** Heap chỉ giữ parent-child order; siblings/subtrees không fully ordered.

**“BST lookup luôn O(log n).”** Chỉ khi height được giữ logarithmic hoặc input shape thuận lợi.

**“B-tree chỉ là BST nhiều children.”** Quan trọng nhất là node sizing/fan-out được thiết kế cho block/page access, làm cost model khác.

## Kết nối

Trees nối [memory locality](./02_memory_models_and_data_layout.md) với [database indexes](../05_data_databases/03_indexes_and_query_execution.md), [compiler AST](../04_programming_languages/03_compilers_interpreters_vm_and_jit.md), [filesystem](../03_operating_systems/04_filesystems_storage_and_io.md) và [graph algorithms](./06_graphs_and_graph_algorithms.md) vì tree là một graph đặc biệt.
