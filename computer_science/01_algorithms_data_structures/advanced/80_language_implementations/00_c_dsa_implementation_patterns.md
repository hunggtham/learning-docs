# DSA Implementation Patterns trong C
**C 자료구조 구현 패턴**

C làm rõ representation và ownership, nên là ngôn ngữ rất tốt để học “chi phí thật” của DSA. Nhưng correctness không chỉ là algorithm; nó còn bao gồm memory safety.

## Ownership phải được thiết kế như một invariant

Một container lưu pointer có thể:

```text
own object
borrow object
copy value
```

API phải nói rõ. Nếu list “own” nodes nhưng values chỉ borrowed, destructor chỉ free nodes. Nếu values cũng owned, cần callback destructor hoặc policy cụ thể.

Không rõ ownership dẫn đến double-free, use-after-free hoặc leak.

## Generic container bằng void* hay macro?

`void *` cho runtime-generic container nhưng mất static type information và thường cần callbacks comparator/hash/destructor. Macro có thể generate typed code nhưng debugging/API complexity khác.

Đối với học DSA, typed implementation cho `int` trước thường giúp tập trung vào invariant; sau đó mới generalize.

## Allocation failure

Production-quality C không giả định `malloc` luôn thành công.

```c
Node *n = malloc(sizeof *n);
if (n == NULL) {
    return false;
}
```

Khi operation gồm nhiều allocations, cần nghĩ transactionally: nếu bước giữa thất bại, data structure cũ có còn valid không?

## Integer overflow

Khi allocate array:

```c
malloc(count * sizeof *ptr)
```

`count * sizeof` có thể overflow `size_t` trước allocation. Code robust kiểm tra boundary.

## Comparator

Comparator `a-b` có thể overflow signed integer. Pattern an toàn:

```c
return (a > b) - (a < b);
```

## Recursion depth

C stack không tự grow vô hạn. DFS/tree recursion trên input adversarial có thể overflow. Iterative stack nên được cân nhắc ở code hệ thống hoặc khi depth không bounded.

## Flexible arrays và contiguous allocation

Đôi khi node/header + data có thể allocate cùng block để giảm pointer indirection và allocations. Đây là optimization representation, nhưng chỉ nên làm khi profiler cho thấy đáng giá và alignment/lifetime được hiểu rõ.

## Sanitizers

Khi luyện implementation C, AddressSanitizer/UndefinedBehaviorSanitizer có giá trị lớn hơn chỉ test output. Algorithm có thể trả đúng sample nhưng vẫn out-of-bounds hoặc use-after-free.

## Mental Model

> Trong C, representation, algorithm và ownership là một khối. Data structure chỉ đúng khi **logical invariant + memory lifetime invariant** đều đúng.

## API design: caller cần biết điều gì?

Một container C tốt nên làm rõ:

```text
ai tạo và ai hủy container?
container có copy element hay giữ pointer?
operation nào invalidates pointer/iterator?
failure được báo bằng bool, enum hay NULL?
```

Dynamic array `realloc` có thể đổi base address, nên mọi pointer tới element cũ có thể invalid sau growth. Đây là semantic consequence trực tiếp của representation.

## `const` và mutation boundary

Nếu function chỉ đọc structure, dùng `const` khi API phù hợp:

```c
const Node *find(const Tree *tree, int key);
```

`const` không chứng minh toàn bộ immutability nhưng làm contract dễ thấy hơn và giúp compiler phát hiện một số mutation ngoài ý muốn.

## Layout: array of structs hay struct of arrays?

Array of Structs:

```c
typedef struct {
    float x, y, z;
    int id;
} Point;

Point points[n];
```

Struct of Arrays:

```c
float x[n], y[n], z[n];
int id[n];
```

Nếu algorithm chỉ quét `x`, SoA có thể sử dụng cache/SIMD tốt hơn vì không kéo fields không cần. Nếu thường cần toàn record cùng lúc, AoS có thể tự nhiên hơn.

Đây là ví dụ cost model thấp tầng ảnh hưởng data-structure design.

## Arena/pool allocation

Node-heavy trees/graphs có thể tạo rất nhiều `malloc` calls. Arena/pool allocator cấp block lớn rồi carve nodes nhỏ, giúp giảm allocator overhead và cải thiện locality. Trade-off là lifetime thường được gom chung và việc free từng node riêng khó hơn.

## Error-safe mutation

Giả sử grow vector cần allocation mới. Structure chỉ nên đổi `data/capacity` sau khi allocation thành công. Nếu mutation một nửa rồi return failure, invariant có thể hỏng.

Một pattern tốt là:

```text
prepare resources
validate success
commit structural change
```

gần với transactional thinking.

## Debugging invariant

Trong debug build có thể viết `validate_tree`, `validate_heap`, `validate_list` để scan structure và assert invariants sau random operations. Với C, đây rất hữu ích vì memory corruption có thể biểu hiện xa điểm gây lỗi.

## Mental Model mở rộng

> C buộc ta nhìn thấy rằng data structure có hai topology cùng lúc: topology logic của nodes/edges và topology vật lý của allocations/bytes. Performance và safety phụ thuộc cả hai.
