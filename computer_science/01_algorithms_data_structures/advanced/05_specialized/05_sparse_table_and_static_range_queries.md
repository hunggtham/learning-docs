# Sparse Table và Static Range Queries
**스파스 테이블과 정적 구간 질의**

Sparse Table là một structure dành cho workload rất cụ thể: **dữ liệu tĩnh (static data / 정적 데이터)** nhưng có rất nhiều range queries. Nếu array không update, ta có thể trả nhiều preprocessing và memory hơn để query sau đó cực nhanh.

Đây là cùng trade-off quen thuộc của DSA:

```text
ít mutation
+ nhiều repeated queries
→ preprocess mạnh
```

Sparse Table đặc biệt mạnh với các operation như minimum, maximum và GCD, nơi query có thể trả `O(1)` sau preprocessing `O(n log n)`.

## Power-of-two decomposition

Sparse Table lưu aggregate của mọi interval có length là power of two:

```text
st[k][i] = aggregate của đoạn bắt đầu tại i, length 2^k
```

Base:

```text
st[0][i] = a[i]
```

Transition:

\[
st[k][i] = combine(st[k-1][i], st[k-1][i + 2^{k-1}])
\]

Vì interval length `2^k` có thể chia thành hai halves length `2^(k-1)`.

Construction cần khoảng:

\[
O(n\log n)
\]

time và memory.

## Tại sao powers of two?

Mọi positive length có logarithmic representation theo powers of two. Precompute intervals tăng gấp đôi giúp ta reuse kết quả nhỏ để tạo block lớn.

Idea này xuất hiện nhiều nơi:

```text
binary lifting ancestors
exponentiation by squaring
segment-tree levels
sparse table
```

Powers of two không phải magic; chúng tạo hierarchy có số levels logarithmic.

## Java construction cho RMQ

```java
final class SparseMin {
    private final int[][] st;
    private final int[] log2;

    SparseMin(int[] a) {
        int n = a.length;

        log2 = new int[n + 1];
        for (int i = 2; i <= n; i++) {
            log2[i] = log2[i / 2] + 1;
        }

        int levels = n == 0 ? 0 : log2[n] + 1;
        st = new int[levels][n];

        if (n == 0) return;

        System.arraycopy(a, 0, st[0], 0, n);

        for (int k = 1; k < levels; k++) {
            int len = 1 << k;
            int half = len >> 1;

            for (int i = 0; i + len <= n; i++) {
                st[k][i] = Math.min(
                    st[k - 1][i],
                    st[k - 1][i + half]
                );
            }
        }
    }

    int min(int l, int r) { // inclusive
        int len = r - l + 1;
        int k = log2[len];
        return Math.min(
            st[k][l],
            st[k][r - (1 << k) + 1]
        );
    }
}
```

Precompute `floor(log2(x))` tránh floating-point logarithm trong query và làm semantics integer rõ ràng.

## O(1) RMQ nhờ idempotence

Cho range `[L,R]`, đặt:

\[
k = \lfloor \log_2(R-L+1) \rfloor
\]

Ta chọn hai blocks length `2^k`:

```text
[L ........ L+2^k-1]
        [R-2^k+1 ........ R]
```

Hai blocks có thể overlap. Với `min`:

\[
\min(x,x)=x
\]

nên việc một element xuất hiện ở cả hai blocks không thay result.

Property:

\[
f(x,x)=x
\]

được gọi là **idempotence / 멱등성**.

Min, max và GCD là các examples quan trọng.

Do đó query chỉ combine hai precomputed values → `O(1)`.

## Associative chưa đủ cho classic O(1) trick

Sum associative:

\[
(a+b)+c=a+(b+c)
\]

nhưng không idempotent:

\[
x+x\ne x
\]

Nếu hai blocks overlap, phần overlap bị double-count.

Vì vậy classic Sparse Table two-overlap query không hoạt động cho sum.

Đây là distinction cần hiểu rõ:

```text
associative -> dễ combine partition không overlap
idempotent  -> cho phép overlap mà result không đổi
```

## Sparse Table cho GCD

GCD idempotent:

\[
\gcd(x,x)=x
\]

nên query range GCD cũng `O(1)` bằng hai blocks overlap.

Điều này hữu ích trong number-theory range problems.

## Sparse Table cho AND/OR

Bitwise AND và OR cũng idempotent:

```text
x & x = x
x | x = x
```

nên có thể dùng same RMQ-style query technique.

Bitwise XOR không idempotent vì:

```text
x ^ x = 0
```

nên overlap trick không đúng.

## Non-overlapping decomposition

Ngay cả với associative non-idempotent operation, ordinary Sparse Table blocks vẫn có thể decompose range thành `O(log n)` disjoint power-of-two blocks.

Ví dụ sum:

```text
length 13 = 8 + 4 + 1
```

Query `O(log n)`.

Nhưng với static sum, prefix sum cho `O(1)` và memory `O(n)` nên sparse table thường không phải lựa chọn tốt.

## Disjoint Sparse Table

**Disjoint Sparse Table (DST)** hỗ trợ `O(1)` range query cho nhiều associative operations, kể cả sum.

Mental model khác classic sparse table.

Ở mỗi level, array được chia thành blocks. Quanh midpoint của mỗi block, preprocess:

```text
suffix aggregates bên trái midpoint
prefix aggregates bên phải midpoint
```

Với query `[L,R]`, tìm highest bit nơi `L` và `R` khác nhau. Level đó xác định một midpoint nằm giữa hai endpoints. Answer combine:

```text
suffix(L -> midpoint-1)
+ prefix(midpoint -> R)
```

Hai phần disjoint nên không cần idempotence.

Preprocessing vẫn khoảng `O(n log n)`, query `O(1)`.

DST phức tạp hơn và constants lớn hơn; dùng khi static associative queries thật sự cần extreme query speed.

## Sparse Table vs Prefix Sum

Static sum:

```text
Prefix Sum:
preprocess O(n)
query O(1)
memory O(n)
```

Sparse table không thắng.

Static min/max/GCD:

```text
Prefix Sum không áp dụng
Sparse Table:
preprocess O(n log n)
query O(1)
```

Data structure phải match algebra của operation.

## Sparse Table vs Segment Tree

Segment Tree:

```text
preprocess O(n)
query O(log n)
point update O(log n)
range update có thể hỗ trợ lazy
```

Sparse Table:

```text
preprocess O(n log n)
query O(1) với idempotent op
updates rất không phù hợp
```

Nếu có mutation, Segment Tree thường là choice tự nhiên hơn.

## Sparse Table vs Fenwick Tree

Fenwick Tree tối ưu prefix-like group operations và point updates:

```text
update O(log n)
prefix/range sum O(log n)
memory O(n)
```

Sparse Table tối ưu static idempotent queries.

Hai structures giải workload khác nhau; không nên chọn theo “cái nào advanced hơn”.

## Vì sao update đắt?

Một point update `a[p]` ảnh hưởng mọi precomputed block chứa `p`.

Ở level `k`, có thể có nhiều starting positions `i` sao cho interval `[i,i+2^k)` chứa `p`. Tổng số affected table entries không chỉ `O(log n)`.

Sparse table intentionally duplicates information để query nhanh. Mutation phá nhiều copies đó.

Đây là trade-off giữa **redundant preprocessing** và update cost.

## Memory layout

`st[k][i]` layout level-major như Java `int[][]` làm mỗi level contiguous logical array.

Query đọc hai cells cùng level. Construction scan sequentially.

Trong C có thể allocate flat buffer:

```c
st[k * n + i]
```

để giảm allocation overhead.

Java object-per-row overhead thường chấp nhận được, nhưng dataset rất lớn cần estimate memory.

## Memory estimation

Với `n = 1,000,000`, levels khoảng 20.

Nếu mỗi cell `int` 4 bytes:

```text
~20,000,000 ints
~80 MB raw numeric data
```

chưa tính array headers/references.

Nếu dùng `long`, raw data khoảng 160 MB.

Đây là lý do Sparse Table không “free” chỉ vì query nhanh.

## Precomputing logs

`log2[len]` array tốn `O(n)` thêm memory.

Alternative có thể dùng integer bit operation:

Java:

```java
int k = 31 - Integer.numberOfLeadingZeros(len);
```

JavaScript:

```js
const k = 31 - Math.clz32(len);
```

nhưng `Math.clz32` có 32-bit semantics. Với very large lengths, representation khác cần cân nhắc.

Choice là readability vs small memory saving/runtime detail.

## Empty array và invalid range

Production API phải định nghĩa:

```text
n = 0 xử lý thế nào?
L > R thì sao?
range out of bounds?
```

Competitive-programming implementation thường assume valid input; reusable library không nên.

## Inclusive vs half-open intervals

Sparse table examples thường dùng inclusive `[L,R]`, nhưng systems/codebase có thể prefer half-open `[L,R)`.

Half-open length:

```text
len = R - L
```

và right block starts at:

```text
R - 2^k
```

Hãy chọn một convention và giữ nhất quán. Mixing interval semantics là source off-by-one phổ biến.

## RMQ — Range Minimum Query

RMQ là một foundational problem:

```text
query(L,R) = minimum value/index trên interval
```

Sparse table cho static RMQ `O(1)` sau `O(n log n)` preprocess.

Nhưng RMQ còn có deeper algorithms đạt linear preprocessing + O(1) query bằng Cartesian Tree/LCA reductions. Đây là chủ đề lý thuyết nâng cao hơn.

Sparse table nổi bật vì implementation đơn giản và constants practical.

## RMQ và LCA

Lowest Common Ancestor trên static tree có thể reduce thành RMQ.

DFS Euler tour ghi sequence nodes và depths:

```text
node:  A B D B E B A C ...
depth: 0 1 2 1 2 1 0 1 ...
```

LCA của `u,v` là node có minimum depth giữa lần xuất hiện phù hợp của chúng trong Euler tour interval.

Pipeline:

```text
Tree
→ Euler tour
→ depth array
→ RMQ
→ Sparse Table
→ O(1) LCA query
```

Đây là example tuyệt đẹp của problem transformation.

## Cartesian Tree connection

Cartesian Tree của array giữ heap property theo value và inorder order theo original indices.

RMQ giữa two positions liên quan LCA của corresponding nodes trong Cartesian Tree.

Vì vậy RMQ, Cartesian Tree và LCA có equivalence sâu về structure.

## Static idempotent query như semilattice intuition

Min/max/GCD có algebraic properties phù hợp: associative + idempotent.

Không cần học lattice theory để dùng structure, nhưng biết algebra giúp chọn data structure đúng hơn:

```text
operation properties
→ decomposition strategy
→ query structure
```

Đây là tư duy tổng quát có ích cho Segment Tree monoid, Fenwick group-like prefix difference và sparse table idempotence.

## 2D Sparse Table

Static 2D range minimum có thể mở rộng sparse table theo hai dimensions:

```text
st[kx][ky][x][y]
```

Memory/preprocessing tăng mạnh khoảng `O(nm log n log m)`.

Query rectangle có thể combine bốn blocks nếu operation idempotent.

Practical only khi dimensions vừa phải và query volume rất lớn.

## Sparse Table trên strings/objects

Structure không bắt buộc numeric nếu combine operation deterministic và table storage feasible.

Ví dụ lưu index của minimum theo custom comparator thay vì value. Điều này hữu ích nếu cần trả original position.

Store index:

```text
st[k][i] = index của best element trong block
```

Combine compares `a[idx1]` và `a[idx2]`.

## Tie-breaking

Nếu range minimum cần earliest index khi values tie, comparator phải define:

```text
smaller value wins
if equal, smaller index wins
```

Tie semantics phải được encoded trong `combine`. Otherwise value đúng nhưng index result có thể không đúng specification.

## Offline queries vs Sparse Table

Nếu tất cả queries biết trước, có thể có offline algorithms khác mạnh hơn.

Ví dụ static RMQ offline có Tarjan LCA-like reductions hoặc Mo's algorithm cho query classes khác.

Sparse Table phù hợp khi muốn online query sau one-time preprocess và data static.

## Mo's Algorithm khác gì?

Mo's algorithm reorder offline range queries để minimize boundary movement. Nó hữu ích khi:

```text
add/remove element khỏi current range rẻ
operation không có simple prefix/segment structure
```

Complexity thường khoảng `O((n+q)sqrt(n))` style tùy variant.

Sparse Table là preprocessing-based online O(1) cho operation class hẹp hơn.

## Query volume và break-even

Sparse Table preprocess `O(n log n)` chỉ đáng giá nếu q lớn hoặc latency per query rất quan trọng.

Nếu chỉ vài RMQ queries, Segment Tree hoặc even scan có thể đủ tùy n.

DSA choice nên nhìn total lifecycle cost:

\[
preprocess + q\times query + updates\times update
\]

không chỉ fastest query complexity.

## Cache behavior

Query classic sparse table đọc hai positions. Rất ít memory accesses, tốt cho latency nhưng table lớn có thể vượt cache.

Preprocessing scan levels sequentially, khá cache-friendly.

Segment tree query chạm logarithmic nodes có pattern nhảy hơn.

Actual performance phụ thuộc n và memory hierarchy.

## JavaScript implementation caveat

Một `Array<Array<number>>` rất tiện nhưng memory overhead có thể lớn. Typed arrays:

```js
const st = Array.from({length: levels}, () => new Int32Array(n));
```

compact hơn nếu numeric range fit 32-bit.

Nếu values vượt range, `Float64Array` hoặc BigInt representation cần cân nhắc.

## C implementation caveat

Nếu `1 << k` dùng signed `int`, large shifts có thể overflow/undefined corners tùy context. Dùng correct unsigned/size type và ensure k within width.

Memory allocation `levels * n * sizeof(T)` cũng cần overflow check cho general-purpose library.

## Common misconceptions

“Sparse Table dùng cho mọi range query” — sai; strength chính là static data và operation properties phù hợp.

“Associative là đủ cho O(1) query” — sai với classic overlapping-block method; idempotence mới cho phép overlap.

“Update chỉ sửa O(log n) cells vì có log levels” — sai; một point thuộc nhiều intervals ở each level.

“Sparse Table luôn tốt hơn Segment Tree vì O(1)” — bỏ qua preprocessing, memory và mutation.

“Sum dùng hai block như min” — sai vì overlap double-count.

## Testing

Randomized differential test rất đơn giản:

```text
generate random array nhỏ
build sparse table
for random L,R:
    expected = scan range
    actual = sparse query
    compare
```

Test đặc biệt:

```text
length 1
range toàn array
power-of-two length
length ngay trên power-of-two
all values equal
duplicates/ties
negative values
```

Nếu lưu index, test tie-breaking separately.

## Mental Model

> Sparse Table là **memoization cho mọi interval power-of-two của dữ liệu tĩnh**. Với idempotent operation, một arbitrary range được cover bởi hai possibly-overlapping blocks nên query chỉ cần hai table reads. Query cực nhanh được mua bằng redundant preprocessing và memory, vì vậy structure này chỉ hợp workload ít/no updates và nhiều repeated queries.

Khi gặp range-query problem, hãy hỏi:

```text
Data có update không?
Operation associative không?
Operation idempotent không?
Query volume lớn tới mức nào?
Prefix Sum/Fenwick/Segment Tree đơn giản hơn không?
Memory O(n log n) có acceptable không?
Need online hay offline queries?
```

Xem thêm: [Range Queries — Fenwick & Segment Tree](./01_range_queries_fenwick_segment_tree.md), [Tree Foundations — LCA](../02_trees/00_tree_foundations.md), [Bit Manipulation](./02_bit_manipulation_and_bitsets.md).