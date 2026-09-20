# Mô hình bộ nhớ trong C, Java và JavaScript
**Memory Model, References & Ownership / 메모리 모델, 참조와 소유권**

DSA cuối cùng phải tồn tại trong memory thật. Một linked list trên giấy chỉ là các node nối nhau bằng mũi tên; trong runtime, mỗi node phải nằm ở một vùng nhớ cụ thể, có metadata, lifetime, alignment và locality. Một array trên giấy chỉ là dãy phần tử; trong máy, contiguous layout cho phép CPU prefetch và index arithmetic rất khác pointer chasing.

Vì vậy khi học cấu trúc dữ liệu nâng cao, representation không chỉ quyết định Big-O. Nó còn quyết định allocation cost, cache behavior, garbage collection pressure, fragmentation, pointer/reference overhead và risk về lifetime.

## 1. Stack và Heap: mental model thực dụng

Ở mức DSA, ta có thể dùng một mental model đơn giản nhưng hữu ích.

**Call stack** chứa function frames: parameters, local state, return information và bookkeeping của lời gọi hàm. Recursive calls tạo thêm frames, nên recursion depth lớn có thể gây stack overflow.

**Heap** chứa dynamic allocations/objects có lifetime linh hoạt hơn call frame. Linked nodes, tree nodes, hash-table backing arrays hoặc objects Java/JavaScript thường sống ở heap theo abstraction runtime.

Implementation thật có thể tối ưu bằng escape analysis, scalar replacement, stack allocation nội bộ hoặc GC generations; nhưng khi reasoning về DSA, stack-vs-heap vẫn là model rất tốt để hiểu recursion và dynamic objects.

## 2. C: pointer là address-level abstraction

Trong C:

```c
int *a = malloc(100 * sizeof(int));
if (!a) return 1;

a[0] = 42;
free(a);
```

`a` giữ một pointer tới vùng memory được cấp phát. Programmer chịu trách nhiệm đảm bảo allocation tồn tại khi dereference và được release đúng lúc.

Sau `free(a)`, pointer value có thể vẫn còn nhưng vùng đó không còn thuộc object hợp lệ. Dereference sau free là **undefined behavior**.

C cho quyền kiểm soát representation rất trực tiếp, nhưng đổi lại ownership và lifetime phải được quản lý thủ công.

## 3. Ownership trong linked structures bằng C

Một linked list node điển hình:

```c
struct Node {
    int value;
    struct Node *next;
};
```

Mỗi node có thể được `malloc` riêng. Khi xóa list, ta phải đi qua từng node, lưu `next`, rồi `free` node hiện tại.

Nếu free node nhưng vẫn giữ một pointer khác trỏ tới nó, ta có dangling pointer. Nếu quên free node đã mất reference, memory leak xảy ra.

Vì vậy API C nên document rõ ai **owns** allocation và ai có trách nhiệm free. DSA implementation bằng C không chỉ là thuật toán; ownership contract là một phần correctness.

## 4. Pointer aliasing

Hai pointers có thể trỏ cùng một object:

```c
int x = 10;
int *p = &x;
int *q = &x;
*q = 20;
printf("%d", *p); // 20
```

Đây là **aliasing**. Mutation qua một alias được quan sát qua alias khác.

Aliasing làm reasoning khó hơn vì một function có thể mutate storage mà caller vẫn giữ pointer tới đó. Compiler optimization cũng phải quan tâm alias rules.

Trong data structures, sharing nodes giữa structures mà không có ownership model rõ rất dễ gây double-free hoặc mutation bugs.

## 5. Contiguous allocation trong C

Array:

```c
int *a = malloc(n * sizeof *a);
```

lưu elements liên tiếp về mặt logical allocation. Address `a+i` được tính trực tiếp từ base address và element size.

Random access vì thế `O(1)` với arithmetic đơn giản. Traversal còn có locality tốt vì nhiều neighboring elements cùng cache line.

Một array of structs:

```c
struct Point { float x, y; };
struct Point points[n];
```

khác cache behavior với array of pointers tới separately allocated Point objects.

Representation ở mức memory layout có thể ảnh hưởng performance lớn dù algorithmic complexity giống nhau.

## 6. Struct padding và alignment

C compiler có thể chèn padding giữa fields để đáp ứng alignment.

Ví dụ:

```c
struct X {
    char flag;
    long value;
};
```

size có thể lớn hơn tổng raw field sizes vì alignment padding.

Khi data structure có hàng triệu nodes, vài bytes padding mỗi node có thể thành nhiều megabytes. Field ordering và compact representation đôi khi quan trọng trong systems code.

Không nên micro-optimize vô căn cứ, nhưng phải hiểu `sizeof(struct)` mới là memory cost thật.

## 7. Java: reference semantics và Garbage Collection

Trong Java:

```java
Node a = new Node(10);
Node b = a;
b.value = 20;
System.out.println(a.value); // 20
```

`a` và `b` là references tới cùng một object. Assignment `b = a` không clone object.

Garbage collector reclaim object khi object không còn reachable từ GC roots theo model runtime. Programmer không gọi `free` thủ công như C.

GC loại bỏ nhiều use-after-free/double-free classes, nhưng không làm memory management “miễn phí”. Allocation, tracing/copying, compaction và pauses vẫn có cost.

## 8. Java memory leak vẫn tồn tại ở cấp logic

Nếu một cache giữ reference tới objects mãi mãi, GC không thể reclaim chúng vì chúng vẫn reachable.

Ví dụ static map không eviction:

```java
static final Map<String, Object> CACHE = new HashMap<>();
```

có thể tăng vô hạn.

Đây vẫn được gọi là memory leak trong application sense, dù không có quên `free`. Root cause là **unintended retention**, không phải manual deallocation failure.

## 9. Java object overhead

Một `Node` Java không chỉ chứa fields logic. Object thường có header, alignment padding và references có kích thước runtime-dependent.

Do đó linked list của boxed `Integer` có thể dùng memory nhiều hơn đáng kể so với primitive `int[]`.

`ArrayList<Integer>` còn có boxing: array chứa references tới `Integer` objects thay vì raw ints theo conceptual model thông thường.

Nếu DSA numerical lớn, primitive arrays như `int[]`, `long[]` thường compact và cache-friendly hơn collections boxed.

## 10. Java array vs object graph

`int[]` là contiguous primitive storage abstraction rất khác một `Node[]` mà mỗi entry trỏ tới Node object riêng.

Node array chứa contiguous references, nhưng targets có thể nằm ở nhiều nơi trong heap. Traversing references gây pointer chasing tương tự linked structure.

Một tree represented bằng parallel arrays `left[]`, `right[]`, `value[]` có thể locality tốt hơn object-per-node tree, dù API ít object-oriented hơn.

Đây là data-oriented design trade-off.

## 11. JavaScript object identity

JavaScript cũng có reference-like semantics cho objects:

```js
const a = { value: 10 };
const b = a;
b.value = 20;
console.log(a.value); // 20
```

Assignment không deep-copy object.

Arrays, Maps, Sets và plain objects đều là runtime-managed objects. Engine dùng garbage collection và có thể thay đổi physical representation dựa trên observed shapes/types.

Programmer không điều khiển layout như C, nhưng allocation pattern và retention vẫn ảnh hưởng memory/performance.

## 12. JavaScript primitive và object distinction

Primitive values như `number`, `boolean`, `bigint`, `string` có value semantics ở language level. Objects có identity.

```js
const x = { a: 1 };
const y = { a: 1 };
console.log(x === y); // false
```

Dù contents giống nhau, object identity khác.

Điều này quan trọng khi dùng object làm key của `Map` hoặc member của `Set`: equality theo object identity, không deep structural equality.

## 13. Closure và retention trong JavaScript

Closure có thể giữ variables sống lâu hơn lexical function call tưởng tượng.

Nếu event listener hoặc callback closure capture một large object và listener không được remove, object có thể vẫn reachable và không GC được.

Caches, global arrays, timers và DOM references cũng là nguồn retention.

Vì vậy “GC language” vẫn cần hiểu reachability graph.

## 14. Reachability graph là mental model của GC

Có thể hình dung heap objects là graph; GC roots là starting vertices. Object reachable từ roots được xem là live.

Nếu object A trỏ B và B trỏ A nhưng không object nào reachable từ root, cycle vẫn có thể được collect bởi tracing GC. Đây là khác reference counting đơn giản.

Mental model graph này liên kết trực tiếp với DSA graph traversal: mark phase về bản chất là reachability computation trên object graph.

## 15. Cache locality

CPU không đọc memory một byte tùy ý với cost đồng nhất. Data được tải qua cache lines. Khi truy cập `a[i]`, neighboring elements có thể được tải cùng line.

Array traversal:

```text
a[0], a[1], a[2], ...
```

có spatial locality mạnh.

Linked-list traversal:

```text
node -> next -> next -> ...
```

có thể nhảy qua nhiều heap regions, gây cache misses.

Do đó hai algorithms cùng `O(n)` có thể khác performance lớn.

## 16. Pointer chasing và memory-level parallelism

Linked list có dependency chain: phải đọc current node mới biết address next node. CPU khó prefetch nhiều bước nếu addresses unpredictable.

Array indices predictable hơn, cho phép hardware prefetch và vectorization dễ hơn.

Đây là lý do arrays/vectors thường được ưu tiên hơn linked lists trong high-performance code dù insert giữa về Big-O có vẻ kém hơn.

## 17. Allocation overhead

Object-per-node structure cần nhiều allocations. Allocation có thể gây allocator contention, metadata overhead, fragmentation hoặc GC pressure.

Arena/pool allocation trong C/C++ hoặc preallocated arrays có thể giảm overhead khi lifetime của nhiều nodes giống nhau.

Trong Java/JavaScript, giảm temporary object creation ở hot loops có thể giảm allocation rate và GC workload.

Nhưng optimization phải dựa trên profiling, không nên hy sinh clarity vô lý.

## 18. Fragmentation

Memory allocator có thể còn nhiều free regions nhưng không phù hợp contiguous request lớn. Đây là fragmentation.

External fragmentation thường liên quan các free blocks rời rạc; internal fragmentation là wasted space trong allocated block lớn hơn nhu cầu.

Data structure có many small variable-sized allocations có behavior khác fixed-size slab/arena.

## 19. Mutation qua reference trong ba ngôn ngữ

C:

```c
void set_first(int *a) {
    a[0] = 99;
}
```

Java:

```java
void setFirst(int[] a) {
    a[0] = 99;
}
```

JavaScript:

```js
function setFirst(a) {
  a[0] = 99;
}
```

Trong cả ba, storage caller quan sát được bị mutate. Nhưng mechanism và lifetime guarantees khác nhau.

C truyền pointer value. Java truyền reference value by value. JavaScript cũng truyền value; với object, value đó biểu diễn reference-like identity tới object.

Cụm “pass by reference” dễ gây hiểu sai nếu không tách language semantics và observable mutation.

## 20. Copy shallow vs deep

Copy array/object không nhất thiết copy nested objects.

JavaScript:

```js
const a = [{ x: 1 }];
const b = [...a];
b[0].x = 9;
console.log(a[0].x); // 9
```

Outer array khác, inner object shared.

Java `clone()`/copy constructors và C `memcpy` cũng có shallow-copy risks với pointers/references.

Persistent data structures khai thác controlled sharing; mutable structures lại có thể gặp alias bugs nếu sharing không intentional.

## 21. Recursion depth và explicit stack

Mỗi recursive call thường tiêu thụ stack frame.

Balanced tree DFS depth `O(log n)` thường an toàn hơn skewed tree depth `O(n)`. Graph DFS trên path dài `10^5` vertices có thể overflow stack trong Java/JavaScript và cả C tùy stack limit.

Đổi recursive DFS sang explicit stack chuyển control state từ call stack sang heap-backed/container memory mà ta quản lý được.

Algorithm vẫn là DFS; execution representation thay đổi.

## 22. Tail recursion không nên được giả định tùy tiện

Một số language/runtime có tail-call optimization trong những conditions nhất định, nhưng Java không guarantee general tail-call elimination. JavaScript specification/history và engine support cũng không nên được giả định như universal solution.

Nếu depth có thể lớn, explicit iterative design an toàn hơn dựa vào tail-call optimization không chắc chắn.

## 23. Numeric representation cũng là memory/correctness issue

C integer width phụ thuộc type/platform constraints; signed overflow có undefined behavior trong C chuẩn cho nhiều trường hợp.

Java `int` 32-bit signed và `long` 64-bit signed, overflow wrap theo two's-complement semantics của language.

JavaScript `Number` là IEEE-754 double; integer exactness chỉ đảm bảo tới:

\[
2^{53}-1
\]

BigInt cung cấp arbitrary-size integer semantics nhưng không trộn trực tiếp với Number arithmetic.

DSA cost/distance/count có thể sai nếu representation numeric không đủ.

## 24. False sharing và concurrency intuition

Trong concurrent code, hai threads update hai variables logic độc lập nhưng nằm cùng cache line có thể gây cache-coherence ping-pong, gọi là false sharing.

Đây là ví dụ memory layout ảnh hưởng parallel performance dù data dependency logic không tồn tại.

Concurrent queues, counters và graph algorithms cần nhìn beyond Big-O tới cache coherence/contention.

## 25. Structure-of-Arrays vs Array-of-Structures

Array of Structures:

```text
[{x,y,z}, {x,y,z}, ...]
```

Structure of Arrays:

```text
x[]
y[]
z[]
```

Nếu computation chỉ scan `x`, SoA có thể locality/vectorization tốt hơn vì không tải y/z không cần thiết. Nếu thường cần toàn record cùng lúc, AoS có thể convenient/local.

DSA implementation production đôi khi chọn physical layout theo access pattern, không chỉ abstract type.

## 26. External memory model

Khi data không vừa RAM, cost lớn không còn là CPU instruction mà là page/block I/O.

B+Tree tăng branching factor để giảm height và page reads. External merge sort đọc/ghi sequential runs thay vì random access. Buffering trở thành core design.

Điều này cho thấy complexity model phải phù hợp hardware layer. RAM model `O(log n)` chưa nói hết khi mỗi step có thể là disk seek.

## 27. Memory complexity phải tính overhead thật

Nói hash table `O(n)` memory và tree `O(n)` memory là đúng asymptotically nhưng không nói constants.

Hash table có spare capacity/load factor. Tree có parent/child pointers, balance metadata và object headers. Trie có nhiều child slots. Graph adjacency list có per-edge references/objects.

Khi `n` lớn, constants quyết định feasibility.

## 28. Persistent và immutable structures

Immutable/persistent structures không mutate version cũ; update tạo nodes mới và share phần không đổi.

Ví dụ persistent tree update một root-to-leaf path có thể copy `O(log n)` nodes thay vì copy whole tree.

Structural sharing an toàn hơn mutable aliasing nhưng tăng allocation. Functional languages và versioned algorithms khai thác trade-off này.

## 29. Benchmark memory-aware

Nếu hai structures cùng complexity, benchmark nên đo cả runtime và allocation/peak memory.

Linked list có thể thua array ở traversal. Object-heavy graph có thể thua compact CSR-style arrays. Hash map với boxed keys có thể tiêu thụ nhiều memory hơn primitive specialized map.

Performance claim chỉ đáng tin khi workload và representation cụ thể được đo.

## Mental Model

> Data structure là **algorithm + physical representation + lifetime model**.

Array mạnh không chỉ vì `O(1)` indexing mà còn locality. Linked structure linh hoạt không chỉ vì pointer rewiring mà còn phải trả allocation/pointer-chasing cost. GC loại bỏ manual `free` nhưng không loại allocation/retention cost. C cho quyền ownership trực tiếp; Java/JavaScript cho reachability-managed lifetime nhưng vẫn cần hiểu identity, aliasing và memory pressure.

Khi chọn structure, hãy hỏi cả bốn câu: operation complexity là gì, layout nằm thế nào trong memory, object sống bao lâu, và runtime/hardware sẽ truy cập representation đó ra sao.

Xem thêm: [Arrays & Dynamic Arrays](../01_linear_structures/00_arrays_and_dynamic_arrays.md), [Linked Lists](../01_linear_structures/01_linked_lists.md), [C Implementation Patterns](../80_language_implementations/00_c_dsa_implementation_patterns.md), [JavaScript Runtime Patterns](../80_language_implementations/02_javascript_dsa_runtime_patterns.md).