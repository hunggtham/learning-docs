# Cây (tree / 트리), vùng nhớ động (heap / 힙) và ordered tìm kiếm (search / 검색) structures

> **Mạch đọc:** [README](./README.md) là bản đồ owner của **Cây (tree / 트리), vùng nhớ động (heap / 힙) và ordered tìm kiếm (search / 검색) structures**. Route đi từ tree vocabulary/shape → BST và ordered search → heap/priority queue → balancing, updates và complexity, để cấu trúc thứ bậc được nối với invariant và thao tác.

Cây (tree / 트리) biểu diễn hierarchy và recursive decomposition. Filesystem directories, DOM, AST, cơ sở dữ liệu (database / 데이터베이스) indexes và organizational structures đều có tree-like shape. Nhưng không phải mọi cây (tree / 트리) phục vụ cùng thao tác (operation / 연산); shape và bất biến (invariant / 불변식) quyết định hiệu năng (performance / 성능).

## Cây (tree / 트리) vocabulary từ cấu trúc (structure / 구조)

Một rooted cây (tree / 트리) có gốc (root / 루트), parent/child, leaves, độ sâu (depth / 깊이) và height. Mỗi nút (node / 노드) trừ gốc (root / 루트) có đúng một parent, và không có cycle. Với n nodes, cây (tree / 트리) connected có n−1 edges.

Recursive definition tự nhiên: cây (tree / 트리) là gốc (root / 루트) cộng một tập subtrees. Vì vậy recursion hoặc tường minh (explicit / 명시적) ngăn xếp (stack / 스택) thường dùng traversal.

DFS traversals gồm preorder, inorder, postorder tùy vị trí xử lý nút (node / 노드). BFS/level-order dùng hàng đợi (queue / 큐).

> **Chuyển mạch:** Trong **Cây (tree / 트리), vùng nhớ động (heap / 힙) và ordered tìm kiếm (search / 검색) structures**, **Tìm kiếm nhị phân (binary search / 이진 탐색) cây (tree / 트리)** tiếp nhận điểm tựa từ **Cây (tree / 트리) vocabulary từ cấu trúc (structure / 구조)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **B-tree và B+ cây (tree / 트리)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Tìm kiếm nhị phân (binary search / 이진 탐색) cây (tree / 트리)

BST đặt thứ tự (ordering / 순서) bất biến (invariant / 불변식): keys trong left subtree nhỏ hơn nút (node / 노드); right lớn hơn, với duplicate chính sách (policy / 정책) tường minh (explicit / 명시적). Lookup so sánh key và loại bỏ một subtree mỗi step.

Nếu cây (tree / 트리) balanced, height O(log n). Nếu insert sorted chuỗi (sequence / 시퀀스) vào naive BST, nó degenerates thành chuỗi (chain / 사슬) height O(n). Vì vậy độ phức tạp (complexity / 복잡도) dựa vào shape.

Self-balancing trees như AVL hoặc Red-Black cây (tree / 트리) dùng rotations và balance siêu dữ liệu (metadata / 메타데이터) để giữ height O(log n). thư viện chuẩn (standard library / 표준 라이브러리) ordered map/set thường dùng một dạng balanced cây (tree / 트리).

> **Chuyển mạch:** Ở chặng này của **Cây (tree / 트리), vùng nhớ động (heap / 힙) và ordered tìm kiếm (search / 검색) structures**, **B-tree và B+ cây (tree / 트리)** tiếp nhận điểm tựa từ **Tìm kiếm nhị phân (binary search / 이진 탐색) cây (tree / 트리)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Vùng nhớ vùng nhớ động (heap / 힙) và priority hàng đợi (queue / 큐)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## B-tree và B+ cây (tree / 트리)

Nhị phân (binary / 이진) cây (tree / 트리) tối ưu không nhất thiết phù hợp lưu trữ (storage / 저장소). Disk/page truy cập (access / 접근) đắt, nên ta muốn fan-out lớn để giảm height. B-tree nodes chứa nhiều keys/children sao cho một nút (node / 노드) gần page/cache-block kích thước (size / 크기). B+ cây (tree / 트리) thường giữ actual records/row pointers ở leaves và link leaves cho phạm vi (range / 범위) scan.

Cơ sở dữ liệu (database / 데이터베이스) chỉ mục (index / 인덱스) có thể chỉ cần 3–4 page reads để tìm trong hàng triệu rows nhờ fan-out lớn. Đây là ví dụ cấu trúc dữ liệu (data structure / 자료구조) được thiết kế theo I/O chi phí (cost / 비용) mô hình (model / 모델), không chỉ comparison count.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Cây (tree / 트리), vùng nhớ động (heap / 힙) và ordered tìm kiếm (search / 검색) structures**, **Vùng nhớ vùng nhớ động (heap / 힙) và priority hàng đợi (queue / 큐)** tiếp nhận điểm tựa từ **B-tree và B+ cây (tree / 트리)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Trie: tìm kiếm (search / 검색) theo prefix** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Vùng nhớ vùng nhớ động (heap / 힙) và priority hàng đợi (queue / 큐)

Vùng nhớ vùng nhớ động (heap / 힙) là tree-shaped partial thứ tự (order / 순서), thường lưu compact trong array. Min-heap bất biến (invariant / 불변식): parent ≤ children. Nó không fully sort elements; chỉ bảo đảm gốc (root / 루트) là minimum.

Nhị phân (binary / 이진) vùng nhớ động (heap / 힙) array ánh xạ (mapping / 매핑): children của chỉ mục (index / 인덱스) i thường ở `2i+1`, `2i+2`; parent ở `(i-1)//2`. Không cần pointers, locality tốt.

`peek-min O(1)`, insert và extract-min `O(log n)`. Priority hàng đợi (queue / 큐) dùng vùng nhớ động (heap / 힙) để scheduler lấy tác vụ (task / 작업) priority cao nhất, Dijkstra lấy vertex distance nhỏ nhất, sự kiện (event / 이벤트) simulation lấy next sự kiện (event / 이벤트).

> **Chuyển mạch:** Trong **Cây (tree / 트리), vùng nhớ động (heap / 힙) và ordered tìm kiếm (search / 검색) structures**, **Trie: tìm kiếm (search / 검색) theo prefix** tiếp nhận điểm tựa từ **Vùng nhớ vùng nhớ động (heap / 힙) và priority hàng đợi (queue / 큐)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Cây (tree / 트리) traversal như một mẫu (pattern / 패턴) computation** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Trie: tìm kiếm (search / 검색) theo prefix

Trie (prefix tree / 트라이) đi theo symbols của key. Lookup chi phí (cost / 비용) phụ thuộc key length hơn number of keys. Autocomplete, routing prefix và dictionaries dùng variants. Đổi lại bộ nhớ (memory / 메모리) overhead có thể lớn; compressed radix cây (tree / 트리) gộp chains để tiết kiệm.

> **Chuyển mạch:** Ở chặng này của **Cây (tree / 트리), vùng nhớ động (heap / 힙) và ordered tìm kiếm (search / 검색) structures**, **Cây (tree / 트리) traversal như một mẫu (pattern / 패턴) computation** tiếp nhận điểm tựa từ **Trie: tìm kiếm (search / 검색) theo prefix** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Balanced không luôn có nghĩa “đẹp”** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Cây (tree / 트리) traversal như một mẫu (pattern / 패턴) computation

Nhiều algorithms trên hierarchical dữ liệu (data / 데이터) là fold: tính kết quả nút (node / 노드) từ kết quả children. Directory kích thước (size / 크기) = tệp (file / 파일) sizes + subtree sizes; expression cây (tree / 트리) evaluation = apply operator vào child results; trình biên dịch (compiler / 컴파일러) AST phân tích (analysis / 분석) tương tự.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Cây (tree / 트리), vùng nhớ động (heap / 힙) và ordered tìm kiếm (search / 검색) structures**, **Balanced không luôn có nghĩa “đẹp”** tiếp nhận điểm tựa từ **Cây (tree / 트리) traversal như một mẫu (pattern / 패턴) computation** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Mô hình tư duy (mental model / 사고 모델)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Balanced không luôn có nghĩa “đẹp”

Balance bất biến (invariant / 불변식) tồn tại để bound height. Mỗi cập nhật (update / 업데이트) phải trả giá rotations/restructuring. Nếu tải công việc (workload / 워크로드) append-only rồi scan, một sorted array có thể tốt hơn cây (tree / 트리). Nếu phạm vi (range / 범위) queries nhiều và writes moderate, B+ cây (tree / 트리) hợp lý. cấu trúc dữ liệu (data structure / 자료구조) phải match operations.

> **Chuyển mạch:** Trong **Cây (tree / 트리), vùng nhớ động (heap / 힙) và ordered tìm kiếm (search / 검색) structures**, **Mô hình tư duy (mental model / 사고 모델)** gom các mảnh từ **Balanced không luôn có nghĩa “đẹp”** thành một kết luận có thể mang sang phần kế tiếp. Từ đây, **Dùng chung (common / 공통) Misconceptions** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Mô hình tư duy (mental model / 사고 모델)

> cây (tree / 트리) biến một tìm kiếm (search / 검색) không gian (space / 공간) lớn thành hierarchy. hiệu năng (performance / 성능) đến từ **height × chi phí (cost / 비용) per nút (node / 노드)**, vì vậy branching factor, balance và vật lý (physical / 물리적) nút (node / 노드) kích thước (size / 크기) đều quan trọng.

> **Chuyển mạch:** Ở chặng này của **Cây (tree / 트리), vùng nhớ động (heap / 힙) và ordered tìm kiếm (search / 검색) structures**, **Dùng chung (common / 공통) Misconceptions** gom các mảnh từ **Mô hình tư duy (mental model / 사고 모델)** thành một kết luận có thể mang sang phần kế tiếp. Từ đây, **Kết nối** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Dùng chung (common / 공통) Misconceptions

**“vùng nhớ động (heap / 힙) là sorted cây (tree / 트리).”** vùng nhớ động (heap / 힙) chỉ giữ parent-child thứ tự (order / 순서); siblings/subtrees không fully ordered.

**“BST lookup luôn O(log n).”** Chỉ khi height được giữ logarithmic hoặc đầu vào (input / 입력) shape thuận lợi.

**“B-tree chỉ là BST nhiều children.”** Quan trọng nhất là nút (node / 노드) sizing/fan-out được thiết kế cho khối (block / 블록)/page truy cập (access / 접근), làm chi phí (cost / 비용) mô hình (model / 모델) khác.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Cây (tree / 트리), vùng nhớ động (heap / 힙) và ordered tìm kiếm (search / 검색) structures**, **Kết nối** tiếp nhận điểm tựa từ **Dùng chung (common / 공통) Misconceptions** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Phần còn lại của file dùng kết quả này để khép lại mạch giải thích.

## Kết nối

Trees nối [memory locality](./02_memory_models_and_data_layout.md) với [database indexes](../05_data_databases/03_indexes_and_query_execution.md), [compiler AST](../04_programming_languages/03_compilers_interpreters_vm_and_jit.md), [filesystem](../03_operating_systems/04_filesystems_storage_and_io.md) và [graph algorithms](./06_graphs_and_graph_algorithms.md) vì cây (tree / 트리) là một đồ thị (graph / 그래프) đặc biệt.

> **Bàn giao:** Sau **Kết nối**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](./README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
