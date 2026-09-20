# Range Queries: Prefix Sum, Fenwick Tree và Segment Tree
**구간 쿼리, 펜윅 트리, 세그먼트 트리**

Nếu có nhiều query như `sum(L,R)`, `min(L,R)`, quét đoạn mỗi lần là `O(n)`. Ta có thể precompute hoặc duy trì aggregates của các đoạn chuẩn.

## Prefix sum

\[
P[i]=a_0+a_1+\cdots+a_{i-1}
\]

thì:

\[
sum(L,R)=P[R+1]-P[L]
\]

Preprocess `O(n)`, query `O(1)`. Nhưng point update có thể làm nhiều prefix values thay đổi, `O(n)`.

## Fenwick Tree

Fenwick/Binary Indexed Tree cho point update và prefix sum đều `O(log n)`.

Core movement:

```text
i += i & -i
i -= i & -i
```

`i & -i` lấy least significant set bit, đại diện block size mà Fenwick node quản lý.

```java
class Fenwick {
    long[] bit;
    Fenwick(int n) { bit = new long[n+1]; }
    void add(int i, long delta) {
        for (; i < bit.length; i += i & -i) bit[i] += delta;
    }
    long sum(int i) {
        long s = 0;
        for (; i > 0; i -= i & -i) s += bit[i];
        return s;
    }
}
```

## Segment Tree

Segment tree chia range thành hierarchy. Root quản toàn range, children quản hai halves. Point update và associative range query như sum/min/max thường `O(log n)`.

## Lazy propagation

Range update trên từng element sẽ `O(n)`. Lazy propagation lưu pending operation ở node và chỉ đẩy xuống khi cần, giúp nhiều range update/query còn `O(log n)` trong các supported operation models.

## Chọn structure

Static range sum → prefix sum. Point update + prefix/range sum → Fenwick đơn giản và memory gọn. Flexible aggregate/range updates → segment tree.

## Mental Model

> Range-query structure lưu sẵn aggregates của các đoạn chuẩn để query tùy ý được ghép từ ít đoạn thay vì đọc từng element.

## Segment tree invariant

Mỗi node quản một interval `[l,r]` và lưu aggregate đúng của interval đó. Nếu operation có tính associative, parent aggregate có thể combine từ children:

\[
value(parent)=combine(value(left),value(right))
\]

Associativity quan trọng vì một query range sẽ bị chia thành nhiều canonical segments; kết quả không được phụ thuộc cách group segments.

## JavaScript segment tree cho sum

```js
class SegmentTree {
  constructor(a) {
    this.n = 1;
    while (this.n < a.length) this.n <<= 1;
    this.t = Array(this.n * 2).fill(0);

    for (let i = 0; i < a.length; i++) this.t[this.n + i] = a[i];
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
    let ansL = 0, ansR = 0;
    for (l += this.n, r += this.n; l < r; l >>= 1, r >>= 1) {
      if (l & 1) ansL += this.t[l++];
      if (r & 1) ansR = this.t[--r] + ansR;
    }
    return ansL + ansR;
  }
}
```

Dùng half-open interval `[l,r)` giúp boundary composition sạch hơn.

## Lazy propagation invariant

Node có `lazy` tag nghĩa là update đã được áp dụng logic cho toàn segment của node nhưng chưa đẩy xuống children. Trước khi descend, `push()` materialize effect xuống children.

Correctness phụ thuộc việc `node.value` luôn phản ánh aggregate hiện tại của segment kể cả khi children chưa được cập nhật vật lý.

## Monoid connection

Segment tree thực chất làm việc tốt với một **monoid**: một associative operation + identity element.

Sum: operation `+`, identity `0`.

Min: operation `min`, identity `+infinity`.

GCD: operation `gcd`, identity phù hợp `0`.

Không cần học abstract algebra để dùng segment tree, nhưng mental model này giải thích vì sao cùng framework có thể thay aggregate function mà vẫn đúng.
