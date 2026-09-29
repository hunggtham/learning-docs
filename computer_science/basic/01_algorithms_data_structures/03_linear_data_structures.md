# Array, linked danh sách (list / 목록), ngăn xếp (stack / 스택), hàng đợi (queue / 큐) và deque

> **Mạch đọc:** Đọc **Array, linked danh sách (list / 목록), ngăn xếp (stack / 스택), hàng đợi (queue / 큐) và deque** như một mắt xích của lộ trình học (learning path / 학습 경로) hiện tại, không như một ghi chú tách rời. Nội dung đi từ **Array: indexing đổi flexibility lấy locality** sang **Linked danh sách (list / 목록): thứ tự (order / 순서) bằng references**; điểm nối này chuẩn bị câu hỏi cho các mục sau thay vì dừng ở định nghĩa đầu tiên.


Tuyến tính (linear / 선형) dữ liệu (data / 데이터) structures tổ chức elements theo một chiều logical thứ tự (order / 순서). Chúng đơn giản nhưng là building blocks cho parsers, schedulers, buffers, đồ thị (graph / 그래프) traversal, caches và runtimes.

## Array: indexing đổi flexibility lấy locality

Array (배열 / mảng) lưu elements cùng kích thước (size / 크기) theo vùng contiguous. Nếu cơ sở (base / 기반) address là `B`, element kích thước (size / 크기) `s`, address của `A[i]` là `B + i·s`. Chính phép tính này cho random truy cập (access / 접근) `O(1)`.

Static array có fixed kích thước (size / 크기); động (dynamic / 동적) array quản lý sức chứa (capacity / 용량) và khi đầy allocate vùng lớn hơn, bản sao (copy / 복사) elements. Growth factor >1 làm append amortized `O(1)`. Nếu tăng sức chứa (capacity / 용량) chỉ từng 1, tổng bản sao (copy / 복사) qua n appends thành `O(n²)`.

Array mạnh khi cần scanning, indexing, sorting và bộ nhớ đệm (cache / 캐시) locality. Weakness là insertion/deletion giữa thường cần move tail.


> **Chuyển mạch:** Từ **Array: indexing đổi flexibility lấy locality**, ta sang **Linked danh sách (list / 목록): thứ tự (order / 순서) bằng references** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## Linked danh sách (list / 목록): thứ tự (order / 순서) bằng references

Singly linked danh sách (list / 목록) mỗi nút (node / 노드) giữ giá trị (value / 값) và next tham chiếu (reference / 참조). Doubly linked danh sách (list / 목록) thêm prev. Nó không cần contiguous bộ nhớ (memory / 메모리) và có thể splice nút (node / 노드) nhanh khi đã có tham chiếu (reference / 참조).

Nhưng `list[i]` cần traverse từ head, `O(n)`. nút (node / 노드) overhead và poor bộ nhớ đệm (cache / 캐시) locality làm nhiều workloads chậm hơn động (dynamic / 동적) array dù độ phức tạp (complexity / 복잡도) insert nghe hấp dẫn.

Linked danh sách (list / 목록) có giá trị khi nodes cần stable định danh (identity / 식별자)/address, frequent cục bộ (local / 로컬) splice hoặc làm building khối (block / 블록) cho intrusive lists/free lists.


> **Chuyển mạch:** Từ **Linked danh sách (list / 목록): thứ tự (order / 순서) bằng references**, ta sang **ngăn xếp (stack / 스택): LIFO như một lớp trừu tượng (abstraction / 추상화)** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

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


> **Chuyển mạch:** Từ **ngăn xếp (stack / 스택): LIFO như một lớp trừu tượng (abstraction / 추상화)**, ta sang **hàng đợi (queue / 큐): FIFO và xử lý công việc theo thời gian đến** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## Hàng đợi (queue / 큐): FIFO và xử lý công việc theo thời gian đến

Hàng đợi (queue / 큐) dùng First-In First-Out. `enqueue` thêm tail, `dequeue` lấy head. BFS dùng hàng đợi (queue / 큐) để khám phá đồ thị (graph / 그래프) theo distance layers. Producer/bên tiêu thụ (consumer / 소비자) các hệ thống (systems / 시스템들) dùng hàng đợi (queue / 큐) để decouple tốc độ hai phía.

Array hàng đợi (queue / 큐) không nên shift toàn bộ elements sau mỗi dequeue. Circular buffer dùng head/tail indices modulo sức chứa (capacity / 용량) để giữ operations `O(1)`.


> **Chuyển mạch:** Từ **hàng đợi (queue / 큐): FIFO và xử lý công việc theo thời gian đến**, ta sang **Deque: hai đầu** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## Deque: hai đầu

Deque (double-ended queue / 덱) cho push/pop ở cả front và back. Nó có thể implement ngăn xếp (stack / 스택) và hàng đợi (queue / 큐). Sliding-window algorithms dùng deque để giữ candidates monotonic, đạt `O(n)` thay vì scan mỗi cửa sổ (window / 윈도우) `O(k)`.


> **Chuyển mạch:** Từ **Deque: hai đầu**, ta sang **Ring buffer và bounded sức chứa (capacity / 용량)** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## Ring buffer và bounded sức chứa (capacity / 용량)

Ring/circular buffer đặc biệt hữu ích cho streaming và I/O. sức chứa (capacity / 용량) cố định khiến bộ nhớ (memory / 메모리) predictable. Khi full, chính sách (policy / 정책) có thể khối (block / 블록) producer, reject, drop newest hoặc overwrite oldest. cấu trúc dữ liệu (data structure / 자료구조) không tự quyết ngữ nghĩa (semantic / 의미적) — hệ thống (system / 시스템) yêu cầu (requirement / 요구사항) quyết định overflow hành vi (behavior / 동작).

Đây là cầu nối (bridge / 브리지) tới backpressure: hàng đợi (queue / 큐) không thể tăng vô hạn trong finite hệ thống (system / 시스템).


> **Chuyển mạch:** Từ **Ring buffer và bounded sức chứa (capacity / 용량)**, ta sang **Sentinel, null và ranh giới (boundary / 경계) conditions** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## Sentinel, null và ranh giới (boundary / 경계) conditions

Tuyến tính (linear / 선형) structures dễ có off-by-one bugs: empty vs one element, head/tail cập nhật (update / 업데이트), wraparound. Sentinel nút (node / 노드) hoặc half-open intervals có thể đơn giản hóa invariants.

Ví dụ động (dynamic / 동적) array thường lập luận (reasoning / 추론) vùng valid `[0, size)` và allocated `[0, capacity)`, với bất biến (invariant / 불변식) `0 ≤ size ≤ capacity`.


> **Chuyển mạch:** Từ **Sentinel, null và ranh giới (boundary / 경계) conditions**, ta sang **mô hình tư duy (mental model / 사고 모델)** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## Mô hình tư duy (mental model / 사고 모델)

> Chọn tuyến tính (linear / 선형) cấu trúc (structure / 구조) bằng truy cập (access / 접근) mẫu (pattern / 패턴): **random chỉ mục (index / 인덱스) → array; cục bộ (local / 로컬) splice với nút (node / 노드) tham chiếu (reference / 참조) → linked; newest-first → ngăn xếp (stack / 스택); oldest-first → hàng đợi (queue / 큐); cả hai đầu → deque**. Sau đó kiểm tra locality, bộ nhớ (memory / 메모리) overhead và tính đồng thời (concurrency / 동시성) requirements.


> **Chuyển mạch:** Từ **mô hình tư duy (mental model / 사고 모델)**, ta sang **dùng chung (common / 공통) Misconceptions** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## Dùng chung (common / 공통) Misconceptions

**“ngăn xếp (stack / 스택) và hàng đợi (queue / 큐) là concrete structures.”** Chúng là abstract dữ liệu (data / 데이터) types; có nhiều representations.

**“hàng đợi (queue / 큐) luôn unbounded.”** môi trường vận hành (production / 운영 환경) queues nên có tường minh (explicit / 명시적) sức chứa (capacity / 용량)/chính sách (policy / 정책), nếu không overload chỉ chuyển thành bộ nhớ (memory / 메모리) exhaustion.

**“Linked danh sách (list / 목록) delete O(1).”** Chỉ nếu đã có nút (node / 노드) và đủ references; tìm nút (node / 노드) vẫn có thể O(n).


> **Chuyển mạch:** Từ **dùng chung (common / 공통) Misconceptions**, ta sang **Kết nối** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## Kết nối

[Graph BFS/DFS](./06_graphs_and_graph_algorithms.md) dùng hàng đợi (queue / 큐)/ngăn xếp (stack / 스택); [OS scheduling](../03_operating_systems/01_processes_threads_and_scheduling.md) dùng run queues; [networking](../06_networks_distributed_systems/02_transport_tcp_udp_and_congestion.md) có packet buffers; [system boundaries](../08_software_systems/03_state_queues_backpressure_and_boundaries.md) mở rộng hàng đợi (queue / 큐) thành cơ chế điều tiết tải (load / 로드).

> **Bàn giao:** Sau **Kết nối**, hãy chốt bất biến (invariant / 불변식) và giới hạn của mục này trước khi nối sang kiến thức kế tiếp. Có thể đọc tiếp [00 algorithmic thinking and correctness](./00_algorithmic_thinking_and_correctness.md) để đối chiếu ranh giới (boundary / 경계) gần nhất.
