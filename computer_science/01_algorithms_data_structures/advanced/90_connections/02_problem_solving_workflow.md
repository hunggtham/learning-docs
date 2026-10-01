# Quy trình giải bài DSA và thiết kế thuật toán

> **Mạch đọc:** [README](../README.md) là bản đồ owner của **Quy trình giải bài DSA và thiết kế thuật toán**; nhìn vào vị trí đó trước để biết file này đang phục vụ nhánh kiến thức nào. **1. Đọc đề như một specification** mở đối tượng chính của file và câu hỏi cần theo dõi; sau đó sang **2. Viết lại bài toán bằng một câu** để mở rộng đối tượng sang phạm vi kế cận. Cách đi này giữ lại điểm tựa của section đầu và cho biết kết luận sẽ được dùng ở đâu, thay vì dừng ở định nghĩa đầu tiên.

**Problem-Solving Workflow / 문제 해결 흐름**

Giải một bài DSA tốt không bắt đầu bằng việc cố nhớ “mẫu nào giống LeetCode”, mà bắt đầu bằng **đặc tả đúng vấn đề**, xây mô hình đúng, tìm một baseline đúng, rồi loại bỏ dần những phần công việc không cần thiết.

Một lời giải đáng tin thường có bốn lớp:

```text
mô hình trạng thái đúng
cách biểu diễn đúng
bất biến / chứng minh đúng
mô hình chi phí phù hợp
```

Nếu một trong bốn lớp sai, mã (code / 코드) có thể vẫn chạy trên mẫu (sample / 표본) nhưng lời giải không bền vững.

## 1. Đọc đề như một specification

Trước khi mã (code / 코드), phải xác định:

```text
input domain
output semantics
preconditions
constraints
edge cases
error behavior
```

Các từ rất giống nhau có thể tạo bài khác hoàn toàn:

```text
subarray      -> liên tiếp
subsequence   -> giữ thứ tự nhưng không cần liên tiếp
subset        -> không quan tâm vị trí
path          -> chuỗi đỉnh/cạnh hợp lệ
simple path   -> không lặp đỉnh
walk          -> có thể lặp
```

Nếu terminology chưa rõ, thuật toán chưa thể bắt đầu chắc chắn.

> **Chuyển mạch:** Specification làm rõ input/output và invariant; viết lại bài toán thành một câu, rồi tách story khỏi computational model để chọn cấu trúc dữ liệu và proof obligation đúng.

## 2. Viết lại bài toán bằng một câu

Một kỹ thuật đơn giản nhưng mạnh:

> “Tôi cần tìm/đếm/tối ưu **X**, sao cho **Y**, dưới các ràng buộc **Z**.”

Ví dụ:

> “Tìm chi phí nhỏ nhất để đi từ `s` tới `t`, với trọng số cạnh không âm.”

Câu này ngay lập tức làm lộ lĩnh vực (domain / 도메인) thích hợp cho Dijkstra.

Nếu chưa viết được bài toán bằng câu ngắn, story tầng (layer / 계층) vẫn đang che mô hình thật.

> **Chuyển mạch:** Ở chặng này của **Quy trình giải bài DSA và thiết kế thuật toán**, **3. Tách story khỏi computational mô hình (model / 모델)** tiếp nhận điểm tựa từ **2. Viết lại bài toán bằng một câu** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **4. Ràng buộc là ngân sách độ phức tạp (complexity / 복잡도)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 3. Tách story khỏi computational mô hình (model / 모델)

“Thành phố” có thể là đỉnh. “Chuyến bay” là cạnh. “Khóa và cửa” có thể biến trạng thái thành `(position,keyMask)`. “Booking” là interval. “Undo” là ngăn xếp (stack / 스택). “Mạng lưới phụ thuộc” là DAG.

Story chỉ là tên gọi. Thuật toán làm việc trên cấu trúc toán học bên dưới.

Một thuật toán đúng trên mô hình sai vẫn giải sai vấn đề.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Quy trình giải bài DSA và thiết kế thuật toán**, **4. Ràng buộc là ngân sách độ phức tạp (complexity / 복잡도)** tiếp nhận điểm tựa từ **3. Tách story khỏi computational mô hình (model / 모델)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **5. Đừng chỉ nhìn n; tìm mọi tham số** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 4. Ràng buộc là ngân sách độ phức tạp (complexity / 복잡도)

Hãy chuyển các ràng buộc (constraints / 제약조건들) thành quy mô công việc (work / 작업) sơ bộ.

```text
n <= 20         -> 2^n có thể khả thi
n ~ 10^3        -> n^2 có thể khả thi
n ~ 10^5        -> thường cần n log n hoặc n
n ~ 10^6        -> memory/allocation cũng thành vấn đề lớn
Q ~ 10^5        -> preprocessing/index có thể rất đáng
```

Đây chỉ là heuristic, không phải luật cứng. thời gian chạy (runtime / 런타임), constant factor và thời gian (time / 시간) limit vẫn quan trọng.

Nhưng các ràng buộc (constraints / 제약조건들) giúp loại nhanh những ý tưởng bất khả thi.

> **Chuyển mạch:** Trong **Quy trình giải bài DSA và thiết kế thuật toán**, **5. Đừng chỉ nhìn n; tìm mọi tham số** tiếp nhận điểm tựa từ **4. Ràng buộc là ngân sách độ phức tạp (complexity / 복잡도)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **6. Tìm baseline đúng trước** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 5. Đừng chỉ nhìn n; tìm mọi tham số

Đồ thị (graph / 그래프) có `V` và `E`. String matching có `n` và `m`. Top-K có `n` và `k`. Knapsack có `n` và `W`.

Một độ phức tạp (complexity / 복잡도) như:

\[
O(n\log k)
\]

có thể tốt hơn nhiều `O(n log n)` khi `k` nhỏ.

Giữ tham số riêng giúp thấy cấu trúc (structure / 구조) mà việc ép tất cả thành một `n` sẽ che mất.

> **Chuyển mạch:** Ở chặng này của **Quy trình giải bài DSA và thiết kế thuật toán**, **6. Tìm baseline đúng trước** tiếp nhận điểm tựa từ **5. Đừng chỉ nhìn n; tìm mọi tham số** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **7. Hỏi: “Tôi đang tính lại cái gì?”** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 6. Tìm baseline đúng trước

Brute force không phải đáp án “ngu ngốc”; nó là **đặc tả có thể chạy được**.

Baseline giúp:

```text
xác nhận hiểu đề
làm oracle cho test nhỏ
cho thấy work nào đang bị lặp
```

Two Sum `O(n²)` làm lộ rằng inner vòng lặp (loop / 루프) chỉ đang hỏi “complement đã xuất hiện chưa?”, từ đó băm (hash / 해시) Set loại quét lặp.

Phạm vi (range / 범위) Sum brute force làm lộ rằng cùng prefix bị cộng lại nhiều lần, dẫn tới Prefix Sum.

Memoization làm lộ rằng nhiều nhánh recursion đang tính lại cùng trạng thái (state / 상태).

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Quy trình giải bài DSA và thiết kế thuật toán**, **7. Hỏi: “Tôi đang tính lại cái gì?”** tiếp nhận điểm tựa từ **6. Tìm baseline đúng trước** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **8. Thiết kế trạng thái (state / 상태)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 7. Hỏi: “Tôi đang tính lại cái gì?”

Đây là câu hỏi tối ưu hóa quan trọng nhất.

Các dạng lặp lại phổ biến:

```text
quét lại cùng prefix
so lại cùng pair
tính lại cùng state
sort lại dữ liệu đã có thứ tự
lookup tuyến tính lặp lại
recompute aggregate sau mỗi update
```

Cấu trúc (structure / 구조) thường xuất hiện để **materialize một summary** giúp tránh recomputation.

> **Chuyển mạch:** Trong **Quy trình giải bài DSA và thiết kế thuật toán**, **8. Thiết kế trạng thái (state / 상태)** tiếp nhận điểm tựa từ **7. Hỏi: “Tôi đang tính lại cái gì?”** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **9. Nhận diện trạng thái (state / 상태) explosion** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 8. Thiết kế trạng thái (state / 상태)

Một trạng thái (state / 상태) tốt phải đủ thông tin để tương lai được xác định, nhưng không giữ lịch sử thừa.

Ví dụ grid có key/door:

```text
(row, col)              -> thiếu
(row, col, keyMask)     -> đủ hơn
```

Nếu hai lịch sử khác nhau dẫn tới cùng trạng thái (state / 상태) và từ đó mọi hành động (action / 동작)/chi phí (cost / 비용) tương lai tương đương, ta có thể gộp chúng.

Đây là nền tảng của memoization, DP và state-space đồ thị (graph / 그래프).

> **Chuyển mạch:** Ở chặng này của **Quy trình giải bài DSA và thiết kế thuật toán**, **9. Nhận diện trạng thái (state / 상태) explosion** tiếp nhận điểm tựa từ **8. Thiết kế trạng thái (state / 상태)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **10. Dense hay Sparse trạng thái (state / 상태)?** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 9. Nhận diện trạng thái (state / 상태) explosion

Nếu trạng thái (state / 상태) có nhiều chiều:

```text
position × mask × time × resource
```

không gian có thể tăng theo tích các miền.

Trước khi mã (code / 코드), ước lượng số trạng thái (state / 상태) tối đa.

```text
n * 2^k
n * m * k
V * stops
```

Một DP chuyển tiếp (transition / 전이) `O(1)` vẫn vô dụng nếu số trạng thái (state / 상태) là `10^12`.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Quy trình giải bài DSA và thiết kế thuật toán**, **10. Dense hay Sparse trạng thái (state / 상태)?** tiếp nhận điểm tựa từ **9. Nhận diện trạng thái (state / 상태) explosion** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **11. Chọn biểu diễn (representation / 표현) trước thuật toán chi tiết** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 10. Dense hay Sparse trạng thái (state / 상태)?

Nếu phần lớn trạng thái (state / 상태) có thể xuất hiện, array/bảng (table / 테이블) dense thường nhanh và bộ nhớ (memory / 메모리) predictable.

Nếu chỉ một phần rất nhỏ reachable, băm (hash / 해시) Map/Set có thể tiết kiệm bộ nhớ (memory / 메모리) dù lookup đắt hơn.

Đừng chỉ hỏi “DP array hay map”; hãy hỏi density của reachable trạng thái (state / 상태).

> **Chuyển mạch:** Trong **Quy trình giải bài DSA và thiết kế thuật toán**, **11. Chọn biểu diễn (representation / 표현) trước thuật toán chi tiết** tiếp nhận điểm tựa từ **10. Dense hay Sparse trạng thái (state / 상태)?** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **12. Viết bất biến (invariant / 불변식) trước vòng lặp (loop / 루프) phức tạp** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 11. Chọn biểu diễn (representation / 표현) trước thuật toán chi tiết

Đồ thị (graph / 그래프) sparse:

```text
adjacency list
```

Đồ thị (graph / 그래프) dense hoặc cần edge lookup nhanh:

```text
adjacency matrix
```

Key integer dense:

```text
array
```

Key sparse/string:

```text
Hash Map
```

Biểu diễn (representation / 표현) quyết định chi phí (cost / 비용) của thao tác (operation / 연산) tiếp theo.

> **Chuyển mạch:** Ở chặng này của **Quy trình giải bài DSA và thiết kế thuật toán**, **12. Viết bất biến (invariant / 불변식) trước vòng lặp (loop / 루프) phức tạp** tiếp nhận điểm tựa từ **11. Chọn biểu diễn (representation / 표현) trước thuật toán chi tiết** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **13. bất biến (invariant / 불변식) cần đủ mạnh** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 12. Viết bất biến (invariant / 불변식) trước vòng lặp (loop / 루프) phức tạp

Nếu không thể nói vòng lặp (loop / 루프) đang bảo vệ điều gì, mã (code / 코드) rất dễ biến thành trial-and-error.

Tìm kiếm nhị phân (binary search / 이진 탐색):

> nếu answer tồn tại, nó vẫn nằm trong vùng ứng viên hiện tại.

Sliding cửa sổ (window / 윈도우):

> cửa sổ hiện tại luôn thỏa ràng buộc (constraint / 제약조건); left là ranh giới nhỏ nhất/lớn nhất theo bất biến (invariant / 불변식) đã chọn.

Monotonic deque:

> deque chứa đúng candidate chưa hết hạn, theo thứ tự giá trị đơn điệu.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Quy trình giải bài DSA và thiết kế thuật toán**, **13. bất biến (invariant / 불변식) cần đủ mạnh** tiếp nhận điểm tựa từ **12. Viết bất biến (invariant / 불변식) trước vòng lặp (loop / 루프) phức tạp** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **14. Tách tính đúng đắn (correctness / 정확성) và độ phức tạp (complexity / 복잡도)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 13. bất biến (invariant / 불변식) cần đủ mạnh

“Inorder prefix đã sorted” chưa đủ chứng minh sorting nếu không đảm bảo các phần tử không bị mất hoặc nhân đôi.

Một bất biến (invariant / 불변식) tốt thường gồm:

```text
shape/order property
membership/conservation property
candidate completeness
```

Nó phải đủ mạnh để kết hợp với điều kiện dừng suy ra postcondition.

> **Chuyển mạch:** Trong **Quy trình giải bài DSA và thiết kế thuật toán**, **14. Tách tính đúng đắn (correctness / 정확성) và độ phức tạp (complexity / 복잡도)** tiếp nhận điểm tựa từ **13. bất biến (invariant / 불변식) cần đủ mạnh** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **15. mẫu (pattern / 패턴) chứng minh** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 14. Tách tính đúng đắn (correctness / 정확성) và độ phức tạp (complexity / 복잡도)

Tính đúng đắn (correctness / 정확성) trả lời:

```text
vì sao answer đúng?
```

Độ phức tạp (complexity / 복잡도) trả lời:

```text
phải làm bao nhiêu work và dùng bao nhiêu memory?
```

Một thuật toán có thể đúng nhưng quá chậm; hoặc nhanh nhưng sai.

Đừng dùng “Big-O tốt” như bằng chứng đúng đắn.

> **Chuyển mạch:** Ở chặng này của **Quy trình giải bài DSA và thiết kế thuật toán**, **15. mẫu (pattern / 패턴) chứng minh** tiếp nhận điểm tựa từ **14. Tách tính đúng đắn (correctness / 정확성) và độ phức tạp (complexity / 복잡도)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **16. Khi baseline O(n²), thử những câu hỏi nào?** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 15. mẫu (pattern / 패턴) chứng minh

Các mẫu (pattern / 패턴) phổ biến:

```text
loop invariant
structural induction
strong induction
exchange argument
greedy stays-ahead
cut/cycle property
contradiction
optimal substructure
residual/certificate proof
```

Nhận diện mẫu (pattern / 패턴) chứng minh thường quan trọng hơn nhận diện tên thuật toán.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Quy trình giải bài DSA và thiết kế thuật toán**, **16. Khi baseline O(n²), thử những câu hỏi nào?** tiếp nhận điểm tựa từ **15. mẫu (pattern / 패턴) chứng minh** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **17. Khi recursion exponential, thử gì?** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 16. Khi baseline O(n²), thử những câu hỏi nào?

Nếu đang xét mọi cặp:

```text
sort có tạo monotonic order không?
hash có thay inner scan bằng lookup không?
two pointers có loại cả vùng candidate không?
prefix/difference có tái sử dụng aggregate không?
sweep line có biến pair interaction thành event stream không?
```

Không có một mẹo duy nhất; mục tiêu là tìm **thông tin nào giúp loại nhiều ứng viên cùng lúc**.

> **Chuyển mạch:** Trong **Quy trình giải bài DSA và thiết kế thuật toán**, **17. Khi recursion exponential, thử gì?** tiếp nhận điểm tựa từ **16. Khi baseline O(n²), thử những câu hỏi nào?** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **18. Khi có nhiều truy vấn (query / 쿼리)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 17. Khi recursion exponential, thử gì?

Phần này chuyển khái niệm Computer Science thành cấu trúc, ví dụ hoặc quy trình có thể kiểm tra. Hãy xác định câu hỏi mà mục trả lời rồi nối kết luận với phần kế tiếp.

```text
có overlapping states không?        -> memoization / DP
có branch vô ích nhận ra sớm không? -> pruning
có bound tốt không?                 -> branch-and-bound
có symmetry không?                  -> canonicalization
n có ~40 không?                     -> meet-in-the-middle
parameter nhỏ không?                -> FPT / bitmask DP
```

Cây tìm kiếm lớn thường được giảm bằng cách hợp nhất trạng thái (state / 상태) hoặc loại nhánh.

> **Chuyển mạch:** Ở chặng này của **Quy trình giải bài DSA và thiết kế thuật toán**, **18. Khi có nhiều truy vấn (query / 쿼리)** tiếp nhận điểm tựa từ **17. Khi recursion exponential, thử gì?** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **19. Khi vừa cập nhật (update / 업데이트) vừa truy vấn (query / 쿼리)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 18. Khi có nhiều truy vấn (query / 쿼리)

Một truy vấn (query / 쿼리) duy nhất có thể quét thẳng. `10^5` truy vấn (query / 쿼리) trên cùng dữ liệu (data / 데이터) thường đáng để preprocess.

```text
sorting
prefix sum
index
Sparse Table
binary lifting
suffix array
```

Hãy so:

\[
C_{bản dựng (build / 빌드)}+Q\cdot C_{truy vấn (query / 쿼리)}
\]

với cách không tiền xử lý.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Quy trình giải bài DSA và thiết kế thuật toán**, **19. Khi vừa cập nhật (update / 업데이트) vừa truy vấn (query / 쿼리)** tiếp nhận điểm tựa từ **18. Khi có nhiều truy vấn (query / 쿼리)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **20. Chú ý mục tiêu (objective / 목표) thay đổi thuật toán** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 19. Khi vừa cập nhật (update / 업데이트) vừa truy vấn (query / 쿼리)

Nếu prefix sum bị phá bởi cập nhật (update / 업데이트), chuyển sang cấu trúc (structure / 구조) động như Fenwick/Segment cây (tree / 트리).

Nếu sorted array bị phá bởi insert/delete thường xuyên, chuyển sang balanced cây (tree / 트리) hoặc cấu trúc (structure / 구조) khác.

Cập nhật (update / 업데이트)/truy vấn (query / 쿼리) sự đánh đổi (trade-off / 트레이드오프) chính là lý do nhiều dữ liệu (data / 데이터) structures tồn tại.

> **Chuyển mạch:** Trong **Quy trình giải bài DSA và thiết kế thuật toán**, **20. Chú ý mục tiêu (objective / 목표) thay đổi thuật toán** tiếp nhận điểm tựa từ **19. Khi vừa cập nhật (update / 업데이트) vừa truy vấn (query / 쿼리)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **21. trường hợp biên (edge case / 경계 사례) phải sinh từ giả định (assumption / 가정)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 20. Chú ý mục tiêu (objective / 목표) thay đổi thuật toán

Cùng dữ liệu interval:

```text
max số interval không overlap   -> greedy
tối đa tổng trọng số            -> DP
minimum rooms                   -> sweep/heap
union length                    -> merge/sweep
```

Đừng nhận diện thuật toán chỉ từ “dữ liệu là interval”. mục tiêu (objective / 목표) quyết định cấu trúc (structure / 구조) lập luận (reasoning / 추론).

> **Chuyển mạch:** Ở chặng này của **Quy trình giải bài DSA và thiết kế thuật toán**, **20. Chú ý mục tiêu (objective / 목표) thay đổi thuật toán** cho ta quy tắc; **21. trường hợp biên (edge case / 경계 사례) phải sinh từ giả định (assumption / 가정)** đặt quy tắc ấy vào tình huống cụ thể để thấy nó hoạt động đến đâu. Từ đây, **22. Integer Overflow** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 21. trường hợp biên (edge case / 경계 사례) phải sinh từ giả định (assumption / 가정)

Nếu Dijkstra yêu cầu non-negative weight, kiểm thử (test / 테스트) cạnh âm.

Nếu tìm kiếm nhị phân (binary search / 이진 탐색) yêu cầu sorted array, kiểm thử (test / 테스트) duplicates/boundaries.

Nếu comparator yêu cầu transitive, kiểm thử (test / 테스트) equal/tie cases.

Nếu recursion độ sâu (depth / 깊이) có thể `n`, kiểm thử (test / 테스트) skewed cây (tree / 트리)/đường dẫn (path / 경로) đồ thị (graph / 그래프).

Edge cases tốt nhất xuất phát từ **điều kiện mà proof sử dụng**.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Quy trình giải bài DSA và thiết kế thuật toán**, **21. trường hợp biên (edge case / 경계 사례) phải sinh từ giả định (assumption / 가정)** cho ta quy tắc; **22. Integer Overflow** đặt quy tắc ấy vào tình huống cụ thể để thấy nó hoạt động đến đâu. Từ đây, **23. Floating điểm (point / 지점)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 22. Integer Overflow

Một thuật toán đúng trên số nguyên toán học có thể sai trong machine integer.

```java
mid = (lo + hi) / 2
```

có thể overflow với integer hữu hạn; mẫu an toàn hơn:

```java
mid = lo + (hi - lo) / 2
```

Distance, prefix sum, count và multiplication phải được bound trước khi chọn kiểu số.

> **Chuyển mạch:** Trong **Quy trình giải bài DSA và thiết kế thuật toán**, **22. Integer Overflow** xác định đầu vào; **23. Floating điểm (point / 지점)** giải thích bước vận hành tạo ra kết quả kế tiếp. Từ đây, **24. Language-Specific rà soát (review / 검토)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 23. Floating điểm (point / 지점)

Nếu comparator dùng epsilon thiếu nhất quán, có thể phá transitivity và làm sort/cây (tree / 트리) sai.

Hình học (geometry / 기하학) predicate gần 0 có thể đổi dấu do rounding.

Numeric ngữ nghĩa (semantics / 의미론) là một phần của specification.

> **Chuyển mạch:** Ở chặng này của **Quy trình giải bài DSA và thiết kế thuật toán**, **24. Language-Specific rà soát (review / 검토)** tiếp nhận điểm tựa từ **23. Floating điểm (point / 지점)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **25. Dry-Run như một trạng thái (state / 상태) dấu vết (trace / 추적)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 24. Language-Specific rà soát (review / 검토)

### C

Phần này chuyển khái niệm Computer Science thành cấu trúc, ví dụ hoặc quy trình có thể kiểm tra. Hãy xác định câu hỏi mà mục trả lời rồi nối kết luận với phần kế tiếp.

```text
bounds
ownership
allocation failure
integer overflow
undefined behavior
pointer invalidation
```

### Java

Trước khi đọc đoạn triển khai, hãy giữ invariant và complexity mà thuật toán phải bảo toàn. Code bên dưới là một cách hiện thực hóa; cần đối chiếu output, ownership và edge case với mô hình vừa học.

```text
boxing
equals/hashCode
Comparator
mutable key
StackOverflowError
GC/allocation
```

### JavaScript

Trước khi đọc đoạn triển khai, hãy giữ invariant và complexity mà thuật toán phải bảo toàn. Code bên dưới là một cách hiện thực hóa; cần đối chiếu output, ownership và edge case với mô hình vừa học.

```text
Number safe integer
bitwise 32-bit coercion
Array.shift cost
Map object identity
sort comparator
UTF-16 semantics
```

Một thuật toán trừu tượng đúng vẫn cần hiện thực (implementation / 구현) phù hợp ngôn ngữ.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Quy trình giải bài DSA và thiết kế thuật toán**, **25. Dry-Run như một trạng thái (state / 상태) dấu vết (trace / 추적)** tiếp nhận điểm tựa từ **24. Language-Specific rà soát (review / 검토)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **26. kiểm thử (test / 테스트) Oracle** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 25. Dry-Run như một trạng thái (state / 상태) dấu vết (trace / 추적)

Đừng chỉ đọc mã (code / 코드) bằng mắt. Tạo đầu vào (input / 입력) nhỏ nhưng khó chịu và ghi:

```text
lo/hi/mid
stack/queue content
heap
visited
DP states
parent links
window boundaries
```

Mỗi chuyển tiếp (transition / 전이) phải giải thích được bằng bất biến (invariant / 불변식).

Nếu một biến cập nhật mà không biết nó bảo vệ tính chất nào, đó là dấu hiệu thiết kế chưa rõ.

> **Chuyển mạch:** Trong **Quy trình giải bài DSA và thiết kế thuật toán**, **26. kiểm thử (test / 테스트) Oracle** tiếp nhận điểm tựa từ **25. Dry-Run như một trạng thái (state / 상태) dấu vết (trace / 추적)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **27. Property-Based Testing** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 26. kiểm thử (test / 테스트) Oracle

Với đầu vào (input / 입력) nhỏ, dùng giải pháp chậm nhưng rõ ràng làm oracle.

```text
Dijkstra       vs Floyd-Warshall
Segment Tree   vs array scan
Top-K          vs full sort
MST            vs brute force nhỏ
custom map     vs standard map
```

Differential testing bắt hiện thực (implementation / 구현) bug rất hiệu quả.

> **Chuyển mạch:** Ở chặng này của **Quy trình giải bài DSA và thiết kế thuật toán**, **27. Property-Based Testing** tiếp nhận điểm tựa từ **26. kiểm thử (test / 테스트) Oracle** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **28. Adversarial kiểm thử (test / 테스트)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 27. Property-Based Testing

Thay vì chỉ kiểm thử (test / 테스트) đầu ra (output / 출력) cụ thể, kiểm thử (test / 테스트) tính chất:

```text
sort output ordered + same multiset
heap pop sequence nondecreasing
DSU union(a,b) => find(a)==find(b)
BFS dist[v] <= dist[u]+1 trên edge tree phù hợp
```

Tính chất thường gần proof hơn example kiểm thử (test / 테스트).

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Quy trình giải bài DSA và thiết kế thuật toán**, **28. Adversarial kiểm thử (test / 테스트)** tiếp nhận điểm tựa từ **27. Property-Based Testing** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **29. độ phức tạp (complexity / 복잡도) rà soát (review / 검토) toàn chuỗi xử lý (pipeline / 파이프라인)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 28. Adversarial kiểm thử (test / 테스트)

Random đầu vào (input / 입력) không thay thế đầu vào (input / 입력) bệnh lý.

```text
sorted/reverse/all equal
long collision chain
skewed tree
line graph
complete graph
large duplicate set
many equal event times
maximum recursion depth
```

Adversarial kiểm thử (test / 테스트) kiểm tra đúng nơi asymptotic hoặc bất biến (invariant / 불변식) dễ vỡ nhất.

> **Chuyển mạch:** Trong **Quy trình giải bài DSA và thiết kế thuật toán**, **28. Adversarial kiểm thử (test / 테스트)** xác định đầu vào; **29. độ phức tạp (complexity / 복잡도) rà soát (review / 검토) toàn chuỗi xử lý (pipeline / 파이프라인)** giải thích bước vận hành tạo ra kết quả kế tiếp. Từ đây, **30. không gian (space / 공간) rà soát (review / 검토)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 29. độ phức tạp (complexity / 복잡도) rà soát (review / 검토) toàn chuỗi xử lý (pipeline / 파이프라인)

Nếu preprocessing `O(n log n)` và mỗi truy vấn (query / 쿼리) `O(log n)`, với `Q` truy vấn (query / 쿼리):

\[
O(n\log n + Q\log n)
\]

Nếu helper bên trong vòng lặp (loop / 루프) là `O(n)`, phải tính nó vào tổng.

Nếu `sort()` được gọi trong mỗi iteration, độ phức tạp (complexity / 복잡도) có thể lớn hơn trực giác rất nhiều.

Không chỉ phân tích “cốt lõi (core / 핵심) vòng lặp (loop / 루프)”.

> **Chuyển mạch:** Ở chặng này của **Quy trình giải bài DSA và thiết kế thuật toán**, **29. độ phức tạp (complexity / 복잡도) rà soát (review / 검토) toàn chuỗi xử lý (pipeline / 파이프라인)** xác định đầu vào; **30. không gian (space / 공간) rà soát (review / 검토)** giải thích bước vận hành tạo ra kết quả kế tiếp. Từ đây, **31. đầu ra (output / 출력) kích thước (size / 크기) Lower Bound** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 30. không gian (space / 공간) rà soát (review / 검토)

Tính cả:

```text
input copy
aux arrays
hash-table slack
object overhead
recursion stack
memo table
adjacency edges
```

`O(n)` bộ nhớ (memory / 메모리) có thể vẫn vượt limit vì hệ số lớn.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Quy trình giải bài DSA và thiết kế thuật toán**, **31. đầu ra (output / 출력) kích thước (size / 크기) Lower Bound** tiếp nhận điểm tựa từ **30. không gian (space / 공간) rà soát (review / 검토)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **32. Stop tối ưu hóa (optimization / 최적화) khi đủ** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 31. đầu ra (output / 출력) kích thước (size / 크기) Lower Bound

Nếu phải xuất `k` kết quả, độ phức tạp (complexity / 복잡도) ít nhất `Ω(k)`.

Không thể yêu cầu liệt kê một triệu occurrence trong `O(log n)` chỉ vì chỉ mục (index / 인덱스) tìm kiếm (search / 검색) nhanh.

Luôn tách:

```text
cost tìm vùng kết quả
cost materialize output
```

> **Chuyển mạch:** Trong **Quy trình giải bài DSA và thiết kế thuật toán**, **32. Stop tối ưu hóa (optimization / 최적화) khi đủ** tiếp nhận điểm tựa từ **31. đầu ra (output / 출력) kích thước (size / 크기) Lower Bound** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **33. Profile trước Micro-Optimization** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 32. Stop tối ưu hóa (optimization / 최적화) khi đủ

Nếu ràng buộc (constraint / 제약조건) cho phép `O(n²)` an toàn và solution đơn giản, đôi khi đó là lựa chọn tốt hơn một cấu trúc (structure / 구조) rất phức tạp.

Độ phức tạp mã (code / 코드) tạo bug và maintenance chi phí (cost / 비용).

Mục tiêu là **đủ tốt với proof rõ**, không phải luôn dùng thuật toán mạnh nhất biết được.

> **Chuyển mạch:** Ở chặng này của **Quy trình giải bài DSA và thiết kế thuật toán**, **33. Profile trước Micro-Optimization** tiếp nhận điểm tựa từ **32. Stop tối ưu hóa (optimization / 최적화) khi đủ** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **34. Từ Interview Solution tới môi trường vận hành (production / 운영 환경)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 33. Profile trước Micro-Optimization

Sau khi asymptotic đã phù hợp, profiling mới trả lời bottleneck thật nằm ở:

```text
allocation
hashing
comparator
cache miss
GC
I/O
network
```

Đừng thay HashMap bằng custom cấu trúc (structure / 구조) chỉ từ trực giác nếu đường dẫn (path / 경로) đó chỉ chiếm 1% thời gian chạy (runtime / 런타임).

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Quy trình giải bài DSA và thiết kế thuật toán**, **34. Từ Interview Solution tới môi trường vận hành (production / 운영 환경)** tiếp nhận điểm tựa từ **33. Profile trước Micro-Optimization** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **35. Viết Solution ghi chú (note / 노트) sau khi giải** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 34. Từ Interview Solution tới môi trường vận hành (production / 운영 환경)

Một solution algorithmic đúng còn cần:

```text
input validation
resource limits
observability
error handling
concurrency semantics
serialization/versioning
backpressure
failure recovery
```

Môi trường vận hành (production / 운영 환경) hardening không thay đổi proof lõi nhưng mở rộng đặc tả hợp đồng (contract / 계약) của hệ thống.

> **Chuyển mạch:** Trong **Quy trình giải bài DSA và thiết kế thuật toán**, **35. Viết Solution ghi chú (note / 노트) sau khi giải** tiếp nhận điểm tựa từ **34. Từ Interview Solution tới môi trường vận hành (production / 운영 환경)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **36. Postmortem khi sai** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 35. Viết Solution ghi chú (note / 노트) sau khi giải

Một ghi chú tốt nên trả lời:

```text
mô hình bài toán
baseline
bottleneck của baseline
insight tối ưu
invariant/proof
complexity
edge cases
implementation caveats
alternative approaches
```

Cách này biến một bài giải đơn lẻ thành kiến thức tái sử dụng.

> **Chuyển mạch:** Ở chặng này của **Quy trình giải bài DSA và thiết kế thuật toán**, **36. Postmortem khi sai** tiếp nhận điểm tựa từ **35. Viết Solution ghi chú (note / 노트) sau khi giải** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **37. Một quy trình 12 bước** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 36. Postmortem khi sai

Không chỉ sửa dòng mã (code / 코드). Hãy phân loại lỗi:

```text
mô hình sai
state thiếu
invariant sai
boundary sai
complexity sai
integer/precision sai
representation sai
implementation bug
```

Phân loại đúng giúp tránh lặp lại cùng kiểu lỗi ở bài khác.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Quy trình giải bài DSA và thiết kế thuật toán**, **36. Postmortem khi sai** xác định đầu vào; **37. Một quy trình 12 bước** giải thích bước vận hành tạo ra kết quả kế tiếp. Từ đây, **38. Checklist trước khi nộp hoặc merge** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 37. Một quy trình 12 bước

Phần này chuyển khái niệm Computer Science thành cấu trúc, ví dụ hoặc quy trình có thể kiểm tra. Hãy xác định câu hỏi mà mục trả lời rồi nối kết luận với phần kế tiếp.

```text
1. Viết lại specification.
2. Xác định mọi constraint và parameter.
3. Bỏ story, dựng computational model.
4. Viết baseline đúng.
5. Xác định work bị lặp hoặc candidate thừa.
6. Thiết kế state tối thiểu đủ thông tin.
7. Chọn representation phù hợp.
8. Viết invariant/proof sketch.
9. Tính time + space toàn pipeline.
10. Test bằng oracle + adversarial cases.
11. Profile nếu cần tối ưu thực tế.
12. Ghi lại insight, không chỉ code.
```

> **Chuyển mạch:** Trong **Quy trình giải bài DSA và thiết kế thuật toán**, **37. Một quy trình 12 bước** xác định đầu vào; **38. Checklist trước khi nộp hoặc merge** giải thích bước vận hành tạo ra kết quả kế tiếp. Từ đây, **Mô hình tư duy** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 38. Checklist trước khi nộp hoặc merge

Phần này kiểm tra ranh giới và failure mode của cơ chế vừa học. Hãy dùng nó để biết khi nào mô hình còn đúng, khi nào cần đổi chiến lược và bằng chứng nào phải thu thập.

```text
Output semantics có đúng mọi case không?
Có dùng giả định nào đề không bảo đảm không?
Invariant có được giữ sau mọi update không?
Termination có chắc chắn không?
Complexity có tính helper/API ẩn không?
Kiểu số có đủ không?
Recursion depth an toàn không?
Có mutation/invalidation ngoài ý muốn không?
Test adversarial đã có chưa?
Có cách oracle nhỏ để đối chiếu không?
```

> **Chuyển mạch:** Ở chặng này của **Quy trình giải bài DSA và thiết kế thuật toán**, **Mô hình tư duy** gom các mảnh từ **38. Checklist trước khi nộp hoặc merge** thành một kết luận có thể mang sang phần kế tiếp. Phần còn lại của file dùng kết quả này để khép lại mạch giải thích.

## Mô hình tư duy

> Giải DSA là quá trình **giảm không gian bất định**: specification xác định câu hỏi, mô hình (model / 모델) xác định trạng thái (state / 상태), bất biến (invariant / 불변식) loại bỏ trạng thái sai, cấu trúc dữ liệu (data structure / 자료구조) lưu thông tin hữu ích, còn thuật toán quyết định thứ tự khai thác thông tin đó.

Khi bí, đừng hỏi “mẫu này dùng thuật toán gì?”. Hãy quay lại hỏi: **baseline đang làm thừa công việc nào, trạng thái (state / 상태) nào thực sự ảnh hưởng tương lai, bất biến (invariant / 불변식) nào cho phép bỏ candidate, và cấu trúc (structure / 구조) nào materialize thông tin đó rẻ nhất?**

Xem thêm: [Problem Modeling](../00_foundations/00_dsa_as_problem_modeling.md), [Correctness & Invariants](../00_foundations/01_algorithm_correctness_and_invariants.md), [Complexity](../00_foundations/02_complexity_analysis.md), [Choose the Right Data Structure](./00_choose_the_right_data_structure.md), [Cross-Language Testing](../80_language_implementations/03_cross_language_testing_and_benchmarking.md).

> **Bàn giao:** Sau **Mô hình tư duy**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](../README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
