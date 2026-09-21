# Hai con trỏ, cửa sổ trượt, tổng tiền tố và kỹ thuật hiệu
**Two Pointers, Sliding Window, Prefix & Difference / 투 포인터, 슬라이딩 윈도우, 누적합, 차분**

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
a[L]+a[R] < target
\]

thì tăng `L` là an toàn. Với `a[L]` hiện tại, mọi phần tử bên trái `R` đều không lớn hơn `a[R]`, nên ghép `a[L]` với chúng chỉ cho tổng còn nhỏ hơn.

Nếu tổng quá lớn, giảm `R` theo reasoning đối xứng.

Mỗi pointer chỉ di chuyển một chiều, nên quét là `O(n)` sau khi dữ liệu đã được sắp xếp.

## 2. Invariant của Two Pointers

Cách chứng minh tốt hơn việc nhớ “nếu nhỏ thì L++” là xác định vùng ứng viên còn lại.

Bất biến:

> Nếu có một cặp đáp án chưa được tìm thấy, ít nhất một cặp như vậy vẫn nằm trong hình chữ nhật chỉ số `[L,R]` hiện tại.

Mỗi lần tăng `L` hoặc giảm `R`, ta phải chứng minh toàn bộ các cặp bị loại không thể là đáp án.

Đây là dạng **candidate elimination** giống binary search nhưng thay vì loại nửa khoảng bằng một phép so sánh, ta loại một hàng/cột ứng viên nhờ monotonic order.

## 3. Chi phí sorting phải được tính

Nếu input chưa được sắp xếp và ta sort trước:

\[
O(n\log n)+O(n)=O(n\log n)
\]

Nếu cần giữ index gốc, mỗi phần tử phải mang theo original index.

Với Two Sum một lần, Hash Map expected `O(n)` có thể tốt hơn. Với nhiều query trên cùng dữ liệu, sorting một lần có thể đáng giá hơn.

Luôn phân tích toàn pipeline, không chỉ phase quét.

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

Hai pointer cùng tăng nhưng đại diện hai ranh giới khác nhau. Sliding window là dạng điển hình.

### Read/Write

Một pointer đọc, một pointer ghi output compact tại chỗ.

### Fast/Slow

Hai pointer chạy tốc độ khác nhau trên linked structure hoặc sequence trạng thái.

Điểm chung là mỗi pointer có nghĩa trong một invariant cụ thể.

## 5. Read/Write Pointer

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

Pattern này dùng cho filter-in-place, remove element, partition và stream compaction.

## 6. Stable vs Unstable Compaction

Read/write pointer như trên giữ thứ tự tương đối của phần tử được giữ lại, tức là stable.

Nếu không cần giữ order, có thể swap phần tử cần xóa với phần tử cuối và giảm kích thước logic; cách này giảm số lần dịch nhưng thay đổi order.

Yêu cầu ổn định là một phần của output semantics, không phải chỉ implementation detail.

## 7. Fast/Slow Pointer trên Linked List

Floyd cycle detection:

```text
slow += 1 bước
fast += 2 bước
```

Nếu có chu trình, hai pointer cuối cùng gặp nhau. Nếu không, `fast` chạm null.

Tìm middle node cũng dùng fast/slow: khi fast đi hết, slow ở gần giữa.

Ở linked list không có random access, relation về tốc độ thay thế arithmetic index.

## 8. Vì sao Floyd gặp nhau?

Sau khi cả hai vào chu trình, xét vị trí modulo độ dài chu trình `C`.

Mỗi bước, khoảng cách tương đối giữa fast và slow tăng 1 modulo `C`.

Do đó sau tối đa `C` bước, khoảng cách trở thành 0 và hai pointer gặp nhau.

Đây là một chứng minh dùng modular arithmetic chứ không phải “fast chắc chắn đuổi kịp slow” theo trực giác mơ hồ.

## 9. Tìm điểm bắt đầu chu trình

Sau khi fast và slow gặp nhau, đặt một pointer về head rồi cho cả hai đi 1 bước mỗi lần. Điểm gặp tiếp theo là đầu chu trình.

Kết quả này đến từ quan hệ giữa:

```text
độ dài đoạn trước chu trình
số vòng fast đã đi thêm
vị trí gặp modulo cycle length
```

Đây là ví dụ nơi hiểu đại số giúp nhớ thuật toán tốt hơn học thuộc bước.

## 10. Fixed-Size Sliding Window

Giả sử cần tổng lớn nhất của subarray dài `k`.

Naive: tính lại từng window `O(k)`, tổng `O(nk)`.

Nếu sum hiện tại là `S`, dịch một bước:

\[
S' = S-a[L]+a[R+1]
\]

Sau initial `O(k)`, mỗi shift `O(1)`, tổng `O(n)`.

Cửa sổ trượt chính là **incremental maintenance** của summary.

## 11. Variable-Size Sliding Window

Một pattern điển hình:

```text
for R từ trái sang phải:
    thêm a[R] vào state
    while window không hợp lệ:
        bỏ a[L]
        L++
    cập nhật answer
```

Nếu `L` và `R` chỉ tăng, mỗi phần tử vào window một lần và rời một lần.

Do đó ngay cả có `while` lồng trong `for`, tổng số bước dịch pointer vẫn `O(n)`.

Đây là amortized reasoning.

## 12. Sliding Window cần tính đơn điệu của tính hợp lệ

Ví dụ mảng số dương, tìm longest subarray có sum `<= K`.

Khi tăng `R`, sum không giảm. Khi tăng `L`, sum không tăng.

Predicate “sum <= K” có quan hệ monotonic với hai biên, nên có thể shrink `L` cho tới khi window hợp lệ trở lại.

Đây là điều kiện bản chất; syntax hai pointer chỉ là biểu hiện bên ngoài.

## 13. Vì sao số âm phá pattern sum đơn giản?

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

Đừng dùng sliding window chỉ vì bài hỏi subarray.

## 14. Window State có thể phức tạp hơn Sum

State có thể là:

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

## 15. Longest Substring Without Repeating Characters

State có thể dùng:

```text
frequency map
hoặc lastSeen[char]
```

Nếu dùng `lastSeen`, khi gặp ký tự đã xuất hiện trong window:

```text
L = max(L, lastSeen[c] + 1)
```

Ta nhảy `L` trực tiếp thay vì tăng từng bước.

Đây là ví dụ summary mạnh hơn có thể giảm số update state dù asymptotic vẫn `O(n)`.

## 16. Minimum Window Substring

Cần duy trì số lượng từng ký tự yêu cầu.

Pattern:

1. mở rộng phải cho đến khi đủ requirement;
2. shrink trái tối đa trong khi vẫn đủ;
3. cập nhật minimum;
4. tiếp tục mở rộng.

Một biến `formed` hoặc số requirement đã thỏa giúp tránh quét toàn frequency map sau mỗi thay đổi.

Bản chất là giữ một predicate “window covers target multiset”.

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

Đây là phép biến đổi từ constraint chính xác khó thành hai constraint tích lũy dễ hơn.

## 18. Counting Windows: tại sao cộng `R-L+1`?

Nếu sau khi shrink, `[L,R]` là window hợp lệ nhỏ nhất theo một invariant kiểu “at most K”, thì mọi suffix của nó kết thúc tại `R`:

```text
[L,R], [L+1,R], ..., [R,R]
```

đều hợp lệ trong nhiều bài at-most.

Số window kết thúc tại `R` là:

\[
R-L+1
\]

Hiểu lý do combinatorial này tốt hơn học công thức thuộc lòng.

## 19. Sliding Window Maximum cần Deque đơn điệu

Nếu cần max của mỗi window, recompute max `O(k)` quá đắt.

Deque giữ index sao cho:

```text
index tăng
value giảm
```

Khi thêm phần tử mới, loại khỏi cuối mọi candidate nhỏ hơn hoặc bằng vì chúng bị dominated: cũ hơn và không lớn hơn.

Front luôn là max hiện tại.

Mỗi index vào/ra deque tối đa một lần, nên `O(n)`.

## 20. Median trong Sliding Window

Median khó hơn max vì không có một extreme duy nhất.

Có thể dùng:

```text
two heaps + delayed deletion
balanced multiset
order-statistic tree
Fenwick trên compressed values nếu domain phù hợp
```

Đây là ví dụ cùng “window” nhưng query summary khác làm cấu trúc phụ thay đổi hoàn toàn.

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

Preprocessing `O(n)`, query `O(1)`.

Prefix array là representation của **trạng thái tích lũy sau mỗi prefix**.

## 22. Prefix Technique dựa trên phép nghịch đảo

Sum có inverse là subtraction:

\[
P[R]-P[L]
\]

XOR tự nghịch đảo:

\[
rangeXor=P[R]\oplus P[L]
\]

Nhưng `min` không có inverse tương tự; không thể lấy range min bằng hiệu hai prefix minimum.

Hiểu tính chất đại số giúp biết khi nào prefix query `O(1)` khả thi.

## 23. Prefix Frequency

Với alphabet nhỏ:

```text
pref[i][c] = số lần c trong prefix length i
```

Frequency của `c` trong `[L,R)`:

```text
pref[R][c] - pref[L][c]
```

Trade-off:

```text
memory O(nσ)
query histogram nhanh
```

Kỹ thuật này rất hữu ích cho string/range counting khi `σ` nhỏ.

## 24. Prefix Sum + Hash Map cho Subarray Sum K

Nếu:

\[
P[i]-P[j]=K
\]

thì:

\[
P[j]=P[i]-K
\]

Khi quét `P[i]`, chỉ cần đếm số prefix trước bằng `P[i]-K`.

Hash Map lưu:

```text
prefixValue -> frequency đã thấy
```

Expected `O(n)` kể cả input có số âm.

Đây là một pattern cực quan trọng: biến subarray thành **quan hệ giữa hai prefix states**.

## 25. Longest Subarray với Sum K

Nếu cần độ dài lớn nhất, lưu **vị trí đầu tiên** của mỗi prefix sum.

Khi tại `i` có `P[i]-K` từng xuất hiện ở `j`, subarray `(j,i]` có sum K. Để maximize length, giữ earliest `j`.

Cùng equation nhưng metadata trong Hash Map thay đổi theo objective:

```text
count -> frequency
longest -> earliest index
shortest -> latest index hoặc cấu trúc khác tùy bài
```

## 26. Prefix Minimum và Maximum Subarray

Maximum subarray sum có thể nhìn qua prefix:

\[
P[R]-\min_{L<R}P[L]
\]

Khi quét `R`, chỉ cần giữ minimum prefix trước đó.

Đây là ví dụ prefix summary vẫn hữu ích dù `min` không invertible cho arbitrary range query.

## 27. Kadane dưới góc nhìn Incremental State

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

## 28. 2D Prefix Sum

Với ma trận và prefix rectangle nửa mở:

\[
P[r][c]=sum([0,r)\times[0,c))
\]

Query rectangle:

\[
P[r2][c2]-P[r1][c2]-P[r2][c1]+P[r1][c1]
\]

Đây là inclusion-exclusion: trừ hai vùng thừa và cộng lại vùng bị trừ hai lần.

## 29. Higher-Dimensional Prefix

Ý tưởng mở rộng lên 3D hoặc nhiều chiều bằng inclusion-exclusion trên các mặt/cạnh/góc.

Nhưng số term tăng theo `2^d`, nên practical chủ yếu khi số chiều nhỏ.

Đây là ví dụ complexity phụ thuộc **số chiều**, không chỉ số phần tử.

## 30. Difference Array

Difference representation lưu:

\[
d[i]=a[i]-a[i-1]
\]

với quy ước thích hợp.

Range add `x` vào `[L,R]`:

```text
diff[L] += x
diff[R+1] -= x
```

Sau mọi update, prefix sum của `diff` khôi phục giá trị cuối.

Ta chuyển `O(length)` work của mỗi range update thành hai boundary updates.

## 31. Difference Array như Event Encoding

`+x` tại `L` nghĩa “bắt đầu hiệu lực”. `-x` sau `R` nghĩa “kết thúc hiệu lực”.

Do đó difference array chính là một sweep-line event representation trên miền tọa độ nhỏ/rời rạc.

Prefix sum là bước tích phân các thay đổi đó.

## 32. 2D Difference

Muốn cộng `x` vào rectangle, cập nhật bốn corner của difference matrix theo inclusion-exclusion. Sau đó prefix 2D tái dựng toàn ma trận.

Kỹ thuật này rất mạnh khi có nhiều rectangle updates nhưng chỉ cần materialize kết quả cuối một lần.

Nếu xen kẽ update/query online, cần Fenwick/Segment Tree 2D hoặc structure khác.

## 33. Prefix và Difference là hai cách biểu diễn đối ngẫu

Prefix lưu **trạng thái tích lũy**.

Difference lưu **sự thay đổi giữa các trạng thái kế tiếp**.

```text
difference --prefix sum--> original
original   --difference--> differences
```

Một bên tối ưu query aggregate, bên kia tối ưu range update offline.

Hiểu mối quan hệ này giúp nhớ kỹ thuật một cách tự nhiên.

## 34. Imos Method

Trong một số tài liệu Nhật, difference + prefix cho range coverage được gọi là Imos method.

Ví dụ nhiều đoạn tô màu trên timeline:

```text
+1 tại start
-1 tại end
prefix -> số lớp phủ tại mỗi vị trí
```

Bản chất vẫn là event accumulation.

## 35. Circular Window

Với circular array, có thể:

```text
xử lý index modulo n
hoặc
conceptually concatenate array với chính nó
```

Nhưng phải giới hạn window length không vượt `n` nếu bài chỉ cho mỗi phần tử xuất hiện một vòng.

Circularity thường làm ranh giới phức tạp hơn, không thay bản chất window.

## 36. Two Pointers trên Hai Mảng

Merge hai sorted arrays dùng pointer `i,j`.

Tìm intersection/union cũng vậy.

Mỗi pointer chỉ tăng, nên `O(n+m)`.

Đây là same-direction two pointers nhưng trên hai sequence khác nhau.

## 37. K-Way Merge

Hai pointer tổng quát lên `k` sorted streams bằng min-heap giữ head hiện tại của mỗi stream.

Complexity:

\[
O(N\log k)
\]

với `N` tổng số phần tử.

Đây là ví dụ “two pointers” mở rộng thành frontier có nhiều candidate, và heap trở thành structure chọn candidate nhỏ nhất tiếp theo.

## 38. Binary Search vs Two Pointers

Nếu cần tìm pair cho một query, có thể với mỗi `i` binary-search complement `O(n log n)`. Two pointers exploit monotonic relation giữa cả hai chỉ số để đạt `O(n)`.

Binary search loại ứng viên theo một chiều độc lập; two pointers khai thác quan hệ hai chiều mạnh hơn.

## 39. Monotonicity là tín hiệu quan trọng

Two pointers/sliding window thường xuất hiện khi có một predicate kiểu:

```text
nếu tăng L thì property chỉ thay theo một hướng
nếu tăng R thì property chỉ thay theo một hướng
```

Nếu validity nhảy lên xuống không có cấu trúc, pointer monotonic không đủ.

Hãy tìm **đơn điệu của không gian ứng viên**, không tìm keyword “subarray”.

## 40. Offline Query và Prefix Precomputation

Nếu toàn bộ query đã biết trước, có thể sort/reorder query hoặc xây multiple prefix summaries.

Nếu query đến online sau mỗi update, static prefix không đủ.

Tính online/offline là một chiều thiết kế quan trọng thường bị bỏ qua khi học kỹ thuật này.

## 41. Overflow

Prefix sum rất dễ overflow vì tích lũy nhiều phần tử.

Nếu `a[i]` là `int`, tổng có thể cần `long`.

2D prefix hoặc weighted count còn có thể cần kiểu rộng hơn do tích số lượng phần tử với magnitude.

Kiểu số phải chọn theo cận tổng, không theo cận của một phần tử.

## 42. Memory Trade-Off

Prefix array dùng `O(n)` memory. Nếu chỉ cần running prefix một lần, không cần lưu toàn bộ.

Nếu có nhiều loại query, có thể phải lưu nhiều prefix arrays, tăng memory nhanh.

Data structure design luôn là trade-off giữa recomputation và materialized summaries.

## 43. Kiểm thử

Các case quan trọng:

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

Với window, nên differential-test trên `n` nhỏ bằng brute-force enumerate mọi subarray.

## 44. Những hiểu lầm phổ biến

“Có subarray là dùng sliding window” — sai nếu validity không đơn điệu.

“Hai vòng while/for nghĩa O(n²)” — sai nếu pointer chỉ đi một chiều và mỗi phần tử bị xử lý hữu hạn lần.

“Prefix Sum chỉ dùng để tính tổng” — sai; có thể lưu count, XOR hoặc nhiều summary tích lũy.

“Difference Array dùng được cho update/query online bất kỳ” — sai; dạng đơn giản phù hợp batch updates rồi materialize.

“Two pointers luôn cần sorted array” — không; fast/slow, read/write và variable window không nhất thiết cần sorting.

## Mô hình tư duy

> Hai con trỏ, cửa sổ trượt, prefix và difference đều là kỹ thuật **khai thác tính gần nhau của các trạng thái**. Một trạng thái mới không được tính từ đầu; nó được suy từ trạng thái trước bằng một thay đổi nhỏ hoặc bằng một dữ liệu tóm lược đã tiền xử lý.

Khi gặp bài sequence/range, hãy hỏi: **candidate space có monotonic không, hai biên có thể chỉ di chuyển một chiều không, window state có cập nhật nhanh khi add/remove không, aggregate có inverse không, và có thể lưu thay đổi ở boundary thay vì cập nhật toàn đoạn không?**

Xem thêm: [Searching](./00_searching.md), [Intervals & Sweep Line](./08_intervals_and_sweep_line.md), [Range Queries](../05_specialized/01_range_queries_fenwick_segment_tree.md), [Monotonic Stack/Queue](../01_linear_structures/02_stacks.md), [Queues & Deques](../01_linear_structures/03_queues_deques_and_priority_queues.md).