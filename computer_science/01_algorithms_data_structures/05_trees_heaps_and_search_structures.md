# Cây (tree / 트리), vùng nhớ động (heap / 힙) và ordered tìm kiếm (search / 검색) structures

> **Mạch đọc:** [README](./README.md) là bản đồ owner của **Cây (tree / 트리), vùng nhớ động (heap / 힙) và ordered tìm kiếm (search / 검색) structures**. Route đi từ tree vocabulary/shape → BST và ordered search → heap/priority queue → balancing, updates và complexity, để cấu trúc thứ bậc được nối với invariant và thao tác.

Cây (tree / 트리) biểu diễn hierarchy và recursive decomposition. Filesystem directories, DOM, AST, cơ sở dữ liệu (database / 데이터베이스) indexes và organizational structures đều có tree-like shape. Nhưng không phải mọi cây (tree / 트리) phục vụ cùng thao tác (operation / 연산); shape và bất biến (invariant / 불변식) quyết định hiệu năng (performance / 성능).

## Cây (tree / 트리) vocabulary từ cấu trúc (structure / 구조)

Một rooted cây (tree / 트리) có gốc (root / 루트), parent/child, leaves, độ sâu (depth / 깊이) và height. Mỗi nút (node / 노드) trừ gốc (root / 루트) có đúng một parent, và không có cycle. Với n nodes, cây (tree / 트리) connected có n−1 edges.

Recursive definition tự nhiên: cây (tree / 트리) là gốc (root / 루트) cộng một tập subtrees. Vì vậy recursion hoặc tường minh (explicit / 명시적) ngăn xếp (stack / 스택) thường dùng traversal.

DFS traversals gồm preorder, inorder, postorder tùy vị trí xử lý nút (node / 노드). BFS/level-order dùng hàng đợi (queue / 큐).

> **Nối mạch:** **Tìm kiếm nhị phân (binary search / 이진 탐색) cây (tree / 트리)** nối từ **Cây (tree / 트리) vocabulary từ cấu trúc (structure / 구조)** sang **B-tree và B+ cây (tree / 트리)**, vì cơ chế trước tạo đầu vào cho bước sau.

## Tìm kiếm nhị phân (binary search / 이진 탐색) cây (tree / 트리)

BST đặt thứ tự (ordering / 순서) bất biến (invariant / 불변식): keys trong left subtree nhỏ hơn nút (node / 노드); right lớn hơn, với duplicate chính sách (policy / 정책) tường minh (explicit / 명시적). Lookup so sánh key và loại bỏ một subtree mỗi step.

Nếu cây (tree / 트리) balanced, height O(log n). Nếu insert sorted chuỗi (sequence / 시퀀스) vào naive BST, nó degenerates thành chuỗi (chain / 사슬) height O(n). Vì vậy độ phức tạp (complexity / 복잡도) dựa vào shape.

Self-balancing trees như AVL hoặc Red-Black cây (tree / 트리) dùng rotations và balance siêu dữ liệu (metadata / 메타데이터) để giữ height O(log n). thư viện chuẩn (standard library / 표준 라이브러리) ordered map/set thường dùng một dạng balanced cây (tree / 트리).

> **Nối mạch:** **B-tree và B+ cây (tree / 트리)** nối từ **Tìm kiếm nhị phân (binary search / 이진 탐색) cây (tree / 트리)** sang **Vùng nhớ vùng nhớ động (heap / 힙) và priority hàng đợi (queue / 큐)**, vì cơ chế trước tạo đầu vào cho bước sau.

## B-tree và B+ cây (tree / 트리)

Nhị phân (binary / 이진) cây (tree / 트리) tối ưu không nhất thiết phù hợp lưu trữ (storage / 저장소). Disk/page truy cập (access / 접근) đắt, nên ta muốn fan-out lớn để giảm height. B-tree nodes chứa nhiều keys/children sao cho một nút (node / 노드) gần page/cache-block kích thước (size / 크기). B+ cây (tree / 트리) thường giữ actual records/row pointers ở leaves và link leaves cho phạm vi (range / 범위) scan.

Cơ sở dữ liệu (database / 데이터베이스) chỉ mục (index / 인덱스) có thể chỉ cần 3–4 page reads để tìm trong hàng triệu rows nhờ fan-out lớn. Đây là ví dụ cấu trúc dữ liệu (data structure / 자료구조) được thiết kế theo I/O chi phí (cost / 비용) mô hình (model / 모델), không chỉ comparison count.

> **Nối mạch:** **Vùng nhớ vùng nhớ động (heap / 힙) và priority hàng đợi (queue / 큐)** nối từ **B-tree và B+ cây (tree / 트리)** sang **Trie: tìm kiếm (search / 검색) theo prefix**, vì cơ chế trước tạo đầu vào cho bước sau.

## Vùng nhớ vùng nhớ động (heap / 힙) và priority hàng đợi (queue / 큐)

Vùng nhớ vùng nhớ động (heap / 힙) là tree-shaped partial thứ tự (order / 순서), thường lưu compact trong array. Min-heap bất biến (invariant / 불변식): parent ≤ children. Nó không fully sort elements; chỉ bảo đảm gốc (root / 루트) là minimum.

Nhị phân (binary / 이진) vùng nhớ động (heap / 힙) array ánh xạ (mapping / 매핑): children của chỉ mục (index / 인덱스) i thường ở `2i+1`, `2i+2`; parent ở `(i-1)//2`. Không cần pointers, locality tốt.

`peek-min O(1)`, insert và extract-min `O(log n)`. Priority hàng đợi (queue / 큐) dùng vùng nhớ động (heap / 힙) để scheduler lấy tác vụ (task / 작업) priority cao nhất, Dijkstra lấy vertex distance nhỏ nhất, sự kiện (event / 이벤트) simulation lấy next sự kiện (event / 이벤트).

> **Nối mạch:** **Trie: tìm kiếm (search / 검색) theo prefix** nối từ **Vùng nhớ vùng nhớ động (heap / 힙) và priority hàng đợi (queue / 큐)** sang **Cây (tree / 트리) traversal như một mẫu (pattern / 패턴) computation**, vì cơ chế trước tạo đầu vào cho bước sau.

## Trie: tìm kiếm (search / 검색) theo prefix

Trie (prefix tree / 트라이) đi theo symbols của key. Lookup chi phí (cost / 비용) phụ thuộc key length hơn number of keys. Autocomplete, routing prefix và dictionaries dùng variants. Đổi lại bộ nhớ (memory / 메모리) overhead có thể lớn; compressed radix cây (tree / 트리) gộp chains để tiết kiệm.

> **Nối mạch:** **Cây (tree / 트리) traversal như một mẫu (pattern / 패턴) computation** nối từ **Trie: tìm kiếm (search / 검색) theo prefix** sang **Balanced không luôn có nghĩa “đẹp”**, vì cơ chế trước tạo đầu vào cho bước sau.

## Cây (tree / 트리) traversal như một mẫu (pattern / 패턴) computation

Nhiều algorithms trên hierarchical dữ liệu (data / 데이터) là fold: tính kết quả nút (node / 노드) từ kết quả children. Directory kích thước (size / 크기) = tệp (file / 파일) sizes + subtree sizes; expression cây (tree / 트리) evaluation = apply operator vào child results; trình biên dịch (compiler / 컴파일러) AST phân tích (analysis / 분석) tương tự.

> **Nối mạch:** **Balanced không luôn có nghĩa “đẹp”** nối từ **Cây (tree / 트리) traversal như một mẫu (pattern / 패턴) computation** sang **Mô hình tư duy (mental model / 사고 모델)**, vì cơ chế trước tạo đầu vào cho bước sau.

## Balanced không luôn có nghĩa “đẹp”

Balance bất biến (invariant / 불변식) tồn tại để bound height. Mỗi cập nhật (update / 업데이트) phải trả giá rotations/restructuring. Nếu tải công việc (workload / 워크로드) append-only rồi scan, một sorted array có thể tốt hơn cây (tree / 트리). Nếu phạm vi (range / 범위) queries nhiều và writes moderate, B+ cây (tree / 트리) hợp lý. cấu trúc dữ liệu (data structure / 자료구조) phải match operations.

> **Nối mạch:** **Mô hình tư duy (mental model / 사고 모델)** tổng hợp từ **Balanced không luôn có nghĩa “đẹp”**; **Dùng chung (common / 공통) Misconceptions** mở rộng mạch bằng hệ quả hoặc giới hạn liên quan.

## Mô hình tư duy (mental model / 사고 모델)

> cây (tree / 트리) biến một tìm kiếm (search / 검색) không gian (space / 공간) lớn thành hierarchy. hiệu năng (performance / 성능) đến từ **height × chi phí (cost / 비용) per nút (node / 노드)**, vì vậy branching factor, balance và vật lý (physical / 물리적) nút (node / 노드) kích thước (size / 크기) đều quan trọng.

> **Nối mạch:** **Dùng chung (common / 공통) Misconceptions** tổng hợp từ **Mô hình tư duy (mental model / 사고 모델)**; **Kết nối** mở rộng mạch bằng hệ quả hoặc giới hạn liên quan.

## Dùng chung (common / 공통) Misconceptions

**“vùng nhớ động (heap / 힙) là sorted cây (tree / 트리).”** vùng nhớ động (heap / 힙) chỉ giữ parent-child thứ tự (order / 순서); siblings/subtrees không fully ordered.

**“BST lookup luôn O(log n).”** Chỉ khi height được giữ logarithmic hoặc đầu vào (input / 입력) shape thuận lợi.

**“B-tree chỉ là BST nhiều children.”** Quan trọng nhất là nút (node / 노드) sizing/fan-out được thiết kế cho khối (block / 블록)/page truy cập (access / 접근), làm chi phí (cost / 비용) mô hình (model / 모델) khác.

> **Nối mạch:** **Kết nối** tổng hợp từ **Dùng chung (common / 공통) Misconceptions**; mục sau khép mạch bằng giới hạn và ứng dụng.

## Kết nối

Trees nối [memory locality](./02_memory_models_and_data_layout.md) với [database indexes](../05_data_databases/03_indexes_and_query_execution.md), [compiler AST](../04_programming_languages/03_compilers_interpreters_vm_and_jit.md), [filesystem](../03_operating_systems/04_filesystems_storage_and_io.md) và [graph algorithms](./06_graphs_and_graph_algorithms.md) vì cây (tree / 트리) là một đồ thị (graph / 그래프) đặc biệt.

> **Bàn giao:** Sau **Kết nối**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](./README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
