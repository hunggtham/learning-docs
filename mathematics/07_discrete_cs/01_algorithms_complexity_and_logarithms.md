# Độ phức tạp thuật toán và ý nghĩa của logarithm

Phân tích độ phức tạp (Algorithmic complexity / 알고리즘 복잡도) hỏi resource usage tăng như thế nào khi input size `n` tăng. Nó không dự đoán exact milliseconds; nó mô tả scaling structure.

## Big-O

`f(n)=O(g(n))` nghĩa tồn tại constants `c,n_0` sao cho

```math
f(n)\le cg(n)
```

với mọi `n≥n_0`. Big-O là upper asymptotic bound, không phải dấu bằng thông thường.

`Θ(g(n))` cho tight asymptotic order; `Ω(g(n))` lower bound theo definition asymptotic tương ứng.

## Vì sao bỏ constants và lower-order terms?

Nếu

```math
T(n)=3n^2+10n+500
```

thì khi `n` lớn, ratio với `n^2` tiến gần 3. Structure growth chủ yếu quadratic, nên `Θ(n^2)`.

Điều này không nói constants không matter trong production. Hai algorithms cùng `O(n)` có thể chênh nhiều do cache, network I/O hoặc constants. Asymptotics và benchmarking trả lời câu hỏi khác nhau.

## O(1), O(n), O(n²)

Constant-time operation không phụ thuộc `n` trong chosen cost model. Linear scan nhìn worst-case proportional `n`. Nested loops độc lập qua `n×n` pairs thường quadratic.

Nhưng code shape không đủ; loops có thể halve range, skip data hoặc depend on sparse structure. Phải count operations theo state evolution.

## Logarithmic complexity

Nếu mỗi step giảm problem size bởi constant factor `b>1`:

```math
n,\frac nb,\frac n{b^2},\ldots
```

sau `k` steps còn roughly 1:

```math
\frac n{b^k}\approx1
```

nên

```math
k\approx\log_b n
```

Đây là source của logarithm trong binary search, balanced tree height và divide-by-factor processes.

## Binary search

Sorted array length `n`; mỗi comparison loại khoảng half remaining elements. Recurrence:

```math
T(n)=T(n/2)+O(1)
```

unroll:

```math
T(n)=O(\log n)
```

Log base thường bỏ trong Big-O vì change-of-base chỉ constant factor.

## Divide and conquer

Merge sort:

```math
T(n)=2T(n/2)+O(n)
```

Có `log n` levels; mỗi level total merge work `O(n)`, nên

```math
T(n)=O(n\log n)
```

Đây là một cách hiểu Master Theorem case cụ thể mà không học thuộc theorem trước.

## Exponential và factorial explosion

Brute force all subsets: `2^n`. All permutations: `n!`. Các rates này nhanh chóng vượt feasible limits.

Ví dụ `2^100` khoảng `1.27×10^30`; không thể “tối ưu code một chút” để enumerate hết trong thời gian thực tế. Mathematical growth rate giúp nhận ra cần đổi algorithm/model, không phải micro-optimization.

## Space complexity

Time không phải resource duy nhất. Memoization đổi memory để giảm repeated computation; BFS có thể giữ frontier lớn; external-memory algorithms tối ưu disk I/O hơn arithmetic count.

## Amortized analysis

Một operation đôi khi expensive nhưng trung bình trên sequence có thể cheap. Dynamic array append thỉnh thoảng resize `O(n)`, nhưng many appends có amortized `O(1)` vì resize hiếm và capacity grows geometrically.

## Mental Model

> Complexity là derivative-like question ở scale algorithmic: khi input tăng, resource tăng theo shape nào? Logarithm xuất hiện khi progress được đo bằng số lần có thể chia scale bởi constant factor.

## Common Misconceptions

`O(1)` không nghĩa “một CPU instruction”. Big-O không phải exact runtime. `O(log n)` không có nghĩa log được tính trong code; nó có thể xuất hiện từ repeated halving. Với small `n`, asymptotically worse algorithm đôi khi vẫn nhanh hơn do constants.
