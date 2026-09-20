# Array, linked list, stack, queue và deque

Linear data structures tổ chức elements theo một chiều logical order. Chúng đơn giản nhưng là building blocks cho parsers, schedulers, buffers, graph traversal, caches và runtimes.

## Array: indexing đổi flexibility lấy locality

Array (배열 / mảng) lưu elements cùng size theo vùng contiguous. Nếu base address là `B`, element size `s`, address của `A[i]` là `B + i·s`. Chính phép tính này cho random access `O(1)`.

Static array có fixed size; dynamic array quản lý capacity và khi đầy allocate vùng lớn hơn, copy elements. Growth factor >1 làm append amortized `O(1)`. Nếu tăng capacity chỉ từng 1, tổng copy qua n appends thành `O(n²)`.

Array mạnh khi cần scanning, indexing, sorting và cache locality. Weakness là insertion/deletion giữa thường cần move tail.

## Linked list: order bằng references

Singly linked list mỗi node giữ value và next reference. Doubly linked list thêm prev. Nó không cần contiguous memory và có thể splice node nhanh khi đã có reference.

Nhưng `list[i]` cần traverse từ head, `O(n)`. Node overhead và poor cache locality làm nhiều workloads chậm hơn dynamic array dù complexity insert nghe hấp dẫn.

Linked list có giá trị khi nodes cần stable identity/address, frequent local splice hoặc làm building block cho intrusive lists/free lists.

## Stack: LIFO như một abstraction

Stack (스택 / ngăn xếp) có Last-In First-Out. Operations chính `push`, `pop`, `peek`. Implementation có thể dùng dynamic array hoặc linked list.

Call stack của execution runtime là ví dụ quan trọng: function call tạo frame; nested call push thêm; return pop frame. Nhưng “stack data structure” và “machine call stack” là cùng mental model, không phải lúc nào cùng implementation API.

Stacks xuất hiện trong DFS, expression evaluation, undo history và parsing nested delimiters.

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

Stack lưu unresolved openings — chính là minimal past state cần cho quyết định hiện tại.

## Queue: FIFO và xử lý công việc theo thời gian đến

Queue (큐 / hàng đợi) dùng First-In First-Out. `enqueue` thêm tail, `dequeue` lấy head. BFS dùng queue để khám phá graph theo distance layers. Producer/consumer systems dùng queue để decouple tốc độ hai phía.

Array queue không nên shift toàn bộ elements sau mỗi dequeue. Circular buffer dùng head/tail indices modulo capacity để giữ operations `O(1)`.

## Deque: hai đầu

Deque (double-ended queue / 덱) cho push/pop ở cả front và back. Nó có thể implement stack và queue. Sliding-window algorithms dùng deque để giữ candidates monotonic, đạt `O(n)` thay vì scan mỗi window `O(k)`.

## Ring buffer và bounded capacity

Ring/circular buffer đặc biệt hữu ích cho streaming và I/O. Capacity cố định khiến memory predictable. Khi full, policy có thể block producer, reject, drop newest hoặc overwrite oldest. Data structure không tự quyết semantic — system requirement quyết định overflow behavior.

Đây là bridge tới backpressure: queue không thể tăng vô hạn trong finite system.

## Sentinel, null và boundary conditions

Linear structures dễ có off-by-one bugs: empty vs one element, head/tail update, wraparound. Sentinel node hoặc half-open intervals có thể đơn giản hóa invariants.

Ví dụ dynamic array thường reasoning vùng valid `[0, size)` và allocated `[0, capacity)`, với invariant `0 ≤ size ≤ capacity`.

## Mental Model

> Chọn linear structure bằng access pattern: **random index → array; local splice với node reference → linked; newest-first → stack; oldest-first → queue; cả hai đầu → deque**. Sau đó kiểm tra locality, memory overhead và concurrency requirements.

## Common Misconceptions

**“Stack và queue là concrete structures.”** Chúng là abstract data types; có nhiều representations.

**“Queue luôn unbounded.”** Production queues nên có explicit capacity/policy, nếu không overload chỉ chuyển thành memory exhaustion.

**“Linked list delete O(1).”** Chỉ nếu đã có node và đủ references; tìm node vẫn có thể O(n).

## Kết nối

[Graph BFS/DFS](./06_graphs_and_graph_algorithms.md) dùng queue/stack; [OS scheduling](../03_operating_systems/01_processes_threads_and_scheduling.md) dùng run queues; [networking](../06_networks_distributed_systems/02_transport_tcp_udp_and_congestion.md) có packet buffers; [system boundaries](../08_software_systems/03_state_queues_backpressure_and_boundaries.md) mở rộng queue thành cơ chế điều tiết load.
