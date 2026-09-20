# JavaScript Runtime Patterns cho DSA  
**JavaScript 자료구조와 런타임 패턴**

JavaScript cho phép viết DSA rất nhanh, nhưng một số habits từ C/Java không map 1:1 vì Number semantics, dynamic arrays và object model.

## Number và integer precision

JavaScript `Number` là IEEE-754 double. Integers chỉ được biểu diễn chính xác tới:

\[
2^{53}-1
\]

Nếu shortest-path cost, combinatorial count hoặc ID arithmetic vượt giới hạn, cần `BigInt` hoặc representation khác.

`BigInt` không trộn trực tiếp với `Number` trong arithmetic.

## Array làm stack tốt, queue cần chú ý

`push/pop` ở cuối là natural stack operations. Repeated `shift()` ở đầu có thể gây cost do reindex/representation; queue lớn nên dùng head index, deque implementation riêng hoặc library.

## Object vs Map

Plain object có property semantics, prototype và string/symbol keys. `Map` hỗ trợ arbitrary key identity và iteration semantics rõ hơn cho general DSA.

```js
const map = new Map();
map.set(objectKey, value);
```

## Set

`Set` là lựa chọn tự nhiên cho visited/membership, thay vì object hacks.

## Sort comparator

```js
[2, 10, 3].sort();
```

không nên dùng cho numeric intent. Hãy dùng:

```js
arr.sort((a, b) => a - b);
```

## Recursion depth

Deep DFS/backtracking có thể vượt maximum call stack. Iterative implementation là lựa chọn an toàn hơn khi depth có thể hàng chục nghìn/hàng trăm nghìn.

## TypedArray

`Int32Array`, `Uint32Array`, `Float64Array` cho fixed-size numeric storage với representation chặt hơn Array general-purpose. Với graph/DP numeric lớn, typed arrays có thể giảm memory và tăng predictability, nhưng fixed length và numeric type constraints phải phù hợp.

## Bitwise operators

Nhiều bitwise operators convert operands sang signed/unsigned 32-bit semantics. Vì vậy bitmask lớn hơn 31/32 bits cần cẩn thận; `BigInt` bitwise có thể là lựa chọn khác.

## Object allocation trong hot loops

Priority queue Dijkstra kiểu `{node, dist}` rất dễ viết nhưng tạo nhiều objects. Với workloads lớn, struct-of-arrays, tuples compact hoặc custom heap storage có thể giảm GC pressure. Chỉ tối ưu sau profiling.

## Mental Model

> JavaScript DSA vẫn dựa trên cùng invariants, nhưng cost model chịu ảnh hưởng dynamic runtime. Correctness trước; sau đó kiểm tra Number limits, recursion limits và collection semantics.

## Dense array, sparse array và holes

JavaScript Array cho phép:

```js
const a = [];
a[1_000_000] = 1;
```

Logical `length` trở thành rất lớn dù chỉ có ít properties/elements. Runtime có thể đổi representation để xử lý sparse shape. Vì vậy algorithm cần dense numeric storage không nên vô tình tạo holes bằng index jumps hoặc `delete a[i]`.

Nếu muốn bỏ element theo position và giữ dense semantics, dùng appropriate compaction/splice strategy với cost đã hiểu.

## `Map` identity và compound state

`Map` với object key dùng object identity:

```js
new Map().set({x: 1}, 'a').get({x: 1}); // undefined
```

Hai object literals khác identity dù fields bằng nhau. Với DP/graph state `(x,y,mask)`, cần canonical key như encoded integer/string, nested maps, hoặc explicit interning.

## `Number` và comparator arithmetic

`a - b` comparator phù hợp numeric values trong safe numeric domain, nhưng nếu values là `BigInt`, comparator phải dùng relational checks vì `BigInt` result không được dùng như Number comparator return một cách tùy tiện.

Khi algorithm dùng infinity sentinel, `Infinity` hữu ích cho Number distances; với `BigInt`, cần sentinel/state riêng vì không có `BigInt Infinity`.

## TypedArray trade-off

TypedArray có fixed length và typed coercion. `Int32Array` wrap theo 32-bit semantics, nên không phù hợp distance có thể vượt range. `Float64Array` cho Number semantics; `BigInt64Array` tồn tại nhưng arithmetic/API ecosystem khác.

Chọn typed array từ numeric range, không chỉ vì “nhanh hơn”.

## Queue với head index và compaction

```js
class Queue {
  constructor() {
    this.a = [];
    this.head = 0;
  }

  push(x) {
    this.a.push(x);
  }

  shift() {
    if (this.head === this.a.length) return undefined;
    const x = this.a[this.head++];

    if (this.head > 4096 && this.head * 2 > this.a.length) {
      this.a = this.a.slice(this.head);
      this.head = 0;
    }

    return x;
  }
}
```

Compaction threshold là engineering parameter; không cần copy sau mỗi dequeue.

## Recursion và async/event loop

Chuyển recursion sâu thành iterative stack giải quyết call-stack limit. Việc dùng `async`/Promise không tự biến recursive graph traversal thành stack-safe algorithm; nó thay scheduling semantics và thường thêm overhead.

## Benchmark JS runtime

JIT có warm-up, hidden-class/shape specialization và deoptimization. Microbenchmark cần chạy đủ iterations, tránh benchmark dead code, dùng realistic data shapes và kiểm tra memory/GC nếu structure object-heavy.

## Mental Model mở rộng

> JavaScript cho phép representation rất linh hoạt; chính vì vậy ta phải chủ động giữ data shape ổn định khi performance quan trọng. DSA invariant vẫn giống nhau, nhưng runtime representation có thể thay đổi dưới abstraction.
