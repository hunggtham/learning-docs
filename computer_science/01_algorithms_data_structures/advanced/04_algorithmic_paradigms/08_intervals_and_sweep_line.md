# Interval Algorithms và Sweep Line
**Interval Algorithms & Sweep Line / 구간 알고리즘과 스위프 라인**

Intervals xuất hiện ở rất nhiều domain: lịch họp, thời gian chạy CPU, validity period của dữ liệu, price range, genomic region, segment trên trục số, rectangle trên màn hình, network reservation hoặc log window. Điểm chung là mỗi object không còn là một điểm đơn lẻ mà chiếm một đoạn `[start,end]` hay `[start,end)` trên một trục có thứ tự.

Khi có nhiều intervals, cách brute-force so từng cặp rất dễ thành `O(n^2)`. Phần lớn interval algorithms nhanh hơn nhờ một ý tưởng cốt lõi: **sort events theo một trục rồi duy trì một state đại diện cho những object đang active**.

## 1. Trước tiên phải xác định interval semantics

Hai kiểu rất phổ biến là closed interval `[l,r]` và half-open interval `[l,r)`.

Với `[l,r]`, hai intervals `[1,3]` và `[3,5]` overlap tại điểm 3. Với `[1,3)` và `[3,5)`, chúng không overlap vì interval đầu kết thúc ngay trước 3.

Trong software systems, half-open interval thường rất tiện. Array slice, time window và memory range thường dùng `[start,end)` vì length đơn giản là `end - start`, và hai đoạn liên tiếp `[0,5)` và `[5,10)` ghép lại không duplicate boundary.

Comparator và tie-breaking phụ thuộc trực tiếp vào semantics này. Nếu domain chưa rõ closed hay half-open, thuật toán chưa thể coi là hoàn chỉnh.

## 2. Merge Intervals

Bài toán: hợp nhất các intervals overlap thành các đoạn rời nhau.

Bước quan trọng là sort theo `start`, thường tie-break theo `end`. Sau đó scan từ trái sang phải và giữ một merged interval hiện tại.

Nếu interval tiếp theo bắt đầu trước hoặc tại end hiện tại theo overlap semantics, ta mở rộng end:

```text
current.end = max(current.end, next.end)
```

Nếu không overlap, current interval đã hoàn tất và có thể output.

Sau sorting `O(n log n)`, scan chỉ `O(n)`.

### Vì sao chỉ cần so với interval cuối đã merge?

Sorting tạo invariant: mọi interval tương lai có `start` không nhỏ hơn interval hiện tại. Nếu `next` không overlap merged interval cuối, nó cũng không thể overlap một merged interval cũ nằm còn xa hơn về trái theo cách cần quay lại sửa.

Đây là một pattern quan trọng: sorting chuyển một quan hệ pairwise toàn cục thành local comparison.

## 3. Insert Interval

Nếu ta đã có danh sách intervals không overlap và sorted, chèn một interval mới không nhất thiết cần merge-sort lại toàn bộ.

Ta có thể đi qua ba vùng: intervals hoàn toàn trước new interval, các intervals overlap cần merge, rồi intervals hoàn toàn sau nó. Total `O(n)`.

Nếu insert xảy ra thường xuyên và `n` lớn, flat sorted array có thể không còn hợp lý; balanced tree hoặc interval tree có thể phù hợp hơn. Đây là ví dụ cho việc cùng bài toán logical nhưng workload mutation khác dẫn tới data structure khác.

## 4. Interval Scheduling: chọn nhiều interval không overlap nhất

Một bài rất nổi tiếng là chọn maximum number of mutually non-overlapping intervals.

Greedy rule đúng là chọn interval có **finish time sớm nhất** trước. Sau đó bỏ các interval conflict và lặp lại.

Tại sao không chọn interval bắt đầu sớm nhất hoặc ngắn nhất? Vì finish-time earliest để lại phần timeline phía sau nhiều nhất.

Proof điển hình dùng exchange argument: trong một optimal solution, nếu first interval không phải interval kết thúc sớm nhất `g`, ta có thể thay first interval đó bằng `g`. Vì `g` kết thúc không muộn hơn, các interval sau vẫn có thể giữ nguyên. Do đó tồn tại optimal solution bắt đầu bằng greedy choice.

Đây là một ví dụ quan trọng nơi sorting by end chứ không phải by start tạo invariant phù hợp với objective.

## 5. Meeting Rooms và maximum overlap

Nếu mục tiêu là tìm số phòng tối thiểu để chứa mọi meeting, ta cần số intervals active lớn nhất tại cùng thời điểm.

Một cách là biến mỗi interval thành hai events:

```text
(start, +1)
(end, -1)
```

Sort events theo time rồi cộng running count. Maximum count là maximum concurrent intervals.

Với half-open meetings `[start,end)`, nếu một meeting kết thúc đúng lúc meeting khác bắt đầu, room có thể reuse. Vì vậy tại cùng timestamp, `end` event phải được xử lý trước `start` event.

Với closed intervals mà boundary được xem là overlap, tie rule ngược lại.

Đây là ví dụ điển hình cho nguyên tắc:

> domain semantics quyết định event ordering.

## 6. Sweep Line là gì?

**Sweep Line / 스위프 라인** tưởng tượng một đường quét di chuyển theo một coordinate, thường từ trái sang phải hoặc từ thời gian nhỏ đến lớn.

Thay vì xét mọi cặp object, ta xử lý các **events** theo order. Một **active set** lưu những object đang có khả năng tương tác với sweep position hiện tại.

Khi gặp start event, object được thêm vào active state. Khi gặp end event, object rời active state. Query hoặc update chỉ diễn ra với active objects thay vì toàn bộ objects.

Đây là cách biến static geometric/global problem thành incremental online-like process theo một trục đã sort.

## 7. Active set cần cấu trúc gì?

Nếu chỉ cần đếm số object active, một integer counter đủ.

Nếu cần biết end nhỏ nhất, heap có thể hữu ích. Nếu cần predecessor/successor theo y-coordinate trong computational geometry, balanced BST/order-statistics structure thường xuất hiện. Nếu cần range aggregate trên compressed coordinates, Fenwick Tree hoặc Segment Tree có thể tham gia.

Sweep line không phải một data structure; nó là algorithmic framework. Active-set requirements mới quyết định data structure bên trong.

## 8. Rectangle overlap

Với axis-aligned rectangles, mỗi rectangle có x-interval và y-interval. Ta có thể sweep theo x.

Khi gặp left edge của rectangle, thêm y-interval của nó vào active structure. Khi gặp right edge, remove. Muốn biết rectangle mới có overlap rectangle active nào không, active structure cần query overlap trên y-axis.

Nếu chỉ cần detect overlap, structure có thể đơn giản hơn. Nếu cần count overlap hoặc union area, ta thường cần segment tree hoặc compressed coordinate structure phức tạp hơn.

## 9. Rectangle Union Area

Bài union area của nhiều rectangles minh họa sweep line rất rõ.

Ta tạo events tại mỗi vertical edge `x`, mỗi event mang y-range và delta `+1/-1`. Giữa hai x-events liên tiếp, tập rectangles active không đổi. Nếu active y-union length là `L`, contribution area là:

\[
L \cdot (x_{next}-x_{current})
\]

Khó khăn chuyển thành duy trì total covered length trên y-axis khi add/remove intervals. Segment Tree với coordinate compression có thể lưu cover count và covered length.

Ta không còn tính area bằng cách pairwise subtract overlaps; thay vào đó tích phân discrete theo sweep strips.

## 10. Coordinate Compression

Coordinates trong bài geometry hoặc time có thể rất lớn, ví dụ tới `10^9`, nhưng chỉ vài trăm nghìn endpoints thật sự xuất hiện. Không thể tạo array size `10^9` chỉ để đánh dấu.

Ta lấy tất cả relevant coordinates, sort unique và map mỗi coordinate sang rank nhỏ:

```text
original:  100, 5000000, 900000000
compressed: 0,   1,       2
```

**Coordinate compression / 좌표 압축** giữ order nhưng không tự giữ khoảng cách.

Nếu bài chỉ cần order/rank, compressed index đủ. Nếu cần length/area, phải lưu original values vì khoảng giữa compressed index 0 và 1 không nhất thiết bằng khoảng giữa 1 và 2.

Đây là lỗi rất thường gặp khi dùng Segment Tree cho geometry.

## 11. Difference Array là sweep line rời rạc

Nếu coordinate domain nhỏ và integer, interval add có thể dùng difference array.

Muốn add `+1` cho `[l,r]` inclusive:

```text
diff[l] += 1
diff[r + 1] -= 1
```

Prefix sum của `diff` cho số intervals active tại mỗi coordinate.

Về mặt mental model, đây chính là event sweep: start event `+1`, end-after event `-1`, nhưng events được lưu trong array thay vì sorted list.

## 12. Two sorted endpoint arrays

Một biến thể Meeting Rooms có thể tách toàn bộ starts và ends thành hai arrays sorted. Dùng hai pointers: nếu next start < next end, cần thêm room; ngược lại một meeting đã kết thúc và room được giải phóng.

Cách này là sweep line nhưng state chỉ là count và events được split thành hai streams.

Nó cho thấy cùng conceptual algorithm có nhiều representation khác nhau.

## 13. Intersections of two sorted interval lists

Nếu hai danh sách intervals đều sorted và non-overlapping nội bộ, ta có thể tìm intersections bằng two pointers.

Với `A=[a1,a2]`, `B=[b1,b2]`, overlap nếu:

\[
\max(a1,b1) \le \min(a2,b2)
\]

sau đó advance interval kết thúc sớm hơn, vì interval đó không thể overlap thêm một interval tương lai của phía kia theo cách chưa xét.

Total `O(n+m)` thay vì pairwise `O(nm)`.

Again, sorted invariant loại bỏ search space.

## 14. Line segment intersection phức tạp hơn interval overlap

Trên một chiều, ordering cố định. Với line segments trong 2D, sweep line active set thường được order theo y-position tại current x. Khi sweep x thay đổi, relative ordering có thể đổi tại intersections.

Algorithms như Bentley–Ottmann quản lý event queue và balanced tree để tìm intersections hiệu quả hơn brute-force pairwise.

Điểm cần nắm là active-set comparator có thể phụ thuộc sweep position, làm correctness và implementation phức tạp hơn nhiều so với time intervals.

## 15. Interval Tree

Nếu intervals được insert/delete động và cần query “có interval nào overlap query `[L,R]` không?”, sorting một lần không đủ.

Interval Tree thường là augmented balanced BST keyed by start, mỗi node lưu `maxEnd` của subtree. Nếu left subtree có `maxEnd < L`, không interval nào bên trái có thể overlap query và subtree đó được prune.

Đây là connection giữa interval algorithms và augmented trees: summary metadata cho phép loại cả subtree.

## 16. Range structures không đồng nghĩa interval structures

Segment Tree cũng làm việc với intervals, nhưng model khác Interval Tree.

Segment Tree thường partition một coordinate/index domain và lưu aggregate cho ranges. Interval Tree lưu một dynamic set của interval objects và hỗ trợ overlap queries.

Tên đều có “interval/range” nhưng workload khác. Chọn nhầm structure vì tên giống nhau là lỗi phổ biến.

## 17. Sweep line và offline processing

Sweep line thường là một dạng **offline algorithm**: ta biết toàn bộ events trước, sort chúng, rồi xử lý theo order thuận lợi.

Nếu events đến real-time và phải trả lời ngay, không thể tự do reorder tương lai. Khi đó cần online data structure khác hoặc maintain ordered state động.

Offline freedom là một tài nguyên algorithmic. Nếu bài không bắt buộc giữ input order, sorting thường mở ra nhiều optimization.

## 18. Tie-breaking phải trở thành một phần của comparator specification

Một comparator “sort theo time” là chưa đủ nếu multiple events có cùng time.

Ví dụ với `[start,end)` và counting overlap, end-before-start. Với closed intervals, start-before-end có thể đúng nếu boundary overlap. Với rectangle union, add/remove at same x thường được group rồi apply theo một order hoặc batch semantics sao cho width giữa equal x là zero.

Nên viết explicit tie rule và lý do của nó trước khi code comparator.

## 19. Integer overflow và coordinate arithmetic

Area có thể vượt 32-bit rất nhanh. Nếu x/y tới `10^9`, product width × coveredLength có thể tới `10^18`. Java cần `long`, C cần integer width phù hợp, JavaScript cần kiểm tra safe-integer range hoặc dùng `BigInt` tùy requirement.

Comparator kiểu `a.start - b.start` cũng có thể overflow trong Java/C-like settings nếu giá trị cực lớn; so sánh trực tiếp an toàn hơn.

## 20. Một workflow nhận diện sweep-line problem

Khi thấy nhiều objects sống trên time/coordinate intervals và brute force đang so từng cặp, hãy hỏi liệu interactions có chỉ thay đổi tại một số **event points** hay không.

Nếu giữa hai event points state không đổi, ta có thể sort events rồi process incremental. Sau đó hỏi active state cần operation gì: count, min end, ordered neighbor, overlap query hay range aggregate. Câu trả lời quyết định counter, heap, balanced tree hay segment tree.

Đây là cách suy ra algorithm từ workload thay vì học thuộc pattern.

## 21. Ví dụ production: booking service

Một booking system có thể dùng half-open interval `[checkIn, checkOut)` để room được tái sử dụng đúng tại thời điểm checkout. Nếu chỉ cần validate một batch booking offline, sort + sweep có thể đủ.

Nếu service nhận booking online liên tục, mỗi room/resource có thể cần ordered interval index để query predecessor/successor quanh requested time. Nếu cần thống kê concurrency theo ngày trên batch lớn, event aggregation hoặc difference structure lại phù hợp hơn.

Cùng domain booking nhưng ba workload khác nhau dẫn tới ba representations khác nhau.

## Mental Model

> Interval/sweep-line algorithms biến bài toán “mọi object có thể tương tác với mọi object” thành bài toán “state chỉ thay đổi tại **events có thứ tự**”.

Sorting tạo timeline/coordinate order; active set giữ đúng phần dữ liệu còn liên quan; tie-breaking encode domain semantics. Từ đó quadratic pairwise reasoning thường được nén thành `O(n log n)` hoặc thậm chí `O(n)` sau preprocessing.

Xem thêm: [Two Pointers, Sliding Window, Prefix & Difference](./07_two_pointers_sliding_window_prefix_difference.md), [Range Queries](../05_specialized/01_range_queries_fenwick_segment_tree.md), [Augmented Trees](../02_trees/06_augmented_trees_and_order_statistics.md).