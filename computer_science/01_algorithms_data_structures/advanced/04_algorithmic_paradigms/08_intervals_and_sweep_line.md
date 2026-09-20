# Thuật toán khoảng và đường quét
**Intervals & Sweep Line / 구간 알고리즘과 스위프 라인**

Khoảng xuất hiện ở rất nhiều miền: lịch họp, thời gian hiệu lực của dữ liệu, vùng nhớ, cửa sổ log, đoạn giá, genomic region, đoạn thẳng trên trục số và hình chữ nhật trong hình học tính toán. Điểm chung là một đối tượng không còn là một điểm mà chiếm một **miền liên tục có thứ tự**.

Nếu xử lý mọi cặp khoảng độc lập, chi phí rất dễ trở thành `O(n²)`. Phần lớn thuật toán nhanh hơn dựa trên một ý tưởng nền tảng:

> **Sắp xếp các sự kiện theo một trục rồi duy trì đúng trạng thái của các đối tượng còn “đang hoạt động” tại vị trí quét hiện tại.**

Đây là bản chất của **đường quét (sweep line / 스위프 라인)**. Sorting không chỉ làm dữ liệu đẹp hơn; nó biến tương tác toàn cục thành một chuỗi thay đổi cục bộ có thứ tự.

## 1. Ngữ nghĩa khoảng phải được chốt trước thuật toán

Hai cách biểu diễn phổ biến là khoảng đóng `[l,r]` và khoảng nửa mở `[l,r)`.

Với `[l,r]`, `[1,3]` và `[3,5]` giao nhau tại 3. Với `[1,3)` và `[3,5)`, chúng không giao nhau.

Khoảng nửa mở thường thuận tiện trong phần mềm vì:

```text
độ dài = r - l
[a,b) + [b,c) ghép liên tiếp nhưng không trùng điểm b
slice, buffer, memory range thường dùng quy ước này
```

Quy tắc xử lý sự kiện trùng tọa độ phụ thuộc trực tiếp vào ngữ nghĩa đó. Với `[start,end)`, sự kiện kết thúc tại `t` phải được xử lý trước sự kiện bắt đầu tại `t` nếu hai khoảng không được xem là chồng lấn.

Nếu quy ước biên chưa rõ, thuật toán chưa hoàn chỉnh.

## 2. Chuẩn hóa dữ liệu trước khi suy luận

Trong hệ thống thật, khoảng đầu vào có thể có `l > r`, timestamp không cùng múi giờ, giá trị thiếu hoặc nhiều quy ước endpoint khác nhau. Trước khi chạy thuật toán nên xác định:

```text
có cho phép khoảng rỗng không?
[l,l) có ý nghĩa gì?
đầu mút có inclusive/exclusive riêng biệt không?
có cần đổi timezone/đơn vị không?
đầu vào có thể chứa NaN hoặc sentinel không?
```

Bước chuẩn hóa là một phần của tính đúng đắn. Một sweep line đúng toán học nhưng dùng timestamp không cùng hệ quy chiếu vẫn cho kết quả sai nghiệp vụ.

## 3. Merge Intervals

Sau khi sắp xếp theo điểm bắt đầu, ta duy trì đoạn hợp nhất cuối cùng.

```text
nếu next.start còn nằm trong current:
    current.end = max(current.end, next.end)
ngược lại:
    xuất current
    current = next
```

Độ phức tạp bị chi phối bởi sorting:

\[
O(n\log n)
\]

và quét `O(n)`.

### Vì sao chỉ cần so với đoạn hợp nhất cuối?

Sau sorting, mọi đoạn tương lai bắt đầu không sớm hơn đoạn hiện tại. Nếu `next` đã nằm hoàn toàn bên phải đoạn hợp nhất cuối, nó càng không thể quay lại giao một đoạn hợp nhất cũ hơn.

Sorting tạo ra một **bất biến đơn điệu (monotonic invariant)** giúp loại nhu cầu so mọi cặp.

## 4. Insert Interval

Nếu tập khoảng đã được đảm bảo có thứ tự và không chồng lấn, chèn một khoảng mới có ba pha:

```text
các khoảng hoàn toàn nằm trước
các khoảng giao nhau cần hợp nhất
các khoảng hoàn toàn nằm sau
```

Một lần chèn là `O(n)` với mảng phẳng. Nếu cập nhật diễn ra thường xuyên, lựa chọn cấu trúc phải thay đổi: cây cân bằng, interval tree hoặc cấu trúc chuyên biệt có thể phù hợp hơn.

Điểm quan trọng là cùng một bài toán logic nhưng **mô hình cập nhật khác nhau** dẫn đến cấu trúc khác nhau.

## 5. Lập lịch khoảng và exchange argument

Bài toán chọn nhiều khoảng không giao nhau nhất có nghiệm tham lam nổi tiếng: chọn khoảng có thời điểm kết thúc sớm nhất.

Lập luận trao đổi:

1. lấy một lời giải tối ưu bất kỳ;
2. nếu khoảng đầu tiên của lời giải không phải khoảng kết thúc sớm nhất `g`;
3. thay khoảng đầu đó bằng `g`;
4. vì `g` kết thúc không muộn hơn nên mọi khoảng phía sau vẫn khả thi;
5. tồn tại một lời giải tối ưu bắt đầu bằng `g`.

Do đó ta có thể khóa lựa chọn tham lam và tiếp tục trên phần timeline còn lại.

Đây là ví dụ rõ cho việc comparator `end` chứ không phải `start` mới tương ứng với bất biến cần chứng minh.

## 6. Weighted Interval Scheduling

Nếu mỗi khoảng có trọng số/lợi ích, “kết thúc sớm nhất” không còn tối ưu. Ta cần quy hoạch động.

Sau khi sắp theo `end`, với mỗi khoảng `i` tìm `p(i)`: khoảng gần nhất kết thúc trước khi `i` bắt đầu.

Khi đó:

\[
dp[i] = \max(dp[i-1],\ value_i + dp[p(i)])
\]

Tìm `p(i)` bằng tìm kiếm nhị phân giúp tổng thời gian `O(n log n)`.

Hai bài nhìn rất giống nhau nhưng objective khác nhau làm thay đổi toàn bộ chiến lược từ greedy sang DP. Đây là một cảnh báo quan trọng: **đừng nhận diện thuật toán chỉ từ hình dạng dữ liệu; phải nhìn objective và exchange property.**

## 7. Meeting Rooms và số lượng chồng lấn cực đại

Biến mỗi khoảng thành hai sự kiện:

```text
(start, +1)
(end,   -1)
```

Quét theo thời gian và duy trì số khoảng đang hoạt động. Giá trị cực đại là số tài nguyên đồng thời tối thiểu cần có.

Với `[start,end)`, tại cùng timestamp cần xử lý `end` trước `start`. Nếu miền dùng khoảng đóng, quy tắc có thể đổi.

Tie-breaking không phải chi tiết code; nó là hiện thân trực tiếp của ngữ nghĩa miền dữ liệu.

## 8. Hai mảng endpoint đã sắp xếp

Ta có thể tách toàn bộ `start[]` và `end[]`, sắp xếp riêng rồi dùng hai con trỏ. Nếu `start[i] < end[j]`, cần thêm tài nguyên; ngược lại một tài nguyên được giải phóng.

Đây vẫn là sweep line, chỉ khác cách biểu diễn sự kiện. Khi trạng thái chỉ cần một bộ đếm, không nhất thiết phải tạo object sự kiện đầy đủ.

## 9. Mảng hiệu như sweep line rời rạc

Nếu miền tọa độ nhỏ và nguyên, có thể đánh dấu thay đổi bằng mảng hiệu.

Với khoảng đóng `[l,r]`:

```text
diff[l] += 1
diff[r+1] -= 1
```

Prefix sum của `diff` chính là số khoảng đang hoạt động tại mỗi tọa độ.

Mảng hiệu là một sweep line trong đó trục đã nhỏ và rời rạc, nên không cần sorting sự kiện.

## 10. Coordinate Compression

Nếu tọa độ lên tới `10^9` nhưng chỉ có `O(n)` endpoint, có thể lấy toàn bộ tọa độ liên quan, sắp xếp unique rồi ánh xạ sang rank.

Compression giữ **thứ tự**, nhưng không tự giữ **khoảng cách**.

```text
100, 5000000, 900000000
 -> 0, 1, 2
```

Khoảng cách giữa rank 0 và 1 không bằng khoảng cách giữa rank 1 và 2. Nếu bài cần chiều dài, diện tích hoặc tích phân, phải giữ tọa độ gốc để tính độ dài thực.

Đây là lỗi rất phổ biến khi kết hợp coordinate compression với Segment Tree.

## 11. Active Set là phần quyết định cấu trúc dữ liệu

Sweep line chỉ quy định **thứ tự xử lý**. Cấu trúc dữ liệu phụ thuộc truy vấn cần thực hiện trên các đối tượng đang hoạt động:

```text
chỉ cần đếm                 -> integer
cần endpoint nhỏ nhất       -> heap
cần predecessor/successor   -> balanced BST
cần range aggregate         -> Fenwick / Segment Tree
cần interval overlap        -> interval tree / ordered structure
cần order statistics       -> augmented tree
```

Vì vậy sweep line là một khung thuật toán, không phải một cấu trúc cụ thể.

## 12. Invariant của active set

Một sweep line đúng phải xác định chính xác:

> Tại thời điểm ngay trước/sau khi xử lý sự kiện `x`, active set chứa chính xác những đối tượng nào?

Ví dụ với hình chữ nhật quét theo `x`, active set có thể chứa các hình chữ nhật có cạnh trái đã đi qua nhưng cạnh phải chưa đi qua.

Nếu ta không định nghĩa mốc “trước hay sau sự kiện” và quy tắc tie, rất dễ thêm/xóa sai đối tượng tại cùng tọa độ.

Đây là lý do event ordering cần được xem như một bất biến, không phải comparator ngẫu nhiên.

## 13. Giao của hai danh sách khoảng đã sắp xếp

Nếu hai danh sách đều đã sắp và nội bộ không giao nhau, dùng hai con trỏ.

Giao của `A=[a1,a2]`, `B=[b1,b2]` tồn tại nếu:

\[
\max(a1,b1) \le \min(a2,b2)
\]

Sau khi xử lý, tiến con trỏ của khoảng kết thúc sớm hơn, vì khoảng đó không còn khả năng giao với khoảng tương lai của phía kia.

Tổng thời gian `O(n+m)` thay vì `O(nm)`.

## 14. Rectangle Overlap

Quét theo `x`. Khi gặp cạnh trái của hình chữ nhật, thêm y-interval vào active set; khi gặp cạnh phải, xóa nó.

Nếu chỉ cần biết “có giao nhau không”, active set cần hỗ trợ tìm interval đang giao với y-interval mới. Nếu cần đếm tất cả cặp giao, cấu trúc và output-size bound thay đổi.

Số giao điểm có thể là `Θ(n²)`, vì vậy thuật toán liệt kê mọi giao không thể chạy nhanh hơn `Ω(k)` với `k` là số kết quả.

Đây là ví dụ của **độ phức tạp nhạy theo kích thước đầu ra (output-sensitive complexity)**.

## 15. Diện tích hợp của hình chữ nhật

Mỗi cạnh dọc tạo một sự kiện `(x, y1, y2, delta)`. Giữa hai giá trị `x` liên tiếp, tập hình chữ nhật đang hoạt động không đổi.

Nếu tổng độ dài y được phủ hiện tại là `L`:

\[
area += L\cdot(x_{next}-x_{current})
\]

Khó khăn còn lại là duy trì tổng độ dài hợp của các y-interval dưới add/remove. Segment Tree trên tọa độ y đã nén có thể lưu:

```text
coverCount
coveredLength
```

Nếu `coverCount > 0`, toàn node interval được phủ; nếu bằng 0, `coveredLength` bằng tổng của hai con.

Đây là một ví dụ mạnh về composition:

```text
sweep line theo x
+ coordinate compression theo y
+ Segment Tree duy trì union length
```

## 16. Event batching tại cùng tọa độ

Trong bài diện tích hoặc hình học, nhiều sự kiện có thể xảy ra cùng `x`. Một pattern an toàn là:

1. tính đóng góp từ `prevX` tới `x` bằng trạng thái active trước khi thay đổi;
2. xử lý toàn bộ sự kiện tại `x` theo quy ước;
3. chuyển sang tọa độ kế tiếp.

Batching tránh phụ thuộc không cần thiết vào thứ tự bên trong nhóm có cùng tọa độ khi bài toán chỉ quan tâm trạng thái giữa các tọa độ khác nhau.

## 17. Line Segment Intersection 2D

Trong 1D, thứ tự của các khoảng cố định. Trong 2D, nếu quét theo `x`, thứ tự `y` của các đoạn đang hoạt động có thể thay đổi khi chúng giao nhau.

Các thuật toán kiểu Bentley–Ottmann duy trì:

```text
event queue theo x
active set có thứ tự theo y tại x hiện tại
sự kiện bắt đầu/kết thúc/giao điểm
```

Điểm khó là comparator của active set phụ thuộc vị trí sweep line hiện tại. Đây không phải trường hợp bình thường của một BST comparator bất biến theo thời gian; implementation hình học tính toán cần xử lý rất cẩn thận các degeneracy và precision issues.

## 18. Geometric Predicates và dấu phẩy động

Orientation test trong hình học thường dựa trên tích có hướng:

\[
orient(a,b,c) = (b-a)\times(c-a)
\]

Dấu của giá trị cho biết ba điểm quay trái, quay phải hay thẳng hàng.

Nếu dùng floating point, sai số làm tròn có thể làm predicate gần 0 đổi dấu, phá thứ tự active set hoặc bỏ sót giao điểm. Với tọa độ nguyên trong miền vừa phải, có thể dùng số nguyên rộng hơn; với hình học chính xác cần kỹ thuật robust predicates.

Tính đúng đắn hình học thường phụ thuộc **predicate chính xác**, không chỉ cấu trúc dữ liệu.

## 19. Interval Tree và Sweep Line giải các workload khác nhau

Sweep line phù hợp khi có một tập sự kiện lớn và có thể xử lý offline theo một trục. Interval Tree phù hợp khi dữ liệu được giữ lâu và cần nhiều truy vấn overlap động.

```text
một lần xử lý offline        -> sorting + sweep thường rất mạnh
nhiều truy vấn động lâu dài  -> interval tree / augmented BST
```

Không nên dùng cấu trúc động phức tạp nếu có thể sort một lần rồi quét tuyến tính.

## 20. Temporal Data trong hệ thống thực tế

Khoảng thời gian trong database thường có các vấn đề mà bài DSA đơn giản bỏ qua:

```text
timezone
DST
valid-time vs transaction-time
open-ended interval
precision milliseconds/microseconds
inclusive/exclusive boundaries
```

Một hệ thống booking có thể dùng `[start,end)` để cho phép tài nguyên được dùng ngay khi booking trước kết thúc. Một hệ thống lịch sử giá có thể có khoảng mở tới vô cực.

Mô hình khoảng phải được thiết kế cùng business semantics.

## 21. Sweep Line trong log và telemetry

Nếu cần tính số request đồng thời từ log `(start,end)`, có thể dùng event sweep. Nếu luồng sự kiện đến theo thời gian thật và không thể reorder toàn bộ, bài toán chuyển sang online processing với watermark, out-of-order event và cửa sổ thời gian.

Sự khác biệt offline/online có thể biến một thuật toán sorting đơn giản thành một hệ thống stream phức tạp.

## 22. External-memory Sweep

Nếu số sự kiện quá lớn để vừa RAM, sorting ngoài bộ nhớ có thể tạo các run rồi merge. Sau khi sự kiện được phát ra theo thứ tự, sweep state có thể vẫn nhỏ hơn tổng dữ liệu.

Điều này minh họa một nguyên lý hệ thống: nhiều thuật toán sweep chỉ cần **thứ tự luồng**, không cần toàn bộ dữ liệu đã sắp xếp nằm trong RAM cùng lúc.

## 23. Parallel Sweep không tự nhiên như quét tuần tự

Trạng thái active tại vị trí `x` phụ thuộc tất cả sự kiện trước `x`, vì vậy sweep có dependency tuần tự. Một số bài có thể chia miền thành block, tính summary rồi ghép, nhưng phải thiết kế dữ liệu biên giữa các block.

Không nên giả định rằng sorting đã song song thì toàn bộ sweep cũng song song tốt.

## 24. Mẫu chứng minh sweep line

Một chứng minh thường có ba phần:

**Thứ tự sự kiện:** mọi thay đổi quan trọng được xử lý đúng thứ tự theo trục.

**Bất biến active set:** tại mỗi thời điểm, active set chứa chính xác các đối tượng có thể tương tác với sự kiện hiện tại hoặc tương lai gần.

**Loại bỏ an toàn:** khi một đối tượng rời active set, nó không thể còn ảnh hưởng tới bất kỳ sự kiện tương lai nào.

Nếu thiếu phần thứ ba, thuật toán rất dễ xóa trạng thái quá sớm.

## 25. Kiểm thử

Các case nên có:

```text
không có khoảng
một khoảng
nhiều khoảng bằng nhau
chỉ chạm biên
nhiều sự kiện cùng tọa độ
khoảng chứa hoàn toàn khoảng khác
tọa độ âm/rất lớn
hình chữ nhật suy biến
rất nhiều overlap
không overlap
```

Với union length/area, có thể differential-test trên miền tọa độ nhỏ bằng cách đánh dấu từng cell hoặc từng đoạn đơn vị rồi so kết quả với sweep.

## 26. Những hiểu lầm phổ biến

“Sort theo start rồi mọi bài interval đều giải giống nhau” — sai. Interval scheduling thường cần sort theo end; weighted scheduling cần DP; sweep geometry có event ordering riêng.

“Coordinate compression biến khoảng cách thành chỉ số” — sai. Nó chỉ giữ thứ tự, không giữ metric.

“Active set luôn là heap” — sai. Cấu trúc phụ thuộc truy vấn cần thực hiện trên các đối tượng đang hoạt động.

“Các event cùng tọa độ xử lý thứ tự nào cũng được” — sai khi ngữ nghĩa endpoint phụ thuộc tie-breaking.

“`O(n log n)` luôn là chi phí cuối” — sai nếu thuật toán phải xuất `k=Θ(n²)` giao điểm.

## Mô hình tư duy

> Thuật toán khoảng và đường quét tận dụng một trục có thứ tự để biến một bài toán tương tác toàn cục thành chuỗi thay đổi cục bộ. Sorting quyết định thứ tự tri thức; active set lưu đúng phần trạng thái còn có thể ảnh hưởng tương lai.

Khi gặp bài khoảng, hãy hỏi: **endpoint là đóng hay nửa mở, objective là hợp/giao/chọn tối đa/đếm overlap hay tối ưu trọng số, dữ liệu tĩnh hay động, có thể xử lý offline không, active set cần trả lời loại truy vấn nào, và số lượng kết quả có thể lớn tới đâu?**

Xem thêm: [Sorting](./01_sorting.md), [Greedy](./04_greedy_algorithms.md), [Dynamic Programming](./05_dynamic_programming.md), [Range Queries](../05_specialized/01_range_queries_fenwick_segment_tree.md), [Augmented Trees](../02_trees/06_augmented_trees_and_order_statistics.md).