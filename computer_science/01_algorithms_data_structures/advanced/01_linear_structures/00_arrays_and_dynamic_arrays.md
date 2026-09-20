# Mảng và mảng động
**Array & Dynamic Array / 배열과 동적 배열**

Array là cấu trúc nền tảng vì nó biến vị trí logic thành một phép tính địa chỉ. Nếu mỗi phần tử chiếm `w` byte và phần tử đầu bắt đầu tại địa chỉ `B`, phần tử index `i` nằm gần như tại:

\[
address(i)=B+i\cdot w
\]

Đây là lý do **truy cập ngẫu nhiên (Random Access / 임의 접근)** theo index có thể `O(1)`: không cần đi qua các phần tử trước đó.

## Fixed array và dynamic array

C array cố định:

```c
int a[5] = {10, 20, 30, 40, 50};
printf("%d\n", a[3]);
```

Java array:

```java
int[] a = {10, 20, 30, 40, 50};
System.out.println(a[3]);
```

JavaScript:

```js
const a = [10, 20, 30, 40, 50];
console.log(a[3]);
```

JS Array có semantics động và runtime representation phức tạp hơn C array, nhưng dense indexing vẫn thường gần constant-time trong use case thông thường.

Dynamic array thêm hai khái niệm quan trọng: `size` là số phần tử logic đang dùng; `capacity` là số slot đã cấp phát. Khi `size == capacity`, cấu trúc phải grow, thường bằng cách cấp vùng lớn hơn và copy elements.

C implementation tối giản:

```c
typedef struct {
    int *data;
    size_t size;
    size_t capacity;
} IntVector;

int vector_push(IntVector *v, int x) {
    if (v->size == v->capacity) {
        size_t new_cap = v->capacity == 0 ? 4 : v->capacity * 2;
        int *p = realloc(v->data, new_cap * sizeof(int));
        if (!p) return 0;
        v->data = p;
        v->capacity = new_cap;
    }
    v->data[v->size++] = x;
    return 1;
}
```

Java `ArrayList` và JavaScript `Array` che giấu mechanics này, nhưng amortized analysis vẫn giải thích vì sao append thường hiệu quả.

## Tại sao insert giữa array là O(n)?

Từ:

```text
[10, 20, 30, 40]
```

chèn `25` trước `30` đòi hỏi dịch suffix:

```text
[10, 20, 25, 30, 40]
```

Array mua random access nhanh bằng contiguous/order-by-index representation, và trả giá khi thay đổi cấu trúc ở giữa.

## Two pointers

Sorted array cho phép loại candidate bằng order invariant. Tìm hai số có tổng target:

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

Nếu tổng quá nhỏ, tăng `l` là safe vì mọi cặp dùng phần tử còn nhỏ hơn ở trái không thể cải thiện đủ. Complexity từ `O(n²)` brute force xuống `O(n)`.

## Sliding window

Khi bài toán xét các đoạn liên tiếp, sliding window tái sử dụng state cũ. Với window sum độ dài `k`:

\[
S_{i+1}=S_i-a_i+a_{i+k}
\]

Ta không tính lại `k` phần tử cho mỗi cửa sổ, nên tổng `O(n)` thay vì `O(nk)`.

## Cache locality

Sequential traversal array thường rất nhanh vì CPU cache hoạt động theo block. Đây là lý do array/dynamic array là baseline tốt cho nhiều workload, ngay cả khi một linked structure có cùng Big-O trên giấy.

## Mental Model

> Array là một hệ tọa độ cho dữ liệu: index cho ta vị trí. Khi giữ dữ liệu theo tọa độ, access rẻ nhưng insert/delete giữa đắt.

## Common misconceptions

`push()` dynamic array không phải worst-case `O(1)` mà là **amortized `O(1)`**. Insert linked list cũng không tự động `O(1)` nếu trước tiên phải search `O(n)` để tìm vị trí.

Xem thêm: [Linked Lists](./01_linked_lists.md), [Searching](../04_algorithmic_paradigms/00_searching.md), [Sorting](../04_algorithmic_paradigms/01_sorting.md).

## Memory layout trong ba ngôn ngữ

Trong C, `int a[n]` biểu diễn trực tiếp một vùng các `int` contiguous. Pointer arithmetic phản ánh chính layout đó:

```c
*(a + i) == a[i]
```

Trong Java, `int[]` là object array của primitive values với contiguous logical storage do JVM quản lý. `Integer[]` lại lưu references tới objects, nên cost model khác: thêm indirection, có thể boxing/unboxing và footprint lớn hơn.

Trong JavaScript, array là một object có array semantics. Engine thường giữ dense arrays trong optimized element storage, nhưng nếu ta tạo nhiều holes, trộn kiểu dữ liệu hoặc gán index rất lớn, representation nội bộ có thể chuyển sang dạng kém tối ưu. DSA reasoning nên dựa trên standard semantics; performance-critical JS nên benchmark engine thật.

## Remove và stable/unstable deletion

Nếu cần xóa `a[i]` nhưng **không cần giữ order**, có một kỹ thuật quan trọng:

```text
swap a[i] với a[size-1]
size--
```

Deletion trở thành `O(1)`. Nếu cần giữ order, phải shift tail và cost `O(n)`.

Đây minh họa nguyên tắc xuyên suốt DSA: **một requirement tưởng nhỏ như “giữ thứ tự” có thể đổi complexity của operation**.

## Matrix và row-major layout

Mảng hai chiều thường được linearize. Với matrix `rows x cols`, row-major address của `(r,c)` có dạng:

\[
index=r\cdot cols+c
\]

Vì vậy traversal theo row thường cache-friendly hơn traversal theo column trong layout row-major.

C:

```c
for (int r = 0; r < rows; ++r)
    for (int c = 0; c < cols; ++c)
        sum += a[r][c];
```

Connection này trở nên quan trọng trong image processing, numerical computing và DP table lớn.

## Difference array

Prefix sum trả lời query nhanh khi data tĩnh. Nếu bài toán là nhiều **range updates** rồi cuối cùng mới cần values, difference array đảo hướng reasoning.

Muốn cộng `delta` cho `[L,R]`:

```text
diff[L] += delta
diff[R+1] -= delta
```

Sau tất cả updates, prefix sum của `diff` phục hồi giá trị cộng dồn tại mỗi index.

Mỗi range update `O(1)`, reconstruction `O(n)`. Đây là ví dụ kinh điển về việc đổi representation để đổi operation cost.

## Edge cases thường gây lỗi

Với C, overflow khi tính allocation size `capacity * sizeof(T)` phải được cân nhắc ở code hệ thống. Với mọi ngôn ngữ, empty array, one-element array và index boundary là nơi invariant thường vỡ. Khi resize, không được tăng `size` nếu allocation thất bại; nếu dùng `realloc`, nên giữ pointer cũ cho tới khi biết allocation mới thành công.

## Connection: arrays là nền của nhiều cấu trúc “không giống array”

Heap, Fenwick Tree, Segment Tree compact implementation, adjacency list dạng CSR, hash table open addressing và ring buffer đều tận dụng array. Học array sâu vì vậy không phải học một cấu trúc đơn giản; nó là học primitive representation mà rất nhiều structure khác xây lên.
