# các truy vấn khoảng (range queries): tổng tiền tố, cây Fenwick (Fenwick Tree) và cây đoạn (Segment Tree)

> **Mạch đọc:** [README](../README.md) là bản đồ owner của **các truy vấn khoảng (range queries): tổng tiền tố, cây Fenwick (Fenwick Tree) và cây đoạn (Segment Tree)**; nhìn vào vị trí đó trước để biết file này đang phục vụ nhánh kiến thức nào. **Mô hình tư duy** gom các mảnh thành mental model có thể mang sang nhánh khác; sau đó sang **tổng tiền tố: tĩnh tiền xử lý** để mở rộng đối tượng sang phạm vi kế cận. Mạch này nối range queries với Fenwick và segment tree, để cập nhật và truy vấn được cân bằng theo complexity.

**Truy vấn đoạn, tổng tiền tố, cây Fenwick và cây đoạn / 구간 쿼리, 누적합, 펜윅 트리, 세그먼트 트리**

Nhiều bài toán không hỏi từng phần tử riêng lẻ mà hỏi trên một đoạn:

```text
sum(L,R)
min(L,R)
max(L,R)
count(L,R)
gcd(L,R)
number of active items in [L,R]
```

Nếu mỗi truy vấn quét toàn đoạn, trường hợp xấu nhất là `O(n)` một truy vấn. Với `q` các truy vấn, chi phí có thể thành `O(nq)`.

Range-truy vấn structures xuất hiện khi ta nhận ra rằng nhiều đoạn khác nhau **chia sẻ subranges**, nên có thể lưu trước aggregate của những đoạn chuẩn và ghép chúng lại.

## Mô hình tư duy

> Một range-truy vấn cấu trúc (structure / 구조) đổi lưu trữ/cập nhật chi phí lấy khả năng trả lời một đoạn bằng **một số ít dữ liệu tóm lược đã có**, thay vì đọc từng phần tử.

Ba câu hỏi quyết định cấu trúc (structure / 구조):

```text
Data static hay dynamic?
Query aggregate là gì?
Update là point update hay range update?
```

tổng tiền tố, cây Fenwick và cây đoạn chỉ là ba điểm khác nhau trên sự đánh đổi (trade-off / 트레이드오프) này.

> **Chuyển mạch:** Trong **các truy vấn khoảng (range queries): tổng tiền tố, cây Fenwick (Fenwick Tree) và cây đoạn (Segment Tree)**, **tổng tiền tố: tĩnh tiền xử lý** gom các mảnh từ **Mô hình tư duy** thành một kết luận có thể mang sang phần kế tiếp. Từ đây, **tổng tiền tố 2D** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## tổng tiền tố: tĩnh tiền xử lý

Cho mảng `a[0..n-1]`, định nghĩa:

\[
P[0]=0
\]

\[
P[i+1]=P[i]+a[i]
\]

Khi đó tổng khoảng nửa mở `[L,R)` là:

\[
sum(L,R)=P[R]-P[L]
\]

Nếu dùng khoảng đóng `[L,R]`:

\[
sum(L,R)=P[R+1]-P[L]
\]

Half-open `[L,R)` thường làm ranh giới composition sạch hơn.

### Vì sao subtraction đúng?

`P[R]` chứa tổng từ `0` tới `R-1`. `P[L]` chứa chính phần prefix ta không muốn từ `0` tới `L-1`. Subtract hai summaries loại prefix chung.

Đây là một example của inverse thao tác: tổng prefix có thể “trừ” để lấy phạm vi (range / 범위).

Preprocess:

\[
O(n)
\]

truy vấn:

\[
O(1)
\]

cập nhật điểm giữa mảng có thể làm mọi prefix phía sau thay đổi:

\[
O(n)
\]

tổng tiền tố vì vậy rất phù hợp tĩnh dữ liệu (data / 데이터) hoặc batch các truy vấn sau khi dữ liệu (data / 데이터) đã cố định.

> **Chuyển mạch:** Ở chặng này của **các truy vấn khoảng (range queries): tổng tiền tố, cây Fenwick (Fenwick Tree) và cây đoạn (Segment Tree)**, **tổng tiền tố 2D** tiếp nhận điểm tựa từ **tổng tiền tố: tĩnh tiền xử lý** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **mảng hiệu: cập nhật khoảng, điểm (point / 지점) reconstruction** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## tổng tiền tố 2D

Với ma trận (matrix / 행렬), ta có thể lưu prefix rectangle:

\[
P[r][c] = \văn bản (text / 텍스트){sum của rectangle từ origin tới trước }(r,c)
\]

Rectangle truy vấn dùng inclusion-exclusion:

\[
S(r_1,c_1,r_2,c_2)
=P[r_2][c_2]-P[r_1][c_2]-P[r_2][c_1]+P[r_1][c_1]
\]

Tại sao phải cộng lại góc giao? Vì hai phép trừ đã remove vùng overlap hai lần.

Đây là liên kết (connection / 연결) trực tiếp giữa prefix sums và **inclusion-exclusion**.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **các truy vấn khoảng (range queries): tổng tiền tố, cây Fenwick (Fenwick Tree) và cây đoạn (Segment Tree)**, **mảng hiệu: cập nhật khoảng, điểm (point / 지점) reconstruction** tiếp nhận điểm tựa từ **tổng tiền tố 2D** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **cây Fenwick: động phép tổng hợp tiền tố** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## mảng hiệu: cập nhật khoảng, điểm (point / 지점) reconstruction

tổng tiền tố lưu cumulative các giá trị. **mảng hiệu (차분 배열)** lưu thay đổi giữa các đỉnh kề:

\[
d[i]=a[i]-a[i-1]
\]

Muốn cộng `x` cho closed phạm vi (range / 범위) `[L,R]`:

```text
d[L] += x
d[R+1] -= x   (nếu R+1 tồn tại)
```

Sau tất cả các cập nhật, prefix-sum mảng hiệu để khôi phục các giá trị.

Nếu có nhiều các cập nhật khoảng nhưng chỉ cần materialize final mảng một lần, total có thể là:

```text
O(number of updates + n)
```

thay vì cập nhật từng phần tử.

> **Chuyển mạch:** Trong **các truy vấn khoảng (range queries): tổng tiền tố, cây Fenwick (Fenwick Tree) và cây đoạn (Segment Tree)**, **cây Fenwick: động phép tổng hợp tiền tố** gom các mảnh từ **mảng hiệu: cập nhật khoảng, điểm (point / 지점) reconstruction** thành một kết luận có thể mang sang phần kế tiếp. Từ đây, **Vì sao i & -i lấy least significant set bit?** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## cây Fenwick: động phép tổng hợp tiền tố

**cây Fenwick / nhị phân (binary / 이진) Indexed cây (펜윅 트리 / BIT)** cho cập nhật điểm và prefix-sum truy vấn đều:

\[
O(\log n)
\]

Nó dùng mảng 1-based `bit[]`, trong đó `bit[i]` lưu aggregate của một khối (block / 블록) kết thúc tại `i`.

Khối (block / 블록) kích thước (size / 크기) là:

\[
lowbit(i)=i\&(-i)
\]

nút `i` quản interval:

\[
(i-lowbit(i), i]
\]

trong 1-based lập chỉ mục.

> **Chuyển mạch:** Ở chặng này của **các truy vấn khoảng (range queries): tổng tiền tố, cây Fenwick (Fenwick Tree) và cây đoạn (Segment Tree)**, **Vì sao i & -i lấy least significant set bit?** gom các mảnh từ **cây Fenwick: động phép tổng hợp tiền tố** thành một kết luận có thể mang sang phần kế tiếp. Từ đây, **Fenwick prefix truy vấn** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Vì sao `i & -i` lấy least significant set bit?

Trong two's complement:

\[
-i = \sim i + 1
\]

Các bits thấp hơn bit 1 thấp nhất bị đảo rồi cộng 1 làm carry, kết quả AND với `i` chỉ giữ lại bit 1 thấp nhất.

Ví dụ:

```text
i       = 12 = 1100₂
-i           = 0100₂   (trong fixed-width view phần thấp)
i & -i       = 0100₂ = 4
```

Vậy `bit[12]` quản khối (block / 블록) length 4.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **các truy vấn khoảng (range queries): tổng tiền tố, cây Fenwick (Fenwick Tree) và cây đoạn (Segment Tree)**, **Fenwick prefix truy vấn** tiếp nhận điểm tựa từ **Vì sao i & -i lấy least significant set bit?** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Fenwick cập nhật điểm** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Fenwick prefix truy vấn

Để lấy sum `1..i`:

```text
answer += bit[i]
i -= lowbit(i)
```

Mỗi bước bỏ đi khối (block / 블록) suffix lớn nhất được encode tại `i`.

```java
long sum(int i) {
    long ans = 0;
    while (i > 0) {
        ans += bit[i];
        i -= i & -i;
    }
    return ans;
}
```

Số set bits/khối (block / 블록) jumps tối đa `O(log n)`.

> **Chuyển mạch:** Trong **các truy vấn khoảng (range queries): tổng tiền tố, cây Fenwick (Fenwick Tree) và cây đoạn (Segment Tree)**, **Fenwick cập nhật điểm** tiếp nhận điểm tựa từ **Fenwick prefix truy vấn** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **cây Fenwick nhìn từ nhị phân (binary / 이진) decomposition** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Fenwick cập nhật điểm

Nếu `a[i] += delta`, mọi Fenwick khối (block / 블록) chứa position `i` phải tăng `delta`:

```text
bit[i] += delta
i += lowbit(i)
```

```java
void add(int i, long delta) {
    while (i < bit.length) {
        bit[i] += delta;
        i += i & -i;
    }
}
```

Movement đi tới những ancestors implicit trong binary-index cấu trúc (structure / 구조).

> **Chuyển mạch:** Ở chặng này của **các truy vấn khoảng (range queries): tổng tiền tố, cây Fenwick (Fenwick Tree) và cây đoạn (Segment Tree)**, **cây Fenwick nhìn từ nhị phân (binary / 이진) decomposition** tiếp nhận điểm tựa từ **Fenwick cập nhật điểm** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Phạm vi (range / 범위) sum bằng hai prefix sums** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## cây Fenwick nhìn từ nhị phân (binary / 이진) decomposition

Fenwick không phải cây tường minh (explicit / 명시적). nút cha/quan hệ tổ tiên được encode trực tiếp trong nhị phân (binary / 이진) cách biểu diễn (representation / 표현) của chỉ mục (index / 인덱스).

Prefix `[1..i]` được decomposition thành các power-of-two blocks. truy vấn đi bằng cách clear lowest set bit; cập nhật đi bằng cách add lowbit để tới khối (block / 블록) lớn hơn chứa position.

Đây là lý do Fenwick rất gọn: chỉ `O(n)` mảng, không nút các đối tượng.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **các truy vấn khoảng (range queries): tổng tiền tố, cây Fenwick (Fenwick Tree) và cây đoạn (Segment Tree)**, **Phạm vi (range / 범위) sum bằng hai prefix sums** tiếp nhận điểm tựa từ **cây Fenwick nhìn từ nhị phân (binary / 이진) decomposition** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Fenwick cho tần suất và thống kê thứ tự** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Phạm vi (range / 범위) sum bằng hai prefix sums

Nếu `prefix(i)` trả tổng `1..i`, thì:

\[
phạm vi (range / 범위)(L,R)=prefix(R)-prefix(L-1)
\]

Fenwick vì vậy tự nhiên nhất khi thao tác có inverse đủ để lấy phạm vi (range / 범위) từ two prefixes, điển hình là sum.

> **Chuyển mạch:** Trong **các truy vấn khoảng (range queries): tổng tiền tố, cây Fenwick (Fenwick Tree) và cây đoạn (Segment Tree)**, **Fenwick cho tần suất và thống kê thứ tự** tiếp nhận điểm tựa từ **Phạm vi (range / 범위) sum bằng hai prefix sums** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Inversion Counting bằng Fenwick** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Fenwick cho tần suất và thống kê thứ tự

Nếu `bit[i]` lưu tần suất của giá trị/chỉ mục (index / 인덱스) `i`, tổng tiền tố cho biết số các phần tử `<= i`.

Ta có thể tìm smallest chỉ mục (index / 인덱스) có cumulative tần suất `>= k`, tức k-th phần tử, bằng **nhảy nhị phân** trên cây Fenwick trong `O(log n)` thay vì tìm kiếm nhị phân `O(log^2 n)`.

Idea: xây answer bit-by-bit từ lũy thừa của hai lớn xuống, thử nhảy nếu cumulative sum vẫn < `k`.

Ứng dụng gồm coordinate-compressed tần suất bảng (table / 테이블), inversion counting và động rank các truy vấn.

> **Chuyển mạch:** Ở chặng này của **các truy vấn khoảng (range queries): tổng tiền tố, cây Fenwick (Fenwick Tree) và cây đoạn (Segment Tree)**, **Inversion Counting bằng Fenwick** tiếp nhận điểm tựa từ **Fenwick cho tần suất và thống kê thứ tự** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **cập nhật khoảng + truy vấn điểm với Fenwick** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Inversion Counting bằng Fenwick

Một inversion là pair `(i,j)`:

\[
i<j \land a[i]>a[j]
\]

Coordinate-compress các giá trị thành ranks. xử lý từ phải sang trái:

```text
count elements nhỏ hơn a[i] đã thấy -> prefix(rank-1)
add rank(a[i]) vào Fenwick
```

Total:

\[
O(n\log n)
\]

thay vì pairwise `O(n^2)`.

Đây là example cấu trúc dữ liệu biến historical truy vấn thành phép tổng hợp tiền tố.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **các truy vấn khoảng (range queries): tổng tiền tố, cây Fenwick (Fenwick Tree) và cây đoạn (Segment Tree)**, **cập nhật khoảng + truy vấn điểm với Fenwick** tiếp nhận điểm tựa từ **Inversion Counting bằng Fenwick** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **cập nhật khoảng + phạm vi (range / 범위) Sum với hai Fenwick các cây** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## cập nhật khoảng + truy vấn điểm với Fenwick

Dùng difference-array idea động.

Muốn add `x` cho `[L,R]`:

```text
add(L, +x)
add(R+1, -x)
```

Giá trị tại position `i` là tổng tiền tố Fenwick tại `i`.

Vì vậy Fenwick cây (tree / 트리) không chỉ hỗ trợ cập nhật điểm và truy vấn khoảng; bằng cách biến đổi cách biểu diễn, ta có thể thay đổi mô hình thao tác mà cấu trúc hỗ trợ.

> **Chuyển mạch:** Trong **các truy vấn khoảng (range queries): tổng tiền tố, cây Fenwick (Fenwick Tree) và cây đoạn (Segment Tree)**, **cập nhật khoảng + phạm vi (range / 범위) Sum với hai Fenwick các cây** tiếp nhận điểm tựa từ **cập nhật khoảng + truy vấn điểm với Fenwick** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **cây đoạn: hierarchy của intervals** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## cập nhật khoảng + phạm vi (range / 범위) Sum với hai Fenwick các cây

Có thể dùng hai BITs `B1`, `B2` để hỗ trợ (support / 지원) cộng trên khoảng và prefix/phạm vi (range / 범위) sum.

Prefix sau các cập nhật khoảng có dạng:

\[
prefix(x)=x\cdot sum(B1,x)-sum(B2,x)
\]

các cập nhật điều chỉnh hai các cây ở các ranh giới.

Điểm quan trọng hơn công thức là mental mô hình: ta biểu diễn cumulative tuyến tính (linear / 선형) hàm bằng hai coefficients, giống difference-array algebra mở rộng.

> **Chuyển mạch:** Ở chặng này của **các truy vấn khoảng (range queries): tổng tiền tố, cây Fenwick (Fenwick Tree) và cây đoạn (Segment Tree)**, **cây đoạn: hierarchy của intervals** tiếp nhận điểm tựa từ **cập nhật khoảng + phạm vi (range / 범위) Sum với hai Fenwick các cây** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **cây đoạn bất biến (invariant / 불변식)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## cây đoạn: hierarchy của intervals

**cây đoạn (세그먼트 트리)** chia chỉ mục (index / 인덱스) lĩnh vực (domain / 도메인) thành hierarchy.

nút gốc quản toàn phạm vi (range / 범위). các nút con quản hai halves. Recursively cho tới các nút lá.

Nếu `n` không phải lũy thừa của hai, triển khai có thể dùng cây đệ quy với khoảng `4n` ô nhớ hoặc cây dạng lặp với kích thước đáy là lũy thừa của hai kế tiếp.

Mỗi nút lưu aggregate của segment nó quản.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **các truy vấn khoảng (range queries): tổng tiền tố, cây Fenwick (Fenwick Tree) và cây đoạn (Segment Tree)**, **cây đoạn bất biến (invariant / 불변식)** tiếp nhận điểm tựa từ **cây đoạn: hierarchy của intervals** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Monoid liên kết (connection / 연결)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## cây đoạn bất biến (invariant / 불변식)

Nếu thao tác `combine` có tính kết hợp (associative):

\[
giá trị(node)=kết hợp(giá trị(left),giá trị(right))
\]

thì truy vấn phạm vi (range / 범위) có thể decomposition thành `O(log n)` chuẩn gốc (canonical / 정본) segments.

Examples:

```text
sum -> combine = +, identity = 0
min -> combine = min, identity = +infinity
max -> combine = max, identity = -infinity
gcd -> combine = gcd, identity = 0
```

Associativity đảm bảo grouping của segments không thay answer.

> **Chuyển mạch:** Trong **các truy vấn khoảng (range queries): tổng tiền tố, cây Fenwick (Fenwick Tree) và cây đoạn (Segment Tree)**, **Monoid liên kết (connection / 연결)** tiếp nhận điểm tựa từ **cây đoạn bất biến (invariant / 불변식)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Iterative cây đoạn** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Monoid liên kết (connection / 연결)

Một **monoid** là một set với có tính kết hợp (associative) nhị phân (binary / 이진) thao tác và định danh (identity / 식별자) phần tử.

cây đoạn là khung làm việc rất tự nhiên cho monoid aggregates.

Không cần trừu tượng algebra để mã (code / 코드), nhưng khái niệm này giải thích vì sao cùng cây skeleton áp dụng cho sum/min/max/gcd/phép nhân ma trận (matrix multiplication / 행렬 곱셈)/hàm composition khi thao tác thỏa các tính chất cần thiết.

Nếu thao tác không có tính giao hoán (commutative), thứ tự kết hợp phải được giữ đúng. Iterative truy vấn thường giữ `ansLeft` và `ansRight` riêng vì thế.

> **Chuyển mạch:** Ở chặng này của **các truy vấn khoảng (range queries): tổng tiền tố, cây Fenwick (Fenwick Tree) và cây đoạn (Segment Tree)**, **Iterative cây đoạn** tiếp nhận điểm tựa từ **Monoid liên kết (connection / 연결)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Tại sao truy vấn chỉ O(log n) segments?** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Iterative cây đoạn

Với cơ sở (base / 기반) kích thước (size / 크기) `n` power-of-two-ish, các nút lá nằm ở `[n,2n)`.

```js
class SegmentTree {
  constructor(a) {
    this.n = 1;
    while (this.n < a.length) this.n <<= 1;

    this.t = Array(this.n * 2).fill(0);
    for (let i = 0; i < a.length; i++) {
      this.t[this.n + i] = a[i];
    }

    for (let i = this.n - 1; i > 0; i--) {
      this.t[i] = this.t[i << 1] + this.t[i << 1 | 1];
    }
  }

  set(i, value) {
    let p = this.n + i;
    this.t[p] = value;

    for (p >>= 1; p > 0; p >>= 1) {
      this.t[p] = this.t[p << 1] + this.t[p << 1 | 1];
    }
  }

  query(l, r) { // [l, r)
    let leftAgg = 0;
    let rightAgg = 0;

    for (l += this.n, r += this.n; l < r; l >>= 1, r >>= 1) {
      if (l & 1) leftAgg += this.t[l++];
      if (r & 1) rightAgg = this.t[--r] + rightAgg;
    }

    return leftAgg + rightAgg;
  }
}
```

cập nhật điểm và truy vấn khoảng (range query) đều:

\[
O(\log n)
\]

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **các truy vấn khoảng (range queries): tổng tiền tố, cây Fenwick (Fenwick Tree) và cây đoạn (Segment Tree)**, **Tại sao truy vấn chỉ O(log n) segments?** tiếp nhận điểm tựa từ **Iterative cây đoạn** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Lazy Propagation** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Tại sao truy vấn chỉ O(log n) segments?

Khi decomposition arbitrary interval `[L,R)` theo cây nhị phân, mỗi tầng chỉ có tối đa vài ranh giới các nút chưa được cover hoàn toàn. Whole interior các cây con được lấy nguyên.

Ta không đi qua mọi nút lá; ta chọn những chuẩn gốc (canonical / 정본) segments lớn nhất nằm hoàn toàn trong truy vấn.

Số segments bounded logarithmically.

> **Chuyển mạch:** Trong **các truy vấn khoảng (range queries): tổng tiền tố, cây Fenwick (Fenwick Tree) và cây đoạn (Segment Tree)**, **Lazy Propagation** tiếp nhận điểm tựa từ **Tại sao truy vấn chỉ O(log n) segments?** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **cộng trên khoảng + phạm vi (range / 범위) Sum** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Lazy Propagation

Nếu cập nhật cả phạm vi (range / 범위) `[L,R)` bằng cách đi từng nút lá, cập nhật có thể `O(n)`.

**Lazy propagation (지연 전파)** lưu pending thao tác tại nút quản whole covered segment.

bất biến quan trọng:

> `node.value` đã phản ánh cập nhật lô-gic (logic / 논리) cho toàn segment, dù các nút con có thể chưa materialize cập nhật đó.

Khi cần descend, `push(node)` truyền lazy tag xuống các nút con trước.

> **Chuyển mạch:** Ở chặng này của **các truy vấn khoảng (range queries): tổng tiền tố, cây Fenwick (Fenwick Tree) và cây đoạn (Segment Tree)**, **cộng trên khoảng + phạm vi (range / 범위) Sum** tiếp nhận điểm tựa từ **Lazy Propagation** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Lazy tag composition** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## cộng trên khoảng + phạm vi (range / 범위) Sum

Nếu một nút quản lý đoạn có độ dài `len` và nhận phép cộng `delta` trên cả khoảng, tổng được lưu tại nút tăng thêm:

\[
nút.sum += delta \cdot len
\]

Lazy tag:

```text
node.lazy += delta
```

Khi push:

```text
apply delta to left child
apply delta to right child
clear current lazy
```

cập nhật/truy vấn vẫn `O(log n)` nếu thao tác/tag composition được thiết kế đúng.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **các truy vấn khoảng (range queries): tổng tiền tố, cây Fenwick (Fenwick Tree) và cây đoạn (Segment Tree)**, **Lazy tag composition** tiếp nhận điểm tựa từ **cộng trên khoảng + phạm vi (range / 범위) Sum** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **cây đoạn Beats và advanced các cập nhật** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Lazy tag composition

Không phải mọi cập nhật kiểu (type / 타입) compose giống nhau.

cộng trên khoảng:

```text
old lazy += newDelta
```

Phạm vi (range / 범위) assign:

```text
new assignment overrides old assignment
```

Nếu hỗ trợ (support / 지원) cả assign và add, thứ tự (order / 순서) matters:

```text
assign 5 rồi add 3 != add 3 rồi assign 5
```

Lazy propagation trở nên khó chính ở việc define algebra của tags, không phải traversal cây.

> **Chuyển mạch:** Trong **các truy vấn khoảng (range queries): tổng tiền tố, cây Fenwick (Fenwick Tree) và cây đoạn (Segment Tree)**, **cây đoạn Beats và advanced các cập nhật** tiếp nhận điểm tựa từ **Lazy tag composition** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Persistent cây đoạn** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## cây đoạn Beats và advanced các cập nhật

Một số thao tác trên khoảng như `chmin/chmax` không thể kết hợp đơn giản bằng thẻ lazy chuẩn. **Segment cây (tree / 트리) Beats** lưu thêm siêu dữ liệu như giá trị lớn nhất, lớn thứ hai và số lần xuất hiện của cực đại để áp dụng trực tiếp một số cập nhật khi điều kiện cho phép.

Đây là advanced technique cho thấy augmentation được thiết kế quanh cập nhật ngữ nghĩa (semantics / 의미론) cụ thể.

Không nên dùng nếu tiêu chuẩn (standard / 표준) cấu trúc (structure / 구조) đủ; chứng minh/bất biến phức tạp hơn đáng kể.

> **Chuyển mạch:** Ở chặng này của **các truy vấn khoảng (range queries): tổng tiền tố, cây Fenwick (Fenwick Tree) và cây đoạn (Segment Tree)**, **Persistent cây đoạn** tiếp nhận điểm tựa từ **cây đoạn Beats và advanced các cập nhật** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **động / Implicit cây đoạn** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Persistent cây đoạn

Thay vì mutate các nút, mỗi cập nhật bản sao (copy / 복사) chỉ `O(log n)` các nút trên đường từ gốc tới lá và share phần còn lại.

Mỗi phiên bản (version / 버전) có một nút gốc riêng.

Ứng dụng:

```text
query historical versions
k-th number in subarray
versioned frequencies
functional/persistent state
```

bộ nhớ cho `q` điểm (point / 지점) các cập nhật khoảng:

\[
O(n + q\log n)
\]

nếu initial xây dựng plus path-copying.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **các truy vấn khoảng (range queries): tổng tiền tố, cây Fenwick (Fenwick Tree) và cây đoạn (Segment Tree)**, **động / Implicit cây đoạn** tiếp nhận điểm tựa từ **Persistent cây đoạn** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Coordinate Compression** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## động / Implicit cây đoạn

Nếu coordinate lĩnh vực (domain / 도메인) rất lớn, ví dụ `[0,10^9]`, nhưng chỉ ít positions được cập nhật, xây dựng full cây là lãng phí.

Implicit cây đoạn chỉ cấp phát các nút khi cần. chiều cao vẫn `O(log coordinateRange)`.

Nó đổi contiguous-array tính cục bộ (locality) lấy sparse-domain bộ nhớ saving.

Coordinate compression thường là alternative nếu toàn bộ các tọa độ liên quan biết trước ngoại tuyến.

> **Chuyển mạch:** Trong **các truy vấn khoảng (range queries): tổng tiền tố, cây Fenwick (Fenwick Tree) và cây đoạn (Segment Tree)**, **Coordinate Compression** tiếp nhận điểm tựa từ **động / Implicit cây đoạn** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **cây đoạn vs bảng thưa (Sparse Table)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Coordinate Compression

Nếu các khóa là:

```text
1, 1000000000, 500000000000
```

nhưng chỉ thứ tự tương đối quan trọng, sort unique các giá trị và map thành ranks `0..m-1`.

Fenwick/cây đoạn sau đó chạy trên compressed indices.

Tuy nhiên nén tọa độ không giữ nguyên khoảng cách thực. Nếu độ dài đoạn có ý nghĩa, chẳng hạn khi tính diện tích hợp các hình chữ nhật, phải lưu tọa độ gốc để nhân với độ dài thật.

> **Chuyển mạch:** Ở chặng này của **các truy vấn khoảng (range queries): tổng tiền tố, cây Fenwick (Fenwick Tree) và cây đoạn (Segment Tree)**, **cây đoạn vs bảng thưa (Sparse Table)** tiếp nhận điểm tựa từ **Coordinate Compression** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Fenwick vs cây đoạn** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## cây đoạn vs bảng thưa (Sparse Table)

tĩnh lũy đẳng (idempotent) các truy vấn như phạm vi (range / 범위) min có thể dùng bảng thưa:

```text
preprocess O(n log n)
query O(1)
no efficient updates
```

cây đoạn:

```text
build O(n)
query O(log n)
update O(log n)
```

Nếu dữ liệu (data / 데이터) không đổi, cây đoạn có thể là overkill.

Xem [Sparse Table](./05_sparse_table_and_static_range_queries.md).

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **các truy vấn khoảng (range queries): tổng tiền tố, cây Fenwick (Fenwick Tree) và cây đoạn (Segment Tree)**, **Fenwick vs cây đoạn** tiếp nhận điểm tựa từ **cây đoạn vs bảng thưa (Sparse Table)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **truy vấn khoảng quyết định (decision / 결정) Guide** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Fenwick vs cây đoạn

Fenwick:

```text
code ngắn
gọn memory
cache-friendly
excellent cho prefix sums/frequencies
less flexible aggregate/update model
```

cây đoạn:

```text
flexible monoid aggregates
range updates với lazy
augmentation mạnh
code/memory phức tạp hơn
```

Không có cấu trúc (structure / 구조) “mạnh hơn nên luôn tốt hơn”. Chọn theo các thao tác thực tế.

> **Chuyển mạch:** Trong **các truy vấn khoảng (range queries): tổng tiền tố, cây Fenwick (Fenwick Tree) và cây đoạn (Segment Tree)**, **truy vấn khoảng quyết định (decision / 결정) Guide** tiếp nhận điểm tựa từ **Fenwick vs cây đoạn** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **lập chỉ mục bugs: 0-based vs 1-based** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## truy vấn khoảng quyết định (decision / 결정) Guide

Phần này chuyển khái niệm Computer Science thành cấu trúc, ví dụ hoặc quy trình có thể kiểm tra. Hãy xác định câu hỏi mà mục trả lời rồi nối kết luận với phần kế tiếp.

| khối lượng công việc | Structure phù hợp |
|---|---|
| tĩnh phạm vi (range / 범위) sum | tổng tiền tố |
| nhiều truy vấn cực tiểu/cực đại trên dữ liệu tĩnh | Bảng thưa (Sparse Table) |
| điểm (point / 지점) add + prefix/phạm vi (range / 범위) sum | cây Fenwick |
| động tần suất + rank/k-th | cây Fenwick |
| cập nhật điểm + tổng hợp khoảng tổng quát có tính kết hợp (associative) | Cây đoạn (Segment Tree) |
| cập nhật khoảng + truy vấn khoảng | Lazy cây đoạn |
| sparse huge coordinate lĩnh vực (domain / 도메인) | Compression hoặc Implicit cây đoạn |
| historical versions | Persistent cây đoạn |

> **Chuyển mạch:** Ở chặng này của **các truy vấn khoảng (range queries): tổng tiền tố, cây Fenwick (Fenwick Tree) và cây đoạn (Segment Tree)**, **lập chỉ mục bugs: 0-based vs 1-based** tiếp nhận điểm tựa từ **truy vấn khoảng quyết định (decision / 결정) Guide** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **tràn số** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## lập chỉ mục bugs: 0-based vs 1-based

Fenwick thường tự nhiên với 1-based lập chỉ mục vì `lowbit(0)=0` làm cập nhật vòng lặp (loop / 루프) không tiến nếu bắt đầu ở 0.

Một wrapper tốt có thể expose 0-based API nhưng convert nội bộ:

```text
external index i
internal index i+1
```

Đừng mix hai các hệ thống trong cùng formula.

cây đoạn nên chọn rõ interval convention. Half-open `[L,R)` thường giảm off-by-one bugs và compose tự nhiên:

```text
[L,M) + [M,R) = [L,R)
```

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **các truy vấn khoảng (range queries): tổng tiền tố, cây Fenwick (Fenwick Tree) và cây đoạn (Segment Tree)**, **tràn số** tiếp nhận điểm tựa từ **lập chỉ mục bugs: 0-based vs 1-based** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Non-có tính giao hoán (commutative) kết hợp** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## tràn số

Phạm vi (range / 범위) sums dễ vượt 32-bit ngay cả khi mỗi phần tử nhỏ.

Ví dụ `n = 100000`, mỗi giá trị `10^9`:

\[
sum = 10^{14}
\]

Java cần `long`, C cần kiểu (type / 타입) đủ rộng như `int64_t` tùy lĩnh vực (domain / 도메인). JavaScript `Number` chính xác integer tới `2^53-1`; lớn hơn có thể cần `BigInt`.

Lazy multiplication `delta * segmentLength` cũng phải dùng wide kiểu (type / 타입) trước khi multiply.

> **Chuyển mạch:** Trong **các truy vấn khoảng (range queries): tổng tiền tố, cây Fenwick (Fenwick Tree) và cây đoạn (Segment Tree)**, **Non-có tính giao hoán (commutative) kết hợp** tiếp nhận điểm tựa từ **tràn số** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **kiểm thử phạm vi (range / 범위) Structures** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Non-có tính giao hoán (commutative) kết hợp

Nếu aggregate là phép nhân ma trận (matrix multiplication / 행렬 곱셈) hoặc string/hàm composition, thao tác có tính kết hợp (associative) nhưng không có tính giao hoán (commutative).

Với phép toán không giao hoán, truy vấn dạng lặp không thể gộp kết quả theo thứ tự tùy ý. Phải duy trì riêng bộ tích lũy trái và phải theo đúng thứ tự:

```text
leftAgg  = combine(leftAgg, segment)
rightAgg = combine(segment, rightAgg)
```

Sau đó:

```text
combine(leftAgg, rightAgg)
```

Đây là lý do monoid mental mô hình sâu hơn “cây đoạn dùng cho sum”.

> **Chuyển mạch:** Ở chặng này của **các truy vấn khoảng (range queries): tổng tiền tố, cây Fenwick (Fenwick Tree) và cây đoạn (Segment Tree)**, **kiểm thử phạm vi (range / 범위) Structures** tiếp nhận điểm tựa từ **Non-có tính giao hoán (commutative) kết hợp** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Real-world connections** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## kiểm thử phạm vi (range / 범위) Structures

Differential kiểm thử rất hiệu quả. Với `n` nhỏ, giữ plain mảng làm oracle.

ngẫu nhiên các thao tác:

```text
point update
range update
range query
```

Sau mỗi truy vấn, so sánh cấu trúc (structure / 구조) với brute-force mảng.

các bất biến:

```text
Fenwick prefix(n) == total array sum
Segment parent == combine(children)
Lazy node value reflects pending tag semantically
Persistent old version không đổi sau new update
```

ranh giới tests:

```text
empty range [i,i)
whole range
single element
first/last index
n not power of two
negative values
duplicate updates
large sums
```

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **các truy vấn khoảng (range queries): tổng tiền tố, cây Fenwick (Fenwick Tree) và cây đoạn (Segment Tree)**, **Real-world connections** tiếp nhận điểm tựa từ **kiểm thử phạm vi (range / 범위) Structures** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Mô hình tư duy mở rộng** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Real-world connections

Tổng hợp theo khoảng xuất hiện trong giám sát chuỗi thời gian, đếm sự kiện, phân tích dữ liệu, bảng điểm, thay đổi tồn kho, hình học tính toán và các cơ chế lập chỉ mục kiểu cơ sở dữ liệu.

Tuy nhiên các hệ thống thực tế thường dùng B-trees, column stores, Fenwick-like structures, hierarchical aggregates hoặc segment các cây tùy lưu trữ mô hình. Kinh điển DSA structures là mental primitives; actual hệ thống cách biểu diễn có thể thay đổi theo bộ nhớ đệm/page/phân phối concerns.

> **Chuyển mạch:** Trong **các truy vấn khoảng (range queries): tổng tiền tố, cây Fenwick (Fenwick Tree) và cây đoạn (Segment Tree)**, **Mô hình tư duy mở rộng** gom các mảnh từ **Real-world connections** thành một kết luận có thể mang sang phần kế tiếp. Phần còn lại của file dùng kết quả này để khép lại mạch giải thích.

## Mô hình tư duy mở rộng

> Range-truy vấn thiết kế (design / 설계) là bài toán chọn **các đoạn chuẩn** sao cho cập nhật chạm ít dữ liệu tóm lược và truy vấn ghép từ ít dữ liệu tóm lược.

tổng tiền tố chọn mọi prefix nên truy vấn cực rẻ nhưng cập nhật đắt. Fenwick chọn nhị phân (binary / 이진) suffix blocks để cân bằng cập nhật điểm/prefix truy vấn. cây đoạn chọn hierarchy intervals để hỗ trợ aggregate linh hoạt và các cập nhật khoảng.

Khi hiểu những decomposition này, bạn không còn cần học thuộc `i += i & -i` hay cây đệ quy như công thức rời rạc; bạn thấy chúng là các cách encode shared range thông tin theo khối lượng công việc.

> **Bàn giao:** Sau **Mô hình tư duy mở rộng**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](../README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
