# Sparse Table và Static Range Queries  
**스파스 테이블과 정적 구간 질의**

Nếu array không update và cần rất nhiều range minimum/maximum/GCD queries, ta có thể preprocess mạnh hơn Fenwick/segment tree.

## Power-of-two blocks

Sparse table lưu:

```text
st[k][i] = aggregate của đoạn length 2^k bắt đầu tại i
```

Base:

```text
st[0][i] = a[i]
```

Transition:

\[
st[k][i] = combine(st[k-1][i], st[k-1][i+2^{k-1}])
\]

Preprocessing `O(n log n)`.

## Idempotent operations và O(1) RMQ

Với min/max/gcd, operation idempotent theo nghĩa `f(x,x)=x`. Một range `[L,R]` có thể phủ bằng hai blocks length `2^k` có overlap:

```text
[L ........ L+2^k-1]
       [R-2^k+1 ........ R]
```

Chọn:

\[
k=\lfloor \log_2(R-L+1)\rfloor
\]

và:

\[
min(st[k][L], st[k][R-2^k+1])
\]

Overlap không làm sai vì `min(x,x)=x`. Query `O(1)`.

Sum không idempotent; overlap sẽ double-count, nên sparse table kiểu này không cho range sum O(1) bằng hai blocks overlap.

## Khi nào dùng?

Static array + rất nhiều min/max/gcd queries → sparse table.

Có updates → segment tree/Fenwick tùy operation.

Chỉ range sum static → prefix sum còn đơn giản và tốt hơn.

## Mental Model

> Sparse table trả memory `O(n log n)` để lưu aggregate của **mọi block power-of-two**, rồi ghép một query từ rất ít blocks.

## Construction trong Java

```java
class SparseMin {
    private final int[][] st;
    private final int[] log2;

    SparseMin(int[] a) {
        int n = a.length;

        log2 = new int[n + 1];
        for (int i = 2; i <= n; i++) {
            log2[i] = log2[i / 2] + 1;
        }

        int levels = log2[n] + 1;
        st = new int[levels][n];

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
        return Math.min(st[k][l], st[k][r - (1 << k) + 1]);
    }
}
```

Precomputing floor-log giúp query không cần gọi floating-point logarithm.

## Vì sao hai blocks được phép overlap?

Với `min`, nếu một element nằm trong cả hai blocks, lấy nó hai lần không đổi result:

\[
\min(x,x)=x
\]

Property này gọi là **idempotence / 멱등성**. Max và GCD cũng có property tương tự.

Sum associative nhưng không idempotent:

\[
x+x \ne x
\]

nên two-overlapping-block trick sẽ double-count.

## Disjoint Sparse Table

Có một biến thể **Disjoint Sparse Table** hỗ trợ `O(1)` query cho nhiều associative operations, kể cả sum, bằng cách precompute prefix/suffix aggregates quanh boundaries của power-of-two blocks. Construction và constant factors phức tạp hơn, nhưng nó cho thấy limitation của classic sparse table là do cách decomposition, không phải mọi static associative query đều bắt buộc `O(log n)`.

## RMQ và LCA

Range Minimum Query có connection sâu với Lowest Common Ancestor. Euler tour một tree tạo sequence depths; LCA của hai nodes có thể được chuyển thành RMQ trên depth interval giữa lần xuất hiện của chúng. Sparse table sau preprocessing trả RMQ `O(1)` cho static tree.

Đây là một ví dụ knowledge graph:

```text
Tree traversal
    ↓
Euler tour
    ↓
array of depths
    ↓
RMQ
    ↓
Sparse Table
```

## Tại sao update làm sparse table không phù hợp?

Một point update có thể ảnh hưởng `O(log n)` levels nhưng ở mỗi level nó nằm trong nhiều starting blocks; sửa đầy đủ có thể rất đắt. Sparse table cố tình tối ưu **static-data workload** bằng preprocessing dày.

Nếu updates xuất hiện, segment tree hoặc Fenwick tree thường có cost model phù hợp hơn.

## Mental Model mở rộng

> Sparse table là memoization có hệ thống cho mọi power-of-two interval của dữ liệu tĩnh. Nó mạnh vì query workload lặp lại còn dữ liệu không thay đổi.
