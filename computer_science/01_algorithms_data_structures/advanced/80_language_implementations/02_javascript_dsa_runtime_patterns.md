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
