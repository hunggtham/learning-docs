# Array, linked danh sách (list / 목록), ngăn xếp (stack / 스택), hàng đợi (queue / 큐) và deque

> **Mạch đọc:** [README](./README.md) là bản đồ owner của **Array, linked danh sách (list / 목록), ngăn xếp (stack / 스택), hàng đợi (queue / 큐) và deque**. Route đi từ layout/indexing → linked references → stack/queue semantics → deque và lựa chọn cấu trúc theo thao tác, để API và hiệu năng được cân bằng cùng locality.

Tuyến tính (linear / 선형) dữ liệu (data / 데이터) structures tổ chức elements theo một chiều logical thứ tự (order / 순서). Chúng đơn giản nhưng là building blocks cho parsers, schedulers, buffers, đồ thị (graph / 그래프) traversal, caches và runtimes.

## Array: indexing đổi flexibility lấy locality

Array (배열 / mảng) lưu elements cùng kích thước (size / 크기) theo vùng contiguous. Nếu cơ sở (base / 기반) address là `B`, element kích thước (size / 크기) `s`, address của `A[i]` là `B + i·s`. Chính phép tính này cho random truy cập (access / 접근) `O(1)`.

Static array có fixed kích thước (size / 크기); động (dynamic / 동적) array quản lý sức chứa (capacity / 용량) và khi đầy allocate vùng lớn hơn, bản sao (copy / 복사) elements. Growth factor >1 làm append amortized `O(1)`. Nếu tăng sức chứa (capacity / 용량) chỉ từng 1, tổng bản sao (copy / 복사) qua n appends thành `O(n²)`.

Array mạnh khi cần scanning, indexing, sorting và bộ nhớ đệm (cache / 캐시) locality. Weakness là insertion/deletion giữa thường cần move tail.

> **Nối mạch:** **Linked danh sách (list / 목록): thứ tự (order / 순서) bằng references** nối từ **Array: indexing đổi flexibility lấy locality** sang **Ngăn xếp (stack / 스택): LIFO như một lớp trừu tượng (abstraction / 추상화)**, vì layout trước quyết định cách cấu trúc sau quản lý thứ tự.

## Linked danh sách (list / 목록): thứ tự (order / 순서) bằng references

Singly linked danh sách (list / 목록) mỗi nút (node / 노드) giữ giá trị (value / 값) và next tham chiếu (reference / 참조). Doubly linked danh sách (list / 목록) thêm prev. Nó không cần contiguous bộ nhớ (memory / 메모리) và có thể splice nút (node / 노드) nhanh khi đã có tham chiếu (reference / 참조).

Nhưng `list[i]` cần traverse từ head, `O(n)`. nút (node / 노드) overhead và poor bộ nhớ đệm (cache / 캐시) locality làm nhiều workloads chậm hơn động (dynamic / 동적) array dù độ phức tạp (complexity / 복잡도) insert nghe hấp dẫn.

Linked danh sách (list / 목록) có giá trị khi nodes cần stable định danh (identity / 식별자)/address, frequent cục bộ (local / 로컬) splice hoặc làm building khối (block / 블록) cho intrusive lists/free lists.

> **Nối mạch:** **Ngăn xếp (stack / 스택): LIFO như một lớp trừu tượng (abstraction / 추상화)** nối từ **Linked danh sách (list / 목록): thứ tự (order / 순서) bằng references** sang **Hàng đợi (queue / 큐): FIFO và xử lý công việc theo thời gian đến**, vì cơ chế trước tạo đầu vào cho bước sau.

## Ngăn xếp (stack / 스택): LIFO như một lớp trừu tượng (abstraction / 추상화)

Ngăn xếp (stack / 스택) có Last-In First-Out. Operations chính `push`, `pop`, `peek`. hiện thực (implementation / 구현) có thể dùng động (dynamic / 동적) array hoặc linked danh sách (list / 목록).

Ngăn xếp lời gọi (call stack / 호출 스택) của thực thi (execution / 실행) thời gian chạy (runtime / 런타임) là ví dụ quan trọng: hàm (function / 함수) lời gọi (call / 호출) tạo frame; nested lời gọi (call / 호출) push thêm; return pop frame. Nhưng “ngăn xếp (stack / 스택) cấu trúc dữ liệu (data structure / 자료구조)” và “machine ngăn xếp lời gọi (call stack / 호출 스택)” là cùng mô hình tư duy (mental model / 사고 모델), không phải lúc nào cùng hiện thực (implementation / 구현) API.

Stacks xuất hiện trong DFS, expression evaluation, undo lịch sử (history / 이력) và parsing nested delimiters.

Ví dụ kiểm tra parentheses:

```text
for token in input:
    if token is opening:
        push(token)
    else if token is closing:
        if stack empty or top mismatches: reject
        pop()
accept iff stack empty
```

Ngăn xếp (stack / 스택) lưu unresolved openings — chính là minimal past trạng thái (state / 상태) cần cho quyết định hiện tại.

> **Nối mạch:** **Hàng đợi (queue / 큐): FIFO và xử lý công việc theo thời gian đến** nối từ **Ngăn xếp (stack / 스택): LIFO như một lớp trừu tượng (abstraction / 추상화)** sang **Deque: hai đầu**, vì cơ chế trước tạo đầu vào cho bước sau.

## Hàng đợi (queue / 큐): FIFO và xử lý công việc theo thời gian đến

Hàng đợi (queue / 큐) dùng First-In First-Out. `enqueue` thêm tail, `dequeue` lấy head. BFS dùng hàng đợi (queue / 큐) để khám phá đồ thị (graph / 그래프) theo distance layers. Producer/bên tiêu thụ (consumer / 소비자) các hệ thống (systems / 시스템들) dùng hàng đợi (queue / 큐) để decouple tốc độ hai phía.

Array hàng đợi (queue / 큐) không nên shift toàn bộ elements sau mỗi dequeue. Circular buffer dùng head/tail indices modulo sức chứa (capacity / 용량) để giữ operations `O(1)`.

> **Nối mạch:** **Deque: hai đầu** nối từ **Hàng đợi (queue / 큐): FIFO và xử lý công việc theo thời gian đến** sang **Ring buffer và bounded sức chứa (capacity / 용량)**, vì cơ chế trước tạo đầu vào cho bước sau.

## Deque: hai đầu

Deque (double-ended queue / 덱) cho push/pop ở cả front và back. Nó có thể implement ngăn xếp (stack / 스택) và hàng đợi (queue / 큐). Sliding-window algorithms dùng deque để giữ candidates monotonic, đạt `O(n)` thay vì scan mỗi cửa sổ (window / 윈도우) `O(k)`.

> **Nối mạch:** **Ring buffer và bounded sức chứa (capacity / 용량)** nối từ **Deque: hai đầu** sang **Sentinel, null và ranh giới (boundary / 경계) conditions**, vì cơ chế trước tạo đầu vào cho bước sau.

## Ring buffer và bounded sức chứa (capacity / 용량)

Ring/circular buffer đặc biệt hữu ích cho streaming và I/O. sức chứa (capacity / 용량) cố định khiến bộ nhớ (memory / 메모리) predictable. Khi full, chính sách (policy / 정책) có thể khối (block / 블록) producer, reject, drop newest hoặc overwrite oldest. cấu trúc dữ liệu (data structure / 자료구조) không tự quyết ngữ nghĩa (semantic / 의미적) — hệ thống (system / 시스템) yêu cầu (requirement / 요구사항) quyết định overflow hành vi (behavior / 동작).

Đây là cầu nối (bridge / 브리지) tới backpressure: hàng đợi (queue / 큐) không thể tăng vô hạn trong finite hệ thống (system / 시스템).

> **Nối mạch:** **Ring buffer và bounded sức chứa (capacity / 용량)** đặt tiêu chí; **Sentinel, null và ranh giới (boundary / 경계) conditions** dùng nó để kiểm tra ranh giới, rồi **Mô hình tư duy (mental model / 사고 모델)** mở rộng hệ quả.

## Sentinel, null và ranh giới (boundary / 경계) conditions

Tuyến tính (linear / 선형) structures dễ có off-by-one bugs: empty vs one element, head/tail cập nhật (update / 업데이트), wraparound. Sentinel nút (node / 노드) hoặc half-open intervals có thể đơn giản hóa invariants.

Ví dụ động (dynamic / 동적) array thường lập luận (reasoning / 추론) vùng valid `[0, size)` và allocated `[0, capacity)`, với bất biến (invariant / 불변식) `0 ≤ size ≤ capacity`.

> **Nối mạch:** **Sentinel, null và ranh giới (boundary / 경계) conditions** đặt tiêu chí; **Mô hình tư duy (mental model / 사고 모델)** dùng nó để kiểm tra ranh giới, rồi **Dùng chung (common / 공통) Misconceptions** mở rộng hệ quả.

## Mô hình tư duy (mental model / 사고 모델)

> Chọn tuyến tính (linear / 선형) cấu trúc (structure / 구조) bằng truy cập (access / 접근) mẫu (pattern / 패턴): **random chỉ mục (index / 인덱스) → array; cục bộ (local / 로컬) splice với nút (node / 노드) tham chiếu (reference / 참조) → linked; newest-first → ngăn xếp (stack / 스택); oldest-first → hàng đợi (queue / 큐); cả hai đầu → deque**. Sau đó kiểm tra locality, bộ nhớ (memory / 메모리) overhead và tính đồng thời (concurrency / 동시성) requirements.

> **Nối mạch:** **Dùng chung (common / 공통) Misconceptions** tổng hợp từ **Mô hình tư duy (mental model / 사고 모델)**; **Kết nối** mở rộng mạch bằng hệ quả hoặc giới hạn liên quan.

## Dùng chung (common / 공통) Misconceptions

**“ngăn xếp (stack / 스택) và hàng đợi (queue / 큐) là concrete structures.”** Chúng là abstract dữ liệu (data / 데이터) types; có nhiều representations.

**“hàng đợi (queue / 큐) luôn unbounded.”** môi trường vận hành (production / 운영 환경) queues nên có tường minh (explicit / 명시적) sức chứa (capacity / 용량)/chính sách (policy / 정책), nếu không overload chỉ chuyển thành bộ nhớ (memory / 메모리) exhaustion.

**“Linked danh sách (list / 목록) delete O(1).”** Chỉ nếu đã có nút (node / 노드) và đủ references; tìm nút (node / 노드) vẫn có thể O(n).

> **Nối mạch:** **Kết nối** tổng hợp từ **Dùng chung (common / 공통) Misconceptions**; mục sau khép mạch bằng giới hạn và ứng dụng.

## Kết nối

[Graph BFS/DFS](./06_graphs_and_graph_algorithms.md) dùng hàng đợi (queue / 큐)/ngăn xếp (stack / 스택); [OS scheduling](../03_operating_systems/01_processes_threads_and_scheduling.md) dùng run queues; [networking](../06_networks_distributed_systems/02_transport_tcp_udp_and_congestion.md) có packet buffers; [system boundaries](../08_software_systems/03_state_queues_backpressure_and_boundaries.md) mở rộng hàng đợi (queue / 큐) thành cơ chế điều tiết tải (load / 로드).

> **Bàn giao:** Sau **Kết nối**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](./README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
