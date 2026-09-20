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
