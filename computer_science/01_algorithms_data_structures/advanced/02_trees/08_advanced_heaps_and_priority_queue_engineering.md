# Heap nâng cao và kỹ thuật hàng đợi ưu tiên
**Advanced Heaps & Priority Queue Engineering / 고급 힙과 우선순위 큐 설계**

Heap nhị phân là lựa chọn mặc định rất mạnh khi cần liên tục lấy phần tử nhỏ nhất hoặc lớn nhất. Tuy nhiên, khi tải công việc thay đổi, đặc biệt khi có nhiều thao tác `decrease-key`, `merge`, hàng triệu phần tử, dữ liệu gần đơn điệu hoặc yêu cầu đồng thời, “một heap nhị phân cho mọi bài” không còn là mô hình đủ sâu.

Chương này tập trung vào câu hỏi thiết kế: **hàng đợi ưu tiên cần hỗ trợ chính xác thao tác nào, với tần suất nào, và cách biểu diễn nào phù hợp nhất với mô hình bộ nhớ cũng như môi trường chạy?**

## 1. Hàng đợi ưu tiên là ADT, heap chỉ là một họ triển khai

Một hàng đợi ưu tiên có thể cần các thao tác:

```text
insert(x, priority)
peekMin()
extractMin()
decreaseKey(handle, newPriority)
increaseKey(handle, newPriority)
delete(handle)
meld(otherQueue)
bulkBuild(items)
```

Không phải mọi tải công việc đều cần tất cả. Heap nhị phân đặc biệt cân bằng cho `insert` và `extract-min`, nhưng nếu `meld` hoặc `decrease-key` xuất hiện dày đặc, các cấu trúc khác có thể đáng cân nhắc.

Điểm quan trọng là **đừng chọn cấu trúc từ tên bài toán; hãy chọn từ vector thao tác**.

## 2. Indexed Heap: khi phần tử có định danh ổn định

Heap chuẩn chỉ biết phần tử nằm ở vị trí nào trong mảng tại thời điểm hiện tại. Nếu muốn cập nhật độ ưu tiên của phần tử đã biết theo ID, cần ánh xạ:

```text
position[id] -> heapIndex
heap[heapIndex] -> itemId
priority[id]
```

Mỗi lần đổi chỗ hai phần tử trong heap phải cập nhật `position` tương ứng. Khi đó `decrease-key` có thể tìm đúng vị trí trong `O(1)` rồi `sift-up` trong `O(log n)`.

Đây là một **bất biến liên cấu trúc**:

```text
heap[position[id]] == id
position[heap[i]] == i
```

Một lỗi nhỏ khi swap mà quên cập nhật `position` có thể làm heap vẫn trông đúng theo thứ tự nhưng mọi cập nhật sau đó tác động nhầm phần tử.

### Khi nào Indexed Heap đáng dùng?

Dijkstra theo kiểu không tạo phần tử cũ, A*, bộ lập lịch nơi task thay đổi độ ưu tiên thường xuyên, hoặc mô phỏng sự kiện cần hủy/cập nhật sự kiện đã tồn tại là các ví dụ điển hình.

Nếu update hiếm và việc giữ phần tử cũ trong heap rẻ hơn, mẫu “push phiên bản mới rồi bỏ stale entry khi pop” thường đơn giản hơn.

## 3. D-ary Heap: giảm chiều cao, tăng chi phí chọn con

Heap nhị phân có 2 con mỗi nút. **D-ary heap** cho mỗi nút `d` con. Khi `d` tăng, chiều cao giảm:

\[
h = O(\log_d n)
\]

`decrease-key` có thể nhanh hơn vì đường đi lên ngắn hơn. Nhưng `extract-min` phải xem tối đa `d` con để chọn đứa nhỏ nhất ở mỗi tầng.

Xấp xỉ:

```text
insert/decrease-key -> O(log_d n)
extract-min         -> O(d log_d n)
```

Với Dijkstra trên đồ thị có rất nhiều phép giảm khóa so với số lần lấy min, `d > 2` đôi khi cải thiện hiệu năng thực tế. Tuy nhiên, lựa chọn tối ưu phụ thuộc cache, comparator và tỷ lệ thao tác; không có một giá trị `d` phổ quát.

## 4. Binomial Heap: thiết kế hướng tới meld

**Binomial Heap** là một rừng các cây nhị thức. Mỗi cây có kích thước là lũy thừa của hai, và trong một heap không có hai cây cùng bậc sau khi chuẩn hóa.

Ý tưởng này giống phép cộng nhị phân. Khi hai cây cùng bậc xuất hiện, ta liên kết cây có root lớn hơn dưới root nhỏ hơn, tạo một cây bậc cao hơn.

Nhờ đó, phép **meld** hai heap trở thành việc gộp hai danh sách cây theo bậc rồi xử lý các “carry”.

Đây là ví dụ cấu trúc dữ liệu được thiết kế từ một thao tác chủ đạo: nếu hợp nhất hai hàng đợi ưu tiên là first-class operation, cấu trúc rừng có thể tự nhiên hơn mảng heap đơn.

## 5. Fibonacci Heap: lý thuyết đẹp và bài học về amortized design

Fibonacci Heap nổi tiếng vì các cận khấu hao:

```text
insert       O(1) amortized
decrease-key O(1) amortized
meld         O(1) amortized
extract-min  O(log n) amortized
```

Ý tưởng là trì hoãn phần lớn việc hợp nhất cây cho tới `extract-min`. `decrease-key` dùng cắt nút và **cascading cut** để bảo vệ một bất biến mềm về cấu trúc.

Fibonacci Heap quan trọng về lý thuyết vì giúp đạt cận đẹp cho một số thuật toán đồ thị. Nhưng trong production hoặc competitive programming, nó thường thua heap nhị phân/pairing heap về constant factor, locality và độ phức tạp triển khai.

Bài học lớn hơn:

> Cận tiệm cận tốt hơn không tự động tạo implementation nhanh hơn nếu cấu trúc có nhiều con trỏ, cấp phát nhỏ và đường truy cập bộ nhớ kém cục bộ.

## 6. Pairing Heap: đơn giản hơn nhưng rất thực dụng

**Pairing Heap** là heap dạng cây với thao tác meld cực đơn giản: so sánh hai root, gắn root lớn hơn làm con của root nhỏ hơn.

`extract-min` thường gom các cây con của root và ghép chúng theo cặp rồi hợp nhất lại.

Pairing Heap có phân tích lý thuyết tinh tế hơn heap nhị phân, nhưng thực tế thường hấp dẫn khi cần `meld` hoặc `decrease-key` và muốn implementation đơn giản hơn Fibonacci Heap.

Nó là ví dụ điển hình cho khoảng cách giữa **cận lý thuyết chính xác** và **lựa chọn kỹ thuật thực tế**.

## 7. Leftist Heap và Skew Heap

Hai cấu trúc này cũng tối ưu quanh phép meld.

**Leftist Heap** lưu thêm thông tin đường null ngắn nhất và duy trì bất biến khiến nhánh phải ngắn. Khi meld, ta đi dọc nhánh phải rồi đổi con nếu cần để khôi phục bất biến.

**Skew Heap** bỏ metadata đó và đơn giản hoá bằng cách đổi hai cây con sau meld. Bảo đảm đến từ phân tích khấu hao chứ không phải một ràng buộc chiều cao chặt sau từng thao tác.

Đây là ví dụ hay cho hai triết lý:

```text
lưu metadata để giữ bất biến rõ ràng
vs
bỏ metadata và dựa vào amortized behavior
```

## 8. Monotone Priority Queue

Một số thuật toán có property rằng khóa được lấy ra không giảm theo thời gian. Dijkstra với trọng số không âm là ví dụ: khoảng cách đã chốt tiếp theo không nhỏ hơn khoảng cách đã chốt trước đó.

Nếu key còn là số nguyên trong miền phù hợp, ta có thể dùng cấu trúc chuyên biệt thay vì heap so sánh tổng quát.

### Dial's Algorithm

Nếu trọng số cạnh là số nguyên không âm bị chặn bởi `C`, có thể dùng các bucket theo khoảng cách modulo một cửa sổ phù hợp. Khi `C` nhỏ, điều này thay `log n` bằng thao tác gần hằng số.

### Radix Heap

Radix Heap khai thác điều kiện khóa trích xuất không giảm. Các bucket được tổ chức theo bit khác biệt cao nhất so với `lastExtracted`. Khi bucket gần nhất được mở, phần tử được phân phối lại theo mốc mới.

Cấu trúc này đặc biệt hữu ích cho shortest path với trọng số nguyên lớn hơn phạm vi Dial nhưng vẫn cần hiệu năng tốt.

Bài học: **monotonicity là thông tin thêm có thể đổi hoàn toàn cấu trúc hàng đợi ưu tiên**.

## 9. Calendar Queue và bộ mô phỏng sự kiện

Trong mô phỏng sự kiện rời rạc, timestamp thường tăng dần và phân phối có thể tương đối đều. **Calendar Queue** chia thời gian thành các bucket tương tự lịch, cố gắng làm insert/extract gần hằng số trung bình.

Nhưng hiệu quả rất nhạy với phân phối timestamp và cách chọn độ rộng bucket. Khi dữ liệu lệch hoặc bursty, cấu trúc có thể suy giảm.

Đây là một ví dụ quan trọng: một cấu trúc có average-case tốt dựa trên mô hình dữ liệu phải được đo với phân phối thật, không chỉ với input ngẫu nhiên đẹp.

## 10. Heap và cache locality

Heap nhị phân bằng mảng có locality tương đối tốt, nhưng `sift-down` nhảy theo chỉ số tăng gần gấp đôi mỗi tầng. Với heap rất lớn, đường đi có thể chạm nhiều dòng cache khác nhau.

D-ary heap giảm số tầng và tăng số con nằm gần nhau hơn trong mảng. Vì vậy, dù phải so nhiều con mỗi tầng, cache behavior đôi khi tốt hơn heap nhị phân.

Đây là lý do benchmarking theo workload thật quan trọng hơn việc chỉ đọc công thức Big-O.

## 11. So sánh comparator và khóa tốn kém

Nếu comparator chỉ so hai `int`, chi phí heap chủ yếu là di chuyển dữ liệu. Nhưng nếu comparator phải so chuỗi dài, nhiều trường object hoặc gọi logic phức tạp, số lần so sánh trở thành yếu tố chính.

Có thể lưu **khóa đã chuẩn hóa (normalized key)** hoặc score đã tính sẵn bên cạnh item để tránh tính lại trong mỗi phép so sánh.

Tuy nhiên, nếu score có thể thay đổi, metadata phải được cập nhật nhất quán; nếu không heap property sẽ dựa trên giá trị cũ.

## 12. Stable Priority Queue

Heap chuẩn không bảo đảm thứ tự giữa hai phần tử có cùng priority. Nếu hệ thống cần FIFO trong cùng mức ưu tiên, có thể dùng khóa tổng hợp:

```text
(priority, sequenceNumber)
```

Trong đó `sequenceNumber` tăng dần theo thời điểm enqueue.

Đây là một ví dụ cho việc **tie-breaking là một phần của specification**, không phải chi tiết trang trí. Nếu bỏ nó, hai lần chạy có thể cho thứ tự khác nhau dù mọi priority giống nhau.

## 13. Deadline, priority và starvation

Một scheduler chỉ dùng max-heap theo priority có thể làm task priority thấp chờ mãi nếu task priority cao liên tục xuất hiện. Đây là **starvation**.

Một kỹ thuật là **aging**: tăng priority hiệu dụng theo thời gian chờ. Khi đó priority không còn tĩnh; cập nhật key trở thành thao tác thường xuyên và có thể ảnh hưởng lựa chọn cấu trúc.

Earliest Deadline First lại dùng deadline thay priority tĩnh. Các mô hình scheduling khác nhau tạo các order khác nhau; không nên gọi chung mọi thứ là “priority queue” rồi bỏ qua semantics.

## 14. Bounded Priority Queue và Top-K streaming

Nếu chỉ quan tâm `k` phần tử tốt nhất, heap không nên tăng đến `n`.

Một min-heap kích thước `k` giữ top-k lớn nhất:

```text
heap chưa đủ k       -> insert
x <= min(heap)       -> bỏ
x > min(heap)        -> thay min bằng x
```

Tổng thời gian `O(n log k)`, bộ nhớ `O(k)`.

Trong hệ thống phân tán, mỗi shard có thể tạo local top-k rồi coordinator gộp các ứng viên. Tuy nhiên, local top-k kích thước đúng `k` không phải lúc nào cũng đủ nếu scoring toàn cục phụ thuộc dữ liệu từ nhiều shard; phải chứng minh reduction giữ đúng candidate set.

## 15. Lazy Deletion

Nhiều heap API không hỗ trợ xóa arbitrary element. Một pattern phổ biến là **lazy deletion**:

```text
đánh dấu item là invalid
khi item lên root thì bỏ qua và pop tiếp
```

Cách này đơn giản nhưng làm heap chứa rác. Nếu invalid item tích lũy nhanh hơn tốc độ bị pop, bộ nhớ và latency có thể tăng.

Do đó lazy deletion thường cần policy rebuild hoặc cơ chế epoch/version để giới hạn rác.

## 16. Hai heap cho median động

Để duy trì median của luồng:

```text
max-heap lowerHalf
min-heap upperHalf
```

Bất biến:

```text
mọi phần tử lower <= mọi phần tử upper
|size(lower) - size(upper)| <= 1
```

Median lấy từ một hoặc hai root. Insert cần đặt vào nửa phù hợp rồi rebalance.

Nếu thêm thao tác xóa phần tử khỏi cửa sổ trượt, hai heap thường kết hợp với lazy deletion và bảng đếm phiên bản. Khi đó correctness không chỉ nằm ở heap property mà còn ở bất biến giữa **kích thước logic** và **kích thước vật lý** của heap.

## 17. Hàng đợi ưu tiên đồng thời

Một heap có một root nóng; nhiều luồng cùng insert/extract có thể tranh chấp khóa mạnh. Vì vậy concurrent priority queue khó mở rộng hơn queue FIFO phân vùng tốt.

Các thiết kế có thể dùng nhiều heap con, skip-list có thứ tự, relaxed priority queue hoặc multi-queue: mỗi thao tác chọn ngẫu nhiên vài queue và thao tác trên một queue phù hợp.

Đổi lại, một số thiết kế chấp nhận **relaxed ordering**: phần tử lấy ra gần nhỏ nhất chứ không tuyệt đối nhỏ nhất. Nếu ứng dụng cho phép, relaxation có thể cải thiện scalability đáng kể.

## 18. External-memory Priority Queue

Khi hàng đợi ưu tiên vượt RAM, số I/O theo khối trở thành mô hình chi phí quan trọng. Heap nhị phân đơn giản có thể gây nhiều truy cập ngẫu nhiên.

Các cấu trúc ưu tiên cho external memory cố batch insert, buffer update và hợp nhất các run để giảm số block transfer. Đây là cùng tư duy với B-Tree và external merge sort: tối ưu **di chuyển dữ liệu**, không chỉ số phép so sánh.

## 19. Kiểm thử heap nâng cao

Ngoài test `extract` ra thứ tự tăng dần, cần kiểm tra bất biến sau chuỗi thao tác ngẫu nhiên.

Với indexed heap:

```text
heap[position[id]] == id
```

Với hai heap median:

```text
max(lower) <= min(upper)
kích thước logic cân bằng
median khớp với mảng tham chiếu đã sắp xếp
```

Với meldable heap, có thể tạo nhiều heap nhỏ, meld theo thứ tự ngẫu nhiên rồi so toàn bộ chuỗi extract với một multiset tham chiếu.

Property-based testing rất phù hợp vì lỗi heap thường chỉ xuất hiện sau một chuỗi update đặc biệt.

## 20. Chọn heap theo tải công việc

| Tải công việc | Ứng viên thường hợp lý |
|---|---|
| General insert/extract | Binary Heap |
| Nhiều decrease-key | Indexed Heap, D-ary Heap, Pairing Heap |
| Meld thường xuyên | Binomial/Pairing/Leftist/Skew Heap |
| Lý thuyết decrease-key tối ưu | Fibonacci Heap |
| Khóa nguyên đơn điệu | Dial / Radix Heap |
| Top-K streaming | Bounded Binary Heap |
| Median động | Two Heaps |
| Concurrent, chấp nhận gần đúng | Multi-queue / relaxed PQ |
| Dữ liệu vượt RAM | External-memory PQ |

Bảng này là điểm xuất phát, không phải luật tuyệt đối. Constant factor, cache, độ phức tạp implementation và semantics của API vẫn phải được đo.

## Mô hình tư duy

> Heap không phải một cấu trúc duy nhất mà là **một họ cách biểu diễn thứ tự bộ phận**. Chọn đúng biến thể nghĩa là hiểu thao tác nào thật sự đắt trong tải công việc của mình.

Khi gặp một bài toán hàng đợi ưu tiên, hãy hỏi:

```text
Có cần update key không?
Có cần xóa arbitrary item không?
Có cần meld không?
Khóa có đơn điệu không?
Có giới hạn top-k không?
Priority có tie-breaking hay fairness semantics không?
Dữ liệu có vừa RAM không?
Có cần concurrent scalability hay strict ordering không?
```

Xem thêm: [Heap cơ bản](./03_heaps.md), [Queue/Deque/Priority Queue](../01_linear_structures/03_queues_deques_and_priority_queues.md), [Shortest Paths](../03_graphs/02_shortest_paths.md), [Selection & Top-K](../04_algorithmic_paradigms/06_selection_and_top_k.md), [Scheduler Case Study](../90_connections/07_case_study_scheduler_backpressure.md).