# Mảng và mảng động
**Array & Dynamic Array / 배열과 동적 배열**

Array là một trong những representation quan trọng nhất của Computer Science vì nó ánh xạ **vị trí logic** thành **vị trí vật lý** có thể tính được trực tiếp. Nếu phần tử có kích thước cố định `w` byte và vùng dữ liệu bắt đầu tại địa chỉ `B`, phần tử index `i` nằm tại:

\[
address(i)=B+i\cdot w
\]

Đây là nguồn gốc của **truy cập ngẫu nhiên (Random Access / 임의 접근)** `O(1)`: không cần lần theo chain hay search qua các phần tử trước đó. Từ primitive này, rất nhiều cấu trúc tưởng như “không phải array” thực chất vẫn được xây trên array: binary heap, hash table open addressing, ring buffer, Fenwick Tree, compact Segment Tree, CSR graph, bitmap và nhiều numeric data structures.

## 1. Fixed Array và Dynamic Array khác nhau ở đâu?

Một fixed array có capacity cố định sau khi được tạo.

C:

```c
int a[5] = {10, 20, 30, 40, 50};
```

Java:

```java
int[] a = {10, 20, 30, 40, 50};
```

Dynamic array thêm hai đại lượng:

```text
size      = số phần tử logic đang dùng
capacity  = số slot đã cấp phát
```

Invariant cốt lõi:

\[
0 \le size \le capacity
\]

Khi `size == capacity`, append tiếp theo phải grow backing storage. Một implementation thường cấp block mới lớn hơn, copy/move elements, rồi giải phóng block cũ.

## 2. Vì sao append có thể amortized O(1)?

Nếu mỗi lần đầy chỉ tăng capacity thêm 1, sequence `n` appends sẽ copy:

\[
1+2+3+\cdots+n=\Theta(n^2)
\]

Nếu tăng theo tỷ lệ, ví dụ nhân đôi:

```text
4 -> 8 -> 16 -> 32 -> ...
```

tổng số elements bị copy qua toàn sequence là geometric series:

\[
4+8+16+\cdots+\frac n2=O(n)
\]

Do đó `n` appends có total `O(n)` và amortized `O(1)` mỗi append.

Nhưng một append riêng lẻ vẫn có thể `O(n)`. Nếu ứng dụng cần tail latency ổn định, growth spike có thể quan trọng hơn amortized throughput.

## 3. Growth factor là trade-off memory và resize frequency

Nhân đôi capacity giảm số lần resize nhưng có thể để trống nhiều memory. Growth factor nhỏ hơn giảm slack nhưng tăng số lần copy.

Ta đang cân bằng:

```text
ít resize hơn      <->      memory waste nhiều hơn
```

Production library chọn factor dựa trên allocator/runtime assumptions chứ không phải có một hằng số “đúng tuyệt đối”.

Shrink cũng cần hysteresis. Nếu grow khi 100% full và shrink ngay khi usage < 100%, workload dao động có thể resize liên tục. Một policy thường shrink ở threshold thấp hơn đáng kể để tránh thrashing.

## 4. C implementation và transactional mutation

```c
typedef struct {
    int *data;
    size_t size;
    size_t capacity;
} IntVector;

bool vector_push(IntVector *v, int x) {
    if (v->size == v->capacity) {
        size_t new_cap = v->capacity == 0 ? 8 : v->capacity * 2;

        if (new_cap > SIZE_MAX / sizeof *v->data) {
            return false;
        }

        int *p = realloc(v->data, new_cap * sizeof *p);
        if (p == NULL) return false;

        v->data = p;
        v->capacity = new_cap;
    }

    v->data[v->size++] = x;
    return true;
}
```

Điểm quan trọng không chỉ là `realloc`. Operation phải giữ invariant nếu allocation fail. Ta chỉ commit `data/capacity/size` sau khi có resource mới hợp lệ.

Pattern này là **prepare → validate → commit** và xuất hiện trong rất nhiều mutable data structures.

## 5. Pointer/reference invalidation

Khi dynamic array grow, backing storage có thể đổi địa chỉ. Trong C, mọi pointer tới elements cũ có thể invalid. Trong C++, iterators/references của vector có invalidation rules cụ thể. Trong Java, caller không thấy raw element address nhưng structural modification vẫn có thể invalid iterator theo fail-fast semantics của collection.

Một API giữ pointer/reference lâu dài vào dynamic-array element phải hiểu rõ lifetime contract.

Đây là điểm khác node-based structures: linked-list node address có thể stable hơn nếu node không bị xóa, đổi lại locality kém hơn.

## 6. Insert giữa array vì sao O(n)?

Từ:

```text
[10, 20, 30, 40]
```

chèn `25` trước `30` yêu cầu dịch suffix:

```text
[10, 20, _, 30, 40]
         ↑
        25
```

Số elements phải move phụ thuộc khoảng cách từ insertion point tới cuối, worst-case `O(n)`.

Array mua `O(1)` random access bằng contiguous ordered layout; đổi lại structural edit ở giữa đắt.

## 7. Stable deletion và unstable deletion

Nếu xóa `a[i]` và phải giữ thứ tự, suffix phải shift trái: `O(n)`.

Nếu **không cần giữ order**, ta có thể:

```text
swap(a[i], a[size-1])
size--
```

và xóa `O(1)`.

Requirement “giữ order” tưởng nhỏ nhưng đổi complexity. Đây là bài học quan trọng khi thiết kế API: semantics quyết định structure, structure quyết định cost.

## 8. Array như một coordinate system

Index tạo một hệ tọa độ. Nhờ đó ta có thể biểu diễn nhiều structure bằng arithmetic thay vì pointer.

Binary heap:

```text
parent(i) = (i - 1) / 2
left(i)   = 2i + 1
right(i)  = 2i + 2
```

Matrix row-major:

\[
index(r,c)=r\cdot cols+c
\]

Fenwick Tree dùng bit arithmetic trên index. Segment Tree iterative dùng các vùng index riêng cho leaves/internal nodes.

Array mạnh không phải vì “đơn giản”, mà vì index arithmetic loại nhiều pointer metadata.

## 9. Cache locality và prefetch

CPU tải memory theo cache line. Sequential array scan có spatial locality: khi đọc `a[i]`, các phần tử kế tiếp thường đã nằm gần trong cache line. Hardware prefetcher cũng dễ dự đoán pattern tuyến tính.

Linked list traversal có cùng `O(n)` nhưng mỗi `next` có thể trỏ tới allocation xa, gây cache miss.

Vì vậy trong production, array-based structure thường thắng node-based structure ngay cả khi Big-O giống nhau.

## 10. AoS và SoA

**Array of Structs (AoS)**:

```c
typedef struct {
    float x, y, z;
    int id;
} Point;

Point points[n];
```

**Struct of Arrays (SoA)**:

```c
float x[n], y[n], z[n];
int id[n];
```

Nếu algorithm luôn dùng toàn record, AoS tự nhiên. Nếu hot loop chỉ đọc `x`, SoA tránh kéo fields không cần vào cache và có thể thuận lợi hơn cho SIMD.

Data-oriented design thường bắt đầu từ câu hỏi: **hot operation thực sự đọc những bytes nào?**

## 11. Dense, sparse và holey arrays trong JavaScript

JavaScript `Array` không phải C array. Engine có thể tối ưu dense packed arrays rất tốt, nhưng nếu tạo holes, gán index rất lớn hoặc trộn element kinds, representation có thể đổi.

```js
const a = [];
a[1_000_000] = 1;
```

`length` trở thành lớn nhưng số elements thực tế rất ít. Đây không phải cách tạo sparse numeric structure hiệu quả một cách tự động.

Với fixed-size numeric data, `Int32Array`, `Uint32Array`, `Float64Array` cho representation predictable hơn, nhưng range/coercion semantics phải phù hợp.

## 12. Java primitive arrays và boxed collections

`int[]` lưu primitive values. `Integer[]` hoặc `ArrayList<Integer>` lưu references tới boxed objects hoặc boxed values tùy runtime optimization, tạo footprint/GC khác.

Nếu Dijkstra, DP hoặc DSU có hàng triệu integers, `int[]`, `long[]`, `boolean[]` thường có cost model tốt hơn generic boxed collections.

Abstraction tiện lợi không xóa representation cost.

## 13. Multidimensional arrays và layout

Trong C, một rectangular array thường row-major. Trong Java, `int[][]` là array của array references, nên rows có thể là objects riêng và thậm chí ragged.

JavaScript nested arrays cũng là object graph, không phải một flat matrix bắt buộc.

Nếu cần numeric matrix lớn/cache-friendly, flat array + manual indexing thường cho layout predictable hơn:

```java
int idx = r * cols + c;
```

## 14. Prefix Sum: preprocessing đổi query cost

Với static array, prefix sum:

\[
P[i]=a_0+a_1+\cdots+a_{i-1}
\]

cho range sum:

\[
sum(L,R)=P[R+1]-P[L]
\]

Preprocess `O(n)`, mỗi query `O(1)`.

Đây là một pattern lớn: **trả cost trước để query về sau rẻ hơn**.

## 15. Difference Array: đảo chiều workload

Nếu có nhiều range updates rồi cuối cùng mới materialize values, difference array giúp mỗi update `O(1)`:

```text
diff[L] += delta
diff[R+1] -= delta
```

Prefix sum cuối cùng phục hồi effect của mọi updates.

Prefix sum tối ưu nhiều query trên data tĩnh. Difference array tối ưu nhiều batch updates trước reconstruction. Cùng array nhưng representation được chọn theo workload.

## 16. Two Pointers và order information

Sorted array cung cấp thông tin cho phép loại candidate.

```js
function twoSumSorted(a, target) {
  let l = 0, r = a.length - 1;
  while (l < r) {
    const s = a[l] + a[r];
    if (s === target) return [l, r];
    if (s < target) l++;
    else r--;
  }
  return null;
}
```

Nếu sum quá nhỏ, giữ `l` và giảm `r` chỉ làm sum nhỏ hơn hoặc bằng, nên không thể giải quyết vấn đề. Vì vậy tăng `l` là safe.

Technique này dựa trên order invariant chứ không phải chỉ “hai biến index”.

## 17. Sliding Window và state reuse

Window sum length `k`:

\[
S_{i+1}=S_i-a_i+a_{i+k}
\]

Mỗi transition chỉ cập nhật contribution rời/đến, thay vì tính lại cả window. Tổng từ `O(nk)` về `O(n)`.

General lesson: nếu hai subproblems liên tiếp overlap mạnh, hãy hỏi state nào có thể reuse.

## 18. Circular array và ring buffer

Nếu logical sequence quay vòng, modulo index cho phép reuse fixed storage:

\[
physical=(head+logicalIndex)\bmod capacity
\]

Ring buffer dùng array nhưng semantics giống queue. Nó tránh shift và cho memory bounded, rất phù hợp audio/network/telemetry buffers.

Nếu capacity là power of two, implementation thấp tầng đôi khi dùng bit mask thay modulo:

```text
index & (capacity - 1)
```

nhưng chỉ đúng khi assumptions được giữ.

## 19. Gap Buffer, Piece Table và Rope: khi insert giữa là workload chính

Text editor không nên luôn dùng một contiguous array và shift hàng megabytes cho mỗi keystroke. **Gap buffer** giữ một vùng trống quanh cursor để local insert nhanh. Piece table/rope dùng representation khác để hỗ trợ edit lớn hơn.

Bài học là: dynamic array là baseline, nhưng nếu workload có nhiều middle edits, representation cần thay đổi.

## 20. Small Vector Optimization và inline storage

Một số container tối ưu trường hợp size nhỏ bằng cách lưu vài elements trực tiếp trong object, chỉ allocate heap khi vượt threshold. Đây là **small-buffer/small-vector optimization**.

Nó giảm allocation cho common small case nhưng làm object lớn hơn và move/copy semantics phức tạp hơn.

Đây là ví dụ constants/memory layout thay đổi design dù asymptotic complexity giữ nguyên.

## 21. Persistent/immutable arrays và copy-on-write

Mutable array cho update index `O(1)` nhưng thay state tại chỗ. Trong immutable/persistent system, update phải tạo logical version mới.

Naive copy toàn array là `O(n)`. Persistent vector kiểu tree-of-arrays có thể update theo path `O(log_B n)` với branching factor lớn. Copy-on-write có thể trì hoãn copy cho tới khi một shared buffer cần mutation.

Khi requirement thêm versioning/immutability, “array update O(1)” không còn tự động đúng.

## 22. Aliasing và slice/view semantics

Một slice có thể là copy hoặc view lên backing array. Nếu là view, mutation backing storage có thể nhìn thấy qua slice và ngược lại.

C pointer + length gần như luôn là view. Java `Arrays.copyOfRange` tạo copy; NIO Buffer có view semantics khác. JavaScript `TypedArray.subarray()` tạo view, còn `slice()` thường copy theo API semantics tương ứng.

API phải nói rõ ownership/aliasing, nếu không correctness bug rất dễ xuất hiện.

## 23. False sharing trong concurrent arrays

Hai threads update hai counters khác nhau nhưng nằm cùng cache line có thể gây cache coherence traffic dù không tranh cùng logical variable. Đây là **false sharing**.

Một dense array rất tốt cho locality sequential, nhưng concurrent write pattern có thể cần padding/sharding để giảm cache-line contention.

Representation tối ưu cho single-thread không luôn tối ưu cho multi-thread.

## 24. Bounds, integer overflow và allocation safety

Trong C/system code, allocation:

```c
malloc(count * sizeof *ptr)
```

có thể overflow multiplication trước khi allocator được gọi. Index arithmetic `r * cols + c` cũng có thể overflow nếu dimensions lớn.

Trong Java/JavaScript, out-of-bounds semantics khác C nhưng integer/numeric range vẫn cần reasoning. JavaScript Number mất integer precision sau `2^53-1`; TypedArray có fixed-width wrap/coercion semantics.

## 25. Testing dynamic arrays bằng invariant

Sau mỗi mutation, các invariant có thể kiểm tra:

```text
0 <= size <= capacity
mọi element logic nằm trong [0, size)
append giữ prefix cũ
remove stable giữ relative order còn lại
reserve không đổi logical contents
resize failure không phá state cũ
```

Property test có thể so custom vector với reference list trên random operation sequence.

## 26. Khi nào array là lựa chọn tốt?

Array/dynamic array đặc biệt mạnh khi:

```text
random access quan trọng
append nhiều
iteration nhiều
memory locality quan trọng
size thay đổi nhưng middle insert không phải hot operation
```

Nếu node identity stable, frequent splice hoặc arbitrary insertion/removal đã biết vị trí là trọng tâm, linked/node-based structures có thể hợp hơn. Nếu ordered lookup/range query là trọng tâm, tree/index có thể phù hợp hơn.

## Mental Model

> Array là một **coordinate system contiguous cho dữ liệu**. Nó mua random access, locality và metadata thấp bằng việc ràng buộc thứ tự logic vào layout vật lý.

Dynamic array thêm một lớp amortization để layout có thể lớn lên. Từ đó, mọi trade-off — resize, invalidation, insert/delete, cache behavior, slices, concurrency — đều có thể suy ra từ cùng representation này.

Xem thêm: [Linked Lists](./01_linked_lists.md), [Queues/Deque](./03_queues_deques_and_priority_queues.md), [Range Queries](../05_specialized/01_range_queries_fenwick_segment_tree.md), [Memory Models](../00_foundations/03_memory_models_c_java_javascript.md).