# Vùng nhớ vùng nhớ động (heap / 힙) nâng cao và kỹ thuật hàng đợi ưu tiên

> **Mạch đọc:** [README](../README.md) là bản đồ owner của **Vùng nhớ vùng nhớ động (heap / 힙) nâng cao và kỹ thuật hàng đợi ưu tiên**; nhìn vào vị trí đó trước để biết file này đang phục vụ nhánh kiến thức nào. **1. Hàng đợi ưu tiên là ADT, vùng nhớ động (heap / 힙) chỉ là một họ triển khai** mở đối tượng chính của file và câu hỏi cần theo dõi; sau đó sang **2. Indexed vùng nhớ động (heap / 힙): khi phần tử có định danh ổn định** để mở rộng đối tượng sang phạm vi kế cận. Mạch này nối advanced heaps với priority queue engineering, invariant và cache, để hàng đợi ưu tiên chạy ổn định.

**Advanced Heaps & Priority hàng đợi (queue / 큐) kỹ thuật (engineering / 엔지니어링) / 고급 힙과 우선순위 큐 설계**

Vùng nhớ vùng nhớ động (heap / 힙) nhị phân là lựa chọn mặc định rất mạnh khi cần liên tục lấy phần tử nhỏ nhất hoặc lớn nhất. Tuy nhiên, khi tải công việc thay đổi, đặc biệt khi có nhiều thao tác `decrease-key`, `merge`, hàng triệu phần tử, dữ liệu gần đơn điệu hoặc yêu cầu đồng thời, “một vùng nhớ động (heap / 힙) nhị phân cho mọi bài” không còn là mô hình đủ sâu.

Chương này tập trung vào câu hỏi thiết kế: **hàng đợi ưu tiên cần hỗ trợ chính xác thao tác nào, với tần suất nào, và cách biểu diễn nào phù hợp nhất với mô hình bộ nhớ cũng như môi trường chạy?**

## 1. Hàng đợi ưu tiên là ADT, vùng nhớ động (heap / 힙) chỉ là một họ triển khai

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

Không phải mọi tải công việc đều cần tất cả. vùng nhớ động (heap / 힙) nhị phân đặc biệt cân bằng cho `insert` và `extract-min`, nhưng nếu `meld` hoặc `decrease-key` xuất hiện dày đặc, các cấu trúc khác có thể đáng cân nhắc.

Điểm quan trọng là **đừng chọn cấu trúc từ tên bài toán; hãy chọn từ véc-tơ (vector / 벡터) thao tác**.

> **Chuyển mạch:** Trong **Vùng nhớ vùng nhớ động (heap / 힙) nâng cao và kỹ thuật hàng đợi ưu tiên**, **2. Indexed vùng nhớ động (heap / 힙): khi phần tử có định danh ổn định** tiếp nhận điểm tựa từ **1. Hàng đợi ưu tiên là ADT, vùng nhớ động (heap / 힙) chỉ là một họ triển khai** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **3. D-ary vùng nhớ động (heap / 힙): giảm chiều cao, tăng chi phí chọn con** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 2. Indexed vùng nhớ động (heap / 힙): khi phần tử có định danh ổn định

Vùng nhớ vùng nhớ động (heap / 힙) chuẩn chỉ biết phần tử nằm ở vị trí nào trong mảng tại thời điểm hiện tại. Nếu muốn cập nhật độ ưu tiên của phần tử đã biết theo ID, cần ánh xạ:

```text
position[id] -> heapIndex
heap[heapIndex] -> itemId
priority[id]
```

Mỗi lần đổi chỗ hai phần tử trong vùng nhớ động (heap / 힙) phải cập nhật `position` tương ứng. Khi đó `decrease-key` có thể tìm đúng vị trí trong `O(1)` rồi `sift-up` trong `O(log n)`.

Đây là một **bất biến liên cấu trúc**:

```text
heap[position[id]] == id
position[heap[i]] == i
```

Một lỗi nhỏ khi swap mà quên cập nhật `position` có thể làm vùng nhớ động (heap / 힙) vẫn trông đúng theo thứ tự nhưng mọi cập nhật sau đó tác động nhầm phần tử.

### Khi nào Indexed vùng nhớ động (heap / 힙) đáng dùng?

Dijkstra theo kiểu không tạo phần tử cũ, A*, bộ lập lịch nơi tác vụ (task / 작업) thay đổi độ ưu tiên thường xuyên, hoặc mô phỏng sự kiện cần hủy/cập nhật sự kiện đã tồn tại là các ví dụ điển hình.

Nếu cập nhật (update / 업데이트) hiếm và việc giữ phần tử cũ trong vùng nhớ động (heap / 힙) rẻ hơn, mẫu “push phiên bản mới rồi bỏ stale entry khi pop” thường đơn giản hơn.

> **Chuyển mạch:** Ở chặng này của **Vùng nhớ vùng nhớ động (heap / 힙) nâng cao và kỹ thuật hàng đợi ưu tiên**, **3. D-ary vùng nhớ động (heap / 힙): giảm chiều cao, tăng chi phí chọn con** tiếp nhận điểm tựa từ **2. Indexed vùng nhớ động (heap / 힙): khi phần tử có định danh ổn định** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **4. Binomial vùng nhớ động (heap / 힙): thiết kế hướng tới meld** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 3. D-ary vùng nhớ động (heap / 힙): giảm chiều cao, tăng chi phí chọn con

Vùng nhớ vùng nhớ động (heap / 힙) nhị phân có 2 con mỗi nút. **D-ary vùng nhớ động (heap / 힙)** cho mỗi nút `d` con. Khi `d` tăng, chiều cao giảm:

\[
h = O(\log_d n)
\]

`decrease-key` có thể nhanh hơn vì đường đi lên ngắn hơn. Nhưng `extract-min` phải xem tối đa `d` con để chọn đứa nhỏ nhất ở mỗi tầng.

Xấp xỉ:

```text
insert/decrease-key -> O(log_d n)
extract-min         -> O(d log_d n)
```

Với Dijkstra trên đồ thị có rất nhiều phép giảm khóa so với số lần lấy min, `d > 2` đôi khi cải thiện hiệu năng thực tế. Tuy nhiên, lựa chọn tối ưu phụ thuộc bộ nhớ đệm (cache / 캐시), comparator và tỷ lệ thao tác; không có một giá trị `d` phổ quát.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Vùng nhớ vùng nhớ động (heap / 힙) nâng cao và kỹ thuật hàng đợi ưu tiên**, **4. Binomial vùng nhớ động (heap / 힙): thiết kế hướng tới meld** tiếp nhận điểm tựa từ **3. D-ary vùng nhớ động (heap / 힙): giảm chiều cao, tăng chi phí chọn con** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **5. Fibonacci vùng nhớ động (heap / 힙): lý thuyết đẹp và bài học về amortized thiết kế (design / 설계)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 4. Binomial vùng nhớ động (heap / 힙): thiết kế hướng tới meld

**Binomial vùng nhớ động (heap / 힙)** là một rừng các cây nhị thức. Mỗi cây có kích thước là lũy thừa của hai, và trong một vùng nhớ động (heap / 힙) không có hai cây cùng bậc sau khi chuẩn hóa.

Ý tưởng này giống phép cộng nhị phân. Khi hai cây cùng bậc xuất hiện, ta liên kết cây có gốc (root / 루트) lớn hơn dưới gốc (root / 루트) nhỏ hơn, tạo một cây bậc cao hơn.

Nhờ đó, phép **meld** hai vùng nhớ động (heap / 힙) trở thành việc gộp hai danh sách cây theo bậc rồi xử lý các “carry”.

Đây là ví dụ cấu trúc dữ liệu được thiết kế từ một thao tác chủ đạo: nếu hợp nhất hai hàng đợi ưu tiên là first-class thao tác (operation / 연산), cấu trúc rừng có thể tự nhiên hơn mảng vùng nhớ động (heap / 힙) đơn.

> **Chuyển mạch:** Trong **Vùng nhớ vùng nhớ động (heap / 힙) nâng cao và kỹ thuật hàng đợi ưu tiên**, **5. Fibonacci vùng nhớ động (heap / 힙): lý thuyết đẹp và bài học về amortized thiết kế (design / 설계)** tiếp nhận điểm tựa từ **4. Binomial vùng nhớ động (heap / 힙): thiết kế hướng tới meld** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **6. Pairing vùng nhớ động (heap / 힙): đơn giản hơn nhưng rất thực dụng** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 5. Fibonacci vùng nhớ động (heap / 힙): lý thuyết đẹp và bài học về amortized thiết kế (design / 설계)

Fibonacci vùng nhớ động (heap / 힙) nổi tiếng vì các cận khấu hao:

```text
insert       O(1) amortized
decrease-key O(1) amortized
meld         O(1) amortized
extract-min  O(log n) amortized
```

Ý tưởng là trì hoãn phần lớn việc hợp nhất cây cho tới `extract-min`. `decrease-key` dùng cắt nút và **cascading cut** để bảo vệ một bất biến mềm về cấu trúc.

Fibonacci vùng nhớ động (heap / 힙) quan trọng về lý thuyết vì giúp đạt cận đẹp cho một số thuật toán đồ thị. Nhưng trong môi trường vận hành (production / 운영 환경) hoặc competitive programming, nó thường thua vùng nhớ động (heap / 힙) nhị phân/pairing vùng nhớ động (heap / 힙) về constant factor, locality và độ phức tạp triển khai.

Bài học lớn hơn:

> Cận tiệm cận tốt hơn không tự động tạo hiện thực (implementation / 구현) nhanh hơn nếu cấu trúc có nhiều con trỏ, cấp phát nhỏ và đường truy cập bộ nhớ kém cục bộ.

> **Chuyển mạch:** Ở chặng này của **Vùng nhớ vùng nhớ động (heap / 힙) nâng cao và kỹ thuật hàng đợi ưu tiên**, **6. Pairing vùng nhớ động (heap / 힙): đơn giản hơn nhưng rất thực dụng** tiếp nhận điểm tựa từ **5. Fibonacci vùng nhớ động (heap / 힙): lý thuyết đẹp và bài học về amortized thiết kế (design / 설계)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **7. Leftist vùng nhớ động (heap / 힙) và Skew vùng nhớ động (heap / 힙)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 6. Pairing vùng nhớ động (heap / 힙): đơn giản hơn nhưng rất thực dụng

**Pairing vùng nhớ động (heap / 힙)** là vùng nhớ động (heap / 힙) dạng cây với thao tác meld cực đơn giản: so sánh hai gốc (root / 루트), gắn gốc (root / 루트) lớn hơn làm con của gốc (root / 루트) nhỏ hơn.

`extract-min` thường gom các cây con của gốc (root / 루트) và ghép chúng theo cặp rồi hợp nhất lại.

Pairing vùng nhớ động (heap / 힙) có phân tích lý thuyết tinh tế hơn vùng nhớ động (heap / 힙) nhị phân, nhưng thực tế thường hấp dẫn khi cần `meld` hoặc `decrease-key` và muốn hiện thực (implementation / 구현) đơn giản hơn Fibonacci vùng nhớ động (heap / 힙).

Nó là ví dụ điển hình cho khoảng cách giữa **cận lý thuyết chính xác** và **lựa chọn kỹ thuật thực tế**.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Vùng nhớ vùng nhớ động (heap / 힙) nâng cao và kỹ thuật hàng đợi ưu tiên**, **7. Leftist vùng nhớ động (heap / 힙) và Skew vùng nhớ động (heap / 힙)** tiếp nhận điểm tựa từ **6. Pairing vùng nhớ động (heap / 힙): đơn giản hơn nhưng rất thực dụng** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **8. Monotone Priority hàng đợi (queue / 큐)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 7. Leftist vùng nhớ động (heap / 힙) và Skew vùng nhớ động (heap / 힙)

Hai cấu trúc này cũng tối ưu quanh phép meld.

**Leftist vùng nhớ động (heap / 힙)** lưu thêm thông tin đường null ngắn nhất và duy trì bất biến khiến nhánh phải ngắn. Khi meld, ta đi dọc nhánh phải rồi đổi con nếu cần để khôi phục bất biến.

**Skew vùng nhớ động (heap / 힙)** bỏ siêu dữ liệu (metadata / 메타데이터) đó và đơn giản hoá bằng cách đổi hai cây con sau meld. Bảo đảm đến từ phân tích khấu hao chứ không phải một ràng buộc chiều cao chặt sau từng thao tác.

Đây là ví dụ hay cho hai triết lý:

```text
lưu metadata để giữ bất biến rõ ràng
vs
bỏ metadata và dựa vào amortized behavior
```

> **Chuyển mạch:** Trong **Vùng nhớ vùng nhớ động (heap / 힙) nâng cao và kỹ thuật hàng đợi ưu tiên**, **8. Monotone Priority hàng đợi (queue / 큐)** tiếp nhận điểm tựa từ **7. Leftist vùng nhớ động (heap / 힙) và Skew vùng nhớ động (heap / 힙)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **9. Calendar hàng đợi (queue / 큐) và bộ mô phỏng sự kiện** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 8. Monotone Priority hàng đợi (queue / 큐)

Một số thuật toán có thuộc tính (property / 속성) rằng khóa được lấy ra không giảm theo thời gian. Dijkstra với trọng số không âm là ví dụ: khoảng cách đã chốt tiếp theo không nhỏ hơn khoảng cách đã chốt trước đó.

Nếu key còn là số nguyên trong miền phù hợp, ta có thể dùng cấu trúc chuyên biệt thay vì vùng nhớ động (heap / 힙) so sánh tổng quát.

### Dial's thuật toán (algorithm / 알고리즘)

Nếu trọng số cạnh là số nguyên không âm bị chặn bởi `C`, có thể dùng các bucket theo khoảng cách modulo một cửa sổ phù hợp. Khi `C` nhỏ, điều này thay `log n` bằng thao tác gần hằng số.

### Radix vùng nhớ động (heap / 힙)

Radix vùng nhớ động (heap / 힙) khai thác điều kiện khóa trích xuất không giảm. Các bucket được tổ chức theo bit khác biệt cao nhất so với `lastExtracted`. Khi bucket gần nhất được mở, phần tử được phân phối lại theo mốc mới.

Cấu trúc này đặc biệt hữu ích cho shortest đường dẫn (path / 경로) với trọng số nguyên lớn hơn phạm vi Dial nhưng vẫn cần hiệu năng tốt.

Bài học: **monotonicity là thông tin thêm có thể đổi hoàn toàn cấu trúc hàng đợi ưu tiên**.

> **Chuyển mạch:** Ở chặng này của **Vùng nhớ vùng nhớ động (heap / 힙) nâng cao và kỹ thuật hàng đợi ưu tiên**, **9. Calendar hàng đợi (queue / 큐) và bộ mô phỏng sự kiện** tiếp nhận điểm tựa từ **8. Monotone Priority hàng đợi (queue / 큐)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **10. vùng nhớ động (heap / 힙) và bộ nhớ đệm (cache / 캐시) locality** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 9. Calendar hàng đợi (queue / 큐) và bộ mô phỏng sự kiện

Trong mô phỏng sự kiện rời rạc, timestamp thường tăng dần và phân phối có thể tương đối đều. **Calendar hàng đợi (queue / 큐)** chia thời gian thành các bucket tương tự lịch, cố gắng làm insert/extract gần hằng số trung bình.

Nhưng hiệu quả rất nhạy với phân phối timestamp và cách chọn độ rộng bucket. Khi dữ liệu lệch hoặc bursty, cấu trúc có thể suy giảm.

Đây là một ví dụ quan trọng: một cấu trúc có average-case tốt dựa trên mô hình dữ liệu phải được đo với phân phối thật, không chỉ với đầu vào (input / 입력) ngẫu nhiên đẹp.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Vùng nhớ vùng nhớ động (heap / 힙) nâng cao và kỹ thuật hàng đợi ưu tiên**, **10. vùng nhớ động (heap / 힙) và bộ nhớ đệm (cache / 캐시) locality** tiếp nhận điểm tựa từ **9. Calendar hàng đợi (queue / 큐) và bộ mô phỏng sự kiện** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **11. So sánh comparator và khóa tốn kém** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 10. vùng nhớ động (heap / 힙) và bộ nhớ đệm (cache / 캐시) locality

Vùng nhớ vùng nhớ động (heap / 힙) nhị phân bằng mảng có locality tương đối tốt, nhưng `sift-down` nhảy theo chỉ số tăng gần gấp đôi mỗi tầng. Với vùng nhớ động (heap / 힙) rất lớn, đường đi có thể chạm nhiều dòng bộ nhớ đệm (cache / 캐시) khác nhau.

D-ary vùng nhớ động (heap / 힙) giảm số tầng và tăng số con nằm gần nhau hơn trong mảng. Vì vậy, dù phải so nhiều con mỗi tầng, bộ nhớ đệm (cache / 캐시) hành vi (behavior / 동작) đôi khi tốt hơn vùng nhớ động (heap / 힙) nhị phân.

Đây là lý do benchmarking theo tải công việc (workload / 워크로드) thật quan trọng hơn việc chỉ đọc công thức Big-O.

> **Chuyển mạch:** Trong **Vùng nhớ vùng nhớ động (heap / 힙) nâng cao và kỹ thuật hàng đợi ưu tiên**, **10. vùng nhớ động (heap / 힙) và bộ nhớ đệm (cache / 캐시) locality** đã nêu tiêu chí phân biệt, còn **11. So sánh comparator và khóa tốn kém** dùng tiêu chí đó để soi ranh giới và điểm dễ nhầm. Từ đây, **12. Stable Priority hàng đợi (queue / 큐)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 11. So sánh comparator và khóa tốn kém

Nếu comparator chỉ so hai `int`, chi phí vùng nhớ động (heap / 힙) chủ yếu là di chuyển dữ liệu. Nhưng nếu comparator phải so chuỗi dài, nhiều trường đối tượng (object / 객체) hoặc gọi lô-gic (logic / 논리) phức tạp, số lần so sánh trở thành yếu tố chính.

Có thể lưu **khóa đã chuẩn hóa (normalized key)** hoặc score đã tính sẵn bên cạnh item để tránh tính lại trong mỗi phép so sánh.

Tuy nhiên, nếu score có thể thay đổi, siêu dữ liệu (metadata / 메타데이터) phải được cập nhật nhất quán; nếu không vùng nhớ động (heap / 힙) thuộc tính (property / 속성) sẽ dựa trên giá trị cũ.

> **Chuyển mạch:** Ở chặng này của **Vùng nhớ vùng nhớ động (heap / 힙) nâng cao và kỹ thuật hàng đợi ưu tiên**, **11. So sánh comparator và khóa tốn kém** đã nêu tiêu chí phân biệt, còn **12. Stable Priority hàng đợi (queue / 큐)** dùng tiêu chí đó để soi ranh giới và điểm dễ nhầm. Từ đây, **13. Deadline, priority và starvation** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 12. Stable Priority hàng đợi (queue / 큐)

Vùng nhớ vùng nhớ động (heap / 힙) chuẩn không bảo đảm thứ tự giữa hai phần tử có cùng priority. Nếu hệ thống cần FIFO trong cùng mức ưu tiên, có thể dùng khóa tổng hợp:

```text
(priority, sequenceNumber)
```

Trong đó `sequenceNumber` tăng dần theo thời điểm enqueue.

Đây là một ví dụ cho việc **tie-breaking là một phần của specification**, không phải chi tiết trang trí. Nếu bỏ nó, hai lần chạy có thể cho thứ tự khác nhau dù mọi priority giống nhau.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Vùng nhớ vùng nhớ động (heap / 힙) nâng cao và kỹ thuật hàng đợi ưu tiên**, **13. Deadline, priority và starvation** tiếp nhận điểm tựa từ **12. Stable Priority hàng đợi (queue / 큐)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **14. Bounded Priority hàng đợi (queue / 큐) và Top-K streaming** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 13. Deadline, priority và starvation

Một scheduler chỉ dùng max-heap theo priority có thể làm tác vụ (task / 작업) priority thấp chờ mãi nếu tác vụ (task / 작업) priority cao liên tục xuất hiện. Đây là **starvation**.

Một kỹ thuật là **aging**: tăng priority hiệu dụng theo thời gian chờ. Khi đó priority không còn tĩnh; cập nhật key trở thành thao tác thường xuyên và có thể ảnh hưởng lựa chọn cấu trúc.

Earliest Deadline First lại dùng deadline thay priority tĩnh. Các mô hình scheduling khác nhau tạo các thứ tự (order / 순서) khác nhau; không nên gọi chung mọi thứ là “priority hàng đợi (queue / 큐)” rồi bỏ qua ngữ nghĩa (semantics / 의미론).

> **Chuyển mạch:** Trong **Vùng nhớ vùng nhớ động (heap / 힙) nâng cao và kỹ thuật hàng đợi ưu tiên**, **14. Bounded Priority hàng đợi (queue / 큐) và Top-K streaming** tiếp nhận điểm tựa từ **13. Deadline, priority và starvation** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **15. Lazy Deletion** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 14. Bounded Priority hàng đợi (queue / 큐) và Top-K streaming

Nếu chỉ quan tâm `k` phần tử tốt nhất, vùng nhớ động (heap / 힙) không nên tăng đến `n`.

Một min-heap kích thước `k` giữ top-k lớn nhất:

```text
heap chưa đủ k       -> insert
x <= min(heap)       -> bỏ
x > min(heap)        -> thay min bằng x
```

Tổng thời gian `O(n log k)`, bộ nhớ `O(k)`.

Trong hệ thống phân tán, mỗi shard có thể tạo cục bộ (local / 로컬) top-k rồi coordinator gộp các ứng viên. Tuy nhiên, cục bộ (local / 로컬) top-k kích thước đúng `k` không phải lúc nào cũng đủ nếu scoring toàn cục phụ thuộc dữ liệu từ nhiều shard; phải chứng minh reduction giữ đúng candidate set.

> **Chuyển mạch:** Ở chặng này của **Vùng nhớ vùng nhớ động (heap / 힙) nâng cao và kỹ thuật hàng đợi ưu tiên**, **15. Lazy Deletion** tiếp nhận điểm tựa từ **14. Bounded Priority hàng đợi (queue / 큐) và Top-K streaming** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **16. Hai vùng nhớ động (heap / 힙) cho median động** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 15. Lazy Deletion

Nhiều vùng nhớ động (heap / 힙) API không hỗ trợ xóa arbitrary element. Một mẫu (pattern / 패턴) phổ biến là **lazy deletion**:

```text
đánh dấu item là invalid
khi item lên root thì bỏ qua và pop tiếp
```

Cách này đơn giản nhưng làm vùng nhớ động (heap / 힙) chứa rác. Nếu invalid item tích lũy nhanh hơn tốc độ bị pop, bộ nhớ và độ trễ (latency / 지연 시간) có thể tăng.

Do đó lazy deletion thường cần chính sách (policy / 정책) rebuild hoặc cơ chế epoch/phiên bản (version / 버전) để giới hạn rác.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Vùng nhớ vùng nhớ động (heap / 힙) nâng cao và kỹ thuật hàng đợi ưu tiên**, **16. Hai vùng nhớ động (heap / 힙) cho median động** tiếp nhận điểm tựa từ **15. Lazy Deletion** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **17. Hàng đợi ưu tiên đồng thời** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 16. Hai vùng nhớ động (heap / 힙) cho median động

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

Median lấy từ một hoặc hai gốc (root / 루트). Insert cần đặt vào nửa phù hợp rồi rebalance.

Nếu thêm thao tác xóa phần tử khỏi cửa sổ trượt, hai vùng nhớ động (heap / 힙) thường kết hợp với lazy deletion và bảng đếm phiên bản. Khi đó tính đúng đắn (correctness / 정확성) không chỉ nằm ở vùng nhớ động (heap / 힙) thuộc tính (property / 속성) mà còn ở bất biến giữa **kích thước lô-gic (logic / 논리)** và **kích thước vật lý** của vùng nhớ động (heap / 힙).

> **Chuyển mạch:** Trong **Vùng nhớ vùng nhớ động (heap / 힙) nâng cao và kỹ thuật hàng đợi ưu tiên**, **17. Hàng đợi ưu tiên đồng thời** tiếp nhận điểm tựa từ **16. Hai vùng nhớ động (heap / 힙) cho median động** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **18. External-memory Priority hàng đợi (queue / 큐)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 17. Hàng đợi ưu tiên đồng thời

Một vùng nhớ động (heap / 힙) có một gốc (root / 루트) nóng; nhiều luồng cùng insert/extract có thể tranh chấp khóa mạnh. Vì vậy concurrent priority hàng đợi (queue / 큐) khó mở rộng hơn hàng đợi (queue / 큐) FIFO phân vùng tốt.

Các thiết kế có thể dùng nhiều vùng nhớ động (heap / 힙) con, skip-list có thứ tự, relaxed priority hàng đợi (queue / 큐) hoặc multi-queue: mỗi thao tác chọn ngẫu nhiên vài hàng đợi (queue / 큐) và thao tác trên một hàng đợi (queue / 큐) phù hợp.

Đổi lại, một số thiết kế chấp nhận **relaxed thứ tự (ordering / 순서)**: phần tử lấy ra gần nhỏ nhất chứ không tuyệt đối nhỏ nhất. Nếu ứng dụng cho phép, relaxation có thể cải thiện scalability đáng kể.

> **Chuyển mạch:** Ở chặng này của **Vùng nhớ vùng nhớ động (heap / 힙) nâng cao và kỹ thuật hàng đợi ưu tiên**, **18. External-memory Priority hàng đợi (queue / 큐)** tiếp nhận điểm tựa từ **17. Hàng đợi ưu tiên đồng thời** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **19. Kiểm thử vùng nhớ động (heap / 힙) nâng cao** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 18. External-memory Priority hàng đợi (queue / 큐)

Khi hàng đợi ưu tiên vượt RAM, số I/O theo khối trở thành mô hình chi phí quan trọng. vùng nhớ động (heap / 힙) nhị phân đơn giản có thể gây nhiều truy cập ngẫu nhiên.

Các cấu trúc ưu tiên cho bên ngoài (external / 외부) bộ nhớ (memory / 메모리) cố batch insert, buffer cập nhật (update / 업데이트) và hợp nhất các run để giảm số khối (block / 블록) transfer. Đây là cùng tư duy với B-Tree và bên ngoài (external / 외부) merge sort: tối ưu **di chuyển dữ liệu**, không chỉ số phép so sánh.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Vùng nhớ vùng nhớ động (heap / 힙) nâng cao và kỹ thuật hàng đợi ưu tiên**, **19. Kiểm thử vùng nhớ động (heap / 힙) nâng cao** tiếp nhận điểm tựa từ **18. External-memory Priority hàng đợi (queue / 큐)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **20. Chọn vùng nhớ động (heap / 힙) theo tải công việc** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 19. Kiểm thử vùng nhớ động (heap / 힙) nâng cao

Ngoài kiểm thử (test / 테스트) `extract` ra thứ tự tăng dần, cần kiểm tra bất biến sau chuỗi thao tác ngẫu nhiên.

Với indexed vùng nhớ động (heap / 힙):

```text
heap[position[id]] == id
```

Với hai vùng nhớ động (heap / 힙) median:

```text
max(lower) <= min(upper)
kích thước logic cân bằng
median khớp với mảng tham chiếu đã sắp xếp
```

Với meldable vùng nhớ động (heap / 힙), có thể tạo nhiều vùng nhớ động (heap / 힙) nhỏ, meld theo thứ tự ngẫu nhiên rồi so toàn bộ chuỗi extract với một multiset tham chiếu.

Property-based testing rất phù hợp vì lỗi vùng nhớ động (heap / 힙) thường chỉ xuất hiện sau một chuỗi cập nhật (update / 업데이트) đặc biệt.

> **Chuyển mạch:** Trong **Vùng nhớ vùng nhớ động (heap / 힙) nâng cao và kỹ thuật hàng đợi ưu tiên**, **20. Chọn vùng nhớ động (heap / 힙) theo tải công việc** tiếp nhận điểm tựa từ **19. Kiểm thử vùng nhớ động (heap / 힙) nâng cao** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Mô hình tư duy** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 20. Chọn vùng nhớ động (heap / 힙) theo tải công việc

Phần này chuyển khái niệm Computer Science thành cấu trúc, ví dụ hoặc quy trình có thể kiểm tra. Hãy xác định câu hỏi mà mục trả lời rồi nối kết luận với phần kế tiếp.

| Tải công việc | Ứng viên thường hợp lý |
|---|---|
| General insert/extract | nhị phân (binary / 이진) vùng nhớ động (heap / 힙) |
| Nhiều decrease-key | Indexed vùng nhớ động (heap / 힙), D-ary vùng nhớ động (heap / 힙), Pairing vùng nhớ động (heap / 힙) |
| Meld thường xuyên | Binomial/Pairing/Leftist/Skew vùng nhớ động (heap / 힙) |
| Lý thuyết decrease-key tối ưu | Fibonacci vùng nhớ động (heap / 힙) |
| Khóa nguyên đơn điệu | Dial / Radix vùng nhớ động (heap / 힙) |
| Top-K streaming | Bounded nhị phân (binary / 이진) vùng nhớ động (heap / 힙) |
| Median động | Two Heaps |
| Concurrent, chấp nhận gần đúng | Multi-queue / relaxed PQ |
| Dữ liệu vượt RAM | External-memory PQ |

Bảng này là điểm xuất phát, không phải luật tuyệt đối. Constant factor, bộ nhớ đệm (cache / 캐시), độ phức tạp hiện thực (implementation / 구현) và ngữ nghĩa (semantics / 의미론) của API vẫn phải được đo.

> **Chuyển mạch:** Ở chặng này của **Vùng nhớ vùng nhớ động (heap / 힙) nâng cao và kỹ thuật hàng đợi ưu tiên**, **Mô hình tư duy** gom các mảnh từ **20. Chọn vùng nhớ động (heap / 힙) theo tải công việc** thành một kết luận có thể mang sang phần kế tiếp. Phần còn lại của file dùng kết quả này để khép lại mạch giải thích.

## Mô hình tư duy

> vùng nhớ động (heap / 힙) không phải một cấu trúc duy nhất mà là **một họ cách biểu diễn thứ tự bộ phận**. Chọn đúng biến thể nghĩa là hiểu thao tác nào thật sự đắt trong tải công việc của mình.

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

> **Bàn giao:** Sau **Mô hình tư duy**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](../README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
