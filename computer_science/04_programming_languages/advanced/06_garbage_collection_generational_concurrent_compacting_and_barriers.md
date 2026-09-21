# Garbage collection: thế hệ, concurrent, compacting và write barrier

**Bộ gom rác (garbage collector, GC / 가비지 컬렉터)** là cơ chế runtime tự động tìm những object không còn có thể được chương trình sử dụng và thu hồi vùng nhớ của chúng. Để hiểu GC sâu, trước hết phải tách ba khái niệm thường bị trộn lẫn: **cấp phát bộ nhớ (allocation)** là tạo vùng nhớ mới; **khả năng truy cập (reachability)** là object còn được đi tới từ các root hay không; **thu hồi (reclamation)** là trả vùng nhớ của object không còn reachable về cho allocator.

GC không “biết object nào còn hữu ích về mặt nghiệp vụ”. Nó chỉ suy luận từ graph tham chiếu mà runtime nhìn thấy. Nếu một cache giữ reference tới object không còn cần thiết, GC vẫn coi object đó đang sống. Vì vậy memory leak vẫn có thể xảy ra trong ngôn ngữ có GC.

## 1. Root và object graph

Runtime bắt đầu từ các **điểm gốc (GC roots)** như stack frame đang hoạt động, biến tĩnh, register hoặc handle native. Từ các root, collector duyệt graph object.

```text
GC roots
  |
  +--> A --> B
  |
  +--> C

D --> E   // không còn đường đi từ root
```

`D` và `E` có thể được thu hồi dù chúng vẫn trỏ lẫn nhau. Đây là khác biệt quan trọng so với reference counting thuần túy, vốn có thể gặp vấn đề cycle.

## 2. Mark–sweep: mô hình cơ bản

Một collector đơn giản có hai pha:

```text
mark  -> đánh dấu object reachable
sweep -> quét heap và thu hồi object chưa được đánh dấu
```

Mark–sweep dễ hiểu nhưng có thể để lại **phân mảnh (fragmentation)**: vùng trống nằm rải rác, khiến object lớn khó tìm chỗ liên tục và locality kém.

## 3. Compacting collector

**Nén heap (compaction)** di chuyển object sống về gần nhau rồi cập nhật reference. Lợi ích là giảm fragmentation và cải thiện locality.

Nhưng di chuyển object tạo chi phí. Runtime phải biết mọi reference cần sửa; code native giữ raw pointer vào object managed cũng trở thành vấn đề. Đây là lý do FFI, pinning và object movement liên quan chặt với thiết kế GC.

## 4. Stop-the-world là gì?

Trong một số giai đoạn GC, runtime phải dừng các thread ứng dụng tại **điểm an toàn (safepoint)**. Khoảng dừng này gọi là **stop-the-world pause**.

Pause không đồng nghĩa toàn bộ công việc GC đều diễn ra khi ứng dụng dừng. Collector hiện đại có thể làm nhiều pha concurrent, nhưng vẫn thường cần một số synchronization point để có snapshot nhất quán hoặc cập nhật metadata.

Đối với dịch vụ latency-sensitive, p99/p999 pause quan trọng hơn thời gian GC trung bình.

## 5. Generational hypothesis

Nhiều workload tạo rất nhiều object sống ngắn. **Giả thuyết thế hệ (generational hypothesis)** nói rằng object trẻ có xác suất chết sớm cao hơn object đã sống qua nhiều chu kỳ.

Heap vì vậy có thể chia thành thế hệ trẻ và già:

```text
young generation -> thu gom thường xuyên
old generation   -> thu gom ít hơn
```

Minor GC chỉ quét phần trẻ nên rẻ hơn full-heap collection. Object sống lâu có thể được **thăng cấp (promotion)** sang old generation.

## 6. Vì sao generational GC cần remembered set?

Nếu chỉ quét young generation, collector vẫn phải biết old object nào đang trỏ sang young object. Quét toàn old generation mỗi minor GC sẽ phá lợi ích.

Runtime vì vậy duy trì **tập ghi nhớ (remembered set)** hoặc card table. Khi application ghi một reference từ old sang young, **write barrier** cập nhật metadata để GC biết vùng nào cần kiểm tra.

Đây là một ví dụ rất quan trọng: GC nhanh không chỉ đến từ thuật toán collector; compiler/runtime chèn thêm code vào đường ghi của application để duy trì invariant phục vụ collector.

## 7. Write barrier và read barrier

**Rào ghi (write barrier)** là đoạn logic nhỏ chạy khi chương trình thay đổi reference. Nó có thể đánh dấu card bẩn, ghi nhớ edge hoặc hỗ trợ concurrent marking.

**Rào đọc (read barrier)** chạy khi đọc reference và có thể giúp xử lý object đang được di chuyển hoặc trạng thái marking.

Barrier làm đường thực thi application đắt hơn một chút để GC giảm pause hoặc làm việc concurrent. Đây là trade-off giữa mutator cost và collector cost.

## 8. Mutator là gì?

Trong tài liệu GC, **mutator** là thread của chương trình đang tạo và thay đổi object graph. Collector và mutator cùng thao tác lên heap nhưng với mục tiêu khác nhau.

Khi GC chạy concurrent, vấn đề cốt lõi là: collector đang cố suy luận graph trong khi mutator vẫn thay đổi graph đó. Nếu không có protocol, collector có thể bỏ sót object vừa trở nên reachable.

## 9. Concurrent marking và invariant

Collector concurrent cần một invariant bảo đảm rằng thay đổi của mutator không làm mất object sống. Hai họ kỹ thuật thường được nhắc đến là snapshot-at-the-beginning và incremental update.

Không cần học thuộc tên trước. Mental model quan trọng là collector cần đảm bảo một trong các điều sau:

```text
hoặc giữ lại ảnh logic của graph tại một thời điểm
hoặc ghi lại các edge mới có thể làm thay đổi reachability
```

Write barrier chính là công cụ để runtime duy trì invariant đó.

## 10. Tri-color abstraction

Một cách lý giải concurrent marking là **mô hình ba màu (tri-color abstraction)**:

- trắng: chưa được chứng minh reachable;
- xám: reachable nhưng children chưa quét xong;
- đen: reachable và children đã xử lý.

Một invariant phổ biến là tránh để object đen trỏ tới object trắng mà collector không biết. Barrier giúp duy trì invariant khi mutator đổi reference.

Mô hình màu là công cụ reasoning, không nhất thiết là cách heap thật lưu ba màu literal.

## 11. Allocation fast path

Trong generational GC, allocation trẻ có thể rất nhanh. Runtime giữ một con trỏ tới vị trí trống tiếp theo trong vùng liên tục:

```text
result = top
top += object_size
```

Nếu mỗi thread có **vùng cấp phát cục bộ (thread-local allocation buffer, TLAB)**, nhiều allocation không cần lock toàn cục.

Do đó “GC language allocation luôn chậm” là hiểu lầm. Allocation có thể rẻ; chi phí thật xuất hiện khi object sống lâu, heap pressure cao hoặc collection không theo kịp allocation rate.

## 12. Allocation rate và live set

Hai workload có cùng heap size nhưng behavior GC rất khác.

**Tốc độ cấp phát (allocation rate)** cho biết chương trình tạo bao nhiêu byte mỗi giây. **Tập object sống (live set)** là lượng memory thực sự còn reachable sau collection.

Nếu allocation rate cao nhưng phần lớn object chết trẻ, generational GC có thể xử lý tốt. Nếu live set gần heap limit, collector phải quét và di chuyển nhiều object mỗi chu kỳ, thời gian GC tăng mạnh.

## 13. Promotion failure và old-generation pressure

Nếu young collection muốn thăng cấp object nhưng old generation không đủ chỗ, runtime có thể phải trigger collection lớn hơn hoặc rơi vào allocation failure.

Hiện tượng này cho thấy young/old không độc lập. Tuning young generation quá lớn có thể tăng pause minor hoặc tạo burst promotion; quá nhỏ làm minor GC quá thường xuyên.

## 14. Fragmentation và pinning

Object **bị ghim (pinned)** không được di chuyển, thường vì native code hoặc I/O đang giữ địa chỉ ổn định. Quá nhiều pinned object có thể làm compacting collector khó nén heap hiệu quả và tăng fragmentation.

Đây là một connection quan trọng giữa runtime, FFI và OS I/O.

## 15. Reference counting khác tracing GC thế nào?

Reference counting giảm counter khi reference biến mất và thu hồi object khi counter về 0. Ưu điểm là reclamation thường sớm và phân tán theo thời gian. Nhược điểm là update reference phải sửa counter và cycle cần cơ chế bổ sung.

Tracing GC không cần counter trên mọi edge nhưng tạo collection phase riêng. Swift ARC và Objective-C ARC là ví dụ reference-counting-oriented runtime; JVM/.NET phổ biến tracing GC.

## 16. GC và concurrency application

GC pause có thể dừng nhiều thread cùng lúc. Concurrent collector giảm pause nhưng dùng CPU và memory bandwidth song song với application. Nếu host đã gần saturation, collector concurrent có thể cạnh tranh tài nguyên và làm throughput giảm.

Vì vậy GC tuning không thể tách khỏi capacity planning. Heap lớn hơn có thể giảm collection frequency nhưng làm collection lớn đắt hơn và tăng working set.

## 17. Memory leak trong managed runtime

Leak trong Java/JavaScript không nhất thiết là memory “không free được”; thường là object vẫn reachable ngoài ý muốn.

Ví dụ:

```text
global map
 -> listener
 -> session
 -> large object graph
```

Nếu listener không được unregister, toàn graph vẫn sống. Heap dump và dominator tree giúp tìm object nào đang giữ phần lớn retained memory.

## 18. Safepoint bias

Một runtime có thể cần đưa thread tới safepoint trước một số thao tác. Nếu thread chạy native code lâu, vòng lặp không có poll phù hợp hoặc bị blocked theo cách đặc biệt, thời gian đi tới safepoint có thể góp vào pause.

Do đó khi xem log GC, cần tách “thời gian collection” khỏi “thời gian chờ tất cả thread đạt trạng thái an toàn” nếu runtime cung cấp số liệu đó.

## 19. GC log và các câu hỏi cần đặt

Khi service có latency spike, nên hỏi:

```text
allocation rate bao nhiêu?
live set sau full collection là bao nhiêu?
pause p95/p99 thế nào?
promotion rate có tăng không?
old generation có liên tục gần đầy không?
GC dùng bao nhiêu CPU?
heap growth có tương ứng traffic không?
```

Nếu heap tăng vì cache hợp lệ, giải pháp khác với heap tăng vì reference leak.

## 20. Không có collector tốt nhất tuyệt đối

Một collector có pause cực thấp có thể dùng thêm CPU hoặc memory. Collector throughput-oriented có thể cho tổng công việc cao nhưng pause dài hơn. Embedded hoặc real-time system có requirement khác server backend.

Chọn collector là chọn mục tiêu tối ưu: throughput, tail latency, footprint, predictability hay khả năng scale heap lớn.

## Common Misconceptions

**“Có GC thì không cần hiểu memory.”** Sai. Developer vẫn cần hiểu allocation, object lifetime, leak, heap pressure và cache.

**“Heap càng lớn càng tốt.”** Heap quá lớn tăng working set và có thể tăng chi phí collection/recovery.

**“GC pause là toàn bộ thời gian GC.”** Concurrent collector có thể làm nhiều việc ngoài pause; ngược lại safepoint coordination cũng có thể góp vào pause.

**“Object không dùng nữa sẽ được thu hồi ngay.”** Chỉ khi nó không còn reachable và collector thực hiện reclamation phù hợp.

## Mô hình tư duy

> GC là protocol giữa **mutator**, **compiler/runtime metadata** và **collector** để duy trì câu trả lời đúng cho câu hỏi “object nào còn reachable?” trong khi chương trình vẫn liên tục thay đổi heap.

Hiểu GC ở mức Senior/Master không phải nhớ tên collector. Cần theo được đường đi từ allocation → object graph → barrier → marking → relocation → pause → CPU/cache/memory pressure → latency của application.

Xem tiếp: [JIT và deoptimization](./05_jit_profiling_speculative_optimization_and_deoptimization.md), [Virtual Memory](../../03_operating_systems/advanced/03_virtual_memory_page_tables_tlb_shootdown_and_huge_pages.md) và [Memory hierarchy](../../02_computer_architecture/advanced/README.md).
