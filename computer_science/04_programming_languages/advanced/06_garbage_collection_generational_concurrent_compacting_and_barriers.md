# Garbage collection: thế hệ, concurrent, compacting và ghi (write / 쓰기) barrier

> **Mạch đọc:** [README](./README.md) là bản đồ owner của **Garbage collection: thế hệ, concurrent, compacting và ghi (write / 쓰기) barrier**; nhìn vào vị trí đó trước để biết file này đang phục vụ nhánh kiến thức nào. **1. gốc (root / 루트) và đối tượng (object / 객체) đồ thị (graph / 그래프)** mở đối tượng chính của file và câu hỏi cần theo dõi; sau đó sang **2. Mark–sweep: mô hình cơ bản** để mở rộng đối tượng sang phạm vi kế cận. Cách đi này giữ lại điểm tựa của section đầu và cho biết kết luận sẽ được dùng ở đâu, thay vì dừng ở định nghĩa đầu tiên.

**Bộ gom rác (garbage collector, GC / 가비지 컬렉터)** là cơ chế thời gian chạy (runtime / 런타임) tự động tìm những đối tượng (object / 객체) không còn có thể được chương trình sử dụng và thu hồi vùng nhớ của chúng. Để hiểu GC sâu, trước hết phải tách ba khái niệm thường bị trộn lẫn: **cấp phát bộ nhớ (allocation)** là tạo vùng nhớ mới; **khả năng truy cập (reachability)** là đối tượng (object / 객체) còn được đi tới từ các gốc (root / 루트) hay không; **thu hồi (reclamation)** là trả vùng nhớ của đối tượng (object / 객체) không còn reachable về cho allocator.

GC không “biết đối tượng (object / 객체) nào còn hữu ích về mặt nghiệp vụ”. Nó chỉ suy luận từ đồ thị (graph / 그래프) tham chiếu mà thời gian chạy (runtime / 런타임) nhìn thấy. Nếu một bộ nhớ đệm (cache / 캐시) giữ tham chiếu (reference / 참조) tới đối tượng (object / 객체) không còn cần thiết, GC vẫn coi đối tượng (object / 객체) đó đang sống. Vì vậy bộ nhớ (memory / 메모리) leak vẫn có thể xảy ra trong ngôn ngữ có GC.

## 1. gốc (root / 루트) và đối tượng (object / 객체) đồ thị (graph / 그래프)

Thời gian chạy (runtime / 런타임) bắt đầu từ các **điểm gốc (GC roots)** như ngăn xếp (stack / 스택) frame đang hoạt động, biến tĩnh, register hoặc handle bản địa (native / 네이티브). Từ các gốc (root / 루트), collector duyệt đồ thị (graph / 그래프) đối tượng (object / 객체).

```text
GC roots
  |
  +--> A --> B
  |
  +--> C

D --> E   // không còn đường đi từ root
```

`D` và `E` có thể được thu hồi dù chúng vẫn trỏ lẫn nhau. Đây là khác biệt quan trọng so với tham chiếu (reference / 참조) counting thuần túy, vốn có thể gặp vấn đề cycle.

> **Chuyển mạch:** Trong **Garbage collection: thế hệ, concurrent, compacting và ghi (write / 쓰기) barrier**, **2. Mark–sweep: mô hình cơ bản** tiếp nhận điểm tựa từ **1. gốc (root / 루트) và đối tượng (object / 객체) đồ thị (graph / 그래프)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **3. Compacting collector** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 2. Mark–sweep: mô hình cơ bản

Một collector đơn giản có hai pha:

```text
mark  -> đánh dấu object reachable
sweep -> quét heap và thu hồi object chưa được đánh dấu
```

Mark–sweep dễ hiểu nhưng có thể để lại **phân mảnh (fragmentation)**: vùng trống nằm rải rác, khiến đối tượng (object / 객체) lớn khó tìm chỗ liên tục và locality kém.

> **Chuyển mạch:** Ở chặng này của **Garbage collection: thế hệ, concurrent, compacting và ghi (write / 쓰기) barrier**, **3. Compacting collector** tiếp nhận điểm tựa từ **2. Mark–sweep: mô hình cơ bản** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **4. Stop-the-world là gì?** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 3. Compacting collector

**Nén vùng nhớ động (heap / 힙) (compaction)** di chuyển đối tượng (object / 객체) sống về gần nhau rồi cập nhật tham chiếu (reference / 참조). Lợi ích là giảm fragmentation và cải thiện locality.

Nhưng di chuyển đối tượng (object / 객체) tạo chi phí. thời gian chạy (runtime / 런타임) phải biết mọi tham chiếu (reference / 참조) cần sửa; mã (code / 코드) bản địa (native / 네이티브) giữ raw pointer vào đối tượng (object / 객체) managed cũng trở thành vấn đề. Đây là lý do FFI, pinning và đối tượng (object / 객체) movement liên quan chặt với thiết kế GC.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Garbage collection: thế hệ, concurrent, compacting và ghi (write / 쓰기) barrier**, **4. Stop-the-world là gì?** tiếp nhận điểm tựa từ **3. Compacting collector** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **5. Generational hypothesis** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 4. Stop-the-world là gì?

Trong một số giai đoạn GC, thời gian chạy (runtime / 런타임) phải dừng các luồng thực thi (thread / 스레드) ứng dụng tại **điểm an toàn (safepoint)**. Khoảng dừng này gọi là **stop-the-world pause**.

Pause không đồng nghĩa toàn bộ công việc GC đều diễn ra khi ứng dụng dừng. Collector hiện đại có thể làm nhiều pha concurrent, nhưng vẫn thường cần một số synchronization điểm (point / 지점) để có snapshot nhất quán hoặc cập nhật siêu dữ liệu (metadata / 메타데이터).

Đối với dịch vụ latency-sensitive, p99/p999 pause quan trọng hơn thời gian GC trung bình.

> **Chuyển mạch:** Trong **Garbage collection: thế hệ, concurrent, compacting và ghi (write / 쓰기) barrier**, **5. Generational hypothesis** tiếp nhận điểm tựa từ **4. Stop-the-world là gì?** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **6. Vì sao generational GC cần remembered set?** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 5. Generational hypothesis

Nhiều tải công việc (workload / 워크로드) tạo rất nhiều đối tượng (object / 객체) sống ngắn. **Giả thuyết thế hệ (generational hypothesis)** nói rằng đối tượng (object / 객체) trẻ có xác suất chết sớm cao hơn đối tượng (object / 객체) đã sống qua nhiều chu kỳ.

Vùng nhớ vùng nhớ động (heap / 힙) vì vậy có thể chia thành thế hệ trẻ và già:

```text
young generation -> thu gom thường xuyên
old generation   -> thu gom ít hơn
```

Minor GC chỉ quét phần trẻ nên rẻ hơn full-heap collection. đối tượng (object / 객체) sống lâu có thể được **thăng cấp (promotion)** sang old generation.

> **Chuyển mạch:** Ở chặng này của **Garbage collection: thế hệ, concurrent, compacting và ghi (write / 쓰기) barrier**, **6. Vì sao generational GC cần remembered set?** tiếp nhận điểm tựa từ **5. Generational hypothesis** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **7. ghi (write / 쓰기) barrier và read barrier** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 6. Vì sao generational GC cần remembered set?

Nếu chỉ quét young generation, collector vẫn phải biết old đối tượng (object / 객체) nào đang trỏ sang young đối tượng (object / 객체). Quét toàn old generation mỗi minor GC sẽ phá lợi ích.

Thời gian chạy (runtime / 런타임) vì vậy duy trì **tập ghi nhớ (remembered set)** hoặc card bảng (table / 테이블). Khi ứng dụng (application / 애플리케이션) ghi một tham chiếu (reference / 참조) từ old sang young, **ghi (write / 쓰기) barrier** cập nhật siêu dữ liệu (metadata / 메타데이터) để GC biết vùng nào cần kiểm tra.

Đây là một ví dụ rất quan trọng: GC nhanh không chỉ đến từ thuật toán collector; trình biên dịch (compiler / 컴파일러)/thời gian chạy (runtime / 런타임) chèn thêm mã (code / 코드) vào đường ghi của ứng dụng (application / 애플리케이션) để duy trì bất biến (invariant / 불변식) phục vụ collector.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Garbage collection: thế hệ, concurrent, compacting và ghi (write / 쓰기) barrier**, **7. ghi (write / 쓰기) barrier và read barrier** tiếp nhận điểm tựa từ **6. Vì sao generational GC cần remembered set?** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **8. Mutator là gì?** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 7. ghi (write / 쓰기) barrier và read barrier

**Rào ghi (write barrier)** là đoạn lô-gic (logic / 논리) nhỏ chạy khi chương trình thay đổi tham chiếu (reference / 참조). Nó có thể đánh dấu card bẩn, ghi nhớ edge hoặc hỗ trợ concurrent marking.

**Rào đọc (read barrier)** chạy khi đọc tham chiếu (reference / 참조) và có thể giúp xử lý đối tượng (object / 객체) đang được di chuyển hoặc trạng thái marking.

Barrier làm đường thực thi ứng dụng (application / 애플리케이션) đắt hơn một chút để GC giảm pause hoặc làm việc concurrent. Đây là sự đánh đổi (trade-off / 트레이드오프) giữa mutator chi phí (cost / 비용) và collector chi phí (cost / 비용).

> **Chuyển mạch:** Trong **Garbage collection: thế hệ, concurrent, compacting và ghi (write / 쓰기) barrier**, **8. Mutator là gì?** tiếp nhận điểm tựa từ **7. ghi (write / 쓰기) barrier và read barrier** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **9. Concurrent marking và bất biến (invariant / 불변식)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 8. Mutator là gì?

Trong tài liệu GC, **mutator** là luồng thực thi (thread / 스레드) của chương trình đang tạo và thay đổi đối tượng (object / 객체) đồ thị (graph / 그래프). Collector và mutator cùng thao tác lên vùng nhớ động (heap / 힙) nhưng với mục tiêu khác nhau.

Khi GC chạy concurrent, vấn đề cốt lõi là: collector đang cố suy luận đồ thị (graph / 그래프) trong khi mutator vẫn thay đổi đồ thị (graph / 그래프) đó. Nếu không có giao thức (protocol / 프로토콜), collector có thể bỏ sót đối tượng (object / 객체) vừa trở nên reachable.

> **Chuyển mạch:** Ở chặng này của **Garbage collection: thế hệ, concurrent, compacting và ghi (write / 쓰기) barrier**, **9. Concurrent marking và bất biến (invariant / 불변식)** tiếp nhận điểm tựa từ **8. Mutator là gì?** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **10. Tri-color lớp trừu tượng (abstraction / 추상화)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 9. Concurrent marking và bất biến (invariant / 불변식)

Collector concurrent cần một bất biến (invariant / 불변식) bảo đảm rằng thay đổi của mutator không làm mất đối tượng (object / 객체) sống. Hai họ kỹ thuật thường được nhắc đến là snapshot-at-the-beginning và incremental cập nhật (update / 업데이트).

Không cần học thuộc tên trước. mô hình tư duy (mental model / 사고 모델) quan trọng là collector cần đảm bảo một trong các điều sau:

```text
hoặc giữ lại ảnh logic của graph tại một thời điểm
hoặc ghi lại các edge mới có thể làm thay đổi reachability
```

Ghi (write / 쓰기) barrier chính là công cụ để thời gian chạy (runtime / 런타임) duy trì bất biến (invariant / 불변식) đó.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Garbage collection: thế hệ, concurrent, compacting và ghi (write / 쓰기) barrier**, **10. Tri-color lớp trừu tượng (abstraction / 추상화)** tiếp nhận điểm tựa từ **9. Concurrent marking và bất biến (invariant / 불변식)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **11. Allocation fast đường dẫn (path / 경로)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 10. Tri-color lớp trừu tượng (abstraction / 추상화)

Một cách lý giải concurrent marking là **mô hình ba màu (tri-color abstraction)**:

- trắng: chưa được chứng minh reachable;
- xám: reachable nhưng children chưa quét xong;
- đen: reachable và children đã xử lý.

Một bất biến (invariant / 불변식) phổ biến là tránh để đối tượng (object / 객체) đen trỏ tới đối tượng (object / 객체) trắng mà collector không biết. Barrier giúp duy trì bất biến (invariant / 불변식) khi mutator đổi tham chiếu (reference / 참조).

Mô hình màu là công cụ lập luận (reasoning / 추론), không nhất thiết là cách vùng nhớ động (heap / 힙) thật lưu ba màu literal.

> **Chuyển mạch:** Trong **Garbage collection: thế hệ, concurrent, compacting và ghi (write / 쓰기) barrier**, **10. Tri-color lớp trừu tượng (abstraction / 추상화)** xác định đầu vào; **11. Allocation fast đường dẫn (path / 경로)** giải thích bước vận hành tạo ra kết quả kế tiếp. Từ đây, **12. Allocation tỷ lệ (rate / 비율) và live set** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 11. Allocation fast đường dẫn (path / 경로)

Trong generational GC, allocation trẻ có thể rất nhanh. thời gian chạy (runtime / 런타임) giữ một con trỏ tới vị trí trống tiếp theo trong vùng liên tục:

```text
result = top
top += object_size
```

Nếu mỗi luồng thực thi (thread / 스레드) có **vùng cấp phát cục bộ (thread-local allocation buffer, TLAB)**, nhiều allocation không cần khóa (lock / 잠금) toàn cục.

Do đó “GC ngôn ngữ (language / 언어) allocation luôn chậm” là hiểu lầm. Allocation có thể rẻ; chi phí thật xuất hiện khi đối tượng (object / 객체) sống lâu, vùng nhớ động (heap / 힙) pressure cao hoặc collection không theo kịp allocation tỷ lệ (rate / 비율).

> **Chuyển mạch:** Ở chặng này của **Garbage collection: thế hệ, concurrent, compacting và ghi (write / 쓰기) barrier**, **11. Allocation fast đường dẫn (path / 경로)** xác định đầu vào; **12. Allocation tỷ lệ (rate / 비율) và live set** giải thích bước vận hành tạo ra kết quả kế tiếp. Từ đây, **13. Promotion thất bại (failure / 실패) và old-generation pressure** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 12. Allocation tỷ lệ (rate / 비율) và live set

Hai tải công việc (workload / 워크로드) có cùng vùng nhớ động (heap / 힙) kích thước (size / 크기) nhưng hành vi (behavior / 동작) GC rất khác.

**Tốc độ cấp phát (allocation rate)** cho biết chương trình tạo bao nhiêu byte mỗi giây. **Tập đối tượng (object / 객체) sống (live set)** là lượng bộ nhớ (memory / 메모리) thực sự còn reachable sau collection.

Nếu allocation tỷ lệ (rate / 비율) cao nhưng phần lớn đối tượng (object / 객체) chết trẻ, generational GC có thể xử lý tốt. Nếu live set gần vùng nhớ động (heap / 힙) limit, collector phải quét và di chuyển nhiều đối tượng (object / 객체) mỗi chu kỳ, thời gian GC tăng mạnh.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Garbage collection: thế hệ, concurrent, compacting và ghi (write / 쓰기) barrier**, **13. Promotion thất bại (failure / 실패) và old-generation pressure** tiếp nhận điểm tựa từ **12. Allocation tỷ lệ (rate / 비율) và live set** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **14. Fragmentation và pinning** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 13. Promotion thất bại (failure / 실패) và old-generation pressure

Nếu young collection muốn thăng cấp đối tượng (object / 객체) nhưng old generation không đủ chỗ, thời gian chạy (runtime / 런타임) có thể phải trigger collection lớn hơn hoặc rơi vào allocation thất bại (failure / 실패).

Hiện tượng này cho thấy young/old không độc lập. Tuning young generation quá lớn có thể tăng pause minor hoặc tạo burst promotion; quá nhỏ làm minor GC quá thường xuyên.

> **Chuyển mạch:** Trong **Garbage collection: thế hệ, concurrent, compacting và ghi (write / 쓰기) barrier**, **14. Fragmentation và pinning** tiếp nhận điểm tựa từ **13. Promotion thất bại (failure / 실패) và old-generation pressure** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **15. tham chiếu (reference / 참조) counting khác tracing GC thế nào?** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 14. Fragmentation và pinning

Đối tượng (object / 객체) **bị ghim (pinned)** không được di chuyển, thường vì bản địa (native / 네이티브) mã (code / 코드) hoặc I/O đang giữ địa chỉ ổn định. Quá nhiều pinned đối tượng (object / 객체) có thể làm compacting collector khó nén vùng nhớ động (heap / 힙) hiệu quả và tăng fragmentation.

Đây là một liên kết (connection / 연결) quan trọng giữa thời gian chạy (runtime / 런타임), FFI và OS I/O.

> **Chuyển mạch:** Ở chặng này của **Garbage collection: thế hệ, concurrent, compacting và ghi (write / 쓰기) barrier**, sau nội dung của **14. Fragmentation và pinning**, **15. tham chiếu (reference / 참조) counting khác tracing GC thế nào?** chỉ rõ tài liệu chuẩn và vị trí sở hữu để người học biết phần nào cần quay lại khi muốn đào sâu. Từ đây, **16. GC và tính đồng thời (concurrency / 동시성) ứng dụng (application / 애플리케이션)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 15. tham chiếu (reference / 참조) counting khác tracing GC thế nào?

Tham chiếu (reference / 참조) counting giảm counter khi tham chiếu (reference / 참조) biến mất và thu hồi đối tượng (object / 객체) khi counter về 0. Ưu điểm là reclamation thường sớm và phân tán theo thời gian. Nhược điểm là cập nhật (update / 업데이트) tham chiếu (reference / 참조) phải sửa counter và cycle cần cơ chế bổ sung.

Tracing GC không cần counter trên mọi edge nhưng tạo collection phase riêng. Swift ARC và Objective-C ARC là ví dụ reference-counting-oriented thời gian chạy (runtime / 런타임); JVM/.NET phổ biến tracing GC.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Garbage collection: thế hệ, concurrent, compacting và ghi (write / 쓰기) barrier**, **16. GC và tính đồng thời (concurrency / 동시성) ứng dụng (application / 애플리케이션)** tiếp nhận điểm tựa từ **15. tham chiếu (reference / 참조) counting khác tracing GC thế nào?** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **17. bộ nhớ (memory / 메모리) leak trong managed thời gian chạy (runtime / 런타임)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 16. GC và tính đồng thời (concurrency / 동시성) ứng dụng (application / 애플리케이션)

GC pause có thể dừng nhiều luồng thực thi (thread / 스레드) cùng lúc. Concurrent collector giảm pause nhưng dùng CPU và bộ nhớ (memory / 메모리) bandwidth song song với ứng dụng (application / 애플리케이션). Nếu host đã gần saturation, collector concurrent có thể cạnh tranh tài nguyên và làm thông lượng (throughput / 처리량) giảm.

Vì vậy GC tuning không thể tách khỏi sức chứa (capacity / 용량) planning. vùng nhớ động (heap / 힙) lớn hơn có thể giảm collection frequency nhưng làm collection lớn đắt hơn và tăng working set.

> **Chuyển mạch:** Trong **Garbage collection: thế hệ, concurrent, compacting và ghi (write / 쓰기) barrier**, **17. bộ nhớ (memory / 메모리) leak trong managed thời gian chạy (runtime / 런타임)** tiếp nhận điểm tựa từ **16. GC và tính đồng thời (concurrency / 동시성) ứng dụng (application / 애플리케이션)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **18. Safepoint độ lệch (bias / 편향)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 17. bộ nhớ (memory / 메모리) leak trong managed thời gian chạy (runtime / 런타임)

Leak trong Java/JavaScript không nhất thiết là bộ nhớ (memory / 메모리) “không free được”; thường là đối tượng (object / 객체) vẫn reachable ngoài ý muốn.

Ví dụ:

```text
global map
 -> listener
 -> session
 -> large object graph
```

Nếu listener không được unregister, toàn đồ thị (graph / 그래프) vẫn sống. vùng nhớ động (heap / 힙) dump và dominator cây (tree / 트리) giúp tìm đối tượng (object / 객체) nào đang giữ phần lớn retained bộ nhớ (memory / 메모리).

> **Chuyển mạch:** Ở chặng này của **Garbage collection: thế hệ, concurrent, compacting và ghi (write / 쓰기) barrier**, **18. Safepoint độ lệch (bias / 편향)** tiếp nhận điểm tựa từ **17. bộ nhớ (memory / 메모리) leak trong managed thời gian chạy (runtime / 런타임)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **19. GC log và các câu hỏi cần đặt** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 18. Safepoint độ lệch (bias / 편향)

Một thời gian chạy (runtime / 런타임) có thể cần đưa luồng thực thi (thread / 스레드) tới safepoint trước một số thao tác. Nếu luồng thực thi (thread / 스레드) chạy bản địa (native / 네이티브) mã (code / 코드) lâu, vòng lặp không có poll phù hợp hoặc bị blocked theo cách đặc biệt, thời gian đi tới safepoint có thể góp vào pause.

Do đó khi xem log GC, cần tách “thời gian collection” khỏi “thời gian chờ tất cả luồng thực thi (thread / 스레드) đạt trạng thái an toàn” nếu thời gian chạy (runtime / 런타임) cung cấp số liệu đó.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Garbage collection: thế hệ, concurrent, compacting và ghi (write / 쓰기) barrier**, **19. GC log và các câu hỏi cần đặt** tiếp nhận điểm tựa từ **18. Safepoint độ lệch (bias / 편향)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **20. Không có collector tốt nhất tuyệt đối** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 19. GC log và các câu hỏi cần đặt

Khi dịch vụ (service / 서비스) có độ trễ (latency / 지연 시간) spike, nên hỏi:

```text
allocation rate bao nhiêu?
live set sau full collection là bao nhiêu?
pause p95/p99 thế nào?
promotion rate có tăng không?
old generation có liên tục gần đầy không?
GC dùng bao nhiêu CPU?
heap growth có tương ứng traffic không?
```

Nếu vùng nhớ động (heap / 힙) tăng vì bộ nhớ đệm (cache / 캐시) hợp lệ, giải pháp khác với vùng nhớ động (heap / 힙) tăng vì tham chiếu (reference / 참조) leak.

> **Chuyển mạch:** Trong **Garbage collection: thế hệ, concurrent, compacting và ghi (write / 쓰기) barrier**, **20. Không có collector tốt nhất tuyệt đối** tiếp nhận điểm tựa từ **19. GC log và các câu hỏi cần đặt** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Dùng chung (common / 공통) Misconceptions** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 20. Không có collector tốt nhất tuyệt đối

Một collector có pause cực thấp có thể dùng thêm CPU hoặc bộ nhớ (memory / 메모리). Collector throughput-oriented có thể cho tổng công việc cao nhưng pause dài hơn. Embedded hoặc real-time hệ thống (system / 시스템) có yêu cầu (requirement / 요구사항) khác máy chủ (server / 서버) backend.

Chọn collector là chọn mục tiêu tối ưu: thông lượng (throughput / 처리량), tail độ trễ (latency / 지연 시간), footprint, predictability hay khả năng quy mô (scale / 규모) vùng nhớ động (heap / 힙) lớn.

> **Chuyển mạch:** Ở chặng này của **Garbage collection: thế hệ, concurrent, compacting và ghi (write / 쓰기) barrier**, **Dùng chung (common / 공통) Misconceptions** tiếp nhận điểm tựa từ **20. Không có collector tốt nhất tuyệt đối** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Mô hình tư duy** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Dùng chung (common / 공통) Misconceptions

**“Có GC thì không cần hiểu bộ nhớ (memory / 메모리).”** Sai. nhà phát triển (developer / 개발자) vẫn cần hiểu allocation, đối tượng (object / 객체) thời gian tồn tại (lifetime / 수명), leak, vùng nhớ động (heap / 힙) pressure và bộ nhớ đệm (cache / 캐시).

**“vùng nhớ động (heap / 힙) càng lớn càng tốt.”** vùng nhớ động (heap / 힙) quá lớn tăng working set và có thể tăng chi phí collection/khôi phục (recovery / 복구).

**“GC pause là toàn bộ thời gian GC.”** Concurrent collector có thể làm nhiều việc ngoài pause; ngược lại safepoint coordination cũng có thể góp vào pause.

**“đối tượng (object / 객체) không dùng nữa sẽ được thu hồi ngay.”** Chỉ khi nó không còn reachable và collector thực hiện reclamation phù hợp.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Garbage collection: thế hệ, concurrent, compacting và ghi (write / 쓰기) barrier**, **Mô hình tư duy** gom các mảnh từ **Dùng chung (common / 공통) Misconceptions** thành một kết luận có thể mang sang phần kế tiếp. Phần còn lại của file dùng kết quả này để khép lại mạch giải thích.

## Mô hình tư duy

> GC là giao thức (protocol / 프로토콜) giữa **mutator**, **trình biên dịch (compiler / 컴파일러)/thời gian chạy (runtime / 런타임) siêu dữ liệu (metadata / 메타데이터)** và **collector** để duy trì câu trả lời đúng cho câu hỏi “đối tượng (object / 객체) nào còn reachable?” trong khi chương trình vẫn liên tục thay đổi vùng nhớ động (heap / 힙).

Hiểu GC ở mức cấp cao (senior / 시니어)/Master không phải nhớ tên collector. Cần theo được đường đi từ allocation → đối tượng (object / 객체) đồ thị (graph / 그래프) → barrier → marking → relocation → pause → CPU/bộ nhớ đệm (cache / 캐시)/bộ nhớ (memory / 메모리) pressure → độ trễ (latency / 지연 시간) của ứng dụng (application / 애플리케이션).

Xem tiếp: [JIT và deoptimization](./05_jit_profiling_speculative_optimization_and_deoptimization.md), [Virtual Memory](../../03_operating_systems/advanced/03_virtual_memory_page_tables_tlb_shootdown_and_huge_pages.md) và [Memory hierarchy](../../02_computer_architecture/advanced/README.md).

> **Bàn giao:** Sau **Mô hình tư duy**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](./README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
