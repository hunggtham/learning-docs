# Hai con trỏ, cửa sổ trượt, tổng tiền tố và kỹ thuật hiệu

> **Mạch đọc:** [README](../README.md) là bản đồ owner của **Hai con trỏ, cửa sổ trượt, tổng tiền tố và kỹ thuật hiệu**; nhìn vào vị trí đó trước để biết file này đang phục vụ nhánh kiến thức nào. **1. Hai con trỏ trên dữ liệu đã sắp xếp** gom dữ liệu hoặc nguồn để kiểm tra một nhận định cụ thể; sau đó sang **2. bất biến (invariant / 불변식) của Two Pointers** để chuyển câu hỏi ấy thành điều kiện phải giữ. Mạch này nối two pointers/sliding window với prefix difference, để bài toán đoạn liên tiếp được giải bằng invariant và cập nhật biên.

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

Hai con trỏ chỉ tiến một chiều khi thứ tự dữ liệu cho phép loại bỏ một vùng chắc chắn không còn cần xét. Invariant đó phải được viết rõ trước khi tính số lần di chuyển.

## 2. bất biến (invariant / 불변식) của Two Pointers

Cách chứng minh tốt hơn việc nhớ “nếu nhỏ thì L++” là xác định vùng ứng viên còn lại.

Bất biến:

> Nếu có một cặp đáp án chưa được tìm thấy, ít nhất một cặp như vậy vẫn nằm trong hình chữ nhật chỉ số `[L,R]` hiện tại.

Mỗi lần tăng `L` hoặc giảm `R`, ta phải chứng minh toàn bộ các cặp bị loại không thể là đáp án.

Đây là dạng **candidate elimination** giống tìm kiếm nhị phân (binary search / 이진 탐색) nhưng thay vì loại nửa khoảng bằng một phép so sánh, ta loại một hàng/cột ứng viên nhờ monotonic thứ tự (order / 순서).

Khi invariant phụ thuộc dữ liệu đã sắp xếp, chi phí sorting không thể bị ẩn trong nhãn O(n). Tổng chi phí gồm cả sắp xếp và lượt quét, rồi mới so với các dạng two pointers khác.

## 3. Chi phí sorting phải được tính

Nếu đầu vào (input / 입력) chưa được sắp xếp và ta sort trước:

\[
O(n\log n)+O(n)=O(n\log n)
\]

Nếu cần giữ chỉ mục (index / 인덱스) gốc, mỗi phần tử phải mang theo original chỉ mục (index / 인덱스).

Với Two Sum một lần, băm (hash / 해시) Map expected `O(n)` có thể tốt hơn. Với nhiều truy vấn (query / 쿼리) trên cùng dữ liệu, sorting một lần có thể đáng giá hơn.

Luôn phân tích toàn chuỗi xử lý (pipeline / 파이프라인), không chỉ phase quét.

Chi phí sorting quyết định có nên đổi một lần sắp xếp lấy nhiều truy vấn nhanh hay không. Từ đây cần phân biệt các dạng con trỏ: hội tụ, cùng chiều, hoặc một con trỏ đọc–một con trỏ ghi.

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

Read/write pointer không tìm cặp giá trị mà duy trì vùng đã xử lý và vùng chưa xử lý. Với thao tác tại chỗ, câu hỏi tiếp theo là phần tử hợp lệ có giữ nguyên thứ tự hay chấp nhận compaction không ổn định.

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

Stable compaction giữ thứ tự nên thường phải trả thêm di chuyển; unstable compaction có thể đổi phần tử với cuối vùng để giảm ghi. Trên linked list, cặp fast/slow lại diễn đạt invariant khoảng cách thay vì vị trí mảng.

## 6. Stable vs Unstable Compaction

Read/ghi (write / 쓰기) pointer như trên giữ thứ tự tương đối của phần tử được giữ lại, tức là stable.

Nếu không cần giữ thứ tự (order / 순서), có thể swap phần tử cần xóa với phần tử cuối và giảm kích thước lô-gic (logic / 논리); cách này giảm số lần dịch nhưng thay đổi thứ tự (order / 순서).

Yêu cầu ổn định là một phần của đầu ra (output / 출력) ngữ nghĩa (semantics / 의미론), không phải chỉ hiện thực (implementation / 구현) detail.

Fast/slow pointer trên linked list dùng tốc độ khác nhau để phát hiện cấu trúc chu kỳ hoặc tìm midpoint. Floyd gặp nhau không phải do may mắn mà do khoảng cách tương đối modulo độ dài chu kỳ.

## 7. Fast/Slow Pointer trên Linked danh sách (list / 목록)

Floyd cycle detection:

```text
slow += 1 bước
fast += 2 bước
```

Nếu có chu trình, hai pointer cuối cùng gặp nhau. Nếu không, `fast` chạm null.

Tìm middle nút (node / 노드) cũng dùng fast/slow: khi fast đi hết, slow ở gần giữa.

Ở linked danh sách (list / 목록) không có random truy cập (access / 접근), quan hệ (relation / 관계) về tốc độ thay thế arithmetic chỉ mục (index / 인덱스).

Khi fast và slow gặp, ta mới biết có chu kỳ chứ chưa biết entry. Đặt lại một con trỏ về head và tiến cùng tốc độ sẽ biến invariant khoảng cách thành vị trí bắt đầu chu trình.

## 8. Vì sao Floyd gặp nhau?

Sau khi cả hai vào chu trình, xét vị trí modulo độ dài chu trình `C`.

Mỗi bước, khoảng cách tương đối giữa fast và slow tăng 1 modulo `C`.

Do đó sau tối đa `C` bước, khoảng cách trở thành 0 và hai pointer gặp nhau.

Đây là một chứng minh dùng modular arithmetic chứ không phải “fast chắc chắn đuổi kịp slow” theo trực giác mơ hồ.

Chứng minh Floyd gặp nhau dựa trên khoảng cách tương đối modulo độ dài chu kỳ. Từ điểm gặp đó, bước tiếp theo là suy ra entry của chu trình bằng cách đặt một con trỏ lại tại head.

## 9. Tìm điểm bắt đầu chu trình

Sau khi fast và slow gặp nhau, đặt một pointer về head rồi cho cả hai đi 1 bước mỗi lần. Điểm gặp tiếp theo là đầu chu trình.

Kết quả này đến từ quan hệ giữa:

```text
độ dài đoạn trước chu trình
số vòng fast đã đi thêm
vị trí gặp modulo cycle length
```

Đây là ví dụ nơi hiểu đại số giúp nhớ thuật toán tốt hơn học thuộc bước.

Sau khi xác định entry của chu trình, ta quay lại dãy tuyến tính và giữ một cửa sổ có độ dài cố định. Mỗi lần dịch chỉ thêm phần tử mới và loại phần tử cũ.

## 10. Fixed-Size Sliding cửa sổ (window / 윈도우)

Giả sử cần tổng lớn nhất của subarray dài `k`.

Naive: tính lại từng cửa sổ (window / 윈도우) `O(k)`, tổng `O(nk)`.

Nếu sum hiện tại là `S`, dịch một bước:

\[
S' = S-a[L]+a[R+1]
\]

Sau initial `O(k)`, mỗi shift `O(1)`, tổng `O(n)`.

Cửa sổ trượt chính là **incremental maintenance** của summary.

Fixed-size window có độ dài cố định, còn variable-size window thay đổi hai biên để khôi phục điều kiện. Cách co trái chỉ đúng khi việc mở rộng hoặc thu hẹp làm tính hợp lệ biến đổi đơn điệu.

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

Variable-size window cần chứng minh rằng khi cửa sổ đã vi phạm, tăng L sẽ khôi phục tính hợp lệ mà không bỏ sót nghiệm. Nếu tính hợp lệ không đơn điệu, mẫu hai con trỏ có thể sai.

## 12. Sliding cửa sổ (window / 윈도우) cần tính đơn điệu của tính hợp lệ

Ví dụ mảng số dương, tìm longest subarray có sum `<= K`.

Khi tăng `R`, sum không giảm. Khi tăng `L`, sum không tăng.

Predicate “sum <= K” có quan hệ monotonic với hai biên, nên có thể shrink `L` cho tới khi cửa sổ (window / 윈도우) hợp lệ trở lại.

Đây là điều kiện bản chất; cú pháp (syntax / 문법) hai pointer chỉ là biểu hiện bên ngoài.

Âm số phá tính đơn điệu của tổng: thêm phần tử có thể làm tổng giảm, nên không thể tùy ý co cửa sổ khi sum vượt ngưỡng. Khi đó phải chuyển sang prefix sum, deque đơn điệu hoặc cấu trúc phù hợp khác.

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

Với số âm, state của cửa sổ không thể chỉ là sum vì việc mở rộng và thu hẹp không còn đơn điệu. Cần mô hình hóa đủ state để kiểm tra validity trước khi chọn hướng di chuyển.

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

Để xử lý cửa sổ có state phức tạp, cần xác định dữ liệu đủ để kiểm tra validity khi L hoặc R dịch chuyển. Longest Substring Without Repeating Characters dùng tần suất hoặc last-seen của từng ký tự.

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

Longest substring duy trì invariant không ký tự lặp trong [L,R], rồi tăng L đến khi hợp lệ sau mỗi lần tăng R. Minimum Window Substring đảo mục tiêu: cần đủ mọi nhu cầu, nên state phải theo dõi thiếu/thừa.

## 16. Minimum cửa sổ (window / 윈도우) Substring

Cần duy trì số lượng từng ký tự yêu cầu.

Mẫu (pattern / 패턴):

1. mở rộng phải cho đến khi đủ yêu cầu (requirement / 요구사항);
2. shrink trái tối đa trong khi vẫn đủ;
3. cập nhật minimum;
4. tiếp tục mở rộng.

Một biến `formed` hoặc số yêu cầu (requirement / 요구사항) đã thỏa giúp tránh quét toàn frequency map sau mỗi thay đổi.

Bản chất là giữ một predicate “cửa sổ (window / 윈도우) covers mục tiêu (target / 대상) multiset”.

Minimum Window cho thấy cùng sliding window nhưng điều kiện và mục tiêu khác nhau: tìm ngắn nhất thay vì dài nhất. Kỹ thuật At-Most → Exactly biến một số bài đếm “đúng bằng” thành hiệu của hai bài “không vượt quá”.

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

At-Most(K) - At-Most(K-1) loại các cửa sổ có số lượng đúng bằng K. Khi đã xác định mỗi R có bao nhiêu L hợp lệ, bài toán đếm cần giải thích vì sao số lựa chọn là R-L+1.

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

R-L+1 đếm mọi cửa sổ kết thúc tại R khi tính hợp lệ được bảo toàn lúc dịch L. Với bài hỏi cực đại trên từng cửa sổ, ta không đếm mà giữ candidate tốt nhất bằng deque đơn điệu.

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

Deque đơn điệu loại các phần tử không thể trở thành maximum trong tương lai, và mỗi phần tử vào/ra nhiều nhất một lần. Median không có phép loại đơn giản như vậy, nên cần hai nửa có cân bằng.

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

Median window cần duy trì thứ tự và xóa phần tử rời cửa sổ, thường bằng hai heap hoặc cấu trúc có lazy deletion. Khi chuyển từ thứ tự động sang truy vấn tổng, prefix sum cung cấp một biểu diễn tĩnh khác.

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

Prefix sum mã hóa tổng đoạn bằng hiệu của hai prefix, biến truy vấn O(n) thành O(1) sau tiền xử lý. Ý tưởng tổng quát hơn là chọn một phép nghịch đảo để khôi phục đại lượng của đoạn.

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

Prefix technique dựa trên phép nghịch đảo cần biết state prefix nào ghép được với prefix hiện tại. Khi nhiều prefix có cùng giá trị hoặc residue, frequency map trở thành cấu trúc đếm tự nhiên.

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

Prefix frequency đếm trạng thái, còn Subarray Sum K dùng prefix + hash map để truy vấn state đối nghịch. Từ đó, câu hỏi “dài nhất” chuyển trọng tâm sang việc giữ prefix cũ phù hợp nhất.

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

Hash map cho biết với prefix hiện tại P, cần tìm P-K đã xuất hiện trước đó. Nếu mục tiêu là longest subarray, ta phải giữ vị trí xuất hiện sớm nhất thay vì chỉ đếm số lần.

## 25. Longest Subarray với Sum K

Nếu cần độ dài lớn nhất, lưu **vị trí đầu tiên** của mỗi prefix sum.

Khi tại `i` có `P[i]-K` từng xuất hiện ở `j`, subarray `(j,i]` có sum K. Để maximize length, giữ earliest `j`.

Cùng equation nhưng siêu dữ liệu (metadata / 메타데이터) trong băm (hash / 해시) Map thay đổi theo mục tiêu (objective / 목표):

```text
count -> frequency
longest -> earliest index
shortest -> latest index hoặc cấu trúc khác tùy bài
```

Để tối đa độ dài với tổng K, giữ vị trí sớm nhất của mỗi prefix là đủ vì vị trí càng sớm thì đoạn càng dài. Với các mục tiêu min/max tổng đoạn khác, prefix minimum và maximum cung cấp invariant tương ứng.

## 26. Prefix Minimum và Maximum Subarray

Maximum subarray sum có thể nhìn qua prefix:

\[
P[R]-\min_{L<R}P[L]
\]

Khi quét `R`, chỉ cần giữ minimum prefix trước đó.

Đây là ví dụ prefix summary vẫn hữu ích dù `min` không invertible cho arbitrary phạm vi (range / 범위) truy vấn (query / 쿼리).

Prefix min/max biến bài toán tổng đoạn thành so sánh một prefix hiện tại với các prefix trước đó. Kadane có thể được nhìn như cập nhật incremental của cùng trạng thái: giữ best ending here và best toàn cục.

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

Kadane là trạng thái một chiều; khi truy vấn mở rộng thành hình chữ nhật, cần hai chiều prefix để lấy tổng vùng bằng bốn điểm. 2D Prefix Sum là bước nâng chiều có quy tắc bao hàm–loại trừ rõ.

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

2D Prefix Sum trả lời rectangle query O(1) sau O(RC) tiền xử lý. Ở nhiều chiều hơn, cùng công thức inclusion–exclusion vẫn đúng nhưng chi phí bộ nhớ và số hạng tăng theo số chiều.

## 29. Higher-Dimensional Prefix

Ý tưởng mở rộng lên 3D hoặc nhiều chiều bằng inclusion-exclusion trên các mặt/cạnh/góc.

Nhưng số term tăng theo `2^d`, nên practical chủ yếu khi số chiều nhỏ.

Đây là ví dụ độ phức tạp (complexity / 복잡도) phụ thuộc **số chiều**, không chỉ số phần tử.

Higher-dimensional prefix làm rõ giới hạn của tiền xử lý: truy vấn nhanh đổi lấy state lớn. Khi thao tác ngược lại là nhiều cập nhật đoạn rồi mới đọc, Difference Array thường là biểu diễn rẻ hơn.

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

Difference Array mã hóa update trên [L,R] bằng hai sự kiện tại L và R+1, rồi lấy prefix để khôi phục giá trị. Cách nhìn theo sự kiện giúp nối range update với một chuỗi điểm thay đổi.

## 31. Difference Array như sự kiện (event / 이벤트) Encoding

`+x` tại `L` nghĩa “bắt đầu hiệu lực”. `-x` sau `R` nghĩa “kết thúc hiệu lực”.

Do đó difference array chính là một sweep-line sự kiện (event / 이벤트) biểu diễn (representation / 표현) trên miền tọa độ nhỏ/rời rạc.

Prefix sum là bước tích phân các thay đổi đó.

Difference Array như event encoding đặt phần bắt đầu và kết thúc của update ở các boundary. Với lưới, mỗi rectangle update cần bốn corner event, tạo thành 2D Difference.

## 32. 2D Difference

Muốn cộng `x` vào rectangle, cập nhật bốn corner của difference ma trận (matrix / 행렬) theo inclusion-exclusion. Sau đó prefix 2D tái dựng toàn ma trận.

Kỹ thuật này rất mạnh khi có nhiều rectangle updates nhưng chỉ cần materialize kết quả cuối một lần.

Nếu xen kẽ cập nhật (update / 업데이트)/truy vấn (query / 쿼리) online, cần Fenwick/Segment cây (tree / 트리) 2D hoặc cấu trúc (structure / 구조) khác.

2D Difference mở rộng hai điểm thành bốn góc theo inclusion–exclusion, sau đó prefix hai chiều khôi phục ma trận. Các phép biến đổi này cho thấy prefix và difference là hai hướng của cùng một biểu diễn.

## 33. Prefix và Difference là hai cách biểu diễn đối ngẫu

Prefix lưu **trạng thái tích lũy**.

Difference lưu **sự thay đổi giữa các trạng thái kế tiếp**.

```text
difference --prefix sum--> original
original   --difference--> differences
```

Một bên tối ưu truy vấn (query / 쿼리) aggregate, bên kia tối ưu phạm vi (range / 범위) cập nhật (update / 업데이트) offline.

Hiểu mối quan hệ này giúp nhớ kỹ thuật một cách tự nhiên.

Prefix là phép tích lũy để trả lời query; difference là phép đạo hàm rời rạc để ghi nhận update. Hiểu chúng đối ngẫu giúp chọn biểu diễn theo thao tác chi phối, thay vì học hai mẹo rời nhau.

## 34. Imos phương thức (method / 메서드)

Trong một số tài liệu Nhật, difference + prefix cho phạm vi (range / 범위) coverage được gọi là Imos phương thức (method / 메서드).

Ví dụ nhiều đoạn tô màu trên timeline:

```text
+1 tại start
-1 tại end
prefix -> số lớp phủ tại mỗi vị trí
```

Bản chất vẫn là sự kiện (event / 이벤트) accumulation.

Imos method tổ chức nhiều range update thành event rồi quét prefix để lấy trạng thái cuối. Sau kỹ thuật tuyến tính này, circular window đặt lại câu hỏi về boundary khi đầu và cuối dãy nối với nhau.

## 35. Circular cửa sổ (window / 윈도우)

Với circular array, có thể:

```text
xử lý index modulo n
hoặc
conceptually concatenate array với chính nó
```

Nhưng phải giới hạn cửa sổ (window / 윈도우) length không vượt `n` nếu bài chỉ cho mỗi phần tử xuất hiện một vòng.

Circularity thường làm ranh giới phức tạp hơn, không thay bản chất cửa sổ (window / 윈도우).

Circular window biến wrap-around thành một đoạn liên tục trên dãy nhân đôi hoặc hai đoạn ghép. Khi hai dãy đã có thứ tự riêng, two pointers có thể ghép chúng mà không cần tạo toàn bộ tích Descartes.

## 36. Two Pointers trên Hai Mảng

Merge hai sorted arrays dùng pointer `i,j`.

Tìm intersection/union cũng vậy.

Mỗi pointer chỉ tăng, nên `O(n+m)`.

Đây là same-direction two pointers nhưng trên hai chuỗi (sequence / 시퀀스) khác nhau.

Two pointers trên hai mảng tăng khai thác thứ tự để tiến con trỏ nhỏ hơn và loại các cặp đã chắc chắn không tối ưu. Với nhiều hơn hai nguồn đã sắp xếp, K-way Merge tổng quát hóa bằng heap.

## 37. K-Way Merge

Hai pointer tổng quát lên `k` sorted streams bằng min-heap giữ head hiện tại của mỗi stream.

Độ phức tạp (complexity / 복잡도):

\[
O(N\log k)
\]

với `N` tổng số phần tử.

Đây là ví dụ “two pointers” mở rộng thành frontier có nhiều candidate, và vùng nhớ động (heap / 힙) trở thành cấu trúc (structure / 구조) chọn candidate nhỏ nhất tiếp theo.

K-way Merge giữ phần tử nhỏ nhất hiện tại của mỗi nguồn trong heap, khác với two pointers chỉ có hai frontier. Khi chỉ còn một dãy hoặc một predicate đơn điệu, binary search có thể phù hợp hơn.

## 38. tìm kiếm nhị phân (binary search / 이진 탐색) vs Two Pointers

Nếu cần tìm pair cho một truy vấn (query / 쿼리), có thể với mỗi `i` binary-search complement `O(n log n)`. Two pointers exploit monotonic quan hệ (relation / 관계) giữa cả hai chỉ số để đạt `O(n)`.

Tìm kiếm nhị phân (binary search / 이진 탐색) loại ứng viên theo một chiều độc lập; two pointers khai thác quan hệ hai chiều mạnh hơn.

Binary search và two pointers đều khai thác monotonicity nhưng trả giá khác nhau: một bên chia đôi miền, một bên quét và loại vùng. Chọn đúng cần nhìn predicate và số truy vấn, không chỉ nhìn độ phức tạp danh nghĩa.

## 39. Monotonicity là tín hiệu quan trọng

Two pointers/sliding cửa sổ (window / 윈도우) thường xuất hiện khi có một predicate kiểu:

```text
nếu tăng L thì property chỉ thay theo một hướng
nếu tăng R thì property chỉ thay theo một hướng
```

Nếu validity nhảy lên xuống không có cấu trúc, pointer monotonic không đủ.

Hãy tìm **đơn điệu của không gian ứng viên**, không tìm từ khóa (keyword / 키워드) “subarray”.

Monotonicity là tín hiệu cho phép chứng minh pointer không quay lui hoặc ngưỡng tìm kiếm thu hẹp. Khi có nhiều truy vấn trên cùng dữ liệu, offline processing và prefix precomputation có thể materialize thông tin dùng chung.

## 40. Offline truy vấn (query / 쿼리) và Prefix Precomputation

Nếu toàn bộ truy vấn (query / 쿼리) đã biết trước, có thể sort/reorder truy vấn (query / 쿼리) hoặc xây multiple prefix summaries.

Nếu truy vấn (query / 쿼리) đến online sau mỗi cập nhật (update / 업데이트), static prefix không đủ.

Tính online/offline là một chiều thiết kế quan trọng thường bị bỏ qua khi học kỹ thuật này.

Offline query đổi thứ tự xử lý để tận dụng prefix hoặc sort, nhưng tiền xử lý phải chọn kiểu số đủ rộng. Prefix lớn, difference update và tích lũy nhiều lần đều có thể gây overflow trước khi kết quả cuối được kiểm tra.

## 41. Overflow

Prefix sum rất dễ overflow vì tích lũy nhiều phần tử.

Nếu `a[i]` là `int`, tổng có thể cần `long`.

2D prefix hoặc weighted count còn có thể cần kiểu rộng hơn do tích số lượng phần tử với magnitude.

Kiểu số phải chọn theo cận tổng, không theo cận của một phần tử.

Overflow là lỗi semantics chứ không chỉ lỗi hiệu năng; dùng kiểu rộng hơn hoặc modular arithmetic phải phù hợp với contract. Sau đó cần cân đối bộ nhớ: prefix toàn mảng nhanh nhưng tốn RAM, còn streaming hoặc nén có thể giảm footprint.

## 42. bộ nhớ (memory / 메모리) sự đánh đổi (trade-off / 트레이드오프)

Prefix array dùng `O(n)` bộ nhớ (memory / 메모리). Nếu chỉ cần running prefix một lần, không cần lưu toàn bộ.

Nếu có nhiều loại truy vấn (query / 쿼리), có thể phải lưu nhiều prefix arrays, tăng bộ nhớ (memory / 메모리) nhanh.

Cấu trúc dữ liệu (data structure / 자료구조) thiết kế (design / 설계) luôn là sự đánh đổi (trade-off / 트레이드오프) giữa recomputation và materialized summaries.

Memory trade-off quyết định có lưu toàn bộ prefix, deque, map hoặc heap hay không. Kiểm thử phải bao phủ cả kết quả và giới hạn tài nguyên, đặc biệt các case buộc cấu trúc phình đến sát capacity.

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

Test nên kiểm tra invariant, boundary, số âm, overflow, wrap-around và trạng thái rỗng thay vì chỉ vài ví dụ dương. Những hiểu lầm phổ biến thường bắt đầu từ việc áp dụng window hoặc prefix khi điều kiện đơn điệu không tồn tại.

## 44. Những hiểu lầm phổ biến

“Có subarray là dùng sliding cửa sổ (window / 윈도우)” — sai nếu validity không đơn điệu.

“Hai vòng while/for nghĩa O(n²)” — sai nếu pointer chỉ đi một chiều và mỗi phần tử bị xử lý hữu hạn lần.

“Prefix Sum chỉ dùng để tính tổng” — sai; có thể lưu count, XOR hoặc nhiều summary tích lũy.

“Difference Array dùng được cho cập nhật (update / 업데이트)/truy vấn (query / 쿼리) online bất kỳ” — sai; dạng đơn giản phù hợp batch updates rồi materialize.

“Two pointers luôn cần sorted array” — không; fast/slow, read/ghi (write / 쓰기) và variable cửa sổ (window / 윈도우) không nhất thiết cần sorting.

Các hiểu lầm như “hai con trỏ luôn O(n)” hoặc “prefix sum giải được mọi subarray” đều bỏ qua invariant và semantics dữ liệu. Mô hình tư duy cuối file gom lại cách chọn biểu diễn theo update, query và tính đơn điệu.

## Mô hình tư duy

> Hai con trỏ, cửa sổ trượt, prefix và difference đều là kỹ thuật **khai thác tính gần nhau của các trạng thái**. Một trạng thái mới không được tính từ đầu; nó được suy từ trạng thái trước bằng một thay đổi nhỏ hoặc bằng một dữ liệu tóm lược đã tiền xử lý.

Khi gặp bài chuỗi (sequence / 시퀀스)/phạm vi (range / 범위), hãy hỏi: **candidate không gian (space / 공간) có monotonic không, hai biên có thể chỉ di chuyển một chiều không, cửa sổ (window / 윈도우) trạng thái (state / 상태) có cập nhật nhanh khi add/remove không, aggregate có inverse không, và có thể lưu thay đổi ở ranh giới (boundary / 경계) thay vì cập nhật toàn đoạn không?**

Xem thêm: [Searching](./00_searching.md), [Intervals & Sweep Line](./08_intervals_and_sweep_line.md), [Range Queries](../05_specialized/01_range_queries_fenwick_segment_tree.md), [Monotonic Stack/Queue](../01_linear_structures/02_stacks.md), [Queues & Deques](../01_linear_structures/03_queues_deques_and_priority_queues.md).

> **Bàn giao:** Sau **Mô hình tư duy**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](../README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
