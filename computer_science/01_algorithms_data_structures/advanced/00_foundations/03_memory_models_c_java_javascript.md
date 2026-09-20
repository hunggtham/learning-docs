# Mô hình bộ nhớ trong C, Java và JavaScript
**Memory Model, References & Ownership / 메모리 모델, 참조와 소유권**

DSA cuối cùng phải sống trong memory. Vì vậy representation không chỉ là hình vẽ; nó quyết định locality, allocation, pointer/reference overhead và lifetime.

## Stack và heap như mô hình thực dụng

Ở mức học DSA, có thể hiểu call stack lưu function frames, còn heap lưu dynamic objects/allocations có lifetime linh hoạt hơn. Runtime thực tế có thể tối ưu mạnh hơn, nhưng mental model này đủ để reasoning về recursion và data structure.

## C: pointer và ownership

```c
int *a = malloc(100 * sizeof(int));
if (!a) return 1;
a[0] = 42;
free(a);
```

Pointer `a` giữ address. Sau `free`, dereference vùng đó là undefined behavior. Với linked structures, mỗi node thường là allocation riêng, nên ta phải quản lý lifecycle rõ ràng.

## Java: reference và garbage collection

```java
Node a = new Node(10);
Node b = a;
b.value = 20;
```

`a` và `b` cùng tham chiếu một object. Garbage collector giải phóng object khi không còn reachable từ GC roots. Điều này giảm lỗi `free`, nhưng memory leak ở mức ứng dụng vẫn có thể xảy ra nếu collection/cache giữ references vô hạn.

## JavaScript: object identity

```js
const a = { value: 10 };
const b = a;
b.value = 20;
console.log(a.value); // 20
```

Object có reference semantics quan sát được. Runtime cũng dùng GC; closure, event listener hoặc cache có thể giữ object sống lâu hơn mong muốn.

## Contiguous memory và cache locality

Array có spatial locality tốt. Khi CPU nạp một cache line, nhiều elements lân cận thường đi kèm. Linked list phải follow pointers tới các vùng heap có thể rời rạc, nên traversal `O(n)` có thể chậm đáng kể hơn array traversal cùng Big-O.

Đây là lý do “linked list insert O(1)” chưa đủ để kết luận nó tốt hơn. Nếu phải traverse `O(n)` để tìm vị trí, tổng operation vẫn `O(n)`, và còn thêm allocation/locality cost.

## Mutation qua reference

C:

```c
void set_first(int *a) { a[0] = 99; }
```

Java:

```java
void setFirst(int[] a) { a[0] = 99; }
```

JavaScript:

```js
function setFirst(a) { a[0] = 99; }
```

Trong cả ba, storage mà caller quan sát được bị mutate, dù language mechanism khác nhau.

## Recursion depth

Mỗi recursive call thường dùng một stack frame. Graph/tree rất sâu có thể gây stack overflow. Vì vậy DFS recursive đôi khi cần đổi sang explicit stack, đặc biệt khi input depth không kiểm soát được.

## Mental Model

> Array tối ưu cho indexing và locality. Linked structure tối ưu cho local rewiring. Garbage collection tự động reclaim memory, nhưng không làm allocation hay retention trở thành miễn phí.
