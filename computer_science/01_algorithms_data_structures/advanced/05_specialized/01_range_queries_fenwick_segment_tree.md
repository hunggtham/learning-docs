# Range Queries: Prefix Sum, Fenwick Tree và Segment Tree
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

Nếu mỗi query quét toàn đoạn, worst-case là `O(n)` một query. Với `q` queries, cost có thể thành `O(nq)`.

Range-query structures xuất hiện khi ta nhận ra rằng nhiều đoạn khác nhau **chia sẻ subranges**, nên có thể lưu trước aggregate của những đoạn chuẩn và ghép chúng lại.

## Mental Model

> Một range-query structure đổi storage/update cost lấy khả năng trả lời một đoạn bằng **một số ít summary đã có**, thay vì đọc từng element.

Ba câu hỏi quyết định structure:

```text
Data static hay dynamic?
Query aggregate là gì?
Update là point update hay range update?
```

Prefix sum, Fenwick tree và segment tree chỉ là ba điểm khác nhau trên trade-off này.

## Prefix Sum: static preprocessing

Cho array `a[0..n-1]`, định nghĩa:

\[
P[0]=0
\]

\[
P[i+1]=P[i]+a[i]
\]

Khi đó tổng half-open interval `[L,R)` là:

\[
sum(L,R)=P[R]-P[L]
\]

Nếu dùng closed interval `[L,R]`:

\[
sum(L,R)=P[R+1]-P[L]
\]

Half-open `[L,R)` thường làm boundary composition sạch hơn.

### Vì sao subtraction đúng?

`P[R]` chứa tổng từ `0` tới `R-1`. `P[L]` chứa chính phần prefix ta không muốn từ `0` tới `L-1`. Subtract hai summaries loại prefix chung.

Đây là một example của inverse operation: tổng prefix có thể “trừ” để lấy range.

Preprocess:

\[
O(n)
\]

Query:

\[
O(1)
\]

Point update giữa array có thể làm mọi prefix phía sau thay đổi:

\[
O(n)
\]

Prefix sum vì vậy rất phù hợp static data hoặc batch queries sau khi data đã cố định.

## Prefix Sum 2D

Với matrix, ta có thể lưu prefix rectangle:

\[
P[r][c] = \text{sum của rectangle từ origin tới trước }(r,c)
\]

Rectangle query dùng inclusion-exclusion:

\[
S(r_1,c_1,r_2,c_2)
=P[r_2][c_2]-P[r_1][c_2]-P[r_2][c_1]+P[r_1][c_1]
\]

Tại sao phải cộng lại góc giao? Vì hai phép trừ đã remove vùng overlap hai lần.

Đây là connection trực tiếp giữa prefix sums và **inclusion-exclusion**.

## Difference Array: range update, point reconstruction

Prefix sum lưu cumulative values. **Difference array (차분 배열)** lưu thay đổi giữa neighbors:

\[
d[i]=a[i]-a[i-1]
\]

Muốn cộng `x` cho closed range `[L,R]`:

```text
d[L] += x
d[R+1] -= x   (nếu R+1 tồn tại)
```

Sau tất cả updates, prefix-sum difference array để khôi phục values.

Nếu có nhiều range updates nhưng chỉ cần materialize final array một lần, total có thể là:

```text
O(number of updates + n)
```

thay vì update từng element.

## Fenwick Tree: dynamic prefix aggregate

**Fenwick Tree / Binary Indexed Tree (펜윅 트리 / BIT)** cho point update và prefix-sum query đều:

\[
O(\log n)
\]

Nó dùng array 1-based `bit[]`, trong đó `bit[i]` lưu aggregate của một block kết thúc tại `i`.

Block size là:

\[
lowbit(i)=i\&(-i)
\]

Node `i` quản interval:

\[
(i-lowbit(i), i]
\]

trong 1-based indexing.

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

Vậy `bit[12]` quản block length 4.

## Fenwick prefix query

Để lấy sum `1..i`:

```text
answer += bit[i]
i -= lowbit(i)
```

Mỗi bước bỏ đi block suffix lớn nhất được encode tại `i`.

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

Số set bits/block jumps tối đa `O(log n)`.

## Fenwick point update

Nếu `a[i] += delta`, mọi Fenwick block chứa position `i` phải tăng `delta`:

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

Movement đi tới những ancestors implicit trong binary-index structure.

## Fenwick Tree nhìn từ binary decomposition

Fenwick không phải tree explicit. Parent/ancestor relation được encode trực tiếp trong binary representation của index.

Prefix `[1..i]` được decomposition thành các power-of-two blocks. Query đi bằng cách clear lowest set bit; update đi bằng cách add lowbit để tới block lớn hơn chứa position.

Đây là lý do Fenwick rất compact: chỉ `O(n)` array, không node objects.

## Range sum bằng hai prefix sums

Nếu `prefix(i)` trả tổng `1..i`, thì:

\[
range(L,R)=prefix(R)-prefix(L-1)
\]

Fenwick vì vậy tự nhiên nhất khi operation có inverse đủ để lấy range từ two prefixes, điển hình là sum.

## Fenwick cho frequency và order statistic

Nếu `bit[i]` lưu frequency của value/index `i`, prefix sum cho biết số elements `<= i`.

Ta có thể tìm smallest index có cumulative frequency `>= k`, tức k-th element, bằng **binary lifting** trên Fenwick tree trong `O(log n)` thay vì binary search `O(log^2 n)`.

Idea: xây answer bit-by-bit từ power of two lớn xuống, thử nhảy nếu cumulative sum vẫn < `k`.

Ứng dụng gồm coordinate-compressed frequency table, inversion counting và dynamic rank queries.

## Inversion Counting bằng Fenwick

Một inversion là pair `(i,j)`:

\[
i<j \land a[i]>a[j]
\]

Coordinate-compress values thành ranks. Process từ phải sang trái:

```text
count elements nhỏ hơn a[i] đã thấy -> prefix(rank-1)
add rank(a[i]) vào Fenwick
```

Total:

\[
O(n\log n)
\]

thay vì pairwise `O(n^2)`.

Đây là example data structure biến historical query thành prefix aggregate.

## Range Update + Point Query với Fenwick

Dùng difference-array idea động.

Muốn add `x` cho `[L,R]`:

```text
add(L, +x)
add(R+1, -x)
```

Giá trị tại position `i` là prefix sum Fenwick tại `i`.

Vậy Fenwick không chỉ point-update/range-query; bằng representation transform, ta đổi operation model.

## Range Update + Range Sum với hai Fenwick Trees

Có thể dùng hai BITs `B1`, `B2` để support range add và prefix/range sum.

Prefix sau range updates có dạng:

\[
prefix(x)=x\cdot sum(B1,x)-sum(B2,x)
\]

Updates điều chỉnh hai trees ở boundaries.

Điểm quan trọng hơn công thức là mental model: ta biểu diễn cumulative linear function bằng hai coefficients, giống difference-array algebra mở rộng.

## Segment Tree: hierarchy của intervals

**Segment Tree (세그먼트 트리)** chia index domain thành hierarchy.

Root quản toàn range. Children quản hai halves. Recursively cho tới leaves.

Nếu `n` không phải power of two, implementation có thể dùng recursive tree `4n` space hoặc iterative tree với base size là next power of two.

Mỗi node lưu aggregate của segment nó quản.

## Segment Tree Invariant

Nếu operation `combine` associative:

\[
value(node)=combine(value(left),value(right))
\]

thì query range có thể decomposition thành `O(log n)` canonical segments.

Examples:

```text
sum -> combine = +, identity = 0
min -> combine = min, identity = +infinity
max -> combine = max, identity = -infinity
gcd -> combine = gcd, identity = 0
```

Associativity đảm bảo grouping của segments không thay answer.

## Monoid connection

Một **monoid** là một set với associative binary operation và identity element.

Segment tree là framework rất tự nhiên cho monoid aggregates.

Không cần abstract algebra để code, nhưng khái niệm này giải thích vì sao cùng tree skeleton áp dụng cho sum/min/max/gcd/matrix multiplication/function composition khi operation thỏa properties cần thiết.

Nếu operation không commutative, thứ tự combine phải được giữ đúng. Iterative query thường giữ `ansLeft` và `ansRight` riêng vì thế.

## Iterative Segment Tree

Với base size `n` power-of-two-ish, leaves nằm ở `[n,2n)`.

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

Point update và range query đều:

\[
O(\log n)
\]

## Tại sao query chỉ O(log n) segments?

Khi decomposition arbitrary interval `[L,R)` theo binary tree, mỗi level chỉ có tối đa vài boundary nodes chưa được cover hoàn toàn. Whole interior subtrees được lấy nguyên.

Ta không đi qua mọi leaf; ta chọn những canonical segments lớn nhất nằm hoàn toàn trong query.

Số segments bounded logarithmically.

## Lazy Propagation

Nếu update cả range `[L,R)` bằng cách đi từng leaf, update có thể `O(n)`.

**Lazy propagation (지연 전파)** lưu pending operation tại node quản whole covered segment.

Invariant quan trọng:

> `node.value` đã phản ánh update logic cho toàn segment, dù children có thể chưa materialize update đó.

Khi cần descend, `push(node)` truyền lazy tag xuống children trước.

## Range Add + Range Sum

Nếu node quản segment length `len` và có range-add `delta`, aggregate sum tăng:

\[
node.sum += delta \cdot len
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

Update/query vẫn `O(log n)` nếu operation/tag composition được thiết kế đúng.

## Lazy tag composition

Không phải mọi update type compose giống nhau.

Range add:

```text
old lazy += newDelta
```

Range assign:

```text
new assignment overrides old assignment
```

Nếu support cả assign và add, order matters:

```text
assign 5 rồi add 3 != add 3 rồi assign 5
```

Lazy propagation trở nên khó chính ở việc define algebra của tags, không phải traversal tree.

## Segment Tree Beats và advanced updates

Một số range operations như range `chmin/chmax` không compose đơn giản bằng standard lazy tag. **Segment Tree Beats** giữ thêm metadata như max, second max, count max để apply một số updates trực tiếp khi condition đủ mạnh.

Đây là advanced technique cho thấy augmentation được thiết kế quanh update semantics cụ thể.

Không nên dùng nếu standard structure đủ; proof/invariant phức tạp hơn đáng kể.

## Persistent Segment Tree

Thay vì mutate nodes, mỗi update copy chỉ `O(log n)` nodes trên root-to-leaf path và share phần còn lại.

Mỗi version có một root riêng.

Ứng dụng:

```text
query historical versions
k-th number in subarray
versioned frequencies
functional/persistent state
```

Memory cho `q` point updates khoảng:

\[
O(n + q\log n)
\]

nếu initial build plus path-copying.

## Dynamic / Implicit Segment Tree

Nếu coordinate domain rất lớn, ví dụ `[0,10^9]`, nhưng chỉ ít positions được update, build full tree là lãng phí.

Implicit segment tree chỉ allocate nodes khi cần. Height vẫn `O(log coordinateRange)`.

Nó đổi contiguous-array locality lấy sparse-domain memory saving.

Coordinate compression thường là alternative nếu toàn bộ relevant coordinates biết trước offline.

## Coordinate Compression

Nếu keys là:

```text
1, 1000000000, 500000000000
```

nhưng chỉ relative order quan trọng, sort unique values và map thành ranks `0..m-1`.

Fenwick/segment tree sau đó chạy trên compressed indices.

Nhưng compression không giữ raw distance. Nếu segment length matter, ví dụ rectangle union area, phải lưu original coordinates để nhân độ dài thật.

## Segment Tree vs Sparse Table

Static idempotent queries như range min có thể dùng Sparse Table:

```text
preprocess O(n log n)
query O(1)
no efficient updates
```

Segment tree:

```text
build O(n)
query O(log n)
update O(log n)
```

Nếu data không đổi, segment tree có thể là overkill.

Xem [Sparse Table](./05_sparse_table_and_static_range_queries.md).

## Fenwick vs Segment Tree

Fenwick:

```text
code ngắn
gọn memory
cache-friendly
excellent cho prefix sums/frequencies
less flexible aggregate/update model
```

Segment tree:

```text
flexible monoid aggregates
range updates với lazy
augmentation mạnh
code/memory phức tạp hơn
```

Không có structure “mạnh hơn nên luôn tốt hơn”. Chọn theo operations thực tế.

## Range Query Decision Guide

| Workload | Structure phù hợp |
|---|---|
| static range sum | Prefix Sum |
| many static range min/max | Sparse Table |
| point add + prefix/range sum | Fenwick Tree |
| dynamic frequency + rank/k-th | Fenwick Tree |
| point update + general associative range aggregate | Segment Tree |
| range update + range query | Lazy Segment Tree |
| sparse huge coordinate domain | Compression hoặc Implicit Segment Tree |
| historical versions | Persistent Segment Tree |

## Indexing bugs: 0-based vs 1-based

Fenwick thường tự nhiên với 1-based indexing vì `lowbit(0)=0` làm update loop không tiến nếu bắt đầu ở 0.

Một wrapper tốt có thể expose 0-based API nhưng convert nội bộ:

```text
external index i
internal index i+1
```

Đừng mix hai systems trong cùng formula.

Segment tree nên chọn rõ interval convention. Half-open `[L,R)` thường giảm off-by-one bugs và compose tự nhiên:

```text
[L,M) + [M,R) = [L,R)
```

## Overflow

Range sums dễ vượt 32-bit ngay cả khi mỗi element nhỏ.

Ví dụ `n = 100000`, mỗi value `10^9`:

\[
sum = 10^{14}
\]

Java cần `long`, C cần type đủ rộng như `int64_t` tùy domain. JavaScript `Number` chính xác integer tới `2^53-1`; lớn hơn có thể cần `BigInt`.

Lazy multiplication `delta * segmentLength` cũng phải dùng wide type trước khi multiply.

## Non-commutative combine

Nếu aggregate là matrix multiplication hoặc string/function composition, operation associative nhưng không commutative.

Query iterative không thể chỉ cộng arbitrary order. Phải giữ left and right accumulator đúng order:

```text
leftAgg  = combine(leftAgg, segment)
rightAgg = combine(segment, rightAgg)
```

Sau đó:

```text
combine(leftAgg, rightAgg)
```

Đây là lý do monoid mental model sâu hơn “segment tree dùng cho sum”.

## Testing Range Structures

Differential testing rất hiệu quả. Với `n` nhỏ, giữ plain array làm oracle.

Random operations:

```text
point update
range update
range query
```

Sau mỗi query, compare structure với brute-force array.

Invariants:

```text
Fenwick prefix(n) == total array sum
Segment parent == combine(children)
Lazy node value reflects pending tag semantically
Persistent old version không đổi sau new update
```

Boundary tests:

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

## Real-world connections

Range aggregation xuất hiện trong monitoring time series, event counts, analytics, scoreboards, inventory changes, computational geometry và database-like indexing.

Tuy nhiên production systems thường dùng B-trees, column stores, Fenwick-like structures, hierarchical aggregates hoặc segment trees tùy storage model. Classic DSA structures là mental primitives; actual system representation có thể thay đổi theo cache/page/distribution concerns.

## Mental Model mở rộng

> Range-query design là bài toán chọn **các đoạn chuẩn** sao cho update chạm ít summary và query ghép từ ít summary.

Prefix sum chọn mọi prefix nên query cực rẻ nhưng update đắt. Fenwick chọn binary suffix blocks để cân bằng point update/prefix query. Segment tree chọn hierarchy intervals để hỗ trợ aggregate linh hoạt và range updates.

Khi hiểu những decomposition này, bạn không còn cần học thuộc `i += i & -i` hay recursion tree như công thức rời rạc; bạn thấy chúng là các cách encode shared range information theo workload.