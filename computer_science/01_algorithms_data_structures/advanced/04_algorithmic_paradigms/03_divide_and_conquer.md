# Divide and Conquer
**Chia để trị (Divide and Conquer / 분할 정복)**

Divide-and-conquer chia problem thành subproblems tương đối độc lập, giải chúng rồi combine.

```text
Divide → Conquer → Combine
```

## Recurrence

Nếu chia thành `a` subproblems size `n/b`, combine cost `f(n)`:

\[
T(n)=aT(n/b)+f(n)
\]

Merge sort:

\[
T(n)=2T(n/2)+O(n)=O(n\log n)
\]

Binary search:

\[
T(n)=T(n/2)+O(1)=O(\log n)
\]

## Khác DP ở đâu?

Divide-and-conquer phù hợp khi subproblems gần độc lập. Dynamic programming xuất hiện khi subproblems overlap và cùng state bị giải lại.

## Quickselect

Nếu chỉ cần phần tử nhỏ thứ `k`, không cần sort toàn bộ. Partition như quicksort rồi recurse vào đúng side chứa `k`. Expected time `O(n)`.

Điểm quan trọng: algorithm design nên bám actual goal. “Tôi biết sort” không có nghĩa sort là bước bắt buộc.

## Mental Model

> Divide-and-conquer giảm độ khó bằng cách chia problem theo structure sao cho mỗi level xử lý work có kiểm soát, còn số levels thường logarithmic.

## Recursion tree như cách nhìn cost

Với merge sort, level 0 xử lý `n`, level 1 có hai subproblems tổng size `n`, level 2 bốn subproblems tổng `n`. Có `log n` levels nên total `n log n`.

Với recurrence:

\[
T(n)=2T(n/2)+O(1)
\]

mỗi level có tổng work tăng theo số nodes, và leaves `Theta(n)`, nên total `Theta(n)`.

Không phải mọi “chia đôi” đều `n log n`; combine work quyết định.

## Closest pair idea

Trong computational geometry, closest pair có thể được giải `O(n log n)` bằng chia theo x-coordinate, recurse hai halves và chỉ kiểm tra một strip hẹp quanh median với ordering theo y. Đây cho thấy divide-and-conquer có thể dùng geometric proof để giảm cross-boundary candidates từ quadratic xuống linear mỗi level.

## Karatsuba multiplication

Nhân hai số lớn split thành high/low halves. Naive cần 4 multiplications subproblems; Karatsuba dùng algebra để giảm còn 3:

\[
T(n)=3T(n/2)+O(n)
\]

nên khoảng:

\[
O(n^{\log_2 3}) \approx O(n^{1.585})
\]

Insight: đôi khi improvement đến từ **giảm số subproblems**, không chỉ giảm size.

## Parallelism

Independent subproblems của divide-and-conquer có thể chạy song song. Merge step hoặc shared memory bandwidth có thể thành bottleneck. Đây là connection tự nhiên với fork-join frameworks.

## Khi divide-and-conquer không phù hợp

Nếu subproblems overlap mạnh, pure recursion lặp work và DP/memoization tốt hơn. Nếu combine cost quá lớn, chia nhỏ không cứu được asymptotics. Phải nhìn recurrence, không nhìn hình thức recursive code.
