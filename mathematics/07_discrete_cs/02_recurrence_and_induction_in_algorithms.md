# Recurrence, induction và đệ quy trong thuật toán

Đệ quy (Recursion / 재귀) trong code và quan hệ truy hồi (Recurrence / 점화식) trong toán mô tả cùng một pattern: một problem/state được định nghĩa từ versions nhỏ hơn của chính nó. Mathematical induction là công cụ tự nhiên để chứng minh recursive structure đúng.

## Recursion needs a decreasing measure

Một recursive algorithm cần base case và một measure tiến dần về base. Ví dụ factorial:

```math
n!=n(n-1)!
```

với `0!=1`.

Code:

```text
factorial(n):
    if n == 0: return 1
    return n * factorial(n-1)
```

Correctness proof mirrors definition.

## Strong induction

Strong induction giả sử property đúng cho mọi sizes nhỏ hơn `n` để chứng minh size `n`. Divide-and-conquer thường hợp với form này vì subproblems có sizes không chỉ `n-1`.

## Recurrence for runtime

Binary search:

```math
T(n)=T(n/2)+c
```

Unroll:

```math
T(n)=T(n/2^k)+kc
```

base khi `n/2^k≈1`, nên `k≈log_2n`, cho `O(log n)`.

Merge sort:

```math
T(n)=2T(n/2)+cn
```

recursion tree có `log n` levels và each level total work `cn`, nên `O(n log n)`.

## Fibonacci and overlapping subproblems

Naive recursion:

```math
F_n=F_{n-1}+F_{n-2}
```

recomputes same values nhiều lần, tạo exponential call tree. Memoization stores solved states, reducing to linear number distinct subproblems.

Dynamic programming vì vậy là recurrence + caching/order of evaluation.

## Loop invariants as induction

Một loop chạy iterations `0,1,...`. To prove property after every iteration:

1. initialization: property đúng trước first iteration;
2. maintenance: nếu đúng trước iteration, vẫn đúng sau;
3. termination: khi loop dừng, invariant + stop condition imply desired result.

Đây chính là induction trên iteration count.

## Structural induction

Với recursive data structures như trees, proof có thể induction trên structure. Base leaf; inductive step assume property cho subtrees rồi prove parent.

Compiler AST transformations, JSON trees và expression evaluators thường được reason theo cách này.

## Termination

Correct output không đủ nếu algorithm không terminate. Một common proof tìm ranking function/variant giảm theo well-founded order và không thể giảm vô hạn.

Ví dụ Euclidean gcd algorithm:

```math
gcd(a,b)=gcd(b,a\bmod b)
```

remainder luôn nhỏ hơn `b` và nonnegative, nên eventually reaches 0.

## Mental Model

> Recursion là self-similarity trong computation; recurrence là self-similarity trong equations; induction là self-similarity trong proof. Ba thứ là những mặt khác nhau của cùng structure “giải size lớn bằng cases nhỏ hơn”.

## Common Misconceptions

Recursive code không tự động chậm; vấn đề là repeated work và stack overhead. Memoization không thay đổi recurrence semantics nhưng thay computation graph. Base case không chỉ tránh stack overflow; nó neo definition/proof vào một case đã biết.

## Worked Example: prove binary search correctness

Giả sử sorted array và target. Invariant: nếu target tồn tại trong array, trước mỗi iteration nó nằm trong current interval `[low,high]`.

Initialization: interval ban đầu chứa toàn array, nên invariant đúng.

Maintenance: lấy `mid`. Nếu `a[mid]<target`, sorted order cho mọi index `≤mid` không thể chứa target, nên update `low=mid+1` vẫn giữ mọi possible target positions. Case `a[mid]>target` tương tự cho upper half.

Termination: khi `low>high`, interval rỗng. Invariant khi đó nói nếu target tồn tại nó phải nằm trong empty set, contradiction; vậy target không tồn tại. Nếu equality gặp trước, return đúng index.

Runtime proof và correctness proof là hai layers khác nhau: recurrence cho `O(log n)` không tự chứng minh algorithm trả result đúng.
