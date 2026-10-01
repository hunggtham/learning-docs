# Hai con trỏ, cửa sổ trượt, tổng tiền tố và kỹ thuật hiệu

> **Mạch đọc:** [README](../README.md) là bản đồ owner của **Hai con trỏ, cửa sổ trượt, tổng tiền tố và kỹ thuật hiệu**; nhìn vào vị trí đó trước để biết file này đang phục vụ nhánh kiến thức nào. **1. Hai con trỏ trên dữ liệu đã sắp xếp** gom dữ liệu hoặc nguồn để kiểm tra một nhận định cụ thể; sau đó sang **2. bất biến (invariant / 불변식) của Two Pointers** để chuyển câu hỏi ấy thành điều kiện phải giữ. Cách đi này giữ lại điểm tựa của section đầu và cho biết kết luận sẽ được dùng ở đâu, thay vì dừng ở định nghĩa đầu tiên.

**Two Pointers, Sliding cửa sổ (window / 윈도우), Prefix & Difference / 투 포인터, 슬라이딩 윈도우, 누적합, 차분**

Nhóm kỹ thuật này thường được học như nhiều “mẫu bài” khác nhau, nhưng chúng có một nguyên lý chung rất sâu:

> **Hai trạng thái lân cận thường giống nhau rất nhiều; đừng tính lại từ đầu nếu có thể cập nhật từ trạng thái trước.**

Hai con trỏ dùng thứ tự hoặc tính đơn điệu để loại cả một vùng ứng viên. Cửa sổ trượt tái sử dụng trạng thái khi hai biên dịch chuyển. Tổng tiền tố lưu trạng thái tích lũy để truy vấn đoạn thành phép hiệu. Mảng hiệu lưu **thay đổi tại ranh giới** thay vì cập nhật mọi phần tử trong đoạn.

Đây không phải bốn mẹo rời rạc; chúng là bốn cách khai thác **sự chồng lặp giữa các trạng thái liên tiếp**.

## 1. Hai con trỏ trên dữ liệu đã sắp xếp

Giả sử mảng tăng dần và cần tìm hai phần tử có tổng bằng `target`.

Đặt:

```text
L = 0
R = n - 1
```

Nếu:

\[
a[L]+a[R] < mục tiêu (target / 대상)
\]

thì tăng `L` là an toàn. Với `a[L]` hiện tại, mọi phần tử bên trái `R` đều không lớn hơn `a[R]`, nên ghép `a[L]` với chúng chỉ cho tổng còn nhỏ hơn.

Nếu tổng quá lớn, giảm `R` theo lập luận (reasoning / 추론) đối xứng.

Mỗi pointer chỉ di chuyển một chiều, nên quét là `O(n)` sau khi dữ liệu đã được sắp xếp.

> **Chuyển mạch:** Trong **Hai con trỏ, cửa sổ trượt, tổng tiền tố và kỹ thuật hiệu**, **1. Hai con trỏ trên dữ liệu đã sắp xếp** nêu điều cần giải thích; **2. bất biến (invariant / 불변식) của Two Pointers** đối chiếu nó với bằng chứng hoặc nguồn kiểm chứng. Từ đây, **3. Chi phí sorting phải được tính** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 2. bất biến (invariant / 불변식) của Two Pointers

Cách chứng minh tốt hơn việc nhớ “nếu nhỏ thì L++” là xác định vùng ứng viên còn lại.

Bất biến:

> Nếu có một cặp đáp án chưa được tìm thấy, ít nhất một cặp như vậy vẫn nằm trong hình chữ nhật chỉ số `[L,R]` hiện tại.

Mỗi lần tăng `L` hoặc giảm `R`, ta phải chứng minh toàn bộ các cặp bị loại không thể là đáp án.

Đây là dạng **candidate elimination** giống tìm kiếm nhị phân (binary search / 이진 탐색) nhưng thay vì loại nửa khoảng bằng một phép so sánh, ta loại một hàng/cột ứng viên nhờ monotonic thứ tự (order / 순서).

> **Chuyển mạch:** Ở chặng này của **Hai con trỏ, cửa sổ trượt, tổng tiền tố và kỹ thuật hiệu**, **3. Chi phí sorting phải được tính** tiếp nhận điểm tựa từ **2. bất biến (invariant / 불변식) của Two Pointers** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **4. Các dạng Two Pointers** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 3. Chi phí sorting phải được tính

Nếu đầu vào (input / 입력) chưa được sắp xếp và ta sort trước:

\[
O(n\log n)+O(n)=O(n\log n)
\]

Nếu cần giữ chỉ mục (index / 인덱스) gốc, mỗi phần tử phải mang theo original chỉ mục (index / 인덱스).

Với Two Sum một lần, băm (hash / 해시) Map expected `O(n)` có thể tốt hơn. Với nhiều truy vấn (query / 쿼리) trên cùng dữ liệu, sorting một lần có thể đáng giá hơn.

Luôn phân tích toàn chuỗi xử lý (pipeline / 파이프라인), không chỉ phase quét.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Hai con trỏ, cửa sổ trượt, tổng tiền tố và kỹ thuật hiệu**, **4. Các dạng Two Pointers** tiếp nhận điểm tựa từ **3. Chi phí sorting phải được tính** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **5. Read/ghi (write / 쓰기) Pointer** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 4. Các dạng Two Pointers

### Đối hướng

`L` từ đầu, `R` từ cuối.

Dùng cho:

```text
pair sum trên sorted array
palindrome
container/interval problems
partition theo điều kiện
```

### Cùng hướng

Hai pointer cùng tăng nhưng đại diện hai ranh giới khác nhau. Sliding cửa sổ (window / 윈도우) là dạng điển hình.

### Read/ghi (write / 쓰기)

Một pointer đọc, một pointer ghi đầu ra (output / 출력) compact tại chỗ.

### Fast/Slow

Hai pointer chạy tốc độ khác nhau trên linked cấu trúc (structure / 구조) hoặc chuỗi (sequence / 시퀀스) trạng thái.

Điểm chung là mỗi pointer có nghĩa trong một bất biến (invariant / 불변식) cụ thể.

> **Chuyển mạch:** Trong **Hai con trỏ, cửa sổ trượt, tổng tiền tố và kỹ thuật hiệu**, **5. Read/ghi (write / 쓰기) Pointer** tiếp nhận điểm tựa từ **4. Các dạng Two Pointers** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **6. Stable vs Unstable Compaction** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 5. Read/ghi (write / 쓰기) Pointer

Ví dụ loại duplicate khỏi sorted array:

```java
int write = 0;
for (int read = 0; read < a.length; read++) {
    if (read == 0 || a[read] != a[read - 1]) {
        a[write++] = a[read];
    }
}
```

Bất biến:

```text
[0, write) là output hợp lệ đã compact
[read, n) chưa xử lý
```

Mẫu (pattern / 패턴) này dùng cho filter-in-place, remove element, partition và stream compaction.

> **Chuyển mạch:** Ở chặng này của **Hai con trỏ, cửa sổ trượt, tổng tiền tố và kỹ thuật hiệu**, **6. Stable vs Unstable Compaction** tiếp nhận điểm tựa từ **5. Read/ghi (write / 쓰기) Pointer** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **7. Fast/Slow Pointer trên Linked danh sách (list / 목록)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 6. Stable vs Unstable Compaction

Read/ghi (write / 쓰기) pointer như trên giữ thứ tự tương đối của phần tử được giữ lại, tức là stable.

Nếu không cần giữ thứ tự (order / 순서), có thể swap phần tử cần xóa với phần tử cuối và giảm kích thước lô-gic (logic / 논리); cách này giảm số lần dịch nhưng thay đổi thứ tự (order / 순서).

Yêu cầu ổn định là một phần của đầu ra (output / 출력) ngữ nghĩa (semantics / 의미론), không phải chỉ hiện thực (implementation / 구현) detail.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Hai con trỏ, cửa sổ trượt, tổng tiền tố và kỹ thuật hiệu**, **7. Fast/Slow Pointer trên Linked danh sách (list / 목록)** tiếp nhận điểm tựa từ **6. Stable vs Unstable Compaction** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **8. Vì sao Floyd gặp nhau?** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 7. Fast/Slow Pointer trên Linked danh sách (list / 목록)

Floyd cycle detection:

```text
slow += 1 bước
fast += 2 bước
```

Nếu có chu trình, hai pointer cuối cùng gặp nhau. Nếu không, `fast` chạm null.

Tìm middle nút (node / 노드) cũng dùng fast/slow: khi fast đi hết, slow ở gần giữa.

Ở linked danh sách (list / 목록) không có random truy cập (access / 접근), quan hệ (relation / 관계) về tốc độ thay thế arithmetic chỉ mục (index / 인덱스).

> **Chuyển mạch:** Trong **Hai con trỏ, cửa sổ trượt, tổng tiền tố và kỹ thuật hiệu**, **8. Vì sao Floyd gặp nhau?** tiếp nhận điểm tựa từ **7. Fast/Slow Pointer trên Linked danh sách (list / 목록)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **9. Tìm điểm bắt đầu chu trình** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 8. Vì sao Floyd gặp nhau?

Sau khi cả hai vào chu trình, xét vị trí modulo độ dài chu trình `C`.

Mỗi bước, khoảng cách tương đối giữa fast và slow tăng 1 modulo `C`.

Do đó sau tối đa `C` bước, khoảng cách trở thành 0 và hai pointer gặp nhau.

Đây là một chứng minh dùng modular arithmetic chứ không phải “fast chắc chắn đuổi kịp slow” theo trực giác mơ hồ.

> **Chuyển mạch:** Ở chặng này của **Hai con trỏ, cửa sổ trượt, tổng tiền tố và kỹ thuật hiệu**, **9. Tìm điểm bắt đầu chu trình** tiếp nhận điểm tựa từ **8. Vì sao Floyd gặp nhau?** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **10. Fixed-Size Sliding cửa sổ (window / 윈도우)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 9. Tìm điểm bắt đầu chu trình

Sau khi fast và slow gặp nhau, đặt một pointer về head rồi cho cả hai đi 1 bước mỗi lần. Điểm gặp tiếp theo là đầu chu trình.

Kết quả này đến từ quan hệ giữa:

```text
độ dài đoạn trước chu trình
số vòng fast đã đi thêm
vị trí gặp modulo cycle length
```

Đây là ví dụ nơi hiểu đại số giúp nhớ thuật toán tốt hơn học thuộc bước.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Hai con trỏ, cửa sổ trượt, tổng tiền tố và kỹ thuật hiệu**, **10. Fixed-Size Sliding cửa sổ (window / 윈도우)** tiếp nhận điểm tựa từ **9. Tìm điểm bắt đầu chu trình** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **11. Variable-Size Sliding cửa sổ (window / 윈도우)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 10. Fixed-Size Sliding cửa sổ (window / 윈도우)

Giả sử cần tổng lớn nhất của subarray dài `k`.

Naive: tính lại từng cửa sổ (window / 윈도우) `O(k)`, tổng `O(nk)`.

Nếu sum hiện tại là `S`, dịch một bước:

\[
S' = S-a[L]+a[R+1]
\]

Sau initial `O(k)`, mỗi shift `O(1)`, tổng `O(n)`.

Cửa sổ trượt chính là **incremental maintenance** của summary.

> **Chuyển mạch:** Trong **Hai con trỏ, cửa sổ trượt, tổng tiền tố và kỹ thuật hiệu**, **11. Variable-Size Sliding cửa sổ (window / 윈도우)** tiếp nhận điểm tựa từ **10. Fixed-Size Sliding cửa sổ (window / 윈도우)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **12. Sliding cửa sổ (window / 윈도우) cần tính đơn điệu của tính hợp lệ** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 11. Variable-Size Sliding cửa sổ (window / 윈도우)

Một mẫu (pattern / 패턴) điển hình:

```text
for R từ trái sang phải:
    thêm a[R] vào state
    while window không hợp lệ:
        bỏ a[L]
        L++
    cập nhật answer
```

Nếu `L` và `R` chỉ tăng, mỗi phần tử vào cửa sổ (window / 윈도우) một lần và rời một lần.

Do đó ngay cả có `while` lồng trong `for`, tổng số bước dịch pointer vẫn `O(n)`.

Đây là amortized lập luận (reasoning / 추론).

> **Chuyển mạch:** Ở chặng này của **Hai con trỏ, cửa sổ trượt, tổng tiền tố và kỹ thuật hiệu**, **12. Sliding cửa sổ (window / 윈도우) cần tính đơn điệu của tính hợp lệ** tiếp nhận điểm tựa từ **11. Variable-Size Sliding cửa sổ (window / 윈도우)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **13. Vì sao số âm phá mẫu (pattern / 패턴) sum đơn giản?** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 12. Sliding cửa sổ (window / 윈도우) cần tính đơn điệu của tính hợp lệ

Ví dụ mảng số dương, tìm longest subarray có sum `<= K`.

Khi tăng `R`, sum không giảm. Khi tăng `L`, sum không tăng.

Predicate “sum <= K” có quan hệ monotonic với hai biên, nên có thể shrink `L` cho tới khi cửa sổ (window / 윈도우) hợp lệ trở lại.

Đây là điều kiện bản chất; cú pháp (syntax / 문법) hai pointer chỉ là biểu hiện bên ngoài.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Hai con trỏ, cửa sổ trượt, tổng tiền tố và kỹ thuật hiệu**, **13. Vì sao số âm phá mẫu (pattern / 패턴) sum đơn giản?** tiếp nhận điểm tựa từ **12. Sliding cửa sổ (window / 윈도우) cần tính đơn điệu của tính hợp lệ** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **14. cửa sổ (window / 윈도우) trạng thái (state / 상태) có thể phức tạp hơn Sum** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 13. Vì sao số âm phá mẫu (pattern / 패턴) sum đơn giản?

Nếu có số âm:

```text
mở rộng R có thể làm sum giảm
bỏ a[L] âm có thể làm sum tăng
```

Tính đơn điệu biến mất. Việc “sum > K thì L++” không còn an toàn.

Khi đó có thể cần:

```text
prefix sum + Hash Map
prefix sum + monotonic deque
balanced tree
binary search trên prefix theo structure đặc biệt
```

Đừng dùng sliding cửa sổ (window / 윈도우) chỉ vì bài hỏi subarray.

> **Chuyển mạch:** Trong **Hai con trỏ, cửa sổ trượt, tổng tiền tố và kỹ thuật hiệu**, **14. cửa sổ (window / 윈도우) trạng thái (state / 상태) có thể phức tạp hơn Sum** tiếp nhận điểm tựa từ **13. Vì sao số âm phá mẫu (pattern / 패턴) sum đơn giản?** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **15. Longest Substring Without Repeating Characters** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 14. cửa sổ (window / 윈도우) trạng thái (state / 상태) có thể phức tạp hơn Sum

Trạng thái (state / 상태) có thể là:

```text
frequency map
count distinct
number of violations
sum
max/min qua monotonic deque
multiset/order-statistic structure
```

Điều kiện quan trọng là có thể cập nhật khi add/remove endpoint đủ rẻ.

Nếu mỗi add/remove là `O(1)` expected và hai biên đơn điệu, tổng vẫn thường `O(n)`.

> **Chuyển mạch:** Ở chặng này của **Hai con trỏ, cửa sổ trượt, tổng tiền tố và kỹ thuật hiệu**, **15. Longest Substring Without Repeating Characters** tiếp nhận điểm tựa từ **14. cửa sổ (window / 윈도우) trạng thái (state / 상태) có thể phức tạp hơn Sum** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **16. Minimum cửa sổ (window / 윈도우) Substring** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 15. Longest Substring Without Repeating Characters

Trạng thái (state / 상태) có thể dùng:

```text
frequency map
hoặc lastSeen[char]
```

Nếu dùng `lastSeen`, khi gặp ký tự đã xuất hiện trong cửa sổ (window / 윈도우):

```text
L = max(L, lastSeen[c] + 1)
```

Ta nhảy `L` trực tiếp thay vì tăng từng bước.

Đây là ví dụ summary mạnh hơn có thể giảm số cập nhật (update / 업데이트) trạng thái (state / 상태) dù asymptotic vẫn `O(n)`.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Hai con trỏ, cửa sổ trượt, tổng tiền tố và kỹ thuật hiệu**, **16. Minimum cửa sổ (window / 윈도우) Substring** tiếp nhận điểm tựa từ **15. Longest Substring Without Repeating Characters** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **17. At-Most → Exactly** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 16. Minimum cửa sổ (window / 윈도우) Substring

Cần duy trì số lượng từng ký tự yêu cầu.

Mẫu (pattern / 패턴):

1. mở rộng phải cho đến khi đủ yêu cầu (requirement / 요구사항);
2. shrink trái tối đa trong khi vẫn đủ;
3. cập nhật minimum;
4. tiếp tục mở rộng.

Một biến `formed` hoặc số yêu cầu (requirement / 요구사항) đã thỏa giúp tránh quét toàn frequency map sau mỗi thay đổi.

Bản chất là giữ một predicate “cửa sổ (window / 윈도우) covers mục tiêu (target / 대상) multiset”.

> **Chuyển mạch:** Trong **Hai con trỏ, cửa sổ trượt, tổng tiền tố và kỹ thuật hiệu**, **17. At-Most → Exactly** tiếp nhận điểm tựa từ **16. Minimum cửa sổ (window / 윈도우) Substring** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **18. Counting Windows: tại sao cộng R-L+1?** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 17. At-Most → Exactly

Một kỹ thuật rất mạnh:

\[
count(exactly\ K)=count(atMost\ K)-count(atMost\ K-1)
\]

Nếu `atMost(K)` có sliding-window solution đơn điệu, ta suy ra exact-K count.

Ứng dụng:

```text
subarray có đúng K distinct values
binary subarray với sum đúng K trong một số formulation
```

Đây là phép biến đổi từ ràng buộc (constraint / 제약조건) chính xác khó thành hai ràng buộc (constraint / 제약조건) tích lũy dễ hơn.

> **Chuyển mạch:** Ở chặng này của **Hai con trỏ, cửa sổ trượt, tổng tiền tố và kỹ thuật hiệu**, **18. Counting Windows: tại sao cộng R-L+1?** tiếp nhận điểm tựa từ **17. At-Most → Exactly** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **19. Sliding cửa sổ (window / 윈도우) Maximum cần Deque đơn điệu** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 18. Counting Windows: tại sao cộng `R-L+1`?

Nếu sau khi shrink, `[L,R]` là cửa sổ (window / 윈도우) hợp lệ nhỏ nhất theo một bất biến (invariant / 불변식) kiểu “at most K”, thì mọi suffix của nó kết thúc tại `R`:

```text
[L,R], [L+1,R], ..., [R,R]
```

đều hợp lệ trong nhiều bài at-most.

Số cửa sổ (window / 윈도우) kết thúc tại `R` là:

\[
R-L+1
\]

Hiểu lý do combinatorial này tốt hơn học công thức thuộc lòng.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Hai con trỏ, cửa sổ trượt, tổng tiền tố và kỹ thuật hiệu**, **19. Sliding cửa sổ (window / 윈도우) Maximum cần Deque đơn điệu** tiếp nhận điểm tựa từ **18. Counting Windows: tại sao cộng R-L+1?** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **20. Median trong Sliding cửa sổ (window / 윈도우)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 19. Sliding cửa sổ (window / 윈도우) Maximum cần Deque đơn điệu

Nếu cần max của mỗi cửa sổ (window / 윈도우), recompute max `O(k)` quá đắt.

Deque giữ chỉ mục (index / 인덱스) sao cho:

```text
index tăng
value giảm
```

Khi thêm phần tử mới, loại khỏi cuối mọi candidate nhỏ hơn hoặc bằng vì chúng bị dominated: cũ hơn và không lớn hơn.

Front luôn là max hiện tại.

Mỗi chỉ mục (index / 인덱스) vào/ra deque tối đa một lần, nên `O(n)`.

> **Chuyển mạch:** Trong **Hai con trỏ, cửa sổ trượt, tổng tiền tố và kỹ thuật hiệu**, **20. Median trong Sliding cửa sổ (window / 윈도우)** tiếp nhận điểm tựa từ **19. Sliding cửa sổ (window / 윈도우) Maximum cần Deque đơn điệu** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **21. Prefix Sum** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 20. Median trong Sliding cửa sổ (window / 윈도우)

Median khó hơn max vì không có một extreme duy nhất.

Có thể dùng:

```text
two heaps + delayed deletion
balanced multiset
order-statistic tree
Fenwick trên compressed values nếu domain phù hợp
```

Đây là ví dụ cùng “cửa sổ (window / 윈도우)” nhưng truy vấn (query / 쿼리) summary khác làm cấu trúc phụ thay đổi hoàn toàn.

> **Chuyển mạch:** Ở chặng này của **Hai con trỏ, cửa sổ trượt, tổng tiền tố và kỹ thuật hiệu**, **21. Prefix Sum** tiếp nhận điểm tựa từ **20. Median trong Sliding cửa sổ (window / 윈도우)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **22. Prefix Technique dựa trên phép nghịch đảo** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 21. Prefix Sum

Quy ước nửa mở:

```text
P[0] = 0
P[i+1] = P[i] + a[i]
```

Khi đó:

\[
sum([L,R))=P[R]-P[L]
\]

Preprocessing `O(n)`, truy vấn (query / 쿼리) `O(1)`.

Prefix array là biểu diễn (representation / 표현) của **trạng thái tích lũy sau mỗi prefix**.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Hai con trỏ, cửa sổ trượt, tổng tiền tố và kỹ thuật hiệu**, **22. Prefix Technique dựa trên phép nghịch đảo** tiếp nhận điểm tựa từ **21. Prefix Sum** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **23. Prefix Frequency** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 22. Prefix Technique dựa trên phép nghịch đảo

Sum có inverse là subtraction:

\[
P[R]-P[L]
\]

XOR tự nghịch đảo:

\[
rangeXor=P[R]\oplus P[L]
\]

Nhưng `min` không có inverse tương tự; không thể lấy phạm vi (range / 범위) min bằng hiệu hai prefix minimum.

Hiểu tính chất đại số giúp biết khi nào prefix truy vấn (query / 쿼리) `O(1)` khả thi.

> **Chuyển mạch:** Trong **Hai con trỏ, cửa sổ trượt, tổng tiền tố và kỹ thuật hiệu**, **23. Prefix Frequency** tiếp nhận điểm tựa từ **22. Prefix Technique dựa trên phép nghịch đảo** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **24. Prefix Sum + băm (hash / 해시) Map cho Subarray Sum K** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 23. Prefix Frequency

Với alphabet nhỏ:

```text
pref[i][c] = số lần c trong prefix length i
```

Frequency của `c` trong `[L,R)`:

```text
pref[R][c] - pref[L][c]
```

Sự đánh đổi (trade-off / 트레이드오프):

```text
memory O(nσ)
query histogram nhanh
```

Kỹ thuật này rất hữu ích cho string/phạm vi (range / 범위) counting khi `σ` nhỏ.

> **Chuyển mạch:** Ở chặng này của **Hai con trỏ, cửa sổ trượt, tổng tiền tố và kỹ thuật hiệu**, **24. Prefix Sum + băm (hash / 해시) Map cho Subarray Sum K** tiếp nhận điểm tựa từ **23. Prefix Frequency** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **25. Longest Subarray với Sum K** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 24. Prefix Sum + băm (hash / 해시) Map cho Subarray Sum K

Nếu:

\[
P[i]-P[j]=K
\]

thì:

\[
P[j]=P[i]-K
\]

Khi quét `P[i]`, chỉ cần đếm số prefix trước bằng `P[i]-K`.

Băm (hash / 해시) Map lưu:

```text
prefixValue -> frequency đã thấy
```

Expected `O(n)` kể cả đầu vào (input / 입력) có số âm.

Đây là một mẫu (pattern / 패턴) cực quan trọng: biến subarray thành **quan hệ giữa hai prefix states**.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Hai con trỏ, cửa sổ trượt, tổng tiền tố và kỹ thuật hiệu**, **25. Longest Subarray với Sum K** tiếp nhận điểm tựa từ **24. Prefix Sum + băm (hash / 해시) Map cho Subarray Sum K** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **26. Prefix Minimum và Maximum Subarray** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 25. Longest Subarray với Sum K

Nếu cần độ dài lớn nhất, lưu **vị trí đầu tiên** của mỗi prefix sum.

Khi tại `i` có `P[i]-K` từng xuất hiện ở `j`, subarray `(j,i]` có sum K. Để maximize length, giữ earliest `j`.

Cùng equation nhưng siêu dữ liệu (metadata / 메타데이터) trong băm (hash / 해시) Map thay đổi theo mục tiêu (objective / 목표):

```text
count -> frequency
longest -> earliest index
shortest -> latest index hoặc cấu trúc khác tùy bài
```

> **Chuyển mạch:** Trong **Hai con trỏ, cửa sổ trượt, tổng tiền tố và kỹ thuật hiệu**, **26. Prefix Minimum và Maximum Subarray** tiếp nhận điểm tựa từ **25. Longest Subarray với Sum K** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **27. Kadane dưới góc nhìn Incremental trạng thái (state / 상태)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 26. Prefix Minimum và Maximum Subarray

Maximum subarray sum có thể nhìn qua prefix:

\[
P[R]-\min_{L<R}P[L]
\]

Khi quét `R`, chỉ cần giữ minimum prefix trước đó.

Đây là ví dụ prefix summary vẫn hữu ích dù `min` không invertible cho arbitrary phạm vi (range / 범위) truy vấn (query / 쿼리).

> **Chuyển mạch:** Ở chặng này của **Hai con trỏ, cửa sổ trượt, tổng tiền tố và kỹ thuật hiệu**, **27. Kadane dưới góc nhìn Incremental trạng thái (state / 상태)** tiếp nhận điểm tựa từ **26. Prefix Minimum và Maximum Subarray** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **28. 2D Prefix Sum** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 27. Kadane dưới góc nhìn Incremental trạng thái (state / 상태)

Kadane giữ:

```text
bestEndingHere
bestOverall
```

Mỗi bước quyết định:

```text
bắt đầu subarray mới tại i
hoặc
nối a[i] vào subarray trước
```

Kadane và prefix-min là hai cách nhìn cùng cấu trúc tối ưu hóa.

Việc liên hệ hai formulation giúp hiểu thuật toán thay vì học tên riêng.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Hai con trỏ, cửa sổ trượt, tổng tiền tố và kỹ thuật hiệu**, **28. 2D Prefix Sum** tiếp nhận điểm tựa từ **27. Kadane dưới góc nhìn Incremental trạng thái (state / 상태)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **29. Higher-Dimensional Prefix** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 28. 2D Prefix Sum

Với ma trận và prefix rectangle nửa mở:

\[
P[r][c]=sum([0,r)\times[0,c))
\]

Truy vấn (query / 쿼리) rectangle:

\[
P[r2][c2]-P[r1][c2]-P[r2][c1]+P[r1][c1]
\]

Đây là inclusion-exclusion: trừ hai vùng thừa và cộng lại vùng bị trừ hai lần.

> **Chuyển mạch:** Trong **Hai con trỏ, cửa sổ trượt, tổng tiền tố và kỹ thuật hiệu**, **29. Higher-Dimensional Prefix** tiếp nhận điểm tựa từ **28. 2D Prefix Sum** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **30. Difference Array** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 29. Higher-Dimensional Prefix

Ý tưởng mở rộng lên 3D hoặc nhiều chiều bằng inclusion-exclusion trên các mặt/cạnh/góc.

Nhưng số term tăng theo `2^d`, nên practical chủ yếu khi số chiều nhỏ.

Đây là ví dụ độ phức tạp (complexity / 복잡도) phụ thuộc **số chiều**, không chỉ số phần tử.

> **Chuyển mạch:** Ở chặng này của **Hai con trỏ, cửa sổ trượt, tổng tiền tố và kỹ thuật hiệu**, **30. Difference Array** tiếp nhận điểm tựa từ **29. Higher-Dimensional Prefix** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **31. Difference Array như sự kiện (event / 이벤트) Encoding** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 30. Difference Array

Difference biểu diễn (representation / 표현) lưu:

\[
d[i]=a[i]-a[i-1]
\]

với quy ước thích hợp.

Phạm vi (range / 범위) add `x` vào `[L,R]`:

```text
diff[L] += x
diff[R+1] -= x
```

Sau mọi cập nhật (update / 업데이트), prefix sum của `diff` khôi phục giá trị cuối.

Ta chuyển `O(length)` công việc (work / 작업) của mỗi phạm vi (range / 범위) cập nhật (update / 업데이트) thành hai ranh giới (boundary / 경계) updates.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Hai con trỏ, cửa sổ trượt, tổng tiền tố và kỹ thuật hiệu**, **31. Difference Array như sự kiện (event / 이벤트) Encoding** tiếp nhận điểm tựa từ **30. Difference Array** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **32. 2D Difference** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 31. Difference Array như sự kiện (event / 이벤트) Encoding

`+x` tại `L` nghĩa “bắt đầu hiệu lực”. `-x` sau `R` nghĩa “kết thúc hiệu lực”.

Do đó difference array chính là một sweep-line sự kiện (event / 이벤트) biểu diễn (representation / 표현) trên miền tọa độ nhỏ/rời rạc.

Prefix sum là bước tích phân các thay đổi đó.

> **Chuyển mạch:** Trong **Hai con trỏ, cửa sổ trượt, tổng tiền tố và kỹ thuật hiệu**, **32. 2D Difference** tiếp nhận điểm tựa từ **31. Difference Array như sự kiện (event / 이벤트) Encoding** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **33. Prefix và Difference là hai cách biểu diễn đối ngẫu** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 32. 2D Difference

Muốn cộng `x` vào rectangle, cập nhật bốn corner của difference ma trận (matrix / 행렬) theo inclusion-exclusion. Sau đó prefix 2D tái dựng toàn ma trận.

Kỹ thuật này rất mạnh khi có nhiều rectangle updates nhưng chỉ cần materialize kết quả cuối một lần.

Nếu xen kẽ cập nhật (update / 업데이트)/truy vấn (query / 쿼리) online, cần Fenwick/Segment cây (tree / 트리) 2D hoặc cấu trúc (structure / 구조) khác.

> **Chuyển mạch:** Ở chặng này của **Hai con trỏ, cửa sổ trượt, tổng tiền tố và kỹ thuật hiệu**, **33. Prefix và Difference là hai cách biểu diễn đối ngẫu** tiếp nhận điểm tựa từ **32. 2D Difference** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **34. Imos phương thức (method / 메서드)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 33. Prefix và Difference là hai cách biểu diễn đối ngẫu

Prefix lưu **trạng thái tích lũy**.

Difference lưu **sự thay đổi giữa các trạng thái kế tiếp**.

```text
difference --prefix sum--> original
original   --difference--> differences
```

Một bên tối ưu truy vấn (query / 쿼리) aggregate, bên kia tối ưu phạm vi (range / 범위) cập nhật (update / 업데이트) offline.

Hiểu mối quan hệ này giúp nhớ kỹ thuật một cách tự nhiên.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Hai con trỏ, cửa sổ trượt, tổng tiền tố và kỹ thuật hiệu**, **34. Imos phương thức (method / 메서드)** tiếp nhận điểm tựa từ **33. Prefix và Difference là hai cách biểu diễn đối ngẫu** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **35. Circular cửa sổ (window / 윈도우)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 34. Imos phương thức (method / 메서드)

Trong một số tài liệu Nhật, difference + prefix cho phạm vi (range / 범위) coverage được gọi là Imos phương thức (method / 메서드).

Ví dụ nhiều đoạn tô màu trên timeline:

```text
+1 tại start
-1 tại end
prefix -> số lớp phủ tại mỗi vị trí
```

Bản chất vẫn là sự kiện (event / 이벤트) accumulation.

> **Chuyển mạch:** Trong **Hai con trỏ, cửa sổ trượt, tổng tiền tố và kỹ thuật hiệu**, **35. Circular cửa sổ (window / 윈도우)** tiếp nhận điểm tựa từ **34. Imos phương thức (method / 메서드)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **36. Two Pointers trên Hai Mảng** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 35. Circular cửa sổ (window / 윈도우)

Với circular array, có thể:

```text
xử lý index modulo n
hoặc
conceptually concatenate array với chính nó
```

Nhưng phải giới hạn cửa sổ (window / 윈도우) length không vượt `n` nếu bài chỉ cho mỗi phần tử xuất hiện một vòng.

Circularity thường làm ranh giới phức tạp hơn, không thay bản chất cửa sổ (window / 윈도우).

> **Chuyển mạch:** Ở chặng này của **Hai con trỏ, cửa sổ trượt, tổng tiền tố và kỹ thuật hiệu**, **36. Two Pointers trên Hai Mảng** tiếp nhận điểm tựa từ **35. Circular cửa sổ (window / 윈도우)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **37. K-Way Merge** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 36. Two Pointers trên Hai Mảng

Merge hai sorted arrays dùng pointer `i,j`.

Tìm intersection/union cũng vậy.

Mỗi pointer chỉ tăng, nên `O(n+m)`.

Đây là same-direction two pointers nhưng trên hai chuỗi (sequence / 시퀀스) khác nhau.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Hai con trỏ, cửa sổ trượt, tổng tiền tố và kỹ thuật hiệu**, **37. K-Way Merge** tiếp nhận điểm tựa từ **36. Two Pointers trên Hai Mảng** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **38. tìm kiếm nhị phân (binary search / 이진 탐색) vs Two Pointers** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 37. K-Way Merge

Hai pointer tổng quát lên `k` sorted streams bằng min-heap giữ head hiện tại của mỗi stream.

Độ phức tạp (complexity / 복잡도):

\[
O(N\log k)
\]

với `N` tổng số phần tử.

Đây là ví dụ “two pointers” mở rộng thành frontier có nhiều candidate, và vùng nhớ động (heap / 힙) trở thành cấu trúc (structure / 구조) chọn candidate nhỏ nhất tiếp theo.

> **Chuyển mạch:** Trong **Hai con trỏ, cửa sổ trượt, tổng tiền tố và kỹ thuật hiệu**, **38. tìm kiếm nhị phân (binary search / 이진 탐색) vs Two Pointers** tiếp nhận điểm tựa từ **37. K-Way Merge** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **39. Monotonicity là tín hiệu quan trọng** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 38. tìm kiếm nhị phân (binary search / 이진 탐색) vs Two Pointers

Nếu cần tìm pair cho một truy vấn (query / 쿼리), có thể với mỗi `i` binary-search complement `O(n log n)`. Two pointers exploit monotonic quan hệ (relation / 관계) giữa cả hai chỉ số để đạt `O(n)`.

Tìm kiếm nhị phân (binary search / 이진 탐색) loại ứng viên theo một chiều độc lập; two pointers khai thác quan hệ hai chiều mạnh hơn.

> **Chuyển mạch:** Ở chặng này của **Hai con trỏ, cửa sổ trượt, tổng tiền tố và kỹ thuật hiệu**, **39. Monotonicity là tín hiệu quan trọng** tiếp nhận điểm tựa từ **38. tìm kiếm nhị phân (binary search / 이진 탐색) vs Two Pointers** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **40. Offline truy vấn (query / 쿼리) và Prefix Precomputation** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 39. Monotonicity là tín hiệu quan trọng

Two pointers/sliding cửa sổ (window / 윈도우) thường xuất hiện khi có một predicate kiểu:

```text
nếu tăng L thì property chỉ thay theo một hướng
nếu tăng R thì property chỉ thay theo một hướng
```

Nếu validity nhảy lên xuống không có cấu trúc, pointer monotonic không đủ.

Hãy tìm **đơn điệu của không gian ứng viên**, không tìm từ khóa (keyword / 키워드) “subarray”.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Hai con trỏ, cửa sổ trượt, tổng tiền tố và kỹ thuật hiệu**, **40. Offline truy vấn (query / 쿼리) và Prefix Precomputation** tiếp nhận điểm tựa từ **39. Monotonicity là tín hiệu quan trọng** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **41. Overflow** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 40. Offline truy vấn (query / 쿼리) và Prefix Precomputation

Nếu toàn bộ truy vấn (query / 쿼리) đã biết trước, có thể sort/reorder truy vấn (query / 쿼리) hoặc xây multiple prefix summaries.

Nếu truy vấn (query / 쿼리) đến online sau mỗi cập nhật (update / 업데이트), static prefix không đủ.

Tính online/offline là một chiều thiết kế quan trọng thường bị bỏ qua khi học kỹ thuật này.

> **Chuyển mạch:** Trong **Hai con trỏ, cửa sổ trượt, tổng tiền tố và kỹ thuật hiệu**, **40. Offline truy vấn (query / 쿼리) và Prefix Precomputation** xác định đầu vào; **41. Overflow** giải thích bước vận hành tạo ra kết quả kế tiếp. Từ đây, **42. bộ nhớ (memory / 메모리) sự đánh đổi (trade-off / 트레이드오프)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 41. Overflow

Prefix sum rất dễ overflow vì tích lũy nhiều phần tử.

Nếu `a[i]` là `int`, tổng có thể cần `long`.

2D prefix hoặc weighted count còn có thể cần kiểu rộng hơn do tích số lượng phần tử với magnitude.

Kiểu số phải chọn theo cận tổng, không theo cận của một phần tử.

> **Chuyển mạch:** Ở chặng này của **Hai con trỏ, cửa sổ trượt, tổng tiền tố và kỹ thuật hiệu**, **41. Overflow** xác định đầu vào; **42. bộ nhớ (memory / 메모리) sự đánh đổi (trade-off / 트레이드오프)** giải thích bước vận hành tạo ra kết quả kế tiếp. Từ đây, **43. Kiểm thử** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 42. bộ nhớ (memory / 메모리) sự đánh đổi (trade-off / 트레이드오프)

Prefix array dùng `O(n)` bộ nhớ (memory / 메모리). Nếu chỉ cần running prefix một lần, không cần lưu toàn bộ.

Nếu có nhiều loại truy vấn (query / 쿼리), có thể phải lưu nhiều prefix arrays, tăng bộ nhớ (memory / 메모리) nhanh.

Cấu trúc dữ liệu (data structure / 자료구조) thiết kế (design / 설계) luôn là sự đánh đổi (trade-off / 트레이드오프) giữa recomputation và materialized summaries.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Hai con trỏ, cửa sổ trượt, tổng tiền tố và kỹ thuật hiệu**, **43. Kiểm thử** tiếp nhận điểm tựa từ **42. bộ nhớ (memory / 메모리) sự đánh đổi (trade-off / 트레이드오프)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **44. Những hiểu lầm phổ biến** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 43. Kiểm thử

Các trường hợp (case / 사례) quan trọng:

```text
empty / one element
all equal
negative values
zeros
duplicates
K=0
window size 1 / n
prefix sum gần overflow
circular boundaries
Unicode nếu window trên string
```

Với cửa sổ (window / 윈도우), nên differential-test trên `n` nhỏ bằng brute-force enumerate mọi subarray.

> **Chuyển mạch:** Trong **Hai con trỏ, cửa sổ trượt, tổng tiền tố và kỹ thuật hiệu**, **44. Những hiểu lầm phổ biến** tiếp nhận điểm tựa từ **43. Kiểm thử** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Mô hình tư duy** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 44. Những hiểu lầm phổ biến

“Có subarray là dùng sliding cửa sổ (window / 윈도우)” — sai nếu validity không đơn điệu.

“Hai vòng while/for nghĩa O(n²)” — sai nếu pointer chỉ đi một chiều và mỗi phần tử bị xử lý hữu hạn lần.

“Prefix Sum chỉ dùng để tính tổng” — sai; có thể lưu count, XOR hoặc nhiều summary tích lũy.

“Difference Array dùng được cho cập nhật (update / 업데이트)/truy vấn (query / 쿼리) online bất kỳ” — sai; dạng đơn giản phù hợp batch updates rồi materialize.

“Two pointers luôn cần sorted array” — không; fast/slow, read/ghi (write / 쓰기) và variable cửa sổ (window / 윈도우) không nhất thiết cần sorting.

> **Chuyển mạch:** Ở chặng này của **Hai con trỏ, cửa sổ trượt, tổng tiền tố và kỹ thuật hiệu**, **Mô hình tư duy** gom các mảnh từ **44. Những hiểu lầm phổ biến** thành một kết luận có thể mang sang phần kế tiếp. Phần còn lại của file dùng kết quả này để khép lại mạch giải thích.

## Mô hình tư duy

> Hai con trỏ, cửa sổ trượt, prefix và difference đều là kỹ thuật **khai thác tính gần nhau của các trạng thái**. Một trạng thái mới không được tính từ đầu; nó được suy từ trạng thái trước bằng một thay đổi nhỏ hoặc bằng một dữ liệu tóm lược đã tiền xử lý.

Khi gặp bài chuỗi (sequence / 시퀀스)/phạm vi (range / 범위), hãy hỏi: **candidate không gian (space / 공간) có monotonic không, hai biên có thể chỉ di chuyển một chiều không, cửa sổ (window / 윈도우) trạng thái (state / 상태) có cập nhật nhanh khi add/remove không, aggregate có inverse không, và có thể lưu thay đổi ở ranh giới (boundary / 경계) thay vì cập nhật toàn đoạn không?**

Xem thêm: [Searching](./00_searching.md), [Intervals & Sweep Line](./08_intervals_and_sweep_line.md), [Range Queries](../05_specialized/01_range_queries_fenwick_segment_tree.md), [Monotonic Stack/Queue](../01_linear_structures/02_stacks.md), [Queues & Deques](../01_linear_structures/03_queues_deques_and_priority_queues.md).

> **Bàn giao:** Sau **Mô hình tư duy**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](../README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
