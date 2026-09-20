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
