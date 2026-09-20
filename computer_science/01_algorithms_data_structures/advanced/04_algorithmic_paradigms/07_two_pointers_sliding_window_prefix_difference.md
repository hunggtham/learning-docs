# Two Pointers, Sliding Window, Prefix Sum và Difference Techniques  
**투 포인터, 슬라이딩 윈도우, 누적합, 차분**

Nhóm kỹ thuật này cùng khai thác một ý tưởng: khi hai subproblems liên tiếp khác nhau rất ít, **đừng tính lại từ đầu**.

## Two pointers trên sorted data

Bài two-sum trên sorted array dùng `L` và `R`.

Nếu:

\[
a[L]+a[R] < target
\]

thì tăng `L` là safe vì với `a[L]` hiện tại, ghép với bất kỳ index nhỏ hơn `R` chỉ cho sum còn nhỏ hơn. Ta loại cả một vùng candidate bằng sorted invariant.

Đây là proof, không phải heuristic.

## Fast/slow pointers

Trên linked list, hai pointers với tốc độ khác nhau dùng cho cycle detection và midpoint. Trên arrays, read/write pointers dùng để compact dữ liệu in-place.

Ví dụ remove duplicates sorted array:

```java
int write = 0;
for (int read = 0; read < a.length; read++) {
    if (read == 0 || a[read] != a[read - 1]) {
        a[write++] = a[read];
    }
}
```

`read` khám phá input; `write` đánh dấu boundary của output hợp lệ.

## Fixed sliding window

Window length `k`. Nếu sum hiện tại là `S`, khi dịch một bước:

\[
S' = S - a[L] + a[R+1]
\]

Mỗi element vào window một lần và ra một lần; total `O(n)`.

## Variable sliding window

Kỹ thuật chỉ đúng khi predicate có monotonic behavior phù hợp. Ví dụ với positive numbers, nếu sum quá lớn, tăng left làm sum không tăng; nếu sum chưa đủ, tăng right làm sum không giảm.

Nếu có negative numbers, monotonicity có thể mất và sliding window đơn giản không còn đúng. Đây là một common misconception quan trọng.

## Prefix sum

Prefix sum đổi repeated range aggregation thành subtraction của hai prefix states:

\[
range(L,R)=P[R+1]-P[L]
\]

Ở 2D:

\[
S(r_1,c_1,r_2,c_2)
\]

được tính bằng inclusion-exclusion của bốn prefix rectangles. Đây là connection trực tiếp với combinatorial inclusion-exclusion idea.

## Difference array

Difference representation lưu thay đổi giữa neighbors thay vì absolute values. Range update trở thành sửa hai boundaries; prefix accumulation khôi phục values cuối.

## Monotonic deque

Sliding window maximum cần biết max của window động. Recompute max mỗi window là `O(nk)`. Deque giữ candidate indices với values giảm dần.

Khi thêm `a[r]`, mọi tail có value `<= a[r]` không thể trở thành max trong tương lai trước `a[r]`, vì `a[r]` mới hơn và không nhỏ hơn. Ta loại chúng vĩnh viễn.

Mỗi index push/pop tối đa một lần → `O(n)`.

## Mental Model

> Các kỹ thuật này thắng bằng cách xác định **phần nào của trạng thái cũ vẫn còn đúng khi boundary dịch chuyển**, rồi chỉ cập nhật phần chênh lệch.
