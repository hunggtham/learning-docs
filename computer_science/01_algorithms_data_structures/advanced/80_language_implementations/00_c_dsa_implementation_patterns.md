# DSA Implementation Patterns trong C
**C 자료구조 구현 패턴**

C là ngôn ngữ rất tốt để học DSA vì nó làm lộ ra những thứ mà runtime cao cấp thường che: memory layout, pointer arithmetic, allocation, ownership, object lifetime và failure handling. Nhưng chính vì vậy, một data structure trong C chỉ được coi là “đúng” khi cả hai lớp invariant đều đúng:

```text
logical invariant của algorithm/data structure
+
memory lifetime / ownership invariant
```

Một heap có thể giữ đúng order property nhưng vẫn sai vì buffer overflow. Một linked list có thể traverse đúng sample nhưng vẫn chứa dangling pointer. Học DSA bằng C vì thế là học cả representation lẫn algorithm.

## Ownership phải là part của API contract

Một container lưu pointer có thể theo một trong ba semantic chính:

```text
own object
borrow object
copy object/value
```

Ví dụ list node chứa `void *value`. Khi destroy list, có free `value` không? Nếu container borrow pointer, không được free. Nếu own, phải free theo đúng allocator/destructor contract.

Một API general-purpose có thể nhận callback:

```c
typedef void (*destroy_fn)(void *);
```

Container giữ `destroy_fn` và gọi khi xóa element.

Nếu ownership không rõ, bug thường là:

```text
double free
use-after-free
memory leak
free sai allocator
```

## Rule “who allocates, who frees”

Một design tốt trả lời được:

```text
ai tạo container?
ai hủy container?
container có allocate nodes riêng không?
element storage thuộc caller hay container?
returned pointer sống tới khi nào?
operation nào invalidate pointer/iterator?
```

Đây là “lifetime API”, không phải documentation phụ.

## Dynamic array representation

Một vector cơ bản:

```c
typedef struct {
    int *data;
    size_t size;
    size_t capacity;
} IntVector;
```

Invariant:

```text
0 <= size <= capacity
data == NULL nếu capacity == 0 (theo convention)
valid elements nằm trong [0, size)
allocated storage đủ capacity elements
```

Append nếu `size == capacity` cần grow.

## Growth strategy và amortized O(1)

Nếu mỗi lần đầy chỉ tăng capacity thêm 1, sequence append có total copy cost quadratic.

Geometric growth:

```text
capacity *= 2
```

hoặc factor ~1.5 giúp append amortized `O(1)`.

C implementation phải tránh overflow:

```c
if (capacity > SIZE_MAX / 2) {
    // cannot double safely
}
```

và tránh overflow trong bytes:

```c
if (new_capacity > SIZE_MAX / sizeof *data) {
    // allocation size overflow
}
```

## `realloc` và pointer invalidation

`realloc` có thể move buffer.

```c
int *new_data = realloc(v->data, new_cap * sizeof *v->data);
if (!new_data) {
    return false;
}

v->data = new_data;
v->capacity = new_cap;
```

Không viết:

```c
v->data = realloc(v->data, ...);
```

nếu muốn preserve old pointer khi failure.

Sau successful growth, mọi pointer tới old elements có thể invalid vì base address đổi.

Đây là API semantic trực tiếp từ representation.

## Transactional mutation

Một mutation tốt thường theo pattern:

```text
prepare resources
validate success
commit structural change
```

Ví dụ insert vào hash table có resize:

```text
allocate new buckets
rehash thành công
sau đó swap pointer/capacity
free old buckets
```

Nếu mutation cập nhật half state rồi allocation fail, structure có thể corrupt.

Thinking transactionally giúp exception-safety-like reasoning trong C.

## Linked list node ownership

```c
typedef struct Node {
    int value;
    struct Node *next;
} Node;
```

Insert front:

```c
Node *n = malloc(sizeof *n);
if (!n) return false;

n->value = value;
n->next = list->head;
list->head = n;
list->size++;
```

Delete phải update links trước/đúng order rồi free đúng node.

Nếu caller giữ pointer tới deleted node, pointer đó invalid. API reusable nên document iterator/node invalidation.

## Doubly linked list invariant

Nếu node có `prev` và `next`, invariant mạnh hơn:

```text
n->next != NULL => n->next->prev == n
n->prev != NULL => n->prev->next == n
```

Bug thường đến từ quên update một chiều.

Debug validator nên assert cả hai directions.

## Sentinel nodes

Sentinel head/tail giảm special cases cho empty/first/last insertion.

Thay vì nhiều branch:

```text
if head == NULL
if deleting first
if deleting last
```

sentinel biến operations thành relink uniform.

Trade-off là thêm nodes/abstraction, nhưng code correctness thường tốt hơn.

## Stack/queue bằng array hay linked nodes?

Array stack thường locality tốt và đơn giản.

Linked stack cho growth từng node nhưng nhiều allocations/pointer chasing.

Queue có thể dùng circular buffer để tránh shifting.

```c
index = (index + 1) % capacity;
```

Nếu capacity power-of-two, có thể dùng mask:

```c
index = (index + 1) & (capacity - 1);
```

nhưng chỉ đúng khi invariant capacity là power-of-two.

Optimization phải đi kèm invariant rõ.

## Circular buffer invariant

Có nhiều design:

```text
head + size
head/tail + one-empty-slot
head/tail + full flag
```

Chọn một model và giữ nhất quán. Nhiều queue bugs đến từ mix hai conventions.

## Generic containers: `void *`

`void *` cho runtime genericity:

```c
typedef int (*compare_fn)(const void *, const void *);
```

BST, heap hoặc sort generic cần comparator.

Trade-off:

```text
mất static type safety
callback overhead
ownership callback phức tạp
casts nhiều hơn
```

Với DSA learning, typed `int` version trước rồi generalize thường tốt hơn.

## Genericity bằng macro

Macro có thể generate typed container code:

```text
VECTOR_DEFINE(int, IntVector)
VECTOR_DEFINE(double, DoubleVector)
```

Ưu điểm: type-specific, no `void *` cast.

Nhược điểm: macro debugging, error messages và compile-time code duplication.

C không có generics native nên đây là design trade-off thật.

## Comparator contract

Comparator không chỉ trả số âm/dương bất kỳ; nó phải consistent.

Tránh:

```c
return a - b;
```

vì signed overflow.

Safer:

```c
return (a > b) - (a < b);
```

Với struct, comparator phải tạo order transitive. Nếu comparator inconsistent, qsort/BST/heap semantics có thể sai khó đoán.

## `qsort` caveat

Standard `qsort` tiện nhưng comparator gọi qua function pointer và API `void *` có overhead/type-unsafety.

Trong hot numeric code, specialized sort có thể nhanh hơn. Nhưng custom sorting chỉ đáng nếu measurement yêu cầu; library qsort đủ cho nhiều workloads.

## Struct padding và alignment

```c
typedef struct {
    char flag;
    int value;
    void *next;
} Node;
```

Compiler có thể insert padding để alignment. `sizeof(Node)` có thể lớn hơn tổng field sizes.

Khi có hàng triệu nodes, padding ảnh hưởng memory footprint/cache.

Reorder fields đôi khi giảm padding, nhưng ABI/readability cũng quan trọng.

## Array of Structs vs Struct of Arrays

AoS:

```c
typedef struct {
    float x, y, z;
    int id;
} Point;

Point points[n];
```

SoA:

```c
float x[n];
float y[n];
float z[n];
int id[n];
```

Nếu algorithm thường đọc toàn record, AoS natural.

Nếu chỉ quét một field, SoA có thể cache/SIMD-friendly hơn.

Data layout nên match access pattern.

## Arena allocation

Node-heavy structures gọi `malloc` cho từng node có overhead và fragmentation.

Arena:

```text
allocate big block
carve nodes sequentially
free whole arena at once
```

Ưu điểm:

```text
fast allocation
better locality
simple bulk lifetime
```

Nhược điểm:

```text
khó free individual node
lifetime coarse
memory có thể giữ tới end of arena
```

AST/temporary graph/tree workloads rất hợp arena.

## Pool allocator

Nếu nodes fixed-size và cần reuse delete/insert, free-list pool có thể tái sử dụng slots.

```text
free node -> push vào free list
allocate node -> pop free list trước khi request new memory
```

Pool giữ stable addresses tốt hơn reallocating vector nhưng cần quản generations nếu external handles tồn tại.

## Handle thay raw pointer

Trong systems code, external users giữ raw pointer vào movable storage rất rủi ro.

Có thể dùng integer handle/index:

```text
handle -> slot
```

Nếu compaction/move xảy ra, mapping cập nhật nhưng public handle stable.

Generation counter giúp detect stale handles:

```text
(index, generation)
```

Game engines/ECS thường dùng idea này.

## Hash table layout

Separate chaining:

```text
bucket array -> linked/list entries
```

Open addressing:

```text
entries stored directly in table slots
```

Open addressing thường locality tốt hơn nhưng load factor/probing/deletion marker phức tạp.

C cho phép thấy rõ cache trade-off của hai designs.

## Tombstone trong open addressing

Delete không thể luôn set slot thành EMPTY vì search chain có thể bị cắt sớm.

Need states:

```text
EMPTY
OCCUPIED
DELETED/TOMBSTONE
```

Too many tombstones degrade probing, nên resize/rehash có thể cần dù table chưa full.

## Hash function và integer overflow

Unsigned overflow trong C có modulo semantics xác định; signed overflow undefined behavior.

Hash code nên dùng unsigned types khi relying on wraparound.

Understanding integer semantics là part của correct implementation.

## Recursion depth

Recursive DFS/tree code rất đẹp nhưng stack size hữu hạn.

Adversarial BST chain hoặc graph depth hàng trăm nghìn có thể crash.

Iterative stack:

```c
typedef struct {
    int *data;
    size_t size, capacity;
} IntStack;
```

cho phép memory grow trên heap và explicit failure handling.

## Function recursion vs manual stack

Manual stack còn cho phép lưu exactly state cần thiết thay vì full function frame. Điều này có thể giảm memory và giúp pause/resume traversal.

Nhưng code phức tạp hơn. Use when depth safety/control needed.

## Integer overflow trong algorithms

Shortest path:

```c
if (dist[u] != INF && dist[u] + w < dist[v])
```

có thể overflow nếu types/sentinel sai.

Use wider unsigned/signed type phù hợp và explicit guard.

C signed overflow là undefined behavior, không chỉ wrap predictable.

## `size_t` vs `int`

Array length/index general-purpose nên cân nhắc `size_t`, nhưng subtraction/negative sentinel trở nên tricky vì unsigned.

Không mix signed/unsigned tùy tiện:

```c
for (size_t i = n; i-- > 0; ) { ... }
```

cần pattern đúng để tránh underflow logic bugs.

## `const` như contract

Reader function:

```c
const Node *tree_find(const Tree *tree, int key);
```

cho thấy function không được mutate qua những pointers đó.

`const` không chứng minh deep immutability, nhưng giúp API intent rõ và compiler bắt accidental writes.

## `restrict`

Trong performance-critical code, `restrict` có thể cho compiler biết pointers không alias theo contract, giúp optimization.

Nhưng dùng sai `restrict` dẫn tới undefined behavior. Chỉ dùng khi ownership/aliasing semantics được hiểu chắc.

## Aliasing

Hai pointers có thể trỏ cùng object. Mutation qua một alias ảnh hưởng value đọc qua alias khác.

Compiler optimization và reasoning manual đều khó hơn khi aliasing uncontrolled.

C data structure API nên hạn chế expose mutable internal pointers nếu không cần.

## Iterator invalidation

Dynamic array growth invalidates element pointers.

Hash table resize invalidates bucket/internal pointers.

Linked list insertion thường không invalid node pointers khác, nhưng deletion invalid deleted node.

Tree rotations có thể giữ node addresses nhưng thay parent/child relations.

Document invalidation rules như C++ containers dù viết C library.

## Error codes

Bool đôi khi không đủ:

```c
typedef enum {
    DS_OK,
    DS_ERR_OOM,
    DS_ERR_NOT_FOUND,
    DS_ERR_INVALID
} DsResult;
```

Explicit errors giúp caller phân biệt allocation failure với semantic failure.

## Partial initialization và cleanup

Constructor-like function allocate nhiều resources:

```text
allocate struct
allocate buffer A
allocate buffer B
```

Nếu B fail, phải free A và struct.

Common `goto cleanup` pattern trong C có thể làm cleanup centralized và correct hơn nested branches.

## Destructor phải idempotent không?

Có thể design:

```c
void vector_destroy(Vector *v) {
    free(v->data);
    v->data = NULL;
    v->size = 0;
    v->capacity = 0;
}
```

Sau đó destroy lần hai relatively safe nếu `free(NULL)`.

Nhưng caller dùng object sau destroy vẫn semantic error. API contract cần rõ.

## Copy, move và clone semantics

C không có automatic copy constructors.

`Tree b = a;` chỉ shallow-copy pointers nếu struct contains pointers.

Nếu cả hai destroy, double-free.

Need explicit:

```text
clone/deep_copy
move/transfer ownership
borrow reference
```

Naming/API patterns giúp tránh accidental shallow copy.

## Stable address vs compact storage

Pointer-based nodes có stable addresses nhưng locality kém.

Index-based nodes trong vector compact hơn nhưng growth may move base pointer; indices vẫn stable nếu elements không reordered.

Choose based on external references and performance.

## Graph representation trong C

Object-per-edge linked lists dễ implement nhưng overhead lớn.

Compact representation:

```c
size_t offsets[n + 1];
int edges[m];
```

CSR rất phù hợp static graph.

Dynamic graph có thể dùng edge vectors per vertex hoặc pooled adjacency blocks.

## Flexible Array Member

C cho phép:

```c
typedef struct {
    size_t len;
    int data[];
} Block;
```

Allocate header + elements trong một block:

```c
malloc(sizeof(Block) + n * sizeof(int));
```

Giảm pointer indirection/allocation, nhưng size arithmetic phải overflow-safe.

## Intrusive data structures

Intrusive list/tree node embed link fields trong user object:

```c
typedef struct Task {
    int priority;
    struct Task *next;
} Task;
```

Không cần wrapper node allocation.

Trade-off là object tied to structure/layout và một object muốn ở nhiều lists cần multiple link fields.

Linux kernel dùng intrusive patterns rất nhiều.

## Sentinel value vs explicit state

Đừng dùng `0`, `-1` hoặc magic value làm “empty” nếu domain có thể chứa value đó.

Prefer explicit state/size/boolean where ambiguity possible.

Same lesson applies hash table tombstones và graph distance INF.

## Debug validators

Mỗi complex structure nên có debug-only validator.

Heap:

```text
for each child: parent <= child
```

BST:

```text
all keys inside allowed range
```

Linked list:

```text
size count matches traversal
prev/next symmetric
no unexpected cycle
```

Hash table:

```text
occupied count matches size
lookup finds every stored entry
```

Validate after random operation sequences.

## Sanitizers

Compiler sanitizers là cực kỳ hữu ích:

```text
AddressSanitizer   -> out-of-bounds/use-after-free
UndefinedBehaviorSanitizer -> signed overflow, invalid shifts, etc.
LeakSanitizer      -> leaks tùy platform/toolchain
```

Correct output không chứng minh memory-safe code.

## Valgrind và static analysis

Valgrind, compiler warnings, clang-tidy/static analyzers giúp tìm lifetime/initialization issues.

Compile với warnings mạnh:

```text
-Wall -Wextra -Wconversion ...
```

và treat warnings nghiêm túc trong learning projects.

## Fuzzing

Data structures rất hợp fuzzing:

```text
random sequence insert/delete/find
compare với simple reference model
run validators/sanitizers
```

Custom parser/tree/hash bugs thường lộ nhanh hơn manual tests.

## Differential testing

Ví dụ custom C heap có thể compare pop sequence với:

```text
copy data
qsort reference
```

Custom set có thể compare small input với sorted-array reference.

Reference chậm nhưng đơn giản là test oracle tốt.

## Benchmark đúng

Benchmark C phải compile optimization flags consistent:

```text
-O2 hoặc -O3
```

đồng thời tránh benchmark bị compiler optimize away.

Test multiple input shapes, warm caches/cold caches nếu relevant, và measure allocation separately nếu node-heavy.

## ABI và library boundaries

Nếu expose struct definition public, caller phụ thuộc layout. Nếu muốn encapsulation, header có thể forward-declare opaque type:

```c
typedef struct HashMap HashMap;
```

Implementation fields nằm trong `.c` file.

Opaque type cho phép đổi representation mà không đổi public API.

## Memory pool và thread safety

Custom allocator/pool không tự thread-safe. Nếu dùng concurrent, cần synchronization hoặc per-thread pools.

Thêm locks có cost/cache contention. Data structure design phải include concurrency model.

## Atomic operations không tự làm structure lock-free

Dùng `_Atomic` pointer chưa đủ để biến linked structure thành correct lock-free algorithm. ABA problem, memory reclamation/hazard pointers/epochs là advanced topics riêng.

Đừng “thêm atomic” vào pointer algorithm rồi assume thread safety.

## Common misconceptions

“C nhanh hơn vì gần hardware” không đảm bảo implementation nhanh; poor locality/malloc-heavy code có thể chậm hơn managed language arrays.

“free xong set local pointer NULL là hết dangling pointers” sai nếu còn aliases.

“malloc failure không cần xử lý trên desktop” không phù hợp reusable/system code.

“Big-O đúng thì implementation đúng” sai; UB/memory bug có thể phá mọi guarantee.

“Linked list insert O(1) nên nhanh hơn vector” bỏ qua search, allocator và cache locality.

## Một checklist implementation C

Trước khi coi data structure hoàn chỉnh:

```text
Representation invariant là gì?
Ownership/lifetime của từng pointer là gì?
Allocation failure có rollback safe không?
Size arithmetic có overflow không?
Pointers/iterators invalid khi nào?
Recursion depth có bounded không?
Comparator/hash contract đúng không?
Có validator và randomized test chưa?
Sanitizers chạy sạch chưa?
Benchmark có realistic workload không?
```

## Mental Model

> Trong C, một data structure tồn tại đồng thời ở hai thế giới: **logical topology** của keys/nodes/edges và **physical topology** của bytes/allocations/pointers. Correctness cần cả hai. Performance cũng cần cả hai: một algorithm asymptotically tốt vẫn có thể tệ nếu allocation dày, locality kém hoặc representation quá lớn.

Học DSA bằng C tốt nhất khi mỗi implementation không chỉ có `push`, `pop`, `find`, mà còn có:

```text
init/destroy
clear/clone nếu cần
error handling
ownership contract
invariant validator
random differential tests
sanitizer run
```

Khi đó C trở thành công cụ để hiểu sâu representation thay vì chỉ là syntax pointer.

Xem thêm: [Memory Models](../00_foundations/03_memory_models_c_java_javascript.md), [Cross-language Testing](./03_cross_language_testing_and_benchmarking.md).